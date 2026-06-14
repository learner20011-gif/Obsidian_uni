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

### 🔴 Q.1 (c) What do you understand by the conservative property of potential function? State how Kirchhoff's Voltage Law (K.V.L.) is originated from this property.

**Conservative Property of Potential Function:**
The conservative property of an electrostatic field (and its associated potential function) means that the work done in moving a point charge from one location to another is completely independent of the path taken between the two points. Mathematically, this is expressed by stating that the line integral of the electric field $\mathbf{E}$ around any closed path $L$ is exactly zero:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$$
By applying Stokes's theorem, this integral form converts to the differential form $\nabla \times \mathbf{E} = 0$. Because the curl is zero, the electric field can be expressed as the negative gradient of a scalar potential field ($\mathbf{E} = -\nabla V$). Therefore, the potential difference between two points is uniquely defined and does not rely on the trajectory.

**Origination of Kirchhoff's Voltage Law (K.V.L.):**
Kirchhoff's Voltage Law states that the algebraic sum of the potential differences (voltages) around any closed loop in an electrical circuit is zero ($\sum V = 0$). This is the direct macroscopic, lumped-circuit equivalent of the conservative property of the electrostatic field. Because $\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$, the sum of the voltage drops (where $V = -\int \mathbf{E} \cdot d\mathbf{l}$) across all components in a closed circuit path must identically evaluate to zero, ensuring energy conservation within the circuit.

*(Related location: Textbook Page 147-148, Page 372 (Table 8.4); Slide 108-109)*

***

### 🔴 Q.2 (a) State Gauss's Law in electrostatic with necessary mathematical expression. Using this law obtain the expression of electric fields due to an uniformly charged infinitely charge plane of thin sheet with surface charge density of $\rho_s$ C/m$^2$.

**Gauss's Law:**
Gauss's Law states that the total electric flux ($\Psi$) passing through any closed imaginary surface (a Gaussian surface) is equal to the total net electric charge ($Q_{enc}$) enclosed by that surface.
*   **Integral Form:** $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ (where $\mathbf{D} = \varepsilon_0\mathbf{E}$ is the electric flux density).
*   **Differential (Point) Form:** $\nabla \cdot \mathbf{D} = \rho_v$ (where $\rho_v$ is the volume charge density).

**Electric Field due to an Infinite Sheet of Charge   ( read frm slide):**  ![[Screenshot_20260613_184913_Xodo.jpg]] 
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

### 🔴 Q.3 (a) Explain the boundary conditions for electrostatic and magnetostatic fields.

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

### 🔴 Q.2 a) State potential function and its conservative property.

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
### 1 (a) State Coulomb’s law and obtain the definition of electric field from that law.

**Solution:**

**Coulomb's Law** is an experimental law that deals with the force a point charge exerts on another point charge. It states that the force $F$ between two point charges $Q_1$ and $Q_2$ is:
1.  Along the line joining them.
2.  Directly proportional to the product $Q_1Q_2$ of the charges.
3.  Inversely proportional to the square of the distance $R$ between them.

Expressed mathematically in SI units, the force vector $\mathbf{F}_{12}$ exerted on charge $Q_2$ by charge $Q_1$ is given by:
$$ \mathbf{F}_{12} = \frac{Q_1 Q_2}{4 \pi \varepsilon_0 R^2} \mathbf{a}_{R_{12}} $$
where $R$ is the distance between the charges, $\mathbf{a}_{R_{12}}$ is the unit vector directed from $Q_1$ to $Q_2$, and $\varepsilon_0$ is the permittivity of free space.

**Definition of Electric Field:**
The concept of electric field intensity (or electric field strength) $\mathbf{E}$ is derived directly from Coulomb's law. If we consider $Q_1$ as a source charge generating a field and $Q_2$ as a small positive "test charge" placed in that field, the electric field intensity $\mathbf{E}$ is defined as the force per unit charge experienced by the test charge.

Taking the limit as the test charge $Q$ approaches zero, we obtain:
$$ \mathbf{E} = \lim_{Q \to 0} \frac{\mathbf{F}}{Q} $$
Or, more simply, it is the force per unit charge:
$$ \mathbf{E} = \frac{\mathbf{F}}{Q} $$

Substituting Coulomb's force equation for a point source charge $Q$ acting on a test charge, the electric field intensity at a distance $r$ from the source charge $Q$ is:
$$ \mathbf{E} = \frac{Q}{4 \pi \varepsilon_0 r^2} \mathbf{a}_r $$
where $\mathbf{a}_r$ is the unit vector pointing radially outward from the source charge.

*(Related location: Book Page 137-139 / Presentation Slides Page 34-45)*

***

### 1 (b) Show that the electric field intensity, $\bar{E}$ of an infinitely long, straight line of uniform density, $\rho_l$ coulomb/m varies inversely with distance, $r$ from that conductor.

**Solution:**

To show this relationship, we can apply Gauss's law to an infinitely long, straight line charge with a uniform linear charge density $\rho_l$ (often denoted $\rho_L$). Let the infinitely long line charge lie along the z-axis.

Due to the infinite length and cylindrical symmetry of the line charge, the electric field must point purely in the radial direction outward from the wire and its magnitude can only depend on the radial distance $r$ (or $\rho$ in cylindrical coordinates). Thus, the electric flux density takes the form $\mathbf{D} = D_r \mathbf{a}_r$.

We construct a mathematical closed surface, known as a Gaussian surface, in the shape of a cylinder coaxial with the line charge, having a radius $r$ and an arbitrary length $L$. Gauss's law states that the total outward electric flux through this closed surface is equal to the total charge enclosed:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$

The closed cylindrical surface consists of three parts: the top flat circular face, the bottom flat circular face, and the curved side wall.
1.  On the top and bottom faces, the surface normal $d\mathbf{S}$ points in the $\pm \mathbf{a}_z$ directions, while $\mathbf{D}$ points in the $\mathbf{a}_r$ direction. Since they are perpendicular, $\mathbf{D} \cdot d\mathbf{S} = 0$, meaning no flux passes through the flat ends.
2.  On the curved side wall, the differential area vector is $d\mathbf{S} = r \, d\phi \, dz \, \mathbf{a}_r$. Here, $\mathbf{D}$ and $d\mathbf{S}$ are parallel.

Evaluating the surface integral over the curved surface gives:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_{z=0}^{L} \int_{\phi=0}^{2\pi} (D_r \mathbf{a}_r) \cdot (r \, d\phi \, dz \, \mathbf{a}_r) = D_r r \int_{0}^{L} dz \int_{0}^{2\pi} d\phi = D_r (r)(L)(2\pi) = D_r 2\pi r L $$

The total charge enclosed by this Gaussian cylinder of length $L$ is simply the line charge density multiplied by the length:
$$ Q_{enc} = \rho_l L $$

Equating the two expressions according to Gauss's law:
$$ D_r 2\pi r L = \rho_l L $$
$$ D_r = \frac{\rho_l}{2\pi r} $$

Since $\mathbf{D} = \varepsilon_0 \mathbf{E}$ in free space, the electric field intensity $\mathbf{E}$ is:
$$ \mathbf{E} = \frac{\mathbf{D}}{\varepsilon_0} = \frac{\rho_l}{2\pi \varepsilon_0 r} \mathbf{a}_r $$

As seen from the final expression, $\mathbf{E} \propto \frac{1}{r}$. This explicitly demonstrates that the electric field intensity of an infinitely long, straight line of uniform charge density varies inversely with the distance $r$ from the conductor.

*(Related location: Book Page 145-147, 160 / Presentation Slides Page 56)*

***

### 1 (c) In cylindrical coordinates, let $\rho_v = 0$ for $\rho < 1$ mm, $\rho_v = 2 \sin(2000\pi\rho)$ nC/m$^3$, for $1$ mm $< \rho < 1.5$ mm, and $\rho_v = 0$ for $\rho > 1.5$ mm. Find the electric flux density, $\bar{D}$ everywhere.

**Solution:**

Due to the cylindrical symmetry of the volume charge density $\rho_v$ (it depends only on the radial coordinate $\rho$), the electric flux density will be purely radial: $\mathbf{D} = D_\rho \mathbf{a}_\rho$. We will apply Gauss's law using a coaxial cylindrical Gaussian surface of radius $\rho$ and length $L$:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
$$ D_\rho (2\pi \rho L) = Q_{enc} \implies D_\rho = \frac{Q_{enc}}{2\pi \rho L} $$

We must evaluate this for the three specified regions.

**Region 1: $\rho \le 0.001$ m (1 mm)**
The charge density $\rho_v = 0$ inside this region.
$$ Q_{enc} = \int \rho_v dv = 0 $$
$$ \mathbf{D} = 0 \quad \text{for } \rho \le 1 \text{ mm} $$

**Region 2: $0.001 \text{ m} < \rho \le 0.0015 \text{ m}$ (1 mm to 1.5 mm)**
The enclosed charge within a radius $\rho$ includes the integral of the charge density from the start of the shell ($0.001$ m) up to $\rho$.
$$ Q_{enc} = \int_{v} \rho_v dv = \int_{0}^{L} \int_{0}^{2\pi} \int_{0.001}^{\rho} \left[ 2 \times 10^{-9} \sin(2000\pi \rho') \right] \rho' \, d\rho' \, d\phi \, dz $$
$$ Q_{enc} = (2\pi L)(2 \times 10^{-9}) \int_{0.001}^{\rho} \rho' \sin(2000\pi \rho') \, d\rho' $$
Let $I = \int \rho' \sin(a\rho') \, d\rho'$ where $a = 2000\pi$. Using integration by parts ($\int u \, dv = uv - \int v \, du$ with $u=\rho'$ and $dv=\sin(a\rho')d\rho'$):
$$ I = -\frac{\rho'}{a} \cos(a\rho') + \frac{1}{a^2} \sin(a\rho') $$
Now we evaluate this definite integral from $0.001$ to $\rho$:
At the upper limit ($\rho$):
$$ I_{upper} = -\frac{\rho}{2000\pi} \cos(2000\pi \rho) + \frac{1}{(2000\pi)^2} \sin(2000\pi \rho) $$
At the lower limit ($0.001$):
$$ I_{lower} = -\frac{0.001}{2000\pi} \cos(2000\pi \times 0.001) + \frac{1}{(2000\pi)^2} \sin(2000\pi \times 0.001) $$
$$ I_{lower} = -\frac{10^{-3}}{2000\pi} \cos(2\pi) + \frac{1}{4 \times 10^6 \pi^2} \sin(2\pi) = -\frac{10^{-3}}{2000\pi}(1) + 0 = -\frac{10^{-6}}{2\pi} $$
Subtracting the lower limit from the upper limit gives the integral value:
$$ \int_{0.001}^{\rho} = -\frac{\rho}{2000\pi} \cos(2000\pi \rho) + \frac{1}{4 \times 10^6 \pi^2} \sin(2000\pi \rho) + \frac{10^{-6}}{2\pi} $$
Substitute this back into the $Q_{enc}$ equation:
$$ Q_{enc} = 4\pi L \times 10^{-9} \left[ -\frac{\rho}{2000\pi} \cos(2000\pi \rho) + \frac{1}{4\pi^2 \times 10^6} \sin(2000\pi \rho) + \frac{10^{-6}}{2\pi} \right] $$
$$ Q_{enc} = L \left[ -2 \times 10^{-12} \rho \cos(2000\pi \rho) + \frac{10^{-15}}{\pi} \sin(2000\pi \rho) + 2 \times 10^{-15} \right] $$
Now, divide by $2\pi \rho L$ to find $D_\rho$:
$$ D_\rho = \frac{Q_{enc}}{2\pi \rho L} = \frac{1}{2\pi \rho} \left[ -2 \times 10^{-12} \rho \cos(2000\pi \rho) + \frac{10^{-15}}{\pi} \sin(2000\pi \rho) + 2 \times 10^{-15} \right] $$
$$ \mathbf{D} = \left[ -\frac{10^{-12}}{\pi} \cos(2000\pi \rho) + \frac{10^{-15}}{2\pi^2 \rho} \sin(2000\pi \rho) + \frac{10^{-15}}{\pi \rho} \right] \mathbf{a}_\rho \; (\text{C/m}^2) \quad \text{for } 1 \text{ mm} < \rho \le 1.5 \text{ mm} $$

**Region 3: $\rho > 0.0015$ m (1.5 mm)**
For this region, the Gaussian surface encloses all the charge within the shell. The total enclosed charge per unit length is constant. We evaluate the definite integral from the previous step at the outer boundary $\rho = 0.0015$.
$$ I_{upper\_bound} = -\frac{0.0015}{2000\pi} \cos(2000\pi \times 0.0015) + \frac{1}{4\pi^2 \times 10^6} \sin(2000\pi \times 0.0015) $$
$$ I_{upper\_bound} = -\frac{1.5 \times 10^{-3}}{2000\pi} \cos(3\pi) + \frac{1}{4\pi^2 \times 10^6} \sin(3\pi) = -\frac{1.5 \times 10^{-6}}{2\pi}(-1) + 0 = \frac{1.5 \times 10^{-6}}{2\pi} $$
The value of the definite integral for the entire shell is $I_{upper\_bound} - I_{lower}$:
$$ \int_{0.001}^{0.0015} = \frac{1.5 \times 10^{-6}}{2\pi} - \left( -\frac{10^{-6}}{2\pi} \right) = \frac{2.5 \times 10^{-6}}{2\pi} $$
Calculate total enclosed charge $Q_{enc\_total}$:
$$ Q_{enc\_total} = (4\pi L \times 10^{-9}) \left( \frac{2.5 \times 10^{-6}}{2\pi} \right) = 2L \times 10^{-9} \times 2.5 \times 10^{-6} = 5 \times 10^{-15} L $$
Now, divide by $2\pi \rho L$ to find $D_\rho$:
$$ D_\rho = \frac{Q_{enc\_total}}{2\pi \rho L} = \frac{5 \times 10^{-15} L}{2\pi \rho L} = \frac{2.5 \times 10^{-15}}{\pi \rho} $$
$$ \mathbf{D} = \frac{2.5 \times 10^{-15}}{\pi \rho} \mathbf{a}_\rho \; (\text{C/m}^2) \quad \text{for } \rho > 1.5 \text{ mm} $$

*(Related location: Book Page 160-162 / Presentation Slides Page 142)*

***

### 2 (a) State and explain Gauss's law of electrostatic field. Mention the limitation of using Gauss's law in determining the electric field for an arbitrary charge distribution.

**Solution:**

**Gauss's Law:**
Gauss’s law states that the total electric flux ($\Psi$) passing through any mathematical closed surface is equal to the total net electric charge ($Q_{enc}$) enclosed by that surface. 

In its integral form, it is expressed mathematically as:
$$ \Psi = \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
where $\mathbf{D}$ is the electric flux density vector, and $d\mathbf{S}$ is the differential area vector directed normally outward from the closed surface $S$.

**Explanation:**
Gauss's law is a fundamental principle of electromagnetism and serves as an alternative statement to Coulomb's law. It relates the behavior of the electric flux density field over a defined boundary (a hypothetical "Gaussian surface") to the sources of the field (charges) residing within that boundary. If there is a net positive charge inside the closed volume, there is a net outward flow of electric flux. If there is no net charge, the flux entering the surface exactly equals the flux leaving it.

**Limitations:**
While Gauss's law is a universal physical law that *always* holds true for any closed surface and any charge distribution, its practical utility as a tool for determining the electric field ($\mathbf{E}$ or $\mathbf{D}$) is severely limited unless the charge distribution exhibits a high degree of spatial symmetry. 

To solve for $\mathbf{D}$ using Gauss's law, one must be able to define a Gaussian surface where the magnitude of $\mathbf{D}$ is constant everywhere on the surface, and $\mathbf{D}$ is everywhere either entirely perpendicular or purely tangential to the surface. This allows $\mathbf{D}$ to be factored out of the integral ($\oint_S \mathbf{D} \cdot d\mathbf{S} = D \oint_S dS$). This is only possible for highly symmetrical charge configurations, such as point charges, infinite lines, infinite cylinders, or perfect spheres. For an arbitrary, non-symmetric charge distribution, finding such a surface is impossible, meaning the integral cannot be algebraically manipulated to solve for the field vector. In those cases, one must resort to applying Coulomb's law directly via integration or solving Poisson's or Laplace's equations.

*(Related location: Book Page 157-159 / Presentation Slides Page 186)*

***

### 2 (b) Explain the effect of electric field on a conducting material in brief.

**Solution:**

A conducting material is characterized by an abundance of free electrons in its outermost atomic shells that are not tightly bound to any specific atom and can move freely throughout the material's lattice.

When an isolated conducting material is placed in an external electrostatic field ($\mathbf{E}_e$), the field exerts a force ($\mathbf{F} = Q\mathbf{E}$) on these mobile charges. Because the electrons are free to move, the negative charges (electrons) are rapidly pushed in the direction opposite to the applied field, while positive charges (holes/ions left behind) are effectively pushed in the same direction as the field. 

This extremely rapid charge migration causes the free charges to accumulate on the exterior surface of the conductor, forming an induced surface charge. These newly separated surface charges establish their own internal induced electric field ($\mathbf{E}_i$) that opposes the externally applied field $\mathbf{E}_e$.

The charges will continue to redistribute themselves on the surface until the internal induced field exactly cancels the external applied field everywhere inside the conductor. Once this state of electrostatic equilibrium is reached (which happens almost instantaneously):
1.  The net electric field inside the perfect conductor is exactly zero ($\mathbf{E} = 0$).
2.  The volume charge density inside the conductor is zero ($\rho_v = 0$); all net charge resides exclusively on the exterior surface.
3.  Because the electric field is zero inside, no work is done moving a charge between any two points within the conductor, making the entire conductor an equipotential body (voltage is uniform throughout).

*(Related location: Book Page 206 / Presentation Slides Page 156-159)*

***

### 2 (c) A positive point charge Q is placed at the center of a spherical dielectric shell of an inner radius $r_i$ and an outer radius $r_o$. The dielectric constant of shell is $\varepsilon_r$. Determine E and P as functions of radial position.

**Solution:**

Due to the spherical symmetry of the problem (a point charge at the origin surrounded by concentric spherical shells), the electric flux density $\mathbf{D}$ will be purely radial and will depend only on the radial distance $r$. Thus, $\mathbf{D} = D_r \mathbf{a}_r$.

We can apply Gauss's law using a spherical Gaussian surface of radius $r$ centered at the origin:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
$$ D_r (4\pi r^2) = Q \implies \mathbf{D} = \frac{Q}{4\pi r^2} \mathbf{a}_r $$
Notice that this equation for $\mathbf{D}$ depends only on the enclosed free charge $Q$ and is entirely independent of the dielectric material properties. Therefore, this expression for $\mathbf{D}$ is valid everywhere ($r > 0$).

Now, we determine the electric field intensity $\mathbf{E} = \mathbf{D}/\varepsilon$ and the polarization vector $\mathbf{P} = \mathbf{D} - \varepsilon_0 \mathbf{E}$ for the three distinct regions:

**Region 1: $0 < r < r_i$ (The inner empty cavity)**
This region is free space, so the permittivity is $\varepsilon = \varepsilon_0$.
$$ \mathbf{E} = \frac{\mathbf{D}}{\varepsilon_0} = \frac{Q}{4\pi \varepsilon_0 r^2} \mathbf{a}_r $$
Because there is no dielectric material in this region to polarize, the polarization vector is zero:
$$ \mathbf{P} = 0 $$

**Region 2: $r_i \le r \le r_o$ (Inside the dielectric shell)**
This region is filled with the dielectric material, so the permittivity is $\varepsilon = \varepsilon_0 \varepsilon_r$.
$$ \mathbf{E} = \frac{\mathbf{D}}{\varepsilon_0 \varepsilon_r} = \frac{Q}{4\pi \varepsilon_0 \varepsilon_r r^2} \mathbf{a}_r $$
The polarization vector $\mathbf{P}$ is the difference between the actual flux density and the flux density that would exist in free space for that $\mathbf{E}$ field:
$$ \mathbf{P} = \mathbf{D} - \varepsilon_0 \mathbf{E} = \frac{Q}{4\pi r^2} \mathbf{a}_r - \varepsilon_0 \left( \frac{Q}{4\pi \varepsilon_0 \varepsilon_r r^2} \mathbf{a}_r \right) $$
$$ \mathbf{P} = \frac{Q}{4\pi r^2} \mathbf{a}_r - \frac{Q}{4\pi \varepsilon_r r^2} \mathbf{a}_r = \frac{Q}{4\pi r^2} \left( 1 - \frac{1}{\varepsilon_r} \right) \mathbf{a}_r = \frac{Q(\varepsilon_r - 1)}{4\pi \varepsilon_r r^2} \mathbf{a}_r $$

**Region 3: $r > r_o$ (The outer free space region)**
This region is again free space, so the permittivity is $\varepsilon = \varepsilon_0$.
$$ \mathbf{E} = \frac{\mathbf{D}}{\varepsilon_0} = \frac{Q}{4\pi \varepsilon_0 r^2} \mathbf{a}_r $$
Similar to the inner cavity, there is no dielectric material here to polarize:
$$ \mathbf{P} = 0 $$

*(Related location: Book Page 162, 190, 219)*
### 3 (a) Derive the expression of the point form of continuity equation. Explain the physical meaning of that equation.

**Solution:**

**Derivation:**
The continuity equation is derived from the fundamental principle of conservation of charge, which states that charge can neither be created nor destroyed. 

Consider a given closed volume $v$ bounded by a surface $S$. If there is a net outward flow of positive charge (current) from this volume, there must be a corresponding decrease in the total charge $Q_{in}$ residing within the volume.

The total current $I_{out}$ leaving the closed surface $S$ is given by the closed surface integral of the current density $\mathbf{J}$:
$$ I_{out} = \oint_S \mathbf{J} \cdot d\mathbf{S} $$

According to the principle of conservation of charge, this outward current must equal the time rate of decrease of the enclosed charge $Q_{in}$:
$$ I_{out} = -\frac{dQ_{in}}{dt} $$

Equating the two expressions for $I_{out}$:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{dQ_{in}}{dt} $$

The total enclosed charge $Q_{in}$ can be expressed as the volume integral of the volume charge density $\rho_v$:
$$ Q_{in} = \int_v \rho_v \, dv $$

Substituting this into the conservation equation gives the integral form of the continuity equation:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{d}{dt} \int_v \rho_v \, dv $$

If we assume the volume $v$ is stationary (does not change its shape or size with time), we can move the time derivative inside the integral as a partial derivative:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = \int_v \left(-\frac{\partial \rho_v}{\partial t}\right) dv $$

Now, we apply the Divergence Theorem to the left side of the equation, which transforms the closed surface integral into a volume integral:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{J}) dv $$

