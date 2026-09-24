from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.most_helpful_reviews import MostHelpfulReviewResponse


router = APIRouter(
    prefix="/api/most_helpful_reviews",
    tags=["Most Helpful Reviews"]
)


@router.get("/", response_model=list[MostHelpfulReviewResponse])
def get_most_helpful_reviews(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.most_helpful_reviews
        ORDER BY helpfulness_ratio DESC
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "id": row.id,
            "product_id": row.product_id,
            "user_id": row.user_id,
            "profile_name": row.profile_name,
            "score": float(row.score),
            "helpfulness_numerator": row.helpfulness_numerator,
            "helpfulness_denominator": row.helpfulness_denominator,
            "helpfulness_ratio": float(row.helpfulness_ratio),
            "summary": row.summary
        }
        for row in rows
    ]