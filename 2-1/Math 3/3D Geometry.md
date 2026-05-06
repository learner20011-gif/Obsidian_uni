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

### Example Problem
**Q:** A variable plane is at a constant distance $p$ from the origin and meets the axes at $A, B, C$. Show that the locus of the centroid of the tetrahedron $OABC$ is $x^{-2} + y^{-2} + z^{-2} = 16p^{-2}$.
**Solution:**
1. Let the equation of the plane be $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$.
2. The perpendicular distance from the origin $(0,0,0)$ to this plane is $p$:
   $$\frac{1}{p^2} = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2} \quad \text{--- (i)}$$
3. The plane meets the axes at $A(a,0,0), B(0,b,0), C(0,0,c)$. The origin is $O(0,0,0)$.
4. Let $(x, y, z)$ be the centroid of the tetrahedron $OABC$:
   $$x = \frac{a+0+0+0}{4} \Rightarrow a = 4x$$
   $$y = \frac{0+b+0+0}{4} \Rightarrow b = 4y$$
   $$z = \frac{0+0+c+0}{4} \Rightarrow c = 4z$$
5. Substituting $a, b, c$ into equation (i):
   $$\frac{1}{p^2} = \frac{1}{(4x)^2} + \frac{1}{(4y)^2} + \frac{1}{(4z)^2}$$
   $$\frac{1}{p^2} = \frac{1}{16x^2} + \frac{1}{16y^2} + \frac{1}{16z^2}$$
   $$16p^{-2} = x^{-2} + y^{-2} + z^{-2}$$ *(Proved)*

---

# 2. Direction Cosines (d.c.'s) & Direction Ratios (d.r.'s)

### Theory & Explanation
If a directed line makes angles $\alpha, \beta, \gamma$ with the positive directions of the X, Y, and Z axes respectively, then $\cos\alpha, \cos\beta, \cos\gamma$ are called the **Direction Cosines** of the line, denoted by $l, m, n$. 
Any three numbers $a, b, c$ proportional to the direction cosines are called **Direction Ratios**.

### Key Formulas
*   **Relation between d.c.'s:** $l^2 + m^2 + n^2 = 1$ (or $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$)
*   **Converting d.r.'s to d.c.'s:** 
    $$l = \frac{a}{\sqrt{a^2+b^2+c^2}}, \quad m = \frac{b}{\sqrt{a^2+b^2+c^2}}, \quad n = \frac{c}{\sqrt{a^2+b^2+c^2}}$$
*   **D.r.'s of a line joining two points $P(x_1, y_1, z_1)$ and $Q(x_2, y_2, z_2)$:**
    $a = x_2-x_1$, $b = y_2-y_1$, $c = z_2-z_1$
*   **Angle $\theta$ between two lines:** 
    $$\cos\theta = l_1l_2 + m_1m_2 + n_1n_2 = \frac{a_1a_2 + b_1b_2 + c_1c_2}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$$
*   **Perpendicularity condition:** $l_1l_2 + m_1m_2 + n_1n_2 = 0 \Rightarrow a_1a_2 + b_1b_2 + c_1c_2 = 0$
*   **Parallelism condition:** $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$

### Example Problem
**Q:** A line makes angles $\alpha, \beta, \gamma, \delta$ with the four diagonals of a cube. Prove that $\cos^2\alpha + \cos^2\beta + \cos^2\gamma + \cos^2\delta = \frac{4}{3}$.
**Solution:**
1. Let $a$ be the length of each side of the cube. The 8 vertices are $(0,0,0)$, $(a,0,0)$, $(0,a,0)$, $(0,0,a)$, $(a,a,0)$, $(a,0,a)$, $(0,a,a)$, and $(a,a,a)$.
2. The four diagonals are $OP, AM, BM, CL$ (based on the figure provided in the notes).
   *   d.c.'s of $OP$ (from $(0,0,0)$ to $(a,a,a)$): $(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})$
   *   d.c.'s of $AM$: $(-\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})$
   *   d.c.'s of $BM$: $(\frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}})$
   *   d.c.'s of $CL$: $(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}})$
3. Let the given line have d.c.'s $(l, m, n)$. Since it makes angles $\alpha, \beta, \gamma, \delta$ with the diagonals:
   $$\cos\alpha = l(\frac{1}{\sqrt{3}}) + m(\frac{1}{\sqrt{3}}) + n(\frac{1}{\sqrt{3}}) = \frac{l+m+n}{\sqrt{3}}$$
   $$\cos\beta = \frac{-l+m+n}{\sqrt{3}}, \quad \cos\gamma = \frac{l-m+n}{\sqrt{3}}, \quad \cos\delta = \frac{l+m-n}{\sqrt{3}}$$
