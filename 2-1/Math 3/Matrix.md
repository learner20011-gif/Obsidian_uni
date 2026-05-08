

---

## **Branch 1: Matrix Fundamentals & Classifications**

### **1.1 Core Definitions**

- **Matrix:** A rectangular array of numbers enclosed by a pair of $1^{st}$ or $3^{rd}$ brackets and subject to certain rules of operations.
    
- **Trace of a Matrix:** The sum of the diagonal elements of a square matrix.
    
    - **Explicit Formula:** $Trace(A)=\Sigma_{i=1}^{n}a_{ii}=a_{11}+a_{22}+\cdot\cdot\cdot+a_{nn}$
        

### **1.2 Structural Classifications (Types of Matrices)**

- **Square matrix:** A matrix $A=[a_{ij}]$ where the number of rows equals the number of columns ($i=j$).
    
- **Unit/Identity matrix ($I$):** A square matrix where all non-diagonal elements are zero and all diagonal elements are unity ($1$).
    
- **Diagonal matrix:** A square matrix where all its non-diagonal elements are precisely zero.
    
- **Scalar matrix:** A diagonal matrix whose all diagonal elements are equal.
    
- **Zero/Null matrix:** A matrix whose all elements are zero.
    
- **Upper triangular matrix:** A square matrix where elements below the main diagonal ($i>j$) are zero.
    
- **Lower triangular matrix:** A square matrix where elements above the main diagonal ($i<j$) are zero.
    

---

## **Branch 2: Matrix Operations & Relational Properties**

### **2.1 Operational Mechanics**

- **Matrix Multiplication Formula:** When multiplying two matrices $A$ and $B$, the specific element $d_{ik}$ in the resulting product matrix $AB$ is calculated using the summation formula: $d_{ik}=\Sigma_{j=1}^{n}a_{ij}b_{jk}$.
    
- **Associative Law:** Matrix multiplication is associative: $A(BC)=(AB)C$.
    

### **2.2 Relational Matrices**

- **Commutative matrix:** Two square matrices A and B where $AB=BA$.
    
- **Anti-commutative matrix:** Two square matrices A and B where $AB=-BA$.
    
- **Idempotent matrix:** A square matrix where $A^{2}=A$.
    
- **Involuntary matrix:** A square matrix where $A^{2}=I$.
    

### **2.3 Transpose and Conjugate Properties**

- **Transpose Concept ($A^{\prime}$):** Formed by interchanging rows with columns.
    
- **Transpose of Product Theorem:** $(AB)^{\prime}=B^{\prime}A^{\prime}$.
    
- **Symmetric matrix:** $A^{\prime}=A$ (i.e., $a_{ij}=a_{ji}$).
    
- **Skew symmetric matrix:** $A^{\prime}=-A$ (i.e., $a_{ij}=-a_{ji}$). _(Note: The diagonal elements of a skew-symmetric matrix are always mathematically zero)._
    
- **Conjugates of a matrix ($\overline{A}$):** Formed by the complex conjugates of its elements.
    
- **Hermitian matrix:** $\overline{A^{\prime}}=A$.
    
- **Skew hermitian matrix:** $\overline{A^{\prime}}=-A$.
    
- **Orthogonal matrix:** $A^{\prime}A=I$.
    
- **Unitary matrix:** $\overline{A^{\prime}}A=I$.
    

---

## **Branch 3: Adjoints, Cofactors, and Inverses**

### **3.1 Cofactor and Minor Mechanics**

- **Minor Concept:** The minor is defined as the sub-determinant of a matrix after removing a specific row and column.
    
- **Explicit Cofactor Formula:** The cofactor dictates the strict sign based on position: $(-1)^{i+j} \times minor$.
    

### **3.2 Adjoint Theorems**

- **Adjoint of a Matrix ($adj~A$):** The transpose of the cofactor matrix of A.
    
- **Theorem 1:** For any n-square matrix A, $A.(adj~A)=(adj~A)A=|A|.I_{n}$.
    
