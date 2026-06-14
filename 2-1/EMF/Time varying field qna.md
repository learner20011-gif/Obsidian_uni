### Derive the equation of continuity, $\nabla \cdot \vec{J} = -\frac{\partial \rho}{\partial t}$. Write the physical significance of the equation.

**Detailed Answer:**
The derivation of the continuity equation is based on the fundamental principle of conservation of charge. This principle states that charges can neither be created nor destroyed. 

Consider a given volume $v$ bounded by a closed surface $S$. If there is a net outward flow of current from this volume, the total charge inside the volume must decrease at the exact same rate. 
Let $I_{out}$ be the total current flowing out of the closed surface, and $Q_{in}$ be the total charge enclosed within the volume. The principle of charge conservation is expressed mathematically as:
$$I_{out} = -\frac{dQ_{in}}{dt}$$

We can express the total outward current as the closed surface integral of the current density vector $\vec{J}$:
$$I_{out} = \oint_S \vec{J} \cdot d\vec{S}$$

Next, we invoke the Divergence Theorem, which allows us to convert the surface integral into a volume integral:
$$\oint_S \vec{J} \cdot d\vec{S} = \int_v (\nabla \cdot \vec{J}) dv$$

We also know that the total enclosed charge $Q_{in}$ can be written as the volume integral of the volume charge density $\rho$ (often denoted as $\rho_v$):
$$Q_{in} = \int_v \rho \, dv$$

Taking the time derivative of $Q_{in}$ (and moving the derivative inside the integral as a partial derivative since the volume is fixed in space):
$$-\frac{dQ_{in}}{dt} = -\frac{d}{dt} \int_v \rho \, dv = -\int_v \frac{\partial \rho}{\partial t} dv$$

Now, equate the two volume integrals:
$$\int_v (\nabla \cdot \vec{J}) dv = -\int_v \frac{\partial \rho}{\partial t} dv$$

For this equality to hold true for any arbitrary volume $v$, the integrands themselves must be equal. Therefore, we arrive at the differential (or point) form of the continuity equation:
$$\nabla \cdot \vec{J} = -\frac{\partial \rho}{\partial t}$$

**Physical Significance:**
The physical significance of this equation is that it serves as the mathematical statement of the conservation of electric charge. It dictates that there can be no spontaneous accumulation or creation of charge at any point in space. If the divergence of the current density at a specific point is positive (meaning there is a net flow of current diverging *away* from that point), the charge density at that exact point must be decreasing over time (hence the negative sign on the partial derivative of $\rho$ with respect to time).

*(Related topic location: Section 5.8 "Continuity Equation and Relaxation Time", page 196 of the document).*

***

### (a) Write the Maxwell's equations for time-varying electric and magnetic fields. State how the curl-equation of magnetic field in time varying case differs from the static case.

**Detailed Answer:**
**Maxwell's Equations for Time-Varying Fields (Differential/Point Form):**
1. **Faraday's Law:** $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$
2. **Ampère's Circuit Law (modified by Maxwell):** $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$
3. **Gauss's Law for Electric Fields:** $\nabla \cdot \vec{D} = \rho_v$
4. **Gauss's Law for Magnetic Fields:** $\nabla \cdot \vec{B} = 0$

*(Where $\vec{E}$ is electric field intensity, $\vec{B}$ is magnetic flux density, $\vec{H}$ is magnetic field intensity, $\vec{D}$ is electric flux density, $\vec{J}$ is conduction current density, and $\rho_v$ is volume charge density).*

**How the Magnetic Field Curl Equation Differs:**
In the static case (magnetostatics), Ampère's law is simply $\nabla \times \vec{H} = \vec{J}$. 
In the time-varying (dynamic) case, the equation is modified to include an additional term, making it $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$.

The term $\frac{\partial \vec{D}}{\partial t}$ is known as the **displacement current density** ($\vec{J}_d$). Maxwell introduced this term to resolve a mathematical and physical contradiction. In static fields, the divergence of the curl of any vector is identically zero, so taking the divergence of Ampère's static law yields $\nabla \cdot (\nabla \times \vec{H}) = \nabla \cdot \vec{J} = 0$. However, for time-varying fields, the continuity equation dictates that $\nabla \cdot \vec{J} = -\frac{\partial \rho_v}{\partial t} \neq 0$. Therefore, the static form of Ampère's law fails under dynamic conditions. 

By adding the displacement current density, Maxwell ensured that taking the divergence of the modified equation results in:
$$\nabla \cdot (\nabla \times \vec{H}) = \nabla \cdot \vec{J} + \nabla \cdot \left(\frac{\partial \vec{D}}{\partial t}\right) = \nabla \cdot \vec{J} + \frac{\partial}{\partial t}(\nabla \cdot \vec{D})$$
Substituting Gauss's law ($\nabla \cdot \vec{D} = \rho_v$), this becomes:
$$0 = \nabla \cdot \vec{J} + \frac{\partial \rho_v}{\partial t}$$
This perfectly satisfies the continuity equation, allowing electromagnetic waves to propagate through spaces where no physical conduction current ($\vec{J}$) exists, such as in a vacuum or a dielectric (like between the plates of a capacitor).

*(Related topic location: Section 9.4 "Displacement Current", page 433, and Section 9.5 "Maxwell's Equations in Final Forms", page 436 of the document).*

***

### (b) A medium is having the characteristics of $\mu = 3 \times 10^{-5}$ H/m, $\varepsilon = 1.2 \times 10^{-10}$ F/m and $\sigma = 0$ everywhere. If the magnetic field intensity within that medium is $\vec{H} = 2 \cos(10^{10}t - \beta x)\vec{a}_y$ A/m, use Maxwell's equation to obtain the expressions for $\vec{B}$, $\vec{D}$, $\vec{E}$ and $\beta$.

**Detailed Answer:**

**1. Given Parameters:**
*   Permeability, $\mu = 3 \times 10^{-5}$ H/m
*   Permittivity, $\varepsilon = 1.2 \times 10^{-10}$ F/m
*   Conductivity, $\sigma = 0$ (This indicates a lossless dielectric medium)
*   Magnetic field intensity, $\vec{H} = 2 \cos(10^{10}t - \beta x)\vec{a}_y$ A/m
*   From the argument of the cosine function, the angular frequency is $\omega = 10^{10}$ rad/s.

**2. Expression for Magnetic Flux Density ($\vec{B}$):**
The relationship between $\vec{B}$ and $\vec{H}$ is given by $\vec{B} = \mu\vec{H}$.
$$\vec{B} = (3 \times 10^{-5}) \left[ 2 \cos(10^{10}t - \beta x)\vec{a}_y \right]$$
$$\vec{B} = 6 \times 10^{-5} \cos(10^{10}t - \beta x)\vec{a}_y \text{ Wb/m}^2 \text{ (or T)}$$

**3. Calculation of Phase Constant ($\beta$):**
For a lossless medium ($\sigma = 0$), the phase constant $\beta$ for a uniform plane wave is determined by the properties of the medium and the angular frequency:
$$\beta = \omega \sqrt{\mu \varepsilon}$$
$$\beta = 10^{10} \sqrt{(3 \times 10^{-5}) \times (1.2 \times 10^{-10})}$$
$$\beta = 10^{10} \sqrt{3.6 \times 10^{-15}} = 10^{10} \sqrt{36 \times 10^{-16}}$$
$$\beta = 10^{10} \times (6 \times 10^{-8}) = 600 \text{ rad/m}$$

**4. Expression for Electric Field Intensity ($\vec{E}$):**
To find $\vec{E}$, we use Maxwell's equation based on Ampère's law:
$$\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$$
Since the medium has $\sigma = 0$, the conduction current density $\vec{J} = \sigma \vec{E} = 0$. Using the constitutive relation $\vec{D} = \varepsilon \vec{E}$, the equation simplifies to:
$$\nabla \times \vec{H} = \varepsilon \frac{\partial \vec{E}}{\partial t}$$
First, we must calculate the curl of $\vec{H}$. Since $\vec{H}$ only has a $y$-component ($H_y$) and only depends on $x$ and $t$:
$$\nabla \times \vec{H} = \left| \begin{matrix} \vec{a}_x & \vec{a}_y & \vec{a}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 0 & H_y & 0 \end{matrix} \right| = \vec{a}_z \left( \frac{\partial H_y}{\partial x} \right)$$
Now, take the partial derivative of $H_y$ with respect to $x$:
$$H_y = 2 \cos(10^{10}t - \beta x)$$
$$\frac{\partial H_y}{\partial x} = 2 \left( -\sin(10^{10}t - \beta x) \right) \cdot (-\beta) = 2\beta \sin(10^{10}t - \beta x)$$
Therefore:
$$\nabla \times \vec{H} = 2\beta \sin(10^{10}t - \beta x) \vec{a}_z$$
Equating this to $\varepsilon \frac{\partial \vec{E}}{\partial t}$:
$$\varepsilon \frac{\partial \vec{E}}{\partial t} = 2\beta \sin(10^{10}t - \beta x) \vec{a}_z$$
$$\frac{\partial \vec{E}}{\partial t} = \frac{2\beta}{\varepsilon} \sin(10^{10}t - \beta x) \vec{a}_z$$
To find $\vec{E}$, we integrate with respect to time $t$:
$$\vec{E} = \int \frac{2\beta}{\varepsilon} \sin(10^{10}t - \beta x) \vec{a}_z \, dt$$
$$\vec{E} = \frac{2\beta}{\varepsilon} \left[ \frac{-\cos(10^{10}t - \beta x)}{10^{10}} \right] \vec{a}_z$$
Now, substitute the known values ($\beta = 600$, $\varepsilon = 1.2 \times 10^{-10}$, $\omega = 10^{10}$):
$$\text{Amplitude of } \vec{E} = -\frac{2 \times 600}{(1.2 \times 10^{-10}) \times 10^{10}} = -\frac{1200}{1.2} = -1000$$
Thus, the electric field intensity is:
$$\vec{E} = -1000 \cos(10^{10}t - 600x) \vec{a}_z \text{ V/m}$$

