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

### Q21. Pg 19, CT-I, 3.(b): Suppose $z = re^{i\theta}$. Prove that $z^i = e^{-(\theta+2k\pi)}\{\cos(\ln r) + i\sin(\ln r)\}$ where $k = 0, \pm 1, \pm 2, \dots$

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





