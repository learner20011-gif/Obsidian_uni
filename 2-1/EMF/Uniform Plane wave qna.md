### (b) Derive the expression of the attenuation constant, $\alpha$ and phase constant, $\beta$ of a propagating wave through a lossy-dielectric medium in terms of the constituent properties of the medium. Prove that the attenuation and phase constant for conducting media as follows:
$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{\frac{1}{2}}$
$\beta = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1 \right]^{\frac{1}{2}}$

**Answer:**

To derive the expressions for the attenuation constant ($\alpha$) and phase constant ($\beta$) in a lossy dielectric medium, we begin with Maxwell's curl equations for a linear, isotropic, homogeneous, and charge-free ($\rho_v = 0$) medium. Suppressing the time-harmonic factor $e^{j\omega t}$, the phasor forms of Maxwell's equations are:
$\nabla \times \vec{E}_s = -j\omega\mu \vec{H}_s$
$\nabla \times \vec{H}_s = (\sigma + j\omega\varepsilon)\vec{E}_s$

Taking the curl of the first equation and substituting the second into it yields the vector wave equation:
$\nabla \times \nabla \times \vec{E}_s = -j\omega\mu(\nabla \times \vec{H}_s)$
$\nabla(\nabla \cdot \vec{E}_s) - \nabla^2\vec{E}_s = -j\omega\mu(\sigma + j\omega\varepsilon)\vec{E}_s$

Since the medium is charge-free, $\nabla \cdot \vec{E}_s = 0$. The equation simplifies to the Helmholtz wave equation:
$\nabla^2\vec{E}_s - \gamma^2\vec{E}_s = 0$

where $\gamma$ is the complex propagation constant of the medium, defined as:
$\gamma^2 = j\omega\mu(\sigma + j\omega\varepsilon) = -\omega^2\mu\varepsilon + j\omega\mu\sigma$

We also know that the complex propagation constant can be expressed in terms of its real part (attenuation constant, $\alpha$) and imaginary part (phase constant, $\beta$):
$\gamma = \alpha + j\beta$

Squaring this expression gives:
$\gamma^2 = (\alpha + j\beta)^2 = (\alpha^2 - \beta^2) + j(2\alpha\beta)$

By equating the real and imaginary parts of the two expressions for $\gamma^2$, we obtain two equations:
1) Real part: $\alpha^2 - \beta^2 = -\omega^2\mu\varepsilon \implies \beta^2 - \alpha^2 = \omega^2\mu\varepsilon$
2) Imaginary part: $2\alpha\beta = \omega\mu\sigma$

Next, we find the magnitude of $\gamma^2$ from both representations. 
From $\gamma = \alpha + j\beta$, the magnitude is:
$|\gamma^2| = \alpha^2 + \beta^2$

From $\gamma^2 = -\omega^2\mu\varepsilon + j\omega\mu\sigma$, the magnitude is:
$|\gamma^2| = \sqrt{(-\omega^2\mu\varepsilon)^2 + (\omega\mu\sigma)^2} = \omega\mu\sqrt{\omega^2\varepsilon^2 + \sigma^2}$
Factoring out $\omega\varepsilon$ from inside the square root gives:
$|\gamma^2| = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2}$

Now we have a system of two algebraic equations:
$\beta^2 - \alpha^2 = \omega^2\mu\varepsilon$
$\beta^2 + \alpha^2 = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2}$

To solve for $\beta$, we add the two equations together:
$2\beta^2 = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + \omega^2\mu\varepsilon$
$2\beta^2 = \omega^2\mu\varepsilon \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1 \right]$
Dividing by 2 and taking the square root yields the expression for the phase constant:
$\beta = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1 \right]^{\frac{1}{2}}$

To solve for $\alpha$, we subtract the first equation from the second:
$2\alpha^2 = \omega^2\mu\varepsilon\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - \omega^2\mu\varepsilon$
$2\alpha^2 = \omega^2\mu\varepsilon \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]$
Dividing by 2 and taking the square root yields the expression for the attenuation constant:
$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{\frac{1}{2}}$

This completes the proof.
*Related location: Slide 305 to Slide 308*


***


### (c) The $\vec{E}$ field of a uniform plane wave propagating in a dielectric medium is given by $\vec{E}(t,z) = \bar{a}_x 2\cos\left(10^8 t - \frac{z}{\sqrt{3}}\right) - \bar{a}_y \sin\left(10^8 t - \frac{z}{\sqrt{3}}\right)$ V/m.
### (i) Determine the frequency and wavelength of the wave.
### (ii) Describe the polarization of the wave.
### (iii) Find the corresponding $\vec{H}$ field.

**Answer:**

**Part (i): Determine the frequency and wavelength of the wave.**
By comparing the given electric field equation to the standard time-domain form of a wave $\cos(\omega t - \beta z)$, we can extract the following parameters:
*   Angular frequency, $\omega = 10^8$ rad/s
*   Phase constant, $\beta = \frac{1}{\sqrt{3}}$ rad/m

The frequency $f$ is calculated as:
$f = \frac{\omega}{2\pi} = \frac{10^8}{2\pi} \approx 15.915 \times 10^6 \text{ Hz} = 15.915 \text{ MHz}$

The wavelength $\lambda$ is calculated as:
$\lambda = \frac{2\pi}{\beta} = \frac{2\pi}{1/\sqrt{3}} = 2\pi\sqrt{3} \approx 10.88 \text{ m}$

**Part (ii): Describe the polarization of the wave.**
Let's analyze the components of the $\vec{E}$ field at a fixed plane, say $z = 0$:
$E_x(t) = 2\cos(10^8 t)$
$E_y(t) = -\sin(10^8 t)$

We can observe two things:
1.  The amplitudes of the $x$ and $y$ components are unequal ($2 \neq 1$).
2.  There is a $90^\circ$ phase difference between the components (cosine vs. negative sine).
Because the amplitudes are different and they are out of phase by $90^\circ$, the wave is **elliptically polarized**.

To determine the handedness (direction of rotation), we observe the vector at successive time intervals at $z=0$:
*   At $t = 0$: $\vec{E} = 2\hat{a}_x$ (points in $+x$ direction)
*   At $\omega t = \pi/2$: $\vec{E} = -1\hat{a}_y$ (points in $-y$ direction)

The tip of the electric field vector rotates from the $+x$-axis toward the $-y$-axis, which is a clockwise rotation when looking down the $z$-axis. 
Since the wave is propagating in the $+z$ direction (indicated by the $-\beta z$ term), we point our right thumb in the $+z$ direction. The fingers of the right hand curl counter-clockwise. Since the actual rotation is clockwise, it matches the left hand. Therefore, the wave exhibits **Left-Hand Elliptical Polarization (LHEP)**.

**Part (iii): Find the corresponding $\vec{H}$ field.**
To find the magnetic field, we first need to determine the intrinsic impedance ($\eta$) of the dielectric medium.
The wave velocity $u$ is given by:
$u = \frac{\omega}{\beta} = \frac{10^8}{1/\sqrt{3}} = \sqrt{3} \times 10^8 \text{ m/s}$

We also know that velocity in a dielectric is $u = \frac{c}{\sqrt{\varepsilon_r\mu_r}}$. Assuming it is a non-magnetic dielectric medium ($\mu_r = 1$):
$\sqrt{3} \times 10^8 = \frac{3 \times 10^8}{\sqrt{\varepsilon_r}}$
$\sqrt{\varepsilon_r} = \frac{3}{\sqrt{3}} = \sqrt{3} \implies \varepsilon_r = 3$

Now, calculate the intrinsic impedance $\eta$:
$\eta = \sqrt{\frac{\mu}{\varepsilon}} = \frac{\eta_0}{\sqrt{\varepsilon_r}} = \frac{120\pi}{\sqrt{3}} = 40\pi\sqrt{3} \approx 217.65 \ \Omega$

The magnetic field $\vec{H}$ is related to the electric field $\vec{E}$ and the direction of propagation $\hat{a}_k$ (which is $\hat{a}_z$ in this case) by the cross product:
$\vec{H} = \frac{1}{\eta} \hat{a}_k \times \vec{E}$
$\vec{H}(t,z) = \frac{1}{40\pi\sqrt{3}} \hat{a}_z \times \left[ 2\cos\left(10^8 t - \frac{z}{\sqrt{3}}\right)\hat{a}_x - \sin\left(10^8 t - \frac{z}{\sqrt{3}}\right)\hat{a}_y \right]$

Using the cross-product rules ($\hat{a}_z \times \hat{a}_x = \hat{a}_y$ and $\hat{a}_z \times \hat{a}_y = -\hat{a}_x$):
$\vec{H}(t,z) = \frac{1}{40\pi\sqrt{3}} \left[ 2\cos\left(10^8 t - \frac{z}{\sqrt{3}}\right)\hat{a}_y - \left(-\sin\left(10^8 t - \frac{z}{\sqrt{3}}\right)\right)(-\hat{a}_x) \right]$

Simplifying the signs gives the final corresponding $\vec{H}$ field:
$\vec{H}(t,z) = \frac{1}{40\pi\sqrt{3}} \left[ \sin\left(10^8 t - \frac{z}{\sqrt{3}}\right)\bar{a}_x + 2\cos\left(10^8 t - \frac{z}{\sqrt{3}}\right)\bar{a}_y \right] \text{ A/m}$
*(Or approximately: $4.59 \sin(10^8 t - \frac{z}{\sqrt{3}})\bar{a}_x + 9.18 \cos(10^8 t - \frac{z}{\sqrt{3}})\bar{a}_y \text{ mA/m}$)*

*Related location: Slide 279, Slide 280, Slide 282, and Slide 297*
### Q.5 (a) Write the time harmonic equation of plane wave as a solution of Helmholtz's phasor-vector wave equation. Using the expression, obtain the equation of phase velocity of the wave interms of constituent properties of the medium.

**Answer:**

**1. Time Harmonic Equation of a Plane Wave:**
We start with the Helmholtz wave equation for a source-free, lossless medium ($\sigma = 0$), which is derived from Maxwell's equations in phasor form:
$\nabla^2 \vec{E}_s + k^2 \vec{E}_s = 0$
where $k = \omega\sqrt{\mu\varepsilon}$ is the wave number (also denoted as phase constant $\beta$).

For a uniform plane wave, we assume propagation along a specific axis, say the $+z$-direction, and uniform field properties in the transverse plane (no variation in $x$ or $y$). If we also assume the electric field is polarized along the $x$-axis, the vector Helmholtz equation simplifies to a scalar ordinary differential equation:
$\frac{d^2 E_{xs}}{dz^2} + \beta^2 E_{xs} = 0$

The solution to this differential equation for a wave traveling in the $+z$-direction is:
$E_{xs}(z) = E_{x0} e^{-j\beta z}$
where $E_{x0}$ is the constant amplitude of the wave.

To find the time-harmonic (instantaneous) equation of the plane wave, we multiply the phasor solution by the time factor $e^{j\omega t}$ and take the real part:
$\vec{E}(z,t) = \text{Re}\left[ \vec{E}_s(z) e^{j\omega t} \right]$
$\vec{E}(z,t) = \text{Re}\left[ E_{x0} e^{-j\beta z} e^{j\omega t} \hat{a}_x \right] = \text{Re}\left[ E_{x0} e^{j(\omega t - \beta z)} \hat{a}_x \right]$

Using Euler's identity, the real part gives the time-harmonic equation:
$\vec{E}(z,t) = E_{x0} \cos(\omega t - \beta z) \hat{a}_x$

**2. Equation of Phase Velocity:**
The phase velocity ($v_p$ or $u$) is the velocity at which a point of constant phase on the wave travels. We can find this by setting the phase angle of the cosine term to a constant:
Phase = $\omega t - \beta z = \text{constant}$

To find the velocity, we take the derivative of this constant phase with respect to time $t$:
$\frac{d}{dt}(\omega t - \beta z) = \frac{d}{dt}(\text{constant})$
$\omega - \beta \frac{dz}{dt} = 0$

Solving for $\frac{dz}{dt}$, which represents the phase velocity $v_p$:
$v_p = \frac{dz}{dt} = \frac{\omega}{\beta}$

Now, we substitute the definition of the phase constant $\beta = \omega\sqrt{\mu\varepsilon}$ (for a lossless medium) into the equation:
$v_p = \frac{\omega}{\omega\sqrt{\mu\varepsilon}} = \frac{1}{\sqrt{\mu\varepsilon}}$

Thus, the phase velocity is expressed in terms of the constituent properties of the medium: magnetic permeability ($\mu$) and electric permittivity ($\varepsilon$).

*Related location pg no. In provided slides: Slide 275, 278, 281, and 289.*

***

### Q.5 (b) Characterize the behaviour of a plane wave, in case, it is propagating through lossy - and lossless dielectric medium, also lossy - and lossless conducting medium.

**Answer:**

The behavior of a uniform plane wave is governed by the properties of the medium it travels through, specifically its conductivity ($\sigma$), permittivity ($\varepsilon$), and permeability ($\mu$). These dictate the propagation constant $\gamma = \alpha + j\beta$ and intrinsic impedance $\eta$.

**1. Lossless Dielectric Medium ($\sigma \approx 0$ or $\sigma \ll \omega\varepsilon$):**
*   **Attenuation:** Because the conductivity is practically zero, there are no ohmic losses. The attenuation constant is zero ($\alpha = 0$). The wave propagates without losing amplitude.
*   **Propagation:** The propagation constant is purely imaginary ($\gamma = j\beta$). The phase constant is $\beta = \omega\sqrt{\mu\varepsilon}$.
*   **Impedance:** The intrinsic impedance $\eta = \sqrt{\frac{\mu}{\varepsilon}}$ is purely real and constant.
*   **Phase:** The electric field ($\vec{E}$) and magnetic field ($\vec{H}$) are perfectly in phase with each other in time.

**2. Lossy Dielectric Medium ($\sigma \neq 0$):**
*   **Attenuation:** The medium is partially conducting. The wave loses power as it travels due to ohmic heating. The attenuation constant $\alpha > 0$. The amplitude decays exponentially as $e^{-\alpha z}$.
*   **Propagation:** The propagation constant $\gamma = \alpha + j\beta$ is complex. Both $\alpha$ and $\beta$ depend on $\sigma, \varepsilon, \mu,$ and the frequency $\omega$.
*   **Impedance:** The intrinsic impedance $\eta = |\eta|\angle\theta_\eta$ is a complex quantity.
*   **Phase:** Because the impedance is complex, the electric and magnetic fields are out of phase. The magnetic field $\vec{H}$ lags the electric field $\vec{E}$ by the angle $\theta_\eta$ (where $0 < \theta_\eta < 45^\circ$).

**3. Lossy Conducting Medium / Good Conductor ($\sigma \gg \omega\varepsilon$):**
*   **Attenuation:** The high conductivity causes rapid energy dissipation. The wave attenuates very rapidly. The attenuation constant is very large, approximately equal to the phase constant: $\alpha \approx \beta \approx \sqrt{\pi f \mu \sigma}$.
*   **Skin Effect:** Due to rapid attenuation, the wave can only penetrate a short distance into the medium. This is characterized by the skin depth $\delta = \frac{1}{\alpha}$, which is very small.
*   **Impedance:** The intrinsic impedance is very small and highly complex, specifically with a phase angle of $45^\circ$ ($\eta = |\eta| \angle 45^\circ$).
*   **Phase:** The magnetic field $\vec{H}$ strongly lags the electric field $\vec{E}$ by exactly $45^\circ$.

**4. Lossless Conducting Medium / Perfect Conductor ($\sigma \to \infty$):**
*   **Attenuation:** A perfect conductor cannot sustain an internal electromagnetic field. The attenuation constant approaches infinity ($\alpha \to \infty$), meaning the skin depth is zero ($\delta = 0$).
*   **Propagation:** Electromagnetic waves absolutely cannot propagate through a perfect conductor.
*   **Impedance:** The intrinsic impedance is zero ($\eta = 0$).
*   **Behavior:** If a plane wave strikes a perfect conductor, it is 100% reflected. The electric field inside the conductor is zero ($\vec{E} = 0$).

*Related location pg no. In provided slides: Slide 284, 304-320 (Lossy Dielectrics), 323-324 (Lossless Dielectrics), 329-334 (Good Conductors), and Slide 206, 367 (Perfect Conductors).*

***

### Q.5 (c) In a nonmagnetic medium the electric field intensity, $\vec{E} = 4\sin(2\pi \times 10^7 t - 0.8x)\bar{a}_z$ V/m. Calculate the intrinsic impedance of the medium. Also calculate the time-average power carried by the wave.

**Answer:**

**1. Calculate the intrinsic impedance ($\eta$) of the medium:**
From the given expression for the electric field $\vec{E} = 4\sin(2\pi \times 10^7 t - 0.8x)\bar{a}_z$, we can extract the following standard wave parameters:
*   Amplitude, $E_0 = 4$ V/m
*   Angular frequency, $\omega = 2\pi \times 10^7$ rad/s
*   Phase constant, $\beta = 0.8$ rad/m
*   Direction of wave propagation is in the $+x$ direction.

The medium is given as "nonmagnetic," which implies its relative permeability is 1. Therefore, its permeability is the permeability of free space:
*   $\mu = \mu_0 = 4\pi \times 10^{-7}$ H/m

The intrinsic impedance of a medium is defined as $\eta = \sqrt{\frac{\mu}{\varepsilon}}$.
We also know the relationship between phase velocity $v_p$, frequency, and phase constant:
$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\varepsilon}}$
From this, we can express $\sqrt{\varepsilon}$ as:
$\sqrt{\varepsilon} = \frac{\beta}{\omega\sqrt{\mu}}$

Substituting this into the intrinsic impedance formula gives a more direct way to solve using our known variables:
$\eta = \frac{\sqrt{\mu}}{\sqrt{\varepsilon}} = \frac{\sqrt{\mu}}{\frac{\beta}{\omega\sqrt{\mu}}} = \frac{\omega \mu}{\beta}$

