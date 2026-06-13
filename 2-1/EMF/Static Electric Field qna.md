### Q.1 (a) Explain the significance of gradient, divergence and curl. Sketch the flux line of $\nabla \cdot \mathbf{E} \neq 0$ and $\nabla \times \mathbf{H} = 0$.

**Significance of Gradient, Divergence, and Curl:**
*   **Gradient ($\nabla V$):** The gradient operates on a scalar field (like electric potential, $V$) and produces a vector field. Its significance lies in the fact that it provides both the direction in which the scalar quantity changes (increases) most rapidly and the magnitude of that maximum rate of change. In electromagnetics, the electric field is the negative gradient of the electric potential ($\mathbf{E} = -\nabla V$), meaning the electric field points in the direction of the steepest decrease in potential.
*   **Divergence ($\nabla \cdot \mathbf{A}$):** The divergence operates on a vector field and results in a scalar field. It represents the net outward flow of flux per unit volume from a given point. Physically, it acts as a measure of the source or sink strength of the field at that point. A positive divergence indicates a source (flux lines spreading out), a negative divergence indicates a sink (flux lines converging), and zero divergence indicates that whatever enters the point also leaves it (no source or sink).
*   **Curl ($\nabla \times \mathbf{A}$):** The curl operates on a vector field and produces another vector field. It represents the maximum circulation (or rotation) of the field per unit area around a point. The direction of the curl vector is the axis of maximum rotation (determined by the right-hand rule). A field with zero curl ($\nabla \times \mathbf{A} = 0$) is called "irrotational" or "conservative," meaning the line integral around any closed path is zero. 

**Sketches:**
*   **$\nabla \cdot \mathbf{E} \neq 0$:** This indicates the presence of a source or a sink (e.g., a point charge). The flux lines will radiate outward from a central point (if positive) or converge inward to a point (if negative). 
    *   *Sketch description:* Draw a central dot with straight arrows radiating outward in all directions like spokes on a wheel.
*   **$\nabla \times \mathbf{H} = 0$:** This indicates an irrotational field with no circulation (e.g., a uniform magnetic field in a region with no current). 
    *   *Sketch description:* Draw a series of straight, parallel arrows pointing in the same direction, indicating no swirling or curling behavior.

*(Related location: Textbook Pages 98, 101, 109; Slides 112, 232)*

***

### Q.1 (b) Two point in free-space are defined as A(4,3,5) and B(8,12,2). If a 2 $\mu$C point charge is located at A, find the cylindrical components of electric field at B.

**Step 1: Find the Cartesian components of the Electric Field at point B.**
The electric field intensity $\mathbf{E}$ at a point $B$ due to a charge $Q$ at point $A$ is given by Coulomb's law:
$$\mathbf{E} = \frac{Q}{4\pi\varepsilon_o|\mathbf{R}_{AB}|^3} \mathbf{R}_{AB}$$
Where $\mathbf{R}_{AB}$ is the distance vector from $A$ to $B$:
$$\mathbf{R}_{AB} = (8 - 4)\hat{a}_x + (12 - 3)\hat{a}_y + (2 - 5)\hat{a}_z = 4\hat{a}_x + 9\hat{a}_y - 3\hat{a}_z$$
The magnitude of the distance vector is:
$$|\mathbf{R}_{AB}| = \sqrt{4^2 + 9^2 + (-3)^2} = \sqrt{16 + 81 + 9} = \sqrt{106} \approx 10.296 \text{ m}$$
Given $Q = 2 \times 10^{-6}$ C and $\frac{1}{4\pi\varepsilon_o} \approx 9 \times 10^9$ m/F:
$$\mathbf{E} = \frac{(2 \times 10^{-6}) \times (9 \times 10^9)}{(\sqrt{106})^3} (4\hat{a}_x + 9\hat{a}_y - 3\hat{a}_z)$$
$$\mathbf{E} = \frac{18000}{106\sqrt{106}} (4\hat{a}_x + 9\hat{a}_y - 3\hat{a}_z) \approx 16.49(4\hat{a}_x + 9\hat{a}_y - 3\hat{a}_z) \text{ V/m}$$
Cartesian components of $\mathbf{E}$ at B:
*   $E_x = 16.49 \times 4 = 65.96$ V/m
*   $E_y = 16.49 \times 9 = 148.41$ V/m
*   $E_z = 16.49 \times -3 = -49.47$ V/m

**Step 2: Transform the Cartesian components to Cylindrical components at point B.**
The observation point $B$ is at Cartesian coordinates $(x,y,z) = (8, 12, 2)$.
We need the cylindrical angle $\phi$ at this specific point to perform the vector transformation:
$$\rho = \sqrt{x^2 + y^2} = \sqrt{8^2 + 12^2} = \sqrt{64 + 144} = \sqrt{208} \approx 14.422$$
$$\cos\phi = \frac{x}{\rho} = \frac{8}{\sqrt{208}} \approx 0.5547$$
$$\sin\phi = \frac{y}{\rho} = \frac{12}{\sqrt{208}} \approx 0.8321$$

Using the vector transformation matrix from Cartesian to Cylindrical:
*   $E_\rho = E_x\cos\phi + E_y\sin\phi$
*   $E_\phi = -E_x\sin\phi + E_y\cos\phi$
*   $E_z = E_z$

Substituting the values:
$$E_\rho = (65.96)(0.5547) + (148.41)(0.8321) = 36.59 + 123.50 = \mathbf{160.09 \text{ V/m}}$$
$$E_\phi = -(65.96)(0.8321) + (148.41)(0.5547) = -54.89 + 82.32 = \mathbf{27.43 \text{ V/m}}$$
$$E_z = \mathbf{-49.47 \text{ V/m}}$$

The cylindrical components of the electric field at point B are **$160.09\hat{a}_\rho + 27.43\hat{a}_\phi - 49.47\hat{a}_z$ V/m**.

