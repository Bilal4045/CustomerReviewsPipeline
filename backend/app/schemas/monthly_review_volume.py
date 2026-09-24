from pydantic import BaseModel
from datetime import date


class MonthlyReviewVolumeResponse(BaseModel):
    review_month: date
    review_count: int
    avg_score: float