Equating the two volume integrals:
$$ \int_v (\nabla \cdot \mathbf{J}) dv = \int_v \left(-\frac{\partial \rho_v}{\partial t}\right) dv $$

For this equality to hold true for *any* arbitrary volume $v$, the integrands must be identically equal. This yields the point form (or differential form) of the continuity equation:
$$ \nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t} $$

**Physical Meaning:**
The point form of the continuity equation ($\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$) provides a localized view of charge conservation. It states that the divergence of the current density vector $\mathbf{J}$ at any specific point in space is exactly equal to the rate of decrease of the volume charge density $\rho_v$ at that same point. 
*   If $\nabla \cdot \mathbf{J} > 0$ (current is diverging or flowing away from the point), then $\frac{\partial \rho_v}{\partial t} < 0$, meaning the charge density there is decreasing.
*   For steady (time-invariant) currents, charges do not accumulate or deplete at any point, meaning $\frac{\partial \rho_v}{\partial t} = 0$. In this case, the equation simplifies to $\nabla \cdot \mathbf{J} = 0$, indicating that the current entering a point exactly equals the current leaving it (Kirchhoff's Current Law).

*(Related location: Book Page 221 / Presentation Slides Page 140-144)*

***

### 3 (b) Explain the method of Image theory of electrostatic field.

**Solution:**

The Method of Images is a powerful analytical technique used in electrostatics to solve problems involving charges located near perfectly conducting boundaries (like infinite planes or spheres). Direct application of Poisson's or Laplace's equations in such scenarios can be highly complex due to the unknown induced charge distributions on the conductor surfaces.

**The core principle of Image Theory states that:**
A given charge configuration situated above an infinite, grounded, perfectly conducting plane can be entirely replaced by the original charge configuration itself, a fictitious "image" charge configuration, and an equipotential surface placed exactly where the conducting plane used to be.

**How it works:**
1.  **Remove the Conductor:** The physical conducting boundary is conceptually removed from the problem space.
2.  **Place the Image Charge:** An image charge (or set of charges) is placed in the region that was previously occupied by the conductor. 
3.  **Satisfy Boundary Conditions:** The magnitude, sign, and location of the image charge(s) must be chosen carefully to ensure that the boundary conditions of the original problem are perfectly satisfied. Specifically, the potential $V$ must evaluate to zero (or a specified constant value) everywhere along the geometrical plane where the conductor surface originally existed.
4.  **Calculate Fields:** Once the correct image configuration is established, the electric potential $V$, electric field $\mathbf{E}$, and flux density $\mathbf{D}$ in the valid region (the side where the original charges reside) can be calculated using the principle of superposition, treating both the original charges and the image charges as if they exist in unbounded free space.

**Classic Example:**
Consider a positive point charge $+Q$ located at a height $h$ above an infinite grounded conducting plane (lying in the $z=0$ plane). 
*   By Image Theory, we remove the plane and place a negative image charge $-Q$ at a depth $h$ below the $z=0$ plane (i.e., at $z=-h$). 
*   This arrangement ($+Q$ at $+h$, $-Q$ at $-h$) naturally creates an equipotential surface of $V=0$ exactly along the mid-plane $z=0$, perfectly mimicking the boundary condition enforced by the grounded conductor. 
*   The electric field in the upper half-space ($z > 0$) is then simply the vector sum of the fields produced by $+Q$ and $-Q$ in free space. 

It is crucial to note that the image method only provides valid field solutions in the region where the original charges are located. The fields inside the region of the assumed image charges (inside the conductor) remain strictly zero.

*(Related location: Book Page 266-267 / Presentation Slides Page 167-170)*

***

### 3 (c) For a dielectric material in an electric filed, show that $\bar{D} = \varepsilon_o\bar{E} + \bar{P}$, where the symbols have their usual meanings.

**Solution:**

When a dielectric material is placed in an external electric field, it becomes polarized. This polarization results in the creation of bound charges within the material. Therefore, in a generalized region containing a dielectric, there can be two types of charges:
1.  **Free charge ($\rho_v$):** Charges that are free to move, such as electrons in a conductor or charges explicitly placed in space.
2.  **Bound (or polarization) charge ($\rho_{pv}$):** Charges that are bound to atoms/molecules but have been slightly displaced due to the applied electric field.

The total volume charge density ($\rho_t$) in the region is the sum of both:
$$ \rho_t = \rho_v + \rho_{pv} $$

From fundamental electrostatics in free space, Gauss's law in point form relates the divergence of the electric field to the *total* charge density driving it:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_t $$
Substituting the expression for total charge:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_v + \rho_{pv} $$

We know from the theory of polarization that the bound volume charge density $\rho_{pv}$ is mathematically related to the polarization vector $\mathbf{P}$ (which is the dipole moment per unit volume) by the negative divergence of $\mathbf{P}$:
$$ \rho_{pv} = -\nabla \cdot \mathbf{P} $$

Substitute this relation for bound charge back into the modified Gauss's law equation:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_v - \nabla \cdot \mathbf{P} $$

Rearrange the terms to group the divergence operators on one side and the free charge on the other:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) + \nabla \cdot \mathbf{P} = \rho_v $$
Since the divergence operator is linear, we can combine the terms:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E} + \mathbf{P}) = \rho_v $$

We define a new macroscopic vector field, the **Electric Flux Density ($\mathbf{D}$)**, such that its divergence is equal strictly to the *free* volume charge density $\rho_v$. This allows us to write Gauss's law in a generalized medium as:
$$ \nabla \cdot \mathbf{D} = \rho_v $$

By comparing the two equations ($\nabla \cdot (\varepsilon_0 \mathbf{E} + \mathbf{P}) = \rho_v$ and $\nabla \cdot \mathbf{D} = \rho_v$), we can clearly define the relationship between the fields:
$$ \mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} $$
This equation fundamentally shows that the electric flux density $\mathbf{D}$ inside a dielectric depends on both the free space electric field component ($\varepsilon_0 \mathbf{E}$) and the contribution from the polarized material itself ($\mathbf{P}$).

*(Related location: Book Page 215 / Presentation Slides Page 187-188)*

***

### 4 (a) Define potential difference between two points in electric field and hence derive its equation in terms of the electric field.

**Solution:**

**Definition:**
The **potential difference** ($V_{AB}$) between two points A and B in an electric field is defined as the work done (by an external agent) per unit positive charge in moving a test charge from point A (the initial point) to point B (the final point) against the electric field. It represents the change in potential energy per unit charge.

**Derivation:**
Suppose we wish to move a test point charge $Q$ from point A to point B within an electric field $\mathbf{E}$. 

According to Coulomb's law, the electric field exerts a force on the charge given by:
$$ \mathbf{F}_E = Q\mathbf{E} $$

To move the charge uniformly (without acceleration) from A to B, an external agent must apply a force $\mathbf{F}_{appl}$ that is exactly equal and opposite to the electric force:
$$ \mathbf{F}_{appl} = -\mathbf{F}_E = -Q\mathbf{E} $$

The differential work $dW$ done by this external agent in moving the charge over an infinitesimal vector distance $d\mathbf{l}$ is the dot product of the applied force and the displacement:
$$ dW = \mathbf{F}_{appl} \cdot d\mathbf{l} = -Q\mathbf{E} \cdot d\mathbf{l} $$

To find the total work $W$ required to move the charge from the initial point A to the final point B, we integrate the differential work along the path of movement:
$$ W = \int_A^B dW = -Q \int_A^B \mathbf{E} \cdot d\mathbf{l} $$

By definition, the potential difference $V_{AB}$ is the total work done divided by the magnitude of the charge $Q$:
$$ V_{AB} = \frac{W}{Q} $$

Substituting the expression for $W$ into this definition yields the equation for potential difference in terms of the electric field:
$$ V_{AB} = -\int_A^B \mathbf{E} \cdot d\mathbf{l} $$

This equation shows that the potential difference $V_{AB}$ (which is equal to $V_B - V_A$) is the negative line integral of the electric field intensity from point A to point B.

*(Related location: Book Page 166-167 / Presentation Slides Page 74-76, 88)*

***

### 4 (b) What do you mean by equipotential surface? Show that the field lines are always perpendicular to equipotential surface.

**Solution:**

**Definition of Equipotential Surface:**
An equipotential surface is an imaginary three-dimensional surface in space on which the electric potential $V$ is identical at every point. Because the potential is constant across the entire surface, no work is required to move a charge from any one point to any other point lying on that same surface.

**Proof that field lines are perpendicular to equipotential surfaces:**
Consider an arbitrary equipotential surface where the potential is $V = \text{constant}$.
Let us take two points, A and B, that lie anywhere on this same surface.
Because the surface is equipotential, the potential difference between point A and point B is zero:
$$ V_{AB} = V_B - V_A = 0 $$

We know from the definition of potential difference that the work done per unit charge moving from A to B is the line integral of the electric field:
$$ V_{AB} = -\int_A^B \mathbf{E} \cdot d\mathbf{l} = 0 $$

Now, let's consider an infinitesimally small displacement $d\mathbf{l}$ exclusively *along* the surface. For this differential movement, the change in potential $dV$ is zero:
$$ dV = -\mathbf{E} \cdot d\mathbf{l} = 0 $$

The dot product of two vectors is defined as $\mathbf{E} \cdot d\mathbf{l} = |\mathbf{E}| |d\mathbf{l}| \cos\theta$, where $\theta$ is the angle between the electric field vector $\mathbf{E}$ and the displacement vector $d\mathbf{l}$.
Since neither the electric field $\mathbf{E}$ (assuming we are not in a field-free region) nor the displacement $d\mathbf{l}$ is zero, their dot product can only be zero if:
$$ \cos\theta = 0 $$
This implies that:
$$ \theta = 90^\circ $$

Because $d\mathbf{l}$ represents any arbitrary tangent vector along the equipotential surface, the electric field vector $\mathbf{E}$ must be perpendicular (orthogonal) to every tangent on the surface. Therefore, electric field lines (lines of force) always intersect equipotential surfaces at right angles ($90^\circ$).

*(Related location: Book Page 177 / Presentation Slides Page 98)*

***

### 4 (c) An electric dipole of dipole moment $p = qd \mathbf{a}_z$ is centered at the coordinate origin. Determine electric field at $P (0, 0, z >> d)$.

**Solution:**

The electric field intensity $\mathbf{E}$ of a z-directed electric dipole centered at the origin in spherical coordinates $(r, \theta, \phi)$ is given by the standard dipole formula:
$$ \mathbf{E} = \frac{p}{4 \pi \varepsilon_0 r^3} (2 \cos\theta \mathbf{a}_r + \sin\theta \mathbf{a}_\theta) $$
where $p$ is the magnitude of the dipole moment ($p = qd$).

We are asked to find the electric field at point $P(0, 0, z)$, with the condition that $z \gg d$ (meaning the observation point is in the "far-field" relative to the dipole separation, validating the use of the ideal dipole formula above).

First, we must convert the coordinates of the observation point $P(0, 0, z)$ from Cartesian to spherical coordinates to plug them into the dipole equation.
Assuming the point $P$ lies on the positive z-axis ($z > 0$):
*   Radial distance $r$: The distance from the origin to the point is simply $r = z$.
*   Polar angle $\theta$: The angle measured from the positive z-axis to the point on the positive z-axis is $\theta = 0^\circ$.

Now, we substitute $r = z$ and $\theta = 0^\circ$ into the electric field equation:
$$ \mathbf{E} = \frac{p}{4 \pi \varepsilon_0 z^3} (2 \cos(0^\circ) \mathbf{a}_r + \sin(0^\circ) \mathbf{a}_\theta) $$

We know that $\cos(0^\circ) = 1$ and $\sin(0^\circ) = 0$. Furthermore, exactly on the positive z-axis, the radial unit vector $\mathbf{a}_r$ points straight up, making it identical to the Cartesian unit vector $\mathbf{a}_z$ ($\mathbf{a}_r = \mathbf{a}_z$).

Substituting these values:
$$ \mathbf{E} = \frac{p}{4 \pi \varepsilon_0 z^3} (2(1) \mathbf{a}_z + (0) \mathbf{a}_\theta) $$
$$ \mathbf{E} = \frac{2p}{4 \pi \varepsilon_0 z^3} \mathbf{a}_z $$
$$ \mathbf{E} = \frac{p}{2 \pi \varepsilon_0 z^3} \mathbf{a}_z $$

Since the problem defines the dipole moment vector as $\mathbf{p} = qd \mathbf{a}_z$ and its magnitude as $p = qd$, we can substitute $p = qd$ into the expression:
$$ \mathbf{E} = \frac{qd}{2 \pi \varepsilon_0 z^3} \mathbf{a}_z $$

This is the electric field intensity at point $P$ on the z-axis far from the dipole.

*(Related location: Book Page 175-177 / Presentation Slides Page 116-118)*
### 🔴 Q.1 (a) State Coulomb's law and the constraints for it, from this law define electric field intensity, E. Write some applications of electrostatics.

**Solution:**

**Coulomb's Law Statement:**
Coulomb's law states that the electrostatic force $F$ between two point charges $Q_1$ and $Q_2$ is:
1.  Directed along the straight line joining the two charges.
2.  Directly proportional to the product of the magnitudes of the charges ($Q_1Q_2$).
3.  Inversely proportional to the square of the distance $R$ between them.

Mathematically, the force vector $\mathbf{F}_{12}$ exerted on charge $Q_2$ by charge $Q_1$ is expressed as:
$$ \mathbf{F}_{12} = \frac{Q_1 Q_2}{4 \pi \varepsilon_0 R^2} \mathbf{a}_{R_{12}} $$
where $\mathbf{a}_{R_{12}}$ is the unit vector directed from $Q_1$ to $Q_2$, and $\varepsilon_0$ is the permittivity of free space.

**Constraints for Coulomb's Law:**
1.  **Point Charges:** The distance $R$ between the charged bodies must be very large compared to the linear dimensions of the bodies themselves. In other words, $Q_1$ and $Q_2$ must be considered point charges.
2.  **Static State:** The charges $Q_1$ and $Q_2$ must be static (at rest). If they are moving, magnetic forces also come into play.
3.  **Sign Consideration:** The algebraic signs of $Q_1$ and $Q_2$ must be taken into account. Like charges (same sign) produce a repulsive force, while unlike charges (opposite signs) produce an attractive force.

**Definition of Electric Field Intensity ($\mathbf{E}$):**
From Coulomb's law, we can define the electric field intensity (or electric field strength) $\mathbf{E}$ as the force per unit positive test charge when placed in an electric field. 
If we place a small test charge $Q$ in the presence of an electric field generated by other sources, the field $\mathbf{E}$ is:
$$ \mathbf{E} = \lim_{Q \to 0} \frac{\mathbf{F}}{Q} $$
Or simply:
$$ \mathbf{E} = \frac{\mathbf{F}}{Q} $$
For a single point source charge $Q$ at the origin, the electric field intensity at a radial distance $r$ is derived directly from Coulomb's law as:
$$ \mathbf{E} = \frac{Q}{4 \pi \varepsilon_0 r^2} \mathbf{a}_r $$

**Applications of Electrostatics:**
Electrostatic principles are utilized in various diverse fields and devices, including:
*   **Solid-state electronics:** Resistors, capacitors, and active devices like bipolar and field-effect transistors.
*   **Computer peripherals:** Capacitance keyboards, touch pads, cathode-ray tubes (CRTs), liquid crystal displays (LCDs), and electrostatic printers.
*   **Medical equipment:** X-ray machines, electrocardiograms (ECGs), and electroencephalograms (EEGs).
*   **Industrial applications:** Paint spraying, electrodeposition, electrochemical machining, separation of fine particles (electrostatic precipitators).
*   **Other areas:** Lightning protection systems, agriculture (sorting seeds, measuring crop moisture), and electric power transmission.

*(Related location: Book Page 136-139 / PDF Page 136-139)*

***

### 🔴 Q.1 (b) Explain Gauss's law along with its salient features and limitations.

**Solution:**

**Gauss's Law:**
Gauss's law constitutes one of the fundamental laws of electromagnetism (and is one of Maxwell's equations). It states that the total electric flux ($\Psi$) passing through any hypothetical closed surface (known as a Gaussian surface) is exactly equal to the total net electric charge ($Q_{enc}$) enclosed by that surface.

In integral form, it is expressed as:
$$ \Psi = \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} = \int_v \rho_v \, dv $$
where $\mathbf{D}$ is the electric flux density vector, $d\mathbf{S}$ is the differential surface area vector (directed normally outward), and $\rho_v$ is the volume charge density.

In differential (point) form, Gauss's law is written as:
$$ \nabla \cdot \mathbf{D} = \rho_v $$

**Salient Features:**
1.  **Alternative to Coulomb's Law:** Gauss's law is an alternative mathematical statement of Coulomb's law. Proper application of the divergence theorem to Coulomb's law results directly in Gauss's law.
2.  **Source Equation:** The differential form ($\nabla \cdot \mathbf{D} = \rho_v$) is considered a "source equation" because it directly links the divergence of the flux lines at a point to the charge density (the source) existing at that precise point.
3.  **Independence of Outside Charges:** The net flux crossing the closed surface depends *only* on the charge enclosed within it. Charges located outside the Gaussian surface do not contribute to the *net* flux (what enters must exit).

**Limitations:**
While Gauss's law is universally true for any closed surface and any charge distribution, its practical utility as a mathematical tool for calculating electric fields ($\mathbf{E}$ or $\mathbf{D}$) is severely limited. 
It is only useful when the charge distribution exhibits a high degree of spatial symmetry (such as spherical, cylindrical, or planar symmetry). To extract $\mathbf{D}$ from the integral $\oint \mathbf{D} \cdot d\mathbf{S}$, one must be able to define a Gaussian surface where $\mathbf{D}$ is constant in magnitude and is everywhere either completely normal or completely tangential to the surface. If the charge distribution is arbitrary or non-symmetric, such a surface cannot be found, and one must resort to using Coulomb's law via integration to find the field.

*(Related location: Book Page 157-159 / PDF Page 157-159)*

***

### Q.1 (c) A point charge $Q_1 = 25\text{nC}$ be located at $P_1 (4, -2, 7)$ and a charge $Q_2 = 60\text{nC}$ be at $P_2 (-3, 4, -2)$. (i) Find $\mathbf{E}$ at $P_3 (1, 2, 3)$ if $\varepsilon = \varepsilon_0$ ; (ii) at what point on the y-axis is $E_x = 0$?

**Solution:**

**Part (i): Find $\mathbf{E}$ at $P_3 (1, 2, 3)$**

The total electric field at point $P_3$ is the vector sum of the fields produced by $Q_1$ and $Q_2$:
$$ \mathbf{E}_3 = \mathbf{E}_{13} + \mathbf{E}_{23} = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q_1 (\mathbf{r}_3 - \mathbf{r}_1)}{|\mathbf{r}_3 - \mathbf{r}_1|^3} + \frac{Q_2 (\mathbf{r}_3 - \mathbf{r}_2)}{|\mathbf{r}_3 - \mathbf{r}_2|^3} \right] $$

Let $\frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9 \text{ m/F}$.

1.  **For Charge $Q_1$:**
    *   Distance vector: $\mathbf{r}_3 - \mathbf{r}_1 = (1 - 4)\mathbf{a}_x + (2 - (-2))\mathbf{a}_y + (3 - 7)\mathbf{a}_z = -3\mathbf{a}_x + 4\mathbf{a}_y - 4\mathbf{a}_z$
    *   Magnitude cubed: $|\mathbf{r}_3 - \mathbf{r}_1|^3 = \left(\sqrt{(-3)^2 + 4^2 + (-4)^2}\right)^3 = (\sqrt{9 + 16 + 16})^3 = (\sqrt{41})^3 = 41\sqrt{41} \approx 262.53$

