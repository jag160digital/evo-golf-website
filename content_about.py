"""About page - built from the client's supplied copy ONLY.

Loaded last in build.py so it overrides the earlier about.html.

Everything here comes from the copy the client sent. No invented
sections, no extra FAQ block, no accreditations band.

THREE PROBLEMS IN THE SOURCE COPY, handled as noted:

1. FACILITY 04 is headed "Trackman 4 Range Bay" but the body underneath
   it is the GOLF FITNESS SUITE ("Move better, play better. TPI
   screening and golf specific fitness..."). Used Golf Fitness Suite,
   since that matches the body copy, the footer and every other page.

2. "Get into Golf" carries the Ladies Coaching description verbatim
   ("Friendly women-only golf lessons"). That is a copy-paste error -
   Get Into Golf is not women-only. Written a short accurate line
   instead rather than publish something that would turn men away.

3. The address block says "Mon to Sun 7:00am to 8:00pm" and the visit
   section a few lines later says "open to the public from 8am to 10pm
   with a rolling bar". Both are in the same supplied copy. Kept 7am to
   8pm, which matches every other page and the schema, and dropped the
   conflicting sentence rather than print two sets of opening hours on
   one page and have somebody turn up at half nine to a locked door.

Also: the stat block shows zeros because they are count-up animations.
Real values used. "Open every single day" is 13 hrs on a 7am-8pm day;
an earlier read of the live page showed 14, which only works on the
8am-10pm figure. Flagged with the hours conflict above.

>>> ACTION FOR THE CLIENT: confirm 1, 2 and 3. <<<
"""

