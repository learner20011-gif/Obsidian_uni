
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
* **Goal / Steps:** Bring in the tools we need and load the `Default` dataset.
* **Line-by-line (What & Why):**
  * `import numpy as np` — Brings in `numpy` for easy math (like finding averages).
  * `import statsmodels.api as sm` — Brings in `statsmodels` to build our regression models.
  * `from ISLP import load_data` — Brings in a helper to load the book's datasets.
  * `from ISLP.models import ModelSpec as MS` — Picks which columns to use and turns text (like Yes/No) into numbers automatically.
  * `from sklearn.model_selection import train_test_split` — Splits our data randomly into a study group (train) and a test group (valid).
  * `Default = load_data('Default')` — Loads the credit card default table and names it `Default`.

#### **(a) Fit logistic regression on the full data (`income` + `balance`)**
```python
X = MS(['income', 'balance']).fit_transform(Default)
y = (Default['default'] == 'Yes').astype(int)

model = sm.GLM(y, X, family=sm.families.Binomial()).fit()
```
* **Goal / Steps:** Pick `income` and `balance` as inputs (`X`), turn `'Yes'`/`'No'` into `1`/`0` (`y`), and train the model on all rows.
* **Line-by-line (What & Why):**
  * `X = MS(['income', 'balance']).fit_transform(Default)` — Grabs the `income` and `balance` columns (plus a starting baseline number). **Why:** The model needs clean number columns to learn from.
  * `y = (Default['default'] == 'Yes').astype(int)` — Changes `'Yes'` to `1` and `'No'` to `0`. **Why:** Computers need numbers (`1` or `0`), not words, to do math.
  * `model = sm.GLM(y, X, family=sm.families.Binomial()).fit()` — Trains a Yes/No prediction model (Logistic Regression) on the data. **Why:** `Binomial()` tells Python we are predicting a Yes/No outcome, not a regular number.

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
* **Goal / Steps:** Cut the data in half $\rightarrow$ teach the model on the first half $\rightarrow$ guess the answers on the second half $\rightarrow$ see how often it gets them wrong.
* **Line-by-line (What & Why):**
  * `def val_error(seed, predictors=['income', 'balance']):` — Makes a reusable recipe that takes a random `seed` number and a list of columns. **Why:** Saves us from copy-pasting the same code in parts (c) and (d).
  * `train, valid = train_test_split(Default, test_size=0.5, random_state=seed)` — Randomly puts half the rows in `train` and half in `valid`. **Why:** Testing on rows the model has never seen shows how well it works in real life. Using `seed` lets us get the exact same split again if we want.
  * `mm = MS(predictors)` — Sets up the rule for which columns to pick. **Why:** We want to set the rules on `train` and use the exact same rules on `valid`.
  * `X_train = mm.fit_transform(train)` — Builds the input table from `train` only. **Why:** We must not peek at `valid` while setting up `train`.
  * `y_train = (train['default'] == 'Yes').astype(int)` — Turns `'Yes'`/`'No'` in `train` into `1`/`0`.
  * `fit = sm.GLM(y_train, X_train, family=sm.families.Binomial()).fit()` — Trains the model using `train` only. **Why:** The model should only learn from the training half.
  * `X_valid = mm.transform(valid)` — Uses the same column rules on `valid`. **Why:** Makes sure `valid` has the exact same setup as `train`.
  * `y_valid = (valid['default'] == 'Yes').astype(int)` — Turns the real answers in `valid` into `1`/`0` so we can check our guesses.
  * `probs = fit.predict(X_valid)` — Asks the model for the chance (0% to 100%) that each person in `valid` will default. **Why:** This model gives a chance/probability first, not a direct Yes/No.
  * `preds = (probs > 0.5).astype(int)` — If the chance is over 50% (`0.5`), guess `1` (Yes); otherwise guess `0` (No). **Why:** Turns the probability into a clear Yes/No guess.
  * `return np.mean(preds != y_valid)` — Checks where our guess was wrong (`1` if wrong, `0` if right) and takes the average. **Why:** Gives the overall wrong-guess rate (error rate).
  * `print("Validation Error (seed=0):", val_error(0))` — Runs the recipe with `seed=0` and shows the error.
* **What happens:** The model typically achieves a low validation error rate around **2.5% – 2.9%**.

#### **(c) Repeat 3 times with different random splits**
```python
for s in [1, 2, 3]:
    print(f"Seed {s} Error:", val_error(s))
```
* **Goal / Steps:** Run the same test 3 more times using different random splits (`1`, `2`, `3`).
* **Line-by-line (What & Why):**
  * `for s in [1, 2, 3]:` — Repeats the code for seeds `1`, `2`, and `3`. **Why:** Each seed shuffles and splits the data differently.
  * `print(f"Seed {s} Error:", val_error(s))` — Prints the error for each split so we can see how much the score jumps around.
* **Comment:** Each split gives a slightly different validation error rate (usually varying around **2.4% – 2.9%**). This shows a key drawback of the validation set approach: the estimated test error depends on which observations happen to land in the training vs. validation set.

