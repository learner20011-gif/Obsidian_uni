

## **LLM Inputs**

The repository inputs the following data types to the LLM:

### **1. Market Data**
```python
- Symbol list (e.g., ['AAPL', 'GOOGL', 'TSLA'])
- Price data (open, close, volume)
- Market volatility metrics
- Date ranges and historical prices
- Technical indicators
```

### **2. Sentiment Data**
```python
- Sentiment scores from news articles
- Social media posts and engagement metrics
- Sentiment sources (Twitter, Reddit, news outlets)
- Sentiment trends (positive/negative/neutral)
- Recency-weighted sentiment scores
```

### **3. Portfolio Data**
```python
- Current positions and weights
- Portfolio total value
- Cash available
- Risk levels
- Position adjustments needed
```

### **4. Factor Scores**
```python
- Sentiment momentum
- Sentiment volatility
- News volume
- Social media volume
- Sentiment consensus
```

### **5. News & Social Media Data**
```python
- News titles and content
- Article sources and timestamps
- Social media posts
- Platform information (Twitter, Reddit)
- Engagement metrics
```

---

## **Prompt Structure**

The system uses **4 main prompt templates**:

### **1. Market Analysis Prompt**
```python
Structure:
├── System Role: "You are an expert financial analyst"
├── Market Data Summary (statistics of prices)
└── Required Output Format:
    ├── Market trend analysis
    ├── Key technical levels
    ├── Potential catalysts
    ├── Risk factors
    └── Trading opportunities
    
JSON Response Format:
{
    "trend": "...",
    "levels": "...",
    "catalysts": "...",
    "risks": "...",
    "opportunities": "..."
}
```

### **2. Signal Generation Prompt**
```python
Structure:
├── System Role: "Quantitative trading strategist"
├── Factor Data (last 5 periods)
├── Price Data (last 5 periods)
├── Strategy Context
└── Required Output Format (JSON):
    ├── signal_type: 'buy'/'sell'/'hold'
    ├── confidence: 0-1
    ├── reasoning: explanation
    ├── target_price
    └── stop_loss
```

### **3. Risk Assessment Prompt**
```python
Structure:
├── System Role: "Risk management expert"
├── Portfolio Data (JSON)
├── Market Conditions (JSON)
└── Required Output Format (JSON):
    ├── overall_risk: 'low'/'medium'/'high'
    ├── risk_factors: [list]
    ├── recommendations: [list]
    └── position_adjustments: [list]
```

### **4. Portfolio Optimization Prompt**
```python
Structure:
├── System Role: "Portfolio optimization specialist"
├── Current Weights (JSON)
├── Factor Scores (JSON)
├── Constraints (JSON)
└── Required Output Format (JSON):
    ├── suggested_weights: {...}
    ├── expected_return: float
    ├── risk_level: string
    └── rebalancing_actions: [list]
```

### **5. Strategy Recommendation Prompt** (from LangChainAgent)
```python
Structure:
├── System Role: "Expert quantitative trading strategist"
├── Market Data Summary
│   ├── Symbols
│   ├── Data points
│   ├── Date range
│   └── Price volatility
├── Sentiment Summary
│   ├── Average sentiment score
│   ├── Number of sources
│   └── Trend direction
├── Portfolio Summary
│   ├── Total value
│   ├── Cash
│   ├── Number of positions
│   └── Current risk level
└── Required Output Format (JSON):
    ├── strategy_name: string
    ├── description: string
    ├── symbols: [list]
    ├── signal: 'buy'/'sell'/'hold'
    ├── confidence: 0.0-1.0
    ├── reasoning: string
    ├── parameters: {lookback_period, position_size, stop_loss, take_profit}
    ├── risk_level: 'low'/'medium'/'high'
    ├── expected_return: 0.0-1.0
    └── time_horizon: 'short'/'medium'/'long'
```

---

## **LLM Output Structure**

All outputs are designed to be **JSON-formatted** for machine parsing:

```python
Response Structure (TradingInsight):
├── insight_type: 'signal'/'analysis'/'recommendation'/'risk_warning'
├── content: str (main response)
├── confidence: 0-1 (confidence score)
├── symbols: [list] (relevant tickers)
├── timeframe: str (current/short/medium/long)
├── reasoning: str (explanation)
├── timestamp: datetime
├── tokens_used: int
├── cost: float
└── metadata: dict
```

---

## **LLM Providers Supported**

```python
1. **OpenAI** (GPT-3.5-turbo, GPT-4)
   - System prompt included
   - Temperature: 0.3 (low randomness for trading)
   - Max tokens: 1000

2. **Local Models** (DialoGPT-medium)
   - Max tokens: 200
   - Temperature: 0.7
   - No API dependency
```

The system is designed to provide comprehensive trading insights by combining multiple data streams into structured prompts that generate actionable, JSON-formatted responses.