from transformers import pipeline

# Sentiment Analysis Pipeline
sentiment_pipeline = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Simple Text Generation Pipeline
generator_pipeline = pipeline(
    task="text-generation",
    model="gpt2"
)


def analyze_review(review: str):

    result = sentiment_pipeline(review)

    return result


def summarize_review(review: str):

    prompt = f"Summarize this movie review briefly: {review}"

    result = generator_pipeline(
        prompt,
        max_new_tokens=40
    )

    return result