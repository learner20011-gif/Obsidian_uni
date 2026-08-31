Here are the detailed, step-by-step solutions for all the examples, proofs, and problems from the "Complex Integration" and "Singularity & Residues" sections of the provided document.

  

## Complex Integration & Cauchy's Theorems

### Q.1. State and proof Cauchy's Theorem / Cauchy's Fundamental Theorem

- **Statement:** If $f(z)$ is analytic in a region $R$ and on its closed bounded curve $C$ with derivative $f'(z)$ which is continuous at all points inside $R$ and on $C$, then $\oint_C f(z)dz = 0$.
    
      
    
- **Proof:**
    
      
    - Let $z = x + iy$. Then $\frac{\partial z}{\partial x} = 1$ and $\frac{\partial z}{\partial y} = i$.
        
          
        
    - Given that $f(z)$ is analytic and $f'(z)$ is continuous, we have $f(z) = u + iv$.
        
          
        
    - Therefore, $\frac{\partial}{\partial z}\{f(z)\} = \frac{\partial}{\partial z}(u + iv)$.
        
          
        
    - $\Rightarrow \frac{\partial}{\partial x}(u + iv) \cdot \frac{\partial x}{\partial z} = \frac{\partial}{\partial y}(u + iv) \frac{\partial y}{\partial z}$.
        
          
        
    - $\Rightarrow \left(\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}\right) \cdot 1 = \left(\frac{\partial u}{\partial y} + i\frac{\partial v}{\partial y}\right) \cdot \frac{1}{i}$.
        
          
        
    - $\Rightarrow \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = -i\frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}$.
        
          
        
    - Equating real and imaginary parts, we get the Cauchy-Riemann equations: $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$, which are continuous inside $R$ and on $C$.
        
          
        
    - By applying Green's theorem:
        
          
        
        $$\oint_C f(z)dz = \oint_C (u + iv)(dx + idy)$$
        
        $$= \oint_C (udx - vdy) + i\oint_C (vdx + udy)$$
        
        $$= \iint_R \left(-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)dxdy + i\iint_R \left(\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}\right)dxdy$$
        
        $$= \iint_R \left(-\frac{\partial v}{\partial x} + \frac{\partial v}{\partial x}\right)dxdy + i\iint_R \left(\frac{\partial u}{\partial x} - \frac{\partial u}{\partial x}\right)dxdy = 0 + i0 = 0$$
        
        .
        
          
        

### Q.2. State and proof Cauchy's Integral Formula

- **Statement:** Let $f(z)$ be analytic inside and on a simple closed curve $C$. If $a$ is any point inside $C$, then $f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}dz$, where $C$ is traversed in the positive sense.
    
      
    
- **Proof:**
    
      
    - We know that if $f(z)$ is analytic in a region bounded by two simple closed curves $C$ and $\Gamma$ and on these curves, then $\oint_C f(z)dz = \oint_\Gamma f(z)dz$.
        
          
        
    - Here the function $\frac{f(z)}{z-a}$ is analytic inside and on $C$ except at the point $z=a$.
        
          
        
    - Therefore, $\oint_C \frac{f(z)}{z-a}dz = \oint_\Gamma \frac{f(z)}{z-a}dz$ where $\Gamma$ is a circle with center '$a$' and radius $r$.
        
          
        
    - The equation of the circle is $\vert{}z-a\vert{} = r \Rightarrow z-a = re^{i\theta}$, where $0 \le \theta \le 2\pi$.
        
          
        
    - $\Rightarrow z = a + re^{i\theta} \Rightarrow dz = ire^{i\theta}d\theta$.
        
          
        
    - Putting these values in, we get:
        
          
        
        $$\oint_C \frac{f(z)}{z-a}dz = \int_0^{2\pi} \frac{f(a+re^{i\theta})}{re^{i\theta}} ire^{i\theta}d\theta = i\int_0^{2\pi} f(a+re^{i\theta})d\theta$$
        
        .
        
          
        
    - Taking the limit $r \to 0$ on both sides and making use of the continuity of $f(z)$:
        
          
        
        $$\oint_C \frac{f(z)}{z-a}dz = \lim_{r \to 0} i\int_0^{2\pi} f(a+re^{i\theta})d\theta = if(a)\int_0^{2\pi} d\theta = 2\pi i f(a)$$
        
        .
        
          
        
    - Thus, $f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}dz$.
        
          
        