**5. Expression for Electric Flux Density ($\vec{D}$):**
Using the constitutive relation $\vec{D} = \varepsilon \vec{E}$:
$$\vec{D} = (1.2 \times 10^{-10}) \times \left[ -1000 \cos(10^{10}t - 600x) \vec{a}_z \right]$$
$$\vec{D} = -1.2 \times 10^{-7} \cos(10^{10}t - 600x) \vec{a}_z \text{ C/m}^2$$

**Summary of Results:**
*   $\beta = 600 \text{ rad/m}$
*   $\vec{B} = 6 \times 10^{-5} \cos(10^{10}t - 600x)\vec{a}_y \text{ Wb/m}^2$
*   $\vec{E} = -1000 \cos(10^{10}t - 600x)\vec{a}_z \text{ V/m}$
*   $\vec{D} = -1.2 \times 10^{-7} \cos(10^{10}t - 600x)\vec{a}_z \text{ C/m}^2$

*(Related topic location: Chapter 9, Example 9.8 "Time-Harmonic Fields" page 450, and Section 10.4 "Plane Waves in Lossless Dielectrics" page 487 of the document).*
### (a) Define displacement current. Explain the physical significance of displacement currents.

**Definition:**
Displacement current is a quantity representing the time rate of change of electric flux density (or displacement density) within a medium or free space. It is defined mathematically by the surface integral of the displacement current density ($J_d$). 
Since the displacement current density is given by $J_d = \frac{\partial D}{\partial t}$, the total displacement current $I_d$ crossing a given surface $S$ is:
$$I_d = \int_S J_d \cdot dS = \int_S \frac{\partial D}{\partial t} \cdot dS$$
where $D$ is the electric flux density ($D = \varepsilon E$).

**Physical Significance:**
The introduction of the displacement current by James Clerk Maxwell was physically significant because it resolved a major inconsistency in Ampère’s circuit law for time-varying fields. In static conditions, Ampère's law ($\nabla \times H = J$) suggests that the divergence of current density is zero ($\nabla \cdot J = 0$), which violates the continuity of current equation ($\nabla \cdot J = -\frac{\partial \rho_v}{\partial t}$) under dynamic (time-varying) conditions. 

By adding the displacement current density term, the modified Ampère’s law becomes $\nabla \times H = J + \frac{\partial D}{\partial t}$. Physically, this indicates that a time-varying electric field produces a magnetic field, just as a conduction current does. This explains how an electromagnetic wave can propagate through a vacuum or a dielectric where no actual conduction charge carriers exist (such as the gap between the plates of a charging capacitor). It establishes the fundamental symmetry between electric and magnetic fields that allows for the existence of electromagnetic radiation.

*(Related location in the provided documents: PDF 1, Pages 260-264; PDF 2, Pages 433-435)*

***

### Write the time harmonic equation of plane wave as a solution of Helmholtz's phasor-vector wave equation. Using the expression, obtain the equation of phase velocity of the wave interms of constituent properties of the medium.

**Time Harmonic Equation as a Solution:**
Helmholtz's phasor-vector wave equation for the electric field in a source-free, lossless medium is given by $\nabla^2 \mathbf{E}_s = -\omega^2 \mu \varepsilon \mathbf{E}_s$. 
If we assume a uniform plane wave propagating in the positive $z$-direction with the electric field polarized along the $x$-axis, the phasor solution to this differential equation is:
$$\mathbf{E}_{xs}(z) = E_{x0} e^{-j\beta z}$$
To obtain the instantaneous time-harmonic equation, we reinsert the time factor $e^{j\omega t}$ and take the real part:
$$\mathbf{E}_x(z, t) = \text{Re} \left[ E_{x0} e^{-j\beta z} e^{j\omega t} \right]$$
$$\mathbf{E}_x(z, t) = E_{x0} \cos(\omega t - \beta z)$$
where:
*   $E_{x0}$ is the amplitude of the electric field.
*   $\omega$ is the angular frequency.
*   $\beta$ is the phase constant (or wave number), where $\beta = \omega\sqrt{\mu\varepsilon}$.

**Derivation of Phase Velocity:**
The phase velocity ($v$ or $u_p$) is the velocity at which a point of constant phase on the wave travels through space. 
From the time-harmonic wave equation $E_x(z, t) = E_{x0} \cos(\omega t - \beta z)$, the phase of the wave is the argument of the cosine function:
$$\text{Phase} = \omega t - \beta z$$
For a fixed point on the wave (a point of constant phase), we set this phase expression to a constant:
$$\omega t - \beta z = \text{constant}$$
To find the velocity at which this constant phase point moves, we differentiate the equation with respect to time $t$:
$$\frac{d}{dt} (\omega t - \beta z) = \frac{d}{dt} (\text{constant})$$
$$\omega - \beta \frac{dz}{dt} = 0$$
Since velocity $v = \frac{dz}{dt}$, we can solve for $v$:
$$\beta v = \omega \implies v = \frac{\omega}{\beta}$$
Now, substituting the constituent properties of the medium using the relation $\beta = \omega\sqrt{\mu\varepsilon}$ (where $\mu$ is permeability and $\varepsilon$ is permittivity):
$$v = \frac{\omega}{\omega\sqrt{\mu\varepsilon}} = \frac{1}{\sqrt{\mu\varepsilon}}$$
Thus, the phase velocity of the wave is determined entirely by the constituent properties ($\mu$ and $\varepsilon$) of the medium.

*(Related location in the provided documents: PDF 1, Pages 275-281, 288-289; PDF 2, Pages 641-642)*

***

### a) Explain Ampere's circuital law and non-existence of magnetic monopole.

**Ampère's Circuital Law:**
Ampère's circuit law states that the line integral of the tangential component of the magnetic field intensity ($\mathbf{H}$) around any closed path is exactly equal to the net direct current ($I_{enc}$) enclosed by that path. 
Mathematically, it is expressed in integral form as:
$$\oint_L \mathbf{H} \cdot d\mathbf{l} = I_{enc} = \int_S \mathbf{J} \cdot d\mathbf{S}$$
In differential (or point) form for static fields, applying Stokes' theorem gives:
$$\nabla \times \mathbf{H} = \mathbf{J}$$
This law is the magnetostatic equivalent of Gauss's law for electrostatics. It is highly useful and easily applied to determine the magnetic field intensity when a current distribution is highly symmetrical (e.g., an infinite line current, an infinite current sheet, or a coaxial cable) by choosing a suitable "Amperian path" where $\mathbf{H}$ is constant in magnitude.

**Non-existence of Magnetic Monopole:**
In electrostatics, individual positive and negative charges (monopoles) exist and act as distinct sources and sinks for electric flux lines. However, in magnetostatics, no such isolated magnetic charges (magnetic monopoles) have ever been discovered. 

Magnetic poles always exist in pairs (North and South). If you take a bar magnet and break it in half, you do not isolate the North pole from the South pole; instead, you get two smaller magnets, each with its own complete North and South pole. Because isolated magnetic charges do not exist, magnetic flux lines do not have a starting or ending point; they must always form continuous, closed loops upon themselves. 

This physical property is mathematically formalized by Gauss's Law for Magnetic Fields, which states that the total magnetic flux leaving any closed surface must be exactly zero:
$$\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$$
In differential form, this implies that the divergence of the magnetic flux density is zero everywhere:
$$\nabla \cdot \mathbf{B} = 0$$
This equation conclusively shows that magnetostatic fields have no point sources or sinks, proving the non-existence of magnetic monopoles.

*(Related location in the provided documents: PDF 1, Pages 221, 244; PDF 2, Pages 309, 317-319)*
### (a) Define conduction, convection and displacement currents. Show that, $\nabla \times \bar{E} = -\frac{\partial \bar{B}}{\partial t}$, where the symbols have their usual meanings.

**Definitions of Currents:**

1.  **Conduction Current:** This current requires a conductor and is caused by the motion of charge carriers (usually free electrons) in a region of zero net charge density due to an applied or impressed electric field. It obeys Ohm's law. The conduction current density is mathematically defined as $\mathbf{J}_c = \sigma \mathbf{E}$, where $\sigma$ is the conductivity of the material and $\mathbf{E}$ is the electric field intensity.
2.  **Convection Current:** This current occurs when charge flows through an insulating medium (like a vacuum, liquid, or rarefied gas) and is distinct from conduction current because it does not involve conductors and consequently does not satisfy Ohm's law. An example is a beam of electrons in a vacuum tube. The convection current density is defined as $\mathbf{J}_v = \rho_v \mathbf{u}$, where $\rho_v$ is the volume charge density and $\mathbf{u}$ is the velocity of the charges.
3.  **Displacement Current:** This is not a physical current representing the transfer of actual charge carriers; rather, it is a theoretical quantity representing the time rate of change of the electric flux density (or displacement density). It is a result of a time-varying electric field, such as the apparent current "flowing" through a capacitor's dielectric when an alternating voltage is applied. The displacement current density is defined as $\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t}$, where $\mathbf{D}$ is the electric flux density.

*(Related locations: Section 5.3 "Convection and Conduction Currents", Pages 178-180 (PDF 2); Section 9.4 "Displacement Current", Pages 433-435 (PDF 2); Page 264-265 (PDF 1))*

**Proof that $\nabla \times \bar{E} = -\frac{\partial \bar{B}}{\partial t}$:**

This equation is the differential (or point) form of Faraday's Law.
According to Faraday's experiments, a time-varying magnetic field produces an induced voltage (electromotive force, or emf) in a closed circuit. Faraday's law states that this induced emf is equal to the negative time rate of change of the magnetic flux linkage:
$$V_{emf} = -\frac{d\Phi}{dt}$$

We know that the induced emf can be defined as the line integral of the electric field intensity $\mathbf{E}$ around the closed path $L$:
$$V_{emf} = \oint_L \mathbf{E} \cdot d\mathbf{l}$$