#### **(d) Add dummy variable for `student`**
```python
# MS() automatically converts 'student' ('Yes'/'No') into a dummy variable
for s in [0, 1, 2, 3]:
    print(f"Seed {s} Error (with student):", val_error(s, ['income', 'balance', 'student']))
```
* **Goal / Steps:** Run the exact same 4 splits (`0, 1, 2, 3`), but also give the model the `student` column.
* **Line-by-line (What & Why):**
  * `for s in [0, 1, 2, 3]:` — Uses the same 4 seeds as before. **Why:** Keeps the test fair so we can compare "with student" vs "without student".
  * `print(..., val_error(s, ['income', 'balance', 'student']))` — Runs `val_error` with `'student'` added (`MS` turns `'Yes'`/`'No'` into `1`/`0` for us). **Why:** Checks if knowing whether someone is a student helps the model make fewer mistakes.
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
* **Goal / Steps:** Fit the model on all rows and print its weights and math-formula error margins (standard errors).
* **Line-by-line (What & Why):**
  * `from ISLP.models import summarize` — Brings in `summarize` to show the model's results in a neat table.
  * `X = MS(['income', 'balance']).fit_transform(Default)` — Grabs `income` and `balance` (plus baseline).
  * `y = (Default['default'] == 'Yes').astype(int)` — Turns `'Yes'`/`'No'` into `1`/`0`.
  * `glm_fit = sm.GLM(y, X, family=sm.families.Binomial()).fit()` — Trains the Yes/No model on all the data. **Why:** When it finishes, Python automatically calculates the formula-based error margin (`std err`) for each weight.
  * `print(summarize(glm_fit)[['coef', 'std err']])` — Shows just the weights (`coef`) and error margins (`std err`). **Why:** We want to compare these numbers with the bootstrap numbers next.
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
* **Goal / Steps:** Take a dataset `D` and a list of picked row numbers `idx`, build a new sample from those rows, train the model, and hand back the `income` and `balance` weights.
* **Line-by-line (What & Why):**
  * `def boot_fn(D, idx):` — Creates a helper function that takes the table `D` and a list of row numbers `idx`. **Why:** `boot_SE()` needs a function in this exact format.
  * `D_ = D.loc[idx]` — Picks out the rows listed in `idx` (some rows can appear more than once). **Why:** This creates one bootstrap sample.
  * `X_ = MS(['income', 'balance']).fit_transform(D_)` — Gets the `income` and `balance` columns from this sample.
  * `y_ = (D_['default'] == 'Yes').astype(int)` — Turns `'Yes'`/`'No'` in this sample into `1`/`0`.
  * `fit = sm.GLM(y_, X_, family=sm.families.Binomial()).fit()` — Trains the model on this sample. **Why:** Every random sample gives slightly different weights.
  * `return fit.params[['income', 'balance']]` — Hands back just the two weights for `income` and `balance`. **Why:** The question only asks for the error margins of these two weights.

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
* **Goal / Steps:** Repeat `1,000` times: pick `n` random rows **with replacement** (allowing repeats) $\rightarrow$ run `boot_fn` to get the weights $\rightarrow$ measure how much those 1,000 weights spread out (standard error).
* **Line-by-line (What & Why):**
  * `def boot_SE(func, D, n=None, B=1000, seed=0):` — Sets up the bootstrap calculator.
  * `rng = np.random.default_rng(seed)` — Sets a random number picker with a `seed` so we get the same answer every time.
  * `first_, second_ = 0, 0` — Two running totals to add up the weights and the squared weights. **Why:** Lets us find the spread at the end without saving all 1,000 results in a huge list.
  * `n = n or D.shape[0]` — Sets the sample size `n` to match the total number of rows in `D`. **Why:** A bootstrap sample is always the same size as the original table.
  * `for _ in range(B):` — Repeats the loop `B` (1,000) times. **Why:** Doing it many times gives a steady, reliable answer.
  * `idx = rng.choice(D.index, n, replace=True)` — Randomly picks `n` row numbers, putting each one back so it can be picked again (`replace=True`). **Why:** Picking with replacement is the main idea of the bootstrap.
  * `value = func(D, idx)` — Runs `boot_fn` on those picked rows to get the two weights.
  * `first_ += value` & `second_ += value**2` — Adds the weights and squared weights to the running totals. **Why:** Needed for the spread (standard deviation) formula on the next line.
  * `return np.sqrt(second_ / B - (first_ / B)**2)` — Calculates how much the 1,000 weights bounce around (their standard deviation = bootstrap standard error).
  * `boot_se = boot_SE(boot_fn, Default, B=1000, seed=0)` — Runs the bootstrap 1,000 times on `Default`.
  * `print(boot_se)` — Shows the bootstrap error margins for `income` and `balance`.

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
* **Goal / Steps:** Load the `Weekly` stock data, pick `Lag1` and `Lag2` as inputs, and turn `'Up'`/`'Down'` into `1`/`0`.
* **Line-by-line (What & Why):**
  * `Weekly = load_data('Weekly')` — Loads the `Weekly` stock market dataset.
  * `X = MS(['Lag1', 'Lag2']).fit_transform(Weekly)` — Picks `Lag1` and `Lag2` (plus a baseline) as inputs.
  * `y = (Weekly['Direction'] == 'Up').astype(int)` — Turns `'Up'` into `1` and `'Down'` into `0` so the model can work with numbers.

#### **(a) Fit logistic regression on all observations**
```python
model_all = sm.GLM(y, X, family=sm.families.Binomial()).fit()
```
* **Line-by-line (What & Why):** Trains the Yes/No model using every single week in the table. **Why:** Gives us our starting full-data model.

#### **(b) Fit logistic regression using all *but* the 1st observation**
```python
model_minus_1 = sm.GLM(y.iloc[1:], X.iloc[1:], family=sm.families.Binomial()).fit()
```
* **Line-by-line (What & Why):** `.iloc[1:]` means "start from row 1 and take everything after" (so it skips row `0`, the very 1st week). **Why:** Leaves out the 1st week so we can test our model on it honestly.

#### **(c) Predict the 1st observation & check if correct**
```python
prob_1 = model_minus_1.predict(X.iloc[[0]]).iloc[0]
pred_1 = int(prob_1 > 0.5)
is_correct = (pred_1 == y.iloc[0])
print(f"Predicted: {pred_1}, Actual: {y.iloc[0]}, Correct: {is_correct}")
```
* **Goal / Steps:** Guess the 1st week using the model from (b), turn the chance into `1` or `0`, and check if it matches what really happened.
* **Line-by-line (What & Why):**
  * `prob_1 = model_minus_1.predict(X.iloc[[0]]).iloc[0]` — Asks the model for the chance that week `0` goes `"Up"`. (`X.iloc[[0]]` keeps it in table shape for `.predict()`, and `.iloc[0]` grabs the single number).
  * `pred_1 = int(prob_1 > 0.5)` — Guesses `1` (`Up`) if the chance is over 50%, otherwise `0` (`Down`).
  * `is_correct = (pred_1 == y.iloc[0])` — Checks if our guess matches the real answer (`True` or `False`).
  * `print(...)` — Shows our guess, the real answer, and whether we got it right.
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
* **Goal / Steps:** Make an empty scoreboard (`errors`) of `n` zeros $\rightarrow$ go through every week `i` one by one: hide week `i`, train on all other weeks, guess week `i`, and write `1` if wrong or `0` if right.
* **Line-by-line (What & Why):**
  * `n = len(Weekly)` — Counts how many weeks are in the table.
  * `errors = np.zeros(n)` — Makes a list of `n` zeros to hold our `1` (wrong) or `0` (right) scores. **Why:** Easier and faster than growing a list step by step.
  * `for i in range(n):` — Loops through every single week `i` from `0` to `n-1`. **Why:** LOOCV tests every single row once by leaving it out.
  * `X_train = X.drop(index=X.index[i])` & `y_train = y.drop(index=y.index[i])` — Removes week `i` from `X` and `y`. **Why:** Trains the model on all the *other* weeks.
  * `fit = sm.GLM(y_train, X_train, family=sm.families.Binomial()).fit()` — Trains the model without week `i`.
  * `prob_i = fit.predict(X.iloc[[i]]).iloc[0]` — Gets the predicted chance of `"Up"` for the hidden week `i`.
  * `pred_i = int(prob_i > 0.5)` — Turns the chance into `1` (`Up`) or `0` (`Down`).
  * `errors[i] = int(pred_i != y.iloc[i])` — Writes `1` if our guess was wrong, or `0` if right, so we can average them next.

