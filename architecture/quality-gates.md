# Architecture — the quality gates

🇮🇹 *Questa pagina è disponibile anche in [italiano](quality-gates.it.md).*

The **quality gates** are the methodological core of florilegium: the point where an
extracted note is put to the test before it enters the vault. They are designed around
four ideas, each with a record behind it — an ADR, a journal entry, or both.

## 1. Two levels, plus an adjudicator

A single “heavy” gate on every note would be costly and slow; a single “light” gate would
miss the errors that matter. florilegium uses **two gate levels** and, above them, **an
adjudicator** who is the only one that signs:

| Level | Who | When | What it does |
|---|---|---|---|
| **Base** | Re-transcriber | Only on **gate notes**: formulas and numeric values at point of use | Re-transcribes from the **image** and **lists the differences** — it does not judge |
| **Full ★** | Verifier | Only when a verdict **accuses the source**, or the note is a **benchmark anchor** | Verifies from the image at **≥400 dpi**; this is where the verdict lives |
| **Adjudicator** | Director | **Always**, on everything that passes | Redoes the numbers before opening anyone else's verdict, performs the third reading from the text layer, settles divergences, **signs** |

The base gate does not run “on every note”: it runs on **gate notes**. The others are
**excluded one by one, with the reason on record** — never a wholesale exclusion.

Classifying a note — gate note or not, base level or full — belongs to the **adjudicator**:
not to whoever extracts, and not to whoever checks. The rule is *when in doubt, the higher
level*. The exclusions are recorded in the **run report**, one by one, each with its own
reason, and never as an aggregate count: the rule was written after two notes were excluded
wholesale and recovered only by re-reading the document in full.

**Notes that are not gate notes.** A note carrying neither formulas nor values at point of
use goes through neither the mechanical pre-gate — which runs on formula notes — nor the
image gate: its exclusion is declared one by one with its reason, and the image
verification field **stays empty**. The guarantee it receives is of a different kind, and
that has to be said: fixed granularity in extraction, a **cross-note coherence** check
before the signatures (one note cannot assert as certain what another declares an
inference), a structural audit of the corpus, and the adjudicator's signature. Multi-channel
verification is reserved for what feeds a computation. On a technical corpus these notes are
the bulk of the volume: saying that they receive a **weaker** guarantee is part of the
method, not an exception to it.

**A benchmark anchor** is a note designated in advance as a **fixed reference** for the M4
measurements: its content has to stay verified to the letter, because later measurements are
compared against it. The designation comes from outside the gate — it is a deliberate act,
not something a role decides on its own while running. Anchors are verified at the full level **regardless of any
accusation**: that is why they are the second entry point.

Escalation has **two entry points**, and they lead to two different places:

- **by flag** — one or more discrepancies at the base level do not trigger the expensive
  check: they open the **adjudication** by the director, with a mandatory reading from the
  text layer. Whoever found the difference is not whoever judges it.
- **by accusation** — any verdict that says *the source is wrong* requires the disputed
  line to be rendered at **≥400 dpi** before it can be signed off. At any level, with no
  suspicion required and no discretion. This is a **reversal of the burden of proof**: to
  accuse the source, the pipeline must prove it through a channel different from the one
  that produced the accusation. It is also the only entry point, together with benchmark
  anchors, that escalates to the full level.

**Who can accuse the source.** The accusation does not originate in the full gate — it is
what *sends* a note there. Three roles can produce one:

- the **librarian**, when the extracted line does not hold up and it declares the suspicion
  instead of silently normalising it (fidelity ≠ correctness →
  [journal/02](../journal/02-the-silent-corrector.md));
- the **adjudicator**, when the third channel does not close: the arithmetic the source
  publishes does not come out of the printed formula;
- the **verifier**, on a benchmark anchor — where the full level runs without an
  accusation, and may produce one.

The base gate is a borderline case, and worth stating precisely: when the print looks
senseless it **flags a candidate source typo** instead of normalising it — but it stops at
the flag. It lists differences, it does not accuse: a difference between two readings is not
an accusation, and turning a candidate into an accusation is the adjudicator's call. Whoever accuses, at any level, owes
the rendering of the disputed line at **≥400 dpi before the signature**: that is the entry
point by accusation, and it has no exceptions.

The second entry point exists because the first is not enough: a silent error generates no
doubt, so a check that fires only on doubt does not fire in the cases it exists for. The
third channel (§3) is unconditional for the same reason — on formula notes it runs **even
when the gate found nothing**. Especially then.

## 2. Third-party verification

Whoever judges did not produce what they judge, and does not see its reasoning (see
[roles](roles.md)). On formulas this happens on **two planes**. **On every gate note**, the
base level re-transcribes from the image and cross-checks its own transcription against the
note — it lists the differences and stops there. **Judging** those differences belongs to
the **adjudicator**, who brings in the third reading from the text layer. **When a
verdict accuses the source** — or the note is a benchmark anchor — the **full** level
renders the disputed line at ≥400 dpi and re-transcribes it independently: that is where
the verdict lives, and it is the reinforced proof, not the routine check. The verdict then
goes back to the adjudicator, who weighs it and **signs**: no level closes on its own.

- Agreement between the two readings is **evidence, not proof**: two channels can be
  wrong together (see §3).
- Disagreement neither promotes nor rejects: it opens the **adjudication** by the
  director — and, if it stays unresolved, quarantine.
- The high-resolution rendering of the contested line is **mandatory**, not “on demand”:
  left to discretion, it never happened. → rationale and data in
  [ADR-0001](decisions/0001-formula-verification-from-image.md).
