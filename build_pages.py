#!/usr/bin/env python3
"""Generate the remaining pages from the canonical index.html shell.

Guarantees every page uses only class names that exist in css/style.css.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
IDX = (ROOT / "index.html").read_text()

# Pull the canonical nav and footer straight out of index.html
NAV = IDX[IDX.index('<div class="nav">'):IDX.index('<div class="hero">')].rstrip()
FOOTER = re.search(r'<footer class="footer">.*?</footer>', IDX, re.S).group(0)
VISIT = re.search(r'<section class="visit">.*?</section>', IDX, re.S).group(0)
FACCAR = re.search(
    r'<section class="sec alt">\n<div class="container">\n<div class="fac-head">.*?</section>',
    IDX, re.S).group(0)
CTABOX = re.search(r'<div class="ctabox-wrap">.*?\n</div>\n</div>\n</div>', IDX, re.S).group(0)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Oswald:ital,wght@0,300;0,400;0,500;0,600;1,400;1,500;1,600'
         '&family=DM+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

CDN = "https://cdn.prod.website-files.com/6a187dc0c83bd78e959102ad/"
CDN2 = "https://cdn.prod.website-files.com/69f787e6054fa345190b8672/"

IMG = {
    "range_night": CDN + "6a19cc0d7ec60f5606217b47_20-evening-trackman-driving-range-bay.webp",
    "bay_night": CDN + "6a19cb0dda2c4575cbb9f495_09-trackman-bay-night-swing-evolution-golf.webp",
    "putting": CDN + "6a19caeafa9a2295acb02437_08-putting-green-golf-coaching-derbyshire.webp",
    "lesson_grip": CDN + "6a19cabb70056bbef3b02d14_06-private-golf-lesson-grip-coaching.webp",
    "student_swing": CDN + "6a19cba8d836578fed08d0af_15-student-swing-driving-range-bay.webp",
    "team": CDN + "6a19cb45956dcc81cc7dd50f_11-evolution-golf-academy-team-derbyshire.webp",
    "over_shoulder": CDN + "6a19cbbf8ed985ca80ee0671_16-over-shoulder-trackman-screen-coaching.webp",
    "bunker": CDN + "6a19c906f1bbd4795f9ffef9_02-bunker-shot-practice-golf-lesson.webp",
    "launch_data": CDN + "6a19cb7c61facbefc52dcc8c_13-trackman-launch-data-numbers.webp",
    "sim": CDN2 + "6a1899edc2f0acdf2f71b74c_669000646476d50f54fe1021_indoor%20track%20simulator%20derby%20nottingham%20golf%20academy.jpg",
    "tpi": CDN2 + "6a189cb44d1578e2e775e2a8_tpi-screening-derby-nottingham%20(1).jpg",
    "ladies": CDN2 + "6a188bd82327d5848fe92ecd_Single%20Golf%20Lessons%20Derby.JPG",
}

DOT = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" width="14" height="14">'
       '<circle cx="7" cy="7" r="6" fill="#f1ece1"></circle></svg>')


def marquee(phrases):
    items = "\n".join(f'<div class="it">{p} {DOT}</div>' for p in phrases)
    return f'<div class="marq" aria-hidden="true">\n<div class="track">\n{items}\n</div>\n</div>'


def hero(kick, l1, l2, para, img, alt):
    return f'''<div class="hero">
<div class="card">
<img class="bg" src="{img}" alt="{alt}">
<div class="shade"></div>
<div class="content">
<h1 class="kick">{kick}</h1>
<div class="h"><span class="l1">{l1}</span><span class="l2">{l2}</span></div>
<p>{para}</p>
<div class="row"><a class="btn cream" href="https://evolutiongolfacademy.setmore.com/book" target="_blank" rel="noopener">Book a lesson</a><span class="call">or call 07710 582036</span></div>
</div>
</div>
</div>'''


def cards4(cards):
    out = []
    for c in cards:
        out.append(
            f'<div class="scard"><div class="ph"><img src="{c["img"]}" alt="{c["alt"]}" loading="lazy"></div>'
            f'<div class="tx"><h3>{c["h"]}</h3><p>{c["p"]}</p></div></div>')
    arrows = ('<div class="carr">\n'
              '<button class="cbtn" aria-label="Previous" onclick="scrollCar(this,-1,\'.cards4\')">'
              '<svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M11 4L6 9L11 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>\n'
              '<button class="cbtn" aria-label="Next" onclick="scrollCar(this,1,\'.cards4\')">'
              '<svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M7 4L12 9L7 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>\n'
              '</div>')
    return '<div class="cards4">\n' + "\n".join(out) + "\n</div>\n" + arrows


def sec(inner, alt=False):
    cls = "sec alt" if alt else "sec"
    return f'<section class="{cls}">\n<div class="container">\n{inner}\n</div>\n</section>'


def intro(kick, h2, p=None):
    body = f'<div class="intro">\n<span class="kick">● {kick}</span>\n<h2>{h2}</h2>'
    if p:
        body += f'\n<p>{p}</p>'
    return body + "\n</div>"


def split(img, alt, kick, h2, para, ticks, btn2=None):
    lis = "\n".join(f'<li><span class="tk">✓</span><span>{t}</span></li>' for t in ticks)
    second = btn2 or '<a class="btn ink" href="contact.html">Ask a question</a>'
    return f'''<div class="split">
<div class="ph"><img src="{img}" alt="{alt}" loading="lazy"></div>
<div>
<span class="kick">● {kick}</span>
<h2>{h2}</h2>
<p>{para}</p>
<ul class="ticks">
{lis}
</ul>
<div class="row"><a class="btn" href="https://evolutiongolfacademy.setmore.com/book" target="_blank" rel="noopener">Book a lesson</a>{second}</div>
</div>
</div>'''


def stats(items):
    cells = "\n".join(f'<div class="s"><b>{b}</b><p>{p}</p></div>' for b, p in items)
    return f'<div class="stats">\n{cells}\n</div>'


def faq(kick, h2, qs):
    items = "\n".join(
        f'<div class="faqitem"><button class="faqq">{q}</button><div class="faqa">{a}</div></div>'
        for q, a in qs)
    return intro(kick, h2) + f'\n<div class="faq">\n{items}\n</div>'


def prices(cards):
    out = []
    for c in cards:
        cls = "pcard feat" if c.get("feat") else "pcard"
        tag = f'<div class="tag">{c["tag"]}</div>' if c.get("tag") else ""
        out.append(f'<div class="{cls}">{tag}<div class="amt">{c["amt"]}</div>'
                   f'<div class="per">{c["per"]}</div><h3>{c["h"]}</h3><p>{c["p"]}</p>'
                   f'<a class="btn" href="https://evolutiongolfacademy.setmore.com/book" target="_blank" rel="noopener">Book now</a></div>')
    return '<div class="prices">\n' + "\n".join(out) + "\n</div>"


def page(fname, title, desc, cur, hero_html, marq_html, body_sections, visit_kick=None):
    nav = NAV
    if cur:
        nav = nav.replace(f'<a href="{fname}">', f'<a class="cur" href="{fname}">', 1)
    visit = VISIT
    if visit_kick:
        visit = visit.replace("● Golf academy near Derby &amp; Nottingham", f"● {visit_kick}")
    parts = [
        "<!DOCTYPE html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        f"<title>{title}</title>", f'<meta name="description" content="{desc}">',
        FONTS, '<link rel="stylesheet" href="./css/style.css">', "</head>", "<body>", "",
        nav, "", hero_html, "", marq_html, "",
    ]
    parts += body_sections
    parts += ["", visit, "", FACCAR, "", CTABOX, "", FOOTER, "",
              '<script src="./js/main.js"></script>', "</body>", "</html>", ""]
    (ROOT / fname).write_text("\n".join(parts))
    print("wrote", fname)


# ---------------------------------------------------------------- PAGES

BOOK = 'https://evolutiongolfacademy.setmore.com/book'

# 1. TRACKMAN DRIVING RANGE ------------------------------------------------
page(
    "trackman-range.html",
    "Trackman Driving Range Derby &amp; Nottingham | Covered Floodlit Bays | Evolution Golf Academy",
    "Trackman driving range near Derby and Nottingham. Covered floodlit bays with ball speed, carry, spin and shot shape data on every shot. Walk in, no booking needed, open 7 days.",
    "trackman-range.html",
    hero("Trackman Driving Range in Derby &amp; Nottingham", "Trackman", "Range.",
         "The <strong>Trackman driving range</strong> at Evolution Golf Academy gives golfers from Derby, Nottingham and across Derbyshire tour-level ball data on every single shot. Covered, floodlit bays mean you can practise properly all year round.",
         IMG["range_night"], "Trackman driving range near Derby and Nottingham"),
    marquee(["Trackman Driving Range Derby", "Driving Range Nottingham", "Ball Speed &amp; Carry Data",
             "Covered Floodlit Bays", "Open 7 Days a Week", "Golf Practice Derbyshire"]),
    [
        sec(intro("Trackman range near Derby &amp; Nottingham",
                  "What Is a Trackman <em>Driving Range?</em>",
                  "A Trackman driving range uses the same radar technology trusted on the PGA Tour to measure your club and ball on every shot. Instead of squinting into the distance guessing where it went, you see <strong>ball speed, launch angle, spin rate, carry distance and shot shape</strong> on a screen in front of you, in real time.") + "\n" +
            cards4([
                {"img": IMG["launch_data"], "alt": "Trackman launch data numbers on screen",
                 "h": "Data on Every Shot",
                 "p": "Ball speed, club speed, launch angle, spin rate, carry and shot shape - measured and displayed the moment the ball leaves the face."},
                {"img": IMG["range_night"], "alt": "Covered floodlit driving range bays in Derbyshire",
                 "h": "Covered, Floodlit Bays",
                 "p": "Rain, wind or a dark winter evening - it makes no difference. Our bays are covered and floodlit so practice never stops between October and March."},
                {"img": IMG["bay_night"], "alt": "Trackman practice games at the driving range",
                 "h": "Practice Games &amp; Challenges",
                 "p": "Trackman's built-in games turn a bucket of balls into targeted practice. Compete against yourself, your mates or golfers around the world."},
                {"img": IMG["student_swing"], "alt": "Golfer using the walk-in driving range near Derby",
                 "h": "Walk In, No Booking",
                 "p": "The range is first come, first served. No app, no phone call, no membership. Turn up, grab a basket and hit balls."},
            ])),
        sec(split(IMG["over_shoulder"], "PGA coach reviewing Trackman data with a golfer",
                  "Why golfers from Derby practise here",
                  "Why Practise at a Trackman Range <em>Near Derby?</em>",
                  "Most range sessions are wasted because you cannot tell what actually changed. A <strong>Trackman range</strong> removes the guesswork - you get a number against every swing, so you know whether that adjustment helped or hurt.",
                  ["<b>Real numbers, not guesswork</b> - see exactly how far each club carries",
                   "<b>Practise all year</b> - covered and floodlit, 7am to 8pm every day",
                   "<b>Track progress over time</b> - compare today's numbers to last month's",
                   "<b>PGA coaches on site</b> - turn a practice session into a lesson whenever you want"],
                  '<a class="btn ink" href="1-1-lessons.html">See golf lessons</a>'), alt=True),
        sec(stats([("7", "Trackman Range Bays"), ("7", "Days a Week"), ("8pm", "Floodlit Until")])),
        sec(faq("Common questions", "Trackman Driving Range Derby &amp; Nottingham - <em>FAQs.</em>", [
            ("Do I need to book the Trackman driving range?",
             "No. The Trackman range is walk-in and works on a first-come basis. Bays are available every day from 7am to 8pm. Private teaching bays for coaching or fitting sessions do need booking in advance."),
            ("What does Trackman measure at the range?",
             "Trackman measures ball speed, club head speed, launch angle, spin rate, carry distance, total distance and shot shape on every shot you hit, displayed live on the screen in your bay."),
            ("How much does the Trackman driving range cost near Derby?",
             "Baskets start from £4 for a small basket. Larger baskets and private bay hire are also available. Call 07710 582036 for current prices before you travel."),
            ("Is the driving range open in winter?",
             "Yes. The bays are covered and floodlit, so the range runs through the winter exactly as it does in summer - 7am to 8pm, seven days a week."),
        ])),
    ],
    visit_kick="Trackman driving range near Derby &amp; Nottingham",
)

# 2. TRACKMAN SIMULATOR ----------------------------------------------------
page(
    "trackman-simulator.html",
    "Golf Simulator Derby &amp; Nottingham | Trackman Indoor Golf | Evolution Golf Academy",
    "Trackman golf simulator near Derby and Nottingham. Play world-famous courses indoors on tour-level Trackman technology. Private bays, book in advance, open 7 days.",
    "trackman-simulator.html",
    hero("Golf Simulator in Derby &amp; Nottingham", "Trackman", "Simulator.",
         "Our <strong>Trackman golf simulator near Derby and Nottingham</strong> lets you play world-famous courses indoors on the same radar technology used on the PGA Tour. Private bays, tour-level accuracy, and weather that never cancels a round.",
         IMG["sim"], "Trackman golf simulator near Derby and Nottingham"),
    marquee(["Golf Simulator Derby", "Indoor Golf Nottingham", "Trackman Simulator",
             "Play Famous Courses", "Private Simulator Bays", "Indoor Golf Derbyshire"]),
    [
        sec(intro("Indoor golf near Derby &amp; Nottingham",
                  "What Is a Trackman <em>Golf Simulator?</em>",
                  "A Trackman golf simulator combines dual-radar ball tracking with a full course simulation, so the shot you hit indoors behaves exactly as it would outdoors. It is the same technology tour players use to dial in their numbers - and it means <strong>a wet Tuesday in February is still a golf day</strong>.") + "\n" +
            cards4([
                {"img": IMG["sim"], "alt": "Playing a famous golf course on the indoor simulator",
                 "h": "Play World-Famous Courses",
                 "p": "Tee it up on courses you would otherwise never get on, without leaving Derbyshire. Play a full round, or just the holes that interest you."},
                {"img": IMG["launch_data"], "alt": "Tour-level Trackman accuracy data",
                 "h": "Tour-Level Accuracy",
                 "p": "Trackman is the launch monitor standard on tour. Every carry number, curve and spin rate is measured, not estimated."},
                {"img": IMG["bay_night"], "alt": "Practice modes and games on the golf simulator",
                 "h": "Practice Modes &amp; Games",
                 "p": "Beyond playing rounds, use the simulator for targeted practice, closest-to-the-pin challenges and long drive competitions."},
                {"img": IMG["over_shoulder"], "alt": "Private golf simulator bay near Nottingham",
                 "h": "Private Bays",
                 "p": "Your own enclosed bay. Bring a friend or three, play at your own pace, no queue behind you and no pressure."},
            ])),
        sec(split(IMG["bay_night"], "Golfers using the indoor simulator near Nottingham",
                  "Who the simulator suits",
                  "Who Is the Golf Simulator <em>Suitable For?</em>",
                  "Just about everyone. The <strong>indoor golf simulator</strong> works as a serious practice tool for low handicappers, a comfortable first introduction for complete beginners, and a genuinely good night out for a group who fancy something different.",
                  ["<b>Club golfers</b> - practise with real numbers through the winter",
                   "<b>Beginners</b> - learn indoors without an audience or a wet fairway",
                   "<b>Groups and friends</b> - play a round together in a couple of hours",
                   "<b>Anyone short on daylight</b> - full rounds at 7am or 7pm, all year"],
                  '<a class="btn ink" href="trackman-range.html">See the range</a>'), alt=True),
        sec(faq("Common questions", "Indoor Golf Simulator Derby &amp; Nottingham - <em>FAQs.</em>", [
            ("How do I book a golf simulator near Derby?",
             "Simulator bays are booked in advance. Book online through our booking system or call 07710 582036. We are 15 minutes from Derby and 20 minutes from Nottingham on the A610."),
            ("What courses are on the Trackman simulator?",
             "The Trackman course library includes a large selection of world-famous championship courses, and it is updated regularly. Ask when you book if there is one in particular you want to play."),
            ("How many people can use a simulator bay?",
             "A bay comfortably takes a small group. Rounds play faster than on a real course, so a group can get eighteen holes done in a fraction of the time."),
            ("Do I need my own golf clubs for the simulator?",
             "No. Clubs are available if you do not have your own, which makes the simulator a straightforward way to try golf for the first time."),
        ])),
    ],
    visit_kick="Golf simulator near Derby &amp; Nottingham",
)

# 3. GOLF FITNESS ----------------------------------------------------------
page(
    "golf-fitness.html",
    "Golf Fitness Suite Derby &amp; Nottingham | TPI Informed Training | Evolution Golf Academy",
    "Golf fitness suite near Derby and Nottingham. TPI informed mobility, strength and speed training built around your golf swing at Evolution Golf Academy, Ripley.",
    "golf-fitness.html",
    hero("Golf Fitness Suite in Derbyshire", "Golf", "Fitness.",
         "The <strong>golf fitness suite</strong> at Evolution Golf Academy gives golfers from Derby, Nottingham and across Derbyshire somewhere to build the mobility, strength and speed their golf swing actually needs - guided by TPI movement screening rather than guesswork.",
         IMG["team"], "Golf fitness suite near Derby and Nottingham"),
    marquee(["Golf Fitness Derby", "Golf Strength Training", "TPI Movement Screening",
             "Swing Speed Training", "Injury Prevention Golf", "Golf Fitness Derbyshire"]),
    [
        sec(intro("Golf fitness near Derby &amp; Nottingham",
                  "Why Does <em>Golf Fitness</em> Matter?",
                  "Most swing faults are not technique problems - they are physical ones. If your hips will not rotate or your thoracic spine will not turn, no amount of coaching will fix the move. Our fitness suite works from a <strong>TPI movement screen</strong>, so training targets the restriction that is actually costing you shots.") + "\n" +
            cards4([
                {"img": IMG["tpi"], "alt": "TPI mobility and movement screening in Derbyshire",
                 "h": "Mobility &amp; Movement",
                 "p": "Rotation through the hips and upper back is where most amateur swings lose power. We screen it, then work on it properly."},
                {"img": IMG["team"], "alt": "Golf specific strength training near Derby",
                 "h": "Strength for Golf",
                 "p": "Golf-specific strength work built around the positions your swing demands, not a generic gym programme borrowed from another sport."},
                {"img": IMG["launch_data"], "alt": "Swing speed training measured on Trackman",
                 "h": "Speed Training",
                 "p": "Clubhead speed is trainable. We measure it on Trackman, work on it in the suite, and measure it again so the gain is provable."},
                {"img": IMG["lesson_grip"], "alt": "Golf injury prevention coaching in Derbyshire",
                 "h": "Injury Prevention",
                 "p": "Backs, elbows and wrists take a beating in golf. Targeted work keeps you playing rather than sitting out half the season."},
            ])),
        sec(split(IMG["tpi"], "TPI screening informing golf fitness training",
                  "Screen first, train second",
                  "How <em>TPI Screening</em> Guides Your Training.",
                  "A <strong>TPI movement screen</strong> tests how your body actually moves, then links each limitation to the swing characteristic it produces. Train the restriction and the swing fault often improves on its own.",
                  ["<b>Screen</b> - a structured physical assessment, not a guess",
                   "<b>Link</b> - every limitation matched to its swing consequence",
                   "<b>Plan</b> - exercises prioritised by what will help your golf most",
                   "<b>Measure</b> - re-screen and re-test speed to prove it worked"],
                  '<a class="btn ink" href="tpi-screening.html">TPI screening</a>'), alt=True),
        sec(faq("Common questions", "Golf Fitness Derby &amp; Nottingham - <em>FAQs.</em>", [
            ("Do I need to be fit already to use the golf fitness suite?",
             "No. The whole point of screening first is that the programme starts from where your body actually is. Plenty of golfers who have not trained in years start here."),
            ("Will golf fitness training actually add distance?",
             "Speed is trainable for most golfers, and we measure clubhead speed on Trackman before and after so you can see the change rather than take our word for it."),
            ("Is golf fitness only for younger players?",
             "Not at all. Older golfers often gain the most, because mobility restrictions build up over time and are very responsive to targeted work."),
            ("How does golf fitness fit around golf lessons?",
             "They work together. Your coach and your screen results inform each other, so technique work and physical work pull in the same direction instead of fighting."),
        ])),
    ],
    visit_kick="Golf fitness suite near Derby &amp; Nottingham",
)

# 4. GRASS RANGE -----------------------------------------------------------
page(
    "grass-range.html",
    "Grass Driving Range Ripley, Derbyshire | Real Turf Practice | Evolution Golf Academy",
    "Grass driving range at Evolution Golf Academy in Ripley, Derbyshire. Hit off real turf like you would on the course. 15 minutes from Derby, 20 from Nottingham.",
    "grass-range.html",
    hero("Grass Driving Range in Ripley, Derbyshire", "Grass", "Range.",
         "The <strong>grass driving range</strong> at Evolution Golf Academy lets golfers from Derby, Nottingham and across Derbyshire hit off real turf - the way the game is actually played, with real turf interaction and honest feedback on your strike.",
         IMG["student_swing"], "Grass driving range in Ripley, Derbyshire"),
    marquee(["Grass Driving Range Ripley", "Real Turf Practice", "Driving Range Derbyshire",
             "Golf Practice Near Derby", "Outdoor Golf Range", "Golf Academy Nottingham"]),
    [
        sec(intro("Grass range near Derby &amp; Nottingham",
                  "Why Practise on a <em>Grass Range?</em>",
                  "Mats forgive a fat shot. Grass does not. Practising off real turf tells you the truth about your low point and strike quality, which is exactly why <strong>hitting off grass</strong> transfers to the course in a way that mat practice never quite does.") + "\n" +
            cards4([
                {"img": IMG["student_swing"], "alt": "Golfer hitting off real turf at the grass range",
                 "h": "Real Turf Interaction",
                 "p": "Take a divot, feel the strike and get honest feedback. A mat will happily hide a heavy contact - grass will not."},
                {"img": IMG["bunker"], "alt": "Practising iron play on the grass range in Derbyshire",
                 "h": "True Strike Feedback",
                 "p": "Where the divot starts tells you where the club bottomed out. It is the most useful piece of feedback in golf and it is free."},
                {"img": IMG["putting"], "alt": "Short game practice alongside the grass range",
                 "h": "Course-Like Practice",
                 "p": "Practise the shot you will actually face on Saturday, from the surface you will actually face it from."},
                {"img": IMG["lesson_grip"], "alt": "PGA coaching on the grass driving range",
                 "h": "Coaching on Grass",
                 "p": "Lessons can be taken out onto the grass when it suits the work, so what you learn transfers straight onto the course."},
            ])),
        sec(split(IMG["range_night"], "Grass range and covered Trackman bays at Evolution Golf Academy",
                  "Grass and Trackman together",
                  "Use the Grass Range <em>and</em> the Trackman Bays.",
                  "The best practice sessions use both. Work on numbers and technique in a <strong>covered Trackman bay</strong>, then take it out onto grass to check it holds up against real turf. When the weather turns, the covered bays keep you going.",
                  ["<b>Grass in summer</b> - real turf, real divots, real feedback",
                   "<b>Covered bays all year</b> - floodlit and weatherproof",
                   "<b>Short game area</b> - chipping, pitching and putting on site",
                   "<b>PGA coaches on site</b> - seven days a week, 7am to 8pm"],
                  '<a class="btn ink" href="trackman-range.html">Trackman range</a>'), alt=True),
        sec(faq("Common questions", "Grass Driving Range Derbyshire - <em>FAQs.</em>", [
            ("Is the grass driving range open all year?",
             "The grass range is weather and ground dependent, so it runs through the drier months. The covered Trackman bays are floodlit and open every day of the year, which is what we fall back on when the grass is not playable."),
            ("Do I need to book the grass range?",
             "No, it is walk-in like the rest of the range. Call 07710 582036 first if you are travelling from Derby or Nottingham and want to check ground conditions."),
            ("Can I have a golf lesson on the grass range?",
             "Yes. Where the work suits it, your PGA coach can take the lesson out onto grass rather than staying in a bay."),
            ("Where is the grass driving range?",
             "At Evolution Golf Academy, Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RL - 15 minutes from Derby and 20 minutes from Nottingham on the A610."),
        ])),
    ],
    visit_kick="Grass driving range in Ripley, Derbyshire",
)

# 5. SHORT GAME ------------------------------------------------------------
page(
    "short-game.html",
    "Short Game Practice Area Derbyshire | Chipping, Pitching &amp; Putting | Evolution Golf Academy",
    "Short game practice area near Derby and Nottingham. Chipping, pitching, bunker play and putting at Evolution Golf Academy, Ripley, Derbyshire. Open 7 days.",
    "short-game.html",
    hero("Short Game Practice Area in Derbyshire", "Short", "Game.",
         "The <strong>short game practice area</strong> at Evolution Golf Academy gives golfers from Derby, Nottingham and across Derbyshire somewhere to work on chipping, pitching, bunker play and putting - the shots that decide most scorecards.",
         IMG["putting"], "Short game practice area near Derby and Nottingham"),
    marquee(["Short Game Practice Derbyshire", "Chipping &amp; Pitching", "Bunker Practice",
             "Putting Green Ripley", "Golf Lessons Derby", "Golf Academy Nottingham"]),
    [
        sec(intro("Short game practice near Derby &amp; Nottingham",
                  "Why Does the <em>Short Game</em> Matter Most?",
                  "Roughly half your shots happen within a hundred yards of the flag, yet almost nobody practises there. An hour on the <strong>short game area</strong> will take more strokes off your handicap than an hour smashing drivers ever will.") + "\n" +
            cards4([
                {"img": IMG["putting"], "alt": "Putting green practice in Derbyshire",
                 "h": "Putting Green",
                 "p": "Work on pace, read and start line on a true surface. Three-putts are the cheapest shots in golf to eliminate."},
                {"img": IMG["bunker"], "alt": "Bunker practice at the short game area",
                 "h": "Bunker Play",
                 "p": "Practise the shot most golfers dread until it stops being a shot you dread. Technique here is very learnable."},
                {"img": IMG["lesson_grip"], "alt": "Chipping and pitching coaching near Derby",
                 "h": "Chipping &amp; Pitching",
                 "p": "Build a reliable chip and a controlled pitch. Distance control around the green is where handicaps genuinely fall."},
                {"img": IMG["over_shoulder"], "alt": "Short game coaching with a PGA professional",
                 "h": "Short Game Coaching",
                 "p": "Take a lesson focused entirely on scoring shots. Our PGA coaches will tell you exactly where your strokes are going."},
            ])),
        sec(split(IMG["putting"], "Golfer practising chipping at Evolution Golf Academy",
                  "Where handicaps actually fall",
                  "Practise the Shots That <em>Save Strokes.</em>",
                  "Most amateurs practise what they enjoy rather than what they need. A <strong>short game session</strong> is less glamorous than the driving range and considerably more effective - and it is available seven days a week here.",
                  ["<b>Chipping and pitching</b> - distance control from inside 50 yards",
                   "<b>Bunker technique</b> - a repeatable method, not hope",
                   "<b>Putting</b> - pace and start line on a true green",
                   "<b>PGA coaching available</b> - book a short game specific lesson"],
                  '<a class="btn ink" href="1-1-lessons.html">Book a lesson</a>'), alt=True),
        sec(faq("Common questions", "Short Game Practice Derbyshire - <em>FAQs.</em>", [
            ("Do I need to book the short game area?",
             "No. The short game area is available to use alongside the rest of the practice facilities at Evolution Golf Academy, seven days a week from 7am to 8pm."),
            ("Can I have a lesson focused only on my short game?",
             "Yes. Plenty of golfers book a lesson specifically for chipping, pitching, bunker play or putting. It is often the fastest way to drop shots off a scorecard."),
            ("Is there a practice bunker?",
             "Yes, the short game area includes bunker practice as well as chipping, pitching and a putting surface."),
            ("How far is the short game area from Derby and Nottingham?",
             "We are at Ormonde Fields Golf Club, Codnor, Ripley DE5 9RL - about 15 minutes from Derby city centre and 20 minutes from Nottingham via the A610."),
        ])),
    ],
    visit_kick="Short game practice near Derby &amp; Nottingham",
)

# 6. LADIES ACADEMY --------------------------------------------------------
page(
    "ladies-academy.html",
    "Ladies Golf Lessons Derby &amp; Nottingham | PGA Coaching for Women | Evolution Golf Academy",
    "Ladies golf lessons near Derby and Nottingham. PGA Professional coaching for women of all abilities, from complete beginners upwards, at Evolution Golf Academy, Ripley.",
    "ladies-academy.html",
    hero("Ladies Golf Lessons in Derby &amp; Nottingham", "Ladies", "Academy.",
         "<strong>Ladies golf lessons near Derby and Nottingham</strong> at Evolution Golf Academy are open to all abilities, from women who have never held a club to established players chasing a lower handicap. PGA Professional coaching, Trackman data, and none of the stuffiness.",
         IMG["ladies"], "Ladies golf lessons near Derby and Nottingham"),
    marquee(["Ladies Golf Lessons Derby", "Womens Golf Coaching Nottingham", "PGA Golf Coach",
             "Beginner Ladies Golf", "Golf Lessons Derbyshire", "Ladies Golf Academy"]),
    [
        sec(intro("Ladies golf coaching near Derby &amp; Nottingham",
                  "What Do Ladies Golf Lessons <em>Include?</em>",
                  "Ladies golf lessons at Evolution Golf Academy are built the same way every lesson here is - around <strong>Trackman data, video analysis and a PGA Professional</strong> who explains what is happening in plain English. Where you start is entirely up to you.") + "\n" +
            cards4([
                {"img": IMG["ladies"], "alt": "Ladies beginner golf lesson near Derby",
                 "h": "Complete Beginners Welcome",
                 "p": "Never played? That is genuinely fine. Clubs provided, no prior knowledge assumed, and nobody watching over your shoulder."},
                {"img": IMG["over_shoulder"], "alt": "Trackman data in a ladies golf lesson",
                 "h": "Trackman on Every Shot",
                 "p": "The same tour-level technology every golfer here gets. Real numbers, so improvement is measured rather than imagined."},
                {"img": IMG["lesson_grip"], "alt": "One to one ladies golf coaching in Derbyshire",
                 "h": "One to One Coaching",
                 "p": "Private lessons at your pace, working on whatever you want to work on - technique, short game or getting round a course."},
                {"img": IMG["putting"], "alt": "Getting onto the golf course after ladies lessons",
                 "h": "Getting Onto the Course",
                 "p": "Coaching that ends with you actually playing golf, not just hitting balls. Etiquette and course management included."},
            ])),
        sec(split(IMG["team"], "PGA coaches at Evolution Golf Academy",
                  "Why women choose EGA",
                  "Why Choose EGA for <em>Ladies Golf Lessons?</em>",
                  "Golf has a reputation for being unwelcoming, and plenty of clubs have earned it. Evolution Golf Academy is a modern coaching facility rather than a members' club, so there is <strong>no dress code to decode and no clubhouse politics</strong> - just coaching.",
                  ["<b>All abilities</b> - beginners through to low handicappers",
                   "<b>PGA Professional coaching</b> - qualified, experienced, patient",
                   "<b>Relaxed environment</b> - a coaching academy, not a members' club",
                   "<b>Open 7 days</b> - 7am to 8pm, so lessons fit round work and family"],
                  '<a class="btn ink" href="beginner-coaching.html">Beginner coaching</a>'), alt=True),
        sec(faq("Common questions", "Ladies Golf Lessons Derby &amp; Nottingham - <em>FAQs.</em>", [
            ("I have never played golf before - can I still book a lesson?",
             "Yes, and a lot of our ladies lessons start exactly there. No experience is assumed, clubs are provided, and the first session is about getting you comfortable rather than perfect."),
            ("Do I need my own golf clubs for a ladies lesson?",
             "Not for your first lesson. Clubs are available here. If you decide to buy your own later, a custom fitting will make sure you get the right ones for your swing."),
            ("Are there ladies only golf sessions?",
             "Ladies coaching is available as one to one lessons and group sessions. Call 07710 582036 to talk through which format suits you best."),
            ("How much do ladies golf lessons cost near Derby?",
             "Lessons are priced the same as all our PGA coaching, with monthly programmes available for ongoing structured improvement. Call 07710 582036 for current prices."),
        ])),
    ],
    visit_kick="Ladies golf lessons near Derby &amp; Nottingham",
)

# 7. TPI SCREENING ---------------------------------------------------------
page(
    "tpi-screening.html",
    "TPI Screening Derby &amp; Nottingham | Titleist Performance Institute | Evolution Golf Academy",
    "TPI screening near Derby and Nottingham. Titleist Performance Institute movement screening identifies the physical limitations affecting your golf swing. Evolution Golf Academy, Ripley.",
    "tpi-screening.html",
    hero("TPI Screening in Derby &amp; Nottingham", "TPI", "Screening.",
         "<strong>TPI screening near Derby and Nottingham</strong> uses the Titleist Performance Institute assessment to find the physical limitations holding your golf swing back - then links each one to the swing fault it actually causes.",
         IMG["tpi"], "TPI screening near Derby and Nottingham"),
    marquee(["TPI Screening Derby", "Titleist Performance Institute", "Golf Movement Screening",
             "Swing Analysis Nottingham", "Golf Fitness Derbyshire", "PGA Golf Coach"]),
    [
        sec(intro("TPI screening near Derby &amp; Nottingham",
                  "What Is <em>TPI Screening?</em>",
                  "TPI screening is a structured physical assessment developed by the Titleist Performance Institute. It tests how your body moves - rotation, stability, balance and mobility - and then connects each limitation to the <strong>swing characteristic it produces</strong>. If your body physically cannot make a position, coaching alone will never get you there.") + "\n" +
            cards4([
                {"img": IMG["tpi"], "alt": "TPI movement screen assessment in Derbyshire",
                 "h": "The Movement Screen",
                 "p": "A structured series of physical tests covering rotation, stability, mobility and balance. It takes the guesswork out of why your swing does what it does."},
                {"img": IMG["over_shoulder"], "alt": "Linking TPI results to golf swing faults",
                 "h": "Swing Connection",
                 "p": "Every limitation found is matched to the swing characteristic it tends to cause - early extension, loss of posture, casting and the rest."},
                {"img": IMG["launch_data"], "alt": "TPI screening personal report",
                 "h": "Your Personal Report",
                 "p": "You leave with a clear written picture of what your body can and cannot currently do, and what that means for your golf."},
                {"img": IMG["team"], "alt": "Golf exercise plan following TPI screening",
                 "h": "Exercise Plan",
                 "p": "A prioritised set of exercises targeting the restrictions that will make the biggest difference to your golf swing first."},
            ])),
        sec(prices([
            {"amt": "£75", "per": "per session", "h": "TPI Screening",
             "p": "Full Titleist Performance Institute movement screen, swing linkage and a personal exercise plan."},
            {"amt": "£55", "per": "per session", "h": "1:1 PGA Lesson", "feat": True, "tag": "Most Popular",
             "p": "Sixty minutes with a PGA Professional, Trackman data and video analysis throughout.", },
            {"amt": "£60", "per": "per month", "h": "Monthly Programme",
             "p": "Structured ongoing coaching so screening findings actually turn into swing change."},
        ])),
        sec(split(IMG["lesson_grip"], "PGA coach explaining TPI screening results",
                  "Screening and coaching together",
                  "How TPI Screening Improves <em>Your Golf Lessons.</em>",
                  "A coach can spend months chasing a swing fault that is physical rather than technical. <strong>Screening first</strong> tells your coach which faults are worth working on directly and which need the body addressing before the swing will follow.",
                  ["<b>Stop chasing impossible positions</b> - work with your body, not against it",
                   "<b>Faster progress</b> - lessons target what is actually fixable now",
                   "<b>Fewer injuries</b> - compensations are what tend to hurt backs and elbows",
                   "<b>Feeds the fitness suite</b> - screening results drive your training plan"],
                  '<a class="btn ink" href="golf-fitness.html">Golf fitness suite</a>'), alt=True),
        sec(faq("Common questions", "TPI Screening Derby &amp; Nottingham - <em>FAQs.</em>", [
            ("What happens during a TPI screening session?",
             "You go through a structured series of physical movement tests. Each result is then linked to the swing characteristics it typically produces, and you leave with a written report and a prioritised exercise plan."),
            ("Do I need to be a good golfer to have a TPI screening?",
             "No. TPI screening is useful at every level. Beginners benefit because it stops them building compensations in from the start."),
            ("How much does TPI screening cost near Derby?",
             "TPI movement screening is £75 per session. Call 07710 582036 to book, or to talk through whether screening or a standard lesson is the better place to start."),
            ("Is TPI screening the same as a golf lesson?",
             "No. A lesson works on your swing, a TPI screen assesses your body. They complement each other - the screen tells your coach what your body will and will not currently allow."),
        ])),
    ],
    visit_kick="TPI screening near Derby &amp; Nottingham",
)

print("\ndone")
