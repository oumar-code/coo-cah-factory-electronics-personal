#!/usr/bin/env python3
"""
IFC GUID Extraction Script — Coo-Cah Personal Electronics Factory
==================================================================
Pre-staged extraction workflow for Pass 7 (BIM Anchors).

Usage
-----
  # Audit pending tokens without an IFC file:
  python extract-ifc-guids.py --md-only docs/bim/asset-anchors.md

  # Match tokens against a delivered IFC file (report only):
  python extract-ifc-guids.py factory.ifc

  # Match and apply to the Markdown file in-place:
  python extract-ifc-guids.py factory.ifc --apply-to docs/bim/asset-anchors.md

  # Apply even when some tokens are unmatched (manual follow-up required):
  python extract-ifc-guids.py factory.ifc --apply-to docs/bim/asset-anchors.md --force

Requirements
------------
  pip install ifcopenshell

Background
----------
asset-anchors.md holds 142 registered assets.  Each row carries an IFC GUID
column whose value is currently a controlled pending-status tag of the form:

    {GUID-SMT-L1-01-REPLACE}

The tag suffix (e.g. ``SMT-L1-01``) is derived from the DT asset ID
(e.g. ``DT-SMT-L1-01``) by stripping the leading ``DT-`` prefix.

Matching strategy
-----------------
1. Parse all ``{GUID-<TOKEN>-REPLACE}`` tokens from the Markdown file.
2. For each IfcProduct in the model, inspect the ``Name``, ``Tag``, and
   ``Description`` attributes.  Attempt a match by:
   a. Exact substring match of the normalised token in the normalised field.
   b. If no match on Name, fall through to Tag then Description.
3. Classify each token as MATCHED, AMBIGUOUS (>1 candidate), or UNMATCHED.
4. With --apply-to, refuse to write if AMBIGUOUS tokens exist unless --force
   is supplied.  UNMATCHED tokens are always left as-is in the Markdown.

After running --apply-to, verify the result by counting remaining
{GUID-...-REPLACE} tokens and checking the DT platform floor-model import.
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import ifcopenshell  # type: ignore[import]
    _IFCOPENSHELL_AVAILABLE = True
except ImportError:
    _IFCOPENSHELL_AVAILABLE = False

TOKEN_RE = re.compile(r"\{GUID-([A-Z0-9\-]+)-REPLACE\}")


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def parse_tokens(md_path: Path) -> list:
    """Return a sorted list of unique GUID token suffixes in the Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    return sorted(set(TOKEN_RE.findall(text)))


# ---------------------------------------------------------------------------
# IFC helpers
# ---------------------------------------------------------------------------

def _require_ifcopenshell() -> None:
    if not _IFCOPENSHELL_AVAILABLE:
        sys.exit(
            "ERROR: ifcopenshell is not installed.\n"
            "       Install it with:  pip install ifcopenshell"
        )


def extract_ifc_elements(ifc_path: Path) -> list:
    """Return a list of dicts with keys: global_id, type, name, tag, description."""
    _require_ifcopenshell()
    ifc = ifcopenshell.open(str(ifc_path))
    elements = []
    for product in ifc.by_type("IfcProduct"):
        elements.append({
            "global_id":   product.GlobalId,
            "type":        product.is_a(),
            "name":        (getattr(product, "Name",        "") or "").strip(),
            "tag":         (getattr(product, "Tag",         "") or "").strip(),
            "description": (getattr(product, "Description", "") or "").strip(),
        })
    return elements


# ---------------------------------------------------------------------------
# Matching
# ---------------------------------------------------------------------------

def _normalise(s: str) -> str:
    """Lower-case and strip hyphens, underscores, and whitespace."""
    return re.sub(r"[-_\s]", "", s).lower()


def match_tokens(tokens: list, elements: list) -> dict:
    """
    For each token return a list of matching IFC element dicts.
    Empty list  → UNMATCHED
    One entry   → MATCHED
    >1 entries  → AMBIGUOUS
    """
    matches: dict = {t: [] for t in tokens}
    norm_tokens = {t: _normalise(t) for t in tokens}

    for element in elements:
        fields = [element["name"], element["tag"], element["description"]]
        for token, norm_token in norm_tokens.items():
            for field in fields:
                if norm_token and norm_token in _normalise(field):
                    existing_ids = {e["global_id"] for e in matches[token]}
                    if element["global_id"] not in existing_ids:
                        matches[token].append(element)
                    break  # one match per element per token is enough

    return matches


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(tokens: list, matches: dict) -> bool:
    """Print a formatted summary table. Return True if problems exist."""
    col_token = 36
    col_status = 12
    col_guid = 28

    header = (
        f"{'TOKEN':<{col_token}} "
        f"{'STATUS':<{col_status}} "
        f"{'IFC GUID':<{col_guid}} "
        f"IFC Name"
    )
    print(f"\n{header}")
    print("-" * (col_token + col_status + col_guid + 3 + 40))

    has_problems = False
    for token in tokens:
        candidates = matches[token]
        if len(candidates) == 1:
            status = "MATCHED"
            guid   = candidates[0]["global_id"]
            name   = candidates[0]["name"] or "(no name)"
        elif len(candidates) == 0:
            status = "UNMATCHED"
            guid   = "—"
            name   = "—"
            has_problems = True
        else:
            status = "AMBIGUOUS"
            guid   = f"({len(candidates)} candidates)"
            name   = " / ".join(c["name"] for c in candidates[:3])
            has_problems = True

        print(
            f"{token:<{col_token}} "
            f"{status:<{col_status}} "
            f"{guid:<{col_guid}} "
            f"{name}"
        )

    n_matched   = sum(1 for c in matches.values() if len(c) == 1)
    n_unmatched = sum(1 for c in matches.values() if len(c) == 0)
    n_ambiguous = sum(1 for c in matches.values() if len(c) > 1)
    print(
        f"\nSummary: {n_matched} matched | {n_unmatched} unmatched | "
        f"{n_ambiguous} ambiguous | {len(tokens)} total tokens"
    )
    return has_problems


