#!/usr/bin/env python3
"""Create a new learning directory from this skill; existing paths are refused.

Usage: python3 init-workspace.py DESTINATION [--dry-run]
Requires Python 3.9+; no external dependencies or network calls.
"""
import argparse
from pathlib import Path
import shutil


REQUIRED_BUNDLE_FILES = (
    'PROTOCOL.md',
    '.gitignore',
    'metadata/teacher_instructions.md',
    'metadata/skills/index.md',
    'metadata/checks/memory_handoff.md',
    'metadata/templates/initial_user_data/memory/learner.md',
    'metadata/templates/initial_user_data/memory/index.md',
    'metadata/templates/initial_user_data/knowledge/index.md',
    'metadata/templates/initial_user_data/projects/index.md',
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    skill = Path(__file__).resolve().parents[1]
    destination = args.destination.expanduser().absolute()
    if destination.exists() or destination.is_symlink():
        parser.error(f'Destination already exists; nothing changed: {destination}')
    if destination.resolve().is_relative_to(skill):
        parser.error('Learning records must be outside the installed skill.')
    source = skill / 'references/workspace'
    missing = [name for name in REQUIRED_BUNDLE_FILES if not (source / name).is_file()]
    if missing:
        parser.error('Incomplete skill bundle; missing: ' + ', '.join(missing)
                     + '. Reinstall the full skill directory; nothing changed.')
    if any(p.is_symlink() for p in source.rglob('*')):
        parser.error('The framework bundle must contain regular files, not symlinks.')
    print(f'Create reference framework and neutral user_data in {destination}')
    if args.dry_run:
        return
    shutil.copytree(source, destination)
    shutil.copytree(destination / 'metadata/templates/initial_user_data', destination / 'user_data')
    (destination / 'AGENTS.md').write_text(
        '# Open Teacher workspace\n\n'
        'Read [the draft specification](PROTOCOL.md) and '
        '[shared teacher instructions](metadata/teacher_instructions.md) before teaching.\n'
        'Resolve workspace paths from this directory. Personal records live in `user_data/`.\n',
        encoding='utf-8',
    )
    (destination / 'CLAUDE.md').write_text('@AGENTS.md\n', encoding='utf-8')
    print('Ready. Open this directory with your agent and read AGENTS.md.')


if __name__ == '__main__':
    main()