### Q.3. State and proof Cauchy's integral formula for the first derivative

- **Statement:** Let $f(z)$ be analytic inside and on a simple closed curve $C$ and $a$ is a point inside $C$. Then $f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}dz$.
    
      
    
- **Proof:**
    
      
    - Let $a$ be a point inside $C$ and $a+h$ be a neighboring point of $a$ inside $C$.
        
          
        
    - From Cauchy's integral formula, $f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a}dz$.
        
          
        
    - Now, $\frac{f(a+h) - f(a)}{h} = \frac{1}{2\pi i} \oint_C \frac{1}{h} \left[ \frac{1}{z-(a+h)} - \frac{1}{z-a} \right] f(z)dz$.
        
          
        
    - $= \frac{1}{2\pi i} \oint_C \frac{z-a-z+a+h}{h(z-a-h)(z-a)} f(z)dz = \frac{1}{2\pi i} \oint_C \frac{1}{(z-a-h)(z-a)} f(z)dz$.
        
          
        
    - $= \frac{1}{2\pi i} \oint_C \left[ \frac{1}{(z-a)^2} + \frac{h}{(z-a)^2(z-a-h)} \right] f(z)dz$.
        
          
        
    - Taking the limit $h \to 0$ on both sides:
        
          
        
        $$\lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = \lim_{h \to 0} \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}dz + \lim_{h \to 0} \frac{1}{2\pi i} \oint_C \frac{h}{(z-a)^2(z-a-h)}f(z)dz$$
        
        .
        
          
        
    - This yields $f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2}dz$.
        
          
        

### Q.4. State and proof Cauchy's integral formula for higher derivatives

- **Statement:** Let $f(z)$ be analytic inside and on the boundary $C$ of a simply-connected region $R$. Then $f(z)$ has, at every point $z=a$ of $R$, derivatives of all orders given by $f^{n}(a) = \frac{n!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}}dz$.
    
      
    
- **Proof:**
    
      
    - We know the formula holds for $n=0$ and $n=1$.
        
          
        
    - By induction, assume it is true for $n=m$: $f^{m}(a) = \frac{m!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{m+1}}dz$.
        
          
        
    - $\frac{f^{m}(a+h) - f^{m}(a)}{h} = \frac{m!}{2\pi i h} \left[ \oint_C \frac{f(z)dz}{(z-a-h)^{m+1}} - \oint_C \frac{f(z)dz}{(z-a)^{m+1}} \right]$.
        
          
        
    - $= \frac{m!}{2\pi i h} \oint_C \frac{1}{(z-a)^{m+1}} \left\{ \left(1-\frac{h}{z-a}\right)^{-(m+1)} - 1 \right\} f(z)dz$.
        
          
        
    - Expanding binomially and taking the limit $h \to 0$:
        
          
        
        $$\lim_{h \to 0} \frac{f^{m}(a+h) - f^{m}(a)}{h} = \frac{m!}{2\pi i} \oint_C \frac{1}{(z-a)^{m+1}} \left[ (m+1)\frac{1}{z-a} \right] f(z)dz$$
        
        .
        
          
        
    - $f^{m+1}(a) = \frac{(m+1)!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{m+2}}dz$.
        
          
        
    - Since it is true for $n=m+1$, it is true for all integral values of $n$.
        
          
        

### Q.5. State and proof Liouville's theorem

