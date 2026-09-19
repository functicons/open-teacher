# Start learning

Clone the public framework, open a file-capable agent in its root, and ask it to
read `AGENTS.md`. Ask a question immediately; no profile interview is required.
The agent should initialize `user_data/` from the neutral starter during your first
learning conversation, adding only missing files and preserving existing records.

The blank starter is in [metadata/templates/initial_user_data](../metadata/templates/initial_user_data/).
There are no real learner records in the distribution. Framework development alone
should not initialize personal data.

## What you can ask

Explore an unfamiliar subject, ask one small question, bring a document, request
an experiment, or change topics without explaining why. Ask for a direct answer
when you prefer one. Request a course or practice routine only if it helps you.

Say “don't record this” to keep an exchange out of the saved learning records.
You can also ask to inspect or correct what the teacher remembers. A correction
should change the current summary and preserve a dated correction in the journal.

## Where your records live

`user_data/memory/index.md` is the local starting point. Topic notes explain what
you explored; journal entries preserve observations; artifact READMEs explain how
to use saved outputs. Optional project READMEs connect related work.

The next agent needs the same current files. For another machine, synchronize the
whole personal workspace through a mechanism appropriate to its contents, then
open the destination copy. The framework does not provide synchronization. Prefer
one writing agent at a time, or explicitly coordinate concurrent edits.

## Keep personal data out of the public framework

The root `.gitignore` ignores `/user_data/`. An ordinary `git add .` should therefore
leave personal records out. Ignoring is not encryption or access control, and does
not untrack files that were already committed. Always inspect the staged diff
before publishing. Never force-add personal records to a public fork casually.

If you want versioned personal history, first create a separate private repository
or private workspace copy. Only there, intentionally change the ignore rule and
inspect exactly what will be tracked. Do not change this public repository's
default merely to synchronize your own learning.

Your agent may send retrieved content to its model provider. The choice of agent,
provider, and environment determines data processing, not the location of these
Markdown files. A request to forget local records does not automatically remove
external conversations, backups, or Git history.

## Update or customize

Keep reusable framework updates separate from personal records. Read release or
migration notes before adopting another protocol version. Preserve your local
preferences and never replace an existing `user_data/` with the blank starter.

Personal preferences belong in the learner profile. Propose broadly useful teaching
methods through the [contribution guide](../CONTRIBUTING.md), without copying a
learner's private conversations into reusable metadata.
