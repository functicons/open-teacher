# Contribute to Open Teacher

Help make learning conversations more useful and their memory more trustworthy.
Small improvements are welcome: a clearer explanation strategy, an accessible
visual method, a reproducible handoff case, or an adapter for another agent.

## Preserve the purpose

- Follow curiosity across arbitrary topics. Do not make courses, quizzes, or
  review queues mandatory.
- Keep the framework usable as files. A new service or dependency needs a concrete
  reason and discussion; do not add one merely to organize notes.
- Keep teaching behavior shared. Client adapters route to the same instructions.
- Distinguish recorded evidence from generated explanations and proposed work.
- Keep personal data out of reusable metadata, examples, images, and Git history.

## Propose a change

Explain the problem, expected behavior, and verification. For changes to the
[protocol](PROTOCOL.md), state whether existing records or implementations need
migration and propose a version change when required behavior changes. Draft 0.1
is a proposal, not a claim of endorsement by a standards body or model provider.

For teaching skills, use `metadata/skills/<skill-name>/SKILL.md` and update the
catalog. Generalize the method, document when it helps, keep it automatically
discoverable, and provide a portable fallback. Learner-specific outcomes belong
in personal records, never the reusable skill.

For framework maintenance, do not initialize or modify `user_data/` unless testing
in an isolated disposable workspace. Use synthetic examples labeled as such.
Never copy a private profile or transcript into a bug report.

## Installable workflow skill

The top-level `skills/open-teacher/` packages the workflow for native skill
installation. Optional teaching techniques stay in `metadata/skills/`.
Its `references/workspace/` is generated from canonical framework files; change
those sources and run `python3 scripts/build-skill.py` rather than editing copies.
See [installation and maintenance](docs/install_skill.md).

## Verify before submitting

Read the full diff, including new assets. Check local links and `git diff --check`.
Confirm `/user_data/` remains ignored. Test changed teaching behavior using the
[handoff checklist](metadata/checks/memory_handoff.md) when possible; distinguish
static checks from real client tests and report unavailable checks honestly.

Keep non-executable filenames underscore-separated; skill directories may use
their conventional hyphenated identifiers. Preserve standard entry point names.
Do not commit, push, or publish through an agent without explicit authorization.

## License and artwork

The framework is distributed under the existing [MIT license](LICENSE). Contribute
only material you have the right to share. Do not copy third-party teaching
instructions without checking their license and attribution requirements.

The [banner record](assets/README.md) identifies generated artwork and its prompt.
It represents the project concept, not a real learner's history or measured result.