2.  **For Charge $Q_2$:**
    *   Distance vector: $\mathbf{r}_3 - \mathbf{r}_2 = (1 - (-3))\mathbf{a}_x + (2 - 4)\mathbf{a}_y + (3 - (-2))\mathbf{a}_z = 4\mathbf{a}_x - 2\mathbf{a}_y + 5\mathbf{a}_z$
    *   Magnitude cubed: $|\mathbf{r}_3 - \mathbf{r}_2|^3 = \left(\sqrt{4^2 + (-2)^2 + 5^2}\right)^3 = (\sqrt{16 + 4 + 25})^3 = (\sqrt{45})^3 = 45\sqrt{45} \approx 301.87$

Now substitute into the superposition equation:
$$ \mathbf{E}_3 = 9 \times 10^9 \left[ \frac{25 \times 10^{-9}}{262.53} (-3\mathbf{a}_x + 4\mathbf{a}_y - 4\mathbf{a}_z) + \frac{60 \times 10^{-9}}{301.87} (4\mathbf{a}_x - 2\mathbf{a}_y + 5\mathbf{a}_z) \right] $$
$$ \mathbf{E}_3 = 9 \left[ 0.0952 (-3\mathbf{a}_x + 4\mathbf{a}_y - 4\mathbf{a}_z) + 0.1988 (4\mathbf{a}_x - 2\mathbf{a}_y + 5\mathbf{a}_z) \right] $$
$$ \mathbf{E}_3 = 9 \left[ (-0.2856\mathbf{a}_x + 0.3808\mathbf{a}_y - 0.3808\mathbf{a}_z) + (0.7952\mathbf{a}_x - 0.3976\mathbf{a}_y + 0.9940\mathbf{a}_z) \right] $$
$$ \mathbf{E}_3 = 9 \left[ 0.5096\mathbf{a}_x - 0.0168\mathbf{a}_y + 0.6132\mathbf{a}_z \right] $$
$$ \mathbf{E}_3 \approx 4.586\mathbf{a}_x - 0.151\mathbf{a}_y + 5.519\mathbf{a}_z \text{ V/m} $$

**Part (ii): At what point on the y-axis is $E_x = 0$?**

Let an arbitrary point on the y-axis be $P_y(0, y, 0)$. The x-component of the total electric field at this point is the sum of the x-components of the fields from $Q_1$ and $Q_2$:
$$ E_{x,total} = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q_1 (0 - x_1)}{|\mathbf{r}_y - \mathbf{r}_1|^3} + \frac{Q_2 (0 - x_2)}{|\mathbf{r}_y - \mathbf{r}_2|^3} \right] = 0 $$

1.  **For $Q_1$ at $(4, -2, 7)$:**
    *   Distance vector to y-axis: $\mathbf{r}_y - \mathbf{r}_1 = -4\mathbf{a}_x + (y + 2)\mathbf{a}_y - 7\mathbf{a}_z$
    *   Magnitude cubed: $|\mathbf{r}_y - \mathbf{r}_1|^3 = [(-4)^2 + (y+2)^2 + (-7)^2]^{3/2} = [(y+2)^2 + 65]^{3/2}$
    *   x-component of vector: $-4$

2.  **For $Q_2$ at $(-3, 4, -2)$:**
    *   Distance vector to y-axis: $\mathbf{r}_y - \mathbf{r}_2 = 3\mathbf{a}_x + (y - 4)\mathbf{a}_y + 2\mathbf{a}_z$
    *   Magnitude cubed: $|\mathbf{r}_y - \mathbf{r}_2|^3 = [3^2 + (y-4)^2 + 2^2]^{3/2} = [(y-4)^2 + 13]^{3/2}$
    *   x-component of vector: $3$

Set the sum of the x-components to zero:
$$ \frac{25 (-4)}{[(y+2)^2 + 65]^{3/2}} + \frac{60 (3)}{[(y-4)^2 + 13]^{3/2}} = 0 $$
$$ \frac{-100}{[(y+2)^2 + 65]^{3/2}} + \frac{180}{[(y-4)^2 + 13]^{3/2}} = 0 $$
$$ \frac{100}{[(y+2)^2 + 65]^{3/2}} = \frac{180}{[(y-4)^2 + 13]^{3/2}} $$
$$ \frac{[(y+2)^2 + 65]^{3/2}}{[(y-4)^2 + 13]^{3/2}} = \frac{100}{180} = \frac{5}{9} $$

Raise both sides to the power of $2/3$:
$$ \frac{(y+2)^2 + 65}{(y-4)^2 + 13} = \left(\frac{5}{9}\right)^{2/3} \approx 0.6754 $$

Cross-multiply and expand the terms:
$$ (y^2 + 4y + 4) + 65 = 0.6754 \left[ (y^2 - 8y + 16) + 13 \right] $$
$$ y^2 + 4y + 69 = 0.6754 (y^2 - 8y + 29) $$
$$ y^2 + 4y + 69 = 0.6754y^2 - 5.4032y + 19.5866 $$

Bring all terms to one side to form a quadratic equation $ay^2 + by + c = 0$:
$$ (1 - 0.6754)y^2 + (4 + 5.4032)y + (69 - 19.5866) = 0 $$
$$ 0.3246y^2 + 9.4032y + 49.4134 = 0 $$

Solve for $y$ using the quadratic formula:
$$ y = \frac{-9.4032 \pm \sqrt{(9.4032)^2 - 4(0.3246)(49.4134)}}{2(0.3246)} $$
$$ y = \frac{-9.4032 \pm \sqrt{88.42 - 64.158}}{0.6492} = \frac{-9.4032 \pm \sqrt{24.262}}{0.6492} $$
$$ y = \frac{-9.4032 \pm 4.9256}{0.6492} $$
Solving for the two possible values of $y$:
$$ y_1 = \frac{-4.4776}{0.6492} \approx -6.897 $$
$$ y_2 = \frac{-14.3288}{0.6492} \approx -22.07 $$

Therefore, $E_x = 0$ at the points on the y-axis approximately located at **$(0, -6.897, 0)$** and **$(0, -22.07, 0)$**.

*(Related location: Book Page 140 / PDF Page 140)*

***

### Q.2 (a) Show that the electric field intensity of an infinitely long, straight line charge of uniform density varies inversely with the radial distance from the line where the charge is located.

**Solution:**

Consider an infinitely long, straight line carrying a uniform line charge density $\rho_L$ (C/m). Let this line lie along the z-axis. We want to find the electric field intensity $\mathbf{E}$ at a point $P$, located at a radial distance $\rho$ from the line.

We will use Gauss's law, which states that the total outward flux over a closed surface equals the enclosed charge:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$

Due to the infinite length and cylindrical symmetry of the line charge, the electric flux density $\mathbf{D}$ must be purely radial (pointing directly away from the line) and constant in magnitude at a fixed distance $\rho$. Therefore, $\mathbf{D} = D_\rho \mathbf{a}_\rho$.

We construct a cylindrical Gaussian surface of radius $\rho$ and length $L$, coaxial with the line charge. The closed surface integral is evaluated over three parts: the top flat face, the bottom flat face, and the curved cylindrical wall.
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_{top} \mathbf{D} \cdot d\mathbf{S} + \int_{bottom} \mathbf{D} \cdot d\mathbf{S} + \int_{curved} \mathbf{D} \cdot d\mathbf{S} $$

1.  On the **top and bottom faces**, the differential surface area vectors $d\mathbf{S}$ point in the $\mathbf{a}_z$ and $-\mathbf{a}_z$ directions, respectively. Since $\mathbf{D}$ is in the $\mathbf{a}_\rho$ direction, the dot product $\mathbf{D} \cdot d\mathbf{S} = 0$. No flux passes through the ends.
2.  On the **curved surface**, $d\mathbf{S} = \rho \, d\phi \, dz \, \mathbf{a}_\rho$. The vectors $\mathbf{D}$ and $d\mathbf{S}$ are parallel.

Evaluating the integral for the curved surface:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_{z=0}^{L} \int_{\phi=0}^{2\pi} (D_\rho \mathbf{a}_\rho) \cdot (\rho \, d\phi \, dz \, \mathbf{a}_\rho) = D_\rho \rho \int_{0}^{2\pi} d\phi \int_{0}^{L} dz $$
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = D_\rho \rho (2\pi) (L) = 2\pi \rho L D_\rho $$

The total charge enclosed by this Gaussian cylinder of length $L$ is simply the line charge density times the length:
$$ Q_{enc} = \rho_L L $$

Equating the two expressions according to Gauss's law:
$$ 2\pi \rho L D_\rho = \rho_L L $$
$$ D_\rho = \frac{\rho_L}{2\pi \rho} $$

Since the electric field intensity in free space is $\mathbf{E} = \frac{\mathbf{D}}{\varepsilon_0}$, we get:
$$ \mathbf{E} = \frac{\rho_L}{2\pi \varepsilon_0 \rho} \mathbf{a}_\rho $$

In this final expression, $\rho_L$, $2$, $\pi$, and $\varepsilon_0$ are constants. Therefore, the magnitude of the electric field intensity $E$ is proportional to $1/\rho$:
$$ E \propto \frac{1}{\rho} $$
This proves that the electric field intensity of an infinitely long, straight line of uniform charge density varies inversely with the radial distance $\rho$ (or $r$) from the line.

*(Related location: Book Page 160 / PDF Page 160)*

***

### 🔴 Q.2 (b) What are meant by the potential difference between two points and absolute potential of a point in the electric field?

**Solution:**

**Potential Difference:**
The potential difference ($V_{AB}$) between two points A and B in an electric field $\mathbf{E}$ is defined as the work done (by an external agent) in moving a unit positive test charge from point A (initial position) to point B (final position).
If $W$ is the work done to move a charge $Q$, then:
$$ V_{AB} = \frac{W}{Q} = -\int_A^B \mathbf{E} \cdot d\mathbf{l} $$
The negative sign indicates that the work is performed against the electric field. It represents a change in potential energy per unit charge between those two specific locations. If $V_{AB}$ is positive, an external agent must do work to move the positive charge; if negative, the field itself does the work.

**Absolute Potential:**
The absolute potential ($V$) of a point in an electric field is the potential difference between that specific point and a chosen reference point where the potential is defined to be zero. 
In most electrostatic problems involving finite charge distributions, the zero-potential reference is conveniently chosen to be at infinity ($V(\infty) = 0$). Thus, the absolute potential at a point with radial position vector $\mathbf{r}$ is the work done per unit charge in bringing a test charge from infinity to that point:
$$ V(\mathbf{r}) = -\int_{\infty}^{\mathbf{r}} \mathbf{E} \cdot d\mathbf{l} $$
Absolute potential essentially provides a scalar field representation of the energy state of any point in space due to the surrounding charge distribution.

*(Related location: Book Page 166-167 / PDF Page 166-167)*

***

### Q.2 (c) A parallel plate capacitor with air as a dielectric has a plate area of $36\pi\text{ cm}^2$ and the separation between the plates of $1\text{ mm}$. It is charged to $100\text{V}$ by connecting across a battery. If the battery is disconnected and plate separation is increased to $2\text{ mm}$, calculate the change in (i) potential difference across the plates and (ii) energy stored.

**Solution:**

**Initial State (State 1):**
*   Plate Area, $S = 36\pi \text{ cm}^2 = 36\pi \times 10^{-4} \text{ m}^2$
*   Initial Separation, $d_1 = 1 \text{ mm} = 10^{-3} \text{ m}$
*   Dielectric is air, so $\varepsilon = \varepsilon_0 = \frac{10^{-9}}{36\pi} \text{ F/m}$ (Using the approximate fractional form for calculation simplicity)
*   Initial Voltage, $V_1 = 100 \text{ V}$

First, we calculate the initial capacitance $C_1$:
$$ C_1 = \frac{\varepsilon_0 S}{d_1} = \frac{\left( \frac{10^{-9}}{36\pi} \right) (36\pi \times 10^{-4})}{10^{-3}} = \frac{10^{-13}}{10^{-3}} = 10^{-10} \text{ F} = 100 \text{ pF} $$

Next, calculate the total charge $Q$ stored on the plates:
$$ Q = C_1 V_1 = (10^{-10} \text{ F})(100 \text{ V}) = 10^{-8} \text{ C} = 10 \text{ nC} $$

The initial energy stored in the capacitor is:
$$ W_1 = \frac{1}{2} C_1 V_1^2 = \frac{1}{2} (10^{-10})(100)^2 = \frac{1}{2} (10^{-6}) = 0.5 \times 10^{-6} \text{ J} = 0.5 \mu\text{J} $$

**Transition:**
The battery is **disconnected**. When a capacitor is isolated from a voltage source, the charge $Q$ trapped on the plates has nowhere to go and remains **constant**. 
Thus, $Q_2 = Q_1 = 10^{-8} \text{ C}$.

**Final State (State 2):**
*   New Separation, $d_2 = 2 \text{ mm} = 2 \times 10^{-3} \text{ m}$ (The separation is doubled).

The new capacitance $C_2$ is:
$$ C_2 = \frac{\varepsilon_0 S}{d_2} = \frac{1}{2} \left( \frac{\varepsilon_0 S}{d_1} \right) = \frac{1}{2} C_1 = 0.5 \times 10^{-10} \text{ F} = 50 \text{ pF} $$

**(i) Calculate the change in potential difference:**
The new potential difference $V_2$ across the plates is:
$$ V_2 = \frac{Q}{C_2} = \frac{10^{-8}}{0.5 \times 10^{-10}} = 200 \text{ V} $$
The change in potential difference $\Delta V$ is:
$$ \Delta V = V_2 - V_1 = 200 \text{ V} - 100 \text{ V} = \mathbf{100 \text{ V}} $$

**(ii) Calculate the change in energy stored:**
The new energy stored $W_2$ is:
$$ W_2 = \frac{1}{2} \frac{Q^2}{C_2} = \frac{1}{2} \frac{(10^{-8})^2}{0.5 \times 10^{-10}} = \frac{10^{-16}}{10^{-10}} = 10^{-6} \text{ J} = 1.0 \mu\text{J} $$
The change in energy stored $\Delta W$ is:
$$ \Delta W = W_2 - W_1 = 1.0 \mu\text{J} - 0.5 \mu\text{J} = \mathbf{0.5 \mu\text{J}} $$
*(Note: The increase in electrostatic energy comes from the mechanical work done by an external force to pull the oppositely charged plates further apart).*

*(Related location: Book Page 256 for capacitance equation, Book Page 181 for energy equation / PDF Page 256, 181)*
### 🔴 Q.3 (a) What are electric dipole and dipole moment?

**Solution:**

**Electric Dipole:**
An electric dipole is formed when two point charges of equal magnitude but opposite sign (e.g., $+Q$ and $-Q$) are separated by a very small distance, denoted as $d$. This arrangement represents a fundamental building block in electrostatics, especially when studying the behavior of dielectric materials, where molecules can act as microscopic dipoles. 

**Dipole Moment:**
The electric dipole moment is a vector quantity that characterizes the strength and orientation of an electric dipole. It is defined as the product of the magnitude of one of the charges ($Q$) and the distance vector ($\mathbf{d}$) separating them.
Mathematically, it is expressed as:
$$ \mathbf{p} = Q\mathbf{d} $$
*   **Magnitude:** The magnitude of the dipole moment is $p = Qd$.
*   **Direction:** By convention, the direction of the distance vector $\mathbf{d}$, and therefore the direction of the dipole moment $\mathbf{p}$, is strictly from the negative charge ($-Q$) to the positive charge ($+Q$). The SI unit for dipole moment is the Coulomb-meter ($\text{C}\cdot\text{m}$).

*(Related location: Book Page 175-176, Equation 4.79 / PDF Page 175-176)*

***

### 🔴 Q.3 (b) Derive the equation of potential due to an electric dipole.

**Solution:**

Consider an electric dipole consisting of a positive charge $+Q$ and a negative charge $-Q$ separated by a small distance $d$. We want to find the electric potential $V$ at an observation point $P(r, \theta, \phi)$ in spherical coordinates. Let the dipole be centered at the origin, with $+Q$ located at $z = +d/2$ and $-Q$ located at $z = -d/2$ along the z-axis.

Let the distance from $+Q$ to point $P$ be $r_1$, and the distance from $-Q$ to point $P$ be $r_2$. The distance from the origin to $P$ is $r$.
Using the principle of superposition, the total potential at $P$ is the algebraic sum of the potentials due to each individual point charge:
$$ V = V_+ + V_- $$
$$ V = \frac{Q}{4\pi\varepsilon_0 r_1} + \frac{-Q}{4\pi\varepsilon_0 r_2} $$
$$ V = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{1}{r_1} - \frac{1}{r_2} \right] $$
$$ V = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{r_2 - r_1}{r_1 r_2} \right] $$

For a macroscopic observation point, the distance $r$ is much much greater than the separation distance $d$ ($r \gg d$). Under this "far-field" assumption, the lines representing $r_1$, $r$, and $r_2$ become essentially parallel to each other.
Drawing a perpendicular line from the $+Q$ position to the $r_2$ line creates a right triangle. From this geometry, we can approximate the path difference:
$$ r_2 - r_1 \approx d \cos\theta $$
Furthermore, since $d$ is very small, the product of the distances in the denominator can be approximated as the square of the distance from the origin:
$$ r_1 r_2 \approx r^2 $$

Substituting these approximations back into the potential equation yields:
$$ V \approx \frac{Q}{4\pi\varepsilon_0} \left[ \frac{d \cos\theta}{r^2} \right] $$
$$ V = \frac{Qd \cos\theta}{4\pi\varepsilon_0 r^2} $$

We know from the definition of dipole moment that its magnitude is $p = Qd$. Also, if the dipole is oriented along the z-axis, the vector $\mathbf{d} = d \mathbf{a}_z$. We can express $d \cos\theta$ as the dot product between the distance vector $\mathbf{d}$ and the radial unit vector $\mathbf{a}_r$ because $\mathbf{a}_z \cdot \mathbf{a}_r = \cos\theta$.
Therefore, $Qd \cos\theta = Q(\mathbf{d} \cdot \mathbf{a}_r) = \mathbf{p} \cdot \mathbf{a}_r$.

Substituting this vector notation into the potential equation gives the final, generalized form of the potential due to an electric dipole:
$$ V = \frac{\mathbf{p} \cdot \mathbf{a}_r}{4\pi\varepsilon_0 r^2} $$

*(Related location: Book Page 176, Equations 4.77, 4.78, 4.80 / PDF Page 176)*

***

### Q.3 (c) Explain the effect of external electric field on dielectric material and hence derive the equation $\bar{D} = \varepsilon_o\bar{E} + \bar{P}$, where the symbols have their usual meanings.

**Solution:**

**Effect of External Electric Field on Dielectric Material:**
Dielectric materials (insulators) do not possess free electrons that can move easily through the material to conduct current. Instead, their electrons are tightly bound to atomic nuclei. However, these charges are bound by finite forces, and when an external electric field $\mathbf{E}$ is applied, it exerts a force on them ($\mathbf{F} = Q\mathbf{E}$). 
*   The positive charges (nuclei) are pushed slightly in the direction of the field.
*   The negative charges (electron clouds) are pushed slightly in the direction opposite to the field.
This slight spatial separation of the centers of positive and negative charge within atoms or molecules creates microscopic electric dipoles. The material is then said to be **polarized**. The overall macroscopic effect is the creation of a vast network of aligned dipole moments throughout the dielectric volume.

**Derivation of $\mathbf{D} = \varepsilon_0\mathbf{E} + \mathbf{P}$:**
We define a macroscopic vector quantity called **Polarization ($\mathbf{P}$)** as the total dipole moment per unit volume.
When a dielectric is polarized, the spatial variation of these aligned dipoles leads to an accumulation of net bound charge in certain regions. This bound volume charge density, $\rho_{pv}$, is mathematically related to the divergence of the polarization vector:
$$ \rho_{pv} = -\nabla \cdot \mathbf{P} $$

If the region also contains free charges (like electrons on a conductor embedded in the dielectric) with a volume density $\rho_v$, the total charge density $\rho_t$ in that space is the sum of free and bound charges:
$$ \rho_t = \rho_v + \rho_{pv} $$

From the fundamental postulates of electrostatics in free space, Gauss's law in point (differential) form relates the divergence of the electric field to the *total* charge density:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_t $$

Substituting the expression for total charge density:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_v + \rho_{pv} $$

Now, substitute the relationship between bound charge and polarization:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) = \rho_v - \nabla \cdot \mathbf{P} $$

Rearrange the equation to group the divergence terms on the left side:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E}) + \nabla \cdot \mathbf{P} = \rho_v $$
Since the divergence operator is linear, we can combine the terms inside a single operator:
$$ \nabla \cdot (\varepsilon_0 \mathbf{E} + \mathbf{P}) = \rho_v $$

To simplify Maxwell's equations and make them dependent only on free charges (which are the charges we can typically control and measure), we define a new vector field called the **Electric Flux Density ($\mathbf{D}$)** such that its divergence equals exactly the free volume charge density:
$$ \nabla \cdot \mathbf{D} = \rho_v $$

