from pydantic import BaseModel


class MostHelpfulReviewResponse(BaseModel):
    id: int
    product_id: str
    user_id: str
    profile_name: str
    score: float
    helpfulness_numerator: int
    helpfulness_denominator: int
    helpfulness_ratio: float
    summary: str