4. Squaring and adding them:
   $\cos^2\alpha + \cos^2\beta + \cos^2\gamma + \cos^2\delta = \frac{(l+m+n)^2 + (-l+m+n)^2 + (l-m+n)^2 + (l+m-n)^2}{3}$
   Expanding the squares, cross terms cancel out, leaving:
   $= \frac{4(l^2 + m^2 + n^2)}{3}$
5. Since $l^2+m^2+n^2=1$, the sum is $\frac{4}{3}$. *(Proved)*

---

# 3. Projections

### Theory & Explanation
The projection of a line segment joining two points on another straight line is the length of the segment intercepted between perpendiculars drawn from the ends of the first segment onto the second line.

### Key Formulas
*   **Projection of $PQ$ on a line with d.c.'s $l, m, n$:**
    $$Projection = (x_2-x_1)l + (y_2-y_1)m + (z_2-z_1)n$$

### Example Problem
**Q:** Find the projection of the line joining points $(-1, 4, 3)$ and $(2, 0, 1)$ on the line through points $(-7, 5, 3)$ and $(2, 6, 8)$.
**Solution:**
1. Find the d.r.'s of the target line (through $(-7,5,3)$ and $(2,6,8)$):
   $a = 2 - (-7) = 9$
   $b = 6 - 5 = 1$
   $c = 8 - 3 = 5$
2. Convert to d.c.'s $(l, m, n)$:
   $\sqrt{9^2 + 1^2 + 5^2} = \sqrt{81 + 1 + 25} = \sqrt{107}$
   $l = \frac{9}{\sqrt{107}}, m = \frac{1}{\sqrt{107}}, n = \frac{5}{\sqrt{107}}$
3. Apply projection formula for points $(-1, 4, 3) \rightarrow (x_1,y_1,z_1)$ and $(2, 0, 1) \rightarrow (x_2,y_2,z_2)$:
   $$Projection = (2 - (-1))\left(\frac{9}{\sqrt{107}}\right) + (0 - 4)\left(\frac{1}{\sqrt{107}}\right) + (1 - 3)\left(\frac{5}{\sqrt{107}}\right)$$
   $$= (3)\left(\frac{9}{\sqrt{107}}\right) + (-4)\left(\frac{1}{\sqrt{107}}\right) + (-2)\left(\frac{5}{\sqrt{107}}\right)$$
   $$= \frac{27 - 4 - 10}{\sqrt{107}} = \frac{13}{\sqrt{107}}$$

---

# 4. The Plane

### Theory & Explanation
A plane is a surface such that if any two points are taken on it, the straight line joining them lies wholly on the plane. The first-degree equation in $x, y, z$ represents a plane.

