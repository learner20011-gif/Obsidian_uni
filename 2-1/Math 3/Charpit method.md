Here is the detailed explanation of pages 4 through 9 from the provided document, covering Charpit's Method and its application to specific problems.

### Theory: Introduction to Charpit’s Method (Page 4)

**Definition**
Charpit's method is a general technique used to find the **complete integral** (solution) of first-order **nonlinear** partial differential equations (PDEs). These equations are typically of the form:
$$ f(x, y, z, p, q) = 0 $$
where $p = \frac{\partial z}{\partial x}$ and $q = \frac{\partial z}{\partial y}$.

**Theorem (Charpit’s Auxiliary Equations)**
If $F(x, y, z, p, q) = 0$ is a nonlinear PDE, determining the solution requires finding a second relation between $p$ and $q$. This is done using **Charpit’s Auxiliary Equations**:

$$ \frac{dp}{\frac{\partial F}{\partial x} + p\frac{\partial F}{\partial z}} = \frac{dq}{\frac{\partial F}{\partial y} + q\frac{\partial F}{\partial z}} = \frac{dz}{-p\frac{\partial F}{\partial p} - q\frac{\partial F}{\partial q}} = \frac{dx}{-\frac{\partial F}{\partial p}} = \frac{dy}{-\frac{\partial F}{\partial q}} $$

**The Complete Integral**
Once values for $p$ and $q$ are found using the auxiliary equations and the original equation, the solution is found by integrating the total differential equation:
$$ dz = p dx + q dy $$

---

### Theory: Working Rule for Charpit’s Method (Page 5)

To solve a problem practically, the following step-by-step procedure is used:

*   **STEP 1: Standardization**
    Transfer all terms to the Left Hand Side (L.H.S.) so that the equation equals zero. Denote this expression by $f$.
    $$ f(x, y, z, p, q) = 0 $$

*   **STEP 2: Setup**
    Write down the standard form of Charpit's auxiliary equations (as shown in Page 4).

*   **STEP 3: Differentiation**
    Calculate the partial derivatives of $f$ with respect to $x, y, z, p,$ and $q$ (i.e., $\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}, \frac{\partial f}{\partial p}, \frac{\partial f}{\partial q}$). Substitute these values into the auxiliary equations.

*   **STEP 4: Finding a Relation**
    Select two proper fractions from the auxiliary equations that allow for the simplest integration. The goal is to find a relation involving at least one of $p$ or $q$ (e.g., finding $p$ in terms of $q$, or $p$ as a constant).

*   **STEP 5: Final Solution**
    1.  Solve the relation from Step 4 together with the original equation to find specific values for $p$ and $q$.
    2.  Substitute these $p$ and $q$ values into the equation $dz = p dx + q dy$.
    3.  Integrate this equation to obtain the complete integral (solution).

---

### Question: Using Charpit’s method, solve: $$ z = px + qy + pq $$

**Using Charpit’s method, solve:**
$$ z = px + qy + pq $$


**Step 1: Define F**
Bring all terms to one side:
$$ f = z - px - qy - pq = 0 \quad \text{..........(2)} $$

**Step 2 & 3: Differentiate and Substitute**
Calculate partial derivatives of $f$:
*   $\frac{\partial f}{\partial x} = -p$
*   $\frac{\partial f}{\partial y} = -q$
*   $\frac{\partial f}{\partial z} = 1$
*   $\frac{\partial f}{\partial p} = -x - q$
*   $\frac{\partial f}{\partial q} = -y - p$

Substitute these into Charpit’s auxiliary equations:
$$ \frac{dp}{\frac{\partial f}{\partial x} + p\frac{\partial f}{\partial z}} = \frac{dq}{\frac{\partial f}{\partial y} + q\frac{\partial f}{\partial z}} = \frac{dx}{-\frac{\partial f}{\partial p}} = \frac{dy}{-\frac{\partial f}{\partial q}} $$

$$ \frac{dp}{-p + p(1)} = \frac{dq}{-q + q(1)} = \frac{dx}{x+q} = \frac{dy}{y+p} $$

$$ \frac{dp}{0} = \frac{dq}{0} = \frac{dx}{x+q} = \frac{dy}{y+p} \quad \text{..........(3)} $$

**Step 4: Solve for p and q**
From the first two terms, we get:
$$ dp = 0 \implies p = a \quad (\text{constant}) $$
$$ dq = 0 \implies q = b \quad (\text{constant}) $$

---


**Step 5: Final Integral**
We have found $p = a$ and $q = b$.
Substitute these values back into the original equation (Eq. 1):
$$ z = px + qy + pq $$
$$ z = ax + by + ab $$

