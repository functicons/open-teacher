# How Open Teacher works

Open Teacher is the standard; this repository also includes one reference
implementation. The agent provides the conversation and reasoning. Ordinary files preserve the
useful context. The [protocol](../PROTOCOL.md) supplies a common agreement about
reading and maintaining those files; the [shared instructions](../metadata/teacher_instructions.md)
implement it for this repository.

## Three layers

| Layer | Purpose | Changes when |
| --- | --- | --- |
| Protocol | Common evidence, ownership, and handoff requirements | The community intentionally revises the contract |
| Reusable methods | Operational instructions, teaching skills, optional templates | A generalized improvement is approved |
| Personal journey | Profile, history, knowledge, projects and artifacts | A meaningful learning event or preference needs saving |

The framework can be reused by another learner without carrying the personal
journey. Codex and Claude Code entry points point to the same shared instructions;
other agents can follow that entry point explicitly. Native plugins are optional.

## Memory supports curiosity

A new question starts a new direction. The agent retrieves earlier material only
when it helps. It can connect subjects without forcing them into one curriculum.
When you explicitly return to a subject, its continuation preserves the question,
inputs and unfinished work needed to resume.

Useful observations become dated journal events. Topic notes keep the current
explanation and questions. The learner profile holds stated or well-supported
cross-topic context, rather than every temporary difficulty. Indexes navigate;
they are not complete transcripts or mastery certificates.

## Artifacts and projects

A diagram, notebook, slide deck or program has a canonical artifact bundle with
editable sources and a README. A project links multiple artifacts toward a stated
goal. The same artifact may support several projects. Neither needs to be created
for a short question, and completing either does not establish understanding.

## What makes a good handoff

Another agent should be able to answer: What is the current question? What actually
happened? What did the learner demonstrate, and with what help? Which files matter?
Where would we resume if asked? Suggestions must be distinguishable from commitments.

This is a behavioral contract, not an enforced transaction system. Agents can miss
writes or misread evidence. Keep the files inspectable, correct mistakes, and test
real handoffs. The [checklist](../metadata/checks/memory_handoff.md) covers recall,
corrections, evaluation isolation, project continuation and neutral initialization.
