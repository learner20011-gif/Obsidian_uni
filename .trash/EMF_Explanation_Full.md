# Detailed Explanation of Electromagnetic Fields & Waves (Document from Rahat Hasan.pdf)

## Part 1: Pages 1-2 (Recap)

### Introduction to Electromagnetics
**Electromagnetics (EM)** is defined as the branch of physics and electrical engineering studying electric and magnetic phenomena. Its principles are foundational to technologies like **microwaves, antennas, electric machines, satellite communications**, and **fiber optics**.

### Applications
*   **Medical:** EM power (shortwaves/microwaves) is used for **diathermy** (heating deep tissues) to stimulate physiological responses.
*   **Industrial:** **Induction heaters** use EM fields for melting, forging, and soldering.
*   **Manufacturing:** Dielectric heating seals plastic sheets.
*   **Agriculture:** EM energy can reduce acidity in vegetables to improve taste.

### Scalar, Vector, and Field
*   **Scalar:** A quantity with only magnitude (e.g., time, mass, temperature).
*   **Vector:** A quantity with both magnitude and direction (e.g., velocity, force).
*   **Field:** A function specifying a quantity everywhere in a region.
    *   **Scalar Field:** Temperature in a room.
    *   **Vector Field:** Gravitational force or raindrop velocity.

### Unit Vector
A **unit vector** $\mathbf{a}_A$ is a vector with a magnitude of 1, pointing in the direction of vector $\mathbf{A}$. It is defined as:
$$ \mathbf{a}_A = \frac{\mathbf{A}}{|\mathbf{A}|} $$
Thus, a vector can be written as its magnitude times its direction: $\mathbf{A} = A \mathbf{a}_A$.

### Cartesian Coordinates
A vector $\mathbf{A}$ is represented by its components along the x, y, and z axes:
$$ \mathbf{A} = A_x \mathbf{a}_x + A_y \mathbf{a}_y + A_z \mathbf{a}_z $$

---

## Part 2: Detailed Explanation of Pages 3-4

### Magnitude of a Vector
**Equation (4):** The magnitude (or length) of a vector $\mathbf{A}$ in Cartesian coordinates is derived from the Pythagorean theorem in 3D space:
$$ A = \sqrt{A_x^2 + A_y^2 + A_z^2} $$

**Equation (5):** By combining the definition of a unit vector (Eq 1) and the magnitude (Eq 4), the unit vector along $\mathbf{A}$ is explicitly given as:
$$ \mathbf{a}_A = \frac{A_x \mathbf{a}_x + A_y \mathbf{a}_y + A_z \mathbf{a}_z}{\sqrt{A_x^2 + A_y^2 + A_z^2}} $$

### Vector Addition and Subtraction
**Addition:** When two vectors $\mathbf{A}$ and $\mathbf{B}$ are added to form a third vector $\mathbf{C}$, the operation is performed component-by-component.
$$ \mathbf{C} = \mathbf{A} + \mathbf{B} $$
**Equation (7):** Expanded in component form:
$$ \mathbf{C} = (A_x + B_x)\mathbf{a}_x + (A_y + B_y)\mathbf{a}_y + (A_z + B_z)\mathbf{a}_z $$

**Subtraction:** Similarly, vector subtraction is defined as adding the negative of a vector.
**Equation (8):**
$$ \mathbf{D} = \mathbf{A} - \mathbf{B} = \mathbf{A} + (-\mathbf{B}) $$
$$ \mathbf{D} = (A_x - B_x)\mathbf{a}_x + (A_y - B_y)\mathbf{a}_y + (A_z - B_z)\mathbf{a}_z $$

**Figure 2:** This figure illustrates the **Parallelogram Rule** and the **Head-to-Tail Rule** for vector addition.
*   (a) shows $\mathbf{C} = \mathbf{A} + \mathbf{B}$ as the diagonal of a parallelogram formed by $\mathbf{A}$ and $\mathbf{B}$.
*   (b) shows the head-to-tail method where $\mathbf{B}$ is placed at the tip of $\mathbf{A}$, and the resultant vector connects the start of $\mathbf{A}$ to the end of $\mathbf{B}$.

