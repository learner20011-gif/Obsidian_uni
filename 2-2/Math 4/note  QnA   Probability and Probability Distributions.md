# Probability and Probability Distributions — Comprehensive Q&A and Solutions

> **Course:** Math-2201 / Math 4 (Statistical Analysis and Probability)  
> **Source Materials:** Class Lecture Notes, Homework Exercises, Class Tests, and Semester Final Exam Papers (Prof. MHU / Department of Mathematics, RUET)  
> **Scope:** Fundamental Probability Concepts, Combinatorial Probability, Laws of Probability, Bayes' Theorem, Discrete & Continuous Random Variables, Probability Mass Functions (PMF), Probability Density Functions (PDF), Cumulative Distribution Functions (CDF), Expectation & Raw/Central Moments, Moment Generating Functions (MGF), Joint/Marginal/Conditional Distributions, and Theoretical Distributions (Binomial, Poisson, and Normal Distributions).

---


### 🏷️ Origin & Problem Identifier Legend
To help distinguish original foundational note material from newly integrated exam and lecture problems:
- 📌 **`[ORIGINAL NOTE]`**: 27 foundational questions, theorems, and problems originally present in this document.
- 🆕 **`[NEW — FROM Q-BANK]`**: 53 newly added problems, proofs, theorems, and exam questions integrated from `Q    statistical Analysis and Probability.md` and `Q    Statistical Properties of Random Variable, Vector and Matrix.md`.

---

