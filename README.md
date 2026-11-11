# Practo for Animals & AI Education — Intern Assignment

> Product Development, Design & AI Systems Intern assignment.
> Submitted by **avinash-as** · Live: https://avinash-as.github.io/practo/

A complete submission package for the *Product Development, Design & AI Systems Intern* role, covering three product tracks:

1. **Practo for Animals** — MVP homepage / search-page prototype for an animal-care discovery platform.
2. **AI Education** — Landing page for practical AI & digital-skills programmes.
3. **AI-Powered Content Creation System** — Workflow design + a sample AI-generated carousel.

---

## 🌐 Live demo

| Deliverable | Link |
|---|---|
| Submission hub (index) | https://avinash-as.github.io/practo/ |
| Practo for Animals — MVP homepage | https://avinash-as.github.io/practo/practo-animals-homepage.html |
| AI Education — Course landing page | https://avinash-as.github.io/practo/ai-course-landing.html |
| AI carousel viewer | https://avinash-as.github.io/practo/carousel-viewer.html |
| Content workflow diagram | https://avinash-as.github.io/practo/workflow-diagram.html |
| Full written submission | https://avinash-as.github.io/practo/SUBMISSION.md |

---

## 📁 Repository structure

```
practo/
├── index.html                      # Submission hub linking all deliverables
├── practo-animals-homepage.html     # (1) MVP homepage / search page
├── ai-course-landing.html          # (2) Course landing page
├── carousel-viewer.html            # (3) Interactive carousel viewer
├── carousel/                       # (3) 8 generated slide PNGs (1080×1080)
│   ├── slide_01_cover.png
│   ├── slide_02_chatgpt.png
│   ├── ...
│   └── slide_08_cta.png
├── workflow-diagram.html           # (4) 7-step content workflow + automation layer
├── make_carousel.py                # (3) Python/Pillow script that generated the carousel
├── SUBMISSION.md                   # (5) Tools, stack, CTAs, automation explanation
└── README.md
```

---

## 1. Practo for Animals — MVP design

A discovery platform where users find veterinary clinics, hospitals, boarding facilities, diagnostics, ambulances and NGOs.

**MVP elements & features**
- Global search (location + service + animal type) with one-click *Find a Vet*.
- Six service categories: Veterinary Clinics, Hospitals, Boarding & Daycare, Diagnostics/Labs, Pet Ambulance, NGOs & Rescues.
- Provider cards: photo, name, rating + review count, distance, area, open/closed status, service tags, languages, price tier.
- How-it-works (3 steps), trust stats, emergency 24/7 banner.

**Useful filters**
Distance radius · rating · open now / 24×7 / weekend · services (emergency, surgery, vaccination, grooming, home visits) · species treated · verified only · insurance accepted · price tier · language.

**Provider information shown**
Name, photo, address, phone, hours, rating, reviews, services, specialties, emergency flag, certifications, languages, price tier, availability (beds / response time).

**Key CTAs**
- *Find a Vet* (primary, hero) · *Explore Services* · *List Your Business* · *Submit a Correction*
- Card-level: **Book**, **Call**, **Directions**, **Call now** (ambulance), **Book stay** (boarding).

**Mobile-friendly**
Sticky search, collapsible filter drawer, large tap targets (≥ 40px), single-column collapse under 900px, bottom action row on provider cards. Responsive breakpoints at 900px and 560px.

---

## 2. AI Education — Course landing page

Landing page for practical AI & digital-skills programmes aimed at students and young professionals.

**Page structure**
Nav (sticky) → Hero (headline + lead form) → Trust logos → Problem → Outcomes (8) → Curriculum (8 modules) → Who it's for → Projects → Mentors → Testimonials → Pricing (3 tiers) → FAQ → Lead-capture section → Sticky CTA → Footer.

**Value proposition**
"Learn Practical AI & digital skills that actually get you hired" — hands-on, 8 weeks, no coding required, real projects, mentorship, placement support.

**Key CTAs**
*Enroll now* · *Book Free Demo* · *Download Syllabus* · *Talk to counselor* · *Enquire now* · WhatsApp shortcut.

**Lead-capture journey**
1. Visitor lands → hero form captures name, email, phone, persona, interest.
2. Submit → instant syllabus PDF email + WhatsApp opt-in confirmation.
3. Lead routed to CRM + counselor assigned; call within 24 hrs.
4. 5-day nurture email drip (sample lesson, alumni story, FAQ, scholarship, deadline).
5. Exit-intent popup for syllabus; sticky CTA bar persists; abandoned-form WhatsApp reminder.
6. Conversion: enrollment checkout with EMI + group discounts.

---

## 3. AI-Powered Content Creation System

A repeatable workflow that lets the founder create high-quality Instagram/LinkedIn carousels without an in-house designer.

**7-step workflow**
1. Founder enters a raw idea (Notion / Google Form / Slack).
2. AI researches & structures (ChatGPT / Claude / Perplexity) → outline, hook, CTA.
3. Generate headlines & slide-by-slide copy as structured JSON (prompt template).
4. Visual direction, layout & design (palette, typography) → render via Canva/Figma or code (Pillow / HTML→PNG).
5. Produce editable carousel (Canva/Figma) + ready-to-publish PNGs + `caption.txt`.
6. Founder reviews, makes minor edits, approves.
7. Export & publish (Buffer / Later / Meta) + analytics feedback loop.

**Sample carousel** — *5 AI tools every student should know in 2026* (8 slides, 1080×1080, IG/LinkedIn ready), generated with `make_carousel.py` (Python + Pillow) and viewable in `carousel-viewer.html`.

**Automation layer**
Trigger (form/Slack) → Orchestration (Make.com / n8n) → LLM API → image render → Google Drive storage → Slack/Email notification → scheduled publish (Buffer/Later/Meta) → analytics feedback into the prompt library.

---

## 🛠 Tech stack

| Layer | Tools |
|---|---|
| Prototypes | HTML5, CSS3 (responsive, no external deps), vanilla JS |
| Image generation | Python 3 + Pillow (PIL) |
| LLMs | ChatGPT (GPT-4o), Claude, Perplexity |
| Design | Canva (templates + brand kit), Figma |
| Automation | Make.com / n8n, webhooks, Google Drive, Slack/Email |
| Publishing | Buffer / Later / Meta Business Suite, LinkedIn API |
| Hosting | GitHub Pages |

All prototypes are **self-contained** (no CDN, no build step) — they work offline and are trivially hostable.

---

## 🚀 Run locally

```bash
cd practo
python -m http.server 8765
# open http://localhost:8765/index.html
```

Regenerate the carousel images:

```bash
python make_carousel.py   # writes to ./carousel/
```

---

## 📊 Evaluation mapping

| Criterion | Weight | Where it's addressed |
|---|---|---|
| UI/UX & visual design quality | 30% | Both HTML prototypes + 8-slide carousel |
| Product thinking & CTA strategy | 20% | CTAs in `SUBMISSION.md` §2–§3 and in-page |
| AI workflow & automation | 25% | `workflow-diagram.html` + `SUBMISSION.md` §4 |
| Technical execution & tool selection | 15% | Self-contained responsive code + Pillow pipeline |
| Initiative & communication | 10% | This README, submission hub, live deployment |

---

## 📝 License

Submitted as part of an internship application. All content © 2026. Feel free to reference for educational purposes.