Now, substitute the known values into this equation:
$\eta = \frac{(2\pi \times 10^7) \times (4\pi \times 10^{-7})}{0.8}$
$\eta = \frac{8\pi^2 \times 10^0}{0.8}$
$\eta = \frac{8\pi^2}{0.8} = 10\pi^2 \ \Omega$

Numerically, $\eta \approx 10 \times (3.14159)^2 \approx 98.696 \ \Omega$.

**2. Calculate the time-average power carried by the wave ($\vec{\mathcal{P}}_{ave}$):**
![[Pasted image 20260614170747.jpg]]
The time-average power density (average Poynting vector) for a uniform plane wave is given by the formula:
$\vec{\mathcal{P}}_{ave} = \frac{E_0^2}{2\eta} \hat{a}_k$
where $\hat{a}_k$ is the unit vector in the direction of wave propagation.

From the $\vec{E}$ field expression (specifically the $-0.8x$ term), the wave propagates in the $+x$ direction, so $\hat{a}_k = \bar{a}_x$.
Substitute the values $E_0 = 4$ V/m and $\eta = 10\pi^2 \ \Omega$:
$\vec{\mathcal{P}}_{ave} = \frac{4^2}{2 \times 10\pi^2} \bar{a}_x$
$\vec{\mathcal{P}}_{ave} = \frac{16}{20\pi^2} \bar{a}_x$
$\vec{\mathcal{P}}_{ave} = \frac{0.8}{\pi^2} \bar{a}_x \text{ W/m}^2$

Numerically:
$\vec{\mathcal{P}}_{ave} \approx \frac{0.8}{9.8696} \bar{a}_x \approx 0.08105 \bar{a}_x \text{ W/m}^2$  or  $81.05 \bar{a}_x \text{ mW/m}^2$.

*Related location pg no. In provided slides: Slide 352 (Example 10.7), Slide 350 (Equation 27 for Power), Slide 291 (Intrinsic Impedance).*
### a) Define intrinsic impedance. Derive the mathematical relationship between phase velocity and group velocity.

**Definition of Intrinsic Impedance:**
The intrinsic impedance (denoted by $\eta$) of a medium is defined as the ratio of the magnitude of the electric field intensity ($E$) to the magnitude of the magnetic field intensity ($H$) for a uniform plane wave propagating through that medium. 
For a generalized lossy medium, it is a complex quantity given by:
$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$
where $\mu$ is the permeability, $\varepsilon$ is the permittivity, $\sigma$ is the conductivity, and $\omega$ is the angular frequency.
For a lossless medium (free space or perfect dielectric where $\sigma = 0$), it simplifies to a purely real value: $\eta = \sqrt{\frac{\mu}{\varepsilon}}$.

**Derivation of the relationship between phase velocity ($u_p$) and group velocity ($u_g$):**
This relationship is classically derived in the context of dispersive media or waveguides. Let's derive it using the standard waveguide dispersion relation.
The phase constant $\beta$ in a waveguide is given by:
$$\beta = \sqrt{\omega^2\mu\varepsilon - k_c^2}$$
where $k_c$ is the cutoff wavenumber (a constant for a given mode and waveguide geometry).

1.  **Phase Velocity ($u_p$):** This is the velocity at which a point of constant phase travels.
    $$u_p = \frac{\omega}{\beta}$$
2.  **Group Velocity ($u_g$):** This is the velocity at which the wave envelope (or energy) propagates.
    $$u_g = \frac{d\omega}{d\beta}$$
    
To find $\frac{d\omega}{d\beta}$, we differentiate the dispersion equation implicitly with respect to $\omega$:
$$\beta^2 = \omega^2\mu\varepsilon - k_c^2$$
$$2\beta \frac{d\beta}{d\omega} = 2\omega\mu\varepsilon - 0$$
$$\frac{d\beta}{d\omega} = \frac{\omega\mu\varepsilon}{\beta}$$

Since $u_g = \frac{d\omega}{d\beta}$, we invert this result:
$$u_g = \frac{\beta}{\omega\mu\varepsilon}$$

Now, multiply the expressions for phase velocity and group velocity:
$$u_p \cdot u_g = \left(\frac{\omega}{\beta}\right) \cdot \left(\frac{\beta}{\omega\mu\varepsilon}\right)$$
$$u_p \cdot u_g = \frac{1}{\mu\varepsilon}$$

Recognizing that the velocity of a uniform plane wave in the unbounded medium is $u' = \frac{1}{\sqrt{\mu\varepsilon}}$ (or $c$ in free space), we get the final mathematical relationship:
$$u_p \cdot u_g = u'^2$$
(or $v_p \cdot v_g = c^2$ in free space).

*Related location pg no. In provided slides: Slide 282, 313 (Intrinsic Impedance) and Slide 527-530 (Phase and Group Velocity).*

***
### Define Poynting vector

**Answer:**

**Definition:**
The **Poynting vector** represents the directional energy flux (or power flow per unit area) of an electromagnetic field. Named after the English physicist John H. Poynting, it is a fundamental quantity used to determine the rate and direction of electromagnetic energy transfer in a uniform plane wave or any electromagnetic system.

**Mathematical Expression:**
Mathematically, the instantaneous Poynting vector (denoted by $\mathscr{P}$) is defined as the cross product of the electric field intensity vector ($\mathbf{E}$) and the magnetic field intensity vector ($\mathbf{H}$):
$$\mathscr{P} = \mathbf{E} \times \mathbf{H}$$

**Key Characteristics:**
1.  **Direction:** Because it is defined by a cross product, the Poynting vector $\mathscr{P}$ is always perpendicular (normal) to both the electric field ($\mathbf{E}$) and the magnetic field ($\mathbf{H}$). For a uniform plane wave, the Poynting vector points exactly in the direction of wave propagation ($\mathbf{a}_k$).
2.  **Units:** The unit of the Poynting vector is **Watts per square meter (W/m²)**, as it represents power density (power per unit area).
3.  **Time-Varying Nature:** The instantaneous Poynting vector $\mathscr{P}(x, y, z, t)$ is a time-varying vector quantity. 
4.  **Relationship to Total Power (Poynting's Theorem):** If you integrate the Poynting vector over a closed surface $S$, it gives the total power flowing out of the volume enclosed by that surface:
    $$\text{Total Power Out} = \oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} = \oint_S \mathscr{P} \cdot d\mathbf{S}$$

**Time-Average Poynting Vector ($\mathscr{P}_{ave}$):**
In most practical engineering and physics applications (especially with time-harmonic fields), the instantaneous power fluctuates rapidly. Therefore, it is far more useful to calculate the **time-average Poynting vector**, which is a time-invariant vector. Using phasor representation ($\mathbf{E}_s$ and $\mathbf{H}_s$), the time-average Poynting vector is given by:
$$\mathscr{P}_{ave}(z) = \frac{1}{2} \text{Re}(\mathbf{E}_s \times \mathbf{H}_s^*)$$
where $\mathbf{H}_s^*$ is the complex conjugate of the magnetic field phasor. Integrating this average vector over a surface yields the scalar average power $P_{ave}$ in Watts.

*Related location pg no. In provided slides: Slide 340, Slide 345, Slide 347, Slide 349, and Slide 351.*
### b) State and prove Poynting theorem.

**Statement of Poynting's Theorem:**
Poynting's theorem states that the net power flowing out of a given volume $v$ is equal to the time rate of decrease of the electromagnetic energy stored within that volume minus the ohmic (conduction) power dissipated within the volume. 
Mathematically, it is expressed in integral form as:
$$-\oint_S (\vec{E} \times \vec{H}) \cdot d\vec{S} = \frac{\partial}{\partial t} \int_v \left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right) dv + \int_v \sigma E^2 dv$$

**Proof:**
We begin with Maxwell's curl equations for time-varying fields:
1)  $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} = -\mu \frac{\partial \vec{H}}{\partial t}$
2)  $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t} = \sigma\vec{E} + \varepsilon \frac{\partial \vec{E}}{\partial t}$

Take the dot product of both sides of the second equation with $\vec{E}$:
$$\vec{E} \cdot (\nabla \times \vec{H}) = \vec{E} \cdot \vec{J} + \vec{E} \cdot \frac{\partial \vec{D}}{\partial t}$$
Substitute $\vec{J} = \sigma\vec{E}$ and $\vec{D} = \varepsilon\vec{E}$:
$$\vec{E} \cdot (\nabla \times \vec{H}) = \sigma E^2 + \vec{E} \cdot \varepsilon \frac{\partial \vec{E}}{\partial t}$$

Now, apply the standard vector identity: $\nabla \cdot (\vec{E} \times \vec{H}) = \vec{H} \cdot (\nabla \times \vec{E}) - \vec{E} \cdot (\nabla \times \vec{H})$.
Rearranging this identity for $\vec{E} \cdot (\nabla \times \vec{H})$ gives:
$$\vec{E} \cdot (\nabla \times \vec{H}) = \vec{H} \cdot (\nabla \times \vec{E}) - \nabla \cdot (\vec{E} \times \vec{H})$$

Substitute this back into our earlier equation:
$$\vec{H} \cdot (\nabla \times \vec{E}) - \nabla \cdot (\vec{E} \times \vec{H}) = \sigma E^2 + \vec{E} \cdot \varepsilon \frac{\partial \vec{E}}{\partial t}$$

Next, substitute Maxwell's first equation ($\nabla \times \vec{E} = -\mu \frac{\partial \vec{H}}{\partial t}$) into the first term:
$$\vec{H} \cdot \left(-\mu \frac{\partial \vec{H}}{\partial t}\right) - \nabla \cdot (\vec{E} \times \vec{H}) = \sigma E^2 + \vec{E} \cdot \varepsilon \frac{\partial \vec{E}}{\partial t}$$

Rearrange to isolate the divergence term on one side:
$$-\nabla \cdot (\vec{E} \times \vec{H}) = \sigma E^2 + \varepsilon \left(\vec{E} \cdot \frac{\partial \vec{E}}{\partial t}\right) + \mu \left(\vec{H} \cdot \frac{\partial \vec{H}}{\partial t}\right)$$

Using the calculus rule that $\frac{1}{2} \frac{\partial}{\partial t}(\vec{A} \cdot \vec{A}) = \vec{A} \cdot \frac{\partial \vec{A}}{\partial t}$, we can rewrite the time derivatives:
$$-\nabla \cdot (\vec{E} \times \vec{H}) = \sigma E^2 + \frac{\partial}{\partial t} \left( \frac{1}{2}\varepsilon E^2 \right) + \frac{\partial}{\partial t} \left( \frac{1}{2}\mu H^2 \right)$$
$$-\nabla \cdot (\vec{E} \times \vec{H}) = \sigma E^2 + \frac{\partial}{\partial t} \left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right)$$

This is the point (differential) form of Poynting's theorem. To get the integral form, we integrate both sides over a volume $v$:
$$\int_v -\nabla \cdot (\vec{E} \times \vec{H}) dv = \int_v \sigma E^2 dv + \int_v \frac{\partial}{\partial t} \left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right) dv$$

Apply the Divergence Theorem to the left side ($\int_v \nabla \cdot \vec{A} dv = \oint_S \vec{A} \cdot d\vec{S}$):
$$-\oint_S (\vec{E} \times \vec{H}) \cdot d\vec{S} = \frac{\partial}{\partial t} \int_v \left( \frac{1}{2}\varepsilon E^2 + \frac{1}{2}\mu H^2 \right) dv + \int_v \sigma E^2 dv$$
This completes the proof. The term $\vec{E} \times \vec{H}$ is defined as the Poynting vector $\vec{\mathcal{P}}$.

*Related location pg no. In provided slides: Slide 340 to Slide 344.*

***

### c) The electric field intensity of a linearly polarized uniform plane wave propagating in the $+z$ direction in sea water is $\vec{E} = \hat{a}_x 100 \cos(10^7 \pi t) \text{ V/m}$ at $z=0$. If $\varepsilon_r = 72$, $\mu_r = 1$ and $\sigma = 4 \text{ S/m}$. 
### (i) Determine the attenuation constant, phase constant, intrinsic impedance, phase velocity, wavelength and skin depth.
### (ii) Find the distance at which the amplitude of $\vec{E}$ is 1% of its value at $z=0$.

**Answer:**

**Part (i): Determine Wave Parameters**
First, identify the given parameters from the problem statement:
*   Angular frequency: $\omega = 10^7 \pi$ rad/s
*   Frequency: $f = \frac{\omega}{2\pi} = \frac{10^7 \pi}{2\pi} = 5 \times 10^6$ Hz = 5 MHz
*   Permeability: $\mu = \mu_0\mu_r = (4\pi \times 10^{-7})(1) = 4\pi \times 10^{-7}$ H/m
*   Permittivity: $\varepsilon = \varepsilon_0\varepsilon_r = \left(\frac{10^{-9}}{36\pi}\right)(72) = \frac{2 \times 10^{-9}}{\pi}$ F/m
*   Conductivity: $\sigma = 4$ S/m

Next, determine the type of medium by calculating the loss tangent ($\frac{\sigma}{\omega\varepsilon}$):
$$\frac{\sigma}{\omega\varepsilon} = \frac{4}{(10^7 \pi) \times \left(\frac{2 \times 10^{-9}}{\pi}\right)} = \frac{4}{2 \times 10^{-2}} = \frac{4}{0.02} = 200$$
Since $\frac{\sigma}{\omega\varepsilon} = 200 \gg 1$, sea water acts as a **good conductor** at this frequency. We can use the good conductor approximations safely.

**1. Attenuation constant ($\alpha$) and Phase constant ($\beta$):**
For a good conductor, $\alpha \approx \beta \approx \sqrt{\pi f \mu \sigma}$.
$$\alpha = \beta = \sqrt{\pi \cdot (5 \times 10^6) \cdot (4\pi \times 10^{-7}) \cdot 4}$$
$$\alpha = \beta = \sqrt{80\pi^2 \times 10^{-1}} = \sqrt{8\pi^2} = \pi\sqrt{8} = 2\pi\sqrt{2}$$
$$\alpha \approx 8.886 \text{ Np/m}$$
$$\beta \approx 8.886 \text{ rad/m}$$

**2. Intrinsic impedance ($\eta$):**
For a good conductor, $\eta \approx \sqrt{\frac{\omega\mu}{\sigma}} \angle 45^\circ$.
$$|\eta| = \sqrt{\frac{10^7 \pi \cdot 4\pi \times 10^{-7}}{4}} = \sqrt{\frac{40\pi^2 \times 10^0}{4}} = \sqrt{10\pi^2} = \pi\sqrt{10} \approx 9.93 \ \Omega$$
*(Note: If calculated using the standard exact method $|\eta| = \frac{\sqrt{\mu/\varepsilon}}{(1+(\sigma/\omega\varepsilon)^2)^{1/4}}$, you get exactly $\pi \ \Omega \approx 3.14 \ \Omega$. Let's stick to the exact calculation for $|\eta|$ to be safe since $200$ is large but exact is always better).*
Exact magnitude $|\eta| = \frac{\sqrt{\mu/\varepsilon}}{\sqrt[4]{1 + (\sigma/\omega\varepsilon)^2}} \approx \frac{\sqrt{(4\pi\cdot 10^{-7}) / (2\cdot 10^{-9} / \pi)}}{\sqrt{200}} = \frac{\sqrt{2\pi^2 \cdot 10^2}}{10\sqrt{2}} = \frac{10\pi\sqrt{2}}{10\sqrt{2}} = \pi \ \Omega$.
Phase angle $\theta_\eta = \frac{1}{2}\tan^{-1}\left(\frac{\sigma}{\omega\varepsilon}\right) = \frac{1}{2}\tan^{-1}(200) \approx 44.85^\circ \approx 45^\circ$.
$$\eta = \pi \angle 45^\circ \ \Omega \approx 3.14 \angle 45^\circ \ \Omega$$

**3. Phase velocity ($u_p$):**
$$u_p = \frac{\omega}{\beta} = \frac{10^7 \pi}{2\pi\sqrt{2}} = \frac{10^7}{2\sqrt{2}} \approx 3.535 \times 10^6 \text{ m/s}$$

**4. Wavelength ($\lambda$):**
$$\lambda = \frac{2\pi}{\beta} = \frac{2\pi}{2\pi\sqrt{2}} = \frac{1}{\sqrt{2}} \approx 0.707 \text{ m}$$

**5. Skin depth ($\delta$):**
$$\delta = \frac{1}{\alpha} = \frac{1}{2\pi\sqrt{2}} \approx 0.1125 \text{ m}$$

---
**Part (ii): Find the distance at which the amplitude of $\vec{E}$ is 1% of its value at $z=0$.**

The amplitude of the electric field as it propagates in the $+z$ direction decays exponentially according to the factor $e^{-\alpha z}$.
At $z=0$, the amplitude is $E_0 = 100$ V/m.
We want to find $z$ where the amplitude is $1\%$ of $E_0$, which is $0.01 E_0$.
$$|E(z)| = E_0 e^{-\alpha z} = 0.01 E_0$$
$$e^{-\alpha z} = 0.01$$
Take the natural logarithm of both sides:
$$-\alpha z = \ln(0.01)$$
$$-\alpha z \approx -4.605$$
Now, solve for $z$:
$$z = \frac{4.605}{\alpha} = \frac{4.605}{2\pi\sqrt{2}} \approx \frac{4.605}{8.886}$$
$$z \approx 0.518 \text{ m}$$
Alternatively, in terms of skin depth: $z = 4.605 \delta \approx 4.605 \times 0.1125 \approx 0.518 \text{ m}$.

*Related location pg no. In provided slides: Slide 304 to Slide 334 (Wave Propagation in Lossy Dielectrics / Good Conductors).*
### 🔴 (a) Define the terms loss tangent and skin depth. Derive the expression of skin depth for good conductor.

**Answer:**

**Definition of Loss Tangent:**
In a lossy medium, the ratio of the magnitude of the conduction current density ($J = \sigma E$) to that of the displacement current density ($J_d = \omega \varepsilon E$) is a measure of how lossy the medium is. This ratio is called the loss tangent, denoted by $\tan\theta$. Mathematically, it is defined as:
$$\tan\theta = \frac{|J_s|}{|J_{ds}|} = \frac{|\sigma E_s|}{|j\omega\varepsilon E_s|} = \frac{\sigma}{\omega\varepsilon}$$
where $\theta$ is known as the loss angle of the medium. It indicates the phase difference between the total current and the electric field.

**Definition of Skin Depth:**
As an electromagnetic wave travels through a conducting medium, its amplitude is attenuated by an exponential factor $e^{-\alpha z}$. The skin depth (or penetration depth), denoted by $\delta$, is defined as the distance through which the wave amplitude decreases by a factor of $e^{-1}$ (which is about $37\%$) of its initial value. It is a measure of the depth to which an EM wave can effectively penetrate the medium.
Mathematically, it is defined as the reciprocal of the attenuation constant:
$$\delta = \frac{1}{\alpha}$$

**Derivation of Skin Depth for a Good Conductor:**
The general expression for the attenuation constant $\alpha$ in any medium is:
$$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2}$$