We also know that the magnetic flux $\Phi$ passing through the surface $S$ bounded by the path $L$ is the surface integral of the magnetic flux density $\mathbf{B}$:
$$\Phi = \int_S \mathbf{B} \cdot d\mathbf{S}$$

Substituting the integral expressions for $V_{emf}$ and $\Phi$ back into Faraday's law gives the integral form of Maxwell's equation:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{S}$$

For a stationary loop, the time derivative can be moved inside the surface integral as a partial derivative:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$$

Now, we apply Stokes's theorem to the left-hand side of the equation. Stokes's theorem relates the line integral around a closed path to the surface integral of the curl over the bounded surface:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S}$$

Equating the two surface integrals:
$$\int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$$

For these two integrals to be equal for any arbitrary surface $S$, their integrands must be identical. Therefore, we arrive at the differential form:
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

*(Related location: Section 9.2 "Faraday's Law" and 9.3 "Transformer and Motional Electromotive Forces", Pages 422-425 (PDF 2); Page 250-253 (PDF 1))*

---

### (b) Derive the Maxwell's equation $\nabla \times \bar{H} = \bar{J}$ for static field from Ampere's circuital law using Stoke's theorem.

**Derivation:**

Ampère's circuit law for static magnetic fields states that the line integral of the magnetic field intensity $\mathbf{H}$ around a closed path $L$ is exactly equal to the net direct current $I_{enc}$ enclosed by that path.
Mathematically, the integral form is written as:
$$\oint_L \mathbf{H} \cdot d\mathbf{l} = I_{enc}$$

We can express the enclosed current $I_{enc}$ as the surface integral of the surface current density $\mathbf{J}$ passing through any surface $S$ bounded by the closed path $L$:
$$I_{enc} = \int_S \mathbf{J} \cdot d\mathbf{S}$$

Substituting this expression for current into Ampère's law gives:
$$\oint_L \mathbf{H} \cdot d\mathbf{l} = \int_S \mathbf{J} \cdot d\mathbf{S}$$

Next, we apply Stokes's theorem to the left-hand side of the equation. Stokes's theorem transforms the line integral of a vector field over a closed loop into the surface integral of the curl of that vector field over the surface bounded by the loop:
$$\oint_L \mathbf{H} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{H}) \cdot d\mathbf{S}$$

Now, we equate the two surface integral expressions:
$$\int_S (\nabla \times \mathbf{H}) \cdot d\mathbf{S} = \int_S \mathbf{J} \cdot d\mathbf{S}$$

Because this equality must hold true for any arbitrary surface $S$ chosen to be bounded by the path $L$, the integrands themselves must be equal. By comparing the integrands, we obtain the differential (or point) form of Ampère's law for static fields:
$$\nabla \times \mathbf{H} = \mathbf{J}$$

*(Related location: Section 7.3 "Ampère's Circuit Law—Maxwell's Equation", Page 309 (PDF 2); Pages 221-223 (PDF 1))*

---

### Q.6 (b) — Stating and proving Poynting theorem

**Statement of Poynting Theorem:**
Poynting's theorem states that the net power flowing out of a given volume $v$ is equal to the time rate of decrease in the energy stored within the volume $v$ minus the ohmic (conduction) power losses dissipated as heat within that volume.

**Proof/Derivation:**
We begin with Maxwell's curl equation for magnetic fields (modified Ampère's law) in a medium:
$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

Take the dot product of both sides of this equation with the electric field intensity vector $\mathbf{E}$:
$$\mathbf{E} \cdot (\nabla \times \mathbf{H}) = \mathbf{E} \cdot \mathbf{J} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

Next, we make use of the standard vector identity: $\nabla \cdot (\mathbf{A} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{A}) - \mathbf{A} \cdot (\nabla \times \mathbf{B})$. Applying this identity to the vectors $\mathbf{E}$ and $\mathbf{H}$, we get:
$$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{H})$$
Rearranging this to isolate the $\mathbf{E} \cdot (\nabla \times \mathbf{H})$ term gives:
$$\mathbf{E} \cdot (\nabla \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \nabla \cdot (\mathbf{E} \times \mathbf{H})$$

Substitute this back into our original dot-product equation:
$$\mathbf{H} \cdot (\nabla \times \mathbf{E}) - \nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

Now, substitute Faraday's law ($\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$) into the first term:
$$\mathbf{H} \cdot \left(-\frac{\partial \mathbf{B}}{\partial t}\right) - \nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

Rearranging the terms so that the divergence term is on one side, we get the point (differential) form of the theorem:
$$-\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} + \mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t}$$

Assuming linear, isotropic, and homogeneous media where $\mathbf{D} = \varepsilon \mathbf{E}$ and $\mathbf{B} = \mu \mathbf{H}$, we can rewrite the time derivative terms:
$$\mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} = \mathbf{E} \cdot \frac{\partial (\varepsilon \mathbf{E})}{\partial t} = \frac{\varepsilon}{2} \frac{\partial E^2}{\partial t} = \frac{\partial}{\partial t} \left(\frac{1}{2} \varepsilon E^2\right)$$
$$\mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} = \mathbf{H} \cdot \frac{\partial (\mu \mathbf{H})}{\partial t} = \frac{\mu}{2} \frac{\partial H^2}{\partial t} = \frac{\partial}{\partial t} \left(\frac{1}{2} \mu H^2\right)$$

Substituting these back yields:
$$-\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \frac{\partial}{\partial t} \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right)$$

Finally, to get the integral form of Poynting's theorem, we integrate both sides over a volume $v$:
$$-\int_v \nabla \cdot (\mathbf{E} \times \mathbf{H}) dv = \int_v \mathbf{J} \cdot \mathbf{E} \, dv + \frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv$$

Apply the divergence theorem to the left-hand side ($\int_v \nabla \cdot \mathbf{A} \, dv = \oint_S \mathbf{A} \cdot d\mathbf{S}$) to convert the volume integral to a closed surface integral:
$$-\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} = \frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv + \int_v \mathbf{J} \cdot \mathbf{E} \, dv$$

**Interpretation of terms:**
*   $\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S}$: The total power leaving the volume $v$ through its surface $S$. The vector $\mathscr{P} = \mathbf{E} \times \mathbf{H}$ is the **Poynting vector**.
*   $\frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv$: The time rate of change (decrease, due to the negative sign on the LHS) of the total stored electric and magnetic energy within the volume.
*   $\int_v \mathbf{J} \cdot \mathbf{E} \, dv$ (or $\int_v \sigma E^2 dv$ since $\mathbf{J}=\sigma\mathbf{E}$): The total ohmic power dissipated as heat within the volume.

*(Related location: "The Poynting Vector and Power Considerations", Pages 340-344 (PDF 1))*
### (a) Explain the concepts of conduction, convection and displacement current.

**Detailed Answer:**

**1. Conduction Current:**
Conduction current requires the presence of a conductor (such as copper or aluminum). It is characterized by the motion of free charge carriers, typically electrons, in a region of zero net charge density. When an external electric field $\mathbf{E}$ is applied to a conductor, it exerts a force on these free electrons, causing them to drift and thereby producing a current. Because the electrons suffer constant collisions with the atomic lattice, they attain an average drift velocity that is directly proportional to the applied field. 
This relationship is described by the point form of Ohm's law:
$$\mathbf{J}_c = \sigma \mathbf{E}$$
where $\mathbf{J}_c$ is the conduction current density and $\sigma$ is the conductivity of the material. 
*(Related location: PDF 2, Section 5.3 "Convection and Conduction Currents", pages 178-180; PDF 1, page 265)*

**2. Convection Current:**
Convection current is distinct from conduction current because it does not involve conductors and, consequently, does not satisfy Ohm's law. It occurs when there is a flow of charge through an insulating medium, such as a vacuum, a rarefied gas, or a liquid. A classic example of convection current is a beam of electrons traveling through a vacuum tube.
If there is a flow of volume charge density $\rho_v$ moving with a velocity $\mathbf{u}$, the convection current density $\mathbf{J}_v$ is defined as:
$$\mathbf{J}_v = \rho_v \mathbf{u}$$
*(Related location: PDF 2, Section 5.3 "Convection and Conduction Currents", pages 178-179; PDF 1, page 265)*

**3. Displacement Current:**
Displacement current was a concept introduced by James Clerk Maxwell to resolve an inconsistency between Ampère's circuit law and the continuity of current equation for time-varying fields. Unlike conduction and convection currents, displacement current does not involve the actual physical transfer or motion of charge carriers. Instead, it is a result of a time-varying electric field. 
It is defined as the time rate of change of the electric flux density (or displacement density) $\mathbf{D}$. The displacement current density $\mathbf{J}_d$ is given by:
$$\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t}$$
This current accounts for the "flow" of current through regions where no conduction current can exist, such as through the dielectric material between the plates of an AC capacitor, allowing for the propagation of electromagnetic waves in free space.
*(Related location: PDF 2, Section 9.4 "Displacement Current", pages 433-435; PDF 1, pages 260, 264)*

***

### (b) State and explain Faraday's law of electromagnetic induction and hence show that $\bar{E} = -\nabla V - \frac{\partial \bar{A}}{\partial t}$, where the symbols have their usual meanings.

**Detailed Answer:**

**Faraday's Law of Electromagnetic Induction:**
Faraday's law states that a time-varying magnetic field produces an induced voltage (or electromotive force, emf) in any closed circuit. Specifically, the induced emf ($V_{emf}$) in a closed circuit is equal to the negative time rate of change of the magnetic flux linkage ($\Psi$) by the circuit. 
Mathematically, this is expressed as:
$$V_{emf} = -\frac{d\Psi}{dt}$$
The negative sign indicates Lenz's law: the induced voltage acts in such a way as to oppose the change in the flux producing it. 
In terms of electric field intensity $\mathbf{E}$ and magnetic flux density $\mathbf{B}$, the emf is the closed line integral of $\mathbf{E}$, and the flux is the surface integral of $\mathbf{B}$. Thus, the integral form is:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{S}$$
Applying Stokes' theorem and equating the integrands yields the differential (point) form of Faraday's Law:
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
*(Related location: PDF 2, Section 9.2 "Faraday's Law", page 422; PDF 1, page 250)*

