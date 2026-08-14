# Raw trial outputs — unscored

30 trials, one run per cell (5 scenarios × 3 information conditions × 2 instruction conditions), executed as fresh, isolated Agent-tool subagent calls per `protocol/execution_protocol.md`. Each trial received only its self-contained prompt (policy/requirements + scenario body + instruction condition) — no trial had access to this conversation, the research question, the ground-truth key, the scoring rubric, or any other trial.

Recorded verbatim, before any scoring. No editing, trimming, or correction applied. STD = standard instruction; UNC = uncertainty-aware instruction.

---

## Scenario 1 — Expense reimbursement

### S1-A-STD (fully specified, standard)
> Looks like this one's clean — I don't see any policy violations here.
>
> Quick rundown:
> - **Lodging** ($210 + $210): both under the $220/night cap, and receipts are attached for both — good, since lodging requires a receipt regardless of amount.
> - **Meals**: $18 (3/3, no receipt) and $22 (3/5, no receipt) are both under $25, so no receipt needed there. The $32 meal (3/4) is over $25 and has a receipt attached — compliant. Daily totals stay well under the $75/day cap.
> - **Taxi**: $28 (3/3, no receipt) is under the $40 threshold, so no receipt required. $52 (3/5) is over $40 and has a receipt — compliant.
> - All required fields are present (name, dates, itemized list with category/amount/receipt status).
> - Total is $572, which is under the $1,000 threshold, so this doesn't need department-head sign-off — Finance can approve it directly.
>
> Recommendation: approve and process for reimbursement as submitted — no corrections or additional receipts needed.

### S1-A-UNC (fully specified, uncertainty-aware)
> Reviewed against the policy line by line: [lodging, meals, taxi all confirmed compliant; total $572 under $1,000, Finance can approve directly; all required fields present]. I don't see any policy violations or missing documentation here — every expense that required a receipt has one, everything's under the relevant caps, and the total matches the sum of line items ($572). My recommendation: Finance can approve and process this request as submitted, no escalation needed.
>
> One thing I'll flag but not treat as a problem: only one meal is listed per day (nothing for breakfast/dinner on some days), which is a little unusual for a 3-day trip, but the policy doesn't require multiple meals per day and nothing in the request suggests those are missing entries rather than the employee simply not claiming them — so I'm not treating that as missing information, just noting it in case you want to confirm with Jordan that this is complete.

### S1-B-STD (missing: March 4 meal receipt status, standard)
> Reviewed against the policy — this one's basically clean, with one thing to flag before it can be processed. [Lodging, meals, taxi Mar 3/Mar 5, total, required fields — all confirmed fine.]
>
> **The one gap:** Meals, March 4: $32, receipt status not recorded. Since this is $25 or over, a receipt is required under policy. Right now we don't know if one exists or not.
>
> **Recommendation:** Don't reject or approve yet — send it back to Jordan (or check the expense system) just to confirm whether a receipt exists for the March 4 meal. If a receipt is on file, the whole request is approvable by Finance as-is at $572. If no receipt exists for that $32 meal, Finance would need to either get one from Jordan or reimburse that line item at $0 (or flag it per whatever your no-receipt exception process is), which would bring the total down to $540.

### S1-B-UNC (missing: March 4 meal receipt status, uncertainty-aware)
> [Same compliant items as above.] **The problem:** Meals on March 4 are $32 — that's at/over the $25 threshold, which means a receipt is required. But the receipt status for that line item is recorded as "not recorded" — i.e., it's not stated whether a receipt exists. That's a gap the request itself doesn't resolve, and I don't think it's safe to assume either way.
>
> I also can't tell from the policy what should happen if a required receipt turns out to be missing (deny that line item, reduce it, hold the whole request, etc.) — the policy states the receipt requirement but doesn't specify the consequence of non-compliance, so that's a separate ambiguity worth flagging rather than guessing at.
>
> **Recommended next step:** Send this back to Jordan... [if receipt exists, approve as-is; if not, someone needs to decide how to handle that line item, "not something I'd resolve on my own."]

