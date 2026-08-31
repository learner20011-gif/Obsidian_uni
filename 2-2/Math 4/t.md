# Complex Integration & Residue Calculus: Step-by-Step Solutions and Proofs

This document provides complete, rigorous, step-by-step mathematical proofs and problem solutions for **Complex Integration**, **Cauchy's Theorems & Formulas**, and **Singularities & Residues**.

---

## Part 1: Complex Integration & Cauchy's Theorems

---

### Q.1. State and prove Cauchy's Theorem (Cauchy's Fundamental Theorem)

#### **Statement:**
Let $f(z)$ be an analytic function in a simply connected domain $R$ and on its simple, closed, rectifiable boundary curve $C$. If the derivative $f'(z)$ is continuous at all points inside $R$ and on $C$, then the contour integral of $f(z)$ along $C$ vanishes:
$$\oint_C f(z)\,dz = 0$$

---

#### **Proof:**

**Step 1: Express $z$, $dz$, and $f(z)$ in Cartesian Components**
Let $z = x + iy$, so the differential is:
$$dz = dx + i\,dy$$
Let the complex function $f(z)$ be split into its real and imaginary parts:
$$f(z) = u(x, y) + i\,v(x, y)$$
where $u(x,y)$ and $v(x,y)$ are real-valued functions of $x$ and $y$.

---

**Step 2: Derive the Cauchy-Riemann Equations from the Derivative $f'(z)$**
Since $f(z)$ is analytic, its complex derivative $f'(z)$ exists independently of the path of approach:
$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

1. **Approach along the real axis ($\Delta z = \Delta x$, $\Delta y = 0$):**
   $$f'(z) = \lim_{\Delta x \to 0} \frac{[u(x+\Delta x, y) + i\,v(x+\Delta x, y)] - [u(x,y) + i\,v(x,y)]}{\Delta x} = \frac{\partial u}{\partial x} + i\,\frac{\partial v}{\partial x} \quad \text{--- (1)}$$

2. **Approach along the imaginary axis ($\Delta z = i\,\Delta y$, $\Delta x = 0$):**
   $$f'(z) = \lim_{\Delta y \to 0} \frac{[u(x, y+\Delta y) + i\,v(x, y+\Delta y)] - [u(x,y) + i\,v(x,y)]}{i\,\Delta y} = \frac{1}{i}\left(\frac{\partial u}{\partial y} + i\,\frac{\partial v}{\partial y}\right)$$
   Since $\frac{1}{i} = -i$:
   $$f'(z) = \frac{\partial v}{\partial y} - i\,\frac{\partial u}{\partial y} \quad \text{--- (2)}$$

3. **Equate the real and imaginary parts of (1) and (2):**
   $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \quad \text{--- (Cauchy-Riemann Equations)}$$
   Since $f'(z)$ is given to be continuous, all four first-order partial derivatives ($\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial v}{\partial x}, \frac{\partial v}{\partial y}$) are continuous in $R$ and on $C$.

---

**Step 3: Expand the Complex Line Integral**
Substitute $f(z) = u + iv$ and $dz = dx + i\,dy$ into the contour integral:
$$\oint_C f(z)\,dz = \oint_C (u + iv)(dx + i\,dy)$$
$$\oint_C f(z)\,dz = \oint_C (u\,dx + i\,u\,dy + i\,v\,dx + i^2 v\,dy)$$
Since $i^2 = -1$, group into real and imaginary line integrals:
$$\oint_C f(z)\,dz = \oint_C (u\,dx - v\,dy) + i \oint_C (v\,dx + u\,dy) \quad \text{--- (3)}$$

---

**Step 4: Apply Green's Theorem in the Plane**
**Green's Theorem** states: If $P(x,y), Q(x,y)$ and their partial derivatives are continuous in a region $R$ bounded by a simple closed curve $C$, then:
$$\oint_C (P\,dx + Q\,dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx\,dy$$

1. **For the real part $\oint_C (u\,dx - v\,dy)$:**
   Set $P = u$ and $Q = -v$:
   $$\oint_C (u\,dx - v\,dy) = \iint_R \left( \frac{\partial(-v)}{\partial x} - \frac{\partial u}{\partial y} \right) dx\,dy = \iint_R \left( -\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} \right) dx\,dy$$
   Using the second C-R equation $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$:
   $$\iint_R \left( -\frac{\partial v}{\partial x} - \left(-\frac{\partial v}{\partial x}\right) \right) dx\,dy = \iint_R 0\,dx\,dy = 0$$

2. **For the imaginary part $\oint_C (v\,dx + u\,dy)$:**
   Set $P = v$ and $Q = u$:
   $$\oint_C (v\,dx + u\,dy) = \iint_R \left( \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \right) dx\,dy$$
   Using the first C-R equation $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$:
   $$\iint_R \left( \frac{\partial u}{\partial x} - \frac{\partial u}{\partial x} \right) dx\,dy = \iint_R 0\,dx\,dy = 0$$

---

**Step 5: Conclusion**
Substituting these two zero integrals back into equation (3):
$$\oint_C f(z)\,dz = 0 + i(0) = 0$$
Hence, Cauchy's Theorem is proved. $\blacksquare$

---

### Q.2. State and prove Cauchy's Integral Formula

#### **Statement:**
Let $f(z)$ be analytic inside and on a simple closed contour $C$ traversed in the counter-clockwise (positive) direction. If $a$ is any point in the interior of $C$, then:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}\,dz$$

---

#### **Proof:**

**Step 1: Deformation of Contours (Multi-connected Region)**
Consider the function $\phi(z) = \frac{f(z)}{z-a}$. 
- Since $f(z)$ is analytic inside and on $C$, $\phi(z)$ is analytic everywhere inside and on $C$ **except** at the single isolated point $z = a$.
- Enclose the point $a$ with a small circle $\Gamma$ of radius $r$ centered at $a$, defined by $\vert z - a \vert = r$, chosen small enough so that $\Gamma$ lies entirely within the interior of $C$.
- In the annular (doubly connected) region lying between $C$ and $\Gamma$, the function $\frac{f(z)}{z-a}$ is analytic everywhere.
- By the Principle of Contour Deformation (extended Cauchy's Theorem):
  $$\oint_C \frac{f(z)}{z-a}\,dz = \oint_\Gamma \frac{f(z)}{z-a}\,dz \quad \text{--- (1)}$$

---

**Step 2: Parametrize the Circle $\Gamma$**
The circle $\Gamma$ centered at $a$ with radius $r$ can be parametrized in polar coordinates as:
$$z - a = r e^{i\theta} \implies z = a + r e^{i\theta}, \quad \text{where } 0 \le \theta \le 2\pi$$
Taking differentials:
$$dz = i r e^{i\theta}\,d\theta$$

---

**Step 3: Evaluate the Integral along $\Gamma$**
Substitute the parametrization into the integral along $\Gamma$:
$$\oint_\Gamma \frac{f(z)}{z-a}\,dz = \int_0^{2\pi} \frac{f(a + r e^{i\theta})}{r e^{i\theta}} \left( i r e^{i\theta}\,d\theta \right) = i \int_0^{2\pi} f(a + r e^{i\theta})\,d\theta$$

Now rewrite $f(a + r e^{i\theta})$ as $f(a) + [f(a + r e^{i\theta}) - f(a)]$:
$$\oint_\Gamma \frac{f(z)}{z-a}\,dz = i \int_0^{2\pi} f(a)\,d\theta + i \int_0^{2\pi} [f(a + r e^{i\theta}) - f(a)]\,d\theta$$
$$= i f(a) \cdot [\theta]_0^{2\pi} + i \int_0^{2\pi} [f(a + r e^{i\theta}) - f(a)]\,d\theta$$
$$= 2\pi i f(a) + i \int_0^{2\pi} [f(a + r e^{i\theta}) - f(a)]\,d\theta \quad \text{--- (2)}$$

---

**Step 4: Take the Limit as $r \to 0$**
Since $f(z)$ is analytic at $z = a$, it is continuous at $z = a$. By the definition of continuity, for every $\epsilon > 0$, there exists $\delta > 0$ such that:
$$\vert f(a + r e^{i\theta}) - f(a) \vert < \epsilon \quad \text{whenever } r < \delta$$

Now, estimate the modulus of the remainder integral:
$$\left\vert i \int_0^{2\pi} [f(a + r e^{i\theta}) - f(a)]\,d\theta \right\vert \le \int_0^{2\pi} \vert f(a + r e^{i\theta}) - f(a) \vert\,d\theta < \int_0^{2\pi} \epsilon\,d\theta = 2\pi\epsilon$$

Since $\epsilon > 0$ is arbitrarily small, taking $r \to 0$ yields:
$$\lim_{r \to 0} i \int_0^{2\pi} [f(a + r e^{i\theta}) - f(a)]\,d\theta = 0$$

---

**Step 5: Final Result**
Since the left-hand side of equation (1) is completely independent of $r$, taking $r \to 0$ on the right-hand side gives:
$$\oint_C \frac{f(z)}{z-a}\,dz = 2\pi i f(a)$$
Dividing both sides by $2\pi i$:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}\,dz$$
Hence proved. $\blacksquare$

