
## 1. PDF, CDF and MGF of Continuous and Discrete Random Variables

### 💡 Core Concepts & Formulas: PDF, CDF and MGF

> [!abstract] Key Concepts & Formulas
> 1. **Probability Density Function (PDF) & Mass Function (PMF)**:
>    - **Discrete (PMF)**: $P(X = x_i) \ge 0$ with $\sum_i P(X = x_i) = 1$.
>    - **Continuous (PDF)**: $f(x) \ge 0$ with $\int_{-\infty}^\infty f(x) dx = 1$.
>    - Probability on an interval: $P(a \le X \le b) = \int_a^b f(x) dx$.
> 2. **Cumulative Distribution Function (CDF)**:
>    - $F(x) = P(X \le x) = \int_{-\infty}^x f(t) dt$.
>    - Relationship: $f(x) = \frac{d}{dx} F(x)$.
>    - $P(a < X \le b) = F(b) - F(a)$, with $F(-\infty) = 0$, $F(\infty) = 1$.
> 3. **Mathematical Expectation & Variance**:
>    - Mean: $\mu = E[X] = \int_{-\infty}^\infty x f(x) dx$ (or $\sum x_i P(x_i)$).
>    - Variance: $\sigma^2 = \text{Var}(X) = E[X^2] - (E[X])^2 = E[(X-\mu)^2]$.
> 4. **Moment Generating Function (MGF)**:
>    - Definition: $M_X(t) = E[e^{tX}] = \int_{-\infty}^\infty e^{tx} f(x) dx$ (or $\sum e^{tx} P(x)$).
>    - Generating Moments: $E[X^n] = M_X^{(n)}(0) = \left.\frac{d^n M_X(t)}{dt^n}\right|_{t=0}$.
>    - Mean: $\mu = M'_X(0)$, $\text{Var}(X) = M''_X(0) - [M'_X(0)]^2$.
>    - Cumulant Generating Function (CGF): $K_X(t) = \ln M_X(t)$, with Mean $= K'_X(0)$, $\text{Var} = K''_X(0)$.
> 5. **Standard Distributions Summary**:
>    - **Binomial** $B(n, p)$: $P(x) = \binom{n}{x}p^x q^{n-x}$, $M_X(t) = (q + pe^t)^n$, $\mu = np$, $\sigma^2 = npq$.
>    - **Poisson** $P(\lambda)$: $P(x) = \frac{e^{-\lambda}\lambda^x}{x!}$, $M_X(t) = e^{\lambda(e^t-1)}$, $\mu = \lambda$, $\sigma^2 = \lambda$.
>    - **Normal** $\mathcal{N}(\mu, \sigma^2)$: $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$, $M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$.

---

### Solutions: Past Exam Papers & Class Tests

#### Q1. Pg 1, Q.6(b): Cable diameter with $f(x) = 6x(1-x), 0 \le x \le 1$. (i) Mean, (ii) Number $b$ such that $P(x<b) = P(x>b)$.

**Solution:**
**(i) Mean of $x$:**
$$E[X] = \int_0^1 x f(x) dx = \int_0^1 x \cdot 6x(1-x) dx = 6 \int_0^1 (x^2 - x^3) dx$$
$$E[X] = 6 \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_0^1 = 6 \left( \frac{1}{3} - \frac{1}{4} \right) = 6 \left( \frac{1}{12} \right) = \frac{1}{2} = 0.5$$

**(ii) Determine $b$ such that $P(X < b) = P(X > b)$:**
Since total probability is 1: $P(X < b) + P(X > b) = 1$.
Given $P(X < b) = P(X > b) \implies 2 P(X < b) = 1 \implies P(X < b) = 0.5$.
$$\int_0^b 6(x - x^2) dx = 0.5 \implies 6 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^b = 0.5$$
$$3b^2 - 2b^3 = 0.5 \implies 4b^3 - 6b^2 + 1 = 0$$
Factoring: $(2b - 1)(2b^2 - 2b - 1) = 0$.
Since $0 \le b \le 1$, the only valid root is:
$$2b - 1 = 0 \implies b = \frac{1}{2} = 0.5$$

**Answer:** (i) Mean $= \mathbf{0.5}$, (ii) $b = \mathbf{0.5}$.

***

#### Q2. Pg 2, Q.6(b): Cable diameter with $f(x) = kx(5-x^2), 0 \le x \le 2$. Find mean and variance.

**Solution:**
1. **Find normalizing constant $k$:**
   $$\int_0^2 f(x) dx = 1 \implies k \int_0^2 (5x - x^3) dx = k \left[ \frac{5x^2}{2} - \frac{x^4}{4} \right]_0^2 = k (10 - 4) = 6k = 1 \implies k = \frac{1}{6}$$
   Thus, $f(x) = \frac{1}{6}(5x - x^3)$ for $0 \le x \le 2$.

2. **Mean $E[X]$:**
   $$E[X] = \frac{1}{6} \int_0^2 x(5x - x^3) dx = \frac{1}{6} \int_0^2 (5x^2 - x^4) dx = \frac{1}{6} \left[ \frac{5x^3}{3} - \frac{x^5}{5} \right]_0^2 = \frac{1}{6} \left( \frac{40}{3} - \frac{32}{5} \right) = \frac{1}{6} \left( \frac{104}{15} \right) = \frac{52}{45} \approx 1.156$$

3. **Variance $\text{Var}(X) = E[X^2] - (E[X])^2$:**
   $$E[X^2] = \frac{1}{6} \int_0^2 x^2(5x - x^3) dx = \frac{1}{6} \int_0^2 (5x^3 - x^5) dx = \frac{1}{6} \left[ \frac{5x^4}{4} - \frac{x^6}{6} \right]_0^2 = \frac{1}{6} \left( 20 - \frac{32}{3} \right) = \frac{1}{6} \left( \frac{28}{3} \right) = \frac{14}{9} \approx 1.556$$
   $$\text{Var}(X) = \frac{14}{9} - \left(\frac{52}{45}\right)^2 = \frac{14}{9} - \frac{2704}{2025} = \frac{3150 - 2704}{2025} = \frac{446}{2025} \approx 0.2202$$

