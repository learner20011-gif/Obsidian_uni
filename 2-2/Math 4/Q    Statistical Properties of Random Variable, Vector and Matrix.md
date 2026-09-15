# Statistical Properties of Random Variable, Vector and Matrix - Comprehensive Question Bank

This document compiles all questions from **Past Exam Papers / Class Tests** and the **MHU Lecture Sheet (EEE/Math-2201)**, organized strictly according to the syllabus topics for Random Variables, Vectors, Matrices, Joint Distributions, Hypothesis Testing, and Regression.

*(Note: Topics from the syllabus outline that have no questions in either past papers or the lecture sheet are explicitly marked.)*

***

### **PDF, CDF and MGF of continuous and discrete random variables**

#### Past Exam Papers & Class Tests
1. **Pg 1, Q.6(b):** The diameter of an electric cable say $x$ , is assumed to be a continuous random variable with probability density function:
   $f(x) = 6x(1-x); \quad 0 \le x \le 1$.
   (i) Find the mean of $x$.
   (ii) Determine a number $b$ such that $P(x<b) = P(x>b)$

2. **Pg 2, Q.6(b):** The diameter of a electric cable is assumed to continuous random variable with probability density function $f(x) = x(5-x^2), 0 \le x \le 2$. Find the mean and variance of it.
   *(Note: Pg 4, Q.7(a) contains a nearly identical question but is missing the word "a" before "electric", so it is technically a unique string).*

3. **Pg 3, Q.8(a):** Find the moment generating function of Poisson distribution and find mean and variance of Poisson distribution from that MGF.

4. **Pg 14, CT-03, Q.3:** Prove that the mean $\mu = np$ and standard deviation $\sigma = \sqrt{npq}$, where p, q and n are probability of success, failure and number of trial respectively, using any moment generating function.

5. **Pg 14, CT-03, Q.3 (Or):** Define probability density function. A manufacturer of pins knows that 5% of his product is defective. If he sells pins in boxes of 100 and guarantees that not more than 10 pins will be defective. What is the approximate probability that a box will fail to meet the guaranteed quality?

6. **Pg 19, Class Test-2, Q2:** The diameter of an electric cable say $x$, is assumed to be a continuous random variable with probability density function $f(x) = 6x(1-x); \quad 0 \le x \le 1$.
   (i) Determine a number $b$ such that $P(x<b) = P(x>b)$. (ii) Find the mean of $x$.

#### MHU Lecture Sheet (EEE/Math-2201)
7. **MHU Sheet, Lec 7-10, Problem-9:** Let X be a random variable with probability density function given by $f(x) = e^{-x}; 0 < x < \infty$.
   (a) Check that the above is p.d.f.
   (b) Find $P(1 < x < 2)$. (Ans: 0.2325)

8. **MHU Sheet, Lec 7-10, Problem 10:** Find $F(x)$ and show that $f(x) = \frac{d}{dx}F(x)$ and find $F(3)$ for $f(x) = \frac{1}{2}e^{-x/2}; 0 < x < \infty$.

9. **MHU Sheet, Lec 7-10, Problem 11:** The distribution function for a random variable X is:
   $$F(x) = \begin{cases} 1 - e^{-2x}, & x \ge 0 \\ 0, & x < 0 \end{cases}$$
   Find (a) the density function, (b) the probability that $X > 2$, and (c) the probability that $-3 < X \le 4$.

10. **MHU Sheet, Lec 7-10, Problem-14:** Find the expected value of the random variable X and also of its square having the following density function:
    $$f(x) = \begin{cases} 2(1-x), & 0 < x < 1 \\ 0, & \text{elsewhere} \end{cases}$$

11. **MHU Sheet, Lec 7-10, Problem 15:** The diameter of an electric cable say $x$, is assumed to be a continuous random variable with probability density function (p.d.f):
    $$f(x) = 6x(1-x); \quad 0 \le x \le 1$$
    (i) Determine a number $b$ such that $P(x < b) = P(x > b)$.
    (ii) Find the mean of $x$. *(Note: Identical to Pg 1, Q.6(b))*

12. **MHU Sheet, Lec 11-14 (Binomial), Problem-2:** Find the moment generating function and cumulant generating function of binomial distribution.

13. **MHU Sheet, Lec 11-14 (Normal), Problem-3:** Find the moment generating function, skewness and kurtosis of normal distribution and comment on the shape.

14. **MHU Sheet, Lec 11-14 (Poisson), Problem-2:** Find the mean and standard deviation of Poisson distribution as a limiting form of binomial distribution.

---

### **Marginal PDF and joint PDF of continuous and discrete random variables**

#### Past Exam Papers & Class Tests
15. **Pg 2 & Pg 3, Q.7(a):** The joint probability density function is given by:
    $$f_{XY}(x,y) = Ke^{-0.001x-0.002y}, \quad \text{for } 0 < x < y < \infty \text{ and } k=6\times 10^{-6}$$
    Find:
    (i) The probability $P(x \le 1000, y \le 2000)$
    (ii) The probability that $y$ exceeds 2000.
    (iii) The conditional density function of $Y$ given $X$.

