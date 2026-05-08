### Find the d.c's of OP, OQ & PQ where O(0,0,0) , P(1,-5,7) & Q(-3,6,-2)

Let $l_1, m_1, n_1$ be d.c.'s of $OP$:
$\frac{l_1}{1-0} = \frac{m_1}{-5-0} = \frac{n_1}{7-0} = \frac{1}{\sqrt{1^2+(-5)^2+7^2}} = \frac{1}{\sqrt{75}}$
$l_1 = \frac{1}{\sqrt{75}}, m_1 = \frac{-5}{\sqrt{75}}, n_1 = \frac{7}{\sqrt{75}}$

For $OQ$:
$OQ = \left[-\frac{3}{7}, \frac{6}{7}, -\frac{2}{7}\right]$

Let $l, m, n$ be d.c.'s of $PQ$:
$\frac{l}{-3-1} = \frac{m}{6+5} = \frac{n}{-2-7} = \frac{\sqrt{l^2+m^2+n^2}}{\sqrt{(-4)^2+(11)^2+(-9)^2}}$
$\frac{l}{-4} = \frac{m}{11} = \frac{n}{-9} = \frac{1}{\sqrt{218}}$
$PQ = \left[\frac{-4}{\sqrt{218}}, \frac{11}{\sqrt{218}}, \frac{-9}{\sqrt{218}}\right]$

### Find the projection of the join of points (-1,-1,3) & (2,0,1) on the line through the points (-7,5,3) & (2,6,8)

Let $l, m, n$ be d.c.'s of the line through $(-7,5,3)$ & $(2,6,8)$:
$\frac{l}{2-(-7)} = \frac{m}{6-5} = \frac{n}{8-3} = \frac{\sqrt{l^2+m^2+n^2}}{\sqrt{9^2+1^2+5^2}}$
$\frac{l}{9} = \frac{m}{1} = \frac{n}{5} = \frac{1}{\sqrt{107}}$
$l = \frac{9}{\sqrt{107}}, m = \frac{1}{\sqrt{107}}, n = \frac{5}{\sqrt{107}}$

$\text{Projection} = (x_2-x_1)l + (y_2-y_1)m + (z_2-z_1)n$
$= (2+1)l + (0+1)m + (1-3)n$
$= 3\left(\frac{9}{\sqrt{107}}\right) + 1\left(\frac{1}{\sqrt{107}}\right) - 2\left(\frac{5}{\sqrt{107}}\right)$
$= \frac{27}{\sqrt{107}} + \frac{1}{\sqrt{107}} - \frac{10}{\sqrt{107}}$
$= \frac{18}{\sqrt{107}}$

### Show that the straight lines whose direction cosines are given by 2l+2m-n=0 ; mn+nl+lm=0 are at right angle

$2l + 2m - n = 0 \Rightarrow n = 2l + 2m$  --- (1)
$mn + nl + lm = 0$ --- (2)

From (1) in (2):
$m(2l+2m) + (2l+2m)l + lm = 0$
$2lm + 2m^2 + 2l^2 + 2lm + lm = 0$
$2l^2 + 5lm + 2m^2 = 0$
$(2l+m)(l+2m) = 0$

Case 1: $2l+m=0 \Rightarrow m=-2l$
From (1): $n = 2l + 2(-2l) = -2l \Rightarrow n=m$
$\frac{l}{-1} = \frac{m}{2} = \frac{n}{2}$
1st line d.c.'s proportional to $[-1, 2, 2]$.

Case 2: $l+2m=0 \Rightarrow l=-2m$
From (1): $n = 2(-2m) + 2m = -2m \Rightarrow n=l$
$\frac{l}{2} = \frac{m}{-1} = \frac{n}{2}$
2nd line d.c.'s proportional to $[2, -1, 2]$.

Angle $\theta$ between lines:
$\cos\theta = \frac{(-1)(2) + (2)(-1) + (2)(2)}{\sqrt{(-1)^2+2^2+2^2}\sqrt{2^2+(-1)^2+2^2}} = \frac{-2-2+4}{3 \times 3} = 0$
$\theta = 90^\circ$

