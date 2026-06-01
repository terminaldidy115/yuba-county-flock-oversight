# Yuba County Flock Oversight — Evidence Brief
**Purpose:** Companion to `Yuba_County_Flock_Oversight_Project.docx` (operational checklist). This document answers *why each piece of evidence matters* and maps documents to specific claims. It does not track task status — the checklist does that.

**Last Updated:** May 19, 2026 (added: Phase 2 CPRA final response #26-245 documented — full response by category, three flagged issues, 263/2025 identity confirmed; FBI nationwide ALPR procurement finding — national infrastructure context updated in conclusion table and §1D)
**Previously:** May 13, 2026 (added: portal field suppression finding §1G; §1A updated with field suppression caveat; vendor/platform layer added to conclusion table; cross-reference methodology documented)
**Target Audience:** BOS public comment (June 2026); DeFlock NorCal coalition; potential media/legal referral
**Argument Structure:** Two primary pillars → shared conclusion of inadequate oversight architecture

---

## Table of Contents

1. [Pillar 1 — SB 34 / Civil Code §§ 1798.90.5 et seq. Compliance Failures](#pillar-1)
   - 1A. Blank Reason Rate: ~58% of Searches Undocumented
   - 1B. Audit Log Integrity: Backdating and Portal Self-Contradiction
   - 1C. Five-Way Data Retention Conflict (incl. Policy 433 § 433.8 Annual Audit Requirement)
   - 1D. Outside-Agency Network Access Without Disclosed Authorization
   - 1E. HaveIBeenFlocked.com (HIBF) Dataset — Third-Party Corroboration of YCSO Search Activity
   - 1F. Flock's December 2025 Platform Changes Placed YCSO in Automatic Non-Compliance
   - 1G. Transparency Portal Field Suppression — Vendor-Controlled Definition of Transparency
2. [Pillar 2 — Measure K Governance Conflict](#pillar-2)
   - 2A. Structural Conflict: Undersheriff Chairs Committee Reviewing His Own Department
   - 2B. Applicable Legal Standards
3. [Supporting Argument — Permitting Gaps (Track B)](#track-b)
   - 3A. Encroachment Permit Inventory vs. Known Camera Deployment
   - 3B. Starbend Boat Ramp: MOU Without a Permit
   - 3C. Cross-Agency Hardware in Yuba County ROW
4. [Supporting Evidence — Effectiveness Claim Rebuttal](#effectiveness)
   - 4A. Crime Clearance Rate Analysis
   - 4B. Facebook Notification Analysis
   - 4C. Peer Policy Comparison
   - 4D. "Game Changer" — Vendor Language Laundered as Independent Assessment
5. [Contractual Anchor Documents](#contracts)
   - 5A. 2022 Master Services Agreement (Original)
   - 5B. 2025 MSA Renewal
   - 5C. OMNIA Contract (RS250203)
   - 5D. JAG Grant Award (FY24)
   - 5E. YCSO ALPR Policy 433 (October 20, 2022; reissued December 18, 2025)
6. [CPRA Status — Outstanding Records](#cpra)
7. [Governance Gap — Shared Conclusion](#conclusion)

---

<a name="pillar-1"></a>
## Pillar 1 — SB 34 / Civil Code §§ 1798.90.5 et seq. Compliance Failures

**Core legal standard:** SB 34 (Statutes of 2015, Ch. 532) is codified at **California Civil Code §§ 1798.90.5 et seq.** — not Vehicle Code § 2413. Vehicle Code § 2413 governs CHP specifically (60-day retention, no data sales, annual Legislative report) and is not the operative statute for county sheriff's offices. The AG's 2023 enforcement bulletin confirms: SB 34, codified at Civil Code § 1798.90.5 et seq., establishes privacy and documentation requirements for California LEAs collecting, storing, using, or sharing ALPR data. **Use Civil Code citations at BOS — not Vehicle Code § 2413 — or county counsel will use the error to discredit the framing.**

The operative obligations for YCSO are:
- **Civil Code § 1798.90.51** — requires ALPR usage and privacy policy to be publicly available in writing and posted conspicuously
- **Civil Code § 1798.90.52** — requires written usage and privacy policy governing authorized purposes, data security, access controls, and training
- **Civil Code § 1798.90.53** — requires annual report to governing body on ALPR usage
- **Civil Code § 1798.90.55(b)** — protects ALPR *detection data* from disclosure (YCSO has misapplied this to deflect administrative governance record requests — a documentable misapplication)

The documentation obligation attaches to the YCSO deputy initiating each search — it cannot be delegated to Flock or satisfied by a vendor-hosted portal. MSA Section 3.2 makes SB 34 compliance an affirmative contractual warranty borne solely by YCSO.

---

### 1A. Blank Reason Rate: ~58% of Searches Undocumented

**The claim:** More than half of YCSO's logged Flock searches from February 2, 2026 onward contain no documented justification in the reason field.

**Key findings:**
- ~53% blank reason rate confirmed from YCSO's own public Transparency Portal CSV export
- This figure is a **post-December 2025 baseline** — the Flock portal format change (eliminating officer-level identifiers) occurred in December 2025; Tom's dataset begins February 2, 2026, after the change took effect
- The blank reason rate is an **independent finding** from the after-hours concentration (44–45%); they are not compounding findings and must not be presented as such without specific evidence linking them
- YCSO's own portal policy statement reads: *"All system access requires a valid reason and is stored indefinitely"* — this directly contradicts the downloadable data on the same page, where ~53% of reason fields are blank
- The policy statement is YCSO-authored (not Flock-authored), making YCSO the owner of the self-contradiction

**Documents:**
- **Flock Transparency Portal CSV exports** (scraped data, `Master Audit.xlsx`, sheet: `search_audit_pacific`) — primary quantitative source
- **YCSO public portal policy statement** — source of the self-contradicting text; screenshot/archive should be preserved

**Specific claims supported:**
- YCSO's own disclosure standards are internally inconsistent
- A ~58% blank rate constitutes a facially deficient audit trail under § 1798.90.52's documentation requirement
- YCSO cannot satisfy SB 34 by pointing to a Flock-hosted portal when that portal's own data shows half of searches have no documented basis
- **Two independent legal bases for this finding:** (1) Civil Code § 1798.90.52 (SB 34 documentation requirement); (2) YCSO's own Policy 433 § 433.6(e), which requires a documented reason for each search — YCSO is violating its own policy, not just state law

**Critical update — May 13, 2026 (portal field suppression finding):**
Cross-referencing the Transparency Portal CSV export against HIBF third-party audit records of the same search events reveals that the ~53% blank rate is **materially overstated as a measure of officer non-compliance** — and simultaneously reframed as a more serious structural finding:

Flock's search reason field is a **two-part structure**: (1) a drop-down category the officer selects (e.g., "Drugs/Narcotics," "Wanted Person (Arrest Warrant/Fugitive)," "Sex Offenses," "Destruction/Damage/Vandalism of Property") plus (2) a free-text sub-field where the officer types a specific reason. YCSO's Transparency Portal CSV exports **only the free-text sub-field**. When an officer selects a drop-down category but leaves the free-text sub-field blank, the portal exports a blank row — and that blank is counted in the ~53% figure.

Buena Park PD's audit export (ingested by HIBF) captures **both fields concatenated**, revealing entries like `"Drugs/Narcotics - "` (category selected, no sub-field text) that appear as blank in the YCSO portal export. Of 52 February 2026 events matched between the portal CSV and HIBF by timestamp, 9 portal-blank entries show a populated category in the HIBF record — meaning those searches were not entered without any justification; they were entered with a category selection that the portal simply does not surface.

**What this means for the argument:**
- The ~53% blank rate should no longer be presented as "53% of officers entered nothing" — it must be restated as "53% of portal exports show a blank free-text field, but an unknown proportion of those had a drop-down category selected that the portal does not disclose"
- This **does not weaken the compliance argument** — it sharpens it. The portal is now provably configured to suppress a field that Flock captures and other agencies' audit exports include. YCSO's own "transparency" mechanism is structurally incomplete by vendor design
- The correct framing shifts from "officers aren't documenting searches" to "the portal YCSO controls doesn't show you what officers actually entered" — a transparency architecture failure, not just an officer behavior failure
- See **§1G** for the full portal field suppression analysis

**Gaps / what this doesn't prove:**
- Cannot determine whether blank entries represent intentional omission, system failure, or officer negligence — requires Phase 2 internal log CPRA
- Cannot confirm whether internal YCSO logs contain justifications that simply weren't entered into the portal field
- The blank rate is a post-change baseline; pre-December 2025 comparison data would require a separate historical pull
- The true proportion of "blank" portal entries that actually have a drop-down category selected cannot be determined from HIBF alone — HIBF only captures searches that hit other agencies' networks; the full universe requires Phase 2 internal log production

---

### 1B. Audit Log Integrity: Backdating and Portal Self-Contradiction

**The claim:** YCSO's audit log contains retroactively added or backdated entries, undermining its reliability as a compliance record.

**Key findings:**
- Backdated/retroactive log entries detected in the downloaded audit data — entries appearing with timestamps inconsistent with sequential portal chronology
- This is **structurally significant**: a backdated audit log cannot serve as contemporaneous documentation under § 1798.90.5 et seq.; it proves the log is being modified after the fact rather than recorded at the time of each search
- The Transparency Portal simultaneously asserts full compliance ("stored indefinitely") and produces data that contradicts that claim — two sources from the same agency, on the same page, saying opposite things

**Documents:**
- **`Master Audit.xlsx` / `search_audit_pacific.xlsx`** — source of backdating analysis; timestamps and entry sequence
- **YCSO Transparency Portal** (archived screenshots) — source of the policy statement vs. data discrepancy

**Specific claims supported:**
- The audit log is not a reliable contemporaneous record
- Evidence of backdating directly undermines YCSO's ability to assert § 2413 compliance after the fact
- The portal self-contradiction is independently presentable to BOS without requiring technical data explanation — it's a simple "their website says X; their data shows not-X" argument

**Gaps / what this doesn't prove:**
- Whether backdating was intentional or a system artifact (e.g., delayed sync from Flock's servers) — requires Phase 2 internal log production to resolve
- Backdating alone does not prove misconduct, but it does prove the audit log is not a reliable compliance mechanism

---

### 1C. Five-Way Data Retention Conflict

**The claim:** YCSO's data retention period is simultaneously defined by five different documents with no single controlling standard — and YCSO's own policy does not match any executed contract term.

**The five conflicting standards:**
| Source | Retention Period | What it covers | Citation |
|---|---|---|---|
| Flock platform default (MSA § 1.15) | 30 days rolling | Vendor-side footage purge | MSA § 1.15 |
| 2025 BOS-signed Order Form header (Exhibit A) | **30 Days** (stated Retention Period field) | Order Form's own stated retention — conflicts with extended add-on purchased on the same document | Order Form header, `Flock_Safety_signed_by_BOS.pdf` p.3 |
| March 2022 amended contract special term | 65 days | Unknown — vendor-side, YCSO-side, or both? | `Agenda_Item_3332022`, Special Terms |
| YCSO Policy 433 § 433.5 | 60 days (Flock vendor purge) / up to 1 year (YCSO server) | Two-tier: 60-day vendor purge; YCSO may retain on own servers up to 1 year | Policy 433 § 433.5 |
| 2022 MSA Order Form / 2025 BOS Order Form | Up to 1 year purchased (extended add-on) | Extended retention purchased for cameras | 2022: $300 × 25 cameras; 2025: $267.90 × 26 cameras |

**Key findings:**
- The 2022 MSA Order Form shows YCSO purchased **extended data retention** for all 25 cameras at $300/camera/year — establishing a one-year contractual entitlement
- The **2025 BOS-signed Order Form** (`Flock_Safety_signed_by_BOS.pdf`, Exhibit A, p.3) **simultaneously states a 30-day retention period in its header field** while purchasing an "Extended data retention (Up to 1 Year)" add-on for 26 cameras at $267.90/camera ($6,965.40 annually) — a direct internal contradiction within the same executed document, signed by BOS Chair Gary Bradford and certified by County Counsel, Janet Bender on August 26, 2025. This is now the sharpest single-document illustration of the retention framework's incoherence: the county signed a document that says "30 Days" at the top and buys a one-year extension on the same page
- The March 2022 amended contract special term says **"65 days"** — a figure that appears nowhere in Policy 433 (which says 60 days for vendor-side) and nowhere in the original MSA; the source and meaning of "65 days" is unresolved
- Policy 433 § 433.5 is a **two-tier structure**: Flock purges footage at 60 days on the vendor side; YCSO may retain data on its own servers for up to one year — the "60-day" figure commonly cited in research materials describes only the vendor-side purge, not YCSO's total retention authority; this two-tier framing is confirmed identical in both the 2022 policy text and the 2025 policy release (`YCSO_2026_Policy_Release.pdf`) — the conflict is not a drafting artifact but a sustained structural inconsistency
- The research summary's characterization of "Policy 433: 60 days" is therefore an oversimplification — YCSO has authority to retain for up to a year on its own servers; whether it exercises that authority is unknown
- **Policy 433 § 433.8 — Annual Audit Requirement:** Policy 433 requires an annual audit memorandum documenting at least 10 sampled searches reviewed per year, submitted to the Sheriff — this internal audit mechanism has never been disclosed and is a direct Phase 2 CPRA target
- Peer agencies (Marysville PD, Wheatland PD) both use **one-year minimum** under Government Code § 34090.6 with explicit statutory citation — YCSO has no comparable statutory anchor in its policy

**Specific claims supported:**
- YCSO's retention framework is internally contradictory across at least five documents with no single controlling standard
- The 2025 executed Order Form contains an internal self-contradiction on its face — "30 Days" retention stated, one-year extension purchased — in a document signed by the BOS Chair and approved by County Counsel
- The "65-day" March 2022 special term matches neither the policy (60 days vendor-side) nor the purchased entitlement (1 year) — its origin and meaning should be demanded via CPRA
- YCSO is an outlier below the regional peer standard with no statutory justification
- Policy 433's § 433.8 annual audit requirement has never been disclosed — either the audits are being conducted and withheld, or they are not being conducted at all; both are significant
- BOS framing: "Your own policy requires an annual audit of Flock searches. Has that audit been done? Where is it?" / "Your Chair signed a contract that says '30 Days' on the same page where you paid for a year of storage. Which is it?"

**Gaps / what this doesn't prove:**
- Policy 433 § 433.5 two-tier framing (60-day vendor / 1-year YCSO) confirmed against both the 2022 policy text and the 2025 policy release (`YCSO_2026_Policy_Release.pdf`) — language is identical across both versions; the retention conflict is not a drafting artifact but a sustained structural inconsistency
- Does not establish which retention period is actually being applied in practice — Phase 2 internal deletion logs needed

**Documents:**
- **`Flock_Safety_signed_by_BOS.pdf`** (Aug 26, 2025, signed by Gary Bradford as BOS Chair) — Exhibit A Order Form; Retention Period field states 30 Days; Extended data retention add-on: $267.90 × 26 cameras = $6,965.40/year; FlockOS Advanced Package: $14,250/year; Annual recurring total: $135,215.40; Contract total (2-year): $273,850.80; references OMNIA Contract #RS250203; approved as to form by County Counsel
- **`Agenda_Item_2142022_BOS__Flock.pdf`** (Feb 14, 2022 BOS agenda) — original MSA Order Form; extended retention line item ($300 × 25 cameras = $7,500/year)
- **`Agenda_Item_3332022.pdf`** (Mar 3, 2022 BOS agenda) — amended contract; retention noted as "65 days" in special terms
- **`Agenda_Item_2632025_BOS__Flock.pdf`** (Feb 26, 2025 BOS agenda) — current MSA (renewed); MSA § 1.15 establishes 30-day Flock default
- **`ALPR_policy_102022.pdf`** — Policy 433 § 433.5 (two-tier retention); § 433.8 (annual audit requirement)
- **`YCSO_2026_Policy_Release.pdf`** — confirms Policy 433 § 433.5 retention language unchanged in 2025 version
- **`Marysville_PD_ALPR_Policy_24_May_2023.pdf`** / **`Wheatland_PD_ALPR_Policy_7_Jun_23.pdf`** — Lexipol Policy 426, § 426.4: one-year minimum citing Gov. Code § 34090.6

---

### 1D. Outside-Agency Network Access Without Disclosed Authorization

**The claim:** YCSO's purchased Flock tier includes statewide and/or nationwide network access, meaning agencies outside Yuba County can query YCSO-collected plate data and vice versa, without any public disclosure of the participating agencies or authorization framework.

**Key findings:**
- YCSO's OMNIA contract (RS250203) FlockOS features table explicitly lists **Statewide Network** and **Nationwide Network** (License Plate Lookup Only) as purchased features
- The FlockOS description for Nationwide Network reads: agencies "leverage a nationwide system boasting 10 billion additional plate reads per month" — YCSO's own contract confirms this access is active
- **2025 BOS-signed Order Form** (`Flock_Safety_signed_by_BOS.pdf`) confirms **FlockOS Advanced Package** as a purchased line item ($14,250/year), independently corroborating the OMNIA contract analysis — the tier is now confirmed by two executed documents. The same Order Form's **FlockOS Features & Description table** (p.5) provides contractually binding, plain-language definitions of all four purchased network access tiers: State Network = "look up license plates on all cameras opted into the Flock Safety network within your state"; Nationwide Network = agencies "no longer have to rely on just their devices alone... 10 billion additional plate reads per month"; Law Enforcement Network Access = "direct access to evidence detection devices from Law Enforcement agencies outside of your jurisdiction"; Community Network Access = "direct access to feeds from privately owned Flock Safety LPR cameras located in neighborhoods, schools, and businesses." These are not Flock marketing materials — they are feature definitions in a BOS-signed contract, approved as to form by County Counsel, Janet Bender
- **MSA Section 4.2 ("Non-Agency End Users")** governs outside-agency access; this section has not been produced by YCSO in response to CPRA 26-136 (outstanding)
- **Flock Network Sharing document** (`Flock_NetworkSharing.pdf`, dated 1/29/2026): confirms **Yuba County Sheriffs Office** shares with "Sacramento County CA SO, Sacramento County CA SO (Condor), Sacramento County CA SO (WSIN FLEX), Rancho Cordova CA (Sacramento SO)" — multi-entity bilateral sharing is live
- The Woodland, CA reference point: Woodland audit data shows **99.92% of searches on Woodland's network by outside agencies** — this figure is **from Woodland, not Yuba County**; the Yuba-specific equivalent is still awaited via CPRA 26-136 (Request for authorization/access structure)
- NCRIC and WSIN appear in related agency sharing networks; both are federal fusion centers with open-ended downstream access. YCSO's own contract confirms WSIN FLEX network sharing

**Documents:**
- **`Flock_Safety_signed_by_BOS.pdf`** (Aug 26, 2025, signed by Gary Bradford as BOS Chair) — Exhibit A Order Form confirming FlockOS Advanced Package ($14,250/year); p.5 FlockOS Features & Description table with contractually binding plain-language definitions of all four purchased network access tiers; approved as to form by County Counsel
- **`PRAR_Response_Flock_OMNIA_Contract.pdf`** — OMNIA contract RS250203; FlockOS features table listing Statewide/Nationwide Network access; Flock's certification that no proprietary information is contained (forecloses trade secret CPRA exemption claims)
- **`Flock_NetworkSharing.pdf`** (1/29/2026) — Flock's own data sharing disclosure; lists Yuba County Sheriffs Office sharing with Sacramento County SO and WSIN FLEX
- **`Agenda_Item_2632025_BOS__Flock.pdf`** — current MSA; Section 4.4 (Data Distribution) and Section 3.2 (compliance warranty)
- **CPRA 26-136 (outstanding)** — authorization/access structure, interagency data sharing agreements

**Specific claims supported:**
- YCSO is participating in multi-agency plate data sharing that was never disclosed to the BOS or the public in any agenda item
- Civil Code § 1798.90.52 requires a written usage and privacy policy that identifies agencies with which ALPR data may be shared — no such public disclosure exists in any YCSO document
- The "local public safety tool" framing offered to the BOS and community is contradicted by the active statewide/nationwide network tier, confirmed in a BOS-signed contract
- YCSO cannot claim the sharing is Flock-initiated: MSA Section 4.4 requires customer authorization for data distribution to third parties; the BOS-signed Order Form defines these features as intentionally purchased capabilities, not incidental platform behavior

**Gaps / what this doesn't prove:**
- The networkCount tier clustering analysis (5 apparent tiers; expanded regional tier = 75.7% blank) is **inference from data patterns**, not confirmed by a Flock data dictionary — present as open question, not finding; the Flock data dictionary CPRA is still outstanding
- The Woodland 99.92% figure is Woodland-specific and should never be cited as a Yuba County statistic; the Yuba-equivalent requires CPRA 26-136 production
- Does not establish that outside-agency access has caused a specific harm — the compliance gap argument is structural, not outcome-based

**Update — May 19, 2026 (FBI procurement context):**
FBI procurement records published May 18, 2026 (404 Media) confirm the agency is seeking up to $36 million for nationwide SaaS ALPR access, with Flock and Motorola identified as the likely fulfilling vendors. The FBI's Directorate of Intelligence — its intelligence community arm — is the contracting entity. ICE/HSI, the Secret Service, and the Navy's criminal investigation division previously had access to Flock's nationwide network, per Senator Wyden's October 2025 letter.

This is atmospheric context, not a YCSO-specific evidentiary finding. **Do not present it as a Yuba County fact.** Its strategic value is reinforcing the BOS framing that the "local public safety tool" characterization is structurally false: YCSO's cameras are nodes in a network that federal intelligence agencies are actively seeking to acquire at the national level. The governance gap is not hypothetical. Use to close the BOS argument, not to open it.

**BOS framing (use sparingly, closing context only):** "The Board approved this as a local public safety tool. This week, federal procurement records confirmed the FBI is seeking up to $36 million to buy nationwide access to this same network. YCSO's cameras are part of that infrastructure. This Board has never been told that — and the governance documents we've requested would tell you whether YCSO has procedures governing federal access requests. They haven't been produced."

---

### 1E. HaveIBeenFlocked.com (HIBF) Dataset — Third-Party Corroboration of YCSO Search Activity

**The claim:** YCSO's Flock search activity appears in audit logs obtained via public records requests by journalists and researchers from agencies across California and beyond — independently corroborating the network scope, search pattern, and documentation quality findings developed from YCSO's own Transparency Portal data.

**Source and methodology:** HaveIBeenFlocked.com aggregates ALPR audit records obtained through public records requests filed against agencies that publish or are compelled to disclose their Flock network audit logs. The HIBF dataset for YCSO (agency ID 3677, downloaded May 12, 2026) contains 4,931 rows covering April 2024 through February 27, 2026, representing YCSO searches that were captured in other agencies' audit exports. This dataset is entirely independent of YCSO's own Transparency Portal — it is sourced from third-party government audit records.

**Key findings:**

*Network scope — confirmed from the outside:*
- YCSO search activity was captured in audit logs from: El Cerrito PD, Mountain View PD, San Jose PD, Capitola PD, Santa Cruz PD, Buena Park PD, El Cajon PD, and agencies in Arkansas and Washington state, among others — at least 20 distinct source audit files
- This independently corroborates the statewide/nationwide network access argument: YCSO's queries reached those agencies' camera networks, and those agencies' audit systems recorded it
- The source agency breadth is self-explaining to a lay audience in a way that network count numbers alone are not: "YCSO's searches showed up in audit logs from Buena Park and Arkansas" requires no statistical interpretation

*Five searches with nationwide + Canada geographic filter:*
- Five unique YCSO search events used a geographic filter explicitly listing all 50 U.S. states plus Canada — meaning those searches were scoped to the entire Flock network including Canadian agency participants
- This is not an inference; the `filters` field in the HIBF JSON record reads: *"alabama, alaska, arizona, arkansas, california, canada, colorado, connecticut..."* through all 50 states
- Policy 433 contains no provision governing cross-border queries; no interagency agreement covering Canadian network access has been produced or disclosed

*Vehicle + filter combination on blank-reason searches — new finding:*
- The HIBF JSON data contains a `filters` field showing the geographic and vehicle-attribute scope officers applied to each search
- Searches with blank reason fields (`reason: ""`) are found with filters such as `SUVNissanwhitecalifornia`, `PickupFordsilver_greycalifornia`, `SedanToyotasilver_grey,greencalifornia`, and partial plate fragments (`9JWJ`, `8BIW`, `8896W1`)
- These are deliberately targeted, operationally specific queries — make, model, color, state, and partial plate — with zero documented justification entered in the reason field
- This combination is the clearest single illustration of the SB 34 documentation failure: the specificity of the filter proves investigative intent; the blank reason field proves the absence of any recorded basis for that specific investigation
- **BOS framing:** "These aren't accidental omissions. Officers were filtering searches by vehicle type, color, and partial plate — deliberately targeted queries — with no reason entered whatsoever."

*Training searches at nationwide scale — confirmed unredacted:*
- Two events with reason `"training demo"` (October 24, 2024) and one with reason `"training"` (November 3, 2024) queried 5,187–5,231 networks simultaneously
- These appear in the 110 fully unredacted HIBF records — officer name partially visible, geographic filter (`California`) present, network counts confirmed
- Using a live investigative surveillance system at nationwide scale for training purposes, with no mechanism in the audit log to distinguish training queries from active investigations, is a supervision and governance failure independent of the blank-reason argument
- **BOS framing:** "YCSO used this system to conduct training exercises querying over 5,000 agency networks simultaneously — the same scope as an active criminal investigation — with no oversight mechanism to distinguish training queries from real ones in the audit log."

*N24-116 — case number as reason field placeholder:*
- "N24-116" is the single most common non-blank reason entry in the HIBF dataset: 93 unique search events spanning August 2024 through February 2026
- All N24-116 events searched 4,900–5,739 networks simultaneously; the `case_number` field is blank in every one
- An internal case designator entered in the reason field tells nothing about the investigative nexus to the plate being queried — it is not the purpose statement SB 34 contemplates
- This pattern demonstrates that even when YCSO fills in the reason field, the entries are not always substantively compliant — a case number is the appearance of compliance, not compliance
- **BOS framing:** "Even when a reason is entered, it isn't always meaningful. 93 searches spanning 18 months list only an internal case number — no description of the investigation, no stated nexus to the vehicle being queried."

*Inbound audit log — absence as evidence:*
- The HIBF dataset contains only YCSO's outbound searches (queries YCSO made against other agencies' networks)
- The inverse record — an inbound audit log showing which outside agencies queried YCSO's cameras — would be YCSO's own network audit export
- No such record appears in HIBF because YCSO has never published one; agencies like El Cerrito, San Jose, El Cajon, and Buena Park produce monthly audit exports that HIBF ingests. YCSO produces nothing equivalent
- CPRA 26-136 requested interagency access records; the May 6 response said "we have no documents responsive to this request"
- The system is architecturally capable of generating inbound query logs (other agencies produce them monthly). Policy 433 states "all system access requires a valid reason and is stored indefinitely." The combination of a policy claiming complete logging, a CPRA response claiming no responsive records, and a vendor-side record system that other agencies demonstrably use — is not a gap in the evidence. It is the argument
- **BOS framing:** "Either YCSO's inbound audit log doesn't exist — meaning their own policy statement is false — or it exists and wasn't produced. Either answer is a problem."

**Evidentiary value:**
- Entirely independent of YCSO's own Transparency Portal — sourced from other governments' public records
- Third-party origin insulates the findings from the "one person's analysis" dismissal
- The source diversity (20+ agencies across multiple states) is itself a finding, not just a methodology note

**Data sourcing discipline:**
- The HIBF blank-reason rate figures are **not interchangeable with the ~53% Transparency Portal figure** — different datasets, different mechanisms, different time windows. The HIBF data is used for the qualitative findings above (vehicle filters, training searches, N24-116); the Transparency Portal data is the quantitative source for the blank-reason rate argument. Do not conflate
- After-hours activity in HIBF (13.6% of unique events) is lower than the ~44–45% Transparency Portal figure — the difference reflects the HIBF dataset being a structural sample of YCSO activity, not a complete record; it does not contradict the Transparency Portal finding

**Documents:**
- **`HIBF_Records_CAO_12_May_26.xlsx`** / **`agency-3677-2026-05-12.json`** — HIBF download, May 12, 2026; 4,931 rows; 1,431 unique events after deduplication
- **HaveIBeenFlocked.com** source page for agency 3677 — cite as third-party public records aggregator

---

### 1F. Flock's December 2025 Platform Changes Placed YCSO in Automatic Non-Compliance

**The claim:** When Flock changed its portal format in December 2025 — eliminating officer-level identifiers and replacing free-text reason fields with a drop-down — YCSO became non-compliant with SB 34 as a matter of platform architecture, not individual officer conduct.

**Key findings:**
- EFF's Dave Maass has publicly stated that Flock's December 2025 portal changes placed California agencies in automatic SB 34 non-compliance
- The changes eliminated: (a) officer names from network audit logs; (b) free-text reason fields (replaced by drop-down); (c) individual plate numbers from logs
- Tom's dataset begins February 2, 2026 — entirely post-change — meaning the ~53% blank rate is the **post-change baseline**, not a pre-change comparison
- YCSO cannot deflect SB 34 obligations to Flock: **MSA Section 3.2** states YCSO "represents, covenants, and warrants that Customer shall use Flock Services only in compliance with this Agreement and all applicable laws and regulations, including but not limited to any laws relating to the recording or sharing of data." This is an affirmative warranty — the compliance burden is YCSO's, not Flock's
- Flock's December 2025 T&C changes are on the record; the Cal DOJ v. El Cajon case is relevant precedent context

**Documents:**
- **`Agenda_Item_2632025_BOS__Flock.pdf`** — current MSA, Section 3.2 (compliance warranty language)
- **EFF / Dave Maass public statements** (external; cite by reference at BOS)
- **`Master Audit.xlsx`** — post-change data beginning 2/2/2026

**Specific claims supported:**
- YCSO knew or should have known that the platform changes compromised its § 2413 documentation capability; no corrective action is documented
- YCSO cannot blame Flock for platform-level non-compliance — the MSA places the legal obligation squarely on YCSO
- The BOS approved the February 2025 MSA renewal after these changes were already known in the industry; either YCSO did not disclose the compliance risk, or the BOS approved renewal without evaluating it

**Gaps / what this doesn't prove:**
- Does not establish that YCSO was aware of the EFF analysis specifically — though awareness is inferable from industry publications
- The pre-December 2025 baseline data (what the reason field looked like under the old format) is not in Tom's dataset; comparison would strengthen the argument but is not required

---

### 1G. Transparency Portal Field Suppression — Vendor-Controlled Definition of Transparency

**The claim:** YCSO's public Transparency Portal is configured — by Flock, not by YCSO — to export only one of two reason-field components, structurally suppressing the drop-down category selection that officers make for every search. This means the portal's own data cannot serve as a complete compliance record, and YCSO does not control what "transparency" means for its own system.

**How the finding was established:**
Cross-referencing 52 February 2026 search events that appear in both YCSO's Transparency Portal CSV export (`Master Audit.xlsx`) and the HIBF third-party audit dataset (sourced from Buena Park PD's February 2026 network audit export) by timestamp reveals a consistent structural discrepancy in the reason field:

| Source | What the reason field shows |
|---|---|
| YCSO Transparency Portal CSV | Free-text sub-field only (e.g., `"Drug Investigation"`, `"suspect ID"`, `""`) |
| Buena Park PD audit export (via HIBF) | Drop-down category + free-text concatenated (e.g., `"Drugs/Narcotics - Drug Investigation"`, `"Wanted Person (Arrest Warrant/Fugitive) - suspect ID"`) |

**Key findings:**

*The two-field structure:*
- Every Flock search reason consists of two inputs: (1) a mandatory or optional **drop-down category** (Drugs/Narcotics, Wanted Person, Sex Offenses, Robbery, Destruction/Damage/Vandalism, Animal Offenses, etc.) and (2) an optional **free-text sub-field**
- YCSO's portal exports only the free-text sub-field — the drop-down category is silently discarded in the public export
- This is not a YCSO decision — it is Flock's configuration of what the portal CSV export contains

*The 9 gap-filler events:*
Of 52 matched events, 9 show a blank free-text field in the portal CSV but a populated category in the Buena Park audit:
- `Sex Offenses -` (portal: blank)
- `Animal Offenses (cruelty/neglect) -` (portal: blank)
- `Destruction/Damage/Vandalism of Property -` (portal: blank)
- `Drugs/Narcotics -` × 4 (portal: blank on each)
- `Wanted Person (Arrest Warrant/Fugitive) -` (portal: blank)

These are not searches where officers entered no justification. They are searches where officers selected a category from the drop-down — an act of documentation — that the portal simply does not surface in its public export.

*The reason "mismatch" pattern across all 52 events:*
41 of 52 matched events show a "mismatch" between portal and HIBF reason fields — but examination reveals these are not contradictions. They are the same content, with the portal showing only the sub-field and HIBF showing both fields:
- Portal: `"Drug Investigation"` → HIBF: `"Drugs/Narcotics - Drug Investigation"`
- Portal: `"suspect ID"` → HIBF: `"Wanted Person (Arrest Warrant/Fugitive) - suspect ID"`
- Portal: `"wanted subject"` → HIBF: `"Robbery - wanted subject"`
- Portal: `"288PC"` → HIBF: `"Sex Offenses - 288PC"`

The category prefix is present in every HIBF record and absent in every portal record. This is systematic and architectural, not random.

*The R7-25-0027 confirmation:*
Event [20] — portal reason `"R7-25-0027"` — Buena Park's audit shows `"Drugs/Narcotics - R7-25-0027"`. The officer selected "Drugs/Narcotics" as the category and entered a case number as the free-text sub-field. This is the N24-116 pattern (§1E) replicated in the February 2026 dataset, now with the category prefix confirmed: the officer is using the free-text field for a case designator, not a purpose description, even though a proper purpose category was available in the drop-down and was in fact selected.

**What this means structurally:**

YCSO cannot verify its own compliance using its own portal. The portal export is definitionally incomplete — it excludes a field that Flock captures, that other agencies' audit systems export, and that materially changes the picture of what officers documented. YCSO is dependent on Flock to define what its "transparency" output contains. And Flock defined it in a way that makes the compliance picture look worse than it may be in the underlying system — while simultaneously making it impossible for YCSO, the BOS, or the public to audit the difference without third-party records.

This is the vendor-controlled black box argument in its most concrete form:
- The compliance mechanism (the audit log) is hosted by the vendor
- The transparency mechanism (the portal export) is configured by the vendor
- The fields exposed in the public export are determined by the vendor
- YCSO has no independent means of verifying what the system is actually recording versus what the portal is reporting
- The only way to see the full record is through third-party audit exports obtained via public records requests filed against other agencies

**Specific claims supported:**
- YCSO's Transparency Portal cannot satisfy § 1798.90.52's documentation requirement because it structurally omits a field that is part of the reason-entry system
- The portal's self-proclaimed transparency statement ("all system access requires a valid reason and is stored indefinitely") is undermined by its own export configuration — the portal does not show all of what is stored
- The BOS has no independent means of evaluating YCSO's compliance using only the records YCSO makes available — the portal YCSO controls is configured by the vendor who profits from the contract
- **The ungovernable argument in sharpest form:** YCSO did not buy a surveillance tool with a compliance mechanism. It bought a vendor dependency in which the vendor defines compliance, configures transparency, hosts the audit record, and controls what the public export contains — while YCSO bears the full legal compliance obligation under MSA Section 3.2

**BOS framing:** "YCSO told this Board that all searches are documented and stored indefinitely. Their own portal shows half of searches have no documented reason. But when we compared their portal export to audit records produced by other agencies for the same searches, we found that the portal is configured — by Flock — to suppress the category field that officers actually filled in. YCSO cannot tell you what their own system is recording. They are dependent on their vendor to define what transparency means. That is not a compliance program. That is a vendor contract."

**Documents:**
- **`Master_Audit.xlsx`** — YCSO Transparency Portal CSV export; free-text reason field only; February 2026 data
- **`HIBF_Records_CAO_12_May_26.xlsx`** / **`agency-3677-2026-05-12.json`** — HIBF Buena Park-sourced records; two-field concatenated reason; 52 timestamp-matched events
- **Cross-reference analysis** (May 13, 2026) — 52 matched events; 41 structural mismatches; 9 gap-filler events; timestamp join methodology documented

**Data integrity note:**
The cross-reference is joinable on `search_time_utc` (timestamp), not on the `id` field. The YCSO portal assigns Flock-native UUID4 identifiers (e.g., `761a53ad-9a16-4582-a1bb-353ea60fc6ac`). HIBF assigns its own 32-character hex row keys at ingest. The same search event receives different IDs in each system — confirming they are independent ID systems. The timestamp is the authoritative cross-reference key.

---

<a name="pillar-2"></a>
## Pillar 2 — Measure K Governance Conflict

**Core legal standard:** Government Code § 1090 prohibits a public officer from participating in making a contract in which they have a financial interest. Yuba County Ordinance No. 1575 / Chapter 5.60 (Conflict of Interest Code) establishes the county's own adopted standards. The Measure K Citizens Oversight Committee was created specifically to provide independent review of Measure K fund expenditures — independence is the structural purpose of the committee's existence.

---

### 2A. Structural Conflict: Undersheriff Chairs Committee Reviewing His Own Department

**The claim:** Undersheriff Morawczewski chairs the Measure K Citizens Oversight Committee that reviews expenditures flowing directly to the Yuba County Sheriff's Office — the department he oversees. This is a structural conflict of interest regardless of intent.

**Key findings:**
- Measure K is a voter-approved public safety sales tax; Flock camera deployment in Plumas Lake is funded through Measure K
- The Citizens Oversight Committee exists to provide independent civilian review of how Measure K funds are spent
- Undersheriff Morawczewski's position as chair means the chief oversight reviewer of Sheriff's Office spending is himself a senior Sheriff's Office official
- The conflict argument is **structural, not personal**: intent is irrelevant when the structure itself violates the county's adopted conflict of interest standards
- The "advisory only" defense does not resolve the concern: an advisory committee that is chaired by a beneficiary of the funds under review cannot be meaningfully independent, regardless of whether its recommendations are binding

**Documents:**
- **Measure K enabling documents / BOS resolutions** (on file via county records)
- **`Yuba_County_Flock_Oversight_Project.docx`** — conflict argument framing and checklist status
- **Yuba County Ordinance No. 1575 / Chapter 5.60** — the county's own Conflict of Interest Code

**Specific claims supported:**
- The oversight architecture for Measure K funds is structurally compromised
- The BOS has a fiduciary obligation to ensure that independent oversight of voter-approved tax spending is genuinely independent
- This is a governance problem the BOS can fix through structural reform — it does not require finding wrongdoing
- BOS framing: "Voters approved this tax expecting independent oversight. The current structure does not provide that."

**Gaps / what this doesn't prove:**
- Does not establish that any specific expenditure decision was improper or corrupted
- Does not prove intent or bad faith — and the argument should not be framed that way
- The "advisory only" limitation on the committee may limit § 1090's direct applicability; the stronger ground may be Chapter 5.60 and general conflict of interest principles rather than a strict § 1090 claim

---

### 2B. Applicable Legal Standards

**Gov. Code § 1090:** Public officers may not participate in making a contract in which they have a financial interest. While the committee is advisory, participation in shaping recommendations that affect one's own department's funding is within the spirit if not the letter of § 1090.

**Yuba County Chapter 5.60 / Ordinance No. 1575:** The county's own adopted Conflict of Interest Code — this is the most direct applicable standard because it is YCSO's own governing document. The argument is that the county is violating its own adopted rules, which is harder to dismiss as external criticism.

**Political Reform Act (Gov. Code § 87100 et seq.):** Prohibits public officials from making, participating in making, or influencing governmental decisions in which they have a financial interest. The breadth of "influencing" is broader than § 1090's "making" — this may be the stronger statutory hook.

**BOS framing guidance:**
- Lead with the county's own ordinance, not the state statute — "your own rules say this"
- Frame as a liability exposure: if a Measure K expenditure decision is later challenged, the chair's conflict is a vulnerability that exposes the county to legal risk
- The fix is structural and easy: restructure the committee to exclude YCSO personnel from chairing or voting

---

<a name="track-b"></a>
## Supporting Argument — Permitting Gaps (Track B)

**Strategic note:** The permitting argument is a **secondary supporting item** for BOS public comment, not a separate primary track. It reinforces the pattern of incomplete process documentation. The core SB 34 and Measure K arguments remain primary. Track B was listed as an investigative thread in CPRA letters to Public Works, which may function as a useful distraction to YCSO while the core arguments are developed separately.

---

### 3A. Encroachment Permit Inventory vs. Known Camera Deployment

**What the produced permits show:**
| Permit | Location | Cameras | Agency | Notes |
|---|---|---|---|---|
| PW22-0166 | 1675 N. Beale Rd | 25 | YCSO | Original 2022 batch |
| ENCR-22-0036 | 5962 Avondale Ave | 6 | YCSO (Flock applicant) | September 2022 |
| ENCR-23-0295 | Road 169 | — | Yuba County Water Agency | Unrelated to YCSO Flock deployment; set aside |
| ENCR-24-0314 | 7638 Jack Slough Rd | 1 | **Marysville PD** | Issued 11/12/2024; cross-agency |
| ENCR-26-0043 | 987 Country Club Rd | 1 | YCSO | Issued 2/11/2026; Final Approval line **blank** |

**Documents:**
- **`1675_North_Beale_RdPW220166Executed.pdf`** — 25-camera 2022 batch permit
- **`5962_Avondale_Ave_ENCR220036_Executed_v1.pdf`** — 6-camera Avondale permit
- **`Road_169_ENCR230295_Executed.pdf`** — Water Agency permit (set aside)
- **`7638_Jack_Sough_Road_ENCR240314_Executed.pdf`** — Marysville PD camera in Yuba County ROW
- **`987_Country_Club_Road_ENCR260043_Executed.pdf`** — Most recent YCSO permit; unsigned final approval

---

### 3B. Starbend Boat Ramp: MOU Without a Permit

**The claim:** YCSO executed a formal MOU with Public Works specifically for a Starbend Boat Ramp Flock camera, but no encroachment permit for that location was produced in response to the CPRA.

**Key findings:**
- **`4152025_Public_Works_MOU.pdf`** — MOU between YCSO and Yuba County Public Works; explicitly covers "One (1) FLOCK Safety Solar Multi-Purpose LPR and Video" at the Starbend Boat Ramp Area; establishes reimbursement structure (Public Works pays YCSO)
- No encroachment permit for Starbend Boat Ramp appears in any produced document
- Flock's OMNIA SOP commits to pre-installation permitting coordination — the OMNIA contract's certified-no-proprietary-information finding means the SOP cannot be withheld as a trade secret
- The discrepancy: YCSO executed an MOU (a formal legal instrument) specifically naming this location, but no corresponding Right-of-Way authorization exists in the public record

**Documents:**
- **`4152025_Public_Works_MOU.pdf`** — primary; establishes the MOU and Starbend location
- **`PRAR_Response_Flock_OMNIA_Contract.pdf`** — OMNIA SOP permitting coordination commitment; no-proprietary-information certification

**Specific claims supported:**
- The MOU's existence proves YCSO knew formal authorization was required at this location; the absence of a permit shows that authorization was not obtained through the standard Public Works channel
- Bridges to the OMNIA SOP finding: if Flock's own standard operating procedure requires pre-installation permitting coordination, and no permit exists, either Flock or YCSO failed to follow that SOP

**Gaps / what this doesn't prove:**
- Does not establish whether the camera was installed without authorization or whether authorization was obtained through a different mechanism not produced in the CPRA response
- A no-records response to the CPRA would itself be a significant finding — absence of a permit in the production is strong but not conclusive until the agency certifies no responsive records exist

---

### 3C. Cross-Agency Hardware in Yuba County ROW

**The claim:** ENCR-24-0314 (Jack Slough Rd, 11/12/2024) is a Flock camera installation **on behalf of Marysville PD** in Yuba County right-of-way, with no disclosed interagency data-sharing agreement produced from CPRA 26-136.

**Key findings:**
- The permit identifies Marysville PD as the agency, with Flock as installer — this is Marysville PD hardware in Yuba County ROW
- CPRA 26-136 requested all interagency data sharing agreements; none covering the Marysville PD camera were produced
- The Flock Network Sharing document confirms Marysville CA PD is a separate Flock network participant
- This bridges directly into the § 2413(b) outside-agency disclosure gap: if Marysville PD's camera is accessible through YCSO's network (or vice versa), the authorization and disclosure framework is unclear

**Documents:**
- **`7638_Jack_Sough_Road_ENCR240314_Executed.pdf`** — permit issued on behalf of Marysville PD
- **`Flock_NetworkSharing.pdf`** — confirms Marysville CA PD as a separate Flock network participant
- **CPRA 26-136 (outstanding)** — interagency sharing agreements not yet produced

---

<a name="effectiveness"></a>
## Supporting Evidence — Effectiveness Claim Rebuttal

**Strategic note:** This section does not aim to prove Flock is ineffective — that cannot be established without Phase 2 CPRA data (hit-to-arrest rates). The goal is to rebut the unsupported effectiveness claims the YCSO and Supervisor Bradford have made to the BOS, and to show that the BOS has been making multi-year funding decisions without independent effectiveness data.

---

### 4A. Crime Clearance Rate Analysis

**The claim:** YCSO's own cited crime clearance rate data does not support a conclusion that Flock deployment improved case-solving outcomes.

**Key findings:**
- 10-crime-type clearance rate analysis compiled from CA DOJ OpenJustice data, 2015–2024 (pre-Flock vs. post-Flock periods)
- Clearance rates in the post-Flock deployment period **declined or remained flat** for most analyzed crime types
- **Critical framing caveat:** clearance rates are lagging metrics that cannot isolate Flock's contribution from confounders including Ring cameras, Nextdoor networks, Measure K staffing increases, and broader crime trend shifts — this limitation must be acknowledged at BOS to avoid overreach
- The argument is not "Flock caused worse outcomes" but rather "the data does not support the effectiveness claims being made"
- Supervisor Bradford publicly acknowledged on Reddit he had no independent data and was relying on YCSO's characterization — this is on the record

**Documents:**
- **`Yuba_Clearance_Rate_PQ.xlsx`** — compiled clearance rate analysis; Power Query workbook; CA DOJ OpenJustice source data

**Specific claims supported:**
- The BOS has been approving Flock expenditures without independent effectiveness verification
- YCSO's own characterizations of Flock's impact are unverified and unverifiable without Phase 2 CPRA data (hit-to-arrest rates)
- The most critical effectiveness metric — hit-to-actionable-outcome rate — has not been disclosed

**Gaps / what this doesn't prove:**
- Cannot prove Flock is ineffective; clearance rates measure case-solving, not crime prevention, and cannot isolate Flock's contribution
- The hit-to-arrest rate (or hit-to-actionable-outcome rate) is the correct metric; this requires Phase 2 CPRA production

---

### 4B. Facebook Notification Analysis

**The claim:** YCSO's own Facebook data (25 months, July 2023–November 2025) shows 14,671 Flock notification posts but establishes no causal link to arrests.

**Key findings:**
- 14,671 total notifications posted by YCSO to Facebook over the analysis period
- YCSO's own footnote definition of "notification" is used against them — the term encompasses alerts, not confirmed outcomes
- No post in the dataset connects a Flock notification to an arrest, conviction, or case closure
- This is Phase 1 analysis; Phase 3 CPRA (notification-to-outcome data) is needed to close the loop

**Documents:**
- YCSO Facebook post dataset (compiled from public posts, 2023–2025)

**Specific claims supported:**
- Volume of notifications alone does not establish effectiveness
- YCSO is publicly representing Flock's activity in ways that imply effectiveness without providing outcome data
- The BOS is being asked to continue funding based on activity metrics rather than outcome metrics

**Gaps / what this doesn't prove:**
- Does not prove that none of the 14,671 notifications led to outcomes — only that no connection was disclosed
- Phase 3 CPRA needed to request notification-to-enforcement outcome data

---

### 4C. Peer Policy Comparison

**The claim:** YCSO's ALPR policy (Policy 433) is structurally weaker than peer agencies on the same template framework, with no statutory basis for the differences.

**Key findings:**
| Policy Element | Marysville PD (Policy 426) | Wheatland PD (Policy 426) | YCSO (Policy 433) |
|---|---|---|---|
| Data retention | 1-year minimum (Gov. Code § 34090.6) | 1-year minimum (Gov. Code § 34090.6) | 60 days (no statutory citation) |
| Statutory anchor | Civil Code § 1798.90.52 explicit | Civil Code § 1798.90.52 explicit | Not explicitly cited |
| Interagency sharing | Written request + Commander approval + retained on file | Authorized verified LE officials | Not comparably documented |
| Website posting | Required (§ 1798.90.51) | Required | Compliance status unclear |

**Documents:**
- **`Marysville_PD_ALPR_Policy_24_May_2023.pdf`** — Lexipol Policy 426, § 426.4 (one-year minimum, Gov. Code § 34090.6 citation)
- **`Wheatland_PD_ALPR_Policy_7_Jun_23.pdf`** — Lexipol Policy 426, § 426.4 (one-year minimum, Gov. Code § 34090.6 citation)

**Specific claims supported:**
- YCSO's 60-day retention is below the regional peer standard with no statutory justification
- The comparison uses the same Lexipol policy framework that YCSO presumably uses (Policy 433 vs. Policy 426), making the differences impossible to attribute to template variation
- BOS framing: "Your neighboring agencies — Marysville PD, Wheatland PD — both keep this data for one year because state law says to. Why does YCSO keep it for 60 days?"

**Strategic note:** Regional peer CPRA requests (Marysville PD and Wheatland PD for audit logs, interagency sharing records, training documentation) are **on hold until after BOS presentation** to avoid alerting YCSO to the comparison framing prematurely. This is a Phase 4 action.

---

### 4D. "Game Changer" — Vendor Language Laundered as Independent Assessment

**The claim:** The Sheriff's characterization of Flock as a "game changer" — cited by Supervisor Bradford as justification for continued funding — is traceable to Flock's own marketing ecosystem, not an independent evidence-based assessment. The phrase's documented trajectory from vendor pitch deck to law enforcement presentation to governing body is itself a governance failure.

**Key findings:**
- Flock Safety's own marketing content uses the phrase "game changer" to describe community adoption of its product
- The phrase has been repeated verbatim by police chiefs across the country in public statements justifying Flock to their governing bodies: Dallas PD, Allentown PA PD, Shorewood IL PD, and others — identical language in each case
- The pattern is consistent with a vendor sales cycle in which marketing language is absorbed into law enforcement presentations and repeated to governing bodies as independent assessment
- When the YCSO Sheriff told the Yuba County Board of Supervisors that Flock cameras are a "game changer," the Board made a multi-year, multi-hundred-thousand-dollar funding commitment based on a vendor talking point — with no independent verification, no outcome metrics, no audit, and no oversight mechanism capable of testing whether the claim is even true
- Supervisor Bradford has acknowledged on the public record (Reddit) that he had no independent data and was relying on YCSO's characterization

*Shorewood, Illinois — the "game changer" department:*
- Shorewood IL PD Chief Phillip Arnold called Flock "a game changer for safety" in a March 2026 ABC7 Chicago interview — the same language the YCSO Sheriff used with the Yuba County Board
- Shorewood subsequently **shut down its Flock cameras** pending a review, following community pressure and findings about federal immigration enforcement access to the system
- Brooklyn Park, MN similarly withdrew from the Flock network entirely in the same period
- Illinois's Secretary of State found that Flock broke state law by allowing federal Customs and Border Patrol officers to access Illinois license plate data without authorization; the system was also used by out-of-state police to locate a woman who had recently had an abortion
- Shorewood had operated its Flock system for nearly two years without completing the mandatory biennial audit required by Minnesota law — and the contract renewal was expected to come up before those audit results were even available

The structural parallel to Yuba County is direct: cameras deployed, compliance mechanisms absent or incomplete, renewal decisions made before any independent verification of how the system is actually being used. The "game changer" police chief's department is now shut down pending review.

**The Option C argument — this system resists meaningful governance:**
This section connects to the overarching framing for the BOS presentation. The Shorewood parallel is not a gotcha — it is corroboration of a documented national pattern. The argument is not that YCSO is uniquely negligent. The argument is that YCSO, like Shorewood, like Mankato (which rejected Flock after community opposition), has deployed a surveillance system that functionally resists the governance mechanisms that are supposed to constrain it:
- The audit log is the compliance mechanism — but the audit log is incomplete, and YCSO's own CPRA response confirms it cannot produce audit records that other agencies publish monthly
- The policy framework is the compliance mechanism — but Policy 433's § 433.8 annual audit has never been disclosed
- The oversight committee is the compliance mechanism — but it is chaired by the department it is supposed to oversee
- The vendor contract places compliance responsibility on YCSO — but YCSO's CPRA responses demonstrate it cannot or will not produce the records that would demonstrate compliance

If YCSO responds to the BOS presentation by promising to fix the gaps, the follow-up question is already built into the record: what is the enforcement mechanism? Who verifies it? The Measure K oversight committee — chaired by the Undersheriff whose department receives the funds? The audit log infrastructure that doesn't currently exist? "We'll do better" is not a governance structure. Two years of non-compliance with a mandatory state audit, followed by a camera shutdown, is the documented trajectory when compliance is left to self-reporting.

**BOS framing:** "The Sheriff told this Board the system was a game changer. A police chief in Illinois used those exact same words. That department just shut the cameras down pending a review after the state found the vendor broke the law. The Board deserves more than a marketing claim. It deserves an independent audit — one not conducted by the Sheriff's Office."

**Documents:**
- **ABC7 Chicago, March 24, 2026** — Shorewood Chief Arnold "game changer for safety" quote; Shorewood shutdown reported
- **Capitol News Illinois / NPR Illinois, August 27, 2025** — Illinois Secretary of State finding Flock broke state law; federal CBP access confirmed
- **Star Tribune / Mankato Free Press, April 2026** — Brooklyn Park Flock withdrawal; Shorewood shutdown confirmed
- **Shorewood Citizen Advocates, November 2025** — nearly two years without mandatory biennial audit; renewal before audit results
- **Flock Safety marketing content** (flocksafety.com) — "game changer" language in vendor materials
- **Supervisor Bradford Reddit post** (on file) — acknowledged relying on YCSO characterization; no independent data

---
## Contractual Anchor Documents

### 5A. 2022 Master Services Agreement (Original)
**Source:** `Agenda_Item_2142022_BOS__Flock.pdf` (Feb 14, 2022 BOS agenda)
- DocuSign Envelope ID: 71A8C4CE-9675-40E5-ABC1-50E8A6129D79
- 25 Flock Falcon cameras; Year 1 total $79,750; recurring $73,500
- **Extended data retention purchased:** $300 × 25 cameras = $7,500 annually — establishes one-year contractual entitlement
- Signed by YCSO Sheriff; countersigned by Flock Chief Revenue Officer

**Evidentiary role:** Establishes the original contractual framework; the extended retention line item directly contradicts Policy 433's 60-day period; confirms YCSO's affirmative acceptance of compliance obligations.

---

### 5B. 2025 MSA Renewal
**Source:** `Agenda_Item_2632025_BOS__Flock.pdf` (Feb 26, 2025 BOS agenda)
- Signed by Gary Bradford (Chair, BOS); countersigned by Flock; approved by Tiffany Manuel (Risk Manager) and County Counsel (Janet Bender)
- Converts to Condor PTZ camera; Year 1: $4,841; recurring: $4,700; contract total: $9,541
- Virginia Sheriff's Association First Responders Supplies contract (#25-01-0524) cited as procurement vehicle
- **MSA Section 3.2** (p.13 of document): "Customer represents, covenants, and warrants that Customer shall use Flock Services only in compliance with this Agreement and all applicable laws and regulations, including but not limited to any laws relating to the recording or sharing of data, video, photo, or audio content."
- **MSA Section 1.15**: "Flock deletes all Footage on a rolling thirty (30) day basis, except as otherwise stated on the Order Form" — establishes Flock default; Order Form governs actual retention
- **MSA Section 4.4** (Data Distribution): Customer must authorize third-party data distribution; Flock cannot share without customer request — YCSO owns the authorization decision for network sharing

**Evidentiary role:** This is the operative contract. Section 3.2 is the affirmative compliance warranty that prevents YCSO from deflecting SB 34 obligations to Flock. The BOS Chair's signature means the BOS itself is bound by these terms. Approved post-December 2025 platform changes, meaning the BOS renewed knowing (or should have known) that the platform had changed.

---

### 5E. YCSO ALPR Policy 433 (October 20, 2022; reissued December 18, 2025)
**Sources:** `ALPR_policy_102022.pdf` (Phase 1 CPRA production); `YCSO_2026_Policy_Release.pdf` (2025 reissue)
- Original policy date: October 20, 2022; reissued December 18, 2025 with structural changes
- **§ 433.5 — Retention (two-tier):** Flock vendor purge at 60 days; YCSO may retain on its own servers for up to one year — language confirmed identical across both the 2022 and 2025 versions; the retention conflict is a sustained structural inconsistency, not a drafting artifact
- **§ 433.6(e) — Documentation requirement:** Each search must have a documented reason — independently mirrors SB 34's Civil Code § 1798.90.52 obligation; YCSO's ~53% blank rate violates its own policy, not just state law. Section numbering confirmed intact in the 2025 reissue
- **§ 433.8 — Annual audit requirement:** Requires a memorandum to the Sheriff documenting at least 10 sampled searches reviewed annually for policy compliance — confirmed in both 2022 and 2025 versions. Note: the 2025 reissue's § 433.8 references "policy section 433.5(e)" internally, but § 433.5 has no subsection (e) in the 2025 version — the documentation requirement is at § 433.6(e). This is a drafting inconsistency in YCSO's own updated policy
- **§ 433.3.1 — Administrator (2025 reissue change):** The 2025 reissue explicitly names the **Operations Division Captain** as the responsible party for Civil Code § 1798.90.5 et seq. compliance — stronger language than the 2022 version; assigns a named role to the obligation YCSO has claimed cannot be documented. This was used directly in the Phase 2 CPRA request to rebut the prior § 7922.000 public interest exemption claim
- **§ 433.10 — Training (new in 2025 reissue):** Added a dedicated training section; corresponds to Category 1 of the Phase 2 CPRA request (training curriculum, completion records, authorization process)

**Evidentiary role:** Policy 433 is a gift — it independently creates obligations YCSO is visibly failing to meet, without requiring any reliance on external law. The blank reason rate violates § 433.6(e). The annual audit has never been disclosed (§ 433.8). And the retention framework in § 433.5 conflicts with three other documents. The 2025 reissue strengthens the argument by explicitly naming the Operations Division Captain as responsible for SB 34 compliance. BOS framing: "YCSO isn't just violating state law — they're violating their own written policy, including the version they issued four months ago."

---

### 5C. OMNIA Contract (RS250203)
**Source:** `PRAR_Response_Flock_OMNIA_Contract.pdf`
- Flock's response to OMNIA Partners public procurement solicitation
- **Key finding 1:** Flock certified no proprietary information — forecloses any trade secret CPRA exemption claims on contract documents
- **Key finding 2:** Flock's own SOP commits to pre-installation permitting coordination — strengthens Track B (Starbend no-permit argument)
- **Key finding 3:** FlockOS features table (visible in document) explicitly lists Statewide Network and Nationwide Network as active features — confirms YCSO's purchased network scope is beyond local-only
- **Key finding 4:** Accountability flows toward the customer (YCSO), not Flock — MSA Section 3.2 warranty confirmed

**Evidentiary role:** The OMNIA contract was independently obtained from the BOS's own public agenda portal after YCSO withheld it in CPRA response — the contrast between YCSO's withholding and the document's availability on the BOS's own portal is a documentable contradiction presentable to the BOS.

---

### 5D. JAG Grant Award (FY24)
**Source:** `7432024_Grant_Award_Package.pdf`, `7432024_BAR.pdf`, `7432024_Certifications_and_Assurances.pdf`
- Award: FY 2024 Edward Byrne Memorial Justice Assistance Grant (JAG) Program
- Award Number: 15PBJA-24-GG-04727-JAGX; Federal Award Date: 12/4/24; Amount: $14,458
- Recipient: County of Yuba (720 Yuba St, Marysville, CA 95901)
- Project: "Yuba County Flock" — explicitly identified in grant documentation
- **JAG Conditions 40, 45, 46, 48** — civil rights, data privacy, and nondiscrimination conditions attached to the grant
- Budget Adjustment Request (`7432024_BAR.pdf`): $14,485 revenue/expenditure adjustment processed through Sheriff-Coroner; Fund 108, Dept 2700

**Evidentiary role:** Federal funding creates federal oversight obligations. JAG Conditions 40, 45, 46, 48 impose civil rights and data privacy compliance requirements on top of state law. If YCSO's SB 34 documentation failures constitute civil rights violations, the federal grant creates a separate accountability vector. Phase 2 CPRA should request JAG compliance documentation. The grant also shows this is not purely a local discretionary expenditure — federal funds are involved.

**CPRA status:** JAG compliance records (Conditions 40, 45, 46, 48) included in Phase 2 CPRA filed May 9, 2026 (Category 5 — SB 34 Compliance Documentation, and Category 4 — Interagency Data Sharing). Determination deadline: ~May 19, 2026.

---

<a name="cpra"></a>
## CPRA Status — Outstanding Records

### Track A — YCSO (Requests 26-97 and 26-136)
**Contact:** Janet Bender (YCSO/County Counsel); CC'd Catherine, Erika, Kelly
**Status: RESOLVED — Substantive determination letter received May 6, 2026**

**Bender's May 6, 2026 determination letter — responses by category:**

- **Request 1 (Authorization/Access Structure):**
  - *Part One (authorized user list):* Withheld under Gov. Code § 7922.000 public interest exemption, citing *Times Mirror Co. v. Superior Court* (1991) 53 Cal.3d 1325, 1337-1339 — security vulnerability rationale. Formally cited; contestable but not frivolous
  - *Part Two (non-YCSO access records):* "We have no documents responsive to this request." — Either no outside agency was ever formally granted access, or the process was never documented. Either outcome is significant

- **Request 2 (Audit Reports/Compliance Summaries):** Referred to the Flock Safety Transparency Portal; "no other documents responsive." Also used the Vehicle Code § 2413 citation error from the prior letters against the request (correctly noting § 2413 is CHP-specific), without volunteering the correct citation (Civil Code § 1798.90.52). The portal referral is itself the compliance gap argument: **Bender's response confirms in writing that the portal is YCSO's audit record** — a record that cannot satisfy § 1798.90.52's individual user attribution requirement

**Escape hatch finding — CAD/off-platform log question:**

Phase 2 Category 2 was drafted with a deliberate structural feature: it does not merely request audit logs — it explicitly asks for any officer-level documentation maintained *independently* of Flock's platform (CAD, dispatch, locally stored logs), *or a written confirmation that no such records exist*. This was intentional. If YCSO has CAD-level records, they must produce them. If they don't, a one-sentence written statement closes the question cleanly — the lowest possible burden on a well-governed agency with nothing to conceal.

The significance is not what YCSO produces. It's whether they can answer the question at all.

A well-governed agency with complete records takes the off-ramp immediately: a single written statement either confirms the records exist or confirms they don't. The failure mode — inability or unwillingness to commit to either answer in writing — is itself the governance finding. It suggests either that no one inside YCSO knows what documentation exists outside the Flock portal, or that they know and cannot put it on the record.

That fits directly into the "ungovernable" frame: not corrupt, not conspiratorial — a system that cannot account for itself even when accounting is made maximally easy.

**BOS framing:** "We didn't ask for much. We asked whether officer-level logs exist outside of Flock's platform. We gave them an explicit out — just say no in writing if they don't. The Board should ask why that question went unanswered."

**Evidentiary value:** This finding is independent of the blank reason rate and the after-hours timing analysis. It does not compound either — it stands on its own as a CPRA process observation. Do not conflate with §1A or §1B.

- **Request 3 (Interagency Data Sharing Agreements):** "We have no documents responsive to this request." Combined with the Marysville PD camera in Yuba County ROW (ENCR-24-0314), this is a documented contradiction: cross-agency hardware installed in YCSO's jurisdiction with no corresponding agreement on the record

**Evidentiary value of the May 6 response:**
- The portal-as-audit-record claim is now YCSO's stated position in writing — directly usable at BOS
- The "no documents" response to Request 3 requires YCSO to affirmatively represent that § 433.9's written request process was never triggered — contradicted by the Marysville PD encroachment permit
- The § 2413 deflection is preserved as evidence of either legal imprecision or deliberate misdirection; Bender did not volunteer the correct Civil Code citations
- The blank-date extension notice from the prior track is preserved as a separate compliance failure

**Coalition resource produced:** A fully annotated constructive denial letter template covering all seven sections (header, opening, timeline, legal standard, demand and final window, AG petition notice, closing) plus statutory quick-reference appendix was produced and shared with DeFlock NorCal (April 30, 2026). Key statutes embedded: Gov. Code §§ 7922.525, 7922.530, 7922.535, 7923.000, 7923.100, 7923.115.

---

### Track B — Public Works (Encroachment Permits)
**Contact:** Samuel Bunton (Public Works Director)
**Status as of May 6, 2026:** Records received May 5, 2026; analysis complete
**Key outcome:** Permit inventory complete; Starbend gap confirmed; ENCR-26-0043 unsigned; Marysville PD cross-agency camera documented

**Resolved:** Track B constructive denial position was established under § 7923.100; records were subsequently produced, resolving the immediate CPRA dispute. The findings from the produced records are now incorporated as evidence (see Section 3 above).

---

### Phase 2 CPRA — Request #26-245
**Filed:** May 9, 2026 to Custodian of Records, Yuba County Sheriff's Office, 215 Fifth Street, Marysville, CA 95901
**Reference:** Prior requests 26-97 and 26-136
**Final response received:** May 19, 2026 — marked "Please consider this as a final response"
**Response came within the 10-day window; no extension invoked.**

**Categories as filed:**

1. **Authorization and Access Structure** — personnel classifications authorized to access Flock; written grant/revocation processes; training curriculum and standards (Policy 433.3.1(b) and 433.4(g)); training completion records by classification and date (individual names excluded per prior exemption claim, but aggregate counts required). Rebuttal of prior § 7922.000 exemption built into the request: this request does not seek individual names or credentials; it seeks administrative governance records that the 2025 reissue's § 433.3.1 explicitly assigns to the Operations Division Captain

2. **Audit Log Integrity and Platform Transition Records** — does not re-request the underlying log (Bender already answered that). Targets: change logs, deletion/modification records, edit history; communications with Flock regarding December 2025 platform change's effect on officer-level logging; any internal assessment of whether the portal satisfies § 1798.90.52 and Policy 433.6(e); any officer-level documentation maintained independently of Flock (CAD, dispatch, locally stored logs) — or written confirmation none exists

3. **Annual Audit Documentation — Policy 433.8** — memoranda from Operations Division Captain or designee to Sheriff; any substitute documentation YCSO contends satisfies § 433.8; or written statement confirming no audits were conducted or documented for the period

4. **Interagency Data Sharing — Written Requests and Approvals** — all written requests from outside agencies for YCSO Flock data; all approvals/denials; internal policies governing YCSO personnel's use of State/Nationwide/Law Enforcement/Community Network tiers to query other agencies' data; or written statement confirming no outside agency requested data and YCSO personnel did not access other agencies' data through those tiers (forces YCSO to affirmatively represent that § 433.9 was never triggered — contradicted by the Marysville PD encroachment permit)

5. **SB 34 Compliance Documentation** — internal audits/reviews; communications with Flock re: SB 34 compliance, platform changes, audit log completeness; communications with CA DOJ re: ALPR usage or SB 34 reporting; internal assessments of whether portal satisfies SB 34 documentation requirements

**Key drafting features:**
- Portal-is-not-a-substitute language explicitly preempts the Request 2 deflection used in Phase 1
- Every "no documents" escape route in Categories 2, 3, and 4 requires a written statement confirming absence — forces the record either way
- Exemption claims section preemptively addresses all four exemptions Bender used or could use: portal referral, § 1798.90.55(b), § 7922.000 public interest, § 7923.600 law enforcement
- Blank-date extension language included in response timeline section (preserves constructive denial trigger for Phase 2)
- § 2413 citation corrected throughout: all references use Civil Code §§ 1798.90.51–.52; Veh. Code § 2413 is identified as CHP-specific in the legal basis section

---

### Phase 2 Response — Full Analysis (May 19, 2026)

**Category 1 — Authorization and Access Structure**
- Personnel classifications and written access grant process: Referred to Policy 433.2(b) and 433.3.1(a) — policy citation only, no underlying records produced
- Written access revocation process: No documents responsive
- Training curriculum/standards (§§ 433.3.1(b), 433.4(g)): No documents responsive — confirms that training requirements exist in policy with no underlying curriculum documentation; YCSO wrote § 433.10 into its 2025 reissue with nothing behind it
- Training completion records (aggregate counts by classification): Claimed exempt under **Penal Code § 832.7** (peace officer personnel records) via Gov. Code § 7927.705

  **Issue flagged — § 832.7 overreach:** Penal Code § 832.7 protects individual peace officer personnel records. Aggregate counts by classification (e.g., "12 patrol deputies completed training in Q1 2025") are not individual personnel records and do not reveal individual identities. The exemption claim is a likely overreach and is contestable. A focused follow-up letter to Bender specifically on this point is warranted.

**Category 2 — Audit Log Integrity and Platform Transition Records**
- Deletion/modification/change log records: No documents responsive
- December 2025 platform change communications with Flock: Deflected to **BOS agenda items 415/2025 (August 26, 2025) and 263/2025 (July 22, 2025)**
- Internal assessment of whether portal satisfies § 1798.90.52 and § 433.6(e): No documents responsive
- Independent officer-level documentation (CAD/dispatch/locally stored logs): Claimed **"overly broad"** — demanded a specific instance, report number, location, date, and time

  **Issue flagged — "overly broad" objection is improper:** CPRA does not require a requester to identify specific instances to obtain a category of records. A categorical request for all officer-level documentation maintained independently of Flock's platform is a proper CPRA request. Demanding a report number, date, time, and location as a condition of response is a scope objection that has no statutory basis under CPRA. This is a standard deflection tactic and is contestable. Critically, the request included an explicit escape hatch — "or, if no such records exist, a written statement to that effect" — which Bender ignored entirely. Her refusal to provide even the written statement is itself a documentable gap: she neither produced the records nor represented in writing that none exist.

  **Issue flagged — BOS item deflection is a documented non-answer:** The two agenda items cited as responsive to communications about the December 2025 platform change are:
  - **263/2025 (July 22, 2025):** A contract between Yuba County **Elections** (County Clerk-Recorder) and Flock Safety for **video surveillance of a ballot drop box** at Linda Fire Station #3 in Plumas Lake. Customer: CA - Yuba County Elections. Product: Flock Safety Platform Essentials + one Solar Video Camera PTZ (Condor). Retention Period stated on Order Form: 30 Days. Funded by HAVA (Help America Vote Act) federal funds, Agreement #24G27158. Total: $9,541. This is a different department, a different product (non-ALPR video surveillance), a different funding source, and predates the December 2025 platform change by five months. It contains no communications between YCSO and Flock about ALPR platform changes. Citing it as responsive is documentably incorrect.
  - **415/2025 (August 26, 2025):** The YCSO ALPR renewal Order Form (already in evidence as `Flock_Safety_signed_by_BOS.pdf`). This is a procurement document signed by BOS Chair Gary Bradford; it predates December 2025 by four months and contains no communications about platform changes.

  Neither document is responsive to a request for YCSO-Flock communications about the December 2025 platform change's effect on officer-level logging. The deflection is on the record as a non-answer. "No documents responsive" would have been more accurate — citing specific documents that demonstrably do not address the subject makes this a stronger record than a bare non-response.

**Category 3 — Annual Audit Documentation (Policy 433.8)**
- All four bullets (audit memoranda, Operations Division Captain memos to Sheriff, substitute documentation, written confirmation of non-compliance): All **no documents responsive**
- The written confirmation bullet was specifically drafted to force an affirmative statement; "no documents responsive" does not satisfy a request for a written statement — this is a gap in the response that strengthens the BOS argument: YCSO cannot produce a single § 433.8 audit memo and will not commit in writing to why

**Category 4 — Interagency Data Sharing**
- All four bullets (written requests from outside agencies, approvals/denials, internal policies on network tier access, written statement confirming § 433.9 was never triggered): All **no documents responsive**
- Same structural gap as Category 3: the written statement bullet required an affirmative representation; "no documents responsive" is a non-answer. Combined with the Marysville PD camera in Yuba County ROW (ENCR-24-0314), YCSO's silence on whether § 433.9 was ever triggered is an evidentiary gap, not a clean answer

**Category 5 — SB 34 Compliance Documentation**
- All four bullets (internal compliance reviews, Flock communications, CA DOJ communications, portal assessment): All **no documents responsive**
- The complete absence of any SB 34 compliance documentation — no internal reviews, no DOJ communications, no portal assessment — is itself the finding. YCSO renewed its contract in August 2025 (post-platform change) and produced zero compliance documentation in response to a direct request.

**Overall evidentiary value of the Phase 2 response:**
The Phase 2 response confirms, across five categories, that YCSO has no documented compliance infrastructure for its Flock deployment. There are no training records, no audit logs beyond the portal, no § 433.8 audit memos, no interagency sharing agreements, and no SB 34 compliance reviews. The three improper or non-responsive answers (§ 832.7 on aggregate training counts, "overly broad" on CAD/dispatch, and the 263/2025 deflection) are each independently contestable and each strengthens the BOS record. By invoking inapplicable exemptions and declining to provide even the written statement escape hatches that were specifically drafted to foreclose these objections, YCSO is building the evidentiary record for the BOS presentation. The Phase 2 response is now part of that record.

### Phase 3 CPRA (Queued)
- Notification-to-enforcement outcome data
- Connecting Facebook notification figures to actual case outcomes (arrest, prosecution, conviction)

### Phase 4 — Regional Peer CPRAs (Post-BOS Hold)
- Marysville PD: audit logs, interagency sharing records, training documentation, website compliance
- Wheatland PD: same categories
- **Hold until after BOS presentation** — do not file before June 2026 to preserve comparison framing asymmetry

---

<a name="conclusion"></a>
## Governance Gap — Shared Conclusion

Both primary argument pillars converge on the same structural finding: **YCSO's Flock deployment operates without adequate oversight architecture at every level.**

| Layer | Governance Gap |
|---|---|
| **Officer level** | ~53% of portal exports show blank free-text reason field; drop-down category suppressed by portal configuration; operationally specific queries (make/model/color/partial plate) with blank reason fields; case number entries substituting for purpose statements |
| **Agency level** | Policy 433 § 433.5 two-tier retention has no statutory anchor; four-way conflict across documents unresolved; § 433.8 annual audit requirement never disclosed — either not being conducted or being withheld |
| **Contract level** | MSA Section 3.2 places full compliance responsibility on YCSO; YCSO cannot deflect to Flock |
| **Vendor/Platform level** | Flock controls the audit log, configures the portal export, and determines what fields are included in the public CSV — YCSO cannot independently verify what its own system is recording; the "transparency" portal structurally suppresses the drop-down category field, making the portal's own compliance claim internally contradicted by its own export configuration |
| **Network level** | Statewide/nationwide/Canada access active; outside-agency sharing undisclosed; inbound audit log nonexistent or not produced; training searches at 5,000+ network scope |
| **Funding level** | Measure K committee chair is a YCSO official; independent oversight is structurally compromised |
| **CPRA response record** | Phase 2 final response (#26-245, May 19, 2026): zero training records produced, zero § 433.8 audit memos produced, zero interagency sharing agreements produced, zero SB 34 compliance documentation produced; three responses flagged as improper or non-responsive (§ 832.7 overreach on aggregate training counts; "overly broad" objection to categorical CAD/dispatch request; deflection to 263/2025 — an Elections/ballot drop box contract with no connection to YCSO ALPR or the December 2025 platform change) |
| **Federal level** | JAG grant conditions impose additional obligations; Phase 2 CPRA produced zero JAG compliance documentation; FBI procurement records (May 18, 2026) confirm active federal push to acquire nationwide Flock/ALPR access — YCSO cameras are nodes in a network with active federal agency interest, not a standalone local tool |
| **National level** | The governance failures documented here are not unique to YCSO — agencies across the country deploying Flock show the same pattern; Shorewood IL shut down cameras after two years of mandatory-audit non-compliance; FBI offering up to $36M for nationwide SaaS ALPR access (Flock and Motorola the named likely vendors) further cements that local governance decisions have federal-infrastructure consequences |

**The overarching argument (Option C):**
The goal of the BOS presentation is not to prove that YCSO is uniquely negligent, or that surveillance technology is inherently wrong. The goal is to demonstrate, empirically, that this specific system has operated for three-plus years in Yuba County without the governance mechanisms that were supposed to constrain it ever functioning as designed. The audit log is the compliance mechanism — it is incomplete. The policy framework is the compliance mechanism — its mandatory annual audit has never been disclosed. The oversight committee is the compliance mechanism — it is chaired by the department it oversees. The vendor contract places compliance on YCSO — but YCSO's own CPRA responses confirm it cannot produce the records that demonstrate compliance.

This is not a story about a compliance gap that YCSO failed to close. It is a story about a surveillance system that resists meaningful governance wherever it is deployed — and a Board that has been making renewal decisions based on a vendor marketing phrase rather than an independent assessment of how the system is actually being used.

The Board cannot fix what it cannot see. The ask is to make it visible.

**The BOS ask (June 2026 target):**
1. Commission an independent SB 34 compliance audit of YCSO's Flock usage — not conducted by YCSO
2. Restructure the Measure K Citizens Oversight Committee to exclude YCSO personnel from the chair position
3. Require YCSO to produce a written interagency data sharing disclosure identifying all agencies with access to Yuba County plate data
4. Require YCSO to reconcile and publicly disclose a single, authoritative data retention standard consistent with peer agencies and Government Code § 34090.6

**BOS framing principle:** Lead with liability and fiduciary duty, not civil liberties. "You could be sued" lands harder than "this is a civil rights issue" in a rural county board context. The governance gap creates legal exposure for the county — that is the argument that creates urgency for supervisors. The Shorewood example adds a concrete national reference point: a governing body that accepted "game changer" without independent verification, and whose police department is now shut down pending review.

---

*This document is a living evidence brief. Update when new CPRA production is received, when BOS date is confirmed, or when new evidentiary findings are established. Do not merge with the operational checklist in `Yuba_County_Flock_Oversight_Project.docx`.*