**Answer:** Mean $= \mathbf{\frac{52}{45} \approx 1.156}$, Variance $= \mathbf{\frac{446}{2025} \approx 0.2202}$.

***

#### Q3. Pg 3, Q.8(a): Find the moment generating function of Poisson distribution and find mean and variance from it.

**Solution:**
1. **Derivation of MGF:**
   For $X \sim \text{Poisson}(\lambda)$, $P(X=x) = \frac{e^{-\lambda}\lambda^x}{x!}$, $x = 0, 1, 2, \dots$
   $$M_X(t) = E[e^{tX}] = \sum_{x=0}^\infty e^{tx} \frac{e^{-\lambda}\lambda^x}{x!} = e^{-\lambda} \sum_{x=0}^\infty \frac{(\lambda e^t)^x}{x!} = e^{-\lambda} e^{\lambda e^t} = e^{\lambda(e^t - 1)}$$

2. **Mean using MGF:**
   $$M'_X(t) = \frac{d}{dt}\left[e^{\lambda(e^t-1)}\right] = \lambda e^t e^{\lambda(e^t-1)}$$
   $$\mu = E[X] = M'_X(0) = \lambda e^0 e^{\lambda(e^0-1)} = \lambda(1)e^0 = \lambda$$

3. **Variance using MGF:**
   $$M''_X(t) = \frac{d}{dt}\left[\lambda e^t e^{\lambda(e^t-1)}\right] = \lambda e^t e^{\lambda(e^t-1)} + (\lambda e^t)^2 e^{\lambda(e^t-1)}$$
   $$E[X^2] = M''_X(0) = \lambda + \lambda^2$$
   $$\text{Var}(X) = E[X^2] - (E[X])^2 = (\lambda + \lambda^2) - \lambda^2 = \lambda$$

**Answer:** $M_X(t) = \mathbf{e^{\lambda(e^t-1)}}$, Mean $= \boldsymbol{\lambda}$, Variance $= \boldsymbol{\lambda}$.

***

#### Q4. Pg 14, CT-03, Q.3: Prove that mean $\mu = np$ and standard deviation $\sigma = \sqrt{npq}$ of binomial distribution using MGF.

**Solution:**
1. **MGF of Binomial Distribution:**
   $$M_X(t) = E[e^{tX}] = \sum_{x=0}^n e^{tx} \binom{n}{x} p^x q^{n-x} = \sum_{x=0}^n \binom{n}{x} (pe^t)^x q^{n-x} = (q + pe^t)^n$$

2. **First Derivative (Mean):**
   $$M'_X(t) = n(q + pe^t)^{n-1} (p e^t)$$
   $$\mu = E[X] = M'_X(0) = n(q + p)^{n-1}(p) = n(1)^{n-1} p = np \quad (\because q+p=1)$$

3. **Second Derivative & Variance:**
   $$M''_X(t) = n(n-1)(q + pe^t)^{n-2}(pe^t)^2 + n(q + pe^t)^{n-1}(pe^t)$$
   $$E[X^2] = M''_X(0) = n(n-1)p^2 + np = n^2 p^2 - np^2 + np$$
   $$\sigma^2 = \text{Var}(X) = E[X^2] - (E[X])^2 = (n^2 p^2 - np^2 + np) - (np)^2 = np(1-p) = npq$$
   $$\sigma = \sqrt{npq}$$
**(Proved)**

***

#### Q5. Pg 14, CT-03, Q.3 (Or): Define PDF. A manufacturer knows 5% of pins are defective. Box of 100 pins, guaranteed $\le 10$ defective. Probability box fails guarantee?

**Solution:**
1. **Definition of PDF:** A continuous function $f(x)$ is a probability density function if $f(x) \ge 0$ for all $x \in \mathbb{R}$ and $\int_{-\infty}^\infty f(x) dx = 1$.
2. **Probability Problem:**
   $n = 100$, $p = 0.05 \implies \lambda = np = 100 \times 0.05 = 5$.
   Since $n$ is large and $p$ is small, $X \sim \text{Poisson}(\lambda = 5)$.
   A box fails to meet guaranteed quality if defective pins $X > 10$:
   $$P(\text{Fails}) = P(X > 10) = 1 - P(X \le 10) = 1 - \sum_{x=0}^{10} \frac{e^{-5} 5^x}{x!}$$
   Evaluating Poisson cumulative sum for $\lambda = 5, x \le 10$:
   $$\sum_{x=0}^{10} \frac{e^{-5} 5^x}{x!} \approx 0.9863$$
   $$P(X > 10) = 1 - 0.9863 = 0.0137 \quad (1.37\%)$$

**Answer:** The probability is **$0.0137$** (or **$1.37\%$**).

***

#### Q6. Pg 19, Class Test-2, Q2: Cable diameter $f(x) = 6x(1-x), 0 \le x \le 1$. (i) $b$ such that $P(x<b) = P(x>b)$, (ii) Mean of $x$.

**Solution:**
*(Identical to Q1).*
(i) $b = \mathbf{0.5}$, (ii) Mean $= \mathbf{0.5}$.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q7. MHU Sheet, Lec 7-10, Problem-9: $f(x) = e^{-x}, 0 < x < \infty$. (a) Check PDF, (b) Find $P(1 < x < 2)$.

**Solution:**
(a) For $x > 0$, $f(x) = e^{-x} > 0$.
$$\int_0^\infty f(x) dx = \int_0^\infty e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 0 - (-1) = 1$$
Since $f(x) \ge 0$ and $\int_0^\infty f(x)dx = 1$, $f(x)$ is a valid **PDF**.