### Key Formulas
*   **General Equation:** $ax + by + cz + d = 0$ (where $a, b, c$ are d.r.'s of the normal to the plane).
*   **Intercept Form:** $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$
*   **Normal Form:** $lx + my + nz = p$ (where $p$ is the perpendicular distance from origin).
*   **Plane passing through a point $(x_1,y_1,z_1)$:** $a(x-x_1) + b(y-y_1) + c(z-z_1) = 0$
*   **Distance of a point $(x_1, y_1, z_1)$ from a plane:**
    $$P = \left| \frac{ax_1 + by_1 + cz_1 + d}{\sqrt{a^2+b^2+c^2}} \right|$$

### Example Problem
**Q:** Find the equation of the plane passing through the points $(2,2,1)$ and $(9,3,6)$ and perpendicular to the plane $2x + 6y + 6z = 9$.
**Solution:**
1. Equation of plane through $(2,2,1)$ is: 
   $a(x-2) + b(y-2) + c(z-1) = 0 \quad \text{--- (i)}$
2. Since it passes through $(9,3,6)$, substitute these values:
   $a(9-2) + b(3-2) + c(6-1) = 0 \Rightarrow 7a + b + 5c = 0 \quad \text{--- (ii)}$
3. The plane (i) is perpendicular to $2x + 6y + 6z = 9$. Therefore, their normals are perpendicular ($a_1a_2 + b_1b_2 + c_1c_2 = 0$):
   $2a + 6b + 6c = 0 \quad \text{--- (iii)}$
4. Solve (ii) and (iii) using cross-multiplication:
   $$\frac{a}{6 - 30} = \frac{b}{10 - 42} = \frac{c}{42 - 2}$$
   $$\frac{a}{-24} = \frac{b}{-32} = \frac{c}{40}$$
   Dividing by $-8$, we get d.r.'s proportional to: $a=3, b=4, c=-5$.
5. Substitute $a, b, c$ back into (i):
   $3(x-2) + 4(y-2) - 5(z-1) = 0$
   $$3x - 6 + 4y - 8 - 5z + 5 = 0 \Rightarrow 3x + 4y - 5z = 9$$

---

# 5. The Straight Line

### Theory & Explanation
A straight line in 3D can be defined as the intersection of two non-parallel planes (General Form) or defined by a point it passes through and its direction ratios (Symmetrical Form).

### Key Formulas
*   **Symmetrical Form:** $\frac{x-x_1}{l} = \frac{y-y_1}{m} = \frac{z-z_1}{n} = r$
*   **General Form:** $a_1x + b_1y + c_1z + d_1 = 0 = a_2x + b_2y + c_2z + d_2$
*   **Angle between a line $(l,m,n)$ and a plane $(a,b,c)$:** $\sin\theta = \frac{al+bm+cn}{\sqrt{a^2+b^2+c^2}\sqrt{l^2+m^2+n^2}}$
*   **Condition for Coplanarity of two lines $\frac{x-x_1}{l_1} = ...$ and $\frac{x-x_2}{l_2} = ...$:**
    $$ \begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0 $$

### Example Problem (Coplanar Lines & Intersection)
**Q:** Show that the lines $\frac{x+1}{2} = \frac{y-2}{2} = \frac{z}{1}$ and $\frac{x-1}{6} = \frac{y+1}{1} = \frac{z-3}{5}$ are coplanar. Find their point of intersection.
**Solution:**
1. **Check Coplanarity:** using points $(-1, 2, 0)$ and $(1, -1, 3)$. 
   Differences: $x_2-x_1 = 2, y_2-y_1 = -3, z_2-z_1 = 3$.
   Determinant:
   $$ \begin{vmatrix} 2 & -3 & 3 \\ 2 & 2 & 1 \\ 6 & 1 & 5 \end{vmatrix} = 2(10-1) - (-3)(10-6) + 3(2-12) = 18 + 12 - 30 = 0$$
   Hence, the lines are coplanar.
2. **Find intersection point:**
   Let $\frac{x+1}{2} = \frac{y-2}{2} = \frac{z}{1} = r_1 \Rightarrow x = 2r_1-1, y = 2r_1+2, z = r_1$
   Let $\frac{x-1}{6} = \frac{y+1}{1} = \frac{z-3}{5} = r_2 \Rightarrow x = 6r_2+1, y = r_2-1, z = 5r_2+3$
3. Equating coordinates for intersection:
   $2r_1 - 1 = 6r_2 + 1 \Rightarrow 2r_1 - 6r_2 = 2 \Rightarrow r_1 - 3r_2 = 1 \quad \text{--- (i)}$
   $2r_1 + 2 = r_2 - 1 \Rightarrow 2r_1 - r_2 = -3 \quad \text{--- (ii)}$
   $r_1 = 5r_2 + 3 \quad \text{--- (iii)}$
4. Solving (i) and (ii): $r_1 = -2, r_2 = -1$. (This also satisfies (iii): $-2 = 5(-1)+3$).
5. Put $r_1 = -2$ into point coordinates:
   $x = 2(-2)-1 = -5, y = 2(-2)+2 = -2, z = -2$.
   Intersection point is **$(-5, -2, -2)$**.

---

# 6. Skew Lines & Shortest Distance (S.D.)

### Theory & Explanation
**Skew lines** are two lines in space that are neither parallel nor intersecting; they lie in different planes. The Shortest Distance (S.D.) between them is the length of the line segment that is perpendicular to both skew lines.

### Key Formulas
For two lines $\frac{x-x_1}{l_1} = \frac{y-y_1}{m_1} = \frac{z-z_1}{n_1}$ and $\frac{x-x_2}{l_2} = \frac{y-y_2}{m_2} = \frac{z-z_2}{n_2}$:
$$ S.D. = \frac{\left| \begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} \right|}{\sqrt{(m_1n_2-m_2n_1)^2 + (n_1l_2-n_2l_1)^2 + (l_1m_2-l_2m_1)^2}} $$