**Proof of $\mathbf{E} = -\nabla V - \frac{\partial \mathbf{A}}{\partial t}$:**
*(Note: The prompt uses total derivative notation $\frac{d\bar{A}}{dt}$, but standard electromagnetic theory, as well as the provided text, utilizes the partial derivative $\frac{\partial \mathbf{A}}{\partial t}$ since $\mathbf{A}$ is a function of both space and time. The proof follows the text's rigorous derivation).*

1.  We begin with Gauss's law for magnetic fields, which states that the divergence of magnetic flux density is zero:
    $$\nabla \cdot \mathbf{B} = 0$$
2.  Because the divergence of the curl of any vector field is identically zero ($\nabla \cdot (\nabla \times \mathbf{A}) = 0$), we can define the magnetic flux density $\mathbf{B}$ in terms of a magnetic vector potential $\mathbf{A}$:
    $$\mathbf{B} = \nabla \times \mathbf{A}$$
3.  We substitute this definition of $\mathbf{B}$ into the differential form of Faraday's law ($\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$):
    $$\nabla \times \mathbf{E} = -\frac{\partial}{\partial t}(\nabla \times \mathbf{A})$$
4.  Since spatial and temporal differentiations are independent, we can swap the order of the curl and the time derivative on the right side:
    $$\nabla \times \mathbf{E} = -\nabla \times \left(\frac{\partial \mathbf{A}}{\partial t}\right)$$
5.  Rearranging the terms to group the curl operations yields:
    $$\nabla \times \left(\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t}\right) = 0$$
6.  A fundamental vector identity states that the curl of the gradient of any scalar field is always zero ($\nabla \times (-\nabla V) = 0$). Therefore, the term inside the parentheses must be equal to the negative gradient of an electric scalar potential $V$:
    $$\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} = -\nabla V$$
7.  Rearranging this equation gives the final expression relating the time-varying electric field to the scalar and vector potentials:
    $$\mathbf{E} = -\nabla V - \frac{\partial \mathbf{A}}{\partial t}$$
*(Related location: PDF 2, Section 9.6 "Time-Varying Potentials", page 439)*

***

### (c) State and prove Poynting theorem.

**Detailed Answer:**

**Statement of the Theorem:**
Poynting's theorem states that the net power flowing out of a given volume $v$ is equal to the time rate of decrease in the energy stored within the volume $v$ minus the ohmic (conduction) power losses dissipated as heat within that volume.

**Proof of the Theorem:**
1.  We begin with Maxwell's curl equation for magnetic fields (Ampère's circuit law for time-varying fields):
    $$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

2.  To introduce power (which relates to $\mathbf{E} \cdot \mathbf{J}$), we take the dot product of both sides of this equation with the electric field intensity $\mathbf{E}$:
    $$\mathbf{E} \cdot (\nabla \times \mathbf{H}) = \mathbf{E} \cdot \mathbf{J} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

3.  We utilize a standard vector identity involving the divergence of a cross product:
    $$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{H})$$
    Rearranging this identity to solve for $\mathbf{E} \cdot (\nabla \times \mathbf{H})$ gives:
    $$\mathbf{E} \cdot (\nabla \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \nabla \cdot (\mathbf{E} \times \mathbf{H})$$

4.  Substitute this back into the equation from step 2:
    $$\mathbf{H} \cdot (\nabla \times \mathbf{E}) - \nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

5.  Next, substitute Faraday's law ($\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$) into the first term on the left side:
    $$\mathbf{H} \cdot \left(-\frac{\partial \mathbf{B}}{\partial t}\right) - \nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}$$

6.  Rearrange the equation to isolate the divergence term (representing outward flow):
    $$-\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} + \mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t}$$

7.  Assuming a linear, isotropic, and homogeneous medium where $\mathbf{D} = \varepsilon \mathbf{E}$ and $\mathbf{B} = \mu \mathbf{H}$, we can rewrite the time-derivative terms as follows:
    $$\mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} = \mathbf{E} \cdot \frac{\partial (\varepsilon \mathbf{E})}{\partial t} = \frac{1}{2}\frac{\partial (\varepsilon E^2)}{\partial t}$$
    $$\mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} = \mathbf{H} \cdot \frac{\partial (\mu \mathbf{H})}{\partial t} = \frac{1}{2}\frac{\partial (\mu H^2)}{\partial t}$$
    Substituting these back into the equation yields the differential (point) form of Poynting's theorem:
    $$-\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{J} \cdot \mathbf{E} + \frac{\partial}{\partial t} \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right)$$

8.  To obtain the integral form, we integrate both sides over a volume $v$:
    $$-\int_v \nabla \cdot (\mathbf{E} \times \mathbf{H}) dv = \int_v \mathbf{J} \cdot \mathbf{E} \, dv + \frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv$$

9.  Finally, apply the divergence theorem ($\int_v \nabla \cdot \mathbf{A} \, dv = \oint_S \mathbf{A} \cdot d\mathbf{S}$) to the left side to convert the volume integral into a closed surface integral:
    $$-\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} = \frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv + \int_v \mathbf{J} \cdot \mathbf{E} \, dv$$

    *   The term $\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S}$ represents the total power leaving the volume. The vector $\mathscr{P} = \mathbf{E} \times \mathbf{H}$ is the **Poynting vector**.
    *   The term involving the time derivative represents the rate of decrease in stored electric and magnetic energy.
    *   The term $\int_v \mathbf{J} \cdot \mathbf{E} \, dv$ represents the ohmic power dissipated as heat.

*(Related location: PDF 1, "The Poynting Vector and Power Considerations", pages 340-344)*

***

### (d) What is meant by polarization of electromagnetic wave?

**Detailed Answer:**
In the context of uniform plane waves, the polarization of an electromagnetic wave refers to the orientation and time-varying behavior of the electric field ($\mathbf{E}$) vector as the wave propagates through space. 

Because a uniform plane wave is a transverse electromagnetic (TEM) wave, both the electric field ($\mathbf{E}$) and the magnetic field ($\mathbf{H}$) are always perpendicular to the direction of wave propagation. However, the $\mathbf{E}$ field vector can still be oriented in various ways within that perpendicular plane. 

When analyzing the reflection of a plane wave at an oblique incidence boundary between two media, any arbitrary polarization of the wave can be decomposed into a linear combination of two fundamental cases:
1.  **Parallel Polarization:** The electric field vector ($\mathbf{E}$) lies entirely *within* the plane of incidence (the plane containing the propagation vector and the normal to the boundary surface).
2.  **Perpendicular Polarization:** The electric field vector ($\mathbf{E}$) is entirely *perpendicular* to the plane of incidence.

Therefore, the term polarization specifies the exact spatial alignment of the $\mathbf{E}$ field as it travels.
*(Related location: PDF 1, "Reflection of a Plane Wave at Oblique Incidence", page 391; "A. Parallel Polarization", page 392; "B. Perpendicular Polarization", page 402)*
### Write down the Maxwell's equation in phasor form and hence derive the wave equation for electric field E in source free generalized medium.

*(Related location: PDF 1, "WAVE PROPAGATION IN LOSSY DIELECTRICS", Pages 304-306; PDF 2, Section 9.7 "Time-Harmonic Fields", Page 445)*

**Maxwell's Equations in Phasor Form:**
Consider a linear, isotropic, homogeneous, generalized medium with conductivity $\sigma$, permittivity $\varepsilon$, and permeability $\mu$. For a source-free region, there are no independent free charges ($\rho_v = 0$) or independent current sources, though conduction current $\mathbf{J} = \sigma\mathbf{E}$ will exist due to the medium's conductivity.
Assuming a time-harmonic variation (where the time dependence $e^{j\omega t}$ is suppressed), the phasor forms of Maxwell's equations are:
1.  **Gauss's Law:** $\nabla \cdot \mathbf{E}_s = 0$
2.  **Gauss's Law for Magnetic Fields:** $\nabla \cdot \mathbf{H}_s = 0$
3.  **Faraday's Law:** $\nabla \times \mathbf{E}_s = -j\omega\mu \mathbf{H}_s$
4.  **Ampère's Circuit Law:** $\nabla \times \mathbf{H}_s = \mathbf{J}_s + j\omega\varepsilon\mathbf{E}_s$
    Substituting $\mathbf{J}_s = \sigma\mathbf{E}_s$, this becomes:
    $\nabla \times \mathbf{H}_s = (\sigma + j\omega\varepsilon)\mathbf{E}_s$

**Derivation of the Wave Equation:**
To derive the wave equation for the electric field, we start by taking the curl of both sides of Faraday's Law:
$$\nabla \times (\nabla \times \mathbf{E}_s) = \nabla \times (-j\omega\mu \mathbf{H}_s)$$
$$\nabla \times \nabla \times \mathbf{E}_s = -j\omega\mu (\nabla \times \mathbf{H}_s)$$

Next, we apply the vector identity for the curl of a curl: $\nabla \times \nabla \times \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$. Applying this to $\mathbf{E}_s$:
$$\nabla(\nabla \cdot \mathbf{E}_s) - \nabla^2 \mathbf{E}_s = -j\omega\mu (\nabla \times \mathbf{H}_s)$$

Since the medium is source-free ($\rho_v = 0$), Gauss's Law states that $\nabla \cdot \mathbf{E}_s = 0$. The first term on the left side vanishes:
$$-\nabla^2 \mathbf{E}_s = -j\omega\mu (\nabla \times \mathbf{H}_s)$$

Now, we substitute the modified Ampère's Law ($\nabla \times \mathbf{H}_s = (\sigma + j\omega\varepsilon)\mathbf{E}_s$) into the right side of the equation:
$$-\nabla^2 \mathbf{E}_s = -j\omega\mu (\sigma + j\omega\varepsilon)\mathbf{E}_s$$