## Table of Contents
1. [Core Definitions & Fundamental Principles](#1-core-definitions--fundamental-principles)
2. [Laws of Probability & Additive Theorems](#2-laws-of-probability--additive-theorems)
3. [Independent Events, Dependent Events & Multiplicative Law](#3-independent-events-dependent-events--multiplicative-law)
4. [Bayes' Theorem & Applications](#4-bayes-theorem--applications)
5. [Discrete Random Variables & Probability Mass Functions (PMF)](#5-discrete-random-variables--probability-mass-functions-pmf)
6. [Continuous Random Variables & Probability Density Functions (PDF)](#6-continuous-random-variables--probability-density-functions-pdf)
7. [Cumulative Distribution Function (CDF) & Properties](#7-cumulative-distribution-function-cdf--properties)
8. [Measures of Central Tendency & Moments for Continuous Distributions](#8-measures-of-central-tendency--moments-for-continuous-distributions)
9. [Mathematical Expectation, Moments & Moment Generating Functions (MGF)](#9-mathematical-expectation-moments--moment-generating-functions-mgf)
10. [Joint, Marginal, and Conditional Distributions (Discrete & Continuous)](#10-joint-marginal-and-conditional-distributions-discrete--continuous)
11. [Binomial Distribution](#11-binomial-distribution)
12. [Poisson Distribution](#12-poisson-distribution)
13. [Normal Distribution (Continuous Probability Distribution)](#13-normal-distribution-continuous-probability-distribution)

---


## 1. Core Definitions & Fundamental Principles

### Question 1.1: Fundamental Probability Terminology
*(Ref: MHU Sheet Lec 7-10 | Pg 12, CT-02, Q.3)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Syllabus Terminology)*
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

### Problem 1.2: Selection of Defective Bulbs
*(Ref: Question Bank Q.70 | Pg 12, CT-02, Q.4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Of ten electric bulbs, three are defective, but it is not known which are defective.
1. In how many ways can three bulbs be selected?
2. How many of these selections will include at least one defective bulb?
3. What is the probability that a random selection of three bulbs contains at least one defective bulb?

---

#### Detailed Solution:

Here:
- Total number of bulbs $N = 10$.
- Number of defective bulbs $D = 3$.
- Number of good (non-defective) bulbs $G = 10 - 3 = 7$.
- Number of bulbs to be chosen $r = 3$.

#### 1. Total Number of Ways to Select 3 Bulbs:
The number of ways to choose any $3$ bulbs out of $10$ without restriction is given by the combination formula:
$$\text{Total Selections} = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120 \text{ ways}$$

#### 2. Number of Selections with at Least One Defective Bulb:
We can find this easily using the complement principle:
$$\text{Selections with } \ge 1 \text{ defective} = (\text{Total selections}) - (\text{Selections with no defective bulbs})$$

- Selections with **no defective bulbs** means all $3$ bulbs are chosen from the $7$ good bulbs:
  $$\text{Ways with no defective} = \binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35 \text{ ways}$$

- Therefore:
  $$\text{Selections with at least one defective} = 120 - 35 = \mathbf{85 \text{ ways}}$$

*(Alternative direct calculation:)*
- $1$ defective and $2$ good: $\binom{3}{1} \binom{7}{2} = 3 \times 21 = 63$
- $2$ defective and $1$ good: $\binom{3}{2} \binom{7}{1} = 3 \times 7 = 21$
- $3$ defective and $0$ good: $\binom{3}{3} \binom{7}{0} = 1 \times 1 = 1$
- $\text{Total} = 63 + 21 + 1 = 85 \text{ ways}$.

#### 3. Probability of at Least One Defective Bulb:
$$P(\text{At least 1 defective}) = \frac{85}{120} = \frac{17}{24} \approx 0.7083 \quad (70.83\%)$$

$$\mathbf{\text{Ans: (1) } 120 \text{ ways}, \quad \text{(2) } 85 \text{ ways}, \quad \text{(3) } \frac{17}{24} \approx 0.7083}$$

---

### Problem 1.3: Committee Selection with a Specific Member
*(Ref: Question Bank Q.64 | Pg 2, Q.6(c))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A committee of $4$ people is to be appointed from:
- $3$ officers of the Production Department
- $4$ officers of the Purchase Department
- $2$ officers of the Sales Department
- $1$ officer who is a Chartered Accountant (CA)

Find the probability that the Chartered Accountant must be in the committee.

---

#### Detailed Solution:

**Step 1: Determine total officers and exhaustive outcomes.**  
- Total available officers:
  $$N = 3 + 4 + 2 + 1 = 10 \text{ officers}$$
- Committee size $r = 4$.
- The total number of exhaustive ways to form a 4-person committee from 10 candidates is:
  $$n(S) = \binom{10}{4} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$$

**Step 2: Determine favorable outcomes.**  
For the Chartered Accountant to be on the committee:
- We must select the $1$ CA from the $1$ available CA: $\binom{1}{1} = 1$ way.
- The remaining $4 - 1 = 3$ committee members must be selected from the remaining $10 - 1 = 9$ other officers:
  $$\binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84 \text{ ways}$$

Therefore, the number of favorable committee combinations is:
$$n(A) = \binom{1}{1} \times \binom{9}{3} = 1 \times 84 = 84$$

**Step 3: Calculate the probability.**  
$$P(\text{CA is on the committee}) = \frac{n(A)}{n(S)} = \frac{84}{210} = \frac{2}{5} = \mathbf{0.40} \quad (40\%)$$

$$\mathbf{P(\text{CA must be in the committee}) = \frac{2}{5} = 0.40}$$

---

### Problem 1.4: Four Squares in a Diagonal Line on a Chessboard
*(Ref: Question Bank Q.68 | Pg 6, Q.6(c))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
If four squares are chosen at random on an $8 \times 8$ standard chessboard, find the chance that they should all lie in a diagonal line.

---

#### Detailed Solution:

**Step 1: Total Exhaustive Cases ($n(S)$).**  
An $8 \times 8$ chessboard contains $8 \times 8 = 64$ squares.  
Choosing $4$ squares at random out of $64$:
$$n(S) = \binom{64}{4} = \frac{64 \times 63 \times 62 \times 61}{4 \times 3 \times 2 \times 1} = 16 \times 21 \times 62 \times 61 = 635,376$$

**Step 2: Structure of Diagonals on a Chessboard.**  
A chessboard has two families of diagonals:
1. Diagonals running from top-left to bottom-right (main-diagonal direction).
2. Diagonals running from bottom-left to top-right (anti-diagonal direction).

To contain $4$ squares, a diagonal must have length $k \ge 4$.  
Let us count the number of diagonals of length $k \in \{4, 5, 6, 7, 8\}$ in **one** direction:
- Length $k = 8$: $1$ diagonal (the main diagonal) $\implies \binom{8}{4}$ ways.
- Length $k = 7$: $2$ diagonals (one on each side of the main diagonal) $\implies 2 \times \binom{7}{4}$ ways.
- Length $k = 6$: $2$ diagonals $\implies 2 \times \binom{6}{4}$ ways.
- Length $k = 5$: $2$ diagonals $\implies 2 \times \binom{5}{4}$ ways.
- Length $k = 4$: $2$ diagonals $\implies 2 \times \binom{4}{4}$ ways.
*(Diagonals of length $k = 1, 2, 3$ cannot contain 4 squares).*

**Step 3: Evaluate combinations for one direction:**
- For $k = 8$: $1 \times \binom{8}{4} = 1 \times 70 = 70$
- For $k = 7$: $2 \times \binom{7}{4} = 2 \times 35 = 70$
- For $k = 6$: $2 \times \binom{6}{4} = 2 \times 15 = 30$
- For $k = 5$: $2 \times \binom{5}{4} = 2 \times 5 = 10$
- For $k = 4$: $2 \times \binom{4}{4} = 2 \times 1 = 2$

Sum of favorable choices in one direction:
$$70 + 70 + 30 + 10 + 2 = 182$$

**Step 4: Total Favorable Outcomes ($n(A)$).**  
Since there are two symmetrical diagonal directions (main and anti-diagonals):
$$n(A) = 2 \times 182 = 364$$

**Step 5: Compute the probability.**  
$$P(\text{4 squares in a diagonal line}) = \frac{n(A)}{n(S)} = \frac{364}{635,376}$$
Dividing numerator and denominator by $4$:
$$P = \frac{91}{158,844} \approx 0.00057288 \quad (0.0573\%)$$

$$\mathbf{P(\text{Diagonal Line}) = \frac{91}{158,844} \approx 5.73 \times 10^{-4}}$$

---

### Problem 1.5: Product of Randomly Chosen Positive and Negative Numbers
*(Ref: Question Bank Q.89 | MHU Sheet Lec 7-10, Problem-16)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
There are $6$ positive numbers and $8$ negative numbers. Four numbers are chosen at random without replacement and are then multiplied together. What is the probability that the resulting product is a positive number?

---

#### Detailed Solution:

**Step 1: Total Exhaustive Outcomes.**  
Total available numbers $= 6 + 8 = 14$ numbers.  
Choosing $4$ numbers at random without replacement:
$$n(S) = \binom{14}{4} = \frac{14 \times 13 \times 12 \times 11}{4 \times 3 \times 2 \times 1} = 1001$$

**Step 2: Condition for a Positive Product.**  
A product of four non-zero real numbers is strictly **positive** if and only if the number of negative factors chosen is **even**.  
Therefore, the number of negative numbers selected must be either $0$, $2$, or $4$:

- **Case 1: $0$ negative numbers and $4$ positive numbers**  
  $$n_1 = \binom{8}{0} \times \binom{6}{4} = 1 \times 15 = 15$$

- **Case 2: $2$ negative numbers and $2$ positive numbers**  
  $$\binom{8}{2} = \frac{8 \times 7}{2} = 28, \quad \binom{6}{2} = \frac{6 \times 5}{2} = 15$$
  $$n_2 = \binom{8}{2} \times \binom{6}{2} = 28 \times 15 = 420$$

- **Case 3: $4$ negative numbers and $0$ positive numbers**  
  $$n_3 = \binom{8}{4} \times \binom{6}{0} = \frac{8 \times 7 \times 6 \times 5}{24} \times 1 = 70 \times 1 = 70$$

**Step 3: Total Favorable Cases.**  
$$n(A) = n_1 + n_2 + n_3 = 15 + 420 + 70 = 505$$

**Step 4: Compute Probability.**  
$$P(\text{Product is positive}) = \frac{n(A)}{n(S)} = \frac{505}{1001} \approx 0.504495$$

$$\mathbf{P(\text{Product is positive}) = \frac{505}{1001} \approx 0.5045 \quad (50.45\%)}$$

---


## 2. Laws of Probability & Additive Theorems

### Question 2.1: Additive Law of Probability
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Core Theoretical Law)*
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

### Theorem 2.2: Proof of the Additive Law of Probability
*(Ref: Question Bank Q.62, Q.73, Q.76, Q.77, Q.78 | Pg 1, Q.6(a), Pg 20 Class Test-2 Q1, MHU Sheet Theorems 1, 2, 3)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**State and prove the Additive Law of Probability for:**
1. Two non-mutually exclusive events $A$ and $B$.
2. Three events $A, B$, and $C$.
3. General extension to $n$ events.

---

#### Detailed Proof:

#### 1. Proof for Two Events:
Let $A$ and $B$ be two events defined on sample space $S$.  
From set theory, the union $A \cup B$ can be decomposed into two mutually exclusive sets:
$$A \cup B = A \cup (B \cap A^c)$$
where $A$ and $(B \cap A^c)$ are disjoint ($A \cap (B \cap A^c) = \emptyset$).  
By the axiom of additivity for mutually exclusive events:
$$P(A \cup B) = P(A) + P(B \cap A^c) \quad \dots \text{(1)}$$

Now consider the event $B$. We can partition $B$ into two mutually exclusive components:
$$B = (A \cap B) \cup (B \cap A^c)$$
Since $(A \cap B)$ and $(B \cap A^c)$ are disjoint:
$$P(B) = P(A \cap B) + P(B \cap A^c)$$
Rearranging terms gives:
$$P(B \cap A^c) = P(B) - P(A \cap B) \quad \dots \text{(2)}$$

Substituting equation (2) into equation (1):
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
*(Hence proved).*

---

#### 2. Proof for Three Events:
Let $D = A \cup B$. Then:
$$P(A \cup B \cup C) = P(D \cup C)$$
Applying the addition theorem for two events to $D$ and $C$:
$$P(D \cup C) = P(D) + P(C) - P(D \cap C) \quad \dots \text{(3)}$$

Substitute $P(D) = P(A \cup B) = P(A) + P(B) - P(A \cap B)$:
$$P(D \cap C) = P((A \cup B) \cap C)$$
Using the distributive law of set theory:
$$(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$$
Applying the two-event addition theorem to $(A \cap C)$ and $(B \cap C)$:
$$P((A \cap C) \cup (B \cap C)) = P(A \cap C) + P(B \cap C) - P((A \cap C) \cap (B \cap C))$$
Since $(A \cap C) \cap (B \cap C) = A \cap B \cap C$:
$$P(D \cap C) = P(A \cap C) + P(B \cap C) - P(A \cap B \cap C)$$

Substituting this back into equation (3):
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(B \cap C) - P(A \cap C) + P(A \cap B \cap C)$$
*(Hence proved).*

---

#### 3. Extension to $n$ Events (Mathematical Induction):
By continuing this inductive substitution for $n$ events, we obtain the **Principle of Inclusion-Exclusion**:
$$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{1 \le i < j \le n} P(A_i \cap A_j) + \sum_{1 \le i < j < k \le n} P(A_i \cap A_j \cap A_k) - \dots + (-1)^{n-1} P\left(\bigcap_{i=1}^n A_i\right)$$

*(Boole's Inequality corollary: $P(\bigcup_{i=1}^n A_i) \le \sum_{i=1}^n P(A_i)$).*

---

### Problem 2.3: Two Unbiased Dice Tossed (Sum 8 or Both Even)
*(Ref: Note Problem 2.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 2.2)*
**Problem Statement:**  
Two unbiased dice are tossed simultaneously. What is the probability of getting a total point of $8$ or even numbers on both dice?

---

#### Detailed Solution:
- Total sample space: $n(S) = 6 \times 6 = 36$.
- Event $A$ (Sum = 8): $A = \{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)\} \implies n(A) = 5, P(A) = \frac{5}{36}$.
- Event $B$ (Both even): $x, y \in \{2, 4, 6\} \implies n(B) = 3 \times 3 = 9, P(B) = \frac{9}{36}$.
- Event $A \cap B$ (Sum = 8 and both even): $\{(2, 6), (4, 4), (6, 2)\} \implies n(A \cap B) = 3, P(A \cap B) = \frac{3}{36}$.
- Applying Addition Law:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{5}{36} + \frac{9}{36} - \frac{3}{36} = \frac{11}{36} \approx 0.3056$$

$$\mathbf{P(A \cup B) = \frac{11}{36} \approx 0.3056}$$

---

### Problem 2.4: Office Demographics (3-Set Venn Diagram & Additive Principles)
*(Ref: Question Bank Q.63 | Pg 2, Q.6(a))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
In a certain office there are $400$ employees. Among them:
- $150$ are men
- $276$ are university graduates
- $212$ are married persons
- $94$ are male university graduates
- $151$ are married university graduates
- $119$ are married men
- $72$ are married male university graduates

Find:
1. The number of single women who are not university graduates.
2. The number of married women who are university graduates.

---

#### Detailed Solution:

Let the universal set of employees be $U$, with $n(U) = 400$.  
Define the three primary attribute sets:
- $M$: set of male employees $\implies n(M) = 150$. (Hence women $W = M^c$, $n(W) = 400 - 150 = 250$).
- $G$: set of university graduates $\implies n(G) = 276$.
- $H$: set of married persons $\implies n(H) = 212$. (Hence single employees are $H^c$).

**Given Intersection Cardinalities:**
- $n(M \cap G) = 94$
- $n(H \cap G) = 151$
- $n(M \cap H) = 119$
- $n(M \cap H \cap G) = 72$

---

#### 1. Calculate the Total Number of Employees Having at Least One Attribute:
Using the Principle of Inclusion-Exclusion:
$$n(M \cup H \cup G) = n(M) + n(H) + n(G) - n(M \cap H) - n(H \cap G) - n(M \cap G) + n(M \cap H \cap G)$$
Substitute the numerical values:
$$n(M \cup H \cup G) = 150 + 212 + 276 - 119 - 151 - 94 + 72$$
$$= 638 - 364 + 72 = 274 + 72 = 346$$

The number of employees who have **none** of the three attributes (i.e. not male, not married, not a graduate) is:
$$n(M^c \cap H^c \cap G^c) = n(U) - n(M \cup H \cup G) = 400 - 346 = \mathbf{54}$$

Since not male means female, and not married means single, and not a graduate means non-graduate:
$$\mathbf{\text{Number of single women who are not university graduates}} = \mathbf{54}$$

---

#### 2. Calculate the Number of Married Women Who Are University Graduates:
This group corresponds to employees who are married ($H$), graduates ($G$), and women ($M^c$):
$$n(M^c \cap H \cap G)$$

Notice that the married graduates group $H \cap G$ is composed of married male graduates and married female graduates:
$$H \cap G = (M \cap H \cap G) \cup (M^c \cap H \cap G)$$
Since these two sets are disjoint:
$$n(H \cap G) = n(M \cap H \cap G) + n(M^c \cap H \cap G)$$
Rearranging gives:
$$n(M^c \cap H \cap G) = n(H \cap G) - n(M \cap H \cap G)$$
Substituting the given values:
$$n(M^c \cap H \cap G) = 151 - 72 = \mathbf{79}$$

$$\mathbf{\text{Ans: (1) } 54 \text{ single non-graduate women}, \quad \text{(2) } 79 \text{ married graduate women}}$$

---

### Problem 2.5: Two Dice Sum or First Face Condition
*(Ref: Question Bank Q.82 | MHU Sheet Lec 7-10, Problem-3)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Two unbiased dice are thrown once. Find the probability that:
1. The sum of the upper faces is $8$ or the first selected die bears the number $4$.
2. Both dice show the same number.

---

#### Detailed Solution:

Total sample space: $n(S) = 6 \times 6 = 36$.

#### 1. Sum of faces is 8 or first die shows 4:
Let:
- Event $A$: Sum of faces equals $8$.  
  $$A = \{(2,6), (3,5), (4,4), (5,3), (6,2)\} \implies n(A) = 5$$
- Event $B$: First die shows $4$.  
  $$B = \{(4,1), (4,2), (4,3), (4,4), (4,5), (4,6)\} \implies n(B) = 6$$
- Event $A \cap B$: Sum is $8$ AND first die is $4$:
  $$A \cap B = \{(4,4)\} \implies n(A \cap B) = 1$$

Applying the Addition Theorem for non-mutually exclusive events:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{5}{36} + \frac{6}{36} - \frac{1}{36} = \frac{10}{36} = \frac{5}{18} \approx 0.2778$$

---

#### 2. Both dice show the same number (Doubles):
Let Event $C$ be getting the same number on both dice:
$$C = \{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\} \implies n(C) = 6$$
$$P(C) = \frac{n(C)}{n(S)} = \frac{6}{36} = \frac{1}{6} \approx 0.1667$$

$$\mathbf{\text{Ans: (1) } \frac{5}{18}, \quad \text{(2) } \frac{1}{6}}$$

---

### Problem 2.6: Probability of Not Getting 7 or 11 on Pair of Dice
*(Ref: Question Bank Q.67, Q.81 | Pg 6, Q.6(b), MHU Sheet Lec 7-10 Problem-2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
1. If a pair of fair dice is thrown once, find the probability that the sum is neither $7$ nor $11$.
2. Find the probability of not getting a $7$ or $11$ total on **either of two tosses** of a pair of fair dice.

---

#### Detailed Solution:

Let $S$ be the sample space of rolling two dice: $n(S) = 36$.

**Step 1: Identify outcomes giving a sum of 7 or 11.**  
- Outcomes with sum $= 7$:
  $$E_7 = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\} \implies n(E_7) = 6$$
- Outcomes with sum $= 11$:
  $$E_{11} = \{(5,6), (6,5)\} \implies n(E_{11}) = 2$$
- Since $E_7$ and $E_{11}$ are mutually exclusive:
  $$n(E_7 \cup E_{11}) = 6 + 2 = 8$$
  $$P(\text{Sum is 7 or 11}) = \frac{8}{36} = \frac{2}{9}$$

---

#### 1. Single Toss: Sum is Neither 7 Nor 11:
Using the complement rule:
$$P(\text{Neither 7 nor 11}) = 1 - P(\text{Sum is 7 or 11}) = 1 - \frac{2}{9} = \mathbf{\frac{7}{9}} \approx 0.7778$$

---

#### 2. Two Consecutive Independent Tosses:
Let $T_1$ and $T_2$ be the events of not getting 7 or 11 in toss 1 and toss 2 respectively.  
Since the two tosses are statistically independent:
$$P(\text{Neither 7 nor 11 on either toss}) = P(T_1 \cap T_2) = P(T_1) \cdot P(T_2)$$
$$P(T_1 \cap T_2) = \frac{7}{9} \times \frac{7}{9} = \mathbf{\frac{49}{81}} \approx 0.6049 \quad (60.49\%)$$

$$\mathbf{\text{Ans: (1) } \frac{7}{9} \approx 0.7778, \quad \text{(2) } \frac{49}{81} \approx 0.6049}$$

---


## 3. Independent Events, Dependent Events & Multiplicative Law

### Question 3.1: Independent vs. Dependent Events
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Core Theoretical Definitions)*
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

### Theorem 3.2: Formal Statement & Proof of Multiplication Law (Compound Probability)
*(Ref: Question Bank Q.79 | MHU Sheet Lec 7-10, Theorem-4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**State and prove the Multiplication Law (Compound Probability Theorem) for two dependent events and extend the result for $n$ events.**

---

#### Detailed Proof:

#### 1. For Two Events:
Let $S$ be a finite sample space with $n$ equally likely, mutually exclusive outcomes.  
Let $n(A)$ be the number of outcomes favorable to event $A$, $n(B)$ be favorable to $B$, and $n(A \cap B)$ be favorable to both $A$ and $B$.

By the classical definition of probability:
$$P(A) = \frac{n(A)}{n}, \quad P(A \cap B) = \frac{n(A \cap B)}{n}$$

Now, if we are given that event $A$ has already occurred, the effective sample space reduces from $S$ to $A$ (which contains $n(A)$ sample points). Among these $n(A)$ outcomes, the outcomes favorable to event $B$ are precisely those outcomes in $A \cap B$.  
Therefore, the conditional probability of $B$ given $A$ is:
$$P(B | A) = \frac{n(A \cap B)}{n(A)}$$

Multiplying and dividing by $n$:
$$P(B | A) = \frac{\frac{n(A \cap B)}{n}}{\frac{n(A)}{n}} = \frac{P(A \cap B)}{P(A)}$$

Multiplying both sides by $P(A)$ (assuming $P(A) > 0$):
$$P(A \cap B) = P(A) \cdot P(B | A)$$

By symmetry, if event $B$ has already occurred ($P(B) > 0$):
$$P(A \cap B) = P(B) \cdot P(A | B)$$
*(Hence proved).*

#### 2. Extension to $n$ Events:
For $n$ dependent events $A_1, A_2, \dots, A_n$:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) \cdot P(A_2 | A_1) \cdot P(A_3 | A_1 \cap A_2) \dots P(A_n | A_1 \cap A_2 \cap \dots \cap A_{n-1})$$

---

### Problem 3.3: Successive Ball Drawing (With and Without Replacement)
*(Ref: Note Problem 3.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 3.2)*
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
The events $W_1$ and $W_2$ are independent:
$$P(W_1) = \frac{4}{9}, \quad P(W_2|W_1) = P(W_2) = \frac{4}{9}$$
$$P(W_1 \cap W_2) = P(W_1) \cdot P(W_2) = \frac{4}{9} \times \frac{4}{9} = \frac{16}{81} \approx 0.1975$$

#### Case (ii): Without Replacement
The second draw depends on the first:
$$P(W_1) = \frac{4}{9}, \quad P(W_2 | W_1) = \frac{3}{8}$$
$$P(W_1 \cap W_2) = P(W_1) \cdot P(W_2 | W_1) = \frac{4}{9} \times \frac{3}{8} = \frac{12}{72} = \frac{1}{6} \approx 0.1667$$

$$\mathbf{\text{Ans: (i) } \frac{16}{81} \approx 0.1975, \quad \text{(ii) } \frac{1}{6} \approx 0.1667}$$

---

### Problem 3.4: Tulip Bulbs Selection With and Without Replacement
*(Ref: Question Bank Q.65 | Pg 4, Q.6(b))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A bag of $30$ tulip bulbs contains:
- $12$ Red bulbs
- $10$ Yellow bulbs
- $8$ Purple bulbs

Two bulbs are selected at random. What is the probability that:
1. Two randomly selected tulip bulbs are both red?
2. The first bulb selected is red and the second is yellow?
3. One bulb is red and the other is purple?  
Calculate all three probabilities for:
**(a) With replacement**  
**(b) Without replacement**

---

#### Detailed Solution:

Total bulbs $= 12 + 10 + 8 = 30$.

#### (a) With Replacement (Independent Draws):

1. **Both are red ($R_1 \cap R_2$):**
   $$P(R_1) = \frac{12}{30} = \frac{2}{5}, \quad P(R_2) = \frac{12}{30} = \frac{2}{5}$$
   $$P(R_1 \cap R_2) = \frac{2}{5} \times \frac{2}{5} = \mathbf{\frac{4}{25} = 0.16} \quad (16\%)$$

2. **First is red and second is yellow ($R_1 \cap Y_2$):**
   $$P(R_1) = \frac{12}{30} = \frac{2}{5}, \quad P(Y_2) = \frac{10}{30} = \frac{1}{3}$$
   $$P(R_1 \cap Y_2) = \frac{2}{5} \times \frac{1}{3} = \mathbf{\frac{2}{15} \approx 0.1333} \quad (13.33\%)$$

3. **One bulb is red and the other is purple:**  
   Order is unspecified, so this can occur as $(R_1 \cap P_2)$ or $(P_1 \cap R_2)$:
   $$P(R_1 \cap P_2) = \frac{12}{30} \times \frac{8}{30} = \frac{2}{5} \times \frac{4}{15} = \frac{8}{75}$$
   $$P(P_1 \cap R_2) = \frac{8}{30} \times \frac{12}{30} = \frac{4}{15} \times \frac{2}{5} = \frac{8}{75}$$
   $$P(\text{One Red, One Purple}) = \frac{8}{75} + \frac{8}{75} = \mathbf{\frac{16}{75} \approx 0.2133} \quad (21.33\%)$$

---

#### (b) Without Replacement (Dependent Draws):

1. **Both are red ($R_1 \cap R_2$):**
   $$P(R_1) = \frac{12}{30} = \frac{2}{5}$$
   After drawing 1 red bulb, $11$ red bulbs remain out of $29$:
   $$P(R_2 | R_1) = \frac{11}{29}$$
   $$P(R_1 \cap R_2) = \frac{2}{5} \times \frac{11}{29} = \mathbf{\frac{22}{145} \approx 0.1517} \quad (15.17\%)$$

2. **First is red and second is yellow ($R_1 \cap Y_2$):**
   $$P(R_1) = \frac{12}{30} = \frac{2}{5}$$
   All $10$ yellow bulbs remain out of $29$:
   $$P(Y_2 | R_1) = \frac{10}{29}$$
   $$P(R_1 \cap Y_2) = \frac{2}{5} \times \frac{10}{29} = \mathbf{\frac{20}{145} = \frac{4}{29} \approx 0.1379} \quad (13.79\%)$$

3. **One bulb is red and the other is purple:**  
   Using combinations directly:
   $$P(\text{One Red, One Purple}) = \frac{\binom{12}{1} \binom{8}{1}}{\binom{30}{2}} = \frac{12 \times 8}{\frac{30 \times 29}{2}} = \frac{96}{435} = \mathbf{\frac{32}{145} \approx 0.2207} \quad (22.07\%)$$

---

### Problem 3.5: Successive Drawings of 3 Balls
*(Ref: Question Bank Q.66 | Pg 6, Q.6(a))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A bag contains $8$ red and $5$ white balls (total $13$ balls). Successive drawings of $3$ balls are made. Find the probability that the first drawing will give $3$ white balls and the second drawing will give $3$ red balls when:
1. Balls are replaced before the next drawing (with replacement).
2. Balls are not replaced before the next drawing (without replacement).

---

#### Detailed Solution:

Total balls in bag $= 8 + 5 = 13$.  
Number of ways to draw $3$ balls from $13$:
$$\binom{13}{3} = \frac{13 \times 12 \times 11}{3 \times 2 \times 1} = 286$$

Let:
- Event $A$ = first drawing gives $3$ white balls.
- Event $B$ = second drawing gives $3$ red balls.

For the first draw:
$$P(A) = \frac{\binom{5}{3}}{\binom{13}{3}} = \frac{10}{286} = \frac{5}{143}$$

---

#### Case 1: With Replacement
Since the $3$ white balls are replaced before the second trial, the composition of the bag is restored to $8$ red and $5$ white:
$$P(B | A) = P(B) = \frac{\binom{8}{3}}{\binom{13}{3}} = \frac{56}{286} = \frac{28}{143}$$

By independence:
$$P(A \cap B) = P(A) \cdot P(B) = \frac{5}{143} \times \frac{28}{143} = \mathbf{\frac{140}{20449} \approx 0.006846} \quad (0.685\%)$$

---

#### Case 2: Without Replacement
The $3$ white balls are not returned.  
Remaining balls for the second draw: $8$ red and $5 - 3 = 2$ white (total $10$ balls).  
The number of ways to draw $3$ balls from the remaining $10$ is:
$$\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$$

The conditional probability of drawing $3$ red balls is:
$$P(B | A) = \frac{\binom{8}{3}}{\binom{10}{3}} = \frac{56}{120} = \frac{7}{15}$$

Applying the multiplication law for dependent events:
$$P(A \cap B) = P(A) \cdot P(B | A) = \frac{5}{143} \times \frac{7}{15} = \frac{1 \times 7}{143 \times 3} = \mathbf{\frac{7}{429} \approx 0.016317} \quad (1.632\%)$$

$$\mathbf{\text{Ans: (1) With replacement: } \frac{140}{20449} \approx 0.00685, \quad \text{(2) Without replacement: } \frac{7}{429} \approx 0.01632}$$

---

### Problem 3.6: Resistors in an Assembly Parts Bin
*(Ref: Question Bank Q.71 | Pg 14, CT-03, Q.2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A parts-bin contains discrete electronic components of three tolerance classes:
- Type R: $7$ resistors of tolerance class R
- Type W: $12$ resistors of tolerance class W
- Type G: $4$ resistors of tolerance class G

You randomly pick $3$ components from the bin without replacement to populate a 3-component subassembly.
1. What is the probability that all three selected components are of tolerance class W?
2. What is the probability that the subassembly ends up with one resistor of each tolerance class (R, W, G)?

---

#### Detailed Solution:

Total components in the bin:
$$N = 7 + 12 + 4 = 23 \text{ resistors}$$
Total ways to pick $3$ resistors without replacement:
$$n(S) = \binom{23}{3} = \frac{23 \times 22 \times 21}{3 \times 2 \times 1} = 23 \times 11 \times 7 = 1771$$

---

#### 1. All Three Components Are of Tolerance Class W:
We choose all $3$ resistors from the $12$ class W resistors:
$$n(\text{All W}) = \binom{12}{3} = \frac{12 \times 11 \times 10}{6} = 220$$
$$P(\text{All W}) = \frac{\binom{12}{3}}{\binom{23}{3}} = \frac{220}{1771} = \mathbf{\frac{20}{161} \approx 0.1242} \quad (12.42\%)$$

---

#### 2. One Resistor of Each Tolerance Class (R, W, G):
We select $1$ from Type R ($7$), $1$ from Type W ($12$), and $1$ from Type G ($4$):
$$n(1R, 1W, 1G) = \binom{7}{1} \times \binom{12}{1} \times \binom{4}{1} = 7 \times 12 \times 4 = 336$$
$$P(1R, 1W, 1G) = \frac{336}{1771} = \mathbf{\frac{48}{253} \approx 0.1897} \quad (18.97\%)$$

$$\mathbf{\text{Ans: (1) } \frac{20}{161} \approx 0.1242, \quad \text{(2) } \frac{48}{253} \approx 0.1897}$$

---

### Problem 3.7: Consecutive Card Draws Without Replacement
*(Ref: Question Bank Q.72 | Pg 16, CT 03, Q.2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A card is drawn from a standard pack of $52$ playing cards and then another card is drawn without the first being replaced. What is the probability of drawing:
1. Two aces?
2. Two spades?

---

#### Detailed Solution:

Total cards in standard deck $= 52$.

#### 1. Probability of Drawing Two Aces:
In a standard deck, there are $4$ aces.
- Probability the first card is an ace: $P(A_1) = \frac{4}{52} = \frac{1}{13}$.
- After an ace is drawn without replacement, $3$ aces remain in $51$ cards:
  $$P(A_2 | A_1) = \frac{3}{51} = \frac{1}{17}$$
- Applying the multiplication rule:
  $$P(A_1 \cap A_2) = P(A_1) \cdot P(A_2 | A_1) = \frac{1}{13} \times \frac{1}{17} = \mathbf{\frac{1}{221} \approx 0.004525} \quad (0.452\%)$$

---

#### 2. Probability of Drawing Two Spades:
In a standard deck, there are $13$ spades.
- Probability the first card is a spade: $P(S_1) = \frac{13}{52} = \frac{1}{4}$.
- After a spade is drawn, $12$ spades remain in $51$ cards:
  $$P(S_2 | S_1) = \frac{12}{51} = \frac{4}{17}$$
- Applying the multiplication rule:
  $$P(S_1 \cap S_2) = P(S_1) \cdot P(S_2 | S_1) = \frac{1}{4} \times \frac{4}{17} = \mathbf{\frac{1}{17} \approx 0.05882} \quad (5.88\%)$$

$$\mathbf{\text{Ans: (1) } \frac{1}{221} \approx 0.00452, \quad \text{(2) } \frac{1}{17} \approx 0.05882}$$

---

### Problem 3.8: Box with Colored Balls (Sampling Combinations & Sequence Order)
*(Ref: Question Bank Q.74, Q.85 | Pg 20 Class Test-2 Q2, MHU Sheet Lec 7-10 Problem-6)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A box contains $8$ red, $3$ blue, and $9$ green balls (total $20$ balls). Three balls are drawn at random from the box. Find the probability that:
1. All $3$ are red.
2. At least $1$ is blue.
3. One of each color is drawn.
4. The balls are drawn in the specific order: Red, Blue, and Green.

---

#### Detailed Solution:

Total balls $= 8 + 3 + 9 = 20$.  
Total number of ways to draw $3$ balls from $20$:
$$n(S) = \binom{20}{3} = \frac{20 \times 19 \times 18}{3 \times 2 \times 1} = 1140$$

---

#### 1. All 3 are Red:
Choose all $3$ balls from the $8$ red balls:
$$P(\text{All 3 Red}) = \frac{\binom{8}{3}}{\binom{20}{3}} = \frac{56}{1140} = \mathbf{\frac{14}{285} \approx 0.04912} \quad (4.91\%)$$

---

#### 2. At Least 1 is Blue:
Using the complement rule:
$$P(\text{At least 1 Blue}) = 1 - P(\text{No Blue balls drawn})$$
Drawing $0$ blue balls means all $3$ balls come from the $8 + 9 = 17$ non-blue balls:
$$P(\text{No Blue}) = \frac{\binom{17}{3}}{\binom{20}{3}} = \frac{\frac{17 \times 16 \times 15}{6}}{1140} = \frac{680}{1140} = \frac{34}{57}$$
$$P(\text{At least 1 Blue}) = 1 - \frac{34}{57} = \mathbf{\frac{23}{57} \approx 0.4035} \quad (40.35\%)$$

---

#### 3. One of Each Color (1 Red, 1 Blue, 1 Green):
Choose $1$ red from $8$, $1$ blue from $3$, and $1$ green from $9$:
$$n(1R, 1B, 1G) = \binom{8}{1} \times \binom{3}{1} \times \binom{9}{1} = 8 \times 3 \times 9 = 216$$
$$P(1R, 1B, 1G) = \frac{216}{1140} = \mathbf{\frac{18}{95} \approx 0.18947} \quad (18.95\%)$$

---

#### 4. Drawn in the Specific Order: Red, Blue, then Green:
Using the conditional multiplication rule step-by-step:
- 1st ball Red: $P(R_1) = \frac{8}{20} = \frac{2}{5}$
- 2nd ball Blue: $P(B_2 | R_1) = \frac{3}{19}$
- 3rd ball Green: $P(G_3 | R_1 \cap B_2) = \frac{9}{18} = \frac{1}{2}$

$$P(R_1 \cap B_2 \cap G_3) = \frac{2}{5} \times \frac{3}{19} \times \frac{1}{2} = \frac{3}{95} \approx 0.031579$$
*(Notice: $P(1R, 1B, 1G) / 3! = \frac{18/95}{6} = \frac{3}{95}$, perfectly matching the $3! = 6$ possible draw orders).*

$$\mathbf{\text{Ans: (1) } \frac{14}{285}, \quad \text{(2) } \frac{23}{57}, \quad \text{(3) } \frac{18}{95}, \quad \text{(4) } \frac{3}{95}}$$

---

### Problem 3.9: Green & Red Dice Sample Space & Event Algebra
*(Ref: Question Bank Q.80, Q.83 | MHU Sheet Lec 7-10, Problem-1 & Problem-4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Two dice, one green and the other red, are thrown simultaneously.  
Let $A$ be the event that the sum of the points on the faces shown is odd.  
Let $B$ be the event that at least one face shows the number '$1$'.
1. Describe the complete sample space $S$ and state its size $n(S)$.
2. Describe events $A, B, \bar{B}, A \cap B, A \cup B, A \cap \bar{B}$ and calculate their probabilities.
3. Find the probabilities: (i) $P(\bar{A} \cup \bar{B})$, (ii) $P(\bar{A} \cap \bar{B})$, (iii) $P(A|B)$, (iv) $P(B|A)$, and (v) $P(\bar{A}|\bar{B})$.

---

#### Detailed Solution:

Let an outcome be written as the ordered pair $(g, r)$, where $g \in \{1,2,3,4,5,6\}$ is the number on the green die and $r \in \{1,2,3,4,5,6\}$ is the number on the red die.

#### 1. Complete Sample Space ($S$):
$$S = \{(g, r) : g \in \{1, 2, 3, 4, 5, 6\}, r \in \{1, 2, 3, 4, 5, 6\}\}$$
$$n(S) = 6 \times 6 = 36$$

---

#### 2. Event Descriptions & Probabilities:

- **Event $A$ (Sum is odd):**  
  The sum $g + r$ is odd when one die is even and the other is odd:
  - Green odd ($1, 3, 5$) and Red even ($2, 4, 6$): $3 \times 3 = 9$ outcomes.
  - Green even ($2, 4, 6$) and Red odd ($1, 3, 5$): $3 \times 3 = 9$ outcomes.
  $$n(A) = 9 + 9 = 18 \implies P(A) = \frac{18}{36} = \frac{1}{2} = 0.50$$

- **Event $B$ (At least one die shows '1'):**  
  $$B = \{(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (2,1), (3,1), (4,1), (5,1), (6,1)\}$$
  $$n(B) = 11 \implies P(B) = \frac{11}{36} \approx 0.3056$$

- **Event $\bar{B}$ (Neither die shows '1'):**  
  All outcomes where both dice show values from $\{2, 3, 4, 5, 6\}$:
  $$n(\bar{B}) = 5 \times 5 = 25 \implies P(\bar{B}) = 1 - P(B) = \frac{25}{36} \approx 0.6944$$

- **Event $A \cap B$ (Sum is odd AND at least one die shows '1'):**  
  Since one die shows $1$ (an odd number), the sum is odd if and only if the other die shows an **even number** ($2, 4, 6$):
  $$A \cap B = \{(1,2), (1,4), (1,6), (2,1), (4,1), (6,1)\}$$
  $$n(A \cap B) = 6 \implies P(A \cap B) = \frac{6}{36} = \frac{1}{6} \approx 0.1667$$

- **Event $A \cup B$ (Sum is odd OR at least one die shows '1'):**  
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{18}{36} + \frac{11}{36} - \frac{6}{36} = \frac{23}{36} \approx 0.6389$$

- **Event $A \cap \bar{B}$ (Sum is odd AND neither die is '1'):**  
  $$P(A \cap \bar{B}) = P(A) - P(A \cap B) = \frac{18}{36} - \frac{6}{36} = \frac{12}{36} = \frac{1}{3} \approx 0.3333$$

---

#### 3. Compound & Conditional Probabilities:

- **(i) $P(\bar{A} \cup \bar{B})$:**  
  By De Morgan's Law, $\bar{A} \cup \bar{B} = \overline{A \cap B}$:
  $$P(\bar{A} \cup \bar{B}) = 1 - P(A \cap B) = 1 - \frac{1}{6} = \mathbf{\frac{5}{6} \approx 0.8333}$$

- **(ii) $P(\bar{A} \cap \bar{B})$:**  
  By De Morgan's Law, $\bar{A} \cap \bar{B} = \overline{A \cup B}$:
  $$P(\bar{A} \cap \bar{B}) = 1 - P(A \cup B) = 1 - \frac{23}{36} = \mathbf{\frac{13}{36} \approx 0.3611}$$

- **(iii) Conditional Probability $P(A|B)$:**
  $$P(A | B) = \frac{P(A \cap B)}{P(B)} = \frac{6/36}{11/36} = \mathbf{\frac{6}{11} \approx 0.5455}$$

- **(iv) Conditional Probability $P(B|A)$:**
  $$P(B | A) = \frac{P(A \cap B)}{P(A)} = \frac{6/36}{18/36} = \mathbf{\frac{6}{18} = \frac{1}{3} \approx 0.3333}$$

- **(v) Conditional Probability $P(\bar{A}|\bar{B})$:**
  $$P(\bar{A} | \bar{B}) = \frac{P(\bar{A} \cap \bar{B})}{P(\bar{B})} = \frac{13/36}{25/36} = \mathbf{\frac{13}{25} = 0.52} \quad (52\%)$$

---


## 4. Bayes' Theorem & Applications

### Theorem 4.1: Statement & Proof of Bayes' Theorem
*(Ref: Question Bank Q.86 | MHU Sheet Lec 7-10, Theorem-5)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Core Theoretical Theorem)*
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
*(Ref: Note Problem 4.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Partition Problem)*
**Problem Statement:**  
There are two identical boxes containing balls as follows:
- **Box 1:** $4$ white and $3$ red balls (total $7$ balls)
- **Box 2:** $3$ white and $7$ red balls (total $10$ balls)

A box is chosen at random and a ball is drawn at random from it. If the ball drawn is found to be white, what is the probability that it was drawn from the first box?

---

#### Detailed Solution:
- Prior: $P(B_1) = 1/2, P(B_2) = 1/2$.
- Likelihoods: $P(W | B_1) = 4/7, P(W | B_2) = 3/10$.
- Total Probability:
  $$P(W) = P(B_1)P(W|B_1) + P(B_2)P(W|B_2) = \frac{1}{2}\left(\frac{4}{7} + \frac{3}{10}\right) = \frac{1}{2}\left(\frac{40 + 21}{70}\right) = \frac{61}{140}$$
- Bayes' Theorem:
  $$P(B_1 | W) = \frac{\frac{1}{2} \times \frac{4}{7}}{\frac{61}{140}} = \frac{\frac{2}{7}}{\frac{61}{140}} = \frac{2}{7} \times \frac{140}{61} = \mathbf{\frac{40}{61} \approx 0.6557}$$

---

### Problem 4.3: Bolt Factory Defective Bolts (Three Machines)
*(Ref: Note Problem 4.3)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Quality Control Problem)*
**Problem Statement:**  
In a bolt factory, machines $A, B$, and $C$ manufacture respectively $25\%$, $35\%$, and $40\%$ of the total output. Of their output, $5\%$, $4\%$, and $2\%$ respectively are defective bolts. A bolt is drawn at random from the total product and is found to be defective. What is the probability that it was manufactured by machine $B$?

---

#### Detailed Solution:
- Priors: $P(E_A) = 0.25, P(E_B) = 0.35, P(E_C) = 0.40$.
- Likelihoods: $P(D|E_A) = 0.05, P(D|E_B) = 0.04, P(D|E_C) = 0.02$.
- Total Probability $P(D)$:
  $$P(D) = 0.25(0.05) + 0.35(0.04) + 0.40(0.02) = 0.0125 + 0.0140 + 0.0080 = 0.0345$$
- Bayes' Theorem for Machine $B$:
  $$P(E_B | D) = \frac{0.35 \times 0.04}{0.0345} = \frac{0.0140}{0.0345} = \frac{140}{345} = \mathbf{\frac{28}{69} \approx 0.4058}$$

---

### Problem 4.4: University Students Financial Status & Statistics Excellence
*(Ref: Question Bank Q.87 | MHU Sheet Lec 7-10, Problem-7)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Among the students of a certain university:
- $50\%$ are poor
- $30\%$ are solvent
- $20\%$ are rich

It is observed that $30\%$ of the poor students, $60\%$ of the solvent students, and $10\%$ of the rich students are excellent in statistics.  
A student selected at random is found to be excellent in statistics. What is the probability that the selected student is **solvent**?

---

#### Detailed Solution:

Let the three categories of students partition the student population:
- $B_1$ = student is poor $\implies P(B_1) = 50\% = 0.50$
- $B_2$ = student is solvent $\implies P(B_2) = 30\% = 0.30$
- $B_3$ = student is rich $\implies P(B_3) = 20\% = 0.20$
*(Check: $0.50 + 0.30 + 0.20 = 1.00$)*

Let $A$ be the event that a student is excellent in statistics.  
The conditional probabilities (likelihoods) are:
- $P(A | B_1) = 30\% = 0.30$
- $P(A | B_2) = 60\% = 0.60$
- $P(A | B_3) = 10\% = 0.10$

**Step 1: Compute Total Probability of an Excellent Student, $P(A)$.**  
Using the Law of Total Probability:
$$P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) + P(B_3)P(A|B_3)$$
$$P(A) = (0.50 \times 0.30) + (0.30 \times 0.60) + (0.20 \times 0.10)$$
$$P(A) = 0.15 + 0.18 + 0.02 = 0.35$$

**Step 2: Apply Bayes' Theorem for Solvent Students ($B_2$).**  
$$P(B_2 | A) = \frac{P(B_2) \cdot P(A | B_2)}{P(A)}$$
$$P(B_2 | A) = \frac{0.30 \times 0.60}{0.35} = \frac{0.18}{0.35} = \frac{18}{35} \approx 0.514286$$

$$\mathbf{P(\text{Solvent} | \text{Excellent}) = \frac{18}{35} \approx 0.5143 \quad (51.43\%)}$$

---

### Problem 4.5: Factory Output and Defective Parts Produced by Machines
*(Ref: Question Bank Q.88 | MHU Sheet Lec 7-10, Problem-8)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
In a factory, machine $A$ produces $60\%$ of the total daily output, and machine $B$ produces the rest. It is known that $1\%$ of the output of machine $A$ is defective, and $2\%$ of the output of machine $B$ is defective.  
An item is selected at random from a day's output and is found to be defective. What is the probability that the defective item was produced by **machine $B$**?

---

#### Detailed Solution:

Let:
- $E_A$ = event that the item was produced by Machine $A$
- $E_B$ = event that the item was produced by Machine $B$
- $D$ = event that the chosen item is defective

**Step 1: Identify Prior Probabilities.**  
$$P(E_A) = 60\% = 0.60$$
$$P(E_B) = 100\% - 60\% = 40\% = 0.40$$

**Step 2: Identify Likelihoods (Defect rates).**  
$$P(D | E_A) = 1\% = 0.01$$
$$P(D | E_B) = 2\% = 0.02$$

**Step 3: Determine Total Probability of a Defective Item, $P(D)$.**  
$$P(D) = P(E_A)P(D|E_A) + P(E_B)P(D|E_B)$$
$$P(D) = (0.60 \times 0.01) + (0.40 \times 0.02) = 0.006 + 0.008 = 0.014$$

**Step 4: Apply Bayes' Theorem for Machine $B$.**  
$$P(E_B | D) = \frac{P(E_B) \cdot P(D | E_B)}{P(D)}$$
$$P(E_B | D) = \frac{0.40 \times 0.02}{0.014} = \frac{0.008}{0.014} = \frac{8}{14} = \mathbf{\frac{4}{7}} \approx 0.571429$$

$$\mathbf{P(\text{Machine } B | \text{Defective}) = \frac{4}{7} \approx 0.5714 \quad (57.14\%)}$$

---


## 5. Discrete Random Variables & Probability Mass Functions (PMF)

### Question 5.1: Definition & Conditions for a PMF
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Core PMF Criteria)*
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
*(Ref: Note Problem 5.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational PMF Verification)*
**Problem Statement:**  
Check whether the following functions can serve as valid probability mass functions:
1. $f(x) = \frac{2x - 1}{8}, \quad x = 0, 1, 2, 3$
2. $f(x) = \frac{x + 1}{16}, \quad x = 0, 1, 2, 3$
3. $f(x) = \frac{3x + 6}{21}, \quad x = 1, 2$

---

#### Detailed Solution:

#### Case (i): $f(x) = \frac{2x - 1}{8}, \quad x \in \{0, 1, 2, 3\}$
- At $x = 0$: $f(0) = -1/8 < 0$.  
- **Conclusion:** Violates non-negativity ($f(x) \ge 0$). **Not a valid PMF.**

#### Case (ii): $f(x) = \frac{x + 1}{16}, \quad x \in \{0, 1, 2, 3\}$
- Check sum: $\sum_{x=0}^3 f(x) = \frac{1}{16} + \frac{2}{16} + \frac{3}{16} + \frac{4}{16} = \frac{10}{16} = \frac{5}{8} \ne 1$.  
- **Conclusion:** Violates unit sum condition. **Not a valid PMF.**

#### Case (iii): $f(x) = \frac{3x + 6}{21}, \quad x \in \{1, 2\}$
- $f(1) = 9/21 > 0, \quad f(2) = 12/21 > 0$.
- $\sum f(x) = \frac{9}{21} + \frac{12}{21} = \frac{21}{21} = 1$.  
- **Conclusion:** Satisfies both conditions. **Is a valid PMF.**

---

### Problem 5.3: Geometric-Type Discrete Distribution
*(Ref: Note Problem 5.3)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Discrete Distribution)*
**Problem Statement:**  
The PMF of a discrete random variable $X$ is defined as:
$$f(x) = \begin{cases} k \left(\frac{3}{4}\right)^x, & x = 0, 1, 2, 3, \dots, \infty \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the value of constant $k$.
2. Compute $P(X \le 3)$.

---

#### Detailed Solution:

#### 1. Find $k$:
$$\sum_{x=0}^{\infty} k \left(\frac{3}{4}\right)^x = 1 \implies k \times \frac{1}{1 - 3/4} = 4k = 1 \implies \mathbf{k = \frac{1}{4}}$$

#### 2. Compute $P(X \le 3)$:
$$P(X \le 3) = \frac{1}{4}\left[1 + \frac{3}{4} + \frac{9}{16} + \frac{27}{64}\right] = \frac{1}{4}\left[\frac{64 + 48 + 36 + 27}{64}\right] = \frac{1}{4} \times \frac{175}{64} = \mathbf{\frac{175}{256} \approx 0.6836}$$

---

### Problem 5.4: Tabular Discrete Distribution
*(Ref: Note Problem 5.4)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Tabular PMF Problem)*
**Problem Statement:**  
The probability distribution of a discrete random variable $Y$ is given by:

| $y$ | -3 | -2 | -1 | 0 | 1 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $f(y)$ | $0.10$ | $0.25$ | $0.30$ | $0.15$ | $k$ |

1. Find the value of $k$.
2. Find $P(-3 < Y < 0)$.
3. Find $P(Y \ge -1)$.

---

#### Detailed Solution:
1. $0.10 + 0.25 + 0.30 + 0.15 + k = 1 \implies 0.80 + k = 1 \implies \mathbf{k = 0.20}$.
2. $P(-3 < Y < 0) = f(-2) + f(-1) = 0.25 + 0.30 = \mathbf{0.55}$.
3. $P(Y \ge -1) = f(-1) + f(0) + f(1) = 0.30 + 0.15 + 0.20 = \mathbf{0.65}$.

---


## 6. Continuous Random Variables & Probability Density Functions (PDF)

### Question 6.1: Definition & Conditions for a PDF
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Core PDF Criteria)*
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
*(Ref: Note Problem 6.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Calculus PDF Problem)*
**Problem Statement:**  
Check whether the function $f(x) = 6x(1-x), \quad 0 \le x \le 1$ (and $0$ elsewhere) is a valid probability density function.

---

#### Detailed Solution:
- On $[0, 1]$, $x \ge 0$ and $1 - x \ge 0$, so $f(x) \ge 0$.
- Integral check:
  $$\int_0^1 6x(1-x) dx = 6 \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = 6 \left(\frac{1}{2} - \frac{1}{3}\right) = 6 \times \frac{1}{6} = 1$$
Since both conditions are satisfied, $f(x)$ is a valid PDF.

---

### Problem 6.3: Continuous PDF $f(x) = kx$
*(Ref: Note Problem 6.3)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational Normalization Problem)*
**Problem Statement:**  
The PDF of a continuous random variable $X$ is $f(x) = kx$ for $0 < x < 4$ ($0$ elsewhere).  
Find $k$, $P(1 < X < 2)$, and $P(2 < X < 4)$.

---

#### Detailed Solution:
1. $\int_0^4 kx dx = k [x^2/2]_0^4 = 8k = 1 \implies \mathbf{k = \frac{1}{8}}$.
2. $P(1 < X < 2) = \int_1^2 \frac{1}{8}x dx = \frac{1}{16}[4 - 1] = \mathbf{\frac{3}{16} \approx 0.1875}$.
3. $P(2 < X < 4) = \int_2^4 \frac{1}{8}x dx = \frac{1}{16}[16 - 4] = \frac{12}{16} = \mathbf{\frac{3}{4} = 0.75}$.

---

### Problem 6.4: Continuous PDF $f(x) = k(1+x)$
*(Ref: Note Problem 6.4)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Foundational PDF Problem)*
**Problem Statement:**  
Given $f(x) = k(1+x)$ for $2 < x < 5$ ($0$ elsewhere). Find $k$, $P(3 < X < 4)$, and $P(X < 4)$.

---

#### Detailed Solution:
1. $\int_2^5 k(1+x) dx = k [x + x^2/2]_2^5 = k [35/2 - 4] = \frac{27}{2}k = 1 \implies \mathbf{k = \frac{2}{27}}$.
2. $P(3 < X < 4) = \frac{2}{27} [x + x^2/2]_3^4 = \frac{2}{27}[12 - 15/2] = \frac{2}{27}(9/2) = \mathbf{\frac{1}{3} \approx 0.3333}$.
3. $P(X < 4) = \int_2^4 \frac{2}{27}(1+x) dx = \frac{2}{27}[12 - 4] = \mathbf{\frac{16}{27} \approx 0.5926}$.

---

### Problem 6.5: Electric Cable Diameter — Mean and Median
*(Ref: Question Bank Q.90, Q.111, Q.116, Q.268 | Pg 1, Q.6(b), Pg 19 Class Test-2 Q2, MHU Sheet Lec 7-10 Problem-15)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The diameter of an electric cable, say $X$, is assumed to be a continuous random variable with probability density function:
$$f(x) = \begin{cases} 6x(1-x), & 0 \le x \le 1 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the mean of $X$.
2. Determine a number $b$ such that $P(X < b) = P(X > b)$ (i.e. the median).

---

#### Detailed Solution:

#### 1. Mean of $X$:
By definition of mathematical expectation for a continuous random variable:
$$E(X) = \mu = \int_{-\infty}^{\infty} x f(x) \, dx$$
$$E(X) = \int_{0}^{1} x \cdot 6x(1 - x) \, dx = 6 \int_{0}^{1} (x^2 - x^3) \, dx$$
Evaluating the definite integral:
$$E(X) = 6 \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_0^1 = 6 \left( \frac{1}{3} - \frac{1}{4} \right) = 6 \left( \frac{4 - 3}{12} \right) = 6 \times \frac{1}{12} = \mathbf{\frac{1}{2} = 0.5}$$

---

#### 2. Determine the Number $b$ such that $P(X < b) = P(X > b)$:
Since the total probability equals $1$:
$$P(X < b) + P(X > b) = 1$$
Given that $P(X < b) = P(X > b)$:
$$2 P(X < b) = 1 \implies P(X < b) = \frac{1}{2} = 0.5$$
*(This means $b$ is precisely the **Median** of the distribution).*

Expressing $P(X < b)$ as an integral:
$$\int_{0}^{b} f(x) \, dx = \frac{1}{2}$$
$$\int_{0}^{b} 6x(1 - x) \, dx = \frac{1}{2}$$
$$6 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^b = \frac{1}{2}$$
$$6 \left( \frac{b^2}{2} - \frac{b^3}{3} \right) = \frac{1}{2}$$
$$3b^2 - 2b^3 = \frac{1}{2}$$

Multiply through by $2$ and rearrange into standard cubic polynomial form:
$$4b^3 - 6b^2 + 1 = 0$$

Let us test rational roots:
At $b = \frac{1}{2}$:
$$4\left(\frac{1}{2}\right)^3 - 6\left(\frac{1}{2}\right)^2 + 1 = 4\left(\frac{1}{8}\right) - 6\left(\frac{1}{4}\right) + 1 = \frac{1}{2} - \frac{3}{2} + 1 = -1 + 1 = 0$$

Since $b = \frac{1}{2}$ is a root and lies within the valid range $[0, 1]$:
$$\mathbf{b = \frac{1}{2} = 0.5}$$

*(Physical Note: Because the PDF $f(x) = 6x(1-x)$ is symmetric about $x = 0.5$, the mean, median, and mode all identically equal $0.5$).*

$$\mathbf{\text{Ans: (i) Mean } = 0.5, \quad \text{(ii) } b = 0.5}$$

---

### Problem 6.6: Cable Diameter PDF $f(x) = kx(5 - x^2)$
*(Ref: Question Bank Q.95, Q.98 | Pg 2, Q.6(b), Pg 4, Q.7(a))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The diameter of an electric cable is assumed to be a continuous random variable with probability density function:
$$f(x) = \begin{cases} k x(5 - x^2), & 0 \le x \le 2 \\ 0, & \text{elsewhere} \end{cases}$$
1. Determine the normalization constant $k$.
2. Find the **Mean** of $X$.
3. Find the **Variance** of $X$.

---

#### Detailed Solution:

#### 1. Determine Constant $k$:
By the total probability property of a PDF:
$$\int_{0}^{2} f(x) \, dx = 1$$
$$k \int_{0}^{2} (5x - x^3) \, dx = 1$$
$$k \left[ \frac{5x^2}{2} - \frac{x^4}{4} \right]_0^2 = 1$$
$$k \left[ \frac{5(4)}{2} - \frac{16}{4} \right] = k [10 - 4] = 6k = 1 \implies \mathbf{k = \frac{1}{6}}$$

Thus, the complete PDF is:
$$f(x) = \frac{1}{6} x(5 - x^2) = \frac{5}{6}x - \frac{1}{6}x^3, \quad 0 \le x \le 2$$

---

#### 2. Mean ($E(X)$):
$$E(X) = \int_{0}^{2} x f(x) \, dx = \frac{1}{6} \int_{0}^{2} x^2(5 - x^2) \, dx = \frac{1}{6} \int_{0}^{2} (5x^2 - x^4) \, dx$$
$$= \frac{1}{6} \left[ \frac{5x^3}{3} - \frac{x^5}{5} \right]_0^2 = \frac{1}{6} \left[ \frac{5(8)}{3} - \frac{32}{5} \right] = \frac{1}{6} \left[ \frac{40}{3} - \frac{32}{5} \right]$$
Finding common denominator ($15$):
$$\frac{40 \times 5 - 32 \times 3}{15} = \frac{200 - 96}{15} = \frac{104}{15}$$
$$E(X) = \frac{1}{6} \times \frac{104}{15} = \frac{52}{45} \approx \mathbf{1.1556}$$

---

#### 3. Variance ($\text{Var}(X)$):
First compute the second raw moment $E(X^2)$:
$$E(X^2) = \int_{0}^{2} x^2 f(x) \, dx = \frac{1}{6} \int_{0}^{2} x^3(5 - x^2) \, dx = \frac{1}{6} \int_{0}^{2} (5x^3 - x^5) \, dx$$
$$= \frac{1}{6} \left[ \frac{5x^4}{4} - \frac{x^6}{6} \right]_0^2 = \frac{1}{6} \left[ \frac{5(16)}{4} - \frac{64}{6} \right] = \frac{1}{6} \left[ 20 - \frac{32}{3} \right]$$
$$= \frac{1}{6} \left( \frac{60 - 32}{3} \right) = \frac{1}{6} \times \frac{28}{3} = \frac{28}{18} = \frac{14}{9} \approx 1.5556$$

Now compute Variance using $\text{Var}(X) = E(X^2) - [E(X)]^2$:
$$\text{Var}(X) = \frac{14}{9} - \left(\frac{52}{45}\right)^2 = \frac{14}{9} - \frac{2704}{2025}$$
Convert $\frac{14}{9}$ to denominator $2025$ ($2025 / 9 = 225$):
$$14 \times 225 = 3150$$
$$\text{Var}(X) = \frac{3150 - 2704}{2025} = \mathbf{\frac{446}{2025}} \approx \mathbf{0.2202}$$

$$\mathbf{\text{Ans: } k = \frac{1}{6}, \quad \text{Mean } = \frac{52}{45} \approx 1.1556, \quad \text{Variance } = \frac{446}{2025} \approx 0.2202}$$

---

### Problem 6.7: Standard Exponential PDF Verification & Interval Probability
*(Ref: Question Bank Q.112 | MHU Sheet Lec 7-10, Problem-9)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Let $X$ be a continuous random variable with probability density function:
$$f(x) = \begin{cases} e^{-x}, & 0 < x < \infty \\ 0, & \text{elsewhere} \end{cases}$$
1. Check that the function is a valid probability density function.
2. Find $P(1 < X < 2)$.

---

#### Detailed Solution:

#### 1. Verification of PDF:
- **Condition 1 (Non-negativity):**  
  For all $x > 0$, $e^{-x} > 0$. Thus $f(x) \ge 0$.
- **Condition 2 (Total Area):**
  $$\int_{-\infty}^{\infty} f(x) \, dx = \int_{0}^{\infty} e^{-x} \, dx = \left[ -e^{-x} \right]_0^\infty = \lim_{M \to \infty} (-e^{-M}) - (-e^0) = 0 - (-1) = 1$$
Since both conditions hold, $f(x)$ is a valid probability density function.

---

#### 2. Calculate $P(1 < X < 2)$:
$$P(1 < X < 2) = \int_{1}^{2} e^{-x} \, dx = \left[ -e^{-x} \right]_1^2 = -e^{-2} - (-e^{-1}) = e^{-1} - e^{-2}$$
Using $e^{-1} \approx 0.367879$ and $e^{-2} \approx 0.135335$:
$$P(1 < X < 2) = 0.367879 - 0.135335 = \mathbf{0.232544} \approx \mathbf{0.2325}$$

$$\mathbf{P(1 < X < 2) = e^{-1} - e^{-2} \approx 0.2325}$$

---

### Problem 6.8: Expected Value and Square Expectation of a Linear Decreasing PDF
*(Ref: Question Bank Q.115 | MHU Sheet Lec 7-10, Problem-14)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Find the expected value of the random variable $X$ and also of its square having the following density function:
$$f(x) = \begin{cases} 2(1 - x), & 0 < x < 1 \\ 0, & \text{elsewhere} \end{cases}$$
Also find the variance of $X$.

---

#### Detailed Solution:

#### 1. Expected Value $E(X)$:
$$E(X) = \int_{0}^{1} x f(x) \, dx = \int_{0}^{1} x \cdot 2(1 - x) \, dx = 2 \int_{0}^{1} (x - x^2) \, dx$$
$$= 2 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2 \left( \frac{1}{2} - \frac{1}{3} \right) = 2 \left( \frac{1}{6} \right) = \mathbf{\frac{1}{3} \approx 0.3333}$$

---

#### 2. Expectation of Square $E(X^2)$:
$$E(X^2) = \int_{0}^{1} x^2 f(x) \, dx = \int_{0}^{1} x^2 \cdot 2(1 - x) \, dx = 2 \int_{0}^{1} (x^2 - x^3) \, dx$$
$$= 2 \left[ \frac{x^3}{3} - \frac{x^4}{4} \right]_0^1 = 2 \left( \frac{1}{3} - \frac{1}{4} \right) = 2 \left( \frac{1}{12} \right) = \mathbf{\frac{1}{6} \approx 0.1667}$$

---

#### 3. Variance $\text{Var}(X)$:
$$\text{Var}(X) = E(X^2) - [E(X)]^2 = \frac{1}{6} - \left(\frac{1}{3}\right)^2 = \frac{1}{6} - \frac{1}{9} = \frac{3 - 2}{18} = \mathbf{\frac{1}{18} \approx 0.0556}$$

$$\mathbf{E(X) = \frac{1}{3}, \quad E(X^2) = \frac{1}{6}, \quad \text{Var}(X) = \frac{1}{18}}$$

---


## 7. Cumulative Distribution Function (CDF) & Properties

### Question 7.1: Definition & Fundamental Properties of the CDF
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Define the Cumulative Distribution Function (CDF) of a random variable, state its mathematical relationship with the PDF, and outline its fundamental properties.**

---

#### Solution:

#### 1. Definition:
The **Cumulative Distribution Function (CDF)**, denoted by $F(x)$, of a random variable $X$ (whether discrete or continuous) is the probability that $X$ takes a value less than or equal to $x$:
$$F(x) = P(X \le x), \quad -\infty < x < \infty$$

- **For a Discrete Random Variable:**
  $$F(x) = \sum_{x_i \le x} f(x_i)$$
- **For a Continuous Random Variable:**
  $$F(x) = \int_{-\infty}^{x} f(t) \, dt$$

#### 2. Fundamental Relationship Between PDF and CDF:
By the Fundamental Theorem of Calculus, for a continuous random variable whose PDF $f(x)$ is continuous at $x$:
$$f(x) = \frac{d}{dx} F(x) = F'(x)$$

#### 3. Core Properties of CDF:
1. **Boundedness:** $0 \le F(x) \le 1$ for all $x \in \mathbb{R}$.
2. **Monotonically Non-Decreasing:** If $x_1 < x_2$, then $F(x_1) \le F(x_2)$.
3. **Limiting Values:**
   $$\lim_{x \to -\infty} F(x) = 0 \quad \text{and} \quad \lim_{x \to \infty} F(x) = 1$$
4. **Right-Continuity:** $F(x)$ is continuous from the right, i.e., $\lim_{h \to 0^+} F(x + h) = F(x)$.
5. **Interval Probability Formula:**
   $$P(a < X \le b) = F(b) - F(a)$$
   $$P(X > a) = 1 - F(a)$$

---

### Problem 7.2: Deriving CDF and Verifying $f(x) = F'(x)$
*(Ref: Question Bank Q.113 | MHU Sheet Lec 7-10, Problem-10)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Given the probability density function:
$$f(x) = \begin{cases} \frac{1}{2} e^{-x/2}, & 0 < x < \infty \\ 0, & \text{elsewhere} \end{cases}$$
1. Find the cumulative distribution function $F(x)$.
2. Show that $f(x) = \frac{d}{dx} F(x)$.
3. Find the value of $F(3)$ and compute $P(X > 3)$.

---

#### Detailed Solution:

#### 1. Find $F(x)$:
For $x \le 0$:
$$F(x) = \int_{-\infty}^x 0 \, dt = 0$$

For $x > 0$:
$$F(x) = \int_{0}^{x} f(t) \, dt = \int_{0}^{x} \frac{1}{2} e^{-t/2} \, dt$$
Evaluating the integral:
$$F(x) = \frac{1}{2} \left[ \frac{e^{-t/2}}{-1/2} \right]_0^x = - \left[ e^{-t/2} \right]_0^x = - (e^{-x/2} - e^0) = 1 - e^{-x/2}$$

Combining cases:
$$F(x) = \begin{cases} 0, & x < 0 \\ 1 - e^{-x/2}, & x \ge 0 \end{cases}$$

---

#### 2. Show that $f(x) = \frac{d}{dx} F(x)$:
Differentiating $F(x)$ with respect to $x$ for $x > 0$:
$$\frac{d}{dx} F(x) = \frac{d}{dx} (1 - e^{-x/2}) = 0 - \left(-\frac{1}{2} e^{-x/2}\right) = \frac{1}{2} e^{-x/2} = f(x)$$
*(Hence proved).*

---

#### 3. Find $F(3)$ and $P(X > 3)$:
Substitute $x = 3$ into $F(x)$:
$$F(3) = 1 - e^{-3/2} = 1 - e^{-1.5}$$
Using $e^{-1.5} \approx 0.22313$:
$$F(3) = 1 - 0.22313 = \mathbf{0.77687} \approx \mathbf{0.7769} \quad (77.69\%)$$

Now compute $P(X > 3)$:
$$P(X > 3) = 1 - P(X \le 3) = 1 - F(3) = e^{-1.5} \approx \mathbf{0.2231} \quad (22.31\%)$$

$$\mathbf{\text{Ans: } F(x) = 1 - e^{-x/2} \; (x \ge 0), \quad F(3) \approx 0.7769, \quad P(X > 3) \approx 0.2231}$$

---

### Problem 7.3: Finding PDF and Probabilities from a Given CDF
*(Ref: Question Bank Q.114 | MHU Sheet Lec 7-10, Problem-11)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The distribution function for a continuous random variable $X$ is given by:
$$F(x) = \begin{cases} 1 - e^{-2x}, & x \ge 0 \\ 0, & x < 0 \end{cases}$$
1. Find the probability density function $f(x)$.
2. Find the probability that $X > 2$.
3. Find the probability that $-3 < X \le 4$.

---

#### Detailed Solution:

#### 1. Find the Density Function $f(x)$:
For $x > 0$:
$$f(x) = \frac{d}{dx} F(x) = \frac{d}{dx} (1 - e^{-2x}) = 0 - (-2 e^{-2x}) = 2 e^{-2x}$$
For $x < 0$, $f(x) = \frac{d}{dx}(0) = 0$.

Therefore, the PDF is:
$$f(x) = \begin{cases} 2e^{-2x}, & x > 0 \\ 0, & x \le 0 \end{cases}$$

---

#### 2. Find $P(X > 2)$:
Using the complement of the CDF:
$$P(X > 2) = 1 - P(X \le 2) = 1 - F(2)$$
Substitute $x = 2$ into $F(x)$:
$$F(2) = 1 - e^{-2(2)} = 1 - e^{-4}$$
$$P(X > 2) = 1 - (1 - e^{-4}) = e^{-4}$$
Using $e^{-4} \approx 0.0183156$:
$$P(X > 2) = \mathbf{e^{-4} \approx 0.01832} \quad (1.832\%)$$

---

#### 3. Find $P(-3 < X \le 4)$:
Using the interval formula for CDF:
$$P(-3 < X \le 4) = F(4) - F(-3)$$
From the definition of $F(x)$:
- $F(4) = 1 - e^{-2(4)} = 1 - e^{-8}$
- $F(-3) = 0$ (since $-3 < 0$)

Therefore:
$$P(-3 < X \le 4) = (1 - e^{-8}) - 0 = 1 - e^{-8}$$
Using $e^{-8} \approx 0.00033546$:
$$P(-3 < X \le 4) = 1 - 0.00033546 = \mathbf{0.999665} \approx \mathbf{0.9997} \quad (99.97\%)$$

$$\mathbf{\text{Ans: (a) } f(x) = 2e^{-2x} \; (x > 0), \quad \text{(b) } e^{-4} \approx 0.0183, \quad \text{(c) } 1 - e^{-8} \approx 0.9997}$$

---


## 8. Measures of Central Tendency & Moments for Continuous Distributions

### Question 8.1: Formulas for Continuous Distributions
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Question 7.1)*
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
**Variance using  2nd Raw Moment and mean:**  $\text{Var}(X) = E(X^2) - [E(X)]^2$:
---

### Problem 8.2: Comprehensive Calculation on $f(x) = cx(2-x)$
*(Ref: Note Problem 7.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 7.2)*
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
$$AM = \int_{0}^{2} x f(x) \, dx = \frac{3}{4} \int_{0}^{2} (2x^2 - x^3) \, dx = \frac{3}{4} \left[ \frac{2x^3}{3} - \frac{x^4}{4} \right]_0^2$$
$$= \frac{3}{4} \left[ \frac{16}{3} - 4 \right] = \frac{3}{4} \left( \frac{4}{3} \right) = \mathbf{1}$$

---

#### Step 3: Harmonic Mean ($HM$)
$$\frac{1}{HM} = \int_{0}^{2} \frac{1}{x} f(x) \, dx = \int_{0}^{2} \frac{1}{x} \left( \frac{3}{4}x(2-x) \right) \, dx = \frac{3}{4} \int_{0}^{2} (2 - x) \, dx$$
$$= \frac{3}{4} \left[ 2x - \frac{x^2}{2} \right]_0^2 = \frac{3}{4} [4 - 2] = \frac{3}{2} \implies \mathbf{HM = \frac{2}{3}}$$

---

#### Step 4: Median ($M_e$)
$$\int_{0}^{M_e} \frac{3}{4}(2x - x^2) \, dx = \frac{1}{2} \implies M_e^2 - \frac{M_e^3}{3} = \frac{2}{3} \implies M_e^3 - 3M_e^2 + 2 = 0$$
Factoring: $(M_e - 1)(M_e^2 - 2M_e - 2) = 0$.  
Roots of quadratic are $1 \pm \sqrt{3}$ (both lie outside $[0, 2]$).  
Therefore, the only admissible root in $[0, 2]$ is:
$$\mathbf{M_e = 1}$$

---

#### Step 5: Mode ($M_o$)
$$f'(x) = \frac{3}{2}(1 - x) = 0 \implies x = 1$$
$$f''(1) = -\frac{3}{2} < 0 \implies \mathbf{M_o = 1}$$

---

#### Step 6: Geometric Mean ($GM$)
$$\ln(GM) = \int_{0}^{2} (\ln x) \cdot \frac{3}{4}(2x - x^2) \, dx$$
Integrating by parts:
$$\ln(GM) = \frac{3}{4} \left[ \frac{4}{3} \ln 2 - \frac{10}{9} \right] = \ln 2 - \frac{5}{6}$$
$$\mathbf{GM = 2 e^{-5/6} \approx 0.8692}$$

$$\mathbf{\text{Summary: } c = \frac{3}{4}, \quad AM = 1, \quad HM = \frac{2}{3}, \quad M_e = 1, \quad M_o = 1, \quad GM = 2e^{-5/6} \approx 0.8692}$$

---


## 9. Mathematical Expectation, Moments & Moment Generating Functions (MGF)

### Question 9.1: Expectation and Raw Moments Definitions
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Question 8.1)*
**Define Mathematical Expectation and Raw Moments for Discrete and Continuous Random Variables.**

---

#### Solution:

1. **For a Discrete Random Variable $X$:**  
   If $X$ takes values $x_1, x_2, \dots, x_n$ with PMF $P(X = x_i)$:
   - **Expectation (Mean):**
     $$E(X) = \mu = \sum_{i=1}^n x_i P(x_i)$$
   - **$r$-th Raw Moment (about origin):**
     $$\mu_r' = E(X^r) = \sum_{i=1}^n x_i^r P(x_i)$$

2. **For a Continuous Random Variable $X$:**  
   If $X$ has probability density function $f(x)$:
   - **Expectation (Mean):**
     $$E(X) = \mu = \int_{-\infty}^{\infty} x f(x) \, dx$$
   - **$r$-th Raw Moment (about origin):**
     $$\mu_r' = E(X^r) = \int_{-\infty}^{\infty} x^r f(x) \, dx$$

---

### Question 9.2: Moment Generating Function (MGF) and Cumulant Generating Function (CGF)
*(Ref: Question Bank Q.97, Q.108, Q.118, Q.125 | Pg 3 Q.8(a), Pg 14 CT-03 Q.3, MHU Sheet)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Define the Moment Generating Function (MGF) and Cumulant Generating Function (CGF). Explain how moments are derived from them.**

---

#### Solution:

#### 1. Moment Generating Function (MGF):
The Moment Generating Function of a random variable $X$, denoted by $M_X(t)$ or $M(t)$, is defined as the mathematical expectation of $e^{tX}$:
$$M_X(t) = E\left(e^{tX}\right)$$
- **For Discrete RV:** $M_X(t) = \sum_{x} e^{tx} P(X = x)$
- **For Continuous RV:** $M_X(t) = \int_{-\infty}^{\infty} e^{tx} f(x) \, dx$
*(provided the expectation exists for $t$ in some neighborhood of zero $|t| < h$).*

#### Generating Moments via Series Expansion:
Expanding $e^{tX}$ as a Maclaurin series:
$$e^{tX} = 1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \dots + \frac{t^r X^r}{r!} + \dots$$
Taking expectations on both sides:
$$M_X(t) = E\left[1 + tX + \frac{t^2 X^2}{2!} + \dots\right] = 1 + t E(X) + \frac{t^2}{2!} E(X^2) + \dots + \frac{t^r}{r!} E(X^r) + \dots$$
$$M_X(t) = 1 + t \mu_1' + \frac{t^2}{2!} \mu_2' + \frac{t^3}{3!} \mu_3' + \dots + \frac{t^r}{r!} \mu_r' + \dots$$

Thus, the $r$-th raw moment $\mu_r' = E(X^r)$ is given by the coefficient of $\frac{t^r}{r!}$ in the power series expansion of $M_X(t)$, or equivalently:
$$\mu_r' = E(X^r) = \left. \frac{d^r M_X(t)}{dt^r} \right|_{t = 0}$$

Specifically:
- First raw moment (Mean): $\mu_1' = E(X) = M_X'(0)$
- Second raw moment: $\mu_2' = E(X^2) = M_X''(0)$
- Variance: $\sigma^2 = \mu_2 = \mu_2' - (\mu_1')^2 = M_X''(0) - [M_X'(0)]^2$

---

#### 2. Cumulant Generating Function (CGF):
The Cumulant Generating Function $K_X(t)$ is defined as the natural logarithm of the moment generating function:
$$K_X(t) = \ln M_X(t) = \sum_{r=1}^{\infty} \kappa_r \frac{t^r}{r!} = \kappa_1 t + \kappa_2 \frac{t^2}{2!} + \kappa_3 \frac{t^3}{3!} + \kappa_4 \frac{t^4}{4!} + \dots$$
where $\kappa_r$ is the $r$-th cumulant:
- $\kappa_1 = \mu_1' = \text{Mean}$
- $\kappa_2 = \mu_2 = \sigma^2 = \text{Variance}$
- $\kappa_3 = \mu_3$ (third central moment)
- $\kappa_4 = \mu_4 - 3\mu_2^2$

---

### Question 9.3: Relations Between Central Moments ($\mu_r$) and Raw Moments ($\mu_r'$)
*(Ref: Question Bank Q.44, Q.49, Q.54, Q.58 | Pg 12 CT-02 Q.1, Pg 16 CT-03 Q.1 (Or), MHU Sheet Lec 5-6 Q.1, Q.5)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Establish the general relationship between central moments ($\mu_r$) and raw moments about an arbitrary origin $A$ ($\mu_r'$). Hence prove that:**
$$\mu_0 = 1, \quad \mu_1 = 0, \quad \mu_2 = \mu_2' - (\mu_1')^2 = \sigma^2$$
$$\mu_3 = \mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3$$
$$\mu_4 = \mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4$$

---

#### Detailed Proof:

Let raw moments about origin $0$ be $\mu_r' = E(X^r)$, with mean $\mu = \mu_1' = E(X)$.  
The $r$-th central moment is defined by:
$$\mu_r = E[(X - \mu)^r]$$

Expanding $(X - \mu)^r$ using the Binomial Theorem:
$$(X - \mu)^r = \sum_{j=0}^r \binom{r}{j} X^{r-j} (-\mu)^j = \sum_{j=0}^r \binom{r}{j} (-1)^j \mu^j X^{r-j}$$
Taking expectations on both sides:
$$\mu_r = E[(X - \mu)^r] = \sum_{j=0}^r \binom{r}{j} (-1)^j \mu^j E(X^{r-j}) = \sum_{j=0}^r \binom{r}{j} (-1)^j (\mu_1')^j \mu_{r-j}'$$

Evaluating for $r = 0, 1, 2, 3, 4$:

1. **For $r = 0$:**
   $$\mu_0 = E[(X - \mu)^0] = E(1) = \mathbf{1}$$

2. **For $r = 1$:**
   $$\mu_1 = E[X - \mu] = E(X) - \mu = \mu - \mu = \mathbf{0}$$
   *(The first central moment is always identically zero).*

3. **For $r = 2$:**
   $$\mu_2 = E[(X - \mu)^2] = E[X^2 - 2\mu X + \mu^2] = E(X^2) - 2\mu E(X) + \mu^2$$
   $$= \mu_2' - 2(\mu_1')(\mu_1') + (\mu_1')^2 = \mathbf{\mu_2' - (\mu_1')^2 = \sigma^2 \quad (\text{Variance})}$$

4. **For $r = 3$:**
   $$\mu_3 = E[(X - \mu)^3] = E[X^3 - 3X^2 \mu + 3X \mu^2 - \mu^3]$$
   $$= E(X^3) - 3\mu E(X^2) + 3\mu^2 E(X) - \mu^3$$
   $$= \mu_3' - 3\mu_1' \mu_2' + 3(\mu_1')^2 (\mu_1') - (\mu_1')^3 = \mathbf{\mu_3' - 3\mu_2'\mu_1' + 2(\mu_1')^3}$$

5. **For $r = 4$:**
   $$\mu_4 = E[(X - \mu)^4] = E[X^4 - 4X^3 \mu + 6X^2 \mu^2 - 4X \mu^3 + \mu^4]$$
   $$= \mu_4' - 4\mu_1' \mu_3' + 6(\mu_1')^2 \mu_2' - 4(\mu_1')^3 (\mu_1') + (\mu_1')^4$$
   $$= \mathbf{\mu_4' - 4\mu_3'\mu_1' + 6\mu_2'(\mu_1')^2 - 3(\mu_1')^4}$$
