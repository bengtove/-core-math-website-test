# Detail-page authoring conventions

This note supports consistent programme, project, research-group and event pages without requiring every page to have the same length or structure.

## Content model

- A **programme** is a continuing framework for related activity.
- A **project** is a defined collaboration with its own objectives and duration.
- An **event** is an activity taking place on particular dates.
- A **research group** is an ongoing scholarly network or community.

Dated activities belong in `_events/`. Where an event belongs to a programme, project or research group, add the corresponding identifier in its front matter. Do not duplicate an event as a project merely to give it a page.

## Detail pages

Use the available information to provide, in this order where relevant:

1. a concise introduction explaining the activity or collaboration;
2. relevant factual information, such as partners, period, location, funding or status;
3. related CoRE-Math activity, using the relevant collection metadata; and
4. external links for authoritative further information.

Existing historical content should be preserved. A short record does not need invented sections merely to match a richer page.

## Contextual navigation

Programme, project and research-group pages generated from their respective collections receive a parent-context link automatically. This returns visitors to Programmes & Projects or Research groups, as appropriate.

Standalone detail pages outside these collections should specify both `parent_context_url` and `parent_context_label` in their front matter so that they provide the same clear route back to their parent area.

### CoRE-Math Schools

CoRE-Math Schools is an intentional exception to the generic related-events listing. Its programme page uses dedicated Upcoming schools and Previous schools navigation instead, linking to the same Event records and to the historical schools archive. This avoids duplicating school listings on the programme page.

## Links

Use explicit action labels on their own line when linking from a catalogue or editorial entry:

- `About the programme →`
- `About the project →`
- `About the research group →`
- `Event details →`
- `Read the report →`

Use a descriptive external-link label when an external destination is the primary source, for example `Visit the FAME website →`.