**Result:**
This is the required complete integral.

---

### Question: Using Charpit’s method, solve: $$ px + qy = pq $$

**Using Charpit’s method, solve:**
$$ px + qy = pq $$


**Step 1: Define F**
$$ f = px + qy - pq = 0 \quad \text{..........(1)} $$

**Step 2 & 3: Differentiate and Substitute**
Calculate partial derivatives:
*   $\frac{\partial f}{\partial x} = p$
*   $\frac{\partial f}{\partial y} = q$
*   $\frac{\partial f}{\partial z} = 0$
*   $\frac{\partial f}{\partial p} = x - q$
*   $\frac{\partial f}{\partial q} = y - p$

Substitute into auxiliary equations:
$$ \frac{dp}{p + p(0)} = \frac{dq}{q + q(0)} = \frac{dx}{-(x-q)} = \frac{dy}{-(y-p)} $$

$$ \frac{dp}{p} = \frac{dq}{q} = \frac{dx}{-x+q} = \frac{dy}{-y+p} \quad \text{..........(2)} $$

**Step 4: Finding a Relation**
Take the first two terms:
$$ \frac{dp}{p} = \frac{dq}{q} $$

---


**Step 5: Integration and Substitution**
Integrating $\frac{dp}{p} = \frac{dq}{q}$:
$$ \ln p = \ln q + \ln a $$
$$ \ln p = \ln (qa) $$
$$ p = aq $$

Now, we solve for $p$ and $q$ using this relation and the original equation ($px + qy - pq = 0$).
Substitute $p = aq$ into the original equation:
$$ (aq)x + qy - (aq)q = 0 $$
$$ q(ax + y - aq) = 0 $$
Since $q \neq 0$:
$$ ax + y - aq = 0 \implies aq = y + ax \implies q = \frac{y + ax}{a} $$

Find $p$:
$$ p = aq = a \left(\frac{y + ax}{a}\right) = y + ax $$

**Step 6: Final Integration**
Substitute $p$ and $q$ into $dz = p dx + q dy$:
$$ dz = (y + ax)dx + \left(\frac{y + ax}{a}\right)dy $$
Multiply by $a$ to simplify:
$$ a dz = a(y + ax)dx + (y + ax)dy $$
$$ a dz = (y + ax)(a dx + dy) $$
Notice that $d(y + ax) = dy + a dx$. Thus:
$$ a dz = (y + ax) d(y + ax) $$

Integrate both sides:
$$ az = \frac{(y + ax)^2}{2} + b $$
$$ az = \frac{1}{2}(y + ax)^2 + b $$

**Result:**
This is the required complete integral.

---

### Question: Solve using Charpit’s method: $$ z^2(p^2 z^2 + q^2) = 1 $$

**Solve using Charpit’s method:**
$$ z^2(p^2 z^2 + q^2) = 1 $$


**Step 1: Define F**
Rearrange the equation:
$$ z^2 p^2 z^2 + z^2 q^2 = 1 $$
$$ p^2 z^4 + q^2 z^2 - 1 = 0 $$
$$ F(x, y, z, p, q) = p^2 z^4 + q^2 z^2 - 1 = 0 \quad \text{..........(i)} $$

**Step 2 & 3: Auxiliary Equations**
Calculate derivatives:
*   $\frac{\partial F}{\partial x} = 0$
*   $\frac{\partial F}{\partial y} = 0$
*   $\frac{\partial F}{\partial z} = 4p^2 z^3 + 2q^2 z$
*   $\frac{\partial F}{\partial p} = 2p z^4$
*   $\frac{\partial F}{\partial q} = 2q z^2$

Substitute into the auxiliary equations:
$$ \frac{dp}{0 + p(4p^2 z^3 + 2q^2 z)} = \frac{dq}{0 + q(4p^2 z^3 + 2q^2 z)} = \frac{dz}{-p(2pz^4) - q(2qz^2)} $$

$$ \frac{dp}{p(4p^2 z^3 + 2q^2 z)} = \frac{dq}{q(4p^2 z^3 + 2q^2 z)} $$

**Step 4: Finding a Relation**
From the 1st and 2nd ratios, the denominators are identical (multiples of the term in the bracket).
$$ \frac{dp}{p} = \frac{dq}{q} $$

Integrating:
$$ \ln p = \ln q + \ln c $$
$$ p = qc \quad \text{..........(ii)} $$

*(Note: The solution continues on the next page of the document using this relation to find the complete integral).* 

Here is the detailed explanation of pages 10 through 15 from the provided document.


This section continues the solution for $z^2(p^2z^2 + q^2) = 1$ from Page 9.

