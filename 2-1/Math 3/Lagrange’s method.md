Here is the detailed explanation of pages 4 through 9 from the provided document.

### Theory: Linear Partial Differential Equation of Order One (Page 4)

**Definition**
A partial differential equation (PDE) is classified as a **linear partial differential equation of order one** if it meets specific criteria regarding its structure and the nature of its derivatives.

*   **Order:** The equation must contain only **first-order** partial derivatives.
    *   These are denoted as $p = \frac{\partial z}{\partial x}$ and $q = \frac{\partial z}{\partial y}$.
*   **Linearity:** The derivatives $p$ and $q$ must appear in the **first degree** (power of 1).
*   **Restrictions:** The equation must **not** contain any transcendental functions (like $\sin p$, $e^q$) or product terms of the derivatives (like $p \cdot q$).

**Example:**
$$ px + qy = z^2 $$
*   Here, $p$ and $q$ are first-order derivatives.
*   They are not multiplied together, nor are they raised to a power higher than 1.
*   Therefore, this is a linear PDE of order one.

---

### Theory: Lagrange's Method Theorem and Proof (Page 5)

**Theorem Statement**
If the functions $u(x, y, z) = c_1$ and $v(x, y, z) = c_2$ represent two independent solutions of the auxiliary equations:
$$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$
where $P, Q,$ and $R$ are functions of $x, y, z$, then the general solution of the Lagrange’s linear equation:
$$ Pp + Qq = R $$
is given by:
$$ \phi(u, v) = 0 \quad \text{or} \quad v = \phi(u) $$
where $\phi$ is an arbitrary function.

**Proof - Part 1: Setup**
Let $u$ and $v$ be two functions of the variables $x, y, z$ connected by an arbitrary functional relation:
$$ \phi(u, v) = 0 \quad ......(i) $$

To eliminate the arbitrary function $\phi$, we differentiate equation (i) partially with respect to independent variables $x$ and $y$. Note that $z$ is a function of $x$ and $y$.

1.  **Differentiating with respect to $x$:**
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial x} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial x} \right) = 0 \quad ......(ii) $$

2.  **Differentiating with respect to $y$:**
    $$ \frac{\partial \phi}{\partial u} \left( \frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial y} \right) + \frac{\partial \phi}{\partial v} \left( \frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial y} \right) = 0 \quad ......(iii) $$

**Proof - Part 2: Elimination of Arbitrary Function**
We now eliminate the partial derivatives of the arbitrary function, $\frac{\partial \phi}{\partial u}$ and $\frac{\partial \phi}{\partial v}$, from equations (ii) and (iii). This forms a system of homogeneous linear equations. For a non-trivial solution to exist, the determinant of the coefficients must be zero.

**Determinant Form:**
$$ 
\begin{vmatrix}
\frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial x} & \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial x} \\
\frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}\frac{\partial z}{\partial y} & \frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}\frac{\partial z}{\partial y}
\end{vmatrix} = 0
$$ 

**Standard Notation Substitution:**
Using $p = \frac{\partial z}{\partial x}$ and $q = \frac{\partial z}{\partial y}$, the determinant becomes:
$$ 
\begin{vmatrix}
\frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}p & \frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}p \\
\frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}q & \frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}q
\end{vmatrix} = 0
$$ 

**Expansion:**
Expanding the determinant ($AD - BC = 0$):
$$ \left(\frac{\partial u}{\partial x} + \frac{\partial u}{\partial z}p\right) \left(\frac{\partial v}{\partial y} + \frac{\partial v}{\partial z}q\right) - \left(\frac{\partial v}{\partial x} + \frac{\partial v}{\partial z}p\right) \left(\frac{\partial u}{\partial y} + \frac{\partial u}{\partial z}q\right) = 0 $$ 

**Rearrangement:**
Expanding the products and grouping the terms by $p$, $q$, and the remaining terms:
$$ p \left( \frac{\partial u}{\partial z}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial z} \right) + q \left( \frac{\partial u}{\partial x}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial x} \right) = \left( \frac{\partial u}{\partial y}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial y} \right) \quad ......(iv) $$ 

**Proof - Part 3: Defining Coefficients and Auxiliary Equations**
To simplify equation (iv), we define $P, Q,$ and $R$ using Jacobian-style notation (or simply as coefficients):

*   Let $\lambda P = \frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y}$
*   Let $\lambda Q = \frac{\partial u}{\partial z}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial z}$
*   Let $\lambda R = \frac{\partial u}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial x}$

Substituting these into equation (iv):
$$ p(\lambda P) + q(\lambda Q) = \lambda R $$
Dividing by $\lambda$:
$$ Pp + Qq = R \quad ......(v) $$
This is **Lagrange’s linear partial differential equation**.

**Deriving the Auxiliary Equations:**
We assumed $u(x, y, z) = c_1$ and $v(x, y, z) = c_2$ are solutions. Differentiating these total differential equations gives:
1.  $$ du = \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy + \frac{\partial u}{\partial z}dz = 0 \quad ......(vi) $$
2.  $$ dv = \frac{\partial v}{\partial x}dx + \frac{\partial v}{\partial y}dy + \frac{\partial v}{\partial z}dz = 0 \quad ......(vii) $$

