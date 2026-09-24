from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.summary import SummaryResponse


router = APIRouter(
    prefix="/api/summary",
    tags=["Summary"]
)


@router.get("/", response_model=SummaryResponse)
def get_summary(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.summary_stats
    """)

    result = db.execute(query)
    row = result.fetchone()

    return {
        "total_reviews": row.total_reviews,
        "total_products": row.total_products,
        "total_users": row.total_users,
        "overall_avg_score": float(row.overall_avg_score),
        "earliest_review": row.earliest_review,
        "latest_review": row.latest_review
    }