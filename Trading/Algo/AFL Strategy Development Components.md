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
    

---

### Candlestick Pattern Detection

- **Single-Bar Patterns:** Doji (`O == C`), Hammer (`(C-L) > 2*(H-C)` with small body near high), Shooting Star (inverted hammer at highs), Marubozu (full body, no wicks).
    
- **Two-Bar Patterns:** Bullish/Bearish Engulfing (`C > Ref(H,-1)` and `O < Ref(L,-1)`), Harami (inside bar, body within prior body), Piercing Line, Dark Cloud Cover.
    
- **Three-Bar Patterns:** Morning Star, Evening Star, Three White Soldiers, Three Black Crows, Three Inside Up/Down.
    
- **AFL Detection Logic:** Use `BarsSince`, `Ref`, `IIf`, and `HHV`/`LLV` to compose pattern conditions into boolean arrays for Buy/Sell signals.
    
- **Body and Wick Helpers:** `bodySize = abs(C - O)`, `upperWick = H - Max(O,C)`, `lowerWick = Min(O,C) - L`, `totalRange = H - L`.
    

---

### Market Regime and Trend Context

- **Trend State:** Compare `Close` vs `MA(Close, 200)` — above = bull regime, below = bear regime. Use `ADX(14) > 25` to confirm trending vs ranging.
    
- **Slope/Direction:** `maSlope = MA(C,20) - Ref(MA(C,20),-5)` — positive slope = uptrend, negative = downtrend.
    
- **Regime Switching:** Use `IIf(regime == 1, longOnly_signal, shortOnly_signal)` to gate signal types by detected market phase.
    
- **Volatility Regime:** `ATR(14) / MA(ATR(14), 50)` — ratio above 1.5 = high-vol regime; adjust position size or stay flat.
    
- **Choppiness Index:** `CHOP = 100 * Log10(Sum(ATR(1), n) / (HHV(H,n) - LLV(L,n))) / Log10(n)` — above 61.8 = choppy, below 38.2 = trending.
    

---

### Entry Condition Filters (Signal Quality)

- **Trend Confirmation Filter:** Only take long signals when `MA(C,50) > MA(C,200)` (golden cross state).
    
- **Momentum Filter:** Require RSI to be in a specific zone (e.g., `RSI(14) > 40 AND RSI(14) < 70`) before entry.
    
- **Volume Confirmation:** `Volume > MA(Volume, 20) * 1.5` — confirms breakout or signal with above-average participation.
    
- **Volatility Filter:** `ATR(14)/C * 100 > minATRpct` — skip low-volatility instruments unlikely to move enough to cover costs.
    
- **Gap Filter:** `openGap = (O - Ref(C,-1)) / Ref(C,-1) * 100` — exclude entries on large gap-up days for mean-reversion systems.
    
- **Time-of-Day Filter (Intraday):** `TimeNum() >= 093000 AND TimeNum() <= 153000` — restrict entries to defined session windows.
    
- **Day-of-Week Filter:** `DayOfWeek() != 1 AND DayOfWeek() != 5` — avoid Mondays/Fridays if historically weak for your system.
    

---

### Exit Logic Components

- **Fixed Profit Target:** `ApplyStop(stopTypeProfit, stopModePercent, profitPct, 1)`.
    
- **Fixed Stop Loss:** `ApplyStop(stopTypeLoss, stopModePercent, lossPct, 1)`.
    
- **Trailing Stop (ATR-based):** `trailStop = C - multiplier * ATR(14)` stored via `HighestSince`; exit when `C < trailStop`.
    
- **Time-Based Exit:** `ApplyStop(stopTypeNBar, stopModeBar, maxBarsInTrade, 1)` — force close after N bars regardless of P&L.
    
- **Opposite Signal Exit:** Set `Sell = Short_signal` or `Cover = Buy_signal` — let opposing signals close positions.
    
- **Chandelier Exit:** `chandelierLong = HHV(H, lookback) - multiplier * ATR(lookback)` — trails from highest high.
    
- **Volatility-Adjusted Target:** `target = entryPrice + profitMultiplier * ATR(14)` — scales with current volatility.
    

---

### Multi-Timeframe Analysis (MTF)

- **TimeFrameSet / TimeFrameRestore:** Switch AFL context to a higher timeframe, compute indicators, then restore.
    
- **Example — Weekly MA on Daily Chart:**
  ```afl
  TimeFrameSet(inWeekly);
  weeklyMA = MA(C, 10);
  TimeFrameRestore();
  weeklyMADaily = TimeFrameExpand(weeklyMA, inWeekly, expandLast);
  Buy = Cross(C, weeklyMADaily);
  ```
    