Rearranging the terms, we obtain the standard wave equation (also known as the Helmholtz equation) for the electric field:
$$\nabla^2 \mathbf{E}_s - j\omega\mu(\sigma + j\omega\varepsilon)\mathbf{E}_s = 0$$
$$\nabla^2 \mathbf{E}_s - \gamma^2 \mathbf{E}_s = 0$$

Where $\gamma$ is the complex propagation constant of the medium, defined as:
$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)} = \alpha + j\beta$$
Here, $\alpha$ is the attenuation constant and $\beta$ is the phase constant.

---

### (a) Write down the Maxwell's equations in point form and integral form.

*(Related location: PDF 2, Section 9.5 "Maxwell's Equations in Final Forms", Table 9.1, Page 436)*

The general forms of Maxwell's equations for time-varying fields are summarized below:

| Law | Differential (Point) Form | Integral Form |
| :--- | :--- | :--- |
| **Faraday's Law** | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | $\oint_L \mathbf{E} \cdot d\mathbf{l} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$ |
| **Ampère's Circuit Law** | $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$ | $\oint_L \mathbf{H} \cdot d\mathbf{l} = \int_S \left( \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \right) \cdot d\mathbf{S}$ |
| **Gauss's Law (Electric)** | $\nabla \cdot \mathbf{D} = \rho_v$ | $\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_v \rho_v dv$ |
| **Gauss's Law (Magnetic)** | $\nabla \cdot \mathbf{B} = 0$ | $\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$ |

*(Where $\mathbf{E}$ is electric field intensity, $\mathbf{D}$ is electric flux density, $\mathbf{H}$ is magnetic field intensity, $\mathbf{B}$ is magnetic flux density, $\mathbf{J}$ is conduction current density, and $\rho_v$ is volume charge density).*

---

### (b) What is displacement current? Compare the conduction and displacement current densities in copper ($\varepsilon \cong \varepsilon_0, \mu \cong \mu_0$ and $\sigma = 5.8 \times 10^7$ s/m) at a frequency of 1 MHz.

*(Related location: PDF 1, Slide 264; Slide 318. PDF 2, Section 9.4 "Displacement Current", Pages 433-435)*

**What is Displacement Current?**
Displacement current is a quantity introduced by James Clerk Maxwell to resolve a theoretical contradiction between Ampère's law and the conservation of charge (continuity equation) in time-varying situations. It is defined as the time rate of change of the electric flux density (or displacement field) $\mathbf{D}$. 

Unlike conduction or convection currents, displacement current does not involve the physical movement of charge carriers (like electrons). Instead, it arises purely from a changing electric field. For example, it represents the apparent current that "flows" across the dielectric gap of a capacitor as it charges or discharges.

Mathematically, the displacement current density $\mathbf{J}_d$ is given by:
$$\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t} = \varepsilon \frac{\partial \mathbf{E}}{\partial t}$$
The total displacement current $I_d$ crossing a surface $S$ is:
$$I_d = \int_S \mathbf{J}_d \cdot d\mathbf{S} = \int_S \frac{\partial \mathbf{D}}{\partial t} \cdot d\mathbf{S}$$

**Comparison of Current Densities in Copper:**
To compare the two, we look at the ratio of the magnitude of the conduction current density ($|\mathbf{J}_c|$) to the magnitude of the displacement current density ($|\mathbf{J}_d|$). 
For a time-harmonic field $\mathbf{E} = \mathbf{E}_s e^{j\omega t}$:
*   Conduction current density phasor: $\mathbf{J}_{cs} = \sigma \mathbf{E}_s$
*   Displacement current density phasor: $\mathbf{J}_{ds} = j\omega\varepsilon \mathbf{E}_s$

The ratio of their magnitudes is equivalent to the loss tangent of the medium:
$$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{\sigma |\mathbf{E}_s|}{\omega\varepsilon |\mathbf{E}_s|} = \frac{\sigma}{\omega\varepsilon}$$

**Given Values for Copper:**
*   Conductivity, $\sigma = 5.8 \times 10^7$ S/m
*   Frequency, $f = 1$ MHz $= 10^6$ Hz $\implies$ Angular frequency, $\omega = 2\pi f = 2\pi \times 10^6$ rad/s
*   Permittivity, $\varepsilon \cong \varepsilon_0 \approx 8.854 \times 10^{-12}$ F/m $\approx \frac{10^{-9}}{36\pi}$ F/m

**Calculation:**
$$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{5.8 \times 10^7}{ (2\pi \times 10^6) \times \left(\frac{10^{-9}}{36\pi}\right) }$$
$$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{5.8 \times 10^7}{ \frac{2 \times 10^{-3}}{36} }$$
$$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{5.8 \times 10^7 \times 36}{2 \times 10^{-3}}$$
$$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = 2.9 \times 36 \times 10^{10} = 104.4 \times 10^{10} = 1.044 \times 10^{12}$$

**Conclusion:**
At a frequency of 1 MHz in copper, the conduction current density is over a trillion ($10^{12}$) times larger than the displacement current density. This demonstrates that in good conductors like copper, the displacement current is completely negligible compared to the conduction current at frequencies up to the microwave range.

---

### (c) Does the electric field in vacuum, $\mathbf{E} = E_0 \cos(\omega t - \beta x)\mathbf{a}_x$ satisfy Maxwell's equations? Under what circumstances would this $\mathbf{E}$ satisfy the equations?

*(Related concept location: PDF 1, Slide 559 "Example 6" introduces this exact question. Analysis relies on applying Maxwell's equations from PDF 2, Section 9.5).*

**Analysis:**
Let us test the given electric field against Maxwell's equations for a vacuum (free space). In a vacuum, there are no source charges ($\rho_v = 0$) and no conduction currents ($\mathbf{J} = 0$).

The given field is $\mathbf{E} = E_0 \cos(\omega t - \beta x)\mathbf{a}_x$.

1.  **Test against Gauss's Law for Electric Fields:**
    In a source-free vacuum, Gauss's law is $\nabla \cdot \mathbf{E} = 0$.
    Let's calculate the divergence of the given field:
    $$\nabla \cdot \mathbf{E} = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}$$
    Since the field only has an $x$-component that depends on $x$:
    $$\nabla \cdot \mathbf{E} = \frac{\partial}{\partial x} \left[ E_0 \cos(\omega t - \beta x) \right]$$
    $$\nabla \cdot \mathbf{E} = E_0 \left( -\sin(\omega t - \beta x) \right) \cdot (-\beta)$$
    $$\nabla \cdot \mathbf{E} = \beta E_0 \sin(\omega t - \beta x)$$
    For Gauss's law to be satisfied in a vacuum, we require $\beta E_0 \sin(\omega t - \beta x) = 0$ for all $x$ and $t$.

**Does it satisfy the equations?**
**No, generally it does not.** For a standard propagating electromagnetic wave, the amplitude $E_0$ is non-zero, and the phase constant $\beta$ ($\beta = \omega/c$) is non-zero. Thus, the divergence is not zero, violating Gauss's law for a charge-free vacuum. 
Physically, the given equation describes a *longitudinal* wave (the field vector points in the same direction as propagation, $\mathbf{a}_x$). However, a fundamental property of electromagnetic waves in free space is that they must be *transverse* (TEM waves), meaning the electric and magnetic fields must be perpendicular to the direction of propagation.

**Under what circumstances would it satisfy the equations?**
For the condition $\beta E_0 \sin(\omega t - \beta x) = 0$ to hold true globally, there are a few restrictive circumstances:

