"""Trip data for Rihla. All text, prices and contact details are dummy data."""
from datetime import date, timedelta
from itertools import zip_longest

TRIPS = [
    {
        "slug": "desert-safari-adventure",
        "name": "Desert Safari Adventure",
        "image": "desert-safari.jpg",
        "description": "Dune bashing, camel rides, and a BBQ dinner under the stars",
        "tagline": "Golden dunes, a desert sunset and dinner under the stars",
        "price": "AED 250",
        "price_unit": "per person",
        "capacity": 20,
        "location": "Al Marmoom Desert, Dubai, UAE",
        "location_name": "Al Marmoom Desert Conservation Reserve",
        "location_text": (
            "The reserve is a protected area about 45 minutes by road from central Dubai. "
            "It is quiet and open, and it is home to Arabian oryx and sand gazelles. "
            "Our camp sits between the dunes, far from the main roads."
        ),
        "meeting_point": (
            "Free pickup from hotels in Dubai city. Guests who drive themselves meet at "
            "the desert camp, and we send the exact pin by WhatsApp."
        ),
        "map_query": "Al Marmoom Desert Conservation Reserve, Dubai",
        "facts": [
            ("Duration", "6 hours"),
            ("Group size", "Up to 20 guests"),
            ("Languages", "English and Arabic"),
            ("Pickup", "From 3:00 PM, free"),
        ],
        "intro": [
            "Leave the city behind and head into the golden dunes of the Al Marmoom Desert "
            "Conservation Reserve. An experienced local driver takes you over the sand in a "
            "4x4, then you stop to watch the sun go down behind the dunes.",
            "After sunset the camp opens for dinner. Enjoy a BBQ, live music and a Tanoura "
            "dance show. The trip is great for families, couples and groups of friends, and "
            "you do not need any experience.",
        ],
        "highlights": [
            "Dune driving in a 4x4 with an experienced local driver",
            "Camel ride and sandboarding",
            "Sunset photo stop on top of the dunes",
            "BBQ dinner with vegetarian options",
            "Tanoura show and live music",
        ],
        "itinerary": [
            ("3:00 PM", "Pickup from your hotel"),
            ("4:15 PM", "Dune driving and first photo stop"),
            ("5:45 PM", "Sunset, camel rides and sandboarding"),
            ("7:00 PM", "BBQ dinner at the camp"),
            ("8:00 PM", "Tanoura show and live music"),
            ("9:00 PM", "Drop off at your hotel"),
        ],
        "included": [
            "Return hotel pickup and drop off",
            "4x4 dune driving with a driver",
            "Camel ride and sandboarding",
            "BBQ dinner with soft drinks, tea and coffee",
            "Tanoura show and live music",
            "Bottled water and a cold towel",
        ],
        "excluded": [
            "Quad bike rides (extra cost)",
            "Alcoholic drinks",
            "Professional photos and video",
            "Tips for your driver and guides",
            "Travel insurance",
        ],
        "faq": [
            ("What should I wear?",
             "Wear light, comfortable clothes and closed shoes. The desert gets cool after "
             "sunset, so bring a light jacket from November to March."),
            ("Is the trip safe for children?",
             "Yes, children from 4 years old are welcome. The dune driving is bumpy, so we "
             "do not recommend the trip for pregnant guests or for anyone with back or neck "
             "problems."),
            ("Is the food halal? Is there vegetarian food?",
             "All meat is halal and there are vegetarian dishes every evening. Please tell "
             "us about any allergies when you book."),
            ("What happens if the weather is bad?",
             "If strong wind or a sandstorm stops the trip, you can choose a new date or get "
             "a full refund."),
            ("Can I cancel my booking?",
             "You can cancel for free up to 24 hours before pickup. After that we cannot "
             "refund the ticket."),
        ],
        "organizer": {
            "company": "Golden Dunes Tours",
            "contact_name": "Khalid Al Mansoori",
            "initials": "KM",
            "role": "Operations manager",
            "phone": "+971 4 000 0001",
            "whatsapp": "+971 50 000 0001",
            "email": "dunes@rihla.example",
            "hours": "Daily, 8:00 AM to 8:00 PM",
            "licence": "Tourism licence DET-000001 (dummy)",
        },
        "available_weekdays": [0, 1, 2, 3, 4, 5, 6],
        "seed": 3,
    },
    {
        "slug": "yacht-charter-experience",
        "name": "Yacht Charter Experience",
        "image": "yacht-charter.jpg",
        "description": "Cruise the marina in style aboard a private luxury yacht",
        "tagline": "Three hours on a private yacht with the Dubai skyline around you",
        "price": "AED 350",
        "price_unit": "per person",
        "capacity": 12,
        "location": "Dubai Marina, Dubai, UAE",
        "location_name": "Dubai Marina Yacht Club",
        "location_text": (
            "Dubai Marina is a waterfront district about 30 minutes by car from Downtown "
            "Dubai. The yacht leaves from the Yacht Club dock, which has easy parking and "
            "cafes close by."
        ),
        "meeting_point": (
            "Meet your captain at the Dubai Marina Yacht Club dock, 20 minutes before "
            "departure. Look for the yacht with the Rihla flag."
        ),
        "map_query": "Dubai Marina Yacht Club, Dubai",
        "facts": [
            ("Duration", "3 hours"),
            ("Group size", "Up to 12 guests"),
            ("Languages", "English and Arabic"),
            ("Departure", "10:00 AM, 2:00 PM or 5:00 PM"),
        ],
        "intro": [
            "Spend three relaxed hours on a private yacht. Your captain takes you past the "
            "towers of Dubai Marina and Jumeirah Beach Residence, then out into open water "
            "for views of the Palm Jumeirah, Atlantis and, on clear days, the Burj Al Arab.",
            "The whole yacht is only for your group. Swim from the back deck, enjoy fresh "
            "fruit and cold drinks, and take as many photos as you like. It is perfect for "
            "birthdays, small celebrations or a special day with friends and family.",
        ],
        "highlights": [
            "Private yacht just for your group",
            "Skyline views of the Marina, the Palm and Atlantis",
            "Swim stop in the open water",
            "Fresh fruit, snacks and cold drinks on board",
            "Professional captain and crew",
        ],
        "itinerary": [
            ("Start", "Welcome drink and safety briefing"),
            ("After 30 min", "Cruise through Dubai Marina and past the towers of JBR"),
            ("After 1 hour", "Open water views of the Palm Jumeirah and Atlantis"),
            ("After 2 hours", "Swim stop and snacks on deck"),
            ("After 3 hours", "Back at the dock"),
        ],
        "included": [
            "Private yacht with captain and crew",
            "Fuel and port fees",
            "Water, soft drinks and fresh fruit",
            "Snacks and a swim stop",
            "Towels and life jackets",
            "Bluetooth speaker for your music",
        ],
        "excluded": [
            "Catering menu (pre-order at extra cost)",
            "Alcoholic drinks",
            "Jet ski, fishing or other water sports",
            "Professional photographer",
            "Tips for the crew",
        ],
        "faq": [
            ("Is the yacht private?",
             "Yes. The whole yacht is only for your group, with up to 12 guests on board."),
            ("Can I bring my own food?",
             "You can bring light snacks and a cake for a celebration. We also offer a "
             "catering menu that you can pre-order at least 48 hours before."),
            ("Can I choose my departure time?",
             "Yes. Departures are at 10:00 AM, 2:00 PM and 5:00 PM. Send us your preferred "
             "time after you book and we will confirm it."),
            ("What if I get seasick?",
             "The water near the Marina is usually calm. If you are worried, take a "
             "seasickness tablet before you board and tell the captain, who can stay in "
             "sheltered water."),
            ("What is the cancellation policy?",
             "You can cancel for free up to 48 hours before departure. In bad weather we "
             "move your trip to another day at no cost."),
        ],
        "organizer": {
            "company": "Marina Blue Yachts",
            "contact_name": "Layla Haddad",
            "initials": "LH",
            "role": "Charter manager",
            "phone": "+971 4 000 0002",
            "whatsapp": "+971 50 000 0002",
            "email": "charter@rihla.example",
            "hours": "Daily, 9:00 AM to 9:00 PM",
            "licence": "Tourism licence DET-000002 (dummy)",
        },
        "available_weekdays": [2, 3, 4, 5, 6],
        "seed": 5,
    },
    {
        "slug": "dhow-cruise-dinner",
        "name": "Dhow Cruise Dinner",
        "image": "dhow-cruise.jpg",
        "description": "Sail Dubai Creek at sunset with a traditional dinner and live entertainment",
        "tagline": "Sail the old heart of Dubai on a traditional wooden dhow",
        "price": "AED 180",
        "price_unit": "per person",
        "capacity": 30,
        "location": "Dubai Creek, Dubai, UAE",
        "location_name": "Al Seef, Dubai Creek",
        "location_text": (
            "Dubai Creek is where the city began as a small trading and pearl diving port. "
            "The dhow leaves from the pier at Al Seef, a heritage waterfront in Bur Dubai "
            "with cafes and traditional shops."
        ),
        "meeting_point": (
            "Check in at the Al Seef dhow pier from 7:00 PM. Look for the Rihla sign next "
            "to the boarding steps."
        ),
        "map_query": "Al Seef, Dubai Creek, Dubai",
        "facts": [
            ("Duration", "2 hours"),
            ("Group size", "Up to 30 guests"),
            ("Languages", "English and Arabic"),
            ("Boarding", "7:30 PM, check in from 7:00 PM"),
        ],
        "intro": [
            "Step on board a traditional wooden dhow and sail along Dubai Creek, the old "
            "heart of the city. See the lights of the old souks on one side and the modern "
            "skyline on the other while a gentle breeze comes off the water.",
            "Dinner is a buffet of Arabic and international dishes, served while you sail. "
            "After dinner, relax with live music and entertainment on deck. It is a calm "
            "and friendly evening for couples, families and visitors who are new to Dubai.",
        ],
        "highlights": [
            "Traditional wooden dhow with an open upper deck",
            "Buffet dinner with Arabic and international dishes",
            "Live music and entertainment on board",
            "Views of Al Seef, the old souks and the Creek skyline",
            "Calm evening, good for all ages",
        ],
        "itinerary": [
            ("7:00 PM", "Check in at the Al Seef pier"),
            ("7:30 PM", "Welcome drink and boarding"),
            ("7:45 PM", "The dhow starts sailing along the Creek"),
            ("8:15 PM", "Buffet dinner is served"),
            ("9:00 PM", "Live entertainment on deck"),
            ("9:45 PM", "Back at the pier"),
        ],
        "included": [
            "Welcome drink with Arabic coffee and dates",
            "Halal buffet dinner",
            "Soft drinks, tea and coffee",
            "Live music and entertainment",
            "Seat on the air-conditioned lower deck",
            "Creek sightseeing for 2 hours",
        ],
        "excluded": [
            "Hotel pickup (available for an extra fee)",
            "Alcoholic drinks",
            "Upper deck seat upgrade",
            "Photos taken on board",
            "Tips for the crew",
        ],
        "faq": [
            ("Is there an air-conditioned area?",
             "Yes. The lower deck is air-conditioned and the upper deck is open air with a "
             "cool breeze from the water."),
            ("Can I choose the upper deck?",
             "You can ask for the upper deck when you book. Seats there are limited and we "
             "give them in the order of booking."),
            ("Are there vegetarian dishes?",
             "All food is halal and the buffet has vegetarian dishes. We can prepare special "
             "meals for allergies if you tell us 24 hours before."),
            ("Is there a dress code?",
             "Smart casual. Comfortable shoes are best because the boarding area has steps."),
            ("Is the dhow suitable for wheelchairs?",
             "Boarding is by steps and a narrow gangway, so access for wheelchairs is "
             "limited. Please contact us before you book and we will do our best to help."),
        ],
        "organizer": {
            "company": "Creek Heritage Cruises",
            "contact_name": "Omar Rahim",
            "initials": "OR",
            "role": "Guest relations",
            "phone": "+971 4 000 0003",
            "whatsapp": "+971 50 000 0003",
            "email": "creek@rihla.example",
            "hours": "Daily, 10:00 AM to 10:00 PM",
            "licence": "Tourism licence DET-000003 (dummy)",
        },
        "available_weekdays": [1, 2, 3, 4, 5, 6],
        "seed": 8,
    },
]


def availability_for(trip, horizon_days=75):
    """Dummy availability: {"2026-11-03": "available" or "limited", ...}.

    Only future days are returned. Some days are skipped so the calendar looks
    natural, and some are marked "limited" (few spots left). Replace this with
    real data later.
    """
    today = date.today()
    days = {}
    for offset in range(1, horizon_days + 1):
        day = today + timedelta(days=offset)
        if day.weekday() not in trip["available_weekdays"]:
            continue
        n = day.toordinal() + trip["seed"]
        if n % 9 == 0:  # looks like a fully booked day
            continue
        days[day.isoformat()] = "limited" if n % 5 == 0 else "available"
    return days


def include_rows(trip):
    """Pairs of (included, not included) for the comparison table."""
    return list(zip_longest(trip["included"], trip["excluded"], fillvalue=""))