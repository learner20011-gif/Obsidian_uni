### **I. Evaluation of the Previous Critiques: The DSE Market Reality**

Navigating the daily charts of the Dhaka Stock Exchange (DSE) requires acknowledging its unique microstructure: high manipulation, sudden liquidity vacuums, and the unforgiving T+2 settlement rule. Here is the evaluation of the previous systemic critiques, highlighting where the logic unified and where it brutally contradicted itself.

#### **Branch 1: Points of Absolute Agreement (The Undeniable Truths)**

- **The T+2 Settlement Dictatorship:** All critiques correctly identified that global high-frequency and day-trading strategies fail here. Because you cannot sell the day after you buy (T+1), buying the exact top of an algorithmic "buy signal" is fatal.
    
- **The Lagging Indicator Death Trap:** Relying on slow, smoothed averages (like the 13/26 EMA crossovers or MACD crossovers found in standard Pine Scripts) guarantees you are buying the distribution phase of a syndicate's pump, not the accumulation phase.
    
- **The Fallacy of Rigid Overbought Exits:** Exiting a swing trade simply because the `RSI > 70` is a mathematically proven way to miss multi-day "limit-up" rallies in the DSE.
    
- **Strict Data Separation:** The absolute necessity to separate **Non-OHLCV data** (used strictly for pre-screening to find _what_ to buy) from **OHLCV data** (used strictly in the algorithmic strategy to dictate _when_ to buy and sell).
    

#### **Branch 2: Points of Contradiction (The Evolution of the Edge)**

- **The Breakout Illusion vs. The Contraction Reality:**
    
    - _The Contradiction:_ Early models suggested buying the "Upper Bollinger Band Breakout on 3x Volume." The final critique aggressively destroyed this idea.
        
    - _The Verdict:_ Buying obvious volume breakouts in the DSE makes you exit liquidity for syndicates. You suffer the "Wick of Death." You must instead buy the quiet _Volatility Contraction_ right before the breakout.
        
- **Static "Value" vs. Dynamic "Cash & Flow":**
    
    - _The Contradiction:_ Early screeners relied on static numbers like Paid-Up Capital, PE Ratio, and simply having a Cash Dividend > 0. The final critique ripped these apart as easily faked accounting tricks or causes of capital stagnation.
        
    - _The Verdict:_ Static value traps must be replaced with un-fakeable metrics: Operating Cash Flow and the active transfer of shares from public to institutional hands.
        
- **Stop-Loss Hunting:**
    
    - _The Contradiction:_ Placing a stop loss precisely at the "low of the breakout candle" is exactly what retail traders are taught, making it a prime target for operator stop-hunting on T+1.
        
    - _The Verdict:_ A tighter, mathematically detached Average True Range (ATR) stop placed during a period of _low_ volatility is much harder for syndicates to intentionally trigger.
        

---

### **II. The Final Verdict: The Apex DSE Swing Trading System**

This is the finalized, stress-tested ruleset. It strictly obeys the law of separating Non-OHLCV screening from OHLCV algorithmic execution.

#### **Branch 1: The Pre-Screener Ruleset (Strictly Non-OHLCV)**

Run this scan periodically (weekly/monthly as data updates) on platforms like Amarstock to create a refined watchlist. Do not look at a chart yet.

- **Rule 1: The "Un-fakeable Cash" Filter**
    
    - _Parameter:_ `Net Operating Cash Flow Per Share (NOCFPS) > EPS`.
        
    - _Logic:_ Earnings can be manipulated via "Accounts Receivable." Cash in the bank cannot. If NOCFPS exceeds EPS, the company is fundamentally bulletproof and generating real liquidity.
        
- **Rule 2: The "Smart Money Transfer" Filter**
    
    - _Parameter:_ `Sponsor/Director Holding % Change` is **Positive** AND `Public Holding % Change` is **Negative**.
        
    - _Logic:_ This proves a mathematical divergence. The stock is actively being accumulated by insiders while retail traders are capitulating.
        
- **Rule 3: The "Operator Playground" Filter**
    
    - _Parameter:_ `Free Float % < 45%` AND `Category = A or B`.
        
    - _Logic:_ Avoids Z-category delisting risk, while ensuring the supply of tradable shares is restricted enough for a syndicate to easily drive the price up.
        

#### **Branch 2: The Algorithmic Trading Strategy (Strictly OHLCV)**

Load the fundamentally cleared watchlist into your charting software (AmiBroker, Pine Script). The algorithm tracks the footprints of the operators.

- **Rule 1: The Macro Baseline (No Falling Knives)**
    
    - _Parameter:_ `Close > SMA(150)` AND `SMA(50) > SMA(150)`.
        
    - _Logic:_ The stock must be in an established Stage-2 macro uptrend.
        
- **Rule 2: The Volatility Contraction Pattern (VCP) Setup**
    
    - _Parameter:_ `High - Low` (Daily Range) is at the lowest point of the last 20 trading sessions AND `Volume < (SMA(Volume, 20) * 0.5)`.
        
    - _Logic:_ Selling pressure has completely evaporated. The chart looks "dead." This is when syndicates finish accumulating.
        
- **Rule 3: The "Pocket Pivot" Stealth Entry Trigger**
    
    - _Parameter:_ `Close > Close[1]` (It is an up day) AND `Volume > Highest Volume of the last 10 Down Days`.
        
    - _Logic:_ You buy when institutional volume quietly steps in on an up-day, eclipsing all recent selling pressure, _before_ it triggers the obvious 300% volume breakout scanners.
        
- **Rule 4: The T+2 Survival Risk Management**
    
    - _Stop Loss:_ `SL = Entry Price - (1.2 * ATR(14))`. Set this hard line. Because you entered during a VCP (low volatility), the ATR is small, keeping your risk exceptionally tight.
        
    - _Take Profit (Scale Out):_ Sell 50% of your position on the day the stock officially "breaks out" (e.g., crosses the upper Bollinger Band with massive volume), happily selling to the retail breakout traders.
        
    - _Take Profit (The Runner):_ Move the stop loss to breakeven on the remaining 50% and trail it. Sell the rest only when the `Close` falls entirely below the `EMA(13)`.