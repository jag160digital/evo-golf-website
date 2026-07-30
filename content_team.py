"""Meet the Team and the main FAQ hub.

Content taken from the live Webflow pages:
  /coaching/golf-coach-derby-nottingham
  /frequently-asked-questions

Loaded last in build.py so these override any earlier definition.

FACTS LOCKED IN HERE (corrected against the live site):
  - Will Painter is an ADVANCED PGA Professional and the only coach
  - membership EXISTS - it is not required, but it gives priority
    booking and better rates
  - club hire on the range and simulators is included at no extra cost
  - fittings are brand neutral
  - enquiries answered within a working day
"""

WILL_BIO = (
    "Will combines over <strong>10 years experience of golf coaching</strong> with Trackman technology and "
    "Titleist Performance certification to understand your golf swing and your body, so he can build a "
    "personalised pathway to better golf. With a background of pursuing a career in tournament golf, his "
    "constant pursuit to better his own game and find the answers has shaped how he coaches, and the passion "
    "to help all ages and abilities improve across Derby and Nottingham. Will has represented England Golf, "
    "has multiple professional wins and spent fifteen years playing at an elite level, and he founded "
    "Evolution Golf Academy in 2023."
)

PAGES = [

    # ============================================== MEET THE TEAM
    {
        "file": "meet-team.html",
        "cur": "meet-team.html",
        "title": "Golf Coach in Derby &amp; Nottingham | Advanced PGA Professional | Evolution Golf Academy",
        "desc": "Meet your golf coach in Derby and Nottingham. Will Painter, Advanced PGA Professional, coaching with Trackman data, TPI screening and fitness support at Evolution Golf Academy, Ripley.",
        "visit_kick": "Meet your golf coach near Derby &amp; Nottingham",
        "cta": ("Book a lesson with <em>Will.</em>",
                "One lesson, no commitment. Advanced PGA Professional coaching with Trackman data and video on every session."),
        "hero": {
            "kick": "Golf Coach in Derby &amp; Nottingham",
            "l1": "Meet the", "l2": "Team.",
            "p": "Your <strong>golf coach in Derby and Nottingham</strong> is Will Painter, an Advanced PGA Professional based at Evolution Golf Academy in Codnor, Ripley. Coaching built on Trackman data, TPI movement principles and fitness support, so change actually lasts.",
            "img": "coach_feedback",
            "alt": "Will Painter, Advanced PGA Professional golf coach in Derby and Nottingham",
        },
        "marq": ["Golf Coach Derby", "Advanced PGA Professional", "Golf Coach Nottingham",
                 "TPI Certified Coaching", "Trackman Experts", "Golf Coaching Derbyshire"],
        "sections": [
            {"type": "pmarq"},

            {"type": "prose", "kick": "Why the academy exists",
             "h2": "What Makes a Good <em>Golf Coach?</em>",
             "blocks": [
                 ("p", "Evolution was started with one goal: to help golfers understand <strong>why they do what they do</strong> within their golf performance, and to offer support that helps them play better golf. That sounds simple and almost nobody does it. Most coaching tells you what to change without ever explaining what caused the fault in the first place."),
                 ("p", "We find the problem and let you understand why it happens. That means combining Advanced PGA Professional coaching, TPI certified principles, Trackman expertise and fitness support to assess what is going on, give you the answers, and then help you make the change stick."),
                 ("h3", "Why Does Understanding the Cause Matter?"),
                 ("p", "Because a swing fault you do not understand comes back. If your hips cannot rotate and nobody tells you, you will keep being asked for a position your body physically cannot reach, and you will keep failing to reach it. Screening how you move before rebuilding how you swing is what separates coaching that lasts from coaching that lasts a fortnight. That is the thinking behind <a href=\"tpi-screening.html\">TPI screening</a> and the <a href=\"golf-fitness.html\">golf fitness suite</a>."),
                 ("h3", "What Does Trackman Add to a Golf Lesson?"),
                 ("p", "Measurement. Trackman is the dual-radar launch monitor used on the PGA Tour, and every bay here has it. When your coach changes something, you both watch ball speed, spin, launch angle, carry and club path either move or fail to. A <a href=\"1-1-lessons.html\">golf lesson</a> stops being a matter of opinion and becomes a matter of evidence."),
             ]},

            {"type": "team", "kick": "Your coach",
             "h2": "Your Golf Coach in <em>Derby and Nottingham.</em>",
             "p": "Coaching at Evolution is led by one Advanced PGA Professional, supported by TPI movement screening and fitness professionals.",
             "people": [
                 {"img": "coach_feedback", "name": "Will Painter",
                  "role": "PGA Professional · TPI Certified · Trackman Expert", "bio": WILL_BIO},
             ], "alt": True},

            {"type": "imgbreak", "img": "coach_feedback",
             "img_alt": "Coaching built around you. at Evolution Golf Academy",
             "kick": "Your coach",
             "h2": "Coaching built <em>around you.</em>",
             "p": "Every session shaped by your body, your goals and what the numbers actually say."},

            {"type": "prose", "kick": "How Will coaches",
             "h2": "What Makes His Coaching <em>Different?</em>",
             "blocks": [
                 ("p", "Not all golf coaches are the same. Some hand you a few swing tips and send you on your way, or try to force you into a generic swing model that does not suit your body or how you play. Will takes a different approach. <strong>Every session is built around you</strong>, your body, your mind and your lifestyle."),
                 ("p", "He looks for the root cause behind the issues in your game, so a few simple changes can fix several problems at once. With a background in sports science and years coaching golfers of every level, Will knows every golfer is different. That is exactly why he tailors his coaching to you."),
                 ("h3", "The Turning Point Behind the Academy"),
                 ("p", "Evolution exists because of a problem Will hit in his own game. He was working hard on his swing and it was not sticking, and the reason turned out to have nothing to do with technique: <strong>his body simply was not capable of consistently producing the movements he was trying to make</strong>."),
                 ("p", "The answer was not the swing, it was the body. Improving mobility, stability and movement quality alongside the coaching is what finally moved his game, and it is why every golfer here gets <a href=\"tpi-screening.html\">TPI movement screening</a> and access to the <a href=\"golf-fitness.html\">golf fitness suite</a> rather than technique work in isolation."),
             ]},

            {"type": "cards", "kick": "Credentials",
             "h2": "What Qualifications Does Your <em>Golf Coach Hold?</em>",
             "cards": [
                 {"img": "over_shoulder", "alt": "PGA Professional golf coaching in Derbyshire",
                  "h": "PGA Professional",
                  "p": "Extensive coaching experience across every level of golfer, from people who have never held a club through to players competing seriously."},
                 {"img": "tpi", "alt": "TPI certified golf coach near Nottingham",
                  "h": "TPI Certified",
                  "p": "A swing that works for your body, not a textbook. TPI certification is what makes it possible to screen movement and coach around what your body can actually do.",
                  "href": "tpi-screening.html", "cta": "TPI screening"},
                 {"img": "launch_data", "alt": "Trackman data specialist golf coach",
                  "h": "Trackman Data Specialist",
                  "p": "Every change backed by real numbers. Ball speed, spin, launch, carry and club path measured on every shot rather than estimated by eye.",
                  "href": "trackman-range.html", "cta": "Trackman range"},
                 {"img": "coach_feedback", "alt": "OnForm golf coaching app support",
                  "h": "OnForm Coaching",
                  "p": "Keep improving between lessons, not just during them. Swing videos and feedback carry on through the OnForm platform once you leave the bay.",
                  "href": "monthly-programme.html", "cta": "Monthly programme"},
             ], "alt": True},

            {"type": "cards", "kick": "How the academy assesses your game",
             "h2": "How Do You Coach Golfers in <em>Derby and Nottingham?</em>",
             "p": "Three things working together, rather than a lesson in isolation.",
             "cards": [
                 {"img": "over_shoulder", "alt": "Advanced PGA Professional golf coaching in Derbyshire",
                  "h": "01 · Advanced PGA Coaching",
                  "p": "Accredited PGA coaching with years of experience across every level of golfer, from total beginners through to professionals. Advanced status means further qualification beyond standard PGA accreditation.",
                  "href": "1-1-lessons.html", "cta": "Golf lessons"},
                 {"img": "tpi", "alt": "TPI certified movement screening near Nottingham",
                  "h": "02 · TPI Certification",
                  "p": "TPI principles let us screen and understand your body, so the coaching decisions we make are the right ones for how you actually move rather than how we wish you moved.",
                  "href": "tpi-screening.html", "cta": "TPI screening"},
                 {"img": "team", "alt": "Golf fitness professionals in Derbyshire",
                  "h": "03 · Fitness Professionals",
                  "p": "Fitness support helps golfers become fitter and more coachable, which makes change not just possible but considerably easier to hold on to between sessions.",
                  "href": "golf-fitness.html", "cta": "Golf fitness"},
                 {"img": "launch_data", "alt": "Trackman launch monitor expertise",
                  "h": "04 · Trackman Experts",
                  "p": "Trackman on every bay, read by someone who knows what the numbers mean. Data on its own is noise. Data plus an Advanced PGA Professional is a plan.",
                  "href": "trackman-range.html", "cta": "Trackman range"},
             ]},

            {"type": "split", "img": "lesson_grip",
             "img_alt": "Golf lesson with an Advanced PGA Professional near Derby",
             "kick": "What a lesson is actually like",
             "h2": "What Happens in a Lesson With <em>Your Coach?</em>",
             "paras": [
                 "No jargon and no lecture. Will will ask what you want from your golf before touching your swing, because coaching a golfer chasing a first round is a different job from coaching one chasing a handicap cut.",
                 "From there it is <strong>Trackman data and video on every shot</strong>, so you can see what your swing is doing rather than take somebody's word for it. You leave with your swing videos and a simple plan you can actually work on.",
             ],
             "ticks": [
                 "<b>Goals first</b> - the plan follows what you want, not a template",
                 "<b>Trackman on every shot</b> - <a href=\"trackman-range.html\">measured</a>, not guessed",
                 "<b>Video you keep</b> - review the session at home afterwards",
                 "<b>Plain English</b> - no jargon, and the reasoning explained",
                 "<b>Clubs available</b> - lent for lessons, and <a href=\"beginner-coaching.html\">beginners</a> need bring nothing",
             ],
             "btn2": ("See lesson prices", "1-1-lessons.html"), "alt": True},

            {"type": "steps", "kick": "Booking",
             "h2": "How Do You Book a Lesson With <em>Will?</em>",
             "p": "Straightforward, and you are not committing to a programme by booking one session.",
             "steps": [
                 ("Get in touch", "Book online, call 07710 582036 or use the <a href=\"contact.html\">contact form</a>. Enquiries are answered within a working day."),
                 ("Tell us your goal", "Whether that is getting round a course for the first time, fixing a slice or breaking a handicap barrier. It changes how the first session is structured."),
                 ("Your first session", "An hour with Trackman running and video recording. Will works out what is actually happening before deciding what to change."),
                 ("Leave with a plan", "Your swing videos and a simple set of things to work on. Not fifteen swing thoughts, which is how golfers get worse."),
                 ("Keep it going", "Practise on the <a href=\"trackman-range.html\">Trackman range</a> between sessions, or move onto the <a href=\"monthly-programme.html\">monthly programme</a> for structured ongoing coaching."),
             ]},

            {"type": "tgrid", "kick": "Reviews",
             "h2": "What Golfers Say About Coaching <em>at Evolution.</em>",
             "items": [
                 ("I had a lesson with Will. He was attentive and planned an approach to how I could improve. After some practice the planned improvements paid off. Highly recommended.", "Ian L."),
                 ("Golf coaching with Will was a great experience. He helped progress my game using their Trackman technology and the driving range facilities to practice what I had been taught.", "Irene B."),
                 ("Will gave me good advice and made adjustments to my swing. Huge improvement in just one lesson, best £50 I have ever spent.", "Reece F."),
             ], "alt": True},

            {"type": "rel", "kick": "Where to next",
             "h2": "Coaching Options at <em>the Academy.</em>",
             "links": [
                 ("1-1-lessons.html", "1:1 Golf Lessons", "One to one coaching with Trackman data and video analysis throughout.", "Golf lessons"),
                 ("beginner-coaching.html", "Beginner Coaching", "No experience needed and clubs provided. The starting point for brand new golfers.", "Beginners"),
                 ("monthly-programme.html", "Monthly Programme", "Structured ongoing coaching with a plan between sessions.", "Monthly"),
                 ("junior-academy.html", "Junior Academy", "Coaching for ages six to sixteen, with group sessions and holiday camps.", "Juniors"),
                 ("ladies-academy.html", "Ladies Academy", "Coaching for women of all abilities, from complete beginners upwards.", "Ladies golf"),
                 ("tpi-screening.html", "TPI Screening", "A movement screen linking how your body moves to what your swing does.", "TPI screening"),
             ]},

            {"type": "faq", "kick": "Common questions",
             "h2": "Golf Coach Derby &amp; Nottingham - <em>FAQs.</em>",
             "qs": [
                 ("Who will coach me at Evolution Golf Academy?",
                  "Will Painter, Advanced PGA Professional. Coaching is supported by TPI movement screening and fitness professionals, so if your swing problem turns out to be physical rather than technical it gets addressed properly rather than coached around."),
                 ("What is an Advanced PGA Professional?",
                  "It is the qualification level above standard PGA Professional, reached through further study and assessed coaching practice. Every PGA Professional is qualified to coach; Advanced status reflects additional depth on top of that."),
                 ("Do you coach complete beginners?",
                  "Yes, regularly. <a href=\"beginner-coaching.html\">Beginner coaching</a> and <a href=\"get-into-golf.html\">Get Into Golf</a> both assume no experience at all, and clubs are lent for lessons so there is nothing to buy first."),
                 ("Do you coach low handicap golfers as well?",
                  "Yes. The same Trackman data that helps a beginner find the middle of the face is what a single-figure golfer uses to tighten dispersion and control spin. Advanced PGA coaching covers both ends comfortably."),
                 ("How long is a golf lesson?",
                  "A standard one to one lesson lasts an hour. You look at your Trackman data, review video of your swing, and leave with a simple plan to work on between sessions."),
                 ("Do I need my own golf clubs?",
                  "No. Clubs can be lent for lessons, and club hire on the <a href=\"trackman-range.html\">range</a> and <a href=\"trackman-simulator.html\">simulators</a> is included at no extra cost. Just bring clothes you can move in."),
                 ("Do I need to be a member to book a lesson?",
                  "No. Lessons, range time and the simulators are open to everyone. Membership is optional and simply gives priority booking and better rates."),
                 ("How quickly will you reply to an enquiry?",
                  "Within a working day. If you would rather not wait, call 07710 582036 and you can usually get booked in there and then."),
                 ("Where are you based?",
                  "Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RJ. Around 20 minutes from <a href=\"golf-lessons-derby.html\">Derby</a> and 25 from <a href=\"golf-lessons-nottingham.html\">Nottingham</a>, with free parking on site."),
             ], "alt": True}
        ],
    },

    # ============================================== FAQ HUB
    {
        "file": "faqs.html",
        "cur": "faqs.html",
        "title": "Golf Questions and Answers | FAQs | Evolution Golf Academy Derby &amp; Nottingham",
        "desc": "Golf lesson FAQs for Derby and Nottingham. Lessons, prices, membership, the Trackman range, simulators, custom fitting and TPI screening at Evolution Golf Academy, Ripley.",
        "visit_kick": "Golf academy near Derby &amp; Nottingham",
        "cta": ("Still not sure? <em>Just ask.</em>",
                "Call 07710 582036 or drop us a line. We answer within a working day, seven days a week."),
        "hero": {
            "kick": "Golf Questions and Answers - Derby &amp; Nottingham",
            "l1": "Frequently asked,", "l2": "frankly answered.",
            "p": "The questions we get most often about <strong>golf lessons in Derby and Nottingham</strong> - coaching, prices, membership, the Trackman range, simulators, custom fitting and TPI screening. Cannot find yours? Drop us a line, we answer within a working day.",
            "img": "bay_night",
            "alt": "Golf questions and answers at Evolution Golf Academy near Derby and Nottingham",
        },
        "marq": ["Golf Lesson Questions", "Golf Lesson Prices", "Trackman Range FAQs",
                 "Custom Fitting Questions", "Golf Academy Derby", "Golf Academy Nottingham"],
        "sections": [

            {"type": "faq", "kick": "01 · Golf lessons",
             "h2": "Golf Lessons in <em>Derby and Nottingham.</em>",
             "qs": [
                 ("What golf lessons do you offer?",
                  "One to one golf lessons, <a href=\"monthly-programme.html\">monthly coaching programmes</a>, <a href=\"junior-academy.html\">junior golf coaching</a> and <a href=\"ladies-academy.html\">ladies golf coaching</a>. Every lesson is tailored to you, your swing, your goals and your handicap, whether you have never played or you are chasing scratch."),
                 ("I have never played golf before, is this the right place?",
                  "Definitely. <a href=\"get-into-golf.html\">Get Into Golf</a> and ladies coaching sessions are built for complete beginners, with clubs provided and no experience needed. Plenty of our golfers in Derby and Nottingham started here without ever having swung a club."),
                 ("How long does a golf lesson take?",
                  "A standard one to one golf lesson lasts an hour. You will look at your Trackman data, review video of your swing, and leave with a simple plan to work on."),
                 ("Do I need my own clubs?",
                  "No. We can lend you a set for lessons, and the range and simulators include club hire at no extra cost. Just bring clothes you can move in."),
                 ("Who will be coaching me?",
                  "Will Painter, Advanced PGA Professional. Coaching is backed by TPI movement principles and fitness support, so physical restrictions get identified rather than coached around. See <a href=\"meet-team.html\">meet the team</a>."),
                 ("How much do golf lessons cost?",
                  "A one to one lesson with an Advanced PGA Professional is £55 for the hour, and the <a href=\"monthly-programme.html\">monthly coaching programme</a> is £60 per month. <a href=\"tpi-screening.html\">TPI screening</a> is £75. Call 07710 582036 to confirm current prices."),
                 ("How often should I have a lesson?",
                  "It depends how much you practise between them. Weekly or fortnightly works well while you are changing something significant; monthly is fine for maintenance. The <a href=\"monthly-programme.html\">monthly programme</a> exists because regular structured coaching beats occasional one-offs."),
             ]},

            {"type": "faq", "kick": "02 · Facilities", "alt": True,
             "h2": "Our Facilities in <em>Codnor, Ripley.</em>",
             "qs": [
                 ("What facilities do you have?",
                  "A <a href=\"trackman-range.html\">Trackman range</a>, indoor <a href=\"trackman-simulator.html\">Trackman simulators</a>, a <a href=\"trackman-teaching-bay.html\">Trackman teaching bay</a>, a <a href=\"golf-fitness.html\">golf fitness suite</a>, a <a href=\"grass-range.html\">grass driving range</a> and a <a href=\"short-game.html\">short game area</a>, all on one site in Codnor near Ripley."),
                 ("Do I need to be a member to book?",
                  "No. Anyone can book golf lessons, the range or the simulators. Membership simply gives you priority booking and better rates, but everything is open to the public."),
                 ("Can I just turn up and hit balls?",
                  "Yes. The range and simulators welcome drop-ins whenever we are open. Coaching, custom fitting and TPI screening are by appointment so we can give you our full attention."),
                 ("What are your opening hours?",
                  "Seven days a week, 7am to 8pm, with no regular closing day. The range bays are floodlit, so the later slots work through the winter as well as the summer."),
                 ("Is the range open in winter?",
                  "Yes. The bays are covered and floodlit, so the <a href=\"trackman-range.html\">Trackman range</a> runs the same in December as it does in June. The <a href=\"grass-range.html\">grass range</a> is the seasonal one, since it depends on ground conditions."),
                 ("Is there parking?",
                  "Yes, free parking on site at Ormonde Fields Golf Club, directly outside the range and teaching studio, so you park and walk straight to your bay."),
             ]},

            {"type": "faq", "kick": "03 · Fitting and technology",
             "h2": "Custom Fitting &amp; <em>Technology.</em>",
             "qs": [
                 ("Do you offer custom fitting?",
                  "Yes. Our custom fitting suite uses the latest Trackman technology so every iron, wedge and driver matches your swing. Our fitters will help you find the right equipment for your game."),
                 ("Do I have to buy what I get fitted for?",
                  "No. Fittings are brand neutral, so you can buy from us or anywhere you like. The fitting itself is always worth doing."),
                 ("What is TPI screening?",
                  "<a href=\"tpi-screening.html\">TPI screening</a> is a simple set of movement tests that show how your body affects your golf swing. It helps us coach a swing that works for your body rather than against it."),
                 ("What does Trackman actually measure?",
                  "Ball speed, club head speed, smash factor, launch angle, spin rate, carry distance, total distance, shot shape, club path and face angle. All of it appears live in your bay within about a second of impact."),
                 ("How long does a club fitting take?",
                  "A full bag fitting typically runs ninety minutes to two hours. A single club fitting, driver only or irons only, is usually around an hour."),
                 ("Is custom fitting worth it for a higher handicapper?",
                  "Often more than for a low handicapper. Better players adapt to poor equipment, while higher handicappers tend to build compensations around it. Getting lie angle and shaft flex right removes a variable you would otherwise fight every round."),
             ]},

            {"type": "faq", "kick": "04 · Booking and visiting", "alt": True,
             "h2": "Booking, Hours &amp; <em>Visiting.</em>",
             "qs": [
                 ("How do I book?",
                  "Book online, call 07710 582036, or send a message through the <a href=\"contact.html\">contact page</a>. Lessons, simulator bays, fitting and TPI screening all need booking; the range does not."),
                 ("How quickly do you reply to enquiries?",
                  "Within a working day. If you want an answer faster than that, calling 07710 582036 is the quickest route and you can usually get booked in on the spot."),
                 ("How far are you from Derby?",
                  "Around 20 minutes via the A610. Full directions from each part of the city are on the <a href=\"golf-lessons-derby.html\">golf lessons in Derby</a> page."),
                 ("How far are you from Nottingham?",
                  "Around 25 minutes on the A610 through Eastwood. See <a href=\"golf-lessons-nottingham.html\">golf lessons in Nottingham</a> for route by route directions."),
                 ("What should I wear?",
                  "Clothes you can move in and flat shoes. There is no dress code to decode here, and you do not need golf shoes for the range, the simulators or a lesson."),
                 ("Can I buy a lesson as a gift?",
                  "Call 07710 582036 to arrange it. A single lesson works well, and <a href=\"get-into-golf.html\">Get Into Golf</a> is a gentler present for somebody who has never played."),
                 ("What if I need to cancel?",
                  "Let us know as far ahead as you reasonably can on 07710 582036 and we will move the session. Late cancellations are harder to reschedule because the coaching slot has usually gone."),
             ]},

            {"type": "faq", "kick": "05 \u00b7 Improving your golf",
             "h2": "Getting Better at <em>Golf.</em>",
             "qs": [
                 ("How long does it take to get good at golf?",
                  "Longer than most people hope and less long than they fear. You can strike a ball reasonably within a handful of sessions. Getting round a course comfortably usually takes a few months of regular coaching and practice. Progress depends far more on how often you practise than on natural ability."),
                 ("Why am I not improving even though I practise?",
                  "Usually because practice without feedback grooves whatever you already do, including the faults. Hitting two hundred balls a week can make you worse. Practising on a <a href=\"trackman-range.html\">Trackman range</a> tells you within one shot whether a change helped, which is what turns repetition into improvement."),
                 ("Should I fix my swing or my short game first?",
                  "The <a href=\"short-game.html\">short game</a>, almost always. Roughly half your shots happen within a hundred yards of the flag and hardly anybody practises there. An hour on chipping and putting will take more strokes off your card than an hour of drivers."),
                 ("Can lessons help if my body is the problem?",
                  "Yes, but only once you know that is the problem. If you physically cannot make a turn, no coaching will give you one. <a href=\"tpi-screening.html\">TPI screening</a> identifies the restriction and the <a href=\"golf-fitness.html\">golf fitness suite</a> is where you address it."),
                 ("Do I need to play on a course to improve?",
                  "Eventually, yes. Range practice builds the swing, but course management, nerves and awkward lies only get tested in a round. The <a href=\"trackman-simulator.html\">simulator</a> bridges the gap in winter by making you pick a target and a club on every shot."),
             ], "alt": True},

            {"type": "stats", "items": [
                ("7", "Days a Week"), ("7", "Trackman Range Bays"), ("2+", "Simulators"), ("1", "Working Day Reply")]},

            {"type": "accred", "kick": "Accreditations",
             "h2": "Who Are You <em>Booking With?</em>",
             "items": [
                 ("Trackman", "Official Performance Centre", "Radar-tracked range and simulator suites, the same technology used on the PGA Tour."),
                 ("PGA", "PGA Qualified", "Coaching from a member of The Professional Golfers' Association."),
                 ("TPI", "Titleist Performance Institute", "Movement and biomechanics screening, so coaching works with your body."),
             ], "alt": True},

            {"type": "rel", "kick": "Where to next",
             "h2": "Popular Pages on <em>the Site.</em>",
             "links": [
                 ("1-1-lessons.html", "1:1 Golf Lessons", "An hour with an Advanced PGA Professional, Trackman data and video throughout.", "Golf lessons"),
                 ("trackman-range.html", "Trackman Driving Range", "Covered floodlit bays, live ball data, drop in seven days a week.", "Driving range"),
                 ("beginner-coaching.html", "Beginner Coaching", "No experience needed and clubs provided. The starting point for new golfers.", "Beginners"),
                 ("meet-team.html", "Meet Your Coach", "Will Painter, Advanced PGA Professional, and how the academy approaches coaching.", "Your coach"),
                 ("golf-lessons-derby.html", "Golf Lessons Derby", "Directions, prices and coaching options for golfers travelling from Derby.", "Derby"),
                 ("golf-lessons-nottingham.html", "Golf Lessons Nottingham", "Directions, prices and options for golfers travelling from Nottingham.", "Nottingham"),
             ]},
        ],
    },
]
