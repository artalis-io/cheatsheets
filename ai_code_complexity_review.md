# Review: *Local Decidability as a Condition for Scalable Agentic Coding*

Assessment of `ai_code_complexity.pdf` against the hallmarks of a scientific IEEE publication.

## Overall framing

The right yardstick matters. This is not — and does not claim to be — a controlled empirical
study. It is a **practitioner experience/position paper** advancing a hypothesis (local
decidability as the explanatory variable for agentic-coding scalability). Judged as an IEEE
Software / ICSE-SEIP-style experience report, it is strong and largely publishable in its class.
Judged as a controlled empirical research paper, it would be rejected for lack of independent
evidence — but it explicitly and repeatedly disclaims that framing, so that would be an unfair
standard. This review holds it to the standard it sets for itself.

The logical arc is coherent and does not need re-engineering: problem statement (§1) → analytical
framework and taxonomy (§2) → four differentiated cases (§3) → synthesis (§4) → actionable
implications (§5) → threats (§6) → conclusion. The central claim is stated early, threaded
consistently, and paid off. That structural integrity is genuinely good and does not warrant rework.

## What is good

- **A clear, falsifiable thesis.** "Local decidability" is defined precisely enough
  (implementation-local vs. outcome-local), and the boxed central hypothesis anchors the whole
  paper. The thesis is memorable ("AI makes code cheap. It does not make complexity cheap.")
  without the memorability substituting for rigor.
- **Case selection is a real methodological strength.** Positive (Keel), converging (Hull),
  prospective (Sail), and *negative* (Ralph) cases. Including a negative/limiting case — and
  foregrounding it — is the single most credibility-building choice in the paper. Most
  practitioner write-ups quietly omit their failures.
