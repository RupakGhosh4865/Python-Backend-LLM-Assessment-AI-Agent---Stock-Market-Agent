# 📈 Stock Market AI Agent

An AI-powered agent that analyzes stocks and provides buy/sell/hold recommendations based on real-time price data and sentiment analysis.

## Features

- Real-time stock price data using yfinance
- Sentiment analysis using OpenAI's GPT model
- Buy/Sell/Hold recommendations
- RESTful API with FastAPI
- CORS support for web applications

## Prerequisites

- Python 3.8+
- OpenAI API key
- Internet connection for stock data and API calls

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd stock_market_agent
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8000`

3. Access the API documentation at `http://localhost:8000/docs`

4. Analyze a stock by making a GET request to:
```
http://localhost:8000/analyze/{ticker}
```
Example: `http://localhost:8000/analyze/AAPL`

## API Response Example

```json
{
    "stock": "AAPL",
    "current_price": 175.50,
    "trend": "up",
    "sentiment_score": 7,
    "sentiment_confidence": 0.85,
    "recommendation": "BUY",
    "price_data": {
        "high": 176.20,
        "low": 174.80,
        "volume": 75000000
    }
}
```

## Project Structure

```
stock_market_agent/
├── main.py               # FastAPI server
├── agent.py             # AI agent implementation
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── utils/
    ├── stock_price.py  # Stock price fetching utility
    └── sentiment.py    # Sentiment analysis utility
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This project is for educational purposes only. The stock market recommendations provided by this agent should not be considered as financial advice. Always do your own research and consult with financial advisors before making investment decisions. 