Solving equations (vi) and (vii) for the ratios $dx:dy:dz$ using cross-multiplication (Cramer's rule):
$$ \frac{dx}{\frac{\partial u}{\partial y}\frac{\partial v}{\partial z} - \frac{\partial u}{\partial z}\frac{\partial v}{\partial y}} = \frac{dy}{\frac{\partial u}{\partial z}\frac{\partial v}{\partial x} - \frac{\partial u}{\partial x}\frac{\partial v}{\partial z}} = \frac{dz}{\frac{\partial u}{\partial x}\frac{\partial v}{\partial y} - \frac{\partial u}{\partial y}\frac{\partial v}{\partial x}} $$ 

Substituting the definitions of $P, Q,$ and $R$ derived earlier:
$$ \frac{dx}{\lambda P} = \frac{dy}{\lambda Q} = \frac{dz}{\lambda R} $$ 
$$ \text{or, } \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$ 

These are the required **Lagrange’s auxiliary equations**.

---

### Theory: Working Rule for Lagrange's Method (Page 8)

To solve a linear PDE of the form $Pp + Qq = R$:

1.  **First Step:** Write down the auxiliary equations (also called subsidiary equations):
    $$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$ 
2.  **Second Step:** Solve the auxiliary equations to find two independent integrals (solutions).
    Let the two solutions be $u(x,y,z) = c_1$ and $v(x,y,z) = c_2$.
3.  **Third Step:** The general solution is written as:
    $$ f(u, v) = 0 \quad \text{or} \quad u = \phi(v) $$ 
    where $f$ or $\phi$ is an arbitrary function.

### Problem: Solve the following PDE: $yq - xp = z$
*Note: Standard notation is $p = \frac{\partial z}{\partial x}$ and $q = \frac{\partial z}{\partial y}$.*

**Step 1: Identify Standard Form**
Rearrange the equation to match $Pp + Qq = R$:
$$ -xp + yq = z $$
Here:
*   $P = -x$
*   $Q = y$
*   $R = z$

**Step 2: Form Auxiliary Equations**
$$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$ 
Substituting the values:
$$ \frac{dx}{-x} = \frac{dy}{y} = \frac{dz}{z} $$ 

---

**Step 3: Solve Auxiliary Equations**

*   **Finding first solution ($u$):**
    Take the first two fractions:
    $$ \frac{dx}{-x} = \frac{dy}{y} $$ 
    $$ -\log x = \log y - \log a $$ (where $\log a$ is an integration constant)
    Rearranging:
    $$ \log a = \log y + \log x $$ 
    $$ \log a = \log(xy) $$ 
    $$ xy = a \quad ......(1) $$ 

*   **Finding second solution ($v$):**
    Take the last two fractions:
    $$ \frac{dy}{y} = \frac{dz}{z} $$ 
    $$ \log y = \log z + \log b $$ (where $\log b$ is an integration constant)
    $$ \log y - \log z = \log b $$ 
    $$ \log\left(\frac{y}{z}\right) = \log b $$ 
    $$ \frac{y}{z} = b \quad ......(2) $$ 

**Step 4: General Solution**
Using the solutions from (1) and (2), the general solution is:
$$ f\left(xy, \frac{y}{z}\right) = 0 $$ 
**Ans.**

---

### Problem: Solve the PDE: $y^2p - xyq = x(z - 2y)$

**Step 1: Identify Standard Form**
The equation is already in the form $Pp + Qq = R$:
$$ y^2p - xyq = x(z - 2y) $$ 
Here:
*   $P = y^2$
*   $Q = -xy$
*   $R = x(z - 2y)$

**Step 2: Form Auxiliary Equations**
$$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} $$ 
Substituting the values:
$$ \frac{dx}{y^2} = \frac{dy}{-xy} = \frac{dz}{x(z - 2y)} \quad ......(1) $$ 

**Step 3: Solving the First Integral**
We take the first two members of the auxiliary equations derived on the previous page:
$$ \frac{dx}{y^2} = \frac{dy}{-xy} $$ 
Canceling $y$ from the denominators (assuming $y \neq 0$):
$$ \frac{dx}{y} = \frac{dy}{-x} $$ 
Cross-multiplying:
$$ -x dx = y dy \implies x dx + y dy = 0 $$ 
Integrating both sides:
$$ \int x dx + \int y dy = C $$ 
$$ \frac{x^2}{2} + \frac{y^2}{2} = \frac{C_1}{2} $$ 
Multiplying by 2:
$$ x^2 + y^2 = C_1 \quad \text{..........(2)} $$ 

**Step 4: Solving the Second Integral**
We take the last two members of the auxiliary equations:
$$ \frac{dy}{-xy} = \frac{dz}{x(z - 2y)} $$ 
Canceling $x$ from the denominators:
$$ \frac{dy}{-y} = \frac{dz}{z - 2y} $$ 
Rearranging to ==separate differentials==:
$$ (z - 2y) dy = -y dz $$ 
$$ z dy - 2y dy = -y dz $$ 
Rearranging terms to group differentials of products:
$$ y dz + z dy = 2y dy $$ 
Notice that $y dz + z dy$ is the exact differential $d(yz)$.
$$ d(yz) = 2y dy $$ 
Integrating both sides:
$$ \int d(yz) = \int 2y dy $$ 
$$ yz = y^2 + C_2' $$ 
Rearranging for the constant:
$$ y^2 - yz = C_2 \quad \text{..........(3)} $$ 

**Step 5: General Solution**
Using the solutions from (2) and (3):
$$ x^2 + y^2 = f(y^2 - yz) $$ 
**Ans.**

---

### Problem: Solve $xzp + yzq = xy$

**Step 1: Identify Standard Form**
The equation is $xzp + yzq = xy$.
Hre:
*   $P = xz$
*   $Q = yz$
*   $R = xy$

**Step 2: Form Auxiliary Equations**
Lagrange’s subsidiary equations are:
$$ \frac{dx}{xz} = \frac{dy}{yz} = \frac{dz}{xy} \quad \text{..........(1.42)} $$ 

**Step 3: First Integral**
Taking the first two fractions of equation (1.42):
$$ \frac{dx}{xz} = \frac{dy}{yz} $$ 
Canceling $z$ from the denominators:
$$ \frac{dx}{x} = \frac{dy}{y} \quad \text{..........(1.43)} $$ 
Integrating:
$$ \log x = \log y + \log c_1 $$ 
$$ \log x - \log y = \log c_1 $$ 
$$ \frac{x}{y} = c_1 \quad \text{..........(1.44)} $$ 
From this, we can also write $x = c_1 y$.

---

**Step 4: Second Integral**
Taking the second and third fractions of equation (1.42):
$$ \frac{dy}{yz} = \frac{dz}{xy} $$ 
==Substitute== $x = c_1 y$ (from equation 1.44) into the term $xy$:
$$ \frac{dy}{yz} = \frac{dz}{(c_1 y)y} $$ 
$$ \frac{dy}{yz} = \frac{dz}{c_1 y^2} $$ 
Canceling one $y$ from the denominators:
$$ \frac{dy}{z} = \frac{dz}{c_1 y} $$ 
Cross-multiplying:
$$ c_1 y dy = z dz \implies c_1 y dy - z dz = 0 \quad \text{..........(1.45)} $$ 
Integrating:
$$ c_1 \frac{y^2}{2} - \frac{z^2}{2} = \frac{c_2}{2} $$ 
Multiplying by 2:
$$ c_1 y^2 - z^2 = c_2 $$ 
Now, substitute the value of $c_1 = \frac{x}{y}$ back into the equation:
$$ \left(\frac{x}{y}\right) y^2 - z^2 = c_2 $$ 
$$ xy - z^2 = c_2 \quad \text{..........(1.46)} $$ 

