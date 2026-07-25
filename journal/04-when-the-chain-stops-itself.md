# 04 — When the chain stops itself

🇮🇹 *Questa pagina è disponibile anche in [italiano](04-when-the-chain-stops-itself.it.md).*

*Journal entry. The data comes from prior use of the pipeline that preceded this project,
reported in generic form.*

---

## The problem with a pipeline that works on its own

The previous entries are about **how you verify**. This one is about **when you stop** —
which is a quality problem dressed up as a management problem.

A chain like this works for a long time and unsupervised. It has no human deciding to break
off because it is late or because their head no longer holds. The risk is not that it stops:
it is that it **stops badly** — in the middle of a unit of work, leaving half-finished
material on disk that nobody can classify when work resumes.

And there is a symmetric risk, less obvious: that it **does not stop at all**.

## The cap that was not a cap

During a trial run, the limit was set to **one paper per run**. The paper was worked,
closed and committed. And then the chain **scheduled its own restart** and began the next
one, with nobody at the keyboard.

The relaunch mechanism worked perfectly. It was **the interpretation of the limit** that was
wrong: the cap was read as a *quota per single execution* — quota spent, start a new
execution — instead of as **the automatic end of the work**. A counter that resets itself is
not a limit, it is an engine.

The remedy was manual and unpleasant: kill the running execution, drain the queue of
scheduled restarts, **delete the uncommitted notes** of the paper opened by mistake and set
its state back to "to do". No residue left — but the lesson cost something.

Hence the correct formulation, which is a definition before it is a parameter: **a cap is a
shutdown, not a quota.** On reaching the limit, the chain does not relaunch: it goes `OFF`
and waits for a human command.

## The density clause

There is a second way to exhaust the budget, and in practice it is the one that fires almost
every time.

A particularly rich paper — many formulas, many notes — **exhausts a run on its own**, even
when the paper count is still wide open. In fact, runs configured for five papers closed
**on the first** three times in the runs recorded here, on density alone.

**What density is, operationally.** It is the **number of notes extraction produces from a
single document**, counted once the document is finished. A document is *dense* when that
count goes over a configured threshold: in the runs told here the threshold was **10
notes**, and the documents that closed a run on their own had produced **12, 14 and 11**.
The threshold was later raised to 15 — it is a dial, not a law of nature.

It looks like a failure. It is not: it is the measure working. The real cost of a paper is
not measured in papers, it is measured in **how many things must be verified** — and a dense
document consumes in one go the attention budget that would have covered five thin ones. A
system that ignored density would pay the difference in the only currency that really
counts: **checks done worse toward the tail of the run**.

## Stopping in order

The rule that holds it all together is a single sentence, and it appears in every recorded
shutdown:

> **No unit left half-done.**

When the working space runs out — because the context is saturating, because the budget is
spent, because a stop command arrives — the chain **does not open a new unit** and **closes
the one in progress in good order**. The residual state is always explicit and always
reconstructible: how many notes written, how many passed through the gate, how many awaiting
a human decision, and from which exact step work resumes.

The practical result is that a shutdown is not an exceptional event to be handled: it is an
**expected state**, with its own line in the log. On resuming, you do not investigate what
happened — you read it.

## The point that holds for anyone

People who build agent chains tend to treat limits — tokens, context, budget — as
**constraints suffered**, to be worked around or deferred as long as possible.

Here they did the opposite: limits became **quality safeguards**. The limit does not degrade
the work, it protects it — because the alternative to stopping is not working more, it is
working worse exactly where attention has already run out. And quality degradation under
pressure **does not show up in the logs**: it shows up in checks that, without telling
anyone, get a little more perfunctory.

Stopping early and in order costs a restart. Stopping late costs a badly certified note that
nobody will ever reopen.

---

**Related decision:** [ADR-0007 — Run limits are shutdowns, not quotas](../architecture/decisions/0007-run-limits-are-shutdowns.md) — the rules told here, written as a decision.

**See also:** [ADR-0005 — The token cost is largely intrinsic to quality](../architecture/decisions/0005-cost-is-intrinsic-to-quality.md)
