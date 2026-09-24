from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.database import get_db
from app.schemas.worst_products import WorstProductResponse


router = APIRouter(
    prefix="/api/worst_products",
    tags=["Worst Products"]
)


@router.get("/", response_model=list[WorstProductResponse])
def get_worst_products(db: Session = Depends(get_db)):

    query = text("""
        SELECT *
        FROM marts.worst_products
        ORDER BY avg_score
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