---
# --- identity ---
video_id:
url:
title:
channel:
vendor_channel:            # true if the channel belongs to the tool's maker

# --- date: read everything else through this ---
published:                 # exact, YYYY-MM-DD, from video_info
date_source: video_info
era:                       # E1-prefile | E2-codeinterp | E3-gpts-agents | E4-connectors

# --- reach ---
views:
views_per_month:
likes:
comment_count:
duration_s:

# --- placement ---
level:                      # see ../README.md spectrum
found_by:                  # queries that surfaced it
rank:

# --- what it is ---
promise:                   # title claim, verbatim
tools: []
artifact:                  # chat thread | file | saved config | script | app | nothing
data_path:
still_accurate:            # yes | no | partly | unknown

# --- omissions: mentioned | gestured | not mentioned  (+ timestamp) ---
om_data_changes:           # (D) next month, when the data differs
om_reproducible:           # (I) could anyone else reproduce it
om_definition:             # (I) what the metric means, who decided
om_error_detection:        # (I) how you'd know a number was wrong
om_data_permission:        # (D) where the data went, whether that was allowed
om_maintenance:            # (I) who owns it when the author leaves

coded_on:
coded_by:
---

# <title>

## What it promises

## What it actually does

Steps as given, briefly. The point is the gap between this and the promise.

## The artifact

What exists when the video ends, and what state it is in.

## Omissions, with evidence

Quote or timestamp each. For era-dependent omissions, say what was possible at
the time of publication before counting it.

## Counter-evidence

Where this tutorial handles specification or validation better than the thesis
predicts. **Do not leave blank without having looked.**

## Comment signal

Verbatim, with like counts and dates. Breakage reports especially.

## Notes
