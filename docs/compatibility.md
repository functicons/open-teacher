# Compatibility and verification

Open Teacher requires an agent that can read shared instructions, retrieve local
files, and write authorized records. It does not require a specific model vendor.

| Client or environment | Entry point | Status in this distribution |
| --- | --- | --- |
| Codex | Root `AGENTS.md` | Entry point provided; fresh draft-0.1 behavioral trial not yet recorded |
| Claude Code | Root `CLAUDE.md` imports `AGENTS.md` | Adapter provided; fresh draft-0.1 behavioral trial not yet recorded |
| Other file-capable agents | Explicitly read `AGENTS.md` | Designed to be portable; validate in the actual host |
| Chat-only interfaces | Manually supply instructions and relevant records, save returned updates | Partial manual workflow; no automatic local persistence promised |

This table describes the intended integration, not verified product configuration
instructions. Use the host's own documentation for permissions and setup. Switching
models inside an app and switching independent agents are different operations;
the latter requires access to the same current workspace.

## Before claiming a successful handoff

Use the [behavioral checklist](../metadata/checks/memory_handoff.md). In addition:

1. Have one agent save a short lesson, including an unfinished question and the
   actual help given. Start a fresh second agent and resume from the files alone.
2. Ask an unrelated question. Confirm it is answered without mandatory review,
   forced course creation, or treating the old question as a prerequisite.
3. Correct a learning claim, then check that a fresh agent uses the correction.
4. Add a project-only milestone; verify that lesson continuation stays intact.
5. Initialize from the blank distribution and confirm no prior learner is invented.

Use synthetic data or records you are authorized to share with the providers.
Keep test outputs out of real learner evidence. Report the tested protocol version,
host versions, prompts, observations and limitations. One passing trial is not a
reliability estimate or proof of educational effectiveness.

## Structural checks

Check Markdown links, relative paths, required entry points, neutral starter data,
and the Git ignore rule. Confirm generated images render and include useful alt
text. These checks cannot establish that an agent will obey the instructions.

There are no package installation steps or runtime dependencies for the core
protocol. Individual artifact-generation tools may need separate setup.
