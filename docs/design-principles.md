# CoRE-Math design principles

CoRE-Math uses a restrained, professional and welcoming visual identity for an international academic research network. The site should make research, education, collaboration and opportunities easy to understand without making the interface feel promotional or over-designed.

## Character

- Use clear typography, comfortable reading measures and straightforward navigation.
- Treat consistency as a governing principle: elements that perform the same information task should normally share the same visual treatment throughout the site. A different treatment is appropriate only when the content structure or user task is materially different, and that exception should be documented.
- Keep a coherent site frame and visual hierarchy while allowing page layouts to respond to their content. A research directory, a chronological event list and a long-form programme page do not need to look identical.
- Use the implemented warm-neutral palette: warm off-white content surfaces and neutral surroundings, with terracotta as a restrained editorial accent. CoRE-Math blue remains the functional and identity colour for branding, navigation, links and focus treatment.
- Prefer open editorial layouts, typography, whitespace and simple rules. Do not introduce cards, shadows, rounded containers, decorative patterns or additional illustration unless the information task genuinely requires them.
- Keep interactive states, hierarchy and responsive behaviour clear, with visible keyboard-focus indicators.

## Hyperlink visibility

Inline hyperlinks use a restrained, muted medium-blue that complements the CoRE-Math palette. They inherit the surrounding text’s font weight: normally regular, while deliberately bold text remains bold. Links have no default underline. Keep this treatment consistent across the website.

Underlining is reserved for hover and keyboard focus. Keyboard focus must also retain a clearly visible outline. Visited links use the same identifiable treatment as unvisited links.

This applies to news articles, research pages, programme descriptions, resources and other textual content, including paragraphs, bullet lists, tables and captions. Maintain adequate contrast against the actual background, including alternate table rows and supporting surfaces.

Preserve established styling for navigation menus, buttons, linked headings, cards and other recognisable interface controls. Inline links within descriptive text follow the body-link treatment.

## News-card images

Every newly featured news item should have a relevant, permitted image. If rights cannot be established, use an appropriate approved alternative or explicitly report the limitation before publishing; do not treat a blank image area as a finished result.

Use the existing shared card dimensions. Photographs fill their image area with a considered crop. Posters and announcement graphics use `image_type: graphic` to show the complete artwork at its original proportions without additional CSS padding. Avoid embedding excessive blank canvas around logos; assess the visible artwork, not just the dimensions of the file. Follow applicable brand rules and report any constraint that prevents an effective card image.

Record source, permission evidence, credit and modifications in post metadata, with public attribution where required. Provide a full-size link for posters whose detailed text cannot be read at card size. Check the actual rendered homepage and News & Events cards on desktop and mobile, including legibility, cropping, whitespace and image loading.

## Working principles

- Reuse the shared CSS variables and established page/component classes before adding a page-specific treatment. Do not create a near-duplicate component merely to solve a local styling problem.
- Preserve the distinction between a section divider and an entry rule: quiet grey rules mark selected section boundaries; terracotta rules introduce editorial entries. Neither is a default decoration for every heading or repeated item.
- Keep the original wide-layout rule assignment when an editorial grid collapses: a rule belongs to its entry, rather than being recalculated for each breakpoint.
- Keep factual content, metadata and external links readable but visually secondary to the page’s main purpose.
- Test every change at desktop and narrow mobile widths. Preserve source order and accessible keyboard behaviour when layouts collapse.

For implemented values, selectors, page patterns and known exceptions, see [the technical design specification](design-system.md). Editorial-grid specifics are maintained in [editorial-grid conventions](editorial-grid-conventions.md). The current review and unresolved decisions are recorded in [the design-consistency audit](design-consistency-audit.md).