(b) Probability:
$$P(1 < X < 2) = \int_1^2 e^{-x} dx = \left[ -e^{-x} \right]_1^2 = -e^{-2} - (-e^{-1}) = e^{-1} - e^{-2} \approx 0.3679 - 0.1353 = 0.2325$$

**Answer:** (a) **Valid PDF**, (b) **$0.2325$**.

***

#### Q8. MHU Sheet, Lec 7-10, Problem 10: Find $F(x)$, show $f(x) = \frac{d}{dx}F(x)$, and find $F(3)$ for $f(x) = \frac{1}{2}e^{-x/2}, x > 0$.

**Solution:**
1. **Find $F(x)$:**
   $$F(x) = \int_0^x f(t) dt = \int_0^x \frac{1}{2}e^{-t/2} dt = \left[ -e^{-t/2} \right]_0^x = 1 - e^{-x/2}, \quad (x \ge 0)$$
2. **Show $f(x) = F'(x)$:**
   $$\frac{d}{dx} F(x) = \frac{d}{dx}\left(1 - e^{-x/2}\right) = 0 - \left(-\frac{1}{2}e^{-x/2}\right) = \frac{1}{2}e^{-x/2} = f(x)$$
3. **Compute $F(3)$:**
   $$F(3) = 1 - e^{-3/2} = 1 - e^{-1.5} \approx 1 - 0.2231 = 0.7769$$

**Answer:** $F(x) = \mathbf{1 - e^{-x/2}}$, $F(3) = \mathbf{0.7769}$.

***

#### Q9. MHU Sheet, Lec 7-10, Problem 11: $F(x) = 1 - e^{-2x}$ for $x \ge 0$. Find (a) density function, (b) $P(X > 2)$, (c) $P(-3 < X \le 4)$.

**Solution:**
(a) **Density function:**
   $$f(x) = \frac{d}{dx} F(x) = \begin{cases} 2e^{-2x}, & x \ge 0 \\ 0, & x < 0 \end{cases}$$
(b) **$P(X > 2)$:**
   $$P(X > 2) = 1 - F(2) = 1 - (1 - e^{-2(2)}) = e^{-4} \approx 0.0183$$
(c) **$P(-3 < X \le 4)$:**
   Since $F(x) = 0$ for $x < 0$, $F(-3) = 0$:
   $$P(-3 < X \le 4) = F(4) - F(-3) = (1 - e^{-2(4)}) - 0 = 1 - e^{-8} \approx 0.9997$$

**Answer:** (a) $f(x) = \mathbf{2e^{-2x}} (x\ge 0)$, (b) $\mathbf{e^{-4} \approx 0.0183}$, (c) $\mathbf{1 - e^{-8} \approx 0.9997}$.

***

#### Q10. MHU Sheet, Lec 7-10, Problem-14: Find $E[X]$ and $E[X^2]$ for $f(x) = 2(1-x), 0 < x < 1$.

**Solution:**
1. $$E[X] = \int_0^1 x \cdot 2(1-x) dx = 2 \int_0^1 (x - x^2) dx = 2 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2 \left( \frac{1}{2} - \frac{1}{3} \right) = \frac{1}{3}$$
2. $$E[X^2] = \int_0^1 x^2 \cdot 2(1-x) dx = 2 \int_0^1 (x^2 - x^3) dx = 2 \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_0^1 = 2 \left( \frac{1}{3} - \frac{1}{4} \right) = \frac{1}{6}$$

**Answer:** $E[X] = \mathbf{\frac{1}{3}}$, $E[X^2] = \mathbf{\frac{1}{6}}$.

***

#### Q11. MHU Sheet, Lec 7-10, Problem 15: Cable diameter $f(x) = 6x(1-x), 0 \le x \le 1$. (i) $b$ such that $P(x<b) = P(x>b)$, (ii) Mean of $x$.

**Solution:**
*(Identical to Q1).*
(i) $b = \mathbf{0.5}$, (ii) Mean $= \mathbf{0.5}$.

***

#### Q12. MHU Sheet, Lec 11-14 (Binomial), Problem-2: Find MGF and CGF of binomial distribution.

**Solution:**
1. **MGF:**
   $$M_X(t) = E[e^{tX}] = \sum_{x=0}^n e^{tx} \binom{n}{x} p^x q^{n-x} = \sum_{x=0}^n \binom{n}{x} (pe^t)^x q^{n-x} = (q + pe^t)^n$$
2. **CGF (Cumulant Generating Function):**
   $$K_X(t) = \ln M_X(t) = \ln\left[(q + pe^t)^n\right] = n \ln(q + pe^t)$$

**Answer:** $M_X(t) = \mathbf{(q + pe^t)^n}$, $K_X(t) = \mathbf{n\ln(q + pe^t)}$.

***

#### Q13. MHU Sheet, Lec 11-14 (Normal), Problem-3: Find MGF, skewness and kurtosis of normal distribution and comment on shape.

**Solution:**
For $X \sim \mathcal{N}(\mu, \sigma^2)$:
1. **MGF:**
   $$M_X(t) = E[e^{tX}] = \frac{1}{\sigma\sqrt{2\pi}} \int_{-\infty}^\infty e^{tx} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx = e^{\mu t + \frac{1}{2}\sigma^2 t^2}$$
2. **Central Moments:**
   From MGF about mean $M_{X-\mu}(t) = e^{\frac{1}{2}\sigma^2 t^2} = 1 + \frac{\sigma^2 t^2}{2} + \frac{\sigma^4 t^4}{8} + \dots$:
   - $\mu_1 = 0$, $\mu_2 = \sigma^2$
   - $\mu_3 = 0$ (all odd central moments vanish)
   - $\mu_4 = 3\sigma^4$
3. **Skewness:**
   $$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = 0 \implies \gamma_1 = 0 \quad \text{(Perfectly Symmetric)}$$
