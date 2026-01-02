# Electromagnetic Fields: Energy, Potential, and Boundary Conditions (Comprehensive Guide)

This document provides a complete, detailed explanation of the topics "Energy and Potential", "Current and Conductors", and "Conductor Properties and Boundary Conditions". It breaks down every paragraph, derivation, and concept found in the source material.

---

## 1. Energy and Potential

This chapter establishes the relationship between the electric field intensity ($\mathbf{E}$) and the scalar electric potential ($V$). It moves from the concept of work to defining potential difference and absolute potential.

### A. Work Done in Moving a Charge
**Concept**: To move a charge in an electric field, force must be applied. If you move a charge against the field, you do work on the charge, storing energy.

*   **The Force**: The force exerted *by* the electric field on a charge Q is $\mathbf{F}_E = Q\mathbf{E}$.
*   **The Applied Force**: To move the charge *against* this field (or keep it in equilibrium while moving), an external agent must apply an equal and opposite force:
    $$\mathbf{F}_{applied} = -\mathbf{F}_E = -Q\mathbf{E}$$
*   **Differential Work ($dW$)**: Work is defined as force dot distance ($dW = \mathbf{F} \cdot d\mathbf{L}$). 
    $$dW = \mathbf{F}_{applied} \cdot d\mathbf{L} = -Q\mathbf{E} \cdot d\mathbf{L}$$ 
    *   **Context**: The dot product handles the vector nature. Only the component of force parallel to the movement does work.
    *   **$d\mathbf{L}$**: Vector representing an infinitesimal displacement ($dx\mathbf{a}_x + dy\mathbf{a}_y + dz\mathbf{a}_z$) in Cartesian.

**Total Work Integral**:
To find the total work moving a charge from an initial point to a final point, we integrate the differential work along the path:
$$W = -Q \int_{initial}^{final} \mathbf{E} \cdot d\mathbf{L}$$ 
*   **Interpretation**: If $W > 0$, external work was required (moving against the field, increasing potential energy). If $W < 0$, the field did the work (moving with the field, losing potential energy).

### B. The Line Integral
**Definition**: The integral $\int \mathbf{E} \cdot d\mathbf{L}$ is a **line integral**.
*   **Path Dependence**: In general vector math, a line integral depends on the specific path taken. However, for **electrostatic** fields, the integral depends *only* on the start and end points. This is a crucial property of conservative fields.
*   **Numerical Calculation**:
    1.  Divide the path into small segments $\Delta \mathbf{L}$.
    2.  Assume $\mathbf{E}$ is constant over that small segment.
    3.  Compute $\mathbf{E} \cdot \Delta \mathbf{L}$ for each.
    4.  Sum them up: $W \approx -Q \sum (\mathbf{E} \cdot \Delta \mathbf{L})$.

### C. Definition of Potential Difference ($V$)
**Concept**: Potential difference is "work per unit charge". It standardizes energy measurement independent of the test charge's magnitude.

*   **Formula**:
    $$V_{AB} = \frac{\text{Work to move } Q \text{ from } B \text{ to } A}{Q}$$ 
    $$V_{AB} = -\int_B^A \mathbf{E} \cdot d\mathbf{L}$$ 
*   **Notation**:
    *   $V_{AB}$ means "Potential at A with respect to B".
    *   $V_{AB} = V_A - V_B$.
    *   If $V_{AB}$ is positive, point A is at a higher potential (energy) than B. Work is required to get there.

### D. The Potential Field of a Point Charge
**Goal**: Derive the formula $V = Q/(4\pi\epsilon_0 r)$.

1.  **Source Field**: A point charge $Q$ is at the origin. Its field is radial:
    $$\mathbf{E} = E_r \mathbf{a}_r = \frac{Q}{4\pi\epsilon_0 r^2} \mathbf{a}_r$$ 
2.  **Path**: Move a test charge from point B (radius $r_B$) to point A (radius $r_A$).
3.  **Displacement**: In spherical coordinates, $d\mathbf{L} = dr\mathbf{a}_r + r d\theta \mathbf{a}_\theta + r \sin\theta d\phi \mathbf{a}_\phi$. 
4.  **Dot Product**: $\mathbf{E}$ only has an $\mathbf{a}_r$ component. So, $\mathbf{E} \cdot d\mathbf{L} = E_r dr$. The angular parts dot to zero.
5.  **Integration**:
    $$V_{AB} = -\int_{r_B}^{r_A} \frac{Q}{4\pi\epsilon_0 r^2} dr = -\frac{Q}{4\pi\epsilon_0} \left[ \frac{-1}{r} \right]_{r_B}^{r_A}$$ 
    $$V_{AB} = \frac{Q}{4\pi\epsilon_0} \left( \frac{1}{r_A} - \frac{1}{r_B} \right)$$ 