### A line makes angles $\alpha, \beta, \gamma, \delta$ with four diagonals of a cube. Prove that $\cos^2\alpha + \cos^2\beta + \cos^2\gamma + \cos^2\delta = 4/3$

Let side length be $a$.
Vertices: $O(0,0,0), P(a,a,a), A(a,0,0), B(0,a,0), C(0,0,a), M(a,a,0), N(0,a,a), L(a,0,a)$
Diagonals and their d.c.'s:
$OP: \left[\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right]$
$AN: \left[-\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right]$
$BM: \left[\frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right]$
$CL: \left[\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}\right]$

Let $[l, m, n]$ be d.c.'s of the given line.
$\cos\alpha = \frac{l+m+n}{\sqrt{3}}$
$\cos\beta = \frac{-l+m+n}{\sqrt{3}}$
$\cos\gamma = \frac{l-m+n}{\sqrt{3}}$
$\cos\delta = \frac{l+m-n}{\sqrt{3}}$

$\cos^2\alpha + \cos^2\beta + \cos^2\gamma + \cos^2\delta = \frac{(l+m+n)^2 + (-l+m+n)^2 + (l-m+n)^2 + (l+m-n)^2}{3}$
$= \frac{4(l^2+m^2+n^2)}{3}$

Since $l^2+m^2+n^2=1$:
$= \frac{4}{3}$

### Prove that the lines whose direction cosines are given by al+bm+cn=0 and ul^2+vm^2+wn^2=0 are perpendicular if u(b^2+c^2)+v(c^2+a^2)+w(a^2+b^2)=0 and parallel if a^2/u + b^2/v + c^2/w = 0

$al+bm+cn=0 \Rightarrow n = \frac{-(al+bm)}{c}$ --- (1)
$ul^2+vm^2+wn^2=0$ --- (2)

From (1) in (2):
$ul^2+vm^2+w\left(\frac{al+bm}{c}\right)^2=0$
$c^2(ul^2+vm^2) + w(a^2l^2+2ablm+b^2m^2)=0$
$(uc^2+wa^2)l^2 + 2wablm + (vc^2+wb^2)m^2 = 0$

Divide by $m^2$:
$(uc^2+wa^2)\left(\frac{l}{m}\right)^2 + 2wab\left(\frac{l}{m}\right) + (vc^2+wb^2) = 0$ --- (3)

Let roots be $\frac{l_1}{m_1}, \frac{l_2}{m_2}$.
Product of roots: $\frac{l_1l_2}{m_1m_2} = \frac{vc^2+wb^2}{uc^2+wa^2}$
$\Rightarrow \frac{l_1l_2}{vc^2+wb^2} = \frac{m_1m_2}{uc^2+wa^2} = \frac{n_1n_2}{ua^2+vb^2}$ (by symmetry)

For perpendicular lines ($l_1l_2 + m_1m_2 + n_1n_2 = 0$):
$vc^2+wb^2 + uc^2+wa^2 + ua^2+vb^2 = 0$
$u(b^2+c^2) + v(a^2+c^2) + w(a^2+b^2) = 0$

For parallel lines, roots are coincident ($B^2-4AC=0$):
$(2wab)^2 - 4(uc^2+wa^2)(vc^2+wb^2) = 0$
$4w^2a^2b^2 = 4(uvc^4 + uwb^2c^2 + vwa^2c^2 + w^2a^2b^2)$
$c^2(uvc^2 + uwb^2 + vwa^2) = 0$
$uvc^2 + uwb^2 + vwa^2 = 0$

Divide by $uvw$:
$\frac{a^2}{u} + \frac{b^2}{v} + \frac{c^2}{w} = 0$

### Find the eq^n of the plane through the points (2,2,1) & (9,3,6) and perpendicular to the plane 2x+6y+6z=9