*(Hence proved).*

---


## 10. Joint, Marginal, and Conditional Distributions (Discrete & Continuous)

### Question 10.1: Theoretical Definitions
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Question 9.1)*
**Define Joint Probability Function, Marginal Probability Function, Conditional Probability Function, and Statistical Independence for both Discrete and Continuous Random Variables.**

---

#### Solution:

1. **Joint Probability Functions:**  
   - **Discrete:** $p(x, y) = P(X = x, Y = y)$ satisfies $p(x, y) \ge 0$ and $\sum_x \sum_y p(x, y) = 1$.
   - **Continuous:** $f(x, y)$ satisfies $f(x, y) \ge 0$ and $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \, dx \, dy = 1$.

2. **Marginal Distributions:**
   - **Discrete:** $p_X(x) = \sum_y p(x, y), \quad p_Y(y) = \sum_x p(x, y)$.
   - **Continuous:** $f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy, \quad f_Y(y) = \int_{-\infty}^{\infty} f(x, y) \, dx$.

3. **Conditional Distributions:**
   - $f(x | y) = \frac{f(x, y)}{f_Y(y)}$ (for $f_Y(y) > 0$), and $f(y | x) = \frac{f(x, y)}{f_X(x)}$ (for $f_X(x) > 0$).

4. **Statistical Independence:**  
   $X$ and $Y$ are independent if and only if:
   $$f(x, y) = f_X(x) \cdot f_Y(y) \quad \text{for all } (x, y)$$

