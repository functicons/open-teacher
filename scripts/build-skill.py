#!/usr/bin/env python3
"""Refresh generated skill references from canonical sources, or check for drift.

Usage: python3 scripts/build-skill.py [--check]
Only public metadata, PROTOCOL.md, LICENSE, and .gitignore are bundled.
"""
import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = root / 'skills/open-teacher/references/workspace'
    files = [root / name for name in ('PROTOCOL.md', 'LICENSE', '.gitignore')]
    for source in sorted((root / 'metadata').rglob('*')):
        if source.is_symlink():
            parser.error(f'Refusing symlink in public metadata: {source}')
        if source.is_file() and (source.suffix == '.md' or source.name == '.gitkeep'):
            files.append(source)
    expected = {p.relative_to(root) for p in files}
    actual = {p.relative_to(target) for p in target.rglob('*') if p.is_file()}
    extra = actual - expected
    if extra:
        parser.error(f'Unexpected bundled files; inspect before removing: {sorted(map(str, extra))}')
    drift = []
    for source in files:
        destination = target / source.relative_to(root)
        if source.is_symlink() or destination.is_symlink():
            parser.error(f'Refusing symlink: {source.relative_to(root)}')
        if not destination.is_file() or destination.read_bytes() != source.read_bytes():
            drift.append(str(source.relative_to(root)))
            if not args.check:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(source.read_bytes())
    if args.check and drift:
        parser.error(f'Stale bundle; run scripts/build-skill.py: {drift}')
    print(f'{len(files)} bundled files verified' if args.check else f'Updated {len(drift)} bundled files')


if __name__ == '__main__':
    main()