- **Timeframe Constants:** `inDaily`, `inWeekly`, `inMonthly`, `in1Minute`, `in5Minute`, `in15Minute`, `in60Minute`.
    
- **expandLast vs expandFirst:** `expandLast` fills the higher-TF value forward to every lower-TF bar; `expandFirst` fills at the open of the period.
    
- **MTF Confirmation Logic:** Use higher-TF trend as a filter: `longOK = weeklyTrend == 1` — only trade longs on daily if weekly is bullish.
    

---

### Walk-Forward Optimization (WFO)

- **In-Sample (IS) / Out-of-Sample (OOS):** IS period is optimized; OOS is the unseen forward test window. Standard ratio: 4:1 or 3:1 IS:OOS.
    
- **WFO Setup in AmiBroker:** Analysis → Settings → Walk-Forward tab. Set IS length, OOS length, anchored or rolling window.
    
- **Anchored vs Rolling:** Anchored IS always starts from the same date, growing over time. Rolling IS window slides forward, keeping a fixed length.
    
- **Parameter Stability:** Prefer parameter sets that perform consistently across multiple WFO folds, not just the best single fold.
    
- **Efficiency Ratio:** `WFO Efficiency = OOS_CAR / IS_CAR * 100` — above 50% is acceptable; above 70% is strong.
    
- **Out-of-Sample Metric Priority:** Favor Sharpe Ratio, Calmar Ratio, or Profit Factor in OOS — not raw Net Profit (over-fitting trap).
    

---

### Optimization Components

- **Optimize Function:** `param = Optimize("Name", defaultVal, minVal, maxVal, step)` — registers a parameter for the optimizer.
    
- **Target Metrics:** Set optimization target in Analysis Settings — options include Net Profit, CAR, Sharpe, Profit Factor, RAR (Risk-Adjusted Return).
    
- **Exhaustive vs Genetic:** Exhaustive tests every combination; Genetic (CMAes) searches efficiently for large parameter spaces.
    
- **Over-Fitting Guard:** Limit free parameters (≤3–5 for simple systems). Use `SetOption("MaxOpenPositions", n)` consistently.
    
- **Parameter Surface Visualization:** In 3D Optimization Chart, look for a broad, flat plateau — not a sharp spike — around the best parameters.
    
- **Robustness Check:** Perturb optimal params ±10–20% and verify performance degrades gracefully, not catastrophically.
    

---

### Position Sizing Methods

- **Fixed Fractional:** `PositionSize = -riskPct` — risk a fixed percentage of equity per trade (e.g., `-2` = 2% of equity).
    
- **Fixed Dollar Amount:** `PositionSize = 10000` — allocate a fixed dollar amount per position.
    
- **ATR-Based Sizing:** `shares = (equity * riskPct) / (ATR(14) * multiplier)` — normalizes risk across instruments with different volatility.
    
- **Kelly Criterion:** `f = (W * R - (1-W)) / R` where W = win rate, R = avg win / avg loss. Use half-Kelly for safety: `PositionSize = -(f/2 * 100)`.
    
- **Volatility Parity:** `PositionSize = targetVol / instrVol * equity` — equalizes each position's volatility contribution to the portfolio.
    
- **Score-Based Ranking:** `PositionScore = RSI(2)` (lower = buy sooner for mean reversion) or `PositionScore = ROC(C,20)` (higher = momentum).
    

---

### Portfolio-Level Backtest Settings

- **Max Open Positions:** `SetOption("MaxOpenPositions", N)` — caps simultaneous holdings; forces `PositionScore` ranking.
    
- **Initial Equity:** `SetOption("InitialEquity", 100000)`.
    
- **Commission Model:** `SetTradeDelays(1,1,1,1)` (1-bar delay on all signals) + `SetOption("CommissionMode", 2); SetOption("CommissionAmount", 0.1)` (0.1% per trade).
    
- **Margin / Leverage:** `SetOption("MarginRequirement", 50)` — 50% margin = 2× leverage.
    
- **Rounding to Lot Size:** `SetOption("RoundLotSize", 100)` — useful for stocks with standard board lots.
    
- **Futures Mode:** `SetOption("FuturesMode", True)` — enables point value and multiplier for futures contracts.
    
- **Allow Shorting:** `SetOption("AllowSameBarExit", True)` + set `Short` and `Cover` arrays to enable short-side simulation.
    

---

### Performance Metrics and Analysis

- **Net Profit %:** Total return over the test period. Compare against buy-and-hold benchmark.
    
- **CAGR (CAR):** Compound Annual Growth Rate — normalizes return across different test lengths.
    
- **Max Drawdown %:** Peak-to-trough equity decline. Key risk metric; aim for MaxDD < 20% for most strategies.
    
