#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

LINK_RE = re.compile(r'\[\[([^\]|#]+)')

def frontmatter(text):
    if not text.startswith('---\n'):
        return {}
    end = text.find('\n---', 4)
    if end < 0:
        return {}

    out = {}
    key = None

    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue

        if re.match(r'^\s*-\s+', raw) and key:
            out.setdefault(key, []).append(
                re.sub(r'^\s*-\s+', '', raw).strip().strip('"\'')
            )
            continue

        m = re.match(r'^([^:#][^:]*):\s*(.*)$', raw)

        if m:
            key, val = m.group(1).strip(), m.group(2).strip()

            if val == '':
                out[key] = []
            else:
                out[key] = val.strip('"\'')

    return out


def main():
    ap = argparse.ArgumentParser(
        description='Create a lightweight structural index of an Obsidian Vault.'
    )

    ap.add_argument('vault')
    ap.add_argument('-o', '--output')

    args = ap.parse_args()

    root = Path(args.vault).expanduser().resolve()

    if not root.is_dir():
        raise SystemExit('Vault path is not a directory')

    records = []
    bases = []

    for p in root.rglob('*'):
        rel = p.relative_to(root)

        if '.obsidian' in rel.parts or '.git' in rel.parts or not p.is_file():
            continue

        if p.suffix == '.base':
            bases.append(str(rel))
            continue

        if p.suffix.lower() != '.md':
            continue

        try:
            text = p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            text = p.read_text(encoding='utf-8', errors='replace')

        props = frontmatter(text)

        records.append({
            'path': str(rel),
            'title': props.get('title') or p.stem,
            'properties': props,
            'wikilinks': sorted(
                set(x.strip() for x in LINK_RE.findall(text))
            )
        })

    result = {
        'vault_root': str(root),
        'has_obsidian_dir': (root / '.obsidian').is_dir(),
        'is_git_repo': (root / '.git').exists(),
        'base_files': sorted(bases),
        'markdown_count': len(records),
        'files': records
    }

    data = json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )

    if args.output:
        Path(args.output).write_text(data, encoding='utf-8')
    else:
        print(data)


if __name__ == '__main__':
    main()
