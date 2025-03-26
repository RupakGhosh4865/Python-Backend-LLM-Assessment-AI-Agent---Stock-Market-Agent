from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import os
from dotenv import load_dotenv
from utils.stock_price import fetch_stock_price
from utils.sentiment import get_stock_sentiment

load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define tools
def get_stock_info(ticker):
    """Fetch stock information"""
    return fetch_stock_price(ticker)

def get_sentiment_info(ticker):
    """Get sentiment analysis"""
    return get_stock_sentiment(ticker)

# Create tools
tools = [
    Tool(
        name="Stock Price Tool",
        func=get_stock_info,
        description="Fetches current stock price and historical data for a given ticker symbol"
    ),
    Tool(
        name="Sentiment Analysis Tool",
        func=get_sentiment_info,
        description="Analyzes market sentiment for a given stock ticker"
    )
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def analyze_stock(ticker):
    """
    Analyze a stock and provide recommendations
    """
    try:
        # Get stock price data
        price_data = fetch_stock_price(ticker)
        if "error" in price_data:
            return {"error": price_data["error"]}
        
        # Get sentiment data
        sentiment_data = get_stock_sentiment(ticker)
        
        # Generate recommendation based on price and sentiment
        recommendation = generate_recommendation(price_data, sentiment_data)
        
        return {
            "stock": ticker,
            "current_price": price_data["price"],
            "trend": price_data["trend"],
            "sentiment_score": sentiment_data["score"],
            "sentiment_confidence": sentiment_data["confidence"],
            "recommendation": recommendation,
            "price_data": {
                "high": price_data["high"],
                "low": price_data["low"],
                "volume": price_data["volume"]
            }
        }
        
    except Exception as e:
        return {"error": str(e)}

def generate_recommendation(price_data, sentiment_data):
    """
    Generate buy/sell/hold recommendation based on price and sentiment
    """
    if price_data["trend"] == "up" and sentiment_data["score"] >= 7:
        return "BUY"
    elif price_data["trend"] == "down" and sentiment_data["score"] <= 3:
        return "SELL"
    else:
        return "HOLD" 