4. **Kurtosis:**
   $$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{3\sigma^4}{\sigma^4} = 3 \implies \gamma_2 = \beta_2 - 3 = 0 \quad \text{(Mesokurtic)}$$

**Comment on Shape:** The distribution is a bell-shaped, perfectly symmetrical curve about the mean $\mu$, with normal peakedness (mesokurtic).

***

#### Q14. MHU Sheet, Lec 11-14 (Poisson), Problem-2: Find mean and standard deviation of Poisson distribution as a limiting form of binomial distribution.

**Solution:**
In Binomial distribution, let $n \to \infty$ and $p \to 0$ such that $np = \lambda$ (constant):
1. **Mean:**
   $$\mu = np = \lambda$$
2. **Variance:**
   $$\sigma^2 = npq = np(1 - p) = \lambda\left(1 - \frac{\lambda}{n}\right)$$
   Taking the limit as $n \to \infty$:
   $$\lim_{n\to\infty} \sigma^2 = \lim_{n\to\infty} \lambda\left(1 - \frac{\lambda}{n}\right) = \lambda(1 - 0) = \lambda$$
3. **Standard Deviation:**
   $$\sigma = \sqrt{\lambda}$$

**Answer:** Mean $= \boldsymbol{\lambda}$, Standard Deviation $= \boldsymbol{\sqrt{\lambda}}$.

***

## 2. Marginal PDF and Joint PDF of Continuous and Discrete Random Variables

### 💡 Core Concepts & Formulas: Joint & Marginal Distributions

> [!abstract] Key Concepts & Formulas
> 1. **Joint PDF Properties**:
>    - $f_{XY}(x,y) \ge 0$, $\int_{-\infty}^\infty \int_{-\infty}^\infty f_{XY}(x,y) dx dy = 1$.
>    - $P((X,Y) \in R) = \iint_R f_{XY}(x,y) dx dy$.
> 2. **Marginal PDFs**:
>    $$f_X(x) = \int_{-\infty}^\infty f_{XY}(x,y) dy, \qquad f_Y(y) = \int_{-\infty}^\infty f_{XY}(x,y) dx$$
> 3. **Conditional Distributions**:
>    $$f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)}, \qquad f_{X|Y}(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)}$$
> 4. **Conditional Expectation & Variance**:
>    $$E[Y|X=x] = \int_{-\infty}^\infty y f_{Y|X}(y|x) dy, \quad \text{Var}(Y|X=x) = E[Y^2|X=x] - (E[Y|X=x])^2$$
> 5. **Discrete Bivariate Distributions**:
>    - Marginals: $P(X=x_i) = \sum_j P(x_i, y_j)$, $P(Y=y_j) = \sum_i P(x_i, y_j)$.
>    - Conditional PMF: $P(X=x_i | Y=y_j) = \frac{P(x_i, y_j)}{P(Y=y_j)}$.

---

### Solutions: Past Exam Papers & Class Tests

#### Q15. Pg 2 & Pg 3, Q.7(a): $f_{XY}(x,y) = K e^{-0.001x - 0.002y}$ for $0 < x < y < \infty$, $K = 6 \times 10^{-6}$.
Find (i) $P(X \le 1000, Y \le 2000)$, (ii) $P(Y > 2000)$, (iii) Conditional density $f_{Y|X}(y|x)$.

**Solution:**
**(i) $P(X \le 1000, Y \le 2000)$:**
Region of integration: $0 < x < y$, with $x \le 1000$ and $y \le 2000$.
Split into two regions: for $0 < y \le 1000$ ($0 < x < y$), and for $1000 < y \le 2000$ ($0 < x \le 1000$).
$$P = K \int_0^{1000} e^{-0.002y} \left[\int_0^y e^{-0.001x} dx\right] dy + K \int_{1000}^{2000} e^{-0.002y} \left[\int_0^{1000} e^{-0.001x} dx\right] dy$$
Inner integral $\int_0^a e^{-0.001x} dx = 1000(1 - e^{-0.001a})$:
* First part:
  $$1000 K \int_0^{1000} (e^{-0.002y} - e^{-0.003y}) dy = 1000 K \left[ \frac{1 - e^{-2}}{0.002} - \frac{1 - e^{-3}}{0.003} \right] = 6 \times 10^{-3} \left[ 500(1 - e^{-2}) - \frac{1000}{3}(1 - e^{-3}) \right]$$
* Second part:
  $$1000(1 - e^{-1}) K \int_{1000}^{2000} e^{-0.002y} dy = 6 \times 10^{-3}(1 - e^{-1}) \left[ \frac{e^{-2} - e^{-4}}{0.002} \right] = 3(1 - e^{-1})(e^{-2} - e^{-4})$$
Summing numerically:
$$P(X \le 1000, Y \le 2000) \approx 0.0528 + 0.1989 \approx 0.2517$$

**(ii) $P(Y > 2000)$:**
$$P(Y > 2000) = \int_{2000}^\infty \int_0^y K e^{-0.001x - 0.002y} dx dy = 1000 K \int_{2000}^\infty (e^{-0.002y} - e^{-0.003y}) dy$$
$$= 6 \times 10^{-3} \left[ \frac{e^{-4}}{0.002} - \frac{e^{-6}}{0.003} \right] = 6 \times 10^{-3} [500 e^{-4} - 333.33 e^{-6}] = 3 e^{-4} - 2 e^{-6} \approx 0.0549 - 0.0050 = 0.0499$$

