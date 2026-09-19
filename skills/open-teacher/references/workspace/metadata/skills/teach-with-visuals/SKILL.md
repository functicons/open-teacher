---
name: teach-with-visuals
description: Create portable visual explanations for learning when a diagram, plot, or interactive experiment clarifies a concept or helps the learner test a prediction. Use for requested visual teaching or a clear learning benefit, not decoration or routine history summaries.
---

# Teach with visuals

Connect one learning question to something the learner can inspect, compare, or
change. Use the current topic note to target an actual question or gap. If a short
explanation or table is sufficient, use that instead of creating an artifact.

## Choose the representation

- Use a labeled diagram for structure, dependencies, or spatial relationships.
  Mermaid source is suitable for simple graphs; use SVG when precise layout matters.
- Use a plot for numeric relationships. Include assumptions, units, and the domain
  where the model applies. Distinguish illustrative data from measured data.
- Use a small interactive HTML experiment when changing an input helps answer
  “what happens if?” Show the starting state and make each control's effect clear.
- Prefer standard plotting tools for scientific figures or shareable static charts.
  Use illustration-generation tools only when pictorial content improves learning;
  exact mathematical relationships need inspectable diagrams or plots.

Choose tools that are actually available. A specialized visualization or timeline
skill can help if installed; read its instructions when using it. Do not assume a
particular provider's tools, widget runtime, or rendering surface exists.

## Make the result portable

Save durable sources and useful outputs together under a descriptive bundle in
`user_data/artifacts/`. A chat-only visualization is insufficient when the explanation is
worth preserving. If a host supports only an inline fragment, also preserve a
standalone form or source plus reconstruction instructions for another agent.

Prefer self-contained SVG or HTML with local data and assets. If a library is
necessary, record its exact version and loading requirements. Do not rely on
ephemeral download links, machine-specific absolute paths, or private host globals.
Mermaid source should have a plain-text explanation and viewing instructions when
the next client cannot render it. Use a static alternative when interactivity is
unavailable; state what the alternative cannot demonstrate.

Use a light theme by default. Label axes, arrows, controls, and important states;
do not communicate meaning through color alone. Provide keyboard-operable controls,
readable labels, and reduced-motion behavior where animation is used. Show the
concept directly rather than surrounding it with unnecessary interface elements.

## Teach and verify

Explain what to look at and why. When useful, invite a prediction before changing
one parameter or revealing the result; respect requests for a direct explanation.
Connect the observed outcome back to the concept and its limitations.

Check the visual against the underlying explanation or equations, including a
simple known case and relevant boundary conditions. For interactive material,
exercise the main control, reset behavior, and the limits of its allowed inputs.
Inspect the rendered result for legibility and clipping when a renderer is available.
If rendering or execution was unavailable, state that explicitly rather than
claiming visual or behavioral verification.

The artifact README records the learning question, file roles, provenance, how to
view or regenerate it, and checks actually performed. Link the bundle from the
topic note and journal. Preserve the state or parameter values at the stopping point
when they are needed to resume the exercise.

Record the learner's response and assistance separately from artifact correctness.
A correct plot or functioning slider does not demonstrate learning. If the method
helped or confused the learner, preserve the specific observation as evidence for
future refinement; do not infer a general learning preference from a single lesson.
