Based on the provided lecture notes, here is a comprehensive compilation of the theory, formulas, and corresponding solved examples for Three-Dimensional (3D) Geometry.

---

# 1. Coordinate Systems & Basic 3D Geometry

### Theory & Explanation
In 3D geometry, the position of a point is determined relative to three mutually perpendicular axes (X, Y, Z). 
*   **Cartesian Coordinates:** A point is represented as $(x, y, z)$.
*   **Spherical Polar Coordinates:** A point is represented as $(r, \theta, \phi)$ where $r$ is the distance from the origin, $\theta$ is the angle with the Z-axis, and $\phi$ is the angle in the XY plane.
*   **Cylindrical Polar Coordinates:** A point is represented as $(r, \theta, z)$ using polar coordinates in the XY plane and the standard Z height.

### Key Formulas
*   **Distance between two points $P(x_1, y_1, z_1)$ and $Q(x_2, y_2, z_2)$:**
    $$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
*   **Section Formula (Internal Division ratio $m:n$):**
    $$x = \frac{mx_2 + nx_1}{m+n}, \quad y = \frac{my_2 + ny_1}{m+n}, \quad z = \frac{mz_2 + nz_1}{m+n}$$
    *(For external division, replace '$+$' with '$-$')*
*   **Midpoint:** $( \frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}, \frac{z_1+z_2}{2} )$
*   **Centroid of a Triangle:** $G = (\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}, \frac{z_1+z_2+z_3}{3})$
*   **Centroid of a Tetrahedron:** $G = (\frac{x_1+x_2+x_3+x_4}{4}, \frac{y_1+y_2+y_3+y_4}{4}, \frac{z_1+z_2+z_3+z_4}{4})$

---

# 2. Direction Cosines (d.c.'s) & Direction Ratios (d.r.'s)

### Theory & Explanation
If a directed line makes angles $\alpha, \beta, \gamma$ with the positive directions of the X, Y, and Z axes respectively, then $\cos\alpha, \cos\beta, \cos\gamma$ are called the **Direction Cosines** of the line, denoted by $l, m, n$. 
Any three numbers $a, b, c$ proportional to the direction cosines are called **Direction Ratios**.

### Key Formulas
*   **Relation between d.c.'s:** $l^2 + m^2 + n^2 = 1$ (or $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$)
*   **Converting d.r.'s to d.c.'s:** 
    $$l = \frac{x_2 - x_1}{d}, \quad m = \frac{y_2 - y_1}{d}, \quad n = \frac{z_2 - z_1}{d}$$$$l = \frac{a}{\sqrt{a^2+b^2+c^2}}, \quad m = \frac{b}{\sqrt{a^2+b^2+c^2}}, \quad n = \frac{c}{\sqrt{a^2+b^2+c^2}}$$
    $$\frac{l}{a} = \frac{m}{b} = \frac{n}{c} = k$$
*   **D.r.'s of a line joining two points $P(x_1, y_1, z_1)$ and $Q(x_2, y_2, z_2)$:**
    $a = x_2-x_1$, $b = y_2-y_1$, $c = z_2-z_1$
*   **Angle $\theta$ between two lines:** 
    $$\cos\theta = l_1l_2 + m_1m_2 + n_1n_2 = \frac{a_1a_2 + b_1b_2 + c_1c_2}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$$
*   **Perpendicularity condition:** $l_1l_2 + m_1m_2 + n_1n_2 = 0 \Rightarrow a_1a_2 + b_1b_2 + c_1c_2 = 0$
*   **Parallelism condition:** $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$

---

# 3. Projections

### Theory & Explanation
The projection of a line segment joining two points on another straight line is the length of the segment intercepted between perpendiculars drawn from the ends of the first segment onto the second line.

### Key Formulas
*   **Projection of $PQ$ on a line with d.c.'s $l, m, n$:**
    $$Projection = (x_2-x_1)l + (y_2-y_1)m + (z_2-z_1)n$$

---

# 4. The Plane

### Theory & Explanation
A plane is a surface such that if any two points are taken on it, the straight line joining them lies wholly on the plane. The first-degree equation in $x, y, z$ represents a plane.

