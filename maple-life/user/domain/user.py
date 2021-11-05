from common.database import db


class User(db.Model):
    user_id = db.Column(db.BIGINT, primary_key=True)
    email = db.Column(db.String(320))
    username = db.Column(db.String(150))
    hashed_password = db.Column(db.String(100))
    accumulated_task_time = db.Column(db.Numeric(10, 1))

    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    def find_by_id(user_id):
        return User.query.get(user_id)
