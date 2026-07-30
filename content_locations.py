"""Location CMS template - "Golf Lessons in {Location}".

ONE template, one row per town. Mirrors the Webflow CMS structure:
`ROWS` is the Locations collection, `location_page()` is the template
page. Adding a town means adding a row, nothing else.

CMS fields per row: location, area, nearest, distance, slug.
Plus per-town unique copy, which is NOT optional - ten pages that differ
only by town name read as doorway pages and get filtered. Every row
carries its own intro, routes, local detail and extra FAQs.

SEO rules locked in by the template:
  - exactly one H1 = the hero kicker, keyword first: "Golf Lessons in {Location}"
  - the big display headline is NOT an h1
  - title = "Golf Lessons in {Location} | Evolution Golf Academy"
  - H2s keep the "...{Location}..." pattern
"""

# ── the Locations collection ────────────────────────────────────────
ROWS = [
    {"location": "Derby", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "20 minutes", "slug": "golf-lessons-derby"},
    {"location": "Nottingham", "area": "Nottinghamshire", "nearest": "Codnor",
     "distance": "25 minutes", "slug": "golf-lessons-nottingham"},
    {"location": "Ripley", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "5 minutes", "slug": "golf-lessons-ripley"},
    {"location": "Heanor", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "8 minutes", "slug": "golf-lessons-heanor"},
    {"location": "Alfreton", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "10 minutes", "slug": "golf-lessons-alfreton"},
    {"location": "Ilkeston", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "12 minutes", "slug": "golf-lessons-ilkeston"},
    {"location": "Belper", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "15 minutes", "slug": "golf-lessons-belper"},
    {"location": "Mansfield", "area": "Nottinghamshire", "nearest": "Codnor",
     "distance": "20 minutes", "slug": "golf-lessons-mansfield"},
    {"location": "Eastwood", "area": "Nottinghamshire", "nearest": "Codnor",
     "distance": "10 minutes", "slug": "golf-lessons-eastwood"},
    {"location": "Chesterfield", "area": "Derbyshire", "nearest": "Codnor",
     "distance": "25 minutes", "slug": "golf-lessons-chesterfield"},
]