---

### Problem 10.2: Bivariate Continuous PDF $f(x, y) = x e^{-x(y+1)}$
*(Ref: Note Problem 9.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 9.2)*
**Problem Statement:**  
The joint probability density function of two continuous random variables $X$ and $Y$ is:
$$f(x, y) = \begin{cases} x e^{-x(y+1)}, & x > 0, y > 0 \\ 0, & \text{elsewhere} \end{cases}$$
1. Find marginal $f_X(x)$.
2. Find marginal $f_Y(y)$.
3. Find conditional PDFs $f(x|y)$ and $f(y|x)$.
4. Determine whether $X$ and $Y$ are independent.

---

#### Detailed Solution:
1. $f_X(x) = \int_0^\infty x e^{-x(y+1)} dy = x e^{-x} \int_0^\infty e^{-xy} dy = x e^{-x} \left(\frac{1}{x}\right) = \mathbf{e^{-x}, \quad x > 0}$.
2. $f_Y(y) = \int_0^\infty x e^{-(y+1)x} dx = \frac{\Gamma(2)}{(y+1)^2} = \mathbf{\frac{1}{(y+1)^2}, \quad y > 0}$.
3. $f(x|y) = \frac{x e^{-x(y+1)}}{1/(y+1)^2} = \mathbf{(y+1)^2 x e^{-x(y+1)}}$.  
   $f(y|x) = \frac{x e^{-x(y+1)}}{e^{-x}} = \mathbf{x e^{-xy}, \quad y > 0}$.