### Example Problem
**Q:** Find the length and equation of the shortest distance between the lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4}$ and $\frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$.
**Solution:**
1. Let the direction ratios of the line of S.D. be $l, m, n$. Since it is perpendicular to both lines:
   $2l + 3m + 4n = 0$
   $3l + 4m + 5n = 0$
2. Solving by cross-multiplication:
   $\frac{l}{15-16} = \frac{m}{12-10} = \frac{n}{8-9} \Rightarrow \frac{l}{-1} = \frac{m}{2} = \frac{n}{-1} \Rightarrow \frac{l}{1} = \frac{m}{-2} = \frac{n}{1}$
   D.r.'s of S.D. line are $(1, -2, 1)$.
   Magnitude: $\sqrt{1^2 + (-2)^2 + 1^2} = \sqrt{6}$. So d.c.'s are $\frac{1}{\sqrt{6}}, \frac{-2}{\sqrt{6}}, \frac{1}{\sqrt{6}}$.
3. Points on the lines are $P(1,2,3)$ and $Q(2,4,5)$.
   Length of S.D. = Projection of $PQ$ on the line of S.D.:
   $$S.D. = (2-1)\left(\frac{1}{\sqrt{6}}\right) + (4-2)\left(\frac{-2}{\sqrt{6}}\right) + (5-3)\left(\frac{1}{\sqrt{6}}\right) = \frac{1 - 4 + 2}{\sqrt{6}} = \left| \frac{-1}{\sqrt{6}} \right| = \frac{1}{\sqrt{6}} \text{ units.}$$
4. **Equation of the line of S.D.** is the intersection of two planes containing each line and the S.D. line:
   Plane 1 containing Line 1 & S.D.:
   $$ \begin{vmatrix} x-1 & y-2 & z-3 \\ 2 & 3 & 4 \\ 1 & -2 & 1 \end{vmatrix} = 0 \Rightarrow 11x + 2y - 7z + 6 = 0 $$
   Plane 2 containing Line 2 & S.D.:
   $$ \begin{vmatrix} x-2 & y-4 & z-5 \\ 3 & 4 & 5 \\ 1 & -2 & 1 \end{vmatrix} = 0 \Rightarrow 14x + 2y - 10z + 14 = 0 \Rightarrow 7x + y - 5z + 7 = 0 $$
   The equation of the S.D. is given by the system: **$11x + 2y - 7z + 6 = 0 = 7x + y - 5z + 7$**.

---

# 7. Image of a Point with Respect to a Plane

