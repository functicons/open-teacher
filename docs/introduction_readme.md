# Visual introduction

[Open the HTML slides](introduction.html) · [Read the PDF](introduction.pdf)

Download `introduction.html` and open it in a browser, or open it from your local
clone. GitHub displays HTML source rather than running the presentation; the PDF
provides a previewable alternative.

The seven slides introduce:

1. Why learning context gets scattered across conversations.
2. The common memory and handoff contract.
3. The distinction between your agent and the open standard.
4. Learning evidence: exposure, self-report, and observed performance.
5. Freedom to follow unrelated questions without a fixed curriculum.
6. Projects and artifacts connected to their learning context.
7. How to start with your preferred agent.

## Controls and portability

Use the arrow buttons, keyboard arrows, Space, Home, or End. Swipe horizontally
in the desktop presentation layout on a touch screen. Slide 3 includes an illustrative agent selector; it does not
connect to an actual agent. Links such as `introduction.html#3` open a specific slide.

The HTML includes its styles, scripts, and SVG diagrams. No external libraries,
fonts, analytics, or network access are required to view it. Repository links
require internet access. Wide screens use a 16:9 presentation layout. Screens up to 760px wide use a
scrollable reading layout with full-size text and touch controls. Scroll diagrams
horizontally to see their full detail; use the arrow buttons to change slides.
Diagram scrolling does not change slides.

Print to PDF with background graphics enabled to export one page per slide.
The checked-in PDF is a static export of the HTML. Update it when the slides change.

## Verification

All seven slides were visually inspected at 1600×900 and 1024×576. Browser checks
covered layout and SVG label bounds, all three agent selections, keyboard/button/
hash navigation, hidden-slide focus isolation, and runtime exceptions. The PDF
export was checked for seven pages. Additional checks at 390px and 760px covered
all slides, 16px body text, 44px controls, and absence of page-level horizontal
overflow. Focused-control arrow navigation, native Space activation, and
independent diagram scrolling were also exercised. These are presentation checks, not tests of
real agent interoperability.
