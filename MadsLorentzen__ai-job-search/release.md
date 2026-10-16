tag: v1.7.2
name: v1.7.2 - Measured PDFs, CLIs that stop trusting the digits, tools that survive non-ASCII
published_at: 2026-09-29T18:32:55Z
prerelease: False

A patch release with one theme: **the checks the workflow documented now actually run, and the tools stop breaking on anything that is not ASCII.** Compiled PDFs get measured instead of eyeballed, the portal CLIs stop trusting the digits in a URL, and every Python tool survives a Cyrillic posting or a Turkish robots.txt on Windows. Thirty-two entries, twenty-four of them fixes, most reported and fixed by contributors within days of each other.

## Highlights

### `/apply` measures the PDF instead of looking at it (#378, #476, #458, #498, #465)
`tools/verify_layout.py` measures what Step 5b previously only eyeballed: per-page text extent, bottom whitespace, the largest internal gap, footer collisions, and an entry header stranded at a page break. It exists for a failure every other check missed: a moderncv `\cventry` is unbreakable, so an entry that does not fit jumps to the next page and leaves a hole while the document still compiles, still has the right page count, and still passes `verify_pdf.py`. Step 5b now also runs the page-count check it had been claiming Step 5d ran (nothing in the workflow passed `--pages` at all). `verify_pdf.py --contains` sees through LaTeX's typographic substitutions, so `--contains "Master's degree"` and `--contains "2016-2024"` no longer report a keyword missing from a document that plainly contains it, and the new `--ascii-dates` flag reads the raw text layer for the one thing the fold must not hide: a year joined to an en-dash, which a real Workday import dropped together with the date. Poppler stays optional; a missing or xpdf `pdftotext` degrades to a `skipped:` exit 2 that now names both causes.

### Portal CLIs stop trusting the digits (#448, #500, #435, #460, #504, #505)
`jobindex-search detail` fetched any URL verbatim and, when the path did not match, returned a well-formed fake posting built from whatever page came back. `linkedin-search detail` took the first six-plus-digit segment from any URL, so a Greenhouse or Lever apply link fetched whichever LinkedIn posting carried that number, with exit 0. Both now parse the host for real and exit 1 with the `BAD_ID` contract before any request, matching the rest of the CLIs. `jobnet-search detail` no longer reports an externally hosted ad as not found, `jobdanmark-search detail` backs off on 429/5xx like every other portal, and `freehire-search` decodes HTML entities in titles and keeps the salary period, so a yearly figure no longer reads as monthly.

### Non-ASCII stops crashing the tools, especially on Windows (#490, #486, #485, #487, #506, #480, #503)
A piped stdout on Windows defaults to the ANSI code page, and that is how Claude Code runs every tool. A single Cyrillic, CJK, Devanagari, Polish or Turkish posting ended `/rank` with `UnicodeEncodeError` before any output reached the workflow; every Python tool now writes UTF-8 at entry, and the Linux CI reproduces the Windows failure through `PYTHONIOENCODING`. `/rank`'s tracker matching keeps Unicode company and role names instead of collapsing them to nothing, handles a BOM on a reordered CSV header, and rejects invalid score dimensions before saving. Distinct non-Latin company names no longer share the unknown-company job key. `robots_check.py` decodes curl output as UTF-8, so a robots.txt with a CJK rule no longer reads as UNCONFIRMED on a Windows locale, and a non-ASCII disallow rule that silently never matched now does. Two docstrings that quoted `\h` and `\s` unescaped printed a `SyntaxWarning` on every run; both are fixed and a compile check over `tools/*.py` and `tests/*.py` keeps the next one out.

### State on disk stays honest (#441, #425, #440, #455, #444)
`seen_jobs.json` keys are now a pure function of the posting, owned by `tools/job_key.py` instead of described in prose, so two runs can no longer store one job twice by truncating a title at different points; `--audit` reports legacy entries and never rewrites them. `/gmail-sync` and `/outcome` keep commas, quotes and line breaks out of the tracker's notes column, which used to shift three columns left on a subject as ordinary as `Re: Your application, Data Scientist`. `/outcome` and `/interview` no longer confuse two roles at the same company when archiving. And the `09-web-research.md` curl snippets fail loudly when `$SCRATCHPAD` is unset instead of writing into the checkout.

### New in the workflow (#467, #468, #437, #439, #474)
`/apply` Step 1 verifies the posting URL's host against installed portals and the six standard ATS apexes, flagging look-alikes and unknown hosts before any drafting tokens are spent. `/setup` ingests project writeups from `documents/projects/`, and `/expand` mines public GitHub repositories, both into the `## Independent Projects` section of the profile. `/outcome stale [N]` batch-resolves applications quiet for 60+ days with explicit confirmation. `/add-template` keeps a registered template's intermediates in `build/`.

## Fork maintainers: what to reconcile

Pull this tag rather than raw `master`, then check four things:

1. **Two `framework_version` markers moved.** `05-cv-templates.md` 1.4.3 -> 1.4.5 (the "Date fields must be ASCII ranges" section now names `verify_pdf.py --ascii-dates`, and the pdflatex preamble gains a T1 line) and `09-web-research.md` 1.1.0 -> 1.1.1 (the `$SCRATCHPAD` guard). `check_upstream_updates.py` flags both; if you personalised those files, re-read the changed paragraphs before merging yours over them.
2. **`cv/main_example.tex` gains one guarded preamble line**, `\ifpdftex\usepackage[T1]{fontenc}\fi`, a no-op under lualatex. A clean 3-way merge unless you edited the preamble; tailored CVs compiled with lualatex need nothing.
3. **`.claude/settings.json` gains four path-scoped lines** (`tools/job_key.py` and `tools/verify_layout.py`, `python` and `python3` each) and `tools/security_guards.py` requires them; `.gitignore` gains `build/` and `documents/projects/**`. Forks with their own allowlist should take both hunks.
4. **`seen_jobs.json` needs no migration**, but new scrapes key differently from entries written before `tools/job_key.py`; `/scrape` matches stored postings by URL regardless of key, so nothing is re-presented as new. Run `python tools/job_key.py --audit` if you want to see the legacy entries.

The fork-skip guard in `test_setup_command.py` now matches `test_placeholder_integrity.py` (#463), so a personalised fork's CI is no longer permanently red on that class. Note that both still run when `GITHUB_REPOSITORY` is unset, so a local run on a personalised fork stays red; the fix is invited as #496.

## Also in this release

- Real Excel workbook integration tests for the salary converter (#489), and two salary fixes: a bare `Count`/`Index` column pair now pairs instead of splitting into a false "too few employees" row (#470), and the privacy footnote prints only when a row actually carries `N/A*` (#475).
- `verify_layout.py`'s `skipped:` message names both causes of a broken extractor, including Poppler 26.0x before 26.05 aborting on any `hyperref` PDF with an empty Info field (#465, #451).

Thanks to everyone who reported and fixed this cycle: ayobamiseun for eleven merged fixes across the CLIs, `/rank` and the salary tools; InstinctEx for the job-key and `$SCRATCHPAD` work; oscarbol09 for the four workflow additions and the jobnet fallback; jakob1379 for the tracker, archive and `build/` fixes; YanCheng-go for `verify_layout.py`; yang2632 and Souptik96 for the docstring and extractor-message fixes and the review catches; iAbhiNaV2005, Nnoot02, canmugan and sahilsahu4102 for the URL, fork-CI, robots and freehire fixes; and 9scorp4, main-sounds-audio and Holo-Eter for the reports that started several of them.