*(Related location: Textbook Page 33, Page 60 (eq 2.15); Slide 36)*

***

### Q.1 (c) What do you understand by the conservative property of potential function? State how Kirchhoff's Voltage Law (K.V.L.) is originated from this property.

**Conservative Property of Potential Function:**
The conservative property of an electrostatic field (and its associated potential function) means that the work done in moving a point charge from one location to another is completely independent of the path taken between the two points. Mathematically, this is expressed by stating that the line integral of the electric field $\mathbf{E}$ around any closed path $L$ is exactly zero:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$$
By applying Stokes's theorem, this integral form converts to the differential form $\nabla \times \mathbf{E} = 0$. Because the curl is zero, the electric field can be expressed as the negative gradient of a scalar potential field ($\mathbf{E} = -\nabla V$). Therefore, the potential difference between two points is uniquely defined and does not rely on the trajectory.

**Origination of Kirchhoff's Voltage Law (K.V.L.):**
Kirchhoff's Voltage Law states that the algebraic sum of the potential differences (voltages) around any closed loop in an electrical circuit is zero ($\sum V = 0$). This is the direct macroscopic, lumped-circuit equivalent of the conservative property of the electrostatic field. Because $\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$, the sum of the voltage drops (where $V = -\int \mathbf{E} \cdot d\mathbf{l}$) across all components in a closed circuit path must identically evaluate to zero, ensuring energy conservation within the circuit.

*(Related location: Textbook Page 147-148, Page 372 (Table 8.4); Slide 108-109)*

***

### Q.2 (a) State Gauss's Law in electrostatic with necessary mathematical expression. Using this law obtain the expression of electric fields due to an uniformly charged infinitely charge plane of thin sheet with surface charge density of $\rho_s$ C/m$^2$.

**Gauss's Law:**
Gauss's Law states that the total electric flux ($\Psi$) passing through any closed imaginary surface (a Gaussian surface) is equal to the total net electric charge ($Q_{enc}$) enclosed by that surface.
*   **Integral Form:** $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ (where $\mathbf{D} = \varepsilon_0\mathbf{E}$ is the electric flux density).
*   **Differential (Point) Form:** $\nabla \cdot \mathbf{D} = \rho_v$ (where $\rho_v$ is the volume charge density).

**Electric Field due to an Infinite Sheet of Charge:**
1.  **Symmetry and Gaussian Surface:** Consider an infinite sheet lying in the $xy$-plane ($z=0$) with a uniform surface charge density $\rho_s$. By symmetry, the electric field $\mathbf{E}$ (and thus $\mathbf{D}$) must be perpendicular to the sheet, pointing directly away from it (along $+\hat{a}_z$ for $z>0$ and $-\hat{a}_z$ for $z<0$). 
2.  We construct a Gaussian surface in the shape of a rectangular box (or pillbox) that is cut symmetrically by the sheet. Let the top and bottom faces each have an area $A$, parallel to the sheet.
3.  **Applying the Integral Form:** 
    $$Q_{enc} = \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_{top} \mathbf{D} \cdot d\mathbf{S} + \int_{bottom} \mathbf{D} \cdot d\mathbf{S} + \int_{sides} \mathbf{D} \cdot d\mathbf{S}$$
4.  **Evaluating the Integrals:**
    *   The charge enclosed by the box is $Q_{enc} = \rho_s A$.
    *   On the sides of the box, $\mathbf{D}$ is parallel to the surface, so $\mathbf{D} \cdot d\mathbf{S} = 0$.
    *   On the top face, $\mathbf{D} = D_z \hat{a}_z$ and $d\mathbf{S} = dS \hat{a}_z$, so $\int_{top} \mathbf{D} \cdot d\mathbf{S} = D_z A$.
    *   On the bottom face, $\mathbf{D} = -D_z \hat{a}_z$ and $d\mathbf{S} = -dS \hat{a}_z$, so $\int_{bottom} \mathbf{D} \cdot d\mathbf{S} = D_z A$.
5.  **Solving:**
    $$\rho_s A = D_z A + D_z A = 2D_z A$$
    $$D_z = \frac{\rho_s}{2} \implies \mathbf{D} = \frac{\rho_s}{2}\hat{a}_n$$
    Since $\mathbf{D} = \varepsilon_0\mathbf{E}$, the electric field intensity is:
    $$\mathbf{E} = \frac{\rho_s}{2\varepsilon_0}\hat{a}_n$$
    where $\hat{a}_n$ is the unit vector pointing normally away from the sheet.

*(Related location: Textbook Page 157, Page 161; Slides 52-57)*

***

### Q.2 (b) Spherical surface at r = 2, 4 and 6m carry uniform surface charge densities of 20 nC/m$^2$, -4 nC/m$^2$, and $\rho_{so}$ respectively. (i) Find the electric flux density, $\mathbf{D}$ at r = 1, 3, and 5m. (ii) Determine the $\rho_{so}$ such that $\mathbf{D} = 0$ at r = 7m.

**Preliminary Step: Calculate Total Charge on Each Surface**
The total charge on a spherical surface of radius $r$ is $Q = \rho_s \times Area = \rho_s \times 4\pi r^2$.
*   Sphere 1 ($r_1 = 2$ m): $Q_1 = (20 \times 10^{-9}) \times 4\pi(2)^2 = 320\pi \text{ nC}$
*   Sphere 2 ($r_2 = 4$ m): $Q_2 = (-4 \times 10^{-9}) \times 4\pi(4)^2 = -256\pi \text{ nC}$
*   Sphere 3 ($r_3 = 6$ m): $Q_3 = \rho_{so} \times 4\pi(6)^2 = 144\pi \rho_{so} \text{ (where } \rho_{so} \text{ is in nC/m}^2\text{)}$