A medium is characterized as a "good conductor" when its conduction current dominates its displacement current, which means the loss tangent is very large: $\sigma \gg \omega\varepsilon$, or $\frac{\sigma}{\omega\varepsilon} \to \infty$.

Applying this approximation to the term inside the inner square root:
$$1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2 \approx \left(\frac{\sigma}{\omega\varepsilon}\right)^2$$

Substituting this back into the equation for $\alpha$:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{\left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2}$$
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} - 1 \right]^{1/2}$$

Since $\frac{\sigma}{\omega\varepsilon}$ is extremely large, we can ignore the $-1$:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2} \cdot \frac{\sigma}{\omega\varepsilon}}$$
$$\alpha \approx \omega \sqrt{\frac{\mu\sigma}{2\omega}} = \sqrt{\frac{\omega^2\mu\sigma}{2\omega}} = \sqrt{\frac{\omega\mu\sigma}{2}}$$

Since angular frequency $\omega = 2\pi f$, we substitute this in:
$$\alpha = \sqrt{\frac{2\pi f\mu\sigma}{2}} = \sqrt{\pi f \mu \sigma}$$

By definition, skin depth $\delta = \frac{1}{\alpha}$. Substituting our expression for $\alpha$ in a good conductor yields the final derived formula:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

*Related location pg no. In provided slides: Slide 318, 319 (Loss tangent definition), Slide 331, 332, 333 (Skin depth definition and derivation).*

***

### 🔴 (b) In a nonmagnetic medium the electric field is given as $\vec{E} = 4 \sin(2\pi \times 10^7 t - 0.8x) \bar{a}_z$ V/m. find relative permittivity and intrinsic impedance of the medium. Calculate also the time-average power carried by the wave.

**Answer:**

From the given electric field equation $\vec{E} = 4 \sin(2\pi \times 10^7 t - 0.8x) \bar{a}_z$, we can extract the standard wave parameters:
*   Amplitude, $E_0 = 4$ V/m
*   Angular frequency, $\omega = 2\pi \times 10^7$ rad/s
*   Phase constant, $\beta = 0.8$ rad/m
*   The medium is nonmagnetic, so relative permeability $\mu_r = 1$, and $\mu = \mu_0$.

**1. Find Relative Permittivity ($\varepsilon_r$):**
We know the relationship for the phase constant in a lossless medium is $\beta = \omega\sqrt{\mu\varepsilon}$.
Substitute $\mu = \mu_0$ and $\varepsilon = \varepsilon_0\varepsilon_r$:
$$\beta = \omega\sqrt{\mu_0\varepsilon_0\varepsilon_r}$$

Knowing that the speed of light in a vacuum is $c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3 \times 10^8$ m/s, we can rewrite this as:
$$\beta = \frac{\omega}{c}\sqrt{\varepsilon_r}$$

Rearranging to solve for $\sqrt{\varepsilon_r}$:
$$\sqrt{\varepsilon_r} = \frac{\beta c}{\omega}$$
$$\sqrt{\varepsilon_r} = \frac{0.8 \times (3 \times 10^8)}{2\pi \times 10^7}$$
$$\sqrt{\varepsilon_r} = \frac{2.4 \times 10^8}{2\pi \times 10^7} = \frac{24}{2\pi} = \frac{12}{\pi}$$

Squaring both sides gives the relative permittivity:
$$\varepsilon_r = \left(\frac{12}{\pi}\right)^2 = \frac{144}{\pi^2} \approx 14.59$$

**2. Find Intrinsic Impedance ($\eta$):**
The intrinsic impedance of a lossless dielectric medium is given by $\eta = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_0}{\varepsilon_0\varepsilon_r}}$.
This can be written in terms of the intrinsic impedance of free space ($\eta_0 \approx 120\pi \ \Omega$):
$$\eta = \frac{\eta_0}{\sqrt{\varepsilon_r}}$$

Substituting our previously found value for $\sqrt{\varepsilon_r}$:
$$\eta = \frac{120\pi}{12/\pi} = \frac{120\pi^2}{12} = 10\pi^2 \ \Omega$$
Numerically, $\eta \approx 98.7 \ \Omega$.

**3. Calculate Time-Average Power ($\vec{\mathcal{P}}_{ave}$):**
The time-average power density (Poynting vector) for a uniform plane wave is:
$$\vec{\mathcal{P}}_{ave} = \frac{E_0^2}{2\eta} \hat{a}_k$$
where $\hat{a}_k$ is the direction of wave propagation. Looking at the phase term $(\omega t - \beta x)$, the wave propagates in the positive $x$-direction, so $\hat{a}_k = \bar{a}_x$.

Substitute the known values into the equation:
$$\vec{\mathcal{P}}_{ave} = \frac{4^2}{2(10\pi^2)} \bar{a}_x$$
$$\vec{\mathcal{P}}_{ave} = \frac{16}{20\pi^2} \bar{a}_x$$
$$\vec{\mathcal{P}}_{ave} = \frac{0.8}{\pi^2} \bar{a}_x \text{ W/m}^2$$

Numerically, this evaluates to:
$$\vec{\mathcal{P}}_{ave} \approx \frac{0.8}{9.87} \bar{a}_x \approx 0.081 \bar{a}_x \text{ W/m}^2 = 81 \bar{a}_x \text{ mW/m}^2$$

*Related location pg no. In provided slides: Slide 352, 353, 354, 355 (Example 10.7 solves this exact problem).*

***

### 🔴 (a) Using the expression of plane wave, obtain the equation of phase velocity in free space imposing the characteristics of plane wave. Take z = 0 at Rangpur, in Rangpur the expression of electric field of a plane wave is given by $E_x = E_{x0} \cos(2\pi \times 10^8 t)$, calculate $E_x$ at Chittagong that is located 500km south of Rangpur.

**Answer:**

**1. Equation of Phase Velocity in Free Space:**
For a uniform plane wave traveling in the $+z$ direction, the electric field can be expressed generally as:
$$E_x(z, t) = E_{x0} \cos(\omega t - \beta z)$$
The phase of this wave is the argument of the cosine function: Phase $= \omega t - \beta z$. 
To find the phase velocity ($v$ or $u$), we track a point of constant phase. Setting the phase to a constant and differentiating with respect to time $t$:
$$\frac{d}{dt}(\omega t - \beta z) = 0$$
$$\omega - \beta \frac{dz}{dt} = 0$$
$$v = \frac{dz}{dt} = \frac{\omega}{\beta}$$
In free space, we impose the characteristic that conductivity $\sigma=0$, permeability $\mu = \mu_0$, and permittivity $\varepsilon = \varepsilon_0$. The phase constant $\beta$ in a lossless medium is defined as $\beta = \omega\sqrt{\mu\varepsilon}$. For free space, $\beta = \omega\sqrt{\mu_0\varepsilon_0}$.
Substituting this into the velocity equation yields:
$$v = \frac{\omega}{\omega\sqrt{\mu_0\varepsilon_0}} = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = c$$
where $c \approx 3 \times 10^8$ m/s is the velocity of light in a vacuum.

**2. Calculation for Chittagong:**
Let the propagation axis $z$ point South. 
At Rangpur ($z = 0$), the field is given as:
$$E_x(0,t) = E_{x0} \cos(2\pi \times 10^8 t)$$
From this, we identify the angular frequency $\omega = 2\pi \times 10^8$ rad/s.
The general traveling wave expression from our derivation is $E_x(z,t) = E_{x0} \cos(\omega t - \beta z)$.
Since $\beta = \frac{\omega}{c}$, we can rewrite the wave equation as:
$$E_x(z,t) = E_{x0} \cos\left(\omega t - \frac{\omega}{c}z\right) = E_{x0} \cos\left[\omega\left(t - \frac{z}{c}\right)\right]$$
Chittagong is located $z = 500 \text{ km} = 5 \times 10^5 \text{ m}$ south. We must find the time delay factor $\frac{z}{c}$ for this distance:
$$\frac{z}{c} = \frac{5 \times 10^5 \text{ m}}{3 \times 10^8 \text{ m/s}} = \frac{5}{3000} = \frac{1}{600} \text{ seconds}$$
$$\frac{z}{c} \approx 0.001667 \text{ seconds}$$
Now, substitute this distance delay back into the wave equation for Chittagong:
$$E_x(\text{Chittagong}, t) = E_{x0} \cos\left[2\pi \times 10^8 \left(t - \frac{1}{600}\right)\right]$$
$$E_x(\text{Chittagong}, t) = E_{x0} \cos\left[2\pi \times 10^8 (t - 0.001667)\right]$$

*Related location pg no. In provided slides: Slide 279 (demonstrates this exact concept using Chicago and Cleveland).*

***

### 🔴 (b) Define loss tangent. State how a medium could be characterized by using the value of loss tangent.

**Answer:**

**Definition of Loss Tangent:**
When analyzing electromagnetic wave propagation in a lossy medium, the total current density $\vec{J}_{total}$ consists of two parts: the conduction current density $\vec{J}_s = \sigma \vec{E}_s$ and the displacement current density $\vec{J}_{ds} = j\omega\varepsilon \vec{E}_s$. 
The ratio of the magnitude of the conduction current density to the magnitude of the displacement current density is defined as the loss tangent. Mathematically:
$$\tan\theta = \frac{|J_s|}{|J_{ds}|} = \frac{|\sigma E_s|}{|j\omega\varepsilon E_s|} = \frac{\sigma}{\omega\varepsilon}$$
where $\theta$ is known as the loss angle of the medium. The loss tangent quantifies the degree to which a medium dissipates electromagnetic energy (turns it into heat via conduction) relative to how much it stores energy (via polarization).

**Characterization of a Medium using Loss Tangent:**
Although there is no strict, absolute line of demarcation, the value of the loss tangent ($\tan\theta = \frac{\sigma}{\omega\varepsilon}$) is the primary metric used to classify whether a medium behaves mostly like a dielectric or mostly like a conductor at a specific frequency $\omega$.

1.  **Good (Lossless or Perfect) Dielectric:** A medium is characterized as a good dielectric if its displacement current vastly exceeds its conduction current. This occurs when the loss tangent is very small.
    $$\text{Condition: } \tan\theta = \frac{\sigma}{\omega\varepsilon} \ll 1$$
    In this case, the medium acts primarily as an insulator, allowing waves to propagate with minimal attenuation.

2.  **Good Conductor:** A medium is characterized as a good conductor if its conduction current vastly exceeds its displacement current. This occurs when the loss tangent is very large.
    $$\text{Condition: } \tan\theta = \frac{\sigma}{\omega\varepsilon} \gg 1$$
    In this case, the medium dissipates energy rapidly, leading to very high attenuation of the wave and causing the "skin effect," where the wave only penetrates a tiny distance into the material.

*Related location pg no. In provided slides: Slide 318, 319.*

***

### 🔴 (c) Define characteristic impedance of a medium. Show that $\vec{E}$ leads $\vec{H}$ by $45^\circ$ in good conductor.

**Answer:**

**Definition:**
*(Note: In the context of unbounded media, this is properly termed "intrinsic impedance", while "characteristic impedance" usually refers to transmission lines. They serve the same physical purpose: linking voltage/electric fields to current/magnetic fields).* 
The intrinsic (or characteristic) wave impedance of a medium, denoted by $\eta$, is defined as the ratio of the magnitude of the electric field intensity ($\vec{E}$) to the magnetic field intensity ($\vec{H}$) of a uniform plane wave traveling through that medium. 
For a general lossy medium, it is a complex quantity defined by:
$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$
where $\mu$ is permeability, $\varepsilon$ is permittivity, $\sigma$ is conductivity, and $\omega$ is angular frequency.

**Show that $\vec{E}$ leads $\vec{H}$ by $45^\circ$ in a good conductor:**
For a medium to be classified as a "good conductor," its conduction current must greatly exceed its displacement current, meaning $\sigma \gg \omega\varepsilon$.

Applying this condition to the denominator of the intrinsic impedance equation:
$$\sigma + j\omega\varepsilon \approx \sigma$$

Substituting this approximation back into the impedance equation yields:
$$\eta \approx \sqrt{\frac{j\omega\mu}{\sigma}}$$

To determine the phase angle of this impedance, we look at the complex operator $j$. In polar form, $j$ is equivalent to $1 \angle 90^\circ$ or $e^{j\pi/2}$.
Taking the square root of $j$ halves its angle:
$$\sqrt{j} = \sqrt{e^{j\pi/2}} = e^{j\pi/4} = 1 \angle 45^\circ$$

Therefore, the intrinsic impedance of a good conductor can be written in polar form as:
$$\eta = \sqrt{\frac{\omega\mu}{\sigma}} \angle 45^\circ$$

Let the electric field be the reference, defined as $E_x = E_0 e^{-\alpha z} \cos(\omega t - \beta z)$. The associated magnetic field $\vec{H}$ is obtained by dividing $\vec{E}$ by the complex intrinsic impedance $\eta$. Because dividing by a complex number with an angle of $+45^\circ$ subtracts $45^\circ$ from the phase of the result, the instantaneous magnetic field takes the form:
$$H_y = \frac{E_0}{|\eta|} e^{-\alpha z} \cos(\omega t - \beta z - 45^\circ)$$

Comparing the phase arguments, the electric field phase is $(\omega t - \beta z)$ while the magnetic field phase is $(\omega t - \beta z - 45^\circ)$. Because the magnetic field has a negative phase shift relative to the electric field, we conclude that the electric field $\vec{E}$ leads the magnetic field $\vec{H}$ by $45^\circ$ in time phase within a good conductor.

*Related location pg no. In provided slides: Slide 313 (Definition), Slide 329, 330 (Good Conductor approximation and $45^\circ$ phase shift).*

### 🔴 (a) Define the terms loss tangent and skin depth. Derive the expression of skin depth for good conductor.

**Answer:**

**Definition of Loss Tangent:**
In a lossy medium, electromagnetic waves experience attenuation because some of the wave's energy is converted into heat due to conduction currents. The total current density in such a medium is the sum of the conduction current density ($\vec{J}_s = \sigma \vec{E}_s$) and the displacement current density ($\vec{J}_{ds} = j\omega\varepsilon \vec{E}_s$). 
The ratio of the magnitude of the conduction current density to the magnitude of the displacement current density is defined as the **loss tangent**, denoted by $\tan\theta$. Mathematically, it is defined as:
$$\tan\theta = \frac{|\vec{J}_s|}{|\vec{J}_{ds}|} = \frac{|\sigma \vec{E}_s|}{|j\omega\varepsilon \vec{E}_s|} = \frac{\sigma}{\omega\varepsilon}$$
where $\theta$ is known as the loss angle of the medium. The loss tangent is a measure of how "lossy" a medium is at a specific frequency.

**Definition of Skin Depth:**
As an electromagnetic wave travels through a conducting medium, its amplitude is attenuated by an exponential factor $e^{-\alpha z}$. The **skin depth** (or penetration depth), denoted by $\delta$, is defined as the distance through which the wave amplitude decreases by a factor of $e^{-1}$ (which is approximately $36.8\%$) of its initial value. It serves as a measure of the depth to which an EM wave can effectively penetrate a conducting medium.
Mathematically, it is defined as the reciprocal of the attenuation constant ($\alpha$):
$$\delta = \frac{1}{\alpha}$$

**Derivation of Skin Depth for a Good Conductor:**
The general expression for the attenuation constant $\alpha$ in any medium is given by:
$$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2}$$

A medium is characterized as a "good conductor" when its conduction current heavily dominates its displacement current, which means the loss tangent is very large: $\sigma \gg \omega\varepsilon$, or $\frac{\sigma}{\omega\varepsilon} \to \infty$.

Applying this large loss tangent approximation to the term inside the inner square root:
$$1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2 \approx \left(\frac{\sigma}{\omega\varepsilon}\right)^2$$

Substituting this approximation back into the general equation for $\alpha$:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{\left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} - 1 \right]^{1/2}$$

Since $\frac{\sigma}{\omega\varepsilon}$ is extremely large for a good conductor, we can ignore the $-1$ term:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2} \cdot \frac{\sigma}{\omega\varepsilon}}$$

Simplifying the terms:
$$\alpha \approx \omega \sqrt{\frac{\mu\sigma}{2\omega}} = \sqrt{\frac{\omega^2\mu\sigma}{2\omega}} = \sqrt{\frac{\omega\mu\sigma}{2}}$$

Knowing that the angular frequency is $\omega = 2\pi f$, we substitute this in:
$$\alpha = \sqrt{\frac{2\pi f\mu\sigma}{2}} = \sqrt{\pi f \mu \sigma}$$

By definition, the skin depth is $\delta = \frac{1}{\alpha}$. Substituting our expression for $\alpha$ in a good conductor yields the final derived formula:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

*Related location pg no. In provided slides: Slide 318, 319 (Loss tangent definition), Slide 331, 332, 333 (Skin depth definition and derivation).*

***

### 🔴 (b) In a nonmagnetic medium the electric field is given as $\vec{E} = 4 \sin(2\pi \times 10^7 t - 0.8x) \bar{a}_z$ V/m. find relative permittivity and intrinsic impedance of the medium. Calculate also the time-average power carried by the wave.

