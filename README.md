# Open Teacher

**An open standard for portable learning memory. Use your preferred AI.**

![Codex and Claude Code share learning memory: your context, knowledge, and artifacts stay in your files.](assets/open_teacher_banner.svg)

Learn something in one chat. Keep the context for the next—even when you switch
agents. **Your agent teaches; Open Teacher defines what carries forward.**

[Get started](docs/getting_started.md) · [Install the skill](docs/install_skill.md) ·
[Read the standard](PROTOCOL.md) · [View the slides](docs/introduction.pdf)

## From one conversation to the next

![Ask any question → save useful context and artifacts → continue with a compatible agent using the same files.](assets/learning_flow.svg)

**Any topic. No required syllabus. No required server or database.**

## Try it with your agent

**Using the skill:** [install it](docs/install_skill.md), then ask:

> Use open-teacher. Create a new learning workspace at ~/learning/my_notes,
> then help me explore a topic I choose.

**Using a workspace:** [open the reference workspace](docs/getting_started.md)
(or one you already created), then ask:

> Read AGENTS.md. Help me understand something I’m curious about, and keep useful
> learning context so we can continue later.

For another agent, open the same current learning directory. Saved explanations,
questions, and attempts provide context; they are not automatic proof of mastery.

## Explore

| I want to… | Go here |
| --- | --- |
| Understand the idea | [Visual introduction](docs/introduction_readme.md) · [Project overview](docs/overview.md) |
| Use Codex, Claude Code, or another agent | [Install the skill](docs/install_skill.md) · [Compatibility](docs/compatibility.md) |
| See how files and memory work | [How it works](docs/how_it_works.md) |
| Build an implementation | [Draft specification](PROTOCOL.md) |
| Improve the standard | [Contribute](CONTRIBUTING.md) |

**Draft 0.1 · Independent community proposal · [MIT licensed](LICENSE)**

Behavior depends on the agent following the instructions. Files must be shared
between agents; synchronization is not automatic. [Scope and limits](docs/compatibility.md).
