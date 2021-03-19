
from .. import db, flask_bcrypt
import datetime
from ..config import key
import jwt
from sqlalchemy import func, and_


class RankingEntry(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "weekly_ranking_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patente = db.Column(db.String)
    step_id_week = db.Column(db.Integer)
    predicted_relevance = db.Column(db.Float)
    predicted_rank = db.Column(db.Integer)
    ten_day_mean_speed = db.Column(db.Float)
    ten_day_pre_alert_low_count  = db.Column(db.Float)
    ten_day_pre_alert_mid_count  = db.Column(db.Float)
    ten_day_pre_alert_high_count = db.Column(db.Float)
    ten_day_alert_low_count  = db.Column(db.Float)
    ten_day_alert_mid_count  = db.Column(db.Float)
    ten_day_alert_high_count  = db.Column(db.Float)
    ten_day_sum_distance = db.Column(db.Float)
    instance_json =  db.Column(db.String)

    @property
    def starting_date(self):
        week_id = str(self.step_id_week)
        r = datetime.datetime.strptime(week_id + '-1', "%Y%W-%w")
        return r

    @property
    def previous_rank(self):
        max_week = int(db.session.query(func.max(RankingEntry.step_id_week)).scalar())
        try:
            prev_rank = RankingEntry.query.filter(
                    RankingEntry.step_id_week < max_week,
                    RankingEntry.patente==self.patente
            ).one().predicted_rank
        except:
            prev_rank = 0
        return prev_rank

    def __repr__(self):
        return "<Patente '{}' | Date '{}' | Rank '{}'>".format(self.patente, self.date, self.predicted_rank)