### Key Formulas
*   **General Equation:** $ax + by + cz + d = 0$ 
        (where $a, b, c$ are d.r.'s of the normal to the plane).
*  **Point–Normal Form**

$$\vec{n} \cdot (\vec{r} - \vec{r}_0) = 0$$
        -   **$\vec{n}$ (Normal Vector):** A vector perpendicular to the surface of the plane.
        - **$\vec{r}_0$ (Known Point):** The position vector of a fixed point $P_0(x_0, y_0, z_0)$ t
        - **$\vec{r}$ (Arbitrary Point):** The position vector of any point $P(x, y, z)$ that belongs to the plane

*   **Intercept Form:** $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$
* **The Determinant Structure**
  The general formula for a plane passing through a point $(x_0, y_0, z_0)$ and containing (or parallel to) two straight line vectors $\mathbf{u} = \langle a_1, b_1, c_1 \rangle$ and $\mathbf{v} = \langle a_2, b_2, c_2 \rangle$ is : 
$$\begin{vmatrix} x - x_0 & y - y_0 & z - z_0 \\ a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \end{vmatrix} = 0$$
 (a ,b ,c ) d.r.  can be replaced with (l ,m ,n) d.c. if convenient.


* Any plane containing a line formed by the intersection of two planes $P_1 = 0$ and $P_2 = 0$ can be written as:

$$P_1 + k P_2 = 0$$
*   **Normal Form:** $lx + my + nz = p$ (where $p$ is the perpendicular distance from origin).
*   **Plane passing through a point $(x_1,y_1,z_1)$:** $a(x-x_1) + b(y-y_1) + c(z-z_1) = 0$
*   **Distance of a point $(x_1, y_1, z_1)$ from a plane:**
    $$P = \left| \frac{ax_1 + by_1 + cz_1 + d}{\sqrt{a^2+b^2+c^2}} \right|$$

---

# 5. The Straight Line
### Key Formulas
*   **Symmetrical Form:** A straight line in 3D can be  or defined by a point it passes through and its direction ratios (Symmetrical Form).
  * $\frac{x-x_1}{l} = \frac{y-y_1}{m} = \frac{z-z_1}{n} = r$
* $$\frac{x - x_1}{a} = \frac{y - y_1}{b} = \frac{z - z_1}{c}$$

   To solve intersection problems, you must know how to convert this into **Parametric Form** by setting the ratios equal to a scalar (usually $r$ or ==**$t$**==):

    - $x = x_1 + ar$
    
    - $y = y_1 + br$
    
    -  $z = z_1 + cr$
    
    This allows you to treat any point on the line as a single variable function of $r$.
*   **General Form:** defined as the intersection of two non-parallel planes (General Form)
		$a_1x + b_1y + c_1z + d_1 = 0 = a_2x + b_2y + c_2z + d_2$
*   **Angle between a line $(l,m,n)$ and a plane $(a,b,c)$:** $\sin\theta = \frac{al+bm+cn}{\sqrt{a^2+b^2+c^2}\sqrt{l^2+m^2+n^2}}$
*   **Condition for Coplanarity of two lines $\frac{x-x_1}{l_1} = ...$ and $\frac{x-x_2}{l_2} = ...$:**
    $$ \begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0 $$

---

# 6. Skew Lines & Shortest Distance (S.D.)

### Theory & Explanation
**Skew lines** are two lines in space that are neither parallel nor intersecting; they **lie in different planes**. The Shortest Distance (**S.D.**) between them is the length of the line segment that is **perpendicular to both** skew lines.

### Key Formulas
For two **Skew lines** $\frac{x-x_1}{l_1} = \frac{y-y_1}{m_1} = \frac{z-z_1}{n_1}$ and $\frac{x-x_2}{l_2} = \frac{y-y_2}{m_2} = \frac{z-z_2}{n_2}$:
$$ S.D. = \frac{\left| \begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} \right|}{\sqrt{(m_1n_2-m_2n_1)^2 + (n_1l_2-n_2l_1)^2 + (l_1m_2-l_2m_1)^2} = \sin \theta} $$
- The length of the shortest distance is the **projection** of the vector connecting $P$ and $Q$   onto the S.D. line .
- The projection formula is:

$$\text{Length} = |(x_2-x_1)l + (y_2-y_1)m + (z_2-z_1)n|$$

---

# 7. Image of a Point with Respect to a Plane

### Theory & Explanation
To find the image (reflection) of a point $P(x_1, y_1, z_1)$ across a plane $ax+by+cz+d=0$:
1. Write the equation of the line passing through $P$ and perpendicular to the plane (d.r.'s will be $a,b,c$).
2. Find the generic point on this line.
3. Substitute the generic point into the plane equation to find the exact point of intersection $Q$ (the foot of the perpendicular/midpoint).
4. Use the midpoint formula to find the image coordinates $R$, where $Q$ is the midpoint of $PR$.

---

# 8. Advanced Plane Theories

### Theory & Explanation
*   **Angle between Two Planes:** The angle between two planes is equal to the angle between their normals. 
*   **Distance between Two Parallel Planes:** If two planes are parallel, their normal vectors are proportional (or can be made identical), differing only by their constant terms.
*   **Family of Planes:** If you have two intersecting planes $P_1 = 0$ and $P_2 = 0$, any plane passing through their line of intersection can be represented by $P_1 + kP_2 = 0$, where $k$ is a constant.
*   **Plane passing through 3 non-collinear points:** If a plane passes through $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, and $(x_3, y_3, z_3)$, its equation is given by setting a specific determinant to zero.

### Key Formulas
*   **Angle between $a_1x+b_1y+c_1z+d_1=0$ and $a_2x+b_2y+c_2z+d_2=0$:**
    $$ \cos\theta = \frac{a_1a_2 + b_1b_2 + c_1c_2}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}} $$
*   **Distance between parallel planes $ax+by+cz+d_1=0$ and $ax+by+cz+d_2=0$:**
    $$ Distance = \frac{|d_1 - d_2|}{\sqrt{a^2+b^2+c^2}} $$
*   **Equation of a plane through 3 points:**
    $$ \begin{vmatrix} x-x_1 & y-y_1 & z-z_1 \\ x_2-x_1 & y_2-y_1 & z_2-z_1 \\ x_3-x_1 & y_3-y_1 & z_3-z_1 \end{vmatrix} = 0 $$

---

# 9. Line and Plane Interactions

### Theory & Explanation
*   **Condition for a Line to Lie in a Plane:** For a line $\frac{x-x_1}{l} = \frac{y-y_1}{m} = \frac{z-z_1}{n}$ to lie completely within the plane $ax+by+cz+d=0$, two conditions must be met:
    1. The point $(x_1, y_1, z_1)$ must lie on the plane: $ax_1 + by_1 + cz_1 + d = 0$.
    2. The line must be perpendicular to the plane's normal: $al + bm + cn = 0$.
*   **Distance of a point from a plane measured parallel to a line:** Instead of finding the perpendicular distance, we draw a line from the point parallel to a given direction until it hits the plane, and calculate the distance of that specific segment.

---

# 10. Vector Form of Direction Cosines

### Theory & Explanation
The notes also introduce a vector-based approach to 3D geometry which is highly useful for simplifications.
*   If a vector is given as $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$, its magnitude is $|\vec{r}| = \sqrt{x^2+y^2+z^2}$.
*   The components $x, y, z$ act as the **Direction Ratios**.
*   The unit vector $\hat{r} = \frac{\vec{r}}{|\vec{r}|}$ directly gives the **Direction Cosines**:
    $$\hat{r} = \cos\alpha\hat{i} + \cos\beta\hat{j} + \cos\gamma\hat{k} = l\hat{i} + m\hat{j} + n\hat{k}$$

---

# 11. Image of a Straight Line with respect to a Plane

### Theory & Explanation
To find the equation of an image line reflected across a plane:
1. Find the point of intersection between the given line and the given plane. Let's call it $S$. (This point is its own image).
2. Take any other arbitrary point on the given line. Find its image point across the plane (using the method described in Topic 7 of the previous response). Let's call the image point $Q'$.
3. Find the equation of the line passing through $S$ and $Q'$. This is the required image line.