**Part (i): Find $\mathbf{D}$ at $r = 1, 3,$ and $5$ m.**
Using Gauss's Law for spherical symmetry: $\mathbf{D} = \frac{Q_{enc}}{4\pi r^2}\hat{a}_r$

*   **At $r = 1$ m:** 
    The Gaussian surface is inside the innermost sphere. 
    $Q_{enc} = 0 \implies \mathbf{D} = \mathbf{0 \text{ nC/m}^2}$

*   **At $r = 3$ m:** 
    The Gaussian surface encloses only Sphere 1.
    $Q_{enc} = Q_1 = 320\pi \text{ nC}$
    $\mathbf{D} = \frac{320\pi \times 10^{-9}}{4\pi (3)^2}\hat{a}_r = \frac{80}{9} \text{ nC/m}^2 \hat{a}_r \approx \mathbf{8.89 \hat{a}_r \text{ nC/m}^2}$

*   **At $r = 5$ m:** 
    The Gaussian surface encloses Sphere 1 and Sphere 2.
    $Q_{enc} = Q_1 + Q_2 = 320\pi \text{ nC} - 256\pi \text{ nC} = 64\pi \text{ nC}$
    $\mathbf{D} = \frac{64\pi \times 10^{-9}}{4\pi (5)^2}\hat{a}_r = \frac{16}{25} \text{ nC/m}^2 \hat{a}_r = \mathbf{0.64 \hat{a}_r \text{ nC/m}^2}$

**Part (ii): Determine $\rho_{so}$ such that $\mathbf{D} = 0$ at $r = 7$ m.**
For $\mathbf{D}$ to be $0$ at $r = 7$ m, the total charge enclosed by a Gaussian sphere of radius $7$ m must be zero. This surface encloses all three spherical shells.
$$Q_{enc} = Q_1 + Q_2 + Q_3 = 0$$
Substitute the values calculated earlier (working in nC):
$$320\pi - 256\pi + 144\pi \rho_{so} = 0$$
$$64\pi + 144\pi \rho_{so} = 0$$
Divide by $\pi$:
$$144 \rho_{so} = -64$$
$$\rho_{so} = -\frac{64}{144} = -\frac{4}{9} \approx \mathbf{-0.444 \text{ nC/m}^2}$$

*(Related location: Textbook Page 162, Page 196 (Problem 4.27); Slide 164)*
### (c) State image theory in electrostatic with necessary figures.

**Statement of Image Theory:**
The method of images (or image theory) is a technique used to determine electric fields, potentials, and charge distributions in the presence of conducting boundaries. 

The **image theory** states that a given charge configuration located above an infinite, grounded, perfect conducting plane may be replaced by the original charge configuration itself, its *image* configuration placed below the plane, and an equipotential surface taking the place of the conducting plane. 

This technique works because it satisfies Poisson's/Laplace's equation in the region of interest while also satisfying the necessary boundary conditions (specifically, that the potential $V = 0$ on the grounded conducting plane).

**Necessary Figures (Description for Sketching):**

To illustrate this, you should sketch two corresponding figures side-by-side:

*   **Figure A (The Original Physical System):**
    1.  Draw a horizontal line representing an infinite, perfectly conducting plane. Shade the area below the line to indicate the conductor. Label the line "$V = 0$".
    2.  Place a positive point charge "$+Q$" at a distance "$h$" directly above the conducting plane.
    3.  Draw electric field lines emanating from $+Q$ and terminating perpendicular to the conducting plane.

*   **Figure B (The Equivalent Image System):**
    1.  Draw a horizontal dashed line in the exact same position as the conducting plane in Figure A. Label this "Equipotential surface $V = 0$". Do not shade below it; the conductor is gone.
    2.  Place the original positive point charge "$+Q$" at distance "$h$" above the dashed line.
    3.  Place an **image charge** "$-Q$" directly below the original charge at a distance "$h$" below the dashed line (so the total distance between $+Q$ and $-Q$ is $2h$).
    4.  Draw electric field lines starting from $+Q$ and ending on $-Q$. In the upper half of the space (above the dashed line), these field lines will look exactly identical to the field lines in Figure A.

*(Related location: Textbook Pages 266-267; Slide 167, 169)*

***

### Q.3 (a) Explain the boundary conditions for electrostatic and magnetostatic fields.

Boundary conditions dictate how electromagnetic fields behave as they cross an interface separating two different media (e.g., moving from a dielectric to a conductor, or from one magnetic material to another). We analyze these by breaking the fields into components tangential (parallel) to the boundary and normal (perpendicular) to the boundary.

**1. Electrostatic Boundary Conditions (Electric Fields $\mathbf{E}$ and $\mathbf{D}$):**
These are derived using $\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$ and Gauss's Law $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$.

*   **Tangential Component:** The tangential component of the electric field intensity ($\mathbf{E}$) is continuous across the boundary. This means the field does not change abruptly parallel to the interface.
    $$E_{1t} = E_{2t}$$
    Consequently, because $\mathbf{D} = \varepsilon\mathbf{E}$, the tangential component of electric flux density ($\mathbf{D}$) is discontinuous if the permittivities are different: $\frac{D_{1t}}{\varepsilon_1} = \frac{D_{2t}}{\varepsilon_2}$.

*   **Normal Component:** The normal component of the electric flux density ($\mathbf{D}$) is discontinuous across the boundary by an amount equal to the free surface charge density ($\rho_S$) present at the interface.
    $$D_{1n} - D_{2n} = \rho_S$$
    If there is no free charge deliberately placed at the boundary (a perfect dielectric-dielectric interface), then the normal component of $\mathbf{D}$ is continuous: $D_{1n} = D_{2n}$. Because of this, the normal component of $\mathbf{E}$ is generally discontinuous: $\varepsilon_1 E_{1n} = \varepsilon_2 E_{2n}$.

