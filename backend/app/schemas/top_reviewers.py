from pydantic import BaseModel


class TopReviewerResponse(BaseModel):
    user_id: str
    profile_name: str
    review_count: int
    avg_score_given: float