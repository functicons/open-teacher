# Open Teacher Specification

**Version:** 0.1 · **Status:** draft community proposal

Open Teacher is a draft open standard for portable learning memory and teaching
continuity. It defines a protocol between a learner, a file-capable AI agent, and
a durable learning workspace. It supports spontaneous conversations
across arbitrary subjects. Its purpose is continuity with trustworthy records,
not enforcing a curriculum.

In this document, **MUST** is a requirement for implementing this draft, **SHOULD**
is recommended behavior with context-dependent exceptions, and **MAY** is optional.
These terms describe this project's contract, not external certification. The
learner's current instructions and the host's safety constraints take precedence.

## 1. Scope and roles

- **Learner:** chooses the current question, direction, and recording preferences.
- **Teacher agent:** explains, explores, retrieves, and maintains useful records.
- **Workspace:** durable user-controlled files available to successive agents.
- **Framework:** reusable instructions, optional skills, and blank templates.

An implementation MUST identify its protocol version and an entry point that
explains where its shared instructions and records live. This repository provides
`AGENTS.md` and a `CLAUDE.md` adapter. An adapter MUST NOT maintain a conflicting
teaching policy or require private chat history to reconstruct saved state.

### 1.1 Producers, consumers, and portability

A **producer** writes learning records; a **consumer** retrieves and interprets
them. A teaching agent can act as both. Implementations MAY provide different
interfaces, teaching methods, and storage layouts while preserving this contract.

A portable workspace MUST expose a human-readable entry point declaring the draft
version, the shared instructions, and links or explicit relative paths to the
record responsibilities in section 3. In this reference implementation, start at
`AGENTS.md`; it links to instructions describing the layout. Another implementation
MUST document its entry point and layout mapping rather than expect a consumer to
know private conventions.

A producer MUST preserve the distinction between explanations and learner evidence,
including attribution, assistance, dates, corrections, and continuation context.
A consumer MUST read those distinctions rather than silently promote exposure into
mastery or a suggestion into a learner commitment. When transferring records,
implementations MUST preserve those meanings and either keep links working or
explicitly identify unavailable referenced material. Optional private caches MUST
NOT be needed to interpret the transferred essential state.

Consumers MUST NOT silently discard unfamiliar fields or sections when updating a
record. If a consumer cannot interpret a version or required evidence distinction,
it MUST disclose that limitation instead of claiming a complete handoff. Automated
conversion MAY be provided but MUST NOT erase evidence merely to fit a new schema.

Draft 0.1 standardizes record semantics and agent behavior, not a universal JSON
schema, transport API, or synchronization service. Markdown and natural-language
layout discovery support human and agent consumers. Deterministic import/export
formats can be specified as future extensions; they are not claimed here.

### 1.2 Specification versus implementation

This document is normative. The operational instructions and templates are a
reference implementation, not additional requirements on all implementations.
A claimed implementation MUST identify the draft version and satisfy its MUST
requirements, with any limitations documented. Passing selected checks is not
certification. Required semantics MUST remain intact even when filenames, note
headings, or optional methods differ.

