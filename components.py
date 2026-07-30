#!/usr/bin/env python3
"""Shared page shell and section components for Evolution Golf Academy.

Content lives in content_*.py as plain data. This module owns ALL markup,
so page copy can be rewritten without any risk of breaking the HTML or
using a class that does not exist in css/style.css.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
BOOK = "https://evolutiongolfacademy.setmore.com/book"
PHONE = "07710 582036"

CDN = "https://cdn.prod.website-files.com/6a187dc0c83bd78e959102ad/"
CDN2 = "https://cdn.prod.website-files.com/69f787e6054fa345190b8672/"

IMG = {
    "range_night": CDN + "6a19cc0d7ec60f5606217b47_20-evening-trackman-driving-range-bay.webp",
    "range_sil": CDN + "6a19cbf8ac9a21b7c5db0ae6_19-driving-range-bay-silhouette-swing.webp",
    "bay_night": CDN + "6a19cb0dda2c4575cbb9f495_09-trackman-bay-night-swing-evolution-golf.webp",
    "bay_indoor": CDN + "6a19ca1061facbefc52cfcec_03-indoor-trackman-bay-swing-derbyshire.webp",
    "bay_screen": CDN + "6a19c8be4e31974a754ee1eb_01-trackman-bay-03-screen-evolution-golf-academy.webp",
    "putting": CDN + "6a19caeafa9a2295acb02437_08-putting-green-golf-coaching-derbyshire.webp",
    "lesson_grip": CDN + "6a19cabb70056bbef3b02d14_06-private-golf-lesson-grip-coaching.webp",
    "student_swing": CDN + "6a19cba8d836578fed08d0af_15-student-swing-driving-range-bay.webp",
    "team": CDN + "6a19cb45956dcc81cc7dd50f_11-evolution-golf-academy-team-derbyshire.webp",
    "over_shoulder": CDN + "6a19cbbf8ed985ca80ee0671_16-over-shoulder-trackman-screen-coaching.webp",
    "coach_feedback": CDN + "6a19cbe32d4ad844fe37388c_18-trackman-coaching-feedback-derbyshire.webp",
    "bunker": CDN + "6a19c906f1bbd4795f9ffef9_02-bunker-shot-practice-golf-lesson.webp",
    "launch_data": CDN + "6a19cb7c61facbefc52dcc8c_13-trackman-launch-data-numbers.webp",
    "trackman_screen": CDN + "6a19cad211c56f2ed1804aeb_07-trackman-launch-monitor-screen.webp",
    "fitting_face": CDN + "6a19ca30cb6467aa207ebcee_04-custom-club-fitting-driver-face.webp",
    "fitting_data": CDN + "6a19caa6ea6e2311fa66273d_05-custom-fitting-data-review-trackman.webp",
    "impact": CDN + "6a19cb1d64d0f8482f46a431_10-club-face-impact-detail-fitting.webp",
    "ball_tee": CDN + "6a19cb8fa03fba6512dcc2d3_14-golf-ball-on-tee-driving-range.webp",
    "driver_balls": CDN + "6a19cbd536af20dfed085b35_17-driver-club-and-range-balls.webp",
    "on_course": CDN + "6a19cb593d9fd98845d88253_12-on-course-coaching-couple-lesson-derbyshire.webp",
    "sim": CDN2 + "6a1899edc2f0acdf2f71b74c_669000646476d50f54fe1021_indoor%20track%20simulator%20derby%20nottingham%20golf%20academy.jpg",
    "tpi": CDN2 + "6a189cb44d1578e2e775e2a8_tpi-screening-derby-nottingham%20(1).jpg",
    "ladies": CDN2 + "6a188bd82327d5848fe92ecd_Single%20Golf%20Lessons%20Derby.JPG",
    "junior": CDN2 + "6a189e986d3fbe64c48a7462_Junior%20Golf%20Coaching%20Lessons%20Derby-Nottingham.jpg",
    "beginner": CDN2 + "6a18915b4686c3a560a13641_Beginner%20Golf%20Coaching%20Derby%20Nottingham.JPG",
    "range": CDN2 + "6a18913dce8afd45486378db_Trackman%20Range%20Derby%20and%20Nottingham%20(1)%20(1).jpg",
}

LOGO = CDN2 + "6a1be33ea8018a51046de401_evolution-golf-academy%20(1).png"
LOGO_W = CDN2 + "6a19bd805f1ccb0675266330_evolution-golf-academy-white%20(1).png"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Oswald:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500;1,600'
         '&family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

CHEV = ('<svg viewBox="0 0 8 5" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 0.4375H6.71929C7.15725 '
        '0.4375 7.38357 0.96063 7.08371 1.27984L4.36442 4.17456C4.16695 4.38478 3.83305 4.38478 3.63558 '
        '4.17457L0.916287 1.27984C0.616426 0.960631 0.842751 0.4375 1.28071 0.4375H4Z" fill="currentColor"></path></svg>')
DOT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" width="14" height="14">'
       '<circle cx="7" cy="7" r="6" fill="#f1ece1"></circle></svg>')
PIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 '
       '9 0 1118 0z"/><circle cx="12" cy="10" r="3"/></svg>')
CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
TEL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 '
       '19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 '
       '12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 '
       '2 0 0122 16.92z"/></svg>')
ARR_L = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M11 4L6 9L11 14" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARR_R = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M7 4L12 9L7 14" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ------------------------------------------------------------------ NAV
NAV_GROUPS = [
    ("About", [("about.html", "About Evolution Golf Academy"), ("location.html", "Location"),
               ("meet-team.html", "Meet The Team")]),
    ("Facilities", [("trackman-range.html", "Trackman Driving Range"),
                    ("trackman-simulator.html", "Trackman Simulator"),
                    ("trackman-teaching-bay.html", "Trackman Teaching Bay"),
                    ("golf-fitness.html", "Golf Fitness Suite"),
                    ("grass-range.html", "Grass Driving Range"),
                    ("short-game.html", "Short Game Area")]),
    ("Coaching", [("1-1-lessons.html", "1:1 Golf Lessons"), ("beginner-coaching.html", "Beginner Coaching"),
                  ("monthly-programme.html", "Monthly Programme"), ("get-into-golf.html", "Get Into Golf"),
                  ("junior-academy.html", "Junior Academy"), ("ladies-academy.html", "Ladies Academy"),
                  ("tpi-screening.html", "TPI Screening"), ("swingfit.html", "SwingFit")]),
    ("Trackman", [("trackman-range.html", "Trackman Driving Range"),
                  ("trackman-simulator.html", "Trackman Simulator"),
                  ("trackman-teaching-bay.html", "Trackman Teaching Bay"),
                  ("tournaments.html", "Tournaments"),
                  ("memberships.html", "Memberships")]),
    ("Areas", [("golf-lessons-derby.html", "Golf Lessons Derby"),
               ("golf-lessons-nottingham.html", "Golf Lessons Nottingham"),
               ("golf-lessons-ripley.html", "Golf Lessons Ripley"),
               ("golf-lessons-heanor.html", "Golf Lessons Heanor"),
               ("golf-lessons-alfreton.html", "Golf Lessons Alfreton"),
               ("golf-lessons-ilkeston.html", "Golf Lessons Ilkeston"),
               ("golf-lessons-belper.html", "Golf Lessons Belper"),
               ("golf-lessons-mansfield.html", "Golf Lessons Mansfield"),
               ("golf-lessons-eastwood.html", "Golf Lessons Eastwood"),
               ("golf-lessons-chesterfield.html", "Golf Lessons Chesterfield")]),
]


def nav(cur=None):
    def a(h, l):
        c = ' class="cur"' if h == cur else ""
        return f'<a{c} href="{h}">{l}</a>'
    groups = "\n".join(
        f'<div class="lk"><span>{g} {CHEV}</span>\n<div class="dd">' + "".join(a(h, l) for h, l in items) + "</div></div>"
        for g, items in NAV_GROUPS)
    mob = "\n".join(
        f'<div class="mgrp"><b>{g}</b>' + "".join(a(h, l) for h, l in items) + "</div>"
        for g, items in NAV_GROUPS)
    return f'''<div class="nav">
<div class="in">
<a class="logo" href="index.html"><img src="{LOGO}" alt="Evolution Golf Academy"></a>
<div class="links">
{groups}
<div class="lk"><a href="faqs.html">FAQs</a></div>
<div class="lk"><a href="contact.html">Contact</a></div>
</div>
<div style="display:flex;align-items:center;gap:12px"><a class="btn navbook" href="{BOOK}" target="_blank" rel="noopener">Book a lesson</a>
<button class="burger" aria-label="Menu" onclick="document.body.classList.toggle('menu-open')"><span></span><span></span><span></span></button></div>
</div>
<div class="mmenu">
{mob}
<div class="mgrp"><a href="faqs.html">FAQs</a><a href="contact.html">Contact</a></div>
<a class="btn" href="{BOOK}" target="_blank" rel="noopener" style="margin-top:8px">Book a lesson</a>
</div>
</div>'''


FOOTER = f'''<footer class="footer">
<div class="container">
<div class="fcta">
<h2 class="rv">Come and <span class="o">play</span> with us<br>in Ripley.</h2>
<div class="row rv"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a lesson</a><a class="btn ghost" href="https://www.google.com/maps/place/Evolution+Golf+Academy" target="_blank" rel="noopener">Get directions</a></div>
</div>
<div class="fade"></div>
<div class="fgrid">
<div><a class="logo" href="index.html"><img src="{LOGO_W}" alt="Evolution Golf Academy"></a><p class="desc">A modern golf academy at Ormonde Fields Golf Club in Ripley. PGA coaching, Trackman, fitness and custom fitting, all in one place.</p></div>
<div><div class="h">● Facilities</div><div class="col"><a href="trackman-range.html">Trackman Driving Range</a><a href="trackman-simulator.html">Trackman Simulator</a><a href="trackman-teaching-bay.html">Teaching Bay</a><a href="golf-fitness.html">Golf Fitness Suite</a><a href="grass-range.html">Grass Driving Range</a><a href="short-game.html">Short Game Area</a></div></div>
<div><div class="h">● Coaching</div><div class="col"><a href="1-1-lessons.html">1:1 Golf Lessons</a><a href="beginner-coaching.html">Beginner Coaching</a><a href="monthly-programme.html">Monthly Programme</a><a href="get-into-golf.html">Get Into Golf</a><a href="junior-academy.html">Junior Academy</a><a href="ladies-academy.html">Ladies Academy</a><a href="tpi-screening.html">TPI Screening</a></div></div>
<div><div class="h">● Visit</div><div class="col">
<div class="vline">{PIN}<span>Nottingham Rd, Codnor,<br>Ripley DE5 9RJ</span></div>
<div class="vline">{TEL}<span>{PHONE}</span></div>
<div class="vline">{CLOCK}<span>Mon to Sun · 7am to 8pm</span></div>
<a href="golf-lessons-derby.html">Golf Lessons Derby</a><a href="golf-lessons-nottingham.html">Golf Lessons Nottingham</a><a href="faqs.html">FAQs</a><a href="contact.html">Contact</a>
</div></div>
</div>
<div class="fbar">
<span class="c">© 2026 Evolution Golf Academy</span>
<div class="socials">
<a href="https://www.instagram.com/evolutiongolfacademy/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
<a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
<a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.33z"/><path d="M9.75 15.02l5.75-3.27-5.75-3.27v6.54z" fill="currentColor" stroke="none"/></svg></a>
</div>
</div>
</div>
</footer>'''


def visit(kick="Golf academy near Derby &amp; Nottingham"):
    return f'''<section class="visit">
<div class="container">
<div class="panel">
<div>
<span class="kick">● {kick}</span>
<h2>Nottingham Rd, <em>Codnor, Ripley.</em></h2>
<div class="line">{PIN}Ormonde Fields Golf Club, Nottingham Road, Codnor, DE5 9RJ</div>
<div class="line">{CLOCK}Mon to Sun · 7:00am to 8:00pm</div>
<div class="line">{TEL}{PHONE}</div>
<div class="row"><a class="btn" href="https://www.google.com/maps/place/Evolution+Golf+Academy" target="_blank" rel="noopener">Get directions</a><a class="btn ink" href="contact.html">Contact us</a></div>
</div>
<div class="map"><iframe src="https://www.google.com/maps?q=Evolution+Golf+Academy,+Nottingham+Road,+Codnor,+Ripley+DE5+9RJ&output=embed" loading="lazy" title="Map to Evolution Golf Academy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
</div>
</section>'''


FAC = [("trackman-range.html", "range_night", "Trackman Driving Range"),
       ("trackman-simulator.html", "sim", "Trackman Simulator"),
       ("trackman-teaching-bay.html", "over_shoulder", "Trackman Teaching Bay"),
       ("grass-range.html", "student_swing", "Grass Driving Range"),
       ("short-game.html", "putting", "Short Game Area"),
       ("golf-fitness.html", "team", "Golf Fitness Suite")]


def faccar(skip=None):
    cards = "\n".join(
        f'<a class="fcard" href="{h}"><img src="{IMG[k]}" alt="{t} at Evolution Golf Academy" loading="lazy">'
        f'<div class="ov"><h3>{t}</h3><span>Explore →</span></div></a>'
        for h, k, t in FAC if h != skip)
    return f'''<section class="sec alt">
<div class="container">
<div class="fac-head">
<div><span class="kick" style="color:var(--orange);display:block;margin-bottom:14px">● Explore the academy</span><h2>Our <em>facilities.</em></h2></div>
<div class="carr2">
<button class="cbtn" aria-label="Previous" onclick="scrollCar(this,-1,'.fac-car')">{ARR_L}</button>
<button class="cbtn" aria-label="Next" onclick="scrollCar(this,1,'.fac-car')">{ARR_R}</button>
</div>
</div>
<div class="fac-car">
{cards}
</div>
</div>
</section>'''


def ctabox(h2="Book your golf lesson <em>today.</em>",
           p="PGA Professional coaching, Trackman data and every facility you need to improve - at Evolution Golf Academy, Ripley. Seven days a week."):
    return f'''<div class="ctabox-wrap">
<div class="container">
<div class="ctabox">
<div>
<h2>{h2}</h2>
<p>{p}</p>
</div>
<div class="row"><a class="btn dark" href="{BOOK}" target="_blank" rel="noopener">Book a lesson</a><a class="btn cream" href="contact.html">Ask a question</a></div>
</div>
</div>
</div>'''


# ------------------------------------------------------------- SECTIONS
def _sec(inner, alt=False):
    return f'<section class="sec{" alt" if alt else ""}">\n<div class="container">\n{inner}\n</div>\n</section>'


def _head(kick, h2, p=None, left=False):
    out = f'<div class="intro{" left" if left else ""}">\n<span class="kick">● {kick}</span>\n<h2>{h2}</h2>'
    if p:
        out += f"\n<p>{p}</p>"
    return out + "\n</div>"


def s_intro(kick, h2, p=None, alt=False):
    return _sec(_head(kick, h2, p), alt)


def s_prose(kick, h2, blocks, p=None, alt=False, wide=False):
    out = []
    for kind, val in blocks:
        if kind == "h3":
            out.append(f"<h3>{val}</h3>")
        elif kind == "h4":
            out.append(f"<h4>{val}</h4>")
        elif kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "ul":
            lis = "".join(f"<li>{x}</li>" for x in val)
            out.append(f"<ul>{lis}</ul>")
    body = f'<div class="prose{" wide" if wide else ""}">\n' + "\n".join(out) + "\n</div>"
    return _sec(_head(kick, h2, p) + "\n" + body, alt)


def s_cards(kick, h2, cards, p=None, alt=False):
    n = len(cards)
    grid = "cards3" if n == 3 else "cards4"
    body = "\n".join(
        f'<div class="scard"><div class="ph"><img src="{IMG[c["img"]]}" alt="{c["alt"]}" loading="lazy"></div>'
        f'<div class="tx"><h3>{c["h"]}</h3><p>{c["p"]}</p>'
        + (f'<a class="more" href="{c["href"]}">{c.get("cta", "Learn more")} →</a>' if c.get("href") else "")
        + "</div></div>" for c in cards)
    arrows = (f'<div class="carr">\n<button class="cbtn" aria-label="Previous" onclick="scrollCar(this,-1,\'.{grid}\')">{ARR_L}</button>\n'
              f'<button class="cbtn" aria-label="Next" onclick="scrollCar(this,1,\'.{grid}\')">{ARR_R}</button>\n</div>')
    return _sec(_head(kick, h2, p) + f'\n<div class="{grid}">\n' + body + "\n</div>\n" + arrows, alt)


def s_split(img, img_alt, kick, h2, paras, ticks=None, btn2=None, alt=False):
    if isinstance(paras, str):
        paras = [paras]
    ps = "\n".join(f"<p>{x}</p>" for x in paras)
    tk = ""
    if ticks:
        tk = '\n<ul class="ticks">\n' + "\n".join(
            f'<li><span class="tk">✓</span><span>{t}</span></li>' for t in ticks) + "\n</ul>"
    b2 = f'<a class="btn ink" href="{btn2[1]}">{btn2[0]}</a>' if btn2 else f'<a class="btn ink" href="contact.html">Ask a question</a>'
    return _sec(f'''<div class="split">
<div class="ph"><img src="{IMG[img]}" alt="{img_alt}" loading="lazy"></div>
<div>
<span class="kick">● {kick}</span>
<h2>{h2}</h2>
{ps}{tk}
<div class="row"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a lesson</a>{b2}</div>
</div>
</div>''', alt)


def s_steps(kick, h2, steps, p=None, alt=False):
    body = "\n".join(
        f'<div class="step"><div class="n">{i}</div><div><h3>{h}</h3><p>{t}</p></div></div>'
        for i, (h, t) in enumerate(steps, 1))
    return _sec(_head(kick, h2, p) + f'\n<div class="steps">\n{body}\n</div>', alt)


def s_stats(items, alt=False):
    cells = "\n".join(f'<div class="s"><b>{b}</b><p>{t}</p></div>' for b, t in items)
    cls = "stats four" if len(items) == 4 else "stats"
    return _sec(f'<div class="{cls}">\n{cells}\n</div>', alt)


def s_prices(kick, h2, cards, p=None, alt=False):
    body = "\n".join(
        f'<div class="pcard{" feat" if c.get("feat") else ""}">'
        + (f'<div class="tag">{c["tag"]}</div>' if c.get("tag") else "")
        + f'<div class="amt">{c["amt"]}</div><div class="per">{c["per"]}</div>'
        f'<h3>{c["h"]}</h3><p>{c["p"]}</p>'
        f'<a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book now</a></div>' for c in cards)
    return _sec(_head(kick, h2, p) + f'\n<div class="prices">\n{body}\n</div>', alt)


def s_faq(kick, h2, qs, p=None, alt=False):
    body = "\n".join(
        f'<div class="faqitem"><button class="faqq">{q}</button><div class="faqa">{a}</div></div>'
        for q, a in qs)
    return _sec(_head(kick, h2, p) + f'\n<div class="faq">\n{body}\n</div>', alt)


def s_rel(kick, h2, links, p=None, alt=False):
    body = "\n".join(
        f'<a href="{h}"><b>{t}</b><span>{d}</span><i>{c} →</i></a>' for h, t, d, c in links)
    return _sec(_head(kick, h2, p) + f'\n<div class="rel">\n{body}\n</div>', alt)


def s_areas(kick, h2, tags, p=None, alt=False):
    chips = "\n".join(f'<a href="{h}">{l}</a>' if h else f"<span>{l}</span>" for l, h in tags)
    return _sec(_head(kick, h2, p) + f'\n<div class="areas">\n{chips}\n</div>', alt)


def s_tgrid(kick, h2, items, p=None, alt=False):
    body = "\n".join(
        f'<div class="tcard"><div class="stars">★★★★★</div><p>"{t}"</p><div class="who">{w}</div></div>'
        for t, w in items)
    return _sec(_head(kick, h2, p) + f'\n<div class="tgrid">\n{body}\n</div>', alt)


def s_team(kick, h2, people, p=None, alt=False):
    body = "\n".join(
        f'<div class="tmcard"><div class="ph"><img src="{IMG[m["img"]]}" alt="{m["name"]} - {m["role"]}" loading="lazy"></div>'
        f'<div class="tx"><h3>{m["name"]}</h3><p class="role">{m["role"]}</p><p>{m["bio"]}</p></div></div>'
        for m in people)
    return _sec(_head(kick, h2, p) + f'\n<div class="team">\n{body}\n</div>', alt)


def s_form(kick, h2, intro_p, right_html, alt=False):
    opts = ["Trackman Range", "Junior academy", "Trackman Simulator", "Membership",
            "Golf Lessons", "Something else"]
    o = "".join(f'<option>{x}</option>' for x in opts)
    return _sec(f'''<div class="fgrid2">
<div>
<span class="kick" style="color:var(--orange);display:block;margin-bottom:16px">● {kick}</span>
<h2 style="font-family:var(--disp);font-weight:500;font-size:clamp(30px,3.2vw,44px);line-height:1.08">{h2}</h2>
<p style="font-size:16px;line-height:1.75;color:var(--muted);margin:18px 0 32px">{intro_p}</p>
<form class="form">
<div class="r">
<div class="g"><label for="fname">First name</label><input type="text" id="fname" name="fname" required></div>
<div class="g"><label for="lname">Last name</label><input type="text" id="lname" name="lname" required></div>
</div>
<div class="r">
<div class="g"><label for="email">Email address</label><input type="email" id="email" name="email" required></div>
<div class="g"><label for="phone">Phone number</label><input type="tel" id="phone" name="phone"></div>
</div>
<div class="g"><label for="service">What can we help with</label><select id="service" name="service"><option value="">Please choose</option>{o}</select></div>
<div class="g"><label for="msg">Anything else we should know</label><textarea id="msg" name="msg" placeholder="Your experience level, preferred days and times, any questions"></textarea></div>
<button type="submit" class="btn" style="width:100%">Send message</button>
</form>
</div>
<div>{right_html}</div>
</div>''', alt)


def s_accred(kick, h2, items, p=None, alt=False):
    """Partners and accreditations band. items = [(tag, name, desc)]"""
    body = "\n".join(
        f'<div class="acard"><div class="tag">{t}</div><b>{n}</b><p>{d}</p></div>'
        for t, n, d in items)
    return _sec(_head(kick, h2, p) + f'\n<div class="accred">\n{body}\n</div>', alt)


def s_ctable(kick, h2, cols, rows, p=None, alt=False):
    """Comparison table. cols = (a,b,c), rows = [(a,b,c)]"""
    head = f'<div class="crow head"><div>{cols[0]}</div><div>{cols[1]}</div><div>{cols[2]}</div></div>'
    body = "\n".join(
        f'<div class="crow"><b>{a}</b><div class="mid">{b}</div><p>{c}</p></div>' for a, b, c in rows)
    return _sec(_head(kick, h2, p) + f'\n<div class="ctable">\n{head}\n{body}\n</div>', alt)


def s_ptable(kick, h2, rows, p=None, alt=False):
    """Simple price list. rows = [(label, price)]"""
    body = "\n".join(f'<div class="prow"><span>{l}</span><b>{v}</b></div>' for l, v in rows)
    return _sec(_head(kick, h2, p) + f'\n<div class="ptable">\n{body}\n</div>', alt)


def s_lead(kick, h2, p, note, cta="Send me the guide"):
    """Lead magnet capture block."""
    return f'''<div class="ctabox-wrap">
<div class="container">
<div class="lead">
<div>
<span class="kick">● {kick}</span>
<h2>{h2}</h2>
<p>{p}</p>
</div>
<div>
<form class="form" onsubmit="return false">
<div class="g"><label for="lgname">First name</label><input type="text" id="lgname" name="lgname"></div>
<div class="g"><label for="lgemail">Email address</label><input type="email" id="lgemail" name="lgemail"></div>
<button type="submit" class="btn" style="width:100%">{cta}</button>
</form>
<p class="note">{note}</p>
</div>
</div>
</div>
</div>'''


BUILDERS = {"intro": s_intro, "prose": s_prose, "cards": s_cards, "split": s_split,
            "steps": s_steps, "stats": s_stats, "prices": s_prices, "faq": s_faq,
            "rel": s_rel, "areas": s_areas, "tgrid": s_tgrid, "team": s_team,
            "form": s_form, "accred": s_accred, "ctable": s_ctable,
            "ptable": s_ptable, "lead": s_lead}


def hero(kick, l1, l2, para, img, img_alt):
    return f'''<div class="hero">
<div class="card">
<img class="bg" src="{IMG[img]}" alt="{img_alt}">
<div class="shade"></div>
<div class="content">
<h1 class="kick">{kick}</h1>
<div class="h"><span class="l1">{l1}</span><span class="l2">{l2}</span></div>
<p>{para}</p>
<div class="row"><a class="btn cream" href="{BOOK}" target="_blank" rel="noopener">Book a lesson</a><span class="call">or call {PHONE}</span></div>
</div>
</div>
</div>'''


def marquee(phrases):
    items = "\n".join(f'<div class="it">{p} {DOT}</div>' for p in phrases)
    return f'<div class="marq" aria-hidden="true">\n<div class="track">\n{items}\n</div>\n</div>'


def build(spec):
    """Render one page spec to disk."""
    h = spec["hero"]
    secs = []
    for s in spec["sections"]:
        s = dict(s)
        fn = BUILDERS[s.pop("type")]
        secs.append(fn(**s))
    parts = ["<!DOCTYPE html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             f'<title>{spec["title"]}</title>',
             f'<meta name="description" content="{spec["desc"]}">',
             f'<link rel="canonical" href="https://jag160digital.github.io/evo-golf-website/{spec["file"]}">',
             FONTS, '<link rel="stylesheet" href="./css/style.css">', "</head>", "<body>", "",
             nav(spec.get("cur")), "",
             hero(h["kick"], h["l1"], h["l2"], h["p"], h["img"], h["alt"]), "",
             marquee(spec["marq"]), ""]
    parts += secs
    parts += ["", visit(spec.get("visit_kick", "Golf academy near Derby &amp; Nottingham")), "",
              faccar(skip=spec["file"]), "",
              ctabox(*spec["cta"]) if spec.get("cta") else ctabox(), "",
              FOOTER, "", '<script src="./js/main.js"></script>', "</body>", "</html>", ""]
    (ROOT / spec["file"]).write_text("\n".join(parts))
    return spec["file"]