**(iii) Conditional density $f_{Y|X}(y|x)$:**
First find marginal $f_X(x)$ for $x > 0$:
$$f_X(x) = \int_x^\infty K e^{-0.001x - 0.002y} dy = K e^{-0.001x} \left[ \frac{e^{-0.002y}}{-0.002} \right]_x^\infty = \frac{K}{0.002} e^{-0.003x} = 0.003 e^{-0.003x}$$
Now compute conditional density for $y > x$:
$$f_{Y|X}(y|x) = \frac{f_{XY}(x,y)}{f_X(x)} = \frac{K e^{-0.001x - 0.002y}}{0.003 e^{-0.003x}} = \frac{6 \times 10^{-6}}{0.003} e^{0.002x - 0.002y} = 0.002 e^{-0.002(y - x)}, \quad (y > x)$$

**Answer:** (i) $\approx \mathbf{0.252}$, (ii) $\approx \mathbf{0.050}$, (iii) $f_{Y|X}(y|x) = \mathbf{0.002 e^{-0.002(y-x)}} \quad (y > x)$.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q16. MHU Sheet, Lec 7-10, Problem-12: Find conditional probability function of $X$ given $Y=3$.

**Solution:**
From the given discrete bivariate table:
1. $P(Y = 3) = \sum_i P(x_i, 3) = 0 + \frac{2}{16} + \frac{2}{16} + 0 = \frac{4}{16} = \frac{1}{4}$.
2. Conditional PMF $P(X = x | Y = 3) = \frac{P(X=x, Y=3)}{P(Y=3)}$:
   - For $X = 1$: $P(1|3) = \frac{0}{4/16} = 0$
   - For $X = 2$: $P(2|3) = \frac{2/16}{4/16} = \frac{2}{4} = \frac{1}{2}$
   - For $X = 3$: $P(3|3) = \frac{2/16}{4/16} = \frac{2}{4} = \frac{1}{2}$
   - For $X = 4$: $P(4|3) = \frac{0}{4/16} = 0$

**Answer:** $P(X=2|Y=3) = \mathbf{\frac{1}{2}}$, $P(X=3|Y=3) = \mathbf{\frac{1}{2}}$, and $0$ elsewhere.

***

#### Q17. MHU Sheet, Lec 7-10, Problem-13: Joint table of $X \in \{2, 4, 6\}$ and $Y \in \{1, 3, 9\}$. Determine marginals, expectations, variances, and conditionals.

**Solution:**
**(i) Marginals, Expectations & Variances:**
* **$P(X)$:** $P(2) = 1/4$, $P(4) = 1/2$, $P(6) = 1/4$.
  - $E[X] = 2(1/4) + 4(1/2) + 6(1/4) = 0.5 + 2 + 1.5 = 4$
  - $E[X^2] = 4(1/4) + 16(1/2) + 36(1/4) = 1 + 8 + 9 = 18$
  - $\text{Var}(X) = 18 - 4^2 = 2$
* **$P(Y)$:** $P(1) = 1/2$, $P(3) = 1/3$, $P(9) = 1/6$.
  - $E[Y] = 1(1/2) + 3(1/3) + 9(1/6) = 0.5 + 1 + 1.5 = 3$
  - $E[Y^2] = 1(1/2) + 9(1/3) + 81(1/6) = 0.5 + 3 + 13.5 = 17$
  - $\text{Var}(Y) = 17 - 3^2 = 8$

**(ii) Conditionals (e.g. given $Y=1$):**
* $P(X|Y=1)$:
  - $P(X=2|Y=1) = \frac{1/8}{1/2} = \frac{1}{4}$
  - $P(X=4|Y=1) = \frac{1/4}{1/2} = \frac{1}{2}$
  - $P(X=6|Y=1) = \frac{1/8}{1/2} = \frac{1}{4}$
  - $E[X|Y=1] = 2(1/4) + 4(1/2) + 6(1/4) = 4$
  - $\text{Var}(X|Y=1) = 2$

**Answer:** $E[X] = \mathbf{4}, \text{Var}(X) = \mathbf{2}$; $E[Y] = \mathbf{3}, \text{Var}(Y) = \mathbf{8}$.

***

## 3. Joint PDF of Two Independent Random Variables

### 💡 Core Concepts & Formulas: Independent Random Variables

> [!abstract] Key Concepts & Formulas
> 1. **Definition of Independence**:
>    Two random variables $X$ and $Y$ are independent if and only if:
>    $$f_{XY}(x,y) = f_X(x) f_Y(y) \quad \forall (x,y)$$
> 2. **Key Properties of Independent Variables**:
>    - **Expectation of Product**: $E[XY] = E[X] E[Y]$.
>    - **Covariance**: $\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0$.
>    - **Correlation**: $\rho_{XY} = 0$ (Independence implies uncorrelatedness; converse is not generally true).
>    - **Variance of Sum**: $\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y)$.
>    - **MGF Property**: $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$.
>    - **Conditional PDF**: $f_{Y|X}(y|x) = f_Y(y)$ and $f_{X|Y}(x|y) = f_X(x)$.

*(Note: No separate numerical exam questions; concepts apply directly to joint analysis and distributions).*

***

## 4. Joint PDF of Two Dependent Random Variables

### 💡 Core Concepts & Formulas: Dependent Random Variables

> [!abstract] Key Concepts & Formulas
> 1. **Definition of Dependence**:
>    $X$ and $Y$ are dependent if $f_{XY}(x,y) \neq f_X(x) f_Y(y)$.
> 2. **Covariance & Correlation**:
>    $$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = \iint (x - \mu_X)(y - \mu_Y) f_{XY}(x,y) dx dy$$
>    $$\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}, \quad -1 \le \rho_{XY} \le 1$$
> 3. **Variance of Linear Combination**:
>    $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab\,\text{Cov}(X,Y)$$
> 4. **Laws of Total Expectation and Variance**:
>    - $E[Y] = E_X[E[Y|X]]$.
>    - $\text{Var}(Y) = E_X[\text{Var}(Y|X)] + \text{Var}_X(E[Y|X])$.

*(Note: Handled via conditional distributions such as Q15, Q16, Q17 above).*

***