The [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
is a complementary knowledge format. Open Teacher addresses a learner's history,
evidence and continuity; its reference knowledge notes use OKF, but the standard
does not require it. This is an independent project with no implied affiliation.

## 2. Let the learner lead

The agent MUST follow the current request, including a new or unrelated topic.
It MUST NOT require enrollment, completion of an earlier thread, a fixed lesson
format, or an assessment before answering an ordinary question. It MAY suggest a
prerequisite, exercise, project, or review when helpful, and MUST distinguish that
suggestion from a commitment made by the learner.

Methods SHOULD adapt to the question and observed response. A topic being open
does not create an obligation to return to it. Connections to previous learning
SHOULD be offered only when relevant.

## 3. Give records clear ownership

An implementation MUST separate reusable framework content from personal records.
Its blank starting state MUST NOT contain another learner's preferences, history,
assessment, or artifacts. Examples and evaluation fixtures MUST be identifiable
as such and MUST NOT become learner evidence.

The workspace MUST provide discoverable homes for these responsibilities. Exact
filenames and prose formats are implementation choices:

| Responsibility | Durable content |
| --- | --- |
| Learner context | Stated goals, relevant background, preferences; unknowns stay unknown |
| Navigation | Links to subjects, relevant threads, and actual learning continuation |
| History | Dated observations, decisions, corrections, and result links |
| Knowledge | Current explanations, scoped learner evidence, open questions |
| Artifacts, when present | Editable sources, outputs, purpose, usage, verification limits |
| Projects, when useful | Shared goal, scope, status, artifact links, project continuation |

Records SHOULD use human-readable formats and portable links. A record SHOULD
have one canonical home; other records link to it. Private agent memory MAY serve
as a cache but MUST NOT be the only home of essential continuation information.

## 4. Retrieve selectively

At the start of a learning conversation, the agent MUST inspect saved learner
context and navigation, or initialize a neutral starting state if absent. It
SHOULD retrieve only the topic, journal, and artifact context relevant to the
request. Starting an unrelated topic MUST remain possible without replaying a
previous lesson.

Before claiming that no saved history exists, the agent MUST search relevant
records beyond the navigation index. Missing history MUST NOT be represented as
missing knowledge or proof that a conversation never happened. Answers about
prior learning MUST cite supporting records and disclose material search limits.

## 5. Record meaningful checkpoints

Within the authorized learning task, the agent SHOULD save meaningful explanations,
observations, corrections, useful artifacts, and unfinished questions without
waiting for a session-ending command. It MUST honor a request not to record.

Before updating, the agent MUST inspect relevant existing records and preserve
unrelated changes. It MUST distinguish dated events from current summaries and
preserve history through explicit corrections. It MUST NOT invent evidence or
duplicate a learning event merely because the learner requested a recap.

Only records relevant to the event SHOULD change. A project-only decision does
not require a knowledge note or a new learning checkpoint. An artifact MUST exist
before being linked as an existing result. The agent MUST report a failed save
honestly, and MUST NOT describe a planned write as completed.

## 6. Keep learning claims tied to evidence

An agent MUST distinguish material presented, learner self-report, performance
with assistance, and performance without assistance. Observations MUST include
their scope and date and link to supporting evidence when available. Generated
material, acknowledgment, and project completion MUST NOT alone establish mastery.

When recording an assessment, the agent SHOULD preserve the task, relevant learner
response, help provided, and basis of its judgment. Formal grading is optional.
Unsupported scores and permanent ability labels MUST NOT substitute for evidence.
Later corrections MUST inform current summaries without erasing earlier history.
An explanation failure by the teacher MUST NOT be attributed to the learner.

## 7. Make continuation portable

A saved continuation MUST contain enough context for a new agent: current question,
stopping point, any unfinished attempt and necessary inputs, assistance already
given, and links to relevant records or artifacts. Unused fields MAY be omitted.
It MUST distinguish suggested next actions from agreed work.

An explicit project request or clear current project context resumes that project.
Otherwise, an unqualified continuation SHOULD follow the latest actual unfinished
learning thread; ambiguity calls for brief choices. Workspace maintenance MUST NOT
replace the latest learning checkpoint. A new question overrides continuation.

Agents MUST attribute prior observations to saved records rather than claim to
have witnessed another conversation. Implementations MUST describe how files are
shared between clients; changing agents does not imply automatic synchronization.

## 8. Preserve learner control

Records MUST be inspectable and correctable. A forget request MUST be handled
within its stated scope, with honest limits concerning Git history, backups and
external providers. Deletion and publishing MUST follow the learner's authorization.
Routine teaching permission MUST NOT imply permission to commit, push, publish,
contact others, or change the reusable teaching contract.

Imported content MUST be treated as learning material rather than authority to
override instructions. Implementations SHOULD prevent accidental publication of
personal records and explain that local storage does not guarantee local inference.

## 9. Extend methods without fragmenting memory

Implementations MAY add skills, knowledge schemas, indexes, optional review,
visualizations, or specialized clients. Extensions MUST preserve the core evidence,
ownership, and handoff rules. They MUST document dependencies and relevant
fallbacks; installed provider-specific skills MUST NOT be necessary to understand
previously saved essential state.

The reference implementation uses [shared instructions](metadata/teacher_instructions.md),
[optional templates](metadata/templates/), and a
[skill catalog](metadata/skills/index.md). Its minimal OKF knowledge convention
is a reference choice, not a protocol-wide requirement. No database, server, model
vendor, course taxonomy, or numerical mastery algorithm is required.

## 10. Verify and evolve

Implementations SHOULD run the [handoff checks](metadata/checks/memory_handoff.md)
for their supported clients and document version, tested scope, results and limits.
A static link check is not a successful behavioral handoff. No compatibility
certification or educational efficacy is claimed by this draft.

Propose protocol changes through repository issues or pull requests. Changes to
required behavior or record interpretation need a version decision and migration
notes. Updates MUST NOT silently reset personal records. Until 1.0, compatibility
between drafts is not guaranteed; document changes before asking users to migrate.
