
Here is a concise, easy-to-follow cheat sheet of all the **core concepts** from **Chapter 5 (Resampling Methods)** needed to solve Exercises 1–9.

---

### **1. Why Resampling? (The Big Picture)**
Resampling means repeatedly drawing samples from your training data and refitting a model to learn more about its accuracy or variability.
* **Model Assessment:** Evaluating how well a model performs on unseen data (estimating **test error**).
* **Model Selection:** Choosing the right level of model flexibility (e.g., polynomial degree 2 vs. 3).

---

### **2. Cross-Validation (Estimating Test Error)**

#### **A. Validation Set Approach** *(Used in Q5)*
* **How it works:** Randomly split data once into a **training set** (e.g., 50%) and a **validation set** (50%). Fit on training, test on validation.
* **Pros:** Simple and fast.
* **Cons:**
  1. **High variability:** Error estimate changes depending on the random split.
  2. **Overestimates test error:** Model is trained on only half the data.

#### **B. Leave-One-Out Cross-Validation (LOOCV)** *(Used in Q3, Q7, Q8)*
* **How it works:** Leave out **1** observation for validation, train on the remaining $n - 1$, repeat $n$ times, and average the errors:
  $$\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^{n} \text{MSE}_i$$
* **Shortcut (Least Squares Linear/Polynomial only):** $\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^{n} \left(\frac{y_i - \hat{y}_i}{1 - h_i}\right)^2$ (requires only 1 fit!).
* **Pros:** Almost zero bias (trains on $n - 1$ points); **no randomness** (same result every time).
* **Cons:** Slow for general models (fits $n$ times); **higher variance** than $k$-fold CV because the $n$ training sets overlap almost completely.

#### **C. $k$-Fold Cross-Validation** *(Used in Q3)*
* **How it works:** Split data into $k$ equal **folds** (typically $k = 5$ or $10$). Hold out 1 fold, train on $k - 1$ folds, repeat $k$ times, and average:
  $$\text{CV}_{(k)} = \frac{1}{k} \sum_{i=1}^{k} \text{MSE}_i$$
* **Bias-Variance Trade-Off:**
  * **Bias:** Lower than Validation Set, slightly higher than LOOCV.
  * **Variance:** Lower than LOOCV (less overlap between training sets).
  * **Rule of thumb:** $k = 5$ or $10$ gives the best balance of speed, low bias, and low variance.

#### **D. CV for Classification** *(Used in Q5, Q7)*
* Replace MSE with the **misclassification error rate**:
  $$\text{Err}_i = I(y_i \neq \hat{y}_i) \quad \text{(1 if wrong, 0 if right)}$$

---

### **3. The Bootstrap (Estimating Uncertainty / Standard Error)**

#### **A. Core Idea** *(Used in Q4, Q6, Q9)*
When we can't draw new samples from the real population, we simulate it by **sampling $n$ observations *with replacement*** from our original dataset $B$ times (e.g., $B = 1,000$).
* Compute your statistic $\hat{\alpha}^{*r}$ on each bootstrap sample $r = 1, \dots, B$.
* **Bootstrap Standard Error Formula:**
  $$\text{SE}_B(\hat{\alpha}) = \sqrt{\frac{1}{B - 1} \sum_{r=1}^{B} \left(\hat{\alpha}^{*r} - \bar{\alpha}^*\right)^2}$$

#### **B. Why Bootstrap is So Useful**
* Works for **any** statistic—even when no simple math formula exists (e.g., **median**, **percentiles**, or **complex model predictions**).
* Doesn't rely on strict parametric assumptions (e.g., constant noise variance or fixed $X$).

#### **C. Key Bootstrap Probability Fact** *(Used in Q2)*
* Chance an observation is **not** picked in 1 draw: $1 - \frac{1}{n}$.
* Chance it is **not** in a bootstrap sample of size $n$: $\left(1 - \frac{1}{n}\right)^n$.
* Chance it **is** in the bootstrap sample: $1 - \left(1 - \frac{1}{n}\right)^n \xrightarrow{n \to \infty} 1 - \frac{1}{e} \approx \mathbf{63.2\%}$.

