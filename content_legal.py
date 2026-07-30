"""Privacy policy and terms pages.

Kyle Roof's audit treats these as E-A-T trust signals - Google decides
whether a site belongs in the index at all partly on whether it looks
like a real, accountable business. His specific criticism of the site he
reviewed was that it pointed its privacy and terms links at Google's own
policies rather than having its own.

These are honest placeholders written around what is actually knowable.
Anything that needs a legal decision - data retention periods, the ICO
registration number, cookie vendors - is flagged rather than invented.

>>> ACTION FOR THE CLIENT: have these reviewed before relying on them. <<<
"""

NOTE = ("This page is a working draft. It should be reviewed against your "
        "actual data handling before you rely on it.")

PAGES = [
    {
        "file": "privacy.html",
        "cur": None,
        "title": "Privacy Policy | Evolution Golf Academy Derby &amp; Nottingham",
        "desc": "How Evolution Golf Academy collects, uses and stores your personal data. Contact details, enquiry forms, booking and your rights under UK GDPR.",
        "visit_kick": "Golf academy near Derby &amp; Nottingham",
        "cta": ("Any questions about <em>your data?</em>",
                "Call 07710 582036 or send a message and we will answer within a working day."),
        "hero": {
            "kick": "Privacy Policy",
            "l1": "Privacy", "l2": "Policy.",
            "p": "How <strong>Evolution Golf Academy</strong> collects, uses and stores your personal information, and what rights you have over it. If anything here is unclear, call 07710 582036 and ask.",
            "img": "bay_screen",
            "alt": "Evolution Golf Academy privacy policy",
        },
        "marq": ["Privacy Policy", "Your Data Rights", "UK GDPR",
                 "Evolution Golf Academy", "Codnor, Ripley", "07710 582036"],
        "sections": [
            {"type": "prose", "kick": "Who we are",
             "h2": "Who Controls <em>Your Data?</em>",
             "blocks": [
                 ("p", f"<strong>{NOTE}</strong>"),
                 ("p", "Evolution Golf Academy, Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley, Derbyshire DE5 9RJ, is the data controller for information collected through this website. You can reach us on 07710 582036 or through the <a href=\"contact.html\">contact page</a>."),
                 ("h3", "What Information Do We Collect?"),
                 ("p", "Only what you give us. If you complete an enquiry form we collect your name, email address, phone number if you provide one, the service you are interested in and anything you write in the message field. If you request the practice guide we collect your first name and email address."),
                 ("p", "Bookings made through our booking system are handled by that provider under their own privacy policy. Payments are not processed by this website."),
                 ("h3", "Why Do We Collect It?"),
                 ("p", "To answer your enquiry, arrange your lesson or session, and keep a record of what was agreed. If you opted in to coaching tips when requesting the practice guide, we use your email address for that until you unsubscribe."),
                 ("p", "We do not sell your data, and we do not share it with third parties for their own marketing."),
             ]},
            {"type": "prose", "kick": "Your rights", "alt": True,
             "h2": "What Rights Do You Have Over <em>Your Data?</em>",
             "blocks": [
                 ("p", "Under UK data protection law you can ask us to show you what we hold about you, correct anything wrong, delete it, restrict how we use it, or send it to you in a portable format. You can also object to us using it for marketing at any time."),
                 ("p", "To exercise any of those, call 07710 582036 or write to us at the address above. We will respond within one month. If you are not satisfied with how we handle it, you can complain to the Information Commissioner's Office at ico.org.uk."),
                 ("h3", "How Long Do We Keep It?"),
                 ("p", "Enquiries and coaching records are kept for as long as you are a customer and for a reasonable period afterwards, so that a coach picking up your file knows what you have already worked on. Marketing contacts are kept until you unsubscribe."),
                 ("h3", "Cookies and Analytics"),
                 ("p", "This site uses cookies where necessary for it to function. Embedded content such as the Google Map on our <a href=\"location.html\">location page</a> and the external booking system may set their own cookies under their own policies. You can block cookies in your browser settings, though parts of the site may not work as expected if you do."),
             ]},
            {"type": "rel", "kick": "Related",
             "h2": "Other <em>Pages.</em>",
             "links": [
                 ("terms.html", "Terms of Service", "The terms that apply when you book a lesson, session or facility with us.", "Read terms"),
                 ("contact.html", "Contact the Academy", "Call 07710 582036 or send a message. Answered within a working day.", "Get in touch"),
                 ("faqs.html", "Frequently Asked Questions", "Prices, booking, facilities, fitting and screening, all answered.", "All FAQs"),
                 ("about.html", "About the Academy", "Who we are, how the academy started and how the coaching works.", "About us"),
                 ("meet-team.html", "Meet Your Coach", "Will Painter, Advanced PGA Professional and Academy Director.", "Your coach"),
                 ("location.html", "Location", "Ormonde Fields Golf Club, Codnor, Ripley. Free parking, open seven days.", "Find us"),
             ]},
        ],
    },
    {
        "file": "terms.html",
        "cur": None,
        "title": "Terms of Service | Evolution Golf Academy Derby &amp; Nottingham",
        "desc": "Terms of service for Evolution Golf Academy. Booking, cancellations, use of the range and simulators, safety and liability at our Codnor, Ripley academy.",
        "visit_kick": "Golf academy near Derby &amp; Nottingham",
        "cta": ("Not sure about <em>something?</em>",
                "Call 07710 582036 before you book rather than after. We would rather answer the question."),
        "hero": {
            "kick": "Terms of Service",
            "l1": "Terms of", "l2": "Service.",
            "p": "The terms that apply when you book a lesson, session or facility at <strong>Evolution Golf Academy</strong>. Written in plain English, because terms nobody reads protect nobody.",
            "img": "bay_indoor",
            "alt": "Evolution Golf Academy terms of service",
        },
        "marq": ["Terms of Service", "Booking &amp; Cancellations", "Range &amp; Simulator Use",
                 "Evolution Golf Academy", "Codnor, Ripley", "07710 582036"],
        "sections": [
            {"type": "prose", "kick": "Booking",
             "h2": "What Applies When You <em>Book With Us?</em>",
             "blocks": [
                 ("p", f"<strong>{NOTE}</strong>"),
                 ("p", "These terms cover bookings made with Evolution Golf Academy at Ormonde Fields Golf Club, Nottingham Road, Codnor, Ripley DE5 9RJ. By booking a lesson, a simulator bay, a fitting or a screening you agree to them."),
                 ("h3", "Booking and Payment"),
                 ("p", "<a href=\"1-1-lessons.html\">Lessons</a>, <a href=\"trackman-simulator.html\">simulator bays</a>, custom fitting and <a href=\"tpi-screening.html\">TPI screening</a> are booked in advance. The <a href=\"trackman-range.html\">Trackman driving range</a> is walk-in and does not need booking. Prices are confirmed at the time of booking."),
                 ("h3", "Cancellations and Rescheduling"),
                 ("p", "Let us know as far ahead as you reasonably can on 07710 582036 and we will move your session. Late cancellations are harder to reschedule because the coaching slot has usually gone. If we have to cancel, we will offer an alternative time."),
                 ("h3", "Membership"),
                 ("p", "<a href=\"memberships.html\">Membership</a> is optional and gives priority booking and better rates. Nothing at the academy requires membership. Current terms are confirmed when you join."),
             ]},
            {"type": "prose", "kick": "Using the academy", "alt": True,
             "h2": "What Are the Rules for <em>Using the Facilities?</em>",
             "blocks": [
                 ("h3", "Safety"),
                 ("p", "Golf clubs and golf balls are dangerous when people are careless. Stay in your bay, keep behind anyone who is swinging, and supervise children at all times. Follow any instruction from academy staff immediately, particularly on the <a href=\"grass-range.html\">grass range</a> and in the <a href=\"short-game.html\">short game area</a> where people are moving about."),
                 ("h3", "Equipment"),
                 ("p", "Club hire on the range and simulators is included at no extra cost. Hired clubs remain ours, and you are responsible for returning them in the condition you received them. Damage caused by misuse may be charged for."),
                 ("h3", "Your Own Belongings"),
                 ("p", "Bring what you need but keep an eye on it. We cannot accept responsibility for personal property left unattended on site or in the car park."),
                 ("h3", "Health"),
                 ("p", "Golf, and <a href=\"golf-fitness.html\">golf fitness work</a> in particular, is physical. Tell your coach about any injury, condition or medication that might be relevant before you start. We are not a medical service, and anything painful or persistent should be seen by a physiotherapist or GP."),
                 ("h3", "Behaviour"),
                 ("p", "We want an academy where a complete beginner feels as comfortable as a low handicapper. Behaviour that undermines that, towards staff or other golfers, means being asked to leave."),
             ]},
            {"type": "rel", "kick": "Related",
             "h2": "Other <em>Pages.</em>",
             "links": [
                 ("privacy.html", "Privacy Policy", "How we collect, use and store your personal data, and your rights over it.", "Read policy"),
                 ("contact.html", "Contact the Academy", "Call 07710 582036 or send a message. Answered within a working day.", "Get in touch"),
                 ("faqs.html", "Frequently Asked Questions", "Prices, booking, facilities, fitting and screening, all answered.", "All FAQs"),
                 ("memberships.html", "Memberships", "Priority booking and better rates for golfers who are here often.", "Membership"),
                 ("1-1-lessons.html", "1:1 Golf Lessons", "An hour with an Advanced PGA Professional, Trackman data throughout.", "Golf lessons"),
                 ("location.html", "Location", "Ormonde Fields Golf Club, Codnor, Ripley. Free parking, open seven days.", "Find us"),
             ]},
        ],
    },
]