**Step 5: Solve for p and q**
We established the relation $p = qc$. Substitute this into the rearranged original equation $p^2 z^4 + q^2 z^2 - 1 = 0$:
$$ (qc)^2 z^4 + q^2 z^2 - 1 = 0 $$
$$ q^2 c^2 z^4 + q^2 z^2 = 1 $$
Factor out $q^2$:
$$ q^2 (c^2 z^4 + z^2) = 1 $$
Solve for $q$:
$$ q^2 = \frac{1}{z^2(c^2 z^2 + 1)} $$
$$ q = \frac{1}{z\sqrt{c^2 z^2 + 1}} $$

Now find $p$ using $p = qc$:
$$ p = c \left( \frac{1}{z\sqrt{c^2 z^2 + 1}} \right) = \frac{c}{z\sqrt{c^2 z^2 + 1}} $$

**Step 6: Integrate for Complete Solution**
Substitute $p$ and $q$ into $dz = p dx + q dy$:
$$ dz = \left( \frac{c}{z\sqrt{c^2 z^2 + 1}} \right) dx + \left( \frac{1}{z\sqrt{c^2 z^2 + 1}} \right) dy $$
Multiply by the denominator term $z\sqrt{c^2 z^2 + 1}$:
$$ z\sqrt{c^2 z^2 + 1} dz = c dx + dy $$
Integrate both sides:
$$ \int z\sqrt{c^2 z^2 + 1} dz = \int c dx + \int 1 dy $$

To integrate the LHS, let $u = c^2 z^2 + 1$, then $du = 2c^2 z dz$, so $z dz = \frac{du}{2c^2}$.
$$ \int \sqrt{u} \frac{du}{2c^2} = \frac{1}{2c^2} \frac{u^{3/2}}{3/2} = \frac{1}{3c^2} (c^2 z^2 + 1)^{3/2} $$

Thus, the equation becomes:
$$ \frac{1}{3c^2} (c^2 z^2 + 1)^{3/2} = cx + y + k \quad \text{[where k is integration constant]} $$

**Result:**
This is the required complete solution.

---

### Question: Find the complete integral of the given partial differential equation by Charpit’s method: $$ p^2 - y^2q = y^2 - x^2 $$

**Find the complete integral of the given partial differential equation by Charpit’s method:**
$$ p^2 - y^2q = y^2 - x^2 $$


**Step 1: Define F**
$$ F(x, y, z, p, q) = p^2 - y^2q - y^2 + x^2 = 0 \quad \text{..........(i)} $$

**Step 2 & 3: Auxiliary Equations**
Calculate derivatives:
*   $\frac{\partial F}{\partial x} = 2x$
*   $\frac{\partial F}{\partial z} = 0$
*   $\frac{\partial F}{\partial p} = 2p$
*   $\frac{\partial F}{\partial y} = -2yq - 2y$
*   $\frac{\partial F}{\partial q} = -y^2$

Substitute into auxiliary equations:
$$ \frac{dp}{2x + p(0)} = \frac{dq}{(-2yq - 2y) + q(0)} = \frac{dz}{-p(2p) - q(-y^2)} = \frac{dx}{-2p} = \frac{dy}{-(-y^2)} $$

$$ \frac{dp}{2x} = \frac{dq}{-2yq - 2y} = \frac{dz}{-2p^2 + y^2q} = \frac{dx}{-2p} = \frac{dy}{y^2} $$

**Step 4: Finding a Relation**
Take the 1st and 4th ratios:
$$ \frac{dp}{2x} = \frac{dx}{-2p} $$
Cross-multiply:
$$ -2p dp = 2x dx $$
$$ p dp + x dx = 0 $$
Integrate:
$$ \frac{p^2}{2} + \frac{x^2}{2} = \frac{c_1}{2} $$
$$ p^2 + x^2 = c_1 \quad \text{..........(ii)} $$

---


**Step 5: Solve for p and q**
From (ii), we have $p^2 = c_1 - x^2$, so:
$$ p = \sqrt{c_1 - x^2} $$

Substitute $p^2 = c_1 - x^2$ into the original equation $p^2 - y^2q = y^2 - x^2$:
$$ (c_1 - x^2) - y^2q = y^2 - x^2 $$
Rearrange to solve for $q$:
$$ c_1 - x^2 - y^2 + x^2 = y^2q $$
$$ c_1 - y^2 = y^2q $$
$$ q = \frac{c_1 - y^2}{y^2} = \frac{c_1}{y^2} - 1 $$

**Step 6: Integrate for Complete Integral**
$$ dz = p dx + q dy $$
$$ dz = \sqrt{c_1 - x^2} dx + \left(\frac{c_1}{y^2} - 1\right) dy $$
Integrate both sides:
$$ \int dz = \int \sqrt{c_1 - x^2} dx + \int \left(c_1 y^{-2} - 1\right) dy $$

