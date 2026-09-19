---
name: open-teacher
description: Use Open Teacher to learn across arbitrary topics with persistent, user-owned memory, resume saved learning across agents, or set up a learning workspace. Use when the user wants this learning-memory workflow; ordinary coding questions do not automatically authorize a personal learning journal.
---

# Open Teacher

Open Teacher is a memory and teaching-continuity standard. You supply the teaching.
This skill connects you to the shared instructions; it does not define a separate
teaching policy. Skill-relative paths below resolve beside this `SKILL.md`, never
against the shell's current directory.

## Find the learner's workspace

Use the user's explicit workspace path first. Otherwise inspect the current
workspace's entry point for Open Teacher instructions and a record-location map.
Do not assume every `AGENTS.md` is an Open Teacher workspace. If the destination
is ambiguous, ask for the learning directory rather than searching unrelated
personal folders or silently creating another history.

For an existing Open Teacher workspace, read its declared protocol and shared
instructions. Preserve its layout and customizations. Do not install the bundled
framework over it. This bundle implements draft 0.1; disclose an unsupported
version or mapping instead of claiming a complete handoff.

## Start a new workspace

If no workspace exists and setup is requested, choose a new directory with the
user. Keep it outside this installed skill, so skill upgrades cannot erase memory.
The helper uses Python 3.9+ and refuses any existing destination:

```sh
python3 /absolute/path/to/open-teacher/scripts/init-workspace.py /chosen/new/directory --dry-run
python3 /absolute/path/to/open-teacher/scripts/init-workspace.py /chosen/new/directory
```

Resolve the actual installed skill path before running these commands. The helper
copies the bundled standard, shared metadata, neutral starter records, and local
agent entry points. It does not initialize Git, install an agent, or contact a service.
Without Python, copy [the bundled framework](references/workspace/) and its blank
`metadata/templates/initial_user_data/` to a new workspace as `user_data/`; add an
`AGENTS.md` linking `PROTOCOL.md` and `metadata/teacher_instructions.md`, and a
`CLAUDE.md` containing `@AGENTS.md`. Preserve the bundled `.gitignore`.

## Teach and continue

Before teaching, read the workspace's `metadata/teacher_instructions.md` and
`PROTOCOL.md` (or their declared equivalents). The bundled
[shared instructions](references/workspace/metadata/teacher_instructions.md) and
[draft specification](references/workspace/PROTOCOL.md) are the reference for new
workspaces, not authority to override an existing workspace's instructions.

Follow the startup, selective retrieval, checkpoint, evidence, and continuation
rules there. Teach the current question, including a topic change. Keep personal
records in the learning workspace, never in this skill. If the user declines
recording, honor that choice. Installation alone is not permission to publish,
commit, contact others, or alter the reusable framework.

When switching agents, point the next agent to the same current workspace and its
entry point. Skill installation does not synchronize files. Record failed reads
or writes honestly; do not invent prior learning. For handoff evaluation, use the
workspace's [checklist](references/workspace/metadata/checks/memory_handoff.md)
with isolated synthetic records.