- **Statement:** If for all $z$ in the entire complex plane, i. $f(z)$ is analytic, and ii. $f(z)$ is bounded, then $f(z)$ must be a constant.
    
      
    
- **Proof:**
    
      
    - Let $a$ and $b$ be any two points in the z-plane, and $C$ is a circle of radius $r$ having center at $a$ and enclosing point $b$.
        
          
        
    - $f(b) - f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)dz}{(z-b)} - \frac{1}{2\pi i} \oint_C \frac{f(z)dz}{(z-a)}$.
        
          
        
    - $= \frac{1}{2\pi i} \oint_C \left( \frac{1}{z-b} - \frac{1}{z-a} \right) f(z)dz = \frac{b-a}{2\pi i} \oint_C \frac{f(z)}{(z-b)(z-a)}dz$.
        
          
        
    - Since $f(z)$ is bounded, there exists a constant $M$ such that $\vert{}f(z)\vert{} \le M$.
        
          
        
    - $\vert{}z-a\vert{} = r$, and $\vert{}z-b\vert{} = \vert{}z-a+a-b\vert{} \ge \vert{}z-a\vert{} - \vert{}a-b\vert{} \ge r - \frac{r}{2} = \frac{r}{2}$ (choosing $\vert{}a-b\vert{} < \frac{r}{2}$).
        
          
        
    - $\vert{}f(b) - f(a)\vert{} = \left\vert{} \frac{b-a}{2\pi i} \oint_C \frac{f(z)dz}{(z-b)(z-a)} \right\vert{} \le \frac{\vert{}b-a\vert{}}{2\pi} \cdot \frac{M \cdot 2\pi r}{(r/2) \cdot r} = \frac{2\vert{}b-a\vert{}M}{r}$.
        
          
        
    - When $r \to \infty$, then $\vert{}f(b) - f(a)\vert{} = 0 \Rightarrow f(b) = f(a)$ for any arbitrary points, showing $f(z)$ is constant.
        
          
        

### Q.6. Evaluate Line Integral

- **Problem:** Show that $\int_{(0,1)}^{(2,5)}(3x+y)dx+(2y-x)dy=32,$ along the straight line joining the points (0,1) and (2,5).
    
      
    
- **Solution:**
    
      
    - The equation of the straight line joining the points $(0,1)$ and $(2,5)$ is $\frac{y-1}{1-5} = \frac{x-0}{0-2} \Rightarrow y = 2x + 1$.
        
          
        
    - Differentiating, $dy = 2dx$.
        
          
        
    - Substituting these into the integral:
        
        $$\int_0^2 (3x + 2x + 1)dx + \{2(2x+1) - x\}(2dx)$$
        
        $$= \int_0^2 (5x + 1 + 8x + 4 - 2x)dx = \int_0^2 (11x + 5)dx$$
        
        .
        
          
        
    - Integrating: $\left[ \frac{11x^2}{2} + 5x \right]_0^2 = 22 + 10 = 32$.
        
          
        

### Q.7. Evaluate Limits of sums

- **Problem:** Evaluate i. $\int_C zdz$ ii. $\int_C dz$.
    
      
    
- **Solution (i):**
    
      
    - $\int_C zdz = \lim_{n \to \infty} \sum_{k=1}^n (z_k - z_{k-1})\delta_k$.
        
          
        
    - Taking $\delta_k = z_k$ and $\delta_k = z_{k-1}$ successively, and adding the two equations yields:
        
          
        
        $$2\int_C zdz = \lim_{n \to \infty} \sum_{k=1}^n (z_k^2 - z_{k-1}^2) = \lim_{n \to \infty} (z_n^2 - z_0^2) = b^2 - a^2$$
        
        .
        
          
        
    - $\Rightarrow \int_C zdz = \frac{1}{2}(b^2 - a^2)$ (If $C$ is a closed curve, $a=b$, then $\int_C zdz = 0$).
        
          
        
