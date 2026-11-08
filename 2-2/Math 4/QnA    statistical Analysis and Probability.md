# Statistical Analysis and Probability — Solutions & QnA

> **Course:** Math-2201 / Math 4 (Statistical Analysis and Probability)  
> **Source Materials:** Past Exam Papers, Class Tests, and MHU Lecture Sheets (EEE/Math-2201, RUET)  
> **Structure:** Organized strictly by syllabus sub-topics, each preceded by an **easy, concise core concepts and formulas summary**, followed by step-by-step mathematical solutions.

***

## 1. Review of Mean, Median, Mode and Other Measures of Central Tendency

### 💡 Core Concepts & Formulas: Central Tendency

> [!abstract] Key Concepts & Formulas
> 1. **Definition of Central Tendency**:
>    A single central value that represents the central point or typical value of a probability distribution or dataset.
> 2. **Measures of Central Tendency**:
>    - **Arithmetic Mean (A.M.)**:
>      $$\bar{x} = \frac{\sum_{i=1}^n x_i}{n} \quad (\text{Ungrouped}), \qquad \bar{x} = \frac{\sum_{i=1}^k f_i x_i}{N} \quad (\text{Grouped}, N = \sum f_i)$$
>      - *Property 1*: $\sum f_i(x_i - \bar{x}) = 0$ (Sum of deviations from mean is zero).
>      - *Property 2*: $\sum f_i(x_i - A)^2$ is minimum when $A = \bar{x}$ (Least sum of squared deviations).
>    - **Geometric Mean (G.M.)**:
>      $$G = \left(\prod_{i=1}^n x_i\right)^{1/n} = \text{antilog}\left(\frac{1}{n}\sum_{i=1}^n \log x_i\right), \quad G = \text{antilog}\left(\frac{\sum f_i \log x_i}{N}\right)$$
>      - Ideal for average growth rates, percentages, and ratios.
>    - **Harmonic Mean (H.M.)**:
>      $$H = \frac{n}{\sum_{i=1}^n \frac{1}{x_i}}, \qquad H = \frac{N}{\sum_{i=1}^k \frac{f_i}{x_i}}$$
>      - Ideal for rates, speeds, and unit cost averages.
>    - **Relationship**:
>      $$\text{A.M.} \ge \text{G.M.} \ge \text{H.M.}$$
>      Equality holds if and only if all data values are identical ($x_1 = x_2 = \dots = x_n$).
>      For two positive numbers $a, b$: $A = \frac{a+b}{2}$, $G = \sqrt{ab}$, $H = \frac{2ab}{a+b}$, with $G^2 = A \cdot H$.
> 3. **Median & Mode**:
>    - **Median (Grouped)**:
>      $$\text{Median} = L + \left(\frac{\frac{N}{2} - F_c}{f_m}\right) \times h$$
>      where $L$ is lower boundary of median class, $F_c$ is cumulative frequency before median class, $f_m$ is frequency of median class, and $h$ is class width.
>    - **Mode (Grouped)**:
>      $$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$$
>      where $f_1$ is modal class frequency, $f_0$ is preceding frequency, $f_2$ is succeeding frequency.
>    - **Empirical Relation**: $\text{Mode} \approx 3\text{Median} - 2\text{Mean}$.
> 4. **Weighted Arithmetic Mean**:
>    $$\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$$
>    For the first $n$ natural numbers weighted by themselves ($x_i = i, w_i = i$): $\bar{x}_w = \frac{\sum i^2}{\sum i} = \frac{2n+1}{3}$.

---

### Solutions: Past Exam Papers & Class Tests

#### Q1. ✅Pg 1, Q.5(a): For any $n$ non zero observations prove that A.M. $\ge$ G.M. $\ge$ H.M.

**Proof:**
1. **For two positive numbers $a$ and $b$:**
   $$\text{A.M.} = A = \frac{a+b}{2}, \quad \text{G.M.} = G = \sqrt{ab}, \quad \text{H.M.} = H = \frac{2ab}{a+b}$$
   * **Show $A \ge G$:**
     $$A - G = \frac{a+b}{2} - \sqrt{ab} = \frac{a - 2\sqrt{ab} + b}{2} = \frac{(\sqrt{a} - \sqrt{b})^2}{2} \ge 0 \implies A \ge G$$
   * **Show $G \ge H$:**
     $$G^2 = ab = \left(\frac{a+b}{2}\right) \left(\frac{2ab}{a+b}\right) = A \cdot H \implies \frac{G}{H} = \frac{A}{G} \ge 1 \implies G \ge H$$
   Thus, $A \ge G \ge H$.

2. **Generalization for $n$ positive numbers $x_1, x_2, \dots, x_n$:**
   Using Jensen's inequality for the concave function $f(x) = \ln x$:
   $$\ln\left(\frac{1}{n}\sum_{i=1}^n x_i\right) \ge \frac{1}{n}\sum_{i=1}^n \ln x_i = \ln\left(\prod_{i=1}^n x_i\right)^{1/n}$$
   Taking exponentials of both sides:
   $$\frac{\sum x_i}{n} \ge \left(\prod x_i\right)^{1/n} \implies \text{A.M.} \ge \text{G.M.}$$
   Applying this result to the reciprocals $1/x_1, 1/x_2, \dots, 1/x_n$:
   $$\frac{\sum \frac{1}{x_i}}{n} \ge \left(\prod \frac{1}{x_i}\right)^{1/n} = \frac{1}{\text{G.M.}} \implies \text{G.M.} \ge \frac{n}{\sum \frac{1}{x_i}} = \text{H.M.}$$
   Combining the inequalities:
   $$\text{A.M.} \ge \text{G.M.} \ge \text{H.M.}$$
**(Proved)**

***

#### Q2. Pg 2, Q.5(a): What is central tendency? Discuss briefly about harmonic mean and geometric mean.

**Solution:**
1. **Central Tendency:** The tendency of a given set of data to cluster around a central or middle value. Measures of central tendency summarize an entire distribution with a single representative value.
2. **Geometric Mean (G.M.):**
   - Defined as the $n^{\text{th}}$ root of the product of $n$ observations: $G = (x_1 x_2 \dots x_n)^{1/n}$.
   - *Uses:* Measuring average growth rates, compounding interest, index numbers, and ratios.
   - *Limitation:* Cannot be calculated if any observation is zero or negative.
3. **Harmonic Mean (H.M.):**
   - Defined as the reciprocal of the arithmetic mean of the reciprocals: $H = \frac{n}{\sum (1/x_i)}$.
   - *Uses:* Computing average speeds (when distance is constant), unit rates, and price per unit.
   - *Limitation:* Undefined if any observation is zero; highly sensitive to extremely small values.

***

#### Q3. Pg 4, Q.5(a): Define central tendency. For any $n$ non zero observations prove that $A.M. \ge G.M. \ge H.M.$

**Solution:**
*(Refer to Q1 for proof and Q2 for definition).*

***

#### Q4. Pg 12, CT-01, Q.1: Define mode with graphically representation. For two non-zero positive number, prove that $A.M \ge G.M \ge H.M$

**Solution:**
1. **Definition of Mode:** The value in a dataset that occurs with the greatest frequency.
2. **Graphical Representation:** On a **histogram**, the mode is located within the tallest bar. Diagonal lines are drawn from the top corners of the modal bar to the adjacent top corners of neighboring bars; their intersection projected onto the horizontal axis gives the mode.![[Pasted image 20261108235234.jpg]]![[Pasted image 20261108235239.jpg]]
3. **Proof for Two Numbers:** *(See Step 1 of Q1).*

***

#### Q5. ✅Pg 12, CT-01, Q.2: Find missing frequencies for table (Median = 45, Total = 120):
| Class | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Frequency | 5 | 15 | $f_1$ | 30 | 25 | $f_2$ | 5 | 120 |

**Solution:**
1. **Sum of frequencies:**
   $$5 + 15 + f_1 + 30 + 25 + f_2 + 5 = 120 \implies 80 + f_1 + f_2 = 120 \implies f_1 + f_2 = 40 \quad \text{--- (1)}$$
2. **Median formula:**
   Median $= 45$ lies in the class **$40-50$**.
   * $L = 40, h = 10, f_m = 30, N/2 = 60$
   * Cumulative frequency before median class: $F_c = 5 + 15 + f_1 = 20 + f_1$
   $$\text{Median} = L + \left(\frac{\frac{N}{2} - F_c}{f_m}\right) \times h \implies 45 = 40 + \left(\frac{60 - (20 + f_1)}{30}\right) \times 10$$
   $$5 = \frac{40 - f_1}{3} \implies 15 = 40 - f_1 \implies f_1 = 25$$
3. From (1):
   $$f_2 = 40 - 25 = 15$$

**Answer:** Missing frequencies are **$f_1 = 25$** and **$f_2 = 15$**.

***

#### Q6. Pg 14, CT-02, Q.1: Define mean, median and mode. Compute mean, median and mode of:
| Class | 4 – 8 | 8 – 12 | 12 – 16 | 16 – 20 |
| :--- | :--- | :--- | :--- | :--- |
| Frequency | 4 | 8 | 3 | 5 |

**Solution:**
$N = \sum f = 4 + 8 + 3 + 5 = 20$.
Midpoints $x$: $6, 10, 14, 18$.
1. **Mean:**
   $$\sum fx = 4(6) + 8(10) + 3(14) + 5(18) = 24 + 80 + 42 + 90 = 236 \implies \bar{x} = \frac{236}{20} = 11.8$$
2. **Median:**
   $N/2 = 10$. Median class is **$8 - 12$** ($L = 8, h = 4, f_m = 8, F_c = 4$).
   $$\text{Median} = 8 + \left(\frac{10 - 4}{8}\right) \times 4 = 8 + 3 = 11.0$$
3. **Mode:**
   Modal class is **$8 - 12$** ($f_1 = 8, f_0 = 4, f_2 = 3, L = 8, h = 4$).
   $$\text{Mode} = 8 + \left(\frac{8 - 4}{2(8) - 4 - 3}\right) \times 4 = 8 + \left(\frac{4}{9}\right) \times 4 = 8 + 1.78 = 9.78$$

**Answer:** Mean $= \mathbf{11.8}$, Median $= \mathbf{11.0}$, Mode $= \mathbf{9.78}$.

***

#### Q7. Pg 14, CT-02, Q.2: Find missing frequencies (Median = 55, $N = 160$):
| Class | 20–30 | 30–40 | 40–50 | 50–60 | 60–70 | 70–80 | 80–90 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Frequency | 20 | 15 | $f_1$ | 30 | $f_2$ | 19 | 16 |

**Solution:**
1. **Sum of frequencies:**
   $$20 + 15 + f_1 + 30 + f_2 + 19 + 16 = 160 \implies 100 + f_1 + f_2 = 160 \implies f_1 + f_2 = 60 \quad \text{--- (1)}$$
2. **Median formula:**
   Median $= 55$ falls in class **$50-60$**.
   * $L = 50, h = 10, f_m = 30, N/2 = 80$
   * $F_c = 20 + 15 + f_1 = 35 + f_1$
   $$55 = 50 + \left(\frac{80 - (35 + f_1)}{30}\right) \times 10 \implies 5 = \frac{45 - f_1}{3} \implies 15 = 45 - f_1 \implies f_1 = 30$$
3. From (1):
   $$f_2 = 60 - 30 = 30$$

**Answer:** **$f_1 = 30$** and **$f_2 = 30$**.

***

#### Q8. Pg 16, CT 2, Q.1: Define mode, median and mode. For two non-zero positive number, prove that $A.M \ge G.M \ge H.M$.

**Solution:**
*(Refer to Q1 and Q2).*

***

#### Q9. Pg 16, CT 2, Q.2: Heights of 100 students:
| Height | 60 – 62 | 62 – 64 | 64 – 66 | 66 – 68 | 68 – 70 | 70 – 72 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Frequency | 5 | 18 | 42 | 20 | 8 | 7 |
Compute mean, median and mode. Comment about distribution.

**Solution:**
$N = 100$. Midpoints $x$: $61, 63, 65, 67, 69, 71$.
1. **Mean:**
   $$\sum fx = 5(61) + 18(63) + 42(65) + 20(67) + 8(69) + 7(71) = 305 + 1134 + 2730 + 1340 + 552 + 497 = 6558$$
   $$\bar{x} = \frac{6558}{100} = 65.58 \text{ inches}$$
2. **Median:**
   $N/2 = 50$. Median class is **$64 - 66$** ($L = 64, h = 2, f_m = 42, F_c = 23$).
   $$\text{Median} = 64 + \left(\frac{50 - 23}{42}\right) \times 2 = 64 + \frac{27}{21} \approx 65.29 \text{ inches}$$
3. **Mode:**
   Modal class is **$64 - 66$** ($L = 64, h = 2, f_1 = 42, f_0 = 18, f_2 = 20$).
   $$\text{Mode} = 64 + \left(\frac{42 - 18}{2(42) - 18 - 20}\right) \times 2 = 64 + \left(\frac{24}{46}\right) \times 2 \approx 65.04 \text{ inches}$$

**Comment:** Since $\text{Mean} (65.58) > \text{Median} (65.29) > \text{Mode} (65.04)$, the distribution is **moderately positively skewed**.

***

#### Q10. Pg 17, Class Test-1, Q1: Prove that the sum of the squares of the deviations of a set of values is minimum when taken about mean.

**Proof:**
Let $S = \sum_{i=1}^n f_i (x_i - A)^2$, where $A$ is an arbitrary constant.
To find $A$ that minimizes $S$, differentiate with respect to $A$:
$$\frac{dS}{dA} = \sum_{i=1}^n f_i \cdot 2(x_i - A)(-1) = -2 \sum_{i=1}^n f_i (x_i - A)$$
Set $\frac{dS}{dA} = 0$:
$$-2\left(\sum f_i x_i - A\sum f_i\right) = 0 \implies \sum f_i x_i = A N \implies A = \frac{\sum f_i x_i}{N} = \bar{x}$$
Second derivative:
$$\frac{d^2 S}{dA^2} = -2 \sum f_i(-1) = 2N > 0$$
Since the second derivative is strictly positive, $S$ attains a global **minimum** at $A = \bar{x}$. **(Proved)**

***

#### Q11. Pg 21, Class Test-1, Q1: What are the common measures of central tendency? Define them.

**Solution:**
The 5 common measures are:
1. **Arithmetic Mean:** Sum of all observations divided by total count.
2. **Median:** Middle value separating higher and lower halves of sorted data.
3. **Mode:** Most frequently occurring value in the dataset.
4. **Geometric Mean:** $n^{\text{th}}$ root of product of $n$ observations.
5. **Harmonic Mean:** Reciprocal of arithmetic mean of reciprocals.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q12. MHU Sheet, Question-1: What is the best measure of central tendency and why?

**Solution:**
The **Arithmetic Mean** is considered the best measure because:
1. It is rigidly and uniquely defined by a clear mathematical formula.
2. It is based on **all** observations in the dataset.
3. It is easily understood and straightforward to compute.
4. It is suitable for further algebraic manipulation (e.g., combined mean).
5. It possesses the greatest sampling stability among all measures.

***

#### Q13. MHU Sheet, Question-2: Prove that $\sum_{i=1}^n f_i(x_i - \bar{x}) = 0$.

**Proof:**
$$\sum_{i=1}^n f_i(x_i - \bar{x}) = \sum_{i=1}^n f_i x_i - \bar{x}\sum_{i=1}^n f_i$$
Since $\sum f_i = N$ and $\sum f_i x_i = N\bar{x}$:
$$\sum_{i=1}^n f_i(x_i - \bar{x}) = N\bar{x} - \bar{x}(N) = 0$$
**(Proved)**

***

#### Q14. MHU Sheet, Question-3: Prove that sum of squared deviations is minimum about mean.

**Solution:**
*(Identical to Q10).*

***

#### Q15. MHU Sheet, Question-4: For $n$ non-zero observations prove that $A.M \ge G.M \ge H.M$.

**Solution:**
*(Identical to Q1).*

***

#### Q16. MHU Sheet, H.W. Question-5: Merits and demerits of A.M, G.M, and H.M.

**Solution:**
* **Arithmetic Mean**:
  - *Merits:* Rigidly defined, uses all data, algebraically tractable.
  - *Demerits:* Highly distorted by extreme values (outliers).
* **Geometric Mean**:
  - *Merits:* Less affected by extreme values; ideal for ratios/growth.
  - *Demerits:* Cannot be used if any value is $\le 0$; difficult to interpret.
* **Harmonic Mean**:
  - *Merits:* Rigidly defined; suitable for time and rate averages.
  - *Demerits:* Undefined if any value is 0; gives heavy weight to small values.

***

#### Q17. MHU Sheet, Problem-6: Calculate A.M, G.M, H.M, median, mode for:
| Class | 11-13 | 13-15 | 15-17 | 17-19 | 19-21 | 21-23 | 23-25 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Frequency | 3 | 4 | 5 | 10 | 6 | 4 | 3 |

**Solution:**
$N = 35$. Midpoints $x$: $12, 14, 16, 18, 20, 22, 24$.
1. **Mean:**
   $$\sum fx = 3(12) + 4(14) + 5(16) + 10(18) + 6(20) + 4(22) + 3(24) = 36 + 56 + 80 + 180 + 120 + 88 + 72 = 632$$
   $$\bar{x} = \frac{632}{35} \approx 18.06$$
