#!/usr/bin/env python3
"""Build the local SEO location pages and the FAQ hub, then sync the
shared footer across every page so nothing drifts out of date.
"""
import pathlib
import re

import build_pages as B  # reuse the shell + component helpers

ROOT = pathlib.Path(__file__).parent
IMG = B.IMG

# ---------------------------------------------------------------- helpers


def areas(kick, h2, para, tags):
    chips = "\n".join(
        f'<a href="{href}" class="">{label}</a>' if href else f"<span>{label}</span>"
        for label, href in tags)
    return (B.intro(kick, h2, para) +
            f'\n<div class="areas">\n{chips}\n</div>')


# ---------------------------------------------------------------- DERBY

B.page(
    "golf-lessons-derby.html",
    "Golf Lessons in Derby | PGA Professional Coaching | Evolution Golf Academy",
    "Golf lessons in Derby with PGA Professionals. Trackman coaching, driving range and simulators 15 minutes from Derby city centre via the A610. Book on 07710 582036.",
    None,
    B.hero("Golf Lessons in Derby - PGA Professional Coaching", "Golf Lessons", "Derby.",
           "<strong>Golf lessons in Derby</strong> are available at Evolution Golf Academy, 15 minutes from Derby city centre on the A610. PGA Professional coaching, Trackman data on every shot, a covered floodlit driving range and indoor simulators - all on one site with free parking.",
           IMG["lesson_grip"], "Golf lessons in Derby with a PGA Professional"),
    B.marquee(["Golf Lessons Derby", "PGA Golf Coach Derby", "Trackman Range Near Derby",
               "Golf Tuition Derby", "Beginner Golf Lessons Derby", "Golf Academy Derbyshire"]),
    [
        B.sec(B.intro("Golf coaching near Derby",
                      "Golf Lessons in Derby - PGA Coaches 15 Minutes From <em>the City Centre.</em>",
                      "You do not need a club membership or a long drive to get proper coaching. Evolution Golf Academy sits just outside Derby at Ormonde Fields Golf Club in Codnor, giving Derby golfers <strong>PGA Professional golf tuition</strong> and a Trackman Official Performance Centre on their doorstep.") + "\n" +
              B.cards4([
                  {"img": IMG["lesson_grip"], "alt": "One to one golf lesson near Derby",
                   "h": "1:1 Golf Lessons",
                   "p": "Sixty minutes with a PGA Professional, Trackman data and video analysis throughout. The fastest way to fix what is actually costing you shots."},
                  {"img": IMG["range_night"], "alt": "Trackman driving range near Derby",
                   "h": "Trackman Driving Range",
                   "p": "Covered floodlit bays with ball speed, carry and shot shape on every swing. Walk in, no booking, from £4 a basket."},
                  {"img": IMG["sim"], "alt": "Indoor golf simulator near Derby",
                   "h": "Indoor Golf Simulator",
                   "p": "Play world-famous courses indoors on Trackman. A proper option for Derby golfers through the winter months."},
                  {"img": IMG["tpi"], "alt": "TPI screening and custom fitting near Derby",
                   "h": "TPI Screening &amp; Fitting",
                   "p": "Movement screening and Trackman-based custom club fitting, so your body and your equipment both stop holding you back."},
              ])),
        B.sec(B.split(IMG["range_night"], "Driving range 15 minutes from Derby city centre",
                      "Getting here from Derby",
                      "How Far Is Evolution Golf Academy <em>From Derby?</em>",
                      "<strong>About 15 minutes from Derby city centre</strong> on the A610 - a straightforward drive with no motorway and free parking when you arrive. We are open 7am to 8pm, seven days a week, so lessons fit around work rather than the other way round.",
                      ["<b>15 minutes from Derby city centre</b> via the A610",
                       "<b>Free parking on site</b> - no permits, no charges",
                       "<b>Open 7 days</b> - 7am to 8pm, floodlit all year",
                       "<b>Every service on one site</b> - coaching, range, simulators, fitting"],
                      '<a class="btn ink" href="location.html">Find us</a>'), alt=True),
        B.sec(areas("Areas near Derby we serve",
                    "Other Areas Near Derby <em>We Serve.</em>",
                    "Golfers travel to us from across Derbyshire. If you are within half an hour of Ripley on the road network, the drive is worth it.",
                    [("Derby", None), ("Ilkeston", None), ("Belper", None), ("Long Eaton", None),
                     ("Borrowash", None), ("Duffield", None), ("Heanor", None), ("Alfreton", None),
                     ("Ripley", "location.html"), ("Nottingham", "golf-lessons-nottingham.html")])),
        B.sec(B.faq("Common questions", "Golf Lessons Derby - <em>FAQs.</em>", [
            ("How far is Evolution Golf Academy from Derby city centre?",
             "Roughly 15 minutes by car via the A610. We are at Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RL, with free parking on site."),
            ("How much do golf lessons cost in Derby?",
             "A 1:1 lesson with a PGA Professional is £55 for sixty minutes, and the monthly coaching programme is £60 per month. TPI movement screening is £75. Call 07710 582036 to confirm current prices."),
            ("Is there a Trackman range near Derby?",
             "Yes. Our Trackman driving range is the closest Trackman-equipped range to Derby, with covered floodlit bays open every day from 7am to 8pm. No booking needed."),
            ("Can I turn up without booking?",
             "For the driving range, yes - it is walk-in. Golf lessons, simulator bays and custom fitting sessions need booking in advance."),
        ])),
    ],
    visit_kick="Golf lessons near Derby",
)