---

### **4. Quick Map: Concept $\rightarrow$ Exercise**

| Exercise | Core Concept Used                                                                                        |
| :------- | :------------------------------------------------------------------------------------------------------- |
| **Q1**   | Variance rules + calculus (1st & 2nd derivatives) to minimize risk $\text{Var}(\alpha X + (1-\alpha)Y)$. |
| **Q2**   | Bootstrap sampling **with replacement** probability ($63.2\%$ rule).                                     |
| **Q3**   | Comparing $k$-fold CV vs. Validation Set vs. LOOCV (**bias-variance trade-off**).                        |
| **Q4**   | Using the **Bootstrap** to estimate the standard deviation of *any* prediction.                          |
| **Q5**   | **Validation Set Approach** for classification (`train_test_split` + `sm.GLM`).                          |
| **Q6**   | Comparing formula SE (`sm.GLM`) vs. **Bootstrap SE** for logistic regression coefficients.               |
| **Q7**   | Manual **LOOCV** loop for classification (`Weekly` dataset).                                             |
| **Q8**   | **LOOCV** for model selection (polynomial degrees 1–4) + determinism of LOOCV.                           |
| **Q9**   | **Bootstrap SE** for mean, median, and 10th percentile + 95% CI ($\hat{\mu} \pm 2\text{SE}$).            |

Here are the concise, step-by-step solutions to the first two questions from **Section 5.4 (Exercises)**.

---

### **Question 1: Deriving the Minimum Risk Formula (5.6)**

**Goal:** Prove that $\alpha = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}}$ minimizes the total variance $f(\alpha) = \text{Var}(\alpha X + (1 - \alpha)Y)$.

**Step 1: Expand the variance**
Using the rule $\text{Var}(aX + bY) = a^2\text{Var}(X) + b^2\text{Var}(Y) + 2ab\text{Cov}(X, Y)$:
$$f(\alpha) = \alpha^2 \sigma_X^2 + (1 - \alpha)^2 \sigma_Y^2 + 2\alpha(1 - \alpha)\sigma_{XY}$$

**Step 2: Take the first derivative and set it to 0**
Differentiate $f(\alpha)$ with respect to $\alpha$:
$$f'(\alpha) = 2\alpha \sigma_X^2 - 2(1 - \alpha)\sigma_Y^2 + 2(1 - 2\alpha)\sigma_{XY} = 0$$

Divide the whole equation by 2 and expand:
$$\alpha \sigma_X^2 - \sigma_Y^2 + \alpha \sigma_Y^2 + \sigma_{XY} - 2\alpha \sigma_{XY} = 0$$

Group the terms containing $\alpha$ on the left and move the rest to the right:
$$\alpha(\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}) = \sigma_Y^2 - \sigma_{XY}$$

Solve for $\alpha$:
$$\alpha = \frac{\sigma_Y^2 - \sigma_{XY}}{\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}}$$