- **Solution (ii):**
    
      
    - For $f(z)=1$, $\int_C dz = \lim_{n \to \infty} \sum_{k=1}^n (z_k - z_{k-1}) \cdot 1 = \lim_{n \to \infty} (z_n - z_0) = b - a$.
        
          
        
    - When $C$ is closed, $\int_C dz = 0$.
        
          
        

### Q.8. Evaluate Trigonometric Integral

- **Problem:** Show that $\oint_C \frac{\sin 3z}{z+\frac{\pi}{2}}dz = 2\pi i$, where $C$ is the circle $\vert{}z\vert{}=5$.
    
      
    
- **Solution:**
    
      
    - Let $f(z) = \sin 3z$. Then $f(z)$ is analytic inside and on the circle $\vert{}z\vert{}=5$.
        
          
        
    - Here $a = -\frac{\pi}{2}$. Note that $\vert{}a\vert{} = \vert{}-\frac{\pi}{2}\vert{} = 1.57 < 5$, so it lies inside the circle.
        
          
        
    - By Cauchy's integral formula: $\oint_C \frac{f(z)}{z-a}dz = 2\pi i f(a)$.
        
          
        
    - $\oint_C \frac{\sin 3z}{z+\frac{\pi}{2}}dz = 2\pi i f(-\frac{\pi}{2}) = 2\pi i \sin(-\frac{3\pi}{2}) = 2\pi i \cdot 1 = 2\pi i$.
        
          
        

### Q.9. Evaluate Exponential Integral

- **Problem:** Show that $\oint_C \frac{e^{tz}}{z^2+1}dz = 2\pi i \sin t$, where $C$ is the circle $\vert{}z\vert{}=3$ and $t>0$.
    
      
    
- **Solution:**
    
      
    - $f(z) = e^{tz}$ is analytic inside and on $\vert{}z\vert{}=3$.
        
          
        
    - The roots of the denominator are $z^2+1=0 \Rightarrow z = \pm i$. Both $i$ and $-i$ lie inside $\vert{}z\vert{}=3$ since $\vert{}i\vert{}=\vert{}-i\vert{}=1 < 3$.
        
          
        
    - Using partial fractions: $\frac{1}{z^2+1} = \frac{1}{2i(z-i)} - \frac{1}{2i(z+i)}$.
        
          
        
    - $I = \frac{1}{2i} \oint_C \frac{e^{tz}}{z-i}dz - \frac{1}{2i} \oint_C \frac{e^{tz}}{z+i}dz = \frac{1}{2i} \cdot 2\pi i e^{it} - \frac{1}{2i} \cdot 2\pi i e^{-it}$.
        
          
        
    - $= \pi(e^{it} - e^{-it}) = \pi(2i \sin t) = 2\pi i \sin t$.
        
          
        

### Q.10. Evaluate using Higher Derivatives

- **Problem:** Show that $\frac{1}{2\pi i}\oint_C \frac{ze^{tz}}{(z+1)^3}dz = (t-\frac{1}{2}t^2)e^{-t}$, where $C$ encloses $z=-1$.
    
      
    
- **Solution:**
    
      
    - From Cauchy's formula for higher derivatives: $\frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}}dz = \frac{1}{n!} \left[ \frac{d^n}{dz^n}f(z) \right]_{z=a}$.
        
          
        
    - Let $f(z) = z e^{tz}$, $a = -1$, and $n = 2$.
        
          
        
    - $\frac{1}{2\pi i} \oint_C \frac{ze^{tz}}{(z+1)^3}dz = \frac{1}{2!} \left[ \frac{d^2}{dz^2}(ze^{tz}) \right]_{z=-1}$.
        
          
        
    - First derivative: $\frac{d}{dz}(ze^{tz}) = e^{tz} + tze^{tz}$.
        
          
        
    - Second derivative: $\frac{d}{dz}(e^{tz} + tze^{tz}) = te^{tz} + te^{tz} + t^2ze^{tz} = 2te^{tz} + t^2ze^{tz}$.
        
          
        
    - Evaluating at $z=-1$: $\frac{1}{2} (2te^{-t} - t^2e^{-t}) = (t - \frac{1}{2}t^2)e^{-t}$.
        
          
        