Plane through $(2,2,1)$:
$a(x-2) + b(y-2) + c(z-1) = 0$ --- (1)

Passes through $(9,3,6)$:
$a(9-2) + b(3-2) + c(6-1) = 0 \Rightarrow 7a+b+5c=0$ --- (2)

Perpendicular to $2x+6y+6z=9$:
$2a+6b+6c=0$ --- (3)

Eliminating $a,b,c$ from (1), (2), (3):
$\begin{vmatrix} x-2 & y-2 & z-1 \\ 7 & 1 & 5 \\ 2 & 6 & 6 \end{vmatrix} = 0$

$(x-2)(6-30) - (y-2)(42-10) + (z-1)(42-2) = 0$
$-24(x-2) - 32(y-2) + 40(z-1) = 0$

Divide by $-8$:
$3(x-2) + 4(y-2) - 5(z-1) = 0$
$3x - 6 + 4y - 8 - 5z + 5 = 0$
$3x + 4y - 5z = 9$
### A variable plane is at a constant distance p from the origin and meets the axes at A,B,C. Show that the locus of the centroid of the tetrahedron OABC is $x^{-2} + y^{-2} + z^{-2} = 16p^{-2}$

Let the equation of the plane be $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ --- (1)

Since $p$ is the perpendicular distance of (1) from the origin $(0,0,0)$:
$p = \frac{1}{\sqrt{\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}}} \Rightarrow \frac{1}{p^2} = \frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{c^2}$ --- (2)

Since plane (1) meets the axes at $A, B, C$, coordinates are $A(a,0,0)$, $B(0,b,0)$, $C(0,0,c)$.
Let $(x,y,z)$ be the centroid of the tetrahedron OABC ($O$ is $(0,0,0)$).
$x = \frac{a+0+0+0}{4} = \frac{a}{4} \Rightarrow a = 4x$
$y = \frac{0+b+0+0}{4} = \frac{b}{4} \Rightarrow b = 4y$
$z = \frac{0+0+c+0}{4} = \frac{c}{4} \Rightarrow c = 4z$

Putting the values of $a, b, c$ in (2):
$\frac{1}{p^2} = \frac{1}{(4x)^2} + \frac{1}{(4y)^2} + \frac{1}{(4z)^2}$
$\frac{1}{p^2} = \frac{1}{16x^2} + \frac{1}{16y^2} + \frac{1}{16z^2}$
$16p^{-2} = x^{-2} + y^{-2} + z^{-2}$ (Proved)

### Find the distance of the point (-1,-5,-10) from point of intersection of line $\frac{x-2}{3} = \frac{y+1}{4} = \frac{z-2}{12}$ and the plane $x-y+z=5$

Let $\frac{x-2}{3} = \frac{y+1}{4} = \frac{z-2}{12} = r$
Any point on line: $x = 3r+2, y = 4r-1, z = 12r+2$

If the line and plane intersect at this point:
$(3r+2) - (4r-1) + (12r+2) = 5$
$3r + 2 - 4r + 1 + 12r + 2 = 5$
$11r + 5 = 5 \Rightarrow 11r = 0 \Rightarrow r = 0$

Point of intersection: $(2, -1, 2)$

Required distance from $(-1,-5,-10)$ to $(2,-1,2)$:
$d = \sqrt{(2 - (-1))^2 + (-1 - (-5))^2 + (2 - (-10))^2}$
$d = \sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144}$
$d = \sqrt{169} = 13$

### Find the equation to the line through the point (1,2,3) parallel to the line $x-y+2z=5, 3x+y+z=6$

Let $[l,m,n]$ be d.c.'s of the required line.
Since the line is parallel to the given planes' intersection:
$l - m + 2n = 0$
$3l + m + n = 0$

By cross-multiplication:
$\frac{l}{-1 - 2} = \frac{m}{6 - 1} = \frac{n}{1 - (-3)}$
$\frac{l}{-3} = \frac{m}{5} = \frac{n}{4}$

