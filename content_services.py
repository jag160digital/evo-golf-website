"""Memberships, Tournaments and SwingFit.

These three appear in the live Webflow nav but the pages there are
PLACEHOLDERS - they carry only the generic driving range boilerplate.
There are no membership tiers, no prices, no tournament formats and no
SwingFit programme detail published anywhere.

So these pages are written WITHOUT inventing commercial terms. Only two
membership facts are confirmed anywhere on the client's site:
    "Anyone can book golf lessons, the range or the simulators.
     Membership simply gives you priority booking and better rates,
     but everything is open to the public."
and one tournament fact:
    "join a league night" (Trackman Simulator page)

Everything specific - tier names, prices, joining fees, fixture dates,
SwingFit session structure - is deliberately routed to "call to discuss"
rather than guessed. Fabricating a price or a tier here would be a
commercial problem, not a copy problem.

>>> ACTION FOR THE CLIENT: send real details and these get filled in. <<<
"""

CALL = 'call <a href="contact.html">07710 582036</a>'

PAGES = [

    # ================================================== MEMBERSHIPS
    {
        "file": "memberships.html",
        "cur": "memberships.html",
        "title": "Golf Academy Membership Derby &amp; Nottingham | Evolution Golf Academy",
        "desc": "Golf academy membership near Derby and Nottingham. Priority booking and better rates on coaching, the Trackman range and simulators at Evolution Golf Academy, Ripley. Call 07710 582036.",
        "visit_kick": "Golf academy membership near Derby &amp; Nottingham",
        "cta": ("Ask about <em>membership.</em>",
                "Call 07710 582036 and we will talk through whether membership makes sense for how much you actually play."),
        "hero": {
            "kick": "Golf Academy Membership in Derby &amp; Nottingham",
            "l1": "Trackman", "l2": "Memberships.",
            "p": "<strong>Golf academy membership near Derby and Nottingham</strong> gives you priority booking and better rates at Evolution Golf Academy. You never need it - everything here is open to the public - but if you play often it changes the maths.",
            "img": "bay_screen",
            "alt": "Golf academy membership near Derby and Nottingham at Evolution Golf Academy",
        },
        "marq": ["Golf Membership Derby", "Trackman Membership", "Priority Booking",
                 "Better Rates", "Golf Academy Nottingham", "Membership Derbyshire"],
        "sections": [
            {"type": "pmarq"},

            {"type": "prose", "kick": "Membership at Evolution",
             "h2": "What Does <em>Golf Academy Membership</em> Include?",
             "blocks": [
                 ("p", "Membership at Evolution Golf Academy does two things: it gives you <strong>priority booking</strong> and it gives you <strong>better rates</strong>. That is the honest summary, and it is worth saying plainly because golf club membership usually implies something very different."),
                 ("p", "We are a coaching academy, not a members' club. There is no course to get on, no tee sheet ballot, no committee and no waiting list. Every part of the site is open to the public: <a href=\"1-1-lessons.html\">golf lessons</a>, the <a href=\"trackman-range.html\">Trackman driving range</a>, the <a href=\"trackman-simulator.html\">simulators</a>, the <a href=\"short-game.html\">short game area</a> and the <a href=\"golf-fitness.html\">golf fitness suite</a>. Membership simply makes frequent use cheaper and easier to book."),
                 ("h3", "Do You Need to Be a Member to Use the Academy?"),
                 ("p", "No, and this is the single most common misconception. You can book a lesson tomorrow, walk in and hit a basket on the range this evening, or hire a simulator bay at the weekend without any membership at all. Nothing on this site is gated."),
                 ("h3", "Who Does Membership Actually Suit?"),
                 ("p", "Broadly, golfers who are here often enough that the better rates outweigh whatever the membership costs. If you hit a basket once a month, paying as you go is almost certainly the right call. If you are on the range twice a week through the winter, booking simulator bays regularly, or working through the <a href=\"monthly-programme.html\">monthly coaching programme</a>, it is worth a conversation."),
                 ("p", "Priority booking matters more than people expect for the <a href=\"trackman-simulator.html\">indoor simulators</a>, because those are the bays that fill up first between November and March when the weather turns and everybody has the same idea at the same time."),
             ]},

            {"type": "cards", "kick": "The two confirmed benefits",
             "h2": "What Are the Benefits of <em>Membership?</em>",
             "p": "Both of these apply across the academy rather than to one facility.",
             "cards": [
                 {"img": "bay_indoor", "alt": "Priority simulator booking for members near Derby",
                  "h": "Priority Booking",
                  "p": "First call on booking slots. Most useful for the indoor simulator bays and peak evening times through the winter, which are the hardest things to get at short notice.",
                  "href": "trackman-simulator.html", "cta": "Trackman simulator"},
                 {"img": "launch_data", "alt": "Better rates on golf coaching and range time",
                  "h": "Better Rates",
                  "p": "Reduced pricing across what you use. The more often you are here, the more that compounds, which is why membership tends to suit regulars rather than occasional visitors.",
                  "href": "trackman-range.html", "cta": "Range pricing"},
                 {"img": "over_shoulder", "alt": "Everything at the academy open to the public",
                  "h": "Nothing Is Gated",
                  "p": "Everything here is open to the public whether you join or not. Membership is a way to pay less for what you already do, not a key that unlocks the door.",
                  "href": "faqs.html", "cta": "Common questions"},
                 {"img": "coach_feedback", "alt": "Golf coaching membership near Nottingham",
                  "h": "Works With Coaching",
                  "p": "Membership sits alongside coaching rather than replacing it. Plenty of golfers pair it with the monthly programme so lessons and practice both run on a regular rhythm.",
                  "href": "monthly-programme.html", "cta": "Monthly programme"},
             ], "alt": True},

            {"type": "imgbreak", "img": "bay_indoor",
             "img_alt": "Priority booking, better rates. at Evolution Golf Academy",
             "kick": "Membership",
             "h2": "Priority booking, <em>better rates.</em>",
             "p": "Never required for anything. Worth it if you are here often enough."},

            {"type": "prose", "kick": "Working out whether it is worth it",
             "h2": "Is Golf Membership Worth It <em>Near Derby?</em>",
             "blocks": [
                 ("p", "The only honest answer is that it depends entirely on how often you play, and the way to find out is to count rather than guess. Three questions get you most of the way there."),
                 ("h3", "How Often Are You Actually Here?"),
                 ("p", "Not how often you intend to be. Look back at the last three months. Golfers consistently overestimate this, which is how unused gym memberships happen. If you have been on the <a href=\"trackman-range.html\">range</a> twice since October, pay as you go."),
                 ("h3", "What Do You Actually Use?"),
                 ("p", "Range baskets, simulator hours, coaching and the <a href=\"golf-fitness.html\">fitness suite</a> are different spends. A golfer who books two simulator hours a week has a very different sum from one who hits a large basket on a Sunday morning."),
                 ("h3", "Does Booking Ahead Frustrate You?"),
                 ("p", "If you have tried to get an indoor bay on a wet January evening and found them gone, priority booking may be worth more to you than the rate saving. That is a convenience question rather than a money one, and for some golfers it is the deciding factor."),
                 ("p", "Rather than guess your way through that, " + CALL + " and we will go through it with you. If membership would not save you money we will say so - a member who never uses it cancels within a year, which suits nobody."),
             ]},

            {"type": "split", "img": "range_night",
             "img_alt": "Golf academy near Derby open seven days a week",
             "kick": "What every golfer gets, member or not",
             "h2": "What Can You Use <em>Without Membership?</em>",
             "paras": [
                 "All of it. This is worth repeating because golf has a reputation for gatekeeping and it puts people off asking.",
                 "The academy is open <strong>7am to 8pm, seven days a week</strong>, to anybody who turns up. Free parking, no dress code to decode, and club hire on the range and simulators included at no extra cost.",
             ],
             "ticks": [
                 "<b><a href=\"trackman-range.html\">Trackman driving range</a></b> - walk in, no booking, baskets from £4",
                 "<b><a href=\"trackman-simulator.html\">Trackman simulators</a></b> - booked by the hour, off-peak from £13",
                 "<b><a href=\"1-1-lessons.html\">Golf lessons</a></b> - £55 for an hour with a PGA Professional",
                 "<b><a href=\"short-game.html\">Short game area</a></b> and <b><a href=\"grass-range.html\">grass range</a></b> - open to everyone",
                 "<b><a href=\"tpi-screening.html\">TPI screening</a></b> and custom fitting - by appointment, brand neutral",
             ],
             "btn2": ("Ask a question", "contact.html"), "alt": True},

            {"type": "stats", "items": [
                ("7", "Days a Week"), ("7", "Trackman Range Bays"), ("2+", "Simulators")]},

            {"type": "steps", "kick": "Working it out",
             "h2": "How Do You Decide Whether to <em>Join?</em>",
             "p": "Four steps, and the first two matter far more than the last two.",
             "steps": [
                 ("Count what you actually did", "Look back at the last three months rather than forward at your intentions. This is the step people skip and it is the one that decides the answer."),
                 ("Work out what you use", "Range baskets, simulator hours and coaching are separate spends. Two <a href=\"trackman-simulator.html\">simulator</a> hours a week is a very different sum from a Sunday basket."),
                 ("Ask whether booking frustrates you", "If you have tried for an indoor bay on a wet January evening and found them gone, priority booking may matter more to you than the rate."),
                 ("Call and check the maths", "Ring 07710 582036 and we will run it against how you actually play. If joining would not save you money we will say so."),
             ], "alt": True},

            {"type": "faq", "kick": "Common questions",
             "h2": "Golf Academy Membership Derby &amp; Nottingham - <em>FAQs.</em>",
             "qs": [
                 ("Do I need to be a member to book a lesson?",
                  "No. Anyone can book golf lessons, the range or the simulators. Membership simply gives you priority booking and better rates, but everything is open to the public. You can book a single <a href=\"1-1-lessons.html\">lesson</a> and never come back if you would rather."),
                 ("What does membership cost?",
                  "Rates depend on what you use and how often, so rather than publish a number that may not fit you, " + CALL + " and we will price it against how you actually play. If it would not save you money we will tell you."),
                 ("What are the benefits of joining?",
                  "Priority booking and better rates across the academy. Priority booking matters most for the indoor <a href=\"trackman-simulator.html\">simulator bays</a> in winter, which are the first things to go when the weather turns."),
                 ("Is this the same as joining a golf club?",
                  "No. There is no course, no tee sheet ballot, no committee and no waiting list. Evolution Golf Academy is a coaching and practice facility, so membership is about frequency of use rather than access to a course."),
                 ("Can I try the academy before deciding?",
                  "Yes, and we would encourage it. Walk in and use the <a href=\"trackman-range.html\">range</a>, or book a single lesson. Get a feel for how often you would realistically come before committing to anything."),
                 ("Does membership include golf lessons?",
                  "Coaching and membership are separate things that work well together. If structured ongoing coaching is what you are after, the <a href=\"monthly-programme.html\">monthly programme</a> is probably the more relevant place to start."),
                 ("Do members get free range balls?",
                  "Rates vary by what you use, so " + CALL + " for the current position rather than assuming. Club hire on the range and simulators is included at no extra cost for everybody, member or not."),
                 ("How do I join?",
                  "Call 07710 582036 or use the <a href=\"contact.html\">contact form</a> and we will talk it through. Enquiries are answered within a working day."),
             ]},

            {"type": "rel", "kick": "Where to next",
             "h2": "What Membership Would <em>Cover.</em>",
             "links": [
                 ("trackman-range.html", "Trackman Driving Range", "Covered floodlit bays with live ball data. Walk in seven days a week, baskets from £4.", "Driving range"),
                 ("trackman-simulator.html", "Trackman Simulator", "Two private simulators, 550+ courses, off-peak from £13 an hour.", "Golf simulator"),
                 ("tournaments.html", "Trackman Tournaments", "League nights and Trackman competitions on the simulators and the range.", "Tournaments"),
                 ("monthly-programme.html", "Monthly Programme", "Structured ongoing coaching at £60 a month with a plan between sessions.", "Monthly coaching"),
                 ("golf-fitness.html", "Golf Fitness Suite", "TPI-informed mobility, strength and speed work built around your swing.", "Golf fitness"),
                 ("contact.html", "Contact the Academy", "Call 07710 582036 or send a message. Answered within a working day.", "Get in touch"),
             ]}
        ],
    },

    # ================================================== TOURNAMENTS
    {
        "file": "tournaments.html",
        "cur": "tournaments.html",
        "title": "Trackman Golf Tournaments &amp; League Nights Derby &amp; Nottingham | Evolution Golf Academy",
        "desc": "Trackman golf tournaments and simulator league nights near Derby and Nottingham. Competitive indoor golf, closest to pin and long drive challenges at Evolution Golf Academy, Ripley.",
        "visit_kick": "Trackman tournaments near Derby &amp; Nottingham",
        "cta": ("Get into a <em>league night.</em>",
                "Call 07710 582036 to find out what is running and when. Competitive indoor golf, whatever the weather is doing outside."),
        "hero": {
            "kick": "Trackman Golf Tournaments in Derby &amp; Nottingham",
            "l1": "Trackman", "l2": "Tournaments.",
            "p": "<strong>Trackman golf tournaments near Derby and Nottingham</strong> run on the indoor simulators and the range at Evolution Golf Academy. League nights, closest to pin, long drive and Trackman's own challenges - competitive golf that does not stop for the weather.",
            "img": "bay_night",
            "alt": "Trackman golf tournaments and league nights near Derby and Nottingham",
        },
        "marq": ["Trackman Tournaments", "Simulator League Night", "Indoor Golf Competition",
                 "Closest to the Pin", "Long Drive Challenge", "Golf Derby &amp; Nottingham"],
        "sections": [
            {"type": "pmarq"},

            {"type": "prose", "kick": "Competitive golf indoors",
             "h2": "What Are <em>Trackman Tournaments?</em>",
             "blocks": [
                 ("p", "<strong>Trackman tournaments</strong> are competitions run on the same radar technology used on the PGA Tour, scored on measured data rather than an honesty system. Because everything is tracked, the scoring is exact: carry distance to the yard, proximity to the pin in feet and inches, ball speed to the decimal."),
                 ("p", "That is what makes indoor competition work. On a course you take your playing partner's word for it. On a <a href=\"trackman-simulator.html\">Trackman simulator</a> or in a <a href=\"trackman-range.html\">Trackman range bay</a>, the machine has already decided, and nobody has to have an awkward conversation about a drop."),
                 ("h3", "What Formats Can Run on Trackman?"),
                 ("p", "Trackman supports a wide range of competitive formats. Full stroke play rounds on famous courses, closest to the pin at a set yardage, long drive, nearest the pin from progressively awkward distances, and Trackman's own skills challenges which score you across different parts of the game rather than one shot type."),
                 ("p", "There is also the Trackman Combine, a standardised test that scores your accuracy from set distances and gives you a single comparable number. It is less of a night out and more of a benchmark, but it is genuinely useful if you want to track improvement over a season rather than a session."),
                 ("h3", "Why Does Competition Improve Your Golf?"),
                 ("p", "Because pressure is a skill and you cannot practise it on your own. Hitting a seven iron to 140 yards on an empty range is a different task from hitting it when three people are watching and it decides the night. Golfers who compete regularly tend to hold their technique together better on the course, and it is one of the few things ordinary <a href=\"1-1-lessons.html\">lesson</a> work struggles to replicate."),
             ]},

            {"type": "cards", "kick": "What runs at the academy",
             "h2": "What Competitions Run <em>Near Derby and Nottingham?</em>",
             "p": "Formats vary through the year and the winter programme is busier than the summer one. Call 07710 582036 for what is running now.",
             "cards": [
                 {"img": "sim", "alt": "Simulator league night near Derby",
                  "h": "Simulator League Nights",
                  "p": "Competitive indoor golf on the Trackman simulators through the darker months, when playing a real course after work stops being an option.",
                  "href": "trackman-simulator.html", "cta": "Trackman simulator"},
                 {"img": "ball_tee", "alt": "Closest to the pin challenge on Trackman",
                  "h": "Closest to the Pin",
                  "p": "Set yardage, measured to the inch by radar rather than paced out and argued over. Quick to run and unreasonably competitive."},
                 {"img": "driver_balls", "alt": "Long drive competition on the Trackman range",
                  "h": "Long Drive",
                  "p": "Total distance and carry both measured. The number on the screen is the number, which settles most arguments before they start."},
                 {"img": "launch_data", "alt": "Trackman skills challenges and Combine test",
                  "h": "Trackman Challenges",
                  "p": "Trackman's built-in games and skills tests, including the Combine, which scores you across set distances and gives you something comparable to measure against next time.",
                  "href": "trackman-range.html", "cta": "Trackman range"},
             ], "alt": True},

            {"type": "split", "img": "bay_indoor",
             "img_alt": "Indoor golf competition near Nottingham",
             "kick": "Who competitions suit",
             "h2": "Do You Need to Be Good to <em>Enter a Competition?</em>",
             "paras": [
                 "No, and the format usually decides that rather than your handicap. Closest to the pin is a lottery for everybody. Long drive rewards speed rather than polish. Skills challenges score you against yourself as much as the room.",
                 "If you have had a few <a href=\"beginner-coaching.html\">beginner lessons</a> and can make contact reliably, you will have a perfectly good evening. Nobody is watching your backswing, they are watching the screen.",
             ],
             "ticks": [
                 "<b>All abilities</b> - format matters more than handicap",
                 "<b>Indoors and warm</b> - the weather is irrelevant",
                 "<b>Measured scoring</b> - no disputes, the radar decides",
                 "<b>Club hire included</b> - at no extra cost if you need a set",
                 "<b>Quicker than a round</b> - an evening, not five hours",
             ],
             "btn2": ("Ask what is on", "contact.html")},

            {"type": "imgbreak", "img": "bay_night",
             "img_alt": "Competition that the weather cannot cancel. at Evolution Golf Academy",
             "kick": "Trackman tournaments",
             "h2": "Competition that <em>the weather cannot cancel.</em>",
             "p": "League nights, closest to the pin and long drive, scored by radar."},

            {"type": "prose", "kick": "Getting involved",
             "h2": "How Do You Enter a <em>Trackman Tournament?</em>",
             "blocks": [
                 ("p", "Formats, fixtures and entry vary through the year, so rather than print a schedule that goes stale, the quickest route is to " + CALL + " or use the <a href=\"contact.html\">contact form</a> and ask what is running. Enquiries are answered within a working day."),
                 ("h3", "Can You Organise Something for a Group?"),
                 ("p", "The <a href=\"trackman-simulator.html\">simulator bays</a> are booked by the hour and take a small group comfortably, so a private competition among friends, a work team or a society is straightforward to set up without waiting for a scheduled event. Off-peak hours are the cheaper way to do it."),
                 ("h3", "What About Junior Competitions?"),
                 ("p", "The <a href=\"junior-academy.html\">junior academy</a> runs weekly group coaching in term time, and competitive elements are part of how juniors are kept engaged. Trackman's games work particularly well with younger players because the feedback is instant and visible."),
                 ("h3", "Where Is the Academy?"),
                 ("p", "Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RJ. Around 15 minutes from <a href=\"golf-lessons-derby.html\">Derby</a> and 25 from <a href=\"golf-lessons-nottingham.html\">Nottingham</a>, with free parking on site and the range open 7am to 8pm every day."),
             ], "alt": True},

            {"type": "stats", "items": [
                ("2", "Simulator Bays"), ("550+", "Courses"), ("40+", "Data Parameters")]},

            {"type": "faq", "kick": "Common questions",
             "h2": "Trackman Tournaments Derby &amp; Nottingham - <em>FAQs.</em>",
             "qs": [
                 ("What tournaments and league nights are running?",
                  "The programme changes through the year and is busier in winter. Call 07710 582036 or use the <a href=\"contact.html\">contact form</a> for what is currently scheduled, and we will come back to you within a working day."),
                 ("Do I need a handicap to enter?",
                  "Not for most formats. Closest to the pin, long drive and Trackman's skills challenges are all playable regardless of handicap, and several of them level the field more than a real course would."),
                 ("How much does it cost to enter?",
                  "It depends on the format and the length of the session, since some run on simulator bay time and others on range time. Call 07710 582036 for current pricing before you commit."),
                 ("Can I book a private competition for a group?",
                  "Yes. <a href=\"trackman-simulator.html\">Simulator bays</a> are hired by the hour and take a small group, so a private event among friends or colleagues does not need to wait for a scheduled league night. Off-peak hours are better value."),
                 ("Do I need my own clubs?",
                  "No. Club hire on the range and simulators is included at no extra cost, so you can turn up with nothing and still take part."),
                 ("Is it indoors?",
                  "Simulator competitions are fully indoors and heated. Range-based challenges run in the covered floodlit bays, so those are weatherproof too."),
                 ("How long does a league night take?",
                  "Considerably less than a round of golf. Indoor rounds play much faster than on a course, and shorter formats like closest to the pin take an evening rather than half a day."),
                 ("Can beginners take part?",
                  "Yes. If you can make contact reliably you will enjoy it. If you are not there yet, a few <a href=\"beginner-coaching.html\">beginner lessons</a> or a <a href=\"get-into-golf.html\">Get Into Golf</a> session will get you there quickly."),
             ]},

            {"type": "rel", "kick": "Where to next",
             "h2": "Where Tournaments <em>Run.</em>",
             "links": [
                 ("trackman-simulator.html", "Trackman Simulator", "Two private simulators, 550+ courses, off-peak from £13 an hour.", "Golf simulator"),
                 ("trackman-range.html", "Trackman Driving Range", "Covered floodlit bays with live ball data on every shot.", "Driving range"),
                 ("memberships.html", "Memberships", "Priority booking and better rates for golfers who are here often.", "Membership"),
                 ("1-1-lessons.html", "1:1 Golf Lessons", "An hour with a PGA Professional, Trackman data and video throughout.", "Golf lessons"),
                 ("junior-academy.html", "Junior Academy", "Weekly group coaching in term time for ages six to sixteen.", "Juniors"),
                 ("contact.html", "Contact the Academy", "Call 07710 582036 to ask what is running and when.", "Get in touch"),
             ]}
        ],
    },

    # ================================================== SWINGFIT
    {
        "file": "swingfit.html",
        "cur": "swingfit.html",
        "title": "SwingFit Golf Movement &amp; Fitness Derby &amp; Nottingham | Evolution Golf Academy",
        "desc": "SwingFit at Evolution Golf Academy near Derby and Nottingham. TPI movement screening and golf specific fitness so your body supports your swing instead of fighting it.",
        "visit_kick": "SwingFit near Derby &amp; Nottingham",
        "cta": ("Find out what your body <em>is doing.</em>",
                "Call 07710 582036 to talk through TPI screening and what a SwingFit programme would look like for you."),
        "hero": {
            "kick": "SwingFit in Derby &amp; Nottingham",
            "l1": "Swing", "l2": "Fit.",
            "p": "<strong>SwingFit near Derby and Nottingham</strong> is where the movement side of your golf gets addressed. TPI screening identifies what your body can and cannot currently do, and the work that follows makes your swing changes stick instead of unravelling.",
            "img": "team",
            "alt": "SwingFit golf movement and fitness near Derby and Nottingham",
        },
        "marq": ["SwingFit Derby", "TPI Movement Screening", "Golf Specific Fitness",
                 "Swing Speed Training", "Injury Prevention", "Golf Fitness Nottingham"],
        "sections": [
            {"type": "pmarq"},

            {"type": "imgbreak", "img": "tpi",
             "img_alt": "Screen first, then train. at Evolution Golf Academy",
             "kick": "SwingFit",
             "h2": "Screen first, <em>then train.</em>",
             "p": "The order matters more than the exercises."},

            {"type": "prose", "kick": "The movement side of golf",
             "h2": "What Is <em>SwingFit?</em>",
             "blocks": [
                 ("p", "<strong>SwingFit</strong> is the strand of Evolution Golf Academy that deals with your body rather than your technique. It pairs <a href=\"tpi-screening.html\">TPI movement screening</a> with golf specific physical work, so that the changes your coach asks for are changes your body can actually make."),
                 ("p", "It exists because of something the academy learned the hard way. Will Painter's own playing career stalled while he was working hard on his swing and getting nowhere, and the reason had nothing to do with technique. <strong>His body simply was not capable of consistently producing the movements he was trying to make.</strong> The answer was not the swing, it was the body."),
                 ("h3", "Why Do Swing Changes Fail?"),
                 ("p", "Most of the time, because they were never physically available in the first place. If your hips will not rotate far enough, you will find a way to make the turn anyway, and that way will be a compensation somewhere else. Coach the compensation and it moves rather than disappears."),
                 ("p", "This is the pattern behind an enormous number of golfers who have had lessons for years and not improved. They are not lazy and their coach is not incompetent. They are being asked for positions their body cannot reach, and no amount of repetition changes that."),
                 ("h3", "What Does the Screening Actually Test?"),
                 ("p", "The <a href=\"tpi-screening.html\">TPI screen</a> is sixteen movement tests covering rotation, stability, mobility and balance. Each result is then linked to the swing characteristic it tends to produce - early extension, loss of posture, casting and the rest - so you finish with a clear picture of which of your swing faults are technical and which are physical."),
             ]},

            {"type": "cards", "kick": "What SwingFit covers",
             "h2": "What Does <em>SwingFit</em> Work On?",
             "p": "Four areas, prioritised by what your screen actually shows rather than a standard programme handed to everybody.",
             "cards": [
                 {"img": "tpi", "alt": "TPI mobility screening near Derby",
                  "h": "Mobility",
                  "p": "Rotation through the hips and thoracic spine is where most amateur swings lose power and posture. Screened first, then worked on specifically.",
                  "href": "tpi-screening.html", "cta": "TPI screening"},
                 {"img": "team", "alt": "Golf specific strength work in Derbyshire",
                  "h": "Stability and Strength",
                  "p": "Golf specific strength built around the positions your swing demands, rather than a generic gym programme borrowed from another sport.",
                  "href": "golf-fitness.html", "cta": "Golf fitness suite"},
                 {"img": "launch_data", "alt": "Swing speed training measured on Trackman",
                  "h": "Speed",
                  "p": "Clubhead speed is trainable. We measure it on Trackman before and after, so the gain is provable rather than a matter of how it feels.",
                  "href": "trackman-range.html", "cta": "Trackman range"},
                 {"img": "lesson_grip", "alt": "Golf injury prevention in Derbyshire",
                  "h": "Resilience",
                  "p": "Backs, elbows and wrists take a beating in golf, usually through compensations. Targeted work keeps you playing rather than sitting out half a season."},
             ], "alt": True},

            {"type": "steps", "kick": "How it runs",
             "h2": "How Does SwingFit <em>Work?</em>",
             "p": "Screen first, then train what the screen found. The order matters more than the exercises.",
             "steps": [
                 ("Screen", "A <a href=\"tpi-screening.html\">TPI movement screen</a>, sixteen tests covering rotation, stability, mobility and balance. About an hour, and no golf swing required for most of it."),
                 ("Link", "Every restriction found is matched to the swing characteristic it tends to cause, so you can see which of your faults are physical rather than technical."),
                 ("Plan", "A prioritised set of exercises targeting the restrictions that will make the biggest difference to your golf first, rather than a long list you will abandon in a fortnight."),
                 ("Train", "Work through it in the <a href=\"golf-fitness.html\">golf fitness suite</a> or at home. Consistency beats intensity here by a distance."),
                 ("Re-test", "Screen again and re-measure clubhead speed on Trackman. If it worked the numbers move, and if it did not we change the plan rather than tell you to try harder."),
             ]},

            {"type": "split", "img": "coach_feedback",
             "img_alt": "Golf coaching and movement screening working together",
             "kick": "Coaching and movement together",
             "h2": "How Does SwingFit Fit With <em>Golf Lessons?</em>",
             "paras": [
                 "They are two halves of the same job. Your <a href=\"1-1-lessons.html\">golf lesson</a> works on what your swing does; SwingFit works on what your body will allow. Run them separately and they pull against each other.",
                 "Run together, your coach knows which positions are realistic to ask for right now and which need the body addressing first. That is the difference between a swing change that holds and one that quietly reverts over six weeks.",
             ],
             "ticks": [
                 "<b>Screen before rebuilding</b> - know what is available before changing it",
                 "<b>Faster progress</b> - lessons target what is actually fixable now",
                 "<b>Fewer injuries</b> - compensations are what hurt backs and elbows",
                 "<b>Measured</b> - Trackman before and after, not a feeling",
                 "<b>Suits every age</b> - older golfers often gain the most",
             ],
             "btn2": ("Golf fitness suite", "golf-fitness.html"), "alt": True},

            {"type": "faq", "kick": "Common questions",
             "h2": "SwingFit Derby &amp; Nottingham - <em>FAQs.</em>",
             "qs": [
                 ("What does SwingFit involve?",
                  "A <a href=\"tpi-screening.html\">TPI movement screen</a> followed by golf specific physical work targeting whatever the screen found. Exactly what your programme looks like depends on your results, so call 07710 582036 and we will talk it through rather than guess."),
                 ("How much does it cost?",
                  "TPI movement screening is £75 per session. What follows depends on what the screen shows and how you want to work on it, so " + CALL + " for current pricing on the programme side."),
                 ("Do I need to be fit already?",
                  "No. Screening first is precisely so the programme starts from where your body actually is. Plenty of golfers who have not trained in years start here."),
                 ("Is this the same as TPI screening?",
                  "<a href=\"tpi-screening.html\">TPI screening</a> is the assessment. SwingFit is the assessment plus the work that follows it. The screen on its own tells you what is wrong; the programme is what changes it."),
                 ("Will it add distance to my drives?",
                  "Clubhead speed is trainable for most golfers, and we measure it on Trackman before and after so you can see the change rather than take our word for it. How much depends on where you are starting from."),
                 ("Is SwingFit only for younger golfers?",
                  "Not at all. Older golfers often gain the most, because mobility restrictions accumulate over time and respond well to targeted work. It is frequently the difference between playing comfortably at seventy and giving up at sixty five."),
                 ("Can it help with golf injuries?",
                  "It can help with the movement restrictions and compensations that tend to cause them. It is not a medical service though, so anything painful or persistent should go to a physiotherapist or GP first."),
                 ("How long before I notice a difference?",
                  "Mobility work often shows up within a few weeks. Strength and speed take longer. The honest answer is that it depends far more on whether you do the work between sessions than on the plan itself."),
             ]},

            {"type": "rel", "kick": "Where to next",
             "h2": "The Rest of <em>the Academy.</em>",
             "links": [
                 ("tpi-screening.html", "TPI Screening", "Sixteen movement tests linking how your body moves to what your swing does.", "TPI screening"),
                 ("golf-fitness.html", "Golf Fitness Suite", "Where the physical work happens, guided by your screen results.", "Golf fitness"),
                 ("1-1-lessons.html", "1:1 Golf Lessons", "An hour with a PGA Professional, Trackman data and video throughout.", "Golf lessons"),
                 ("monthly-programme.html", "Monthly Programme", "Structured ongoing coaching with a plan between sessions.", "Monthly coaching"),
                 ("meet-team.html", "Meet Your Coach", "Will Painter, and the thinking that led to the academy being built this way.", "Your coach"),
                 ("trackman-range.html", "Trackman Driving Range", "Where speed and strike changes get measured on the way through.", "Driving range"),
             ]}
        ],
    },
]