# ── per-town unique copy (the anti-doorway-page layer) ──────────────
UNIQUE = {
"Derby": {
 "img": "lesson_grip",
 "road": "the A610",
 "intro": [
  "Derby is not short of places to hit a golf ball. It is short of places to actually learn. Most options are either a members' club with a waiting list and a dress code, or a strip of mats with no coaching attached and nobody watching.",
  "Evolution Golf Academy sits deliberately between the two. It is a full performance facility with Advanced PGA Professional coaching, Trackman on every bay and no membership requirement whatsoever, roughly <strong>20 minutes from Derby city centre</strong> on the A610 through Ripley.",
  "For most Derby golfers that journey is shorter than crossing the city at rush hour, and there is free parking at the end of it rather than a multi-storey and a ten minute walk with a golf bag.",
 ],
 "why_h3": "Why Do Derby Golfers Drive Out to Codnor?",
 "why": "Because the coaching here is measured rather than guessed at. Every bay carries Trackman, so when your coach changes something you both watch the numbers move or fail to. Derby has ranges. What it does not have is a Trackman Official Performance Centre where an Advanced PGA Professional coaches from live launch data.",
 "routes": [
  ("From Derby city centre", "Head north east and join the A610 towards Ripley and Codnor. Stay on it past Ripley and the academy is on Nottingham Road at Ormonde Fields Golf Club. Around 20 minutes in normal traffic."),
  ("From Allestree, Oakwood and Chaddesden", "You start on the right side of the city. Pick up the A38 or A61 north and cut across to the A610 at Ripley. Usually a little quicker than from the centre."),
  ("From Spondon, Borrowash and Long Eaton", "Head north through Ilkeston and Heanor and join the A610 at Codnor, which avoids Derby city traffic altogether."),
  ("From Mickleover and the south west", "Ring road round to the A38 north, then across to Ripley. Allow a bit longer at peak times."),
 ],
 "areas": ["Allestree", "Oakwood", "Chaddesden", "Spondon", "Mickleover", "Borrowash",
           "Littleover", "Darley Abbey", "Breadsall", "Duffield"],
 "faqs": [
  ("What is the best golf driving range near Derby?",
   "It depends what you want from it. If you want to hit a bucket cheaply, plenty of ranges will do the job. If you want to know your genuine carry distances and improve measurably, a <a href=\"trackman-range.html\">Trackman range</a> gives you information that mats and a bucket simply cannot."),
  ("Do you coach complete beginners from Derby?",
   "Every week. <a href=\"beginner-coaching.html\">Beginner golf lessons</a> assume no experience at all and clubs are provided, so there is nothing to buy before your first session. If a one to one feels like too much, <a href=\"get-into-golf.html\">Get Into Golf</a> runs as a friendlier group format."),
  ("Are there junior golf lessons near Derby?",
   "Yes. The <a href=\"junior-academy.html\">junior academy</a> covers ages six to sixteen with weekend group coaching and holiday camps, led by Will Painter, Advanced PGA Professional. A lot of Derby parents make the trip because structured junior coaching with launch monitor data is hard to find closer in."),
 ],
},
"Nottingham": {
 "img": "over_shoulder",
 "road": "the A610 through Eastwood",
 "intro": [
  "Nottingham golfers have a decent choice of courses and a much thinner choice of proper coaching facilities. There is a difference between somewhere to play and somewhere to get better, and the city is better supplied with the first than the second.",
  "Evolution Golf Academy is a Trackman Official Performance Centre with Advanced PGA Professional coaching on site, about <strong>25 minutes from Nottingham city centre</strong> on the A610 through Eastwood and Langley Mill.",
  "It is a single-road run for most of the way and it avoids the motorway entirely. From the north west of the city - Kimberley, Nuthall, Watnall, Giltbrook - you are considerably closer than that.",
 ],
 "why_h3": "Is It Worth Driving Out of Nottingham for a Golf Lesson?",
 "why": "That depends what you want. If you want somebody to watch you hit balls and offer a tip, you can find that closer to home. If you want your swing measured, your equipment checked against Trackman data and a plan you can actually follow between sessions, the drive buys you a facility that does not really exist inside the city.",
 "routes": [
  ("From Nottingham city centre", "Head north west and pick up the A610 towards Eastwood and Ripley. Stay on it through Eastwood and Langley Mill and the academy is on Nottingham Road at Codnor. Around 25 minutes outside peak hours."),
  ("From Kimberley, Nuthall and Giltbrook", "You are practically next door. Join the A610 north west and you are here in a fraction of the time it takes from the centre."),
  ("From Hucknall, Bulwell and Annesley", "Cut across to the A610 at Eastwood, or come down through Selston. Similar either way."),
  ("From Beeston, Stapleford and the south", "Head up the A6002 or A52 to join the A610 west of the city, then straight out."),
 ],
 "areas": ["Eastwood", "Kimberley", "Nuthall", "Watnall", "Giltbrook", "Bulwell",
           "Hucknall", "Arnold", "Beeston", "Stapleford"],
 "faqs": [
  ("Can I play indoor golf near Nottingham in winter?",
   "Yes, and it is one of the main reasons Nottingham golfers come here between November and March. The <a href=\"trackman-simulator.html\">Trackman simulator</a> lets you play full rounds on world courses indoors, and the covered floodlit range means ordinary practice carries on regardless of the weather."),
  ("Do you coach beginners from Nottingham?",
   "Every week. <a href=\"beginner-coaching.html\">Beginner golf lessons</a> assume no prior experience and clubs are provided, so you can turn up with nothing at all. Nobody is going to make you feel awkward about starting from zero."),
  ("Is there a Trackman range near Nottingham?",
   "Yes. Our <a href=\"trackman-range.html\">Trackman driving range</a> is a straight run out on the A610 and is open every day from 7am to 8pm. Bays are covered and floodlit, so it runs identically in December and June, and it is walk-in with no booking needed."),
 ],
},
"Ripley": {
 "img": "range_night",
 "road": "the A610",
 "intro": [
  "If you live in Ripley, this is your local golf academy in the most literal sense. Evolution Golf Academy is at Ormonde Fields Golf Club on Nottingham Road in Codnor, <strong>about 5 minutes from Ripley town centre</strong>.",
  "That proximity changes how you can use the place. Golfers from further afield plan a trip. Ripley golfers can drop in for half an hour on a Tuesday evening, hit fifty balls with Trackman running, and be home before the kettle has gone cold.",
  "It also makes the <a href=\"monthly-programme.html\">monthly coaching programme</a> considerably easier to stick to, because practising between lessons stops being something you have to schedule around a drive.",
 ],
 "why_h3": "What Does Having the Academy on Your Doorstep Change?",
 "why": "Frequency. The single biggest predictor of whether coaching sticks is how much you practise between sessions, and the biggest barrier to practising is travel. Five minutes down the road removes that barrier entirely, which is why Ripley golfers tend to progress faster than the coaching alone would explain.",
 "routes": [
  ("From Ripley town centre", "Head out on Nottingham Road towards Codnor. The academy is at Ormonde Fields Golf Club on your right. Around 5 minutes."),
  ("From Waingroves and Marehay", "Straight across to Codnor, a matter of minutes in either case."),
  ("From Swanwick and Butterley", "Down the A610 towards Codnor and you are here almost immediately."),
  ("Walking or cycling", "Parts of Ripley and Codnor are close enough to walk or cycle, though you will want a light for the evening range sessions in winter."),
 ],
 "areas": ["Codnor", "Waingroves", "Marehay", "Butterley", "Swanwick", "Loscoe",
           "Langley Mill", "Somercotes", "Ironville", "Pentrich"],
 "faqs": [
  ("Can I just turn up to the range from Ripley?",
   "Yes. The <a href=\"trackman-range.html\">Trackman driving range</a> is walk-in on a first-come basis, seven days a week from 7am to 8pm. Being this close, plenty of Ripley golfers use it for short, frequent sessions rather than one long one a week."),
  ("Do you run junior coaching for Ripley families?",
   "Yes. The <a href=\"junior-academy.html\">junior academy</a> covers ages six to sixteen with weekend group sessions and holiday camps, which are considerably easier to commit to when the drive is five minutes each way."),
  ("Is the academy part of Ormonde Fields Golf Club?",
   "We are based at Ormonde Fields Golf Club, but the academy is open to everybody. You do not need to be a member of the club, or any club, to book a lesson, use the range or hire the simulator."),
 ],
},
"Heanor": {
 "img": "student_swing",
 "road": "the A6007 and A610",
 "intro": [
  "Heanor golfers are close enough that Evolution Golf Academy functions as a local range rather than a destination. It is <strong>about 8 minutes from Heanor</strong>, down through Loscoe and Langley Mill to Codnor.",
  "That short hop gets you a six bay Trackman range, an indoor simulator, a private teaching bay, a grass range and a golf fitness suite on a single site, with free parking and no membership to join.",
  "For anyone who has been making do with hitting balls into a net or driving considerably further for coaching that actually measures something, it is a straightforward upgrade.",
 ],
 "why_h3": "What Can Heanor Golfers Use the Academy For?",
 "why": "Most Heanor golfers who come to us use it in two ways: regular short range sessions with Trackman running to keep an eye on their numbers, and periodic <a href=\"1-1-lessons.html\">lessons with a PGA Professional</a> when something goes wrong they cannot diagnose themselves. Being eight minutes away makes both realistic on a weeknight.",
 "routes": [
  ("From Heanor town centre", "Head north on the A6007 through Loscoe towards Langley Mill, then join the A610 west to Codnor. Around 8 minutes."),
  ("From Langley Mill and Aldercar", "Straight up the A610 towards Ripley and the academy is on Nottingham Road at Codnor."),
  ("From Marlpool and Shipley", "Cut across to Heanor and follow the same route north, or come round via Codnor Park."),
  ("From Smalley and Kilburn", "North on the A608 to Heanor then across to Codnor, or the country roads via Loscoe if you know them."),
 ],
 "areas": ["Loscoe", "Langley Mill", "Aldercar", "Marlpool", "Shipley", "Codnor Park",
           "Smalley", "Kilburn", "Denby", "Eastwood"],
 "faqs": [
  ("How close is the golf academy to Heanor?",
   "Around 8 minutes by car, north through Loscoe and Langley Mill to Codnor. Free parking directly outside the range, so you can be hitting balls within a couple of minutes of arriving."),
  ("Is there a driving range near Heanor?",
   "Yes. Our <a href=\"trackman-range.html\">Trackman driving range</a> is the closest full launch-monitor range to Heanor. Six covered floodlit bays, walk-in with no booking, open 7am to 8pm every day of the year."),
  ("Can I get custom club fitting near Heanor?",
   "Yes. Custom fitting runs on Trackman data and covers shaft, loft, lie and gapping. Fittings are brand neutral, so you leave with a full written specification and can buy from us or anywhere you like."),
 ],
},
"Alfreton": {
 "img": "bay_night",
 "road": "the A38 and A610",
 "intro": [
  "Evolution Golf Academy is <strong>about 10 minutes from Alfreton</strong>, south through Swanwick and down to Codnor. For Alfreton golfers that puts a full Trackman coaching facility closer than most people realise.",
  "The site carries a six bay Trackman range, an indoor simulator with over 200 world courses, a private teaching bay with video analysis, a grass range for the drier months and a golf fitness suite, all in one place.",
  "You do not need to be a member for any of it. Membership is available and gives priority booking and better rates, but everything here is open to the public.",
 ],
 "why_h3": "Why Do Alfreton Golfers Come Here Rather Than Stay Local?",
 "why": "Because ten minutes is a small price for coaching that works from measured data rather than opinion. Trackman shows ball speed, spin, launch angle, carry and club path on every shot, so a lesson produces evidence rather than a feeling that things went reasonably well.",
 "routes": [
  ("From Alfreton town centre", "Head south through Swanwick on the A61 or B6016, then down to Codnor via Ripley. Around 10 minutes."),
  ("From Somercotes and Ironville", "Straight down towards Codnor Park and Codnor, one of the quickest approaches to the academy."),
  ("From South Normanton and Pinxton", "Join the A38 south then cut across at Alfreton and follow the route through Swanwick."),
  ("From Riddings and Leabrooks", "Short run south to Codnor, often under ten minutes."),
 ],
 "areas": ["Swanwick", "Somercotes", "Ironville", "Riddings", "Leabrooks", "South Normanton",
           "Pinxton", "Codnor Park", "Westhouses", "Golden Valley"],
 "faqs": [
  ("How far is the golf academy from Alfreton?",
   "About 10 minutes by car, south through Swanwick towards Ripley and Codnor. Free on-site parking when you arrive."),
  ("Do I need to be a member to use the academy?",
   "No. Lessons, range time, the simulator and fitting are all open to everyone. Membership exists and gives priority booking and better rates, but nothing here requires it."),
  ("What is TPI screening and do I need it?",
   "<a href=\"tpi-screening.html\">TPI screening</a> is a movement assessment that shows how your body actually moves and links each restriction to the swing fault it tends to cause. It becomes worth doing when a coach keeps asking for a position you physically cannot reach."),
 ],
},
"Ilkeston": {
 "img": "coach_feedback",
 "road": "the A6007",
 "intro": [
  "Evolution Golf Academy is <strong>about 12 minutes from Ilkeston</strong>, north on the A6007 through Heanor and across to Codnor. It sits right on the Derbyshire and Nottinghamshire border, which is handy given Ilkeston does the same.",
  "What you get at the end of that drive is a six bay Trackman range, an indoor Trackman simulator, a private teaching bay with video analysis, a grass range and a golf fitness suite, with Advanced PGA Professional coaching across all of it.",
  "Free parking, open seven days a week from 7am to 8pm, and no membership needed.",
 ],
 "why_h3": "What Makes This Different From an Ordinary Range Near Ilkeston?",
 "why": "Every bay has Trackman on it. That sounds like a detail and it changes everything, because it turns practice from repetition into feedback. You find out within one shot whether a change helped, instead of believing it helped because one ball out of ten felt good.",
 "routes": [
  ("From Ilkeston town centre", "North on the A6007 through Cotmanhay and Shipley towards Heanor, then across to Codnor. Around 12 minutes."),
  ("From Cotmanhay and Shipley", "You are already on the route north, so the run is shorter still."),
  ("From Kirk Hallam and Little Hallam", "Join the A6007 north through Ilkeston and follow the same road up towards Heanor."),
  ("From Awsworth and Trowell", "Cut across to the A610 at Eastwood and come in from the Nottinghamshire side."),
 ],
 "areas": ["Cotmanhay", "Shipley", "Kirk Hallam", "Little Hallam", "Awsworth", "Trowell",
           "Stanton by Dale", "West Hallam", "Smalley", "Heanor"],
 "faqs": [
  ("How long does it take to get here from Ilkeston?",
   "Around 12 minutes by car, north on the A6007 through Heanor and across to Codnor. Free parking directly outside the range."),
  ("Are there ladies golf lessons near Ilkeston?",
   "Yes. <a href=\"ladies-academy.html\">Ladies coaching</a> covers all abilities including complete beginners. We are a coaching academy rather than a members' club, so there is no dress code to decode and no clubhouse politics to navigate."),
  ("Can I book a simulator bay for a group?",
   "Yes. The <a href=\"trackman-simulator.html\">Trackman simulator</a> is booked by the hour and takes a small group comfortably. Rounds play far quicker indoors than on a real course, so a group can get eighteen holes done in an evening."),
 ],
},
"Belper": {
 "img": "putting",
 "road": "the A610 via Ambergate",
 "intro": [
  "Evolution Golf Academy is <strong>about 15 minutes from Belper</strong>, across through Ambergate and down the A610 to Codnor. For Belper golfers it is the nearest facility that combines PGA coaching with launch monitor data on every bay.",
  "The academy has a six bay Trackman range, an indoor simulator, a private teaching bay, a grass driving range for the drier months and a short game area covering chipping, pitching, bunker play and putting.",
  "All of it is open to anybody. You do not need to be a member to book a lesson, hit balls or hire a simulator bay, and club hire on the range and simulators is included at no extra cost.",
  "Belper golfers tend to fall into two camps: people who play regularly at a club and want somewhere to actually practise with feedback, and people who have never played and want to start without an audience. The academy handles both, which is unusual, because most facilities are set up for one or the other.",
 ],
 "why_h3": "What Should Belper Golfers Work On Here?",
 "why": "Whatever is actually costing shots, which for most club golfers is the <a href=\"short-game.html\">short game</a> rather than the driver. Roughly half of all shots happen within a hundred yards of the flag and almost nobody practises there, which makes it the fastest place to find strokes.",
 "routes": [
  ("From Belper town centre", "Head north east through Ambergate, join the A610 towards Ripley and continue to Codnor. Around 15 minutes."),
  ("From Ambergate and Heage", "You are on the direct route already, so the run is shorter."),
  ("From Duffield and Milford", "North through Belper then across via Ambergate on the same road."),
  ("From Holbrook and Denby", "Across country to the A610 at Ripley and straight through to Codnor."),
 ],
 "areas": ["Ambergate", "Heage", "Duffield", "Milford", "Holbrook", "Denby",
           "Openwoodgate", "Kilburn", "Crich", "Bargate"],
 "faqs": [
  ("How far is the academy from Belper?",
   "Around 15 minutes by car, through Ambergate and down the A610 to Codnor. Free on-site parking."),
  ("Is there a short game practice area?",
   "Yes. The <a href=\"short-game.html\">short game area</a> covers chipping, pitching, bunker play and putting. It is the most underused facility on site and comfortably the quickest way for a club golfer to drop shots."),
  ("Do you do golf lessons for older players?",
   "Yes, and plenty of them. <a href=\"tpi-screening.html\">TPI screening</a> is particularly useful later on, because mobility restrictions build up over time and respond well to targeted work. The <a href=\"golf-fitness.html\">golf fitness suite</a> is where that gets addressed."),
  ("Can I practise in the evening after work?",
   "Yes. The range bays are floodlit and we are open until 8pm every day, so an evening session works in January as well as it does in June. For Belper golfers the drive over through Ambergate is straightforward at that time of day."),
 ],
},
"Mansfield": {
 "img": "range_sil",
 "road": "the A38 and B6016",
 "intro": [
  "Evolution Golf Academy is <strong>about 20 minutes from Mansfield</strong>, west across through Kirkby in Ashfield and Alfreton and down to Codnor. For Mansfield golfers it is a straightforward run to a facility with more under one roof than anything closer.",
  "Six Trackman bays, an indoor simulator with over 200 world courses, a private teaching bay with video analysis, a grass range, a short game area and a golf fitness suite, with Advanced PGA Professional coaching across them.",
  "Open seven days a week, 7am to 8pm, free parking, no membership.",
 ],
 "why_h3": "Is There Trackman Coaching Near Mansfield?",
 "why": "Not much of it, which is why Mansfield golfers travel. Trackman is the dual-radar launch monitor used on the PGA Tour, and being an Official Performance Centre means every bay here has it. A lesson works from measured numbers rather than a coach's read of your ball flight.",
 "routes": [
  ("From Mansfield town centre", "Head west on the A38 towards Alfreton, then south through Swanwick to Ripley and Codnor. Around 20 minutes."),
  ("From Kirkby in Ashfield and Sutton", "Join the A38 west and follow the same route down through Alfreton."),
  ("From Mansfield Woodhouse", "South through Mansfield to pick up the A38 west, then as above."),
  ("From Annesley and Selston", "Cut down through Selston towards Ironville and Codnor, which avoids Alfreton entirely."),
 ],
 "areas": ["Mansfield Woodhouse", "Kirkby in Ashfield", "Sutton in Ashfield", "Annesley",
           "Selston", "Skegby", "Huthwaite", "Pleasley", "Blidworth", "Rainworth"],
 "faqs": [
  ("How long is the drive from Mansfield?",
   "Around 20 minutes, west on the A38 through Alfreton and down to Codnor. Free parking on site when you arrive."),
  ("Is it worth travelling from Mansfield for a golf lesson?",
   "If you want coaching built on Trackman data and a facility that covers range, simulator, short game, fitting and fitness on one site, yes. If you only want to hit a bucket of balls, there will be somewhere closer that does the job."),
  ("Do you offer a monthly coaching programme?",
   "Yes. The <a href=\"monthly-programme.html\">monthly programme</a> gives you structured coaching with a plan between sessions rather than occasional one-off lessons, which is what actually shifts a handicap and keeps it shifted."),
 ],
},
"Eastwood": {
 "img": "driver_balls",
 "road": "the A610",
 "intro": [
  "Evolution Golf Academy is <strong>about 10 minutes from Eastwood</strong>, straight out on the A610 through Langley Mill to Codnor. It is one of the shortest runs of any town we serve and effectively makes this Eastwood's local golf academy.",
  "You get a six bay Trackman range, an indoor Trackman simulator, a private teaching bay with video analysis, a grass driving range and a golf fitness suite, with Advanced PGA Professional coaching across all of it.",
  "Free parking, seven days a week, 7am to 8pm, and no membership needed to use any of it.",
 ],
 "why_h3": "What Can Eastwood Golfers Get Here?",
 "why": "Everything in one place, ten minutes from home. Most golfers end up splitting their practice across a range in one town and coaching in another. Here the range, the teaching bay, the simulator, the short game area, custom fitting and the fitness suite are on a single site, so nothing gets skipped because it was inconvenient.",
 "routes": [
  ("From Eastwood town centre", "Join the A610 north west towards Langley Mill and Ripley. The academy is on Nottingham Road at Codnor. Around 10 minutes."),
  ("From Newthorpe and Giltbrook", "Straight onto the A610 and out, often under ten minutes."),
  ("From Brinsley and Underwood", "Down to the A610 at Langley Mill and west to Codnor."),
  ("From Kimberley and Watnall", "North west on the A610 the whole way, a simple single-road run."),
 ],
 "areas": ["Langley Mill", "Newthorpe", "Giltbrook", "Brinsley", "Underwood", "Kimberley",
           "Watnall", "Nuthall", "Aldercar", "Moorgreen"],
 "faqs": [
  ("How close is the academy to Eastwood?",
   "About 10 minutes on the A610 through Langley Mill. One of the shortest journeys of any town we serve, with free parking outside the range."),
  ("Can I use the range without booking from Eastwood?",
   "Yes. The <a href=\"trackman-range.html\">Trackman driving range</a> is walk-in on a first-come basis, seven days a week. Being this close, a lot of Eastwood golfers drop in for short frequent sessions rather than one long one."),
  ("Do you run group coaching for beginners?",
   "Yes. <a href=\"get-into-golf.html\">Get Into Golf</a> is a group format built for people who have never played, with clubs provided and nobody expecting you to know anything. It is the gentlest way in."),
 ],
},
"Chesterfield": {
 "img": "bay_indoor",
 "road": "the A61",
 "intro": [
  "Evolution Golf Academy is <strong>about 25 minutes from Chesterfield</strong>, south on the A61 through Clay Cross and Alfreton to Codnor. It is the longest run of the towns we serve, and the reason Chesterfield golfers make it is that there is nothing equivalent closer.",
  "Six Trackman bays, an indoor simulator with over 200 world courses, a private teaching bay with video analysis and training aids, a grass range, a short game area and a golf fitness suite, with Advanced PGA Professional coaching across the lot.",
  "No membership needed, free parking, and open every day from 7am to 8pm.",
 ],
 "why_h3": "Is the Drive From Chesterfield Worth It?",
 "why": "Honestly, that depends on what you want. For a bucket of balls, no. For coaching that measures your swing on Trackman, checks your equipment against real data and screens how your body moves, there is no closer facility that does all three, and most golfers who make the trip come back.",
 "routes": [
  ("From Chesterfield town centre", "South on the A61 through Clay Cross and Higham towards Alfreton, then down through Swanwick to Ripley and Codnor. Around 25 minutes."),
  ("From Clay Cross and Tupton", "You are already on the A61 route south, which takes a decent chunk off the journey."),
  ("From Brimington and Staveley", "Round to the A61 south through Chesterfield and follow the same road down."),
  ("From Dronfield and the north", "Straight down the A61 through Chesterfield and continue south towards Alfreton."),
 ],
 "areas": ["Clay Cross", "Tupton", "Brimington", "Staveley", "Dronfield", "Wingerworth",
           "North Wingfield", "Grassmoor", "Holmewood", "Higham"],
 "faqs": [
  ("How far is Evolution Golf Academy from Chesterfield?",
   "Around 25 minutes by car, south on the A61 through Clay Cross and Alfreton. Free on-site parking when you get here."),
  ("Can I combine a lesson and range time in one trip?",
   "Yes, and if you are travelling from Chesterfield it is worth doing. Book a <a href=\"1-1-lessons.html\">lesson</a>, then stay on afterwards for range time or a <a href=\"trackman-simulator.html\">simulator</a> session to work on what you have just been shown while it is fresh."),
  ("Do you do full bag custom fitting?",
   "Yes. Full bag fittings run on Trackman data and typically take ninety minutes to two hours, covering shaft, loft, lie and gapping. Fittings are brand neutral, so you get a full written specification and can buy wherever you like."),
 ],
},
}

