"""Exercise the standalone skill in synthetic, disposable workspaces."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.skill = self.base / 'installed/open-teacher'
        shutil.copytree(ROOT / 'skills/open-teacher', self.skill)
        self.destination = self.base / 'learning'

    def run_setup(self, destination: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.skill / 'scripts/init-workspace.py'), str(destination), *args],
            cwd=self.base, text=True, capture_output=True, check=False,
        )

    def test_detached_install_creates_neutral_portable_workspace(self) -> None:
        result = self.run_setup(self.destination)
        self.assertEqual(result.returncode, 0, result.stderr)
        starter = self.skill / 'references/workspace/metadata/templates/initial_user_data'
        expected = {p.relative_to(starter): p.read_bytes() for p in starter.rglob('*') if p.is_file()}
        data = self.destination / 'user_data'
        self.assertEqual(expected, {p.relative_to(data): p.read_bytes() for p in data.rglob('*') if p.is_file()})
        self.assertEqual((self.destination / 'CLAUDE.md').read_text(), '@AGENTS.md\n')
        self.assertIn('/user_data/', (self.destination / '.gitignore').read_text())
        self.assertFalse((self.destination / '.git').exists())
        self.assertEqual((self.destination / 'PROTOCOL.md').read_bytes(), (ROOT / 'PROTOCOL.md').read_bytes())
        for file in [self.destination / 'AGENTS.md', self.destination / 'PROTOCOL.md', self.destination / 'metadata/teacher_instructions.md']:
            for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((file.parent / link.split('#')[0]).exists(), f'{file}: {link}')

    def test_incomplete_bundle_is_rejected_before_creating_destination(self) -> None:
        missing_paths = (
            'PROTOCOL.md', '.gitignore', 'metadata/teacher_instructions.md',
            'metadata/skills/index.md', 'metadata/checks/memory_handoff.md',
            'metadata/templates/initial_user_data/memory/learner.md',
            'metadata/templates/initial_user_data/memory/index.md',
            'metadata/templates/initial_user_data/knowledge/index.md',
            'metadata/templates/initial_user_data/projects/index.md',
        )
        complete = self.skill
        for index, missing in enumerate(missing_paths):
            with self.subTest(missing=missing):
                self.skill = self.base / f'incomplete_{index}'
                for source in complete.rglob('*'):
                    relative = source.relative_to(complete)
                    if source.is_file() and relative.as_posix() != f'references/workspace/{missing}':
                        target = self.skill / relative
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(source, target)
                for mode, options in enumerate([(), ('--dry-run',)]):
                    self.destination = self.base / f'learning_{index}_{mode}'
                    result = self.run_setup(self.destination, *options)
                    self.assertNotEqual(result.returncode, 0, result.stdout)
                    self.assertIn(missing, result.stderr)
                    self.assertFalse(self.destination.exists())
        self.skill = complete

    def test_dry_run_has_no_filesystem_effect(self) -> None:
        result = self.run_setup(self.destination, '--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.destination.exists())

    def test_existing_workspace_remains_byte_identical(self) -> None:
        self.assertEqual(self.run_setup(self.destination).returncode, 0)
        (self.destination / 'user_data/memory/learner.md').write_text('Synthetic learner: preserve me.\n')
        before = {p.relative_to(self.destination): p.read_bytes() for p in self.destination.rglob('*') if p.is_file()}
        self.assertNotEqual(self.run_setup(self.destination).returncode, 0)
        after = {p.relative_to(self.destination): p.read_bytes() for p in self.destination.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_cannot_store_memory_inside_installed_skill(self) -> None:
        destination = self.skill / 'personal'
        self.assertNotEqual(self.run_setup(destination).returncode, 0)
        self.assertFalse(destination.exists())

    def test_existing_destination_symlink_is_not_followed(self) -> None:
        self.destination.symlink_to(self.base / 'absent')
        self.assertNotEqual(self.run_setup(self.destination).returncode, 0)
        self.assertFalse((self.base / 'absent').exists())

    def test_builder_excludes_personal_data_and_detects_stale_sources(self) -> None:
        source = self.base / 'source'
        source.mkdir()
        for name in ('PROTOCOL.md', 'LICENSE', '.gitignore'):
            shutil.copyfile(ROOT / name, source / name)
        shutil.copytree(ROOT / 'metadata', source / 'metadata')
        (source / 'scripts').mkdir()
        shutil.copyfile(ROOT / 'scripts/build-skill.py', source / 'scripts/build-skill.py')
        (source / 'user_data').mkdir()
        (source / 'user_data/private.md').write_text('SYNTHETIC_PRIVATE_CANARY')
        command = [sys.executable, str(source / 'scripts/build-skill.py')]
        built = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(built.returncode, 0, built.stderr)
        bundle = source / 'skills/open-teacher/references/workspace'
        self.assertFalse((bundle / 'user_data').exists())
        self.assertFalse(any(b'SYNTHETIC_PRIVATE_CANARY' in p.read_bytes() for p in bundle.rglob('*') if p.is_file()))
        canonical = source / 'metadata/teacher_instructions.md'
        canonical.write_text(canonical.read_text() + '\nSynthetic framework revision.\n')
        self.assertNotEqual(subprocess.run(command + ['--check'], capture_output=True).returncode, 0)
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        self.assertEqual(subprocess.run(command + ['--check'], capture_output=True).returncode, 0)

    def test_generated_bundle_matches_canonical_sources(self) -> None:
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/build-skill.py'), '--check'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