6.  **Defining Absolute Potential**:
    *   We need a reference point where $V=0$.
    *   By convention, we choose infinity ($r_B \rightarrow \infty$). Since $1/\infty = 0$:
    $$V_A = \frac{Q}{4\pi\epsilon_0 r_A}$$ 
    *   **General Formula** (at any distance $r$):
        $$V = \frac{Q}{4\pi\epsilon_0 r}$$ 

### E. Potential of a System of Charges
**Principle**: Potentials adds up algebraically (scalars), unlike fields which add geometrically (vectors). This makes calculating $V$ much easier than $\mathbf{E}$.

1.  **Multiple Point Charges**:
    $$V(\mathbf{r}) = \frac{Q_1}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}_1|} + \frac{Q_2}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}_2|} + \dots$$ 
    $$V(\mathbf{r}) = \sum_{m=1}^{N} \frac{Q_m}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}_m|}$$ 
    *   $|\mathbf{r} - \mathbf{r}_m|$ is the distance from the $m$-th charge to the observation point.

2.  **Continuous Charge Distributions**:
    *   Replace summation $\sum Q$ with integration $\int dQ$.
    *   $dQ$ depends on the geometry (Line, Surface, Volume).
    *   **Line Charge**: $dQ = \rho_L dL \rightarrow V = \int \frac{\rho_L dL}{4\pi\epsilon_0 R}$
    *   **Surface Charge**: $dQ = \rho_S dS \rightarrow V = \int \frac{\rho_S dS}{4\pi\epsilon_0 R}$
    *   **Volume Charge**: $dQ = \rho_v dv \rightarrow V = \int \frac{\rho_v dv}{4\pi\epsilon_0 R}$

### F. Example Derivation: Potential of a Ring of Charge
**Scenario**: Uniform line charge $\rho_L$ on a circular ring of radius $a$ in the $xy$-plane. Find $V$ at point $P(0,0,h)$ on the $z$-axis.

1.  **Charge Element**: Consider a small segment $dL = a d\phi$. The charge is $dQ = \rho_L (a d\phi)$.
2.  **Distance**: The distance $R$ from any point on the ring to $P$ is the hypotenuse of the triangle formed by radius $a$ and height $h$:
    $$R = \sqrt{a^2 + h^2}$$ 
    *   *Crucial Point*: This distance $R$ is constant for *all* points on the ring because of symmetry.
3.  **Integral**:
    $$V = \int_{0}^{2\pi} \frac{\rho_L a d\phi}{4\pi\epsilon_0 \sqrt{a^2 + h^2}}$$ 
4.  **Solving**: Everything except $d\phi$ is constant.
    $$V = \frac{\rho_L a}{4\pi\epsilon_0 \sqrt{a^2 + h^2}} \int_{0}^{2\pi} d\phi$$ 
    $$V = \frac{\rho_L a (2\pi)}{4\pi\epsilon_0 \sqrt{a^2 + h^2}}$$ 
    Since Total Charge $Q = 2\pi a \rho_L$:
    $$V = \frac{Q}{4\pi\epsilon_0 \sqrt{a^2 + h^2}}$$ 

### G. Conservative Field Property
**Statement**: $\oint \mathbf{E} \cdot d\mathbf{L} = 0$
*   **Meaning**: If you move a charge in a closed loop (start and end at the same point), the net work done is zero. You might do work going up potential "hills", but you get it all back going down.
*   **Kirchhoff's Voltage Law (KVL)**: This physical property is why the sum of voltage drops around a circuit loop is zero. $\sum V = 0$.

### H. Potential Gradient ($\mathbf{E} = -\nabla V$)
**Concept**: We derived $V$ from $\mathbf{E}$ (via integration). Can we find $\mathbf{E}$ if we know $V$? Yes, via differentiation (Gradient).

