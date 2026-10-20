# Editorial-grid conventions

These conventions summarise the open editorial-grid pattern identified in the design-consistency review. They supplement, rather than replace, the page-specific guidance in [the design audit](website-design-audit.md). The earlier audit predates the approved warm-neutral palette; this document and [the technical design specification](design-system.md) are the current references for colours and rule treatments.

## Section and entry rules

- A thin light-grey rule beneath a heading is a **section** boundary, not an item separator. Use it where a structured landing-page section needs a quiet division (for example Research, Education and Projects & Collaborations). Do not add it automatically to every heading, especially where the heading immediately introduces an editorial grid.
- A 2px terracotta editorial rule (`--editorial-accent`, currently `#874432`) introduces an **editorial entry**. In a multi-row editorial grid it normally appears only on entries in the first row of that component's widest standard layout. This includes Latest News on News & Events; chronological ordering does not require a separate rule treatment.
- Later rows use whitespace for separation; they do not repeat the terracotta rule.
- When a grid retains two or more columns at a narrower width, it preserves the wide-layout first-row rule assignment. In particular, the rule on the original second first-row entry remains when that entry moves below the first because of a two-column-to-two-column reflow.
- When an editorial grid collapses to one column, each entry receives the terracotta rule. The rule signals the actual stacked entry boundary rather than an earlier desktop row. This applies at the component's single-column breakpoint; it does not change specialised lists, directories, news cards or event chronologies.

Homepage editorial groups use the same terracotta entry-rule signal. Because their visible groups are single-row arrangements, each visible entry can intentionally have a terracotta rule. The Working Together links are navigation gateways rather than editorial entries, so their headings use quiet grey rules beneath them instead. This does not change the multi-row convention used by comparable editorial grids on other landing pages.

## Shared CSS primitives

`assets/css/content.css` defines the shared editorial values used by equivalent landing-page grids: the two-column definition, common column and row gaps, the terracotta entry-rule, its opening padding, and the quiet section-rule. Page styles use these only where the values are genuinely identical. They retain their own widths, margins, row spacing, responsive column changes and purposeful variants.

## When to use another pattern

- A single-row editorial group may give each visible entry a terracotta rule.
- Chronological, metadata-rich or filterable catalogues use their own list/separator treatment rather than editorial-grid rules when they are presented as lists rather than editorial grids.
- Image directories, tables and other specialised components retain the rule treatment appropriate to their information task. The member-university directory's marker on every image card is a current specialised exception, not a precedent for editorial grids; see [the design-consistency audit](design-consistency-audit.md) for the pending decision.
- Intentionally different grids, including the homepage news subgrid, member-university directory, event chronology, opportunities catalogue and contact directory, remain page-specific rather than being forced into the editorial-grid primitive.

This keeps the terracotta rule a restrained entry-boundary signal, while the grey rule continues to mark selected section boundaries. CoRE-Math blue remains the functional/identity colour for navigation, links, focus treatment and the header rule; see [the technical design specification](design-system.md).
