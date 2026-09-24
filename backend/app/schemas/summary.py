from pydantic import BaseModel
from datetime import date


class SummaryResponse(BaseModel):
    total_reviews: int
    total_products: int
    total_users: int
    overall_avg_score: float
    earliest_review: date
    latest_review: date