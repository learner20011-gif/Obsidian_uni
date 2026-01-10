Here is the detailed explanation of pages 4 through 8 of the provided document, covering the basic discussion of Differential Equations and the Formation of Partial Differential Equations.

### Basic Discussion of Differential Equations (DE)

**Definition of a Differential Equation**
A differential equation is a mathematical equation that relates functions with their derivatives. Specifically, it is an equation involving derivatives of one or more dependent variable(s) with respect to (w.r.t) one or more independent variable(s).

*   **Examples:**
    *   (i) $\frac{dy}{dx} + x = 0$
    *   (ii) $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} = 0$

**Types of Differential Equations**
Differential equations are broadly categorized based on the type of derivatives they contain:

*   **1. Ordinary Differential Equation (ODE)**
    *   **Definition:** An equation involving **ordinary derivatives** of one or more dependent variable(s) with respect to a **single** independent variable.
    *   **Key Characteristic:** It depends on only one independent variable (e.g., $x$).
    *   **Example:**
        $$ \frac{d^2y}{dx^2} + x = 0 $$

*   **2. Partial Differential Equation (PDE)**
    *   **Definition:** An equation involving **partial derivatives** of one or more dependent variable(s) with respect to **two or more** independent variable(s).
    *   **Key Characteristic:** It depends on multiple independent variables (e.g., $x$ and $y$), requiring partial differentiation notation ($\partial$).
    *   **Example:**
        $$ x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = z $$

---

### Classification of Partial Differential Equations

Partial differential equations are further classified based on their linearity.

**A) Linear Partial Differential Equation**
*   **Definition:** A PDE is considered linear if it is of the **first degree** in the dependent variable and its partial derivatives. This means no derivative is raised to a power greater than 1, and there are no products of the dependent variable and its derivatives.
*   **Example:**
    $$ x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = z $$
    *   *Explanation:* Here, the partial derivatives $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$ both have a power of 1.

**B) Non-Linear Partial Differential Equation**
*   **Definition:** A PDE is considered non-linear if it is of **more than one degree** in the partial derivatives or includes products of derivatives.
*   **Example:**
    $$ x\frac{\partial z}{\partial x} + y\left(\frac{\partial z}{\partial y}\right)^2 = z $$
    *   *Explanation:* This equation is non-linear because the term $\left(\frac{\partial z}{\partial y}\right)^2$ is of the second degree.

---

### Order and Degree of Differential Equations

To analyze differential equations, it is essential to identify their order and degree.

**1. Order of the Differential Equation**
*   **Definition:** The order is defined as the order of the **highest derivative** involved in the equation.
*   **Example:**
    $$ x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = z $$
    *   *Analysis:* The derivatives are first-order ($\frac{\partial}{\partial x}$). Therefore, this is a **1st Order** Differential Equation.

**2. Degree of the Differential Equation**
*   **Definition:** The degree is the **power (exponent)** of the highest ordered derivative present in the equation, provided the equation is free from radicals and fractions regarding derivatives.
*   **Examples:**
    *   (i) $\frac{d^3 y}{dx^3} + 3\left(\frac{dy}{dx}\right)^4 = e^x$
        *   *Analysis:* The highest derivative is $\frac{d^3 y}{dx^3}$ (order 3). Its power is 1. Therefore, it is a **1st degree** Differential Equation.
    *   (ii) $\left(\frac{d^4 y}{dx^4}\right)^3 + 5\frac{d^2y}{dx^2} + 3y = 0$
        *   *Analysis:* The highest derivative is $\frac{d^4 y}{dx^4}$ (order 4). Its power is 3. Therefore, it is a **3rd degree** Differential Equation.

**Standard Notation for PDE**
In the study of PDEs involving a dependent variable $z$ and independent variables $x$ and $y$, standard abbreviations are used for partial derivatives:
*   Function: $z = f(x, y)$
*   First partial derivative w.r.t $x$: $$ p = \frac{\partial z}{\partial x} $$
*   First partial derivative w.r.t $y$: $$ q = \frac{\partial z}{\partial y} $$

---

### Formation of Partial Differential Equations

A Partial Differential Equation can be formed using two primary methods:
1.  **By eliminating arbitrary constants.**
2.  **By eliminating arbitrary functions.**

Below are examples of forming a PDE using the first method.

