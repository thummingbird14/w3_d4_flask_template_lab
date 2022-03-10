from models.event import Event

event_1 = Event("11/03/2022", "Trnsmt", 1000, "Glasgow Green", "Large party festival")
event_2 = Event("12/03/2022", "Smith-Eyre Wedding", 250, "Ballroom", "Big Wedding")

events=[event_1, event_2]

def add_event(new_event):
    events.append(new_event)