# ---------------------------------------------------------------------------
# Apply replacements
# ---------------------------------------------------------------------------

def apply_replacements(md_path: Path, matches: dict, force: bool = False) -> None:
    """Rewrite the Markdown file replacing matched tokens with real GUIDs."""
    n_problems = sum(1 for c in matches.values() if len(c) != 1)
    if n_problems and not force:
        sys.exit(
            f"\nERROR: {n_problems} token(s) are unmatched or ambiguous.\n"
            "       Resolve them manually, or re-run with --force to apply\n"
            "       only cleanly matched tokens and leave the rest as-is."
        )

    text = md_path.read_text(encoding="utf-8")
    replaced = 0
    for token, candidates in matches.items():
        if len(candidates) == 1:
            placeholder = "{GUID-" + token + "-REPLACE}"
            guid = candidates[0]["global_id"]
            if placeholder in text:
                text = text.replace(placeholder, guid)
                replaced += 1

    md_path.write_text(text, encoding="utf-8")
    print(f"\nApplied {replaced} replacement(s) → {md_path}")

    remaining = len(TOKEN_RE.findall(text))
    if remaining:
        print(f"WARNING: {remaining} token(s) remain in the file (unmatched or forced-skip).")
    else:
        print("All pending GUID tokens resolved.  Remove §1.1 status control note when verified.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Extract IFC GlobalIds and optionally apply them to asset-anchors.md.\n"
            "See module docstring for full usage details."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "ifc_file",
        nargs="?",
        help="Path to the contractor-delivered .ifc file",
    )
    parser.add_argument(
        "--apply-to",
        metavar="MARKDOWN_FILE",
        help="Markdown file to update in-place (e.g. docs/bim/asset-anchors.md)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Apply clean matches even when some tokens are unmatched or ambiguous",
    )
    parser.add_argument(
        "--md-only",
        metavar="MARKDOWN_FILE",
        help=(
            "Parse pending tokens from a Markdown file without loading an IFC model "
            "(useful for auditing how many tokens remain)"
        ),
    )
    args = parser.parse_args()

    # --- Token-audit mode (no IFC file needed) ---
    if args.md_only:
        md_path = Path(args.md_only)
        if not md_path.exists():
            sys.exit(f"ERROR: File not found: {md_path}")
        tokens = parse_tokens(md_path)
        print(f"Found {len(tokens)} pending GUID token(s) in {md_path}:")
        for t in tokens:
            print(f"  {{GUID-{t}-REPLACE}}")
        return

    # --- Normal mode: IFC file required ---
    if not args.ifc_file:
        parser.error("ifc_file is required unless --md-only is specified.")

    ifc_path = Path(args.ifc_file)
    if not ifc_path.exists():
        sys.exit(f"ERROR: IFC file not found: {ifc_path}")

    md_path = Path(args.apply_to) if args.apply_to else None
    if md_path and not md_path.exists():
        sys.exit(f"ERROR: Markdown file not found: {md_path}")

    # Determine where to read tokens from
    default_md = Path(__file__).parent.parent / "docs" / "bim" / "asset-anchors.md"
    token_source = md_path if md_path else default_md
    if not token_source.exists():
        sys.exit(
            f"ERROR: Cannot locate asset-anchors.md at {token_source}.\n"
            "       Pass --apply-to <path> explicitly."
        )

    print(f"Parsing GUID tokens from : {token_source}")
    tokens = parse_tokens(token_source)
    print(f"Found {len(tokens)} pending token(s).\n")

    print(f"Loading IFC model        : {ifc_path}")
    elements = extract_ifc_elements(ifc_path)
    print(f"Found {len(elements)} IfcProduct element(s) in model.\n")

    matches = match_tokens(tokens, elements)
    has_problems = report(tokens, matches)

    if md_path:
        apply_replacements(md_path, matches, force=args.force)
    elif not has_problems:
        print(
            f"\nAll tokens matched cleanly.  "
            f"Re-run with --apply-to {token_source} to write replacements."
        )


if __name__ == "__main__":
    main()
