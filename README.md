# -core-math-website-test

Test website for CoRE-Math.

## Documentation

For website maintenance, editorial procedures, design, metadata, deployment
and recovery, start with the [CoRE-Math website documentation](docs/README.md).

## Events

Dated activities are stored as Markdown records in `_events/`. This is the central register for schools, research workshops, conferences, mathematics competitions, modelling weeks, Study Groups with Industry and other network events.

Each event needs a `title`, `type`, `start_date`, `location` and a short description in the Markdown body. Add `end_date` for a multi-day event; otherwise the start date is used as the end date. Links to internal pages or external information belong in the body.

Supported `type` values are `school`, `research-workshop`, `conference`, `mathematics-competition`, `modelling-week`, `study-group-with-industry` and `network-event`. Optional `programme`, `project` and `research_group` fields associate an event with the corresponding record ID where relevant.

Upcoming lists include events whose end date is today or later and sort them by start date. News & Events and Education are filtered when Jekyll builds the site. The homepage also refreshes its two-event selection in the browser, so events advance as dates pass without a new deployment.

For conventions for programme, project, research-group and event detail pages, see [detail-page authoring conventions](docs/detail-page-authoring.md).