**Step 3: Confirm it is a minimum (Second Derivative Test)**
Take the second derivative of $f(\alpha)$:
$$f''(\alpha) = 2\sigma_X^2 + 2\sigma_Y^2 - 4\sigma_{XY} = 2(\sigma_X^2 + \sigma_Y^2 - 2\sigma_{XY}) = 2\text{Var}(X - Y)$$
Since variance is always $\ge 0$ (and $> 0$ as long as $X - Y$ isn't constant), $f''(\alpha) > 0$. This confirms that $\alpha$ gives the **minimum** variance.

---
### Problem 1: Stock Portfolio (Independent Assets)

* **Q:** You split money between Tech Stock $X$ (Variance $\sigma_X^2 = 16$) and Bond $Y$ (Variance $\sigma_Y^2 = 4$). They move completely independently ($\sigma_{XY} = 0$). What percentage ($\alpha$) should go into Tech Stock $X$ to minimize risk?
* **A:** Plug the values into the formula:

$$\alpha = \frac{4 - 0}{16 + 4 - 2(0)} = \frac{4}{20} = 0.20$$

**Result:** Invest **20%** in Tech Stock $X$ and **80%** in Bond $Y$.

---

### Problem 2: Weather Hedge (Negative Covariance)

* **Q:** An Umbrella Company ($X$, $\sigma_X^2 = 9$) and an Ice Cream Shop ($Y$, $\sigma_Y^2 = 9$) have opposite seasonal sales, giving a negative covariance ($\sigma_{XY} = -9$). Find the safest investment mix ($\alpha$).
* **A:** Plug the values into the formula:

$$\alpha = \frac{9 - (-9)}{9 + 9 - 2(-9)} = \frac{18}{36} = 0.50$$

**Result:** Invest **50%** in each. Because they cancel each other out, your total risk drops to **zero**.

---

### Problem 3: Identical Risk, Positively Linked

* **Q:** Two competing coffee shops ($X$ and $Y$) have the exact same risk ($\sigma_X^2 = 10, \sigma_Y^2 = 10$) and tend to rise and fall together ($\sigma_{XY} = 4$). How should you divide your money?
* **A:** Plug the values into the formula:

$$\alpha = \frac{10 - 4}{10 + 10 - 2(4)} = \frac{6}{12} = 0.50$$

**Result:** Even when two assets move together, splitting **50/50** still lowers your overall risk compared to betting everything on just one shop.

---

### Problem 4: Real-World Commute Time

* **Q:** Route $X$ (Highway) has a time variance of $25\text{ mins}^2$. Route $Y$ (City Streets) has a variance of $16\text{ mins}^2$. Traffic spills over between them ($\sigma_{XY} = 5$). If you split your weekly trips between both routes to keep your average arrival time as predictable as possible, what fraction ($\alpha$) of days should you take the Highway?
* **A:** Plug the values into the formula:

$$\alpha = \frac{16 - 5}{25 + 16 - 2(5)} = \frac{11}{31} \approx 0.355$$

**Result:** Take the Highway **35.5%** of the time (about 2 days a week) and City Streets **64.5%** of the time.
### **Question 2: Probability of Being in a Bootstrap Sample**

Suppose we draw a bootstrap sample of size $n$ (with replacement) from $n$ original observations.

* **(a) Probability the 1st draw is *not* the $j$th observation:**
  * **Answer:** $1 - \frac{1}{n}$
  * **Why:** Every observation has an equal $\frac{1}{n}$ chance of being picked, so the chance of *not* picking the $j$th one is $1 - \frac{1}{n}$.

* **(b) Probability the 2nd draw is *not* the $j$th observation:**
  * **Answer:** $1 - \frac{1}{n}$
  * **Why:** Because we sample **with replacement**, the pool of $n$ observations resets for every draw, making each draw independent with the exact same probability.

* **(c) Why the probability the $j$th observation is *not* in the sample is $(1 - 1/n)^n$:**
  * For the $j$th observation to be missing completely, it must be skipped in **all $n$ independent draws**. Multiplying the probability of skipping it $n$ times gives:
    $$\left(1 - \frac{1}{n}\right) \times \left(1 - \frac{1}{n}\right) \times \dots \times \left(1 - \frac{1}{n}\right) = \left(1 - \frac{1}{n}\right)^n$$

* **(d) Probability it *is* in the sample when $n = 5$:**
  $$1 - \left(1 - \frac{1}{5}\right)^5 = 1 - (0.8)^5 = 1 - 0.32768 = \mathbf{0.6723} \text{ (or } 67.2\%)$$

* **(e) Probability it *is* in the sample when $n = 100$:**
  $$1 - \left(1 - \frac{1}{100}\right)^{100} = 1 - (0.99)^{100} \approx \mathbf{0.6340} \text{ (or } 63.4\%)$$

* **(f) Probability it *is* in the sample when $n = 10,000$:**
  $$1 - \left(1 - \frac{1}{10,000}\right)^{10,000} \approx \mathbf{0.6321} \text{ (or } 63.2\%)$$

* **(g) Plot for $n = 1$ to $100,000$ and comment:**
  ```python
  import numpy as np
  import matplotlib.pyplot as plt

  n = np.arange(1, 100001)
  prob = 1 - (1 - 1/n)**n

  plt.plot(n, prob)
  plt.xscale('log') # Log scale makes the early drop easier to see
  plt.xlabel('Sample size (n)')
  plt.ylabel('Probability jth obs is in sample')
  plt.show()
  ```
  * **Observation:** The probability starts at $1$ (when $n=1$), drops very quickly for small values of $n$, and then levels off (asymptotes) at $1 - \frac{1}{e} \approx \mathbf{0.632}$. This means for any reasonably large dataset, a single bootstrap sample contains about **63.2%** of the original unique observations.

* **(h) Comment on the numerical simulation ($n = 100$):**
  * **Intended result:** If you correctly draw 100 observations per bootstrap sample, `np.mean(store)` will be around **0.634**, which matches our exact calculation in part **(e)**.
  * *(Note on a typo in the textbook's snippet: `rng.choice(100, replace=True)` is missing the sample size argument `100`—i.e., `rng.choice(100, 100, replace=True)`. If run exactly as printed without the second `100`, it only draws 1 number per loop and gives $\approx 0.01$ instead of $\approx 0.634$.)*

Here are the concise, organized solutions for **Questions 3 and 4** from **Section 5.4 (Exercises)**.

---

### **Question 3: Reviewing $k$-Fold Cross-Validation**

#### **(a) How $k$-fold cross-validation is implemented:**
1. **Split the data:** Randomly divide the $n$ observations into $k$ non-overlapping groups (*folds*) of roughly equal size.
2. **Hold out 1 fold:** Set aside the 1st fold as the validation set, and fit the model on the remaining $k - 1$ folds (training set).
3. **Compute error:** Calculate the test error (e.g., MSE for regression, or misclassification rate for classification) on the held-out fold ($\text{MSE}_1$).
4. **Repeat:** Repeat steps 2 and 3 $k$ times, using a different fold as the validation set each time.
5. **Average:** Average the $k$ resulting error estimates to get the overall $k$-fold CV error:
   $$\text{CV}_{(k)} = \frac{1}{k} \sum_{i=1}^{k} \text{MSE}_i$$

#### **(b) Advantages and disadvantages of $k$-fold CV:**

**i. Relative to the Validation Set Approach:**
* **Advantages:**
  * **Lower bias:** Each model trains on $\frac{k-1}{k}$ of the data (e.g., 90% for 10-fold CV) instead of ~50%, so it doesn't overestimate the test error as much.
  * **Less variability:** Averaging across $k$ folds reduces the randomness caused by a single lucky or unlucky train/validation split.
* **Disadvantages:**
  * **More computation:** The model must be fit $k$ times instead of just once.

**ii. Relative to Leave-One-Out Cross-Validation (LOOCV):**
* **Advantages:**
  * **Much faster:** Fits the model $k$ times (usually $k = 5$ or $10$) instead of $n$ times—a huge speedup when $n$ is large.
  * **Lower variance:** LOOCV averages $n$ models trained on almost identical data, making their errors highly correlated (high variance). $k$-fold CV has less overlap between training sets, resulting in lower variance and often a more accurate test error estimate.
* **Disadvantages:**
  * **Slightly higher bias:** Training on $\frac{k-1}{k}n$ observations instead of $n - 1$ introduces a small upward bias in the error estimate.
  * **Randomness:** Results vary slightly depending on how the data is randomly split into folds (whereas LOOCV is deterministic).

---

### **Question 4: Estimating the Standard Deviation of a Prediction**

To estimate the standard deviation (standard error) of a prediction $\hat{Y}$ at a specific value $X = x_0$ for *any* statistical learning method, we can use **the Bootstrap**:

1. **Create a bootstrap sample:** Randomly draw $n$ observations **with replacement** from the original training dataset of size $n$. Call this sample $Z^{*1}$.
2. **Fit and predict:** Fit the statistical learning method on $Z^{*1}$ and predict the response at $X = x_0$. Call this prediction $\hat{y}^{*1}$.
3. **Repeat $B$ times:** Repeat steps 1 and 2 a large number of times (e.g., $B = 1,000$) to get $B$ bootstrap predictions: $\hat{y}^{*1}, \hat{y}^{*2}, \dots, \hat{y}^{*B}$.
4. **Compute the standard deviation:** Calculate the sample standard deviation of these $B$ predictions:
   $$\text{SE}_B(\hat{y}) = \sqrt{\frac{1}{B - 1} \sum_{r=1}^{B} \left(\hat{y}^{*r} - \bar{y}^*\right)^2}$$
   where $\bar{y}^* = \frac{1}{B}\sum_{r=1}^{B} \hat{y}^{*r}$ is the mean of the $B$ bootstrap predictions.

This gives a reliable estimate of how much our prediction at $X = x_0$ would vary across different training samples.

Here are the concise, organized solutions (with ready-to-run Python code matching the textbook's `ISLP` lab style) for **Questions 5 and 6** from **Section 5.4 (Applied Exercises)**.

---

### **Question 5: Validation Set Approach on the `Default` Data**

#### **Setup**
```python
import numpy as np
import statsmodels.api as sm
from ISLP import load_data
from ISLP.models import ModelSpec as MS
from sklearn.model_selection import train_test_split

Default = load_data('Default')
```

#### **(a) Fit logistic regression on the full data (`income` + `balance`)**
```python
X = MS(['income', 'balance']).fit_transform(Default)
y = (Default['default'] == 'Yes').astype(int)

model = sm.GLM(y, X, family=sm.families.Binomial()).fit()
```

#### **(b) Estimate test error using the validation set approach**
```python
def val_error(seed, predictors=['income', 'balance']):
    # i. Split into training and validation sets (50/50 split)
    train, valid = train_test_split(Default, test_size=0.5, random_state=seed)
    
    # ii. Fit logistic regression on training set only
    mm = MS(predictors)
    X_train = mm.fit_transform(train)
    y_train = (train['default'] == 'Yes').astype(int)
    fit = sm.GLM(y_train, X_train, family=sm.families.Binomial()).fit()
    
    # iii. Predict default status on validation set (cutoff = 0.5)
    X_valid = mm.transform(valid)
    y_valid = (valid['default'] == 'Yes').astype(int)
    probs = fit.predict(X_valid)
    preds = (probs > 0.5).astype(int)
    
    # iv. Compute validation error rate (fraction misclassified)
    return np.mean(preds != y_valid)

print("Validation Error (seed=0):", val_error(0))
```
* **What happens:** The model typically achieves a low validation error rate around **2.5% – 2.9%**.

#### **(c) Repeat 3 times with different random splits**
```python
for s in [1, 2, 3]:
    print(f"Seed {s} Error:", val_error(s))
```
* **Comment:** Each split gives a slightly different validation error rate (usually varying around **2.4% – 2.9%**). This shows a key drawback of the validation set approach: the estimated test error depends on which observations happen to land in the training vs. validation set.

#### **(d) Add dummy variable for `student`**
```python
# MS() automatically converts 'student' ('Yes'/'No') into a dummy variable
for s in [0, 1, 2, 3]:
    print(f"Seed {s} Error (with student):", val_error(s, ['income', 'balance', 'student']))
```
* **Comment:** Including `student` produces nearly the exact same validation error rates (still around **2.5% – 2.9%**). It **does not** lead to a meaningful reduction in the test error rate.

---

### **Question 6: Standard Errors via `sm.GLM()` vs. The Bootstrap**

#### **(a) Standard errors using `sm.GLM()` and `summarize()`**
```python
from ISLP.models import summarize

X = MS(['income', 'balance']).fit_transform(Default)
y = (Default['default'] == 'Yes').astype(int)

glm_fit = sm.GLM(y, X, family=sm.families.Binomial()).fit()
print(summarize(glm_fit)[['coef', 'std err']])
```
* **What this gives:** `std err` outputs the standard formula-based standard errors for `income` and `balance` (typically around `4.99e-6` for `income` and `2.27e-4` for `balance`).

#### **(b) Write `boot_fn()`**
```python
def boot_fn(D, idx):
    D_ = D.loc[idx]
    X_ = MS(['income', 'balance']).fit_transform(D_)
    y_ = (D_['default'] == 'Yes').astype(int)
    fit = sm.GLM(y_, X_, family=sm.families.Binomial()).fit()
    return fit.params[['income', 'balance']]
```

#### **(c) Estimate standard errors using the bootstrap**
Using the `boot_SE()` helper function from the Section 5.3 lab:
```python
def boot_SE(func, D, n=None, B=1000, seed=0):
    rng = np.random.default_rng(seed)
    first_, second_ = 0, 0
    n = n or D.shape[0]
    for _ in range(B):
        idx = rng.choice(D.index, n, replace=True)
        value = func(D, idx)
        first_ += value
        second_ += value**2
    return np.sqrt(second_ / B - (first_ / B)**2)

boot_se = boot_SE(boot_fn, Default, B=1000, seed=0)
print(boot_se)
```

#### **(d) Comment on `sm.GLM()` vs. Bootstrap standard errors**
* **Comparison:** The standard errors estimated by `sm.GLM()` and the bootstrap are **very close** to each other.
* **Why:** Unlike the `Auto` linear regression example in the lab (where a non-linear relationship violated model assumptions), the logistic regression model fits the `Default` data well. When the model's assumptions hold, the standard mathematical formulas used by `sm.GLM()` are accurate and closely match the assumption-free bootstrap estimates.

Here are the concise, organized solutions (with ready-to-run Python code matching the `ISLP` lab style) for **Questions 7 and 8** from **Section 5.4 (Applied Exercises)**.

---

### **Question 7: Manual LOOCV on the `Weekly` Data**

#### **Setup**
```python
import numpy as np
import statsmodels.api as sm
from ISLP import load_data
from ISLP.models import ModelSpec as MS

Weekly = load_data('Weekly')
X = MS(['Lag1', 'Lag2']).fit_transform(Weekly)
y = (Weekly['Direction'] == 'Up').astype(int)
```

#### **(a) Fit logistic regression on all observations**
```python
model_all = sm.GLM(y, X, family=sm.families.Binomial()).fit()
```

#### **(b) Fit logistic regression using all *but* the 1st observation**
```python
model_minus_1 = sm.GLM(y.iloc[1:], X.iloc[1:], family=sm.families.Binomial()).fit()
```

#### **(c) Predict the 1st observation & check if correct**
```python
prob_1 = model_minus_1.predict(X.iloc[[0]]).iloc[0]
pred_1 = int(prob_1 > 0.5)
is_correct = (pred_1 == y.iloc[0])
print(f"Predicted: {pred_1}, Actual: {y.iloc[0]}, Correct: {is_correct}")
```
* **Result:** The model predicts `"Up"` ($P > 0.5$), while the actual direction is `"Down"` (`0`), so the first observation is **misclassified** (`False`).

#### **(d) Write the LOOCV `for` loop for all $n$ observations**
```python
n = len(Weekly)
errors = np.zeros(n)

for i in range(n):
    # i. Fit model leaving out the ith observation
    X_train = X.drop(index=X.index[i])
    y_train = y.drop(index=y.index[i])
    fit = sm.GLM(y_train, X_train, family=sm.families.Binomial()).fit()
    
    # ii. Posterior probability for the ith observation
    prob_i = fit.predict(X.iloc[[i]]).iloc[0]
    
    # iii. Predict Up (1) if prob > 0.5, else Down (0)
    pred_i = int(prob_i > 0.5)
    
    # iv. Record 1 if error, 0 if correct
    errors[i] = int(pred_i != y.iloc[i])
```

#### **(e) Compute LOOCV test error & comment**
```python
loocv_error = np.mean(errors)
print("LOOCV Error Rate:", loocv_error)
```
* **Comment:** The LOOCV error rate is around **45%** (`~0.450`). Since random guessing gives a 50% error rate, `Lag1` and `Lag2` provide only very weak predictive power for weekly market direction.

---

### **Question 8: LOOCV on Simulated Quadratic Data**

#### **(a) Generate data, identify $n$ and $p$, and write the equation**
```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(1)
x = rng.normal(size=100)
y = x - 2 * x**2 + rng.normal(size=100)
df = pd.DataFrame({'X': x, 'Y': y})
```
* **$n$ and $p$:** $n = \mathbf{100}$ observations, and $p = \mathbf{1}$ predictor ($X$).
* **Model equation:**
  $$Y = X - 2X^2 + \epsilon, \quad \text{where } \epsilon \sim \mathcal{N}(0, 1)$$

#### **(b) Scatterplot of $X$ against $Y$**
```python
import matplotlib.pyplot as plt

plt.scatter(df['X'], df['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```
* **Observation:** The plot shows a clear **inverted U-shape** (a curved quadratic relationship), peaking near $X \approx 0.25$ and curving downward for both larger positive and negative values of $X$.

#### **(c) Compute LOOCV errors for polynomial models (degrees 1–4)**
```python
from sklearn.model_selection import cross_validate
from ISLP.models import ModelSpec as MS, poly, sklearn_sm
import statsmodels.api as sm

rng_cv = np.random.default_rng(10)  # Random seed (note: LOOCV doesn't use it)
loocv_errors = []

for d in range(1, 5):
    X_poly = MS([poly('X', degree=d, raw=True)])
    model = sklearn_sm(sm.OLS, X_poly)
    cv_res = cross_validate(model, df, df['Y'], cv=len(df))
    loocv_errors.append(np.mean(cv_res['test_score']))

print("LOOCV MSE (degrees 1 to 4):", loocv_errors)
```

#### **(d) Repeat (c) with a different random seed**
* **Are the results the same?** **Yes, they are 100% identical.**
* **Why:** LOOCV has **no randomness** in its splitting process—it deterministically leaves out each of the $n = 100$ observations one by one. Therefore, changing the random seed has no effect on LOOCV.

#### **(e) Which model had the smallest LOOCV error?**
* **Answer:** **Model ii (the quadratic model, degree 2)** has the smallest LOOCV error (a sharp drop from degree 1 to degree 2, with slightly higher error for degrees 3 and 4).
* **Is this expected?** **Yes.** The true relationship used to generate the data ($Y = X - 2X^2 + \epsilon$) is quadratic, so a degree-2 polynomial captures the true signal without overfitting.

#### **(f) Statistical significance of coefficients vs. LOOCV results**
```python
from ISLP.models import summarize

for d in range(1, 5):
    X_d = MS([poly('X', degree=d, raw=True)]).fit_transform(df)
    fit_d = sm.OLS(df['Y'], X_d).fit()
    print(f"\n--- Degree {d} ---")
    print(summarize(fit_d)[['coef', 'p-value']])
```
* **Observation:** Across all four models, the linear ($X$) and quadratic ($X^2$) terms are **highly statistically significant** (very small p-values), while the cubic ($X^3$) and quartic ($X^4$) terms are **not significant** (large p-values).
* **Agreement:** This **agrees completely** with the LOOCV results—both methods confirm that the true underlying model is quadratic (degree 2) and adding higher-order terms is unnecessary.
Here is the concise, organized solution (with ready-to-run Python code) for **Question 9** from **Section 5.4 (Applied Exercises)**. *(Note: Question 9 is the final question in Chapter 5's exercise section.)*

---

### **Question 9: Bootstrap on the `Boston` Housing Data**

#### **Setup**
```python
import numpy as np
from ISLP import load_data

Boston = load_data('Boston')
medv = Boston['medv']
```

#### **(a) Estimate the population mean ($\hat{\mu}$)**
```python
mu_hat = medv.mean()
print("Mean (mu_hat):", mu_hat)
```
* **Result:** $\hat{\mu} \approx \mathbf{22.53}$ (in $1,000s).

#### **(b) Estimate the standard error of $\hat{\mu}$ using the formula**
```python
se_formula = medv.std() / np.sqrt(len(medv))
print("Formula SE:", se_formula)
```
* **Result:** $\text{SE}(\hat{\mu}) \approx \mathbf{0.409}$.
* **Interpretation:** If we repeatedly took random samples of size 506 from the population, the sample mean $\hat{\mu}$ would typically differ from the true population mean $\mu$ by about **0.41** ($410) on average.

#### **(c) Estimate the standard error of $\hat{\mu}$ using the bootstrap**
Using a bootstrap helper function (like `boot_SE` from the lab):
```python
def boot_stat(data, stat_fn, B=1000, seed=0):
    rng = np.random.default_rng(seed)
    estimates = [stat_fn(rng.choice(data, size=len(data), replace=True)) for _ in range(B)]
    return np.std(estimates, ddof=1)

se_boot = boot_stat(medv, np.mean)
print("Bootstrap SE:", se_boot)
```
* **Comparison:** The bootstrap SE ($\approx \mathbf{0.41}$) is **virtually identical** to the formula-based SE from part (b).

#### **(d) 95% Confidence Interval for the mean of `medv`**
```python
ci_boot = [mu_hat - 2 * se_boot, mu_hat + 2 * se_boot]
ci_formula = [mu_hat - 2 * se_formula, mu_hat + 2 * se_formula]

print("Bootstrap 95% CI:", ci_boot)
print("Formula 95% CI:  ", ci_formula)
```
* **Comparison:** Both intervals are nearly identical (around **[21.71, 23.35]**), because the bootstrap SE and formula SE are almost the same.

#### **(e) Estimate the population median ($\hat{\mu}_{med}$)**
```python
mu_med = medv.median()
print("Median (mu_med):", mu_med)
```
* **Result:** $\hat{\mu}_{med} \approx \mathbf{21.2}$.

#### **(f) Bootstrap standard error of $\hat{\mu}_{med}$**
```python
se_med_boot = boot_stat(medv, np.median)
print("Bootstrap SE (median):", se_med_boot)
```
* **Findings:** The bootstrap SE of the median is small (around **0.38**), which is even slightly smaller than the SE of the mean. Even though there is no simple formula for the SE of a median, the bootstrap easily shows that our median estimate ($\approx 21.2$) is very precise.

#### **(g) Estimate the 10th percentile ($\hat{\mu}_{0.1}$)**
```python
mu_01 = np.percentile(medv, 10)
print("10th Percentile (mu_0.1):", mu_01)
```
* **Result:** $\hat{\mu}_{0.1} \approx \mathbf{12.75}$.

#### **(h) Bootstrap standard error of $\hat{\mu}_{0.1}$**
```python
se_01_boot = boot_stat(medv, lambda x: np.percentile(x, 10))
print("Bootstrap SE (10th percentile):", se_01_boot)
```
* **Findings:** The bootstrap SE of the 10th percentile is around **0.50**. It is still relatively small compared to $\hat{\mu}_{0.1} \approx 12.75$, though slightly larger than the SE of the median—which makes sense because there are fewer data points in the lower tail of the distribution.

---

That completes all the exercises in **Chapter 5 (Resampling Methods)**! Let me know if you'd like any further clarification or help with another chapter.

