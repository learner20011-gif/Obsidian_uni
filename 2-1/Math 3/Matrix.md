# Lecture 11-17: Matrix Algebra and Properties

## 1. Fundamental Concepts of Matrices (Page 1)

A matrix is a fundamental object in linear algebra used to represent data, linear transformations, and systems of equations.

### **Definition and Notation**
*   **Matrix:** A rectangular array of numbers enclosed by brackets (either square $[ ]$ or round $( )$). It is subject to specific rules of operation.
*   **Dimension:** An $m \times n$ matrix has $m$ rows and $n$ columns.

👁️ **Example:**
$$ A = \begin{bmatrix} 2 & 3 & 5 \\ 1 & -1 & 4 \end{bmatrix} $$
This is a matrix with 2 rows and 3 columns ($2 \times 3$).

---

### **Types of Matrices**

#### **A. Dimensions Based**
1.  **Square Matrix:** A matrix where the number of rows equals the number of columns ($m=n$).
    *   👁️ **Example:** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ is a $2 \times 2$ square matrix.

#### **B. Diagonal Properties**
2.  **Diagonal Matrix:** A square matrix where all non-diagonal elements are zero ($a_{ij} = 0$ for $i \neq j$).
    *   👁️ **Example:** $A = \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}$.
3.  **Scalar Matrix:** A diagonal matrix where all the diagonal elements are **equal**.
    *   👁️ **Example:** $A = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$.
4.  **Unit / Identity Matrix ($I$):** A scalar matrix where all diagonal elements are unity ($1$) and non-diagonal elements are zero.
    *   👁️ **Example:** $I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.

#### **C. Element Value Based**
5.  **Zero / Null Matrix:** A matrix where **all** elements are zero.
    *   👁️ **Example:** $A = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$.

#### **D. Relationship Between Two Matrices**
6.  **Commutative Matrices:** Two square matrices $A$ and $B$ are commutative if their product order does not matter.
    *   **Condition:** $AB = BA$.
    *   👁️ **Example:** $A=\begin{bmatrix} 1 & -2 \\ -1 & 3 \end{bmatrix}, B = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix}$.
7.  **Anti-commutative Matrices:** Two matrices where reversing the order negates the result.
    *   **Condition:** $AB = -BA$.

#### **E. Triangular Matrices**
8.  **Upper Triangular Matrix:** A square matrix where all elements **below** the main diagonal are zero ($a_{ij} = 0$ if $i > j$).
    *   👁️ **Example:** $A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 0 & a_{22} & a_{23} \\ 0 & 0 & a_{33} \end{bmatrix}$.
9.  **Lower Triangular Matrix:** A square matrix where all elements **above** the main diagonal are zero ($a_{ij} = 0$ if $i < j$).
    *   👁️ **Example:** $A = \begin{bmatrix} a_{11} & 0 & 0 \\ a_{21} & a_{22} & 0 \\ a_{31} & a_{32} & a_{33} \end{bmatrix}$.

#### **F. Power Properties**
10. **Idempotent Matrix:** A square matrix that remains unchanged when squared.
    *   **Condition:** $A^2 = A$.
    *   👁️ **Example:** $A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.
11. **Involuntary Matrix:** A square matrix which, when squared, results in the Identity matrix.
    *   **Condition:** $A^2 = I$.
    *   👁️ **Example:** $A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$ (Note: The provided text example $A = \begin{bmatrix} 1 & 2 \\ 0 & -1 \end{bmatrix}$ actually yields $A^2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$).

#### **G. Transpose**
12. **Transpose of a Matrix ($A'$ or $A^T$):** Obtained by interchanging rows and columns. If $A$ is $m \times n$, then $A'$ is $n \times m$.
    *   👁️ **Example:** If $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$, then $A' = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$.

---

## 2. Advanced Matrix Types & Operations (Page 2)

### **Real Matrix Properties**
1.  **Symmetric Matrix:** A square matrix equal to its transpose.
    *   **Condition:** $A' = A$ (or $a_{ij} = a_{ji}$).
    *   👁️ **Example:** $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{bmatrix}$.
2.  **Skew-Symmetric Matrix:** A square matrix equal to the negative of its transpose.
    *   **Condition:** $A' = -A$ (or $a_{ij} = -a_{ji}$).
    *   **Note:** The diagonal elements must be zero (proven in Theorem 3).
    *   👁️ **Example:** $\begin{bmatrix} 0 & -2 & 3 \\ 2 & 0 & 4 \\ -3 & -4 & 0 \end{bmatrix}$.
3.  **Orthogonal Matrix:** A square matrix whose transpose is its inverse.
    *   **Condition:** $A'A = I$ (or $A' = A^{-1}$).
    *   👁️ **Example:** $A = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$.

### **Complex Matrix Properties**
When matrices contain complex numbers ($z = a + ib$), we introduce the concept of conjugation.

4.  **Conjugate of a Matrix ($\bar{A}$):** Obtained by replacing every element $a_{ij}$ with its complex conjugate $\bar{a}_{ij}$ (changing the sign of the imaginary part).
    *   👁️ **Example:** If $A = \begin{bmatrix} 1+2i & 3i \\ 3i & 2-3i \end{bmatrix}$, then $\bar{A} = \begin{bmatrix} 1-2i & -3i \\ -3i & 2+3i \end{bmatrix}$.
5.  **Hermitian Matrix:** A square matrix equal to the transpose of its conjugate (Tranjugate).
    *   **Condition:** $(\bar{A})' = A$. (Also denoted as $A^{\dagger} = A$).
    *   **Property:** Diagonal elements must be real.
6.  **Skew-Hermitian Matrix:** A square matrix equal to the negative transpose of its conjugate.
    *   **Condition:** $(\bar{A})' = -A$.
    *   **Property:** Diagonal elements must be zero or pure imaginary.
7.  **Unitary Matrix:** The complex equivalent of an orthogonal matrix.
    *   **Condition:** $(\bar{A})' A = I$.

### **Other Properties**
8.  **Trace of a Matrix:** The sum of the diagonal elements of a square matrix.
    *   **Formula:** $\text{Trace}(A) = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \dots + a_{nn}$.

