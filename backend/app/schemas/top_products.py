from pydantic import BaseModel


class TopProductsResponse(BaseModel):
    product_id: str
    review_count: int
    avg_score: float