### Laws of Vector Algebra
The text summarizes the fundamental algebraic properties that vectors obey:
1.  **Commutative Law:** $\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$ (Order of addition doesn't matter).
2.  **Associative Law:** $\mathbf{A} + (\mathbf{B} + \mathbf{C}) = (\mathbf{A} + \mathbf{B}) + \mathbf{C}$ (Grouping doesn't matter).
3.  **Distributive Law:** $k(\mathbf{A} + \mathbf{B}) = k\mathbf{A} + k\mathbf{B}$ (Multiplication by a scalar $k$ distributes over addition).

### Position and Distance Vectors
**Position Vector ($r_p$):**
A point $P(x, y, z)$ is defined by a position vector (or radius vector) extending from the origin $O(0,0,0)$ to the point $P$.
**Equation (9):**
$$ \mathbf{r}_p = \mathbf{OP} = x\mathbf{a}_x + y\mathbf{a}_y + z\mathbf{a}_z $$

**Figure 3:** Illustrates a position vector for point $P(3, 4, 5)$. The vector is the diagonal of a box with sides 3, 4, and 5 along the respective axes.
$$ \mathbf{r}_p = 3\mathbf{a}_x + 4\mathbf{a}_y + 5\mathbf{a}_z $$

**Distance Vector ($\mathbf{r}_{PQ}$):**
This vector represents the displacement from one point $P$ to another point $Q$.
**Figure 4:** Shows the vector triangle involved. By vector addition, $\mathbf{OQ} = \mathbf{OP} + \mathbf{PQ}$, so $\mathbf{r}_Q = \mathbf{r}_P + \mathbf{r}_{PQ}$.
**Equation (10):** Rearranging for the distance vector:
$$ \mathbf{r}_{PQ} = \mathbf{r}_Q - \mathbf{r}_P $$
$$ \mathbf{r}_{PQ} = (x_Q - x_P)\mathbf{a}_x + (y_Q - y_P)\mathbf{a}_y + (z_Q - z_P)\mathbf{a}_z $$

**Example 1 & 2:** The text provides practice problems (finding components, magnitudes, and unit vectors given specific vectors $\mathbf{A}$ and $\mathbf{B}$) to reinforce these concepts.

### Vector Multiplication
The document defines two primary types of vector multiplication:

#### 1. Scalar (or Dot) Product
**Definition:** $\mathbf{A} \cdot \mathbf{B} = AB \cos \theta_{AB}$
*   The result is a **scalar**.
*   $\theta_{AB}$ is the smaller angle between the vectors.
*   **Orthogonality:** If $\mathbf{A} \cdot \mathbf{B} = 0$, the vectors are perpendicular (orthogonal).

**Component Form:**
$$ \mathbf{A} \cdot \mathbf{B} = A_x B_x + A_y B_y + A_z B_z $$

**Properties:**
*   **Commutative:** $\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}$
*   **Self-Dot:** $\mathbf{A} \cdot \mathbf{A} = |\mathbf{A}|^2$
*   **Unit Vectors:** $\mathbf{a}_x \cdot \mathbf{a}_x = 1$, but $\mathbf{a}_x \cdot \mathbf{a}_y = 0$ (since axes are perpendicular).

#### 2. Vector (or Cross) Product
**Definition:** $\mathbf{A} \times \mathbf{B} = AB \sin \theta_{AB} \mathbf{a}_n$
*   The result is a **vector**.
*   The magnitude is the area of the parallelogram formed by $\mathbf{A}$ and $\mathbf{B}$.
*   The direction $\mathbf{a}_n$ is perpendicular to both $\mathbf{A}$ and $\mathbf{B}$, determined by the **Right-Hand Rule**.

**Figure 5:** Shows the cross product as the area of the parallelogram.
**Figure 6:** Illustrates the Right-Hand Rule: if you curl your fingers from $\mathbf{A}$ to $\mathbf{B}$, your thumb points in the direction of the result.

**Properties:**
*   **Not Commutative:** $\mathbf{A} \times \mathbf{B} \neq \mathbf{B} \times \mathbf{A}$
*   **Anticommutative:** $\mathbf{A} \times \mathbf{B} = - (\mathbf{B} \times \mathbf{A})$
*   **Unit Vectors:** $\mathbf{a}_x \times \mathbf{a}_y = \mathbf{a}_z$ (cyclic permutation).

---

## Part 3: Electrostatics (Pages 5-6)

### Introduction to Electrostatics
Electrostatics is the study of **static (stationary) charge distributions**.
*   **Applications:** Cathode-ray tubes, oscilloscope, X-ray machines, lightning protection, solid-state electronics (resistors, capacitors, FETs), and computer peripherals.

### Coulomb's Law
Formulated by Charles Augustin de Coulomb in 1785, this experimental law governs the force between stationary point charges.
**Statement:** The force $F$ between two point charges $Q_1$ and $Q_2$ is:
1.  Along the line joining them.
2.  Directly proportional to the product $Q_1 Q_2$.
3.  Inversely proportional to the square of the distance $R$ between them.

**Equation (1):**
$$ F = \frac{k Q_1 Q_2}{R^2} $$
Where $k$ is the proportionality constant given by $k = \frac{1}{4\pi\epsilon_0}$.
*   $\epsilon_0$ is the **permittivity of free space**: $\epsilon_0 \approx 8.854 \times 10^{-12} \text{ F/m}$.
*   $k \approx 9 \times 10^9 \text{ m/F}$.

### Vector Form of Coulomb's Law
**Equation (2):**
$$ \mathbf{F} = \frac{Q_1 Q_2}{4\pi\epsilon_0 R^2} \mathbf{a}_R $$
This equation adds direction to the force.

**Figure 7:** Shows the geometry for the force $\mathbf{F}_{12}$ (force on $Q_2$ due to $Q_1$).
*   The distance vector is $\mathbf{R}_{12} = \mathbf{r}_2 - \mathbf{r}_1$.
*   The unit vector $\mathbf{a}_{R12} = \frac{\mathbf{R}_{12}}{|\mathbf{R}_{12}|}$.

**Equation (6):** Newton's Third Law applies: $\mathbf{F}_{21} = -\mathbf{F}_{12}$. The force on charge 1 is equal and opposite to the force on charge 2.

### Principle of Superposition
If there are multiple charges ($Q_1, Q_2, \dots, Q_N$), the total force on a test charge $Q$ is the vector sum of the individual forces exerted by each charge.
**Equation (7):**
$$ \mathbf{F} = \frac{Q}{4\pi\epsilon_0} \sum_{k=1}^{N} \frac{Q_k (\mathbf{r} - \mathbf{r}_k)}{|\mathbf{r} - \mathbf{r}_k|^3} $$

### Electric Field Intensity (E)
The electric field intensity $\mathbf{E}$ is defined as the **force per unit charge**.
**Equation (8):**
$$ \mathbf{E} = \lim_{Q \to 0} \frac{\mathbf{F}}{Q} $$
**Equation (10):** For a single point charge $Q$ located at $\mathbf{r}'$, the field at point $\mathbf{r}$ is:
$$ \mathbf{E} = \frac{Q (\mathbf{r} - \mathbf{r}')}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|^3} $$

---

## Part 4: Continuous Charge Distributions (Page 7+)

### Types of Charge Distributions
When charge is not concentrated at points but spread out, we define charge densities:
1.  **Line Charge ($\rho_L$):** Charge per unit length (C/m).
2.  **Surface Charge ($\rho_S$):** Charge per unit area (C/m²).
3.  **Volume Charge ($\rho_v$):** Charge per unit volume (C/m³).

**Equations (12-14):** The differential charge $dQ$ is expressed as:
*   $dQ = \rho_L dl$ (Line)
*   $dQ = \rho_S dS$ (Surface)
*   $dQ = \rho_v dv$ (Volume)

**Equations (15-17):** To find the total Electric Field $\mathbf{E}$, we integrate the contribution of each differential charge element over the entire distribution. For example, for volume charge:
$$ \mathbf{E} = \int \frac{\rho_v dv}{4\pi\epsilon_0 R^2} \mathbf{a}_R $$

### Example: Field of a Line Charge
**Setup:** An infinite line charge along the z-axis with uniform density $\rho_L$.
**Symmetry Analysis:**
*   The field must have **azimuthal symmetry** (independent of $\phi$).
*   The field must have **axial symmetry** (independent of $z$ since the line is infinite).
*   The field components $E_\phi$ and $E_z$ cancel out due to symmetry, leaving only the radial component $E_\rho$.

**Equation (18):** The final derived formula for the electric field of an infinite line charge is:
$$ \mathbf{E} = \frac{\rho_L}{2\pi\epsilon_0 \rho} \mathbf{a}_\rho $$
This shows the field is inversely proportional to the radial distance $\rho$.

### Example: Field of a Surface Charge (Sheet)
**Setup:** An infinite sheet of charge in the xy-plane with uniform density $\rho_S$.
**Equation (22):** Through integration, the field is found to be:
$$ \mathbf{E} = \frac{\rho_S}{2\epsilon_0} \mathbf{a}_z $$
**Significance:**
*   The field is **constant**; it does not depend on the distance from the sheet.
*   It points normally away from the sheet.
*   **Equation (23):** Generally written as $\mathbf{E} = \frac{\rho_S}{2\epsilon_0} \mathbf{a}_n$, where $\mathbf{a}_n$ is the unit normal vector.

### Electric Flux Density (D)
**Definition:** To handle electric fields in different media, the vector field $\mathbf{D}$ is introduced.
**Equation (34):**
$$ \mathbf{D} = \epsilon_0 \mathbf{E} $$
In SI units, $\mathbf{D}$ is measured in **Coulombs per square meter** ($C/m^2$). It is also known as **electric displacement**.

**Equation (35):** Electric Flux $\Psi$ is the integral of $\mathbf{D}$ over a surface $S$:
$$ \Psi = \int_S \mathbf{D} \cdot d\mathbf{S} $$

---

## Part 5: Energy, Potential, and Conductors

### Work and Potential
**Work Done:** Moving a charge $Q$ against an electric field $\mathbf{E}$ requires work.
**Equation (3):** The work $W$ to move charge $Q$ from an initial to a final point is:
$$ W = -Q \int_{init}^{final} \mathbf{E} \cdot d\mathbf{L} $$

**Potential Difference ($V$):** Defined as the work done per unit charge.
**Equation (7):**
$$ V = -\int_{init}^{final} \mathbf{E} \cdot d\mathbf{L} $$
$V_{AB}$ represents the potential difference between points A and B.

**Potential of a Point Charge:**
**Equation (13):** The absolute potential $V$ at a distance $r$ from a point charge $Q$ (with zero reference at infinity) is:
$$ V = \frac{Q}{4\pi\epsilon_0 r} $$

### Potential Gradient
The relationship between Electric Field and Potential is given by the **Gradient**.
**Equation (23):**
$$ \mathbf{E} = -\nabla V $$
This states that the electric field points in the direction of the maximum decrease of potential.

### Current and Current Density
**Current ($I$):** Rate of flow of charge ($dQ/dt$).
**Current Density ($\mathbf{J}$):** Current per unit cross-sectional area.
**Equation (2):**
$$ I = \int_S \mathbf{J} \cdot d\mathbf{S} $$
**Equation (3):** Convection current density relates to charge density $\rho_v$ and velocity $\mathbf{v}$:
$$ \mathbf{J} = \rho_v \mathbf{v} $$

**Ohm's Law (Point Form):**
**Equation (8):** In a conductor, current density is proportional to the electric field:
$$ \mathbf{J} = \sigma \mathbf{E} $$
Where $\sigma$ is the **conductivity** of the material.

### Boundary Conditions
When an electric field crosses the boundary between a conductor and free space:
1.  **Tangential Field:** $E_t = 0$ (Tangential component is zero).
2.  **Normal Field:** $D_N = \rho_S$ (Normal flux density equals surface charge density).
This implies that the electric field must leave a conductor surface **perpendicularly**.

### Method of Images
A technique to solve electrostatic problems involving charges near a conducting plane.
*   **Concept:** A charge $+Q$ near a grounded conducting plane can be modeled by removing the plane and placing an "image charge" $-Q$ at the mirror-image position.
*   This simplifies the calculation of potential and field in the region above the plane.

### Semiconductors and Dielectrics
*   **Semiconductors:** Conductivity depends on both electrons and "holes".
    $$ \sigma = -\rho_e \mu_e + \rho_h \mu_h $$
*   **Dielectrics:** Insulating materials where charges are "bound". An external field causes **polarization** ($\mathbf{P}$), creating electric dipoles.
    **Equation (6):** The definition of $\mathbf{D}$ is generalized:
    $$ \mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P} $$
    **Equation (11):** For linear dielectrics:
    $$ \mathbf{D} = \epsilon \mathbf{E} $$
    Where $\epsilon = \epsilon_0 \epsilon_r$ is the permittivity of the material.

### Poisson's and Laplace's Equations
These are differential equations for the electric potential $V$.
**Poisson's Equation (p4):**
$$ \nabla^2 V = -\frac{\rho_v}{\epsilon} $$
Used when charge density is present.

**Laplace's Equation (p5):**
$$ \nabla^2 V = 0 $$
Used in charge-free regions. Solving this equation is the primary method for finding potential distributions in many boundary-value problems.
