from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import summary
from app.routers import score_distribution
from app.routers import daily_review_volume
from app.routers import monthly_review_volume
from app.routers import top_products
from app.routers import worst_products
from app.routers import most_reviewed_products
from app.routers import top_reviewers
from app.routers import most_helpful_reviews

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(summary.router)
app.include_router(score_distribution.router)
app.include_router(daily_review_volume.router)
app.include_router(monthly_review_volume.router)
app.include_router(top_products.router)
app.include_router(worst_products.router)
app.include_router(most_reviewed_products.router)
app.include_router(top_reviewers.router)
app.include_router(most_helpful_reviews.router)

@app.get("/")
def home():
    return {"message": "Customer Reviews API is running"}