1.  **Trivial Case:** $E_0 = 0$. There is no field.
2.  **Static DC Field:** If $\beta = 0$, then the wave is not propagating through space. If $\beta=0$, then $\omega = \beta c = 0$. 
    In this case, the field simplifies to $\mathbf{E} = E_0 \cos(0)\mathbf{a}_x = E_0 \mathbf{a}_x$.
    Let's test this static field $\mathbf{E} = E_0 \mathbf{a}_x$:
    *   $\nabla \cdot \mathbf{E} = \frac{\partial}{\partial x}(E_0) = 0$ (Satisfies Gauss's Law)
    *   $\nabla \times \mathbf{E} = 0$ (Satisfies Faraday's law, implying a static $\mathbf{H}$ field)
    *   $\frac{\partial \mathbf{E}}{\partial t} = 0$ (Satisfies Ampère's law if $\mathbf{H}$ is uniform or zero)
    Therefore, the field satisfies Maxwell's equations only if it degenerates into a uniform, static (DC) electric field.
3.  **Non-Vacuum Medium:** If we relax the "vacuum" constraint, the field *could* exist if the medium contains a very specific, time-varying volume charge density $\rho_v$. According to Gauss's law ($\nabla \cdot \mathbf{D} = \rho_v \implies \varepsilon_0 \nabla \cdot \mathbf{E} = \rho_v$), the required charge density would be $\rho_v(x,t) = \varepsilon_0 \beta E_0 \sin(\omega t - \beta x)$. Such a field describes a longitudinal plasma oscillation, but this cannot occur in a pure vacuum.
### Derive the phasor expressions for the electric and magnetic field intensity vectors of an x-polarized uniform plane wave propagating in the +z direction.

**Derivation:**

1.  **Start with the Wave Equation:**
    For a linear, isotropic, homogeneous, and source-free medium, the electric field phasor $\mathbf{E}_s$ satisfies the Helmholtz wave equation:
    $$\nabla^2 \mathbf{E}_s - \gamma^2 \mathbf{E}_s = 0$$
    where $\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$ is the complex propagation constant.

2.  **Apply Assumptions for the Specific Wave:**
    *   **Uniform Plane Wave:** The fields do not vary in the transverse plane. Therefore, all derivatives with respect to $x$ and $y$ are zero ($\frac{\partial}{\partial x} = 0$, $\frac{\partial}{\partial y} = 0$).
    *   **x-polarized:** The electric field vector points only in the $x$-direction, meaning $\mathbf{E}_s = E_{xs}(z)\mathbf{a}_x$.
    *   **Propagating in +z direction:** The wave travels along the positive $z$-axis.

3.  **Simplify the Wave Equation:**
    Substituting the assumptions into the general wave equation reduces it to a 1D ordinary differential equation:
    $$\frac{d^2 E_{xs}(z)}{dz^2} - \gamma^2 E_{xs}(z) = 0$$

4.  **Solve for the Electric Field Phasor ($\mathbf{E}_s$):**
    The general solution to this 2nd-order linear differential equation is a combination of forward and backward traveling waves:
    $$E_{xs}(z) = E_{x0}^+ e^{-\gamma z} + E_{x0}^- e^{+\gamma z}$$
    Since we are explicitly looking for a wave propagating *only* in the $+z$ direction, the coefficient for the backward-traveling wave ($E_{x0}^-$) must be zero. Let $E_{x0}^+ = E_0$.
    $$E_{xs}(z) = E_0 e^{-\gamma z}$$
    So, the full phasor vector expression for the electric field is:
    $$\mathbf{E}_s(z) = E_0 e^{-\gamma z} \mathbf{a}_x$$
    *(where $E_0$ is the complex amplitude at $z=0$)*.

5.  **Derive the Magnetic Field Phasor ($\mathbf{H}_s$):**
    To find the associated magnetic field, we use Faraday's Law in phasor form:
    $$\nabla \times \mathbf{E}_s = -j\omega\mu \mathbf{H}_s$$
    Calculate the curl of our specific $\mathbf{E}_s$:
    $$\nabla \times \mathbf{E}_s = \left| \begin{matrix} \mathbf{a}_x & \mathbf{a}_y & \mathbf{a}_z \\ 0 & 0 & \frac{\partial}{\partial z} \\ E_{xs}(z) & 0 & 0 \end{matrix} \right| = \mathbf{a}_y \frac{\partial E_{xs}(z)}{\partial z}$$
    Substitute $E_{xs}(z) = E_0 e^{-\gamma z}$:
    $$\nabla \times \mathbf{E}_s = \mathbf{a}_y \frac{d}{dz} (E_0 e^{-\gamma z}) = \mathbf{a}_y (-\gamma E_0 e^{-\gamma z})$$
    Now equate this to $-j\omega\mu \mathbf{H}_s$:
    $$-\gamma E_0 e^{-\gamma z} \mathbf{a}_y = -j\omega\mu \mathbf{H}_s$$
    Solve for $\mathbf{H}_s$:
    $$\mathbf{H}_s = \frac{\gamma}{j\omega\mu} E_0 e^{-\gamma z} \mathbf{a}_y$$
    We define the intrinsic wave impedance of the medium as $\eta = \frac{j\omega\mu}{\gamma} = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$. 
    Substituting $\eta$:
    $$\mathbf{H}_s(z) = \frac{E_0}{\eta} e^{-\gamma z} \mathbf{a}_y$$

**Final Expressions:**
*   **Electric Field Phasor:** $\mathbf{E}_s(z) = E_0 e^{-\gamma z} \mathbf{a}_x$
*   **Magnetic Field Phasor:** $\mathbf{H}_s(z) = \frac{E_0}{\eta} e^{-\gamma z} \mathbf{a}_y$

*(Related topic location: PDF 1, "Wave Motion in Perfect Dielectrics" & "Wave Propagation in Lossy Dielectrics", pages 284-288, 309-313)*

---

### What is meant by the skin depth of a conductor?

**Detailed Answer:**
As an electromagnetic wave propagates into a conducting medium (a lossy material where conductivity $\sigma \neq 0$), its amplitude decays exponentially due to the factor $e^{-\alpha z}$, where $\alpha$ is the attenuation constant. The energy of the wave is dissipated as heat (ohmic loss) as it interacts with the free charges in the conductor.

The **skin depth** (also known as the depth of penetration), denoted by the symbol $\delta$, is defined as the distance a wave must travel through a lossy medium to have its amplitude reduced by a factor of $e^{-1}$ (which is approximately $37\%$) of its initial value at the surface. 

Mathematically, it is the reciprocal of the attenuation constant:
$$\delta = \frac{1}{\alpha}$$
For a "good conductor" (where $\sigma \gg \omega\varepsilon$), the attenuation constant $\alpha$ is large, meaning the wave attenuates very rapidly. In this specific case, the skin depth simplifies to:
$$\delta \approx \frac{1}{\sqrt{\pi f \mu \sigma}}$$
This formula shows that the skin depth becomes incredibly small at high frequencies ($f$), for highly conductive materials ($\sigma$), or highly permeable materials ($\mu$). Because the fields and currents are confined to this extremely thin layer near the surface, the phenomenon is called the "skin effect."

*(Related topic location: PDF 1, "Plane Waves in Good Conductors", pages 331-334)*

---

### (b) Let $\mathbf{B} = 0.5 x \mathbf{a}_z$ T in the figure shown below. The position of the sliding bar is given by $x = 4t - 2t^2$. If the separation of the rails is $10$ cm, find the voltmeter reading $V_{ab}$ at : (i) $t = 0.5$ s, (ii) $x = 1$ m.
![[2-1/EMF/attachments/c538a64c-d064-4e27-a128-846b98dbeff2.jpg]]
**Detailed Answer:**

**1. Identify the Type of EMF:**
The setup involves a conducting bar moving through a static (time-invariant) but spatially varying magnetic field. Therefore, the induced voltage is a **motional EMF**.

**2. State the Given Information:**
*   Magnetic flux density: $\mathbf{B} = 0.5x \, \mathbf{a}_z$ (Tesla)
*   Position of the moving bar: $x(t) = 4t - 2t^2$ (meters)
*   Separation of rails (length of the bar in the field): $l = 10 \text{ cm} = 0.1 \text{ m}$
*   The bar is oriented parallel to the $y$-axis, so the differential length vector along the bar is $d\mathbf{l} = dy \, \mathbf{a}_y$.
*   The bar moves along the $x$-axis, so its velocity vector is $\mathbf{u} = v \, \mathbf{a}_x$.

**3. Calculate Velocity ($\mathbf{u}$):**
The velocity $v$ is the time derivative of the position $x(t)$:
$$v = \frac{dx}{dt} = \frac{d}{dt}(4t - 2t^2) = 4 - 4t$$
So, the velocity vector is $\mathbf{u} = (4 - 4t) \mathbf{a}_x$.

**4. Formulate the Motional EMF Equation:**
The motional EMF is given by:
$$V_{emf} = \int_L (\mathbf{u} \times \mathbf{B}) \cdot d\mathbf{l}$$
First, compute the cross product $\mathbf{u} \times \mathbf{B}$:
$$\mathbf{u} \times \mathbf{B} = \left( (4 - 4t)\mathbf{a}_x \right) \times \left( 0.5x \, \mathbf{a}_z \right)$$
Since $\mathbf{a}_x \times \mathbf{a}_z = -\mathbf{a}_y$:
$$\mathbf{u} \times \mathbf{B} = -0.5x(4 - 4t) \mathbf{a}_y$$
Now, substitute $x(t) = 4t - 2t^2$ into the expression:
$$\mathbf{u} \times \mathbf{B} = -0.5(4t - 2t^2)(4 - 4t) \mathbf{a}_y$$

Now, evaluate the line integral along the bar from $y=0$ to $y=0.1$:
$$V_{emf} = \int_0^{0.1} \left[ -0.5(4t - 2t^2)(4 - 4t) \mathbf{a}_y \right] \cdot (dy \, \mathbf{a}_y)$$
$$V_{emf} = -0.5(4t - 2t^2)(4 - 4t) \int_0^{0.1} dy$$
$$V_{emf} = -0.5(4t - 2t^2)(4 - 4t) [y]_0^{0.1}$$
$$V_{emf} = -0.05(4t - 2t^2)(4 - 4t)$$

*(Note regarding polarity: The problem asks for the voltmeter reading $V_{ab}$, which implies the potential at 'a' relative to 'b', so $V_{ab} = V_a - V_b$. The integral $\int (\mathbf{u} \times \mathbf{B}) \cdot d\mathbf{l}$ gives the emf driving current *in the direction* of $d\mathbf{l}$. Here $d\mathbf{l}$ is along $+y$ (from bottom rail to top rail). The $(\mathbf{u} \times \mathbf{B})$ force is along $-\mathbf{a}_y$. This pushes positive charge to the bottom rail ('b') and leaves negative charge at the top ('a'). Therefore, 'b' is at a higher potential than 'a', meaning $V_{ab}$ will be negative. The magnitude is what matters most for a generic "voltmeter reading", but we will compute the signed value based on the integral).*

**5. Evaluate at specific conditions:**

**Condition (i): At $t = 0.5$ s**
Substitute $t = 0.5$ into the $V_{emf}$ equation:
$$V_{ab}(t=0.5) = -0.05 \left[ 4(0.5) - 2(0.5)^2 \right] \left[ 4 - 4(0.5) \right]$$
$$V_{ab} = -0.05 \left[ 2 - 2(0.25) \right] \left[ 4 - 2 \right]$$
$$V_{ab} = -0.05 \left[ 2 - 0.5 \right] \left[ 2 \right]$$
$$V_{ab} = -0.05 \times [1.5] \times [2]$$
$$V_{ab} = -0.05 \times 3 = -0.15 \text{ Volts}$$
**The voltmeter reading at $t=0.5$ s is -0.15 V (or magnitude 0.15 V).**

**Condition (ii): At $x = 1$ m**
First, we must find the time $t$ when the bar is at position $x = 1$.
Set $x(t) = 1$:
$$4t - 2t^2 = 1$$
$$2t^2 - 4t + 1 = 0$$
Solve this quadratic equation for $t$ using the quadratic formula ($t = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$):
$$t = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(2)(1)}}{2(2)}$$
$$t = \frac{4 \pm \sqrt{16 - 8}}{4} = \frac{4 \pm \sqrt{8}}{4} = \frac{4 \pm 2\sqrt{2}}{4} = 1 \pm \frac{\sqrt{2}}{2}$$
So, $t \approx 1 \pm 0.707$. The bar is at $x=1$ at two different times: $t_1 \approx 0.293$ s and $t_2 \approx 1.707$ s.
We must calculate the voltage for both possible times.

Instead of plugging $t$ back in, we can express velocity in terms of $x$.
$v^2 = (4-4t)^2 = 16 - 32t + 16t^2 = 16 - 8(4t - 2t^2) = 16 - 8x$.
So $v = \pm \sqrt{16 - 8x}$.
At $x = 1$, $v = \pm \sqrt{16 - 8(1)} = \pm \sqrt{8} = \pm 2\sqrt{2}$ m/s.
The two velocities correspond to the bar moving forward and then backward through the point $x=1$.

Now, substitute $x=1$ and the corresponding velocities into the cross product:
$\mathbf{u} \times \mathbf{B} = (v \mathbf{a}_x) \times (0.5x \mathbf{a}_z) = -0.5 v x \mathbf{a}_y$
At $x=1$:
$\mathbf{u} \times \mathbf{B} = -0.5 (\pm 2\sqrt{2}) (1) \mathbf{a}_y = \mp \sqrt{2} \mathbf{a}_y$

Now, compute the integral:
$$V_{ab} = \int_0^{0.1} (\mp \sqrt{2} \mathbf{a}_y) \cdot (dy \mathbf{a}_y) = \mp \sqrt{2} \int_0^{0.1} dy = \mp 0.1\sqrt{2} \text{ Volts}$$

Since $\sqrt{2} \approx 1.414$:
$$V_{ab} = \mp 0.1414 \text{ Volts}$$
**The voltmeter reading when $x=1$ m is $-0.1414$ V (when moving forward) or $+0.1414$ V (when moving backward).**

*(Related concept location: PDF 2, Section 9.3 "Moving Loop in Static B Field (Motional emf)", pages 425-428)*
## Concise notes

Vacuum Permittivity (ε₀): 8.854 × 10⁻¹² F/m

Vacuum Permeability (μ₀): 4π × 10⁻⁷ H/m (approx. 1.257 × 10⁻⁶ H/m)

Here are the highly scannable, concise notes derived from the provided Q&A document.

***

### 1. CONTINUITY EQUATION & CHARGE CONSERVATION
*Ref: Sec 5.8, pg 196*

*   **Principle**: Charge is conserved. Cannot be created/destroyed.
*   **Formula**: Outward current = Rate of charge decrease.
    $$I_{out} = -\frac{dQ_{in}}{dt}$$
*   **Derivation**:
    1. Express $I_{out}$ as surface integral: $I_{out} = \oint_S \vec{J} \cdot d\vec{S}$
    2. Apply Divergence Thm: $\oint_S \vec{J} \cdot d\vec{S} = \int_v (\nabla \cdot \vec{J}) dv$
    3. Express $Q_{in}$ as volume integral: $Q_{in} = \int_v \rho dv \implies -\frac{dQ_{in}}{dt} = -\int_v \frac{\partial \rho}{\partial t} dv$
    4. Equate integrals: $\int_v (\nabla \cdot \vec{J}) dv = -\int_v \frac{\partial \rho}{\partial t} dv$
*   **Result (Point Form)**: 
    $$\nabla \cdot \vec{J} = -\frac{\partial \rho}{\partial t}$$
*   **Significance**: No spontaneous charge accumulation. Net current diverging from a point causes charge density $\rho$ to drop over time.


***

### 2. MAXWELL'S EQUATIONS
*Ref: Sec 9.5, pg 436, Table 9.1*

| Name | Point (Differential) Form | Integral Form |
| :--- | :--- | :--- |
| **Faraday's Law** | $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$ | $\oint_L \vec{E} \cdot d\vec{l} = -\int_S \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}$ |
| **Ampère's Law** | $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$ | $\oint_L \vec{H} \cdot d\vec{l} = \int_S \left( \vec{J} + \frac{\partial \vec{D}}{\partial t} \right) \cdot d\vec{S}$ |
| **Gauss (Electric)** | $\nabla \cdot \vec{D} = \rho_v$ | $\oint_S \vec{D} \cdot d\vec{S} = \int_v \rho_v dv$ |
| **Gauss (Magnetic)**| $\nabla \cdot \vec{B} = 0$ | $\oint_S \vec{B} \cdot d\vec{S} = 0$ |


***

### 3. CURRENTS & AMPÈRE'S LAW MODIFICATION
*Ref: Sec 5.3, 9.4; Pgs 178-180, 260-265, 433-435*

*   **Conduction ($\vec{J}_c$)**: Motion of free electrons in conductor via applied $\vec{E}$. Obeys Ohm's law: $\vec{J}_c = \sigma \vec{E}$.
*   **Convection ($\vec{J}_v$)**: Charge flow in insulator (vacuum/gas). No Ohm's law. $\vec{J}_v = \rho_v \vec{u}$.
*   **Displacement ($\vec{J}_d$)**: Fictitious current. Arises from time-varying $\vec{E}$ (e.g., across capacitor gap). $\vec{J}_d = \frac{\partial \vec{D}}{\partial t}$.

**Why modify Ampère's Law?**
*   Static Ampère: $\nabla \times \vec{H} = \vec{J}$
*   Identity: $\nabla \cdot (\nabla \times \vec{A}) \equiv 0 \implies \nabla \cdot \vec{J} = 0$.
*   *Conflict*: Continuity eq says $\nabla \cdot \vec{J} = -\partial\rho_v/\partial t \neq 0$ for dynamic fields.
*   *Fix*: Add $\vec{J}_d$. $\nabla \cdot (\vec{J} + \partial\vec{D}/\partial t) = -\partial\rho_v/\partial t + \partial(\nabla \cdot \vec{D})/\partial t = 0$. Resolves conflict! Allows EM wave propagation in vacuum.

**Copper at 1 MHz (Comparison):**
*   Ratio: $|\vec{J}_c| / |\vec{J}_d| = \sigma / (\omega\varepsilon)$ = Loss Tangent.
*   For Cu: Ratio $\approx 10^{12}$. Conduction current dominates massively. Displacement current is negligible.


***

### 4. KEY DERIVATIONS USING THEOREMS
*Ref: Sec 7.3, 9.2, 9.6; Pgs 309, 422, 439*

**Faraday's Law ($\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$)**
1. $V_{emf} = -d\Phi/dt$
2. Sub definitions: $\oint_L \vec{E} \cdot d\vec{l} = -\frac{d}{dt} \int_S \vec{B} \cdot d\vec{S}$
3. Apply Stokes' Thm to LHS: $\int_S (\nabla \times \vec{E}) \cdot d\vec{S} = -\int_S \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}$
4. Equate integrands $\implies \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$

**Static Ampère's Law ($\nabla \times \vec{H} = \vec{J}$)**
1. Integral form: $\oint_L \vec{H} \cdot d\vec{l} = I_{enc} = \int_S \vec{J} \cdot d\vec{S}$
2. Apply Stokes' Thm to LHS: $\int_S (\nabla \times \vec{H}) \cdot d\vec{S} = \int_S \vec{J} \cdot d\vec{S}$
3. Equate integrands $\implies \nabla \times \vec{H} = \vec{J}$

**Potentials Relation ($\vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}$)**
1. Gauss (Magnetic): $\nabla \cdot \vec{B} = 0 \implies \vec{B} = \nabla \times \vec{A}$ (Vector potential)
2. Sub into Faraday: $\nabla \times \vec{E} = -\frac{\partial}{\partial t}(\nabla \times \vec{A}) \implies \nabla \times (\vec{E} + \frac{\partial \vec{A}}{\partial t}) = 0$
3. Identity: $\nabla \times (-\nabla V) \equiv 0$
4. Equate inner terms $\implies \vec{E} + \frac{\partial \vec{A}}{\partial t} = -\nabla V \implies \vec{E} = -\nabla V - \frac{\partial \vec{A}}{\partial t}$


