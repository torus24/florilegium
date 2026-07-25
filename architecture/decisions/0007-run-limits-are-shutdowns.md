# ADR-0007 — Run limits are shutdowns, not quotas

**Status:** accepted

---

## Context

A pipeline that works unattended has to decide **by itself** when to stop. Two opposite
failure modes were observed in the chain that preceded this project, and both were paid for:

- **It does not stop.** A cap of one document per run was read as a *quota per execution*:
  quota spent, so the chain scheduled its own restart and opened the next document with
  nobody at the keyboard. A counter that resets itself is not a limit, it is an engine.
- **It stops badly.** Breaking off in the middle of a unit of work leaves material on disk
  that nobody can classify when work resumes — notes written but not verified, verified but
  not signed.

Underneath both there is the reason the limits exist at all: quality degradation under
pressure **does not show up in the logs**. It shows up in checks that get a little more
perfunctory toward the end of a run, and it is invisible precisely to whoever is running
out of attention. → [journal/04](../../journal/04-when-the-chain-stops-itself.md).

## Decision

**Run limits are shutdowns, not quotas**, and they are formulated in five points.

1. **On reaching the limit the pipeline goes off and waits.** It does not relaunch, does not
   requeue, does not start the next unit. Re-arming is a **human act** — a decision taken
   outside the run, not a state the run can reach on its own.
2. **The governing limit is the occupied context, not the item count.** A cap in documents
   describes past averages; what really runs out is the working space. Two thresholds
   therefore: below the first, a new document may be opened; above it the run continues **one
   atomic unit at a time**, re-estimating at each one; above a **hard margin** no new unit is
   opened at all. In the originating chain the two thresholds were **65%** and **85%** of the
   context — dials, not laws of nature. Continuing past the limit *to finish the cluster* is
   forbidden.
3. **No unit left half-done.** A unit already opened is finished; everything not worked
   becomes explicitly **suspended** — a visible marker in the note itself saying the
   verification is not complete and the note must not be used at point of use, the
   verification field left empty, and the list of suspended notes written **both** in the run
   report and in the work queue. A state that lives only in the session that produced it does
   not exist.
4. **Suspended is not held.** Suspension comes from the limit and is resolved by resuming
   work; a **hold** comes from an unresolved verdict and is resolved by adjudication or
   quarantine. Two different states with two different exits: merging them would let a
   failed check disappear into a scheduling event.
5. **The limit is enforced, not recommended.** In the originating chain the declaration of
   context occupancy stayed *on paper* until a run signed six notes without a single written
   estimate. From then on the declaration is mechanical: a system hook **refuses** to
   complete a note's verification field until the current report carries at least one
   occupancy line, stating the estimate and how it was made. A rule that nothing enforces is
   not in force — the same reasoning as
   [ADR-0006](0006-reader-must-not-know-the-expected-answer.md).

## Consequences

- **What it says:** a shutdown is not an exceptional event to be handled — it is an
  **expected state**, with its own line in the log. On resuming you do not investigate what
  happened, you read it.
- **What it costs:** restarts, and work that spans several sessions. That is the trade-off of
  [ADR-0005](0005-cost-is-intrinsic-to-quality.md) seen from the scheduling side: stopping
  early and in order costs a restart, stopping late costs a badly certified note that nobody
  will ever reopen.
- **What it does NOT solve:** the occupancy figure is an **estimate**, declared as such. The
  rule does not make it exact — it forces it to be **written down and justified** before it
  can authorize anything. Nor does it protect against a limit set at the wrong value: the
  thresholds are calibration, and calibration is revisable.
- **Reusable lesson:** a limit that the role subject to it can **reinterpret** is not a
  limit. Write explicitly who ends the run, what re-arms it, and what the pipeline is
  forbidden to do once the limit is reached.
- **When to revisit:** if the orchestration stopped assuming sessions with a limited context
  (see the portability constraint stated in the README), these thresholds would have to be
  rewritten in terms of whatever the scarce resource becomes.

## Related journal entry

[journal/04 — When the chain stops itself](../../journal/04-when-the-chain-stops-itself.md)