*   The $x$-integral is a standard form $\int \sqrt{a^2 - x^2} dx = \frac{x}{2}\sqrt{a^2-x^2} + \frac{a^2}{2}\sin^{-1}(\frac{x}{a})$. Here $a^2 = c_1$.
    $$ \int \sqrt{c_1 - x^2} dx = \frac{x}{2}\sqrt{c_1 - x^2} + \frac{c_1}{2}\sin^{-1}\left(\frac{x}{\sqrt{c_1}}\right) $$
*   The $y$-integral:
    $$ \int (c_1 y^{-2} - 1) dy = -\frac{c_1}{y} - y $$

Combine results:
$$ z = \frac{\sqrt{c_1 - x^2}}{2c_1} + \frac{c_1}{2}\sin^{-1}\left(\frac{x}{\sqrt{c_1}}\right) - \frac{c_1}{y} - y + k $$
*(Note: There appears to be a typo in the slide's final line fraction $ \frac{\sqrt{c_1-x^2}}{2c_1}$, it should likely be $ \frac{x\sqrt{c_1-x^2}}{2} $ based on standard integration formulas).*

**Result:**
This is the required complete integral.

---

### Question: Using Charpit’s method solve: $$ 2xz - px^2 - 2qxy + pq = 0 $$

**Using Charpit’s method solve:**
$$ 2xz - px^2 - 2qxy + pq = 0 $$


**Step 1: Define F**
$$ f = 2xz - px^2 - 2qxy + pq = 0 \quad \text{..........(1)} $$

**Step 2 & 3: Auxiliary Equations**
Calculate derivatives:
*   $\frac{\partial f}{\partial x} = 2z - 2px - 2qy$
*   $\frac{\partial f}{\partial y} = -2qx$
*   $\frac{\partial f}{\partial z} = 2x$
*   $\frac{\partial f}{\partial p} = -x^2 + q$
*   $\frac{\partial f}{\partial q} = -2xy + p$

Substitute into auxiliary equations (focusing on $dp$ and $dq$):
$$ \frac{dp}{(2z - 2px - 2qy) + p(2x)} = \frac{dq}{(-2qx) + q(2x)} $$

$$ \frac{dp}{2z - 2qy} = \frac{dq}{0} $$

**Step 4: Finding a Relation**
From the second term, we get:
$$ dq = 0 $$
Integrating:
$$ q = a \quad [\text{constant}] $$

---


**Step 5: Solve for p**
Substitute $q = a$ into the original equation (1):
$$ 2xz - px^2 - 2axy + ap = 0 $$
Group terms with $p$:
$$ 2xz - 2axy = px^2 - ap $$
$$ 2x(z - ay) = p(x^2 - a) $$
$$ p = \frac{2x(z - ay)}{x^2 - a} $$

**Step 6: Integrate for Complete Integral**
$$ dz = p dx + q dy $$
$$ dz = \frac{2x(z - ay)}{x^2 - a} dx + a dy $$
Rearrange to group $z$ and $y$:
$$ dz - a dy = \frac{2x(z - ay)}{x^2 - a} dx $$
Let $U = z - ay$, then $dU = dz - a dy$.
$$ dU = \frac{2x}{x^2 - a} U dx $$
$$ \frac{dU}{U} = \frac{2x}{x^2 - a} dx $$

Integrate:
$$ \ln U = \ln(x^2 - a) + \ln b $$
$$ \ln(z - ay) = \ln(b(x^2 - a)) $$
$$ z - ay = b(x^2 - a) $$
$$ z - ay - b(x^2 - a) = 0 $$

**Result:**
This is the required complete integral.

---

### Theory: Singular Solution (Page 15)

**Definition**
A **singular solution** to a differential equation is a solution that cannot be obtained from the general (or complete) solution by assigning specific values to the arbitrary constants.
*   It exists independently.
*   Geometrically, it often represents the envelope of the family of surfaces given by the general solution.

**Method to Find Singular Solution:**
Given a complete integral with arbitrary constants $a$ and $b$: $z = f(x, y, a, b)$.
1.  Differentiate the integral partially w.r.t $a$ and set to zero: $\frac{\partial z}{\partial a} = 0$.
2.  Differentiate the integral partially w.r.t $b$ and set to zero: $\frac{\partial z}{\partial b} = 0$.
3.  Eliminate constants $a$ and $b$ using these three equations.

**Example from Problem Continued:**
From the previous page, the complete integral is:
$$ z = ay + b(x^2 - a) \quad \text{..........(3)} $$
Differentiating w.r.t $a$:
$$ 0 = y - b \implies b = y \quad \text{..........(4)} $$
Differentiating w.r.t $b$:
$$ 0 = x^2 - a \implies a = x^2 \quad \text{..........(5)} $$

Substitute $a = x^2$ and $b = y$ into (3):
$$ z = (x^2)y + y(x^2 - x^2) $$
$$ z = x^2y $$
This is the **singular integral**.

---

### Theory: Standard Form I (Page 16)

**Form:** $f(p, q) = 0$
This form only involves $p$ and $q$ (no $x, y, z$).

**Method:**
From Charpit's equations for this form:
$$ \frac{dp}{0} = \frac{dq}{0} $$
This implies $p = a$ (constant) and $q = b$ (constant).
Substitute these into the original equation $f(a, b) = 0$ to find a relationship between $a$ and $b$, say $b = F(a)$.

**Complete Integral:**
$$ z = ax + by + c $$
Substitute $b = F(a)$:
$$ z = ax + y F(a) + c $$
This contains two arbitrary constants $a$ and $c$.

Here is the detailed explanation of pages 17 through 22 from the provided document.

### Question: Solve $pq = k$, where $k$ is a constant.

**Solve $pq = k$, where $k$ is a constant.**


**Step 1: Identify Standard Form**
The given equation is $pq = k$. This is of the form $f(p, q) = 0$ (Standard Form I).

**Step 2: Apply Solution Structure**
For Standard Form I, the solution is $z = ax + by + c$, where the constants $a$ and $b$ must satisfy the original PDE.
Here, substituting $p = a$ and $q = b$ into the PDE:
$$ ab = k \quad \text{or} \quad b = \frac{k}{a} $$

**Step 3: Write Complete Integral**
Substitute $b = k/a$ into the linear solution:
$$ z = ax + \left(\frac{k}{a}\right)y + c \quad \text{...(3)} $$
This contains two arbitrary constants $a$ and $c$.

**Step 4: Singular Solution Analysis**
To find the singular solution, differentiate (3) with respect to $a$ and $c$:
*   $\frac{\partial z}{\partial c} = 1 \implies 1 = 0$, which is absurd.
*   **Conclusion:** There is no singular solution for this equation.

---

### Question: Solve $p^2 + q^2 = m^2$, where $m$ is a constant.

**Solve $p^2 + q^2 = m^2$, where $m$ is a constant.**


**Step 1: Identify Standard Form**
Equation: $p^2 + q^2 = m^2$. This is Form $f(p, q) = 0$.

**Step 2: Relation of Constants**
Substitute $p = a$ and $q = b$:
$$ a^2 + b^2 = m^2 $$
Solve for $b$:
$$ b^2 = m^2 - a^2 \implies b = (m^2 - a^2)^{1/2} $$

**Step 3: Complete Integral**
Substitute $b$ into $z = ax + by + c$:
$$ z = ax + y(m^2 - a^2)^{1/2} + c \quad \text{...(3)} $$
This is the complete integral with arbitrary constants $a$ and $c$.

---

### Theory: Standard Form II (Clairaut Equation) (Page 18)

**Definition**
A first-order PDE is said to be of **Clairaut form** if it can be written as:
$$ z = px + qy + f(p, q) \quad \text{...(1)} $$
Rearranging to $F(x, y, z, p, q) = px + qy + f(p, q) - z = 0$.

**Derivation of Solution using Charpit’s Method**
The auxiliary equations for $F$ are:
$$ \frac{dp}{\frac{\partial F}{\partial x} + p\frac{\partial F}{\partial z}} = \frac{dq}{\frac{\partial F}{\partial y} + q\frac{\partial F}{\partial z}} = \dots $$
*   $\frac{\partial F}{\partial x} = p$, $\frac{\partial F}{\partial z} = -1 \implies \text{denom for } dp: p + p(-1) = 0$.
*   $\frac{\partial F}{\partial y} = q$, $\frac{\partial F}{\partial z} = -1 \implies \text{denom for } dq: q + q(-1) = 0$.

Thus:
$$ \frac{dp}{0} = \frac{dq}{0} $$
This implies $p = a$ and $q = b$ (constants).

**Complete Integral**
Substitute $p = a$ and $q = b$ directly into the original equation (1):
$$ z = ax + by + f(a, b) $$
This linear equation is the complete integral.

---

### Question: Solve $z = px + qy + pq$.

**Solve $z = px + qy + pq$.**


**Step 1: Complete Integral**
This matches the Clairaut form $z = px + qy + f(p, q)$ where $f(p, q) = pq$.
Replace $p$ with $a$ and $q$ with $b$:
$$ z = ax + by + ab \quad \text{...(1)} $$

**Step 2: Singular Integral**
Differentiate (1) w.r.t $a$ and $b$:
*   $\frac{\partial z}{\partial a} = x + b = 0 \implies b = -x$
*   $\frac{\partial z}{\partial b} = y + a = 0 \implies a = -y$

**Step 3: Final Substitution**
Substitute $a = -y$ and $b = -x$ into (1):
$$ z = (-y)x + (-x)y + (-y)(-x) $$
$$ z = -xy - xy + xy $$
$$ z = -xy $$
This is the required singular solution.

---

### Question: Prove that the complete integral of the equation $(px + qy - z)^2 = 1 + p^2 + q^2$ is $ax + by + cz = (a^2 + b^2 + c^2)^{1/2}$.

**Prove that the complete integral of the equation $(px + qy - z)^2 = 1 + p^2 + q^2$ is $ax + by + cz = (a^2 + b^2 + c^2)^{1/2}$.**


**Step 1: Rewrite Equation**
Take the square root:
$$ px + qy - z = \pm\sqrt{1 + p^2 + q^2} $$
$$ z = px + qy \mp \sqrt{1 + p^2 + q^2} $$
This is Standard Form II (Clairaut).

**Step 2: Standard Complete Integral**
Replace $p, q$ with constants $A, B$:
$$ z = Ax + By \pm (1 + A^2 + B^2)^{1/2} \quad \text{...(1)} $$

**Step 3: Transform Constants**
To match the desired form, let $A = -a/c$ and $B = -b/c$.
Substitute into (1) (taking positive sign for derivation):
$$ z = -\frac{a}{c}x - \frac{b}{c}y + \left(1 + \frac{a^2}{c^2} + \frac{b^2}{c^2}\right)^{1/2} $$
Multiply by $c$ (assuming $c>0$ for the root term):
$$ cz = -ax - by + c\sqrt{\frac{c^2 + a^2 + b^2}{c^2}} $$
$$ cz = -ax - by + \sqrt{c^2 + a^2 + b^2} $$
$$ ax + by + cz = (a^2 + b^2 + c^2)^{1/2} $$
This matches the required form.

---

### Theory: Standard Form III (Page 20)

**Form:** $f(p, q, z) = 0$
This form involves $p, q,$ and $z$ but no $x$ or $y$.

**Method:**
From Charpit's equations, since $\frac{\partial f}{\partial x} = 0$ and $\frac{\partial f}{\partial y} = 0$:
$$ \frac{dp}{p(\partial f/\partial z)} = \frac{dq}{q(\partial f/\partial z)} $$
$$ \frac{dp}{p} = \frac{dq}{q} $$
Integrating gives $q = ap$.

**Process:**
1.  Substitute $q = ap$ into the original equation $f(p, ap, z) = 0$ to solve for $p$ and $q$ in terms of $z$ and $a$.
2.  Use $dz = p dx + q dy = p dx + ap dy = p(dx + a dy)$.
3.  Let $u = x + ay$, then $dz = p du$.
4.  Solve the resulting ordinary differential equation (ODE) for $z$ and $u$.

---

### Question: Find a complete integral of $9(p^2z + q^2) = 4$.

**Find a complete integral of $9(p^2z + q^2) = 4$.**


**Step 1: Identify Form**
Equation: $f(p, q, z) = 9(p^2z + q^2) - 4 = 0$. (Standard Form III).

**Step 2: Substitution**
Let $u = x + ay$. Replace $p$ by $\frac{dz}{du}$ and $q$ by $a\frac{dz}{du}$.
Substitute into original equation:
$$ 9 \left[ z\left(\frac{dz}{du}\right)^2 + \left(a\frac{dz}{du}\right)^2 \right] = 4 $$
$$ 9 \left(\frac{dz}{du}\right)^2 (z + a^2) = 4 $$

**Step 3: Solve for derivative**
$$ \left(\frac{dz}{du}\right)^2 = \frac{4}{9(z + a^2)} $$
$$ \frac{dz}{du} = \pm \frac{2}{3\sqrt{z + a^2}} = \pm \frac{2}{3}(z + a^2)^{-1/2} $$

**Step 4: Separate and Integrate**
$$ (z + a^2)^{1/2} dz = \pm \frac{2}{3} du $$
Integrating both sides:
$$ \int (z + a^2)^{1/2} dz = \pm \frac{2}{3} \int du $$
$$ \frac{(z + a^2)^{3/2}}{3/2} = \pm \frac{2}{3} (u + b) $$
$$ \frac{2}{3}(z + a^2)^{3/2} = \pm \frac{2}{3} (u + b) $$
Cancel $2/3$:
$$ (z + a^2)^{3/2} = \pm (u + b) $$
Square both sides:
$$ (z + a^2)^3 = (u + b)^2 $$

**Step 5: Final Substitution**
Replace $u = x + ay$:
$$ (z + a^2)^3 = (x + ay + b)^2 $$

---

### Question: Find complete, singular and general integral of $p^3 + q^3 = 27z$.

**Find complete, singular and general integral of $p^3 + q^3 = 27z$.**


**Step 1: Complete Integral (Form III)**
Let $u = x + ay$, so $p = \frac{dz}{du}, q = a\frac{dz}{du}$.
$$ \left(\frac{dz}{du}\right)^3 + \left(a\frac{dz}{du}\right)^3 = 27z $$
$$ \left(\frac{dz}{du}\right)^3 (1 + a^3) = 27z $$
Solve for $dz/du$:
$$ \frac{dz}{du} (1 + a^3)^{1/3} = 3 z^{1/3} $$
Separate variables:
$$ z^{-1/3} dz = \frac{3}{(1 + a^3)^{1/3}} du $$
Integrate:
$$ \frac{z^{2/3}}{2/3} = \frac{3u}{(1 + a^3)^{1/3}} + b' $$
Simplifying leads to:
$$ 8(x + ay + b)^3 = (1 + a^3)z^2 \quad \text{...(1)} $$
(where constant is adjusted for simplicity).

**Step 2: Singular Integral**
Differentiate (1) w.r.t $a$ and $b$.
*   w.r.t $b$: $24(x + ay + b)^2 = 0 \implies x + ay + b = 0 \quad \text{...(3)}$
*   w.r.t $a$: $24y(x + ay + b)^2 = 3a^2z^2 \quad \text{...(2)}$
From (3), the LHS of (2) is 0, so $3a^2z^2 = 0 \implies z = 0$ (assuming $a \neq 0$).
Substitute $z=0$ into (1): $8(x+ay+b)^3 = 0 \implies x+ay+b=0$.
Substitute back into original PDE: if $z=0$, $p=0, q=0$. $0^3 + 0^3 = 27(0)$.
**Conclusion:** $z=0$ is the singular integral.

Here is the detailed explanation of pages 23 through 25 from the provided document.

### Theory: Standard Form IV (Page 23)

**Form:** $f_1(x, p) = f_2(y, q)$
This form (also known as Separation of Variables) applies when the equation can be separated such that terms containing $x$ and $p$ are on one side, and terms containing $y$ and $q$ are on the other. Note that $z$ does not appear.

**Derivation using Charpit’s Method:**
Let the equation be $F(x, y, z, p, q) = f_1(x, p) - f_2(y, q) = 0$.
The auxiliary equations are:
$$ \frac{dp}{\frac{\partial f_1}{\partial x} + p(0)} = \frac{dq}{-\frac{\partial f_2}{\partial y} + q(0)} = \frac{dz}{\dots} = \frac{dx}{-\frac{\partial f_1}{\partial p}} = \frac{dy}{-\left(-\frac{\partial f_2}{\partial q}\right)} $$

Focusing on the first and fourth ratios involving $x$ and $p$:
$$ \frac{dp}{\frac{\partial f_1}{\partial x}} = \frac{dx}{-\frac{\partial f_1}{\partial p}} $$
Cross-multiplying:
$$ -\frac{\partial f_1}{\partial p} dp = \frac{\partial f_1}{\partial x} dx $$
$$ \frac{\partial f_1}{\partial p} dp + \frac{\partial f_1}{\partial x} dx = 0 $$
This expression is the total differential of $f_1(x, p)$, assuming $f_1$ only depends on $x$ and $p$.
$$ df_1 = 0 $$
Integrating gives:
$$ f_1(x, p) = a \quad (\text{constant}) $$
Since $f_1 = f_2$, it follows that:
$$ f_2(y, q) = a $$

**Procedure:**
1.  Separate the equation into $f_1(x, p) = f_2(y, q)$.
2.  Equate both sides to an arbitrary constant $a$.
3.  Solve $f_1(x, p) = a$ for $p$ to get $p = F_1(x, a)$.
4.  Solve $f_2(y, q) = a$ for $q$ to get $q = F_2(y, a)$.
5.  Substitute these into $dz = p dx + q dy$.
6.  Integrate to find the complete integral:
    $$ z = \int F_1(x, a) dx + \int F_2(y, a) dy + b $$

---

### Question: Find a complete integral of $x(1 + y)p = y(1 + x)q$.

**Find a complete integral of $x(1 + y)p = y(1 + x)q$.**


**Step 1: Separate Variables**
Rewrite the equation to separate $x, p$ from $y, q$:
$$ \frac{xp}{1 + x} = \frac{yq}{1 + y} $$

**Step 2: Equate to Constant**
Set both sides equal to an arbitrary constant $a$:
$$ \frac{xp}{1 + x} = a \quad \text{and} \quad \frac{yq}{1 + y} = a $$

**Step 3: Solve for p and q**
*   For $p$:
    $$ xp = a(1 + x) \implies p = a \frac{1 + x}{x} = a\left(\frac{1}{x} + 1\right) $$
*   For $q$:
    $$ yq = a(1 + y) \implies q = a \frac{1 + y}{y} = a\left(\frac{1}{y} + 1\right) $$

**Step 4: Integrate for Complete Integral**
Substitute $p$ and $q$ into $dz = p dx + q dy$:
$$ dz = a\left(\frac{1}{x} + 1\right) dx + a\left(\frac{1}{y} + 1\right) dy $$
$$ dz = a\left(\frac{1}{x} dx + dx\right) + a\left(\frac{1}{y} dy + dy\right) $$

Integrate term by term:
$$ z = a(\ln x + x) + a(\ln y + y) + b $$
$$ z = a(\ln x + \ln y + x + y) + b $$
$$ z = a(\ln(xy) + x + y) + b $$

**Result:**
This is the complete integral containing two arbitrary constants $a$ and $b$.

---

### Question: Find a complete integral of $p - 3x^2 = q^2 - y$.

**Find a complete integral of $p - 3x^2 = q^2 - y$.**


**Step 1: Separate Variables**
The equation is already separated:
$$ f_1(x, p) = p - 3x^2 $$
$$ f_2(y, q) = q^2 - y $$

**Step 2: Equate to Constant**
Set both sides equal to $a$:
$$ p - 3x^2 = a \quad \text{and} \quad q^2 - y = a $$

**Step 3: Solve for p and q**
*   For $p$: $p = a + 3x^2$
*   For $q$: $q^2 = a + y \implies q = (a + y)^{1/2}$

**Step 4: Integrate for Complete Integral**
$$ dz = p dx + q dy $$
$$ dz = (a + 3x^2) dx + (a + y)^{1/2} dy $$

Integrate:
$$ z = ax + \frac{3x^3}{3} + \frac{(a + y)^{3/2}}{3/2} + b $$
$$ z = ax + x^3 + \frac{2}{3}(a + y)^{3/2} + b $$

**Result:**
This is the required complete integral.

---

### Homework Problems (Page 25)

**i) Problem:** $p^2 + q^2 = x^2 + y^2$
*   **Method:** Separate as $p^2 - x^2 = y^2 - q^2$ (or $p^2 - x^2 = a$ and $y^2 - q^2 = a$).
    *   $p = \sqrt{a + x^2}$, $q = \sqrt{y^2 - a}$ (Note: signs depend on rearrangement).