Comparing the last two equations, it is evident that the definition of the electric flux density in any generalized medium must be:
$$ \mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} $$
This shows that the total flux density $\mathbf{D}$ consists of a free space component ($\varepsilon_0 \mathbf{E}$) and a material polarization component ($\mathbf{P}$).

*(Related location: Book Page 212-215 / PDF Page 212-215)*

***

### Q.3 (d) A metallic sphere of radius 10cm has a surface charge density of $10\text{nC/m}^2$. Calculate the potential at the center of the sphere.

**Solution:**

**Key Concept:**
A metallic sphere is a perfect conductor. Under static conditions, there can be no electric field inside a conductor ($\mathbf{E} = 0$). Because $\mathbf{E} = -\nabla V = 0$, it implies that there is no potential difference between any two points within the conductor. Therefore, a conductor forms an **equipotential volume**. 
This means that the electric potential is exactly the same everywhere inside the sphere, and this internal potential is equal to the potential on its surface.
$$ V_{center} = V_{surface} $$

**Calculation:**
First, we find the potential at the surface of the sphere. For a spherically symmetric charge distribution, the potential at or outside the surface is the same as if all the charge were concentrated at a point at the center.
The formula for the potential at the surface ($r = a$) of a sphere with total charge $Q$ is:
$$ V = \frac{Q}{4\pi\varepsilon_0 a} $$

We are given the surface charge density $\rho_S = 10 \text{ nC/m}^2 = 10 \times 10^{-9} \text{ C/m}^2$.
The total charge $Q$ on the sphere is the surface charge density multiplied by the surface area of the sphere ($A = 4\pi a^2$):
$$ Q = \rho_S \times (4\pi a^2) $$

Substitute this expression for $Q$ into the potential formula:
$$ V_{surface} = \frac{\rho_S (4\pi a^2)}{4\pi\varepsilon_0 a} $$
Simplifying the expression by canceling terms ($4\pi$ and one factor of $a$):
$$ V_{surface} = \frac{\rho_S \cdot a}{\varepsilon_0} $$

Given values:
*   Radius $a = 10 \text{ cm} = 0.1 \text{ m}$
*   Surface charge density $\rho_S = 10 \times 10^{-9} \text{ C/m}^2$
*   Permittivity of free space $\varepsilon_0 \approx 8.854 \times 10^{-12} \text{ F/m}$ (or using $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^9$)

Using the simplified formula:
$$ V_{center} = V_{surface} = \frac{(10 \times 10^{-9} \text{ C/m}^2)(0.1 \text{ m})}{8.854 \times 10^{-12} \text{ F/m}} $$
$$ V_{center} = \frac{10^{-9}}{8.854 \times 10^{-12}} \text{ Volts} $$
$$ V_{center} = \frac{1000}{8.854} \text{ Volts} \approx 112.94 \text{ V} $$

Alternatively, using $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^9$:
$$ V_{surface} = \rho_S \cdot a \cdot \frac{4\pi}{4\pi\varepsilon_0} = (10 \times 10^{-9})(0.1)(4\pi)(9 \times 10^9) $$
$$ V_{surface} = (10^{-9}) \cdot (10^9) \cdot 1 \cdot 36\pi = 36\pi \text{ Volts} \approx 113.1 \text{ V} $$

Therefore, the potential at the center of the sphere is approximately **113 V**.

*(Related location: Concept of Equipotential Conductor: Book Page 206 / PDF Page 206)*
### 🔴 Q1. (a) Define Electric Field and Electric Field intensity of a point in space. Show that $\mathbf{E} = -\nabla V$.

**Electric Field Definition:**
An electric field is a region of space around a charged particle or object within which a force would be exerted on other charged particles or objects. It is a vector field that associates to each point in space the electrostatic force per unit of charge exerted on an infinitesimal positive test charge at rest at that point.

**Electric Field Intensity ($\mathbf{E}$):**
The electric field intensity (or electric field strength) $\mathbf{E}$ at a point in space is defined as the electrical force $\mathbf{F}$ experienced by a unit positive test charge $Q$ placed at that point. Mathematically, it is given by:
$$ \mathbf{E} = \lim_{Q \to 0} \frac{\mathbf{F}}{Q} $$
or simply, $\mathbf{E} = \frac{\mathbf{F}}{Q}$. It is measured in Newtons per Coulomb (N/C) or Volts per meter (V/m).

**Derivation of $\mathbf{E} = -\nabla V$:**
The potential difference $V_{AB}$ between two points A and B is defined as the work done per unit charge in moving a test charge from A to B against the electric field $\mathbf{E}$. This is expressed as the line integral:
$$ V_{AB} = V_B - V_A = -\int_A^B \mathbf{E} \cdot d\mathbf{l} $$
For an infinitesimal displacement $d\mathbf{l}$, the differential change in potential $dV$ is:
$$ dV = -\mathbf{E} \cdot d\mathbf{l} $$
From multi-variable calculus, the total differential change $dV$ of a scalar field $V(x, y, z)$ over a displacement $d\mathbf{l} = dx\mathbf{a}_x + dy\mathbf{a}_y + dz\mathbf{a}_z$ is given by the dot product of its gradient and the displacement vector:
$$ dV = \frac{\partial V}{\partial x}dx + \frac{\partial V}{\partial y}dy + \frac{\partial V}{\partial z}dz = \left( \frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z \right) \cdot (dx\mathbf{a}_x + dy\mathbf{a}_y + dz\mathbf{a}_z) $$
$$ dV = \nabla V \cdot d\mathbf{l} $$
By comparing the two expressions for $dV$:
$$ \nabla V \cdot d\mathbf{l} = -\mathbf{E} \cdot d\mathbf{l} $$
Since this relationship must hold true for any arbitrary displacement vector $d\mathbf{l}$, the vectors themselves must be equal. Therefore:
$$ \mathbf{E} = -\nabla V $$
This shows that the electric field intensity is the negative gradient of the electric potential. The negative sign indicates that the electric field points in the direction of decreasing potential.

*(Related location: Book Page 147-148 / PDF Page 172-173)*

---

### 🔴 Q1. (b) Describe the effect of electric field on conductor and hence explain that we are safe inside a car during the thunder storm.

**Effect of Electric Field on a Conductor:**
A conducting material contains a sea of free electrons that are not tightly bound to their parent atoms and can move freely throughout the material. 
When an isolated conductor is placed in an external static electric field ($\mathbf{E}_e$), this field exerts a force ($\mathbf{F} = -e\mathbf{E}_e$) on the free electrons. The electrons are pushed in the direction opposite to the applied field. This rapid migration of charges causes negative charges to accumulate on one side of the conductor's surface and leaves a net positive charge on the opposite side.
These accumulated surface charges create their own internal "induced" electric field ($\mathbf{E}_i$) that opposes the external field. The charges will continue to redistribute almost instantaneously until the induced internal field exactly cancels the external applied field everywhere inside the conductor material.
As a result:
1.  The net electric field inside a perfect conductor under static conditions is identically zero ($\mathbf{E} = 0$).
2.  All net charge resides exclusively on the outer surface of the conductor ($\rho_v = 0$ inside).
3.  The entire conductor forms an equipotential volume, meaning the potential difference between any two points within or on the conductor is zero.

**Safety Inside a Car During a Thunderstorm:**
A car with a metal body acts essentially as a hollow conductor, often referred to as a Faraday cage. During a thunderstorm, when lightning strikes the car, it subjects the car to an immense external electric field and deposits a massive amount of charge onto it.
Because of the properties of conductors described above, these charges rapidly distribute themselves completely over the exterior metallic surface of the car's body. The induced field generated by these surface charges perfectly cancels the external electric field inside the vehicle. 
Therefore, the net electric field inside the passenger cabin remains zero ($\mathbf{E} = 0$). Since there is no electric field inside, no electrical forces are exerted on the occupants, and no current flows through the interior space. The occupants are entirely shielded from the lightning strike, making the inside of the car a safe place.

*(Related location: Book Page 202, 206 / PDF Page 227, 231)*

---

### Q1. (c) Two uniform sheets of charges with each of density of $100 \text{ nC/m}^2$ are located at $x = \pm 1$ m apart. Determine $\mathbf{E}$ in all regions ($x < -1$, $-1 < x < 1$, $x > 1$).

**Solution:**
The electric field intensity $\mathbf{E}$ produced by an infinite sheet of uniform surface charge density $\rho_S$ is given by:
$$ \mathbf{E} = \frac{\rho_S}{2\varepsilon_0} \mathbf{a}_n $$
where $\mathbf{a}_n$ is the unit normal vector directed away from the sheet.

Let's calculate the magnitude of the electric field produced by one such sheet:
$$ E_0 = \frac{|\rho_S|}{2\varepsilon_0} = \frac{100 \times 10^{-9}}{2 \times \varepsilon_0} $$
Using the approximation $\frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9 \text{ m/F}$, we have $\frac{1}{2\varepsilon_0} = 18\pi \times 10^9$.
$$ E_0 = (100 \times 10^{-9}) \times (18\pi \times 10^9) = 1800\pi \text{ V/m} $$

We have two sheets:
*   Sheet 1 at $x = -1$ m with $\rho_{S1} = 100 \text{ nC/m}^2$
*   Sheet 2 at $x = 1$ m with $\rho_{S2} = 100 \text{ nC/m}^2$

By the principle of superposition, the total electric field $\mathbf{E}$ in any region is the vector sum of the fields from each sheet: $\mathbf{E} = \mathbf{E}_1 + \mathbf{E}_2$.

**Region 1: $x < -1$**
This region is to the left of both sheets.
*   For Sheet 1 ($x = -1$), the outward normal pointing into this region is $-\mathbf{a}_x$. So, $\mathbf{E}_1 = -E_0 \mathbf{a}_x$.
*   For Sheet 2 ($x = 1$), the outward normal pointing into this region is $-\mathbf{a}_x$. So, $\mathbf{E}_2 = -E_0 \mathbf{a}_x$.
*   Total Field: $\mathbf{E} = (-E_0 - E_0)\mathbf{a}_x = -2E_0 \mathbf{a}_x = -3600\pi \mathbf{a}_x \text{ V/m}$

**Region 2: $-1 < x < 1$**
This region is between the two sheets.
*   For Sheet 1 ($x = -1$), the outward normal pointing into this region is $+\mathbf{a}_x$. So, $\mathbf{E}_1 = +E_0 \mathbf{a}_x$.
*   For Sheet 2 ($x = 1$), the outward normal pointing into this region is $-\mathbf{a}_x$. So, $\mathbf{E}_2 = -E_0 \mathbf{a}_x$.
*   Total Field: $\mathbf{E} = (E_0 - E_0)\mathbf{a}_x = \mathbf{0} \text{ V/m}$

**Region 3: $x > 1$**
This region is to the right of both sheets.
*   For Sheet 1 ($x = -1$), the outward normal pointing into this region is $+\mathbf{a}_x$. So, $\mathbf{E}_1 = +E_0 \mathbf{a}_x$.
*   For Sheet 2 ($x = 1$), the outward normal pointing into this region is $+\mathbf{a}_x$. So, $\mathbf{E}_2 = +E_0 \mathbf{a}_x$.
*   Total Field: $\mathbf{E} = (E_0 + E_0)\mathbf{a}_x = +2E_0 \mathbf{a}_x = +3600\pi \mathbf{a}_x \text{ V/m}$

*(Related location: Book Page 136 / PDF Page 161)*

---

### 🔴 Q2. (a) Derive the point form of Gauss's law. State divergence theorem and prove it using Gauss's law.

**Derivation of the Point Form of Gauss's Law:**
Gauss's law in its integral form states that the total electric flux passing through a closed surface $S$ is equal to the total charge $Q_{enc}$ enclosed by that volume $v$:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
The total enclosed charge can also be expressed as the volume integral of the volume charge density $\rho_v$ over the volume $v$ bounded by surface $S$:
$$ Q_{enc} = \int_v \rho_v \, dv $$
Equating the two expressions gives:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v \, dv $$
Now, we apply the Divergence Theorem to the left side of the equation. The Divergence Theorem allows us to convert the closed surface integral of a vector field into a volume integral of its divergence:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{D}) \, dv $$
Substituting this back into our equation yields:
$$ \int_v (\nabla \cdot \mathbf{D}) \, dv = \int_v \rho_v \, dv $$
For this equality to hold true for *any* arbitrary continuous volume $v$, the integrands themselves must be identically equal at every point. Therefore:
$$ \nabla \cdot \mathbf{D} = \rho_v $$
This is the differential or point form of Gauss's law (also the first of Maxwell's equations).

**Divergence Theorem Statement:**
The Divergence Theorem states that the total outward flux of a vector field $\mathbf{A}$ through a closed surface $S$ is equal to the volume integral of the divergence of the vector field $\mathbf{A}$ over the volume $v$ enclosed by the surface $S$.
$$ \oint_S \mathbf{A} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{A}) \, dv $$

**Proof showing connection using Gauss's law concepts:**
While the Divergence Theorem is a purely mathematical identity, its relationship can be elegantly illustrated using the physical concepts of Gauss's law.
From the physical law, we know the total flux relates to enclosed charge:
1) $ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $
And we know charge relates to charge density:
2) $ Q_{enc} = \int_v \rho_v \, dv $
From the point form of Gauss's law (derived independently for infinitesimal volumes), we know the charge density is the divergence of the flux density:
3) $ \rho_v = \nabla \cdot \mathbf{D} $
Substituting (3) into (2) gives:
$ Q_{enc} = \int_v (\nabla \cdot \mathbf{D}) \, dv $
Finally, equating this expression for $Q_{enc}$ with the original flux equation (1) yields:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{D}) \, dv $$
Since the physical field $\mathbf{D}$ can represent any well-behaved continuous vector field, this physically-motivated derivation demonstrates the mathematical truth of the Divergence Theorem: $\oint_S \mathbf{A} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{A}) \, dv$.

*(Related location: Book Page 133 / PDF Page 158)*

---

### Q2. (b) A rectangular parallelepiped defined by $0 < x < 2, 0 < y < 3$, and $0 < z < 5$ m contains a volume charge density that causes an electric field $\mathbf{E} = \frac{1}{\varepsilon_0} [4xy\mathbf{a}_x + 2(x^2 + z^2)\mathbf{a}_y + 4yz\mathbf{a}_z]$. Find the total charge contained in the volume.

**Solution:**
We are given the electric field $\mathbf{E}$ and need to find the total enclosed charge $Q$. We can use the point form of Gauss's law to find the volume charge density $\rho_v$ and then integrate it over the given volume.

First, find the electric flux density $\mathbf{D}$:
$$ \mathbf{D} = \varepsilon_0 \mathbf{E} = 4xy\mathbf{a}_x + 2(x^2 + z^2)\mathbf{a}_y + 4yz\mathbf{a}_z $$

Next, apply the point form of Gauss's law ($\nabla \cdot \mathbf{D} = \rho_v$) to find the charge density $\rho_v$:
$$ \rho_v = \nabla \cdot \mathbf{D} = \frac{\partial D_x}{\partial x} + \frac{\partial D_y}{\partial y} + \frac{\partial D_z}{\partial z} $$
$$ \rho_v = \frac{\partial}{\partial x}(4xy) + \frac{\partial}{\partial y}(2x^2 + 2z^2) + \frac{\partial}{\partial z}(4yz) $$
$$ \rho_v = 4y + 0 + 4y $$
$$ \rho_v = 8y \text{ C/m}^3 $$

Now, calculate the total charge $Q$ by integrating the volume charge density over the defined rectangular parallelepiped volume $v$:
$$ Q = \int_v \rho_v \, dv = \int_{z=0}^{5} \int_{y=0}^{3} \int_{x=0}^{2} 8y \, dx \, dy \, dz $$
Since the limits are constant, we can separate the integrals:
$$ Q = \left( \int_{0}^{2} dx \right) \left( \int_{0}^{3} 8y \, dy \right) \left( \int_{0}^{5} dz \right) $$
Evaluate each integral:
*   $\int_{0}^{2} dx = [x]_0^2 = 2 - 0 = 2$
*   $\int_{0}^{3} 8y \, dy = \left[ 4y^2 \right]_0^3 = 4(3^2) - 4(0^2) = 4(9) = 36$
*   $\int_{0}^{5} dz = [z]_0^5 = 5 - 0 = 5$

Multiply the results together:
$$ Q = 2 \times 36 \times 5 = 10 \times 36 = 360 \text{ C} $$

The total charge contained in the volume is **360 Coulombs**.

*(Related location: Book Page 133 / PDF Page 158)*

---

### 🔴 Q2. (c) Define electric potential and equipotential line. Show that electric potential difference between two points a and b is independent of the path through which a charge is taken between the points.

**Electric Potential:**
The electric potential $V$ at any given point in an electric field is defined as the work done by an external agent in bringing a unit positive test charge from a reference point (usually assumed to be at infinity, where potential is zero) to that specific point. It is a scalar quantity measured in Volts (V) or Joules per Coulomb (J/C).

**Equipotential Line/Surface:**
An equipotential line (in 2D) or equipotential surface (in 3D) is a locus of points in space that all share the exact same electric potential. Because the potential difference between any two points on an equipotential surface is zero, no work is required to move a charge along this surface.

**Proof of Path Independence:**
The potential difference $V_{ab}$ between two points $a$ and $b$ is the work done per unit charge to move from $a$ to $b$, defined by the line integral:
$$ V_{ab} = -\int_a^b \mathbf{E} \cdot d\mathbf{l} $$
We must show that this integral yields the same value regardless of the path taken from $a$ to $b$.
A fundamental property of an electrostatic field is that it is a **conservative field**. This means that the total work done in moving a charge around *any* closed path $L$ is identically zero. Mathematically, this is expressed as:
$$ \oint_L \mathbf{E} \cdot d\mathbf{l} = 0 $$
Consider two distinct paths between points $a$ and $b$: Path 1 and Path 2. We can form a closed loop by moving from $a$ to $b$ via Path 1, and then returning from $b$ to $a$ via Path 2.
Applying the conservative field property to this closed loop:
$$ \int_{\text{Path 1 (a to b)}} \mathbf{E} \cdot d\mathbf{l} + \int_{\text{Path 2 (b to a)}} \mathbf{E} \cdot d\mathbf{l} = 0 $$
The integral from $b$ to $a$ is the negative of the integral from $a$ to $b$ along the same path. So we can reverse the direction of the second term:
$$ \int_{\text{Path 1 (a to b)}} \mathbf{E} \cdot d\mathbf{l} - \int_{\text{Path 2 (a to b)}} \mathbf{E} \cdot d\mathbf{l} = 0 $$
Rearranging the equation yields:
$$ \int_{\text{Path 1 (a to b)}} \mathbf{E} \cdot d\mathbf{l} = \int_{\text{Path 2 (a to b)}} \mathbf{E} \cdot d\mathbf{l} $$
This equality proves that the line integral of the electric field—and therefore the electric potential difference $V_{ab}$—evaluates to the exact same value regardless of whether Path 1, Path 2, or any other path is chosen between points $a$ and $b$.

*(Related location: Book Page 141-143, 147 / PDF Page 166-168, 172)*

---

### Obtain the boundary conditions for the conductor-to-free space boundary in electrostatics.

**Derivation of Boundary Conditions:**
Boundary conditions define how electromagnetic fields behave as they cross an interface between two different media. Here, we analyze the interface between a perfect conductor and free space.
A fundamental property of a perfect conductor in electrostatics is that the electric field inside it must be zero ($\mathbf{E}_{inside} = 0$, $\mathbf{D}_{inside} = 0$).

**1. Tangential Component:**
We apply the conservative property of the electrostatic field, which states that the closed line integral of the electric field is zero:
$$ \oint \mathbf{E} \cdot d\mathbf{l} = 0 $$
Consider a small rectangular closed path $abcda$ spanning the boundary. Let the path have a width $\Delta w$ parallel to the boundary and a very small height $\Delta h$ normal to it. The top half lies in free space and the bottom half lies inside the conductor.
Integrating around the loop:
$$ \int_{a}^{b} \mathbf{E} \cdot d\mathbf{l} + \int_{b}^{c} \mathbf{E} \cdot d\mathbf{l} + \int_{c}^{d} \mathbf{E} \cdot d\mathbf{l} + \int_{d}^{a} \mathbf{E} \cdot d\mathbf{l} = 0 $$
Assuming the path is small enough that $\mathbf{E}$ is uniform along each segment:
$$ E_{t\_free} \Delta w - E_n \frac{\Delta h}{2} - E_{t\_cond} \Delta w + E_n \frac{\Delta h}{2} = 0 $$
Since the field inside the conductor is zero, $E_{t\_cond} = 0$.
As we shrink the height of the loop to zero ($\Delta h \to 0$), the contributions from the vertical sides vanish. The equation simplifies to:
$$ E_{t\_free} \Delta w = 0 $$
Since $\Delta w \neq 0$, it must be that:
$$ E_{t} = 0 $$
This indicates that the tangential component of the electric field just outside a perfect conductor must be zero. Since $\mathbf{D} = \varepsilon_0 \mathbf{E}$, it follows that $D_t = 0$.

