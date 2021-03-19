
from .. import db, flask_bcrypt
import datetime
from ..config import key
import jwt


class DetallePatenteDia(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "detalle_patente_dia"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    step_id_day = db.Column(db.Integer)
    step_id_week = db.Column(db.Integer)
    patente = db.Column(db.String)
    sum_distance = db.Column(db.Float)
    min_distance = db.Column(db.Float)
    max_distance = db.Column(db.Float)
    mean_distance = db.Column(db.Float)
    std_distance = db.Column(db.Float)
    min_speed = db.Column(db.Float)
    max_speed = db.Column(db.Float)
    mean_speed = db.Column(db.Float)
    std_speed = db.Column(db.Float)
    prealert_low_count = db.Column(db.Integer)
    prealert_mid_count = db.Column(db.Integer)
    prealert_high_count = db.Column(db.Integer)
    alert_low_count = db.Column(db.Integer)
    alert_mid_count = db.Column(db.Integer)
    alert_high_count = db.Column(db.Integer)
    alert_speed_limit_low_count = db.Column(db.Integer)
    alert_speed_limit_mid_count = db.Column(db.Integer)
    alert_speed_limit_high_count = db.Column(db.Integer)
    no_alert_flag = db.Column(db.Boolean)
    risk_index = db.Column(db.Float)
    risk_index_w = db.Column(db.Float)
    pre_alert_count_by_100km = db.Column(db.Integer)
    alert_count_by_100km = db.Column(db.Integer)
    speed_limit_alert_count_by_100km = db.Column(db.Integer)
    mixed_alert_count_by_100km = db.Column(db.Integer)
    no_alert_count_by_100km = db.Column(db.Integer)
    max_speed_over_weekly_max = db.Column(db.Float)
    speed_departure_from_weekly_mean = db.Column(db.Float)
    std_speed_departure_from_weekly_mean = db.Column(db.Float)
    pre_alert_count_by_100km_departure_from_weekly_mean = db.Column(db.Float)
    alert_count_by_100km_departure_from_weekly_mean = db.Column(db.Float)
    speed_limit_alert_count_by_100km_departure_from_weekly_mean = db.Column(db.Float)
    mixed_alert_count_by_100km_departure_from_weekly_mean = db.Column(db.Float)
    dt_dayofweek0 = db.Column(db.Boolean)
    dt_dayofweek1 = db.Column(db.Boolean)
    dt_dayofweek2 = db.Column(db.Boolean)
    dt_dayofweek3 = db.Column(db.Boolean)
    dt_dayofweek4 = db.Column(db.Boolean)
    dt_dayofweek5 = db.Column(db.Boolean)
    dt_dayofweek6 = db.Column(db.Boolean)
    dt_month1 = db.Column(db.Boolean)
    dt_month2 = db.Column(db.Boolean)
    dt_month3 = db.Column(db.Boolean)
    dt_month4 = db.Column(db.Boolean)
    dt_month5 = db.Column(db.Boolean)
    dt_month6 = db.Column(db.Boolean)
    dt_month7 = db.Column(db.Boolean)
    dt_month8 = db.Column(db.Boolean)
    dt_month11 = db.Column(db.Boolean)
    dt_month12 = db.Column(db.Boolean)


    def __repr__(self):
        return "<Patente '{}' | Dia '{}'>".format(self.patente, self.step_id_day)