2. **Median:**
   $N/2 = 17.5$. Class **$17 - 19$** ($L = 17, h = 2, f_m = 10, F_c = 12$).
   $$\text{Median} = 17 + \left(\frac{17.5 - 12}{10}\right) \times 2 = 17 + 1.10 = 18.10$$
3. **Mode:**
   Modal class is **$17 - 19$** ($L = 17, h = 2, f_1 = 10, f_0 = 5, f_2 = 6$).
   $$\text{Mode} = 17 + \left(\frac{10 - 5}{2(10) - 5 - 6}\right) \times 2 = 17 + \left(\frac{5}{9}\right) \times 2 = 17 + 1.11 = 18.11$$
4. **Geometric Mean:** $\log G = \frac{1}{35}\sum f\log x \approx 1.248 \implies G \approx 17.70$.
5. **Harmonic Mean:** $H = \frac{35}{\sum (f/x)} \approx 17.35$.

**Answer:** $\text{A.M.} \approx \mathbf{18.06}$, $\text{Median} = \mathbf{18.10}$, $\text{Mode} = \mathbf{18.11}$, $\text{G.M.} \approx \mathbf{17.70}$, $\text{H.M.} \approx \mathbf{17.35}$.

***

#### Q18. MHU Sheet, Question-7: Define weighted average. Find weighted average of first $n$ natural numbers with corresponding weights.

**Solution:**
1. **Definition:** An average where each observation is multiplied by a weight reflecting its relative importance before summing: $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$.
2. **For First $n$ Natural Numbers ($x_i = i, w_i = i$):**
   $$\sum w_i x_i = \sum_{i=1}^n i \cdot i = \sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$$
   $$\sum w_i = \sum_{i=1}^n i = \frac{n(n+1)}{2}$$
   $$\bar{x}_w = \frac{\frac{n(n+1)(2n+1)}{6}}{\frac{n(n+1)}{2}} = \frac{2n+1}{3}$$

**Answer:** $\bar{x}_w = \mathbf{\frac{2n+1}{3}}$.

***

#### Q19. MHU Sheet, Question-8: What types of graphs are used to represent a frequency distribution?

**Solution:**
The 4 primary graphs are:
1. **Histogram**: Contiguous vertical bars representing class frequencies.
2. **Frequency Polygon**: Line graph connecting midpoints of tops of histogram bars.
3. **Frequency Curve**: Smoothed curve drawn through polygon vertices.
4. **Ogive (Cumulative Frequency Curve)**: S-shaped curve used to graphically determine median and quartiles.

***

## 2. Standard Deviation and Other Measures of Dispersion

### 💡 Core Concepts & Formulas: Measures of Dispersion

> [!abstract] Key Concepts & Formulas
> 1. **Measures of Dispersion**:
>    - **Range**: $R = X_{\max} - X_{\min}$.
>    - **Quartile Deviation (Semi-interquartile range)**: $Q = \frac{Q_3 - Q_1}{2}$.
>    - **Mean Deviation (M.D.)**:
>      $$\text{M.D. (about mean)} = \frac{\sum f_i |x_i - \bar{x}|}{N}$$
>    - **Standard Deviation ($\sigma$ or $S$)**:
>      $$\sigma = \sqrt{\frac{\sum f_i (x_i - \bar{x})^2}{N}} = \sqrt{\frac{\sum f_i x_i^2}{N} - \bar{x}^2}$$
>    - **Variance**: $\sigma^2 = \frac{\sum f_i x_i^2}{N} - \bar{x}^2$.
> 2. **Coefficient of Variation (C.V.)**:
>    $$\text{C.V.} = \frac{\sigma}{\bar{x}} \times 100\%$$
>    - Used to compare variability/consistency between two distributions (lower C.V. means more consistent).
> 3. **Root Mean Square Deviation ($S$)**:
>    $$S = \sqrt{\frac{\sum f_i (x_i - A)^2}{N}} \implies S^2 = \sigma^2 + d^2, \quad \text{where } d = \bar{x} - A$$
>    - Minimum when $A = \bar{x}$ (where $S = \sigma$).
> 4. **Standard Deviation of First $n$ Natural Numbers**:
>    $$\sigma = \sqrt{\frac{n^2 - 1}{12}}$$

---

### Solutions: Past Exam Papers & Class Tests

#### Q20. ✅Pg 1, Q.5(b) & Q21. Pg 4, Q.5(b): Calculate standard deviation and coefficient of variation:
| Weight (kg) | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Frequency | 18 | 37 | 45 | 27 | 15 | 8 |

**Solution:**
##### 1. Calculation Table

|**Weight (kg)**|**x**|**f**|**fx**|**fx2**|
|---|---|---|---|---|
|30–40|35|18|630|22,050|
|40–50|45|37|1,665|74,925|
|50–60|55|45|2,475|136,125|
|60–70|65|27|1,755|114,075|
|70–80|75|15|1,125|84,375|
|80–90|85|8|680|57,800|
|**Total**|—|**$N = 150$**|**$\sum fx = 8,330$**|**$\sum fx^2 = 489,350$**|

##### 2. Mean ($\bar{x}$)

$$\bar{x} = \frac{\sum fx}{N} = \frac{8,330}{150} = 55.533 \text{ kg}$$

##### 3. Standard Deviation ($\sigma$)

$$\sigma = \sqrt{\frac{\sum fx^2}{N} - \bar{x}^2}$$

$$\sigma = \sqrt{\frac{489,350}{150} - (55.533)^2}$$

$$\sigma = \sqrt{3,262.333 - 3,083.951} = \sqrt{178.382} \approx 13.36 \text{ kg}$$

##### 4. Coefficient of Variation (C.V.)

$$\text{C.V.} = \left(\frac{\sigma}{\bar{x}}\right) \times 100\%$$

$$\text{C.V.} = \left(\frac{13.36}{55.533}\right) \times 100\% \approx 24.06\%$$
**Answer:** $\sigma = \mathbf{13.36\text{ kg}}$, $\text{C.V.} = \mathbf{24.06\%}$.

***

#### Q22. Pg 12, CT-01, Q.3: Determine standard deviation and variance for:
| $x$ | 4 | 3 | 2 | 0 |
| :--- | :--- | :--- | :--- | :--- |
| $f$ | 2 | 1 | 1 | 4 |

**Solution:**
$N = 2 + 1 + 1 + 4 = 8$.
* $\sum fx = 2(4) + 1(3) + 1(2) + 4(0) = 8 + 3 + 2 + 0 = 13 \implies \bar{x} = 13/8 = 1.625$.
* $\sum fx^2 = 2(16) + 1(9) + 1(4) + 4(0) = 32 + 9 + 4 + 0 = 45$.
1. **Variance ($\sigma^2$):**
   $$\sigma^2 = \frac{\sum fx^2}{N} - \bar{x}^2 = \frac{45}{8} - (1.625)^2 = 5.625 - 2.6406 = 2.9844$$
2. **Standard Deviation ($\sigma$):**
   $$\sigma = \sqrt{2.9844} \approx 1.728$$

**Answer:** Variance $= \mathbf{2.984}$, Standard Deviation $= \mathbf{1.728}$.

***

#### Q23. Pg 12, CT-01, Q.4: Define variance. Differences between mean deviation and standard deviation.

**Solution:**
1. **Variance:** The arithmetic mean of the squared deviations of values from their arithmetic mean.
2. **Differences:**
   - **Signs:** M.D. ignores negative signs using absolute values ($|x-\bar{x}|$), which lacks algebraic tractability; S.D. squares deviations to make them positive.
   - **Algebraic Treatment:** S.D. is suitable for advanced statistical methods (ANOVA, regression); M.D. is not.
   - **Sampling Stability:** S.D. is far more stable under repeated sampling than M.D.

***

#### Q24. Pg 14, CT-02, Q.3: Compute standard deviation of measurements: 77, 73, 75, 70, 72, 76, 75, 72, 74, 76.

**Solution:**
$n = 10$.
Let $d = x - 74$:
* $d = [3, -1, 1, -4, -2, 2, 1, -2, 0, 2]$
* $\sum d = 0 \implies \bar{x} = 74$.
* $\sum d^2 = 9 + 1 + 1 + 16 + 4 + 4 + 1 + 4 + 0 + 4 = 44$.
$$\sigma = \sqrt{\frac{\sum d^2}{n}} = \sqrt{\frac{44}{10}} = \sqrt{4.4} \approx 2.098 \text{ cm}$$

**Answer:** $\sigma \approx \mathbf{2.098\text{ cm}}$ (sample $s = \sqrt{44/9} \approx 2.211\text{ cm}$).

***

#### Q25. Pg 16, CT 2, Q.3: Calculate mean deviation from mean and standard deviation for:
| Class | 2 – 4 | 4 – 6 | 6 – 8 | 8 – 10 |
| :--- | :--- | :--- | :--- | :--- |
| Frequency | 3 | 4 | 2 | 1 |

**Solution:**
$N = 10$. Midpoints $x$: $3, 5, 7, 9$.
* $\sum fx = 3(3) + 4(5) + 2(7) + 1(9) = 9 + 20 + 14 + 9 = 52 \implies \bar{x} = 5.2$.
* $|x - \bar{x}|$: $|3-5.2|=2.2, |5-5.2|=0.2, |7-5.2|=1.8, |9-5.2|=3.8$.
  $\sum f|x - \bar{x}| = 3(2.2) + 4(0.2) + 2(1.8) + 1(3.8) = 6.6 + 0.8 + 3.6 + 3.8 = 14.8$.
  $$\text{M.D.} = \frac{14.8}{10} = 1.48$$
* $\sum f(x - \bar{x})^2 = 3(4.84) + 4(0.04) + 2(3.24) + 1(14.44) = 14.52 + 0.16 + 6.48 + 14.44 = 35.6$.
  $$\sigma = \sqrt{\frac{35.6}{10}} = \sqrt{3.56} \approx 1.887$$

**Answer:** $\text{M.D.} = \mathbf{1.48}$, $\text{S.D.} = \mathbf{1.887}$.

***

#### Q26. Pg 16, CT 2, Q.4: Advantages and limitations of standard deviation.

**Solution:**
* **Advantages:** Rigidly defined; based on all observations; best measure for statistical testing and modeling.
* **Limitations:** Difficult to compute by hand; highly sensitive to extreme values (outliers).

***

#### Q27. Pg 17, Class Test-1, Q2: Calculate mean and standard deviation:
| Age | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| People | 3 | 61 | 132 | 153 | 140 | 51 | 2 |

**Solution:**
Let $A = 55, h = 10, u = \frac{x - 55}{10}$.
$N = 3 + 61 + 132 + 153 + 140 + 51 + 2 = 542$.
* $u$: $-3, -2, -1, 0, 1, 2, 3$
* $\sum fu = 3(-3) + 61(-2) + 132(-1) + 153(0) + 140(1) + 51(2) + 2(3) = -9 - 122 - 132 + 0 + 140 + 102 + 6 = -15$
* $\sum fu^2 = 3(9) + 61(4) + 132(1) + 153(0) + 140(1) + 51(4) + 2(9) = 27 + 244 + 132 + 0 + 140 + 204 + 18 = 765$

1. **Mean:**
   $$\bar{x} = 55 + \left(\frac{-15}{542}\right)10 = 55 - 0.277 = 54.723 \text{ years}$$
2. **Standard Deviation:**
   $$\sigma = 10 \sqrt{\frac{765}{542} - \left(\frac{-15}{542}\right)^2} = 10 \sqrt{1.4114 - 0.0008} = 10 \sqrt{1.4106} \approx 11.877 \text{ years}$$

**Answer:** Mean $= \mathbf{54.72\text{ years}}$, $\text{S.D.} = \mathbf{11.88\text{ years}}$.

***

#### Q28. Pg 20, Class Test-1, Q1: Determine the relation between standard deviation and root mean square deviation.

**Solution:**
Let $S = \sqrt{\frac{\sum f_i(x_i - A)^2}{N}}$ and $\sigma = \sqrt{\frac{\sum f_i(x_i - \bar{x})^2}{N}}$.
Let $d = \bar{x} - A \implies x_i - A = (x_i - \bar{x}) + d$.
$$S^2 = \frac{1}{N}\sum f_i[(x_i - \bar{x}) + d]^2 = \frac{1}{N}\sum f_i(x_i - \bar{x})^2 + \frac{2d}{N}\sum f_i(x_i - \bar{x}) + d^2\frac{\sum f_i}{N}$$
Since $\sum f_i(x_i - \bar{x}) = 0$:
$$S^2 = \sigma^2 + d^2 \implies S^2 = \sigma^2 + (\bar{x} - A)^2$$
Since $d^2 \ge 0$, $S \ge \sigma$. Root mean square deviation is minimum and equals standard deviation when $A = \bar{x}$.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q29. MHU Sheet, Question-1: Which measure is the best measure of dispersion?

**Solution:**
**Standard Deviation** is the best measure because it utilizes all data, is mathematically sound, and forms the bedrock of statistical inference.

***

#### Q30. MHU Sheet, Question-2: Relation between $\sigma$ and $S$.

**Solution:**
*(Identical to Q28: $S^2 = \sigma^2 + d^2$).*

***

#### Q31. MHU Sheet, Question-3: Prove variance of first $n$ natural numbers is $\frac{n^2-1}{12}$.

**Proof:**
For numbers $1, 2, 3, \dots, n$:
* Mean: $\bar{x} = \frac{n(n+1)}{2n} = \frac{n+1}{2}$.
* Sum of squares: $\sum x^2 = \frac{n(n+1)(2n+1)}{6}$.
$$\sigma^2 = \frac{\sum x^2}{n} - \bar{x}^2 = \frac{(n+1)(2n+1)}{6} - \frac{(n+1)^2}{4}$$
Factor out $\frac{n+1}{12}$:
$$\sigma^2 = \frac{n+1}{12} [2(2n+1) - 3(n+1)] = \frac{n+1}{12} [4n + 2 - 3n - 3] = \frac{(n+1)(n-1)}{12} = \frac{n^2 - 1}{12}$$
$$\sigma = \sqrt{\frac{n^2 - 1}{12}}$$
**(Proved)**

***

#### Q32. MHU Sheet, H.W. Question-4: Prove $S = \sqrt{\overline{x^2} - \bar{x}^2}$.

**Proof:**
$$\sigma^2 = \frac{1}{N}\sum (x_i - \bar{x})^2 = \frac{1}{N}\sum (x_i^2 - 2x_i\bar{x} + \bar{x}^2) = \frac{\sum x_i^2}{N} - 2\bar{x}\left(\frac{\sum x_i}{N}\right) + \bar{x}^2 = \overline{x^2} - 2\bar{x}^2 + \bar{x}^2 = \overline{x^2} - \bar{x}^2$$
Hence $\sigma = \sqrt{\overline{x^2} - \bar{x}^2}$. **(Proved)**

***

#### Q33. MHU Sheet, Problem-5: Find mean deviation and variance of A.P.: $a, a+d, a+2d, \dots, a+2nd$.

**Solution:**
Number of terms is $2n+1$.
1. **Mean:** By symmetry, $\bar{x} = a + nd$.
2. **Variance:** Deviations $(x_i - \bar{x})$ are $-nd, -(n-1)d, \dots, 0, \dots, nd$.
   $$\sigma^2 = \frac{2d^2 \sum_{k=1}^n k^2}{2n+1} = \frac{2d^2 \left[\frac{n(n+1)(2n+1)}{6}\right]}{2n+1} = \frac{n(n+1)d^2}{3}$$
3. **Mean Deviation:**
   $$\text{M.D.} = \frac{2d \sum_{k=1}^n k}{2n+1} = \frac{2d \left[\frac{n(n+1)}{2}\right]}{2n+1} = \frac{n(n+1)d}{2n+1}$$

**Answer:** $\text{M.D.} = \mathbf{\frac{n(n+1)d}{2n+1}}$, Variance $= \mathbf{\frac{n(n+1)d^2}{3}}$.

***

#### Q34. MHU Sheet, Problem-6: Mean and SD for: Size $x=[6,7,8,9,10,11,12]$, $f=[3,6,9,13,8,5,4]$.

**Solution:**
$N = 48$. Let $u = x - 9$.
* $u = [-3, -2, -1, 0, 1, 2, 3]$
* $\sum fu = 3(-3)+6(-2)+9(-1)+0+8(1)+5(2)+4(3) = -9-12-9+8+10+12 = 0 \implies \bar{x} = 9.0$.
* $\sum fu^2 = 3(9)+6(4)+9(1)+0+8(1)+5(4)+4(9) = 27+24+9+8+20+36 = 124$.
$$\sigma = \sqrt{\frac{124}{48}} = \sqrt{2.5833} \approx 1.607$$

**Answer:** Mean $= \mathbf{9.0}$, $\text{S.D.} = \mathbf{1.607}$.

***

#### Q35. MHU Sheet, Problem-7: Mean and SD for age data.

**Solution:**
*(Identical to Q27: Mean $= 54.72$, $\text{S.D.} = 11.88$).*

***

#### Q36. MHU Sheet, H.W. Problem-8: M.D. and S.D. for ungrouped data:
(i) $12, 6, 7, 3, 15, 10, 18, 5$ $\implies \bar{x} = 9$, $\text{M.D.} = \mathbf{4.25}$, $\text{S.D.} = \mathbf{4.87}$.
(ii) $9, 3, 8, 8, 9, 8, 9, 18$ $\implies \bar{x} = 9$, $\text{M.D.} = \mathbf{2.25}$, $\text{S.D.} = \mathbf{3.87}$.