BAYS = "6"


def location_page(row):
    """The CMS template page. One row in, one page spec out."""
    L, A = row["location"], row["area"]
    near, dist = row["nearest"], row["distance"]
    mins = dist.split()[0]
    u = UNIQUE[L]

    intro_blocks = [("p", p) for p in u["intro"]]
    intro_blocks += [("h3", u["why_h3"]), ("p", u["why"])]

    return {
        "file": row["slug"] + ".html",
        "cur": row["slug"] + ".html",
        # SEO rule: title is exactly this pattern
        "title": f"Golf Lessons in {L} | Evolution Golf Academy",
        "desc": (f"Golf lessons in {L} with an Advanced PGA Professional at Evolution Golf Academy, {dist} away. "
                 f"Trackman range, indoor simulator, TPI screening and custom fitting for golfers across {A}."),
        "visit_kick": f"Golf academy near {L}",
        "cta": (f"Golf lessons in <em>{L}</em> start here.",
                "One lesson, no commitment. We pair you with the right coach based on your goals and where you are in your game."),
        "hero": {
            # SEO rule: the H1 is this small kicker, keyword first
            "kick": f"Golf Lessons in {L}",
            # the big display headline is NOT an h1
            "l1": "Golf Lessons", "l2": f"{L}.",
            "p": (f"<strong>Golf lessons in {L}</strong> at Evolution Golf Academy, {dist} away in {near}. "
                  f"Advanced PGA Professional coaching, Trackman range time, indoor simulators and TPI movement screening "
                  f"for golfers across {A}, from complete beginners through to low handicaps."),
            "img": u["img"],
            "alt": f"Golf lessons in {L} with a PGA Professional at Evolution Golf Academy",
        },
        "marq": [f"Golf Lessons {L}", f"PGA Coaching {A}", "Trackman Range",
                 "TPI Screening", f"Junior Lessons {L}", f"Golf Academy Near {L}"],
        "sections": [

            {"type": "prose", "kick": f"The academy that {L} golfers drive to",
             "h2": f"Where Can You Get <em>Golf Lessons in {L}?</em>",
             "blocks": intro_blocks},

            {"type": "split", "img": "range_night",
             "img_alt": f"Trackman driving range near {L}",
             "kick": f"Why golfers across {L} choose Evolution",
             "h2": f"Why Do Golfers Across {L} <em>Choose Evolution?</em>",
             "paras": [
                 f"Evolution Golf Academy is a modern coaching facility at Ormonde Fields Golf Club, <strong>{dist} from {L}</strong>. "
                 f"A {BAYS} bay Trackman range, indoor simulator, private teaching bay, grass range and golf fitness suite, all on one site.",
                 f"From your first lesson to your fifteenth season, our golf coaching in {A} is built around how you learn rather than how we would prefer to teach.",
             ],
             "ticks": [
                 f"<b>{dist} from {L}</b> via {u['road']}, with free on-site parking",
                 f"<b>Trackman on every bay</b> - <a href=\"trackman-range.html\">measured practice</a>, not guesswork",
                 "<b>Advanced PGA Professional coaching</b> - <a href=\"meet-team.html\">meet your coach</a>",
                 "<b>Open 7 days</b> - 7am to 8pm, floodlit right through the winter",
                 "<b>No membership needed</b> - book one <a href=\"1-1-lessons.html\">lesson</a> and that is the whole commitment",
             ],
             "btn2": ("See pricing", "1-1-lessons.html"), "alt": True},

            {"type": "stats", "items": [
                ("1:1", "PGA Coaching"), (BAYS, "Range Bays"), (mins, f"Minutes From {L}")]},

            {"type": "cards", "kick": f"What we offer to {L} golfers",
             "h2": f"Golf Lessons, Trackman and Fitting in <em>{A}.</em>",
             "cards": [
                 {"img": "lesson_grip", "alt": f"1:1 golf lesson near {L}",
                  "h": f"1:1 Golf Lessons · {L}",
                  "p": f"One to one coaching with an Advanced PGA Professional and Trackman feedback on every shot. Golfers from {L} are with us in about {dist}.",
                  "href": "1-1-lessons.html", "cta": "Golf lessons"},
                 {"img": "range_night", "alt": f"Trackman driving range near {L}",
                  "h": f"Trackman Range · Near {L}",
                  "p": f"{BAYS} covered bays with Trackman on every one. Open seven days a week, and the closest full Trackman range to {L}.",
                  "href": "trackman-range.html", "cta": "Driving range"},
                 {"img": "sim", "alt": f"Indoor golf simulator near {L}",
                  "h": "Trackman Simulator",
                  "p": "Play over 200 world courses indoors whatever the weather. Hourly bay hire, and a group can get a full round done in an evening.",
                  "href": "trackman-simulator.html", "cta": "Golf simulator"},
                 {"img": "tpi", "alt": f"TPI movement screening in {A}",
                  "h": f"TPI Screening · {A}",
                  "p": "A movement screen that shows how your body actually moves, so the swing changes you work on actually stick.",
                  "href": "tpi-screening.html", "cta": "TPI screening"},
                 {"img": "junior", "alt": f"Junior golf coaching near {L}",
                  "h": f"Junior Coaching · {L}",
                  "p": f"Weekend group coaching, holiday camps and on-course sessions. Juniors travel in from {L} and across {A}.",
                  "href": "junior-academy.html", "cta": "Junior academy"},
                 {"img": "coach_feedback", "alt": "Monthly golf coaching programme",
                  "h": "Monthly Programme",
                  "p": "Structured coaching with regular reviews and support between lessons. Built for golfers committed to improving.",
                  "href": "monthly-programme.html", "cta": "Monthly programme"},
             ], "alt": True},

            {"type": "steps", "kick": f"Coming from {L}?",
             "h2": f"How Do You Get Here <em>From {L}?</em>",
             "p": f"About {dist} by car via {u['road']}, with free parking directly outside the range.",
             "steps": u["routes"] + [
                 ("Parking and arrival",
                  "Free parking directly outside the driving range and teaching studio, so you park and walk straight to your bay. "
                  "If it is your first lesson, arrive ten minutes early so your coach can find out what you want from it before the clock starts.")]},

            {"type": "areas", "kick": f"Areas near {L} we serve",
             "h2": f"Which Areas Near {L} <em>Do You Cover?</em>",
             "p": f"Golfers travel to us from right across {L} and the surrounding {A} towns.",
             "tags": [(t, None) for t in u["areas"]]
                     + [("Ripley", "location.html"), ("All areas", "location.html")]},

            {"type": "rel", "kick": "Explore the academy",
             "h2": f"What Else Is on Site Near <em>{L}?</em>",
             "links": [
                 ("trackman-teaching-bay.html", "Trackman Teaching Bay",
                  "A private, quiet bay with Trackman, video analysis, mirrors and training aids for one to one coaching.", "Teaching bay"),
                 ("grass-range.html", "Grass Driving Range",
                  "Real turf, real divots and honest feedback on your strike through the drier months.", "Grass range"),
                 ("short-game.html", "Short Game Area",
                  "Chipping, pitching, bunker play and putting - where most amateur golfers save strokes quickest.", "Short game"),
                 ("golf-fitness.html", "Golf Fitness Suite",
                  "TPI-informed mobility, strength and speed work built around the demands of the golf swing.", "Golf fitness"),
                 ("beginner-coaching.html", "Beginner Coaching",
                  "No experience needed and clubs provided. The standard starting point for brand new golfers.", "Beginners"),
                 ("faqs.html", "Frequently Asked Questions",
                  "Prices, booking, the range, the simulator, custom fitting and TPI screening, all answered.", "All FAQs"),
             ]},

            {"type": "faq", "kick": f"{L} golf lesson FAQs",
             "h2": f"Golf Lessons in {L}, <em>Answered.</em>",
             "p": f"Common questions from golfers travelling from {L} and the wider {A} area.",
             "qs": [
                 (f"How long does it take to drive from {L}?",
                  f"Around {dist} via {u['road']}, with free on-site parking when you arrive. The academy is at Ormonde Fields Golf Club, Nottingham Road, {near}, Ripley DE5 9RL."),
                 ("Do I need to be a member to book a lesson?",
                  f"No. Lessons and range time are open to everyone in {A}, member or not. Membership is optional and simply gives priority booking and better rates."),
                 (f"Are golf clubs provided for beginners from {L}?",
                  "Yes. <a href=\"beginner-coaching.html\">Beginner lessons</a>, <a href=\"get-into-golf.html\">Get Into Golf</a> and junior sessions all provide clubs, and club hire on the range and simulators is included at no extra cost. You only need comfortable clothing and flat shoes."),
                 ("Is there parking at the academy?",
                  "Yes, free parking directly outside the driving range and teaching studio, so you can park and walk straight to your bay without carrying a bag across a car park."),
                 (f"Do you coach complete beginners from {L}?",
                  f"Yes. A lot of golfers who come to us from {L} have never held a club. <a href=\"beginner-coaching.html\">Beginner Coaching</a> and <a href=\"get-into-golf.html\">Get Into Golf</a> are both built for exactly that, and nobody is going to make you feel awkward about starting from zero."),
             ] + u["faqs"], "alt": True},
        ],
    }


PAGES = [location_page(r) for r in ROWS]