**Step 5: General Solution**
Using (1.44) and (1.46), the general solution is:
$$ \phi(xy - z^2, x/y) = 0 $$ 
where $\phi$ is an arbitrary function.

---

### Problem: Solve $z(z^2 + xy)(px - qy) = x^4$
"Solve $z(z^2 + xy)(px - qy) = x^4$", but the solution steps indicate the equation is treated as $xz(z^2 + xy)p - yz(z^2 + xy)q = x^4$. 

**Corrected Standard Form based on Solution:**
$$ P = xz(z^2 + xy), \quad Q = -yz(z^2 + xy), \quad R = x^4 $$ 

**Step 1: Form Auxiliary Equations**
$$ \frac{dx}{xz(z^2 + xy)} = \frac{dy}{-yz(z^2 + xy)} = \frac{dz}{x^4} \quad \text{...(2)} $$ 

**Step 2: First Integral**
Considering the first two fractions, cancel the common term $z(z^2 + xy)$:
$$ \frac{dx}{x} = \frac{dy}{-y} \implies \frac{1}{x}dx = -\frac{1}{y}dy $$ 
Rearranging:
$$ \frac{1}{x}dx + \frac{1}{y}dy = 0 $$ 
Integrating:
$$ \log x + \log y = \log c_1 $$ 
$$ xy = c_1 \quad \text{...(4)} $$ 

**Step 3: Second Integral**
Take the first and third fractions from equation (2):
$$ \frac{dx}{xz(z^2 + xy)} = \frac{dz}{x^4} $$ 
==Substitute== $xy = c_1$ into the denominator term $(z^2 + xy)$:
$$ \frac{dx}{xz(z^2 + c_1)} = \frac{dz}{x^4} $$ 
Rearranging to separate variables $x$ and $z$:
$$ \frac{x^4}{x} dx = z(z^2 + c_1) dz $$ 
$$ x^3 dx = (z^3 + c_1 z) dz $$ 
Rearranging for integration:
$$ x^3 dx - (z^3 + c_1 z) dz = 0 $$ 
Integrating:
$$ \frac{x^4}{4} - \left( \frac{z^4}{4} + \frac{c_1 z^2}{2} \right) = \frac{c_2}{4} $$ 
Multiply by 4:
$$ x^4 - z^4 - 2c_1 z^2 = c_2 $$ 
Substitute $c_1 = xy$ back into the equation:
$$ x^4 - z^4 - 2(xy)z^2 = c_2 \quad \text{...(6)} $$ 

**Step 4: General Solution**
$$ \phi(xy, x^4 - z^4 - 2xyz^2) = 0 $$ 

---

### Theory: Method of Multipliers (Page 14)

Sometimes, solving the auxiliary equations $\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}$ directly by grouping is difficult. In such cases, we use **Lagrange’s Method of Multipliers**.

**Concept:**
We know from algebra that if $\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}$, then for any multipliers $l, m, n$:
$$ \frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R} = \frac{l dx + m dy + n dz}{lP + mQ + nR} $$ 
Here, $l, m, n$ can be constants or functions of $x, y, z$.

**Procedure:**
1.  Choose multipliers $l, m, n$ such that the denominator becomes zero:
    $$ lP + mQ + nR = 0 $$ 
2.  If the denominator is zero, the numerator must also be zero (to maintain the ratio):
    $$ l dx + m dy + n dz = 0 $$ 
3.  Integrate this equation ($ldx + mdy + ndz = 0$) to find the first solution $u = c_1$.
4.  Choose another set of multipliers $(l_1, m_1, n_1)$ to make the denominator zero again, leads to a second differential equation.
5.  Integrate to find the second solution $v = c_2$.
6.  The general solution is $f(u, v) = 0$.

---

### Problem: Solve $(y + zx)p - (x + yz)q = x^2 - y^2$ 🔴

**Step 1: Identify Standard Form**
$$ P = y + zx $$ 
$$ Q = -(x + yz) $$ 
$$ R = x^2 - y^2 $$ 

**Step 2: Auxiliary Equations**
$$ \frac{dx}{y + zx} = \frac{dy}{-(x + yz)} = \frac{dz}{x^2 - y^2} $$ 

**Step 3: Applying First Set of Multipliers**
We choose multipliers $y, x, 1$. Let's check the denominator:
$$ y(P) + x(Q) + 1(R) $$ 
$$ = y(y + zx) + x(-(x + yz)) + 1(x^2 - y^2) $$ 
$$ = y^2 + xyz - x^2 - xyz + x^2 - y^2 $$ 
$$ = 0 $$ 
Since the denominator is zero, the numerator is zero:
$$ y dx + x dy + dz = 0 $$ 

**Step 4: Applying Second Set of Multipliers**
We choose multipliers $x, y, -z$. Let's check the denominator:
$$ x(P) + y(Q) - z(R) $$ 
$$ = x(y + zx) + y(-(x + yz)) - z(x^2 - y^2) $$ 
$$ = xy + zx^2 - xy - y^2z - zx^2 + zy^2 $$ 
$$ = 0 $$ 
Since the denominator is zero, the numerator is zero:
$$ x dx + y dy - z dz = 0 $$ 

**Step 5: Solving the First Integral**
From the first set of multipliers ($y, x, 1$), we found that the numerator must be zero:
$$ y dx + x dy + dz = 0 $$ 
Rearranging the terms:
$$ (y dx + x dy) + dz = 0 $$ 
Recognizing that $y dx + x dy$ is the differential of the product $xy$:
$$ d(xy) + dz = 0 $$ 
Integrating:
$$ xy + z = c_1 \quad \text{[By integrating]} $$ 

**Step 6: Solving the Second Integral**
From the second set of multipliers ($x, y, -z$), we found that the numerator must be zero:
$$ x dx + y dy - z dz = 0 $$ 
Integrating term by term:
$$ \frac{x^2}{2} + \frac{y^2}{2} - \frac{z^2}{2} = \text{constant} $$ 
Multiplying by 2 to clear fractions:
$$ x^2 + y^2 - z^2 = c_2 \quad \text{[By integrating]} $$ 