**Answer:**

From the given time-domain electric field equation $\vec{E} = 4 \sin(2\pi \times 10^7 t - 0.8x) \bar{a}_z$, we can extract the standard uniform plane wave parameters:
*   Amplitude, $E_0 = 4$ V/m
*   Angular frequency, $\omega = 2\pi \times 10^7$ rad/s
*   Phase constant, $\beta = 0.8$ rad/m
*   The wave propagates in the $+x$ direction.
*   The medium is stated as "nonmagnetic," which implies its relative permeability $\mu_r = 1$, so $\mu = \mu_0 = 4\pi \times 10^{-7}$ H/m.

**1. Find Relative Permittivity ($\varepsilon_r$):**
For a lossless medium (implied by the lack of an attenuation factor $e^{-\alpha x}$), the relationship for the phase constant is $\beta = \omega\sqrt{\mu\varepsilon}$.
Substitute $\mu = \mu_0$ and $\varepsilon = \varepsilon_0\varepsilon_r$:
$$\beta = \omega\sqrt{\mu_0\varepsilon_0\varepsilon_r}$$

Knowing that the speed of light in a vacuum is $c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3 \times 10^8$ m/s, we can rewrite the phase constant equation as:
$$\beta = \frac{\omega}{c}\sqrt{\varepsilon_r}$$

Rearranging the formula to solve for $\sqrt{\varepsilon_r}$:
$$\sqrt{\varepsilon_r} = \frac{\beta c}{\omega}$$
$$\sqrt{\varepsilon_r} = \frac{0.8 \times (3 \times 10^8)}{2\pi \times 10^7} = \frac{2.4 \times 10^8}{2\pi \times 10^7} = \frac{24}{2\pi} = \frac{12}{\pi}$$

Squaring both sides gives the relative permittivity:
$$\varepsilon_r = \left(\frac{12}{\pi}\right)^2 = \frac{144}{\pi^2} \approx 14.59$$

**2. Find Intrinsic Impedance ($\eta$):**
The intrinsic impedance of a lossless dielectric medium is given by $\eta = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_0}{\varepsilon_0\varepsilon_r}}$.
This can be written in terms of the intrinsic impedance of free space ($\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \ \Omega$):
$$\eta = \frac{\eta_0}{\sqrt{\varepsilon_r}}$$

Substituting our previously found exact value for $\sqrt{\varepsilon_r} = \frac{12}{\pi}$:
$$\eta = \frac{120\pi}{12/\pi} = \frac{120\pi^2}{12} = 10\pi^2 \ \Omega$$
Numerically, $\eta \approx 98.696 \ \Omega$.

**3. Calculate Time-Average Power ($\vec{\mathcal{P}}_{ave}$):**
The time-average power density (average Poynting vector) for a uniform plane wave is calculated as:
$$\vec{\mathcal{P}}_{ave} = \frac{E_0^2}{2\eta} \hat{a}_k$$
where $\hat{a}_k$ is the unit vector in the direction of wave propagation. Looking at the phase term $(\omega t - \beta x)$, the wave propagates in the positive $x$-direction, so $\hat{a}_k = \bar{a}_x$.

Substitute the known values ($E_0 = 4$ V/m and $\eta = 10\pi^2 \ \Omega$) into the equation:
$$\vec{\mathcal{P}}_{ave} = \frac{4^2}{2(10\pi^2)} \bar{a}_x = \frac{16}{20\pi^2} \bar{a}_x = \frac{0.8}{\pi^2} \bar{a}_x \text{ W/m}^2$$

Numerically, this evaluates to:
$$\vec{\mathcal{P}}_{ave} \approx \frac{0.8}{9.8696} \bar{a}_x \approx 0.08105 \bar{a}_x \text{ W/m}^2 \text{ or } 81.05 \bar{a}_x \text{ mW/m}^2$$

*Related location pg no. In provided slides: Slide 352, 353, 354, 355 (Example 10.7 mirrors this exact calculation).*

***

### 🔴 (a) Using the expression of plane wave, obtain the equation of phase velocity in free space imposing the characteristics of plane wave. Take z = 0 at Rangpur, in Rangpur the expression of electric field of a plane wave is given by $E_x = E_{x0} \cos(2\pi \times 10^8 t)$, calculate $E_x$ at Chittagong that is located 500km south of Rangpur.

**Answer:**

**1. Equation of Phase Velocity in Free Space:**
For a uniform plane wave traveling in the $+z$ direction, the instantaneous electric field can be expressed generally as:
$$E_x(z, t) = E_{x0} \cos(\omega t - \beta z)$$
The phase of this wave is the argument of the cosine function: $\text{Phase} = \omega t - \beta z$. 
The phase velocity ($v$ or $u$) is the speed at which a point of constant phase travels. We find this by setting the phase to a constant and differentiating it with respect to time $t$:
$$\frac{d}{dt}(\omega t - \beta z) = \frac{d}{dt}(\text{constant}) = 0$$
$$\omega - \beta \frac{dz}{dt} = 0$$
$$v = \frac{dz}{dt} = \frac{\omega}{\beta}$$

In free space, we impose the characteristics of a vacuum: conductivity $\sigma=0$, permeability $\mu = \mu_0$, and permittivity $\varepsilon = \varepsilon_0$. The phase constant $\beta$ in a lossless medium is defined as $\beta = \omega\sqrt{\mu\varepsilon}$. For free space, this becomes $\beta = \omega\sqrt{\mu_0\varepsilon_0}$.

Substituting this $\beta$ into the phase velocity equation yields:
$$v = \frac{\omega}{\omega\sqrt{\mu_0\varepsilon_0}} = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = c$$
where $c \approx 3 \times 10^8$ m/s is the universal speed of light in a vacuum.

**2. Calculation for Chittagong:**
Let the propagation axis $z$ point South. 
At Rangpur ($z = 0$), the field is given as:
$$E_x(0,t) = E_{x0} \cos(2\pi \times 10^8 t)$$
Comparing this to the general form $E_x(0,t) = E_{x0} \cos(\omega t)$, we identify the angular frequency as $\omega = 2\pi \times 10^8$ rad/s.

The general traveling wave expression is $E_x(z,t) = E_{x0} \cos(\omega t - \beta z)$.
Since phase velocity $c = \frac{\omega}{\beta}$, we can write $\beta = \frac{\omega}{c}$. Substituting this into the wave equation gives:
$$E_x(z,t) = E_{x0} \cos\left(\omega t - \frac{\omega}{c}z\right) = E_{x0} \cos\left[\omega\left(t - \frac{z}{c}\right)\right]$$

Chittagong is located $z = 500 \text{ km} = 5 \times 10^5 \text{ m}$ south of Rangpur. We must find the time delay factor $\frac{z}{c}$ for this distance:
$$\frac{z}{c} = \frac{5 \times 10^5 \text{ m}}{3 \times 10^8 \text{ m/s}} = \frac{5}{3000} = \frac{1}{600} \text{ seconds} \approx 0.001667 \text{ s}$$

Now, substitute this distance delay back into the wave equation evaluated at Chittagong:
$$E_x(\text{Chittagong}, t) = E_{x0} \cos\left[2\pi \times 10^8 \left(t - \frac{1}{600}\right)\right]$$
$$E_x(\text{Chittagong}, t) = E_{x0} \cos\left[2\pi \times 10^8 (t - 0.001667)\right]$$

*Related location pg no. In provided slides: Slide 279, 280 (Shows an identical conceptual example using Chicago and Cleveland).*

***

### 🔴 (b) Define loss tangent. State how a medium could be characterized by using the value of loss tangent.

**Answer:**

**Definition of Loss Tangent:**
When analyzing electromagnetic wave propagation in any lossy medium, the total current density $\vec{J}_{total}$ consists of two distinct components: the conduction current density $\vec{J}_s = \sigma \vec{E}_s$ and the displacement current density $\vec{J}_{ds} = j\omega\varepsilon \vec{E}_s$. 
The ratio of the magnitude of the conduction current density to the magnitude of the displacement current density is mathematically defined as the **loss tangent**. It is written as:
$$\tan\theta = \frac{|\vec{J}_s|}{|\vec{J}_{ds}|} = \frac{|\sigma \vec{E}_s|}{|j\omega\varepsilon \vec{E}_s|} = \frac{\sigma}{\omega\varepsilon}$$
where $\theta$ is known as the loss angle of the medium. The loss tangent quantifies the degree to which a medium dissipates electromagnetic energy (converting it into heat via conduction) relative to how much it stores energy (via polarization/displacement).

**Characterization of a Medium using Loss Tangent:**
Although there is no strict, absolute line of demarcation, the numerical value of the loss tangent ($\tan\theta = \frac{\sigma}{\omega\varepsilon}$) is the primary metric used to classify whether a medium behaves mostly like a dielectric or mostly like a conductor at a specific operating frequency $\omega$.

1.  **Good (Lossless or Perfect) Dielectric:** A medium is characterized as a good dielectric if its displacement current vastly exceeds its conduction current. This occurs when the loss tangent is very small.
    $$\text{Condition: } \tan\theta = \frac{\sigma}{\omega\varepsilon} \ll 1$$
    In this scenario, the medium acts primarily as an insulator, allowing waves to propagate with minimal attenuation or power loss.

2.  **Good Conductor:** A medium is characterized as a good conductor if its conduction current vastly exceeds its displacement current. This occurs when the loss tangent is very large.
    $$\text{Condition: } \tan\theta = \frac{\sigma}{\omega\varepsilon} \gg 1$$
    In this scenario, the medium dissipates electromagnetic energy rapidly, leading to very high attenuation of the wave and causing the "skin effect," where the wave can only penetrate a tiny, marginal distance into the surface of the material.

*Related location pg no. In provided slides: Slide 318, 319.*

***

### 🔴 (c) Define characteristic impedance of a medium. Show that $\vec{E}$ leads $\vec{H}$ by $45^\circ$ in good conductor.

**Answer:**

**Definition of Characteristic (Intrinsic) Impedance:**
The intrinsic (or characteristic) wave impedance of a medium, denoted by $\eta$, is defined as the ratio of the magnitude of the electric field intensity ($\vec{E}$) to the magnetic field intensity ($\vec{H}$) of a uniform plane wave traveling through that specific medium. 
For a generalized lossy medium, it is a complex quantity defined mathematically by:
$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$
where $\mu$ is the magnetic permeability, $\varepsilon$ is the electric permittivity, $\sigma$ is the conductivity, and $\omega$ is the angular frequency of the wave.

**Proof that $\vec{E}$ leads $\vec{H}$ by $45^\circ$ in a good conductor:**
For a medium to be classified as a "good conductor," its conduction current must greatly exceed its displacement current. Mathematically, this means $\sigma \gg \omega\varepsilon$.

Applying this condition to the denominator of the intrinsic impedance equation:
$$\sigma + j\omega\varepsilon \approx \sigma$$

Substituting this approximation back into the intrinsic impedance equation yields:
$$\eta \approx \sqrt{\frac{j\omega\mu}{\sigma}}$$

To determine the phase angle of this complex impedance, we look at the complex operator $j$. In polar form, $j$ is equivalent to $1 \angle 90^\circ$ or $e^{j\pi/2}$.
Taking the square root of $j$ halves its phase angle:
$$\sqrt{j} = \sqrt{e^{j\pi/2}} = e^{j\pi/4} = 1 \angle 45^\circ$$

Therefore, the intrinsic impedance of a good conductor can be written entirely in polar form as:
$$\eta = \sqrt{\frac{\omega\mu}{\sigma}} \angle 45^\circ = |\eta| \angle 45^\circ$$

Let the electric field be the phase reference, defined in the time domain as $E_x = E_0 e^{-\alpha z} \cos(\omega t - \beta z)$. 
The associated magnetic field $\vec{H}$ is obtained by dividing the $\vec{E}$ field by the complex intrinsic impedance $\eta$. Because dividing by a complex number with an angle of $+45^\circ$ forces us to subtract $45^\circ$ from the phase of the result, the instantaneous magnetic field takes the form:
$$H_y = \frac{E_0}{|\eta|} e^{-\alpha z} \cos(\omega t - \beta z - 45^\circ)$$

Comparing the phase arguments, the electric field phase is $(\omega t - \beta z)$ while the magnetic field phase is $(\omega t - \beta z - 45^\circ)$. Because the magnetic field has a negative phase shift relative to the electric field, we conclude that the electric field $\vec{E}$ leads the magnetic field $\vec{H}$ by $45^\circ$ in time phase within a good conductor.

*Related location pg no. In provided slides: Slide 313 (Definition), Slide 329, 330 (Good Conductor approximation and $45^\circ$ phase shift).*
### (a) Derive the electromagnetic wave equation of electric field in a source free simple media.

**Answer:**

To derive the electromagnetic wave equation for the electric field, we begin with Maxwell's equations. A "simple medium" is linear, isotropic, and homogeneous. "Source-free" means that there are no external charge densities ($\rho_v = 0$) and no external impressed current densities. However, the medium might have a conductivity $\sigma$, allowing for a conduction current $\vec{J} = \sigma\vec{E}$. 

The relevant Maxwell's equations in the time domain for such a medium are:
1.  **Faraday's Law:** $\nabla \times \vec{E} = -\mu \frac{\partial \vec{H}}{\partial t}$
2.  **Ampere's Law:** $\nabla \times \vec{H} = \sigma\vec{E} + \varepsilon \frac{\partial \vec{E}}{\partial t}$
3.  **Gauss's Law for Electric Field:** $\nabla \cdot \vec{E} = \frac{\rho_v}{\varepsilon} = 0$ (since it is source-free)

To derive the wave equation for $\vec{E}$, we take the curl of both sides of Faraday's Law (Equation 1):
$$\nabla \times (\nabla \times \vec{E}) = \nabla \times \left(-\mu \frac{\partial \vec{H}}{\partial t}\right)$$

Since spatial and temporal derivatives are independent, we can swap the order of the curl and the time derivative on the right side:
$$\nabla \times (\nabla \times \vec{E}) = -\mu \frac{\partial}{\partial t} (\nabla \times \vec{H})$$

Next, we use the standard vector identity for the curl of a curl: $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2\vec{E}$. Substituting this into the left side gives:
$$\nabla(\nabla \cdot \vec{E}) - \nabla^2\vec{E} = -\mu \frac{\partial}{\partial t} (\nabla \times \vec{H})$$

Because the medium is source-free, Gauss's Law states $\nabla \cdot \vec{E} = 0$. Therefore, the first term on the left side vanishes:
$$-\nabla^2\vec{E} = -\mu \frac{\partial}{\partial t} (\nabla \times \vec{H})$$

Now, substitute Ampere's Law (Equation 2) into the right side for $\nabla \times \vec{H}$:
$$-\nabla^2\vec{E} = -\mu \frac{\partial}{\partial t} \left(\sigma\vec{E} + \varepsilon \frac{\partial \vec{E}}{\partial t}\right)$$

Distributing the time derivative and the $-\mu$ yields:
$$-\nabla^2\vec{E} = -\mu\sigma \frac{\partial \vec{E}}{\partial t} - \mu\varepsilon \frac{\partial^2 \vec{E}}{\partial t^2}$$

Multiplying both sides by $-1$ provides the general electromagnetic wave equation for the electric field in a lossy, source-free medium:
$$\nabla^2\vec{E} = \mu\sigma \frac{\partial \vec{E}}{\partial t} + \mu\varepsilon \frac{\partial^2 \vec{E}}{\partial t^2}$$

**Note:** If the simple medium is a *perfect dielectric (lossless)*, then the conductivity $\sigma = 0$. The first derivative term drops out, reducing the equation to the classic undamped wave equation:
$$\nabla^2\vec{E} = \mu\varepsilon \frac{\partial^2 \vec{E}}{\partial t^2}$$

*Related location pg no. In provided slides: Slide 272 to Slide 276 (Derivation shown using phasor/Helmholtz forms).*

***

### (b) If the electric field $\bar{E} = 377\cos(10^9 t - 5z)\bar{a}_x$ V/m represents a uniform plane wave propagating through a dielectric media characterized by $\mu = \mu_0$ and $\varepsilon = \varepsilon_0\varepsilon_r$, determine the direction of wave propagation, the phase velocity of wave propagation and magnetic field $\bar{H}$.

**Answer:**

Given the electric field: $\vec{E} = 377\cos(10^9 t - 5z)\hat{a}_x$ V/m.
By comparing this to the standard time-domain wave equation $\vec{E}(z,t) = E_0 \cos(\omega t - \beta z) \hat{a}_E$, we can extract the following parameters:
*   Amplitude, $E_0 = 377$ V/m
*   Angular frequency, $\omega = 10^9$ rad/s
*   Phase constant, $\beta = 5$ rad/m
*   The electric field is polarized in the $\hat{a}_x$ direction.

**1. Direction of Wave Propagation:**
The phase argument of the cosine term is $(\omega t - \beta z)$. The negative sign in front of the spatial variable $z$ indicates that the wave is traveling in the positive $z$-direction.
**Direction: $+z$ direction (or $\hat{a}_z$)**

**2. Phase Velocity of Wave Propagation ($v_p$):**
The phase velocity is defined as the ratio of angular frequency to the phase constant:
$$v_p = \frac{\omega}{\beta} = \frac{10^9}{5} = 0.2 \times 10^9 = 2 \times 10^8 \text{ m/s}$$

**3. Magnetic Field ($\vec{H}$):**
To find the magnetic field, we first need to determine the intrinsic impedance ($\eta$) of the medium. We know that phase velocity is also given by $v_p = \frac{c}{\sqrt{\varepsilon_r}}$, where $c \approx 3 \times 10^8$ m/s is the speed of light in a vacuum.
$$2 \times 10^8 = \frac{3 \times 10^8}{\sqrt{\varepsilon_r}}$$
$$\sqrt{\varepsilon_r} = \frac{3}{2} = 1.5$$

