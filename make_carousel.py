from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1080, 1080
OUT = r"S:\Project\Assignment\practo\carousel"
os.makedirs(OUT, exist_ok=True)

def font(size, bold=True):
    path = r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf"
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def gradient_bg(img, c1, c2, direction="diag"):
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H-1)
        r = int(c1[0]*(1-t) + c2[0]*t)
        g = int(c1[1]*(1-t) + c2[1]*t)
        b = int(c1[2]*(1-t) + c2[2]*t)
        d.line([(0,y),(W,y)], fill=(r,g,b))

def wrap(draw, text, font_obj, max_width):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=font_obj) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_text_block(draw, text, x, y, font_obj, color, max_width, line_gap=8, align="left"):
    lines = wrap(draw, text, font_obj, max_width)
    yy = y
    for ln in lines:
        if align == "center":
            tw = draw.textlength(ln, font=font_obj)
            draw.text((x - tw/2, yy), ln, font=font_obj, fill=color)
        else:
            draw.text((x, yy), ln, font=font_obj, fill=color)
        yy += font_obj.size + line_gap
    return yy

def round_rect(draw, xy, radius, fill):
    x0,y0,x1,y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)

def slide_base(c1, c2):
    img = Image.new("RGB", (W,H))
    gradient_bg(img, c1, c2)
    # subtle noise overlay
    return img

def footer_chip(draw, idx, total, handle="@ailaunchpad"):
    # slide counter
    draw.text((W-120, H-60), f"{idx}/{total}", font=font(22, False), fill=(255,255,255,180))
    draw.text((60, H-60), handle, font=font(20, False), fill=(255,255,255,150))

# ---------- Slides ----------
slides = []

# 1. Cover
img = slide_base((30,41,59),(79,70,229))
d = ImageDraw.Draw(img)
d.ellipse((W-260, -80, W+80, 200), fill=(255,255,255,18))
d.ellipse((-120, H-260, 200, H+80), fill=(255,255,255,12))
draw_text_block(d, "5 AI tools", 60, 180, font(96), (255,255,255), W-120, 4, "left")
draw_text_block(d, "every student should know in 2026", 60, 300, font(52), (255,210,90), W-120, 6)
draw_text_block(d, "Save this. Share with a friend who needs it.", 60, 500, font(26, False), (200,210,240), W-120, 4)
# tag
round_rect(d, (60, 560, 300, 606), 28, (255,255,255,40))
d.text((84, 572), "⚡ AI Launchpad", font=font(22), fill=(255,255,255))
footer_chip(d, 1, 8)
img.save(os.path.join(OUT, "slide_01_cover.png"))
slides.append("slide_01_cover.png")

# tool slides
tools = [
  ("ChatGPT", "Your all-round AI assistant", "Research, writing, coding, brainstorming. The Swiss army knife — start here if you're new to AI.", "🧠", (16,185,129),(5,150,105)),
  ("Claude", "Best for long documents & reasoning", "Paste entire PDFs, books, codebases. Claude reads carefully and explains clearly.", "✨", (139,92,246),(91,33,182)),
  ("Perplexity", "AI search with sources", "Ask anything — get cited answers from the web. Perfect for research and fact-checking.", "🔍", (59,130,246),(37,99,235)),
  ("Canva + AI", "Design without a designer", "Generate carousels, posts, presentations with Magic Design & AI image tools.", "🎨", (236,72,153),(190,24,93)),
  ("Make / n8n", "Automate your life", "Connect apps and let AI do the boring work — emails, data, social posts, on autopilot.", "⚙️", (245,158,11),(217,119,6)),
]
for i,(name,tag,desc,ico,c1,c2) in enumerate(tools, start=2):
    img = slide_base(c1, c2)
    d = ImageDraw.Draw(img)
    # big icon circle
    d.ellipse((60, 120, 220, 280), fill=(255,255,255,30))
    d.text((105, 160), ico, font=font(80), fill=(255,255,255))
    draw_text_block(d, f"{i-1}. {name}", 60, 320, font(72), (255,255,255), W-120, 4)
    draw_text_block(d, tag, 60, 420, font(34), (255,230,120), W-120, 4)
    draw_text_block(d, desc, 60, 500, font(28, False), (240,245,255), W-120, 6)
    # tip box
    round_rect(d, (60, 720, W-60, 840), 18, (0,0,0,60))
    d.text((84, 740), "💡 Pro tip: combine 2-3 of these for 10x output", font=font(22, False), fill=(255,255,255))
    footer_chip(d, i, 8)
    img.save(os.path.join(OUT, f"slide_0{i}_{name.split()[0].lower()}.png"))
    slides.append(f"slide_0{i}_{name.split()[0].lower()}.png")

# 7. Recap
img = slide_base((30,41,59),(30,41,59))
d = ImageDraw.Draw(img)
# gradient accent top
for x in range(W):
    t=x/W
    r=int(79*(1-t)+245*t); g=int(70*(1-t)+158*t); b=int(229*(1-t)+11*t)
    d.line([(x,0),(x,12)], fill=(r,g,b))
draw_text_block(d, "Quick recap", 60, 120, font(72), (255,255,255), W-120, 4)
recap = ["1. ChatGPT — general assistant","2. Claude — long docs & reasoning","3. Perplexity — research with sources","4. Canva + AI — design","5. Make / n8n — automation"]
yy = 260
for r in recap:
    round_rect(d, (60, yy, W-60, yy+62), 14, (255,255,255,18))
    d.text((84, yy+16), r, font=font(28), fill=(255,255,255))
    yy += 76
draw_text_block(d, "Which one will you try first? Comment below 👇", 60, yy+20, font(30, False), (255,210,90), W-120, 4)
footer_chip(d, 7, 8)
img.save(os.path.join(OUT, "slide_07_recap.png"))
slides.append("slide_07_recap.png")

# 8. CTA
img = slide_base((79,70,229),(245,158,11))
d = ImageDraw.Draw(img)
draw_text_block(d, "Want to master AI in 8 weeks?", 60, 220, font(60), (255,255,255), W-120, 6, "left")
draw_text_block(d, "Join AI Launchpad — practical skills, real projects, mentorship.", 60, 360, font(30, False), (255,240,200), W-120, 6)
round_rect(d, (60, 520, 420, 600), 30, (255,255,255))
d.text((110, 545), "Enroll now →", font=font(30), fill=(79,70,229))
draw_text_block(d, "Link in bio · hello@ailaunchpad.in", 60, 640, font(22, False), (255,255,255), W-120, 4)
footer_chip(d, 8, 8)
img.save(os.path.join(OUT, "slide_08_cta.png"))
slides.append("slide_08_cta.png")

print("Generated", len(slides), "slides")
print(slides)