### Problem: Form a PDE from the equation $z = ax + by + ab$ by eliminating the arbitrary constants $a$ and $b$.

**Solution:**
**Step 1: State the given equation.**
$$ z = ax + by + ab \quad \text{..........(1)} $$

**Step 2: Differentiate partially.**
We differentiate equation (1) partially with respect to the independent variables $x$ and $y$.

*   Differentiating w.r.t $x$:
    $$ \frac{\partial z}{\partial x} = a $$
    Using standard notation, we write:
    $$ p = a $$

*   Differentiating w.r.t $y$:
    $$ \frac{\partial z}{\partial y} = b $$
    Using standard notation, we write:
    $$ q = b $$

**Step 3: Substitute values back into the original equation.**
We substitute the values of $a$ (which is $p$) and $b$ (which is $q$) back into equation (1).
$$ z = (p)x + (q)y + (p)(q) $$

**Final Result:**
$$ z = px + qy + pq $$
This represents the required Partial Differential Equation.

---

### Problem: Form a PDE from the equation $x^2 + y^2 + (z - c)^2 = a^2$ by eliminating arbitrary constants.

**Solution:**
**Step 1: State the given equation.**
$$ x^2 + y^2 + (z - c)^2 = a^2 \quad \text{..........(1)} $$
Here, the equation contains two arbitrary constants, $a$ and $c$.

**Step 2: Differentiate partially w.r.t $x$.**
Differentiating equation (1) with respect to $x$:
$$ 2x + 0 + 2(z - c)\frac{\partial z}{\partial x} = 0 $$
$$ 2x + 2(z - c)p = 0 $$
Dividing by 2:
$$ x + (z - c)p = 0 \quad \text{..........(2)} $$

**Step 3: Differentiate partially w.r.t $y$.**
Differentiating equation (1) with respect to $y$:
$$ 0 + 2y + 2(z - c)\frac{\partial z}{\partial y} = 0 $$
$$ 2y + 2(z - c)q = 0 $$
Dividing by 2:
$$ y + (z - c)q = 0 \quad \text{..........(3)} $$

**Step 4: Eliminate the constant $c$.**
To find the PDE, we must eliminate the term involving $c$ using equations (2) and (3).

From equation (2), we can isolate $(z-c)$:
$$ (z - c)p = -x $$
$$ (z - c) = -\frac{x}{p} $$

*(Note: The solution continues on the subsequent page by substituting this value into equation (3) to find the final relationship between $x, y, p,$ and $q$.)*

From the previous page, we established two derivatives:
1.  From differentiating with respect to $x$: $$ (z - c) = -\frac{x}{p} \quad \text{..........(2)} $$
2.  From differentiating with respect to $y$: $$ y + (z - c)q = 0 \quad \text{..........(3)} $$

**Step 1: Substitution**
We substitute the value of $(z-c)$ from equation (2) into equation (3):
$$ y + \left(-\frac{x}{p}\right)q = 0 $$

**Step 2: Simplification**
$$ y - \frac{xq}{p} = 0 $$
Multiplying the entire equation by $p$:
$$ yp - xq = 0 $$

**Answer:**
$$ yp - xq = 0 $$

---

### Problem: Construct the partial differential equation by eliminating the arbitrary constants $a$ and $b$ from the equation: $z = (x^2 + a^2)(y^2 + b^2)$

**Solution:**
**Step 1: Given Equation**
$$ z = (x^2 + a^2)(y^2 + b^2) \quad \text{..........(1)} $$

**Step 2: Differentiate with respect to x**
We treat $y$ as a constant. The term $(y^2 + b^2)$ acts as a constant coefficient.
$$ p = \frac{\partial z}{\partial x} = 2x(y^2 + b^2) $$
From this, we can isolate the term with $b$:
$$ (y^2 + b^2) = \frac{p}{2x} $$

**Step 3: Differentiate with respect to y**
We treat $x$ as a constant. The term $(x^2 + a^2)$ acts as a constant coefficient.
$$ q = \frac{\partial z}{\partial y} = (x^2 + a^2)2y $$
From this, we can isolate the term with $a$:
$$ (x^2 + a^2) = \frac{q}{2y} $$

**Step 4: Substitution**
Substitute the expressions found in Step 2 and Step 3 back into the original equation (1):
$$ z = \left(\frac{q}{2y}\right) \left(\frac{p}{2x}\right) $$
$$ z = \frac{pq}{4xy} $$

