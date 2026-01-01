# Electromagnetic Fields: Energy, Potential, and Boundary Conditions

## 1. Energy and Potential
This section explores the relationship between work, energy, and electric potential in an electrostatic field.

### A. Work Done
*   **Definition**: Work required to move a charge $Q$ against an electric field $\mathbf{E}$.
*   **Formula**:
    $$dW = -Q \mathbf{E} \cdot d\mathbf{L}$$
    *   The negative sign indicates work is done *against* the field (by an external agent).
    *   $d\mathbf{L}$ is the differential displacement vector.
*   **Finite Displacement**:
    $$W = -Q \int_{initial}^{final} \mathbf{E} \cdot d\mathbf{L}$$ 

### B. The Line Integral
*   **Concept**: The work expression is a line integral, meaning the path matters in general vector fields, but not in electrostatic fields.
*   **Calculation**:
    *   The path is broken into small segments $d\mathbf{L}$.
    *   The dot product $\mathbf{E} \cdot d\mathbf{L}$ is calculated for each segment (taking the component of $\mathbf{E}$ parallel to the path).
    *   Summation (integration) yields the total work.
*   **Uniform Field**: For a uniform field, path doesn't matter; only start and end points.

### C. Potential Difference and Potential
*   **Potential Difference ($V$)**: Defined as the work done (by an external source) to move a *unit positive charge* from one point to another.
    $$V_{AB} = \frac{W}{Q} = -\int_B^A \mathbf{E} \cdot d\mathbf{L}$$ 
    *   $V_{AB}$ is the potential difference between point A and point B ($V_{AB} = V_A - V_B$).
    *   Measured in **Volts (V)** or **Joules/Coulomb (J/C)**.
*   **Absolute Potential ($V$)**:
    *   Requires a reference point of zero potential (usually at infinity).
    *   $$V_A = -\int_{\infty}^A \mathbf{E} \cdot d\mathbf{L}$$ 

### D. Potential Field of a Point Charge
*   **Derivation**: Using the E-field of a point charge $\mathbf{E} = \frac{Q}{4\pi\epsilon_0 r^2} \mathbf{a}_r$ and integrating radially from infinity (reference) to $r$.
*   **Formula**:
    $$V = \frac{Q}{4\pi\epsilon_0 r}$$ 
*   **Key Characteristics**:
    *   $V \rightarrow 0$ as $r \rightarrow \infty$ (Zero reference at infinity).
    *   Equipotential surfaces are **spheres** centered at the charge.

### E. Potential Field of a System of Charges
*   **Principle of Superposition**: The total potential is the scalar sum of potentials due to individual charges.
*   **Discrete Charges**:
    $$V(\mathbf{r}) = \sum_{m=1}^{n} \frac{Q_m}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}_m|}$$ 