---

### Q.3. State and prove Cauchy's Integral Formula for the First Derivative

#### **Statement:**
Let $f(z)$ be analytic inside and on a simple closed contour $C$. If $a$ is any point inside $C$, then the derivative $f'(a)$ exists and is given by:
$$f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz$$

---

#### **Proof:**

**Step 1: Set up the Difference Quotient**
By definition of the complex derivative:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$
Choose $h$ sufficiently small so that the neighboring point $a+h$ also lies strictly inside $C$.

Applying Cauchy's Integral Formula to both $f(a+h)$ and $f(a)$:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}\,dz \quad \text{and} \quad f(a+h) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-(a+h)}\,dz$$

---

**Step 2: Compute the Difference $\frac{f(a+h) - f(a)}{h}$**
$$\frac{f(a+h) - f(a)}{h} = \frac{1}{2\pi i h} \oint_C \left[ \frac{1}{z-(a+h)} - \frac{1}{z-a} \right] f(z)\,dz$$

Combine the fractions inside the bracket:
$$\frac{1}{z-a-h} - \frac{1}{z-a} = \frac{(z-a) - (z-a-h)}{(z-a-h)(z-a)} = \frac{h}{(z-a-h)(z-a)}$$

Substitute this back:
$$\frac{f(a+h) - f(a)}{h} = \frac{1}{2\pi i h} \oint_C \frac{h}{(z-a-h)(z-a)} f(z)\,dz = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a-h)(z-a)}\,dz \quad \text{--- (1)}$$

---

**Step 3: Subtract the Target Expression $\frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz$**
$$\frac{f(a+h) - f(a)}{h} - \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz = \frac{1}{2\pi i} \oint_C \left[ \frac{1}{(z-a-h)(z-a)} - \frac{1}{(z-a)^2} \right] f(z)\,dz$$

Simplify the integrand:
$$\frac{1}{(z-a-h)(z-a)} - \frac{1}{(z-a)^2} = \frac{(z-a) - (z-a-h)}{(z-a)^2 (z-a-h)} = \frac{h}{(z-a)^2 (z-a-h)}$$

Thus:
$$\frac{f(a+h) - f(a)}{h} - \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz = \frac{h}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2 (z-a-h)}\,dz \quad \text{--- (2)}$$

---

**Step 4: Bound the Remainder using the $ML$-Inequality**
Let:
- $L$ be the arc length of the contour $C$.
- $M = \max_{z \in C} \vert f(z) \vert$ (since $f(z)$ is continuous on the compact curve $C$, it is bounded).
- $d = \min_{z \in C} \vert z-a \vert > 0$ be the shortest distance from $a$ to the boundary curve $C$.

For any point $z \in C$:
$$\vert z - a \vert \ge d$$
Choose $\vert h \vert \le \frac{d}{2}$. Using the reverse triangle inequality:
$$\vert z - a - h \vert \ge \vert z - a \vert - \vert h \vert \ge d - \frac{d}{2} = \frac{d}{2}$$

Now apply the modulus to the right-hand side of equation (2):
$$\left\vert \frac{h}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2 (z-a-h)}\,dz \right\vert \le \frac{\vert h \vert}{2\pi} \cdot \frac{M}{d^2 \cdot (d/2)} \cdot L = \frac{M L \vert h \vert}{\pi d^3}$$

---

**Step 5: Take the Limit as $h \to 0$**
$$\lim_{h \to 0} \left\vert \frac{f(a+h) - f(a)}{h} - \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz \right\vert \le \lim_{h \to 0} \frac{M L \vert h \vert}{\pi d^3} = 0$$

Therefore:
$$\lim_{h \to 0} \frac{f(a+h) - f(a)}{h} = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz$$
$$f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz$$
Hence proved. $\blacksquare$

---

### Q.4. State and prove Cauchy's Integral Formula for Higher Derivatives

#### **Statement:**
Let $f(z)$ be analytic inside and on a simple closed contour $C$. Then $f(z)$ has derivatives of all orders at any interior point $a$ inside $C$, given by:
$$f^{(n)}(a) = \frac{n!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}}\,dz, \quad \text{for } n = 1, 2, 3, \dots$$

---

#### **Proof (By Mathematical Induction):**

**Step 1: Base Case ($n = 1$)**
For $n = 1$:
$$f'(a) = \frac{1!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{1+1}}\,dz = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}\,dz$$
This was rigorously proved in **Q.3**. Therefore, the formula is true for $n = 1$.

---

**Step 2: Induction Hypothesis**
Assume the formula is valid for $n = m$:
$$f^{(m)}(a) = \frac{m!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{m+1}}\,dz \quad \text{--- (Hypothesis)}$$

---

**Step 3: Inductive Step ($n = m + 1$)**
By definition of the $(m+1)$-th derivative:
$$f^{(m+1)}(a) = \lim_{h \to 0} \frac{f^{(m)}(a+h) - f^{(m)}(a)}{h}$$

Using the induction hypothesis:
$$f^{(m)}(a+h) = \frac{m!}{2\pi i} \oint_C \frac{f(z)}{(z-a-h)^{m+1}}\,dz$$
Therefore:
$$\frac{f^{(m)}(a+h) - f^{(m)}(a)}{h} = \frac{m!}{2\pi i h} \oint_C \left[ \frac{1}{(z-a-h)^{m+1}} - \frac{1}{(z-a)^{m+1}} \right] f(z)\,dz$$

Factor out $\frac{1}{(z-a)^{m+1}}$ from the integrand:
$$\frac{1}{(z-a-h)^{m+1}} - \frac{1}{(z-a)^{m+1}} = \frac{1}{(z-a)^{m+1}} \left[ \left( 1 - \frac{h}{z-a} \right)^{-(m+1)} - 1 \right]$$

---

**Step 4: Binomial Expansion**
Recall the general binomial series $(1 - w)^{-k} = 1 + kw + \frac{k(k+1)}{2!} w^2 + \dots$ for $\vert w \vert < 1$.
Here $w = \frac{h}{z-a}$ and $k = m+1$:
$$\left( 1 - \frac{h}{z-a} \right)^{-(m+1)} = 1 + (m+1)\frac{h}{z-a} + \frac{(m+1)(m+2)}{2!} \left( \frac{h}{z-a} \right)^2 + O(h^3)$$

Subtracting 1 and dividing by $h$:
$$\frac{1}{h} \left[ \left( 1 - \frac{h}{z-a} \right)^{-(m+1)} - 1 \right] = \frac{m+1}{z-a} + \frac{(m+1)(m+2)}{2!} \frac{h}{(z-a)^2} + O(h^2)$$

---

**Step 5: Evaluate the Limit as $h \to 0$**
Substitute this back into the difference quotient and take the limit $h \to 0$:
$$\lim_{h \to 0} \frac{f^{(m)}(a+h) - f^{(m)}(a)}{h} = \frac{m!}{2\pi i} \oint_C \frac{1}{(z-a)^{m+1}} \lim_{h \to 0} \left( \frac{m+1}{z-a} + O(h) \right) f(z)\,dz$$
$$f^{(m+1)}(a) = \frac{m!}{2\pi i} \oint_C \frac{(m+1)}{(z-a)^{m+2}} f(z)\,dz$$
Since $m! \cdot (m+1) = (m+1)!$:
$$f^{(m+1)}(a) = \frac{(m+1)!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{m+2}}\,dz$$

---

**Step 6: Conclusion**
Since the base step holds ($n=1$) and the truth for $n=m$ implies the truth for $n=m+1$, by mathematical induction, the formula holds for all positive integers $n \in \mathbb{N}$. $\blacksquare$

---

### Q.5. State and prove Liouville's Theorem

#### **Statement:**
If an entire function $f(z)$ (analytic everywhere in the whole complex plane $\mathbb{C}$) is bounded for all $z \in \mathbb{C}$, then $f(z)$ must be a constant.

---

#### **Proof:**

**Step 1: Set up Two Arbitrary Points**
Let $a$ and $b$ be any two arbitrary points in the complex plane $\mathbb{C}$.
Draw a circle $C$ centered at $a$ with radius $R$, where the radius is chosen sufficiently large such that $R > 2\vert b - a \vert$ (meaning $b$ lies strictly inside $C$).

The equation of the contour $C$ is $\vert z - a \vert = R$.

---

**Step 2: Express $f(b) - f(a)$ using Cauchy's Integral Formula**
By Cauchy's Integral Formula:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}\,dz \quad \text{and} \quad f(b) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-b}\,dz$$

