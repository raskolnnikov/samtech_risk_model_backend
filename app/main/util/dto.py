from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'public_id': fields.String(description='user Identifier'),
        'email': fields.String(required=True, description='user email address'),
        'org': fields.String(required=True, description='user organization'),
        'admin': fields.Boolean(default=False),
        'active': fields.Boolean(default=True),
        'password': fields.String(description='user password'),
        'registered_on': fields.DateTime(description='user Identifier')
    })

class RankingEntryDto:
    api = Namespace('ranking_entry', description='An entry with the predictions for a given patent.')
    ranking_entry = api.model('entry_details', {
        'patente': fields.String(),
        'step_id_week': fields.Integer(),
        'starting_date': fields.Date(),
        'predicted_relevance': fields.Float(),
        'predicted_rank': fields.Integer(),
        'previous_rank': fields.Integer(),
        'ten_day_mean_speed' : fields.Float(),
        'ten_day_pre_alert_low_count'  : fields.Float(),
        'ten_day_pre_alert_mid_count' : fields.Float(),
        'ten_day_pre_alert_high_count' : fields.Float(),
        'ten_day_alert_low_count'  : fields.Float(),
        'ten_day_alert_mid_count'  : fields.Float(),
        'ten_day_alert_high_count' : fields.Float(),
        'ten_day_sum_distance' : fields.Float(),
        'instance_json': fields.String(),
    })

class DetallePatenteDiaDto:
    api = Namespace('historic_details', description='Patente related operations')
    detail = api.model('patente_detail', {
    'date' : fields.DateTime(),
    'step_id_day' : fields.Integer(),
    'step_id_week' : fields.Integer(),
    'patente' : fields.String(),
    'sum_distance' : fields.Float(),
    'min_distance' : fields.Float(),
    'max_distance' : fields.Float(),
    'mean_distance' : fields.Float(),
    'std_distance' : fields.Float(),
    'min_speed' : fields.Float(),
    'max_speed' : fields.Float(),
    'mean_speed' : fields.Float(),
    'std_speed' : fields.Float(),
    'prealert_low_count' : fields.Integer(),
    'prealert_mid_count' : fields.Integer(),
    'prealert_high_count' : fields.Integer(),
    'alert_low_count' : fields.Integer(),
    'alert_mid_count' : fields.Integer(),
    'alert_high_count' : fields.Integer(),
    'alert_speed_limit_low_count' : fields.Integer(),
    'alert_speed_limit_mid_count' : fields.Integer(),
    'alert_speed_limit_high_count' : fields.Integer(),
    'no_alert_flag' : fields.Boolean(),
    'risk_index' : fields.Float(),
    'risk_index_w' : fields.Float(),
    'pre_alert_count_by_100km' : fields.Integer(),
    'alert_count_by_100km' : fields.Integer(),
    'speed_limit_alert_count_by_100km' : fields.Integer(),
    'mixed_alert_count_by_100km' : fields.Integer(),
    'no_alert_count_by_100km' : fields.Integer(),
    'max_speed_over_weekly_max' : fields.Float(),
    'speed_departure_from_weekly_mean' : fields.Float(),
    'std_speed_departure_from_weekly_mean' : fields.Float(),
    'pre_alert_count_by_100km_departure_from_weekly_mean' : fields.Float(),
    'alert_count_by_100km_departure_from_weekly_mean' : fields.Float(),
    'speed_limit_alert_count_by_100km_departure_from_weekly_mean' : fields.Float(),
    'mixed_alert_count_by_100km_departure_from_weekly_mean' : fields.Float(),
    'dt_dayofweek0' : fields.Boolean(),
    'dt_dayofweek1' : fields.Boolean(),
    'dt_dayofweek2' : fields.Boolean(),
    'dt_dayofweek3' : fields.Boolean(),
    'dt_dayofweek4' : fields.Boolean(),
    'dt_dayofweek5' : fields.Boolean(),
    'dt_dayofweek6' : fields.Boolean(),
    'dt_month1' : fields.Boolean(),
    'dt_month2' : fields.Boolean(),
    'dt_month3' : fields.Boolean(),
    'dt_month4' : fields.Boolean(),
    'dt_month5' : fields.Boolean(),
    'dt_month6' : fields.Boolean(),
    'dt_month7' : fields.Boolean(),
    'dt_month8' : fields.Boolean(),
    'dt_month9' : fields.Boolean(),
    'dt_month10' : fields.Boolean(),
    'dt_month11' : fields.Boolean(),
    'dt_month12' : fields.Boolean()
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