- **Theorem 2:** If $|A|\ne0$, then $adj(adj~A)=|A|^{n-2}A$.
    

### **3.3 Inverse Matrix Theory**

- **Singularity:** A square matrix is singular if $|A|=0$ and non-singular if $|A|\ne0$.
    
- **Inverse Formula ($A^{-1}$):** Only exists for non-singular matrices: $A^{-1}=\frac{adjA}{|A|}$.
    

---

## **Branch 4: Rank Theory and Canonical Forms**

### **4.1 Definition and Rules of Rank**

- **Rank Conditions ($\rho(A)=r$):** The rank is $r$ if every minor of order $r+1$ is zero, and there is at least one minor of order $r$ that is not zero.
    
- **Null Matrix Rule:** The rank of a null matrix is exactly zero.
    

### **4.2 Target Canonical / Normal Forms**

- **Methodology:** Using elementary transformations, a matrix of rank $r>0$ must be reduced to specific block matrix shapes to reveal its rank.
    
- **Explicit Target Forms:** You aim to reduce the matrix into one of these exact structures:
    
    1. $[I_{r}]$
        
    2. $[\begin{matrix}I_{r}&0\\ 0&0\end{matrix}]$
        
    3. $[\begin{matrix}I_{r}\\ 0\end{matrix}]$
        
    4. $[I_{r}~0]$
        

---

## **Branch 5: Systems of Linear Equations**

### **5.1 Setup and Representation**

- **Matrix Equation:** $AX=B$ (where A is the coefficient matrix, B is the constant matrix).
    
- **Homogeneity:** Homogeneous if $B=0$; Non-homogeneous if $B\ne0$.
    
- **Augmented Matrix ($A^{*}$):** Formed by appending B to A: $[A:B]$.
    

### **5.2 Consistency and Problem-Solving Mechanics**

- **Inconsistent System (No Solution):** Occurs if $\rho(A)\ne\rho(A^{*})$.
    
- **Consistent System (Has Solutions):** Occurs if $\rho(A)=\rho(A^{*})$.
    
    - **Unique Solution:** Occurs if $\rho(A)=r=n$ (where $n$ is the total number of variables).
        
    - **Infinite Solutions:** Occurs if $\rho(A)=\rho(A^{*})<n$.
        
    - **Free Variable Formula:** When infinite solutions exist, you must assign arbitrary constants. The formula is: $\text{Number of free variables} = \text{Total variables (n)} - \text{Rank (r)}$.
        

---

## **Branch 6: Eigenvalues, Eigenvectors, & Polynomials**

### **6.1 Eigen Theories and Setup**

- **General Formula:** $AV=\lambda V$ (where $\lambda$ is the eigenvalue/characteristic root, and $V$ is the eigenvector/characteristic vector).
    
- **Characteristic Polynomial:** The determinant $|A-\lambda I|$.
    
- **Step 1: Finding Eigenvalues:** Solve the characteristic equation $|A-\lambda I|=0$.
    
- **Step 2: Finding Eigenvectors:** Plug each $\lambda$ back into the homogeneous linear system setup $[A-\lambda I]X=0$ and solve for vector $X$.
    

### **6.2 Cayley-Hamilton Theorem & Matrix Polynomials**

- **Cayley-Hamilton Statement:** Every square matrix satisfies its own characteristic equation.
    
- **Cayley-Hamilton Proof Formula:** If $|A-\lambda I|=\lambda^{n}+a_{n-1}\lambda^{n-1}+\cdot\cdot\cdot+a_{0}=0$, then replacing $\lambda$ with matrix $A$ yields $A^{n}+a_{n-1}A^{n-1}+\cdot\cdot\cdot+a_{0}I_{n}=0$.
    
- **Solving Fractional Matrix Polynomials:** When a function involves division, e.g., $f(x)=\frac{1+x}{1-x}$, matrices cannot be divided. It must be converted into an inverse multiplication operation: $f(A)=(I+A)(I-A)^{-1}$.