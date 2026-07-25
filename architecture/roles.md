# Architecture — the pipeline roles

The pipeline is a sequence of **roles**, each with a **single task** and well-defined start
and end conditions. The underlying rule:

> Roles **share no hidden state**. A later role never accesses the reasoning of the
> previous one: it receives **only its output**.

It is this separation that makes verification *independent* (**third-party**) rather than
self-confirming: whoever judges did not produce what they judge, and has not seen its
reasoning.

Each role is described with the same schema: **Mission · Input · Output · What it does NOT
do · Why it exists**.

---

## Director (orchestrator and adjudicator)

- **Mission:** **it orchestrates and signs; it does not produce.** It sets the pace of the
  pipeline — chooses what to work on, in what order, and sends each note through the stages.
  But it is also the **third party that decides**: it redoes the others' computations, runs
  the **third reading from the text layer**, settles divergences between extraction and
  gates, performs the high-resolution renderings of the contested line, and is the **only**
  role that can certify a note (see [quality-gates](quality-gates.md)).
- **Input:** the work queue (Discovery), the pipeline state, and the gates' outputs — the
  base level's differences, the full level's verdicts.
- **Output:** the third reading on the contested line, the recomputed analyses, the decision
  on divergences, the note's **signature** — or a hold or quarantine, with the reason.
- **What it does NOT do:** **it does not distil** (whoever writes a note does not certify
  it). **It does not open anyone else's verdict before redoing the computation on its own**,
  starting from the note alone: if its own result and the verdict diverge, adjudication
  opens *even when the verdict says “faithful”*. It does not treat a verdict as truth in
  either direction — neither the confirmation nor the accusation. And it **never** corrects
  silently: if it finds an error of its own, it declares it and reopens the note.
- **Why it exists:** because **the last signature errs like every other role — only nobody
  checks it.** The earlier stages check each other; the one that signs has no one above it.
  The counterweight can only be a written procedure that role must run on itself, before
  every certification.

## Librarian (extraction)

- **Mission:** reads the text layer and produces **atomic notes** — one note per single
  concept or formula — with the provenance frontmatter (source, page).
- **Input:** the source document (text layer) and the item to extract.
- **Output:** an atomic Markdown note, with the provenance fields filled in.
- **What it does NOT do:** it does not “verify” its own extraction (the gates do that); it
  does not write from memory — if the source is not verifiable, it flags the gap instead
  of inventing.
- **Why it exists:** extraction and verification must live in **different roles**,
  otherwise verification is not independent.

## Pre-gate operator

- **Mission:** mechanically prepares the notes before the gates (normalizations,
  preconditions, page-existence checks).
- **Input:** the freshly extracted notes.
- **Output:** notes ready for the gate, or discarded with a reason.
- **What it does NOT do:** it does not get into the correctness of the content; it does
  mechanical, repeatable work.
- **Why it exists:** taking the mechanical work off the gates keeps them focused on
  judgment.

## Re-transcriber (gate — base level)

- **Mission:** re-reads the content **independently** and compares it with the extraction.
  It is the base check, and it runs on every **gate note** — those carrying a formula or a
  point-of-use value; exclusions are declared one by one, never wholesale.
- **Input:** the note to check (without the reasoning of whoever extracted it) and the pages
  rendered as images. Targets are pointed at by position and quantity, never by value.
- **Output:** the list of **differences** against the note, or “no differences”. A
  difference opens the **adjudication**, not the full level. Plus, for every glyph it is
  unsure of, a **declared
  doubt**: a declared doubt is worth more than a confident wrong reading.
- **What it does NOT do:** **it issues no verdicts.** It does not say “faithful” or “not
  faithful”, it does not judge and it does not accuse: a difference between two readings is
  not an accusation, and it is judged by a third party who also holds the text layer. It
  does not normalise what it reads: the target is what is **printed**, even when what is
  printed makes no sense.
- **Why it exists:** because it was created by *removing* the verdict from the second
  reading. When the second reading issued verdicts, it erred in both directions —
  correlated confirmations on faulty notes, and accusations against sound ones. What
  remained useful, measured, was the **independent re-transcription**: the value this role
  brings is the transcription, not the opinion (see
  [ADR-0002](decisions/0002-verdict-as-source-of-error.md)).

## Verifier (gate — full level, from the image)

- **Mission:** when a verdict **accuses the source**, or the note is a **benchmark
  anchor** — in particular on **formulas** — it verifies from the **image** of the page,
  not from the OCR text. The high-resolution rendering of the contested line is
  **mandatory** before signing off (see
  [ADR-0001](decisions/0001-formula-verification-from-image.md)).
- **Input:** the contested note and the high-resolution image of the page/line.
- **Output:** confirmation, correction, or quarantine of unresolvable content.
- **What it does NOT do:** it does not “correct” a source without stronger independent
  proof; it does not guess where not even the image is legible — it flags. It also does
  **not receive the expected answer**: the prompt points at targets by **position and
  quantity**, never by value, and does not carry the expected form — neither in the
  instructions nor through free-text fields that let it back in. The note is handed to it
  *for the comparison*, which opens only **after** its own transcription is closed: what
  holds the safeguard up is the separation between whoever reads and whoever judges, not
  the good will not to look (see
  [ADR-0006](decisions/0006-reader-must-not-know-the-expected-answer.md)).
- **Why it exists:** it is where florilegium closes the OCR blind spot on formulas. It is
  the hero feature.
