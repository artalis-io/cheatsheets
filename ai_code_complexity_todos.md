# TODOs: *Local Decidability as a Condition for Scalable Agentic Coding*

## Postponed review findings

### Evidence durability and artifact availability

Archive immutable snapshots of the primary evidence cited by the paper, especially:

- Ralph's dated 72-configuration diagnostic, including the configurations and recorded results.
- Keel's normative stream contract.
- Hull's cited architecture document.
- Sail's cited architectural roadmap.
- A manifest mapping each archived artifact to its repository, exact commit hash, and supporting claim in the paper.

Deposit the evidence in a durable archive such as Zenodo and obtain a DOI. After the archive exists, add an artifact-availability statement to the paper and supplement the mutable GitHub references with the immutable DOI. Describe this as an evidence archive or artifact package unless the archived material genuinely supports full reproduction of the reported results.

Do not add an availability claim before the archive and DOI exist.

### Citation verification before submission

Verify every reference against its current bibliographic record before submission, including author list, title, identifier, year, publication status, and venue. Replace arXiv citations with peer-reviewed proceedings or journal versions wherever those exist. Retain arXiv citations for works that remain available only as preprints.

Rejected review item: explicitly adding the word "preprint" only to references [9], [13], [14], and [15]. The arXiv identifiers already disclose preprint status, and selectively labeling those entries would be inconsistent with other arXiv citations such as [8] and [10]. Revisit labels only if required by the target venue's bibliography style, applying the rule consistently to all references.

## Rejected review findings

### Reduce the density of coined terminology

Rejected. The principal terms have distinct analytical roles and are defined where introduced:

- "Implementation-local" and "outcome-local" distinguish two dimensions of local decidability.
- "Matrix-coupled" and "emergent-outcome" distinguish separate complexity regimes.
- "Verification debt" identifies accumulated assurance work rather than ordinary technical debt.
- "Premature architectural hardening" identifies the process by which rapid implementation turns provisional boundaries into costly dependencies.

Removing these terms would reduce the framework's precision without materially improving readability. The tightened abstract addresses initial cognitive load without weakening the terminology used in the analysis.

## Pre-submission verification

### Model and tooling designations

Verify the paper's model and tooling claims against dated usage records and authoritative release information, including Claude Opus 4.6, 4.7, and 4.8; OpenAI GPT-5-series models through GPT-5.6; and Qwen3.6 and Qwen3.8 27B. If a public model name differs from an internal or tool-displayed identifier, use the externally verifiable designation in the paper or explain the distinction.

Perform this check together with the citation-verification task before submission.