**2. Normal Component:**
We apply Gauss's law in integral form:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
Consider a small cylindrical pillbox (Gaussian surface) spanning the boundary, with its top face in free space, bottom face in the conductor, and height $\Delta h$. Let the area of the flat faces be $\Delta S$.
Integrating over the pillbox surface:
$$ \int_{top} \mathbf{D} \cdot d\mathbf{S} + \int_{bottom} \mathbf{D} \cdot d\mathbf{S} + \int_{sides} \mathbf{D} \cdot d\mathbf{S} = \Delta Q_{enc} = \rho_S \Delta S $$
Where $\rho_S$ is the surface charge density on the conductor.
*   On the top face in free space, $\mathbf{D} \cdot d\mathbf{S} = D_{n\_free} \Delta S$.
*   On the bottom face inside the conductor, $\mathbf{D} = 0$, so the integral is 0.
*   As we shrink the height of the pillbox to zero ($\Delta h \to 0$), the flux through the sides approaches 0.

The equation becomes:
$$ D_{n\_free} \Delta S - 0 + 0 = \rho_S \Delta S $$
Dividing by $\Delta S$, we get:
$$ D_n = \rho_S $$
This indicates that the normal component of the electric flux density just outside the conductor is equal to the surface charge density. Since $D_n = \varepsilon_0 E_n$, the normal electric field is $E_n = \frac{\rho_S}{\varepsilon_0}$.

**Summary:**
The boundary conditions for a conductor-to-free space interface dictate that the electric field must be entirely normal (perpendicular) to the conductor surface.
*   Tangential fields: $E_t = 0, \quad D_t = 0$
*   Normal fields: $D_n = \rho_S, \quad E_n = \frac{\rho_S}{\varepsilon_0}$

*(Related location: Book Page 202 / PDF Page 227)*
### 🔴 Q.3 (a) What is electric dipole? Determine the equation of voltage for an electric dipole system.

**Solution:**

**Electric Dipole Definition:**
An electric dipole is formed when two point charges of exactly equal magnitude but opposite sign (e.g., $+Q$ and $-Q$) are separated by a very small distance. 
The strength and orientation of this arrangement are characterized by the **magnetic dipole moment**, $\mathbf{p}$. It is defined as the product of the charge magnitude $Q$ and the distance vector $\mathbf{d}$ directed from the negative charge to the positive charge:
$$ \mathbf{p} = Q\mathbf{d} $$

**Derivation of Voltage (Electric Potential) for a Dipole:**
Consider an electric dipole centered at the origin of a coordinate system. Let the positive charge $+Q$ be located at $z = +d/2$ and the negative charge $-Q$ be located at $z = -d/2$ along the z-axis. We want to find the potential $V$ at an observation point $P(r, \theta, \phi)$ in spherical coordinates.

Let $r_1$ be the distance from $+Q$ to point $P$, and $r_2$ be the distance from $-Q$ to point $P$. 
Using the principle of superposition, the total electric potential at $P$ is the scalar sum of the potentials from the individual charges:
$$ V = V_+ + V_- = \frac{Q}{4\pi\varepsilon_0 r_1} + \frac{-Q}{4\pi\varepsilon_0 r_2} $$
$$ V = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{1}{r_1} - \frac{1}{r_2} \right] = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{r_2 - r_1}{r_1 r_2} \right] $$

For practical dipole applications, we are usually interested in the potential at a point far away compared to the separation distance, so we assume $r \gg d$ (far-field approximation). 
Under this assumption, the lines representing $r_1$, $r$, and $r_2$ are approximately parallel. From the geometry of the setup, if we drop a perpendicular from the $+Q$ position to the $r_2$ line, the path length difference is:
$$ r_2 - r_1 \approx d \cos\theta $$
Furthermore, the product of the distances in the denominator can be approximated as:
$$ r_1 r_2 \approx r^2 $$

Substituting these approximations back into the potential equation gives:
$$ V \approx \frac{Q}{4\pi\varepsilon_0} \left[ \frac{d \cos\theta}{r^2} \right] $$
$$ V = \frac{Qd \cos\theta}{4\pi\varepsilon_0 r^2} $$

Recognizing that the magnitude of the dipole moment is $p = Qd$, we can write:
$$ V = \frac{p \cos\theta}{4\pi\varepsilon_0 r^2} $$
To express this in a more general vector form, note that the dipole moment vector is $\mathbf{p} = p\mathbf{a}_z$. Since the dot product of $\mathbf{a}_z$ with the radial unit vector $\mathbf{a}_r$ is $\mathbf{a}_z \cdot \mathbf{a}_r = \cos\theta$, we can write $p\cos\theta = \mathbf{p} \cdot \mathbf{a}_r$. 
Thus, the final equation for the voltage (potential) of an electric dipole is:
$$ V = \frac{\mathbf{p} \cdot \mathbf{a}_r}{4\pi\varepsilon_0 r^2} $$

*(Related location: Book Page 150-151 / PDF Page 175-176)*

### 🔴 Q.3 (b) Show that the energy stored in an electric field can be given by $W_E = \frac{1}{2} \int \varepsilon_o E^2 dv$.

**Solution:**

The energy required to assemble a continuous volume charge distribution with density $\rho_v$ is given by integrating the potential energy of infinitesimal charge elements over the volume $v$:
$$ W_E = \frac{1}{2} \int_v \rho_v V \, dv $$
where $V$ is the absolute potential at the location of the charge element.

We want to express this energy entirely in terms of the electric field $\mathbf{E}$. 
From the point form of Gauss's law, we know the relationship between volume charge density and electric flux density $\mathbf{D}$:
$$ \rho_v = \nabla \cdot \mathbf{D} $$

Substituting this into the energy integral:
$$ W_E = \frac{1}{2} \int_v (\nabla \cdot \mathbf{D}) V \, dv $$

Now, we use the vector identity for the divergence of the product of a scalar and a vector: $\nabla \cdot (V\mathbf{A}) = \mathbf{A} \cdot \nabla V + V(\nabla \cdot \mathbf{A})$. 
Rearranging this identity to isolate the term we have:
$$ V(\nabla \cdot \mathbf{D}) = \nabla \cdot (V\mathbf{D}) - \mathbf{D} \cdot (\nabla V) $$

Substitute this back into the integral:
$$ W_E = \frac{1}{2} \int_v [\nabla \cdot (V\mathbf{D}) - \mathbf{D} \cdot (\nabla V)] \, dv $$
$$ W_E = \frac{1}{2} \int_v \nabla \cdot (V\mathbf{D}) \, dv - \frac{1}{2} \int_v \mathbf{D} \cdot (\nabla V) \, dv $$

Apply the Divergence Theorem to the first term on the right side to convert the volume integral to a closed surface integral over surface $S$ bounding volume $v$:
$$ W_E = \frac{1}{2} \oint_S (V\mathbf{D}) \cdot d\mathbf{S} - \frac{1}{2} \int_v \mathbf{D} \cdot (\nabla V) \, dv $$

To find the total energy stored in the entire field, we must extend the volume of integration to all of space (infinity). For a localized charge distribution, as $r \to \infty$, the potential $V$ falls off at least as fast as $1/r$, and the flux density $\mathbf{D}$ falls off at least as fast as $1/r^2$. The surface area $S$ increases as $r^2$. Therefore, the integrand of the surface integral $(V\mathbf{D})$ falls off as $1/r^3$, while the area $dS$ grows only as $r^2$. 
As the surface expands to infinity, the surface integral approaches zero:
$$ \oint_S (V\mathbf{D}) \cdot d\mathbf{S} \to 0 $$

We are left with only the second volume integral:
$$ W_E = -\frac{1}{2} \int_v \mathbf{D} \cdot (\nabla V) \, dv $$

Recall that the electric field intensity is the negative gradient of the potential: $\mathbf{E} = -\nabla V$. Substituting this yields:
$$ W_E = \frac{1}{2} \int_v \mathbf{D} \cdot \mathbf{E} \, dv $$

Finally, in a linear, isotropic medium (or free space), the electric flux density is proportional to the electric field: $\mathbf{D} = \varepsilon_0 \mathbf{E}$.
Substituting this relationship into the equation gives the final result:
$$ W_E = \frac{1}{2} \int_v (\varepsilon_0 \mathbf{E}) \cdot \mathbf{E} \, dv $$
$$ W_E = \frac{1}{2} \int_v \varepsilon_0 E^2 \, dv $$

*(Related location: Book Page 155-156 / PDF Page 180-181)*

### Q.3 (c) Two wires having charges $\rho_l$ C/m and $-\rho_l$ C/m are spaced $D$ m apart in the unbounded free space. The radius of each wire is $a$ m ($a \ll D$). Calculate the capacitance between the wires.

**Solution:**

This problem asks for the capacitance per unit length of a parallel two-wire transmission line. 
Let the two infinitely long, parallel cylindrical wires lie along the z-direction. 
*   Wire 1 has radius $a$ and carries a uniform line charge density $+\rho_l$.
*   Wire 2 has radius $a$ and carries a uniform line charge density $-\rho_l$.
*   The center-to-center separation distance between them is $D$.

To find the capacitance $C = Q/V$, we need to find the potential difference $V$ between the two wires due to the charge $Q$ (or $\rho_l$ per unit length).

First, recall the electric potential at a radial distance $r$ from a single infinitely long line charge $\rho_l$. It is obtained by integrating the electric field $\mathbf{E} = \frac{\rho_l}{2\pi\varepsilon_0 r}\mathbf{a}_r$:
$$ V(r) = -\int \frac{\rho_l}{2\pi\varepsilon_0 r} dr = -\frac{\rho_l}{2\pi\varepsilon_0} \ln(r) + K $$

By the principle of superposition, the total potential $V$ at any point $P$ in space is the sum of the potentials from both wires. Let $r_1$ be the perpendicular distance from Wire 1 to $P$, and $r_2$ be the perpendicular distance from Wire 2 to $P$:
$$ V_P = \left( -\frac{+\rho_l}{2\pi\varepsilon_0} \ln(r_1) \right) + \left( -\frac{-\rho_l}{2\pi\varepsilon_0} \ln(r_2) \right) = \frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{r_2}{r_1}\right) $$

Now, let's find the absolute potential of each wire surface. Because the radius $a \ll D$, we can assume the charge distribution on the surface of each wire is uniform and behaves as if concentrated along its central axis.

**Potential at the surface of Wire 1 ($V_1$):**
A point on the surface of Wire 1 is at a distance $r_1 = a$ from the center of Wire 1, and approximately at a distance $r_2 \approx D$ from the center of Wire 2 (since $a \ll D$).
$$ V_1 = \frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) $$

**Potential at the surface of Wire 2 ($V_2$):**
A point on the surface of Wire 2 is at a distance $r_2 = a$ from the center of Wire 2, and approximately at a distance $r_1 \approx D$ from the center of Wire 1.
$$ V_2 = \frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{a}{D}\right) = -\frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) $$

**Potential Difference ($V$):**
The total potential difference (voltage) $V$ between the two wires is:
$$ V = V_1 - V_2 = \frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) - \left[ -\frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) \right] $$
$$ V = 2 \left[ \frac{\rho_l}{2\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) \right] = \frac{\rho_l}{\pi\varepsilon_0} \ln\left(\frac{D}{a}\right) $$

**Capacitance per unit length ($C$):**
Capacitance is defined as the ratio of the charge to the potential difference. Using the charge per unit length $\rho_l$:
$$ C = \frac{\rho_l}{V} = \frac{\rho_l}{\frac{\rho_l}{\pi\varepsilon_0} \ln\left(\frac{D}{a}\right)} $$
$$ C = \frac{\pi\varepsilon_0}{\ln\left(\frac{D}{a}\right)} \text{ F/m} $$

*(Related location: Book Page 292 (Problem 6.64) / PDF Page 271, and Table 11.1 on Page 556)*

### Define conduction, convection, and displacement current. Deduce the equation of continuity and hence show that the charges introduced inside a conducting material redistribute themselves in such a way as to make the charge density inside the material is zero under equilibrium condition.

**Solution:**

**Definitions:**
1.  **Convection Current:** This current occurs when charge flows through an insulating medium, such as a liquid, a rarefied gas, or a vacuum. It represents the physical mass transport of charged particles. Convection current does *not* involve a conductor and consequently does *not* satisfy Ohm's law. Its current density is given by $\mathbf{J} = \rho_v \mathbf{u}$, where $\rho_v$ is the volume charge density and $\mathbf{u}$ is the velocity of the charges.
2.  **Conduction Current:** This current requires a conducting medium. It involves the drift movement of abundant free electrons through an atomic lattice under the influence of an applied external electric field. Conduction current satisfies the point form of Ohm's law. Its current density is given by $\mathbf{J} = \sigma \mathbf{E}$, where $\sigma$ is the conductivity of the material and $\mathbf{E}$ is the electric field.
3.  **Displacement Current:** This is a theoretical current postulated by Maxwell to satisfy the continuity equation in time-varying fields. It is a result of a time-varying electric field (or electric flux) and does not involve the physical movement of charge. It allows electromagnetic waves to propagate through free space or dielectrics. Its current density is given by $\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t}$, where $\mathbf{D}$ is the electric flux density.

**Deduction of the Equation of Continuity:**
The continuity equation is a mathematical statement of the principle of conservation of charge. If we consider a closed surface $S$ bounding a volume $v$, the total current $I_{out}$ flowing completely out of that surface must equal the time rate of decrease of the total charge $Q_{in}$ enclosed within it.
$$ I_{out} = \oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{dQ_{in}}{dt} $$
Since the enclosed charge $Q_{in} = \int_v \rho_v dv$, we substitute this in:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{d}{dt} \int_v \rho_v dv $$
Assuming the volume is stationary, the time derivative moves inside the integral as a partial derivative:
$$ \oint_S \mathbf{J} \cdot d\mathbf{S} = \int_v \left(-\frac{\partial \rho_v}{\partial t}\right) dv $$
Applying the Divergence Theorem to the left side ($\oint_S \mathbf{J} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{J}) dv$), we get:
$$ \int_v (\nabla \cdot \mathbf{J}) dv = \int_v \left(-\frac{\partial \rho_v}{\partial t}\right) dv $$
For this to be true for any arbitrary volume, the integrands must be equal, giving the point form of the continuity equation:
$$ \nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t} $$

**Charge Redistribution in a Conducting Material:**
Suppose an excess charge density is artificially introduced into the interior of a conducting material characterized by conductivity $\sigma$ and permittivity $\varepsilon$. We want to see how this charge behaves over time.

We use three fundamental equations:
1.  Continuity equation: $\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$
2.  Ohm's law for conductors: $\mathbf{J} = \sigma \mathbf{E}$
3.  Gauss's law: $\nabla \cdot \mathbf{E} = \frac{\rho_v}{\varepsilon}$

Substitute Ohm's law into the continuity equation:
$$ \nabla \cdot (\sigma \mathbf{E}) = -\frac{\partial \rho_v}{\partial t} $$
Assuming a homogeneous conductor, $\sigma$ is constant and can be pulled out of the divergence operator:
$$ \sigma (\nabla \cdot \mathbf{E}) = -\frac{\partial \rho_v}{\partial t} $$
Now, substitute Gauss's law ($\nabla \cdot \mathbf{E} = \frac{\rho_v}{\varepsilon}$) into this expression:
$$ \sigma \left( \frac{\rho_v}{\varepsilon} \right) = -\frac{\partial \rho_v}{\partial t} $$
Rearranging this yields a first-order homogeneous linear ordinary differential equation:
$$ \frac{\partial \rho_v}{\partial t} + \frac{\sigma}{\varepsilon} \rho_v = 0 $$
By separating variables and integrating ($\int \frac{d\rho_v}{\rho_v} = \int -\frac{\sigma}{\varepsilon} dt$), we find the solution:
$$ \rho_v(t) = \rho_{vo} e^{-(\sigma/\varepsilon)t} $$
where $\rho_{vo}$ is the initial charge density introduced at $t=0$.

This equation shows that any volume charge density placed inside a conductor decays exponentially over time. The time constant for this decay is $T_r = \varepsilon/\sigma$, known as the *relaxation time*.
For a good conductor (like copper), $\sigma$ is extremely large, making the relaxation time $T_r$ incredibly short (on the order of $10^{-19}$ seconds). Therefore, the initial charge decays to zero almost instantaneously. 
Because charge is conserved, this migrating charge does not disappear but rushes to the exterior surface of the material, establishing a surface charge. Thus, under equilibrium conditions ($t \gg T_r$), the charge density inside the conducting material is zero ($\rho_v = 0$).

*(Related location: Book Page 178-180, 196-197, 433 / PDF Page 203-205, 221-222, 412)*
### 🔴 Q.1. (a) State and explain Coulomb's force law.

**Solution:**

**State:**
Coulomb's law is an experimental law that describes the force between two point charges. It states that the electrostatic force $F$ between two point charges $Q_1$ and $Q_2$ is:
1.  Along the line joining them.
2.  Directly proportional to the product $Q_1Q_2$ of the charges.
3.  Inversely proportional to the square of the distance $R$ between them.

**Explain:**
Expressed mathematically, the force $\mathbf{F}_{12}$ exerted on charge $Q_2$ by charge $Q_1$ is given by:
$$ \mathbf{F}_{12} = \frac{Q_1 Q_2}{4\pi\varepsilon_0 R^2} \mathbf{a}_{R_{12}} $$
where:
*   $Q_1$ and $Q_2$ are the magnitudes of the point charges in Coulombs (C).
*   $R$ is the distance between the two charges in meters (m).
*   $\mathbf{a}_{R_{12}}$ is the unit vector directed from the source charge $Q_1$ to the observation charge $Q_2$. It dictates the direction of the force.
*   $\varepsilon_0$ is the permittivity of free space, approximately $8.854 \times 10^{-12}$ F/m. The proportionality constant is $k = \frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9$ m/F.

The law implies that like charges (charges of the same sign, so $Q_1Q_2 > 0$) repel each other, pushing them apart along the line joining them. Conversely, unlike charges (charges of opposite signs, so $Q_1Q_2 < 0$) attract each other. It's crucial to note that this law strictly applies to *point charges* in a static state, meaning the size of the charged bodies must be negligibly small compared to the distance $R$ separating them.

*(Related location: Book Page 112-113 / PDF Page 137-138)*

***

### 🔴 Q.1. (b) Define electric field intensity and hence show that $\vec{E} = \lim_{q \to 0} \frac{\vec{F}}{q}$.

**Solution:**

**Definition:**
The electric field intensity (or electric field strength) $\mathbf{E}$ at a specific point in space is defined as the electrical force per unit positive charge experienced by a hypothetical test charge placed at that point. It is a vector quantity that dictates both the magnitude and direction of the force that a $+1$ C charge would feel.

**Showing the limit expression:**
Suppose we have an existing electric field generated by some unknown distribution of source charges. We want to measure the electric field intensity $\mathbf{E}$ at a specific point. To do this, we bring a small positive "test charge," let's call it $q$, to that point and measure the electrostatic force $\mathbf{F}$ acting on it due to the source charges.

By our basic definition, the electric field is the force per unit charge:
$$ \mathbf{E} \approx \frac{\mathbf{F}}{q} $$

However, introducing a test charge $q$ into the region can potentially disturb the original source charge distribution that created the field we are trying to measure (especially if the source charges are on conductors where they can move freely). To ensure we are measuring the *original* undisturbed electric field, the test charge $q$ must be vanishingly small so its own electric field does not exert enough force to redistribute the source charges.

Therefore, the strict mathematical definition of the electric field intensity requires taking the limit as the test charge $q$ approaches zero:
$$ \mathbf{E} = \lim_{q \to 0} \frac{\mathbf{F}}{q} $$

This ensures that the test charge acts purely as a probe and does not alter the system it is measuring.

*(Related location: Book Page 114 / PDF Page 139)*

***

### Q.1. (c) What is the physical significance of $\nabla \times \vec{E} = 0$.

**Solution:**

The mathematical statement $\nabla \times \mathbf{E} = 0$ (the curl of the electric field is zero) indicates that the static electric field is **irrotational** or **conservative**.

**Physical Significance:**
1.  **Zero Work in a Closed Path:** By applying Stokes's theorem, $\oint_L \mathbf{E} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S}$. If $\nabla \times \mathbf{E} = 0$, then the closed line integral $\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$. Physically, this means that the net work done by the electric field (or by an external agent against the field) in moving a charge around *any* completely closed path is exactly zero. No net energy is gained or lost.
2.  **Path Independence:** Because the work done around a closed loop is zero, the work done in moving a charge from point A to point B is independent of the specific path taken between those two points.
3.  **Existence of Scalar Potential:** A fundamental theorem of vector calculus states that if a vector field has zero curl, it can always be expressed as the gradient of a scalar field. Therefore, $\nabla \times \mathbf{E} = 0$ allows us to define the electric scalar potential $V$, such that $\mathbf{E} = -\nabla V$. This vastly simplifies many electrostatic problems, reducing vector calculations to simpler scalar mathematics.

*(Related location: Book Page 93, 147-148 / PDF Page 118, 172-173)*

***

### Q.1. (d) A plane circular sheet of radius $a$ has a uniform charge density $\rho_s \text{ C/m}^2$ is placed on the xy plane at z=0 and is centered at the origin. Calculate $\vec{E}$ at P(0,0,h).

**Solution:**

