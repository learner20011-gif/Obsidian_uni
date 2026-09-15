# Probability and Probability Distributions — Comprehensive Q&A and Solutions

> **Course:** Math-2201 / Math 4 (Statistical Analysis and Probability)  
> **Source Materials:** Class Lecture Notes, Exercises, and Classical Problems (Prof. MHU / Department of Mathematics)  
> **Scope:** Fundamental Probability Concepts, Laws of Probability, Bayes' Theorem, Discrete & Continuous Random Variables, PMF, PDF, Expectation, Measures of Central Location, Moments, Joint/Marginal/Conditional Distributions, and Standard Distributions (Binomial & Poisson).

---

## Table of Contents
1. [Core Definitions & Fundamental Principles](#1-core-definitions--fundamental-principles)
2. [Laws of Probability & Additive Theorems](#2-laws-of-probability--additive-theorems)
3. [Independent Events, Dependent Events & Multiplicative Law](#3-independent-events-dependent-events--multiplicative-law)
4. [Bayes' Theorem & Applications](#4-bayes-theorem--applications)
5. [Discrete Random Variables & Probability Mass Functions (PMF)](#5-discrete-random-variables--probability-mass-functions-pmf)
6. [Continuous Random Variables & Probability Density Functions (PDF)](#6-continuous-random-variables--probability-density-functions-pdf)
7. [Measures of Central Tendency & Moments for Continuous Distributions](#7-measures-of-central-tendency--moments-for-continuous-distributions)
8. [Mathematical Expectation & Raw Moments](#8-mathematical-expectation--raw-moments)
9. [Joint, Marginal, and Conditional Distributions](#9-joint-marginal-and-conditional-distributions)
10. [Binomial Distribution](#10-binomial-distribution)
11. [Poisson Distribution](#11-poisson-distribution)

---

## 1. Core Definitions & Fundamental Principles

### Question 1.1: Fundamental Probability Terminology
**Define the following terms used in probability theory:**
1. **Experiment / Random Experiment**
2. **Trial and Event**
3. **Exhaustive Cases (Exhaustive Events)**
4. **Equally Likely Cases (Equally Likely Events)**
5. **Mutually Exclusive Events**
6. **Mathematical (Classical) Definition of Probability**
7. **Complement of an Event**

---

#### Solution:

1. **Experiment (Random Experiment):**
   An experiment is an act or operation that can be repeated under identical or specified conditions, and whose outcomes are well-defined. If the outcome cannot be predicted with certainty in advance, it is termed a **random experiment**.

2. **Trial and Event:**
   - **Trial:** Performing a random experiment once is known as a **trial**.
   - **Event:** An outcome, or a combination of outcomes, resulting from a trial is called an **event**.  
   *Example:* Tossing a coin is a *trial*; getting a "Head" ($H$) is an *event*.

3. **Exhaustive Cases / Events:**
   The total number of all possible distinct outcomes of an experiment is called the **exhaustive cases** (or exhaustive events). In modern set terminology, the set of all exhaustive outcomes constitutes the **sample space** ($S$), and each individual outcome is a **sample point**.  
   *Example:* When rolling a standard fair six-sided die, the exhaustive cases are $\{1, 2, 3, 4, 5, 6\}$, so $n(S) = 6$.

4. **Equally Likely Cases / Events:**
   Events or outcomes are said to be **equally likely** when none of them is expected to occur in preference to any other; that is, each outcome has the exact same likelihood of occurring.  
   *Example:* When tossing an unbiased, symmetrical coin, obtaining a Head ($H$) and obtaining a Tail ($T$) are equally likely.

5. **Mutually Exclusive Events:**
   Two or more events are said to be **mutually exclusive** (or disjoint) if they cannot happen simultaneously in a single trial. In set notation:
   $$A \cap B = \emptyset \implies P(A \cap B) = 0$$
   *Example:* In a single toss of a die, getting an even number and getting an odd number are mutually exclusive.

6. **Mathematical (Classical) Definition of Probability:**
   If a random experiment can result in $n$ mutually exclusive, exhaustive, and equally likely outcomes, and if $m$ of these outcomes are favorable to an event $A$, then the mathematical probability of event $A$, denoted by $P(A)$, is defined as:
   $$P(A) = \frac{\text{Number of favorable cases}}{\text{Total number of exhaustive cases}} = \frac{m}{n}$$
   **Key Properties:**
   - $0 \le P(A) \le 1$
   - Let $p = P(\text{Success})$ and $q = P(\text{Failure})$. Then $p + q = 1 \implies q = 1 - p$.
   - If $P(A) = 1$, event $A$ is called a **certain event**.
   - If $P(A) = 0$, event $A$ is called an **impossible event**.

7. **Complement of an Event:**
   The complement of an event $A$, denoted by $A^c$ or $\bar{A}$ or $A'$, is the event that $A$ does not occur. It consists of all outcomes in the sample space $S$ that are not in $A$.
   $$P(A^c) = 1 - P(A)$$

---

## 2. Laws of Probability & Additive Theorems

### Question 2.1: Additive Law of Probability
**State the Additive Law of Probability for:**
1. **Mutually Exclusive Events**
2. **Non-Mutually Exclusive Events (for two events and three events, and general case)**

---

#### Solution:

#### 1. For Mutually Exclusive Events:
If $A_1, A_2, A_3, \dots, A_n$ are mutually exclusive events, the probability that at least one of them will happen is the sum of their individual probabilities:
$$P(A_1 + A_2 + \dots + A_n) = P(A_1) + P(A_2) + \dots + P(A_n)$$
In set notation:
$$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)$$

#### 2. For Non-Mutually Exclusive Events:
When events can occur simultaneously:

- **For two events ($A_1$ and $A_2$):**
  $$P(A_1 \cup A_2) = P(A_1) + P(A_2) - P(A_1 \cap A_2)$$

- **For three events ($A_1, A_2, A_3$):**
  $$P(A_1 \cup A_2 \cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 \cap A_2) - P(A_2 \cap A_3) - P(A_3 \cap A_1) + P(A_1 \cap A_2 \cap A_3)$$

- **Generally for $n$ events (Principle of Inclusion-Exclusion):**
  $$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{1 \le i < j \le n} P(A_i \cap A_j) + \sum_{1 \le i < j < k \le n} P(A_i \cap A_j \cap A_k) - \dots + (-1)^{n-1} P\left(\bigcap_{i=1}^n A_i\right)$$

---

### Problem 2.2: Two Unbiased Dice Tossed
**Problem Statement:**  
Two unbiased dice are tossed simultaneously. What is the probability of getting a total point of $8$ or even numbers on both dice?

---

#### Detailed Solution:

**Step 1: Determine the Sample Space ($S$).**  
When two fair six-sided dice are rolled simultaneously, the total number of exhaustive sample points is:
$$n(S) = 6 \times 6 = 36$$
The sample space is:
$$S = \{(x, y) : x \in \{1,2,3,4,5,6\}, y \in \{1,2,3,4,5,6\}\}$$

**Step 2: Identify Event $A$ (Sum of points equals 8).**  
$$A = \{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)\}$$
The number of favorable outcomes for event $A$ is $n(A) = 5$.  
Therefore:
$$P(A) = \frac{n(A)}{n(S)} = \frac{5}{36}$$

**Step 3: Identify Event $B$ (Even numbers on both dice).**  
Both dice must show numbers from $\{2, 4, 6\}$.  
$$B = \{(2,2), (2,4), (2,6), (4,2), (4,4), (4,6), (6,2), (6,4), (6,6)\}$$
The number of favorable outcomes for event $B$ is:
$$n(B) = 3 \times 3 = 9$$
Therefore:
$$P(B) = \frac{n(B)}{n(S)} = \frac{9}{36}$$

**Step 4: Identify the Intersection Event ($A \cap B$).**  
$A \cap B$ is the event where the sum is 8 **and** both numbers are even:
$$A \cap B = \{(2, 6), (4, 4), (6, 2)\}$$
The number of common outcomes is $n(A \cap B) = 3$.  
Therefore:
$$P(A \cap B) = \frac{n(A \cap B)}{n(S)} = \frac{3}{36}$$

**Step 5: Apply the Addition Law for Non-Mutually Exclusive Events.**  
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
Substituting the values:
$$P(A \cup B) = \frac{5}{36} + \frac{9}{36} - \frac{3}{36} = \frac{5 + 9 - 3}{36} = \frac{11}{36}$$

$$\mathbf{P(\text{Sum of 8 or both even}) = \frac{11}{36} \approx 0.3056}$$

---

## 3. Independent Events, Dependent Events & Multiplicative Law

### Question 3.1: Independent vs. Dependent Events
**Define independent and dependent events and state the Multiplication Law of Probability.**

---

#### Solution:

1. **Independent Events:**  
   Events are said to be **independent** if the occurrence (or non-occurrence) of one event has absolutely no influence on the probability of occurrence of any other event.  
   Two events $A$ and $B$ are independent if and only if:
   $$P(A \cap B) = P(A) \cdot P(B)$$
   Equivalently:
   $$P(A|B) = P(A) \quad \text{and} \quad P(B|A) = P(B)$$

2. **Dependent Events:**  
   If the occurrence of one event affects the probability of occurrence of the other, the events are called **dependent events**.

3. **Multiplication Law of Probability (Compound Probability):**  
   - For **dependent events**:
     $$P(A \cap B) = P(A) \cdot P(B|A) = P(B) \cdot P(A|B)$$
     where $P(A|B)$ is the conditional probability of $A$ given that $B$ has occurred ($P(B) > 0$).
   - For **three dependent events ($A, B, C$):**
     $$P(A \cap B \cap C) = P(A) \cdot P(B|A) \cdot P(C|A \cap B)$$

---

### Problem 3.2: Successive Ball Drawing (With and Without Replacement)
**Problem Statement:**  
A bag contains $4$ white balls and $5$ red balls (total $9$ balls). Two balls are drawn successively at random from the bag. What is the probability that both the balls drawn are white when the drawings are made:
1. **With replacement**
2. **Without replacement**

---

#### Detailed Solution:

Let:
- $W_1$ = event that the 1st ball drawn is white
- $W_2$ = event that the 2nd ball drawn is white
- Total balls $= 4 + 5 = 9$.

#### Case (i): With Replacement
Since the first ball is replaced back into the bag before the second ball is drawn, the composition of the bag remains unchanged ($4$ white, $5$ red; total $9$).  
The events $W_1$ and $W_2$ are **independent**:
$$P(W_1) = \frac{4}{9}$$
$$P(W_2|W_1) = P(W_2) = \frac{4}{9}$$

Therefore, the probability that both balls are white is:
$$P(W_1 \cap W_2) = P(W_1) \cdot P(W_2) = \frac{4}{9} \times \frac{4}{9} = \frac{16}{81} \approx 0.1975$$

*(Complete probability distribution for with replacement draws:)*
- $P(W_1 \cap R_2) = \frac{4}{9} \times \frac{5}{9} = \frac{20}{81}$
- $P(R_1 \cap W_2) = \frac{5}{9} \times \frac{4}{9} = \frac{20}{81}$
- $P(R_1 \cap R_2) = \frac{5}{9} \times \frac{5}{9} = \frac{25}{81}$
- *Sum of all probabilities:* $\frac{16 + 20 + 20 + 25}{81} = \frac{81}{81} = 1$.

---

#### Case (ii): Without Replacement
The first ball is not replaced. The outcome of the second draw **depends** on the outcome of the first draw.

- In the first draw: $P(W_1) = \frac{4}{9}$
- After drawing a white ball, there remain $3$ white balls and $5$ red balls (total $8$ balls).  
  Therefore, the conditional probability of drawing a second white ball is:
  $$P(W_2 | W_1) = \frac{3}{8}$$

Applying the multiplication theorem for dependent events:
$$P(W_1 \cap W_2) = P(W_1) \cdot P(W_2 | W_1) = \frac{4}{9} \times \frac{3}{8} = \frac{12}{72} = \frac{1}{6} \approx 0.1667$$

*(Complete probability distribution for without replacement draws:)*
- $P(W_1 \cap R_2) = \frac{4}{9} \times \frac{5}{8} = \frac{20}{72}$
- $P(R_1 \cap W_2) = \frac{5}{9} \times \frac{4}{8} = \frac{20}{72}$
- $P(R_1 \cap R_2) = \frac{5}{9} \times \frac{4}{8} = \frac{20}{72}$
- *Sum of all probabilities:* $\frac{12 + 20 + 20 + 20}{72} = \frac{72}{72} = 1$.

$$\mathbf{\text{Ans: (i) } \frac{16}{81}, \quad \text{(ii) } \frac{1}{6}}$$

---

## 4. Bayes' Theorem & Applications

### Theorem 4.1: Statement & Proof of Bayes' Theorem
**Statement:**  
Let $B_1, B_2, B_3, \dots, B_n$ be a set of $n$ mutually exclusive and exhaustive events forming a partition of the sample space $S$, with prior probabilities $P(B_i) \ne 0$ for each $i = 1, 2, \dots, n$.  
If $A$ is any arbitrary event associated with $S$ such that $P(A) > 0$, then the posterior probability of occurrence of event $B_i$, given that event $A$ has already occurred, is given by:
$$P(B_i | A) = \frac{P(B_i) \cdot P(A | B_i)}{\sum_{k=1}^n P(B_k) \cdot P(A | B_k)}$$

---

#### Proof:

**Step 1: Express conditional probability.**  
By the definition of conditional probability:
$$P(B_i | A) = \frac{P(A \cap B_i)}{P(A)} \quad \dots \text{(1)}$$

**Step 2: Express joint probability using multiplication rule.**  
$$P(A \cap B_i) = P(B_i) \cdot P(A | B_i) \quad \dots \text{(2)}$$

**Step 3: Determine the total probability $P(A)$.**  
Since $B_1, B_2, \dots, B_n$ are mutually exclusive and exhaustive:
$$S = B_1 \cup B_2 \cup \dots \cup B_n$$
We can express event $A$ as:
$$A = A \cap S = A \cap (B_1 \cup B_2 \cup \dots \cup B_n) = (A \cap B_1) \cup (A \cap B_2) \cup \dots \cup (A \cap B_n)$$

Since the events $B_i$ are mutually exclusive, the intersections $(A \cap B_i)$ are also mutually exclusive. Hence, by the additive law of probability:
$$P(A) = P(A \cap B_1) + P(A \cap B_2) + \dots + P(A \cap B_n) = \sum_{k=1}^n P(A \cap B_k)$$

Using the multiplication rule $P(A \cap B_k) = P(B_k) \cdot P(A | B_k)$:
$$P(A) = \sum_{k=1}^n P(B_k) \cdot P(A | B_k) \quad \dots \text{(3)}$$
*(This equation (3) is known as the **Theorem of Total Probability**).*

**Step 4: Substitute (2) and (3) into (1).**  
$$P(B_i | A) = \frac{P(B_i) \cdot P(A | B_i)}{\sum_{k=1}^n P(B_k) \cdot P(A | B_k)}$$
*(Hence proved).*

---

### Problem 4.2: Two Identical Boxes (White and Red Balls)
**Problem Statement:**  
There are two identical boxes containing balls as follows:
- **Box 1:** $4$ white and $3$ red balls (total $7$ balls)
- **Box 2:** $3$ white and $7$ red balls (total $10$ balls)

A box is chosen at random and a ball is drawn at random from it. If the ball drawn is found to be white, what is the probability that it was drawn from the first box?

---

#### Detailed Solution:

Let:
- $B_1$ = event that Box 1 is chosen
- $B_2$ = event that Box 2 is chosen
- $A$ = event that the drawn ball is white

**Step 1: Prior Probabilities.**  
Since the two boxes are identical and chosen at random:
$$P(B_1) = \frac{1}{2}, \quad P(B_2) = \frac{1}{2}$$

**Step 2: Likelihoods (Conditional Probabilities of drawing a white ball).**  
- From Box 1: $P(A | B_1) = \frac{4}{4 + 3} = \frac{4}{7}$
- From Box 2: $P(A | B_2) = \frac{3}{3 + 7} = \frac{3}{10}$

**Step 3: Total Probability of drawing a white ball, $P(A)$.**  
$$P(A) = P(B_1) \cdot P(A | B_1) + P(B_2) \cdot P(A | B_2)$$
$$P(A) = \left(\frac{1}{2} \times \frac{4}{7}\right) + \left(\frac{1}{2} \times \frac{3}{10}\right) = \frac{2}{7} + \frac{3}{20}$$
Finding a common denominator ($140$):
$$P(A) = \frac{2 \times 20 + 3 \times 7}{140} = \frac{40 + 21}{140} = \frac{61}{140}$$

**Step 4: Apply Bayes' Theorem.**  
$$P(B_1 | A) = \frac{P(B_1) \cdot P(A | B_1)}{P(A)} = \frac{\frac{1}{2} \times \frac{4}{7}}{\frac{61}{140}} = \frac{\frac{2}{7}}{\frac{61}{140}} = \frac{2}{7} \times \frac{140}{61} = \frac{2 \times 20}{61} = \frac{40}{61}$$

$$\mathbf{P(B_1 | A) = \frac{40}{61} \approx 0.6557 \quad (65.57\%)}$$

---

### Problem 4.3: Bolt Factory Defective Bolts
**Problem Statement:**  
In a bolt factory, machines $A, B$, and $C$ manufacture respectively $25\%$, $35\%$, and $40\%$ of the total output. Of their output, $5\%$, $4\%$, and $2\%$ respectively are defective bolts.  
A bolt is drawn at random from the total product and is found to be defective. What is the probability that it was manufactured by machine $B$?

---

#### Detailed Solution:

Let:
- $E_A$ = event that the bolt is produced by Machine $A$
- $E_B$ = event that the bolt is produced by Machine $B$
- $E_C$ = event that the bolt is produced by Machine $C$
- $D$ = event that the selected bolt is defective

**Step 1: Prior Probabilities.**  
$$P(E_A) = 25\% = 0.25 = \frac{25}{100}$$
$$P(E_B) = 35\% = 0.35 = \frac{35}{100}$$
$$P(E_C) = 40\% = 0.40 = \frac{40}{100}$$
*(Check sum: $0.25 + 0.35 + 0.40 = 1.00$)*

**Step 2: Likelihoods (Defect rates).**  
$$P(D | E_A) = 5\% = 0.05 = \frac{5}{100}$$
$$P(D | E_B) = 4\% = 0.04 = \frac{4}{100}$$
$$P(D | E_C) = 2\% = 0.02 = \frac{2}{100}$$

**Step 3: Total Probability of drawing a defective bolt, $P(D)$.**  
$$P(D) = P(E_A)P(D|E_A) + P(E_B)P(D|E_B) + P(E_C)P(D|E_C)$$
$$P(E_A)P(D|E_A) = 0.25 \times 0.05 = 0.0125$$
$$P(E_B)P(D|E_B) = 0.35 \times 0.04 = 0.0140$$
$$P(E_C)P(D|E_C) = 0.40 \times 0.02 = 0.0080$$

$$P(D) = 0.0125 + 0.0140 + 0.0080 = 0.0345 = \frac{345}{10000}$$

**Step 4: Apply Bayes' Theorem for Machine $B$.**  
$$P(E_B | D) = \frac{P(E_B) \cdot P(D | E_B)}{P(D)} = \frac{0.0140}{0.0345} = \frac{140}{345}$$
Dividing numerator and denominator by $5$:
$$P(E_B | D) = \frac{28}{69} \approx 0.4058 \quad (40.58\%)$$

$$\mathbf{P(E_B | D) = \frac{28}{69} \approx 0.4058}$$

---

## 5. Discrete Random Variables & Probability Mass Functions (PMF)

### Question 5.1: Definition & Conditions for a PMF
**Define a Probability Mass Function (PMF) and state the essential conditions it must satisfy.**

---

#### Solution:
If a random variable $X$ is discrete, taking distinct values $x_1, x_2, \dots$, its probability mass function $f(x) = P(X = x)$ assigns a probability to each value $x$.

A function $f(x)$ is a valid PMF if and only if:
1. **Non-negativity:** $f(x) \ge 0$ for all possible values of $x$.
2. **Total Probability:** $\sum_{x} f(x) = 1$, where the summation runs over all possible values in the domain of $X$.
3. **Event Probability:** For any subset of values $A$, $P(X \in A) = \sum_{x \in A} f(x)$.

---

### Problem 5.2: Verification of PMFs
**Problem Statement:**  
Check whether the following functions can serve as valid probability mass functions:
1. $f(x) = \frac{2x - 1}{8}, \quad x = 0, 1, 2, 3$
2. $f(x) = \frac{x + 1}{16}, \quad x = 0, 1, 2, 3$  *(also test with denominator 6: $f(x) = \frac{x+1}{6}$)*
3. $f(x) = \frac{3x + 6}{21}, \quad x = 1, 2$

---

#### Detailed Solution:

#### Case (i): $f(x) = \frac{2x - 1}{8}, \quad x \in \{0, 1, 2, 3\}$
- Evaluate at each point:
  - $x = 0: \quad f(0) = \frac{2(0) - 1}{8} = -\frac{1}{8} < 0$
- **Condition 1 Violation:** Since $f(0) < 0$, the non-negativity requirement ($f(x) \ge 0$) is violated.
- **Conclusion:** $f(x)$ is **not** a probability mass function.

---

#### Case (ii-A): $f(x) = \frac{x + 1}{16}, \quad x \in \{0, 1, 2, 3\}$
- Check Condition 1 (Non-negativity):
  - $f(0) = 1/16 > 0$
  - $f(1) = 2/16 > 0$
  - $f(2) = 3/16 > 0$
  - $f(3) = 4/16 > 0$  
  *(Condition 1 is satisfied).*
- Check Condition 2 ($\sum f(x) = 1$):
  $$\sum_{x=0}^3 f(x) = \frac{1}{16} + \frac{2}{16} + \frac{3}{16} + \frac{4}{16} = \frac{10}{16} = \frac{5}{8} \ne 1$$
- **Conclusion:** Because the sum of probabilities is $\frac{10}{16} \ne 1$, $f(x)$ is **not** a probability mass function.

#### Case (ii-B): $f(x) = \frac{x + 1}{6}, \quad x \in \{0, 1, 2, 3\}$
- Evaluating the sum:
  $$\sum_{x=0}^3 f(x) = \frac{1}{6} + \frac{2}{6} + \frac{3}{6} + \frac{4}{6} = \frac{10}{6} = \frac{5}{3} \ne 1$$
- **Conclusion:** $f(x)$ is **not** a probability mass function.

---

#### Case (iii): $f(x) = \frac{3x + 6}{21}, \quad x \in \{1, 2\}$
- Check Condition 1 (Non-negativity):
  - $f(1) = \frac{3(1) + 6}{21} = \frac{9}{21} > 0$
  - $f(2) = \frac{3(2) + 6}{21} = \frac{12}{21} > 0$  
  *(Condition 1 is satisfied).*
- Check Condition 2 ($\sum f(x) = 1$):
  $$\sum_{x=1}^2 f(x) = f(1) + f(2) = \frac{9}{21} + \frac{12}{21} = \frac{21}{21} = 1$$
  *(Condition 2 is satisfied).*
- **Conclusion:** Both conditions are satisfied; therefore, $f(x)$ **is a valid probability mass function**.

---

### Problem 5.3: Geometric-Type Discrete Distribution
**Problem Statement:**  
The probability mass function of a discrete random variable $X$ is defined as:
$$f(x) = \begin{cases} k \left(\frac{3}{4}\right)^x, & x = 0, 1, 2, 3, \dots, \infty \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the value of constant $k$ (or $\alpha$).
2. Compute $P(X \le 3)$.

---

#### Detailed Solution:

#### Step 1: Find the value of $k$
Using the total probability condition:
$$\sum_{x=0}^{\infty} f(x) = 1$$
$$k \sum_{x=0}^{\infty} \left(\frac{3}{4}\right)^x = 1$$

This is an infinite geometric series with first term $a = 1$ and common ratio $r = \frac{3}{4}$.  
Since $|r| = \frac{3}{4} < 1$, the sum is:
$$S_\infty = \frac{a}{1 - r} = \frac{1}{1 - \frac{3}{4}} = \frac{1}{\frac{1}{4}} = 4$$

Therefore:
$$k \times 4 = 1 \implies \mathbf{k = \frac{1}{4}}$$

The complete PMF is:
$$f(x) = \frac{1}{4} \left(\frac{3}{4}\right)^x, \quad x = 0, 1, 2, \dots$$

---

#### Step 2: Calculate $P(X \le 3)$
$$P(X \le 3) = f(0) + f(1) + f(2) + f(3)$$
$$P(X \le 3) = \frac{1}{4}\left[\left(\frac{3}{4}\right)^0 + \left(\frac{3}{4}\right)^1 + \left(\frac{3}{4}\right)^2 + \left(\frac{3}{4}\right)^3\right]$$
$$P(X \le 3) = \frac{1}{4}\left[1 + \frac{3}{4} + \frac{9}{16} + \frac{27}{64}\right]$$

Finding the common denominator ($64$):
$$1 + \frac{3}{4} + \frac{9}{16} + \frac{27}{64} = \frac{64 + 48 + 36 + 27}{64} = \frac{175}{64}$$

Multiplying by $\frac{1}{4}$:
$$P(X \le 3) = \frac{1}{4} \times \frac{175}{64} = \frac{175}{256} \approx 0.6836$$

$$\mathbf{k = \frac{1}{4}, \quad P(X \le 3) = \frac{175}{256} \approx 0.6836}$$

---

### Problem 5.4: Tabular Discrete Distribution
**Problem Statement:**  
The probability distribution of a discrete random variable $Y$ is given by the table:

| $y$ | -3 | -2 | -1 | 0 | 1 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $f(y)$ | $0.10$ | $0.25$ | $0.30$ | $0.15$ | $k$ |

1. Find the value of $k$.
2. Find $P(-3 < Y < 0)$.
3. Find $P(Y \ge -1)$.

---

#### Detailed Solution:

#### 1. Find $k$:
By the property of a probability distribution, the sum of all probabilities must equal $1$:
$$\sum_{y} f(y) = 1$$
$$f(-3) + f(-2) + f(-1) + f(0) + f(1) = 1$$
$$0.10 + 0.25 + 0.30 + 0.15 + k = 1$$
$$0.80 + k = 1 \implies \mathbf{k = 0.20}$$

---

#### 2. Find $P(-3 < Y < 0)$:
The inequality $-3 < Y < 0$ strictly excludes $-3$ and $0$, including only $y = -2$ and $y = -1$:
$$P(-3 < Y < 0) = P(Y = -2) + P(Y = -1)$$
$$P(-3 < Y < 0) = 0.25 + 0.30 = \mathbf{0.55} = \frac{55}{100} = \frac{11}{20}$$

---

#### 3. Find $P(Y \ge -1)$:
This condition includes $y = -1, 0, 1$:
$$P(Y \ge -1) = P(Y = -1) + P(Y = 0) + P(Y = 1)$$
$$P(Y \ge -1) = 0.30 + 0.15 + 0.20 = \mathbf{0.65} = \frac{65}{100} = \frac{13}{20}$$

*(Alternative using complement rule: $P(Y \ge -1) = 1 - [P(Y = -3) + P(Y = -2)] = 1 - (0.10 + 0.25) = 1 - 0.35 = 0.65$)*.

$$\mathbf{\text{Ans: (i) } k = 0.20, \quad \text{(ii) } 0.55, \quad \text{(iii) } 0.65}$$

---

## 6. Continuous Random Variables & Probability Density Functions (PDF)

### Question 6.1: Definition & Conditions for a PDF
**Define a Probability Density Function (PDF) and state the mathematical conditions it must satisfy.**

---

#### Solution:
A random variable $X$ is continuous if it can take any real value in an interval $[a, b]$ (or $(-\infty, \infty)$). The function $f(x)$ is called the **probability density function (p.d.f.)** of $X$ if:
1. **Non-negativity:** $f(x) \ge 0$ for all $-\infty < x < \infty$.
2. **Total Area Under Curve equals 1:**
   $$\int_{-\infty}^{\infty} f(x) \, dx = 1$$
3. **Probability in an interval:** The probability that $X$ falls within the interval $(c, d)$ is given by the definite integral:
   $$P(c < X < d) = \int_{c}^{d} f(x) \, dx$$

---

### Problem 6.2: Verifying a Continuous PDF
**Problem Statement:**  
Check whether the function $f(x) = 6x(1-x), \quad 0 \le x \le 1$ (and $0$ elsewhere) is a valid probability density function.

---

#### Detailed Solution:

**Condition 1: Check $f(x) \ge 0$ on $[0, 1]$:**  
For any $x \in [0, 1]$, both $x \ge 0$ and $(1 - x) \ge 0$.  
Thus, $f(x) = 6x(1-x) \ge 0$ for all $x \in [0, 1]$.

**Condition 2: Check $\int_{-\infty}^\infty f(x) dx = 1$:**
$$\int_{-\infty}^{\infty} f(x) \, dx = \int_{0}^{1} 6x(1 - x) \, dx$$
$$= 6 \int_{0}^{1} (x - x^2) \, dx = 6 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1$$
$$= 6 \left( \frac{1}{2} - \frac{1}{3} \right) = 6 \left( \frac{3 - 2}{6} \right) = 6 \times \frac{1}{6} = 1$$

Since both conditions are satisfied, $f(x)$ **is a valid probability density function**.

---

### Problem 6.3: Continuous PDF $f(x) = kx$
**Problem Statement:**  
The probability density function of a continuous random variable $X$ is:
$$f(x) = \begin{cases} kx, & 0 < x < 4 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the value of constant $k$.
2. Find $P(1 < X < 2)$.
3. Find $P(2 < X < 4)$.

---

#### Detailed Solution:

#### 1. Find $k$:
By the normalization condition:
$$\int_{-\infty}^{\infty} f(x) \, dx = 1 \implies \int_{0}^{4} kx \, dx = 1$$
$$k \left[ \frac{x^2}{2} \right]_0^4 = 1 \implies k \left( \frac{16}{2} - 0 \right) = 1 \implies 8k = 1 \implies \mathbf{k = \frac{1}{8}}$$

Thus, $f(x) = \frac{1}{8}x$ for $0 < x < 4$.

---

#### 2. Find $P(1 < X < 2)$:
$$P(1 < X < 2) = \int_{1}^{2} \frac{1}{8}x \, dx = \frac{1}{8} \left[ \frac{x^2}{2} \right]_1^2 = \frac{1}{16} [2^2 - 1^2] = \frac{1}{16} (4 - 1) = \mathbf{\frac{3}{16}} \approx 0.1875$$

---

#### 3. Find $P(2 < X < 4)$:
$$P(2 < X < 4) = \int_{2}^{4} \frac{1}{8}x \, dx = \frac{1}{8} \left[ \frac{x^2}{2} \right]_2^4 = \frac{1}{16} [4^2 - 2^2] = \frac{1}{16} (16 - 4) = \frac{12}{16} = \mathbf{\frac{3}{4}} = 0.75$$

$$\mathbf{\text{Ans: (i) } k = \frac{1}{8}, \quad \text{(ii) } \frac{3}{16}, \quad \text{(iii) } \frac{3}{4}}$$

---

### Problem 6.4: Continuous PDF $f(x) = k(1+x)$
**Problem Statement:**  
The probability function of a continuous random variable $X$ is:
$$f(x) = \begin{cases} k(1+x), & 2 < x < 5 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the value of constant $k$.
2. Find $P(3 < X < 4)$.
3. Find $P(X < 4)$.

---

#### Detailed Solution:

#### 1. Find $k$:
$$\int_{2}^{5} k(1 + x) \, dx = 1$$
$$k \left[ x + \frac{x^2}{2} \right]_2^5 = 1$$
$$k \left[ \left(5 + \frac{25}{2}\right) - \left(2 + \frac{4}{2}\right) \right] = 1$$
$$k \left[ \left(\frac{35}{2}\right) - 4 \right] = k \left[ \frac{35 - 8}{2} \right] = k \left( \frac{27}{2} \right) = 1$$
$$\mathbf{k = \frac{2}{27}}$$

So the PDF is $f(x) = \frac{2}{27}(1 + x)$ on $2 < x < 5$.

---

#### 2. Find $P(3 < X < 4)$:
$$P(3 < X < 4) = \int_{3}^{4} \frac{2}{27}(1 + x) \, dx = \frac{2}{27} \left[ x + \frac{x^2}{2} \right]_3^4$$
$$= \frac{2}{27} \left[ \left(4 + \frac{16}{2}\right) - \left(3 + \frac{9}{2}\right) \right]$$
$$= \frac{2}{27} \left[ 12 - \frac{15}{2} \right] = \frac{2}{27} \left( \frac{9}{2} \right) = \frac{2 \times 9}{27 \times 2} = \frac{9}{27} = \mathbf{\frac{1}{3}} \approx 0.3333$$

---

#### 3. Find $P(X < 4)$:
Since the random variable is only defined starting from $x = 2$:
$$P(X < 4) = \int_{2}^{4} \frac{2}{27}(1 + x) \, dx = \frac{2}{27} \left[ x + \frac{x^2}{2} \right]_2^4$$
$$= \frac{2}{27} \left[ \left(4 + \frac{16}{2}\right) - \left(2 + \frac{4}{2}\right) \right]$$
$$= \frac{2}{27} [12 - 4] = \frac{2}{27} \times 8 = \mathbf{\frac{16}{27}} \approx 0.5926$$

$$\mathbf{\text{Ans: (i) } k = \frac{2}{27}, \quad \text{(ii) } \frac{1}{3}, \quad \text{(iii) } \frac{16}{27}}$$

---

## 7. Measures of Central Tendency & Moments for Continuous Distributions

### Question 7.1: Formulas for Continuous Distributions
**Write down the definitions and mathematical formulas for the different measures of central tendency and moments for a continuous random variable $X$ defined on $[a, b]$ with probability density function $f(x)$:**

---

#### Formulas:

1. **Arithmetic Mean ($AM$ or $\mu$):**
   $$AM = \mu = E(X) = \int_{a}^{b} x f(x) \, dx$$

2. **Harmonic Mean ($HM$):**
   $$\frac{1}{HM} = \int_{a}^{b} \frac{1}{x} f(x) \, dx$$

3. **Geometric Mean ($GM$ or $G$):**
   $$\log(GM) = \int_{a}^{b} (\log x) f(x) \, dx \implies GM = \exp\left( \int_{a}^{b} (\log x) f(x) \, dx \right)$$

4. **Median ($M_e$):**
   The value $M_e$ that divides the total probability into two equal halves ($50\%$ each):
   $$\int_{a}^{M_e} f(x) \, dx = \int_{M_e}^{b} f(x) \, dx = \frac{1}{2}$$

5. **Mode ($M_o$):**
   The value of $x$ at which $f(x)$ attains its global maximum in the permissible range:
   $$f'(x) = 0 \quad \text{and} \quad f''(x) < 0$$

6. **Moments:**
   - **$r$-th Raw Moment (about origin):**
     $$\mu_r' = E(X^r) = \int_{a}^{b} x^r f(x) \, dx$$
   - **$r$-th Central Moment (about mean $\mu$):**
     $$\mu_r = E[(X - \mu)^r] = \int_{a}^{b} (x - \mu)^r f(x) \, dx$$

---

### Problem 7.2: Comprehensive Calculation on $f(x) = cx(2-x)$
**Problem Statement:**  
A continuous random variable $X$ has the probability density function:
$$f(x) = \begin{cases} cx(2-x), & 0 \le x \le 2 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the value of constant $c$.
2. Calculate the **Arithmetic Mean ($AM$)**.
3. Calculate the **Harmonic Mean ($HM$)**.
4. Calculate the **Median ($M_e$)**.
5. Calculate the **Mode ($M_o$)**.
6. Calculate the **Geometric Mean ($GM$)**.

---

#### Detailed Solution:

#### Step 1: Find Constant $c$
$$\int_{0}^{2} f(x) \, dx = 1 \implies c \int_{0}^{2} (2x - x^2) \, dx = 1$$
$$c \left[ x^2 - \frac{x^3}{3} \right]_0^2 = 1 \implies c \left( 4 - \frac{8}{3} \right) = 1 \implies c \left( \frac{4}{3} \right) = 1 \implies \mathbf{c = \frac{3}{4}}$$

Hence, the PDF is:
$$f(x) = \frac{3}{4}x(2-x) = \frac{3}{2}x - \frac{3}{4}x^2, \quad 0 \le x \le 2$$

---

#### Step 2: Arithmetic Mean ($AM$)
$$AM = \int_{0}^{2} x f(x) \, dx = \int_{0}^{2} x \cdot \frac{3}{4}x(2-x) \, dx$$
$$= \frac{3}{4} \int_{0}^{2} (2x^2 - x^3) \, dx = \frac{3}{4} \left[ \frac{2x^3}{3} - \frac{x^4}{4} \right]_0^2$$
$$= \frac{3}{4} \left[ \frac{2(8)}{3} - \frac{16}{4} \right] = \frac{3}{4} \left[ \frac{16}{3} - 4 \right] = \frac{3}{4} \left( \frac{4}{3} \right) = \mathbf{1}$$

---

#### Step 3: Harmonic Mean ($HM$)
$$\frac{1}{HM} = \int_{0}^{2} \frac{1}{x} f(x) \, dx = \int_{0}^{2} \frac{1}{x} \left( \frac{3}{4}x(2-x) \right) \, dx$$
$$= \frac{3}{4} \int_{0}^{2} (2 - x) \, dx = \frac{3}{4} \left[ 2x - \frac{x^2}{2} \right]_0^2$$
$$= \frac{3}{4} \left[ 2(2) - \frac{4}{2} \right] = \frac{3}{4} [4 - 2] = \frac{3}{4} \times 2 = \frac{3}{2}$$

$$\frac{1}{HM} = \frac{3}{2} \implies \mathbf{HM = \frac{2}{3}}$$

---

#### Step 4: Median ($M_e$)
By definition of the median:
$$\int_{0}^{M_e} f(x) \, dx = \frac{1}{2}$$
$$\int_{0}^{M_e} \frac{3}{4}(2x - x^2) \, dx = \frac{1}{2}$$
$$\frac{3}{4} \left[ x^2 - \frac{x^3}{3} \right]_0^{M_e} = \frac{1}{2}$$
$$M_e^2 - \frac{M_e^3}{3} = \frac{1}{2} \times \frac{4}{3} = \frac{2}{3}$$
Multiply through by $3$:
$$3M_e^2 - M_e^3 = 2 \implies M_e^3 - 3M_e^2 + 2 = 0$$

To solve the cubic equation $M_e^3 - 3M_e^2 + 2 = 0$:  
Notice that $M_e = 1$ is a root, because:
$$1^3 - 3(1)^2 + 2 = 1 - 3 + 2 = 0$$

Factor out $(M_e - 1)$:
$$M_e^3 - M_e^2 - 2M_e^2 + 2M_e - 2M_e + 2 = 0$$
$$(M_e - 1)(M_e^2 - 2M_e - 2) = 0$$

Solving the quadratic part $M_e^2 - 2M_e - 2 = 0$:
$$M_e = \frac{-(-2) \pm \sqrt{(-2)^2 - 4(1)(-2)}}{2(1)} = \frac{2 \pm \sqrt{4 + 8}}{2} = \frac{2 \pm \sqrt{12}}{2} = 1 \pm \sqrt{3}$$
- $M_e = 1 + \sqrt{3} \approx 2.732$ (lies outside the permissible interval $[0, 2]$)
- $M_e = 1 - \sqrt{3} \approx -0.732$ (lies outside the permissible interval $[0, 2]$)

Therefore, the only admissible root lying within the range $[0, 2]$ is:
$$\mathbf{M_e = 1}$$

---

#### Step 5: Mode ($M_o$)
To find the mode, differentiate $f(x)$ with respect to $x$:
$$f(x) = \frac{3}{2}x - \frac{3}{4}x^2$$
$$f'(x) = \frac{3}{2} - \frac{3}{2}x$$
Set $f'(x) = 0$:
$$\frac{3}{2}(1 - x) = 0 \implies x = 1$$

Now check the second derivative:
$$f''(x) = -\frac{3}{2} < 0 \quad (\text{strictly negative for all } x)$$

Since $f''(1) < 0$, $f(x)$ attains a local (and global) maximum at $x = 1$.  
Since $x = 1$ lies inside $[0, 2]$:
$$\mathbf{M_o = 1}$$

---

#### Step 6: Geometric Mean ($GM$)
$$\ln(GM) = \int_{0}^{2} (\ln x) f(x) \, dx = \frac{3}{4} \int_{0}^{2} (2x - x^2) \ln x \, dx$$

Using integration by parts ($\int u v' dx = u v - \int u' v dx$):
- $\int x \ln x \, dx = \frac{x^2}{2} \ln x - \int \frac{x^2}{2} \frac{1}{x} dx = \frac{x^2}{2} \ln x - \frac{x^2}{4}$
- $\int x^2 \ln x \, dx = \frac{x^3}{3} \ln x - \int \frac{x^3}{3} \frac{1}{x} dx = \frac{x^3}{3} \ln x - \frac{x^3}{9}$

Combining:
$$\int (2x - x^2) \ln x \, dx = \left( x^2 - \frac{x^3}{3} \right) \ln x - \left( \frac{x^2}{2} - \frac{x^3}{9} \right)$$

Evaluating between limits $0$ and $2$:
- At upper limit $x = 2$:
  $$\left( 4 - \frac{8}{3} \right) \ln 2 - \left( \frac{4}{2} - \frac{8}{9} \right) = \frac{4}{3} \ln 2 - \left( 2 - \frac{8}{9} \right) = \frac{4}{3} \ln 2 - \frac{10}{9}$$
- At lower limit $x \to 0^+$:
  $$\lim_{x \to 0^+} \left( x^2 - \frac{x^3}{3} \right) \ln x = 0, \quad \lim_{x \to 0^+} \left( \frac{x^2}{2} - \frac{x^3}{9} \right) = 0$$

Thus:
$$\ln(GM) = \frac{3}{4} \left[ \frac{4}{3} \ln 2 - \frac{10}{9} \right] = \ln 2 - \frac{5}{6}$$
Exponentiating both sides:
$$\mathbf{GM = e^{\ln 2 - \frac{5}{6}} = 2 e^{-5/6} \approx 2 \times 0.4346 = 0.8692}$$

$$\mathbf{\text{Summary: } c = \frac{3}{4}, \quad AM = 1, \quad HM = \frac{2}{3}, \quad M_e = 1, \quad M_o = 1, \quad GM = 2e^{-5/6} \approx 0.8692}$$

*(Note: Because the distribution is completely symmetric about $x = 1$, $AM = \text{Median} = \text{Mode} = 1$).*

---

## 8. Mathematical Expectation & Raw Moments

### Question 8.1: Expectation Formulas
**Define Mathematical Expectation and Moments for Discrete and Continuous Random Variables.**

---

#### Solution:

1. **For a Discrete Random Variable $X$:**  
   If $X$ takes values $x_1, x_2, \dots, x_n$ with probabilities $P(x_1), P(x_2), \dots, P(x_n)$ where $\sum_{i=1}^n P(x_i) = 1$:
   - **Expectation (Mean):**
     $$E(X) = \sum_{i=1}^n x_i P(x_i)$$
   - **$r$-th Moment about Origin:**
     $$E(X^r) = \mu_r' = \sum_{i=1}^n x_i^r P(x_i)$$

2. **For a Continuous Random Variable $X$:**  
   If $X$ has probability density function $f(x)$:
   - **Expectation (Mean):**
     $$E(X) = \int_{-\infty}^{\infty} x f(x) \, dx$$
   - **$r$-th Moment about Origin:**
     $$E(X^r) = \mu_r' = \int_{-\infty}^{\infty} x^r f(x) \, dx$$

---

## 9. Joint, Marginal, and Conditional Distributions

### Question 9.1: Theoretical Definitions
**Define Joint Probability Function, Marginal Probability Function, Conditional Probability Function, and Statistical Independence.**

---

#### Solution:

1. **Joint Probability Density Function (Continuous Bivariate):**  
   For two continuous random variables $X$ and $Y$, $f(x, y)$ satisfies:
   - $f(x, y) \ge 0$ for all $(x, y)$
   - $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1$

2. **Marginal Density Functions:**
   - Marginal density of $X$:
     $$f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy$$
   - Marginal density of $Y$:
     $$f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$$

3. **Conditional Density Functions:**
   - Conditional density of $X$ given $Y = y$:
     $$f(x | y) = \frac{f(x, y)}{f_Y(y)}, \quad \text{provided } f_Y(y) > 0$$
   - Conditional density of $Y$ given $X = x$:
     $$f(y | x) = \frac{f(x, y)}{f_X(x)}, \quad \text{provided } f_X(x) > 0$$

4. **Independence of Random Variables:**  
   Two random variables $X$ and $Y$ are **independent** if and only if for all $x$ and $y$:
   $$f(x, y) = f_X(x) \cdot f_Y(y)$$
   Equivalently: $f(x | y) = f_X(x)$ and $f(y | x) = f_Y(y)$.

---

### Problem 9.2: Bivariate Exponential-Related PDF
**Problem Statement:**  
The joint probability density function of two continuous random variables $X$ and $Y$ is given by:
$$f(x, y) = \begin{cases} x e^{-x(y+1)}, & x > 0, y > 0 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the marginal density function of $X$, $f_X(x)$.
2. Find the marginal density function of $Y$, $f_Y(y)$.
3. Find the conditional density functions $f(x|y)$ and $f(y|x)$.
4. Determine whether $X$ and $Y$ are statistically independent.

---

#### Detailed Solution:

#### 1. Marginal Density Function of $X$, $f_X(x)$:
Integrate $f(x, y)$ with respect to $y$ over $(0, \infty)$:
$$f_X(x) = \int_{0}^{\infty} x e^{-x(y+1)} \, dy = \int_{0}^{\infty} x e^{-x} e^{-xy} \, dy$$
Since $x$ is constant with respect to $y$, factor out $x e^{-x}$:
$$f_X(x) = x e^{-x} \int_{0}^{\infty} e^{-xy} \, dy$$
Evaluating the integral:
$$\int_{0}^{\infty} e^{-xy} \, dy = \left[ \frac{e^{-xy}}{-x} \right]_{y=0}^{y\to\infty} = 0 - \left( -\frac{1}{x} \right) = \frac{1}{x}$$
Therefore:
$$f_X(x) = x e^{-x} \left( \frac{1}{x} \right) = \mathbf{e^{-x}, \quad x > 0}$$
*(Notice that $X$ follows a standard exponential distribution with parameter $\lambda = 1$).*

---

#### 2. Marginal Density Function of $Y$, $f_Y(y)$:
Integrate $f(x, y)$ with respect to $x$ over $(0, \infty)$:
$$f_Y(y) = \int_{0}^{\infty} x e^{-x(y+1)} \, dx$$
Let $a = y + 1$. Since $y > 0$, $a > 1 > 0$.  
The integral becomes:
$$\int_{0}^{\infty} x e^{-ax} \, dx$$
Using the standard Gamma integral $\int_0^\infty x^{n-1} e^{-ax} dx = \frac{\Gamma(n)}{a^n}$, where $n = 2$:
$$\int_{0}^{\infty} x e^{-ax} \, dx = \frac{\Gamma(2)}{a^2} = \frac{1!}{a^2} = \frac{1}{a^2}$$
*(Alternatively by parts: let $z = ax \implies dx = \frac{dz}{a}$, yielding $\frac{1}{a^2}\int_0^\infty z e^{-z} dz = \frac{1}{a^2}$).*

Substituting $a = y + 1$:
$$\mathbf{f_Y(y) = \frac{1}{(y + 1)^2}, \quad y > 0}$$
*(Check validity: $\int_0^\infty \frac{1}{(y+1)^2} dy = \left[ -\frac{1}{y+1} \right]_0^\infty = 0 - (-1) = 1$).*

---

#### 3. Conditional Density Functions:

- **Conditional PDF of $X$ given $Y = y$:**
  $$f(x | y) = \frac{f(x, y)}{f_Y(y)} = \frac{x e^{-x(y+1)}}{\frac{1}{(y+1)^2}} = \mathbf{(y+1)^2 x e^{-x(y+1)}, \quad x > 0}$$

- **Conditional PDF of $Y$ given $X = x$:**
  $$f(y | x) = \frac{f(x, y)}{f_X(x)} = \frac{x e^{-x(y+1)}}{e^{-x}} = \frac{x e^{-x} e^{-xy}}{e^{-x}} = \mathbf{x e^{-xy}, \quad y > 0}$$

---

#### 4. Check for Independence:
Two random variables are independent if and only if $f(x, y) = f_X(x) \cdot f_Y(y)$ for all $x > 0, y > 0$.
$$f_X(x) \cdot f_Y(y) = e^{-x} \cdot \frac{1}{(y+1)^2} = \frac{e^{-x}}{(y+1)^2}$$
Comparing with the joint density:
$$f(x, y) = x e^{-x(y+1)}$$
Clearly:
$$\frac{e^{-x}}{(y+1)^2} \ne x e^{-x(y+1)}$$
Also, $f(y|x) = x e^{-xy}$, which explicitly depends on $x$.

**Conclusion:**  
$\mathbf{X \text{ and } Y \text{ are NOT independent (they are dependent random variables)}}$.

---

## 10. Binomial Distribution

### Question 10.1: Definition & Mathematical Model
**Define the Binomial Distribution, state its assumptions, and write down its probability function and main properties.**

---

#### Solution:
A random experiment is called a **Binomial Experiment** if it satisfies the following four conditions:
1. The experiment consists of a fixed number, $n$, of repeated trials.
2. Each trial results in only one of two mutually exclusive outcomes: **Success ($S$)** or **Failure ($F$)**.
3. The probability of success on any single trial, denoted by $p$, remains constant from trial to trial ($q = 1 - p$ is the probability of failure).
4. The trials are statistically independent.

If $X$ denotes the number of successes in $n$ trials, then $X$ is a binomial random variable denoted as $X \sim B(n, p)$.

#### Probability Mass Function:
$$b(x; n, p) = P(X = x) = \binom{n}{x} p^x q^{n-x} = \frac{n!}{x!(n-x)!} p^x (1-p)^{n-x}, \quad x = 0, 1, 2, \dots, n$$

#### Key Properties:
1. Total probability: $\sum_{x=0}^n \binom{n}{x} p^x q^{n-x} = (p + q)^n = 1^n = 1$.
2. **Mean ($\mu$):** $\mu = E(X) = np$.
3. **Variance ($\sigma^2$):** $\sigma^2 = \text{Var}(X) = npq$.
4. **Standard Deviation ($\sigma$):** $\sigma = \sqrt{npq}$.
5. Note that for a binomial distribution, $\text{Variance} < \text{Mean}$ always holds since $q < 1$.

---

### Problem 10.2: Determining $n, p, q$ from Mean and Standard Deviation
**Problem Statement:**  
The mean and standard deviation of a binomial distribution are $40$ and $6$ respectively. Find the parameters $n, p$, and $q$.

---

#### Detailed Solution:

**Given:**
- Mean: $\mu = np = 40 \quad \dots \text{(1)}$
- Standard Deviation: $\sigma = \sqrt{npq} = 6 \quad \dots \text{(2)}$

**Step 1: Find $q$**  
Squaring equation (2):
$$\sigma^2 = npq = 6^2 = 36$$
Substitute $np = 40$ from equation (1) into $npq = 36$:
$$40 \cdot q = 36 \implies q = \frac{36}{40} = \mathbf{0.90} = \frac{9}{10}$$

**Step 2: Find $p$**  
Since $p + q = 1$:
$$p = 1 - q = 1 - 0.90 = \mathbf{0.10} = \frac{1}{10}$$

**Step 3: Find $n$**  
From equation (1), $np = 40$:
$$n \times 0.10 = 40 \implies n = \frac{40}{0.10} = \mathbf{400}$$

$$\mathbf{n = 400, \quad p = 0.10, \quad q = 0.90}$$

---

### Problem 10.3: Occupational Disease in an Industry
**Problem Statement:**  
In an industry, there is a $20\%$ chance that a worker will suffer from a certain occupational disease. What is the probability that out of $6$ randomly selected workers:
1. Exactly $3$ workers will contract the disease
2. Exactly $4$ workers will contract the disease
3. $4$ or more workers will contract the disease

---

#### Detailed Solution:

Here:
- Number of trials: $n = 6$
- Probability of success (contracting the disease): $p = 20\% = 0.2$
- Probability of failure: $q = 1 - p = 1 - 0.2 = 0.8$
- Let $X$ be the number of workers contracting the disease: $X \sim B(6, 0.2)$.
$$P(X = x) = \binom{6}{x} (0.2)^x (0.8)^{6-x}$$

---

#### 1. Exactly 3 workers ($X = 3$):
$$P(X = 3) = \binom{6}{3} (0.2)^3 (0.8)^{6-3} = \binom{6}{3} (0.2)^3 (0.8)^3$$
- $\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$
- $(0.2)^3 = 0.008$
- $(0.8)^3 = 0.512$
$$P(X = 3) = 20 \times 0.008 \times 0.512 = 20 \times 0.004096 = \mathbf{0.08192} \quad (8.192\%)$$

---

#### 2. Exactly 4 workers ($X = 4$):
$$P(X = 4) = \binom{6}{4} (0.2)^4 (0.8)^{6-4} = \binom{6}{4} (0.2)^4 (0.8)^2$$
- $\binom{6}{4} = \binom{6}{2} = \frac{6 \times 5}{2 \times 1} = 15$
- $(0.2)^4 = 0.0016$
- $(0.8)^2 = 0.64$
$$P(X = 4) = 15 \times 0.0016 \times 0.64 = 15 \times 0.001024 = \mathbf{0.01536} \quad (1.536\%)$$

---

#### 3. 4 or more workers ($X \ge 4$):
$$P(X \ge 4) = P(X = 4) + P(X = 5) + P(X = 6)$$
We already have $P(X = 4) = 0.01536$. Now compute $P(X = 5)$ and $P(X = 6)$:
- $P(X = 5) = \binom{6}{5} (0.2)^5 (0.8)^1 = 6 \times 0.00032 \times 0.8 = 6 \times 0.000256 = 0.001536$
- $P(X = 6) = \binom{6}{6} (0.2)^6 (0.8)^0 = 1 \times 0.000064 \times 1 = 0.000064$

Summing these up:
$$P(X \ge 4) = 0.01536 + 0.001536 + 0.000064 = \mathbf{0.01696} \quad (1.696\%)$$

$$\mathbf{\text{Ans: (i) } 0.08192 \text{ (or } 8.192\%), \quad \text{(ii) } 0.01536 \text{ (or } 1.536\%), \quad \text{(iii) } 0.01696 \text{ (or } 1.696\%)}$$

---

### Problem 10.4: Children Gender Probabilities in a Family of 4
**Problem Statement:**  
Find the probability that in a family of $4$ children, there will be:
1. Exactly $1$ boy
2. At least $1$ boy
3. At least $1$ boy and $1$ girl
4. Exactly $2$ boys and $2$ girls  
*(Assume the probability of a male and a female birth are equal, i.e., $p = q = \frac{1}{2}$).*

---

#### Detailed Solution:

Let $X$ be the number of boys in a family of $n = 4$ children.  
Assuming births are independent and $P(\text{Boy}) = p = \frac{1}{2}$, $P(\text{Girl}) = q = \frac{1}{2}$:
$$X \sim B\left(4, \frac{1}{2}\right)$$
The probability mass function is:
$$P(X = x) = \binom{4}{x} \left(\frac{1}{2}\right)^x \left(\frac{1}{2}\right)^{4-x} = \binom{4}{x} \left(\frac{1}{2}\right)^4 = \frac{\binom{4}{x}}{16}, \quad x \in \{0, 1, 2, 3, 4\}$$

Total outcomes in the sample space: $2^4 = 16$.

---

#### 1. Exactly 1 boy ($X = 1$):
$$P(X = 1) = \frac{\binom{4}{1}}{16} = \frac{4}{16} = \mathbf{\frac{1}{4} = 0.25} \quad (25\%)$$

---

#### 2. At least 1 boy ($X \ge 1$):
Using the complement rule:
$$P(X \ge 1) = 1 - P(X = 0)$$
$$P(X = 0) = \frac{\binom{4}{0}}{16} = \frac{1}{16}$$
$$P(X \ge 1) = 1 - \frac{1}{16} = \mathbf{\frac{15}{16} = 0.9375} \quad (93.75\%)$$

---

#### 3. At least 1 boy and 1 girl:
"At least 1 boy and 1 girl" means the family cannot consist of **all boys** ($X = 4$) and cannot consist of **all girls** ($X = 0$):
$$P(\text{At least 1 boy and 1 girl}) = 1 - [P(X = 0) + P(X = 4)]$$
- $P(X = 0) = \frac{\binom{4}{0}}{16} = \frac{1}{16}$
- $P(X = 4) = \frac{\binom{4}{4}}{16} = \frac{1}{16}$

$$P(\text{At least 1 boy and 1 girl}) = 1 - \left(\frac{1}{16} + \frac{1}{16}\right) = 1 - \frac{2}{16} = \frac{14}{16} = \mathbf{\frac{7}{8} = 0.875} \quad (87.5\%)$$

---

#### 4. Exactly 2 boys and 2 girls ($X = 2$):
$$P(X = 2) = \frac{\binom{4}{2}}{16} = \frac{\frac{4 \times 3}{2 \times 1}}{16} = \frac{6}{16} = \mathbf{\frac{3}{8} = 0.375} \quad (37.5\%)$$

$$\mathbf{\text{Ans: (i) } \frac{1}{4}, \quad \text{(ii) } \frac{15}{16}, \quad \text{(iii) } \frac{7}{8}, \quad \text{(iv) } \frac{3}{8}}$$

---

## 11. Poisson Distribution

### Question 11.1: Definition as a Limiting Form of Binomial Distribution
**Define the Poisson Distribution and state the conditions under which the Binomial Distribution tends to the Poisson Distribution.**

---

#### Solution:
The **Poisson Distribution** is a discrete probability distribution that expresses the probability of a given number of rare events occurring in a fixed interval of time or space.

#### Limiting Conditions:
The Binomial Distribution $B(n, p)$ tends to the Poisson Distribution under the following three simultaneous conditions:
1. The number of trials is indefinitely large: $n \to \infty$.
2. The probability of success in each trial is extremely small: $p \to 0$.
3. The average number of successes remains a finite positive constant:
   $$\mu = \lambda = np = \text{finite constant}$$

#### Probability Mass Function:
If $X$ is a Poisson random variable with parameter $\lambda$ (or $\mu$):
$$P(X = x) = f(x; \lambda) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, 2, 3, \dots, \infty$$
where $e \approx 2.71828$.

#### Key Properties:
- $\sum_{x=0}^{\infty} \frac{e^{-\lambda} \lambda^x}{x!} = e^{-\lambda} \sum_{x=0}^{\infty} \frac{\lambda^x}{x!} = e^{-\lambda} \cdot e^{\lambda} = 1$.
- **Mean:** $E(X) = \lambda$.
- **Variance:** $\text{Var}(X) = \lambda$.
- *Characteristic feature:* For a Poisson distribution, $\mathbf{\text{Mean} = \text{Variance} = \lambda}$.

---

### Problem 11.2: Rare Reaction to an Injection
**Problem Statement:**  
If the probability that an individual suffers a bad reaction from a certain injection is $0.001$, what is the probability that out of $2000$ individuals:
1. Exactly $3$ will suffer the bad reaction
2. None will suffer the bad reaction
3. More than $2$ will suffer the bad reaction  
*(Given $e^{-2} \approx 0.135335$)*

---

#### Detailed Solution:

**Step 1: Identify Parameters and Applicability.**
- Total trials: $n = 2000$ (very large, $n \to \infty$)
- Probability of bad reaction: $p = 0.001$ (very small, $p \to 0$)
- Mean $\lambda$:
  $$\lambda = \mu = np = 2000 \times 0.001 = \mathbf{2}$$

Since $n$ is large and $p$ is small, we model $X$ (the number of individuals suffering a bad reaction) using a **Poisson distribution** with parameter $\lambda = 2$:
$$P(X = x) = \frac{e^{-2} \cdot 2^x}{x!}, \quad x = 0, 1, 2, \dots$$

---

#### 1. Exactly 3 will suffer the bad reaction ($X = 3$):
$$P(X = 3) = \frac{e^{-2} \cdot 2^3}{3!} = \frac{e^{-2} \times 8}{6} = \frac{4}{3} e^{-2}$$
Using $e^{-2} \approx 0.135335$:
$$P(X = 3) \approx \frac{4}{3} \times 0.135335 \approx \mathbf{0.18045} \quad (18.05\%)$$

---

#### 2. None will suffer the bad reaction ($X = 0$):
$$P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!} = \frac{e^{-2} \times 1}{1} = e^{-2}$$
$$P(X = 0) \approx \mathbf{0.13534} \quad (13.53\%)$$

---

#### 3. More than 2 will suffer the bad reaction ($X > 2$):
Using the complement rule:
$$P(X > 2) = 1 - P(X \le 2) = 1 - [P(X = 0) + P(X = 1) + P(X = 2)]$$

Compute the individual probabilities:
- $P(X = 0) = e^{-2}$
- $P(X = 1) = \frac{e^{-2} \cdot 2^1}{1!} = 2 e^{-2}$
- $P(X = 2) = \frac{e^{-2} \cdot 2^2}{2!} = \frac{4 e^{-2}}{2} = 2 e^{-2}$

Sum of terms for $X \le 2$:
$$P(X \le 2) = e^{-2} + 2e^{-2} + 2e^{-2} = 5 e^{-2}$$

Now subtract from $1$:
$$P(X > 2) = 1 - 5 e^{-2}$$
$$P(X > 2) \approx 1 - 5(0.135335) = 1 - 0.676675 = \mathbf{0.323325} \approx \mathbf{0.3233} \quad (32.33\%)$$

$$\mathbf{\text{Ans: (i) } \frac{4}{3}e^{-2} \approx 0.1805, \quad \text{(ii) } e^{-2} \approx 0.1353, \quad \text{(iii) } 1 - 5e^{-2} \approx 0.3233}$$
