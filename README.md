# Sphinx Guardian Archive

This repository collects recovered and decoded source material from the
*Voyagers* series and related Guardian transmissions.  The primary
purpose is to power the EverLight OS **Codex** by converting raw
PDFs into structured Markdown entries.  Each entry summarises a source
document, highlights its key chapters and concepts and provides tags
for easier navigation.  The archive is curated under the *Sphinx Guardian
Protocol*.

## Structure

- **`/Source`** – contains the original, raw scans and PDFs of the
  *Voyagers* materials.
- **`/Codex`** – contains processed entries, transcripts or Markdown
  decodings derived from the source material.  Each entry begins with
  a YAML header specifying the title, source file and tags, followed
  by a detailed table of contents, discussion of key concepts and a
  narrative summary.
- **`metadata.json`** – provides a machine‑readable index mapping
  source files to their corresponding Codex entries and tags.

## Available entries

| Codex entry | Source file | Description |
|---|---|---|
| **Entry 001** – *Voyagers I – The Sleeping Abductees* | `voyagers-1-the-sleeping-abductees.pdf` | Summarises the first *Voyagers* volume.  It introduces Guardian teachings on UFOs, Keylonta science, human–ET hybridisation and the hidden agendas behind abduction programmes【531157327078095†L106-L128】. |
| **Entry 002** – *Voyagers II – Secrets of Amenti* | `Voyagers_The_Secrets_of_Amenti_Volume_II (2022_12_07 01_21_23 UTC).pdf.pdf` | Covers the second volume, focusing on Amenti transmissions, seeding experiments, ascension mechanics and contemporary updates from the Guardian Alliance【126639197193535†L96-L176】. |

See the individual files in the `Codex` directory for comprehensive
summaries and key‑concept glossaries.

## Contributing

1. **Add new source materials.** Place any new raw PDFs in the
   `Source` directory.  Make sure the filename is descriptive.
2. **Create a Codex entry.** For each source document, add a
   Markdown file in `Codex/` following the format demonstrated in
   the existing entries.  Include a YAML header with `title`,
   `source` and `tags` fields, a table of contents section, a
   *Key concepts* section and a narrative summary.
3. **Update `metadata.json`.** Append a new object describing your
   entry.  Use relative paths for the `file` and `codex_entry`
   fields and include a short list of tags.
4. **Submit your changes.** Once your entry and metadata update are
   ready, open a pull request explaining the additions and any
   insights gleaned from the source material.

By maintaining this workflow, we can gradually build a comprehensive
codified archive of the *Voyagers* materials.