We need to find the electric field at a point $P(0,0,h)$ on the z-axis due to a circular disk of radius $a$ in the xy-plane carrying a uniform surface charge density $\rho_s$. We will use Coulomb's law for a continuous surface charge distribution:
$$ \mathbf{E} = \int_S \frac{dQ}{4\pi\varepsilon_0 R^2} \mathbf{a}_R $$

We use cylindrical coordinates $(\rho, \phi, z)$ for the integration.
*   **Charge Element ($dQ$):** An elemental area on the disk is $dS = \rho \, d\rho \, d\phi$. The charge on this element is $dQ = \rho_s \, dS = \rho_s \rho \, d\rho \, d\phi$.
*   **Source Point:** The coordinates of the charge element on the disk are $(x, y, 0)$ or in cylindrical coordinates $(\rho, \phi, 0)$. The position vector is $\mathbf{r}' = \rho \mathbf{a}_\rho$.
*   **Field Point:** The point of interest $P$ is at $(0, 0, h)$. Its position vector is $\mathbf{r} = h \mathbf{a}_z$.
*   **Distance Vector ($\mathbf{R}$):** The vector from the source element to the field point is $\mathbf{R} = \mathbf{r} - \mathbf{r}' = h \mathbf{a}_z - \rho \mathbf{a}_\rho$.
*   **Magnitude Squared ($R^2$):** $R^2 = |\mathbf{R}|^2 = \rho^2 + h^2$.
*   **Unit Vector ($\mathbf{a}_R$):** $\mathbf{a}_R = \frac{\mathbf{R}}{R} = \frac{-\rho \mathbf{a}_\rho + h \mathbf{a}_z}{\sqrt{\rho^2 + h^2}}$.

Substituting these into the electric field integral:
$$ d\mathbf{E} = \frac{\rho_s \rho \, d\rho \, d\phi}{4\pi\varepsilon_0 (\rho^2 + h^2)} \left( \frac{-\rho \mathbf{a}_\rho + h \mathbf{a}_z}{\sqrt{\rho^2 + h^2}} \right) $$

Due to the circular symmetry of the disk, for every charge element at $(\rho, \phi, 0)$ producing a radial component $-dE_\rho \mathbf{a}_\rho$, there is an identical charge element diametrically opposite at $(\rho, \phi+\pi, 0)$ producing a radial component $+dE_\rho \mathbf{a}_\rho$. These horizontal components perfectly cancel each other out when integrated around the full circle ($0$ to $2\pi$). We can therefore ignore the $\mathbf{a}_\rho$ component and only integrate the $\mathbf{a}_z$ component.

$$ dE_z = \frac{\rho_s h \rho \, d\rho \, d\phi}{4\pi\varepsilon_0 (\rho^2 + h^2)^{3/2}} $$

Now, integrate over the entire surface of the disk ($\rho$ from $0$ to $a$, $\phi$ from $0$ to $2\pi$):
$$ E_z = \int_{\phi=0}^{2\pi} \int_{\rho=0}^{a} \frac{\rho_s h \rho}{4\pi\varepsilon_0 (\rho^2 + h^2)^{3/2}} d\rho \, d\phi $$
$$ E_z = \frac{\rho_s h}{4\pi\varepsilon_0} \left( \int_{0}^{2\pi} d\phi \right) \left( \int_{0}^{a} \rho (\rho^2 + h^2)^{-3/2} d\rho \right) $$
$$ E_z = \frac{\rho_s h}{4\pi\varepsilon_0} (2\pi) \int_{0}^{a} \rho (\rho^2 + h^2)^{-3/2} d\rho = \frac{\rho_s h}{2\varepsilon_0} \int_{0}^{a} \rho (\rho^2 + h^2)^{-3/2} d\rho $$

To evaluate the integral, let $u = \rho^2 + h^2$. Then $du = 2\rho \, d\rho \implies \rho \, d\rho = \frac{du}{2}$.
$$ \int \rho (\rho^2 + h^2)^{-3/2} d\rho = \int u^{-3/2} \frac{du}{2} = \frac{1}{2} \left[ \frac{u^{-1/2}}{-1/2} \right] = -u^{-1/2} = \frac{-1}{\sqrt{\rho^2 + h^2}} $$

Applying the limits from $0$ to $a$:
$$ E_z = \frac{\rho_s h}{2\varepsilon_0} \left[ \frac{-1}{\sqrt{\rho^2 + h^2}} \right]_0^a = \frac{\rho_s h}{2\varepsilon_0} \left( \frac{-1}{\sqrt{a^2 + h^2}} - \left( \frac{-1}{\sqrt{0^2 + h^2}} \right) \right) $$
$$ E_z = \frac{\rho_s h}{2\varepsilon_0} \left( \frac{1}{h} - \frac{1}{\sqrt{a^2 + h^2}} \right) = \frac{\rho_s}{2\varepsilon_0} \left( 1 - \frac{h}{\sqrt{a^2 + h^2}} \right) $$

Therefore, the total electric field intensity vector at point $P(0,0,h)$ is:
$$ \mathbf{E} = \frac{\rho_s}{2\varepsilon_0} \left( 1 - \frac{h}{\sqrt{a^2 + h^2}} \right) \mathbf{a}_z $$

*(Related location: Book Page 127, Practice Exercise 4.4 / PDF Page 152)*

***

### 🔴 Q.2. (a) What is electric dipole? Show the geometry of electric dipole and derive the expression of electric potential in terms of dipole moment.

**Solution:**

**What is an electric dipole?**
An electric dipole is formed when two point charges of exactly equal magnitude but opposite sign (i.e., $+Q$ and $-Q$) are separated by a very small distance $d$.

**Geometry of Electric Dipole:**
The standard geometry places the dipole centered at the origin of a spherical coordinate system.
*   Charge $+Q$ is located at the coordinates $(0, 0, d/2)$ on the positive z-axis.
*   Charge $-Q$ is located at the coordinates $(0, 0, -d/2)$ on the negative z-axis.
*   The dipole moment vector $\mathbf{p}$ is defined as $\mathbf{p} = Qd \mathbf{a}_z$, pointing from the negative charge to the positive charge.
*(Imagine a diagram with the z-axis vertical, an origin O, $+Q$ slightly above O, $-Q$ slightly below O, and a distant point P at distance $r$ from O, with angle $\theta$ between the z-axis and the line OP. Let $r_1$ be the distance from $+Q$ to P, and $r_2$ be the distance from $-Q$ to P.)*

**Derivation of Electric Potential:**
We wish to find the potential $V$ at an observation point $P(r, \theta, \phi)$. By the principle of superposition, the total potential at $P$ is the sum of the potentials from the individual charges:
$$ V = V_+ + V_- $$
$$ V = \frac{Q}{4\pi\varepsilon_0 r_1} + \frac{-Q}{4\pi\varepsilon_0 r_2} = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{1}{r_1} - \frac{1}{r_2} \right] $$
$$ V = \frac{Q}{4\pi\varepsilon_0} \left[ \frac{r_2 - r_1}{r_1 r_2} \right] $$

For a dipole, we are generally interested in the potential at a point $P$ where the distance $r$ is much much greater than the separation distance $d$ ($r \gg d$). 
In this far-field region, the lines representing $r_1$, $r$, and $r_2$ become essentially parallel to each other.
From the geometry, dropping a perpendicular from the $+Q$ position to the $r_2$ line shows that the path length difference is approximately:
$$ r_2 - r_1 \approx d \cos\theta $$
Also, the product of the distances in the denominator can be approximated as the square of the center distance:
$$ r_1 r_2 \approx r^2 $$

Substituting these far-field approximations back into the potential equation:
$$ V \approx \frac{Q}{4\pi\varepsilon_0} \left[ \frac{d \cos\theta}{r^2} \right] $$
$$ V = \frac{Qd \cos\theta}{4\pi\varepsilon_0 r^2} $$

We defined the magnitude of the dipole moment as $p = Qd$. Also, if we consider $\mathbf{p} = p\mathbf{a}_z$, and the radial unit vector $\mathbf{a}_r$, their dot product is $\mathbf{p} \cdot \mathbf{a}_r = p(\mathbf{a}_z \cdot \mathbf{a}_r) = p\cos\theta$.
Replacing $Qd\cos\theta$ with $\mathbf{p} \cdot \mathbf{a}_r$, we get the final general expression for the electric potential of a dipole:
$$ V = \frac{\mathbf{p} \cdot \mathbf{a}_r}{4\pi\varepsilon_0 r^2} $$

*(Related location: Book Page 150-151 / PDF Page 175-176)*

***

### Q.2. (b) A dipole moment $\mathbf{P} = -4\hat{a}_x + 5\hat{a}_y + 3\hat{a}_z \text{ nC-m}$ is located at D(1, 2, -1) in free space. Find V at (i) $P_A(1, 2, 0)$ and (ii) $P_B(r=2, \theta=40^\circ, \phi=50^\circ)$.

**Solution:**

The formula for the potential at an observation point $\mathbf{r}$ due to a dipole moment $\mathbf{p}$ located at a source point $\mathbf{r}'$ is:
$$ V(\mathbf{r}) = \frac{\mathbf{p} \cdot (\mathbf{r} - \mathbf{r}')}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r}'|^3} $$
Given:
*   Dipole moment $\mathbf{p} = (-4\mathbf{a}_x + 5\mathbf{a}_y + 3\mathbf{a}_z) \times 10^{-9}$ C-m
*   Source location $\mathbf{r}' = 1\mathbf{a}_x + 2\mathbf{a}_y - 1\mathbf{a}_z$
*   Let $\frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9$ m/F

**Part (i): Find V at $P_A(1, 2, 0)$**
*   Observation point $\mathbf{r}_A = 1\mathbf{a}_x + 2\mathbf{a}_y + 0\mathbf{a}_z$
*   Distance vector $\mathbf{R}_A = \mathbf{r}_A - \mathbf{r}' = (1 - 1)\mathbf{a}_x + (2 - 2)\mathbf{a}_y + (0 - (-1))\mathbf{a}_z = 1\mathbf{a}_z$
*   Magnitude $R_A = |\mathbf{R}_A| = \sqrt{0^2 + 0^2 + 1^2} = 1$ m
*   $R_A^3 = 1^3 = 1$
*   Dot product: $\mathbf{p} \cdot \mathbf{R}_A = [(-4\mathbf{a}_x + 5\mathbf{a}_y + 3\mathbf{a}_z) \cdot (1\mathbf{a}_z)] \times 10^{-9} = (3 \times 1) \times 10^{-9} = 3 \times 10^{-9}$

Calculate Potential $V_A$:
$$ V_A = (9 \times 10^9) \frac{3 \times 10^{-9}}{1} = 27 \text{ V} $$

**Part (ii): Find V at $P_B(r=2, \theta=40^\circ, \phi=50^\circ)$**
First, we must convert the observation point $P_B$ from spherical to Cartesian coordinates so we can subtract the vectors.
*   $x = r \sin\theta \cos\phi = 2 \sin(40^\circ) \cos(50^\circ) = 2 \times 0.6428 \times 0.6428 \approx 0.826$
*   $y = r \sin\theta \sin\phi = 2 \sin(40^\circ) \sin(50^\circ) = 2 \times 0.6428 \times 0.7660 \approx 0.985$
*   $z = r \cos\theta = 2 \cos(40^\circ) = 2 \times 0.7660 \approx 1.532$
*   Observation point $\mathbf{r}_B \approx 0.826\mathbf{a}_x + 0.985\mathbf{a}_y + 1.532\mathbf{a}_z$

*   Distance vector $\mathbf{R}_B = \mathbf{r}_B - \mathbf{r}'$:
    $\mathbf{R}_B = (0.826 - 1)\mathbf{a}_x + (0.985 - 2)\mathbf{a}_y + (1.532 - (-1))\mathbf{a}_z$
    $\mathbf{R}_B = -0.174\mathbf{a}_x - 1.015\mathbf{a}_y + 2.532\mathbf{a}_z$
*   Magnitude squared $R_B^2 = (-0.174)^2 + (-1.015)^2 + (2.532)^2 = 0.0303 + 1.0302 + 6.4110 \approx 7.4715$
*   Magnitude $R_B = \sqrt{7.4715} \approx 2.733$
*   $R_B^3 = (2.733)^3 \approx 20.42$
*   Dot product $\mathbf{p} \cdot \mathbf{R}_B$:
    $\mathbf{p} \cdot \mathbf{R}_B = [(-4)(-0.174) + (5)(-1.015) + (3)(2.532)] \times 10^{-9}$
    $\mathbf{p} \cdot \mathbf{R}_B = [0.696 - 5.075 + 7.596] \times 10^{-9} = 3.217 \times 10^{-9}$

Calculate Potential $V_B$:
$$ V_B = (9 \times 10^9) \frac{3.217 \times 10^{-9}}{20.42} = \frac{28.953}{20.42} \approx 1.418 \text{ V} $$

*(Related location: Book Page 151 (Equation 4.81) / PDF Page 176)*
### 🔴 Q.3 (a) State and explain Gauss' laws for electric and magnetic fields. Also, explain their physical meanings.

**Solution:**

Gauss's laws form half of Maxwell's fundamental equations of electromagnetism. They describe the relationship between flux and its sources.

**1. Gauss's Law for Electric Fields**

*   **Statement:** Gauss's law for electrostatics states that the total electric flux ($\Psi$) passing through any hypothetical closed surface (a Gaussian surface) is exactly equal to the total net electric charge ($Q_{enc}$) enclosed by that surface.
*   **Equations:**
    *   *Integral Form:* $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} = \int_v \rho_v \, dv$
    *   *Differential (Point) Form:* $\nabla \cdot \mathbf{D} = \rho_v$
        (where $\mathbf{D}$ is the electric flux density and $\rho_v$ is the volume charge density).
*   **Physical Meaning:** This law implies that electric charges act as distinct sources (if positive) or sinks (if negative) for electric field lines. Electric flux lines originate on positive charges and terminate on negative charges. If a closed volume contains a net positive charge, there will be a net outward flow of electric flux. If it contains no net charge, whatever flux enters the volume must exit it.

**2. Gauss's Law for Magnetic Fields**

*   **Statement:** Gauss's law for magnetostatics (also known as the law of conservation of magnetic flux) states that the total magnetic flux passing through any closed surface is always identically zero.
*   **Equations:**
    *   *Integral Form:* $\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$
    *   *Differential (Point) Form:* $\nabla \cdot \mathbf{B} = 0$
        (where $\mathbf{B}$ is the magnetic flux density).
*   **Physical Meaning:** This law fundamentally asserts the non-existence of isolated magnetic charges, or "magnetic monopoles." Unlike electric charges, you cannot isolate a "North" pole from a "South" pole. Because there are no isolated sources or sinks for magnetic fields, magnetic flux lines must always form continuous, closed loops. Therefore, for any closed surface you draw, the number of magnetic flux lines entering the surface must exactly equal the number of lines leaving it.

*(Related location: Book Page 132-133, 317-319 / PDF Page 157-158, 296-298)*

***

### 🔴 Q.3 (b) Show that $\nabla \cdot \bar{D} = \rho_v$.

**Solution:**

This equation is the differential (or point) form of Gauss's Law. It is derived directly from the integral form of Gauss's law using the Divergence Theorem.

1.  We begin with the integral form of Gauss's law, which relates the total electric flux through a closed surface $S$ to the total charge enclosed within the volume $v$ bounded by that surface:
    $$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$

2.  The total enclosed charge $Q_{enc}$ can be expressed as the volume integral of the volume charge density $\rho_v$ over the entire volume $v$:
    $$ Q_{enc} = \int_v \rho_v \, dv $$

3.  Equating the two expressions for the enclosed charge yields:
    $$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v \, dv $$

4.  Now, we apply the **Divergence Theorem** (also known as Gauss's theorem in vector calculus) to the left-hand side of the equation. The Divergence Theorem allows us to convert a closed surface integral of a vector field into a volume integral of the divergence of that vector field over the enclosed volume:
    $$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{D}) \, dv $$

5.  Substituting this back into the equation from step 3, we get:
    $$ \int_v (\nabla \cdot \mathbf{D}) \, dv = \int_v \rho_v \, dv $$
    $$ \int_v (\nabla \cdot \mathbf{D} - \rho_v) \, dv = 0 $$

6.  For this volume integral to evaluate to zero for *any* arbitrary volume $v$ we might choose to define, the integrand itself must be identically equal to zero at every point in space. 
    Therefore:
    $$ \nabla \cdot \mathbf{D} - \rho_v = 0 $$
    $$ \nabla \cdot \mathbf{D} = \rho_v $$

This completes the proof showing that the divergence of the electric flux density at a specific point is equal to the volume charge density at that same point.

*(Related location: Book Page 133 / PDF Page 158)*

***

### 🔴 Q.3 (c) Define absolute potential and hence derive an equation for absolute potential due to a point charge.

**Solution:**

**Definition of Absolute Potential:**
The absolute electric potential $V$ at a specific point in space is defined as the work done by an external agent in moving a unit positive test charge from a reference point of zero potential to that specific point against the electric field. By convention, the reference point where the potential is considered to be zero is chosen to be at infinity.

**Derivation for a Point Charge:**
The potential difference $V_{AB}$ between two points A and B is the work done per unit charge in moving from A to B:
$$ V_{AB} = V_B - V_A = -\int_A^B \mathbf{E} \cdot d\mathbf{l} $$

To find the absolute potential $V(r)$ at a radial distance $r$ from a point charge $Q$ located at the origin, we set our initial point A at infinity ($r = \infty$) where $V_A = V(\infty) = 0$, and our final point B at the distance $r$. 

1.  The setup is:
    $$ V(r) - V(\infty) = -\int_{\infty}^{r} \mathbf{E} \cdot d\mathbf{l} $$
    Since $V(\infty) = 0$, this simplifies to:
    $$ V(r) = -\int_{\infty}^{r} \mathbf{E} \cdot d\mathbf{l} $$