*   **Derivation Logic**:
    *   $dV = -\mathbf{E} \cdot d\mathbf{L}$.
    *   From calculus, the total differential is $dV = \nabla V \cdot d\mathbf{L}$.
    *   Therefore: $\mathbf{E} = -\nabla V$.
*   **Interpretation**:
    1.  **Magnitude**: The field strength is the rate of change of potential (Volts per meter). Steep potential slope = Strong Field.
    2.  **Direction**: $\mathbf{E}$ points "downhill", from high potential to low potential (hence the negative sign). It points in the direction of steepest descent.

### I. The Electric Dipole
**Setup**: Charge $+Q$ at $z = d/2$ and $-Q$ at $z = -d/2$. Distance $d$ is very small. We want $V$ at a far point $P(r, \theta, \phi)$.

1.  **Exact Potential**: $V = \frac{Q}{4\pi\epsilon_0 R_+} - \frac{Q}{4\pi\epsilon_0 R_-}$.
2.  **Approximation**: Since $r \gg d$, the lines from the two charges to $P$ are almost parallel.
    *   The path difference is $R_- - R_+ \approx d \cos \theta$.
    *   The product $R_+ R_- \approx r^2$.
3.  **Approximate Formula**:
    $$V \approx \frac{Q (d \cos \theta)}{4\pi\epsilon_0 r^2}$$ 
4.  **Dipole Moment ($\mathbf{p}$)**: Define vector $\mathbf{p} = Q\mathbf{d}$ (pointing minus to plus).
    *   $Q d \cos \theta = \mathbf{p} \cdot \mathbf{a}_r$.
    $$V = \frac{\mathbf{p} \cdot \mathbf{a}_r}{4\pi\epsilon_0 r^2}$$ 
5.  **Significance**:
    *   Monopole (Point charge) $V \propto 1/r$.
    *   Dipole $V \propto 1/r^2$. (Falls off faster).
    *   Quadrupole $V \propto 1/r^3$.

### J. Energy Density
**Concept**: How much energy is stored in empty space containing an electric field?

1.  **Assembly Work**: To assemble a system of discrete charges, you do work bringing each one in against the field of the others.
    $$W_E = \frac{1}{2} \sum Q_m V_m$$ 
    *(Factor of 1/2 prevents double counting interactions).*
2.  **Continuous Volume**:
    $$W_E = \frac{1}{2} \int_{vol} \rho_v V dv$$ 