Since the medium is a lossless dielectric (implied by the lack of attenuation in the wave equation and $\mu=\mu_0$), the intrinsic impedance is real and calculated as:
$$\eta = \sqrt{\frac{\mu}{\varepsilon}} = \frac{\eta_0}{\sqrt{\varepsilon_r}}$$
We know the intrinsic impedance of free space $\eta_0 \approx 120\pi \approx 377 \ \Omega$.
$$\eta = \frac{377}{1.5} \approx 251.33 \ \Omega$$

The magnetic field $\vec{H}$ is related to the electric field $\vec{E}$ and the direction of propagation $\hat{a}_k$ by the cross product relationship:
$$\vec{H} = \frac{1}{\eta} (\hat{a}_k \times \vec{E})$$
Here, propagation is in $\hat{a}_z$ and $\vec{E}$ is in $\hat{a}_x$:
$$\vec{H} = \frac{1}{251.33} \hat{a}_z \times [377\cos(10^9 t - 5z)\hat{a}_x]$$

Using the cross-product rule $\hat{a}_z \times \hat{a}_x = \hat{a}_y$:
$$\vec{H} = \frac{377}{251.33} \cos(10^9 t - 5z) \hat{a}_y$$
$$\vec{H} = 1.5 \cos(10^9 t - 5z) \bar{a}_y \text{ A/m}$$

*Related location pg no. In provided slides: Slide 278, 279, 280, 282, 289, and Example 10.1 on Slide 292.*

***

### (c) Show that a linearly polarized wave can be written as the sum of two circularly polarized waves rotating in opposite directions but at the same angular rate.

**Answer:**

To prove this, we will mathematically construct two circularly polarized waves—one rotating right-handed and one rotating left-handed—and sum them together to show that the result is a linearly polarized wave.

Assume a wave propagating in the $+z$ direction. 

**1. Define a Right-Hand Circularly Polarized (RHCP) wave:**
A uniform plane wave is circularly polarized if its $x$ and $y$ components have equal amplitudes but are $90^\circ$ ($\pi/2$ radians) out of phase. 
Let the RHCP wave be defined as:
$$\vec{E}_{RHCP} = E_0 \cos(\omega t - \beta z) \hat{a}_x + E_0 \sin(\omega t - \beta z) \hat{a}_y$$
*(Notice that at $z=0$, as time advances, the vector rotates from the $+x$ axis to the $+y$ axis, which is counter-clockwise. With the thumb pointing in $+z$, the right-hand fingers curl counter-clockwise, hence RHCP).*

**2. Define a Left-Hand Circularly Polarized (LHCP) wave:**
The LHCP wave must have the same amplitude and frequency (angular rate) but rotate in the opposite direction. We can achieve this by negating the $y$-component:
$$\vec{E}_{LHCP} = E_0 \cos(\omega t - \beta z) \hat{a}_x - E_0 \sin(\omega t - \beta z) \hat{a}_y$$
*(At $z=0$, as time advances, the vector rotates from the $+x$ axis to the $-y$ axis, which is clockwise, hence LHCP).*

**3. Sum the two waves:**
According to the principle of linear superposition, the total electric field $\vec{E}_{total}$ is the sum of the two individual waves:
$$\vec{E}_{total} = \vec{E}_{RHCP} + \vec{E}_{LHCP}$$
$$\vec{E}_{total} = \left[ E_0 \cos(\omega t - \beta z) \hat{a}_x + E_0 \sin(\omega t - \beta z) \hat{a}_y \right] + \left[ E_0 \cos(\omega t - \beta z) \hat{a}_x - E_0 \sin(\omega t - \beta z) \hat{a}_y \right]$$

Group the $\hat{a}_x$ and $\hat{a}_y$ terms together:
$$\vec{E}_{total} = [E_0 \cos(\omega t - \beta z) + E_0 \cos(\omega t - \beta z)] \hat{a}_x + [E_0 \sin(\omega t - \beta z) - E_0 \sin(\omega t - \beta z)] \hat{a}_y$$

The $\hat{a}_y$ components perfectly cancel each other out ($+E_0\sin(...) - E_0\sin(...) = 0$). We are left with:
$$\vec{E}_{total} = 2E_0 \cos(\omega t - \beta z) \hat{a}_x$$

**Conclusion:**
The resulting equation, $\vec{E}_{total} = 2E_0 \cos(\omega t - \beta z) \hat{a}_x$, describes a wave that oscillates exclusively along a single axis (the $x$-axis in this case) with an amplitude of $2E_0$. Because the vector remains on a single line at all times, this is the strict definition of a **linearly polarized wave**. 

Therefore, we have successfully shown that summing two circularly polarized waves rotating in opposite directions at the same angular rate yields a linearly polarized wave.

*Related location pg no. In provided slides: Slide 292 (Refers to Section 10.7 Wave Polarization in the textbook).*
### A 2GHz uniform plane wave has an amplitude $E_{y0} = 1.4 \text{ kV/m}$ at $(0, 0, 0)$ at $t = 0$ and propagating in the $\mathbf{a}_z$ direction in a medium where $\varepsilon'' = 1.6 \times 10^{-11} \text{ F/m}$, $\varepsilon' = 3.0 \times 10^{-11} \text{ F/m}$, and $\mu = 2.5 \ \mu\text{H/m}$. Find (i) $\mathbf{E}_y$ at $P(0, 0, 1.8 \text{ cm})$ at $0.2 \text{ ns}$, (ii) $\mathbf{H}_x$ at $P$ at $2.0 \text{ ns}$.

**Answer:**

First, let's identify the given parameters for this lossy dielectric medium:
*   Frequency $f = 2 \text{ GHz} = 2 \times 10^9 \text{ Hz}$
*   Angular frequency $\omega = 2\pi f = 4\pi \times 10^9 \text{ rad/s}$
*   Initial amplitude $E_{y0} = 1.4 \text{ kV/m} = 1400 \text{ V/m}$
*   Real part of permittivity $\varepsilon' = 3.0 \times 10^{-11} \text{ F/m}$
*   Imaginary part of permittivity $\varepsilon'' = 1.6 \times 10^{-11} \text{ F/m}$
*   Permeability $\mu = 2.5 \times 10^{-6} \text{ H/m}$

**1. Calculate the Loss Tangent and Basic Parameters**
The loss tangent is defined as the ratio of the imaginary part to the real part of the complex permittivity:
$$\tan(2\theta_\eta) = \frac{\varepsilon''}{\varepsilon'} = \frac{1.6 \times 10^{-11}}{3.0 \times 10^{-11}} = 0.5333$$

**2. Calculate Attenuation Constant ($\alpha$) and Phase Constant ($\beta$)**
We use the exact general formulas for a lossy medium. First, let's compute the term $\omega\sqrt{\mu\varepsilon'}$:
$$\omega\sqrt{\mu\varepsilon'} = (4\pi \times 10^9) \sqrt{(2.5 \times 10^{-6})(3.0 \times 10^{-11})} = (4\pi \times 10^9)\sqrt{7.5 \times 10^{-17}}$$
$$\omega\sqrt{\mu\varepsilon'} = 4\pi \times 10^9 \times (\sqrt{75} \times 10^{-9}) = 4\pi\sqrt{75} \approx 108.828 \text{ rad/m}$$

Now, compute the inner root term:
$$\sqrt{1 + \left(\frac{\varepsilon''}{\varepsilon'}\right)^2} = \sqrt{1 + (0.5333)^2} = \sqrt{1 + 0.2844} = \sqrt{1.2844} \approx 1.1333$$

Calculate $\alpha$:
$$\alpha = \omega\sqrt{\frac{\mu\varepsilon'}{2}} \left[ \sqrt{1 + \left(\frac{\varepsilon''}{\varepsilon'}\right)^2} - 1 \right]^{1/2} = \frac{108.828}{\sqrt{2}} \sqrt{1.1333 - 1}$$
$$\alpha = \frac{108.828}{\sqrt{2}} \sqrt{0.1333} = 76.953 \times 0.3651 \approx 28.1 \text{ Np/m}$$

Calculate $\beta$:
$$\beta = \omega\sqrt{\frac{\mu\varepsilon'}{2}} \left[ \sqrt{1 + \left(\frac{\varepsilon''}{\varepsilon'}\right)^2} + 1 \right]^{1/2} = \frac{108.828}{\sqrt{2}} \sqrt{1.1333 + 1}$$
$$\beta = 76.953 \times \sqrt{2.1333} = 76.953 \times 1.4606 \approx 112.4 \text{ rad/m}$$

**3. Calculate the Intrinsic Impedance ($\eta$)**
The intrinsic impedance is a complex value defined as $\eta = |\eta|\angle\theta_\eta$.
Magnitude:
$$|\eta| = \frac{\sqrt{\mu/\varepsilon'}}{[1 + (\varepsilon''/\varepsilon')^2]^{1/4}} = \frac{\sqrt{2.5 \times 10^{-6} / 3.0 \times 10^{-11}}}{\sqrt{1.1333}} = \frac{\sqrt{83333.33}}{1.0645} = \frac{288.675}{1.0645} \approx 271.1 \ \Omega$$
Phase Angle:
$$2\theta_\eta = \tan^{-1}(0.5333) = 28.07^\circ \implies \theta_\eta = 14.03^\circ \approx 0.245 \text{ rad}$$
So, $\eta = 271.1 \angle 14.03^\circ \ \Omega$.

**4. Part (i): Find $\mathbf{E}_y$ at $P(0, 0, 1.8 \text{ cm})$ at $0.2 \text{ ns}$**
The general time-domain expression for the electric field propagating in the $+z$ direction and polarized in the $y$-direction is:
$$E_y(z,t) = E_{y0} e^{-\alpha z} \cos(\omega t - \beta z)$$
Given $z = 1.8 \text{ cm} = 0.018 \text{ m}$ and $t = 0.2 \text{ ns} = 0.2 \times 10^{-9} \text{ s}$.
Calculate the individual terms:
*   Exponential decay: $e^{-\alpha z} = e^{-(28.1)(0.018)} = e^{-0.5058} \approx 0.603$
*   Temporal phase: $\omega t = (4\pi \times 10^9)(0.2 \times 10^{-9}) = 0.8\pi \approx 2.513 \text{ rad}$
*   Spatial phase: $\beta z = 112.4 \times 0.018 \approx 2.023 \text{ rad}$

$$E_y(0.018, 0.2 \text{ ns}) = 1400 \times 0.603 \times \cos(2.513 - 2.023)$$
$$E_y = 844.2 \times \cos(0.490 \text{ rad}) = 844.2 \times 0.8823 \approx 744.8 \text{ V/m}$$
**$\mathbf{E}_y \approx 744.8 \text{ V/m}$**

**5. Part (ii): Find $\mathbf{H}_x$ at $P$ at $2.0 \text{ ns}$**
By the right-hand rule for uniform plane waves ($\hat{a}_E \times \hat{a}_H = \hat{a}_k$), since $\hat{a}_E = \hat{a}_y$ and $\hat{a}_k = \hat{a}_z$, the magnetic field must be in the $-\hat{a}_x$ direction because $\hat{a}_y \times (-\hat{a}_x) = \hat{a}_z$.
The time-domain expression for the corresponding magnetic field is:
$$H_x(z,t) = -\frac{E_{y0}}{|\eta|} e^{-\alpha z} \cos(\omega t - \beta z - \theta_\eta)$$
Given $z = 0.018 \text{ m}$ and $t = 2.0 \text{ ns} = 2.0 \times 10^{-9} \text{ s}$.
Calculate the individual terms:
*   Amplitude factor: $\frac{1400}{271.1} \times 0.603 \approx 5.164 \times 0.603 \approx 3.11 \text{ A/m}$
*   Temporal phase: $\omega t = (4\pi \times 10^9)(2.0 \times 10^{-9}) = 8\pi \text{ rad}$ (equivalent to $0 \text{ rad}$)
*   Spatial phase: $\beta z = 2.023 \text{ rad}$
*   Impedance phase: $\theta_\eta = 0.245 \text{ rad}$

$$H_x(0.018, 2.0 \text{ ns}) = -3.11 \times \cos(8\pi - 2.023 - 0.245)$$
$$H_x = -3.11 \times \cos(-2.268 \text{ rad}) = -3.11 \times (-0.645) \approx 1.99 \text{ A/m}$$
**$\mathbf{H}_x \approx 1.99 \text{ A/m}$**

*Related location pg no. In provided slides: Slide 562 (This is identical to Example 8, which references prob 12.11 page 431 HYTE, seventh edition), Slide 308 (Eq 30, 31 for $\alpha, \beta$), Slide 314-315 (Intrinsic impedance $\eta$ calculations).*

***

### (a) Derive the phasor expressions for the electric and magnetic field intensity vectors of an x-polarized uniform plane wave propagating in the $+z$ direction.

**Answer:**

**1. Phasor Expression for the Electric Field ($\vec{E}_s$):**
We start with the source-free vector Helmholtz wave equation for the electric field phasor in a given medium:
$$\nabla^2\vec{E}_s - \gamma^2\vec{E}_s = 0$$
where $\gamma = \alpha + j\beta$ is the complex propagation constant.

For a uniform plane wave, the field does not vary in the transverse directions (i.e., $\frac{\partial}{\partial x} = 0$ and $\frac{\partial}{\partial y} = 0$). The problem specifies that the wave is propagating along the $z$-axis. It also states that the wave is $x$-polarized, meaning the electric field vector only has an $x$-component. Thus, we can write:
$$\vec{E}_s(z) = E_{xs}(z)\hat{a}_x$$

Substituting this into the Helmholtz equation reduces the 3D vector Laplacian to a 1D scalar ordinary differential equation:
$$\frac{d^2 E_{xs}(z)}{dz^2} - \gamma^2 E_{xs}(z) = 0$$

This is a standard second-order linear homogeneous differential equation. Its general solution is a linear combination of forward and backward traveling waves:
$$E_{xs}(z) = E_0^+ e^{-\gamma z} + E_0^- e^{\gamma z}$$
The term $E_0^+ e^{-\gamma z}$ represents a wave propagating in the $+z$ direction, and $E_0^- e^{\gamma z}$ represents a wave propagating in the $-z$ direction. Since the problem explicitly states the wave is propagating in the $+z$ direction, we set the amplitude of the backward-traveling wave to zero ($E_0^- = 0$). Let $E_0^+ = E_0$.
The final phasor expression for the electric field is:
**$$\vec{E}_s(z) = E_0 e^{-\gamma z} \hat{a}_x$$**
*(Note: For a lossless medium, $\gamma = j\beta$, making this $\vec{E}_s(z) = E_0 e^{-j\beta z} \hat{a}_x$)*

**2. Phasor Expression for the Magnetic Field ($\vec{H}_s$):**
To find the corresponding magnetic field, we use Faraday's Law in phasor form:
$$\nabla \times \vec{E}_s = -j\omega\mu \vec{H}_s \implies \vec{H}_s = -\frac{1}{j\omega\mu} (\nabla \times \vec{E}_s)$$

Since $\vec{E}_s$ only has an $x$-component and only depends on $z$, the curl evaluates as follows:
$$\nabla \times \vec{E}_s = \begin{vmatrix} \hat{a}_x & \hat{a}_y & \hat{a}_z \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ E_{xs}(z) & 0 & 0 \end{vmatrix} = \hat{a}_y \frac{\partial E_{xs}(z)}{\partial z}$$

Substituting $E_{xs}(z) = E_0 e^{-\gamma z}$:
$$\nabla \times \vec{E}_s = \hat{a}_y \frac{\partial}{\partial z} (E_0 e^{-\gamma z}) = \hat{a}_y (-\gamma E_0 e^{-\gamma z}) = -\gamma E_0 e^{-\gamma z} \hat{a}_y$$

Now, substitute this curl result back into the rearranged Faraday's law:
$$\vec{H}_s(z) = -\frac{1}{j\omega\mu} (-\gamma E_0 e^{-\gamma z} \hat{a}_y) = \frac{\gamma}{j\omega\mu} E_0 e^{-\gamma z} \hat{a}_y$$

We know that the intrinsic impedance of the medium is defined as $\eta = \frac{j\omega\mu}{\gamma}$. Therefore, $\frac{\gamma}{j\omega\mu} = \frac{1}{\eta}$. Substituting this in gives the final phasor expression for the magnetic field:
**$$\vec{H}_s(z) = \frac{E_0}{\eta} e^{-\gamma z} \hat{a}_y$$**

*Related location pg no. In provided slides: Slide 309-311 (Derivation of $\vec{E}_s$), Slide 313 (Derivation of $\vec{H}_s$).*

***

### (b) What is meant by the skin depth of a conductor? How is it related to the attenuation constant?

**Answer:**

**Meaning of Skin Depth:**
When an electromagnetic wave impinges upon and travels into a conducting medium (like a metal), it does not penetrate infinitely. Because the conductor possesses free charge carriers, the changing electromagnetic field induces currents (eddy currents). These induced currents dissipate the wave's energy as heat (ohmic losses), causing the wave's amplitude to decay exponentially as it moves deeper into the material.

The **skin depth** (or penetration depth), denoted by the Greek letter $\delta$, is a measure of how deeply an electromagnetic wave can penetrate into a conducting material. Specifically, it is defined as the distance the wave must travel into the conductor for its electric (and magnetic) field amplitude to decrease by a factor of $e^{-1}$ (which is approximately $0.368$ or $36.8\%$) relative to its value at the surface. 

Because the majority of the current density is concentrated within this thin layer near the surface, this phenomenon is referred to as the "skin effect."

**Relationship to the Attenuation Constant:**
The attenuation of an electromagnetic wave is governed by the attenuation constant, denoted by $\alpha$ (measured in Nepers per meter, Np/m). The wave amplitude decays according to the exponential function $e^{-\alpha z}$, where $z$ is the distance traveled.

By definition, at the skin depth ($z = \delta$), the amplitude factor must equal $e^{-1}$. Therefore, we can set up the equality:
$$e^{-\alpha \delta} = e^{-1}$$
Equating the exponents gives:
$$-\alpha \delta = -1 \implies \delta = \frac{1}{\alpha}$$