2.  From Coulomb's law, the electric field intensity $\mathbf{E}$ of a point charge $Q$ at the origin at a distance $r'$ is purely radial:
    $$ \mathbf{E} = \frac{Q}{4\pi\varepsilon_0 r'^2} \mathbf{a}_r $$

3.  Since we are moving the test charge radially inward from infinity to $r$, the differential path length vector $d\mathbf{l}$ is along the radial direction:
    $$ d\mathbf{l} = dr' \mathbf{a}_r $$

4.  Substituting $\mathbf{E}$ and $d\mathbf{l}$ into the integral:
    $$ V(r) = -\int_{\infty}^{r} \left( \frac{Q}{4\pi\varepsilon_0 r'^2} \mathbf{a}_r \right) \cdot (dr' \mathbf{a}_r) $$
    Since $\mathbf{a}_r \cdot \mathbf{a}_r = 1$, the dot product simplifies:
    $$ V(r) = -\int_{\infty}^{r} \frac{Q}{4\pi\varepsilon_0 r'^2} dr' $$

5.  Pulling the constants out of the integral:
    $$ V(r) = -\frac{Q}{4\pi\varepsilon_0} \int_{\infty}^{r} \frac{1}{r'^2} dr' $$
    $$ V(r) = -\frac{Q}{4\pi\varepsilon_0} \left[ -\frac{1}{r'} \right]_{\infty}^{r} $$

6.  Evaluating the integral at the limits:
    $$ V(r) = \frac{Q}{4\pi\varepsilon_0} \left( \frac{1}{r} - \frac{1}{\infty} \right) $$
    Since $1/\infty \to 0$, we arrive at the final equation:
    $$ V(r) = \frac{Q}{4\pi\varepsilon_0 r} $$

*(Related location: Book Page 141-143 / PDF Page 166-168)*

***

### 🔴 Q.4 (a) Determine the boundary conditions for electrostatic fields at the interface between a good conductor and a dielectric media with permittivity $\varepsilon$.

**Solution:**

To determine the behavior of electric fields at the boundary between a perfect conductor and a dielectric medium, we apply two fundamental electrostatic principles: the conservative nature of the electric field ($\oint \mathbf{E} \cdot d\mathbf{l} = 0$) and Gauss's law ($\oint \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$). 

A fundamental prerequisite is that under static conditions, **the electric field inside a perfect conductor is exactly zero** ($\mathbf{E}_{cond} = 0$, $\mathbf{D}_{cond} = 0$).

We decompose the field in the dielectric just outside the conductor into tangential ($\mathbf{E}_t$, $\mathbf{D}_t$) and normal ($\mathbf{E}_n$, $\mathbf{D}_n$) components relative to the boundary surface.

**1. Tangential Component:**
We apply the closed line integral $\oint \mathbf{E} \cdot d\mathbf{l} = 0$ to a very small rectangular loop intersecting the boundary. The top half of the loop is in the dielectric, and the bottom half is in the conductor. Let the width parallel to the boundary be $\Delta w$ and the height be $\Delta h$.
*   As we shrink the height of the loop to zero ($\Delta h \to 0$), the contributions from the vertical segments vanish.
*   We are left with the integral along the top path (in the dielectric) and the bottom path (in the conductor):
    $$ E_{t\_dielectric} \Delta w - E_{t\_conductor} \Delta w = 0 $$
*   Because the field inside the conductor is zero, $E_{t\_conductor} = 0$. Therefore:
    $$ E_{t\_dielectric} \Delta w = 0 $$
    $$ E_{t\_dielectric} = 0 $$
Since $\mathbf{D} = \varepsilon\mathbf{E}$, it also follows that $D_t = 0$.
**Conclusion 1:** The tangential electric field intensity and electric flux density must be zero just outside the conductor. The field must approach the conductor surface perfectly perpendicularly.

**2. Normal Component:**
We apply Gauss's law $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ to a small cylindrical "pillbox" Gaussian surface intersecting the boundary. The top face (area $\Delta S$) is in the dielectric, and the bottom face is in the conductor. Let the surface charge density on the conductor be $\rho_S$.
*   As the height of the pillbox approaches zero ($\Delta h \to 0$), the flux through the curved sides vanishes.
*   The total flux is the sum of the flux through the top and bottom faces.
    $$ \int_{top} \mathbf{D} \cdot d\mathbf{S} + \int_{bottom} \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
*   On the top face, the flux is $D_{n\_dielectric} \Delta S$. On the bottom face, $\mathbf{D}_{cond} = 0$, so the flux is zero.
*   The enclosed charge is $Q_{enc} = \rho_S \Delta S$.
    $$ D_{n\_dielectric} \Delta S - 0 = \rho_S \Delta S $$
    $$ D_{n\_dielectric} = \rho_S $$
Since $D_n = \varepsilon E_n$, we can write $E_n = \frac{\rho_S}{\varepsilon}$.
**Conclusion 2:** The normal component of the electric flux density just outside the conductor is equal to the surface charge density residing on the conductor.

**Summary of Boundary Conditions:**
*   $E_t = 0$
*   $D_t = 0$
*   $D_n = \rho_S$
*   $E_n = \frac{\rho_S}{\varepsilon}$

*(Related location: Book Page 201-202 / PDF Page 226-227)*

***

### 🔴 Q.4 (b) Explain the effect of static electric field on a conducting material in brief.

**Solution:**

A conducting material is distinct from an insulator because it contains a vast number of "free electrons" in its outermost atomic shells. These electrons are not bound to any specific nucleus and can migrate freely throughout the crystalline lattice of the material.

When an isolated conducting material is exposed to an external static electric field ($\mathbf{E}_e$):
1.  **Force and Migration:** The external field exerts an electrostatic force on the free electrons, given by $\mathbf{F} = -e\mathbf{E}_e$. Because they are free to move, the electrons are rapidly pushed in the direction opposite to the applied field lines.
2.  **Induced Surface Charge:** This massive migration of electrons causes a surplus of negative charge to accumulate on one side of the conductor's exterior surface and leaves a deficiency of electrons (a net positive charge) on the opposite surface.
3.  **Cancellation of Internal Field:** These newly established, separated surface charges generate their own internal "induced" electric field ($\mathbf{E}_i$). This induced field points from the positive surface charges to the negative surface charges, which is precisely the opposite direction of the original external field.
4.  **Electrostatic Equilibrium:** The charges will continue to move almost instantaneously until the induced internal field ($\mathbf{E}_i$) perfectly cancels out the external applied field ($\mathbf{E}_e$) everywhere inside the material.

**Resulting State:**
Once this electrostatic equilibrium is achieved (in fractions of a nanosecond), the following conditions hold true for the perfect conductor:
*   The net electric field inside the conductor is absolutely zero ($\mathbf{E}_{net} = \mathbf{E}_e + \mathbf{E}_i = 0$).
*   Consequently, the volume charge density inside the conductor must be zero ($\rho_v = 0$). All unbalanced charge resides exclusively on the outer surface.
*   Because $\mathbf{E} = 0$ internally, no work is required to move a charge between any two points within the conductor. Therefore, the entire volume of the conductor becomes an **equipotential body** (it is at a single, uniform voltage).

*(Related location: Book Page 181 / PDF Page 206)*

***

### Q.4 (c) Derive Poisson's and Laplace equation for electrostatics and explain their usefulness.

**Solution:**

**Derivation:**
Poisson's and Laplace's equations are derived by combining Gauss's law in point form with the relationship between electric field and potential.

1.  We start with the differential (point) form of Gauss's law, which relates electric flux density $\mathbf{D}$ to volume charge density $\rho_v$:
    $$ \nabla \cdot \mathbf{D} = \rho_v $$

2.  For a linear, isotropic, and homogeneous dielectric medium, the constitutive relation connects flux density to electric field intensity $\mathbf{E}$ via the permittivity $\varepsilon$:
    $$ \mathbf{D} = \varepsilon \mathbf{E} $$

3.  Substituting the constitutive relation into Gauss's law gives:
    $$ \nabla \cdot (\varepsilon \mathbf{E}) = \rho_v $$
    Assuming the medium is homogeneous, $\varepsilon$ is a constant and can be factored out of the divergence operator:
    $$ \varepsilon (\nabla \cdot \mathbf{E}) = \rho_v $$
    $$ \nabla \cdot \mathbf{E} = \frac{\rho_v}{\varepsilon} $$

4.  We know that an electrostatic field is conservative ($\nabla \times \mathbf{E} = 0$), which allows us to express the electric field intensity as the negative gradient of the scalar electric potential $V$:
    $$ \mathbf{E} = -\nabla V $$

5.  Substitute this potential relationship back into the modified Gauss's law:
    $$ \nabla \cdot (-\nabla V) = \frac{\rho_v}{\varepsilon} $$
    $$ \nabla \cdot \nabla V = -\frac{\rho_v}{\varepsilon} $$

6.  The operation "divergence of the gradient" ($\nabla \cdot \nabla$) is defined as the Laplacian operator, denoted by $\nabla^2$. Thus, we obtain **Poisson's Equation**:
    $$ \nabla^2 V = -\frac{\rho_v}{\varepsilon} $$

7.  **Laplace's Equation** is simply a special case of Poisson's equation. If we are analyzing a region of space that is charge-free (meaning there is no volume charge density, $\rho_v = 0$), the right-hand side of Poisson's equation becomes zero. This yields:
    $$ \nabla^2 V = 0 $$

**Usefulness:**
Maxwell's equations (like Gauss's law) or Coulomb's law are straightforward to use when the complete charge distribution in a region is known. However, in most practical engineering scenarios (like designing capacitors, electron guns, or transmission lines), the charge distribution is *not* known. Instead, we know the boundary conditions—specifically, the potentials (voltages) applied to conducting surfaces.

Poisson's and Laplace's equations are immensely useful because they transform complex vector electrostatic problems into scalar boundary-value problems. 
By solving these second-order partial differential equations (usually via methods like separation of variables or numerical techniques) subject to the known voltage boundaries, an engineer can determine the potential $V$ everywhere in the space. 
Once the scalar field $V$ is found, the vector electric field $\mathbf{E}$ can be easily computed via $\mathbf{E} = -\nabla V$, and from there, parameters like charge distribution (using $\rho_S = D_n$), capacitance, and forces can be fully determined.

*(Related location: Presentation Slides Page 195-196 / Book Page 225-226)*
### 🔴 Q.1 (a) State and explain Gauss' law for electrostatics, and hence show that $\nabla \cdot \mathbf{D} = \rho_v$, where the symbols have their usual meaning.

**Solution:**

**State and Explain Gauss's Law:**
Gauss’s law is a fundamental principle of electromagnetism that relates the distribution of electric charge to the resulting electric field. 

It states that the total electric flux ($\Psi$) passing outward through any hypothetical closed surface (called a Gaussian surface) is exactly equal to the total net electric charge ($Q_{enc}$) enclosed within the volume bounded by that surface.

Mathematically, the integral form of Gauss's law is written as:
$$ \Psi = \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} $$
where:
*   $\mathbf{D}$ is the electric flux density vector (measured in C/m$^2$).
*   $d\mathbf{S}$ is the differential surface area vector, pointing normally outward from the closed surface $S$.
*   $Q_{enc}$ is the total net charge enclosed by surface $S$.

Physical meaning: This law implies that electric charges are the sources (if positive) and sinks (if negative) of the electric flux lines. The net number of flux lines passing out of a closed boundary is entirely determined by how much net charge is trapped inside. Charges outside the closed surface do not contribute to the net flux, as any field line from an external charge that enters the volume must also exit it.

**Derivation of $\nabla \cdot \mathbf{D} = \rho_v$:**
We begin with the integral form of Gauss's law:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc} \quad \text{--- (Equation 1)} $$

The total charge enclosed, $Q_{enc}$, can also be expressed as the volume integral of the volume charge density $\rho_v$ over the entire volume $v$ that is enclosed by the surface $S$:
$$ Q_{enc} = \int_v \rho_v \, dv \quad \text{--- (Equation 2)} $$

Equating Equation 1 and Equation 2 gives:
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v \, dv \quad \text{--- (Equation 3)} $$

Now, we apply the Divergence Theorem to the left side of Equation 3. The Divergence Theorem allows us to convert the closed surface integral of a vector field ($\mathbf{D}$) into a volume integral of the divergence of that vector field ($\nabla \cdot \mathbf{D}$):
$$ \oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{D}) \, dv $$

Substituting this back into Equation 3 yields:
$$ \int_v (\nabla \cdot \mathbf{D}) \, dv = \int_v \rho_v \, dv $$

This equality must hold true for *any* arbitrarily chosen volume $v$. The only way two volume integrals can be identical for every possible volume is if their integrands are identically equal at every point in space. 

Therefore, equating the integrands gives the differential (or point) form of Gauss's law:
$$ \nabla \cdot \mathbf{D} = \rho_v $$
This shows that the divergence of the electric flux density at a point is exactly equal to the volume charge density at that point.

*(Related location: Book Page 132-133 / PDF Page 157-158)*

***

### Q.1 (b) How is electric field intensity, E related with electric flux density, D? When a fluorescent lamp glows with full brightness, it is filled with electric charges. If the charged lamp is approximated by a line charge density with $\rho_L \text{ C/m}$ and placed along y-axis as shown in the figure below, find the expression of E at the point P and show that the result approaches $\mathbf{E} = \frac{\rho_L}{2\pi\varepsilon h}\mathbf{a}_z$ as L approaches to infinity.

**Solution:**

**Relationship between $\mathbf{E}$ and $\mathbf{D}$:**
The electric flux density $\mathbf{D}$ and the electric field intensity $\mathbf{E}$ are related by the constitutive parameter of the medium in which the fields exist, known as the permittivity ($\varepsilon$). For a linear, isotropic, and homogeneous medium, the relationship is linear:
$$ \mathbf{D} = \varepsilon \mathbf{E} $$
In free space, $\varepsilon = \varepsilon_0$, so $\mathbf{D} = \varepsilon_0 \mathbf{E}$.

**Finding the expression for $\mathbf{E}$ at point P:**
The lamp is modeled as a line charge with uniform density $\rho_L$ located on the y-axis, extending from $y = -L/2$ to $y = L/2$. We want to find the electric field at point $P(0, 0, h)$ on the z-axis.

1.  **Define the differential elements:**
    Consider an infinitesimally small segment of the line charge $dy$ located at an arbitrary position $y$ on the y-axis. The coordinates of this source element are $(0, y, 0)$.
    The amount of charge on this element is $dQ = \rho_L dy$.

2.  **Determine distance vectors:**
    The position vector of the source element is $\mathbf{r}' = y\mathbf{a}_y$.
    The position vector of the observation point $P$ is $\mathbf{r} = h\mathbf{a}_z$.
    The distance vector $\mathbf{R}$ pointing from the source element to point $P$ is:
    $$ \mathbf{R} = \mathbf{r} - \mathbf{r}' = h\mathbf{a}_z - y\mathbf{a}_y $$
    The magnitude of the distance vector is:
    $$ R = |\mathbf{R}| = \sqrt{h^2 + y^2} $$
    The unit vector in the direction of $\mathbf{R}$ is:
    $$ \mathbf{a}_R = \frac{\mathbf{R}}{R} = \frac{h\mathbf{a}_z - y\mathbf{a}_y}{\sqrt{h^2 + y^2}} $$

3.  **Apply Coulomb's law for the differential field $d\mathbf{E}$:**
    The differential electric field $d\mathbf{E}$ at $P$ due to the charge element $dQ$ is:
    $$ d\mathbf{E} = \frac{dQ}{4\pi\varepsilon R^2} \mathbf{a}_R = \frac{\rho_L dy}{4\pi\varepsilon (h^2 + y^2)} \left( \frac{h\mathbf{a}_z - y\mathbf{a}_y}{\sqrt{h^2 + y^2}} \right) $$
    $$ d\mathbf{E} = \frac{\rho_L (h\mathbf{a}_z - y\mathbf{a}_y)}{4\pi\varepsilon (h^2 + y^2)^{3/2}} dy $$

4.  **Integrate over the length of the line:**
    To find the total field $\mathbf{E}$, we integrate $d\mathbf{E}$ from $y = -L/2$ to $y = L/2$:
    $$ \mathbf{E} = \int_{-L/2}^{L/2} \frac{\rho_L h \mathbf{a}_z}{4\pi\varepsilon (h^2 + y^2)^{3/2}} dy - \int_{-L/2}^{L/2} \frac{\rho_L y \mathbf{a}_y}{4\pi\varepsilon (h^2 + y^2)^{3/2}} dy $$

    *   **Symmetry argument:** Notice the second integral involving the $y$-component. The integrand contains $y/(h^2+y^2)^{3/2}$, which is an odd function. Integrating an odd function over symmetric limits ($-L/2$ to $L/2$) yields zero. Physically, this means the $y$-component of the field from a charge element at $+y$ exactly cancels the $y$-component from a corresponding charge element at $-y$. 
    Thus, the $\mathbf{a}_y$ component vanishes.

    *   We are left only with the $z$-component, whose integrand is an even function:
    $$ \mathbf{E} = \mathbf{a}_z \int_{-L/2}^{L/2} \frac{\rho_L h}{4\pi\varepsilon (h^2 + y^2)^{3/2}} dy = \mathbf{a}_z \frac{2\rho_L h}{4\pi\varepsilon} \int_{0}^{L/2} \frac{dy}{(h^2 + y^2)^{3/2}} $$
    $$ \mathbf{E} = \frac{\rho_L h}{2\pi\varepsilon} \left[ \frac{y}{h^2\sqrt{h^2 + y^2}} \right]_0^{L/2} \mathbf{a}_z $$
    Evaluate at the limits:
    $$ \mathbf{E} = \frac{\rho_L h}{2\pi\varepsilon h^2} \left[ \frac{L/2}{\sqrt{h^2 + (L/2)^2}} - 0 \right] \mathbf{a}_z $$
    $$ \mathbf{E} = \frac{\rho_L}{2\pi\varepsilon h} \frac{L/2}{\sqrt{h^2 + (L/2)^2}} \mathbf{a}_z $$
    This is the expression for $\mathbf{E}$ at point $P$ for a finite line charge of length $L$.

**Showing the limit as $L$ approaches infinity:**
To model an infinitely long fluorescent lamp, we take the limit of the derived expression as $L \to \infty$:
$$ \lim_{L \to \infty} \mathbf{E} = \lim_{L \to \infty} \left[ \frac{\rho_L}{2\pi\varepsilon h} \frac{L/2}{\sqrt{h^2 + (L/2)^2}} \mathbf{a}_z \right] $$
Divide numerator and denominator of the term inside the limit by $L/2$:
$$ \lim_{L \to \infty} \mathbf{E} = \frac{\rho_L}{2\pi\varepsilon h} \mathbf{a}_z \lim_{L \to \infty} \left[ \frac{1}{\sqrt{\frac{h^2}{(L/2)^2} + 1}} \right] $$
As $L \to \infty$, the term $\frac{h^2}{(L/2)^2}$ approaches $0$. The expression inside the limit bracket becomes $\frac{1}{\sqrt{0 + 1}} = 1$.

Therefore, the result simplifies to:
$$ \mathbf{E} = \frac{\rho_L}{2\pi\varepsilon h} \mathbf{a}_z $$
This confirms that as the line becomes infinitely long, the electric field intensity matches the standard formula for an infinite line charge.

*(Related location: Relation D and E: Book Page 130 / PDF Page 155; Line charge derivation: Book Page 120-121 / PDF Page 145-146, also see example on PDF Page 556)*

***

### Q.1 (c) The cylindrical surface $\rho = 8$ contains surface density, $\rho_S = 5e^{-20z} \text{ nC/m}^2$. How much electric flux leaves the surface $\rho = 8, 1\text{cm} < z < 5\text{cm}, 30^\circ < \phi < 90^\circ$?

**Solution:**

The total electric flux $\Psi$ leaving a given surface $S$ is defined by the surface integral of the electric flux density $\mathbf{D}$:
$$ \Psi = \int_S \mathbf{D} \cdot d\mathbf{S} $$

From the boundary conditions for electrostatic fields, we know that the normal component of the electric flux density exiting a surface carrying a surface charge density $\rho_S$ is exactly equal to that charge density:
$$ D_n = \rho_S $$
Since the surface is a cylinder at constant $\rho=8$, the outward normal direction is the radial direction $\mathbf{a}_\rho$. Therefore, on this specific surface, the radial component of the flux density is $D_\rho = \rho_S = 5e^{-20z} \text{ nC/m}^2$.
$$ \mathbf{D} \cdot d\mathbf{S} = (D_\rho \mathbf{a}_\rho) \cdot (dS \mathbf{a}_\rho) = D_\rho dS = \rho_S dS $$
Thus, integrating the flux density over the surface is mathematically equivalent to integrating the surface charge density over the surface to find the total charge, which by Gauss's law equals the flux leaving that surface:
$$ \Psi = \int_S \rho_S \, dS $$

In cylindrical coordinates, the differential surface area element on a cylinder of constant radius $\rho$ is:
$$ dS = \rho \, d\phi \, dz $$

We are given the following surface limits (assuming standard SI base unit of meters for coordinates lacking units in equations, while explicitly converting the provided cm limits):
*   Radius $\rho = 8$
*   Height $z$ ranges from $1\text{ cm}$ to $5\text{ cm}$. In meters, this is $0.01\text{ m}$ to $0.05\text{ m}$.
*   Angle $\phi$ ranges from $30^\circ$ to $90^\circ$. In radians, this is $\frac{\pi}{6}$ to $\frac{\pi}{2}$.

Set up the double integral for the flux $\Psi$:
$$ \Psi = \int_{z=0.01}^{0.05} \int_{\phi=\pi/6}^{\pi/2} (5 \times 10^{-9} e^{-20z}) (\rho \, d\phi \, dz) $$
Substitute $\rho = 8$ into the integral:
$$ \Psi = \int_{0.01}^{0.05} \int_{\pi/6}^{\pi/2} 5 \times 10^{-9} \cdot e^{-20z} \cdot 8 \, d\phi \, dz $$
Pull constants out of the integral:
$$ \Psi = 40 \times 10^{-9} \left( \int_{\pi/6}^{\pi/2} d\phi \right) \left( \int_{0.01}^{0.05} e^{-20z} dz \right) $$

Evaluate the $\phi$ integral:
$$ \int_{\pi/6}^{\pi/2} d\phi = [\phi]_{\pi/6}^{\pi/2} = \frac{\pi}{2} - \frac{\pi}{6} = \frac{3\pi}{6} - \frac{\pi}{6} = \frac{2\pi}{6} = \frac{\pi}{3} $$

Evaluate the $z$ integral:
$$ \int_{0.01}^{0.05} e^{-20z} dz = \left[ \frac{e^{-20z}}{-20} \right]_{0.01}^{0.05} = \frac{e^{-20(0.05)} - e^{-20(0.01)}}{-20} $$
$$ = \frac{e^{-1.0} - e^{-0.2}}{-20} $$
Calculate numerical values for the exponential terms:
$$ e^{-1.0} \approx 0.36788 $$
$$ e^{-0.2} \approx 0.81873 $$
$$ \text{Integral value} = \frac{0.36788 - 0.81873}{-20} = \frac{-0.45085}{-20} = 0.0225425 $$

Combine the results to find total flux $\Psi$:
$$ \Psi = (40 \times 10^{-9}) \times \left( \frac{\pi}{3} \right) \times (0.0225425) $$
$$ \Psi = (40 \times 10^{-9}) \times (1.0472) \times (0.0225425) $$
$$ \Psi \approx 0.9443 \times 10^{-9} \text{ C} $$

The total electric flux leaving the specified section of the cylindrical surface is **$0.944 \text{ nC}$**.

*(Related location: Book Page 131, 200 / PDF Page 156, 225)*

***

### Q.2 (a) Derive the expression of capacitance, $C$ of two parallel plate of each having area, $S$ separated by the distance, $d$ and permittivity of the medium between the plates is $\varepsilon$.

**Solution:**

Consider a parallel-plate capacitor consisting of two very large conductive plates, each with surface area $S$, separated by a small distance $d$. The space between the plates is filled with a homogeneous dielectric medium having permittivity $\varepsilon$. 

To derive the capacitance, we will establish a potential difference $V_0$ between the plates, find the resulting electric field $\mathbf{E}$, calculate the total charge $Q$ on the plates, and then use the definition of capacitance $C = Q/V_0$.

1.  **Set up Coordinates and Boundary Conditions:**
    Let the lower plate be located in the $z = 0$ plane and the upper plate in the $z = d$ plane. 
    Assume the lower plate is grounded ($V = 0$ at $z=0$) and the upper plate is maintained at a positive potential $V_0$ ($V = V_0$ at $z=d$).
    Because the plates are assumed to be very large compared to $d$, we ignore fringing effects at the edges. This means the electric field between the plates will be uniform and directed entirely along the z-axis.

2.  **Determine Potential $V(z)$:**
    In the charge-free dielectric region between the plates ($\rho_v = 0$), the electric potential satisfies Laplace's equation:
    $$ \nabla^2 V = 0 $$
    Since $V$ only varies in the z-direction, this reduces to a simple ordinary differential equation:
    $$ \frac{d^2 V}{dz^2} = 0 $$
    Integrating twice yields the general solution:
    $$ V(z) = Az + B $$
    Apply boundary conditions to find constants A and B:
    *   At $z = 0, V = 0 \implies 0 = A(0) + B \implies B = 0$
    *   At $z = d, V = V_0 \implies V_0 = A(d) + 0 \implies A = V_0 / d$
    So, the potential function between the plates is:
    $$ V(z) = \frac{V_0}{d} z $$

3.  **Determine Electric Field $\mathbf{E}$ and Flux Density $\mathbf{D}$:**
    The electric field intensity is the negative gradient of the potential:
    $$ \mathbf{E} = -\nabla V = -\frac{dV}{dz} \mathbf{a}_z = -\frac{V_0}{d} \mathbf{a}_z $$
    The electric flux density is related to $\mathbf{E}$ by the permittivity of the medium:
    $$ \mathbf{D} = \varepsilon \mathbf{E} = -\frac{\varepsilon V_0}{d} \mathbf{a}_z $$

4.  **Calculate the Charge $Q$ on the Plates:**
    The boundary condition at the surface of a perfect conductor states that the normal component of $\mathbf{D}$ evaluates to the surface charge density $\rho_S$.
    Let's look at the lower plate at $z=0$. The outward normal from the conductor into the dielectric is $+\mathbf{a}_z$. 
    However, the charge $Q$ used in the capacitance formula usually refers to the positive plate. Let's look at the upper plate at $z=d$. The outward normal from this conductor into the dielectric is $-\mathbf{a}_z$.
    $$ \rho_S \text{ (on upper plate)} = \mathbf{D} \cdot \mathbf{a}_n = \left(-\frac{\varepsilon V_0}{d} \mathbf{a}_z\right) \cdot (-\mathbf{a}_z) = \frac{\varepsilon V_0}{d} $$
    Assuming uniform charge distribution over the area $S$, the total magnitude of charge $Q$ on the positive plate is:
    $$ Q = \int_S \rho_S \, dS = \rho_S \cdot S = \frac{\varepsilon V_0 S}{d} $$

5.  **Calculate Capacitance $C$:**
    Capacitance is defined as the ratio of the magnitude of charge on one plate to the potential difference between the plates:
    $$ C = \frac{Q}{V_0} = \frac{\left( \frac{\varepsilon V_0 S}{d} \right)}{V_0} $$
    $$ C = \frac{\varepsilon S}{d} $$

This is the standard expression for the capacitance of a parallel-plate capacitor.

*(Related location: Book Page 263 / PDF Page 242)*

***

### 🔴 Q.2 (b) Show that the energy stored in an electrostatic field can be calculated by using the equation $W_E = \int_{vol} \frac{1}{2} \varepsilon |\mathbf{E}|^2 dv$.

*(Note: The prompt image contains a slight typo, omitting the factor of $\frac{1}{2}$. The physical derivation below yields the correct standard formula, $W_E = \frac{1}{2} \int \varepsilon |\mathbf{E}|^2 dv$)*

**Solution:**

To determine the energy present in a continuous volume charge distribution $\rho_v$, we analyze the work required to assemble that charge configuration. The total potential energy $W_E$ stored in the system is given by the integral over the volume $v$ of half the product of the charge density and the potential $V$ at each point:
$$ W_E = \frac{1}{2} \int_v \rho_v V \, dv $$
(The factor of 1/2 ensures we do not double-count the interactive energy between charge pairs).

Our goal is to express this energy purely in terms of electric field quantities rather than charge and potential. 

1.  From the differential form of Gauss's law, we can replace the volume charge density $\rho_v$ with the divergence of the electric flux density $\mathbf{D}$:
    $$ \rho_v = \nabla \cdot \mathbf{D} $$
    Substituting this into the energy integral gives:
    $$ W_E = \frac{1}{2} \int_v (\nabla \cdot \mathbf{D}) V \, dv $$

2.  We apply a standard vector identity to expand the integrand. The divergence of the product of a scalar $V$ and a vector $\mathbf{D}$ is:
    $$ \nabla \cdot (V\mathbf{D}) = V(\nabla \cdot \mathbf{D}) + \mathbf{D} \cdot (\nabla V) $$
    Rearranging this identity to isolate the term matching our integrand:
    $$ V(\nabla \cdot \mathbf{D}) = \nabla \cdot (V\mathbf{D}) - \mathbf{D} \cdot (\nabla V) $$

3.  Substitute this reorganized identity back into the energy integral:
    $$ W_E = \frac{1}{2} \int_v [\nabla \cdot (V\mathbf{D}) - \mathbf{D} \cdot (\nabla V)] \, dv $$
    We can split this into two separate volume integrals:
    $$ W_E = \frac{1}{2} \int_v \nabla \cdot (V\mathbf{D}) \, dv - \frac{1}{2} \int_v \mathbf{D} \cdot (\nabla V) \, dv $$

4.  Apply the **Divergence Theorem** to the first integral. This theorem converts the volume integral of a divergence into a closed surface integral over surface $S$ that bounds volume $v$:
    $$ \int_v \nabla \cdot (V\mathbf{D}) \, dv = \oint_S (V\mathbf{D}) \cdot d\mathbf{S} $$
    To find the total energy stored in the entire field, the volume $v$ must encompass all of space, meaning the bounding surface $S$ must be expanded to infinity ($r \to \infty$).
    For any localized finite charge distribution, as distance $r \to \infty$:
    *   Potential $V$ drops off at least as fast as $1/r$.
    *   Flux density $\mathbf{D}$ drops off at least as fast as $1/r^2$.
    *   The surface area $dS$ increases as $r^2$.
    Consequently, the product $(V\mathbf{D}) \cdot d\mathbf{S}$ behaves proportionally to $\frac{1}{r} \cdot \frac{1}{r^2} \cdot r^2 = \frac{1}{r}$. As $r \to \infty$, this term approaches zero.
    Therefore, the surface integral vanishes over a surface at infinity:
    $$ \oint_S (V\mathbf{D}) \cdot d\mathbf{S} = 0 $$

5.  This leaves only the second volume integral for the total energy:
    $$ W_E = -\frac{1}{2} \int_v \mathbf{D} \cdot (\nabla V) \, dv $$

6.  We know that the electric field intensity $\mathbf{E}$ is the negative gradient of the potential ($\mathbf{E} = -\nabla V$). Substitute this into the equation:
    $$ W_E = \frac{1}{2} \int_v \mathbf{D} \cdot \mathbf{E} \, dv $$

7.  Finally, use the constitutive relationship for a linear, isotropic medium, $\mathbf{D} = \varepsilon\mathbf{E}$:
    $$ W_E = \frac{1}{2} \int_v (\varepsilon\mathbf{E}) \cdot \mathbf{E} \, dv $$
    Since the dot product of a vector with itself is the square of its magnitude ($\mathbf{E} \cdot \mathbf{E} = |\mathbf{E}|^2 = E^2$), the final expression is:
    $$ W_E = \int_{vol} \frac{1}{2} \varepsilon |\mathbf{E}|^2 \, dv $$

This demonstrates that the electrostatic energy can be viewed as being stored directly in the electric field distributed throughout the volume.

*(Related location: Book Page 155-156 / PDF Page 180-181)*

### (c) Does the potential $\phi = \frac{1}{r}$ satisfy Laplace's equation, where $r = (x^2+y^2+z^2)^{1/2}$?

**Solution:**

Laplace's equation states that the Laplacian of the potential must be zero: $\nabla^2 \phi = 0$. We must evaluate this for the given potential function $\phi = \frac{1}{r}$.
While this can be solved in Cartesian coordinates (by substituting $r = \sqrt{x^2+y^2+z^2}$ and taking partial derivatives with respect to $x, y$, and $z$), it is much more straightforward to evaluate the Laplacian in spherical coordinates since the potential depends *only* on the radial distance $r$.

The Laplacian operator for a scalar field $V$ in spherical coordinates is given by:
$$ \nabla^2 V = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial V}{\partial r}\right) + \frac{1}{r^2 \sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial V}{\partial \theta}\right) + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2 V}{\partial \phi^2} $$