- **Calmar Ratio:** `CAR / MaxDD` — reward per unit of drawdown risk. Above 1.0 is good.
    
- **Sharpe Ratio:** `(AvgReturn - RiskFree) / StdDev(Returns)` — risk-adjusted return. Above 1.0 is acceptable, 2.0+ is excellent.
    
- **Profit Factor:** `GrossProfit / GrossLoss` — above 1.5 is solid; above 2.0 is strong.
    
- **Win Rate vs Avg Win/Loss:** High win rate + small avg win can lose to low win rate + large avg win. Use Expectancy: `(WinRate * AvgWin) - (LossRate * AvgLoss)`.
    
- **Recovery Factor:** `NetProfit / MaxDD` — how efficiently the system recovers from drawdowns.
    
- **Trade Duration Stats:** Avg bars in winning vs losing trades — short losing trades and long winning trades are ideal.
    

---

### Custom Indicator Construction

- **Rate of Change (ROC):** `ROC(C, n) = (C - Ref(C,-n)) / Ref(C,-n) * 100`.
    
- **Z-Score Normalization:** `zscore = (C - MA(C,n)) / StDev(C,n)` — standardizes price relative to its own history.
    
- **Relative Strength (vs Index):** `RS = C / Foreign("^NSEI", "C")` — compares instrument to a benchmark.
    
- **Composite Momentum Score:** Average of multiple ROC windows: `mom = (ROC(C,5) + ROC(C,10) + ROC(C,20)) / 3`.
    
- **Donchian Channel:** `donchianHigh = HHV(H, n)`, `donchianLow = LLV(L, n)`, `donchianMid = (donchianHigh + donchianLow) / 2`.
    
- **Elder's Force Index:** `FI = Volume * (C - Ref(C,-1))` — combines price change and volume into one momentum signal.
    
- **True Strength Index (TSI):** Double-smoothed momentum: `TSI = 100 * EMA(EMA(priceChange,r),s) / EMA(EMA(absPriceChange,r),s)`.
    
- **Fractal Indicator (Williams):** Bearish fractal: `H[-2] < H[-1] < H[0] > H[1] > H[2]` (center bar is the highest of 5). `FractalHigh = H == HHV(H,5) AND Ref(HHV(H,5),-2) == H`.
    

---

### Signal Combination and Logic Patterns

- **AND Logic (All conditions must be true):**
  ```afl
  Buy = trendUp AND momentumOK AND volumeConfirmed;
  ```
    
- **OR Logic (Any trigger fires entry):**
  ```afl
  Buy = crossoverSignal OR breakoutSignal;
  ```
    
- **Scoring / Weighting:**
  ```afl
  score = (RSI(14) > 50) + (MA(C,20) > MA(C,50)) + (Volume > MA(V,20));
  Buy = score >= 2;  // At least 2 of 3 conditions true
  ```
    
- **Signal Confirmation Delay:** `Buy = buySignal AND Ref(buySignal,-1)` — require signal to be true for 2 consecutive bars.
    
- **Cooldown / Re-entry Block:** `Buy = buySignal AND BarsSince(Sell) > minBars` — prevent rapid re-entry after an exit.
    
- **Opposite-Direction Guard:** `Buy = buyRaw AND NOT InShortTrade` — prevent conflicting signals.
    

---

### Breadth and Inter-Market Components

- **Advance-Decline Concept (via Foreign):** Load breadth indices: `adLine = Foreign("$ADVDEC", "C")` — use as market filter.
    
- **Benchmark Relative Strength:** `relStr = MA(C/Foreign("INDEX","C"), 10)` — rising = outperforming benchmark.
    
- **Sector Rotation:** Load multiple sector ETFs, rank by `ROC(C,63)` over 63 bars — rotate into top-ranked sectors.
    
- **VIX-Based Filter:** `vix = Foreign("^VIX","C")` — reduce position size or go flat when `vix > 30`.
    
- **Yield Curve / Macro (via custom data):** Import economic indicators as custom securities; use `Foreign()` to access in strategy AFL.
    

---

### Mean Reversion Components

- **RSI(2) Strategy Core:** `Buy = RSI(2) < 10; Sell = RSI(2) > 90` — extreme short-term RSI reversions.
    
- **Bollinger Band Mean Reversion:** `Buy = C < BBandBot(C,20,2); Sell = C > MA(C,20)` — buy at lower band, exit at midline.
    
- **Percent Distance from MA:** `distFromMA = (C - MA(C,n)) / MA(C,n) * 100` — buy when oversold (e.g., < -5%), sell when recovered.
    
- **Statistical Z-Score Entry:** `Buy = zscore < -2; Sell = zscore > 0` — enter on extreme deviations, exit at mean.
    