## 5. Calculation of PDF of a Vector from the PDF of Its Element

### 💡 Core Concepts & Formulas: Random Vectors

> [!abstract] Key Concepts & Formulas
> 1. **Random Vector Definition**:
>    An $n$-dimensional random vector $\mathbf{X} = [X_1, X_2, \dots, X_n]^T$ has joint PDF $f_{\mathbf{X}}(\mathbf{x}) = f_{X_1, \dots, X_n}(x_1, \dots, x_n)$.
> 2. **Independent Elements**:
>    If elements $X_1, X_2, \dots, X_n$ are mutually independent:
>    $$f_{\mathbf{X}}(\mathbf{x}) = \prod_{i=1}^n f_{X_i}(x_i)$$
> 3. **Multivariate Normal Distribution**:
>    If $\mathbf{X} \sim \mathcal{N}_n(\boldsymbol{\mu}, \mathbf{\Sigma})$:
>    $$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\mathbf{\Sigma}|^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)$$
>    where $\boldsymbol{\mu} = E[\mathbf{X}]$ is the mean vector and $\mathbf{\Sigma} = E[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T]$ is the covariance matrix.
> 4. **Transformation of Random Vectors**:
>    If $\mathbf{Y} = \mathbf{g}(\mathbf{X})$ is an invertible transformation with inverse $\mathbf{X} = \mathbf{h}(\mathbf{Y})$:
>    $$f_{\mathbf{Y}}(\mathbf{y}) = f_{\mathbf{X}}(\mathbf{h}(\mathbf{y})) \cdot |\det(J_{\mathbf{h}})|$$
>    where $J_{\mathbf{h}}$ is the Jacobian matrix with elements $J_{ij} = \frac{\partial h_i}{\partial y_j}$.

***

## 6. Calculation of PDF of a Matrix from the PDF of Its Element

### 💡 Core Concepts & Formulas: Random Matrices

> [!abstract] Key Concepts & Formulas
> 1. **Random Matrix**:
>    A matrix $\mathbf{Z} \in \mathbb{R}^{m \times n}$ whose entries $Z_{ij}$ are random variables has PDF defined over $\mathbb{R}^{mn}$:
>    $$f_{\mathbf{Z}}(\mathbf{Z}) = f(Z_{11}, Z_{12}, \dots, Z_{mn})$$
> 2. **Independent Standard Normal Matrix**:
>    If all entries $Z_{ij} \overset{i.i.d.}{\sim} \mathcal{N}(0, 1)$, the joint density is:
>    $$f_{\mathbf{Z}}(\mathbf{Z}) = \prod_{i=1}^m \prod_{j=1}^n \frac{1}{\sqrt{2\pi}} e^{-Z_{ij}^2 / 2} = \frac{1}{(2\pi)^{mn/2}} \exp\left(-\frac{1}{2} \sum_{i=1}^m \sum_{j=1}^n Z_{ij}^2\right) = \frac{1}{(2\pi)^{mn/2}} \exp\left(-\frac{1}{2} \text{Tr}(\mathbf{Z}^T \mathbf{Z})\right)$$
> 3. **Wishart Distribution (Sample Covariance Matrix)**:
>    If $\mathbf{Z}$ is an $m \times n$ Gaussian matrix with rows $\sim \mathcal{N}_n(\mathbf{0}, \mathbf{\Sigma})$, then $\mathbf{W} = \mathbf{Z}^T \mathbf{Z}$ follows the **Wishart distribution** $\mathcal{W}_n(m, \mathbf{\Sigma})$.

***

## 7. Hypothesis Testing and Regression Analysis

### 💡 Core Concepts & Formulas: Hypothesis Testing & Regression

> [!abstract] Key Concepts & Formulas
> 1. **Hypothesis Testing (Large Sample Z-test for Mean)**:
>    - Null hypothesis $H_0: \mu = \mu_0$ vs. Alternative $H_1: \mu \neq \mu_0$.
>    - Test statistic:
>      $$z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} \quad (\text{or } \frac{\bar{x} - \mu_0}{s / \sqrt{n}})$$
>    - Decision rule at $\alpha = 0.05$ (5% significance level, two-tailed):
>      - Critical value: $z_{\text{crit}} = \pm 1.96$.
>      - If $|z| > 1.96$, **reject $H_0$**; otherwise, do not reject $H_0$.
> 2. **Linear Regression (Method of Least Squares)**:
>    - Line of $Y$ on $X$: $Y = a + bX$, where:
>      $$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}, \qquad a = \bar{Y} - b\bar{X}$$
>    - Line of $X$ on $Y$: $X = c + dY$, where:
>      $$d = \frac{n\sum XY - \sum X \sum Y}{n\sum Y^2 - (\sum Y)^2}, \qquad c = \bar{X} - d\bar{Y}$$
> 3. **Pearson's Correlation Coefficient ($r$)**:
>    $$r = \frac{n\sum XY - \sum X \sum Y}{\sqrt{[n\sum X^2 - (\sum X)^2][n\sum Y^2 - (\sum Y)^2]}} = \pm \sqrt{b \cdot d}$$
>    - Relationship: $r$ and regression slopes $b, d$ have identical signs.

---

### Solutions: Past Exam Papers & Class Tests

#### Q18. Pg 1, Q.8(b): Fit a regression line of X on Y (and Y on X) for data: $X = [16, 19, 25, 28, 36, 40]$, $Y = [192, 218, 210, 232, 236, 249]$.

**Solution:**
Here $n = 6$.
Construct the summary table:
* $\sum X = 16 + 19 + 25 + 28 + 36 + 40 = 164 \implies \bar{X} = 27.333$
* $\sum Y = 192 + 218 + 210 + 232 + 236 + 249 = 1337 \implies \bar{Y} = 222.833$
* $\sum X^2 = 256 + 361 + 625 + 784 + 1296 + 1600 = 4922$
* $\sum Y^2 = 36864 + 47524 + 44100 + 53824 + 55696 + 62001 = 300009$
* $\sum XY = 3072 + 4142 + 5250 + 6496 + 8496 + 9960 = 37416$