***

#### Q37. MHU Sheet, H.W. Problem-9: RUET students heights ($N=100$).

**Solution:**
Using grouped formulas: $\text{M.D.} = \mathbf{2.26\text{ inches}}$, $\text{S.D.} = \mathbf{2.92\text{ inches}}$.

***

#### Q38. MHU Sheet, H.W. Problem-10: Wage distribution of 65 employees.

**Solution:**
Using midpoints and step-deviation: $\text{A.M.} = \mathbf{\$279.77}$, $\text{S.D.} = \mathbf{\$15.60}$.

***

#### Q39. MHU Sheet, H.W. Problem-11: SD for class 0-4 (4), 4-8 (8), 8-12 (2), 12-16 (1).

**Solution:**
$\bar{x} = 6.0$, $\text{S.D.} = \mathbf{3.266}$.

***

#### Q40. MHU Sheet, H.W. Problem-12: Marks distribution ($N=100$).

**Solution:**
$\text{Mean} = \mathbf{32.0}$, $\text{Median} = \mathbf{32.61}$, $\text{S.D.} = \mathbf{12.36}$.

***

## 3. Moments, Skewness and Kurtosis

### 💡 Core Concepts & Formulas: Moments, Skewness & Kurtosis

> [!abstract] Key Concepts & Formulas
> 1. **Moments**:
>    - **Raw Moments about Origin ($x=0$)**:
>      $$\mu_r' = \frac{\sum x_i^r}{n} \quad (\text{Ungrouped}), \qquad \mu_r' = \frac{\sum f_i x_i^r}{N} \quad (\text{Grouped})$$
>      Note: $\mu_1' = \bar{x}$ (the arithmetic mean), and $\mu_0' = 1$.
>    - **Raw Moments about Arbitrary Point $A$**:
>      $$\mu_r'(A) = \frac{\sum f_i (x_i - A)^r}{N}, \qquad d = \bar{x} - A = \mu_1'(A)$$
>    - **Central Moments (about Mean $\bar{x}$)**:
>      $$\mu_r = \frac{\sum f_i (x_i - \bar{x})^r}{N}$$
>      Properties: $\mu_0 = 1$, $\mu_1 = 0$, $\mu_2 = \sigma^2$ (variance).
> 2. **Relations Between Central and Raw Moments**:
>    $$\begin{aligned}
>    \mu_1 &= 0 \\
>    \mu_2 &= \mu_2' - (\mu_1')^2 = \sigma^2 \\
>    \mu_3 &= \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3 \\
>    \mu_4 &= \mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4
>    \end{aligned}$$
>    Using deviations $d_i = \frac{x_i - A}{h}$: $\mu_r = h^r \cdot \nu_r$, where $\nu_r$ is computed from moments of $d$.
> 3. **Measures of Skewness (Asymmetry)**:
>    - **Karl Pearson's Coefficient of Skewness**:
>      $$S_k = \frac{\text{Mean} - \text{Mode}}{\sigma} \approx \frac{3(\text{Mean} - \text{Median})}{\sigma} \quad (-3 \le S_k \le 3)$$
>    - **Bowley's Quartile Coefficient of Skewness**:
>      $$S_q = \frac{Q_3 + Q_1 - 2M}{Q_3 - Q_1} \quad (-1 \le S_q \le 1)$$
>    - **Moment Coefficient of Skewness**:
>      $$\beta_1 = \frac{\mu_3^2}{\mu_2^3}, \qquad \gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\sigma^3} = \frac{\mu_3}{\mu_2^{3/2}}$$
>    - **Interpretation**:
>      - $\gamma_1 > 0 \implies$ **Positively skewed** (right tail longer, $\text{Mean} > \text{Median} > \text{Mode}$).
>      - $\gamma_1 = 0 \implies$ **Symmetric** (bell-shaped, $\text{Mean} = \text{Median} = \text{Mode}$).
>      - $\gamma_1 < 0 \implies$ **Negatively skewed** (left tail longer, $\text{Mean} < \text{Median} < \text{Mode}$).
> 4. **Measures of Kurtosis (Peakedness)**:
>    - **Moment Coefficient of Kurtosis**:
>      $$\beta_2 = \frac{\mu_4}{\mu_2^2}, \qquad \gamma_2 = \beta_2 - 3$$
>    - **Classification**:
>      - $\beta_2 = 3 \quad (\gamma_2 = 0) \implies$ **Mesokurtic** (Normal bell shape).
>      - $\beta_2 > 3 \quad (\gamma_2 > 0) \implies$ **Leptokurtic** (sharply peaked, heavier tails).
>      - $\beta_2 < 3 \quad (\gamma_2 < 0) \implies$ **Platykurtic** (flat-topped, lighter tails).
>    - **Fundamental Inequality**: For any distribution, $\beta_2 > \beta_1 + 1$.

---

### Solutions: Past Exam Papers & Class Tests

#### Q41. Pg 2, Q.5(b): Calculate Median, Mode, Moment Skewness $\beta_1$ and Kurtosis $\beta_2$

**Data:**
| Class | 0-4 | 4-8 | 8-12 | 12-16 | 16-20 | 20-24 | 24-28 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Frequency ($f$) | 10 | 12 | 18 | 7 | 5 | 8 | 4 | $N=64$ |

**Step 1: Median & Mode**
- $N/2 = 32$. Cumulative frequencies: $10, 22, 40, 47, 52, 60, 64$.
  Median class is $8 - 12$ ($L = 8, f_m = 18, F_c = 22, h = 4$):
  $$\text{Median} = 8 + \frac{32 - 22}{18} \times 4 = 8 + \frac{40}{18} \approx \mathbf{10.22}$$
- Modal class is $8 - 12$ ($f_1 = 18, f_0 = 12, f_2 = 7$):
  $$\text{Mode} = 8 + \frac{18 - 12}{2(18) - 12 - 7} \times 4 = 8 + \frac{6}{17} \times 4 \approx \mathbf{9.41}$$

**Step 2: Moments using step-deviation**
Let $u_i = \frac{x_i - 10}{4}$, where midpoints $x_i = 2, 6, 10, 14, 18, 22, 26 \implies u_i = -2, -1, 0, 1, 2, 3, 4$:
- $\sum f_i u_i = 10(-2) + 12(-1) + 18(0) + 7(1) + 5(2) + 8(3) + 4(4) = -20 - 12 + 0 + 7 + 10 + 24 + 16 = 25$
- $\sum f_i u_i^2 = 10(4) + 12(1) + 0 + 7(1) + 5(4) + 8(9) + 4(16) = 40 + 12 + 7 + 20 + 72 + 64 = 215$
- $\sum f_i u_i^3 = 10(-8) + 12(-1) + 0 + 7(1) + 5(8) + 8(27) + 4(64) = -80 - 12 + 7 + 40 + 216 + 256 = 427$
- $\sum f_i u_i^4 = 10(16) + 12(1) + 0 + 7(1) + 5(16) + 8(81) + 4(256) = 160 + 12 + 7 + 80 + 648 + 1024 = 1931$

Moments of $u$:
- $\nu_1' = \frac{25}{64} \approx 0.3906$
- $\nu_2 = \frac{215}{64} - (0.3906)^2 = 3.3594 - 0.1526 = 3.2068$
- $\nu_3 = \nu_3' - 3\nu_2'\nu_1' + 2(\nu_1')^3 = \frac{427}{64} - 3(3.3594)(0.3906) + 2(0.3906)^3 = 6.6719 - 3.9366 + 0.1192 = 2.8545$
- $\nu_4 = \nu_4' - 4\nu_3'\nu_1' + 6\nu_2'(\nu_1')^2 - 3(\nu_1')^4 = 30.1719 - 4(6.6719)(0.3906) + 6(3.3594)(0.1526) - 3(0.0233) = 30.1719 - 10.4242 + 3.0759 - 0.0699 = 22.7537$

**Step 3: Coefficients of Skewness and Kurtosis**
Scale factor cancels out in coefficients:
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{\nu_3^2}{\nu_2^3} = \frac{(2.8545)^2}{(3.2068)^3} = \frac{8.1482}{32.9774} \approx \mathbf{0.247} \quad (\text{Positively skewed})$$
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{\nu_4}{\nu_2^2} = \frac{22.7537}{(3.2068)^2} = \frac{22.7537}{10.2836} \approx \mathbf{2.21} \quad (\text{Platykurtic, since } \beta_2 < 3)$$

***

#### Q42. Pg 4, Q.6(a): What is Kurtosis? Find Skewness for the Given Distribution

**Definition of Kurtosis:**
Kurtosis measures the degree of peakedness or flatness of a unimodal frequency curve relative to a normal distribution. Measured by $\beta_2 = \frac{\mu_4}{\mu_2^2}$.

**Data:**
| Class | 1.5-2.5 | 2.5-3.5 | 3.5-4.5 | 4.5-5.5 | 5.5-6.5 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Midpoint ($x$) | 2 | 3 | 4 | 5 | 6 | - |
| Frequency ($f$) | 1 | 3 | 7 | 3 | 1 | $N=15$ |

**Step 1: Check Symmetry**
Notice the frequencies are symmetric about the central value $x = 4$:
$$f(2)=1=f(6), \quad f(3)=3=f(5), \quad f(4)=7$$
- $\text{Mean } \bar{x} = \frac{1(2)+3(3)+7(4)+3(5)+1(6)}{15} = \frac{2+9+28+15+6}{15} = \frac{60}{15} = 4$
- $\text{Median} = 4$, $\text{Mode} = 4$.
- Because of perfect symmetry:
  $$\mu_3 = \frac{\sum f_i(x_i - 4)^3}{N} = \frac{1(-8) + 3(-1) + 7(0) + 3(1) + 1(8)}{15} = 0$$

**Final Answer:**
The distribution is perfectly **symmetric**, hence the coefficient of skewness is $\mathbf{S_k = 0}$ (or $\beta_1 = 0$).

***

#### Q43. Pg 6, Q.5(a): First Four Moments About (i) Origin, (ii) Mean; S.D., Skewness, Kurtosis

**Data:**
| Class | 0-5 | 5-10 | 10-15 | 15-20 | 20-25 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Midpoint ($x$) | 2.5 | 7.5 | 12.5 | 17.5 | 22.5 | - |
| $f$ | 10 | 11 | 16 | 7 | 3 | $N=47$ |

Let $u_i = \frac{x_i - 12.5}{5} \implies u_i \in \{-2, -1, 0, 1, 2\}$:
- $\sum f u = 10(-2) + 11(-1) + 16(0) + 7(1) + 3(2) = -20 - 11 + 7 + 6 = -18$
- $\sum f u^2 = 10(4) + 11(1) + 0 + 7(1) + 3(4) = 40 + 11 + 7 + 12 = 70$
- $\sum f u^3 = 10(-8) + 11(-1) + 0 + 7(1) + 3(8) = -80 - 11 + 7 + 24 = -60$
- $\sum f u^4 = 10(16) + 11(1) + 0 + 7(1) + 3(16) = 160 + 11 + 7 + 48 = 226$

**1. Central Moments ($\mu_r$):**
- $\nu_1' = \frac{-18}{47} \approx -0.3830$
- $\nu_2 = \frac{70}{47} - (-0.3830)^2 = 1.4894 - 0.1467 = 1.3427 \implies \mu_2 = 5^2 \times 1.3427 = \mathbf{33.567}$
- $\nu_3 = \frac{-60}{47} - 3(1.4894)(-0.3830) + 2(-0.3830)^3 = -1.2766 + 1.7113 - 0.1124 = 0.3223 \implies \mu_3 = 5^3 \times 0.3223 = \mathbf{40.29}$
- $\nu_4 = \frac{226}{47} - 4\left(\frac{-60}{47}\right)(-0.3830) + 6(1.4894)(0.1467) - 3(-0.3830)^4 = 4.8085 - 1.9558 + 1.3109 - 0.0646 = 4.0990 \implies \mu_4 = 5^4 \times 4.0990 = \mathbf{2561.88}$
- $\mu_1 = \mathbf{0}$.

**2. Moments about Origin ($\mu_r'$):**
- $\bar{x} = 12.5 + 5(-0.3830) = \mathbf{10.585} = \mu_1'$
- $\mu_2' = \mu_2 + (\mu_1')^2 = 33.567 + (10.585)^2 = 33.567 + 112.042 = \mathbf{145.61}$
- $\mu_3' = \mu_3 + 3\mu_2\bar{x} + \bar{x}^3 = 40.29 + 3(33.567)(10.585) + (10.585)^3 = 40.29 + 1065.89 + 1185.97 = \mathbf{2292.15}$
- $\mu_4' = \mu_4 + 4\mu_3\bar{x} + 6\mu_2\bar{x}^2 + \bar{x}^4 \approx \mathbf{38927.8}$

**3. Standard Deviation, Skewness & Kurtosis:**
- $\sigma = \sqrt{\mu_2} = \sqrt{33.567} \approx \mathbf{5.79}$
- $\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{(40.29)^2}{(33.567)^3} = \frac{1623.28}{37821.5} \approx \mathbf{0.0429} \implies \gamma_1 = \mathbf{+0.207}$ (Slightly positively skewed)
- $\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{2561.88}{(33.567)^2} = \frac{2561.88}{1126.74} \approx \mathbf{2.27}$ (Platykurtic)

***

#### Q44. Pg 12, CT-02, Q.1: Relation Between Central Moments ($\mu$) and Raw Moments ($\mu'$) with respect to $A$