*   **Provided Ans:** $2z = x(x^2 + a^2)^{1/2} + a^2\sinh^{-1}(x/a) + y(y^2 - a^2)^{1/2} - a^2\cosh^{-1}(y/a) + b$.
    *(This suggests integrating $\sqrt{x^2+a^2}$ and $\sqrt{y^2-a^2}$).*

**ii) Problem:** $\sqrt{p} + \sqrt{q} = 2x$
*   **Correction/Note:** This looks like it should be separated. If standard form IV, we might rearrange terms. However, if it depends on $x$ only (Standard Form IV requires separation), we treat it as $f_1(x,p) = f_2(y,q)$. Since no $y$ is explicit, this might be viewed as $q$ being constant relative to $x$-terms or rearranging if possible.
*   **Actually:** This looks like $\sqrt{p} - 2x = -\sqrt{q}$. Let equal constant $a$.
    *   $\\sqrt{p} = 2x + a \implies p = (2x+a)^2$.
    *   $-\\sqrt{q} = a \implies q = a^2$.
*   **Provided Ans:** C.I. $z = (2x - a)^3/6 + a^2y + b$.
    *   Let's check the integration of $(2x-a)^2$: $\int (2x-a)^2 dx = \frac{(2x-a)^3}{3 \cdot 2} = \frac{(2x-a)^3}{6}$. This matches the $x$ part.
    *   The $y$ part is $\int a^2 dy = a^2y$. This matches.
    *   Note: The sign of $a$ in the answer suggests separation was $\sqrt{p} - 2x = a$ or similar.

**Reference:**
For more practice, follow **Ordinary and Partial Differential Equations** book by **M.D. Raisinghania**.