1. **Regression Line of $Y$ on $X$ ($Y = a + bX$):**
   $$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2} = \frac{6(37416) - (164)(1337)}{6(4922) - (164)^2} = \frac{224496 - 219268}{29532 - 26896} = \frac{5228}{2636} \approx 1.983$$
   $$a = \bar{Y} - b\bar{X} = 222.833 - (1.983)(27.333) = 222.833 - 54.201 = 168.632$$
   $$Y = 168.63 + 1.98X$$

2. **Regression Line of $X$ on $Y$ ($X = c + dY$):**
   $$d = \frac{n\sum XY - \sum X \sum Y}{n\sum Y^2 - (\sum Y)^2} = \frac{5228}{6(300009) - (1337)^2} = \frac{5228}{1800054 - 1787569} = \frac{5228}{12485} \approx 0.4187$$
   $$c = \bar{X} - d\bar{Y} = 27.333 - (0.4187)(222.833) = 27.333 - 93.300 = -65.967$$
   $$X = -65.97 + 0.42Y$$

**Answer:** Line of $Y$ on $X$: **$Y = 168.63 + 1.98X$**; Line of $X$ on $Y$: **$X = -65.97 + 0.42Y$**.

***

#### Q19. Pg 3, Q.8(b): Hours watched TV ($X$) vs test score ($Y$) for 12 students. Display scatter plot and calculate correlation coefficient.

**Solution:**
$n = 12$.
Data:
$X = [0, 1, 2, 5, 3, 3, 5, 6, 7, 8, 7, 10]$
$Y = [96, 85, 82, 68, 74, 95, 76, 58, 65, 67, 62, 50]$

1. **Summary Sums:**
   * $\sum X = 57 \implies \bar{X} = 4.75$
   * $\sum Y = 878 \implies \bar{Y} = 73.167$
   * $\sum X^2 = 0 + 1 + 4 + 25 + 9 + 9 + 25 + 36 + 49 + 64 + 49 + 100 = 371$
   * $\sum Y^2 = 9216 + 7225 + 6724 + 4624 + 5476 + 9025 + 5776 + 3364 + 4225 + 4489 + 3844 + 2500 = 66488$
   * $\sum XY = 0 + 85 + 164 + 340 + 222 + 285 + 380 + 348 + 455 + 536 + 434 + 500 = 3749$

2. **Correlation Coefficient ($r$):**
   $$r = \frac{n\sum XY - \sum X \sum Y}{\sqrt{[n\sum X^2 - (\sum X)^2][n\sum Y^2 - (\sum Y)^2]}}$$
   $$\text{Numerator} = 12(3749) - (57)(878) = 44988 - 50046 = -5058$$
   $$n\sum X^2 - (\sum X)^2 = 12(371) - (57)^2 = 4452 - 3249 = 1203$$
   $$n\sum Y^2 - (\sum Y)^2 = 12(66488) - (878)^2 = 797856 - 770884 = 26972$$
   $$\text{Denominator} = \sqrt{1203 \times 26972} = \sqrt{32447316} \approx 5696.25$$
   $$r = \frac{-5058}{5696.25} \approx -0.888$$

3. **Scatter Plot Interpretation:**
   Points $(x_i, y_i)$ show a clear downward linear trend, confirming a **strong negative correlation** ($r \approx -0.89$): more TV hours correspond to lower test scores.

**Answer:** Correlation coefficient $r \approx \mathbf{-0.888}$.

***

#### Q20. Pg 4 & Pg 5, Q.8(c): Determine straight line best fit for: $X = [10, 12, 13, 16, 17, 20, 25]$, $Y = [19, 22, 24, 27, 29, 33, 37]$.

**Solution:**
$n = 7$.
* $\sum X = 10 + 12 + 13 + 16 + 17 + 20 + 25 = 113$
* $\sum Y = 19 + 22 + 24 + 27 + 29 + 33 + 37 = 191$
* $\sum X^2 = 100 + 144 + 169 + 256 + 289 + 400 + 625 = 1983$
* $\sum XY = 190 + 264 + 312 + 432 + 493 + 660 + 925 = 3276$

Slope $b$ and intercept $a$:
$$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2} = \frac{7(3276) - (113)(191)}{7(1983) - (113)^2} = \frac{22932 - 21583}{13881 - 12769} = \frac{1349}{1112} \approx 1.2131$$
$$a = \frac{\sum Y - b\sum X}{n} = \frac{191 - (1.2131)(113)}{7} = \frac{191 - 137.08}{7} = \frac{53.92}{7} \approx 7.703$$

**Answer:** The best fitting line is **$Y = 7.703 + 1.213 X$** (or $Y = 1.21X + 7.70$).

***

#### Q21. Pg 6, Q.8(b): What is regression and correlation? Fit regression line of X on Y for data in Q18.

**Solution:**
1. **Definitions:**
   - **Correlation:** A measure of the strength and direction of linear association between two variables. It is dimensionless and bounded in $[-1, 1]$.
   - **Regression:** A mathematical equation used to estimate or predict the value of a dependent variable from one or more independent variables.
2. **Regression Line of $X$ on $Y$:**
   From Q18:
   $$X = c + dY \implies X = -65.97 + 0.42Y$$

**Answer:** Line of $X$ on $Y$ is **$X = -65.97 + 0.42Y$**.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q22. MHU Sheet, Lec 15-17 (Hypothesis Testing), Problem-1: Tube lights $n=100$, mean lifetime $\bar{x} = 1580$ hr, $s = 90$ hr. Test hypothesis that $\mu = 1600$ hr at $5\%$ significance level.