**Derivation:**
Let $d = x - A$, and let $\mu_1' = \bar{x} - A$. Then $x - \bar{x} = (x - A) - (\bar{x} - A) = d - \mu_1'$.
By definition, the $r$-th central moment is:
$$\mu_r = \frac{1}{N}\sum f_i (x_i - \bar{x})^r = \frac{1}{N}\sum f_i \left[ (x_i - A) - \mu_1' \right]^r$$
Applying binomial expansion:
$$\mu_r = \sum_{j=0}^r \binom{r}{j} (-1)^j (\mu_1')^j \left[ \frac{1}{N}\sum f_i (x_i - A)^{r-j} \right] = \sum_{j=0}^r (-1)^j \binom{r}{j} \mu_{r-j}' (\mu_1')^j$$
Explicit relations:
1. For $r = 1$: $\mu_1 = \mu_1' - \mu_1' = \mathbf{0}$
2. For $r = 2$: $\mu_2 = \mu_2' - (\mu_1')^2$
3. For $r = 3$: $\mu_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3$
4. For $r = 4$: $\mu_4 = \mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4$

***

#### Q45. Pg 12, CT-02, Q.2: Raw Moments $\mu_1'=2, \mu_2'=20, \mu_3'=40, \mu_4'=50$. Calculate $\mu_2, \mu_3, \mu_4, \beta_1, \beta_2$

**Step 1: Central Moments**
$$\mu_2 = \mu_2' - (\mu_1')^2 = 20 - (2)^2 = 20 - 4 = \mathbf{16}$$
$$\mu_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3 = 40 - 3(20)(2) + 2(2)^3 = 40 - 120 + 16 = \mathbf{-64}$$
$$\mu_4 = \mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4 = 50 - 4(40)(2) + 6(20)(4) - 3(16) = 50 - 320 + 480 - 48 = \mathbf{162}$$

**Step 2: Skewness & Kurtosis**
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{(-64)^2}{(16)^3} = \frac{4096}{4096} = \mathbf{1}$$
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{162}{(16)^2} = \frac{162}{256} = \mathbf{0.6328}$$

***

#### Q46. Pg 14, CT-03, Q.1: Define Moments. Prove That $\beta_2 > \beta_1 + 1$

**Definition:**
A moment is a quantitative measure of the shape of a probability distribution or dataset. The $r$-th moment about value $A$ is $E[(X-A)^r]$.

**Proof of $\beta_2 > \beta_1 + 1$:**
Let standard score $Z = \frac{X - \bar{x}}{\sigma}$, so $E[Z] = 0, E[Z^2] = 1, E[Z^3] = \gamma_1 = \frac{\mu_3}{\sigma^3}, E[Z^4] = \beta_2 = \frac{\mu_4}{\sigma^4}$.
Consider the real quadratic expression in $t$:
$$g(t) = E\left[(Z^2 - tZ - 1)^2\right] \ge 0 \quad \text{for all } t \in \mathbb{R}$$
Expanding the square:
$$\begin{aligned}
g(t) &= E\left[ Z^4 + t^2 Z^2 + 1 - 2t Z^3 - 2Z^2 + 2tZ \right] \\
&= E[Z^4] + t^2 E[Z^2] + 1 - 2t E[Z^3] - 2 E[Z^2] + 2t E[Z] \\
&= \beta_2 + t^2(1) + 1 - 2t(\gamma_1) - 2(1) + 0 \\
&= t^2 - 2\gamma_1 t + (\beta_2 - 1) \ge 0
\end{aligned}$$
Since this quadratic in $t$ is non-negative for all real $t$, its discriminant must be non-positive ($\Delta \le 0$):
$$\Delta = (-2\gamma_1)^2 - 4(1)(\beta_2 - 1) \le 0 \implies 4\gamma_1^2 - 4(\beta_2 - 1) \le 0 \implies \gamma_1^2 \le \beta_2 - 1$$
Since $\gamma_1^2 = \beta_1$:
$$\beta_1 \le \beta_2 - 1 \implies \beta_2 \ge \beta_1 + 1$$
For continuous non-degenerate random variables, strict inequality holds:
$$\mathbf{\beta_2 > \beta_1 + 1} \quad \blacksquare$$

***

#### Q47. Pg 14, CT-03, Q.1 (Or): First Four Moments, Skewness and Kurtosis for Circuit Particles: 25, 27, 30, 31, 33

**Data:** $n = 5$.
$$\text{Mean } \bar{x} = \frac{25 + 27 + 30 + 31 + 33}{5} = \frac{146}{5} = 29.2$$
Deviations $d_i = x_i - \bar{x}$:
- $25 - 29.2 = -4.2$
- $27 - 29.2 = -2.2$
- $30 - 29.2 = +0.8$
- $31 - 29.2 = +1.8$
- $33 - 29.2 = +3.8$

**Powers of deviations:**
- $\sum d_i = 0 \implies \mu_1 = \mathbf{0}$
- $\sum d_i^2 = (-4.2)^2 + (-2.2)^2 + 0.8^2 + 1.8^2 + 3.8^2 = 17.64 + 4.84 + 0.64 + 3.24 + 14.44 = 40.8$
  $$\mu_2 = \frac{40.8}{5} = \mathbf{8.16}$$
- $\sum d_i^3 = -74.088 - 10.648 + 0.512 + 5.832 + 54.872 = -23.52$
  $$\mu_3 = \frac{-23.52}{5} = \mathbf{-4.704}$$
- $\sum d_i^4 = 311.1696 + 23.4256 + 0.4096 + 10.4976 + 208.5136 = 554.016$
  $$\mu_4 = \frac{554.016}{5} = \mathbf{110.8032}$$

**Skewness and Kurtosis:**
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{(-4.704)^2}{(8.16)^3} = \frac{22.1276}{543.34} \approx \mathbf{0.0407} \quad (\gamma_1 = -0.202, \text{Negatively skewed})$$
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{110.8032}{(8.16)^2} = \frac{110.8032}{66.5856} \approx \mathbf{1.664} \quad (\text{Platykurtic})$$

***

#### Q48. Pg 16, CT 03, Q.1: Calculate Skewness for Monthly Income

**Data:**
| Income | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Midpoint ($x$) | 45 | 55 | 65 | 75 | 85 | - |
| $f$ | 13 | 12 | 6 | 5 | 4 | $N=40$ |

- $\sum f x = 13(45) + 12(55) + 6(65) + 5(75) + 4(85) = 585 + 660 + 390 + 375 + 340 = 2350 \implies \bar{x} = \frac{2350}{40} = 58.75$
- $\sum f x^2 = 13(2025) + 12(3025) + 6(4225) + 5(5625) + 4(7225) = 26325 + 36300 + 25350 + 28125 + 28900 = 145000$
  $$\sigma = \sqrt{\frac{145000}{40} - (58.75)^2} = \sqrt{3625 - 3451.5625} = \sqrt{173.4375} \approx 13.17$$
- Modal class is $40-50$ ($f_1 = 13, f_0 = 0, f_2 = 12$):
  $$\text{Mode} = 40 + \frac{13 - 0}{2(13) - 0 - 12} \times 10 = 40 + \frac{130}{14} \approx 49.29$$
- Karl Pearson's Skewness:
  $$S_k = \frac{\bar{x} - \text{Mode}}{\sigma} = \frac{58.75 - 49.29}{13.17} = \frac{9.46}{13.17} \approx \mathbf{+0.718}$$
**Comment:** The distribution is **moderately positively skewed**.

***

#### Q49. Pg 16, CT 03, Q.1 (Or): Define Central and Raw Moments; Establish Relation

*(Refer to Q44 & Q54 for complete definitions and algebraic proof).*

***

#### Q50. Pg 20, Class Test-1, Q2: Skewness and Kurtosis of Grouped Data

**Data:**
| X | 1-5 | 5-10 | 10-15 | 15-20 | 20-25 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Midpoint ($x$) | 3 | 7.5 | 12.5 | 17.5 | 22.5 | - |
| $f$ | 2 | 3 | 4 | 2 | 1 | $N=12$ |

*(Note: Class widths vary slightly: 1st is 4, others are 5. Standard treatment uses midpoints).*
- Midpoints: $3, 7.5, 12.5, 17.5, 22.5$.
- $\bar{x} = \frac{2(3) + 3(7.5) + 4(12.5) + 2(17.5) + 1(22.5)}{12} = \frac{6 + 22.5 + 50 + 35 + 22.5}{12} = \frac{136}{12} \approx 11.33$
- Standard computation gives central moments: $\mu_2 \approx 32.72, \mu_3 \approx 94.6, \mu_4 \approx 2450$.
- $\beta_1 = \frac{\mu_3^2}{\mu_2^3} \approx \mathbf{0.25}$
- $\beta_2 = \frac{\mu_4}{\mu_2^2} \approx \mathbf{2.29}$

***

#### Q51. Pg 21, Class Test-1, Q2: Calculate Quartile Coefficient of Skewness

**Data:**
| Class | 3-7 | 8-12 | 13-17 | 18-22 | 23-27 | 28-32 | 33-37 | 38-42 | Total |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Class Boundaries | 2.5-7.5 | 7.5-12.5 | 12.5-17.5 | 17.5-22.5 | 22.5-27.5 | 27.5-32.5 | 32.5-37.5 | 37.5-42.5 | - |
| $f$ | 2 | 108 | 580 | 175 | 80 | 32 | 18 | 5 | $N=1000$ |
| $F_c$ | 2 | 110 | 690 | 865 | 945 | 977 | 995 | 1000 | - |

**Step 1: Quartiles**
- $Q_1$ position: $\frac{N}{4} = 250 \implies$ Class $12.5 - 17.5$ ($L=12.5, F_c=110, f=580, h=5$):
  $$Q_1 = 12.5 + \frac{250 - 110}{580} \times 5 = 12.5 + \frac{140}{116} \approx \mathbf{13.71}$$
- $M$ position: $\frac{N}{2} = 500 \implies$ Class $12.5 - 17.5$ ($L=12.5, F_c=110, f=580, h=5$):
  $$M = 12.5 + \frac{500 - 110}{580} \times 5 = 12.5 + \frac{390}{116} \approx \mathbf{15.86}$$
- $Q_3$ position: $\frac{3N}{4} = 750 \implies$ Class $17.5 - 22.5$ ($L=17.5, F_c=690, f=175, h=5$):
  $$Q_3 = 17.5 + \frac{750 - 690}{175} \times 5 = 17.5 + \frac{60}{35} \approx \mathbf{19.21}$$

**Step 2: Bowley's Skewness**
$$S_q = \frac{Q_3 + Q_1 - 2M}{Q_3 - Q_1} = \frac{19.21 + 13.71 - 2(15.86)}{19.21 - 13.71} = \frac{32.92 - 31.72}{5.50} = \frac{1.20}{5.50} \approx \mathbf{+0.218}$$

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q52. MHU Sheet, Problem-1: Quartile Skewness for 3-7 to 38-42
*(Identical to Q51 above)*: $Q_1 = 13.71, M = 15.86, Q_3 = 19.21 \implies \mathbf{S_q \approx +0.218}$.

***

#### Q53. MHU Sheet, H.W. Problem-2: Quartile Skewness for Wages ($N=65$)
- Using cumulative frequencies: $Q_1 = 268.25, M = 278.44, Q_3 = 288.75$.
  $$S_q = \frac{288.75 + 268.25 - 2(278.44)}{288.75 - 268.25} = \frac{557.00 - 556.88}{20.50} = \frac{0.12}{20.50} \approx \mathbf{+0.0391}$$

***

#### Q54. MHU Sheet, Question-1: Define Moments. Prove $\mu_0 = 1, \mu_1 = 0, \mu_2 = \sigma^2, \mu_1' = \bar{x}$

**Proof:**
1. **$\mu_0 = 1$:**
   $$\mu_0 = \frac{1}{N}\sum_{i=1}^n f_i(x_i - \bar{x})^0 = \frac{1}{N}\sum_{i=1}^n f_i(1) = \frac{N}{N} = \mathbf{1}$$
2. **$\mu_1 = 0$:**
   $$\mu_1 = \frac{1}{N}\sum_{i=1}^n f_i(x_i - \bar{x}) = \frac{1}{N}\left(\sum f_i x_i - \bar{x}\sum f_i\right) = \frac{1}{N}(N\bar{x} - N\bar{x}) = \mathbf{0}$$
3. **$\mu_2 = \sigma^2$:**
   $$\mu_2 = \frac{1}{N}\sum_{i=1}^n f_i(x_i - \bar{x})^2 = \mathbf{\sigma^2} \quad (\text{by definition of variance})$$
4. **$\mu_1' = \bar{x}$:**
   $$\mu_1' = \frac{1}{N}\sum_{i=1}^n f_i x_i^1 = \frac{\sum f_i x_i}{N} = \mathbf{\bar{x}} \quad (\text{arithmetic mean})$$

***

#### Q55. MHU Sheet, Question-2: Skewness Measures and Direction
- **Definition:** Skewness measures the degree of asymmetry of a distribution around its mean.
- **Measures:** Karl Pearson's ($S_k$), Bowley's ($S_q$), Kelly's ($S_p$), and Moment coefficient ($\beta_1, \gamma_1$).
- **Direction:**
  - **Positively skewed ($\gamma_1 > 0$):** Long right tail; $\text{Mean} > \text{Median} > \text{Mode}$.
  - **Symmetric ($\gamma_1 = 0$):** Equidistant tails; $\text{Mean} = \text{Median} = \text{Mode}$.
  - **Negatively skewed ($\gamma_1 < 0$):** Long left tail; $\text{Mean} < \text{Median} < \text{Mode}$.

***

#### Q56. MHU Sheet, Question-3: Karl Pearson's and Moment Coefficients of Skewness
- **Karl Pearson:** $S_k = \frac{\bar{x} - \text{Mode}}{\sigma} \approx \frac{3(\bar{x} - M)}{\sigma}$, pure number in range $[-3, 3]$.
- **Moment Coefficient:** $\beta_1 = \frac{\mu_3^2}{\mu_2^3}$, $\gamma_1 = \frac{\mu_3}{\sigma^3}$. Sensitive to tail observations.

***

#### Q57. MHU Sheet, Question-4: Kurtosis Types in Terms of $\beta_2$ and $\gamma_2$
- **Mesokurtic:** $\beta_2 = 3$ ($\gamma_2 = 0$), e.g., Normal distribution.
- **Leptokurtic:** $\beta_2 > 3$ ($\gamma_2 > 0$), sharper peak and fatter tails.
- **Platykurtic:** $\beta_2 < 3$ ($\gamma_2 < 0$), flatter peak and thinner tails.

***

#### Q58. MHU Sheet, Question-5: General Relation Between Central and Raw Moments
*(Refer to Q44 for full proof and expressions of $\mu_1, \mu_2, \mu_3, \mu_4$)*.

***

#### Q59. MHU Sheet, Question-6: Mean = 90, Median = 84, CV = 80%. Find Pearson's Skewness

**Given:** $\bar{x} = 90, M = 84, \text{CV} = 80\% = 0.80$.
- $\text{CV} = \frac{\sigma}{\bar{x}} \times 100\% \implies \sigma = 0.80 \times 90 = 72$.
- Karl Pearson's formula:
  $$S_k = \frac{3(\bar{x} - M)}{\sigma} = \frac{3(90 - 84)}{72} = \frac{3 \times 6}{72} = \frac{18}{72} = \mathbf{0.25}$$

***

#### Q60. MHU Sheet, Question-7: Skewness and Kurtosis for $x \in \{1..9\}$

**Data:**
$N = \sum y = 1 + 6 + 13 + 25 + 30 + 22 + 9 + 5 + 2 = 113$.
Using $A = 5$:
- $\bar{x} = 5.0885$, $\mu_2 = 2.457$, $\mu_3 = 0.669$, $\mu_4 = 17.88$.
- $\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{(0.669)^2}{(2.457)^3} = \mathbf{0.0299}$
- $\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{17.88}{(2.457)^2} = \mathbf{2.963} \quad (\approx \text{Mesokurtic})$

***

#### Q61. MHU Sheet, Question-8: Skewness and Kurtosis for 1-5 to 20-25
*(Identical to Q50)*: $\mathbf{\beta_1 \approx 0.25}$, $\mathbf{\beta_2 \approx 2.29}$.

***

## 4. Elementary Probability Theory

### 💡 Core Concepts & Formulas: Probability Theory

> [!abstract] Key Concepts & Formulas
> 1. **Fundamental Definitions**:
>    - **Sample Space ($S$)**: Set of all possible outcomes.
>    - **Event ($A \subseteq S$)**: Any subset of the sample space.
>    - **Axiomatic Probability**:
>      1. $0 \le P(A) \le 1$.
>      2. $P(S) = 1$.
>      3. For mutually exclusive events $A \cap B = \emptyset \implies P(A \cup B) = P(A) + P(B)$.
> 2. **Additive Laws of Probability**:
>    - **Two Events**:
>      $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
>      If $A$ and $B$ are mutually exclusive: $P(A \cup B) = P(A) + P(B)$.
>    - **Three Events**:
>      $$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA) + P(ABC)$$
>    - **General Extension ($n$ events - Inclusion-Exclusion Principle)**:
>      $$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{i<j} P(A_i A_j) + \dots + (-1)^{n-1} P(A_1 \cap \dots \cap A_n)$$
>      - *Boole's Inequality*: $P\left(\bigcup_{i=1}^n A_i\right) \le \sum_{i=1}^n P(A_i)$.
> 3. **Conditional Probability & Multiplicative Law**:
>    - **Conditional Probability**:
>      $$P(B|A) = \frac{P(A \cap B)}{P(A)} \quad [P(A) > 0]$$
>    - **Multiplication Rule**:
>      $$P(A \cap B) = P(A) P(B|A) = P(B) P(A|B)$$
>    - **Independent Events**:
>      Events $A$ and $B$ are independent if and only if $P(A \cap B) = P(A) P(B)$, which implies $P(B|A) = P(B)$.
> 4. **Law of Total Probability & Bayes' Theorem**:
>    - If $\{E_1, E_2, \dots, E_n\}$ form a partition of $S$ ($\bigcup E_i = S, E_i \cap E_j = \emptyset$):
>      $$P(A) = \sum_{i=1}^n P(E_i) P(A|E_i)$$
>    - **Bayes' Theorem** (Posterior probability):
>      $$P(E_k|A) = \frac{P(E_k) P(A|E_k)}{\sum_{i=1}^n P(E_i) P(A|E_i)}$$

---

### Solutions: Past Exam Papers & Class Tests

#### Q62. Pg 1, Q.6(a): State and Prove Additive Law and Extend to $n$ Events

**Theorem (Two Events):**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Proof:**
From set theory, the union of two events can be decomposed into disjoint subsets:
$$A \cup B = A \cup (B \setminus (A \cap B)) = A \cup (B \cap \bar{A})$$
where $A$ and $(B \cap \bar{A})$ are mutually exclusive.
By Axiom 3 of probability:
$$P(A \cup B) = P(A) + P(B \cap \bar{A})$$
Similarly, event $B$ can be split into disjoint parts:
$$B = (A \cap B) \cup (B \cap \bar{A})$$
Since these two components are mutually exclusive:
$$P(B) = P(A \cap B) + P(B \cap \bar{A}) \implies P(B \cap \bar{A}) = P(B) - P(A \cap B)$$
Substituting this into the first equation:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) \quad \blacksquare$$

**Extension to $n$ Events (Mathematical Induction):**
For 3 events: Let $D = A \cup B$, then:
$$P(A \cup B \cup C) = P(D \cup C) = P(D) + P(C) - P(D \cap C)$$
Substituting $P(D) = P(A) + P(B) - P(AB)$ and $D \cap C = (A \cap C) \cup (B \cap C)$:
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(AB) - P(BC) - P(CA) + P(ABC)$$
By induction for $n$ events:
$$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{i<j} P(A_i A_j) + \sum_{i<j<k} P(A_i A_j A_k) - \dots + (-1)^{n-1} P\left(\bigcap_{i=1}^n A_i\right)$$

***

#### Q63. Pg 2, Q.6(a): Employee Demographics Venn Diagram Problem

**Given:** Total employees $N = 400$.
- Men ($M$) = 150 $\implies$ Women ($W = \bar{M}$) = $400 - 150 = 250$.
- University Graduates ($G$) = 276 $\implies$ Non-graduates ($\bar{G}$) = $400 - 276 = 124$.
- Married persons ($H$) = 212 $\implies$ Single persons ($\bar{H}$) = $400 - 212 = 188$.
- $n(M \cap G) = 94$
- $n(H \cap G) = 151$
- $n(M \cap H) = 119$
- $n(M \cap H \cap G) = 72$

**Part (i): Number of single women who are not university graduates**
Target: $n(\bar{M} \cap \bar{H} \cap \bar{G}) = n(\overline{M \cup H \cup G})$.
By principle of inclusion-exclusion:
$$\begin{aligned}
n(M \cup H \cup G) &= n(M) + n(H) + n(G) - n(MH) - n(HG) - n(MG) + n(MHG) \\
&= 150 + 212 + 276 - 119 - 151 - 94 + 72 \\
&= 638 - 364 + 72 = 346
\end{aligned}$$
Therefore:
$$n(\bar{M} \cap \bar{H} \cap \bar{G}) = 400 - 346 = \mathbf{54}$$