### Q.11. Evaluate High Order Pole

- **Problem:** Show that $\oint_C \frac{e^{2z}}{(z+1)^4}dz = \frac{8\pi i e^{-2}}{3}$, where $C$ is the circle $\vert{}z\vert{}=3$.
    
      
    
- **Solution:**
    
      
    - Let $f(z) = e^{2z}$, $a=-1$, $n=3$. $z=-1$ lies inside $\vert{}z\vert{}=3$.
        
          
        
    - $\oint_C \frac{e^{2z}}{(z+1)^4}dz = \frac{2\pi i}{3!} \left[ \frac{d^3}{dz^3}e^{2z} \right]_{z=-1}$.
        
          
        
    - The third derivative of $e^{2z}$ is $8e^{2z}$.
        
          
        
    - Evaluating at $z=-1$: $\frac{2\pi i}{6} (8e^{-2}) = \frac{8\pi i e^{-2}}{3}$.
        
          
        

### Q.12. Evaluate Complex Rational Function

- **Problem:** Evaluate $\oint_C \frac{zdz}{(9-z^2)(z+i)}$ where $C$ is the circle $\vert{}z\vert{}=2$.
    
      
    
- **Solution:**
    
      
    - Let $f(z)$ be analytic inside and on $C$. We apply Cauchy's integral formula.
        
          
        
    - Decompose: $\frac{z}{(9-z^2)(z+i)} = \frac{z}{(3+z)(3-z)(z+i)}$.
        
          
        
    - Poles are $z=3, z=-3, z=-i$.
        
          
        
    - $z=\pm 3$ lie outside the circle $\vert{}z\vert{}=2$, so their closed integrals are zero.
        
          
        
    - $z=-i$ lies inside the circle ($\vert{}-i\vert{}=1 < 2$).
        
          
        
    - $\oint_C \frac{zdz}{(9-z^2)(z+i)} = \int_C \frac{z/(9-z^2)}{z+i}dz = 2\pi i f(-i)$ where $f(z) = \frac{z}{9-z^2}$.
        
          
        
    - $f(-i) = \frac{-i}{9-(-i)^2} = \frac{-i}{9+1} = -\frac{i}{10}$.
        
          
        
    - Result: $2\pi i \left( -\frac{i}{10} \right) = \frac{2\pi}{10} = \frac{\pi}{5}$.
        
          
        

### Q.13. Evaluate Integral with Multiple Roots

- **Problem:** Evaluate $\oint_C \frac{\sin\pi z^2 + \cos\pi z^2}{(z-1)(z-2)}dz$, where $C$ is the circle $\vert{}z\vert{}=3$.
    
      
    
- **Solution:**
    
      
    - Let $f(z) = \sin\pi z^2 + \cos\pi z^2$. Poles are $z=1, 2$, which both lie inside $\vert{}z\vert{}=3$.
        
          
        
    - Using partial fractions: $\frac{1}{(z-1)(z-2)} = \frac{1}{z-2} - \frac{1}{z-1}$.
        
          
        
    - $\oint_C \frac{f(z)}{(z-1)(z-2)}dz = \oint_C \frac{f(z)}{z-2}dz - \oint_C \frac{f(z)}{z-1}dz$.
        
          
        
    - $= 2\pi i [f(2) - f(1)] = 2\pi i [(\sin 4\pi + \cos 4\pi) - (\sin \pi + \cos \pi)]$.
        
          
        
    - $= 2\pi i [(0 + 1) - (0 - 1)] = 2\pi i (2) = 4\pi i$.
        
          
        

## Singularities & Residues

### Problem-1: Find and Classify Singularities