**Step 7: General Solution**
Combining the two independent solutions found above, the general solution is:
$$ \phi(xy + z, \ x^2 + y^2 - z^2) = 0 $$ 
where $\phi$ is an arbitrary function.

---

### Problem: Solve $x(y^2 - z^2)p + y(z^2 - x^2)q = z(x^2 - y^2)$ 🔴

**Step 1: Form Auxiliary Equations**
$$ \frac{dx}{x(y^2 - z^2)} = \frac{dy}{y(z^2 - x^2)} = \frac{dz}{z(x^2 - y^2)} $$ 

**Step 2: First Set of Multipliers**
We choose multipliers $x, y, z$.
*   **Numerator:** $x dx + y dy + z dz$
*   **Denominator:**
    $$ x[x(y^2 - z^2)] + y[y(z^2 - x^2)] + z[z(x^2 - y^2)] $$ 
    $$ = x^2(y^2 - z^2) + y^2(z^2 - x^2) + z^2(x^2 - y^2) $$ 
    $$ = x^2y^2 - x^2z^2 + y^2z^2 - y^2x^2 + z^2x^2 - z^2y^2 = 0 $$ 
*   **Integration:** Since the denominator is zero, the numerator is zero.
    $$ x dx + y dy + z dz = 0 $$ 
    $$ \implies \frac{x^2}{2} + \frac{y^2}{2} + \frac{z^2}{2} = \text{const} $$ 
    $$ \implies x^2 + y^2 + z^2 = a \quad \text{(By integrating)} $$ 

**Step 3: Second Set of Multipliers**
We choose multipliers $\frac{1}{x}, \frac{1}{y}, \frac{1}{z}$.
*   **Numerator:** $\frac{1}{x} dx + \frac{1}{y} dy + \frac{1}{z} dz$
*   **Denominator:**
    $$ \frac{1}{x}[x(y^2 - z^2)] + \frac{1}{y}[y(z^2 - x^2)] + \frac{1}{z}[z(x^2 - y^2)] $$ 
    $$ = (y^2 - z^2) + (z^2 - x^2) + (x^2 - y^2) = 0 $$ 
*   **Integration:** Since the denominator is zero, the numerator is zero.
    $$ \frac{dx}{x} + \frac{dy}{y} + \frac{dz}{z} = 0 $$ 
    $$ \implies \ln x + \ln y + \ln z = \ln b $$ 
    $$ \implies \ln(xyz) = \ln b $$ 
    $$ \implies xyz = b $$ 

**Step 4: General Solution**
$$ \phi(x^2 + y^2 + z^2, \ xyz) = 0 $$ 

---

### ==Problem==: Find the general solution of $(x^2 - y^2 - z^2)p + 2xyq = 2xz$

**Step 1: Form Auxiliary Equations**
$$ \frac{dx}{x^2 - y^2 - z^2} = \frac{dy}{2xy} = \frac{dz}{2xz} $$ 

**Step 2: Finding First Integral (Simple Grouping)**
Take the 2nd and 3rd ratios:
$$ \frac{dy}{2xy} = \frac{dz}{2xz} $$ 
Cancel $2x$ from the denominators:
$$ \frac{dy}{y} = \frac{dz}{z} $$ 
Integrating:
$$ \ln y = \ln z + \ln c_1 $$ 
$$ \ln y - \ln z = \ln c_1 $$ 
$$ \frac{y}{z} = c_1 \quad \text{[By integrating]} $$

**Step 3: Finding Second Integral (Using Multipliers)**
We need to combine fractions to find a term that relates to the original ratios.
Choose multipliers $x, y, z$.

*   **Numerator:** $x dx + y dy + z dz$
*   **Denominator:**
    $$ x(x^2 - y^2 - z^2) + y(2xy) + z(2xz) $$ 
    $$ = x^3 - xy^2 - xz^2 + 2xy^2 + 2xz^2 $$ 
    $$ = x^3 + xy^2 + xz^2 $$ 
    $$ = x(x^2 + y^2 + z^2) $$ 

Now, create a new ratio equal to the original auxiliary equations:
$$ \frac{x dx + y dy + z dz}{x(x^2 + y^2 + z^2)} $$ 

**Step 4: Equating Ratios**
Set this new ratio equal to the 3rd ratio from the auxiliary equations ($\frac{dz}{2xz}$):
$$ \frac{x dx + y dy + z dz}{x(x^2 + y^2 + z^2)} = \frac{dz}{2xz} $$ 
Cancel $x$ from the denominators on both sides:
$$ \frac{x dx + y dy + z dz}{x^2 + y^2 + z^2} = \frac{dz}{2z} $$ 
Multiply by 2:
$$ \frac{2(x dx + y dy + z dz)}{x^2 + y^2 + z^2} = \frac{dz}{z} $$ 

**Step 5: Integration**
Notice that the numerator on the left, $2x dx + 2y dy + 2z dz$, is exactly the differential of the denominator $d(x^2 + y^2 + z^2)$.
$$ \ln(x^2 + y^2 + z^2) = \ln z + \ln c_2 $$ 
$$ \ln(x^2 + y^2 + z^2) - \ln z = \ln c_2 $$ 
$$ \frac{x^2 + y^2 + z^2}{z} = c_2 $$ 

**Step 6: General Solution**
$$ \phi\left( \frac{y}{z}, \frac{x^2 + y^2 + z^2}{z} \right) = 0 $$ 
where $\phi$ is an arbitrary function.

---

### Problem: Solve $(y + z)p + (z + x)q = x + y$

**Step 1: Auxiliary Equations**
$$ \frac{dx}{y + z} = \frac{dy}{z + x} = \frac{dz}{x + y} \quad \text{...(1)} $$ 

**Step 2: Subtraction Method (First Ratio)**
Choose multipliers $1, -1, 0$.
*   Numerator: $dx - dy$
*   Denominator: $(y + z) - (z + x) = y - x = -(x - y)$
$$ \text{Ratio 1: } \frac{d(x - y)}{-(x - y)} \quad \text{...(2)} $$ 