Subtracting the two:
$$f(b) - f(a) = \frac{1}{2\pi i} \oint_C \left( \frac{1}{z-b} - \frac{1}{z-a} \right) f(z)\,dz$$
Simplify the bracket:
$$\frac{1}{z-b} - \frac{1}{z-a} = \frac{(z-a) - (z-b)}{(z-b)(z-a)} = \frac{b-a}{(z-b)(z-a)}$$
Therefore:
$$f(b) - f(a) = \frac{b-a}{2\pi i} \oint_C \frac{f(z)}{(z-b)(z-a)}\,dz \quad \text{--- (1)}$$

---

**Step 3: Establish Bounds on the Integrand**
1. **Boundedness of $f(z)$:** Since $f(z)$ is bounded everywhere in $\mathbb{C}$, there exists a real constant $M > 0$ such that:
   $$\vert f(z) \vert \le M, \quad \forall z \in \mathbb{C}$$
2. **On the contour $C$:**
   $$\vert z - a \vert = R$$
3. **Bound for $\vert z - b \vert$ using reverse triangle inequality:**
   $$\vert z - b \vert = \vert (z - a) - (b - a) \vert \ge \vert z - a \vert - \vert b - a \vert = R - \vert b - a \vert$$
   Since we chose $R > 2\vert b - a \vert \implies \vert b - a \vert < \frac{R}{2}$:
   $$\vert z - b \vert > R - \frac{R}{2} = \frac{R}{2}$$

---

**Step 4: Apply the $ML$-Inequality**
Length of the circular contour $C$ is $L = 2\pi R$.
Taking absolute values on both sides of equation (1):
$$\vert f(b) - f(a) \vert = \left\vert \frac{b-a}{2\pi i} \oint_C \frac{f(z)}{(z-b)(z-a)}\,dz \right\vert \le \frac{\vert b - a \vert}{2\pi} \cdot \max_{z \in C} \left\vert \frac{f(z)}{(z-b)(z-a)} \right\vert \cdot (2\pi R)$$
$$\vert f(b) - f(a) \vert \le \frac{\vert b - a \vert}{2\pi} \cdot \frac{M}{\left(\frac{R}{2}\right) \cdot R} \cdot (2\pi R) = \frac{2 M \vert b - a \vert}{R}$$

---

**Step 5: Take the Limit as $R \to \infty$**
Since $f(z)$ is entire, $C$ can be expanded indefinitely to any radius $R$. Taking $R \to \infty$:
$$\lim_{R \to \infty} \vert f(b) - f(a) \vert \le \lim_{R \to \infty} \frac{2 M \vert b - a \vert}{R} = 0$$
$$\implies \vert f(b) - f(a) \vert = 0 \implies f(b) = f(a)$$

Since $a$ and $b$ were chosen arbitrarily in $\mathbb{C}$, $f(z)$ has the exact same value at all points. Thus, $f(z) = \text{constant}$. $\blacksquare$

---

### Q.6. Evaluate Line Integral

#### **Problem:**
Show that $\int_{(0,1)}^{(2,5)} (3x+y)\,dx + (2y-x)\,dy = 32$, along the straight line joining the points $(0,1)$ and $(2,5)$.

---

#### **Solution:**

**Step 1: Find the Equation of the Path (Straight Line)**
The two-point equation of a line passing through $(x_1, y_1) = (0,1)$ and $(x_2, y_2) = (2,5)$ is:
$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$$
$$\frac{y - 1}{5 - 1} = \frac{x - 0}{2 - 0} \implies \frac{y - 1}{4} = \frac{x}{2}$$
$$y - 1 = 2x \implies y = 2x + 1$$

---

**Step 2: Find the Differential and Limits of Integration**
- Differentiating with respect to $x$:
  $$dy = 2\,dx$$
- As the point moves from $(0,1)$ to $(2,5)$, the variable $x$ varies from $x = 0$ to $x = 2$.

---

**Step 3: Substitute $y$ and $dy$ into the Integral**
$$I = \int_{x=0}^2 \Big[ (3x + y)\,dx + (2y - x)\,dy \Big]$$
Substitute $y = 2x + 1$ and $dy = 2\,dx$:
$$I = \int_0^2 \Big[ (3x + (2x + 1))\,dx + \{2(2x + 1) - x\}(2\,dx) \Big]$$

Simplify each term step-by-step:
1. First term:
   $$(3x + 2x + 1)\,dx = (5x + 1)\,dx$$
2. Second term:
   $$\{4x + 2 - x\}(2\,dx) = (3x + 2)(2\,dx) = (6x + 4)\,dx$$
3. Combine all terms:
   $$I = \int_0^2 (5x + 1 + 6x + 4)\,dx = \int_0^2 (11x + 5)\,dx$$

---

**Step 4: Integrate and Evaluate the Limits**
$$I = \left[ 11 \cdot \frac{x^2}{2} + 5x \right]_0^2$$
Substitute the upper limit $x = 2$:
$$I = \left( \frac{11(2)^2}{2} + 5(2) \right) - \left( \frac{11(0)^2}{2} + 5(0) \right)$$
$$I = \left( \frac{11 \cdot 4}{2} + 10 \right) - 0 = (22 + 10) = 32$$

$$\therefore \int_{(0,1)}^{(2,5)} (3x+y)\,dx + (2y-x)\,dy = 32 \quad \text{(Verified)}$$

---

### Q.7. Evaluate Limits of Sums (Riemann Definition of Complex Contour Integral)

#### **Problem:**
Evaluate from first principles (definition of integral as limit of a sum):
1. $\int_C z\,dz$
2. $\int_C dz$
along a curve $C$ connecting initial point $a$ to final point $b$.

---

#### **Solution:**

**Definition:**
Let $C$ be a smooth curve with initial point $z_0 = a$ and terminal point $z_n = b$. Subdivide $C$ by points $z_0, z_1, z_2, \dots, z_n$.
The contour integral is defined as the limit of the Riemann sum:
$$\int_C f(z)\,dz = \lim_{n \to \infty, \vert \Delta z_k \vert \to 0} \sum_{k=1}^n f(\zeta_k) \Delta z_k$$
where $\Delta z_k = z_k - z_{k-1}$ and $\zeta_k$ is any point on the arc between $z_{k-1}$ and $z_k$.

---

#### **(i) Evaluation of $\int_C z\,dz$:**

1. **Choice 1:** Choose the right-endpoint $\zeta_k = z_k$:
   $$S_1 = \sum_{k=1}^n z_k (z_k - z_{k-1}) \xrightarrow{n \to \infty} \int_C z\,dz \quad \text{--- (1)}$$

2. **Choice 2:** Choose the left-endpoint $\zeta_k = z_{k-1}$:
   $$S_2 = \sum_{k=1}^n z_{k-1} (z_k - z_{k-1}) \xrightarrow{n \to \infty} \int_C z\,dz \quad \text{--- (2)}$$

3. **Add equations (1) and (2):**
   $$2 \int_C z\,dz = \lim_{n \to \infty} \sum_{k=1}^n (z_k + z_{k-1})(z_k - z_{k-1})$$
   Using algebraic identity $(A+B)(A-B) = A^2 - B^2$:
   $$2 \int_C z\,dz = \lim_{n \to \infty} \sum_{k=1}^n (z_k^2 - z_{k-1}^2)$$

4. **Expand the Telescoping Sum:**
   $$\sum_{k=1}^n (z_k^2 - z_{k-1}^2) = (z_1^2 - z_0^2) + (z_2^2 - z_1^2) + (z_3^2 - z_2^2) + \dots + (z_n^2 - z_{n-1}^2) = z_n^2 - z_0^2$$
   Since $z_0 = a$ and $z_n = b$:
   $$2 \int_C z\,dz = b^2 - a^2 \implies \int_C z\,dz = \frac{1}{2}(b^2 - a^2)$$

5. **Closed Contour:**
   If $C$ is a closed curve, the start and end points coincide ($a = b$):
   $$\oint_C z\,dz = \frac{1}{2}(a^2 - a^2) = 0$$

---

#### **(ii) Evaluation of $\int_C dz$:**

1. Here $f(z) = 1$. The Riemann sum is:
   $$\int_C dz = \lim_{n \to \infty} \sum_{k=1}^n 1 \cdot (z_k - z_{k-1})$$

2. **Expand the Telescoping Sum:**
   $$\sum_{k=1}^n (z_k - z_{k-1}) = (z_1 - z_0) + (z_2 - z_1) + \dots + (z_n - z_{n-1}) = z_n - z_0$$

3. **Substitute endpoints $z_0 = a$ and $z_n = b$:**
   $$\int_C dz = b - a$$

4. **Closed Contour:**
   If $C$ is closed, $a = b \implies \oint_C dz = 0$.

---

### Q.8. Evaluate Trigonometric Integral

#### **Problem:**
Show that $\oint_C \frac{\sin 3z}{z+\frac{\pi}{2}}\,dz = 2\pi i$, where $C$ is the circle $\vert z \vert = 5$.

---

#### **Solution:**

