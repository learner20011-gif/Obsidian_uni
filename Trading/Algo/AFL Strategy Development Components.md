## AmiBroker AFL: Strategy Development Components

---

### Built-in Technical Indicators

- **Moving Averages:** Simple (SMA), Exponential (EMA), Weighted (WMA), Double Exponential (DEMA), Triple Exponential (TEMA), Kaufman Adaptive (KAMA).
    
- **Momentum Oscillators:** Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), Stochastic Oscillator (StochK, StochD), Commodity Channel Index (CCI).
    
- **Trend Following:** Average Directional Index (ADX), Parabolic SAR (SAR), Aroon, Ichimoku Kinko Hyo.
    
- **Volatility Indicators:** Average True Range (ATR), Bollinger Bands (BBandBot, BBandTop), Standard Deviation (StDev), Keltner Channels.
    
- **Volume Indicators:** On-Balance Volume (OBV), Chaikin Money Flow (CMF), Volume Weighted Average Price (VWAP), Money Flow Index (MFI).
    

---

### Trading System Core Variables

- **Signal Arrays:** `Buy`, `Sell`, `Short`, `Cover` (used to trigger entries and exits).
    
- **Price Arrays:** `Open` (O), `High` (H), `Low` (L), `Close` (C), `Volume` (V), `OpenInterest` (OI).
    
- **Position Sizing:** `PositionSize` (allocates fixed capital or equity percentages), `PositionScore` (ranks multiple signals when capital is limited).
    
- **Risk Management:** `ApplyStop` (configures maximum loss, trailing stops, profit targets, or time-based exits).
    
- **Backtest Settings:** `SetOption` (defines initial equity, commission models, and maximum open positions).
    

---

### Price Action and Structural Functions

- **Swing Analysis:** `Peak`, `Trough`, `PeakBars`, `TroughBars`, `Zig` (ZigZag trend lines).
    
- **Price Extremes:** `HHV` (Highest High Value), `LLV` (Lowest Low Value).
    
- **Conditional Referencing:** `ValueWhen`, `HighestSince`, `LowestSince`.
    
- **Signal Triggers:** `Cross` (identifies exact crossover points of two arrays).
    
- **Time Shifting:** `Ref` (looks back at past bars or peeks at future bars).
    

---

### Mathematical and Array Logic

- **Conditional Statements:** `IIf` (fast, vector-based if/else logic for entire arrays).
    
- **Math Operations:** `Abs`, `Log`, `Sqrt`, `Round`, `Ceil`, `Floor`.
    
- **Statistical Tools:** `LinearReg` (Linear Regression), `Correlation`, `Percentile`.
    
- **Custom Iteration:** `AMA` (Adaptive Moving Average function for recursive array calculations), `For` / `While` (standard loops for procedural code execution).
    

---

### Exploration and Visualization

- **Exploration Filter:** `Filter` (boolean array that determines which tickers appear in scan results).
    
- **Data Columns:** `AddColumn`, `AddTextColumn` (outputs specific metrics to the exploration grid).
    
- **Charting Elements:** `Plot`, `PlotShapes`, `PlotText`, `PlotOHLC` (draws lines, shapes, and candlesticks on the graphical interface).
    