**Step 3: Subtraction Method (Second Ratio)**
Choose multipliers $0, 1, -1$.
*   Numerator: $dy - dz$
*   Denominator: $(z + x) - (x + y) = z - y = -(y - z)$
$$ \text{Ratio 2: } \frac{d(y - z)}{-(y - z)} \quad \text{...(3)} $$ 

**Step 4: Addition Method (Third Ratio)**
Choose multipliers $1, 1, 1$.      
*   Numerator: $dx + dy + dz$
*   Denominator: $(y + z) + (z + x) + (x + y) = 2x + 2y + 2z = 2(x + y + z)$
$$ \text{Ratio 3: } \frac{d(x + y + z)}{2(x + y + z)} \quad \text{...(4)} $$ 


       What if $1,0,-1$

**Step 5: Solving First Integral**
Equate Ratio 1 and Ratio 2 (from Eq 2 and 3):
$$ \frac{d(x - y)}{-(x - y)} = \frac{d(y - z)}{-(y - z)} $$ 
$$ \frac{d(x - y)}{x - y} = \frac{d(y - z)}{y - z} $$ 
Integrating:
$$ \ln(x - y) = \ln(y - z) + \ln c_1 $$ 
$$ \ln(x - y) - \ln(y - z) = \ln c_1 $$ 

*(Continued on next page)*

---

**Step 5 Continued:**
From the logarithmic relation:
$$ \frac{x - y}{y - z} = c_1 \quad \text{...(6)} $$ 

**Step 6: Solving Second Integral**
Take the first ratio (Eq 2) and the third ratio (Eq 4) from the previous steps:
$$ \frac{d(x - y)}{-(x - y)} = \frac{d(x + y + z)}{2(x + y + z)} $$ 
Rearranging:
$$ 2 \frac{d(x - y)}{x - y} + \frac{d(x + y + z)}{x + y + z} = 0 $$ 
Integrating:
$$ 2 \ln(x - y) + \ln(x + y + z) = \ln c_2 $$ 
Using log properties ($a \ln b = \ln b^a$ and $\ln a + \ln b = \ln ab$):
$$ \ln(x - y)^2 + \ln(x + y + z) = \ln c_2 $$ 
$$ (x - y)^2 (x + y + z) = c_2 \quad \text{...(7)} $$ 

**Step 7: General Solution**
Using (6) and (7), the required general solution is:
$$ \phi\left[ \frac{x - y}{y - z}, \ (x - y)^2(x + y + z) \right] = 0 $$ 
where $\phi$ is an arbitrary function.

Here is the detailed explanation of pages 22 through 27 from the provided document.

### Problem: Solve the PDE: $y^2(x - y)p + x^2(y - x)q = z(x^2 + y^2)$

**Step 1: Form Auxiliary Equations**
Hre $P = y^2(x - y)$, $Q = -x^2(x - y)$ (factoring out minus to match terms), and $R = z(x^2 + y^2)$.
The subsidiary equations are:
$$ \frac{dx}{y^2(x - y)} = \frac{dy}{-x^2(x - y)} = \frac{dz}{z(x^2 + y^2)} \quad \text{...(1)} $$ 

**Step 2: Finding First Integral**
Take the first two fractions of equation (1):
$$ \frac{dx}{y^2(x - y)} = \frac{dy}{-x^2(x - y)} $$ 
Cancel the common term $(x - y)$:
$$ \frac{dx}{y^2} = \frac{dy}{-x^2} $$ 
Cross-multiply:
$$ -x^2 dx = y^2 dy $$ 
$$ x^2 dx + y^2 dy = 0 $$ 
Integrating:
$$ \frac{x^3}{3} + \frac{y^3}{3} = \frac{c_1}{3} $$ 
$$ x^3 + y^3 = c_1 \quad \text{...(2)} $$ 

**Step 3: Finding Second Integral**
We need to form a ratio equivalent to the third fraction $\frac{dz}{z(x^2 + y^2)}$.
Choose multipliers $1, -1, 0$ for the first two fractions.
*   Numerator: $dx - dy$
*   Denominator: $y^2(x - y) - [-x^2(x - y)] = y^2(x - y) + x^2(x - y) = (x - y)(y^2 + x^2)$.
New Ratio:
$$ \frac{dx - dy}{(x - y)(x^2 + y^2)} \quad \text{...(3)} $$ 

Combine this new ratio with the third fraction of (1):
$$ \frac{dx - dy}{(x - y)(x^2 + y^2)} = \frac{dz}{z(x^2 + y^2)} $$ 
Cancel $(x^2 + y^2)$ from the denominators:
$$ \frac{dx - dy}{x - y} = \frac{dz}{z} $$ 
$$ \frac{d(x - y)}{x - y} - \frac{dz}{z} = 0 $$ 
Integrating:
$$ \log(x - y) - \log z = \log c_2 $$ 
$$ \frac{x - y}{z} = c_2 \quad \text{...(4)} $$ 

**Step 4: General Solution**
Using (2) and (4):
$$ \phi\left( x^3 + y^3, \frac{x - y}{z} \right) = 0 $$ 
where $\phi$ is an arbitrary function.

---

### Problem: Solve $(x^2 - yz)p + (y^2 - zx)q = (z^2 - xy)$ 🔴

**Step 1: Auxiliary Equations**
$$ \frac{dx}{x^2 - yz} = \frac{dy}{y^2 - zx} = \frac{dz}{z^2 - xy} $$ 

**Step 2: Using Multipliers for Subtraction**
This system is symmetric. We use subtraction to find integrable combinations.
*   **First two terms:** Choose multipliers $1, -1, 0$.
    $$ \frac{dx - dy}{(x^2 - yz) - (y^2 - zx)} = \frac{dx - dy}{(x^2 - y^2) + z(x - y)} = \frac{dx - dy}{(x - y)(x + y + z)} $$ 
    $$ \text{Ratio 1} = \frac{dx - dy}{(x - y)(x + y + z)} $$ 

*   **Last two terms:** Choose multipliers $0, 1, -1$.
    $$ \frac{dy - dz}{(y^2 - zx) - (z^2 - xy)} = \frac{dy - dz}{(y^2 - z^2) + x(y - z)} = \frac{dy - dz}{(y - z)(y + z + x)} $$ 
    $$ \text{Ratio 2} = \frac{dy - dz}{(y - z)(x + y + z)} $$ 