4. $f_X(x) f_Y(y) = \frac{e^{-x}}{(y+1)^2} \ne x e^{-x(y+1)} \implies \mathbf{X \text{ and } Y \text{ are NOT independent}}$.

---

### Problem 10.3: Joint Continuous PDF of Dependent Random Variables
*(Ref: Question Bank Q.94, Q.15 | Pg 2 & Pg 3, Q.7(a))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The joint probability density function of two continuous random variables $X$ and $Y$ is given by:
$$f_{XY}(x, y) = \begin{cases} K e^{-0.001x - 0.002y}, & 0 < x < y < \infty \\ 0, & \text{elsewhere} \end{cases}$$
where $K = 6 \times 10^{-6}$.  
Find:
1. The probability $P(X \le 1000, Y \le 2000)$.
2. The probability that $Y$ exceeds $2000$ ($P(Y > 2000)$).
3. The conditional density function of $Y$ given $X$, $f(y|x)$.

---

#### Detailed Solution:

Let $\lambda_1 = 0.001 = 10^{-3}$ and $\lambda_2 = 0.002 = 2 \times 10^{-3}$.  
Notice that the permissible region is the wedge $0 < x < y < \infty$.  
Check total integral:
$$\int_{0}^{\infty} dx \int_{x}^{\infty} K e^{-\lambda_1 x - \lambda_2 y} \, dy = \int_{0}^{\infty} K e^{-\lambda_1 x} \left[ \frac{e^{-\lambda_2 y}}{-\lambda_2} \right]_x^\infty dx$$
$$= \frac{K}{\lambda_2} \int_{0}^{\infty} e^{-\lambda_1 x} e^{-\lambda_2 x} \, dx = \frac{K}{\lambda_2} \int_{0}^{\infty} e^{-(\lambda_1 + \lambda_2)x} \, dx = \frac{K}{\lambda_2 (\lambda_1 + \lambda_2)}$$
$$= \frac{6 \times 10^{-6}}{(2 \times 10^{-3})(3 \times 10^{-3})} = \frac{6 \times 10^{-6}}{6 \times 10^{-6}} = 1$$
*(The given constant $K$ is fully verified).*

---

#### 1. Compute $P(X \le 1000, Y \le 2000)$:
The integration limits in the $xy$-plane for $0 < x < y < \infty$ with $x \le 1000$ and $y \le 2000$ are:
- $x$ ranges from $0$ to $1000$
- For a given $x$, $y$ ranges from $x$ to $2000$

$$P(X \le 1000, Y \le 2000) = \int_{0}^{1000} dx \int_{x}^{2000} K e^{-0.001x - 0.002y} \, dy$$
Evaluate the inner integral over $y$:
$$\int_{x}^{2000} e^{-0.002y} \, dy = \left[ \frac{e^{-0.002y}}{-0.002} \right]_x^{2000} = \frac{e^{-0.002x} - e^{-0.002(2000)}}{0.002} = \frac{e^{-0.002x} - e^{-4}}{0.002}$$

Now evaluate the outer integral:
$$P = \frac{K}{0.002} \int_{0}^{1000} e^{-0.001x} (e^{-0.002x} - e^{-4}) \, dx$$
Since $\frac{K}{0.002} = \frac{6 \times 10^{-6}}{2 \times 10^{-3}} = 3 \times 10^{-3} = 0.003$:
$$P = 0.003 \int_{0}^{1000} \left( e^{-0.003x} - e^{-4} e^{-0.001x} \right) \, dx$$
$$= 0.003 \left[ \frac{1 - e^{-0.003(1000)}}{0.003} - e^{-4} \frac{1 - e^{-0.001(1000)}}{0.001} \right]$$
$$= (1 - e^{-3}) - \frac{0.003}{0.001} e^{-4} (1 - e^{-1}) = (1 - e^{-3}) - 3 e^{-4} (1 - e^{-1})$$

Using numerical values:
- $e^{-1} \approx 0.367879 \implies 1 - e^{-1} \approx 0.632121$
- $e^{-3} \approx 0.049787 \implies 1 - e^{-3} \approx 0.950213$
- $e^{-4} \approx 0.018316$
$$3 e^{-4} (1 - e^{-1}) = 3 \times 0.018316 \times 0.632121 \approx 0.034734$$
$$P = 0.950213 - 0.034734 = \mathbf{0.915479} \approx \mathbf{0.9155} \quad (91.55\%)$$

---

#### 2. Compute $P(Y > 2000)$:
To find $P(Y > 2000)$, integrate over $y$ from $2000$ to $\infty$, where for each $y$, $x$ ranges from $0$ to $y$:
$$P(Y > 2000) = \int_{2000}^{\infty} dy \int_{0}^{y} K e^{-0.001x - 0.002y} \, dx$$
Inner integral over $x$:
$$\int_{0}^{y} e^{-0.001x} \, dx = \left[ \frac{1 - e^{-0.001y}}{0.001} \right] = 1000 (1 - e^{-0.001y})$$

Now integrate over $y$:
$$P(Y > 2000) = \frac{K}{0.001} \int_{2000}^{\infty} e^{-0.002y} (1 - e^{-0.001y}) \, dy$$
Since $\frac{K}{0.001} = 0.006$:
$$= 0.006 \int_{2000}^{\infty} (e^{-0.002y} - e^{-0.003y}) \, dy$$
$$= 0.006 \left[ \frac{e^{-0.002(2000)}}{0.002} - \frac{e^{-0.003(2000)}}{0.003} \right]$$
$$= 0.006 \left[ \frac{e^{-4}}{0.002} - \frac{e^{-6}}{0.003} \right] = 3 e^{-4} - 2 e^{-6}$$

Using $e^{-4} \approx 0.0183156$ and $e^{-6} \approx 0.00247875$:
$$P(Y > 2000) = 3(0.0183156) - 2(0.00247875) = 0.054947 - 0.004958 = \mathbf{0.049989} \approx \mathbf{0.0500} \quad (5.00\%)$$

---

#### 3. Conditional Density Function of $Y$ given $X$, $f(y | x)$:
First determine the marginal density $f_X(x)$:
$$f_X(x) = \int_{x}^{\infty} f(x, y) \, dy = \int_{x}^{\infty} K e^{-0.001x - 0.002y} \, dy = K e^{-0.001x} \left[ \frac{e^{-0.002y}}{-0.002} \right]_x^\infty$$
$$f_X(x) = \frac{K}{0.002} e^{-0.001x} e^{-0.002x} = \frac{6 \times 10^{-6}}{2 \times 10^{-3}} e^{-0.003x} = 0.003 e^{-0.003x}, \quad x > 0$$

Now evaluate the conditional density:
$$f(y | x) = \frac{f_{XY}(x, y)}{f_X(x)} = \frac{6 \times 10^{-6} e^{-0.001x - 0.002y}}{0.003 e^{-0.003x}}$$
$$f(y | x) = \frac{6 \times 10^{-6}}{3 \times 10^{-3}} e^{-0.001x - 0.002y + 0.003x} = 0.002 e^{0.002x - 0.002y}$$
$$\mathbf{f(y | x) = 0.002 e^{-0.002(y - x)}, \quad y > x > 0}$$
*(Notice: Given $X = x$, the variable $Y - x$ is exponentially distributed with rate parameter $\lambda = 0.002$).*

$$\mathbf{\text{Ans: (i) } 0.9155, \quad \text{(ii) } 3e^{-4} - 2e^{-6} \approx 0.0500, \quad \text{(iii) } f(y|x) = 0.002 e^{-0.002(y-x)} \; (y > x)}$$

---

### Problem 10.4: Discrete Contingency Table and Conditional Probability
*(Ref: Question Bank Q.16 | MHU Sheet Lec 7-10, Problem-12)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The joint probability distribution of $X$ and $Y$ is given by the following contingency table:

| $X \backslash Y$ | 0 | 1 | 2 | 3 | 4 | $P(X = x_i)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $1/16$ | 0 | 0 | 0 | $1/16$ | $2/16$ |
| **2** | 0 | $2/16$ | $2/16$ | $2/16$ | 0 | $6/16$ |
| **3** | 0 | $2/16$ | $2/16$ | $2/16$ | 0 | $6/16$ |
| **4** | 0 | 0 | $2/16$ | 0 | 0 | $2/16$ |
| **$P(Y = y_j)$** | $1/16$ | $4/16$ | $6/16$ | $4/16$ | $1/16$ | **1** |

Find the conditional probability function of $X$ given that $Y = 3$, i.e., $P(X = x | Y = 3)$.

---

#### Detailed Solution:

By definition of conditional probability:
$$P(X = x | Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}$$

For $Y = 3$, the marginal probability is:
$$P(Y = 3) = \sum_{x=1}^4 P(X = x, Y = 3) = 0 + \frac{2}{16} + \frac{2}{16} + 0 = \frac{4}{16} = \frac{1}{4}$$

Now evaluate for each possible value of $X \in \{1, 2, 3, 4\}$:
- For $X = 1$:
  $$P(X = 1 | Y = 3) = \frac{P(X = 1, Y = 3)}{P(Y = 3)} = \frac{0}{4/16} = \mathbf{0}$$
- For $X = 2$:
  $$P(X = 2 | Y = 3) = \frac{P(X = 2, Y = 3)}{P(Y = 3)} = \frac{2/16}{4/16} = \frac{2}{4} = \mathbf{\frac{1}{2} = 0.5}$$
- For $X = 3$:
  $$P(X = 3 | Y = 3) = \frac{P(X = 3, Y = 3)}{P(Y = 3)} = \frac{2/16}{4/16} = \frac{2}{4} = \mathbf{\frac{1}{2} = 0.5}$$
- For $X = 4$:
  $$P(X = 4 | Y = 3) = \frac{P(X = 4, Y = 3)}{P(Y = 3)} = \frac{0}{4/16} = \mathbf{0}$$

**Summary of Conditional PMF $P(X | Y = 3)$:**

| $x$ | 1 | 2 | 3 | 4 | Total |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $P(X = x \| Y = 3)$ | $0$ | $1/2$ | $1/2$ | $0$ | **1** |

---

### Problem 10.5: Comprehensive Discrete Joint Distribution Analysis
*(Ref: Question Bank Q.17 | MHU Sheet Lec 7-10, Problem-13)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The joint probability distribution of $X$ and $Y$ is given by the table:

| $X \backslash Y$ | 1 | 3 | 9 | $P(X = x)$ |
| :---: | :---: | :---: | :---: | :---: |
| **2** | $1/8$ | $1/24$ | $1/12$ | $1/4$ |
| **4** | $1/4$ | $1/4$ | 0 | $1/2$ |
| **6** | $1/8$ | $1/24$ | $1/12$ | $1/4$ |
| **$P(Y = y)$** | $1/2$ | $1/3$ | $1/6$ | **1** |

Determine:
1. The marginal distributions $P(X)$ and $P(Y)$, and compute $E(X), E(Y), \text{Var}(X), \text{Var}(Y)$.
2. The conditional distributions $P(X|Y)$ and $P(Y|X)$.
3. The conditional expectations $E(X | Y = 1)$ and $E(Y | X = 4)$.
4. The covariance $\text{Cov}(X, Y)$ and check whether $X$ and $Y$ are independent.

---

#### Detailed Solution:

#### 1. Marginals, Means, and Variances:

- **Marginal PMF of $X$:**
  - $P(X = 2) = \frac{1}{8} + \frac{1}{24} + \frac{1}{12} = \frac{3 + 1 + 2}{24} = \frac{6}{24} = \frac{1}{4}$
  - $P(X = 4) = \frac{1}{4} + \frac{1}{4} + 0 = \frac{2}{4} = \frac{1}{2}$
  - $P(X = 6) = \frac{1}{8} + \frac{1}{24} + \frac{1}{12} = \frac{6}{24} = \frac{1}{4}$
  *(Sum: $1/4 + 1/2 + 1/4 = 1$).*

  $$E(X) = 2\left(\frac{1}{4}\right) + 4\left(\frac{1}{2}\right) + 6\left(\frac{1}{4}\right) = \frac{2}{4} + 2 + \frac{6}{4} = 4$$
  $$E(X^2) = 2^2\left(\frac{1}{4}\right) + 4^2\left(\frac{1}{2}\right) + 6^2\left(\frac{1}{4}\right) = 4\left(\frac{1}{4}\right) + 16\left(\frac{1}{2}\right) + 36\left(\frac{1}{4}\right) = 1 + 8 + 9 = 18$$
  $$\text{Var}(X) = E(X^2) - [E(X)]^2 = 18 - 4^2 = 18 - 16 = \mathbf{2}$$

- **Marginal PMF of $Y$:**
  - $P(Y = 1) = \frac{1}{8} + \frac{1}{4} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}$
  - $P(Y = 3) = \frac{1}{24} + \frac{1}{4} + \frac{1}{24} = \frac{1 + 6 + 1}{24} = \frac{8}{24} = \frac{1}{3}$
  - $P(Y = 9) = \frac{1}{12} + 0 + \frac{1}{12} = \frac{2}{12} = \frac{1}{6}$
  *(Sum: $1/2 + 1/3 + 1/6 = 1$).*

  $$E(Y) = 1\left(\frac{1}{2}\right) + 3\left(\frac{1}{3}\right) + 9\left(\frac{1}{6}\right) = \frac{1}{2} + 1 + \frac{3}{2} = 3$$
  $$E(Y^2) = 1^2\left(\frac{1}{2}\right) + 3^2\left(\frac{1}{3}\right) + 9^2\left(\frac{1}{6}\right) = \frac{1}{2} + 3 + \frac{81}{6} = \frac{1}{2} + 3 + \frac{27}{2} = 17$$
  $$\text{Var}(Y) = E(Y^2) - [E(Y)]^2 = 17 - 3^2 = 17 - 9 = \mathbf{8}$$

---

#### 2. Conditional Distributions:
- **Conditional PMF of $X$ given $Y = 1$ ($P(Y=1) = 1/2$):**
  - $P(X = 2 | Y = 1) = \frac{1/8}{1/2} = \frac{2}{8} = \frac{1}{4}$
  - $P(X = 4 | Y = 1) = \frac{1/4}{1/2} = \frac{2}{4} = \frac{1}{2}$
  - $P(X = 6 | Y = 1) = \frac{1/8}{1/2} = \frac{2}{8} = \frac{1}{4}$

- **Conditional PMF of $Y$ given $X = 4$ ($P(X=4) = 1/2$):**
  - $P(Y = 1 | X = 4) = \frac{1/4}{1/2} = \frac{1}{2}$
  - $P(Y = 3 | X = 4) = \frac{1/4}{1/2} = \frac{1}{2}$
  - $P(Y = 9 | X = 4) = \frac{0}{1/2} = 0$

---

#### 3. Conditional Expectations:
- **$E(X | Y = 1)$:**
  $$E(X | Y = 1) = 2\left(\frac{1}{4}\right) + 4\left(\frac{1}{2}\right) + 6\left(\frac{1}{4}\right) = \frac{1}{2} + 2 + \frac{3}{2} = \mathbf{4}$$

- **$E(Y | X = 4)$:**
  $$E(Y | X = 4) = 1\left(\frac{1}{2}\right) + 3\left(\frac{1}{2}\right) + 9(0) = \frac{1}{2} + \frac{3}{2} = \mathbf{2}$$

---

#### 4. Covariance & Statistical Independence:
Calculate joint expectation $E(XY)$:
$$E(XY) = \sum_x \sum_y x y P(X = x, Y = y)$$
$$= (2 \times 1)\left(\frac{1}{8}\right) + (2 \times 3)\left(\frac{1}{24}\right) + (2 \times 9)\left(\frac{1}{12}\right)$$
$$+ (4 \times 1)\left(\frac{1}{4}\right) + (4 \times 3)\left(\frac{1}{4}\right) + (4 \times 9)(0)$$
$$+ (6 \times 1)\left(\frac{1}{8}\right) + (6 \times 3)\left(\frac{1}{24}\right) + (6 \times 9)\left(\frac{1}{12}\right)$$

$$= \frac{2}{8} + \frac{6}{24} + \frac{18}{12} + 1 + 3 + 0 + \frac{6}{8} + \frac{18}{24} + \frac{54}{12}$$
$$= \frac{1}{4} + \frac{1}{4} + \frac{3}{2} + 4 + \frac{3}{4} + \frac{3}{4} + \frac{9}{2}$$
$$= \left(\frac{1}{4} + \frac{1}{4} + \frac{3}{4} + \frac{3}{4}\right) + \left(\frac{3}{2} + \frac{9}{2}\right) + 4 = 2 + 6 + 4 = 12$$

Now compute covariance:
$$\text{Cov}(X, Y) = E(XY) - E(X)E(Y) = 12 - (4 \times 3) = 12 - 12 = \mathbf{0}$$

**Check for Independence:**  
Although $\text{Cov}(X, Y) = 0$ (meaning $X$ and $Y$ are uncorrelated), let us check independence at $X = 4, Y = 9$:
$$P(X = 4, Y = 9) = 0$$
$$P(X = 4) \cdot P(Y = 9) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12} \ne 0$$
Since $P(X = 4, Y = 9) \ne P(X = 4) \cdot P(Y = 9)$:  
$$\mathbf{X \text{ and } Y \text{ are NOT independent (they are dependent but uncorrelated)}}.$$

---


## 11. Binomial Distribution

### Question 11.1: Definition & Mathematical Model
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Question 10.1)*
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
5. For a binomial distribution, $\text{Variance} < \text{Mean}$ always holds since $q = 1 - p < 1$.

---

### Theorem 11.2: Total Probability of Binomial Distribution is Unity
*(Ref: Question Bank Q.117 | MHU Sheet Lec 11-14 (Binomial), Problem-1)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Prove that the total probability density (mass) function of the Binomial Distribution is unity.**

---

#### Detailed Proof:
The probability mass function of $X \sim B(n, p)$ is $P(X = x) = \binom{n}{x} p^x q^{n-x}$ for $x = 0, 1, 2, \dots, n$.  
Summing over all possible values of $x$:
$$\sum_{x=0}^n P(X = x) = \sum_{x=0}^n \binom{n}{x} p^x q^{n-x}$$
By the Binomial Theorem:
$$(q + p)^n = \sum_{x=0}^n \binom{n}{x} p^x q^{n-x}$$
Since $p$ and $q$ represent the probabilities of success and failure in any single trial, $p + q = 1$.  
Therefore:
$$\sum_{x=0}^n P(X = x) = (q + p)^n = 1^n = 1$$
*(Hence proved).*

---

### Theorem 11.3: Derivation of Mean and Variance of Binomial Distribution
*(Ref: Question Bank Q.103, Q.107, Q.108, Q.110, Q.119 | Pg 6 Q.6(d), Pg 12 CT-02 Q.5, Pg 14 CT-03 Q.3, Pg 16 CT 03 Q.3)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Prove that for a Binomial Distribution with parameters $n$ and $p$, the Mean is $\mu = np$ and the Standard Deviation is $\sigma = \sqrt{npq}$ using:**
1. **Direct Expectation Definition (Algebraic Method)**
2. **Moment Generating Function (MGF Method)**

---

#### Detailed Proof:

#### Method 1: Direct Expectation Definition

