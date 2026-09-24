from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.top_products import TopProductsResponse


router = APIRouter(
    prefix="/api/top_products",
    tags=["Top Products"]
)


@router.get("/", response_model=list[TopProductsResponse])
def get_top_products(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.top_products
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