---

## 3. Fundamental Matrix Theorems (Pages 2-3)

### **Theorem 1: Associativity of Matrix Multiplication**
**Statement:** Assuming dimensions allow for multiplication, $A(BC) = (AB)C$.

**Proof Breakdown:**
1.  **Define Matrices:**
    *   Let $A = [a_{ij}]_{m \times n}$
    *   Let $B = [b_{jk}]_{n \times p}$
    *   Let $C = [c_{kr}]_{p \times q}$

2.  **Analyze Left Hand Side ($A(BC)$):**
    *   Let $BC = [h_{jr}]$. The element at $(j, r)$ is $h_{jr} = \sum_{k=1}^{p} b_{jk}c_{kr}$.
    *   The $(i, r)$-th element of $A(BC)$ is:
        $$ \sum_{j=1}^{n} a_{ij} h_{jr} = \sum_{j=1}^{n} a_{ij} \left( \sum_{k=1}^{p} b_{jk}c_{kr} \right) $$

3.  **Analyze Right Hand Side ($(AB)C$):**
    *   Let $AB = [d_{ik}]$. The element at $(i, k)$ is $d_{ik} = \sum_{j=1}^{n} a_{ij}b_{jk}$.
    *   The $(i, r)$-th element of $(AB)C$ is:
        $$ \sum_{k=1}^{p} d_{ik} c_{kr} = \sum_{k=1}^{p} \left( \sum_{j=1}^{n} a_{ij}b_{jk} \right) c_{kr} $$

4.  **Conclusion:**
    Since summation is finite, the order of summation can be interchanged. The expressions derived in step 2 and 3 are identical.
    $$ \sum_{j=1}^{n} \sum_{k=1}^{p} a_{ij} b_{jk} c_{kr} = \sum_{k=1}^{p} \sum_{j=1}^{n} a_{ij} b_{jk} c_{kr} $$
    Therefore, matrix multiplication is associative.

### **Theorem 2: Transpose of a Product (Reversal Rule)**
**Statement:** The transpose of a product is the product of the transposes in reverse order.
$$ (AB)' = B'A' $$

**Proof Breakdown:**
1.  **Element Definition:**
    The $(k, i)$-th element of $(AB)'$ is the $(i, k)$-th element of $AB$.
    $$ (AB)_{ik} = \sum_{j=1}^{n} a_{ij}b_{jk} $$
    Therefore, element $(k, i)$ of $(AB)' = \sum_{j=1}^{n} a_{ij}b_{jk}$.

2.  **Product of Transposes ($B'A'$):**
    *   Let $B' = [b'_{kj}]$ where $b'_{kj} = b_{jk}$ (columns of $B$ become rows of $B'$).
    *   Let $A' = [a'_{ji}]$ where $a'_{ji} = a_{ij}$ (rows of $A$ become columns of $A'$).
    *   Row $k$ of $B'$ is $(b_{1k}, b_{2k}, \dots, b_{nk})$ from column $k$ of $B$.
    *   Column $i$ of $A'$ is $(a_{i1}, a_{i2}, \dots, a_{in})$ from row $i$ of $A$.

3.  **Multiplication:**
    The $(k, i)$-th element of $B'A'$ is the dot product of the $k$-th row of $B'$ and $i$-th column of $A'$:
    $$ \sum_{j=1}^{n} b_{jk} a_{ij} = \sum_{j=1}^{n} a_{ij} b_{jk} $$

4.  **Conclusion:**
    The $(k, i)$-th element of $(AB)'$ is identical to the $(k, i)$-th element of $B'A'$.
    $$ (AB)' = B'A' $$

### **Theorem 3: Diagonal of Skew-Symmetric Matrix**
**Statement:** The diagonal elements of a skew-symmetric matrix are zero.

**Proof:**
1.  **Definition:** For a skew-symmetric matrix $A$, $A = -A'$.
    $$ a_{ij} = -a_{ji} \quad \text{for all } i, j $$
2.  **Apply to Diagonal:** For diagonal elements, the row index equals the column index ($i = j$).
    $$ a_{ii} = -a_{ii} $$
3.  **Solve:**
    $$ a_{ii} + a_{ii} = 0 $$
    $$ 2a_{ii} = 0 \implies a_{ii} = 0 $$
    Thus, all diagonal elements are zero.

---

## 4. The Adjoint of a Matrix (Page 4)

The adjoint is a crucial concept for finding the inverse of a matrix.

### **Definitions**
*   **Minor ($M_{ij}$):** The determinant of the sub-matrix obtained by deleting the $i$-th row and $j$-th column.
*   **Cofactor ($A_{ij}$ or $\alpha_{ij}$):** The signed minor.
    $$ \text{Cofactor } \alpha_{ij} = (-1)^{i+j} \times \text{Minor} $$
*   **Cofactor Matrix:** A matrix formed by replacing every element $a_{ij}$ with its cofactor $\alpha_{ij}$.
*   **Adjoint Matrix ($\text{adj } A$):** The **transpose** of the cofactor matrix.
    $$ \text{adj } A = [\alpha_{ij}]^T $$

### 👁️ **Example Problem 1: Find adj(A)**
Given:
$$ A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 2 \\ 3 & 3 & 4 \end{bmatrix} $$

**Step 1: Calculate Cofactors**
*   $\alpha_{11} = + \begin{vmatrix} 3 & 2 \\ 3 & 4 \end{vmatrix} = (12 - 6) = 6$
*   $\alpha_{12} = - \begin{vmatrix} 2 & 2 \\ 3 & 4 \end{vmatrix} = -(8 - 6) = -2$
*   $\alpha_{13} = + \begin{vmatrix} 2 & 3 \\ 3 & 3 \end{vmatrix} = (6 - 9) = -3$
*   $\alpha_{21} = - \begin{vmatrix} 2 & 3 \\ 3 & 4 \end{vmatrix} = -(8 - 9) = 1$
*   $\alpha_{22} = + \begin{vmatrix} 1 & 3 \\ 3 & 4 \end{vmatrix} = (4 - 9) = -5$
*   $\alpha_{23} = - \begin{vmatrix} 1 & 2 \\ 3 & 3 \end{vmatrix} = -(3 - 6) = 3$
*   $\alpha_{31} = + \begin{vmatrix} 2 & 3 \\ 3 & 2 \end{vmatrix} = (4 - 9) = -5$
*   $\alpha_{32} = - \begin{vmatrix} 1 & 3 \\ 2 & 2 \end{vmatrix} = -(2 - 6) = 4$
*   $\alpha_{33} = + \begin{vmatrix} 1 & 2 \\ 2 & 3 \end{vmatrix} = (3 - 4) = -1$