#### **(e) Compute LOOCV test error & comment**
```python
loocv_error = np.mean(errors)
print("LOOCV Error Rate:", loocv_error)
```
* **Line-by-line (What & Why):**
  * `loocv_error = np.mean(errors)` — Takes the average of all the `1`s and `0`s in `errors`. **Why:** The average of `1`s and `0`s tells us what percent of weeks we guessed wrong.
  * `print("LOOCV Error Rate:", loocv_error)` — Prints the final error rate (~0.45, or 45%).
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
* **Goal / Steps:** Make 100 random `x` numbers, calculate `y = x - 2x^2 + noise`, and put them in a table.
* **Line-by-line (What & Why):**
  * `rng = np.random.default_rng(1)` — Picks random numbers using seed `1` so we get the same fake data every time.
  * `x = rng.normal(size=100)` — Creates 100 random `x` values around `0` (bell-curve style).
  * `y = x - 2 * x**2 + rng.normal(size=100)` — Builds a curved shape ($x - 2x^2$) and adds random noise. **Why:** Real-world data always has some random noise on top of the true pattern.
  * `df = pd.DataFrame({'X': x, 'Y': y})` — Puts `x` and `y` into a clean table named `df` so the next tools can read it easily.
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
* **Goal / Steps:** Draw a dot plot of `X` vs `Y`.
* **Line-by-line (What & Why):**
  * `plt.scatter(df['X'], df['Y'])` — Draws a dot for every `(X, Y)` pair. **Why:** Lets us see with our own eyes that the data forms an upside-down U curve.
  * `plt.xlabel('X')` / `plt.ylabel('Y')` — Names the bottom and side axes.
  * `plt.show()` — Pops up the chart on screen.
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
* **Goal / Steps:** Test 4 curve powers (`d = 1, 2, 3, 4`): build the curve inputs $\rightarrow$ run automatic LOOCV (`cv = 100`) $\rightarrow$ save the average error for each power.
* **Line-by-line (What & Why):**
  * `from sklearn.model_selection import cross_validate` — Brings in `cross_validate` to run cross-validation automatically without writing a manual loop.
  * `from ISLP.models import ModelSpec as MS, poly, sklearn_sm` — Brings in `poly` (to make $X, X^2, \dots, X^d$) and `sklearn_sm` (so `statsmodels` can plug into `cross_validate`).
  * `rng_cv = np.random.default_rng(10)` — Makes a random seed (LOOCV doesn't actually use it, which we prove in part (d)).
  * `loocv_errors = []` — Empty list to hold the error score for each of the 4 models.
  * `for d in range(1, 5):` — Loops through powers `1, 2, 3, 4`.
  * `X_poly = MS([poly('X', degree=d, raw=True)])` — Tells the model to use powers up to $X^d$ (`raw=True` keeps plain $X, X^2, \dots$). **Why:** Lets us test a straight line (`d=1`), a U-curve (`d=2`), and wigglier curves (`d=3, 4`).
  * `model = sklearn_sm(sm.OLS, X_poly)` — Wraps `sm.OLS` (regular linear regression) so `cross_validate` knows how to run it.
  * `cv_res = cross_validate(model, df, df['Y'], cv=len(df))` — Runs cross-validation with `cv=100` (the number of rows in `df`). **Why:** When `cv` equals the number of rows, it leaves out 1 row at a time (exact LOOCV).
  * `loocv_errors.append(np.mean(cv_res['test_score']))` — Averages the 100 test errors and adds the result to our list.
  * `print("LOOCV MSE (degrees 1 to 4):", loocv_errors)` — Prints the 4 error scores so we can see which curve fits best.

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
* **Goal / Steps:** Train each of the 4 curve models (`d = 1..4`) on all 100 rows and print each term's weight and p-value.
* **Line-by-line (What & Why):**
  * `for d in range(1, 5):` — Loops through powers 1 to 4.
  * `X_d = MS([poly('X', degree=d, raw=True)]).fit_transform(df)` — Builds the input table with powers up to $X^d$.
  * `fit_d = sm.OLS(df['Y'], X_d).fit()` — Fits regular regression on all 100 rows.
  * `print(f"\n--- Degree {d} ---")` — Prints a clear title for each model.
  * `print(summarize(fit_d)[['coef', 'p-value']])` — Shows each term's weight (`coef`) and `p-value`. **Why:** A tiny p-value (< 0.05) means that term really matters ($X$ and $X^2$), while a big p-value means it's just noise ($X^3$ and $X^4$).
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
* **Line-by-line (What & Why):**
  * `Boston = load_data('Boston')` — Loads the Boston housing dataset.
  * `medv = Boston['medv']` — Grabs just the `medv` column (home prices in $1,000s) so it's short and easy to use.

#### **(a) Estimate the population mean ($\hat{\mu}$)**
```python
mu_hat = medv.mean()
print("Mean (mu_hat):", mu_hat)
```
* **Line-by-line (What & Why):**
  * `mu_hat = medv.mean()` — Finds the average home price. **Why:** The sample average is our best guess for the true overall average.
  * `print("Mean (mu_hat):", mu_hat)` — Shows the average.
* **Result:** $\hat{\mu} \approx \mathbf{22.53}$ (in $1,000s).

#### **(b) Estimate the standard error of $\hat{\mu}$ using the formula**
```python
se_formula = medv.std() / np.sqrt(len(medv))
print("Formula SE:", se_formula)
```
* **Line-by-line (What & Why):**
  * `se_formula = medv.std() / np.sqrt(len(medv))` — Divides the spread of prices (`std`) by the square root of how many homes we have (`len(medv)`). **Why:** Classic math formula for how much our average guess might be off.
  * `print("Formula SE:", se_formula)` — Shows the formula error margin.
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
* **Goal / Steps:** Repeat `1,000` times: pick `n` home prices **with replacement** (repeats allowed) and run `stat_fn` $\rightarrow$ measure how spread out those `1,000` answers are.
* **Line-by-line (What & Why):**
  * `def boot_stat(data, stat_fn, B=1000, seed=0):` — Makes a general bootstrap helper that works for **any** math function (`stat_fn`). **Why:** We can reuse this for the mean (c), median (f), and 10th percentile (h).
  * `rng = np.random.default_rng(seed)` — Sets a random picker with a `seed` so we get the same result each time.
  * `estimates = [stat_fn(rng.choice(data, size=len(data), replace=True)) for _ in range(B)]` — Runs `1,000` times: picks `len(data)` prices with replacement (`replace=True`) and calculates `stat_fn` on each batch. **Why:** Acts like taking 1,000 new surveys of homes.
  * `return np.std(estimates, ddof=1)` — Measures how much the 1,000 answers bounce around (`ddof=1` divides by $B - 1$). **Why:** That spread is the bootstrap standard error.
  * `se_boot = boot_stat(medv, np.mean)` — Runs the bootstrap using `np.mean` (average).
  * `print("Bootstrap SE:", se_boot)` — Shows the bootstrap error margin to compare with part (b).
* **Comparison:** The bootstrap SE ($\approx \mathbf{0.41}$) is **virtually identical** to the formula-based SE from part (b).

#### **(d) 95% Confidence Interval for the mean of `medv`**
```python
ci_boot = [mu_hat - 2 * se_boot, mu_hat + 2 * se_boot]
ci_formula = [mu_hat - 2 * se_formula, mu_hat + 2 * se_formula]

print("Bootstrap 95% CI:", ci_boot)
print("Formula 95% CI:  ", ci_formula)
```
* **Line-by-line (What & Why):**
  * `ci_boot = [mu_hat - 2 * se_boot, mu_hat + 2 * se_boot]` — Takes our average guess and goes 2 error margins down and 2 up. **Why:** Gives a 95% range where the true average likely sits.
  * `ci_formula = [mu_hat - 2 * se_formula, mu_hat + 2 * se_formula]` — Does the exact same thing using the formula error margin so we can compare them.
  * `print(...)` — Shows both ranges.
* **Comparison:** Both intervals are nearly identical (around **[21.71, 23.35]**), because the bootstrap SE and formula SE are almost the same.

#### **(e) Estimate the population median ($\hat{\mu}_{med}$)**
```python
mu_med = medv.median()
print("Median (mu_med):", mu_med)
```
* **Line-by-line (What & Why):**
  * `mu_med = medv.median()` — Finds the exact middle home price. **Why:** A few super expensive houses don't pull the median up like they do the average.
  * `print("Median (mu_med):", mu_med)` — Shows the middle price.
* **Result:** $\hat{\mu}_{med} \approx \mathbf{21.2}$.

#### **(f) Bootstrap standard error of $\hat{\mu}_{med}$**
```python
se_med_boot = boot_stat(medv, np.median)
print("Bootstrap SE (median):", se_med_boot)
```
* **Line-by-line (What & Why):**
  * `se_med_boot = boot_stat(medv, np.median)` — Reuses `boot_stat` with `np.median`. **Why:** There is no easy math formula for the error margin of a median, so bootstrap is the easiest way to find it.
  * `print("Bootstrap SE (median):", se_med_boot)` — Shows the median's bootstrap error margin.
* **Findings:** The bootstrap SE of the median is small (around **0.38**), which is even slightly smaller than the SE of the mean. Even though there is no simple formula for the SE of a median, the bootstrap easily shows that our median estimate ($\approx 21.2$) is very precise.

#### **(g) Estimate the 10th percentile ($\hat{\mu}_{0.1}$)**
```python
mu_01 = np.percentile(medv, 10)
print("10th Percentile (mu_0.1):", mu_01)
```
* **Line-by-line (What & Why):**
  * `mu_01 = np.percentile(medv, 10)` — Finds the price where 10% of homes are cheaper and 90% are pricier. **Why:** Tells us what the lower-priced homes look like.
  * `print("10th Percentile (mu_0.1):", mu_01)` — Shows the 10th percentile price.
* **Result:** $\hat{\mu}_{0.1} \approx \mathbf{12.75}$.

#### **(h) Bootstrap standard error of $\hat{\mu}_{0.1}$**
```python
se_01_boot = boot_stat(medv, lambda x: np.percentile(x, 10))
print("Bootstrap SE (10th percentile):", se_01_boot)
```
* **Line-by-line (What & Why):**
  * `se_01_boot = boot_stat(medv, lambda x: np.percentile(x, 10))` — Passes a quick mini-function (`lambda`) into `boot_stat`. **Why:** `np.percentile` needs two inputs (`data` and `10`), so `lambda` wraps it into a 1-input function for `boot_stat`. Again, bootstrap works easily even though there's no simple math formula for percentiles.
  * `print("Bootstrap SE (10th percentile):", se_01_boot)` — Shows the 10th percentile's bootstrap error margin.
* **Findings:** The bootstrap SE of the 10th percentile is around **0.50**. It is still relatively small compared to $\hat{\mu}_{0.1} \approx 12.75$, though slightly larger than the SE of the median—which makes sense because there are fewer data points in the lower tail of the distribution.

---

That completes all the exercises in **Chapter 5 (Resampling Methods)**! Let me know if you'd like any further clarification or help with another chapter.


### Lab: Cross-Validation and the Bootstrap
```python
# ==============================================================================
# 0. SETUP & IMPORTS
# ==============================================================================

# Instruction: Silently download and install the textbook's custom Python package.
# Algo: Package management (setup).
# Why: Gives Kaggle access to the book's datasets (Carseats, Boston) and helper tools.
!pip install -q ISLP

# Instruction: Load NumPy and give it the short nickname 'np'.
# Algo: Fast array and matrix math.
# Why: Machine learning models process data as grids of numbers, not raw text.
import numpy as np

# Instruction: Load Pandas and give it the short nickname 'pd'.
# Algo: Tabular data handling (rows and columns).
# Why: Lets us easily view, sort, and clean spreadsheet-style datasets.
import pandas as pd

# Instruction: Load the subplot drawing tool from Matplotlib.
# Algo: Data visualization.
# Why: Allows us to draw decision trees and error curves to visually inspect models.
from matplotlib.pyplot import subplots

# Instruction: Load model selection tools (train/test splitting, cross-validation, grid search).
# Algo: Resampling and model validation.
# Why: Prevents overfitting by testing models on data they haven't seen during training.
import sklearn.model_selection as skm

# Instruction: Load the dataset loader and confusion table helper from ISLP.
# Algo: Data loading and classification evaluation.
# Why: Quickly imports textbook datasets and prints a neat grid of right vs. wrong guesses.
from ISLP import load_data, confusion_table

# Instruction: Load ModelSpec and nickname it 'MS'.
# Algo: Design matrix preprocessing (one-hot encoding).
# Why: Automatically turns text categories into 0/1 numbers that math models require.
from ISLP.models import ModelSpec as MS

# Instruction: Load Classification Tree (DTC), Regression Tree (DTR), and tree plotting tools.
# Algo: Decision Trees (recursive binary splitting).
# Why: Core algorithms for splitting data into if-then rules for categories or numbers.
from sklearn.tree import (DecisionTreeClassifier as DTC,
                          DecisionTreeRegressor as DTR,
                          plot_tree,
                          export_text)

# Instruction: Load accuracy and log-loss scoring functions.
# Algo: Classification error metrics.
# Why: Measures what percentage of category predictions the model got right.
from sklearn.metrics import accuracy_score, log_loss

# Instruction: Load Random Forest (RF) and Gradient Boosting (GBR) regressors.
# Algo: Ensemble learning (Bagging and Boosting).
# Why: Combines hundreds of weak/noisy trees into one highly accurate prediction model.
from sklearn.ensemble import (RandomForestRegressor as RF,
                              GradientBoostingRegressor as GBR)

# Instruction: Load Bayesian Additive Regression Trees (BART).
# Algo: Bayesian MCMC tree ensemble.
# Why: Combines boosting and random forests while estimating prediction uncertainty.
from ISLP.bart import BART


# ==============================================================================
# 1. CLASSIFICATION TREES & PRUNING (Page 356)
# ==============================================================================

# Instruction: Load the Carseats store dataset into a table.
# Algo: Data ingestion.
# Why: Provides store features (Price, Advertising, ShelveLoc) to predict sales performance.
Carseats = load_data('Carseats')

# Instruction: Create a target list labeling Sales > 8 as "Yes" and <= 8 as "No".
# Algo: Binary target discretization.
# Why: Turns a continuous sales number into two classes so we can use a Classification Tree.
High = np.where(Carseats.Sales > 8, "Yes", "No")

# Instruction: Define a preprocessing blueprint using all columns except 'Sales' (and no intercept column).
# Algo: Feature selection & encoding setup.
# Why: Removes 'Sales' so the model doesn't cheat using the answer, and skips the intercept since trees don't need one.
model = MS(Carseats.columns.drop('Sales'), intercept=False)

# Instruction: Apply the blueprint to convert text columns (like ShelveLoc) into numeric dummy columns.
# Algo: One-hot / dummy variable encoding.
# Why: Decision tree math can only split on numbers, not words like "Good" or "Bad".
D = model.fit_transform(Carseats)

# Instruction: Save the list of column names for plotting later.
# Algo: Metadata extraction.
# Why: Lets the tree diagram show actual feature names instead of generic numbers like X[0].
feature_names = list(D.columns)

# Instruction: Convert the Pandas table into a pure NumPy number grid 'X'.
# Algo: Array conversion.
# Why: Scikit-learn algorithms run faster and cleaner on pure NumPy arrays.
X = np.asarray(D)

# Instruction: Randomly split X and High into 50% training data and 50% testing data.
# Algo: Hold-out validation split (fixed seed=0 for reproducibility).
# Why: Keeps half the data completely hidden so we can honestly grade the model at the end.
(X_train, X_test, High_train, High_test) = skm.train_test_split(
    X, High, test_size=0.5, random_state=0
)

# Instruction: Initialize a Classification Tree using 'entropy' to measure split quality.
# Algo: Greedy recursive binary splitting (Information Gain / Deviance).
# Why: Entropy tells the tree which split creates the purest groups of "Yes" and "No".
clf = DTC(criterion='entropy', random_state=0)

# Instruction: Grow the full unpruned classification tree on the training data.
# Algo: Top-down tree induction.
# Why: Learns all possible rules from the training set (though this full tree usually overfits).
clf.fit(X_train, High_train)

# Instruction: Calculate the sequence of pruning penalties (ccp_alphas) from a full tree down to a single root.
# Algo: Cost-complexity pruning path (minimizing Error + alpha * Leaves).
# Why: Generates candidate penalty values so we can test how much trimming gives the best accuracy.
ccp_path = clf.cost_complexity_pruning_path(X_train, High_train)

# Instruction: Set up a 10-fold cross-validation splitter that shuffles data reproducibly.
# Algo: K-Fold Cross-Validation (K=10).
# Why: Splits training data into 10 chunks so every chunk gets a turn acting as a mini-test set.
kfold = skm.KFold(10, random_state=1, shuffle=True)

# Instruction: Configure a grid search to test every ccp_alpha penalty across the 10 folds using accuracy.
# Algo: Hyperparameter tuning via Cross-Validation.
# Why: Finds the exact pruning penalty that prevents overfitting without touching the real test set.
grid = skm.GridSearchCV(
    clf,
    {'ccp_alpha': ccp_path.ccp_alphas},
    refit=True,
    cv=kfold,
    scoring='accuracy'
)

# Instruction: Run the 10-fold grid search on the training data and automatically retrain the winning tree.
# Algo: Automated model selection and refitting.
# Why: Executes all CV experiments and locks in the single best pruned tree.
grid.fit(X_train, High_train)

# Instruction: Print the highest average cross-validation accuracy found.
# Algo: Cross-validation performance metric.
# Why: Shows how well the winning pruned tree performed during internal validation.
print("Best CV Accuracy:", grid.best_score_)

# Instruction: Create a 12x12 inch blank figure canvas.
# Algo: Plot initialization.
# Why: Gives the tree diagram enough space so branch text doesn't overlap.
ax = subplots(figsize=(12, 12))[1]

# Instruction: Extract the single best pruned tree from the grid search.
# Algo: Estimator extraction.
# Why: Grabs the winning model so we can plot it and test it on unseen data.
best_ = grid.best_estimator_

# Instruction: Draw the pruned decision tree with feature names on the canvas.
# Algo: Tree visualization.
# Why: Lets humans inspect the exact if-then rules the model learned.
plot_tree(best_, feature_names=feature_names, ax=ax)

# Instruction: Predict "Yes"/"No" on the unseen test set and print the accuracy percentage.
# Algo: Out-of-sample generalization evaluation.
# Why: Measures true real-world performance on data the model has never seen.
print("Test Accuracy:", accuracy_score(High_test, best_.predict(X_test)))

# Instruction: Build a table comparing predicted labels against actual test labels.
# Algo: Confusion matrix.
# Why: Reveals whether errors come from false positives or false negatives.
confusion = confusion_table(best_.predict(X_test), High_test)

# Instruction: Display the confusion table.
# Algo: Diagnostic output.
# Why: Lets you read the exact counts of correct and incorrect guesses.
print(confusion)


# ==============================================================================
# 2. REGRESSION TREES (Pages 357–358)
# ==============================================================================

# Instruction: Load the Boston neighborhood housing dataset.
# Algo: Data ingestion.
# Why: Provides neighborhood stats (crime, rooms, poverty) to predict continuous house prices ('medv').
Boston = load_data("Boston")

# Instruction: Set up preprocessing for all predictors except the target 'medv'.
# Algo: Feature matrix definition.
# Why: Separates input features from the house price we want to predict.
model = MS(Boston.columns.drop('medv'), intercept=False)

# Instruction: Transform predictors into a clean numeric table.
# Algo: Feature matrix transformation.
# Why: Ensures all inputs are properly formatted numbers.
D = model.fit_transform(Boston)

# Instruction: Save predictor column names for plotting.
# Algo: Metadata extraction.
# Why: Displays readable variable names inside the regression tree boxes.
feature_names = list(D.columns)

# Instruction: Convert predictors into a NumPy array 'X'.
# Algo: Array conversion.
# Why: Prepares data in the standard array format required by Scikit-Learn.
X = np.asarray(D)

# Instruction: Split data into 70% training and 30% testing neighborhoods.
# Algo: Hold-out train/test split.
# Why: Reserves 30% of neighborhoods to evaluate price prediction errors honestly.
(X_train, X_test, y_train, y_test) = skm.train_test_split(
    X, Boston['medv'], test_size=0.3, random_state=0
)

# Instruction: Initialize a Regression Tree limited to at most 3 levels deep.
# Algo: Top-down greedy splitting minimizing Residual Sum of Squares (RSS).
# Why: Predicts the average house price inside each box while staying shallow enough to read easily.
reg = DTR(max_depth=3)

# Instruction: Train the 3-level regression tree on the training neighborhoods.
# Algo: Regression tree fitting.
# Why: Learns the top 3 most important price-splitting rules.
reg.fit(X_train, y_train)

# Instruction: Create a 12x12 figure canvas.
# Algo: Plot initialization.
# Why: Provides room to display the regression tree clearly.
ax = subplots(figsize=(12, 12))[1]

# Instruction: Plot the 3-level regression tree.
# Algo: Tree visualization.
# Why: Shows which variables (like room count 'rm' or status 'lstat') drive house prices most.
plot_tree(reg, feature_names=feature_names, ax=ax)

# Instruction: Compute candidate pruning penalties (ccp_alphas) for the regression tree.
# Algo: Cost-complexity pruning path (minimizing RSS + alpha * Leaves).
# Why: Lists possible tree sizes so CV can test whether trimming branches lowers test error.
ccp_path = reg.cost_complexity_pruning_path(X_train, y_train)

# Instruction: Create a 5-fold cross-validation splitter.
# Algo: K-Fold Cross-Validation (K=5).
# Why: Divides training data into 5 parts to test each pruning penalty reliably.
kfold = skm.KFold(5, shuffle=True, random_state=10)

# Instruction: Set up grid search over ccp_alphas scored by negative Mean Squared Error.
# Algo: Hyperparameter tuning via CV (maximizing -MSE = minimizing MSE).
# Why: Picks the tree complexity that minimizes squared price prediction errors.
grid = skm.GridSearchCV(
    reg,
    {'ccp_alpha': ccp_path.ccp_alphas},
    refit=True,
    cv=kfold,
    scoring='neg_mean_squared_error'
)

# Instruction: Run the 5-fold CV grid search and refit the best regression tree.
# Algo: Automated pruning selection.
# Why: Finds and trains the optimal pruned regression tree.
G = grid.fit(X_train, y_train)

# Instruction: Extract the best pruned regression tree.
# Algo: Estimator extraction.
# Why: Grabs the winning tree for testing and visualization.
best_ = grid.best_estimator_

# Instruction: Predict test prices, square the errors, average them (MSE), and print the result.
# Algo: Mean Squared Error (MSE) evaluation.
# Why: Gives a single benchmark number (lower is better) to compare against Random Forests and Boosting.
print("Pruned Regression Tree Test MSE:", np.mean((y_test - best_.predict(X_test))**2))

# Instruction: Create another 12x12 figure canvas.
# Algo: Plot initialization.
# Why: Prepares space to draw the final pruned regression tree.
ax = subplots(figsize=(12, 12))[1]

# Instruction: Draw the optimal pruned regression tree.
# Algo: Tree visualization.
# Why: Lets us verify whether CV kept all branches or trimmed any away.
plot_tree(G.best_estimator_, feature_names=feature_names, ax=ax)


# ==============================================================================
# 3. BAGGING & RANDOM FORESTS (Pages 358–360)
# ==============================================================================

# Instruction: Initialize a Random Forest using ALL features at every split (which equals Bagging).
# Algo: Bootstrap Aggregation (Bagging) — 100 deep trees grown on bootstrap samples with m = p features.
# Why: Single trees have high variance; averaging 100 trees dramatically stabilizes predictions.
bag_boston = RF(max_features=X_train.shape[1], random_state=0)

# Instruction: Train all 100 bagged trees on the training data.
# Algo: Parallel ensemble training on random resamples with replacement.
# Why: Builds 100 slightly different trees whose random errors cancel out when averaged.
bag_boston.fit(X_train, y_train)

# Instruction: Create an 8x8 square plot canvas.
# Algo: Plot initialization.
# Why: Gives a balanced square grid to compare predicted vs. actual prices.
ax = subplots(figsize=(8, 8))[1]

# Instruction: Average predictions across all 100 bagged trees for the test set.
# Algo: Ensemble prediction averaging.
# Why: Produces smooth, low-variance house price predictions.
y_hat_bag = bag_boston.predict(X_test)

# Instruction: Plot predicted prices (x-axis) against actual prices (y-axis).
# Algo: Scatter plot diagnostic.
# Why: Visually checks if points form a tight diagonal line (meaning accurate predictions).
ax.scatter(y_hat_bag, y_test)

# Instruction: Calculate and print the Test MSE for 100 bagged trees.
# Algo: Mean Squared Error evaluation.
# Why: Proves that bagging cuts error roughly in half compared to a single regression tree.
print("Bagging (100 trees) Test MSE:", np.mean((y_test - y_hat_bag)**2))

# Instruction: Rebuild and fit Bagging using 500 trees instead of 100.
# Algo: Large-ensemble Bagging (n_estimators = 500).
# Why: Shows that increasing the number of trees stabilizes predictions without overfitting.
bag_boston = RF(max_features=X_train.shape[1], n_estimators=500, random_state=0).fit(X_train, y_train)

# Instruction: Generate test predictions from the 500-tree bagged ensemble.
# Algo: Ensemble averaging.
# Why: Gets updated predictions to check if 500 trees beat 100 trees.
y_hat_bag = bag_boston.predict(X_test)

# Instruction: Print Test MSE for 500 bagged trees.
# Algo: Mean Squared Error evaluation.
# Why: Confirms error stays low and stable with more trees.
print("Bagging (500 trees) Test MSE:", np.mean((y_test - y_hat_bag)**2))

# Instruction: Fit a true Random Forest that only considers 6 random features at each split (m = 6).
# Algo: Random Forest (decorrelated bootstrap trees with random feature subsampling m < p).
# Why: Stops one dominant predictor from making all trees look identical, reducing variance even further.
RF_boston = RF(max_features=6, random_state=0).fit(X_train, y_train)

# Instruction: Predict test house prices using the Random Forest.
# Algo: Decorrelated ensemble averaging.
# Why: Evaluates whether decorrelating the trees improves test accuracy over plain bagging.
y_hat_RF = RF_boston.predict(X_test)

# Instruction: Print the Random Forest Test MSE.
# Algo: Mean Squared Error evaluation.
# Why: Demonstrates that Random Forests usually outperform both single trees and Bagging.
print("Random Forest Test MSE:", np.mean((y_test - y_hat_RF)**2))

# Instruction: Create a table pairing each predictor name with its Random Forest importance score.
# Algo: Impurity-based Feature Importance (mean decrease in RSS across all trees).
# Why: Quantifies how much each variable contributes to accurate price predictions.
feature_imp = pd.DataFrame(
    {'importance': RF_boston.feature_importances_},
    index=feature_names
)

# Instruction: Sort and print predictors from most important to least important.
# Algo: Ranked feature attribution.
# Why: Identifies the key drivers of house prices (e.g., 'lstat' and 'rm') for human insight.
print(feature_imp.sort_values(by='importance', ascending=False))


# ==============================================================================
# 4. BOOSTING (Pages 360–361)
# ==============================================================================

# Instruction: Initialize Gradient Boosting with 5,000 shallow trees (depth 3) and tiny step size 0.001.
# Algo: Gradient Boosted Decision Trees (sequential residual fitting with shrinkage lambda = 0.001).
# Why: Builds trees one after another where each tree slowly corrects the mistakes of previous trees.
boost_boston = GBR(n_estimators=5000,
                   learning_rate=0.001,
                   max_depth=3,
                   random_state=0)

# Instruction: Sequentially train all 5,000 boosted trees on the training data.
# Algo: Stagewise additive modeling.
# Why: Gradually reduces bias and variance by taking 5,000 tiny, careful learning steps.
boost_boston.fit(X_train, y_train)

# Instruction: Create an empty array of zeros matching the length of training error history (5,000).
# Algo: Array pre-allocation.
# Why: Prepares storage to record test MSE at every single boosting step from tree 1 to 5,000.
test_error = np.zeros_like(boost_boston.train_score_)

# Instruction: Loop through predictions after tree 1, tree 2, ..., tree 5,000 and record test MSE at each step.
# Algo: Staged ensemble evaluation.
# Why: Lets us watch how test error drops as more trees are added (and check for overfitting).
for idx, y_ in enumerate(boost_boston.staged_predict(X_test)):
    test_error[idx] = np.mean((y_test - y_)**2)

# Instruction: Create an index list [0, 1, 2, ..., 4999] for the x-axis.
# Algo: Iteration indexing.
# Why: Represents the number of trees on the horizontal axis of our learning curve plot.
plot_idx = np.arange(boost_boston.train_score_.shape[0])

# Instruction: Create an 8x8 plot canvas.
# Algo: Plot initialization.
# Why: Sets up a clean graph for comparing training vs. test error curves.
ax = subplots(figsize=(8, 8))[1]

# Instruction: Plot training error in blue ('b') across all 5,000 trees.
# Algo: Learning curve visualization (in-sample error).
# Why: Shows how steadily the model fits the training data.
ax.plot(plot_idx, boost_boston.train_score_, 'b', label='Training')

# Instruction: Plot test error in red ('r') across all 5,000 trees.
# Algo: Generalization curve visualization (out-of-sample error).
# Why: Shows whether test error keeps improving or starts rising (overfitting) at high tree counts.
ax.plot(plot_idx, test_error, 'r', label='Test')

# Instruction: Display the legend identifying the blue and red lines.
# Algo: Plot annotation.
# Why: Makes the chart readable so you know which curve is Training and which is Test.
ax.legend()

# Instruction: Predict final test prices using all 5,000 boosted trees.
# Algo: Full boosted ensemble inference.
# Why: Gets the final predictions to compute overall Test MSE.
y_hat_boost = boost_boston.predict(X_test)

# Instruction: Print Test MSE for slow-learning Boosting (learning_rate = 0.001).
# Algo: Mean Squared Error evaluation.
# Why: Benchmarks slow-shrinkage boosting against Random Forests.
print("Boosting (lr=0.001) Test MSE:", np.mean((y_test - y_hat_boost)**2))

# Instruction: Re-initialize Gradient Boosting with a much larger learning rate of 0.2.
# Algo: Gradient Boosting with faster shrinkage (lambda = 0.2).
# Why: Tests what happens when each tree fixes 20% of remaining errors instead of 0.1%.
boost_boston = GBR(n_estimators=5000,
                   learning_rate=0.2,
                   max_depth=3,
                   random_state=0)

# Instruction: Train the fast-learning boosted model on the training set.
# Algo: Stagewise additive modeling.
# Why: Fits 5,000 trees with aggressive step sizes.
boost_boston.fit(X_train, y_train)

# Instruction: Predict test prices with the aggressive learning rate model.
# Algo: Boosted ensemble inference.
# Why: Generates predictions to compare against the slower learning rate.
y_hat_boost = boost_boston.predict(X_test)

# Instruction: Print Test MSE for fast-learning Boosting (learning_rate = 0.2).
# Algo: Mean Squared Error evaluation.
# Why: Shows how changing the learning rate knob impacts final accuracy (too fast can slightly overfit).
print("Boosting (lr=0.2) Test MSE:", np.mean((y_test - y_hat_boost)**2))


# ==============================================================================
# 5. BAYESIAN ADDITIVE REGRESSION TREES — BART (Pages 361–362)
# ==============================================================================

# Instruction: Initialize BART, discarding the first 5 warmup rounds (burnin) and saving 15 posterior draws (ndraw).
# Algo: Bayesian Additive Regression Trees via MCMC sampling (random tree perturbations on partial residuals).
# Why: Combines Random Forests and Boosting in a Bayesian framework to get strong accuracy plus uncertainty estimates.
bart_boston = BART(random_state=0, burnin=5, ndraw=15)

# Instruction: Run the MCMC sampler on the training data to generate 15 posterior tree ensembles.
# Algo: Bayesian posterior sampling (backfitting MCMC).
# Why: Explores many plausible tree ensembles that explain the training data well.
bart_boston.fit(X_train, y_train)

# Instruction: Convert X_test to 32-bit floats and average predictions across the 15 saved BART ensembles.
# Algo: Posterior predictive averaging.
# Why: ISLP's BART implementation requires float32 arrays to compute fast final predictions.
yhat_test = bart_boston.predict(X_test.astype(np.float32))

# Instruction: Calculate and print the final BART Test MSE.
# Algo: Mean Squared Error evaluation.
# Why: Shows that BART achieves competitive accuracy right alongside Random Forests and Boosting.
print("BART Test MSE:", np.mean((y_test - yhat_test)**2))
```

Here are **5 creative Q&A problems** covering the key Chapter 5 concepts that **Exercises 1–9 skipped**, so you have 100% mastery of the chapter.

---

### **Bonus Q1: Model Assessment vs. Model Selection (Figure 5.6)**
**Question:**
Suppose you run 10-fold CV on smoothing splines across different flexibility levels. You discover that your CV curve consistently **underestimates** the true test MSE by about 15% at every flexibility level. Is your CV curve useless for choosing the best model? Explain.

**Answer:**
* **No, it is still very useful!** It depends on your goal:
  * **Model Assessment** (knowing the *exact* test error): Here, the 15% underestimate matters because the actual MSE value is off.
  * **Model Selection** (choosing the *best flexibility level*): Here, we only care about the **location of the minimum point** on the curve, not its exact height. As shown in Figure 5.6 of the book, even when CV underestimates the true test MSE, its U-shape still hits its minimum at almost the exact same flexibility level as the true test MSE.

---

### **Bonus Q2: The LOOCV Shortcut & High-Leverage Points (Equation 5.2)**
**Question:**
For least squares linear regression, LOOCV has a famous shortcut that requires fitting the model only once:
$$\text{CV}_{(n)} = \frac{1}{n} \sum_{i=1}^{n} \left(\frac{y_i - \hat{y}_i}{1 - h_i}\right)^2$$
(a) Suppose observation $i$ has a residual of $y_i - \hat{y}_i = 2$ and a high leverage of $h_i = 0.9$. What value does it contribute inside the sum, compared to a normal point with $h_i = 0.1$ and the same residual?
(b) Can we use this shortcut for Logistic Regression or KNN?

**Answer:**
* **(a) Effect of Leverage ($h_i$):**
  * For the **high-leverage point** ($h_i = 0.9$): $\left(\frac{2}{1 - 0.9}\right)^2 = \left(\frac{2}{0.1}\right)^2 = 20^2 = \mathbf{400}$.
  * For the **normal point** ($h_i = 0.1$): $\left(\frac{2}{1 - 0.1}\right)^2 = \left(\frac{2}{0.9}\right)^2 \approx \mathbf{4.94}$.
  * **Why:** A high-leverage point pulls the regression line toward itself, making its ordinary residual look artificially small. Dividing by $(1 - h_i)$ inflates its error by the exact right amount to reflect what happens when that point is actually left out.
* **(b) When it works:** **No.** The shortcut *only* holds for least squares linear or polynomial regression. For Logistic Regression, LDA, or KNN, you must refit the model $n$ times (or use $k$-fold CV).

---

### **Bonus Q3: When Bootstrap Disagrees with Standard SE Formulas (Section 5.3.3 Lab)**
**Question:**
In Exercise 6 (`Default` data), `sm.GLM()` and the Bootstrap gave nearly identical standard errors. Yet in the Chapter 5 Lab (`Auto` data: `mpg ~ horsepower`), the Bootstrap gave **larger** standard errors than `sm.OLS()` (`0.85` vs `0.72` for the intercept). Which one should you trust more, and why did they differ?

**Answer:**
* **Trust the Bootstrap more.**
* **Why they differed:**
  1. **Model Misspecification:** The true relationship between `mpg` and `horsepower` is **non-linear (curved)**. Because a straight line fits poorly, the residuals are inflated, distorting $\hat{\sigma}^2$ in the standard `sm.OLS()` formula.
  2. **Fixed-$X$ Assumption:** Standard OLS formulas unrealistically assume the predictor values $x_i$ are fixed and all randomness comes from the error $\epsilon_i$.
  3. **Bootstrap Advantage:** The bootstrap makes **none** of these assumptions—and when the lab switched to a quadratic model (which fits the data well), the `sm.OLS()` and bootstrap SEs matched closely again.

---

### **Bonus Q4: Bootstrapping Paired Observations (Section 5.2, Figure 5.11)**
**Question:**
You want to use the bootstrap to estimate the standard error of the correlation between $X$ (income) and $Y$ (balance). A classmate suggests sampling $n$ values from column $X$ with replacement, and *separately* sampling $n$ values from column $Y$ with replacement. What is wrong with this approach?

**Answer:**
* **It destroys the relationship between $X$ and $Y$!**
* In the bootstrap, you must sample **entire rows (pairs $(X_i, Y_i)$)** together with replacement.
* If you sample $X$ and $Y$ independently, you break the pairing between each person's income and their own balance—making the average correlation $\approx 0$ regardless of the true data.

---

### **Bonus Q5: KNN Flexibility & Avoiding "Data Leakage" (Figures 5.8 & Lab `clone()`)**
**Question:**
(a) In KNN classification, as $1/K$ increases (meaning $K$ gets smaller, e.g., $K = 1$), what happens to the **training error** vs. the **10-fold CV error**?
(b) In the Chapter 5 Lab, `boot_OLS()` uses `clone(model_matrix).fit_transform(D_)` *inside* the bootstrap loop instead of transforming the full dataset once beforehand. Why is this good practice for both CV and the Bootstrap?

**Answer:**
* **(a) KNN Error Curves:**
  * As $1/K$ increases (model becomes more flexible), **training error** drops steadily toward $0$ (at $K=1$, training error is $0$).
  * **10-fold CV error** forms a **U-shape**: it drops at first as the model captures the pattern, then rises again when $K$ becomes too small (overfitting). Thus, CV—not training error—must be used to pick $K$.
* **(b) Preventing Data Leakage:**
  * If you compute derived features (like scaling, centering, or orthogonal `poly()` terms) on the *entire* dataset before splitting, information from the validation set/out-of-bag points "leaks" into the training set.
  * Using `clone()` (or `Pipeline` in `sklearn`) ensures all transformations are fit **only on the resampled training data** inside each fold or bootstrap sample, giving an honest estimate of error and variability.
Here are **5 more creative Q&A problems** that test deeper intuition, common traps, and subtle details from **Chapter 5**.

---

### **Bonus Q6: Why `ShuffleSplit` Standard Deviation Isn't a True SE (Lab `In [14]`, Page 220)**
**Question:**
In the lab, you run `ShuffleSplit(n_splits=10, test_size=0.5)` on the `Auto` dataset and get 10 validation MSEs with a mean of `23.80` and a standard deviation of `1.42`. Why does the textbook warn that `1.42` is **not** a valid estimate of the sampling variability (standard error) of the test score?

**Answer:**
* **Because the 10 splits overlap!**
* Unlike independent samples from a population, the 10 training sets (and 10 validation sets) share many of the same observations, which introduces **positive correlation** between the 10 scores.
* Therefore, `1.42` only measures the *Monte Carlo variation* (how much your estimate jiggles due to picking different random splits), **not** the true sampling variability of the test error.

---

### **Bonus Q7: "Free" Validation with Out-of-Bag (OOB) Observations (Connecting Q2 & CV)**
**Question:**
In Exercise 2, we proved that for large $n$, a single bootstrap sample contains only about **63.2%** of the original unique observations. What happens to the remaining **36.8%**, and how can we use them?

**Answer:**
* The remaining **~36.8%** of observations were never picked in that bootstrap sample—they are called **Out-of-Bag (OOB)** observations.
* Because the model was **not** trained on those OOB points, you can test the fitted model on them to get a **"free" estimate of the test error** without needing a separate cross-validation loop! *(This is a core idea used in Random Forests in Chapter 8.)*

---

### **Bonus Q8: Why Must a Bootstrap Sample Have Size $n$?**
**Question:**
Your dataset has $n = 100$ observations. Why does the bootstrap require drawing **$100$** observations with replacement for every bootstrap sample, instead of drawing $50$ or $500$?

**Answer:**
* Because the **standard error (SE) depends on sample size $n$** (typically $\text{SE} \propto \frac{1}{\sqrt{n}}$).
* The goal of the bootstrap is to emulate drawing a new dataset *of the same size* from the true population.
* If you drew $500$ observations per bootstrap sample, your $\text{SE}_B$ would be artificially **too small** (overconfident); if you drew $50$, your $\text{SE}_B$ would be artificially **too large**.

---

### **Bonus Q9: When Does the Standard Bootstrap Fail?**
**Question:**
Suppose you are studying daily temperature or stock market returns over 100 consecutive days, where today's value strongly depends on yesterday's value. If you use the standard bootstrap (sampling individual days with replacement), why can your standard error estimate be wrong?

**Answer:**
* **Standard bootstrap assumes observations are independent.**
* In time-series data, consecutive days are correlated. Sampling individual rows at random breaks the time-order and correlation structure between yesterday and today.
* *(To fix this in practice, statisticians use a **block bootstrap**, which samples chunks of consecutive days together instead of single rows.)*

---

### **Bonus Q10: Choosing Between Models When the CV Curve is Flat (Figure 5.8)**
**Question:**
In Figure 5.8 (left) of the textbook, 10-fold CV error for polynomial logistic regression is `0.155` at degree 3, reaches its minimum of `0.153` at degree 4, and is `0.156` at degree 5. Why might a data scientist still choose **degree 3** over degree 4?

**Answer:**
* **Parsimony (simpler is better):** When two models have virtually identical CV error (within the noise of random fold splitting), the simpler, less flexible model (degree 3) is preferred because it is **less likely to overfit** new data and is easier to interpret.
* *(In fact, Figure 5.7/5.8 shows that degree 3 actually had the lowest **true** test error of `0.160`!)*
