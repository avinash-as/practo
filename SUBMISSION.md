# Product Development, Design & AI Systems — Intern Assignment

**Candidate:** (submitted via OpenCode agent)
**Expected effort:** 4–5 hours
**Date:** 2026

---

## 1. Deliverables index

| # | Deliverable | File | How to view |
|---|---|---|---|
| 1 | Practo for Animals — MVP homepage/search page | `practo-animals-homepage.html` | Open in browser / preview |
| 2 | AI Education — Course landing page | `ai-course-landing.html` | Open in browser / preview |
| 3 | AI-generated sample carousel (8 slides) | `carousel/slide_01..08*.png` + `carousel-viewer.html` | Open viewer |
| 4 | Workflow diagram | `workflow-diagram.html` | Open in browser / preview |
| 5 | Tools, stack, CTAs, automation explanation | this document | — |

---

## 2. Practo for Animals — MVP design

### Essential MVP elements & features
- **Global search** (location + service + animal type) with one-click "Find a Vet".
- **Service categories**: Veterinary Clinics, Hospitals, Boarding & Daycare, Diagnostics/Labs, Pet Ambulance, NGOs & Rescues.
- **Provider cards** with photo, name, rating + review count, distance, area, open/closed status, services tags, languages, price tier.
- **Filters**: distance radius, rating, open now / 24×7 / weekend, services (emergency, surgery, vaccination, grooming, home visits), verified only, insurance accepted, price tier, animal/species.
- **Trust signals**: verified badge, real reviews, response time for ambulances, bed availability for boarding.
- **How it works** (3 steps), trust stats, emergency banner for 24/7 care.
- **Provider-side**: "List Your Business" CTA + provider dashboard link.
- **Corrections loop**: "Submit a Correction" CTA to keep data accurate (community trust points).
- **Mobile-friendly**: sticky search, collapsible filter drawer, large tap targets, bottom action row on cards.

### Useful filters & provider information
Filters: distance, rating, availability, service type, species treated, emergency flag, price, verified, insurance, language.
Provider info: name, photo, address, phone, hours, rating, reviews, services, specialties, emergency flag, certifications, languages, price tier, availability (beds/response time).

### Key CTAs
- **Find a Vet** (primary, hero)
- **Explore Services** (secondary)
- **List Your Business** (provider acquisition)
- **Submit a Correction** (data quality)
- Card-level: Book, Call, Directions, Call now (ambulance), Book stay (boarding)

### Attractive / intuitive / mobile-friendly
Teal + warm-orange palette, generous whitespace, card-based results, emoji/icon-led categories for quick scanning, emergency red banner, floating trust badges on hero, responsive grid collapsing to single column under 900px, filter sidebar becoming inline on mobile.

---

## 3. AI Education — Course landing page

### Page structure
Nav (sticky) → Hero (headline + lead form) → Trust logos → Problem → Outcomes (8) → Curriculum (8 modules) → Who it's for → Projects → Mentors → Testimonials → Pricing (3 tiers) → FAQ → Lead-capture section → Sticky CTA → Footer.

### Value proposition
"Learn Practical AI & digital skills that actually get you hired" — hands-on, 8 weeks, no coding required, real projects, mentorship, placement support. Compact, high-ROI, built for students & young professionals.

### Key registration / enquiry CTAs
- Enroll now (primary, nav + sticky + pricing)
- Book Free Demo / Download Syllabus (hero form)
- Talk to counselor (nav)
- Enquire now (bottom lead form)
- WhatsApp shortcut (+91 98765 43210)

### Lead-capture journey
1. Visitor lands → hero form captures name, email, phone, persona, interest.
2. Submit → instant "syllabus PDF" email + WhatsApp opt-in confirmation.
3. Lead routed to CRM (HubSpot/Zoho) + counselor assigned; call within 24 hrs.
4. Nurture sequence: 5-day email drip (sample lesson, alumni story, FAQ, scholarship, deadline).
5. Exit-intent popup for syllabus; sticky CTA bar persists; abandoned-form reminder via WhatsApp.
6. Conversion: enrollment checkout with EMI + group discounts.

---

## 4. AI-powered content creation system

### Workflow (7 steps)
1. Founder enters raw idea (Notion/Google Form/Slack).
2. AI researches & structures (ChatGPT/Claude/Perplexity) → outline + hook + CTA.
3. Generate headlines & slide-by-slide copy (structured JSON) via prompt template.
4. Visual direction, layout & design (palette, typography) → render via Canva/Figma or code (Pillow/HTML→PNG).
5. Produce editable carousel (Canva/Figma) + ready-to-publish PNGs + caption.txt.
6. Founder reviews, minor edits, approves.
7. Export & publish (Buffer/Later/Meta) + analytics feedback loop.

### Recommended tools, stack & automation
- **LLMs**: ChatGPT (GPT-4o), Claude (Sonnet/Opus), Perplexity (research).
- **Design**: Canva (templates, brand kit), Figma (advanced), Python/Pillow or HTML→PNG for code-driven rendering.
- **Automation**: Make.com or n8n (orchestration), webhooks, Google Drive storage, Slack/Email notifications.
- **Publishing**: Buffer / Later / Meta Business Suite; LinkedIn API.
- **Storage/CRM**: Google Drive (per-post folders), Notion (content calendar), Airtable (asset tracker).
- **Analytics**: platform insights → feed top performers into prompt library.

### Tech stack for prototypes
HTML5, CSS3 (responsive, no external deps), vanilla JS, Python 3 + Pillow for image generation. Self-contained, works offline, previewable.

### CTAs summary (cross-product)
- Practo: Find a Vet, Explore Services, List Your Business, Submit a Correction, Book, Call, Directions.
- Course: Enroll now, Book Free Demo, Download Syllabus, Talk to counselor, Enquire now, WhatsApp.
- Carousel/Content: Enroll now (in-slide CTA), link in bio.

---

## 5. Notes on execution
- All prototypes are self-contained HTML (no CDN) so they render offline and are easy to host (GitHub Pages / Netlify / Vercel).
- Carousel generated programmatically with Python/Pillow to demonstrate the "AI/code-assisted production" workflow; the same pipeline can be templated in Canva for non-technical founders.
- Responsive breakpoints at 900px and 560px; tap targets ≥ 40px.

---

*End of submission.*