**Part (a): Derivation of Mean $\mu = E(X)$:**
$$E(X) = \sum_{x=0}^n x P(X = x) = \sum_{x=0}^n x \binom{n}{x} p^x q^{n-x}$$
The term for $x = 0$ is zero, so the sum starts at $x = 1$:
$$E(X) = \sum_{x=1}^n x \frac{n!}{x! (n-x)!} p^x q^{n-x} = \sum_{x=1}^n \frac{n!}{(x-1)! (n-x)!} p^x q^{n-x}$$
Factor out $n p$:
$$E(X) = n p \sum_{x=1}^n \frac{(n-1)!}{(x-1)! [(n-1) - (x-1)]!} p^{x-1} q^{(n-1)-(x-1)}$$
Let $y = x - 1$ and $m = n - 1$. As $x$ ranges from $1$ to $n$, $y$ ranges from $0$ to $m$:
$$E(X) = n p \sum_{y=0}^m \binom{m}{y} p^y q^{m-y} = n p (p + q)^m$$
Since $p + q = 1$:
$$E(X) = n p (1)^m = \mathbf{np}$$

---

**Part (b): Derivation of Variance $\sigma^2 = npq$:**  
Use the factorial moment identity $E(X^2) = E[X(X - 1)] + E(X)$:
$$E[X(X - 1)] = \sum_{x=0}^n x(x - 1) \binom{n}{x} p^x q^{n-x}$$
The terms for $x = 0$ and $x = 1$ vanish, so the sum begins at $x = 2$:
$$E[X(X - 1)] = \sum_{x=2}^n x(x - 1) \frac{n!}{x! (n-x)!} p^x q^{n-x} = \sum_{x=2}^n \frac{n!}{(x-2)! (n-x)!} p^x q^{n-x}$$
Factor out $n(n - 1) p^2$:
$$E[X(X - 1)] = n(n - 1) p^2 \sum_{x=2}^n \frac{(n-2)!}{(x-2)! [(n-2) - (x-2)]!} p^{x-2} q^{(n-2)-(x-2)}$$
Let $y = x - 2$ and $k = n - 2$:
$$E[X(X - 1)] = n(n - 1) p^2 \sum_{y=0}^k \binom{k}{y} p^y q^{k-y} = n(n - 1) p^2 (p + q)^k = n(n - 1) p^2$$

Now compute $E(X^2)$:
$$E(X^2) = E[X(X - 1)] + E(X) = n(n - 1) p^2 + np = n^2 p^2 - np^2 + np = n^2 p^2 + np(1 - p) = n^2 p^2 + npq$$

Now evaluate the Variance:
$$\text{Var}(X) = \sigma^2 = E(X^2) - [E(X)]^2 = (n^2 p^2 + npq) - (np)^2 = \mathbf{npq}$$
Standard Deviation:
$$\sigma = \mathbf{\sqrt{npq}}$$
*(Hence proved).*

---

#### Method 2: Moment Generating Function (MGF) Method

The MGF of $X$ is:
$$M_X(t) = E\left(e^{tX}\right) = \sum_{x=0}^n e^{tx} \binom{n}{x} p^x q^{n-x} = \sum_{x=0}^n \binom{n}{x} (pe^t)^x q^{n-x} = \mathbf{(q + pe^t)^n}$$

**First derivative with respect to $t$:**
$$M_X'(t) = \frac{d}{dt} (q + pe^t)^n = n(q + pe^t)^{n-1} \cdot (pe^t)$$
Evaluating at $t = 0$:
$$\mu_1' = E(X) = M_X'(0) = n(q + p)^{n-1} (p) = n(1)^{n-1} p = \mathbf{np}$$

**Second derivative with respect to $t$:**
$$M_X''(t) = \frac{d}{dt} \left[ n p e^t (q + pe^t)^{n-1} \right]$$
Using the product rule:
$$M_X''(t) = n p e^t (q + pe^t)^{n-1} + n p e^t \left[ (n - 1)(q + pe^t)^{n-2} \cdot p e^t \right]$$
Evaluating at $t = 0$:
$$\mu_2' = E(X^2) = M_X''(0) = n p (q + p)^{n-1} + n(n - 1) p^2 (q + p)^{n-2}$$
$$= n p + n(n - 1) p^2 = np + n^2 p^2 - np^2 = n^2 p^2 + np(1 - p) = n^2 p^2 + npq$$

**Variance:**
$$\sigma^2 = \mu_2' - (\mu_1')^2 = (n^2 p^2 + npq) - (np)^2 = \mathbf{npq} \implies \sigma = \mathbf{\sqrt{npq}}$$
*(Hence proved).*

---

### Theorem 11.4: Cumulant Generating Function of Binomial Distribution
*(Ref: Question Bank Q.118 | MHU Sheet Lec 11-14 (Binomial), Problem-2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Find the Moment Generating Function (MGF) and Cumulant Generating Function (CGF) of the Binomial Distribution, and determine the first two cumulants.**

---

#### Solution:
- **Moment Generating Function:**
  $$M_X(t) = (q + pe^t)^n$$
- **Cumulant Generating Function:**
  $$K_X(t) = \ln M_X(t) = \ln \left[ (q + pe^t)^n \right] = n \ln(q + pe^t)$$

To obtain the cumulants, differentiate $K_X(t)$ with respect to $t$:
$$K_X'(t) = n \frac{pe^t}{q + pe^t}$$
- **First Cumulant (Mean):**
  $$\kappa_1 = K_X'(0) = n \frac{p}{q + p} = n \frac{p}{1} = \mathbf{np}$$

Differentiating again:
$$K_X''(t) = n \left[ \frac{(q + pe^t)(pe^t) - (pe^t)(pe^t)}{(q + pe^t)^2} \right] = n \left[ \frac{p q e^t}{(q + pe^t)^2} \right]$$
- **Second Cumulant (Variance):**
  $$\kappa_2 = K_X''(0) = n \frac{pq}{(q + p)^2} = n \frac{pq}{1^2} = \mathbf{npq}$$

---

### Problem 11.5: Determining $n, p, q$ from Mean and Standard Deviation
*(Ref: Note Problem 10.2)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 10.2)*
**Problem Statement:**  
The mean and standard deviation of a binomial distribution are $40$ and $6$ respectively. Find the parameters $n, p$, and $q$.

---

#### Detailed Solution:
- Mean: $\mu = np = 40$.
- Standard deviation: $\sigma = \sqrt{npq} = 6 \implies npq = 36$.
- Dividing: $q = \frac{npq}{np} = \frac{36}{40} = \mathbf{0.90} = \frac{9}{10}$.
- $p = 1 - q = 1 - 0.90 = \mathbf{0.10} = \frac{1}{10}$.
- $n = \frac{40}{0.10} = \mathbf{400}$.

$$\mathbf{n = 400, \quad p = 0.10, \quad q = 0.90}$$

---

### Problem 11.6: Binomial Calculations from Mean=4 and Variance=2
*(Ref: Question Bank Q.99 | Pg 4, Q.7(b))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
If the mean and variance of a binomial distribution are $4$ and $2$ respectively, find the probability of:
1. Exactly $2$ successes ($P(X = 2)$)
2. Less than $2$ successes ($P(X < 2)$)
3. At least $3$ successes ($P(X \ge 3)$)

---

#### Detailed Solution:

**Step 1: Determine parameters $n, p, q$.**  
- Mean: $np = 4 \quad \dots \text{(1)}$
- Variance: $npq = 2 \quad \dots \text{(2)}$

Dividing equation (2) by equation (1):
$$q = \frac{npq}{np} = \frac{2}{4} = \mathbf{\frac{1}{2} = 0.5}$$
$$p = 1 - q = 1 - \frac{1}{2} = \mathbf{\frac{1}{2} = 0.5}$$
From equation (1):
$$n \left(\frac{1}{2}\right) = 4 \implies \mathbf{n = 8}$$

Therefore:
$$X \sim B\left(8, \frac{1}{2}\right)$$
The PMF is:
$$P(X = x) = \binom{8}{x} \left(\frac{1}{2}\right)^x \left(\frac{1}{2}\right)^{8-x} = \binom{8}{x} \left(\frac{1}{2}\right)^8 = \frac{\binom{8}{x}}{256}, \quad x = 0, 1, \dots, 8$$

---

#### 1. Exactly 2 Successes ($X = 2$):
$$P(X = 2) = \frac{\binom{8}{2}}{256} = \frac{\frac{8 \times 7}{2}}{256} = \frac{28}{256} = \mathbf{\frac{7}{64} \approx 0.109375} \quad (10.94\%)$$

---

#### 2. Less Than 2 Successes ($X < 2$):
$$P(X < 2) = P(X = 0) + P(X = 1)$$
- $P(X = 0) = \frac{\binom{8}{0}}{256} = \frac{1}{256}$
- $P(X = 1) = \frac{\binom{8}{1}}{256} = \frac{8}{256}$

$$P(X < 2) = \frac{1 + 8}{256} = \mathbf{\frac{9}{256} \approx 0.035156} \quad (3.52\%)$$

---

#### 3. At Least 3 Successes ($X \ge 3$):
Using the complement rule:
$$P(X \ge 3) = 1 - P(X \le 2) = 1 - [P(X = 0) + P(X = 1) + P(X = 2)]$$
$$P(X \le 2) = \frac{1 + 8 + 28}{256} = \frac{37}{256}$$
$$P(X \ge 3) = 1 - \frac{37}{256} = \mathbf{\frac{219}{256} \approx 0.855469} \quad (85.55\%)$$

$$\mathbf{\text{Ans: (i) } \frac{7}{64} \approx 0.1094, \quad \text{(ii) } \frac{9}{256} \approx 0.0352, \quad \text{(iii) } \frac{219}{256} \approx 0.8555}$$

---

### Problem 11.7: Occupational Disease in an Industry
*(Ref: Note Problem 10.3)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 10.3)*
**Problem Statement:**  
In an industry, there is a $20\%$ chance that a worker will suffer from a certain occupational disease. What is the probability that out of $6$ randomly selected workers:
1. Exactly $3$ workers will contract the disease
2. Exactly $4$ workers will contract the disease
3. $4$ or more workers will contract the disease

---

#### Detailed Solution:
- $n = 6, p = 0.2, q = 0.8, X \sim B(6, 0.2)$.
- $P(X = 3) = \binom{6}{3}(0.2)^3(0.8)^3 = 20(0.008)(0.512) = \mathbf{0.08192} \; (8.192\%)$.
- $P(X = 4) = \binom{6}{4}(0.2)^4(0.8)^2 = 15(0.0016)(0.64) = \mathbf{0.01536} \; (1.536\%)$.
- $P(X \ge 4) = P(4) + P(5) + P(6) = 0.01536 + 6(0.00032)(0.8) + (0.2)^6 = 0.01536 + 0.001536 + 0.000064 = \mathbf{0.01696} \; (1.696\%)$.

---

### Problem 11.8: Machine Bolts Defective Probability
*(Ref: Question Bank Q.105 | Pg 6, Q.7(b))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
If $20\%$ of the bolts produced by a machine are defective, determine the probability that out of $4$ bolts chosen at random:
1. Exactly $1$ bolt will be defective
2. No bolts ($0$) will be defective
3. At least $2$ bolts will be defective

---

#### Detailed Solution:

Here:
- Number of trials: $n = 4$
- Probability of a defective bolt: $p = 20\% = 0.20$
- Probability of a non-defective bolt: $q = 1 - 0.20 = 0.80$
- $X \sim B(4, 0.20)$:
  $$P(X = x) = \binom{4}{x} (0.2)^x (0.8)^{4-x}, \quad x \in \{0, 1, 2, 3, 4\}$$

---

#### 1. Exactly 1 Defective Bolt ($X = 1$):
$$P(X = 1) = \binom{4}{1} (0.2)^1 (0.8)^3 = 4 \times 0.2 \times 0.512 = \mathbf{0.4096} \quad (40.96\%)$$

---

#### 2. No Defective Bolts ($X = 0$):
$$P(X = 0) = \binom{4}{0} (0.2)^0 (0.8)^4 = 1 \times 1 \times 0.4096 = \mathbf{0.4096} \quad (40.96\%)$$

---

#### 3. At Least 2 Defective Bolts ($X \ge 2$):
Using the complement rule:
$$P(X \ge 2) = 1 - [P(X = 0) + P(X = 1)] = 1 - [0.4096 + 0.4096] = 1 - 0.8192 = \mathbf{0.1808} \quad (18.08\%)$$

$$\mathbf{\text{Ans: (i) } 0.4096, \quad \text{(ii) } 0.4096, \quad \text{(iii) } 0.1808}$$

---

### Problem 11.9: Children Gender Probabilities in a Family of 4
*(Ref: Note Problem 10.4)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 10.4)*
**Problem Statement:**  
In a family of $4$ children, assuming male and female births are equally likely ($p = q = 1/2$), find the probability of:
1. Exactly $1$ boy: $P(X = 1) = \frac{\binom{4}{1}}{16} = \mathbf{\frac{1}{4} = 0.25}$
2. At least $1$ boy: $1 - P(X = 0) = 1 - \frac{1}{16} = \mathbf{\frac{15}{16} = 0.9375}$
3. At least $1$ boy and $1$ girl: $1 - [P(0) + P(4)] = 1 - \frac{2}{16} = \mathbf{\frac{7}{8} = 0.875}$
4. Exactly $2$ boys and $2$ girls: $\frac{\binom{4}{2}}{16} = \mathbf{\frac{3}{8} = 0.375}$

---

### Problem 11.10: Server Signal Transmission Success
*(Ref: Question Bank Q.122 | MHU Sheet Lec 11-14 (Binomial), H.W. Problem-6)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Seventy percent ($70\%$) of signals sent from a server reach their destination properly. If $3$ signals are checked randomly, find the probability that:
1. At least $1$ signal reaches properly.
2. At most $2$ signals reach properly (at best $2$).

---

#### Detailed Solution:

Here:
- Number of signals tested: $n = 3$
- Probability of reaching properly: $p = 70\% = 0.7$
- Probability of failing to reach properly: $q = 1 - 0.7 = 0.3$
- Let $X$ be the number of signals reaching properly: $X \sim B(3, 0.7)$.
$$P(X = x) = \binom{3}{x} (0.7)^x (0.3)^{3-x}$$

#### 1. At Least 1 Signal Reaches Properly ($X \ge 1$):
$$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{3}{0} (0.7)^0 (0.3)^3 = 1 - (0.3)^3 = 1 - 0.027 = \mathbf{0.973} \quad (97.3\%)$$

#### 2. At Most 2 Signals Reach Properly ($X \le 2$):
$$P(X \le 2) = 1 - P(X = 3) = 1 - \binom{3}{3} (0.7)^3 (0.3)^0 = 1 - (0.7)^3 = 1 - 0.343 = \mathbf{0.657} \quad (65.7\%)$$

$$\mathbf{\text{Ans: (a) } 0.973, \quad \text{(b) } 0.657}$$

---

### Problem 11.11: Chebyshev's Inequality Applied to Binomial Die Tosses
*(Ref: Question Bank Q.120 | MHU Sheet Lec 11-14 (Binomial), Problem-4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A symmetric fair six-sided die is thrown $600$ times. Using **Chebyshev's inequality**, estimate the lower bound of the probability of getting between $80$ and $120$ sixes (inclusive).

---

#### Detailed Solution:

**Step 1: Model the Experiment as a Binomial RV.**  
- Total rolls: $n = 600$
- Success = rolling a '$6$' $\implies p = \frac{1}{6}$
- Failure = rolling not a '$6$' $\implies q = 1 - \frac{1}{6} = \frac{5}{6}$
- Number of sixes: $X \sim B\left(600, \frac{1}{6}\right)$.

**Step 2: Compute Mean and Variance.**  
- Mean:
  $$\mu = E(X) = n p = 600 \times \frac{1}{6} = 100$$
- Variance:
  $$\sigma^2 = \text{Var}(X) = n p q = 600 \times \frac{1}{6} \times \frac{5}{6} = 100 \times \frac{5}{6} = \frac{500}{6} = \frac{250}{3} \approx 83.333$$
- Standard Deviation:
  $$\sigma = \sqrt{\frac{250}{3}} \approx 9.1287$$

**Step 3: State Chebyshev's Inequality.**  
Chebyshev's inequality states that for any random variable $X$ with mean $\mu$ and finite variance $\sigma^2$, and for any constant $k > 0$:
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2} \implies P(|X - \mu| < k\sigma) \ge 1 - \frac{1}{k^2}$$

**Step 4: Relate the Event to $|X - \mu| < k\sigma$.**  
We want the probability of getting between $80$ and $120$ sixes:
$$80 \le X \le 120 \iff 80 - 100 \le X - 100 \le 120 - 100 \iff -20 \le X - 100 \le 20$$
$$|X - \mu| \le 20$$

Setting $k\sigma = 20$:
$$k^2 \sigma^2 = 20^2 = 400$$
$$k^2 = \frac{400}{\sigma^2} = \frac{400}{250 / 3} = \frac{400 \times 3}{250} = \frac{1200}{250} = \frac{24}{5} = 4.8$$

**Step 5: Compute the Bound.**  
$$\frac{1}{k^2} = \frac{5}{24}$$
$$P(80 \le X \le 120) \ge 1 - \frac{1}{k^2} = 1 - \frac{5}{24} = \mathbf{\frac{19}{24}} \approx \mathbf{0.79167}$$

$$\mathbf{P(80 \le X \le 120) \ge \frac{19}{24} \approx 0.7917 \quad (\ge 79.17\%)}$$

---


## 12. Poisson Distribution

### Question 12.1: Definition & Conditions as a Limiting Case
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Question 11.1)*
**Define the Poisson Distribution and state the conditions under which the Binomial Distribution tends to the Poisson Distribution.**

---

#### Solution:
The **Poisson Distribution** is a discrete probability distribution that models the number of occurrences of rare events over a fixed interval of time, length, area, or volume.

#### Limiting Conditions:
The Binomial Distribution $B(n, p)$ tends to the Poisson Distribution under three simultaneous conditions:
1. $n \to \infty$ (number of trials is indefinitely large).
2. $p \to 0$ (probability of success is very small).
3. $n p = \lambda$ remains a finite positive constant (average rate).

#### Probability Mass Function:
$$P(X = x) = f(x; \lambda) = \frac{e^{-\lambda} \lambda^x}{x!}, \quad x = 0, 1, 2, 3, \dots, \infty$$

#### Characteristic Feature:
For a Poisson distribution, **$\text{Mean} = \text{Variance} = \lambda$**.

---

### Problem 12.2: Rare Reaction to an Injection
*(Ref: Original Note Problem 11.2 | Classical Rare Event Application)*  
> 🏷️ **Identifier:** 📌 `[ORIGINAL NOTE]` *(Formerly Problem 11.2)*
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

---

### Theorem 12.3: Mathematical Proof that Binomial Tends to Poisson Distribution
*(Ref: Question Bank Q.93, Q.101, Q.130 | Pg 1 Q.8(a), Pg 4 Q.8(a), MHU Sheet Lec 11-14 (Poisson), Problem-1)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Show mathematically that under certain conditions, the Binomial Distribution tends to the Poisson Distribution.**

---

#### Detailed Proof:

Let $X \sim B(n, p)$. The probability of $x$ successes in $n$ independent trials is:
$$P(X = x) = \binom{n}{x} p^x (1 - p)^{n-x} = \frac{n(n - 1)(n - 2) \dots (n - x + 1)}{x!} p^x (1 - p)^{n-x}$$

Let $\lambda = np$, so that $p = \frac{\lambda}{n}$ and $1 - p = 1 - \frac{\lambda}{n}$.  
Substitute $p = \frac{\lambda}{n}$ into the PMF:
$$P(X = x) = \frac{n(n - 1)(n - 2) \dots (n - x + 1)}{x!} \left( \frac{\lambda}{n} \right)^x \left( 1 - \frac{\lambda}{n} \right)^{n-x}$$
Rearranging powers of $n$:
$$P(X = x) = \frac{\lambda^x}{x!} \left[ \frac{n(n - 1)(n - 2) \dots (n - x + 1)}{n^x} \right] \left( 1 - \frac{\lambda}{n} \right)^n \left( 1 - \frac{\lambda}{n} \right)^{-x}$$
Distribute $n^x$ as $n \times n \times \dots \times n$ across the $x$ numerator factors:
$$P(X = x) = \frac{\lambda^x}{x!} \left[ 1 \cdot \left( 1 - \frac{1}{n} \right) \left( 1 - \frac{2}{n} \right) \dots \left( 1 - \frac{x - 1}{n} \right) \right] \left( 1 - \frac{\lambda}{n} \right)^n \left( 1 - \frac{\lambda}{n} \right)^{-x}$$

Now take the limit as $n \to \infty$ keeping $x$ and $\lambda$ fixed:
1. For each fixed $k \in \{1, 2, \dots, x - 1\}$:
   $$\lim_{n \to \infty} \left( 1 - \frac{k}{n} \right) = 1$$
   Therefore:
   $$\lim_{n \to \infty} \left[ 1 \cdot \left( 1 - \frac{1}{n} \right) \dots \left( 1 - \frac{x - 1}{n} \right) \right] = 1$$

2. By the standard calculus limit definition of the exponential function:
   $$\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^n = e^{-\lambda}$$

3. Since $x$ is finite:
   $$\lim_{n \to \infty} \left( 1 - \frac{\lambda}{n} \right)^{-x} = (1 - 0)^{-x} = 1$$