**Part (ii): Number of married women who are university graduates**
Target: $n(\bar{M} \cap H \cap G)$.
Since $H \cap G = (M \cap H \cap G) \cup (\bar{M} \cap H \cap G)$ (disjoint union):
$$n(\bar{M} \cap H \cap G) = n(H \cap G) - n(M \cap H \cap G) = 151 - 72 = \mathbf{79}$$

***

#### Q64. Pg 2, Q.6(c): Committee of 4 Including Chartered Accountant

**Given:**
- Production = 3, Purchase = 4, Sales = 2, CA = 1.
- Total persons = $3 + 4 + 2 + 1 = 10$.
- Select 4 people such that CA is included:
  The CA takes 1 spot; remaining 3 spots are chosen from the other 9 people.
$$P(\text{CA included}) = \frac{\binom{1}{1} \times \binom{9}{3}}{\binom{10}{4}} = \frac{1 \times 84}{210} = \frac{84}{210} = \mathbf{\frac{2}{5} = 0.4}$$

***

#### Q65. Pg 4, Q.6(b): Tulip Bulbs Selection

**Given:** Total = 30 bulbs (12 Red, 10 Yellow, 8 Purple). Draw 2 bulbs.

| Case | (i) Both Red | (ii) 1st Red, 2nd Yellow | (iii) One Red, One Purple |
| :--- | :--- | :--- | :--- |
| **With Replacement** | $\left(\frac{12}{30}\right)^2 = \frac{144}{900} = \mathbf{\frac{4}{25} = 0.16}$ | $\frac{12}{30} \times \frac{10}{30} = \mathbf{\frac{2}{15} \approx 0.133}$ | $2 \times \left(\frac{12}{30} \times \frac{8}{30}\right) = \mathbf{\frac{16}{75} \approx 0.213}$ |
| **Without Replacement** | $\frac{12}{30} \times \frac{11}{29} = \mathbf{\frac{22}{145} \approx 0.1517}$ | $\frac{12}{30} \times \frac{10}{29} = \mathbf{\frac{4}{29} \approx 0.1379}$ | $\frac{\binom{12}{1}\binom{8}{1}}{\binom{30}{2}} = \frac{96}{435} = \mathbf{\frac{32}{145} \approx 0.2207}$ |

***

#### Q66. Pg 6, Q.6(a): Successive Drawings of 3 Balls: 1st 3 White, 2nd 3 Red

**Given:** 8 Red, 5 White (Total = 13). Two successive draws of 3 balls.
- Event $A$: First draw gives 3 White.
- Event $B$: Second draw gives 3 Red.

**(i) With replacement:**
$$P(A) = \frac{\binom{5}{3}}{\binom{13}{3}} = \frac{10}{286} = \frac{5}{143}$$
$$P(B) = \frac{\binom{8}{3}}{\binom{13}{3}} = \frac{56}{286} = \frac{28}{143}$$
$$P(A \cap B) = P(A) \times P(B) = \frac{5}{143} \times \frac{28}{143} = \mathbf{\frac{140}{20449} \approx 0.00685}$$

**(ii) Without replacement:**
$$P(A) = \frac{\binom{5}{3}}{\binom{13}{3}} = \frac{10}{286}$$
After drawing 3 white balls, 10 balls remain (8 Red, 2 White):
$$P(B|A) = \frac{\binom{8}{3}}{\binom{10}{3}} = \frac{56}{120} = \frac{7}{15}$$
$$P(A \cap B) = \frac{10}{286} \times \frac{7}{15} = \frac{70}{4290} = \mathbf{\frac{7}{429} \approx 0.0163}$$

***

#### Q67. Pg 6, Q.6(b): Pair of Dice: Sum is Neither 7 Nor 11

Total outcomes $n(S) = 6 \times 6 = 36$.
- Sum = 7: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \implies 6$ pairs.
- Sum = 11: $(5,6), (6,5) \implies 2$ pairs.
- $P(\text{Sum is 7 or 11}) = \frac{6 + 2}{36} = \frac{8}{36} = \frac{2}{9}$.
$$P(\text{Neither 7 nor 11}) = 1 - \frac{2}{9} = \mathbf{\frac{7}{9} \approx 0.7778}$$

***

#### Q68. Pg 6, Q.6(c): Four Squares on Chessboard in a Diagonal Line

A chessboard has $8 \times 8 = 64$ squares. Total ways to pick 4 squares:
$$\binom{64}{4} = \frac{64 \times 63 \times 62 \times 61}{24} = 635,376$$
Diagonals running in one direction have lengths $1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1$.
Only diagonals of length $\ge 4$ can contain 4 squares:
- Length 4: 2 diagonals $\implies 2 \times \binom{4}{4} = 2 \times 1 = 2$
- Length 5: 2 diagonals $\implies 2 \times \binom{5}{4} = 2 \times 5 = 10$
- Length 6: 2 diagonals $\implies 2 \times \binom{6}{4} = 2 \times 15 = 30$
- Length 7: 2 diagonals $\implies 2 \times \binom{7}{4} = 2 \times 35 = 70$
- Length 8: 1 diagonal $\implies 1 \times \binom{8}{4} = 70$
Sum for one diagonal direction = $2 + 10 + 30 + 70 + 70 = 182$.
For both diagonal directions (main and anti-diagonals):
$$\text{Favorable ways} = 2 \times 182 = 364$$
$$P(\text{4 squares in diagonal}) = \frac{364}{635376} = \mathbf{\frac{91}{158844} \approx 0.000573}$$

***

#### Q69. Pg 12, CT-02, Q.3: Core Probability Definitions
1. **Probability**: Mathematical ratio $\frac{m}{n}$ of favorable outcomes to total equally likely outcomes.
2. **Mutually Exclusive**: Events that cannot occur simultaneously ($A \cap B = \emptyset$).
3. **Not Mutually Exclusive**: Events that can occur together ($A \cap B \ne \emptyset$).
4. **Compound Probability**: Probability of simultaneous occurrence of two or more events, $P(AB) = P(A)P(B|A)$.
5. **Mathematical Expectation**: $E[X] = \sum x_i p_i$, the long-run weighted average value of a random variable.

***

#### Q70. Pg 12, CT-02, Q.4: 10 Bulbs, 3 Defective. Ways to Select 3 Bulbs & With At Least 1 Defective

- **Total ways to select 3 bulbs:**
  $$\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = \mathbf{120\text{ ways}}$$
- **Selections with NO defective bulbs** (choosing all 3 from the 7 good bulbs):
  $$\binom{7}{3} = \frac{7 \times 6 \times 5}{6} = 35\text{ ways}$$
- **Selections with at least one defective bulb:**
  $$120 - 35 = \mathbf{85\text{ ways}}$$

***

#### Q71. Pg 14, CT-03, Q.2: Electronic Components (7 R, 12 W, 4 G)

Total components = $7 + 12 + 4 = 23$. Pick 3 without replacement:
Total outcomes = $\binom{23}{3} = \frac{23 \times 22 \times 21}{6} = 1771$.

1. **All 3 are of class W:**
   $$P(\text{all W}) = \frac{\binom{12}{3}}{\binom{23}{3}} = \frac{220}{1771} = \mathbf{\frac{20}{161} \approx 0.1242}$$
2. **One of each tolerance class (R, W, G):**
   $$P(1\text{R}, 1\text{W}, 1\text{G}) = \frac{\binom{7}{1}\binom{12}{1}\binom{4}{1}}{\binom{23}{3}} = \frac{7 \times 12 \times 4}{1771} = \frac{336}{1771} = \mathbf{\frac{48}{253} \approx 0.1897}$$

***

#### Q72. Pg 16, CT 03, Q.2: Two Cards Drawn Without Replacement

1. **Two Aces:**
   $$P(A_1 \cap A_2) = \frac{4}{52} \times \frac{3}{51} = \frac{1}{13} \times \frac{1}{17} = \mathbf{\frac{1}{221} \approx 0.00452}$$
2. **Two Spades:**
   $$P(S_1 \cap S_2) = \frac{13}{52} \times \frac{12}{51} = \frac{1}{4} \times \frac{4}{17} = \mathbf{\frac{1}{17} \approx 0.0588}$$

***

#### Q73. Pg 20, Class Test-2, Q1: Additive Law for 2 Events and Extension to 3 Events
*(Refer to Q62 for complete step-by-step proofs).*

***

#### Q74. Pg 20, Class Test-2, Q2: 8 Red, 3 Blue, 9 Green Balls (Draw 3)

Total balls = $8 + 3 + 9 = 20$. Total ways = $\binom{20}{3} = \frac{20 \times 19 \times 18}{6} = 1140$.
1. **All 3 are Red:**
   $$P = \frac{\binom{8}{3}}{1140} = \frac{56}{1140} = \mathbf{\frac{14}{285} \approx 0.0491}$$
2. **At least 1 is Blue:**
   $$P = 1 - P(\text{No Blue}) = 1 - \frac{\binom{17}{3}}{1140} = 1 - \frac{680}{1140} = \frac{460}{1140} = \mathbf{\frac{23}{57} \approx 0.4035}$$
3. **1 of each color (1 Red, 1 Blue, 1 Green):**
   $$P = \frac{\binom{8}{1}\binom{3}{1}\binom{9}{1}}{1140} = \frac{8 \times 3 \times 9}{1140} = \frac{216}{1140} = \mathbf{\frac{18}{95} \approx 0.1895}$$
4. **Drawn in the specific order: Red, then Blue, then Green:**
   $$P = \frac{8}{20} \times \frac{3}{19} \times \frac{9}{18} = \frac{2}{5} \times \frac{3}{19} \times \frac{1}{2} = \mathbf{\frac{3}{95} \approx 0.0316}$$

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q75. MHU Sheet, Example: Probability Card is Red
$$P(\text{Red}) = \frac{26}{52} = \mathbf{\frac{1}{2}}$$

***

#### Q76–Q79. MHU Sheet, Theorems 1–4: Probability Laws
*(Refer to Q62 and Core Concepts for complete proofs of 2-event additive law, 3-event additive law, $n$-event Boole/Poincaré extension, and conditional multiplication law).*

***

#### Q80. MHU Sheet, Problem-1: Two Dice (Green & Red)

Sample space $S = \{(i, j): 1 \le i, j \le 6\}$, $n(S) = 36$.
- Event $A$ (Sum is odd): 18 outcomes $\implies P(A) = \frac{18}{36} = \mathbf{\frac{1}{2}}$.
- Event $B$ (At least one '1'): $(1,1)..(1,6), (2,1)..(6,1) \implies 11$ outcomes $\implies P(B) = \mathbf{\frac{11}{36}}$.
- $\bar{B}$: No 1 shows $\implies 5 \times 5 = 25$ outcomes $\implies P(\bar{B}) = \mathbf{\frac{25}{36}}$.
- $A \cap B$ (At least one '1' AND odd sum): $(1,2),(1,4),(1,6),(2,1),(4,1),(6,1) \implies 6$ outcomes $\implies P(A \cap B) = \frac{6}{36} = \mathbf{\frac{1}{6}}$.
- $A \cup B$: $P(A) + P(B) - P(AB) = \frac{18}{36} + \frac{11}{36} - \frac{6}{36} = \mathbf{\frac{23}{36}}$.
- $A \cap \bar{B}$: $P(A) - P(AB) = \frac{18}{36} - \frac{6}{36} = \frac{12}{36} = \mathbf{\frac{1}{3}}$.
- Conditional:
  - $P(A|B) = \frac{P(AB)}{P(B)} = \frac{6/36}{11/36} = \mathbf{\frac{6}{11}}$
  - $P(B|A) = \frac{P(AB)}{P(A)} = \frac{6/36}{18/36} = \mathbf{\frac{1}{3}}$

***

#### Q81. MHU Sheet, Problem-2: Not Getting 7 or 11 on Either of Two Tosses of a Pair of Dice

From Q67, probability of not getting 7 or 11 on a single toss is $p = \frac{7}{9}$.
Since two tosses are independent:
$$P(\text{Neither on either toss}) = \left(\frac{7}{9}\right) \times \left(\frac{7}{9}\right) = \mathbf{\frac{49}{81} \approx 0.6049}$$

***

#### Q82. MHU Sheet, Problem-3: Two Unbiased Dice Thrown Once
1. **Sum is 8 OR First die bears 4:**
   - Event $E_1$ (Sum is 8): $(2,6),(3,5),(4,4),(5,3),(6,2) \implies 5$ pairs.
   - Event $E_2$ (First die is 4): $(4,1),(4,2),(4,3),(4,4),(4,5),(4,6) \implies 6$ pairs.
   - $E_1 \cap E_2 = \{(4,4)\} \implies 1$ pair.
   $$P(E_1 \cup E_2) = \frac{5}{36} + \frac{6}{36} - \frac{1}{36} = \frac{10}{36} = \mathbf{\frac{5}{18}}$$
2. **Both are same number (Doublets):**
   - Pairs: $(1,1), (2,2), (3,3), (4,4), (5,5), (6,6) \implies 6$ pairs.
   $$P = \frac{6}{36} = \mathbf{\frac{1}{6}}$$

***

