from flask import render_template, request
from app import app
from models.event_planner import events, add_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods={"POST"})
def add_task():
    date = request.form["event_date"]
    event_name=request.form["event_name"]
    num_guests=request.form["num_of_guests"]
    location=request.form["location"]
    description=request.form["description"]
    new_event = Event(date, event_name, num_guests, location, description)
    add_event(new_event)
    return render_template('index.html', title="Home", events=events)