#### MHU Lecture Sheet (EEE/Math-2201)
16. **MHU Sheet, Lec 7-10, Problem-12:** Find the conditional probability function of $X$ given $Y = 3$ for the following data:
    | $X \backslash Y$ | 0 | 1 | 2 | 3 | 4 | $P(y_j)$ |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | **1** | $1/16$ | 0 | 0 | 0 | $1/16$ | $2/16$ |
    | **2** | 0 | $2/16$ | $2/16$ | $2/16$ | 0 | $6/16$ |
    | **3** | 0 | $2/16$ | $2/16$ | $2/16$ | 0 | $6/16$ |
    | **4** | 0 | 0 | $2/16$ | 0 | 0 | $2/16$ |
    | **$P(x_i)$** | $1/16$ | $4/16$ | $6/16$ | $4/16$ | $1/16$ | 1 |

17. **MHU Sheet, Lec 7-10, Problem-13:** The joint probability distribution of $X$ and $Y$ is given by the following table:
    | $X \backslash Y$ | 1 | 3 | 9 | $P(x)$ |
    | :--- | :--- | :--- | :--- | :--- |
    | **2** | $1/8$ | $1/24$ | $1/12$ | $1/4$ |
    | **4** | $1/4$ | $1/4$ | 0 | $1/2$ |
    | **6** | $1/8$ | $1/24$ | $1/12$ | $1/4$ |
    | **$P(y)$** | $1/2$ | $1/3$ | $1/6$ | 1 |
    Determine:
    (i) $P(x), P(y), E(X), E(Y), V(X), V(Y)$.
    (ii) $P(x/y), P(y/x), E(X/Y), E(Y/X), V(X/Y), V(Y/X)$.

---

### **Joint PDF of two independent random variables**
*No explicit separate questions regarding the joint PDF of independent random variables were found in the provided past papers or lecture sheet.*

---

### **Joint PDF of two dependent random variables**
*No explicit separate questions regarding dependent random variables were found, other than the conditional density/distribution calculations in **Pg 2 & Pg 3, Q.7(a)** and **MHU Sheet Problem-12 & 13** listed above.*

---

### **Calculation of PDF of a vector from the PDF of its element**
*No questions related to vector PDFs were found in the provided past papers or lecture sheet.*

---

### **Calculation of PDF of a matrix from the PDF of its element**
*No questions related to matrix PDFs were found in the provided past papers or lecture sheet.*

---

### **Hypothesis testing and regression analysis**

#### Past Exam Papers & Class Tests
18. **Pg 1, Q.8(b):** Fit a regression line of X and Y to the following data using least square method.
    | X: | 16 | 19 | 25 | 28 | 36 | 40 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Y: | 192 | 218 | 210 | 232 | 236 | 249 |

19. **Pg 3, Q.8(b):** The following data represent the number of hours 12 different students watched television during the weekend and the score of each student who took a test the following Sunday.
    | Hour's | 0 | 1 | 2 | 5 | 3 | 3 | 5 | 6 | 7 | 8 | 7 | 10 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Test score | 96 | 85 | 82 | 68 | 74 | 95 | 76 | 58 | 65 | 67 | 62 | 50 |
    (i) Display the scatter plot
    (ii) Calculate the correlation coefficient.

20. **Pg 4 & Pg 5, Q.8(c):** Deetrmine the equation of the straight line which best fits the following data.
    | X | 10 | 12 | 13 | 16 | 17 | 20 | 25 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Y | 19 | 22 | 24 | 27 | 29 | 33 | 37 |

21. **Pg 6, Q.8(b):** What is regression and correlation? Fit a regression line of X on Y to the following data using least square method.
    | X | 16 | 19 | 25 | 28 | 36 | 40 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Y | 192 | 218 | 210 | 232 | 236 | 249 |

#### MHU Lecture Sheet (EEE/Math-2201)
22. **MHU Sheet, Lec 15-17 (Hypothesis Testing), Problem-1:** The mean lifetime of a sample of 100 tubelights produced by a company is found to be 1580 hours with standard deviation of 90 hours. Test the hypothesis that mean lifetime of the tubes produced by the company is 1600 hr (at 5% level of significance).
    *(Ans: Computed $z = -2.22$, falls in rejection region $|z| > 1.96$; reject null hypothesis).*

23. **MHU Sheet, Lec 15-17 (Regression), Problem-1:** Calculate the regression equation of X on Y and Y on X from the following data:
    | X | 1 | 2 | 3 | 4 | 5 |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | Y | 2 | 5 | 3 | 8 | 7 |
    *(Ans: Regression of X on Y: $X = 0.5 + 0.5Y$; Regression of Y on X: $Y = 1.10 + 1.30X$).*

24. **MHU Sheet, Lec 15-17 (Regression), Problem-2:** The following data related to length of service and income of the employees of an organization:
    | Length of service (years) | 11 | 7 | 2 | 5 | 8 | 6 | 10 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Income (Tk. hundred) | 7 | 5 | 3 | 2 | 6 | 4 | 8 |
    Compute the coefficient of correlation for the above data. Find the two regression equations.
    *(Ans: $X = 0.75 + 1.25Y$, $Y = 0.625 + 0.625X$, $r = 0.884$).*

25. **MHU Sheet, Lec 15-17 (Regression), Problem-3:** The following data gives the ages and blood pressure of 10 women:
    | Age (X) | 50 | 45 | 56 | 48 | 50 | 44 | 60 | 63 | 73 | 55 |
    | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
    | Blood pressure (Y) | 143 | 126 | 120 | 129 | 147 | 145 | 143 | 158 | 164 | 148 |
    (i) Estimate the Least square regression equation of Y on X.
    (ii) Predict the blood pressure of a woman whose age is 52 years.
    *(Ans: (i) $Y = 0.954X + 90.402$, (ii) At age 52, $Y = 140.1$).*