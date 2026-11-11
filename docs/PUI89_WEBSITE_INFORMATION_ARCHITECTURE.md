# PUI89 Website Information Architecture and Simplification

**Status:** Navigation simplification implemented on a feature branch; content consolidation is deliberately non-destructive.

## Visitor-facing primary navigation

Keep the primary navigation focused on six destinations:

1. Projects — the seven project pages and project discovery.
2. Shared AI Core — the common intelligence, safety and interface architecture.
3. Research — the Research & Knowledge Centre.
4. Evidence — validation records, test boundaries and source evidence.
5. Intelligence Dashboard — cross-project status and development observability.
6. Collaboration — research, partnership and contact routes.

Secondary material remains available under **More**: AI Vehicles, Engineering Atlas, Work Intelligence, Security & Trust, Roadmap, Open-source Resources, About PUI89, AI & Robotics in Thailand and GitHub.

## Content boundaries (avoid repeated explanations)

- **Home:** concise mission, project discovery, shared foundation, collaboration and contact. Do not repeat full technical specifications from project pages.
- **Project pages:** one authoritative overview per project. Keep project-specific goals, architecture, risks, constraints, implementation status and repository links here.
- **Shared AI Core:** the authoritative explanation of reusable contracts, world-state, uncertainty, safety gates, permissions, compute coordination and shared evaluation. Other pages should link here rather than reproduce the full architecture.
- **Research & Knowledge:** curated research papers, technical references and learning resources. Do not present a link collection as completed research.
- **Engineering Atlas:** cross-project system maps, interfaces, engineering decisions and constraints. Link to project pages for their detailed specifications.
- **Evidence & Validation:** dated test records and provenance. Keep measured, simulated, synthetic, estimated, proposed and unknown clearly distinct.
- **Intelligence Dashboard:** concise portfolio status, source timestamp, repository/commit evidence, freshness and exceptions. Do not duplicate long research or policy prose.
- **Work Intelligence:** explain the supervised work pipeline and autonomy limits; do not imply proposed specialist roles are deployed agents.
- **Security & Trust:** one shared policy overview with links to repository-specific policies and current audit evidence.
- **Roadmap:** milestones and priorities only; avoid repeating project descriptions.
- **About PUI89:** identity, purpose and current collaboration status only; avoid copying the project portfolio or roadmap.
- **Collaboration / Support:** one clear route for researchers, universities, sponsors and contributors.

## Simplification rules

1. Do not delete project pages, source code, datasets, test records, repository history or technical documents merely to shorten the menu.
2. Do not remove a page from the sitemap until its useful content has been migrated and inbound links have been checked.
3. Prefer linking to one authoritative page over maintaining duplicate technical descriptions.
4. Keep English and Thai navigation labels and destinations aligned.
5. Treat old reports as historical unless regenerated and verified against current repository sources.
6. Do not expose private Shared AI Core contents on the public website. A public status may say only that the repository is private and its details are not publicly available.
7. Never invent progress scores, performance results, partner relationships, deployed agents or physical robot validation.
8. Preserve the zero-cost policy and protected pull-request workflow. No paid API, subscription, cloud GPU, new metered service or unreviewed external automation is introduced by this change.

## Implemented in this change

- Reduced the English and Thai homepage primary navigation to six core destinations.
- Moved secondary destinations into a single **More / เพิ่มเติม** menu.
- Preserved the seven project links and all existing deep pages.
- No page or technical evidence was deleted.
- This is a navigation and information-architecture improvement, not a claim that all duplicate page content has already been consolidated.