Required equation of the line passing through $(1,2,3)$:
$\frac{x-1}{-3} = \frac{y-2}{5} = \frac{z-3}{4}$

### Find the equation of the line perpendicular to both the lines $\frac{x-1}{1} = \frac{y-1}{2} = \frac{z+2}{3} \ \& \ \frac{x+2}{2} = \frac{y-5}{-1} = \frac{z+3}{2}$ and passing through their intersection

Let $\frac{x-1}{1} = \frac{y-1}{2} = \frac{z+2}{3} = r_1$
Point 1: $(r_1+1, 2r_1+1, 3r_1-2)$

Let $\frac{x+2}{2} = \frac{y-5}{-1} = \frac{z+3}{2} = r_2$
Point 2: $(2r_2-2, -r_2+5, 2r_2-3)$

For intersection:
$r_1+1 = 2r_2-2 \Rightarrow r_1 - 2r_2 = -3$ --- (i)
$2r_1+1 = -r_2+5 \Rightarrow 2r_1 + r_2 = 4$ --- (ii)

Solving (i) & (ii): $r_1=1, r_2=2$
Intersection point is $(2, 3, 1)$.

Let $[l,m,n]$ be d.c.'s of required line.
Perpendicular to given lines:
$l + 2m + 3n = 0$
$2l - m + 2n = 0$

Solving for $l,m,n$:
$\frac{l}{4+3} = \frac{m}{6-2} = \frac{n}{-1-4} \Rightarrow \frac{l}{7} = \frac{m}{4} = \frac{n}{-5}$

Equation of required line:
$\frac{x-2}{7} = \frac{y-3}{4} = \frac{z-1}{-5}$

### Find the eq^n of the line drawn parallel to $\frac{x}{2} = \frac{y}{3} = \frac{z}{4}$ so as to intersect $9x+y+z+4=0=5x+y+3z$ and $x+2y-3z-3=0=2x-5y+3z+3$

The line is produced by intersection of two planes:
$(9x+y+z+4) + k_1(5x+y+3z) = 0 \Rightarrow (9+5k_1)x + (1+k_1)y + (1+3k_1)z + 4 = 0$ --- (i)
$(x+2y-3z-3) + k_2(2x-5y+3z+3) = 0 \Rightarrow (1+2k_2)x + (2-5k_2)y + (-3+3k_2)z + (-3+3k_2) = 0$ --- (ii)

Line is parallel to $\frac{x}{2}=\frac{y}{3}=\frac{z}{4}$, so normals are perpendicular to it:
$2(9+5k_1) + 3(1+k_1) + 4(1+3k_1) = 0 \Rightarrow 18+10k_1+3+3k_1+4+12k_1 = 0 \Rightarrow 25k_1 = -25 \Rightarrow k_1=-1$
$2(1+2k_2) + 3(2-5k_2) + 4(-3+3k_2) = 0 \Rightarrow 2+4k_2+6-15k_2-12+12k_2 = 0 \Rightarrow k_2 = 4$

Substitute $k_1, k_2$ into (i) & (ii):
$(9-5)x + (1-1)y + (1-3)z + 4 = 0 \Rightarrow 4x - 2z + 4 = 0 \Rightarrow 2x - z + 2 = 0$
$(1+8)x + (2-20)y + (-3+12)z + (-3+12) = 0 \Rightarrow 9x - 18y + 9z + 9 = 0 \Rightarrow x - 2y + z + 1 = 0$

Equation of the line: $2x-z+2 = 0 = x-2y+z+1$
Symmetrical form: $\frac{x+1}{2} = \frac{y}{3} = \frac{z}{4}$

### Find the length and Equation of shortest distance bet^n the lines $\frac{x-1}{2} = \frac{y-2}{3} = \frac{z-3}{4} ; \frac{x-2}{3} = \frac{y-4}{4} = \frac{z-5}{5}$