**Step 5: Final Arrangement**
Multiply both sides by $4xy$:
$$ 4xyz = pq $$
This is the required Partial Differential Equation.

---

### Problem: Find the partial differential equation of the family of spheres of radius one whose center lies on the $xy$-plane. 🔴

**Solution:**
**Step 1: Formulate the Geometric Equation**
The general equation of a sphere is $(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2$.
*   Since the radius is one, $r = 1$.
*   Since the center lies on the $xy$-plane, the z-coordinate of the center is zero ($c=0$). The center is $(a, b, 0)$.
The equation becomes:
$$ (x - a)^2 + (y - b)^2 + z^2 = 1 \quad \text{..........(1)} $$

**Step 2: Differentiate w.r.t x**
$$ 2(x - a) + 0 + 2z\frac{\partial z}{\partial x} = 0 $$
$$ 2(x - a) + 2zp = 0 $$
Dividing by 2 and isolating $(x-a)$:
$$ x - a = -zp \quad \text{..........(2)} $$

**Step 3: Differentiate w.r.t y**
$$ 0 + 2(y - b) + 2z\frac{\partial z}{\partial y} = 0 $$
$$ 2(y - b) + 2zq = 0 $$
Dividing by 2 and isolating $(y-b)$:
$$ y - b = -zq \quad \text{..........(3)} $$

**Step 4: Eliminate Constants**
Substitute values from (2) and (3) back into equation (1):
$$ (-zp)^2 + (-zq)^2 + z^2 = 1 $$
$$ z^2p^2 + z^2q^2 + z^2 = 1 $$

**Final Result:**
Factor out $z^2$:
$$ z^2(p^2 + q^2 + 1) = 1 $$
Alternatively written as:
$$ z^2(p^2 + q^2 + 1)^2 = 1 $$ *(Note: The slide has a typo squaring the bracket in the final line, but the line before is the standard simplified form).*

---

### Theory: Method of Elimination of Arbitrary Functions

This section introduces the second method for forming PDEs. We consider a relation between independent variables $x, y, z$ involving an arbitrary function $\phi$.

**Methodology:**
Let an arbitrary function be defined as $\phi(u, v) = 0$, where $u = u(x, y, z)$ and $v = v(x, y, z)$ are known functions of the coordinates.

**Step 1: Differentiate the Function Relation**
We differentiate the equation $\phi(u, v) = 0$ with respect to $x$ and $y$. Since $z$ is dependent on $x$ and $y$, we must use the chain rule.

*   **Differentiating w.r.t $x$:**
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial x} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial x} \right) = 0 $$
    Using $p = \frac{\partial z}{\partial x}$:
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial x} + p\frac{\partial u}{\partial z} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial x} + p\frac{\partial v}{\partial z} \right) = 0 \quad \text{..........(ii)} $$

*   **Differentiating w.r.t $y$:**
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial y} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial y} \right) = 0 $$
    Using $q = \frac{\partial z}{\partial y}$:
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial y} + q\frac{\partial u}{\partial z} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial y} + q\frac{\partial v}{\partial z} \right) = 0 \quad \text{..........(iii)} $$

---

### Theory: Derivation of Lagrange's Linear Equation

Continuing from the differentiation in the previous section, we must eliminate the partial derivatives of the arbitrary function $\phi$ (i.e., $\frac{\partial \phi}{\partial u}$ and $\frac{\partial \phi}{\partial v}$) to form the PDE.

**Step 2: Eliminating $\phi$ terms using Determinants**
We have a system of homogeneous linear equations in terms of $\frac{\partial \phi}{\partial u}$ and $\frac{\partial \phi}{\partial v}$. For a non-trivial solution, the determinant of their coefficients must be zero.

$$
\begin{vmatrix}
\frac{\partial u}{\partial x} + p\frac{\partial u}{\partial z} & \frac{\partial v}{\partial x} + p\frac{\partial v}{\partial z} \\
\frac{\partial u}{\partial y} + q\frac{\partial u}{\partial z} & \frac{\partial v}{\partial y} + q\frac{\partial v}{\partial z}
\end{vmatrix} = 0
$$

