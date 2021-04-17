
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
    geo_fence_0 = db.Column(db.Integer)
    geo_fence_1 = db.Column(db.Integer)
    geo_fence_2 = db.Column(db.Integer)
    geo_fence_3 = db.Column(db.Integer)
    geo_fence_4 = db.Column(db.Integer)
    geo_fence_5 = db.Column(db.Integer)
    geo_fence_6 = db.Column(db.Integer)
    geo_fence_7 = db.Column(db.Integer)
    geo_fence_8 = db.Column(db.Integer)
    geo_fence_9 = db.Column(db.Integer)
    geo_fence_10 = db.Column(db.Integer)
    geo_fence_11 = db.Column(db.Integer)
    geo_fence_12 = db.Column(db.Integer)
    geo_fence_13 = db.Column(db.Integer)
    geo_fence_14 = db.Column(db.Integer)
    geo_fence_15 = db.Column(db.Integer)
    geo_fence_16 = db.Column(db.Integer)
    geo_fence_17 = db.Column(db.Integer)
    geo_fence_18 = db.Column(db.Integer)
    geo_fence_19 = db.Column(db.Integer)
    geo_fence_20 = db.Column(db.Integer)
    geo_fence_21 = db.Column(db.Integer)
    geo_fence_22 = db.Column(db.Integer)
    geo_fence_23 = db.Column(db.Integer)
    geo_fence_24 = db.Column(db.Integer)
    geo_fence_25 = db.Column(db.Integer)
    geo_fence_26 = db.Column(db.Integer)
    geo_fence_27 = db.Column(db.Integer)
    geo_fence_28 = db.Column(db.Integer)
    geo_fence_29 = db.Column(db.Integer)
    geo_fence_30 = db.Column(db.Integer)
    geo_fence_31 = db.Column(db.Integer)
    geo_fence_32 = db.Column(db.Integer)
    geo_fence_33 = db.Column(db.Integer)
    geo_fence_34 = db.Column(db.Integer)
    geo_fence_35 = db.Column(db.Integer)
    geo_fence_36 = db.Column(db.Integer)
    geo_fence_37 = db.Column(db.Integer)
    geo_fence_38 = db.Column(db.Integer)
    geo_fence_39 = db.Column(db.Integer)
    geo_fence_40 = db.Column(db.Integer)
    geo_fence_41 = db.Column(db.Integer)
    geo_fence_42 = db.Column(db.Integer)
    geo_fence_43 = db.Column(db.Integer)
    geo_fence_44 = db.Column(db.Integer)
    geo_fence_45 = db.Column(db.Integer)
    geo_fence_46 = db.Column(db.Integer)
    geo_fence_47 = db.Column(db.Integer)
    geo_fence_48 = db.Column(db.Integer)
    geo_fence_49 = db.Column(db.Integer)
    geo_fence_50 = db.Column(db.Integer)
    geo_fence_51 = db.Column(db.Integer)
    geo_fence_52 = db.Column(db.Integer)
    geo_fence_53 = db.Column(db.Integer)
    geo_fence_54 = db.Column(db.Integer)
    geo_fence_55 = db.Column(db.Integer)
    geo_fence_56 = db.Column(db.Integer)
    geo_fence_57 = db.Column(db.Integer)
    geo_fence_58 = db.Column(db.Integer)
    geo_fence_59 = db.Column(db.Integer)


    @property
    def starting_date(self):
        week_id = str(self.step_id_week)
        r = datetime.datetime.strptime(week_id + '-1', "%Y%W-%w")
        return r

    @property
    def previous_rank(self):
        max_week = int(db.session.query(func.max(RankingEntry.step_id_week)).scalar())
        try:
            prev_rank = RankingEntry.query.filter(RankingEntry.patente==self.patente).filter(RankingEntry.step_id_week < max_week).order_by(RankingEntry.step_id_week.desc()).first().predicted_rank
        except Exception as e:
            prev_rank = 100
        return prev_rank

    def __repr__(self):
        return "<Patente '{}' | Date '{}' | Rank '{}'>".format(self.patente, self.date, self.predicted_rank)