**2. Magnetostatic Boundary Conditions (Magnetic Fields $\mathbf{H}$ and $\mathbf{B}$):**
These are derived using Gauss's Law for magnetic fields $\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$ and Ampère's Law $\oint_L \mathbf{H} \cdot d\mathbf{l} = I_{enc}$.

*   **Normal Component:** The normal component of the magnetic flux density ($\mathbf{B}$) is continuous across the boundary. This reflects the fact that magnetic monopoles do not exist.
    $$B_{1n} = B_{2n}$$
    Since $\mathbf{B} = \mu\mathbf{H}$, the normal component of magnetic field intensity ($\mathbf{H}$) is discontinuous if the permeabilities are different: $\mu_1 H_{1n} = \mu_2 H_{2n}$.

*   **Tangential Component:** The tangential component of the magnetic field intensity ($\mathbf{H}$) is discontinuous across the boundary by an amount equal to the free surface current density ($\mathbf{K}$) at the interface.
    $$(\mathbf{H}_1 - \mathbf{H}_2) \times \mathbf{a}_{n12} = \mathbf{K} \quad \text{or} \quad H_{1t} - H_{2t} = K$$
    If the boundary is free of current (which is typical for boundaries between two insulating magnetic materials), then the tangential component of $\mathbf{H}$ is continuous: $H_{1t} = H_{2t}$.

*(Related location: Textbook Pages 198-200 for Electrostatics; Pages 375-377 for Magnetostatics)*

***

### (b) Derive the equation of continuity, $\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}$. Write the physical significance of the equation.

**Derivation:**
1.  We start with the fundamental principle of the **conservation of charge**. Consider an arbitrary closed surface $S$ enclosing a volume $v$. 
2.  If there is a net outward flow of positive charge through this closed surface, it constitutes a current $I_{out}$. By definition, this current is the surface integral of the current density $\mathbf{J}$:
    $$I_{out} = \oint_S \mathbf{J} \cdot d\mathbf{S}$$
3.  Because charge cannot be created or destroyed, this outward flow of current must be exactly balanced by a decrease in the total charge $Q_{in}$ enclosed within the volume $v$. 
    $$I_{out} = -\frac{dQ_{in}}{dt}$$
4.  The total enclosed charge $Q_{in}$ can be expressed as the volume integral of the volume charge density $\rho_v$ (notated as $\rho$ in your prompt):
    $$Q_{in} = \int_v \rho_v \, dv$$
5.  Substituting step 4 into step 3 gives:
    $$I_{out} = -\frac{d}{dt} \int_v \rho_v \, dv$$
6.  Now, equate the expression for $I_{out}$ from step 2 with the expression from step 5:
    $$\oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{d}{dt} \int_v \rho_v \, dv$$
    Assuming the volume $v$ is stationary (its boundary does not change with time), we can bring the time derivative inside the integral as a partial derivative:
    $$\oint_S \mathbf{J} \cdot d\mathbf{S} = -\int_v \frac{\partial \rho_v}{\partial t} \, dv$$
7.  Apply the **Divergence Theorem** to the left side of the equation. The Divergence Theorem relates a surface integral to a volume integral: $\oint_S \mathbf{J} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{J}) \, dv$. Substituting this into our equation:
    $$\int_v (\nabla \cdot \mathbf{J}) \, dv = -\int_v \frac{\partial \rho_v}{\partial t} \, dv$$
8.  For this equality to hold true for *any* arbitrary volume $v$, the integrands themselves must be equal at every point in space. Therefore:
    $$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$
    *(Note: Using the notation from the prompt where volume charge density is $\rho$, this is written as $\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}$)*.

**Physical Significance:**
The equation of continuity is the mathematical expression of the **principle of conservation of electric charge** applied to a specific point in space. 

