import caldav

client = caldav.DAVClient(
    "webcal://p23-caldav.icloud.com/published/2/MTk0OTIyNTMwMTE5NDkyMuTKq-XsPS_631omiGpPcTkYqQBKql0h9pQ-R83bKYFV2ajH6QugaNBDTv1snD50pnt6yEet0Zy3cJ1IH-2bB1A",

)
principal = client.principal()
for calendar in principal.calendars():
    for event in calendar.events():
        ical_text = event.data
