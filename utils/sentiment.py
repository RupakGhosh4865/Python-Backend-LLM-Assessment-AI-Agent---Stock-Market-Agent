import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(text):
    """
    Analyze sentiment of text using OpenAI's GPT model
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis expert. Analyze the sentiment of the following text and return a score between 1-10, where 1 is very negative and 10 is very positive."},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
            max_tokens=50
        )
        
        # Extract the score from the response
        score = int(response.choices[0].message.content.strip())
        return max(1, min(10, score))  # Ensure score is between 1-10
        
    except Exception as e:
        print(f"Error in sentiment analysis: {str(e)}")
        return 5  # Neutral score in case of error

def get_stock_sentiment(ticker):
    """
    Get sentiment analysis for a stock ticker
    """
    # This is a placeholder - in a real application, you would:
    # 1. Fetch news articles about the stock
    # 2. Extract relevant text
    # 3. Analyze sentiment
    # For now, we'll return a simulated sentiment
    return {
        "score": 7,
        "confidence": 0.85,
        "summary": "Positive market sentiment"
    } 