For our specific potential function $\phi = \frac{1}{r}$, the function is independent of the angular variables $\theta$ and $\phi$. Therefore, the partial derivatives with respect to $\theta$ and $\phi$ are zero:
$$ \frac{\partial \phi}{\partial \theta} = 0 \quad \text{and} \quad \frac{\partial \phi}{\partial \phi} = 0 $$

The Laplacian expression simplifies to just the radial term:
$$ \nabla^2 \phi = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial \phi}{\partial r}\right) $$

Now, substitute $\phi = \frac{1}{r} = r^{-1}$ into the equation:
1.  Take the first derivative with respect to $r$:
    $$ \frac{\partial \phi}{\partial r} = \frac{\partial}{\partial r}(r^{-1}) = -1 \cdot r^{-2} = -\frac{1}{r^2} $$
2.  Multiply this result by $r^2$:
    $$ r^2 \frac{\partial \phi}{\partial r} = r^2 \left( -\frac{1}{r^2} \right) = -1 $$
3.  Take the derivative of this product with respect to $r$:
    $$ \frac{\partial}{\partial r} \left( r^2 \frac{\partial \phi}{\partial r} \right) = \frac{\partial}{\partial r}(-1) = 0 $$
4.  Finally, multiply by $\frac{1}{r^2}$:
    $$ \nabla^2 \phi = \frac{1}{r^2} (0) = 0 $$

Since $\nabla^2 \phi = 0$ everywhere (except at the singularity $r=0$, where the point charge resides), we conclude that **Yes, the potential $\phi = \frac{1}{r}$ satisfies Laplace's equation** in a charge-free region.

*(Related location: Book Page 90, 558 / PDF Page 115, 558)*

***

### 🔴 Q.3 (a) Define boundary conditions. Explain the boundary conditions for (i) dielectric-dielectric and (ii) dielectric-conductor interfaces.

**Solution:**

**Definition of Boundary Conditions:**
When an electromagnetic field exists in a region comprising two different media, the fields undergo changes at the interface separating the materials. The mathematical rules that govern how the electric ($\mathbf{E}$, $\mathbf{D}$) and magnetic ($\mathbf{H}$, $\mathbf{B}$) field vectors transition from one medium across the interface to the other are called **boundary conditions**. They are derived by applying the integral forms of Maxwell's equations (specifically, $\oint \mathbf{E} \cdot d\mathbf{l} = 0$ for tangential components and $\oint \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ for normal components) to an infinitesimally small loop and a pillbox spanning the boundary.

**Explanation of Specific Interface Conditions:**

**(i) Dielectric-Dielectric Interface:**
Consider the boundary between two ideal dielectric materials characterized by permittivities $\varepsilon_1$ and $\varepsilon_2$.
*   **Tangential Components:** The tangential component of the electric field intensity $\mathbf{E}$ is continuous across the boundary. This means the field strength along the surface is the same on both sides.
    $$ E_{1t} = E_{2t} $$
    Because $\mathbf{D} = \varepsilon\mathbf{E}$, the tangential component of the electric flux density $\mathbf{D}$ undergoes a change (it is discontinuous) proportional to the ratio of the permittivities:
    $$ \frac{D_{1t}}{\varepsilon_1} = \frac{D_{2t}}{\varepsilon_2} $$
*   **Normal Components:** If we assume there are no deliberately placed free charges on the boundary surface between the two dielectrics (surface charge density $\rho_S = 0$), then the normal component of the electric flux density $\mathbf{D}$ is continuous across the interface.
    $$ D_{1n} = D_{2n} $$
    Consequently, the normal component of the electric field intensity $\mathbf{E}$ is discontinuous:
    $$ \varepsilon_1 E_{1n} = \varepsilon_2 E_{2n} $$

**(ii) Conductor-Dielectric (Free Space) Interface:**
Consider a boundary separating a perfect conductor and a dielectric (or free space, where $\varepsilon = \varepsilon_0$). A fundamental property of a perfect conductor under static conditions is that the electric field inside it must be exactly zero ($\mathbf{E}_{cond} = 0$, $\mathbf{D}_{cond} = 0$).
*   **Tangential Components:** Since the electric field inside the conductor is zero, and the tangential electric field must be continuous across any boundary ($E_{t\_dielectric} = E_{t\_cond}$), it follows that the tangential electric field just outside the conductor must also be zero.
    $$ E_{t} = 0 \quad \text{and} \quad D_{t} = 0 $$
    This implies that the electric field must always strike a conducting surface perfectly perpendicularly (normal to the surface).
*   **Normal Components:** Because the field inside is zero, all the electric flux must originate or terminate on the surface charges residing on the conductor boundary. Applying Gauss's law shows that the normal component of the electric flux density $\mathbf{D}$ just outside the conductor is exactly equal to the surface charge density $\rho_S$ on the conductor.
    $$ D_n = \rho_S \quad \text{and} \quad E_n = \frac{\rho_S}{\varepsilon} $$

*(Related location: Book Page 198-203 / PDF Page 223-228)*

***

### Q.3 (b) Define conduction current density. Prove that $\mathbf{J} = \sigma \mathbf{E}$.

**Solution:**

**Definition of Conduction Current Density:**
Conduction current density ($\mathbf{J}$) is a vector quantity that represents the electric current flowing per unit cross-sectional area through a conducting material. It is caused by the drift motion of numerous free electrons (or other charge carriers) moving through the atomic lattice of the conductor under the influence of an externally applied electric field. 

**Proof of $\mathbf{J} = \sigma \mathbf{E}$:**
1.  When an external electric field $\mathbf{E}$ is applied to a conductor, a free electron with charge $-e$ experiences an electrostatic force $\mathbf{F}$ given by:
    $$ \mathbf{F} = -e\mathbf{E} $$
2.  If the electron were in free space, this force would cause constant acceleration. However, inside a conductor, the electron suffers continuous collisions with the fixed atomic lattice. These collisions impede its progress, resulting in a constant average velocity called the **drift velocity**, $\mathbf{u}$.
3.  According to Newton's second law, the average change in momentum of the free electron must balance the applied electric force. Let $m$ be the mass of the electron and $\tau$ be the mean time interval between collisions. The average acceleration can be represented as $\mathbf{u}/\tau$.
    $$ m \frac{\mathbf{u}}{\tau} = -e\mathbf{E} $$
4.  Rearranging this equation gives the expression for the drift velocity:
    $$ \mathbf{u} = -\frac{e\tau}{m} \mathbf{E} $$
    This shows that the drift velocity is directly proportional to the applied electric field.
5.  If the conductor contains $n$ free electrons per unit volume, the volume charge density contributed by these mobile electrons is:
    $$ \rho_v = -ne $$
6.  The fundamental definition of current density for moving charges is the product of the volume charge density and their velocity:
    $$ \mathbf{J} = \rho_v \mathbf{u} $$
7.  Substitute the expressions for $\rho_v$ and $\mathbf{u}$ into the current density equation:
    $$ \mathbf{J} = (-ne) \left( -\frac{e\tau}{m} \mathbf{E} \right) $$
    $$ \mathbf{J} = \left( \frac{ne^2\tau}{m} \right) \mathbf{E} $$
8.  The term in the parentheses is a macroscopic material property representing how easily the material allows electrons to flow. We define this constant term as the **conductivity** of the conductor, denoted by the symbol $\sigma$:
    $$ \sigma = \frac{ne^2\tau}{m} $$
9.  Substituting $\sigma$ back into the equation yields the point form of Ohm's law:
    $$ \mathbf{J} = \sigma \mathbf{E} $$
This proves that in a linear, isotropic conducting material, the conduction current density is directly proportional to the applied electric field intensity.

*(Related location: Book Page 180 / PDF Page 205)*

***

### Q.3 (c) Einstein's theory of relativity stipulates that the work required to assemble a charge is stored as energy in the mass and is equal to $mc^2$, where $m$ is the mass, and $c \cong 3 \times 10^8$ m/s is the velocity of light. Assume the electron to be a perfect sphere, find its radius from its charge and mass ($9.1 \times 10^{-31}$ kg).

**Solution:**

This problem asks us to determine the "classical electron radius" by equating the rest mass energy of the electron (given by Einstein's mass-energy equivalence, $E=mc^2$) to the electrostatic potential energy required to assemble the electron's charge into a perfect sphere. 

Let's assume the electron is modeled as a spherical shell of radius $a$ where all its charge $Q$ is uniformly distributed on its surface. The work done (electrostatic energy $W_E$) to assemble this surface charge configuration is equal to the energy stored in the electric field it produces.

1.  **Calculate the Electrostatic Energy ($W_E$):**
    For a spherical shell of charge $Q$ and radius $a$, the electric field inside the sphere ($r < a$) is zero. The electric field exists only outside the sphere ($r > a$) and is given by Coulomb's law:
    $$ \mathbf{E} = \frac{Q}{4\pi\varepsilon_0 r^2} \mathbf{a}_r $$
    The total electrostatic energy stored in this field is the volume integral over all space outside the sphere:
    $$ W_E = \frac{1}{2} \int_v \varepsilon_0 |\mathbf{E}|^2 dv $$
    Using spherical coordinates, the differential volume element is $dv = r^2 \sin\theta \, dr \, d\theta \, d\phi$. Integrating from $r=a$ to $\infty$:
    $$ W_E = \frac{1}{2} \varepsilon_0 \int_{r=a}^{\infty} \int_{\theta=0}^{\pi} \int_{\phi=0}^{2\pi} \left( \frac{Q}{4\pi\varepsilon_0 r^2} \right)^2 r^2 \sin\theta \, dr \, d\theta \, d\phi $$
    $$ W_E = \frac{1}{2} \varepsilon_0 \left( \frac{Q^2}{16\pi^2\varepsilon_0^2} \right) \int_{a}^{\infty} \frac{1}{r^4} \cdot r^2 \, dr \int_{0}^{\pi} \sin\theta \, d\theta \int_{0}^{2\pi} d\phi $$
    $$ W_E = \frac{Q^2}{32\pi^2\varepsilon_0} \left( \int_{a}^{\infty} \frac{1}{r^2} \, dr \right) (2) (2\pi) $$
    $$ W_E = \frac{Q^2}{8\pi\varepsilon_0} \left[ -\frac{1}{r} \right]_a^\infty = \frac{Q^2}{8\pi\varepsilon_0} \left( 0 - \left(-\frac{1}{a}\right) \right) $$
    $$ W_E = \frac{Q^2}{8\pi\varepsilon_0 a} $$

2.  **Equate to Rest Mass Energy:**
    According to the problem statement, this assembly work is stored as mass energy:
    $$ W_{relativistic} = W_E $$
    $$ mc^2 = \frac{Q^2}{8\pi\varepsilon_0 a} $$

3.  **Solve for the radius ($a$):**
    Rearranging the formula to solve for the radius $a$:
    $$ a = \frac{Q^2}{8\pi\varepsilon_0 m c^2} $$

4.  **Plug in the constants:**
    *   Magnitude of electron charge, $Q = e = 1.6 \times 10^{-19}$ C
    *   Mass of electron, $m = 9.1 \times 10^{-31}$ kg
    *   Speed of light, $c = 3 \times 10^8$ m/s
    *   The constant $\frac{1}{4\pi\varepsilon_0} \approx 9 \times 10^9$ m/F. Therefore, $\frac{1}{8\pi\varepsilon_0} = \frac{1}{2} \left( \frac{1}{4\pi\varepsilon_0} \right) \approx 4.5 \times 10^9$ m/F.

    Substitute these values into the equation for $a$:
    $$ a = \frac{(1.6 \times 10^{-19})^2 \times (4.5 \times 10^9)}{(9.1 \times 10^{-31}) \times (3 \times 10^8)^2} $$
    $$ a = \frac{(2.56 \times 10^{-38}) \times (4.5 \times 10^9)}{(9.1 \times 10^{-31}) \times (9 \times 10^{16})} $$
    $$ a = \frac{11.52 \times 10^{-29}}{81.9 \times 10^{-15}} $$
    $$ a \approx 0.14066 \times 10^{-14} \text{ m} $$
    $$ a \approx 1.407 \times 10^{-15} \text{ m} $$

*(Note: If the electron were modeled as a uniform solid sphere of volume charge rather than a surface shell, the electrostatic energy would be $W_E = \frac{3Q^2}{20\pi\varepsilon_0 a}$, leading to a slightly different numerical result of $a \approx 1.688 \times 10^{-15}$ m. The spherical shell model is the standard assumption used when defining the classic electron radius).*

The calculated radius of the electron is approximately **$1.41 \times 10^{-15}$ m**.

*(Related location: Book Page 155-156 (Energy formula), Page 1 (Constants) / PDF Page 180-181, 1




### untill 2015