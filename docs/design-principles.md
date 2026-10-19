# CoRE-Math design principles

CoRE-Math uses a restrained, professional and welcoming visual identity for an international academic research network. The site should make research, education, collaboration and opportunities easy to understand without making the interface feel promotional or over-designed.

## Character

- Use clear typography, comfortable reading measures and straightforward navigation.
- Keep a coherent site frame and visual hierarchy while allowing page layouts to respond to their content. A research directory, a chronological event list and a long-form programme page do not need to look identical.
- Use the implemented warm-neutral palette: warm off-white content surfaces and neutral surroundings, with terracotta as a restrained editorial accent. CoRE-Math blue remains the functional and identity colour for branding, navigation, links and focus treatment.
- Prefer open editorial layouts, typography, whitespace and simple rules. Do not introduce cards, shadows, rounded containers, decorative patterns or additional illustration unless the information task genuinely requires them.
- Make links, focus states, hierarchy and responsive behaviour clear independently of colour alone.

## Working principles

- Reuse the shared CSS variables and established page/component classes before adding a page-specific treatment.
- Preserve the distinction between a section divider and an entry rule: grey rules mark selected section boundaries; terracotta rules introduce editorial entries.
- Keep factual content, metadata and external links readable but visually secondary to the page’s main purpose.
- Test every change at desktop and narrow mobile widths. Preserve source order and accessible keyboard behaviour when layouts collapse.

For implemented values, selectors, page patterns and known exceptions, see [the technical design specification](design-system.md). Editorial-grid specifics are maintained in [editorial-grid conventions](editorial-grid-conventions.md).