**Step 3: Expansion of the Determinant**
Expanding the determinant (cross-multiplying):
$$ \left( \frac{\partial u}{\partial x} + p\frac{\partial u}{\partial z} \right) \left( \frac{\partial v}{\partial y} + q\frac{\partial v}{\partial z} \right) - \left( \frac{\partial v}{\partial x} + p\frac{\partial v}{\partial z} \right) \left( \frac{\partial u}{\partial y} + q\frac{\partial u}{\partial z} \right) = 0 $$

**Step 4: Grouping Terms**
We expand the multiplication and group terms by $p$, $q$, and those without derivatives of $z$.
$$ p \left( \frac{\partial u}{\partial z}\frac{\partial v}{\partial y} - \frac{\partial v}{\partial z}\frac{\partial u}{\partial y} \right) + q \left( \frac{\partial u}{\partial x}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial x} \right) = \left( \frac{\partial u}{\partial y}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial y} \right) $$

**Step 5: Jacobians Notation**
This equation can be written compactly using Jacobian notation. Let us define $P$, $Q$, and $R$:

*   $$ P = \frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y} $$ (Note: The sign is reversed in the slide's standard form derivation compared to the expansion, often absorbed into the definition of $R$).
    *   *Correction based on slide notation:* The slide defines:
        $$ \lambda P = \frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y} $$
        $$ \lambda Q = \frac{\partial u}{\partial z}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial z} $$
        $$ \lambda R = \frac{\partial u}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial x} $$

**Step 6: Final Linear Form**
Substituting these definitions into the expanded equation results in **Lagrange's Linear Partial Differential Equation**:
$$ Pp + Qq = R $$

---

### Theory: Lagrange's Auxiliary Equations

The theory connects the linear PDE back to the original solutions $u$ and $v$.

**Relationship to Total Differentials:**
If $u(x, y, z) = c_1$ and $v(x, y, z) = c_2$ are solutions, differentiating them yields:
$$ \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy + \frac{\partial u}{\partial z}dz = 0 \quad \text{..........(vi)} $$
$$ \frac{\partial v}{\partial x}dx + \frac{\partial v}{\partial y}dy + \frac{\partial v}{\partial z}dz = 0 \quad \text{..........(vii)} $$

**Solving for Ratios:**
Solving equations (vi) and (vii) using cross-multiplication (Cramer's rule) for the ratios of $dx, dy, dz$:
$$ \frac{dx}{\frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y}} = \frac{dy}{\frac{\partial u}{\partial z}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial z}} = \frac{dz}{\frac{\partial u}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial x}} $$

Using the definitions of $P, Q, R$ from the previous section:
$$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$

These are known as **Lagrange's Auxiliary Equations**. They provide the method to solve linear PDEs of the form $Pp + Qq = R$.


Here is the detailed explanation of pages 14 through 18 of the provided document.

### Problem: Find the partial differential equation of the relation $\phi\left(\frac{z}{x^2}, x^2 - y^2 + z\right) = 0$.

**Solution:**
**Step 1: Define the intermediate variables**
Let the arguments of the arbitrary function $\phi$ be $u$ and $v$.
$$ u = \frac{z}{x^2} $$
$$ v = x^2 - y^2 + z $$
The given equation becomes $\phi(u, v) = 0$ .........(ii)

**Step 2: Differentiate with respect to x**
We differentiate equation (ii) partially with respect to $x$. Using the chain rule for multivariable calculus:
$$ \frac{\partial \phi}{\partial u}\left( \frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial x} \right) + \frac{\partial \phi}{\partial v}\left( \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial x} \right) = 0 $$

Now, we calculate the partial derivatives for $u$ and $v$:
*   For $u = zx^{-2}$:
    $$ \frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial x} = z(-2x^{-3}) + x^{-2}p = \frac{-2z}{x^3} + \frac{1}{x^2}p $$
*   For $v = x^2 - y^2 + z$:
    $$ \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial x} = 2x + p $$

Substituting these into the chain rule equation:
$$ \frac{\partial \phi}{\partial u}\left( \frac{-2z}{x^3} + \frac{1}{x^2}p \right) + \frac{\partial \phi}{\partial v}(2x + 1 \cdot p) = 0 \quad \text{.........(iii)} $$

---

**Step 3: Differentiate with respect to y**
We differentiate equation (ii) partially with respect to $y$:
$$ \frac{\partial \phi}{\partial u}\left( \frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial y} \right) + \frac{\partial \phi}{\partial v}\left( \frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial y} \right) = 0 $$

