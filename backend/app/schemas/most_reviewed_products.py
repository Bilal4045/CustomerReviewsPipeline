from pydantic import BaseModel


class MostReviewedProductResponse(BaseModel):
    product_id: str
    review_count: int
    avg_score: float