- **The Ralph diagnostic is the empirical high point.** The dated 72-configuration stress table
  (0/24, 0/24, 8/24; 1.26× GLPK wall time) is concrete, and the paper *pre-empts its own
  over-reading* ("these configurations are not independent observations… not Ralph's overall
  solve rate"). That is exactly the epistemic discipline reviewers look for.
- **The complexity-regime taxonomy (Regimes 0–5)** is a genuine conceptual contribution, not just
  narrative. It gives the paper a reusable artifact and cleanly separates the two baseline regimes
  as out-of-scope.
- **Exemplary threats-to-validity treatment.** Section 6 plus in-text hedging (no counterfactuals,
  single practitioner, post-hoc documentation risk, model non-independence) is more candid than
  most published work. The point that agreement among models sharing training-derived assumptions
  is *not independent evidence* is sharp and correct.
- **Related-work positioning is current and specific** (SWE-bench, METR task-horizons, SAKE, the
  AI-smells audit), and the paper articulates precisely how its question differs.
- **Offers testable predictions** (e.g., the systems-expertise productivity differential may
  *widen* before it narrows), which is what a hypothesis paper should do.

## What should be improved

Limited to issues a competent IEEE reviewer would actually flag as material.

1. **Reproducibility / evidence durability — the most substantive weakness.** Nearly all primary
   evidence is self-citation to author-owned GitHub repositories ([1]–[5], [7]) with "accessed
   2026-09-02." These are mutable and, in some cases, private-looking; a reviewer cannot
   independently verify the central artifacts, and the record will rot. For an IEEE venue this is
   the gap most worth closing: archive immutable snapshots (Zenodo DOI / figshare) of at least the
   Ralph benchmark records and the contract/architecture docs, and add an artifact/data-availability
   statement.

2. **The central construct is never operationalized, even ordinally.** "Local decidability" carries
   the entire argument but is only ever assessed narratively; the four cases are placed into regimes
   by qualitative judgment. The paper concedes this, but the contribution would be materially
   stronger with even a *proposed* measurement protocol or proxy set (e.g., change-context breadth,
   cross-module edit fan-out, local-test-pass-vs-system-failure rate). §6's future-work list
   gestures at outcome measures but doesn't tie them back to *measuring local decidability itself*.

3. **Single-rater subjectivity in regime assignment.** The same person designed the theory, built
   the systems, and classified them — an unaddressed confirmation-bias surface (theory-author =
   system-author = coder). The threats section notes qualitative judgment generally, but not this
   specific circularity. A sentence naming it, and ideally any external corroboration of the regime
   placements, would help.

## Minor points (optional, not blocking)

- **Regime 5 (open-world) is populated only by external exemplars** (autonomous transport, ATC,
  etc.), not by any study case. Legitimate extrapolation, but it slightly undercuts the "grounded
  in four cases" framing at the top of the scale; one clause acknowledging that the scale extends
  beyond the evidence would be honest.
- **Several 2026 references are non-peer-reviewed preprints** ([9], [13], [14], [15]). Acceptable,
  but worth flagging them as preprints so claims resting on them aren't overweighted.
- **The abstract packs multiple long, clause-chained sentences.** Purely stylistic; tightening
  would improve readability but nothing is wrong logically.
- **High density of coined terms** (verification debt, premature architectural hardening,
  matrix-coupled/emergent-outcome, implementation- vs outcome-local decidability). Each is defined,
  so this is manageable, but it is close to the ceiling a reader can absorb in seven pages.

## Bottom line

The paper is coherent, intellectually honest, and makes a real contribution as an
experience/position paper; its argumentative arc does not need rework. The improvements worth
making are about **evidentiary durability and construct measurability**, not about logic or
structure. As an IEEE Software / ICSE-SEIP review, the recommendation would be **accept with minor
revisions**: (1) archive verifiable artifacts + add a data-availability statement, (2) propose at
least a proxy operationalization of local decidability, and (3) explicitly name the
theory-author/system-author circularity in the threats section. Everything else is polish.

One factual caveat not verifiable from the text alone: the forward-dated tooling and references
(Opus 4.8, GPT-5.6, Qwen3.8, arXiv IDs in the 2602/2606 range) are internally consistent with the
paper's 2026 setting, but any citation to a not-yet-existing or mis-numbered preprint will be
caught in review — worth a verification pass before submission.

---

# Part 2 — Re-review of Section IV (*What determines agentic tractability*)

Focused re-review after commit `2c2e9f7` ("Add testable predictions").

## What changed

The lone "productivity differential may widen" prediction that previously sat mid-paragraph has
been pulled out and consolidated into a new **§IV-E "Testable predictions"** subsection listing
five predictions; the preceding paragraph now ends cleanly on the asymmetry statement.

This is a solid improvement, for a specific reason: the five predictions are expressed in terms of
the three operationalization dimensions introduced in §II-A (change-context breadth, validation
locality, compositional reliability). That closes the chain a hypothesis paper needs —
*framework → measurable constructs → falsifiable predictions* — which is what makes it
scientifically respectable rather than merely evocative. Predictions #1, #2, and #5 are crisp and
directional.

## Fair critique of the current Section IV

Four genuine issues, ordered by how actionable they are:

1. **Structural: the closing "Alternative explanations" paragraph now falls *under* the "Testable
   predictions" subsection.** After the `== Testable predictions` heading, the final paragraph
   ("Alternative explanations remain plausible… the narrower claim…") belongs semantically to that
   subsection until the next `=`. So a section-level humility caveat is rhetorically trapped as the
   tail of a subsection titled "Testable predictions," which reads oddly. **Recommended fix:** move
   that paragraph to *before* `== Testable predictions`. This un-nests the caveat and lets §IV end
   on the five falsifiable predictions — a stronger close for a hypothesis paper than ending on
   hedging. This is the one change worth making.

2. **Prediction #3 (verification debt) lacks a proposed proxy, unlike #1/#2.** Predictions 1 and 2
   inherit measurable constructs from §II-A; prediction 3 asserts "verification debt should
   increase when…" but verification debt has only a conceptual definition — no suggested way to
   *observe* it. A reviewer will ask how the increase would be detected. One clause proposing a
   proxy (e.g., unresolved cross-component assumptions per unit of merged change, or growth in
   system-level failures attributable to previously-accepted local changes) would bring it up to
   the standard of its siblings.

3. **Prediction #4 is the softest and the only one untethered from the operationalization
   dimensions.** "systems-engineering expertise may become more strongly leveraged, initially
   widening… productivity differences" is double-hedged ("may," "initially") and "more strongly
   leveraged" is not directly measurable the way the others are. Defensible to include, but it is
   the weakest link in an otherwise sharp list — worth tightening the measurable claim or
   acknowledging it as the most speculative.

4. **Mild overlap between §IV-E and §VI.** Future-comparative-evaluation content now lives in two
   places: the predictions here and the "future evaluations should compare matched tasks… vary
   feedback latency and coverage" list in Threats to Validity. They don't contradict, but they are
   stated independently. A single cross-reference ("these predictions could be tested via the
   evaluation designs in §VI") would tie them together and avoid the reader feeling the paper says
   the same forward-looking thing twice.

## Verdict on Section IV

The section does its job as the synthesis: it abstracts cleanly from the four cases, keeps its
causal claims appropriately narrow (the closing paragraph explicitly retreats to "the narrower
claim"), and the new predictions subsection materially strengthens it. Nothing here is broken or
incoherent. Of the four points, only #1 (reorder the closing paragraph) is worth doing before
submission; #2 is a real but minor gap; #3 and #4 are polish. The logical arc is intact.

---

# Part 3 — Re-review after Section IV/VI refinement

Focused re-review after commit `2327580` ("Refine testable predictions and evaluation design").

## All four Part 2 findings resolved

1. **Structural reorder (Part 2 #1) → done.** The "Alternative explanations remain plausible…"
   paragraph now sits *before* `== Testable predictions`, so §IV ends on the five falsifiable
   predictions and the humility caveat is no longer trapped inside the subsection. Flow now reads
   correctly: limits of what the cases show → the predictions the framework nonetheless implies.

2. **Prediction #3 proxy (Part 2 #2) → done.** Now reads "verification debt, *measured by
   unresolved validation obligations and the delay between local acceptance and representative
   system-level evidence*, should increase when…" — a clean two-part observable proxy (count +
   latency), matching the measurability standard of predictions #1 and #2.

3. **Prediction #4 tightening (Part 2 #3) → done, and well.** The double-hedged "may become more
   strongly leveraged, initially widening…" is replaced by a proper interaction-effect hypothesis:
   "improvements in implementation capability should yield larger gains in reliable engineering
   throughput *under more experienced systems-engineering supervision than under less experienced
   supervision*." Directional, comparative, and directly testable via the "vary the
   systems-engineering expertise" design in §VI. The weakest prediction is now one of the sharper
   ones.

4. **§IV-E ↔ §VI cross-reference (Part 2 #4) → done.** §VI now opens "The predictions derived in
   Section IV could be tested by comparing matched tasks…", explicitly linking predictions to their
   evaluation designs. The prior duplication now reads as intentional structure.

## New nit introduced and fixed

The revised §VI sentence made "predictions" the subject, so the following "They should also
vary…" bound to the wrong antecedent (predictions don't vary expertise; evaluations do). Fixed in
this commit by replacing "They" with "Such evaluations."

## Verdict

Every substantive Part 2 point is retired, and the fixes are genuine improvements rather than
mechanical patches — #3 and #4 in particular are meaningfully stronger. Section IV now has a clean
*framework → measurable constructs → falsifiable predictions → evaluation design* arc across
§II-A / §IV-E / §VI. No outstanding issues in these sections. The remaining pre-submission item is
unchanged and lives outside these sections: the artifact archive + data-availability statement
(tracked in the todos).