**Step 2: Form Cofactor Matrix**
$$ C = \begin{bmatrix} 6 & -2 & -3 \\ 1 & -5 & 3 \\ -5 & 4 & -1 \end{bmatrix} $$

**Step 3: Transpose to get Adjoint**
$$ \text{adj } A = C^T = \begin{bmatrix} 6 & 1 & -5 \\ -2 & -5 & 4 \\ -3 & 3 & -1 \end{bmatrix} $$

### **Fundamental Adjoint Theorem**
**Statement:** For any $n$-square matrix $A$:
$$ A \cdot (\text{adj } A) = (\text{adj } A) \cdot A = |A| \cdot I_n $$

**Proof Outline (Starts on Page 4):**
1.  Let $A = [a_{ij}]$ and the cofactor matrix be $[\alpha_{ij}]$.
2.  The adjoint is the transpose of the cofactor matrix, so the element at row $i$, column $j$ of $\text{adj } A$ is $\alpha_{ji}$.
3.  When multiplying $A \times \text{adj } A$, the element at position $(i, j)$ is the sum of products of the $i$-th row of $A$ and the $j$-th column of $\text{adj } A$ (which corresponds to the $j$-th row of cofactors).
4.  **Key Determinant Property:**
    *   If elements of a row are multiplied by their own cofactors ($i=j$), the sum equals the determinant $|A|$.
    *   If elements of a row are multiplied by cofactors of a different row ($i \neq j$), the sum is zero.
5.  This results in a diagonal matrix where every diagonal element is $|A|$ and others are 0, which factors out to $|A|I$.

## 5. Properties of Adjoint Matrix (Page 5)

This page concludes the proof regarding the product of a matrix and its adjoint, and introduces a new theorem regarding the adjoint of an adjoint.

### **Theorem: $A(\text{adj } A) = |A|I$ (Proof Continuation)**

We previously established that:
*   $\text{adj } A$ is the transpose of the cofactor matrix.
*   Row $i$ of $A$ $\times$ Column $j$ of $\text{adj } A$ = Row $i$ of $A$ $\times$ Row $j$ of Cofactors.

**The Logic:**
1.  **Same Row ($i=j$):** The sum of elements multiplied by their own cofactors equals the determinant $|A|$.
2.  **Different Row ($i \neq j$):** The sum of elements multiplied by cofactors of a different row is always $0$.

**Matrix Multiplication Result:**
$$
A \cdot (\text{adj } A) =
\begin{bmatrix}
|A| & 0 & \cdots & 0 \\
0 & |A| & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & |A|
\end{bmatrix}
= |A| \begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix}
= |A|I_n
$$
Similarly, $(\text{adj } A)A = |A|I_n$.

---

### **Theorem: $\text{adj}(\text{adj } A) = |A|^{n-2}A$**

**Statement:** If $|A| \neq 0$ (non-singular), the adjoint of the adjoint of $A$ scales the original matrix $A$ by the determinant raised to the power of $n-2$.

**Proof Breakdown:**
1.  **Fundamental Identity:** We know $B (\text{adj } B) = |B|I$.
2.  **Substitution:** Let $B = \text{adj } A$.
    $$ (\text{adj } A) \cdot [\text{adj}(\text{adj } A)] = |\text{adj } A| \cdot I \quad \dots (i) $$
3.  **Determinant Property:**
    We know $A (\text{adj } A) = |A|I$. Taking the determinant of both sides:
    $$ |A (\text{adj } A)| = ||A|I| $$
    $$ |A| \cdot |\text{adj } A| = |A|^n $$
    $$ |\text{adj } A| = |A|^{n-1} \quad \dots (ii) $$
4.  **Combine (i) and (ii):** Substitute Eq (ii) into Eq (i):
    $$ (\text{adj } A) \cdot [\text{adj}(\text{adj } A)] = |A|^{n-1} \cdot I $$
5.  **Isolate:** Multiply both sides by $A$ from the left:
    $$ A \cdot (\text{adj } A) \cdot [\text{adj}(\text{adj } A)] = A \cdot |A|^{n-1} \cdot I $$
    $$ (|A|I) \cdot [\text{adj}(\text{adj } A)] = |A|^{n-1} A $$
    $$ |A| \cdot [\text{adj}(\text{adj } A)] = |A|^{n-1} A $$
    Divide by $|A|$:
    $$ \text{adj}(\text{adj } A) = |A|^{n-2} A $$

---

## 6. Inverse of a Matrix (Page 6)

### **Definition and Conditions**
The inverse of a square matrix $A$ is a matrix $A^{-1}$ such that $AA^{-1} = A^{-1}A = I$.

*   **Formula:**
    $$ A^{-1} = \frac{\text{adj } A}{|A|} $$
*   **Singular Matrix:** If $|A| = 0$, the inverse does not exist (cannot divide by zero).
*   **Non-singular Matrix:** If $|A| \neq 0$, the inverse exists.

### 👁️ **Example Problem 1**
**Task:** Find the inverse of $A = \begin{bmatrix} 1 & 2 & -1 \\ -1 & 1 & 2 \\ 2 & -1 & 1 \end{bmatrix}$.

1.  **Determinant ($|A|$):**
    $$ |A| = 1(1+2) - 2(-1-4) - 1(1-2) $$
    $$ |A| = 3 + 10 + 1 = 14 $$
    Since $14 \neq 0$, $A^{-1}$ exists.