**Step 1: Identify Singularities and Check Enclosure**
- The integrand is $\frac{f(z)}{z - a}$ where $f(z) = \sin 3z$.
- The singularity occurs at the root of the denominator:
  $$z + \frac{\pi}{2} = 0 \implies z = -\frac{\pi}{2}$$
- The contour $C$ is the circle centered at origin with radius $R = 5$: $\vert z \vert = 5$.
- Compute the modulus of the singular point $a = -\frac{\pi}{2}$:
  $$\vert a \vert = \left\vert -\frac{\pi}{2} \right\vert = \frac{\pi}{2} \approx 1.5708$$
- Since $1.5708 < 5$, the singularity $a = -\frac{\pi}{2}$ lies **strictly inside** the contour $C$.

---

**Step 2: Apply Cauchy's Integral Formula**
Since $f(z) = \sin 3z$ is analytic everywhere in $\mathbb{C}$ (an entire function), by Cauchy's Integral Formula:
$$\oint_C \frac{f(z)}{z - a}\,dz = 2\pi i f(a)$$

---

**Step 3: Evaluate $f(a)$**
Substitute $a = -\frac{\pi}{2}$ into $f(z) = \sin 3z$:
$$f\left(-\frac{\pi}{2}\right) = \sin\left( 3 \left(-\frac{\pi}{2}\right) \right) = \sin\left( -\frac{3\pi}{2} \right)$$
Using the odd symmetry of the sine function ($\sin(-\theta) = -\sin\theta$):
$$f\left(-\frac{\pi}{2}\right) = -\sin\left(\frac{3\pi}{2}\right) = -(-1) = 1$$

---

**Step 4: Compute the Integral**
$$\oint_C \frac{\sin 3z}{z+\frac{\pi}{2}}\,dz = 2\pi i \cdot (1) = 2\pi i \quad \text{(Verified)}$$

---

### Q.9. Evaluate Exponential Integral

#### **Problem:**
Show that $\oint_C \frac{e^{tz}}{z^2+1}\,dz = 2\pi i \sin t$, where $C$ is the circle $\vert z \vert = 3$ and $t > 0$.

---

#### **Solution:**

**Step 1: Identify Singularities and Check Enclosure**
- Factorize the denominator:
  $$z^2 + 1 = 0 \implies z^2 = -1 \implies z = \pm i$$
- The contour is the circle $\vert z \vert = 3$.
- Moduli of the poles:
  $$\vert i \vert = 1 < 3 \quad \text{and} \quad \vert -i \vert = 1 < 3$$
  Both singularities $z = i$ and $z = -i$ lie **strictly inside** $C$.

---

**Step 2: Partial Fraction Decomposition**
Decompose $\frac{1}{z^2+1} = \frac{1}{(z-i)(z+i)}$ into partial fractions:
$$\frac{1}{(z-i)(z+i)} = \frac{A}{z-i} + \frac{B}{z+i}$$
$$1 = A(z+i) + B(z-i)$$
- Setting $z = i$: $1 = A(2i) \implies A = \frac{1}{2i}$
- Setting $z = -i$: $1 = B(-2i) \implies B = -\frac{1}{2i}$

Thus:
$$\frac{1}{z^2+1} = \frac{1}{2i}\left( \frac{1}{z-i} - \frac{1}{z+i} \right)$$

---

**Step 3: Split the Integral and Apply Cauchy's Integral Formula**
$$\oint_C \frac{e^{tz}}{z^2+1}\,dz = \frac{1}{2i} \oint_C \frac{e^{tz}}{z-i}\,dz - \frac{1}{2i} \oint_C \frac{e^{tz}}{z+i}\,dz$$

Let $f(z) = e^{tz}$, which is entire. Applying Cauchy's Integral Formula $\oint_C \frac{f(z)}{z-a}\,dz = 2\pi i f(a)$ to each term:
1. For $a = i$:
   $$\oint_C \frac{e^{tz}}{z-i}\,dz = 2\pi i f(i) = 2\pi i e^{it}$$
2. For $a = -i$:
   $$\oint_C \frac{e^{tz}}{z+i}\,dz = 2\pi i f(-i) = 2\pi i e^{-it}$$

---

**Step 4: Combine and Simplify**
$$I = \frac{1}{2i} (2\pi i e^{it}) - \frac{1}{2i} (2\pi i e^{-it}) = \pi (e^{it} - e^{-it})$$

Using Euler's identity $\sin t = \frac{e^{it} - e^{-it}}{2i} \implies e^{it} - e^{-it} = 2i\sin t$:
$$I = \pi (2i \sin t) = 2\pi i \sin t \quad \text{(Verified)}$$

---

### Q.10. Evaluate using Higher Derivatives

#### **Problem:**
Show that $\frac{1}{2\pi i}\oint_C \frac{z e^{tz}}{(z+1)^3}\,dz = \left(t - \frac{1}{2}t^2\right)e^{-t}$, where $C$ is a simple closed contour enclosing $z = -1$.

---

#### **Solution:**

**Step 1: State Cauchy's Formula for Higher Derivatives**
Cauchy's derivative formula states:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}}\,dz = \frac{2\pi i}{n!} f^{(n)}(a) \implies \frac{1}{2\pi i}\oint_C \frac{f(z)}{(z-a)^{n+1}}\,dz = \frac{f^{(n)}(a)}{n!}$$

---

**Step 2: Identify the Parameters**
- Integrand denominator: $(z+1)^3 = (z - (-1))^{2+1} \implies a = -1$ and $n = 2$.
- Numerator function: $f(z) = z e^{tz}$ (analytic everywhere).

---

**Step 3: Compute the Derivatives of $f(z) = z e^{tz}$**
1. **First Derivative $f'(z)$ (Product Rule):**
   $$f'(z) = \frac{d}{dz}(z) \cdot e^{tz} + z \cdot \frac{d}{dz}(e^{tz}) = 1 \cdot e^{tz} + z \cdot (t e^{tz}) = (1 + tz)e^{tz}$$

2. **Second Derivative $f''(z)$ (Product Rule again):**
   $$f''(z) = \frac{d}{dz}(1 + tz) \cdot e^{tz} + (1 + tz) \cdot \frac{d}{dz}(e^{tz})$$
   $$f''(z) = t \cdot e^{tz} + (1 + tz) \cdot (t e^{tz}) = (t + t + t^2 z)e^{tz} = (2t + t^2 z)e^{tz}$$

---

**Step 4: Evaluate the Derivative at $z = a = -1$**
$$f''(-1) = [2t + t^2(-1)]e^{t(-1)} = (2t - t^2)e^{-t}$$

---

**Step 5: Compute the Final Value**
$$\frac{1}{2\pi i}\oint_C \frac{z e^{tz}}{(z+1)^3}\,dz = \frac{f''(-1)}{2!} = \frac{(2t - t^2)e^{-t}}{2} = \left(t - \frac{1}{2}t^2\right)e^{-t} \quad \text{(Verified)}$$

---

### Q.11. Evaluate High Order Pole

#### **Problem:**
Show that $\oint_C \frac{e^{2z}}{(z+1)^4}\,dz = \frac{8\pi i e^{-2}}{3}$, where $C$ is the circle $\vert z \vert = 3$.

---

#### **Solution:**

**Step 1: Identify Parameters and Enclosure**
- Denominator: $(z+1)^4 = (z - (-1))^{3+1} \implies a = -1$ and $n = 3$.
- The pole is at $z = -1$.
- Enclosure test: $\vert -1 \vert = 1 < 3$, so $z = -1$ lies **strictly inside** $\vert z \vert = 3$.
- Numerator function: $f(z) = e^{2z}$ (entire).

---

**Step 2: Apply Cauchy's Generalized Integral Formula**
$$\oint_C \frac{f(z)}{(z-a)^{n+1}}\,dz = \frac{2\pi i}{n!} f^{(n)}(a)$$
For $n = 3$ and $a = -1$:
$$\oint_C \frac{e^{2z}}{(z+1)^4}\,dz = \frac{2\pi i}{3!} f'''(-1)$$

---

**Step 3: Compute the Successive Derivatives**
$$f(z) = e^{2z}$$
$$f'(z) = \frac{d}{dz}(e^{2z}) = 2e^{2z}$$
$$f''(z) = \frac{d}{dz}(2e^{2z}) = 4e^{2z}$$
$$f'''(z) = \frac{d}{dz}(4e^{2z}) = 8e^{2z}$$

---

