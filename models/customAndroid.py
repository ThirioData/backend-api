from db import db

class CustomAndroidModel(db.Model):
    __tablename__ = "andoidModel"
    and_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mobileno = db.Column(db.String(11))
    steps = db.Column(db.String(300))
    timestamp = db.Column(db.String(100))

    def __init__(self, mobileno, steps, timestamp):
        self.mobileno = mobileno
        self.steps = steps
        self.timestamp = timestamp

    def json(self):
        return {
            "mobileno": self.mobileno,
            "steps": self.steps,
            "timestamp": self.timestamp
        }

    @classmethod
    def find_by_id(cls, mobileno):
        return cls.query.filter_by(mobileno=mobileno).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
