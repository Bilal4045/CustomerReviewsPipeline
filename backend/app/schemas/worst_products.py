from pydantic import BaseModel


class WorstProductResponse(BaseModel):
    product_id: str
    review_count: int
    avg_score: float