2.  **Cofactors:**
    *   Calculated individually (e.g., $\alpha_{11} = 3$, $\alpha_{12} = 5$, etc.).
    *   Cofactor Matrix: $\begin{bmatrix} 3 & 5 & -1 \\ -1 & 3 & 5 \\ 5 & -1 & 3 \end{bmatrix}$.
3.  **Adjoint (Transpose of Cofactors):**
    $$ \text{adj } A = \begin{bmatrix} 3 & -1 & 5 \\ 5 & 3 & -1 \\ -1 & 5 & 3 \end{bmatrix} $$
4.  **Inverse:**
    $$ A^{-1} = \frac{1}{14} \begin{bmatrix} 3 & -1 & 5 \\ 5 & 3 & -1 \\ -1 & 5 & 3 \end{bmatrix} $$

---

### ✍️ **Solution to H.W. Problem-2 (Unsolved in PDF)**

**Problem:** If $A = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$, find $A^2$ and show that $A^2 = A^{-1}$.

**Step 1: Find Determinant $|A|$**
Expanding along the 3rd row (easiest):
$$ |A| = 1 \begin{vmatrix} -1 & 1 \\ -1 & 0 \end{vmatrix} - 0 + 0 = 1(0 - (-1)) = 1 $$

**Step 2: Find $A^{-1}$**
*   **Cofactors:**
    *   $\alpha_{11}=0, \quad \alpha_{12}=0, \quad \alpha_{13}=1$
    *   $\alpha_{21}=0, \quad \alpha_{22}=-1, \quad \alpha_{23}=-1$
    *   $\alpha_{31}=1, \quad \alpha_{32}=2, \quad \alpha_{33}=1$
*   **Adjoint (Transpose):**
    $$ \text{adj } A = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -1 & 2 \\ 1 & -1 & 1 \end{bmatrix} $$
*   **Inverse ($ \frac{1}{|A|} \text{adj } A$):**
    $$ A^{-1} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -1 & 2 \\ 1 & -1 & 1 \end{bmatrix} $$

**Step 3: Find $A^2$**
$$ A^2 = A \cdot A = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 0 \\ 1 & 0 & 0 \end{bmatrix} $$
*   $R_1 C_1 = 1-2+1 = 0$
*   $R_1 C_2 = -1+1+0 = 0$
*   $R_1 C_3 = 1+0+0 = 1$
*   $R_2 C_1 = 2-2+0 = 0$
*   $R_2 C_2 = -2+1+0 = -1$
*   $R_2 C_3 = 2+0+0 = 2$
*   $R_3 C_1 = 1+0+0 = 1$
*   $R_3 C_2 = -1+0+0 = -1$
*   $R_3 C_3 = 1+0+0 = 1$

$$ A^2 = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -1 & 2 \\ 1 & -1 & 1 \end{bmatrix} $$

**Conclusion:** Comparing Step 2 and Step 3, **$A^2 = A^{-1}$. (Proved)**

---

## 7. Rank of a Matrix (Page 7)

### **Definition**
The rank of a matrix $A$, denoted $\rho(A)$, is the order (size) of the largest square sub-matrix (minor) whose determinant is **non-zero**.
*   **Note:** Rank of a Null matrix is 0.

### **Method 1: By Minors**
We check determinants of square sub-matrices starting from the largest possible size.

👁️ **Example 1:**
$$ A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 5 & 7 \end{bmatrix} $$
*   Check order 3: $|A| = 1(21-20) - 2(14-12) + 3(10-9) = 1 - 4 + 3 = 0$.
*   Since $|A|=0$, Rank $\neq 3$.
*   Check order 2: Take sub-matrix $\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}$. Determinant $= 3-4 = -1 \neq 0$.
*   **Result:** $\rho(A) = 2$.

### **Method 2: Normal / Canonical Form**
We use elementary row and column operations to reduce matrix $A$ to the form:
$$ \begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix} $$
Where $I_r$ is the identity matrix of order $r$. The rank is **$r$**.

👁️ **Example Problem 3 (Page 7 Walkthrough):**
Given $A$ ($4 \times 4$).
**Operations performed:**
1.  Used $a_{11}$ to make the rest of column 1 zero ($R_{21}, R_{31}, R_{41}$).
2.  Used $a_{11}$ to make the rest of row 1 zero ($C_{21}, C_{31}, C_{41}$).
    *   Result: First row/col is $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \dots \end{bmatrix}$.
3.  Continued this process for the sub-matrices.

---

## 8. Rank Determination Continued (Page 8)

This page continues the reduction of matrices to Normal form to find the rank.

### 👁️ **Problem 4 Walkthrough**
**Given:** $P = \begin{bmatrix} 1 & -1 & 3 & 6 \\ 1 & 3 & -3 & -4 \\ 5 & 3 & 3 & 1 \end{bmatrix}$.

1.  **Zeros in Column 1:** $R_2 - R_1$, $R_3 - 5R_1$.
    $$ \rightarrow \begin{bmatrix} 1 & -1 & 3 & 6 \\ 0 & 4 & -6 & -10 \\ 0 & 8 & -12 & -29 \end{bmatrix} $$
2.  **Zeros in Row 1:** Column operations $C_2+C_1$, etc. (The matrix becomes block diagonal).
3.  **Zeros in Column 2:** $R_3 - 2R_2$.
    $$ \rightarrow \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 4 & -6 & -10 \\ 0 & 0 & 0 & -9 \end{bmatrix} $$
4.  **Final Reduction:** Scale rows/cols to get Identity elements.
    $$ \text{Result: } \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix} = [I_3 \quad 0] $$
    **Rank:** $\rho(P) = 3$.

---

### ✍️ **Solutions to H.W. Problems 5, 6, 7**

#### **H.W. Problem-5**
**Find Rank of:** $A = \begin{bmatrix} -2 & -1 & -3 & -1 \\ 1 & 2 & 3 & -1 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & -1 \end{bmatrix}$

**Logic:**
1.  Swap $R_1 \leftrightarrow R_2$ to get 1 in top-left: $\begin{bmatrix} 1 & 2 & 3 & -1 \\ -2 & -1 & -3 & -1 \\ \dots \end{bmatrix}$.
2.  $R_2 \to R_2 + 2R_1$, $R_3 \to R_3 - R_1$.
    $$ \sim \begin{bmatrix} 1 & 2 & 3 & -1 \\ 0 & 3 & 3 & -3 \\ 0 & -2 & -2 & 2 \\ 0 & 1 & 1 & -1 \end{bmatrix} $$