It states that the divergence of current density ($\nabla \cdot \mathbf{J}$, which represents the net rate at which charge is flowing outward from a point) is exactly equal to the rate of decrease of the charge density at that specific point ($-\frac{\partial \rho}{\partial t}$). In simpler terms: charge cannot accumulate or vanish at a point out of nowhere. If current is flowing away from a point, the amount of charge stored at that point must be decreasing proportionally. In a steady-state condition (direct current), $\frac{\partial \rho}{\partial t} = 0$, meaning $\nabla \cdot \mathbf{J} = 0$ (what goes in must come out, which is the basis for Kirchhoff's Current Law).

*(Related location: Textbook Page 196; Slide 140-144)*
### b) Show that the electric field for a sheet of charge of uniform charge density is constant in magnitude and direction, and it does not vary with the distance from the sheet.

**Proof using Gauss's Law:**

1.  **Define the Geometry:** Consider an infinite sheet of charge lying in the $xy$-plane (at $z = 0$) with a uniform surface charge density $\rho_s$ (in C/m$^2$).
2.  **Determine Field Direction:** By symmetry, the electric field $\mathbf{E}$ (and the electric flux density $\mathbf{D} = \varepsilon_0\mathbf{E}$) cannot have any $x$- or $y$-components. For any charge element producing a non-vertical field component, there is a corresponding symmetric charge element producing an equal and opposite non-vertical component, causing them to cancel out. Therefore, the field must be entirely normal (perpendicular) to the sheet.
    *   Above the sheet ($z > 0$), $\mathbf{D}$ points in the $+\hat{a}_z$ direction.
    *   Below the sheet ($z < 0$), $\mathbf{D}$ points in the $-\hat{a}_z$ direction.
3.  **Construct a Gaussian Surface:** Choose a rectangular box (a "pillbox") that is cut symmetrically by the charged sheet. Let the top face (at $z > 0$) and bottom face (at $z < 0$) each have an area $A$ and be parallel to the sheet. 
4.  **Apply Gauss's Law:** Gauss's law states that the total outward electric flux through the closed surface $S$ equals the enclosed charge:
    $$\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$$
5.  **Evaluate the Enclosed Charge:** The charge enclosed by the pillbox is simply the surface charge density multiplied by the area of the sheet captured within the box:
    $$Q_{enc} = \rho_s A$$
6.  **Evaluate the Surface Integral:** The integral over the closed surface is the sum of the integrals over the top, bottom, and sides of the pillbox:
    $$\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_{top} \mathbf{D} \cdot d\mathbf{S} + \int_{bottom} \mathbf{D} \cdot d\mathbf{S} + \int_{sides} \mathbf{D} \cdot d\mathbf{S}$$
    *   **Sides:** On the vertical sides, $\mathbf{D}$ is parallel to the surface (or perpendicular to the surface normal vector $d\mathbf{S}$), so $\mathbf{D} \cdot d\mathbf{S} = 0$.
    *   **Top:** On the top face, $\mathbf{D} = D_z \hat{a}_z$ and the area vector is $d\mathbf{S} = dS \hat{a}_z$. Thus, $\int_{top} \mathbf{D} \cdot d\mathbf{S} = D_z \int dS = D_z A$.
    *   **Bottom:** On the bottom face, the field points downwards ($\mathbf{D} = -D_z \hat{a}_z$) and the outward area vector also points downwards ($d\mathbf{S} = -dS \hat{a}_z$). Thus, $\int_{bottom} (-D_z \hat{a}_z) \cdot (-dS \hat{a}_z) = D_z \int dS = D_z A$.
7.  **Equate and Solve:**
    $$D_z A + D_z A = \rho_s A$$
    $$2D_z A = \rho_s A$$
    $$D_z = \frac{\rho_s}{2}$$
8.  **Express as Electric Field $\mathbf{E}$:** 
    Since $\mathbf{D} = \frac{\rho_s}{2}\hat{a}_n$ (where $\hat{a}_n$ is the outward normal vector), and $\mathbf{D} = \varepsilon_0\mathbf{E}$ for free space:
    $$\mathbf{E} = \frac{\rho_s}{2\varepsilon_0}\hat{a}_n$$

**Conclusion:** 
The derived formula $\mathbf{E} = \frac{\rho_s}{2\varepsilon_0}\hat{a}_n$ shows that the electric field intensity depends only on the charge density $\rho_s$ and the permittivity $\varepsilon_0$. 
*   **Magnitude:** $\frac{\rho_s}{2\varepsilon_0}$ is a constant value.
*   **Direction:** $\hat{a}_n$ is always normal to the sheet (constant direction).
*   **Distance dependency:** The variable representing distance from the sheet ($z$) does not appear in the final equation. Therefore, the field is uniform and does not vary with distance from the sheet.

*(Related location: Textbook Page 161, Section 4.6C)*

***

### c) The charge density varies with radius in a cylindrical coordinate system as $\rho_v = \frac{\rho_0}{(\rho^2+a^2)^2}$ C/m$^3$. Within what distance from the z-axis does half the total charge lie?

**Step 1: Calculate the total charge per unit length ($Q_{total}$)**
To find the total charge, we must integrate the volume charge density over all space in cylindrical coordinates. Since the cylinder extends infinitely in the $z$-direction, we will calculate the charge per unit length, $L$.
The volume differential in cylindrical coordinates is $dv = \rho \, d\rho \, d\phi \, dz$.
$$Q_{total\_per\_L} = \int_{0}^{2\pi} \int_{0}^{\infty} \rho_v \, \rho \, d\rho \, d\phi$$
$$Q_{total\_per\_L} = \int_{0}^{2\pi} d\phi \int_{0}^{\infty} \frac{\rho_0}{(\rho^2+a^2)^2} \rho \, d\rho$$
$$Q_{total\_per\_L} = 2\pi \rho_0 \int_{0}^{\infty} \frac{\rho}{(\rho^2+a^2)^2} \, d\rho$$

To solve the integral, use $u$-substitution:
Let $u = \rho^2 + a^2 \implies du = 2\rho \, d\rho \implies \rho \, d\rho = \frac{du}{2}$
When $\rho = 0$, $u = a^2$. When $\rho \to \infty$, $u \to \infty$.
$$\int_{0}^{\infty} \frac{\rho}{(\rho^2+a^2)^2} \, d\rho = \frac{1}{2} \int_{a^2}^{\infty} \frac{1}{u^2} \, du = \frac{1}{2} \left[ -\frac{1}{u} \right]_{a^2}^{\infty} = \frac{1}{2} \left( 0 - \left(-\frac{1}{a^2}\right) \right) = \frac{1}{2a^2}$$
Substituting this back into the total charge equation:
$$Q_{total\_per\_L} = 2\pi \rho_0 \left( \frac{1}{2a^2} \right) = \frac{\pi \rho_0}{a^2}$$

**Step 2: Calculate the charge enclosed within an arbitrary radius $R$ ($Q_{enc}$)**
We repeat the integration, but this time set the upper limit of the $\rho$ integral to an unknown radius $R$:
$$Q_{enc}(R) = 2\pi \rho_0 \int_{0}^{R} \frac{\rho}{(\rho^2+a^2)^2} \, d\rho$$
Using the same integral evaluation as above, but with the new upper limit:
$$Q_{enc}(R) = 2\pi \rho_0 \left[ -\frac{1}{2(\rho^2+a^2)} \right]_{0}^{R}$$
$$Q_{enc}(R) = 2\pi \rho_0 \left( -\frac{1}{2(R^2+a^2)} - \left(-\frac{1}{2(0^2+a^2)}\right) \right)$$
$$Q_{enc}(R) = 2\pi \rho_0 \left( \frac{1}{2a^2} - \frac{1}{2(R^2+a^2)} \right) = \pi \rho_0 \left( \frac{1}{a^2} - \frac{1}{R^2+a^2} \right)$$

**Step 3: Solve for the distance $R$ where half the total charge lies**
We set the enclosed charge $Q_{enc}(R)$ equal to half of the total charge $Q_{total\_per\_L}$:
$$Q_{enc}(R) = \frac{1}{2} Q_{total\_per\_L}$$
$$\pi \rho_0 \left( \frac{1}{a^2} - \frac{1}{R^2+a^2} \right) = \frac{1}{2} \left( \frac{\pi \rho_0}{a^2} \right)$$
Divide both sides by $\pi \rho_0$:
$$\frac{1}{a^2} - \frac{1}{R^2+a^2} = \frac{1}{2a^2}$$
Rearrange to solve for the term containing $R$:
$$\frac{1}{a^2} - \frac{1}{2a^2} = \frac{1}{R^2+a^2}$$
$$\frac{1}{2a^2} = \frac{1}{R^2+a^2}$$
Inverting both sides:
$$2a^2 = R^2 + a^2$$
$$R^2 = a^2$$
Taking the positive root (since radius must be positive):
$$R = a$$

Half the total charge lies within the distance **$R = a$** from the z-axis.

*(Integration techniques related to volume integrals in cylindrical coordinates: Textbook Section 3.2)*

***

### Q.2 a) State potential function and its conservative property.

**Potential Function:**
The electric scalar potential $V$ at any specific point in an electric field is defined as the work done (by an external agent) per unit charge in transferring a positive test charge from a reference point (usually assumed to be at infinity where potential is zero) to that specific point. Mathematically, it is expressed as:
$$V = -\int_{\infty}^{r} \mathbf{E} \cdot d\mathbf{l}$$
It is a scalar field that completely describes the electrostatic field. The electric field intensity $\mathbf{E}$ can be obtained back from the potential function by taking its negative gradient: $\mathbf{E} = -\nabla V$.

**Conservative Property:**
An electrostatic field is a conservative field. The conservative property means that the total work done in moving a point charge along any closed path within the electric field is identically zero. This implies that the potential difference (or work done) between any two points is completely independent of the path taken between them. 
Mathematically, this is stated by the closed line integral of the electric field being zero:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$$
By applying Stokes's theorem ($\oint_L \mathbf{E} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S}$), this integral form yields the differential form showing the field is irrotational:
$$\nabla \times \mathbf{E} = 0$$
Any vector field that satisfies this condition is conservative, allowing it to be expressed as the gradient of a scalar potential field.

*(Related location: Textbook Page 166, Section 4.7; Page 147-148, Section 4.8)*

***

### Q.2 b) Mathematically show how you can obtain Maxwell's divergence equation about electric flux density in electrostatics using Gauss's law.

**Derivation:**
1.  **Start with the Integral form of Gauss's Law:** 
    Gauss's law states that the total electric flux ($\Psi$) penetrating any closed surface $S$ is exactly equal to the total net charge ($Q_{enc}$) enclosed by that mathematical surface.
    $$\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$$
    Where $\mathbf{D}$ is the electric flux density vector and $d\mathbf{S}$ is the differential normal surface area vector.

2.  **Express the Enclosed Charge as a Volume Integral:**
    If the charge is distributed continuously throughout a volume $v$ enclosed by the surface $S$ with a volume charge density $\rho_v$, the total enclosed charge can be expressed mathematically as a volume integral:
    $$Q_{enc} = \int_v \rho_v \, dv$$
    Substitute this back into the Gauss's Law equation:
    $$\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v \, dv$$

3.  **Apply the Divergence Theorem:**
    The Divergence Theorem (or Gauss-Ostrogradsky theorem) is a mathematical identity that relates the surface integral of a vector field over a closed surface to the volume integral of the divergence of that field over the enclosed volume. Applying it to the left side of our equation gives:
    $$\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{D}) \, dv$$

