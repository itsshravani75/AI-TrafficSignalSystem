from flask import Flask, jsonify, request
from database import db
from models import TrafficRecord


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///traffic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify({
        "message": "AI Traffic Signal Optimization Backend is Running"
    })


@app.route("/api/traffic")
def get_traffic():
    records = TrafficRecord.query.order_by(
        TrafficRecord.id.desc()
    ).all()

    data = []

    for record in records:
        data.append({
            "id": record.id,

            "vehicle_counts": {
                "NORTH": record.north_count,
                "SOUTH": record.south_count,
                "EAST": record.east_count,
                "WEST": record.west_count
            },

            "waiting_times": {
                "NORTH": record.north_waiting,
                "SOUTH": record.south_waiting,
                "EAST": record.east_waiting,
                "WEST": record.west_waiting
            },

            "next_green": record.next_green,

            "green_times": {
                "NORTH": record.north_green_time,
                "SOUTH": record.south_green_time,
                "EAST": record.east_green_time,
                "WEST": record.west_green_time
            }
        })

    return jsonify(data)

@app.route("/api/traffic", methods=["POST"])
def save_traffic():
    data = request.get_json()

    record = TrafficRecord(
        north_count=data.get("vehicle_counts", {}).get("NORTH", 0),
        south_count=data.get("vehicle_counts", {}).get("SOUTH", 0),
        east_count=data.get("vehicle_counts", {}).get("EAST", 0),
        west_count=data.get("vehicle_counts", {}).get("WEST", 0),

        north_waiting=data.get("waiting_times", {}).get("NORTH", 0),
        south_waiting=data.get("waiting_times", {}).get("SOUTH", 0),
        east_waiting=data.get("waiting_times", {}).get("EAST", 0),
        west_waiting=data.get("waiting_times", {}).get("WEST", 0),

        next_green=data.get("next_green"),

        north_green_time=data.get("green_times", {}).get("NORTH", 0),
        south_green_time=data.get("green_times", {}).get("SOUTH", 0),
        east_green_time=data.get("green_times", {}).get("EAST", 0),
        west_green_time=data.get("green_times", {}).get("WEST", 0)
    )

    db.session.add(record)
    db.session.commit()

    return jsonify({
        "message": "Traffic data saved successfully",
        "id": record.id
    }), 201

if __name__ == "__main__":
    app.run(debug=True)