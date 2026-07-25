# Complex Variables & Analysis — Master Lecture Notes (Page-by-Page Guide)

> [!NOTE]
> This master document presents a complete, page-by-page breakdown of the **Math 4: Complex Variables** lecture notes (Pages 1 through 27). Every page number is explicitly preserved, and all theoretical concepts, omitted mathematical steps, geometric figures/diagrams, and step-by-step problem solutions have been fully expanded and filled in.

---

## Page-by-Page Table of Contents

- [Page 1: Basic Concepts of Complex Variables](#page-1-basic-concepts-of-complex-variables)
- [Page 2: The Roots of Complex Numbers](#page-2-the-roots-of-complex-numbers)
- [Page 3: Polar Format, Square Roots, and Topology](#page-3-polar-format-square-roots-and-topology)
- [Page 4: Geometric Regions and Modulus Inequalities](#page-4-geometric-regions-and-modulus-inequalities)
- [Page 5: Proving the Triangle Inequality](#page-5-proving-the-triangle-inequality)
- [Page 6: Complex Functions (Single vs. Multi-Valued)](#page-6-complex-functions-single-vs-multi-valued)
- [Page 7: Analytic Functions, Singular Points, and Limits](#page-7-analytic-functions-singular-points-and-limits)
- [Page 8: Rigorous Definition of Complex Limits & Path Independence](#page-8-rigorous-definition-of-complex-limits--path-independence)
- [Page 9: Continuity, Differentiability, and Cauchy-Riemann Equations (Part 1)](#page-9-continuity-differentiability-and-cauchy-riemann-equations-part-1)
- [Page 10: Cauchy-Riemann Equations (Part 2) & Differentiability Homework](#page-10-cauchy-riemann-equations-part-2--differentiability-homework)
- [Page 11: Differentiability vs. Analyticity of $f(z) = |z|^2$ (Homework Solution - Part 1)](#page-11-differentiability-vs-analyticity-of-fz--z2-homework-solution---part-1)
- [Page 12: Concluding the $f(z) = |z|^2$ Proof via Paths & C-R Equations](#page-12-concluding-the-fz--z2-proof-via-paths--c-r-equations)
- [Page 13: Harmonic Functions, Laplace's Equation & Exact Differentials](#page-13-harmonic-functions-laplaces-equation--exact-differentials)
- [Page 14: Exact Differential Condition & Constant Modulus Theorem (Part 1)](#page-14-exact-differential-condition--constant-modulus-theorem-part-1)
- [Page 15: Concluding the Constant Modulus Theorem Proof](#page-15-concluding-the-constant-modulus-theorem-proof)
- [Page 16: Orthogonal Trajectories of Analytic Functions](#page-16-orthogonal-trajectories-of-analytic-functions)
- [Page 17: Proof that $u$ and $v$ are Harmonic Functions](#page-17-proof-that-u-and-v-are-harmonic-functions)
- [Page 18: Cauchy-Riemann Problems & Derivative Analysis](#page-18-cauchy-riemann-problems--derivative-analysis)
- [Page 19: Reconstructing Analytic Functions via Exact Differentials](#page-19-reconstructing-analytic-functions-via-exact-differentials)
- [Page 20: Harmonic Conjugates & Exact Differential Method](#page-20-harmonic-conjugates--exact-differential-method)
- [Page 21: Alternate Integration Method for Harmonic Conjugates](#page-21-alternate-integration-method-for-harmonic-conjugates)
- [Page 22: Derivation of the Milne-Thomson Shortcut Method](#page-22-derivation-of-the-milne-thomson-shortcut-method)
- [Page 23: Applying Milne-Thomson & The $u-v$ Problem (Part 1)](#page-23-applying-milne-thomson--the-u-v-problem-part-1)
- [Page 24: Conclusion of the $u-v$ Transformation Problem](#page-24-conclusion-of-the-u-v-transformation-problem)
- [Page 25: Complex Integration: Curves, Arcs, and Contours](#page-25-complex-integration-curves-arcs-and-contours)
- [Page 26: Complex Line Integrals & Cauchy's Integral Theorem](#page-26-complex-line-integrals--cauchys-integral-theorem)
- [Page 27: Rigorous Proof of Cauchy's Theorem via Green's Theorem](#page-27-rigorous-proof-of-cauchys-theorem-via-greens-theorem)

---

### **Page 1: Basic Concepts of Complex Variables**

**Overview:** Foundational definitions, representation, and core algebraic properties of complex numbers.

#### 1. Definitions
A complex number $z$ is an ordered pair of real numbers $(x,y)$ expressed as:
$$z = x + iy \quad \text{where } i = \sqrt{-1} \; (i^2 = -1)$$
- **Real Part:** $\text{Re}(z) = x \in \mathbb{R}$
- **Imaginary Part:** $\text{Im}(z) = y \in \mathbb{R}$ *(Note: $\text{Im}(z)$ is the real coefficient of $i$, not $iy$)*.
- **Complex Conjugate:** The conjugate $\bar{z}$ (or $z^*$) is formed by reflecting $z$ across the real axis:
  $$\bar{z} = x - iy$$

#### 2. Modulus and Argument
- **Modulus (Radius / Magnitude):** 
  $$r = |z| = \sqrt{x^2 + y^2} = \sqrt{z \cdot \bar{z}}$$
  $$|z|^2 = x^2 + y^2 = z \cdot \bar{z}$$
- **Argument (Phase Angle):**
  $$\theta = \arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$$
  - **Principal Argument $\text{Arg}(z)$:** The unique value of $\theta$ lying strictly in $(-\pi, \pi]$.
  - **General Argument $\arg(z)$:** $\arg(z) = \text{Arg}(z) + 2k\pi, \; k \in \mathbb{Z}$.

#### 3. Key Properties & Theorems
- **Equality:** $z_1 = z_2 \iff x_1 = x_2$ and $y_1 = y_2$.
- **De Moivre's Theorem:** For any $n \in \mathbb{R}$:
  $$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$
- **Argument Properties:**
  $$\text{Arg}(z_1 \cdot z_2) = \text{Arg}(z_1) + \text{Arg}(z_2)$$
  $$\text{Arg}\left(\frac{z_1}{z_2}\right) = \text{Arg}(z_1) - \text{Arg}(z_2)$$

#### 4. Euler's Formula & Polar Representation
$$e^{i\theta} = \cos\theta + i\sin\theta$$
$$z = r(\cos\theta + i\sin\theta) = r e^{i\theta}$$

*Figures involved:* None.

---

### **Page 2: The Roots of Complex Numbers**

**Overview:** Derivation of the general $n$-th root formula for complex numbers and a complete worked problem.

#### 1. General Formula for $n$-th Roots
If $w^n = z = r e^{i\theta}$, then $w$ has $n$ distinct complex roots $w_0, w_1, \dots, w_{n-1}$ given by:
$$w_k = z^{1/n} = r^{1/n} \left[ \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right] = r^{1/n} e^{i \frac{\theta + 2k\pi}{n}}$$
where $k = 0, 1, 2, \dots, n-1$. Geometrically, all $n$ roots lie on a circle of radius $r^{1/n}$ centered at the origin, spaced equally by angles of $\frac{2\pi}{n}$.

---

#### 2. Solved Example: Cube Roots ($n=3$) of $z = -1 + i$
**Problem:** Find all values of $(-1 + i)^{1/3}$.

**Step-by-Step Solution:**
1. **Identify Real & Imaginary Parts:** $x = -1, y = 1$.
2. **Calculate Modulus $r$:**
   $$r = \sqrt{(-1)^2 + 1^2} = \sqrt{2} = 2^{1/2}$$
3. **Calculate Principal Argument $\theta$:**
   Since $x < 0$ and $y > 0$, $z$ lies in Quadrant II:
   $$\theta = \text{Arg}(z) = \pi - \tan^{-1}\left(\frac{1}{1}\right) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$$
4. **Apply Root Formula for $n=3$:**
   $$w_k = (\sqrt{2})^{1/3} \left[ \cos\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) + i\sin\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) \right], \quad k = 0, 1, 2$$
   $$w_k = \sqrt[6]{2} \left[ \cos\left(\frac{3\pi + 8k\pi}{12}\right) + i\sin\left(\frac{3\pi + 8k\pi}{12}\right) \right]$$
5. **Evaluate Roots for each $k$:**
   - **For $k = 0$:**
     $$\theta_0 = \frac{3\pi}{12} = \frac{\pi}{4} \implies w_0 = \sqrt[6]{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right) = \sqrt[6]{2}\left(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right) = 2^{-1/3}(1 + i)$$
   - **For $k = 1$:**
     $$\theta_1 = \frac{3\pi + 8\pi}{12} = \frac{11\pi}{12} \implies w_1 = \sqrt[6]{2}\left(\cos\frac{11\pi}{12} + i\sin\frac{11\pi}{12}\right)$$
   - **For $k = 2$:**
     $$\theta_2 = \frac{3\pi + 16\pi}{12} = \frac{19\pi}{12} \equiv -\frac{5\pi}{12} \implies w_2 = \sqrt[6]{2}\left(\cos\frac{19\pi}{12} + i\sin\frac{19\pi}{12}\right)$$

*Figures involved:* None.

---

### **Page 3: Polar Format, Square Roots, and Topology**

**Overview:** Polar form conversions, algebraic methods for finding square roots without trigonometry, and foundational complex plane topology.

#### 1. Polar Conversion Example
Convert $z = 2 + 2\sqrt{3}i$ to polar form:
- $r = \sqrt{2^2 + (2\sqrt{3})^2} = \sqrt{4 + 12} = \sqrt{16} = 4$
- $\theta = \tan^{-1}\left(\frac{2\sqrt{3}}{2}\right) = \tan^{-1}(\sqrt{3}) = \frac{\pi}{3}$
- **Polar Form:** $z = 4\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right) = 4 e^{i\pi/3}$.

#### 2. Algebraic Method for Square Roots
Instead of trigonometry, we can solve $\sqrt{x+iy} = \pm(a+ib)$ using algebraic complete squares.

- **Example A: Square Root of $5 - 12i$**
  - *System Method:* Let $(a+ib)^2 = (a^2-b^2) + 2abi = 5-12i \implies a^2-b^2=5$ and $ab=-6$. Since $(a^2+b^2)^2 = (a^2-b^2)^2 + (2ab)^2 = 25+144=169 \implies a^2+b^2=13$. Thus $2a^2=18 \implies a=\pm 3, b=\mp 2$.
  - *Shortcut Factoring:* Rewrite $5 - 12i = 9 - 12i - 4 = 3^2 - 2(3)(2i) + (2i)^2 = (3 - 2i)^2$.
  - **Answer:** $\sqrt{5 - 12i} = \pm(3 - 2i)$.

- **Example B: Square Root of $-15 - 8i$**
  - *Shortcut Factoring:* Rewrite $-15 - 8i = 1 - 8i - 16 = 1^2 - 2(1)(4i) + (4i)^2 = (1 - 4i)^2$.
  - **Answer:** $\sqrt{-15 - 8i} = \pm(1 - 4i)$.

#### 3. Topological Definitions in $\mathbb{C}$
- **$\epsilon$-Neighborhood:** Open disk centered at $z_0$: $N(z_0, \epsilon) = \{ z \in \mathbb{C} : |z - z_0| < \epsilon \}$.
- **Interior Point:** A point $z_0 \in S$ whose neighborhood $N(z_0,\epsilon) \subset S$.
- **Boundary Point:** Every neighborhood of $z_0$ contains points inside $S$ and outside $S$.
- **Exterior Point:** A point with a neighborhood containing no points of $S$.

#### Figures Involved: Neighborhood Diagram
Hand-drawn circle centered at $z_0$ illustrating point classifications:
```
       +-----------------------------------------+
       |           Exterior Point (*)            |
       |                                         |
       |         ...- - - - - -...               |
       |       .   Boundary Point  .             |
       |      .         (o)         .            |
       |     .                       .           |
       |    .    Interior Point       .          |
       |    .         (•)             .          |
       |     .   Center z₀            .          |
       |      .                      .           |
       |       . . - - - - - - - . .             |
       +-----------------------------------------+
```

---

### **Page 4: Geometric Regions and Modulus Inequalities**

**Overview:** Graphing complex plane inequalities and Cartesian proof of modulus products.

#### 1. Geometric Region $1 < |z+i| \le 2$
Substitute $z = x + iy$:
$$z + i = x + i(y + 1) \implies |z + i| = \sqrt{x^2 + (y + 1)^2}$$
$$1 < \sqrt{x^2 + (y + 1)^2} \le 2 \implies 1^2 < x^2 + (y + 1)^2 \le 2^2$$

- **Center:** $(0, -1)$
- **Inner Boundary:** Circle of radius $r_1 = 1$. The strict inequality ($1 <$) excludes the inner boundary (dashed circle).
- **Outer Boundary:** Circle of radius $r_2 = 2$. The non-strict inequality ($\le 2$) includes the outer boundary (solid circle).
- **Geometric Region:** An **annulus** (ring shape) bounded between the two circles.

#### Figures Involved: Diagram of Annulus Region
```
                        y
                        |
            ... - - - - + - - - - ...        Outer Circle (r = 2, solid)
          .             |             .
        .       o - - - + - - - o       .    Inner Circle (r = 1, dashed)
       .      .         |         .      .
  ----+------+----------+----------+------+---- x
      .      .     Center (0,-1)   .      .
       .      .                   .      .
        .       o - - - - - - - o       .
          .                           .
            ... - - - - - - - - - ...
                        |
```

#### 2. Cartesian Proof of $|z_1 z_2| = |z_1| |z_2|$
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$.
$$z_1 z_2 = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + x_2 y_1)$$
$$|z_1 z_2|^2 = (x_1 x_2 - y_1 y_2)^2 + (x_1 y_2 + x_2 y_1)^2$$
$$= x_1^2 x_2^2 - 2x_1 x_2 y_1 y_2 + y_1^2 y_2^2 + x_1^2 y_2^2 + 2x_1 y_2 x_2 y_1 + x_2^2 y_1^2$$
$$= x_1^2 x_2^2 + y_1^2 y_2^2 + x_1^2 y_2^2 + x_2^2 y_1^2 = (x_1^2 + y_1^2)(x_2^2 + y_2^2) = |z_1|^2 |z_2|^2$$
Taking positive square root yields $|z_1 z_2| = |z_1| |z_2|$. $\blacksquare$

---

### **Page 5: Proving the Triangle Inequality**

**Overview:** Elegant proofs of modulus properties using the conjugate identity $|z|^2 = z\bar{z}$.

#### 1. Conjugate Proof of $|z_1 z_2| = |z_1||z_2|$
$$|z_1 z_2|^2 = (z_1 z_2)\overline{(z_1 z_2)} = (z_1 z_2)(\bar{z}_1 \bar{z}_2) = (z_1 \bar{z}_1)(z_2 \bar{z}_2) = |z_1|^2 |z_2|^2$$
Taking square root: $|z_1 z_2| = |z_1| |z_2|$. Generalizes to $n$ factors: $|z_1 z_2 \cdots z_n| = |z_1| |z_2| \cdots |z_n|$.

#### 2. Complete Proof of Triangle Inequality $|z_1 + z_2| \le |z_1| + |z_2|$
Using $|z|^2 = z \bar{z}$:
$$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = (z_1 + z_2)(\bar{z}_1 + \bar{z}_2)$$
$$= z_1 \bar{z}_1 + z_1 \bar{z}_2 + z_2 \bar{z}_1 + z_2 \bar{z}_2 = |z_1|^2 + z_1 \bar{z}_2 + \overline{(z_1 \bar{z}_2)} + |z_2|^2$$
Note that for any complex number $w$, $w + \bar{w} = 2\text{Re}(w)$. Letting $w = z_1 \bar{z}_2$:
$$|z_1 + z_2|^2 = |z_1|^2 + 2\text{Re}(z_1 \bar{z}_2) + |z_2|^2$$
Since $\text{Re}(w) \le |w|$ for all $w \in \mathbb{C}$:
$$\text{Re}(z_1 \bar{z}_2) \le |z_1 \bar{z}_2| = |z_1| |\bar{z}_2| = |z_1| |z_2|$$
Substituting this back:
$$|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = (|z_1| + |z_2|)^2$$
Taking positive square root of both sides:
$$|z_1 + z_2| \le |z_1| + |z_2| \quad \blacksquare$$

*Figures involved:* None.

---

### **Page 6: Complex Functions (Single vs. Multi-Valued)**

**Overview:** Subtraction inequality, definition of complex functions $w = u+iv$, and rigorous phase-rotation test for single-valuedness.

#### 1. Subtraction & Reverse Triangle Inequalities
- **Difference Inequality:** Replacing $z_2$ with $-z_2$ in the Triangle Inequality:
  $$|z_1 - z_2| \le |z_1| + |-z_2| = |z_1| + |z_2|$$
- **Reverse Triangle Inequality:** $|z_1 - z_2| \ge ||z_1| - |z_2||$.

#### 2. Complex Function Definition
A complex function $w = f(z)$ splits into real and imaginary parts:
$$w = f(z) = u(x,y) + i v(x,y)$$

#### 3. Single-Valued vs. Multi-Valued Functions
- **Single-Valued:** A $2\pi$ phase rotation ($\theta \to \theta + 2\pi$) leaves $f(z)$ unchanged.
- **Proof that $f(z) = z^2$ is Single-Valued:**
  Express $z = r e^{i\theta}$:
  $$f(z) = (r e^{i\theta})^2 = r^2 e^{i 2\theta}$$
  Rotate $\theta$ by $2\pi$:
  $$f(r e^{i(\theta + 2\pi)}) = r^2 e^{i 2(\theta + 2\pi)} = r^2 e^{i 2\theta + i 4\pi} = r^2 e^{i 2\theta} \cdot e^{i 4\pi}$$
  Since $e^{i 4\pi} = 1$:
  $$f(r e^{i(\theta + 2\pi)}) = r^2 e^{i 2\theta} = f(z)$$
  Hence, $f(z) = z^2$ is **single-valued**.

*Figures involved:* None.

---

### **Page 7: Analytic Functions, Singular Points, and Limits**

**Overview:** Proof of multi-valuedness, core calculus definitions, and geometric mapping of $\epsilon-\delta$ limits.

#### 1. Multi-Valued Function Example: $f(z) = z^{1/2}$
Express $z = r e^{i\theta} \implies f(z) = r^{1/2} e^{i\theta/2}$.
Rotate $\theta$ by $2\pi$:
$$f(r e^{i(\theta + 2\pi)}) = r^{1/2} e^{i(\theta + 2\pi)/2} = r^{1/2} e^{i\theta/2} e^{i\pi} = - r^{1/2} e^{i\theta/2} = -f(z) \neq f(z)$$
Because the output changes sign after one $2\pi$ rotation, $f(z) = z^{1/2}$ has 2 branches and is **multi-valued**.

#### 2. Calculus Definitions
- **Analytic (Holomorphic) Function:** $f(z)$ is analytic at $z_0$ if it is differentiable at $z_0$ and at all points in some neighborhood of $z_0$.
- **Singular Point:** A point where $f(z)$ fails to be differentiable.
- **Entire Function:** Analytic everywhere in $\mathbb{C}$ (e.g., polynomials, $e^z$).

#### Figures Involved: Limit Mapping ($z$-plane to $w$-plane)
1. Neighborhood circle around $z_0$.
2. $z$-plane showing $z_0$ enclosed in a $\delta$-disk.
3. $w$-plane ($u+iv$) showing $w_0$ enclosed in an $\epsilon$-disk:
```
       z-Plane (Input)                          w-Plane (Output)
         y                                         v
         |      . - - - .                          |      . - - - .
         |    .   δ-disk  .                        |    .   ε-disk  .
         |   .     (•)     .     f(z)              |   .     (•)     .
         |   .      z₀     .   --------->          |   .      w₀     .
         |    .           .                        |    .           .
         |      ' - - - '                          |      ' - - - '
  -------+------------------ x              -------+------------------ u
```

---

### **Page 8: Rigorous Definition of Complex Limits & Path Independence**

**Overview:** Formal $\epsilon-\delta$ limit definition, path independence rule, and proof of non-existent limit.

#### 1. Formal Limit Definition
$$\lim_{z \to z_0} f(z) = w_0 \iff \forall \epsilon > 0, \exists \delta > 0 : 0 < |z - z_0| < \delta \implies |f(z) - w_0| < \epsilon$$

> [!IMPORTANT]
> **Path Independence Principle:** A complex limit exists **if and only if** the limit value is identical along *every* possible path approaching $z_0$.

#### 2. Solved Problem: Non-Existence of $\lim_{z \to 0} \frac{\bar{z}}{z}$
Evaluate $f(z) = \frac{\bar{z}}{z} = \frac{x - iy}{x + iy}$ as $z \to 0$:
- **Path 1 (Real Axis, $y = 0, x \to 0$):** $\lim_{x \to 0} \frac{x}{x} = 1$.
- **Path 2 (Imaginary Axis, $x = 0, y \to 0$):** $\lim_{y \to 0} \frac{-iy}{iy} = -1$.
- **Path 3 (Line $y = mx$):** $\lim_{x \to 0} \frac{x(1-im)}{x(1+im)} = \frac{1-im}{1+im}$ (depends on slope $m$).

**Conclusion:** Since different paths yield different values ($1 \neq -1$), the limit **does not exist**.

*Figures involved:* None.

---

### **Page 9: Continuity, Differentiability, and Cauchy-Riemann Equations (Part 1)**

**Overview:** Definitions of continuity and derivative, and Part 1 of the Cauchy-Riemann equations proof along the real axis.

#### 1. Definitions
- **Continuous Function:** $\lim_{z \to z_0} f(z) = f(z_0)$.
- **Differentiable Function:** $f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$.

#### 2. Proof of Cauchy-Riemann (C-R) Equations — Part 1
Let $w = f(z) = u(x,y) + i v(x,y)$ be differentiable.
$$f'(z) = \lim_{\Delta z \to 0} \frac{[u(x+\Delta x, y+\Delta y) + i v(x+\Delta x, y+\Delta y)] - [u(x,y) + i v(x,y)]}{\Delta x + i \Delta y}$$

**Approach along Real Axis ($\Delta y = 0, \Delta z = \Delta x$):**
$$f'(z) = \lim_{\Delta x \to 0} \left[ \frac{u(x+\Delta x, y) - u(x,y)}{\Delta x} + i \frac{v(x+\Delta x, y) - v(x,y)}{\Delta x} \right]$$
$$f'(z) = \frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x} \quad \text{--- (Equation 1)}$$

*Figures involved:* None.

---

### **Page 10: Cauchy-Riemann Equations (Part 2) & Differentiability Homework**

**Overview:** Part 2 of C-R proof along the imaginary axis, equating paths, and homework assignment statement.

#### 1. Proof of Cauchy-Riemann (C-R) Equations — Part 2
**Approach along Imaginary Axis ($\Delta x = 0, \Delta z = i \Delta y$):**
$$f'(z) = \lim_{\Delta y \to 0} \left[ \frac{u(x, y+\Delta y) - u(x,y)}{i \Delta y} + i \frac{v(x, y+\Delta y) - v(x,y)}{i \Delta y} \right]$$
Multiply by $\frac{1}{i} = -i$:
$$f'(z) = \frac{1}{i} \frac{\partial u}{\partial y} + \frac{\partial v}{\partial y} = \frac{\partial v}{\partial y} - i \frac{\partial u}{\partial y} \quad \text{--- (Equation 2)}$$

#### 2. Equating Both Paths
Equating Real and Imaginary parts of Equation 1 and Equation 2:
$$\frac{\partial u}{\partial x} + i \frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i \frac{\partial u}{\partial y}$$
- **Real Part:** $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad (u_x = v_y)$
- **Imaginary Part:** $\frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y} \quad (u_y = -v_x)$

#### 3. Homework Problem Statement
*"Homework: Prove that $f(z) = |z|^2$ is continuous everywhere, differentiable at $z=0$, but not differentiable anywhere else (nowhere analytic)."*

*Figures involved:* None.

---

### **Page 11: Differentiability vs. Analyticity of $f(z) = |z|^2$ (Homework Solution - Part 1)**

**Overview:** Solving the homework from Page 10 for $z=0$ and setting up the limit at generic $z_0 \neq 0$.

#### 1. Differentiability at Origin ($z = 0$)
$$f'(0) = \lim_{\Delta z \to 0} \frac{|\Delta z|^2 - |0|^2}{\Delta z} = \lim_{\Delta z \to 0} \frac{\Delta z \cdot \overline{\Delta z}}{\Delta z} = \lim_{\Delta z \to 0} \overline{\Delta z} = 0$$
Since the limit exists uniquely ($=0$), $f(z)$ is **differentiable at $z = 0$**.

#### 2. Derivative at General Point $z_0 \neq 0$
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{|z_0 + \Delta z|^2 - |z_0|^2}{\Delta z} = \lim_{\Delta z \to 0} \frac{(z_0 + \Delta z)(\bar{z}_0 + \overline{\Delta z}) - z_0 \bar{z}_0}{\Delta z}$$
$$= \lim_{\Delta z \to 0} \left( \bar{z}_0 + z_0 \frac{\overline{\Delta z}}{\Delta z} + \overline{\Delta z} \right)$$
- **Path 1 ($\Delta y = 0 \implies \Delta z = \Delta x$):** $\frac{\overline{\Delta z}}{\Delta z} = 1 \implies \text{Limit} = \bar{z}_0 + z_0$.
- **Path 2 ($\Delta x = 0 \implies \Delta z = i\Delta y$):** $\frac{\overline{\Delta z}}{\Delta z} = -1 \implies \text{Limit} = \bar{z}_0 - z_0$.

*Figures involved:* None.

---

### **Page 12: Concluding the $f(z) = |z|^2$ Proof via Paths & C-R Equations**

**Overview:** Concluding non-differentiability for $z \neq 0$ via path dependence and alternate proof using C-R equations.

#### 1. Path Dependence Conclusion
Equating limits from Path 1 and Path 2:
$$\bar{z}_0 + z_0 = \bar{z}_0 - z_0 \implies 2z_0 = 0 \implies z_0 = 0$$
For any $z_0 \neq 0$, the limits along the two paths differ. Thus, $f'(z_0)$ **does not exist for $z \neq 0$**.

#### 2. Alternative Proof using Cauchy-Riemann Equations
$f(z) = |z|^2 = x^2 + y^2 + i(0) \implies u(x,y) = x^2 + y^2$ and $v(x,y) = 0$.
Compute partial derivatives:
$$u_x = 2x, \quad u_y = 2y, \quad v_x = 0, \quad v_y = 0$$
Apply C-R equations:
- $u_x = v_y \implies 2x = 0 \implies x = 0$
- $u_y = -v_x \implies 2y = 0 \implies y = 0$

C-R equations are satisfied **only at $(0,0)$**. Since analyticity requires differentiability in an open neighborhood around a point, $f(z) = |z|^2$ is **nowhere analytic**.

*Figures involved:* None.

---

### **Page 13: Harmonic Functions, Laplace's Equation & Exact Differentials**

**Overview:** Harmonic functions, harmonic conjugates, and review of exact differential equations.

#### 1. Harmonic Function Definition
A function $u(x,y)$ is **harmonic** if it satisfies **Laplace's Equation**:
$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 \quad \left(u_{xx} + u_{yy} = 0\right)$$
- *Example:* $u = x^2 - y^2 \implies u_{xx} = 2, u_{yy} = -2 \implies 2 + (-2) = 0$ (Harmonic).

#### 2. Harmonic Conjugate
If $f(z) = u + iv$ is analytic, $v(x,y)$ is called the **harmonic conjugate** of $u(x,y)$.

#### 3. Exact Differential Equations Review
Review of exact differential equations $M(x,y)dx + N(x,y)dy = 0$.

*Figures involved:* None.

---

### **Page 14: Exact Differential Condition & Constant Modulus Theorem (Part 1)**

**Overview:** Condition for exactness and Part 1 of the Constant Modulus Theorem proof.

#### 1. Exactness Condition
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

#### 2. Theorem: Analytic Function with Constant Modulus is Constant (Part 1)
**Statement:** If $f(z) = u + iv$ is analytic and $|f(z)| = c$ (constant), then $f(z)$ is constant.

**Proof:**
$$|f(z)|^2 = u^2 + v^2 = c^2$$
Differentiate with respect to $x$ and $y$:
1. w.r.t $x$: $2u u_x + 2v v_x = 0 \implies u u_x + v v_x = 0 \quad \text{--- (Eq 1)}$
2. w.r.t $y$: $2u u_y + 2v v_y = 0 \implies u u_y + v v_y = 0$
Apply C-R equations ($u_y = -v_x$ and $v_y = u_x$):
$$u(-v_x) + v(u_x) = 0 \implies -u v_x + v u_x = 0 \quad \text{--- (Eq 2)}$$

*Figures involved:* None.

---

### **Page 15: Concluding the Constant Modulus Theorem Proof**

**Overview:** Completing the proof that an analytic function with constant modulus must be constant.

#### Conclusion of Proof
Square equations (Eq 1) and (Eq 2) from Page 14 and add them together:
$$(u u_x + v v_x)^2 + (-u v_x + v u_x)^2 = 0$$
$$u^2 u_x^2 + 2uv u_x v_x + v^2 v_x^2 + u^2 v_x^2 - 2uv u_x v_x + v^2 u_x^2 = 0$$
$$(u^2 + v^2)(u_x^2 + v_x^2) = 0$$
Since $u^2 + v^2 = c^2 \neq 0$:
$$u_x^2 + v_x^2 = 0 \implies u_x = 0 \quad \text{and} \quad v_x = 0$$
By C-R, $v_y = u_x = 0$ and $u_y = -v_x = 0$.
Thus $f'(z) = u_x + i v_x = 0$. Integrating gives $f(z) = \text{constant}$. $\blacksquare$

*Figures involved:* None.

---

### **Page 16: Orthogonal Trajectories of Analytic Functions**

**Overview:** Proof that level curves $u(x,y)=c_1$ and $v(x,y)=c_2$ of an analytic function intersect at right angles.

#### Proof of Orthogonality
Let $u(x,y) = c_1$ and $v(x,y) = c_2$.
Total differentials:
1. $du = u_x dx + u_y dy = 0 \implies m_1 = \left.\frac{dy}{dx}\right|_{u=c_1} = -\frac{u_x}{u_y}$
2. $dv = v_x dx + v_y dy = 0 \implies m_2 = \left.\frac{dy}{dx}\right|_{v=c_2} = -\frac{v_x}{v_y}$

Multiply slopes:
$$m_1 \cdot m_2 = \left(-\frac{u_x}{u_y}\right)\left(-\frac{v_x}{v_y}\right) = \frac{u_x v_x}{u_y v_y}$$
Apply C-R equations ($v_x = -u_y$ and $v_y = u_x$):
$$m_1 \cdot m_2 = \frac{u_x (-u_y)}{u_y (u_x)} = -1$$
Since the product of their slopes is $-1$, the level curves are **orthogonal**. $\blacksquare$

*Figures involved:* None.

---

### **Page 17: Proof that $u$ and $v$ are Harmonic Functions**

**Overview:** Proof that the real and imaginary components of any analytic function satisfy Laplace's equation.

#### 1. Proof for $u(x,y)$
Start with C-R: $u_x = v_y$ and $u_y = -v_x$.
- Differentiate $u_x = v_y$ w.r.t $x$: $u_{xx} = v_{yx}$.
- Differentiate $u_y = -v_x$ w.r.t $y$: $u_{yy} = -v_{xy}$.

Assuming continuous second partial derivatives (Clairaut's Theorem $v_{yx} = v_{xy}$):
$$u_{xx} + u_{yy} = v_{yx} - v_{xy} = 0 \implies \nabla^2 u = 0 \quad \text{(u is harmonic)}$$

#### 2. Proof for $v(x,y)$
- Differentiate $u_x = v_y$ w.r.t $y$: $u_{xy} = v_{yy}$.
- Differentiate $u_y = -v_x$ w.r.t $x$: $u_{yx} = -v_{xx} \implies v_{xx} = -u_{yx}$.

$$v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0 \implies \nabla^2 v = 0 \quad \text{(v is harmonic)} \quad \blacksquare$$

*Figures involved:* None.

---

### **Page 18: Cauchy-Riemann Problems & Derivative Analysis**

**Overview:** Worked problems on testing C-R equations and setting up derivative integrals.

#### Worked Problem 1
**Show $f(z) = z^2 + 5iz + 3 - i$ satisfies C-R equations.**
Substitute $z = x + iy$:
$$f(z) = (x^2 - y^2 - 5y + 3) + i(2xy + 5x - 1)$$
$$u = x^2 - y^2 - 5y + 3 \implies u_x = 2x, \; u_y = -2y - 5$$
$$v = 2xy + 5x - 1 \implies v_x = 2y + 5, \; v_y = 2x$$
$u_x = v_y = 2x$ and $u_y = -v_x = -2y-5$. C-R satisfied everywhere (Entire function).

#### Worked Problem 2 (Setup)
**Find analytic $f(z)$ given $\text{Im}\{f'(z)\} = V(x,y) = 6xy + 4x$, $f'(0) = 0$, $f(1+i) = 0$.**
Let $w = f'(z) = U + iV$. Since $f(z)$ is analytic, $f'(z)$ is analytic, so $U$ and $V$ satisfy C-R:
$$U_x = V_y = 6x \quad \text{and} \quad U_y = -V_x = -6y - 4$$

*Figures involved:* None.

---

### **Page 19: Reconstructing Analytic Functions via Exact Differentials**

**Overview:** Concluding Worked Problem 2 using exact differentials to reconstruct $f(z)$.

#### Solution to Problem 2 (Continued)
Total differential $dU = U_x dx + U_y dy = 6x dx - (6y + 4) dy$.
Integrating $U$:
$$U(x,y) = 3x^2 - 3y^2 - 4y + C$$
Form $f'(z) = U + iV$:
$$f'(z) = (3x^2 - 3y^2 - 4y + C) + i(6xy + 4x) = 3z^2 + 4iz + C$$
Apply $f'(0) = 0 \implies C = 0 \implies f'(z) = 3z^2 + 4iz$.
Integrate $f'(z)$:
$$f(z) = z^3 + 2iz^2 + D$$
Apply $f(1+i) = 0$:
$$(1+i)^3 + 2i(1+i)^2 + D = (-2 + 2i) + (-4) + D = 0 \implies D = 6 - 2i$$
$$\therefore f(z) = z^3 + 2iz^2 + (6 - 2i)$$

*Figures involved:* None.

---

### **Page 20: Harmonic Conjugates & Exact Differential Method**

**Overview:** Proving harmonicity of $u$ and finding harmonic conjugate $v$ via exact differential $dv = -u_y dx + u_x dy$.

#### Worked Problem 3
**Prove $u = x^2 - y^2 - 2xy - 2x + 3y$ is harmonic, find $v$, and construct $f(z)$.**

1. **Harmonic Proof:** $u_{xx} = 2, u_{yy} = -2 \implies 2 + (-2) = 0$. (Harmonic!).
2. **Finding $v$ (Exact Differential):**
   $$dv = -u_y dx + u_x dy = -(-2x - 2y + 3) dx + (2x - 2y - 2) dy$$
   $$dv = (2x + 2y - 3) dx + (2x - 2y - 2) dy$$
   Check exactness ($M = 2x+2y-3, N = 2x-2y-2$):
   $$\frac{\partial M}{\partial y} = 2, \quad \frac{\partial N}{\partial x} = 2 \quad \text{(Exact!)}$$
   Integrating: $v = \int (2x + 2y - 3) dx + \int (-2y - 2) dy$.

*Figures involved:* None.

---

### **Page 21: Alternate Integration Method for Harmonic Conjugates**

**Overview:** Evaluating $v$ from Page 20 and demonstrating an alternate step-by-step partial integration method.

#### 1. Evaluation of $v$ & $f(z)$
$$v = x^2 + 2xy - 3x - y^2 - 2y + c$$
$$f(z) = u + iv = z^2(1+i) - z(2+3i) + K$$

#### 2. Alternate Method for Finding $v$
Integrate $v_y = u_x = 2x - 2y - 2$ with respect to $y$:
$$v(x,y) = 2xy - y^2 - 2y + F(x)$$
Differentiate with respect to $x$:
$$v_x = 2y + F'(x)$$
Apply C-R ($v_x = -u_y = 2x + 2y - 3$):
$$2y + F'(x) = 2x + 2y - 3 \implies F'(x) = 2x - 3 \implies F(x) = x^2 - 3x + c$$
Substituting $F(x)$ back yields $v = x^2 + 2xy - 3x - y^2 - 2y + c$.

*Figures involved:* None.

---

### **Page 22: Derivation of the Milne-Thomson Shortcut Method**

**Overview:** Full theoretical derivation of the Milne-Thomson Method to bypass finding $v$.

#### Milne-Thomson Derivation
Express $x$ and $y$ in terms of $z$ and $\bar{z}$:
$$x = \frac{z + \bar{z}}{2}, \quad y = \frac{z - \bar{z}}{2i}$$
Evaluate on the real axis ($y = 0 \implies z = \bar{z}$):
$$x = z, \quad y = 0$$
Since $f'(z) = u_x + i v_x = u_x - i u_y$ (by C-R):
$$\mathbf{f'(z) = u_x(z, 0) - i u_y(z, 0)}$$
Similarly, if $v(x,y)$ is given:
$$\mathbf{f'(z) = v_y(z, 0) + i v_x(z, 0)}$$

*Figures involved:* None.

---

### **Page 23: Applying Milne-Thomson & The $u-v$ Problem (Part 1)**

**Overview:** Applying Milne-Thomson to Problem 3 and setting up the $u-v$ linear combination trick problem.

#### 1. Milne-Thomson on Problem 3
Given $u = x^2 - y^2 - 2xy - 2x + 3y$:
- $u_x(z,0) = 2z - 2$
- $u_y(z,0) = -2z + 3$
$$f'(z) = (2z - 2) - i(-2z + 3) = 2z(1+i) - (2+3i)$$
Integrating: $f(z) = z^2(1+i) - z(2+3i) + K$. (Bypasses finding $v$!).

#### 2. Problem 4 Setup: Given $u - v = e^x(\cos y - \sin y)$
Multiply $f(z) = u + iv$ by $i \implies i f(z) = -v + iu$.
Add together: $(1+i)f(z) = (u-v) + i(u+v)$.
Define auxiliary analytic function $F(z) = (1+i)f(z) = U + iV$, where $U = u - v = e^x(\cos y - \sin y)$.

*Figures involved:* None.

---

### **Page 24: Conclusion of the $u-v$ Transformation Problem**

**Overview:** Completing Problem 4 using Milne-Thomson on the auxiliary function $F(z)$.

#### Solution to Problem 4 (Continued)
Apply Milne-Thomson to $F(z)$: $F'(z) = U_x(z,0) - i U_y(z,0)$.
- $U_x(x,y) = e^x(\cos y - \sin y) \implies U_x(z,0) = e^z$
- $U_y(x,y) = e^x(-\sin y - \cos y) \implies U_y(z,0) = -e^z$

$$F'(z) = e^z - i(-e^z) = (1 + i)e^z$$
Integrating $F'(z)$:
$$F(z) = (1 + i)e^z + C$$
Substitute back $F(z) = (1+i)f(z)$:
$$(1 + i)f(z) = (1 + i)e^z + C \implies f(z) = e^z + \frac{C}{1+i} = e^z + c_0 \quad \blacksquare$$

*Figures involved:* None.

---

### **Page 25: Complex Integration: Curves, Arcs, and Contours**

**Overview:** Definitions of curves, arcs, and contours required for complex integration.

#### 1. Definitions
- **Continuous Curve (Arc):** $z(t) = x(t) + i y(t), \; t \in [a,b]$.
- **Closed Curve:** $z(a) = z(b)$.
- **Closed Contour:** A simple closed curve differentiable everywhere (smooth) except possibly at a finite number of corners.

#### Figures Involved: 6 Diagrams
1. Closed generic curve bounding region $D$.
2. Continuous arc on Cartesian axes.
3. Generic closed loop.
4. Cardioid contour $r = a(1 - \cos\theta)$.
5. Astroid contour $x^{2/3} + y^{2/3} = a^{2/3}$.
6. Contour with sharp corners (corners marked as non-differentiable).

```
   Astroid Contour (x²/³ + y²/³ = a²/³)          Cardioid Contour
              y                                        y
              |                                        |
            . | .                                   .  |  .
          .   |   .                              .     |     .
  -------+----+----+------- x             ------+------+------+------ x
          .   |   .                              .     |     .
            . | .                                   .  |  .
              |                                        |
```

---

### **Page 26: Complex Line Integrals & Cauchy's Integral Theorem**

**Overview:** Definition of line integrals as Riemann sums and statement of Cauchy's Theorem.

#### 1. Complex Line Integral
$$\int_C f(z) dz = \lim_{n \to \infty} \sum_{k=1}^n f(\zeta_k)(z_k - z_{k-1}) = \int_C (udx - vdy) + i \int_C (vdx + udy)$$

#### 2. Cauchy's Fundamental Theorem Statement
If $f(z)$ is analytic in a simply connected domain $R$ and on its simple closed boundary $C$, then:
$$\oint_C f(z) dz = 0$$

#### Figures Involved: 2 Diagrams
1. Curve $C$ partitioned into discrete segments ($z_0, z_1, \dots, z_k$).
2. Region $R$ enclosed by closed boundary curve $C$.

---

### **Page 27: Rigorous Proof of Cauchy's Theorem via Green's Theorem**

**Overview:** Complete proof of Cauchy's Theorem combining complex integrals with Green's Theorem in the plane.

#### Proof of Cauchy's Theorem
$$\oint_C f(z) dz = \oint_C (u dx - v dy) + i \oint_C (v dx + u dy)$$

Recall Green's Theorem: $\oint_C (M dx + N dy) = \iint_R \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) dx dy$.

1. **Real Line Integral $\oint_C (u dx - v dy)$:**
   Set $M = u, N = -v$:
   $$\oint_C (u dx - v dy) = \iint_R \left( -\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} \right) dx dy$$
   Apply C-R equation $u_y = -v_x$:
   $$\iint_R \left( -v_x - (-v_x) \right) dx dy = \iint_R 0 \, dx dy = 0$$

2. **Imaginary Line Integral $\oint_C (v dx + u dy)$:**
   Set $M = v, N = u$:
   $$\oint_C (v dx + u dy) = \iint_R \left( \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \right) dx dy$$
   Apply C-R equation $u_x = v_y$:
   $$\iint_R \left( v_y - v_y \right) dx dy = \iint_R 0 \, dx dy = 0$$

**Conclusion:**
$$\oint_C f(z) dz = 0 + i(0) = 0 \quad \blacksquare$$

*Figures involved:* None.