4.  **Equate the Volume Integrals:**
    Substitute the result from the Divergence Theorem back into the equation from Step 2:
    $$\int_v (\nabla \cdot \mathbf{D}) \, dv = \int_v \rho_v \, dv$$

5.  **Extract the Differential Equation:**
    For the volume integrals on both sides to be equal for *any* arbitrarily chosen volume $v$, the integrands themselves must be identically equal everywhere in space. Therefore, we can drop the integral signs to obtain the point (or differential) form:
    $$\nabla \cdot \mathbf{D} = \rho_v$$
    
This final expression is Maxwell's divergence equation for electrostatics (also known as the point form of Gauss's law). It states that the divergence of the electric flux density at any point is exactly equal to the volume charge density at that point.

*(Related location: Textbook Page 158, Section 4.5)*
### An infinite line charge of charge density $\rho_L$ C/m is located along the z-axis as shown in the figure below. Calculate the work done for carrying a positive charge of amount Q from point a-to-b in case of figure 1 and figure 2.
![[Pasted image 20260613154427.jpg]]
**Calculation for Figure 1:**
In Figure 1, the path from point $a$ to point $b$ lies on a circular trajectory with a constant radius $\rho_1$ centered around the infinite line charge. 
The electric field intensity $\mathbf{E}$ generated by an infinite line charge along the z-axis is strictly radial:
$$\mathbf{E} = \frac{\rho_L}{2\pi\varepsilon_0 \rho} \mathbf{a}_\rho$$
The work done $W$ in moving a charge $Q$ from point $a$ to point $b$ is given by the line integral:
$$W = -Q \int_{a}^{b} \mathbf{E} \cdot d\mathbf{L}$$
Because the path is circular, the differential length vector $d\mathbf{L}$ is entirely in the azimuthal ($\phi$) direction:
$$d\mathbf{L} = \rho_1 \, d\phi \, \mathbf{a}_\phi$$
Evaluating the dot product inside the integral:
$$\mathbf{E} \cdot d\mathbf{L} = \left( \frac{\rho_L}{2\pi\varepsilon_0 \rho_1} \mathbf{a}_\rho \right) \cdot (\rho_1 \, d\phi \, \mathbf{a}_\phi) = 0$$
Because the radial vector $\mathbf{a}_\rho$ and the azimuthal vector $\mathbf{a}_\phi$ are orthogonal ($\mathbf{a}_\rho \cdot \mathbf{a}_\phi = 0$), the integral evaluates to zero. 
Therefore, **the work done is $W = 0$**. This makes sense because a circular path around an infinite line charge is an equipotential surface, and moving a charge along an equipotential surface requires no work.

