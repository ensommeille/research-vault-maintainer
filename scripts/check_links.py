#!/usr/bin/env python3

import argparse, json, re
from pathlib import Path

LINK_RE = re.compile(r'\[\[([^\]|#]+)')


def main():
    ap = argparse.ArgumentParser(
        description='Report unresolved Obsidian wikilink candidates; never repairs them.'
    )

    ap.add_argument('vault')

    args = ap.parse_args()
    root = Path(args.vault).resolve()

    notes = []

    for p in root.rglob('*.md'):
        rel = p.relative_to(root)

        if '.obsidian' in rel.parts:
            continue

        notes.append(p)

    stems = {
        p.stem.casefold(): p
        for p in notes
    }

    unresolved = []

    for p in notes:
        text = p.read_text(
            encoding='utf-8',
            errors='replace'
        )

        for target in sorted(
            set(
                x.strip()
                for x in LINK_RE.findall(text)
            )
        ):
            leaf = Path(target).name.casefold()

            if leaf not in stems:
                unresolved.append({
                    'source': str(p.relative_to(root)),
                    'target': target
                })

    print(json.dumps(
        {
            'unresolved_candidates': unresolved
        },
        ensure_ascii=False,
        indent=2
    ))


if __name__ == '__main__':
    main()