- **Consecutive Down Bars:** `Buy = Sum(C < Ref(C,-1), 3) == 3` — buy after 3 consecutive down-closes (short-term exhaustion).
    

---

### Breakout and Momentum Components

- **Donchian Breakout:** `Buy = C == HHV(C, 20)` — new N-bar high; `Short = C == LLV(C, 20)`.
    
- **Volatility Contraction + Expansion:** `narrowRange = (H - L) == LLV(H-L, 7)` — NR7 day signals potential breakout setup.
    
- **Opening Range Breakout (Intraday):** Store first-bar high/low; `Buy = C > orHigh AND TimeNum() > openingPeriodEnd`.
    
- **MACD Histogram Divergence:** `macdHist = MACD() - Signal()` — declining histogram with rising price = bearish divergence.
    
- **52-Week High Momentum:** `Buy = C >= 0.95 * HHV(C, 252)` — within 5% of yearly high (trending strength filter).
    
- **Turtle Trading Rules:** `Buy = C == HHV(C,20); Sell = C == LLV(C,10)` — classic 20-bar entry, 10-bar exit.
    

---

### Utility Functions and AFL Patterns

- **Persistent Variables:** `StaticVarSet("key", value)` / `StaticVarGet("key")` — store values across bars or between runs.
    
- **Trade State Tracking:** `InTrade = Flip(Buy, Sell)` — boolean array: 1 while position is held.
    
- **BarsSince:** `BarsSince(condition)` — number of bars elapsed since condition was last true; use for time-based filters.
    
- **Highest/Lowest Since Entry:** `highSinceEntry = HighestSince(Buy, H)` — tracks the highest high since buy signal.
    
- **WriteIf / WriteVal:** Format exploration output strings: `AddTextColumn(WriteIf(Buy,"BUY","—"), "Signal")`.
    
- **Null / Padding Handling:** `Nz(value, 0)` — replaces Null with 0 to avoid array calculation errors.
    
- **DateNum / TimeNum:** `DateNum()` returns YYYYMMDD integer; `TimeNum()` returns HHMMSS — use for time-based filters.
    
- **Name() / FullName() / Interval():** Access current ticker name and bar interval inside AFL for dynamic logic.
    

---

### Backtest Validation and Anti-Overfitting Checklist

- **Minimum Trade Count:** Aim for ≥ 30–50 trades per test segment for statistical significance. Fewer = unreliable metrics.
    
- **In-Sample vs Out-of-Sample Split:** Reserve at least 20–30% of data as unseen OOS. Never optimize on OOS data.
    
- **Parameter Sensitivity Test:** Vary each parameter ±1 step from optimal — performance should degrade smoothly, not collapse.
    
- **Monte Carlo Simulation:** Randomize trade order 1000× — assess worst-case drawdown distribution from the same trade set.
    
- **Multiple Market Test:** Run the same system on different instruments/markets — a truly robust edge should work broadly.
    
- **Benchmark Comparison:** Your system must beat a simple buy-and-hold on the same instrument, adjusted for drawdown.
    
- **Transaction Cost Sensitivity:** Double/triple your commission assumption — if strategy fails, the edge is too thin.
    
- **Regime Stability:** Split data by bull/bear/sideways periods — confirm the system works across regime types, not just one.
    

---

### AFL Code Snippet Templates

- **Simple MA Crossover System:**
  ```afl
  fast = Optimize("Fast MA", 10, 5, 30, 1);
  slow = Optimize("Slow MA", 30, 20, 100, 5);
  Buy  = Cross(MA(C, fast), MA(C, slow));
  Sell = Cross(MA(C, slow), MA(C, fast));
  Short  = Sell;
  Cover  = Buy;
  ApplyStop(stopTypeLoss, stopModePercent, 5, 1);
  ```
    
- **RSI Mean Reversion with Trend Filter:**
  ```afl
  trendFilter = C > MA(C, 200);
  entry = RSI(2) < 10 AND trendFilter;
  exitSig = RSI(2) > 70;
  Buy  = entry;
  Sell = exitSig;
  PositionSize = -2;  // 2% risk per trade
  ```
    
- **ATR Trailing Stop Template:**
  ```afl
  mult  = Optimize("ATR Mult", 2, 1, 4, 0.5);
  atrVal = ATR(14);
  longStop = HHV(C, 1) - mult * atrVal;
  Sell = C < longStop AND InTrade;
  ```
    
- **Multi-Condition Scored Signal:**
  ```afl
  c1 = RSI(14) > 50;
  c2 = MACD() > Signal();
  c3 = Volume > MA(V, 20);
  c4 = C > MA(C, 50);
  score = c1 + c2 + c3 + c4;
  Buy  = score >= 3;
  Sell = score <= 1;
  PositionScore = score;
  ```
    