**Calculation for Figure 2:**
In Figure 2, the path from point $a$ to point $b$ is a radial line. Let's denote the radial distance of point $a$ from the z-axis as $\rho_a$ (or simply $a$) and the radial distance of point $b$ as $\rho_b$ (or simply $b$).
The differential length vector for a purely radial path is:
$$d\mathbf{L} = d\rho \, \mathbf{a}_\rho$$
Setting up the work integral:
$$W = -Q \int_{a}^{b} \mathbf{E} \cdot d\mathbf{L} = -Q \int_{a}^{b} \left( \frac{\rho_L}{2\pi\varepsilon_0 \rho} \mathbf{a}_\rho \right) \cdot (d\rho \, \mathbf{a}_\rho)$$
Since $\mathbf{a}_\rho \cdot \mathbf{a}_\rho = 1$, the integral simplifies to:
$$W = -Q \frac{\rho_L}{2\pi\varepsilon_0} \int_{a}^{b} \frac{1}{\rho} \, d\rho$$
Evaluating the integral:
$$W = -Q \frac{\rho_L}{2\pi\varepsilon_0} [\ln \rho]_{a}^{b} = -Q \frac{\rho_L}{2\pi\varepsilon_0} (\ln b - \ln a)$$
$$W = -\frac{Q \rho_L}{2\pi\varepsilon_0} \ln\left(\frac{b}{a}\right)$$
This is the work done by the external source.

*(Related location: Slides 84-87, Page 90)*

***

### a) What is dipole moment and polarization vector, P? It is known that in free space $\bar{D} = \epsilon_0 \bar{E}$. Obtain the modified expression of $\bar{D}$ when polarizable material is present.

**Definitions:**
*   **Dipole Moment ($\mathbf{p}$):** An electric dipole is formed by two point charges of equal magnitude but opposite sign ($+Q$ and $-Q$) separated by a small distance. The electric dipole moment is a vector quantity defined as the product of the charge magnitude $Q$ and the distance vector $\mathbf{d}$ directed from the negative charge to the positive charge:
    $$\mathbf{p} = Q\mathbf{d}$$
*   **Polarization Vector ($\mathbf{P}$):** When a dielectric material is subjected to an external electric field, the atomic or molecular dipoles within it align with the field. The polarization vector $\mathbf{P}$ is defined as the total dipole moment per unit volume of the dielectric material. It is a measure of the intensity of the polarization:
    $$\mathbf{P} = \lim_{\Delta v \to 0} \frac{\sum_{k=1}^{N} \mathbf{p}_k}{\Delta v}$$
    where $N$ is the number of dipoles in the volume element $\Delta v$.

**Modified Expression for $\mathbf{D}$:**
In free space, the electric flux density is simply $\mathbf{D} = \varepsilon_0\mathbf{E}$. 
However, when a polarizable dielectric material is introduced, the applied electric field $\mathbf{E}$ causes the material to polarize, creating bound volume and surface charge densities ($\rho_{pv}$ and $\rho_{ps}$). 
If the region also contains free charge density $\rho_v$, the total volume charge density $\rho_t$ is the sum of the free and bound volume charges:
$$\rho_t = \rho_v + \rho_{pv}$$
From Gauss's Law in free space, the divergence of $\varepsilon_0\mathbf{E}$ equals the total charge density:
$$\nabla \cdot (\varepsilon_0\mathbf{E}) = \rho_t = \rho_v + \rho_{pv}$$
We know that the bound volume charge density is related to the polarization vector by $\rho_{pv} = -\nabla \cdot \mathbf{P}$. Substituting this in gives:
$$\nabla \cdot (\varepsilon_0\mathbf{E}) = \rho_v - \nabla \cdot \mathbf{P}$$
Rearranging to group the divergence terms:
$$\rho_v = \nabla \cdot (\varepsilon_0\mathbf{E}) + \nabla \cdot \mathbf{P} = \nabla \cdot (\varepsilon_0\mathbf{E} + \mathbf{P})$$
Because Gauss's Law for electric flux density defines that $\nabla \cdot \mathbf{D} = \rho_v$ (where $\rho_v$ is *free* charge density), we can equate the terms inside the divergence operator to obtain the modified expression for $\mathbf{D}$ in a dielectric medium:
$$\mathbf{D} = \varepsilon_0\mathbf{E} + \mathbf{P}$$

*(Related location: Textbook Pages 187, 189-190; Slides 178-181, 188)*

***

### b) State and prove Poisson's equation in electrostatics.

**Statement:**
Poisson's equation is a second-order partial differential equation that relates the electric scalar potential $V$ at a point in a medium to the volume charge density $\rho_v$ at that point, taking into account the permittivity $\varepsilon$ of the medium. It states that the Laplacian of the potential field is equal to the negative of the volume charge density divided by the permittivity.
$$\nabla^2 V = -\frac{\rho_v}{\varepsilon}$$

**Proof:**
1.  **Start with the point form of Gauss's Law:**
    $$\nabla \cdot \mathbf{D} = \rho_v$$
    where $\mathbf{D}$ is the electric flux density and $\rho_v$ is the volume charge density.