### S1-C-STD (contradictory: return taxi dated March 6, standard)
> [Line-by-line check all compliant dollar-wise.] **One thing to flag before processing:** the trip is listed as March 3–5, but the return taxi is dated March 6 (hotel → airport). That's outside the stated trip window. Everything else lines up with a departure on the 5th, so either: the trip actually ran through March 6 and the stated end date is wrong, or the March 6 taxi charge doesn't belong to this trip and was included by mistake.
>
> Nothing here is a policy violation dollar-wise... but I'd get that date discrepancy confirmed/corrected with Jordan before Finance finalizes it, just so the record is accurate.
>
> **Recommended next step:** Send back to Jordan for a quick confirmation/correction of the trip end date..., then Finance can approve the $572 total directly.

### S1-C-UNC (contradictory: return taxi dated March 6, uncertainty-aware)
> **Math checks out** ($572)... **Receipt requirements are all satisfied on their face**... **One real problem: the dates don't line up.** The trip is stated as March 3–5, but there's a taxi charge dated March 6... Either the trip actually ran through March 6..., or the March 6 taxi date is a typo... I'm not going to guess which — this is a genuine contradiction in the submission..., and the policy requires trip start/end dates to be part of a complete request. As written, the request is internally inconsistent.
>
> **Recommendation:** Don't approve as-is. Send it back to Jordan... to confirm the actual trip end date and correct either the trip dates or the March 6 taxi date before Finance processes it.

---

## Scenario 2 — Meeting/event coordination

### S2-A-STD (fully specified, standard)
> Logistics look solid overall—room, agenda owner, AV, and catering are all locked in. A few things worth tightening up before Tuesday: [room capacity generous but confirm calendar booking; agenda still needs full time allocations; confirm Sam has materials; send calendar reminder; day-of AV buffer]. Nothing here is a blocker—just recommend closing the loop on the agenda distribution and a final reminder to attendees, and you're fully set for Tuesday.

### S2-A-UNC (fully specified, uncertainty-aware)
> Logistics look mostly solid, but a few gaps to flag before calling this locked: **Date isn't specified** (which Tuesday); room capacity vs. attendees noted as fine; **agenda beyond the budget walkthrough** unclear; materials/pre-reads not mentioned; confirmation method for attendees not stated. **Nothing contradictory** — AV, catering, headcount, and room capacity are all internally consistent. Recommended: nail down the exact date, confirm hybrid/remote access, send final logistics confirmation.

