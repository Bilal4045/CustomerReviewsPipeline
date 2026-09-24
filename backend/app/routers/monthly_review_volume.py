from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.monthly_review_volume import MonthlyReviewVolumeResponse


router = APIRouter(
    prefix="/api/monthly_review_volume",
    tags=["Monthly Review Volume"]
)


@router.get("/", response_model=list[MonthlyReviewVolumeResponse])
def get_monthly_review_volume(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.monthly_review_volume
        ORDER BY review_month
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "review_month": row.review_month,
            "review_count": row.review_count,
            "avg_score": float(row.avg_score)
        }
        for row in rows
    ]