Let $[l,m,n]$ be d.c.'s of S.D. perpendicular to both lines:
$2l + 3m + 4n = 0$
$3l + 4m + 5n = 0$
$\frac{l}{15-16} = \frac{m}{12-10} = \frac{n}{8-9} \Rightarrow \frac{l}{-1} = \frac{m}{2} = \frac{n}{-1}$
$d.c.'s = \left[ \frac{1}{\sqrt{6}}, \frac{-2}{\sqrt{6}}, \frac{1}{\sqrt{6}} \right]$

Points on lines: $P(1,2,3)$, $Q(2,4,5)$.
Length of S.D = Projection of PQ on SD line:
$= (x_2-x_1)l + (y_2-y_1)m + (z_2-z_1)n$
$= (2-1)\frac{1}{\sqrt{6}} + (4-2)\frac{-2}{\sqrt{6}} + (5-3)\frac{1}{\sqrt{6}} = \frac{1}{\sqrt{6}} - \frac{4}{\sqrt{6}} + \frac{2}{\sqrt{6}} = \frac{-1}{\sqrt{6}} \Rightarrow \text{Length} = \frac{1}{\sqrt{6}}$

Equation of plane containing 1st line and SD:
$\begin{vmatrix} x-1 & y-2 & z-3 \\ 2 & 3 & 4 \\ 1 & -2 & 1 \end{vmatrix} = 0 \Rightarrow 11x + 2y - 7z + 6 = 0$

Equation of plane containing 2nd line and SD:
$\begin{vmatrix} x-2 & y-4 & z-5 \\ 3 & 4 & 5 \\ 1 & -2 & 1 \end{vmatrix} = 0 \Rightarrow 14x + 2y - 10z + 14 = 0 \Rightarrow 7x + y - 5z + 7 = 0$

Equation of SD line: $11x + 2y - 7z + 6 = 0 = 7x + y - 5z + 7$

### Show that the lines $\frac{x+1}{2} = \frac{y-2}{2} = \frac{z}{1}$ and $\frac{x-1}{6} = \frac{y+1}{1} = \frac{z-3}{5}$ are co-planer also find their point of intersection and the eq^n of the plane containing these

Condition for coplanarity:
$\begin{vmatrix} x_2-x_1 & y_2-y_1 & z_2-z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = \begin{vmatrix} 1-(-1) & -1-2 & 3-0 \\ 2 & 2 & 1 \\ 6 & 1 & 5 \end{vmatrix} = \begin{vmatrix} 2 & -3 & 3 \\ 2 & 2 & 1 \\ 6 & 1 & 5 \end{vmatrix}$
$= 2(10-1) - (-3)(10-6) + 3(2-12) = 18 + 12 - 30 = 0$. (Lines are coplanar).

Intersection:
Let $\frac{x+1}{2} = \frac{y-2}{2} = \frac{z}{1} = r_1 \Rightarrow (2r_1-1, 2r_1+2, r_1)$
Let $\frac{x-1}{6} = \frac{y+1}{1} = \frac{z-3}{5} = r_2 \Rightarrow (6r_2+1, r_2-1, 5r_2+3)$
$2r_1-1 = 6r_2+1 \Rightarrow 2r_1 - 6r_2 = 2$ --- (i)
$2r_1+2 = r_2-1 \Rightarrow 2r_1 - r_2 = -3$ --- (ii)
$r_1 = 5r_2+3$ --- (iii)

Solving (i) and (ii): $-5r_2 = 5 \Rightarrow r_2 = -1$. Then $r_1 = -2$.
Point of intersection is $(2(-2)-1, 2(-2)+2, -2) = (-5, -2, -2)$.

Equation of plane containing lines:
$\begin{vmatrix} x+1 & y-2 & z \\ 2 & 2 & 1 \\ 6 & 1 & 5 \end{vmatrix} = 0$
$(x+1)(10-1) - (y-2)(10-6) + z(2-12) = 0$
$9x + 9 - 4y + 8 - 10z = 0 \Rightarrow 9x - 4y - 10z + 17 = 0$