# ---------------------------------------------------------------- NOTTINGHAM

B.page(
    "golf-lessons-nottingham.html",
    "Golf Lessons in Nottingham | PGA Professional Coaching | Evolution Golf Academy",
    "Golf lessons near Nottingham with PGA Professionals. Trackman coaching, driving range and simulators 20 minutes from Nottingham via the A610 through Eastwood.",
    None,
    B.hero("Golf Lessons in Nottingham - PGA Professional Coaching", "Golf Lessons", "Nottingham.",
           "<strong>Golf lessons near Nottingham</strong> are available at Evolution Golf Academy, 20 minutes from the city centre on the A610 through Eastwood. A fully equipped PGA coaching facility with Trackman on every shot, indoor simulators and custom club fitting.",
           IMG["over_shoulder"], "Golf lessons near Nottingham with a PGA Professional"),
    B.marquee(["Golf Lessons Nottingham", "PGA Golf Coach Nottingham", "Trackman Range Nottingham",
               "Golf Tuition Nottinghamshire", "Indoor Golf Nottingham", "Golf Academy Near Me"]),
    [
        B.sec(B.intro("Golf coaching near Nottingham",
                      "Golf Lessons Near Nottingham - 20 Minutes <em>on the A610.</em>",
                      "Nottingham golfers get a full performance facility rather than a strip of mats and a bucket. Evolution Golf Academy is a <strong>Trackman Official Performance Centre</strong> with PGA Professional coaching, indoor simulators and a covered floodlit range, straight out through Eastwood.") + "\n" +
              B.cards4([
                  {"img": IMG["lesson_grip"], "alt": "One to one golf lesson near Nottingham",
                   "h": "1:1 Golf Lessons",
                   "p": "Sixty minutes with a PGA Professional. Trackman numbers and video analysis so you can see precisely what changed and why."},
                  {"img": IMG["range_night"], "alt": "Trackman driving range near Nottingham",
                   "h": "Trackman Driving Range",
                   "p": "Covered, floodlit bays with full ball and club data. Walk in seven days a week, all year round."},
                  {"img": IMG["sim"], "alt": "Indoor golf simulator near Nottingham",
                   "h": "Indoor Golf Simulator",
                   "p": "Play championship courses indoors on Trackman. Rain in Nottingham stops being a reason not to play."},
                  {"img": IMG["team"], "alt": "Junior and ladies golf coaching near Nottingham",
                   "h": "Junior &amp; Ladies Coaching",
                   "p": "Structured junior coaching for ages 6 to 16 and ladies lessons for all abilities, from complete beginners upwards."},
              ])),
        B.sec(B.split(IMG["bay_night"], "Golf academy 20 minutes from Nottingham",
                      "Getting here from Nottingham",
                      "How Far Is Evolution Golf Academy <em>From Nottingham?</em>",
                      "<strong>About 20 minutes from Nottingham city centre</strong>, straight out on the A610 through Eastwood. No motorway, no city parking, and free parking on site when you get here.",
                      ["<b>20 minutes from Nottingham</b> via the A610 through Eastwood",
                       "<b>Close to Eastwood, Kimberley and Hucknall</b> - often under 15 minutes",
                       "<b>Free parking</b> and open 7am to 8pm every day",
                       "<b>Everything on one site</b> - coaching, range, simulators, fitness, fitting"],
                      '<a class="btn ink" href="location.html">Find us</a>'), alt=True),
        B.sec(areas("Areas in Nottinghamshire we serve",
                    "Areas in Nottinghamshire <em>We Serve.</em>",
                    "Golfers come to us from across west Nottinghamshire and beyond. If you are within half an hour of Ripley, it is an easy trip.",
                    [("Nottingham", None), ("Eastwood", None), ("Hucknall", None), ("Kimberley", None),
                     ("Kirkby in Ashfield", None), ("Arnold", None), ("Nuthall", None), ("Selston", None),
                     ("Ripley", "location.html"), ("Derby", "golf-lessons-derby.html")])),
        B.sec(B.faq("Common questions", "Golf Lessons Nottingham - <em>FAQs.</em>", [
            ("How far is Evolution Golf Academy from Nottingham?",
             "About 20 minutes from Nottingham city centre via the A610 through Eastwood and Heanor. We are at Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RL."),
            ("What golf lessons are available near Nottingham?",
             "1:1 PGA lessons, a monthly coaching programme, beginner coaching, junior academy for ages 6 to 16, ladies coaching, TPI screening and custom club fitting."),
            ("Is there a Trackman range near Nottingham?",
             "Yes. Our covered floodlit Trackman range is a short drive out on the A610 and is open every day from 7am to 8pm. The range is walk-in with no booking required."),
            ("How do I book golf lessons from Nottingham?",
             "Book online through our booking system or call 07710 582036. Lessons run seven days a week from 7am to 8pm, so early mornings and evenings are both available."),
        ])),
    ],
    visit_kick="Golf lessons near Nottingham",
)