### Theory & Explanation
To find the image (reflection) of a point $P(x_1, y_1, z_1)$ across a plane $ax+by+cz+d=0$:
1. Write the equation of the line passing through $P$ and perpendicular to the plane (d.r.'s will be $a,b,c$).
2. Find the generic point on this line.
3. Substitute the generic point into the plane equation to find the exact point of intersection $Q$ (the foot of the perpendicular/midpoint).
4. Use the midpoint formula to find the image coordinates $R$, where $Q$ is the midpoint of $PR$.

### Example Problem
**Q:** Find the image of the point $P(1, 2, -1)$ with respect to the plane $2x + y - 5z = 16$.
**Solution:**
1. The direction ratios of the normal to the plane are $2, 1, -5$.
2. Equation of the line $PR$ passing through $P$ and perpendicular to the plane is:
   $\frac{x-1}{2} = \frac{y-2}{1} = \frac{z+1}{-5} = K$
3. A general point on this line is $(2K+1, K+2, -5K-1)$. Let this be $Q$ (the intersection with the plane).
4. Substitute $Q$ into the plane equation:
   $2(2K+1) + (K+2) - 5(-5K-1) = 16$
   $4K + 2 + K + 2 + 25K + 5 = 16$
   $30K + 9 = 16 \Rightarrow 30K = 7 \Rightarrow K = \frac{7}{30}$
5. Coordinates of midpoint $Q$:
   $x = 2(\frac{7}{30})+1 = \frac{22}{15}$, $y = \frac{7}{30}+2 = \frac{67}{30}$, $z = -5(\frac{7}{30})-1 = -\frac{13}{6}$
   So, $Q = (\frac{22}{15}, \frac{67}{30}, -\frac{13}{6})$.
6. Let the image point be $R(x_1, y_1, z_1)$. Since $Q$ is the midpoint of $PR$:
   $\frac{x_1 + 1}{2} = \frac{22}{15} \Rightarrow x_1 = \frac{44}{15} - 1 = \frac{29}{15}$
   $\frac{y_1 + 2}{2} = \frac{67}{30} \Rightarrow y_1 = \frac{67}{15} - 2 = \frac{37}{15}$
   $\frac{z_1 - 1}{2} = -\frac{13}{6} \Rightarrow z_1 = -\frac{13}{3} + 1 = -\frac{10}{3}$
   Therefore, the image point is **$(\frac{29}{15}, \frac{37}{15}, -\frac{10}{3})$**.

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

### Example Problem (Family of Planes)
**Q:** Find the equation of a plane passing through the point $(1, -1, 1)$ and the intersection of the planes $x - 2y + 3z + 4 = 0$ and $2x - 3y + 4z - 7 = 0$.
**Solution:**
1. The equation of any plane passing through the intersection is:
   $(x - 2y + 3z + 4) + k(2x - 3y + 4z - 7) = 0 \quad \text{--- (i)}$
2. Since the plane passes through the point $(1, -1, 1)$, substitute $x=1, y=-1, z=1$ into the equation:
   $(1 - 2(-1) + 3(1) + 4) + k(2(1) - 3(-1) + 4(1) - 7) = 0$
   $(1 + 2 + 3 + 4) + k(2 + 3 + 4 - 7) = 0$
   $10 + k(2) = 0 \implies 2k = -10 \implies k = -5$
3. Substitute $k = -5$ back into equation (i):
   $(x - 2y + 3z + 4) - 5(2x - 3y + 4z - 7) = 0$
   $x - 2y + 3z + 4 - 10x + 15y - 20z + 35 = 0$
   $$-9x + 13y - 17z + 39 = 0$$ *(Required Equation)*

---

# 9. Line and Plane Interactions

### Theory & Explanation
*   **Condition for a Line to Lie in a Plane:** For a line $\frac{x-x_1}{l} = \frac{y-y_1}{m} = \frac{z-z_1}{n}$ to lie completely within the plane $ax+by+cz+d=0$, two conditions must be met:
    1. The point $(x_1, y_1, z_1)$ must lie on the plane: $ax_1 + by_1 + cz_1 + d = 0$.
    2. The line must be perpendicular to the plane's normal: $al + bm + cn = 0$.
*   **Distance of a point from a plane measured parallel to a line:** Instead of finding the perpendicular distance, we draw a line from the point parallel to a given direction until it hits the plane, and calculate the distance of that specific segment.

### Example Problem (Distance Measured Parallel to a Line)
**Q:** Find the distance of the point $(1, 2, 3)$ from the plane $2x + 4y + 3z = 20$ measured parallel to the line $\frac{x}{2} = \frac{y}{-2} = \frac{z}{1}$.
**Solution:**
1. The direction ratios of the line are $2, -2, 1$.
2. The equation of the line passing through $(1,2,3)$ and parallel to the given line is:
   $\frac{x-1}{2} = \frac{y-2}{-2} = \frac{z-3}{1} = K$
3. A generic point on this new line is $(2K+1, -2K+2, K+3)$.
4. Let this point be the intersection with the given plane. Substitute it into $2x + 4y + 3z = 20$:
   $2(2K+1) + 4(-2K+2) + 3(K+3) = 20$
   $4K + 2 - 8K + 8 + 3K + 9 = 20$
   $-K + 19 = 20 \implies -K = 1 \implies K = -1$
5. Substitute $K = -1$ to find the intersection coordinate:
   $x = 2(-1)+1 = -1$
   $y = -2(-1)+2 = 4$
   $z = (-1)+3 = 2$
   The intersection point is $(-1, 4, 2)$.
6. The required distance is the distance between $(1,2,3)$ and $(-1,4,2)$:
   $$D = \sqrt{(-1 - 1)^2 + (4 - 2)^2 + (2 - 3)^2}$$
   $$D = \sqrt{(-2)^2 + 2^2 + (-1)^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3 \text{ units.}$$

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

### Key Example Setup (from the notes)
*   Line: $\frac{x-2}{1} = \frac{y+5}{-1} = \frac{z-3}{-2}$
*   Plane: $5x - y + z = 30$
*   *Step 1:* Point of intersection $S(5, -8, -3)$.
*   *Step 2:* Pick point $P(2, -5, 3)$ from the line. Find image $Q(38/9, -49/9, 31/9)$.
*   *Step 3:* Equation of line joining $S$ and $Q$ will yield the final symmetrical form.