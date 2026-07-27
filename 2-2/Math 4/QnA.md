Here are the detailed solutions for the first four questions from the provided document.

### Q1. Pg 1, Q1(a): Find two complex numbers whose sum is 4 and whose product is 8.

**Solution:**

Let the two unknown complex numbers be $z_1$ and $z_2$. According to the given conditions, we have:
1) $z_1 + z_2 = 4$
2) $z_1 \cdot z_2 = 8$

We know that any two numbers having a given sum and product can be considered as the roots of a quadratic equation. The standard form of such a quadratic equation in terms of a variable $z$ is:
$$z^2 - (\text{Sum of roots})z + (\text{Product of roots}) = 0$$

Substituting the given values into the equation:
$$z^2 - 4z + 8 = 0$$

Now, we solve for $z$ using the quadratic formula, where $a=1$, $b=-4$, and $c=8$:
$$z = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
$$z = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(8)}}{2(1)}$$
$$z = \frac{4 \pm \sqrt{16 - 32}}{2}$$
$$z = \frac{4 \pm \sqrt{-16}}{2}$$

Since $\sqrt{-16} = \sqrt{16 \cdot (-1)} = 4i$:
$$z = \frac{4 \pm 4i}{2} = 2 \pm 2i$$

Thus, the two roots are $2 + 2i$ and $2 - 2i$. 

**Answer:** The two complex numbers are **$2 + 2i$** and **$2 - 2i$**.

***

### Q2. Pg 1, Q1(c): Find the acute angle between the vectors $z_1 = 3-4i$ and $z_2 = -4+3i$.

**Solution:**

We can treat the complex numbers as geometric vectors in the 2D Cartesian plane (the Argand plane).
The vectors are:
$\vec{v_1} = (3, -4)$ representing $z_1$
$\vec{v_2} = (-4, 3)$ representing $z_2$

The angle $\theta$ between two vectors can be found using the dot product formula:
$$\cos \theta = \frac{\vec{v_1} \cdot \vec{v_2}}{|\vec{v_1}| |\vec{v_2}|}$$

**Step 1: Calculate the dot product.**
$$\vec{v_1} \cdot \vec{v_2} = (3)(-4) + (-4)(3) = -12 - 12 = -24$$

*(Note: In complex numbers, the dot product is equivalent to the real part of $z_1\bar{z}_2$. $\text{Re}((3-4i)(-4-3i)) = \text{Re}(-12 - 9i + 16i - 12) = \text{Re}(-24+7i) = -24$.)*

**Step 2: Calculate the magnitudes of the vectors.**
$$|\vec{v_1}| = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
$$|\vec{v_2}| = \sqrt{(-4)^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$$

**Step 3: Calculate the angle $\theta$.**
$$\cos \theta = \frac{-24}{(5)(5)} = -\frac{24}{25}$$
$$\theta = \cos^{-1}\left(-\frac{24}{25}\right) \approx 163.74^\circ$$

**Step 4: Find the acute angle.**
Because the cosine is negative, the angle $\theta$ between the vectors is obtuse (greater than $90^\circ$). The question specifically asks for the *acute* angle between their corresponding lines of action. 
The acute angle $\alpha$ is found by subtracting the obtuse angle from $180^\circ$ (or $\pi$ radians):
$$\alpha = 180^\circ - \theta$$
Alternatively, the acute angle satisfies $\cos \alpha = |\cos \theta| = \frac{24}{25}$.
$$\alpha = \cos^{-1}\left(\frac{24}{25}\right) \approx 16.26^\circ$$

**Answer:** The acute angle between the vectors is **$\cos^{-1}\left(\frac{24}{25}\right)$** or approximately **$16.26^\circ$**.

***

### Q3. Pg 2, Q1(a): Find the value of $\sqrt{i} + \sqrt{-i}$.

**Solution:**

Let the given expression be $x = \sqrt{i} + \sqrt{-i}$. We can solve this algebraically by squaring both sides or by using De Moivre's formula (polar form). 

**Method 1: Algebraic Method**
Square the expression:
$$x^2 = (\sqrt{i} + \sqrt{-i})^2$$
$$x^2 = (\sqrt{i})^2 + (\sqrt{-i})^2 + 2\sqrt{i}\sqrt{-i}$$
$$x^2 = i + (-i) + 2\sqrt{i \cdot (-i)}$$
$$x^2 = 0 + 2\sqrt{-i^2}$$
Since $i^2 = -1$, we have $-i^2 = 1$:
$$x^2 = 2\sqrt{1}$$

The square root of 1 has two possible values: $1$ and $-1$.
*   **Case 1 (Principal branch where $\sqrt{1} = 1$):**
    $$x^2 = 2(1) = 2 \implies x = \pm\sqrt{2}$$
*   **Case 2 (Secondary branch where $\sqrt{1} = -1$):**
    $$x^2 = 2(-1) = -2 \implies x = \pm\sqrt{-2} = \pm i\sqrt{2}$$

**Method 2: Polar Form (Principal Values)**
Let's find the principal roots explicitly. 
In polar form, $i = e^{i\pi/2}$ and $-i = e^{-i\pi/2}$.
Taking the principal square root (halving the angle):
$$\sqrt{i} = \left(e^{i\pi/2}\right)^{1/2} = e^{i\pi/4} = \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$$

$$\sqrt{-i} = \left(e^{-i\pi/2}\right)^{1/2} = e^{-i\pi/4} = \cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right) = \frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$$

Now, add the two principal roots together:
$$x = \left(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right) + \left(\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}\right)$$
$$x = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} = \frac{2}{\sqrt{2}} = \sqrt{2}$$

If we mix and match the primary and secondary roots of $\sqrt{i}$ (which are $\pm e^{i\pi/4}$) and $\sqrt{-i}$ (which are $\pm e^{-i\pi/4}$), we retrieve the four values found in Method 1: $\sqrt{2}$, $-\sqrt{2}$, $i\sqrt{2}$, and $-i\sqrt{2}$. The principal value is $\sqrt{2}$.

**Answer:** The principal value is **$\sqrt{2}$**. The set of all possible values considering different branches of the square roots is **$\{\sqrt{2}, -\sqrt{2}, i\sqrt{2}, -i\sqrt{2}\}$**.

***

### Q4. Pg 2, Q1(b): Represent graphically the set of values of z for which $\left|\frac{z-3}{z+3}\right| = 2$.

**Solution:**

Let the complex number be $z = x + iy$. Substitute this into the given equation:
$$\left|\frac{(x+iy)-3}{(x+iy)+3}\right| = 2$$

Using the property of modulus $\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$:
$$\frac{|(x-3) + iy|}{|(x+3) + iy|} = 2$$

Multiply both sides by the denominator:
$$|(x-3) + iy| = 2 |(x+3) + iy|$$

Square both sides to remove the square root of the modulus ($|a+ib|^2 = a^2 + b^2$):
$$(x-3)^2 + y^2 = 4 \left[ (x+3)^2 + y^2 \right]$$

Now, expand the binomials:
$$(x^2 - 6x + 9) + y^2 = 4 \left( x^2 + 6x + 9 + y^2 \right)$$
$$x^2 - 6x + 9 + y^2 = 4x^2 + 24x + 36 + 4y^2$$

Group all terms on one side to bring it to a standard polynomial equation form:
$$4x^2 - x^2 + 4y^2 - y^2 + 24x + 6x + 36 - 9 = 0$$
$$3x^2 + 3y^2 + 30x + 27 = 0$$

Divide the entire equation by 3 to simplify:
$$x^2 + y^2 + 10x + 9 = 0$$

Now, complete the square for the $x$ terms to identify the geometric shape:
$$(x^2 + 10x) + y^2 = -9$$
$$(x^2 + 10x + 25) + y^2 = -9 + 25$$
$$(x + 5)^2 + y^2 = 16$$
$$(x + 5)^2 + (y - 0)^2 = 4^2$$

This is the standard equation of a circle, $(x-h)^2 + (y-k)^2 = r^2$.
*   **Center:** $(h, k) = (-5, 0)$
*   **Radius:** $r = \sqrt{16} = 4$

**Graphical Representation:**
To represent this graphically on the complex plane (Argand diagram):
1.  Draw the real (Re) and imaginary (Im) axes.
2.  Mark the center of the circle at the point $-5$ on the real axis (coordinate $(-5, 0)$).
3.  Draw a circle with a radius of $4$ units around this center.
4.  The circle will intersect the real axis at $x = -5 + 4 = -1$ and $x = -5 - 4 = -9$. 
5.  It will peak on the vertical directions at $(-5, 4i)$ and $(-5, -4i)$.

**Answer:** The equation represents a **circle** in the complex plane with its center at **$z = -5$** (or $(-5, 0)$) and a radius of **$4$

### Q5. Pg 2, Q1(c): State and prove DeMoivre's theorem.

**Statement:**
De Moivre's Theorem states that for any real number $\theta$ and any integer $n$, the following identity holds:
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

**Proof (Using Exponential Form $e^{i\theta}$ / Euler's Formula):**

**Step 1: Euler's Formula**
By Euler's formula, any complex expression $(\cos\theta + i\sin\theta)$ can be written in exponential form as:
$$e^{i\theta} = \cos \theta + i \sin \theta$$

**Step 2: Exponentiation of Left-Hand Side (LHS)**
Substituting Euler's formula into the LHS of De Moivre's identity:
$$\text{LHS} = (\cos \theta + i \sin \theta)^n = \left(e^{i\theta}\right)^n$$

**Step 3: Applying Laws of Exponents**
Using the law of indices $(e^a)^b = e^{ab}$:
$$\left(e^{i\theta}\right)^n = e^{i(n\theta)}$$

**Step 4: Re-applying Euler's Formula to Right-Hand Side (RHS)**
Applying Euler's formula with angle $\phi = n\theta$:
$$e^{i(n\theta)} = \cos(n\theta) + i \sin(n\theta) = \text{RHS}$$

---

**Case Analysis for any Integer $n$:**

1. **For Positive Integer ($n > 0$):**
   $$\left(e^{i\theta}\right)^n = \underbrace{e^{i\theta} \cdot e^{i\theta} \cdots e^{i\theta}}_{n \text{ times}} = e^{i(\overbrace{\theta + \theta + \dots + \theta}^{n \text{ times}})} = e^{i(n\theta)} = \cos(n\theta) + i\sin(n\theta)$$

2. **For Zero ($n = 0$):**
   $$\text{LHS} = (\cos \theta + i \sin \theta)^0 = 1$$
   $$\text{RHS} = e^{i(0\cdot\theta)} = e^0 = 1 = \cos(0) + i \sin(0) = 1$$

3. **For Negative Integer ($n < 0$):**
   Let $n = -m$ where $m$ is a positive integer ($m > 0$).
   $$\text{LHS} = (\cos \theta + i \sin \theta)^n = (e^{i\theta})^{-m} = \frac{1}{(e^{i\theta})^m} = \frac{1}{e^{im\theta}} = e^{-im\theta}$$
   Substituting $-m = n$:
   $$= e^{i(n\theta)} = \cos(n\theta) + i \sin(n\theta) = \text{RHS}$$

**Conclusion:** 
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$ 
for all integers $n$. **(Proved)**

***

### Q6. Pg 4, Q1(b): Find the roots of $z = (-1 + i)^{\frac{1}{3}}$ and locate these roots in the complex plane.

**Solution:**

We need to find the three cube roots of the complex number $w = -1 + i$. 

**Step 1: Express $w = -1 + i$ in polar form.**
Let $w = x + iy$, so $x = -1$ and $y = 1$.
*   **Modulus ($r$):** 
    $r = |w| = \sqrt{(-1)^2 + 1^2} = \sqrt{1 + 1} = \sqrt{2}$
*   **Argument ($\theta$):** 
    Since $x$ is negative and $y$ is positive, the point lies in the second quadrant. 
    $\theta = \pi + \tan^{-1}\left(\frac{y}{x}\right) = \pi + \tan^{-1}(-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$

So, the polar form of $w$ is:
$$w = \sqrt{2} \left( \cos \frac{3\pi}{4} + i \sin \frac{3\pi}{4} \right)$$
Using the general argument $\theta + 2k\pi$:
$$w = 2^{1/2} \left[ \cos\left(\frac{3\pi}{4} + 2k\pi\right) + i\sin\left(\frac{3\pi}{4} + 2k\pi\right) \right]$$

**Step 2: Apply De Moivre's Theorem for roots.**
$$z = w^{1/3} = \left( 2^{1/2} \right)^{1/3} \left[ \cos\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) + i\sin\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) \right]$$
The magnitude of all roots will be $R = 2^{1/6}$.
The angles will be $\alpha_k = \frac{\pi}{4} + \frac{2k\pi}{3}$ for $k = 0, 1, 2$.

**Step 3: Calculate the individual roots.**
*   **For $k = 0$:**
    $$\alpha_0 = \frac{3\pi/4}{3} = \frac{\pi}{4}$$
    $$z_0 = 2^{1/6} \left( \cos\frac{\pi}{4} + i\sin\frac{\pi}{4} \right)$$
*   **For $k = 1$:**
    $$\alpha_1 = \frac{\frac{3\pi}{4} + 2\pi}{3} = \frac{\frac{11\pi}{4}}{3} = \frac{11\pi}{12}$$
    $$z_1 = 2^{1/6} \left( \cos\frac{11\pi}{12} + i\sin\frac{11\pi}{12} \right)$$
*   **For $k = 2$:**
    $$\alpha_2 = \frac{\frac{3\pi}{4} + 4\pi}{3} = \frac{\frac{19\pi}{4}}{3} = \frac{19\pi}{12}$$
    $$z_2 = 2^{1/6} \left( \cos\frac{19\pi}{12} + i\sin\frac{19\pi}{12} \right)$$

**Graphical Location:**
In the complex plane, the three roots $z_0, z_1,$ and $z_2$ lie on the circumference of a circle centered at the origin $(0,0)$ with a radius of $2^{1/6} \approx 1.122$. 
They form the vertices of an equilateral triangle inscribed inside this circle, spaced equally by $120^\circ$ ($\frac{2\pi}{3}$ radians). 
*   $z_0$ is in the 1st quadrant at an angle of $45^\circ$ ($\frac{\pi}{4}$).
*   $z_1$ is in the 2nd quadrant at an angle of $165^\circ$ ($\frac{11\pi}{12}$).
*   $z_2$ is in the 4th quadrant at an angle of $285^\circ$ ($\frac{19\pi}{12}$).

***

### Q7. Pg 4, Q1(c): Given a complex number z, interpret geometrically $ze^{i\alpha}$ where $\alpha$ is real.

**Solution:**

Let the complex number $z$ be represented in polar (exponential) form:
$$z = r e^{i\theta}$$
where:
*   $r = |z|$ is the modulus (the length of the vector from the origin to $z$).
*   $\theta = \text{Arg}(z)$ is the argument (the counterclockwise angle the vector makes with the positive real axis).

Now, consider the expression $ze^{i\alpha}$. By substituting $z$:
$$ze^{i\alpha} = (r e^{i\theta}) e^{i\alpha}$$

Using the laws of exponents ($e^a \cdot e^b = e^{a+b}$):
$$ze^{i\alpha} = r e^{i(\theta + \alpha)}$$

**Geometrical Interpretation:**
Let the new complex number be $w = ze^{i\alpha}$.
1.  **Modulus:** $|w| = r$. The magnitude (length) of the new vector is exactly the same as the magnitude of the original vector $z$.
2.  **Argument:** $\text{Arg}(w) = \theta + \alpha$. The new angle is the original angle $\theta$ shifted by the angle $\alpha$.

Therefore, geometrically, multiplying a complex number $z$ by $e^{i\alpha}$ represents a **rotation of the vector $z$ about the origin $(0,0)$ by an angle $\alpha$**. 
*   If $\alpha > 0$, the rotation is **counterclockwise**.
*   If $\alpha < 0$, the rotation is **clockwise**.
*   The length (magnitude) of the vector remains entirely unchanged. 

This property is what makes exponential forms highly useful for modeling rotational transformations in 2D geometry and physics.

***

### Q8. Pg 6, Q1(b): Find all the roots of $(-4 + 4i)^{\frac{1}{5}}$ and locate them graphically.

**Solution:**

We need to find the five $5^{\text{th}}$ roots of the complex number $w = -4 + 4i$.

**Step 1: Express $w = -4 + 4i$ in polar form.**
Let $x = -4$ and $y = 4$.
*   **Modulus ($r$):** 
    $r = \sqrt{(-4)^2 + 4^2} = \sqrt{16 + 16} = \sqrt{32} = 4\sqrt{2} = 2^{5/2}$
*   **Argument ($\theta$):** 
    Since $x < 0$ and $y > 0$, the point lies in the second quadrant. 
    $\theta = \pi + \tan^{-1}\left(\frac{4}{-4}\right) = \pi + \tan^{-1}(-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$

So, $w = 2^{5/2} \left[ \cos\left(\frac{3\pi}{4} + 2k\pi\right) + i\sin\left(\frac{3\pi}{4} + 2k\pi\right) \right]$.

**Step 2: Apply De Moivre's Theorem to find the roots.**
$$z_k = w^{1/5} = \left( 2^{5/2} \right)^{1/5} \left[ \cos\left(\frac{\frac{3\pi}{4} + 2k\pi}{5}\right) + i\sin\left(\frac{\frac{3\pi}{4} + 2k\pi}{5}\right) \right]$$
The magnitude for all roots is $R = (2^{5/2})^{1/5} = 2^{1/2} = \sqrt{2}$.
The angles are $\alpha_k = \frac{3\pi + 8k\pi}{20}$ for $k = 0, 1, 2, 3, 4$.

**Step 3: Calculate the specific roots (converted to degrees for easier plotting).**
We know $\pi$ radians $= 180^\circ$. Let's calculate the angles:
*   **For $k = 0$:**
    $\alpha_0 = \frac{3\pi}{20} = \frac{3 \times 180^\circ}{20} = 27^\circ$
    $$z_0 = \sqrt{2}(\cos 27^\circ + i\sin 27^\circ)$$
*   **For $k = 1$:**
    $\alpha_1 = \frac{11\pi}{20} = 99^\circ$
    $$z_1 = \sqrt{2}(\cos 99^\circ + i\sin 99^\circ)$$
*   **For $k = 2$:**
    $\alpha_2 = \frac{19\pi}{20} = 171^\circ$
    $$z_2 = \sqrt{2}(\cos 171^\circ + i\sin 171^\circ)$$
*   **For $k = 3$:**
    $\alpha_3 = \frac{27\pi}{20} = 243^\circ$
    $$z_3 = \sqrt{2}(\cos 243^\circ + i\sin 243^\circ)$$
*   **For $k = 4$:**
    $\alpha_4 = \frac{35\pi}{20} = \frac{7\pi}{4} = 315^\circ$
    $$z_4 = \sqrt{2}(\cos 315^\circ + i\sin 315^\circ)$$

**Graphical Location:**
To locate them graphically in the complex plane:
1.  Draw a circle centered at the origin $(0,0)$ with a radius of $\sqrt{2} \approx 1.414$.
2.  The five roots $z_0, z_1, z_2, z_3,$ and $z_4$ all lie on the circumference of this circle.
3.  They form the vertices of a **regular pentagon** inscribed within the circle.
4.  The angular separation between any two adjacent roots is exactly $\frac{2\pi}{5}$ radians or $72^\circ$.
5.  Starting from the first vector $z_0$ at an angle of $27^\circ$ (in Quadrant I), you rotate $72^\circ$ successively to plot $z_1$ in Quadrant II ($99^\circ$), $z_2$ in Quadrant II ($171^\circ$), $z_3$ in Quadrant III ($243^\circ$), and $z_4$ in Quadrant IV ($315^\circ$).
Here are the detailed solutions for the next four questions (Q9 to Q12).

### Q9. Pg 13, CT-03, 1.(b): State vector interpretation of complex number.

**Solution:**

The vector interpretation of a complex number provides a geometric way to visualize complex numbers and their operations. 

**Statement & Explanation:**
A complex number $z = x + iy$ (where $x$ and $y$ are real numbers, and $i = \sqrt{-1}$) can be uniquely represented as a point $P(x, y)$ in a 2-dimensional Cartesian coordinate system known as the **Complex Plane** or **Argand Plane**. 
*   The horizontal x-axis represents the **Real axis** (Re).
*   The vertical y-axis represents the **Imaginary axis** (Im).

Geometrically, this point $P(x, y)$ can be interpreted as a **position vector** $\vec{OP}$ originating from the origin $O(0,0)$ and terminating at the point $P(x, y)$.

**Key characteristics of this vector interpretation:**
1.  **Modulus as Magnitude (Length):** The length or magnitude of the vector $\vec{OP}$ corresponds to the absolute value (or modulus) of the complex number, denoted by $|z|$. By the Pythagorean theorem:
    $$|z| = \sqrt{x^2 + y^2}$$
2.  **Argument as Direction (Angle):** The direction of the vector is given by the angle $\theta$ it makes with the positive real (x) axis, measured in the counterclockwise direction. This angle is called the argument of $z$, denoted by $\text{Arg}(z)$.
    $$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$
3.  **Vector Addition:** The addition of two complex numbers $z_1$ and $z_2$ geometrically corresponds to the standard vector addition (Parallelogram Law or Triangle Law) of their respective position vectors.
4.  **Multiplication by a Scalar:** Multiplying a complex number by a real scalar $c$ scales the length of the vector by $|c|$. If $c < 0$, it also reverses the vector's direction.

***

### Q10. Pg 13, CT-03, 2.(a): Find the modulus and argument($\theta$) of $e^{1+i}$

**Solution:**

Let the complex number be $z = e^{1+i}$.

**Step 1: Separate the exponent into real and imaginary parts.**
Using the fundamental law of exponents ($a^{m+n} = a^m \cdot a^n$), we can rewrite the expression as:
$$z = e^1 \cdot e^i$$
$$z = e \cdot e^{i(1)}$$

**Step 2: Compare with the standard polar (Euler's) form.**
The standard polar form of a complex number is $z = r e^{i\theta}$, where:
*   $r$ is the modulus ($r > 0$).
*   $\theta$ is the argument in radians.

Comparing $z = e \cdot e^{i(1)}$ with $z = r e^{i\theta}$, we can directly identify the parameters:
*   $r = e$ (Euler's number, which is approximately $2.718...$)
*   $\theta = 1$ radian.

**Alternative Method (via Cartesian form):**
We can expand $e^i$ using Euler's formula, $e^{i\theta} = \cos \theta + i\sin \theta$:
$$z = e(\cos 1 + i\sin 1)$$
$$z = (e\cos 1) + i(e\sin 1)$$
Here, the real part is $x = e\cos 1$ and the imaginary part is $y = e\sin 1$.
*   **Modulus ($|z|$):** 
    $$|z| = \sqrt{x^2 + y^2} = \sqrt{(e\cos 1)^2 + (e\sin 1)^2}$$
    $$|z| = \sqrt{e^2(\cos^2 1 + \sin^2 1)}$$
    Since $\cos^2 \theta + \sin^2 \theta = 1$:
    $$|z| = \sqrt{e^2(1)} = e$$
*   **Argument ($\theta$):**
    $$\theta = \tan^{-1}\left(\frac{y}{x}\right) = \tan^{-1}\left(\frac{e\sin 1}{e\cos 1}\right) = \tan^{-1}(\tan 1) = 1 \text{ radian}$$

**Answer:**
*   **Modulus:** $e$
*   **Argument ($\theta$):** $1$ radian (principal argument)

***

### Q11. Pg 13, CT-03, 2.(b): Find the roots of $z = (-1 - i)^{\frac{1}{3}}$, and locate them graphically.

**Solution:**

We are asked to find the three cube roots of the complex number $w = -1 - i$.

**Step 1: Express $w = -1 - i$ in polar form.**
Let $w = x + iy$, so $x = -1$ and $y = -1$.
*   **Modulus ($r$):** 
    $r = \sqrt{(-1)^2 + (-1)^2} = \sqrt{1 + 1} = \sqrt{2}$
*   **Argument ($\theta$):** 
    Since both $x$ and $y$ are negative, the point lies in the third quadrant.
    The principal argument is $\theta = -\pi + \tan^{-1}\left(\frac{-1}{-1}\right) = -\pi + \frac{\pi}{4} = -\frac{3\pi}{4}$.
    (Alternatively, using positive angles: $\pi + \frac{\pi}{4} = \frac{5\pi}{4}$. Let's use $\frac{5\pi}{4}$ to avoid negative angles during calculation.)

So, the polar form of $w$ with general argument is:
$$w = \sqrt{2} \left[ \cos\left(\frac{5\pi}{4} + 2k\pi\right) + i\sin\left(\frac{5\pi}{4} + 2k\pi\right) \right]$$

**Step 2: Apply De Moivre's Theorem for roots.**
$$z_k = w^{1/3} = (\sqrt{2})^{1/3} \left[ \cos\left(\frac{\frac{5\pi}{4} + 2k\pi}{3}\right) + i\sin\left(\frac{\frac{5\pi}{4} + 2k\pi}{3}\right) \right]$$
The magnitude of all three roots will be $R = (2^{1/2})^{1/3} = 2^{1/6}$.
The arguments will be $\alpha_k = \frac{5\pi + 8k\pi}{12}$ for $k = 0, 1, 2$.

**Step 3: Calculate the individual roots.**
Let's convert to degrees for easier graphical plotting ($\pi = 180^\circ$):
*   **For $k = 0$:**
    $\alpha_0 = \frac{5\pi}{12} = \frac{5(180^\circ)}{12} = 75^\circ$
    $$z_0 = 2^{1/6} (\cos 75^\circ + i\sin 75^\circ)$$
*   **For $k = 1$:**
    $\alpha_1 = \frac{5\pi + 8\pi}{12} = \frac{13\pi}{12} = \frac{13(180^\circ)}{12} = 195^\circ$
    $$z_1 = 2^{1/6} (\cos 195^\circ + i\sin 195^\circ)$$
*   **For $k = 2$:**
    $\alpha_2 = \frac{5\pi + 16\pi}{12} = \frac{21\pi}{12} = \frac{7\pi}{4} = 315^\circ$
    $$z_2 = 2^{1/6} (\cos 315^\circ + i\sin 315^\circ)$$

**Graphical Location:**
To represent these roots graphically in the complex plane:
1.  Draw a circle centered at the origin $(0,0)$ with a radius of $2^{1/6}$ (which is approximately $1.122$).
2.  The three roots lie exactly on the circumference of this circle.
3.  They form the vertices of an **equilateral triangle** inscribed in the circle, with exactly $120^\circ$ ($\frac{2\pi}{3}$ radians) between adjacent roots.
4.  Plot $z_0$ in the first quadrant at an angle of $75^\circ$.
5.  Plot $z_1$ in the third quadrant at an angle of $195^\circ$.
6.  Plot $z_2$ in the fourth quadrant at an angle of $315^\circ$ (or $-45^\circ$).

***

### Q12. Pg 14, CT-01, 2.(a): Find the modulus and argument($\theta$) of $z = i\sqrt{2}$

**Solution:**

Let the complex number be $z = i\sqrt{2}$.

**Step 1: Identify the real and imaginary parts.**
We can write this complex number in the standard Cartesian form $z = x + iy$:
$$z = 0 + i\sqrt{2}$$
Here, the real part is $x = 0$ and the imaginary part is $y = \sqrt{2}$.

**Step 2: Calculate the Modulus ($|z|$).**
The modulus represents the distance of the point from the origin.
$$|z| = \sqrt{x^2 + y^2}$$
$$|z| = \sqrt{0^2 + (\sqrt{2})^2}$$
$$|z| = \sqrt{0 + 2} = \sqrt{2}$$

**Step 3: Calculate the Argument ($\theta$).**
The argument represents the angle the vector makes with the positive real axis.
We plot the point $(0, \sqrt{2})$ on the complex plane. 
Since $x = 0$ and $y > 0$, the point lies exactly on the **positive imaginary axis** (the upper half of the y-axis).
The angle corresponding to the positive imaginary axis is exactly $90^\circ$ or $\frac{\pi}{2}$ radians.

Using the formula (keeping limits in mind):
$$\theta = \lim_{x \to 0^+} \tan^{-1}\left(\frac{y}{x}\right) = \tan^{-1}\left(\frac{\sqrt{2}}{0}\right) \to \tan^{-1}(+\infty) = \frac{\pi}{2}$$

**Answer:**
*   **Modulus:** $\sqrt{2}$
*   **Argument ($\theta$):** $\frac{\pi}{2}$ radians (or $90^\circ$)

Here are the detailed solutions for the next four questions (Q13 to Q16).

### Q13. Pg 14, CT-01, 2.(b): Find the roots of $z = (-4 - i4)^{\frac{1}{5}}$ and locate them graphically.

**Solution:**

We need to find the five $5^{\text{th}}$ roots of the complex number $w = -4 - 4i$.

**Step 1: Express $w = -4 - 4i$ in polar form.**
Let $x = -4$ and $y = -4$.
*   **Modulus ($r$):** 
    $r = \sqrt{(-4)^2 + (-4)^2} = \sqrt{16 + 16} = \sqrt{32} = \sqrt{16 \cdot 2} = 4\sqrt{2}$.
    Note that $4\sqrt{2} = 2^2 \cdot 2^{1/2} = 2^{5/2}$.
*   **Argument ($\theta$):** 
    Since both $x$ and $y$ are negative, the point lies in the third quadrant. 
    To keep the angle positive for easier calculation, we calculate the angle counterclockwise from the positive real axis:
    $\theta = \pi + \tan^{-1}\left(\frac{-4}{-4}\right) = \pi + \tan^{-1}(1) = \pi + \frac{\pi}{4} = \frac{5\pi}{4}$.

So, the polar form of $w$ with the general argument is:
$$w = 2^{5/2} \left[ \cos\left(\frac{5\pi}{4} + 2k\pi\right) + i\sin\left(\frac{5\pi}{4} + 2k\pi\right) \right]$$

**Step 2: Apply De Moivre's Theorem to find the roots.**
$$z_k = w^{1/5} = \left( 2^{5/2} \right)^{1/5} \left[ \cos\left(\frac{\frac{5\pi}{4} + 2k\pi}{5}\right) + i\sin\left(\frac{\frac{5\pi}{4} + 2k\pi}{5}\right) \right]$$
*   The magnitude for all roots is $R = (2^{5/2})^{1/5} = 2^{1/2} = \sqrt{2}$.
*   The angles are $\alpha_k = \frac{5\pi + 8k\pi}{20}$ for $k = 0, 1, 2, 3, 4$.

**Step 3: Calculate the specific roots (converting to degrees for easier plotting).**
We know $\pi = 180^\circ$, so $\frac{\pi}{20} = 9^\circ$.
*   **For $k = 0$:**
    $\alpha_0 = \frac{5\pi}{20} = \frac{\pi}{4} = 45^\circ$
    $$z_0 = \sqrt{2}(\cos 45^\circ + i\sin 45^\circ) = 1 + i$$
*   **For $k = 1$:**
    $\alpha_1 = \frac{13\pi}{20} = 13 \times 9^\circ = 117^\circ$
    $$z_1 = \sqrt{2}(\cos 117^\circ + i\sin 117^\circ)$$
*   **For $k = 2$:**
    $\alpha_2 = \frac{21\pi}{20} = 21 \times 9^\circ = 189^\circ$
    $$z_2 = \sqrt{2}(\cos 189^\circ + i\sin 189^\circ)$$
*   **For $k = 3$:**
    $\alpha_3 = \frac{29\pi}{20} = 29 \times 9^\circ = 261^\circ$
    $$z_3 = \sqrt{2}(\cos 261^\circ + i\sin 261^\circ)$$
*   **For $k = 4$:**
    $\alpha_4 = \frac{37\pi}{20} = 37 \times 9^\circ = 333^\circ$
    $$z_4 = \sqrt{2}(\cos 333^\circ + i\sin 333^\circ)$$

**Graphical Location:**
To locate them graphically in the complex (Argand) plane:
1.  Draw a circle centered at the origin $(0,0)$ with a radius of $\sqrt{2} \approx 1.414$.
2.  The five roots $z_0, z_1, z_2, z_3,$ and $z_4$ lie evenly spaced on the circumference of this circle.
3.  They form the vertices of a **regular pentagon** inscribed within the circle.
4.  The angular separation between any two adjacent roots is exactly $\frac{2\pi}{5}$ radians or $72^\circ$.
5.  Starting from $z_0$ at $45^\circ$ (in Quadrant I), the subsequent roots fall at $117^\circ$ (Quadrant II), $189^\circ$ (Quadrant III), $261^\circ$ (Quadrant III), and $333^\circ$ (Quadrant IV).

***

### Q14. Pg 14, CT-01, 1.(b): If $z = 1+i$, then evaluate $|e^z|$ and find $\text{Arg}(e^z)$.

**Solution:**

Given the complex number $z = 1 + i$. We need to analyze the complex exponential function $e^z$.

**Step 1: Substitute $z$ into the exponential function.**
$$e^z = e^{1+i}$$
Using the properties of exponents ($e^{a+b} = e^a \cdot e^b$):
$$e^z = e^1 \cdot e^i$$

**Step 2: Express in polar form to find the modulus and argument.**
Using Euler's formula, $e^{iy} = \cos y + i\sin y$. Thus:
$$e^z = e(\cos 1 + i\sin 1)$$
This is exactly in the standard polar form $w = r(\cos \theta + i\sin \theta)$ or $w = r e^{i\theta}$, where $r > 0$ is the modulus and $\theta$ is the argument.
By direct comparison:
*   $r = e$
*   $\theta = 1$

**Alternative Analytical Calculation:**
Let $e^z = w = u + iv$.
$$e^{1+i} = e^1(\cos 1 + i\sin 1) = (e\cos 1) + i(e\sin 1)$$
Here, $u = e\cos 1$ and $v = e\sin 1$.

*   **To find the Modulus $|e^z|$:**
    $$|e^z| = \sqrt{u^2 + v^2} = \sqrt{(e\cos 1)^2 + (e\sin 1)^2}$$
    $$|e^z| = \sqrt{e^2(\cos^2 1 + \sin^2 1)}$$
    Since $\cos^2 \theta + \sin^2 \theta = 1$:
    $$|e^z| = \sqrt{e^2(1)} = e$$

*   **To find the Argument $\text{Arg}(e^z)$:**
    $$\text{Arg}(e^z) = \tan^{-1}\left(\frac{v}{u}\right) = \tan^{-1}\left(\frac{e\sin 1}{e\cos 1}\right)$$
    $$\text{Arg}(e^z) = \tan^{-1}(\tan 1) = 1 \text{ radian}$$

*General Rule:* For any complex number $z = x + iy$, the modulus $|e^z| = e^x$ and the principal argument $\text{Arg}(e^z) = y$ (adjusted by multiples of $2\pi$ to fall within the principal range $(-\pi, \pi]$ if necessary). Here, $x=1, y=1$, so $|e^z| = e^1 = e$ and $\text{Arg}(e^z) = 1$.

**Answer:** 
*   **$|e^z| = e$**
*   **$\text{Arg}(e^z) = 1$ radian**

***

### Q15. Pg 15, CT-01, 1.(b): Find an equation for a circle of radius 2 with centre at (-3,4) interms of z.

**Solution:**

In the complex plane, a circle is defined as the set of all points $z$ that are at a constant distance (the radius, $r$) from a fixed point (the center, $z_0$). 

The distance between any two complex points $z$ and $z_0$ is given by the modulus of their difference: $|z - z_0|$.

**Step 1: Identify the given parameters.**
*   Radius: $r = 2$
*   Center: The point $(-3, 4)$ in Cartesian coordinates corresponds to the complex number $z_0 = -3 + 4i$.

**Step 2: Write the standard equation of a circle in the complex plane.**
The equation is:
$$|z - z_0| = r$$

**Step 3: Substitute the parameters into the equation.**
$$|z - (-3 + 4i)| = 2$$
$$|z + 3 - 4i| = 2$$

This is the standard and most concise way to represent the equation of the circle in terms of $z$.

**Optional Step (Expanding into general form):**
Sometimes equations are required in the expanded form $z\bar{z} + B\bar{z} + \bar{B}z + C = 0$. To do this, square both sides:
$$|z + 3 - 4i|^2 = 2^2$$
Using the property $|w|^2 = w\bar{w}$:
$$(z + 3 - 4i)\overline{(z + 3 - 4i)} = 4$$
$$(z + 3 - 4i)(\bar{z} + 3 + 4i) = 4$$
$$z\bar{z} + z(3+4i) + \bar{z}(3-4i) + (3-4i)(3+4i) = 4$$
$$z\bar{z} + (3+4i)z + (3-4i)\bar{z} + (3^2 + 4^2) = 4$$
$$z\bar{z} + (3+4i)z + (3-4i)\bar{z} + 25 = 4$$
$$z\bar{z} + (3+4i)z + (3-4i)\bar{z} + 21 = 0$$
Both the compact modulus form and the expanded form are valid equations in terms of $z$. 

**Answer:** The equation for the circle is **$|z + 3 - 4i| = 2$**.

***

### Q16. Pg 15, CT-01, 3.(b): Find the area of a triangle having sides $z_1$ and $z_2$.

**Solution:**

Geometrically, the complex numbers $z_1$ and $z_2$ can be viewed as position vectors extending from the origin in the complex plane. A triangle formed by sides $z_1$ and $z_2$ (with the origin as the third vertex) has an area that is exactly half the area of the parallelogram formed by these two vectors.

**Derivation using Trigonometry:**
Let the complex numbers be expressed in polar form:
$z_1 = r_1 e^{i\theta_1}$
$z_2 = r_2 e^{i\theta_2}$

Here:
*   $r_1 = |z_1|$ is the length of the first side.
*   $r_2 = |z_2|$ is the length of the second side.
*   The angle between the two vectors is $|\theta_2 - \theta_1|$.

From basic geometry, the area of a triangle given two sides and the included angle is:
$$\text{Area} = \frac{1}{2} \cdot (\text{side 1}) \cdot (\text{side 2}) \cdot \sin(\text{included angle})$$
$$\text{Area} = \frac{1}{2} r_1 r_2 |\sin(\theta_2 - \theta_1)| \quad \text{--- (Equation 1)}$$

**Translating to Complex Number Operations:**
Let's evaluate the product of the complex conjugate of $z_1$ and $z_2$:
$$\bar{z}_1 z_2 = (r_1 e^{-i\theta_1})(r_2 e^{i\theta_2})$$
$$\bar{z}_1 z_2 = r_1 r_2 e^{i(\theta_2 - \theta_1)}$$

Using Euler's formula ($e^{i\alpha} = \cos \alpha + i\sin \alpha$):
$$\bar{z}_1 z_2 = r_1 r_2 [\cos(\theta_2 - \theta_1) + i\sin(\theta_2 - \theta_1)]$$

The imaginary part of this product is:
$$\text{Im}(\bar{z}_1 z_2) = r_1 r_2 \sin(\theta_2 - \theta_1)$$

Comparing this with Equation 1, we see that the Area is exactly half the absolute value of this imaginary part:
$$\text{Area} = \frac{1}{2} |\text{Im}(\bar{z}_1 z_2)|$$

**Alternative Derivation (Cartesian form):**
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$.
The area of a triangle formed by vectors $(x_1, y_1)$ and $(x_2, y_2)$ is given by half the absolute value of the determinant of their coordinates:
$$\text{Area} = \frac{1}{2} |x_1 y_2 - x_2 y_1|$$
Now calculate $\bar{z}_1 z_2$:
$$\bar{z}_1 z_2 = (x_1 - iy_1)(x_2 + iy_2) = (x_1 x_2 + y_1 y_2) + i(x_1 y_2 - x_2 y_1)$$
The imaginary part is exactly $(x_1 y_2 - x_2 y_1)$.
Therefore, the area is:
$$\text{Area} = \frac{1}{2} |\text{Im}(\bar{z}_1 z_2)|$$

*(Note: Since $\text{Im}(w) = \frac{w - \bar{w}}{2i}$, another common valid way to write this is Area = $\frac{1}{4} | \bar{z}_1 z_2 - z_1 \bar{z}_2 |$.)*

**Answer:** The area of the triangle is given by the formula **$\frac{1}{2} |\text{Im}(\bar{z}_1 z_2)|$** or **$\frac{1}{4} | \bar{z}_1 z_2 - z_1 \bar{z}_2 |$**.

Here are the detailed solutions for the next four questions (Q17 to Q20).

### Q17. Pg 18, CT-I, 2.(a): If $z = 6e^{\frac{\pi i}{3}}$, then evaluate $|e^{-iz}|$

**Solution:**

We need to evaluate the modulus of the exponential function $e^{-iz}$ given the complex number $z$.

**Step 1: Convert $z$ from polar (exponential) form to Cartesian (rectangular) form.**
The given complex number is $z = 6e^{\frac{\pi i}{3}}$. 
Using Euler's formula, $e^{i\theta} = \cos\theta + i\sin\theta$:
$$z = 6 \left( \cos\left(\frac{\pi}{3}\right) + i\sin\left(\frac{\pi}{3}\right) \right)$$
We know that $\cos(\frac{\pi}{3}) = \cos(60^\circ) = \frac{1}{2}$ and $\sin(\frac{\pi}{3}) = \sin(60^\circ) = \frac{\sqrt{3}}{2}$.
$$z = 6 \left( \frac{1}{2} + i\frac{\sqrt{3}}{2} \right)$$
$$z = 3 + 3\sqrt{3}i$$

**Step 2: Calculate the exponent $-iz$.**
Multiply $z$ by $-i$:
$$-iz = -i(3 + 3\sqrt{3}i)$$
$$-iz = -3i - 3\sqrt{3}i^2$$
Since $i^2 = -1$:
$$-iz = -3i - 3\sqrt{3}(-1)$$
$$-iz = 3\sqrt{3} - 3i$$

**Step 3: Evaluate the modulus $|e^{-iz}|$.**
Substitute the result back into the exponential expression:
$$e^{-iz} = e^{3\sqrt{3} - 3i}$$
Using the laws of exponents ($e^{a+b} = e^a \cdot e^b$):
$$e^{-iz} = e^{3\sqrt{3}} \cdot e^{-3i}$$
Now, we take the absolute value (modulus) of both sides. The modulus of a product is the product of the moduli ($|w_1 w_2| = |w_1| |w_2|$):
$$|e^{-iz}| = |e^{3\sqrt{3}}| \cdot |e^{-3i}|$$
*   Since $e^{3\sqrt{3}}$ is a purely real positive number, its modulus is just itself: $|e^{3\sqrt{3}}| = e^{3\sqrt{3}}$.
*   The term $e^{-3i}$ is of the form $e^{i\theta}$ (where $\theta = -3$). For any real number $\theta$, $|e^{i\theta}| = |\cos\theta + i\sin\theta| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$. Therefore, $|e^{-3i}| = 1$.

$$|e^{-iz}| = e^{3\sqrt{3}} \cdot 1 = e^{3\sqrt{3}}$$

**Answer:** **$|e^{-iz}| = e^{3\sqrt{3}}$**

***

### Q18. Pg 18, CT-I, 2.(b): Find the roots of $z = (-16i)^{\frac{1}{4}}$ and locate them graphically.

**Solution:**

We need to find the four $4^{\text{th}}$ roots of the complex number $w = -16i$.

**Step 1: Express $w = -16i$ in polar form.**
Let $w = x + iy$, so $x = 0$ and $y = -16$.
*   **Modulus ($r$):** 
    $r = \sqrt{0^2 + (-16)^2} = 16$
*   **Argument ($\theta$):** 
    The point $(0, -16)$ lies directly on the negative imaginary axis. The angle for the negative imaginary axis is $270^\circ$ or $\frac{3\pi}{2}$ radians (using a positive angle).

So, the polar form of $w$ with the general argument is:
$$w = 16 \left[ \cos\left(\frac{3\pi}{2} + 2k\pi\right) + i\sin\left(\frac{3\pi}{2} + 2k\pi\right) \right]$$

**Step 2: Apply De Moivre's Theorem to find the roots.**
$$z_k = w^{1/4} = (16)^{1/4} \left[ \cos\left(\frac{\frac{3\pi}{2} + 2k\pi}{4}\right) + i\sin\left(\frac{\frac{3\pi}{2} + 2k\pi}{4}\right) \right]$$
*   The magnitude for all roots is $R = 16^{1/4} = (2^4)^{1/4} = 2$.
*   The angles are $\alpha_k = \frac{3\pi + 4k\pi}{8}$ for $k = 0, 1, 2, 3$.

**Step 3: Calculate the specific roots (converting to degrees for easier plotting).**
We know $\pi = 180^\circ$, so $\frac{\pi}{8} = 22.5^\circ$.
*   **For $k = 0$:**
    $\alpha_0 = \frac{3\pi}{8} = 3 \times 22.5^\circ = 67.5^\circ$
    $$z_0 = 2(\cos 67.5^\circ + i\sin 67.5^\circ)$$
*   **For $k = 1$:**
    $\alpha_1 = \frac{7\pi}{8} = 7 \times 22.5^\circ = 157.5^\circ$
    $$z_1 = 2(\cos 157.5^\circ + i\sin 157.5^\circ)$$
*   **For $k = 2$:**
    $\alpha_2 = \frac{11\pi}{8} = 11 \times 22.5^\circ = 247.5^\circ$
    $$z_2 = 2(\cos 247.5^\circ + i\sin 247.5^\circ)$$
*   **For $k = 3$:**
    $\alpha_3 = \frac{15\pi}{8} = 15 \times 22.5^\circ = 337.5^\circ$
    $$z_3 = 2(\cos 337.5^\circ + i\sin 337.5^\circ)$$

**Graphical Location:**
To locate them graphically in the complex plane:
1.  Draw a circle centered at the origin $(0,0)$ with a radius of $R=2$.
2.  The four roots $z_0, z_1, z_2,$ and $z_3$ lie on the circumference of this circle.
3.  Because they are 4th roots, they are spaced evenly by $\frac{2\pi}{4} = \frac{\pi}{2}$ radians, or exactly $90^\circ$ apart.
4.  They form the vertices of a **square** inscribed within the circle.
5.  Starting from the first vector $z_0$ at an angle of $67.5^\circ$ (Quadrant I), the other roots are obtained by adding $90^\circ$ successively: $157.5^\circ$ (Quadrant II), $247.5^\circ$ (Quadrant III), and $337.5^\circ$ (Quadrant IV).

***

### Q19. Pg 19, CT-I, 2.(a): Express the complex number $-2\sqrt{3} - 2i$ in polar form.

**Solution:**

We need to convert the complex number $z = -2\sqrt{3} - 2i$ into the standard polar form $z = r(\cos\theta + i\sin\theta)$.

**Step 1: Identify the Cartesian coordinates.**
Let $z = x + iy$.
Here, the real part is $x = -2\sqrt{3}$ and the imaginary part is $y = -2$.

**Step 2: Calculate the Modulus ($r$).**
The modulus represents the distance from the origin.
$$r = |z| = \sqrt{x^2 + y^2}$$
$$r = \sqrt{(-2\sqrt{3})^2 + (-2)^2}$$
$$r = \sqrt{4(3) + 4}$$
$$r = \sqrt{12 + 4} = \sqrt{16} = 4$$

**Step 3: Calculate the Argument ($\theta$).**
The argument $\theta$ is the angle made with the positive real axis.
Since $x$ is negative and $y$ is negative, the complex number lies in the **third quadrant**. 

First, let's find the reference angle $\alpha$ in the first quadrant:
$$\alpha = \tan^{-1}\left(\left| \frac{y}{x} \right|\right) = \tan^{-1}\left(\frac{2}{2\sqrt{3}}\right) = \tan^{-1}\left(\frac{1}{\sqrt{3}}\right)$$
We know that $\tan(\frac{\pi}{6}) = \frac{1}{\sqrt{3}}$, so $\alpha = \frac{\pi}{6}$ (or $30^\circ$).

Now, we adjust the angle for the third quadrant.
*   **Using Principal Argument (range $-\pi < \theta \le \pi$):**
    $\theta = -\pi + \alpha = -\pi + \frac{\pi}{6} = -\frac{5\pi}{6}$
*   **Using Positive Argument (range $0 \le \theta < 2\pi$):**
    $\theta = \pi + \alpha = \pi + \frac{\pi}{6} = \frac{7\pi}{6}$

Both conventions are mathematically correct. The principal argument is generally preferred in advanced mathematics.

**Step 4: Write the polar form.**
Using the principal argument:
$$z = 4\left(\cos\left(-\frac{5\pi}{6}\right) + i\sin\left(-\frac{5\pi}{6}\right)\right)$$
Or, using the positive argument:
$$z = 4\left(\cos\frac{7\pi}{6} + i\sin\frac{7\pi}{6}\right)$$

In exponential form, this can be written as $z = 4e^{-i\frac{5\pi}{6}}$ or $z = 4e^{i\frac{7\pi}{6}}$.

**Answer:** The polar form is **$4\left(\cos\left(-\frac{5\pi}{6}\right) + i\sin\left(-\frac{5\pi}{6}\right)\right)$** or equivalently **$4\left(\cos\frac{7\pi}{6} + i\sin\frac{7\pi}{6}\right)$**.

***

### Q20. Pg 19, CT-I, 2.(b): Find the roots of $z = (i)^{\frac{2}{3}}$ and locate them graphically.

**Solution:**

We are asked to find the values of $(i)^{\frac{2}{3}}$. In complex analysis, fractional exponents $z^{m/n}$ can be interpreted as evaluating the $n^{\text{th}}$ roots of the $m^{\text{th}}$ power: $z = (i^2)^{\frac{1}{3}}$. 

*(Note: Reversing the order to $(i^{1/3})^2$ yields the exact same set of three complex roots, but squaring first is much simpler.)*

**Step 1: Simplify the base expression.**
Let $w = i^2$. We know that $i^2 = -1$.
Therefore, the problem reduces to finding the three cube roots of $-1$.
$$z = (-1)^{\frac{1}{3}}$$

**Step 2: Express $w = -1$ in polar form.**
For the number $-1$:
*   Modulus $r = 1$.
*   Argument $\theta = \pi$ (since it lies on the negative real axis).
The general polar form is:
$$w = 1 \cdot [\cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi)]$$

**Step 3: Apply De Moivre's Theorem for roots.**
$$z_k = 1^{1/3} \left[ \cos\left(\frac{\pi + 2k\pi}{3}\right) + i\sin\left(\frac{\pi + 2k\pi}{3}\right) \right]$$
The magnitude for all roots is $R = 1^{1/3} = 1$.
The angles are $\alpha_k = \frac{\pi + 2k\pi}{3}$ for $k = 0, 1, 2$.

**Step 4: Calculate the specific roots.**
*   **For $k = 0$:**
    $\alpha_0 = \frac{\pi}{3} = 60^\circ$
    $$z_0 = \cos 60^\circ + i\sin 60^\circ = \frac{1}{2} + i\frac{\sqrt{3}}{2}$$
*   **For $k = 1$:**
    $\alpha_1 = \frac{\pi + 2\pi}{3} = \frac{3\pi}{3} = \pi = 180^\circ$
    $$z_1 = \cos 180^\circ + i\sin 180^\circ = -1 + 0i = -1$$
*   **For $k = 2$:**
    $\alpha_2 = \frac{\pi + 4\pi}{3} = \frac{5\pi}{3} = 300^\circ$ (or $-60^\circ$)
    $$z_2 = \cos 300^\circ + i\sin 300^\circ = \frac{1}{2} - i\frac{\sqrt{3}}{2}$$

**Graphical Location:**
To represent these roots graphically in the complex Argand plane:
1.  Draw a **unit circle** (a circle with a radius of 1) centered at the origin $(0,0)$.
2.  The three roots $z_0, z_1,$ and $z_2$ all lie exactly on the circumference of this unit circle.
3.  They form the vertices of an **equilateral triangle** inscribed in the circle, as they are spaced exactly $120^\circ$ ($\frac{2\pi}{3}$) apart.
4.  $z_0$ is located in the first quadrant at an angle of $60^\circ$.
5.  $z_1$ is located precisely on the negative real axis at the point $(-1, 0)$.
6.  $z_2$ is located in the fourth quadrant at an angle of $300^\circ$ (or $-60^\circ$).

Here are the detailed solutions for the next four questions (Q21 to Q24).

### Q21🤓. Pg 19, CT-I, 3.(b): Suppose $z = re^{i\theta}$. Prove that $z^i = e^{-(\theta+2k\pi)}\{\cos(\ln r) + i\sin(\ln r)\}$ where $k = 0, \pm 1, \pm 2, \dots$

**Solution:**

We need to evaluate the complex power $z^i$. 

**Step 1: Define the complex power using logarithms.**
By definition, a complex number $z$ raised to a complex power $c$ is evaluated using the complex exponential and natural logarithm:
$$z^c = e^{c \ln z}$$
Therefore, for our problem:
$$z^i = e^{i \ln z}$$

**Step 2: Expand the complex logarithm $\ln z$.**
The natural logarithm of a complex number $z = r e^{i\theta}$ is a multi-valued function defined as:
$$\ln z = \ln|z| + i \text{Arg}(z)$$
Because the argument is periodic, the general argument is $\theta + 2k\pi$ (where $k$ is any integer: $0, \pm 1, \pm 2, \dots$).
Substitute this into the logarithm:
$$\ln z = \ln r + i(\theta + 2k\pi)$$

**Step 3: Substitute $\ln z$ back into the exponent.**
$$z^i = e^{i [\ln r + i(\theta + 2k\pi)]}$$

**Step 4: Distribute the $i$ in the exponent.**
$$z^i = e^{i \ln r + i^2 (\theta + 2k\pi)}$$
Since we know that $i^2 = -1$, substitute it in:
$$z^i = e^{i \ln r - (\theta + 2k\pi)}$$

**Step 5: Separate the real and imaginary parts of the exponent.**
Using the exponent rule $e^{a+b} = e^a \cdot e^b$:
$$z^i = e^{-(\theta + 2k\pi)} \cdot e^{i \ln r}$$

**Step 6: Apply Euler's formula.**
Euler's formula states that $e^{i\phi} = \cos\phi + i\sin\phi$. Here, our angle is $\phi = \ln r$.
$$e^{i \ln r} = \cos(\ln r) + i\sin(\ln r)$$

Substitute this back into our expression for $z^i$:
$$z^i = e^{-(\theta + 2k\pi)} \{ \cos(\ln r) + i\sin(\ln r) \}$$

This completes the proof.

***

### Q22. (i) $|Z|$ represents (a) complex (b) real (c) distance (d) equation of circle

*(Note: This is a multiple-choice question from the Complex Number System section).*

**Solution:**

Let the complex number be defined in Cartesian coordinates as $Z = x + iy$.
By definition, the modulus (or absolute value) of $Z$, denoted as $|Z|$, is calculated as:
$$|Z| = \sqrt{x^2 + y^2}$$

Let's evaluate the given options based on this:
*   **(a) complex:** While $|Z|$ belongs to the set of complex numbers (since all real numbers are technically complex numbers with a zero imaginary part), calling it "complex" is not its defining geometric or algebraic feature in this context.
*   **(b) real:** $|Z|$ is always a non-negative **real** number. This is mathematically correct.
*   **(c) distance:** Geometrically, in the complex Argand plane, the coordinates $(x,y)$ represent the point $Z$. By the distance formula (or Pythagorean theorem), $\sqrt{x^2 + y^2}$ is exactly the physical **distance** from the origin $(0,0)$ to the point $Z(x,y)$. 
*   **(d) equation of circle:** $|Z| = r$ is the equation of a circle, but $|Z|$ by itself is just an expression, not an equation.

In the context of standard multiple-choice questions in complex variables, when asked what the modulus *represents*, the examiner is typically looking for its geometric interpretation. Therefore, it represents the **distance** (specifically, the distance from the origin to the point $Z$).

**Answer:** **(c) distance**

***

### Q23. (ii) Complex number Z can be represents (a) real (b) vector (c) line

**Solution:**

A complex number $Z = x + iy$ consists of a real part $x$ and an imaginary part $y$. 

To represent this graphically, we use the 2D Cartesian coordinate system called the Argand plane. The number $Z$ is plotted as a point $P$ with coordinates $(x, y)$. 

By drawing a directed line segment from the origin $O(0,0)$ to the point $P(x,y)$, we form a **position vector** $\vec{OP}$.
*   The length of this vector is the modulus $|Z|$.
*   The angle this vector makes with the positive x-axis is the argument $\text{Arg}(Z)$.
*   Complex addition ($Z_1 + Z_2$) perfectly mirrors the parallelogram law of **vector** addition.

Because of these properties, complex numbers are deeply tied to 2D vector mathematics and are fundamentally represented geometrically as vectors. They cannot represent a whole line, nor are they strictly real numbers (unless $y=0$).

**Answer:** **(b) vector**

***

### Q24. (iii) $|e^{ix}|$ is equal to (a) $ie^x$ (b) $ie^y$ (c) $e^{-y}$

**Solution:**

First, we must critically analyze the question. As literally written ($|e^{ix}|$), if $x$ is assumed to be a standard real variable, by Euler's formula $e^{ix} = \cos x + i\sin x$. The modulus would be $\sqrt{\cos^2 x + \sin^2 x} = \sqrt{1} = 1$. Notice that $1$ is not among the options.

This strongly indicates a standard typographical error in the source exam paper. In the context of Complex Variables, this question almost certainly intended to ask for the modulus of $e^{iz}$, where $z$ is a complex variable $z = x + iy$. 

Let's solve the corrected assumption: **Evaluate $|e^{iz}|$ where $z = x + iy$**.

**Step 1: Substitute $z$ into the expression.**
$$iz = i(x + iy)$$
$$iz = ix + iy^2$$
Since $i^2 = -1$:
$$iz = ix - y = -y + ix$$

**Step 2: Apply the exponential function.**
$$e^{iz} = e^{-y + ix}$$
Using the properties of exponents:
$$e^{iz} = e^{-y} \cdot e^{ix}$$

**Step 3: Find the modulus.**
The modulus of a product is the product of the individual moduli ($|A \cdot B| = |A| \cdot |B|$):
$$|e^{iz}| = |e^{-y} \cdot e^{ix}| = |e^{-y}| \cdot |e^{ix}|$$

*   **Evaluate $|e^{-y}|$:** Since $y$ is a real number, $-y$ is a real number. The exponential function $e^{\text{real number}}$ always outputs a positive real number. Therefore, its absolute value is just itself: $|e^{-y}| = e^{-y}$.
*   **Evaluate $|e^{ix}|$:** Since $x$ is a real number, Euler's formula states $e^{ix} = \cos x + i\sin x$. Its modulus is $\sqrt{\cos^2 x + \sin^2 x} = \sqrt{1} = 1$.

**Step 4: Multiply the results.**
$$|e^{iz}| = (e^{-y}) \cdot (1) = e^{-y}$$

This perfectly matches option (c).

**Answer:** **(c) $e^{-y}$** *(Note: This assumes the original question intended to ask for $|e^{iz}|$, which is standard for this topic.)*


Here are the detailed solutions for the next four questions (Q25 to Q28).

### Q25. (iii) (Alternative variant) $e^{i\theta} = \cos\theta + i\sin\theta$ is called (a) De-Moivre's identity (b) Euler's formula

**Solution:**

This question tests fundamental mathematical definitions in complex analysis.

*   The equation $e^{i\theta} = \cos\theta + i\sin\theta$ establishes the profound relationship between trigonometric functions and the complex exponential function. It was introduced by the Swiss mathematician Leonhard Euler in 1748. Thus, this equation is universally known as **Euler's formula**.
*   Let's check the other option for clarity: **De Moivre's identity** (or theorem) relates to raising a complex number in polar form to an integer power. It states that $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$. 

Since the given expression matches Euler's derivation, option (b) is the correct choice.

**Answer:** **(b) Euler's formula**

***

### Q26. (iv) $(\cos \theta + i \sin \theta)^n = \cos n\theta + i \sin n\theta$ where n is any positive integer. is called (a) De-Moivre's Theorem (b) Euler's formula

**Solution:**

Similar to the previous question, this tests a core theorem's name.

*   The given equation is $(\cos \theta + i \sin \theta)^n = \cos n\theta + i \sin n\theta$. This formula allows us to easily compute the powers and roots of complex numbers when they are written in trigonometric (polar) form. 
*   This relationship was discovered by the French mathematician Abraham de Moivre. Therefore, it is formally known as **De Moivre's Theorem**.
*   As established in Q25, Euler's formula is $e^{i\theta} = \cos\theta + i\sin\theta$, which is structurally different (though Euler's formula can be used to *prove* De Moivre's Theorem very easily using exponent rules: $(e^{i\theta})^n = e^{in\theta}$).

Therefore, the statement provided exactly matches De Moivre's Theorem.

**Answer:** **(a) De-Moivre's Theorem**

***

### Q27. (v) A circle of radius 2 with centre at (0,-3) can be represented by ...........

**Solution:**

We need to construct the standard mathematical equation for a circle in the complex plane.

**Step 1: Recall the general equation of a circle.**
In the complex Argand plane, the distance between any arbitrary point $z$ and a fixed center point $z_0$ is given by the modulus $|z - z_0|$. 
A circle is defined geometrically as the locus of all points $z$ that are at a constant distance (radius, $r$) from the center ($z_0$). 
Therefore, the general equation of a circle is:
$$|z - z_0| = r$$

**Step 2: Identify the given parameters.**
*   The radius is given as $r = 2$.
*   The center is given as Cartesian coordinates $(0, -3)$. In the complex plane, the x-coordinate is the real part and the y-coordinate is the imaginary part. Therefore, the center corresponds to the complex number:
    $$z_0 = 0 + i(-3) = -3i$$

**Step 3: Substitute the parameters into the general equation.**
$$|z - (-3i)| = 2$$
$$|z + 3i| = 2$$

This absolute value equation accurately and concisely represents the requested circle. 

**Answer:** **$|z + 3i| = 2$**

***

### Q28. (v) (Alternative variant) $|z+3-4i|=2$ represents (a) complex number (b) circle (c) Line

**Solution:**

We are given the algebraic equation $|z + 3 - 4i| = 2$ and asked to identify the geometric locus it represents in the complex plane.

**Step 1: Rewrite the equation into standard geometric form.**
The standard equation linking distance in the complex plane is $|z - z_0| = \text{distance}$. Let's factor out a minus sign inside the modulus to match this standard form:
$$|z - (-3 + 4i)| = 2$$

**Step 2: Interpret the components geometrically.**
*   $z$ represents any arbitrary point $(x, y)$ on the locus.
*   $z_0 = -3 + 4i$ is a fixed point (coordinate $(-3, 4)$).
*   The modulus operator $|\dots|$ denotes the Euclidean distance between $z$ and $z_0$.
*   The equation states that the distance between any point $z$ and the fixed point $(-3 + 4i)$ is always exactly $2$.

**Step 3: Identify the shape.**
By definition in classical geometry, the set of all points in a 2D plane that are at a fixed, constant distance (radius $r=2$) from a specific center point ($z_0 = -3 + 4i$) constitutes a **circle**. 
*   It does not represent a single complex number (which would just be a point).
*   It does not represent a line (a line in complex numbers usually looks like $|z - A| = |z - B|$ or involves arguments).

**Answer:** **(b) circle**


Here are the detailed solutions for the next four questions (Q29 to Q32).

### Q29. (v) (Alternative variant) $|z+3| + |z-3| = 10$ represents (a) complex number (b) circle (c) ellipse.

**Solution:**

To determine the geometric shape represented by this equation, let's analyze the expression logically and geometrically.

**Step 1: Understand the geometric meaning of modulus.**
In the complex plane, the expression $|z - z_0|$ represents the Euclidean distance between a variable point $z$ and a fixed point $z_0$.
*   $|z + 3| = |z - (-3)|$ is the distance from point $z$ to the fixed point $z_1 = -3$ (or coordinate $(-3,0)$).
*   $|z - 3|$ is the distance from point $z$ to the fixed point $z_2 = 3$ (or coordinate $(3,0)$).

**Step 2: Translate the equation into geometry.**
The equation $|z+3| + |z-3| = 10$ translates to: 
*"The sum of the distances from a point $z$ to two fixed points ($-3$ and $3$) is a constant value of $10$."*

**Step 3: Identify the classical geometric locus.**
By definition in coordinate geometry, an **ellipse** is the locus of all points in a plane such that the sum of their distances from two fixed points (called the foci) is constant.
*   Here, the foci are $F_1 = -3$ and $F_2 = 3$.
*   The constant sum of distances is $2a = 10$ (which is the length of the major axis).
*   We must also verify that this constant sum ($10$) is strictly greater than the distance between the two foci ($|3 - (-3)| = 6$). Since $10 > 6$, it forms a valid, non-degenerate ellipse.

*(Note: If the sum was equal to the distance between the foci, it would be a line segment. If the equation had a minus sign between the moduli, $|z+3| - |z-3| = \text{const}$, it would represent a hyperbola.)*

**Answer:** **(c) ellipse**

***

### Q30. (vi) $ze^{i\alpha}$ represents multiplication of the vector Z with $e^{i\alpha}$ amount. (a) Yes (b) No (c) none of a,b.

**Solution:**

This question tests the geometric interpretation of multiplying a complex number by $e^{i\alpha}$.

**Step 1: Analyze the term "$e^{i\alpha}$ amount".**
In mathematics and physics, when we talk about multiplying a vector by an "amount" (a scalar), we generally mean scaling the vector—changing its magnitude (stretching or shrinking its length). 

**Step 2: Analyze the actual geometric effect of $ze^{i\alpha}$.**
Let $z = re^{i\theta}$.
The product is $z e^{i\alpha} = (re^{i\theta})e^{i\alpha} = re^{i(\theta + \alpha)}$.
*   **Magnitude (Amount):** The new magnitude is still $r$. The length of the vector is entirely unchanged because $|e^{i\alpha}| = \sqrt{\cos^2\alpha + \sin^2\alpha} = 1$. It does not multiply the vector by any numerical "amount" in terms of length.
*   **Direction:** The argument changes from $\theta$ to $\theta + \alpha$. 

**Step 3: Conclusion.**
Geometrically, multiplying $z$ by $e^{i\alpha}$ represents a pure **rotation** of the vector $z$ around the origin by the angle $\alpha$. It does *not* represent multiplying the vector's magnitude by an amount. Because the phrasing implies a change in magnitude or scaling (which is false), the statement is incorrect.

**Answer:** **(b) No** (It represents a rotation, not a scaling/multiplication by an amount).

***

### Q31. (vii) $|z-z_0|$ represents (a) circle (b) Distance between two points z & $z_0$. (c) none of a & b.

**Solution:**

We need to interpret the mathematical expression $|z - z_0|$.

**Step 1: Define the expression algebraically.**
Let the complex numbers be represented in Cartesian coordinates:
$z = x + iy$
$z_0 = x_0 + iy_0$

The difference inside the modulus is:
$z - z_0 = (x - x_0) + i(y - y_0)$

The modulus of this difference is:
$$|z - z_0| = \sqrt{(x - x_0)^2 + (y - y_0)^2}$$

**Step 2: Interpret the result geometrically.**
The formula $\sqrt{(x - x_0)^2 + (y - y_0)^2}$ is precisely the standard Euclidean **distance formula** between the two points $(x,y)$ and $(x_0, y_0)$ in the 2D plane. 

**Step 3: Why is it not a circle?**
While the *equation* $|z - z_0| = r$ (where it is set equal to a constant $r$) represents a circle, the expression $|z - z_0|$ *on its own* is not an equation; it is simply a scalar value that evaluates to the distance between those two specific points.

**Answer:** **(b) Distance between two points z & $z_0$.**

***

### Q32. (viii) Determine which of the following points lie inside the circle $|z-i|=1$. (a) $\frac{1}{2}+i$ (b) $1+\frac{i}{2}$

**Solution:**

We are given a boundary defined by the equation of a circle: $|z - i| = 1$.
*   **Center of the circle:** $z_0 = i$ (or coordinate $(0, 1)$).
*   **Radius:** $r = 1$.

A point $z$ lies **inside** the circle if its distance from the center is strictly less than the radius. Mathematically, the condition for a point to be inside is:
$$|z - i| < 1$$

We will test both points to see which one satisfies this condition.

**Test Point (a): $z_a = \frac{1}{2} + i$**
Substitute $z_a$ into the distance expression:
$$|z_a - i| = \left| \left(\frac{1}{2} + i\right) - i \right|$$
$$= \left| \frac{1}{2} + 0i \right|$$
$$= \sqrt{\left(\frac{1}{2}\right)^2 + 0^2} = \frac{1}{2}$$
Compare the result with the radius $r=1$:
Since $\frac{1}{2} < 1$, the condition is satisfied.
Therefore, Point (a) lies **inside** the circle.

**Test Point (b): $z_b = 1 + \frac{i}{2}$**
Substitute $z_b$ into the distance expression:
$$|z_b - i| = \left| \left(1 + \frac{1}{2}i\right) - i \right|$$
$$= \left| 1 - \frac{1}{2}i \right|$$
Calculate the modulus:
$$= \sqrt{1^2 + \left(-\frac{1}{2}\right)^2} = \sqrt{1 + \frac{1}{4}} = \sqrt{\frac{5}{4}} = \frac{\sqrt{5}}{2}$$
We know that $\sqrt{5} \approx 2.236$, so $\frac{\sqrt{5}}{2} \approx 1.118$.
Compare the result with the radius $r=1$:
Since $\frac{\sqrt{5}}{2} > 1$, the condition is NOT satisfied.
Therefore, Point (b) lies **outside** the circle.

**Answer:** Point **(a) $\frac{1}{2}+i$** lies inside the circle.





Here are the detailed solutions for the next four questions (Q33 to Q36).

### Q33. (viii) (Alternative variant) Determine which of the following points inside the circle $|z-2|=\frac{1}{2}$ Ans. (a) $1+\frac{1}{2}i$ (b) $0+\frac{1}{2}i$ (c) $1+i$

**Solution:**

We are given the equation of a circle: $|z - 2| = \frac{1}{2}$.
*   **Center of the circle:** $z_0 = 2$ (or coordinate $(2, 0)$).
*   **Radius:** $r = \frac{1}{2} = 0.5$.

A point $z$ lies **inside** the circle if its distance from the center is strictly less than the radius. Mathematically, the condition is:
$$|z - 2| < 0.5$$

We evaluate this condition for all three given options:

**Test Option (a): $z = 1 + 0.5i$**
$$|z - 2| = |(1 + 0.5i) - 2| = |-1 + 0.5i|$$
$$|-1 + 0.5i| = \sqrt{(-1)^2 + (0.5)^2} = \sqrt{1 + 0.25} = \sqrt{1.25} \approx 1.118$$
Since $1.118 > 0.5$, this point lies **outside** the circle.

**Test Option (b): $z = 0 + 0.5i$**
$$|z - 2| = |(0 + 0.5i) - 2| = |-2 + 0.5i|$$
$$|-2 + 0.5i| = \sqrt{(-2)^2 + (0.5)^2} = \sqrt{4 + 0.25} = \sqrt{4.25} \approx 2.062$$
Since $2.062 > 0.5$, this point lies **outside** the circle.

**Test Option (c): $z = 1 + i$**
$$|z - 2| = |(1 + i) - 2| = |-1 + i|$$
$$|-1 + i| = \sqrt{(-1)^2 + 1^2} = \sqrt{1 + 1} = \sqrt{2} \approx 1.414$$
Since $1.414 > 0.5$, this point lies **outside** the circle.

**Conclusion:** 
Mathematically, based on the exact values provided in the text, **none** of the given options lie inside the circle. (It is highly likely there is a typographical error in the source exam paper, such as the center being $z=1$ or the radius being larger, but evaluating strictly what is written proves they are all outside).

**Answer:** **None of the options** satisfy the condition $|z-2| < 0.5$. All given points lie outside the circle.

***

### Q34. (ix) $z\bar{z}$ is always (a) complex (b) real (c) imaginary.

**Solution:**

We need to determine the mathematical nature of the product of a complex number and its complex conjugate.

**Step 1: Define the complex number and its conjugate.**
Let $z$ be a complex number in standard Cartesian form:
$$z = x + iy$$
where $x$ and $y$ are real numbers.
The complex conjugate of $z$, denoted by $\bar{z}$, is obtained by flipping the sign of the imaginary part:
$$\bar{z} = x - iy$$

**Step 2: Multiply $z$ and $\bar{z}$.**
$$z\bar{z} = (x + iy)(x - iy)$$

This is a classic "difference of squares" algebraic expansion, $(a+b)(a-b) = a^2 - b^2$:
$$z\bar{z} = (x)^2 - (iy)^2$$
$$z\bar{z} = x^2 - i^2y^2$$

**Step 3: Simplify the expression.**
Since the imaginary unit squared is $i^2 = -1$:
$$z\bar{z} = x^2 - (-1)y^2$$
$$z\bar{z} = x^2 + y^2$$

**Step 4: Analyze the result.**
Because $x$ and $y$ are real numbers, their squares $x^2$ and $y^2$ are non-negative real numbers. The sum of two real numbers is always a purely **real** number. There is no imaginary unit "$i$" left in the final expression. 
*(Note: $x^2 + y^2$ is also equal to $|z|^2$, the square of the modulus).*

**Answer:** **(b) real**

***

### Q35. (x) $e^{i\pi}+1$ is equal to (a) 1 (b) 0 (c) $\infty$

**Solution:**

This question requires the evaluation of the most famous equation in complex analysis, Euler's Identity.

**Step 1: Evaluate $e^{i\pi}$ using Euler's formula.**
Euler's formula states that for any real number $\theta$:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

Let $\theta = \pi$ radians (which is equivalent to $180^\circ$):
$$e^{i\pi} = \cos\pi + i\sin\pi$$

**Step 2: Substitute the trigonometric values.**
We know from standard trigonometry that:
*   $\cos\pi = -1$
*   $\sin\pi = 0$

Substitute these values back into the expression:
$$e^{i\pi} = -1 + i(0) = -1$$

**Step 3: Add 1 to the result.**
Now substitute $e^{i\pi} = -1$ into the original expression given in the question:
$$e^{i\pi} + 1 = (-1) + 1$$
$$e^{i\pi} + 1 = 0$$

*(Note: The equation $e^{i\pi} + 1 = 0$ is known as Euler's Identity, widely considered one of the most beautiful equations in mathematics because it elegantly connects the five most fundamental mathematical constants: $e, i, \pi, 1,$ and $0$.)*

**Answer:** **(b) 0**

***

### Q36. (x) (Alternative variant) $|z-2i|=2$ equation of ............ of radius .......with centre at .........

**Solution:**

We need to identify the geometric shape and parameters of the locus represented by the equation $|z - 2i| = 2$.

**Step 1: Compare with the standard geometric equation.**
In the complex plane, the distance between any arbitrary point $z$ and a fixed point $z_0$ is defined as $|z - z_0|$.
The geometric definition of a circle is the locus of all points $z$ that are equidistant (a constant radius, $r$) from a single fixed center point ($z_0$). 
Therefore, the standard mathematical equation for a circle is:
$$|z - z_0| = r$$

**Step 2: Extract the parameters.**
By directly comparing our given equation $|z - 2i| = 2$ with the standard form $|z - z_0| = r$, we can identify:
1.  **Shape:** Because it matches the distance-modulus formula exactly, the equation represents a **circle**.
2.  **Radius ($r$):** The constant value on the right side of the equation is the radius. Thus, $r = 2$.
3.  **Center ($z_0$):** The fixed point being subtracted from $z$ inside the modulus is the center. Thus, $z_0 = 2i$. 
    *   In Cartesian coordinates $(x, y)$, the point $2i$ has a real part of $0$ and an imaginary part of $2$, which corresponds to the point $(0, 2)$.

**Answer:** $|z-2i|=2$ equation of **circle** of radius **2** with centre at **$2i$ (or $(0,2)$)**.


Here are the detailed solutions for the next four questions (Q37 to Q40).

### Q37. (x) (Alternative variant) A circle of radius 1 with centre at origin can be represented by .............

**Solution:**

We need to provide the standard mathematical equation for a specific circle in the complex plane.

**Step 1: Recall the standard equation of a circle.**
In the complex plane, the distance between any arbitrary point $z$ and a fixed center point $z_0$ is expressed by the modulus $|z - z_0|$. 
A circle is the set of all points $z$ that are at a constant distance (the radius, $r$) from the center ($z_0$). 
Thus, the general equation of a circle is:
$$|z - z_0| = r$$

**Step 2: Identify the given parameters.**
*   **Radius:** $r = 1$
*   **Center:** The origin is the point $(0,0)$, which corresponds to the complex number $z_0 = 0 + 0i = 0$.

**Step 3: Substitute the parameters into the equation.**
$$|z - 0| = 1$$
$$|z| = 1$$

*(Note: This specific circle is famously known as the **unit circle** in complex analysis. In Cartesian coordinates where $z = x+iy$, this is equivalent to $\sqrt{x^2+y^2}=1$, which squares to $x^2+y^2=1$.)*

**Answer:** A circle of radius 1 with centre at origin can be represented by **$|z| = 1$**.

***

### Q38. Problem-11: Prove that, $\overline{z_1+z_2}=\overline{z_1}+\overline{z_2}$

**Solution:**

This is a fundamental property of complex conjugates stating that the conjugate of a sum is equal to the sum of the conjugates. We will prove this using the Cartesian (rectangular) form of complex numbers.

**Step 1: Define the complex numbers.**
Let $z_1$ and $z_2$ be two arbitrary complex numbers defined as:
$$z_1 = x_1 + iy_1$$
$$z_2 = x_2 + iy_2$$
where $x_1, y_1, x_2, y_2$ are real numbers.

**Step 2: Evaluate the Left-Hand Side (LHS).**
First, find the sum $z_1 + z_2$:
$$z_1 + z_2 = (x_1 + iy_1) + (x_2 + iy_2)$$
Group the real and imaginary parts:
$$z_1 + z_2 = (x_1 + x_2) + i(y_1 + y_2)$$

Now, take the complex conjugate of this sum. The conjugate is formed by changing the sign of the imaginary part:
$$\overline{z_1 + z_2} = (x_1 + x_2) - i(y_1 + y_2) \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the Right-Hand Side (RHS).**
First, find the individual complex conjugates of $z_1$ and $z_2$:
$$\overline{z_1} = x_1 - iy_1$$
$$\overline{z_2} = x_2 - iy_2$$

Now, add these two conjugates together:
$$\overline{z_1} + \overline{z_2} = (x_1 - iy_1) + (x_2 - iy_2)$$
Group the real and imaginary parts:
$$\overline{z_1} + \overline{z_2} = (x_1 + x_2) + i(-y_1 - y_2)$$
$$\overline{z_1} + \overline{z_2} = (x_1 + x_2) - i(y_1 + y_2) \quad \text{--- (Equation 2)}$$

**Step 4: Conclusion.**
Comparing Equation 1 and Equation 2, we can see they are identical.
$$\text{LHS} = \text{RHS}$$
$$\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$$
**(Proved)**

***

### Q39. Prblm-12: Prove that, $(ii) \overline{z_1-z_2}=\overline{z_1}-\overline{z_2}$

**Solution:**

Similar to the previous question, this property states that the conjugate of a difference is equal to the difference of the conjugates. We will prove this using Cartesian coordinates.

**Step 1: Define the complex numbers.**
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$ (where $x_1, y_1, x_2, y_2 \in \mathbb{R}$).

**Step 2: Evaluate the Left-Hand Side (LHS).**
First, find the difference $z_1 - z_2$:
$$z_1 - z_2 = (x_1 + iy_1) - (x_2 + iy_2)$$
Group the real and imaginary parts:
$$z_1 - z_2 = (x_1 - x_2) + i(y_1 - y_2)$$

Now, take the complex conjugate of this difference (change the sign of the imaginary part):
$$\overline{z_1 - z_2} = (x_1 - x_2) - i(y_1 - y_2) \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the Right-Hand Side (RHS).**
First, identify the individual conjugates:
$$\overline{z_1} = x_1 - iy_1$$
$$\overline{z_2} = x_2 - iy_2$$

Now, subtract the conjugate of $z_2$ from the conjugate of $z_1$:
$$\overline{z_1} - \overline{z_2} = (x_1 - iy_1) - (x_2 - iy_2)$$
Distribute the negative sign:
$$\overline{z_1} - \overline{z_2} = x_1 - iy_1 - x_2 + iy_2$$
Group the real and imaginary parts:
$$\overline{z_1} - \overline{z_2} = (x_1 - x_2) + i(-y_1 + y_2)$$
Factor out the negative sign from the imaginary part:
$$\overline{z_1} - \overline{z_2} = (x_1 - x_2) - i(y_1 - y_2) \quad \text{--- (Equation 2)}$$

**Step 4: Conclusion.**
Comparing Equation 1 and Equation 2, they are exactly the same.
$$\text{LHS} = \text{RHS}$$
$$\overline{z_1 - z_2} = \overline{z_1} - \overline{z_2}$$
**(Proved)**

***

### Q40. Prblm-12: Prove that, $(iii) \overline{z_1z_2}=\overline{z_1}\overline{z_2}$

**Solution:**

This property states that the conjugate of a product is equal to the product of the conjugates. We can prove this using either Cartesian or Polar forms. The Cartesian method is standard.

**Step 1: Define the complex numbers.**
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$ (where $x_1, y_1, x_2, y_2 \in \mathbb{R}$).

**Step 2: Evaluate the Left-Hand Side (LHS).**
First, multiply $z_1$ and $z_2$:
$$z_1 z_2 = (x_1 + iy_1)(x_2 + iy_2)$$
Expand using algebraic distribution (FOIL):
$$z_1 z_2 = x_1 x_2 + i x_1 y_2 + i y_1 x_2 + i^2 y_1 y_2$$
Since $i^2 = -1$:
$$z_1 z_2 = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + x_2 y_1)$$

Now, take the complex conjugate of this product (flip the sign of the imaginary part):
$$\overline{z_1 z_2} = (x_1 x_2 - y_1 y_2) - i(x_1 y_2 + x_2 y_1) \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the Right-Hand Side (RHS).**
Identify the individual conjugates:
$$\overline{z_1} = x_1 - iy_1$$
$$\overline{z_2} = x_2 - iy_2$$

Now, multiply these two conjugates together:
$$\overline{z_1}\overline{z_2} = (x_1 - iy_1)(x_2 - iy_2)$$
Expand using algebraic distribution:
$$\overline{z_1}\overline{z_2} = x_1 x_2 - i x_1 y_2 - i y_1 x_2 + i^2 y_1 y_2$$
Since $i^2 = -1$:
$$\overline{z_1}\overline{z_2} = x_1 x_2 - i x_1 y_2 - i y_1 x_2 - y_1 y_2$$
Group the real and imaginary parts:
$$\overline{z_1}\overline{z_2} = (x_1 x_2 - y_1 y_2) + i(-x_1 y_2 - x_2 y_1)$$
Factor out the negative sign from the imaginary part:
$$\overline{z_1}\overline{z_2} = (x_1 x_2 - y_1 y_2) - i(x_1 y_2 + x_2 y_1) \quad \text{--- (Equation 2)}$$

**Step 4: Conclusion.**
Comparing Equation 1 and Equation 2, they perfectly match.
$$\text{LHS} = \text{RHS}$$
$$\overline{z_1 z_2} = \overline{z_1}\overline{z_2}$$
**(Proved)**

*(Alternative Proof using Polar Form: Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$. Then $z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}$. The conjugate $\overline{z_1 z_2} = r_1 r_2 e^{-i(\theta_1 + \theta_2)}$. The product of conjugates is $\overline{z_1}\overline{z_2} = (r_1 e^{-i\theta_1})(r_2 e^{-i\theta_2}) = r_1 r_2 e^{-i(\theta_1 + \theta_2)}$. The expressions match, proving the theorem.)*

Here are the detailed solutions for the next four questions (Q41 to Q44).

### Q41. Prblm-12: Prove that $z\overline{z}=\vert{}z\vert{}^2$

**Solution:**

This is one of the most fundamental and frequently used identities in complex analysis. We will prove it using the Cartesian (rectangular) representation of a complex number.

**Step 1: Define the complex number.**
Let $z$ be a complex number in standard form:
$$z = x + iy$$
where $x$ and $y$ are real numbers.

**Step 2: Define its complex conjugate.**
The complex conjugate $\overline{z}$ is obtained by reversing the sign of the imaginary part:
$$\overline{z} = x - iy$$

**Step 3: Evaluate the Left-Hand Side (LHS), $z\overline{z}$.**
Multiply the complex number by its conjugate:
$$z\overline{z} = (x + iy)(x - iy)$$
This represents the algebraic difference of squares, $(a+b)(a-b) = a^2 - b^2$:
$$z\overline{z} = x^2 - (iy)^2$$
$$z\overline{z} = x^2 - i^2y^2$$
Since the imaginary unit squared is $i^2 = -1$, substitute it into the equation:
$$z\overline{z} = x^2 - (-1)y^2$$
$$z\overline{z} = x^2 + y^2 \quad \text{--- (Equation 1)}$$

**Step 4: Evaluate the Right-Hand Side (RHS), $|z|^2$.**
By definition, the modulus (or absolute value) of a complex number $z = x + iy$ is the Euclidean distance from the origin:
$$|z| = \sqrt{x^2 + y^2}$$
Squaring both sides of this definition gives:
$$|z|^2 = \left(\sqrt{x^2 + y^2}\right)^2$$
$$|z|^2 = x^2 + y^2 \quad \text{--- (Equation 2)}$$

**Step 5: Conclusion.**
Comparing Equation 1 and Equation 2, we can see that both sides are exactly equal to $x^2 + y^2$.
$$\text{LHS} = \text{RHS}$$
$$z\overline{z} = |z|^2$$
**(Proved)**

***

### Q42. Prblm-12: Prove that $\overline{z_1}z_2=\overline{z_1\overline{z_2}}$

*(Note: The original text had empty parentheses `( )`, representing a list item number, likely `(iv)`).*

**Solution:**

This property can be proved very elegantly using the properties of complex conjugates established in earlier problems (specifically, the conjugate of a product is the product of the conjugates, and the conjugate of a conjugate is the original number).

**Method 1: Using established properties**

**Step 1: Evaluate the Right-Hand Side (RHS).**
The RHS is the conjugate of the product $z_1\overline{z_2}$:
$$\text{RHS} = \overline{(z_1)(\overline{z_2})}$$

**Step 2: Apply the product rule for conjugates.**
We proved in Q40 that $\overline{AB} = \overline{A}\overline{B}$. Applying this to our RHS expression:
$$\overline{(z_1)(\overline{z_2})} = \overline{z_1} \cdot \overline{(\overline{z_2})}$$

**Step 3: Apply the involution property.**
The conjugate of a conjugate returns the original complex number. Let $z_2 = x - iy$, its conjugate is $x + iy$, and taking the conjugate again returns $x - iy$. Therefore, $\overline{(\overline{z_2})} = z_2$.
Substitute this back:
$$\text{RHS} = \overline{z_1} \cdot z_2$$

This exactly matches the Left-Hand Side (LHS).
$$\overline{z_1}z_2 = \overline{z_1\overline{z_2}}$$
**(Proved)**

**Method 2: Cartesian coordinates (for thoroughness)**
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$.
*   **LHS:** $\overline{z_1}z_2 = (x_1 - iy_1)(x_2 + iy_2) = (x_1x_2 + y_1y_2) + i(x_1y_2 - x_2y_1)$
*   **RHS Part 1 (inner):** $z_1\overline{z_2} = (x_1 + iy_1)(x_2 - iy_2) = (x_1x_2 + y_1y_2) + i(-x_1y_2 + x_2y_1)$
*   **RHS Part 2 (outer conjugate):** $\overline{z_1\overline{z_2}} = (x_1x_2 + y_1y_2) - i(-x_1y_2 + x_2y_1) = (x_1x_2 + y_1y_2) + i(x_1y_2 - x_2y_1)$
The expanded LHS perfectly matches the expanded RHS. **(Proved)**

***

### Q43. Prblm-12: Prove that, $z_1\overline{z_2} + \overline{z_1}z_2 = 2Re(z_1\overline{z_2})$

**Solution:**

We need to prove that the sum of a specific complex product and its conjugate results in twice the real part of that product.

**Step 1: Let $w$ be a new complex number.**
Let us define $w$ as the product inside the real operator on the Right-Hand Side:
$$w = z_1\overline{z_2}$$

**Step 2: Find the complex conjugate of $w$.**
Using the properties from the previous question (Q42):
$$\overline{w} = \overline{z_1\overline{z_2}}$$
$$\overline{w} = \overline{z_1} \cdot \overline{\overline{z_2}}$$
$$\overline{w} = \overline{z_1}z_2$$

**Step 3: Rewrite the Left-Hand Side (LHS) using $w$.**
Looking at the intended correct LHS ($z_1\overline{z_2} + \overline{z_1}z_2$), we can now substitute $w$ and $\overline{w}$:
$$\text{LHS} = w + \overline{w}$$

**Step 4: Evaluate $w + \overline{w}$.**
Every complex number $w$ can be expressed in terms of its real and imaginary parts. 
Let $w = u + iv$, where $u = Re(w)$ and $v = Im(w)$.
Then its conjugate is $\overline{w} = u - iv$.

Add them together:
$$w + \overline{w} = (u + iv) + (u - iv)$$
$$w + \overline{w} = u + u + iv - iv$$
$$w + \overline{w} = 2u$$

**Step 5: Substitute back the original variables.**
Since $u$ is the real part of $w$, we have $2u = 2Re(w)$.
Substitute $w = z_1\overline{z_2}$ back into the equation:
$$z_1\overline{z_2} + \overline{z_1}z_2 = 2Re(z_1\overline{z_2})$$
**(Proved)**

***

### Q44. Prblm-13: Prove that $\vert{}z_1+z_2\vert{}\le\vert{}z_1\vert{}+\vert{}z_2\vert{}$ and $(ii) \vert{}z_1+z_2+z_3\vert{}\le\vert{}z_1\vert{}+\vert{}z_2\vert{}+\vert{}z_3\vert{}$

**Solution:**

This is the famous **Triangle Inequality** in complex analysis. 

**Part (i): Prove $|z_1 + z_2| \le |z_1| + |z_2|$**

**Step 1: Square the left side to avoid square roots.**
Using the property $|z|^2 = z\overline{z}$ (proven in Q41):
$$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)}$$

**Step 2: Apply conjugate properties and expand.**
Since $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$:
$$|z_1 + z_2|^2 = (z_1 + z_2)(\overline{z_1} + \overline{z_2})$$
Multiply the terms (FOIL):
$$|z_1 + z_2|^2 = z_1\overline{z_1} + z_1\overline{z_2} + z_2\overline{z_1} + z_2\overline{z_2}$$

**Step 3: Simplify using modulus properties.**
We know $z_1\overline{z_1} = |z_1|^2$ and $z_2\overline{z_2} = |z_2|^2$. Also, note that $z_2\overline{z_1} = \overline{z_1\overline{z_2}}$.
$$|z_1 + z_2|^2 = |z_1|^2 + z_1\overline{z_2} + \overline{z_1\overline{z_2}} + |z_2|^2$$

From Q43, we proved that $w + \overline{w} = 2Re(w)$. Let $w = z_1\overline{z_2}$:
$$|z_1 + z_2|^2 = |z_1|^2 + 2Re(z_1\overline{z_2}) + |z_2|^2$$

**Step 4: Use the real part inequality.**
For any complex number $w = x+iy$, its real part $x$ is always less than or equal to its modulus $\sqrt{x^2+y^2}$. Therefore, $Re(w) \le |w|$.
Applying this to our equation:
$$2Re(z_1\overline{z_2}) \le 2|z_1\overline{z_2}|$$
Since $|z_1\overline{z_2}| = |z_1||\overline{z_2}| = |z_1||z_2|$:
$$2Re(z_1\overline{z_2}) \le 2|z_1||z_2|$$

**Step 5: Substitute the inequality back into the main equation.**
$$|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2$$
The right side is a perfect square $(a^2 + 2ab + b^2 = (a+b)^2)$:
$$|z_1 + z_2|^2 \le (|z_1| + |z_2|)^2$$

Because the modulus is always non-negative, we can take the square root of both sides without altering the inequality sign:
$$|z_1 + z_2| \le |z_1| + |z_2|$$
**(Proved Part i)**

---

**Part (ii): Prove $|z_1 + z_2 + z_3| \le |z_1| + |z_2| + |z_3|$**

This can be proved easily by directly applying the result from Part (i).

**Step 1: Group the terms to apply the Triangle Inequality.**
Treat $(z_1 + z_2)$ as a single complex number $Z$.
$$|z_1 + z_2 + z_3| = |(z_1 + z_2) + z_3|$$

**Step 2: Apply the Triangle Inequality for two numbers.**
Using Part (i) where the two numbers are $(z_1 + z_2)$ and $z_3$:
$$|(z_1 + z_2) + z_3| \le |z_1 + z_2| + |z_3| \quad \text{--- (Inequality 1)}$$

**Step 3: Apply the Triangle Inequality again.**
We know from Part (i) that $|z_1 + z_2| \le |z_1| + |z_2|$. 
Substitute this into Inequality 1:
$$|z_1 + z_2| + |z_3| \le (|z_1| + |z_2|) + |z_3|$$

**Step 4: Conclude the final statement.**
Tracing the inequalities from start to finish:
$$|z_1 + z_2 + z_3| \le |z_1| + |z_2| + |z_3|$$
**(Proved Part ii)**






Here are the detailed solutions for the next four questions (Q45 to Q48).

### Q45. Prblm-1.4: Prove that $(i) \vert{}z_1z_2\vert{}=\vert{}z_1\vert{}\vert{}z_2\vert{}$, $(ii) \vert{}z_1-z_2\vert{}\ge\vert{}z_1\vert{}-\vert{}z_2\vert{}$, $(iii) \vert{}\overline{z}\vert{}=\vert{}z\vert{}$

**Solution:**

**Part (i): Prove $|z_1 z_2| = |z_1| |z_2|$**
*Method: Using properties of conjugates.*
1. Square the left-hand side to avoid square roots: $|z_1 z_2|^2$.
2. Use the property $|w|^2 = w\overline{w}$: 
   $|z_1 z_2|^2 = (z_1 z_2)\overline{(z_1 z_2)}$
3. Use the conjugate of a product property ($\overline{AB} = \overline{A}\overline{B}$):
   $|z_1 z_2|^2 = (z_1 z_2)(\overline{z_1} \cdot \overline{z_2})$
4. Commute the terms (since complex multiplication is commutative):
   $|z_1 z_2|^2 = (z_1\overline{z_1})(z_2\overline{z_2})$
5. Substitute $|z|^2$ back in for $z\overline{z}$:
   $|z_1 z_2|^2 = |z_1|^2 |z_2|^2$
6. Take the positive square root of both sides (since moduli are non-negative real numbers):
   $|z_1 z_2| = |z_1| |z_2|$ **(Proved)**

**Part (ii): Prove $|z_1 - z_2| \ge |z_1| - |z_2|$**
*Method: Using the Triangle Inequality proved in Q44 ($|A+B| \le |A| + |B|$).*
1. Let $A = z_1 - z_2$ and $B = z_2$.
2. We can express $z_1$ as the sum of $A$ and $B$:
   $z_1 = (z_1 - z_2) + z_2$
3. Apply the absolute value (modulus) to both sides:
   $|z_1| = |(z_1 - z_2) + z_2|$
4. Apply the standard Triangle Inequality ($|A+B| \le |A| + |B|$) to the right side:
   $|z_1| = |(z_1 - z_2) + z_2| \le |z_1 - z_2| + |z_2|$
   Therefore, $|z_1| \le |z_1 - z_2| + |z_2|$
5. Subtract $|z_2|$ from both sides of the inequality:
   $|z_1| - |z_2| \le |z_1 - z_2|$
6. Rearrange to match the required format:
   $|z_1 - z_2| \ge |z_1| - |z_2|$ **(Proved)**

**Part (iii): Prove $|\overline{z}| = |z|$**
*Method: Using Cartesian coordinates.*
1. Let $z = x + iy$.
2. By definition, its modulus is $|z| = \sqrt{x^2 + y^2}$.
3. The complex conjugate is $\overline{z} = x - iy$.
4. Calculate the modulus of the conjugate:
   $|\overline{z}| = \sqrt{x^2 + (-y)^2}$
5. Since the square of a negative number is positive ($(-y)^2 = y^2$):
   $|\overline{z}| = \sqrt{x^2 + y^2}$
6. Comparing the two expressions:
   $|\overline{z}| = |z|$ **(Proved)**

***

### Q46. Prblm-1-5: find the valur of, $(i) \vert{}e^z\vert{}$, $(ii) \vert{}e^{iz}\vert{}$

**Solution:**

Let the complex variable $z$ be defined in Cartesian coordinates as $z = x + iy$, where $x$ and $y$ are real numbers.

**Part (i): Find the value of $|e^z|$**
1. Substitute $z = x + iy$ into the exponential expression:
   $e^z = e^{x+iy}$
2. Apply the exponent rule $a^{m+n} = a^m \cdot a^n$:
   $e^z = e^x \cdot e^{iy}$
3. To find the modulus, take the absolute value of the product. The modulus of a product is the product of moduli:
   $|e^z| = |e^x \cdot e^{iy}| = |e^x| \cdot |e^{iy}|$
4. Evaluate the individual moduli:
   *   Since $x$ is real, $e^x$ is a positive real number. Therefore, $|e^x| = e^x$.
   *   Using Euler's formula, $e^{iy} = \cos y + i\sin y$. Its modulus is $\sqrt{\cos^2 y + \sin^2 y} = \sqrt{1} = 1$. Therefore, $|e^{iy}| = 1$.
5. Multiply them together:
   $|e^z| = e^x \cdot 1 = e^x$

**Answer (i): $|e^z| = e^x$** (where $x = Re(z)$).

---

**Part (ii): Find the value of $|e^{iz}|$**
1. Substitute $z = x + iy$ into the expression $iz$:
   $iz = i(x + iy) = ix + i^2y = ix - y = -y + ix$
2. Substitute this back into the exponential expression:
   $e^{iz} = e^{-y + ix}$
3. Apply the exponent rule:
   $e^{iz} = e^{-y} \cdot e^{ix}$
4. Take the modulus of the product:
   $|e^{iz}| = |e^{-y} \cdot e^{ix}| = |e^{-y}| \cdot |e^{ix}|$
5. Evaluate the individual moduli:
   *   Since $y$ is real, $-y$ is real, so $e^{-y}$ is a positive real number. Thus, $|e^{-y}| = e^{-y}$.
   *   Since $x$ is real, by Euler's formula, $|e^{ix}| = \sqrt{\cos^2 x + \sin^2 x} = 1$.
6. Multiply them together:
   $|e^{iz}| = e^{-y} \cdot 1 = e^{-y}$

**Answer (ii): $|e^{iz}| = e^{-y}$** (where $y = Im(z)$).

***

### Q47. Example 13.3: Find the modulus , argument & polar form of the complex number. 
$a) z_1=5$
$b) z_2=-3i$
$c) z_3=\sqrt{3}+i$ (Note: fixing typo in original text from `\sqrt{3}+1` to `\sqrt{3}+i` based on standard problems and feruj sheet equivalent Q69).
$d) z_4=1+i$
$e) z_6=-1-i$
$f) z_5=1-i$
$g) z_7=\frac{-1+i\sqrt{2}}{2}$

**Solution:**

For each complex number $z = x+iy$, we calculate:
*   **Modulus:** $r = \sqrt{x^2+y^2}$
*   **Argument (Principal):** $\theta = \tan^{-1}(y/x)$, adjusted for the correct quadrant to be within $(-\pi, \pi]$.
*   **Polar Form:** $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$

**a) $z_1 = 5$** (or $5 + 0i$)
*   **Modulus:** $r = \sqrt{5^2+0^2} = 5$
*   **Argument:** Point is on the positive real axis, so $\theta = 0$.
*   **Polar Form:** $5(\cos 0 + i\sin 0)$ or $5e^{i0}$

**b) $z_2 = -3i$** (or $0 - 3i$)
*   **Modulus:** $r = \sqrt{0^2+(-3)^2} = 3$
*   **Argument:** Point is on the negative imaginary axis, so $\theta = -\pi/2$.
*   **Polar Form:** $3\left(\cos\left(-\frac{\pi}{2}\right) + i\sin\left(-\frac{\pi}{2}\right)\right)$ or $3e^{-i\pi/2}$

**c) $z_3 = \sqrt{3} + i$**
*   **Modulus:** $r = \sqrt{(\sqrt{3})^2+1^2} = \sqrt{3+1} = 2$
*   **Argument:** First quadrant. $\theta = \tan^{-1}(1/\sqrt{3}) = \pi/6$.
*   **Polar Form:** $2\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$ or $2e^{i\pi/6}$

**d) $z_4 = 1 + i$**
*   **Modulus:** $r = \sqrt{1^2+1^2} = \sqrt{2}$
*   **Argument:** First quadrant. $\theta = \tan^{-1}(1/1) = \pi/4$.
*   **Polar Form:** $\sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$ or $\sqrt{2}e^{i\pi/4}$

**e) $z_6 = -1 - i$**
*   **Modulus:** $r = \sqrt{(-1)^2+(-1)^2} = \sqrt{2}$
*   **Argument:** Third quadrant. Reference angle $\alpha = \pi/4$. Principal $\theta = -\pi + \pi/4 = -3\pi/4$.
*   **Polar Form:** $\sqrt{2}\left(\cos\left(-\frac{3\pi}{4}\right) + i\sin\left(-\frac{3\pi}{4}\right)\right)$ or $\sqrt{2}e^{-i3\pi/4}$

**f) $z_5 = 1 - i$**
*   **Modulus:** $r = \sqrt{1^2+(-1)^2} = \sqrt{2}$
*   **Argument:** Fourth quadrant. $\theta = \tan^{-1}(-1/1) = -\pi/4$.
*   **Polar Form:** $\sqrt{2}\left(\cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right)\right)$ or $\sqrt{2}e^{-i\pi/4}$

**g) $z_7 = -\frac{1}{2} + i\frac{\sqrt{2}}{2}$**
*   **Modulus:** $r = \sqrt{(-\frac{1}{2})^2 + (\frac{\sqrt{2}}{2})^2} = \sqrt{\frac{1}{4} + \frac{2}{4}} = \sqrt{\frac{3}{4}} = \frac{\sqrt{3}}{2}$
*   **Argument:** Second quadrant. $\alpha = \tan^{-1}\left(\frac{\sqrt{2}/2}{1/2}\right) = \tan^{-1}(\sqrt{2})$. $\theta = \pi - \tan^{-1}(\sqrt{2})$.
*   **Polar Form:** $\frac{\sqrt{3}}{2}(\cos\theta + i\sin\theta)$ where $\theta = \pi - \tan^{-1}(\sqrt{2})$.

***

### Q48. Ques: If $z=6 e^{i\pi/3}$ Evaluate, $\vert{}e^{iz}\vert{}$

**Solution:**

This is the exact same problem conceptually and numerically as Q17, but we'll provide the detailed steps here again for completeness.

**Step 1: Convert $z$ from polar form to Cartesian form.**
The given complex number is $z = 6e^{i\frac{\pi}{3}}$. 
Using Euler's formula, $e^{i\theta} = \cos\theta + i\sin\theta$:
$$z = 6 \left( \cos\frac{\pi}{3} + i\sin\frac{\pi}{3} \right)$$
Using standard trigonometric values ($\cos 60^\circ = 1/2$, $\sin 60^\circ = \sqrt{3}/2$):
$$z = 6 \left( \frac{1}{2} + i\frac{\sqrt{3}}{2} \right)$$
Distribute the 6:
$$z = 3 + 3\sqrt{3}i$$

**Step 2: Substitute $z$ into the expression $iz$.**
Multiply $z$ by $i$:
$$iz = i(3 + 3\sqrt{3}i)$$
$$iz = 3i + 3\sqrt{3}i^2$$
Since $i^2 = -1$:
$$iz = 3i - 3\sqrt{3}$$
Rewrite in standard real+imaginary form:
$$iz = -3\sqrt{3} + 3i$$

**Step 3: Evaluate the modulus $|e^{iz}|$.**
*(Note: As derived in Q46 Part (ii), $|e^{iz}| = e^{-y}$ where $y$ is the imaginary part of $z$. Here $y = 3\sqrt{3}$, so the answer should be $e^{-3\sqrt{3}}$. Let's prove it directly to be sure).*

Substitute $iz$ into the exponential:
$$e^{iz} = e^{-3\sqrt{3} + 3i}$$
Separate the real and imaginary exponents:
$$e^{iz} = e^{-3\sqrt{3}} \cdot e^{3i}$$
Take the modulus of both sides:
$$|e^{iz}| = |e^{-3\sqrt{3}} \cdot e^{3i}|$$
$$|e^{iz}| = |e^{-3\sqrt{3}}| \cdot |e^{3i}|$$

*   Since $-3\sqrt{3}$ is a real number, $e^{-3\sqrt{3}}$ is a positive real number, so $|e^{-3\sqrt{3}}| = e^{-3\sqrt{3}}$.
*   Using Euler's formula, $|e^{i(3)}| = \sqrt{\cos^2(3) + \sin^2(3)} = 1$.

Therefore:
$$|e^{iz}| = e^{-3\sqrt{3}} \cdot 1 = e^{-3\sqrt{3}}$$

**Answer:** **$|e^{iz}| = e^{-3\sqrt{3}}$**

Here are the detailed solutions for the next four questions (Q49 to Q52).

### Q49. Prblm-2-1: Prove that, $(i) \arg(z_1z_2)=\arg z_1+\arg z_2$, $(ii) \arg\overline{z}=-\arg z$

**Solution:**

We will prove these fundamental properties of complex arguments using the polar (exponential) form of complex numbers.

**Part (i): Prove $\arg(z_1 z_2) = \arg z_1 + \arg z_2$**

**Step 1: Define the complex numbers in polar form.**
Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$.
By definition, the arguments are:
$\arg(z_1) = \theta_1$
$\arg(z_2) = \theta_2$

**Step 2: Multiply the two complex numbers.**
$$z_1 z_2 = (r_1 e^{i\theta_1}) \cdot (r_2 e^{i\theta_2})$$
Group the moduli and the exponential terms:
$$z_1 z_2 = (r_1 r_2) \cdot e^{i\theta_1} e^{i\theta_2}$$

**Step 3: Apply the laws of exponents.**
Using the rule $e^a \cdot e^b = e^{a+b}$:
$$z_1 z_2 = (r_1 r_2) e^{i(\theta_1 + \theta_2)}$$

**Step 4: Identify the argument of the product.**
The product is now in the standard polar form $R e^{i\Theta}$, where $R = r_1 r_2$ is the modulus and $\Theta = \theta_1 + \theta_2$ is the argument.
$$\arg(z_1 z_2) = \theta_1 + \theta_2$$

Substitute back $\arg(z_1)$ and $\arg(z_2)$:
$$\arg(z_1 z_2) = \arg(z_1) + \arg(z_2)$$
*(Note: This equality holds true up to an integer multiple of $2\pi$ to account for the periodic nature of angles).*
**(Proved)**

---

**Part (ii): Prove $\arg(\overline{z}) = -\arg z$**

**Step 1: Define the complex number in polar form.**
Let $z = r e^{i\theta}$.
By definition, its argument is:
$\arg(z) = \theta$

**Step 2: Find the complex conjugate.**
In Cartesian form, if $z = x + iy$, then $\overline{z} = x - iy$.
In polar form, changing the sign of the imaginary part is equivalent to changing the sign of the angle.
Euler's formula states: $z = r(\cos\theta + i\sin\theta)$.
The conjugate is: $\overline{z} = r(\cos\theta - i\sin\theta)$.
Since cosine is an even function ($\cos(-\theta) = \cos\theta$) and sine is an odd function ($-\sin\theta = \sin(-\theta)$):
$$\overline{z} = r(\cos(-\theta) + i\sin(-\theta))$$
In exponential form, this is:
$$\overline{z} = r e^{-i\theta}$$

**Step 3: Identify the argument of the conjugate.**
The conjugate is in the standard polar form $r e^{i\Theta}$, where $\Theta = -\theta$.
$$\arg(\overline{z}) = -\theta$$

Substitute back $\theta = \arg(z)$:
$$\arg(\overline{z}) = -\arg(z)$$
**(Proved)**

***

### Q50. Prblm-2.3: Express $-6-\sqrt{2}i$ in polar form.

**Solution:**

We need to convert the complex number $z = -6 - \sqrt{2}i$ into the standard polar form $z = r(\cos\theta + i\sin\theta)$.

**Step 1: Identify the Cartesian coordinates.**
Let $z = x + iy$.
Here, the real part is $x = -6$ and the imaginary part is $y = -\sqrt{2}$.

**Step 2: Calculate the Modulus ($r$).**
The modulus is the distance from the origin:
$$r = |z| = \sqrt{x^2 + y^2}$$
$$r = \sqrt{(-6)^2 + (-\sqrt{2})^2}$$
$$r = \sqrt{36 + 2}$$
$$r = \sqrt{38}$$

**Step 3: Calculate the Argument ($\theta$).**
The argument $\theta$ is the angle made with the positive real axis.
Since both $x$ and $y$ are negative, the point $(-6, -\sqrt{2})$ lies in the **third quadrant**.

First, let's find the reference angle $\alpha$ in the first quadrant:
$$\alpha = \tan^{-1}\left(\left| \frac{y}{x} \right|\right) = \tan^{-1}\left(\frac{\sqrt{2}}{6}\right)$$

Now, we adjust the angle for the third quadrant to find the principal argument $\theta$ (which must be in the range $-\pi < \theta \le \pi$):
$$\theta = -\pi + \alpha$$
$$\theta = -\pi + \tan^{-1}\left(\frac{\sqrt{2}}{6}\right)$$

*(Alternatively, a positive argument in the range $0 \le \theta < 2\pi$ would be $\theta = \pi + \tan^{-1}(\frac{\sqrt{2}}{6})$).*

**Step 4: Write the polar form.**
Substitute the modulus $r$ and argument $\theta$ into the polar form structure:
$$z = \sqrt{38} \left( \cos\left(-\pi + \tan^{-1}\left(\frac{\sqrt{2}}{6}\right)\right) + i\sin\left(-\pi + \tan^{-1}\left(\frac{\sqrt{2}}{6}\right)\right) \right)$$

This is the exact polar representation. If numerical approximations are acceptable:
$r = \sqrt{38} \approx 6.164$
$\alpha \approx \tan^{-1}(0.2357) \approx 0.231$ radians (or $13.26^\circ$)
$\theta \approx -\pi + 0.231 \approx -2.91$ radians (or $-166.74^\circ$)

**Answer:** 
The exact polar form is **$z = \sqrt{38}(\cos\theta + i\sin\theta)$**, where **$\theta = -\pi + \tan^{-1}\left(\frac{\sqrt{2}}{6}\right)$**.

***

### Q51. Ques: State & Prove De-Moiver's Theorem: For any positive integer n then $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$

**Solution:**

**Statement:**
De Moivre's Theorem states that for any real number $\theta$ and any positive integer $n$, the $n$-th power of the complex number $(\cos\theta + i\sin\theta)$ is given by multiplying the angle by $n$:
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

**Proof (using the Principle of Mathematical Induction):**

**Step 1: Base Case ($n=1$)**
Let's check if the theorem holds true for $n=1$.
LHS: $(\cos\theta + i\sin\theta)^1 = \cos\theta + i\sin\theta$
RHS: $\cos(1\cdot\theta) + i\sin(1\cdot\theta) = \cos\theta + i\sin\theta$
Since LHS = RHS, the theorem is true for $n=1$.

**Step 2: Inductive Hypothesis**
Assume that the theorem is true for some arbitrary positive integer $k$. That is, assume:
$$(\cos\theta + i\sin\theta)^k = \cos(k\theta) + i\sin(k\theta) \quad \text{--- (Equation 1)}$$

**Step 3: Inductive Step ($n=k+1$)**
We must now prove that if the theorem is true for $k$, it must also be true for $k+1$.
Consider the expression for $n = k+1$:
$$(\cos\theta + i\sin\theta)^{k+1}$$

Using the laws of exponents, split the term:
$$= (\cos\theta + i\sin\theta)^k \cdot (\cos\theta + i\sin\theta)^1$$

Substitute Equation 1 (our inductive hypothesis) into the first part:
$$= (\cos(k\theta) + i\sin(k\theta)) \cdot (\cos\theta + i\sin\theta)$$

Now, multiply these two complex numbers together using algebraic expansion (FOIL):
$$= \cos(k\theta)\cos\theta + i\cos(k\theta)\sin\theta + i\sin(k\theta)\cos\theta + i^2\sin(k\theta)\sin\theta$$

Since $i^2 = -1$, replace $i^2$ and group the real and imaginary parts:
Real part: $\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta$
Imaginary part: $i(\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta)$

$$= [\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta] + i[\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta]$$

**Step 4: Apply Trigonometric Identities**
Recall the standard compound angle formulas for cosine and sine:
*   $\cos(A + B) = \cos A\cos B - \sin A\sin B$
*   $\sin(A + B) = \sin A\cos B + \cos A\sin B$

Applying these identities to our real and imaginary parts (with $A = k\theta$ and $B = \theta$):
Real part becomes: $\cos(k\theta + \theta) = \cos((k+1)\theta)$
Imaginary part becomes: $\sin(k\theta + \theta) = \sin((k+1)\theta)$

Substitute these back into the expression:
$$= \cos((k+1)\theta) + i\sin((k+1)\theta)$$

**Step 5: Conclusion**
We have shown that if the formula holds for $n=k$, it also holds for $n=k+1$. Since it holds for the base case $n=1$, by the Principle of Mathematical Induction, De Moivre's Theorem is true for all positive integers $n$. **(Proved)**

***

### Q52. Example-1.38: (Double Angle Identities) Use De-moiver's identity with $n=2$ to derive the double-angle formulas for $\cos 2\theta$ & $\sin 2\theta$

**Solution:**

De Moivre's Theorem provides a very elegant and quick way to derive multiple-angle trigonometric identities.

**Step 1: State De Moivre's theorem for $n=2$.**
According to De Moivre's theorem:
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$
Setting $n=2$, we get:
$$(\cos\theta + i\sin\theta)^2 = \cos(2\theta) + i\sin(2\theta) \quad \text{--- (Equation 1)}$$

**Step 2: Expand the left-hand side algebraically.**
Instead of using De Moivre's theorem, we can expand the expression $(\cos\theta + i\sin\theta)^2$ using the standard algebraic binomial squared formula: $(a+b)^2 = a^2 + 2ab + b^2$.

Let $a = \cos\theta$ and $b = i\sin\theta$:
$$(\cos\theta + i\sin\theta)^2 = (\cos\theta)^2 + 2(\cos\theta)(i\sin\theta) + (i\sin\theta)^2$$
$$(\cos\theta + i\sin\theta)^2 = \cos^2\theta + 2i\sin\theta\cos\theta + i^2\sin^2\theta$$

Since $i^2 = -1$, substitute it into the last term:
$$(\cos\theta + i\sin\theta)^2 = \cos^2\theta + 2i\sin\theta\cos\theta - \sin^2\theta$$

Now, group the real and imaginary parts together:
$$(\cos\theta + i\sin\theta)^2 = (\cos^2\theta - \sin^2\theta) + i(2\sin\theta\cos\theta) \quad \text{--- (Equation 2)}$$

**Step 3: Equate Equation 1 and Equation 2.**
Since both Equation 1 and Equation 2 represent the exact same quantity $(\cos\theta + i\sin\theta)^2$, their right-hand sides must be equal:
$$\cos(2\theta) + i\sin(2\theta) = (\cos^2\theta - \sin^2\theta) + i(2\sin\theta\cos\theta)$$

**Step 4: Extract the double-angle formulas.**
For two complex numbers to be strictly equal, their real parts must be equal to each other, and their imaginary parts must be equal to each other.

*   **Equating the Real parts:**
    $$\cos(2\theta) = \cos^2\theta - \sin^2\theta$$

*   **Equating the Imaginary parts (the coefficients of $i$):**
    $$\sin(2\theta) = 2\sin\theta\cos\theta$$

These are exactly the standard double-angle trigonometric identities. 
**(Derived successfully)**

Here are the detailed solutions for the next four questions (Q53 to Q56).

*Note on the text: In questions Q54, Q55, and Q56, the second part of the prompt says "locate the value of $z^5$" or "$n^5$". This is a standard typographical/copy-paste error in the original source material. It is intended to say "locate the roots graphically in the complex plane," which is standard for these types of problems. The solutions below reflect this correct interpretation.*

### Q53. Problem-3-1: Prove that, $e^{i\theta}=e^{i(\theta+2k\pi)}$ , $K=0,\pm1,\pm2,$

**Solution:**

This question asks us to prove the $2\pi$-periodicity of the complex exponential function.

**Step 1: Start with the Right-Hand Side (RHS).**
$$\text{RHS} = e^{i(\theta + 2k\pi)}$$

**Step 2: Expand the exponent.**
Using the standard rule of exponents $e^{a+b} = e^a \cdot e^b$, we can separate the terms:
$$e^{i(\theta + 2k\pi)} = e^{i\theta + i2k\pi} = e^{i\theta} \cdot e^{i2k\pi}$$

**Step 3: Evaluate $e^{i2k\pi}$ using Euler's formula.**
Euler's formula states that $e^{i\phi} = \cos\phi + i\sin\phi$. 
Let $\phi = 2k\pi$:
$$e^{i2k\pi} = \cos(2k\pi) + i\sin(2k\pi)$$

**Step 4: Apply the properties of trigonometric functions.**
For any integer $k$ ($0, \pm1, \pm2, \dots$):
*   $2k\pi$ represents full rotations around the unit circle.
*   The cosine of any full integer multiple of $2\pi$ is always $1$: $\cos(2k\pi) = 1$
*   The sine of any full integer multiple of $2\pi$ is always $0$: $\sin(2k\pi) = 0$

Substitute these values back:
$$e^{i2k\pi} = 1 + i(0) = 1$$

**Step 5: Conclude the proof.**
Substitute $e^{i2k\pi} = 1$ back into the separated exponential expression from Step 2:
$$\text{RHS} = e^{i\theta} \cdot (1) = e^{i\theta}$$
This perfectly matches the Left-Hand Side (LHS).
$$e^{i\theta} = e^{i(\theta + 2k\pi)}$$
**(Proved)**

***

### Q54. Prblm-3.2: a) find the roots of $z^5+32=0$ b) locate the value of $z^5$ in the complex plane.

**Solution:**

**Part a) Find the roots of $z^5 + 32 = 0$**

**Step 1: Isolate $z$.**
$$z^5 = -32$$
$$z = (-32)^{\frac{1}{5}}$$
We need to find the five $5^{\text{th}}$ roots of the complex number $w = -32$ (or $-32 + 0i$).

**Step 2: Express $w = -32$ in polar form.**
*   **Modulus ($r$):** The distance from the origin to $-32$ on the real axis is $|-32| = 32$.
*   **Argument ($\theta$):** Since it lies on the negative real axis, the angle is exactly $\pi$ radians ($180^\circ$).

Including the periodic rotations, the general polar form is:
$$w = 32 \left( \cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi) \right)$$

**Step 3: Apply De Moivre's Theorem for roots.**
$$z_k = w^{\frac{1}{5}} = (32)^{\frac{1}{5}} \left[ \cos\left(\frac{\pi + 2k\pi}{5}\right) + i\sin\left(\frac{\pi + 2k\pi}{5}\right) \right]$$
*   The magnitude for all roots is $R = 32^{\frac{1}{5}} = (2^5)^{\frac{1}{5}} = 2$.
*   The angles are $\alpha_k = \frac{\pi + 2k\pi}{5}$ for $k = 0, 1, 2, 3, 4$.

**Step 4: Calculate the individual roots (converting to degrees for clarity).**
Since $\pi = 180^\circ$, $\frac{\pi}{5} = 36^\circ$ and $\frac{2\pi}{5} = 72^\circ$.
*   **$k = 0$:** $\alpha_0 = 36^\circ \implies z_0 = 2(\cos 36^\circ + i\sin 36^\circ)$
*   **$k = 1$:** $\alpha_1 = 36^\circ + 72^\circ = 108^\circ \implies z_1 = 2(\cos 108^\circ + i\sin 108^\circ)$
*   **$k = 2$:** $\alpha_2 = 108^\circ + 72^\circ = 180^\circ \implies z_2 = 2(\cos 180^\circ + i\sin 180^\circ) = -2$
*   **$k = 3$:** $\alpha_3 = 180^\circ + 72^\circ = 252^\circ \implies z_3 = 2(\cos 252^\circ + i\sin 252^\circ)$
*   **$k = 4$:** $\alpha_4 = 252^\circ + 72^\circ = 324^\circ \implies z_4 = 2(\cos 324^\circ + i\sin 324^\circ)$

**Part b) Locate the roots graphically in the complex plane.**
*(Assuming the prompt intends to ask to plot the roots derived above).*
1.  Draw a circle centered at the origin $(0,0)$ with a radius of exactly $R = 2$.
2.  The five roots lie evenly spaced on the circumference of this circle, separated by exactly $72^\circ$.
3.  They form the vertices of a **regular pentagon**.
4.  One root ($z_2$) sits squarely on the negative real axis at $(-2, 0)$. The others are symmetric pairs across the real axis in the remaining quadrants.

***

### Q55. Prblm-3.3: a) find the roots of $z=(-1+i)^{1/3}$ b) locate the value of $n^5$ in the complex plane.

*(Note: This is numerically identical to Q6. The second part is a typo for "locate the roots").*

**Solution:**

We need to find the three cube roots of the complex number $w = -1 + i$.

**Part a) Find the roots**

**Step 1: Express $w = -1 + i$ in polar form.**
Let $x = -1$ and $y = 1$.
*   **Modulus ($r$):** $r = \sqrt{(-1)^2 + 1^2} = \sqrt{2}$
*   **Argument ($\theta$):** Second quadrant. $\theta = \pi + \tan^{-1}(1/-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$.

General polar form:
$$w = 2^{\frac{1}{2}} \left[ \cos\left(\frac{3\pi}{4} + 2k\pi\right) + i\sin\left(\frac{3\pi}{4} + 2k\pi\right) \right]$$

**Step 2: Apply De Moivre's Theorem for roots.**
$$z_k = w^{\frac{1}{3}} = \left( 2^{\frac{1}{2}} \right)^{\frac{1}{3}} \left[ \cos\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) + i\sin\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) \right]$$
*   Magnitude: $R = 2^{\frac{1}{6}} \approx 1.122$
*   Angles: $\alpha_k = \frac{3\pi + 8k\pi}{12}$ for $k = 0, 1, 2$.

**Step 3: Calculate the individual roots.**
*   **$k = 0$:** $\alpha_0 = \frac{3\pi}{12} = \frac{\pi}{4} = 45^\circ \implies z_0 = 2^{\frac{1}{6}} \left( \cos 45^\circ + i\sin 45^\circ \right)$
*   **$k = 1$:** $\alpha_1 = \frac{11\pi}{12} = 165^\circ \implies z_1 = 2^{\frac{1}{6}} \left( \cos 165^\circ + i\sin 165^\circ \right)$
*   **$k = 2$:** $\alpha_2 = \frac{19\pi}{12} = 285^\circ \implies z_2 = 2^{\frac{1}{6}} \left( \cos 285^\circ + i\sin 285^\circ \right)$

**Part b) Locate the roots in the complex plane.**
1.  Draw a circle at the origin with a radius of $2^{\frac{1}{6}}$.
2.  The three roots are spaced exactly $120^\circ$ apart on this circle.
3.  They form the vertices of an **equilateral triangle**.
4.  Plot $z_0$ in Quadrant I ($45^\circ$), $z_1$ in Quadrant II ($165^\circ$), and $z_2$ in Quadrant IV ($285^\circ$).

***

### Q56. Prblm-3: a) find the roots of $z=(-2\sqrt{3}-2i)^{1/4}$ b) locate the value of $z^5$ in the complex plane

**Solution:**

We need to find the four $4^{\text{th}}$ roots of the complex number $w = -2\sqrt{3} - 2i$.

**Part a) Find the roots**

**Step 1: Express $w = -2\sqrt{3} - 2i$ in polar form.**
Let $x = -2\sqrt{3}$ and $y = -2$.
*   **Modulus ($r$):** 
    $r = \sqrt{(-2\sqrt{3})^2 + (-2)^2} = \sqrt{4(3) + 4} = \sqrt{12 + 4} = \sqrt{16} = 4$.
*   **Argument ($\theta$):** 
    Since both $x$ and $y$ are negative, it is in the third quadrant. 
    Reference angle $\alpha = \tan^{-1}\left|\frac{-2}{-2\sqrt{3}}\right| = \tan^{-1}\left(\frac{1}{\sqrt{3}}\right) = 30^\circ$ (or $\frac{\pi}{6}$).
    Using positive angles for easier root calculation: $\theta = 180^\circ + 30^\circ = 210^\circ$ (or $\frac{7\pi}{6}$).

General polar form:
$$w = 4 \left[ \cos(210^\circ + k \cdot 360^\circ) + i\sin(210^\circ + k \cdot 360^\circ) \right]$$

**Step 2: Apply De Moivre's Theorem for roots.**
$$z_k = w^{\frac{1}{4}} = 4^{\frac{1}{4}} \left[ \cos\left(\frac{210^\circ + k \cdot 360^\circ}{4}\right) + i\sin\left(\frac{210^\circ + k \cdot 360^\circ}{4}\right) \right]$$
*   Magnitude: $R = 4^{\frac{1}{4}} = (2^2)^{\frac{1}{4}} = 2^{\frac{2}{4}} = 2^{\frac{1}{2}} = \sqrt{2} \approx 1.414$.
*   Angles: $\alpha_k = 52.5^\circ + k \cdot 90^\circ$ for $k = 0, 1, 2, 3$.

**Step 3: Calculate the specific roots.**
*   **$k = 0$:** $\alpha_0 = 52.5^\circ \implies z_0 = \sqrt{2}(\cos 52.5^\circ + i\sin 52.5^\circ)$
*   **$k = 1$:** $\alpha_1 = 52.5^\circ + 90^\circ = 142.5^\circ \implies z_1 = \sqrt{2}(\cos 142.5^\circ + i\sin 142.5^\circ)$
*   **$k = 2$:** $\alpha_2 = 142.5^\circ + 90^\circ = 232.5^\circ \implies z_2 = \sqrt{2}(\cos 232.5^\circ + i\sin 232.5^\circ)$
*   **$k = 3$:** $\alpha_3 = 232.5^\circ + 90^\circ = 322.5^\circ \implies z_3 = \sqrt{2}(\cos 322.5^\circ + i\sin 322.5^\circ)$

**Part b) Locate the roots graphically.**
1.  Draw a circle centered at the origin $(0,0)$ with a radius of $R = \sqrt{2}$.
2.  The four roots lie on the circumference of this circle.
3.  Because they are separated by exactly $90^\circ$, they form the vertices of a **square** inscribed inside the circle.
4.  There is exactly one root in each of the four quadrants: $z_0$ in QI, $z_1$ in QII, $z_2$ in QIII, and $z_3$ in QIV.
Here are the detailed solutions for the next four questions (Q57 to Q60).

### Q57. Prblm-3.3: find the roots of followings: $(i) z^2+\pi^2=0$, $(ii) z^6+1=0$, $(iii) z^4+a^4=0$, $(iv) z^4+8i=0$

**Solution:**

This problem requires finding the complex roots for four different polynomial equations using De Moivre's Theorem.

**Part (i): $z^2 + \pi^2 = 0$**
1.  Isolate $z^2$: 
    $$z^2 = -\pi^2$$
2.  Take the square root of both sides. Since taking the square root of a negative real number introduces the imaginary unit $i = \sqrt{-1}$:
    $$z = \pm\sqrt{-\pi^2} = \pm\sqrt{-1 \cdot \pi^2} = \pm i\pi$$
*Roots:* **$z_1 = i\pi$, $z_2 = -i\pi$**

---

**Part (ii): $z^6 + 1 = 0$**
1.  Isolate $z$: 
    $$z^6 = -1 \implies z = (-1)^{\frac{1}{6}}$$
2.  Express $-1$ in general polar form:
    Modulus $r = 1$, Argument $\theta = \pi$.
    $$-1 = 1 \cdot (\cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi))$$
3.  Apply De Moivre's Theorem for roots ($k = 0, 1, 2, 3, 4, 5$):
    $$z_k = \cos\left(\frac{\pi + 2k\pi}{6}\right) + i\sin\left(\frac{\pi + 2k\pi}{6}\right)$$
4.  Calculate the 6 roots:
    *   $k=0$: $z_0 = \cos(\frac{\pi}{6}) + i\sin(\frac{\pi}{6}) = \frac{\sqrt{3}}{2} + i\frac{1}{2}$
    *   $k=1$: $z_1 = \cos(\frac{3\pi}{6}) + i\sin(\frac{3\pi}{6}) = \cos(\frac{\pi}{2}) + i\sin(\frac{\pi}{2}) = i$
    *   $k=2$: $z_2 = \cos(\frac{5\pi}{6}) + i\sin(\frac{5\pi}{6}) = -\frac{\sqrt{3}}{2} + i\frac{1}{2}$
    *   $k=3$: $z_3 = \cos(\frac{7\pi}{6}) + i\sin(\frac{7\pi}{6}) = -\frac{\sqrt{3}}{2} - i\frac{1}{2}$
    *   $k=4$: $z_4 = \cos(\frac{9\pi}{6}) + i\sin(\frac{9\pi}{6}) = \cos(\frac{3\pi}{2}) + i\sin(\frac{3\pi}{2}) = -i$
    *   $k=5$: $z_5 = \cos(\frac{11\pi}{6}) + i\sin(\frac{11\pi}{6}) = \frac{\sqrt{3}}{2} - i\frac{1}{2}$

---

**Part (iii): $z^4 + a^4 = 0$** (assuming $a > 0$)
1.  Isolate $z$:
    $$z^4 = -a^4 \implies z = (-a^4)^{\frac{1}{4}}$$
2.  Express $-a^4$ in general polar form:
    Modulus $r = a^4$, Argument $\theta = \pi$.
    $$-a^4 = a^4(\cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi))$$
3.  Apply De Moivre's theorem ($k = 0, 1, 2, 3$):
    $$z_k = (a^4)^{\frac{1}{4}} \left[ \cos\left(\frac{\pi + 2k\pi}{4}\right) + i\sin\left(\frac{\pi + 2k\pi}{4}\right) \right]$$
    $$z_k = a \left[ \cos\left(\frac{(2k+1)\pi}{4}\right) + i\sin\left(\frac{(2k+1)\pi}{4}\right) \right]$$
4.  Calculate the 4 roots:
    *   $k=0$: $z_0 = a(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}) = a(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}})$
    *   $k=1$: $z_1 = a(\cos\frac{3\pi}{4} + i\sin\frac{3\pi}{4}) = a(-\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}})$
    *   $k=2$: $z_2 = a(\cos\frac{5\pi}{4} + i\sin\frac{5\pi}{4}) = a(-\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}})$
    *   $k=3$: $z_3 = a(\cos\frac{7\pi}{4} + i\sin\frac{7\pi}{4}) = a(\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}})$

---

**Part (iv): $z^4 + 8i = 0$**
1.  Isolate $z$:
    $$z^4 = -8i \implies z = (-8i)^{\frac{1}{4}}$$
2.  Express $-8i$ in general polar form:
    Modulus $r = 8$. Argument $\theta = \frac{3\pi}{2}$ (or $270^\circ$).
    $$-8i = 8\left(\cos\left(\frac{3\pi}{2} + 2k\pi\right) + i\sin\left(\frac{3\pi}{2} + 2k\pi\right)\right)$$
3.  Apply De Moivre's theorem ($k = 0, 1, 2, 3$):
    $$z_k = 8^{\frac{1}{4}} \left[ \cos\left(\frac{\frac{3\pi}{2} + 2k\pi}{4}\right) + i\sin\left(\frac{\frac{3\pi}{2} + 2k\pi}{4}\right) \right]$$
    Note that $8^{1/4} = (2^3)^{1/4} = 2^{3/4}$.
    Angles $\alpha_k = \frac{3\pi + 4k\pi}{8}$.
4.  Calculate the 4 roots:
    *   $k=0$: $z_0 = 2^{3/4} (\cos\frac{3\pi}{8} + i\sin\frac{3\pi}{8})$
    *   $k=1$: $z_1 = 2^{3/4} (\cos\frac{7\pi}{8} + i\sin\frac{7\pi}{8})$
    *   $k=2$: $z_2 = 2^{3/4} (\cos\frac{11\pi}{8} + i\sin\frac{11\pi}{8})$
    *   $k=3$: $z_3 = 2^{3/4} (\cos\frac{15\pi}{8} + i\sin\frac{15\pi}{8})$

***

### Q58. Problem: a) find the eqn for a circle of radius $4$ with center at $(-2,1)$ b) an ellipse with major axis of length $10$ foci at $(-3,0)$ & $(3,0)$

**Solution:**

This problem asks us to translate classical geometric descriptions into complex plane equations.

**Part a) Equation for a Circle**
1.  **Recall the definition:** A circle is the set of all points $z$ that are a fixed distance (radius $r$) from a center point ($z_0$). In the complex plane, distance is represented by the modulus of the difference: $|z - z_0| = r$.
2.  **Identify parameters:** 
    *   Radius $r = 4$.
    *   Center at Cartesian coordinates $(-2, 1)$, which corresponds to the complex number $z_0 = -2 + i$.
3.  **Formulate the equation:**
    $$|z - (-2 + i)| = 4$$
    $$|z + 2 - i| = 4$$

**Part b) Equation for an Ellipse**
1.  **Recall the definition:** An ellipse is the locus of all points $z$ such that the *sum* of their distances from two fixed points (the foci) is a constant (the length of the major axis, usually denoted as $2a$).
2.  **Identify parameters:**
    *   Length of major axis (the constant sum of distances): $2a = 10$.
    *   Focus 1 at Cartesian coordinates $(-3, 0)$, which corresponds to complex number $z_1 = -3$.
    *   Focus 2 at Cartesian coordinates $(3, 0)$, which corresponds to complex number $z_2 = 3$.
3.  **Formulate the equation:**
    The distance from $z$ to Focus 1 is $|z - z_1| = |z - (-3)| = |z + 3|$.
    The distance from $z$ to Focus 2 is $|z - z_2| = |z - 3|$.
    The sum of these distances equals $10$:
    $$|z + 3| + |z - 3| = 10$$

***

### Q59. Ques: Given a complex number $z$, interpret geometrically $ze^{i\alpha}$ where $\alpha$ is real.

*(Note: This is conceptually identical to Q7, but answered here again for sequential completeness).*

**Solution:**

To find the geometric interpretation, we express the complex number in polar coordinates.

**Step 1: Write $z$ in polar form.**
Let $z = r e^{i\theta}$, where:
*   $r = |z|$ is the modulus (length of the vector).
*   $\theta = \arg(z)$ is the argument (angle with the positive real axis).

**Step 2: Multiply by $e^{i\alpha}$.**
$$z \cdot e^{i\alpha} = (r e^{i\theta}) \cdot e^{i\alpha}$$
Using the laws of exponents ($e^x \cdot e^y = e^{x+y}$):
$$z e^{i\alpha} = r e^{i(\theta + \alpha)}$$

**Step 3: Geometrically interpret the result.**
Let $w = z e^{i\alpha} = R e^{i\Theta}$.
Comparing this to our result:
1.  **New Modulus ($R$):** $R = r$. The magnitude (length) of the new complex vector is identical to the original vector $z$. It has not been stretched or shrunk.
2.  **New Argument ($\Theta$):** $\Theta = \theta + \alpha$. The new angle is the old angle $\theta$ shifted by exactly $\alpha$ radians.

**Conclusion:**
Geometrically, multiplying a complex number $z$ by $e^{i\alpha}$ represents a pure **rotation** of the vector $z$ about the origin $(0,0)$ by an angle $\alpha$. 
*   If $\alpha > 0$, the rotation is counterclockwise.
*   If $\alpha < 0$, the rotation is clockwise.

***

### Q60. Prblm-41: If $z_1=3-4i$ & $z_2=-4+3i$ Find. $(i) z_1\cdot z_2$, $(ii) z_1\times z_2$

**Solution:**

In the context of 2D complex vectors (as taught in standard Engineering Mathematics texts like Feruj Sheet), the symbols "$\cdot$" and "$\times$" between complex numbers do *not* represent standard scalar algebraic multiplication. Instead, they represent the 2D **Dot Product** and the scalar magnitude of the **Cross Product**, respectively.

Let two complex numbers represent 2D vectors: 
$\vec{v_1} = (x_1, y_1)$ corresponding to $z_1 = x_1 + iy_1$
$\vec{v_2} = (x_2, y_2)$ corresponding to $z_2 = x_2 + iy_2$

The formulas for these operations in terms of complex components are:
*   **Dot Product:** $z_1 \cdot z_2 = x_1 x_2 + y_1 y_2$
    *(Note: This is also equal to the real part of $\overline{z_1}z_2$, i.e., $Re(\overline{z_1}z_2)$)*
*   **Cross Product (Scalar magnitude):** $z_1 \times z_2 = x_1 y_2 - x_2 y_1$
    *(Note: This is also equal to the imaginary part of $\overline{z_1}z_2$, i.e., $Im(\overline{z_1}z_2)$)*

**Given:**
$z_1 = 3 - 4i \implies x_1 = 3$, $y_1 = -4$
$z_2 = -4 + 3i \implies x_2 = -4$, $y_2 = 3$

**Part (i): Find $z_1 \cdot z_2$ (Dot Product)**
$$z_1 \cdot z_2 = x_1 x_2 + y_1 y_2$$
$$z_1 \cdot z_2 = (3)(-4) + (-4)(3)$$
$$z_1 \cdot z_2 = -12 - 12$$
$$z_1 \cdot z_2 = -24$$

**Part (ii): Find $z_1 \times z_2$ (Cross Product)**
$$z_1 \times z_2 = x_1 y_2 - x_2 y_1$$
$$z_1 \times z_2 = (3)(3) - (-4)(-4)$$
$$z_1 \times z_2 = 9 - 16$$
$$z_1 \times z_2 = -7$$

*(Self-Check using $\overline{z_1}z_2$:
$\overline{z_1}z_2 = (3+4i)(-4+3i) = -12 + 9i - 16i + 12i^2 = -12 - 7i - 12 = -24 - 7i$. 
The real part is $-24$ (dot product) and the imaginary part is $-7$ (cross product). This confirms the calculations are correct).*

**Answer:**
*   **(i) $z_1 \cdot z_2 = -24$**
*   **(ii) $z_1 \times z_2 = -7$**


Here are the detailed solutions for the next four questions (Q61 to Q64).

### Q61. Ques: Prove that, the area of a parallelogram having sides $z_1$ & $z_2$ is $\vert{}z_1\times z_2\vert{}$

**Solution:**

In the complex plane, the complex numbers $z_1$ and $z_2$ can be treated as 2D position vectors originating from the origin $(0,0)$. 
The "cross product" $z_1 \times z_2$ in 2D complex vector notation (as defined in standard engineering mathematics texts) is a scalar quantity representing the imaginary part of $\overline{z_1}z_2$. Let's prove that the absolute value of this scalar yields the area of the parallelogram formed by these two vectors.

**Method 1: Using Polar Coordinates (Trigonometric approach)**

**Step 1: Express the complex numbers in polar form.**
Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$.
*   $r_1 = |z_1|$ is the length of the first side of the parallelogram.
*   $r_2 = |z_2|$ is the length of the second side.
*   The angle between the two vectors is $\theta = |\theta_2 - \theta_1|$.

**Step 2: Recall the geometric formula for the area of a parallelogram.**
From standard geometry, the area of a parallelogram formed by two vectors is given by the product of their magnitudes and the sine of the angle between them:
$$\text{Area} = (\text{length of side 1}) \times (\text{length of side 2}) \times \sin(\text{angle between them})$$
$$\text{Area} = r_1 r_2 |\sin(\theta_2 - \theta_1)| \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the 2D complex cross product $z_1 \times z_2$.**
By definition in this context, the 2D cross product is $Im(\overline{z_1}z_2)$. 
Let's calculate $\overline{z_1}z_2$:
$$\overline{z_1}z_2 = (r_1 e^{-i\theta_1}) (r_2 e^{i\theta_2})$$
$$\overline{z_1}z_2 = r_1 r_2 e^{i(\theta_2 - \theta_1)}$$

Using Euler's formula to expand this:
$$\overline{z_1}z_2 = r_1 r_2 [\cos(\theta_2 - \theta_1) + i\sin(\theta_2 - \theta_1)]$$

The imaginary part (which is $z_1 \times z_2$) is:
$$z_1 \times z_2 = Im(\overline{z_1}z_2) = r_1 r_2 \sin(\theta_2 - \theta_1)$$

**Step 4: Relate the area to the cross product.**
Taking the absolute value of the cross product:
$$|z_1 \times z_2| = |r_1 r_2 \sin(\theta_2 - \theta_1)| = r_1 r_2 |\sin(\theta_2 - \theta_1)|$$

Comparing this with Equation 1, we see they are exactly the same.
$$\text{Area} = |z_1 \times z_2|$$
**(Proved)**

---

**Method 2: Using Cartesian Coordinates**

**Step 1: Define the vectors.**
Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$.

**Step 2: Area of a parallelogram in 2D.**
From linear algebra and coordinate geometry, the area of a parallelogram formed by vectors $(x_1, y_1)$ and $(x_2, y_2)$ is the absolute value of the determinant of their coordinates:
$$\text{Area} = \left| \det \begin{pmatrix} x_1 & y_1 \\ x_2 & y_2 \end{pmatrix} \right| = |x_1 y_2 - x_2 y_1|$$

**Step 3: Evaluate $z_1 \times z_2$.**
By the definition of the 2D complex cross product:
$$z_1 \times z_2 = x_1 y_2 - x_2 y_1$$
Taking the absolute value:
$$|z_1 \times z_2| = |x_1 y_2 - x_2 y_1|$$

This matches the determinant area formula exactly. 
**(Proved)**

***

### Q62. Problem: a) $\vert{}\frac{z-3}{z+3}\vert{}=2$

*(Note: This asks to represent graphically the set of values of $z$. This is numerically identical to Q4, but is solved here again with complete algebraic steps for clarity).*

**Solution:**

We need to find the geometric locus of all points $z = x + iy$ that satisfy this equation.

**Step 1: Apply modulus properties and substitute $z$.**
Using the division property of the modulus $\left|\frac{A}{B}\right| = \frac{|A|}{|B|}$:
$$\frac{|z - 3|}{|z + 3|} = 2$$
$$|z - 3| = 2|z + 3|$$

Substitute $z = x + iy$:
$$|(x - 3) + iy| = 2|(x + 3) + iy|$$

**Step 2: Apply the definition of the modulus.**
The modulus of $a + ib$ is $\sqrt{a^2 + b^2}$.
$$\sqrt{(x - 3)^2 + y^2} = 2\sqrt{(x + 3)^2 + y^2}$$

Square both sides to eliminate the square roots:
$$(x - 3)^2 + y^2 = 4 \left[ (x + 3)^2 + y^2 \right]$$

**Step 3: Expand the binomials.**
$$(x^2 - 6x + 9) + y^2 = 4(x^2 + 6x + 9 + y^2)$$
$$x^2 - 6x + 9 + y^2 = 4x^2 + 24x + 36 + 4y^2$$

**Step 4: Collect all terms on one side to form a polynomial equation.**
Subtract the left side's terms from the right side:
$$0 = 4x^2 - x^2 + 4y^2 - y^2 + 24x - (-6x) + 36 - 9$$
$$0 = 3x^2 + 3y^2 + 30x + 27$$

Divide the entire equation by $3$ to simplify:
$$x^2 + y^2 + 10x + 9 = 0$$

**Step 5: Complete the square to identify the shape.**
Group the $x$ terms together:
$$(x^2 + 10x) + y^2 = -9$$
To complete the square for $x$, add $(10/2)^2 = 25$ to both sides:
$$(x^2 + 10x + 25) + y^2 = -9 + 25$$
$$(x + 5)^2 + y^2 = 16$$
$$(x + 5)^2 + (y - 0)^2 = 4^2$$

**Conclusion:**
This is the standard Cartesian equation of a circle, $(x-h)^2 + (y-k)^2 = r^2$.
*   **Shape:** Circle
*   **Center:** $(h, k) = (-5, 0)$, which corresponds to the complex number $z = -5$.
*   **Radius:** $r = \sqrt{16} = 4$.

**Answer:** The equation represents a **circle** in the complex plane with its center at **$(-5, 0)$** and a radius of **$4$**.

***

### Q63. Problem: a) $\vert{}\frac{z-3}{z+3}\vert{}<2$

**Solution:**

This problem is an inequality based on the exact same algebraic expression as Q62. We need to determine which region of the complex plane satisfies this inequality.

**Step 1: Set up the inequality algebraically.**
Following the exact same steps as Q62, but keeping the "<" sign intact:
$$\frac{|z - 3|}{|z + 3|} < 2$$
$$|z - 3| < 2|z + 3|$$
Substitute $z = x + iy$:
$$\sqrt{(x - 3)^2 + y^2} < 2\sqrt{(x + 3)^2 + y^2}$$

Square both sides (since both sides are positive, the inequality direction does not change):
$$(x - 3)^2 + y^2 < 4 \left[ (x + 3)^2 + y^2 \right]$$

**Step 2: Expand and simplify.**
$$x^2 - 6x + 9 + y^2 < 4x^2 + 24x + 36 + 4y^2$$

Subtract the left side's terms from the right side:
$$0 < 3x^2 + 3y^2 + 30x + 27$$

Divide by 3:
$$0 < x^2 + y^2 + 10x + 9$$

**Step 3: Complete the square.**
$$x^2 + 10x + y^2 > -9$$
$$x^2 + 10x + 25 + y^2 > -9 + 25$$
$$(x + 5)^2 + y^2 > 16$$
$$(x + 5)^2 + (y - 0)^2 > 4^2$$

**Conclusion:**
The corresponding equality $(x + 5)^2 + y^2 = 16$ defines a boundary circle with center $(-5, 0)$ and radius $4$. 
The inequality "$>$" indicates that the distance from any point $(x,y)$ to the center $(-5,0)$ is *strictly greater* than the radius $4$.

**Answer:** 
The inequality represents the open region **strictly outside the circle** whose center is at **$z = -5$** and whose radius is **$4$**. (The boundary circle itself is not included).

***

### Q64. Problem 1.1: Prove that $z_{1}+z_{2}=\overline{z_{1}}+\overline{z_{2}}$

*(Correction Note: The statement provided in the source text "$z_1+z_2 = \overline{z_1}+\overline{z_2}$" is a well-known typographical error in the lecture sheets. A complex number is generally not equal to its conjugate. The standard, mathematically correct theorem that needs to be proven is that the conjugate of a sum is equal to the sum of the conjugates: $\overline{z_1+z_2} = \overline{z_1} + \overline{z_2}$. This is identical to Q38. We will prove the corrected identity).*

**Solution:**

We will prove the corrected identity $\overline{z_1+z_2} = \overline{z_1} + \overline{z_2}$ using the Cartesian representation of complex numbers.

**Step 1: Define the complex numbers.**
Let $z_1$ and $z_2$ be two complex numbers such that:
$$z_1 = x_1 + iy_1$$
$$z_2 = x_2 + iy_2$$
where $x_1, y_1, x_2, y_2$ are real numbers.

**Step 2: Evaluate the Left-Hand Side (LHS).**
First, calculate the sum $z_1 + z_2$:
$$z_1 + z_2 = (x_1 + iy_1) + (x_2 + iy_2)$$
Combine the real parts and the imaginary parts:
$$z_1 + z_2 = (x_1 + x_2) + i(y_1 + y_2)$$

Now, take the complex conjugate of this entire sum. The conjugate is found by changing the sign in front of the imaginary part:
$$\overline{z_1 + z_2} = (x_1 + x_2) - i(y_1 + y_2) \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the Right-Hand Side (RHS).**
First, find the individual complex conjugates of $z_1$ and $z_2$:
$$\overline{z_1} = x_1 - iy_1$$
$$\overline{z_2} = x_2 - iy_2$$

Now, add these two conjugates together:
$$\overline{z_1} + \overline{z_2} = (x_1 - iy_1) + (x_2 - iy_2)$$
Combine the real parts and the imaginary parts:
$$\overline{z_1} + \overline{z_2} = (x_1 + x_2) + i(-y_1 - y_2)$$
Factor out the negative sign from the imaginary part:
$$\overline{z_1} + \overline{z_2} = (x_1 + x_2) - i(y_1 + y_2) \quad \text{--- (Equation 2)}$$

**Step 4: Conclusion.**
By comparing the results of Equation 1 and Equation 2, we can see that they are identical.
$$\text{LHS} = \text{RHS}$$
$$\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$$
**(Proved)**


Here are the detailed solutions for the next four questions (Q65 to Q68). 

*(Note: These questions from the "Feruj Sheet" source are conceptually identical to earlier questions Q39-Q46 from the "Firoz Note" source. They cover the fundamental properties of complex numbers. Detailed proofs are provided again below for completeness).*

### Q65. Prob. 1.2: Prove that (i) $z_{1}-z_{2}=\overline{z}_{1}-\overline{z}_{2}$ (ii) $\overline{z_{1}z_{2}}=\overline{z}_{1}\overline{z}_{2}$ (iii) $z\overline{z}=\vert{}z\vert{}^{2}$ (iv) $\overline{z_{1}}z_{2}=\overline{z_{1}\overline{z_{2}}}$ (v) $z_{1}\overline{z}_{2}+\overline{z_{1}\overline{z_{2}}}=2~Re(z_{1}\overline{z}_{2})$

**Solution:**

Let $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$, where $x_1, y_1, x_2, y_2$ are real numbers.

**Part (i): Prove $\overline{z_1 - z_2} = \overline{z}_1 - \overline{z}_2$**
*(Correction Note: The source text has a typo missing the overline on the LHS. A complex difference is not equal to the difference of its conjugates. We will prove the mathematically correct standard identity).*
1.  **LHS:** First, find the difference $z_1 - z_2$:
    $$z_1 - z_2 = (x_1 + iy_1) - (x_2 + iy_2) = (x_1 - x_2) + i(y_1 - y_2)$$
    Take the conjugate by flipping the sign of the imaginary part:
    $$\overline{z_1 - z_2} = (x_1 - x_2) - i(y_1 - y_2)$$
2.  **RHS:** Find the individual conjugates and subtract them:
    $$\overline{z_1} = x_1 - iy_1$$
    $$\overline{z_2} = x_2 - iy_2$$
    $$\overline{z_1} - \overline{z_2} = (x_1 - iy_1) - (x_2 - iy_2) = x_1 - x_2 - iy_1 + iy_2 = (x_1 - x_2) - i(y_1 - y_2)$$
3.  **Conclusion:** LHS = RHS. **(Proved)**

**Part (ii): Prove $\overline{z_1 z_2} = \overline{z}_1 \overline{z}_2$**
1.  **LHS:** Multiply $z_1$ and $z_2$:
    $$z_1 z_2 = (x_1 + iy_1)(x_2 + iy_2) = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + x_2 y_1)$$
    Take the conjugate:
    $$\overline{z_1 z_2} = (x_1 x_2 - y_1 y_2) - i(x_1 y_2 + x_2 y_1)$$
2.  **RHS:** Multiply the conjugates:
    $$\overline{z}_1 \overline{z}_2 = (x_1 - iy_1)(x_2 - iy_2) = x_1 x_2 - i x_1 y_2 - i y_1 x_2 + i^2 y_1 y_2$$
    Since $i^2 = -1$:
    $$\overline{z}_1 \overline{z}_2 = (x_1 x_2 - y_1 y_2) - i(x_1 y_2 + x_2 y_1)$$
3.  **Conclusion:** LHS = RHS. **(Proved)**

**Part (iii): Prove $z\overline{z} = |z|^2$**
1.  Let $z = x + iy$. Its conjugate is $\overline{z} = x - iy$.
2.  Multiply them (difference of squares):
    $$z\overline{z} = (x + iy)(x - iy) = x^2 - (iy)^2 = x^2 - i^2y^2$$
    Since $i^2 = -1$, $z\overline{z} = x^2 + y^2$.
3.  By definition, the modulus is $|z| = \sqrt{x^2 + y^2}$. Squaring both sides yields $|z|^2 = x^2 + y^2$.
4.  Therefore, $z\overline{z} = |z|^2$. **(Proved)**

**Part (iv): Prove $\overline{z_1}z_2 = \overline{z_1\overline{z_2}}$**
1.  Start with the RHS and apply the product rule for conjugates proved in Part (ii) ($\overline{AB} = \overline{A}\overline{B}$):
    $$\overline{z_1 \overline{z_2}} = \overline{z_1} \cdot \overline{(\overline{z_2})}$$
2.  The conjugate of a conjugate returns the original number: $\overline{(\overline{z_2})} = z_2$.
    $$\overline{z_1 \overline{z_2}} = \overline{z_1} z_2$$
3.  This matches the LHS. **(Proved)**

**Part (v): Prove $z_1\overline{z}_2 + \overline{z_1\overline{z_2}} = 2 Re(z_1\overline{z}_2)$**
1.  Let $w$ be the complex number $z_1\overline{z}_2$.
2.  From Part (iv), we know that the second term on the LHS is simply the conjugate of the first term: $\overline{z_1\overline{z_2}} = \overline{w}$.
3.  So the LHS becomes $w + \overline{w}$.
4.  Let $w = u + iv$ (where $u = Re(w)$ and $v = Im(w)$). Then $\overline{w} = u - iv$.
5.  Add them: $w + \overline{w} = (u + iv) + (u - iv) = 2u$.
6.  Since $u = Re(w)$, we have $w + \overline{w} = 2 Re(w)$. Substituting $w$ back gives $z_1\overline{z}_2 + \overline{z_1\overline{z_2}} = 2 Re(z_1\overline{z}_2)$. **(Proved)**

***

### Q66. Problem 1.3: Prove that (i) $\vert{}z_{1}+z_{2}\vert{}\le\vert{}z_{1}\vert{}+\vert{}z_{2}\vert{}$ (ii) $\vert{}z_{1}+z_{2}+z_{3}\vert{}\le\vert{}z_{1}\vert{}+\vert{}z_{2}\vert{}+\vert{}z_{3}\vert{}$

**Solution:**

**Part (i): Prove $|z_1 + z_2| \le |z_1| + |z_2|$ (The Triangle Inequality)**
1.  Square the left side and use the property $|z|^2 = z\overline{z}$:
    $$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = (z_1 + z_2)(\overline{z_1} + \overline{z_2})$$
2.  Expand the expression:
    $$|z_1 + z_2|^2 = z_1\overline{z_1} + z_1\overline{z_2} + z_2\overline{z_1} + z_2\overline{z_2}$$
3.  Use $|z|^2 = z\overline{z}$ on the first and last terms, and recognize that $z_2\overline{z_1}$ is the conjugate of $z_1\overline{z_2}$:
    $$|z_1 + z_2|^2 = |z_1|^2 + (z_1\overline{z_2} + \overline{z_1\overline{z_2}}) + |z_2|^2$$
4.  Using the property from Q65(v), $w + \overline{w} = 2Re(w)$:
    $$|z_1 + z_2|^2 = |z_1|^2 + 2Re(z_1\overline{z_2}) + |z_2|^2$$
5.  The real part of any complex number is always less than or equal to its absolute value (modulus), $Re(w) \le |w|$:
    $$2Re(z_1\overline{z_2}) \le 2|z_1\overline{z_2}| = 2|z_1||\overline{z_2}| = 2|z_1||z_2|$$
6.  Substitute this inequality back:
    $$|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2$$
7.  The right side is a perfect binomial square:
    $$|z_1 + z_2|^2 \le (|z_1| + |z_2|)^2$$
8.  Taking the square root of both sides (since moduli are non-negative):
    $$|z_1 + z_2| \le |z_1| + |z_2|$$
    **(Proved)**

**Part (ii): Prove $|z_1 + z_2 + z_3| \le |z_1| + |z_2| + |z_3|$**
1.  Treat $(z_1 + z_2)$ as a single grouping:
    $$|z_1 + z_2 + z_3| = |(z_1 + z_2) + z_3|$$
2.  Apply the Triangle Inequality proven in Part (i) to the two terms $(z_1 + z_2)$ and $z_3$:
    $$|(z_1 + z_2) + z_3| \le |z_1 + z_2| + |z_3|$$
3.  Apply the Triangle Inequality again to $|z_1 + z_2|$:
    Since $|z_1 + z_2| \le |z_1| + |z_2|$, substitute this in:
    $$|z_1 + z_2| + |z_3| \le (|z_1| + |z_2|) + |z_3|$$
4.  Therefore:
    $$|z_1 + z_2 + z_3| \le |z_1| + |z_2| + |z_3|$$
    **(Proved)**

***

### Q67. Prob. 1.4: Prove that (i) $\vert{}z_{1}z_{2}\vert{}=\vert{}z_{1}\vert{}\vert{}z_{2}\vert{}$ (ii) $\vert{}z_{1}-z_{2}\vert{}\ge\vert{}z_{1}\vert{}-\vert{}z_{2}\vert{}$ (iii) $\vert{}\overline{z}\vert{}=\vert{}z\vert{}$

**Solution:**

**Part (i): Prove $|z_1 z_2| = |z_1| |z_2|$**
1.  Square the Left-Hand Side and use the property $|w|^2 = w\overline{w}$:
    $$|z_1 z_2|^2 = (z_1 z_2)\overline{(z_1 z_2)}$$
2.  Apply the conjugate property for products ($\overline{AB} = \overline{A}\overline{B}$):
    $$|z_1 z_2|^2 = (z_1 z_2)(\overline{z_1} \cdot \overline{z_2})$$
3.  Rearrange the terms (complex multiplication is commutative):
    $$|z_1 z_2|^2 = (z_1\overline{z_1}) \cdot (z_2\overline{z_2})$$
4.  Convert back to moduli ($z\overline{z} = |z|^2$):
    $$|z_1 z_2|^2 = |z_1|^2 \cdot |z_2|^2$$
5.  Take the square root of both sides (all quantities are non-negative):
    $$|z_1 z_2| = |z_1| |z_2|$$
    **(Proved)**

**Part (ii): Prove $|z_1 - z_2| \ge |z_1| - |z_2|$**
1.  We use a clever algebraic manipulation relying on the Triangle Inequality ($|A + B| \le |A| + |B|$).
2.  Express $z_1$ as the sum of $(z_1 - z_2)$ and $z_2$:
    $$z_1 = (z_1 - z_2) + z_2$$
3.  Take the modulus of both sides:
    $$|z_1| = |(z_1 - z_2) + z_2|$$
4.  Apply the Triangle Inequality to the right side:
    $$|(z_1 - z_2) + z_2| \le |z_1 - z_2| + |z_2|$$
    So, $|z_1| \le |z_1 - z_2| + |z_2|$
5.  Subtract $|z_2|$ from both sides to isolate the difference term:
    $$|z_1| - |z_2| \le |z_1 - z_2|$$
6.  Flip the inequality around to match the required form:
    $$|z_1 - z_2| \ge |z_1| - |z_2|$$
    **(Proved)**

**Part (iii): Prove $|\overline{z}| = |z|$**
1.  Let $z$ be defined in Cartesian coordinates as $z = x + iy$.
2.  By definition, its modulus is $|z| = \sqrt{x^2 + y^2}$.
3.  Its complex conjugate is defined as $\overline{z} = x - iy$.
4.  Calculate the modulus of the conjugate:
    $$|\overline{z}| = \sqrt{x^2 + (-y)^2}$$
5.  Since the square of a negative number is positive, $(-y)^2 = y^2$:
    $$|\overline{z}| = \sqrt{x^2 + y^2}$$
6.  Therefore, comparing the expressions, $|\overline{z}| = |z|$.
    **(Proved)**

***

### Q68. Prob. 1.5: Find the value of $(i)\vert{}e^{z}\vert{}$ $(ii)\vert{}e^{iz}\vert{}$

**Solution:**

Let the complex variable $z$ be written in standard Cartesian form: $z = x + iy$ (where $x$ and $y$ are real numbers).

**Part (i): Evaluate $|e^z|$**
1.  Substitute $z = x + iy$ into the expression:
    $$e^z = e^{x + iy}$$
2.  Use the exponent addition rule ($e^{a+b} = e^a \cdot e^b$):
    $$e^z = e^x \cdot e^{iy}$$
3.  Take the modulus of the product. The modulus of a product is the product of the moduli:
    $$|e^z| = |e^x \cdot e^{iy}| = |e^x| \cdot |e^{iy}|$$
4.  Evaluate the individual moduli:
    *   Since $x$ is a real number, $e^x$ is a strictly positive real number. Thus, its modulus is itself: $|e^x| = e^x$.
    *   Using Euler's formula, $e^{iy} = \cos y + i\sin y$. The modulus is $\sqrt{\cos^2 y + \sin^2 y} = \sqrt{1} = 1$. So, $|e^{iy}| = 1$.
5.  Multiply them together:
    $$|e^z| = e^x \cdot 1 = e^x$$
**Answer (i): $|e^z| = e^x$** (where $x$ is the real part of $z$).

**Part (ii): Evaluate $|e^{iz}|$**
1.  First, evaluate the exponent $iz$ by substituting $z = x + iy$:
    $$iz = i(x + iy) = ix + i^2y$$
    Since $i^2 = -1$:
    $$iz = ix - y = -y + ix$$
2.  Substitute this back into the exponential expression:
    $$e^{iz} = e^{-y + ix}$$
3.  Use the exponent rule to separate the real and imaginary exponents:
    $$e^{iz} = e^{-y} \cdot e^{ix}$$
4.  Take the modulus of the product:
    $$|e^{iz}| = |e^{-y} \cdot e^{ix}| = |e^{-y}| \cdot |e^{ix}|$$
5.  Evaluate the individual moduli:
    *   Since $y$ is real, $-y$ is real, making $e^{-y}$ a positive real number. Its modulus is itself: $|e^{-y}| = e^{-y}$.
    *   Since $x$ is real, $e^{ix} = \cos x + i\sin x$. Its modulus is $\sqrt{\cos^2 x + \sin^2 x} = 1$. So, $|e^{ix}| = 1$.
6.  Multiply them together:
    $$|e^{iz}| = e^{-y} \cdot 1 = e^{-y}$$
**Answer (ii): $|e^{iz}| = e^{-y}$** (where $y$ is the imaginary part of $z$).

Here are the detailed solutions for the next four questions (Q69 to Q72).

### Q69. Example 1.3.3. (Polar form): Find the modulus, argument, and polar form of the complex numbers: 
(a) $z_{1}=5$ 
(b) $z_{2}=-3i$ 
(c) $z_{3}=\sqrt{3}+i$ 
(d) $z_{4}=1+i$ 
(e) $z_{5}=1-i$ 
(f) $z_{6}=-1-i$

**Solution:**

To find these values, we use the relations for a complex number $z = x + iy$:
*   **Modulus:** $r = |z| = \sqrt{x^2 + y^2}$
*   **Argument:** $\theta = \tan^{-1}(y/x)$, adjusted for the correct quadrant.
*   **Polar form:** $z = r(\cos\theta + i\sin\theta)$ or in exponential form $z = re^{i\theta}$.

**(a) $z_1 = 5$** (or $5 + 0i$)
*   **Modulus:** $r = \sqrt{5^2 + 0^2} = 5$
*   **Argument:** The point lies on the positive real axis, so the angle is $0$. $\theta = 0$.
*   **Polar Form:** $5(\cos 0 + i\sin 0)$ or $5e^{i0}$.

**(b) $z_2 = -3i$** (or $0 - 3i$)
*   **Modulus:** $r = \sqrt{0^2 + (-3)^2} = \sqrt{9} = 3$
*   **Argument:** The point lies on the negative imaginary axis, which corresponds to $-90^\circ$ or $-\pi/2$ radians. $\theta = -\frac{\pi}{2}$.
*   **Polar Form:** $3\left(\cos\left(-\frac{\pi}{2}\right) + i\sin\left(-\frac{\pi}{2}\right)\right)$ or $3e^{-i\pi/2}$.

**(c) $z_3 = \sqrt{3} + i$**
*   **Modulus:** $r = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = \sqrt{4} = 2$
*   **Argument:** Both $x$ and $y$ are positive (Quadrant I). $\theta = \tan^{-1}(1/\sqrt{3}) = \frac{\pi}{6}$ (or $30^\circ$).
*   **Polar Form:** $2\left(\cos\frac{\pi}{6} + i\sin\frac{\pi}{6}\right)$ or $2e^{i\pi/6}$.

**(d) $z_4 = 1 + i$**
*   **Modulus:** $r = \sqrt{1^2 + 1^2} = \sqrt{2}$
*   **Argument:** Quadrant I. $\theta = \tan^{-1}(1/1) = \tan^{-1}(1) = \frac{\pi}{4}$ (or $45^\circ$).
*   **Polar Form:** $\sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$ or $\sqrt{2}e^{i\pi/4}$.

**(e) $z_5 = 1 - i$**
*   **Modulus:** $r = \sqrt{1^2 + (-1)^2} = \sqrt{2}$
*   **Argument:** Quadrant IV ($x$ positive, $y$ negative). $\theta = \tan^{-1}(-1/1) = -\frac{\pi}{4}$ (or $-45^\circ$).
*   **Polar Form:** $\sqrt{2}\left(\cos\left(-\frac{\pi}{4}\right) + i\sin\left(-\frac{\pi}{4}\right)\right)$ or $\sqrt{2}e^{-i\pi/4}$.

**(f) $z_6 = -1 - i$**
*   **Modulus:** $r = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$
*   **Argument:** Quadrant III ($x$ negative, $y$ negative). The reference angle is $\pi/4$. The angle relative to the negative real axis is $-\pi + \pi/4 = -\frac{3\pi}{4}$ (or $-135^\circ$).
*   **Polar Form:** $\sqrt{2}\left(\cos\left(-\frac{3\pi}{4}\right) + i\sin\left(-\frac{3\pi}{4}\right)\right)$ or $\sqrt{2}e^{-i3\pi/4}$.

***

### Q70. Example 1.3.4. (Principal argument): Compute $Argz_{j},$ where $z_{j}$ is as in the preceding example for $j=1,...,6$.

**Solution:**

The **Principal Argument**, denoted with a capital "A" as $\text{Arg}(z)$, is the unique angle $\theta$ of the complex number that satisfies the restriction:
$$-\pi < \text{Arg}(z) \le \pi$$
*(or $-180^\circ < \text{Arg}(z) \le 180^\circ$)*.

We will simply extract the angles we calculated in Q69 and ensure they fall within this specified principal range.

*   **For $z_1 = 5$:** The angle is $0$. Since $0$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_1) = 0$$

*   **For $z_2 = -3i$:** The angle is $-\pi/2$. Since $-\pi/2$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_2) = -\frac{\pi}{2}$$

*   **For $z_3 = \sqrt{3} + i$:** The angle is $\pi/6$. Since $\pi/6$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_3) = \frac{\pi}{6}$$

*   **For $z_4 = 1 + i$:** The angle is $\pi/4$. Since $\pi/4$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_4) = \frac{\pi}{4}$$

*   **For $z_5 = 1 - i$:** The angle is $-\pi/4$. Since $-\pi/4$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_5) = -\frac{\pi}{4}$$

*   **For $z_6 = -1 - i$:** The angle is $-3\pi/4$. Since $-3\pi/4$ is within $(-\pi, \pi]$, the principal argument is:
    $$\text{Arg}(z_6) = -\frac{3\pi}{4}$$

***

### Q71. Problem 2.1: Prove that $(i)\arg(z_{1}z_{2})=\arg~z_{1}+\arg~z_{2}$ and $(ii)\arg\overline{z}=-\arg~z$

**Solution:**

We will prove these properties using the exponential (polar) representation of complex numbers. Note that the lowercase "arg" denotes the general argument, which allows for multiples of $2\pi$.

**Part (i): Prove $\arg(z_1 z_2) = \arg z_1 + \arg z_2$**

1.  **Define the complex numbers:** Let $z_1$ and $z_2$ be expressed in polar form as:
    $$z_1 = r_1 e^{i\theta_1}$$
    $$z_2 = r_2 e^{i\theta_2}$$
    By definition, their arguments are $\arg(z_1) = \theta_1$ and $\arg(z_2) = \theta_2$.
2.  **Multiply the numbers:**
    $$z_1 z_2 = (r_1 e^{i\theta_1})(r_2 e^{i\theta_2})$$
3.  **Combine using exponent rules:** The rule $e^a \cdot e^b = e^{a+b}$ gives:
    $$z_1 z_2 = (r_1 r_2) e^{i(\theta_1 + \theta_2)}$$
4.  **Identify the argument of the product:** The resulting expression is in standard polar form $Re^{i\Theta}$, where the modulus is $r_1r_2$ and the argument is $(\theta_1 + \theta_2)$.
    $$\arg(z_1 z_2) = \theta_1 + \theta_2$$
5.  **Substitute the original arguments back:**
    $$\arg(z_1 z_2) = \arg(z_1) + \arg(z_2)$$ 
    *(Holding true up to additive multiples of $2\pi$)*. **(Proved)**

**Part (ii): Prove $\arg(\overline{z}) = -\arg z$**

1.  **Define the complex number:** Let $z$ be expressed in polar form as:
    $$z = r e^{i\theta}$$
    where $\arg(z) = \theta$.
2.  **Find the complex conjugate:** Using Euler's formula, $z = r(\cos\theta + i\sin\theta)$. 
    The complex conjugate $\overline{z}$ flips the sign of the imaginary part:
    $$\overline{z} = r(\cos\theta - i\sin\theta)$$
3.  **Apply trigonometric properties:** Since cosine is even ($\cos\theta = \cos(-\theta)$) and sine is odd ($-\sin\theta = \sin(-\theta)$), we can rewrite the conjugate as:
    $$\overline{z} = r(\cos(-\theta) + i\sin(-\theta))$$
4.  **Convert back to exponential form:**
    $$\overline{z} = r e^{i(-\theta)}$$
5.  **Identify the new argument:** The argument of $\overline{z}$ is clearly $-\theta$.
    $$\arg(\overline{z}) = -\theta$$
6.  **Substitute the original argument back:**
    $$\arg(\overline{z}) = -\arg(z)$$ 
    **(Proved)**

***

### Q72. Prob. 2.2: Express $2+2\sqrt{3}i$ in polar form.

**Solution:**

We need to convert the complex number $z = 2 + 2\sqrt{3}i$ into the standard polar form $z = r(\cos\theta + i\sin\theta)$ or $re^{i\theta}$.

**Step 1: Identify Cartesian coordinates.**
The complex number is in the form $z = x + iy$.
*   Real part: $x = 2$
*   Imaginary part: $y = 2\sqrt{3}$

**Step 2: Calculate the Modulus ($r$).**
The modulus is the distance from the origin.
$$r = \sqrt{x^2 + y^2}$$
$$r = \sqrt{2^2 + (2\sqrt{3})^2}$$
$$r = \sqrt{4 + 4(3)}$$
$$r = \sqrt{4 + 12}$$
$$r = \sqrt{16} = 4$$

**Step 3: Calculate the Argument ($\theta$).**
The argument $\theta$ is the angle made with the positive real axis.
Since both $x$ and $y$ are positive, the point $(2, 2\sqrt{3})$ lies in the **first quadrant**.
For the first quadrant, we can calculate the principal argument directly:
$$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$
$$\theta = \tan^{-1}\left(\frac{2\sqrt{3}}{2}\right)$$
$$\theta = \tan^{-1}(\sqrt{3})$$

From standard trigonometric values, we know that $\tan(60^\circ) = \sqrt{3}$.
Therefore, $\theta = 60^\circ$, or in radians:
$$\theta = \frac{\pi}{3}$$

**Step 4: Write the polar form.**
Substitute the calculated modulus $r=4$ and argument $\theta=\frac{\pi}{3}$ into the standard polar format.
$$z = 4\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)$$
Or, in exponential form:
$$z = 4e^{i\pi/3}$$

**Answer:** 
The polar form is **$4\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)$**.
Here are the detailed solutions for the next four questions (Q73 to Q76). 

*(Note: Several of these questions from the Feruj Sheet are conceptually identical to problems covered earlier in the Firoz Note section. Detailed step-by-step solutions are provided again below for completeness).*

### Q73. Prob. 2.3: Express $-\sqrt{6}-\sqrt{2}i$ in polar form.

**Solution:**

We need to convert the Cartesian complex number $z = -\sqrt{6} - \sqrt{2}i$ into the polar form $z = r(\cos\theta + i\sin\theta)$.

**Step 1: Identify Cartesian coordinates.**
The complex number is in the form $z = x + iy$.
*   Real part: $x = -\sqrt{6}$
*   Imaginary part: $y = -\sqrt{2}$

**Step 2: Calculate the Modulus ($r$).**
The modulus represents the absolute distance from the origin $(0,0)$.
$$r = \sqrt{x^2 + y^2}$$
$$r = \sqrt{(-\sqrt{6})^2 + (-\sqrt{2})^2}$$
$$r = \sqrt{6 + 2}$$
$$r = \sqrt{8} = \sqrt{4 \cdot 2} = 2\sqrt{2}$$

**Step 3: Calculate the Argument ($\theta$).**
The argument $\theta$ is the angle the vector makes with the positive real axis.
Because both $x$ and $y$ are negative, the point lies in the **third quadrant**.

First, find the reference angle $\alpha$ in the first quadrant:
$$\alpha = \tan^{-1}\left(\left| \frac{y}{x} \right|\right)$$
$$\alpha = \tan^{-1}\left(\frac{\sqrt{2}}{\sqrt{6}}\right)$$
$$\alpha = \tan^{-1}\left(\sqrt{\frac{2}{6}}\right) = \tan^{-1}\left(\sqrt{\frac{1}{3}}\right) = \tan^{-1}\left(\frac{1}{\sqrt{3}}\right)$$
From standard trigonometric ratios, we know that $\tan(\frac{\pi}{6}) = \frac{1}{\sqrt{3}}$. Thus, $\alpha = \frac{\pi}{6}$ (or $30^\circ$).

Now, adjust for the third quadrant. 
To find the **principal argument** (which must be in the range $-\pi < \theta \le \pi$), we subtract $\pi$ from the reference angle:
$$\theta = -\pi + \alpha = -\pi + \frac{\pi}{6} = -\frac{6\pi}{6} + \frac{\pi}{6} = -\frac{5\pi}{6}$$
*(Alternatively, using a positive argument in the range $0 \le \theta < 2\pi$: $\theta = \pi + \pi/6 = 7\pi/6$).*

**Step 4: Write the polar form.**
Substitute the modulus $r = 2\sqrt{2}$ and the principal argument $\theta = -\frac{5\pi}{6}$ into the polar structure:
$$z = 2\sqrt{2} \left[ \cos\left(-\frac{5\pi}{6}\right) + i\sin\left(-\frac{5\pi}{6}\right) \right]$$

**Answer:** 
The polar form is **$2\sqrt{2} \left( \cos\left(-\frac{5\pi}{6}\right) + i\sin\left(-\frac{5\pi}{6}\right) \right)$** or equivalently **$2\sqrt{2}e^{-i5\pi/6}$**.

***

### Q74. Question: Prove De Moivre's theorem: $(\cos~\theta+i~\sin~\theta)^{n}=\cos~n\theta+i~\sin~n\theta$ where n is any positive integer
![[IMG_20260725_092823034_HDR.jpg]]
**Solution:**

We will prove this theorem using the Principle of Mathematical Induction.

**Step 1: Verify the Base Case ($n = 1$)**
For $n = 1$, we substitute $1$ into both sides of the equation.
*   **Left-Hand Side (LHS):** $(\cos\theta + i\sin\theta)^1 = \cos\theta + i\sin\theta$
*   **Right-Hand Side (RHS):** $\cos(1\cdot\theta) + i\sin(1\cdot\theta) = \cos\theta + i\sin\theta$
Since LHS = RHS, the statement is true for $n=1$.

**Step 2: Formulate the Inductive Hypothesis**
Assume that the theorem holds true for some arbitrary positive integer $k$. That is:
$$(\cos\theta + i\sin\theta)^k = \cos(k\theta) + i\sin(k\theta) \quad \text{--- (Assumption)}$$

**Step 3: Perform the Inductive Step ($n = k + 1$)**
We must prove that if the assumption holds, the theorem must also be true for $n = k + 1$. 
Let's evaluate the expression for $n = k + 1$:
$$(\cos\theta + i\sin\theta)^{k+1}$$

Using standard exponent rules ($x^{a+b} = x^a \cdot x^b$), split the expression:
$$= (\cos\theta + i\sin\theta)^k \cdot (\cos\theta + i\sin\theta)^1$$

Now, substitute our Inductive Hypothesis for the first term:
$$= (\cos(k\theta) + i\sin(k\theta)) \cdot (\cos\theta + i\sin\theta)$$

Multiply the two complex binomials together (using FOIL):
$$= \cos(k\theta)\cos\theta + i\cos(k\theta)\sin\theta + i\sin(k\theta)\cos\theta + i^2\sin(k\theta)\sin\theta$$

Since $i^2 = -1$, substitute it and group the real and imaginary parts:
$$= [\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta] + i[\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta]$$

**Step 4: Apply Trigonometric Compound Angle Identities**
We utilize the standard angle addition formulas:
1.  $\cos(A + B) = \cos A\cos B - \sin A\sin B$
2.  $\sin(A + B) = \sin A\cos B + \cos A\sin B$

Let $A = k\theta$ and $B = \theta$:
*   The real part becomes: $\cos(k\theta + \theta) = \cos((k+1)\theta)$
*   The imaginary part becomes: $\sin(k\theta + \theta) = \sin((k+1)\theta)$

Substitute these back:
$$= \cos((k+1)\theta) + i\sin((k+1)\theta)$$

**Step 5: Conclusion**
We have shown that if the formula is true for $n=k$, it inherently must be true for $n=k+1$. Because we proved it is true for the base case $n=1$, it is therefore true for all positive integers $n$ by mathematical induction. **(Proved)**

***

### Q75. Example 1.3.8. (Double-angle Identities): Use De Moivre's identity with $n=2$ to derive the double-angle formulas for $\cos~2\theta$ and $\sin 2\theta$.

**Solution:**

De Moivre's Theorem allows us to quickly link exponents of complex numbers to multiples of angles, making it a powerful tool to derive trigonometric identities.

**Step 1: Apply De Moivre's theorem for $n=2$.**
The theorem states: $(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$.
Substitute $n = 2$:
$$(\cos\theta + i\sin\theta)^2 = \cos(2\theta) + i\sin(2\theta) \quad \text{--- (Equation 1)}$$

**Step 2: Expand the left side using basic algebra.**
Treat $(\cos\theta + i\sin\theta)$ as a standard binomial $(a+b)$ and square it using $(a+b)^2 = a^2 + 2ab + b^2$:
$$(\cos\theta + i\sin\theta)^2 = (\cos\theta)^2 + 2(\cos\theta)(i\sin\theta) + (i\sin\theta)^2$$
$$(\cos\theta + i\sin\theta)^2 = \cos^2\theta + 2i\sin\theta\cos\theta + i^2\sin^2\theta$$

We know that the imaginary unit squared is $i^2 = -1$. Substitute this into the last term:
$$(\cos\theta + i\sin\theta)^2 = \cos^2\theta + 2i\sin\theta\cos\theta - \sin^2\theta$$

Rearrange to group the real terms and imaginary terms:
$$(\cos\theta + i\sin\theta)^2 = (\cos^2\theta - \sin^2\theta) + i(2\sin\theta\cos\theta) \quad \text{--- (Equation 2)}$$

**Step 3: Equate the two representations.**
Since Equation 1 and Equation 2 are expansions of the exact same expression, they must be perfectly equal to each other:
$$\cos(2\theta) + i\sin(2\theta) = (\cos^2\theta - \sin^2\theta) + i(2\sin\theta\cos\theta)$$

**Step 4: Separate into real and imaginary parts.**
For two complex numbers to be equal, their real parts must be identical, and their imaginary parts must be identical.
*   **Equating the Real parts:**
    $$\cos(2\theta) = \cos^2\theta - \sin^2\theta$$
*   **Equating the Imaginary parts (the coefficients of $i$):**
    $$\sin(2\theta) = 2\sin\theta\cos\theta$$

These two equations are the exact standard double-angle formulas for cosine and sine. **(Derived)**

***

### Q76. Problems.1: Prove that $e^{i\theta}=e^{i(\theta+2k\pi)}$ , $k=0,\pm1,\pm2,\dots$

**Solution:**

This question asks us to mathematically prove that the complex exponential function $e^{i\theta}$ is periodic with a period of $2\pi$.

**Step 1: Start by expanding the Right-Hand Side (RHS).**
$$\text{RHS} = e^{i(\theta + 2k\pi)}$$
Distribute the $i$ in the exponent:
$$= e^{i\theta + i2k\pi}$$

**Step 2: Apply exponent rules.**
Using the fundamental law of exponents $e^{a+b} = e^a \cdot e^b$, we separate the sum into a product:
$$= e^{i\theta} \cdot e^{i2k\pi}$$

**Step 3: Evaluate $e^{i2k\pi}$ using Euler's Formula.**
Euler's formula defines the complex exponential as $e^{i\phi} = \cos\phi + i\sin\phi$. 
Apply this to the angle $\phi = 2k\pi$:
$$e^{i2k\pi} = \cos(2k\pi) + i\sin(2k\pi)$$

**Step 4: Use trigonometric properties of integers.**
We are given that $k$ is an integer ($0, \pm1, \pm2, \dots$). 
*   $2k\pi$ represents full $360^\circ$ rotations around the unit circle. 
*   The cosine of any integer multiple of $2\pi$ is always exactly $1$: $\cos(2k\pi) = 1$.
*   The sine of any integer multiple of $2\pi$ is always exactly $0$: $\sin(2k\pi) = 0$.

Substitute these trigonometric values back into the expression:
$$e^{i2k\pi} = 1 + i(0)$$
$$e^{i2k\pi} = 1$$

**Step 5: Final substitution and conclusion.**
Substitute $e^{i2k\pi} = 1$ back into our expanded RHS from Step 2:
$$\text{RHS} = e^{i\theta} \cdot (1)$$
$$\text{RHS} = e^{i\theta}$$

This matches the Left-Hand Side (LHS).
$$e^{i\theta} = e^{i(\theta+2k\pi)}$$
**(Proved)**




Here are the detailed solutions for the next four questions (Q77 to Q80).

### Q77. Problem 3.2: (a) Find the roots of $z^{5}+32=0$ and (b) locate values of $z^{5}$ in the complex Plane.

*(Note: Part (b) asks to locate the values of "$z^5$". Because $z^5 = -32$, locating $z^5$ just means plotting the single point $-32$ on the real axis. However, in the context of this specific topic, this is almost certainly a typographical error in the source material intended to say "locate the values of **$z$**" (i.e., the roots). I will solve for the roots and plot the roots).*

**Solution:**

**Part (a): Find the roots of $z^5 + 32 = 0$**

**Step 1: Isolate $z$**
$$z^5 = -32$$
We are looking for the five $5^{\text{th}}$ roots of the complex number $w = -32 + 0i$.

**Step 2: Express $w = -32$ in polar form**
*   **Modulus ($r$):** The distance from the origin to $-32$ is $32$.
*   **Argument ($\theta$):** The number lies on the negative real axis, so the angle is exactly $\pi$ radians ($180^\circ$).

Adding the $2k\pi$ periodicity, the general polar form is:
$$w = 32 \left( \cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi) \right)$$

**Step 3: Apply De Moivre's Theorem for roots**
To find the $5^{\text{th}}$ roots, we raise $w$ to the power of $\frac{1}{5}$:
$$z_k = w^{\frac{1}{5}} = 32^{\frac{1}{5}} \left[ \cos\left(\frac{\pi + 2k\pi}{5}\right) + i\sin\left(\frac{\pi + 2k\pi}{5}\right) \right]$$
*   The magnitude for all roots is $R = 32^{\frac{1}{5}} = (2^5)^{\frac{1}{5}} = 2$.
*   The angles are $\alpha_k = \frac{\pi(1 + 2k)}{5}$ for $k = 0, 1, 2, 3, 4$.

**Step 4: Calculate the specific roots (converting to degrees for clarity)**
Since $\pi = 180^\circ$, the base angle is $\frac{180^\circ}{5} = 36^\circ$, and we add $\frac{360^\circ}{5} = 72^\circ$ for each subsequent root.
*   **For $k = 0$:** $\alpha_0 = 36^\circ$
    $$z_0 = 2(\cos 36^\circ + i\sin 36^\circ)$$
*   **For $k = 1$:** $\alpha_1 = 36^\circ + 72^\circ = 108^\circ$
    $$z_1 = 2(\cos 108^\circ + i\sin 108^\circ)$$
*   **For $k = 2$:** $\alpha_2 = 108^\circ + 72^\circ = 180^\circ$
    $$z_2 = 2(\cos 180^\circ + i\sin 180^\circ) = 2(-1 + 0i) = -2$$
*   **For $k = 3$:** $\alpha_3 = 180^\circ + 72^\circ = 252^\circ$
    $$z_3 = 2(\cos 252^\circ + i\sin 252^\circ)$$
*   **For $k = 4$:** $\alpha_4 = 252^\circ + 72^\circ = 324^\circ$
    $$z_4 = 2(\cos 324^\circ + i\sin 324^\circ)$$

**Part (b): Locate the roots graphically in the complex plane**
1.  Draw the real (x) and imaginary (y) axes.
2.  Draw a circle centered at the origin $(0,0)$ with a radius of exactly $2$.
3.  All five roots lie on the circumference of this circle.
4.  Because they are spaced evenly by $72^\circ$, they form the vertices of a **regular pentagon**.
5.  Plot $z_2$ directly on the negative real axis at $(-2, 0)$. Plot $z_0$ in Quadrant I ($36^\circ$), $z_1$ in Quadrant II ($108^\circ$), $z_3$ in Quadrant III ($252^\circ$), and $z_4$ in Quadrant IV ($324^\circ$).

***

### Q78. Problem 3.3: Find the roots of the followings: (i) $z^{2}+\pi^{2}=0$ (ii) $z^{6}+1=0$ (iii) $z^{2}+1=0$

**Solution:**

**Part (i): $z^2 + \pi^2 = 0$**
1.  Isolate $z^2$:
    $$z^2 = -\pi^2$$
2.  Take the square root of both sides.
    $$z = \pm\sqrt{-\pi^2}$$
    $$z = \pm\sqrt{\pi^2 \cdot (-1)}$$
    $$z = \pm\pi\sqrt{-1}$$
3.  Since $\sqrt{-1} = i$:
    **$z = \pm i\pi$** (The two roots are $i\pi$ and $-i\pi$).

---

**Part (ii): $z^6 + 1 = 0$**
1.  Isolate $z^6$:
    $$z^6 = -1$$
2.  Write $-1$ in polar form:
    $w = 1 \cdot (\cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi))$
3.  Apply De Moivre's theorem for the 6th roots ($k = 0, 1, 2, 3, 4, 5$):
    $$z_k = 1^{\frac{1}{6}} \left[ \cos\left(\frac{\pi + 2k\pi}{6}\right) + i\sin\left(\frac{\pi + 2k\pi}{6}\right) \right]$$
4.  Calculate the 6 roots:
    *   $k=0$: $z_0 = \cos\frac{\pi}{6} + i\sin\frac{\pi}{6} = \frac{\sqrt{3}}{2} + \frac{1}{2}i$
    *   $k=1$: $z_1 = \cos\frac{3\pi}{6} + i\sin\frac{3\pi}{6} = \cos\frac{\pi}{2} + i\sin\frac{\pi}{2} = i$
    *   $k=2$: $z_2 = \cos\frac{5\pi}{6} + i\sin\frac{5\pi}{6} = -\frac{\sqrt{3}}{2} + \frac{1}{2}i$
    *   $k=3$: $z_3 = \cos\frac{7\pi}{6} + i\sin\frac{7\pi}{6} = -\frac{\sqrt{3}}{2} - \frac{1}{2}i$
    *   $k=4$: $z_4 = \cos\frac{9\pi}{6} + i\sin\frac{9\pi}{6} = \cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2} = -i$
    *   $k=5$: $z_5 = \cos\frac{11\pi}{6} + i\sin\frac{11\pi}{6} = \frac{\sqrt{3}}{2} - \frac{1}{2}i$

---

**Part (iii): $z^2 + 1 = 0$**
1.  Isolate $z^2$:
    $$z^2 = -1$$
2.  Take the square root of both sides:
    $$z = \pm\sqrt{-1}$$
3.  By the fundamental definition of the imaginary unit:
    **$z = \pm i$** (The two roots are $i$ and $-i$).

***

### Q79. Problem 3.4: Find an equation for (a) a circle of radius 4 with center at $(-2,1)$

**Solution:**

We need to provide the mathematical equation representing this specific circle in the complex plane.

**Step 1: Understand the definition of a circle in the complex plane.**
Geometrically, a circle is the locus (set) of all points $z$ that are at a constant, fixed distance from a central point. 
In complex variables, the distance between any arbitrary point $z$ and a fixed center point $z_0$ is defined by the modulus of their difference: $|z - z_0|$.
Therefore, the general equation of a circle is:
$$|z - z_0| = r$$
where $r$ is the constant radius.

**Step 2: Identify the given parameters.**
*   **Radius:** The problem states $r = 4$.
*   **Center:** The Cartesian coordinates are $(-2, 1)$. The x-coordinate represents the real part and the y-coordinate represents the imaginary part. Therefore, the center corresponds to the complex number:
    $$z_0 = -2 + 1i = -2 + i$$

**Step 3: Substitute the parameters into the general equation.**
Replace $z_0$ with $(-2 + i)$ and $r$ with $4$:
$$|z - (-2 + i)| = 4$$

Distribute the negative sign to simplify the expression inside the modulus:
$$|z + 2 - i| = 4$$

This is the standard, concise representation of the circle.

**Answer:** The equation for the circle is **$|z + 2 - i| = 4$**.

***

### Q80. Problem 3.5: Given a complex number Z, interpret geometrically $Ze^{ia}$, where a is real.

*(Note: This is conceptually identical to Q7 and Q59, using "$a$" instead of "$\alpha$").*

**Solution:**

To determine the geometric effect of multiplying by $e^{ia}$, we should represent the original complex number $Z$ in polar (exponential) coordinates.

**Step 1: Express $Z$ in polar form.**
Let $Z$ be represented as a vector in the complex plane. Its polar form is:
$$Z = r e^{i\theta}$$
where:
*   $r = |Z|$ is the modulus (the length of the vector from the origin).
*   $\theta = \arg(Z)$ is the argument (the counterclockwise angle the vector makes with the positive real axis).

**Step 2: Perform the multiplication.**
Multiply $Z$ by the given term $e^{ia}$:
$$Z \cdot e^{ia} = (r e^{i\theta}) \cdot e^{ia}$$

**Step 3: Apply the laws of exponents.**
When multiplying exponential terms with the same base, you add their exponents ($x^m \cdot x^n = x^{m+n}$):
$$Z e^{ia} = r e^{i(\theta + a)}$$

**Step 4: Geometrically interpret the new expression.**
Let's call the new resulting complex number $W = Z e^{ia}$. The new expression $r e^{i(\theta + a)}$ is also in standard polar form. We can analyze its components:
1.  **Modulus (Magnitude):** The modulus of $W$ is $r$. This is exactly the same as the modulus of the original vector $Z$. Therefore, the length of the vector has not changed.
2.  **Argument (Direction):** The new argument of $W$ is $(\theta + a)$. The original angle $\theta$ has been increased by an amount exactly equal to $a$.

**Conclusion:**
Multiplying a complex number $Z$ by $e^{ia}$ (where $a$ is real) does not change the length of the vector representing $Z$, but it adds an angle $a$ to its direction.
Therefore, it geometrically represents a **rotation of the vector $Z$ around the origin by an angle $a$**. 
*   If $a > 0$, the rotation is counter-clockwise.
*   If $a < 0$, the rotation is clockwise.
Here are the detailed solutions for the next four questions (Q81 to Q84).

*(Note: Questions Q81, Q82, and Q83 from the Feruj Sheet are conceptually and numerically identical to questions Q60, Q61, Q62, and Q63 from the Firoz Note. Detailed step-by-step solutions are provided again below for completeness).*

### Q81. Problem 4.1: If $z_{1}=3-i4$ and $z_{2}=-4+i3$, find (i) $z_{1}\circ z_{2}$ (ii) $z_{1}\times z_{2}$.

**Solution:**

In 2D complex vector notation (standard in engineering mathematics), the symbols "$\circ$" and "$\times$" between complex numbers denote the **Dot Product** and the scalar magnitude of the **Cross Product**, respectively. They do not represent standard algebraic complex multiplication.

Let the complex numbers represent 2D Cartesian vectors:
$z_1 = x_1 + iy_1 \implies \vec{v_1} = (x_1, y_1)$
$z_2 = x_2 + iy_2 \implies \vec{v_2} = (x_2, y_2)$

The algebraic definitions for these operations are:
*   **Dot Product ($z_1 \circ z_2$):** $x_1x_2 + y_1y_2$
*   **Cross Product ($z_1 \times z_2$):** $x_1y_2 - x_2y_1$

**Identify the components:**
$z_1 = 3 - 4i \implies x_1 = 3, y_1 = -4$
$z_2 = -4 + 3i \implies x_2 = -4, y_2 = 3$

**Part (i): Find $z_1 \circ z_2$**
$$z_1 \circ z_2 = (x_1)(x_2) + (y_1)(y_2)$$
$$z_1 \circ z_2 = (3)(-4) + (-4)(3)$$
$$z_1 \circ z_2 = -12 - 12 = -24$$

**Part (ii): Find $z_1 \times z_2$**
$$z_1 \times z_2 = (x_1)(y_2) - (x_2)(y_1)$$
$$z_1 \times z_2 = (3)(3) - (-4)(-4)$$
$$z_1 \times z_2 = 9 - 16 = -7$$

*(Self-Check: Both of these can be found simultaneously by calculating $\overline{z_1}z_2$.
$\overline{z_1}z_2 = (3+4i)(-4+3i) = -12 + 9i - 16i + 12i^2 = -12 - 7i - 12 = -24 - 7i$. 
The real part is the dot product ($-24$) and the imaginary part is the cross product ($-7$).)*

**Answer:**
*   **(i) $z_1 \circ z_2 = -24$**
*   **(ii) $z_1 \times z_2 = -7$**

***

### Q82. Problem 4.2: Prove that area of a parallelogram having sides $z_{1}$ and $z_{2}$ is $\vert{}z_{1}\times z_{2}\vert{}$.

**Solution:**

We will prove this geometrically by connecting the definition of the complex 2D cross product to the standard trigonometric formula for the area of a parallelogram.

**Step 1: Express the complex numbers in polar form.**
Let the two sides of the parallelogram be represented by position vectors $z_1$ and $z_2$:
$$z_1 = r_1 e^{i\theta_1}$$
$$z_2 = r_2 e^{i\theta_2}$$
where:
*   $r_1 = |z_1|$ is the length of the first side.
*   $r_2 = |z_2|$ is the length of the second side.
*   The angle between the two sides is $\Delta\theta = \theta_2 - \theta_1$.

**Step 2: State the geometric area of the parallelogram.**
From standard geometry, the area of a parallelogram formed by two adjacent vectors is the product of their lengths and the sine of the angle between them:
$$\text{Area} = r_1 \cdot r_2 \cdot |\sin(\theta_2 - \theta_1)| \quad \text{--- (Equation 1)}$$

**Step 3: Evaluate the complex product $\overline{z_1}z_2$.**
The 2D cross product $z_1 \times z_2$ is mathematically defined as the imaginary part of $\overline{z_1}z_2$. Let's evaluate this:
$$\overline{z_1}z_2 = (r_1 e^{-i\theta_1}) \cdot (r_2 e^{i\theta_2})$$
$$\overline{z_1}z_2 = r_1 r_2 e^{i(\theta_2 - \theta_1)}$$

Using Euler's formula ($e^{i\phi} = \cos\phi + i\sin\phi$), we expand this into real and imaginary parts:
$$\overline{z_1}z_2 = r_1 r_2 [\cos(\theta_2 - \theta_1) + i\sin(\theta_2 - \theta_1)]$$

**Step 4: Extract the cross product.**
Taking the imaginary part gives us the cross product:
$$z_1 \times z_2 = Im(\overline{z_1}z_2) = r_1 r_2 \sin(\theta_2 - \theta_1)$$

**Step 5: Relate the cross product to the Area.**
Take the absolute value (modulus) of the cross product:
$$|z_1 \times z_2| = |r_1 r_2 \sin(\theta_2 - \theta_1)|$$
Since $r_1$ and $r_2$ are lengths (always positive), they can be pulled outside the absolute value:
$$|z_1 \times z_2| = r_1 r_2 |\sin(\theta_2 - \theta_1)|$$

Comparing this result directly with Equation 1, we conclude:
$$\text{Area} = |z_1 \times z_2|$$
**(Proved)**

***

### Q83. Question: Represent graphically the set of values of z for which (a) $\vert{}\frac{z-3}{z+3}\vert{}=2,$ (b) $\vert{}\frac{z-3}{z+3}\vert{}<2.$

**Solution:**

We need to translate these algebraic conditions into geometric loci in the complex plane.

**Part (a): $\left|\frac{z-3}{z+3}\right| = 2$**

**Step 1: Simplify using modulus properties.**
$$\frac{|z - 3|}{|z + 3|} = 2 \implies |z - 3| = 2|z + 3|$$

**Step 2: Substitute $z = x + iy$.**
$$|(x - 3) + iy| = 2|(x + 3) + iy|$$

**Step 3: Apply the distance formula and square both sides.**
The modulus of $a + ib$ is $\sqrt{a^2 + b^2}$.
$$\sqrt{(x - 3)^2 + y^2} = 2\sqrt{(x + 3)^2 + y^2}$$
Squaring both sides removes the square roots:
$$(x - 3)^2 + y^2 = 4 \left[ (x + 3)^2 + y^2 \right]$$

**Step 4: Expand the binomials.**
$$x^2 - 6x + 9 + y^2 = 4(x^2 + 6x + 9 + y^2)$$
$$x^2 - 6x + 9 + y^2 = 4x^2 + 24x + 36 + 4y^2$$

**Step 5: Group terms to form a standard equation.**
Subtract the left-hand terms from the right side:
$$0 = 3x^2 + 3y^2 + 30x + 27$$
Divide by 3:
$$x^2 + y^2 + 10x + 9 = 0$$

**Step 6: Complete the square for $x$.**
$$(x^2 + 10x + 25) + y^2 = -9 + 25$$
$$(x + 5)^2 + y^2 = 16$$
$$(x + 5)^2 + (y - 0)^2 = 4^2$$

**Conclusion for (a):** This is the equation of a **circle**. 
*   **Center:** $(-5, 0)$ or $z = -5$
*   **Radius:** $4$
*   **Graphical Representation:** The set of values forms the boundary (circumference) of this circle.

---

**Part (b): $\left|\frac{z-3}{z+3}\right| < 2$**

**Step 1: Follow the same algebraic steps as (a).**
$$\frac{|z - 3|}{|z + 3|} < 2 \implies |z - 3| < 2|z + 3|$$
$$(x - 3)^2 + y^2 < 4 \left[ (x + 3)^2 + y^2 \right]$$
$$x^2 - 6x + 9 + y^2 < 4x^2 + 24x + 36 + 4y^2$$

**Step 2: Group terms.**
$$0 < 3x^2 + 3y^2 + 30x + 27$$
$$0 < x^2 + y^2 + 10x + 9$$

**Step 3: Complete the square.**
$$-9 + 25 < x^2 + 10x + 25 + y^2$$
$$16 < (x + 5)^2 + y^2$$
$$(x + 5)^2 + (y - 0)^2 > 4^2$$

**Conclusion for (b):** 
The inequality states that the distance squared from any point $(x,y)$ to the center $(-5,0)$ is strictly *greater* than $16$ (the radius squared).
*   **Graphical Representation:** The set of values is the **entire region strictly outside the circle** found in Part (a). It does not include the boundary of the circle itself.

***

### Q84. Problems.1: Prove that the equation of any circle or line in the z plane can be written as $\alpha\overline{z}+\beta z+\overline{\beta}\overline{z}+\gamma=0$ where a and y are real constants while $\beta$ may be a complex constant.

*(Note: There is a typographical error in the source material's equation. The correct standard form for the general equation of a circle or a straight line in the complex plane is $\alpha z\overline{z} + \overline{\beta}z + \beta\overline{z} + \gamma = 0$, where $\alpha, \gamma \in \mathbb{R}$ and $\beta \in \mathbb{C}$. We will prove this corrected, standard mathematical identity).*

**Solution:**

We will prove this by showing that this single equation can transform into the standard geometric equation of a circle (when $\alpha \neq 0$) and the standard equation of a line (when $\alpha = 0$).

**Part 1: Proof for a Circle ($\alpha \neq 0$)**

1.  **Define a circle geometrically:** A circle with center $z_0$ and radius $r$ is given by:
    $$|z - z_0| = r$$
2.  **Square both sides and use $|w|^2 = w\overline{w}$:**
    $$|z - z_0|^2 = r^2$$
    $$(z - z_0)(\overline{z - z_0}) = r^2$$
    $$(z - z_0)(\overline{z} - \overline{z_0}) = r^2$$
3.  **Expand the expression:**
    $$z\overline{z} - z\overline{z_0} - z_0\overline{z} + z_0\overline{z_0} = r^2$$
    $$z\overline{z} - \overline{z_0}z - z_0\overline{z} + (|z_0|^2 - r^2) = 0$$
4.  **Map to the general equation:**
    Let $\alpha = 1$ (a real constant).
    Let $\beta = -z_0$ (a complex constant). This means $\overline{\beta} = -\overline{z_0}$.
    Let $\gamma = |z_0|^2 - r^2$ (a real constant, since absolute values and radii are real).
    
    Substituting these into our expanded equation yields:
    $$\alpha z\overline{z} + \overline{\beta}z + \beta\overline{z} + \gamma = 0$$
    Thus, the equation represents a circle if $\alpha \neq 0$ and $|\beta|^2 > \alpha\gamma$ (to ensure a real, positive radius).

**Part 2: Proof for a Straight Line ($\alpha = 0$)**

1.  **Define a line in Cartesian coordinates:** The standard equation of a straight line in the 2D plane is:
    $$Ax + By + C = 0 \quad \text{(where } A, B, C \in \mathbb{R} \text{)}$$
2.  **Convert $x$ and $y$ into complex variables:**
    We know that $z = x + iy$ and $\overline{z} = x - iy$. 
    Adding them gives: $z + \overline{z} = 2x \implies x = \frac{z + \overline{z}}{2}$
    Subtracting them gives: $z - \overline{z} = 2iy \implies y = \frac{z - \overline{z}}{2i} = \frac{-i(z - \overline{z})}{2}$
3.  **Substitute $x$ and $y$ into the line equation:**
    $$A\left(\frac{z + \overline{z}}{2}\right) + B\left(\frac{z - \overline{z}}{2i}\right) + C = 0$$
    Multiply the whole equation by 2 to clear denominators:
    $$A(z + \overline{z}) + \frac{B}{i}(z - \overline{z}) + 2C = 0$$
    Since $\frac{1}{i} = -i$:
    $$A(z + \overline{z}) - iB(z - \overline{z}) + 2C = 0$$
4.  **Group the $z$ and $\overline{z}$ terms:**
    $$(A - iB)z + (A + iB)\overline{z} + 2C = 0$$
5.  **Map to the general equation:**
    Let $\alpha = 0$ (a real constant).
    Let $\beta = A + iB$ (a complex constant). This means $\overline{\beta} = A - iB$.
    Let $\gamma = 2C$ (a real constant).
    
    Substituting these into our grouped equation yields:
    $$\alpha z\overline{z} + \overline{\beta}z + \beta\overline{z} + \gamma = 0$$
    
**Conclusion:**
Because both a circle and a straight line can be algebraically manipulated into the exact form $\alpha z\overline{z} + \overline{\beta}z + \beta\overline{z} + \gamma = 0$ (depending solely on the value of the real constant $\alpha$), we have proven that this single equation represents any circle or line in the complex plane. **(Proved)**


Here are the detailed solutions for the next four questions (Q85 to Q88).

### Q85. Problem 5.2: Find an equation for the circle passing through the points 1-i, 2i, $1+i$.

**Solution:**

We need to find the equation of a circle that passes through three specific points in the complex plane: $z_1 = 1 - i$, $z_2 = 0 + 2i$, and $z_3 = 1 + i$.

**Step 1: Convert the complex numbers to Cartesian coordinates.**
In the $xy$-plane, the three points are:
*   $P_1 (1, -1)$
*   $P_2 (0, 2)$
*   $P_3 (1, 1)$

**Step 2: Use the general Cartesian equation of a circle.**
The general equation of a circle is:
$$x^2 + y^2 + Dx + Ey + F = 0$$
where $D, E,$ and $F$ are real constants. We will substitute our three points into this equation to create a system of three linear equations.

*   **Substitute $P_1 (1, -1)$:**
    $$1^2 + (-1)^2 + D(1) + E(-1) + F = 0$$
    $$1 + 1 + D - E + F = 0$$
    $$D - E + F = -2 \quad \text{--- (Equation 1)}$$

*   **Substitute $P_3 (1, 1)$:** *(Doing this one next because it's similar to P1)*
    $$1^2 + 1^2 + D(1) + E(1) + F = 0$$
    $$1 + 1 + D + E + F = 0$$
    $$D + E + F = -2 \quad \text{--- (Equation 2)}$$

*   **Substitute $P_2 (0, 2)$:**
    $$0^2 + 2^2 + D(0) + E(2) + F = 0$$
    $$4 + 2E + F = 0$$
    $$2E + F = -4 \quad \text{--- (Equation 3)}$$

**Step 3: Solve the system of equations.**
Subtract Equation 1 from Equation 2:
$$(D + E + F) - (D - E + F) = -2 - (-2)$$
$$2E = 0 \implies E = 0$$

Substitute $E = 0$ into Equation 3:
$$2(0) + F = -4 \implies F = -4$$

Substitute $E = 0$ and $F = -4$ into Equation 2:
$$D + 0 - 4 = -2 \implies D = 2$$

**Step 4: Write the Cartesian equation and find the center/radius.**
Substitute $D=2, E=0, F=-4$ back into the general equation:
$$x^2 + y^2 + 2x - 4 = 0$$

To find the center and radius, complete the square for the $x$ terms:
$$(x^2 + 2x) + y^2 = 4$$
$$(x^2 + 2x + 1) + y^2 = 4 + 1$$
$$(x + 1)^2 + (y - 0)^2 = 5$$
$$(x - (-1))^2 + (y - 0)^2 = (\sqrt{5})^2$$

This is a circle with:
*   **Center:** $(h, k) = (-1, 0)$, which corresponds to the complex number $z_0 = -1$.
*   **Radius:** $r = \sqrt{5}$.

**Step 5: Convert back to the complex plane format.**
The standard equation for a circle in the complex plane is $|z - z_0| = r$.
$$|z - (-1)| = \sqrt{5}$$
$$|z + 1| = \sqrt{5}$$

**Answer:** The equation for the circle is **$|z + 1| = \sqrt{5}$** (or $x^2 + y^2 + 2x - 4 = 0$ in Cartesian form).

***

### Q86. Problem 5.3: Find the radius and coordinate of the follwings: where C is the circle $(i)\vert{}z+1+i\vert{}=2$ $(ii)\vert{}z+1-i\vert{}=2$ (iii) z = 1

**Solution:**

The standard equation of a circle in the complex plane is $|z - z_0| = r$, where $z_0$ is the coordinate of the center and $r$ is the radius. We must rearrange the given equations into this standard form.

**Part (i): $|z + 1 + i| = 2$**
Rewrite the expression inside the modulus to isolate the minus sign:
$$|z - (-1 - i)| = 2$$
By comparing this to $|z - z_0| = r$, we get:
*   **Center coordinate ($z_0$):** $-1 - i$ (In Cartesian coordinates, this is the point **$(-1, -1)$**).
*   **Radius ($r$):** **$2$**.

**Part (ii): $|z + 1 - i| = 2$**
Rewrite the expression inside the modulus:
$$|z - (-1 + i)| = 2$$
By comparing this to $|z - z_0| = r$, we get:
*   **Center coordinate ($z_0$):** $-1 + i$ (In Cartesian coordinates, this is the point **$(-1, 1)$**).
*   **Radius ($r$):** **$2$**.

**Part (iii): $z = 1$**
*(Note: As written, "$z=1$" is the equation of a single point, not a circle. However, in the context of typical complex variables exams where it explicitly states "where C is the circle...", this is universally a typographical error for **$|z| = 1$**. I will provide the answer for the corrected standard interpretation).*

Assuming the intended equation is **$|z| = 1$**:
Rewrite in standard form:
$$|z - 0| = 1$$
*   **Center coordinate ($z_0$):** $0$ (or $0+0i$, which is the origin **$(0,0)$**).
*   **Radius ($r$):** **$1$**.

*(If taken literally as $z=1$, it represents a "point circle" with center $(1,0)$ and radius $0$).*

***

### Q87. Problem 5.4: Explain the fallacy: $-1=\sqrt{-1}\sqrt{-1}=\sqrt{(-1)(-1)}=\sqrt{1}=1$ Hence $1=-1$.

**Solution:**

This is a famous mathematical paradox. The fallacy lies in the misapplication of a rule of radicals that is only partially true.

**The Rule in Question:**
The product rule for square roots states that:
$$\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}$$

**The Fallacy Explained:**
In basic algebra, students are taught this rule using real, positive numbers. However, **this rule is only universally true if at least one of the real numbers $a$ or $b$ is non-negative ($a \ge 0$ or $b \ge 0$).**

When *both* $a$ and $b$ are strictly negative (as in $a = -1$ and $b = -1$), the rule completely breaks down. The principal square root function is multi-valued when extended to the complex plane. To maintain consistency, mathematics defines the principal branch of the square root such that for a negative real number $-x$ (where $x>0$), $\sqrt{-x} = i\sqrt{x}$.

Let's break down the exact sequence of the paradox:
1.  **$-1 = \sqrt{-1}\sqrt{-1}$** : This step is **Correct**. By definition, the imaginary unit $i = \sqrt{-1}$, and $i \cdot i = i^2 = -1$.
2.  **$\sqrt{-1}\sqrt{-1} = \sqrt{(-1)(-1)}$** : This step is **Incorrect (The Fallacy)**. Because both numbers are negative, you cannot combine them under a single square root radical. By blindly multiplying the negatives inside the root, you jump from the imaginary number line back to the positive real number line, discarding the necessary $i^2 = -1$ phase shift.
3.  **$\sqrt{(-1)(-1)} = \sqrt{1} = 1$** : This step is mathematically correct based *only* on the expression $\sqrt{1}$, but it's built on the illegal operation from the previous step.

**Conclusion:**
The fallacy occurs exactly at the step $\sqrt{-1}\sqrt{-1} = \sqrt{(-1)(-1)}$. The algebraic identity $\sqrt{a}\sqrt{b} = \sqrt{ab}$ is strictly invalid when $a < 0$ and $b < 0$. 

***

### Q88. Problems 1.1 Question 1: Find the real and imaginary parts of the following: 
(a) $3x+2iy-ix+5y=7+5i$. 
(b) $x-3iy+4ix-2y-5-10i=(x+y+2)-(y-x+3)i$. 
(d) $f(z)=i~ze^{-z}$ 
(e) $f(z)=\sqrt{z}$ 
(f) $\frac{z-a}{z+a}$ 
(g) $(\frac{-1+i\sqrt{3}}{2})^{3}$

**Solution:**

This question contains two types of problems: (a) and (b) are algebraic equations where we must solve for the real variables $x$ and $y$, while (d), (e), (f), and (g) require us to separate complex expressions into their real $u(x,y)$ and imaginary $v(x,y)$ functions.

---
**Part (a): Solve $3x+2iy-ix+5y=7+5i$**
Group the real and imaginary terms on the left side:
$$(3x + 5y) + i(-x + 2y) = 7 + 5i$$
For two complex numbers to be equal, their real parts and imaginary parts must be equal:
1.  $3x + 5y = 7$ (Real part)
2.  $-x + 2y = 5$ (Imaginary part) $\implies x = 2y - 5$

Substitute $x$ into equation 1:
$$3(2y - 5) + 5y = 7$$
$$6y - 15 + 5y = 7$$
$$11y = 22 \implies y = 2$$
Find $x$:
$$x = 2(2) - 5 = 4 - 5 = -1$$
**Answer (a):** The real part is $x = -1$, and the imaginary part is $y = 2$.

---
**Part (b): Solve $x-3iy+4ix-2y-5-10i=(x+y+2)-(y-x+3)i$**
Group the real and imaginary terms on both sides:
$$\text{LHS}: (x - 2y - 5) + i(4x - 3y - 10)$$
$$\text{RHS}: (x + y + 2) + i(-y + x - 3)$$
Equate the real parts:
$$x - 2y - 5 = x + y + 2$$
$$-3y = 7 \implies y = -\frac{7}{3}$$
Equate the imaginary parts:
$$4x - 3y - 10 = x - y - 3$$
$$3x - 2y = 7$$
Substitute $y = -7/3$:
$$3x - 2\left(-\frac{7}{3}\right) = 7$$
$$3x + \frac{14}{3} = \frac{21}{3}$$
$$3x = \frac{7}{3} \implies x = \frac{7}{9}$$
**Answer (b):** Real part $x = \frac{7}{9}$, Imaginary part $y = -\frac{7}{3}$.

---
**Part (d): $f(z) = ize^{-z}$**
Let $z = x + iy$.
$$f(z) = i(x + iy) e^{-(x+iy)}$$
$$f(z) = (ix + i^2y) e^{-x} e^{-iy}$$
Since $i^2 = -1$ and $e^{-iy} = \cos y - i\sin y$:
$$f(z) = (-y + ix) e^{-x} (\cos y - i\sin y)$$
$$f(z) = e^{-x} \left[ -y\cos y + iy\sin y + ix\cos y - i^2x\sin y \right]$$
$$f(z) = e^{-x} \left[ -y\cos y + iy\sin y + ix\cos y + x\sin y \right]$$
Group real and imaginary parts:
$$f(z) = e^{-x}(x\sin y - y\cos y) + i \cdot e^{-x}(x\cos y + y\sin y)$$
**Answer (d):** 
*   **Real part:** $u = e^{-x}(x\sin y - y\cos y)$
*   **Imaginary part:** $v = e^{-x}(x\cos y + y\sin y)$

---
**Part (e): $f(z) = \sqrt{z}$**
It is easiest to find this using polar coordinates. Let $z = r e^{i\theta}$, where $r = \sqrt{x^2+y^2}$ and $\theta = \tan^{-1}(y/x)$.
$$f(z) = \sqrt{r e^{i\theta}} = \sqrt{r} e^{i\theta/2}$$
Using Euler's formula:
$$f(z) = \sqrt{r} \left( \cos\frac{\theta}{2} + i\sin\frac{\theta}{2} \right)$$
**Answer (e):** 
*   **Real part:** $u = \sqrt{r}\cos(\frac{\theta}{2})$
*   **Imaginary part:** $v = \sqrt{r}\sin(\frac{\theta}{2})$

---
**Part (f): $f(z) = \frac{z-a}{z+a}$** *(Assuming 'a' is a real constant)*
Let $z = x + iy$.
$$f(z) = \frac{(x-a) + iy}{(x+a) + iy}$$
Multiply numerator and denominator by the complex conjugate of the denominator:
$$f(z) = \frac{(x-a) + iy}{(x+a) + iy} \cdot \frac{(x+a) - iy}{(x+a) - iy}$$
Denominator: $(x+a)^2 - i^2y^2 = (x+a)^2 + y^2$.
Numerator: $(x-a)(x+a) - iy(x-a) + iy(x+a) - i^2y^2$
$$= (x^2 - a^2) - ixy + iay + ixy + iay + y^2$$
$$= (x^2 + y^2 - a^2) + i(2ay)$$
Separate the fraction:
$$f(z) = \frac{x^2+y^2-a^2}{(x+a)^2+y^2} + i\frac{2ay}{(x+a)^2+y^2}$$
**Answer (f):** 
*   **Real part:** $u = \frac{x^2+y^2-a^2}{(x+a)^2+y^2}$
*   **Imaginary part:** $v = \frac{2ay}{(x+a)^2+y^2}$

---
**Part (g): $f(z) = \left(\frac{-1+i\sqrt{3}}{2}\right)^{3}$**
The term inside the parentheses is one of the complex cube roots of unity (often denoted as $\omega$). Let's convert it to polar form.
$x = -1/2$, $y = \sqrt{3}/2$.
$r = \sqrt{(-1/2)^2 + (\sqrt{3}/2)^2} = \sqrt{1/4 + 3/4} = 1$.
$\theta = \pi - \tan^{-1}(\sqrt{3}/1) = \pi - \pi/3 = 2\pi/3$.
So, $\frac{-1+i\sqrt{3}}{2} = e^{i(2\pi/3)}$.
Now, cube it:
$$\left(e^{i\frac{2\pi}{3}}\right)^3 = e^{i\left(\frac{2\pi}{3} \cdot 3\right)} = e^{i2\pi}$$
By Euler's formula: $e^{i2\pi} = \cos(2\pi) + i\sin(2\pi) = 1 + i(0) = 1$.
**Answer (g):** 
*   **Real part:** $1$
*   **Imaginary part:** $0$

Here are the detailed solutions for the next four questions (Q89 to Q92).

*(Note: Several of these questions from the Feruj Sheet are conceptually or numerically identical to problems covered earlier in the document. Detailed step-by-step solutions are provided again below for completeness).*

### Q89. Problems 1.1 Question 2: Find two complex numbers whose sum is 4 and whose product is 8.

**Solution:**

Let the two unknown complex numbers be denoted as $z_1$ and $z_2$.
According to the problem description, we are given two conditions:
1) $z_1 + z_2 = 4$ (Sum of the roots)
2) $z_1 \cdot z_2 = 8$ (Product of the roots)

In algebra, any two numbers that have a known sum and a known product can be represented as the two roots of a quadratic equation. The standard form of such an equation with variable $z$ is:
$$z^2 - (\text{Sum})z + (\text{Product}) = 0$$

**Step 1: Form the quadratic equation.**
Substitute the given sum and product into the standard equation:
$$z^2 - 4z + 8 = 0$$

**Step 2: Solve the quadratic equation using the quadratic formula.**
The quadratic formula is $z = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
Here, $a = 1$, $b = -4$, and $c = 8$.

$$z = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(8)}}{2(1)}$$
$$z = \frac{4 \pm \sqrt{16 - 32}}{2}$$
$$z = \frac{4 \pm \sqrt{-16}}{2}$$

**Step 3: Simplify the square root of the negative number.**
We know that $\sqrt{-16} = \sqrt{16 \cdot (-1)} = \sqrt{16}\sqrt{-1} = 4i$.
Substitute this back into the equation:
$$z = \frac{4 \pm 4i}{2}$$
$$z = 2 \pm 2i$$

**Answer:** The two complex numbers are **$2 + 2i$** and **$2 - 2i$**.

***

### Q90. Problems 1.1 Question 3: Prove that $z=re^{i\theta}$, if $z=x+iy$.

**Solution:**

This question asks us to derive the exponential (polar) form of a complex number from its Cartesian representation.

**Step 1: Represent Cartesian coordinates in terms of polar coordinates.**
If we plot the complex number $z = x + iy$ as a point $P(x,y)$ on the 2D Cartesian plane (the Argand diagram):
*   Let $r$ be the distance from the origin to point $P$. By the Pythagorean theorem, $r = \sqrt{x^2 + y^2}$.
*   Let $\theta$ be the angle that the line segment from the origin to $P$ makes with the positive x-axis.

Using basic right-triangle trigonometry, we can relate $(x,y)$ to $(r,\theta)$:
*   $\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{x}{r} \implies x = r\cos\theta$
*   $\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{y}{r} \implies y = r\sin\theta$

**Step 2: Substitute into the complex number expression.**
Start with the Cartesian form:
$$z = x + iy$$
Substitute $x$ and $y$ with their polar equivalents:
$$z = (r\cos\theta) + i(r\sin\theta)$$

**Step 3: Factor out the common modulus $r$.**
$$z = r(\cos\theta + i\sin\theta)$$

**Step 4: Apply Euler's Formula.**
Euler's formula states that for any real angle $\theta$:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

Substitute this exponential term into our equation for $z$:
$$z = r(e^{i\theta})$$
$$z = re^{i\theta}$$

**(Proved)**

***

### Q91. Problems 1.1 Question 4: Prove that (i) $-\vert{}z\vert{}\le Re~z\le\vert{}z\vert{}$ (ii) $-\vert{}z\vert{}\le Im~z\le\vert{}z\vert{}$

**Solution:**

We need to prove that the real and imaginary parts of any complex number are bounded by the positive and negative values of its modulus.

Let the complex number be defined as $z = x + iy$, where $x$ and $y$ are real numbers.
*   The real part is $Re(z) = x$.
*   The imaginary part is $Im(z) = y$.
*   The modulus is $|z| = \sqrt{x^2 + y^2}$.

**Part (i): Prove $-|z| \le Re(z) \le |z|$**
1.  Since $y$ is a real number, its square is always non-negative: $y^2 \ge 0$.
2.  Therefore, adding $x^2$ to both sides, we get: $x^2 \le x^2 + y^2$.
3.  Because both sides are non-negative, we can take the principal square root without changing the inequality:
    $$\sqrt{x^2} \le \sqrt{x^2 + y^2}$$
4.  By definition, $\sqrt{x^2}$ is the absolute value of $x$, denoted $|x|$, and $\sqrt{x^2 + y^2}$ is $|z|$.
    $$|x| \le |z|$$
5.  A fundamental property of absolute values states that $|A| \le B$ is equivalent to $-B \le A \le B$. Applying this property:
    $$-|z| \le x \le |z|$$
6.  Substitute $x = Re(z)$:
    $$-|z| \le Re(z) \le |z|$$
    **(Proved)**

**Part (ii): Prove $-|z| \le Im(z) \le |z|$**
1.  Since $x$ is a real number, its square is always non-negative: $x^2 \ge 0$.
2.  Therefore, adding $y^2$ to both sides, we get: $y^2 \le x^2 + y^2$.
3.  Taking the square root of both sides:
    $$\sqrt{y^2} \le \sqrt{x^2 + y^2}$$
4.  This simplifies to:
    $$|y| \le |z|$$
5.  Applying the absolute value inequality property:
    $$-|z| \le y \le |z|$$
6.  Substitute $y = Im(z)$:
    $$-|z| \le Im(z) \le |z|$$
    **(Proved)**

***

### Q92. Problems 1.1 Question 5: (i) If $z=x+iy$, evaluate $\vert{}e^{iz}\vert{}$. (ii) If $z=x+iy$, evaluate $\vert{}e^{z}\vert{}$ (iii) If $z=6e^{\pi\frac{1}{3}}$ , evaluate $\vert{}e^{iz}\vert{}$ .

**Solution:**

**Part (i): Evaluate $|e^{iz}|$**
1.  Substitute $z = x + iy$ into the exponent $iz$:
    $$iz = i(x + iy) = ix + i^2y = ix - y = -y + ix$$
2.  Apply this to the exponential function:
    $$e^{iz} = e^{-y + ix}$$
3.  Use the rule of exponents $e^{a+b} = e^a \cdot e^b$:
    $$e^{iz} = e^{-y} \cdot e^{ix}$$
4.  Take the modulus. The modulus of a product is the product of moduli:
    $$|e^{iz}| = |e^{-y}| \cdot |e^{ix}|$$
5.  Since $y$ is real, $-y$ is real, making $e^{-y}$ a positive real number. Thus, $|e^{-y}| = e^{-y}$.
6.  By Euler's formula, $|e^{ix}| = |\cos x + i\sin x| = \sqrt{\cos^2x+\sin^2x} = 1$.
    $$|e^{iz}| = e^{-y} \cdot 1 = e^{-y}$$
**Answer (i): $e^{-y}$**

---

**Part (ii): Evaluate $|e^z|$**
1.  Substitute $z = x + iy$ directly:
    $$e^z = e^{x + iy} = e^x \cdot e^{iy}$$
2.  Take the modulus of the product:
    $$|e^z| = |e^x| \cdot |e^{iy}|$$
3.  Since $x$ is real, $e^x$ is a positive real number, so $|e^x| = e^x$.
4.  By Euler's formula, $|e^{iy}| = \sqrt{\cos^2y+\sin^2y} = 1$.
    $$|e^z| = e^x \cdot 1 = e^x$$
**Answer (ii): $e^x$**

---

**Part (iii): If $z = 6e^{i\frac{\pi}{3}}$, evaluate $|e^{iz}|$**
*(Note: There is a typo in the prompt's source text "$e^{\pi\frac{1}{3}}$". It strictly requires the imaginary unit "$i$" in the exponent to represent an angle, so $6e^{i\pi/3}$ is used. This is numerically identical to Q17 and Q48).*
1.  First, convert $z$ into Cartesian coordinates to find its imaginary part ($y$), because we know from Part (i) that $|e^{iz}| = e^{-y}$.
2.  Using Euler's formula on $z$:
    $$z = 6\left(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}\right)$$
3.  Substitute standard trigonometric values ($\cos 60^\circ = 1/2$, $\sin 60^\circ = \sqrt{3}/2$):
    $$z = 6\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 3 + 3\sqrt{3}i$$
4.  Identify the imaginary part: $y = 3\sqrt{3}$.
5.  Substitute $y$ into our formula from Part (i):
    $$|e^{iz}| = e^{-y} = e^{-3\sqrt{3}}$$
**Answer (iii): $e^{-3\sqrt{3}}$**

Here are the detailed solutions for the next four questions (Q93 to Q96).

### Q93. Problems 1.1 Question 6: Prove that (i) $Re\{z\}=\frac{z+\overline{z}}{2}$ (ii) $Im\{z\}=\frac{z-\overline{z}}{2i}$

**Solution:**

We will prove these fundamental relationships between a complex number, its conjugate, and its real and imaginary parts using Cartesian coordinates.

Let the complex number be defined in standard Cartesian form:
$$z = x + iy$$
where $x$ is the real part, $Re\{z\} = x$, and $y$ is the imaginary part, $Im\{z\} = y$.

The complex conjugate of $z$ is obtained by changing the sign of the imaginary part:
$$\overline{z} = x - iy$$

**Part (i): Prove $Re\{z\} = \frac{z+\overline{z}}{2}$**

**Step 1: Evaluate the sum $z + \overline{z}$.**
Add the complex number and its conjugate together:
$$z + \overline{z} = (x + iy) + (x - iy)$$
$$z + \overline{z} = x + x + iy - iy$$
The imaginary terms $+iy$ and $-iy$ cancel each other out:
$$z + \overline{z} = 2x$$

**Step 2: Isolate $x$.**
Divide both sides of the equation by 2:
$$x = \frac{z + \overline{z}}{2}$$

**Step 3: Conclude.**
Since we defined $x$ as the real part of $z$ ($Re\{z\}$):
$$Re\{z\} = \frac{z + \overline{z}}{2}$$
**(Proved)**

---

**Part (ii): Prove $Im\{z\} = \frac{z-\overline{z}}{2i}$**

**Step 1: Evaluate the difference $z - \overline{z}$.**
Subtract the complex conjugate from the original complex number:
$$z - \overline{z} = (x + iy) - (x - iy)$$
Distribute the negative sign:
$$z - \overline{z} = x + iy - x + iy$$
The real terms $+x$ and $-x$ cancel each other out:
$$z - \overline{z} = 2iy$$

**Step 2: Isolate $y$.**
Divide both sides of the equation by $2i$:
$$y = \frac{z - \overline{z}}{2i}$$

**Step 3: Conclude.**
Since we defined $y$ as the imaginary part of $z$ ($Im\{z\}$):
$$Im\{z\} = \frac{z - \overline{z}}{2i}$$
**(Proved)**

***

### Q94. Problems 1.1 Question 7: Prove that $z^{-1}=\frac{\overline{z}}{\vert{}z\vert{}^{2}}$

**Solution:**

We need to prove the formula for the multiplicative inverse of a complex number $z$.

**Step 1: Start with a fundamental property of complex moduli.**
We know from earlier proofs (Q41) that multiplying a complex number by its conjugate yields the square of its modulus:
$$z\overline{z} = |z|^2$$

**Step 2: Divide by $z$.**
Assuming $z \neq 0$ (since the inverse of $0$ is undefined), divide both sides of the equation by $z$:
$$\frac{z\overline{z}}{z} = \frac{|z|^2}{z}$$
$$\overline{z} = \frac{|z|^2}{z}$$

**Step 3: Divide by $|z|^2$.**
Divide both sides of the equation by $|z|^2$ (which is a strictly positive real number since $z \neq 0$):
$$\frac{\overline{z}}{|z|^2} = \frac{1}{z}$$

**Step 4: Rewrite the expression.**
By algebraic definition, $\frac{1}{z}$ is written as $z^{-1}$. Therefore:
$$z^{-1} = \frac{\overline{z}}{|z|^2}$$
**(Proved)**

*(Alternative Cartesian proof: Let $z = x+iy$. Then $z^{-1} = \frac{1}{x+iy}$. To rationalize the denominator, multiply top and bottom by the conjugate $x-iy$. This gives $\frac{x-iy}{(x+iy)(x-iy)} = \frac{x-iy}{x^2+y^2}$. We recognize the numerator as $\overline{z}$ and the denominator as $|z|^2$. Thus, $z^{-1} = \frac{\overline{z}}{|z|^2}$.)*

***

### Q95. Problems 1.1 Question 8: If $w=3iz-z^{2}$ and $z=x+iy$, find $\vert{}w\vert{}^{2}$ in terms of x and y.

**Solution:**

We are given a complex function $w$ in terms of $z$ and need to find the square of its modulus in terms of the real variables $x$ and $y$.

**Method 1: Using Algebraic substitution directly (Cartesian approach)**

**Step 1: Substitute $z = x + iy$ into the equation for $w$.**
$$w = 3i(x + iy) - (x + iy)^2$$

**Step 2: Expand the terms.**
For the first term: $3i(x + iy) = 3ix + 3i^2y = 3ix - 3y = -3y + 3ix$
For the second term: $(x + iy)^2 = x^2 + 2ixy + i^2y^2 = x^2 - y^2 + 2ixy$

Substitute these back into $w$:
$$w = (-3y + 3ix) - (x^2 - y^2 + 2ixy)$$
Distribute the negative sign:
$$w = -3y + 3ix - x^2 + y^2 - 2ixy$$

**Step 3: Group the real and imaginary parts.**
Let $w = u + iv$.
Real part ($u$): $y^2 - x^2 - 3y$
Imaginary part ($v$): $3x - 2xy$
So, $w = (y^2 - x^2 - 3y) + i(3x - 2xy)$.

**Step 4: Calculate $|w|^2$.**
The square of the modulus is the sum of the squares of the real and imaginary parts: $|w|^2 = u^2 + v^2$.
$$|w|^2 = (y^2 - x^2 - 3y)^2 + (3x - 2xy)^2$$
*(While technically correct, expanding this binomial and trinomial leads to a very long polynomial. Let's use a more elegant method utilizing complex conjugate properties).*

---

**Method 2: Using Conjugate Properties ($|w|^2 = w\overline{w}$)**

This method is often cleaner algebraically for complex polynomials.

**Step 1: Write $w$ and factor it.**
$$w = 3iz - z^2$$
$$w = z(3i - z)$$

**Step 2: Apply the modulus property $|AB|^2 = |A|^2|B|^2$.**
$$|w|^2 = |z|^2 \cdot |3i - z|^2$$

**Step 3: Evaluate the individual moduli in terms of $x$ and $y$.**
*   **Evaluate $|z|^2$:**
    Since $z = x + iy$, we have:
    $$|z|^2 = x^2 + y^2$$

*   **Evaluate $|3i - z|^2$:**
    Substitute $z = x + iy$ into the expression:
    $$3i - z = 3i - (x + iy) = -x + i(3 - y)$$
    The modulus squared of this new complex number is the sum of the squares of its real and imaginary parts:
    $$|3i - z|^2 = (-x)^2 + (3 - y)^2$$
    $$|3i - z|^2 = x^2 + (9 - 6y + y^2)$$
    $$|3i - z|^2 = x^2 + y^2 - 6y + 9$$

**Step 4: Multiply the results together.**
$$|w|^2 = (x^2 + y^2) \cdot (x^2 + y^2 - 6y + 9)$$

This is a much cleaner and more factored final answer than the full expansion from Method 1. (If expanded fully, it would be $x^4 + 2x^2y^2 + y^4 - 6x^2y - 6y^3 + 9x^2 + 9y^2$).

**Answer:** **$|w|^2 = (x^2 + y^2)(x^2 + y^2 - 6y + 9)$**

***

### Q96. Problems 1.1 Question 9: Prove that on the circle $z=Re^{i\theta}$, $\vert{}e^{iz}\vert{}=e^{-R~\sin~\theta}$

**Solution:**

We need to evaluate the modulus of the complex exponential function $e^{iz}$ specifically for points $z$ that lie on a circle of radius $R$ centered at the origin.

**Step 1: Express the condition $z$ in Cartesian form.**
We are given $z$ in polar form: $z = R e^{i\theta}$.
Using Euler's formula ($e^{i\theta} = \cos\theta + i\sin\theta$), we can convert this to Cartesian coordinates:
$$z = R(\cos\theta + i\sin\theta)$$
$$z = (R\cos\theta) + i(R\sin\theta)$$
Let $z = x + iy$. By direct comparison:
*   $x = R\cos\theta$
*   $y = R\sin\theta$

**Step 2: Recall the formula for $|e^{iz}|$.**
In a previous problem (Q46 Part ii, or Q92 Part i), we proved the general identity that for any complex number $z = x + iy$:
$$|e^{iz}| = e^{-y}$$

*Quick re-derivation:*
$iz = i(x+iy) = ix - y = -y + ix$
$e^{iz} = e^{-y + ix} = e^{-y} \cdot e^{ix}$
$|e^{iz}| = |e^{-y}| \cdot |e^{ix}| = e^{-y} \cdot 1 = e^{-y}$.

**Step 3: Substitute the polar $y$-component into the formula.**
From Step 1, we found that for points on this circle, the imaginary part is $y = R\sin\theta$.
Substitute this into the modulus expression:
$$|e^{iz}| = e^{-y}$$
$$|e^{iz}| = e^{-(R\sin\theta)}$$
$$|e^{iz}| = e^{-R\sin\theta}$$

**(Proved)**

Here are the detailed solutions for the next four questions (Q97 to Q100).

### Q97. Problems 1.1 Question 11: If $z=x+iy$, prove that $\vert{}x\vert{}+\vert{}y\vert{}\le\sqrt{2}\vert{}x+iy\vert{}$.

**Solution:**

We need to prove that the sum of the absolute values of the real and imaginary parts of a complex number is bounded by $\sqrt{2}$ times its modulus.

**Step 1: Understand the components.**
Let $z = x + iy$.
*   The modulus is $|z| = \sqrt{x^2 + y^2}$.
*   We need to prove: $|x| + |y| \le \sqrt{2} \sqrt{x^2 + y^2}$.

**Step 2: Use algebraic manipulation (Squaring).**
Since both sides of the target inequality ($|x| + |y|$ and $\sqrt{2}|z|$) are strictly non-negative real numbers, squaring both sides will preserve the direction of the inequality. 
Let's analyze the square of the left-hand side (LHS):
$$(\text{LHS})^2 = (|x| + |y|)^2$$
Expand the binomial:
$$(\text{LHS})^2 = |x|^2 + 2|x||y| + |y|^2$$
Since the square of an absolute value is just the square of the number ($|a|^2 = a^2$):
$$(\text{LHS})^2 = x^2 + 2|xy| + y^2$$

Now let's analyze the square of the right-hand side (RHS):
$$(\text{RHS})^2 = (\sqrt{2} \sqrt{x^2 + y^2})^2$$
$$(\text{RHS})^2 = 2(x^2 + y^2)$$
$$(\text{RHS})^2 = 2x^2 + 2y^2$$

**Step 3: Compare the squared expressions.**
We want to prove that $(\text{LHS})^2 \le (\text{RHS})^2$.
Substitute the expanded forms:
$$x^2 + 2|xy| + y^2 \le 2x^2 + 2y^2$$

Subtract $(x^2 + y^2)$ from both sides:
$$2|xy| \le x^2 + y^2$$

Subtract $2|xy|$ from both sides to bring everything to one side:
$$0 \le x^2 - 2|xy| + y^2$$

**Step 4: Complete the algebraic proof.**
Recognize that $x^2 = |x|^2$ and $y^2 = |y|^2$. The right side of our inequality forms a perfect binomial square:
$$0 \le |x|^2 - 2|x||y| + |y|^2$$
$$0 \le (|x| - |y|)^2$$

This statement is universally true. The square of any real number (in this case, the difference between two absolute values, $|x| - |y|$) is always greater than or equal to zero. 

Because this foundational statement is true, we can reverse all our logical steps:
1.  $0 \le (|x| - |y|)^2$ (True for all $x,y$)
2.  $2|xy| \le x^2 + y^2$
3.  $x^2 + 2|xy| + y^2 \le 2x^2 + 2y^2$
4.  $(|x| + |y|)^2 \le 2(x^2 + y^2)$
5.  Take the principal square root of both non-negative sides:
    $$|x| + |y| \le \sqrt{2} \sqrt{x^2 + y^2}$$
6.  Substitute $|z| = \sqrt{x^2 + y^2}$:
    $$|x| + |y| \le \sqrt{2} |z|$$
**(Proved)**

***

### Q98. Problems 1.1 Question 13: Express each of the following complex numbers in polar form. (i) $-1+\sqrt{3}i$ (ii) $-2\sqrt{3}-2i$ (iii) $2\sqrt{2}+2\sqrt{2}i$ (iv) $\sqrt{5}-i$

**Solution:**

We will convert each Cartesian complex number $z = x + iy$ into the polar form $z = r(\cos\theta + i\sin\theta)$, where $r = \sqrt{x^2 + y^2}$ and $\theta$ is the principal argument in the range $(-\pi, \pi]$.

**Part (i): $-1 + \sqrt{3}i$**
*   **Modulus ($r$):** $r = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = \sqrt{4} = 2$.
*   **Argument ($\theta$):** The point is in the **second quadrant** ($x<0, y>0$).
    Reference angle $\alpha = \tan^{-1}\left|\frac{\sqrt{3}}{-1}\right| = \tan^{-1}(\sqrt{3}) = \frac{\pi}{3}$.
    Principal argument $\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$.
*   **Polar Form:** **$2\left(\cos\frac{2\pi}{3} + i\sin\frac{2\pi}{3}\right)$**

**Part (ii): $-2\sqrt{3} - 2i$** *(Note: This is numerically identical to Q19).*
*   **Modulus ($r$):** $r = \sqrt{(-2\sqrt{3})^2 + (-2)^2} = \sqrt{12 + 4} = \sqrt{16} = 4$.
*   **Argument ($\theta$):** The point is in the **third quadrant** ($x<0, y<0$).
    Reference angle $\alpha = \tan^{-1}\left|\frac{-2}{-2\sqrt{3}}\right| = \tan^{-1}\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{6}$.
    Principal argument $\theta = -\pi + \frac{\pi}{6} = -\frac{5\pi}{6}$.
*   **Polar Form:** **$4\left(\cos\left(-\frac{5\pi}{6}\right) + i\sin\left(-\frac{5\pi}{6}\right)\right)$**

**Part (iii): $2\sqrt{2} + 2\sqrt{2}i$**
*   **Modulus ($r$):** $r = \sqrt{(2\sqrt{2})^2 + (2\sqrt{2})^2} = \sqrt{8 + 8} = \sqrt{16} = 4$.
*   **Argument ($\theta$):** The point is in the **first quadrant** ($x>0, y>0$).
    $\theta = \tan^{-1}\left(\frac{2\sqrt{2}}{2\sqrt{2}}\right) = \tan^{-1}(1) = \frac{\pi}{4}$.
*   **Polar Form:** **$4\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)$**

**Part (iv): $\sqrt{5} - i$**
*   **Modulus ($r$):** $r = \sqrt{(\sqrt{5})^2 + (-1)^2} = \sqrt{5 + 1} = \sqrt{6}$.
*   **Argument ($\theta$):** The point is in the **fourth quadrant** ($x>0, y<0$).
    $\theta = \tan^{-1}\left(\frac{-1}{\sqrt{5}}\right) = -\tan^{-1}\left(\frac{1}{\sqrt{5}}\right)$.
    Since $1/\sqrt{5}$ is not a standard trigonometric fraction, we leave it in inverse tangent form.
*   **Polar Form:** **$\sqrt{6}\left[\cos\left(-\tan^{-1}\frac{1}{\sqrt{5}}\right) + i\sin\left(-\tan^{-1}\frac{1}{\sqrt{5}}\right)\right]$**

***

### Q99. Problems 1.1 Question 14: Find the roots of the following: (i) $z^{4}=-a^{4}$ (ii) $z^{4}=16$ (iii) $z^{2}-z=1$

**Solution:**

**Part (i): $z^4 = -a^4$** *(Note: This was solved earlier in Q57 Part iii. Repeating briefly here).*
Assume $a > 0$.
1.  Polar form of $-a^4$: $w = a^4 \left( \cos(\pi + 2k\pi) + i\sin(\pi + 2k\pi) \right)$.
2.  De Moivre's Theorem for 4th roots ($k = 0, 1, 2, 3$):
    $$z_k = a \left[ \cos\left(\frac{\pi + 2k\pi}{4}\right) + i\sin\left(\frac{\pi + 2k\pi}{4}\right) \right]$$
3.  The four roots are:
    **$z_0 = a\left(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right)$**
    **$z_1 = a\left(-\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right)$**
    **$z_2 = a\left(-\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}\right)$**
    **$z_3 = a\left(\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}\right)$**

---

**Part (ii): $z^4 = 16$**
1.  Polar form of $16$: $w = 16 \left( \cos(0 + 2k\pi) + i\sin(0 + 2k\pi) \right)$.
2.  De Moivre's Theorem for 4th roots ($k = 0, 1, 2, 3$):
    $$z_k = 16^{\frac{1}{4}} \left[ \cos\left(\frac{2k\pi}{4}\right) + i\sin\left(\frac{2k\pi}{4}\right) \right] = 2 \left[ \cos\left(\frac{k\pi}{2}\right) + i\sin\left(\frac{k\pi}{2}\right) \right]$$
3.  The four roots are separated by $90^\circ$ ($\pi/2$):
    *   $k=0$: **$z_0 = 2(\cos 0 + i\sin 0) = 2$**
    *   $k=1$: **$z_1 = 2(\cos\frac{\pi}{2} + i\sin\frac{\pi}{2}) = 2i$**
    *   $k=2$: **$z_2 = 2(\cos\pi + i\sin\pi) = -2$**
    *   $k=3$: **$z_3 = 2(\cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2}) = -2i$**

---

**Part (iii): $z^2 - z = 1$**
1.  This is a standard quadratic equation. Rearrange to standard form:
    $$z^2 - z - 1 = 0$$
2.  Apply the quadratic formula, where $a=1, b=-1, c=-1$:
    $$z = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
    $$z = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2(1)}$$
    $$z = \frac{1 \pm \sqrt{1 + 4}}{2}$$
    $$z = \frac{1 \pm \sqrt{5}}{2}$$
3.  Because the discriminant is positive ($5 > 0$), this equation has purely real roots (which are a subset of complex numbers).
    **The two roots are $z = \frac{1 + \sqrt{5}}{2}$ and $z = \frac{1 - \sqrt{5}}{2}$.** *(Note: The positive root is the famous Golden Ratio, $\phi$).*

***

### Q100. Problems 1.1 Question 15: Represent graphically the set of values of z for which (a) $\vert{}z\vert{}>\vert{}z-1\vert{}$ (b) $\vert{}z+2\vert{}>1+\vert{}z-2\vert{}$

**Solution:**

We need to interpret these algebraic inequalities geometrically.

**Part (a): $|z| > |z - 1|$**
1.  **Geometric Interpretation:** 
    *   $|z|$ is the distance from point $z$ to the origin $(0,0)$.
    *   $|z - 1|$ is the distance from point $z$ to the fixed point $z_0 = 1$ (or coordinate $(1,0)$).
    *   The inequality states: "The distance from $z$ to the origin is strictly *greater* than the distance from $z$ to the point $(1,0)$."
2.  **Find the boundary line:**
    The boundary occurs where the distances are equal: $|z| = |z - 1|$. 
    The locus of points equidistant from two fixed points is the **perpendicular bisector** of the line segment joining them. The segment joins $(0,0)$ and $(1,0)$. The perpendicular bisector is the vertical line passing exactly halfway between them: $x = 0.5$.
3.  **Algebraic confirmation:**
    Let $z = x + iy$.
    $$\sqrt{x^2 + y^2} > \sqrt{(x-1)^2 + y^2}$$
    Square both sides:
    $$x^2 + y^2 > (x-1)^2 + y^2$$
    $$x^2 > x^2 - 2x + 1$$
    $$0 > -2x + 1$$
    $$2x > 1 \implies x > 0.5$$
4.  **Graphical Representation:** The set of values is the entire **right half-plane** strictly to the right of the vertical line $x = 0.5$. (The line $x=0.5$ itself is drawn as dashed and is not included).

---

**Part (b): $|z + 2| > 1 + |z - 2|$**
1.  **Algebraic setup:**
    Let $z = x + iy$. This inequality is quite complex to interpret purely geometrically at first glance due to the "$+1$". Let's use algebra.
    $$\sqrt{(x+2)^2 + y^2} > 1 + \sqrt{(x-2)^2 + y^2}$$
2.  **Square both sides to eliminate the outer square roots:**
    $$(x+2)^2 + y^2 > 1 + 2\sqrt{(x-2)^2 + y^2} + [(x-2)^2 + y^2]$$
    $$x^2 + 4x + 4 + y^2 > 1 + 2\sqrt{(x-2)^2 + y^2} + x^2 - 4x + 4 + y^2$$
3.  **Cancel common terms and simplify:**
    $$4x > 1 + 2\sqrt{(x-2)^2 + y^2} - 4x$$
    $$8x - 1 > 2\sqrt{(x-2)^2 + y^2}$$
4.  **Square both sides again** (Note: this is only fully valid if $8x - 1 > 0$, implying $x > 1/8$):
    $$(8x - 1)^2 > 4[(x-2)^2 + y^2]$$
    $$64x^2 - 16x + 1 > 4(x^2 - 4x + 4 + y^2)$$
    $$64x^2 - 16x + 1 > 4x^2 - 16x + 16 + 4y^2$$
5.  **Simplify into standard conic form:**
    $$60x^2 - 4y^2 > 15$$
    Divide by 15:
    $$\frac{60x^2}{15} - \frac{4y^2}{15} > 1$$
    $$4x^2 - \frac{4y^2}{15} > 1$$
    $$\frac{x^2}{(1/2)^2} - \frac{y^2}{(\sqrt{15}/2)^2} > 1$$
6.  **Graphical Representation:**
    The corresponding equality $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ is the standard equation of a **hyperbola** centered at the origin, opening left and right along the x-axis. 
    *   Vertices are at $(\pm 1/2, 0)$.
    *   The inequality "$>$" represents the regions "inside" the cups of the hyperbola (i.e., further away from the origin than the vertices).
    *   However, recall our restriction from Step 4 that $8x - 1 > 0$, so $x > 1/8$. This means we completely discard the left branch of the hyperbola (where $x < -1/2$).
    *   Therefore, the graphical representation is the **open region strictly enclosed by the right-hand branch of the hyperbola** $4x^2 - \frac{4y^2}{15} = 1$.


Here are the detailed solutions for the next four questions (Q101 to Q104).

### Q101. Question: $|z - 1 + 3i| = 2$

*(Note: The source text has a typo using `$j$` instead of `$i$`. In engineering, `$j$` is often used for the imaginary unit. The prompt also has an extraneous `|` at the end. The standard interpretation is the equation of the circle $|z - (1 - 3i)| = 2$. Assuming the task is to describe this geometrically).*

**Solution:**

We need to interpret the algebraic equation $|z - 1 + 3i| = 2$ geometrically in the complex plane.

**Step 1: Understand the standard equation.**
In the complex plane, the distance between any variable point $z$ and a fixed point $z_0$ is given by the modulus of their difference: $|z - z_0|$. 
A circle is defined as the set of all points that are a constant distance (the radius, $r$) from a fixed center point ($z_0$). 
Thus, the standard equation of a circle is:
$$|z - z_0| = r$$

**Step 2: Format the given equation to match the standard form.**
We need to factor out a minus sign inside the absolute value bars so it matches the format $(z - z_0)$.
$$|z - (1 - 3i)| = 2$$

**Step 3: Extract the geometric parameters.**
By comparing our formatted equation to the standard form $|z - z_0| = r$, we can directly read the parameters:
1.  **Radius ($r$):** The constant on the right side of the equation is $2$. So, the radius is $2$.
2.  **Center ($z_0$):** The complex number being subtracted from $z$ is $1 - 3i$. 
    *   In Cartesian coordinates, the real part is $1$ and the imaginary part is $-3$. 
    *   Therefore, the center is the point $(1, -3)$.

**Answer:** The equation represents a **circle** in the complex plane with its center at **$1 - 3i$** (coordinate $(1, -3)$) and a radius of **$2$**.

***

### Q102. Pg 1, Q1(b): Separate real and imaginary parts of the following function. $f(z) = \sqrt{z}$.

**Solution:**

We need to express the complex function $f(z) = \sqrt{z}$ in the form $u(x,y) + iv(x,y)$, where $u$ and $v$ are purely real functions. Let $z = x + iy$.

**Method 1: Using Polar Coordinates (Standard and Easiest Method)**
**Step 1: Express $z$ in polar form.**
Let $z = r e^{i\theta}$, where:
*   $r = \sqrt{x^2 + y^2}$
*   $\theta = \tan^{-1}\left(\frac{y}{x}\right)$ (Principal argument)

**Step 2: Apply the square root function.**
$$f(z) = z^{1/2} = (r e^{i\theta})^{1/2} = r^{1/2} e^{i\theta/2} = \sqrt{r} e^{i\frac{\theta}{2}}$$

**Step 3: Expand using Euler's formula.**
$$f(z) = \sqrt{r} \left( \cos\frac{\theta}{2} + i\sin\frac{\theta}{2} \right)$$
$$f(z) = \sqrt{r}\cos\frac{\theta}{2} + i\sqrt{r}\sin\frac{\theta}{2}$$

**Step 4: State the real and imaginary parts.**
*   **Real part $u(r,\theta)$:** $\sqrt{r}\cos\frac{\theta}{2}$
*   **Imaginary part $v(r,\theta)$:** $\sqrt{r}\sin\frac{\theta}{2}$

---
**Method 2: Using Strict Cartesian Coordinates (Algebraic Method)**
Let $\sqrt{x+iy} = u + iv$. We need to find $u$ and $v$ in terms of $x$ and $y$.
**Step 1: Square both sides.**
$$x + iy = (u + iv)^2$$
$$x + iy = u^2 + 2iuv + i^2v^2$$
$$x + iy = (u^2 - v^2) + i(2uv)$$

**Step 2: Equate real and imaginary parts.**
1) $x = u^2 - v^2$
2) $y = 2uv \implies v = \frac{y}{2u}$

**Step 3: Solve for $u$.**
Substitute $v$ into the first equation:
$$x = u^2 - \left(\frac{y}{2u}\right)^2$$
$$x = u^2 - \frac{y^2}{4u^2}$$
Multiply by $4u^2$:
$$4u^2 x = 4u^4 - y^2$$
$$4u^4 - 4xu^2 - y^2 = 0$$
This is a quadratic equation in terms of $u^2$. Using the quadratic formula:
$$u^2 = \frac{-(-4x) \pm \sqrt{(-4x)^2 - 4(4)(-y^2)}}{2(4)}$$
$$u^2 = \frac{4x \pm \sqrt{16x^2 + 16y^2}}{8}$$
$$u^2 = \frac{4x \pm 4\sqrt{x^2 + y^2}}{8} = \frac{x \pm \sqrt{x^2 + y^2}}{2}$$
Since $u$ must be a real number, $u^2$ must be positive. Since $\sqrt{x^2+y^2} \ge x$, we must take the positive root. Let $r = \sqrt{x^2+y^2}$.
$$u^2 = \frac{r + x}{2} \implies u = \pm\sqrt{\frac{r + x}{2}}$$

**Step 4: Solve for $v$.**
Using $v^2 = u^2 - x$:
$$v^2 = \frac{r + x}{2} - x = \frac{r + x - 2x}{2} = \frac{r - x}{2} \implies v = \pm\sqrt{\frac{r - x}{2}}$$
The signs of $u$ and $v$ must match the sign of $y$ (since $2uv = y$). Assuming the principal branch where the real part $u \ge 0$:

**Answer:** 
Let $r = \sqrt{x^2+y^2}$.
*   **Real part $u(x,y) = \sqrt{\frac{r + x}{2}}$**
*   **Imaginary part $v(x,y) = \text{sgn}(y)\sqrt{\frac{r - x}{2}}$** (where sgn is the sign function).

***

### Q103. Pg 4, Q1(a): Separate the real and imaginary parts of $f(z) = \sqrt{1-z}$.

**Solution:**

We need to express $f(z) = \sqrt{1-z}$ in the form $u + iv$.

Let $z = x + iy$.
Substitute this into the function:
$$f(z) = \sqrt{1 - (x + iy)}$$
$$f(z) = \sqrt{(1 - x) - iy}$$

To handle the square root, we will use the same algebraic technique as Q102 (Method 2).
Let the square root equal a new complex number $u + iv$:
$$\sqrt{(1 - x) - iy} = u + iv$$

**Step 1: Square both sides.**
$$(1 - x) - iy = (u + iv)^2$$
$$(1 - x) - iy = u^2 - v^2 + i(2uv)$$

**Step 2: Equate real and imaginary parts.**
We get a system of two equations:
1) $u^2 - v^2 = 1 - x$
2) $2uv = -y$

**Step 3: Solve for $u^2$ and $v^2$ using the modulus identity.**
We know an algebraic identity: $(u^2 + v^2)^2 = (u^2 - v^2)^2 + (2uv)^2$.
Let's substitute our equations into this identity:
$$(u^2 + v^2)^2 = (1 - x)^2 + (-y)^2$$
$$(u^2 + v^2)^2 = (1 - x)^2 + y^2$$
Taking the principal positive square root (since $u^2+v^2$ must be positive):
$$u^2 + v^2 = \sqrt{(1 - x)^2 + y^2}$$

Let's define $R = \sqrt{(1 - x)^2 + y^2}$ to simplify notation. So, $u^2 + v^2 = R$.

**Step 4: Solve for $u$ and $v$.**
We now have a much simpler system:
A) $u^2 + v^2 = R$
B) $u^2 - v^2 = 1 - x$

Add equation (A) and equation (B):
$$2u^2 = R + (1 - x)$$
$$u^2 = \frac{R + 1 - x}{2} \implies u = \pm\sqrt{\frac{R + 1 - x}{2}}$$

Subtract equation (B) from equation (A):
$$2v^2 = R - (1 - x)$$
$$v^2 = \frac{R - 1 + x}{2} \implies v = \pm\sqrt{\frac{R - 1 + x}{2}}$$

**Step 5: Determine signs.**
From Equation 2 ($2uv = -y$), we know the product of $u$ and $v$ has the opposite sign of $y$. If we take the principal root where the real part $u > 0$, the sign of $v$ must be opposite to the sign of $y$.

**Answer:**
Let $R = \sqrt{(1-x)^2 + y^2}$.
*   **Real part: $u(x,y) = \sqrt{\frac{R + 1 - x}{2}}$**
*   **Imaginary part: $v(x,y) = -\text{sgn}(y) \sqrt{\frac{R - 1 + x}{2}}$**

***

### Q104. Pg 6, Q1(a): Separate the real and imaginary part of $f(z) = \sin 2z$.

**Solution:**

We need to express $f(z) = \sin(2z)$ in the form $u(x,y) + iv(x,y)$, where $u$ and $v$ are real functions.

**Step 1: Substitute $z = x + iy$ into the function.**
$$f(z) = \sin(2(x + iy))$$
$$f(z) = \sin(2x + i2y)$$

**Step 2: Use the trigonometric compound angle formula.**
The formula for the sine of a sum is:
$$\sin(A + B) = \sin A\cos B + \cos A\sin B$$
Let $A = 2x$ and $B = i2y$:
$$f(z) = \sin(2x)\cos(i2y) + \cos(2x)\sin(i2y)$$

**Step 3: Convert complex trigonometric functions to hyperbolic functions.**
There are fundamental identities relating circular trigonometric functions of imaginary arguments to real hyperbolic functions:
*   $\cos(i\theta) = \cosh(\theta)$
*   $\sin(i\theta) = i\sinh(\theta)$

Apply these identities to our expression (where $\theta = 2y$):
*   $\cos(i2y) = \cosh(2y)$
*   $\sin(i2y) = i\sinh(2y)$

Substitute these back into the function:
$$f(z) = \sin(2x)[\cosh(2y)] + \cos(2x)[i\sinh(2y)]$$

**Step 4: Group the real and imaginary parts.**
Rearrange the terms to clearly show the $u + iv$ format:
$$f(z) = [\sin(2x)\cosh(2y)] + i[\cos(2x)\sinh(2y)]$$

Both $\sin(2x)\cosh(2y)$ and $\cos(2x)\sinh(2y)$ are entirely real-valued functions for any real numbers $x$ and $y$. Therefore, the separation is complete.

**Answer:**
*   **Real part: $u(x,y) = \sin(2x)\cosh(2y)$**
*   **Imaginary part: $v(x,y) = \cos(2x)\sinh(2y)$**

Here are the detailed solutions for the next four questions (Q105 to Q108).

### Q105. Pg 13, CT-03, 3.(a): Separate the real and imaginary parts of $z^x$, if $z = x+iy$

**Solution:**

We need to express the complex power function $f(z) = z^x$ in the form $u(x,y) + iv(x,y)$, where $z = x + iy$ and $x$ is real.

**Step 1: Express $z$ in polar form.**
Let $z = r e^{i\theta}$, where:
*   $r = |z| = \sqrt{x^2 + y^2}$
*   $\theta = \arg(z) = \tan^{-1}\left(\frac{y}{x}\right)$

**Step 2: Substitute polar form into the function.**
$$z^x = (r e^{i\theta})^x$$
Using exponent rules $(ab)^x = a^x b^x$:
$$z^x = r^x \cdot (e^{i\theta})^x$$
$$z^x = r^x \cdot e^{ix\theta}$$

**Step 3: Expand the exponential term using Euler's formula.**
Euler's formula states that $e^{i\phi} = \cos\phi + i\sin\phi$. Here, $\phi = x\theta$.
$$e^{ix\theta} = \cos(x\theta) + i\sin(x\theta)$$

Substitute this back into the expression:
$$z^x = r^x [\cos(x\theta) + i\sin(x\theta)]$$
$$z^x = r^x \cos(x\theta) + i \cdot r^x \sin(x\theta)$$

**Step 4: Express the result fully in terms of $x$ and $y$.**
Substitute $r = \sqrt{x^2 + y^2} = (x^2 + y^2)^{1/2}$ and $\theta = \tan^{-1}(y/x)$.
Therefore, $r^x = \left((x^2 + y^2)^{1/2}\right)^x = (x^2 + y^2)^{x/2}$.

$$z^x = (x^2 + y^2)^{\frac{x}{2}} \cos\left(x \tan^{-1}\left(\frac{y}{x}\right)\right) + i (x^2 + y^2)^{\frac{x}{2}} \sin\left(x \tan^{-1}\left(\frac{y}{x}\right)\right)$$

**Answer:**
Let $r = \sqrt{x^2+y^2}$ and $\theta = \tan^{-1}(y/x)$.
*   **Real part: $u(x,y) = r^x \cos(x\theta) = (x^2 + y^2)^{\frac{x}{2}} \cos\left(x \tan^{-1}\frac{y}{x}\right)$**
*   **Imaginary part: $v(x,y) = r^x \sin(x\theta) = (x^2 + y^2)^{\frac{x}{2}} \sin\left(x \tan^{-1}\frac{y}{x}\right)$**

***

### Q106. Pg 14, CT-01, 3.(a): Separate the real and imaginary parts of $\frac{1}{1+z}$

**Solution:**

We need to express the rational complex function $f(z) = \frac{1}{1+z}$ in the form $u(x,y) + iv(x,y)$.

**Step 1: Substitute $z = x + iy$ into the function.**
$$f(z) = \frac{1}{1 + (x + iy)}$$
Group the real parts together in the denominator:
$$f(z) = \frac{1}{(1 + x) + iy}$$

**Step 2: Rationalize the denominator.**
To remove the imaginary unit $i$ from the denominator, we multiply both the numerator and the denominator by the complex conjugate of the denominator, which is $(1 + x) - iy$.
$$f(z) = \frac{1}{(1 + x) + iy} \cdot \frac{(1 + x) - iy}{(1 + x) - iy}$$

**Step 3: Perform the multiplication.**
*   **Numerator:** $1 \cdot [(1 + x) - iy] = (1 + x) - iy$
*   **Denominator:** This is a difference of squares, $(A + iB)(A - iB) = A^2 + B^2$.
    Here, $A = (1+x)$ and $B = y$.
    Denominator $= (1 + x)^2 + y^2$

Put it all together:
$$f(z) = \frac{(1 + x) - iy}{(1 + x)^2 + y^2}$$

**Step 4: Separate the real and imaginary parts.**
Split the fraction into two distinct terms over the common denominator:
$$f(z) = \frac{1 + x}{(1 + x)^2 + y^2} - i \frac{y}{(1 + x)^2 + y^2}$$

Rewrite slightly to explicitly show the $u + iv$ format:
$$f(z) = \left[ \frac{1 + x}{(1 + x)^2 + y^2} \right] + i \left[ \frac{-y}{(1 + x)^2 + y^2} \right]$$

**Answer:**
*   **Real part: $u(x,y) = \frac{1 + x}{(1 + x)^2 + y^2}$**
*   **Imaginary part: $v(x,y) = \frac{-y}{(1 + x)^2 + y^2}$**

***

### Q107. Pg 18, CT-I, 1.(b): Separate each of the following into real and imaginary parts, i.e., find $u(x, y)$ and $v(x, y)$ $f(z) = z + \frac{1}{z}$

**Solution:**

We need to express $f(z) = z + \frac{1}{z}$ in the standard form $u(x,y) + iv(x,y)$. 
*(Note: This function is famous in fluid dynamics, known as the Joukowsky transform).*

**Step 1: Substitute $z = x + iy$ into the function.**
$$f(z) = (x + iy) + \frac{1}{x + iy}$$

**Step 2: Rationalize the fraction term.**
We need to remove $i$ from the denominator of the second term. Multiply the numerator and denominator by the complex conjugate $x - iy$.
$$\frac{1}{x + iy} = \frac{1}{x + iy} \cdot \frac{x - iy}{x - iy}$$
$$\frac{1}{x + iy} = \frac{x - iy}{x^2 - (iy)^2}$$
Since $i^2 = -1$:
$$\frac{1}{x + iy} = \frac{x - iy}{x^2 + y^2}$$

Separate this into real and imaginary parts:
$$\frac{1}{x + iy} = \frac{x}{x^2 + y^2} - i \frac{y}{x^2 + y^2}$$

**Step 3: Combine with the original $z$ term.**
Substitute the rationalized fraction back into the full function equation:
$$f(z) = (x + iy) + \left( \frac{x}{x^2 + y^2} - i \frac{y}{x^2 + y^2} \right)$$

**Step 4: Group the real parts and imaginary parts.**
Group the terms without $i$ (real) and the terms with $i$ (imaginary):
$$f(z) = \left( x + \frac{x}{x^2 + y^2} \right) + i \left( y - \frac{y}{x^2 + y^2} \right)$$

We can factor out $x$ and $y$ to make it look cleaner:
$$f(z) = x\left( 1 + \frac{1}{x^2 + y^2} \right) + iy\left( 1 - \frac{1}{x^2 + y^2} \right)$$

**Answer:**
*   **Real part: $u(x,y) = x + \frac{x}{x^2 + y^2}$**  *(or $x\left( 1 + \frac{1}{x^2 + y^2} \right)$)*
*   **Imaginary part: $v(x,y) = y - \frac{y}{x^2 + y^2}$** *(or $y\left( 1 - \frac{1}{x^2 + y^2} \right)$)*

*(Alternatively, in polar coordinates $z = re^{i\theta}$, $f(z) = (r+1/r)\cos\theta + i(r-1/r)\sin\theta$.)*

***

### Q108. Pg 6, Q1(c): Is the function $f(z) = \begin{cases} \frac{z^2+2z}{z-i}; & z \neq i \\ 3+2i; & z=i \end{cases}$ Continuous at $z = i$? If it is not true, redefine the function to be continuous at $z = i$.

**Solution:**

A complex function $f(z)$ is continuous at a point $z = z_0$ if and only if three conditions are met:
1.  $f(z_0)$ is defined.
2.  $\lim_{z \to z_0} f(z)$ exists.
3.  $\lim_{z \to z_0} f(z) = f(z_0)$.

Let's test these conditions at the point $z_0 = i$.

**Step 1: Check if $f(i)$ is defined.**
From the piecewise definition, when $z = i$, the function value is given as:
$$f(i) = 3 + 2i$$
So, the function is defined at $z=i$.

**Step 2: Evaluate the limit as $z \to i$.**
We must evaluate the limit of the function for $z \neq i$.
$$\lim_{z \to i} f(z) = \lim_{z \to i} \frac{z^2 + 2z}{z - i}$$

Let's try direct substitution of $z=i$:
Numerator: $i^2 + 2i = -1 + 2i$
Denominator: $i - i = 0$
Since we get $\frac{-1 + 2i}{0}$, the limit approaches **infinity** (or more accurately, the limit does not exist as a finite complex number).

*(Note: There is highly likely a typo in the exam paper's question. A standard calculus/complex analysis limit problem of this type is usually designed to be an indeterminate form $0/0$ that can be factored. For example, if the numerator was $z^2+1$, it factors to $(z+i)(z-i)$, which cancels the denominator. Or perhaps the numerator was meant to be $z^2 - 2iz - 1 = (z-i)^2$. However, we must solve the problem exactly as written).*

Because the denominator goes to 0 while the numerator goes to a non-zero constant ($-1+2i$), the magnitude of the fraction grows without bound.
$$\lim_{z \to i} |f(z)| = \infty$$

**Step 3: Compare the limit to the function value.**
Since the limit does not exist as a finite number, it cannot possibly equal the defined finite value $f(i) = 3+2i$.
Therefore, the function is **not continuous** at $z = i$.

**Step 4: Redefine the function to be continuous (if possible).**
To make a function continuous at a removable singularity, we define $f(z_0)$ to be exactly equal to $\lim_{z \to z_0} f(z)$.
However, because the limit evaluates to infinity, $z=i$ is a **pole**, not a removable singularity. It is mathematically impossible to redefine the function with a finite complex value to make it continuous at a pole.

**Conclusion/Answer:**
*   Is the function continuous at $z = i$? **No.** The limit as $z \to i$ goes to infinity.
*   Redefine the function: **It cannot be redefined** to be continuous at $z=i$ because the singularity is a pole (the limit does not exist finitely), unless we are working in the extended complex plane where we can define $f(i) = \infty$. 

*(Assuming the likely typo where the numerator was meant to be $z^2+1$: $\lim_{z\to i} \frac{z^2+1}{z-i} = \lim \frac{(z+i)(z-i)}{z-i} = \lim(z+i) = 2i$. Then we would redefine $f(i) = 2i$.)*


Here are the detailed solutions for the next four questions (Q109 to Q112).

### Q109. Pg 13, CT-03, 3.(b): Evaluate $\lim_{z\to i} \frac{d}{dz}\left\{(z-\pi i)^2 \frac{e^z}{(z^2+\pi^2)^2}\right\}$

**Solution:**

We need to evaluate the limit of the derivative of a complex function.
Let $F(z) = (z-\pi i)^2 \frac{e^z}{(z^2+\pi^2)^2}$.

**Step 1: Simplify the expression inside the derivative.**
The term $(z^2 + \pi^2)$ is a difference of squares in the complex plane, because $\pi^2 = -(-\pi^2) = -(i\pi)^2$.
Thus, $z^2 + \pi^2 = (z + i\pi)(z - i\pi)$.

Substitute this back into the denominator of $F(z)$:
$$(z^2 + \pi^2)^2 = [(z + i\pi)(z - i\pi)]^2 = (z + i\pi)^2(z - i\pi)^2$$

Now, substitute this expanded denominator back into $F(z)$:
$$F(z) = (z - \pi i)^2 \frac{e^z}{(z + i\pi)^2(z - i\pi)^2}$$

Cancel the common term $(z - \pi i)^2$ from the numerator and denominator:
$$F(z) = \frac{e^z}{(z + i\pi)^2}$$

**Step 2: Find the derivative $\frac{d}{dz} F(z)$.**
We need to differentiate $F(z) = \frac{e^z}{(z + i\pi)^2}$. We will use the quotient rule: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.
*   $u = e^z \implies u' = e^z$
*   $v = (z + i\pi)^2 \implies v' = 2(z + i\pi) \cdot (1) = 2(z + i\pi)$

Apply the quotient rule:
$$\frac{d}{dz}F(z) = \frac{e^z(z + i\pi)^2 - e^z[2(z + i\pi)]}{[(z + i\pi)^2]^2}$$
$$\frac{d}{dz}F(z) = \frac{e^z(z + i\pi)^2 - 2e^z(z + i\pi)}{(z + i\pi)^4}$$

Factor out the common terms $e^z(z + i\pi)$ from the numerator:
$$\frac{d}{dz}F(z) = \frac{e^z(z + i\pi) [(z + i\pi) - 2]}{(z + i\pi)^4}$$

Cancel one $(z + i\pi)$ from the numerator and denominator:
$$\frac{d}{dz}F(z) = \frac{e^z(z + i\pi - 2)}{(z + i\pi)^3}$$

**Step 3: Evaluate the limit as $z \to i$.**
We want to find $\lim_{z \to i} \frac{d}{dz} F(z)$.
Substitute the derivative expression:
$$\lim_{z \to i} \frac{e^z(z + i\pi - 2)}{(z + i\pi)^3}$$

Since $z=i$ does not cause the denominator to be zero (the denominator only vanishes at $z = -i\pi$), we can evaluate the limit by direct substitution:
$$= \frac{e^i(i + i\pi - 2)}{(i + i\pi)^3}$$
$$= \frac{e^i(i(1+\pi) - 2)}{[i(1+\pi)]^3}$$

Evaluate the denominator using $i^3 = -i$:
$$[i(1+\pi)]^3 = i^3(1+\pi)^3 = -i(1+\pi)^3$$

Substitute this back:
$$= \frac{e^i(i(1+\pi) - 2)}{-i(1+\pi)^3}$$

Multiply numerator and denominator by $i$ to remove $-i$ from the denominator:
$$= \frac{i \cdot e^i(i(1+\pi) - 2)}{-i^2(1+\pi)^3}$$
$$= \frac{e^i(i^2(1+\pi) - 2i)}{1(1+\pi)^3}$$
$$= \frac{e^i(-(1+\pi) - 2i)}{(1+\pi)^3}$$

Factor out the negative sign:
$$= \frac{-e^i((1+\pi) + 2i)}{(1+\pi)^3}$$

**Answer:** 
The limit evaluates to **$\frac{-e^i((1+\pi) + 2i)}{(1+\pi)^3}$**. 
*(This can also be written using Euler's formula $e^i = \cos 1 + i\sin 1$, but exponential form is generally preferred here).*

***

### Q110. Pg 14, CT-01, 3.(b): Evaluate $\lim_{z\to 2i} \left\{(z-2i) \frac{z^2-2z}{(z+1)^2(z^2+4)}\right\}$

**Solution:**

We need to evaluate the limit of a complex rational expression.
Let $F(z) = (z-2i) \frac{z^2-2z}{(z+1)^2(z^2+4)}$.

**Step 1: Direct substitution check.**
If we directly substitute $z = 2i$:
Numerator: $(2i - 2i) \cdot \dots = 0 \cdot \dots = 0$
Denominator: $(2i+1)^2 ((2i)^2 + 4) = (2i+1)^2 (-4 + 4) = (2i+1)^2 \cdot 0 = 0$
We get an indeterminate form $0/0$. We must simplify the expression.

**Step 2: Factor the denominator.**
Look at the term $(z^2 + 4)$. This is a sum of squares, which can be factored over complex numbers using $i^2 = -1$:
$z^2 + 4 = z^2 - (-4) = z^2 - (2i)^2$
Using the difference of squares formula $a^2 - b^2 = (a-b)(a+b)$:
$$z^2 + 4 = (z - 2i)(z + 2i)$$

**Step 3: Substitute the factored form back into the limit expression.**
Substitute this into the denominator of $F(z)$:
$$F(z) = (z-2i) \frac{z^2-2z}{(z+1)^2 (z - 2i)(z + 2i)}$$

**Step 4: Simplify the expression.**
Cancel the common factor $(z - 2i)$ from the numerator and denominator. (This is valid because in a limit as $z \to 2i$, $z$ approaches but is not exactly equal to $2i$, so we are not dividing by exactly zero).
$$F(z) = \frac{z^2 - 2z}{(z+1)^2 (z + 2i)}$$
We can also factor $z$ from the numerator:
$$F(z) = \frac{z(z - 2)}{(z+1)^2 (z + 2i)}$$

**Step 5: Evaluate the limit by direct substitution.**
Now evaluate the limit of the simplified expression as $z \to 2i$:
$$\lim_{z\to 2i} \frac{z(z - 2)}{(z+1)^2 (z + 2i)}$$
Substitute $z = 2i$:
$$= \frac{(2i)(2i - 2)}{(2i + 1)^2 (2i + 2i)}$$
$$= \frac{2i(2i - 2)}{(2i + 1)^2 (4i)}$$

Cancel $2i$ from the top and $4i$ from the bottom:
$$= \frac{2i - 2}{2 (2i + 1)^2}$$
Factor out 2 from the numerator:
$$= \frac{2(i - 1)}{2 (2i + 1)^2}$$
$$= \frac{i - 1}{(1 + 2i)^2}$$

**Step 6: Expand and simplify the result.**
Expand the denominator $(1 + 2i)^2$:
$$(1 + 2i)^2 = 1^2 + 2(1)(2i) + (2i)^2 = 1 + 4i + 4i^2 = 1 + 4i - 4 = -3 + 4i$$

So the result is:
$$= \frac{i - 1}{-3 + 4i}$$

**Step 7: Rationalize the denominator.**
Multiply numerator and denominator by the complex conjugate of the denominator, $-3 - 4i$:
$$= \frac{(i - 1)(-3 - 4i)}{(-3 + 4i)(-3 - 4i)}$$
Numerator: $(i)(-3) + (i)(-4i) + (-1)(-3) + (-1)(-4i) = -3i - 4i^2 + 3 + 4i = -3i + 4 + 3 + 4i = 7 + i$
Denominator: $(-3)^2 - (4i)^2 = 9 - 16(-1) = 9 + 16 = 25$

Result:
$$= \frac{7 + i}{25} = \frac{7}{25} + i\frac{1}{25}$$

**Answer:** The limit evaluates to **$\frac{7}{25} + \frac{1}{25}i$**.

***

### Q111. Pg 18, CT-I, 3.(b): $\lim_{z\to i/3} \frac{d}{dz} \left\{(z-i/3)^2 \cdot \frac{z}{(3z-i)^2(z-3i)^2}\right\}$

**Solution:**

We need to evaluate the limit of the derivative of a complex function.
Let $F(z) = (z-i/3)^2 \cdot \frac{z}{(3z-i)^2(z-3i)^2}$.

**Step 1: Simplify the expression inside the derivative.**
Look closely at the term $(3z - i)^2$ in the denominator.
We can factor a $3$ out of the base expression:
$(3z - i) = 3(z - i/3)$
Therefore, squaring it gives:
$(3z - i)^2 = [3(z - i/3)]^2 = 9(z - i/3)^2$

Substitute this back into $F(z)$:
$$F(z) = (z - i/3)^2 \cdot \frac{z}{9(z - i/3)^2 (z - 3i)^2}$$

Cancel the common term $(z - i/3)^2$ from the numerator and denominator:
$$F(z) = \frac{z}{9(z - 3i)^2}$$
To make differentiation easier, bring the 9 out:
$$F(z) = \frac{1}{9} \frac{z}{(z - 3i)^2}$$

**Step 2: Find the derivative $\frac{d}{dz} F(z)$.**
We will differentiate $\frac{1}{9} \frac{z}{(z - 3i)^2}$ using the quotient rule: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$.
*   The constant $1/9$ stays in front.
*   $u = z \implies u' = 1$
*   $v = (z - 3i)^2 \implies v' = 2(z - 3i) \cdot (1) = 2(z - 3i)$

Apply the quotient rule:
$$\frac{d}{dz}F(z) = \frac{1}{9} \left[ \frac{(1)(z - 3i)^2 - z[2(z - 3i)]}{[(z - 3i)^2]^2} \right]$$
$$\frac{d}{dz}F(z) = \frac{1}{9} \left[ \frac{(z - 3i)^2 - 2z(z - 3i)}{(z - 3i)^4} \right]$$

Factor out the common term $(z - 3i)$ from the numerator:
$$\frac{d}{dz}F(z) = \frac{1}{9} \left[ \frac{(z - 3i) [ (z - 3i) - 2z ]}{(z - 3i)^4} \right]$$

Cancel one $(z - 3i)$ term from the top and bottom:
$$\frac{d}{dz}F(z) = \frac{1}{9} \frac{z - 3i - 2z}{(z - 3i)^3}$$
$$\frac{d}{dz}F(z) = \frac{1}{9} \frac{-z - 3i}{(z - 3i)^3}$$
Factor out the negative sign:
$$\frac{d}{dz}F(z) = -\frac{1}{9} \frac{z + 3i}{(z - 3i)^3}$$

**Step 3: Evaluate the limit as $z \to i/3$.**
We evaluate $\lim_{z \to i/3} -\frac{1}{9} \frac{z + 3i}{(z - 3i)^3}$ by direct substitution:
$$= -\frac{1}{9} \frac{(i/3) + 3i}{(i/3 - 3i)^3}$$

Simplify the numerator and denominator by finding common denominators:
*   Numerator: $\frac{i}{3} + 3i = \frac{i}{3} + \frac{9i}{3} = \frac{10i}{3}$
*   Denominator base: $\frac{i}{3} - 3i = \frac{i}{3} - \frac{9i}{3} = -\frac{8i}{3}$
*   Denominator cubed: $(-\frac{8i}{3})^3 = \frac{(-8)^3 i^3}{3^3} = \frac{-512(-i)}{27} = \frac{512i}{27}$

Substitute these values back into the limit expression:
$$= -\frac{1}{9} \frac{\frac{10i}{3}}{\frac{512i}{27}}$$
$$= -\frac{1}{9} \left( \frac{10i}{3} \cdot \frac{27}{512i} \right)$$

Cancel the $i$ terms:
$$= -\frac{1}{9} \left( \frac{10}{3} \cdot \frac{27}{512} \right)$$
$$= -\frac{1}{9} \left( \frac{10 \cdot 9}{512} \right)$$
Cancel the 9s:
$$= -\frac{10}{512}$$
Simplify the fraction by dividing top and bottom by 2:
$$= -\frac{5}{256}$$

**Answer:** The limit evaluates to **$-\frac{5}{256}$**.

***

### Q112. Ques: a) $\lim_{z\rightarrow\infty}\frac{z-1}{z+1}$, b) $\lim_{z\rightarrow\infty}\frac{2z+3i}{z^2+z+1}$

**Solution:**

We need to evaluate two limits of complex rational functions as $z$ approaches complex infinity. The technique is identical to evaluating limits at infinity in real calculus: divide the numerator and denominator by the highest power of $z$ present in the denominator. 
Note that as $|z| \to \infty$, the term $1/z \to 0$.

**Part a) Evaluate $\lim_{z\rightarrow\infty}\frac{z-1}{z+1}$**

**Step 1: Identify the highest power of $z$ in the denominator.**
The denominator is $z+1$. The highest power of $z$ is $z^1 = z$.

**Step 2: Divide numerator and denominator by $z$.**
$$\lim_{z\rightarrow\infty} \frac{\frac{z-1}{z}}{\frac{z+1}{z}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{z}{z} - \frac{1}{z}}{\frac{z}{z} + \frac{1}{z}}$$
$$\lim_{z\rightarrow\infty} \frac{1 - \frac{1}{z}}{1 + \frac{1}{z}}$$

**Step 3: Apply the limit.**
As $z \to \infty$, the term $\frac{1}{z} \to 0$.
Substitute $0$ for these terms:
$$= \frac{1 - 0}{1 + 0} = \frac{1}{1} = 1$$

**Answer (a): $1$**

---

**Part b) Evaluate $\lim_{z\rightarrow\infty}\frac{2z+3i}{z^2+z+1}$**

**Step 1: Identify the highest power of $z$ in the denominator.**
The denominator is $z^2+z+1$. The highest power of $z$ is $z^2$.

**Step 2: Divide numerator and denominator by $z^2$.**
$$\lim_{z\rightarrow\infty} \frac{\frac{2z+3i}{z^2}}{\frac{z^2+z+1}{z^2}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{2z}{z^2} + \frac{3i}{z^2}}{\frac{z^2}{z^2} + \frac{z}{z^2} + \frac{1}{z^2}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{2}{z} + \frac{3i}{z^2}}{1 + \frac{1}{z} + \frac{1}{z^2}}$$

**Step 3: Apply the limit.**
As $z \to \infty$, any term with $z$ in the denominator (like $\frac{1}{z}$, $\frac{1}{z^2}$) approaches $0$.
Substitute $0$ for these terms:
$$= \frac{0 + 0}{1 + 0 + 0} = \frac{0}{1} = 0$$

**Answer (b): $0$**

Here are the detailed solutions for the next four questions (Q113 to Q116).

### Q113. Example-2: Prove that $\lim_{z\rightarrow0}\frac{\overline{z}}{z}$ lim doesn't exists.

**Solution:**

In complex analysis, for a limit $\lim_{z \to z_0} f(z)$ to exist, the function must approach the exact same value regardless of the path or direction $z$ takes to get to $z_0$ in the 2D complex plane. If we can find two different paths to $z=0$ that yield two different limit values, then the overall limit does not exist.

Let $z$ be represented in Cartesian coordinates: $z = x + iy$.
The complex conjugate is $\overline{z} = x - iy$.
The limit expression becomes:
$$\lim_{(x,y) \to (0,0)} \frac{x - iy}{x + iy}$$

We will test two different straight-line paths approaching the origin $(0,0)$.

**Path 1: Approach along the real axis (x-axis)**
If we move along the real axis, the imaginary part is always zero ($y = 0$).
We substitute $y = 0$ into our limit expression and let $x \to 0$:
$$\lim_{x \to 0} \frac{x - i(0)}{x + i(0)} = \lim_{x \to 0} \frac{x}{x}$$
Since $x$ is approaching $0$ but is not exactly $0$, we can cancel $x$:
$$\lim_{x \to 0} 1 = 1$$
So, along the x-axis, the limit approaches **$1$**.

**Path 2: Approach along the imaginary axis (y-axis)**
If we move along the imaginary axis, the real part is always zero ($x = 0$).
We substitute $x = 0$ into our limit expression and let $y \to 0$:
$$\lim_{y \to 0} \frac{0 - iy}{0 + iy} = \lim_{y \to 0} \frac{-iy}{iy}$$
Cancel the $iy$ terms:
$$\lim_{y \to 0} -1 = -1$$
So, along the y-axis, the limit approaches **$-1$**.

*(Optional Path 3: Approach along any line $y = mx$. The limit becomes $\frac{x-imx}{x+imx} = \frac{1-im}{1+im}$, meaning the limit's value depends entirely on the slope $m$ of the approach path).*

**Conclusion:**
Since the function approaches $1$ along the real axis and $-1$ along the imaginary axis, it does not approach a single unique value. Therefore, by definition, the limit does not exist. **(Proved)**

***

### Q114. Example 03: Evaluate $\lim_{z\rightarrow i}(z-i)\frac{e^{mz}}{(z^2+1)}$

**Solution:**

We need to evaluate the limit of a complex rational function.
Let $f(z) = (z-i)\frac{e^{mz}}{z^2+1}$.

**Step 1: Check for direct substitution.**
If we substitute $z = i$ directly:
Numerator: $(i - i) e^{mi} = 0$
Denominator: $i^2 + 1 = -1 + 1 = 0$
We get the indeterminate form $0/0$. We must simplify the expression to eliminate the singularity at $z=i$.

**Step 2: Factor the denominator.**
The term $z^2 + 1$ is a sum of squares. Using the fact that $i^2 = -1$, we can rewrite it as a difference of squares:
$$z^2 + 1 = z^2 - (-1) = z^2 - i^2$$
Factor using $a^2 - b^2 = (a-b)(a+b)$:
$$z^2 + 1 = (z - i)(z + i)$$

**Step 3: Substitute the factored denominator back into the limit.**
$$\lim_{z \to i} \frac{(z-i) e^{mz}}{(z - i)(z + i)}$$

**Step 4: Cancel the common factor.**
Since $z$ is approaching $i$ but is not exactly equal to $i$ in the context of the limit limit ($z \neq i$), we can safely cancel the $(z-i)$ term from the numerator and the denominator:
$$\lim_{z \to i} \frac{e^{mz}}{z + i}$$

**Step 5: Evaluate the limit by direct substitution.**
Now, substitute $z = i$ into the simplified expression. The denominator is no longer zero.
$$= \frac{e^{m(i)}}{i + i}$$
$$= \frac{e^{mi}}{2i}$$

*(Optional: We can rationalize the denominator by multiplying top and bottom by $-i$:)*
$$= \frac{e^{mi} \cdot (-i)}{2i \cdot (-i)} = \frac{-i e^{mi}}{-2i^2} = \frac{-i e^{mi}}{2(1)} = -\frac{i}{2}e^{mi}$$

**Answer:** The limit evaluates to **$\frac{e^{mi}}{2i}$** (or **$-\frac{i}{2}e^{mi}$**).

***

### Q115. Example 04: Evaluate $\lim_{z\rightarrow ae^{i\pi/4}}(z-ae^{i\pi/4})\frac{1}{z^4+a^4}$

**Solution:**

Let $z_0 = a e^{i\pi/4}$. We are evaluating the limit:
$$L = \lim_{z \to z_0} \frac{z - z_0}{z^4 + a^4}$$

*(Note: This specific limit format represents the calculation of the residue of the function $f(z) = \frac{1}{z^4+a^4}$ at its simple pole $z_0$).*

**Step 1: Check for direct substitution.**
If we substitute $z = z_0$:
Numerator: $z_0 - z_0 = 0$
Denominator: $z_0^4 + a^4 = (a e^{i\pi/4})^4 + a^4 = a^4 e^{i\pi} + a^4$.
Since Euler's identity states $e^{i\pi} = -1$:
Denominator: $a^4(-1) + a^4 = -a^4 + a^4 = 0$.
We have the indeterminate form $0/0$.

**Step 2: Apply L'Hôpital's Rule.**
Because both the numerator and denominator are analytic (differentiable) complex functions, and they approach $0/0$, we can use complex L'Hôpital's Rule. We differentiate the numerator and denominator with respect to $z$:
*   Derivative of numerator: $\frac{d}{dz}(z - z_0) = 1$
*   Derivative of denominator: $\frac{d}{dz}(z^4 + a^4) = 4z^3$

Apply L'Hôpital's Rule to the limit:
$$L = \lim_{z \to z_0} \frac{1}{4z^3}$$

**Step 3: Evaluate by substitution.**
Substitute $z = z_0 = a e^{i\pi/4}$:
$$L = \frac{1}{4(a e^{i\pi/4})^3}$$
$$L = \frac{1}{4 a^3 e^{i3\pi/4}}$$

**Step 4: Simplify the expression.**
Bring the exponential term to the numerator by changing the sign of the exponent:
$$L = \frac{e^{-i3\pi/4}}{4a^3}$$

*(Optional: Convert to Cartesian form using $e^{-i3\pi/4} = \cos(-\frac{3\pi}{4}) + i\sin(-\frac{3\pi}{4}) = -\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$. The limit becomes $\frac{-1 - i}{4a^3\sqrt{2}}$).*

**Answer:** The limit evaluates to **$\frac{e^{-i3\pi/4}}{4a^3}$**.

***

### Q116. Example-05: Evaluate $\lim_{z\rightarrow ae^{i3\pi/4}}(z-ae^{i3\pi/4})\frac{1}{z^4+a^4}$

**Solution:**

This question is mechanically identical to Q115, but we are evaluating the limit at a different root of the denominator.
Let $z_1 = a e^{i3\pi/4}$. We are evaluating:
$$L = \lim_{z \to z_1} \frac{z - z_1}{z^4 + a^4}$$

**Step 1: Check for direct substitution.**
Numerator approaches $z_1 - z_1 = 0$.
Denominator approaches $z_1^4 + a^4 = (a e^{i3\pi/4})^4 + a^4 = a^4 e^{i3\pi} + a^4$.
Since $e^{i3\pi} = \cos(3\pi) + i\sin(3\pi) = -1 + 0 = -1$:
Denominator $= a^4(-1) + a^4 = 0$.
We have the indeterminate form $0/0$.

**Step 2: Apply L'Hôpital's Rule.**
Differentiate the numerator and denominator with respect to $z$:
*   Derivative of numerator: $\frac{d}{dz}(z - z_1) = 1$
*   Derivative of denominator: $\frac{d}{dz}(z^4 + a^4) = 4z^3$

Apply the rule:
$$L = \lim_{z \to z_1} \frac{1}{4z^3}$$

**Step 3: Evaluate by substitution.**
Substitute $z = z_1 = a e^{i3\pi/4}$:
$$L = \frac{1}{4(a e^{i3\pi/4})^3}$$
$$L = \frac{1}{4 a^3 e^{i9\pi/4}}$$

**Step 4: Simplify the argument (angle).**
The angle $\frac{9\pi}{4}$ is greater than a full rotation ($2\pi$). We can simplify it by subtracting $2\pi$ (which is $\frac{8\pi}{4}$):
$$\frac{9\pi}{4} - \frac{8\pi}{4} = \frac{\pi}{4}$$
Therefore, $e^{i9\pi/4} = e^{i\pi/4}$.

Substitute this simplified exponential back into the expression:
$$L = \frac{1}{4 a^3 e^{i\pi/4}}$$

Bring the exponential term to the numerator by changing the sign of the exponent:
$$L = \frac{e^{-i\pi/4}}{4a^3}$$

*(Optional: Convert to Cartesian form using $e^{-i\pi/4} = \cos(-\frac{\pi}{4}) + i\sin(-\frac{\pi}{4}) = \frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$. The limit becomes $\frac{1 - i}{4a^3\sqrt{2}}$).*

**Answer:** The limit evaluates to **$\frac{e^{-i\pi/4}}{4a^3}$**.





Here are the detailed solutions for the next four questions (Q117 to Q120).

### Q117. Example-06: $f(z)=z^2$ if $z\ne i$, $0$ if $z=i$ (Implied: Check continuity)

*(Note: This is conceptually identical to Q125 from the Feruj sheet section. The prompt asks to check continuity and redefine if necessary).*

**Solution:**

We are given a piecewise complex function:
$$f(z) = \begin{cases} z^2 & \text{if } z \neq i \\ 0 & \text{if } z = i \end{cases}$$

A complex function $f(z)$ is continuous at a point $z = z_0$ if and only if three conditions are satisfied:
1.  The function is defined at $z_0$: $f(z_0)$ exists.
2.  The limit exists at $z_0$: $\lim_{z \to z_0} f(z)$ exists.
3.  The limit equals the function value: $\lim_{z \to z_0} f(z) = f(z_0)$.

Let's test these conditions for the point $z_0 = i$.

**Step 1: Check the function value at $z = i$.**
According to the piecewise definition, when $z$ is exactly exactly $i$, the function value is $0$.
$$f(i) = 0$$

**Step 2: Evaluate the limit as $z \to i$.**
For the limit, we consider the behavior of the function as $z$ approaches $i$, but is not equal to $i$. Therefore, we use the first part of the piecewise definition: $f(z) = z^2$.
$$\lim_{z \to i} f(z) = \lim_{z \to i} z^2$$
Since $z^2$ is a simple polynomial, it is continuous everywhere, so we can evaluate the limit by direct substitution:
$$\lim_{z \to i} z^2 = (i)^2 = -1$$

**Step 3: Compare the limit to the function value.**
*   Limit: $\lim_{z \to i} f(z) = -1$
*   Function value: $f(i) = 0$
Since $-1 \neq 0$, the third condition for continuity fails. 
Therefore, the function is **not continuous** at $z=i$. This is known as a *removable discontinuity*.

**Step 4: Redefine the function to make it continuous.**
To remove the discontinuity, we simply redefine the value of $f(i)$ so that it matches the limit.
We need $f(i) = -1$.
The newly redefined continuous function is:
$$f_{new}(z) = \begin{cases} z^2 & \text{if } z \neq i \\ -1 & \text{if } z = i \end{cases}$$
*(Notice that this redefined function is simply $f_{new}(z) = z^2$ for all complex numbers $z$).*

**Answer:** 
The function is **not continuous** at $z=i$ because $\lim_{z\to i} f(z) = -1$ but $f(i) = 0$. 
To make it continuous, redefine $f(i)$ to be **$-1$**.

***

### Q118. Problem-7: $f(z)=\frac{z^2+4}{z-2i}$ if $z\ne 2i$, $3+4i$ if $z=2i$ (Implied: Check continuity)

*(Note: This is conceptually identical to Q126).*

**Solution:**

We are given the piecewise complex function:
$$f(z) = \begin{cases} \frac{z^2+4}{z-2i} & \text{if } z \neq 2i \\ 3+4i & \text{if } z = 2i \end{cases}$$
We will test the three conditions for continuity at $z_0 = 2i$.

**Step 1: Check the function value at $z = 2i$.**
From the definition:
$$f(2i) = 3 + 4i$$

**Step 2: Evaluate the limit as $z \to 2i$.**
We use the main branch of the function:
$$\lim_{z \to 2i} f(z) = \lim_{z \to 2i} \frac{z^2 + 4}{z - 2i}$$
If we substitute $z=2i$ directly, we get $\frac{(2i)^2+4}{2i-2i} = \frac{-4+4}{0} = \frac{0}{0}$. We must factor.
The numerator is a sum of squares, which factors as a difference of squares using $i^2 = -1$:
$$z^2 + 4 = z^2 - (-4) = z^2 - (2i)^2 = (z - 2i)(z + 2i)$$

Substitute this factored form into the limit:
$$\lim_{z \to 2i} \frac{(z - 2i)(z + 2i)}{z - 2i}$$
Since $z \to 2i$ means $z \neq 2i$, we can cancel the $(z-2i)$ term:
$$\lim_{z \to 2i} (z + 2i)$$
Now substitute $z = 2i$:
$$= 2i + 2i = 4i$$

**Step 3: Compare the limit to the function value.**
*   Limit: $\lim_{z \to 2i} f(z) = 4i$
*   Function value: $f(2i) = 3 + 4i$
Since $4i \neq 3 + 4i$, the third condition fails. 
Therefore, the function is **not continuous** at $z=2i$.

**Step 4: Redefine the function to make it continuous.**
We must redefine $f(2i)$ to equal the limit we just calculated. Let $f(2i) = 4i$.
The redefined continuous function is:
$$f_{new}(z) = \begin{cases} \frac{z^2+4}{z-2i} & \text{if } z \neq 2i \\ 4i & \text{if } z = 2i \end{cases}$$

**Answer:** 
The function is **not continuous** at $z=2i$ because the limit is $4i$ while the function value is $3+4i$. 
To make it continuous, redefine $f(2i)$ to be **$4i$**.

***

### Q119. Example-8: Explain the difference between the limit of a function of real variable & complex variable.

*(Note: This is identical to Q127).*

**Solution:**

The fundamental difference between limits in real calculus and complex calculus lies in the **degrees of freedom** available when approaching a target point.

**1. Limit of a Real Variable ($x \to x_0$):**
In real calculus, variables exist on a 1-dimensional line (the real number line). 
When evaluating the limit $\lim_{x \to x_0} f(x)$, the variable $x$ can approach the target point $x_0$ from only **two directions**:
*   From the left (values slightly less than $x_0$, denoted as $x \to x_0^-$)
*   From the right (values slightly greater than $x_0$, denoted as $x \to x_0^+$)
For the real limit to exist, the function must approach the exact same value from both the left and the right.

**2. Limit of a Complex Variable ($z \to z_0$):**
In complex analysis, variables exist in a 2-dimensional plane (the Argand plane or Cartesian plane).
When evaluating the limit $\lim_{z \to z_0} f(z)$, the variable $z$ can approach the target point $z_0$ from **infinitely many directions and along infinitely many paths** (e.g., straight lines, parabolas, spirals, etc.).
For the complex limit to exist, the function must approach the exact same unique value $L$ *regardless of the path or direction* chosen to approach $z_0$.

**Summary/Conclusion:**
*   **Real Limit:** Approach is restricted to 1 dimension (2 paths: left and right).
*   **Complex Limit:** Approach occurs in 2 dimensions (infinitely many paths from any $360^\circ$ direction).
Because of this requirement, complex limits are much more stringent. If you can find even two different paths in the complex plane that yield different limit values (as demonstrated in Q113), the complex limit does not exist.

***

### Q120. Question 1: Evaluate: (a) $lim_{z\rightarrow\infty}\frac{z-1}{z+i}$ and (b) $lim_{z\rightarrow\infty}\frac{2z+3i}{z^{2}+z+1}$

*(Note: Part (b) is numerically identical to Q112(b). Part (a) is a slight variation of Q112(a)).*

**Solution:**

We evaluate these limits as $z$ approaches complex infinity by dividing the numerator and denominator by the highest power of $z$ found in the denominator. As $z \to \infty$, the fraction $1/z^n \to 0$ for any integer $n > 0$.

**Part (a) Evaluate $\lim_{z\rightarrow\infty}\frac{z-1}{z+i}$**

**Step 1: Identify highest power.**
The highest power of $z$ in the denominator ($z+i$) is $z^1$.

**Step 2: Divide numerator and denominator by $z$.**
$$\lim_{z\rightarrow\infty} \frac{\frac{z-1}{z}}{\frac{z+i}{z}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{z}{z} - \frac{1}{z}}{\frac{z}{z} + \frac{i}{z}}$$
$$\lim_{z\rightarrow\infty} \frac{1 - \frac{1}{z}}{1 + i\left(\frac{1}{z}\right)}$$

**Step 3: Evaluate the limit.**
As $z \to \infty$, the term $\frac{1}{z}$ approaches $0$.
Substitute $0$ for $\frac{1}{z}$:
$$= \frac{1 - 0}{1 + i(0)} = \frac{1}{1} = 1$$

**Answer (a): $1$**

---

**Part (b) Evaluate $\lim_{z\rightarrow\infty}\frac{2z+3i}{z^{2}+z+1}$**

**Step 1: Identify highest power.**
The highest power of $z$ in the denominator ($z^2+z+1$) is $z^2$.

**Step 2: Divide numerator and denominator by $z^2$.**
$$\lim_{z\rightarrow\infty} \frac{\frac{2z+3i}{z^2}}{\frac{z^2+z+1}{z^2}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{2z}{z^2} + \frac{3i}{z^2}}{\frac{z^2}{z^2} + \frac{z}{z^2} + \frac{1}{z^2}}$$
$$\lim_{z\rightarrow\infty} \frac{\frac{2}{z} + \frac{3i}{z^2}}{1 + \frac{1}{z} + \frac{1}{z^2}}$$

**Step 3: Evaluate the limit.**
As $z \to \infty$, both $\frac{1}{z}$ and $\frac{1}{z^2}$ approach $0$.
Substitute $0$ into the expression:
$$= \frac{2(0) + 3i(0)}{1 + 0 + 0} = \frac{0}{1} = 0$$

**Answer (b): $0$**

Here are the detailed solutions for the next four questions (Q121 to Q124).

*(Note: These questions from the Feruj Sheet are identical to earlier questions from the Firoz Note section. Detailed step-by-step solutions are provided again below for completeness).*

### Q121. Example 2: Prove that $lim_{z\rightarrow0}\frac{\overline{z}}{z}$ does not exists.

**Solution:**

In complex analysis, a limit $\lim_{z \to z_0} f(z)$ only exists if the function approaches a single, unique value regardless of the path $z$ takes to reach $z_0$ in the 2D complex plane. If we evaluate the limit along two different paths and get two different answers, the limit does not exist.

Let the complex number be $z = x + iy$.
The complex conjugate is $\overline{z} = x - iy$.
The limit we are evaluating is:
$$\lim_{(x,y) \to (0,0)} \frac{x - iy}{x + iy}$$

We will test two standard straight-line paths through the origin.

**Path 1: Approach along the real axis (the x-axis)**
If we move along the x-axis, the imaginary part $y$ is constantly $0$.
Substitute $y = 0$ into the limit expression, leaving only the $x$ variable:
$$\lim_{x \to 0} \frac{x - i(0)}{x + i(0)} = \lim_{x \to 0} \frac{x}{x}$$
Because $x$ approaches zero but is not exactly zero, the fraction simplifies to 1:
$$\lim_{x \to 0} 1 = 1$$
Along the real axis, the limit approaches **1**.

**Path 2: Approach along the imaginary axis (the y-axis)**
If we move along the y-axis, the real part $x$ is constantly $0$.
Substitute $x = 0$ into the limit expression, leaving only the $y$ variable:
$$\lim_{y \to 0} \frac{0 - iy}{0 + iy} = \lim_{y \to 0} \frac{-iy}{iy}$$
Cancel the $iy$ terms:
$$\lim_{y \to 0} -1 = -1$$
Along the imaginary axis, the limit approaches **-1**.

**Conclusion:**
Because the limit approaches $1$ along one path and $-1$ along another path, there is no single unique limiting value. Therefore, the limit does not exist. **(Proved)**

***

### Q122. Example 3: Evaluate $lim_{z\rightarrow i}\{(z-i)\frac{e^{imx}}{(z^{2}+1)}\}$

*(Note: There is a typo in the source text "$e^{imx}$". Because this is a function of the complex variable $z$, the standard intended problem is $e^{imz}$. I will solve it using $e^{imz}$, which is also consistent with the identical problem Q114).*

**Solution:**

We need to evaluate the limit:
$$L = \lim_{z \to i} (z-i)\frac{e^{imz}}{z^2+1}$$

**Step 1: Check for direct substitution.**
Substitute $z=i$ into the expression:
Numerator: $(i - i)e^{im(i)} = 0 \cdot e^{-m} = 0$
Denominator: $i^2 + 1 = -1 + 1 = 0$
This results in the indeterminate form $0/0$, meaning we must simplify the expression algebraically.

**Step 2: Factor the denominator.**
The denominator is $z^2 + 1$. Because $i^2 = -1$, we can rewrite this as a difference of squares:
$$z^2 + 1 = z^2 - (-1) = z^2 - i^2$$
Using the algebraic identity $a^2 - b^2 = (a-b)(a+b)$:
$$z^2 + 1 = (z - i)(z + i)$$

**Step 3: Substitute and simplify the limit expression.**
Replace the denominator in the limit:
$$L = \lim_{z \to i} \frac{(z-i)e^{imz}}{(z-i)(z+i)}$$

Since $z$ is approaching $i$ but is not exactly equal to $i$ during the limit process (so $z-i \neq 0$), we can safely cancel the common $(z-i)$ term from the top and bottom:
$$L = \lim_{z \to i} \frac{e^{imz}}{z+i}$$

**Step 4: Evaluate the simplified limit.**
Now we can evaluate the limit by direct substitution of $z = i$, because the denominator will no longer be zero.
$$L = \frac{e^{im(i)}}{i + i}$$
$$L = \frac{e^{im \cdot i^2}}{2i}$$
Since $i^2 = -1$:
$$L = \frac{e^{-m}}{2i}$$

*(Optional: We can bring the $i$ to the numerator by multiplying top and bottom by $-i$:
$L = \frac{-i e^{-m}}{2i(-i)} = \frac{-i e^{-m}}{-2i^2} = \frac{-i e^{-m}}{2}$).*

**Answer:** The limit evaluates to **$\frac{e^{-m}}{2i}$** (or **$-i\frac{e^{-m}}{2}$**).

***

### Q123. Example 4: Evaluate $lim_{z\rightarrow ae^{\frac{\pi i}{4}}}\{(z-ae^{\frac{\pi i}{4}})\frac{1}{z^{4}+a^{4}}\}$

**Solution:**

Let $z_0 = a e^{i\pi/4}$. The limit we are evaluating is:
$$L = \lim_{z \to z_0} \frac{z - z_0}{z^4 + a^4}$$

**Step 1: Check for direct substitution.**
Substitute $z = z_0$:
Numerator: $z_0 - z_0 = 0$
Denominator: $z_0^4 + a^4 = (a e^{i\pi/4})^4 + a^4 = a^4 e^{i\pi} + a^4$.
We know that Euler's identity is $e^{i\pi} = -1$.
Denominator $= a^4(-1) + a^4 = -a^4 + a^4 = 0$.
Since we get $0/0$, we can apply L'Hôpital's Rule.

**Step 2: Apply L'Hôpital's Rule.**
Because both the numerator and denominator are analytic functions, we take the derivative of the numerator and the denominator with respect to $z$:
*   Derivative of numerator: $\frac{d}{dz}(z - z_0) = 1$
*   Derivative of denominator: $\frac{d}{dz}(z^4 + a^4) = 4z^3$

The limit becomes:
$$L = \lim_{z \to z_0} \frac{1}{4z^3}$$

**Step 3: Evaluate by substitution.**
Now substitute $z = z_0 = a e^{i\pi/4}$:
$$L = \frac{1}{4(a e^{i\pi/4})^3}$$
$$L = \frac{1}{4 a^3 e^{i3\pi/4}}$$

**Step 4: Clean up the expression.**
Bring the exponential term to the numerator by negating the exponent:
$$L = \frac{e^{-i3\pi/4}}{4a^3}$$

*(If requested in Cartesian form: $e^{-i3\pi/4} = \cos(-\frac{3\pi}{4}) + i\sin(-\frac{3\pi}{4}) = -\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$. 
So $L = \frac{-\frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}}{4a^3} = \frac{-1 - i}{4a^3\sqrt{2}}$).*

**Answer:** The limit evaluates to **$\frac{e^{-i3\pi/4}}{4a^3}$**.

***

### Q124. Examples: Evaluate $lim_{z\rightarrow ae^{\frac{3\pi i}{4}}}\{(z-ae^{\frac{3\pi i}{4}})\frac{1}{z^{4}+a^{4}}\}$

**Solution:**

This is solved using the exact same procedure as Q123, just evaluating at a different pole.
Let $z_1 = a e^{i3\pi/4}$. The limit is:
$$L = \lim_{z \to z_1} \frac{z - z_1}{z^4 + a^4}$$

**Step 1: Check for direct substitution.**
Numerator: $z_1 - z_1 = 0$
Denominator: $z_1^4 + a^4 = (a e^{i3\pi/4})^4 + a^4 = a^4 e^{i3\pi} + a^4$.
Since $e^{i3\pi} = \cos(3\pi) + i\sin(3\pi) = -1 + 0 = -1$.
Denominator $= a^4(-1) + a^4 = 0$.
The form is $0/0$.

**Step 2: Apply L'Hôpital's Rule.**
Differentiate the top and bottom with respect to $z$:
*   Derivative of top: $1$
*   Derivative of bottom: $4z^3$

$$L = \lim_{z \to z_1} \frac{1}{4z^3}$$

**Step 3: Evaluate by substitution.**
Substitute $z = z_1 = a e^{i3\pi/4}$:
$$L = \frac{1}{4(a e^{i3\pi/4})^3}$$
$$L = \frac{1}{4 a^3 e^{i9\pi/4}}$$

**Step 4: Simplify the angle.**
The angle $\frac{9\pi}{4}$ is greater than $2\pi$. We subtract $2\pi$ (or $\frac{8\pi}{4}$) to find the equivalent principal angle:
$$\frac{9\pi}{4} - \frac{8\pi}{4} = \frac{\pi}{4}$$
So, $e^{i9\pi/4} = e^{i\pi/4}$.

Substitute this back:
$$L = \frac{1}{4 a^3 e^{i\pi/4}}$$

Bring the exponential to the numerator:
$$L = \frac{e^{-i\pi/4}}{4a^3}$$

*(In Cartesian form: $e^{-i\pi/4} = \frac{1}{\sqrt{2}} - i\frac{1}{\sqrt{2}}$. So $L = \frac{1 - i}{4a^3\sqrt{2}}$).*

**Answer:** The limit evaluates to **$\frac{e^{-i\pi/4}}{4a^3}$**.
Here are the detailed solutions for the next four questions (Q125 to Q128).

### Q125. Example 6: If $f(z)=\begin{cases}z^{2}&;z\ne i\\ 0&;z=i\end{cases},$ Is the function continuous at $z=i$ ? If not, redefine the function to be continuous.

**Solution:**

To determine if a complex function $f(z)$ is continuous at a specific point $z_0$, we must verify three conditions:
1.  The function must be defined at $z_0$ (i.e., $f(z_0)$ exists).
2.  The limit of the function as $z$ approaches $z_0$ must exist.
3.  The limit must equal the defined function value: $\lim_{z \to z_0} f(z) = f(z_0)$.

Let's test these conditions for $z_0 = i$.

**Step 1: Determine the defined function value at $z = i$.**
Looking at the piecewise definition, when $z$ is exactly exactly $i$, the function is explicitly defined to equal $0$.
$$f(i) = 0$$

**Step 2: Evaluate the limit as $z$ approaches $i$.**
When calculating the limit as $z \to i$, we are examining values of $z$ that are infinitesimally close to $i$, but *not exactly equal* to $i$. Therefore, we must use the top branch of the piecewise function: $f(z) = z^2$.
$$\lim_{z \to i} f(z) = \lim_{z \to i} z^2$$
Since $z^2$ is a simple polynomial, it is continuous everywhere in the complex plane. We can evaluate this limit by direct substitution.
$$\lim_{z \to i} z^2 = (i)^2 = -1$$

**Step 3: Compare the limit to the function value.**
*   The limit is $\lim_{z \to i} f(z) = -1$.
*   The function value is $f(i) = 0$.
Since $-1 \neq 0$, the third condition for continuity fails. The function has a "removable discontinuity" (a hole) at $z=i$.
Therefore, the function is **not continuous** at $z=i$.

**Step 4: Redefine the function to make it continuous.**
To "fix" a removable discontinuity, we simply redefine the single point $f(z_0)$ so that it matches the limit we found. We need $f(i)$ to equal $-1$.

The redefined continuous function is:
$$f_{\text{new}}(z) = \begin{cases} z^2 & ; z \neq i \\ -1 & ; z = i \end{cases}$$
*(Note that because $i^2 = -1$, this redefined function is identical to simply stating $f_{\text{new}}(z) = z^2$ for all $z$).*

**Answer:**
The function is **not continuous** at $z=i$. To make it continuous, redefine the function value at $z=i$ to be **$-1$**.

***

### Q126. Problem 7: If $f(z)=\begin{cases}\frac{z^{2}+4}{z-2i}&;z\ne2i\\ 3+4i&;z=2i\end{cases}$ Is the function continuous at $z=2i$ ? If not, redefine the function to be continuous.

**Solution:**

We test the three standard conditions for continuity at the point $z_0 = 2i$.

**Step 1: Determine the defined function value at $z = 2i$.**
According to the piecewise definition, when $z = 2i$:
$$f(2i) = 3 + 4i$$

**Step 2: Evaluate the limit as $z$ approaches $2i$.**
Because $z$ is approaching $2i$ but is not equal to it, we use the rational branch of the function:
$$\lim_{z \to 2i} f(z) = \lim_{z \to 2i} \frac{z^2 + 4}{z - 2i}$$

Let's test direct substitution:
Numerator: $(2i)^2 + 4 = -4 + 4 = 0$
Denominator: $2i - 2i = 0$
We get the indeterminate form $0/0$. We must use algebra to simplify the fraction.

Factor the numerator. The expression $z^2 + 4$ is a sum of squares, which we can rewrite as a difference of squares by using $i^2 = -1$:
$$z^2 + 4 = z^2 - (-4) = z^2 - (2i)^2$$
Using the identity $a^2 - b^2 = (a-b)(a+b)$:
$$z^2 + 4 = (z - 2i)(z + 2i)$$

Substitute this back into the limit expression:
$$\lim_{z \to 2i} \frac{(z - 2i)(z + 2i)}{z - 2i}$$

Since $z \neq 2i$ in the limit process, we can cancel the common $(z - 2i)$ term from the top and bottom:
$$= \lim_{z \to 2i} (z + 2i)$$

Now we can evaluate this simplified limit by direct substitution:
$$= (2i) + 2i = 4i$$

**Step 3: Compare the limit to the function value.**
*   The limit is $\lim_{z \to 2i} f(z) = 4i$.
*   The function value is $f(2i) = 3 + 4i$.
Because $4i \neq 3 + 4i$, the third condition for continuity fails. 
Therefore, the function is **not continuous** at $z = 2i$.

**Step 4: Redefine the function to make it continuous.**
To remove the discontinuity, we must redefine $f(2i)$ to be equal to the limit we calculated ($4i$).

The redefined continuous function is:
$$f_{\text{new}}(z) = \begin{cases} \frac{z^2+4}{z-2i} & ; z \neq 2i \\ 4i & ; z = 2i \end{cases}$$

**Answer:**
The function is **not continuous** at $z=2i$. To make it continuous, redefine the function value at $z=2i$ to be **$4i$**.

***

### Q127. Example 8: State the basic difference between the limit of a function of a real variable and that of a complex variable.

**Solution:**

The fundamental difference lies in the dimensionality of the space where the variable resides, which dictates how the variable can approach a target point.

**1. Real Variable Limit ($x \to x_0$):**
*   **Dimensionality:** A real variable $x$ exists on a 1-dimensional line (the real number line).
*   **Approach Paths:** To approach a target point $x_0$, the variable $x$ is highly restricted. It can only approach from exactly **two directions**:
    *   From the left ($x \to x_0^-$), where values are less than $x_0$.
    *   From the right ($x \to x_0^+$), where values are greater than $x_0$.
*   **Condition for Existence:** For the real limit to exist, the function must converge to the same value from both of these two directions.

**2. Complex Variable Limit ($z \to z_0$):**
*   **Dimensionality:** A complex variable $z$ exists in a 2-dimensional plane (the Argand/Cartesian plane).
*   **Approach Paths:** To approach a target point $z_0$, the variable $z$ can take **infinitely many directions and paths**. It can approach along the x-axis, the y-axis, any diagonal line, a parabola, a spiral, or any other continuous curve ending at $z_0$.
*   **Condition for Existence:** For the complex limit to exist, the function must converge to the *exact same unique value* regardless of which of the infinitely many paths is taken to reach $z_0$.

**Summary:**
Because a complex variable can approach a point from $360^\circ$ of directions rather than just two, proving that a complex limit exists is a much stronger and more restrictive condition than proving a real limit exists. If just two different paths in the complex plane yield different limit values, the overall complex limit fails to exist.

***

### Q128. Problems 2.1 Question 1: Prove that the zeros of (a) sin z and (b) cos z are all real and find them

**Solution:**

We need to find all complex values of $z$ that make $\sin z = 0$ and $\cos z = 0$, and prove that these values only occur on the real axis (i.e., their imaginary part is zero). Let $z = x + iy$.

**Part (a): Zeros of $\sin z$**

**Step 1: Express $\sin z$ in terms of real and imaginary parts.**
Using the trigonometric addition formula $\sin(A+B) = \sin A\cos B + \cos A\sin B$:
$$\sin(x+iy) = \sin x\cos(iy) + \cos x\sin(iy)$$
Substitute the hyperbolic identities $\cos(iy) = \cosh y$ and $\sin(iy) = i\sinh y$:
$$\sin z = \sin x\cosh y + i\cos x\sinh y$$

**Step 2: Set the function to zero.**
For $\sin z = 0$, both its real and imaginary parts must simultaneously equal zero:
1) $\sin x\cosh y = 0$
2) $\cos x\sinh y = 0$

**Step 3: Solve the system.**
Look at equation 1: $\sin x\cosh y = 0$.
The hyperbolic cosine function $\cosh y = \frac{e^y + e^{-y}}{2}$ is always strictly greater than or equal to $1$ for all real numbers $y$. It can never be zero. 
Therefore, the only way equation 1 can be true is if $\sin x = 0$.
The solutions for $\sin x = 0$ are $x = n\pi$, where $n$ is any integer ($n = 0, \pm 1, \pm 2, \dots$).

Now look at equation 2: $\cos x\sinh y = 0$.
We know from our result above that $x = n\pi$.
The cosine of $n\pi$ is $\cos(n\pi) = (-1)^n$, which is always either $1$ or $-1$. It is never zero.
Therefore, the only way equation 2 can be true is if $\sinh y = 0$.
The hyperbolic sine function $\sinh y = \frac{e^y - e^{-y}}{2}$ equals $0$ if and only if $e^y = e^{-y}$, which only happens when $y = 0$.

**Step 4: Conclude.**
We found that $y = 0$ is required. Since the imaginary part $y$ must be zero, all zeros of $\sin z$ lie purely on the real axis.
The zeros are located at $z = x + i(0) = n\pi$.

**Answer (a):** Zeros are all real because $y=0$. The zeros are **$z = n\pi$** (where $n \in \mathbb{Z}$).

---

**Part (b): Zeros of $\cos z$**

**Step 1: Express $\cos z$ in terms of real and imaginary parts.**
Using the addition formula $\cos(A+B) = \cos A\cos B - \sin A\sin B$:
$$\cos(x+iy) = \cos x\cos(iy) - \sin x\sin(iy)$$
Substitute the hyperbolic identities:
$$\cos z = \cos x\cosh y - i\sin x\sinh y$$

**Step 2: Set the function to zero.**
Both real and imaginary parts must equal zero:
1) $\cos x\cosh y = 0$
2) $-\sin x\sinh y = 0 \implies \sin x\sinh y = 0$

**Step 3: Solve the system.**
Look at equation 1: $\cos x\cosh y = 0$.
As established earlier, $\cosh y \ge 1$, so it is never zero.
Therefore, it must be that $\cos x = 0$.
The solutions for $\cos x = 0$ are $x = \frac{\pi}{2} + n\pi = (n + \frac{1}{2})\pi$, where $n$ is any integer.

Now look at equation 2: $\sin x\sinh y = 0$.
Since $x = (n + \frac{1}{2})\pi$, we evaluate $\sin((n + \frac{1}{2})\pi)$. This evaluates to $\pm 1$ depending on $n$. It is never zero.
Therefore, it must be that $\sinh y = 0$.
As established earlier, $\sinh y = 0$ implies $y = 0$.

**Step 4: Conclude.**
Since $y = 0$, all zeros of $\cos z$ lie purely on the real axis.
The zeros are located at $z = x + i(0) = (n + \frac{1}{2})\pi$.

**Answer (b):** Zeros are all real because $y=0$. The zeros are **$z = (n + \frac{1}{2})\pi$** (where $n \in \mathbb{Z}$).

Here are the detailed solutions for the next four questions (Q129 to Q132).

### Q129. Problems 2.1 Question 2: Find the limits of the followings: 
(i) $lim_{z\rightarrow\frac{-a+\sqrt{a^{2}-b^{2}}}{b}i}(z-\frac{-a+\sqrt{a^{2}-b^{2}}}{b}i)\frac{2}{bz^{2}+2aiz-b}$ *(Note: Corrected typo in source text where the approach point was missing the $i$, based on the structure of the denominator's roots).*
(ii) $lim_{z\rightarrow\frac{1}{2}}\{(z-\frac{1}{2})\frac{z^{6}+1}{z^{3}(2z-1)(z-2)}\}$ 
(iii) $lim_{z\rightarrow\pi i}\frac{d}{dz}\{(z-\pi i)^{2}\frac{e^{z}}{(z-\pi i)^{2}(z+\pi i)^{2}}\}$

**Solution:**

---
**Part (i):** Evaluate $L = \lim_{z\to z_0} (z-z_0)\frac{2}{bz^2+2aiz-b}$ where $z_0 = \frac{-a+\sqrt{a^2-b^2}}{b}i$.

**Step 1: Analyze the limit structure.**
This limit is explicitly designed to find the residue at a simple pole $z_0$. The expression is of the form $\lim_{z\to z_0} (z-z_0)f(z)$. Let the denominator of $f(z)$ be $D(z) = bz^2+2aiz-b$. 

**Step 2: Verify $z_0$ is a root of the denominator.**
Let's find the roots of $D(z) = 0$ using the quadratic formula for $z$:
$$z = \frac{-2ai \pm \sqrt{(2ai)^2 - 4(b)(-b)}}{2b}$$
$$z = \frac{-2ai \pm \sqrt{-4a^2 + 4b^2}}{2b}$$
$$z = \frac{-2ai \pm 2\sqrt{-(a^2-b^2)}}{2b}$$
$$z = \frac{-ai \pm i\sqrt{a^2-b^2}}{b} = \left(\frac{-a \pm \sqrt{a^2-b^2}}{b}\right)i$$
We can clearly see that the given limit point $z_0$ is one of these two roots (the one using the "$+$" sign). Let the other root be $z_1 = \frac{-a-\sqrt{a^2-b^2}}{b}i$.

**Step 3: Factor the denominator.**
Since we know the roots $z_0$ and $z_1$ and the leading coefficient $b$, we can rewrite the denominator as:
$$bz^2+2aiz-b = b(z-z_0)(z-z_1)$$

**Step 4: Substitute and cancel.**
Substitute the factored denominator into the limit:
$$L = \lim_{z\to z_0} (z-z_0) \frac{2}{b(z-z_0)(z-z_1)}$$
Cancel the $(z-z_0)$ term:
$$L = \lim_{z\to z_0} \frac{2}{b(z-z_1)}$$

**Step 5: Evaluate the limit.**
Substitute $z = z_0$:
$$L = \frac{2}{b(z_0 - z_1)}$$
Calculate the difference $(z_0 - z_1)$:
$$z_0 - z_1 = \left(\frac{-a+\sqrt{a^2-b^2}}{b}i\right) - \left(\frac{-a-\sqrt{a^2-b^2}}{b}i\right)$$
$$z_0 - z_1 = \frac{-a + \sqrt{a^2-b^2} + a + \sqrt{a^2-b^2}}{b}i = \frac{2\sqrt{a^2-b^2}}{b}i$$

Substitute this back into $L$:
$$L = \frac{2}{b \left( \frac{2\sqrt{a^2-b^2}}{b}i \right)}$$
$$L = \frac{2}{2i\sqrt{a^2-b^2}}$$
$$L = \frac{1}{i\sqrt{a^2-b^2}} = \frac{-i}{\sqrt{a^2-b^2}}$$

**Answer (i): $\frac{-i}{\sqrt{a^{2}-b^{2}}}$**

---
**Part (ii):** Evaluate $L = \lim_{z\rightarrow\frac{1}{2}}\{(z-\frac{1}{2})\frac{z^{6}+1}{z^{3}(2z-1)(z-2)}\}$

**Step 1: Simplify the expression.**
Notice the term $(2z-1)$ in the denominator. We can factor a $2$ out of it:
$$2z - 1 = 2(z - \frac{1}{2})$$

Substitute this into the limit expression:
$$L = \lim_{z\to\frac{1}{2}} (z - \frac{1}{2}) \frac{z^6+1}{z^3 \cdot 2(z - \frac{1}{2}) \cdot (z-2)}$$

**Step 2: Cancel the common term.**
Cancel $(z - 1/2)$ from numerator and denominator:
$$L = \lim_{z\to\frac{1}{2}} \frac{z^6+1}{2z^3(z-2)}$$

**Step 3: Evaluate by direct substitution.**
Substitute $z = 1/2$:
$$L = \frac{(\frac{1}{2})^6 + 1}{2(\frac{1}{2})^3(\frac{1}{2} - 2)}$$
Numerator: $\frac{1}{64} + 1 = \frac{65}{64}$
Denominator: $2(\frac{1}{8})(-\frac{3}{2}) = \frac{1}{4}(-\frac{3}{2}) = -\frac{3}{8}$

$$L = \frac{\frac{65}{64}}{-\frac{3}{8}} = \frac{65}{64} \cdot \left(-\frac{8}{3}\right)$$
$$L = -\frac{65 \cdot 8}{64 \cdot 3} = -\frac{65}{8 \cdot 3} = -\frac{65}{24}$$

**Answer (ii): $-\frac{65}{24}$**

---
**Part (iii):** Evaluate $L = \lim_{z\rightarrow\pi i}\frac{d}{dz}\{(z-\pi i)^{2}\frac{e^{z}}{(z-\pi i)^{2}(z+\pi i)^{2}}\}$

**Step 1: Simplify the expression inside the derivative.**
The term $(z - \pi i)^2$ appears in both the numerator and denominator. We cancel it:
$$F(z) = \frac{e^z}{(z+\pi i)^2}$$

**Step 2: Take the derivative $\frac{d}{dz}F(z)$.**
Use the quotient rule: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$
*   $u = e^z \implies u' = e^z$
*   $v = (z+\pi i)^2 \implies v' = 2(z+\pi i)$

$$\frac{d}{dz}F(z) = \frac{e^z(z+\pi i)^2 - e^z[2(z+\pi i)]}{[(z+\pi i)^2]^2}$$
Factor out $e^z(z+\pi i)$ from the numerator:
$$\frac{d}{dz}F(z) = \frac{e^z(z+\pi i) [(z+\pi i) - 2]}{(z+\pi i)^4}$$
Cancel one $(z+\pi i)$ term:
$$\frac{d}{dz}F(z) = \frac{e^z(z+\pi i - 2)}{(z+\pi i)^3}$$

**Step 3: Evaluate the limit.**
Substitute $z = \pi i$:
$$L = \frac{e^{\pi i}(\pi i + \pi i - 2)}{(\pi i + \pi i)^3}$$
$$L = \frac{e^{\pi i}(2\pi i - 2)}{(2\pi i)^3}$$

We know $e^{\pi i} = -1$ (Euler's identity). Also, $(2\pi i)^3 = 8\pi^3 i^3 = -8\pi^3 i$.
$$L = \frac{-1(2\pi i - 2)}{-8\pi^3 i}$$
$$L = \frac{2\pi i - 2}{8\pi^3 i}$$
Divide numerator and denominator by 2:
$$L = \frac{\pi i - 1}{4\pi^3 i}$$
Multiply top and bottom by $i$ to clear the $i$ from the denominator:
$$L = \frac{(\pi i - 1)i}{4\pi^3 i^2} = \frac{\pi i^2 - i}{-4\pi^3} = \frac{-\pi - i}{-4\pi^3} = \frac{\pi + i}{4\pi^3}$$

**Answer (iii): $\frac{\pi+i}{4\pi^{3}}$**

***

### Q130. Problems 2.1 Question 3: If $f(z)=\begin{cases}z^{2}+2z&;z\ne i\\ 3+2i&;z=i\end{cases}$ , Is the function continuous at $z=i$ ? If not, redefine the function to be continuous.

**Solution:**

We test the three continuity conditions at $z_0 = i$:
1. $f(i)$ is defined.
2. $\lim_{z\to i} f(z)$ exists.
3. $\lim_{z\to i} f(z) = f(i)$.

**Step 1: Check the defined value.**
From the piecewise definition, $f(i) = 3 + 2i$.

**Step 2: Evaluate the limit.**
For the limit $z \to i$, we use the branch where $z \neq i$:
$$\lim_{z \to i} f(z) = \lim_{z \to i} (z^2 + 2z)$$
Since $z^2+2z$ is a polynomial, it is continuous, and we evaluate by direct substitution:
$$= (i)^2 + 2(i)$$
$$= -1 + 2i$$

**Step 3: Compare limit to value.**
The limit is $-1 + 2i$, but the function value is $3 + 2i$. 
Since they are not equal, the function is **not continuous** at $z=i$.

**Step 4: Redefine the function.**
To make it continuous, we redefine $f(i)$ to equal the evaluated limit.
The new definition is:
$$f_{new}(z) = \begin{cases} z^2+2z & ; z \neq i \\ -1+2i & ; z=i \end{cases}$$

**Answer:** The function is **not continuous**. To make it continuous, redefine $f(i) =$ **$-1+2i$**.

***

### Q131. Problems 2.1 Question 4: (a) Suppose $z=e^{w}$ where $z=r(cos~\theta+i~sin~\theta)$ and $w=u+iv.$ Show that $u=ln~r$ and $v=\theta+2k\pi$ $k=0,$ $\pm1$, ±2,... so that $w=ln~z=ln~r+i(\theta+2k\pi).$ (b) Determine the values of $ln(1-i).$ What is the principal value?

*(Note: There is a typo in the source text "$ln(I-i)$". I assumes it means "$ln(1-i)$" which is standard).*

**Solution:**

**Part (a): Prove the complex logarithm formula.**

1.  We are given $z = e^w$. Substitute the given definitions $z = r(\cos\theta + i\sin\theta)$ and $w = u+iv$:
    $$r(\cos\theta + i\sin\theta) = e^{u+iv}$$
2.  Rewrite the left side in exponential form and the right side using exponent rules:
    $$r e^{i\theta} = e^u \cdot e^{iv}$$
3.  For these two complex numbers to be strictly equal, their moduli (magnitudes) must be equal, and their arguments (angles) must be equal up to an integer multiple of $2\pi$.
    *   **Equating Moduli:** The modulus of the left side is $r$, and the modulus of the right side is $e^u$ (since $|e^{iv}| = 1$).
        $$r = e^u$$
        Taking the natural log of both sides (since $r > 0$ and $u$ is real):
        **$u = \ln r$**
    *   **Equating Arguments:** The argument of the left side is $\theta$, and the argument of the right side is $v$. These must be equivalent angles:
        **$v = \theta + 2k\pi$** (for $k = 0, \pm1, \dots$)
4.  Substitute $u$ and $v$ back into $w = u + iv$:
    $$w = \ln r + i(\theta + 2k\pi)$$
    Since $z = e^w$, by definition $w = \ln z$. Therefore:
    **$\ln z = \ln r + i(\theta + 2k\pi)$** (Proved)

---

**Part (b): Determine values and principal value of $\ln(1-i)$.**

**Step 1: Find $r$ and $\theta$ for $z = 1-i$.**
*   $r = |1-i| = \sqrt{1^2 + (-1)^2} = \sqrt{2}$.
*   The point is in the fourth quadrant. The principal argument ($-\pi < \theta \le \pi$) is:
    $\theta = \tan^{-1}(-1/1) = -\pi/4$.

**Step 2: Determine all values using the formula from Part (a).**
$$\ln(1-i) = \ln(\sqrt{2}) + i\left(-\frac{\pi}{4} + 2k\pi\right) \quad \text{for } k=0, \pm1, \dots$$
Using logarithm properties $\ln(\sqrt{2}) = \ln(2^{1/2}) = \frac{1}{2}\ln 2$:
**Values:** **$\frac{1}{2}\ln 2 + i\left(-\frac{\pi}{4} + 2k\pi\right)$**

**Step 3: Determine the Principal Value.**
The principal value of the complex logarithm, denoted $\text{Ln}(z)$, is obtained by taking $k=0$ (which corresponds to using the principal argument).
**Principal Value:** **$\frac{1}{2}\ln 2 - i\frac{\pi}{4}$**

***

### Q132. Problems 2.1 Question 5: Find $lim_{z\rightarrow e^{\pi i/3}}(z-e^{\pi i/3})(\frac{z}{z^{3}+1})$

**Solution:**

Let $z_0 = e^{\pi i/3}$. We evaluate the limit:
$$L = \lim_{z \to z_0} \frac{z(z - z_0)}{z^3 + 1}$$

**Step 1: Check for direct substitution.**
Numerator: $z_0(z_0 - z_0) = 0$.
Denominator: $z_0^3 + 1 = (e^{\pi i/3})^3 + 1 = e^{\pi i} + 1 = -1 + 1 = 0$.
Form is $0/0$. We will apply L'Hôpital's Rule.

**Step 2: Apply L'Hôpital's Rule.**
Take the derivative of the top and bottom with respect to $z$.
*   Numerator is $z^2 - z_0 z$. Its derivative is $2z - z_0$.
*   Denominator is $z^3 + 1$. Its derivative is $3z^2$.

$$L = \lim_{z \to z_0} \frac{2z - z_0}{3z^2}$$

**Step 3: Evaluate by substitution.**
Substitute $z = z_0$:
$$L = \frac{2z_0 - z_0}{3z_0^2}$$
$$L = \frac{z_0}{3z_0^2}$$
$$L = \frac{1}{3z_0}$$

**Step 4: Substitute $z_0$ back and simplify.**
$$L = \frac{1}{3e^{\pi i/3}}$$
$$L = \frac{1}{3} e^{-\pi i/3}$$

If Cartesian form is needed:
$e^{-\pi i/3} = \cos(-\pi/3) + i\sin(-\pi/3) = \frac{1}{2} - i\frac{\sqrt{3}}{2}$.
$$L = \frac{1}{3} \left(\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = \frac{1}{6} - i\frac{\sqrt{3}}{6}$$

**Answer:** The limit evaluates to **$\frac{1}{3} e^{-\pi i/3}$** (or **$\frac{1}{6} - i\frac{\sqrt{3}}{6}$**).
Here are the detailed solutions for the next four questions (Q133 to Q136).

### Q133. Problems 2.1 Question 6: Prove that If $u(x,y)=y^{3}/(x^{2}+y^{2})$ then $lim_{(x,y)\rightarrow(0,0)}u(x,y)=0$

**Solution:**

We need to prove that the two-variable limit of $u(x,y)$ as it approaches the origin is exactly $0$, regardless of the path taken.

**Method 1: Using Polar Coordinates (The most rigorous and standard method for 2D limits at the origin)**

**Step 1: Convert the function to polar coordinates.**
Let $x = r\cos\theta$ and $y = r\sin\theta$.
As $(x,y) \to (0,0)$, the radius $r \to 0$. The angle $\theta$ can be any value, representing the infinitely many paths to the origin.

Substitute these into $u(x,y)$:
$$u(r, \theta) = \frac{(r\sin\theta)^3}{(r\cos\theta)^2 + (r\sin\theta)^2}$$

**Step 2: Simplify the expression.**
$$u(r, \theta) = \frac{r^3\sin^3\theta}{r^2\cos^2\theta + r^2\sin^2\theta}$$
Factor out $r^2$ in the denominator:
$$u(r, \theta) = \frac{r^3\sin^3\theta}{r^2(\cos^2\theta + \sin^2\theta)}$$
Since $\cos^2\theta + \sin^2\theta = 1$:
$$u(r, \theta) = \frac{r^3\sin^3\theta}{r^2}$$
Cancel $r^2$ (valid since $r \to 0$ means $r \neq 0$ during the limit):
$$u(r, \theta) = r\sin^3\theta$$

**Step 3: Evaluate the limit as $r \to 0$.**
We need to evaluate $\lim_{r \to 0} (r\sin^3\theta)$.
We know that the sine function is bounded: $-1 \le \sin\theta \le 1$, which means $-1 \le \sin^3\theta \le 1$.
Because $\sin^3\theta$ is bounded, multiplying it by $r$ (which is approaching $0$) will force the entire product to approach $0$.
By the Squeeze Theorem:
$$-|r| \le r\sin^3\theta \le |r|$$
As $r \to 0$, both boundaries go to $0$.
Therefore:
$$\lim_{r \to 0} r\sin^3\theta = 0$$

Because this result is $0$ entirely independently of the angle $\theta$, the limit exists and equals $0$ for all possible paths to the origin.
**(Proved)**

---

**Method 2: Using the Squeeze Theorem in Cartesian Coordinates**

**Step 1: Establish a bounding inequality.**
We know that for any real numbers $x$ and $y$ (except both zero), $x^2 \ge 0$.
Therefore, adding $y^2$ to both sides gives:
$$x^2 + y^2 \ge y^2$$
Because $x^2+y^2$ is strictly positive as $(x,y) \to (0,0)$, we can divide both sides by it (and by $y^2$, assuming $y \neq 0$ to establish the bound):
$$1 \ge \frac{y^2}{x^2 + y^2}$$
Since squares are non-negative, we can say:
$$0 \le \frac{y^2}{x^2 + y^2} \le 1$$

**Step 2: Multiply by $|y|$ to reconstruct our function.**
Multiply the entire inequality by $|y|$:
$$0 \le |y| \cdot \frac{y^2}{x^2 + y^2} \le |y|$$
Notice that $|y| \cdot y^2 = |y|^3 = |y^3|$. Also, since $x^2+y^2$ is always positive, we can pull the absolute value across the whole fraction:
$$0 \le \left| \frac{y^3}{x^2 + y^2} \right| \le |y|$$
Which is:
$$0 \le |u(x,y)| \le |y|$$

**Step 3: Apply the limit.**
As $(x,y) \to (0,0)$, clearly $|y| \to 0$.
Taking the limit of all parts of the inequality:
$$\lim_{(x,y)\to(0,0)} 0 \le \lim_{(x,y)\to(0,0)} |u(x,y)| \le \lim_{(x,y)\to(0,0)} |y|$$
$$0 \le \lim_{(x,y)\to(0,0)} |u(x,y)| \le 0$$
By the Squeeze Theorem, the limit of $|u(x,y)|$ must be exactly $0$. If the absolute value of a function goes to $0$, the function itself must go to $0$.
$$\lim_{(x,y)\to(0,0)} u(x,y) = 0$$
**(Proved)**

***

### Q134. Pg 1, Q2(a): Show that $f(z) = |z|^2$ is differentiable at $z=0$ but not analytic at $z=0$.

**Solution:**

We must show two distinct things: first, that the derivative exists at $z=0$, and second, that it is not analytic there.

**Part 1: Show it is differentiable at $z=0$**
By definition, a complex function $f(z)$ is differentiable at $z_0$ if the limit $\lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$ exists.
Here, $z_0 = 0$.
The limit expression is:
$$\lim_{\Delta z \to 0} \frac{f(0 + \Delta z) - f(0)}{\Delta z} = \lim_{\Delta z \to 0} \frac{f(\Delta z) - 0}{\Delta z}$$
Substitute $f(z) = |z|^2$:
$$= \lim_{\Delta z \to 0} \frac{|\Delta z|^2}{\Delta z}$$
We use the property that $|w|^2 = w\overline{w}$. Therefore, $|\Delta z|^2 = \Delta z \overline{\Delta z}$.
$$= \lim_{\Delta z \to 0} \frac{\Delta z \overline{\Delta z}}{\Delta z}$$
Cancel the $\Delta z$ terms:
$$= \lim_{\Delta z \to 0} \overline{\Delta z}$$
As $\Delta z \to 0$, its complex conjugate $\overline{\Delta z}$ also clearly goes to $0$.
So, $f'(0) = 0$.
Because this limit exists and evaluates to a single finite number ($0$) regardless of the path $\Delta z$ takes, **the function is differentiable at $z=0$.**

---

**Part 2: Show it is not analytic at $z=0$**
By definition, a function is **analytic** at a point $z_0$ if it is differentiable not only at $z_0$, but *also in some neighborhood (some surrounding open disk)* around $z_0$.
To test if it's differentiable anywhere else, we use the Cauchy-Riemann equations.

Let $z = x + iy$.
$$f(z) = |z|^2 = x^2 + y^2$$
This function is purely real. We can separate it into $u(x,y) + iv(x,y)$:
*   $u(x,y) = x^2 + y^2$
*   $v(x,y) = 0$

Calculate the partial derivatives:
*   $u_x = \frac{\partial u}{\partial x} = 2x$
*   $u_y = \frac{\partial u}{\partial y} = 2y$
*   $v_x = \frac{\partial v}{\partial x} = 0$
*   $v_y = \frac{\partial v}{\partial y} = 0$

Check the Cauchy-Riemann equations:
1) $u_x = v_y \implies 2x = 0 \implies x = 0$
2) $u_y = -v_x \implies 2y = 0 \implies y = 0$

The Cauchy-Riemann equations are *only* satisfied at the single isolated point $(0,0)$ (which corresponds to $z=0$). They are not satisfied anywhere else in the complex plane.
Since the function is not differentiable in any neighborhood surrounding $z=0$, **it is not analytic at $z=0$.** (Proved)

***

### Q135. Pg 1, Q2(b): Prove that $u = 2x(1-y)$ is a harmonic function and find v such that $f(z) = u+iv$ becomes an analytic function.

**Solution:**

**Part 1: Prove $u$ is harmonic.**
A function $u(x,y)$ is harmonic if it satisfies Laplace's equation: $\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$.

Given: $u(x,y) = 2x - 2xy$.
Calculate first partial derivatives:
*   $u_x = \frac{\partial}{\partial x}(2x - 2xy) = 2 - 2y$
*   $u_y = \frac{\partial}{\partial y}(2x - 2xy) = -2x$

Calculate second partial derivatives:
*   $u_{xx} = \frac{\partial}{\partial x}(2 - 2y) = 0$
*   $u_{yy} = \frac{\partial}{\partial y}(-2x) = 0$

Check Laplace's equation:
$u_{xx} + u_{yy} = 0 + 0 = 0$.
Since Laplace's equation is satisfied everywhere, **$u$ is a harmonic function.** (Proved)

---

**Part 2: Find the harmonic conjugate $v(x,y)$.**
For $f(z) = u + iv$ to be analytic, $u$ and $v$ must satisfy the Cauchy-Riemann equations:
1) $u_x = v_y$
2) $u_y = -v_x$

**Step 1: Use the first C-R equation.**
$v_y = u_x$
$v_y = 2 - 2y$

**Step 2: Integrate with respect to $y$.**
Integrate $v_y$ partially with respect to $y$ to find $v$:
$$v(x,y) = \int (2 - 2y) dy$$
$$v(x,y) = 2y - y^2 + g(x)$$
where $g(x)$ is an arbitrary function of $x$ (the "constant" of partial integration).

**Step 3: Use the second C-R equation to find $g(x)$.**
Differentiate our new $v(x,y)$ partially with respect to $x$:
$v_x = \frac{\partial}{\partial x}(2y - y^2 + g(x)) = g'(x)$

Now substitute this into the second C-R equation ($u_y = -v_x$):
$u_y = -2x$ (from Part 1 calculations)
So, $-2x = -g'(x)$
$g'(x) = 2x$

**Step 4: Integrate to find $g(x)$.**
Integrate $g'(x)$ with respect to $x$:
$g(x) = \int 2x dx = x^2 + C$ (where $C$ is a real constant).

**Step 5: Write the final function $v$.**
Substitute $g(x)$ back into our equation for $v$:
$$v(x,y) = 2y - y^2 + x^2 + C$$

**Answer:** The harmonic conjugate is **$v(x,y) = x^2 - y^2 + 2y + C$**. 
*(The analytic function is $f(z) = (2x - 2xy) + i(x^2 - y^2 + 2y + C)$).*

***

### Q136. Pg 1, Q2(c): In a two dimensional flow, the stream function is $\psi = \tan^{-1}(y/x)$. Find the velocity potential $\phi$ if $f(z) = \phi(x,y) + i\psi(x,y)$ is analytic.

*(Note: The standard complex potential function is defined as $F(z) = \phi + i\psi$. If this function is analytic, $\phi$ and $\psi$ must satisfy the Cauchy-Riemann equations).*

**Solution:**

We are given the imaginary part $\psi(x,y) = \tan^{-1}(y/x)$. We need to find its harmonic conjugate, the real part $\phi(x,y)$.
Because $F(z) = \phi + i\psi$ is analytic, the Cauchy-Riemann equations apply:
1) $\phi_x = \psi_y$
2) $\phi_y = -\psi_x$

**Step 1: Calculate the partial derivatives of $\psi$.**
$$\psi = \tan^{-1}\left(\frac{y}{x}\right)$$
Recall the chain rule for arctangent: $\frac{d}{du}\tan^{-1}(u) = \frac{1}{1+u^2} \cdot u'$.

*   Calculate $\psi_x$:
    $$\psi_x = \frac{\partial}{\partial x}\tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1 + (y/x)^2} \cdot \frac{\partial}{\partial x}\left(y \cdot x^{-1}\right)$$
    $$\psi_x = \frac{1}{1 + \frac{y^2}{x^2}} \cdot \left(-yx^{-2}\right) = \frac{x^2}{x^2 + y^2} \cdot \left(-\frac{y}{x^2}\right) = -\frac{y}{x^2 + y^2}$$

*   Calculate $\psi_y$:
    $$\psi_y = \frac{\partial}{\partial y}\tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1 + (y/x)^2} \cdot \frac{\partial}{\partial y}\left(\frac{y}{x}\right)$$
    $$\psi_y = \frac{x^2}{x^2 + y^2} \cdot \left(\frac{1}{x}\right) = \frac{x}{x^2 + y^2}$$

**Step 2: Use the first C-R equation.**
From C-R equation 1: $\phi_x = \psi_y$.
$$\phi_x = \frac{x}{x^2 + y^2}$$

**Step 3: Integrate with respect to $x$.**
Integrate $\phi_x$ partially with respect to $x$ to find $\phi$:
$$\phi(x,y) = \int \frac{x}{x^2 + y^2} dx$$
Let $u = x^2 + y^2$, then $du = 2x dx$, so $x dx = \frac{1}{2} du$.
$$\phi(x,y) = \frac{1}{2} \int \frac{1}{u} du = \frac{1}{2} \ln(u) + g(y)$$
$$\phi(x,y) = \frac{1}{2} \ln(x^2 + y^2) + g(y)$$
where $g(y)$ is an arbitrary function of $y$.

**Step 4: Use the second C-R equation to find $g(y)$.**
Differentiate our new $\phi(x,y)$ partially with respect to $y$:
$$\phi_y = \frac{\partial}{\partial y} \left( \frac{1}{2} \ln(x^2 + y^2) + g(y) \right)$$
Using the chain rule:
$$\phi_y = \frac{1}{2} \cdot \frac{1}{x^2 + y^2} \cdot (2y) + g'(y)$$
$$\phi_y = \frac{y}{x^2 + y^2} + g'(y)$$

Now substitute this into the second C-R equation ($\phi_y = -\psi_x$):
We know from Step 1 that $-\psi_x = -\left(-\frac{y}{x^2+y^2}\right) = \frac{y}{x^2+y^2}$.
So:
$$\frac{y}{x^2 + y^2} + g'(y) = \frac{y}{x^2 + y^2}$$
$$g'(y) = 0$$

**Step 5: Find $g(y)$ and write the final function.**
Integrating $g'(y) = 0$ gives $g(y) = C$ (a real constant).
Substitute this back into the equation for $\phi$:
$$\phi(x,y) = \frac{1}{2} \ln(x^2 + y^2) + C$$

**Answer:** The velocity potential is **$\phi(x,y) = \frac{1}{2} \ln(x^2 + y^2) + C$**.
*(Notice that this corresponds to the complex potential $F(z) = \ln(z) + C$).*


Here are the detailed solutions for the next four questions (Q137 to Q140).

### Q137. Pg 2, Q2(a): Prove that the real and imaginary parts of an analytic function satisfy Laplace's equation.

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function in some region $R$. 
To prove that $u$ and $v$ satisfy Laplace's equation, we must show that $\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ and $\nabla^2 v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$.

**Step 1: State the Cauchy-Riemann (C-R) equations.**
Because $f(z)$ is analytic, its real part $u$ and imaginary part $v$ must satisfy the C-R equations throughout $R$:
1.  $u_x = v_y \quad$ (or $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$)
2.  $u_y = -v_x \quad$ (or $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$)

Additionally, a fundamental theorem of complex analysis states that if a function is analytic, it is infinitely differentiable, which guarantees that all second-order (and higher) partial derivatives of $u$ and $v$ exist and are continuous.

**Step 2: Prove that $u(x,y)$ satisfies Laplace's equation.**
Take the partial derivative of the first C-R equation with respect to $x$:
$$\frac{\partial}{\partial x}(u_x) = \frac{\partial}{\partial x}(v_y) \implies u_{xx} = v_{yx}$$

Take the partial derivative of the second C-R equation with respect to $y$:
$$\frac{\partial}{\partial y}(u_y) = \frac{\partial}{\partial y}(-v_x) \implies u_{yy} = -v_{xy}$$

Add the two resulting equations together:
$$u_{xx} + u_{yy} = v_{yx} - v_{xy}$$

Because the mixed partial derivatives of continuous functions are equal (Clairaut's Theorem), $v_{yx} = v_{xy}$. Therefore, their difference is zero:
$$u_{xx} + u_{yy} = 0$$
Thus, $u(x,y)$ satisfies Laplace's equation. **(Proved for $u$)**

**Step 3: Prove that $v(x,y)$ satisfies Laplace's equation.**
Take the partial derivative of the first C-R equation with respect to $y$:
$$\frac{\partial}{\partial y}(u_x) = \frac{\partial}{\partial y}(v_y) \implies u_{xy} = v_{yy}$$

Take the partial derivative of the second C-R equation with respect to $x$:
$$\frac{\partial}{\partial x}(u_y) = \frac{\partial}{\partial x}(-v_x) \implies u_{yx} = -v_{xx}$$

Rearrange the second result:
$$v_{xx} = -u_{yx}$$

Add the two equations together:
$$v_{xx} + v_{yy} = -u_{yx} + u_{xy}$$

Again, by Clairaut's Theorem, mixed partial derivatives are equal ($u_{yx} = u_{xy}$), so:
$$v_{xx} + v_{yy} = 0$$
Thus, $v(x,y)$ satisfies Laplace's equation. **(Proved for $v$)**

**(Conclusion: Both the real and imaginary parts of an analytic function are harmonic functions.)**

***

### Q138. Pg 2, Q2(b): Show that the function $u = \frac{1}{2}\log(x^2+y^2)$ is harmonic and find v such that $f(z) = u+iv$ is analytic.

*(Note: "log" here typically denotes the natural logarithm $\ln$ in complex analysis texts).*

**Solution:**

Given $u(x,y) = \frac{1}{2}\ln(x^2 + y^2)$.

**Part 1: Show $u$ is harmonic.**
We must show $u_{xx} + u_{yy} = 0$.

*   **Find first derivatives:**
    $$u_x = \frac{\partial}{\partial x} \left[ \frac{1}{2}\ln(x^2+y^2) \right] = \frac{1}{2} \cdot \frac{1}{x^2+y^2} \cdot (2x) = \frac{x}{x^2+y^2}$$
    $$u_y = \frac{\partial}{\partial y} \left[ \frac{1}{2}\ln(x^2+y^2) \right] = \frac{1}{2} \cdot \frac{1}{x^2+y^2} \cdot (2y) = \frac{y}{x^2+y^2}$$

*   **Find second derivatives (using quotient rule $\frac{u'v-uv'}{v^2}$):**
    $$u_{xx} = \frac{\partial}{\partial x} \left[ \frac{x}{x^2+y^2} \right] = \frac{(1)(x^2+y^2) - (x)(2x)}{(x^2+y^2)^2} = \frac{x^2+y^2-2x^2}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}$$
    
    $$u_{yy} = \frac{\partial}{\partial y} \left[ \frac{y}{x^2+y^2} \right] = \frac{(1)(x^2+y^2) - (y)(2y)}{(x^2+y^2)^2} = \frac{x^2+y^2-2y^2}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2}$$

*   **Check Laplace's equation:**
    $$u_{xx} + u_{yy} = \frac{y^2-x^2}{(x^2+y^2)^2} + \frac{x^2-y^2}{(x^2+y^2)^2} = \frac{y^2-x^2+x^2-y^2}{(x^2+y^2)^2} = \frac{0}{(x^2+y^2)^2} = 0$$
    Since $u_{xx} + u_{yy} = 0$, $u$ is a **harmonic function**. (Proved)

---

**Part 2: Find the harmonic conjugate $v(x,y)$.**
We use the Cauchy-Riemann equations: $u_x = v_y$ and $u_y = -v_x$.

*   **Step 1:** From $u_x = v_y$, we have:
    $$v_y = \frac{x}{x^2+y^2}$$
*   **Step 2:** Integrate with respect to $y$:
    $$v(x,y) = \int \frac{x}{x^2+y^2} dy$$
    Recall the standard integral form $\int \frac{a}{a^2+y^2} dy = \tan^{-1}\left(\frac{y}{a}\right)$. Here, $a=x$.
    $$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + g(x)$$
*   **Step 3:** Use the second C-R equation. Differentiate $v$ with respect to $x$:
    $$v_x = \frac{\partial}{\partial x} \left[ \tan^{-1}\left(\frac{y}{x}\right) + g(x) \right] = \frac{1}{1+(y/x)^2} \cdot \left(-\frac{y}{x^2}\right) + g'(x)$$
    $$v_x = \frac{x^2}{x^2+y^2} \cdot \left(-\frac{y}{x^2}\right) + g'(x) = -\frac{y}{x^2+y^2} + g'(x)$$
*   **Step 4:** Substitute into $u_y = -v_x$:
    From Part 1, we know $u_y = \frac{y}{x^2+y^2}$.
    $$\frac{y}{x^2+y^2} = -\left( -\frac{y}{x^2+y^2} + g'(x) \right)$$
    $$\frac{y}{x^2+y^2} = \frac{y}{x^2+y^2} - g'(x)$$
    $$g'(x) = 0 \implies g(x) = C \text{ (a constant)}$$

**Answer:** The harmonic conjugate is **$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + C$**.
*(Note: $f(z) = u+iv = \ln|z| + i\arg(z) = \ln(z)$).*

***

### Q139. Pg 2, Q2(c): Define analytic function. Show that $\frac{d}{dz}(\bar{z})$ does not exists anywhere.

**Solution:**

**Part 1: Define Analytic Function**
A complex function $f(z)$ is said to be **analytic** at a point $z_0$ if its derivative $f'(z)$ exists not only at the point $z_0$ itself, but also exists at every point in some neighborhood (an open disk) surrounding $z_0$.
If a function is analytic at every point in a region $R$, it is said to be analytic in $R$. (If it's analytic in the entire complex plane, it's called an *entire function*).

---

**Part 2: Show that $\frac{d}{dz}(\bar{z})$ does not exist anywhere.**
Let $f(z) = \bar{z}$. We want to evaluate its derivative using the fundamental limit definition:
$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

**Step 1: Substitute $f(z) = \bar{z}$ into the definition.**
$$f'(z) = \lim_{\Delta z \to 0} \frac{\overline{(z + \Delta z)} - \bar{z}}{\Delta z}$$
Using the property of conjugates $\overline{A+B} = \overline{A} + \overline{B}$:
$$f'(z) = \lim_{\Delta z \to 0} \frac{\bar{z} + \overline{\Delta z} - \bar{z}}{\Delta z}$$
$$f'(z) = \lim_{\Delta z \to 0} \frac{\overline{\Delta z}}{\Delta z}$$

**Step 2: Evaluate the limit along two different paths.**
For the derivative to exist, this limit must approach a single unique value regardless of the path $\Delta z$ takes as it approaches $0$.
Let $\Delta z = \Delta x + i\Delta y$. Then $\overline{\Delta z} = \Delta x - i\Delta y$.
The limit is: $\lim_{(\Delta x, \Delta y) \to (0,0)} \frac{\Delta x - i\Delta y}{\Delta x + i\Delta y}$

*   **Path 1: Approach along the real axis.**
    Set $\Delta y = 0$ and let $\Delta x \to 0$.
    $$L_1 = \lim_{\Delta x \to 0} \frac{\Delta x - i(0)}{\Delta x + i(0)} = \lim_{\Delta x \to 0} \frac{\Delta x}{\Delta x} = 1$$

*   **Path 2: Approach along the imaginary axis.**
    Set $\Delta x = 0$ and let $\Delta y \to 0$.
    $$L_2 = \lim_{\Delta y \to 0} \frac{0 - i\Delta y}{0 + i\Delta y} = \lim_{\Delta y \to 0} \frac{-i\Delta y}{i\Delta y} = -1$$

**Step 3: Conclusion.**
Because the limit yields different results depending on the path taken ($1 \neq -1$), the limit does not exist. Since the limit definition of the derivative fails at every point $z$, the derivative $\frac{d}{dz}(\bar{z})$ **does not exist anywhere**. (Proved)

*(Alternatively, checking C-R equations for $f(z) = x-iy \implies u=x, v=-y \implies u_x=1, v_y=-1$. Since $u_x \neq v_y$ everywhere, it is nowhere differentiable).*

***

### Q140. Pg 4, Q2(a): State and prove necessary and sufficient condition for Cauchy-Riemann equations.

*(Note: The standard phrasing for this theorem is "State and prove the necessary condition for a function to be differentiable (or analytic) at a point". The C-R equations ARE the conditions. We will provide the standard proof that if a function is differentiable, the C-R equations must hold).*

**Solution:**

**Statement (Necessary Condition for Differentiability):**
If a complex function $f(z) = u(x,y) + iv(x,y)$ is differentiable at a point $z_0 = x_0 + iy_0$, then the first-order partial derivatives of $u$ and $v$ with respect to $x$ and $y$ must exist at $(x_0, y_0)$ and they must satisfy the Cauchy-Riemann equations:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

**Proof:**
Assume $f(z)$ is differentiable at $z$. By definition, the limit for the derivative exists and is unique regardless of the path $\Delta z$ takes approaching $0$:
$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$
Let $z = x+iy$ and $\Delta z = \Delta x + i\Delta y$.
$$f(z+\Delta z) = u(x+\Delta x, y+\Delta y) + iv(x+\Delta x, y+\Delta y)$$

**Case 1: Let $\Delta z \to 0$ strictly along the real axis.**
This means $\Delta y = 0$ and $\Delta x \to 0$. Thus, $\Delta z = \Delta x$.
Substitute this into the limit definition:
$$f'(z) = \lim_{\Delta x \to 0} \frac{[u(x+\Delta x, y) + iv(x+\Delta x, y)] - [u(x,y) + iv(x,y)]}{\Delta x}$$
Separate real and imaginary parts:
$$f'(z) = \lim_{\Delta x \to 0} \frac{u(x+\Delta x, y) - u(x,y)}{\Delta x} + i \lim_{\Delta x \to 0} \frac{v(x+\Delta x, y) - v(x,y)}{\Delta x}$$
By the standard definition of partial derivatives in real calculus, these limits are exactly $\frac{\partial u}{\partial x}$ and $\frac{\partial v}{\partial x}$.
$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} \quad \text{--- (Equation 1)}$$

**Case 2: Let $\Delta z \to 0$ strictly along the imaginary axis.**
This means $\Delta x = 0$ and $\Delta y \to 0$. Thus, $\Delta z = i\Delta y$.
Substitute this into the limit definition:
$$f'(z) = \lim_{\Delta y \to 0} \frac{[u(x, y+\Delta y) + iv(x, y+\Delta y)] - [u(x,y) + iv(x,y)]}{i\Delta y}$$
Separate real and imaginary parts:
$$f'(z) = \lim_{\Delta y \to 0} \frac{u(x, y+\Delta y) - u(x,y)}{i\Delta y} + \lim_{\Delta y \to 0} \frac{i[v(x, y+\Delta y) - v(x,y)]}{i\Delta y}$$
Pull the $1/i$ out of the first term (note $1/i = -i$), and cancel $i$ in the second term:
$$f'(z) = -i \lim_{\Delta y \to 0} \frac{u(x, y+\Delta y) - u(x,y)}{\Delta y} + \lim_{\Delta y \to 0} \frac{v(x, y+\Delta y) - v(x,y)}{\Delta y}$$
Identify the partial derivatives:
$$f'(z) = -i\frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}$$
Rearrange to standard form:
$$f'(z) = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y} \quad \text{--- (Equation 2)}$$

**Conclusion:**
Since $f(z)$ is differentiable, the derivative $f'(z)$ must be unique. Therefore, Equation 1 must equal Equation 2:
$$\frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}$$
For two complex expressions to be equal, their real parts must match and their imaginary parts must match.
Equating real parts:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
Equating imaginary parts:
$$\frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}$$
These are exactly the Cauchy-Riemann equations. **(Proved)**



Here are the detailed solutions for the next four questions (Q141 to Q144).

### Q141. Pg 6, Q2(b): Find the orthogonal trajectories of the family of curves $e^{-x}\cos y + xy = \alpha$

*(Note: In complex analysis, if a family of curves is defined by $u(x,y) = c_1$ where $u$ is the real part of an analytic function, its orthogonal trajectories are given by $v(x,y) = c_2$, where $v$ is the harmonic conjugate of $u$. We will verify $u$ is harmonic and find $v$).*

**Solution:**

Let $u(x,y) = e^{-x}\cos y + xy$. We need to find its harmonic conjugate $v(x,y)$. The curves $v(x,y) = \beta$ will be the orthogonal trajectories to $u(x,y) = \alpha$.

**Step 1: Calculate the first partial derivatives of $u$.**
*   $u_x = \frac{\partial}{\partial x}(e^{-x}\cos y + xy) = -e^{-x}\cos y + y$
*   $u_y = \frac{\partial}{\partial y}(e^{-x}\cos y + xy) = -e^{-x}\sin y + x$

*(Optional but good practice: Verify $u$ is harmonic. $u_{xx} = e^{-x}\cos y$ and $u_{yy} = -e^{-x}\cos y$. Indeed, $u_{xx} + u_{yy} = 0$).*

**Step 2: Use the Cauchy-Riemann equations to find $v_x$ and $v_y$.**
The C-R equations are $u_x = v_y$ and $u_y = -v_x$.
*   From $v_y = u_x$: $v_y = -e^{-x}\cos y + y$
*   From $v_x = -u_y$: $v_x = -(-e^{-x}\sin y + x) = e^{-x}\sin y - x$

**Step 3: Integrate $v_y$ with respect to $y$ to find $v(x,y)$.**
$$v(x,y) = \int (-e^{-x}\cos y + y) dy$$
Treat $x$ as a constant:
$$v(x,y) = -e^{-x}\sin y + \frac{y^2}{2} + g(x)$$
where $g(x)$ is an arbitrary function of $x$.

**Step 4: Differentiate the result with respect to $x$ to find $g(x)$.**
$$v_x = \frac{\partial}{\partial x} \left( -e^{-x}\sin y + \frac{y^2}{2} + g(x) \right)$$
$$v_x = e^{-x}\sin y + 0 + g'(x)$$

**Step 5: Equate to the $v_x$ found in Step 2.**
$$e^{-x}\sin y + g'(x) = e^{-x}\sin y - x$$
Subtract $e^{-x}\sin y$ from both sides:
$$g'(x) = -x$$

**Step 6: Integrate $g'(x)$ to find $g(x)$.**
$$g(x) = \int -x dx = -\frac{x^2}{2} + C$$

**Step 7: Write the final function $v(x,y)$.**
Substitute $g(x)$ back into the expression for $v$ from Step 3:
$$v(x,y) = -e^{-x}\sin y + \frac{y^2}{2} - \frac{x^2}{2} + C$$

The orthogonal trajectories are represented by setting $v(x,y)$ to an arbitrary constant $\beta$. (We can absorb $C$ into $\beta$).

**Answer:** The orthogonal trajectories are given by the family of curves:
**$-e^{-x}\sin y + \frac{y^2 - x^2}{2} = \beta$** (where $\beta$ is a real constant).

***

### Q142. Pg 13, CT-04, 2.(a): If $v = x^2-y^2-a^2$, find u such that $f(z) = u+iv$ is analytic. Aso find $f(z)$ interms of z.

*(Note: There is a likely typo in the given $v$. The function $x^2-y^2$ is harmonic, but it's usually the real part $u$ for $f(z)=z^2$. However, we will solve it exactly as written. If $v = x^2-y^2-a^2$, then $f(z) = i(x^2-y^2) + \dots = iz^2 + \dots$ Let's proceed).*

**Solution:**

We are given the imaginary part $v(x,y) = x^2 - y^2 - a^2$. We need to find the real part $u(x,y)$ using the Cauchy-Riemann equations: $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Calculate the partial derivatives of $v$.**
*   $v_x = \frac{\partial}{\partial x}(x^2 - y^2 - a^2) = 2x$
*   $v_y = \frac{\partial}{\partial y}(x^2 - y^2 - a^2) = -2y$

**Step 2: Use the C-R equations to find $u_x$ and $u_y$.**
*   From $u_x = v_y$: $u_x = -2y$
*   From $u_y = -v_x$: $u_y = -2x$

**Step 3: Integrate $u_x$ with respect to $x$ to find $u(x,y)$.**
$$u(x,y) = \int (-2y) dx$$
Treat $y$ as a constant:
$$u(x,y) = -2xy + h(y)$$
where $h(y)$ is an arbitrary function of $y$.

**Step 4: Differentiate the result with respect to $y$ to find $h(y)$.**
$$u_y = \frac{\partial}{\partial y}(-2xy + h(y)) = -2x + h'(y)$$

**Step 5: Equate to the $u_y$ found in Step 2.**
$$-2x + h'(y) = -2x$$
$$h'(y) = 0$$

**Step 6: Integrate $h'(y)$.**
$$h(y) = C$$ (where $C$ is a real constant).

**Step 7: Write the final function $u(x,y)$.**
$$u(x,y) = -2xy + C$$

---
**Part 2: Find $f(z)$ in terms of $z$.**

We construct the analytic function $f(z) = u + iv$:
$$f(z) = (-2xy + C) + i(x^2 - y^2 - a^2)$$

To express this in terms of $z$, we can use the **Milne-Thomson method**.
We evaluate $f(z)$ by setting $x = z$ and $y = 0$.
$$f(z) = (-2(z)(0) + C) + i(z^2 - 0^2 - a^2)$$
$$f(z) = C + i(z^2 - a^2)$$
$$f(z) = iz^2 - ia^2 + C$$

*(Alternative algebraic check:
$f(z) = i(x^2 - y^2 + 2ixy) - ia^2 + C = i(x^2 + 2ixy - y^2) - ia^2 + C = i(x+iy)^2 - ia^2 + C = iz^2 - ia^2 + C$. Matches perfectly).*

**Answer:**
*   **$u(x,y) = -2xy + C$**
*   **$f(z) = iz^2 - ia^2 + C$**

***

### Q143. Pg 15, CT-04, 2.(a): If $v = \tan^{-1}(y/x)$, find u such that $f(z) = u+iv$ is analytic. Aso find $f(z)$ interms of z.

*(Note: This is the exact inverse setup of Q136, where $\psi = \tan^{-1}(y/x)$ was the imaginary part. We will re-derive it here).*

**Solution:**

Given imaginary part $v(x,y) = \tan^{-1}(y/x)$. We find real part $u(x,y)$ using C-R equations $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Calculate the partial derivatives of $v$.**
Using chain rule $\frac{d}{dw}\tan^{-1}w = \frac{1}{1+w^2}$:
*   $v_x = \frac{1}{1+(y/x)^2} \cdot \left(\frac{-y}{x^2}\right) = \frac{x^2}{x^2+y^2} \cdot \left(\frac{-y}{x^2}\right) = -\frac{y}{x^2+y^2}$
*   $v_y = \frac{1}{1+(y/x)^2} \cdot \left(\frac{1}{x}\right) = \frac{x^2}{x^2+y^2} \cdot \left(\frac{1}{x}\right) = \frac{x}{x^2+y^2}$

**Step 2: Use C-R equations for $u_x$ and $u_y$.**
*   $u_x = v_y \implies u_x = \frac{x}{x^2+y^2}$
*   $u_y = -v_x \implies u_y = -\left(-\frac{y}{x^2+y^2}\right) = \frac{y}{x^2+y^2}$

**Step 3: Integrate $u_x$ with respect to $x$.**
$$u(x,y) = \int \frac{x}{x^2+y^2} dx$$
Let substitution $w = x^2+y^2 \implies dw = 2xdx \implies \frac{1}{2}dw = xdx$.
$$u(x,y) = \frac{1}{2}\ln(x^2+y^2) + h(y)$$

**Step 4: Differentiate with respect to $y$ and solve for $h(y)$.**
$$u_y = \frac{\partial}{\partial y}\left(\frac{1}{2}\ln(x^2+y^2) + h(y)\right) = \frac{1}{2}\frac{1}{x^2+y^2}(2y) + h'(y) = \frac{y}{x^2+y^2} + h'(y)$$
Equate to $u_y$ from Step 2:
$$\frac{y}{x^2+y^2} + h'(y) = \frac{y}{x^2+y^2} \implies h'(y) = 0 \implies h(y) = C$$
Thus, $u(x,y) = \frac{1}{2}\ln(x^2+y^2) + C$.

---
**Part 2: Find $f(z)$ in terms of $z$.**

Construct the function:
$$f(z) = u + iv = \left(\frac{1}{2}\ln(x^2+y^2) + C\right) + i\tan^{-1}(y/x)$$

**Using Milne-Thomson method:**
Set $x = z$ and $y = 0$.
$$f(z) = \frac{1}{2}\ln(z^2 + 0^2) + C + i\tan^{-1}(0/z)$$
$$f(z) = \frac{1}{2}\ln(z^2) + C + i(0)$$
Using log properties $\ln(z^2) = 2\ln(z)$:
$$f(z) = \frac{1}{2}(2\ln z) + C$$
$$f(z) = \ln z + C$$

**Answer:**
*   **$u(x,y) = \frac{1}{2}\ln(x^2+y^2) + C$**
*   **$f(z) = \ln z + C$**

***

### Q144. Pg 17, CT-II, 2.(a): If $u = \frac{1}{2}\log(x^2-y^2)$, find v such that $f(z) = u+iv$ is analytic. Aso find $f(z)$ interms of z

*(Note: The function $u = \frac{1}{2}\log(x^2-y^2)$ is NOT harmonic everywhere. Let's check it: $u_{xx} = -\frac{x^2+y^2}{(x^2-y^2)^2}$ and $u_{yy} = -\frac{x^2+y^2}{(x^2-y^2)^2}$, so $u_{xx}+u_{yy} \neq 0$. This is almost certainly a severe typo in the original exam paper for $u = \frac{1}{2}\log(x^2+y^2)$. Since Q138 explicitly covers $x^2+y^2$, and $x^2-y^2$ cannot yield an analytic function via standard integration, I will solve the mathematically sound corrected version: **$u = \frac{1}{2}\log(x^2+y^2)$**).*

**Solution (for corrected $u = \frac{1}{2}\ln(x^2+y^2)$):**

Given $u(x,y) = \frac{1}{2}\ln(x^2+y^2)$. We need to find $v(x,y)$ using C-R equations $v_y = u_x$ and $v_x = -u_y$.

**Step 1: Calculate partial derivatives of $u$.**
*   $u_x = \frac{x}{x^2+y^2}$
*   $u_y = \frac{y}{x^2+y^2}$

**Step 2: Use C-R equations.**
*   $v_y = u_x = \frac{x}{x^2+y^2}$
*   $v_x = -u_y = -\frac{y}{x^2+y^2}$

**Step 3: Integrate $v_y$ with respect to $y$.**
$$v(x,y) = \int \frac{x}{x^2+y^2} dy$$
Using standard integration $\int \frac{a}{a^2+y^2} dy = \tan^{-1}(y/a)$:
$$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + g(x)$$

**Step 4: Differentiate with respect to $x$ and solve for $g(x)$.**
$$v_x = \frac{\partial}{\partial x}\left(\tan^{-1}(y/x) + g(x)\right) = -\frac{y}{x^2+y^2} + g'(x)$$
Equate to $v_x$ from Step 2:
$$-\frac{y}{x^2+y^2} + g'(x) = -\frac{y}{x^2+y^2} \implies g'(x) = 0 \implies g(x) = C$$
Thus, $v(x,y) = \tan^{-1}(y/x) + C$.

---
**Part 2: Find $f(z)$ in terms of $z$.**

Construct the function:
$$f(z) = u + iv = \frac{1}{2}\ln(x^2+y^2) + i\left(\tan^{-1}(y/x) + C\right)$$

**Using Milne-Thomson method:**
Set $x = z$ and $y = 0$.
$$f(z) = \frac{1}{2}\ln(z^2) + i(\tan^{-1}(0) + C)$$
$$f(z) = \ln z + iC$$

**Answer (assuming corrected typo):**
*   **$v(x,y) = \tan^{-1}(y/x) + C_1$**
*   **$f(z) = \ln z + iC_1$**
*(If the question strictly requires solving $x^2-y^2$, no analytic function exists because it is not a harmonic function).*
Here are the detailed solutions for the next four questions (Q145 to Q148).

### Q145. Pg 19, CT-II, 2.(a): If $v = 2y + x^2 - y^2$, find u such that $f(z) = u+iv$ is analytic. Aso find $f(z)$ interms of z.

**Solution:**

We are given the imaginary part $v(x,y) = x^2 - y^2 + 2y$ of an analytic function $f(z) = u + iv$. We need to find the real part $u(x,y)$ using the Cauchy-Riemann (C-R) equations: $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Calculate the partial derivatives of $v$.**
*   $v_x = \frac{\partial}{\partial x}(x^2 - y^2 + 2y) = 2x$
*   $v_y = \frac{\partial}{\partial y}(x^2 - y^2 + 2y) = -2y + 2$

**Step 2: Use the C-R equations to establish $u_x$ and $u_y$.**
*   From $u_x = v_y$, we get: $u_x = -2y + 2$
*   From $u_y = -v_x$, we get: $u_y = -2x$

**Step 3: Integrate $u_x$ with respect to $x$ to find $u(x,y)$.**
$$u(x,y) = \int (-2y + 2) dx$$
Since we are integrating with respect to $x$, treat $y$ as a constant:
$$u(x,y) = -2xy + 2x + h(y)$$
where $h(y)$ is an arbitrary function of $y$.

**Step 4: Differentiate the result with respect to $y$ and solve for $h(y)$.**
$$u_y = \frac{\partial}{\partial y}(-2xy + 2x + h(y))$$
$$u_y = -2x + 0 + h'(y) = -2x + h'(y)$$

Equate this to the $u_y$ we found in Step 2:
$$-2x + h'(y) = -2x$$
$$h'(y) = 0$$

Integrate $h'(y)$ with respect to $y$:
$$h(y) = C$$ (where $C$ is a real constant).

**Step 5: Write the final function $u(x,y)$.**
Substitute $h(y)$ back into the equation for $u$:
$$u(x,y) = -2xy + 2x + C$$

---
**Part 2: Find $f(z)$ in terms of $z$.**

The function is $f(z) = u + iv$. Substitute the expressions:
$$f(z) = (-2xy + 2x + C) + i(x^2 - y^2 + 2y)$$

**Method 1: Milne-Thomson Method (The easiest approach).**
To express $f(z)$ purely in terms of $z$, we substitute $x = z$ and $y = 0$.
$$f(z) = (-2(z)(0) + 2z + C) + i(z^2 - 0^2 + 2(0))$$
$$f(z) = (2z + C) + i(z^2)$$
Rearranging to standard polynomial form:
$$f(z) = iz^2 + 2z + C$$

**Method 2: Algebraic factoring (To verify).**
Group terms by degrees:
$$f(z) = i(x^2 - y^2) - 2xy + 2x + i2y + C$$
Factor out $i$ from the squared terms:
$$f(z) = i(x^2 - y^2 + 2ixy) + 2(x + iy) + C$$
Recognize the expansion $(x+iy)^2 = x^2 - y^2 + 2ixy$:
$$f(z) = i(x+iy)^2 + 2(x+iy) + C$$
Substitute $z = x+iy$:
$$f(z) = iz^2 + 2z + C$$

**Answer:**
*   **$u(x,y) = -2xy + 2x + C$**
*   **$f(z) = iz^2 + 2z + C$**

***

### Q146. Pg 20, CT-II, 2.(a): Determine whether or not the function $2xy + i(x^2-y^2)$ is analytic

**Solution:**

We are given a complex function $f(z) = u(x,y) + iv(x,y)$ where:
*   Real part: $u(x,y) = 2xy$
*   Imaginary part: $v(x,y) = x^2 - y^2$

To determine if a function is analytic, we must check if its real and imaginary parts satisfy the Cauchy-Riemann (C-R) equations everywhere in the region (typically the entire complex plane). 
The C-R equations are:
1.  $u_x = v_y$
2.  $u_y = -v_x$

**Step 1: Calculate the partial derivatives.**
*   $u_x = \frac{\partial}{\partial x}(2xy) = 2y$
*   $u_y = \frac{\partial}{\partial y}(2xy) = 2x$
*   $v_x = \frac{\partial}{\partial x}(x^2 - y^2) = 2x$
*   $v_y = \frac{\partial}{\partial y}(x^2 - y^2) = -2y$

**Step 2: Check the first C-R equation.**
Does $u_x = v_y$?
$$2y = -2y$$
This equation is only true if $y = 0$. It is not true for all values of $y$. 

**Step 3: Check the second C-R equation.**
Does $u_y = -v_x$?
$$2x = -(2x)$$
$$2x = -2x$$
This equation is only true if $x = 0$. It is not true for all values of $x$.

**Conclusion:**
Because the Cauchy-Riemann equations are only satisfied at the single isolated origin point $(0,0)$ and fail everywhere else in any neighborhood around that point, the function cannot be differentiated in any open region.

**Answer:** The function is **not analytic** anywhere.
*(Note: If the function had been $x^2-y^2 + i(2xy)$, it would have been analytic, equal to $z^2$. By swapping $u$ and $v$, it becomes $i\bar{z}^2$, which is nowhere analytic).*

***

### Q147. Pg 20, CT-II, 2.(b): Find u such that $f(z) = u+iv$ is analytic and if $v = -2xy$

**Solution:**

We are given the imaginary part $v(x,y) = -2xy$. We need to find the harmonic conjugate $u(x,y)$ using the C-R equations $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Calculate the partial derivatives of $v$.**
*   $v_x = \frac{\partial}{\partial x}(-2xy) = -2y$
*   $v_y = \frac{\partial}{\partial y}(-2xy) = -2x$

**Step 2: Set up the C-R equations for $u$.**
*   From $u_x = v_y \implies u_x = -2x$
*   From $u_y = -v_x \implies u_y = -(-2y) = 2y$

**Step 3: Integrate $u_x$ with respect to $x$.**
$$u(x,y) = \int (-2x) dx$$
$$u(x,y) = -x^2 + g(y)$$
where $g(y)$ is an arbitrary function of $y$.

**Step 4: Differentiate with respect to $y$ and solve for $g(y)$.**
$$u_y = \frac{\partial}{\partial y}(-x^2 + g(y)) = g'(y)$$

Equate this to the $u_y$ found in Step 2:
$$g'(y) = 2y$$

Integrate with respect to $y$:
$$g(y) = \int 2y dy = y^2 + C$$
(where $C$ is a real constant).

**Step 5: Write the final function $u(x,y)$.**
Substitute $g(y)$ back into the expression for $u$:
$$u(x,y) = -x^2 + y^2 + C$$

*(Optional check for $f(z)$: $f(z) = (-x^2+y^2+C) + i(-2xy) = -(x^2-y^2+2ixy) + C = -z^2 + C$).*

**Answer:** The real part is **$u(x,y) = -x^2 + y^2 + C$**.

***

### Q148. Pg 21, CT-I, 3.(a): Test analyticity of the function $f(z) = e^{z^2}$

**Solution:**

To test if a function is analytic, we must separate it into its real $u(x,y)$ and imaginary $v(x,y)$ components and verify that they satisfy the Cauchy-Riemann equations and have continuous partial derivatives.

**Step 1: Separate $f(z)$ into $u$ and $v$.**
Let $z = x + iy$.
$$z^2 = (x + iy)^2 = x^2 - y^2 + i2xy$$

Substitute this into the exponential function:
$$f(z) = e^{x^2 - y^2 + i2xy}$$
Use the laws of exponents to separate the real and imaginary powers:
$$f(z) = e^{x^2 - y^2} \cdot e^{i2xy}$$

Use Euler's formula to expand the imaginary exponent term:
$$f(z) = e^{x^2 - y^2} \left[ \cos(2xy) + i\sin(2xy) \right]$$

Distribute to find $u$ and $v$:
*   $u(x,y) = e^{x^2 - y^2} \cos(2xy)$
*   $v(x,y) = e^{x^2 - y^2} \sin(2xy)$

**Step 2: Calculate the partial derivatives using the product and chain rules.**
Let $E = e^{x^2 - y^2}$. Note that $\frac{\partial E}{\partial x} = 2xE$ and $\frac{\partial E}{\partial y} = -2yE$.

*   **Calculate $u_x$:**
    $$u_x = (2xE)\cos(2xy) + E(-\sin(2xy) \cdot 2y)$$
    $$u_x = 2e^{x^2 - y^2} [ x\cos(2xy) - y\sin(2xy) ]$$

*   **Calculate $u_y$:**
    $$u_y = (-2yE)\cos(2xy) + E(-\sin(2xy) \cdot 2x)$$
    $$u_y = -2e^{x^2 - y^2} [ y\cos(2xy) + x\sin(2xy) ]$$

*   **Calculate $v_x$:**
    $$v_x = (2xE)\sin(2xy) + E(\cos(2xy) \cdot 2y)$$
    $$v_x = 2e^{x^2 - y^2} [ x\sin(2xy) + y\cos(2xy) ]$$

*   **Calculate $v_y$:**
    $$v_y = (-2yE)\sin(2xy) + E(\cos(2xy) \cdot 2x)$$
    $$v_y = 2e^{x^2 - y^2} [ -y\sin(2xy) + x\cos(2xy) ]$$
    $$v_y = 2e^{x^2 - y^2} [ x\cos(2xy) - y\sin(2xy) ]$$

**Step 3: Check the Cauchy-Riemann equations.**
1.  **Check $u_x = v_y$:**
    Comparing the results above, $u_x$ and $v_y$ are identical. The first equation holds.
2.  **Check $u_y = -v_x$:**
    Comparing the results, $u_y$ is exactly the negative of $v_x$. The second equation holds.

**Conclusion:**
Since the partial derivatives exist, are continuous, and satisfy the Cauchy-Riemann equations for all real values of $x$ and $y$ (the entire complex plane), the function $f(z)$ is analytic everywhere.

**Answer:** The function **is analytic** everywhere (it is an entire function).

Here are the detailed solutions for the next four questions (Q149 to Q152). These are multiple-choice questions testing the fundamental theory of complex differentiation.

### Q149. (a) Analytic function and derivable function of complex variable are same (i) yes (ii) no.(iii) none

**Solution:**

To answer this, we must strictly define both terms in the context of complex analysis:

1.  **Derivable Function (Differentiable Function):** A complex function $f(z)$ is derivable at a specific point $z_0$ if the limit of the difference quotient, $f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0+\Delta z) - f(z_0)}{\Delta z}$, exists.
2.  **Analytic Function:** A complex function $f(z)$ is analytic at a point $z_0$ if it is derivable not only at $z_0$ itself, but also **at every point within some neighborhood** (an open disk) surrounding $z_0$.

**The Distinction:**
Because analyticity requires a *region* of differentiability, it is a much stronger condition. 
For example, we proved earlier (in Q134) that the function $f(z) = |z|^2$ is derivable at exactly one point ($z=0$), but it is not derivable anywhere else. Because it lacks a neighborhood of differentiability, it is **not analytic** at $z=0$, even though it is **derivable** there.

Therefore, the set of "derivable functions" and "analytic functions" are not identical. Every analytic function is derivable, but not every derivable function is analytic. 

**Answer:** **(ii) no**

***

### Q150. (a) (Alternative variant from Pg 17) Analytic function $f(z)$ is the derivative $f'(z)$ exists at all points of z in complex region. (i) yes (ii) no.(iii) none

**Solution:**

This question tests the formal definition of an analytic function over a region.

As established in the previous question, a function is analytic at a *single point* if it is differentiable in some neighborhood of that point. 
By extension, a function $f(z)$ is said to be **analytic in a region $R$** if it is differentiable (i.e., its derivative $f'(z)$ exists) at **every single point** contained within that region $R$. 

This is the exact standard mathematical definition of an analytic (or holomorphic) function on a domain. Since the statement perfectly matches the definition, the statement is true.

**Answer:** **(i) yes**

***

### Q151. (b) Analytic function satisfy Laplacee's equn. & Cauchy Riemann equn. (i) yes (ii) no. (iii) both

**Solution:**

Let's evaluate the properties of an analytic function $f(z) = u(x,y) + iv(x,y)$.

1.  **Cauchy-Riemann Equations:** A fundamental theorem of complex analysis states that a necessary condition for a function to be analytic in a region is that its real part $u$ and imaginary part $v$ must satisfy the Cauchy-Riemann equations ($u_x = v_y$ and $u_y = -v_x$) everywhere in that region. Thus, it **does** satisfy the C-R equations.
2.  **Laplace's Equation:** As proven earlier in Q137, if a function is analytic, we can take the second partial derivatives of the C-R equations to show that $u_{xx} + u_{yy} = 0$ and $v_{xx} + v_{yy} = 0$. This means both $u$ and $v$ are harmonic functions and therefore **do** satisfy Laplace's equation.

Because an analytic function satisfies *both* of these mathematical conditions, the premise stated in the question is entirely correct. 

*(Note on the options: Grammatically, the statement is a true/false proposition, so "yes" is the logical answer. Sometimes in subcontinental exam formats, if two things are listed and an option "both" exists, students are tempted to circle it. However, the statement itself is a single proposition asking if analytic functions satisfy [A & B]. The truth value of that proposition is Yes).*

**Answer:** **(i) yes**

***

### Q152. (c) $f'(z) = u_1(z,0) - iu_2(z,0)$ is (i) Laplace's equn. (ii) Milne-Thomson rule. (iii) both

**Solution:**

Let's identify the given formula. 
In complex analysis, if you are given only the real part $u(x,y)$ of an analytic function $f(z) = u + iv$, you can find the exact derivative $f'(z)$ strictly in terms of $z$ without needing to integrate to find $v(x,y)$ first. 

Let $u_1 = \frac{\partial u}{\partial x}$ and $u_2 = \frac{\partial u}{\partial y}$.
We know that $f'(z) = u_x + iv_x$. 
Using the Cauchy-Riemann equation $v_x = -u_y$, we can rewrite this as:
$$f'(z) = u_x - iu_y$$
$$f'(z) = u_1(x,y) - iu_2(x,y)$$

To express this directly in terms of the complex variable $z$, we can substitute $x = z$ and $y = 0$. This yields:
$$f'(z) = u_1(z,0) - iu_2(z,0)$$

This specific algebraic shortcut for constructing an analytic function (or its derivative) directly from its real or imaginary part by substituting $x=z$ and $y=0$ is universally known as the **Milne-Thomson method** (or rule).

It has nothing to do with Laplace's equation (which is $u_{xx} + u_{yy} = 0$).

**Answer:** **(ii) Milne-Thomson rule**



Here are the detailed solutions for the next four questions (Q153 to Q156).

### Q153. (d) Real & imaginary parts of an analytic function represents two families of curves are orthogonal(i) yes (ii) no.(iii) none

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function. The equation $u(x,y) = c_1$ represents one family of level curves (equipotential lines), and $v(x,y) = c_2$ represents another family of level curves (streamlines). 

To determine if two families of curves are orthogonal (intersect at $90^\circ$), their gradient vectors must be perpendicular. In 2D, this means the dot product of their gradient vectors must be zero, or equivalently, the product of their slopes at any point of intersection must be $-1$.

**Step 1: Find the slope of the curve $u(x,y) = c_1$.**
Take the implicit derivative with respect to $x$:
$$\frac{\partial u}{\partial x} + \frac{\partial u}{\partial y} \frac{dy}{dx} = 0$$
$$u_x + u_y \frac{dy}{dx} = 0$$
Let the slope of this curve be $m_1$:
$$m_1 = \frac{dy}{dx} = -\frac{u_x}{u_y}$$

**Step 2: Find the slope of the curve $v(x,y) = c_2$.**
Take the implicit derivative with respect to $x$:
$$v_x + v_y \frac{dy}{dx} = 0$$
Let the slope of this curve be $m_2$:
$$m_2 = \frac{dy}{dx} = -\frac{v_x}{v_y}$$

**Step 3: Multiply the slopes and apply the Cauchy-Riemann equations.**
Since $f(z)$ is analytic, the C-R equations hold: $u_x = v_y$ and $u_y = -v_x$.
Substitute these into the slope $m_1$:
$$m_1 = -\frac{v_y}{-v_x} = \frac{v_y}{v_x}$$

Now multiply $m_1$ and $m_2$:
$$m_1 \cdot m_2 = \left( \frac{v_y}{v_x} \right) \cdot \left( -\frac{v_x}{v_y} \right)$$
Assuming the partial derivatives are not zero at the point of intersection:
$$m_1 \cdot m_2 = -1$$

**Conclusion:**
Because the product of their slopes is $-1$, the tangent lines to the curves are perpendicular. Therefore, the two families of curves $u = c_1$ and $v = c_2$ are orthogonal trajectories of each other. The statement is true.

**Answer:** **(i) yes**

***

### Q154. (e) A point at which $f(z)$ fails to be Analytic is called singular point. (i) yes (ii) no.(iii) none

**Solution:**

This question tests a fundamental definition in complex analysis.

*   An **analytic function** is a function that is differentiable at a point and in some neighborhood around that point.
*   If a function $f(z)$ is analytic everywhere in a region *except* at a specific point $z_0$ (or a set of specific points), then the function fails to be analytic at $z_0$.
*   By standard mathematical definition, any point $z_0$ where a function $f(z)$ ceases to be analytic (i.e., it is not differentiable there, or it "blows up" to infinity) is officially called a **singular point** or a **singularity** of the function.

Examples of singular points include:
*   Poles (e.g., $z=0$ for $f(z) = 1/z$)
*   Essential singularities (e.g., $z=0$ for $f(z) = e^{1/z}$)
*   Branch points (e.g., $z=0$ for $f(z) = \sqrt{z}$)

Since the statement perfectly matches the definition, it is true.

**Answer:** **(i) yes**

***

### Q155. (f) Which is Laplace's equn. (i) $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial x} = 0$ (ii) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 v}{\partial x^2} = 0$ (iii) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ 

*(Note: The source text includes "(i) ? (ii)? .(iii) ?" which just prompts the user to pick one).*

**Solution:**

We must identify the correct mathematical formula for Laplace's equation in two dimensions.

Let's evaluate the options:
*   **(i) $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial x} = 0$**: This is just a sum of first-order partial derivatives. It has no special name and is not related to Laplace's equation.
*   **(ii) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 v}{\partial x^2} = 0$**: This sums the second derivative of $u$ with respect to $x$ and the second derivative of $v$ with respect to $x$. This is incorrect. Laplace's equation applies to a single scalar function.
*   **(iii) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$**: This represents the sum of the unmixed second-order partial derivatives of a single function $u(x,y)$ with respect to its spatial coordinates. This operator is called the Laplacian, denoted as $\nabla^2 u$ or $\Delta u$. The equation $\nabla^2 u = 0$ is the exact definition of **Laplace's equation** in two Cartesian dimensions.

**Answer:** **(iii) $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$**

***

### Q156. (g) Define complex integration $\int_C f(z)dz$.

**Solution:**

The question asks for the formal definition of a line integral of a complex function over a contour.

**Definition:**
Let $f(z)$ be a continuous complex-valued function defined in a region of the complex plane. Let $C$ be a smooth (or piecewise smooth) curve (called a contour) in that region, extending from an initial point $A$ to a terminal point $B$. 

To define the integral, we partition the curve $C$ into $n$ small segments using points $z_0, z_1, z_2, \dots, z_n$, where $z_0 = A$ and $z_n = B$. 
Let $\Delta z_k = z_k - z_{k-1}$ be the length of the $k$-th segment.
Choose an arbitrary sample point $\xi_k$ anywhere on the curve segment between $z_{k-1}$ and $z_k$.

We form the Riemann sum:
$$S_n = \sum_{k=1}^{n} f(\xi_k) \Delta z_k$$

The **complex contour integral** of $f(z)$ along $C$ is defined as the limit of this sum as the number of segments $n$ approaches infinity and the length of the largest segment approaches zero ($|\Delta z_k| \to 0$):

$$\int_C f(z) dz = \lim_{n \to \infty} \sum_{k=1}^{n} f(\xi_k) \Delta z_k$$
provided that this limit exists and is independent of the choice of partition and the sample points $\xi_k$.

**(Alternative Operational Definition via real integrals):**
If $f(z) = u(x,y) + iv(x,y)$ and $dz = dx + i dy$, the complex integral can be defined in terms of two real-valued line integrals:
$$\int_C f(z) dz = \int_C (u + iv)(dx + i dy)$$
$$\int_C f(z) dz = \int_C (u dx - v dy) + i \int_C (v dx + u dy)$$
This is the most common way to calculate complex integrals analytically when a parametrization of the curve $C$ is known.

Here are the detailed solutions for the next four questions (Q157 to Q160). These questions deal with the fundamental theorems of complex integration.

### Q157. (h) If $f(z)$ is analytic in a simple closed curve C then $\int_C f(z)dz =$ (i) $2\pi i$ (ii) 0 (iii) None.

**Solution:**

This question tests the knowledge of one of the most important theorems in complex analysis: **Cauchy's Integral Theorem** (also known as the Cauchy-Goursat Theorem).

**Theorem Statement:**
If a complex function $f(z)$ is analytic (holomorphic) everywhere inside and on the boundary of a simple closed contour $C$, then the contour integral of $f(z)$ around $C$ is exactly zero.

Mathematically, it is written as:
$$\oint_C f(z) dz = 0$$

Because the premise of the question states that $f(z)$ is analytic in the simple closed curve $C$, the conditions for Cauchy's Integral Theorem are perfectly met. Therefore, the integral evaluates to zero.

*(Note: The answer $2\pi i$ is typically the result of Cauchy's Integral Formula when evaluating a function with a simple pole inside the contour, like $\int_C \frac{1}{z}dz$ around the origin, where $1/z$ is *not* analytic at $z=0$.)*

**Answer:** **(ii) 0**

***

### Q158. (h) (Alternative variant from Pg 20) If $f(z)$ be continuous in a region R and $\int_C f(z)dz = 0$ around a simple closed curve C then $f(z)$ is .........

**Solution:**

This question tests the converse of Cauchy's Integral Theorem.

**Concept:**
While Cauchy's Integral Theorem states that "If a function is analytic, its integral around a closed curve is zero," there is a powerful reverse theorem called **Morera's Theorem**.

**Theorem Statement (Morera's Theorem):**
If $f(z)$ is a continuous complex-valued function defined in a simply connected region $R$, and if the contour integral $\oint_C f(z) dz = 0$ for every simple closed curve $C$ within $R$, then $f(z)$ must be an **analytic** function throughout $R$.

Morera's Theorem is a standard way to prove that a function is analytic without having to directly compute its derivative or check the Cauchy-Riemann equations, provided you know its integral behavior.

**Answer:** then $f(z)$ is **analytic** (or **holomorphic**).

***

### Q159. (i) $\oint_C Pdx + Qdy = ?$ (Also written as $\oint_C udx + vdy = ?$ on pg 17)

**Solution:**

This question asks for the right-hand side of a fundamental theorem from vector calculus that is heavily utilized in complex analysis.

**Concept:**
The expression $\oint_C Pdx + Qdy$ is the standard notation for a line integral over a closed curve $C$. The theorem that relates this 1D line integral over a boundary $C$ to a 2D double integral over the region $R$ enclosed by $C$ is **Green's Theorem in the plane**.

**Theorem Statement (Green's Theorem):**
Let $C$ be a positively oriented (counter-clockwise), piecewise-smooth, simple closed curve in a plane, and let $R$ be the region bounded by $C$. If $P(x,y)$ and $Q(x,y)$ have continuous partial derivatives on an open region that contains $R$, then:
$$\oint_C P dx + Q dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$$

*(Context in Complex Analysis: This theorem is used to prove Cauchy's Integral Theorem. If $f(z) = u+iv$, then $\oint_C f(z)dz = \oint_C (udx - vdy) + i\oint_C (vdx + udy)$. Applying Green's theorem to both parts yields integrands of $(-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y})$ and $(\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y})$. By the Cauchy-Riemann equations, both of these integrands are $0$, proving the integral is $0$.)*

**Answer:** **$\iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$** 
*(or $\iint_R \left( \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} \right) dx dy$ for the alternate variable variant).*

***

### Q160. (j) If $\int_C zdz = 0$, C is closed curve, then z (i)must be satisfy Cauchy-Riemanns equns. (ii) analytic function (iii)None

**Solution:**

We are given a specific function, $f(z) = z$, and the fact that its integral around a closed curve is zero. We must categorize what this implies about the function $f(z) = z$.

**Step 1: Analyze the function $f(z) = z$.**
The function $f(z) = z$ is the simplest complex polynomial. All polynomial functions in complex variables are continuous and infinitely differentiable everywhere in the complex plane. Therefore, $f(z) = z$ is an **entire function** (a function that is analytic everywhere).

**Step 2: Relate the integral to the theorems.**
Because $f(z) = z$ is analytic, Cauchy's Integral Theorem guarantees that $\oint_C z dz = 0$ for any closed curve $C$.
Conversely, by Morera's Theorem, if we know that $\oint_C z dz = 0$ for closed curves, we can conclude that the function $f(z) = z$ is an **analytic function**.

**Step 3: Evaluate the options.**
*   **(i) must satisfy Cauchy-Riemann eqns:** This is technically true. Since the function is analytic, it *must* satisfy the C-R equations ($u=x, v=y \implies u_x=1, v_y=1, u_y=0, v_x=0$).
*   **(ii) analytic function:** This is also true, and it is the much broader, overarching reason *why* the integral is zero (via Cauchy/Morera's theorems) and *why* it satisfies the C-R equations. In standard complex analysis multiple-choice questions, "analytic function" is the primary category being tested when relating to $\oint_C f(z)dz = 0$.

Because Morera's theorem explicitly concludes "then $f(z)$ is analytic", option (ii) is the most direct and formally expected answer to this "if-then" statement.

**Answer:** **(ii) analytic function**

Here are the detailed solutions for the next four questions (Q161 to Q164).

### Q161. (k) Difference between Cau.'s int. formu. & Cau.'s Resi. Them. are any point 'a' & 'poles of order m' respectively (i) no (ii) yes

**Solution:**

We need to evaluate the conceptual difference between two major theorems in complex analysis.

**1. Cauchy's Integral Formula:**
This theorem states that if $f(z)$ is analytic inside and on a simple closed contour $C$, and $z=a$ is **any specific point** situated *inside* $C$, then the value of the function at that point is given by:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
The formula specifically evaluates an integral containing a simple singularity (a pole of order 1 at $z=a$), using the value of the analytic numerator $f(z)$ at that exact arbitrary point '$a$'.

**2. Cauchy's Residue Theorem:**
This is a more generalized theorem. It states that if a function $F(z)$ is analytic inside and on a simple closed contour $C$, *except* for a finite number of isolated singularities (which can be **poles of any order $m$**) inside $C$, then the integral around $C$ is $2\pi i$ times the sum of the residues at those poles:
$$\oint_C F(z) dz = 2\pi i \sum \text{Res}(F, a_k)$$
Here, we evaluate the limit/derivative structure associated with "poles of order $m$" rather than just evaluating a numerator at "any point $a$".

**Conclusion:**
The statement accurately summarizes the core operational distinction taught to students: The Integral Formula is used to find the value of an analytic function at *any point 'a'* inside a contour (by creating an artificial simple pole in the denominator), whereas the Residue Theorem generalizes this to handle pre-existing *poles of order 'm'* inside the contour by calculating their residues.

**Answer:** **(ii) yes**

***

### Q162. (l) All derivable function are Analytic function. Ans. (a) yes (b) no (Pg 21)

**Solution:**

This question asks if "derivable" (differentiable) and "analytic" mean the exact same thing in complex analysis.

**Definitions:**
*   A function $f(z)$ is **derivable** at a specific point $z_0$ if the limit $f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0+\Delta z) - f(z_0)}{\Delta z}$ exists at that single point.
*   A function $f(z)$ is **analytic** at a point $z_0$ if it is derivable at $z_0$ **and** derivable at every other point in some open neighborhood (a small circle) surrounding $z_0$.

**The Proof by Counterexample:**
Consider the function $f(z) = |z|^2 = x^2 + y^2$.
As proven earlier (Q134):
1.  The derivative $f'(0)$ exists and equals $0$. Thus, it is **derivable at $z=0$**.
2.  However, the Cauchy-Riemann equations ($2x=0, 2y=0$) are *only* satisfied at $(0,0)$. The function is not differentiable at any point arbitrarily close to $(0,0)$. 
3.  Because it lacks a neighborhood of differentiability, $f(z)$ is **not analytic** at $z=0$.

**Conclusion:**
Just because a function has a derivative at a single isolated point does not grant it the title of being an "analytic function." Analyticity is a regional property, while derivability is a point property. Therefore, not all derivable functions are analytic.

**Answer:** **(b) no**

***

### Q163. (m) All Analytic function are derivable function. Ans. (a) yes (b) no (Pg 21)

**Solution:**

This question asks the converse of Q162: Does being analytic guarantee being derivable?

**Definition:**
By the strict mathematical definition of analyticity, a function $f(z)$ is said to be analytic at a point $z_0$ if and only if it is **derivable** at $z_0$ and derivable at all points in some neighborhood of $z_0$.

**Logical Deduction:**
Analyticity is a stricter, stronger condition than basic point derivability. 
If a function meets the high standard of being analytic at a point, it has inherently already passed the lower standard of being derivable at that point. It is impossible to be analytic without being derivable.

Therefore, the set of analytic functions is a subset of the set of derivable functions. Every single analytic function is, by definition, derivable.

**Answer:** **(a) yes**

***

### Q164. Problem 3.1.1: $f(z)=z^2$ (Implied: Evaluate analytic function derivative)

*(Note: Based on standard textbook structures, early problems introducing $f(z)=z^2$ ask to either prove it is analytic via the limit definition or to find its derivative using Cauchy-Riemann equations. We will do both).*

**Solution:**

Let $f(z) = z^2$.

**Method 1: Using the Limit Definition of the Derivative**
We evaluate $f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$.
$$f'(z) = \lim_{\Delta z \to 0} \frac{(z + \Delta z)^2 - z^2}{\Delta z}$$
Expand the binomial:
$$f'(z) = \lim_{\Delta z \to 0} \frac{z^2 + 2z\Delta z + (\Delta z)^2 - z^2}{\Delta z}$$
Cancel $z^2$:
$$f'(z) = \lim_{\Delta z \to 0} \frac{2z\Delta z + (\Delta z)^2}{\Delta z}$$
Factor out and cancel $\Delta z$ (since $\Delta z \to 0$ means $\Delta z \neq 0$):
$$f'(z) = \lim_{\Delta z \to 0} (2z + \Delta z)$$
As $\Delta z \to 0$, the limit becomes:
**$f'(z) = 2z$**
Because this limit exists for all complex numbers $z$, the function is analytic everywhere (entire).

---

**Method 2: Using Cauchy-Riemann Equations**
Let $z = x + iy$.
$$f(z) = (x + iy)^2 = x^2 - y^2 + i(2xy)$$
Separate into real ($u$) and imaginary ($v$) parts:
*   $u(x,y) = x^2 - y^2$
*   $v(x,y) = 2xy$

Find the partial derivatives:
*   $u_x = 2x$
*   $u_y = -2y$
*   $v_x = 2y$
*   $v_y = 2x$

Check the C-R equations:
1) $u_x = v_y \implies 2x = 2x$ (True everywhere)
2) $u_y = -v_x \implies -2y = -(2y)$ (True everywhere)

Because the partial derivatives are continuous polynomials and satisfy the C-R equations everywhere, $f(z)$ is analytic everywhere.

Find the derivative using $f'(z) = u_x + iv_x$:
$$f'(z) = 2x + i(2y)$$
Factor out 2:
$$f'(z) = 2(x + iy) = 2z$$

**Answer:** The function $f(z) = z^2$ is an analytic (entire) function, and its derivative is **$f'(z) = 2z$**.

Here are the detailed solutions for the next four questions (Q165 to Q168).

### Q165. Prblm 3.1.3: $f(z)=\overline{z}$ (Implied: Check if analytic)

*(Note: This is identical to the proof requested in Q139 and Q182. We will prove it here using the Cauchy-Riemann equations).*

**Solution:**

We need to determine if the complex conjugate function $f(z) = \overline{z}$ is an analytic function. To do this, we test if it satisfies the Cauchy-Riemann (C-R) equations.

**Step 1: Separate the function into real and imaginary parts.**
Let $z = x + iy$.
By definition, the complex conjugate is:
$$f(z) = \overline{x + iy} = x - iy$$

Identify the real part $u(x,y)$ and the imaginary part $v(x,y)$:
*   $u(x,y) = x$
*   $v(x,y) = -y$

**Step 2: Calculate the first-order partial derivatives.**
*   $u_x = \frac{\partial}{\partial x}(x) = 1$
*   $u_y = \frac{\partial}{\partial y}(x) = 0$
*   $v_x = \frac{\partial}{\partial x}(-y) = 0$
*   $v_y = \frac{\partial}{\partial y}(-y) = -1$

**Step 3: Test the Cauchy-Riemann equations.**
For the function to be analytic, the C-R equations must hold: $u_x = v_y$ and $u_y = -v_x$.
*   **Test Equation 1:** $u_x = v_y$
    Substitute our calculated values:
    $$1 = -1$$
    This statement is fundamentally false. The first Cauchy-Riemann equation fails everywhere.
*   **Test Equation 2:** $u_y = -v_x$
    Substitute our calculated values:
    $$0 = -0$$
    This is true, but *both* equations must be satisfied simultaneously for the function to be differentiable.

**Conclusion:**
Because the Cauchy-Riemann equation $u_x = v_y$ is not satisfied at any point in the complex plane, the function is not differentiable anywhere. Therefore, it cannot be analytic anywhere.

**Answer:** The function $f(z) = \overline{z}$ is **not analytic** anywhere in the complex plane.

***

### Q166. Problem: $f(z)=ize^z$ (Implied: Satisfy Cauchy Riemann equations)

**Solution:**

We need to separate the function $f(z) = ize^z$ into its real ($u$) and imaginary ($v$) parts and verify that it satisfies the Cauchy-Riemann equations, proving it is analytic.

**Step 1: Substitute $z = x + iy$ and expand the expression.**
$$f(z) = i(x + iy) e^{x + iy}$$
Distribute the $i$:
$$f(z) = (ix + i^2y) e^x e^{iy}$$
Since $i^2 = -1$:
$$f(z) = (-y + ix) e^x e^{iy}$$

**Step 2: Apply Euler's formula.**
Substitute $e^{iy} = \cos y + i\sin y$:
$$f(z) = e^x (-y + ix) (\cos y + i\sin y)$$

**Step 3: Expand the product.**
Use algebraic expansion (FOIL):
$$(-y + ix) (\cos y + i\sin y) = -y\cos y - iy\sin y + ix\cos y + i^2x\sin y$$
Since $i^2 = -1$:
$$= (-y\cos y - x\sin y) + i(x\cos y - y\sin y)$$

Multiply by the $e^x$ term outside to get $u$ and $v$:
*   **$u(x,y) = e^x (-y\cos y - x\sin y)$**
*   **$v(x,y) = e^x (x\cos y - y\sin y)$**

**Step 4: Calculate the partial derivatives (using Product Rule).**
*   **$u_x$:**
    $$u_x = \frac{\partial}{\partial x}(e^x) \cdot (-y\cos y - x\sin y) + e^x \cdot \frac{\partial}{\partial x}(-y\cos y - x\sin y)$$
    $$u_x = e^x(-y\cos y - x\sin y) + e^x(-\sin y)$$
    $$u_x = -e^x (y\cos y + x\sin y + \sin y)$$

*   **$u_y$:**
    $$u_y = e^x \cdot \frac{\partial}{\partial y}(-y\cos y - x\sin y)$$
    Using product rule for $y\cos y$:
    $$u_y = e^x \left[ -(\cos y - y\sin y) - x\cos y \right]$$
    $$u_y = e^x (y\sin y - \cos y - x\cos y)$$

*   **$v_x$:**
    $$v_x = \frac{\partial}{\partial x}(e^x) \cdot (x\cos y - y\sin y) + e^x \cdot \frac{\partial}{\partial x}(x\cos y - y\sin y)$$
    $$v_x = e^x(x\cos y - y\sin y) + e^x(\cos y)$$
    $$v_x = e^x (x\cos y - y\sin y + \cos y)$$

*   **$v_y$:**
    $$v_y = e^x \cdot \frac{\partial}{\partial y}(x\cos y - y\sin y)$$
    Using product rule for $y\sin y$:
    $$v_y = e^x \left[ -x\sin y - (\sin y + y\cos y) \right]$$
    $$v_y = -e^x (x\sin y + \sin y + y\cos y)$$

**Step 5: Check the Cauchy-Riemann equations.**
1.  **$u_x = v_y$**:
    $u_x = -e^x (y\cos y + x\sin y + \sin y)$
    $v_y = -e^x (x\sin y + \sin y + y\cos y)$
    These are identical. The first C-R equation holds.
2.  **$u_y = -v_x$**:
    $u_y = e^x (y\sin y - \cos y - x\cos y) = -e^x (-y\sin y + \cos y + x\cos y)$
    $-v_x = -[e^x (x\cos y - y\sin y + \cos y)]$
    These are identical. The second C-R equation holds.

**Answer:** The partial derivatives are continuous and satisfy the Cauchy-Riemann equations everywhere, confirming that $f(z) = ize^z$ is an **analytic function**.

***

### Q167. Problem: $f(z)=ze^{-z}$ (Implied: Satisfy Cauchy Riemann equations)

**Solution:**

We need to separate $f(z) = ze^{-z}$ into $u+iv$ and verify the Cauchy-Riemann equations.

**Step 1: Substitute $z = x + iy$ and expand.**
$$f(z) = (x + iy) e^{-(x + iy)}$$
$$f(z) = (x + iy) e^{-x} e^{-iy}$$

**Step 2: Apply Euler's formula.**
Substitute $e^{-iy} = \cos(-y) + i\sin(-y) = \cos y - i\sin y$:
$$f(z) = e^{-x} (x + iy) (\cos y - i\sin y)$$

**Step 3: Expand the product.**
$$(x + iy) (\cos y - i\sin y) = x\cos y - ix\sin y + iy\cos y - i^2y\sin y$$
Since $i^2 = -1$:
$$= (x\cos y + y\sin y) + i(y\cos y - x\sin y)$$

Multiply by $e^{-x}$ to get $u$ and $v$:
*   **$u(x,y) = e^{-x} (x\cos y + y\sin y)$**
*   **$v(x,y) = e^{-x} (y\cos y - x\sin y)$**

**Step 4: Calculate the partial derivatives (using Product Rule).**
*   **$u_x$:**
    $$u_x = (-e^{-x})(x\cos y + y\sin y) + e^{-x}(1\cdot\cos y + 0)$$
    $$u_x = e^{-x} (\cos y - x\cos y - y\sin y)$$

*   **$u_y$:**
    $$u_y = e^{-x} [x(-\sin y) + (\sin y + y\cos y)]$$
    $$u_y = e^{-x} (-x\sin y + \sin y + y\cos y)$$

*   **$v_x$:**
    $$v_x = (-e^{-x})(y\cos y - x\sin y) + e^{-x}(0 - \sin y)$$
    $$v_x = e^{-x} (-y\cos y + x\sin y - \sin y)$$

*   **$v_y$:**
    $$v_y = e^{-x} [(\cos y - y\sin y) - x\cos y]$$
    $$v_y = e^{-x} (\cos y - y\sin y - x\cos y)$$

**Step 5: Check the Cauchy-Riemann equations.**
1.  **$u_x = v_y$**:
    $u_x = e^{-x} (\cos y - x\cos y - y\sin y)$
    $v_y = e^{-x} (\cos y - y\sin y - x\cos y)$
    These are identical. First equation holds.
2.  **$u_y = -v_x$**:
    $u_y = e^{-x} (-x\sin y + \sin y + y\cos y)$
    $-v_x = -[e^{-x} (-y\cos y + x\sin y - \sin y)] = e^{-x} (y\cos y - x\sin y + \sin y)$
    These are identical. Second equation holds.

**Answer:** The partial derivatives are continuous and satisfy the Cauchy-Riemann equations everywhere, confirming that $f(z) = ze^{-z}$ is an **analytic function**.

***

### Q168. Prblm 3.2.1: Prove that, real & imaginary parts of an analytic function f(z) of a complex variable satisfy laplace's equation.

*(Note: This is theoretically identical to Q137. The formal proof is provided below again).*

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function in a region $R$. 
We must prove that both $u$ and $v$ satisfy Laplace's equation: $\nabla^2 \phi = 0$.
That is, we must show $u_{xx} + u_{yy} = 0$ and $v_{xx} + v_{yy} = 0$.

**Step 1: State the necessary conditions for analyticity.**
Because $f(z)$ is analytic, its real and imaginary parts must satisfy the Cauchy-Riemann (C-R) equations:
1.  $u_x = v_y$
2.  $u_y = -v_x$

Furthermore, because $f(z)$ is analytic, all its higher-order partial derivatives exist and are continuous.

**Step 2: Prove that $u$ satisfies Laplace's equation.**
Differentiate the first C-R equation with respect to $x$:
$$\frac{\partial}{\partial x}(u_x) = \frac{\partial}{\partial x}(v_y) \implies u_{xx} = v_{yx}$$

Differentiate the second C-R equation with respect to $y$:
$$\frac{\partial}{\partial y}(u_y) = \frac{\partial}{\partial y}(-v_x) \implies u_{yy} = -v_{xy}$$

Add the two resulting second-order derivative equations together:
$$u_{xx} + u_{yy} = v_{yx} - v_{xy}$$

By Clairaut's Theorem on mixed partial derivatives (since the derivatives are continuous), the order of differentiation does not matter: $v_{yx} = v_{xy}$.
Therefore, $v_{yx} - v_{xy} = 0$.
$$u_{xx} + u_{yy} = 0$$
Thus, $u(x,y)$ satisfies Laplace's equation. **(Proved)**

**Step 3: Prove that $v$ satisfies Laplace's equation.**
Differentiate the first C-R equation with respect to $y$:
$$\frac{\partial}{\partial y}(u_x) = \frac{\partial}{\partial y}(v_y) \implies u_{xy} = v_{yy}$$

Differentiate the second C-R equation with respect to $x$:
$$\frac{\partial}{\partial x}(u_y) = \frac{\partial}{\partial x}(-v_x) \implies u_{yx} = -v_{xx}$$
Rearrange this to isolate $v_{xx}$:
$$v_{xx} = -u_{yx}$$

Add the equations for $v_{xx}$ and $v_{yy}$ together:
$$v_{xx} + v_{yy} = -u_{yx} + u_{xy}$$

Again, by Clairaut's Theorem, $u_{yx} = u_{xy}$.
Therefore, $-u_{yx} + u_{xy} = 0$.
$$v_{xx} + v_{yy} = 0$$
Thus, $v(x,y)$ satisfies Laplace's equation. **(Proved)**

Here are the detailed solutions for the next four questions (Q169 to Q172).

### Q169. Prblm 3.2.2: Show that, $f(z)=\vert{}z\vert{}^2$ is diff at $z=0$ but not analytic at $z=0$

*(Note: This is identical to Q134. We will re-state the proof clearly here).*

**Solution:**

**Part 1: Show it is differentiable at $z=0$.**
We use the fundamental limit definition of the complex derivative at a point $z_0$:
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$
Here, $z_0 = 0$ and $f(z) = |z|^2$.
$$f'(0) = \lim_{\Delta z \to 0} \frac{f(\Delta z) - f(0)}{\Delta z}$$
$$f'(0) = \lim_{\Delta z \to 0} \frac{|\Delta z|^2 - 0}{\Delta z}$$
We use the complex property $|w|^2 = w\overline{w}$. Therefore, $|\Delta z|^2 = \Delta z \cdot \overline{\Delta z}$.
$$f'(0) = \lim_{\Delta z \to 0} \frac{\Delta z \cdot \overline{\Delta z}}{\Delta z}$$
Cancel the $\Delta z$ term (since $\Delta z \to 0$ implies $\Delta z \neq 0$):
$$f'(0) = \lim_{\Delta z \to 0} \overline{\Delta z}$$
As the complex number $\Delta z$ approaches zero, its conjugate $\overline{\Delta z}$ also approaches zero, regardless of the path taken.
$$f'(0) = 0$$
Because the limit exists and equals a single finite number, **$f(z)$ is differentiable at $z=0$**.

---

**Part 2: Show it is not analytic at $z=0$.**
By definition, a function is **analytic** at a point $z_0$ only if it is differentiable at $z_0$ *and* everywhere within some neighborhood (an open circle) surrounding $z_0$.
To check its differentiability anywhere else, we use the Cauchy-Riemann equations.

Let $z = x + iy$.
$$f(z) = |x + iy|^2 = x^2 + y^2$$
This function is purely real.
*   $u(x,y) = x^2 + y^2$
*   $v(x,y) = 0$

Calculate the partial derivatives:
*   $u_x = 2x$
*   $u_y = 2y$
*   $v_x = 0$
*   $v_y = 0$

Check the Cauchy-Riemann equations:
1) $u_x = v_y \implies 2x = 0 \implies x = 0$
2) $u_y = -v_x \implies 2y = 0 \implies y = 0$

The Cauchy-Riemann equations are *only* satisfied at the exact point $(0,0)$. For any point even infinitesimally far away from the origin (e.g., $x=0.001$), the equations fail.
Since the function is not differentiable in any neighborhood surrounding $z=0$, **it is not analytic at $z=0$.**

***

### Q170. Prblm 3.2.3: Show that a) $u=n^3-3ny^2+3n^2-3y^2+1$ is harmonic b) find v such that $f(z)=u+iv$ is analytic. c) find also $f(z)$ in terms of $z$.

*(Note: The variable '$n$' in the source text is clearly a typographical error for '$x$', which is extremely common in OCR or handwritten transcription. The standard polynomial is $u(x,y) = x^3 - 3xy^2 + 3x^2 - 3y^2 + 1$. I will solve the mathematically sound version using $x$).*

**Solution:**

Given $u(x,y) = x^3 - 3xy^2 + 3x^2 - 3y^2 + 1$.

**Part a) Show $u$ is harmonic.**
We must verify Laplace's equation: $u_{xx} + u_{yy} = 0$.
1.  **First derivatives:**
    $$u_x = \frac{\partial}{\partial x}(x^3 - 3xy^2 + 3x^2 - 3y^2 + 1) = 3x^2 - 3y^2 + 6x$$
    $$u_y = \frac{\partial}{\partial y}(x^3 - 3xy^2 + 3x^2 - 3y^2 + 1) = -6xy - 6y$$
2.  **Second derivatives:**
    $$u_{xx} = \frac{\partial}{\partial x}(3x^2 - 3y^2 + 6x) = 6x + 6$$
    $$u_{yy} = \frac{\partial}{\partial y}(-6xy - 6y) = -6x - 6$$
3.  **Check Laplace's equation:**
    $$u_{xx} + u_{yy} = (6x + 6) + (-6x - 6) = 0$$
Since Laplace's equation holds, **$u$ is a harmonic function.** (Proved)

---

**Part b) Find the harmonic conjugate $v(x,y)$.**
We use the Cauchy-Riemann equations: $v_y = u_x$ and $v_x = -u_y$.
1.  **From $v_y = u_x$:**
    $$v_y = 3x^2 - 3y^2 + 6x$$
2.  **Integrate with respect to $y$:**
    $$v(x,y) = \int (3x^2 - 3y^2 + 6x) dy$$
    $$v(x,y) = 3x^2y - y^3 + 6xy + g(x)$$
3.  **Differentiate with respect to $x$:**
    $$v_x = \frac{\partial}{\partial x}(3x^2y - y^3 + 6xy + g(x))$$
    $$v_x = 6xy + 6y + g'(x)$$
4.  **Use the second C-R equation ($v_x = -u_y$):**
    From Part a, $-u_y = -(-6xy - 6y) = 6xy + 6y$.
    Equating the two expressions for $v_x$:
    $$6xy + 6y + g'(x) = 6xy + 6y$$
    $$g'(x) = 0$$
5.  **Integrate to find $g(x)$:**
    $$g(x) = C$$ (where $C$ is a real constant).
6.  **Write the final function $v(x,y)$:**
    **$v(x,y) = 3x^2y - y^3 + 6xy + C$**

---

**Part c) Find $f(z)$ in terms of $z$.**
We use the **Milne-Thomson method** to directly construct $f'(z)$ and integrate, or substitute directly. The direct substitution of $x=z, y=0$ into $f(z) = u+iv$ is fastest.
$$f(z) = u(z,0) + iv(z,0)$$
$$u(z,0) = z^3 - 3z(0)^2 + 3z^2 - 3(0)^2 + 1 = z^3 + 3z^2 + 1$$
$$v(z,0) = 3z^2(0) - 0^3 + 6z(0) + C = C$$
Substitute these into $f(z)$:
$$f(z) = (z^3 + 3z^2 + 1) + i(C)$$
Let $C_1 = iC$ be a complex constant.
**$f(z) = z^3 + 3z^2 + 1 + C_1$**

***

### Q171. Prblm 3.2.4: Show that a) $u=2n(1-y)$ is harmonic b) find v such that $f(z)=u+iv$ is analytic. c) find also $f(z)$ in terms of $z$.

*(Note: Again, '$n$' is a typo for '$x$'. The equation is $u(x,y) = 2x(1-y) = 2x - 2xy$. This is mathematically identical to Q135. We will quickly run through the steps).*

**Solution:**

Given $u(x,y) = 2x - 2xy$.

**Part a) Show $u$ is harmonic.**
1.  First derivatives: $u_x = 2 - 2y$, $u_y = -2x$.
2.  Second derivatives: $u_{xx} = 0$, $u_{yy} = 0$.
3.  Check Laplace's equation: $u_{xx} + u_{yy} = 0 + 0 = 0$.
**$u$ is a harmonic function.** (Proved)

---

**Part b) Find the harmonic conjugate $v(x,y)$.**
1.  From C-R equation $v_y = u_x$:
    $$v_y = 2 - 2y$$
2.  Integrate with respect to $y$:
    $$v(x,y) = \int (2 - 2y) dy = 2y - y^2 + g(x)$$
3.  Differentiate with respect to $x$:
    $$v_x = g'(x)$$
4.  Use C-R equation $v_x = -u_y$:
    $$g'(x) = -(-2x) = 2x$$
5.  Integrate with respect to $x$:
    $$g(x) = \int 2x dx = x^2 + C$$
6.  Write the final function $v(x,y)$:
    **$v(x,y) = 2y - y^2 + x^2 + C$**

---

**Part c) Find $f(z)$ in terms of $z$.**
Use the Milne-Thomson method: substitute $x=z, y=0$ into $f(z) = u(x,y) + iv(x,y)$.
$$u(z,0) = 2z - 2z(0) = 2z$$
$$v(z,0) = 2(0) - 0^2 + z^2 + C = z^2 + C$$
Construct $f(z)$:
$$f(z) = 2z + i(z^2 + C)$$
**$f(z) = iz^2 + 2z + iC$**

***

### Q172. Prblm 3.2.4: (Milne- Thomson Rule) $u_1(n,y)=\frac{\partial u}{\partial x}$ and $u_2(x,y)=\frac{\partial u}{\partial y}$ prove that $f'(z)=u_1(z,0)-i u_2(z,0)$

*(Note: Typo '$n$' corrected to '$x$').*

**Solution:**

This is the formal proof of the Milne-Thomson rule for constructing the derivative of an analytic function directly from its real part.

**Step 1: State the derivative in terms of partials.**
Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function.
The derivative of an analytic function can be written entirely in terms of partial derivatives with respect to $x$:
$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$$
Let's use the given notation $u_1 = \frac{\partial u}{\partial x}$.
$$f'(z) = u_1(x,y) + i\frac{\partial v}{\partial x}$$

**Step 2: Apply the Cauchy-Riemann equations.**
We want to express the derivative strictly in terms of the known function $u$.
The C-R equations state that $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$, which means $\frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}$.
Using the given notation $u_2 = \frac{\partial u}{\partial y}$, we have $\frac{\partial v}{\partial x} = -u_2(x,y)$.
Substitute this back into the derivative equation:
$$f'(z) = u_1(x,y) - i u_2(x,y) \quad \text{--- (Equation 1)}$$

**Step 3: Justify the variable substitution.**
Since $f(z)$ is analytic, its derivative $f'(z)$ is also an analytic function of $z$. Therefore, we can express $f'(z)$ as a function of the single complex variable $z$, independent of any specific relationship between $x$ and $y$.
Since $z = x + iy$, the identity must hold true for *any* choice of $y$.
To write the function purely in terms of $z$, we can make the convenient choice of setting $y = 0$.
If $y = 0$, then $z = x + i(0) \implies x = z$.

**Step 4: Perform the substitution.**
Substitute $x = z$ and $y = 0$ into Equation 1:
$$f'(z) = u_1(z,0) - i u_2(z,0)$$
**(Proved)**
Here are the detailed solutions for the next four questions (Q173 to Q176).

### Q173. Prblm 3.2.5: (Milne-Thomson Rule) If $v_1(x,y)=\frac{\partial v}{\partial x}$ and $v_2(x,y)=\frac{\partial v}{\partial y}$ prove that $f'(z)=v_1(z,0)-i v_2(z,0)$

*(Note: There is a typographical error in the source text's formula. The correct Milne-Thomson rule derived from the imaginary part $v$ is $f'(z) = v_2(z,0) + i v_1(z,0)$. I will prove the mathematically correct standard identity).*

**Solution:**

We must construct the derivative $f'(z)$ strictly in terms of the known imaginary part $v(x,y)$ and its partial derivatives.

**Step 1: State the derivative in terms of partials.**
Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function.
The standard expression for the complex derivative using partial derivatives with respect to $x$ is:
$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$$
Using the given notation $v_1(x,y) = \frac{\partial v}{\partial x}$, we can substitute the imaginary part:
$$f'(z) = \frac{\partial u}{\partial x} + i v_1(x,y)$$

**Step 2: Apply the Cauchy-Riemann equations.**
We want to eliminate $u$ from the expression so it only depends on $v$.
The C-R equations state that $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$.
Using the given notation $v_2(x,y) = \frac{\partial v}{\partial y}$, we have $\frac{\partial u}{\partial x} = v_2(x,y)$.
Substitute this back into the derivative equation:
$$f'(z) = v_2(x,y) + i v_1(x,y) \quad \text{--- (Equation 1)}$$

**Step 3: Apply the Milne-Thomson substitution.**
Because $f(z)$ is analytic, its derivative $f'(z)$ is also analytic and can be written purely as a function of the complex variable $z$. The relationship holds regardless of the specific path in the complex plane. 
We can cleanly convert the variables from $(x,y)$ to $(z)$ by evaluating the function along the real axis, where $y = 0$.
If $y = 0$, then $z = x + i(0)$, meaning $x = z$.

**Step 4: Perform the substitution.**
Substitute $x = z$ and $y = 0$ into Equation 1:
$$f'(z) = v_2(z,0) + i v_1(z,0)$$
**(Proved - corrected version)**.

***

### Q174. Prblm 3.2.5: If $Im\{f'(z)\}=6x(2y-1)$ & $f(0)=3-2i$ find $f(z)$ & $f(1+i)$

**Solution:**

Let $f(z) = u + iv$. Then $f'(z) = u_x + iv_x$.
We are given that the imaginary part of the derivative is $Im\{f'(z)\} = v_x = 6x(2y-1)$.
We need to construct the full analytic function $f(z)$.

**Step 1: Expand the given partial derivative.**
$$v_x(x,y) = 12xy - 6x$$

**Step 2: Find $v(x,y)$ by integrating.**
Integrate $v_x$ with respect to $x$:
$$v(x,y) = \int (12xy - 6x) dx$$
$$v(x,y) = 6x^2y - 3x^2 + h(y)$$

**Step 3: Use the Cauchy-Riemann equations to find $u(x,y)$.**
We know $u_y = -v_x$.
$$u_y = -(12xy - 6x) = -12xy + 6x$$
Integrate $u_y$ with respect to $y$:
$$u(x,y) = \int (-12xy + 6x) dy$$
$$u(x,y) = -6xy^2 + 6xy + g(x)$$

**Step 4: Reconcile the remaining unknowns using the other C-R equation.**
We know $u_x = v_y$. Let's calculate both from our current expressions for $u$ and $v$:
*   $u_x = \frac{\partial}{\partial x}(-6xy^2 + 6xy + g(x)) = -6y^2 + 6y + g'(x)$
*   $v_y = \frac{\partial}{\partial y}(6x^2y - 3x^2 + h(y)) = 6x^2 + h'(y)$

Equate them:
$$-6y^2 + 6y + g'(x) = 6x^2 + h'(y)$$
Separate the $x$ terms and $y$ terms onto different sides of the equation:
$$g'(x) - 6x^2 = h'(y) + 6y^2 - 6y$$
Since the left side depends only on $x$ and the right side depends only on $y$, they must both equal a constant $C_1$.
*   $g'(x) - 6x^2 = C_1 \implies g'(x) = 6x^2 + C_1 \implies g(x) = 2x^3 + C_1x + C_2$
*   $h'(y) + 6y^2 - 6y = C_1 \implies h'(y) = -6y^2 + 6y + C_1 \implies h(y) = -2y^3 + 3y^2 + C_1y + C_3$

Substitute these back into $u$ and $v$:
*   $u(x,y) = -6xy^2 + 6xy + 2x^3 + C_1x + C_2$
*   $v(x,y) = 6x^2y - 3x^2 - 2y^3 + 3y^2 + C_1y + C_3$

**Step 5: Construct $f(z)$ and apply the boundary condition.**
Using the Milne-Thomson method (substituting $x=z, y=0$):
*   $u(z,0) = 2z^3 + C_1z + C_2$
*   $v(z,0) = -3z^2 + C_3$
$$f(z) = (2z^3 + C_1z + C_2) + i(-3z^2 + C_3)$$
$$f(z) = 2z^3 - 3iz^2 + C_1z + (C_2 + iC_3)$$
Let the complex constant $C = C_2 + iC_3$.
$$f(z) = 2z^3 - 3iz^2 + C_1z + C$$

Apply the condition $f(0) = 3 - 2i$:
$$f(0) = 2(0)^3 - 3i(0)^2 + C_1(0) + C = 3 - 2i \implies C = 3 - 2i$$
*(Note: Because $C_1$ is attached to $z$, we cannot solve for it with only $f(0)$. We must assume $C_1=0$ based on standard problem constraints where $Im(f'(z))$ is given exclusively, meaning $Re(f'(z))$ has no standalone constants, or the problem is slightly underdefined. Assuming $C_1=0$):*
**$f(z) = 2z^3 - 3iz^2 + 3 - 2i$**

**Step 6: Evaluate $f(1+i)$.**
Substitute $z = 1+i$:
$$f(1+i) = 2(1+i)^3 - 3i(1+i)^2 + 3 - 2i$$
*   $(1+i)^2 = 1 + 2i + i^2 = 2i$
*   $(1+i)^3 = (1+i)(2i) = 2i + 2i^2 = -2 + 2i$

Substitute these in:
$$f(1+i) = 2(-2 + 2i) - 3i(2i) + 3 - 2i$$
$$f(1+i) = -4 + 4i - 6i^2 + 3 - 2i$$
$$f(1+i) = -4 + 4i + 6 + 3 - 2i$$
Combine real and imaginary terms:
$$f(1+i) = 5 + 2i$$

**Answer:** 
*   **$f(z) = 2z^3 - 3iz^2 + 3 - 2i$**
*   **$f(1+i) = 5 + 2i$**

***

### Q175. Prblm 3.4.1: find the orthogonal set of curves $x^2-y^2=a^2$

**Solution:**

We are given a family of curves defined by a constant level set of a function: $u(x,y) = x^2 - y^2 = a^2$.
To find the orthogonal set of curves, we must find the harmonic conjugate $v(x,y)$. The curves $v(x,y) = b^2$ will be orthogonal to the given curves everywhere they intersect.

**Step 1: Calculate the partial derivatives of $u$.**
*   $u_x = \frac{\partial}{\partial x}(x^2 - y^2) = 2x$
*   $u_y = \frac{\partial}{\partial y}(x^2 - y^2) = -2y$

*(Verification: $u_{xx} = 2, u_{yy} = -2 \implies u_{xx}+u_{yy}=0$, so $u$ is harmonic and an orthogonal family exists).*

**Step 2: Set up the Cauchy-Riemann equations to find $v$.**
*   $v_y = u_x \implies v_y = 2x$
*   $v_x = -u_y \implies v_x = -(-2y) = 2y$

**Step 3: Integrate to find $v(x,y)$.**
Integrate $v_y$ with respect to $y$:
$$v(x,y) = \int 2x dy$$
$$v(x,y) = 2xy + g(x)$$

**Step 4: Differentiate and solve for $g(x)$.**
Differentiate $v(x,y)$ with respect to $x$:
$$v_x = \frac{\partial}{\partial x}(2xy + g(x)) = 2y + g'(x)$$

Equate this to the $v_x$ found in Step 2:
$$2y + g'(x) = 2y$$
$$g'(x) = 0$$
Integrating gives $g(x) = C$ (where $C$ is a real constant).

**Step 5: Write the final orthogonal family of curves.**
Substitute $g(x)$ back into $v(x,y)$:
$$v(x,y) = 2xy + C$$

The orthogonal set of curves is defined by setting $v(x,y)$ to an arbitrary constant, let's call it $c_2$.
$$2xy + C = c_2 \implies 2xy = c_2 - C$$
Let the new arbitrary constant be $k = c_2 - C$.
$$2xy = k$$

*(Note: Geometrically, $x^2-y^2=a^2$ represents a family of rectangular hyperbolas opening along the x and y axes. The orthogonal trajectories $2xy=k$ represent a family of rectangular hyperbolas rotated by $45^\circ$, perfectly intersecting the first set at right angles).*

**Answer:** The orthogonal set of curves is **$2xy = k$** (where $k$ is a constant).

***

### Q176. Prblm 3.4.2: Find the orthogonal set of curves $e^{-n}(x\sin y-y\cos y)=\alpha$

*(Note: Typo '$n$' corrected to '$x$'. The equation is $u(x,y) = e^{-x}(x\sin y - y\cos y) = \alpha$).*

**Solution:**

We are given $u(x,y) = e^{-x}(x\sin y - y\cos y)$. We must find the harmonic conjugate $v(x,y)$. The set $v(x,y) = \beta$ will be the orthogonal trajectories.

**Step 1: Calculate the partial derivatives of $u$.**
Use the product rule for $u_x$:
$$u_x = \frac{\partial}{\partial x}(e^{-x}) \cdot (x\sin y - y\cos y) + e^{-x} \cdot \frac{\partial}{\partial x}(x\sin y - y\cos y)$$
$$u_x = -e^{-x}(x\sin y - y\cos y) + e^{-x}(\sin y)$$
$$u_x = e^{-x}(\sin y - x\sin y + y\cos y)$$

Use the product rule for $u_y$:
$$u_y = e^{-x} \cdot \frac{\partial}{\partial y}(x\sin y - y\cos y)$$
$$u_y = e^{-x} [x\cos y - (\cos y - y\sin y)]$$
$$u_y = e^{-x} (x\cos y - \cos y + y\sin y)$$

**Step 2: Set up the Cauchy-Riemann equations to find $v$.**
*   $v_y = u_x = e^{-x}(\sin y - x\sin y + y\cos y)$
*   $v_x = -u_y = -e^{-x}(x\cos y - \cos y + y\sin y) = e^{-x}(\cos y - x\cos y - y\sin y)$

**Step 3: Integrate $v_y$ with respect to $y$ to find $v(x,y)$.**
$$v(x,y) = \int e^{-x}(\sin y - x\sin y + y\cos y) dy$$
Distribute the integral (treating $x$ as a constant):
$$v(x,y) = e^{-x} \left[ \int \sin y dy - x\int \sin y dy + \int y\cos y dy \right]$$
$$v(x,y) = e^{-x} \left[ -\cos y - x(-\cos y) + (\text{integration by parts}) \right]$$
For $\int y\cos y dy$, let $w=y, dw=dy, dz=\cos y dy, z=\sin y$.
$\int y\cos y dy = y\sin y - \int \sin y dy = y\sin y + \cos y$.
Substitute this back:
$$v(x,y) = e^{-x} [-\cos y + x\cos y + y\sin y + \cos y] + g(x)$$
Cancel the $-\cos y$ and $+\cos y$:
$$v(x,y) = e^{-x}(x\cos y + y\sin y) + g(x)$$

**Step 4: Differentiate and solve for $g(x)$.**
$$v_x = \frac{\partial}{\partial x} [e^{-x}(x\cos y + y\sin y) + g(x)]$$
Using the product rule:
$$v_x = -e^{-x}(x\cos y + y\sin y) + e^{-x}(\cos y) + g'(x)$$
$$v_x = e^{-x}(\cos y - x\cos y - y\sin y) + g'(x)$$
Equate this to $v_x$ from Step 2:
$$e^{-x}(\cos y - x\cos y - y\sin y) + g'(x) = e^{-x}(\cos y - x\cos y - y\sin y)$$
$$g'(x) = 0 \implies g(x) = C$$

**Step 5: Write the final orthogonal set.**
Substitute $g(x)$ back into $v(x,y)$:
$$v(x,y) = e^{-x}(x\cos y + y\sin y) + C$$
Set this equal to a constant $c_2$, yielding $e^{-x}(x\cos y + y\sin y) = c_2 - C = \beta$.

**Answer:** The orthogonal set of curves is **$e^{-x}(x\cos y + y\sin y) = \beta$**.
Here are the detailed solutions for the next four questions (Q177 to Q180).

### Q177. Prblm 3.4.3: Prove that, in polar form Cauchy Riemann eqn can be written $\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial\theta}$ & $\frac{\partial v}{\partial r}=\frac{-1}{r}\frac{\partial u}{\partial\theta}$

**Solution:**

We need to transform the Cauchy-Riemann (C-R) equations from Cartesian coordinates $(x,y)$ to polar coordinates $(r,\theta)$.

**Step 1: State the coordinate transformations.**
The relationships between Cartesian and polar coordinates are:
$$x = r\cos\theta$$
$$y = r\sin\theta$$
$$r^2 = x^2 + y^2 \implies r = \sqrt{x^2+y^2}$$
$$\theta = \tan^{-1}\left(\frac{y}{x}\right)$$

**Step 2: Calculate the partial derivatives of $r$ and $\theta$ with respect to $x$ and $y$.**
*   $\frac{\partial r}{\partial x} = \frac{\partial}{\partial x} (x^2+y^2)^{1/2} = \frac{1}{2}(x^2+y^2)^{-1/2}(2x) = \frac{x}{\sqrt{x^2+y^2}} = \frac{x}{r} = \cos\theta$
*   $\frac{\partial r}{\partial y} = \frac{\partial}{\partial y} (x^2+y^2)^{1/2} = \frac{1}{2}(x^2+y^2)^{-1/2}(2y) = \frac{y}{\sqrt{x^2+y^2}} = \frac{y}{r} = \sin\theta$
*   $\frac{\partial \theta}{\partial x} = \frac{\partial}{\partial x} \tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1+(y/x)^2} \cdot \left(-\frac{y}{x^2}\right) = \frac{x^2}{x^2+y^2} \left(-\frac{y}{x^2}\right) = -\frac{y}{r^2} = -\frac{r\sin\theta}{r^2} = -\frac{\sin\theta}{r}$
*   $\frac{\partial \theta}{\partial y} = \frac{\partial}{\partial y} \tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1+(y/x)^2} \cdot \left(\frac{1}{x}\right) = \frac{x^2}{x^2+y^2} \left(\frac{1}{x}\right) = \frac{x}{r^2} = \frac{r\cos\theta}{r^2} = \frac{\cos\theta}{r}$

**Step 3: Apply the multi-variable Chain Rule to $u$ and $v$.**
We can express the Cartesian partials of $u$ and $v$ in terms of their polar partials:
*   $u_x = \frac{\partial u}{\partial x} = \frac{\partial u}{\partial r}\frac{\partial r}{\partial x} + \frac{\partial u}{\partial \theta}\frac{\partial \theta}{\partial x} = u_r \cos\theta - u_\theta \frac{\sin\theta}{r}$
*   $u_y = \frac{\partial u}{\partial y} = \frac{\partial u}{\partial r}\frac{\partial r}{\partial y} + \frac{\partial u}{\partial \theta}\frac{\partial \theta}{\partial y} = u_r \sin\theta + u_\theta \frac{\cos\theta}{r}$
*   $v_x = \frac{\partial v}{\partial x} = \frac{\partial v}{\partial r}\frac{\partial r}{\partial x} + \frac{\partial v}{\partial \theta}\frac{\partial \theta}{\partial x} = v_r \cos\theta - v_\theta \frac{\sin\theta}{r}$
*   $v_y = \frac{\partial v}{\partial y} = \frac{\partial v}{\partial r}\frac{\partial r}{\partial y} + \frac{\partial v}{\partial \theta}\frac{\partial \theta}{\partial y} = v_r \sin\theta + v_\theta \frac{\cos\theta}{r}$

**Step 4: Substitute these into the Cartesian C-R equations.**
The Cartesian C-R equations are $u_x = v_y$ and $u_y = -v_x$.

Substitute into $u_x = v_y$:
$$u_r \cos\theta - u_\theta \frac{\sin\theta}{r} = v_r \sin\theta + v_\theta \frac{\cos\theta}{r} \quad \text{--- (Equation 1)}$$

Substitute into $u_y = -v_x$:
$$u_r \sin\theta + u_\theta \frac{\cos\theta}{r} = -\left( v_r \cos\theta - v_\theta \frac{\sin\theta}{r} \right)$$
$$u_r \sin\theta + u_\theta \frac{\cos\theta}{r} = -v_r \cos\theta + v_\theta \frac{\sin\theta}{r} \quad \text{--- (Equation 2)}$$

**Step 5: Solve the system of equations for $u_r$ and $v_r$.**
To isolate $u_r$, multiply Equation 1 by $\cos\theta$ and Equation 2 by $\sin\theta$, then add them together:
Eq1 * $\cos\theta$: $u_r \cos^2\theta - u_\theta \frac{\sin\theta\cos\theta}{r} = v_r \sin\theta\cos\theta + v_\theta \frac{\cos^2\theta}{r}$
Eq2 * $\sin\theta$: $u_r \sin^2\theta + u_\theta \frac{\cos\theta\sin\theta}{r} = -v_r \cos\theta\sin\theta + v_\theta \frac{\sin^2\theta}{r}$
Add the equations:
$u_r(\cos^2\theta + \sin^2\theta) + 0 = 0 + \frac{v_\theta}{r}(\cos^2\theta + \sin^2\theta)$
$$u_r = \frac{1}{r} v_\theta \implies \frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$$

To isolate $v_r$, multiply Equation 1 by $-\sin\theta$ and Equation 2 by $\cos\theta$, then add them together:
Eq1 * $-\sin\theta$: $-u_r \cos\theta\sin\theta + u_\theta \frac{\sin^2\theta}{r} = -v_r \sin^2\theta - v_\theta \frac{\cos\theta\sin\theta}{r}$
Eq2 * $\cos\theta$: $u_r \sin\theta\cos\theta + u_\theta \frac{\cos^2\theta}{r} = -v_r \cos^2\theta + v_\theta \frac{\sin\theta\cos\theta}{r}$
Add the equations:
$0 + \frac{u_\theta}{r}(\sin^2\theta + \cos^2\theta) = -v_r(\sin^2\theta + \cos^2\theta) + 0$
$$\frac{u_\theta}{r} = -v_r \implies v_r = -\frac{1}{r}u_\theta \implies \frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$$
**(Proved)**

***

### Q178. Prblm-3.4.4: $\frac{\partial^2\Psi}{\partial r^2}+\frac{1}{r}\frac{\partial\Psi}{\partial r}+\frac{1}{r^2}\frac{\partial^2\Psi}{\partial\theta^2}=0$ That is $\frac{\partial^2u}{\partial r^2}+\frac{1}{r}\frac{\partial u}{\partial r}+\frac{1}{r^2}\frac{\partial^2u}{\partial\theta^2}=0$ and $\frac{\partial^2v}{\partial r^2}+\frac{1}{r}\frac{\partial v}{\partial r}+\frac{1}{r^2}\frac{\partial^2v}{\partial\theta^2}=0$

*(Note: The question is asking to prove Laplace's equation in polar coordinates using the polar C-R equations derived in Q177).*

**Solution:**

We need to prove that the real part $u(r,\theta)$ and imaginary part $v(r,\theta)$ of an analytic function satisfy Laplace's equation in polar form.

**Step 1: State the Polar Cauchy-Riemann equations.**
From Q177, we know that if $f(z)$ is analytic, its components satisfy:
1.  $u_r = \frac{1}{r} v_\theta$
2.  $v_r = -\frac{1}{r} u_\theta \implies u_\theta = -r v_r$

**Step 2: Derive Laplace's equation for $u$.**
We need to find second-order partial derivatives. Let's differentiate the first C-R equation with respect to $r$:
$$\frac{\partial}{\partial r}(u_r) = \frac{\partial}{\partial r}\left(\frac{1}{r} v_\theta\right)$$
Using the product rule on the right side:
$$u_{rr} = -\frac{1}{r^2} v_\theta + \frac{1}{r} v_{\theta r} \quad \text{--- (Equation 3)}$$

Now, differentiate the second rearranged C-R equation ($u_\theta = -r v_r$) with respect to $\theta$:
$$\frac{\partial}{\partial \theta}(u_\theta) = \frac{\partial}{\partial \theta}(-r v_r)$$
Treating $r$ as a constant with respect to $\theta$:
$$u_{\theta\theta} = -r v_{r\theta} \quad \text{--- (Equation 4)}$$

By Clairaut's Theorem, mixed partial derivatives are equal: $v_{\theta r} = v_{r\theta}$.
From Equation 4, we can write $v_{\theta r} = -\frac{1}{r} u_{\theta\theta}$.

Substitute this $v_{\theta r}$ into Equation 3:
$$u_{rr} = -\frac{1}{r^2} v_\theta + \frac{1}{r} \left(-\frac{1}{r} u_{\theta\theta}\right)$$
$$u_{rr} = -\frac{1}{r^2} v_\theta - \frac{1}{r^2} u_{\theta\theta}$$

Notice that the term $v_\theta$ can be substituted out using the very first C-R equation ($v_\theta = r u_r$):
$$u_{rr} = -\frac{1}{r^2} (r u_r) - \frac{1}{r^2} u_{\theta\theta}$$
$$u_{rr} = -\frac{1}{r} u_r - \frac{1}{r^2} u_{\theta\theta}$$

Move all terms to the left side:
$$u_{rr} + \frac{1}{r} u_r + \frac{1}{r^2} u_{\theta\theta} = 0$$
This matches exactly the target equation: $\frac{\partial^2u}{\partial r^2}+\frac{1}{r}\frac{\partial u}{\partial r}+\frac{1}{r^2}\frac{\partial^2u}{\partial\theta^2}=0$. **(Proved for $u$)**

**Step 3: Derive Laplace's equation for $v$.**
We follow a very similar process. Differentiate the second C-R equation ($v_r = -\frac{1}{r} u_\theta$) with respect to $r$:
$$v_{rr} = \frac{1}{r^2} u_\theta - \frac{1}{r} u_{\theta r} \quad \text{--- (Equation 5)}$$

Differentiate the first rearranged C-R equation ($v_\theta = r u_r$) with respect to $\theta$:
$$v_{\theta\theta} = r u_{r\theta} \implies u_{r\theta} = \frac{1}{r} v_{\theta\theta}$$

Since $u_{\theta r} = u_{r\theta}$, substitute into Equation 5:
$$v_{rr} = \frac{1}{r^2} u_\theta - \frac{1}{r} \left(\frac{1}{r} v_{\theta\theta}\right)$$
$$v_{rr} = \frac{1}{r^2} u_\theta - \frac{1}{r^2} v_{\theta\theta}$$

Substitute $u_\theta = -r v_r$ (from the second C-R equation):
$$v_{rr} = \frac{1}{r^2} (-r v_r) - \frac{1}{r^2} v_{\theta\theta}$$
$$v_{rr} = -\frac{1}{r} v_r - \frac{1}{r^2} v_{\theta\theta}$$

Move all terms to the left side:
$$v_{rr} + \frac{1}{r} v_r + \frac{1}{r^2} v_{\theta\theta} = 0$$
This matches the target equation for $v$. **(Proved for $v$)**

***

### Q179. Problem-3.4.5: An analytic function with constant modulus is constant

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function defined in a region $R$. We are given that its modulus is a constant value $c$. We must prove that the entire function $f(z)$ is constant (i.e., $f'(z) = 0$ everywhere).

**Step 1: Set up the modulus condition.**
The modulus of $f(z)$ is given by $|f(z)| = \sqrt{u^2 + v^2}$.
Since the modulus is constant, let $|f(z)| = c$.
Squaring both sides gives:
$$u^2 + v^2 = c^2$$

If $c = 0$, then $u=0$ and $v=0$ everywhere, which means $f(z) = 0$, a constant. The proof is trivial. Let's assume $c > 0$.

**Step 2: Differentiate the modulus equation.**
Take the partial derivative of $u^2 + v^2 = c^2$ with respect to $x$:
$$2u \frac{\partial u}{\partial x} + 2v \frac{\partial v}{\partial x} = 0$$
Divide by 2:
$$u u_x + v v_x = 0 \quad \text{--- (Equation 1)}$$

Take the partial derivative with respect to $y$:
$$2u \frac{\partial u}{\partial y} + 2v \frac{\partial v}{\partial y} = 0$$
Divide by 2:
$$u u_y + v v_y = 0 \quad \text{--- (Equation 2)}$$

**Step 3: Apply the Cauchy-Riemann equations.**
Because $f(z)$ is analytic, $u_x = v_y$ and $u_y = -v_x$.
Substitute these into Equation 2 to express everything in terms of $x$-derivatives:
$$u (-v_x) + v (u_x) = 0$$
$$v u_x - u v_x = 0 \quad \text{--- (Equation 3)}$$

**Step 4: Solve the system of equations.**
We now have a system of two linear equations regarding the variables $u_x$ and $v_x$:
1) $u u_x + v v_x = 0$
2) $v u_x - u v_x = 0$

To eliminate $v_x$, multiply Eq 1 by $u$ and Eq 3 by $v$:
*   $u^2 u_x + uv v_x = 0$
*   $v^2 u_x - uv v_x = 0$

Add the two equations together:
$u_x(u^2 + v^2) = 0$
We know from Step 1 that $u^2 + v^2 = c^2$, and $c > 0$. Therefore, $c^2 \neq 0$.
The only way the product can be zero is if:
$$u_x = 0$$

Now, substitute $u_x = 0$ back into Equation 1:
$$u(0) + v v_x = 0 \implies v v_x = 0$$
If $v_x$ is not $0$, then $v$ must be $0$. But if $v=0$, since $u^2+v^2=c^2$, $u$ must be $\pm c$. If $u$ is a constant, then $u_x=0$ and $u_y=0$. In all valid cases requiring the C-R equations to hold:
$$v_x = 0$$

**Step 5: Conclude.**
We found that $u_x = 0$ and $v_x = 0$ everywhere in the region.
The derivative of the complex function can be written as:
$$f'(z) = u_x + i v_x$$
Substitute our results:
$$f'(z) = 0 + i(0) = 0$$
Since the derivative is zero everywhere in the region $R$, the function $f(z)$ must be a constant. **(Proved)**

***

### Q180. Prblm 3.4.6: Show that, $u=\frac{1}{2}\log(x^2+y^2)$ is harmonic & determine its conjugate & find $f(z)$.

*(Note: This is numerically and conceptually identical to Q138 and Q143. Detailed steps are provided below).*

**Solution:**

Given $u(x,y) = \frac{1}{2}\ln(x^2 + y^2)$.

**Part a) Show $u$ is harmonic.**
1.  **First derivatives:**
    $$u_x = \frac{\partial}{\partial x} \left( \frac{1}{2}\ln(x^2+y^2) \right) = \frac{1}{2} \cdot \frac{2x}{x^2+y^2} = \frac{x}{x^2+y^2}$$
    $$u_y = \frac{\partial}{\partial y} \left( \frac{1}{2}\ln(x^2+y^2) \right) = \frac{1}{2} \cdot \frac{2y}{x^2+y^2} = \frac{y}{x^2+y^2}$$
2.  **Second derivatives (using quotient rule):**
    $$u_{xx} = \frac{1\cdot(x^2+y^2) - x\cdot(2x)}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}$$
    $$u_{yy} = \frac{1\cdot(x^2+y^2) - y\cdot(2y)}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2}$$
3.  **Check Laplace's equation:**
    $$u_{xx} + u_{yy} = \frac{y^2-x^2 + x^2-y^2}{(x^2+y^2)^2} = 0$$
Since $\nabla^2 u = 0$, $u$ is **harmonic**.

---

**Part b) Find the harmonic conjugate $v(x,y)$.**
Using the Cauchy-Riemann equations $v_y = u_x$ and $v_x = -u_y$.
1.  **Integrate $v_y$:**
    $$v_y = \frac{x}{x^2+y^2} \implies v = \int \frac{x}{x^2+y^2} dy = \tan^{-1}\left(\frac{y}{x}\right) + g(x)$$
2.  **Differentiate and use $v_x = -u_y$:**
    $$v_x = \frac{\partial}{\partial x}\left( \tan^{-1}\left(\frac{y}{x}\right) + g(x) \right) = -\frac{y}{x^2+y^2} + g'(x)$$
    Equate to $-u_y = -\frac{y}{x^2+y^2}$:
    $$-\frac{y}{x^2+y^2} + g'(x) = -\frac{y}{x^2+y^2} \implies g'(x) = 0 \implies g(x) = C$$
3.  **Final conjugate:**
    **$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + C$**

---

**Part c) Find $f(z)$ in terms of $z$.**
$$f(z) = u + iv = \frac{1}{2}\ln(x^2+y^2) + i\left(\tan^{-1}\left(\frac{y}{x}\right) + C\right)$$
Using the Milne-Thomson method (substitute $x=z, y=0$):
$$f(z) = \frac{1}{2}\ln(z^2) + i(\tan^{-1}(0) + C)$$
Using log properties:
$$f(z) = \ln(z) + iC$$

**Answer:** 
*   **$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + C$**
*   **$f(z) = \ln z + iC$**



Here are the detailed solutions for the next four questions (Q181 to Q184).

### Q181. Prblm 3.4.7: $\Psi=\tan^{-1}(y/x)$ Find $\phi=?$

*(Note: This is exactly identical to Q136, but uses $\Psi$ (Psi) and $\phi$ (Phi) instead of $\psi$ and $\phi$. In fluid dynamics or electromagnetism, $\phi$ is the scalar potential (real part) and $\Psi$ is the stream function (imaginary part) of the complex potential $F(z) = \phi + i\Psi$. We will re-derive the solution).*

**Solution:**

We are given the imaginary part $\Psi(x,y) = \tan^{-1}(y/x)$ of an analytic function $F(z) = \phi + i\Psi$. We need to find the real part $\phi(x,y)$ using the Cauchy-Riemann equations: $\phi_x = \Psi_y$ and $\phi_y = -\Psi_x$.

**Step 1: Calculate the partial derivatives of $\Psi$.**
Using the chain rule $\frac{d}{dw}\tan^{-1}(w) = \frac{1}{1+w^2}$:
*   $\Psi_x = \frac{\partial}{\partial x}\tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1+(y/x)^2} \cdot \frac{\partial}{\partial x}\left(yx^{-1}\right) = \frac{x^2}{x^2+y^2} \cdot \left(-yx^{-2}\right) = -\frac{y}{x^2+y^2}$
*   $\Psi_y = \frac{\partial}{\partial y}\tan^{-1}\left(\frac{y}{x}\right) = \frac{1}{1+(y/x)^2} \cdot \frac{\partial}{\partial y}\left(\frac{y}{x}\right) = \frac{x^2}{x^2+y^2} \cdot \left(\frac{1}{x}\right) = \frac{x}{x^2+y^2}$

**Step 2: Use the C-R equations to establish $\phi_x$ and $\phi_y$.**
*   From $\phi_x = \Psi_y$: $\phi_x = \frac{x}{x^2+y^2}$
*   From $\phi_y = -\Psi_x$: $\phi_y = -\left(-\frac{y}{x^2+y^2}\right) = \frac{y}{x^2+y^2}$

**Step 3: Integrate $\phi_x$ with respect to $x$ to find $\phi(x,y)$.**
$$\phi(x,y) = \int \frac{x}{x^2+y^2} dx$$
Let $u = x^2+y^2 \implies du = 2xdx \implies \frac{1}{2}du = xdx$.
$$\phi(x,y) = \frac{1}{2}\int \frac{1}{u} du = \frac{1}{2}\ln(u) + g(y) = \frac{1}{2}\ln(x^2+y^2) + g(y)$$

**Step 4: Differentiate with respect to $y$ and solve for $g(y)$.**
$$\phi_y = \frac{\partial}{\partial y}\left(\frac{1}{2}\ln(x^2+y^2) + g(y)\right) = \frac{1}{2}\frac{1}{x^2+y^2}(2y) + g'(y) = \frac{y}{x^2+y^2} + g'(y)$$

Equate this to the $\phi_y$ found in Step 2:
$$\frac{y}{x^2+y^2} + g'(y) = \frac{y}{x^2+y^2}$$
$$g'(y) = 0 \implies g(y) = C$$ (where $C$ is a real constant).

**Step 5: Write the final function $\phi(x,y)$.**
Substitute $g(y)$ back into the expression for $\phi$:
$$\phi(x,y) = \frac{1}{2}\ln(x^2+y^2) + C$$

**Answer:** The velocity potential is **$\phi(x,y) = \frac{1}{2}\ln(x^2+y^2) + C$**.

***

### Q182. Problem 3.1.1: Test the analyticity of the function $f(z)=\overline{z}$

*(Note: This is numerically and conceptually identical to Q139 and Q165. A brief step-by-step solution is provided below).*

**Solution:**

To test if $f(z) = \overline{z}$ is analytic, we separate it into real and imaginary parts and check if they satisfy the Cauchy-Riemann equations.

**Step 1: Separate into $u$ and $v$.**
Let $z = x + iy$.
$$f(z) = \overline{x + iy} = x - iy$$
*   Real part: $u(x,y) = x$
*   Imaginary part: $v(x,y) = -y$

**Step 2: Calculate partial derivatives.**
*   $u_x = 1$
*   $u_y = 0$
*   $v_x = 0$
*   $v_y = -1$

**Step 3: Test the Cauchy-Riemann equations.**
1.  **Does $u_x = v_y$?**
    $1 \neq -1$. This equation is false everywhere.
2.  **Does $u_y = -v_x$?**
    $0 = 0$. This is true, but both equations must be simultaneously satisfied.

**Conclusion:**
Because the primary Cauchy-Riemann equation fails everywhere in the complex plane, the function has no derivative anywhere. Therefore, it cannot be analytic anywhere.

**Answer:** The function $f(z) = \overline{z}$ is **not analytic** anywhere.

***

### Q183. Problem 3.1.2: Prove that a (i) necessary and (ii) sufficient condition that $w=f(z)=u(x,y)+iv(x,y)$ be analytic in a region R is that the Cauchy-Riemann equations $\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},$ $\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$ are satisfied in R where it is supposed that these partial derivatives are continuous in R.

**Solution:**

This is the foundational proof linking complex differentiability to real partial derivatives. 

---
**Part (i): Prove the Necessary Condition**
*(If $f(z)$ is analytic, then C-R equations must hold).*

Assume $f(z)$ is analytic in $R$. This means the derivative $f'(z)$ exists uniquely at every point $z \in R$ regardless of how $\Delta z \to 0$.
$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z+\Delta z) - f(z)}{\Delta z}$$
Let $\Delta z = \Delta x + i\Delta y$.

**Case A: Approach along the real axis ($\Delta y = 0$, $\Delta x \to 0$).**
$$f'(z) = \lim_{\Delta x \to 0} \frac{[u(x+\Delta x, y) + iv(x+\Delta x, y)] - [u(x,y) + iv(x,y)]}{\Delta x}$$
$$f'(z) = \lim_{\Delta x \to 0} \frac{u(x+\Delta x, y) - u(x,y)}{\Delta x} + i \lim_{\Delta x \to 0} \frac{v(x+\Delta x, y) - v(x,y)}{\Delta x}$$
By the definition of partial derivatives:
$$f'(z) = u_x + iv_x \quad \text{--- (Equation 1)}$$

**Case B: Approach along the imaginary axis ($\Delta x = 0$, $\Delta y \to 0$).**
$$f'(z) = \lim_{\Delta y \to 0} \frac{[u(x, y+\Delta y) + iv(x, y+\Delta y)] - [u(x,y) + iv(x,y)]}{i\Delta y}$$
$$f'(z) = \lim_{\Delta y \to 0} \frac{u(x, y+\Delta y) - u(x,y)}{i\Delta y} + i \lim_{\Delta y \to 0} \frac{v(x, y+\Delta y) - v(x,y)}{i\Delta y}$$
Pulling $1/i = -i$ out:
$$f'(z) = -i u_y + v_y = v_y - iu_y \quad \text{--- (Equation 2)}$$

Since $f'(z)$ is unique, Equation 1 must equal Equation 2:
$$u_x + iv_x = v_y - iu_y$$
Equating real and imaginary parts yields the C-R equations: $u_x = v_y$ and $u_y = -v_x$. **(Necessary condition proved)**.

---
**Part (ii): Prove the Sufficient Condition**
*(If C-R equations hold and partials are continuous, then $f(z)$ is analytic).*

Assume $u_x, u_y, v_x, v_y$ are continuous and satisfy C-R equations. We must prove $f'(z)$ exists.
Let $\Delta z = \Delta x + i\Delta y$.
The change in the function is $\Delta f = f(z+\Delta z) - f(z) = \Delta u + i\Delta v$.

Because the partial derivatives are continuous, we can use the multi-variable linear approximation (Total Differential theorem) for small $\Delta x, \Delta y$:
$$\Delta u = u_x\Delta x + u_y\Delta y + \varepsilon_1\Delta x + \epsilon_2\Delta y$$
$$\Delta v = v_x\Delta x + v_y\Delta y + \varepsilon_3\Delta x + \epsilon_4\Delta y$$
where $\varepsilon_1, \varepsilon_2, \varepsilon_3, \varepsilon_4 \to 0$ as $\Delta x, \Delta y \to 0$.

Substitute these into $\Delta f$:
$$\Delta f = (u_x\Delta x + u_y\Delta y) + i(v_x\Delta x + v_y\Delta y) + E$$
(where $E$ represents the sum of the infinitesimal error terms).

Now, use the C-R equations ($u_y = -v_x$ and $v_y = u_x$) to replace the $y$-derivatives:
$$\Delta f = (u_x\Delta x - v_x\Delta y) + i(v_x\Delta x + u_x\Delta y) + E$$
Rearrange to group $u_x$ and $v_x$:
$$\Delta f = u_x(\Delta x + i\Delta y) + iv_x(\Delta x + i\Delta y) + E$$
Notice that $\Delta x + i\Delta y = \Delta z$:
$$\Delta f = u_x(\Delta z) + iv_x(\Delta z) + E$$
$$\Delta f = (u_x + iv_x)\Delta z + E$$

Divide by $\Delta z$:
$$\frac{\Delta f}{\Delta z} = u_x + iv_x + \frac{E}{\Delta z}$$

Take the limit as $\Delta z \to 0$. Because the partials are continuous, the error term fraction $\frac{E}{\Delta z}$ strictly approaches $0$.
$$\lim_{\Delta z \to 0} \frac{\Delta f}{\Delta z} = u_x + iv_x$$
Because this limit exists as a finite unique value, $f'(z)$ exists, meaning $f(z)$ is analytic. **(Sufficient condition proved)**.

***

### Q184. Problem 3.1.3: Test the analyticity of the following function $(i)f(z)=ize^{-z}$ (ii) $f(z) = ze^{-z}$

*(Note: These two functions were solved identically in Q166 and Q167 respectively. I will provide a condensed summary of the C-R checks).*

**Solution:**

To test analyticity, we must separate into $u+iv$ and verify $u_x = v_y$ and $u_y = -v_x$.

**Part (i): $f(z) = ize^{-z}$**
1.  **Substitute $z = x+iy$:** $f(z) = i(x+iy)e^{-x-iy} = (-y+ix)e^{-x}(\cos y - i\sin y)$.
2.  **Separate $u$ and $v$:**
    *   $u(x,y) = e^{-x}(-y\cos y + x\sin y)$
    *   $v(x,y) = e^{-x}(x\cos y + y\sin y)$
3.  **Partial derivatives:**
    *   $u_x = e^{-x}(\sin y - x\sin y + y\cos y) \cdot (-1) = e^{-x}(x\sin y - \sin y - y\cos y)$ (Correction from Q166 step, applying product rule carefully: $u_x = \frac{\partial}{\partial x}(e^{-x}x\sin y - e^{-x}y\cos y) = (\sin y(e^{-x} - xe^{-x})) - (-e^{-x}y\cos y) = e^{-x}(\sin y - x\sin y + y\cos y)$)
    *   $u_y = e^{-x}(-y(-\sin y) - \cos y + x\cos y) = e^{-x}(y\sin y - \cos y + x\cos y)$
    *   $v_x = \frac{\partial}{\partial x}(e^{-x}x\cos y + e^{-x}y\sin y) = \cos y(e^{-x} - xe^{-x}) + (-e^{-x}y\sin y) = e^{-x}(\cos y - x\cos y - y\sin y)$
    *   $v_y = e^{-x}(x(-\sin y) + y\cos y + \sin y) = e^{-x}(-x\sin y + y\cos y + \sin y)$
4.  **Check C-R equations:**
    *   $u_x = v_y$: $e^{-x}(\sin y - x\sin y + y\cos y) = e^{-x}(\sin y - x\sin y + y\cos y)$. (True)
    *   $u_y = -v_x$: $e^{-x}(y\sin y - \cos y + x\cos y) = -[e^{-x}(\cos y - x\cos y - y\sin y)]$. (True)
Since C-R equations hold everywhere, **$f(z) = ize^{-z}$ is analytic**.

**Part (ii): $f(z) = ze^{-z}$**
1.  **Substitute $z = x+iy$:** $f(z) = (x+iy)e^{-x-iy} = (x+iy)e^{-x}(\cos y - i\sin y)$.
2.  **Separate $u$ and $v$:**
    *   $u(x,y) = e^{-x}(x\cos y + y\sin y)$
    *   $v(x,y) = e^{-x}(y\cos y - x\sin y)$
3.  **Partial derivatives:**
    *   $u_x = e^{-x}(\cos y - x\cos y - y\sin y)$
    *   $u_y = e^{-x}(-x\sin y + \sin y + y\cos y)$
    *   $v_x = e^{-x}(-y\cos y - \sin y + x\sin y) = -e^{-x}(y\cos y + \sin y - x\sin y)$
    *   $v_y = e^{-x}(\cos y - y\sin y - x\cos y)$
4.  **Check C-R equations:**
    *   $u_x = v_y$: $e^{-x}(\cos y - x\cos y - y\sin y) = e^{-x}(\cos y - x\cos y - y\sin y)$. (True)
    *   $u_y = -v_x$: $e^{-x}(-x\sin y + \sin y + y\cos y) = -[-e^{-x}(y\cos y + \sin y - x\sin y)]$. (True)
Since C-R equations hold everywhere, **$f(z) = ze^{-z}$ is analytic**.

Here are the detailed solutions for the next four questions (Q185 to Q188). 

*(Note: These questions from the Feruj Sheet are identical to earlier questions from the Firoz Note section. Detailed step-by-step solutions are provided again below for completeness).*

### Q185. Problem 3.2.1: Prove that real and imaginary parts of an analytic function $f(z)$ of a complex variable satisfy Laplace's equation.

*(This is identical to Q137 and Q168).*

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function defined in a region $R$. We must prove that its real part $u$ and imaginary part $v$ satisfy Laplace's equation: $\frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0$.

**Step 1: State the Cauchy-Riemann equations.**
Because $f(z)$ is analytic in $R$, it must satisfy the C-R equations everywhere in $R$:
1.  $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$
2.  $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$

Additionally, the analyticity of $f(z)$ guarantees that all second-order partial derivatives of $u$ and $v$ exist and are continuous.

**Step 2: Prove $u(x,y)$ is harmonic.**
Take the partial derivative of the first C-R equation with respect to $x$:
$$\frac{\partial^2 u}{\partial x^2} = \frac{\partial^2 v}{\partial x \partial y}$$
Take the partial derivative of the second C-R equation with respect to $y$:
$$\frac{\partial^2 u}{\partial y^2} = -\frac{\partial^2 v}{\partial y \partial x}$$

Add these two new equations together:
$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \frac{\partial^2 v}{\partial x \partial y} - \frac{\partial^2 v}{\partial y \partial x}$$

By Clairaut's Theorem, because the mixed partial derivatives are continuous, the order of differentiation does not matter: $\frac{\partial^2 v}{\partial x \partial y} = \frac{\partial^2 v}{\partial y \partial x}$. Therefore, their difference is zero.
$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$
Thus, $u$ satisfies Laplace's equation. **(Proved)**

**Step 3: Prove $v(x,y)$ is harmonic.**
Take the partial derivative of the first C-R equation with respect to $y$:
$$\frac{\partial^2 u}{\partial y \partial x} = \frac{\partial^2 v}{\partial y^2}$$
Take the partial derivative of the second C-R equation with respect to $x$:
$$\frac{\partial^2 u}{\partial x \partial y} = -\frac{\partial^2 v}{\partial x^2}$$
Rearrange this to: $\frac{\partial^2 v}{\partial x^2} = -\frac{\partial^2 u}{\partial x \partial y}$

Add the equations for $v_{xx}$ and $v_{yy}$ together:
$$\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = -\frac{\partial^2 u}{\partial x \partial y} + \frac{\partial^2 u}{\partial y \partial x}$$

Again, by Clairaut's Theorem, the mixed partials of $u$ are equal, so their sum is zero.
$$\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$
Thus, $v$ satisfies Laplace's equation. **(Proved)**

***

### Q186. Problem 3.2.2: Show that $f(z)=\vert{}z\vert{}^{2}$ is differentiable at $z=0$ but not analytic at $z=0.$

*(This is identical to Q134 and Q169).*

**Solution:**

**Part 1: Show it is differentiable at $z=0$.**
We use the formal limit definition of the derivative:
$$f'(0) = \lim_{\Delta z \to 0} \frac{f(0 + \Delta z) - f(0)}{\Delta z}$$
$$f'(0) = \lim_{\Delta z \to 0} \frac{|\Delta z|^2 - |0|^2}{\Delta z}$$
Using the property $|w|^2 = w\overline{w}$, we substitute $|\Delta z|^2 = \Delta z \cdot \overline{\Delta z}$:
$$f'(0) = \lim_{\Delta z \to 0} \frac{\Delta z \cdot \overline{\Delta z}}{\Delta z}$$
Cancel the $\Delta z$ terms (valid since $\Delta z \neq 0$ during the limit approach):
$$f'(0) = \lim_{\Delta z \to 0} \overline{\Delta z}$$
As the complex number $\Delta z$ approaches zero, its conjugate also clearly approaches zero.
$$f'(0) = 0$$
Because this limit exists and gives a single finite value regardless of the approach path, **the function is differentiable at $z=0$.**

---

**Part 2: Show it is not analytic at $z=0$.**
A function is **analytic** at a point $z_0$ only if it is differentiable at $z_0$ *and* everywhere in some open neighborhood surrounding $z_0$.
Let's test differentiability at any general point using the Cauchy-Riemann equations.

Let $z = x + iy$.
$$f(z) = |z|^2 = x^2 + y^2$$
This function is purely real, so:
*   $u(x,y) = x^2 + y^2$
*   $v(x,y) = 0$

Calculate the partial derivatives:
*   $u_x = 2x$
*   $u_y = 2y$
*   $v_x = 0$
*   $v_y = 0$

Check the Cauchy-Riemann equations:
1) $u_x = v_y \implies 2x = 0 \implies x = 0$
2) $u_y = -v_x \implies 2y = 0 \implies y = 0$

The equations are only true when $x=0$ AND $y=0$ simultaneously. At any other point in the complex plane (e.g., $z=0.001$), the equations fail. Therefore, the function is not differentiable anywhere except the origin. Because it lacks a neighborhood of differentiability, **it is not analytic at $z=0$.**

***

### Q187. Problem 3.2.3: Show that (a) $u=x^{3}-3xy^{2}+3x^{2}-3y^{2}+1$ is harmonic. (b) Find v such that $f(z)=u+iv$ is analytic. (c) Find also, $f(z)$ in terms of z.

*(This is identical to Q170).*

**Solution:**

Given $u(x,y) = x^3 - 3xy^2 + 3x^2 - 3y^2 + 1$.

**Part (a): Show $u$ is harmonic.**
Verify Laplace's equation: $u_{xx} + u_{yy} = 0$.
1.  **First derivatives:**
    $u_x = 3x^2 - 3y^2 + 6x$
    $u_y = -6xy - 6y$
2.  **Second derivatives:**
    $u_{xx} = \frac{\partial}{\partial x}(3x^2 - 3y^2 + 6x) = 6x + 6$
    $u_{yy} = \frac{\partial}{\partial y}(-6xy - 6y) = -6x - 6$
3.  **Check Laplace's equation:**
    $u_{xx} + u_{yy} = (6x + 6) + (-6x - 6) = 0$.
**$u$ is a harmonic function.** (Proved)

---

**Part (b): Find the harmonic conjugate $v(x,y)$.**
Use the Cauchy-Riemann equations: $v_y = u_x$ and $v_x = -u_y$.
1.  **Integrate $v_y$:**
    $v_y = u_x = 3x^2 - 3y^2 + 6x$
    $$v(x,y) = \int (3x^2 - 3y^2 + 6x) dy = 3x^2y - y^3 + 6xy + g(x)$$
2.  **Differentiate with respect to $x$:**
    $$v_x = \frac{\partial}{\partial x}(3x^2y - y^3 + 6xy + g(x)) = 6xy + 6y + g'(x)$$
3.  **Use the second C-R equation:**
    We know $-u_y = -(-6xy - 6y) = 6xy + 6y$.
    Equate to $v_x$:
    $$6xy + 6y + g'(x) = 6xy + 6y \implies g'(x) = 0 \implies g(x) = C$$
4.  **Final conjugate:**
    **$v(x,y) = 3x^2y - y^3 + 6xy + C$**

---

**Part (c): Find $f(z)$ in terms of $z$.**
Use the Milne-Thomson method. Substitute $x=z$ and $y=0$ directly into $u$ and $v$:
*   $u(z,0) = z^3 - 3z(0)^2 + 3z^2 - 3(0)^2 + 1 = z^3 + 3z^2 + 1$
*   $v(z,0) = 3z^2(0) - 0^3 + 6z(0) + C = C$

Construct the function:
$$f(z) = u(z,0) + iv(z,0)$$
$$f(z) = (z^3 + 3z^2 + 1) + i(C)$$
Let $C_1 = iC$.
**Answer: $f(z) = z^3 + 3z^2 + 1 + C_1$**

***

### Q188. Problem 3.2.4: Show that (a) $u=2x(1-y)$ is harmonic. (b) Find v such that $f(z)=u+iv$ is analytic. (c) Find also, $f(z)=u+iv$ in term of z.

*(This is identical to Q135 and Q171).*

**Solution:**

Given $u(x,y) = 2x(1-y) = 2x - 2xy$.

**Part (a): Show $u$ is harmonic.**
1.  First derivatives: $u_x = 2 - 2y$, $u_y = -2x$.
2.  Second derivatives: $u_{xx} = 0$, $u_{yy} = 0$.
3.  Check Laplace's equation: $u_{xx} + u_{yy} = 0 + 0 = 0$.
**$u$ is a harmonic function.** (Proved)

---

**Part (b): Find the harmonic conjugate $v(x,y)$.**
1.  From C-R equation $v_y = u_x$:
    $$v_y = 2 - 2y$$
2.  Integrate with respect to $y$:
    $$v(x,y) = \int (2 - 2y) dy = 2y - y^2 + g(x)$$
3.  Differentiate with respect to $x$:
    $$v_x = g'(x)$$
4.  Use C-R equation $v_x = -u_y$:
    $$g'(x) = -(-2x) = 2x$$
5.  Integrate with respect to $x$:
    $$g(x) = \int 2x dx = x^2 + C$$
6.  Final conjugate:
    **$v(x,y) = 2y - y^2 + x^2 + C$**

---

**Part (c): Find $f(z)$ in terms of $z$.**
Use the Milne-Thomson method. Substitute $x=z$ and $y=0$ directly into $u$ and $v$:
*   $u(z,0) = 2z(1 - 0) = 2z$
*   $v(z,0) = 2(0) - 0^2 + z^2 + C = z^2 + C$

Construct the function:
$$f(z) = u(z,0) + iv(z,0)$$
$$f(z) = 2z + i(z^2 + C)$$
**Answer: $f(z) = iz^2 + 2z + iC$**

Here are the detailed solutions for the next four questions (Q189 to Q192).

### Q189. Problem 3.2.4(Milne-thomson rule): If $u_{1}(x,y)=\frac{\partial u}{\partial x}$ and $u_{2}(x,y)=\frac{\partial u}{\partial y}$ prove that $f^{\prime}(z)=u_{1}(z,0)-iu_{2}(z,0)=[\frac{\partial u}{\partial x}]_{y=0}-i[\frac{\partial u}{\partial y}]_{y=0}.$

*(Note: This is identical to Q172. The proof is provided below).*

**Solution:**

The Milne-Thomson rule provides a direct method to find the derivative $f'(z)$ of an analytic function $f(z)$ using only its real part $u(x,y)$.

**Step 1: Write the definition of the complex derivative.**
Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function.
Its derivative with respect to $z$ can be written using partial derivatives with respect to the real variable $x$:
$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$$
Using the notation provided in the question ($u_1 = \frac{\partial u}{\partial x}$):
$$f'(z) = u_1(x,y) + i\frac{\partial v}{\partial x}$$

**Step 2: Apply the Cauchy-Riemann equations.**
To express the derivative entirely in terms of $u$, we must eliminate the $\frac{\partial v}{\partial x}$ term.
Because $f(z)$ is analytic, the Cauchy-Riemann equations hold:
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \implies \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}$$
Using the notation provided in the question ($u_2 = \frac{\partial u}{\partial y}$), we substitute this into the derivative:
$$f'(z) = u_1(x,y) - i u_2(x,y) \quad \text{--- (Equation 1)}$$

**Step 3: Convert the function to be strictly in terms of $z$.**
Since $f(z)$ is analytic, its derivative $f'(z)$ is also analytic. An analytic function can be expressed purely as a function of the complex variable $z$, independent of the specific independent values of $x$ and $y$. This means the identity holds for any arbitrary path or coordinate assignment in the complex plane.
A very convenient assignment to isolate $z$ is to evaluate the function strictly along the real axis, where $y = 0$.
If $y = 0$, then $z = x + iy \implies z = x + 0 \implies x = z$.

**Step 4: Substitute the variables.**
Substitute $x = z$ and $y = 0$ directly into Equation 1:
$$f'(z) = u_1(z,0) - i u_2(z,0)$$
Or, written in standard partial derivative notation:
$$f'(z) = \left[ \frac{\partial u}{\partial x} \right]_{y=0, x=z} - i \left[ \frac{\partial u}{\partial y} \right]_{y=0, x=z}$$
**(Proved)**

***

### Q190. Problem 3.2.5 (Milne-thomson rule): If $v_{1}(x,y)=\frac{\partial v}{\partial y}$ and $v_{2}(x,y)=\frac{\partial v}{\partial x}$ , Prove that $f^{\prime}(z)=v_{1}(z,0)+iv_{2}(z,0)=[\frac{\partial v}{\partial y}]_{y=0}+i[\frac{\partial v}{\partial x}]_{y=0}.$

**Solution:**

This is the alternative form of the Milne-Thomson rule, used to construct the derivative $f'(z)$ strictly from the imaginary part $v(x,y)$.

**Step 1: Write the definition of the complex derivative.**
Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function.
The complex derivative expressed using partial derivatives with respect to $x$ is:
$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$$
Using the notation provided in the question ($v_2 = \frac{\partial v}{\partial x}$):
$$f'(z) = \frac{\partial u}{\partial x} + i v_2(x,y)$$

**Step 2: Apply the Cauchy-Riemann equations.**
We want to eliminate $u$ from this expression. 
The first Cauchy-Riemann equation states:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
Using the notation provided in the question ($v_1 = \frac{\partial v}{\partial y}$), we substitute this into the derivative:
$$f'(z) = v_1(x,y) + i v_2(x,y) \quad \text{--- (Equation 1)}$$

**Step 3: Convert the function to be strictly in terms of $z$.**
Because the derivative $f'(z)$ is an analytic function, it can be written strictly as a function of the variable $z = x+iy$. 
To easily convert the $(x,y)$ coordinate system back to $z$, we evaluate the function on the real axis by setting $y = 0$.
When $y = 0$, $z = x + i(0) \implies x = z$.

**Step 4: Substitute the variables.**
Substitute $x = z$ and $y = 0$ directly into Equation 1:
$$f'(z) = v_1(z,0) + i v_2(z,0)$$
Or, written in standard partial derivative notation:
$$f'(z) = \left[ \frac{\partial v}{\partial y} \right]_{y=0, x=z} + i \left[ \frac{\partial v}{\partial x} \right]_{y=0, x=z}$$
**(Proved)**

***

### Q191. Problem 3.2.5: If $Im\{f^{\prime}(z)\}=6x(2y-1)$ and $f(0)=3-2i$ $f(1)=6-5i$ Find $f(z)$ and $f(1+i)$.

**Solution:**

We are given the imaginary part of the derivative, $Im\{f'(z)\}$, and two boundary conditions to find the exact function $f(z)$. Let $f(z) = u(x,y) + iv(x,y)$. The derivative is $f'(z) = u_x + iv_x$.
Therefore, $Im\{f'(z)\} = v_x = 6x(2y-1) = 12xy - 6x$.

**Step 1: Integrate to find $v(x,y)$.**
$$v(x,y) = \int (12xy - 6x) dx$$
$$v(x,y) = 6x^2y - 3x^2 + h(y)$$

**Step 2: Use the Cauchy-Riemann equations to find $u(x,y)$.**
We know $u_y = -v_x$:
$$u_y = -12xy + 6x$$
Integrate with respect to $y$:
$$u(x,y) = \int (-12xy + 6x) dy$$
$$u(x,y) = -6xy^2 + 6xy + g(x)$$

**Step 3: Reconcile $g(x)$ and $h(y)$ using the other C-R equation.**
We know $u_x = v_y$. Calculate both from our current expressions:
*   $u_x = \frac{\partial}{\partial x}(-6xy^2 + 6xy + g(x)) = -6y^2 + 6y + g'(x)$
*   $v_y = \frac{\partial}{\partial y}(6x^2y - 3x^2 + h(y)) = 6x^2 + h'(y)$

Equate them:
$$-6y^2 + 6y + g'(x) = 6x^2 + h'(y)$$
Isolate $x$ terms and $y$ terms on opposite sides:
$$g'(x) - 6x^2 = h'(y) + 6y^2 - 6y$$
Because the left side is purely a function of $x$ and the right side is purely a function of $y$, they must both equal a constant $C_1$:
*   $g'(x) - 6x^2 = C_1 \implies g'(x) = 6x^2 + C_1 \implies g(x) = 2x^3 + C_1x + C_2$
*   $h'(y) + 6y^2 - 6y = C_1 \implies h'(y) = -6y^2 + 6y + C_1 \implies h(y) = -2y^3 + 3y^2 + C_1y + C_3$

Substitute these back into $u$ and $v$:
*   $u(x,y) = -6xy^2 + 6xy + 2x^3 + C_1x + C_2$
*   $v(x,y) = 6x^2y - 3x^2 - 2y^3 + 3y^2 + C_1y + C_3$

**Step 4: Construct $f(z)$ using the Milne-Thomson method.**
Set $x=z, y=0$:
*   $u(z,0) = 2z^3 + C_1z + C_2$
*   $v(z,0) = -3z^2 + C_3$
$$f(z) = u(z,0) + iv(z,0)$$
$$f(z) = (2z^3 + C_1z + C_2) + i(-3z^2 + C_3)$$
$$f(z) = 2z^3 - 3iz^2 + C_1z + (C_2 + iC_3)$$
Let the complex constant $C = C_2 + iC_3$.
$$f(z) = 2z^3 - 3iz^2 + C_1z + C$$

**Step 5: Apply boundary conditions to find the constants.**
*Condition 1: $f(0) = 3 - 2i$*
$$f(0) = 2(0)^3 - 3i(0)^2 + C_1(0) + C = 3 - 2i \implies C = 3 - 2i$$
So, $f(z) = 2z^3 - 3iz^2 + C_1z + 3 - 2i$.

*Condition 2: $f(1) = 6 - 5i$*
$$f(1) = 2(1)^3 - 3i(1)^2 + C_1(1) + 3 - 2i = 6 - 5i$$
$$2 - 3i + C_1 + 3 - 2i = 6 - 5i$$
$$5 - 5i + C_1 = 6 - 5i$$
$$C_1 = 1$$

The exact analytic function is:
**$f(z) = 2z^3 - 3iz^2 + z + 3 - 2i$**

**Step 6: Evaluate $f(1+i)$.**
Substitute $z = 1+i$:
*   $z = 1+i$
*   $z^2 = (1+i)^2 = 1 + 2i + i^2 = 2i$
*   $z^3 = z \cdot z^2 = (1+i)(2i) = 2i + 2i^2 = -2 + 2i$

Substitute these into $f(z)$:
$$f(1+i) = 2(-2 + 2i) - 3i(2i) + (1 + i) + 3 - 2i$$
$$f(1+i) = -4 + 4i - 6i^2 + 1 + i + 3 - 2i$$
Since $i^2 = -1$:
$$f(1+i) = -4 + 4i + 6 + 1 + i + 3 - 2i$$
Group the real and imaginary numbers:
$$f(1+i) = (-4 + 6 + 1 + 3) + i(4 + 1 - 2)$$
$$f(1+i) = 6 + 3i$$

**Answer:**
*   **$f(z) = 2z^3 - 3iz^2 + z + 3 - 2i$**
*   **$f(1+i) = 6 + 3i$**

***

### Q192. Question: Let $u(x,y)=\alpha$ and $v(x,y)=\beta$, where u and v are the real and imaginary parts of an analytic function $f(z)$ and $\alpha$ and $\beta$ are any constants, represent two families of curves. Prove that the families are orthogonal.

**Solution:**

We must prove that the families of level curves (equipotential lines and streamlines) of the real and imaginary parts of an analytic function always intersect at right angles ($90^\circ$ or orthogonal).
Two curves are orthogonal at their point of intersection if the product of their slopes at that point is $-1$.

**Step 1: Find the slope of the curve $u(x,y) = \alpha$.**
Take the total implicit derivative of the equation $u(x,y) = \alpha$ with respect to $x$:
$$\frac{d}{dx} u(x,y) = \frac{d}{dx}(\alpha)$$
By the multivariable chain rule:
$$\frac{\partial u}{\partial x} \frac{dx}{dx} + \frac{\partial u}{\partial y} \frac{dy}{dx} = 0$$
$$u_x + u_y \frac{dy}{dx} = 0$$
Let the slope of this curve be $m_1 = \frac{dy}{dx}$. Solving for $m_1$:
$$m_1 = -\frac{u_x}{u_y}$$

**Step 2: Find the slope of the curve $v(x,y) = \beta$.**
Take the total implicit derivative of $v(x,y) = \beta$ with respect to $x$:
$$\frac{\partial v}{\partial x} \frac{dx}{dx} + \frac{\partial v}{\partial y} \frac{dy}{dx} = 0$$
$$v_x + v_y \frac{dy}{dx} = 0$$
Let the slope of this curve be $m_2 = \frac{dy}{dx}$. Solving for $m_2$:
$$m_2 = -\frac{v_x}{v_y}$$

**Step 3: Multiply the slopes and apply the Cauchy-Riemann equations.**
Because $f(z) = u+iv$ is an analytic function, the Cauchy-Riemann equations hold at every point where the derivative is non-zero:
1.  $u_x = v_y$
2.  $u_y = -v_x$

We calculate the product of the slopes $m_1 \cdot m_2$:
$$m_1 \cdot m_2 = \left( -\frac{u_x}{u_y} \right) \cdot \left( -\frac{v_x}{v_y} \right)$$
$$m_1 \cdot m_2 = \frac{u_x \cdot v_x}{u_y \cdot v_y}$$

Now, substitute the Cauchy-Riemann equations into the numerator to replace the $u$ derivatives with $v$ derivatives:
*   Replace $u_x$ with $v_y$
*   Replace $u_y$ with $-v_x$

$$m_1 \cdot m_2 = \frac{(v_y) \cdot v_x}{(-v_x) \cdot v_y}$$
$$m_1 \cdot m_2 = -\frac{v_y v_x}{v_x v_y}$$

Assuming we are at a point where the derivative $f'(z) \neq 0$ (so the partials are not all zero):
$$m_1 \cdot m_2 = -1$$

**Conclusion:**
Because the product of their tangent slopes is exactly $-1$, the two families of curves intersect at right angles everywhere in the analytic region (except at critical points where $f'(z)=0$). Therefore, the families of curves are orthogonal. **(Proved)**

Here are the detailed solutions for the next four questions (Q193 to Q196).

### Q193. Problem 3.4.1: Find the orthogonal set of curves $x^{2}-y^{2}=a^{2}$.

*(Note: This is identical to Q175. The detailed steps are provided again below).*

**Solution:**

We are given a family of curves defined by setting a function $u(x,y) = x^2 - y^2$ equal to a constant $a^2$.
To find the orthogonal set of curves, we must find the harmonic conjugate $v(x,y)$ of $u(x,y)$. The curves defined by $v(x,y) = b^2$ (where $b^2$ is an arbitrary constant) will be orthogonal to the original curves.

**Step 1: Calculate the first partial derivatives of $u$.**
*   $u_x = \frac{\partial}{\partial x}(x^2 - y^2) = 2x$
*   $u_y = \frac{\partial}{\partial y}(x^2 - y^2) = -2y$

**Step 2: Use the Cauchy-Riemann equations to set up equations for $v$.**
The Cauchy-Riemann equations are $v_y = u_x$ and $v_x = -u_y$.
*   From $v_y = u_x$: $v_y = 2x$
*   From $v_x = -u_y$: $v_x = -(-2y) = 2y$

**Step 3: Integrate $v_y$ with respect to $y$.**
$$v(x,y) = \int 2x dy$$
$$v(x,y) = 2xy + g(x)$$
where $g(x)$ is an arbitrary function of $x$.

**Step 4: Differentiate with respect to $x$ and solve for $g(x)$.**
Take the partial derivative of our integrated $v(x,y)$ with respect to $x$:
$$v_x = \frac{\partial}{\partial x}(2xy + g(x)) = 2y + g'(x)$$

Equate this to the $v_x$ found in Step 2:
$$2y + g'(x) = 2y$$
$$g'(x) = 0$$

Integrate with respect to $x$:
$$g(x) = C$$ (where $C$ is a real constant).

**Step 5: Write the orthogonal family of curves.**
Substitute $g(x)$ back into $v(x,y)$:
$$v(x,y) = 2xy + C$$

The orthogonal set of curves is defined by setting $v(x,y)$ equal to an arbitrary constant $c_2$:
$$2xy + C = c_2$$
$$2xy = c_2 - C$$
Let $k = c_2 - C$ be a new arbitrary constant.
$$2xy = k$$

**Answer:** The orthogonal set of curves is **$2xy = k$** (where $k$ is any real constant).

***

### Q194. Problem 3.4.2: Find the orthogonal trajectories of the family of curves in the xy plane defined by $e^{-x}(x~\sin~y-y~\cos~y)=\alpha$ where $\alpha$ is a real constant.

*(Note: This is identical to Q176. The detailed steps are provided again below).*

**Solution:**

We are given a family of curves $u(x,y) = \alpha$, where $u(x,y) = e^{-x}(x\sin y - y\cos y)$. We must find the harmonic conjugate $v(x,y)$. The curves $v(x,y) = \beta$ will be the orthogonal trajectories.

**Step 1: Calculate the first partial derivatives of $u$.**
Use the product rule for $u_x$:
$$u_x = \frac{\partial}{\partial x}(e^{-x}) \cdot (x\sin y - y\cos y) + e^{-x} \cdot \frac{\partial}{\partial x}(x\sin y - y\cos y)$$
$$u_x = -e^{-x}(x\sin y - y\cos y) + e^{-x}(1 \cdot \sin y - 0)$$
$$u_x = e^{-x}(\sin y - x\sin y + y\cos y)$$

Use the product rule for $u_y$:
$$u_y = e^{-x} \cdot \frac{\partial}{\partial y}(x\sin y - y\cos y)$$
$$u_y = e^{-x} [x\cos y - (\cos y + y(-\sin y))]$$
$$u_y = e^{-x} (x\cos y - \cos y + y\sin y)$$

**Step 2: Use the Cauchy-Riemann equations to set up equations for $v$.**
*   From $v_y = u_x$: $v_y = e^{-x}(\sin y - x\sin y + y\cos y)$
*   From $v_x = -u_y$: $v_x = -e^{-x}(x\cos y - \cos y + y\sin y) = e^{-x}(\cos y - x\cos y - y\sin y)$

**Step 3: Integrate $v_y$ with respect to $y$ to find $v(x,y)$.**
$$v(x,y) = \int e^{-x}(\sin y - x\sin y + y\cos y) dy$$
Distribute the integral:
$$v(x,y) = e^{-x} \int \sin y dy - xe^{-x} \int \sin y dy + e^{-x} \int y\cos y dy$$
$$v(x,y) = e^{-x}(-\cos y) - xe^{-x}(-\cos y) + e^{-x}(\text{integration by parts})$$
For $\int y\cos y dy$, use integration by parts ($\int u dv = uv - \int v du$): let $u=y \implies du=dy$, and $dv=\cos y dy \implies v=\sin y$.
$$\int y\cos y dy = y\sin y - \int \sin y dy = y\sin y + \cos y$$
Substitute this back:
$$v(x,y) = -e^{-x}\cos y + xe^{-x}\cos y + e^{-x}(y\sin y + \cos y) + g(x)$$
$$v(x,y) = e^{-x}(-\cos y + x\cos y + y\sin y + \cos y) + g(x)$$
$$v(x,y) = e^{-x}(x\cos y + y\sin y) + g(x)$$

**Step 4: Differentiate and solve for $g(x)$.**
Differentiate $v(x,y)$ with respect to $x$:
$$v_x = \frac{\partial}{\partial x} [e^{-x}(x\cos y + y\sin y) + g(x)]$$
Using the product rule:
$$v_x = -e^{-x}(x\cos y + y\sin y) + e^{-x}(\cos y) + g'(x)$$
$$v_x = e^{-x}(\cos y - x\cos y - y\sin y) + g'(x)$$

Equate this to $v_x$ from Step 2:
$$e^{-x}(\cos y - x\cos y - y\sin y) + g'(x) = e^{-x}(\cos y - x\cos y - y\sin y)$$
$$g'(x) = 0 \implies g(x) = C$$

**Step 5: Write the final orthogonal set.**
Substitute $g(x)$ back into $v(x,y)$:
$$v(x,y) = e^{-x}(x\cos y + y\sin y) + C$$

Setting this to an arbitrary constant gives the orthogonal trajectories.
**Answer:** The orthogonal trajectories are given by **$e^{-x}(x\cos y + y\sin y) = \beta$** (where $\beta$ is an arbitrary constant).

***

### Q195. Problem 3.4.3: Prove that in polar form the Cauchy-Riemann equations can be written $\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial\theta},$ $\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial\theta}$

*(Note: This is identical to Q177. The detailed proof is provided again below).*

**Solution:**

We need to transform the Cauchy-Riemann (C-R) equations from Cartesian $(x,y)$ to polar $(r,\theta)$ coordinates.
The Cartesian C-R equations are: $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Coordinate transformation definitions.**
$x = r\cos\theta$
$y = r\sin\theta$
$r = \sqrt{x^2+y^2}$
$\theta = \tan^{-1}(y/x)$

**Step 2: Partial derivatives of the coordinates.**
*   $\frac{\partial r}{\partial x} = \frac{x}{\sqrt{x^2+y^2}} = \frac{x}{r} = \cos\theta$
*   $\frac{\partial r}{\partial y} = \frac{y}{\sqrt{x^2+y^2}} = \frac{y}{r} = \sin\theta$
*   $\frac{\partial \theta}{\partial x} = \frac{1}{1+(y/x)^2} \cdot \left(-\frac{y}{x^2}\right) = -\frac{y}{x^2+y^2} = -\frac{r\sin\theta}{r^2} = -\frac{\sin\theta}{r}$
*   $\frac{\partial \theta}{\partial y} = \frac{1}{1+(y/x)^2} \cdot \left(\frac{1}{x}\right) = \frac{x}{x^2+y^2} = \frac{r\cos\theta}{r^2} = \frac{\cos\theta}{r}$

**Step 3: Chain rule for partial derivatives of $u$ and $v$.**
*   $u_x = u_r\frac{\partial r}{\partial x} + u_\theta\frac{\partial \theta}{\partial x} = u_r \cos\theta - u_\theta \frac{\sin\theta}{r}$
*   $u_y = u_r\frac{\partial r}{\partial y} + u_\theta\frac{\partial \theta}{\partial y} = u_r \sin\theta + u_\theta \frac{\cos\theta}{r}$
*   $v_x = v_r\frac{\partial r}{\partial x} + v_\theta\frac{\partial \theta}{\partial x} = v_r \cos\theta - v_\theta \frac{\sin\theta}{r}$
*   $v_y = v_r\frac{\partial r}{\partial y} + v_\theta\frac{\partial \theta}{\partial y} = v_r \sin\theta + v_\theta \frac{\cos\theta}{r}$

**Step 4: Substitute into Cartesian C-R equations.**
From $u_x = v_y$:
$$u_r \cos\theta - u_\theta \frac{\sin\theta}{r} = v_r \sin\theta + v_\theta \frac{\cos\theta}{r} \quad \text{--- (Equation 1)}$$
From $u_y = -v_x$:
$$u_r \sin\theta + u_\theta \frac{\cos\theta}{r} = -v_r \cos\theta + v_\theta \frac{\sin\theta}{r} \quad \text{--- (Equation 2)}$$

**Step 5: Solve for $u_r$ and $v_r$.**
To find $u_r$, multiply Eq 1 by $\cos\theta$, Eq 2 by $\sin\theta$, and add them:
$(u_r \cos^2\theta - u_\theta \frac{\sin\theta\cos\theta}{r}) + (u_r \sin^2\theta + u_\theta \frac{\sin\theta\cos\theta}{r}) = (v_r \sin\theta\cos\theta + v_\theta \frac{\cos^2\theta}{r}) + (-v_r \sin\theta\cos\theta + v_\theta \frac{\sin^2\theta}{r})$
$$u_r(\cos^2\theta + \sin^2\theta) = \frac{v_\theta}{r}(\cos^2\theta + \sin^2\theta)$$
**$u_r = \frac{1}{r} v_\theta$** (Proved first equation)

To find $v_r$, multiply Eq 1 by $-\sin\theta$, Eq 2 by $\cos\theta$, and add them:
$(-u_r \sin\theta\cos\theta + u_\theta \frac{\sin^2\theta}{r}) + (u_r \sin\theta\cos\theta + u_\theta \frac{\cos^2\theta}{r}) = (-v_r \sin^2\theta - v_\theta \frac{\sin\theta\cos\theta}{r}) + (-v_r \cos^2\theta + v_\theta \frac{\sin\theta\cos\theta}{r})$
$$\frac{u_\theta}{r}(\sin^2\theta + \cos^2\theta) = -v_r(\sin^2\theta + \cos^2\theta)$$
**$v_r = -\frac{1}{r} u_\theta$** (Proved second equation)

***

### Q196. Problem 3.4.4: Prove that the real and imaginary parts of an analytic function of a complex variable when expressed in polar form satisfy the equation [Laplace's equation in polar form] That is, $\frac{\partial^{2}u}{\partial r^{2}}+\frac{1}{r}\frac{\partial u}{\partial r}+\frac{1}{r^{2}}\frac{\partial^{2}u}{\partial\theta^{2}}=0$ and $\frac{\partial^{2}v}{\partial r^{2}}+\frac{1}{r}\frac{\partial v}{\partial r}+\frac{1}{r^{2}}\frac{\partial^{2}v}{\partial\theta^{2}}=0$

*(Note: This is identical to Q178. The detailed proof is provided again below).*

**Solution:**

We start with the Polar Cauchy-Riemann equations proved in Q195:
1.  $u_r = \frac{1}{r} v_\theta$
2.  $v_r = -\frac{1}{r} u_\theta \implies u_\theta = -r v_r$

**Step 1: Derive Laplace's equation for $u$.**
Differentiate C-R equation 1 with respect to $r$:
$$u_{rr} = \frac{\partial}{\partial r}\left(\frac{1}{r} v_\theta\right) = -\frac{1}{r^2} v_\theta + \frac{1}{r} v_{\theta r} \quad \text{--- (Equation 3)}$$

Differentiate C-R equation 2 with respect to $\theta$:
$$u_{\theta\theta} = \frac{\partial}{\partial \theta}(-r v_r) = -r v_{r\theta} \implies v_{r\theta} = -\frac{1}{r} u_{\theta\theta}$$

By Clairaut's Theorem, $v_{\theta r} = v_{r\theta}$. Substitute this into Equation 3:
$$u_{rr} = -\frac{1}{r^2} v_\theta + \frac{1}{r} \left(-\frac{1}{r} u_{\theta\theta}\right)$$
$$u_{rr} = -\frac{1}{r^2} v_\theta - \frac{1}{r^2} u_{\theta\theta}$$

Substitute $v_\theta = r u_r$ (from C-R eq 1) back into the expression:
$$u_{rr} = -\frac{1}{r^2} (r u_r) - \frac{1}{r^2} u_{\theta\theta}$$
$$u_{rr} = -\frac{1}{r} u_r - \frac{1}{r^2} u_{\theta\theta}$$

Rearrange terms:
**$u_{rr} + \frac{1}{r} u_r + \frac{1}{r^2} u_{\theta\theta} = 0$** (Proved for $u$)

**Step 2: Derive Laplace's equation for $v$.**
Differentiate C-R equation 2 with respect to $r$:
$$v_{rr} = \frac{\partial}{\partial r}\left(-\frac{1}{r} u_\theta\right) = \frac{1}{r^2} u_\theta - \frac{1}{r} u_{\theta r} \quad \text{--- (Equation 4)}$$

Differentiate C-R equation 1 (rewritten as $v_\theta = r u_r$) with respect to $\theta$:
$$v_{\theta\theta} = \frac{\partial}{\partial \theta}(r u_r) = r u_{r\theta} \implies u_{r\theta} = \frac{1}{r} v_{\theta\theta}$$

By Clairaut's Theorem, $u_{\theta r} = u_{r\theta}$. Substitute this into Equation 4:
$$v_{rr} = \frac{1}{r^2} u_\theta - \frac{1}{r} \left(\frac{1}{r} v_{\theta\theta}\right)$$
$$v_{rr} = \frac{1}{r^2} u_\theta - \frac{1}{r^2} v_{\theta\theta}$$

Substitute $u_\theta = -r v_r$ (from C-R eq 2) back into the expression:
$$v_{rr} = \frac{1}{r^2} (-r v_r) - \frac{1}{r^2} v_{\theta\theta}$$
$$v_{rr} = -\frac{1}{r} v_r - \frac{1}{r^2} v_{\theta\theta}$$

Rearrange terms:
**$v_{rr} + \frac{1}{r} v_r + \frac{1}{r^2} v_{\theta\theta} = 0$** (Proved for $v$)
Here are the detailed solutions for the next four questions (Q197 to Q200). 

*(Note: Questions Q197, Q198, and Q199 from the Feruj Sheet are conceptually and numerically identical to questions solved earlier. Detailed step-by-step solutions are provided again below for completeness).*

### Q197. Problem 3.4.5: An analytic function with constant modulus is constant.

*(This is identical to Q179).*

**Solution:**

Let $f(z) = u(x,y) + iv(x,y)$ be an analytic function defined in a region $R$. We are given that its modulus $|f(z)|$ is a constant value $c$. We must prove that $f(z)$ itself is a constant function.

**Step 1: Express the constant modulus algebraically.**
By definition, the modulus is $|f(z)| = \sqrt{u^2 + v^2}$.
Since it is constant, $|f(z)|^2 = c^2$.
$$u^2 + v^2 = c^2$$
*(If $c=0$, then $u=0$ and $v=0$ everywhere, so $f(z)=0$, which is constant. We assume $c \neq 0$ for the rest of the proof).*

**Step 2: Differentiate the modulus equation.**
Take the partial derivative of $u^2 + v^2 = c^2$ with respect to $x$:
$$2u \frac{\partial u}{\partial x} + 2v \frac{\partial v}{\partial x} = 0 \implies u u_x + v v_x = 0 \quad \text{--- (Equation 1)}$$

Take the partial derivative with respect to $y$:
$$2u \frac{\partial u}{\partial y} + 2v \frac{\partial v}{\partial y} = 0 \implies u u_y + v v_y = 0 \quad \text{--- (Equation 2)}$$

**Step 3: Apply the Cauchy-Riemann equations.**
Because $f(z)$ is analytic, the C-R equations hold: $u_x = v_y$ and $u_y = -v_x$.
Substitute these into Equation 2 to express it entirely in terms of $x$-derivatives:
$$u (-v_x) + v (u_x) = 0$$
$$v u_x - u v_x = 0 \quad \text{--- (Equation 3)}$$

**Step 4: Solve the system of linear equations.**
We have a system of two equations for the variables $u_x$ and $v_x$:
1) $u u_x + v v_x = 0$
2) $v u_x - u v_x = 0$

To solve for $u_x$, multiply Eq 1 by $u$ and Eq 3 by $v$:
*   $u^2 u_x + uv v_x = 0$
*   $v^2 u_x - uv v_x = 0$
Add them together:
$$u_x(u^2 + v^2) = 0$$
Since $u^2 + v^2 = c^2 \neq 0$, it must be that **$u_x = 0$**.

Substitute $u_x = 0$ back into Equation 1:
$$u(0) + v v_x = 0 \implies v v_x = 0$$
Since this must hold everywhere (and $u,v$ cannot both be 0 if $c \neq 0$), it implies **$v_x = 0$**.

**Step 5: Conclude.**
The derivative of $f(z)$ can be written as $f'(z) = u_x + i v_x$.
Since we found $u_x = 0$ and $v_x = 0$ everywhere in the region,
$$f'(z) = 0 + i0 = 0$$
A function whose derivative is zero everywhere in a connected region is a constant function. **(Proved)**

***

### Q198. Problem 3.4.6: Show that the function $u=\frac{1}{2}\log(x^{2}+y^{2})$ is harmonic and determine its conjugate. Also find $f(z)$

*(This is identical to Q138, Q144, and Q180).*

**Solution:**

**Part 1: Show $u$ is harmonic.**
Verify Laplace's equation: $u_{xx} + u_{yy} = 0$.
*   **First derivatives:**
    $$u_x = \frac{\partial}{\partial x} \left[ \frac{1}{2}\ln(x^2+y^2) \right] = \frac{1}{2} \frac{2x}{x^2+y^2} = \frac{x}{x^2+y^2}$$
    $$u_y = \frac{\partial}{\partial y} \left[ \frac{1}{2}\ln(x^2+y^2) \right] = \frac{1}{2} \frac{2y}{x^2+y^2} = \frac{y}{x^2+y^2}$$
*   **Second derivatives (quotient rule):**
    $$u_{xx} = \frac{(1)(x^2+y^2) - (x)(2x)}{(x^2+y^2)^2} = \frac{y^2-x^2}{(x^2+y^2)^2}$$
    $$u_{yy} = \frac{(1)(x^2+y^2) - (y)(2y)}{(x^2+y^2)^2} = \frac{x^2-y^2}{(x^2+y^2)^2}$$
*   **Sum them:**
    $$u_{xx} + u_{yy} = \frac{y^2-x^2+x^2-y^2}{(x^2+y^2)^2} = 0$$
Since Laplace's equation holds, $u$ is **harmonic**.

**Part 2: Find the harmonic conjugate $v(x,y)$.**
Use C-R equations: $v_y = u_x$ and $v_x = -u_y$.
1.  **Integrate $v_y$:**
    $$v_y = \frac{x}{x^2+y^2} \implies v(x,y) = \int \frac{x}{x^2+y^2} dy = \tan^{-1}\left(\frac{y}{x}\right) + g(x)$$
2.  **Differentiate and use the second C-R equation:**
    $$v_x = \frac{\partial}{\partial x}\left( \tan^{-1}\left(\frac{y}{x}\right) + g(x) \right) = \frac{1}{1+(y/x)^2}\left(-\frac{y}{x^2}\right) + g'(x) = -\frac{y}{x^2+y^2} + g'(x)$$
    Equate to $-u_y = -\frac{y}{x^2+y^2}$:
    $$-\frac{y}{x^2+y^2} + g'(x) = -\frac{y}{x^2+y^2} \implies g'(x) = 0 \implies g(x) = C$$
3.  **Final conjugate:** **$v(x,y) = \tan^{-1}\left(\frac{y}{x}\right) + C$**

**Part 3: Find $f(z)$.**
Using the Milne-Thomson method (substitute $x=z, y=0$ into $u+iv$):
$$f(z) = u(z,0) + iv(z,0) = \frac{1}{2}\ln(z^2) + i(\tan^{-1}(0) + C)$$
$$f(z) = \ln(z) + iC$$

***

### Q199. Problems 3.4.7: If In a two dimensional flow, the stream function is $\psi=\tan^{-1}(\frac{y}{x})$ Find the velocity potential $\varphi$.

*(This is identical to Q136 and Q181).*

**Solution:**

The velocity potential $\phi(x,y)$ and stream function $\psi(x,y)$ form the real and imaginary parts of an analytic complex potential function $F(z) = \phi + i\psi$. Therefore, they must satisfy the Cauchy-Riemann equations: $\phi_x = \psi_y$ and $\phi_y = -\psi_x$.

**Step 1: Find partial derivatives of $\psi$.**
$$\psi = \tan^{-1}\left(\frac{y}{x}\right)$$
*   $\psi_x = \frac{1}{1+(y/x)^2} \cdot \left(-\frac{y}{x^2}\right) = \frac{x^2}{x^2+y^2} \cdot \left(-\frac{y}{x^2}\right) = -\frac{y}{x^2+y^2}$
*   $\psi_y = \frac{1}{1+(y/x)^2} \cdot \left(\frac{1}{x}\right) = \frac{x^2}{x^2+y^2} \cdot \left(\frac{1}{x}\right) = \frac{x}{x^2+y^2}$

**Step 2: Set up C-R equations for $\phi$.**
*   $\phi_x = \psi_y = \frac{x}{x^2+y^2}$
*   $\phi_y = -\psi_x = \frac{y}{x^2+y^2}$

**Step 3: Integrate $\phi_x$ with respect to $x$.**
$$\phi(x,y) = \int \frac{x}{x^2+y^2} dx$$
Let $w = x^2+y^2 \implies dw = 2xdx$.
$$\phi(x,y) = \frac{1}{2} \ln(x^2+y^2) + h(y)$$

**Step 4: Differentiate with respect to $y$ and solve for $h(y)$.**
$$\phi_y = \frac{\partial}{\partial y}\left( \frac{1}{2} \ln(x^2+y^2) + h(y) \right) = \frac{y}{x^2+y^2} + h'(y)$$
Equate this to $\phi_y$ from Step 2:
$$\frac{y}{x^2+y^2} + h'(y) = \frac{y}{x^2+y^2}$$
$$h'(y) = 0 \implies h(y) = C$$

**Answer:** The velocity potential is **$\varphi(x,y) = \frac{1}{2}\ln(x^2+y^2) + C$**.

***

### Q200. Problems 3.1 Question 1: Test the analyticity of the following functions: (i) $f(z)=\overline{z}$ (ii) $f(z)=ize^{-z}$ (iii) $f(z)=ze^{-z}$ (iv) $f(z)=\vert{}z\vert{}^{4}$ (v) $f(z)=\frac{1+z}{1-z}$

**Solution:**

We test analyticity by checking if the functions are differentiable in a neighborhood (which requires satisfying the Cauchy-Riemann equations $u_x=v_y, u_y=-v_x$ everywhere in that region).

---
**(i) $f(z) = \overline{z}$** *(Previously solved in Q182)*
$f(z) = x - iy \implies u = x, v = -y$.
Partials: $u_x = 1, u_y = 0, v_x = 0, v_y = -1$.
Check C-R: $u_x = v_y \implies 1 = -1$ (False).
**Conclusion:** The function is **not analytic anywhere**.

---
**(ii) $f(z) = ize^{-z}$** *(Previously solved in Q184)*
$f(z) = i(x+iy)e^{-x}(\cos y - i\sin y) = e^{-x}(-y\cos y + x\sin y) + i e^{-x}(x\cos y + y\sin y)$.
*   $u = e^{-x}(-y\cos y + x\sin y)$
*   $v = e^{-x}(x\cos y + y\sin y)$
Calculating partials confirms $u_x = v_y$ and $u_y = -v_x$ for all $x,y \in \mathbb{R}$.
**Conclusion:** The function is **analytic everywhere** (entire).

---
**(iii) $f(z) = ze^{-z}$** *(Previously solved in Q184)*
$f(z) = (x+iy)e^{-x}(\cos y - i\sin y) = e^{-x}(x\cos y + y\sin y) + i e^{-x}(y\cos y - x\sin y)$.
*   $u = e^{-x}(x\cos y + y\sin y)$
*   $v = e^{-x}(y\cos y - x\sin y)$
Calculating partials confirms $u_x = v_y$ and $u_y = -v_x$ for all $x,y \in \mathbb{R}$.
**Conclusion:** The function is **analytic everywhere** (entire).

---
**(iv) $f(z) = |z|^4$**
We know $|z| = \sqrt{x^2+y^2}$, so $|z|^4 = (x^2+y^2)^2 = x^4 + 2x^2y^2 + y^4$.
Because this is a purely real function:
*   $u(x,y) = x^4 + 2x^2y^2 + y^4$
*   $v(x,y) = 0$

Calculate partials:
$u_x = 4x^3 + 4xy^2 = 4x(x^2+y^2)$
$u_y = 4x^2y + 4y^3 = 4y(x^2+y^2)$
$v_x = 0$
$v_y = 0$

Check C-R equations:
1. $u_x = v_y \implies 4x(x^2+y^2) = 0$
2. $u_y = -v_x \implies 4y(x^2+y^2) = 0$

These equations are only true simultaneously if $x=0$ and $y=0$. The function is differentiable at exactly one point ($z=0$), meaning it lacks a neighborhood of differentiability.
**Conclusion:** The function is **not analytic anywhere**.

---
**(v) $f(z) = \frac{1+z}{1-z}$**
This is a rational function composed of two polynomials, $P(z) = 1+z$ and $Q(z) = 1-z$. 
In complex analysis, any polynomial is an entire (analytic everywhere) function. Furthermore, the quotient of two analytic functions is analytic everywhere *except* where the denominator is zero (which creates a singularity/pole).

Set the denominator to zero to find the singularity:
$1 - z = 0 \implies z = 1$.

At $z=1$, the function is undefined and its derivative does not exist. Everywhere else in the complex plane, the derivative exists (and can be found easily using the complex quotient rule: $f'(z) = \frac{1(1-z) - (-1)(1+z)}{(1-z)^2} = \frac{2}{(1-z)^2}$).

**Conclusion:** The function is **analytic everywhere except at $z=1$** (analytic in $\mathbb{C} \setminus \{1\}$).

Here are the detailed solutions for the next four questions (Q201 to Q204).

### Q201. Problems 3.1 Question 2: Show that (a) $u=2x(1-y)$ is harmonic. (b) Find v such that $f(z)=u+iv$ is analytic. (c) Find also, $f(z)$ in terms of z.

*(Note: This is numerically identical to Q135, Q171, and Q188. A concise step-by-step solution is provided below).*

**Solution:**

Given $u(x,y) = 2x(1-y) = 2x - 2xy$.

**Part (a): Show $u$ is harmonic.**
To be harmonic, $u$ must satisfy Laplace's equation: $u_{xx} + u_{yy} = 0$.
1.  **First derivatives:**
    $$u_x = \frac{\partial}{\partial x}(2x - 2xy) = 2 - 2y$$
    $$u_y = \frac{\partial}{\partial y}(2x - 2xy) = -2x$$
2.  **Second derivatives:**
    $$u_{xx} = \frac{\partial}{\partial x}(2 - 2y) = 0$$
    $$u_{yy} = \frac{\partial}{\partial y}(-2x) = 0$$
3.  **Check Laplace's equation:**
    $$u_{xx} + u_{yy} = 0 + 0 = 0$$
Since Laplace's equation holds everywhere, **$u$ is a harmonic function.** (Proved)

---

**Part (b): Find the harmonic conjugate $v(x,y)$.**
We use the Cauchy-Riemann equations: $v_y = u_x$ and $v_x = -u_y$.
1.  **Set up using $v_y = u_x$:**
    $$v_y = 2 - 2y$$
2.  **Integrate with respect to $y$:**
    $$v(x,y) = \int (2 - 2y) dy = 2y - y^2 + g(x)$$
3.  **Differentiate with respect to $x$:**
    $$v_x = \frac{\partial}{\partial x}(2y - y^2 + g(x)) = g'(x)$$
4.  **Use the second C-R equation ($v_x = -u_y$):**
    We know $-u_y = -(-2x) = 2x$.
    Equating the two expressions for $v_x$:
    $$g'(x) = 2x$$
5.  **Integrate with respect to $x$:**
    $$g(x) = \int 2x dx = x^2 + C$$
6.  **Final conjugate:**
    **$v(x,y) = 2y - y^2 + x^2 + C$**

---

**Part (c): Find $f(z)$ in terms of $z$.**
Use the Milne-Thomson method (substitute $x=z$ and $y=0$ directly into $u$ and $v$):
*   $u(z,0) = 2z - 2z(0) = 2z$
*   $v(z,0) = 2(0) - 0^2 + z^2 + C = z^2 + C$

Construct the function $f(z) = u(z,0) + iv(z,0)$:
$$f(z) = 2z + i(z^2 + C)$$
**Answer: $f(z) = iz^2 + 2z + iC$**

***

### Q202. Problems 3.1 Question 3: Show that (a) $u=3x^{2}y+2x^{2}-y^{3}-2y^{2}$ is harmonic. (b) Find v such that $f(z)=u+iv$ is analytic. (c) Find also, $f(z)$ in terms of z.

**Solution:**

Given $u(x,y) = 3x^2y + 2x^2 - y^3 - 2y^2$.

**Part (a): Show $u$ is harmonic.**
Verify Laplace's equation: $u_{xx} + u_{yy} = 0$.
1.  **First derivatives:**
    $$u_x = 6xy + 4x$$
    $$u_y = 3x^2 - 3y^2 - 4y$$
2.  **Second derivatives:**
    $$u_{xx} = \frac{\partial}{\partial x}(6xy + 4x) = 6y + 4$$
    $$u_{yy} = \frac{\partial}{\partial y}(3x^2 - 3y^2 - 4y) = -6y - 4$$
3.  **Check Laplace's equation:**
    $$u_{xx} + u_{yy} = (6y + 4) + (-6y - 4) = 0$$
Since it equals zero, **$u$ is a harmonic function.** (Proved)

---

**Part (b): Find the harmonic conjugate $v(x,y)$.**
Use C-R equations $v_y = u_x$ and $v_x = -u_y$.
1.  **Integrate $v_y$:**
    $$v_y = u_x = 6xy + 4x$$
    $$v(x,y) = \int (6xy + 4x) dy = 3xy^2 + 4xy + g(x)$$
2.  **Differentiate with respect to $x$:**
    $$v_x = \frac{\partial}{\partial x}(3xy^2 + 4xy + g(x)) = 3y^2 + 4y + g'(x)$$
3.  **Use the second C-R equation:**
    We know $-u_y = -(3x^2 - 3y^2 - 4y) = -3x^2 + 3y^2 + 4y$.
    Equate this to $v_x$:
    $$3y^2 + 4y + g'(x) = -3x^2 + 3y^2 + 4y$$
    Cancel identical terms:
    $$g'(x) = -3x^2$$
4.  **Integrate to find $g(x)$:**
    $$g(x) = \int -3x^2 dx = -x^3 + C$$
5.  **Final conjugate:**
    **$v(x,y) = 3xy^2 + 4xy - x^3 + C$**

---

**Part (c): Find $f(z)$ in terms of $z$.**
Use the Milne-Thomson method. Substitute $x=z, y=0$:
*   $u(z,0) = 3z^2(0) + 2z^2 - 0^3 - 2(0)^2 = 2z^2$
*   $v(z,0) = 3z(0)^2 + 4z(0) - z^3 + C = -z^3 + C$

Construct the analytic function $f(z) = u(z,0) + iv(z,0)$:
$$f(z) = 2z^2 + i(-z^3 + C)$$
$$f(z) = -iz^3 + 2z^2 + iC$$
**Answer: $f(z) = -iz^3 + 2z^2 + C_1$** (where $C_1 = iC$ is a complex constant).

***

### Q203. Problems 3.1 Question 4: Show that (a) $u=e^{-2xy}\sin(x^{2}-y^{2})$ is harmonic. (b) Find v such that $f(z)=u+iv$ is analytic. (c) Find also, $f(z)$ in terms of z.

**Solution:**

Given $u(x,y) = e^{-2xy}\sin(x^2 - y^2)$. Let $B = (x^2 - y^2)$. 
*(Note: Because integrating partial derivatives for this function is algebraically massive, it is highly recommended to use the Milne-Thomson rule to find $f'(z)$ and integrate it to find $f(z)$ first, then extract $v$ from $f(z)$).*

**Part (a): Show $u$ is harmonic.**
1.  **Find $u_x$ using the product and chain rules:**
    $$u_x = \frac{\partial}{\partial x}(e^{-2xy}) \cdot \sin B + e^{-2xy} \cdot \frac{\partial}{\partial x}(\sin B)$$
    $$u_x = -2ye^{-2xy}\sin B + e^{-2xy}\cos B \cdot (2x)$$
    $$u_x = 2e^{-2xy} [ x\cos(x^2-y^2) - y\sin(x^2-y^2) ]$$
2.  **Find $u_{xx}$:**
    $$u_{xx} = 2 \left[ \frac{\partial}{\partial x}(e^{-2xy}) [ x\cos B - y\sin B ] + e^{-2xy} \frac{\partial}{\partial x}[ x\cos B - y\sin B ] \right]$$
    $$u_{xx} = 2 \left[ -2y e^{-2xy} (x\cos B - y\sin B) + e^{-2xy} (\cos B - x\sin B(2x) - y\cos B(2x)) \right]$$
    Factor out $e^{-2xy}$:
    $$u_{xx} = 2e^{-2xy} [ -2xy\cos B + 2y^2\sin B + \cos B - 2x^2\sin B - 2xy\cos B ]$$
    $$u_{xx} = 2e^{-2xy} [ \cos B - 4xy\cos B + (2y^2 - 2x^2)\sin B ]$$
3.  **Find $u_y$:**
    $$u_y = \frac{\partial}{\partial y}(e^{-2xy}) \cdot \sin B + e^{-2xy} \cdot \frac{\partial}{\partial y}(\sin B)$$
    $$u_y = -2xe^{-2xy}\sin B + e^{-2xy}\cos B \cdot (-2y)$$
    $$u_y = -2e^{-2xy} [ x\sin(x^2-y^2) + y\cos(x^2-y^2) ]$$
4.  **Find $u_{yy}$:**
    $$u_{yy} = -2 \left[ \frac{\partial}{\partial y}(e^{-2xy}) [ x\sin B + y\cos B ] + e^{-2xy} \frac{\partial}{\partial y}[ x\sin B + y\cos B ] \right]$$
    $$u_{yy} = -2 \left[ -2x e^{-2xy} (x\sin B + y\cos B) + e^{-2xy} (x\cos B(-2y) + \cos B + y(-\sin B)(-2y)) \right]$$
    Factor out $e^{-2xy}$:
    $$u_{yy} = -2e^{-2xy} [ -2x^2\sin B - 2xy\cos B - 2xy\cos B + \cos B + 2y^2\sin B ]$$
    $$u_{yy} = -2e^{-2xy} [ \cos B - 4xy\cos B + (2y^2 - 2x^2)\sin B ]$$
5.  **Check Laplace's equation:**
    Comparing $u_{xx}$ and $u_{yy}$, we clearly see that $u_{yy} = -u_{xx}$.
    Therefore, $u_{xx} + u_{yy} = 0$. **$u$ is a harmonic function.**

---

**Part (c): Find $f(z)$ in terms of $z$ (Done before Part b for efficiency).**
Use the Milne-Thomson rule for the derivative: $f'(z) = u_x(z,0) - i u_y(z,0)$.
1.  **Evaluate $u_x(z,0)$:**
    Substitute $x=z, y=0$ into the $u_x$ we found in Part a:
    $$u_x(z,0) = 2e^0 [ z\cos(z^2) - 0 ] = 2z\cos(z^2)$$
2.  **Evaluate $u_y(z,0)$:**
    Substitute $x=z, y=0$ into $u_y$:
    $$u_y(z,0) = -2e^0 [ z\sin(z^2) + 0 ] = -2z\sin(z^2)$$
3.  **Construct $f'(z)$:**
    $$f'(z) = 2z\cos(z^2) - i(-2z\sin(z^2)) = 2z(\cos(z^2) + i\sin(z^2))$$
    Using Euler's formula:
    $$f'(z) = 2z e^{iz^2}$$
4.  **Integrate to find $f(z)$:**
    $$f(z) = \int 2z e^{iz^2} dz$$
    Use u-substitution: Let $w = iz^2 \implies dw = 2iz dz \implies \frac{dw}{i} = 2z dz \implies -i dw = 2z dz$.
    $$f(z) = \int -i e^w dw = -i e^w + C = -i e^{iz^2} + C$$
**Answer (c): $f(z) = -i e^{iz^2} + C$**

---

**Part (b): Find $v$ such that $f(z)=u+iv$ is analytic.**
Now that we have $f(z)$, we can simply expand it into its real and imaginary parts to extract $v(x,y)$.
$$f(z) = -i e^{i(x+iy)^2} + C$$
$$f(z) = -i e^{i(x^2 - y^2 + 2ixy)} + C$$
$$f(z) = -i e^{i(x^2 - y^2) - 2xy} + C$$
$$f(z) = -i e^{-2xy} [\cos(x^2 - y^2) + i\sin(x^2 - y^2)] + C$$
$$f(z) = -i e^{-2xy} \cos(x^2 - y^2) - i^2 e^{-2xy}\sin(x^2 - y^2) + C$$
Since $i^2 = -1$:
$$f(z) = e^{-2xy}\sin(x^2 - y^2) - i e^{-2xy}\cos(x^2 - y^2) + C$$
Notice the real part perfectly matches the $u(x,y)$ given in the problem. The imaginary part is $v(x,y)$.
Let $C = C_{Re} + iC_{Im}$.
**Answer (b): $v(x,y) = -e^{-2xy}\cos(x^2 - y^2) + C_{Im}$**

***

### Q204. Problems 3.1 Question 5: Give an example such that u and v are harmonic but $u+iv$ is not analytic.

**Solution:**

An analytic function $f(z) = u + iv$ requires its real and imaginary parts to meet two conditions:
1.  They must be harmonic functions ($\nabla^2 u = 0$ and $\nabla^2 v = 0$).
2.  They must be strictly coupled together by the Cauchy-Riemann equations ($u_x = v_y$ and $u_y = -v_x$).

To provide an example where $u$ and $v$ are harmonic but $u+iv$ is *not* analytic, we simply need to choose two arbitrary harmonic functions that **fail to satisfy the Cauchy-Riemann equations.**

**Example Formulation:**
Let's pick the simplest possible non-trivial harmonic functions: $x$ and $y$.
*   Let **$u(x,y) = x$**
*   Let **$v(x,y) = -y$**

**Step 1: Verify that $u$ and $v$ are harmonic.**
*   For $u$: $u_x = 1 \implies u_{xx} = 0$. $u_y = 0 \implies u_{yy} = 0$. 
    $u_{xx} + u_{yy} = 0 + 0 = 0$. (Harmonic)
*   For $v$: $v_x = 0 \implies v_{xx} = 0$. $v_y = -1 \implies v_{yy} = 0$. 
    $v_{xx} + v_{yy} = 0 + 0 = 0$. (Harmonic)

**Step 2: Check the Cauchy-Riemann equations.**
The C-R equations require $u_x = v_y$.
*   $u_x = 1$
*   $v_y = -1$
Clearly, $1 \neq -1$. The C-R equations fail.

**Conclusion:**
Because the Cauchy-Riemann equations are not satisfied, the complex function formed by their sum, $f(z) = u + iv = x - iy$ (which is exactly the complex conjugate $f(z) = \overline{z}$ evaluated in Q182), is not analytic.

**Answer:** 
An example is **$u(x,y) = x$** and **$v(x,y) = -y$**. Both functions are harmonic (their Laplacians are zero), but the resulting complex function $f(z) = x - iy$ is not analytic because it fails the Cauchy-Riemann equations ($u_x \neq v_y$).

Here are the detailed solutions for the next four questions (Q205 to Q208).

### Q205. Problems 3.1 Question 6: If $w=f(z)=u+iv$ is an analytic function and $v(x,y)=\frac{x-y}{x^{2}+y^{2}}$ , find u.

**Solution:**

We are given the imaginary part $v(x,y) = \frac{x-y}{x^2+y^2}$ of an analytic function. We need to find the real part $u(x,y)$ (the harmonic conjugate) using the Cauchy-Riemann equations: $u_x = v_y$ and $u_y = -v_x$.

**Step 1: Calculate the partial derivatives of $v$.**
We use the quotient rule $\left(\frac{A}{B}\right)' = \frac{A'B - AB'}{B^2}$.

*   **Calculate $v_x$:**
    $$v_x = \frac{\partial}{\partial x} \left( \frac{x-y}{x^2+y^2} \right) = \frac{(1)(x^2+y^2) - (x-y)(2x)}{(x^2+y^2)^2}$$
    $$v_x = \frac{x^2 + y^2 - 2x^2 + 2xy}{(x^2+y^2)^2} = \frac{y^2 - x^2 + 2xy}{(x^2+y^2)^2}$$

*   **Calculate $v_y$:**
    $$v_y = \frac{\partial}{\partial y} \left( \frac{x-y}{x^2+y^2} \right) = \frac{(-1)(x^2+y^2) - (x-y)(2y)}{(x^2+y^2)^2}$$
    $$v_y = \frac{-x^2 - y^2 - 2xy + 2y^2}{(x^2+y^2)^2} = \frac{y^2 - x^2 - 2xy}{(x^2+y^2)^2}$$

**Step 2: Set up the Cauchy-Riemann equations for $u$.**
*   From $u_x = v_y$:
    $$u_x = \frac{y^2 - x^2 - 2xy}{(x^2+y^2)^2}$$
*   From $u_y = -v_x$:
    $$u_y = -\frac{y^2 - x^2 + 2xy}{(x^2+y^2)^2} = \frac{x^2 - y^2 - 2xy}{(x^2+y^2)^2}$$

*(Note: Integrating these rational functions directly is algebraically tedious. A much faster and elegant method is to use the Milne-Thomson rule to find $f'(z)$, integrate to find $f(z)$, and then extract the real part $u$).*

**Step 3: Apply the Milne-Thomson rule to find $f'(z)$.**
The rule states $f'(z) = v_y(z,0) + i v_x(z,0)$.
Substitute $x=z$ and $y=0$ into the partial derivatives found in Step 1:
*   $v_y(z,0) = \frac{0^2 - z^2 - 2z(0)}{(z^2+0^2)^2} = \frac{-z^2}{z^4} = -\frac{1}{z^2}$
*   $v_x(z,0) = \frac{0^2 - z^2 + 2z(0)}{(z^2+0^2)^2} = \frac{-z^2}{z^4} = -\frac{1}{z^2}$

Construct the derivative:
$$f'(z) = \left(-\frac{1}{z^2}\right) + i\left(-\frac{1}{z^2}\right) = -\frac{1 + i}{z^2}$$

**Step 4: Integrate $f'(z)$ to find $f(z)$.**
$$f(z) = \int -\frac{1 + i}{z^2} dz = -(1+i) \int z^{-2} dz = -(1+i) \left( \frac{z^{-1}}{-1} \right) + C$$
$$f(z) = \frac{1+i}{z} + C$$

**Step 5: Extract the real part $u(x,y)$ from $f(z)$.**
Substitute $z = x+iy$:
$$f(z) = \frac{1+i}{x+iy} + C$$
Rationalize the denominator by multiplying top and bottom by the conjugate $(x-iy)$:
$$f(z) = \frac{(1+i)(x-iy)}{(x+iy)(x-iy)} + C$$
$$f(z) = \frac{x - iy + ix - i^2y}{x^2+y^2} + C$$
Since $i^2 = -1$:
$$f(z) = \frac{x - iy + ix + y}{x^2+y^2} + C$$
Group the real and imaginary terms:
$$f(z) = \left( \frac{x+y}{x^2+y^2} \right) + i\left( \frac{x-y}{x^2+y^2} \right) + C$$

Notice that the imaginary part $\frac{x-y}{x^2+y^2}$ matches the $v(x,y)$ given in the problem perfectly.
Therefore, the real part $u(x,y)$ is the other term in the bracket. Let $C = c_1 + ic_2$.

**Answer:** The real part is **$u(x,y) = \frac{x+y}{x^2+y^2} + c_1$** (where $c_1$ is a real constant).

***

### Q206. Pg 2, Q4(a): Prove that the bilinear transformation can be considered as a combination of translation, rotation, stretching and inversion.

*(Note: This is conceptually identical to Q209. We will provide the formal proof).*

**Solution:**

A standard **bilinear transformation** (also known as a Möbius transformation) maps the complex $z$-plane to the $w$-plane and is defined by the equation:
$$w = \frac{az + b}{cz + d} \quad \text{where } ad - bc \neq 0$$

To prove this transformation is a composition of fundamental geometric operations, we must algebraically decompose this single fraction into a sequence of simpler, sequential transformations.

**Case 1: If $c = 0$**
If $c = 0$, the condition $ad - bc \neq 0$ implies $ad \neq 0$, so $a \neq 0$ and $d \neq 0$.
The transformation becomes:
$$w = \frac{a}{d}z + \frac{b}{d}$$
Let $A = a/d$ (a complex constant) and $B = b/d$ (a complex constant).
$$w = Az + B$$
This represents a standard linear transformation. 
Let $A = r e^{i\theta}$.
1.  **$z_1 = e^{i\theta} z$** : This is a pure **rotation** by angle $\theta$.
2.  **$z_2 = r z_1$** : This is a pure **stretching** (or magnification) by factor $r$.
3.  **$w = z_2 + B$** : This is a pure **translation** by the vector $B$.
Thus, for $c=0$, it is a combination of rotation, stretching, and translation (no inversion required).

**Case 2: If $c \neq 0$ (The General Case)**
We must perform algebraic long division (or add and subtract cleverly) to separate the $z$ term from the numerator.
$$w = \frac{az + b}{cz + d}$$
Multiply and divide by $c$:
$$w = \frac{\frac{a}{c}(cz) + b}{cz + d}$$
Add and subtract $d$ inside the parenthesis:
$$w = \frac{\frac{a}{c}(cz + d - d) + b}{cz + d}$$
Distribute the $a/c$:
$$w = \frac{\frac{a}{c}(cz + d) - \frac{ad}{c} + b}{cz + d}$$
Separate into two fractions:
$$w = \frac{a}{c} + \frac{b - \frac{ad}{c}}{cz + d}$$
Find a common denominator for the numerator of the second term:
$$w = \frac{a}{c} + \frac{\frac{bc - ad}{c}}{cz + d}$$
$$w = \frac{a}{c} - \frac{ad - bc}{c(cz + d)}$$
$$w = \frac{a}{c} - \left( \frac{ad - bc}{c^2} \right) \frac{1}{z + \frac{d}{c}}$$

This decomposed equation can now be read as a sequence of independent transformations:
Let's define them step-by-step starting from $z$:
1.  **Translation:** $z_1 = z + \frac{d}{c}$ (Translates $z$ by the constant $d/c$).
2.  **Inversion:** $z_2 = \frac{1}{z_1}$ (Inverts the complex number).
3.  **Rotation & Stretching:** $z_3 = -\left(\frac{ad - bc}{c^2}\right) z_2$. Since the term in brackets is a complex constant $K$, multiplying by it represents a rotation by $\arg(K)$ and a stretching by $|K|$.
4.  **Translation:** $w = \frac{a}{c} + z_3$ (Translates the final result by $a/c$).

**Conclusion:**
Because any general bilinear transformation $w = \frac{az+b}{cz+d}$ can be strictly decomposed into this specific sequence of operations ($z \xrightarrow{\text{translate}} z_1 \xrightarrow{\text{invert}} z_2 \xrightarrow{\text{rotate/stretch}} z_3 \xrightarrow{\text{translate}} w$), we have proven it is purely a combination of translation, rotation, stretching, and inversion. **(Proved)**

***

### Q207. Pg 6, Q4(a): Prove that every bilinear transformation transforms a circle of the z-plane into a circle of the w-plane.

*(Note: In the context of this theorem, a straight line is considered a "circle of infinite radius." So the theorem actually states it maps circles and lines to circles and lines. This is conceptually identical to Q213. We will provide the algebraic proof).*

**Solution:**

We need to prove that the mapping $w = \frac{az+b}{cz+d}$ maps the general equation of a circle/line in the $z$-plane to the general equation of a circle/line in the $w$-plane.

**Step 1: State the general equation of a circle/line.**
As proven in Q84, the most general equation representing any circle or straight line in the complex plane is:
$$A z\overline{z} + \overline{B}z + B\overline{z} + C = 0 \quad \text{--- (Equation 1)}$$
where $A$ and $C$ are real constants, and $B$ is a complex constant.
*   If $A \neq 0$, it is a circle.
*   If $A = 0$, it is a straight line.

**Step 2: Express $z$ in terms of $w$.**
We need to map from the $z$-plane to the $w$-plane, so we find the inverse transformation of $w = \frac{az+b}{cz+d}$.
$$w(cz+d) = az+b$$
$$cwz + dw = az+b$$
$$cwz - az = -dw + b$$
$$z(cw - a) = -dw + b$$
$$z = \frac{-dw + b}{cw - a}$$

The complex conjugate of $z$ is:
$$\overline{z} = \frac{-\overline{d}\overline{w} + \overline{b}}{\overline{c}\overline{w} - \overline{a}}$$

**Step 3: Substitute $z$ and $\overline{z}$ into the general circle equation.**
Substitute these expressions into Equation 1:
$$A \left( \frac{-dw+b}{cw-a} \right) \left( \frac{-\overline{d}\overline{w}+\overline{b}}{\overline{c}\overline{w}-\overline{a}} \right) + \overline{B} \left( \frac{-dw+b}{cw-a} \right) + B \left( \frac{-\overline{d}\overline{w}+\overline{b}}{\overline{c}\overline{w}-\overline{a}} \right) + C = 0$$

**Step 4: Clear the denominators.**
Multiply the entire equation by the common denominator $(cw-a)(\overline{c}\overline{w}-\overline{a})$:
$$A(-dw+b)(-\overline{d}\overline{w}+\overline{b}) + \overline{B}(-dw+b)(\overline{c}\overline{w}-\overline{a}) + B(-\overline{d}\overline{w}+\overline{b})(cw-a) + C(cw-a)(\overline{c}\overline{w}-\overline{a}) = 0$$

**Step 5: Expand and group terms by powers of $w$.**
We want to collect terms to form a new equation structured like $P w\overline{w} + \overline{Q}w + Q\overline{w} + S = 0$.

*   **Terms containing $w\overline{w}$:**
    $$A(d\overline{d}) + \overline{B}(-d\overline{c}) + B(-\overline{d}c) + C(c\overline{c})$$
    Let $P = A|d|^2 - \overline{B}d\overline{c} - B\overline{d}c + C|c|^2$.
    Notice that $P$ is a purely real number (since it equals its own conjugate).

*   **Terms containing only $w$:**
    $$A(-d\overline{b}) + \overline{B}(d\overline{a}) + B(b\overline{c}) + C(-c\overline{a})$$
    Let this coefficient be $\overline{Q}$.

*   **Terms containing only $\overline{w}$:**
    $$A(-b\overline{d}) + \overline{B}(-b\overline{c}) + B(\overline{b}c) + C(-a\overline{c})$$
    Let this coefficient be $Q$. (It is easy to verify that this is exactly the conjugate of $\overline{Q}$).

*   **Constant terms (no $w$):**
    $$A(b\overline{b}) + \overline{B}(-b\overline{a}) + B(-\overline{b}a) + C(a\overline{a})$$
    Let $S = A|b|^2 - \overline{B}b\overline{a} - B\overline{b}a + C|a|^2$.
    Notice that $S$ is a purely real number.

**Step 6: Conclusion.**
After grouping, the transformed equation in the $w$-plane is:
$$P w\overline{w} + \overline{Q}w + Q\overline{w} + S = 0$$
Since $P$ and $S$ are real numbers and $Q$ is a complex number, this equation is structurally identical to the general equation of a circle/line (Equation 1). 
Therefore, any circle or line in the $z$-plane maps exactly to a circle or line in the $w$-plane under a bilinear transformation. **(Proved)**

***

### Q208. Problem 8.1: Let $w=f(z)=u+iv$ be analytic in a region R. Prove that $\frac{\partial(u,v)}{\partial(x,y)}=\vert{}f^{\prime}(z)\vert{}^{2}$

**Solution:**

We must prove that the Jacobian determinant of the transformation from $(x,y)$ to $(u,v)$ is equal to the square of the modulus of the complex derivative $f'(z)$.

**Step 1: Define the Jacobian determinant.**
The mathematical definition of the Jacobian of the transformation $(u,v)$ with respect to $(x,y)$ is the determinant of the matrix of their first partial derivatives:
$$J = \frac{\partial(u,v)}{\partial(x,y)} = \det \begin{pmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{pmatrix}$$
Using our standard notation:
$$J = \det \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix}$$

**Step 2: Evaluate the determinant.**
$$J = u_x v_y - u_y v_x \quad \text{--- (Equation 1)}$$

**Step 3: Apply the Cauchy-Riemann equations.**
Because the function $f(z)$ is analytic in the region $R$, the Cauchy-Riemann equations must hold everywhere in $R$:
1.  $u_x = v_y$
2.  $u_y = -v_x$

We will use these equations to eliminate the $y$-derivatives from Equation 1.
*   Replace $v_y$ with $u_x$.
*   Replace $u_y$ with $-v_x$.

Substitute these into Equation 1:
$$J = u_x(u_x) - (-v_x)v_x$$
$$J = (u_x)^2 + (v_x)^2$$

**Step 4: Relate the result to the complex derivative.**
The standard expression for the complex derivative of an analytic function is:
$$f'(z) = u_x + iv_x$$

The square of the modulus (absolute magnitude) of this complex derivative is defined as the sum of the squares of its real and imaginary parts:
$$|f'(z)|^2 = (u_x)^2 + (v_x)^2$$

**Step 5: Conclude.**
Comparing the results of Step 3 and Step 4, we see they are perfectly identical.
$$J = |f'(z)|^2$$
$$\frac{\partial(u,v)}{\partial(x,y)} = |f'(z)|^2$$
**(Proved)**

Here are the detailed solutions for the next four questions (Q209 to Q212).

### Q209. Problem 8.2: Prove that the bilinear transformation can be considered as a combination of the transformations of translation, rotation, stretching, and inversion.

*(Note: This is identical to Q206. The detailed algebraic proof is provided again below for completeness).*

**Solution:**

A standard **bilinear transformation** (or Möbius transformation) maps the complex $z$-plane to the $w$-plane via the equation:
$$w = \frac{az + b}{cz + d} \quad \text{where } ad - bc \neq 0$$

To prove this theorem, we must decompose this single algebraic fraction into a sequence of simpler, foundational geometric transformations.

**Case 1: If $c = 0$**
The condition $ad - bc \neq 0$ becomes $ad \neq 0$, meaning neither $a$ nor $d$ is zero.
The transformation simplifies to:
$$w = \frac{a}{d}z + \frac{b}{d}$$
Let $A = a/d$ and $B = b/d$. This is a linear transformation: $w = Az + B$.
If we write $A$ in polar form as $A = r e^{i\theta}$, the transformation sequence is:
1.  **$z_1 = e^{i\theta} z$** : A pure **rotation** by angle $\theta$.
2.  **$z_2 = r z_1$** : A pure **stretching** (magnification) by factor $r$.
3.  **$w = z_2 + B$** : A pure **translation** by the complex vector $B$.
Thus, for $c=0$, the transformation is a combination of rotation, stretching, and translation (inversion is not needed).

**Case 2: If $c \neq 0$ (The General Case)**
We must perform algebraic manipulation to separate the variable $z$ from the numerator.
$$w = \frac{az + b}{cz + d}$$
Multiply and divide the numerator by $c$:
$$w = \frac{\frac{a}{c}(cz) + b}{cz + d}$$
Add and subtract $d$ inside the parenthesis to match the denominator:
$$w = \frac{\frac{a}{c}(cz + d - d) + b}{cz + d}$$
Distribute $\frac{a}{c}$:
$$w = \frac{\frac{a}{c}(cz + d) - \frac{ad}{c} + b}{cz + d}$$
Separate the fraction into two parts:
$$w = \frac{\frac{a}{c}(cz + d)}{cz + d} + \frac{b - \frac{ad}{c}}{cz + d}$$
$$w = \frac{a}{c} + \frac{\frac{bc - ad}{c}}{c(z + \frac{d}{c})}$$
$$w = \frac{a}{c} - \frac{ad - bc}{c^2} \cdot \frac{1}{z + \frac{d}{c}}$$

This decomposed equation can now be read strictly as a sequence of distinct geometric operations. Let's trace a point $z$ through the sequence:
1.  **$z_1 = z + \frac{d}{c}$** : This is a pure **translation** by the vector $d/c$.
2.  **$z_2 = \frac{1}{z_1}$** : This is a pure **inversion** (mapping points outside the unit circle to the inside, and vice versa).
3.  **$z_3 = -\left(\frac{ad - bc}{c^2}\right) z_2$** : Since the term in brackets is a complex constant $K$, multiplying by it represents a **rotation** by $\arg(K)$ and a **stretching** by $|K|$.
4.  **$w = z_3 + \frac{a}{c}$** : This is a final pure **translation** by the vector $a/c$.

**Conclusion:**
Because the general bilinear formula $w = \frac{az+b}{cz+d}$ can be decomposed exactly into a sequential chain of translation, inversion, rotation/stretching, and translation, we have proven it is purely a combination of these foundational transformations. **(Proved)**

***

### Q210. Problem 8.3: Find a bilinear transformation that maps points $z_{1},$ $z_{2}$, $z_{3}$ of the z plane into points $w_{1}$, $w_{2}$, $w_{3}$ of the w plane, respectively.

**Solution:**

This question asks for the derivation of the standard cross-ratio formula used to find a specific bilinear transformation given three distinct points in both planes.

**Step 1: State the general bilinear transformation.**
$$w = \frac{az + b}{cz + d}$$
Or, rearranged linearly:
$$w(cz + d) - (az + b) = 0$$
$$cwz + dw - az - b = 0 \quad \text{--- (Equation 1)}$$

**Step 2: Establish the conditions.**
We are given that the points map respectively:
*   $z_1 \to w_1$
*   $z_2 \to w_2$
*   $z_3 \to w_3$

Substitute these pairs into Equation 1 to create three specific equations:
$$cw_1z_1 + dw_1 - az_1 - b = 0 \quad \text{--- (Eq 2)}$$
$$cw_2z_2 + dw_2 - az_2 - b = 0 \quad \text{--- (Eq 3)}$$
$$cw_3z_3 + dw_3 - az_3 - b = 0 \quad \text{--- (Eq 4)}$$

**Step 3: Eliminate the constants by subtraction.**
We want to find differences.
Subtract Eq 2 from Eq 1 (to find $w - w_1$):
$$c(wz - w_1z_1) + d(w - w_1) - a(z - z_1) = 0$$
This isn't quite what we want. Instead, let's use the explicit fraction form to find differences:
$$w - w_k = \frac{az + b}{cz + d} - \frac{az_k + b}{cz_k + d}$$
$$w - w_k = \frac{(az+b)(cz_k+d) - (az_k+b)(cz+d)}{(cz+d)(cz_k+d)}$$
Expand the numerator:
$$aczz_k + adz + bcz_k + bd - [aczz_k + adz_k + bcz + bd]$$
$$adz - adz_k - bcz + bcz_k$$
$$a(z - z_k)d - bc(z - z_k)$$
$$w - w_k = \frac{(ad - bc)(z - z_k)}{(cz+d)(cz_k+d)}$$

**Step 4: Construct the specific differences.**
Using the identity derived above, we can write out the four differences needed for the cross-ratio:
1.  $w - w_1 = \frac{(ad-bc)(z-z_1)}{(cz+d)(cz_1+d)}$
2.  $w - w_3 = \frac{(ad-bc)(z-z_3)}{(cz+d)(cz_3+d)}$
3.  $w_2 - w_1 = \frac{(ad-bc)(z_2-z_1)}{(cz_2+d)(cz_1+d)}$
4.  $w_2 - w_3 = \frac{(ad-bc)(z_2-z_3)}{(cz_2+d)(cz_3+d)}$

**Step 5: Form the cross-ratio.**
Divide (1) by (2), and divide (3) by (4), then set them as a ratio.
$$\frac{w - w_1}{w - w_3} = \frac{z - z_1}{z - z_3} \cdot \frac{cz_3+d}{cz_1+d}$$
$$\frac{w_2 - w_1}{w_2 - w_3} = \frac{z_2 - z_1}{z_2 - z_3} \cdot \frac{cz_3+d}{cz_1+d}$$

Now, divide the first resulting equation by the second resulting equation. Notice that the $\frac{cz_3+d}{cz_1+d}$ terms perfectly cancel out, as does the $(ad-bc)$ determinant.

$$\frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}$$

**Answer:** 
The required bilinear transformation is found by solving the **cross-ratio implicit equation** for $w$:
**$\frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}$**

***

### Q211. Problem 8.4: Find bilinear transformation that maps points $z=0,$ $i$ , -1 into $w=i,1,0,$ respectively.

**Solution:**

We use the cross-ratio formula derived in Q210 to map three specific points to three specific targets.

**Step 1: Identify the points.**
*   $z_1 = 0 \implies w_1 = i$
*   $z_2 = i \implies w_2 = 1$
*   $z_3 = -1 \implies w_3 = 0$

**Step 2: Apply the cross-ratio formula.**
$$\frac{(w - w_1)(w_2 - w_3)}{(w - w_3)(w_2 - w_1)} = \frac{(z - z_1)(z_2 - z_3)}{(z - z_3)(z_2 - z_1)}$$

Substitute the given points:
$$\frac{(w - i)(1 - 0)}{(w - 0)(1 - i)} = \frac{(z - 0)(i - (-1))}{(z - (-1))(i - 0)}$$
$$\frac{(w - i)(1)}{w(1 - i)} = \frac{z(i + 1)}{(z + 1)(i)}$$

**Step 3: Solve for $w$.**
We need to isolate $w$ algebraically.
Multiply both sides by $w(1-i)$ and $(z+1)i$ to clear fractions:
$$(w - i)(z + 1)i = z(i + 1)w(1 - i)$$

Simplify the right side. $(1+i)(1-i)$ is a difference of squares: $1^2 - i^2 = 1 - (-1) = 2$.
$$(w - i)(z + 1)i = z(2)w$$
$$(w - i)(zi + i) = 2zw$$
Expand the left side:
$$wzi + wi - izi - i^2 = 2zw$$
Since $i^2 = -1$:
$$wzi + wi - zi^2 + 1 = 2zw$$
$$wzi + wi + z + 1 = 2zw$$

Gather all terms containing $w$ on one side:
$$z + 1 = 2zw - wzi - wi$$
Factor out $w$ on the right side:
$$z + 1 = w(2z - zi - i)$$
$$w = \frac{z + 1}{2z - zi - i}$$

Factor out $z$ in the denominator to make it look cleaner:
$$w = \frac{z + 1}{z(2 - i) - i}$$

**Answer:** The bilinear transformation is **$w = \frac{z + 1}{(2 - i)z - i}$**.

***

### Q212. Problem 8.5: Find a bilinear transformation that maps the upper half of the z plane into the unit circle in the w plane in such a way that $z=i$ is mapped into $w=0$ while the point at infinity is mapped into $w=-1$

**Solution:**

We need to find $w = f(z) = \frac{az+b}{cz+d}$ satisfying specific boundary and interior mappings.

**Step 1: Analyze the given mappings.**
1.  Upper half plane ($Im(z) > 0$) $\to$ Unit circle ($|w| < 1$). This means the real axis ($Im(z)=0$) maps to the boundary of the unit circle ($|w|=1$).
2.  $z_1 = i \to w_1 = 0$
3.  $z_2 = \infty \to w_2 = -1$

**Step 2: Use $z=i \to w=0$ to find the numerator.**
If $w=0$ when $z=i$, then the numerator of the transformation must be $0$ when $z=i$.
$a(i) + b = 0 \implies b = -ai$.
So the transformation looks like:
$$w = \frac{a(z - i)}{cz + d}$$

**Step 3: Use $z=\infty \to w=-1$ to find the denominator.**
To evaluate the limit as $z \to \infty$, we divide numerator and denominator by $z$:
$$w = \lim_{z \to \infty} \frac{a(1 - i/z)}{c + d/z} = \frac{a(1 - 0)}{c + 0} = \frac{a}{c}$$
We are given this limit is $-1$:
$$\frac{a}{c} = -1 \implies c = -a$$
Substitute $c$ into the transformation:
$$w = \frac{a(z - i)}{-az + d}$$

**Step 4: Use symmetry to find $d$.**
Because the real axis ($y=0$) maps to the boundary of the unit circle ($|w|=1$), any point on the real axis must have a modulus of $1$.
Furthermore, if $z=i$ maps to the center $w=0$, then its reflection across the real axis, $z=-i$, must map to the reflection of the center across the unit circle boundary, which is $w=\infty$.
*(Or, more simply: for $w$ to be $\infty$, the denominator must be zero).*
So, at $z = -i$, the denominator must be $0$:
$$-a(-i) + d = 0 \implies ai + d = 0 \implies d = -ai$$

Substitute $d$ into the transformation:
$$w = \frac{a(z - i)}{-az - ai}$$

**Step 5: Simplify.**
Factor out $-a$ from the denominator:
$$w = \frac{a(z - i)}{-a(z + i)}$$
Cancel the $a$:
$$w = -\frac{z - i}{z + i}$$
Or, to write it more cleanly:
$$w = \frac{i - z}{i + z}$$

*(Self Check:
1. $z=i \implies w = (i-i)/(2i) = 0$. Correct.
2. $z=\infty \implies w = \lim \frac{-z}{z} = -1$. Correct.
3. Test a point on the real axis, e.g., $z=0 \implies w = i/i = 1 \implies |w|=1$. Correct.
4. Test upper half plane, e.g., $z=2i \implies w = (i-2i)/(i+2i) = -i/3i = -1/3 \implies |-1/3| < 1$. Correct.)*

**Answer:** The bilinear transformation is **$w = \frac{i - z}{i + z}$** (or $w = -\frac{z - i}{z + i}$).

Here are the detailed solutions for the next four questions (Q213 to Q216).

### Q213. Problem 8.6: Prove that the bilinear transformation transforms circles of the z plane into circles of the w plane where, by circles, we include circles of infinite radius, which are straight lines.

*(Note: This is conceptually identical to Q207, which asked the exact same thing but from a different source document. I will provide the standard algebraic proof here again).*

**Solution:**

We need to prove that the general bilinear transformation $w = \frac{az+b}{cz+d}$ (where $ad-bc \neq 0$) maps the general equation of a circle/line in the $z$-plane to the general equation of a circle/line in the $w$-plane.

**Step 1: State the general equation of a circle or line.**
In the complex plane, any circle or straight line can be represented by the equation:
$$A z\overline{z} + \overline{B}z + B\overline{z} + C = 0 \quad \text{--- (Equation 1)}$$
where $A$ and $C$ are real constants, and $B$ is a complex constant. (If $A \neq 0$, it's a circle; if $A = 0$, it's a line).

**Step 2: Find the inverse transformation to express $z$ in terms of $w$.**
We need to map the equation from $z$ to $w$.
$$w(cz+d) = az+b$$
$$cwz + dw = az+b$$
$$cwz - az = -dw + b$$
$$z(cw - a) = -dw + b$$
$$z = \frac{-dw + b}{cw - a}$$

The complex conjugate is:
$$\overline{z} = \frac{-\overline{d}\overline{w} + \overline{b}}{\overline{c}\overline{w} - \overline{a}}$$

**Step 3: Substitute $z$ and $\overline{z}$ into the general circle equation.**
$$A \left( \frac{-dw+b}{cw-a} \right) \left( \frac{-\overline{d}\overline{w}+\overline{b}}{\overline{c}\overline{w}-\overline{a}} \right) + \overline{B} \left( \frac{-dw+b}{cw-a} \right) + B \left( \frac{-\overline{d}\overline{w}+\overline{b}}{\overline{c}\overline{w}-\overline{a}} \right) + C = 0$$

**Step 4: Clear the denominators.**
Multiply the entire equation by the common denominator $(cw-a)(\overline{c}\overline{w}-\overline{a})$:
$$A(-dw+b)(-\overline{d}\overline{w}+\overline{b}) + \overline{B}(-dw+b)(\overline{c}\overline{w}-\overline{a}) + B(-\overline{d}\overline{w}+\overline{b})(cw-a) + C(cw-a)(\overline{c}\overline{w}-\overline{a}) = 0$$

**Step 5: Expand and group terms by powers of $w$ to form a new equation.**
We want to collect terms to see if it matches the structure of $P w\overline{w} + \overline{Q}w + Q\overline{w} + S = 0$.

*   **Terms containing $w\overline{w}$:**
    $$[A(d\overline{d}) - \overline{B}(d\overline{c}) - B(\overline{d}c) + C(c\overline{c})] w\overline{w}$$
    Let the term in brackets be $P$. Notice that $P$ equals its own conjugate, meaning $P$ is a **real number**.

*   **Terms containing only $w$:**
    $$[A(-d\overline{b}) + \overline{B}(d\overline{a}) + B(b\overline{c}) + C(-c\overline{a})] w$$
    Let the term in brackets be $\overline{Q}$ (a complex constant).

*   **Terms containing only $\overline{w}$:**
    $$[A(-b\overline{d}) + \overline{B}(-b\overline{c}) + B(\overline{b}c) + C(-a\overline{c})] \overline{w}$$
    Let the term in brackets be $Q$. Note that $Q$ is exactly the complex conjugate of $\overline{Q}$.

*   **Constant terms (no $w$ or $\overline{w}$):**
    $$[A(b\overline{b}) - \overline{B}(b\overline{a}) - B(\overline{b}a) + C(a\overline{a})]$$
    Let the term in brackets be $S$. Notice that $S$ equals its own conjugate, meaning $S$ is a **real number**.

**Step 6: Conclusion.**
The transformed equation in the $w$-plane is:
$$P w\overline{w} + \overline{Q}w + Q\overline{w} + S = 0$$
Because $P$ and $S$ are purely real constants, and $Q$ is a complex constant, this new equation is structurally identical to Equation 1. 
Therefore, it represents a circle (if $P \neq 0$) or a straight line (if $P = 0$) in the $w$-plane. **(Proved)**

***

### Q214. Pg 6, Q3(c): Evaluate $\oint_c |z|^2 dz$ around the square with vertices at $(0, 0), (1, 0), (1, 1)$, and $(0, 1)$.

**Solution:**

We need to evaluate a complex contour integral around a closed square path $C$. 
The function to integrate is $f(z) = |z|^2$. Let $z = x + iy$. Then $|z|^2 = x^2 + y^2$.
The differential is $dz = dx + i dy$.

The square $C$ is traversed counterclockwise (standard positive orientation). It consists of four line segments:
1.  **$C_1$**: From $(0,0)$ to $(1,0)$.
2.  **$C_2$**: From $(1,0)$ to $(1,1)$.
3.  **$C_3$**: From $(1,1)$ to $(0,1)$.
4.  **$C_4$**: From $(0,1)$ to $(0,0)$.

The total integral is $\oint_C = \int_{C_1} + \int_{C_2} + \int_{C_3} + \int_{C_4}$.
We substitute $f(z) = x^2 + y^2$ and $dz = dx + i dy$ into the integral:
$$\int (x^2 + y^2) (dx + i dy)$$

**Evaluate over $C_1$ (From $(0,0)$ to $(1,0)$):**
*   Path condition: $y = 0 \implies dy = 0$.
*   Limits: $x$ goes from $0$ to $1$.
*   Integral: $\int_0^1 (x^2 + 0^2)(dx + i(0)) = \int_0^1 x^2 dx = \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{3}$.

**Evaluate over $C_2$ (From $(1,0)$ to $(1,1)$):**
*   Path condition: $x = 1 \implies dx = 0$.
*   Limits: $y$ goes from $0$ to $1$.
*   Integral: $\int_0^1 (1^2 + y^2)(0 + i dy) = i \int_0^1 (1 + y^2) dy = i \left[ y + \frac{y^3}{3} \right]_0^1 = i(1 + \frac{1}{3}) = i\frac{4}{3}$.

**Evaluate over $C_3$ (From $(1,1)$ to $(0,1)$):**
*   Path condition: $y = 1 \implies dy = 0$.
*   Limits: $x$ goes from $1$ down to $0$.
*   Integral: $\int_1^0 (x^2 + 1^2)(dx + i(0)) = \int_1^0 (x^2 + 1) dx = \left[ \frac{x^3}{3} + x \right]_1^0 = 0 - (\frac{1}{3} + 1) = -\frac{4}{3}$.

**Evaluate over $C_4$ (From $(0,1)$ to $(0,0)$):**
*   Path condition: $x = 0 \implies dx = 0$.
*   Limits: $y$ goes from $1$ down to $0$.
*   Integral: $\int_1^0 (0^2 + y^2)(0 + i dy) = i \int_1^0 y^2 dy = i \left[ \frac{y^3}{3} \right]_1^0 = i(0 - \frac{1}{3}) = -i\frac{1}{3}$.

**Sum the parts:**
$$\oint_C |z|^2 dz = \int_{C_1} + \int_{C_2} + \int_{C_3} + \int_{C_4}$$
$$\oint_C |z|^2 dz = \frac{1}{3} + i\frac{4}{3} - \frac{4}{3} - i\frac{1}{3}$$

Group real and imaginary parts:
Real: $\frac{1}{3} - \frac{4}{3} = -\frac{3}{3} = -1$
Imaginary: $i(\frac{4}{3} - \frac{1}{3}) = i(\frac{3}{3}) = i$

**Answer:** The value of the integral is **$-1 + i$**.

***

### Q215. Pg 13, CT-04, 2.(b): (i) Define complex integration. (ii) Apply Green's theorem on the $\int_C f(z)dz$ and hence find the result by using Cauchy Riemann equations .

**Solution:**

**Part (i): Define Complex Integration**
*(This is identical to Q156).*
Let $f(z)$ be a continuous complex-valued function defined in a region, and let $C$ be a piecewise smooth curve in that region from point $A$ to point $B$. The complex line integral $\int_C f(z) dz$ is defined as the limit of the Riemann sum:
$$\int_C f(z) dz = \lim_{n \to \infty} \sum_{k=1}^{n} f(\xi_k) \Delta z_k$$
where the curve is partitioned into $n$ segments of length $\Delta z_k$, and $\xi_k$ is a sample point within the $k$-th segment, provided the limit exists as the maximum segment length approaches zero.
Operationally, if $f(z) = u+iv$ and $dz = dx+idy$, it is evaluated as:
$$\int_C f(z) dz = \int_C (u dx - v dy) + i \int_C (v dx + u dy)$$

---

**Part (ii): Apply Green's Theorem to prove Cauchy's Integral Theorem.**

**Step 1: Express the complex integral as two real line integrals.**
Let $f(z) = u(x,y) + iv(x,y)$ and $dz = dx + i dy$.
We are evaluating over a simple closed curve $C$ bounding a region $R$:
$$\oint_C f(z) dz = \oint_C (u + iv)(dx + i dy)$$
$$\oint_C f(z) dz = \oint_C (u dx - v dy) + i \oint_C (v dx + u dy)$$

**Step 2: State Green's Theorem.**
Green's Theorem in the plane states that for a positively oriented simple closed curve $C$ bounding a region $R$:
$$\oint_C (P dx + Q dy) = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$$

**Step 3: Apply Green's Theorem to the Real part.**
For the real integral $\oint_C (u dx - v dy)$:
Let $P = u$ and $Q = -v$.
$$\oint_C (u dx - v dy) = \iint_R \left( \frac{\partial (-v)}{\partial x} - \frac{\partial (u)}{\partial y} \right) dx dy = \iint_R \left( -v_x - u_y \right) dx dy$$

**Step 4: Apply Green's Theorem to the Imaginary part.**
For the imaginary integral $\oint_C (v dx + u dy)$:
Let $P = v$ and $Q = u$.
$$\oint_C (v dx + u dy) = \iint_R \left( \frac{\partial (u)}{\partial x} - \frac{\partial (v)}{\partial y} \right) dx dy = \iint_R \left( u_x - v_y \right) dx dy$$

**Step 5: Apply the Cauchy-Riemann equations.**
If $f(z)$ is analytic inside and on $C$, it must satisfy the C-R equations everywhere in $R$:
1. $u_x = v_y$
2. $u_y = -v_x$

Substitute these into the double integrals:
*   Real part: $-v_x - u_y$. Since $u_y = -v_x$, this becomes $-v_x - (-v_x) = -v_x + v_x = 0$.
    So, the real double integral evaluates to $\iint_R 0 \ dx dy = 0$.
*   Imaginary part: $u_x - v_y$. Since $u_x = v_y$, this becomes $v_y - v_y = 0$.
    So, the imaginary double integral evaluates to $\iint_R 0 \ dx dy = 0$.

**Step 6: State the final result.**
$$\oint_C f(z) dz = 0 + i(0) = 0$$

**(Result found. This serves as a formal proof of Cauchy's Integral Theorem).**

***

### Q216. Prblm 4.1.1: Evaluate $\int_C \overline{z} dz$ from $z=0$ to $z=4+2i$ along the curve C given by $z=t^2+it$

**Solution:**

We need to evaluate a complex line integral using a given parametric path.
The function is $f(z) = \overline{z}$.
The path $C$ is parameterized by $z(t) = t^2 + it$.

**Step 1: Define the parameter limits for $t$.**
*   Start point: $z = 0 \implies t^2 + it = 0 \implies t = 0$.
*   End point: $z = 4 + 2i$. 
    Equating imaginary parts: $it = 2i \implies t = 2$.
    (Check real part: $t^2 = 2^2 = 4$. Matches).
So, the parameter $t$ ranges from $0$ to $2$.

**Step 2: Parameterize the function $f(z)$.**
$f(z) = \overline{z}$.
Since $z = t^2 + it$, the conjugate is:
$\overline{z} = t^2 - it$.

**Step 3: Parameterize the differential $dz$.**
We need to find $dz$ in terms of $dt$.
$$z = t^2 + it$$
Take the derivative with respect to $t$:
$$dz = \frac{dz}{dt} dt = (2t + i) dt$$

**Step 4: Substitute everything into the integral.**
$$\int_C \overline{z} dz = \int_0^2 (t^2 - it) (2t + i) dt$$

**Step 5: Expand the integrand.**
Use algebraic expansion (FOIL):
$$(t^2 - it) (2t + i) = 2t^3 + it^2 - 2it^2 - i^2 t$$
Since $i^2 = -1$:
$$= 2t^3 - it^2 + t$$
Group into real and imaginary parts:
$$= (2t^3 + t) - i(t^2)$$

**Step 6: Evaluate the definite integral.**
$$\int_0^2 \left[ (2t^3 + t) - i(t^2) \right] dt$$
Integrate term by term:
$$= \left[ \frac{2t^4}{4} + \frac{t^2}{2} - i\frac{t^3}{3} \right]_0^2$$
$$= \left[ \frac{t^4}{2} + \frac{t^2}{2} - i\frac{t^3}{3} \right]_0^2$$

Substitute the upper limit $t=2$ (the lower limit $t=0$ yields $0$):
$$= \left( \frac{2^4}{2} + \frac{2^2}{2} - i\frac{2^3}{3} \right) - 0$$
$$= \left( \frac{16}{2} + \frac{4}{2} - i\frac{8}{3} \right)$$
$$= 8 + 2 - i\frac{8}{3}$$
$$= 10 - \frac{8}{3}i$$

**Answer:** The value of the integral is **$10 - \frac{8}{3}i$**.

Here are the detailed solutions for the next four questions (Q217 to Q220).

### Q217. Prblm-4.1.2: Evaluate $\int_{(0,3)}^{(2,4)}(2y+x^2)dx+(3x-y)dy$ i) Along parabola $x=2t$, $y=t^2+3$ ii) Straight line from $(0,3)$ to $(2,3)$ then $(2,3)$ to $(2,4)$

**Solution:**

We need to evaluate a real line integral of a vector field over two different paths in the xy-plane.
Let the integral be $I = \int_C P dx + Q dy$ where $P(x,y) = 2y + x^2$ and $Q(x,y) = 3x - y$.

**Part (i): Along the parabola $x=2t$, $y=t^2+3$**

**Step 1: Determine the parameter limits for $t$.**
*   Start point $(0,3)$: $x = 0 \implies 2t = 0 \implies t = 0$. (Check y: $0^2+3 = 3$. Correct).
*   End point $(2,4)$: $x = 2 \implies 2t = 2 \implies t = 1$. (Check y: $1^2+3 = 4$. Correct).
Limits are $t = 0$ to $t = 1$.

**Step 2: Find the differentials $dx$ and $dy$ in terms of $t$.**
*   $x = 2t \implies dx = 2 dt$
*   $y = t^2+3 \implies dy = 2t dt$

**Step 3: Substitute the parameterizations into the integrand.**
$P(x,y) dx = [2(t^2+3) + (2t)^2] (2 dt) = [2t^2 + 6 + 4t^2] (2 dt) = (6t^2 + 6) 2 dt = (12t^2 + 12) dt$
$Q(x,y) dy = [3(2t) - (t^2+3)] (2t dt) = [6t - t^2 - 3] (2t dt) = (12t^2 - 2t^3 - 6t) dt$

**Step 4: Set up and evaluate the integral.**
$$I_1 = \int_0^1 [ (12t^2 + 12) + (12t^2 - 2t^3 - 6t) ] dt$$
$$I_1 = \int_0^1 (-2t^3 + 24t^2 - 6t + 12) dt$$
Integrate term by term:
$$= \left[ -\frac{2t^4}{4} + \frac{24t^3}{3} - \frac{6t^2}{2} + 12t \right]_0^1$$
$$= \left[ -\frac{1}{2}t^4 + 8t^3 - 3t^2 + 12t \right]_0^1$$
Substitute $t=1$:
$$= -\frac{1}{2}(1) + 8(1) - 3(1) + 12(1) = -\frac{1}{2} + 8 - 3 + 12 = 17 - 0.5 = 16.5 = \frac{33}{2}$$

**Answer (i): $\frac{33}{2}$**

---
**Part (ii): Straight line from $(0,3)$ to $(2,3)$ then $(2,3)$ to $(2,4)$**

This path consists of two separate line segments. We evaluate them individually and add the results.
$I_2 = \int_{C_a} + \int_{C_b}$

**Evaluate along $C_a$ (From $(0,3)$ to $(2,3)$):**
This is a horizontal line segment.
*   Path condition: $y = 3$. Because $y$ is constant, $dy = 0$.
*   Limits: $x$ goes from $0$ to $2$.
Substitute into the integral:
$$\int_{C_a} (2y+x^2)dx + (3x-y)dy = \int_0^2 (2(3) + x^2)dx + 0$$
$$= \int_0^2 (6 + x^2) dx = \left[ 6x + \frac{x^3}{3} \right]_0^2$$
$$= (12 + \frac{8}{3}) - 0 = \frac{36}{3} + \frac{8}{3} = \frac{44}{3}$$

**Evaluate along $C_b$ (From $(2,3)$ to $(2,4)$):**
This is a vertical line segment.
*   Path condition: $x = 2$. Because $x$ is constant, $dx = 0$.
*   Limits: $y$ goes from $3$ to $4$.
Substitute into the integral:
$$\int_{C_b} (2y+x^2)dx + (3x-y)dy = \int_3^4 0 + (3(2) - y)dy$$
$$= \int_3^4 (6 - y) dy = \left[ 6y - \frac{y^2}{2} \right]_3^4$$
$$= \left( 6(4) - \frac{16}{2} \right) - \left( 6(3) - \frac{9}{2} \right)$$
$$= (24 - 8) - (18 - 4.5) = 16 - 13.5 = 2.5 = \frac{5}{2}$$

**Sum the parts:**
$$I_2 = \frac{44}{3} + \frac{5}{2} = \frac{88}{6} + \frac{15}{6} = \frac{103}{6}$$

**Answer (ii): $\frac{103}{6}$**

***

### Q218. Prblm 4.1.3: Evaluate $\int_0^{1+i}(x^2-iy)dz$ along the path $y=x$

**Solution:**

We need to evaluate a complex line integral.
The function is $f(z) = x^2 - iy$.
The differential is $dz = dx + i dy$.
The path $C$ is the straight line $y = x$, from the origin $(0,0)$ to the point $(1,1)$ which corresponds to $z = 1+i$.

**Step 1: Parameterize the path.**
The simplest parameterization is to let $x$ be the parameter.
Let $x$ range from $0$ to $1$.
Since the path is $y = x$, we substitute $y$ with $x$ everywhere in the integral.

**Step 2: Express differentials in terms of $x$.**
Since $y = x$, taking the derivative gives $dy = dx$.
The complex differential becomes:
$$dz = dx + i dy = dx + i(dx) = (1 + i)dx$$

**Step 3: Substitute everything into the integral.**
$$\int_C (x^2 - iy) dz = \int_0^1 (x^2 - ix) (1 + i) dx$$

**Step 4: Expand the integrand.**
Because $(1+i)$ is a constant with respect to $x$, we can pull it out of the integral:
$$= (1 + i) \int_0^1 (x^2 - ix) dx$$

**Step 5: Evaluate the definite integral.**
Integrate term by term with respect to $x$:
$$= (1 + i) \left[ \frac{x^3}{3} - i\frac{x^2}{2} \right]_0^1$$
Substitute the upper limit $x=1$ (lower limit $x=0$ yields $0$):
$$= (1 + i) \left( \frac{1}{3} - i\frac{1}{2} \right)$$

**Step 6: Perform the final complex multiplication.**
Use FOIL:
$$= (1)\left(\frac{1}{3}\right) + (1)\left(-i\frac{1}{2}\right) + (i)\left(\frac{1}{3}\right) + (i)\left(-i\frac{1}{2}\right)$$
$$= \frac{1}{3} - \frac{1}{2}i + \frac{1}{3}i - i^2\frac{1}{2}$$
Since $i^2 = -1$:
$$= \frac{1}{3} - \frac{1}{2}i + \frac{1}{3}i + \frac{1}{2}$$

Group real and imaginary parts:
Real: $\frac{1}{3} + \frac{1}{2} = \frac{2}{6} + \frac{3}{6} = \frac{5}{6}$
Imaginary: $i(-\frac{1}{2} + \frac{1}{3}) = i(-\frac{3}{6} + \frac{2}{6}) = -i\frac{1}{6}$

**Answer:** The value of the integral is **$\frac{5}{6} - \frac{1}{6}i$**.

***

### Q219. Prblm 4.1.4: Evaluate from $(1,2)$ to $(2,8)$ $\int_C (x^2-iy^2)dz$ i) $y=2x^2$ ii) Straight line from $(1,2)$ to $(2,8)$

**Solution:**

We evaluate $\int_C f(z)dz$ where $f(z) = x^2 - iy^2$ and $dz = dx + idy$.
Substitute these to get the working integral form:
$$I = \int_C (x^2 - iy^2)(dx + i dy)$$
$$I = \int_C (x^2 dx + ix^2 dy - iy^2 dx - i^2 y^2 dy)$$
$$I = \int_C (x^2 + y^2)dx + i(x^2 - y^2)dy$$

**Part (i): Along the parabola $y = 2x^2$**

**Step 1: Parameterize the path.**
Let $x$ be the parameter, going from $1$ to $2$.
Substitute $y = 2x^2$.
Differentiate to find $dy$: $dy = 4x dx$.

**Step 2: Substitute into the integral.**
$$I_1 = \int_1^2 \left( x^2 + (2x^2)^2 \right) dx + i \left( x^2 - (2x^2)^2 \right) (4x dx)$$
$$I_1 = \int_1^2 (x^2 + 4x^4) dx + i (x^2 - 4x^4) 4x dx$$
$$I_1 = \int_1^2 (x^2 + 4x^4) dx + i \int_1^2 (4x^3 - 16x^5) dx$$

**Step 3: Evaluate the integrals.**
Real part:
$$Re(I_1) = \left[ \frac{x^3}{3} + \frac{4x^5}{5} \right]_1^2 = \left( \frac{8}{3} + \frac{4(32)}{5} \right) - \left( \frac{1}{3} + \frac{4}{5} \right)$$
$$= \left( \frac{8}{3} + \frac{128}{5} \right) - \left( \frac{1}{3} + \frac{4}{5} \right) = \frac{7}{3} + \frac{124}{5} = \frac{35 + 372}{15} = \frac{407}{15}$$

Imaginary part:
$$Im(I_1) = \left[ x^4 - \frac{16x^6}{6} \right]_1^2 = \left[ x^4 - \frac{8x^6}{3} \right]_1^2$$
$$= \left( 16 - \frac{8(64)}{3} \right) - \left( 1 - \frac{8}{3} \right) = \left( 16 - \frac{512}{3} \right) - \left( 1 - \frac{8}{3} \right) = 15 - \frac{504}{3} = 15 - 168 = -153$$

**Answer (i): $\frac{407}{15} - 153i$**

---
**Part (ii): Along the straight line from $(1,2)$ to $(2,8)$**

**Step 1: Find the equation of the line.**
Slope $m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{8 - 2}{2 - 1} = 6$.
Point-slope form: $y - 2 = 6(x - 1) \implies y = 6x - 6 + 2 \implies y = 6x - 4$.

**Step 2: Parameterize.**
Let $x$ be the parameter, from $1$ to $2$.
Substitute $y = 6x - 4$.
Differentiate to find $dy$: $dy = 6 dx$.

**Step 3: Substitute into the integral.**
$dz = dx + i(6 dx) = (1+6i)dx$.
$$I_2 = \int_1^2 [x^2 - i(6x-4)^2] (1+6i) dx$$
We can pull out the constant $(1+6i)$:
$$I_2 = (1+6i) \int_1^2 [x^2 - i(36x^2 - 48x + 16)] dx$$
$$I_2 = (1+6i) \int_1^2 [(1 - 36i)x^2 + 48ix - 16i] dx$$

**Step 4: Evaluate the integral.**
$$= (1+6i) \left[ (1 - 36i)\frac{x^3}{3} + 48i\frac{x^2}{2} - 16ix \right]_1^2$$
$$= (1+6i) \left[ (1 - 36i)\frac{x^3}{3} + 24ix^2 - 16ix \right]_1^2$$
Substitute limits (evaluating $F(2) - F(1)$):
$x^3/3 \implies 8/3 - 1/3 = 7/3$
$x^2 \implies 4 - 1 = 3$
$x \implies 2 - 1 = 1$
$$= (1+6i) \left[ (1 - 36i)\left(\frac{7}{3}\right) + 24i(3) - 16i(1) \right]$$
$$= (1+6i) \left[ \frac{7}{3} - 84i + 72i - 16i \right]$$
$$= (1+6i) \left[ \frac{7}{3} - 28i \right]$$

**Step 5: Perform the multiplication.**
$$= 1(\frac{7}{3}) + 1(-28i) + 6i(\frac{7}{3}) + 6i(-28i)$$
$$= \frac{7}{3} - 28i + 14i - 168i^2$$
$$= \frac{7}{3} - 14i + 168$$
$$= \frac{504}{3} + \frac{7}{3} - 14i = \frac{511}{3} - 14i$$

**Answer (ii): $\frac{511}{3} - 14i$**

***

### Q220. Prblm 4.1.5: $\int(z^2+3z)dz$ from $(2,0)$ to $(2,1)$ and $(2,1)$ to $(2,2)$

*(Note: The integration path described is a single continuous vertical line segment from $(2,0)$ up to $(2,2)$. The intermediate point $(2,1)$ just splits it into two collinear segments, which is mathematically identical to integrating straight from start to finish. We will evaluate it as a single line segment for efficiency).*

**Solution:**

We need to evaluate the complex integral $\int_C f(z) dz$ where $f(z) = z^2 + 3z$.
Because $f(z)$ is an analytic polynomial function (entire), its line integral is path-independent. We can evaluate it either by parameterizing the path, or much simpler, by using the Fundamental Theorem of Calculus (finding the antiderivative). Let's do it using the antiderivative for elegance, and then verify with path parameterization.

**Method 1: Fundamental Theorem of Calculus**
Since $f(z) = z^2 + 3z$ is analytic, it has an exact complex antiderivative $F(z) = \frac{z^3}{3} + \frac{3z^2}{2}$.
The integral from $z_1$ to $z_2$ is simply $F(z_2) - F(z_1)$.

*   Start point: $(2,0) \implies z_1 = 2 + 0i = 2$.
*   End point: $(2,2) \implies z_2 = 2 + 2i$.

Evaluate $F(z_2)$:
$$F(2+2i) = \frac{(2+2i)^3}{3} + \frac{3(2+2i)^2}{2}$$
Expand $(2+2i)^2 = 4 + 8i + 4i^2 = 4 + 8i - 4 = 8i$.
Expand $(2+2i)^3 = (2+2i)(8i) = 16i + 16i^2 = -16 + 16i$.
$$F(2+2i) = \frac{-16 + 16i}{3} + \frac{3(8i)}{2} = -\frac{16}{3} + i\frac{16}{3} + 12i = -\frac{16}{3} + i\frac{16+36}{3} = -\frac{16}{3} + \frac{52}{3}i$$

Evaluate $F(z_1)$:
$$F(2) = \frac{2^3}{3} + \frac{3(2^2)}{2} = \frac{8}{3} + \frac{12}{2} = \frac{8}{3} + 6 = \frac{8+18}{3} = \frac{26}{3}$$

Subtract:
$$I = F(2+2i) - F(2) = \left( -\frac{16}{3} + \frac{52}{3}i \right) - \frac{26}{3} = -\frac{42}{3} + \frac{52}{3}i = -14 + \frac{52}{3}i$$

---
**Method 2: Path Parameterization (as requested by typical textbook problems)**
The path is a vertical line from $(2,0)$ to $(2,2)$.
*   Path condition: $x = 2$ is constant. Therefore $dx = 0$.
*   Limits: $y$ goes from $0$ to $2$.
*   Differential: $dz = dx + idy = 0 + idy = i dy$.
*   Variable: $z = x + iy = 2 + iy$.

Substitute into the integral:
$$I = \int_0^2 \left( (2+iy)^2 + 3(2+iy) \right) i dy$$
Expand the integrand:
$$I = \int_0^2 \left( (4 + 4iy - y^2) + (6 + 3iy) \right) i dy$$
$$I = \int_0^2 (10 - y^2 + 7iy) i dy$$
Distribute the $i$:
$$I = \int_0^2 (10i - iy^2 + 7i^2y) dy$$
Since $i^2 = -1$:
$$I = \int_0^2 (-7y + 10i - iy^2) dy$$

Integrate with respect to $y$:
$$I = \left[ -7\frac{y^2}{2} + 10iy - i\frac{y^3}{3} \right]_0^2$$

Substitute the upper limit $y=2$ (lower limit yields 0):
$$I = -7\frac{(2)^2}{2} + 10i(2) - i\frac{(2)^3}{3}$$
$$I = -7(2) + 20i - i\frac{8}{3}$$
$$I = -14 + i\left( 20 - \frac{8}{3} \right)$$
$$I = -14 + i\left( \frac{60 - 8}{3} \right)$$
$$I = -14 + \frac{52}{3}i$$

Both methods yield the exact same result.

**Answer:** The value of the integral is **$-14 + \frac{52}{3}i$**.

Here are the detailed solutions for the next four questions (Q221 to Q224).

### Q221. Prblm 4.3.1: $\oint_C (2xy-x^2)dx+(x+y)dy$ along $y=x^2$ & $x=y^2$

*(Note: This is numerically identical to Q239, which asks to verify Green's Theorem for this integral. We will evaluate the line integral directly and then verify it using the double integral from Green's Theorem).*

**Solution:**

We need to evaluate the closed loop line integral $\oint_C P dx + Q dy$ where $P = 2xy - x^2$ and $Q = x + y$.
The curve $C$ is the boundary of the region enclosed by two parabolas: $y = x^2$ and $x = y^2$.

**Step 1: Find the points of intersection.**
Set $y = x^2$ equal to $x = y^2$.
Substitute $y$: $x = (x^2)^2 \implies x = x^4$.
$x^4 - x = 0 \implies x(x^3 - 1) = 0$.
The real solutions are $x = 0$ and $x = 1$.
*   If $x = 0$, $y = 0^2 = 0$. Point $(0,0)$.
*   If $x = 1$, $y = 1^2 = 1$. Point $(1,1)$.

**Step 2: Define the paths for the line integral.**
To traverse the closed loop counter-clockwise (positive orientation):
*   **Path $C_1$:** Along the lower curve $y = x^2$ from $(0,0)$ to $(1,1)$.
*   **Path $C_2$:** Along the upper curve $x = y^2$ (or $y = \sqrt{x}$) from $(1,1)$ back to $(0,0)$.
The total integral is $I = \int_{C_1} + \int_{C_2}$.

**Step 3: Evaluate $\int_{C_1}$**
*   Path: $y = x^2 \implies dy = 2x dx$.
*   Limits: $x$ from $0$ to $1$.
$$\int_{C_1} = \int_0^1 \left[ (2x(x^2) - x^2)dx + (x + x^2)(2x dx) \right]$$
$$= \int_0^1 [ 2x^3 - x^2 + 2x^2 + 2x^3 ] dx$$
$$= \int_0^1 (4x^3 + x^2) dx = \left[ x^4 + \frac{x^3}{3} \right]_0^1 = 1 + \frac{1}{3} = \frac{4}{3}$$

**Step 4: Evaluate $\int_{C_2}$**
*   Path: Let's use $y$ as the parameter to avoid square roots. Path is $x = y^2 \implies dx = 2y dy$.
*   Limits: $y$ from $1$ down to $0$ (since we are returning to the origin).
$$\int_{C_2} = \int_1^0 \left[ (2(y^2)y - (y^2)^2)(2y dy) + (y^2 + y)dy \right]$$
$$= \int_1^0 \left[ (2y^3 - y^4)(2y) + y^2 + y \right] dy$$
$$= \int_1^0 (4y^4 - 2y^5 + y^2 + y) dy$$
Reverse the limits to remove the negative sign conceptually: $= -\int_0^1 (4y^4 - 2y^5 + y^2 + y) dy$
$$= -\left[ \frac{4y^5}{5} - \frac{2y^6}{6} + \frac{y^3}{3} + \frac{y^2}{2} \right]_0^1$$
$$= -\left( \frac{4}{5} - \frac{1}{3} + \frac{1}{3} + \frac{1}{2} \right) = -\left( \frac{4}{5} + \frac{1}{2} \right) = -\left( \frac{8+5}{10} \right) = -\frac{13}{10}$$

**Step 5: Sum the line integrals.**
$$I = \int_{C_1} + \int_{C_2} = \frac{4}{3} - \frac{13}{10} = \frac{40 - 39}{30} = \frac{1}{30}$$

---
**Verify using Green's Theorem (Double Integral approach):**
Green's Theorem states $\oint_C P dx + Q dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$.
*   $P = 2xy - x^2 \implies \frac{\partial P}{\partial y} = 2x$
*   $Q = x + y \implies \frac{\partial Q}{\partial x} = 1$
Integrand: $\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) = 1 - 2x$.

The region $R$ is bounded by $y = x^2$ (bottom) and $y = \sqrt{x}$ (top), with $x$ from $0$ to $1$.
$$I = \int_0^1 \int_{x^2}^{\sqrt{x}} (1 - 2x) dy dx$$
Inner integral:
$$= \int_0^1 \left[ (1-2x)y \right]_{x^2}^{\sqrt{x}} dx = \int_0^1 (1-2x)(\sqrt{x} - x^2) dx$$
Expand:
$$= \int_0^1 (x^{1/2} - x^2 - 2x^{3/2} + 2x^3) dx$$
Integrate:
$$= \left[ \frac{x^{3/2}}{3/2} - \frac{x^3}{3} - \frac{2x^{5/2}}{5/2} + \frac{2x^4}{4} \right]_0^1$$
$$= \left[ \frac{2}{3}x^{3/2} - \frac{1}{3}x^3 - \frac{4}{5}x^{5/2} + \frac{1}{2}x^4 \right]_0^1$$
Evaluate at 1:
$$= \frac{2}{3} - \frac{1}{3} - \frac{4}{5} + \frac{1}{2} = \frac{1}{3} - \frac{4}{5} + \frac{1}{2} = \frac{10 - 24 + 15}{30} = \frac{1}{30}$$
The values match perfectly.

**Answer:** The value of the integral is **$\frac{1}{30}$**.

***

### Q222. Complen form of Green's Theorem Proof: $\oint_C B(z,\overline{z})dz=2i\iint_R \frac{\partial B}{\partial \overline{z}} dx dy$

*(Note: This is conceptually identical to Q240).*

**Solution:**

We must prove the complex formulation of Green's Theorem using the standard real-variable Green's Theorem.

**Step 1: Express the complex integral in real terms.**
Let the complex function be $B(z, \overline{z}) = U(x,y) + iV(x,y)$.
Let the differential be $dz = dx + i dy$.
Substitute these into the line integral:
$$\oint_C B(z, \overline{z}) dz = \oint_C (U + iV) (dx + i dy)$$
Expand the product and separate real and imaginary parts:
$$\oint_C B dz = \oint_C (U dx - V dy) + i \oint_C (V dx + U dy)$$

**Step 2: Apply the real Green's Theorem.**
Green's Theorem states: $\oint_C P dx + Q dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx dy$.

Apply to the real part ($P=U, Q=-V$):
$$\oint_C (U dx - V dy) = \iint_R \left( \frac{\partial (-V)}{\partial x} - \frac{\partial U}{\partial y} \right) dx dy = \iint_R \left( -V_x - U_y \right) dx dy$$

Apply to the imaginary part ($P=V, Q=U$):
$$i \oint_C (V dx + U dy) = i \iint_R \left( \frac{\partial U}{\partial x} - \frac{\partial V}{\partial y} \right) dx dy = i \iint_R \left( U_x - V_y \right) dx dy$$

**Step 3: Combine the double integrals.**
$$\oint_C B dz = \iint_R \left( -V_x - U_y \right) dx dy + i \iint_R \left( U_x - V_y \right) dx dy$$
Combine into a single double integral:
$$\oint_C B dz = \iint_R \left[ -V_x - U_y + iU_x - iV_y \right] dx dy$$
Factor out an $i$ to match the standard complex derivative form:
$$\oint_C B dz = \iint_R i \left( U_x + iV_x - \frac{1}{i}U_y - V_y \right) dx dy$$
Since $1/i = -i$:
$$\oint_C B dz = i \iint_R \left[ (U_x + iV_x) + i(U_y + iV_y) \right] dx dy \quad \text{--- (Equation 1)}$$

**Step 4: Express partial derivatives using the Wirtinger operator $\frac{\partial}{\partial \overline{z}}$.**
By definition in complex analysis, the Wirtinger derivative with respect to $\overline{z}$ is:
$$\frac{\partial}{\partial \overline{z}} = \frac{1}{2} \left( \frac{\partial}{\partial x} + i\frac{\partial}{\partial y} \right)$$
Apply this operator to our function $B = U + iV$:
$$\frac{\partial B}{\partial \overline{z}} = \frac{1}{2} \left( \frac{\partial}{\partial x} + i\frac{\partial}{\partial y} \right) (U + iV)$$
$$\frac{\partial B}{\partial \overline{z}} = \frac{1}{2} \left[ \left(\frac{\partial U}{\partial x} + i\frac{\partial V}{\partial x}\right) + i\left(\frac{\partial U}{\partial y} + i\frac{\partial V}{\partial y}\right) \right]$$
$$\frac{\partial B}{\partial \overline{z}} = \frac{1}{2} [ (U_x + iV_x) + i(U_y + iV_y) ]$$

Multiply both sides by 2:
$$2 \frac{\partial B}{\partial \overline{z}} = (U_x + iV_x) + i(U_y + iV_y)$$

**Step 5: Substitute back into the integral.**
Notice that the right side of this equation is exactly the term inside the brackets in Equation 1. Substitute it in:
$$\oint_C B dz = i \iint_R \left[ 2 \frac{\partial B}{\partial \overline{z}} \right] dx dy$$
Pull the constant 2 to the front:
$$\oint_C B(z,\overline{z}) dz = 2i \iint_R \frac{\partial B}{\partial \overline{z}} dx dy$$
**(Proved)**

***

### Q223. Prblm 4.4.9: $F=3z+5$, $z=t^2+it$ Total Work done $z=0$ to $z=4+2i$

*(Note: This is numerically identical to Q288. In physics, work done by a complex force field $F(z)$ along a path $C$ is defined as the line integral $\int_C F(z) dz$).*

**Solution:**

We need to evaluate the line integral $W = \int_C (3z+5) dz$ along the path given by $z(t) = t^2 + it$.

**Step 1: Find the parameter limits.**
*   Start: $z = 0 \implies t^2 + it = 0 \implies t = 0$.
*   End: $z = 4 + 2i$. Equating imaginary parts: $it = 2i \implies t = 2$.
The parameter $t$ ranges from $0$ to $2$.

**Step 2: Find the differential $dz$.**
$$z = t^2 + it \implies dz = (2t + i) dt$$

**Step 3: Substitute everything into the integral.**
Substitute $z$ into the force field $F(z)$:
$$F(z) = 3(t^2 + it) + 5 = 3t^2 + 5 + 3it$$

Set up the integral:
$$W = \int_0^2 (3t^2 + 5 + 3it) (2t + i) dt$$

**Step 4: Expand the integrand.**
Use algebraic distribution:
$$(3t^2 + 5 + 3it) (2t + i) = 3t^2(2t) + 3t^2(i) + 5(2t) + 5(i) + 3it(2t) + 3it(i)$$
$$= 6t^3 + 3it^2 + 10t + 5i + 6it^2 + 3i^2t$$
Since $i^2 = -1$:
$$= 6t^3 + 3it^2 + 10t + 5i + 6it^2 - 3t$$
Group like terms:
$$= (6t^3 + 7t) + i(9t^2 + 5)$$

**Step 5: Evaluate the definite integral.**
$$W = \int_0^2 \left[ (6t^3 + 7t) + i(9t^2 + 5) \right] dt$$
Integrate term by term:
$$W = \left[ \frac{6t^4}{4} + \frac{7t^2}{2} + i\left(\frac{9t^3}{3} + 5t\right) \right]_0^2$$
$$W = \left[ \frac{3}{2}t^4 + \frac{7}{2}t^2 + i(3t^3 + 5t) \right]_0^2$$

Substitute the upper limit $t=2$ (the lower limit yields $0$):
$$W = \left( \frac{3}{2}(16) + \frac{7}{2}(4) \right) + i\left( 3(8) + 5(2) \right)$$
$$W = (24 + 14) + i(24 + 10)$$
$$W = 38 + 34i$$

*(Alternative Method: Since $F(z)=3z+5$ is analytic, the integral is path-independent. We can use the antiderivative $W = [\frac{3z^2}{2} + 5z]_0^{4+2i}$. 
$z^2 = (4+2i)^2 = 16 + 16i - 4 = 12 + 16i$. 
$W = \frac{3(12+16i)}{2} + 5(4+2i) = (18 + 24i) + (20 + 10i) = 38 + 34i$. Both methods match perfectly).*

**Answer:** The total work done is **$38 + 34i$**.

***

### Q224. Example: Evaluate $\int_{0}^{2+i}(\overline{z})^{2}dz$ along the real axis from $z=0$ to $z=2$ and then along a line parallel to y-axis from $z=2$ to $z=2+i.$

**Solution:**

We need to evaluate a complex line integral along a path composed of two straight-line segments.
The function is $f(z) = (\overline{z})^2$.
Let $z = x + iy$. Then $\overline{z} = x - iy$.
The function becomes: $f(z) = (x - iy)^2 = x^2 - y^2 - 2ixy$.
The differential is $dz = dx + i dy$.

The path $C$ is split into two parts: $I = \int_{C_1} + \int_{C_2}$.
1.  **$C_1$**: Along the real axis from $(0,0)$ to $(2,0)$.
2.  **$C_2$**: Vertical line from $(2,0)$ up to $(2,1)$.

**Evaluate along $C_1$:**
*   Path condition: $y = 0 \implies dy = 0$.
*   Limits: $x$ from $0$ to $2$.
Substitute into $f(z)dz$:
$f(z) = x^2 - 0^2 - 2ix(0) = x^2$
$dz = dx + i(0) = dx$
$$I_1 = \int_0^2 x^2 dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3} - 0 = \frac{8}{3}$$

**Evaluate along $C_2$:**
*   Path condition: $x = 2 \implies dx = 0$.
*   Limits: $y$ from $0$ to $1$.
Substitute into $f(z)dz$:
$f(z) = (2)^2 - y^2 - 2i(2)y = 4 - y^2 - 4iy$
$dz = 0 + i dy = i dy$
$$I_2 = \int_0^1 (4 - y^2 - 4iy)(i dy)$$
Distribute the $i$:
$$I_2 = \int_0^1 (4i - iy^2 - 4i^2y) dy$$
Since $i^2 = -1$:
$$I_2 = \int_0^1 (4y + 4i - iy^2) dy$$
Integrate term by term with respect to $y$:
$$I_2 = \left[ 2y^2 + 4iy - i\frac{y^3}{3} \right]_0^1$$
Substitute the upper limit $y=1$:
$$I_2 = 2(1) + 4i(1) - i\frac{1}{3} = 2 + 4i - \frac{1}{3}i = 2 + i\left(\frac{12 - 1}{3}\right) = 2 + \frac{11}{3}i$$

**Sum the parts:**
$$I = I_1 + I_2 = \frac{8}{3} + \left( 2 + \frac{11}{3}i \right) = \left( \frac{8}{3} + \frac{6}{3} \right) + \frac{11}{3}i = \frac{14}{3} + \frac{11}{3}i$$

**Answer:** The value of the integral is **$\frac{14}{3} + \frac{11}{3}i$**.


Here are the detailed solutions for the next four questions (Q225 to Q228).

### Q225. Example: Find the value of the integral $\int_{0}^{1+i}(x-y+i~x^{2})dz$ (a) Along the straight line from $z=0$ to $z=1+i$; (b) Along real axis from $z=0$ to $z=1$ and then along a line parallel to the imaginary axis from $z=1$ to $z=1+i$

**Solution:**

We must evaluate the integral $\int_C f(z)dz$ where $f(z) = (x-y) + ix^2$ and $dz = dx + idy$.
Substitute these into the integral:
$$I = \int_C [(x-y) + ix^2](dx + idy)$$
$$I = \int_C (x-y)dx + i(x-y)dy + ix^2 dx + i^2 x^2 dy$$
Since $i^2 = -1$:
$$I = \int_C [(x-y)dx - x^2 dy] + i[(x-y)dy + x^2 dx]$$

**Part (a): Along the straight line from $(0,0)$ to $(1,1)$**
The path is the line connecting the origin to $(1,1)$. The equation of this line is $y = x$.
*   Path condition: $y = x \implies dy = dx$.
*   Limits: $x$ goes from $0$ to $1$.

Substitute $y=x$ and $dy=dx$ into the integrand:
$$[(x-x)dx - x^2 dx] + i[(x-x)dx + x^2 dx]$$
$$[-x^2 dx] + i[x^2 dx]$$
$$(-x^2 + ix^2)dx$$

Set up the definite integral:
$$I_a = \int_0^1 (-x^2 + ix^2) dx = (-1+i)\int_0^1 x^2 dx$$
$$I_a = (-1+i) \left[ \frac{x^3}{3} \right]_0^1 = (-1+i) \left( \frac{1}{3} \right)$$
$$I_a = -\frac{1}{3} + \frac{1}{3}i$$

---
**Part (b): Path composed of two segments (0,0) to (1,0) then (1,0) to (1,1)**
This requires evaluating two separate integrals and adding them. Let $I_b = \int_{C_1} + \int_{C_2}$.

**Evaluate over $C_1$ (From $(0,0)$ to $(1,0)$):**
*   Path condition: $y = 0 \implies dy = 0$.
*   Limits: $x$ goes from $0$ to $1$.
Substitute into the general integral:
$$\int_{C_1} = \int_0^1 [(x-0)dx - x^2(0)] + i[(x-0)(0) + x^2 dx]$$
$$\int_{C_1} = \int_0^1 (xdx + ix^2 dx) = \int_0^1 (x + ix^2) dx$$
$$= \left[ \frac{x^2}{2} + i\frac{x^3}{3} \right]_0^1 = \frac{1}{2} + \frac{1}{3}i$$

**Evaluate over $C_2$ (From $(1,0)$ to $(1,1)$):**
*   Path condition: $x = 1 \implies dx = 0$.
*   Limits: $y$ goes from $0$ to $1$.
Substitute into the general integral:
$$\int_{C_2} = \int_0^1 [(1-y)(0) - 1^2 dy] + i[(1-y)dy + 1^2(0)]$$
$$\int_{C_2} = \int_0^1 (-dy + i(1-y)dy) = \int_0^1 (-1 + i - iy) dy$$
$$= \left[ -y + iy - i\frac{y^2}{2} \right]_0^1$$
$$= -1 + i - \frac{1}{2}i = -1 + \frac{1}{2}i$$

**Sum the parts:**
$$I_b = I_{C_1} + I_{C_2} = \left( \frac{1}{2} + \frac{1}{3}i \right) + \left( -1 + \frac{1}{2}i \right)$$
$$I_b = \left( \frac{1}{2} - 1 \right) + i\left( \frac{1}{3} + \frac{1}{2} \right) = -\frac{1}{2} + \frac{5}{6}i$$

**Answer:** 
*(a)* **$-\frac{1}{3} + \frac{1}{3}i$**
*(b)* **$-\frac{1}{2} + \frac{5}{6}i$**
*(Notice that because $f(z)$ is not an analytic function—it doesn't satisfy C-R equations—the integral is path-dependent, yielding different answers).*

***

### Q226. Example: Evaluate $\int_{C}zdz$ where C is given by $x=3t$, $y=t^{2}$, $-1\le t\le4$.

**Solution:**

We evaluate $\int_C z dz$ using the given parametric equations for the path.
Given $z = x + iy$.
Substitute the parameterizations:
$$z(t) = 3t + i(t^2)$$

**Step 1: Find the differential $dz$.**
Differentiate $z(t)$ with respect to $t$:
$$dz = \frac{dz}{dt} dt = (3 + 2it) dt$$

**Step 2: Set up the definite integral.**
Substitute $z$ and $dz$ into the integral, using the provided limits for $t$ from $-1$ to $4$:
$$I = \int_{-1}^4 (3t + it^2)(3 + 2it) dt$$

**Step 3: Expand the integrand.**
Use FOIL to multiply the complex terms:
$$(3t + it^2)(3 + 2it) = 9t + 6it^2 + 3it^2 + 2i^2t^3$$
Since $i^2 = -1$:
$$= 9t + 9it^2 - 2t^3$$
Rearrange to group real and imaginary parts:
$$= (9t - 2t^3) + i(9t^2)$$

**Step 4: Evaluate the definite integral.**
$$I = \int_{-1}^4 \left[ (9t - 2t^3) + i(9t^2) \right] dt$$
Integrate term by term:
$$I = \left[ \frac{9t^2}{2} - \frac{2t^4}{4} + i\frac{9t^3}{3} \right]_{-1}^4$$
$$I = \left[ \frac{9}{2}t^2 - \frac{1}{2}t^4 + i3t^3 \right]_{-1}^4$$

**Step 5: Substitute the limits.**
Evaluate at the upper limit $t=4$:
$$F(4) = \frac{9}{2}(16) - \frac{1}{2}(256) + i3(64) = 72 - 128 + 192i = -56 + 192i$$

Evaluate at the lower limit $t=-1$:
$$F(-1) = \frac{9}{2}(1) - \frac{1}{2}(1) + i3(-1) = \frac{9}{2} - \frac{1}{2} - 3i = \frac{8}{2} - 3i = 4 - 3i$$

Subtract the lower limit evaluation from the upper limit evaluation:
$$I = F(4) - F(-1) = (-56 + 192i) - (4 - 3i)$$
$$I = -56 - 4 + 192i + 3i = -60 + 195i$$

*(Alternative Method: Because $f(z) = z$ is analytic, the integral is path independent. We can use the antiderivative $F(z) = z^2/2$. Start point $z(-1) = -3 + i$. End point $z(4) = 12 + 16i$. $I = \frac{1}{2}[ (12+16i)^2 - (-3+i)^2 ] = \frac{1}{2}[ (144 + 384i - 256) - (9 - 6i - 1) ] = \frac{1}{2}[ (-112 + 384i) - (8 - 6i) ] = \frac{1}{2}[ -120 + 390i ] = -60 + 195i$. Both match).*

**Answer:** The value of the integral is **$-60 + 195i$**.

***

### Q227. Example: Evaluate $\oint_{C}\frac{1}{z}dz$ where C is the circle $x=cos~t$, $y=sin~t,0\le t\le2\pi.$

**Solution:**

We are asked to evaluate the contour integral of $f(z) = 1/z$ around the unit circle.

**Step 1: Write the path $C$ in complex exponential notation.**
We are given $x = \cos t$ and $y = \sin t$.
In the complex plane, $z = x + iy$.
Substitute the parameterizations:
$$z(t) = \cos t + i\sin t$$
By Euler's formula, this simplifies perfectly to:
$$z(t) = e^{it}$$
The limits are given as $0 \le t \le 2\pi$, which represents exactly one full counter-clockwise traversal of the unit circle.

**Step 2: Find the differential $dz$.**
Differentiate $z(t)$ with respect to $t$:
$$dz = \frac{d}{dt}(e^{it}) dt = ie^{it} dt$$

**Step 3: Substitute $z$ and $dz$ into the integral.**
$$\oint_C \frac{1}{z} dz = \int_0^{2\pi} \frac{1}{e^{it}} (ie^{it} dt)$$

**Step 4: Simplify and evaluate.**
The $e^{it}$ terms completely cancel out from the numerator and denominator:
$$= \int_0^{2\pi} i dt$$
Pull the constant $i$ out of the integral:
$$= i \int_0^{2\pi} 1 dt$$
Evaluate the integral:
$$= i [t]_0^{2\pi} = i(2\pi - 0)$$
$$= 2\pi i$$

*(Note: This is one of the most fundamental benchmark results in complex analysis. The integral of $1/z$ around the origin is always $2\pi i$, which forms the entire basis for Cauchy's Integral Formula and Residue Theorem).*

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q228. Example: Evaluate $\int_{C}(x^{2}+iy^{2})dz$ where C is the contour in Fig.

*(Note: Since the figure is missing, I must infer the standard path used for this classic textbook problem. The most common "contour in Fig" for this specific integrand is the closed parabolic-straight line shape evaluated in Q219/Q237, or the boundary of the region $y=x^2, y=x$. I will solve it for the most standard introductory contour: the closed path from $(0,0)$ to $(1,1)$ along $y=x^2$ and returning along $y=x$. If the figure was a square or circle, the method remains identical: split into segments and parameterize).*

**Assumption for Solution:** Evaluate around the closed loop $C$ defined by $y=x^2$ from $(0,0)$ to $(1,1)$, returning via $y=x$ from $(1,1)$ to $(0,0)$. Let $I = \int_{C_1} + \int_{C_2}$.
Integrand: $f(z) = x^2 + iy^2$. Differential $dz = dx + i dy$.
$$I = \int_C (x^2 + iy^2)(dx + idy) = \int_C (x^2dx - y^2dy) + i\int_C (x^2dy + y^2dx)$$

**Evaluate $C_1$ (Curve $y=x^2$ from $x=0$ to $1$):**
*   $y = x^2 \implies dy = 2xdx$.
*   $\int_{C_1} = \int_0^1 [x^2 - (x^2)^2(2x)]dx + i[x^2(2x) + (x^2)^2]dx$
*   $= \int_0^1 (x^2 - 2x^5)dx + i \int_0^1 (2x^3 + x^4)dx$
*   $= \left[ \frac{x^3}{3} - \frac{2x^6}{6} \right]_0^1 + i \left[ \frac{2x^4}{4} + \frac{x^5}{5} \right]_0^1$
*   $= (\frac{1}{3} - \frac{1}{3}) + i(\frac{1}{2} + \frac{1}{5}) = 0 + i\frac{7}{10} = \frac{7}{10}i$.

**Evaluate $C_2$ (Line $y=x$ from $x=1$ to $0$):**
*   $y = x \implies dy = dx$.
*   $\int_{C_2} = \int_1^0 [x^2 - x^2]dx + i[x^2 + x^2]dx$
*   $= \int_1^0 0dx + i\int_1^0 2x^2dx = 0 + i\left[ \frac{2x^3}{3} \right]_1^0 = i(0 - \frac{2}{3}) = -\frac{2}{3}i$.

**Sum the parts:**
$$I = \frac{7}{10}i - \frac{2}{3}i = \left( \frac{21}{30} - \frac{20}{30} \right)i = \frac{1}{30}i$$

*(If the figure was just the parabolic arc from 0 to $1+i$, the answer is just $7i/10$. The steps shown map the universal technique for evaluating this integral given any path).*


Here are the detailed solutions for the next four questions (Q229 to Q232).

### Q229. Example: Evaluate $\oint_{C}\frac{dz}{z^{2}}$ where C is the ellipse $(x-2)^{2}+(y-5)^{2}/4=1$ .

**Solution:**

We need to evaluate the contour integral $\oint_C \frac{1}{z^2} dz$ over a specified closed curve.

**Step 1: Identify the function and its singularities.**
Let $f(z) = \frac{1}{z^2}$.
A singularity occurs where the denominator is zero. Here, the only singularity is at $z = 0$ (the origin).

**Step 2: Analyze the contour $C$.**
The contour $C$ is given by the equation of an ellipse:
$$(x-2)^2 + \frac{(y-5)^2}{4} = 1$$
This is an ellipse with:
*   Center at Cartesian coordinates $(2, 5)$.
*   Semi-major/minor axes of lengths $a=1$ (horizontal) and $b=2$ (vertical).

**Step 3: Determine if the singularity lies inside the contour.**
We must check if the origin $(0,0)$ lies inside, on, or outside this ellipse.
Substitute $x=0, y=0$ into the left side of the ellipse equation:
$$(0 - 2)^2 + \frac{(0 - 5)^2}{4} = (-2)^2 + \frac{(-5)^2}{4} = 4 + \frac{25}{4} = 4 + 6.25 = 10.25$$

The value $10.25$ is much greater than $1$.
Geometrically, this means the point $(0,0)$ lies strictly **outside** the ellipse.

**Step 4: Apply Cauchy's Integral Theorem.**
Cauchy's Integral Theorem states that if a function $f(z)$ is analytic everywhere *inside and on* a simple closed contour $C$, then the integral of $f(z)$ around $C$ is exactly zero.

*   The function $f(z) = 1/z^2$ is analytic everywhere in the complex plane except at $z=0$.
*   We have established that the point $z=0$ lies entirely outside the region bounded by $C$.
*   Therefore, the function $f(z) = 1/z^2$ is perfectly analytic everywhere inside and on the boundary of the ellipse $C$.

By Cauchy's Integral Theorem, the integral must be zero.

**Answer:** **$0$**

***

### Q230. Example: Evaluate $\oint_{C}\frac{dz}{z-i}$ where C is the outer contour in Fig.

*(Note: Since the figure is missing, I must infer the standard properties from similar textbook problems. The specific shape of the outer contour does not matter as long as it is a simple closed curve that encloses the point $z=i$. If it does not enclose $z=i$, the answer is 0. Assuming it is a standard problem where the contour encloses the singularity, we will apply Cauchy's Integral Formula).*

**Solution (Assuming C encloses $z=i$):**

**Step 1: Identify the function and singularity.**
The integral is of the form $\oint_C \frac{f(z)}{z-z_0} dz$.
Here, the numerator function is simply $f(z) = 1$. This is a constant function, which is analytic (entire) everywhere.
The denominator has a root at $z_0 = i$. Thus, there is a simple pole at $z=i$.

**Step 2: Apply Cauchy's Integral Formula.**
Cauchy's Integral Formula states that if $f(z)$ is analytic inside and on a simple closed contour $C$, and if $z_0$ is any point in the interior of $C$, then:
$$\oint_C \frac{f(z)}{z - z_0} dz = 2\pi i \cdot f(z_0)$$

*   We assume the contour $C$ encloses the point $z_0 = i$.
*   Our analytic numerator function is $f(z) = 1$.

**Step 3: Evaluate the formula.**
Substitute $f(z)=1$ and $z_0=i$ into the formula:
$$\oint_C \frac{1}{z - i} dz = 2\pi i \cdot f(i)$$
Since $f(z)$ is the constant $1$, its value at any point, including $i$, is $1$.
$f(i) = 1$

Therefore:
$$\oint_C \frac{1}{z - i} dz = 2\pi i \cdot (1) = 2\pi i$$

**Answer:** **$2\pi i$** (Assuming the contour encloses $z=i$).

***

### Q231. Example: integrate the function $f(z)=z^{2}$ along the path C joining 2 to $1+2i$ as shown

*(Note: Without the figure, we don't know the exact path. However, because $f(z)=z^2$ is an analytic polynomial, its integral is path-independent. Any path joining these two points will yield the exact same result. We will solve it using the Fundamental Theorem of Calculus).*

**Solution:**

We need to evaluate $I = \int_C z^2 dz$ from an initial point $z_1 = 2$ to a final point $z_2 = 1+2i$.

**Step 1: Determine the analyticity of the function.**
The function $f(z) = z^2$ is a polynomial. All complex polynomials are entire functions (analytic everywhere in the complex plane). 
Because the integrand is analytic, the integral is path-independent. We can evaluate it using the Fundamental Theorem of Complex Calculus.

**Step 2: Find the antiderivative.**
Let $F(z)$ be the antiderivative of $f(z) = z^2$.
$$F(z) = \int z^2 dz = \frac{z^3}{3}$$

**Step 3: Apply the Fundamental Theorem of Calculus.**
$$I = \int_{z_1}^{z_2} f(z) dz = F(z_2) - F(z_1)$$
Substitute our points $z_1 = 2$ and $z_2 = 1+2i$:
$$I = F(1+2i) - F(2)$$

**Step 4: Evaluate the bounds.**
*   **Upper bound evaluation:**
    $$F(1+2i) = \frac{(1+2i)^3}{3}$$
    Expand $(1+2i)^3$ using the binomial theorem $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$:
    $$(1+2i)^3 = 1^3 + 3(1^2)(2i) + 3(1)(2i)^2 + (2i)^3$$
    $$(1+2i)^3 = 1 + 6i + 3(4i^2) + 8i^3$$
    Since $i^2 = -1$ and $i^3 = -i$:
    $$(1+2i)^3 = 1 + 6i + 3(-4) + 8(-i)$$
    $$(1+2i)^3 = 1 + 6i - 12 - 8i$$
    $$(1+2i)^3 = -11 - 2i$$
    So, $F(1+2i) = \frac{-11 - 2i}{3} = -\frac{11}{3} - \frac{2}{3}i$.

*   **Lower bound evaluation:**
    $$F(2) = \frac{2^3}{3} = \frac{8}{3}$$

**Step 5: Subtract to find the final integral.**
$$I = \left( -\frac{11}{3} - \frac{2}{3}i \right) - \frac{8}{3}$$
$$I = \left( -\frac{11}{3} - \frac{8}{3} \right) - \frac{2}{3}i$$
$$I = -\frac{19}{3} - \frac{2}{3}i$$

**Answer:** The value of the integral is **$-\frac{19}{3} - \frac{2}{3}i$**.

***

### Q232. Example: integrate the function $f(z)=z^{2}$ along the path Cand then along $C_{1}$ to $C_{2}$ joining 2 to $1+2i$ as shown

*(Note: This question is logically identical to Q231, emphasizing the concept of path independence. Even if the path is broken into different segments $C_1$ and $C_2$, the final result between the same two endpoints for an analytic function is identical).*

**Solution:**

We are asked to integrate $f(z) = z^2$ from point $A(z_1 = 2)$ to point $B(z_2 = 1+2i)$ along a broken path $C_1 + C_2$.

**Key Principle:**
Cauchy's Integral Theorem dictates that for any function $f(z)$ that is analytic in a simply connected domain containing paths $C_A$ and $C_B$, if both paths have the same starting point and the same ending point, then:
$$\int_{C_A} f(z) dz = \int_{C_B} f(z) dz$$
This is the principle of **path independence**.

Since $f(z) = z^2$ is an entire function (analytic everywhere), any path taken from $z=2$ to $z=1+2i$ will yield the exact same numeric result. 

We can bypass parameterizing the potentially complex broken paths $C_1$ and $C_2$ entirely by using the fundamental theorem of calculus, just as we did in Q231.

1.  Antiderivative: $F(z) = z^3/3$.
2.  Evaluate at $z_2 = 1+2i$: $F(1+2i) = \frac{-11-2i}{3}$.
3.  Evaluate at $z_1 = 2$: $F(2) = \frac{8}{3}$.
4.  Subtract: $F(1+2i) - F(2) = \frac{-11-2i-8}{3} = \frac{-19-2i}{3}$.

**Answer:** Because the integral of an analytic function is path-independent, the result is exactly the same as the straight-line integral: **$-\frac{19}{3} - \frac{2}{3}i$**.

Here are the detailed solutions for the next four questions (Q233 to Q236).

### Q233. Example: Evaluate $\int_{C}2z~dz$ where C is shown in Fig 18.20.

*(Note: Without the specific figure, the exact path $C$ is unknown. However, the integrand $f(z) = 2z$ is an analytic polynomial. Therefore, the integral depends ONLY on the start and end points of the contour $C$, not the specific path taken. I will assume the contour starts at a generic point $z_1$ and ends at $z_2$ to demonstrate the method).*

**Solution:**

We must evaluate the complex line integral $I = \int_C 2z dz$.

**Step 1: Determine the analyticity of the integrand.**
The function $f(z) = 2z$ is a polynomial. All polynomials are analytic everywhere in the complex plane (they are entire functions). 
Because the integrand is analytic, the integral is path-independent. We can use the Fundamental Theorem of Complex Calculus to evaluate it directly between the endpoints.

**Step 2: Find the antiderivative.**
Let $F(z)$ be the antiderivative of $f(z) = 2z$.
$$F(z) = \int 2z dz = 2 \frac{z^2}{2} = z^2$$

**Step 3: Apply the Fundamental Theorem.**
Let the path $C$ shown in the figure start at complex point $z_1$ and end at complex point $z_2$.
The integral is evaluated simply by subtracting the antiderivative at the start point from the antiderivative at the end point:
$$I = F(z_2) - F(z_1)$$
$$I = (z_2)^2 - (z_1)^2$$

**Specific Case (Closed Loop):**
If the figure shows a closed loop (where the start point is the same as the end point, $z_1 = z_2$), then:
$$I = (z_1)^2 - (z_1)^2 = 0$$
(This is also guaranteed directly by Cauchy's Integral Theorem for analytic functions on closed contours).

**Answer:** 
The value of the integral is **$z_{end}^2 - z_{start}^2$**. If the contour $C$ is a closed loop, the answer is **$0$**.

***

### Q234. Problem 4.1.1: Evaluate $\int_{C}\overline{z}dz$ from $z=0$ to $z=4+2i$ along the curve C given by $z=t^{2}+it$

*(Note: This is numerically and conceptually identical to Q216. A slightly more streamlined solution is provided below).*

**Solution:**

We are integrating the non-analytic function $f(z) = \overline{z}$. Therefore, the integral is path-dependent, and we must use the given parameterization $z(t) = t^2 + it$.

**Step 1: Determine the parameter limits.**
*   Start point $z=0 \implies t^2 + it = 0 \implies t=0$.
*   End point $z=4+2i \implies t^2=4$ and $t=2 \implies t=2$.
Limits: $t = 0$ to $t = 2$.

**Step 2: Set up the parameterized integrand and differential.**
*   Function: $f(z) = \overline{z} = \overline{t^2 + it} = t^2 - it$
*   Differential: $z = t^2 + it \implies dz = (2t + i)dt$

**Step 3: Substitute into the integral and expand.**
$$I = \int_0^2 (t^2 - it)(2t + i) dt$$
Expand the product:
$$(t^2 - it)(2t + i) = 2t^3 + it^2 - 2it^2 - i^2t$$
Since $i^2 = -1$:
$$= 2t^3 - it^2 + t = (2t^3 + t) - it^2$$

**Step 4: Integrate with respect to $t$.**
$$I = \int_0^2 [(2t^3 + t) - it^2] dt$$
$$I = \left[ \frac{2t^4}{4} + \frac{t^2}{2} - i\frac{t^3}{3} \right]_0^2$$
$$I = \left[ \frac{1}{2}t^4 + \frac{1}{2}t^2 - i\frac{1}{3}t^3 \right]_0^2$$

**Step 5: Evaluate at the limits.**
Substitute $t=2$ (since $t=0$ evaluates to $0$):
$$I = \frac{1}{2}(2)^4 + \frac{1}{2}(2)^2 - i\frac{1}{3}(2)^3$$
$$I = \frac{16}{2} + \frac{4}{2} - i\frac{8}{3}$$
$$I = 8 + 2 - i\frac{8}{3}$$
$$I = 10 - \frac{8}{3}i$$

**Answer:** The value of the integral is **$10 - \frac{8}{3}i$**.

***

### Q235. Problem 4.1.2: Evaluate $\int_{(0,3)}^{(2,4)}(2y+x^{2})dx+(3x-y)dy$ along (i) the parabola $x=2t$, $y=t^{2}+3$ (ii) Straight lines from (0,3) to (2,3) and then (2,3) to (2,4).

*(Note: This is exactly identical to Q217. The solution steps are summarized below).*

**Solution:**

Let $I = \int_C P dx + Q dy$ where $P = 2y + x^2$ and $Q = 3x - y$.

**Part (i): Along the parabola $x=2t$, $y=t^2+3$**
1.  **Limits:** $(0,3) \implies t=0$. $(2,4) \implies t=1$. Range: $[0, 1]$.
2.  **Differentials:** $dx = 2dt$, $dy = 2tdt$.
3.  **Substitute into integrand:**
    $P dx = [2(t^2+3) + (2t)^2](2) dt = [2t^2+6+4t^2]2 dt = (12t^2+12)dt$.
    $Q dy = [3(2t) - (t^2+3)](2t) dt = [6t-t^2-3]2t dt = (12t^2-2t^3-6t)dt$.
4.  **Integrate:**
    $$I_1 = \int_0^1 (12t^2 + 12 + 12t^2 - 2t^3 - 6t) dt = \int_0^1 (-2t^3 + 24t^2 - 6t + 12) dt$$
    $$I_1 = \left[ -\frac{1}{2}t^4 + 8t^3 - 3t^2 + 12t \right]_0^1$$
    $$I_1 = -\frac{1}{2} + 8 - 3 + 12 = 16.5 = \frac{33}{2}$$

---
**Part (ii): Straight lines $(0,3) \to (2,3) \to (2,4)$**
Let $I_2 = \int_{C_a} + \int_{C_b}$.

1.  **Along $C_a$ ($(0,3)$ to $(2,3)$):**
    $y=3 \implies dy=0$. Limits: $x \in [0, 2]$.
    $$\int_{C_a} = \int_0^2 (2(3) + x^2)dx + 0 = \int_0^2 (6+x^2)dx = \left[6x + \frac{x^3}{3}\right]_0^2 = 12 + \frac{8}{3} = \frac{44}{3}$$

2.  **Along $C_b$ ($(2,3)$ to $(2,4)$):**
    $x=2 \implies dx=0$. Limits: $y \in [3, 4]$.
    $$\int_{C_b} = \int_3^4 0 + (3(2) - y)dy = \int_3^4 (6-y)dy = \left[6y - \frac{y^2}{2}\right]_3^4$$
    $$\int_{C_b} = (24 - 8) - (18 - 4.5) = 16 - 13.5 = 2.5 = \frac{5}{2}$$

3.  **Sum the parts:**
    $$I_2 = \frac{44}{3} + \frac{5}{2} = \frac{88}{6} + \frac{15}{6} = \frac{103}{6}$$

**Answer:** 
*(i)* **$\frac{33}{2}$**
*(ii)* **$\frac{103}{6}$**

***

### Q236. Problem 4.1.3: Evaluate $\int_{0}^{1+i}(x^{2}-iy)dz$ along the path $y=x.$

*(Note: This is exactly identical to Q218. A concise solution is provided below).*

**Solution:**

Evaluate $\int_C f(z)dz$ where $f(z) = x^2 - iy$, $dz = dx + idy$, along the path $y=x$ from origin to $1+i$.

**Step 1: Parameterize the path.**
The path is $y=x$.
The differential is $dy = dx$.
The limits for $x$ are from $0$ to $1$.

**Step 2: Substitute into the integral.**
$$I = \int_0^1 (x^2 - ix)(dx + idx)$$
$$I = \int_0^1 (x^2 - ix)(1 + i) dx$$

**Step 3: Evaluate the integral.**
Pull out the constant $(1+i)$:
$$I = (1+i) \int_0^1 (x^2 - ix) dx$$
$$I = (1+i) \left[ \frac{x^3}{3} - i\frac{x^2}{2} \right]_0^1$$
$$I = (1+i) \left( \frac{1}{3} - i\frac{1}{2} \right)$$

**Step 4: Expand the result.**
$$I = \frac{1}{3} - i\frac{1}{2} + i\frac{1}{3} - i^2\frac{1}{2}$$
Since $i^2 = -1$:
$$I = \frac{1}{3} - i\frac{1}{2} + i\frac{1}{3} + \frac{1}{2}$$
$$I = \left(\frac{1}{3} + \frac{1}{2}\right) + i\left(\frac{1}{3} - \frac{1}{2}\right)$$
$$I = \frac{5}{6} - \frac{1}{6}i$$

**Answer:** The value of the integral is **$\frac{5}{6} - \frac{1}{6}i$**.

Here are the detailed solutions for the next four questions (Q237 to Q240).

*(Note: These questions from the Feruj Sheet are identical to earlier questions from the Firoz Note section. Detailed step-by-step solutions are provided again below for completeness).*

### Q237. Problem 4.1.4: Evaluate $\int_{C}(x^{2}-iy^{2})dz$ along (i) the parabola $y=2x^{2}$ from (1, 2) to (2,8) (ii) the straight line from (1, 1) to (2,8)

*(Note: The point "(1,1)" in part (ii) is a typographical error in the source text. It should be "(1,2)" to match part (i) and to connect the same endpoints, which is standard for testing path independence. This is identical to Q219 where it is correctly written as (1,2). I will solve part (ii) using the intended point (1,2)).*

**Solution:**

Evaluate $I = \int_C (x^2 - iy^2)(dx + idy)$.
Expand to separate real and imaginary integrands:
$$I = \int_C (x^2 dx + ix^2 dy - iy^2 dx - i^2 y^2 dy)$$
$$I = \int_C (x^2 + y^2)dx + i \int_C (x^2 - y^2)dy$$

**Part (i): Along the parabola $y = 2x^2$**
1.  **Parameterize:** Let $x \in [1, 2]$. $y = 2x^2 \implies dy = 4xdx$.
2.  **Substitute:**
    $$I_1 = \int_1^2 (x^2 + (2x^2)^2)dx + i \int_1^2 (x^2 - (2x^2)^2)(4xdx)$$
    $$I_1 = \int_1^2 (x^2 + 4x^4)dx + i \int_1^2 (4x^3 - 16x^5)dx$$
3.  **Evaluate:**
    $$I_1 = \left[ \frac{x^3}{3} + \frac{4x^5}{5} \right]_1^2 + i \left[ x^4 - \frac{16x^6}{6} \right]_1^2$$
    Real part: $(\frac{8}{3} + \frac{128}{5}) - (\frac{1}{3} + \frac{4}{5}) = \frac{7}{3} + \frac{124}{5} = \frac{35+372}{15} = \frac{407}{15}$.
    Imaginary part: $(16 - \frac{8(64)}{3}) - (1 - \frac{8}{3}) = (16 - \frac{512}{3}) - (1 - \frac{8}{3}) = 15 - \frac{504}{3} = 15 - 168 = -153$.
4.  **Result:** **$I_1 = \frac{407}{15} - 153i$**

**Part (ii): Along the straight line from $(1,2)$ to $(2,8)$**
1.  **Equation of line:** Slope $m = \frac{8-2}{2-1} = 6$. Equation: $y - 2 = 6(x-1) \implies y = 6x - 4$.
2.  **Parameterize:** Let $x \in [1, 2]$. $y = 6x - 4 \implies dy = 6dx$.
    $dz = dx + idy = dx + 6idx = (1+6i)dx$.
3.  **Substitute (using the original unexpanded integral form for easier algebra):**
    $$I_2 = \int_1^2 [x^2 - i(6x-4)^2](1+6i)dx$$
    $$I_2 = (1+6i) \int_1^2 [x^2 - i(36x^2 - 48x + 16)]dx$$
    $$I_2 = (1+6i) \int_1^2 [(1-36i)x^2 + 48ix - 16i]dx$$
4.  **Evaluate:**
    $$I_2 = (1+6i) \left[ (1-36i)\frac{x^3}{3} + 24ix^2 - 16ix \right]_1^2$$
    Substitute limits (Upper - Lower):
    $= (1+6i) [ (1-36i)(\frac{8}{3}-\frac{1}{3}) + 24i(4-1) - 16i(2-1) ]$
    $= (1+6i) [ (1-36i)(\frac{7}{3}) + 72i - 16i ]$
    $= (1+6i) [ \frac{7}{3} - 84i + 56i ] = (1+6i) [ \frac{7}{3} - 28i ]$
    $= \frac{7}{3} - 28i + 14i - 168i^2 = \frac{7}{3} - 14i + 168 = \frac{511}{3} - 14i$
5.  **Result:** **$I_2 = \frac{511}{3} - 14i$**

*(Note: Because the integrand $x^2-iy^2 = \overline{z}^2$ is not analytic, the integral is path-dependent, resulting in different answers for the two paths).*

***

### Q238. Problem 4.1.5: Evaluate $\int_{C}(z^{2}+3z)dz$ along the straight lines (2,0) to (2, 2) and then from (2, 2) to (0, 2).

*(Note: The integrand is identical to Q220, but the path is different. Because the integrand is an analytic polynomial, the integral is strictly path-independent. We can solve this using the Fundamental Theorem of Calculus directly between the start and end points).*

**Solution:**

We need to evaluate $I = \int_C (z^2+3z)dz$.
The path starts at $z_1 = 2+0i = 2$ and ends at $z_2 = 0+2i = 2i$.

**Method 1: Using the Fundamental Theorem of Complex Calculus (Fastest)**
Because $f(z) = z^2+3z$ is an entire function, its integral depends only on the endpoints.
1.  **Find the antiderivative:** $F(z) = \frac{z^3}{3} + \frac{3z^2}{2}$.
2.  **Evaluate at the upper limit ($z_2 = 2i$):**
    $$F(2i) = \frac{(2i)^3}{3} + \frac{3(2i)^2}{2} = \frac{8i^3}{3} + \frac{3(4i^2)}{2} = \frac{-8i}{3} + \frac{3(-4)}{2} = -\frac{8i}{3} - 6 = -6 - \frac{8}{3}i$$
3.  **Evaluate at the lower limit ($z_1 = 2$):**
    $$F(2) = \frac{2^3}{3} + \frac{3(2^2)}{2} = \frac{8}{3} + \frac{12}{2} = \frac{8}{3} + 6 = \frac{8+18}{3} = \frac{26}{3}$$
4.  **Subtract:**
    $$I = F(2i) - F(2) = \left( -6 - \frac{8}{3}i \right) - \frac{26}{3} = \left( -\frac{18}{3} - \frac{26}{3} \right) - \frac{8}{3}i = -\frac{44}{3} - \frac{8}{3}i$$

**Answer:** The value of the integral is **$-\frac{44}{3} - \frac{8}{3}i$**.

---
*(Optional Method 2: Path Parameterization to verify)*
Let $I = \int_{C_1} + \int_{C_2}$.
*   **$C_1$:** From $(2,0)$ to $(2,2)$. $x=2 \implies dx=0$. $y \in [0,2]$. $z=2+iy$. $dz=idy$.
    $$\int_{C_1} = \int_0^2 [(2+iy)^2 + 3(2+iy)] idy = \int_0^2 (4 - y^2 + 4iy + 6 + 3iy) idy = \int_0^2 (-7y + 10i - iy^2)dy$$
    $$= \left[ -\frac{7y^2}{2} + 10iy - i\frac{y^3}{3} \right]_0^2 = -14 + 20i - i\frac{8}{3} = -14 + \frac{52}{3}i$$
*   **$C_2$:** From $(2,2)$ to $(0,2)$. $y=2 \implies dy=0$. $x \in [2,0]$. $z=x+2i$. $dz=dx$.
    $$\int_{C_2} = \int_2^0 [(x+2i)^2 + 3(x+2i)] dx = \int_2^0 (x^2 - 4 + 4ix + 3x + 6i) dx = \int_2^0 (x^2 + 3x - 4 + i(4x+6)) dx$$
    $$= \left[ \frac{x^3}{3} + \frac{3x^2}{2} - 4x + i(2x^2+6x) \right]_2^0 = 0 - \left( \frac{8}{3} + 6 - 8 + i(8+12) \right)$$
    $$= -\left( \frac{8}{3} - 2 + 20i \right) = -\left( \frac{2}{3} + 20i \right) = -\frac{2}{3} - 20i$$
*   **Sum:** $I = (-14 + \frac{52}{3}i) + (-\frac{2}{3} - 20i) = -\frac{42+2}{3} + i(\frac{52-60}{3}) = -\frac{44}{3} - \frac{8}{3}i$. (Matches perfectly).

***

### Q239. Problem 4.3.1: Verify Green's Theorem in the plane for $\oint_{c}(2xy-x^{2})dx+(x+y^{2})dy$ where C is the closed curve of the region bounded by $y=x^{2}$ and $y^{2}=x$.

*(This is identical to Q221. The full verification requires evaluating both the line integral and the double integral. Steps are summarized below).*

**Solution:**

We must show that $\oint_C P dx + Q dy = \iint_R \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$.
Let $P = 2xy - x^2$ and $Q = x + y^2$.
The intersection points of $y=x^2$ and $x=y^2$ are $(0,0)$ and $(1,1)$.

**Part 1: Evaluate the Line Integral (LHS)**
The path $C$ consists of $C_1$ (lower curve $y=x^2$ from 0 to 1) and $C_2$ (upper curve $x=y^2$ from 1 to 0).
*   **Along $C_1$:** $y=x^2 \implies dy=2xdx$.
    $$I_1 = \int_0^1 [(2x(x^2) - x^2)dx + (x + x^4)(2xdx)] = \int_0^1 (2x^3 - x^2 + 2x^2 + 2x^5)dx$$
    $$= \int_0^1 (2x^5 + 2x^3 + x^2)dx = \left[ \frac{2x^6}{6} + \frac{2x^4}{4} + \frac{x^3}{3} \right]_0^1 = \frac{1}{3} + \frac{1}{2} + \frac{1}{3} = \frac{7}{6}$$
*   **Along $C_2$:** $x=y^2 \implies dx=2ydy$.
    $$I_2 = \int_1^0 [(2(y^2)y - y^4)(2ydy) + (y^2 + y^2)dy] = \int_1^0 (4y^4 - 2y^5 + 2y^2)dy$$
    $$= -\int_0^1 (4y^4 - 2y^5 + 2y^2)dy = -\left[ \frac{4y^5}{5} - \frac{2y^6}{6} + \frac{2y^3}{3} \right]_0^1 = -\left(\frac{4}{5} - \frac{1}{3} + \frac{2}{3}\right) = -\left(\frac{4}{5} + \frac{1}{3}\right) = -\frac{17}{15}$$
*   **Total Line Integral:** $I = I_1 + I_2 = \frac{7}{6} - \frac{17}{15} = \frac{35}{30} - \frac{34}{30} = \frac{1}{30}$.

**Part 2: Evaluate the Double Integral (RHS)**
*   Calculate partials: $\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(x+y^2) = 1$. $\frac{\partial P}{\partial y} = \frac{\partial}{\partial y}(2xy-x^2) = 2x$.
*   Integrand: $1 - 2x$.
*   Region $R$: $x$ goes from $0$ to $1$, $y$ goes from $x^2$ (bottom) to $\sqrt{x}$ (top).
    $$D = \int_0^1 \int_{x^2}^{\sqrt{x}} (1 - 2x) dy dx = \int_0^1 [(1-2x)y]_{x^2}^{\sqrt{x}} dx = \int_0^1 (1-2x)(\sqrt{x} - x^2) dx$$
    $$D = \int_0^1 (x^{1/2} - x^2 - 2x^{3/2} + 2x^3) dx = \left[ \frac{2}{3}x^{3/2} - \frac{1}{3}x^3 - \frac{4}{5}x^{5/2} + \frac{1}{2}x^4 \right]_0^1$$
    $$D = \frac{2}{3} - \frac{1}{3} - \frac{4}{5} + \frac{1}{2} = \frac{1}{3} - \frac{4}{5} + \frac{1}{2} = \frac{10 - 24 + 15}{30} = \frac{1}{30}$$

**Conclusion:** Since LHS ($1/30$) = RHS ($1/30$), Green's Theorem is **verified**.

***

### Q240. Question: Complex form of Green's Theorem: If $B(z,\overline{z})$ is continuous and has continuous partial derivatives in a region and on its boundary C, where $z=x+iy$ and $\overline{z}=x-iy$, Prove that Green's theorem can be written in complex form as $\oint_{C}B(z,\overline{z})dz=2~i\iint_{R}\frac{\partial B}{\partial\overline{z}}dxdy$ .

*(Note: This is identically proven in Q222. The formal steps are summarized below).*

**Solution:**

**Step 1: Express the complex integral in Cartesian terms.**
Let $B = U + iV$ and $dz = dx + idy$.
$$\oint_C B dz = \oint_C (U+iV)(dx+idy) = \oint_C (Udx - Vdy) + i\oint_C (Vdx + Udy)$$

**Step 2: Apply the standard Real Green's Theorem.**
$\oint_C P dx + Q dy = \iint_R (Q_x - P_y) dx dy$.
*   For real part ($P=U, Q=-V$): $\iint_R (-V_x - U_y) dx dy$
*   For imaginary part ($P=V, Q=U$): $\iint_R (U_x - V_y) dx dy$
Combine them:
$$\oint_C B dz = \iint_R \left[ (-V_x - U_y) + i(U_x - V_y) \right] dx dy$$

**Step 3: Factor to expose the complex derivative structure.**
Factor out an $i$ from the integrand. Note that $1 = -i^2$, so $-1 = i^2$.
$$-V_x - U_y + iU_x - iV_y = i(iV_x + iU_y + U_x - V_y) = i [ (U_x + iV_x) + i(U_y + iV_y) ]$$
So the integral becomes:
$$\oint_C B dz = i \iint_R [ (U_x + iV_x) + i(U_y + iV_y) ] dx dy \quad \text{--- (Equation 1)}$$

**Step 4: Define the Wirtinger derivative.**
The derivative operator with respect to $\overline{z}$ is defined as $\frac{\partial}{\partial \overline{z}} = \frac{1}{2}\left( \frac{\partial}{\partial x} + i\frac{\partial}{\partial y} \right)$.
Apply this to $B = U+iV$:
$$\frac{\partial B}{\partial \overline{z}} = \frac{1}{2}\left( \frac{\partial}{\partial x} + i\frac{\partial}{\partial y} \right)(U+iV)$$
$$\frac{\partial B}{\partial \overline{z}} = \frac{1}{2} [ (U_x + iV_x) + i(U_y + iV_y) ]$$
Multiply by 2:
$$2\frac{\partial B}{\partial \overline{z}} = (U_x + iV_x) + i(U_y + iV_y)$$

**Step 5: Substitute back into the integral.**
The right side of this equation perfectly matches the bracketed term in Equation 1.
$$\oint_C B dz = i \iint_R \left( 2\frac{\partial B}{\partial \overline{z}} \right) dx dy$$
Pull the constant out:
$$\oint_C B(z,\overline{z}) dz = 2i \iint_R \frac{\partial B}{\partial \overline{z}} dx dy$$
**(Proved)**




Here are the detailed solutions for the next four questions (Q241 to Q244).

### Q241. Pg 2, Q3(b): State and prove Cauchy's integral formula.

**Solution:**

**Statement:**
Let $f(z)$ be an analytic function everywhere inside and on a simple closed contour $C$, taken in the positive (counter-clockwise) sense. If $a$ is any interior point within $C$, then the value of the function at $a$ is given by the contour integral:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - a} dz$$

**Proof:**
**Step 1: Isolate the singularity.**
Consider the integrand function $F(z) = \frac{f(z)}{z-a}$. This function is analytic everywhere inside $C$ *except* at the point $z=a$, where the denominator becomes zero.
To use Cauchy's Integral Theorem (which requires analyticity everywhere inside the region), we isolate the singularity. We draw a small circle $C_r$ centered at $a$ with a very small radius $r$, such that $C_r$ lies entirely inside $C$.

**Step 2: Apply the Principle of Deformation of Contours.**
The region between the outer contour $C$ and the inner small circle $C_r$ contains no singularities (since $z=a$ is isolated inside $C_r$). Therefore, by Cauchy's Integral Theorem for multiply connected domains (or deformation of contours), the integral around the outer curve equals the integral around the inner curve:
$$\oint_C \frac{f(z)}{z-a} dz = \oint_{C_r} \frac{f(z)}{z-a} dz$$

**Step 3: Parameterize the small circle $C_r$.**
The equation of the circle $C_r$ is $|z-a| = r$.
In polar form, any point on this circle can be written as $z - a = r e^{i\theta}$, or:
$$z = a + r e^{i\theta} \quad \text{where } 0 \le \theta \le 2\pi$$
The differential $dz$ is:
$$dz = i r e^{i\theta} d\theta$$

**Step 4: Substitute the parameterization into the integral.**
$$\oint_{C_r} \frac{f(z)}{z-a} dz = \int_0^{2\pi} \frac{f(a + r e^{i\theta})}{r e^{i\theta}} (i r e^{i\theta} d\theta)$$
Cancel the $r e^{i\theta}$ terms:
$$= \int_0^{2\pi} f(a + r e^{i\theta}) \cdot i \ d\theta$$
$$= i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta$$

**Step 5: Take the limit as $r \to 0$.**
Because the equality holds for *any* small circle $C_r$ as long as it's inside $C$, it must hold in the limit as the radius shrinks to zero.
$$\oint_C \frac{f(z)}{z-a} dz = \lim_{r \to 0} \left[ i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta \right]$$
Since $f(z)$ is analytic, it is continuous. We can pass the limit inside the integral. As $r \to 0$, the term $r e^{i\theta} \to 0$, so $f(a + r e^{i\theta}) \to f(a)$.
$$= i \int_0^{2\pi} f(a) d\theta$$
Since $f(a)$ is a constant with respect to $\theta$, pull it out of the integral:
$$= i f(a) \int_0^{2\pi} d\theta$$
$$= i f(a) [\theta]_0^{2\pi} = i f(a) (2\pi)$$
$$= 2\pi i f(a)$$

**Step 6: Final rearrangement.**
We established that:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i f(a)$$
Divide both sides by $2\pi i$:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
**(Proved)**

***

### Q242. Pg 2, Q3(c): Evaluate $\oint_c \frac{e^z}{(z^2+\pi^2)^2} dz$ where c is the circle $|z|=4$.

**Solution:**

We will evaluate this integral using the **Generalized Cauchy Integral Formula** (or Cauchy's Residue Theorem).

**Step 1: Identify the function and its singularities.**
The integrand is $F(z) = \frac{e^z}{(z^2+\pi^2)^2}$.
Singularities occur where the denominator is zero:
$$(z^2 + \pi^2)^2 = 0 \implies z^2 = -\pi^2 \implies z = \pm i\pi$$
The singularities are at $z = i\pi$ and $z = -i\pi$.
Because the factor $(z^2+\pi^2)$ is squared, these are **poles of order 2**.

**Step 2: Check which singularities lie inside the contour.**
The contour $C$ is a circle centered at the origin with radius $R = 4$.
We must check if the distances from the origin to the poles are less than 4.
*   $|i\pi| = \pi \approx 3.14159$. Since $3.14 < 4$, the pole $z = i\pi$ is **inside** the contour.
*   $|-i\pi| = \pi \approx 3.14159$. Since $3.14 < 4$, the pole $z = -i\pi$ is **inside** the contour.
Both poles are enclosed.

**Step 3: Calculate the Residues at the poles.**
The formula for the residue at a pole of order $m=2$ at point $a$ is:
$$\text{Res}(F, a) = \lim_{z \to a} \frac{d}{dz} \left[ (z-a)^2 F(z) \right]$$
We rewrite $F(z)$ by factoring the denominator: $F(z) = \frac{e^z}{(z-i\pi)^2(z+i\pi)^2}$.

*   **Residue at $a = i\pi$:**
    $$R_1 = \lim_{z \to i\pi} \frac{d}{dz} \left[ (z-i\pi)^2 \frac{e^z}{(z-i\pi)^2(z+i\pi)^2} \right] = \lim_{z \to i\pi} \frac{d}{dz} \left[ \frac{e^z}{(z+i\pi)^2} \right]$$
    *(Note: This exact limit derivative was solved step-by-step in Q109).*
    Using quotient rule: $\frac{d}{dz}\left(\frac{e^z}{(z+i\pi)^2}\right) = \frac{e^z(z+i\pi-2)}{(z+i\pi)^3}$.
    Evaluate at $z = i\pi$:
    $$R_1 = \frac{e^{i\pi}(i\pi+i\pi-2)}{(i\pi+i\pi)^3} = \frac{-1(2i\pi-2)}{(2i\pi)^3} = \frac{2-2i\pi}{-8i\pi^3} = \frac{1-i\pi}{-4i\pi^3}$$
    Multiply top and bottom by $i$:
    $$R_1 = \frac{i+\pi}{4\pi^3}$$

*   **Residue at $a = -i\pi$:**
    $$R_2 = \lim_{z \to -i\pi} \frac{d}{dz} \left[ (z+i\pi)^2 \frac{e^z}{(z-i\pi)^2(z+i\pi)^2} \right] = \lim_{z \to -i\pi} \frac{d}{dz} \left[ \frac{e^z}{(z-i\pi)^2} \right]$$
    Using quotient rule: $\frac{d}{dz}\left(\frac{e^z}{(z-i\pi)^2}\right) = \frac{e^z(z-i\pi-2)}{(z-i\pi)^3}$.
    Evaluate at $z = -i\pi$:
    $$R_2 = \frac{e^{-i\pi}(-i\pi-i\pi-2)}{(-i\pi-i\pi)^3} = \frac{-1(-2i\pi-2)}{(-2i\pi)^3} = \frac{2+2i\pi}{8i\pi^3} = \frac{1+i\pi}{4i\pi^3}$$
    Multiply top and bottom by $i$:
    $$R_2 = \frac{i-\pi}{-4\pi^3} = \frac{\pi-i}{4\pi^3}$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$\oint_C F(z) dz = 2\pi i (R_1 + R_2)$$
$$\oint_C F(z) dz = 2\pi i \left( \frac{\pi+i}{4\pi^3} + \frac{\pi-i}{4\pi^3} \right)$$
Combine the numerators:
$$\oint_C F(z) dz = 2\pi i \left( \frac{\pi + i + \pi - i}{4\pi^3} \right) = 2\pi i \left( \frac{2\pi}{4\pi^3} \right)$$
$$\oint_C F(z) dz = 2\pi i \left( \frac{1}{2\pi^2} \right) = \frac{2\pi i}{2\pi^2} = \frac{i}{\pi}$$

**Answer:** The value of the integral is **$\frac{i}{\pi}$**.

***

### Q243. Pg 4, Q3(b): Evaluate $\frac{1}{2\pi i}\oint_c \frac{e^{zt}}{z^2+1} dz$, if $t > 0$ and c is the circle $|z|=3$.

**Solution:**

Let $I = \frac{1}{2\pi i}\oint_C \frac{e^{zt}}{z^2+1} dz$. 

**Step 1: Identify the singularities.**
The denominator is zero when $z^2+1 = 0 \implies z = \pm i$.
There are two **simple poles** at $z_1 = i$ and $z_2 = -i$.

**Step 2: Check enclosure.**
The contour $C$ is a circle of radius 3 centered at the origin ($|z|=3$).
*   $|i| = 1 < 3$ (Inside)
*   $|-i| = 1 < 3$ (Inside)
Both poles are enclosed.

**Step 3: Calculate the residues.**
For a simple pole at $a$, the residue is $\lim_{z\to a} (z-a)F(z)$.
Here $F(z) = \frac{e^{zt}}{(z-i)(z+i)}$.

*   **Residue at $z_1 = i$:**
    $$R_1 = \lim_{z \to i} (z-i) \frac{e^{zt}}{(z-i)(z+i)} = \lim_{z \to i} \frac{e^{zt}}{z+i} = \frac{e^{it}}{i+i} = \frac{e^{it}}{2i}$$
*   **Residue at $z_2 = -i$:**
    $$R_2 = \lim_{z \to -i} (z+i) \frac{e^{zt}}{(z-i)(z+i)} = \lim_{z \to -i} \frac{e^{zt}}{z-i} = \frac{e^{-it}}{-i-i} = \frac{e^{-it}}{-2i} = -\frac{e^{-it}}{2i}$$

**Step 4: Apply Cauchy's Residue Theorem.**
The theorem states $\oint_C F(z)dz = 2\pi i \sum \text{Residues}$.
Since our target expression already has $\frac{1}{2\pi i}$ in front of it:
$$I = \frac{1}{2\pi i} [2\pi i (R_1 + R_2)] = R_1 + R_2$$
$$I = \frac{e^{it}}{2i} - \frac{e^{-it}}{2i}$$
$$I = \frac{e^{it} - e^{-it}}{2i}$$

**Step 5: Simplify using trigonometric definitions.**
Euler's formula gives us the definition of the sine function:
$$\sin(t) = \frac{e^{it} - e^{-it}}{2i}$$
Therefore, the result simplifies perfectly to $\sin(t)$.

*(Note: This integral represents the Inverse Laplace Transform of $F(s) = \frac{1}{s^2+1}$ where $s=z$, which yields $\sin(t)$).*

**Answer:** The value of the integral is **$\sin t$**.

***

### Q244. Pg 13, CT-04, 4.(a): Evaluate $\oint_C \frac{e^{iz}}{(z+3)^4} dz$ where C is the circle (i) $|z|=1$ (ii) $|z|=4$

**Solution:**

We evaluate the integral $\oint_C \frac{e^{iz}}{(z+3)^4} dz$ for two different contours using the Generalized Cauchy Integral Formula.

**Step 1: Identify the singularity.**
The function $F(z) = \frac{e^{iz}}{(z+3)^4}$ has a singularity where the denominator is zero:
$(z+3)^4 = 0 \implies z = -3$.
This is a **pole of order 4**.
The analytic numerator part is $f(z) = e^{iz}$.

---
**Part (i): Contour C is $|z|=1$**
1.  **Check enclosure:** The contour is a circle of radius 1 centered at the origin. The pole is at $z = -3$.
    Distance from origin: $|-3| = 3$.
    Since $3 > 1$, the pole $z = -3$ lies strictly **outside** the contour $C$.
2.  **Evaluate:** Because the entire function $F(z)$ is completely analytic everywhere inside and on the contour $|z|=1$ (it has no singularities inside), we apply Cauchy's Integral Theorem.
    **Answer (i): $0$**

---
**Part (ii): Contour C is $|z|=4$**
1.  **Check enclosure:** The contour is a circle of radius 4.
    Distance from origin: $|-3| = 3$.
    Since $3 < 4$, the pole $z = -3$ lies **inside** the contour $C$.
2.  **Apply Generalized Cauchy Integral Formula:**
    The formula for a pole of order $n+1$ at $z=a$ is:
    $$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$
    Here:
    *   $a = -3$
    *   $n+1 = 4 \implies n = 3$. So we need the 3rd derivative.
    *   $f(z) = e^{iz}$

3.  **Calculate the derivatives of $f(z)$:**
    *   $f(z) = e^{iz}$
    *   $f'(z) = i e^{iz}$
    *   $f''(z) = i^2 e^{iz} = -e^{iz}$
    *   $f'''(z) = -i e^{iz}$
4.  **Evaluate the 3rd derivative at the pole $a = -3$:**
    $$f'''(-3) = -i e^{i(-3)} = -i e^{-3i}$$
5.  **Substitute into the formula:**
    $$\oint_C \frac{e^{iz}}{(z+3)^4} dz = \frac{2\pi i}{3!} (-i e^{-3i})$$
    Since $3! = 3 \times 2 \times 1 = 6$:
    $$= \frac{2\pi i}{6} (-i e^{-3i})$$
    $$= \frac{\pi i}{3} (-i e^{-3i})$$
    $$= \frac{-\pi i^2 e^{-3i}}{3}$$
    Since $i^2 = -1$:
    $$= \frac{\pi e^{-3i}}{3}$$

**Answer (ii): $\frac{\pi e^{-3i}}{3}$** *(or $\frac{\pi}{3}(\cos 3 - i\sin 3)$)*.

Here are the detailed solutions for the next four questions (Q245 to Q248).

### Q245. Pg 13, CT-04, 4.(b): Evaluate $\oint_C \frac{3z^2+z}{z^2-1} dz$ where C is the circle $|z-1|=1$

*(Note: This is identically stated in Q296).*

**Solution:**

Let $I = \oint_C \frac{3z^2+z}{z^2-1} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero:
$$z^2 - 1 = 0 \implies (z-1)(z+1) = 0$$
There are two simple poles: $z_1 = 1$ and $z_2 = -1$.

**Step 2: Check which poles lie inside the contour $C$.**
The contour $C$ is a circle given by $|z-1| = 1$. This is a circle centered at $1$ with a radius of $1$.
*   **Test $z_1 = 1$:** $|1 - 1| = 0 < 1$. This pole is exactly at the center, so it is **inside** $C$.
*   **Test $z_2 = -1$:** $|-1 - 1| = |-2| = 2$. Since $2 > 1$, this pole lies strictly **outside** $C$.

**Step 3: Apply Cauchy's Integral Formula.**
Because only $z=1$ is inside the contour, we can rewrite the integral to isolate this singularity in the denominator. The remaining parts of the function will be analytic inside $C$.
$$I = \oint_C \frac{3z^2+z}{(z-1)(z+1)} dz = \oint_C \frac{ \left( \frac{3z^2+z}{z+1} \right) }{z-1} dz$$
Let the analytic numerator function be $f(z) = \frac{3z^2+z}{z+1}$.
According to Cauchy's Integral Formula:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 1$.

**Step 4: Evaluate the formula.**
Calculate $f(1)$:
$$f(1) = \frac{3(1)^2 + 1}{1 + 1} = \frac{3 + 1}{2} = \frac{4}{2} = 2$$

Multiply by $2\pi i$:
$$I = 2\pi i \cdot f(1) = 2\pi i \cdot 2 = 4\pi i$$

**Answer:** The value of the integral is **$4\pi i$**.

***

### Q246. Pg 15, CT-04, 3.(a): Evaluate $\oint_C \frac{z^2+1}{z^2-1} dz$ where C is the circle $|z-1|=1$

**Solution:**

Let $I = \oint_C \frac{z^2+1}{z^2-1} dz$.

**Step 1: Identify singularities and check enclosure.**
The denominator factors to $(z-1)(z+1)$, giving simple poles at $z=1$ and $z=-1$.
The contour $C$ is $|z-1| = 1$ (center at $z=1$, radius $1$).
*   $z=1$ is **inside** ($|1-1|=0<1$).
*   $z=-1$ is **outside** ($|-1-1|=2>1$).

**Step 2: Apply Cauchy's Integral Formula.**
Rewrite the integral to isolate the enclosed singularity $z=1$:
$$I = \oint_C \frac{ \left( \frac{z^2+1}{z+1} \right) }{z-1} dz$$
Let $f(z) = \frac{z^2+1}{z+1}$. This function is analytic inside and on $C$.
The formula is:
$$I = 2\pi i \cdot f(1)$$

**Step 3: Evaluate $f(1)$.**
$$f(1) = \frac{(1)^2 + 1}{1 + 1} = \frac{2}{2} = 1$$

**Step 4: Calculate final result.**
$$I = 2\pi i \cdot 1 = 2\pi i$$

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q247. Pg 15, CT-04, 3.(b): Evaluate $\oint_C \frac{z^2}{(z-1)(z+2)^2} dz$ where C is the circle $|z|=3$

**Solution:**

Let $I = \oint_C \frac{z^2}{(z-1)(z+2)^2} dz$.

**Step 1: Identify singularities.**
The denominator is zero at:
*   $z_1 = 1$ (Simple pole, order 1)
*   $z_2 = -2$ (Pole of order 2)

**Step 2: Check enclosure.**
The contour $C$ is $|z|=3$ (circle centered at origin, radius 3).
*   $|1| = 1 < 3$ (**Inside**)
*   $|-2| = 2 < 3$ (**Inside**)
Both poles are enclosed by the contour. We will use the Residue Theorem: $I = 2\pi i \sum \text{Residues}$.

**Step 3: Calculate Residue at $z_1 = 1$ (Simple Pole).**
For a simple pole at $a$: $\text{Res}(a) = \lim_{z\to a} (z-a)F(z)$.
$$R_1 = \lim_{z \to 1} (z-1) \frac{z^2}{(z-1)(z+2)^2} = \lim_{z \to 1} \frac{z^2}{(z+2)^2}$$
Substitute $z=1$:
$$R_1 = \frac{1^2}{(1+2)^2} = \frac{1}{3^2} = \frac{1}{9}$$

**Step 4: Calculate Residue at $z_2 = -2$ (Pole of order 2).**
For a pole of order $m=2$ at $a$: $\text{Res}(a) = \lim_{z\to a} \frac{d}{dz} \left[ (z-a)^2 F(z) \right]$.
$$R_2 = \lim_{z \to -2} \frac{d}{dz} \left[ (z+2)^2 \frac{z^2}{(z-1)(z+2)^2} \right] = \lim_{z \to -2} \frac{d}{dz} \left( \frac{z^2}{z-1} \right)$$
Use the quotient rule to differentiate $\frac{z^2}{z-1}$:
$$ \frac{d}{dz} \left( \frac{z^2}{z-1} \right) = \frac{(2z)(z-1) - (z^2)(1)}{(z-1)^2} = \frac{2z^2 - 2z - z^2}{(z-1)^2} = \frac{z^2 - 2z}{(z-1)^2}$$
Now evaluate this limit as $z \to -2$:
$$R_2 = \frac{(-2)^2 - 2(-2)}{(-2 - 1)^2} = \frac{4 + 4}{(-3)^2} = \frac{8}{9}$$

**Step 5: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i \left( \frac{1}{9} + \frac{8}{9} \right) = 2\pi i \left( \frac{9}{9} \right) = 2\pi i (1)$$
$$I = 2\pi i$$

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q248. Problem 4.4.1: Prove that, (i) $\oint_C dz=0$ (ii) $\oint_C z dz=0$ (iii) $\oint_C (z-z_0)dz=0$ where C is simple closed curve & $z_0$ is constant.

*(Note: This is identical to Q281).*

**Solution:**

We can prove all three parts simultaneously using **Cauchy's Integral Theorem**.

**Theorem Statement Review:**
Cauchy's Integral Theorem states that if a function $f(z)$ is analytic everywhere inside and on a simple closed contour $C$, then $\oint_C f(z) dz = 0$.

**Proof for (i): $\oint_C dz=0$**
1.  The integrand is $f(z) = 1$.
2.  The constant function $f(z) = 1$ is a polynomial of degree 0. All polynomials are entire functions, meaning they are analytic everywhere in the complex plane.
3.  Since $f(z)=1$ is analytic everywhere inside and on $C$, by Cauchy's Integral Theorem, its integral around $C$ is strictly zero.
$$\oint_C 1 dz = 0$$ **(Proved)**

**Proof for (ii): $\oint_C z dz=0$**
1.  The integrand is $f(z) = z$.
2.  The function $f(z) = z$ is a polynomial of degree 1. It is an entire function, analytic everywhere in the complex plane.
3.  Since $f(z)=z$ is analytic everywhere inside and on $C$, by Cauchy's Integral Theorem, its integral around $C$ is strictly zero.
$$\oint_C z dz = 0$$ **(Proved)**

**Proof for (iii): $\oint_C (z-z_0)dz=0$**
1.  The integrand is $f(z) = z - z_0$.
2.  Since $z_0$ is a constant, this function is a polynomial of degree 1. It is an entire function, analytic everywhere in the complex plane.
3.  Since $f(z)=z-z_0$ is analytic everywhere inside and on $C$, by Cauchy's Integral Theorem, its integral around $C$ is strictly zero.
$$\oint_C (z-z_0) dz = 0$$ **(Proved)**

*(Alternative Proof Method via Fundamental Theorem: All three functions have analytic antiderivatives: $z$, $z^2/2$, and $(z-z_0)^2/2$ respectively. For any closed curve, the start point equals the end point ($z_{start} = z_{end}$). The integral evaluates to $F(z_{end}) - F(z_{start}) = 0$).*
Here are the detailed solutions for the next four questions (Q249 to Q252).

### Q249. 4.4.3: Evaluate $\oint_C \frac{dz}{z-a}$ where is any simple closed curve C and $z=a$ is (i) outside (ii) Inside

*(Note: This is numerically identical to Q283 and conceptually similar to Q267).*

**Solution:**

We need to evaluate the fundamental contour integral $I = \oint_C \frac{1}{z-a} dz$.

**Part (i): Evaluate if $z = a$ is OUTSIDE $C$**
**Step 1: Check analyticity.**
The integrand $f(z) = \frac{1}{z-a}$ has a single point of singularity (a simple pole) at $z = a$. Everywhere else, it is completely analytic.
Because the point $z = a$ lies strictly *outside* the simple closed curve $C$, the function has no singularities anywhere inside or on $C$.
**Step 2: Apply Cauchy's Integral Theorem.**
Cauchy's Integral Theorem states that if a function is analytic everywhere inside and on a closed contour, its integral around that contour is exactly zero.
Therefore:
**Answer (i): $0$**

---

**Part (ii): Evaluate if $z = a$ is INSIDE $C$**
**Method 1: Using Cauchy's Integral Formula (Fastest)**
The formula states $\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$.
Here, the numerator function is the constant $f(z) = 1$, which is analytic everywhere.
Because $z=a$ is inside $C$, we apply the formula:
$$I = 2\pi i \cdot f(a) = 2\pi i \cdot 1 = 2\pi i$$

**Method 2: Direct Parameterization (Formal Proof Method)**
To prove this rigorously without invoking the formula we are trying to establish, we use the Principle of Deformation of Contours.
1.  Draw a small circle $C_r$ centered at $z=a$ with a very small radius $r$, such that it lies entirely inside $C$.
2.  Because the region between $C$ and $C_r$ is analytic, $\oint_C \frac{dz}{z-a} = \oint_{C_r} \frac{dz}{z-a}$.
3.  Parameterize the small circle $C_r$: $z - a = r e^{i\theta}$ where $\theta$ goes from $0$ to $2\pi$.
    $dz = ir e^{i\theta} d\theta$.
4.  Substitute into the integral:
    $$\oint_{C_r} \frac{dz}{z-a} = \int_0^{2\pi} \frac{ir e^{i\theta} d\theta}{r e^{i\theta}}$$
5.  The $r e^{i\theta}$ terms cancel out completely:
    $$= \int_0^{2\pi} i \ d\theta = i[\theta]_0^{2\pi} = i(2\pi - 0) = 2\pi i$$
**Answer (ii): $2\pi i$**

***

### Q250. Prblm-4.4.4: Find the value of $\oint_C (z^2+2z+1)dz$ where C is the circle $\vert{}z\vert{}=1$

*(Note: This is identically stated in Q284).*

**Solution:**

We must evaluate the complex line integral $I = \oint_C (z^2+2z+1)dz$ around the unit circle $|z|=1$.

**Step 1: Analyze the integrand.**
The function $f(z) = z^2 + 2z + 1$ is a polynomial.
A fundamental property of complex analysis is that all polynomial functions are **entire functions**, meaning they are analytic (infinitely differentiable and continuous) everywhere in the complex plane. They possess no singularities, poles, or undefined points.

**Step 2: Apply the relevant theorem.**
Cauchy's Integral Theorem states that if a function $f(z)$ is analytic everywhere inside and on a simple closed contour $C$, then:
$$\oint_C f(z) dz = 0$$

Since $f(z) = z^2+2z+1$ is analytic everywhere, it is naturally analytic inside and on the boundary of the unit circle $|z|=1$.

Therefore, by direct application of Cauchy's Integral Theorem, the integral evaluates to zero.

*(Alternative Method: Use the Fundamental Theorem. The antiderivative is $F(z) = z^3/3 + z^2 + z$. Because the path is a closed loop, the start point equals the end point, so $F(z_{end}) - F(z_{start}) = 0$).*

**Answer:** **$0$**

***

### Q251. Prblm-4.4.5: Evaluate $\oint_C \frac{dz}{2z-3}$ where c is $\vert{}z\vert{}=1$

*(Note: This is identically stated in Q285).*

**Solution:**

We need to evaluate $I = \oint_C \frac{1}{2z-3} dz$ around the unit circle.

**Step 1: Identify the singularity.**
Set the denominator to zero to find the pole:
$$2z - 3 = 0 \implies 2z = 3 \implies z = \frac{3}{2} = 1.5$$
The function has a simple pole at $z = 1.5$.

**Step 2: Check if the singularity is enclosed by the contour.**
The contour $C$ is defined by $|z| = 1$, which is a circle centered at the origin with a radius of $1$.
The pole is located at $z = 1.5$.
Since $|1.5| = 1.5$, and $1.5 > 1$, the pole lies strictly **outside** the contour $C$.

**Step 3: Apply the relevant theorem.**
Because the only singularity of the function lies completely outside the contour, the function $f(z) = \frac{1}{2z-3}$ is completely analytic everywhere inside and on the boundary of the contour $C$.

According to Cauchy's Integral Theorem, the contour integral of an analytic function around a closed path is exactly zero.

**Answer:** **$0$**

***

### Q252. Prblm 4.4.6: Evaluate $\frac{1}{2\pi i}\oint_C \frac{e^z}{z-2}dz$ where c is $\vert{}z\vert{}=1$

*(Note: This is identically stated in Q286).*

**Solution:**

We evaluate the integral expression $I = \frac{1}{2\pi i}\oint_C \frac{e^z}{z-2} dz$ over the unit circle.

**Step 1: Identify the singularity.**
The integrand function is $F(z) = \frac{e^z}{z-2}$.
The denominator becomes zero at $z = 2$.
Therefore, there is a simple pole at $z = 2$.

**Step 2: Check if the singularity is enclosed by the contour.**
The contour $C$ is the unit circle, defined by $|z| = 1$.
The distance of the pole from the origin is $|2| = 2$.
Since $2 > 1$, the pole $z = 2$ lies strictly **outside** the contour $C$.

**Step 3: Apply the relevant theorem.**
Because the only singularity lies outside the contour, the entire integrand $F(z) = \frac{e^z}{z-2}$ is analytic everywhere inside and on the simple closed curve $C$.

By Cauchy's Integral Theorem, the integral of any analytic function around a closed contour is zero:
$$\oint_C \frac{e^z}{z-2} dz = 0$$

Therefore, the full expression evaluates to:
$$I = \frac{1}{2\pi i} (0) = 0$$

*(Note: If the contour had been, for example, $|z|=3$, the pole would be inside, and we would use Cauchy's Integral Formula to get $\frac{1}{2\pi i} [2\pi i \cdot e^2] = e^2$. But since it's outside, the result is 0).*

**Answer:** **$0$**

Here are the detailed solutions for the next four questions (Q253 to Q256).

### Q253. Prblm 4.4.7: Evaluate $\oint_C \frac{dz}{(z-a)^n}$, $n=1,2,3$ Where $z=a$ is inside the curve C

*(Note: This is identically stated in Q287, though Q287 specifies $n=2,3,4\dots$. Evaluating for a general integer $n$ is standard, and we will evaluate specifically for $n=1$, and then for $n \ge 2$).*

**Solution:**

We need to evaluate the contour integral $I_n = \oint_C \frac{1}{(z-a)^n} dz$ where $C$ is a simple closed curve enclosing the point $a$.

**Case 1: When $n = 1$**
The integral is $\oint_C \frac{1}{z-a} dz$.
We evaluated this exactly in **Q249 Part (ii)**.
Using Cauchy's Integral Formula: $\oint_C \frac{f(z)}{z-a} dz = 2\pi i f(a)$.
Here, $f(z) = 1$. Since $a$ is inside the contour:
$$I_1 = 2\pi i (1) = 2\pi i$$

**Case 2: When $n \ge 2$ (e.g., $n=2, 3, 4\dots$)**
The integral is $\oint_C \frac{1}{(z-a)^n} dz$.
Because $a$ is inside the contour, this is a pole of order $n$. We must use the **Generalized Cauchy Integral Formula** for higher-order poles:
$$\oint_C \frac{f(z)}{(z-a)^{m+1}} dz = \frac{2\pi i}{m!} f^{(m)}(a)$$

To match our integral's format with the formula, let:
*   Numerator function: $f(z) = 1$ (analytic everywhere).
*   Power matching: $m + 1 = n \implies m = n - 1$.
Because $n \ge 2$, $m$ is a positive integer ($m \ge 1$).

We need the $m$-th derivative of the numerator $f(z)$.
Since $f(z) = 1$ is a constant, its first derivative is zero: $f'(z) = 0$.
Consequently, all subsequent higher-order derivatives are also zero.
$$f^{(m)}(z) = 0 \quad \text{for all } m \ge 1$$

Therefore, evaluating the $m$-th derivative at the point $a$:
$$f^{(m)}(a) = 0$$

Substitute this into the Generalized Formula:
$$I_n = \frac{2\pi i}{(n-1)!} \cdot 0$$
$$I_n = 0$$

*(Alternative proof via parameterization: Deform contour to a circle $z-a=re^{i\theta}, dz=ire^{i\theta}d\theta$. $\int_0^{2\pi} \frac{ire^{i\theta}}{r^ne^{in\theta}}d\theta = ir^{1-n} \int_0^{2\pi} e^{i(1-n)\theta}d\theta = ir^{1-n} \left[ \frac{e^{i(1-n)\theta}}{i(1-n)} \right]_0^{2\pi} = \frac{r^{1-n}}{1-n}(1 - 1) = 0$. Valid for any integer $n \neq 1$).*

**Answer:** 
*   For **$n = 1$**, the integral evaluates to **$2\pi i$**.
*   For **$n \ge 2$** (e.g., $n=2,3$), the integral evaluates to **$0$**.

***

### Q254. 5.1 Cauchy's Integration Formula: prove that $f(a)=\frac{1}{2\pi i}\oint_C \frac{f(z)}{z-a}dz$

*(Note: This is identically proven in Q241 and corresponds to Q289. The formal proof is restated below).*

**Solution:**

**Theorem Statement:** If $f(z)$ is analytic everywhere inside and on a simple closed contour $C$, and $a$ is any point interior to $C$, then $f(a) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{z-a}dz$.

**Proof:**
1.  **Isolate the singularity:** The integrand $\frac{f(z)}{z-a}$ is analytic everywhere inside $C$ except at $z=a$. Construct a small circle $C_r$ centered at $a$ with radius $r$, lying entirely inside $C$.
2.  **Deformation of contours:** By the principle of deformation (an extension of Cauchy's Integral Theorem for multiply connected domains), the integral over the outer boundary equals the integral over the inner boundary because the region between them is analytic.
    $$\oint_C \frac{f(z)}{z-a} dz = \oint_{C_r} \frac{f(z)}{z-a} dz$$
3.  **Parameterize the small circle:** For $C_r$, the equation is $|z-a| = r$. In exponential form, $z - a = r e^{i\theta}$, so $z = a + r e^{i\theta}$ where $\theta \in [0, 2\pi]$. The differential is $dz = ir e^{i\theta} d\theta$.
4.  **Substitute into the integral:**
    $$\oint_{C_r} \frac{f(z)}{z-a} dz = \int_0^{2\pi} \frac{f(a + r e^{i\theta})}{r e^{i\theta}} (ir e^{i\theta} d\theta)$$
    Cancel the common $re^{i\theta}$ terms:
    $$= i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta$$
5.  **Evaluate the limit as $r \to 0$:** Because this relation holds for any arbitrary radius $r > 0$, it must hold in the limit as $r$ approaches zero.
    $$\oint_C \frac{f(z)}{z-a} dz = \lim_{r \to 0} \left[ i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta \right]$$
    Since $f(z)$ is analytic, it is continuous, so the limit can be passed inside. As $r \to 0$, $r e^{i\theta} \to 0$, making $f(a+re^{i\theta}) \to f(a)$.
    $$= i \int_0^{2\pi} f(a) d\theta$$
6.  **Evaluate the final integral:** Since $f(a)$ acts as a constant with respect to $\theta$:
    $$= i f(a) \int_0^{2\pi} d\theta = i f(a) [\theta]_0^{2\pi} = 2\pi i f(a)$$
7.  **Rearrange:** We have $\oint_C \frac{f(z)}{z-a} dz = 2\pi i f(a)$. Divide by $2\pi i$:
    $$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
**(Proved)**

***

### Q255. Prblm 5.1.1: Evaluate $\oint_C \frac{e^z}{z-2}dz$, where C is the circle (i) $\vert{}z\vert{}=3$ (ii) $\vert{}z\vert{}=1$

*(Note: Part (ii) was identically solved in Q252 and Q286. Part (i) evaluates when the pole is inside).*

**Solution:**

We must evaluate $I = \oint_C \frac{e^z}{z-2} dz$.

**Step 1: Identify the singularity.**
The integrand $F(z) = \frac{e^z}{z-2}$ has a zero in the denominator at $z-2 = 0 \implies z = 2$.
This is a simple pole at $z=2$. The numerator $f(z) = e^z$ is analytic everywhere.

---
**Part (i): Contour is $|z| = 3$**
1.  **Check enclosure:** The contour is a circle of radius 3 centered at the origin.
    The distance to the pole is $|2| = 2$.
    Since $2 < 3$, the pole is strictly **inside** the contour.
2.  **Apply Cauchy's Integral Formula:** 
    The formula is $\oint_C \frac{f(z)}{z-a} dz = 2\pi i f(a)$.
    Here, $a = 2$ and $f(z) = e^z$.
    $$I_1 = 2\pi i \cdot f(2)$$
    $$I_1 = 2\pi i \cdot e^2$$
**Answer (i): $2\pi i e^2$**

---
**Part (ii): Contour is $|z| = 1$**
1.  **Check enclosure:** The contour is a circle of radius 1 centered at the origin.
    The distance to the pole is $|2| = 2$.
    Since $2 > 1$, the pole is strictly **outside** the contour.
2.  **Apply Cauchy's Integral Theorem:**
    Because the only singularity lies outside $C$, the entire function $F(z) = \frac{e^z}{z-2}$ is analytic everywhere inside and on the contour $C$.
    By Cauchy's Integral Theorem, the integral of an analytic function around a closed path is zero.
    $$I_2 = 0$$
**Answer (ii): $0$**

***

### Q256. Prblm-5.1.2: Evaluate $\oint_C \frac{e^{2z}}{(z+1)^4}dz$ , where c is the circle $\vert{}z\vert{}=3$

*(Note: This is identically stated in Q292).*

**Solution:**

We need to evaluate $I = \oint_C \frac{e^{2z}}{(z+1)^4} dz$.

**Step 1: Identify the singularity and analytic numerator.**
Set the denominator to zero:
$$(z+1)^4 = 0 \implies z = -1$$
There is a **pole of order 4** at $z = -1$.
The numerator function is $f(z) = e^{2z}$, which is an entire function (analytic everywhere).

**Step 2: Check enclosure.**
The contour $C$ is defined by $|z| = 3$, a circle of radius 3.
The distance to the pole is $|-1| = 1$.
Since $1 < 3$, the pole lies **inside** the contour.

**Step 3: Apply the Generalized Cauchy Integral Formula.**
The formula for higher-order poles is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map the parameters:
*   $a = -1$
*   $n+1 = 4 \implies n = 3$. We need to find the third derivative.
*   $f(z) = e^{2z}$

**Step 4: Calculate the derivatives.**
We need the 3rd derivative of $f(z)$:
*   $f(z) = e^{2z}$
*   $f'(z) = 2e^{2z}$
*   $f''(z) = 4e^{2z}$
*   $f'''(z) = 8e^{2z}$

**Step 5: Evaluate the formula.**
Calculate $f'''(a)$ at $a = -1$:
$$f'''(-1) = 8e^{2(-1)} = 8e^{-2}$$

Substitute this back into the generalized formula:
$$I = \frac{2\pi i}{3!} f'''(-1)$$
$$I = \frac{2\pi i}{3 \times 2 \times 1} \left( 8e^{-2} \right)$$
$$I = \frac{2\pi i}{6} \left( 8e^{-2} \right)$$
$$I = \frac{\pi i}{3} \left( 8e^{-2} \right)$$
$$I = \frac{8\pi i e^{-2}}{3}$$

**Answer:** The value of the integral is **$\frac{8\pi i}{3e^2}$** (or **$\frac{8\pi i e^{-2}}{3}$**).
Here are the detailed solutions for the next four questions (Q257 to Q260).

### Q257. Prblm 5.1.3: Evaluate $\oint_C \frac{e^{iz}}{z^3}dz$ where C is the circle $\vert{}z\vert{}=2$

*(Note: This is identically stated in Q293).*

**Solution:**

We must evaluate the contour integral $I = \oint_C \frac{e^{iz}}{z^3} dz$.

**Step 1: Identify the singularity and analytic numerator.**
Set the denominator to zero to find the singularity:
$$z^3 = 0 \implies z = 0$$
This is a **pole of order 3** at the origin ($z=0$).
The numerator function is $f(z) = e^{iz}$, which is an entire function (analytic everywhere).

**Step 2: Check enclosure.**
The contour $C$ is a circle of radius 2 centered at the origin ($|z|=2$).
The pole is exactly at the origin ($z=0$).
Since $|0| = 0 < 2$, the pole lies safely **inside** the contour.

**Step 3: Apply the Generalized Cauchy Integral Formula.**
For a pole of order $n+1$, the formula is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map our problem's parameters to the formula:
*   $a = 0$
*   $n+1 = 3 \implies n = 2$. We need the second derivative.
*   $f(z) = e^{iz}$

**Step 4: Calculate the derivatives.**
We need the second derivative of $f(z)$:
*   $f(z) = e^{iz}$
*   $f'(z) = i e^{iz}$
*   $f''(z) = i^2 e^{iz} = -e^{iz}$

**Step 5: Evaluate the formula.**
Calculate $f''(a)$ at $a = 0$:
$$f''(0) = -e^{i(0)} = -e^0 = -1$$

Substitute this back into the generalized formula:
$$I = \frac{2\pi i}{2!} f''(0)$$
$$I = \frac{2\pi i}{2 \times 1} (-1)$$
$$I = \frac{2\pi i}{2} (-1)$$
$$I = -\pi i$$

**Answer:** The value of the integral is **$-\pi i$**.

***

### Q258. Prblm 5.1.4: Evaluate $\oint \frac{1}{z(z-2)^4}dz$ where C is the circle $\vert{}z\vert{}=1$

*(Note: This is identically stated in Q294).*

**Solution:**

Let $I = \oint_C \frac{1}{z(z-2)^4} dz$.

**Step 1: Identify all singularities.**
Set the denominator to zero:
$$z(z-2)^4 = 0$$
This yields two singular points:
1.  $z_1 = 0$ (a simple pole, order 1).
2.  $z_2 = 2$ (a pole of order 4).

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is defined by $|z|=1$, a circle of radius 1 centered at the origin.
*   **Test $z_1 = 0$:** $|0| = 0 < 1$. This pole lies **inside** the contour.
*   **Test $z_2 = 2$:** $|2| = 2 > 1$. This pole lies strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_1 = 0$ is enclosed by the contour, we must rewrite the integrand so that the "outside" singularity is absorbed into the analytic numerator function. 
$$I = \oint_C \frac{\left( \frac{1}{(z-2)^4} \right)}{z} dz$$
Let the analytic numerator function be $f(z) = \frac{1}{(z-2)^4}$. 
This function $f(z)$ is analytic everywhere *inside and on* the contour $|z|=1$ because its only singularity ($z=2$) is outside.

**Step 4: Apply Cauchy's Integral Formula.**
Since the enclosed pole is simple (order 1), we use the standard formula:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 0$.

**Step 5: Evaluate.**
Calculate $f(0)$:
$$f(0) = \frac{1}{(0-2)^4} = \frac{1}{(-2)^4} = \frac{1}{16}$$

Substitute into the formula:
$$I = 2\pi i \cdot f(0)$$
$$I = 2\pi i \left( \frac{1}{16} \right) = \frac{2\pi i}{16}$$
$$I = \frac{\pi i}{8}$$

**Answer:** The value of the integral is **$\frac{\pi i}{8}$**.

***

### Q259. Prblm 5.1.5: Evaluate $\oint_C \frac{(z+4)}{(z^2+2z+5)}dz$ where C is the circle $\vert{}z+1-i\vert{}=2$

*(Note: This is identically stated in Q295. Q262 is a variant of this problem with a different contour).*

**Solution:**

Let $I = \oint_C \frac{z+4}{z^2+2z+5} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator $z^2+2z+5 = 0$. Use the quadratic formula:
$$z = \frac{-2 \pm \sqrt{2^2 - 4(1)(5)}}{2}$$
$$z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2}$$
$$z = \frac{-2 \pm 4i}{2} = -1 \pm 2i$$
There are two simple poles:
1.  $z_1 = -1 + 2i$
2.  $z_2 = -1 - 2i$

The factored denominator is $(z - (-1+2i))(z - (-1-2i))$.

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is $|z+1-i| = 2$.
Rewrite in standard form: $|z - (-1+i)| = 2$. This is a circle centered at $-1+i$ with radius $2$.

*   **Test $z_1 = -1 + 2i$:**
    Substitute into the contour equation's left side:
    $$|(-1 + 2i) - (-1 + i)| = |-1 + 2i + 1 - i| = |i| = 1$$
    Since $1 < 2$, the pole $z_1 = -1+2i$ is **inside** the contour.

*   **Test $z_2 = -1 - 2i$:**
    Substitute into the contour equation's left side:
    $$|(-1 - 2i) - (-1 + i)| = |-1 - 2i + 1 - i| = |-3i| = 3$$
    Since $3 > 2$, the pole $z_2 = -1-2i$ is strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Only $z_1 = -1+2i$ is enclosed. Isolate it in the denominator and push the rest of the function into the numerator:
$$I = \oint_C \frac{\left( \frac{z+4}{z - (-1-2i)} \right)}{z - (-1+2i)} dz$$
Let the analytic numerator function be $f(z) = \frac{z+4}{z+1+2i}$.

**Step 4: Apply Cauchy's Integral Formula.**
$$I = 2\pi i \cdot f(-1+2i)$$

Calculate $f(-1+2i)$:
$$f(-1+2i) = \frac{(-1+2i) + 4}{(-1+2i) + 1 + 2i}$$
$$f(-1+2i) = \frac{3 + 2i}{4i}$$

**Step 5: Final calculation.**
Multiply by $2\pi i$:
$$I = 2\pi i \left( \frac{3 + 2i}{4i} \right)$$
The $i$ terms cancel, and the $2/4$ reduces to $1/2$:
$$I = \frac{2\pi(3 + 2i)}{4}$$
$$I = \frac{\pi(3 + 2i)}{2}$$
$$I = \frac{3\pi}{2} + \pi i$$

**Answer:** The value of the integral is **$\frac{\pi}{2}(3 + 2i)$** (or **$\frac{3\pi}{2} + \pi i$**).

***

### Q260. Example: Evaluate $\int(z-a)^{n}dz$ where c is the circle with centre a and r. Discuss the case when $n=-1$.

**Solution:**

We need to evaluate the contour integral $I_n = \oint_C (z-a)^n dz$ where $n$ is any integer ($\dots, -2, -1, 0, 1, 2, \dots$) and $C$ is a circle of radius $r$ centered at $a$.

**Step 1: Parameterize the contour $C$.**
The standard parameterization of a circle $|z-a|=r$ is:
$$z - a = r e^{i\theta} \implies z = a + r e^{i\theta}$$
where $\theta$ goes from $0$ to $2\pi$.
The differential $dz$ is:
$$dz = \frac{d}{d\theta}(a + r e^{i\theta}) d\theta = ire^{i\theta} d\theta$$

**Step 2: Substitute into the integral.**
$$I_n = \int_0^{2\pi} (r e^{i\theta})^n (ire^{i\theta} d\theta)$$
$$I_n = \int_0^{2\pi} r^n e^{in\theta} \cdot ir e^{i\theta} d\theta$$
Combine terms using exponent rules:
$$I_n = \int_0^{2\pi} i \cdot r^{n+1} \cdot e^{i(n+1)\theta} d\theta$$

Since $i$ and $r$ are constants with respect to $\theta$, pull them out:
$$I_n = ir^{n+1} \int_0^{2\pi} e^{i(n+1)\theta} d\theta$$

**Step 3: Discuss and evaluate cases based on the value of $n$.**

**Case 1: $n = -1$ (The special requested case)**
Substitute $n = -1$ into the integral expression:
$$I_{-1} = ir^{-1+1} \int_0^{2\pi} e^{i(-1+1)\theta} d\theta$$
$$I_{-1} = ir^0 \int_0^{2\pi} e^{i(0)\theta} d\theta$$
$$I_{-1} = i(1) \int_0^{2\pi} 1 d\theta$$
$$I_{-1} = i [\theta]_0^{2\pi} = i(2\pi - 0) = 2\pi i$$
This is the fundamental building block of the residue theorem. The integral of $1/(z-a)$ around a pole is always $2\pi i$, regardless of the radius $r$.

**Case 2: Any integer $n \neq -1$**
For any other integer (e.g., $n = -2, 0, 1, 2, \dots$), the coefficient $n+1$ in the exponent is a non-zero integer. Let $k = n+1$ (where $k \neq 0$).
$$I_n = ir^k \int_0^{2\pi} e^{ik\theta} d\theta$$
Evaluate the integral:
$$I_n = ir^k \left[ \frac{e^{ik\theta}}{ik} \right]_0^{2\pi}$$
Cancel the $i$:
$$I_n = \frac{r^k}{k} \left( e^{ik(2\pi)} - e^{ik(0)} \right)$$
$$I_n = \frac{r^k}{k} \left( e^{i2k\pi} - e^0 \right)$$
Because $k$ is an integer, $e^{i2k\pi} = \cos(2k\pi) + i\sin(2k\pi) = 1 + i(0) = 1$. Also, $e^0 = 1$.
$$I_n = \frac{r^k}{k} (1 - 1) = \frac{r^k}{k} (0) = 0$$

**(Mathematical sanity check: If $n \ge 0$, the function $(z-a)^n$ is an analytic polynomial, so Cauchy's Theorem dictates the integral is 0. If $n \le -2$, it's a pole of order $|n|$ with a derivative evaluation $f^{(m)}(a) = 0$ as proven in Q253, so the integral is 0. The only non-zero case is $n=-1$).**

**Answer/Discussion Summary:**
*   For **$n = -1$**, the integral evaluates to **$2\pi i$**. This proves that the contour integral of $1/(z-a)$ encloses a residue of 1, forming the core of Cauchy's Integral Formula.
*   For all other integers **$n \neq -1$**, the integral evaluates to **$0$**.
Here are the detailed solutions for the next four questions (Q261 to Q264).

### Q261. Question: Home work: For the region prove that $\int_{c_{1}}f(z)dz=\int_{c_{2}}f(z)dz+\int_{c_{3}}f(z)dz+\int_{c_{4}}f(z)dz$

*(Note: Without the accompanying figure, I must reconstruct the standard topological theorem this question refers to. The equation describes the **Principle of Deformation of Contours** for a multiply connected domain. It implies $C_1$ is an outer bounding contour, and $C_2, C_3, C_4$ are non-overlapping inner "hole" contours entirely contained within $C_1$. All contours are traversed in the standard positive (counter-clockwise) direction, and $f(z)$ is analytic everywhere in the region between $C_1$ and the inner contours).*

**Solution:**

**Step 1: Define the region and orientation.**
Let $R$ be a multiply connected region (a region with "holes"). 
Let $C_1$ be the outer boundary of $R$, traversed in the positive (counter-clockwise) direction.
Let $C_2, C_3,$ and $C_4$ be the boundaries of the "holes" inside $R$, also traversed in the counter-clockwise direction.
We assume $f(z)$ is analytic everywhere in the shaded region $R$ between the outer curve $C_1$ and the inner curves $C_2, C_3, C_4$.

**Step 2: Construct "cross-cuts" to make the region simply connected.**
Cauchy's Integral Theorem ($\oint f(z)dz = 0$) only applies to *simply connected* domains (regions with no holes).
To apply it, we introduce artificial straight-line segments called "cross-cuts" connecting the contours:
*   Draw cut $L_2$ from $C_1$ to $C_2$.
*   Draw cut $L_3$ from $C_1$ to $C_3$.
*   Draw cut $L_4$ from $C_1$ to $C_4$.

Imagine traversing a new single, continuous master contour $\Gamma$ that traces the entire boundary of the region $R$ without ever leaving it or crossing a hole. 
To keep the region $R$ to the "left" of our path, we must traverse:
*   The outer contour $C_1$ counter-clockwise.
*   The cross-cuts inward (towards the holes).
*   The inner contours $C_2, C_3, C_4$ **clockwise** (opposite to their defined positive direction, so we denote these paths as $-C_2, -C_3, -C_4$).
*   The cross-cuts outward (back to $C_1$).

Because the cross-cuts are infinitesimal in width, the inward journey exactly cancels the outward journey for the integrals along $L_k$.

**Step 3: Apply Cauchy's Integral Theorem.**
Our new master contour $\Gamma$ bounds a simply connected region where $f(z)$ is perfectly analytic.
Therefore, by Cauchy's Integral Theorem:
$$\oint_\Gamma f(z) dz = 0$$

Let's break down the components of $\Gamma$:
$$\oint_{C_1} + \int_{\text{in } L_2} + \oint_{-C_2} + \int_{\text{out } L_2} + \dots + \oint_{-C_4} = 0$$

Because $\int_{\text{in } L_k} f(z)dz = -\int_{\text{out } L_k} f(z)dz$, the cross-cut integrals sum to exactly zero.
This leaves only the contour integrals:
$$\oint_{C_1} f(z)dz + \oint_{-C_2} f(z)dz + \oint_{-C_3} f(z)dz + \oint_{-C_4} f(z)dz = 0$$

**Step 4: Rearrange using directional properties.**
Reversing the direction of a line integral negates its value: $\oint_{-C} f(z)dz = -\oint_C f(z)dz$.
Substitute this property into the equation:
$$\oint_{C_1} f(z)dz - \oint_{C_2} f(z)dz - \oint_{C_3} f(z)dz - \oint_{C_4} f(z)dz = 0$$

Move the negative terms to the right side of the equation:
$$\oint_{C_1} f(z)dz = \oint_{C_2} f(z)dz + \oint_{C_3} f(z)dz + \oint_{C_4} f(z)dz$$
**(Proved)**

***

### Q262. Example: Find the value of $\int_{c}\frac{z+4}{z^{2}+2z+5}dz$ , if C is the circle $\vert{}z+1\vert{}=1$.

**Solution:**

Let $I = \oint_C \frac{z+4}{z^2+2z+5} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator $z^2+2z+5 = 0$ using the quadratic formula:
$$z = \frac{-2 \pm \sqrt{2^2 - 4(1)(5)}}{2}$$
$$z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2}$$
$$z = \frac{-2 \pm 4i}{2} = -1 \pm 2i$$
The two simple poles are $z_1 = -1 + 2i$ and $z_2 = -1 - 2i$.

**Step 2: Check enclosure.**
The contour $C$ is the circle $|z+1| = 1$. This circle is centered at $z=-1$ and has a radius of $1$.
We check the distance from the center $(-1)$ to the poles:
*   **Test $z_1 = -1+2i$:** $|(-1+2i) - (-1)| = |2i| = 2$.
    Since $2 > 1$, the pole $z_1$ is strictly **outside** the contour.
*   **Test $z_2 = -1-2i$:** $|(-1-2i) - (-1)| = |-2i| = 2$.
    Since $2 > 1$, the pole $z_2$ is strictly **outside** the contour.

**Step 3: Apply Cauchy's Integral Theorem.**
Because *both* singularities of the integrand lie strictly outside the boundary of the contour $C$, the entire function $F(z) = \frac{z+4}{z^2+2z+5}$ is analytic everywhere inside and on the contour $C$.

According to Cauchy's Integral Theorem, the integral of any analytic function around a closed loop is exactly zero.

**Answer:** The value of the integral is **$0$**.

***

### Q263. Example: Find the integral $\int_{c}\frac{3z^{2}+7z+1}{z+1}dz,$ where C is the circle $\vert{}z\vert{}=\frac{1}{2}.$

**Solution:**

Let $I = \oint_C \frac{3z^2+7z+1}{z+1} dz$.

**Step 1: Identify the singularity.**
The denominator is zero when $z+1 = 0 \implies z = -1$.
There is a simple pole at $z = -1$.
The numerator is a polynomial and is therefore analytic everywhere.

**Step 2: Check enclosure.**
The contour $C$ is $|z| = 1/2$. This is a circle centered at the origin with a radius of $0.5$.
The distance to the pole is $|-1| = 1$.
Since $1 > 0.5$, the pole $z = -1$ lies strictly **outside** the contour $C$.

**Step 3: Apply Cauchy's Integral Theorem.**
Because the single point of singularity ($z=-1$) lies entirely outside the region bounded by $C$, the full integrand function $F(z) = \frac{3z^2+7z+1}{z+1}$ is completely analytic everywhere inside and on the simple closed curve $C$.

By Cauchy's Integral Theorem, the contour integral of a function over a region where it is analytic is zero.

**Answer:** The value of the integral is **$0$**.

***

### Q264. Example: Evaluate $\oint_{C}e^{z}dz$ where C is shown in Fig.

*(Note: Once again, without the figure, the exact shape of $C$ is unknown. However, because $C$ is indicated as a closed contour ($\oint$) and the integrand is a specific, fundamental type of function, the shape of the contour is irrelevant to the final answer).*

**Solution:**

We must evaluate the closed contour integral $I = \oint_C e^z dz$.

**Step 1: Determine the analyticity of the function.**
The integrand is $f(z) = e^z$.
The complex exponential function $e^z$ is an **entire function**. This means it is infinitely differentiable and continuous (analytic) at every single point in the entire complex plane. It possesses no singularities, poles, or branch cuts anywhere.

**Step 2: Apply the relevant theorem.**
Because $f(z)$ is analytic everywhere in the complex plane, it is guaranteed to be analytic everywhere inside and on the boundary of *any* simple closed contour $C$, regardless of what shape or size the figure shows.

According to Cauchy's Integral Theorem, if a function is analytic inside and on a closed contour $C$, its integral around that contour is exactly zero:
$$\oint_C f(z) dz = 0$$

*(Verification via the Fundamental Theorem of Calculus: The antiderivative of $e^z$ is $e^z$. For any closed loop, the start and end points are identical ($z_{start} = z_{end}$). Evaluating the antiderivative gives $F(z_{end}) - F(z_{start}) = e^{z_{start}} - e^{z_{start}} = 0$).*

**Answer:** The value of the integral is **$0$** (irrespective of the specific shape of the closed contour $C$).

Here are the detailed solutions for the next four questions (Q265 to Q268).

### Q265. Example: Evaluate $\oint_{C}\frac{5z+7}{z^{2}+2z-3}dz$ where C is the circle $|z-2|=2$.

**Solution:**

Let $I = \oint_C \frac{5z+7}{z^2+2z-3} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator by factoring:
$$z^2 + 2z - 3 = 0$$
$$(z + 3)(z - 1) = 0$$
The function has two simple poles:
1.  $z_1 = -3$
2.  $z_2 = 1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z-2| = 2$. It is centered at $z = 2$ and has a radius of $2$.
We check the distance from the center ($2$) to each pole:
*   **Test $z_1 = -3$:** $|(-3) - 2| = |-5| = 5$.
    Since $5 > 2$, the pole $z_1 = -3$ lies strictly **outside** the contour.
*   **Test $z_2 = 1$:** $|(1) - 2| = |-1| = 1$.
    Since $1 < 2$, the pole $z_2 = 1$ lies strictly **inside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_2 = 1$ is enclosed by the contour, we rewrite the integrand to isolate $(z-1)$ in the denominator. The remaining parts form the analytic numerator $f(z)$.
$$I = \oint_C \frac{\left( \frac{5z+7}{z+3} \right)}{z-1} dz$$
Let the numerator function be $f(z) = \frac{5z+7}{z+3}$. This function is analytic inside and on $C$ because its only singularity ($z=-3$) is outside $C$.

**Step 4: Apply Cauchy's Integral Formula.**
The formula for a simple pole is:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 1$.
$$I = 2\pi i \cdot f(1)$$

**Step 5: Evaluate.**
Calculate $f(1)$:
$$f(1) = \frac{5(1) + 7}{1 + 3} = \frac{12}{4} = 3$$

Substitute into the formula:
$$I = 2\pi i (3)$$
$$I = 6\pi i$$

**Answer:** The value of the integral is **$6\pi i$**.

***

### Q266. Example: Evaluate $\oint_{C}\frac{dz}{z^{2}+1}$ where C is the circle $|z|=3$.

**Solution:**

Let $I = \oint_C \frac{1}{z^2+1} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero:
$$z^2 + 1 = 0 \implies z^2 = -1$$
There are two simple poles at $z_1 = i$ and $z_2 = -i$.

**Step 2: Check enclosure.**
The contour $C$ is a circle of radius 3 centered at the origin ($|z|=3$).
*   $|i| = 1 < 3$ (**Inside**)
*   $|-i| = 1 < 3$ (**Inside**)
Both poles are enclosed. We will use the **Residue Theorem**: $I = 2\pi i \sum \text{Residues}$.

**Step 3: Calculate Residue at $z_1 = i$.**
The formula for the residue at a simple pole $a$ is $\text{Res}(a) = \lim_{z\to a} (z-a)F(z)$.
Here $F(z) = \frac{1}{(z-i)(z+i)}$.
$$R_1 = \lim_{z \to i} (z-i) \frac{1}{(z-i)(z+i)} = \lim_{z \to i} \frac{1}{z+i}$$
$$R_1 = \frac{1}{i+i} = \frac{1}{2i}$$
*(Optional: $\frac{1}{2i} \cdot \frac{-i}{-i} = -\frac{i}{2}$)*.

**Step 4: Calculate Residue at $z_2 = -i$.**
$$R_2 = \lim_{z \to -i} (z+i) \frac{1}{(z-i)(z+i)} = \lim_{z \to -i} \frac{1}{z-i}$$
$$R_2 = \frac{1}{-i-i} = \frac{1}{-2i}$$
*(Optional: $\frac{1}{-2i} \cdot \frac{i}{i} = \frac{i}{2}$)*.

**Step 5: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i \left( \frac{1}{2i} + \frac{1}{-2i} \right)$$
$$I = 2\pi i \left( \frac{1}{2i} - \frac{1}{2i} \right)$$
$$I = 2\pi i (0)$$
$$I = 0$$

*(Note: We can also solve this via Partial Fractions without residues. $\frac{1}{z^2+1} = \frac{1}{2i(z-i)} - \frac{1}{2i(z+i)}$. Both poles are inside, so using Cauchy's formula for each gives: $\frac{1}{2i}(2\pi i \cdot 1) - \frac{1}{2i}(2\pi i \cdot 1) = \pi - \pi = 0$.)*

**Answer:** The value of the integral is **$0$**.

***

### Q267. Example: Prove that $\int_{C}\frac{d~z}{z-a}=2\pi i$

*(Note: This statement implicitly assumes $C$ is a simple closed contour enclosing the point $a$ in the positive counter-clockwise direction. This is mathematically identical to Q249(ii) and the $n=-1$ case in Q260. The proof via parameterization is standard and shown below).*

**Solution:**

We need to evaluate the contour integral $I = \oint_C \frac{1}{z-a} dz$, assuming $C$ is a simple closed curve enclosing $z=a$.

**Step 1: Use the Principle of Deformation of Contours.**
The function $f(z) = \frac{1}{z-a}$ is analytic everywhere except at the pole $z=a$.
By the principle of deformation, the integral over any simple closed curve $C$ enclosing $a$ is perfectly equal to the integral over a small circle $C_r$ of radius $r$ centered precisely at $a$, provided $C_r$ lies entirely within $C$.
$$\oint_C \frac{dz}{z-a} = \oint_{C_r} \frac{dz}{z-a}$$

**Step 2: Parameterize the circular contour $C_r$.**
A circle of radius $r$ centered at $a$ is defined by the equation $|z-a| = r$.
We can express this in exponential polar coordinates:
$$z - a = r e^{i\theta}$$
$$z = a + r e^{i\theta}$$
To traverse the circle once in the positive (counter-clockwise) direction, the parameter $\theta$ must go from $0$ to $2\pi$.

**Step 3: Differentiate to find $dz$.**
Take the derivative of $z$ with respect to $\theta$:
$$dz = \frac{d}{d\theta}(a + r e^{i\theta}) d\theta$$
Since $a$ and $r$ are constants:
$$dz = i r e^{i\theta} d\theta$$

**Step 4: Substitute the parameterization into the integral.**
Replace $(z-a)$ in the denominator and $dz$ in the numerator:
$$I = \int_0^{2\pi} \frac{i r e^{i\theta} d\theta}{r e^{i\theta}}$$

**Step 5: Simplify and evaluate the integral.**
The term $r e^{i\theta}$ appears in both the numerator and the denominator, so it cancels out completely. This shows that the value of the integral is entirely independent of the radius $r$.
$$I = \int_0^{2\pi} i \ d\theta$$
Pull the constant $i$ outside the integral:
$$I = i \int_0^{2\pi} 1 \ d\theta$$
Evaluate the definite integral:
$$I = i [\theta]_0^{2\pi}$$
$$I = i (2\pi - 0)$$
$$I = 2\pi i$$
**(Proved)**

***

### Q268. Example: Use Cauchy's integral formula to evaluate $\int_{c}\frac{z}{(z^{2}-3z+2)}d~z$ where c is the circle $|z-2|=\frac{1}{2}$

**Solution:**

Let $I = \oint_C \frac{z}{z^2-3z+2} dz$.

**Step 1: Identify the singularities.**
Factor the quadratic denominator:
$$z^2 - 3z + 2 = 0$$
$$(z - 1)(z - 2) = 0$$
The function has two simple poles:
1.  $z_1 = 1$
2.  $z_2 = 2$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z-2| = 0.5$. It is centered at $z = 2$ and has a radius of $0.5$.
We check the distance from the center ($2$) to each pole:
*   **Test $z_1 = 1$:** $|1 - 2| = |-1| = 1$.
    Since $1 > 0.5$, the pole $z_1 = 1$ lies strictly **outside** the contour.
*   **Test $z_2 = 2$:** $|2 - 2| = |0| = 0$.
    Since $0 < 0.5$ (it is exactly the center), the pole $z_2 = 2$ lies **inside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_2 = 2$ is enclosed by the contour, we must isolate $(z-2)$ in the denominator. The rest of the expression will form our analytic numerator $f(z)$.
$$I = \oint_C \frac{ \left( \frac{z}{z-1} \right) }{z-2} dz$$
Let the analytic numerator function be $f(z) = \frac{z}{z-1}$. This function is perfectly analytic everywhere inside and on $C$ because its singularity ($z=1$) is located outside the contour.

**Step 4: Apply Cauchy's Integral Formula.**
The formula states:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 2$.
$$I = 2\pi i \cdot f(2)$$

**Step 5: Evaluate $f(2)$.**
Substitute $z = 2$ into our numerator function:
$$f(2) = \frac{2}{2 - 1} = \frac{2}{1} = 2$$

Multiply by $2\pi i$:
$$I = 2\pi i (2)$$
$$I = 4\pi i$$

**Answer:** The value of the integral is **$4\pi i$**.

Here are the detailed solutions for the next four questions (Q269 to Q272).

### Q269. Example: $\int_{C}\frac{2z+1}{z^{2}+z}dz$ where C is $|z|=\frac{1}{2}.$

**Solution:**

Let $I = \oint_C \frac{2z+1}{z^2+z} dz$.

**Step 1: Identify the singularities.**
Factor the denominator to find where it equals zero:
$$z^2 + z = 0$$
$$z(z + 1) = 0$$
There are two simple poles:
1.  $z_1 = 0$
2.  $z_2 = -1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 1/2$. This is a circle centered at the origin $(0,0)$ with a radius of $0.5$.
*   **Test $z_1 = 0$:** $|0| = 0 < 0.5$. This pole is at the center, so it is **inside** the contour.
*   **Test $z_2 = -1$:** $|-1| = 1 > 0.5$. This pole is strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Since only the pole at $z=0$ is enclosed, we isolate $z$ in the denominator and move the rest of the function to the numerator.
$$I = \oint_C \frac{\left( \frac{2z+1}{z+1} \right)}{z} dz$$
Let the numerator function be $f(z) = \frac{2z+1}{z+1}$. This function is analytic everywhere inside and on the contour $C$ because its only singularity ($z=-1$) is outside.

**Step 4: Apply Cauchy's Integral Formula.**
The formula is $\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$.
Here, $a = 0$.
$$I = 2\pi i \cdot f(0)$$

**Step 5: Evaluate.**
Calculate $f(0)$:
$$f(0) = \frac{2(0) + 1}{0 + 1} = \frac{1}{1} = 1$$

Substitute into the formula:
$$I = 2\pi i (1)$$
$$I = 2\pi i$$

*(Alternative "trick" method: Notice that the numerator is the exact derivative of the denominator. Let $u = z^2+z$, then $du = (2z+1)dz$. The integral is $\oint_C \frac{du}{u}$. We know from fundamental complex analysis that $\oint_C \frac{du}{u} = 2\pi i$ if the contour winds once around $u=0$. Since $z=0 \implies u=0$ is enclosed, and it's a simple mapping near the origin, the answer is $2\pi i$. The formal method above is much safer).*

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q270. Example: Evaluate the complex integral $\int_{c}tan~z.d~z$ where c is $|z|=2$.

**Solution:**

Let $I = \oint_C \tan z \ dz$.

**Step 1: Express the function in a rational form to identify singularities.**
$$\tan z = \frac{\sin z}{\cos z}$$
Singularities occur where the denominator is zero:
$$\cos z = 0$$
The roots of the complex cosine function (as shown in Q128) are entirely real and occur at:
$$z = \frac{\pi}{2} + n\pi \quad \text{where } n \text{ is an integer } (0, \pm 1, \pm 2, \dots)$$
The singularities are simple poles.

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 2$ (centered at the origin with radius 2).
We need to find which values of $\frac{\pi}{2} + n\pi$ have an absolute value less than 2.
We know $\pi \approx 3.14159$.
*   For $n = 0$: $z = \frac{\pi}{2} \approx 1.57$. Since $1.57 < 2$, this pole is **inside**.
*   For $n = -1$: $z = -\frac{\pi}{2} \approx -1.57$. Since $|-1.57| = 1.57 < 2$, this pole is **inside**.
*   For $n = 1$: $z = \frac{3\pi}{2} \approx 4.71$. Since $4.71 > 2$, this pole is **outside**.
*   For $n = -2$: $z = -\frac{3\pi}{2} \approx -4.71$. Since $4.71 > 2$, this pole is **outside**.

There are exactly two simple poles enclosed by the contour: $z_1 = \pi/2$ and $z_2 = -\pi/2$.

**Step 3: Calculate the residues at the enclosed poles.**
For a function of the form $F(z) = \frac{P(z)}{Q(z)}$ where $P$ and $Q$ are analytic, $Q(a) = 0$ (a simple root), and $P(a) \neq 0$, the residue at $z=a$ can be quickly calculated using the formula:
$$\text{Res}(F, a) = \frac{P(a)}{Q'(a)}$$
Here, $P(z) = \sin z$ and $Q(z) = \cos z$.
The derivative of the denominator is $Q'(z) = -\sin z$.

*   **Residue at $z_1 = \pi/2$:**
    $$R_1 = \frac{P(\pi/2)}{Q'(\pi/2)} = \frac{\sin(\pi/2)}{-\sin(\pi/2)}$$
    Since $\sin(\pi/2) = 1$:
    $$R_1 = \frac{1}{-1} = -1$$

*   **Residue at $z_2 = -\pi/2$:**
    $$R_2 = \frac{P(-\pi/2)}{Q'(-\pi/2)} = \frac{\sin(-\pi/2)}{-\sin(-\pi/2)}$$
    Since $\sin(-\pi/2) = -1$:
    $$R_2 = \frac{-1}{-(-1)} = \frac{-1}{1} = -1$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \sum \text{Residues enclosed in } C$$
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i (-1 + -1)$$
$$I = 2\pi i (-2)$$
$$I = -4\pi i$$

**Answer:** The value of the integral is **$-4\pi i$**.

***

### Q271. Example: Evaluate the following integral using Cauchy integral formula $\int_{c}\frac{4-3z}{z(z-1)(z-2)}dz$ where c is the circle $|z|=\frac{3}{2}.$

**Solution:**

Let $I = \oint_C \frac{4-3z}{z(z-1)(z-2)} dz$.

**Step 1: Identify the singularities.**
The denominator is already factored: $z(z-1)(z-2) = 0$.
There are three simple poles:
1.  $z_1 = 0$
2.  $z_2 = 1$
3.  $z_3 = 2$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 3/2 = 1.5$.
*   $|0| = 0 < 1.5$ (**Inside**)
*   $|1| = 1 < 1.5$ (**Inside**)
*   $|2| = 2 > 1.5$ (**Outside**)

There are two poles enclosed: $z=0$ and $z=1$.

**Step 3: Apply Cauchy's Integral Formula.**
Because there are two enclosed poles, we cannot isolate just one in the denominator directly. We must use partial fractions to split the expression, or use the Residue Theorem. Since the prompt explicitly asks to use Cauchy's integral formula, we must use **Partial Fraction Decomposition** on the part of the function containing the enclosed poles.

Let's look at the term $\frac{1}{z(z-1)}$. We can decompose it:
$$\frac{1}{z(z-1)} = \frac{A}{z} + \frac{B}{z-1}$$
$$1 = A(z-1) + Bz$$
If $z=0 \implies 1 = -A \implies A = -1$.
If $z=1 \implies 1 = B \implies B = 1$.
So, $\frac{1}{z(z-1)} = \frac{-1}{z} + \frac{1}{z-1}$.

Now substitute this back into our full integrand:
$$\frac{4-3z}{z(z-1)(z-2)} = \frac{4-3z}{z-2} \left[ \frac{-1}{z} + \frac{1}{z-1} \right]$$
$$= \frac{-(4-3z)}{z(z-2)} + \frac{4-3z}{(z-1)(z-2)}$$

We can now split the main integral into two separate integrals:
$$I = \oint_C \frac{ \left( \frac{3z-4}{z-2} \right) }{z} dz + \oint_C \frac{ \left( \frac{4-3z}{z-2} \right) }{z-1} dz$$

**Step 4: Evaluate the two integrals using Cauchy's Formula.**
*   **First Integral ($I_1$):**
    Enclosed pole: $a = 0$. Analytic numerator: $f_1(z) = \frac{3z-4}{z-2}$.
    $$I_1 = 2\pi i \cdot f_1(0) = 2\pi i \left( \frac{3(0)-4}{0-2} \right) = 2\pi i \left( \frac{-4}{-2} \right) = 2\pi i (2) = 4\pi i$$

*   **Second Integral ($I_2$):**
    Enclosed pole: $a = 1$. Analytic numerator: $f_2(z) = \frac{4-3z}{z-2}$.
    $$I_2 = 2\pi i \cdot f_2(1) = 2\pi i \left( \frac{4-3(1)}{1-2} \right) = 2\pi i \left( \frac{1}{-1} \right) = 2\pi i (-1) = -2\pi i$$

**Step 5: Sum the integrals.**
$$I = I_1 + I_2 = 4\pi i - 2\pi i = 2\pi i$$

*(Self-Check using Residue Theorem: 
Res at $0$: $\frac{4-0}{(0-1)(0-2)} = \frac{4}{2} = 2$.
Res at $1$: $\frac{4-3(1)}{1(1-2)} = \frac{1}{-1} = -1$.
Sum = $2 - 1 = 1$. Integral = $2\pi i(1) = 2\pi i$. Matches perfectly and is much faster).*

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q272. Example: Integrate $\frac{1}{(z^{3}-1)^{2}}$ the counter clock-wise sense around the circle $|z-1|=1$.

**Solution:**

Let $I = \oint_C \frac{1}{(z^3-1)^2} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator:
$$(z^3 - 1)^2 = 0 \implies z^3 = 1$$
We need to find the three cube roots of unity.
$z^3 - 1 = (z-1)(z^2+z+1) = 0$
The roots are:
1.  $z_1 = 1$
2.  $z_2 = \frac{-1 + i\sqrt{3}}{2}$
3.  $z_3 = \frac{-1 - i\sqrt{3}}{2}$

Because the entire expression $(z^3-1)$ is squared in the denominator, all three of these roots are **poles of order 2**.

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z-1| = 1$. Center is $z=1$, radius is $1$.
*   **Test $z_1 = 1$:** $|1 - 1| = 0 < 1$. This pole is the center, so it is **inside**.
*   **Test $z_2 = -0.5 + i\frac{\sqrt{3}}{2}$:**
    $$|(-0.5 + i\frac{\sqrt{3}}{2}) - 1| = |-1.5 + i\frac{\sqrt{3}}{2}| = \sqrt{(-1.5)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} = \sqrt{2.25 + 0.75} = \sqrt{3} \approx 1.732$$
    Since $1.732 > 1$, this pole is **outside**.
*   **Test $z_3 = -0.5 - i\frac{\sqrt{3}}{2}$:**
    $$|(-0.5 - i\frac{\sqrt{3}}{2}) - 1| = |-1.5 - i\frac{\sqrt{3}}{2}| = \sqrt{3} \approx 1.732$$
    Since $1.732 > 1$, this pole is **outside**.

Only $z_1 = 1$ is enclosed. It is a pole of order 2.

**Step 3: Structure the integral for the Generalized Cauchy Formula.**
We factor the denominator: $(z^3-1)^2 = [(z-1)(z^2+z+1)]^2 = (z-1)^2(z^2+z+1)^2$.
Isolate $(z-1)^2$ in the denominator:
$$I = \oint_C \frac{ \left( \frac{1}{(z^2+z+1)^2} \right) }{(z-1)^2} dz$$
Let the analytic numerator function be $f(z) = \frac{1}{(z^2+z+1)^2}$.

**Step 4: Apply the Generalized Cauchy Integral Formula.**
For a pole of order 2 ($n+1=2 \implies n=1$):
$$\oint_C \frac{f(z)}{(z-a)^2} dz = \frac{2\pi i}{1!} f'(a) = 2\pi i \cdot f'(a)$$
Here, $a = 1$.
$$I = 2\pi i \cdot f'(1)$$

**Step 5: Calculate the derivative $f'(z)$.**
$f(z) = (z^2+z+1)^{-2}$
Using the power rule and chain rule:
$$f'(z) = -2(z^2+z+1)^{-3} \cdot \frac{d}{dz}(z^2+z+1)$$
$$f'(z) = \frac{-2(2z+1)}{(z^2+z+1)^3}$$

**Step 6: Evaluate $f'(1)$.**
Substitute $z = 1$:
$$f'(1) = \frac{-2(2(1)+1)}{((1)^2+1+1)^3} = \frac{-2(3)}{(3)^3} = \frac{-6}{27} = -\frac{2}{9}$$

**Step 7: Final calculation.**
Substitute into the integral formula:
$$I = 2\pi i \left( -\frac{2}{9} \right) = -\frac{4\pi i}{9}$$

**Answer:** The value of the integral is **$-\frac{4\pi i}{9}$**.

Here are the detailed solutions for the next four questions (Q273 to Q276).

### Q273. Example: Evaluate $\oint_{C}\frac{z^{2}-4z+4}{z+i}dz$ where C is the circle $|z|=2$.

**Solution:**

Let $I = \oint_C \frac{z^2-4z+4}{z+i} dz$.

**Step 1: Identify the singularity.**
Set the denominator to zero:
$$z + i = 0 \implies z = -i$$
There is a simple pole at $z = -i$.

**Step 2: Check if the pole lies inside the contour.**
The contour $C$ is defined by $|z| = 2$. This is a circle of radius 2 centered at the origin.
Evaluate the modulus of the pole:
$$|-i| = 1$$
Since $1 < 2$, the pole $z = -i$ lies strictly **inside** the contour $C$.

**Step 3: Apply Cauchy's Integral Formula.**
The integral is already in the correct form to apply the formula directly:
$$I = \oint_C \frac{f(z)}{z - a} dz$$
Where:
*   The pole is $a = -i$.
*   The analytic numerator function is $f(z) = z^2 - 4z + 4$. (Note: $z^2-4z+4$ can be factored as $(z-2)^2$, which is a polynomial and thus analytic everywhere).

The formula states:
$$I = 2\pi i \cdot f(a)$$

**Step 4: Evaluate $f(-i)$.**
Substitute $z = -i$ into $f(z)$:
$$f(-i) = (-i)^2 - 4(-i) + 4$$
$$f(-i) = i^2 + 4i + 4$$
Since $i^2 = -1$:
$$f(-i) = -1 + 4i + 4$$
$$f(-i) = 3 + 4i$$

**Step 5: Calculate the final result.**
Multiply by $2\pi i$:
$$I = 2\pi i (3 + 4i)$$
$$I = 6\pi i + 8\pi i^2$$
Since $i^2 = -1$:
$$I = 6\pi i - 8\pi$$
$$I = 2\pi(-4 + 3i)$$

**Answer:** The value of the integral is **$-8\pi + 6\pi i$** (or **$2\pi(-4 + 3i)$**).

***

### Q274. Example: Evaluate $\oint_{C}\frac{z}{z^{2}+9}dz$ where C is the circle $|z-2i|=4$.

**Solution:**

Let $I = \oint_C \frac{z}{z^2+9} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator:
$$z^2 + 9 = 0 \implies z^2 = -9 \implies z = \pm \sqrt{-9} = \pm 3i$$
There are two simple poles:
1.  $z_1 = 3i$
2.  $z_2 = -3i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z - 2i| = 4$. It is centered at $z = 2i$ (coordinate $(0,2)$) with a radius of $4$.
*   **Test $z_1 = 3i$:**
    $|3i - 2i| = |i| = 1$.
    Since $1 < 4$, the pole $z_1 = 3i$ lies **inside** the contour.
*   **Test $z_2 = -3i$:**
    $|-3i - 2i| = |-5i| = 5$.
    Since $5 > 4$, the pole $z_2 = -3i$ lies strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_1 = 3i$ is enclosed, we factor the denominator to $(z-3i)(z+3i)$ and isolate $(z-3i)$ as the denominator of the whole expression.
$$I = \oint_C \frac{\left( \frac{z}{z+3i} \right)}{z - 3i} dz$$
Let the analytic numerator function be $f(z) = \frac{z}{z+3i}$. This function is analytic everywhere inside and on $C$ because its singularity ($z=-3i$) is outside.

**Step 4: Apply Cauchy's Integral Formula.**
$$I = 2\pi i \cdot f(3i)$$

**Step 5: Evaluate $f(3i)$.**
Substitute $z = 3i$ into our numerator function:
$$f(3i) = \frac{3i}{3i + 3i} = \frac{3i}{6i}$$
The $i$'s cancel out:
$$f(3i) = \frac{3}{6} = \frac{1}{2}$$

**Step 6: Calculate final result.**
$$I = 2\pi i \left( \frac{1}{2} \right)$$
$$I = \pi i$$

**Answer:** The value of the integral is **$\pi i$**.

***

### Q275. Example: Evaluate the integral $\int_{c}\frac{z^{2}}{2-z}dz$ where C is $|z-1|=2$

**Solution:**

Let $I = \oint_C \frac{z^2}{2-z} dz$.

**Step 1: Identify the singularity.**
Set the denominator to zero:
$$2 - z = 0 \implies z = 2$$
There is a simple pole at $z = 2$.

**Step 2: Check if the pole lies inside the contour.**
The contour $C$ is the circle $|z-1| = 2$. It is centered at $z = 1$ with a radius of $2$.
Test the distance from the center to the pole:
$$|2 - 1| = |1| = 1$$
Since $1 < 2$, the pole $z = 2$ lies **inside** the contour.

**Step 3: Reformat the integral to match Cauchy's Formula exactly.**
Cauchy's Integral Formula requires the denominator to be strictly in the form $(z - a)$, not $(a - z)$.
We can achieve this by factoring out a $-1$ from the denominator:
$$2 - z = -(z - 2)$$
Substitute this back into the integral:
$$I = \oint_C \frac{z^2}{-(z - 2)} dz = -\oint_C \frac{z^2}{z - 2} dz$$

**Step 4: Apply Cauchy's Integral Formula.**
We evaluate $I = -\oint_C \frac{f(z)}{z - a} dz$.
Where:
*   The pole is $a = 2$.
*   The analytic numerator function is $f(z) = z^2$.

The formula gives:
$$I = - [ 2\pi i \cdot f(2) ]$$

**Step 5: Evaluate $f(2)$.**
Substitute $z = 2$ into $f(z)$:
$$f(2) = (2)^2 = 4$$

**Step 6: Calculate the final result.**
$$I = - [ 2\pi i \cdot 4 ]$$
$$I = -8\pi i$$

**Answer:** The value of the integral is **$-8\pi i$**.

***

### Q276. Example: Evaluate $\oint_{C}\frac{z+1}{z^{4}+4z^{3}}dz$ where C is the circle $|z|=1$.

**Solution:**

Let $I = \oint_C \frac{z+1}{z^4+4z^3} dz$.

**Step 1: Identify the singularities.**
Factor the denominator to find its roots:
$$z^4 + 4z^3 = 0$$
$$z^3(z + 4) = 0$$
There are two singular points:
1.  $z_1 = 0$ (This is a **pole of order 3** because of the $z^3$ term).
2.  $z_2 = -4$ (This is a simple pole).

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 1$ (centered at the origin with radius 1).
*   **Test $z_1 = 0$:** $|0| = 0 < 1$. This pole is **inside** the contour.
*   **Test $z_2 = -4$:** $|-4| = 4 > 1$. This pole is strictly **outside** the contour.

**Step 3: Structure the integral for the Generalized Cauchy Formula.**
Because only the higher-order pole $z_1 = 0$ is enclosed, we isolate $z^3$ in the denominator and move the rest of the function into the numerator.
$$I = \oint_C \frac{\left( \frac{z+1}{z+4} \right)}{z^3} dz$$
Let the analytic numerator function be $f(z) = \frac{z+1}{z+4}$. This function is analytic everywhere inside and on $|z|=1$ because its singularity ($z=-4$) lies safely outside.

**Step 4: Apply the Generalized Cauchy Integral Formula.**
For a pole of order $n+1$, the formula is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map our parameters to the formula:
*   $a = 0$
*   $n+1 = 3 \implies n = 2$. We need to find the **second derivative** of $f(z)$.

**Step 5: Calculate the derivatives of $f(z)$.**
$f(z) = \frac{z+1}{z+4}$
Use the quotient rule to find the first derivative $f'(z)$:
$$f'(z) = \frac{(1)(z+4) - (z+1)(1)}{(z+4)^2} = \frac{z + 4 - z - 1}{(z+4)^2} = \frac{3}{(z+4)^2}$$
Rewrite $f'(z)$ to make the second derivative easier: $f'(z) = 3(z+4)^{-2}$.

Find the second derivative $f''(z)$ using the power rule:
$$f''(z) = -2 \cdot 3(z+4)^{-3} \cdot (1) = \frac{-6}{(z+4)^3}$$

**Step 6: Evaluate $f''(0)$.**
Substitute $z = 0$ into our second derivative:
$$f''(0) = \frac{-6}{(0+4)^3} = \frac{-6}{4^3} = \frac{-6}{64} = -\frac{3}{32}$$

**Step 7: Calculate final result.**
Substitute everything into the generalized formula:
$$I = \frac{2\pi i}{2!} f''(0)$$
$$I = \frac{2\pi i}{2} \left( -\frac{3}{32} \right)$$
$$I = \pi i \left( -\frac{3}{32} \right)$$
$$I = -\frac{3\pi i}{32}$$

**Answer:** The value of the integral is **$-\frac{3\pi i}{32}$**.

Here are the detailed solutions for the next four questions (Q277 to Q280).

### Q277. Example: Evaluate $\oint_{C}\frac{z^{3}+3}{z(z-i)^{2}}dz$ where C is shown in Fig.

*(Note: As with previous questions mentioning a figure, the exact shape of $C$ is unknown. For a contour integral, the only thing that matters is which poles are enclosed. I will assume the standard textbook configuration for this problem where $C$ is a simple closed contour enclosing BOTH singularities. The steps shown below cover the universal technique, and you can simply drop any residue if the figure reveals a pole is actually outside).*

**Assumption for Solution:** Assume contour $C$ is large enough to enclose all singularities (e.g., $|z| = 2$). Let $I = \oint_C \frac{z^3+3}{z(z-i)^2} dz$.

**Step 1: Identify the singularities.**
The denominator is $z(z-i)^2 = 0$.
There are two singular points:
1.  $z_1 = 0$ (a simple pole, order 1).
2.  $z_2 = i$ (a pole of order 2).
*(We assume both are inside $C$. If the figure shows one outside, skip its residue).*

**Step 2: Calculate the Residues at the enclosed poles.**
Because there are multiple poles of different orders enclosed, we use Cauchy's Residue Theorem: $I = 2\pi i \sum \text{Residues}$.

*   **Calculate Residue at $z_1 = 0$ (Simple Pole):**
    Formula: $\text{Res}(0) = \lim_{z\to 0} (z-0)F(z)$.
    $$R_1 = \lim_{z \to 0} z \cdot \frac{z^3+3}{z(z-i)^2} = \lim_{z \to 0} \frac{z^3+3}{(z-i)^2}$$
    Substitute $z=0$:
    $$R_1 = \frac{0^3+3}{(0-i)^2} = \frac{3}{(-i)^2} = \frac{3}{i^2} = \frac{3}{-1} = -3$$

*   **Calculate Residue at $z_2 = i$ (Pole of Order 2):**
    Formula for order $m=2$: $\text{Res}(i) = \lim_{z\to i} \frac{d}{dz} \left[ (z-i)^2 F(z) \right]$.
    $$R_2 = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 \frac{z^3+3}{z(z-i)^2} \right] = \lim_{z \to i} \frac{d}{dz} \left( \frac{z^3+3}{z} \right)$$
    Simplify the fraction before differentiating: $\frac{z^3+3}{z} = z^2 + 3z^{-1}$.
    Take the derivative:
    $$\frac{d}{dz} (z^2 + 3z^{-1}) = 2z - 3z^{-2} = 2z - \frac{3}{z^2}$$
    Now evaluate the limit as $z \to i$:
    $$R_2 = 2(i) - \frac{3}{(i)^2} = 2i - \frac{3}{-1} = 2i + 3 = 3 + 2i$$

**Step 3: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i (-3 + 3 + 2i)$$
$$I = 2\pi i (2i)$$
$$I = 4\pi i^2$$
Since $i^2 = -1$:
$$I = -4\pi$$

**Answer:** Assuming the contour encloses both poles, the value of the integral is **$-4\pi$**.

***

### Q278. Example: $\int_{C}\frac{dz}{z^{4}-1}$ where C is the circle $|z-i|=1$

**Solution:**

Let $I = \oint_C \frac{1}{z^4-1} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator by factoring:
$$z^4 - 1 = 0$$
Using difference of squares $(a^2-b^2) = (a-b)(a+b)$:
$$(z^2 - 1)(z^2 + 1) = 0$$
$$(z - 1)(z + 1)(z - i)(z + i) = 0$$
There are four simple poles:
1.  $z_1 = 1$
2.  $z_2 = -1$
3.  $z_3 = i$
4.  $z_4 = -i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z-i| = 1$. It is centered at $z=i$ with a radius of $1$.
*   **Test $z_1 = 1$:** $|1 - i| = \sqrt{1^2 + (-1)^2} = \sqrt{2} \approx 1.414$. Since $\sqrt{2} > 1$, it is **outside**.
*   **Test $z_2 = -1$:** $|-1 - i| = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$. Since $\sqrt{2} > 1$, it is **outside**.
*   **Test $z_3 = i$:** $|i - i| = |0| = 0$. Since $0 < 1$ (it is the center), it is **inside**.
*   **Test $z_4 = -i$:** $|-i - i| = |-2i| = 2$. Since $2 > 1$, it is **outside**.

Only one pole, $z_3 = i$, is enclosed by the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
We isolate $(z-i)$ in the denominator and move the rest of the factored expression to the numerator:
$$I = \oint_C \frac{\left( \frac{1}{(z-1)(z+1)(z+i)} \right)}{z-i} dz$$
Notice that $(z-1)(z+1) = z^2-1$. We can rewrite the numerator more compactly to save calculation time:
$$f(z) = \frac{1}{(z^2-1)(z+i)}$$
This function $f(z)$ is analytic inside and on $C$ because all its singularities are safely outside.

**Step 4: Apply Cauchy's Integral Formula.**
$$I = 2\pi i \cdot f(i)$$

**Step 5: Evaluate $f(i)$.**
Substitute $z = i$ into our numerator function:
$$f(i) = \frac{1}{( (i)^2 - 1 )(i + i)}$$
Since $i^2 = -1$:
$$f(i) = \frac{1}{(-1 - 1)(2i)} = \frac{1}{(-2)(2i)} = \frac{1}{-4i}$$

Multiply top and bottom by $i$ to rationalize:
$$f(i) = \frac{1 \cdot i}{-4i \cdot i} = \frac{i}{-4i^2} = \frac{i}{-4(-1)} = \frac{i}{4}$$

**Step 6: Calculate final result.**
$$I = 2\pi i \left( \frac{i}{4} \right)$$
$$I = \frac{2\pi i^2}{4}$$
$$I = \frac{2\pi(-1)}{4} = -\frac{2\pi}{4} = -\frac{\pi}{2}$$

**Answer:** The value of the integral is **$-\frac{\pi}{2}$**.

***

### Q279. Example: $\int_{C}\frac{dz}{z^{2}+1}$ where C is the circle $|z+i|=1$

**Solution:**

Let $I = \oint_C \frac{1}{z^2+1} dz$.

**Step 1: Identify the singularities.**
Factor the denominator:
$$z^2 + 1 = 0 \implies (z-i)(z+i) = 0$$
There are two simple poles:
1.  $z_1 = i$
2.  $z_2 = -i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z+i| = 1$. It is centered at $z = -i$ with a radius of $1$.
*   **Test $z_1 = i$:** $|i + i| = |2i| = 2$. Since $2 > 1$, the pole $z_1=i$ lies strictly **outside** the contour.
*   **Test $z_2 = -i$:** $|-i + i| = |0| = 0$. Since $0 < 1$ (it is the center), the pole $z_2=-i$ lies **inside** the contour.

Only the pole at $z = -i$ is enclosed.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Isolate $(z+i)$ in the denominator, keeping the rest as the analytic numerator $f(z)$.
$$I = \oint_C \frac{\left( \frac{1}{z-i} \right)}{z+i} dz$$
Here, $f(z) = \frac{1}{z-i}$. This function is analytic everywhere inside and on $C$.

**Step 4: Apply Cauchy's Integral Formula.**
The formula is $\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$.
Here, $a = -i$.
$$I = 2\pi i \cdot f(-i)$$

**Step 5: Evaluate.**
Calculate $f(-i)$:
$$f(-i) = \frac{1}{-i - i} = \frac{1}{-2i}$$

Substitute into the formula:
$$I = 2\pi i \left( \frac{1}{-2i} \right)$$
The $\pi i$ terms and the $2$ terms cancel out entirely:
$$I = -1 \cdot \pi = -\pi$$

**Answer:** The value of the integral is **$-\pi$**.

***

### Q280. Question: Morera's Theorem (converse of Cauchy's theorem) Let $f(z)$ be continuous in a simply-connected region R and suppose that $\oint_{C}f(z)dz=0$ around every simple closed curve C in R. Then $f(z)$ is analytic in R.

*(Note: The prompt does not explicitly ask to prove this theorem, but rather states it as a fact for memorization, typical of lecture slides. A formal proof of Morera's theorem is generally considered advanced material and relies on constructing an analytic antiderivative. I will provide a standard outline of the proof for completeness).*

**Solution (Proof Outline of Morera's Theorem):**

**Step 1: Construct an antiderivative function $F(z)$.**
Fix a base point $z_0$ in the simply connected region $R$. Define a new function $F(z)$ by integrating $f(w)$ from $z_0$ to any point $z$ inside $R$:
$$F(z) = \int_{z_0}^z f(w) dw$$

**Step 2: Justify that $F(z)$ is well-defined (Path Independence).**
For $F(z)$ to be a valid, single-valued function, the integral must yield the exact same result regardless of the path chosen between $z_0$ and $z$.
Let $C_1$ and $C_2$ be two different paths from $z_0$ to $z$ within $R$. 
If we travel along $C_1$ and return along $-C_2$ (the reverse of $C_2$), we form a simple closed contour $C = C_1 - C_2$.
We are given the hypothesis that $\oint_C f(w)dw = 0$ for *any* closed curve. Therefore:
$$\int_{C_1} f(w)dw - \int_{C_2} f(w)dw = 0 \implies \int_{C_1} f(w)dw = \int_{C_2} f(w)dw$$
Because the integrals are equal, $F(z)$ is a well-defined, path-independent function.

**Step 3: Prove that $F'(z) = f(z)$.**
We evaluate the derivative of $F(z)$ using the limit definition:
$$F'(z) = \lim_{h \to 0} \frac{F(z+h) - F(z)}{h}$$
Substitute the integral definition of $F$:
$$F'(z) = \lim_{h \to 0} \frac{1}{h} \left( \int_{z_0}^{z+h} f(w) dw - \int_{z_0}^z f(w) dw \right)$$
By the properties of path-independent integrals, the difference of these integrals is simply the integral from $z$ to $z+h$:
$$F'(z) = \lim_{h \to 0} \frac{1}{h} \int_{z}^{z+h} f(w) dw$$
Because $f(w)$ is continuous at $z$, for small $h$, $f(w)$ is approximately constant and equal to $f(z)$ over the short path from $z$ to $z+h$. We can extract it:
$$F'(z) = \lim_{h \to 0} \frac{1}{h} f(z) \int_{z}^{z+h} 1 \ dw$$
$$F'(z) = \lim_{h \to 0} \frac{1}{h} f(z) [w]_z^{z+h} = \lim_{h \to 0} \frac{1}{h} f(z) (h) = f(z)$$
Since $F'(z)$ exists (and equals $f(z)$), $F(z)$ is an analytic function.

**Step 4: Use a fundamental theorem of analytic functions.**
A major theorem in complex analysis (derived from Cauchy's Integral Formula) states that if a function $F(z)$ is analytic, its derivative $F'(z)$ is also analytic, and so are all higher-order derivatives.
Since we proved $F(z)$ is analytic, its derivative $F'(z)$ must be analytic.
Because $F'(z) = f(z)$, this implies that **$f(z)$ is analytic**. **(Proved)**


Here are the detailed solutions for the next four questions (Q281 to Q284).

*(Note: Questions Q281, Q283, and Q284 are identical to Q248, Q249, and Q250. Detailed solutions are provided again below).*

### Q281. Problem 4.4.1: Prove that (i) $\oint_{C}dz=0$ (ii) $\oint_{C}z~dz=0$ (iii) $\oint_{C}(z-z_{0})dz=0$ where C is any simple closed curve and $z_{0}$ is a constant.

**Solution:**

We prove these identically using **Cauchy's Integral Theorem**.

**Theorem Review:** Cauchy's Integral Theorem states that if a function $f(z)$ is analytic (holomorphic) everywhere inside and on a simple closed contour $C$, then its contour integral around $C$ is exactly zero: $\oint_C f(z) dz = 0$.

**Part (i): Prove $\oint_C dz=0$**
1.  The integrand is the constant function $f(z) = 1$.
2.  The constant function $f(z) = 1$ is a polynomial of degree 0. All polynomials are analytic everywhere in the complex plane (they are entire functions).
3.  Since $f(z)=1$ is analytic everywhere inside and on $C$, Cauchy's Integral Theorem applies directly.
$$\oint_C 1 \ dz = 0$$ **(Proved)**

**Part (ii): Prove $\oint_C z dz=0$**
1.  The integrand is $f(z) = z$.
2.  The function $f(z) = z$ is a polynomial of degree 1. Therefore, it is an entire function, analytic everywhere in the complex plane.
3.  Since $f(z)=z$ is analytic everywhere inside and on $C$, Cauchy's Integral Theorem applies directly.
$$\oint_C z \ dz = 0$$ **(Proved)**

**Part (iii): Prove $\oint_C (z-z_0)dz=0$**
1.  The integrand is $f(z) = z - z_0$.
2.  Since $z_0$ is a constant, this function is a polynomial of degree 1. Therefore, it is an entire function, analytic everywhere.
3.  Since $f(z)=z-z_0$ is analytic everywhere inside and on $C$, Cauchy's Integral Theorem applies directly.
$$\oint_C (z-z_0) \ dz = 0$$ **(Proved)**

***

### Q282. Problem 4.4.2: Let $f(z)$ be analytic in a region $\mathcal{R}$ bounded by two simple closed curves $C_{1}$ and $C_{2}$ and also on curves $C_{1}$ and $C_{2}$. Prove that $\oint_{C_{1}}f(z)dz=\oint_{C_{2}}f(z)dz$ where $C_{1}$ and $C_{2}$ are both traversed in the positive sense relative to their interior's

**Solution:**

This is the formal proof for the **Principle of Deformation of Contours** (for a doubly-connected domain). It shows that an integral around an outer contour is equal to the integral around an inner contour, provided the region between them is analytic.

**Step 1: Define the geometry.**
*   Let $C_1$ be the outer closed curve, traversed counter-clockwise (positive sense).
*   Let $C_2$ be the inner closed curve, also traversed counter-clockwise (positive sense).
*   The region $\mathcal{R}$ is the "donut-shaped" (annular) region between $C_1$ and $C_2$. We are given that $f(z)$ is analytic throughout $\mathcal{R}$ and on its boundaries.

**Step 2: Create a single simply connected contour.**
Cauchy's Integral Theorem ($\oint f(z)dz = 0$) only applies to simply connected regions (regions with no holes).
To apply it, we introduce a straight-line "cross-cut" (let's call it $L$) connecting a point on the outer curve $C_1$ to a point on the inner curve $C_2$.

We now define a new, continuous master contour $\Gamma$ that traces the entire boundary of the region $\mathcal{R}$ without crossing the hole:
1.  Traverse $C_1$ in the positive (counter-clockwise) direction.
2.  Travel inward along the cross-cut $L$ from $C_1$ to $C_2$. Let's denote this path as $L_{in}$.
3.  Traverse the inner curve $C_2$ in the **negative (clockwise)** direction to keep the region $\mathcal{R}$ to our left. We denote this path as $-C_2$.
4.  Travel outward along the exact same cross-cut $L$ back to $C_1$. We denote this path as $L_{out}$.

**Step 3: Apply Cauchy's Integral Theorem to $\Gamma$.**
The new contour $\Gamma$ bounds a simply connected region where $f(z)$ is completely analytic.
Therefore, by Cauchy's Integral Theorem:
$$\oint_\Gamma f(z) dz = 0$$

Let's break down the components of $\Gamma$:
$$\oint_{C_1} f(z)dz + \int_{L_{in}} f(z)dz + \oint_{-C_2} f(z)dz + \int_{L_{out}} f(z)dz = 0$$

**Step 4: Cancel the cross-cut integrals.**
Because the path $L_{out}$ is exactly the reverse of path $L_{in}$, their line integrals are exact negatives of each other:
$$\int_{L_{out}} f(z)dz = - \int_{L_{in}} f(z)dz$$
Therefore, they cancel each other out in our equation:
$$\oint_{C_1} f(z)dz + \oint_{-C_2} f(z)dz = 0$$

**Step 5: Rearrange using directional properties.**
Reversing the direction of a line integral negates its value. Therefore, the integral over the clockwise path $-C_2$ is the negative of the integral over the counter-clockwise path $C_2$:
$$\oint_{-C_2} f(z)dz = -\oint_{C_2} f(z)dz$$

Substitute this into the equation:
$$\oint_{C_1} f(z)dz - \oint_{C_2} f(z)dz = 0$$

Move the negative term to the other side:
$$\oint_{C_1} f(z)dz = \oint_{C_2} f(z)dz$$
**(Proved)**

***

### Q283. Problem 4.4.3: Evaluate $\oint_{C}\frac{dz}{z-a}$ where C is any simple closed curve C and $z=a$ is (i) outside C (ii) inside C.

**Solution:**

Evaluate $I = \oint_C \frac{1}{z-a} dz$.

**Part (i): Evaluate if $z = a$ is OUTSIDE $C$**
1.  **Check analyticity:** The integrand $f(z) = \frac{1}{z-a}$ has a simple pole at $z = a$.
2.  Because the point $z = a$ lies strictly *outside* the simple closed curve $C$, the function $f(z)$ is perfectly analytic everywhere inside and on $C$.
3.  **Apply Cauchy's Integral Theorem:** Since $f(z)$ is analytic inside and on $C$, its contour integral evaluates to zero.
**Answer (i): $0$**

---

**Part (ii): Evaluate if $z = a$ is INSIDE $C$**
1.  **Apply Cauchy's Integral Formula:** The formula states $\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$.
2.  Here, our analytic numerator function is simply the constant $1$, so $f(z) = 1$.
3.  Because $z=a$ is inside $C$, we apply the formula directly:
    $$I = 2\pi i \cdot f(a) = 2\pi i \cdot (1) = 2\pi i$$

*(Alternatively, parameterize a small circle $|z-a|=r \implies z = a+re^{i\theta}, dz=ire^{i\theta}d\theta$. $\int_0^{2\pi} \frac{ire^{i\theta}}{re^{i\theta}}d\theta = \int_0^{2\pi} i d\theta = 2\pi i$. This holds regardless of contour shape via the deformation principle proved in Q282).*
**Answer (ii): $2\pi i$**

***

### Q284. Problem 4.4.4: Find the value of $\int_{C}(z^{2}+2z+1)dz$ where C is the circle $|z|=1$.

**Solution:**

We evaluate the complex contour integral $I = \oint_C (z^2+2z+1)dz$ around the unit circle.

**Step 1: Analyze the integrand.**
The function $f(z) = z^2 + 2z + 1$ is a polynomial.
Polynomial functions contain no division by zero, no non-integer roots, and no logarithms. Therefore, they possess no singularities anywhere in the complex plane. 
Because it is differentiable everywhere, $f(z)$ is an **entire function** (it is analytic everywhere).

**Step 2: Apply the relevant theorem.**
Cauchy's Integral Theorem dictates that if a function $f(z)$ is analytic everywhere inside and on a simple closed contour $C$, the integral over that contour is strictly zero:
$$\oint_C f(z) dz = 0$$

Because $f(z) = z^2+2z+1$ is analytic everywhere, it trivially satisfies the condition of being analytic inside and on the unit circle $|z|=1$.

**Answer:** The value of the integral is **$0$**.

Here are the detailed solutions for the next four questions (Q285 to Q288).

### Q285. Problem 4.4.5: Evaluate $\int_{C}\frac{1}{2z-3}dz$ where C is $|z|=1$

**Solution:**

We need to evaluate the contour integral $I = \oint_C \frac{1}{2z-3} dz$.

**Step 1: Identify the singularity.**
Set the denominator equal to zero to find the pole:
$$2z - 3 = 0$$
$$2z = 3$$
$$z = \frac{3}{2} = 1.5$$
The function has a simple pole at $z = 1.5$.

**Step 2: Check if the singularity is enclosed by the contour.**
The contour $C$ is defined by $|z| = 1$. This is a circle centered at the origin with a radius of $1$.
The pole is located at $z = 1.5$ on the real axis.
Since the distance from the origin to the pole is $|1.5| = 1.5$, and $1.5 > 1$ (the radius of the contour), the pole lies strictly **outside** the contour $C$.

**Step 3: Apply the relevant theorem.**
Because the only singularity of the function lies completely outside the contour, the function $f(z) = \frac{1}{2z-3}$ is completely analytic everywhere inside and on the boundary of the contour $C$.

According to **Cauchy's Integral Theorem**, the contour integral of any analytic function around a closed path is exactly zero.

**Answer:** **$0$**

***

### Q286. Problem 4.4.6: Evaluate $\frac{1}{2\pi~i}\oint_{C}\frac{e^{z}}{(z-2)}dz$ , where C is the circle $|z|=1$,

**Solution:**

We need to evaluate the expression $I = \frac{1}{2\pi i} \oint_C \frac{e^z}{z-2} dz$.

**Step 1: Identify the singularity.**
The integrand function is $F(z) = \frac{e^z}{z-2}$.
The denominator becomes zero at $z - 2 = 0 \implies z = 2$.
Therefore, there is a simple pole at $z = 2$. (The numerator $e^z$ is analytic everywhere).

**Step 2: Check if the singularity is enclosed by the contour.**
The contour $C$ is the unit circle, defined by $|z| = 1$.
The distance of the pole from the origin is $|2| = 2$.
Since $2 > 1$, the pole $z = 2$ lies strictly **outside** the contour $C$.

**Step 3: Apply the relevant theorem.**
Because the only singularity lies outside the contour, the entire integrand $F(z) = \frac{e^z}{z-2}$ is perfectly analytic everywhere inside and on the simple closed curve $C$.

By **Cauchy's Integral Theorem**, the integral of an analytic function around a closed contour is zero:
$$\oint_C \frac{e^z}{z-2} dz = 0$$

Therefore, multiplying this result by the constant factor in front:
$$I = \frac{1}{2\pi i} \cdot (0) = 0$$

**Answer:** **$0$**

***

### Q287. Problem 4.4.7: Evaluate $\oint_{C}\frac{dz}{(z-a)^{n}},n=2,3,4,...$ where $z=a$ is inside the simple closed curve C.

**Solution:**

We must evaluate the contour integral $I_n = \oint_C \frac{1}{(z-a)^n} dz$ where $n \ge 2$ is an integer, and the pole $z=a$ lies inside $C$.

**Method 1: Using the Generalized Cauchy Integral Formula**
The Generalized Cauchy Integral Formula for a pole of higher order is:
$$\oint_C \frac{f(z)}{(z-a)^{m+1}} dz = \frac{2\pi i}{m!} f^{(m)}(a)$$

Let's match our integral to the formula:
*   Numerator function: $f(z) = 1$. This is a constant function, meaning it is analytic everywhere.
*   Power matching: Let $m+1 = n$. Therefore, $m = n - 1$.
    Because the problem states $n \ge 2$ ($n=2, 3, 4\dots$), $m$ must be a positive integer $m \ge 1$.

We need the $m$-th derivative of the numerator $f(z)$.
Since $f(z) = 1$ is a constant, its first derivative is $0$: $f'(z) = 0$.
Consequently, all subsequent higher-order derivatives are also $0$.
$$f^{(m)}(z) = 0 \quad \text{for all } m \ge 1$$

Evaluating the $m$-th derivative at the point $a$:
$$f^{(m)}(a) = 0$$

Substitute this into the Generalized Formula:
$$I_n = \frac{2\pi i}{(n-1)!} \cdot 0$$
$$I_n = 0$$

---
**Method 2: Direct Parameterization (Formal Proof)**
By the Principle of Deformation of Contours, we can shrink $C$ to a small circle $C_r$ of radius $r$ centered at $a$.
Parameterize $C_r$: $z - a = r e^{i\theta} \implies z = a + r e^{i\theta}$, where $\theta$ goes from $0$ to $2\pi$.
The differential is $dz = ir e^{i\theta} d\theta$.

Substitute into the integral:
$$I_n = \int_0^{2\pi} \frac{1}{(r e^{i\theta})^n} (ir e^{i\theta} d\theta)$$
$$I_n = \int_0^{2\pi} \frac{ir e^{i\theta}}{r^n e^{in\theta}} d\theta$$
Combine the $r$ and exponential terms:
$$I_n = \int_0^{2\pi} ir^{1-n} e^{i\theta(1-n)} d\theta$$
Pull the constants ($i$ and $r^{1-n}$) out of the integral:
$$I_n = ir^{1-n} \int_0^{2\pi} e^{i(1-n)\theta} d\theta$$

Now evaluate the integral with respect to $\theta$. Because $n \ge 2$, the term $(1-n)$ is a non-zero integer. Let $k = 1-n$.
$$I_n = ir^k \left[ \frac{e^{ik\theta}}{ik} \right]_0^{2\pi}$$
Cancel the $i$:
$$I_n = \frac{r^k}{k} \left( e^{ik(2\pi)} - e^{ik(0)} \right)$$
$$I_n = \frac{r^k}{k} \left( e^{i2k\pi} - e^0 \right)$$
For any integer $k$, $e^{i2k\pi} = \cos(2k\pi) + i\sin(2k\pi) = 1 + i(0) = 1$. Also, $e^0 = 1$.
$$I_n = \frac{r^k}{k} (1 - 1) = \frac{r^k}{k} (0) = 0$$

**Answer:** The value of the integral is **$0$**.

***

### Q288. Problem 4.4.9: A force field is given by $F=3z+5$ Find the work done in moving an object in this force field along the parabola $z=t^{2}+it$ from $z=0$ to $z=4+2i.$

**Solution:**

In complex physics applications, the work done by a complex force field $F(z)$ moving an object along a path $C$ is calculated as the complex line integral:
$$W = \int_C F(z) dz$$
Here, $F(z) = 3z + 5$ and the path is parameterized by $z(t) = t^2 + it$.

**Method 1: Direct Parameterization**
**Step 1: Find the parameter limits for $t$.**
*   Start point: $z = 0 \implies t^2 + it = 0 \implies t = 0$.
*   End point: $z = 4 + 2i$. Equating the imaginary parts: $it = 2i \implies t = 2$.
    *(Checking the real part: $t^2 = 2^2 = 4$. This matches).*
The integration limits for $t$ are from $0$ to $2$.

**Step 2: Find the differential $dz$.**
$$z = t^2 + it \implies dz = \frac{dz}{dt}dt = (2t + i) dt$$

**Step 3: Substitute into the integral.**
Substitute $z$ into the force field:
$$F(z) = 3(t^2 + it) + 5 = 3t^2 + 5 + 3it$$

Set up the integral:
$$W = \int_0^2 (3t^2 + 5 + 3it) (2t + i) dt$$

**Step 4: Expand the integrand using FOIL.**
$$(3t^2 + 5 + 3it) (2t + i) = 3t^2(2t) + 3t^2(i) + 5(2t) + 5(i) + 3it(2t) + 3it(i)$$
$$= 6t^3 + 3it^2 + 10t + 5i + 6it^2 + 3i^2t$$
Since $i^2 = -1$, the last term becomes $-3t$:
$$= 6t^3 + 3it^2 + 10t + 5i + 6it^2 - 3t$$
Group into real and imaginary polynomials:
$$= (6t^3 + 7t) + i(9t^2 + 5)$$

**Step 5: Evaluate the definite integral.**
$$W = \int_0^2 \left[ (6t^3 + 7t) + i(9t^2 + 5) \right] dt$$
Integrate term by term:
$$W = \left[ \frac{6t^4}{4} + \frac{7t^2}{2} + i\left(\frac{9t^3}{3} + 5t\right) \right]_0^2$$
$$W = \left[ \frac{3}{2}t^4 + \frac{7}{2}t^2 + i(3t^3 + 5t) \right]_0^2$$

Substitute the upper limit $t=2$ (the lower limit $0$ just yields $0$):
$$W = \left( \frac{3}{2}(16) + \frac{7}{2}(4) \right) + i\left( 3(8) + 5(2) \right)$$
$$W = (24 + 14) + i(24 + 10)$$
$$W = 38 + 34i$$

---
**Method 2: Fundamental Theorem of Calculus (Because the field is conservative)**
Notice that the force field $F(z) = 3z + 5$ is a polynomial. Therefore, it is an analytic (entire) function.
Because it is analytic, the integral is path-independent (the field is conservative). We can simply evaluate it using the antiderivative, ignoring the parameterization $z(t)$ entirely.

1.  Find the antiderivative: $\Phi(z) = \int (3z+5) dz = \frac{3z^2}{2} + 5z$.
2.  Evaluate at upper limit $z_{end} = 4+2i$:
    $$z^2 = (4+2i)^2 = 16 + 16i + 4i^2 = 16 + 16i - 4 = 12 + 16i$$
    $$\Phi(4+2i) = \frac{3(12+16i)}{2} + 5(4+2i) = \frac{36+48i}{2} + 20 + 10i = 18 + 24i + 20 + 10i = 38 + 34i$$
3.  Evaluate at lower limit $z_{start} = 0$:
    $$\Phi(0) = \frac{3(0)^2}{2} + 5(0) = 0$$
4.  Subtract:
    $$W = \Phi(4+2i) - \Phi(0) = 38 + 34i - 0 = 38 + 34i$$

Both methods yield the exact same answer, confirming the result.

**Answer:** The total work done is **$38 + 34i$**.


Here are the detailed solutions for the next four questions (Q289 to Q292).

### Q289. Question (5.1): Cauchy's Integral formula : If $f(z)$ is analytic inside and on the boundary C of simply connected region R except at the point a inside C, prove that Cauchy's integral formula $f(a)=\frac{1}{2\pi i}\oint_{C}\frac{f(z)}{z-a}dz$ .

*(Correction Note: The phrasing in the source text contains a slight inaccuracy common in copied notes. For Cauchy's Integral Formula to work, the function $f(z)$ must be completely analytic **everywhere** inside and on $C$, including at the point $a$. It is the quotient function $\frac{f(z)}{z-a}$ that has a singularity at $a$. We will prove the standard, mathematically correct theorem).*

**Solution:**

**Theorem Statement:** If $f(z)$ is analytic everywhere inside and on a simple closed contour $C$ (traversed counter-clockwise), and $a$ is any interior point within $C$, then $f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - a} dz$.

**Proof:**

**Step 1: Isolate the singularity.**
We construct a new function $F(z) = \frac{f(z)}{z-a}$. This function is analytic everywhere inside $C$ except at $z=a$ (because division by zero is undefined).
To safely evaluate the integral, we isolate this singularity. We draw a small circle $C_r$ centered at $a$ with a very small radius $r$, such that $C_r$ lies entirely inside the region bounded by $C$.

**Step 2: Apply the Principle of Deformation of Contours.**
The region located *between* the outer contour $C$ and the inner circle $C_r$ contains no singularities. Therefore, $F(z)$ is perfectly analytic in this "donut-shaped" region.
By the principle of deformation (an extension of Cauchy's Integral Theorem for multiply connected domains), the contour integral around the outer boundary equals the integral around the inner boundary:
$$\oint_C \frac{f(z)}{z-a} dz = \oint_{C_r} \frac{f(z)}{z-a} dz$$

**Step 3: Parameterize the inner circle $C_r$.**
The equation of the circle $C_r$ is $|z-a| = r$.
In polar exponential form, any point on this circle can be represented as:
$$z - a = r e^{i\theta} \implies z = a + r e^{i\theta}$$
where the angle $\theta$ ranges from $0$ to $2\pi$ to trace the full circle counter-clockwise.
The differential $dz$ is:
$$dz = \frac{d}{d\theta}(a + r e^{i\theta}) d\theta = i r e^{i\theta} d\theta$$

**Step 4: Substitute the parameterization into the integral.**
Replace $z$, $(z-a)$, and $dz$ in the right-hand side integral:
$$\oint_{C_r} \frac{f(z)}{z-a} dz = \int_0^{2\pi} \frac{f(a + r e^{i\theta})}{r e^{i\theta}} (i r e^{i\theta} d\theta)$$

Cancel the common term $r e^{i\theta}$ from the numerator and denominator:
$$= \int_0^{2\pi} f(a + r e^{i\theta}) \cdot i \ d\theta$$
$$= i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta$$

**Step 5: Take the limit as the radius shrinks to zero ($r \to 0$).**
Because the equation holds for *any* arbitrarily small radius $r$, it must hold in the limit as $r \to 0$.
$$\oint_C \frac{f(z)}{z-a} dz = \lim_{r \to 0} \left[ i \int_0^{2\pi} f(a + r e^{i\theta}) d\theta \right]$$

Since $f(z)$ is an analytic function, it is by definition continuous. This continuity allows us to pass the limit inside the integral.
As $r \to 0$, the term $r e^{i\theta} \to 0$. Thus, $f(a + r e^{i\theta}) \to f(a)$.
$$= i \int_0^{2\pi} f(a) d\theta$$

**Step 6: Evaluate the final integral.**
Because $f(a)$ evaluates to a specific complex constant, it does not depend on $\theta$ and can be pulled outside the integral:
$$= i f(a) \int_0^{2\pi} 1 \ d\theta$$
$$= i f(a) [\theta]_0^{2\pi}$$
$$= i f(a) (2\pi - 0) = 2\pi i f(a)$$

**Step 7: Final algebraic rearrangement.**
We have established that:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i f(a)$$
Divide both sides by $2\pi i$ to isolate $f(a)$:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
**(Proved)**

***

### Q290. Question: Derivative of Cauchy's Integral formula : Proof: Yourself (1) $f^{\prime}(a)=\frac{1}{2\pi i}\oint_{C}\frac{f(z)}{(z-a)^{2}}dz$ (2) $f^{(n)}(a)=\frac{n!}{2\pi i}\oint_{C}\frac{f(z)}{(z-a)^{n+1}}dz$

**Solution:**

We will prove the first derivative formula from first principles (the limit definition of a derivative) and then demonstrate how it generalizes.

**Proof of (1): $f^{\prime}(a)=\frac{1}{2\pi i}\oint_{C}\frac{f(z)}{(z-a)^{2}}dz$**

**Step 1: Set up the limit definition of the derivative.**
The derivative of $f(z)$ at the point $a$ is defined as:
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

**Step 2: Apply Cauchy's Integral Formula to $f(a+h)$ and $f(a)$.**
From Cauchy's Integral Formula (proven in Q289), we know:
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
Similarly, for a point $(a+h)$ that is also inside $C$:
$$f(a+h) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - (a+h)} dz$$

**Step 3: Construct the difference quotient.**
Substitute these integral expressions into the numerator of the limit definition:
$$f(a+h) - f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a-h} dz - \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
Combine them into a single integral by factoring out $\frac{1}{2\pi i} f(z)$:
$$f(a+h) - f(a) = \frac{1}{2\pi i} \oint_C f(z) \left[ \frac{1}{z-a-h} - \frac{1}{z-a} \right] dz$$

**Step 4: Find a common denominator for the bracketed term.**
$$\frac{1}{z-a-h} - \frac{1}{z-a} = \frac{(z-a) - (z-a-h)}{(z-a-h)(z-a)}$$
$$= \frac{z - a - z + a + h}{(z-a-h)(z-a)} = \frac{h}{(z-a-h)(z-a)}$$

Substitute this back into the integral difference:
$$f(a+h) - f(a) = \frac{1}{2\pi i} \oint_C f(z) \frac{h}{(z-a-h)(z-a)} dz$$

**Step 5: Divide by $h$ and take the limit.**
Now, divide the entire expression by $h$:
$$\frac{f(a+h) - f(a)}{h} = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a-h)(z-a)} dz$$

Take the limit as $h \to 0$:
$$f'(a) = \lim_{h \to 0} \left[ \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a-h)(z-a)} dz \right]$$

Because $f(z)$ is continuous on the contour $C$, and the contour does not pass through the point $a$ (so the denominator is never zero), we are permitted to bring the limit inside the integral operator:
$$f'(a) = \frac{1}{2\pi i} \oint_C \lim_{h \to 0} \left[ \frac{f(z)}{(z-a-h)(z-a)} \right] dz$$
As $h \to 0$, the term $(z-a-h)$ simply becomes $(z-a)$.
$$f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)(z-a)} dz$$
$$f'(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2} dz$$
**(Proved (1))**

---

**Proof Outline for (2): $f^{(n)}(a)=\frac{n!}{2\pi i}\oint_{C}\frac{f(z)}{(z-a)^{n+1}}dz$**

This generalized formula is known as the **Generalized Cauchy Integral Formula**. 
A highly elegant way to prove this is through Leibniz's rule, which allows us to differentiate an integral with respect to a parameter under the integral sign.

1.  Start with Cauchy's Integral Formula:
    $$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$
2.  Take the first derivative with respect to the parameter $a$ on both sides. Differentiate the integrand directly with respect to $a$:
    $$\frac{d}{da} [f(a)] = \frac{1}{2\pi i} \oint_C f(z) \frac{d}{da} \left[ (z-a)^{-1} \right] dz$$
    $$f'(a) = \frac{1}{2\pi i} \oint_C f(z) \left[ -1(z-a)^{-2}(-1) \right] dz = \frac{1}{2\pi i} \oint_C \frac{f(z)}{(z-a)^2} dz$$
    *(This perfectly matches our rigorous proof for part 1).*
3.  Take the second derivative with respect to $a$:
    $$f''(a) = \frac{d}{da}[f'(a)] = \frac{1}{2\pi i} \oint_C f(z) \frac{d}{da} \left[ (z-a)^{-2} \right] dz$$
    $$f''(a) = \frac{1}{2\pi i} \oint_C f(z) \left[ -2(z-a)^{-3}(-1) \right] dz = \frac{2}{2\pi i} \oint_C \frac{f(z)}{(z-a)^3} dz$$
4.  Take the third derivative:
    $$f'''(a) = \frac{d}{da}[f''(a)] = \frac{2}{2\pi i} \oint_C f(z) \frac{d}{da} \left[ (z-a)^{-3} \right] dz$$
    $$f'''(a) = \frac{2}{2\pi i} \oint_C f(z) \left[ -3(z-a)^{-4}(-1) \right] dz = \frac{3 \times 2}{2\pi i} \oint_C \frac{f(z)}{(z-a)^4} dz = \frac{3!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^4} dz$$
5.  By continuing this differentiation $n$ times (which can be formalized via mathematical induction), every time we take a derivative, the power in the denominator increases by $1$, and the new power drops down into the numerator, forming a factorial pattern $n \times (n-1) \times (n-2) \dots = n!$.
    This directly yields the formula:
    **$f^{(n)}(a) = \frac{n!}{2\pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}} dz$**
**(Proved (2))**

***

### Q291. Problem 5.1.1: Evaluate $\frac{1}{2\pi~i}\oint_{C}\frac{e^{z}}{(z-2)}dz$ , where C is the circle (i) $|z|=3$, (ii) $|z|=1$.

*(Note: The integrals themselves are identical to Q255, but note the explicit coefficient $\frac{1}{2\pi i}$ sitting in front of the integral in this version of the problem).*

**Solution:**

We need to evaluate the expression $I = \frac{1}{2\pi i} \oint_C \frac{e^z}{z-2} dz$.

**Step 1: Identify the singularity and analytic numerator.**
Set the denominator to zero:
$$z - 2 = 0 \implies z = 2$$
There is a simple pole at $z = 2$.
The numerator function is $f(z) = e^z$, which is an entire function (analytic everywhere).

---
**Part (i): Contour C is $|z| = 3$**
1.  **Check enclosure:** The contour is a circle of radius 3 centered at the origin.
    The distance to the pole is $|2| = 2$.
    Since $2 < 3$, the pole $z = 2$ lies strictly **inside** the contour.
2.  **Apply Cauchy's Integral Formula:**
    The standard formula states:
    $$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
    Rearranging this by dividing both sides by $2\pi i$ gives:
    $$\frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz = f(a)$$
    Notice that the left side of this rearranged equation perfectly matches the expression we are asked to evaluate.
3.  **Evaluate $f(a)$:**
    Here, $a = 2$ and $f(z) = e^z$.
    $$I = f(2) = e^2$$
**Answer (i): $e^2$**

---
**Part (ii): Contour C is $|z| = 1$**
1.  **Check enclosure:** The contour is a circle of radius 1 centered at the origin.
    The distance to the pole is $|2| = 2$.
    Since $2 > 1$, the pole $z = 2$ lies strictly **outside** the contour.
2.  **Apply Cauchy's Integral Theorem:**
    Because the only singularity lies completely outside the contour, the entire integrand $F(z) = \frac{e^z}{z-2}$ is analytic everywhere inside and on the contour $C$.
    By Cauchy's Integral Theorem, the integral of an analytic function around a closed path is zero:
    $$\oint_C \frac{e^z}{z-2} dz = 0$$
3.  **Calculate final result:**
    Multiply by the constant in front:
    $$I = \frac{1}{2\pi i} (0) = 0$$
**Answer (ii): $0$**

***

### Q292. Problem 5.1.2: Evaluate $\oint_{C}\frac{e^{2z}}{(z+1)^{4}}dz$ , where C is the circle $|z|=3$

*(Note: This is numerically and conceptually identical to Q256. A concise step-by-step solution is provided below).*

**Solution:**

Let $I = \oint_C \frac{e^{2z}}{(z+1)^4} dz$.

**Step 1: Identify the singularity and analytic numerator.**
Set the denominator to zero:
$$(z+1)^4 = 0 \implies z = -1$$
There is a **pole of order 4** at $z = -1$.
The numerator function is $f(z) = e^{2z}$, which is analytic everywhere.

**Step 2: Check enclosure.**
The contour $C$ is a circle of radius 3 centered at the origin ($|z| = 3$).
The distance to the pole is $|-1| = 1$.
Since $1 < 3$, the pole $z = -1$ lies **inside** the contour.

**Step 3: Apply the Generalized Cauchy Integral Formula.**
The formula for higher-order poles is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map our parameters to the formula:
*   $a = -1$
*   $n+1 = 4 \implies n = 3$. We need the third derivative of the numerator.
*   $f(z) = e^{2z}$

**Step 4: Calculate the derivatives.**
*   $f(z) = e^{2z}$
*   $f'(z) = 2e^{2z}$
*   $f''(z) = 4e^{2z}$
*   $f'''(z) = 8e^{2z}$

**Step 5: Evaluate $f'''(a)$.**
Substitute $a = -1$:
$$f'''(-1) = 8e^{2(-1)} = 8e^{-2}$$

**Step 6: Final calculation.**
Substitute this value into the generalized formula:
$$I = \frac{2\pi i}{3!} (8e^{-2})$$
Since $3! = 3 \times 2 \times 1 = 6$:
$$I = \frac{2\pi i}{6} (8e^{-2})$$
$$I = \frac{\pi i}{3} (8e^{-2})$$
$$I = \frac{8\pi i}{3 e^2}$$

**Answer:** The value of the integral is **$\frac{8\pi i}{3e^2}$** (or **$\frac{8\pi i e^{-2}}{3}$**).


Here are the detailed solutions for the next four questions (Q293 to Q296).

*(Note: Questions Q293, Q294, Q295, and Q296 from the Feruj Sheet are numerically and conceptually identical to questions solved earlier from the Firoz Note section. Detailed step-by-step solutions are provided again below for completeness).*

### Q293. Problem 5.1.3: Evaluate $\oint_{C}\frac{e^{iz}}{z^{3}}dz$ , where C is the circle $|z|=2$.

*(This is identical to Q257).*

**Solution:**

Let $I = \oint_C \frac{e^{iz}}{z^3} dz$.

**Step 1: Identify the singularity and analytic numerator.**
Set the denominator to zero:
$$z^3 = 0 \implies z = 0$$
This indicates a **pole of order 3** at the origin ($z=0$).
The numerator function is $f(z) = e^{iz}$. Exponential functions are entire, so $f(z)$ is analytic everywhere.

**Step 2: Check enclosure.**
The contour $C$ is defined by $|z| = 2$. This is a circle of radius 2 centered at the origin.
The pole is exactly at the origin ($z=0$).
Since $|0| = 0 < 2$, the pole lies safely **inside** the contour $C$.

**Step 3: Apply the Generalized Cauchy Integral Formula.**
For a higher-order pole, the formula is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map our parameters to the formula:
*   $a = 0$
*   $n+1 = 3 \implies n = 2$. We need to find the **second derivative** of $f(z)$.

**Step 4: Calculate the derivatives.**
*   $f(z) = e^{iz}$
*   First derivative: $f'(z) = i e^{iz}$
*   Second derivative: $f''(z) = i^2 e^{iz}$. Since $i^2 = -1$:
    $$f''(z) = -e^{iz}$$

**Step 5: Evaluate $f''(a)$.**
Substitute $a = 0$ into our second derivative:
$$f''(0) = -e^{i(0)} = -e^0 = -1$$

**Step 6: Final calculation.**
Substitute everything into the generalized formula:
$$I = \frac{2\pi i}{2!} (-1)$$
Since $2! = 2 \times 1 = 2$:
$$I = \frac{2\pi i}{2} (-1)$$
$$I = -\pi i$$

**Answer:** The value of the integral is **$-\pi i$**.

***

### Q294. Problem 5.1.4: Evaluate $\oint_{C}\frac{1}{z(z-2)^{4}}dz$ , where C is the circle $|z|=1$.

*(This is identical to Q258).*

**Solution:**

Let $I = \oint_C \frac{1}{z(z-2)^4} dz$.

**Step 1: Identify all singularities.**
Set the denominator to zero:
$$z(z-2)^4 = 0$$
This yields two singular points:
1.  $z_1 = 0$ (a simple pole, order 1).
2.  $z_2 = 2$ (a pole of order 4).

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is defined by $|z| = 1$ (a circle of radius 1 centered at the origin).
*   **Test $z_1 = 0$:** $|0| = 0 < 1$. This pole lies **inside** the contour.
*   **Test $z_2 = 2$:** $|2| = 2 > 1$. This pole lies strictly **outside** the contour.

Only the simple pole at $z=0$ is enclosed by $C$.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z=0$ is enclosed, we must isolate $z$ in the denominator and move the rest of the function into the numerator. This new numerator function will be entirely analytic inside and on the contour because the singularity at $z=2$ is excluded.
$$I = \oint_C \frac{ \left( \frac{1}{(z-2)^4} \right) }{z} dz$$
Let the analytic numerator function be $f(z) = \frac{1}{(z-2)^4}$. 

**Step 4: Apply Cauchy's Integral Formula.**
Since the enclosed pole is simple (order 1), we use the standard formula:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 0$.
$$I = 2\pi i \cdot f(0)$$

**Step 5: Evaluate $f(0)$.**
Substitute $z = 0$ into our numerator function:
$$f(0) = \frac{1}{(0 - 2)^4} = \frac{1}{(-2)^4} = \frac{1}{16}$$

**Step 6: Final calculation.**
Substitute into the formula:
$$I = 2\pi i \left( \frac{1}{16} \right)$$
$$I = \frac{2\pi i}{16}$$
$$I = \frac{\pi i}{8}$$

**Answer:** The value of the integral is **$\frac{\pi i}{8}$**.

***

### Q295. Problem 5.1.5: Evaluate $\oint_{C}\frac{z+4}{z^{2}+2z+5}dz$ , where C is the circle $|z+1-i|=2$

*(This is identical to Q259).*

**Solution:**

Let $I = \oint_C \frac{z+4}{z^2+2z+5} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator:
$$z^2 + 2z + 5 = 0$$
Using the quadratic formula:
$$z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$$
There are two simple poles:
1.  $z_1 = -1 + 2i$
2.  $z_2 = -1 - 2i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is $|z+1-i| = 2$.
Rewrite this in standard form: $|z - (-1+i)| = 2$. This is a circle centered at $z = -1+i$ with a radius of $2$.

*   **Test $z_1 = -1+2i$:**
    Substitute into the contour equation's left side:
    $|(-1+2i) - (-1+i)| = |-1 + 2i + 1 - i| = |i| = 1$
    Since $1 < 2$, the pole $z_1 = -1+2i$ is **inside** the contour.

*   **Test $z_2 = -1-2i$:**
    Substitute into the contour equation's left side:
    $|(-1-2i) - (-1+i)| = |-1 - 2i + 1 - i| = |-3i| = 3$
    Since $3 > 2$, the pole $z_2 = -1-2i$ is strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_1 = -1+2i$ is enclosed, we isolate the factor $(z - (-1+2i))$ in the denominator and push the other factor into the numerator.
The factored denominator is $(z - (-1+2i))(z - (-1-2i))$.
$$I = \oint_C \frac{\left( \frac{z+4}{z - (-1-2i)} \right)}{z - (-1+2i)} dz$$
Let the analytic numerator function be $f(z) = \frac{z+4}{z+1+2i}$.

**Step 4: Apply Cauchy's Integral Formula.**
$$I = 2\pi i \cdot f(-1+2i)$$

**Step 5: Evaluate $f(-1+2i)$.**
$$f(-1+2i) = \frac{(-1+2i) + 4}{(-1+2i) + 1 + 2i}$$
$$f(-1+2i) = \frac{3 + 2i}{4i}$$

**Step 6: Final calculation.**
$$I = 2\pi i \left( \frac{3 + 2i}{4i} \right)$$
The $i$ terms cancel out, and $2/4$ simplifies to $1/2$:
$$I = \frac{2\pi(3 + 2i)}{4}$$
$$I = \frac{\pi(3 + 2i)}{2}$$

**Answer:** The value of the integral is **$\frac{\pi}{2}(3 + 2i)$** (or **$\frac{3\pi}{2} + \pi i$**).

***

### Q296. Problem 5.1.6: Evaluate $\int_{C}\frac{3z^{2}+z}{z^{2}-1}dz$ where C is the circle $|z-1|=1$

*(This is identical to Q245).*

**Solution:**

Let $I = \oint_C \frac{3z^2+z}{z^2-1} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero:
$$z^2 - 1 = 0 \implies (z-1)(z+1) = 0$$
There are two simple poles:
1.  $z_1 = 1$
2.  $z_2 = -1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z-1| = 1$. This circle is centered at $z=1$ with a radius of $1$.
*   **Test $z_1 = 1$:** $|1 - 1| = 0 < 1$. This pole is the exact center of the circle, so it is **inside**.
*   **Test $z_2 = -1$:** $|-1 - 1| = |-2| = 2$. Since $2 > 1$, this pole lies strictly **outside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Only $z=1$ is inside the contour. We isolate the factor $(z-1)$ in the denominator and group the rest of the expression to form the analytic numerator function $f(z)$.
$$I = \oint_C \frac{ \left( \frac{3z^2+z}{z+1} \right) }{z-1} dz$$
Let the analytic numerator function be $f(z) = \frac{3z^2+z}{z+1}$.

**Step 4: Apply Cauchy's Integral Formula.**
The formula for a simple pole is:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 1$.
$$I = 2\pi i \cdot f(1)$$

**Step 5: Evaluate $f(1)$.**
$$f(1) = \frac{3(1)^2 + 1}{1 + 1} = \frac{3 + 1}{2} = \frac{4}{2} = 2$$

**Step 6: Final calculation.**
$$I = 2\pi i (2)$$
$$I = 4\pi i$$

**Answer:** The value of the integral is **$4\pi i$**.

Here are the detailed solutions for the next four questions (Q297 to Q300).

### Q297. Problem 5.1.7: Evaluate $\int_{C}\frac{z+1}{(z-3)(z-1)}dz,$ where C is $|z|=2$

**Solution:**

Let $I = \oint_C \frac{z+1}{(z-3)(z-1)} dz$.

**Step 1: Identify the singularities.**
The denominator is already factored: $(z-3)(z-1) = 0$.
There are two simple poles:
1.  $z_1 = 3$
2.  $z_2 = 1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 2$. It is centered at the origin with a radius of $2$.
*   **Test $z_1 = 3$:** $|3| = 3 > 2$. This pole lies strictly **outside** the contour.
*   **Test $z_2 = 1$:** $|1| = 1 < 2$. This pole lies **inside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only the pole at $z=1$ is enclosed by $C$, we must isolate $(z-1)$ in the denominator. The rest of the function becomes the analytic numerator $f(z)$.
$$I = \oint_C \frac{ \left( \frac{z+1}{z-3} \right) }{z-1} dz$$
Let $f(z) = \frac{z+1}{z-3}$. This function is perfectly analytic everywhere inside and on $C$ because its only singularity ($z=3$) is outside the contour.

**Step 4: Apply Cauchy's Integral Formula.**
The formula for a simple pole is:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 1$.
$$I = 2\pi i \cdot f(1)$$

**Step 5: Evaluate $f(1)$.**
Substitute $z = 1$ into our numerator function:
$$f(1) = \frac{1 + 1}{1 - 3} = \frac{2}{-2} = -1$$

**Step 6: Calculate final result.**
$$I = 2\pi i (-1)$$
$$I = -2\pi i$$

**Answer:** The value of the integral is **$-2\pi i$**.

***

### Q298. Problem 5.1.8: Evaluate $\int_{c}\frac{z+4}{z^{2}+2z+5}$ Where C is the circle $(i)|z+1+i|=2$ $(ii)|z+1-i|=2$ (iii) $|z|=1$

**Solution:**

Let $I = \oint_C \frac{z+4}{z^2+2z+5} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator (as solved previously in Q259/Q295):
$$z^2 + 2z + 5 = 0 \implies z = \frac{-2 \pm \sqrt{-16}}{2} = -1 \pm 2i$$
The two simple poles are $z_1 = -1 + 2i$ and $z_2 = -1 - 2i$.

---
**Part (i): Contour is $|z+1+i| = 2$**
Rewrite the contour in standard form: $|z - (-1-i)| = 2$.
Center is at $-1-i$, radius is 2.
*   **Test $z_1 = -1+2i$:** $|(-1+2i) - (-1-i)| = |3i| = 3 > 2$. (Outside).
*   **Test $z_2 = -1-2i$:** $|(-1-2i) - (-1-i)| = |-i| = 1 < 2$. (Inside).

Only $z_2 = -1-2i$ is enclosed.
Isolate $(z - (-1-2i))$ in the denominator:
$$I_1 = \oint_C \frac{ \left( \frac{z+4}{z - (-1+2i)} \right) }{z - (-1-2i)} dz$$
Let $f(z) = \frac{z+4}{z+1-2i}$. Apply Cauchy's Integral Formula:
$$I_1 = 2\pi i \cdot f(-1-2i) = 2\pi i \left( \frac{(-1-2i) + 4}{(-1-2i) + 1 - 2i} \right) = 2\pi i \left( \frac{3 - 2i}{-4i} \right)$$
$$I_1 = 2\pi \left( \frac{3 - 2i}{-4} \right) = -\frac{\pi}{2}(3 - 2i)$$
**Answer (i): $-\frac{\pi}{2}(3 - 2i)$**

---
**Part (ii): Contour is $|z+1-i| = 2$**
*(This specific part is identical to Q259/Q295. We already evaluated it).*
Rewrite contour: $|z - (-1+i)| = 2$.
*   **Test $z_1 = -1+2i$:** $|(-1+2i) - (-1+i)| = |i| = 1 < 2$. (Inside).
*   **Test $z_2 = -1-2i$:** $|(-1-2i) - (-1+i)| = |-3i| = 3 > 2$. (Outside).

Only $z_1 = -1+2i$ is enclosed.
Isolate $(z - (-1+2i))$ in the denominator:
$$I_2 = \oint_C \frac{ \left( \frac{z+4}{z - (-1-2i)} \right) }{z - (-1+2i)} dz$$
Let $f(z) = \frac{z+4}{z+1+2i}$. Apply Cauchy's Integral Formula:
$$I_2 = 2\pi i \cdot f(-1+2i) = 2\pi i \left( \frac{(-1+2i) + 4}{(-1+2i) + 1 + 2i} \right) = 2\pi i \left( \frac{3 + 2i}{4i} \right)$$
$$I_2 = 2\pi \left( \frac{3 + 2i}{4} \right) = \frac{\pi}{2}(3 + 2i)$$
**Answer (ii): $\frac{\pi}{2}(3 + 2i)$**

---
**Part (iii): Contour is $|z| = 1$**
The contour is a circle of radius 1 centered at the origin.
*   **Test $z_1 = -1+2i$:** $|-1+2i| = \sqrt{(-1)^2 + 2^2} = \sqrt{5} \approx 2.236 > 1$. (Outside).
*   **Test $z_2 = -1-2i$:** $|-1-2i| = \sqrt{(-1)^2 + (-2)^2} = \sqrt{5} \approx 2.236 > 1$. (Outside).

Because *neither* pole is enclosed by the contour, the entire function is analytic inside and on the contour $C$. By Cauchy's Integral Theorem, the integral evaluates to zero.
**Answer (iii): $0$**

***

### Q299. Pg 1, Q3(c): Expand $f(z) = \frac{1}{(z+1)(z+3)}$ in a Laurent series valid for $1 < |z| < 3$.

**Solution:**

We need to find the Laurent series expansion for $f(z) = \frac{1}{(z+1)(z+3)}$ in the specified annular region.

**Step 1: Perform Partial Fraction Decomposition.**
We split the rational function into simpler fractions:
$$\frac{1}{(z+1)(z+3)} = \frac{A}{z+1} + \frac{B}{z+3}$$
$$1 = A(z+3) + B(z+1)$$
*   If $z = -1 \implies 1 = A(2) \implies A = 1/2$
*   If $z = -3 \implies 1 = B(-2) \implies B = -1/2$

So, $f(z) = \frac{1}{2} \left( \frac{1}{z+1} \right) - \frac{1}{2} \left( \frac{1}{z+3} \right)$.

**Step 2: Analyze the region of convergence.**
The given region is $1 < |z| < 3$.
This breaks down into two separate conditions:
1.  $|z| > 1 \implies \left| \frac{1}{z} \right| < 1$
2.  $|z| < 3 \implies \left| \frac{z}{3} \right| < 1$

To use the standard geometric series expansion $\frac{1}{1-w} = \sum_{n=0}^\infty w^n$, we strictly require the modulus of the term $w$ to be less than 1 ($|w| < 1$).

**Step 3: Expand the first term $\frac{1}{z+1}$.**
We must use the condition $|z| > 1$, which means $\left|\frac{1}{z}\right| < 1$.
Therefore, we must factor out $z$ from the denominator so that the remaining term is a function of $\frac{1}{z}$:
$$\frac{1}{z+1} = \frac{1}{z(1 + \frac{1}{z})} = \frac{1}{z} \cdot \frac{1}{1 - (-\frac{1}{z})}$$
Since $|-\frac{1}{z}| < 1$, we can expand this as a geometric series:
$$= \frac{1}{z} \sum_{n=0}^\infty \left(-\frac{1}{z}\right)^n = \frac{1}{z} \sum_{n=0}^\infty (-1)^n z^{-n} = \sum_{n=0}^\infty (-1)^n z^{-(n+1)}$$
Expanding a few terms: $= \frac{1}{z} - \frac{1}{z^2} + \frac{1}{z^3} - \dots$

**Step 4: Expand the second term $\frac{1}{z+3}$.**
We must use the condition $|z| < 3$, which means $\left|\frac{z}{3}\right| < 1$.
Therefore, we must factor out $3$ from the denominator so that the remaining term is a function of $\frac{z}{3}$:
$$\frac{1}{z+3} = \frac{1}{3(1 + \frac{z}{3})} = \frac{1}{3} \cdot \frac{1}{1 - (-\frac{z}{3})}$$
Since $|-\frac{z}{3}| < 1$, we can expand this as a geometric series:
$$= \frac{1}{3} \sum_{n=0}^\infty \left(-\frac{z}{3}\right)^n = \frac{1}{3} \sum_{n=0}^\infty (-1)^n \frac{z^n}{3^n} = \sum_{n=0}^\infty (-1)^n \frac{z^n}{3^{n+1}}$$
Expanding a few terms: $= \frac{1}{3} - \frac{z}{9} + \frac{z^2}{27} - \dots$

**Step 5: Combine the expansions.**
Substitute the expansions back into the partial fraction equation from Step 1:
$$f(z) = \frac{1}{2} \left[ \sum_{n=0}^\infty (-1)^n z^{-(n+1)} \right] - \frac{1}{2} \left[ \sum_{n=0}^\infty (-1)^n \frac{z^n}{3^{n+1}} \right]$$

**Answer:** 
The Laurent series is **$f(z) = \frac{1}{2} \sum_{n=0}^\infty (-1)^n z^{-(n+1)} - \frac{1}{2} \sum_{n=0}^\infty (-1)^n \frac{z^n}{3^{n+1}}$**.
*(Expanded form: $f(z) = \dots + \frac{1}{2z^3} - \frac{1}{2z^2} + \frac{1}{2z} - \frac{1}{6} + \frac{z}{18} - \frac{z^2}{54} + \dots$)*

***

### Q300. Pg 4, Q3(c): If $F(z) = \frac{3z-3}{(2z-1)(z-2)}$, find a Laurent series of $F(z)$ about $z=1$ convergent for $\frac{1}{2} < |z-1| < 1$.

**Solution:**

We need to expand $F(z)$ around the point $z_0 = 1$. The standard approach is to use a substitution to shift the center to the origin.

**Step 1: Perform the substitution.**
Let $u = z - 1$. This implies $z = u + 1$.
The region of convergence $\frac{1}{2} < |z-1| < 1$ becomes $\frac{1}{2} < |u| < 1$.
Substitute $z = u+1$ into the function $F(z)$:
$$F(u) = \frac{3(u+1) - 3}{(2(u+1) - 1)((u+1) - 2)}$$
$$F(u) = \frac{3u + 3 - 3}{(2u + 2 - 1)(u - 1)}$$
$$F(u) = \frac{3u}{(2u + 1)(u - 1)}$$

**Step 2: Perform Partial Fraction Decomposition.**
$$\frac{3u}{(2u + 1)(u - 1)} = \frac{A}{2u + 1} + \frac{B}{u - 1}$$
$$3u = A(u - 1) + B(2u + 1)$$
*   If $u = 1 \implies 3(1) = B(3) \implies B = 1$.
*   If $u = -1/2 \implies 3(-1/2) = A(-3/2) \implies -3/2 = -3A/2 \implies A = 1$.

So, $F(u) = \frac{1}{2u + 1} + \frac{1}{u - 1}$.

**Step 3: Analyze the region of convergence.**
The region is $\frac{1}{2} < |u| < 1$.
This gives two conditions for geometric series expansion ($|w| < 1$):
1.  $|u| > \frac{1}{2} \implies |2u| > 1 \implies \left| \frac{1}{2u} \right| < 1$
2.  $|u| < 1 \implies |u| < 1$

**Step 4: Expand the first term $\frac{1}{2u+1}$.**
We must use the condition $\left|\frac{1}{2u}\right| < 1$.
Factor out $2u$ from the denominator:
$$\frac{1}{2u + 1} = \frac{1}{2u(1 + \frac{1}{2u})} = \frac{1}{2u} \cdot \frac{1}{1 - (-\frac{1}{2u})}$$
Since $|-\frac{1}{2u}| < 1$, we can expand this as a geometric series:
$$= \frac{1}{2u} \sum_{n=0}^\infty \left(-\frac{1}{2u}\right)^n = \frac{1}{2u} \sum_{n=0}^\infty (-1)^n (2u)^{-n} = \sum_{n=0}^\infty (-1)^n (2u)^{-(n+1)}$$
$$= \sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1} u^{n+1}}$$

**Step 5: Expand the second term $\frac{1}{u-1}$.**
We must use the condition $|u| < 1$.
Factor out $-1$ from the denominator to get the standard form:
$$\frac{1}{u - 1} = \frac{1}{-(1 - u)} = -1 \cdot \frac{1}{1 - u}$$
Since $|u| < 1$, we can expand this directly:
$$= -1 \sum_{n=0}^\infty u^n = -\sum_{n=0}^\infty u^n$$

**Step 6: Combine and reverse the substitution.**
Combine the two expansions to get $F(u)$:
$$F(u) = \sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1} u^{n+1}} - \sum_{n=0}^\infty u^n$$

Substitute $u = z - 1$ back into the expression:
$$F(z) = \sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1} (z-1)^{n+1}} - \sum_{n=0}^\infty (z-1)^n$$

**Answer:** The Laurent series is **$\sum_{n=0}^\infty \frac{(-1)^n}{2^{n+1} (z-1)^{n+1}} - \sum_{n=0}^\infty (z-1)^n$**.


Here are the detailed solutions for the next four questions (Q301 to Q304).

### Q301. Pg 6, Q2(c): Expand $\ln(\frac{1+z}{1-z})$ in a Taylor series about, $z=0$.

**Solution:**

We need to find the Taylor (Maclaurin) series expansion for $f(z) = \ln\left(\frac{1+z}{1-z}\right)$ around $z=0$.

**Method 1: Using known standard series expansions.**
**Step 1: Use logarithm properties to split the function.**
Using the standard property $\ln(a/b) = \ln(a) - \ln(b)$, we can rewrite the function as:
$$f(z) = \ln(1+z) - \ln(1-z)$$

**Step 2: Recall the standard Maclaurin series for $\ln(1+z)$ and $\ln(1-z)$.**
The well-known series for $\ln(1+x)$ around $0$ is:
$$\ln(1+z) = z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \frac{z^5}{5} - \dots = \sum_{n=1}^\infty (-1)^{n+1} \frac{z^n}{n}$$
(This is valid for $|z| < 1$).

To find the series for $\ln(1-z)$, we substitute $(-z)$ into the series for $\ln(1+z)$:
$$\ln(1-z) = (-z) - \frac{(-z)^2}{2} + \frac{(-z)^3}{3} - \frac{(-z)^4}{4} + \frac{(-z)^5}{5} - \dots$$
$$\ln(1-z) = -z - \frac{z^2}{2} - \frac{z^3}{3} - \frac{z^4}{4} - \frac{z^5}{5} - \dots = -\sum_{n=1}^\infty \frac{z^n}{n}$$

**Step 3: Subtract the two series.**
$$f(z) = \left( z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \frac{z^5}{5} - \dots \right) - \left( -z - \frac{z^2}{2} - \frac{z^3}{3} - \frac{z^4}{4} - \frac{z^5}{5} - \dots \right)$$

Distribute the negative sign to the second series:
$$f(z) = \left( z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \dots \right) + \left( z + \frac{z^2}{2} + \frac{z^3}{3} + \frac{z^4}{4} + \dots \right)$$

When we add them together, all the even-powered terms ($z^2/2, z^4/4$, etc.) have opposite signs and cancel exactly to zero.
All the odd-powered terms ($z, z^3/3, z^5/5$, etc.) have the same signs and double up.
$$f(z) = 2z + 2\frac{z^3}{3} + 2\frac{z^5}{5} + \dots$$
$$f(z) = 2 \left( z + \frac{z^3}{3} + \frac{z^5}{5} + \dots \right)$$

Written in compact summation notation (where odd powers can be represented by $2n-1$ or $2n+1$):
$$f(z) = 2 \sum_{n=0}^\infty \frac{z^{2n+1}}{2n+1}$$

**Answer:** The Taylor series expansion is **$2 \left( z + \frac{z^3}{3} + \frac{z^5}{5} + \frac{z^7}{7} + \dots \right)$** or **$2 \sum_{n=0}^\infty \frac{z^{2n+1}}{2n+1}$**.

***

### Q302. Problem 6.1: Prove Taylor's theorem: If $f(z)$ is analytic inside a circle C with center at a, then for all z inside C, $f(z)=f(a)+f^{\prime}(a)(z-a)+\frac{f^{\prime\prime}(a)}{2!}(z-a)^{2}+\frac{f^{\prime\prime\prime}(a)}{3!}(z-a)^{3}+\dots$

**Solution:**

**Proof:**
Let $z$ be any point inside a circle $C$ centered at $a$. We draw a slightly smaller concentric circle $C_1$ with radius $r$ centered at $a$, such that $z$ lies strictly inside $C_1$, and $C_1$ lies entirely inside $C$. 
By Cauchy's Integral Formula, since $f$ is analytic on and inside $C_1$:
$$f(z) = \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{w - z} dw \quad \text{--- (Eq 1)}$$
where $w$ is the variable of integration along the contour $C_1$.

We need to express $\frac{1}{w-z}$ in powers of $(z-a)$. We use algebraic manipulation:
$$\frac{1}{w-z} = \frac{1}{(w-a) - (z-a)} = \frac{1}{(w-a) \left[ 1 - \frac{z-a}{w-a} \right]}$$

Since $w$ is on $C_1$ and $z$ is inside $C_1$, the distance $|z-a|$ is strictly less than the distance $|w-a| = r$. Therefore, the term $\left|\frac{z-a}{w-a}\right| < 1$. 
Because this magnitude is less than 1, we can expand $\frac{1}{1 - q}$ as a geometric series ($1 + q + q^2 + \dots$):
$$\frac{1}{1 - \frac{z-a}{w-a}} = 1 + \left(\frac{z-a}{w-a}\right) + \left(\frac{z-a}{w-a}\right)^2 + \dots + \left(\frac{z-a}{w-a}\right)^{n-1} + \dots$$

Substitute this back into our expression for $\frac{1}{w-z}$:
$$\frac{1}{w-z} = \frac{1}{w-a} \left[ 1 + \left(\frac{z-a}{w-a}\right) + \left(\frac{z-a}{w-a}\right)^2 + \dots \right]$$
$$\frac{1}{w-z} = \frac{1}{w-a} + \frac{z-a}{(w-a)^2} + \frac{(z-a)^2}{(w-a)^3} + \dots \quad \text{--- (Eq 2)}$$

Now, substitute Equation 2 into the integral in Equation 1:
$$f(z) = \frac{1}{2\pi i} \oint_{C_1} f(w) \left[ \frac{1}{w-a} + \frac{z-a}{(w-a)^2} + \frac{(z-a)^2}{(w-a)^3} + \dots \right] dw$$

Because the series converges uniformly on $C_1$, we can integrate term by term. We can also pull the $(z-a)$ terms outside the integrals, because $z$ and $a$ are constants with respect to the integration variable $w$:
$$f(z) = \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{w-a} dw + (z-a) \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^2} dw + (z-a)^2 \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^3} dw + \dots$$

Finally, we apply the **Generalized Cauchy Integral Formula** to each term. The formula states that $f^{(n)}(a) = \frac{n!}{2\pi i} \oint_C \frac{f(w)}{(w-a)^{n+1}} dw$, which rearranges to $\frac{1}{2\pi i} \oint_C \frac{f(w)}{(w-a)^{n+1}} dw = \frac{f^{(n)}(a)}{n!}$.
*   Term 1 ($n=0$): $\frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{w-a} dw = f(a)$
*   Term 2 ($n=1$): $\frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^2} dw = \frac{f'(a)}{1!} = f'(a)$
*   Term 3 ($n=2$): $\frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^3} dw = \frac{f''(a)}{2!}$

Substituting these derivative definitions back into the expanded series yields:
$$f(z) = f(a) + f'(a)(z-a) + \frac{f''(a)}{2!}(z-a)^2 + \frac{f'''(a)}{3!}(z-a)^3 + \dots$$
**(Proved)**

***

### Q303. Problem 6.2: Expand $f(z)=sin~z$ in a Taylor series about $z=\pi/4$ and determine the region of convergence of this series.

**Solution:**

We need to find the Taylor series for $f(z) = \sin z$ centered at $a = \pi/4$.
The formula is $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (z-a)^n$.

**Step 1: Calculate the derivatives of $f(z)$ evaluated at $a = \pi/4$.**
We need to evaluate $f(z)$ and its successive derivatives at $z = \pi/4$. Note that $\sin(\pi/4) = \cos(\pi/4) = 1/\sqrt{2}$.

*   $n=0$: $f(z) = \sin z \implies f(\pi/4) = \sin(\pi/4) = \frac{1}{\sqrt{2}}$
*   $n=1$: $f'(z) = \cos z \implies f'(\pi/4) = \cos(\pi/4) = \frac{1}{\sqrt{2}}$
*   $n=2$: $f''(z) = -\sin z \implies f''(\pi/4) = -\sin(\pi/4) = -\frac{1}{\sqrt{2}}$
*   $n=3$: $f'''(z) = -\cos z \implies f'''(\pi/4) = -\cos(\pi/4) = -\frac{1}{\sqrt{2}}$
*   $n=4$: $f^{(4)}(z) = \sin z \implies f^{(4)}(\pi/4) = \sin(\pi/4) = \frac{1}{\sqrt{2}}$
The pattern of coefficients repeats every 4 derivatives: $+1, +1, -1, -1, +1, +1, -1, -1 \dots$ (all scaled by $1/\sqrt{2}$).

**Step 2: Substitute into the Taylor series formula.**
$$f(z) = f(\pi/4) + f'(\pi/4)(z - \pi/4) + \frac{f''(\pi/4)}{2!}(z - \pi/4)^2 + \frac{f'''(\pi/4)}{3!}(z - \pi/4)^3 + \dots$$
$$f(z) = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}(z - \pi/4) - \frac{1}{\sqrt{2} \cdot 2!}(z - \pi/4)^2 - \frac{1}{\sqrt{2} \cdot 3!}(z - \pi/4)^3 + \frac{1}{\sqrt{2} \cdot 4!}(z - \pi/4)^4 + \dots$$

Factor out $1/\sqrt{2}$ for a cleaner expression:
$$f(z) = \frac{1}{\sqrt{2}} \left[ 1 + (z - \pi/4) - \frac{(z - \pi/4)^2}{2!} - \frac{(z - \pi/4)^3}{3!} + \frac{(z - \pi/4)^4}{4!} + \dots \right]$$

**Step 3: Determine the region of convergence.**
The function $f(z) = \sin z$ is an entire function, meaning it is analytic everywhere in the complex plane. It has no singular points. 
A Taylor series converges in the largest open disk centered at $a$ that does not contain any singularities. Since there are no singularities anywhere to bound the disk, the radius of convergence is infinite ($R = \infty$).

**Answer:** 
*   **Taylor Series:** **$\frac{1}{\sqrt{2}} \left[ 1 + (z - \pi/4) - \frac{(z - \pi/4)^2}{2!} - \frac{(z - \pi/4)^3}{3!} + \dots \right]$**
*   **Region of Convergence:** The entire complex plane, **$|z| < \infty$** (or $|z-\pi/4| < \infty$).

***

### Q304. Problem 6.3: Find the Taylors series expansion of $f(z)=\frac{z^{2}-1}{(z+2)(z+3)}$ in $|z|<2.$

**Solution:**

We need to find the Taylor series (Maclaurin series, since the center is $z=0$) for $f(z) = \frac{z^2-1}{(z+2)(z+3)}$ valid for $|z| < 2$.

**Step 1: Perform Polynomial Division.**
Because the degree of the numerator (2) is equal to the degree of the expanded denominator ($z^2+5z+6$), we must divide them first to extract the integer part before using partial fractions.
$$\frac{z^2-1}{z^2+5z+6} = \frac{(z^2+5z+6) - 5z - 7}{z^2+5z+6} = 1 - \frac{5z+7}{(z+2)(z+3)}$$

**Step 2: Perform Partial Fraction Decomposition on the remainder.**
We decompose $\frac{5z+7}{(z+2)(z+3)}$:
$$\frac{5z+7}{(z+2)(z+3)} = \frac{A}{z+2} + \frac{B}{z+3}$$
$$5z + 7 = A(z+3) + B(z+2)$$
*   If $z = -2 \implies 5(-2)+7 = A(-2+3) \implies -3 = A(1) \implies A = -3$.
*   If $z = -3 \implies 5(-3)+7 = B(-3+2) \implies -8 = B(-1) \implies B = 8$.

Substitute these back into $f(z)$:
$$f(z) = 1 - \left( \frac{-3}{z+2} + \frac{8}{z+3} \right) = 1 + \frac{3}{z+2} - \frac{8}{z+3}$$

**Step 3: Analyze the region of convergence.**
The required region is $|z| < 2$.
To use the geometric series formula $\frac{1}{1-w} = \sum w^n$, we need $|w| < 1$.
*   For the $(z+2)$ term, since $|z| < 2$, we can write it as a function of $(z/2)$ because $|z/2| < 1$.
*   For the $(z+3)$ term, since $|z| < 2$, it automatically follows that $|z| < 3$. We can write it as a function of $(z/3)$ because $|z/3| < 2/3 < 1$.

**Step 4: Expand the terms into geometric series.**
*   **First fractional term:**
    $$\frac{3}{z+2} = \frac{3}{2(1 + \frac{z}{2})} = \frac{3}{2} \cdot \frac{1}{1 - (-\frac{z}{2})}$$
    Since $|-z/2| < 1$, we expand:
    $$= \frac{3}{2} \sum_{n=0}^\infty \left(-\frac{z}{2}\right)^n = \frac{3}{2} \sum_{n=0}^\infty (-1)^n \frac{z^n}{2^n} = \sum_{n=0}^\infty (-1)^n \frac{3 \cdot z^n}{2^{n+1}}$$
    
*   **Second fractional term:**
    $$\frac{8}{z+3} = \frac{8}{3(1 + \frac{z}{3})} = \frac{8}{3} \cdot \frac{1}{1 - (-\frac{z}{3})}$$
    Since $|-z/3| < 1$, we expand:
    $$= \frac{8}{3} \sum_{n=0}^\infty \left(-\frac{z}{3}\right)^n = \frac{8}{3} \sum_{n=0}^\infty (-1)^n \frac{z^n}{3^n} = \sum_{n=0}^\infty (-1)^n \frac{8 \cdot z^n}{3^{n+1}}$$

**Step 5: Combine everything.**
Substitute the expansions back into the full function equation:
$$f(z) = 1 + \sum_{n=0}^\infty (-1)^n \frac{3}{2^{n+1}} z^n - \sum_{n=0}^\infty (-1)^n \frac{8}{3^{n+1}} z^n$$

We can combine the sums into a single sigma notation. Notice the $n=0$ term is special because of the lone '$1$' at the start. Let's pull the $n=0$ term out of the sums to evaluate the constant term of the series:
Constant term = $1 + (-1)^0\frac{3}{2^1}(0)^0 - (-1)^0\frac{8}{3^1}(0)^0 = 1 + \frac{3}{2} - \frac{8}{3} = \frac{6+9-16}{6} = -\frac{1}{6}$.

So the series can be written strictly as a single combined sum from $n=1$, plus the constant term, but keeping it in the general summation form from $n=0$ (and adding 1) is perfectly acceptable.
$$f(z) = 1 + \sum_{n=0}^\infty (-1)^n \left( \frac{3}{2^{n+1}} - \frac{8}{3^{n+1}} \right) z^n$$

**Answer:** The Taylor series expansion is **$1 + \sum_{n=0}^\infty (-1)^n \left( \frac{3}{2^{n+1}} - \frac{8}{3^{n+1}} \right) z^n$**.




Here are the detailed solutions for the next four questions (Q305 to Q308).

### Q305. Problem 6.4: Obtain Taylor's series for $f(z)=\frac{1}{(z+2)(1+z^{2})}$ in $|z|<1$

**Solution:**

We need to find the Taylor series (Maclaurin series, centered at $z=0$) for $f(z) = \frac{1}{(z+2)(1+z^2)}$ valid within the unit disk $|z| < 1$.

**Step 1: Perform Partial Fraction Decomposition.**
We must split the function into simpler terms.
$$f(z) = \frac{1}{(z+2)(z^2+1)} = \frac{A}{z+2} + \frac{Bz + C}{z^2+1}$$
Multiply by the common denominator:
$$1 = A(z^2+1) + (Bz+C)(z+2)$$

Let's find the constants by choosing convenient values for $z$:
*   **Let $z = -2$:**
    $$1 = A((-2)^2+1) + (-2B+C)(0)$$
    $$1 = 5A \implies A = \frac{1}{5}$$
*   **Let $z = i$** (to eliminate $A$):
    $$1 = A(i^2+1) + (Bi+C)(i+2)$$
    $$1 = A(0) + Bi^2 + 2Bi + Ci + 2C$$
    Since $i^2 = -1$:
    $$1 = -B + 2Bi + Ci + 2C$$
    $$1 = (2C - B) + i(2B + C)$$
    Equate real and imaginary parts:
    Real: $2C - B = 1 \implies B = 2C - 1$
    Imaginary: $2B + C = 0$
    Substitute $B$: $2(2C-1) + C = 0 \implies 4C - 2 + C = 0 \implies 5C = 2 \implies C = \frac{2}{5}$.
    Find $B$: $B = 2(2/5) - 1 = 4/5 - 5/5 = -\frac{1}{5}$.

Substitute $A, B, C$ back into the partial fraction decomposition:
$$f(z) = \frac{1/5}{z+2} + \frac{(-1/5)z + 2/5}{1+z^2}$$
$$f(z) = \frac{1}{5} \left( \frac{1}{z+2} \right) - \frac{1}{5} \left( \frac{z-2}{1+z^2} \right)$$
$$f(z) = \frac{1}{5(z+2)} - \frac{z}{5(1+z^2)} + \frac{2}{5(1+z^2)}$$

**Step 2: Expand each term using geometric series.**
The required region of convergence is $|z| < 1$. We must format each term to use $\frac{1}{1-w} = \sum_{n=0}^\infty w^n$ where $|w| < 1$.

*   **Term 1:** $\frac{1}{5(z+2)}$
    Factor out 2 from the denominator so we get $(z/2)$, which satisfies $|z/2| < 1/2 < 1$.
    $$= \frac{1}{10(1 + \frac{z}{2})} = \frac{1}{10} \frac{1}{1 - (-\frac{z}{2})} = \frac{1}{10} \sum_{n=0}^\infty \left(-\frac{z}{2}\right)^n = \sum_{n=0}^\infty \frac{(-1)^n}{10 \cdot 2^n} z^n$$

*   **Term 2:** $-\frac{z}{5(1+z^2)}$
    Since $|z| < 1$, it implies $|z^2| < 1$. We can expand directly.
    $$= -\frac{z}{5} \cdot \frac{1}{1 - (-z^2)} = -\frac{z}{5} \sum_{n=0}^\infty (-z^2)^n = -\frac{z}{5} \sum_{n=0}^\infty (-1)^n z^{2n} = \sum_{n=0}^\infty \frac{(-1)^{n+1}}{5} z^{2n+1}$$

*   **Term 3:** $\frac{2}{5(1+z^2)}$
    $$= \frac{2}{5} \cdot \frac{1}{1 - (-z^2)} = \frac{2}{5} \sum_{n=0}^\infty (-z^2)^n = \sum_{n=0}^\infty \frac{2(-1)^n}{5} z^{2n}$$

**Step 3: Combine the series.**
$$f(z) = \sum_{n=0}^\infty \frac{(-1)^n}{10 \cdot 2^n} z^n + \sum_{n=0}^\infty \frac{2(-1)^n}{5} z^{2n} + \sum_{n=0}^\infty \frac{(-1)^{n+1}}{5} z^{2n+1}$$

This format is mathematically correct. If desired, one could painstakingly combine the terms for even powers ($z^{2k}$) and odd powers ($z^{2k+1}$), but leaving them as separate geometric sums derived from partial fractions is standard practice.

**Answer:** **$f(z) = \sum_{n=0}^\infty \frac{(-1)^n}{10 \cdot 2^n} z^n + \sum_{n=0}^\infty \frac{2(-1)^n}{5} z^{2n} + \sum_{n=0}^\infty \frac{(-1)^{n+1}}{5} z^{2n+1}$**

***

### Q306. Problem 6.5: If $f(z)=ln(1+z)$ where we consider the branch that has the zero value when $z=0$ (a) Expand f(z) in a Taylor series about $z=0$ (b) Determine the region of convergence for the series in (a). (c) Expand $ln(1+z/1-z)$ in a Taylor series about $z=0$.

**Solution:**

**Part (a): Expand $f(z) = \ln(1+z)$ in a Taylor series about $z=0$.**
We use the definition of the Maclaurin series: $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} z^n$.
1.  Evaluate function and derivatives at $z=0$:
    *   $f(z) = \ln(1+z) \implies f(0) = \ln(1) = 0$
    *   $f'(z) = (1+z)^{-1} \implies f'(0) = 1^{-1} = 1$
    *   $f''(z) = -1(1+z)^{-2} \implies f''(0) = -1$
    *   $f'''(z) = 2(1+z)^{-3} \implies f'''(0) = 2$
    *   $f^{(4)}(z) = -6(1+z)^{-4} \implies f^{(4)}(0) = -6$
    *   General pattern for $n \ge 1$: $f^{(n)}(0) = (-1)^{n-1} (n-1)!$
2.  Substitute into the series formula:
    $$f(z) = 0 + \frac{1}{1!}z + \frac{-1}{2!}z^2 + \frac{2}{3!}z^3 + \frac{-6}{4!}z^4 + \dots$$
    $$f(z) = z - \frac{1}{2}z^2 + \frac{2}{6}z^3 - \frac{6}{24}z^4 + \dots$$
    $$f(z) = z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \dots$$
3.  Write in summation notation:
    **Answer (a): $\sum_{n=1}^\infty (-1)^{n-1} \frac{z^n}{n}$**

---
**Part (b): Determine the region of convergence.**
The radius of convergence for a Taylor series centered at $z_0$ is the distance to the nearest singularity.
The function $f(z) = \ln(1+z)$ has a branch point singularity where the argument of the logarithm is zero.
$$1 + z = 0 \implies z = -1$$
The distance from the center $z=0$ to the singularity $z=-1$ is $|-1| = 1$.
Therefore, the radius of convergence is $R = 1$.
**Answer (b): The region of convergence is $|z| < 1$.**

---
**Part (c): Expand $\ln\left(\frac{1+z}{1-z}\right)$ in a Taylor series about $z=0$.**
*(Note: This is identically solved in Q301. I will summarize it here).*
1.  Use log properties to split: $\ln\left(\frac{1+z}{1-z}\right) = \ln(1+z) - \ln(1-z)$.
2.  We know $\ln(1+z) = z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \dots$
3.  Substitute $(-z)$ to find the other: $\ln(1-z) = -z - \frac{z^2}{2} - \frac{z^3}{3} - \frac{z^4}{4} - \dots$
4.  Subtract the two series. All even powers cancel out, and all odd powers double:
    $\ln(1+z) - \ln(1-z) = 2z + \frac{2z^3}{3} + \frac{2z^5}{5} + \dots$
**Answer (c): $2 \sum_{n=0}^\infty \frac{z^{2n+1}}{2n+1}$**

***

### Q307. Problem 6.6: Prove Laurent's theorem: Suppose $f(z)$ is analytic inside and on the boundary of the ring-shaped region R bounded by two concentric circles $C_{1}$ and $C_{2}$ with center at a and respective radii r and $r_{2}(r_{1}>r_{2})$ (see Fig. 6-5). Then for all z in R, $f(z)=\sum_{n=0}^{\infty}a_{n}(z-a)^{n}+\sum_{n=1}^{\infty}\frac{a_{-n}}{(z-a)^{n}}$

**Solution:**

**Proof Outline of Laurent's Theorem:**
Let $z$ be an arbitrary point in the annular region between the outer circle $C_1$ and inner circle $C_2$. Both circles are centered at $a$. We introduce a cross-cut to make the region simply connected.

**Step 1: Apply Cauchy's Integral Formula.**
By Cauchy's Integral Formula for a multiply connected domain (or by creating a cross-cut and using the standard theorem), the value of the function at $z$ is the sum of integrals over the boundaries. We traverse $C_1$ counter-clockwise and $C_2$ clockwise (or subtract the counter-clockwise $C_2$ integral):
$$f(z) = \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{w-z} dw - \frac{1}{2\pi i} \oint_{C_2} \frac{f(w)}{w-z} dw \quad \text{--- (Eq 1)}$$

**Step 2: Expand the integral over $C_1$ (The Taylor Part).**
For any point $w$ on the outer circle $C_1$, the distance to the center is $|w-a| = r_1$. Since $z$ is strictly inside $C_1$, we know $|z-a| < |w-a|$.
Therefore, the ratio $\left|\frac{z-a}{w-a}\right| < 1$.
We manipulate the denominator:
$$\frac{1}{w-z} = \frac{1}{(w-a) - (z-a)} = \frac{1}{(w-a)} \cdot \frac{1}{1 - \frac{z-a}{w-a}}$$
We expand this using the geometric series (just like in the Taylor series proof in Q302):
$$\frac{1}{w-z} = \sum_{n=0}^\infty \frac{(z-a)^n}{(w-a)^{n+1}}$$
Substitute this into the first integral of Eq 1. Because the series converges uniformly on $C_1$, we can swap the integral and summation:
$$\frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{w-z} dw = \sum_{n=0}^\infty \left[ \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^{n+1}} dw \right] (z-a)^n$$
Let $a_n = \frac{1}{2\pi i} \oint_{C_1} \frac{f(w)}{(w-a)^{n+1}} dw$. Then the first integral becomes $\sum_{n=0}^\infty a_n (z-a)^n$. This generates the positive powers.

**Step 3: Expand the integral over $C_2$ (The Principal Part).**
For any point $w$ on the inner circle $C_2$, the distance to the center is $|w-a| = r_2$. Since $z$ is strictly outside $C_2$, we know $|w-a| < |z-a|$.
Therefore, the ratio $\left|\frac{w-a}{z-a}\right| < 1$.
We must manipulate the denominator differently to utilize this valid ratio:
$$-\frac{1}{w-z} = \frac{1}{z-w} = \frac{1}{(z-a) - (w-a)} = \frac{1}{(z-a)} \cdot \frac{1}{1 - \frac{w-a}{z-a}}$$
We expand this using the geometric series:
$$-\frac{1}{w-z} = \frac{1}{z-a} \sum_{n=0}^\infty \left(\frac{w-a}{z-a}\right)^n = \sum_{n=0}^\infty \frac{(w-a)^n}{(z-a)^{n+1}}$$
To make indices match the theorem statement (where powers of $z-a$ in the denominator are denoted by $n=1, 2, \dots$), let's shift the index by letting $m = n+1$ (so $n = m-1$ and $m$ starts from $1$):
$$-\frac{1}{w-z} = \sum_{m=1}^\infty \frac{(w-a)^{m-1}}{(z-a)^m}$$

Substitute this into the second integral of Eq 1 (note that the negative sign is already absorbed):
$$-\frac{1}{2\pi i} \oint_{C_2} \frac{f(w)}{w-z} dw = \sum_{m=1}^\infty \left[ \frac{1}{2\pi i} \oint_{C_2} f(w) (w-a)^{m-1} dw \right] \frac{1}{(z-a)^m}$$
Let $a_{-m} = \frac{1}{2\pi i} \oint_{C_2} f(w) (w-a)^{m-1} dw = \frac{1}{2\pi i} \oint_{C_2} \frac{f(w)}{(w-a)^{-m+1}} dw$. 
Then the second integral becomes $\sum_{m=1}^\infty \frac{a_{-m}}{(z-a)^m}$.

**Step 4: Combine the parts.**
Combining the results from Step 2 and Step 3 back into Equation 1 yields:
$$f(z) = \sum_{n=0}^\infty a_n (z-a)^n + \sum_{n=1}^\infty \frac{a_{-n}}{(z-a)^n}$$
where $a_k = \frac{1}{2\pi i} \oint_C \frac{f(w)}{(w-a)^{k+1}} dw$ for any integer $k$ (positive, negative, or zero), and $C$ is any contour in the annulus. **(Proved)**

***

### Q308. Problem 6.7: Expand $f(z)=\frac{1}{(z+1)(z+3)}$ in a Laurent series valid for: (a) $1<|z|<3$ (b) $|z|>3$, (c) $0<|z+1|<2$ (d) $|z|<1$.

*(Note: Part (a) is identically solved in Q299. We will solve all four requested regions here using the partial fraction decomposition).*

**Solution:**

First, perform partial fraction decomposition on $f(z)$:
$$f(z) = \frac{1}{(z+1)(z+3)} = \frac{1}{2(z+1)} - \frac{1}{2(z+3)}$$

---
**Part (a): Region $1 < |z| < 3$**
This is an annulus centered at the origin.
*   **For the $(z+1)$ term:** We must use $|z| > 1$, so $|1/z| < 1$. Factor out $z$:
    $$\frac{1}{2(z+1)} = \frac{1}{2z(1 + \frac{1}{z})} = \frac{1}{2z} \sum_{n=0}^\infty (-1)^n \left(\frac{1}{z}\right)^n = \sum_{n=0}^\infty \frac{(-1)^n}{2 z^{n+1}}$$
*   **For the $(z+3)$ term:** We must use $|z| < 3$, so $|z/3| < 1$. Factor out $3$:
    $$-\frac{1}{2(z+3)} = -\frac{1}{6(1 + \frac{z}{3})} = -\frac{1}{6} \sum_{n=0}^\infty (-1)^n \left(\frac{z}{3}\right)^n = \sum_{n=0}^\infty \frac{(-1)^{n+1}}{2 \cdot 3^{n+1}} z^n$$
**Answer (a): $f(z) = \sum_{n=0}^\infty \frac{(-1)^n}{2 z^{n+1}} + \sum_{n=0}^\infty \frac{(-1)^{n+1}}{2 \cdot 3^{n+1}} z^n$**

---
**Part (b): Region $|z| > 3$**
This is the region completely outside the outermost singularity.
*   Since $|z| > 3$, it is inherently true that $|z| > 1$. Therefore, for both fractions, we must factor out $z$ to ensure the geometric ratio is less than 1 ($|1/z|<1$ and $|3/z|<1$).
*   **Term 1:** $\frac{1}{2z(1 + 1/z)} = \sum_{n=0}^\infty \frac{(-1)^n}{2 z^{n+1}}$
*   **Term 2:** $-\frac{1}{2(z+3)} = -\frac{1}{2z(1 + 3/z)} = -\frac{1}{2z} \sum_{n=0}^\infty (-1)^n \left(\frac{3}{z}\right)^n = \sum_{n=0}^\infty \frac{(-1)^{n+1} 3^n}{2 z^{n+1}}$
**Answer (b): $f(z) = \sum_{n=0}^\infty \frac{(-1)^n (1 - 3^n)}{2 z^{n+1}}$**

---
**Part (c): Region $0 < |z+1| < 2$**
The center is shifted to $z = -1$. Let $u = z+1$. The function becomes:
$$F(u) = \frac{1}{2u} - \frac{1}{2(u-1+3)} = \frac{1}{2u} - \frac{1}{2(u+2)}$$
The region is $0 < |u| < 2$.
*   **Term 1:** $\frac{1}{2u}$ is already in its final Laurent form (it represents the principal part).
*   **Term 2:** For $-\frac{1}{2(u+2)}$, we use $|u| < 2 \implies |u/2| < 1$. Factor out 2:
    $$-\frac{1}{4(1 + u/2)} = -\frac{1}{4} \sum_{n=0}^\infty (-1)^n \left(\frac{u}{2}\right)^n = \sum_{n=0}^\infty \frac{(-1)^{n+1}}{2^{n+2}} u^n$$
Substitute $u = z+1$ back:
**Answer (c): $f(z) = \frac{1}{2(z+1)} + \sum_{n=0}^\infty \frac{(-1)^{n+1}}{2^{n+2}} (z+1)^n$**

---
**Part (d): Region $|z| < 1$**
This is a standard Taylor (Maclaurin) series since it encloses no singularities.
*   Since $|z| < 1$, it is inherently true that $|z| < 3$. For both fractions, we factor out the constants.
*   **Term 1:** $\frac{1}{2(1+z)} = \frac{1}{2} \sum_{n=0}^\infty (-1)^n z^n = \sum_{n=0}^\infty \frac{(-1)^n}{2} z^n$
*   **Term 2:** $-\frac{1}{2(z+3)} = -\frac{1}{6(1+z/3)} = -\frac{1}{6} \sum_{n=0}^\infty (-1)^n \left(\frac{z}{3}\right)^n = \sum_{n=0}^\infty \frac{(-1)^{n+1}}{2 \cdot 3^{n+1}} z^n$
**Answer (d): $f(z) = \sum_{n=0}^\infty (-1)^n \left( \frac{1}{2} - \frac{1}{2 \cdot 3^{n+1}} \right) z^n$**

Here are the detailed solutions for the next four questions (Q309 to Q312).

### Q309. Pg 2, Q3(a): Find all the singular points of $f(z) = \frac{(z+3i)^5}{(z^2-2z+5)^2}$.

**Solution:**

A singular point (or singularity) of a rational complex function is a point where the function ceases to be analytic, which typically occurs where the denominator equals zero (causing the function to "blow up" or become undefined).

**Step 1: Set the denominator equal to zero.**
To find the singular points, we must find the roots of the denominator:
$$(z^2 - 2z + 5)^2 = 0$$
This requires solving the quadratic equation inside the parenthesis:
$$z^2 - 2z + 5 = 0$$

**Step 2: Solve the quadratic equation.**
We use the standard quadratic formula, $z = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, where $a = 1$, $b = -2$, and $c = 5$.
$$z = \frac{-(-2) \pm \sqrt{(-2)^2 - 4(1)(5)}}{2(1)}$$
$$z = \frac{2 \pm \sqrt{4 - 20}}{2}$$
$$z = \frac{2 \pm \sqrt{-16}}{2}$$
Since $\sqrt{-16} = \sqrt{16 \cdot -1} = 4i$:
$$z = \frac{2 \pm 4i}{2}$$
Divide both terms by 2:
$$z = 1 \pm 2i$$

**Step 3: Classify the singular points.**
The two singular points are $z_1 = 1 + 2i$ and $z_2 = 1 - 2i$.
Because the entire quadratic expression in the original denominator was squared, $(z^2 - 2z + 5)^2 = [(z - (1+2i))(z - (1-2i))]^2 = (z - (1+2i))^2 (z - (1-2i))^2$.
Therefore, both of these points are **poles of order 2**. 

*(Note: We should quickly check the numerator $(z+3i)^5$ to ensure neither of these roots makes the numerator zero as well, which would reduce the order of the pole. Since $1+2i \neq -3i$ and $1-2i \neq -3i$, the numerator is non-zero at these points, so they remain strict poles of order 2).*

**Answer:** The singular points are **$z = 1 + 2i$** and **$z = 1 - 2i$**. (Both are poles of order 2).

***

### Q310. Pg 4, Q2(b): Define two types of singular point with example. Prove that $u = e^{-x}(x\sin y - y\cos y)$ is harmonic. Find v such that $f(z) = u+iv$ is analytic. Express $u+iv$ as a function of z.

**Solution:**

**Part 1: Define two types of singular points.**
1.  **Pole:** A singular point $z_0$ is called a pole if the function $f(z)$ goes to infinity as $z$ approaches $z_0$. More formally, $z_0$ is a pole of order $m$ if you can multiply the function by $(z-z_0)^m$ to completely remove the singularity and get a non-zero, finite limit.
    *   *Example:* $f(z) = \frac{1}{(z-2)^3}$ has a pole of order 3 at $z=2$.
2.  **Essential Singularity:** A singular point $z_0$ is an essential singularity if the function exhibits extreme, wildly oscillating behavior near $z_0$, and no finite integer $m$ exists such that multiplying by $(z-z_0)^m$ will clear the singularity. In its Laurent series expansion, it has an infinite number of terms with negative powers.
    *   *Example:* $f(z) = e^{1/z}$ has an essential singularity at $z=0$.

---

**Part 2: Prove $u = e^{-x}(x\sin y - y\cos y)$ is harmonic.**
*(Note: This function was partially evaluated in Q176. We will do the full derivation here).*
We must show $\nabla^2 u = u_{xx} + u_{yy} = 0$.

*   **Find $u_x$:**
    $u_x = -e^{-x}(x\sin y - y\cos y) + e^{-x}(\sin y) = e^{-x}(\sin y - x\sin y + y\cos y)$
*   **Find $u_{xx}$:**
    $u_{xx} = -e^{-x}(\sin y - x\sin y + y\cos y) + e^{-x}(-\sin y)$
    $u_{xx} = e^{-x}(-\sin y + x\sin y - y\cos y - \sin y)$
    $u_{xx} = e^{-x}(-2\sin y + x\sin y - y\cos y)$
*   **Find $u_y$:**
    $u_y = e^{-x}[x\cos y - (\cos y - y\sin y)] = e^{-x}(x\cos y - \cos y + y\sin y)$
*   **Find $u_{yy}$:**
    $u_{yy} = e^{-x}[-x\sin y - (-\sin y) + (\sin y + y\cos y)]$
    $u_{yy} = e^{-x}[-x\sin y + \sin y + \sin y + y\cos y]$
    $u_{yy} = e^{-x}(2\sin y - x\sin y + y\cos y)$

*   **Check Laplace:**
    $u_{xx} + u_{yy} = e^{-x}(-2\sin y + x\sin y - y\cos y) + e^{-x}(2\sin y - x\sin y + y\cos y) = 0$.
**$u$ is harmonic.** (Proved)

---

**Part 3: Find $v$ and $f(z)$.**
*(We will use the Milne-Thomson method directly on $u$ to find $f(z)$ first, which is much faster, then extract $v$ from it).*
The Milne-Thomson rule states: $f'(z) = u_x(z,0) - i u_y(z,0)$.
*   Substitute $x=z, y=0$ into $u_x$:
    $u_x(z,0) = e^{-z}(\sin(0) - z\sin(0) + 0\cdot\cos(0)) = 0$
*   Substitute $x=z, y=0$ into $u_y$:
    $u_y(z,0) = e^{-z}(z\cos(0) - \cos(0) + 0\cdot\sin(0)) = e^{-z}(z - 1)$

Construct the derivative:
$f'(z) = 0 - i[e^{-z}(z-1)]$
$f'(z) = -iz e^{-z} + i e^{-z}$

Integrate to find $f(z)$:
$f(z) = \int (-iz e^{-z} + i e^{-z}) dz$
Use integration by parts for $\int -iz e^{-z} dz$: Let $w = -iz, dv = e^{-z} dz \implies dw = -i dz, v = -e^{-z}$.
$\int -iz e^{-z} dz = (-iz)(-e^{-z}) - \int (-e^{-z})(-i dz) = ize^{-z} - i\int e^{-z} dz = ize^{-z} + ie^{-z}$.
Add the second part of the integral:
$f(z) = (ize^{-z} + ie^{-z}) + \int i e^{-z} dz$
$f(z) = ize^{-z} + ie^{-z} - ie^{-z} + C$
**$f(z) = ize^{-z} + C$**

To find $v$, extract the imaginary part of $f(z) = i(x+iy)e^{-x}(\cos y - i\sin y)$.
$f(z) = e^{-x}(-y+ix)(\cos y - i\sin y) = e^{-x}[(-y\cos y - x\sin y) + i(x\cos y - y\sin y)]$
The imaginary part is exactly $v$. Let $C = c_1 + ic_2$.
**$v(x,y) = e^{-x}(x\cos y - y\sin y) + c_2$**

***

### Q311. Example: Locate and name all the singularities of $f(z)=\frac{z^{8}+z^{4}+2}{(z-1)^{3}(3z+2)^{2}}.$ Determine where $f(z)$ is analytic.

**Solution:**

**Step 1: Locate the singularities.**
Singularities for a rational function occur where the denominator equals zero (provided the numerator is non-zero at those points).
$$(z-1)^3 (3z+2)^2 = 0$$
This yields two separate locations:
1.  $z - 1 = 0 \implies z = 1$
2.  $3z + 2 = 0 \implies 3z = -2 \implies z = -2/3$

*(Self-check: Substitute these into the numerator to ensure it's not $0/0$. For $z=1$, Num $= 1+1+2=4 \neq 0$. For $z=-2/3$, Num is clearly non-zero).*

**Step 2: Name (Classify) the singularities.**
The classification of a pole depends on the exponent (power) of the singular factor in the denominator.
*   The factor $(z-1)$ is raised to the 3rd power. Therefore, **$z = 1$ is a pole of order 3**.
*   The factor $(3z+2)$ is raised to the 2nd power. Therefore, **$z = -2/3$ is a pole of order 2**.

**Step 3: Determine where $f(z)$ is analytic.**
A rational complex function (a polynomial divided by a polynomial) is analytic everywhere in the complex plane except at its singular points (poles).

Therefore, $f(z)$ is analytic in the entire complex plane $\mathbb{C}$, excluding the points $z=1$ and $z=-2/3$.
In set notation, the region of analyticity is:
**$\mathbb{C} \setminus \{1, -2/3\}$**

**Answer:**
*   Singularities: **$z=1$ (Pole of order 3)** and **$z=-2/3$ (Pole of order 2)**.
*   Analytic everywhere except at **$z=1$ and $z=-2/3$**.

***

### Q312. Pg 1, Q3(a): State and prove Cauchy's Residue theorem for a pole of order m at $z=a$ inside simple closed curve C.

*(Note: The wording is slightly non-standard. Cauchy's Residue Theorem applies generally to *any* number of isolated singularities inside $C$. The prompt asks specifically to state and prove it for a *single* pole of order $m$. I will provide the proof for a single pole of order $m$, which bridges Cauchy's Integral Formula to the Residue Concept).*

**Solution:**

**Statement:**
Let $f(z)$ be analytic inside and on a simple closed contour $C$, except for a single isolated singularity at $z=a$ inside $C$, which is a pole of order $m$. Then the integral of $f(z)$ around $C$ is given by:
$$\oint_C f(z) dz = 2\pi i \cdot \text{Res}(f, a)$$
where the residue at the pole of order $m$ is calculated as:
$$\text{Res}(f, a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \left[ (z-a)^m f(z) \right]$$

**Proof:**
**Step 1: Define the function using the definition of a pole.**
If $f(z)$ has a pole of order $m$ at $z=a$, it means that multiplying $f(z)$ by $(z-a)^m$ completely removes the singularity, leaving a function that is completely analytic at and around $a$.
Let's define a new function $\phi(z)$:
$$\phi(z) = (z-a)^m f(z)$$
By the definition of a pole of order $m$, the function $\phi(z)$ is completely analytic everywhere inside and on $C$. We can also express $f(z)$ as:
$$f(z) = \frac{\phi(z)}{(z-a)^m}$$

**Step 2: Set up the integral.**
Substitute this expression for $f(z)$ into our contour integral:
$$\oint_C f(z) dz = \oint_C \frac{\phi(z)}{(z-a)^m} dz$$

**Step 3: Apply the Generalized Cauchy Integral Formula.**
Recall the Generalized Cauchy Integral Formula (proven in Q290):
$$\oint_C \frac{\text{Analytic}(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} \text{Analytic}^{(n)}(a)$$

We map our specific integral to this formula:
*   The analytic numerator is $\phi(z)$.
*   The exponent in the denominator is $m$. Let $m = n+1$, which means $n = m-1$.

Substituting these parameters into the formula gives:
$$\oint_C \frac{\phi(z)}{(z-a)^m} dz = \frac{2\pi i}{(m-1)!} \phi^{(m-1)}(a)$$

**Step 4: Substitute $\phi(z)$ back into the result.**
We know $\phi(z) = (z-a)^m f(z)$. Therefore, the $(m-1)$-th derivative evaluated at $a$ is:
$$\phi^{(m-1)}(a) = \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} [ (z-a)^m f(z) ]$$

Substitute this back into the integral equation:
$$\oint_C f(z) dz = \frac{2\pi i}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} [ (z-a)^m f(z) ]$$

**Step 5: Define the Residue.**
The block of terms multiplying $2\pi i$ on the right-hand side is defined in complex analysis as the "Residue" of the function $f(z)$ at the pole $a$.
$$\text{Res}(f, a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} [ (z-a)^m f(z) ]$$

Substitute this definition into the equation to achieve the final stated form:
$$\oint_C f(z) dz = 2\pi i \cdot \text{Res}(f, a)$$
**(Proved)**

Here are the detailed solutions for the next four questions (Q313 to Q316).

### Q313. Pg 1, Q3(b): Evalute $\oint_C \frac{z^2-2z}{(z+1)^2(z^2+4)} dz$ Where C is the circle $|z|=3$

**Solution:**

Let $I = \oint_C \frac{z^2-2z}{(z+1)^2(z^2+4)} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero to find the poles:
$$(z+1)^2(z^2+4) = 0$$
This yields two conditions:
1.  $(z+1)^2 = 0 \implies z = -1$. Because of the square, this is a **pole of order 2**.
2.  $z^2+4 = 0 \implies z^2 = -4 \implies z = \pm 2i$. These are two **simple poles**.

The three poles are: $z_1 = -1$ (order 2), $z_2 = 2i$ (order 1), $z_3 = -2i$ (order 1).

**Step 2: Check which poles are enclosed by the contour.**
The contour $C$ is the circle $|z| = 3$ (centered at origin, radius 3).
*   $|-1| = 1 < 3$ (**Inside**)
*   $|2i| = 2 < 3$ (**Inside**)
*   $|-2i| = 2 < 3$ (**Inside**)

All three poles lie inside the contour. We will use Cauchy's Residue Theorem: $I = 2\pi i (R_1 + R_2 + R_3)$.

**Step 3: Calculate Residue $R_1$ at $z = -1$ (Pole of order 2).**
Formula for order $m=2$: $R_1 = \lim_{z \to -1} \frac{d}{dz} \left[ (z+1)^2 F(z) \right]$.
$$R_1 = \lim_{z \to -1} \frac{d}{dz} \left[ \frac{z^2-2z}{z^2+4} \right]$$
Use the quotient rule:
$$\frac{d}{dz} \left[ \frac{z^2-2z}{z^2+4} \right] = \frac{(2z-2)(z^2+4) - (z^2-2z)(2z)}{(z^2+4)^2}$$
$$= \frac{2z^3 + 8z - 2z^2 - 8 - (2z^3 - 4z^2)}{(z^2+4)^2} = \frac{2z^2 + 8z - 8}{(z^2+4)^2}$$
Evaluate at $z = -1$:
$$R_1 = \frac{2(-1)^2 + 8(-1) - 8}{((-1)^2+4)^2} = \frac{2 - 8 - 8}{(1+4)^2} = \frac{-14}{25}$$

**Step 4: Calculate Residue $R_2$ at $z = 2i$ (Simple pole).**
Formula for simple pole: $R_2 = \lim_{z \to 2i} (z-2i) F(z)$.
Factor the denominator: $(z^2+4) = (z-2i)(z+2i)$.
$$R_2 = \lim_{z \to 2i} (z-2i) \frac{z^2-2z}{(z+1)^2(z-2i)(z+2i)} = \lim_{z \to 2i} \frac{z^2-2z}{(z+1)^2(z+2i)}$$
Substitute $z = 2i$:
Numerator: $(2i)^2 - 2(2i) = -4 - 4i$
Denominator: $(2i+1)^2 (2i+2i) = (1+4i-4)(4i) = (-3+4i)(4i) = -12i + 16i^2 = -16 - 12i$
$$R_2 = \frac{-4 - 4i}{-16 - 12i} = \frac{-4(1+i)}{-4(4+3i)} = \frac{1+i}{4+3i}$$
Rationalize by multiplying by conjugate $(4-3i)$:
$$R_2 = \frac{(1+i)(4-3i)}{(4+3i)(4-3i)} = \frac{4 - 3i + 4i - 3i^2}{16 - 9i^2} = \frac{4 + i + 3}{16+9} = \frac{7+i}{25} = \frac{7}{25} + i\frac{1}{25}$$

**Step 5: Calculate Residue $R_3$ at $z = -2i$ (Simple pole).**
$$R_3 = \lim_{z \to -2i} (z+2i) \frac{z^2-2z}{(z+1)^2(z-2i)(z+2i)} = \lim_{z \to -2i} \frac{z^2-2z}{(z+1)^2(z-2i)}$$
Substitute $z = -2i$:
Numerator: $(-2i)^2 - 2(-2i) = -4 + 4i$
Denominator: $(-2i+1)^2 (-2i-2i) = (1-4i-4)(-4i) = (-3-4i)(-4i) = 12i + 16i^2 = -16 + 12i$
$$R_3 = \frac{-4 + 4i}{-16 + 12i} = \frac{-4(1-i)}{-4(4-3i)} = \frac{1-i}{4-3i}$$
Rationalize:
$$R_3 = \frac{(1-i)(4+3i)}{(4-3i)(4+3i)} = \frac{4 + 3i - 4i - 3i^2}{25} = \frac{4 - i + 3}{25} = \frac{7-i}{25} = \frac{7}{25} - i\frac{1}{25}$$

**Step 6: Sum the residues and calculate the integral.**
$$Sum = R_1 + R_2 + R_3 = \left(-\frac{14}{25}\right) + \left(\frac{7}{25} + i\frac{1}{25}\right) + \left(\frac{7}{25} - i\frac{1}{25}\right)$$
$$Sum = \frac{-14 + 7 + 7}{25} + i\left(\frac{1 - 1}{25}\right) = \frac{0}{25} + 0i = 0$$

$$I = 2\pi i (0) = 0$$

**Answer:** The value of the integral is **$0$**.

***

### Q314. Pg 6, Q3(a): If $F(z)$ is analytic inside and on a simple closed curve C except for a pole of order m and at $z=a$ inside C, then Prove that $\oint F(z)dz = 2\pi i \left[\lim_{z\to a} \frac{1}{(m-1)!}\frac{d^{m-1}}{dz^{m-1}}\{(z-a)^m F(z)\}\right]$.

*(Note: This is numerically and conceptually identical to Q312. The complete formal proof linking the definition of a pole to Cauchy's integral formula is provided again below).*

**Solution:**

**Proof:**

**Step 1: Define the behavior at the pole.**
We are given that $F(z)$ has a pole of order $m$ at the point $z=a$.
By the mathematical definition of a pole of order $m$, multiplying the function $F(z)$ by the factor $(z-a)^m$ will exactly cancel out the singularity, resulting in a new function that is perfectly analytic at $a$ and everywhere else inside $C$.
Let's define this new analytic function as $\phi(z)$:
$$\phi(z) = (z-a)^m F(z)$$
Since $\phi(z)$ is analytic inside and on $C$, we can express the original function as:
$$F(z) = \frac{\phi(z)}{(z-a)^m}$$

**Step 2: Substitute into the contour integral.**
Substitute our new expression for $F(z)$ into the integral we want to evaluate:
$$\oint_C F(z) dz = \oint_C \frac{\phi(z)}{(z-a)^m} dz$$

**Step 3: Apply the Generalized Cauchy Integral Formula.**
The Generalized Cauchy Integral Formula allows us to evaluate integrals with higher-order powers in the denominator. The theorem states:
$$\oint_C \frac{g(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} g^{(n)}(a)$$
where $g(z)$ must be an analytic function.

We map our specific integral to this general formula:
*   Our analytic numerator function is $g(z) = \phi(z)$.
*   The exponent in the denominator is $m$. To match the formula's format of $n+1$, we set $n+1 = m$, which means $n = m-1$.

Substituting these mapped parameters into the theorem gives:
$$\oint_C \frac{\phi(z)}{(z-a)^m} dz = \frac{2\pi i}{(m-1)!} \phi^{(m-1)}(a)$$

**Step 4: Substitute $\phi(z)$ back into the resulting equation.**
We need to express the derivative term $\phi^{(m-1)}(a)$ in terms of our original function $F(z)$.
We defined $\phi(z) = (z-a)^m F(z)$.
Therefore, the $(m-1)$-th derivative of $\phi(z)$ evaluated at the point $z=a$ can be written using a limit expression:
$$\phi^{(m-1)}(a) = \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \left[ (z-a)^m F(z) \right]$$

**Step 5: Final construction.**
Substitute this derivative expression back into the right side of the equation from Step 3:
$$\oint_C F(z) dz = \frac{2\pi i}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \left[ (z-a)^m F(z) \right]$$

Rearrange slightly to exactly match the target formula:
$$\oint_C F(z) dz = 2\pi i \left[ \lim_{z \to a} \frac{1}{(m-1)!} \frac{d^{m-1}}{dz^{m-1}} \{ (z-a)^m F(z) \} \right]$$
**(Proved)**

***

### Q315. Pg 6, Q3(b): Evaluate $\oint_c \frac{dz}{z(z-4)^2}$ where c is the circle, $|z|=1$.

**Solution:**

Let $I = \oint_C \frac{1}{z(z-4)^2} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero:
$$z(z-4)^2 = 0$$
This yields two singular points:
1.  $z_1 = 0$ (a simple pole, order 1).
2.  $z_2 = 4$ (a pole of order 2).

**Step 2: Check which poles are enclosed by the contour.**
The contour $C$ is the unit circle $|z| = 1$. It is centered at the origin with a radius of $1$.
*   **Test $z_1 = 0$:** $|0| = 0 < 1$. This pole is **inside** the contour.
*   **Test $z_2 = 4$:** $|4| = 4 > 1$. This pole is strictly **outside** the contour.

**Step 3: Structure the integral to use Cauchy's Integral Formula.**
Because only the simple pole $z=0$ is enclosed, we must isolate $z$ in the denominator and group the remaining part of the expression to form the analytic numerator function.
$$I = \oint_C \frac{ \left( \frac{1}{(z-4)^2} \right) }{z} dz$$
Let the analytic numerator function be $f(z) = \frac{1}{(z-4)^2}$. This function is perfectly analytic everywhere inside and on the unit circle because its only singularity ($z=4$) lies outside.

**Step 4: Apply Cauchy's Integral Formula.**
The formula for a simple pole is:
$$\oint_C \frac{f(z)}{z-a} dz = 2\pi i \cdot f(a)$$
Here, $a = 0$.
$$I = 2\pi i \cdot f(0)$$

**Step 5: Evaluate $f(0)$.**
Substitute $z = 0$ into our numerator function:
$$f(0) = \frac{1}{(0 - 4)^2} = \frac{1}{(-4)^2} = \frac{1}{16}$$

**Step 6: Calculate final result.**
$$I = 2\pi i \left( \frac{1}{16} \right)$$
$$I = \frac{2\pi i}{16}$$
$$I = \frac{\pi i}{8}$$

**Answer:** The value of the integral is **$\frac{\pi i}{8}$**.

***

### Q316. Pg 17, CT-II, 3.(a): Evaluate $\oint_C \frac{z+4}{z^2+2z+5}$ where C is the circle (i) $|z+1+i|=2$

*(Note: This is identically stated in Q259 and Q295, and is part (i) of Q298).*

**Solution:**

Let $I = \oint_C \frac{z+4}{z^2+2z+5} dz$.

**Step 1: Identify the singularities.**
Find the roots of the denominator:
$$z^2 + 2z + 5 = 0$$
Use the quadratic formula:
$$z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$$
There are two simple poles:
1.  $z_1 = -1 + 2i$
2.  $z_2 = -1 - 2i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is $|z+1+i| = 2$.
Rewrite this in standard geometric form: $|z - (-1-i)| = 2$.
This represents a circle centered at $z = -1-i$ with a radius of $2$.

*   **Test $z_1 = -1+2i$:**
    Substitute into the contour equation's left side to find the distance from the center:
    $|(-1+2i) - (-1-i)| = |-1 + 2i + 1 + i| = |3i| = 3$
    Since $3 > 2$, the pole $z_1 = -1+2i$ lies strictly **outside** the contour.

*   **Test $z_2 = -1-2i$:**
    Substitute into the contour equation:
    $|(-1-2i) - (-1-i)| = |-1 - 2i + 1 + i| = |-i| = 1$
    Since $1 < 2$, the pole $z_2 = -1-2i$ lies safely **inside** the contour.

**Step 3: Structure the integral for Cauchy's Integral Formula.**
Because only $z_2 = -1-2i$ is enclosed, we isolate the factor $(z - (-1-2i))$ in the denominator and push the other factor into the numerator.
The factored denominator is $(z - (-1+2i))(z - (-1-2i))$.
$$I = \oint_C \frac{\left( \frac{z+4}{z - (-1+2i)} \right)}{z - (-1-2i)} dz$$
Let the analytic numerator function be $f(z) = \frac{z+4}{z+1-2i}$.

**Step 4: Apply Cauchy's Integral Formula.**
$$I = 2\pi i \cdot f(-1-2i)$$

**Step 5: Evaluate $f(-1-2i)$.**
Substitute $z = -1-2i$ into the numerator function:
$$f(-1-2i) = \frac{(-1-2i) + 4}{(-1-2i) + 1 - 2i}$$
$$f(-1-2i) = \frac{3 - 2i}{-4i}$$

**Step 6: Final calculation.**
Multiply by $2\pi i$:
$$I = 2\pi i \left( \frac{3 - 2i}{-4i} \right)$$
The $i$ terms cancel out, and $2 / -4$ simplifies to $-1/2$:
$$I = 2\pi \left( \frac{3 - 2i}{-4} \right)$$
$$I = -\frac{\pi(3 - 2i)}{2}$$
$$I = -\frac{3\pi}{2} + \pi i$$

**Answer:** The value of the integral is **$-\frac{\pi}{2}(3 - 2i)$** (or **$-\frac{3\pi}{2} + \pi i$**).

Here are the detailed solutions for the next four questions (Q317 to Q320).

### Q317. Pg 17, CT-II, 3.(b): Evaluate $\oint_C \frac{z^2-2z}{z^2+4} dz$ where C is the circle $|z|=3$

**Solution:**

Let $I = \oint_C \frac{z^2-2z}{z^2+4} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero to find the poles:
$$z^2 + 4 = 0$$
$$z^2 = -4$$
$$z = \pm \sqrt{-4} = \pm 2i$$
There are two simple poles:
1.  $z_1 = 2i$
2.  $z_2 = -2i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 3$. This is a circle centered at the origin with a radius of $3$.
*   **Test $z_1 = 2i$:** $|2i| = 2$. Since $2 < 3$, this pole is **inside** the contour.
*   **Test $z_2 = -2i$:** $|-2i| = 2$. Since $2 < 3$, this pole is **inside** the contour.

Since both poles are enclosed by the contour, we will use **Cauchy's Residue Theorem**:
$$I = 2\pi i \sum \text{Residues} = 2\pi i (R_1 + R_2)$$

**Step 3: Calculate Residue at $z_1 = 2i$.**
For a rational function $F(z) = P(z)/Q(z)$ with a simple pole at $a$, the residue is $\frac{P(a)}{Q'(a)}$.
Here, $P(z) = z^2 - 2z$ and $Q(z) = z^2 + 4$.
$Q'(z) = 2z$.
$$R_1 = \frac{P(2i)}{Q'(2i)} = \frac{(2i)^2 - 2(2i)}{2(2i)}$$
$$R_1 = \frac{4i^2 - 4i}{4i} = \frac{-4 - 4i}{4i}$$
Divide top and bottom by 4:
$$R_1 = \frac{-1 - i}{i}$$
Multiply top and bottom by $i$ to rationalize:
$$R_1 = \frac{(-1 - i)i}{i^2} = \frac{-i - i^2}{-1} = \frac{-i - (-1)}{-1} = \frac{1 - i}{-1} = -1 + i$$

**Step 4: Calculate Residue at $z_2 = -2i$.**
$$R_2 = \frac{P(-2i)}{Q'(-2i)} = \frac{(-2i)^2 - 2(-2i)}{2(-2i)}$$
$$R_2 = \frac{4i^2 + 4i}{-4i} = \frac{-4 + 4i}{-4i}$$
Divide top and bottom by -4:
$$R_2 = \frac{1 - i}{i}$$
Multiply top and bottom by $i$:
$$R_2 = \frac{(1 - i)i}{i^2} = \frac{i - i^2}{-1} = \frac{i - (-1)}{-1} = \frac{1 + i}{-1} = -1 - i$$

**Step 5: Apply the Residue Theorem.**
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i [(-1 + i) + (-1 - i)]$$
$$I = 2\pi i (-2)$$
$$I = -4\pi i$$

**Answer:** The value of the integral is **$-4\pi i$**.

***

### Q318. Pg 19, CT-II, 3.(b): Evaluate $\oint_C \frac{z^2-2z}{(z+1)^2} dz$ where C is the circle $|z|=2$

**Solution:**

Let $I = \oint_C \frac{z^2-2z}{(z+1)^2} dz$.

**Step 1: Identify the singularity.**
Set the denominator to zero:
$$(z+1)^2 = 0 \implies z = -1$$
Because of the squared term, this is a **pole of order 2**.
The numerator $f(z) = z^2 - 2z$ is a polynomial, so it is analytic everywhere.

**Step 2: Check if the pole lies inside the contour.**
The contour $C$ is the circle $|z| = 2$.
The distance to the pole is $|-1| = 1$.
Since $1 < 2$, the pole $z = -1$ is safely **inside** the contour.

**Step 3: Apply the Generalized Cauchy Integral Formula.**
For a higher-order pole, the formula is:
$$\oint_C \frac{f(z)}{(z-a)^{n+1}} dz = \frac{2\pi i}{n!} f^{(n)}(a)$$

Map our parameters to the formula:
*   $a = -1$
*   $n+1 = 2 \implies n = 1$. We need to find the **first derivative** of $f(z)$.
*   $f(z) = z^2 - 2z$

**Step 4: Calculate the derivative.**
$$f(z) = z^2 - 2z$$
$$f'(z) = 2z - 2$$

**Step 5: Evaluate $f'(a)$.**
Substitute $a = -1$ into the first derivative:
$$f'(-1) = 2(-1) - 2$$
$$f'(-1) = -2 - 2 = -4$$

**Step 6: Final calculation.**
Substitute everything into the generalized formula:
$$I = \frac{2\pi i}{1!} f'(-1)$$
$$I = \frac{2\pi i}{1} (-4)$$
$$I = -8\pi i$$

**Answer:** The value of the integral is **$-8\pi i$**.

***

### Q319. Question (5.2): Cauchy's Residue theorem: If $F(z)$ is analytic inside and on a simple closed curve C except for a pole of order m at $z=a$ inside C, Prove that (i) $\frac{1}{2\pi~i}\oint_{C}F(z)dz=lim_{z\rightarrow a}\frac{1}{(m-1)!}\frac{d^{m-1}}{dz^{m-1}}\{(z-a)^{m}F(z)\}$ (ii) if there are two poles at $z=a_{1}$ and $z=a_{2}$ inside C of orders $m_{1}$ and $m_{2}$ respectively, Prove that... (iii) In general if $F(z)$ has a number of poles inside C with residues $R_{1}$, $R_{2}$, $R_{3}$,........., then $\oint_{C}F(z)dz=2\pi i\{R_{1}+R_{2}+R_{3}+\dots\}$

*(Note: Part (i) is identically proven in Q312 and Q314. I will briefly summarize it, and then prove parts (ii) and (iii) which establish the full Residue Theorem).*

**Solution:**

**Part (i): Prove the formula for a single pole of order $m$.**
1.  Since $F(z)$ has a pole of order $m$ at $z=a$, the function $\phi(z) = (z-a)^m F(z)$ is analytic inside and on $C$.
2.  We can rewrite the integral as $\oint_C F(z) dz = \oint_C \frac{\phi(z)}{(z-a)^m} dz$.
3.  Apply the Generalized Cauchy Integral Formula ($n+1=m \implies n=m-1$):
    $$\oint_C \frac{\phi(z)}{(z-a)^m} dz = \frac{2\pi i}{(m-1)!} \phi^{(m-1)}(a)$$
4.  Substitute $\phi(z)$ back in and isolate the limit definition of the derivative:
    $$\oint_C F(z) dz = 2\pi i \left[ \lim_{z \to a} \frac{1}{(m-1)!} \frac{d^{m-1}}{dz^{m-1}} \{ (z-a)^m F(z) \} \right]$$
5.  Divide both sides by $2\pi i$ to match the requested format:
    $$\frac{1}{2\pi i} \oint_C F(z) dz = \lim_{z \to a} \frac{1}{(m-1)!} \frac{d^{m-1}}{dz^{m-1}} \{ (z-a)^m F(z) \}$$
**(Proved)**

---
**Part (ii) & (iii): Prove the generalized theorem for multiple poles.**
We must prove that $\oint_C F(z)dz = 2\pi i \sum R_k$.

**Proof:**
**Step 1: Isolate the singularities.**
Suppose $F(z)$ is analytic inside and on $C$, except at a finite number of isolated poles $a_1, a_2, \dots, a_k$ located inside $C$.
We draw a small, non-overlapping circle $C_1, C_2, \dots, C_k$ around each respective pole $a_1, a_2, \dots, a_k$. We choose the radii small enough so that all these circles lie completely inside $C$ and do not intersect each other.

**Step 2: Apply the Principle of Deformation of Contours.**
The region inside $C$ but outside all the small circles $C_k$ contains no singularities. Therefore, $F(z)$ is completely analytic in this multiply connected region.
By the principle of deformation of contours, the integral around the outer boundary equals the sum of the integrals around all the inner boundaries:
$$\oint_C F(z) dz = \oint_{C_1} F(z) dz + \oint_{C_2} F(z) dz + \dots + \oint_{C_k} F(z) dz$$

**Step 3: Apply the single-pole result (from Part i) to each inner circle.**
Each small circle $C_k$ encloses exactly one pole, $a_k$.
From the definition of a residue (and proven in Part i), the integral around a contour enclosing a single pole is exactly $2\pi i$ times the residue at that pole:
$$\oint_{C_k} F(z) dz = 2\pi i \cdot \text{Res}(F, a_k)$$

**Step 4: Substitute and conclude.**
Substitute these individual residue expressions back into the deformation equation:
$$\oint_C F(z) dz = 2\pi i \cdot \text{Res}(F, a_1) + 2\pi i \cdot \text{Res}(F, a_2) + \dots + 2\pi i \cdot \text{Res}(F, a_k)$$

Factor out $2\pi i$:
$$\oint_C F(z) dz = 2\pi i \left[ \text{Res}(F, a_1) + \text{Res}(F, a_2) + \dots + \text{Res}(F, a_k) \right]$$

If we denote the residues as $R_1, R_2, \dots, R_k$:
$$\oint_C F(z) dz = 2\pi i \{ R_1 + R_2 + R_3 + \dots \}$$
**(Proved)**

***

### Q320. Problem 5.2.1: Evaluate $\oint_{C}\frac{e^{z}}{(z^{2}+\pi^{2})^{2}}dz$ , where C is the circle $|z|=4$

*(Note: This is identically stated and solved in Q242. A concise step-by-step solution is provided below).*

**Solution:**

Let $I = \oint_C \frac{e^z}{(z^2+\pi^2)^2} dz$.

**Step 1: Identify the singularities.**
Denominator is $(z^2 + \pi^2)^2 = [(z-i\pi)(z+i\pi)]^2$.
There are two poles of order 2: $z_1 = i\pi$ and $z_2 = -i\pi$.

**Step 2: Check enclosure.**
Contour $C$ is $|z|=4$.
$|\pm i\pi| = \pi \approx 3.14 < 4$. Both poles are **inside**.
We use Cauchy's Residue Theorem: $I = 2\pi i (R_1 + R_2)$.

**Step 3: Calculate Residue $R_1$ at $z=i\pi$.**
$$R_1 = \lim_{z \to i\pi} \frac{d}{dz} \left[ (z-i\pi)^2 \frac{e^z}{(z-i\pi)^2(z+i\pi)^2} \right] = \lim_{z \to i\pi} \frac{d}{dz} \left[ \frac{e^z}{(z+i\pi)^2} \right]$$
Derivative (quotient rule): $\frac{e^z(z+i\pi-2)}{(z+i\pi)^3}$.
Substitute $z=i\pi$:
$$R_1 = \frac{e^{i\pi}(2i\pi-2)}{(2i\pi)^3} = \frac{-1(2i\pi-2)}{-8i\pi^3} = \frac{2-2i\pi}{8i\pi^3} = \frac{1-i\pi}{4i\pi^3} = \frac{i+\pi}{4\pi^3}$$

**Step 4: Calculate Residue $R_2$ at $z=-i\pi$.**
$$R_2 = \lim_{z \to -i\pi} \frac{d}{dz} \left[ (z+i\pi)^2 \frac{e^z}{(z-i\pi)^2(z+i\pi)^2} \right] = \lim_{z \to -i\pi} \frac{d}{dz} \left[ \frac{e^z}{(z-i\pi)^2} \right]$$
Derivative: $\frac{e^z(z-i\pi-2)}{(z-i\pi)^3}$.
Substitute $z=-i\pi$:
$$R_2 = \frac{e^{-i\pi}(-2i\pi-2)}{(-2i\pi)^3} = \frac{-1(-2i\pi-2)}{8i\pi^3} = \frac{2i\pi+2}{8i\pi^3} = \frac{i\pi+1}{4i\pi^3} = \frac{\pi-i}{4\pi^3}$$

**Step 5: Apply Residue Theorem.**
$$I = 2\pi i (R_1 + R_2) = 2\pi i \left( \frac{\pi+i}{4\pi^3} + \frac{\pi-i}{4\pi^3} \right) = 2\pi i \left( \frac{2\pi}{4\pi^3} \right) = 2\pi i \left( \frac{1}{2\pi^2} \right) = \frac{i}{\pi}$$

**Answer:** The value of the integral is **$\frac{i}{\pi}$**.

Here are the detailed solutions for the next four questions (Q321 to Q324).

### Q321. Problem 5.2.2: Evaluate $\frac{1}{2\pi~i}\oint_{C}\frac{e^{zt}}{(z^{2}+1)^{2}}dz$ if $t>0$ and C is the circle $|z|=3$.

*(Note: This is very similar to Q243, but the denominator is squared, making the poles order 2 instead of simple poles).*

**Solution:**

Let $I = \frac{1}{2\pi i} \oint_C \frac{e^{zt}}{(z^2+1)^2} dz$.

**Step 1: Identify the singularities.**
Set the denominator to zero:
$$(z^2 + 1)^2 = 0$$
Using $i^2 = -1$, factor $z^2+1 = (z-i)(z+i)$:
$$(z - i)^2 (z + i)^2 = 0$$
There are two poles, both of **order 2**:
1.  $z_1 = i$
2.  $z_2 = -i$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 3$.
*   $|i| = 1 < 3$ (**Inside**)
*   $|-i| = 1 < 3$ (**Inside**)
Both poles are enclosed. 
By Cauchy's Residue Theorem, $\oint_C F(z)dz = 2\pi i \sum \text{Res}$.
Because our expression already has $\frac{1}{2\pi i}$ in front, it simplifies perfectly:
$$I = \frac{1}{2\pi i} \left[ 2\pi i (R_1 + R_2) \right] = R_1 + R_2$$

**Step 3: Calculate Residue $R_1$ at $z=i$ (Pole of order 2).**
Formula: $R_1 = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 \frac{e^{zt}}{(z-i)^2(z+i)^2} \right]$
$$R_1 = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{zt}}{(z+i)^2} \right]$$
Use the quotient rule: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$
*   $u = e^{zt} \implies u' = t e^{zt}$
*   $v = (z+i)^2 \implies v' = 2(z+i)$
$$\frac{d}{dz} \left[ \frac{e^{zt}}{(z+i)^2} \right] = \frac{t e^{zt} (z+i)^2 - e^{zt} [2(z+i)]}{(z+i)^4}$$
Factor out $e^{zt}(z+i)$ from numerator:
$$= \frac{e^{zt}(z+i) [t(z+i) - 2]}{(z+i)^4} = \frac{e^{zt}[t(z+i) - 2]}{(z+i)^3}$$
Substitute $z = i$:
$$R_1 = \frac{e^{it}[t(i+i) - 2]}{(i+i)^3} = \frac{e^{it}[2it - 2]}{(2i)^3} = \frac{e^{it}(2it - 2)}{-8i}$$
Divide numerator and denominator by 2:
$$R_1 = \frac{e^{it}(it - 1)}{-4i} = \frac{-e^{it}(it - 1)}{4i} = \frac{e^{it}(1 - it)}{4i}$$

**Step 4: Calculate Residue $R_2$ at $z=-i$ (Pole of order 2).**
$$R_2 = \lim_{z \to -i} \frac{d}{dz} \left[ (z+i)^2 \frac{e^{zt}}{(z-i)^2(z+i)^2} \right] = \lim_{z \to -i} \frac{d}{dz} \left[ \frac{e^{zt}}{(z-i)^2} \right]$$
Using the same quotient rule process:
$$\frac{d}{dz} \left[ \frac{e^{zt}}{(z-i)^2} \right] = \frac{e^{zt}[t(z-i) - 2]}{(z-i)^3}$$
Substitute $z = -i$:
$$R_2 = \frac{e^{-it}[t(-i-i) - 2]}{(-i-i)^3} = \frac{e^{-it}[-2it - 2]}{(-2i)^3} = \frac{e^{-it}(-2it - 2)}{8i}$$
Divide by 2:
$$R_2 = \frac{e^{-it}(-it - 1)}{4i} = -\frac{e^{-it}(1 + it)}{4i}$$

**Step 5: Sum the residues.**
$$I = R_1 + R_2 = \frac{e^{it}(1 - it)}{4i} - \frac{e^{-it}(1 + it)}{4i}$$
$$I = \frac{1}{2} \left[ \frac{e^{it} - ite^{it} - e^{-it} - ite^{-it}}{2i} \right]$$
Group terms to form trigonometric functions ($\sin(t) = \frac{e^{it}-e^{-it}}{2i}$, $\cos(t) = \frac{e^{it}+e^{-it}}{2}$):
$$I = \frac{1}{2} \left[ \frac{e^{it} - e^{-it}}{2i} - t \frac{e^{it} + e^{-it}}{2i} \right]$$
$$I = \frac{1}{2} \left[ \sin(t) - t \left( \frac{e^{it} + e^{-it}}{2i} \cdot \frac{i}{i} \right) \right]$$
Notice that $\frac{e^{it} + e^{-it}}{2i} = \frac{1}{i} \cos(t) = -i \cos(t)$. However, let's look closer at the grouping.
$$I = \frac{1}{2} \left[ \frac{e^{it} - e^{-it}}{2i} - \frac{t(e^{it} + e^{-it})}{2i} \right]$$
$$I = \frac{1}{2} \left( \sin t \right) - \frac{t}{2i} \cos t$$
Multiply top and bottom of second term by $i$:
$$I = \frac{1}{2} \sin t - \frac{it}{-2} \cos t = \frac{1}{2} \sin t + \frac{i}{2} t \cos t$$
*(Wait, let's re-evaluate the combination, usually Inverse Laplace transforms yield strictly real functions. Let's re-check the $R_1+R_2$ sum).*
$$I = \frac{e^{it} - ite^{it} - e^{-it} - ite^{-it}}{4i}$$
$$I = \frac{(e^{it} - e^{-it}) - it(e^{it} + e^{-it})}{4i}$$
$$I = \frac{1}{2} \left[ \frac{e^{it} - e^{-it}}{2i} \right] - \frac{t}{2} \left[ \frac{e^{it} + e^{-it}}{2} \right]$$
$$I = \frac{1}{2} \sin(t) - \frac{1}{2} t \cos(t)$$
*(Ah, the $i$ in the denominator canceled nicely with the $i$ from $it$ in the numerator. Let's trace it: $\frac{-it(e^{it} + e^{-it})}{4i} = \frac{-t(e^{it} + e^{-it})}{4} = -\frac{1}{2} t (\frac{e^{it} + e^{-it}}{2}) = -\frac{1}{2} t \cos t$. Yes, this is correct and yields a purely real function).*

**Answer:** The value of the integral is **$\frac{1}{2} (\sin t - t \cos t)$**.

***

### Q322. Problem 5.2.3: Find the residues of $f(z)=\frac{z^{2}}{(z-1)(z+2)^{2}}$ at its singular points.

*(Note: The integration of this function was performed in Q247. We are asked to explicitly find only the residues here).*

**Solution:**

Given $f(z) = \frac{z^2}{(z-1)(z+2)^2}$.

**Step 1: Identify the singular points.**
Set the denominator equal to zero:
$$(z-1)(z+2)^2 = 0$$
There are two singular points:
1.  **$z = 1$**: A simple pole (order 1).
2.  **$z = -2$**: A pole of order 2.

**Step 2: Calculate the Residue at $z=1$ (Simple Pole).**
For a simple pole at $a$, the residue is calculated as:
$$\text{Res}(f, a) = \lim_{z \to a} (z-a) f(z)$$
$$\text{Res}(f, 1) = \lim_{z \to 1} (z-1) \frac{z^2}{(z-1)(z+2)^2}$$
Cancel the $(z-1)$ terms:
$$\text{Res}(f, 1) = \lim_{z \to 1} \frac{z^2}{(z+2)^2}$$
Evaluate by direct substitution $z=1$:
$$\text{Res}(f, 1) = \frac{1^2}{(1+2)^2} = \frac{1}{3^2} = \frac{1}{9}$$

**Step 3: Calculate the Residue at $z=-2$ (Pole of order 2).**
For a pole of order $m=2$ at $a$, the residue is:
$$\text{Res}(f, a) = \lim_{z \to a} \frac{d}{dz} \left[ (z-a)^2 f(z) \right]$$
$$\text{Res}(f, -2) = \lim_{z \to -2} \frac{d}{dz} \left[ (z+2)^2 \frac{z^2}{(z-1)(z+2)^2} \right]$$
Cancel the $(z+2)^2$ terms:
$$\text{Res}(f, -2) = \lim_{z \to -2} \frac{d}{dz} \left[ \frac{z^2}{z-1} \right]$$
Use the quotient rule to differentiate:
$$\frac{d}{dz} \left( \frac{z^2}{z-1} \right) = \frac{(2z)(z-1) - (z^2)(1)}{(z-1)^2} = \frac{2z^2 - 2z - z^2}{(z-1)^2} = \frac{z^2 - 2z}{(z-1)^2}$$
Evaluate the limit by direct substitution $z=-2$:
$$\text{Res}(f, -2) = \frac{(-2)^2 - 2(-2)}{(-2-1)^2} = \frac{4 + 4}{(-3)^2} = \frac{8}{9}$$

**Answer:**
*   Residue at $z=1$ is **$1/9$**.
*   Residue at $z=-2$ is **$8/9$**.

***

### Q323. Problem 5.2.4: Evaluate the following, using Cauchy's residue theorem (i) $\int_{C}\frac{4-3z}{z(z-1)(z-2)}dz,$ where C is $|z|=3/2$

*(Note: This is numerically identical to Q271, where it was solved using Cauchy's Integral formula and partial fractions. Here, we MUST solve it using the Residue Theorem as requested).*

**Solution:**

Let $I = \oint_C \frac{4-3z}{z(z-1)(z-2)} dz$.

**Step 1: Identify the singular points.**
Set the denominator to zero:
$$z(z-1)(z-2) = 0$$
There are three simple poles:
1.  $z_1 = 0$
2.  $z_2 = 1$
3.  $z_3 = 2$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 3/2 = 1.5$.
*   $|0| = 0 < 1.5$ (**Inside**)
*   $|1| = 1 < 1.5$ (**Inside**)
*   $|2| = 2 > 1.5$ (**Outside**)

We only calculate residues for the enclosed poles: $z=0$ and $z=1$.

**Step 3: Calculate Residues.**
For a simple pole at $a$, $\text{Res}(a) = \lim_{z\to a} (z-a)F(z)$.
*   **Residue at $z_1 = 0$:**
    $$R_1 = \lim_{z \to 0} z \cdot \frac{4-3z}{z(z-1)(z-2)} = \lim_{z \to 0} \frac{4-3z}{(z-1)(z-2)}$$
    $$R_1 = \frac{4 - 3(0)}{(0-1)(0-2)} = \frac{4}{(-1)(-2)} = \frac{4}{2} = 2$$

*   **Residue at $z_2 = 1$:**
    $$R_2 = \lim_{z \to 1} (z-1) \frac{4-3z}{z(z-1)(z-2)} = \lim_{z \to 1} \frac{4-3z}{z(z-2)}$$
    $$R_2 = \frac{4 - 3(1)}{1(1-2)} = \frac{1}{1(-1)} = \frac{1}{-1} = -1$$

**Step 4: Apply Cauchy's Residue Theorem.**
The theorem states $I = 2\pi i \sum \text{Residues enclosed}$.
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i (2 + (-1))$$
$$I = 2\pi i (1)$$
$$I = 2\pi i$$

**Answer:** The value of the integral is **$2\pi i$**.

***

### Q324. Problem (ii): $\int_{C}\frac{z-2}{z(z-1)}dz$ $C:|z|=2$

**Solution:**

Let $I = \oint_C \frac{z-2}{z(z-1)} dz$.

**Step 1: Identify the singular points.**
Set the denominator to zero:
$$z(z-1) = 0$$
There are two simple poles:
1.  $z_1 = 0$
2.  $z_2 = 1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 2$.
*   $|0| = 0 < 2$ (**Inside**)
*   $|1| = 1 < 2$ (**Inside**)

Both poles are enclosed by the contour.

**Step 3: Calculate Residues.**
For a simple pole at $a$, $\text{Res}(a) = \lim_{z\to a} (z-a)F(z)$.
*   **Residue at $z_1 = 0$:**
    $$R_1 = \lim_{z \to 0} z \cdot \frac{z-2}{z(z-1)} = \lim_{z \to 0} \frac{z-2}{z-1}$$
    $$R_1 = \frac{0-2}{0-1} = \frac{-2}{-1} = 2$$

*   **Residue at $z_2 = 1$:**
    $$R_2 = \lim_{z \to 1} (z-1) \frac{z-2}{z(z-1)} = \lim_{z \to 1} \frac{z-2}{z}$$
    $$R_2 = \frac{1-2}{1} = \frac{-1}{1} = -1$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \sum \text{Residues}$$
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i (2 + (-1))$$
$$I = 2\pi i (1)$$
$$I = 2\pi i$$

**Answer:** The value of the integral is **$2\pi i$**.

Here are the detailed solutions for the next four questions (Q325 to Q328).

### Q325. Example 2: The function $f(z) = 1/(z – 1)^{2}(z – 3)$ has a pole of order 2 at $z = 1$. Find the residues.

**Solution:**

We need to find the residues for the function $f(z) = \frac{1}{(z-1)^2(z-3)}$ at all of its singular points.

**Step 1: Identify the singular points (poles).**
Set the denominator equal to zero:
$$(z-1)^2(z-3) = 0$$
This yields two poles:
1.  **$z_1 = 1$**: This is a **pole of order 2** (because of the squared term).
2.  **$z_2 = 3$**: This is a **simple pole** (order 1).

**Step 2: Calculate the residue at $z_1 = 1$ (Pole of order 2).**
The general formula for the residue at a pole $a$ of order $m$ is:
$$\text{Res}(f, a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}} \left[ (z-a)^m f(z) \right]$$
Here, $a = 1$ and $m = 2$. Therefore, $m-1 = 1$.
$$\text{Res}(f, 1) = \frac{1}{1!} \lim_{z \to 1} \frac{d}{dz} \left[ (z-1)^2 \frac{1}{(z-1)^2(z-3)} \right]$$
Cancel the $(z-1)^2$ terms:
$$\text{Res}(f, 1) = \lim_{z \to 1} \frac{d}{dz} \left[ \frac{1}{z-3} \right]$$
Take the derivative using the power rule (rewrite as $(z-3)^{-1}$):
$$\frac{d}{dz} (z-3)^{-1} = -1(z-3)^{-2} = \frac{-1}{(z-3)^2}$$
Evaluate the limit as $z \to 1$:
$$\text{Res}(f, 1) = \frac{-1}{(1-3)^2} = \frac{-1}{(-2)^2} = \frac{-1}{4} = -\frac{1}{4}$$

**Step 3: Calculate the residue at $z_2 = 3$ (Simple pole).**
The formula for a simple pole is:
$$\text{Res}(f, a) = \lim_{z \to a} (z-a) f(z)$$
$$\text{Res}(f, 3) = \lim_{z \to 3} (z-3) \frac{1}{(z-1)^2(z-3)}$$
Cancel the $(z-3)$ terms:
$$\text{Res}(f, 3) = \lim_{z \to 3} \frac{1}{(z-1)^2}$$
Evaluate the limit as $z \to 3$:
$$\text{Res}(f, 3) = \frac{1}{(3-1)^2} = \frac{1}{(2)^2} = \frac{1}{4}$$

*(Self-check: A known property of rational functions where the degree of the denominator is at least 2 greater than the numerator is that the sum of all residues is zero. $-1/4 + 1/4 = 0$. This confirms our calculation).*

**Answer:** 
*   The residue at $z=1$ is **$-1/4$**.
*   The residue at $z=3$ is **$1/4$**.

***

### Q326. Example 4: Evaluate $\int_{c}\frac{d~z}{z^{2}-1}$ where (b) the contour C is the circle |z|= 2

**Solution:**

Let $I = \oint_C \frac{1}{z^2-1} dz$.

**Step 1: Identify the singularities.**
Factor the denominator and set it to zero:
$$z^2 - 1 = 0 \implies (z-1)(z+1) = 0$$
There are two simple poles:
1.  $z_1 = 1$
2.  $z_2 = -1$

**Step 2: Check which poles lie inside the contour.**
The contour $C$ is the circle $|z| = 2$. It is centered at the origin with a radius of $2$.
*   **Test $z_1 = 1$:** $|1| = 1 < 2$. The pole $z=1$ is **inside**.
*   **Test $z_2 = -1$:** $|-1| = 1 < 2$. The pole $z=-1$ is **inside**.

Because both poles are enclosed, we will use Cauchy's Residue Theorem: $I = 2\pi i (R_1 + R_2)$.

**Step 3: Calculate Residue $R_1$ at $z=1$.**
$$R_1 = \lim_{z \to 1} (z-1) \frac{1}{(z-1)(z+1)} = \lim_{z \to 1} \frac{1}{z+1}$$
$$R_1 = \frac{1}{1+1} = \frac{1}{2}$$

**Step 4: Calculate Residue $R_2$ at $z=-1$.**
$$R_2 = \lim_{z \to -1} (z+1) \frac{1}{(z-1)(z+1)} = \lim_{z \to -1} \frac{1}{z-1}$$
$$R_2 = \frac{1}{-1-1} = -\frac{1}{2}$$

**Step 5: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \sum \text{Residues}$$
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i \left( \frac{1}{2} - \frac{1}{2} \right)$$
$$I = 2\pi i (0)$$
$$I = 0$$

**Answer:** The value of the integral is **$0$**.

***

### Q327. Pg 1, Q4(i): Evaluate $\int_0^\infty \frac{1}{x^4+a^4} dx$

*(Note: We assume $a > 0$ and $x$ is real. This is a classic contour integration problem over the real line. It is conceptually identical to Q339).*

**Solution:**

Let $I = \int_0^\infty \frac{1}{x^4+a^4} dx$.

**Step 1: Extend the integral to the entire real line.**
The integrand $f(x) = \frac{1}{x^4+a^4}$ is an *even* function (since $(-x)^4 = x^4$).
Therefore, the integral from $0$ to $\infty$ is exactly half of the integral from $-\infty$ to $\infty$:
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{x^4+a^4} dx$$

**Step 2: Set up the complex contour integral.**
We consider the complex function $f(z) = \frac{1}{z^4+a^4}$.
We integrate over a closed semi-circular contour $\Gamma$ in the upper half-plane, consisting of:
1.  The real axis segment $C_R$ from $-R$ to $R$.
2.  The upper semi-circle $C_S$ defined by $|z|=R, 0 \le \theta \le \pi$.

As $R \to \infty$, the integral over the semi-circle $C_S$ goes to zero because the degree of the denominator (4) is $\ge$ the degree of the numerator (0) + 2. Thus, the closed contour integral equals the integral over the entire real line:
$$\oint_\Gamma f(z) dz = \int_{-\infty}^\infty f(x) dx$$

**Step 3: Identify poles in the upper half-plane.**
Find the roots of $z^4 + a^4 = 0 \implies z^4 = -a^4$.
Using polar form, $-a^4 = a^4 e^{i(\pi + 2k\pi)}$.
The four roots are $z_k = a e^{i(\pi + 2k\pi)/4}$ for $k=0,1,2,3$.
*   $k=0: z_0 = a e^{i\pi/4}$ (Quadrant I, upper half)
*   $k=1: z_1 = a e^{i3\pi/4}$ (Quadrant II, upper half)
*   $k=2: z_2 = a e^{i5\pi/4}$ (Quadrant III, lower half)
*   $k=3: z_3 = a e^{i7\pi/4}$ (Quadrant IV, lower half)

Only $z_0$ and $z_1$ lie inside our upper half-plane contour $\Gamma$.

**Step 4: Calculate the residues at $z_0$ and $z_1$.**
For $f(z) = P(z)/Q(z)$ with simple poles, $\text{Res}(z_k) = \frac{P(z_k)}{Q'(z_k)} = \frac{1}{4z_k^3}$.
To simplify, multiply top and bottom by $z_k$: $\text{Res}(z_k) = \frac{z_k}{4z_k^4}$.
Since $z_k$ is a root of $z^4+a^4=0$, we know $z_k^4 = -a^4$. Therefore:
$$\text{Res}(z_k) = \frac{z_k}{4(-a^4)} = -\frac{z_k}{4a^4}$$

*   **Residue at $z_0$:** $R_0 = -\frac{a e^{i\pi/4}}{4a^4} = -\frac{e^{i\pi/4}}{4a^3}$
*   **Residue at $z_1$:** $R_1 = -\frac{a e^{i3\pi/4}}{4a^4} = -\frac{e^{i3\pi/4}}{4a^3}$

**Step 5: Apply Residue Theorem.**
$$\int_{-\infty}^\infty f(x) dx = 2\pi i (R_0 + R_1)$$
$$\int_{-\infty}^\infty f(x) dx = 2\pi i \left( -\frac{1}{4a^3} \right) (e^{i\pi/4} + e^{i3\pi/4})$$
Expand the exponentials using Euler's formula:
$e^{i\pi/4} = \cos 45^\circ + i\sin 45^\circ = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$
$e^{i3\pi/4} = \cos 135^\circ + i\sin 135^\circ = -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$
Sum: $(e^{i\pi/4} + e^{i3\pi/4}) = \left(\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}}\right) + i\left(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}\right) = i\frac{2}{\sqrt{2}} = i\sqrt{2}$.

Substitute back into the integral:
$$\int_{-\infty}^\infty f(x) dx = 2\pi i \left( -\frac{1}{4a^3} \right) (i\sqrt{2})$$
$$= 2\pi i^2 \left( -\frac{\sqrt{2}}{4a^3} \right) = 2\pi(-1) \left( -\frac{\sqrt{2}}{4a^3} \right) = \frac{2\pi\sqrt{2}}{4a^3} = \frac{\pi\sqrt{2}}{2a^3}$$

**Step 6: Final evaluation for half the real line.**
$$I = \frac{1}{2} \int_{-\infty}^\infty f(x) dx = \frac{1}{2} \left( \frac{\pi\sqrt{2}}{2a^3} \right) = \frac{\pi\sqrt{2}}{4a^3}$$

**Answer:** The value of the integral is **$\frac{\pi\sqrt{2}}{4a^3}$**.

***

### Q328. Pg 1, Q4(ii): Evaluate $\int_0^{2\pi} \frac{d\theta}{a+b\sin\theta}$ if $a > |b|$.

*(Note: This is a classic trigonometric contour integration problem. It is numerically identical to Q345).*

**Solution:**

Let $I = \int_0^{2\pi} \frac{1}{a+b\sin\theta} d\theta$.

**Step 1: Substitute complex variables on the unit circle.**
We map the integration from the real interval $[0, 2\pi]$ to the unit circle $C$ in the complex plane, defined by $|z|=1$.
Let $z = e^{i\theta}$.
Then $dz = ie^{i\theta} d\theta \implies d\theta = \frac{dz}{iz}$.
Using Euler's formula, $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z^{-1}}{2i} = \frac{z^2 - 1}{2iz}$.

**Step 2: Transform the integral into a complex contour integral.**
Substitute these into $I$:
$$I = \oint_C \frac{1}{a + b\left(\frac{z^2 - 1}{2iz}\right)} \frac{dz}{iz}$$
Multiply the denominator terms by $iz$:
$$I = \oint_C \frac{1}{iaz + b\left(\frac{z^2 - 1}{2}\right)} dz$$
Multiply numerator and denominator by 2 to clear fractions:
$$I = \oint_C \frac{2}{2iaz + bz^2 - b} dz$$
$$I = \oint_C \frac{2}{bz^2 + 2iaz - b} dz$$

**Step 3: Find the singularities (poles).**
Set the denominator to zero and use the quadratic formula for $z$:
$$bz^2 + 2iaz - b = 0$$
$$z = \frac{-2ia \pm \sqrt{(2ia)^2 - 4(b)(-b)}}{2b} = \frac{-2ia \pm \sqrt{-4a^2 + 4b^2}}{2b}$$
Factor out $4$ from the root:
$$z = \frac{-2ia \pm 2\sqrt{-(a^2 - b^2)}}{2b} = \frac{-ia \pm i\sqrt{a^2 - b^2}}{b}$$
Let the two roots be:
$$z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}i \quad \text{and} \quad z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}i$$

**Step 4: Determine which pole lies inside the unit circle.**
We are given $a > |b| > 0$. This ensures that $\sqrt{a^2-b^2}$ is a real, positive number, and $\sqrt{a^2-b^2} < a$.
Let's analyze the moduli of the roots:
$|z_1 \cdot z_2| = \left| \frac{-b}{b} \right| = 1$. (Product of roots is $c/a$).
Since their product is 1, one root must be inside the unit circle ($|z|<1$) and the other outside ($|z|>1$).
Look at $z_2$: its magnitude is $\frac{a + \sqrt{a^2-b^2}}{|b|}$. Since $a > |b|$, this fraction is clearly $> 1$.
Therefore, $z_2$ is outside the circle, leaving **$z_1$ as the only pole inside the contour**.

**Step 5: Calculate the Residue at $z_1$.**
Let $F(z) = \frac{2}{b(z-z_1)(z-z_2)}$.
$$\text{Res}(z_1) = \lim_{z \to z_1} (z-z_1) F(z) = \lim_{z \to z_1} \frac{2/b}{z - z_2} = \frac{2/b}{z_1 - z_2}$$
Calculate the denominator difference $(z_1 - z_2)$:
$$z_1 - z_2 = \left( \frac{-a + \sqrt{a^2-b^2}}{b}i \right) - \left( \frac{-a - \sqrt{a^2-b^2}}{b}i \right) = \frac{2\sqrt{a^2-b^2}}{b}i$$
*(Note: This exact derivation was shown previously in Q129).*

Substitute this back into the residue formula:
$$\text{Res}(z_1) = \frac{2/b}{\frac{2\sqrt{a^2-b^2}}{b}i} = \frac{1}{i\sqrt{a^2-b^2}}$$

**Step 6: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \cdot \text{Res}(z_1)$$
$$I = 2\pi i \left( \frac{1}{i\sqrt{a^2-b^2}} \right)$$
The $i$ cancels out completely:
$$I = \frac{2\pi}{\sqrt{a^2-b^2}}$$

**Answer:** The value of the integral is **$\frac{2\pi}{\sqrt{a^2-b^2}}$**.

Here are the detailed solutions for the next four questions (Q329 to Q332).

### Q329. Pg 2, Q4(b)(i): Evaluate $\int_0^\infty \frac{dx}{1+x^6}$

**Solution:**

Let $I = \int_0^\infty \frac{1}{1+x^6} dx$.

**Step 1: Extend to the entire real line.**
The integrand $f(x) = \frac{1}{1+x^6}$ is an **even function** (since $(-x)^6 = x^6$).
Therefore, the integral from $0$ to $\infty$ is exactly half of the integral over the entire real line:
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{1+x^6} dx$$

**Step 2: Set up the complex contour integral.**
We evaluate the contour integral $\oint_C f(z) dz$ where $f(z) = \frac{1}{1+z^6}$.
The contour $C$ is a closed semi-circle in the upper half-plane, consisting of the real axis from $-R$ to $R$, and the semi-circular arc $C_R$ of radius $R$.
As $R \to \infty$, the integral over the arc $C_R$ goes to $0$ (because the degree of the denominator is 6, which is $\ge$ degree of numerator + 2).
Thus, $\oint_C f(z) dz = \int_{-\infty}^\infty f(x) dx$.

**Step 3: Identify the poles in the upper half-plane.**
Set the denominator to zero:
$$z^6 + 1 = 0 \implies z^6 = -1$$
In polar form, $-1 = e^{i(\pi + 2k\pi)}$.
The 6 roots are $z_k = e^{i\frac{\pi + 2k\pi}{6}}$ for $k = 0, 1, 2, 3, 4, 5$.
We only need the poles in the **upper half-plane** (where the angle is between $0$ and $\pi$):
*   $k=0 \implies z_0 = e^{i\pi/6}$
*   $k=1 \implies z_1 = e^{i3\pi/6} = e^{i\pi/2} = i$
*   $k=2 \implies z_2 = e^{i5\pi/6}$

**Step 4: Calculate the residues.**
For a function $f(z) = \frac{P(z)}{Q(z)}$ with simple poles, the residue is $\frac{P(a)}{Q'(a)}$.
Here, $P(z) = 1$ and $Q(z) = 1+z^6 \implies Q'(z) = 6z^5$.
So, $\text{Res}(z_k) = \frac{1}{6z_k^5}$.
To make calculation easier, multiply top and bottom by $z_k$:
$$\text{Res}(z_k) = \frac{z_k}{6z_k^6}$$
Since $z_k$ is a root of $z^6 = -1$, we substitute $z_k^6 = -1$:
$$\text{Res}(z_k) = -\frac{z_k}{6}$$

Now calculate the three residues:
*   $R_0 = -\frac{1}{6} e^{i\pi/6} = -\frac{1}{6} \left( \cos\frac{\pi}{6} + i\sin\frac{\pi}{6} \right) = -\frac{1}{6} \left( \frac{\sqrt{3}}{2} + i\frac{1}{2} \right)$
*   $R_1 = -\frac{1}{6} (i) = -i\frac{1}{6}$
*   $R_2 = -\frac{1}{6} e^{i5\pi/6} = -\frac{1}{6} \left( \cos\frac{5\pi}{6} + i\sin\frac{5\pi}{6} \right) = -\frac{1}{6} \left( -\frac{\sqrt{3}}{2} + i\frac{1}{2} \right)$

**Step 5: Apply Cauchy's Residue Theorem.**
$$\int_{-\infty}^\infty \frac{dx}{1+x^6} = 2\pi i (R_0 + R_1 + R_2)$$

Sum the residues:
$$R_0 + R_1 + R_2 = -\frac{1}{6} \left[ \left(\frac{\sqrt{3}}{2} + i\frac{1}{2}\right) + i + \left(-\frac{\sqrt{3}}{2} + i\frac{1}{2}\right) \right]$$
The real parts cancel out ($\frac{\sqrt{3}}{2} - \frac{\sqrt{3}}{2} = 0$).
$$= -\frac{1}{6} \left[ i\frac{1}{2} + i + i\frac{1}{2} \right] = -\frac{1}{6} [ 2i ] = -i\frac{1}{3}$$

Substitute the sum back into the theorem:
$$\int_{-\infty}^\infty \frac{dx}{1+x^6} = 2\pi i \left( -i\frac{1}{3} \right) = -2\pi i^2 \frac{1}{3}$$
Since $i^2 = -1$:
$$\int_{-\infty}^\infty \frac{dx}{1+x^6} = \frac{2\pi}{3}$$

**Step 6: Final evaluation.**
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{1+x^6} dx = \frac{1}{2} \left( \frac{2\pi}{3} \right) = \frac{\pi}{3}$$

**Answer:** The value of the integral is **$\frac{\pi}{3}$**.

***

### Q330. Pg 2, Q4(b)(ii): Evaluate $\int_0^\infty \frac{\sin x}{x} dx$

**Solution:**

This is the famous Dirichlet integral. We evaluate it using a complex contour.

**Step 1: Relate to a complex function.**
We know that $\sin x$ is the imaginary part of $e^{ix}$. Also, the integrand $\frac{\sin x}{x}$ is an even function.
$$I = \int_0^\infty \frac{\sin x}{x} dx = \frac{1}{2} \int_{-\infty}^\infty \frac{\sin x}{x} dx = \frac{1}{2} \text{Im} \left( \int_{-\infty}^\infty \frac{e^{ix}}{x} dx \right)$$

**Step 2: Choose the contour.**
We consider the complex function $f(z) = \frac{e^{iz}}{z}$.
This function has a simple pole exactly on the real axis at $z = 0$.
We integrate over an **indented semi-circular contour** $\Gamma$ in the upper half-plane. It consists of:
1.  The real axis from $-R$ to $-r$.
2.  A small semi-circle $C_r$ of radius $r$ around the origin (traversed clockwise).
3.  The real axis from $r$ to $R$.
4.  A large semi-circle $C_R$ of radius $R$ (traversed counter-clockwise).

**Step 3: Apply Cauchy's Integral Theorem.**
Because we indented the contour to avoid the pole at $z=0$, the function $f(z)$ is analytic everywhere *inside* the closed contour $\Gamma$.
$$\oint_\Gamma \frac{e^{iz}}{z} dz = 0$$
$$\int_{-R}^{-r} \frac{e^{ix}}{x} dx + \int_{C_r} \frac{e^{iz}}{z} dz + \int_r^R \frac{e^{ix}}{x} dx + \int_{C_R} \frac{e^{iz}}{z} dz = 0$$

**Step 4: Evaluate the limits as $R \to \infty$ and $r \to 0$.**
*   **Large semi-circle ($C_R$):** By Jordan's Lemma, since $|1/z| \to 0$ uniformly as $R \to \infty$ in the upper half-plane, $\lim_{R \to \infty} \int_{C_R} \frac{e^{iz}}{z} dz = 0$.
*   **Small semi-circle ($C_r$):** The integral over a small circular arc around a simple pole $a$ is $\theta i \text{Res}(a)$, where $\theta$ is the angle of the arc. Since $C_r$ is a half-circle ($\pi$) traversed *clockwise* (negative direction), the integral is:
    $$\lim_{r \to 0} \int_{C_r} \frac{e^{iz}}{z} dz = -\pi i \cdot \text{Res}(0)$$
    The residue at $z=0$ is $\lim_{z \to 0} z \frac{e^{iz}}{z} = e^0 = 1$.
    So, the integral over $C_r$ evaluates to $-\pi i (1) = -\pi i$.

**Step 5: Calculate the Principal Value integral.**
Substituting these limits back into our contour equation:
$$\left( \lim_{r \to 0, R \to \infty} \left[ \int_{-R}^{-r} \frac{e^{ix}}{x} dx + \int_r^R \frac{e^{ix}}{x} dx \right] \right) - \pi i + 0 = 0$$
The bracketed term defines the Cauchy Principal Value (P.V.) of the integral over the real line:
$$\text{P.V.} \int_{-\infty}^\infty \frac{e^{ix}}{x} dx = \pi i$$

**Step 6: Extract the final answer.**
Euler's formula gives $\frac{e^{ix}}{x} = \frac{\cos x}{x} + i\frac{\sin x}{x}$.
$$\int_{-\infty}^\infty \frac{\cos x}{x} dx + i \int_{-\infty}^\infty \frac{\sin x}{x} dx = 0 + i\pi$$
Equating the imaginary parts:
$$\int_{-\infty}^\infty \frac{\sin x}{x} dx = \pi$$

Finally, since we need the integral from $0$ to $\infty$:
$$I = \frac{1}{2} (\pi) = \frac{\pi}{2}$$

**Answer:** The value of the integral is **$\frac{\pi}{2}$**.

***

### Q331. Pg 4, Q4(a): Evaluate $\int_0^\infty \frac{dx}{x^6+1}$

*(Note: This is identically stated and solved in Q329. A brief summary of the solution is provided below).*

**Solution:**

Let $I = \int_0^\infty \frac{1}{x^6+1} dx$.
Because the integrand is an even function, $I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{z^6+1} dz$ evaluated over the standard closed upper-half plane semi-circle contour.

1.  **Poles:** $z^6 = -1$. The poles in the upper half-plane are $z_0 = e^{i\pi/6}$, $z_1 = e^{i\pi/2} = i$, and $z_2 = e^{i5\pi/6}$.
2.  **Residues:** The residue at a simple pole $z_k$ for $1/(z^6+1)$ is $\frac{1}{6z_k^5} = -\frac{z_k}{6}$.
    *   $R_0 = -\frac{1}{6}(\frac{\sqrt{3}}{2} + i\frac{1}{2})$
    *   $R_1 = -\frac{1}{6}(i)$
    *   $R_2 = -\frac{1}{6}(-\frac{\sqrt{3}}{2} + i\frac{1}{2})$
3.  **Sum of Residues:** $R_0 + R_1 + R_2 = -\frac{1}{6}(2i) = -\frac{i}{3}$.
4.  **Contour Integral:** $\int_{-\infty}^\infty \frac{dx}{x^6+1} = 2\pi i (-\frac{i}{3}) = \frac{2\pi}{3}$.
5.  **Final Evaluation:** $I = \frac{1}{2} \left( \frac{2\pi}{3} \right) = \frac{\pi}{3}$.

**Answer:** The value of the integral is **$\frac{\pi}{3}$**.

***

### Q332. Pg 4, Q4(b): Evaluate $\int_0^{2\pi} \frac{\cos 3\theta}{5+4\cos 2\theta} d\theta$.

**Solution:**

Let $I = \int_0^{2\pi} \frac{\cos 3\theta}{5+4\cos 2\theta} d\theta$.
This is a standard trigonometric contour integral, evaluated by mapping it to the unit circle $|z|=1$.

**Step 1: Simplify using complex exponentials.**
We know $\cos 3\theta = \text{Re}(e^{i3\theta}) = \text{Re}(z^3)$. Because the denominator $\cos 2\theta$ is purely real and integration is a linear operator over the real parameter $\theta$, we can rewrite the integral as:
$$I = \text{Re} \left[ \int_0^{2\pi} \frac{e^{i3\theta}}{5+4\cos 2\theta} d\theta \right]$$

**Step 2: Map to the unit circle.**
Let $z = e^{i\theta}$. Then $dz = iz d\theta \implies d\theta = \frac{dz}{iz}$.
For the denominator: $\cos 2\theta = \frac{e^{i2\theta} + e^{-i2\theta}}{2} = \frac{z^2 + z^{-2}}{2}$.
Substitute these into our complex integral over the contour $C$ ($|z|=1$):
$$I_c = \oint_C \frac{z^3}{5 + 4\left(\frac{z^2 + z^{-2}}{2}\right)} \frac{dz}{iz}$$
$$I_c = \oint_C \frac{z^3}{5 + 2z^2 + 2z^{-2}} \frac{dz}{iz}$$

Multiply the numerator and denominator by $z^2$ to clear the negative exponent:
$$I_c = \oint_C \frac{z^3 \cdot z^2}{(5z^2 + 2z^4 + 2)} \frac{dz}{iz}$$
$$I_c = \oint_C \frac{z^5}{i z (2z^4 + 5z^2 + 2)} dz = \frac{1}{i} \oint_C \frac{z^4}{2z^4 + 5z^2 + 2} dz$$

Let $F(z) = \frac{z^4}{2z^4 + 5z^2 + 2}$.

**Step 3: Find the singularities.**
Set the denominator to zero:
$$2z^4 + 5z^2 + 2 = 0$$
This is a quadratic in terms of $z^2$. Factor it:
$$(2z^2 + 1)(z^2 + 2) = 0$$
This yields two conditions:
1.  $z^2 = -1/2 \implies z = \pm \frac{i}{\sqrt{2}}$
2.  $z^2 = -2 \implies z = \pm i\sqrt{2}$

**Step 4: Check which poles lie inside the unit circle $|z|=1$.**
*   $| \pm i/\sqrt{2} | = 1/\sqrt{2} \approx 0.707 < 1$. These two poles are **inside** $C$.
*   $| \pm i\sqrt{2} | = \sqrt{2} \approx 1.414 > 1$. These two poles are **outside** $C$.

The enclosed simple poles are $z_1 = \frac{i}{\sqrt{2}}$ and $z_2 = -\frac{i}{\sqrt{2}}$.

**Step 5: Calculate the residues.**
Using the formula $\text{Res}(z_k) = \frac{P(z_k)}{Q'(z_k)}$ where $P(z) = z^4$ and $Q(z) = 2z^4 + 5z^2 + 2$:
$Q'(z) = 8z^3 + 10z$
$$\text{Res}(z_k) = \frac{z_k^4}{8z_k^3 + 10z_k} = \frac{z_k^3}{8z_k^2 + 10}$$

*   **For $z_1 = \frac{i}{\sqrt{2}}$:**
    We know $z_1^2 = -1/2$.
    The denominator is $8(-1/2) + 10 = -4 + 10 = 6$.
    The numerator is $z_1^3 = z_1 \cdot z_1^2 = (i/\sqrt{2})(-1/2) = -\frac{i}{2\sqrt{2}}$.
    $$R_1 = \frac{-\frac{i}{2\sqrt{2}}}{6} = -\frac{i}{12\sqrt{2}}$$

*   **For $z_2 = -\frac{i}{\sqrt{2}}$:**
    We know $z_2^2 = -1/2$.
    The denominator is $6$.
    The numerator is $z_2^3 = z_2 \cdot z_2^2 = (-i/\sqrt{2})(-1/2) = \frac{i}{2\sqrt{2}}$.
    $$R_2 = \frac{\frac{i}{2\sqrt{2}}}{6} = \frac{i}{12\sqrt{2}}$$

**Step 6: Evaluate the integral.**
$$I_c = \frac{1}{i} [ 2\pi i (R_1 + R_2) ] = 2\pi \left( -\frac{i}{12\sqrt{2}} + \frac{i}{12\sqrt{2}} \right)$$
$$I_c = 2\pi (0) = 0$$

Finally, taking the real part: $I = \text{Re}(I_c) = \text{Re}(0) = 0$.

*(Symmetry shortcut: Note that $f(\theta) = \frac{\cos 3\theta}{5+4\cos 2\theta}$. If we shift the interval by $\pi/2$ (let $\theta = \phi + \pi/2$), the numerator $\cos 3(\phi + \pi/2) = \sin 3\phi$ is an ODD function, while the denominator $5+4\cos(2\phi+\pi) = 5-4\cos 2\phi$ is an EVEN function. Integrating an odd function over a full $2\pi$ symmetric period evaluates to exactly 0).*

**Answer:** The value of the integral is **$0$**.
Here are the detailed solutions for the next four questions (Q333 to Q336).

### Q333. Pg 6, Q4(b)(iii): Evaluate $\int_0^\infty \frac{\cos mx}{(x^2+1)^2} dx$ if $m>0$

*(Note: This is identically stated in Q342).*

**Solution:**

Let $I = \int_0^\infty \frac{\cos mx}{(x^2+1)^2} dx$.

**Step 1: Relate to a complex contour integral.**
The integrand $f(x) = \frac{\cos mx}{(x^2+1)^2}$ is an even function of $x$. Therefore, the integral from $0$ to $\infty$ is half the integral over the entire real line:
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{\cos mx}{(x^2+1)^2} dx$$
Since $\cos mx$ is the real part of $e^{imx}$ (where $m>0$), we can write this as:
$$I = \frac{1}{2} \text{Re} \left( \int_{-\infty}^\infty \frac{e^{imx}}{(x^2+1)^2} dx \right)$$

We evaluate the complex contour integral $\oint_\Gamma F(z) dz$ where $F(z) = \frac{e^{imz}}{(z^2+1)^2}$, over the standard upper half-plane semi-circular contour $\Gamma$.
Because $m > 0$, by Jordan's Lemma, the integral over the large semi-circular arc $C_R$ goes to $0$ as $R \to \infty$. Thus, the contour integral exactly equals the integral over the real line.

**Step 2: Identify the singularities of $F(z)$.**
Set the denominator to zero:
$$(z^2 + 1)^2 = 0 \implies (z-i)^2(z+i)^2 = 0$$
There are two poles of **order 2**:
1.  $z_1 = i$
2.  $z_2 = -i$

Only $z_1 = i$ lies in the upper half-plane (inside our contour $\Gamma$).

**Step 3: Calculate the residue at $z_1 = i$.**
Using the formula for a pole of order $n=2$:
$$\text{Res}(F, i) = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 \frac{e^{imz}}{(z-i)^2(z+i)^2} \right]$$
$$\text{Res}(F, i) = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{imz}}{(z+i)^2} \right]$$
Use the quotient rule:
$$\frac{d}{dz} \left[ \frac{e^{imz}}{(z+i)^2} \right] = \frac{im e^{imz} (z+i)^2 - e^{imz} [2(z+i)]}{(z+i)^4}$$
Factor out $e^{imz}(z+i)$ from the numerator:
$$= \frac{e^{imz}(z+i) [im(z+i) - 2]}{(z+i)^4} = \frac{e^{imz} [im(z+i) - 2]}{(z+i)^3}$$
Evaluate this expression at $z = i$:
$$\text{Res}(F, i) = \frac{e^{im(i)} [im(i+i) - 2]}{(i+i)^3} = \frac{e^{-m} [im(2i) - 2]}{(2i)^3} = \frac{e^{-m} [2i^2m - 2]}{-8i}$$
Since $i^2 = -1$:
$$\text{Res}(F, i) = \frac{e^{-m} [-2m - 2]}{-8i} = \frac{-2e^{-m} (m + 1)}{-8i} = \frac{e^{-m} (m + 1)}{4i}$$
Multiply top and bottom by $i$:
$$\text{Res}(F, i) = -i \frac{e^{-m}(m+1)}{4}$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$\int_{-\infty}^\infty \frac{e^{imx}}{(x^2+1)^2} dx = 2\pi i \cdot \text{Res}(F, i)$$
$$= 2\pi i \left( -i \frac{e^{-m}(m+1)}{4} \right)$$
$$= -2\pi i^2 \frac{e^{-m}(m+1)}{4}$$
Since $i^2 = -1$:
$$= 2\pi \frac{e^{-m}(m+1)}{4} = \frac{\pi(m+1)e^{-m}}{2}$$

**Step 5: Extract the final integral.**
The result is purely real, so the real part is just the result itself. We must divide by 2 for the integral from $0$ to $\infty$:
$$I = \frac{1}{2} \text{Re} \left( \frac{\pi(m+1)e^{-m}}{2} \right) = \frac{\pi(m+1)e^{-m}}{4}$$

**Answer:** The value of the integral is **$\frac{\pi(m+1)e^{-m}}{4}$**.

***

### Q334. Example: Evaluate the Cauchy principal value of $\int_{-\infty}^{\infty}\frac{dx}{(x^{2}+1)(x^{2}+9)}$

**Solution:**

Let $I = \int_{-\infty}^\infty \frac{1}{(x^2+1)(x^2+9)} dx$.

**Step 1: Set up the complex contour integral.**
We define the complex function $f(z) = \frac{1}{(z^2+1)(z^2+9)}$.
We evaluate the contour integral $\oint_\Gamma f(z) dz$ over the standard upper half-plane semi-circular contour $\Gamma$ (radius $R$). 
Because the degree of the denominator (4) is $\ge$ the degree of the numerator (0) + 2, the integral over the semi-circular arc goes to $0$ as $R \to \infty$. 
Thus, $\oint_\Gamma f(z) dz = \int_{-\infty}^\infty f(x) dx$.

**Step 2: Identify the singularities.**
Set the denominator to zero:
$$(z^2+1)(z^2+9) = 0$$
This yields four simple poles:
1.  $z^2 = -1 \implies z = \pm i$
2.  $z^2 = -9 \implies z = \pm 3i$

Only the poles with a positive imaginary part lie inside our upper half-plane contour $\Gamma$:
*   **$z_1 = i$**
*   **$z_2 = 3i$**

**Step 3: Calculate the residues.**
For a function $f(z) = \frac{P(z)}{Q(z)}$ with simple poles, the residue is $\frac{P(a)}{Q'(a)}$.
Here, $P(z) = 1$ and $Q(z) = (z^2+1)(z^2+9) = z^4 + 10z^2 + 9$.
$Q'(z) = 4z^3 + 20z = z(4z^2 + 20)$.

*   **Residue at $z_1 = i$:**
    $$R_1 = \frac{1}{i(4(i)^2 + 20)} = \frac{1}{i(-4 + 20)} = \frac{1}{16i} = -\frac{i}{16}$$
    *(Alternative factorization method: $\lim_{z\to i} \frac{1}{(z+i)(z^2+9)} = \frac{1}{(2i)(-1+9)} = \frac{1}{16i} = -\frac{i}{16}$)*

*   **Residue at $z_2 = 3i$:**
    $$R_2 = \frac{1}{3i(4(3i)^2 + 20)} = \frac{1}{3i(4(-9) + 20)} = \frac{1}{3i(-36 + 20)} = \frac{1}{3i(-16)} = \frac{1}{-48i} = \frac{i}{48}$$
    *(Alternative factorization method: $\lim_{z\to 3i} \frac{1}{(z^2+1)(z+3i)} = \frac{1}{(-9+1)(6i)} = \frac{1}{-48i} = \frac{i}{48}$)*

**Step 4: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i (R_1 + R_2)$$
$$I = 2\pi i \left( -\frac{i}{16} + \frac{i}{48} \right)$$
Find a common denominator (48):
$$I = 2\pi i \left( -\frac{3i}{48} + \frac{i}{48} \right) = 2\pi i \left( -\frac{2i}{48} \right) = 2\pi i \left( -\frac{i}{24} \right)$$
$$I = \frac{-2\pi i^2}{24}$$
Since $i^2 = -1$:
$$I = \frac{2\pi}{24} = \frac{\pi}{12}$$

**Answer:** The value of the integral is **$\frac{\pi}{12}$**.

***

### Q335. Example 3: Evaluate the Cauchy principal value of $\int_{-\infty}^{\infty}\frac{dx}{x^{4}+1}$

**Solution:**

Let $I = \int_{-\infty}^\infty \frac{1}{x^4+1} dx$.

**Step 1: Set up the complex contour integral.**
Consider the complex function $f(z) = \frac{1}{z^4+1}$.
We evaluate it over the standard upper half-plane semi-circular contour $\Gamma$. As $R\to\infty$, the integral over the arc goes to 0 (degree $4 \ge 0+2$).
Thus, $\oint_\Gamma f(z) dz = \int_{-\infty}^\infty f(x) dx$.

**Step 2: Identify the singularities in the upper half-plane.**
Set $z^4 + 1 = 0 \implies z^4 = -1 = e^{i\pi}$.
The four roots are $z_k = e^{i(\pi + 2k\pi)/4}$ for $k=0,1,2,3$.
The poles in the upper half-plane are:
1.  **$z_0 = e^{i\pi/4} = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$**
2.  **$z_1 = e^{i3\pi/4} = -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$**

**Step 3: Calculate the residues.**
Since the poles are simple, $\text{Res}(z_k) = \frac{P(z_k)}{Q'(z_k)}$.
$P(z) = 1$ and $Q'(z) = 4z^3$.
$$\text{Res}(z_k) = \frac{1}{4z_k^3}$$
Multiply top and bottom by $z_k$:
$$\text{Res}(z_k) = \frac{z_k}{4z_k^4}$$
Since $z_k^4 = -1$ at the poles:
$$\text{Res}(z_k) = \frac{z_k}{-4} = -\frac{z_k}{4}$$

Calculate the two residues:
*   $R_0 = -\frac{1}{4} e^{i\pi/4} = -\frac{1}{4} \left( \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}} \right)$
*   $R_1 = -\frac{1}{4} e^{i3\pi/4} = -\frac{1}{4} \left( -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}} \right)$

**Step 4: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i (R_0 + R_1)$$
Sum the residues:
$$R_0 + R_1 = -\frac{1}{4} \left[ \left( \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}} \right) \right]$$
The real parts cancel out:
$$= -\frac{1}{4} \left[ 2i\frac{1}{\sqrt{2}} \right] = -\frac{i}{2\sqrt{2}}$$

Substitute back into the theorem:
$$I = 2\pi i \left( -\frac{i}{2\sqrt{2}} \right)$$
$$I = \frac{-2\pi i^2}{2\sqrt{2}}$$
Since $i^2 = -1$:
$$I = \frac{2\pi}{2\sqrt{2}} = \frac{\pi}{\sqrt{2}}$$

**Answer:** The Cauchy principal value is **$\frac{\pi}{\sqrt{2}}$**.

***

### Q336. Example 4: Evaluate the Cauchy principal value of $\int_{0}^{\infty}\frac{x\sin x~dx}{x^{2}+9}$

**Solution:**

Let $I = \int_0^\infty \frac{x\sin x}{x^2+9} dx$.

**Step 1: Relate to a complex contour integral.**
The integrand $f(x) = \frac{x\sin x}{x^2+9}$ is an **even function**. (Both $x$ and $\sin x$ are odd functions, so their product is even: $(-x)\sin(-x) = (-x)(-\sin x) = x\sin x$. The denominator $x^2+9$ is also even).
Therefore, the integral from $0$ to $\infty$ is half the integral over the entire real line:
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{x\sin x}{x^2+9} dx$$

Since $x\sin x$ is the imaginary part of $x e^{ix}$, we write:
$$I = \frac{1}{2} \text{Im} \left( \int_{-\infty}^\infty \frac{x e^{ix}}{x^2+9} dx \right)$$

We evaluate the complex contour integral $\oint_\Gamma F(z) dz$ where $F(z) = \frac{z e^{iz}}{z^2+9}$ over the standard upper half-plane semi-circular contour $\Gamma$.
By Jordan's Lemma (since $m=1>0$ and $z/(z^2+9) \to 0$ as $R \to \infty$), the integral over the arc goes to zero.

**Step 2: Identify the singularities.**
Set the denominator to zero:
$$z^2 + 9 = 0 \implies z = \pm 3i$$
The only pole in the upper half-plane is the simple pole at **$z_1 = 3i$**.

**Step 3: Calculate the residue at $z_1 = 3i$.**
For a simple pole, $\text{Res}(F, a) = \frac{P(a)}{Q'(a)}$.
Here, $P(z) = z e^{iz}$ and $Q(z) = z^2+9 \implies Q'(z) = 2z$.
$$\text{Res}(3i) = \frac{3i \cdot e^{i(3i)}}{2(3i)}$$
Cancel the $3i$ terms:
$$\text{Res}(3i) = \frac{e^{-3}}{2}$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$\int_{-\infty}^\infty \frac{x e^{ix}}{x^2+9} dx = 2\pi i \cdot \text{Res}(3i)$$
$$= 2\pi i \left( \frac{e^{-3}}{2} \right) = \pi i e^{-3}$$

**Step 5: Extract the final integral.**
From Step 1, $I = \frac{1}{2} \text{Im} ( \pi i e^{-3} )$.
The imaginary part of $\pi i e^{-3}$ is simply $\pi e^{-3}$.
$$I = \frac{1}{2} (\pi e^{-3}) = \frac{\pi}{2e^3}$$

**Answer:** The value of the integral is **$\frac{\pi}{2e^3}$**.





Here are the detailed solutions for the next four questions (Q337 to Q340).

### Q337. Example 5: Evaluate the Cauchy principal value of $\int_{-\infty}^{\infty}\frac{\sin x~dx}{x^{2}+x+1}$

**Solution:**

Let $I = \int_{-\infty}^\infty \frac{\sin x}{x^2+x+1} dx$.

**Step 1: Relate to a complex contour integral.**
We know that $\sin x$ is the imaginary part of $e^{ix}$. 
Therefore, we can write:
$$I = \text{Im} \left( \int_{-\infty}^\infty \frac{e^{ix}}{x^2+x+1} dx \right)$$

We define the complex function $F(z) = \frac{e^{iz}}{z^2+z+1}$ and evaluate its contour integral $\oint_\Gamma F(z) dz$ over the standard upper half-plane semi-circular contour $\Gamma$.
By Jordan's Lemma, because $m=1>0$ and $1/(z^2+z+1) \to 0$ as $R \to \infty$, the integral over the large semi-circular arc evaluates to zero.
Thus, $\oint_\Gamma F(z) dz = \int_{-\infty}^\infty F(x) dx$.

**Step 2: Identify the singularities.**
Find the roots of the denominator using the quadratic formula:
$$z^2 + z + 1 = 0$$
$$z = \frac{-1 \pm \sqrt{1^2 - 4(1)(1)}}{2}$$
$$z = \frac{-1 \pm \sqrt{-3}}{2} = -\frac{1}{2} \pm i\frac{\sqrt{3}}{2}$$

There are two simple poles. Only the one with a positive imaginary part lies inside our upper half-plane contour $\Gamma$:
**$z_1 = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$**

**Step 3: Calculate the residue at $z_1$.**
For a simple pole, $\text{Res}(F, a) = \frac{P(a)}{Q'(a)}$.
Here, $P(z) = e^{iz}$ and $Q(z) = z^2+z+1 \implies Q'(z) = 2z+1$.

Substitute $z = z_1$:
$$\text{Res}(z_1) = \frac{e^{i z_1}}{2z_1 + 1}$$

Let's evaluate the denominator first:
$$2z_1 + 1 = 2\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) + 1 = -1 + i\sqrt{3} + 1 = i\sqrt{3}$$

Now evaluate the exponent in the numerator:
$$i z_1 = i\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = -\frac{i}{2} + i^2\frac{\sqrt{3}}{2} = -\frac{\sqrt{3}}{2} - i\frac{1}{2}$$
So, the numerator is $e^{-\frac{\sqrt{3}}{2} - i\frac{1}{2}} = e^{-\sqrt{3}/2} \cdot e^{-i/2}$.

Put them together to find the residue:
$$\text{Res}(z_1) = \frac{e^{-\sqrt{3}/2} e^{-i/2}}{i\sqrt{3}}$$
Multiply top and bottom by $i$:
$$\text{Res}(z_1) = \frac{i e^{-\sqrt{3}/2} e^{-i/2}}{i^2\sqrt{3}} = -\frac{i e^{-\sqrt{3}/2} e^{-i/2}}{\sqrt{3}}$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$\int_{-\infty}^\infty \frac{e^{ix}}{x^2+x+1} dx = 2\pi i \cdot \text{Res}(z_1)$$
$$= 2\pi i \left( -\frac{i e^{-\sqrt{3}/2} e^{-i/2}}{\sqrt{3}} \right)$$
$$= -2\pi i^2 \frac{e^{-\sqrt{3}/2} e^{-i/2}}{\sqrt{3}}$$
$$= \frac{2\pi}{\sqrt{3}} e^{-\sqrt{3}/2} e^{-i/2}$$

**Step 5: Extract the imaginary part.**
We established in Step 1 that $I$ is the imaginary part of this result.
Expand $e^{-i/2}$ using Euler's formula: $e^{-i/2} = \cos(-1/2) + i\sin(-1/2) = \cos(1/2) - i\sin(1/2)$.

Substitute this back:
$$\int_{-\infty}^\infty \frac{e^{ix}}{x^2+x+1} dx = \frac{2\pi}{\sqrt{3}} e^{-\sqrt{3}/2} \left[ \cos\left(\frac{1}{2}\right) - i\sin\left(\frac{1}{2}\right) \right]$$

The imaginary part is the coefficient of $i$:
$$I = \text{Im}(\dots) = -\frac{2\pi}{\sqrt{3}} e^{-\sqrt{3}/2} \sin\left(\frac{1}{2}\right)$$

**Answer:** The value of the integral is **$-\frac{2\pi}{\sqrt{3}} e^{-\sqrt{3}/2} \sin\left(\frac{1}{2}\right)$**.

***

### Q338. Theorem 1: Consider the evaluation of integrals of the type $I=\int_{-\infty}^{+\infty}F(x)dx$ , where $F(z)$ is a function that satisfies the following conditions: 1. It is analytic in the upper half plane except at a finite number of poles. 2. It has no poles on the real axis. 3. $zF(z)\rightarrow0$ uniformly as $|z|\rightarrow\infty$ for $0\le arg~z\le\pi$. 4. When x is real, $xF(x)\rightarrow0$ as $x\rightarrow\pm\infty$ in such way that $\int_{\infty}^{0}F(x)dx$ and $\int_{-\infty}^{0}F(x)dx$ both converge. Then $I=\int_{-\infty}^{+\infty}F(x)dx=2\pi i\{sum$ of Residue \}.

*(Note: This is not a problem to solve, but rather a formal statement of the theorem used to evaluate real improper integrals via contour integration. It dictates the conditions under which the integral over the large semicircular arc $C_R$ vanishes, allowing the contour integral to perfectly equal the real line integral. Condition 3 is crucial for ensuring $\lim_{R\to\infty} \int_{C_R} F(z)dz = 0$. The conclusion explicitly states the operational method applied in Q327, Q329, Q331, etc).*

**Explanation of the Theorem's Mechanics:**
1.  We define a closed contour $\Gamma$ consisting of the real axis segment $[-R, R]$ and an upper semi-circle $C_R$ of radius $R$.
2.  By Cauchy's Residue Theorem, $\oint_\Gamma F(z)dz = \int_{-R}^R F(x)dx + \int_{C_R} F(z)dz = 2\pi i \sum \text{Res}(F, z_k)$.
3.  Condition 3 mathematically guarantees that as $R \to \infty$, the integral over the semi-circle $C_R$ becomes exactly zero. 
4.  Consequently, taking the limit as $R \to \infty$ isolates the real line integral: $\int_{-\infty}^\infty F(x)dx = 2\pi i \sum \text{Res}(F, z_k)$.

***

### Q339. Example 7.1: Evaluate $\int_{0}^{\infty}\frac{dx}{x^{4}+a^{4}}$

*(Note: This is identically stated and solved in Q327. I will summarize the steps here for flow).*

**Solution:**

Let $I = \int_0^\infty \frac{1}{x^4+a^4} dx$.

1.  **Extend to the real line:** Since the integrand is an even function, $I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{x^4+a^4} dx$.
2.  **Define Complex Function & Contour:** Let $F(z) = \frac{1}{z^4+a^4}$. Evaluate over the standard upper half-plane semi-circle $\Gamma$. Since $z F(z) = \frac{z}{z^4+a^4} \to 0$ as $|z|\to\infty$, the theorem from Q338 applies.
3.  **Identify Poles:** $z^4 = -a^4 \implies z_k = a e^{i(\pi+2k\pi)/4}$.
    The poles in the upper half-plane are $z_0 = a e^{i\pi/4}$ and $z_1 = a e^{i3\pi/4}$.
4.  **Calculate Residues:** $\text{Res}(z_k) = \frac{1}{4z_k^3} = \frac{z_k}{4z_k^4} = -\frac{z_k}{4a^4}$.
    *   $R_0 = -\frac{e^{i\pi/4}}{4a^3}$
    *   $R_1 = -\frac{e^{i3\pi/4}}{4a^3}$
5.  **Apply Residue Theorem:**
    $$\int_{-\infty}^\infty F(x) dx = 2\pi i (R_0 + R_1) = 2\pi i \left( -\frac{1}{4a^3} \right) (e^{i\pi/4} + e^{i3\pi/4})$$
    Since $e^{i\pi/4} + e^{i3\pi/4} = (\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}) + (-\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}) = i\frac{2}{\sqrt{2}} = i\sqrt{2}$:
    $$\int_{-\infty}^\infty F(x) dx = -\frac{2\pi i}{4a^3} (i\sqrt{2}) = \frac{2\pi\sqrt{2}}{4a^3} = \frac{\pi\sqrt{2}}{2a^3}$$
6.  **Final Evaluation:**
    $$I = \frac{1}{2} \left( \frac{\pi\sqrt{2}}{2a^3} \right) = \frac{\pi\sqrt{2}}{4a^3}$$

**Answer:** The value of the integral is **$\frac{\pi\sqrt{2}}{4a^3}$**.

***

### Q340. Example 7.2: Evaluate $\int_{0}^{\infty}\frac{dx}{x^{6}+1}$

*(Note: This is identically stated and solved in Q329 and Q331. I will summarize the steps here).*

**Solution:**

Let $I = \int_0^\infty \frac{1}{x^6+1} dx$.

1.  **Extend to the real line:** The integrand is even, so $I = \frac{1}{2} \int_{-\infty}^\infty \frac{1}{x^6+1} dx$.
2.  **Define Complex Function & Contour:** Let $F(z) = \frac{1}{z^6+1}$. Evaluate over the standard upper half-plane contour.
3.  **Identify Poles:** $z^6 = -1 \implies z_k = e^{i(\pi+2k\pi)/6}$.
    The poles in the upper half-plane are:
    *   $z_0 = e^{i\pi/6} = \frac{\sqrt{3}}{2} + i\frac{1}{2}$
    *   $z_1 = e^{i3\pi/6} = e^{i\pi/2} = i$
    *   $z_2 = e^{i5\pi/6} = -\frac{\sqrt{3}}{2} + i\frac{1}{2}$
4.  **Calculate Residues:** $\text{Res}(z_k) = \frac{1}{6z_k^5} = \frac{z_k}{6z_k^6} = -\frac{z_k}{6}$.
    *   $R_0 = -\frac{1}{6}(\frac{\sqrt{3}}{2} + i\frac{1}{2})$
    *   $R_1 = -\frac{1}{6}(i)$
    *   $R_2 = -\frac{1}{6}(-\frac{\sqrt{3}}{2} + i\frac{1}{2})$
5.  **Apply Residue Theorem:**
    $$\int_{-\infty}^\infty F(x) dx = 2\pi i (R_0 + R_1 + R_2)$$
    Sum the residues: $R_0 + R_1 + R_2 = -\frac{1}{6} (i\frac{1}{2} + i + i\frac{1}{2}) = -\frac{1}{6}(2i) = -\frac{i}{3}$.
    $$\int_{-\infty}^\infty F(x) dx = 2\pi i \left( -\frac{i}{3} \right) = \frac{2\pi}{3}$$
6.  **Final Evaluation:**
    $$I = \frac{1}{2} \left( \frac{2\pi}{3} \right) = \frac{\pi}{3}$$

**Answer:** The value of the integral is **$\frac{\pi}{3}$**.

Here are the detailed solutions for the next four questions (Q341 to Q344).

### Q341. Example 7.3: Evaluate $\int_{0}^{\infty}\frac{cos~mx}{x^{2}+1}dx$

**Solution:**

Let $I = \int_0^\infty \frac{\cos mx}{x^2+1} dx$. We assume $m > 0$.

**Step 1: Relate to a complex contour integral.**
Because the integrand $\frac{\cos mx}{x^2+1}$ is an even function of $x$, the integral from $0$ to $\infty$ is half the integral over the entire real line:
$$I = \frac{1}{2} \int_{-\infty}^\infty \frac{\cos mx}{x^2+1} dx$$

Since $\cos mx$ is the real part of $e^{imx}$, we can write:
$$I = \frac{1}{2} \text{Re} \left( \int_{-\infty}^\infty \frac{e^{imx}}{x^2+1} dx \right)$$

We evaluate the complex contour integral $\oint_\Gamma F(z) dz$ where $F(z) = \frac{e^{imz}}{z^2+1}$, over the standard upper half-plane semi-circular contour $\Gamma$.
By Jordan's Lemma (since $m > 0$), the integral over the semi-circular arc goes to $0$ as the radius $R \to \infty$. Thus, the closed contour integral equals the integral over the real line.

**Step 2: Identify the singularities.**
Set the denominator to zero:
$$z^2 + 1 = 0 \implies z = \pm i$$
There are two simple poles. Only $z_1 = i$ lies in the upper half-plane (inside our contour $\Gamma$).

**Step 3: Calculate the residue at $z_1 = i$.**
Using the formula for a simple pole $\text{Res}(F, a) = \frac{P(a)}{Q'(a)}$:
Here, $P(z) = e^{imz}$ and $Q(z) = z^2+1 \implies Q'(z) = 2z$.
$$\text{Res}(i) = \frac{e^{im(i)}}{2(i)} = \frac{e^{-m}}{2i}$$

**Step 4: Apply Cauchy's Residue Theorem.**
$$\int_{-\infty}^\infty \frac{e^{imx}}{x^2+1} dx = 2\pi i \cdot \text{Res}(i)$$
$$= 2\pi i \left( \frac{e^{-m}}{2i} \right)$$
The $2i$ terms cancel out perfectly:
$$= \pi e^{-m}$$

**Step 5: Extract the final integral.**
The result is purely real. Therefore, taking the real part changes nothing. We just multiply by $1/2$:
$$I = \frac{1}{2} \text{Re}(\pi e^{-m}) = \frac{\pi}{2} e^{-m}$$

*(Note: If $m$ can be negative, the formula generalizes to $\frac{\pi}{2} e^{-|m|}$ because $\cos(mx) = \cos(-mx)$).*

**Answer:** The value of the integral is **$\frac{\pi}{2} e^{-m}$**.

***

### Q342. Example 7.4: Evaluate $\int_{0}^{\infty}\frac{cos~mx}{(x^{2}+1)^{2}}dx$

*(Note: This is identically stated and solved in Q333. A concise summary of the steps is provided below).*

**Solution:**

Let $I = \int_0^\infty \frac{\cos mx}{(x^2+1)^2} dx$. Assume $m > 0$.

1.  **Extend to real line:** Integrand is even, so $I = \frac{1}{2} \text{Re} \left( \int_{-\infty}^\infty \frac{e^{imx}}{(x^2+1)^2} dx \right)$.
2.  **Define Complex Function:** $F(z) = \frac{e^{imz}}{(z^2+1)^2}$. Evaluate over upper half-plane contour $\Gamma$. By Jordan's Lemma, arc integral vanishes.
3.  **Identify Poles:** $(z^2+1)^2 = 0 \implies z = \pm i$. These are poles of order 2. Only $z_1 = i$ is in the upper half-plane.
4.  **Calculate Residue at $z_1=i$:**
    Formula: $\lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{imz}}{(z+i)^2} \right]$.
    Derivative: $\frac{im e^{imz} (z+i)^2 - e^{imz} [2(z+i)]}{(z+i)^4} = \frac{e^{imz} [im(z+i) - 2]}{(z+i)^3}$.
    Substitute $z=i$: $\frac{e^{-m}[im(2i) - 2]}{(2i)^3} = \frac{e^{-m}[-2m - 2]}{-8i} = \frac{-2e^{-m}(m+1)}{-8i} = \frac{e^{-m}(m+1)}{4i} = -i\frac{e^{-m}(m+1)}{4}$.
5.  **Apply Residue Theorem:**
    $\int_{-\infty}^\infty \frac{e^{imx}}{(x^2+1)^2} dx = 2\pi i \left( -i\frac{e^{-m}(m+1)}{4} \right) = 2\pi \frac{e^{-m}(m+1)}{4} = \frac{\pi(m+1)e^{-m}}{2}$.
6.  **Final Evaluation:**
    $I = \frac{1}{2} \text{Re} \left( \frac{\pi(m+1)e^{-m}}{2} \right) = \frac{\pi(m+1)e^{-m}}{4}$.

**Answer:** The value of the integral is **$\frac{\pi(m+1)e^{-m}}{4}$**.

***

### Q343. Example 7.5: Evaluate $\int_{0}^{\infty}\frac{sinx}{x}dx$

*(Note: This is identically stated and solved in Q330. A concise summary of the steps is provided below).*

**Solution:**

Let $I = \int_0^\infty \frac{\sin x}{x} dx$.

1.  **Extend to real line:** Integrand is even, so $I = \frac{1}{2} \int_{-\infty}^\infty \frac{\sin x}{x} dx = \frac{1}{2} \text{Im} \left( \int_{-\infty}^\infty \frac{e^{ix}}{x} dx \right)$.
2.  **Define Complex Function:** $F(z) = \frac{e^{iz}}{z}$.
3.  **Contour choice:** The function has a pole at the origin $z=0$, which lies exactly on our integration path. We must use an indented semi-circular contour $\Gamma$ in the upper half-plane. It consists of the real axis $[-R, -r]$, a small clockwise semi-circle $C_r$ over the origin, the real axis $[r, R]$, and the large counter-clockwise semi-circle $C_R$.
4.  **Evaluate Contours:**
    *   $\oint_\Gamma F(z) dz = 0$ (because the pole is bypassed, no singularities are inside $\Gamma$).
    *   $\lim_{R \to \infty} \int_{C_R} F(z) dz = 0$ (By Jordan's Lemma).
    *   $\lim_{r \to 0} \int_{C_r} F(z) dz = -\pi i \cdot \text{Res}(F, 0)$. (The negative sign is because $C_r$ is traversed clockwise).
5.  **Calculate Residue:**
    $\text{Res}(0) = \lim_{z \to 0} z \frac{e^{iz}}{z} = e^0 = 1$.
    So, the small semi-circle integral evaluates to $-\pi i$.
6.  **Assemble limits:**
    $$\text{P.V.} \int_{-\infty}^\infty \frac{e^{ix}}{x} dx - \pi i + 0 = 0 \implies \int_{-\infty}^\infty \frac{e^{ix}}{x} dx = \pi i$$
7.  **Final Evaluation:**
    Extract the imaginary part for the sine integral:
    $\int_{-\infty}^\infty \frac{\sin x}{x} dx = \text{Im}(\pi i) = \pi$.
    Half of this gives our final answer:
    $I = \frac{1}{2} (\pi) = \frac{\pi}{2}$.

**Answer:** The value of the integral is **$\frac{\pi}{2}$**.

***

### Q344. Problem 7.6: Evaluate $\int_{0}^{2\pi}\frac{d\theta}{3-2~cos~\theta+sin~\theta}.$

**Solution:**

Let $I = \int_0^{2\pi} \frac{1}{3 - 2\cos\theta + \sin\theta} d\theta$.
This is a standard contour integral evaluated by mapping to the unit circle.

**Step 1: Substitute complex variables.**
Let $z = e^{i\theta}$. As $\theta$ goes from $0$ to $2\pi$, $z$ traces the unit circle $C$ ($|z|=1$) counter-clockwise.
*   $dz = ie^{i\theta} d\theta \implies d\theta = \frac{dz}{iz}$
*   $\cos\theta = \frac{z + z^{-1}}{2} = \frac{z^2+1}{2z}$
*   $\sin\theta = \frac{z - z^{-1}}{2i} = \frac{z^2-1}{2iz}$

**Step 2: Transform the integral.**
Substitute these into $I$:
$$I = \oint_C \frac{1}{3 - 2\left(\frac{z^2+1}{2z}\right) + \frac{z^2-1}{2iz}} \frac{dz}{iz}$$
Multiply the denominator terms by $iz$:
$$I = \oint_C \frac{1}{3iz - 2i\left(\frac{z^2+1}{2}\right) + \frac{z^2-1}{2}} dz$$
Multiply numerator and denominator by 2 to clear the remaining fractions:
$$I = \oint_C \frac{2}{6iz - 2i(z^2+1) + (z^2-1)} dz$$
Expand the denominator:
$$I = \oint_C \frac{2}{6iz - 2iz^2 - 2i + z^2 - 1} dz$$
Group terms by powers of $z$:
$$I = \oint_C \frac{2}{z^2(1 - 2i) + 6iz - (1 + 2i)} dz$$

**Step 3: Find the singularities.**
Set the denominator to zero and use the quadratic formula:
$$(1-2i)z^2 + 6iz - (1+2i) = 0$$
$$z = \frac{-6i \pm \sqrt{(6i)^2 - 4(1-2i)(-(1+2i))}}{2(1-2i)}$$
Evaluate the term under the root:
$(1-2i)(-(1+2i)) = -(1 - 4i^2) = -(1 - (-4)) = -(5) = -5$.
Therefore, $-4(1-2i)(-(1+2i)) = -4(-5) = 20$.
Also, $(6i)^2 = -36$.
$$z = \frac{-6i \pm \sqrt{-36 + 20}}{2(1-2i)} = \frac{-6i \pm \sqrt{-16}}{2(1-2i)} = \frac{-6i \pm 4i}{2(1-2i)}$$
Divide by 2:
$$z = \frac{-3i \pm 2i}{1-2i}$$

This yields two roots:
1.  **$z_1 = \frac{-3i + 2i}{1-2i} = \frac{-i}{1-2i}$**
    Rationalize: $z_1 = \frac{-i(1+2i)}{(1-2i)(1+2i)} = \frac{-i - 2i^2}{1^2+2^2} = \frac{2-i}{5} = 0.4 - 0.2i$.
2.  **$z_2 = \frac{-3i - 2i}{1-2i} = \frac{-5i}{1-2i}$**
    Rationalize: $z_2 = \frac{-5i(1+2i)}{5} = -i(1+2i) = -i - 2i^2 = 2 - i$.

**Step 4: Check which pole lies inside the unit circle.**
*   $|z_1| = \sqrt{0.4^2 + (-0.2)^2} = \sqrt{0.16 + 0.04} = \sqrt{0.2}$. Since $\sqrt{0.2} < 1$, $z_1$ is **inside** $C$.
*   $|z_2| = \sqrt{2^2 + (-1)^2} = \sqrt{5}$. Since $\sqrt{5} > 1$, $z_2$ is **outside** $C$.

**Step 5: Calculate the residue at $z_1$.**
Let the integrand be $F(z) = \frac{P(z)}{Q(z)}$ where $P(z) = 2$ and $Q(z) = (1-2i)z^2 + 6iz - (1+2i)$.
$Q'(z) = 2(1-2i)z + 6i$.
$$\text{Res}(z_1) = \frac{P(z_1)}{Q'(z_1)} = \frac{2}{2(1-2i)z_1 + 6i}$$
Substitute the un-rationalized form $z_1 = \frac{-i}{1-2i}$ to make cancellation easy:
$$\text{Res}(z_1) = \frac{2}{2(1-2i)\left(\frac{-i}{1-2i}\right) + 6i} = \frac{2}{-2i + 6i} = \frac{2}{4i} = \frac{1}{2i}$$

**Step 6: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \cdot \text{Res}(z_1)$$
$$I = 2\pi i \left( \frac{1}{2i} \right)$$
$$I = \pi$$

**Answer:** The value of the integral is **$\pi$**.

Here are the detailed solutions for the final two questions (Q345 and Q346).

### Q345. Problem 7.7: Given $a>|b|$, show that $\int_{0}^{2\pi}\frac{d\theta}{a+b~sin~\theta}=\frac{2\pi}{\sqrt{a^{2}-b^{2}}}.$

*(Note: This is identically stated and solved in Q328. A concise step-by-step summary is provided below).*

**Solution:**

Let $I = \int_0^{2\pi} \frac{1}{a+b\sin\theta} d\theta$. We are given $a > |b| > 0$.

**Step 1: Map the integral to the unit circle.**
Let $z = e^{i\theta}$. The path is the unit circle $C$ ($|z|=1$).
*   $d\theta = \frac{dz}{iz}$
*   $\sin\theta = \frac{z - z^{-1}}{2i} = \frac{z^2 - 1}{2iz}$

**Step 2: Transform the integral.**
Substitute into $I$:
$$I = \oint_C \frac{1}{a + b\left(\frac{z^2 - 1}{2iz}\right)} \frac{dz}{iz}$$
Distribute the $iz$ into the denominator:
$$I = \oint_C \frac{1}{iaz + b\left(\frac{z^2 - 1}{2}\right)} dz$$
Multiply numerator and denominator by 2 to clear fractions:
$$I = \oint_C \frac{2}{2iaz + bz^2 - b} dz = \oint_C \frac{2}{bz^2 + 2iaz - b} dz$$

**Step 3: Find the singularities.**
Find roots of the denominator $bz^2 + 2iaz - b = 0$:
$$z = \frac{-2ia \pm \sqrt{(2ia)^2 - 4(b)(-b)}}{2b} = \frac{-2ia \pm \sqrt{-4a^2 + 4b^2}}{2b}$$
Factor out 4 from the root and divide by 2:
$$z = \frac{-ia \pm i\sqrt{a^2 - b^2}}{b}$$
Let the two roots be:
$$z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}i \quad \text{and} \quad z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}i$$

**Step 4: Check which pole is inside $C$.**
Because $a > |b|$, the term $\sqrt{a^2-b^2}$ is a real positive number strictly less than $a$.
Therefore, $-a + \sqrt{a^2-b^2}$ is negative. 
Look at the modulus of the product of the roots: $|z_1 z_2| = |c/a| = |-b/b| = 1$. Since the product of their magnitudes is 1, one must be inside the unit circle ($<1$) and the other outside ($>1$).
Look at the magnitude of $z_2$: $|z_2| = \frac{a + \sqrt{a^2-b^2}}{|b|}$. Since $a > |b|$, this magnitude is clearly greater than 1.
Therefore, $z_2$ is outside, leaving **$z_1$ as the only pole inside the contour.**

**Step 5: Calculate the residue at $z_1$.**
Let $F(z) = \frac{2}{b(z-z_1)(z-z_2)}$. The residue at the simple pole $z_1$ is:
$$\text{Res}(z_1) = \lim_{z \to z_1} (z-z_1) F(z) = \frac{2/b}{z_1 - z_2}$$
Calculate $(z_1 - z_2)$:
$$z_1 - z_2 = \frac{-a + \sqrt{a^2-b^2}}{b}i - \frac{-a - \sqrt{a^2-b^2}}{b}i = \frac{2\sqrt{a^2-b^2}}{b}i$$
Substitute into the residue:
$$\text{Res}(z_1) = \frac{2/b}{\frac{2\sqrt{a^2-b^2}}{b}i} = \frac{1}{i\sqrt{a^2-b^2}}$$

**Step 6: Apply Cauchy's Residue Theorem.**
$$I = 2\pi i \cdot \text{Res}(z_1) = 2\pi i \left( \frac{1}{i\sqrt{a^2-b^2}} \right)$$
The $i$ terms cancel completely:
$$I = \frac{2\pi}{\sqrt{a^2-b^2}}$$
**(Proved)**

***

### Q346. Problem 7.8: Show that $\int_{0}^{2\pi}\frac{\cos~3\theta}{5-4~\cos~\theta}d\theta=\frac{\pi}{12}.$

**Solution:**

Let $I = \int_0^{2\pi} \frac{\cos 3\theta}{5 - 4\cos\theta} d\theta$.

**Step 1: Simplify using complex exponentials.**
Because $\cos 3\theta = \text{Re}(e^{i3\theta})$ and the denominator is purely real, we can rewrite the integral as:
$$I = \text{Re} \left[ \int_0^{2\pi} \frac{e^{i3\theta}}{5 - 4\cos\theta} d\theta \right]$$

**Step 2: Map to the unit circle.**
Let $z = e^{i\theta}$. The path is the unit circle $C$ ($|z|=1$).
*   $d\theta = \frac{dz}{iz}$
*   $\cos\theta = \frac{z + z^{-1}}{2} = \frac{z^2+1}{2z}$

Substitute into the integral to get the complex contour integral $I_c$:
$$I_c = \oint_C \frac{z^3}{5 - 4\left(\frac{z^2+1}{2z}\right)} \frac{dz}{iz}$$
Simplify the denominator:
$$I_c = \oint_C \frac{z^3}{5 - \frac{2(z^2+1)}{z}} \frac{dz}{iz}$$
Multiply numerator and denominator of the main fraction by $z$:
$$I_c = \oint_C \frac{z^4}{5z - 2(z^2+1)} \frac{dz}{iz}$$
$$I_c = \frac{1}{i} \oint_C \frac{z^3}{-2z^2 + 5z - 2} dz$$

Let $F(z) = \frac{z^3}{-2z^2 + 5z - 2}$. To make factoring easier, factor out a $-1$ from the denominator:
$$F(z) = \frac{-z^3}{2z^2 - 5z + 2}$$

**Step 3: Find the singularities.**
Set the denominator to zero:
$$2z^2 - 5z + 2 = 0$$
Factor the quadratic:
$$(2z - 1)(z - 2) = 0$$
There are two simple poles:
1.  $z_1 = 1/2$
2.  $z_2 = 2$

**Step 4: Check which pole lies inside the unit circle.**
*   $|1/2| = 0.5 < 1$. This pole is **inside** $C$.
*   $|2| = 2 > 1$. This pole is **outside** $C$.

Only $z_1 = 1/2$ is enclosed by the contour.

**Step 5: Calculate the residue at $z_1 = 1/2$.**
Use the formula $\text{Res}(F, a) = \frac{P(a)}{Q'(a)}$ where $P(z) = -z^3$ and $Q(z) = 2z^2 - 5z + 2$.
$Q'(z) = 4z - 5$.
$$\text{Res}(1/2) = \frac{-(1/2)^3}{4(1/2) - 5} = \frac{-1/8}{2 - 5} = \frac{-1/8}{-3} = \frac{1}{24}$$

**Step 6: Apply Cauchy's Residue Theorem.**
$$I_c = \frac{1}{i} [ 2\pi i \cdot \text{Res}(1/2) ]$$
The $i$ terms cancel out:
$$I_c = 2\pi \left( \frac{1}{24} \right) = \frac{2\pi}{24} = \frac{\pi}{12}$$

**Step 7: Extract the final real integral.**
The contour integral result is purely real.
$$I = \text{Re}(I_c) = \text{Re}\left(\frac{\pi}{12}\right) = \frac{\pi}{12}$$
**(Proved)**