3.  Observe Rows 2, 3, and 4 are proportional. $R_2 = 3(R_4)$, $R_3 = -2(R_4)$.
4.  Perform $R_2 - 3R_4$ and $R_3 + 2R_4$.
    $$ \sim \begin{bmatrix} 1 & 2 & 3 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & -1 \end{bmatrix} $$
5.  Swap $R_2 \leftrightarrow R_4$. We have 2 non-zero rows.
**Answer:** **Rank = 2**.

#### **H.W. Problem-6**
**Find Rank of:** $P = \begin{bmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & -2 & 1 \\ 1 & -1 & 4 & 0 \\ 2 & 2 & 8 & 0 \end{bmatrix}$

**Logic:**
1.  $R_3 \to R_3 - R_1$, $R_4 \to R_4 - 2R_1$.
    $$ \sim \begin{bmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & -2 & 1 \\ 0 & -1 & 2 & -1 \\ 0 & 2 & 4 & -2 \end{bmatrix} $$
2.  $R_3 \to R_3 + R_2$. This makes Row 3 all zeros ($0\ 0\ 0\ 0$).
3.  $R_4 \to R_4 - 2R_2$.
    $$ \sim \begin{bmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 8 & -4 \end{bmatrix} $$
4.  Swap $R_3 \leftrightarrow R_4$. We have 3 non-zero rows. The pivots are at $(1,1), (2,2), (3,3)$.
**Answer:** **Rank = 3**.

#### **H.W. Problem-7**
**Find Rank of:** $A = \begin{bmatrix} 3 & -2 & 0 & 1 \\ 0 & 2 & 2 & 1 \\ 1 & -2 & -3 & 2 \\ 0 & 1 & 2 & 1 \end{bmatrix}$

**Logic:**
1.  Swap $R_1 \leftrightarrow R_3$ (to get 1 at pivot).
2.  Eliminate column 1.
3.  Eliminate column 2 using Row 2.
4.  In this specific matrix, the determinant is non-zero (Calculated: $|A| \neq 0$).
5.  Since the determinant of the $4 \times 4$ matrix is non-zero, the rank must be equal to the dimension.
**Answer:** **Rank = 4**.


## 9. System of Linear Equations (Page 9)

### **Fundamental Concepts**
A system of $m$ linear equations with $n$ unknowns ($x_1, x_2, \dots, x_n$) can be represented in matrix form:
$$ AX = B $$

*   **Coefficient Matrix ($A$):** The matrix containing the coefficients of the variables.
*   **Variable Matrix ($X$):** The column vector of unknowns.
*   **Constant Matrix ($B$):** The column vector of constants on the right side of the equals sign.
*   **Augmented Matrix ($A^*$ or $[A:B]$):** A combined matrix formed by appending $B$ as an extra column to $A$.
    $$ A^* = \begin{bmatrix} a_{11} & \cdots & a_{1n} & : & b_1 \\ \vdots & \ddots & \vdots & : & \vdots \\ a_{m1} & \cdots & a_{mn} & : & b_m \end{bmatrix} $$

### **Types of Systems**
1.  **Homogeneous:** If $B = 0$ (All constants are zero). Always has at least the trivial solution ($X=0$).
2.  **Non-Homogeneous:** If $B \neq 0$.

### **Consistency and Rank (Theory)**
We determine the nature of the solution by comparing the Rank ($\rho$) of the coefficient matrix $A$ and the augmented matrix $A^*$. Let $n$ be the number of variables.

*   **Consistent (Solution Exists):**
    $$ \rho(A) = \rho(A^*) $$
    *   **Unique Solution:** If $\rho(A) = \rho(A^*) = n$.
    *   **Infinite Solutions:** If $\rho(A) = \rho(A^*) = r < n$.
        *   Number of independent variables (free parameters) $= n - r$.
*   **Inconsistent (No Solution):**
    $$ \rho(A) \neq \rho(A^*) $$
    *   Usually happens when a row reduces to $[0 \ 0 \ \dots \ 0 \ : \ k]$ where $k \neq 0$ (implying $0 = k$, which is false).

---

### 👁️ **Problem 1: Infinite Solutions Walkthrough (Pages 9-10)**

**System:**
$$ \begin{aligned} x + 2y - 3z + 2w &= 2 \\ 2x + 5y - 8z + 6w &= 5 \\ 3x + 4y - 5z + 2w &= 4 \end{aligned} $$

**Step 1: Augmented Matrix**
$$ A^* = \begin{bmatrix} 1 & 2 & -3 & 2 & : & 2 \\ 2 & 5 & -8 & 6 & : & 5 \\ 3 & 4 & -5 & 2 & : & 4 \end{bmatrix} $$

**Step 2: Row Operations (Echelon Form)**
1.  $R_2 \to R_2 - 2R_1$
2.  $R_3 \to R_3 - 3R_1$
    $$ \sim \begin{bmatrix} 1 & 2 & -3 & 2 & : & 2 \\ 0 & 1 & -2 & 2 & : & 1 \\ 0 & -2 & 4 & -4 & : & -2 \end{bmatrix} $$
3.  $R_3 \to R_3 + 2R_2$
    $$ \sim \begin{bmatrix} 1 & 2 & -3 & 2 & : & 2 \\ 0 & 1 & -2 & 2 & : & 1 \\ 0 & 0 & 0 & 0 & : & 0 \end{bmatrix} $$

**Step 3: Rank Analysis**
*   $\rho(A) = 2$ (2 non-zero rows in $A$ part).
*   $\rho(A^*) = 2$ (2 non-zero rows in total).
*   $n = 4$ (variables $x, y, z, w$).
*   **Conclusion:** $\rho(A) = \rho(A^*) = 2 < 4$. The system is **Consistent** with **Infinite Solutions**.

**Step 4: Finding the General Solution**
*   Free variables $= n - r = 4 - 2 = 2$. Let $z = a$ and $w = b$.
*   From Row 2: $y - 2z + 2w = 1 \implies y = 1 + 2a - 2b$.
*   From Row 1: $x + 2y - 3z + 2w = 2$.
    Substitute $y, z, w$:
    $x + 2(1 + 2a - 2b) - 3a + 2b = 2$
    $x + 2 + 4a - 4b - 3a + 2b = 2$
    $x = -a + 2b$.

---

## 10. Solving for Unique and No Solutions (Pages 10-11)

### 👁️ **Problem 2: Unique Solution**
**System:**
$$ \begin{aligned} 2x + y - 2z &= 10 \\ 3x + 2y + 2z &= 1 \\ 5x + 4y + 3z &= 4 \end{aligned} $$

**Process:**
Applying row operations reduces the augmented matrix to:
$$ \begin{bmatrix} 2 & 1 & -2 & : & 10 \\ 0 & 1 & 10 & : & -28 \\ 0 & 0 & -14 & : & 42 \end{bmatrix} $$
*   $\rho(A) = 3$, $\rho(A^*) = 3$, $n=3$.
*   Since Rank = $n$, **Unique Solution**.
*   Back substitution:
    1.  $-14z = 42 \implies z = -3$.
    2.  $y + 10(-3) = -28 \implies y = 2$.
    3.  $2x + 2 - 2(-3) = 10 \implies x = 1$.

### 👁️ **Problem 3: Inconsistent System (No Solution)**
**System:**
$$ \begin{aligned} 4x_1 + 5x_2 + 3x_3 &= 7 \\ \dots \end{aligned} $$
**Process:**
After row operations, the matrix becomes:
$$ \begin{bmatrix} 1 & 1 & 2 & : & 5 \\ 0 & 1 & -5 & : & -8 \\ 0 & 0 & 0 & : & -5 \end{bmatrix} $$
*   $\rho(A) = 2$ (Last row of coefficients is 0).
*   $\rho(A^*) = 3$ (Last row of augmented is non-zero).
*   **Conclusion:** Inconsistent. **No Solution**.

### 👁️ **Problem 4: Conditional Consistency**
**Goal:** Find relation between $a, b, c$ for a solution to exist.
**Reduced Matrix:**
$$ \begin{bmatrix} 1 & 2 & -3 & : & a \\ 0 & -7 & 11 & : & b - 3a \\ 0 & 0 & 0 & : & 2a - b + c \end{bmatrix} $$
*   For the system to be consistent, we cannot have $0 = \text{non-zero}$.
*   Therefore, the final element must be zero.
*   **Condition:** $2a - b + c = 0$.

---

## 11. Parametric Analysis of Systems (Pages 11-12)

### 👁️ **Problem 5: Analysis with Parameter $\lambda$**
**System:**
$$ \begin{aligned} x + y + \lambda z &= 2 \\ 3x + 4y + 2z &= \lambda \\ 2x + 3y - z &= 1 \end{aligned} $$

**Step 1: Reduction**
After operations ($R_2-3R_1$, $R_3-2R_1$, then $R_3-R_2$), we get:
$$ \begin{bmatrix} 1 & 1 & \lambda & : & 2 \\ 0 & 1 & 2-3\lambda & : & \lambda-6 \\ 0 & 0 & \lambda-3 & : & 3-\lambda \end{bmatrix} $$
Note: The last term $3-\lambda = -(\lambda-3)$.

**Step 2: Case Analysis**
1.  **Unique Solution:**
    *   Requires pivots in all 3 rows.
    *   Condition: $\lambda - 3 \neq 0 \implies \lambda \neq 3$.
2.  **More than one solution (Infinite):**
    *   Requires rank $< n$.
    *   If $\lambda = 3$, the last row becomes $[0 \ 0 \ 0 \ : \ 0]$.
    *   $\rho(A) = \rho(A^*) = 2 < 3$. Consistent, infinite solutions.
3.  **No Solution:**
    *   Requires $0 = k$ ($k \neq 0$).
    *   In this specific reduction, if LHS is 0 ($\lambda=3$), RHS is also 0. Thus, there is **no value** of $\lambda$ that produces "No Solution" for this specific setup.

---

### ✍️ **H.W. Problem Solutions**

#### **H.W. Problem-6**
**Solve:**
$$ \begin{aligned} x + 2y + 3z &= 3 \\ 2x + 3y + 8z &= 4 \\ 3x + 2y + 17z &= 1 \end{aligned} $$

**Solution:**
1.  **Augmented Matrix:**
    $$ \begin{bmatrix} 1 & 2 & 3 & : & 3 \\ 2 & 3 & 8 & : & 4 \\ 3 & 2 & 17 & : & 1 \end{bmatrix} $$
2.  **Row Ops ($R_2-2R_1, R_3-3R_1$):**
    $$ \sim \begin{bmatrix} 1 & 2 & 3 & : & 3 \\ 0 & -1 & 2 & : & -2 \\ 0 & -4 & 8 & : & -8 \end{bmatrix} $$
3.  **Row Ops ($R_3 - 4R_2$):**
    $$ \sim \begin{bmatrix} 1 & 2 & 3 & : & 3 \\ 0 & -1 & 2 & : & -2 \\ 0 & 0 & 0 & : & 0 \end{bmatrix} $$
4.  **Result:** Infinite solutions. Let $z = k$.
    *   $-y + 2k = -2 \implies y = 2k + 2$.
    *   $x + 2(2k+2) + 3k = 3 \implies x + 7k + 4 = 3 \implies x = -7k - 1$.
    **Ans:** $x = -7k-1, y=2k+2, z=k$.

#### **H.W. Problem-7**
**Find values of $k$ for solution types:**
$$ \begin{aligned} kx + y + z &= 1 \\ x + ky + z &= 1 \\ x + y + kz &= 1 \end{aligned} $$

**Solution:**
Use the Determinant of $A$:
$$ |A| = k(k^2-1) - 1(k-1) + 1(1-k) $$
$$ |A| = k(k-1)(k+1) - (k-1) - (k-1) $$
$$ |A| = (k-1) [k(k+1) - 1 - 1] = (k-1)(k^2+k-2) $$
$$ |A| = (k-1)(k+2)(k-1) = (k-1)^2(k+2) $$

1.  **Unique Solution:** $|A| \neq 0$.
    *   $k \neq 1$ and $k \neq -2$.
2.  **No Solution:**
    *   If $k = -2$: Sum of equations $\implies 0 = 3$ (Impossible). So, **No Solution** when $k = -2$.
3.  **Infinite Solutions:**
    *   If $k = 1$: All equations become $x+y+z=1$. Rank = 1. **Infinite solutions**.

---

## 12. Eigen Values and Eigen Vectors (Page 12)

### **Definitions**
If $A$ is an $n \times n$ square matrix, a non-zero vector $V$ is an **Eigenvector** if:
$$ AV = \lambda V $$
Where $\lambda$ is a scalar called the **Eigenvalue** (or characteristic root).

### **Characteristic Equation**
To find $\lambda$, we rearrange the equation:
$$ AV - \lambda I V = 0 $$
$$ (A - \lambda I)V = 0 $$
For non-trivial solutions ($V \neq 0$), the determinant of the characteristic matrix must be zero:
$$ |A - \lambda I| = 0 $$

### 👁️ **Problem 1: Finding Eigenvalues**
**Matrix:**
$$ A = \begin{bmatrix} 1 & 0 & -2 \\ 0 & 0 & 0 \\ -2 & 0 & 4 \end{bmatrix} $$

**Solution:**
1.  **Form $(A - \lambda I)$:**
    $$ \begin{bmatrix} 1-\lambda & 0 & -2 \\ 0 & -\lambda & 0 \\ -2 & 0 & 4-\lambda \end{bmatrix} $$
2.  **Set Determinant to 0:**
    Expand along row 2:
    $$ -\lambda \left[ (1-\lambda)(4-\lambda) - (-2)(-2) \right] = 0 $$
    $$ -\lambda [ 4 - \lambda - 4\lambda + \lambda^2 - 4 ] = 0 $$
    $$ -\lambda [ \lambda^2 - 5\lambda ] = 0 $$
    $$ -\lambda \cdot \lambda (\lambda - 5) = 0 $$
3.  **Roots:**
    $$ \lambda = 0, 0, 5 $$
    **Eigenvalues are 0, 0, and 5.**

## 13. Calculating Eigenvectors (Page 13)

### **Concept**
After finding Eigenvalues ($\lambda$) from $|A - \lambda I| = 0$, we find the corresponding **Eigenvectors** ($X$) by solving the homogeneous system:
$$ (A - \lambda I)X = 0 $$

### 👁️ **Problem 1 Continued: Finding Vectors**
**Recall:** Matrix $A = \begin{bmatrix} 1 & 0 & -2 \\ 0 & 0 & 0 \\ -2 & 0 & 4 \end{bmatrix}$. We found Eigenvalues $\lambda = 0, 0, 5$.

#### **Case 1: For $\lambda = 0$**
Substitute $\lambda=0$ into $(A - \lambda I)X = 0$:
$$ \begin{bmatrix} 1 & 0 & -2 \\ 0 & 0 & 0 \\ -2 & 0 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$
1.  **Equations:**
    *   $x - 2z = 0 \implies x = 2z$
    *   Row 3 is a multiple of Row 1. Row 2 is zero.
2.  **Free Variables:**
    *   Variable $y$ does not appear in the restriction, so $y$ is free ($y=1$).
    *   Variable $z$ is free. Let $z=1 \implies x=2$.
3.  **Constructing Vectors:**
    Since there are 2 instances of $\lambda=0$ and the rank is 1, we look for 2 linearly independent vectors.
    $$ X = \begin{bmatrix} 2z \\ y \\ z \end{bmatrix} = y\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + z\begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix} $$
    **Eigenvectors:** $V_1 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$ and $V_2 = \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}$.

#### **Case 2: For $\lambda = 5$**
Substitute $\lambda=5$ into $(A - 5I)X = 0$:
$$ \begin{bmatrix} -4 & 0 & -2 \\ 0 & -5 & 0 \\ -2 & 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$
1.  From Row 2: $-5y = 0 \implies y = 0$.
2.  From Row 1: $-4x - 2z = 0 \implies z = -2x$.
3.  Let $x = 1$, then $z = -2$.
    **Eigenvector:** $V_3 = \begin{bmatrix} 1 \\ 0 \\ -2 \end{bmatrix}$.

---

### 👁️ **Problem 2: Full Eigen-Analysis**
**Matrix:** $A = \begin{bmatrix} 2 & 2 & 1 \\ 1 & 3 & 1 \\ 1 & 2 & 2 \end{bmatrix}$

**Step 1: Characteristic Equation**
$$ |A - \lambda I| = \begin{vmatrix} 2-\lambda & 2 & 1 \\ 1 & 3-\lambda & 1 \\ 1 & 2 & 2-\lambda \end{vmatrix} = 0 $$
Expanding this determinant involves algebraic grouping:
$$ (2-\lambda)[(3-\lambda)(2-\lambda)-2] - 2(2-\lambda-1) + 1(2 - (3-\lambda)) = 0 $$
After simplification:
$$ (\lambda - 1)^2 (\lambda - 5) = 0 $$
**Eigenvalues:** $\lambda = 1, 1, 5$.

---

## 14. Eigenvectors Problem 2 Continued (Page 14)

We need to find vectors for $\lambda = 1$ and $\lambda = 5$.

#### **Case 1: For $\lambda = 1$**
Matrix becomes $(A - 1I)$:
$$ \begin{bmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \\ 1 & 2 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = 0 $$
1.  **Reduction:** All rows are identical. $R_2-R_1, R_3-R_1$ gives:
    $$ \begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} $$
2.  **Equation:** $x + 2y + z = 0$.
3.  **Free Variables:** Rank = 1, Variables = 3. Free vars = 2.
    Let $y = a$ and $z = b$.
    Then $x = -(2a + b)$.
    **Eigenvector:** $X = \begin{bmatrix} -(2a+b) \\ a \\ b \end{bmatrix}$.

#### **Case 2: For $\lambda = 5$**
Matrix becomes $(A - 5I)$:
$$ \begin{bmatrix} -3 & 2 & 1 \\ 1 & -2 & 1 \\ 1 & 2 & -3 \end{bmatrix} X = 0 $$
1.  **Row Operations:**
    *   Swap $R_1 \leftrightarrow R_3$ (to get 1 at top).
    *   Eliminate column 1.
    *   Resulting Matrix implies:
        $$ \begin{cases} x - 2y + z = 0 \\ -4y + 4z = 0 \implies y = z \end{cases} $$
2.  **Solution:**
    Let $z = a$. Then $y = a$.
    Substitute into Eq 1: $x - 2a + a = 0 \implies x = a$.
    **Eigenvector:** $X = \begin{bmatrix} a \\ a \\ a \end{bmatrix} = a \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$.

---

## 15. Cayley-Hamilton Theorem (Page 15)

This section contains homework problems and a major theoretical proof.

### ✍️ **Homework Problems**
*   **Problem 3:** $A = \begin{bmatrix} 4 & 6 & 6 \\ 1 & 3 & 2 \\ -1 & -4 & -3 \end{bmatrix}$. Find eigenvalues/vectors.
*   **Problem 4:** $A = \begin{bmatrix} 5 & 2 & 0 \\ -1 & 3 & 0 \\ 0 & 2 & -1 \end{bmatrix}$. **Answers:** $\lambda = 5, 3, -1$.
*   **Problem 5:** $A = \begin{bmatrix} 1 & -3 & 3 \\ 3 & -5 & 3 \\ 6 & -6 & 4 \end{bmatrix}$. **Answers:** $\lambda = 4, -2, -2$.

### **Cayley-Hamilton Theorem**
**Statement:** Every square matrix satisfies its own characteristic equation.
If the characteristic equation is $|A - \lambda I| = \lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_0 = 0$, then:
$$ A^n + a_{n-1}A^{n-1} + \dots + a_0 I = 0 $$

**Proof Explanation:**
1.  **Setup:** Let $P(\lambda) = |A - \lambda I|$ be the characteristic polynomial.
2.  **Adjoint Property:** The elements of $\text{adj}(A - \lambda I)$ are cofactors, which are polynomials in $\lambda$ of degree at most $n-1$.
    We can write the adjoint matrix as a polynomial with matrix coefficients $B_k$:
    $$ \text{adj}(A - \lambda I) = B_{n-1}\lambda^{n-1} + B_{n-2}\lambda^{n-2} + \dots + B_0 $$
3.  **Fundamental Matrix Identity:**
    $$ (A - \lambda I) \cdot \text{adj}(A - \lambda I) = |A - \lambda I| \cdot I $$
4.  **Substitution:**
    $$ (A - \lambda I)(B_{n-1}\lambda^{n-1} + \dots + B_0) = (\lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_0)I $$
5.  **Compare Coefficients of $\lambda$:**
    *   $\lambda^n$: $-B_{n-1} = I$
    *   $\lambda^{n-1}$: $AB_{n-1} - B_{n-2} = a_{n-1}I$
    *   ...
    *   $\lambda^0$: $AB_0 = a_0 I$
6.  **Telescoping Sum:**
    Multiply the first equation by $A^n$, the second by $A^{n-1}$, etc.
    $$ \begin{aligned} -A^n B_{n-1} &= A^n \\ A^n B_{n-1} - A^{n-1}B_{n-2} &= a_{n-1}A^{n-1} \\ &\vdots \\ A B_0 &= a_0 I \end{aligned} $$
7.  **Conclusion:** Adding all these equations cancels out all terms on the left (LHS = 0). The right side becomes the polynomial in A.
    $$ 0 = A^n + a_{n-1}A^{n-1} + \dots + a_0 I \quad \text{(Proved)} $$

---

## 16. Verification and Applications (Page 16)

### 👁️ **Problem 5: Verify Cayley-Hamilton**
**Given:** $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & -1 & 1 \\ 3 & 1 & 1 \end{bmatrix}$.

**Step 1: Characteristic Equation**
$$ |A - \lambda I| = \lambda^3 - \lambda^2 - 15\lambda - 15 = 0 $$

**Step 2: Matrix Powers Calculation**
*   **$A^2$:** Standard matrix multiplication $A \times A$.
    $$ A^2 = \begin{bmatrix} 14 & 3 & 8 \\ 3 & 6 & 6 \\ 8 & 6 & 11 \end{bmatrix} $$
*   **$A^3$:** Calculate $A^2 \times A$.
    $$ A^3 = \begin{bmatrix} 44 & 33 & 53 \\ 33 & 6 & 21 \\ 53 & 21 & 41 \end{bmatrix} $$

**Step 3: Verification**
Compute $A^3 - A^2 - 15A - 15I$.
$$ \begin{bmatrix} 44 \\ 33 \\ 53 \end{bmatrix} - \begin{bmatrix} 14 \\ 3 \\ 8 \end{bmatrix} - 15\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} - 15\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} $$
(Checking top-left element: $44 - 14 - 15 - 15 = 0$).
**Result:** The zero matrix. Theorem Verified.

---

### 👁️ **Problem 6: Matrix Polynomials**
**Task:** Compute $f(A)$ if $f(x) = \frac{1+x}{1-x}$ and $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.

**Method:**
In matrix algebra, division is multiplication by an inverse.
$$ f(A) = (I+A)(I-A)^{-1} $$

1.  **Compute Terms:**
    *   $I + A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$
    *   $I - A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ -2 & 0 \end{pmatrix}$

2.  **Find Inverse $(I-A)^{-1}$:**
    Let $B = I - A$. $|B| = 0 - 4 = -4$.
    $$ B^{-1} = \frac{1}{-4} \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1/2 \\ -1/2 & 0 \end{pmatrix} $$

3.  **Multiply $(I+A)B^{-1}$:**
    $$ \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} \begin{pmatrix} 0 & -0.5 \\ -0.5 & 0 \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix} $$

**Answer:** $f(A) = \begin{pmatrix} -1 & -1 \\ -1 & -1 \end{pmatrix}$.