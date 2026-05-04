from fastapi import FastAPI
from pydantic import BaseModel

from services.review_service import (
    analyze_review,
    summarize_review
)

app = FastAPI(
    title="CineMind AI",
    description="AI-Powered Narrative Intelligence Platform",
    version="1.0.0"
)


class ReviewRequest(BaseModel):
    review: str


@app.get("/")
def root():

    return {
        "message": "Welcome to CineMind AI"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


@app.post("/analyze-review")
def analyze_movie_review(data: ReviewRequest):

    result = analyze_review(data.review)

    return {
        "analysis": result
    }


@app.post("/summarize-review")
def summarize_movie_review(data: ReviewRequest):

    result = summarize_review(data.review)

    return {
        "summary": result
    }