2.  **Apply the constitutive relation:**
    For a linear, isotropic, and homogeneous medium, the electric flux density is related to the electric field intensity $\mathbf{E}$ by:
    $$\mathbf{D} = \varepsilon\mathbf{E}$$
    Substitute this into Gauss's Law:
    $$\nabla \cdot (\varepsilon\mathbf{E}) = \rho_v$$
    Since the medium is homogeneous, $\varepsilon$ is a constant and can be pulled out of the divergence operator:
    $$\varepsilon(\nabla \cdot \mathbf{E}) = \rho_v \implies \nabla \cdot \mathbf{E} = \frac{\rho_v}{\varepsilon}$$
3.  **Relate Electric Field to Potential:**
    In electrostatics, the electric field is conservative, meaning it can be expressed as the negative gradient of a scalar potential $V$:
    $$\mathbf{E} = -\nabla V$$
4.  **Substitute and Finalize:**
    Substitute the gradient expression for $\mathbf{E}$ into the divergence equation:
    $$\nabla \cdot (-\nabla V) = \frac{\rho_v}{\varepsilon}$$
    The divergence of a gradient is known as the Laplacian operator, denoted as $\nabla^2$. Thus:
    $$-\nabla^2 V = \frac{\rho_v}{\varepsilon}$$
    Rearranging yields **Poisson's equation**:
    $$\nabla^2 V = -\frac{\rho_v}{\varepsilon}$$

*(Related location: Textbook Page 225, 327; Slides 195-196)*

***

### c) For the given potential field, $V = \frac{\cos(2\phi)}{\rho}$ in free space, find the volume charge density at point $A(0.5, 60^\circ, 1)$.

To find the volume charge density $\rho_v$ from a potential field $V$ in free space, we use Poisson's equation:
$$\nabla^2 V = -\frac{\rho_v}{\varepsilon_0} \implies \rho_v = -\varepsilon_0 \nabla^2 V$$

**Step 1: Apply the Laplacian operator in cylindrical coordinates.**
The potential $V(\rho, \phi, z) = \frac{\cos(2\phi)}{\rho}$ is given in cylindrical coordinates. The Laplacian operator for a scalar $V$ in cylindrical coordinates is:
$$\nabla^2 V = \frac{1}{\rho}\frac{\partial}{\partial \rho}\left(\rho \frac{\partial V}{\partial \rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 V}{\partial \phi^2} + \frac{\partial^2 V}{\partial z^2}$$

Let's evaluate each term:
*   **Radial term:**
    First, find the first derivative: $\frac{\partial V}{\partial \rho} = \frac{\partial}{\partial \rho} \left( \rho^{-1}\cos(2\phi) \right) = -\rho^{-2}\cos(2\phi)$
    Multiply by $\rho$: $\rho \frac{\partial V}{\partial \rho} = \rho(-\rho^{-2}\cos(2\phi)) = -\rho^{-1}\cos(2\phi)$
    Take the derivative again: $\frac{\partial}{\partial \rho} \left( -\rho^{-1}\cos(2\phi) \right) = \rho^{-2}\cos(2\phi)$
    Multiply by $\frac{1}{\rho}$: $\frac{1}{\rho} \left( \rho^{-2}\cos(2\phi) \right) = \mathbf{\frac{\cos(2\phi)}{\rho^3}}$

*   **Azimuthal term:**
    First derivative: $\frac{\partial V}{\partial \phi} = \frac{\partial}{\partial \phi} \left( \frac{\cos(2\phi)}{\rho} \right) = \frac{-2\sin(2\phi)}{\rho}$
    Second derivative: $\frac{\partial^2 V}{\partial \phi^2} = \frac{\partial}{\partial \phi} \left( \frac{-2\sin(2\phi)}{\rho} \right) = \frac{-4\cos(2\phi)}{\rho}$
    Multiply by $\frac{1}{\rho^2}$: $\frac{1}{\rho^2} \left( \frac{-4\cos(2\phi)}{\rho} \right) = \mathbf{-\frac{4\cos(2\phi)}{\rho^3}}$

*   **Axial term:**
    Since $V$ does not depend on $z$, $\frac{\partial^2 V}{\partial z^2} = \mathbf{0}$

Combine the terms to find the Laplacian:
$$\nabla^2 V = \frac{\cos(2\phi)}{\rho^3} - \frac{4\cos(2\phi)}{\rho^3} + 0 = -\frac{3\cos(2\phi)}{\rho^3}$$

**Step 2: Calculate the volume charge density.**
$$\rho_v = -\varepsilon_0 \left( -\frac{3\cos(2\phi)}{\rho^3} \right) = \frac{3\varepsilon_0\cos(2\phi)}{\rho^3}$$

**Step 3: Evaluate at point A.**
Point A is given as $(\rho, \phi, z) = (0.5, 60^\circ, 1)$.
Substitute $\rho = 0.5$ and $\phi = 60^\circ$:
$$\rho_v = \frac{3\varepsilon_0\cos(2 \cdot 60^\circ)}{(0.5)^3}$$
$$\rho_v = \frac{3\varepsilon_0\cos(120^\circ)}{0.125}$$
Since $\cos(120^\circ) = -0.5$:
$$\rho_v = \frac{3\varepsilon_0(-0.5)}{0.125} = \frac{-1.5\varepsilon_0}{0.125} = -12\varepsilon_0$$

If a numerical value is required, substituting the free space permittivity $\varepsilon_0 \approx 8.854 \times 10^{-12}$ F/m:
$$\rho_v = -12 \times (8.854 \times 10^{-12}) = -1.062 \times 10^{-10} \text{ C/m}^3$$
The volume charge density at point A is **$-12\varepsilon_0 \text{ C/m}^3$** (or **$-106.2 \text{ pC/m}^3$**).

*(Related location: Textbook Page 90, 225)*