*   **First and last terms:** Choose multipliers $1, 0, -1$ (implied for symmetry).
    $$ \text{Ratio 3} = \frac{dz - dx}{(z - x)(x + y + z)} $$ 

**Step 3: Solving Integrals**
*   **Equate Ratio 1 and Ratio 2:**
    $$ \frac{dx - dy}{(x - y)(x + y + z)} = \frac{dy - dz}{(y - z)(x + y + z)} $$ 
    Cancel $(x + y + z)$:
    $$ \frac{d(x - y)}{x - y} = \frac{d(y - z)}{y - z} $$ 
    Integrate:
    $$ \log(x - y) = \log(y - z) + \log a \implies \frac{x - y}{y - z} = a $$ 

*   **Equate Ratio 2 and Ratio 3:**
    $$ \frac{dy - dz}{y - z} = \frac{dz - dx}{z - x} $$ 
    Integrate:
    $$ \log(y - z) = \log(z - x) + \log b \implies \frac{y - z}{z - x} = b $$ 

**Step 4: General Solution**
$$ \phi\left( \frac{x - y}{y - z}, \frac{y - z}{z - x} \right) = 0 $$ 

---

### Problem: Find the equation of surfaces satisfying $4yzp + q + 2y = 0$ and passing through the curves $y^2 + z^2 = 1$ and $x + z = 2$. 🔴

**Step 1: Identify Standard Form**
Rewrite as $4yzp + 1q = -2y$.
$$ P = 4yz, \quad Q = 1, \quad R = -2y $$ 

**Step 2: Auxiliary Equations**
$$ \frac{dx}{4yz} = \frac{dy}{1} = \frac{dz}{-2y} $$ 

**Step 3: Finding First Integral**
Take the 1st and 3rd terms:
$$ \frac{dx}{4yz} = \frac{dz}{-2y} $$ 
Cancel $2y$ from denominators:
$$ \frac{dx}{2z} = \frac{dz}{-1} $$ 
$$ -dx = 2z dz \implies dx + 2z dz = 0 $$ 
Integrate:
$$ x + z^2 = a \quad \text{[By integrating]} \quad \text{...(2)} $$ 

*(Solution continues on next page)*

---

**Step 4: Finding Second Integral**
Take the 2nd and 3rd terms from the auxiliary equations:
$$ \frac{dy}{1} = \frac{dz}{-2y} $$ 
$$ -2y dy = dz \implies 2y dy + dz = 0 $$ 
Integrate:
$$ y^2 + z = b \quad \text{[By integrating]} \quad \text{...(3)} $$ 

**Step 5: Applying the Curve Condition**
We have two relations involving constants $a$ and $b$:
1.  $x + z^2 = a$
2.  $y^2 + z = b$
Adding equation (2) and (3):
$$ x + z^2 + y^2 + z = a + b \quad \text{...(4)} $$ 

The surface passes through $y^2 + z^2 = 1$ and $x + z = 2$.
Substitute these values into (4):
$$ (x + z) + (y^2 + z^2) = a + b $$ 
$$ 2 + 1 = a + b $$ 
$$ 3 = a + b $$ 

**Step 6: Final Equation**
Substitute $a$ and $b$ back into the relation $a + b = 3$:
$$ (x + z^2) + (y^2 + z) = 3 $$ 
$$ x + z + y^2 + z^2 = 3 $$ 
This is the required integral surface.

---

### Problem: Find the integral surface of the PDE: $x(y^2 + z)p - y(x^2 + z)q = (x^2 - y^2)z$
**which contains the line $x + y = 0, z = 1$.**

**Step 1: Auxiliary Equations**
$$ \frac{dx}{x(y^2 + z)} = \frac{dy}{-y(x^2 + z)} = \frac{dz}{(x^2 - y^2)z} $$ 

**Step 2: Finding First Integral**
Choose multipliers $x, y, -1$.
*   Numerator: $x dx + y dy - dz$
*   Denominator:
    $$ x[x(y^2 + z)] + y[-y(x^2 + z)] - 1[(x^2 - y^2)z] $$ 
    $$ = x^2y^2 + x^2z - y^2x^2 - y^2z - x^2z + y^2z = 0 $$ 

Since the denominator is zero, equate the numerator to zero:
$$ x dx + y dy - dz = 0 $$ 
Integrate:
$$ \frac{x^2}{2} + \frac{y^2}{2} - z = \frac{c_1}{2} $$ 
$$ x^2 + y^2 - 2z = c_1 \quad \text{..........(i) [By integrating]} $$ 

*(Solution continues on next page)*

---

**Step 3: Finding Second Integral**
Choose multipliers $\frac{1}{x}, \frac{1}{y}, \frac{1}{z}$.
*   Numerator: $\frac{dx}{x} + \frac{dy}{y} + \frac{dz}{z}$
*   Denominator:
    $$ \frac{1}{x}[x(y^2 + z)] + \frac{1}{y}[-y(x^2 + z)] + \frac{1}{z}[(x^2 - y^2)z] $$ 
    $$ = (y^2 + z) - (x^2 + z) + (x^2 - y^2) $$ 
    $$ = y^2 + z - x^2 - z + x^2 - y^2 = 0 $$ 

Since the denominator is zero, equate the numerator to zero:
$$ \frac{dx}{x} + \frac{dy}{y} + \frac{dz}{z} = 0 $$ 
Integrate:
$$ \log x + \log y + \log z = \log c_2 $$ 
$$ xyz = c_2 \quad \text{..........(ii)} $$ 

**Step 4: Applying the Line Condition**
The surface passes through the line given by $x + y = 0$ (so $y = -x$) and $z = 1$.

*   Substitute these into (ii):
    $$ x(y)(z) = c_2 \implies x(-x)(1) = c_2 \implies -x^2 = c_2 \implies x^2 = -c_2 $$ 

*   Substitute these into (i):
    $$ x^2 + y^2 - 2z = c_1 \implies x^2 + (-x)^2 - 2(1) = c_1 $$ 
    $$ 2x^2 - 2 = c_1 $$ 

**Step 5: Forming the Final Relation**
Substitute $x^2 = -c_2$ into the equation for $c_1$:
$$ 2(-c_2) - 2 = c_1 $$ 
$$ -2c_2 - 2 = c_1 $$ 
$$ c_1 + 2c_2 + 2 = 0 $$ 