***

### 5. MAGNETIC MONOPOLE NON-EXISTENCE
*Ref: Sec 7.5, pgs 317-319*

*   **Concept**: Magnetic charges (monopoles) do not exist isolated. Always N-S pairs.
*   **Physical Meaning**: Magnetic flux lines have no start/end. They form continuous closed loops.
*   **Math Proof**: Gauss's Law for $\vec{B}$. Total flux leaving closed surface is zero. $\oint_S \vec{B} \cdot d\vec{S} = 0 \implies \nabla \cdot \vec{B} = 0$.


***

### 6. POYNTING THEOREM
*Ref: Pgs 340-344*

*   **Statement**: Net power leaving volume $v$ = (-) Rate of decrease of stored EM energy - Ohmic heat loss.
*   **Derivation**:
    1. Start with Ampère: $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$
    2. Dot with $\vec{E}$: $\vec{E} \cdot (\nabla \times \vec{H}) = \vec{E} \cdot \vec{J} + \vec{E} \cdot \frac{\partial \vec{D}}{\partial t}$
    3. Use Identity: $\nabla \cdot (\vec{E} \times \vec{H}) = \vec{H} \cdot (\nabla \times \vec{E}) - \vec{E} \cdot (\nabla \times \vec{H})$
    4. Sub Faraday ($\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$) into identity, rearrange.
    5. Result: $-\nabla \cdot (\vec{E} \times \vec{H}) = \vec{J} \cdot \vec{E} + \vec{E} \cdot \frac{\partial \vec{D}}{\partial t} + \vec{H} \cdot \frac{\partial \vec{B}}{\partial t}$
    6. Simplify time derivs: $\frac{\partial}{\partial t} ( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 )$
    7. Integrate over volume $v$, apply Divergence Thm to LHS.
*   **Final Integral Form**:
    $-\oint_S (\vec{E} \times \vec{H}) \cdot d\vec{S} = \int_v \mathbf{J} \cdot \mathbf{E} \, dv + \frac{\partial}{\partial t} \int_v \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv$
*   **Poynting Vector**: $\mathscr{P} = \vec{E} \times \vec{H}$ (Power density out).


