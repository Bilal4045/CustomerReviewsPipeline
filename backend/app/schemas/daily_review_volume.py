from pydantic import BaseModel
from datetime import date


class DailyReviewVolumeResponse(BaseModel):
    review_date: date
    review_count: int