**Step 6: Final Equation**
Substitute $c_1$ and $c_2$ back into the relation:
$$ (x^2 + y^2 - 2z) + 2(xyz) + 2 = 0 $$ 
$$ x^2 + y^2 - 2z + 2xyz + 2 = 0 $$ 
This is the required integral surface.

Here is the detailed explanation of the remaining pages (28 through 31) from the provided document.

### Problem: Find the integral surface of the PDE: $(x - y)y^2p + (y - x)x^2q = (x^2 + y^2)z$ 🔴
which passes through the curve defined by $xz = a^3$ and $y = 0$.

**Step 1: Form Auxiliary Equations**
Identify the coefficients $P, Q, R$:
*   $P = (x - y)y^2$
*   $Q = (y - x)x^2 = -(x - y)x^2$
*   $R = (x^2 + y^2)z$

The auxiliary equations are:
$$ \frac{dx}{(x - y)y^2} = \frac{dy}{-(x - y)x^2} = \frac{dz}{(x^2 + y^2)z} $$ 

**Step 2: Finding First Integral**
Take the 1st and 2nd ratios:
$$ \frac{dx}{(x - y)y^2} = \frac{dy}{-(x - y)x^2} $$ 
Cancel the common factor $(x - y)$ (assuming $x \neq y$):
$$ \frac{dx}{y^2} = \frac{dy}{-x^2} $$ 
Cross-multiply to separate variables:
$$ -x^2 dx = y^2 dy $$ 
$$ x^2 dx + y^2 dy = 0 $$ 
Integrate:
$$ \frac{x^3}{3} + \frac{y^3}{3} = C $$ 
Multiply by 3:
$$ x^3 + y^3 = c_1 \quad \text{..........(i) [By integrating]} $$ 

---

**Step 3: Finding Second Integral**
We need to combine fractions to match the denominator of the 3rd ratio $(x^2 + y^2)z$.
Choose multipliers $1, -1, 0$ for the ratios.
*   **Numerator:** $dx - dy$
*   **Denominator:**
    $$ (x - y)y^2 - [-(x - y)x^2] $$ 
    $$ = (x - y)y^2 + (x - y)x^2 $$ 
    $$ = (x - y)(y^2 + x^2) $$ 

Now equate this new fraction with the 3rd ratio from the auxiliary equations:
$$ \frac{dx - dy}{(x - y)(x^2 + y^2)} = \frac{dz}{(x^2 + y^2)z} $$ 

Cancel $(x^2 + y^2)$ from the denominators:
$$ \frac{dx - dy}{x - y} = \frac{dz}{z} $$ 
$$ \frac{d(x - y)}{x - y} = \frac{dz}{z} $$ 

Integrate:
$$ \log(x - y) = \log z + \log A $$ 
Rearrange logarithmic terms (Note: The slide rearranges it as $\log z - \log(x - y) = \log c_2$):
$$ \log z = \log(x - y) + \log c_2 $$ 
$$ \log \frac{z}{x - y} = \log c_2 $$ 
$$ \frac{z}{x - y} = c_2 \quad \text{..........(ii)} $$ 

**Step 4: Applying Boundary Conditions**
The surface passes through $xz = a^3$ and $y = 0$.
We substitute $y = 0$ into our integral equations (i) and (ii).

*   From (i), substitute $y = 0$:
    $$ x^3 + 0^3 = c_1 \implies x^3 = c_1 $$ 

*   From (ii), substitute $y = 0$:
    $$ \frac{z}{x - 0} = c_2 \implies z = c_2x $$ 

Now substitute this expression for $z$ into the given curve equation $xz = a^3$:
$$ x(c_2x) = a^3 $$ 
$$ c_2x^2 = a^3 \implies \frac{a^3}{x^2} = c_2 $$ 

---

**Step 5: Eliminate the Parameter $x$**
We have two relations involving the parameter $x$:
1.  $c_1 = x^3 \implies c_1^2 = x^6$
2.  $c_2 = \frac{a^3}{x^2} \implies c_2^3 = \frac{a^9}{x^6}$

Multiply $c_1^2$ by $c_2^3$ to eliminate $x^6$:
$$ c_1^2 c_2^3 = (x^6) \cdot \left( \frac{a^9}{x^6} \right) $$ 
$$ c_1^2 c_2^3 = a^9 $$ 

**Step 6: Final Integral Surface**
Substitute the original expressions for $c_1$ and $c_2$ back into this relation:
*   $c_1 = x^3 + y^3$
*   $c_2 = \frac{z}{x - y}$

Equation becomes:
$$ (x^3 + y^3)^2 \left( \frac{z}{x - y} \right)^3 = a^9 $$ 

Rearranging to clear the denominator:
$$ z^3 (x^3 + y^3)^2 = a^9 (x - y)^3 $$ 
This is the required integral surface.

---

## Homework Examples (Page 31)

This page lists practice problems. The general method for all is Lagrange's method ($dx/P = dy/Q = dz/R$).

### Problem: $y^2zp - x^2zq = x^2y$
*   **Hints:** Take 1st and 2nd ratio; then take 2nd and 3rd ratio.
*   **Ans:** $\phi(x^3 + y^3, y^2 + z^2) = 0$

### Problem: $(x^2 - yz)p + (y^2 - zx)q = z^2 - xy$
*   *(No answer listed on this specific line, but this is a standard symmetric cyclic problem typically solved with multipliers 1,-1,0 etc., yielding ratios like $(x-y)/(y-z)$ and sum multipliers).*

### Problem: $(y - z)p + (x - y)q = z - x$
*   **Hints:** Use multipliers $1, 1, 1$ (sum is 0) and $x, z, y$ (sum is 0).
*   **Ans:** $\phi(x + y + z, x^2 + 2yz) = 0$

### Problem: $x(2y^4 - z^4)p + y(z^4 - 2x^4)q = z(x^4 - y^4)$
*   **Hints:** Use $x^3, y^3, z^3$ as multipliers and $x, y, z/2$ as dividers (likely meaning modifying the denominators to find integrable combinations).
*   **Ans:** $\phi(x^4 + y^4 + z^4, xyz^2) = 0$

### Problem: Solve $x(z^2 - y^2)p + y(x^2 - z^2)q = z(y^2 - x^2)$ 🔴

