from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.daily_review_volume import DailyReviewVolumeResponse


router = APIRouter(
    prefix="/api/daily_review_volume",
    tags=["Daily Review Volume"]
)


@router.get("/", response_model=list[DailyReviewVolumeResponse])
def get_daily_review_volume(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.daily_review_volume
        ORDER BY review_date
    """)

    result = db.execute(query)

    rows = result.fetchall()

    return [
        {
            "review_date": row.review_date,
            "review_count": row.review_count
        }
        for row in rows
    ]