from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.score_distribution import ScoreDistributionResponse


router = APIRouter(
    prefix="/api/score-distribution",
    tags=["Score Distribution"]
)


@router.get("/", response_model=list[ScoreDistributionResponse])
def get_score_distribution(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.score_distribution
        ORDER BY score
    """)

    result = db.execute(query)

    rows = result.fetchall()

    return [
        {
            "score": row.score,
            "review_count": row.review_count
        }
        for row in rows
    ]