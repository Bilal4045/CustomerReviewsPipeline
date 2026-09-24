from pydantic import BaseModel


class ScoreDistributionResponse(BaseModel):
    score: int
    review_count: int