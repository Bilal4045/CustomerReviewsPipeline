from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.most_reviewed_products import MostReviewedProductResponse


router = APIRouter(
    prefix="/api/most_reviewed_products",
    tags=["Most Reviewed Products"]
)


@router.get("/", response_model=list[MostReviewedProductResponse])
def get_most_reviewed_products(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.most_reviewed_products
        ORDER BY review_count DESC
    """)

    result = db.execute(query)
    rows = result.fetchall()

    return [
        {
            "product_id": row.product_id,
            "review_count": row.review_count,
            "avg_score": float(row.avg_score)
        }
        for row in rows
    ]