3.  **Field Formulation**:
    *   Replace $\rho_v$ with $\nabla \cdot \mathbf{D}$ (Maxwell's 1st Eq).
    *   Use vector calculus identity and Divergence Theorem to transform the integral.
    *   Result:
        $$W_E = \frac{1}{2} \int_{vol} \mathbf{D} \cdot \mathbf{E} dv$$ 
4.  **Energy Density ($w_E$)**: Energy per unit volume.
    $$w_E = \frac{1}{2} \mathbf{D} \cdot \mathbf{E} = \frac{1}{2} \epsilon_0 E^2$$ 
    *   This implies energy is stored *in the field itself*.

---

## 2. Current and Conductors

This section introduces charge motion.

### A. Current ($I$) and Current Density ($\mathbf{J}$)
*   **Current**: Scalar $I = dQ/dt$. (Coulombs/sec = Amps).
*   **Current Density**: Vector $\mathbf{J}$.
    *   Magnitude: Current per unit area normal to flow ($A/m^2$).
    *   Direction: Direction of positive charge flow.
    *   Relationship: $I = \int \mathbf{J} \cdot d\mathbf{S}$.
*   **Convection Current**: Moving charge cloud (e.g., electron beam).
    $$\mathbf{J} = \rho_v \mathbf{v}$$ 
    (Charge density $\times$ Velocity).

### B. Continuity Equation
**Physics**: Conservation of Charge. Charge cannot just disappear.
*   **Logic**: If current flows *out* of a volume, the amount of charge *inside* must decrease.
*   **Equation**:
    $$\text{Current Out} = -\text{Rate of charge decrease}$$ 
    $$\oint \mathbf{J} \cdot d\mathbf{S} = -\frac{d}{dt} \int \rho_v dv$$ 
*   **Point Form**: Apply divergence theorem.
    $$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$ 
*   **Steady State**: For DC currents, nothing changes with time ($\partial/\partial t = 0$).
    $$\nabla \cdot \mathbf{J} = 0$$ 
    (Current entering a point must equal current leaving).

### C. Metallic Conductors & Ohm's Law
*   **Drift Velocity**: In a conductor, electrons bounce randomly. An E-field adds a small "drift" velocity.
    $$\mathbf{v}_d = -\mu_e \mathbf{E}$$ 
*   **Point Form of Ohm's Law**:
    *   Since $\mathbf{J} = \rho \mathbf{v}$, substituting velocity gives:
    $$\mathbf{J} = \sigma \mathbf{E}$$ 
    *   $\sigma$ (Sigma) is **Conductivity**. High $\sigma$ = Good conductor.

### D. Resistance Calculation
*   We move from the point form ($\mathbf{J}=\sigma\mathbf{E}$) to the circuit form ($V=IR$).
*   **General Formula**:
    $$R = \frac{V}{I} = \frac{-\int \mathbf{E} \cdot d\mathbf{L}}{\int \sigma \mathbf{E} \cdot d\mathbf{S}}$$ 
*   **Cylindrical Wire** (Length $L$, Area $S$, Uniform field):
    *   $V = E \times L$
    *   $I = J \times S = (\sigma E) \times S$
    *   $R = \frac{EL}{\sigma E S} = \frac{L}{\sigma S}$ (Familiar formula).

---

## 3. Conductor Properties and Boundary Conditions

What happens at the edge of a conductor?

### A. Inside a Conductor (Static Case)
1.  **$\mathbf{E} = 0$**: If there were a field inside, charges would move (current). In statics, charges have stopped moving, so the net force (field) must be zero.
2.  **$\rho_v = 0$**: From Gauss's Law ($\nabla \cdot \mathbf{E} = \rho_v/\epsilon$), if $\mathbf{E}=0$, then $\rho_v=0$. No net charge *inside* the volume.
3.  **Charge on Surface**: Any net charge placed on a conductor is pushed by mutual repulsion to the very outer surface.

### B. Boundary Conditions (Interface between Conductor & Free Space)
We need to determine how $\mathbf{E}$ and $\mathbf{D}$ behave crossing the boundary.

**1. Tangential Component ($E_t$)**
*   **Tool**: Conservative Line Integral $\oint \mathbf{E} \cdot d\mathbf{L} = 0$.
*   **Path**: A small rectangular loop half inside, half outside the conductor.
    *   Length $\Delta w$, Height $\Delta h \rightarrow 0$.
*   **Evaluation**:
    *   Outside leg: $E_t \Delta w$.
    *   Inside leg: $0$ (since E=0 inside).
    *   Sides: $0$ (as $\Delta h \rightarrow 0$).
    *   Sum: $E_t \Delta w = 0$.
*   **Conclusion**: $E_t = 0$.
    *   **The electric field cannot have a component parallel to the conductor surface.** It must point straight out (Normal).

**2. Normal Component ($D_n$)**
*   **Tool**: Gauss's Law $\oint \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$.
*   **Surface**: A small cylinder ("pillbox") cut into the surface.
*   **Evaluation**:
    *   Top (Outside): $D_n \Delta S$.
    *   Bottom (Inside): $0$ (since E=0 inside).
    *   Sides: $0$ (flux is parallel to sides).
    *   Enclosed Charge: The surface charge $\rho_S \Delta S$ captured by the cylinder.
    *   Equation: $D_n \Delta S = \rho_S \Delta S$.
*   **Conclusion**: $D_n = \rho_S$.
    *   **The electric flux density coming out is exactly equal to the surface charge density.**

### C. Summary of Conductor Rules
1.  Field inside is zero.
2.  Field outside is purely normal (perpendicular) to the surface.
3.  Magnitude of field outside is $E = \frac{\rho_S}{\epsilon_0}$.
4.  The conductor surface is an **Equipotential Surface** (Moving along the surface requires no work because $\mathbf{E}$ is perpendicular to the motion).

---

## 4. Implicit Knowledge & Assumptions
To fully grasp these notes, the reader is assumed to understand:
*   **Vector Algebra**: Dot products, cross products, magnitude.
*   **Coordinate Systems**: How to integrate over spheres ($r^2 \sin\theta d\theta d\phi$) and cylinders ($\rho d\rho d\phi dz$).
*   **Differentiation**: Partial derivatives for computing gradients.
*   **Physical Intuition**: The concept that "Infinity" is just a reference point far away from localized charges.
