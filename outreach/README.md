# Outreach — Working Instructions

## CRM

### Source of truth: local CSVs
All CRM data lives in `outreach/crm/`:
- `contacts.csv` — all contacts (was `prospects.csv`)
- `interactions.csv` — touchpoint log (denormalized with name)
- `deals.csv` — pipeline tracking (denormalized with name)
- `goals.csv` — outreach goals and timeline
- `feedback.csv` — website feedback (denormalized with name)
- `README.md` — full schema documentation (proximity tiers, eras, field definitions)

### Google Sheets: periodic sync for viewing
The Drive API can only create new files, not update existing ones. Workflow:
1. Arthur asks to sync → agent creates new Sheet files from CSVs
2. Agent notes old file IDs to delete
3. Arthur deletes old versions in Drive

Current Sheets (synced 2026-08-11 ~2:15pm):
- **Dashbud CRM — Contacts**: `17PlalJn64sKCGUbdmsLk02-SPZgTtSc8H9r2LsuIOSI`
- **Dashbud CRM — Interactions**: `1QHne8lhxiUUeEZwriEx26B1EYbSlJsOEep1xPlEQ0qo`
- **Dashbud CRM — Goals**: `1vfwVQwlrtUEAMB9LlDebRYcnl9gYk9I1YHrukb78ABw`
- **Dashbud CRM — Feedback**: `1eLO7i6Rv0VkQdnZt5HU1RSWozVd5B8BIJ1BO4850vQA`
- **Dashbud CRM — Deals**: `1yLREoOBpOdsp-e3tGBG774F8dQhbgm2isskkFXg8NGc`

Old versions to delete from Drive:
- ~~`1vIS0mDQNbIHjPiLfjT4FjZAzuERNVPK8ORMZ1zNZ8zw`~~ (old Prospects)
- ~~`19JpPQtITdv5s7diw25u95Wh_wJRjjjGGuq_uUwycJvE`~~ (old Interactions)
- ~~`1WtaeJIFMbZNnPhqSJlMhq6S54eXhIEm5AvPuYmjXUII`~~ (old Deals)
- ~~`1N1hgOcNpVd8I8uXyoElL9osHODPTan8lYY0IkQNsWP0`~~ (old Goals)
- ~~`1YrZXS6HJ2j__oxiUcUGs9_0ICm4N0Zr-tJkmULFgTaM`~~ (old Feedback)
- ~~`1gsPk4bYlUo3B-MLOHWj4vwRDriRHaUuVYZhwL3IceUs`~~
- ~~`18pBcFeTU2M0FaW9w3tkaqjJCmnwEpDk2_lkDWMmc_Vw`~~
- ~~`1nwB1PIzB5qCWxJGJlEfn_P0N9xyQVsMZrw810P7aa7I`~~
- ~~`1v06vO93CjSJg7V-QWjeQQyf6gmG0eRAbjQC38FGziPI`~~

### LinkedIn export
`outreach/linkedin_export.csv` — raw LinkedIn connections (~1,500), lightly categorized. Mined for contacts using `scripts/contacts/mine_prospects.py`.

### Mining script
`scripts/contacts/mine_prospects.py` — searches linkedin_export.csv for contact candidates. Supports filtering by era, seniority, category, company, keyword, relevance, and `--not-in-crm`.

## Key resources
- `outreach/handoff.md` — full context for outreach sessions
- `outreach/advance_local_outreach.md` — Advance Local contact strategy and persona archetypes
- `outreach/arthur_personal/personal_contacts.md` — personal contacts
- `outreach/arthur_personal/nyu_law_evc_2026.md` — NYU Law event attendees
- `wiki/dashbud/messaging/elevator-pitches-v2.md` — pitches by business type and persona