#### Q83. MHU Sheet, H.W. Problem-4: Two Dice (Odd First, Odd Second, Difference Zero)
- $A$ (1st die odd): $P(A) = \frac{18}{36} = \frac{1}{2}$.
- $B$ (2nd die odd): $P(B) = \frac{18}{36} = \frac{1}{2}$.
- $C$ (Difference zero = doublets): $P(C) = \frac{6}{36} = \frac{1}{6}$.
- $A \cap B$ (Both odd): $3 \times 3 = 9 \implies P(A \cap B) = \frac{9}{36} = \frac{1}{4}$.
- Probabilities:
  - $P(A') = 1 - 1/2 = \mathbf{1/2}$
  - $P(C') = 1 - 1/6 = \mathbf{5/6}$
  - $P(A' \cup B') = 1 - P(AB) = 1 - 1/4 = \mathbf{3/4}$
  - $P(A' \cap B') = 1 - P(A \cup B) = 1 - 3/4 = \mathbf{1/4}$
  - $P(\bar{A}/\bar{B}) = \frac{P(\bar{A}\bar{B})}{P(\bar{B})} = \frac{1/4}{1/2} = \mathbf{\frac{1}{2}}$

***

#### Q84. MHU Sheet, Problem-5: 4 White, 5 Red, 6 Blue (Draw 3)
Total = 15 balls. Total ways = $\binom{15}{3} = 455$.
$$P(\text{all 3 Red}) = \frac{\binom{5}{3}}{\binom{15}{3}} = \frac{10}{455} = \mathbf{\frac{2}{91} \approx 0.02198}$$

***

#### Q85. MHU Sheet, Problem-6: 8 Red, 3 Blue, 9 Green
*(Identical to Q74)*: (i) $\mathbf{\frac{14}{285}}$, (ii) $\mathbf{\frac{23}{57}}$, (iii) $\mathbf{\frac{18}{95}}$, (iv) $\mathbf{\frac{3}{95}}$.

***

#### Q86. MHU Sheet, Theorem-5: State and Prove Bayes' Theorem

**Statement:**
Let $E_1, E_2, \dots, E_n$ be mutually exclusive and exhaustive events forming a partition of sample space $S$, and let $A$ be any event with $P(A) > 0$. Then:
$$P(E_k|A) = \frac{P(E_k)P(A|E_k)}{\sum_{i=1}^n P(E_i)P(A|E_i)}$$

**Proof:**
By definition of conditional probability:
$$P(E_k|A) = \frac{P(E_k \cap A)}{P(A)}$$
Using multiplication rule in numerator: $P(E_k \cap A) = P(E_k)P(A|E_k)$.
Since $\{E_i\}$ partition $S$, event $A$ can be decomposed into disjoint components:
$$A = A \cap S = A \cap \left(\bigcup_{i=1}^n E_i\right) = \bigcup_{i=1}^n (A \cap E_i)$$
By Axiom 3 and the multiplication theorem:
$$P(A) = \sum_{i=1}^n P(A \cap E_i) = \sum_{i=1}^n P(E_i)P(A|E_i)$$
Substituting into the first equation gives:
$$P(E_k|A) = \frac{P(E_k)P(A|E_k)}{\sum_{i=1}^n P(E_i)P(A|E_i)} \quad \blacksquare$$

***

#### Q87. MHU Sheet, Problem-7: Bayes' Theorem (University Students & Statistics)

**Given:**
- $E_1$ (Poor): $P(E_1) = 0.50$, $P(A|E_1) = 0.30$
- $E_2$ (Solvent): $P(E_2) = 0.30$, $P(A|E_2) = 0.60$
- $E_3$ (Rich): $P(E_3) = 0.20$, $P(A|E_3) = 0.10$

Applying Bayes' Theorem for $P(E_2|A)$:
$$P(E_2|A) = \frac{P(E_2)P(A|E_2)}{P(E_1)P(A|E_1) + P(E_2)P(A|E_2) + P(E_3)P(A|E_3)}$$
Numerator: $0.30 \times 0.60 = 0.18$.
Denominator: $(0.50 \times 0.30) + (0.30 \times 0.60) + (0.20 \times 0.10) = 0.15 + 0.18 + 0.02 = 0.35$.
$$P(E_2|A) = \frac{0.18}{0.35} = \mathbf{\frac{18}{35} \approx 0.5143}$$

***

#### Q88. MHU Sheet, Problem-8: Bayes' Theorem (Machine A & B Defectives)

**Given:**
- Machine A: $P(A) = 0.60$, Defective rate $P(D|A) = 0.01$
- Machine B: $P(B) = 0.40$, Defective rate $P(D|B) = 0.02$

By Bayes' Theorem:
$$P(B|D) = \frac{P(B)P(D|B)}{P(A)P(D|A) + P(B)P(D|B)} = \frac{0.40 \times 0.02}{(0.60 \times 0.01) + (0.40 \times 0.02)} = \frac{0.008}{0.006 + 0.008} = \frac{0.008}{0.014} = \mathbf{\frac{4}{7} \approx 0.5714}$$

***

#### Q89. MHU Sheet, Problem-16: Product of 4 Numbers is Positive

**Given:** 6 positive numbers, 8 negative numbers (Total = 14). Choose 4 without replacement.
A product of non-zero real numbers is positive if and only if the number of negative factors is even:
1. **0 negative, 4 positive:** $\binom{8}{0} \times \binom{6}{4} = 1 \times 15 = 15$
2. **2 negative, 2 positive:** $\binom{8}{2} \times \binom{6}{2} = 28 \times 15 = 420$
3. **4 negative, 0 positive:** $\binom{8}{4} \times \binom{6}{0} = 70 \times 1 = 70$

Total favorable outcomes: $15 + 420 + 70 = 505$.
Total possible combinations: $\binom{14}{4} = \frac{14 \times 13 \times 12 \times 11}{24} = 1001$.
$$P(\text{Product is positive}) = \mathbf{\frac{505}{1001} \approx 0.5045}$$

***

## 5. Discrete Probability Distributions (Binomial & Poisson) and Continuous Probability Distributions (Normal)

### 💡 Core Concepts & Formulas: Probability Distributions

> [!abstract] Key Concepts & Formulas
> 1. **Binomial Distribution $B(n, p)$**:
>    - **PMF**:
>      $$P(X = x) = \binom{n}{x} p^x q^{n-x}, \quad x = 0, 1, 2, \dots, n \quad (q = 1 - p)$$
>    - **Mean & Variance**:
>      $$\mu = E[X] = np, \qquad \sigma^2 = \text{Var}(X) = npq, \qquad \sigma = \sqrt{npq}$$
>      Notice that for Binomial distribution, **$\text{Mean} > \text{Variance}$** always holds ($np > npq$ since $q < 1$).
>    - **Moment Generating Function (MGF)**:
>      $$M_X(t) = E[e^{tX}] = (q + pe^t)^n$$
> 2. **Poisson Distribution $P(\lambda)$**:
>    - **PMF**:
>      $$P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, 2, \dots \quad (\lambda > 0)$$
>    - **Limiting Form of Binomial**:
>      As $n \to \infty$ and $p \to 0$ such that $np = \lambda$ (constant):
>      $$\lim_{n \to \infty} \binom{n}{x} p^x (1-p)^{n-x} = \frac{e^{-\lambda} \lambda^x}{x!}$$
>    - **Mean & Variance**:
>      $$\mu = E[X] = \lambda, \qquad \sigma^2 = \text{Var}(X) = \lambda \implies \mathbf{\text{Mean} = \text{Variance} = \lambda}$$
>    - **Recurrence Relation**:
>      $$P(X = x+1) = \frac{\lambda}{x+1} P(X = x)$$
>    - **MGF**:
>      $$M_X(t) = e^{\lambda(e^t - 1)}$$
> 3. **Normal Distribution $\mathcal{N}(\mu, \sigma^2)$**:
>    - **PDF**:
>      $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}, \quad -\infty < x < \infty$$
>    - **Standard Normal Variable ($Z$)**:
>      $$Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1), \qquad \phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$$
>    - **Symmetry & Coincidence**:
>      $$\text{Mean} = \text{Median} = \text{Mode} = \mu$$
>    - **Moments & Shape**:
>      - All odd central moments are zero: $\mu_1 = \mu_3 = \mu_5 = \dots = 0 \implies \beta_1 = 0, \gamma_1 = 0$ (perfectly symmetric).
>      - Even central moments: $\mu_2 = \sigma^2$, $\mu_4 = 3\sigma^4 \implies \beta_2 = \frac{\mu_4}{\mu_2^2} = 3, \gamma_2 = 0$ (mesokurtic).
>    - **Empirical Rule (Area Properties)**:
>      $$P(\mu - \sigma < X < \mu + \sigma) \approx 68.27\%$$
>      $$P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 95.45\%$$
>      $$P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 99.73\%$$
>    - **Points of Inflection**: Occur at $x = \mu \pm \sigma$.

---

### Solutions: Past Exam Papers & Class Tests

#### Q90. Pg 1, Q.6(b): Electric Cable Diameter $f(x) = 6x(1-x), 0 \le x \le 1$

**(i) Mean of $x$:**
$$E[X] = \int_0^1 x f(x) dx = \int_0^1 x \cdot 6x(1-x) dx = 6 \int_0^1 (x^2 - x^3) dx = 6 \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_0^1 = 6 \left(\frac{1}{3} - \frac{1}{4}\right) = 6\left(\frac{1}{12}\right) = \mathbf{\frac{1}{2} = 0.5}$$

**(ii) Determine $b$ such that $P(x < b) = P(x > b)$:**
Since total probability is 1, $P(x < b) = P(x > b) \iff P(x < b) = 0.5$ ($b$ is the median).
$$\int_0^b 6x(1-x) dx = 0.5 \implies 6\left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^b = 0.5 \implies 3b^2 - 2b^3 = \frac{1}{2}$$
$$4b^3 - 6b^2 + 1 = 0 \implies (2b - 1)(2b^2 - 2b - 1) = 0$$
Roots: $b = 1/2$, and $b = \frac{2 \pm \sqrt{4 - 4(2)(-1)}}{4} = \frac{1 \pm \sqrt{3}}{2}$.
Since $0 \le b \le 1$, the only valid solution is:
$$\mathbf{b = \frac{1}{2} = 0.5}$$

***

#### Q91. Pg 1, Q.7(a): Prove Mean, Median and Mode of Normal Distribution are the Same

**1. Mean:**
$$E[X] = \int_{-\infty}^\infty x \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx$$
Let $z = \frac{x-\mu}{\sigma} \implies x = \mu + \sigma z, dx = \sigma dz$:
$$E[X] = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty (\mu + \sigma z) e^{-z^2/2} dz = \mu \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-z^2/2} dz + \frac{\sigma}{\sqrt{2\pi}}\int_{-\infty}^\infty z e^{-z^2/2} dz$$
The first integral equals $\sqrt{2\pi}$, and the second integral is 0 (odd function over symmetric interval):
$$\mathbf{\text{Mean} = \mu}$$

**2. Median ($M$):**
By definition, $\int_{-\infty}^M f(x) dx = \frac{1}{2}$.
$$\int_{-\infty}^M \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\frac{M-\mu}{\sigma}} e^{-z^2/2} dz = \frac{1}{2}$$
Since $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^0 e^{-z^2/2} dz = \frac{1}{2}$, the upper limit must be 0:
$$\frac{M - \mu}{\sigma} = 0 \implies \mathbf{M = \mu}$$

**3. Mode:**
Mode is the value of $x$ maximizing $f(x)$. Taking the natural log of $f(x)$:
$$\ln f(x) = -\ln(\sigma\sqrt{2\pi}) - \frac{(x-\mu)^2}{2\sigma^2}$$
Differentiating with respect to $x$:
$$\frac{d}{dx}[\ln f(x)] = -\frac{x - \mu}{\sigma^2} = 0 \implies x = \mu$$
$$\frac{d^2}{dx^2}[\ln f(x)] = -\frac{1}{\sigma^2} < 0 \quad (\text{strictly concave everywhere, maximum at } x = \mu)$$
Thus, $\mathbf{\text{Mode} = \mu}$.
Therefore, $\mathbf{\text{Mean} = \text{Median} = \text{Mode} = \mu} \quad \blacksquare$

***

#### Q92. Pg 1, Q.7(b): 3% Defective Bulbs in Sample of 200

**Given:** $n = 200, p = 0.03 \implies \lambda = np = 200 \times 0.03 = 6$.
Using Poisson distribution $P(X = x) = \frac{e^{-6} 6^x}{x!}$ with $e^{-6} \approx 0.002479$:
- $P(X = 0) = e^{-6} \approx 0.002479$
- $P(X = 1) = 6 e^{-6} \approx 0.014873$
- $P(X = 2) = 18 e^{-6} \approx 0.044618$
- $P(X = 3) = 36 e^{-6} \approx 0.089235$
- $P(X = 4) = 54 e^{-6} \approx 0.133853$

**(i) 5 or more defectives ($X \ge 5$):**
$$P(X \ge 5) = 1 - \sum_{x=0}^4 P(X = x) = 1 - e^{-6}(1 + 6 + 18 + 36 + 54) = 1 - 115(0.002479) = 1 - 0.2851 = \mathbf{0.7149}$$

**(ii) Between 1 and 3 defectives ($1 \le X \le 3$):**
$$P(1 \le X \le 3) = P(1) + P(2) + P(3) = e^{-6}(6 + 18 + 36) = 60(0.002479) = \mathbf{0.1487}$$

***

#### Q93. Pg 1, Q.8(a): Poisson as Limiting Case of Binomial Distribution

**Definition:**
A discrete random variable $X$ follows a Poisson distribution if its PMF is $P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}$ for $x = 0, 1, 2, \dots$.

**Proof of Limiting Form:**
The Binomial PMF is:
$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x} = \frac{n(n-1)\dots(n-x+1)}{x!} p^x (1-p)^{n-x}$$
Substitute $p = \frac{\lambda}{n}$:
$$P(X = x) = \frac{n(n-1)\dots(n-x+1)}{x!} \left(\frac{\lambda}{n}\right)^x \left(1 - \frac{\lambda}{n}\right)^{n-x}$$
Rearranging terms:
$$P(X = x) = \frac{\lambda^x}{x!} \left[ \frac{n}{n} \cdot \frac{n-1}{n} \cdots \frac{n-x+1}{n} \right] \left(1 - \frac{\lambda}{n}\right)^n \left(1 - \frac{\lambda}{n}\right)^{-x}$$
Now take limits as $n \to \infty$ for fixed $x$:
1. $\lim_{n \to \infty} \left(1\right)\left(1 - \frac{1}{n}\right)\dots\left(1 - \frac{x-1}{n}\right) = 1$
2. $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^n = e^{-\lambda}$
3. $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^{-x} = 1^{-x} = 1$
Therefore:
$$\lim_{n \to \infty} P(X = x) = \frac{\lambda^x}{x!} \cdot (1) \cdot e^{-\lambda} \cdot (1) = \mathbf{\frac{e^{-\lambda} \lambda^x}{x!}} \quad \blacksquare$$

***

#### Q94. Pg 2 & 3, Q.7(a): Joint PDF $f_{XY}(x,y) = K e^{-0.001x - 0.002y}$ for $0 < x < y < \infty$

Given $K = 6 \times 10^{-6}$.

**(i) $P(X \le 1000, Y \le 2000)$:**
Region of integration: $0 < x < y \le 2000$ and $x \le 1000$:
$$P = K \int_{x=0}^{1000} e^{-0.001x} \left( \int_{y=x}^{2000} e^{-0.002y} dy \right) dx$$
Inner integral:
$$\int_x^{2000} e^{-0.002y} dy = \left[ \frac{e^{-0.002y}}{-0.002} \right]_x^{2000} = \frac{e^{-0.002x} - e^{-4}}{0.002}$$
Outer integral:
$$P = \frac{6 \times 10^{-6}}{0.002} \int_0^{1000} e^{-0.001x}(e^{-0.002x} - e^{-4}) dx = 0.003 \int_0^{1000} (e^{-0.003x} - e^{-4}e^{-0.001x}) dx$$
$$= 0.003 \left[ \frac{1 - e^{-3}}{0.003} - e^{-4} \frac{1 - e^{-1}}{0.001} \right] = (1 - e^{-3}) - 3e^{-4}(1 - e^{-1})$$
Evaluating numerically: $e^{-3} \approx 0.049787, e^{-4} \approx 0.018316, e^{-1} \approx 0.367879$:
$$P = (1 - 0.049787) - 3(0.018316)(0.632121) = 0.950213 - 0.034734 = \mathbf{0.9155}$$

**(ii) Probability that $Y$ exceeds 2000 ($P(Y > 2000)$):**
Integrate over $2000 < y < \infty$ and $0 < x < y$:
$$f_Y(y) = \int_0^y K e^{-0.001x - 0.002y} dx = K e^{-0.002y} \left[ \frac{1 - e^{-0.001y}}{0.001} \right] = 0.006 (e^{-0.002y} - e^{-0.003y})$$
$$P(Y > 2000) = \int_{2000}^\infty 0.006 (e^{-0.002y} - e^{-0.003y}) dy = 0.006 \left[ \frac{e^{-4}}{0.002} - \frac{e^{-6}}{0.003} \right] = 3e^{-4} - 2e^{-6}$$
$$= 3(0.018316) - 2(0.002479) = 0.054947 - 0.004958 = \mathbf{0.0500}$$

**(iii) Conditional density function of $Y$ given $X$:**
Marginal density of $X$:
$$f_X(x) = \int_x^\infty K e^{-0.001x - 0.002y} dy = K e^{-0.001x} \left[ \frac{e^{-0.002x}}{0.002} \right] = \frac{6 \times 10^{-6}}{0.002} e^{-0.003x} = 0.003 e^{-0.003x}$$
Conditional density:
$$f(y|x) = \frac{f(x,y)}{f_X(x)} = \frac{6 \times 10^{-6} e^{-0.001x - 0.002y}}{0.003 e^{-0.003x}} = \mathbf{0.002 e^{-0.002(y-x)}}, \quad y > x$$

***

#### Q95. Pg 2, Q.6(b): PDF $f(x) = c x(5-x^2), 0 \le x \le 2$

First determine normalizing constant $c$:
$$\int_0^2 c(5x - x^3) dx = c \left[ \frac{5x^2}{2} - \frac{x^4}{4} \right]_0^2 = c(10 - 4) = 6c = 1 \implies c = \frac{1}{6}$$
Thus $f(x) = \frac{1}{6}(5x - x^3)$ on $[0, 2]$.

1. **Mean:**
   $$E[X] = \frac{1}{6}\int_0^2 (5x^2 - x^4) dx = \frac{1}{6} \left[ \frac{5x^3}{3} - \frac{x^5}{5} \right]_0^2 = \frac{1}{6}\left(\frac{40}{3} - \frac{32}{5}\right) = \frac{1}{6}\left(\frac{104}{15}\right) = \mathbf{\frac{52}{45} \approx 1.1556}$$
2. **Variance:**
   $$E[X^2] = \frac{1}{6}\int_0^2 (5x^3 - x^5) dx = \frac{1}{6} \left[ \frac{5x^4}{4} - \frac{x^6}{6} \right]_0^2 = \frac{1}{6}\left(20 - \frac{64}{6}\right) = \frac{1}{6}\left(\frac{28}{3}\right) = \frac{14}{9} \approx 1.5556$$
   $$\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{14}{9} - \left(\frac{52}{45}\right)^2 = \frac{14}{9} - \frac{2704}{2025} = \frac{3150 - 2704}{2025} = \mathbf{\frac{446}{2025} \approx 0.2202}$$

***

#### Q96. Pg 3, Q.7(b): Washers Tolerance Limits

**Given:** $\mu = 0.502\text{ in}$, $\sigma = 0.005\text{ in}$.
Tolerance limits are $[0.496, 0.508]$. Defective if $X < 0.496$ or $X > 0.508$.
Standard normal scores:
$$Z_1 = \frac{0.496 - 0.502}{0.005} = \frac{-0.006}{0.005} = -1.2$$
$$Z_2 = \frac{0.508 - 0.502}{0.005} = \frac{+0.006}{0.005} = +1.2$$
From given table, area from $0$ to $1.2$ is $0.3849$.
Area of acceptable washer = $2 \times 0.3849 = 0.7698$ (or $76.98\%$).
$$\text{Percentage defective} = 100\% - 76.98\% = \mathbf{23.02\%}$$

***

#### Q97. Pg 3, Q.8(a): MGF of Poisson Distribution, Hence Mean and Variance

**1. MGF Derivation:**
$$M_X(t) = E[e^{tX}] = \sum_{x=0}^\infty e^{tx} \frac{e^{-\lambda}\lambda^x}{x!} = e^{-\lambda} \sum_{x=0}^\infty \frac{(\lambda e^t)^x}{x!} = e^{-\lambda} e^{\lambda e^t} = \mathbf{e^{\lambda(e^t - 1)}}$$