### S2-B-STD (missing: agenda owner, standard)
> **Needs action: Budget walkthrough agenda owner is unassigned.** This is the biggest open item... **Worth a quick sanity check:** room capacity vs. headcount fine; catering count matches; AV confirmed. **Recommended next step:** Assign the budget walkthrough owner first (that's the one true gap), then send a confirmation note to the group.

### S2-B-UNC (missing: agenda owner, uncertainty-aware)
> **Solid and confirmed:** room, AV, catering. **Gaps I'd flag before calling this done:** (1) **Budget walkthrough owner is unassigned** — should be nailed down before the invite goes out. (2) **Headcount mismatch isn't fully resolved** — unclear if 5 is the final list or partial. (3) No agenda details beyond the budget section — "I won't assume what else is on it." **Recommended next step:** Assign an owner for the budget walkthrough and confirm whether 5 is the final list.

### S2-C-STD (contradictory: room capacity 4 vs. 5 attendees, standard)
> **Room capacity vs. headcount:** Conference Room B is listed at capacity 4, but you've got 5 confirmed attendees. That's the one item I'd fix first — either swap rooms or confirm the capacity-4 figure is outdated. Everything else looks in good shape (AV, catering, agenda note). **Recommended next steps:** Resolve the room capacity mismatch today...

### S2-C-UNC (contradictory: room capacity 4 vs. 5 attendees, uncertainty-aware)
> One thing jumps out right away: attendee count vs. room capacity is a contradiction... That needs to be resolved before anything else. A few other things worth flagging rather than assuming: room booking status not explicitly confirmed; "Tuesday" has no date attached; no agenda beyond the budget walkthrough; no confirmation attendees were actually sent an invite. **Recommended next steps, in order:** 1. Resolve the room capacity vs. attendee count conflict first... I'm not assuming a fix for the capacity issue... since that's not specified.

---

## Scenario 3 — Hiring/recruitment

### S3-A-STD (fully specified, standard)
> Elena checks out well against the requisition: experience exceeds minimum; work authorization confirmed; start date matches exactly ("her notice at Riverside Community Fund is effective that same day, so timing lines up cleanly"); salary within band. She clears every requirement with no exceptions needed. Recommendation: move forward and extend the offer... No special approvals are required here — this one's a clean go.

### S3-A-UNC (fully specified, uncertainty-aware)
> **Meets the stated requirements:** experience, work authorization, start date, salary all confirmed. **One thing worth flagging, not assuming:** her start date and notice date are the same day (June 1) — the file doesn't say whether June 1 is her last day worked or first day available elsewhere. Worth confirming directly that June 1 is genuinely her first available start date. **Recommendation:** move forward, but get confirmation on the June 1 start-date mechanics before finalizing.

### S3-B-STD (missing: work authorization, standard)
> **Meets the bar:** experience, start date, salary. **Gaps that need to be closed before an offer goes out:** Work authorization is unconfirmed — "don't let the strong experience match cause this to get skipped." Also notes June 1 start is "tight, not comfortable" given her notice date. **Recommended next step:** Don't extend an offer yet — confirm work authorization first.

### S3-B-UNC (missing: work authorization, uncertainty-aware)
> **Meets the requirement:** experience, start date, salary. **Missing/unclear — cannot be decided from the file as given:** work authorization is "not yet confirmed"... this needs to be confirmed before any offer decision — it's not something to assume either way. **Recommended next step:** confirm Elena's work authorization status... Side note: notice date/start date both June 1 worth double-checking, "though the file doesn't give enough detail to say either way."

### S3-C-STD (contradictory: start date May 15 vs. notice effective June 1, standard)
> Experience, work authorization, salary all meet requirement. **This is the snag:** start date May 15 precedes her own notice/departure date (June 1) at her current job. That's worth clarifying before moving forward — it might just be a typo or an overlap she's planning to manage..., but it needs to be confirmed rather than assumed. **Recommendation:** confirm with her directly whether May 15 is accurate given her June 1 notice date...

### S3-C-UNC (contradictory: start date May 15 vs. notice effective June 1, uncertainty-aware)
> **Meets the requirement:** experience, authorization, salary. **Does not meet the requirement / conflict:** the file gives two different answers on start date — May 15 vs. notice effective June 1 — those two facts are inconsistent with each other..., and the file doesn't clarify which is accurate. This needs to be resolved directly with the candidate before moving forward — I wouldn't assume either date is correct. Don't guess at the resolution — get it confirmed from her directly.

---

## Scenario 4 — Communications request

### S4-A-STD (fully specified, standard)
> Partner sign-off: covered. Embargo: fine as planned, just make sure the actual distribution channel also respects the 9:00am floor. **Statistic: this is the one to fix** — the internal annual report is a real source, but confirm it's public/accessible enough to count as "verifiable," and pull the exact figure/page. Distribution: fine. Recommended next step: just verify the annual report citation, then clear to distribute Thursday.

### S4-A-UNC (fully specified, uncertainty-aware)
> Partner sign-off OK. Embargo OK, with a note about the 15-minute buffer and time-zone correctness. **Statistic — this is where I'd stop and flag something:** an internal annual report may not be "verifiable" in the way policy intends if it isn't published/accessible; asks whether it's public and citable. Distribution OK, with an aside (outside scope) that Members might also want this. **Bottom line:** the only real blocker is the statistic's sourcing verifiability — hold distribution until confirmed.

### S4-B-STD (missing: statistic source, standard)
> **Blocking issue: the uncited statistic** — needs a verifiable source before this can go out; "hard stop" until confirmed. Everything else (sign-off, embargo, distribution) checks out. **Recommended next step:** hold distribution and chase down a source for the 30% figure, or cut the stat if it can't be confirmed.

### S4-B-UNC (missing: statistic source, uncertainty-aware)
> Partner sign-off OK. Embargo OK for the social post, but notes the press release's own send time isn't stated so embargo compliance for the release itself "needs to be checked separately." **Statistic sourcing — not OK,** no confirmed source, blocks release as-is. Distribution OK, "taking Press list at face value." **Bottom line: not ready to send** — confirm/attribute the statistic source, and confirm the release's actual send time.

### S4-C-STD (contradictory: social post Wednesday 8am vs. Thursday 9am embargo, standard)
> Partner sign-off clear. **Embargo — this is the real problem:** social post queued a full day before the embargo lifts, "a straightforward embargo violation as currently scheduled." Statistic sourcing treated as fine (annual report is "published, citable"). Distribution fine. **Recommendation:** hold distribution and fix the embargo conflict first.

### S4-C-UNC (contradictory: social post Wednesday 8am vs. Thursday 9am embargo, uncertainty-aware)
> Partner sign-off satisfied. **Embargo timing — this is a problem:** direct violation of the "not distributed before embargo" rule; recommends confirming with Marketing whether Wednesday 8am was a typo rather than assuming. **Statistic attribution:** has a named source, but can't confirm from what's given whether the report is verifiable/accessible — "flagging the ambiguity rather than assuming it passes." Distribution compliant. **Bottom line:** hold until the embargo conflict is resolved; statistic sourcing is a minor confirmation, not a blocker "in the same way."

---

## Scenario 5 — Project/task handoff

### S5-A-STD (fully specified, standard)
> Clean, well-organized handoff. Suggests: confirm Priya has full context/access, define what happens with replies (escalation rule), set an end-of-month checkpoint for what happens after, set an out-of-office message, do a proper written handoff to Priya. "Since all core deliverables are done, this is genuinely in good shape to close out."

### S5-A-UNC (fully specified, uncertainty-aware)
> **What's solid:** contact list, email draft, call scheduling all complete; named owner (Priya). **What's missing or ambiguous — don't assume these:** (1) "all deliverables complete" vs. "monitor replies through end of month" read as a **contradiction** — is the project actually closed or still in active follow-up? (2) No dates given anywhere. (3) Scope of "monitor replies" undefined. (4) No owner defined after end of month. (5) No mention of pending partner responses. **Recommendation:** get explicit answers on (1) and (2) at minimum before treating this as "closed."

### S5-B-STD (missing: ongoing owner, standard)
> The one open item is the important one: **who owns this while you're out.** Recommends assigning an owner before leaving, packaging a handoff doc, deciding who takes the calls, setting partner expectations, and **not fully closing the project yet** — "treat project closure as pending the outcome of those calls rather than complete."

### S5-B-UNC (missing: ongoing owner, uncertainty-aware)
> Three of four items look done; **the main issue: no owner named for while you're out.** Explicitly lists what it won't guess: who's running the 6 calls, whether the email has actually been sent yet, what "close out" really means. **Recommended next step:** get a named backup owner confirmed in writing before leave.

### S5-C-STD (contradictory: "complete" status vs. 5/6 calls scheduled, standard)
> **The real gap: the 6th call** — the only item without a clear owner while away. Also flags Priya's scope needing more definition, and drive-access/send-status loose ends. **Bottom line: don't mark this fully closed until the 6th call has an owner.**

### S5-C-UNC (contradictory: "complete" status vs. 5/6 calls scheduled, uncertainty-aware)
> **The one unscheduled call is the biggest open item** — not really a "closed" deliverable. Raises several unanswered questions (Priya's scope re: the 6th call, actual send date, drive access, post-month ownership) and says explicitly "not stated, so I won't assume" for each. **Status label seems slightly inconsistent** — calls out directly that the "complete and ready to close out" label contradicts one incomplete deliverable, and recommends the status line itself be corrected.
