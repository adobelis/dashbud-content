"""Generate a sales pipeline XLSX for the hero carousel Google Sheets screenshot.
Modeled on a mid-market outdoor gear wholesaler with 15+ reps, 1000+ accounts,
heavy repeat business. Ridgeline Gear sells to specialty retailers, outfitters, etc.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Pipeline"

headers = ["Date Added", "Account", "City", "Contact", "Deal", "Order Type", "Amount", "Stage", "Rep", "Date Closed"]

# Styling
header_font = Font(bold=True, size=10)
header_fill = PatternFill(start_color="E8F0FE", end_color="E8F0FE", fill_type="solid")
link_font = Font(color="1155CC", underline="single", size=10)
currency_fmt = '"$"#,##0'
date_fmt = "MM/DD/YYYY"
thin_border = Border(
    bottom=Side(style="thin", color="E0E0E0"),
)

# date_added, account, city, contact, deal, order_type, amount, stage, rep, date_closed
rows = [
    # Closed Won — reorders and seasonal buys (the bread and butter)
    (date(2023,10,2),  "Trailhead Supply",         "Bend, OR",           "M. Kowalski",  "Fall '23 Restock",      "Reorder",     185000, "Closed Won",  "Sarah T.",    date(2023,11,14)),
    (date(2023,10,8),  "Blue Ridge Outfitters",     "Asheville, NC",      "D. Parsons",   "Holiday Floor Set",     "Seasonal",    92400,  "Closed Won",  "James R.",    date(2023,11,28)),
    (date(2023,10,15), "Lakeshore Provisions",      "Traverse City, MI",  "R. Okafor",    "Winter Collection",     "Seasonal",    147500, "Closed Won",  "Anna L.",     date(2023,12,10)),
    (date(2023,10,22), "Summit Creek Outfitters",   "Park City, UT",      "B. Hayward",   "Q4 Restock",            "Reorder",     68200,  "Closed Won",  "Kevin M.",    date(2023,11,30)),
    (date(2023,11,1),  "Piedmont Trail Co.",        "Charlottesville, VA", "S. Whitmore", "New Account Setup",     "New Account", 234000, "Closed Won",  "Rachel D.",   date(2024,1,8)),
    (date(2023,11,5),  "Iron Range Surplus",        "Ely, MN",            "C. Bjornson",  "Annual Contract",       "Reorder",     312000, "Closed Won",  "Anna L.",     date(2023,12,19)),
    (date(2023,11,12), "Tidewater Outdoor",         "Wilmington, NC",     "J. Koroma",    "Spring '24 Pre-book",   "Seasonal",    126800, "Closed Won",  "James R.",    date(2024,1,2)),

    # Negotiation — larger deals in progress
    (date(2023,11,18), "Granite Peak Sports",       "Bozeman, MT",        "K. Lund",      "Expansion - Footwear",  "Expansion",   558000, "Negotiation", "Sarah T.",    None),
    (date(2023,12,3),  "Northwoods Mercantile",     "Duluth, MN",         "T. Erickson",  "2024 Annual Contract",  "Reorder",     445000, "Negotiation", "Anna L.",     None),
    (date(2023,12,10), "Catamount Gear",            "Stowe, VT",          "E. Dubois",    "Regional Exclusive",    "Expansion",   189000, "Negotiation", "Mike P.",     None),

    # Proposal — mid-pipeline
    (date(2024,1,5),   "Cascade Gear Co.",          "Bellingham, WA",     "T. Nygaard",   "Q1 Restock",            "Reorder",     246000, "Proposal",    "James R.",    None),
    (date(2024,1,8),   "High Desert Trading",       "Flagstaff, AZ",      "P. Reeves",    "Spring Line Launch",    "Seasonal",    372000, "Proposal",    "Sarah T.",    None),
    (date(2024,1,12),  "Ozark Trail Supply",        "Fayetteville, AR",   "D. Nguyen",    "New Account Setup",     "New Account", 88500,  "Proposal",    "Lisa W.",     None),
    (date(2024,1,15),  "Adirondack Outpost",        "Lake Placid, NY",    "M. Ferraro",   "Seasonal Restock",      "Reorder",     154000, "Proposal",    "Rachel D.",   None),

    # Qualified — early stage
    (date(2024,1,18),  "Fox & Finch General",       "Hudson, NY",         "L. Chen",      "Pop-up Partnership",    "New Account", 45000,  "Qualified",   "Mike P.",     None),
    (date(2024,1,22),  "Bitterroot Dry Goods",      "Hamilton, MT",       "W. Greer",     "Spring Floor Set",      "Seasonal",    167000, "Qualified",   "Kevin M.",    None),
    (date(2024,1,29),  "Palmetto Provisions",       "Charleston, SC",     "A. Washington","New Account Setup",     "New Account", 215000, "Qualified",   "James R.",    None),

    # Prospect — top of funnel
    (date(2024,2,1),   "Copper Basin Outfitters",   "Missoula, MT",       "J. Whitfield", "Spring '24 Buy",        "New Account", 285000, "Prospect",    "Sarah T.",    None),
    (date(2024,2,3),   "Great Lakes Gear",          "Petoskey, MI",       "N. Patel",     "Introductory Order",    "New Account", 52000,  "Prospect",    "Anna L.",     None),
    (date(2024,2,5),   "Timberline Trading",        "Sandpoint, ID",      "R. Kowalczyk", "Q2 Restock",            "Reorder",     198000, "Prospect",    "Kevin M.",    None),
]

# Write headers
for col, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="left")

# Write data
for r, row_data in enumerate(rows, 2):
    dt_added, account, city, contact, deal, order_type, amount, stage, rep, dt_closed = row_data

    ws.cell(row=r, column=1, value=dt_added).number_format = date_fmt

    acct_cell = ws.cell(row=r, column=2, value=account)
    acct_cell.hyperlink = "#"
    acct_cell.font = link_font

    ws.cell(row=r, column=3, value=city)

    contact_cell = ws.cell(row=r, column=4, value=contact)
    contact_cell.hyperlink = "#"
    contact_cell.font = link_font

    ws.cell(row=r, column=5, value=deal)
    ws.cell(row=r, column=6, value=order_type)
    ws.cell(row=r, column=7, value=amount).number_format = currency_fmt
    ws.cell(row=r, column=8, value=stage)
    ws.cell(row=r, column=9, value=rep)

    closed_cell = ws.cell(row=r, column=10, value=dt_closed)
    if dt_closed:
        closed_cell.number_format = date_fmt

    for col in range(1, len(headers) + 1):
        ws.cell(row=r, column=col).border = thin_border

# Column widths
widths = [12, 24, 20, 14, 22, 14, 12, 14, 12, 14]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w

ws.freeze_panes = "A2"

out = "/Users/arthur/www/dashbud/content/scripts/ridgeline_pipeline.xlsx"
wb.save(out)
print(f"Saved to {out}")
