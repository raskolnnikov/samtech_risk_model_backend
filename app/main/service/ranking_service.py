import uuid
import datetime
from sqlalchemy import func

from app.main import db
from app.main.model.ranking import RankingEntry


def get_latest_ranking_list():
    max_week = db.session.query(func.max(RankingEntry.step_id_week)).scalar()
    return RankingEntry.query.filter_by(step_id_week=max_week).order_by(RankingEntry.predicted_rank.asc()).limit(100).all(), 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()