PAGES = [{
    "file": "about.html",
    "cur": "about.html",
    "title": "About Evolution Golf Academy | Golf Academy in Derby &amp; Nottingham",
    "desc": "About Evolution Golf Academy, a modern golf academy for Derby and Nottingham at Ormonde Fields Golf Club, Codnor near Ripley. Founded by Academy Director Will Painter.",
    "visit_kick": "pga golf coach in derby and nottingham",
    "faccar": False,
    "cta": ("Come and <em>see what we do.</em>",
            "Pop in, hit some balls, meet the team and have a proper look round. No pressure and no hard sell, we just love showing golfers from Derby and Nottingham what we have built."),
    "hero": {
        "kick": "About · Golf Academy in Derby &amp; Nottingham",
        "l1": "The golf academy", "l2": "built around you.",
        "p": "Based at Ormonde Fields Golf Club in Codnor near Ripley, <strong>Evolution is a modern golf academy for Derby and Nottingham</strong>. Practice with purpose, learn with clarity and play for fun. We are open to the public and welcome golfers of all ages and abilities.",
        "img": "team",
        "alt": "Evolution Golf Academy, a modern golf academy for Derby and Nottingham",
    },
    "marq": ["Golf Academy Derby", "Golf Academy Nottingham", "Advanced PGA Professional",
             "TPI Movement Screening", "3D Trackman Swing Analysis", "Codnor, Ripley"],
    "sections": [
            {"type": "stats", "items": [
            ("2023", "The year we were founded"),
            ("15 yrs", "Playing at an elite level"),
            ("13 hrs", "Open every single day"),
            ("7", "Days a week on the range")]},

            {"type": "split", "img": "lesson_grip",
         "img_alt": "Man in a green sweater and PING hat swinging a golf club indoors at a wooden driving range",
         "kick": "Our story · Golf coaching in Derbyshire",
         "h2": "Founded by <em>Academy Director Will Painter</em>",
         "paras": [
             "Evolution Golf Academy was built around one simple belief: <strong>practice should lead to improvement</strong>. Founder Will Painter knows how frustrating it is to spend hours practising, taking lessons and searching for answers, only to find yourself making the same mistakes time and time again.",
             "As an aspiring professional golfer, Will dedicated his life to the game. Along the journey he proudly represented England Golf and won multiple professional events, but like every golfer, he also experienced periods where improvement felt impossible. No matter how much he practised or how many lessons he had, lasting change never seemed to happen.",
         ],
         "ticks": [
             "Represented England Golf.",
             "Multiple professional wins.",
             "15 years playing at an elite level.",
         ],
         "btn2": ("Meet the team", "meet-team.html"), "alt": True},

            {"type": "split", "img": "bunker",
         "img_alt": "Golf instructor teaching woman how to hold a golf club on a sand bunker with ball in front",
         "kick": "The turning point",
         "h2": "The answer wasn't the swing, <em>it was the body.</em>",
         "paras": [
             "Everything changed when he began working with Advanced PGA Professional Graham Walker alongside biomechanics specialist Mark Bull and a team of fitness professionals. Rather than focusing only on the golf swing, they first assessed how Will's body moved. The answer became clear. <strong>His body simply wasn't capable of consistently producing the movements he was trying to make.</strong>",
             "By improving his mobility, stability and movement quality through a structured fitness programme, alongside regular coaching and biomechanics assessments, something clicked. His body began supporting the technical changes instead of fighting against them. Practice became more productive, improvement became measurable and lasting swing changes finally became achievable. That experience became the foundation of Evolution Golf Academy.",
         ],
         "ticks": [
             "Advanced PGA Professional Coaching",
             "3D Trackman Swing Analysis",
             "<a href=\"tpi-screening.html\">TPI Movement Screening</a>",
             "<a href=\"golf-fitness.html\">Fitness Professionals</a>",
         ],
         "btn2": ("Book a lesson with Will", "contact.html")},

            {"type": "imgbreak", "img": "trackman_screen",
         "img_alt": "Trackman launch monitor screen during a golf swing assessment in Derbyshire",
         "kick": "How we can help you improve",
         "h2": "We assess, identify, then <em>build the plan.</em>",
         "p": "Rather than guessing why you are struggling, every journey starts with a PGA Professional Swing Assessment and a TPI Movement Screen."},

            {"type": "prose", "kick": "golf facilities in derby and nottingham",
         "h2": "How we can help you <em>improve</em>",
         "p": "Every golfer is different, which is why every journey at Evolution begins with understanding both your golf swing and how your body moves. Rather than guessing why you are struggling, we assess, identify and build a clear plan for improvement.",
         "blocks": [
             ("h3", "Step 1 · PGA Professional Golf Swing Assessment"),
             ("p", "Your journey begins with a comprehensive <strong>golf swing assessment</strong> with one of our Advanced PGA Professionals. Using TrackMan technology, video analysis, 3D data and our coaching experience, we assess how you currently move the golf club, how the golf ball behaves and, most importantly, what is preventing you from reaching your goals."),
             ("p", "During your Golf Swing Assessment, we'll identify:"),
             ("ul", ["Your current ball flight tendencies",
                     "The swing characteristics limiting your performance",
                     "Your biggest opportunities for improvement",
                     "Whether your current swing matches your goals",
                     "Whether the limitations appear to be technical, physical or a combination of both"]),
             ("p", "This gives us a clear understanding of your golf swing and provides the foundation for the next stage of your assessment. See <a href=\"1-1-lessons.html\">1:1 golf lessons</a> for how the coaching that follows works."),
             ("h3", "Step 2 · TPI Movement Screen"),
             ("p", "Your golf swing is only part of the picture. To create lasting improvement, your body must be capable of producing the movements your coach is asking you to make. Our <a href=\"tpi-screening.html\">TPI Movement Screen</a> assesses your mobility, stability, balance and overall movement quality to identify any physical limitations that could be affecting your golf swing or preventing long-term improvement."),
             ("p", "During your TPI Movement Screen, we'll identify:"),
             ("ul", ["Any mobility or stability restrictions affecting your swing",
                     "Movement patterns limiting your performance",
                     "Physical limitations that may be preventing swing changes",
                     "Areas that could increase power, consistency and efficiency",
                     "Whether further support from a fitness professional or physiotherapist would benefit your development"]),
             ("p", "By combining your PGA Professional Swing Assessment with your TPI Movement Screen, we build a complete understanding of both your golf swing and your body's ability to support it."),
         ], "alt": True},

            {"type": "cards", "kick": "golf facilities in derby and nottingham",
         "h2": "Your <em>Evolution Plan.</em>",
         "p": "Following your PGA Professional Swing Assessment and TPI Movement Screen, we'll create a personalised plan designed around your goals, your golf swing and how your body moves. Every golfer is different, which means every Evolution Plan is unique. Depending on your assessment, your plan may include one or more of the following services.",
         "cards": [
             {"img": "over_shoulder", "alt": "Advanced PGA Professional coaching in Derby and Nottingham",
              "h": "Plan 1 · Advanced PGA Professional Coaching",
              "p": "Build lasting improvement through structured coaching with an Advanced PGA Professional, regular reviews and a clear pathway to achieving your golfing goals.",
              "href": "1-1-lessons.html", "cta": "Explore more"},
             {"img": "tpi", "alt": "TPI golf movement programme in Derbyshire",
              "h": "Plan 2 · TPI Golf Movement Programme",
              "p": "Improve your mobility, stability and movement quality with golf-specific exercises designed to help your body support lasting swing changes.",
              "href": "swingfit.html", "cta": "Explore more"},
             {"img": "team", "alt": "Golf specific strength and conditioning near Nottingham",
              "h": "Plan 3 · Strength &amp; Conditioning",
              "p": "Develop strength, power and resilience through golf-specific training to improve performance and reduce the risk of injury.",
              "href": "golf-fitness.html", "cta": "Explore more"},
             {"img": "coach_feedback", "alt": "Physiotherapy support for golfers in Derbyshire",
              "h": "Plan 4 · Physiotherapy",
              "p": "Assess and treat pain, injuries and movement restrictions that may be limiting your golf, helping you move and perform with greater confidence.",
              "href": "contact.html", "cta": "Explore more"},
         ]},

            {"type": "gal", "kick": "Inside the academy",
         "h2": "A look around <em>Evolution.</em>",
         "items": [
             ("bay_night", "Floodlit Trackman bays"),
             ("putting", "Short game and putting"),
             ("fitting_data", "Trackman data review"),
             ("student_swing", "Grass driving range"),
             ("impact", "Custom fitting detail"),
             ("on_course", "On-course coaching"),
         ], "alt": True},

            {"type": "cards", "kick": "What's inside · Facilities in Derby &amp; Nottingham",
         "h2": "One golf academy,<br><em>six ways to play.</em>",
         "cards": [
             {"img": "range_night", "alt": "Trackman driving range in Derby and Nottingham",
              "h": "Facility 01 · Trackman Driving Range",
              "p": "Heated TrackMan bays with live ball data on every shot. Warm up, work on your swing or just hit a few balls, whatever the weather.",
              "href": "trackman-range.html", "cta": "TrackMan Range"},
             {"img": "sim", "alt": "Trackman simulator near Derby and Nottingham",
              "h": "Facility 02 · Trackman Simulator",
              "p": "Play famous courses, practise in the dry or join a league night. Indoor TrackMan simulators, booked by the hour.",
              "href": "trackman-simulator.html", "cta": "TrackMan Simulator"},
             {"img": "bay_screen", "alt": "Trackman teaching bay at Evolution Golf Academy",
              "h": "Facility 03 · Trackman Teaching Bay",
              "p": "Where the real improving happens. One to one golf lessons with full TrackMan data and video swing analysis.",
              "href": "trackman-teaching-bay.html", "cta": "Teaching Bay"},
             {"img": "team", "alt": "Golf fitness suite in Derbyshire",
              "h": "Facility 04 · Golf Fitness Suite",
              "p": "Move better, play better. TPI screening and golf specific fitness so your body supports your swing instead of fighting it.",
              "href": "golf-fitness.html", "cta": "Fitness Suite"},
             {"img": "student_swing", "alt": "Grass driving range in Ripley, Derbyshire",
              "h": "Facility 05 · Grass Driving Range",
              "p": "Hit off real turf and shape proper shots. An outdoor grass driving range for practice that feels like the course.",
              "href": "grass-range.html", "cta": "Driving Range"},
             {"img": "putting", "alt": "Short game area and putting green in Derbyshire",
              "h": "Facility 06 · Short Game Area",
              "p": "Sharpen the part of the game that saves the most shots. A short game area and putting green for chipping, pitching and putting.",
              "href": "short-game.html", "cta": "Short Game Area"},
         ]},

            {"type": "cards", "kick": "Golf lessons, Trackman &amp; custom fitting",
         "h2": "Beginner coaching services in <em>Derby.</em>",
         "p": "At Evolution, we believe golf should be accessible, enjoyable and welcoming for everyone. Whether you are picking up a golf club for the very first time, returning to the game after a break or introducing your child to golf, our programmes are designed to build confidence, develop skills and help you enjoy the game from day one. Explore our beginner-friendly programmes below and discover the best place to start your golfing journey.",
         "cards": [
             {"img": "ball_tee", "alt": "Golf club poised to hit a golf ball on grass with a green basket holding more balls nearby",
              "h": "Beginner Coaching",
              "p": "Just you and a PGA pro for an hour. We'll look at your Trackman numbers, film your swing, and send you off with a clear, simple plan.",
              "href": "beginner-coaching.html", "cta": "Learn more"},
             {"img": "junior", "alt": "Young golfer practicing a swing on an indoor tee at night with golf balls and targets ahead",
              "h": "Junior Coaching",
              "p": "A proper start, full of fun. Friendly group golf lessons for ages 6 to 16, clubs provided, every week in term time.",
              "href": "junior-academy.html", "cta": "Learn more"},
             {"img": "bunker", "alt": "Golf instructor teaching woman how to hold a golf club on a sand bunker with ball in front",
              "h": "Ladies Coaching",
              "p": "A relaxed, welcoming space to learn. Friendly women-only golf lessons, from complete first-timers to club golfers.",
              "href": "ladies-academy.html", "cta": "Learn more"},
             {"img": "on_course", "alt": "Man in navy golf jacket holding up a golf club, explaining stance to another person wearing a glove",
              "h": "Get into Golf",
              "p": "A relaxed, welcoming way in for anyone who has never played. Clubs provided, no experience needed and nobody expecting you to know anything.",
              "href": "get-into-golf.html", "cta": "Learn more"},
         ], "alt": True}
        ],
}]
