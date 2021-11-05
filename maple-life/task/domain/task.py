from app import db


class Task(db.Model):
    task_id = db.Column(db.BIGINT, primary_key=True)
    task_title = db.Column(db.String(300))
    expected_time = db.Column(db.Numeric(3, 1))
    status = db.Column(db.String(50))
    icon = db.Column(db.String(50))

    user = db.relationship("User", backref=db.backref("tasks"))
    user_id = db.Column(db.BIGINT, db.ForeignKey("user.user_id", ondelete="CASCADE"))

    def find_by_id(task_id):
        return Task.query.get(task_id)

    def find_all_by_user_id(user_id):
        return Task.query.filter_by(user_id=user_id).all()
