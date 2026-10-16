# Editorial-grid conventions

These conventions summarise the open editorial-grid pattern identified in the design-consistency review. They supplement, rather than replace, the page-specific guidance in [the design audit](website-design-audit.md).

## Section and entry rules

- A major content section uses a thin light-grey rule beneath its heading. This is a **section** boundary, not an item separator.
- A 2px CoRE-Math blue rule introduces an **editorial entry**. In a multi-row, two-column editorial grid it normally appears only on the entries in the first desktop row. This includes Latest News on News & Events; chronological ordering does not require a separate rule treatment.
- Later rows use whitespace for separation; they do not repeat the blue rule.
- When a grid collapses to one column on narrow screens, it preserves the source order and the desktop rule assignment. In particular, the rule on the original second first-row entry remains; a responsive layout must not remove it simply because that entry now appears below the first.
- Conversely, responsive collapse must not add blue rules to entries that did not have them on desktop.

Homepage editorial groups use the same blue entry-rule signal. Because their visible groups are single-row arrangements, each visible entry can intentionally have a blue rule. This does not change the multi-row convention used by comparable editorial grids on the other landing pages.

## Shared CSS primitives

`assets/css/content.css` defines the shared editorial values used by equivalent landing-page grids: the two-column definition, common column and row gaps, the blue entry-rule, its opening padding, and the quiet section-rule. Page styles use these only where the values are genuinely identical. They retain their own widths, margins, row spacing, responsive column changes and purposeful variants.

## When to use another pattern

- A single-row editorial group may give each visible entry a blue rule.
- Chronological, metadata-rich or filterable catalogues use their own list/separator treatment rather than editorial-grid rules when they are presented as lists rather than editorial grids.
- Image directories, tables and other specialised components retain the rule treatment appropriate to their information task.
- Intentionally different grids, including the homepage news subgrid, member-university directory, event chronology, opportunities catalogue and contact directory, remain page-specific rather than being forced into the editorial-grid primitive.

This keeps the blue rule a restrained entry-boundary signal, while the grey rule continues to mark ordinary section boundaries.