Calculating the partial derivatives:
*   For $u = z/x^2$ (treating $x$ as constant):
    $$ \frac{\partial u}{\partial y}+\frac{\partial u}{\partial z}\frac{\partial z}{\partial y} = 0 + \frac{1}{x^2}q $$
*   For $v = x^2 - y^2 + z$:
    $$ \frac{\partial v}{\partial y}+ \frac{\partial v}{\partial z}\frac{\partial z}{\partial y}  = -2y + q $$

Substituting these into the equation:
$$ \frac{\partial \phi}{\partial u}\left( 0 + \frac{1}{x^2}q \right) + \frac{\partial \phi}{\partial v}(-2y + 1 \cdot q) = 0 \quad \text{.........(iv)} $$

**Step 4: Eliminate $\phi$ using a Determinant**
To eliminate the unknown partial derivatives $\frac{\partial \phi}{\partial u}$ and $\frac{\partial \phi}{\partial v}$, we set the determinant of the coefficients from equations (iii) and (iv) to zero:

$$
\begin{vmatrix}
\frac{-2z}{x^3} + \frac{p}{x^2} & 2x + p \\
\frac{q}{x^2} & -2y + q
\end{vmatrix} = 0
$$

**Step 5: Expansion and Simplification**
Expand the determinant (AD - BC = 0):
$$ \left( \frac{-2z}{x^3} + \frac{p}{x^2} \right)(-2y + q) - (2x + p)\left( \frac{q}{x^2} \right) = 0 $$

Multiply the terms out:
$$ \frac{4yz}{x^3} - \frac{2zq}{x^3} - \frac{2yp}{x^2} + \frac{pq}{x^2} - \frac{2xq}{x^2} - \frac{pq}{x^2} = 0 $$

Notice that $+ \frac{pq}{x^2}$ and $- \frac{pq}{x^2}$ cancel each other out.
$$ \frac{4yz}{x^3} - \frac{2zq}{x^3} - \frac{2yp}{x^2} - \frac{2q}{x} = 0 $$

Multiply the entire equation by $x^3$ to clear the denominators:
$$ 4yz - 2zq - 2xyp - 2x^2q = 0 $$

Rearrange the terms to group $p$ and $q$:
$$ 4yz = 2xyp + 2zq + 2x^2q $$
Divide by 2:
$$ 2yz = xyp + q(z + x^2) $$

**Final Answer:**
$$ xyp + q(x^2 + z) = 2yz $$

---

### Problem: Find the partial differential equation arising from $\phi(x + y + z, x^2 + y^2 - z^2) = 0$. 🔴

**Solution:**
**Step 1: Define variables**
Given $\phi(x + y + z, x^2 + y^2 - z^2) = 0$ .........(i)
Let:
$$ u = x + y + z $$
$$ v = x^2 + y^2 - z^2 $$
The equation becomes $\phi(u, v) = 0$ .........(ii)

**Step 2: Differentiate with respect to x**
Using the chain rule:
$$ \frac{\partial \phi}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial \phi}{\partial v}\frac{\partial v}{\partial x} = 0 $$
Calculating partials:
*   $u_x = 1 + p$
*   $v_x = 2x - 2zp$
Substituting:
$$ \frac{\partial \phi}{\partial u}(1 + 1 \cdot p) + \frac{\partial \phi}{\partial v}(2x - 2z \cdot p) = 0 \quad \text{.........(iii)} $$

**Step 3: Differentiate with respect to y**
Using the chain rule:
$$ \frac{\partial \phi}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial \phi}{\partial v}\frac{\partial v}{\partial y} = 0 $$
Calculating partials:
*   $u_y = 1 + q$
*   $v_y = 2y - 2zq$
Substituting:
$$ \frac{\partial \phi}{\partial u}(1 + 1 \cdot q) + \frac{\partial \phi}{\partial v}(2y - 2z \cdot q) = 0 \quad \text{.........(iv)} $$

**Step 4: Eliminate $\phi$ terms**
We eliminate $\frac{\partial \phi}{\partial u}$ and $\frac{\partial \phi}{\partial v}$ from equations (iii) and (iv) using a determinant:

$$
\begin{vmatrix}
1 + p & 2x - 2zp \\
1 + q & 2y - 2zq
\end{vmatrix} = 0
$$