**Step 1: Form Auxiliary Equations**
Hre $P = x(z^2 - y^2)$, $Q = y(x^2 - z^2)$, $R = z(y^2 - x^2)$.
$$ \frac{dx}{x(z^2 - y^2)} = \frac{dy}{y(x^2 - z^2)} = \frac{dz}{z(y^2 - x^2)} $$ 

**Step 2: First Set of Multipliers**
Choose multipliers $x, y, z$.
*   **Numerator:** $x dx + y dy + z dz$
*   **Denominator:**
    $$ x[x(z^2 - y^2)] + y[y(x^2 - z^2)] + z[z(y^2 - x^2)] $$ 
    $$ = x^2z^2 - x^2y^2 + y^2x^2 - y^2z^2 + z^2y^2 - z^2x^2 = 0 $$ 
*   **Integration:** Since the denominator is zero, the numerator is zero.
    $$ x dx + y dy + z dz = 0 $$ 
    $$ \frac{x^2}{2} + \frac{y^2}{2} + \frac{z^2}{2} = \text{const} $$ 
    $$ x^2 + y^2 + z^2 = c_1 \quad \text{..........(i)} $$ 

**Step 3: Second Set of Multipliers**
Choose multipliers $\frac{1}{x}, \frac{1}{y}, \frac{1}{z}$.
*   **Numerator:** $\frac{dx}{x} + \frac{dy}{y} + \frac{dz}{z}$
*   **Denominator:**
    $$ \frac{1}{x}[x(z^2 - y^2)] + \frac{1}{y}[y(x^2 - z^2)] + \frac{1}{z}[z(y^2 - x^2)] $$ 
    $$ = (z^2 - y^2) + (x^2 - z^2) + (y^2 - x^2) = 0 $$ 
*   **Integration:** Since the denominator is zero, the numerator is zero.
    $$ \frac{dx}{x} + \frac{dy}{y} + \frac{dz}{z} = 0 $$ 
    $$ \ln x + \ln y + \ln z = \ln c_2 $$ 
    $$ \ln(xyz) = \ln c_2 $$ 
    $$ xyz = c_2 \quad \text{..........(ii)} $$ 

**Step 4: General Solution**
Using (i) and (ii):
$$ \phi(x^2 + y^2 + z^2, xyz) = 0 $$ 
where $\phi$ is an arbitrary function.

**N.B.:** For more, follow **Ordinary and Partial Differential Equations** book (**M.D. Raisinghania**).

---

## Technique: Choosing Multipliers for Lagrange's Method

The core idea of **Lagrange's Method of Multipliers** is to find a set of multipliers $(l, m, n)$ such that when you form the fraction:
$$ \frac{l dx + m dy + n dz}{lP + mQ + nR} $$ 
one of two things happens:

1.  **The Denominator becomes Zero:**
    If $lP + mQ + nR = 0$, then it implies the numerator $l dx + m dy + n dz = 0$.
    *   This resulting differential equation is then integrated to find a solution (e.g., $lx + my + nz = c$).
    *   **Common patterns:** $(x, y, z)$, $(1/x, 1/y, 1/z)$, $(1, -1, 0)$, $(1, 1, 1)$.

2.  **Exact Differential:**
    The numerator $l dx + m dy + n dz$ becomes the exact differential of the denominator (or a function of it).
    *   For example, if the fraction equals $\frac{d(\text{something})}{\text{something}}$, you can equate it to another ratio like $\frac{dz}{z}$ and integrate logarithmically.

### Summary of Problems and Multipliers

Hre is a quick reference table of the problems discussed in this document and the specific multipliers or techniques used to solve them.

| Problem Equation                                   | Multipliers / Technique Used                                                      |     |
| :------------------------------------------------- | :-------------------------------------------------------------------------------- | --- |
| **$yq - xp = z$**                                  | **Grouping:** $(1, 2)$ & $(2, 3)$. No complex multipliers.                        |     |
| **$y^2p - xyq = x(z - 2y)$**                       | **Grouping:** $(1, 2)$ & $(2, 3)$.                                                |     |
| **$xzp + yzq = xy$**                               | **Grouping:** $(1, 2)$ & $(2, 3)$ (with subst).                                   |     |
| **$z(z^2 + xy)(px - qy) = x^4$**                   | **Grouping:** $(1, 2)$ & $(1, 3)$ (with subst).                                   |     |
| **$(y + zx)p - (x + yz)q = x^2 - y^2$**            | **==Set 1==:** $(y, x, 1)$ <br> **Set 2:** $(x, y, -z)$                           |     |
| **$x(y^2 - z^2)p + y(z^2 - x^2)q = z(x^2 - y^2)$** | **Set 1:** $(x, y, z)$ <br> **Set 2:** $(1/x, 1/y, 1/z)$                          |     |
| **$(x^2 - y^2 - z^2)p + 2xyq = 2xz$**              | **Set 1:** Grouping $(2, 3)$ <br> **Set 2:** $(x, y, z)$ combined with ratio 3.   |     |
| **$(y + z)p + (z + x)q = x + y$**                  | **Set 1:** $(1, -1, 0)$ <br> **Set 2:** $(0, 1, -1)$ <br> **Set 3:** $(1, 1, 1)$  |     |
| **$y^2(x - y)p + x^2(y - x)q = z(x^2 + y^2)$**     | **Set 1:** Grouping $(1, 2)$ <br> **Set 2:** $(1, -1, 0)$ combined with ratio 3.  |     |
| **$(x^2 - yz)p + (y^2 - zx)q = z^2 - xy$**         | **Set 1:** $(1, -1, 0)$ <br> **Set 2:** $(0, 1, -1)$ <br> **Set 3:** $(1, 0, -1)$ |     |
| **$4yzp + q = -2y$**                               | **Grouping:** $(1, 3)$ & $(2, 3)$.                                                |     |
| **$x(y^2 + z)p - y(x^2 + z)q = (x^2 - y^2)z$**     | **==Set 1:==** $(x, y, -1)$ <br> **Set 2:** $(1/x, 1/y, 1/z)$                     |     |
| **$(x - y)y^2p + (y - x)x^2q = (x^2 + y^2)z$**     | **Set 1:** Grouping $(1, 2)$ <br> **Set 2:** $(1, -1, 0)$ combined with ratio 3.  |     |
