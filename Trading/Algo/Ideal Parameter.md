| **Tier** | **Metric Name**             | **What It Measures**                                                    | **The Optimal Target**                                                              | **Why It Matters (Significance)**                                                                                                                        |
| -------- | --------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**    | **CAR/MDD**                 | Compound Annual Return divided by Maximum Drawdown.                     | **> 1.0** (Good)<br><br>**> 0.7**  for long trade only<br><br>**> 2.0** (Excellent) | The ultimate "Holy Grail" risk-adjusted return metric. It prevents you from trading a high-profit system that would wipe out your account along the way. |
| **1**    | **Max. Sys % Drawdown**     | The deepest percentage drop in total equity from a previous peak.       | **< 15%** (Or half your personal pain threshold)                                    | Backtests are optimistic. In live trading, your drawdown will likely be worse than the test. Keeping this low ensures you don't panic-quit the strategy. |
| **1**    | **Profit Factor**           | Gross Profits divided by Gross Losses.                                  | **1.5 to 2.5**                                                                      | Proves the mathematical edge. < 1.5 means you are barely surviving friction (commissions/slippage). > 3.0 usually indicates dangerous curve-fitting.     |
| **1**    | **Recovery Factor**         | Total Net Profit divided by the Maximum System Drawdown.                | **> 2.0**                                                                           | Shows how quickly the system bounces back from pain. If a system loses $5k but only makes $6k total over two years, it is too slow to recover.           |
| **2**    | **# Trades**                | The total sample size of the backtest.                                  | **> 100** (Minimum)<br>per year<br>  <br><br>**200+** (Ideal)                       | Statistical significance. A system with a perfect Profit Factor over only 30 trades is just lucky. You need volume to prove the edge is real.            |
| **2**    | **% of Winners** (Win Rate) | How often a trade closes at a profit.                                   | Strategy Dependent (Often **30% - 50%** for swing/trend)                            | High win rates (70%+) usually mean tiny profits per trade. Low win rates (30%) require massive winners to survive.                                       |
| **2**    | **Payoff Ratio**            | The average winning trade amount divided by the average losing trade.   | **> 2.0** (If Win Rate is < 50%)                                                    | The seesaw balance to Win Rate. If you only win 1 out of 3 trades, your winners _must_ be at least twice as large as your losers to make money.          |
| **2**    | **Exposure %**              | The percentage of time your capital is actually in the market vs. cash. | **As low as possible** while maintaining CAR.                                       | Lower exposure means your money is sitting safely in cash during market crashes, drastically reducing your overall risk profile.                         |
### The Strategy: How to Find the Balanced "Sweet Spot"

You asked how to choose optimal values without making other parameters worse. This is called finding the **Pareto Front**. You do not want the absolute highest return; you want the most robust compromise. Here is the exact workflow:

1. **The Floor Filter:** Discard the trash immediately. Go to your AmiBroker results and delete/ignore any row where `# Trades` is less than 50, or `Max % Drawdown` is worse than -15%.
    
2. **The Core Sort:** Sort the remaining rows by **CAR/MDD** from highest to lowest.
    
3. **The Reality Check:** Look at the top 5 rows. Check the `Profit Factor`. If one row has a Profit Factor of 4.5 and the others are around 2.5, **throw out the 4.5**. It is an anomaly and will fail live.
    
4. **Find the Parameter Neighborhood:** Look at your custom parameters (far right) for the top 10 surviving rows.
    
    - Does the `Time Stop Days` consistently sit at 3 or 5?
        
    - Does the `Risk Per Trade` consistently sit at 1.5%?
        
    - **The Optimal Value:** Choose the parameters that show up _most frequently_ in the top 10 rows, rather than blindly copying the exact parameters of row #1. If a parameter value works well across multiple slightly different variations, it is robust and will survive the live market.