**Step 4: Evaluate at $z = -1$ and Calculate the Integral**
$$f'''(-1) = 8e^{2(-1)} = 8e^{-2}$$
Substitute into the integral formula:
$$\oint_C \frac{e^{2z}}{(z+1)^4}\,dz = \frac{2\pi i}{6} \cdot (8e^{-2}) = \frac{\pi i}{3} \cdot 8e^{-2} = \frac{8\pi i e^{-2}}{3} \quad \text{(Verified)}$$

---

### Q.12. Evaluate Complex Rational Function

#### **Problem:**
Evaluate $\oint_C \frac{z\,dz}{(9-z^2)(z+i)}$ where $C$ is the circle $\vert z \vert = 2$.

---

#### **Solution:**

**Step 1: Factorize the Denominator and Locate All Poles**
The denominator is:
$$(9 - z^2)(z + i) = -(z^2 - 9)(z + i) = -(z - 3)(z + 3)(z + i)$$
Setting denominator to zero gives the poles:
$$z_1 = 3, \quad z_2 = -3, \quad z_3 = -i$$

---

**Step 2: Determine Which Poles Lie Inside the Contour $C$ ($\vert z \vert = 2$)**
1. $\vert z_1 \vert = \vert 3 \vert = 3 > 2 \implies z = 3$ is **outside** $C$.
2. $\vert z_2 \vert = \vert -3 \vert = 3 > 2 \implies z = -3$ is **outside** $C$.
3. $\vert z_3 \vert = \vert -i \vert = 1 < 2 \implies z = -i$ is **inside** $C$.

---

**Step 3: Express Integrand in Cauchy Form**
Rewrite the integrand so that all terms analytic inside $C$ are grouped into $f(z)$:
$$\frac{z}{(9-z^2)(z+i)} = \frac{\frac{z}{9-z^2}}{z - (-i)}$$
Let $f(z) = \frac{z}{9-z^2}$.
Since the singularities of $f(z)$ ($z = \pm 3$) lie entirely outside $C$, $f(z)$ is analytic inside and on $C$.

---

**Step 4: Apply Cauchy's Integral Formula**
$$\oint_C \frac{f(z)}{z - (-i)}\,dz = 2\pi i f(-i)$$

Calculate $f(-i)$:
$$f(-i) = \frac{-i}{9 - (-i)^2} = \frac{-i}{9 - (i^2)} = \frac{-i}{9 - (-1)} = \frac{-i}{9 + 1} = -\frac{i}{10}$$

---

**Step 5: Compute the Final Value**
$$\oint_C \frac{z\,dz}{(9-z^2)(z+i)} = 2\pi i \left( -\frac{i}{10} \right) = -2\pi \cdot \frac{i^2}{10} = -2\pi \cdot \frac{-1}{10} = \frac{2\pi}{10} = \frac{\pi}{5}$$

---

### Q.13. Evaluate Integral with Multiple Roots

#### **Problem:**
Evaluate $\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z-1)(z-2)}\,dz$, where $C$ is the circle $\vert z \vert = 3$.

---

#### **Solution:**

**Step 1: Check Poles and Enclosure**
- The denominator has roots at $z = 1$ and $z = 2$.
- Contour $C$ is $\vert z \vert = 3$.
- Since $\vert 1 \vert = 1 < 3$ and $\vert 2 \vert = 2 < 3$, **both poles** $z = 1$ and $z = 2$ lie strictly inside $C$.
- The numerator function $f(z) = \sin(\pi z^2) + \cos(\pi z^2)$ is analytic everywhere in $\mathbb{C}$.

---

**Step 2: Partial Fraction Decomposition**
$$\frac{1}{(z-1)(z-2)} = \frac{A}{z-1} + \frac{B}{z-2}$$
$$1 = A(z-2) + B(z-1)$$
- For $z = 1$: $1 = A(-1) \implies A = -1$
- For $z = 2$: $1 = B(1) \implies B = 1$

Therefore:
$$\frac{1}{(z-1)(z-2)} = \frac{1}{z-2} - \frac{1}{z-1}$$

---

**Step 3: Split the Contour Integral**
$$\oint_C \frac{f(z)}{(z-1)(z-2)}\,dz = \oint_C \frac{f(z)}{z-2}\,dz - \oint_C \frac{f(z)}{z-1}\,dz$$

Applying Cauchy's Integral Formula to each term:
$$\oint_C \frac{f(z)}{z-2}\,dz = 2\pi i f(2) \quad \text{and} \quad \oint_C \frac{f(z)}{z-1}\,dz = 2\pi i f(1)$$
$$\oint_C \frac{f(z)}{(z-1)(z-2)}\,dz = 2\pi i \Big[ f(2) - f(1) \Big]$$

---

**Step 4: Evaluate $f(1)$ and $f(2)$**
1. For $z = 1$:
   $$f(1) = \sin(\pi \cdot 1^2) + \cos(\pi \cdot 1^2) = \sin(\pi) + \cos(\pi) = 0 + (-1) = -1$$
2. For $z = 2$:
   $$f(2) = \sin(\pi \cdot 2^2) + \cos(\pi \cdot 2^2) = \sin(4\pi) + \cos(4\pi) = 0 + 1 = 1$$

---

**Step 5: Compute the Final Integral**
$$\oint_C \frac{f(z)}{(z-1)(z-2)}\,dz = 2\pi i \Big[ 1 - (-1) \Big] = 2\pi i (2) = 4\pi i$$

---
---

## Part 2: Singularities & Residue Calculus

---

### Problem-1: Find and Classify Singularities

#### **Problem:**
Find the singular points of $f(z) = \frac{z^2}{(z+1)^2} \sin\left(\frac{1}{z-1}\right)$ and determine their nature.

---

#### **Solution:**

A singularity occurs wherever $f(z)$ fails to be analytic. For this function:
1. The denominator vanishes at $z = -1$.
2. The argument of the sine function is undefined at $z = 1$.

---

**1. Analysis at $z = -1$:**
Consider the limit $\lim_{z \to -1} (z+1)^m f(z)$:
- For $m = 2$:
  $$\lim_{z \to -1} (z+1)^2 f(z) = \lim_{z \to -1} z^2 \sin\left(\frac{1}{z-1}\right) = (-1)^2 \sin\left(\frac{1}{-1-1}\right) = 1 \cdot \sin\left(-\frac{1}{2}\right) = -\sin\left(\frac{1}{2}\right)$$
- Since $-\sin(1/2)$ is a **non-zero, finite** number, by the definition of poles:
  $$\mathbf{z = -1} \text{ is a pole of order 2 (double pole)}.$$

---

**2. Analysis at $z = 1$:**
Consider the Laurent series expansion around $z = 1$.
The Taylor series for $\sin w$ is:
$$\sin w = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \frac{w^7}{7!} + \dots = \sum_{k=0}^\infty \frac{(-1)^k w^{2k+1}}{(2k+1)!}$$

Substituting $w = \frac{1}{z-1}$:
$$\sin\left(\frac{1}{z-1}\right) = \frac{1}{z-1} - \frac{1}{6(z-1)^3} + \frac{1}{120(z-1)^5} - \dots$$

The factor $\frac{z^2}{(z+1)^2}$ is analytic and non-zero at $z = 1$ (value is $\frac{1}{(1+1)^2} = \frac{1}{4}$). It has a regular Taylor series in powers of $(z-1)$:
$$\frac{z^2}{(z+1)^2} = \frac{1}{4} + c_1(z-1) + c_2(z-1)^2 + \dots$$

Multiplying the two series yields an expansion containing **infinitely many negative powers** of $(z-1)$:
$$f(z) = \dots + \frac{a_{-5}}{(z-1)^5} + \frac{a_{-3}}{(z-1)^3} + \frac{a_{-1}}{z-1} + a_0 + a_1(z-1) + \dots$$
Since the principal part (negative power terms) has infinitely many terms:
$$\mathbf{z = 1} \text{ is an isolated essential singularity}.$$

---

### Q.3 & Q.4: Cauchy's Residue Theorem and Formula for Poles

#### **1. Cauchy's Residue Theorem:**

**Statement:**
If $f(z)$ is analytic inside and on a simple closed contour $C$, except at a finite number of isolated singular points $z_1, z_2, \dots, z_k$ lying inside $C$, then:
$$\oint_C f(z)\,dz = 2\pi i \sum_{j=1}^k \operatorname{Res}(f, z_j)$$

**Derivation / Proof Outline:**
1. Enclose each singular point $z_j$ with a tiny disjoint circle $\gamma_j$ lying entirely inside $C$.
2. By the deformation principle for multi-connected domains:
   $$\oint_C f(z)\,dz = \sum_{j=1}^k \oint_{\gamma_j} f(z)\,dz$$
3. Around each isolated singularity $z_j$, $f(z)$ can be expanded in a Laurent series:
   $$f(z) = \sum_{n=0}^\infty a_n (z-z_j)^n + \sum_{n=1}^\infty \frac{b_n}{(z-z_j)^n}$$
4. Integrating term-by-term on $\gamma_j$:
   $$\oint_{\gamma_j} (z-z_j)^m\,dz = \begin{cases} 2\pi i, & m = -1 \\ 0, & m \neq -1 \end{cases}$$
5. Therefore, $\oint_{\gamma_j} f(z)\,dz = 2\pi i \cdot b_1 = 2\pi i \operatorname{Res}(f, z_j)$.
6. Summing over all $k$ singularities proves the theorem: $\oint_C f(z)\,dz = 2\pi i \sum_{j=1}^k \operatorname{Res}(f, z_j)$. $\blacksquare$

---

#### **2. Formula for Residue at a Pole of Order $m$:**

**Statement:**
If $f(z)$ has a pole of order $m$ at $z = a$, the residue is given by:
$$\operatorname{Res}(f, a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \Big[ (z-a)^m f(z) \Big]$$

**Proof:**
Since $f(z)$ has a pole of order $m$ at $z = a$, its Laurent series is:
$$f(z) = \frac{b_m}{(z-a)^m} + \frac{b_{m-1}}{(z-a)^{m-1}} + \dots + \frac{b_1}{z-a} + a_0 + a_1(z-a) + a_2(z-a)^2 + \dots$$
where $\operatorname{Res}(f, a) = b_1$.

1. Multiply both sides by $(z-a)^m$:
   $$(z-a)^m f(z) = b_m + b_{m-1}(z-a) + \dots + b_1(z-a)^{m-1} + a_0(z-a)^m + a_1(z-a)^{m+1} + \dots$$
2. Differentiate both sides $(m-1)$ times with respect to $z$:
   - All constant terms and terms with power $< (m-1)$ vanish.
   - The derivative of $b_1(z-a)^{m-1}$ is $b_1 (m-1)!$.
   - All subsequent terms retain at least one factor of $(z-a)$.
   $$\frac{d^{m-1}}{dz^{m-1}} \Big[ (z-a)^m f(z) \Big] = (m-1)! \, b_1 + \sum_{k=1}^\infty c_k (z-a)^k$$
3. Taking the limit as $z \to a$:
   $$\lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \Big[ (z-a)^m f(z) \Big] = (m-1)! \, b_1$$
4. Isolating $b_1$:
   $$b_1 = \operatorname{Res}(f, a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \Big[ (z-a)^m f(z) \Big] \quad \blacksquare$$

---

### Problem-5: Find the Residues

#### **Problem:**
Find the residues of $f(z) = \frac{z^2-2z}{(z+1)^2(z^2+4)}$ at all its poles.

---

#### **Solution:**

**Step 1: Identify all Poles and their Orders**
Set the denominator to zero:
1. $(z+1)^2 = 0 \implies z = -1$ is a **pole of order 2 (double pole)**.
2. $z^2 + 4 = 0 \implies z = \pm 2i$ are **simple poles (order 1)**.

---

**Step 2: Residue at the Double Pole $z = -1$ ($m = 2$)**
Using the pole formula:
$$\operatorname{Res}(f, -1) = \frac{1}{(2-1)!} \lim_{z \to -1} \frac{d}{dz} \left[ (z+1)^2 \frac{z^2-2z}{(z+1)^2(z^2+4)} \right] = \lim_{z \to -1} \frac{d}{dz} \left[ \frac{z^2-2z}{z^2+4} \right]$$

Apply the Quotient Rule $\frac{d}{dz}\left(\frac{u}{v}\right) = \frac{u'v - uv'}{v^2}$:
- $u = z^2 - 2z \implies u' = 2z - 2$
- $v = z^2 + 4 \implies v' = 2z$

$$\frac{d}{dz}\left( \frac{z^2-2z}{z^2+4} \right) = \frac{(z^2+4)(2z-2) - (z^2-2z)(2z)}{(z^2+4)^2}$$

Expand the numerator:
$$\text{Numerator} = (2z^3 - 2z^2 + 8z - 8) - (2z^3 - 4z^2) = 2z^3 - 2z^2 + 8z - 8 - 2z^3 + 4z^2 = 2z^2 + 8z - 8$$

Evaluate the limit at $z = -1$:
- $\text{Numerator}\vert_{z=-1} = 2(-1)^2 + 8(-1) - 8 = 2(1) - 8 - 8 = -14$
- $\text{Denominator}\vert_{z=-1} = ((-1)^2 + 4)^2 = (1 + 4)^2 = 5^2 = 25$

$$\operatorname{Res}(f, -1) = -\frac{14}{25}$$

---

**Step 3: Residue at the Simple Pole $z = 2i$ ($m = 1$)**
$$\operatorname{Res}(f, 2i) = \lim_{z \to 2i} (z-2i) f(z) = \lim_{z \to 2i} \frac{z^2-2z}{(z+1)^2(z+2i)}$$

Evaluate numerator and denominator at $z = 2i$:
- $\text{Numerator} = (2i)^2 - 2(2i) = 4i^2 - 4i = -4 - 4i = -4(1+i)$
- $(z+1)^2 = (2i+1)^2 = 4i^2 + 4i + 1 = -4 + 4i + 1 = -3 + 4i$
- $(z+2i) = 2i + 2i = 4i$
- $\text{Denominator} = (-3+4i)(4i) = -12i + 16i^2 = -16 - 12i = -4(4+3i)$

Form the fraction and simplify:
$$\operatorname{Res}(f, 2i) = \frac{-4(1+i)}{-4(4+3i)} = \frac{1+i}{4+3i}$$

Rationalize the denominator by multiplying by conjugate $(4-3i)$:
$$\operatorname{Res}(f, 2i) = \frac{(1+i)(4-3i)}{(4+3i)(4-3i)} = \frac{4 - 3i + 4i - 3i^2}{4^2 - (3i)^2} = \frac{4 + i - 3(-1)}{16 - (-9)} = \frac{7+i}{25}$$

---

**Step 4: Residue at the Simple Pole $z = -2i$ ($m = 1$)**
$$\operatorname{Res}(f, -2i) = \lim_{z \to -2i} (z+2i) f(z) = \lim_{z \to -2i} \frac{z^2-2z}{(z+1)^2(z-2i)}$$

Evaluate numerator and denominator at $z = -2i$:
- $\text{Numerator} = (-2i)^2 - 2(-2i) = -4 + 4i = -4(1-i)$
- $(z+1)^2 = (-2i+1)^2 = 1 - 4i - 4 = -3 - 4i$
- $(z-2i) = -2i - 2i = -4i$
- $\text{Denominator} = (-3-4i)(-4i) = 12i + 16i^2 = -16 + 12i = -4(4-3i)$

Form the fraction and rationalize:
$$\operatorname{Res}(f, -2i) = \frac{-4(1-i)}{-4(4-3i)} = \frac{1-i}{4-3i} = \frac{(1-i)(4+3i)}{(4-3i)(4+3i)} = \frac{4 + 3i - 4i - 3i^2}{16 + 9} = \frac{7-i}{25}$$

*(Note: Since all coefficients of $f(z)$ are real, $\operatorname{Res}(f, -2i) = \overline{\operatorname{Res}(f, 2i)} = \frac{7-i}{25}$, as expected).*

---

### Problem-6: Evaluate Integral using Residues

#### **Problem:**
Evaluate $\oint_C \frac{e^{tz}}{(z^2+1)^2}\,dz = \pi i (\sin t - t\cos t)$, where $C$ is the circle $\vert z \vert = 3$.

---

#### **Solution:**

**Step 1: Identify Singularities and Check Enclosure**
$$z^2 + 1 = 0 \implies z = \pm i \implies (z^2+1)^2 = (z-i)^2 (z+i)^2$$
- The function $f(z) = \frac{e^{tz}}{(z^2+1)^2}$ has two **poles of order 2 (double poles)** at $z = i$ and $z = -i$.
- Since $\vert i \vert = 1 < 3$ and $\vert -i \vert = 1 < 3$, **both poles** lie inside the circle $\vert z \vert = 3$.

---

**Step 2: Compute Residue at $z = i$ ($m = 2$)**
$$\operatorname{Res}(f, i) = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 \frac{e^{tz}}{(z-i)^2(z+i)^2} \right] = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{tz}}{(z+i)^2} \right]$$

Apply Quotient Rule:
$$\frac{d}{dz}\left[ \frac{e^{tz}}{(z+i)^2} \right] = \frac{(z+i)^2 (t e^{tz}) - e^{tz} \cdot 2(z+i)}{(z+i)^4} = \frac{(z+i)t e^{tz} - 2e^{tz}}{(z+i)^3}$$

Evaluate at $z = i$:
- $z + i = 2i$
- $(z+i)^3 = (2i)^3 = 8i^3 = -8i$
- Numerator $= (2i)t e^{it} - 2e^{it} = 2(it - 1)e^{it}$

$$\operatorname{Res}(f, i) = \frac{2(it - 1)e^{it}}{-8i} = \frac{(it - 1)e^{it}}{-4i} = \frac{(1 - it)e^{it}}{4i}$$
Multiply numerator and denominator by $i$:
$$\operatorname{Res}(f, i) = \frac{i(1 - it)e^{it}}{4i^2} = \frac{(i - i^2 t)e^{it}}{-4} = \frac{(i + t)e^{it}}{-4} = -\frac{t+i}{4}e^{it}$$

---

**Step 3: Compute Residue at $z = -i$ ($m = 2$)**
$$\operatorname{Res}(f, -i) = \lim_{z \to -i} \frac{d}{dz} \left[ \frac{e^{tz}}{(z-i)^2} \right] = \lim_{z \to -i} \frac{(z-i)t e^{tz} - 2e^{tz}}{(z-i)^3}$$

Evaluate at $z = -i$:
- $z - i = -2i$
- $(z-i)^3 = (-2i)^3 = -8i^3 = 8i$
- Numerator $= (-2i)t e^{-it} - 2e^{-it} = -2(it + 1)e^{-it}$

$$\operatorname{Res}(f, -i) = \frac{-2(it + 1)e^{-it}}{8i} = \frac{-(it + 1)e^{-it}}{4i}$$
Multiply numerator and denominator by $i$:
$$\operatorname{Res}(f, -i) = \frac{-i(it + 1)e^{-it}}{4i^2} = \frac{(-i^2 t - i)e^{-it}}{-4} = \frac{(t - i)e^{-it}}{-4} = -\frac{t-i}{4}e^{-it}$$

---

**Step 4: Sum of Residues**
$$\sum \operatorname{Res} = -\frac{t+i}{4}e^{it} - \frac{t-i}{4}e^{-it} = -\frac{t}{4}(e^{it} + e^{-it}) - \frac{i}{4}(e^{it} - e^{-it})$$

Using Euler's relations:
$$e^{it} + e^{-it} = 2\cos t \quad \text{and} \quad e^{it} - e^{-it} = 2i\sin t$$

Substitute these:
$$\sum \operatorname{Res} = -\frac{t}{4}(2\cos t) - \frac{i}{4}(2i\sin t) = -\frac{t\cos t}{2} - \frac{i^2 \sin t}{2} = -\frac{t\cos t}{2} + \frac{\sin t}{2} = \frac{\sin t - t\cos t}{2}$$

---

**Step 5: Apply Cauchy's Residue Theorem**
$$\oint_C \frac{e^{tz}}{(z^2+1)^2}\,dz = 2\pi i \sum \operatorname{Res} = 2\pi i \left( \frac{\sin t - t\cos t}{2} \right) = \pi i (\sin t - t\cos t) \quad \text{(Verified)}$$

---

### Problem-7: Evaluate Integral with $\pi$

#### **Problem:**
Evaluate $\oint_C \frac{e^z}{(z^2+\pi^2)^2}\,dz$ where $C$ is the circle $\vert z \vert = 4$.

---

#### **Solution:**

**Step 1: Identify Poles and Check Enclosure**
- The denominator factorizes as:
  $$(z^2 + \pi^2)^2 = (z - \pi i)^2 (z + \pi i)^2$$
- Poles are at $z = \pi i$ and $z = -\pi i$ (both are **poles of order 2**).
- Modulus check: $\vert \pm \pi i \vert = \pi \approx 3.1416 < 4$.
- Therefore, **both poles** lie inside the circle $\vert z \vert = 4$.

---

**Step 2: Residue at $z = \pi i$ ($m = 2$)**
$$\operatorname{Res}(f, \pi i) = \lim_{z \to \pi i} \frac{d}{dz}\left[ \frac{e^z}{(z+\pi i)^2} \right] = \lim_{z \to \pi i} \frac{(z+\pi i)e^z - 2e^z}{(z+\pi i)^3}$$

Evaluate at $z = \pi i$:
- $z + \pi i = 2\pi i$
- $(z+\pi i)^3 = (2\pi i)^3 = 8\pi^3 i^3 = -8\pi^3 i$
- $e^{\pi i} = \cos\pi + i\sin\pi = -1$
- Numerator $= (2\pi i)e^{\pi i} - 2e^{\pi i} = 2(\pi i - 1)(-1) = 2(1 - \pi i)$

$$\operatorname{Res}(f, \pi i) = \frac{2(1 - \pi i)}{-8\pi^3 i} = \frac{1 - \pi i}{-4\pi^3 i}$$
Multiply numerator and denominator by $i$:
$$\operatorname{Res}(f, \pi i) = \frac{i(1 - \pi i)}{-4\pi^3 i^2} = \frac{i - \pi i^2}{4\pi^3} = \frac{\pi + i}{4\pi^3}$$

---

**Step 3: Residue at $z = -\pi i$ ($m = 2$)**
$$\operatorname{Res}(f, -\pi i) = \lim_{z \to -\pi i} \frac{d}{dz}\left[ \frac{e^z}{(z-\pi i)^2} \right] = \lim_{z \to -\pi i} \frac{(z-\pi i)e^z - 2e^z}{(z-\pi i)^3}$$

Evaluate at $z = -\pi i$:
- $z - \pi i = -2\pi i$
- $(z-\pi i)^3 = (-2\pi i)^3 = -8\pi^3 i^3 = 8\pi^3 i$
- $e^{-\pi i} = -1$
- Numerator $= (-2\pi i)(-1) - 2(-1) = 2\pi i + 2 = 2(1 + \pi i)$

$$\operatorname{Res}(f, -\pi i) = \frac{2(1 + \pi i)}{8\pi^3 i} = \frac{1 + \pi i}{4\pi^3 i}$$
Multiply numerator and denominator by $-i$:
$$\operatorname{Res}(f, -\pi i) = \frac{-i(1 + \pi i)}{4\pi^3 (-i^2)} = \frac{-i - \pi i^2}{4\pi^3} = \frac{\pi - i}{4\pi^3}$$

---

**Step 4: Sum of Residues and Final Integration**
$$\sum \operatorname{Res} = \frac{\pi + i}{4\pi^3} + \frac{\pi - i}{4\pi^3} = \frac{2\pi}{4\pi^3} = \frac{1}{2\pi^2}$$

By Cauchy's Residue Theorem:
$$\oint_C \frac{e^z}{(z^2+\pi^2)^2}\,dz = 2\pi i \left( \frac{1}{2\pi^2} \right) = \frac{i}{\pi}$$

---

### Problem-9: Evaluate Simple Integral

#### **Problem:**
Evaluate $\oint_C \frac{e^{3z}}{z+\pi i}\,dz$, where $C$ is the circle $\vert z+1 \vert = 4$.

---

#### **Solution:**

**Step 1: Find Pole and Check Enclosure**
- Denominator root: $z + \pi i = 0 \implies z = -\pi i$ (simple pole).
- Contour $C$ is the circle centered at $z_0 = -1$ with radius $R = 4$: $\vert z - (-1) \vert = 4$.
- Compute the distance from the center $z_0 = -1$ to the pole $z = -\pi i$:
  $$\vert -\pi i - (-1) \vert = \vert 1 - \pi i \vert = \sqrt{1^2 + (-\pi)^2} = \sqrt{1 + \pi^2}$$
  Since $\pi \approx 3.14159 \implies \pi^2 \approx 9.8696$:
  $$\sqrt{1 + 9.8696} = \sqrt{10.8696} \approx 3.297 < 4$$
- The pole $z = -\pi i$ lies **strictly inside** the circle $C$.

---

**Step 2: Compute Residue at $z = -\pi i$**
$$\operatorname{Res}(f, -\pi i) = \lim_{z \to -\pi i} (z + \pi i) \frac{e^{3z}}{z+\pi i} = e^{3(-\pi i)} = e^{-3\pi i}$$

Using Euler's formula:
$$e^{-3\pi i} = \cos(-3\pi) + i\sin(-3\pi) = \cos(3\pi) - i\sin(3\pi) = -1 - i(0) = -1$$

---

**Step 3: Apply Residue Theorem**
$$\oint_C \frac{e^{3z}}{z+\pi i}\,dz = 2\pi i \cdot \operatorname{Res}(f, -\pi i) = 2\pi i (-1) = -2\pi i$$

---

### Problem-10: Evaluate over an Arbitrary Circle

#### **Problem:**
Evaluate $\oint_C \frac{e^{-iz}}{(z+3)(z-i)^2}\,dz$ where $C$ is the circle given by $z = 1 + 2e^{i\theta}, 0 \le \theta \le 2\pi$.

---

#### **Solution:**

**Step 1: Understand the Contour and Locate Poles**
- The equation $z = 1 + 2e^{i\theta}$ represents a circle centered at $z_0 = 1$ with radius $R = 2$: $\vert z - 1 \vert = 2$.
- The poles of the integrand are:
  1. $z = -3$ (simple pole).
  2. $z = i$ (double pole, order 2).

---

**Step 2: Test which Poles Lie Inside $C$**
1. **For $z = -3$:**
   $$\vert -3 - 1 \vert = \vert -4 \vert = 4 > 2 \implies z = -3 \text{ is OUTSIDE } C.$$
2. **For $z = i$:**
   $$\vert i - 1 \vert = \sqrt{(-1)^2 + 1^2} = \sqrt{2} \approx 1.414 < 2 \implies z = i \text{ is INSIDE } C.$$

Only the double pole $z = i$ contributes to the integral.

---

**Step 3: Compute the Residue at $z = i$ ($m = 2$)**
$$\operatorname{Res}(f, i) = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 \frac{e^{-iz}}{(z+3)(z-i)^2} \right] = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{-iz}}{z+3} \right]$$

Using Quotient Rule:
$$\frac{d}{dz}\left[ \frac{e^{-iz}}{z+3} \right] = \frac{(z+3) \frac{d}{dz}(e^{-iz}) - e^{-iz} \frac{d}{dz}(z+3)}{(z+3)^2} = \frac{(z+3)(-i e^{-iz}) - e^{-iz}(1)}{(z+3)^2}$$

Evaluate at $z = i$:
- $z + 3 = 3 + i$
- $e^{-iz} = e^{-i(i)} = e^{-i^2} = e^{-(-1)} = e^1 = e$
- Numerator $= (3+i)(-ie) - e = (-3ie - i^2 e) - e = -3ie - (-1)e - e = -3ie + e - e = -3ie$
- Denominator $= (3+i)^2 = 9 + 6i + i^2 = 9 + 6i - 1 = 8 + 6i$

$$\operatorname{Res}(f, i) = \frac{-3ie}{8 + 6i}$$

Rationalize the denominator by multiplying by $(8 - 6i)$:
$$\operatorname{Res}(f, i) = \frac{-3ie (8 - 6i)}{(8+6i)(8-6i)} = \frac{-24ie + 18i^2 e}{8^2 - (6i)^2} = \frac{-24ie - 18e}{64 - (-36)} = \frac{-(18 + 24i)e}{100}$$
Divide numerator and denominator by 2:
$$\operatorname{Res}(f, i) = -\frac{(9 + 12i)e}{50}$$

---

**Step 4: Compute the Integral by Residue Theorem**
$$\oint_C \frac{e^{-iz}}{(z+3)(z-i)^2}\,dz = 2\pi i \cdot \operatorname{Res}(f, i) = 2\pi i \left[ -\frac{(9+12i)e}{50} \right]$$
$$= -\frac{2\pi i (9 + 12i)e}{50} = -\frac{\pi i (9 + 12i)e}{25} = -\frac{\pi (9i + 12i^2)e}{25}$$
Since $i^2 = -1$:
$$= -\frac{\pi (9i - 12)e}{25} = \frac{\pi (12 - 9i)e}{25} = \frac{(12 - 9i)\pi e}{25}$$

---

### Problem-11: Evaluate Over Disjoint Domains

#### **Problem:**
Evaluate $\oint_C \frac{e^{3z}}{z-\pi i}\,dz$ where $C$ is:
1. The circle $\vert z-1 \vert = 4$
2. The ellipse $\vert z-2 \vert + \vert z+2 \vert = 6$

---

#### **Solution:**

**Singularity of the Integrand:**
The only singularity occurs at $z = \pi i$ (simple pole).

---

#### **Case (i): Contour is the circle $\vert z-1 \vert = 4$**

1. **Check Enclosure:**
   Center is $z_0 = 1$, radius is $R = 4$.
   Distance from center to the pole $z = \pi i$:
   $$\vert \pi i - 1 \vert = \sqrt{(-1)^2 + \pi^2} = \sqrt{1 + \pi^2} \approx 3.297 < 4$$
   The pole $z = \pi i$ lies **inside** the circle.

2. **Compute Residue at $z = \pi i$:**
   $$\operatorname{Res}(f, \pi i) = \lim_{z \to \pi i} (z - \pi i) \frac{e^{3z}}{z - \pi i} = e^{3\pi i} = \cos(3\pi) + i\sin(3\pi) = -1 + 0 = -1$$

3. **Compute Integral:**
   $$\oint_C \frac{e^{3z}}{z-\pi i}\,dz = 2\pi i \operatorname{Res}(f, \pi i) = 2\pi i (-1) = -2\pi i$$

---

#### **Case (ii): Contour is the ellipse $\vert z-2 \vert + \vert z+2 \vert = 6$**

1. **Geometric Properties of the Ellipse:**
   - The equation $\vert z - 2 \vert + \vert z + 2 \vert = 6$ represents an ellipse with foci at $F_1(2,0)$ and $F_2(-2,0)$ and major axis $2a = 6 \implies a = 3$.
   - Focal distance $c = 2$.
   - Semi-minor axis $b = \sqrt{a^2 - c^2} = \sqrt{3^2 - 2^2} = \sqrt{9-4} = \sqrt{5} \approx 2.236$.
   - In Cartesian coordinates, the equation is $\frac{x^2}{9} + \frac{y^2}{5} = 1$.

2. **Check if the pole $z = \pi i = (0, \pi)$ lies inside the ellipse:**
   - **Method A (Using sum of focal distances):**
     $$\vert \pi i - 2 \vert + \vert \pi i + 2 \vert = \sqrt{(-2)^2 + \pi^2} + \sqrt{2^2 + \pi^2} = 2\sqrt{4 + \pi^2}$$
     Since $\pi \approx 3.14159 \implies \pi^2 \approx 9.8696$:
     $$2\sqrt{4 + 9.8696} = 2\sqrt{13.8696} \approx 2(3.724) = 7.448 > 6$$
   - **Method B (Cartesian test):**
     $$\frac{0^2}{9} + \frac{\pi^2}{5} = \frac{9.8696}{5} \approx 1.974 > 1$$
   Since $7.448 > 6$ (and $1.974 > 1$), the pole $z = \pi i$ lies **strictly OUTSIDE** the ellipse.

3. **Compute Integral:**
   Since the integrand $\frac{e^{3z}}{z-\pi i}$ is analytic everywhere inside and on the ellipse $C$, by **Cauchy's Fundamental Theorem**:
   $$\oint_C \frac{e^{3z}}{z-\pi i}\,dz = 0$$

---

### Problem-12: Evaluate Over a Square

#### **Problem:**
Evaluate $\oint_C \frac{1}{(z^2+1)(z^2+9)}\,dz$ where $C$ is the square bounded by lines $x = \pm 2, y = \pm 2$.

---

#### **Solution:**

**Step 1: Factorize the Denominator and Locate All Poles**
$$(z^2+1)(z^2+9) = (z-i)(z+i)(z-3i)(z+3i)$$
The function has four simple poles:
$$z = \pm i \quad \text{and} \quad z = \pm 3i$$

---

**Step 2: Determine Enclosure inside the Square $C$**
The interior of the square $C$ is defined by:
$$-2 \le x \le 2 \quad \text{and} \quad -2 \le y \le 2$$

1. **For $z = i = (0, 1)$:** $x = 0 \in [-2, 2]$ and $y = 1 \in [-2, 2] \implies \mathbf{z = i \text{ is INSIDE } C}$.
2. **For $z = -i = (0, -1)$:** $x = 0 \in [-2, 2]$ and $y = -1 \in [-2, 2] \implies \mathbf{z = -i \text{ is INSIDE } C}$.
3. **For $z = 3i = (0, 3)$:** $y = 3 > 2 \implies \mathbf{z = 3i \text{ is OUTSIDE } C}$.
4. **For $z = -3i = (0, -3)$:** $y = -3 < -2 \implies \mathbf{z = -3i \text{ is OUTSIDE } C}$.

---

**Step 3: Compute Residue at $z = i$**
$$\operatorname{Res}(f, i) = \lim_{z \to i} (z-i) \frac{1}{(z-i)(z+i)(z^2+9)} = \frac{1}{(i+i)(i^2+9)} = \frac{1}{(2i)(-1+9)} = \frac{1}{(2i)(8)} = \frac{1}{16i}$$
Multiply numerator and denominator by $i$:
$$\operatorname{Res}(f, i) = \frac{i}{16i^2} = -\frac{i}{16}$$

---

**Step 4: Compute Residue at $z = -i$**
$$\operatorname{Res}(f, -i) = \lim_{z \to -i} (z+i) \frac{1}{(z^2+1)(z-3i)(z+3i)} = \lim_{z \to -i} \frac{1}{(z-i)(z^2+9)} = \frac{1}{(-i-i)((-i)^2+9)} = \frac{1}{(-2i)(-1+9)} = \frac{1}{-16i}$$
Multiply numerator and denominator by $i$:
$$\operatorname{Res}(f, -i) = \frac{i}{-16i^2} = \frac{i}{16}$$

---

**Step 5: Compute Sum of Residues and Final Integral**
$$\sum \operatorname{Res} = \operatorname{Res}(f, i) + \operatorname{Res}(f, -i) = -\frac{i}{16} + \frac{i}{16} = 0$$

Applying Cauchy's Residue Theorem:
$$\oint_C \frac{1}{(z^2+1)(z^2+9)}\,dz = 2\pi i \sum \operatorname{Res} = 2\pi i (0) = 0$$