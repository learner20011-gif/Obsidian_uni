### (c) State how the propagation of EM-wave through a waveguide differs from that of through free space.

The propagation of an electromagnetic (EM) wave through a waveguide differs from propagation through free space in several fundamental ways:

*   **Mode of Propagation (Field Configuration):** In free space, an EM wave propagates as a Transverse Electromagnetic (TEM) wave, meaning both the electric field (E) and magnetic field (H) are completely perpendicular (transverse) to the direction of wave propagation and to each other. However, a hollow waveguide cannot support TEM modes. Instead, it supports Transverse Electric (TE) modes (where the E-field is entirely transverse, but the H-field has a component in the direction of propagation) and Transverse Magnetic (TM) modes (where the H-field is entirely transverse, but the E-field has a component in the direction of propagation). 
*   **Frequency Response (High-Pass Filter):** Free space allows the propagation of EM waves at all frequencies (from DC to infinity). A waveguide, on the other hand, acts as a high-pass filter. It will only allow the propagation of waves that have a frequency above a specific minimum threshold called the **cutoff frequency ($f_c$)**. Waves with frequencies below this cutoff are rapidly attenuated and do not propagate (these are known as evanescent modes).
*   **Velocities:** In free space, the energy of the wave and its phase fronts travel at the exact same speed (the speed of light, $c$). Inside a waveguide, the wave bounces in a zigzag path off the conducting walls. As a result, the phase velocity ($u_p$) is actually *greater* than the speed of light, while the group velocity ($u_g$, the speed at which energy and information travel) is *less* than the speed of light.

*Related location in provided documents: Presentation PDF Pages 283, 450-451, 468-469, 481, 528.*

***

### (a) Establish the relationship between the group velocity and phase velocity of EM wave propagating through a rectangular waveguide.

When an EM wave propagates through a rectangular waveguide, it does so by reflecting off the inner walls in a zigzag pattern. Because of this behavior, two distinct velocities are defined:
1.  **Phase Velocity ($u_p$):** The velocity at which the loci of constant phase propagate down the guide. 
2.  **Group Velocity ($u_g$):** The velocity at which the actual signal energy (or wave-packet envelope) propagates down the guide. 

The phase velocity is defined mathematically as:
$u_p = \frac{u'}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$

The group velocity is defined mathematically as:
$u_g = u' \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$

Where:
*   $u'$ is the velocity of the wave in the unbounded dielectric medium filling the waveguide ($u' = \frac{1}{\sqrt{\mu\epsilon}}$). If the waveguide is hollow/air-filled, $u' = c$ (the speed of light in a vacuum).
*   $f_c$ is the cutoff frequency for the specific propagating mode.
*   $f$ is the operating frequency.