# ---------------------------------------------------------------- FAQS

B.page(
    "faqs.html",
    "Golf Lessons FAQ - Derby &amp; Nottingham | Evolution Golf Academy",
    "Frequently asked questions about golf lessons, the Trackman range, simulators and custom fitting at Evolution Golf Academy near Derby and Nottingham.",
    None,
    B.hero("Golf Lessons in Derby &amp; Nottingham - Frequently Asked Questions", "Your", "Questions.",
           "Everything you need to know about <strong>golf lessons, the Trackman range and the simulator</strong> at Evolution Golf Academy near Derby and Nottingham. If your question is not answered here, call 07710 582036.",
           IMG["bay_night"], "Golf lessons FAQ - Evolution Golf Academy Derby and Nottingham"),
    B.marquee(["Golf Lessons FAQ", "Golf Academy Derby", "Trackman Range Questions",
               "Golf Lesson Prices", "Custom Club Fitting", "Golf Academy Nottingham"]),
    [
        B.sec(B.faq("Location", "Location &amp; Getting to <em>the Academy.</em>", [
            ("Where is Evolution Golf Academy located?",
             "Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley, Derbyshire DE5 9RL. We are on the A610 between Derby and Nottingham, with free parking on site."),
            ("How far is Evolution Golf Academy from Derby city centre?",
             "Around 15 minutes by car via the A610. See our <a href=\"golf-lessons-derby.html\">golf lessons in Derby</a> page for more detail."),
            ("How far is Evolution Golf Academy from Nottingham?",
             "Around 20 minutes via the A610 through Eastwood. See our <a href=\"golf-lessons-nottingham.html\">golf lessons in Nottingham</a> page for more detail."),
            ("What are the opening hours at Evolution Golf Academy?",
             "We are open 7am to 8pm, seven days a week, with no regular closing day. Call 07710 582036 to confirm a specific slot."),
        ])),
        B.sec(B.faq("Lessons and prices", "Golf Lesson Prices &amp; Booking <em>Near Derby.</em>", [
            ("How much do golf lessons cost in Derby?",
             "A 1:1 lesson with a PGA Professional is £55 for sixty minutes. The monthly coaching programme is £60 per month, and TPI movement screening is £75 per session."),
            ("Do I need experience to have a golf lesson?",
             "No. We coach complete beginners regularly. Coaching starts exactly where you are, with no prior knowledge assumed."),
            ("Do I need my own golf clubs for a lesson?",
             "Not for your first session - clubs are available here. If you decide to buy your own later, a custom fitting will make sure you get the right ones."),
            ("Which PGA coach will I have for my lesson?",
             "It depends what you are working on. Will Painter leads general coaching, Scott Hassall handles juniors and Hayden Berridge runs custom fitting. Tell us your goal and we will match you."),
            ("What is the monthly golf coaching programme?",
             "Structured, ongoing coaching at £60 per month. It gives you a planned route to improvement rather than occasional one-off lessons."),
            ("Do you offer junior golf lessons near Derby?",
             "Yes. Scott Hassall PGA runs our <a href=\"junior-academy.html\">junior academy</a> for ages 6 to 16, with individual and group sessions available."),
            ("Do you offer ladies golf lessons near Nottingham?",
             "Yes. <a href=\"ladies-academy.html\">Ladies coaching</a> is available for all abilities, including complete beginners, in a relaxed environment."),
        ])),
        B.sec(B.faq("Facilities", "Trackman Range &amp; <em>Facilities.</em>", [
            ("Do I need to book the Trackman range in advance?",
             "No. The <a href=\"trackman-range.html\">Trackman range</a> is walk-in on a first-come basis. Private teaching bays do need booking ahead."),
            ("How much does the Trackman driving range cost near Derby?",
             "Baskets start from £4. Private bay hire is also available. Call 07710 582036 for current prices before travelling."),
            ("What is Trackman and what does it measure?",
             "Trackman is the launch monitor system used on the PGA Tour. It measures ball speed, club head speed, launch angle, spin rate, carry distance and shot shape on every shot, live on screen."),
            ("How do I book a golf simulator session near Derby?",
             "<a href=\"trackman-simulator.html\">Simulator bays</a> are booked in advance - online or by calling 07710 582036."),
            ("Is there an outdoor driving range at the academy?",
             "Yes. We have a <a href=\"grass-range.html\">grass driving range</a> for hitting off real turf, plus a <a href=\"short-game.html\">short game area</a>. The covered Trackman bays run all year regardless of weather."),
        ])),
        B.sec(B.faq("Fitting", "Custom Golf <em>Club Fitting.</em>", [
            ("Who carries out custom golf club fitting at EGA?",
             "Hayden Berridge PGA. Hayden is a specialist fitter as well as a coach, so the fitting accounts for both your current swing and how it is likely to change."),
            ("Do I have to buy clubs from you after a fitting?",
             "No. You receive a full specification document and can take it to any retailer or manufacturer. Where you buy is entirely your choice."),
            ("How long does a golf club fitting take?",
             "A full bag fitting typically takes 90 minutes to two hours. Single club fittings such as driver only can usually be done in around 60 minutes."),
            ("What is TPI screening?",
             "<a href=\"tpi-screening.html\">TPI screening</a> is a Titleist Performance Institute movement assessment that identifies physical limitations affecting your golf swing, and builds an exercise plan around them."),
        ])),
    ],
    visit_kick="Golf academy near Derby &amp; Nottingham",
)

# ------------------------------------------------- sync footer everywhere
CANON = re.search(r'<footer class="footer">.*?</footer>',
                  (ROOT / "index.html").read_text(), re.S).group(0)
synced = 0
for f in sorted(ROOT.glob("*.html")):
    t = f.read_text()
    m = re.search(r'<footer class="footer">.*?</footer>', t, re.S)
    if m and m.group(0) != CANON:
        f.write_text(t[:m.start()] + CANON + t[m.end():])
        synced += 1
        print("footer synced:", f.name)
print(f"\n{synced} footers synced")