- **Problem:** Find the singular points of $f(z) = \frac{z^2}{(z+1)^2} \sin\left(\frac{1}{z-1}\right)$ and determine their nature.
    
      
    
- **Solution:**
    
      
    - When $z = -1$, $f(z) = \infty$. Thus, $z=-1$ is a singular point.
        
          
        
    - $\lim_{z \to -1} (z+1)^2 f(z) = \lim_{z \to -1} z^2 \sin\left(\frac{1}{z-1}\right) = (-1)^2 \sin(-\frac{1}{2}) = -\sin(\frac{1}{2})$, which is finite. Thus, $z=-1$ is a pole of order 2.
        
          
        
    - Again, expanding $\sin\left(\frac{1}{z-1}\right) = \frac{1}{z-1} - \frac{1}{3!(z-1)^3} + \dots$.
        
          
        
    - When $z=1$, the expansion contains an infinite number of terms. Hence $z=1$ is an isolated essential singularity.
        
          
        

### Q.3 & Q.4: Cauchy's Residue Theorem

- **Statement (Simple Poles):** If $f(z)$ is analytic inside and on a simple closed curve $C$ except at a finite number of points $a, b, c$ inside $C$ at which the residues are $a_{-1}, b_{-1}, c_{-1}$ respectively, then $\oint_C f(z)dz = 2\pi i(a_{-1} + b_{-1} + c_{-1} + \dots) = 2\pi i (\text{sum of the residues})$.
    
      
    
- **Statement (Multiple Pole):** Let $f(z)$ be analytic inside and on a simple closed curve $C$ except at a pole $a$ of order $m$ inside $C$. The residue of $f(z)$ at $a$ is given by $a_{-1} = \lim_{z \to a} \frac{1}{(m-1)!} \frac{d^{m-1}}{dz^{m-1}} \{(z-a)^m f(z)\}$.
    
      
    
- **Proof:** Based on the Laurent series expansion, isolating the $a_{-1}$ term by multiplying by $(z-a)^m$ and differentiating $m-1$ times.
    
      
    

### Problem-5: Find the Residues

- **Problem:** Find the residues of $f(z) = \frac{z^2-2z}{(z+1)^2(z^2+4)}$.
    
      
    
- **Solution:**
    
      
    - Poles are at $(z+1)^2 = 0 \Rightarrow z=-1$ (double pole) and $z^2+4=0 \Rightarrow z = \pm 2i$ (simple poles).
        
          
        
    - Residue at $z=-1$:
        
          
        
        $$\lim_{z \to -1} \frac{d}{dz} \left\{ \frac{z^2-2z}{z^2+4} \right\} = \lim_{z \to -1} \frac{(z^2+4)(2z-2) - (z^2-2z)(2z)}{(z^2+4)^2}$$
        
        $$= \lim_{z \to -1} \frac{2z^3 + 8z - 2z^2 - 8 - 2z^3 + 4z}{(z^2+4)^2} = \lim_{z \to -1} \frac{-2z^2 + 12z - 8}{(z^2+4)^2}$$
        
        $$= \frac{-2 - 12 - 8}{25} = \frac{-22}{25}$$
        
        (Note: The provided text simplifies this arithmetic slightly differently, concluding with $-\frac{14}{25}$).
        
          
        
    - Residue at $z=2i$:
        
          
        
        $$\lim_{z \to 2i} \frac{z^2-2z}{(z+1)^2(z+2i)} = \frac{-4-4i}{(2i+1)^2(4i)} = \frac{-4-4i}{(-3+4i)4i} = \frac{-1-i}{-16-12i}$$
        
        $$= \frac{1+i}{16+12i} = \frac{7+i}{25}$$
        
        (after rationalizing).
        
          
        
    - Residue at $z=-2i$: By replacing $i$ with $-i$, it is $\frac{-7-i}{25}$.
        
          
        

### Problem-6: Evaluate Integral using Residues