To establish the relationship between them, we simply multiply the phase velocity by the group velocity:
$u_p \cdot u_g = \left[ \frac{u'}{\sqrt{1 - (f_c/f)^2}} \right] \cdot \left[ u' \sqrt{1 - (f_c/f)^2} \right]$

The square root terms in the numerator and denominator cancel each other out, leaving:
**$u_p \cdot u_g = (u')^2$**

For a hollow (air-filled) rectangular waveguide where $u' = c$, the relationship simplifies to:
**$u_p \cdot u_g = c^2$**

This relationship mathematically proves that since the group velocity ($u_g$) must always be less than the speed of light, the phase velocity ($u_p$) must mathematically be greater than the speed of light to satisfy the equation. 

*Related location in provided documents: Presentation PDF Pages 527-530.*

***

### (b) A rectangular waveguide of dimension 2.5cm $\times$ 1.5cm working in TE mode at 7.5 GHz. Calculate phase constant, $\beta$, phase velocity, $u_p$, group velocity, $u_g$ and $Z_{TE10}$ if the waveguide is hollow.

**1. Identify the given parameters:**
*   Dimensions: $a = 2.5 \text{ cm} = 0.025 \text{ m}$, $b = 1.5 \text{ cm} = 0.015 \text{ m}$
*   Operating frequency: $f = 7.5 \text{ GHz} = 7.5 \times 10^9 \text{ Hz}$
*   Mode: $\text{TE}_{10}$ (derived from the question asking for $Z_{TE10}$, meaning $m=1, n=0$)
*   Medium: Hollow (air-filled), so $\mu = \mu_0, \epsilon = \epsilon_0$. 
    *   Speed of light $u' = c = 3 \times 10^8 \text{ m/s}$
    *   Intrinsic impedance of free space $\eta' = \eta_0 \approx 120\pi \, \Omega \approx 377 \, \Omega$

**2. Calculate the Cutoff Frequency ($f_c$) for the $\text{TE}_{10}$ mode:**
The formula for the cutoff frequency of the dominant $\text{TE}_{10}$ mode is:
$f_{c_{10}} = \frac{u'}{2a} = \frac{c}{2a}$
$f_{c_{10}} = \frac{3 \times 10^8}{2 \times 0.025} = \frac{3 \times 10^8}{0.05} = 60 \times 10^8 \text{ Hz} = 6.0 \text{ GHz}$

Next, we find the ratio of cutoff frequency to operating frequency, which will be used in subsequent formulas:
$\frac{f_c}{f} = \frac{6.0 \text{ GHz}}{7.5 \text{ GHz}} = 0.8$
The scale factor used in the formulas is: $\sqrt{1 - \left(\frac{f_c}{f}\right)^2} = \sqrt{1 - (0.8)^2} = \sqrt{1 - 0.64} = \sqrt{0.36} = 0.6$

**3. Calculate the Phase Constant ($\beta$):**
First, find the angular frequency $\omega$:
$\omega = 2\pi f = 2\pi \times (7.5 \times 10^9) = 15\pi \times 10^9 \text{ rad/s}$
The phase constant formula is:
$\beta = \frac{\omega}{c} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$
$\beta = \frac{15\pi \times 10^9}{3 \times 10^8} \times 0.6 = 50\pi \times 0.6 = 30\pi \text{ rad/m}$
**$\beta \approx 94.25 \text{ rad/m}$**

**4. Calculate the Phase Velocity ($u_p$):**
$u_p = \frac{c}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}} = \frac{3 \times 10^8}{0.6}$
**$u_p = 5.0 \times 10^8 \text{ m/s}$**

**5. Calculate the Group Velocity ($u_g$):**
$u_g = c \sqrt{1 - \left(\frac{f_c}{f}\right)^2} = (3 \times 10^8) \times 0.6$
**$u_g = 1.8 \times 10^8 \text{ m/s}$**

**6. Calculate the Wave Impedance ($Z_{TE10}$ or $\eta_{TE10}$):**
$\eta_{TE} = \frac{\eta'}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}} = \frac{120\pi}{0.6}$
$\eta_{TE} = 200\pi \, \Omega$
**$Z_{TE10} \approx 628.32 \, \Omega$**

*Related location in provided documents: Presentation PDF Pages 484, 495, 498, 527, 529.*
### Justification of why the TEM mode does not exist in a waveguide

**Mathematical Explanation:**

A Transverse Electromagnetic (TEM) mode is characterized by both the electric field ($E$) and magnetic field ($H$) being entirely transverse (perpendicular) to the direction of wave propagation. If we assume the wave propagates in the $z$-direction, this means there are no longitudinal components: $E_z = 0$ and $H_z = 0$.

In a rectangular waveguide, the behavior of the fields is governed by the wave equations derived from Maxwell's equations. By expressing the transverse field components ($E_x, E_y, H_x, H_y$) in terms of the longitudinal components ($E_z, H_z$), we arrive at a set of standard waveguide equations. 

For instance, the transverse electric field in the $x$-direction ($E_{xs}$) is related to the longitudinal components by the equation:
$$E_{xs} = -\frac{\gamma}{h^2} \frac{\partial E_{zs}}{\partial x} - \frac{j\omega\mu}{h^2} \frac{\partial H_{zs}}{\partial y}$$

Where:
*   $\gamma$ is the propagation constant.
*   $h^2 = \gamma^2 + k^2$ (where $k = \omega\sqrt{\mu\epsilon}$ is the wave number).

If we assume a TEM mode exists, we must set $E_{zs} = 0$ and $H_{zs} = 0$. Looking at the equation above, if the derivatives of zero are taken, the entire right side of the equation becomes zero. Consequently, $E_{xs} = 0$. 

By applying this same logic to the equations for $E_{ys}, H_{xs},$ and $H_{ys}$, all transverse components are also forced to be zero. The only condition where this might not immediately force all fields to zero is if the denominator $h^2 = 0$. 

However, if $h^2 = 0$, then $\gamma^2 + k^2 = 0$, which implies $\gamma = j\beta = \pm jk$. This is the propagation constant for a uniform plane wave traveling in unbounded free space, not a wave constrained within the metallic boundaries of a hollow waveguide. In order to satisfy the boundary conditions at the conducting walls (where the tangential $E$-field must be zero), the fields must have spatial variations in the $x$ and $y$ directions, making it impossible for $h^2$ to be zero.

Therefore, because setting $E_z = 0$ and $H_z = 0$ forces all other field components to vanish completely, a hollow rectangular waveguide cannot support a TEM mode. It can only support Transverse Electric (TE, where $E_z = 0$ but $H_z \neq 0$) or Transverse Magnetic (TM, where $H_z = 0$ but $E_z \neq 0$) modes.

*Related location in provided documents: Pages 466, 467, and 468.*

***

### Comprehensive Explanation of Waveguides, High-Pass Filtering, Maxwell's Equations, Boundary Conditions, and Cutoff Frequency

**1. What is a Waveguide?**
A waveguide is a structure, typically a hollow metallic tube of uniform cross-section (such as rectangular or circular), used to guide electromagnetic waves at high frequencies (generally in the microwave range of 3 GHz to 300 GHz). Unlike standard two-wire transmission lines that support TEM waves and can operate down to DC (0 Hz), waveguides support TE and TM field configurations to obtain larger bandwidths and lower signal attenuation at high frequencies.

**2. Maxwell's Equations for an Air-Filled Hollow Rectangular Waveguide**
Assuming a source-free region inside the hollow waveguide (volume charge density $\rho_v = 0$ and current density $J = 0$), and a lossless air-filled dielectric ($\sigma = 0, \mu = \mu_0, \epsilon = \epsilon_0$), Maxwell's equations in phasor form reduce to the vector Helmholtz equations:
$$\nabla^2 \mathbf{E}_s + k^2 \mathbf{E}_s = 0$$
$$\nabla^2 \mathbf{H}_s + k^2 \mathbf{H}_s = 0$$
where $k = \omega\sqrt{\mu_0\epsilon_0}$ is the wave number.

**3. Corresponding Boundary Conditions**
The walls of the waveguide are assumed to be perfect conductors ($\sigma_c = \infty$). The fundamental boundary condition is that the tangential components of the electric field must be zero at the conductor walls. For a rectangular waveguide with dimensions $a$ (width along x-axis) and $b$ (height along y-axis):
*   $E_x = 0$ at $y = 0$ and $y = b$ (top and bottom walls)
*   $E_y = 0$ at $x = 0$ and $x = a$ (side walls)
*   $E_z = 0$ at $x = 0, a$ and $y = 0, b$ (all walls)
For the magnetic field, the normal derivative evaluated at the boundary surface must be zero (e.g., $\frac{\partial H_z}{\partial x} = 0$ at $x=0, a$).

**4. How and Why a Waveguide Acts as a High-Pass Filter**
A waveguide acts as a high-pass filter because it only permits the propagation of electromagnetic waves whose frequencies are strictly above a certain threshold, known as the **cutoff frequency ($f_c$)**. 
When solving the wave equation using separation of variables and applying the boundary conditions, a separation constant $h^2$ emerges, defined as:
$$h^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$
We also know that $h^2$ is related to the propagation constant $\gamma$ and the wave number $k$ by:
$$h^2 = \gamma^2 + k^2 \implies \gamma^2 = h^2 - k^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 - \omega^2\mu\epsilon$$

The propagation constant is complex: $\gamma = \alpha + j\beta$. 
*   If the operating frequency $f$ is low, $\omega^2\mu\epsilon$ is small, making $\gamma^2$ positive. Therefore, $\gamma$ is purely real ($\gamma = \alpha$). This means the wave attenuates exponentially without phase progression; it does not propagate. This is called an **evanescent mode**.
*   As frequency increases, $\omega^2\mu\epsilon$ gets larger. When it exceeds $h^2$, $\gamma^2$ becomes negative, making $\gamma$ purely imaginary ($\gamma = j\beta$). Here, attenuation $\alpha = 0$, and the wave propagates freely down the guide.
Because propagation only occurs above the specific frequency that causes $\gamma$ to transition from real to imaginary, the waveguide blocks low frequencies (including DC) and passes high frequencies, acting perfectly as a high-pass filter.

**5. Derivation of the Cutoff Frequency ($f_c$) Equation**
The cutoff condition occurs exactly at the boundary between attenuation and propagation, which is when $\gamma = 0$. Setting the propagation constant equation to zero:
$$0 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 - \omega_c^2\mu\epsilon$$
Rearranging to solve for the cutoff angular frequency $\omega_c$:
$$\omega_c^2\mu\epsilon = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$
$$\omega_c = \frac{1}{\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$
Since $\omega_c = 2\pi f_c$ and the velocity of the wave in the unbounded medium is $u' = \frac{1}{\sqrt{\mu\epsilon}}$ (which equals $c$ for an air-filled guide):
$$2\pi f_c = u' \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$
$$f_c = \frac{u'}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**6. Meaning of the Subscripts $m$ and $n$**
In the mode designations $\text{TE}_{mn}$ and $\text{TM}_{mn}$, the subscripts $m$ and $n$ are integers that dictate the specific field pattern (mode) inside the waveguide. 
*   **$m$** represents the number of half-cycle variations of the electric or magnetic field intensity along the $x$-direction (the width $a$).
*   **$n$** represents the number of half-cycle variations of the field intensity along the $y$-direction (the height $b$).

*Related location in provided documents: Pages 450, 451, 454, 467-471, 475-478, 481, 482, 489, 490.*

***

### Obtain the cutoff frequency and phase velocity for the dominant mode in a 2.3 cm x 1.0 cm rectangular waveguide at 10 GHz.

**1. Identify Parameters and Dominant Mode:**
*   Width $a = 2.3 \text{ cm} = 0.023 \text{ m}$
*   Height $b = 1.0 \text{ cm} = 0.010 \text{ m}$
*   Operating frequency $f = 10 \text{ GHz} = 10 \times 10^9 \text{ Hz}$
*   Medium: Assuming air-filled (standard unless specified), so the speed of light $c = 3 \times 10^8 \text{ m/s}$.
*   **Dominant Mode:** The dominant mode in a rectangular waveguide where $a > b$ is the mode with the lowest cutoff frequency, which is always the **$\text{TE}_{10}$ mode**. Therefore, $m=1$ and $n=0$.

**2. Calculate the Cutoff Frequency ($f_c$):**
Using the general cutoff frequency equation for the $\text{TE}_{10}$ mode ($m=1, n=0$):
$$f_{c_{10}} = \frac{c}{2} \sqrt{\left(\frac{1}{a}\right)^2 + \left(\frac{0}{b}\right)^2} = \frac{c}{2a}$$
$$f_{c_{10}} = \frac{3 \times 10^8 \text{ m/s}}{2 \times 0.023 \text{ m}}$$
$$f_{c_{10}} = \frac{3 \times 10^8}{0.046}$$
**$f_c = 6.52 \times 10^9 \text{ Hz} = 6.52 \text{ GHz}$**

*(Note: Because the operating frequency of 10 GHz is strictly greater than the cutoff frequency of 6.52 GHz, the wave will successfully propagate).*

**3. Calculate the Phase Velocity ($u_p$):**
The phase velocity formula in a waveguide is:
$$u_p = \frac{c}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

First, find the ratio of cutoff frequency to operating frequency:
$$\frac{f_c}{f} = \frac{6.52 \text{ GHz}}{10 \text{ GHz}} = 0.652$$

Next, calculate the denominator scaling factor:
$$\sqrt{1 - (0.652)^2} = \sqrt{1 - 0.4251} = \sqrt{0.5749} \approx 0.7582$$

Now, calculate $u_p$:
$$u_p = \frac{3 \times 10^8 \text{ m/s}}{0.7582}$$
**$u_p \approx 3.957 \times 10^8 \text{ m/s}$**

*Related location in provided documents: Pages 482, 484, 494, 495, 497.*

### Define waveguide. What is meant by dominant mode in a waveguide?

**Definition of a Waveguide:**
A waveguide is a structure utilized for guiding electromagnetic (EM) waves at high frequencies (typically in the microwave range of roughly 3 to 300 GHz). It differs from a standard transmission line in that a transmission line supports only transverse electromagnetic (TEM) waves and can operate down to DC (0 Hz). In contrast, a waveguide cannot transmit DC and acts as a high-pass filter, operating only above a certain cutoff frequency. Furthermore, a waveguide can support many possible field configurations, specifically Transverse Electric (TE) and Transverse Magnetic (TM) modes.

**Dominant Mode:**
The dominant mode of a waveguide is defined as the specific mode of propagation that possesses the lowest cutoff frequency (or equivalently, the longest cutoff wavelength). Because the waveguide acts as a high-pass filter, this is the very first mode that is able to propagate as the frequency of the source is increased from zero. For a standard rectangular waveguide where the width dimension is greater than the height ($a > b$), the dominant mode is the $\text{TE}_{10}$ mode.

*Related location in provided documents: Pages 450, 451, 487, 495, 497.*

***

### Derive the equation for electric field $E_z$ in a rectangular waveguide of dimension a x b.

To derive the equation for the longitudinal electric field $E_z$ in a rectangular waveguide (specifically for Transverse Magnetic or TM modes, since $E_z = 0$ for TE modes), we start with the wave equation (Helmholtz equation) in a source-free, lossless dielectric medium inside the waveguide walls:
$$\nabla^2 \mathbf{E}_s + k^2 \mathbf{E}_s = 0$$

For the $z$-component, this partial differential equation becomes:
$$\frac{\partial^2 E_{zs}}{\partial x^2} + \frac{\partial^2 E_{zs}}{\partial y^2} + \frac{\partial^2 E_{zs}}{\partial z^2} + k^2 E_{zs} = 0$$

To solve this, we use the method of separation of variables. We assume the solution can be written as a product of three independent functions:
$$E_{zs}(x, y, z) = X(x) Y(y) Z(z)$$

Substituting this back into the differential equation and dividing the entire equation by $XYZ$ yields:
$$\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} = -k^2$$

Since the variables are independent, each term must be equal to a constant. We define the separation constants as $-k_x^2$, $-k_y^2$, and $\gamma^2$, giving the relation:
$$-k_x^2 - k_y^2 + \gamma^2 = -k^2$$
*(Note: the text defines $h^2 = \gamma^2 + k^2 = k_x^2 + k_y^2$)*

This separates the problem into three ordinary differential equations:
1. $X'' + k_x^2X = 0$
2. $Y'' + k_y^2Y = 0$
3. $Z'' - \gamma^2Z = 0$

The general solutions to these differential equations are:
$$X(x) = c_1 \cos(k_x x) + c_2 \sin(k_x x)$$
$$Y(y) = c_3 \cos(k_y y) + c_4 \sin(k_y y)$$
$$Z(z) = c_5 e^{\gamma z} + c_6 e^{-\gamma z}$$

Assuming the wave propagates in the $+z$ direction, the field must be finite at infinity, which requires $c_5 = 0$. Therefore, $Z(z)$ is proportional to $e^{-\gamma z}$.

Next, we apply the boundary conditions for a rectangular waveguide with perfectly conducting walls. The tangential component of the electric field ($E_{zs}$) must be zero at the walls:
1.  **At $x = 0$, $E_{zs} = 0$**: This requires $c_1 = 0$, leaving $X(x) = c_2 \sin(k_x x)$.
2.  **At $x = a$, $E_{zs} = 0$**: This requires $\sin(k_x a) = 0$, which means $k_x a = m\pi$, or $k_x = \frac{m\pi}{a}$ (where $m = 1, 2, 3...$).
3.  **At $y = 0$, $E_{zs} = 0$**: This requires $c_3 = 0$, leaving $Y(y) = c_4 \sin(k_y y)$.
4.  **At $y = b$, $E_{zs} = 0$**: This requires $\sin(k_y b) = 0$, which means $k_y b = n\pi$, or $k_y = \frac{n\pi}{b}$ (where $n = 1, 2, 3...$).

Combining the remaining constants ($c_2, c_4, c_6$) into a single amplitude constant $E_o$, and substituting $k_x$ and $k_y$ back into the product solution, we arrive at the final derived equation for the $E_z$ field:
$$E_{zs} = E_o \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}$$

*Related location in provided documents: Pages 454-460, 471-473.*

***

### What are the meanings of the subscripts m and n, used in the definition of the propagating waves TEmn and TMmn in waveguide.

The subscripts $m$ and $n$ used in mode designations like $\text{TE}_{mn}$ and $\text{TM}_{mn}$ are integers that dictate the specific field pattern (or configuration) inside the waveguide. 

Specifically, they denote the number of half-cycle variations of the electromagnetic field components in the transverse cross-section of the guide:
*   **Integer $m$** represents the number of half-cycle variations of the field along the $x$-direction (which corresponds to the width dimension '$a$' of the waveguide).
*   **Integer $n$** represents the number of half-cycle variations of the field along the $y$-direction (which corresponds to the height dimension '$b$' of the waveguide).

Each unique combination of $m$ and $n$ creates a distinct spatial field pattern, and each of these patterns has its own specific cutoff frequency. 

*Related location in provided documents: Pages 467, 475, 476, 486, 494.*

***

### Show that the wave impedance of propagating TM modes in a waveguide with a lossless dielectric is purely resistive and is always less than the intrinsic impedance of the dielectric medium.

By definition, the intrinsic wave impedance of the TM mode ($\eta_{\text{TM}}$) is the ratio of the transverse electric field to the transverse magnetic field:
$$\eta_{\text{TM}} = \frac{E_x}{H_y} = -\frac{E_y}{H_x}$$

From the standard derivation of TM field components in a waveguide, this ratio evaluates mathematically to:
$$\eta_{\text{TM}} = \frac{\beta}{\omega\epsilon}$$
Where $\beta$ is the phase constant, $\omega$ is the angular frequency, and $\epsilon$ is the permittivity of the medium.

For a propagating wave in a lossless medium, the phase constant $\beta$ is defined as:
$$\beta = \omega\sqrt{\mu\epsilon} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

Substituting this expression for $\beta$ into the impedance equation yields:
$$\eta_{\text{TM}} = \frac{\omega\sqrt{\mu\epsilon}\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}{\omega\epsilon}$$

The $\omega$ terms cancel out. Recognizing that $\frac{\sqrt{\mu\epsilon}}{\epsilon} = \sqrt{\frac{\mu}{\epsilon}}$, the equation becomes:
$$\eta_{\text{TM}} = \sqrt{\frac{\mu}{\epsilon}} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

We know that the intrinsic impedance of the unbounded uniform plane wave in the dielectric medium is $\eta' = \sqrt{\frac{\mu}{\epsilon}}$. Substituting this in gives the final relation:
$$\eta_{\text{TM}} = \eta' \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

**Proof that it is purely resistive:**
For a mode to be "propagating," the operating frequency $f$ must be strictly greater than the cutoff frequency $f_c$ (i.e., $f > f_c$). Because $f > f_c$, the ratio $(f_c/f)$ is less than 1, and the term under the square root $\left(1 - (f_c/f)^2\right)$ is positive. Therefore, the square root yields a purely real number. Since $\eta'$ for a lossless dielectric is also a real number, $\eta_{\text{TM}}$ is purely real, meaning it is purely resistive.

**Proof that it is always less than the intrinsic impedance ($\eta'$):**
As established above, for a propagating wave, the fraction $(f_c/f)$ is less than 1. Consequently, the entire square root multiplier $\sqrt{1 - (f_c/f)^2}$ evaluates to a decimal value strictly greater than 0 but less than 1. Multiplying the medium's intrinsic impedance $\eta'$ by a value less than 1 mathematically guarantees that $\eta_{\text{TM}}$ will always be less than $\eta'$.

*Related location in provided documents: Pages 484, 486, 499.*

***

### What are the differences between group velocity and phase velocity? Explain with suitable examples.

When electromagnetic waves propagate through a waveguide, the waves reflect off the conducting walls in a zigzag path. Because the wave does not travel straight down the guide, two distinct velocities must be defined to describe the wave's behavior:

**1. Phase Velocity ($u_p$):**
*   **Definition:** The phase velocity is the velocity at which loci of constant phase are propagated down the guide. 
*   **Mathematical Formula:** It is calculated as $u_p = \frac{\omega}{\beta}$. In relation to the medium's unbounded velocity ($u' = \frac{1}{\sqrt{\mu\epsilon}}$), it is given by $u_p = \frac{u'}{\sqrt{1 - (f_c/f)^2}}$.
*   **Characteristics:** Because the denominator is a fraction less than 1 for propagating waves, the phase velocity is always *greater* than the speed of light in that medium ($u_p \geq u'$). If the waveguide is filled with a vacuum, the phase velocity actually exceeds the speed of light ($c$).

**2. Group Velocity ($u_g$):**
*   **Definition:** The group velocity is the velocity with which the resultant repeated reflected waves travel down the guide. It represents the velocity of propagation of the "wave-packet envelope" formed by a group of frequencies. Most importantly, it is the velocity at which actual energy and information travel through the waveguide.
*   **Mathematical Formula:** It is calculated as $u_g = \frac{1}{\partial\beta/\partial\omega}$. In relation to the medium's velocity, it is given by $u_g = u' \sqrt{1 - (f_c/f)^2}$.
*   **Characteristics:** Because it is multiplied by a fraction less than 1, the group velocity is always *less* than or equal to the speed of light in the medium ($u_g \leq u'$).

**Explanation and Example:**
The relationship between the two is established by the equation $u_p u_g = (u')^2$. 

A suitable way to conceptualize the difference is to imagine the decomposition of the waveguide mode into two plane waves traveling in zigzag paths (as illustrated in the text's geometric decompositions). The *group velocity* represents the actual forward progress of the physical wave packet (the energy) bouncing down the tube. Because it takes an angled, bouncing path rather than a straight line, its forward velocity ($u_g$) is slower than the speed of light. 

Conversely, the *phase velocity* tracks the intersection point of the wave's phase fronts along the waveguide wall. Because of the angle of intersection, this geometric point of constant phase moves faster than the wave itself, exceeding the speed of light. The text explicitly notes that $u_p > c$ does *not* violate Einstein's theory of relativity because information and energy do not travel at the phase velocity; they travel at the slower group velocity.

*Related location in provided documents: Pages 526-530.*
### Compare waveguide with transmission lines regarding wave propagation and frequency limitations.

Waveguides and transmission lines are both used to guide electromagnetic energy from one point to another, but they have fundamental differences in their wave propagation modes, operating frequencies, and physical characteristics:

**1. Wave Propagation Modes:**
*   **Transmission Lines:** A standard transmission line (like a coaxial cable or two-wire line) typically consists of two or more conductors. It supports **Transverse Electromagnetic (TEM)** waves, where both the electric ($E$) and magnetic ($H$) fields are entirely perpendicular to the direction of propagation.
*   **Waveguides:** A waveguide is typically a single hollow metallic tube. It cannot support TEM waves because the continuous conducting walls would force the tangential electric field to zero everywhere, making the entire field vanish. Instead, waveguides support **Transverse Electric (TE)** modes (where the $E$-field is purely transverse, but the $H$-field has a longitudinal component) and **Transverse Magnetic (TM)** modes (where the $H$-field is purely transverse, but the $E$-field has a longitudinal component).

**2. Frequency Limitations:**
*   **Transmission Lines:** Transmission lines can theoretically operate from **DC ($f = 0$) up to very high frequencies**. However, at microwave frequencies (roughly 3 GHz to 300 GHz), transmission lines become highly inefficient due to severe skin effect (increased ohmic resistance) and dielectric losses.
*   **Waveguides:** Waveguides act as **high-pass filters**. They cannot transmit DC or low-frequency signals. They will only allow wave propagation above a specific threshold known as the **cutoff frequency ($f_c$)**, which is dictated by the waveguide's physical dimensions. Below this cutoff frequency, the waves are rapidly attenuated (evanescent). Waveguides are preferred at microwave frequencies because they offer much lower signal attenuation, larger bandwidth, and higher power-handling capacity compared to transmission lines.

*Related location in provided documents: Pages 450, 451, 468, 469, 481.*

***

### Starting from the propagation constant determine the phase and group velocities, $u_p$ and $u_g$ of electromagnetic wave in a rectangular waveguide and hence show that $u_p u_g = c^2$.

The propagation constant $\gamma$ for an electromagnetic wave in a waveguide is given by:
$$\gamma = \alpha + j\beta$$
For a propagating wave in a lossless medium, the attenuation constant $\alpha = 0$, so $\gamma = j\beta$. The phase constant $\beta$ is defined from the separation equation $k^2 = h^2 + \beta^2$, which gives:
$$\beta = \sqrt{k^2 - h^2}$$
Where $k = \omega\sqrt{\mu\epsilon}$ is the wave number of the unbounded medium, and $h$ is the cutoff wavenumber $h = \omega_c\sqrt{\mu\epsilon}$. Substituting these in:
$$\beta = \sqrt{\omega^2\mu\epsilon - \omega_c^2\mu\epsilon} = \omega\sqrt{\mu\epsilon} \sqrt{1 - \left(\frac{\omega_c}{\omega}\right)^2}$$
Since $f_c/f = \omega_c/\omega$ and the velocity in the unbounded medium is $u' = \frac{1}{\sqrt{\mu\epsilon}}$, we can write:
$$\beta = \frac{\omega}{u'} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$
To simplify the derivative later, let's write it as: $\beta = \frac{1}{u'} \sqrt{\omega^2 - \omega_c^2}$

**1. Phase Velocity ($u_p$):**
Phase velocity is the speed at which points of constant phase travel. It is defined as $u_p = \frac{\omega}{\beta}$.
$$u_p = \frac{\omega}{\frac{\omega}{u'} \sqrt{1 - (f_c/f)^2}}$$
$$u_p = \frac{u'}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

**2. Group Velocity ($u_g$):**
Group velocity is the speed at which the wave envelope (and therefore energy and information) travels. It is defined as $u_g = \frac{d\omega}{d\beta}$, or equivalently $\left( \frac{d\beta}{d\omega} \right)^{-1}$.
Using $\beta = \frac{1}{u'} \sqrt{\omega^2 - \omega_c^2}$:
$$\frac{d\beta}{d\omega} = \frac{1}{u'} \cdot \frac{1}{2\sqrt{\omega^2 - \omega_c^2}} \cdot 2\omega = \frac{1}{u'} \frac{\omega}{\sqrt{\omega^2 - \omega_c^2}}$$
Divide numerator and denominator by $\omega$:
$$\frac{d\beta}{d\omega} = \frac{1}{u'} \frac{1}{\sqrt{1 - (\omega_c/\omega)^2}} = \frac{1}{u'} \frac{1}{\sqrt{1 - (f_c/f)^2}}$$
Therefore, taking the reciprocal:
$$u_g = \frac{d\omega}{d\beta} = u' \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

**3. Showing $u_p u_g = c^2$:**
Now, we multiply the expressions for phase and group velocity:
$$u_p \cdot u_g = \left[ \frac{u'}{\sqrt{1 - (f_c/f)^2}} \right] \cdot \left[ u' \sqrt{1 - (f_c/f)^2} \right]$$
The square root terms cancel out, leaving:
$$u_p \cdot u_g = (u')^2$$
For an air-filled (or vacuum) waveguide, the velocity of the unbounded medium $u' = \frac{1}{\sqrt{\mu_0\epsilon_0}} = c$ (the speed of light). Therefore:
$$u_p \cdot u_g = c^2$$

*Related location in provided documents: Pages 484, 527-530.*

***

### Show that $\frac{1}{\lambda^2} = \frac{1}{\lambda_g^2} + \frac{1}{\lambda_c^2}$ , where the symbols have their usual meaning.

In waveguide theory, the solution to the wave equation yields a relationship between the wave numbers in different directions. Let's define the symbols first:
*   $\lambda$ = wavelength of a uniform plane wave in the unbounded medium ($\lambda = u'/f$).
*   $\lambda_g$ = waveguide wavelength, which is the distance required to effect a phase change of $2\pi$ radians along the guide axis ($\lambda_g = 2\pi/\beta$).
*   $\lambda_c$ = cutoff wavelength, the maximum wavelength that can propagate in a specific mode ($\lambda_c = u'/f_c$).

From the separation of variables in the Helmholtz wave equation, we obtain the relationship between the propagation constant $\gamma$, the wave number $k$, and the separation constants $k_x$ and $k_y$:
$$-k_x^2 - k_y^2 + \gamma^2 = -k^2$$
Letting the transverse wave number be $h^2 = k_x^2 + k_y^2$, we get:
$$-h^2 + \gamma^2 = -k^2 \implies k^2 = h^2 - \gamma^2$$
For a propagating wave, the attenuation constant is zero ($\alpha = 0$), so $\gamma = j\beta$. Substituting this gives:
$$k^2 = h^2 - (j\beta)^2$$
$$k^2 = h^2 + \beta^2$$
Now, we express each of these wave numbers in terms of their corresponding wavelengths:
1.  **Free-space wave number:** $k = \frac{2\pi}{\lambda}$
2.  **Cutoff wave number:** $h = k_c = \frac{2\pi}{\lambda_c}$
3.  **Phase constant (longitudinal wave number):** $\beta = \frac{2\pi}{\lambda_g}$

Substitute these wavelength expressions into the main equation $k^2 = h^2 + \beta^2$:
$$\left(\frac{2\pi}{\lambda}\right)^2 = \left(\frac{2\pi}{\lambda_c}\right)^2 + \left(\frac{2\pi}{\lambda_g}\right)^2$$
Divide the entire equation by $(2\pi)^2$:
$$\frac{1}{\lambda^2} = \frac{1}{\lambda_c^2} + \frac{1}{\lambda_g^2}$$
Rearranging to match the required format:
$$\frac{1}{\lambda^2} = \frac{1}{\lambda_g^2} + \frac{1}{\lambda_c^2}$$

*Related location in provided documents: Pages 457, 480, 483, 526.*

***

### (a) What is dispersive waveguide? Why is it called dispersive?

**What is a dispersive waveguide?**
A dispersive waveguide is a medium in which the velocities of wave propagation—specifically the phase velocity ($u_p$) and the group velocity ($u_g$)—are not constant, but rather depend on the operating frequency ($f$) of the wave. 

**Why is it called dispersive?**
It is called "dispersive" because this frequency dependence causes a pulse of electromagnetic energy to spread out, or "disperse," as it travels down the guide. 

Any practical communication signal consists of a band of frequencies (a wave packet) rather than a single pure frequency. Because $u_p$ and $u_g$ are functions of frequency in a waveguide (e.g., $u_g = u' \sqrt{1 - (f_c/f)^2}$), the different frequency components making up the signal will travel at slightly different speeds. Consequently, over a long distance, the faster components will pull ahead of the slower components, causing the original pulse shape to broaden and distort in the time domain. If this dispersion is severe enough, consecutive pulses representing digital bits (1s and 0s) may overlap, leading to data errors or confusion at the receiver. 

*Related location in provided documents: Pages 519, 527-529.*

***

### (b) What is meant by dominant mode of waveguide? Consider an air-filled rectangular waveguide with dimensions a=2.286 cm, b=1.016 cm operates at 5 GHz. Find the cutoff frequencies of all possible propagating modes.

**What is meant by the dominant mode?**
The dominant mode of a waveguide is the specific mode of propagation that has the **lowest cutoff frequency** (or equivalently, the longest cutoff wavelength) of all possible modes. Because a waveguide acts as a high-pass filter, the dominant mode is the first and only mode capable of propagating when the operating frequency is gradually increased from zero and just barely exceeds this lowest cutoff threshold. For a standard rectangular waveguide where width $a > b$, the dominant mode is always the $\text{TE}_{10}$ mode.

**Calculation for the given waveguide:**
1.  **Identify Parameters:**
    *   $a = 2.286 \text{ cm} = 0.02286 \text{ m}$
    *   $b = 1.016 \text{ cm} = 0.01016 \text{ m}$
    *   Operating frequency $f = 5 \text{ GHz} = 5 \times 10^9 \text{ Hz}$
    *   Air-filled, so wave velocity $u' = c \approx 3 \times 10^8 \text{ m/s}$

2.  **Calculate the Cutoff Frequency of the Dominant Mode ($\text{TE}_{10}$):**
    The cutoff frequency for any $TE_{mn}$ or $TM_{mn}$ mode is given by:
    $$f_{c_{mn}} = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$
    For the dominant $\text{TE}_{10}$ mode ($m=1, n=0$):
    $$f_{c_{10}} = \frac{3 \times 10^8}{2} \sqrt{\left(\frac{1}{0.02286}\right)^2 + 0} = \frac{3 \times 10^8}{2 \times 0.02286}$$
    $$f_{c_{10}} = \frac{3 \times 10^8}{0.04572} \approx 6.561 \times 10^9 \text{ Hz} = 6.56 \text{ GHz}$$

3.  **Determine Propagating Modes:**
    For a wave to propagate, the operating frequency $f$ must be *greater* than the cutoff frequency $f_c$ ($f > f_c$).
    
    Here, the operating frequency is **5 GHz**, but the lowest possible cutoff frequency (for the dominant $\text{TE}_{10}$ mode) is **6.56 GHz**. 
    
    Since $5 \text{ GHz} < 6.56 \text{ GHz}$, the operating frequency is below the cutoff frequency of even the lowest-order mode. Therefore, **there are no possible propagating modes**. All modes at 5 GHz will be evanescent and will rapidly attenuate without propagating down the guide.

*Related location in provided documents: Pages 481, 482, 487, 495, 497.*
### Compare waveguides with transmission lines regarding wave propagation and frequency limitations.

While both waveguides and transmission lines are used to direct electromagnetic energy from one point to another, they differ significantly in their modes of wave propagation, their operational frequency ranges, and their practical limitations.

**1. Wave Propagation (Supported Modes):**
*   **Transmission Lines:** A standard transmission line (such as a coaxial cable or a two-wire line) is designed primarily to support **Transverse Electromagnetic (TEM) waves**. In a TEM mode, both the electric and magnetic fields are entirely transverse (perpendicular) to the direction of propagation. 
*   **Waveguides:** A hollow waveguide cannot support a TEM wave. If one attempts to set the longitudinal components of both the electric and magnetic fields to zero ($E_z = 0$ and $H_z = 0$) inside a hollow guide, all other field components mathematically vanish. Instead, waveguides support many other possible field configurations, specifically **Transverse Electric (TE)** modes (where only the electric field is entirely transverse) and **Transverse Magnetic (TM)** modes (where only the magnetic field is entirely transverse).

**2. Frequency Limitations and Filtering:**
*   **Transmission Lines:** These structures can operate from **DC ($f = 0$ Hz) up to very high frequencies**. They act essentially as all-pass filters in terms of theoretical frequency cutoffs, meaning they can transmit a steady direct current just as well as alternating currents (up to a certain practical limit).
*   **Waveguides:** Waveguides act as strict **high-pass filters**. They cannot transmit DC. A waveguide will only allow the propagation of electromagnetic waves that have a frequency above a specific minimum threshold known as the **cutoff frequency ($f_c$)**. Any signal with a frequency below this cutoff will be rapidly attenuated (evanescent) and will not propagate through the structure.

**3. Efficiency and Losses at Microwave Frequencies:**
*   **Transmission Lines:** As frequencies reach the microwave range (roughly 3 GHz to 300 GHz), traditional transmission lines become highly inefficient. They suffer from severe signal attenuation due to the **skin effect** (where current crowds to the outer edges of the conductor, increasing resistance) and substantial **dielectric losses** in the material separating the conductors.
*   **Waveguides:** Waveguides are specifically designed to overcome these high-frequency limitations. Because they are typically hollow (air-filled) and lack an inner conductor, dielectric losses are negligible, and conductor losses are much lower. Therefore, at microwave frequencies, waveguides are preferred to obtain **larger bandwidths and lower signal attenuation**.

**4. Physical Size Constraints:**
*   Because a waveguide's cutoff frequency is inversely proportional to its physical dimensions (larger guides have lower cutoff frequencies), using a waveguide for low-frequency signals (like radio or lower RF bands) would require the waveguide to be **excessively large** and practically impossible to build or use. Transmission lines are much more compact for these lower frequencies. 

*Related location in provided documents: Presentation PDF Pages 450, 451, and 468.*
:


### What do you mean by dominant mode in a waveguide? Consider an air-filled rectangular waveguide with dimensions $a=2.286 \text{ cm}$, $b=1.016 \text{ cm}$ operates at $10 \text{ GHz}$. Find the cutoff frequencies of all possible propagating modes.

**Definition of Dominant Mode:**
In a waveguide, different field patterns or configurations can exist, which are called modes (such as $\text{TE}_{mn}$ or $\text{TM}_{mn}$). Every mode has a specific cutoff frequency below which it cannot propagate. The **dominant mode** is defined as the mode with the lowest cutoff frequency (or equivalently, the longest cutoff wavelength). Because a waveguide acts as a high-pass filter, the dominant mode is the very first mode that is able to propagate as the signal frequency is increased from zero. For a standard rectangular waveguide where the width is greater than the height ($a > b$), the dominant mode is always the $\text{TE}_{10}$ mode.

**Calculation of Cutoff Frequencies for Propagating Modes:**
To find all *possible propagating modes*, we must find all modes whose cutoff frequencies ($f_c$) are strictly less than the operating frequency ($f = 10 \text{ GHz}$).

**1. Identify given parameters:**
*   Width $a = 2.286 \text{ cm} = 0.02286 \text{ m}$
*   Height $b = 1.016 \text{ cm} = 0.01016 \text{ m}$
*   Operating frequency $f = 10 \text{ GHz} = 10 \times 10^9 \text{ Hz}$
*   Speed of light in an air-filled guide $u' = c = 3 \times 10^8 \text{ m/s}$

**2. State the cutoff frequency formula:**
The general formula for the cutoff frequency of any $\text{TE}_{mn}$ or $\text{TM}_{mn}$ mode in a rectangular waveguide is:
$$f_{c_{mn}} = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**3. Calculate the base frequencies for $m=1$ and $n=1$:**
*   For $m=1, n=0$ ($\text{TE}_{10}$ mode):
    $$f_{c_{10}} = \frac{c}{2a} = \frac{3 \times 10^8}{2 \times 0.02286} = \frac{3 \times 10^8}{0.04572} \approx 6.56 \times 10^9 \text{ Hz} = 6.56 \text{ GHz}$$
*   For $m=0, n=1$ ($\text{TE}_{01}$ mode):
    $$f_{c_{01}} = \frac{c}{2b} = \frac{3 \times 10^8}{2 \times 0.01016} = \frac{3 \times 10^8}{0.02032} \approx 14.76 \times 10^9 \text{ Hz} = 14.76 \text{ GHz}$$

**4. Evaluate which modes can propagate ($f_c < 10 \text{ GHz}$):**
*   **$\text{TE}_{10}$ mode:** $f_{c_{10}} = 6.56 \text{ GHz}$. Since $6.56 \text{ GHz} < 10 \text{ GHz}$, this mode **will propagate**.
*   **$\text{TE}_{20}$ mode:** $m=2, n=0$. The cutoff is $f_{c_{20}} = 2 \times f_{c_{10}} = 2 \times 6.56 \text{ GHz} = 13.12 \text{ GHz}$. Since $13.12 \text{ GHz} > 10 \text{ GHz}$, this mode will **not** propagate.
*   **$\text{TE}_{01}$ mode:** $f_{c_{01}} = 14.76 \text{ GHz}$. Since $14.76 \text{ GHz} > 10 \text{ GHz}$, this mode will **not** propagate.
*   Any higher-order modes (like $\text{TE}_{11}$, $\text{TM}_{11}$, $\text{TE}_{02}$, etc.) will mathematically require combinations of these base frequencies, resulting in even higher cutoff frequencies well above 10 GHz.

**Conclusion:**
For the given waveguide operating at 10 GHz, the **only possible propagating mode is the dominant $\text{TE}_{10}$ mode**, and its cutoff frequency is **$6.56 \text{ GHz}$**.

*Related location in provided documents: Pages 482-484, 495, 497, 501-507.*

***

### Can a TM or TE wave with a wave length $3 \text{ cm}$ propagate in a parallel-plate waveguide whose plate separation is $1 \text{ or } 2 \text{ cm}$? Explain.

For an electromagnetic wave to propagate through any waveguide structure (including a parallel-plate waveguide), its operating wavelength ($\lambda$) must be **less than the cutoff wavelength ($\lambda_c$)** of that specific waveguide mode. If $\lambda \ge \lambda_c$ (which corresponds to $f \le f_c$), the wave becomes evanescent and attenuates rapidly without propagating.

For a parallel-plate waveguide, the cutoff wavelength for the lowest-order (dominant) TE or TM mode ($m=1$) is given by:
$$\lambda_c = \frac{2a}{m}$$
where '$a$' is the separation distance between the plates. For the first propagating mode ($m=1$), the cutoff wavelength is simply twice the plate separation: **$\lambda_c = 2a$**.

**Given:**
Operating wavelength of the wave: $\lambda = 3 \text{ cm}$.

**Case 1: Plate separation is $a = 1 \text{ cm}$**
*   The cutoff wavelength is $\lambda_c = 2(1 \text{ cm}) = 2 \text{ cm}$.
*   Comparing the wavelengths: The operating wavelength ($3 \text{ cm}$) is *greater* than the cutoff wavelength ($2 \text{ cm}$). Mathematically, $\lambda > \lambda_c$. 
*   **Conclusion:** The wave **cannot propagate**. The plates are too close together to support the wave, and it will be completely attenuated.

**Case 2: Plate separation is $a = 2 \text{ cm}$**
*   The cutoff wavelength is $\lambda_c = 2(2 \text{ cm}) = 4 \text{ cm}$.
*   Comparing the wavelengths: The operating wavelength ($3 \text{ cm}$) is *less* than the cutoff wavelength ($4 \text{ cm}$). Mathematically, $\lambda < \lambda_c$.
*   **Conclusion:** The wave **can propagate**. The spacing is sufficiently wide to support the field configuration of the wave.

*Related location in provided documents: Pages 481-484, 495-497 (Extrapolated from standard waveguide cutoff principles $\lambda_c = 2a$).*

***

### What are the propagating waves in a waveguide

In a waveguide, electromagnetic waves do not propagate in a single, simple manner like they do in free space. Instead, they propagate in specific field patterns or configurations known as **modes**. Depending on how the electric ($E$) and magnetic ($H$) fields orient themselves relative to the direction of propagation (the $z$-axis), the following categories of waves can exist:

1.  **Transverse Electric (TE) Modes:** In these modes, the electric field is entirely transverse (perpendicular) to the direction of wave propagation. This means there is no electric field component along the axis of the waveguide ($E_z = 0$), but there is a longitudinal magnetic field component ($H_z \neq 0$).
2.  **Transverse Magnetic (TM) Modes:** In these modes, the magnetic field is entirely transverse to the direction of wave propagation. This means there is no magnetic field component along the axis of the waveguide ($H_z = 0$), but there is a longitudinal electric field component ($E_z \neq 0$).
3.  **Transverse Electromagnetic (TEM) Modes:** In this mode, both the electric and magnetic fields are entirely transverse to the direction of propagation ($E_z = 0$ and $H_z = 0$). **However, a hollow rectangular (or circular) waveguide cannot support a TEM mode.** Setting both longitudinal components to zero mathematically forces all other field components inside a hollow guide to vanish. TEM modes can only propagate in structures with two or more separate conductors (like a coaxial cable or parallel transmission lines).
4.  **Hybrid Modes (HE Modes):** In these modes, neither the electric field nor the magnetic field is purely transverse to the direction of propagation ($E_z \neq 0$ and $H_z \neq 0$). These are sometimes found in more complex waveguide structures (like dielectric waveguides or optical fibers).

Therefore, the primary propagating waves inside standard hollow waveguides are the **TE and TM modes**. Each of these modes is further categorized by integer subscripts ($m$ and $n$, e.g., $\text{TE}_{10}$ or $\text{TM}_{11}$) that describe the number of half-cycle variations of the fields across the dimensions of the waveguide.

*Related location in provided documents: Pages 468-469.*

***

### Write the boundary conditions for TM and TE modes in a rectangular waveguide.

The boundary conditions in a rectangular waveguide are derived from the fundamental electromagnetic principle that the tangential components of an electric field must be continuous across a boundary. Because the walls of the waveguide are assumed to be perfect conductors ($\sigma_c = \infty$), the electric field inside the conducting walls is zero. Therefore, the tangential electric field components evaluated precisely at the inner surface of the walls must also be zero.

Assuming a rectangular waveguide with width $a$ along the $x$-axis and height $b$ along the $y$-axis, the boundary conditions are as follows:

**Boundary Conditions for TM (Transverse Magnetic) Modes:**
For TM modes, the primary longitudinal component is $E_z$ (since $H_z = 0$). The longitudinal electric field $E_z$ is entirely tangential to all four walls of the waveguide. Therefore, it must be zero at all boundaries:
*   $E_{zs} = 0$ at $y = 0$ (Bottom wall)
*   $E_{zs} = 0$ at $y = b$ (Top wall)
*   $E_{zs} = 0$ at $x = 0$ (Left side wall)
*   $E_{zs} = 0$ at $x = a$ (Right side wall)

**Boundary Conditions for TE (Transverse Electric) Modes:**
For TE modes, the primary longitudinal component is $H_z$ (since $E_z = 0$). To find the boundary conditions, we must look at the transverse electric field components ($E_{xs}$ and $E_{ys}$) that are tangential to the specific walls:
*   The tangential component $E_{xs}$ must be zero at the top and bottom walls:
    *   $E_{xs} = 0$ at $y = 0$
    *   $E_{xs} = 0$ at $y = b$
*   The tangential component $E_{ys}$ must be zero at the left and right side walls:
    *   $E_{ys} = 0$ at $x = 0$
    *   $E_{ys} = 0$ at $x = a$

Because the transverse electric fields $E_{xs}$ and $E_{ys}$ are mathematically related to the derivatives of the longitudinal magnetic field $H_{zs}$ via Maxwell's curl equations, these electric field boundary conditions directly translate into boundary conditions for $H_{zs}$ (specifically, the normal derivative of $H_{zs}$ must be zero at the walls):
*   $\frac{\partial H_{zs}}{\partial y} = 0$ at $y = 0$
*   $\frac{\partial H_{zs}}{\partial y} = 0$ at $y = b$
*   $\frac{\partial H_{zs}}{\partial x} = 0$ at $x = 0$
*   $\frac{\partial H_{zs}}{\partial x} = 0$ at $x = a$

*Related location in provided documents: Pages 470, 471, 489, 490, 491.*
### Show that waveguides act as high-pass filters and determine the cutoff frequency equation for a×b dimensions.

**1. The Propagation Constant in a Waveguide**
To understand how a waveguide filters frequencies, we must look at the propagation constant, $\gamma$, which dictates how a wave travels through the guide. For a rectangular waveguide of width $a$ and height $b$, solving the wave equation (Helmholtz equation) using the method of separation of variables yields the following expression for the propagation constant:
$$\gamma = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 - k^2}$$

Here, $k$ is the wave number of the unbounded medium, defined as $k = \omega\sqrt{\mu\epsilon}$. Substituting this into the equation gives:
$$\gamma = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 - \omega^2\mu\epsilon}$$

The propagation constant is a complex number, generally expressed as $\gamma = \alpha + j\beta$, where $\alpha$ is the attenuation constant and $\beta$ is the phase constant. The propagation behavior depends entirely on the value inside the square root.

**2. Justifying the High-Pass Filter Behavior**
We can analyze the behavior of the wave by examining what happens at different angular frequencies ($\omega$):

*   **Low Frequencies (Evanescent Mode):** If the frequency is low enough such that $\omega^2\mu\epsilon < \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$, the quantity under the square root is positive. Therefore, $\gamma$ is purely real ($\gamma = \alpha$, and $\beta = 0$). Because the field components are proportional to $e^{-\gamma z} = e^{-\alpha z}$, the wave decays exponentially along the $z$-direction without any phase progression. The wave is severely attenuated and **does not propagate**.
*   **High Frequencies (Propagation Mode):** If the frequency is high enough such that $\omega^2\mu\epsilon > \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$, the quantity under the square root becomes negative. The square root of a negative number yields an imaginary result, meaning $\gamma$ is purely imaginary ($\gamma = j\beta$, and $\alpha = 0$). The field components are proportional to $e^{-\gamma z} = e^{-j\beta z}$. In this state, there is no attenuation, and the wave **propagates freely** down the guide.

**Conclusion on Filtering:** Because the waveguide completely attenuates signals below a certain frequency and allows signals above that frequency to pass without attenuation, it functions inherently as a **high-pass filter**.

**3. Determining the Cutoff Frequency Equation**
The exact transition point between the non-propagating (evanescent) state and the propagating state occurs when the quantity under the square root is exactly zero. The frequency at which this occurs is defined as the **cutoff angular frequency, $\omega_c$**:
$$0 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 - \omega_c^2\mu\epsilon$$

Rearranging the equation to solve for $\omega_c$:
$$\omega_c^2\mu\epsilon = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$
$$\omega_c = \frac{1}{\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$

To express this in terms of the standard cutoff frequency $f_c$ (in Hertz), we substitute $\omega_c = 2\pi f_c$:
$$2\pi f_c = \frac{1}{\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$
$$f_c = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$

By bringing the $\frac{1}{\pi}$ inside the square root (which becomes $\frac{1}{\pi^2}$), the $\pi$ terms cancel out:
$$f_c = \frac{1}{2\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

Finally, recognizing that the phase velocity of a uniform plane wave in the unbounded dielectric medium is $u' = \frac{1}{\sqrt{\mu\epsilon}}$, we arrive at the standard cutoff frequency equation for a specific $TM_{mn}$ or $TE_{mn}$ mode:
$$f_{c_{mn}} = \frac{u'}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

*Related location in provided documents: Presentation PDF Pages 477-482, 640-641.*