Thus, the skin depth $\delta$ is strictly defined as the mathematical reciprocal of the attenuation constant $\alpha$. For a good conductor, where $\alpha \approx \sqrt{\pi f \mu \sigma}$, the skin depth becomes $\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$.

*Related location pg no. In provided slides: Slide 316 (Attenuation constant definition), Slide 331, 332, 333 (Skin depth definition and formulas).*

***

### (c) Compare the distance required for a uniform plane wave to travel in sea water ($\sigma = 4 \text{ S/m}$, $\mu_r \cong 1$ and $\varepsilon_r \cong 81$) in order that the amplitude is reduced by 80 dB (a factor of 10000) at the frequencies (i) 1kHz; (ii) 100MHz.

**Answer:**

First, we establish the relationship between decibels (dB), the attenuation constant ($\alpha$), and distance ($z$). 
The attenuation of the electric field amplitude is given by $E(z) = E_0 e^{-\alpha z}$. 
The attenuation in dB is defined using $20\log_{10}$ for field amplitudes:
$$\text{Attenuation (dB)} = -20 \log_{10}\left(\frac{E(z)}{E_0}\right) = -20 \log_{10}(e^{-\alpha z}) = 20 (\alpha z) \log_{10}(e)$$
$$80 = 20 \alpha z (0.4343) \implies 80 = 8.686 \alpha z \implies z = \frac{80}{8.686 \alpha} = \frac{9.21}{\alpha} \text{ meters}$$

To find the distance $z$, we must first calculate $\alpha$ for both frequencies. 
Given parameters for sea water: $\sigma = 4 \text{ S/m}$, $\mu = \mu_0 = 4\pi \times 10^{-7} \text{ H/m}$, $\varepsilon = 81\varepsilon_0 = 81 \times \frac{10^{-9}}{36\pi} = \frac{2.25 \times 10^{-9}}{\pi} \text{ F/m}$.

**Case (i): Frequency $f = 1 \text{ kHz} = 10^3 \text{ Hz}$**
Angular frequency $\omega = 2\pi f = 2\pi \times 10^3 \text{ rad/s}$.
First, calculate the loss tangent to characterize the medium:
$$\tan\theta = \frac{\sigma}{\omega\varepsilon} = \frac{4}{(2\pi \times 10^3) \times \left(\frac{2.25 \times 10^{-9}}{\pi}\right)} = \frac{4}{4.5 \times 10^{-6}} \approx 8.89 \times 10^5$$
Since $\tan\theta \gg 1$, sea water at 1 kHz behaves as an excellent **good conductor**. 
We can use the good conductor approximation for $\alpha$:
$$\alpha \approx \sqrt{\pi f \mu \sigma} = \sqrt{\pi (10^3) (4\pi \times 10^{-7}) (4)} = \sqrt{16\pi^2 \times 10^{-4}} = 4\pi \times 10^{-2} \approx 0.1257 \text{ Np/m}$$
Now, calculate the distance $z$ required for 80 dB attenuation:
$$z_1 = \frac{9.21}{\alpha} = \frac{9.21}{0.1257} \approx 73.27 \text{ meters}$$

**Case (ii): Frequency $f = 100 \text{ MHz} = 10^8 \text{ Hz}$**
Angular frequency $\omega = 2\pi f = 2\pi \times 10^8 \text{ rad/s}$.
Calculate the loss tangent:
$$\tan\theta = \frac{\sigma}{\omega\varepsilon} = \frac{4}{(2\pi \times 10^8) \times \left(\frac{2.25 \times 10^{-9}}{\pi}\right)} = \frac{4}{0.45} \approx 8.889$$
Because $8.889$ is neither $\gg 1$ nor $\ll 1$, we must use the exact general formula for $\alpha$ for a **lossy dielectric**:
$$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]}$$
Let's compute the leading term $\omega\sqrt{\mu\varepsilon}$:
$$\omega\sqrt{\mu\varepsilon} = (2\pi \times 10^8) \sqrt{(4\pi \times 10^{-7})\left(\frac{2.25 \times 10^{-9}}{\pi}\right)} = (2\pi \times 10^8) \frac{\sqrt{9 \times 10^{-16}}}{2} = \pi \times 10^8 \times 3 \times 10^{-8} = 3\pi \approx 9.4248 \text{ rad/m}$$
Now, compute the term inside the bracket:
$$\sqrt{1 + (8.889)^2} - 1 = \sqrt{1 + 79.01} - 1 = \sqrt{80.01} - 1 \approx 8.945 - 1 = 7.945$$
Calculate $\alpha$:
$$\alpha = 9.4248 \times \sqrt{\frac{7.945}{2}} = 9.4248 \times \sqrt{3.9725} = 9.4248 \times 1.993 \approx 18.78 \text{ Np/m}$$
Now, calculate the distance $z$ required for 80 dB attenuation:
$$z_2 = \frac{9.21}{\alpha} = \frac{9.21}{18.78} \approx 0.490 \text{ meters} \text{ (or } 49.0 \text{ cm)}$$

**Comparison:**
The distance required to attenuate the wave by 80 dB drops drastically from **$\approx 73.3 \text{ m}$ at 1 kHz** down to **$\approx 0.49 \text{ m}$ at 100 MHz**. This proves that high-frequency electromagnetic waves are attenuated much more rapidly in lossy media like sea water compared to low-frequency waves, confirming the physical reality of the "skin effect."

*Related location pg no. In provided slides: Slide 316 (Attenuation in dB formula), Slide 308 (Exact $\alpha$ formula), Slide 329-330 (Good conductor $\alpha$ formula).*
### (b) Write the characteristic of uniform plane wave. Derive the equation of plane wave propagating in the free space in terms of $\mathbf{H}$.

**Answer:**

**Characteristics of a Uniform Plane Wave:**
1.  **Transverse Nature:** Both the electric field ($\mathbf{E}$) and magnetic field ($\mathbf{H}$) are perpendicular (transverse) to the direction of wave propagation.
2.  **Orthogonality:** The electric and magnetic fields are mutually orthogonal ($\mathbf{E} \perp \mathbf{H}$). The direction of propagation is given by the cross product $\mathbf{E} \times \mathbf{H}$.
3.  **Uniformity:** The $\mathbf{E}$ and $\mathbf{H}$ fields have uniform magnitude and phase over any plane perpendicular to the direction of propagation (equiphase surfaces are flat planes).
4.  **No spatial variation in transverse directions:** If the wave propagates in the $z$-direction, the field components do not vary with $x$ or $y$ (e.g., $\frac{\partial \mathbf{E}}{\partial x} = \frac{\partial \mathbf{E}}{\partial y} = 0$).
5.  **In-Phase:** In a lossless medium (like free space), $\mathbf{E}$ and $\mathbf{H}$ are perfectly in phase with each other in time.
6.  **Intrinsic Impedance:** The ratio of the magnitudes of the electric and magnetic fields is a constant called the intrinsic impedance ($\eta$), where $\eta = \frac{|\mathbf{E}|}{|\mathbf{H}|} = \sqrt{\frac{\mu}{\varepsilon}}$.

**Derivation of the Plane Wave Equation for $\mathbf{H}$ in Free Space:**
In free space, there are no free charges ($\rho_v = 0$) and no conduction currents ($\mathbf{J} = 0$). The medium is lossless ($\sigma = 0$) with permittivity $\varepsilon_0$ and permeability $\mu_0$.
Maxwell's equations in the time domain for free space reduce to:
1.  $\nabla \cdot \mathbf{E} = 0$
2.  $\nabla \cdot \mathbf{H} = 0$
3.  $\nabla \times \mathbf{E} = -\mu_0 \frac{\partial \mathbf{H}}{\partial t}$  (Faraday's Law)
4.  $\nabla \times \mathbf{H} = \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}$   (Ampere's Law)

To derive the wave equation for $\mathbf{H}$, we take the curl of both sides of Ampere's Law (Equation 4):
$$\nabla \times (\nabla \times \mathbf{H}) = \nabla \times \left(\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}\right)$$

Since spatial derivatives ($\nabla$) and time derivatives ($\frac{\partial}{\partial t}$) are independent, we can exchange their order on the right side:
$$\nabla \times (\nabla \times \mathbf{H}) = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

Now, we apply the standard vector identity for the curl of a curl to the left side: $\nabla \times (\nabla \times \mathbf{H}) = \nabla(\nabla \cdot \mathbf{H}) - \nabla^2\mathbf{H}$.
Substitute this into the equation:
$$\nabla(\nabla \cdot \mathbf{H}) - \nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

From Equation 2, we know $\nabla \cdot \mathbf{H} = 0$, so the first term on the left vanishes:
$$-\nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

Next, substitute Faraday's Law (Equation 3) into the right side for $\nabla \times \mathbf{E}$:
$$-\nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}\left(-\mu_0 \frac{\partial \mathbf{H}}{\partial t}\right)$$

Simplify the right side:
$$-\nabla^2\mathbf{H} = -\mu_0\varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2}$$

Multiply by $-1$ to get the final electromagnetic wave equation for the magnetic field in free space:
$$\nabla^2\mathbf{H} = \mu_0\varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2}$$
*(This can also be written as $\nabla^2\mathbf{H} - \frac{1}{c^2}\frac{\partial^2 \mathbf{H}}{\partial t^2} = 0$, where $c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$).*

*Related location pg no. In provided slides: Slide 272-273 (Derivation of wave equation), Slide 283 (Characteristics of uniform plane wave).*

***

### (c) Define skin depth. Determine the value of skin depth for copper for a wave of frequency of $200\text{ Hz}$.

**Answer:**

**Definition of Skin Depth:**
When an electromagnetic wave travels through a lossy or conducting medium, its amplitude decays exponentially as it penetrates deeper into the material. The **skin depth** (also called penetration depth), denoted by the Greek letter $\delta$, is defined as the distance an electromagnetic wave must travel into a conducting medium for its amplitude (electric or magnetic field) to be reduced to $e^{-1}$ (which is approximately $0.368$ or $36.8\%$) of its value at the surface. 
Mathematically, it is the reciprocal of the attenuation constant $\alpha$:
$$\delta = \frac{1}{\alpha}$$
For a good conductor (where conduction current dominates displacement current, $\sigma \gg \omega\varepsilon$), the skin depth is approximated by the formula: $\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$.

**Calculation for Copper at $200\text{ Hz}$:**
To calculate the skin depth for copper, we need its standard material properties:
*   Conductivity of copper, $\sigma_{Cu} \approx 5.8 \times 10^7 \text{ S/m}$
*   Permeability of copper, $\mu_{Cu} \approx \mu_0 = 4\pi \times 10^{-7} \text{ H/m}$ (copper is nonmagnetic)
*   Given frequency, $f = 200 \text{ Hz}$

Since copper is an excellent conductor, we use the good conductor approximation formula:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

Substitute the values:
$$\delta = \frac{1}{\sqrt{\pi \cdot (200) \cdot (4\pi \times 10^{-7}) \cdot (5.8 \times 10^7)}}$$
$$\delta = \frac{1}{\sqrt{200 \cdot 4 \cdot 5.8 \cdot \pi^2 \cdot 10^{-7} \cdot 10^7}}$$
$$\delta = \frac{1}{\sqrt{4640 \cdot \pi^2}}$$
$$\delta = \frac{1}{\pi \sqrt{4640}}$$
$$\delta \approx \frac{1}{3.14159 \times 68.1175}$$
$$\delta \approx \frac{1}{214.05}$$
$$\delta \approx 0.00467 \text{ meters}$$

Therefore, the skin depth for copper at $200\text{ Hz}$ is approximately **$4.67\text{ mm}$**.

*Related location pg no. In provided slides: Slide 331, 332, 333 (Skin depth definition and formulas), Slide 203, 208 (Reference to standard properties like conductivity).*

***

### (a) Define standing wave ratio. Show that $1 + \Gamma = \tau$, where the symbols have their usual meanings.

**Answer:**

**Definition of Standing Wave Ratio (SWR):**
When a uniform plane wave reflects off a boundary between two media, the incident and reflected waves combine to form a standing wave. The Standing Wave Ratio (denoted as $s$ or SWR) is defined as the ratio of the maximum amplitude of the electric field to the minimum amplitude of the electric field in this standing wave pattern. 
Mathematically, it is expressed in terms of the magnitude of the reflection coefficient $|\Gamma|$:
$$s = \frac{|E|_{max}}{|E|_{min}} = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$
The SWR is a dimensionless quantity that ranges from $1$ (no reflection, $|\Gamma| = 0$) to $\infty$ (total reflection, $|\Gamma| = 1$).

**Proof that $1 + \Gamma = \tau$:**
Consider a uniform plane wave propagating in Medium 1 normally incident upon the boundary of Medium 2 located at $z = 0$. 
Let the incident electric field amplitude be $E_{i0}$, the reflected electric field amplitude be $E_{r0}$, and the transmitted electric field amplitude be $E_{t0}$.
The total electric field in Medium 1 is the sum of the incident and reflected fields:
$$\vec{E}_1 = \vec{E}_i + \vec{E}_r$$
The total electric field in Medium 2 is just the transmitted field:
$$\vec{E}_2 = \vec{E}_t$$

One of the fundamental boundary conditions for electromagnetic fields is that the tangential components of the electric field must be continuous across the interface. For a normally incident plane wave, the entire electric field vector is tangential to the boundary plane at $z=0$.
Therefore, matching the fields at the boundary ($z=0$):
$$\vec{E}_1(z=0) = \vec{E}_2(z=0)$$
$$E_{i0} + E_{r0} = E_{t0}$$

Now, divide the entire equation by the incident amplitude $E_{i0}$:
$$\frac{E_{i0}}{E_{i0}} + \frac{E_{r0}}{E_{i0}} = \frac{E_{t0}}{E_{i0}}$$
$$1 + \frac{E_{r0}}{E_{i0}} = \frac{E_{t0}}{E_{i0}}$$

By definition, the reflection coefficient $\Gamma$ is the ratio of the reflected electric field amplitude to the incident electric field amplitude:
$$\Gamma = \frac{E_{r0}}{E_{i0}}$$
And the transmission coefficient $\tau$ is the ratio of the transmitted electric field amplitude to the incident electric field amplitude:
$$\tau = \frac{E_{t0}}{E_{i0}}$$

Substituting these definitions into our equation yields:
$$1 + \Gamma = \tau$$
This proves the relationship between the reflection and transmission coefficients for normal incidence.

*Related location pg no. In provided slides: Slide 377 (SWR definition), Slide 362-366 (Boundary conditions and derivation of $1+\Gamma=\tau$ on slide 407, eq 78).*

***

### (b) The electric field of a travelling wave is $10\cos(10^9t - 4z)$. Determine the velocity and wavelength of the wave.

**Answer:**

The given expression for the electric field is:
$$E = 10\cos(10^9t - 4z)$$
We compare this given expression to the standard mathematical form of a traveling uniform plane wave:
$$E = E_0\cos(\omega t - \beta z)$$

By direct comparison, we can extract the wave's angular frequency ($\omega$) and phase constant ($\beta$):
*   Angular frequency, $\omega = 10^9 \text{ rad/s}$
*   Phase constant, $\beta = 4 \text{ rad/m}$

**1. Determine the velocity of the wave ($v$):**
The phase velocity of a wave is the ratio of its angular frequency to its phase constant.
$$v = \frac{\omega}{\beta}$$
Substitute the extracted values:
$$v = \frac{10^9}{4} = 0.25 \times 10^9 = 2.5 \times 10^8 \text{ m/s}$$

**2. Determine the wavelength of the wave ($\lambda$):**
The wavelength is the spatial period of the wave, related to the phase constant by:
$$\lambda = \frac{2\pi}{\beta}$$
Substitute the phase constant:
$$\lambda = \frac{2\pi}{4} = \frac{\pi}{2} \text{ meters}$$
Numerically, $\lambda \approx 1.57 \text{ m}$.

*Related location pg no. In provided slides: Slide 280, Slide 289 (Phase velocity and wavelength formulas).*

***

### (c) What is meant by polarization? Show that $\nabla \times \mathbf{E} = 0$ for electrostatic field.

**Answer:**

**Meaning of Polarization:**
Polarization of a uniform plane electromagnetic wave refers to the time-varying behavior and orientation of the electric field vector $\mathbf{E}$ at a fixed point in space as the wave propagates. It describes the geometric figure (locus) traced by the tip of the electric field vector over one complete cycle (one period). 
Depending on the relative amplitudes and phase differences of the orthogonal components of the $\mathbf{E}$ field, the polarization can be classified as:
1.  **Linear:** The electric field vector oscillates along a single straight line.
2.  **Circular:** The electric field vector rotates in a circle, maintaining a constant magnitude.
3.  **Elliptical:** The electric field vector rotates and changes magnitude, tracing an ellipse (this is the most general case).

**Proof that $\nabla \times \mathbf{E} = 0$ for an Electrostatic Field:**
There are two primary ways to show this based on fundamental principles:

*Method 1: From the Conservative Nature of Electrostatic Fields (Work-Energy)*
By definition, an electrostatic field is conservative. This means that the net work done by the field in moving a test charge $q$ around any closed path $L$ is identically zero.
$$W = -q \oint_L \mathbf{E} \cdot d\mathbf{l} = 0$$
Dividing by $-q$ gives the integral form of this property:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = 0$$
To find the differential (point) form, we apply Stokes's theorem, which relates the closed line integral to a surface integral of the curl over the open surface $S$ bounded by the path $L$:
$$\oint_L \mathbf{E} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S} = 0$$
For this surface integral to evaluate to zero for *any* arbitrarily chosen surface $S$, the integrand itself must be zero everywhere in the region.
Therefore:
$$\nabla \times \mathbf{E} = 0$$

*Method 2: From Faraday's Law*
Maxwell's equation derived from Faraday's law of induction for general time-varying fields is:
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
In an electrostatic scenario, all fields are static, meaning they do not change with time. Therefore, all time derivatives evaluate to zero:
$$\frac{\partial \mathbf{B}}{\partial t} = 0$$
Substituting this into Faraday's law directly yields:
$$\nabla \times \mathbf{E} = 0$$

