#!/usr/bin/env python3

import argparse, json, re
from pathlib import Path

ALLOWED = {
    'unread',
    'skimmed',
    'studied',
    'reproduced'
}

FIELDS = {
    'title',
    'year',
    'url',
    'status',
    'rating',
    'topics',
    'concepts'
}


def parse(text):
    if not text.startswith('---\n'):
        return None

    end = text.find('\n---', 4)

    if end < 0:
        return None

    fm = text[4:end]
    out = {}
    key = None

    for raw in fm.splitlines():

        if re.match(r'^\s*-\s+', raw) and key:
            out.setdefault(key, []).append(
                re.sub(r'^\s*-\s+', '', raw)
                .strip()
                .strip('"\'')
            )
            continue

        m = re.match(
            r'^([^:#][^:]*):\s*(.*)$',
            raw
        )

        if m:
            key, val = (
                m.group(1).strip(),
                m.group(2).strip()
            )

            out[key] = (
                []
                if val == ''
                else val.strip('"\'')
            )

    return out


def main():
    ap = argparse.ArgumentParser(
        description='Validate Obsidian paper-note properties without modifying files.'
    )

    ap.add_argument('path')

    args = ap.parse_args()
    root = Path(args.path)

    files = (
        [root]
        if root.is_file()
        else list(root.rglob('*.md'))
    )

    issues = []
    checked = 0

    for p in files:

        if '.obsidian' in p.parts:
            continue

        text = p.read_text(
            encoding='utf-8',
            errors='replace'
        )

        fm = parse(text)

        if fm is None:
            continue

        if not (set(fm) & FIELDS):
            continue

        checked += 1

        for f in (
            'title',
            'year',
            'url',
            'status',
            'rating',
            'topics',
            'concepts'
        ):
            if f not in fm:
                issues.append({
                    'file': str(p),
                    'field': f,
                    'issue': 'missing'
                })

        st = fm.get('status')

        if (
            isinstance(st, str)
            and st
            and st not in ALLOWED
        ):
            issues.append({
                'file': str(p),
                'field': 'status',
                'issue': 'invalid',
                'value': st
            })

        r = fm.get('rating')

        if isinstance(r, str) and r:
            try:
                rv = int(r)
                valid = 1 <= rv <= 5
            except ValueError:
                valid = False

            if not valid:
                issues.append({
                    'file': str(p),
                    'field': 'rating',
                    'issue': 'must be integer 1-5 or empty',
                    'value': r
                })

    print(json.dumps(
        {
            'checked': checked,
            'issues': issues
        },
        ensure_ascii=False,
        indent=2
    ))


if __name__ == '__main__':
    main()
