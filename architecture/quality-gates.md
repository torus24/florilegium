# Architecture — the quality gates

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

The second entry point exists because the first is not enough: a silent error generates no
doubt, so a check that fires only on doubt does not fire in the cases it exists for. The
third channel (§3) is unconditional for the same reason — on formula notes it runs **even
when the gate found nothing**. Especially then.

## 2. Third-party verification

Whoever judges did not produce what they judge, and does not see its reasoning (see
[roles](roles.md)). On formulas this becomes concrete: the full level does not trust the
OCR text — it renders the page as an **image** at high resolution, re-transcribes the
formula **independently**, and cross-checks it against the text reading.

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
   ├─ MECHANICAL pre-gate ... a script, not a model: checks that the equation number and
   │                          the distinctive strings are on the declared page
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
             └─ the verdict accuses the source  ·or·  the note is an anchor
                       ↓
                  FULL gate ★ ... the page IMAGE at ≥400 dpi, with a verdict   (channel 2)
                       │
                       ├─ confirm / correct ────────────────────────────────► Vault
                       └─ unresolvable ──► Quarantine  (neither promoted nor lost, with a reason)
```

## Quarantine

What no level manages to resolve is **neither promoted nor thrown away**: it goes into
**quarantine**, with the reason. It is a first-class mechanism, not an error: it makes
explicit what the system does not know, instead of guessing. The quarantine folder exists
by convention even when empty.
