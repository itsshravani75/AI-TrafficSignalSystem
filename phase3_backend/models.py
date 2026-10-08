from database import db


class TrafficRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    north_count = db.Column(db.Integer, default=0)
    south_count = db.Column(db.Integer, default=0)
    east_count = db.Column(db.Integer, default=0)
    west_count = db.Column(db.Integer, default=0)

    north_waiting = db.Column(db.Float, default=0)
    south_waiting = db.Column(db.Float, default=0)
    east_waiting = db.Column(db.Float, default=0)
    west_waiting = db.Column(db.Float, default=0)

    next_green = db.Column(db.String(20))

    north_green_time = db.Column(db.Integer, default=0)
    south_green_time = db.Column(db.Integer, default=0)
    east_green_time = db.Column(db.Integer, default=0)
    west_green_time = db.Column(db.Integer, default=0)