Both methods demonstrate that an electrostatic field is irrotational (curl-free).

*Related location pg no. In provided slides: Slide 283, 498 (Polarization definition/mention), Slide 160-161, 172 (Conservative field proof).*
### (c) What do you mean by skin effect? What are the factors that influence the skin effect?

**Answer:**

**Meaning of Skin Effect:**
The skin effect is a phenomenon observed in conductors carrying alternating current (AC) or high-frequency electromagnetic waves. Unlike direct current (DC), which distributes evenly across the entire cross-section of a conductor, alternating current tends to crowd near the surface (the "skin") of the conductor. 
As an electromagnetic wave impinges upon and travels into a conducting medium, the changing electric and magnetic fields induce eddy currents within the material. These eddy currents oppose the original fields deeper inside the conductor, causing the wave's amplitude to decay exponentially as it penetrates. Because the current density is highest at the surface and decreases exponentially with depth, the effective cross-sectional area through which the current flows is reduced, leading to an increase in the effective AC resistance (skin resistance) compared to the DC resistance.

**Factors Influencing the Skin Effect:**
The severity of the skin effect (quantified by how small the skin depth $\delta$ is) depends on three main factors of the conductor and the wave:
1.  **Frequency ($f$):** As frequency increases, the rate of change of magnetic fields increases, inducing stronger opposing eddy currents. Therefore, higher frequencies lead to a more pronounced skin effect (shallower skin depth).
2.  **Conductivity ($\sigma$):** Better conductors (higher $\sigma$) allow for stronger induced eddy currents, which more effectively cancel the fields deeper inside. Thus, higher conductivity results in a stronger skin effect.
3.  **Permeability ($\mu$):** Materials with higher magnetic permeability concentrate magnetic flux more intensely, increasing the induced opposing currents. Magnetic materials experience a much stronger skin effect than non-magnetic materials of the same conductivity.

*Related location pg no. In provided slides: Slide 331, 332, 334 (Skin depth, attenuation, and ac resistance due to skin effect).*

***

### (a) Write the characteristic of uniform plane wave. Derive the equation of plane EM wave propagating in free space in terms of H.

**Answer:**

**Characteristics of a Uniform Plane Wave:**
1.  **Transverse Nature:** Both the electric field ($\mathbf{E}$) and magnetic field ($\mathbf{H}$) vectors are perpendicular (transverse) to each other and to the direction of wave propagation.
2.  **Uniformity:** The $\mathbf{E}$ and $\mathbf{H}$ fields have uniform magnitude and phase over any plane perpendicular to the direction of propagation (equiphase surfaces are flat planes).
3.  **No Transverse Variation:** If the wave propagates in the $z$-direction, the field components do not vary with $x$ or $y$ (i.e., $\frac{\partial \mathbf{E}}{\partial x} = \frac{\partial \mathbf{E}}{\partial y} = 0$).
4.  **In-Phase (in Lossless Media):** In a lossless medium like free space, the $\mathbf{E}$ and $\mathbf{H}$ fields oscillate perfectly in phase with each other in the time domain.
5.  **Intrinsic Impedance:** The ratio of the magnitudes of the electric and magnetic fields is a constant determined by the medium, called the intrinsic impedance ($\eta = \frac{|\mathbf{E}|}{|\mathbf{H}|} = \sqrt{\frac{\mu}{\varepsilon}}$).

**Derivation of the Plane Wave Equation for $\mathbf{H}$ in Free Space:**
In free space, there are no free charges ($\rho_v = 0$) and no conduction currents ($\mathbf{J} = 0$). The medium is lossless ($\sigma = 0$) with permittivity $\varepsilon_0$ and permeability $\mu_0$.
Maxwell's equations in the time domain for free space reduce to:
1.  $\nabla \cdot \mathbf{E} = 0$
2.  $\nabla \cdot \mathbf{H} = 0$
3.  $\nabla \times \mathbf{E} = -\mu_0 \frac{\partial \mathbf{H}}{\partial t}$  (Faraday's Law)
4.  $\nabla \times \mathbf{H} = \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}$   (Ampere's Law)

To derive the wave equation for $\mathbf{H}$, we take the curl of both sides of Ampere's Law (Equation 4):
$$\nabla \times (\nabla \times \mathbf{H}) = \nabla \times \left(\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}\right)$$

Since spatial derivatives ($\nabla$) and time derivatives ($\frac{\partial}{\partial t}$) are independent linear operators, we can exchange their order on the right side:
$$\nabla \times (\nabla \times \mathbf{H}) = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

Now, we apply the standard vector identity for the curl of a curl to the left side: $\nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$.
Substitute this into the equation:
$$\nabla(\nabla \cdot \mathbf{H}) - \nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

From Equation 2, we know $\nabla \cdot \mathbf{H} = 0$, so the first term on the left vanishes:
$$-\nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{E})$$

Next, substitute Faraday's Law (Equation 3) into the right side for $\nabla \times \mathbf{E}$:
$$-\nabla^2\mathbf{H} = \varepsilon_0 \frac{\partial}{\partial t}\left(-\mu_0 \frac{\partial \mathbf{H}}{\partial t}\right)$$

Simplify the right side by pulling out the constants:
$$-\nabla^2\mathbf{H} = -\mu_0\varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2}$$

Multiply by $-1$ to get the final electromagnetic wave equation for the magnetic field in free space:
$$\nabla^2\mathbf{H} = \mu_0\varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2}$$

*Related location pg no. In provided slides: Slide 272-273 (Wave equation derivation steps), Slide 283 (Characteristics of uniform plane wave).*

***

### (b) Define skin depth. Derive the equation of skin depth for a good conductor. Hence determine the value of it for copper operating at $60\text{ Hz}$.

**Answer:**

**Definition of Skin Depth:**
When an electromagnetic wave travels through a lossy or conducting medium, its amplitude decays exponentially as it penetrates deeper. The **skin depth** (or penetration depth), denoted by $\delta$, is defined as the distance an electromagnetic wave must travel into a conducting medium for its amplitude to be reduced by a factor of $e^{-1}$ (which is approximately $36.8\%$) relative to its value at the surface. 
Mathematically, it is defined as the reciprocal of the attenuation constant $\alpha$:
$$\delta = \frac{1}{\alpha}$$

**Derivation of Skin Depth for a Good Conductor:**
The general expression for the attenuation constant $\alpha$ in any medium is given by:
$$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2}$$

A medium is categorized as a "good conductor" when its conduction current heavily dominates its displacement current. This means the loss tangent is very large: $\sigma \gg \omega\varepsilon$, or $\frac{\sigma}{\omega\varepsilon} \to \infty$.

Applying this large loss tangent approximation to the term inside the inner square root:
$$1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2 \approx \left(\frac{\sigma}{\omega\varepsilon}\right)^2$$

Substituting this approximation back into the general equation for $\alpha$:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{\left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} - 1 \right]^{1/2}$$

Since $\frac{\sigma}{\omega\varepsilon}$ is extremely large for a good conductor, we can ignore the $-1$ term:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2} \cdot \frac{\sigma}{\omega\varepsilon}}$$

Simplifying the terms under the square root:
$$\alpha \approx \omega \sqrt{\frac{\mu\sigma}{2\omega}} = \sqrt{\frac{\omega^2\mu\sigma}{2\omega}} = \sqrt{\frac{\omega\mu\sigma}{2}}$$

Knowing that the angular frequency is $\omega = 2\pi f$, we substitute this in:
$$\alpha = \sqrt{\frac{2\pi f\mu\sigma}{2}} = \sqrt{\pi f \mu \sigma}$$

By definition, the skin depth is $\delta = \frac{1}{\alpha}$. Substituting our expression for $\alpha$ in a good conductor yields the derived formula:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

**Calculation for Copper at $60\text{ Hz}$:**
We need the standard material properties for copper:
*   Conductivity of copper, $\sigma_{Cu} \approx 5.8 \times 10^7 \text{ S/m}$
*   Permeability of copper, $\mu_{Cu} \approx \mu_0 = 4\pi \times 10^{-7} \text{ H/m}$ (copper is nonmagnetic)
*   Given frequency, $f = 60 \text{ Hz}$

Substitute the values into the derived formula:
$$\delta = \frac{1}{\sqrt{\pi \cdot 60 \cdot (4\pi \times 10^{-7}) \cdot (5.8 \times 10^7)}}$$
$$\delta = \frac{1}{\sqrt{240 \cdot 4 \cdot 5.8 \cdot \pi^2 \cdot 10^{-7} \cdot 10^7}}$$
$$\delta = \frac{1}{\sqrt{240 \cdot \pi^2 \cdot 5.8}}$$
$$\delta = \frac{1}{\pi\sqrt{1392}}$$
$$\delta \approx \frac{1}{3.14159 \times 37.31}$$
$$\delta \approx \frac{1}{117.21} \approx 0.00853 \text{ meters}$$

Therefore, the skin depth for copper at $60\text{ Hz}$ is approximately **$8.53\text{ mm}$**.

*Related location pg no. In provided slides: Slide 331, 332, 333 (Skin depth definition and formulas), Slide 203/208 (Reference to standard properties like conductivity).*

***

### (c) A $5\text{-GHz}$ uniform plane wave is propagating in a material characterized by $\varepsilon_r = 2.53$, $\mu_r = 1$, and $\sigma = 0$. If the electric field is given by $E = 10\cos(10\pi \times 10^9 t - \beta z)a_x$, determine (i) $u_p$ (ii) $\lambda$ (iii) $\beta$ and (iv) the magnitude of magnetic field.

**Answer:**

From the problem statement, we have the following parameters for the medium and the wave:
*   Operating frequency $f = 5\text{ GHz} = 5 \times 10^9\text{ Hz}$
*   Angular frequency $\omega = 2\pi f = 10\pi \times 10^9\text{ rad/s}$ (matches the term in the cosine argument)
*   Relative permittivity $\varepsilon_r = 2.53$
*   Relative permeability $\mu_r = 1$ (implies $\mu = \mu_0$)
*   Conductivity $\sigma = 0$ (implies a **lossless dielectric** medium)
*   Electric field amplitude $E_0 = 10\text{ V/m}$

Because $\sigma = 0$, the medium is a perfect (lossless) dielectric. We will use the standard formulas for this case.

**(i) Determine the phase velocity ($u_p$):**
In a lossless dielectric, phase velocity is given by:
$$u_p = \frac{c}{\sqrt{\mu_r \varepsilon_r}}$$
where $c \approx 3 \times 10^8\text{ m/s}$.
$$u_p = \frac{3 \times 10^8}{\sqrt{(1)(2.53)}}$$
$$u_p = \frac{3 \times 10^8}{1.5906} \approx 1.886 \times 10^8 \text{ m/s}$$

**(ii) Determine the wavelength ($\lambda$):**
Wavelength is the ratio of phase velocity to frequency:
$$\lambda = \frac{u_p}{f}$$
$$\lambda = \frac{1.886 \times 10^8}{5 \times 10^9} = 0.03772 \text{ meters}$$
$$\lambda \approx 37.7 \text{ mm}$$

**(iii) Determine the phase constant ($\beta$):**
The phase constant for a lossless medium is:
$$\beta = \omega\sqrt{\mu\varepsilon} = \frac{\omega}{u_p}$$
$$\beta = \frac{10\pi \times 10^9}{1.886 \times 10^8} \approx 53.02\pi \text{ rad/m}$$
Numerically, $\beta \approx 166.57 \text{ rad/m}$.

**(iv) Determine the magnitude of the magnetic field ($H_0$):**
The magnitude of the magnetic field is related to the electric field amplitude by the intrinsic impedance $\eta$ of the medium:
$$H_0 = \frac{E_0}{\eta}$$
First, calculate the intrinsic impedance for a lossless dielectric:
$$\eta = \sqrt{\frac{\mu}{\varepsilon}} = \frac{\eta_0}{\sqrt{\varepsilon_r}}$$
where $\eta_0 \approx 120\pi \approx 377 \ \Omega$.
$$\eta = \frac{377}{\sqrt{2.53}} = \frac{377}{1.5906} \approx 237.0 \ \Omega$$
Now calculate $H_0$:
$$H_0 = \frac{10}{237.0} \approx 0.04219 \text{ A/m}$$
The magnitude of the magnetic field is approximately **$42.2\text{ mA/m}$**.

*Related location pg no. In provided slides: Slide 323, 324 (Formulas for Plane waves in lossless dielectrics), Slide 289, 290 (velocity, lambda, beta).*
### (b) Write the characteristic of uniform plane wave. Derive the equation of plane wave propagating in the free space in terms of E.

**Answer:**

**Characteristics of a Uniform Plane Wave:**
1.  **Transverse Nature:** Both the electric field ($\vec{E}$) and the magnetic field ($\vec{H}$) are perpendicular (transverse) to each other and to the direction of wave propagation. There is no field component in the direction of propagation.
2.  **Orthogonality:** The vectors $\vec{E}$, $\vec{H}$, and the direction of propagation ($\hat{k}$) form a mutually orthogonal right-handed system, such that $\hat{a}_E \times \hat{a}_H = \hat{a}_k$.
3.  **Uniformity:** The amplitudes and phases of the $\vec{E}$ and $\vec{H}$ fields are uniform (constant) over any plane that is perpendicular to the direction of propagation. Such planes are called equiphase surfaces.
4.  **No Spatial Variation in Transverse Directions:** If a wave propagates along the $z$-axis, the partial derivatives of the fields with respect to the transverse axes ($x$ and $y$) are zero: $\frac{\partial}{\partial x} = 0$ and $\frac{\partial}{\partial y} = 0$.
5.  **Time Phase:** In a lossless medium (like free space), the $\vec{E}$ and $\vec{H}$ fields oscillate perfectly in phase with each other in time.
6.  **Intrinsic Impedance:** The ratio of the magnitude of the electric field to the magnetic field is a constant defined by the medium, called the intrinsic impedance: $\eta = \frac{|\vec{E}|}{|\vec{H}|} = \sqrt{\frac{\mu}{\varepsilon}}$.

**Derivation of the Plane Wave Equation for $\vec{E}$ in Free Space:**
In free space, the medium is characterized by zero volume charge density ($\rho_v = 0$), zero conduction current density ($\vec{J} = 0$), conductivity $\sigma = 0$, permeability $\mu = \mu_0$, and permittivity $\varepsilon = \varepsilon_0$.

We begin with Maxwell's curl equations in the time domain for free space:
1.  Faraday's Law: $\nabla \times \vec{E} = -\mu_0 \frac{\partial \vec{H}}{\partial t}$
2.  Ampere's Law: $\nabla \times \vec{H} = \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$

To derive the wave equation for the electric field, take the curl of both sides of Faraday's Law:
$$\nabla \times (\nabla \times \vec{E}) = \nabla \times \left(-\mu_0 \frac{\partial \vec{H}}{\partial t}\right)$$

Because spatial derivatives ($\nabla$) and time derivatives ($\frac{\partial}{\partial t}$) are independent, we can swap their order on the right side:
$$\nabla \times (\nabla \times \vec{E}) = -\mu_0 \frac{\partial}{\partial t}(\nabla \times \vec{H})$$

Apply the standard vector identity to the left side: $\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2\vec{A}$.
$$\nabla(\nabla \cdot \vec{E}) - \nabla^2\vec{E} = -\mu_0 \frac{\partial}{\partial t}(\nabla \times \vec{H})$$

From Gauss's Law for electric fields in a charge-free region ($\rho_v = 0$), we know $\nabla \cdot \vec{E} = 0$. Thus, the first term on the left vanishes:
$$-\nabla^2\vec{E} = -\mu_0 \frac{\partial}{\partial t}(\nabla \times \vec{H})$$

Now, substitute Ampere's Law ($\nabla \times \vec{H} = \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$) into the right side of the equation:
$$-\nabla^2\vec{E} = -\mu_0 \frac{\partial}{\partial t}\left(\varepsilon_0 \frac{\partial \vec{E}}{\partial t}\right)$$

Simplify by pulling out constants and applying the second time derivative:
$$-\nabla^2\vec{E} = -\mu_0\varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Multiply both sides by $-1$ to arrive at the classic electromagnetic wave equation for the electric field in free space:
$$\nabla^2\vec{E} = \mu_0\varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

*Related location: Standard Electromagnetics textbooks (e.g., Sadiku "Elements of Electromagnetics") Chapter on Electromagnetic Wave Propagation, Section on Waves in General / Free Space.*

***

### (c) Define polarization. Discuss different type of polarizations.

**Answer:**

**Definition of Polarization:**
The polarization of a uniform plane electromagnetic wave describes the time-varying behavior and geometric orientation of the electric field vector ($\vec{E}$) at a fixed point in space as the wave passes through that point. It is defined by the shape (locus) traced by the tip of the $\vec{E}$ vector over one complete period of oscillation. 

**Types of Polarization:**
Depending on the relative amplitudes and the phase difference between the orthogonal components of the electric field, polarization is broadly classified into three types:

1.  **Linear Polarization:**
    A wave is linearly polarized if the electric field vector always oscillates along a single, fixed straight line in the transverse plane. This occurs under two conditions:
    *   The wave has only one transverse component (e.g., only an $E_x$ component or only an $E_y$ component).
    *   The wave has two transverse components ($E_x$ and $E_y$), but they are either exactly in phase (phase difference $\delta = 0^\circ$) or exactly out of phase ($\delta = 180^\circ$).

2.  **Circular Polarization:**
    A wave is circularly polarized if the tip of the electric field vector traces out a perfect circle in the transverse plane as time progresses. The magnitude of the $\vec{E}$ field remains constant, but its direction rotates continuously. This requires two specific conditions to be met simultaneously:
    *   The orthogonal components must have equal amplitudes ($|E_x| = |E_y|$).
    *   The orthogonal components must have a phase difference of exactly $90^\circ$ ($\pi/2$ radians).
    *   *Sub-types:* Depending on the direction of rotation relative to wave propagation, it is classified as Right-Hand Circular Polarization (RHCP) or Left-Hand Circular Polarization (LHCP).

