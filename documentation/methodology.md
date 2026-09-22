# Methodology

## Purpose

This project demonstrates a public-source cybersecurity risk assessment using a real incident. It is designed to show how a risk analyst can move from evidence to business-risk analysis without claiming knowledge that is not available publicly.

## Step 1 — Evidence Collection

I used a source-priority model:

1. **SEC filings** — primary source for company disclosures, financial impact, risk factors, and governance.
2. **State breach notifications** — primary/regulatory source for breach dates, affected population, and categories of personal information.
3. **NIST CSF 2.0** — reference framework for organizing cybersecurity outcomes.

Each source is assigned a Source ID in `data/sources.csv`.

Each factual observation receives an Evidence ID in `data/evidence-register.csv`.

## Step 2 — Evidence Boundary

A public-source assessment has an important limitation: it cannot see internal logs, architecture, policies, tickets, security-tool telemetry, or control-testing results.

Therefore:

- public disclosures are treated as facts when directly stated;
- risk scores are analyst judgments;
- recommendations are written as **validation or enhancement actions** rather than unsupported claims that controls are absent;
- unknown root cause is left unknown.

## Step 3 — Risk Statement Construction

Risk statements use the pattern:

**Threat/event + asset/business process + potential consequence**

A vulnerability is not automatically treated as the risk itself.

Example:

- Evidence: sensitive personal information was accessed.
- Risk: unauthorized access to sensitive customer data may lead to identity theft, privacy harm, litigation, regulatory exposure, and loss of trust.

## Step 4 — Likelihood Scale

Likelihood estimates the chance of the risk occurring or recurring within the scenario.

| Score | Label | Guidance |
|---:|---|---|
| 1 | Rare | Exceptional circumstances would be required |
| 2 | Unlikely | Credible but not expected under normal conditions |
| 3 | Possible | Could reasonably occur |
| 4 | Likely | Strong basis to expect continued exposure or recurrence |
| 5 | Almost Certain | Expected to occur frequently or persistently |

Likelihood scores are **analytical judgments**, not company-published values.

## Step 5 — Impact Scale

| Score | Label | Guidance |
|---:|---|---|
| 1 | Minimal | Limited business effect |
| 2 | Minor | Manageable localized disruption |
| 3 | Moderate | Noticeable operational, financial, or data impact |
| 4 | Major | Significant financial, legal, customer, or operational effect |
| 5 | Severe | Large-scale sensitive-data impact or major disruption to critical operations |

## Step 6 — Risk Rating

**Risk Score = Likelihood × Impact**

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–15 | High |
| 16–25 | Critical |

The number is a prioritization aid, not a substitute for judgment.

## Step 7 — Confidence

Each risk has an assessment-confidence field:

- **High** — strong direct public evidence supports the risk and impact.
- **Medium-High** — strong evidence exists, but some prospective judgment is required.
- **Medium** — relevant public evidence exists, but internal evidence would be needed for a stronger conclusion.

## Step 8 — Control Analysis

Publicly disclosed controls are not treated as automatically effective or ineffective.

For each control, the project asks:

1. What control does the company publicly say exists?
2. What does the public source *not* establish?
3. What evidence would an internal auditor/risk analyst request?
4. Which risk(s) and NIST CSF outcomes relate to that control?

This avoids the common mistake of equating "breach occurred" with "no controls existed."

## Step 9 — NIST CSF 2.0 Mapping

Risk treatments are mapped to relevant NIST CSF 2.0 categories. The mapping is intentionally high-level.

The six CSF 2.0 Functions are:

- Govern
- Identify
- Protect
- Detect
- Respond
- Recover

The project does not claim formal CSF conformance.