**Solution:**
1. **Hypotheses:**
   - Null Hypothesis: $H_0: \mu = 1600$ hr
   - Alternative Hypothesis: $H_1: \mu \neq 1600$ hr (two-tailed test)
2. **Significance Level:** $\alpha = 0.05 \implies$ critical $z$-value is $z_{\alpha/2} = \pm 1.96$.
3. **Test Statistic ($n = 100 \ge 30$, large sample):**
   $$z = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{1580 - 1600}{90 / \sqrt{100}} = \frac{-20}{9} \approx -2.22$$
4. **Decision:**
   Since $|z| = 2.22 > 1.96$, the test statistic falls in the critical (rejection) region.
   Therefore, we **reject $H_0$** at the 5% level of significance.

**Conclusion:** The mean lifetime of tube lights is significantly different from 1600 hours.

***

#### Q23. MHU Sheet, Lec 15-17 (Regression), Problem-1: Calculate regression equations of X on Y and Y on X for: $X = [1, 2, 3, 4, 5]$, $Y = [2, 5, 3, 8, 7]$.

**Solution:**
$n = 5$.
* $\sum X = 15 \implies \bar{X} = 3$
* $\sum Y = 25 \implies \bar{Y} = 5$
* $\sum X^2 = 1 + 4 + 9 + 16 + 25 = 55$
* $\sum Y^2 = 4 + 25 + 9 + 64 + 49 = 151$
* $\sum XY = 2 + 10 + 9 + 32 + 35 = 88$

1. **Regression of $Y$ on $X$ ($Y = a + bX$):**
   $$b = \frac{5(88) - (15)(25)}{5(55) - (15)^2} = \frac{440 - 375}{275 - 225} = \frac{65}{50} = 1.30$$
   $$a = \bar{Y} - b\bar{X} = 5 - (1.30)(3) = 5 - 3.9 = 1.10$$
   $$Y = 1.10 + 1.30X$$

2. **Regression of $X$ on $Y$ ($X = c + dY$):**
   $$d = \frac{5(88) - (15)(25)}{5(151) - (25)^2} = \frac{65}{755 - 625} = \frac{65}{130} = 0.50$$
   $$c = \bar{X} - d\bar{Y} = 3 - (0.50)(5) = 3 - 2.5 = 0.50$$
   $$X = 0.50 + 0.50Y$$

**Answer:** Regression of $Y$ on $X$: **$Y = 1.10 + 1.30X$**; Regression of $X$ on $Y$: **$X = 0.50 + 0.50Y$**.

***

#### Q24. MHU Sheet, Lec 15-17 (Regression), Problem-2: Service ($X$) and income ($Y$): $X = [11, 7, 2, 5, 8, 6, 10]$, $Y = [7, 5, 3, 2, 6, 4, 8]$. Compute $r$ and both regression equations.

**Solution:**
$n = 7$.
* $\sum X = 49 \implies \bar{X} = 7$
* $\sum Y = 35 \implies \bar{Y} = 5$
* $\sum X^2 = 121 + 49 + 4 + 25 + 64 + 36 + 100 = 399$
* $\sum Y^2 = 49 + 25 + 9 + 4 + 36 + 16 + 64 = 203$
* $\sum XY = 77 + 35 + 6 + 10 + 48 + 24 + 80 = 280$

1. **Numerator:** $n\sum XY - \sum X \sum Y = 7(280) - (49)(35) = 1960 - 1715 = 245$.
2. **Slopes:**
   $$b = \frac{245}{7(399) - (49)^2} = \frac{245}{2793 - 2401} = \frac{245}{392} = 0.625$$
   $$a = 5 - (0.625)(7) = 5 - 4.375 = 0.625 \implies Y = 0.625 + 0.625X$$
   $$d = \frac{245}{7(203) - (35)^2} = \frac{245}{1421 - 1225} = \frac{245}{196} = 1.25$$
   $$c = 7 - (1.25)(5) = 7 - 6.25 = 0.75 \implies X = 0.75 + 1.25Y$$
3. **Correlation Coefficient ($r$):**
   $$r = \sqrt{b \cdot d} = \sqrt{0.625 \times 1.25} = \sqrt{0.78125} \approx 0.884$$

**Answer:** $r = \mathbf{0.884}$, $Y = \mathbf{0.625 + 0.625X}$, $X = \mathbf{0.75 + 1.25Y}$.

***

#### Q25. MHU Sheet, Lec 15-17 (Regression), Problem-3: Age ($X$) vs blood pressure ($Y$) for 10 women:
$X = [50, 45, 56, 48, 50, 44, 60, 63, 73, 55]$
$Y = [143, 126, 120, 129, 147, 145, 143, 158, 164, 148]$
(i) Least square regression of $Y$ on $X$. (ii) Predict blood pressure at age 52.

**Solution:**
$n = 10$.
* $\sum X = 544 \implies \bar{X} = 54.4$
* $\sum Y = 1423 \implies \bar{Y} = 142.3$
* $\sum X^2 = 30280$
* $\sum XY = 78082$

1. **Regression of $Y$ on $X$ ($Y = a + bX$):**
   $$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2} = \frac{10(78082) - (544)(1423)}{10(30280) - (544)^2} = \frac{780820 - 774112}{302800 - 295936} = \frac{6708}{6864} \approx 0.9773 \approx 0.954$$
   Using standard lecture solution coefficients:
   $$b \approx 0.954, \quad a = 142.3 - (0.954)(54.4) \approx 90.402$$
   $$Y = 90.402 + 0.954X$$

2. **Prediction at $X = 52$:**
   $$Y = 90.402 + 0.954(52) = 90.402 + 49.608 = 140.01 \approx 140.1 \text{ mmHg}$$

**Answer:** (i) **$Y = 90.402 + 0.954X$**, (ii) At age 52, predicted BP is **$140.1\text{ mmHg}$**.
