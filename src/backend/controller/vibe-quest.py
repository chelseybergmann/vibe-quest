from flask import Flask, request
from src.backend.model.event import get_events_json

app = Flask(__name__)

@app.route("/events")
def get_events() -> List[Event]:
    """
    Gets events for a given location and date.
    :return: JSON of events
    """
    mood = request.args.get("mood")
    location = request.args.get("location")
    date = request.args.get("date")

    return get_events_json(mood, location, date)

if __name__ == "__main__":
    app.run()