**Step 5: Expand the determinant**
$$ (1 + p)(2y - 2zq) - (2x - 2zp)(1 + q) = 0 $$

Multiply the factors:
$$ (2y - 2zq + 2yp - 2zpq) - (2x + 2xq - 2zp - 2zpq) = 0 $$

Notice that $-2zpq$ appears in both expanded groups (one is being subtracted), so they cancel out:
$$ 2y - 2zq + 2yp - 2x - 2xq + 2zp = 0 $$

**Step 6: Group terms**
Group terms containing $p$, terms containing $q$, and the remaining terms:
$$ p(2y + 2z) - q(2x + 2z) + (2y - 2x) = 0 $$

Divide the entire equation by 2:
$$ p(y + z) - q(x + z) + y - x = 0 $$

Rearrange to the standard form ($Pp + Qq = R$):
$$ p(y + z) - q(x + z) = x - y $$

**Final Answer:**
This is the required PDE.

---

### Problem: Form the partial differential equation from $z = f(x^2 - y^2)$.

**Solution:**
**Step 1: Given Equation**
$$ z = f(x^2 - y^2) \quad \text{.........(1)} $$

**Step 2: Differentiate w.r.t x**
Differentiating equation (1) partially with respect to $x$. We apply the chain rule to the function $f$.
Let the argument be $t = x^2 - y^2$.
$$ p = \frac{\partial z}{\partial x} = f'(x^2 - y^2) \cdot \frac{\partial}{\partial x}(x^2 - y^2) $$
$$ p = f'(x^2 - y^2) \cdot 2x \quad \text{.........(2)} $$

**Step 3: Differentiate w.r.t y**
Differentiating equation (1) partially with respect to $y$.
$$ q = \frac{\partial z}{\partial y} = f'(x^2 - y^2) \cdot \frac{\partial}{\partial y}(x^2 - y^2) $$
$$ q = f'(x^2 - y^2) \cdot (-2y) \quad \text{.........(3)} $$

**Step 4: Eliminate the arbitrary function $f'$**
To eliminate $f'(x^2 - y^2)$, we divide equation (2) by equation (3):
$$ \frac{p}{q} = \frac{f'(x^2 - y^2) \cdot 2x}{f'(x^2 - y^2) \cdot (-2y)} $$

The term $f'(x^2 - y^2)$ cancels out, as does the 2:
$$ \frac{p}{q} = \frac{x}{-y} $$

**Step 5: Final Arrangement**
Cross-multiply to linearize the equation:
$$ -py = qx $$
$$ py + qx = 0 $$

**Answer:**
$$ yp + xq = 0 $$


### Problem: Eliminate the arbitrary functions from the relation $u = f(x + at) + g(x - at)$. 🔴

**Solution:**
**Step 1: State the Given Equation**
$$ u = f(x + at) + g(x - at) \quad \text{..........(1)} $$
Here, $u$ is a function of independent variables $x$ and $t$. We need to eliminate the functions $f$ and $g$. Since there are two arbitrary functions, we will likely need second-order derivatives.

**Step 2: Differentiate Twice with Respect to x**
First partial derivative w.r.t $x$:
$$ \frac{\partial u}{\partial x} = f'(x + at) \cdot (1) + g'(x - at) \cdot (1) $$
$$ \frac{\partial u}{\partial x} = f'(x + at) + g'(x - at) $$

Second partial derivative w.r.t $x$:
$$ \frac{\partial^2 u}{\partial x^2} = f''(x + at) + g''(x - at) \quad \text{..........(2)} $$

**Step 3: Differentiate Twice with Respect to t**
First partial derivative w.r.t $t$ (using the Chain Rule):
The derivative of $(x + at)$ w.r.t $t$ is $a$.
The derivative of $(x - at)$ w.r.t $t$ is $-a$.
$$ \frac{\partial u}{\partial t} = f'(x + at) \cdot (a) + g'(x - at) \cdot (-a) $$
$$ \frac{\partial u}{\partial t} = a f'(x + at) - a g'(x - at) $$

Second partial derivative w.r.t $t$:
$$ \frac{\partial^2 u}{\partial t^2} = a f''(x + at) \cdot (a) - a g''(x - at) \cdot (-a) $$
$$ \frac{\partial^2 u}{\partial t^2} = a^2 f''(x + at) + a^2 g''(x - at) $$

