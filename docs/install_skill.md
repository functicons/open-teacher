# Use Open Teacher as an agent skill

The installable [open-teacher skill](../skills/open-teacher/SKILL.md) brings the
workflow into an existing agent setup. It includes the draft standard, shared
instructions, optional teaching methods, and blank templates. It works without
the original repository after installation. No agent service or model is included.

## Install the complete folder

From a clone of this repository, copy `skills/open-teacher/` into one location:

| Agent | Personal installation | Project installation |
| --- | --- | --- |
| Codex | `~/.agents/skills/open-teacher/` | `.agents/skills/open-teacher/` |
| Claude Code | `~/.claude/skills/open-teacher/` | `.claude/skills/open-teacher/` |

For example, run this from the repository root for Codex:

```sh
python3 -c 'import shutil; from pathlib import Path; shutil.copytree("skills/open-teacher", Path.home() / ".agents/skills/open-teacher")'
```

For Claude Code, substitute `.claude/skills/open-teacher` for the destination.
Python's `copytree` refuses an existing destination. Inspect an existing skill
before replacing it; do not merge releases blindly. Copy the entire directory,
including hidden files, rather than just `SKILL.md`. These commands install only
the skill; they do not create or relocate learning records.

Installation paths follow the official [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
and [Claude Code skill documentation](https://code.claude.com/docs/en/skills),
checked 2026-09-19. Start a fresh agent session after installation and verify that
`open-teacher` is available. Automatic selection is enabled by default; host
permissions and configuration still apply.

## Use it

Ask your agent:

> Use the open-teacher skill. Set up a new learning workspace at ~/learning/my_notes,
> then help me understand a topic I choose.

Or point it to an existing workspace:

> Use Open Teacher in ~/learning/my_notes. Continue from the saved learning context.

The setup helper requires Python 3.9+, refuses existing destinations, and checks
for required instructions, the ignore file, and starter records before writing; the skill
also describes manual setup. Teaching itself does not require Python. The agent
reads the shared instructions and records relevant checkpoints as you converse.
You can switch topics freely or ask it not to record.

Install the same skill for another agent and give it access to the **same current
learning directory**. Memory belongs there, outside the installed skill. Keep
separate directories for different learners. Skills neither synchronize files nor
give an agent access that its host has denied.

## Maintain the bundle

`skills/open-teacher/SKILL.md` is the integration entry point. The files under
`references/workspace/` are generated copies, not another teaching policy.
Edit the root `PROTOCOL.md`, `metadata/`, `.gitignore`, or `LICENSE`, then run:

```sh
python3 scripts/build-skill.py
python3 scripts/build-skill.py --check
python3 -m unittest discover -s tests
```

The builder only includes public framework files. It never copies `user_data/`,
Git history, installed skills, or project artwork. Existing workspaces are not
upgraded automatically; their version and customized instructions remain in effect.

`metadata/skills/` contains optional teaching techniques such as visualization;
the top-level `skills/open-teacher/` installs the overall workflow.

## Verification scope

The local tests cover installing a detached bundle, creating a neutral workspace,
resolving bundled instruction links, preserving existing files on a repeated
setup attempt, refusing records inside the skill, and a non-mutating dry run.
Missing required bundle files are rejected before creating a destination in both
normal and dry-run modes, with the missing paths included in the error.
They do not establish successful teaching or automatic discovery in either agent.
Use the [handoff checklist](../metadata/checks/memory_handoff.md) for a real
cross-agent behavioral trial with synthetic learning records.