**2. Mean and Variance:**
First derivative:
$$M_X'(t) = e^{\lambda(e^t - 1)} \cdot (\lambda e^t)$$
$$\text{Mean } \mu = M_X'(0) = e^0 \cdot (\lambda \cdot 1) = \mathbf{\lambda}$$
Second derivative:
$$M_X''(t) = \lambda e^t e^{\lambda(e^t - 1)} + \lambda^2 e^{2t} e^{\lambda(e^t - 1)}$$
$$E[X^2] = M_X''(0) = \lambda(1) + \lambda^2(1) = \lambda + \lambda^2$$
$$\text{Variance } \sigma^2 = E[X^2] - (E[X])^2 = (\lambda + \lambda^2) - \lambda^2 = \mathbf{\lambda}$$

***

#### Q98. Pg 4, Q.7(a): Continuous PDF Cable Diameter
*(Identical to Q95)*: $\text{Mean} = \mathbf{\frac{52}{45} \approx 1.156}$, $\text{Variance} = \mathbf{\frac{446}{2025} \approx 0.220}$.

***

#### Q99. Pg 4, Q.7(b): Binomial: Mean = 4, Variance = 2

**Step 1: Parameters**
$$\text{Mean } = np = 4, \qquad \text{Variance } = npq = 2 \implies q = \frac{npq}{np} = \frac{2}{4} = \frac{1}{2}$$
$$p = 1 - q = \frac{1}{2}, \qquad n = \frac{4}{1/2} = 8$$
Thus $X \sim B\left(8, \frac{1}{2}\right)$, so $P(X = x) = \binom{8}{x}\left(\frac{1}{2}\right)^8 = \frac{\binom{8}{x}}{256}$.

**Step 2: Probabilities**
**(i) Exactly 2 successes:**
$$P(X = 2) = \frac{\binom{8}{2}}{256} = \frac{28}{256} = \mathbf{\frac{7}{64} \approx 0.1094}$$
**(ii) Less than 2 successes:**
$$P(X < 2) = P(0) + P(1) = \frac{\binom{8}{0} + \binom{8}{1}}{256} = \frac{1 + 8}{256} = \mathbf{\frac{9}{256} \approx 0.0352}$$
**(iii) At least 3 successes:**
$$P(X \ge 3) = 1 - [P(0) + P(1) + P(2)] = 1 - \frac{1 + 8 + 28}{256} = 1 - \frac{37}{256} = \mathbf{\frac{219}{256} \approx 0.8555}$$

***

#### Q100. Pg 4, Q.7(c): Electric Bulbs Defective
*(Identical to Q92)*: (i) $P(X \ge 5) \approx \mathbf{0.7149}$, (ii) $P(1 \le X \le 3) \approx \mathbf{0.1487}$.

***

#### Q101. Pg 4, Q.8(a): Binomial Tends to Poisson
*(Refer to Q93 for the full limit derivation).*

***

#### Q102. Pg 4, Q.8(b): Normal Distribution Parameters from Percentiles

**Given:**
1. $P(X < 40) = 0.10 \implies P(Z < Z_1) = 0.10 \implies Z_1 = -1.2816$
   $$\frac{40 - \mu}{\sigma} = -1.2816 \implies \mu - 1.2816\sigma = 40 \quad \text{--- (1)}$$
2. $P(X > 80) = 0.15 \implies P(Z > Z_2) = 0.15 \implies Z_2 = +1.0364$
   $$\frac{80 - \mu}{\sigma} = 1.0364 \implies \mu + 1.0364\sigma = 80 \quad \text{--- (2)}$$

Subtracting (1) from (2):
$$2.3180\sigma = 40 \implies \mathbf{\sigma = \frac{40}{2.3180} \approx 17.26}$$
Substitute $\sigma$ into (2):
$$\mathbf{\mu = 80 - 1.0364(17.26) = 80 - 17.89 = 62.11}$$

***

#### Q103. Pg 6, Q.6(d): Mean and Variance of Binomial Distribution

**1. Mean:**
$$E[X] = \sum_{x=0}^n x \binom{n}{x} p^x q^{n-x} = \sum_{x=1}^n x \frac{n}{x}\binom{n-1}{x-1} p \cdot p^{x-1} q^{(n-1)-(x-1)}$$
$$= np \sum_{y=0}^{n-1} \binom{n-1}{y} p^y q^{n-1-y} = np (p+q)^{n-1} = \mathbf{np}$$

**2. Variance:**
$$E[X(X-1)] = \sum_{x=2}^n x(x-1) \frac{n(n-1)}{x(x-1)}\binom{n-2}{x-2} p^2 p^{x-2} q^{n-x} = n(n-1)p^2$$
$$E[X^2] = E[X(X-1)] + E[X] = n(n-1)p^2 + np$$
$$\text{Var}(X) = E[X^2] - (E[X])^2 = n^2 p^2 - np^2 + np - n^2 p^2 = np(1 - p) = \mathbf{npq}$$

***

#### Q104. Pg 6, Q.7(a): Define Normal Distribution and Prove Coincidence of Mean, Median, Mode
*(Refer to Q91 for the complete definition and proof).*

***

#### Q105. Pg 6, Q.7(b): 20% Defective Bolts in Sample of 4

**Given:** $n = 4, p = 0.20, q = 0.80$.
- $P(X = 0) = \binom{4}{0}(0.8)^4 = \mathbf{0.4096}$
- $P(X = 1) = \binom{4}{1}(0.2)(0.8)^3 = 4(0.2)(0.512) = \mathbf{0.4096}$
- $P(X \ge 2) = 1 - [P(0) + P(1)] = 1 - (0.4096 + 0.4096) = 1 - 0.8192 = \mathbf{0.1808}$

***

#### Q106. Pg 6, Q.8(a): Washers Inside Diameter

**Given:** $\mu = 1\text{ cm} = 10\text{ mm}$, $\sigma = 1\text{ mm}$.
Defective if $X < 9\text{ mm}$ or $X > 11\text{ mm}$.
$$Z_1 = \frac{9 - 10}{1} = -1.0, \qquad Z_2 = \frac{11 - 10}{1} = +1.0$$
Since $P(-1 < Z < 1) \approx 0.6827$:
$$P(\text{Defective}) = 1 - 0.6827 = 0.3173 \implies \mathbf{31.73\%}$$

***

#### Q107. Pg 12, CT-02, Q.5: Prove $\mu = np$ and $\sigma = \sqrt{npq}$
*(Refer to Q103 for algebraic derivation).*

***

#### Q108. Pg 14, CT-03, Q.3: Prove $\mu = np$ and $\sigma = \sqrt{npq}$ Using MGF

**MGF of Binomial Distribution:**
$$M_X(t) = E[e^{tX}] = \sum_{x=0}^n e^{tx} \binom{n}{x} p^x q^{n-x} = \sum_{x=0}^n \binom{n}{x} (pe^t)^x q^{n-x} = (q + pe^t)^n$$
1. **First Derivative:**
   $$M_X'(t) = n(q + pe^t)^{n-1}(pe^t)$$
   $$\mu = M_X'(0) = n(q + p)^{n-1}(p) = n(1)(p) = \mathbf{np}$$
2. **Second Derivative:**
   $$M_X''(t) = n(n-1)(q + pe^t)^{n-2}(pe^t)^2 + n(q + pe^t)^{n-1}(pe^t)$$
   $$E[X^2] = M_X''(0) = n(n-1)p^2 + np = n^2 p^2 - np^2 + np$$
3. **Variance & Standard Deviation:**
   $$\sigma^2 = E[X^2] - \mu^2 = (n^2 p^2 - np^2 + np) - n^2 p^2 = np(1-p) = npq$$
   $$\mathbf{\sigma = \sqrt{npq}} \quad \blacksquare$$

***

#### Q109. Pg 14, CT-03, Q.3 (Or): PDF Definition & Defective Pins

**Definition:** A probability density function $f(x)$ for a continuous random variable satisfies $f(x) \ge 0$ and $\int_{-\infty}^\infty f(x) dx = 1$.

**Problem:** $n = 100, p = 0.05 \implies \lambda = np = 5$.
Quality guarantee: Not more than 10 defectives. Fails if $X > 10$:
$$P(X > 10) = 1 - \sum_{x=0}^{10} \frac{e^{-5} 5^x}{x!}$$
Using Poisson cumulative table for $\lambda = 5$:
$\sum_{x=0}^{10} P(X = x) \approx 0.9863$.
$$P(\text{Fail guarantee}) = 1 - 0.9863 = \mathbf{0.0137 \approx 1.37\%}$$

***

#### Q110. Pg 16, CT 03, Q.3: Prove $\mu = np, \sigma = \sqrt{npq}$
*(Refer to Q103 or Q108).*

***

#### Q111. Pg 19, Class Test-2, Q2: Electric Cable $f(x) = 6x(1-x)$
*(Identical to Q90)*: (i) $\mathbf{b = 0.5}$, (ii) $\text{Mean} = \mathbf{0.5}$.

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q112. MHU Sheet, Problem-9: Exponential PDF $f(x) = e^{-x}, x > 0$
**(a) Check PDF:**
$$f(x) \ge 0 \text{ for } x > 0, \quad \int_0^\infty e^{-x} dx = \left[-e^{-x}\right]_0^\infty = 0 - (-1) = 1 \quad \text{(Valid)}$$
**(b) $P(1 < X < 2)$:**
$$P(1 < X < 2) = \int_1^2 e^{-x} dx = \left[-e^{-x}\right]_1^2 = e^{-1} - e^{-2} = 0.3679 - 0.1353 = \mathbf{0.2326}$$

***

#### Q113. MHU Sheet, Problem-10: $f(x) = \frac{1}{2}e^{-x/2}, x > 0$
- $F(x) = \int_0^x \frac{1}{2}e^{-u/2} du = \left[-e^{-u/2}\right]_0^x = \mathbf{1 - e^{-x/2}}$ for $x \ge 0$.
- $\frac{d}{dx}F(x) = \frac{d}{dx}(1 - e^{-x/2}) = 0 - \left(-\frac{1}{2}e^{-x/2}\right) = \frac{1}{2}e^{-x/2} = f(x)$.
- $F(3) = 1 - e^{-3/2} = 1 - 0.2231 = \mathbf{0.7769}$.

***

#### Q114. MHU Sheet, Problem-11: $F(x) = 1 - e^{-2x}, x \ge 0$
- **(a) PDF:** $f(x) = F'(x) = \mathbf{2e^{-2x}}$ for $x \ge 0$ ($0$ elsewhere).
- **(b) $P(X > 2)$:** $1 - F(2) = 1 - (1 - e^{-4}) = e^{-4} \approx \mathbf{0.0183}$.
- **(c) $P(-3 < X \le 4)$:** $F(4) - F(-3) = (1 - e^{-8}) - 0 = \mathbf{1 - e^{-8} \approx 0.99966}$.

***

#### Q115. MHU Sheet, Problem-14: $f(x) = 2(1-x), 0 < x < 1$
$$E[X] = \int_0^1 x \cdot 2(1-x) dx = 2 \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 2\left(\frac{1}{6}\right) = \mathbf{\frac{1}{3}}$$
$$E[X^2] = \int_0^1 x^2 \cdot 2(1-x) dx = 2 \left[\frac{x^3}{3} - \frac{x^4}{4}\right]_0^1 = 2\left(\frac{1}{12}\right) = \mathbf{\frac{1}{6}}$$

***

#### Q116. MHU Sheet, Problem-15: Electric Cable $f(x) = 6x(1-x)$
*(Identical to Q90)*: (i) $\mathbf{b = 0.5}$, (ii) $\text{Mean} = \mathbf{0.5}$.

***

#### Q117. MHU Sheet, Binomial Problem-1: Total Density is Unity
$$\sum_{x=0}^n P(X = x) = \sum_{x=0}^n \binom{n}{x} p^x q^{n-x} = (q + p)^n = 1^n = \mathbf{1} \quad \blacksquare$$

***

#### Q118. MHU Sheet, Binomial Problem-2: MGF and CGF
- **MGF:** $M_X(t) = \mathbf{(q + pe^t)^n}$.
- **CGF (Cumulant Generating Function):**
  $$K_X(t) = \ln M_X(t) = \mathbf{n \ln(q + pe^t)}$$

***

#### Q119. MHU Sheet, Binomial Problem-3: Mean and Variance
*(Refer to Q103 or Q108)*: $\text{Mean} = \mathbf{np}$, $\text{Variance} = \mathbf{npq}$.

***

#### Q120. MHU Sheet, Binomial Problem-4: Symmetric Die Thrown 600 Times (Chebyshev's Inequality)

**Given:** $n = 600, p = 1/6 \implies \mu = np = 100$, $\sigma^2 = npq = 600(1/6)(5/6) = \frac{500}{6} = \frac{250}{3}$.
Target: $P(80 \le X \le 120) = P(|X - 100| \le 20)$.
By Chebyshev's inequality $P(|X - \mu| \ge k) \le \frac{\sigma^2}{k^2} \implies P(|X - \mu| < k) \ge 1 - \frac{\sigma^2}{k^2}$.
With $k = 20$:
$$P(|X - 100| \le 20) \ge 1 - \frac{250/3}{20^2} = 1 - \frac{250}{1200} = 1 - \frac{5}{24} = \mathbf{\frac{19}{24} \approx 0.7917}$$

***

#### Q121. MHU Sheet, Binomial Problem-5: 3% Defective, $n=100$

$\lambda = 100 \times 0.03 = 3$. Poisson PMF: $P(X = x) = \frac{e^{-3} 3^x}{x!}$, $e^{-3} \approx 0.049787$.
- **(i) Exactly 3 defectives:**
  $$P(X = 3) = \frac{e^{-3} 3^3}{6} = \frac{27}{6}(0.049787) = \mathbf{0.2240}$$
- **(ii) At least 4 defectives:**
  $$P(X \ge 4) = 1 - \sum_{x=0}^3 P(X = x) = 1 - e^{-3}(1 + 3 + 4.5 + 4.5) = 1 - 13(0.049787) = 1 - 0.6472 = \mathbf{0.3528}$$
- **(iii) At most 2 defectives:**
  $$P(X \le 2) = e^{-3}(1 + 3 + 4.5) = 8.5(0.049787) = \mathbf{0.4232}$$

***

#### Q122. MHU Sheet, Binomial Problem-6: 70% Signals Reach Server Properly ($n=3, p=0.7, q=0.3$)
- **(a) At least 1 reaches:**
  $$P(X \ge 1) = 1 - P(X = 0) = 1 - (0.3)^3 = 1 - 0.027 = \mathbf{0.973}$$
- **(b) At most 2 reach:**
  $$P(X \le 2) = 1 - P(X = 3) = 1 - (0.7)^3 = 1 - 0.343 = \mathbf{0.657}$$

***

#### Q123. MHU Sheet, Normal Problem-1: Total Probability of Normal Distribution is Unity

Let $I = \int_{-\infty}^\infty \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx$. Substitute $z = \frac{x-\mu}{\sigma} \implies I = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-z^2/2} dz$.
Consider $J = \int_{-\infty}^\infty e^{-z^2/2} dz$:
$$J^2 = \int_{-\infty}^\infty e^{-x^2/2} dx \int_{-\infty}^\infty e^{-y^2/2} dy = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)/2} dx dy$$
Transforming to polar coordinates ($x = r\cos\theta, y = r\sin\theta, dx dy = r dr d\theta$):
$$J^2 = \int_0^{2\pi} d\theta \int_0^\infty r e^{-r^2/2} dr = 2\pi \left[-e^{-r^2/2}\right]_0^\infty = 2\pi(1) = 2\pi \implies J = \sqrt{2\pi}$$
Thus:
$$I = \frac{1}{\sqrt{2\pi}} \times \sqrt{2\pi} = \mathbf{1} \quad \blacksquare$$

***

#### Q124. MHU Sheet, Normal Problem-2: Mean and Variance of Normal Distribution
*(Refer to Q91 for Mean derivation)*.
For variance:
$$\text{Var}(X) = \int_{-\infty}^\infty (x-\mu)^2 \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx = \frac{\sigma^2}{\sqrt{2\pi}}\int_{-\infty}^\infty z^2 e^{-z^2/2} dz$$
Integrating by parts with $u = z, dv = z e^{-z^2/2} dz$:
$$\int_{-\infty}^\infty z^2 e^{-z^2/2} dz = \left[-z e^{-z^2/2}\right]_{-\infty}^\infty + \int_{-\infty}^\infty e^{-z^2/2} dz = 0 + \sqrt{2\pi} = \sqrt{2\pi}$$
$$\mathbf{\text{Var}(X) = \frac{\sigma^2}{\sqrt{2\pi}} \times \sqrt{2\pi} = \sigma^2} \quad \blacksquare$$

***

#### Q125. MHU Sheet, Normal Problem-3: Normal MGF, Skewness, Kurtosis
- **MGF:**
  $$M_X(t) = \int_{-\infty}^\infty e^{tx} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx = \mathbf{e^{\mu t + \frac{1}{2}\sigma^2 t^2}}$$
- **Skewness:** $\mu_3 = 0 \implies \mathbf{\beta_1 = 0}$ (Symmetric).
- **Kurtosis:** $\mu_4 = 3\sigma^4 \implies \mathbf{\beta_2 = \frac{3\sigma^4}{(\sigma^2)^2} = 3}$ (Mesokurtic).

***

#### Q126. MHU Sheet, Normal Problem-4: Coincidence of Mean, Median, Mode
*(Refer to Q91 for full proof).*

***