- Independence is **informational**, not just organizational: whoever verifies must not be
  handed the answer being verified. A verifier that already knows what it is supposed to
  find will find it. →
  [ADR-0006](decisions/0006-reader-must-not-know-the-expected-answer.md).

This cuts in **two directions**: it catches silent errors *and* clears false alarms (it
does not “correct” sources that were already right).

## 3. Three channels, not two

Two independent readings can agree **on the same error**. When they do, the gate sees no
discrepancy — and the error is not caught, it is *certified*. So the check does not rest on
two channels but on **three**, chosen for **how differently they fail**:

| Channel | What it reads | How it fails |
|---|---|---|
| **Text layer** | the characters embedded in the PDF | drops or reorders characters — a lost operator, an inverted index |
| **Page image** | the page rendered at high resolution | confuses **glyphs** that look alike |
| **The source's own arithmetic** | a value the formula must reproduce, a limiting case, the dimensional balance | it does not fail by *reading*: either the result closes, or it does not |

The third pass is performed by **the adjudicator**, and it is performed **always** on every
formula note: a **third reading from the text layer**, even when the gate found nothing.
Wherever the source publishes a number that the formula must reproduce, **the source's own
arithmetic is the form to be preferred** — it settles the question **without looking at
either reading**. And when *that particular line* is unreadable in the layer, the internal
arithmetic **stands in for it**: line by line, never page by page. A worked case:
[examples/01](../examples/01/README.md).

Three rules follow, and they are rules, not advice:

- **No channel is ever declared dead wholesale.** Unavailability is decided **line by
  line** and justified in the report — never as an a-priori exclusion of a page or a
  document.
- **Raising the resolution does not fix a glyph error.** If two symbols resemble each
  other, looking closer does not help: you have to look **from somewhere else**.
- **The text layer is never enough, on its own, for a verdict.** It is a channel, not a
  proof: any conclusion resting on it alone stays open.

**Triage adds a channel, it does not remove one.** Pages whose text layer is empty or
corrupted are read **as images too**, for extraction: that is a page-level decision, and it
is the only one. It does not declare the text layer dead — the layer stays due **line by
line** for verification: the third channel is attempted on the contested line even on a page
declared corrupted, because the plain text, the equation numbers and the source's own
arithmetic **survive** the corruption of the symbols. In the originating chain a page
declared unavailable wholesale later turned out to be decisive on three contested lines out
of three. It must be said just as plainly that on those pages extraction and the base gate
read **the same image**: there the first two channels can fail the same way, and what stays
independent is the third. How to give the first two their independence back on those pages —
different renderings, different roles, or an inversion of the channels — is a **declared
debt of M2**.

→ the episodes behind this: [journal/03](../journal/03-the-third-channel.md).

## 4. The verdict is evidence, not absolute truth

Forcing a clear-cut verdict (pass / fail) on **every** item manufactures false confidence:
on ambiguous evidence, the role produces a verdict anyway — often a wrong one. Therefore:

- An outcome of **“cannot determine → escalation”** is allowed — and sometimes required.
- A **high-impact** verdict (e.g. “the source is wrong”) is not signable without stronger
  independent proof.
- The gate **rewards honest doubt**: an escalation is not a failure, it is the correct
  behaviour. → [ADR-0002](decisions/0002-verdict-as-source-of-error.md).

## The path of an item

```
Extraction  (channel 1 · text layer)
   │
   ├─ MECHANICAL pre-gate ... the check is the script's, not the model's: it checks that
   │                          the equation number and the distinctive strings are on the
   │                          declared page
   │
   └─ BASE gate ........... gate notes only ...... re-transcription from the IMAGE  (channel 2)
                                                   lists the differences, does not judge
             ↓
   ADJUDICATOR — the director, always
      ├─ redoes the numbers BEFORE opening anyone else's verdict
      ├─ third reading from the TEXT LAYER on every formula note, even at zero discrepancies
      └─ the source's own arithmetic wherever it publishes a number             (channel 3)
             │
             ├─ all consistent ─────────────────────────────────────────────► Vault
             │
             ├─ divergence settled ──► correction, always DECLARED, never silent ──► Vault
             │
             ├─ does not close ──► HELD NOTE — “do not use at point of use”
             │                       the unit closes without it; releasing it is an
             │                       explicit decision, and re-runs the MISSING STEP only
             │
             └─ the verdict accuses the source  ·or·  the note is an anchor
                       ↓
                  FULL gate ★ ... the page IMAGE at ≥400 dpi, with a verdict   (channel 2)
                       │
                       └─ reasoned verdict ──► back to the ADJUDICATOR, who weighs it and SIGNS
                                 ├─ confirm / correct ──────────────────────► Vault
                                 └─ unresolvable ──► Quarantine  (neither promoted nor lost, with a reason)
```

## Held notes

Quarantine is decided **note by note**, not per document — a whole item is quarantined only
when the problem invalidates all of it. And most of the time the trouble is **one note out of
N** and does not even call for quarantine: that note is **held**. The unit closes with the other
N−1; the held note stays in place carrying, at the top of its body, the line **“do not use
at point of use”**, and its verification field stays empty. It is not lost and it is not
usable — and the difference is written where a reader will actually see it.

A held note is released only by an **explicit decision**, never automatically, and the
release re-runs the **missing step only** — the image gate, the adjudication, or both. If
it still does not close, the note is corrected outside the chain or dropped: that too is a
decision, not a default. Corrections are always **declared**; a silent correction is a
defect in itself (see [journal/02](../journal/02-the-silent-corrector.md)).

## Quarantine

What no level manages to resolve is **neither promoted nor thrown away**: it goes into
**quarantine**, with the reason. It is a first-class mechanism, not an error: it makes
explicit what the system does not know, instead of guessing. The quarantine folder exists
by convention even when empty.
