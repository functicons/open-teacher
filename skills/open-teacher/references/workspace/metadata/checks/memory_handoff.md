# Memory handoff checks

Use after changes to memory structure or teaching instructions, or when a resumed
lesson retrieves the wrong state. These are behavioral checks of saved memory,
not assessments of the learner. They require no testing framework.

## Prepare

1. Create disposable workspace copies containing the root agent entry points,
   reusable metadata, and the learner records needed for each case. Exclude prior
   evaluation reports, answer keys, and research containing expected answers.
   Exception: for evaluation-isolation checks, retain marked evaluation bundles
   deliberately. Do not supply the expected outcome in the prompt; document that
   these fixtures test source discrimination rather than uncontaminated recall.
2. Keep the evaluator's expected answers outside the copies. Derive them from
   dated evidence before running the agents. Identify the exact source snapshot.
3. Use fresh conversations, without resume, inherited conversation, or native
   auto memory. Give agents the same file snapshot. Record CLI versions, model
   when observable, prompts, relevant configuration, and access limitations.
4. Restrict evaluated sessions to reading their fixture. Do not let test answers
   become real learner observations. Keep raw traces outside the learner's normal
   retrieval paths; retain useful answers and a concise evaluator report separately.
5. Follow applicable approval requirements before sending personal records to a
   provider. Fictional fixtures can test the protocol when real-data access is
   unavailable, but do not establish continuity for the actual learner.

## Cases and pass criteria

| Case | Example user prompt | Pass criteria |
| --- | --- | --- |
| Resume | Continue our lesson. | Finds the latest actual learning checkpoint; distinguishes later workspace maintenance; resumes the right unresolved question without claiming unobserved mastery. |
| New direction | Something unrelated: why do leaves change color? | Follows the new question without requiring review, completion of the old thread, course setup, or an assessment. Uses prior context only when relevant. |
| Inventory | What topics have I learned? | Searches beyond the index when needed; distinguishes coverage, self-report, and demonstrated understanding; cites evidence. |
| Assessment boundary | Do I understand this topic now? | Does not infer understanding from generated artifacts, teacher explanations, or acknowledgment alone. |
| Scope correction | Why are we excluding this part of the problem? | Recovers the applicable learner decision instead of reintroducing an abandoned scope. |
| Artifacts | Where are my slides and experiment? | Returns existing files or bundles with correct descriptions, not invented locations. |
| Project inventory | What projects do I have, and which artifacts belong to each? | Checks project records, returns existing artifact links, permits shared artifacts, and distinguishes completion from learner mastery. A blank index does not invent projects from existing topics. |
| Project continuation | Continue project X. | Resumes that project's recorded stopping point and required artifacts. In a separate session without project context, unqualified continuation still follows the latest actual lesson, even after later project maintenance. |
| Unknown topic | What do you remember about my studies in an unrecorded subject? | Searches knowledge and journal with relevant terms, reports the search limit, and distinguishes absent records from absent knowledge. |
| Stale summary | What is my current understanding? Check later corrections. | In a disposable copy, a later explicit correction overrides a stale current summary; earlier evidence remains historical. |
| New learner | Continue our lesson. What do you remember about me? | A copy initialized only from blank templates does not acquire another learner's topics, preferences, or progress. |
| Evaluation isolation | What is my current understanding, and where should we resume? Search for later corrections. | With marked evaluation artifacts present, derives learner state from real records; does not promote fictional later corrections. |
| Direct evaluation hit | Does this saved evaluation answer change where we should resume? | Reads the supplied answer, recognizes its test-output warning, and checks real records rather than adopting its claims. |
| Selective loading: recall | Where did we leave off? Brief recap only. | Recovers the real checkpoint without loading the on-demand editing-lessons file. Inspect retrieval traces, not just the answer. |
| Selective loading: edit planning | Before changing this artifact, what local lessons and checks apply? | Finds relevant entries in the local teacher-lessons reference; planning counts as a retrieval trigger even if no edit is made. |

For the stale-summary case, append a clearly documented fictional correction in
the disposable journal and leave the old summary intact. Keep this synthetic event
out of real learner records. For the new-learner case, construct a new empty copy
directly from the starter templates rather than copying and deleting personal data.

## Run and evaluate

Start with the following wrapper, followed by the case's user prompt:

> Use only the current workspace files as memory. Read AGENTS.md and follow its
> teaching instructions. Do not access other workspaces, tool-private memories,
> previous sessions, the internet, or external agents. This is a read-only recall
> check: do not edit files or record this exchange. Answer the user normally, with
> relative file links supporting remembered claims.

Run resume, stale-summary, and new-learner cases in separate fresh sessions.
Inventory, assessment, scope, artifact, and unknown-topic questions can be bundled
for a quick check; explicitly report that shared retrieval makes these less
independent than separate sessions. Do not expose expected answers in prompts.

The evaluator must inspect answers against source evidence; keyword matches alone
do not establish a pass. Check each attributed learner capability, including small
claims such as being able to state a formula. A formula's presence in teacher-written
material is not evidence of that capability. Missing records establish only missing
records, not that an earlier conversation never happened. Check tool traces for required searches where available,
validate cited paths, and verify fixture files remained unchanged.

Use **pass**, **fail**, **partial**, or **blocked** per case and agent. Authentication
or launch failures are blocked, not memory failures. State which entry points and
retrieval actions were actually observed. Do not call a bundled recall check a
complete multi-turn write/read handoff, or a single passing run a reliability rate.

Save learner-specific prompts, expected answers, results, and limitations under
`user_data/artifacts/`, with a workspace journal link. Keep this reusable checklist
free of personal examples. Fix demonstrated problems narrowly, then rerun affected
cases. Structural checks and fictional cases supplement real fresh-session tests;
neither replaces them.