Combining all three limits:
$$\lim_{n \to \infty} P(X = x) = \frac{\lambda^x}{x!} \cdot (1) \cdot e^{-\lambda} \cdot (1) = \mathbf{\frac{e^{-\lambda} \lambda^x}{x!}}$$
*(Hence proved: The Poisson distribution is the limiting form of the Binomial distribution).*

---

### Theorem 12.4: MGF, Mean, and Variance of Poisson Distribution
*(Ref: Question Bank Q.97, Q.131 | Pg 3, Q.8(a), MHU Sheet Lec 11-14 (Poisson), Problem-2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Find the Moment Generating Function (MGF) of the Poisson Distribution, and from that MGF, derive the Mean and Variance.**

---

#### Detailed Proof:

**Step 1: Derivation of the MGF $M_X(t)$:**
$$M_X(t) = E\left(e^{tX}\right) = \sum_{x=0}^{\infty} e^{tx} P(X = x) = \sum_{x=0}^{\infty} e^{tx} \frac{e^{-\lambda} \lambda^x}{x!}$$
Factor out $e^{-\lambda}$:
$$M_X(t) = e^{-\lambda} \sum_{x=0}^{\infty} \frac{(\lambda e^t)^x}{x!}$$
Recognize the Taylor series for the exponential function $\sum_{x=0}^{\infty} \frac{u^x}{x!} = e^u$ where $u = \lambda e^t$:
$$M_X(t) = e^{-\lambda} \cdot e^{\lambda e^t} = \mathbf{e^{\lambda(e^t - 1)}}$$

---

**Step 2: Derivation of Mean $\mu = E(X)$:**  
Differentiate $M_X(t)$ with respect to $t$:
$$M_X'(t) = \frac{d}{dt} e^{\lambda(e^t - 1)} = e^{\lambda(e^t - 1)} \cdot \frac{d}{dt} [\lambda(e^t - 1)] = \lambda e^t e^{\lambda(e^t - 1)}$$
Evaluating at $t = 0$:
$$\mu_1' = E(X) = M_X'(0) = \lambda e^0 e^{\lambda(e^0 - 1)} = \lambda(1) e^{\lambda(0)} = \mathbf{\lambda}$$
*(The Mean of a Poisson distribution is $\lambda$).*

---

**Step 3: Derivation of Variance $\sigma^2$:**  
Differentiate $M_X'(t)$ with respect to $t$ using the product rule:
$$M_X''(t) = \frac{d}{dt} \left[ \lambda e^t e^{\lambda(e^t - 1)} \right] = \lambda e^t e^{\lambda(e^t - 1)} + \lambda e^t \left[ \lambda e^t e^{\lambda(e^t - 1)} \right]$$
$$M_X''(t) = \lambda e^t e^{\lambda(e^t - 1)} [1 + \lambda e^t]$$
Evaluating at $t = 0$:
$$\mu_2' = E(X^2) = M_X''(0) = \lambda (1)(1)[1 + \lambda(1)] = \lambda(1 + \lambda) = \lambda + \lambda^2$$

Now evaluate the Variance:
$$\text{Var}(X) = \sigma^2 = E(X^2) - [E(X)]^2 = (\lambda + \lambda^2) - \lambda^2 = \mathbf{\lambda}$$
Standard Deviation:
$$\sigma = \mathbf{\sqrt{\lambda}}$$
*(Hence proved).*

---

### Theorem 12.5: Recurrence Relation of the Poisson Distribution
*(Ref: Question Bank Q.132 | MHU Sheet Lec 11-14 (Poisson), Problem-3)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**1. Establish the recurrence relation for the Poisson Distribution:**
$$P(X = x + 1) = \frac{\lambda}{x + 1} P(X = x)$$
**2. If the variance of a Poisson distribution is $2$, find the probabilities for $r = 1, 2, 3, 4$ using this recurrence relation, and also find $P(X \ge 4)$.**

---

#### Detailed Solution:

#### 1. Derivation of Recurrence Formula:
$$P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}$$
$$P(X = x + 1) = \frac{e^{-\lambda} \lambda^{x+1}}{(x + 1)!} = \frac{e^{-\lambda} \lambda^x \cdot \lambda}{(x + 1) \cdot x!} = \frac{\lambda}{x + 1} \left[ \frac{e^{-\lambda} \lambda^x}{x!} \right]$$
Therefore:
$$\mathbf{P(X = x + 1) = \frac{\lambda}{x + 1} P(X = x)}$$
*(Hence proved).*

---

#### 2. Calculation for Variance $\lambda = 2$:
Given $\text{Var}(X) = \lambda = 2$.
Base probability at $x = 0$:
$$P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!} = e^{-2} \approx 0.135335$$

Using the recurrence relation $P(r) = \frac{2}{r} P(r - 1)$:
- For $r = 1$:
  $$P(1) = \frac{2}{1} P(0) = 2 e^{-2} \approx 2(0.135335) = \mathbf{0.270670} \quad (27.07\%)$$
- For $r = 2$:
  $$P(2) = \frac{2}{2} P(1) = 1 \cdot P(1) = 2 e^{-2} \approx \mathbf{0.270670} \quad (27.07\%)$$
- For $r = 3$:
  $$P(3) = \frac{2}{3} P(2) = \frac{2}{3}(2 e^{-2}) = \frac{4}{3} e^{-2} \approx \frac{4}{3}(0.135335) = \mathbf{0.180447} \quad (18.04\%)$$
- For $r = 4$:
  $$P(4) = \frac{2}{4} P(3) = \frac{1}{2} \left( \frac{4}{3} e^{-2} \right) = \frac{2}{3} e^{-2} \approx \frac{2}{3}(0.135335) = \mathbf{0.090223} \quad (9.02\%)$$

---

#### 3. Compute $P(X \ge 4)$:
Using the complement rule:
$$P(X \ge 4) = 1 - P(X \le 3) = 1 - [P(0) + P(1) + P(2) + P(3)]$$
Substitute terms in terms of $e^{-2}$:
$$P(X \le 3) = e^{-2} + 2e^{-2} + 2e^{-2} + \frac{4}{3}e^{-2} = \left( 5 + \frac{4}{3} \right) e^{-2} = \frac{19}{3} e^{-2}$$
$$P(X \le 3) \approx \frac{19}{3} \times 0.135335 = 0.857122$$
$$P(X \ge 4) = 1 - 0.857122 = \mathbf{0.142878} \approx \mathbf{0.1429} \quad (14.29\%)$$

$$\mathbf{P(1) = 0.2707, \quad P(2) = 0.2707, \quad P(3) = 0.1804, \quad P(4) = 0.0902, \quad P(X \ge 4) \approx 0.1429}$$

---

### Problem 12.6: Defective Electric Bulbs in Large Samples
*(Ref: Question Bank Q.92, Q.100, Q.121 | Pg 1 Q.7(b), Pg 4 Q.7(c), MHU Sheet Lec 11-14 (Binomial), Problem-5)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
If $3\%$ of electric bulbs manufactured by a company are defective ($p = 0.03$):
1. Find the probability that in a sample of $200$ bulbs:
   - (i) $5$ or more will be defective ($P(X \ge 5)$).
   - (ii) Between $1$ and $3$ will be defective ($P(1 < X < 3)$ or $P(1 \le X \le 3)$).
2. Find the probability that in a sample of $100$ bulbs:
   - (i) Exactly $3$ will be defective.
   - (ii) At least $4$ will be defective.
   - (iii) At most $2$ will be defective.

---

#### Detailed Solution:

#### Part 1: Sample of $n = 200$ Bulbs
Since $n = 200$ is large and $p = 0.03$ is small, use Poisson distribution:
$$\lambda = np = 200 \times 0.03 = \mathbf{6}$$
$$P(X = x) = \frac{e^{-6} \cdot 6^x}{x!}, \quad e^{-6} \approx 0.00247875$$

- **(i) 5 or more defective ($X \ge 5$):**
  $$P(X \ge 5) = 1 - P(X \le 4) = 1 - \sum_{x=0}^4 \frac{e^{-6} \cdot 6^x}{x!}$$
  Compute terms:
  - $P(0) = e^{-6} \approx 0.002479$
  - $P(1) = 6 e^{-6} \approx 0.014873$
  - $P(2) = \frac{36}{2} e^{-6} = 18 e^{-6} \approx 0.044618$
  - $P(3) = \frac{216}{6} e^{-6} = 36 e^{-6} \approx 0.089235$
  - $P(4) = \frac{1296}{24} e^{-6} = 54 e^{-6} \approx 0.133853$
  Sum for $X \le 4$:
  $$P(X \le 4) = (1 + 6 + 18 + 36 + 54) e^{-6} = 115 e^{-6} \approx 115 \times 0.00247875 = 0.285056$$
  $$P(X \ge 5) = 1 - 0.285056 = \mathbf{0.714944} \approx \mathbf{0.7149} \quad (71.49\%)$$

- **(ii) Between 1 and 3 defective:**
  - Inclusive ($1 \le X \le 3$):
    $$P(1 \le X \le 3) = P(1) + P(2) + P(3) = (6 + 18 + 36) e^{-6} = 60 e^{-6} \approx 60 \times 0.00247875 = \mathbf{0.148725} \approx \mathbf{0.1487}$$
  - Strictly between ($X = 2$):
    $$P(X = 2) = 18 e^{-6} \approx \mathbf{0.0446}$$

---

#### Part 2: Sample of $n = 100$ Bulbs
$$\lambda = np = 100 \times 0.03 = \mathbf{3}$$
$$P(X = x) = \frac{e^{-3} \cdot 3^x}{x!}, \quad e^{-3} \approx 0.049787$$

- **(i) Exactly 3 defective:**
  $$P(X = 3) = \frac{e^{-3} \cdot 3^3}{3!} = \frac{27 e^{-3}}{6} = 4.5 e^{-3} \approx 4.5 \times 0.049787 = \mathbf{0.22404} \approx \mathbf{0.2240} \quad (22.40\%)$$

- **(ii) At least 4 defective ($X \ge 4$):**
  $$P(X \ge 4) = 1 - P(X \le 3)$$
  - $P(0) = e^{-3} \approx 0.049787$
  - $P(1) = 3 e^{-3} \approx 0.149361$
  - $P(2) = \frac{9}{2} e^{-3} = 4.5 e^{-3} \approx 0.224042$
  - $P(3) = 4.5 e^{-3} \approx 0.224042$
  Sum for $X \le 3$:
  $$P(X \le 3) = (1 + 3 + 4.5 + 4.5) e^{-3} = 13 e^{-3} \approx 13 \times 0.049787 = 0.647231$$
  $$P(X \ge 4) = 1 - 0.647231 = \mathbf{0.352769} \approx \mathbf{0.3528} \quad (35.28\%)$$

- **(iii) At most 2 defective ($X \le 2$):**
  $$P(X \le 2) = P(0) + P(1) + P(2) = (1 + 3 + 4.5) e^{-3} = 8.5 e^{-3} \approx 8.5 \times 0.049787 = \mathbf{0.42319} \approx \mathbf{0.4232} \quad (42.32\%)$$

---

### Problem 12.7: Quality Guarantee for Pin Manufacturer
*(Ref: Question Bank Q.109 | Pg 14, CT-03, Q.3 (Or))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
A manufacturer of pins knows that $5\%$ of his product is defective ($p = 0.05$). If he sells pins in boxes of $100$ and guarantees that not more than $10$ pins will be defective, what is the approximate probability that a box will fail to meet the guaranteed quality?

---

#### Detailed Solution:

Here:
- $n = 100$ (large)
- $p = 5\% = 0.05$ (small)
- Average defective pins per box:
  $$\lambda = np = 100 \times 0.05 = \mathbf{5}$$

A box **fails to meet the guaranteed quality** if it contains strictly more than $10$ defective pins ($X > 10$):
$$P(\text{Failure to meet guarantee}) = P(X > 10) = 1 - P(X \le 10) = 1 - \sum_{x=0}^{10} \frac{e^{-5} \cdot 5^x}{x!}$$

Using the Poisson cumulative distribution values for $\lambda = 5$:
- $P(X \le 10) = e^{-5} \sum_{x=0}^{10} \frac{5^x}{x!} \approx 0.9863$

Therefore:
$$P(X > 10) = 1 - 0.9863 = \mathbf{0.0137} \quad (1.37\%)$$

$$\mathbf{P(\text{Box fails guarantee}) \approx 0.0137 \quad (1.37\%) }$$

---

### Problem 12.8: Laboratory Beaker Breakage (Binomial vs. Poisson)
*(Ref: Question Bank Q.133 | MHU Sheet Lec 11-14 (Poisson), Problem-4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The probability of breaking a glass beaker while heating in a laboratory is $0.012$. If we heat $200$ such glass beakers, find the probability of breaking exactly $2$ beakers using:
1. **Binomial Distribution**
2. **Poisson Distribution**

---

#### Detailed Solution:

Here:
- $n = 200$
- $p = 0.012$
- $q = 1 - 0.012 = 0.988$

#### 1. Using Binomial Distribution:
$$P(X = 2) = \binom{200}{2} (0.012)^2 (0.988)^{198}$$
- $\binom{200}{2} = \frac{200 \times 199}{2} = 19,900$
- $(0.012)^2 = 0.000144$
- $(0.988)^{198} = e^{198 \ln(0.988)} \approx e^{198(-0.0120728)} = e^{-2.3904} \approx 0.091593$

$$P(X = 2) = 19900 \times 0.000144 \times 0.091593 = 2.8656 \times 0.091593 = \mathbf{0.26246} \approx \mathbf{0.2625}$$

---

#### 2. Using Poisson Distribution:
$$\lambda = np = 200 \times 0.012 = \mathbf{2.4}$$
$$P(X = 2) = \frac{e^{-2.4} \cdot (2.4)^2}{2!} = \frac{5.76}{2} e^{-2.4} = 2.88 e^{-2.4}$$
Using $e^{-2.4} \approx 0.090718$:
$$P(X = 2) = 2.88 \times 0.090718 = \mathbf{0.26127} \approx \mathbf{0.2613}$$

*(Comparison: The Poisson approximation $0.2613$ agrees remarkably well with the exact Binomial probability $0.2625$, with a relative error of less than $0.5\%$).*

$$\mathbf{\text{Ans: (i) Binomial } \approx 0.2625, \quad \text{(ii) Poisson } \approx 0.2613}$$

---

### Problem 12.9: Machine Bolts Defective Rate (Boxes of 50)
*(Ref: Question Bank Q.134 | MHU Sheet Lec 11-14 (Poisson), Problem-5)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Suppose $3\%$ of bolts made by a machine are defective, the defects occurring at random during production. If bolts are packaged $50$ per box, find:
1. The exact probability (using Binomial distribution)
2. The Poisson approximation  
that a given box will contain exactly $5$ defectives.

---

#### Detailed Solution:

Here: $n = 50, p = 0.03, q = 0.97$.

#### 1. Exact Binomial Probability:
$$P(X = 5) = \binom{50}{5} (0.03)^5 (0.97)^{45}$$
- $\binom{50}{5} = \frac{50 \times 49 \times 48 \times 47 \times 46}{120} = 2,118,760$
- $(0.03)^5 = 2.43 \times 10^{-8}$
- $(0.97)^{45} \approx 0.254424$
$$P(X = 5) = 2,118,760 \times (2.43 \times 10^{-8}) \times 0.254424 = 0.051486 \times 0.254424 = \mathbf{0.013099} \approx \mathbf{0.0131}$$

---

#### 2. Poisson Approximation:
$$\lambda = np = 50 \times 0.03 = \mathbf{1.5}$$
$$P(X = 5) = \frac{e^{-1.5} \cdot (1.5)^5}{5!} = \frac{e^{-1.5} \times 7.59375}{120} = 0.06328125 e^{-1.5}$$
Using $e^{-1.5} \approx 0.22313$:
$$P(X = 5) = 0.06328125 \times 0.22313 = \mathbf{0.014120} \approx \mathbf{0.0141}$$

$$\mathbf{\text{Ans: (a) Exact Binomial: } \approx 0.0131, \quad \text{(b) Poisson Approximation: } \approx 0.0141}$$

---

### Problem 12.10: Drawing the Ace of Spades in 104 Consecutive Trials
*(Ref: Question Bank Q.135 | MHU Sheet Lec 11-14 (Poisson), Problem-6)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
Using the Poisson distribution, find the probability that the Ace of Spades will be drawn from a pack of well-shuffled playing cards at least once in $104$ consecutive independent trials (with replacement).

---

#### Detailed Solution:

In each trial:
- Total cards $= 52$
- Success = drawing the Ace of Spades $\implies p = \frac{1}{52}$
- Number of trials $n = 104$
- Average rate:
  $$\lambda = np = 104 \times \frac{1}{52} = \mathbf{2}$$

Let $X$ be the number of times the Ace of Spades is drawn: $X \sim \text{Poisson}(\lambda = 2)$.  
We want the probability of drawing it **at least once** ($X \ge 1$):
$$P(X \ge 1) = 1 - P(X = 0)$$
$$P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!} = e^{-2}$$
Using $e^{-2} \approx 0.135335$:
$$P(X \ge 1) = 1 - e^{-2} \approx 1 - 0.135335 = \mathbf{0.864665} \approx \mathbf{0.8647} \quad (86.47\%)$$

$$\mathbf{P(\text{At least once}) = 1 - e^{-2} \approx 0.8647 \quad (86.47\%) }$$

---


## 13. Normal Distribution (Continuous Probability Distribution)

### Question 13.1: Definition & Mathematical Model of Normal Distribution
*(Ref: Question Bank Q.104, Q.123 | Pg 6 Q.7(a), MHU Sheet Lec 11-14 (Normal), Problem-1)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Define the Normal Distribution. Write down its probability density function (PDF), define the Standard Normal Variable $Z$, and give the standard normal density function.**

---

#### Solution:

A continuous random variable $X$ is said to follow a **Normal Distribution** with parameters $\mu$ (mean) and $\sigma^2$ (variance), denoted as $X \sim N(\mu, \sigma^2)$, if its probability density function is given by:
$$f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$
where:
- $\mu \in (-\infty, \infty)$ is the mean (location parameter).
- $\sigma > 0$ is the standard deviation (scale parameter).
- $\pi \approx 3.14159$ and $e \approx 2.71828$.

#### Standard Normal Distribution:
The **Standard Normal Variable** $Z$ is defined by the transformation:
$$Z = \frac{X - \mu}{\sigma}$$
The variable $Z$ has mean $0$ and variance $1$, denoted as $Z \sim N(0, 1)$. Its probability density function $\phi(z)$ is:
$$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}, \quad -\infty < z < \infty$$

---

### Theorem 13.2: Total Area Under Normal Curve Equals Unity
*(Ref: Question Bank Q.123 | MHU Sheet Lec 11-14 (Normal), Problem-1)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Prove that the total probability of the Normal Distribution is unity, i.e.:**
$$\int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \, dx = 1$$

---

#### Detailed Proof:

Let $I = \int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \, dx$.  
Substitute $z = \frac{x - \mu}{\sigma} \implies dx = \sigma \, dz$.  
As $x \to -\infty$, $z \to -\infty$; as $x \to \infty$, $z \to \infty$.  
$$I = \int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2\pi}} e^{-z^2/2} (\sigma \, dz) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-z^2/2} \, dz$$

Let $J = \int_{-\infty}^{\infty} e^{-z^2/2} \, dz$. To evaluate this improper integral, compute $J^2$:
$$J^2 = \left( \int_{-\infty}^{\infty} e^{-x^2/2} \, dx \right) \left( \int_{-\infty}^{\infty} e^{-y^2/2} \, dy \right) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2 + y^2)/2} \, dx \, dy$$

Transform to polar coordinates:
- $x = r \cos\theta, \quad y = r \sin\theta \implies x^2 + y^2 = r^2$
- The Jacobian is $dx \, dy = r \, dr \, d\theta$
- Limits: $0 \le r < \infty$ and $0 \le \theta \le 2\pi$.

$$J^2 = \int_{0}^{2\pi} d\theta \int_{0}^{\infty} r e^{-r^2/2} \, dr$$
- $\int_0^{2\pi} d\theta = 2\pi$
- $\int_{0}^{\infty} r e^{-r^2/2} \, dr = \left[ -e^{-r^2/2} \right]_0^\infty = 0 - (-1) = 1$

Therefore:
$$J^2 = 2\pi \times 1 = 2\pi \implies J = \sqrt{2\pi}$$

Substitute $J = \sqrt{2\pi}$ back into $I$:
$$I = \frac{1}{\sqrt{2\pi}} \cdot J = \frac{1}{\sqrt{2\pi}} \cdot \sqrt{2\pi} = \mathbf{1}$$
*(Hence proved: The total probability under the Normal curve is identically unity).*

---

### Theorem 13.3: Mean, Median, and Mode of Normal Distribution Coincide
*(Ref: Question Bank Q.91, Q.104, Q.126 | Pg 1 Q.7(a), Pg 6 Q.7(a), MHU Sheet Lec 11-14 (Normal), Problem-4)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Prove that the Mean, Median, and Mode of the Normal Distribution coincide, i.e.:**
$$\text{Mean} = \text{Median} = \text{Mode} = \mu$$

---

#### Detailed Proof:

#### 1. Proof that $\text{Mean} = \mu$:
$$E(X) = \int_{-\infty}^{\infty} x \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \, dx$$
Substitute $z = \frac{x - \mu}{\sigma} \implies x = \mu + \sigma z$ and $dx = \sigma dz$:
$$E(X) = \int_{-\infty}^{\infty} (\mu + \sigma z) \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz = \mu \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz + \frac{\sigma}{\sqrt{2\pi}} \int_{-\infty}^{\infty} z e^{-z^2/2} \, dz$$
- The first integral is $\mu \times 1 = \mu$.
- The second integrand $g(z) = z e^{-z^2/2}$ is an **odd function** ($g(-z) = -g(z)$), so its integral over symmetric limits $(-\infty, \infty)$ is identically zero:
  $$\int_{-\infty}^{\infty} z e^{-z^2/2} \, dz = 0$$

Therefore:
$$\mathbf{E(X) = \mu}$$

---

#### 2. Proof that $\text{Median} = \mu$:
The median $M_e$ is the value of $x$ such that $P(X \le M_e) = 0.5$:
$$\int_{-\infty}^{M_e} f(x) \, dx = \frac{1}{2}$$
Split the total integral into two halves at $x = \mu$:
$$\int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^{\mu} f(x) \, dx + \int_{\mu}^{\infty} f(x) \, dx = 1$$
In the first integral, substitute $z = \frac{x - \mu}{\sigma}$:
$$\int_{-\infty}^{\mu} f(x) \, dx = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{0} e^{-z^2/2} \, dz$$
Since $e^{-z^2/2}$ is completely symmetric about $z = 0$:
$$\int_{-\infty}^{0} e^{-z^2/2} \, dz = \int_{0}^{\infty} e^{-z^2/2} \, dz = \frac{\sqrt{2\pi}}{2}$$
Thus:
$$\int_{-\infty}^{\mu} f(x) \, dx = \frac{1}{\sqrt{2\pi}} \cdot \frac{\sqrt{2\pi}}{2} = \frac{1}{2} = 0.5$$
By definition of the median, since $\int_{-\infty}^{\mu} f(x) dx = 0.5$:
$$\mathbf{M_e = \mu}$$

---

#### 3. Proof that $\text{Mode} = \mu$:
The mode is the point where the PDF $f(x)$ attains its maximum value.  
Taking the natural logarithm of $f(x)$:
$$\ln f(x) = \ln\left(\frac{1}{\sigma \sqrt{2\pi}}\right) - \frac{(x - \mu)^2}{2\sigma^2}$$
Differentiating with respect to $x$:
$$\frac{f'(x)}{f(x)} = -\frac{2(x - \mu)}{2\sigma^2} = -\frac{x - \mu}{\sigma^2} \implies f'(x) = -\frac{x - \mu}{\sigma^2} f(x)$$
Set $f'(x) = 0$:
$$-\frac{x - \mu}{\sigma^2} f(x) = 0$$
Since $f(x) > 0$ for all real $x$, we must have:
$$x - \mu = 0 \implies x = \mu$$

Differentiating again to check the second derivative:
$$f''(x) = -\frac{1}{\sigma^2} f(x) - \frac{x - \mu}{\sigma^2} f'(x)$$
At $x = \mu$:
$$f''(\mu) = -\frac{1}{\sigma^2} f(\mu) - 0 = -\frac{1}{\sigma^3 \sqrt{2\pi}} < 0$$
Since $f''(\mu) < 0$, $f(x)$ attains its absolute global maximum at $x = \mu$.  
Therefore:
$$\mathbf{M_o = \mu}$$

**Conclusion:**
$$\mathbf{\text{Mean} = \text{Median} = \text{Mode} = \mu}$$
*(Hence proved: For the Normal Distribution, Mean, Median, and Mode all coincide at $\mu$).*

---

### Theorem 13.4: Derivation of Variance of Normal Distribution
*(Ref: Question Bank Q.124 | MHU Sheet Lec 11-14 (Normal), Problem-2)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Derive the Variance $\text{Var}(X) = \sigma^2$ of the Normal Distribution from first principles.**

---

#### Detailed Proof:

By definition of variance:
$$\text{Var}(X) = \sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) \, dx = \int_{-\infty}^{\infty} (x - \mu)^2 \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \, dx$$
Substitute $z = \frac{x - \mu}{\sigma} \implies x - \mu = \sigma z$ and $dx = \sigma dz$:
$$\text{Var}(X) = \int_{-\infty}^{\infty} (\sigma z)^2 \frac{1}{\sigma \sqrt{2\pi}} e^{-z^2/2} (\sigma \, dz) = \frac{\sigma^2}{\sqrt{2\pi}} \int_{-\infty}^{\infty} z^2 e^{-z^2/2} \, dz$$
Since the integrand is even:
$$\text{Var}(X) = \frac{2\sigma^2}{\sqrt{2\pi}} \int_{0}^{\infty} z \cdot (z e^{-z^2/2}) \, dz$$
Use integration by parts:
- Let $u = z \implies du = dz$
- Let $dv = z e^{-z^2/2} dz \implies v = -e^{-z^2/2}$
$$\int_{0}^{\infty} z (z e^{-z^2/2}) \, dz = \left[ -z e^{-z^2/2} \right]_0^\infty - \int_{0}^{\infty} (-e^{-z^2/2}) \, dz$$
- The boundary term: $\lim_{z \to \infty} (-z e^{-z^2/2}) - 0 = 0$.
- The integral term: $\int_{0}^{\infty} e^{-z^2/2} \, dz = \frac{\sqrt{2\pi}}{2}$.

Therefore:
$$\int_{-\infty}^{\infty} z^2 e^{-z^2/2} \, dz = 2 \left( \frac{\sqrt{2\pi}}{2} \right) = \sqrt{2\pi}$$
Substituting this back:
$$\text{Var}(X) = \frac{\sigma^2}{\sqrt{2\pi}} \cdot \sqrt{2\pi} = \mathbf{\sigma^2}$$
Standard Deviation:
$$\text{SD}(X) = \mathbf{\sigma}$$
*(Hence proved).*

---

### Theorem 13.5: MGF, Skewness, and Kurtosis of Normal Distribution
*(Ref: Question Bank Q.125 | MHU Sheet Lec 11-14 (Normal), Problem-3)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Find the Moment Generating Function (MGF) of the Normal Distribution. From it, determine the Skewness ($\beta_1$) and Kurtosis ($\beta_2$) and comment on the shape.**

---

#### Detailed Proof:

**Step 1: Derivation of the MGF $M_X(t)$:**
$$M_X(t) = E\left(e^{tX}\right) = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \, dx$$
Substitute $z = \frac{x - \mu}{\sigma} \implies x = \mu + \sigma z$:
$$M_X(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{t(\mu + \sigma z)} e^{-z^2/2} \, dz = e^{\mu t} \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(z^2 - 2\sigma t z)} \, dz$$
Complete the square in the exponent:
$$z^2 - 2\sigma t z = (z - \sigma t)^2 - \sigma^2 t^2$$
$$-\frac{1}{2}(z^2 - 2\sigma t z) = -\frac{1}{2}(z - \sigma t)^2 + \frac{1}{2}\sigma^2 t^2$$

Factor out $e^{\frac{1}{2}\sigma^2 t^2}$:
$$M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2} \left[ \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(z - \sigma t)^2} \, dz \right]$$
The integral in brackets is the total area under a normal curve shifted by $\sigma t$, which equals $1$.  
Therefore, the MGF of $X \sim N(\mu, \sigma^2)$ is:
$$\mathbf{M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2 t^2}}$$

---

**Step 2: Moments About the Mean:**  
The central moment generating function is $M_{X - \mu}(t) = e^{-\mu t} M_X(t)$:
$$M_{X - \mu}(t) = e^{\frac{1}{2}\sigma^2 t^2}$$
Expanding as a Maclaurin series in $t$:
$$e^{\frac{1}{2}\sigma^2 t^2} = 1 + \left( \frac{\sigma^2 t^2}{2} \right) + \frac{1}{2!} \left( \frac{\sigma^2 t^2}{2} \right)^2 + \frac{1}{3!} \left( \frac{\sigma^2 t^2}{2} \right)^3 + \dots$$
$$= 1 + \frac{\sigma^2}{2} t^2 + \frac{\sigma^4}{8} t^4 + \frac{\sigma^6}{48} t^6 + \dots$$

Expressing in terms of central moments $\mu_r = \text{coefficient of } \frac{t^r}{r!}$:
- For $r = 1$: $\mu_1 = 0$
- For $r = 2$: $\frac{\mu_2}{2!} = \frac{\sigma^2}{2} \implies \mathbf{\mu_2 = \sigma^2}$
- For $r = 3$: Since there are no odd powers of $t$ in the series, all odd central moments vanish:
  $$\mathbf{\mu_3 = 0} \quad (\mu_{2k+1} = 0 \text{ for all } k)$$
- For $r = 4$: $\frac{\mu_4}{4!} = \frac{\sigma^4}{8} \implies \mu_4 = 24 \times \frac{\sigma^4}{8} = \mathbf{3\sigma^4}$

---

**Step 3: Measure of Skewness ($\beta_1$):**
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{0}{(\sigma^2)^3} = \mathbf{0}$$
$$\gamma_1 = \sqrt{\beta_1} = \mathbf{0}$$
- **Comment:** Since $\beta_1 = 0$, the normal distribution is perfectly **symmetric** about the mean $\mu$.

---

**Step 4: Measure of Kurtosis ($\beta_2$):**
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{3\sigma^4}{(\sigma^2)^2} = \frac{3\sigma^4}{\sigma^4} = \mathbf{3}$$
$$\gamma_2 = \beta_2 - 3 = 3 - 3 = \mathbf{0}$$
- **Comment:** Since $\beta_2 = 3$ (kurtosis excess $\gamma_2 = 0$), the normal distribution is **Mesokurtic** (it serves as the universal baseline standard of peakedness).

---

### Question 13.6: Chief Characteristics & Properties of Normal Distribution
*(Ref: Question Bank Q.127 | MHU Sheet Lec 11-14 (Normal), Problem-5)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**What are the chief characteristics and properties of the Normal Distribution?**

---

#### Solution:
1. **Bell-Shaped Curve:** The graph of $f(x)$ is perfectly symmetrical and bell-shaped.
2. **Coincidence of Central Measures:** Mean $=$ Median $=$ Mode $= \mu$.
3. **Unimodal:** The curve has a single maximum at $x = \mu$, with maximum ordinate $f(\mu) = \frac{1}{\sigma \sqrt{2\pi}} \approx \frac{0.3989}{\sigma}$.
4. **Points of Inflection:** The concavity of the curve changes from concave downward to concave upward at two points:
   $$x = \mu - \sigma \quad \text{and} \quad x = \mu + \sigma$$
5. **Asymptotic Tails:** The curve extends from $-\infty$ to $+\infty$ along the $x$-axis, approaching but never touching the horizontal axis ($x$-axis is an asymptote).
6. **Empirical Area Rules (68-95-99.7 Rule):**
   - Area within $\mu \pm 1\sigma$: $P(\mu - \sigma < X < \mu + \sigma) = 0.6827 \quad (68.27\%)$
   - Area within $\mu \pm 2\sigma$: $P(\mu - 2\sigma < X < \mu + 2\sigma) = 0.9545 \quad (95.45\%)$
   - Area within $\mu \pm 3\sigma$: $P(\mu - 3\sigma < X < \mu + 3\sigma) = 0.9973 \quad (99.73\%)$
7. **Dispersion Relationships:**
   - **Quartile Deviation ($QD$):** $QD \approx \frac{2}{3}\sigma \approx 0.6745\sigma$.
   - **Mean Deviation ($MD$):** $MD \approx \sqrt{\frac{2}{\pi}}\sigma \approx \frac{4}{5}\sigma \approx 0.7979\sigma$.
   - Ratio: $QD : MD : \sigma \approx 10 : 12 : 15$.
8. **Moments:** All odd central moments are zero ($\mu_1 = \mu_3 = \mu_5 = 0$). Even central moments satisfy $\mu_{2n} = 1 \cdot 3 \cdot 5 \dots (2n - 1) \sigma^{2n}$.

---

### Problem 13.7: Probability Computations Using Normal Distribution
*(Ref: Question Bank Q.128, Q.129 | MHU Sheet Lec 11-14 (Normal), Problem-6 & 7)*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
1. $X$ is normally distributed with mean $\mu = 12$ and standard deviation $\sigma = 4$. Find:
   - (i) $P(X \ge 20)$
   - (ii) $P(X \le 20)$
   - (iii) $P(0 \le X \le 12)$
2. A random variable follows a normal distribution with mean $80$ and standard deviation $20$. What is the probability that a randomly selected value is:
   - (i) Less than $110$ ($P(X < 110)$)
   - (ii) More than $40$ ($P(X > 40)$)

---

#### Detailed Solution:

#### Part 1: $X \sim N(12, 4^2)$ (with $\mu = 12, \sigma = 4$)
Standardize using $Z = \frac{X - 12}{4}$:

- **(i) $P(X \ge 20)$:**
  $$Z = \frac{20 - 12}{4} = \frac{8}{4} = 2.0$$
  $$P(X \ge 20) = P(Z \ge 2.0) = 0.5 - P(0 \le Z \le 2.0)$$
  Using standard normal tables, $P(0 \le Z \le 2.0) = 0.4772$:
  $$P(X \ge 20) = 0.5 - 0.4772 = \mathbf{0.0228} \quad (2.28\%)$$

- **(ii) $P(X \le 20)$:**
  $$P(X \le 20) = 1 - P(X \ge 20) = 1 - 0.0228 = \mathbf{0.9772} \quad (97.72\%)$$
  *(Or $0.5 + P(0 \le Z \le 2.0) = 0.5 + 0.4772 = 0.9772$).*

- **(iii) $P(0 \le X \le 12)$:**
  - At $X = 0$: $Z = \frac{0 - 12}{4} = -3.0$
  - At $X = 12$: $Z = \frac{12 - 12}{4} = 0$
  $$P(0 \le X \le 12) = P(-3.0 \le Z \le 0) = P(0 \le Z \le 3.0)$$
  From normal tables, $P(0 \le Z \le 3.0) = 0.4987$:
  $$P(0 \le X \le 12) = \mathbf{0.4987} \quad (49.87\%)$$

---

#### Part 2: $X \sim N(80, 20^2)$ (with $\mu = 80, \sigma = 20$)
Standardize using $Z = \frac{X - 80}{20}$:

- **(i) $P(X < 110)$:**
  $$Z = \frac{110 - 80}{20} = \frac{30}{20} = 1.5$$
  $$P(X < 110) = P(Z < 1.5) = 0.5 + P(0 \le Z \le 1.5)$$
  Using $P(0 \le Z \le 1.5) = 0.4332$:
  $$P(X < 110) = 0.5 + 0.4332 = \mathbf{0.9332} \quad (93.32\%)$$

- **(ii) $P(X > 40)$:**
  $$Z = \frac{40 - 80}{20} = -\frac{40}{20} = -2.0$$
  $$P(X > 40) = P(Z > -2.0) = P(Z < 2.0) = 0.5 + P(0 \le Z \le 2.0)$$
  Using $P(0 \le Z \le 2.0) = 0.4772$:
  $$P(X > 40) = 0.5 + 0.4772 = \mathbf{0.9772} \quad (97.72\%)$$

---

### Problem 13.8: Industrial Quality Control — Washer Diameter Tolerance
*(Ref: Question Bank Q.96, Q.106 | Pg 3 Q.7(b), Pg 6 Q.8(a))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
1. The mean inside diameter of a sample of $200$ washers produced by a machine is $0.502$ inches and the standard deviation is $0.005$ inches. The intended specification allows a tolerance in diameter from $0.496$ to $0.508$ inches, otherwise the washers are considered defective. Determine the percentage of defective washers produced by the machine, assuming the diameters are normally distributed.  
*(Given standard normal area table values: for $Z = 1.2$, Area $= 0.3849$)*
2. Washers are produced so that their inside diameter is normally distributed with mean $1\text{ cm}$ and standard deviation $1\text{ mm}$. The washers are considered defective if their inside diameter is less than $9\text{ mm}$ or greater than $11\text{ mm}$. Find the percentage of defective washers.

---

#### Detailed Solution:

#### 1. First Case (Inches):
- Mean $\mu = 0.502\text{ in}$
- Standard deviation $\sigma = 0.005\text{ in}$
- Acceptable specification limits: $[x_1, x_2] = [0.496, 0.508]$

Compute the standard scores ($Z$-values):
- Lower limit $x_1 = 0.496$:
  $$Z_1 = \frac{0.496 - 0.502}{0.005} = \frac{-0.006}{0.005} = -1.2$$
- Upper limit $x_2 = 0.508$:
  $$Z_2 = \frac{0.508 - 0.502}{0.005} = \frac{+0.006}{0.005} = +1.2$$

Probability of a washer being **acceptable (non-defective)**:
$$P(0.496 \le X \le 0.508) = P(-1.2 \le Z \le 1.2) = 2 \times P(0 \le Z \le 1.2)$$
Given $P(0 \le Z \le 1.2) = 0.3849$:
$$P(\text{Acceptable}) = 2 \times 0.3849 = 0.7698 \quad (76.98\%)$$

Probability of a washer being **defective**:
$$P(\text{Defective}) = 1 - P(\text{Acceptable}) = 1 - 0.7698 = 0.2302 = \mathbf{23.02\%}$$

---

#### 2. Second Case (Metric Units: Millimeters):
- Mean $\mu = 1\text{ cm} = 10\text{ mm}$
- Standard deviation $\sigma = 1\text{ mm}$
- Acceptable range: $9\text{ mm} \le X \le 11\text{ mm}$

Compute $Z$-scores:
- At $x_1 = 9\text{ mm}$:
  $$Z_1 = \frac{9 - 10}{1} = -1.0$$
- At $x_2 = 11\text{ mm}$:
  $$Z_2 = \frac{11 - 10}{1} = +1.0$$

Probability of an acceptable washer:
$$P(9 \le X \le 11) = P(-1.0 \le Z \le 1.0) = 2 \times P(0 \le Z \le 1.0) = 2 \times 0.3413 = 0.6826 \quad (68.26\%)$$

Percentage of defective washers:
$$P(\text{Defective}) = 1 - 0.6826 = 0.3174 = \mathbf{31.74\%}$$

$$\mathbf{\text{Ans: (1) } 23.02\% \text{ defective}, \quad \text{(2) } 31.74\% \text{ defective}}$$

---

### Problem 13.9: Examination Marks — Determining Parameters $\mu$ and $\sigma$
*(Ref: Question Bank Q.102 | Pg 4, Q.8(b))*  
> 🏷️ **Identifier:** 🆕 `[NEW — FROM Q-BANK]` *(Added from Past Papers / Lecture Sheet)*
**Problem Statement:**  
The marks obtained by students in an examination are known to be normally distributed. If $10\%$ of the students scored less than $40$ marks, while $15\%$ scored over $80$ marks, find the **mean** ($\mu$) and **standard deviation** ($\sigma$) of the marks.

---

#### Detailed Solution:

Let $X$ be the marks obtained: $X \sim N(\mu, \sigma^2)$.  
We are given two percentile conditions:
1. $P(X < 40) = 10\% = 0.10$
2. $P(X > 80) = 15\% = 0.15$

**Step 1: Determine the Standard Normal $Z$-Scores.**

- **For the lower tail ($X = 40$):**  
  $$P(X < 40) = P\left( Z < \frac{40 - \mu}{\sigma} \right) = 0.10$$
  Since $0.10 < 0.5$, this point lies to the left of the mean:
  $$P\left( \frac{40 - \mu}{\sigma} < Z < 0 \right) = 0.50 - 0.10 = 0.4000$$
  From standard normal distribution tables, the value of $Z$ corresponding to area $0.4000$ is approximately $1.28$.  
  Since it lies to the left of zero:
  $$Z_1 = \frac{40 - \mu}{\sigma} = -1.28155 \approx -1.28$$
  $$40 - \mu = -1.28 \sigma \implies \mu - 1.28 \sigma = 40 \quad \dots \text{(1)}$$

- **For the upper tail ($X = 80$):**  
  $$P(X > 80) = P\left( Z > \frac{80 - \mu}{\sigma} \right) = 0.15$$
  $$P\left( 0 < Z < \frac{80 - \mu}{\sigma} \right) = 0.50 - 0.15 = 0.3500$$
  From standard normal distribution tables, the value of $Z$ corresponding to area $0.3500$ is approximately $1.0364 \approx 1.04$:
  $$Z_2 = \frac{80 - \mu}{\sigma} = +1.0364 \approx 1.04$$
  $$80 - \mu = 1.04 \sigma \implies \mu + 1.04 \sigma = 80 \quad \dots \text{(2)}$$

---

**Step 2: Solve the Simultaneous Linear Equations.**  
Subtract equation (1) from equation (2):
$$(\mu + 1.04 \sigma) - (\mu - 1.28 \sigma) = 80 - 40$$
$$2.32 \sigma = 40$$
$$\sigma = \frac{40}{2.32} \approx \mathbf{17.24}$$

*(Using exact values $Z_1 = -1.2816$ and $Z_2 = 1.0364$):*
$$\sigma = \frac{40}{1.0364 - (-1.2816)} = \frac{40}{2.318} \approx \mathbf{17.256} \approx 17.26$$

Now substitute $\sigma$ into equation (2):
$$\mu = 80 - 1.0364(17.256) = 80 - 17.88 = \mathbf{62.12}$$
*(Check with equation (1): $\mu = 40 + 1.2816(17.256) = 40 + 22.115 = 62.12$)*.

$$\mathbf{\text{Mean } (\mu) \approx 62.12, \quad \text{Standard Deviation } (\sigma) \approx 17.26}$$

---