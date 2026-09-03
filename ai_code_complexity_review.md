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