*   **Continuous Charge Distributions**:
    *   **Line Charge**: $$V = \int_L \frac{\rho_L dL'}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|}$$ 
    *   **Surface Charge**: $$V = \int_S \frac{\rho_S dS'}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|}$$ 
    *   **Volume Charge**: $$V = \int_{vol} \frac{\rho_v dv'}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|}$$ 

### F. Example: Potential of a Ring of Charge
*   **Setup**: A circular ring of radius $a$ carries a uniform linear charge density $\rho_L$. We want to find potential $V$ on the z-axis at point $(0,0,z)$.
*   **Geometry**:
    *   Distance $R = \sqrt{a^2 + z^2}$.
    *   This distance is constant for every element $dL$ on the ring.
*   **Integration**:
    *   $V = \int_0^{2\pi} \frac{\rho_L (a d\phi)}{4\pi\epsilon_0 \sqrt{a^2 + z^2}}$
    *   Since terms are constant with respect to $\phi$:
    *   $$V = \frac{\rho_L (2\pi a)}{4\pi\epsilon_0 \sqrt{a^2 + z^2}} = \frac{Q_{total}}{4\pi\epsilon_0 \sqrt{a^2 + z^2}}$$ 
*   **Significance**: Demonstrates that for a point on the axis, the ring acts like a point charge $Q_{total}$ at distance $\sqrt{a^2+z^2}$.

### G. Conservative Property
*   **Closed Loop Integral**: The work done in moving a charge around a closed path in an electrostatic field is zero.
    $$\oint \mathbf{E} \cdot d\mathbf{L} = 0$$ 
*   **Implication**: The electrostatic field is a **conservative field**. The potential depends only on position, not path.
*   **Circuit Theory Connection**: This is the basis for Kirchhoff’s Voltage Law (KVL).

### H. Potential Gradient
*   **Relationship**: How to find Electric Field ($\mathbf{E}$) if Potential ($V$) is known.
*   **Definition**: The electric field intensity is the negative gradient of the electric potential.
    $$\mathbf{E} = -\nabla V$$ 
    *   The gradient ($\nabla V$) points in the direction of the maximum rate of increase of $V$.
    *   The negative sign shows $\mathbf{E}$ points from higher potential to lower potential.
*   **Coordinate Forms**:
    *   *Cartesian*: $\nabla V = \frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z$
    *   *Cylindrical*: $\nabla V = \frac{\partial V}{\partial \rho}\mathbf{a}_\rho + \frac{1}{\rho}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi + \frac{\partial V}{\partial z}\mathbf{a}_z$
    *   *Spherical*: $\nabla V = \frac{\partial V}{\partial r}\mathbf{a}_r + \frac{1}{r}\frac{\partial V}{\partial \theta}\mathbf{a}_\theta + \frac{1}{r \sin \theta}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi$

### I. The Dipole
*   **Definition**: Two point charges of equal magnitude ($Q$) but opposite sign, separated by a small distance $d$.
*   **Approximation**:
    *   For a distant point $P$ (where $r \gg d$), the path difference is approx $d \cos \theta$.
    *   $R_2 - R_1 \approx d \cos \theta$ and $R_1 R_2 \approx r^2$.
*   **Dipole Moment ($\mathbf{p}$)**: Vector pointing from $-Q$ to $+Q$ with magnitude $Qd$.
    $$\mathbf{p} = Q\mathbf{d}$$ 
*   **Potential Field**:
    $$V = \frac{Q(R_2 - R_1)}{4\pi\epsilon_0 R_1 R_2} \approx \frac{Qd \cos\theta}{4\pi\epsilon_0 r^2} = \frac{\mathbf{p} \cdot \mathbf{a}_r}{4\pi\epsilon_0 r^2}$$ 
*   **Key Insight**: Potential drops off as $1/r^2$ (faster than a point charge's $1/r$).

### J. Energy Density in Electrostatic Field
*   **Concept**: Energy stored in the assembly of charges.
*   **Work to Position Charges**:
    $$W_E = \frac{1}{2} \sum_{m=1}^{N} Q_m V_m$$ 
*   **Integral Form**:
    $$W_E = \frac{1}{2} \int_{vol} \rho_v V dv$$ 
*   **In terms of Fields**:
    *   Using vector identity $\nabla \cdot (V\mathbf{D}) = V(\nabla \cdot \mathbf{D}) + \mathbf{D} \cdot (\nabla V)$ and Divergence Theorem.
    $$W_E = \frac{1}{2} \int_{vol} \mathbf{D} \cdot \mathbf{E} dv = \frac{1}{2} \int_{vol} \epsilon_0 E^2 dv$$ 
*   **Energy Density ($w_E$)**: Energy per unit volume.
    $$w_E = \frac{1}{2} \epsilon_0 E^2$$ 

---\n
## 2. Current and Conductors
Transitioning from static charges to charges in motion (current).

### A. Current and Current Density
*   **Current ($I$)**: Rate of charge flow. $I = dQ/dt$ (Amperes).
*   **Current Density ($\mathbf{J}$)**: Current per unit cross-sectional area (Amps/m²).
    $$I = \int_S \mathbf{J} \cdot d\mathbf{S}$$ 
*   **Relation to Velocity**:
    $$\mathbf{J} = \rho_v \mathbf{v}$$ 
    (where $\rho_v$ is volume charge density, $\mathbf{v}$ is velocity).

### B. Continuity of Current
*   **Conservation of Charge**: Charge cannot be created or destroyed.
*   **Integral Form**: Current flowing *out* of a closed surface equals the rate of decrease of charge *inside*.
    $$\oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{dQ_{in}}{dt}$$ 
*   **Point Form (Continuity Equation)**:
    $$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$ 
    *   For steady currents (DC), $\partial \rho_v / \partial t = 0$, so $\nabla \cdot \mathbf{J} = 0$ (Current entering = Current leaving).

### C. Metallic Conductors
*   **Mechanism**: Valence electrons are loosely bound and move freely ("electron gas").
*   **Drift Velocity ($\mathbf{v}_d$)**: Average velocity of electrons under an E-field (opposed by collisions).
    $$\mathbf{v}_d = -\mu_e \mathbf{E}$$ 
    ($\mu_e$ = electron mobility).
*   **Point Form of Ohm's Law**:
    $$\mathbf{J} = \sigma \mathbf{E}$$ 
    *   $\sigma$ (Sigma) is **Conductivity**. $\sigma = -\rho_e \mu_e$.

### D. Resistance
*   **Macroscopic View**: From point form to circuit form.
    $$V = IR$$ 
*   **Resistance Formula**:
    $$R = \frac{V_{ab}}{I} = \frac{-\int_b^a \mathbf{E} \cdot d\mathbf{L}}{\int_S \sigma \mathbf{E} \cdot d\mathbf{S}}$$ 
*   **Uniform Conductor** (Length $L$, Area $S$):
    $$R = \frac{L}{\sigma S}$$ 

---\n
## 3. Conductor Properties and Boundary Conditions
Behavior of fields at the interface of a perfect conductor and free space.

### A. Properties of a Conductor in Static Field
1.  **Zero Internal Field**: $\mathbf{E} = 0$ inside the conductor (otherwise charges would move).
2.  **Zero Internal Charge**: $\rho_v = 0$ inside. All charge resides on the **surface**.
3.  **Equipotential**: The entire conductor (volume and surface) is at the same potential.

### B. Boundary Conditions
Analyzing the interface between Conductor and Free Space using Maxwell's integral laws.

*   **Tangential Component ($E_t$)**:
    *   **Method**: Apply $\oint \mathbf{E} \cdot d\mathbf{L} = 0$ to a small rectangular loop across the boundary.
    *   **Derivation**: $E_t \Delta w - 0 \cdot \Delta w = 0$ (since E=0 inside).
    *   **Result**: $E_t = 0$.
    *   The electric field has **no tangential component** on the surface. It is always **normal** (perpendicular) to the surface.

*   **Normal Component ($D_n$)**:
    *   **Method**: Apply Gauss's Law $\oint \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ to a small cylinder ("pillbox") at the surface.
    *   **Derivation**: $D_n \Delta S - 0 \cdot \Delta S = \rho_S \Delta S$ (Flux out top - Flux out bottom = Enclosed Charge).
    *   **Result**: $D_n = \rho_S$.
    *   The normal component of Flux Density equals the surface charge density.
    *   In terms of E: $E_n = \frac{\rho_S}{\epsilon_0}$.

### C. Summary of Boundary Conditions
$$D_t = E_t = 0$$ 
$$D_n = \epsilon_0 E_n = \rho_S$$ 

---\n
## 4. Missing Context, Assumptions, and Knowledge Gaps

To fully understand the document, the following implied knowledge is necessary:

### A. Vector Calculus Prerequisities
*   **Gradient ($\nabla V$)**: The text assumes knowledge of the del operator ($\nabla$) and how to compute gradients in different coordinate systems (Cartesian, Cylindrical, Spherical).
*   **Divergence ($\nabla \cdot \mathbf{A}$)**: Used in the Continuity Equation and Maxwell's First Equation.
*   **Divergence Theorem**: implicitly used in deriving the energy density field integral.
*   **Line & Surface Integrals**: The definitions of Work and Current rely heavily on understanding vector path and area integration.

### B. Physics Fundamentals
*   **Coulomb's Law**: The base for the potential of a point charge is assumed ($E = kQ/r^2$).
*   **Maxwell's Equations**: The text references "Maxwell's first equation" ($\nabla \cdot \mathbf{D} = \rho_v$) without deriving it, assuming it was covered in a previous Electrostatics chapter.
*   **Conservative Fields**: The concept that "work done in a closed loop is zero" defines a conservative field, a property fundamental to defining Scalar Potential $V$.
*   **Zero Reference**: The derivations for absolute potential assume $V=0$ at infinity, which is standard for bounded charge distributions but requires justification.

### C. Notation
*   **$\mathbf{a}_r, \mathbf{a}_\phi, \mathbf{a}_z$**: Unit vectors are used without introduction (standard IEEE/Engineering notation).
*   **$\epsilon_0$**: Permittivity of free space ($8.854 \times 10^{-12}$ F/m) is a constant used throughout but not always defined in every section.
*   **Coordinate Systems**: The text assumes fluency in switching between Cartesian, Cylindrical ($\rho, \phi, z$), and Spherical ($r, \theta, \phi$) coordinates, often without explicitly stating which system is active in a generic equation.