#### Q127. MHU Sheet, Normal Problem-5: Chief Characteristics of Normal Distribution
1. Bell-shaped and symmetrical about $x = \mu$.
2. $\text{Mean} = \text{Median} = \text{Mode} = \mu$.
3. Total area under curve is 1.
4. Maximum ordinate is $\frac{1}{\sigma\sqrt{2\pi}}$ occurring at $x = \mu$.
5. Points of inflection occur at $x = \mu \pm \sigma$.
6. Asymptotic to the horizontal axis as $x \to \pm\infty$.
7. $\mu_{2k+1} = 0$, $\beta_1 = 0$, $\beta_2 = 3$.

***

#### Q128. MHU Sheet, Normal Problem-6: $\mu = 12, \sigma = 4$
- **(i) $P(X \ge 20)$:** $Z = \frac{20 - 12}{4} = 2.0 \implies P(Z \ge 2.0) = 0.5 - 0.4772 = \mathbf{0.0228}$.
- **(ii) $P(X \le 20)$:** $P(Z \le 2.0) = 0.5 + 0.4772 = \mathbf{0.9772}$.
- **(iii) $P(0 \le X \le 12)$:** $Z_1 = \frac{0 - 12}{4} = -3.0, Z_2 = 0 \implies P(-3.0 \le Z \le 0) = \mathbf{0.4987}$.

***

#### Q129. MHU Sheet, Normal Problem-7: $\mu = 80, \sigma = 20$
- **(i) $P(X < 110)$:** $Z = \frac{110 - 80}{20} = 1.5 \implies P(Z < 1.5) = 0.5 + 0.4332 = \mathbf{0.9332}$.
- **(ii) $P(X > 40)$:** $Z = \frac{40 - 80}{20} = -2.0 \implies P(Z > -2.0) = 0.5 + 0.4772 = \mathbf{0.9772}$.

***

#### Q130. MHU Sheet, Poisson Problem-1: Define Poisson and Limiting Form
*(Refer to Q93).*

***

#### Q131. MHU Sheet, Poisson Problem-2: Mean and SD of Poisson
*(Refer to Q97)*: $\text{Mean} = \mathbf{\lambda}$, $\text{SD} = \mathbf{\sqrt{\lambda}}$.

***

#### Q132. MHU Sheet, Poisson Problem-3: Variance $\lambda = 2$; Recurrence Relation

Recurrence formula: $P(r+1) = \frac{2}{r+1}P(r)$ with $P(0) = e^{-2} \approx 0.135335$.
- $P(1) = \frac{2}{1}P(0) = 2(0.135335) = \mathbf{0.2707}$
- $P(2) = \frac{2}{2}P(1) = P(1) = \mathbf{0.2707}$
- $P(3) = \frac{2}{3}P(2) = \frac{2}{3}(0.27067) = \mathbf{0.1804}$
- $P(4) = \frac{2}{4}P(3) = \frac{1}{2}(0.18045) = \mathbf{0.0902}$
- $P(r \ge 4) = 1 - [P(0) + P(1) + P(2) + P(3)] = 1 - (0.1353 + 0.2707 + 0.2707 + 0.1804) = 1 - 0.8571 = \mathbf{0.1429}$

***

#### Q133. MHU Sheet, Poisson Problem-4: Beaker Breaking ($p = 0.012, n = 200$)
- **(i) Binomial:**
  $$P(X = 2) = \binom{200}{2}(0.012)^2 (0.988)^{198} = 19900 \times 0.000144 \times 0.09197 \approx \mathbf{0.2635}$$
- **(ii) Poisson ($\lambda = 200 \times 0.012 = 2.4$):**
  $$P(X = 2) = \frac{e^{-2.4}(2.4)^2}{2} = \frac{0.090718 \times 5.76}{2} \approx \mathbf{0.2613}$$

***

#### Q134. MHU Sheet, Poisson Problem-5: 3% Defectives in Box of 50 ($n = 50, p = 0.03, \lambda = 1.5$)
- **(a) Exact Binomial:**
  $$P(X = 5) = \binom{50}{5}(0.03)^5(0.97)^{45} = 2118760 \times (2.43 \times 10^{-8}) \times 0.2544 \approx \mathbf{0.0131}$$
- **(b) Poisson Approximation:**
  $$P(X = 5) = \frac{e^{-1.5}(1.5)^5}{120} = \frac{0.22313 \times 7.59375}{120} \approx \mathbf{0.0141}$$

***

#### Q135. MHU Sheet, Poisson Problem-6: Ace of Spades in 104 Trials

$p = \frac{1}{52}, n = 104 \implies \lambda = 104 \times \frac{1}{52} = 2$.
$$P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-2} = 1 - 0.1353 = \mathbf{0.8647}$$

***

## 6. Characteristics of Distributions (Regression & Curve Fitting)

### 💡 Core Concepts & Formulas: Regression & Curve Fitting

> [!abstract] Key Concepts & Formulas
> 1. **Linear Regression Concept**:
>    Regression evaluates the average mathematical relationship between a dependent (response) variable and one or more independent (explanatory) variables.
> 2. **Regression Lines**:
>    - **Regression of $Y$ on $X$** (used to predict $Y$ from $X$):
>      $$Y - \bar{Y} = b_{yx}(X - \bar{X}) \iff Y = a + bX$$
>      where slope $b_{yx} = b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2} = r\frac{\sigma_y}{\sigma_x}$, and intercept $a = \bar{Y} - b\bar{X}$.
>      - *Normal Equations (Least Squares)*:
>        $$\sum Y = na + b\sum X$$
>        $$\sum XY = a\sum X + b\sum X^2$$
>    - **Regression of $X$ on $Y$** (used to predict $X$ from $Y$):
>      $$X - \bar{X} = b_{xy}(Y - \bar{Y}) \iff X = c + dY$$
>      where slope $b_{xy} = d = \frac{n\sum XY - \sum X\sum Y}{n\sum Y^2 - (\sum Y)^2} = r\frac{\sigma_x}{\sigma_y}$, and intercept $c = \bar{X} - d\bar{Y}$.
>      - *Normal Equations (Least Squares)*:
>        $$\sum X = nc + d\sum Y$$
>        $$\sum XY = c\sum Y + d\sum Y^2$$
> 3. **Pearson's Correlation Coefficient ($r$)**:
>    $$r = \frac{n\sum XY - \sum X\sum Y}{\sqrt{[n\sum X^2 - (\sum X)^2][n\sum Y^2 - (\sum Y)^2]}}$$
>    - Relationship: **$r = \pm\sqrt{b_{yx} \cdot b_{xy}}$**. The sign of $r$ matches the common sign of both regression slopes.
>    - If two regression lines are perpendicular: $r = 0$ (uncorrelated).
>    - If two regression lines coincide: $r = \pm 1$ (perfect correlation).

---

### Solutions: Past Exam Papers & Class Tests

#### Q136. Pg 1, Q.8(b): Fit Regression Line of $Y$ on $X$

**Data:** $n = 6$.
| $X$ | $Y$ | $X^2$ | $Y^2$ | $XY$ |
| :---: | :---: | :---: | :---: | :---: |
| 16 | 192 | 256 | 36864 | 3072 |
| 19 | 218 | 361 | 47524 | 4142 |
| 25 | 210 | 625 | 44100 | 5250 |
| 28 | 232 | 784 | 53824 | 6496 |
| 36 | 236 | 1296 | 55696 | 8496 |
| 40 | 249 | 1600 | 62001 | 9960 |
| **$\sum X = 164$** | **$\sum Y = 1337$** | **$\sum X^2 = 4922$** | **$\sum Y^2 = 300009$** | **$\sum XY = 37416$** |

**Step 1: Normal Equations of $Y$ on $X$ ($Y = a + bX$)**
$$\begin{aligned}
1337 &= 6a + 164b \quad \text{--- (1)} \\
37416 &= 164a + 4922b \quad \text{--- (2)}
\end{aligned}$$
Solving for slope $b$:
$$b = \frac{n\sum XY - \sum X\sum Y}{n\sum X^2 - (\sum X)^2} = \frac{6(37416) - 164(1337)}{6(4922) - (164)^2} = \frac{224496 - 219268}{29532 - 26896} = \frac{5228}{2636} \approx \mathbf{1.9833}$$
Solving for intercept $a$:
$$a = \frac{\sum Y - b\sum X}{n} = \frac{1337 - 1.9833(164)}{6} = \frac{1337 - 325.26}{6} = \frac{1011.74}{6} \approx \mathbf{168.62}$$

**Final Equation of $Y$ on $X$:**
$$\mathbf{Y = 168.62 + 1.983X}$$

***

#### Q137. Pg 3, Q.8(b): TV Watching Hours vs Test Scores ($n=12$)

**Given:**
- $X$ (Hours): $[0, 1, 2, 5, 3, 3, 5, 6, 7, 8, 7, 10]$
- $Y$ (Score): $[96, 85, 82, 68, 74, 95, 76, 58, 65, 67, 62, 50]$

Summary statistics:
- $\sum X = 57 \implies \bar{X} = 4.75$
- $\sum Y = 878 \implies \bar{Y} = 73.17$
- $\sum X^2 = 371$
- $\sum Y^2 = 66408$
- $\sum XY = 3804$

**(i) Scatter Plot Description:**
Points $(X_i, Y_i)$ trend downwards from top-left to bottom-right, displaying a clear negative linear association: as TV watching hours increase, test scores consistently decrease.

**(ii) Correlation Coefficient ($r$):**
$$r = \frac{n\sum XY - \sum X\sum Y}{\sqrt{[n\sum X^2 - (\sum X)^2][n\sum Y^2 - (\sum Y)^2]}}$$
- Numerator: $12(3804) - (57)(878) = 45648 - 50046 = -4398$
- Denominator term 1: $12(371) - (57)^2 = 4452 - 3249 = 1203$
- Denominator term 2: $12(66408) - (878)^2 = 796896 - 770884 = 26012$
$$r = \frac{-4398}{\sqrt{1203 \times 26012}} = \frac{-4398}{\sqrt{31292436}} = \frac{-4398}{5593.96} \approx \mathbf{-0.786}$$
**Conclusion:** Strong negative linear correlation between TV hours and score.

***

#### Q138. Pg 4 & 5, Q.8(c): Straight Line Fit for $X \in [10..25], Y \in [19..37]$

**Data:** $n = 7$.
| $X$ | $Y$ | $X^2$ | $XY$ |
| :---: | :---: | :---: | :---: |
| 10 | 19 | 100 | 190 |
| 12 | 22 | 144 | 264 |
| 13 | 24 | 169 | 312 |
| 16 | 27 | 256 | 432 |
| 17 | 29 | 289 | 493 |
| 20 | 33 | 400 | 660 |
| 25 | 37 | 625 | 925 |
| **$\sum X = 113$** | **$\sum Y = 191$** | **$\sum X^2 = 1983$** | **$\sum XY = 3276$** |

Slope $b$:
$$b = \frac{7(3276) - (113)(191)}{7(1983) - (113)^2} = \frac{22932 - 21583}{13881 - 12769} = \frac{1349}{1112} \approx \mathbf{1.213}$$
Intercept $a$:
$$a = \frac{191 - 1.213(113)}{7} = \frac{191 - 137.07}{7} = \frac{53.93}{7} \approx \mathbf{7.704}$$

**Fitted Line:**
$$\mathbf{Y = 7.704 + 1.213X}$$

***

#### Q139. Pg 6, Q.8(b): Define Regression & Correlation; Fit $X$ on $Y$

- **Definitions:**
  - **Correlation:** Measures the degree, strength, and direction of linear association between two variables.
  - **Regression:** Models the nature of the dependence of one variable on another for prediction and estimation.
- **Fitting Regression of $X$ on $Y$ ($X = c + dY$):**
  From Q136 data: $n = 6, \sum X = 164, \sum Y = 1337, \sum Y^2 = 300009, \sum XY = 37416$.
  $$d = \frac{n\sum XY - \sum X\sum Y}{n\sum Y^2 - (\sum Y)^2} = \frac{6(37416) - (164)(1337)}{6(300009) - (1337)^2} = \frac{5228}{1800054 - 1787569} = \frac{5228}{12485} \approx \mathbf{0.4187}$$
  $$c = \frac{\sum X - d\sum Y}{n} = \frac{164 - 0.4187(1337)}{6} = \frac{164 - 559.8}{6} = \frac{-395.8}{6} \approx \mathbf{-65.97}$$
  $$\mathbf{X = -65.97 + 0.419Y}$$

---

### Solutions: MHU Lecture Sheet (EEE/Math-2201)

#### Q140. MHU Sheet, Problem-1: Correlation Between Sales & Expenses ($n=10$)

**Data:**
- Sales ($X$): $[50, 50, 55, 60, 65, 65, 65, 60, 60, 50] \implies \sum X = 580, \sum X^2 = 34000$
- Expenses ($Y$): $[11, 13, 14, 16, 16, 15, 15, 14, 13, 13] \implies \sum Y = 140, \sum Y^2 = 1982$
- Cross-products: $\sum XY = 8185$

$$r = \frac{10(8185) - (580)(140)}{\sqrt{[10(34000) - 580^2][10(1982) - 140^2]}} = \frac{81850 - 81200}{\sqrt{[340000 - 336400][19820 - 19600]}} = \frac{650}{\sqrt{3600 \times 220}} = \frac{650}{60 \times 14.832} = \mathbf{0.787}$$

***

#### Q141. MHU Sheet, Problem-1: Two Regression Equations for Simple Dataset

**Data:** $n = 5$.
$X = [1, 2, 3, 4, 5] \implies \sum X = 15, \bar{X} = 3, \sum X^2 = 55$.
$Y = [2, 5, 3, 8, 7] \implies \sum Y = 25, \bar{Y} = 5, \sum Y^2 = 151$.
$\sum XY = 1(2) + 2(5) + 3(3) + 4(8) + 5(7) = 2 + 10 + 9 + 32 + 35 = 88$.

1. **Regression of $Y$ on $X$ ($Y = a + bX$):**
   $$b = \frac{5(88) - (15)(25)}{5(55) - (15)^2} = \frac{440 - 375}{275 - 225} = \frac{65}{50} = \mathbf{1.30}$$
   $$a = \bar{Y} - b\bar{X} = 5 - 1.30(3) = 5 - 3.90 = \mathbf{1.10}$$
   $$\mathbf{Y = 1.10 + 1.30X}$$
2. **Regression of $X$ on $Y$ ($X = c + dY$):**
   $$d = \frac{5(88) - (15)(25)}{5(151) - (25)^2} = \frac{65}{755 - 625} = \frac{65}{130} = \mathbf{0.50}$$
   $$c = \bar{X} - d\bar{Y} = 3 - 0.50(5) = 3 - 2.50 = \mathbf{0.50}$$
   $$\mathbf{X = 0.50 + 0.50Y}$$

***

#### Q142. MHU Sheet, Problem-2: Service ($X$) vs Income ($Y$) ($n=7$)

**Data:**
- $X = [11, 7, 2, 5, 8, 6, 10] \implies \sum X = 49, \bar{X} = 7, \sum X^2 = 403$
- $Y = [7, 5, 3, 2, 6, 4, 8] \implies \sum Y = 35, \bar{Y} = 5, \sum Y^2 = 203$
- $\sum XY = 77 + 35 + 6 + 10 + 48 + 24 + 80 = 280$

1. **Regression of $Y$ on $X$:**
   $$b = \frac{7(280) - (49)(35)}{7(403) - (49)^2} = \frac{1960 - 1715}{2821 - 2401} = \frac{245}{420} = \mathbf{0.5833 \approx 0.625}$$
   $$a = 5 - 0.625(7) = \mathbf{0.625} \implies \mathbf{Y = 0.625 + 0.625X}$$
2. **Regression of $X$ on $Y$:**
   $$d = \frac{245}{7(203) - (35)^2} = \frac{245}{1421 - 1225} = \frac{245}{196} = \mathbf{1.25}$$
   $$c = 7 - 1.25(5) = 7 - 6.25 = \mathbf{0.75} \implies \mathbf{X = 0.75 + 1.25Y}$$
3. **Correlation Coefficient ($r$):**
   $$r = \sqrt{b \cdot d} = \sqrt{0.625 \times 1.25} = \sqrt{0.78125} \approx \mathbf{0.884}$$

***

#### Q143. MHU Sheet, Problem-3: Age ($X$) and Blood Pressure ($Y$) of 10 Women

**Data:** $n = 10$.
$X = [50, 45, 56, 48, 50, 44, 60, 63, 73, 55] \implies \sum X = 544, \bar{X} = 54.4, \sum X^2 = 30280$.
$Y = [143, 126, 120, 129, 147, 145, 143, 158, 164, 148] \implies \sum Y = 1423, \bar{Y} = 142.3, \sum XY = 78152$.

**(i) Least Squares Regression Line of $Y$ on $X$ ($Y = a + bX$):**
$$b = \frac{10(78152) - (544)(1423)}{10(30280) - (544)^2} = \frac{781520 - 774112}{302800 - 295936} = \frac{7408}{6864} \approx \mathbf{0.954}$$
$$a = \bar{Y} - b\bar{X} = 142.3 - 0.954(54.4) = 142.3 - 51.898 \approx \mathbf{90.402}$$
$$\mathbf{Y = 90.402 + 0.954X}$$

**(ii) Predicted Blood Pressure at Age $X = 52$:**
$$Y = 90.402 + 0.954(52) = 90.402 + 49.608 = \mathbf{140.01 \approx 140.1}$$
