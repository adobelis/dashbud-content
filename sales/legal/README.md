# Sales Legal Process

Legal documents and review process for Dashbud sales deals.

## Directory structure

- `templates/` — standard agreement templates (BAA, NDA, MSA, etc.)
- `deals/` — executed and in-progress agreements, organized by customer

## When to use what

| Document | When | Notes |
|----------|------|-------|
| NDA | Before sharing product details or customer data schemas | Usually mutual NDA |
| BAA | Any prospect handling PHI (healthcare, benefits, etc.) | Required before they connect health-related data |
| MSA | Closing a deal | Main service agreement with pricing, terms, SLA |

## Review checklist

Before sending any agreement to a customer:

1. Start from the current template in `templates/`
2. Fill in customer-specific details (company name, contact, dates)
3. Flag any requested modifications or redlines
4. Review with Scott before sending non-standard terms
5. Save the final/executed version in `deals/<customer>/`

## Deal folder convention

Each customer gets a folder under `deals/`:

```
deals/
  omega-molding/
    nda_signed_2026-08-15.pdf
    msa_draft_v2.docx
    notes.md
  trillium-creek/
    nda_signed_2026-09-01.pdf
```

Use `notes.md` in each deal folder for tracking status, redline history, and review notes.
