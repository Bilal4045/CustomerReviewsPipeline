from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.top_reviewers import TopReviewerResponse


router = APIRouter(
    prefix="/api/top_reviewers",
    tags=["Top Reviewers"]
)


@router.get("/", response_model=list[TopReviewerResponse])
def get_top_reviewers(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.top_reviewers
        ORDER BY review_count DESC
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "user_id": row.user_id,
            "profile_name": row.profile_name,
            "review_count": row.review_count,
            "avg_score_given": float(row.avg_score_given)
        }
        for row in rows
    ]