### Find the angle bet^n the lines $3x-2y+13=0, y+3z-26=0$ and $\frac{x+4}{5} = \frac{y-1}{-3} = \frac{z-3}{1}$

Direction ratios of 1st line:
$\begin{vmatrix} i & j & k \\ 3 & -2 & 0 \\ 0 & 1 & 3 \end{vmatrix} = (-6, -9, 3) \equiv (-2, -3, 1)$

Direction ratios of 2nd line: $(5, -3, 1)$.
Angle $\theta$:
$\cos\theta = \frac{a_1a_2 + b_1b_2 + c_1c_2}{\sqrt{a_1^2+b_1^2+c_1^2} \sqrt{a_2^2+b_2^2+c_2^2}}$
$\cos\theta = \frac{(-2 \times 5) + (-3 \times -3) + (1 \times 1)}{\sqrt{...}} = \frac{-10 + 9 + 1}{\sqrt{...}} = 0$
$\theta = \pi/2$ (Lines are perpendicular)

### Find the symmetrical form of the equation of a line $x+y+z+1=0 = 4x+y-2z+2$ and find the d.c's of it's

Let $[l,m,n]$ be d.c.'s of the line.
$l + m + n = 0$
$4l + m - 2n = 0$
$\frac{l}{-2-1} = \frac{m}{4+2} = \frac{n}{1-4} \Rightarrow \frac{l}{-3} = \frac{m}{6} = \frac{n}{-3} \Rightarrow \frac{l}{-1} = \frac{m}{2} = \frac{n}{-1} = \frac{1}{\sqrt{6}}$
$d.c.'s = \left[\frac{-1}{\sqrt{6}}, \frac{2}{\sqrt{6}}, \frac{-1}{\sqrt{6}}\right]$

To find a point, let $z=0$:
$x+y+1=0$
$4x+y+2=0$
Subtract: $3x+1=0 \Rightarrow x=-1/3$.
$y = -(-1/3) - 1 = -2/3$.
Point is $(-1/3, -2/3, 0)$.

Symmetrical form:
$\frac{x + 1/3}{-1} = \frac{y + 2/3}{2} = \frac{z}{-1}$

### Find the equation of the line of intersection of the planes $2x-y+2z+7=0$ and $x+2y-3z+6=0$

Let $z=0$:
$2x-y = -7$
$x+2y = -6 \Rightarrow x = -2y-6$
$2(-2y-6)-y = -7 \Rightarrow -4y-12-y = -7 \Rightarrow -5y = 5 \Rightarrow y=-1, x=-4$
Point on line: $(-4, -1, 0)$.

Direction ratios:
$\begin{vmatrix} i & j & k \\ 2 & -1 & 2 \\ 1 & 2 & -3 \end{vmatrix} = (3-4)i - (-6-2)j + (4+1)k = -1, 8, 5$

Equation of line:
$\left[ \frac{x+4}{-1} = \frac{y+1}{8} = \frac{z}{5} \right]$
### A plane cuts the axes at A, B, C. If (p,q,r) be the centroid of the triangle ABC Then show that the eq^n of the plane is x/p + y/q + z/r = 3

Let the equation of the plane be in intercept form:
$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$  --- (1)

The plane cuts the coordinate axes at:
$A(a, 0, 0)$
$B(0, b, 0)$
$C(0, 0, c)$

The centroid $(p, q, r)$ of $\triangle ABC$ is given by:
$p = \frac{a+0+0}{3} \Rightarrow a = 3p$
$q = \frac{0+b+0}{3} \Rightarrow b = 3q$
$r = \frac{0+0+c}{3} \Rightarrow c = 3r$

Substituting the values of $a, b, c$ into equation (1):
$\frac{x}{3p} + \frac{y}{3q} + \frac{z}{3r} = 1$

Multiplying both sides by 3:
$\frac{x}{p} + \frac{y}{q} + \frac{z}{r} = 3$ 
*(Proved)*