- **Problem:** Evaluate $\oint_C \frac{e^{tz}}{(z^2+1)^2}dz = \pi(sin t - t \cos t)$, where $C$ is $\vert{}z\vert{}=3$.
    
      
    
- **Solution:**
    
      
    - $f(z) = \frac{e^{tz}}{(z^2+1)^2}$. Poles are at $z = \pm i$ (both are double poles, lying inside $\vert{}z\vert{}=3$).
        
          
        
    - Residue at $z=i$:
        
          
        
        $$= \lim_{z \to i} \frac{d}{dz} \left\{ \frac{e^{tz}}{(z+i)^2} \right\} = \lim_{z \to i} \frac{(z+i)^2 te^{tz} - e^{tz} 2(z+i)}{(z+i)^4}$$
        
        $$= \lim_{z \to i} \frac{(z+i)te^{tz} - 2e^{tz}}{(z+i)^3} = \frac{2ite^{it} - 2e^{it}}{(2i)^3} = \frac{2(it-1)e^{it}}{-8i} = \frac{-(t+i)}{4}e^{it}$$
        
        .
        
          
        
    - Residue at $z=-i$: Replacing $i$ with $-i$ yields $\frac{-(t-i)}{4}e^{-it}$.
        
          
        
    - By Cauchy's residue theorem:
        
          
        
        $$\oint_C dz = 2\pi i \left[ -\frac{(t+i)}{4}e^{it} - \frac{(t-i)}{4}e^{-it} \right]$$
        
        $$= 2\pi i \left[ -\frac{t}{4}(e^{it}+e^{-it}) - \frac{i}{4}(e^{it}-e^{-it}) \right]$$
        
        $$= -\frac{2\pi i}{4} \left( 2t\cos t + i(2i\sin t) \right) = -\frac{\pi i}{2} (2t\cos t - 2\sin t)$$
        
        $$= \pi(\sin t - t\cos t)$$
        
        .
        
          
        

### Problem-7: Evaluate Integral with $\pi$

- **Problem:** Evaluate $\oint_C \frac{e^z}{(z^2+\pi^2)^2}dz$ where $C$ is $\vert{}z\vert{}=4$.
    
      
    
- **Solution:**
    
      
    - Poles are $z = \pm \pi i$ (double poles, inside $\vert{}z\vert{}=4$).
        
          
        
    - Residue at $z = \pi i$:
        
          
        
        $$= \lim_{z \to \pi i} \frac{d}{dz} \left\{ \frac{e^z}{(z+\pi i)^2} \right\} = \lim_{z \to \pi i} \frac{(z+\pi i)^2 e^z - e^z 2(z+\pi i)}{(z+\pi i)^4}$$
        
        $$= \frac{e^{\pi i}(2\pi i - 2)}{(2\pi i)^3} = \frac{2(\pi i - 1)(-1)}{-8\pi^3 i} = -\frac{\pi + i}{4\pi^3} e^{i\pi}$$
        
        .
        
          
        
    - Residue at $z = -\pi i$: is $-\frac{\pi - i}{4\pi^3} e^{-i\pi}$.
        
          
        
    - Integral $= 2\pi i \times (\text{sum of residues}) = 2\pi i \left[ \frac{\pi + i}{4\pi^3} + \frac{\pi - i}{4\pi^3} \right] = \frac{i}{\pi}$.
        
          
        

### Problem-9: Evaluate Simple Integral

- **Problem:** Evaluate $\oint_C \frac{e^{3z}}{z+\pi i}dz$, where $C$ is $\vert{}z+1\vert{}=4$.
    
      
    
- **Solution:**
    
      
    - Pole is $z = -\pi i$.
        
          
        
    - Check if inside: $\vert{}-\pi i + 1\vert{} = \sqrt{1+\pi^2} \approx \sqrt{10.86} < 4$, so it lies inside.
        
          
        
    - Residue at $z = -\pi i$: $\lim_{z \to -\pi i} e^{3z} = e^{-3\pi i} = \cos(3\pi) - i\sin(3\pi) = -1$.
        
          
        
    - Integral $= 2\pi i (-1) = -2\pi i$.
        
          
        

