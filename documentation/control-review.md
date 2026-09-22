# Control Review Approach

## Why This Section Matters

A common mistake in cybersecurity case studies is to see that a breach occurred and immediately write:

> "The company should implement MFA, vulnerability scanning, backups, and security training."

That may be unsupported.

loanDepot's public filings disclose a meaningful cybersecurity control and governance environment. The correct public-source question is therefore not always **"Does this control exist?"**

It is often:

> **"What evidence would I need to evaluate whether the disclosed control is designed appropriately and operating effectively?"**

## Example 1 — Penetration and Vulnerability Testing

### Public evidence

The company says it performs penetration and vulnerability testing.

### What I cannot conclude

I cannot determine from the public filing:

- testing frequency,
- exact scope,
- severity methodology,
- remediation time,
- whether critical findings remained open,
- whether retesting confirmed fixes.

### Evidence I would request internally

- testing policy and schedule,
- recent penetration-test report,
- vulnerability scan summaries,
- remediation tickets,
- SLA exception approvals,
- retest evidence,
- management reporting.

## Example 2 — Data Recovery Testing

### Public evidence

The company says it performs data-recovery testing.

### Evidence I would request

- backup architecture and scope,
- recovery policy,
- RTO/RPO targets,
- recent restore-test evidence,
- success/failure results,
- unresolved exceptions,
- backup integrity checks,
- lessons learned.

## Example 3 — Phishing Training

### Public evidence

The company says it conducts regular employee cyber/security training and phishing simulations.

### Evidence I would request

- completion rates,
- simulation click/report rates,
- repeat-failure process,
- role-based training,
- trend reports,
- management follow-up.

## Design vs. Operating Effectiveness

This distinction is important in audit and GRC:

**Design effectiveness:** If the control works as designed, is it capable of reducing the risk?

**Operating effectiveness:** Did the control actually operate as intended during the period being reviewed?

A public filing may tell us a control exists. It usually does not give enough evidence to conclude that the control operated effectively.

See `data/control-observations.csv` for the complete public-control review table.