3.  **Elliptical Polarization:**
    This is the most general state of polarization. A wave is elliptically polarized if the tip of the electric field vector traces out an ellipse in the transverse plane. This occurs when the field has two orthogonal components that do not meet the strict conditions for linear or circular polarization.
    *   It happens when the components have unequal amplitudes and an arbitrary phase difference (other than $0^\circ$ or $180^\circ$).
    *   Like circular polarization, elliptical polarization can also be Right-Handed or Left-Handed depending on the rotation direction.

*Related location: Standard Electromagnetics textbooks (e.g., Sadiku "Elements of Electromagnetics") Chapter on Electromagnetic Wave Propagation, Section on Wave Polarization.*

***

### (b) What is skin depth? Derive the expression of skin depth.

**Answer:**

**Definition of Skin Depth:**
When an electromagnetic wave travels through a lossy dielectric or a conducting medium, its amplitude decays exponentially as it penetrates the material. The **skin depth** (also known as the depth of penetration), denoted by the Greek letter $\delta$, is defined as the distance the wave must travel into the lossy medium for its amplitude to be attenuated by a factor of $e^{-1}$ (which is approximately $36.8\%$) relative to its initial value at the surface. 
Mathematically, it is the reciprocal of the attenuation constant $\alpha$:
$$\delta = \frac{1}{\alpha}$$

**Derivation of the Expression for Skin Depth (for a Good Conductor):**
To derive a practical expression for skin depth, we typically assume the medium is a "good conductor." 
The general expression for the attenuation constant $\alpha$ in any medium is:
$$\alpha = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2}$$

A medium is defined as a good conductor when its conduction current heavily dominates its displacement current, which means $\sigma \gg \omega\varepsilon$. Therefore, the ratio $\left(\frac{\sigma}{\omega\varepsilon}\right)$ is very large.

Applying this approximation to the term under the inner square root:
$$1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2 \approx \left(\frac{\sigma}{\omega\varepsilon}\right)^2$$

Substitute this back into the general equation for $\alpha$:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \sqrt{\left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1 \right]^{1/2} = \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} - 1 \right]^{1/2}$$

Because $\frac{\sigma}{\omega\varepsilon}$ is extremely large, subtracting $1$ has a negligible effect, allowing us to approximate further:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon}{2}} \left[ \frac{\sigma}{\omega\varepsilon} \right]^{1/2}$$

Combine the terms inside a single square root:
$$\alpha \approx \omega \sqrt{\frac{\mu\varepsilon\sigma}{2\omega\varepsilon}} = \sqrt{\frac{\omega^2\mu\sigma}{2\omega}} = \sqrt{\frac{\omega\mu\sigma}{2}}$$

Since angular frequency is $\omega = 2\pi f$, substitute this into the expression:
$$\alpha = \sqrt{\frac{2\pi f\mu\sigma}{2}} = \sqrt{\pi f \mu \sigma}$$

By definition, the skin depth is $\delta = \frac{1}{\alpha}$. Therefore, substituting the derived expression for $\alpha$ gives the standard formula for skin depth in a good conductor:
$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

*Related location: Standard Electromagnetics textbooks (e.g., Sadiku "Elements of Electromagnetics") Chapter on Electromagnetic Wave Propagation, Section on Plane Waves in Good Conductors.*

***

### (c) Consider the boundary between free space and glass having $\sigma = 0$, $\varepsilon_r = 4$ and $\mu_r = 1$. If a uniform plane wave with $E_{oi} = 1 \text{ V/m}$ and a frequency of $200 \text{ MHz}$ is incident from the free space normal to the glass, determine: (i) the time-domain forms of the incident, reflected and transmitted fields. (ii) the average power transmitted through a $5 \text{ m}^2$ surface of the glass, and (iii) the standing wave ratio in free space.

**Answer:**

**Initial Parameter Calculations:**
*   Frequency $f = 200 \text{ MHz} = 2 \times 10^8 \text{ Hz}$
*   Angular frequency $\omega = 2\pi f = 4\pi \times 10^8 \text{ rad/s}$
*   Region 1 (Free Space): $\varepsilon_1 = \varepsilon_0$, $\mu_1 = \mu_0$, $\sigma_1 = 0$
*   Region 2 (Glass): $\varepsilon_{r2} = 4 \implies \varepsilon_2 = 4\varepsilon_0$, $\mu_2 = \mu_0$, $\sigma_2 = 0$ (lossless)

**Wave Parameters for Region 1 (Free Space):**
*   Phase velocity: $u_1 = c \approx 3 \times 10^8 \text{ m/s}$
*   Phase constant: $\beta_1 = \frac{\omega}{u_1} = \frac{4\pi \times 10^8}{3 \times 10^8} = \frac{4\pi}{3} \text{ rad/m}$
*   Intrinsic impedance: $\eta_1 = \eta_0 \approx 120\pi \ \Omega \approx 377 \ \Omega$

**Wave Parameters for Region 2 (Glass):**
*   Phase velocity: $u_2 = \frac{c}{\sqrt{\varepsilon_{r2}\mu_{r2}}} = \frac{3 \times 10^8}{\sqrt{4}} = 1.5 \times 10^8 \text{ m/s}$
*   Phase constant: $\beta_2 = \frac{\omega}{u_2} = \frac{4\pi \times 10^8}{1.5 \times 10^8} = \frac{8\pi}{3} \text{ rad/m}$
*   Intrinsic impedance: $\eta_2 = \sqrt{\frac{\mu_2}{\varepsilon_2}} = \frac{\eta_0}{\sqrt{\varepsilon_{r2}}} = \frac{120\pi}{\sqrt{4}} = 60\pi \ \Omega \approx 188.5 \ \Omega$

**Reflection ($\Gamma$) and Transmission ($\tau$) Coefficients:**
*   $\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} = \frac{60\pi - 120\pi}{60\pi + 120\pi} = \frac{-60\pi}{180\pi} = -\frac{1}{3}$
*   $\tau = \frac{2\eta_2}{\eta_2 + \eta_1} = \frac{2(60\pi)}{60\pi + 120\pi} = \frac{120\pi}{180\pi} = \frac{2}{3}$  (Alternatively, $\tau = 1 + \Gamma = 1 - 1/3 = 2/3$)

**(i) Time-domain forms of the fields:**
Let's assume the wave propagates in the $+z$ direction and the incident electric field is polarized in the $+x$ direction.
*   **Incident Fields (Region 1):**
    $E_{oi} = 1 \text{ V/m}$
    $\vec{E}_i(z,t) = E_{oi} \cos(\omega t - \beta_1 z) \hat{a}_x = \mathbf{\cos\left(4\pi \times 10^8 t - \frac{4\pi}{3}z\right) \hat{a}_x \text{ V/m}}$
    $\vec{H}_i(z,t) = \frac{E_{oi}}{\eta_1} \cos(\omega t - \beta_1 z) \hat{a}_y = \mathbf{\frac{1}{120\pi} \cos\left(4\pi \times 10^8 t - \frac{4\pi}{3}z\right) \hat{a}_y \text{ A/m}}$

*   **Reflected Fields (Region 1):**
    $E_{or} = \Gamma E_{oi} = -\frac{1}{3} (1) = -\frac{1}{3} \text{ V/m}$
    The wave travels in the $-z$ direction.
    $\vec{E}_r(z,t) = E_{or} \cos(\omega t + \beta_1 z) \hat{a}_x = \mathbf{-\frac{1}{3} \cos\left(4\pi \times 10^8 t + \frac{4\pi}{3}z\right) \hat{a}_x \text{ V/m}}$
    For the magnetic field, to maintain $\vec{E} \times \vec{H} = \text{direction of propagation} (-\hat{a}_z)$, the $H$ field must remain in the $+y$ direction (since $\hat{a}_x \times (-\hat{a}_y) = -\hat{a}_z$ but we have a negative E field amplitude, so $-\hat{a}_x \times \hat{a}_y = -\hat{a}_z$). Therefore, $H_{or} = -\frac{E_{or}}{\eta_1} = -\frac{-1/3}{120\pi} = \frac{1}{360\pi}$.
    $\vec{H}_r(z,t) = \mathbf{\frac{1}{360\pi} \cos\left(4\pi \times 10^8 t + \frac{4\pi}{3}z\right) \hat{a}_y \text{ A/m}}$

*   **Transmitted Fields (Region 2):**
    $E_{ot} = \tau E_{oi} = \frac{2}{3} (1) = \frac{2}{3} \text{ V/m}$
    The wave travels in the $+z$ direction.
    $\vec{E}_t(z,t) = E_{ot} \cos(\omega t - \beta_2 z) \hat{a}_x = \mathbf{\frac{2}{3} \cos\left(4\pi \times 10^8 t - \frac{8\pi}{3}z\right) \hat{a}_x \text{ V/m}}$
    $\vec{H}_t(z,t) = \frac{E_{ot}}{\eta_2} \cos(\omega t - \beta_2 z) \hat{a}_y = \frac{2/3}{60\pi} \cos(...) \hat{a}_y = \mathbf{\frac{1}{90\pi} \cos\left(4\pi \times 10^8 t - \frac{8\pi}{3}z\right) \hat{a}_y \text{ A/m}}$

**(ii) Average power transmitted through a $5 \text{ m}^2$ surface of the glass:**
First, calculate the average power density (Poynting vector) of the transmitted wave in Region 2:
$\mathcal{P}_{ave,t} = \frac{1}{2} \frac{|E_{ot}|^2}{\eta_2} = \frac{1}{2} \frac{(2/3)^2}{60\pi} = \frac{1}{2} \frac{4/9}{60\pi} = \frac{4}{1080\pi} = \frac{1}{270\pi} \text{ W/m}^2$

Total average power transmitted ($P_{tr}$) through an area $A = 5 \text{ m}^2$:
$P_{tr} = \mathcal{P}_{ave,t} \times A = \left(\frac{1}{270\pi}\right) \times 5 = \mathbf{\frac{1}{54\pi} \text{ W}}$
*(Numerically, $P_{tr} \approx 0.00589 \text{ W}$ or $5.89 \text{ mW}$)*

**(iii) Standing wave ratio (SWR) in free space:**
The SWR, denoted by $s$, occurs in Region 1 where both incident and reflected waves coexist. It is calculated using the magnitude of the reflection coefficient $\Gamma$:
$s = \frac{1 + |\Gamma|}{1 - |\Gamma|}$
$s = \frac{1 + |-1/3|}{1 - |-1/3|} = \frac{1 + 1/3}{1 - 1/3} = \frac{4/3}{2/3}$
**$s = 2$**

*Related location: Standard Electromagnetics textbooks Chapter on Plane Waves, Section on Reflection of a Plane Wave at Normal Incidence.*

***

### (a) Write the properties of lossless and lossy media. Prove that phase velocity $u_p = 1/\sqrt{\mu\varepsilon}$.

**Answer:**

**Properties of Lossless Media (Perfect Dielectrics):**
1.  Conductivity $\sigma = 0$.
2.  The medium does not dissipate electromagnetic energy (no ohmic losses).
3.  The attenuation constant $\alpha = 0$. Waves propagate without a decrease in amplitude.
4.  The propagation constant is purely imaginary: $\gamma = j\beta$, where the phase constant $\beta = \omega\sqrt{\mu\varepsilon}$.
5.  The intrinsic impedance $\eta = \sqrt{\frac{\mu}{\varepsilon}}$ is a purely real number.
6.  The electric ($\vec{E}$) and magnetic ($\vec{H}$) fields are perfectly in phase with each other.

**Properties of Lossy Media (Imperfect Dielectrics or Conductors):**
1.  Conductivity $\sigma \neq 0$.
2.  The medium dissipates electromagnetic energy as heat due to conduction currents.
3.  The attenuation constant $\alpha > 0$. Wave amplitude decreases exponentially ($e^{-\alpha z}$) as it travels.
4.  The propagation constant is complex: $\gamma = \alpha + j\beta$.
5.  The intrinsic impedance $\eta = |\eta|\angle\theta_\eta$ is a complex number, where the angle $0 < \theta_\eta \le 45^\circ$.
6.  The magnetic field $\vec{H}$ lags the electric field $\vec{E}$ in time by the phase angle $\theta_\eta$.

**Proof that Phase Velocity $u_p = 1/\sqrt{\mu\varepsilon}$ (in a lossless medium):**
Consider a uniform plane wave propagating in the $+z$ direction in a lossless medium. The instantaneous electric field expression is:
$$E(z,t) = E_0 \cos(\omega t - \beta z)$$
The phase of the wave is the argument of the cosine function: $\text{Phase} = \omega t - \beta z$.
The phase velocity ($u_p$) is defined as the velocity at which a point of constant phase travels through space. To find this, we set the phase to a constant value and take the derivative with respect to time $t$:
$$\frac{d}{dt} (\omega t - \beta z) = \frac{d}{dt} (\text{constant})$$
$$\omega - \beta \frac{dz}{dt} = 0$$
Since velocity is the rate of change of distance over time ($u_p = \frac{dz}{dt}$), we solve for $\frac{dz}{dt}$:
$$u_p = \frac{\omega}{\beta}$$
For a lossless medium ($\sigma = 0$), the complex propagation constant $\gamma = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$ reduces to:
$$\gamma = \sqrt{(j\omega\mu)(j\omega\varepsilon)} = \sqrt{j^2\omega^2\mu\varepsilon} = j\omega\sqrt{\mu\varepsilon}$$
Since $\gamma = \alpha + j\beta$ and $\alpha=0$ for a lossless medium, we identify the phase constant as:
$$\beta = \omega\sqrt{\mu\varepsilon}$$
Substitute this expression for $\beta$ back into the phase velocity equation:
$$u_p = \frac{\omega}{\omega\sqrt{\mu\varepsilon}}$$
Canceling $\omega$ yields the final proof:
**$$u_p = \frac{1}{\sqrt{\mu\varepsilon}}$$**

*Related location: Standard Electromagnetics textbooks Chapter on Plane Waves, Sections on Wave Propagation in Lossless Dielectrics.*

***

### (b) Consider a $100 \text{ V/m}$ uniform plane wave of frequency $300 \text{ MHz}$ travelling in an infinite lossless medium having $\sigma = 0$, $\varepsilon_r = 9$ and $\mu_r = 1$. Write complete time domain expressions for the field vectors of the forward travelling wave and determine the average power density vector.

**Answer:**

**1. Identify Parameters:**
*   Amplitude $E_0 = 100 \text{ V/m}$
*   Frequency $f = 300 \text{ MHz} = 3 \times 10^8 \text{ Hz}$
*   Angular frequency $\omega = 2\pi f = 2\pi \times (3 \times 10^8) = 6\pi \times 10^8 \text{ rad/s}$
*   Lossless medium: $\sigma = 0 \implies \alpha = 0$
*   Relative permittivity $\varepsilon_r = 9$
*   Relative permeability $\mu_r = 1 \implies \mu = \mu_0 = 4\pi \times 10^{-7} \text{ H/m}$

**2. Calculate Wave Constants:**
*   Phase velocity ($u_p$):
    $u_p = \frac{c}{\sqrt{\mu_r \varepsilon_r}} = \frac{3 \times 10^8}{\sqrt{(1)(9)}} = \frac{3 \times 10^8}{3} = 10^8 \text{ m/s}$
*   Phase constant ($\beta$):
    $\beta = \frac{\omega}{u_p} = \frac{6\pi \times 10^8}{10^8} = 6\pi \text{ rad/m}$
*   Intrinsic impedance ($\eta$):
    $\eta = \sqrt{\frac{\mu}{\varepsilon}} = \frac{\eta_0}{\sqrt{\varepsilon_r}} \approx \frac{120\pi}{\sqrt{9}} = \frac{120\pi}{3} = 40\pi \ \Omega$ (approx. $125.66 \ \Omega$)

**3. Time Domain Expressions for Field Vectors:**
Assume the "forward travelling wave" propagates in the $+z$ direction and the electric field is polarized in the $+x$ direction.
*   **Electric Field ($\vec{E}$):**
    $\vec{E}(z,t) = E_0 \cos(\omega t - \beta z) \hat{a}_x$
    **$\vec{E}(z,t) = 100 \cos(6\pi \times 10^8 t - 6\pi z) \hat{a}_x \text{ V/m}$**
*   **Magnetic Field ($\vec{H}$):**
    The magnitude is $H_0 = \frac{E_0}{\eta} = \frac{100}{40\pi} = \frac{2.5}{\pi} \text{ A/m}$.
    To ensure wave propagation in $+z$ ($\hat{a}_z$) given $\vec{E}$ is in $+x$ ($\hat{a}_x$), $\vec{H}$ must be in $+y$ ($\hat{a}_y$) because $\hat{a}_x \times \hat{a}_y = \hat{a}_z$.
    $\vec{H}(z,t) = \frac{E_0}{\eta} \cos(\omega t - \beta z) \hat{a}_y$
    **$\vec{H}(z,t) = \frac{2.5}{\pi} \cos(6\pi \times 10^8 t - 6\pi z) \hat{a}_y \text{ A/m}$**
    *(Numerically: $\approx 0.796 \cos(6\pi \times 10^8 t - 6\pi z) \hat{a}_y \text{ A/m}$)*

**4. Determine the Average Power Density Vector ($\vec{\mathcal{P}}_{ave}$):**
For a lossless medium, the average power density is calculated as:
$$\vec{\mathcal{P}}_{ave} = \frac{E_0^2}{2\eta} \hat{a}_k$$
where $\hat{a}_k = \hat{a}_z$.
$$\vec{\mathcal{P}}_{ave} = \frac{(100)^2}{2(40\pi)} \hat{a}_z$$
$$\vec{\mathcal{P}}_{ave} = \frac{10000}{80\pi} \hat{a}_z = \frac{125}{\pi} \hat{a}_z \text{ W/m}^2$$
**$\vec{\mathcal{P}}_{ave} \approx 39.79 \hat{a}_z \text{ W/m}^2$**

*Related location: Standard Electromagnetics textbooks Chapter on Plane Waves, Section on Plane Waves in Lossless Dielectrics and Power/Poynting Vector.*
### up untill 2013