**Step 4: Comparison and Substitution**
Factor out $a^2$ from the equation derived in Step 3:
$$ \frac{\partial^2 u}{\partial t^2} = a^2 [ f''(x + at) + g''(x - at) ] $$

Notice that the term in the brackets is exactly equal to equation (2). Substitute Eq. (2) into this expression:
$$ \frac{\partial^2 u}{\partial t^2} = a^2 \frac{\partial^2 u}{\partial x^2} $$

**Final Result:**
This is the required partial differential equation (known as the one-dimensional Wave Equation).

---

### Problem: Eliminate the arbitrary functions from the relation $u = f(x + iy) + g(x - iy)$.

**Solution:**
**Step 1: State the Given Equation**
$$ u = f(x + iy) + g(x - iy) \quad \text{..........(1)} $$
Here, $i$ is the imaginary unit where $i^2 = -1$.

**Step 2: Differentiate Twice with Respect to x**
First partial derivative w.r.t $x$:
$$ \frac{\partial u}{\partial x} = f'(x + iy) + g'(x - iy) $$

Second partial derivative w.r.t $x$:
$$ \frac{\partial^2 u}{\partial x^2} = f''(x + iy) + g''(x - iy) \quad \text{..........(2)} $$

**Step 3: Differentiate Twice with Respect to y**
First partial derivative w.r.t $y$ (using the Chain Rule):
The derivative of $(x + iy)$ w.r.t $y$ is $i$.
The derivative of $(x - iy)$ w.r.t $y$ is $-i$.
$$ \frac{\partial u}{\partial y} = f'(x + iy) \cdot (i) + g'(x - iy) \cdot (-i) $$
$$ \frac{\partial u}{\partial y} = i f'(x + iy) - i g'(x - iy) $$

Second partial derivative w.r.t $y$:
$$ \frac{\partial^2 u}{\partial y^2} = i f''(x + iy) \cdot (i) - i g''(x - iy) \cdot (-i) $$
$$ \frac{\partial^2 u}{\partial y^2} = i^2 f''(x + iy) + i^2 g''(x - iy) $$

**Step 4: Comparison and Substitution**
Recall that $i^2 = -1$. Substitute this value into the equation from Step 3:
$$ \frac{\partial^2 u}{\partial y^2} = -1 \cdot f''(x + iy) - 1 \cdot g''(x - iy) $$
$$ \frac{\partial^2 u}{\partial y^2} = - [ f''(x + iy) + g''(x - iy) ] $$

From equation (2), we know that the term in the brackets is $\frac{\partial^2 u}{\partial x^2}$.
$$ \frac{\partial^2 u}{\partial y^2} = - \frac{\partial^2 u}{\partial x^2} $$

**Final Result:**
Rearranging the terms to one side gives the required PDE (known as the Laplace Equation):
$$ \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 $$

---

### Homework Problems and Reference

This page lists practice problems for students to solve on their own, along with the final answers to check their work.

**Homework (H.W.) - Form the partial differential equation:**

### Problem: $z = (x + a)(y + b)$
**Answer:** $pq = z$

### Problem: $(x - h)^2 + (y - k)^2 + z^2 = a^2$
**Answer:** $z^2(p^2 + q^2 + 1) = a^2$

### Problem: $2z = (ax + y)^2 + b$
**Answer:** $px + qy = q^2$

### Problem: $ax^2 + by^2 + z^2 = 1$
**Answer:** $z(px + qy) = z^2 - 1$

### Problem: $x^2 + y^2 = (z - c)^2 \tan^2 \alpha$
**Answer:** $yp - xq = 0$
*(Note: This answer suggests the problem involves eliminating rotational symmetry constants, though standard derivation for cones often yields $p^2+q^2 = \tan^2 \alpha$. The provided answer $yp - xq = 0$ specifically implies elimination leading to cylindrical symmetry).*

### Problem: $z = f(x^2 + y^2)$
**Answer:** $yp - xq = 0$

### Problem: $2z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$
**Answer:** $2z = xp + yq$

### Problem: $f(x + y + z, x^2 + y^2 + z^2) = 0$
**Answer:** $(y - z)p + (z - x)q = x - y$

**Reference Book Recommendation:**
*   **N.B.:** For more information and practice, follow the book **"Ordinary and Partial Differential Equations"** by **M.D. Raisinghania**.