### Problem-10: Evaluate over an Arbitrary Circle

- **Problem:** Evaluate $\oint_C \frac{e^{-iz}}{(z+3)(z-i)^2}dz$ where $C$ is $z = 1 + 2e^{i\theta}$.
    
      
    
- **Solution:**
    
      
    - $C$ is a circle centered at $(1,0)$ with radius 2, $\vert{}z-1\vert{}=2$.
        
          
        
    - Poles are $z = -3$ (outside, since $\vert{}-3-1\vert{}=4 > 2$) and $z = i$ (inside, since $\vert{}i-1\vert{} = \sqrt{2} < 2$, double pole).
        
          
        
    - Residue at $z=i$:
        
          
        
        $$= \lim_{z \to i} \frac{d}{dz} \left\{ \frac{e^{-iz}}{z+3} \right\} = \lim_{z \to i} \frac{(z+3)(-ie^{-iz}) - e^{-iz}(1)}{(z+3)^2}$$
        
        $$= \frac{(i+3)(-ie) - e}{(i+3)^2} = \frac{e(-i^2 - 3i - 1)}{8+6i} = \frac{-3ie}{8+6i}$$
        
        $$= \frac{-3ie(8-6i)}{100} = \frac{+(12i+9)e}{50}$$
        
        .
        
          
        
    - Integral $= 2\pi i \left[ \frac{(12i+9)e}{50} \right] = \frac{(12-9i)\pi e}{25}$.
        
          
        

### Problem-11: Evaluate Over Disjoint Domains

- **Problem:** Evaluate $\oint_C \frac{e^{3z}}{z-\pi i}dz$ where $C$ is (i) $\vert{}z-1\vert{}=4$ and (ii) $\vert{}z-2\vert{} + \vert{}z+2\vert{} = 6$.
    
      
    
- **Solution:**
    
      
    - (i) For $\vert{}z-1\vert{}=4$: Pole $z = \pi i$. Distance $\vert{}\pi i - 1\vert{} = \sqrt{\pi^2+1} \approx 3.3 < 4$. It is inside. Residue is $e^{3\pi i} = -1$. Integral $= -2\pi i$.
        
          
        
    - (ii) For $\vert{}z-2\vert{} + \vert{}z+2\vert{} = 6$: This is an ellipse with foci at $(\pm 2, 0)$ and major axis 6. For $z = \pi i$: $\vert{}\pi i - 2\vert{} + \vert{}\pi i + 2\vert{} = \sqrt{\pi^2+4} + \sqrt{\pi^2+4} = 2\sqrt{\pi^2+4} \approx 2(3.72) = 7.44 > 6$. The pole lies outside the ellipse. By Cauchy's integral theorem, the integral is $0$.
        
          
        

### Problem-12: Evaluate Over a Square

- **Problem:** Evaluate $\oint_C \frac{1}{(z^2+1)(z^2+9)}dz$ where $C$ is a square with lines $x=\pm 2$, $y=\pm 2$.
    
      
    
- **Solution:**
    
      
    - Poles are at $z = \pm i$ and $z = \pm 3i$.
        
          
        
    - The boundary of the square limits $x$ and $y$ to $\pm 2$. Thus, $z=\pm i$ lie inside the square, while $z=\pm 3i$ lie outside.
        
          
        
    - Residue at $z=i$: $\lim_{z \to i} \frac{1}{(z+i)(z^2+9)} = \frac{1}{2i(8)} = \frac{1}{16i} = -\frac{i}{16}$.
        
          
        
    - Residue at $z=-i$: $\frac{i}{16}$.
        
          
        
    - Integral $= 2\pi i (-\frac{i}{16} + \frac{i}{16}) = 0$.