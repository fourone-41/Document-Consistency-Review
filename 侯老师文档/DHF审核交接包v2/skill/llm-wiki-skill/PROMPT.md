# LLM Wiki Prompt

You are building or extending an LLM wiki from converted DHF/DMR Markdown evidence.

Do not treat the wiki as the evidence itself. The wiki is an index over source Markdown and `.assets` evidence.

For each wiki task:

1. Read `D:\AI_0415\03DHF\skill\llm-wiki-skill\SKILL.md`.
2. Determine whether this is a full rebuild or incremental extension.
3. Read the existing wiki index and manifests before changing anything.
4. Preserve existing sources unless the user explicitly asked for a rebuild.
5. Copy converted Markdown into `llm_wiki\sources\<modality>\` as `.source.md`.
6. Keep original `.assets` directories referenced in catalogs.
7. Generate modality catalogs and an all-source catalog.
8. Generate modality coverage, high-risk pages, ignored-file pages, and stage pages.
9. Update `wiki\index.md`, `README.md`, `AGENTS.md`, `llms.txt`, and `llms-full.txt`.
10. Verify counts against source manifests.

Final output must include:

- wiki root
- index path
- source counts by modality
- blocked count
- ignored count
- key catalog paths
- any known limitations