***

### 7. HELMHOLTZ WAVE EQUATION & PLANE WAVES
*Ref: Pgs 284-288, 304-306, 445, 641-642*

**Helmholtz Equation Derivation (Source-free, Lossy medium):**
*   Phasor Maxwell: $\nabla \times \vec{E}_s = -j\omega\mu \vec{H}_s$  and  $\nabla \times \vec{H}_s = (\sigma + j\omega\varepsilon)\vec{E}_s$
*   Curl of Faraday: $\nabla \times (\nabla \times \vec{E}_s) = -j\omega\mu (\nabla \times \vec{H}_s)$
*   Identity: $\nabla(\nabla \cdot \vec{E}_s) - \nabla^2 \vec{E}_s$. Since $\rho_v=0$, $\nabla \cdot \vec{E}_s = 0$.
*   Combine: $-\nabla^2 \vec{E}_s = -j\omega\mu (\sigma + j\omega\varepsilon)\vec{E}_s$
*   Result: $\nabla^2 \vec{E}_s - \gamma^2 \vec{E}_s = 0$
*   *Propagation const*: $\gamma = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)} = \alpha + j\beta$

**Phasor Expressions (+z dir, x-polarized):**
*   Solve 1D differential eq: $d^2E_{xs}/dz^2 - \gamma^2 E_{xs} = 0 \implies \vec{E}_s(z) = E_0 e^{-\gamma z} \vec{a}_x$
*   Find $\vec{H}_s$ via Faraday ($\nabla \times \vec{E}_s = -j\omega\mu \vec{H}_s$): $\vec{H}_s(z) = \frac{E_0}{\eta} e^{-\gamma z} \vec{a}_y$
*   Intrinsic impedance: $\eta = \frac{j\omega\mu}{\gamma}$

**Phase Velocity ($v$ or $u_p$):**
*   Instantaneous form: $\vec{E}_x(z, t) = E_{x0} \cos(\omega t - \beta z)$
*   Set phase = const: $\omega t - \beta z = const$
*   Differentiate w.r.t $t$: $\omega - \beta(dz/dt) = 0 \implies v = \frac{\omega}{\beta}$
*   For lossless ($\sigma=0$): $\beta = \omega\sqrt{\mu\varepsilon} \implies v = \frac{1}{\sqrt{\mu\varepsilon}}$


***

### 8. POLARIZATION & SKIN DEPTH
*Ref: Pgs 331-334, 391-392, 402*

*   **Polarization**: Orientation of $\vec{E}$ field vector during propagation.
    *   *Parallel*: $\vec{E}$ lies strictly within the plane of incidence.
    *   *Perpendicular*: $\vec{E}$ is normal to the plane of incidence.
*   **Skin Depth ($\delta$)**: Depth at which wave amplitude decays by $e^{-1}$ ($\sim37\%$) inside a lossy medium.
    *   Formula: $\delta = \frac{1}{\alpha}$
    *   Good conductor: $\delta \approx \frac{1}{\sqrt{\pi f \mu \sigma}}$. (High frequency/conductivity $\implies$ wave confined to surface skin).


***

### 9. SPECIFIC PROBLEM LOGICS

**Problem: Find $\vec{B}, \vec{D}, \vec{E}, \beta$ from $\vec{H}$ in lossless medium ($\sigma=0$)**
*   Given: $\vec{H} = H_0 \cos(\omega t - \beta x)\vec{a}_y$
*   $\vec{B} = \mu \vec{H}$
*   $\beta = \omega\sqrt{\mu\varepsilon}$
*   Use Ampere: $\nabla \times \vec{H} = \varepsilon \frac{\partial \vec{E}}{\partial t} \implies$ find curl of $\vec{H}$, integrate w.r.t $t$, divide by $\varepsilon$ to get $\vec{E}$.
*   $\vec{D} = \varepsilon \vec{E}$

**Problem: Does $\vec{E} = E_0 \cos(\omega t - \beta x)\vec{a}_x$ satisfy vacuum Maxwell eq?**
*Ref: Ex 6, pg 559*
*   **No**. $\nabla \cdot \vec{E} = \beta E_0 \sin(\dots) \neq 0$. Violates Gauss's law for vacuum ($\rho_v=0$).
*   It's a longitudinal wave; EM waves must be transverse (TEM).
*   *Exception*: Only works if $\beta=0$ (Static DC field) or in non-vacuum plasma where $\rho_v \neq 0$.

**Problem: Motional EMF (Sliding Bar)**
*Ref: Sec 9.3, pgs 425-428*
*   Formula: $V_{emf} = \int_L (\vec{u} \times \vec{B}) \cdot d\vec{l}$
*   Velocity: $\vec{u} = \frac{dx}{dt} \vec{a}_x$
*   Calculate $\vec{u} \times \vec{B}$, dot it with $d\vec{l}$ (oriented along the bar), and integrate over rail separation length. Substitute specific $x$ or $t$ values.
Here are the specific mathematical derivations, exact equations, and numerical solutions that were glossed over in the initial summary. 

***

### 10. EXACT DERIVATION: $\vec{H}$ TO $\vec{E}$ IN LOSSLESS MEDIUM
*Ref: Chapter 9, Example 9.8*

*   **Given**: $\sigma = 0$, $\vec{H} = 2 \cos(10^{10}t - \beta x)\vec{a}_y$
*   **Find Curl of $\vec{H}$**:
    $$\nabla \times \vec{H} = \left| \begin{matrix} \vec{a}_x & \vec{a}_y & \vec{a}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 0 & H_y & 0 \end{matrix} \right| = \vec{a}_z \left( \frac{\partial H_y}{\partial x} \right)$$
    $$\nabla \times \vec{H} = 2\beta \sin(10^{10}t - \beta x) \vec{a}_z$$
*   **Apply Ampère's Law** ($\nabla \times \vec{H} = \varepsilon \frac{\partial \vec{E}}{\partial t}$ since $\vec{J}=0$):
    $$\frac{\partial \vec{E}}{\partial t} = \frac{2\beta}{\varepsilon} \sin(10^{10}t - \beta x) \vec{a}_z$$
*   **Integrate w.r.t Time ($t$)**:
    $$\vec{E} = \int \frac{2\beta}{\varepsilon} \sin(10^{10}t - \beta x) \vec{a}_z \, dt$$
    $$\vec{E} = -\frac{2\beta}{\omega\varepsilon} \cos(10^{10}t - \beta x) \vec{a}_z$$
*   **Substitute Values** ($\omega = 10^{10}$, $\beta = 600$, $\varepsilon = 1.2 \times 10^{-10}$):
    $$\vec{E} = -1000 \cos(10^{10}t - 600x) \vec{a}_z \text{ V/m}$$


***

### 11. EXACT CALCULATION: $J_c$ vs $J_d$ IN COPPER
*Ref: Sec 9.4, pg 433*

*   **Given**: $f = 1$ MHz, $\sigma = 5.8 \times 10^7$ S/m, $\varepsilon \approx 10^{-9}/(36\pi)$ F/m.
*   **Ratio Formula** (Loss Tangent): 
    $$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{\sigma}{\omega\varepsilon}$$
*   **Computation**:
    $$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{5.8 \times 10^7}{ (2\pi \times 10^6) \times (10^{-9}/36\pi) }$$
    $$\frac{|\mathbf{J}_{cs}|}{|\mathbf{J}_{ds}|} = \frac{5.8 \times 10^7 \times 36}{2 \times 10^{-3}}$$
*   **Exact Result**: $1.044 \times 10^{12}$. 
*   **Conclusion**: $J_c \gg J_d$. Displacement current is negligible in good conductors at RF frequencies.


***

### 12. EXACT SOLUTION: SLIDING BAR MOTIONAL EMF
*Ref: Sec 9.3, pg 425*
![[Screenshot_20260615_033410_Xodo.jpg]]

*   **Given**: $\vec{B} = 0.5x \vec{a}_z$, $x(t) = 4t - 2t^2$, $l = 0.1$ m. 
*   **Velocity ($\vec{u}$)**: 
    $$\vec{u} = \frac{dx}{dt} \vec{a}_x = (4 - 4t)\vec{a}_x$$
*   **Cross Product**: 
    $$\vec{u} \times \vec{B} = ((4 - 4t)\vec{a}_x) \times (0.5x \vec{a}_z) = -0.5x(4 - 4t) \vec{a}_y$$
*   **Integral Setup**: $d\vec{l}$ is along y-axis ($dy \vec{a}_y$).
    $$V_{ab} = \int_0^{0.1} -0.5x(4 - 4t) dy = -0.05x(4 - 4t)$$

**Condition (i): At $t = 0.5$ s**
*   Find $x$: $x(0.5) = 4(0.5) - 2(0.5)^2 = 1.5$ m.
*   Find $V_{ab}$: $V_{ab} = -0.05(1.5)(4 - 2) = -0.15$ V.

**Condition (ii): At $x = 1$ m**
*   Find $v(x)$: $v^2 = (4-4t)^2 = 16 - 32t + 16t^2 = 16 - 8x$.
*   At $x=1$: $v = \pm \sqrt{16-8} = \pm 2\sqrt{2}$ m/s.
*   Cross product at $x=1$: $\vec{u} \times \vec{B} = -0.5 (\pm 2\sqrt{2})(1) \vec{a}_y = \mp \sqrt{2} \vec{a}_y$.
*   Find $V_{ab}$: $\int_0^{0.1} \mp \sqrt{2} dy = \mp 0.1\sqrt{2} \approx \mp 0.1414$ V.


***

### 13. INTRINSIC WAVE IMPEDANCE ($\eta$)
*Ref: Pg 282, Eq 13*

*   **Definition**: Ratio of $\vec{E}$ and $\vec{H}$ field intensities.
*   **General Formula (Lossy)**: 
    $$\eta = \frac{j\omega\mu}{\gamma} = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$
*   **Lossless Formula ($\sigma=0$)**: 
    $$\eta = \sqrt{\frac{\mu}{\varepsilon}}$$