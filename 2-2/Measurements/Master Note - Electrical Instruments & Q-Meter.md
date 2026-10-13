# Master Note: Electrical Measuring Instruments, PMMC, CRO & Q-Meter

---

> [!tip] ⚡ Quick Formula Cheat-Sheet (Exam Problem Solver)
> *Instant reference when a numerical problem appears. Identify the problem type / given values $\to$ pick the formula.*

### 🎯 Problem-Solving Formula Decision Matrix

| Problem / Target Question | Given Variables | Core Formula to Use | Key Trap / Tip |
| :--- | :--- | :--- | :--- |
| **PMMC Deflection / Torque** | $B, I, N, A, K$ (spring const) | $$T_d = BINA = G \cdot I, \quad \theta = \left(\frac{G}{K}\right) I$$ | Strictly linear: $\theta \propto I_{\text{avg}}$. Reads DC only (reads $0$ on pure sinusoidal AC). |
| **Moving Iron (MI) Deflection** | Current $I$, inductance gradient $\frac{dL}{d\theta}, K$ | $$\theta = \frac{I^2}{2K} \frac{dL}{d\theta}$$ | Non-linear: $\theta \propto I_{\text{rms}}^2$. Reads true RMS on AC & DC. Cramped scale at bottom. |
| **Electrostatic Voltmeter Deflection** | Voltage $V$, capacitance gradient $\frac{dC}{d\theta}, K$ | $$\theta = \frac{V^2}{2K} \frac{dC}{d\theta}$$ | Non-linear: $\theta \propto V_{\text{rms}}^2$. Consumes zero DC power. True RMS reader. |
| **Ammeter Range Extension (Shunt)** | Meter $I_m, R_m$; Target current $I$ | $$m = \frac{I}{I_m} \implies R_{\text{sh}} = \frac{R_m}{m - 1}$$ | Shunt in **parallel**. Always $R_{\text{sh}} \ll R_m$. Manganin alloy avoids thermo-emf errors. |
| **Voltmeter Range Extension (Multiplier)** | Meter $v_m, R_m$; Target voltage $V$ | $$m = \frac{V}{v_m} \implies R_s = R_m (m - 1)$$ | Multiplier in **series**. Always $R_s \gg R_m$. Drops the bulk of line voltage. |
| **Series Ohmmeter Unknown $R_x$** | Half-scale $R_h$, deflection ratio $s = \frac{I_m}{I_{\text{fsd}}}$ | $$R_x = R_h \left( \frac{1 - s}{s} \right), \quad R_h \approx R_1$$ | Scale: $\infty$ on Left ($s=0$), $0$ on Right ($s=1$). Half-scale deflection ($s=0.5$) $\implies R_x = R_h$. |
| **Shunt Ohmmeter Unknown $R_x$** | Half-scale $R_h$, deflection ratio $s = \frac{I_m}{I_{\text{fsd}}}$ | $$R_x = R_h \left( \frac{s}{1 - s} \right), \quad R_h = \frac{R_1 R_m}{R_1 + R_m}$$ | Scale: $0$ on Left ($s=0$), $\infty$ on Right ($s=1$). Best suited for low-resistance tests ($< 10\,\Omega$). |
| **3-Voltmeter AC Power & $\cos\phi$** | Supply $V_1$, Load $V_2$, Resistor $V_3$, Standard $R$ | $$P = \frac{V_1^2 - V_2^2 - V_3^2}{2R}, \quad \cos\phi = \frac{V_1^2 - V_2^2 - V_3^2}{2 V_2 V_3}$$ | $V_3 = I \cdot R$. Voltmeters must draw negligible current compared to load. |
| **3-Ammeter AC Power & $\cos\phi$** | Supply $I_1$, Load $I_2$, Resistor $I_3$, Standard $R$ | $$P = \frac{(I_1^2 - I_2^2 - I_3^2)R}{2}, \quad \cos\phi = \frac{I_1^2 - I_2^2 - I_3^2}{2 I_2 I_3}$$ | Supply $I_1$, load in parallel with non-inductive branch $R$. Avoids potential coil errors. |
| **Induction Energy Meter Constant & Error** | Disk revs $N$, Power $P$, time $t$, true kWh | $$K = \frac{N}{\text{kWh}}, \quad \%\text{ Error} = \frac{\text{Recorded kWh} - \text{True kWh}}{\text{True kWh}} \times 100$$ | True $\text{kWh} = \frac{P [\text{W}] \times t [\text{h}]}{1000}$. Lag angle $\Delta = 90^\circ$ gives $T_d \propto VI\cos\phi$. |
| **Ballistic Flux Meter (Flux Change)** | Search coil $N$, Galvanometer const $G$, Deflection $\Delta\theta$ | $$\Delta\Phi = \frac{G}{N} \cdot \Delta\theta$$ | **No spring control** ($K=0$). Deflection depends only on total $\Delta\Phi$, strictly independent of time. |
| **Core Loss Separation ($P_h$ and $P_e$)** | Total iron loss $P_i$ at varied frequencies $f$ | $$\frac{P_i}{f} = A + B f \implies \begin{cases} P_h = A f & (\text{Hysteresis}) \\ P_e = B f^2 & (\text{Eddy Current}) \end{cases}$$ | Plot $\frac{P_i}{f}$ vs $f$: Vertical intercept $= A$; Slope of straight line $= B$. |
| **Current Transformer (CT) Actual Ratio $R$** | Turn ratio $n = N_s/N_p$, secondary $I_s$, magnetizing $I_m$, core loss $I_c$, burden angle $\delta$ | $$R = \frac{I_p}{I_s} \approx n + \frac{I_m \sin\delta + I_c \cos\delta}{I_s}$$ | Ratio error: $\sigma = \frac{K_n - R}{R} \times 100\%$, where $K_n = \text{Nominal } (I_p/I_s)$. |
| **CT Phase Angle Error ($\theta$)** | Secondary $I_s$, $I_m, I_c$, burden angle $\delta$ | $$\theta \approx \frac{180}{\pi} \left[ \frac{I_m \cos\delta - I_c \sin\delta}{n\, I_s} \right]\quad [\text{degrees}]$$ | Safety: **Never open-circuit CT secondary under load** (extreme core saturation & fatal voltage surge). |
| **CRO Electrostatic Deflection ($D$)** | Screen dist $L$, plate len $l$, plate gap $d$, $V_d, V_a$ | $$D = \frac{L \cdot l \cdot V_d}{2\, d \cdot V_a}$$ | $D \propto V_d$, but $D \propto 1/V_a$. Higher accelerating voltage reduces deflection sensitivity! |
| **CRO Sensitivity ($S$) & Deflection Factor ($G$)** | Deflection $D$, deflecting voltage $V_d$ | $$S = \frac{D}{V_d} = \frac{L \cdot l}{2\, d \cdot V_a}\quad [\text{mm/V}], \quad G = \frac{1}{S}\quad [\text{V/mm}]$$ | $G$ is reciprocal of sensitivity $S$. |
| **CRO Lissajous: Phase Difference ($\phi$)** | Y-intercept $Y_1$, Y-maximum $Y_2$ | $$\sin\phi = \frac{Y_1}{Y_2} \implies \phi = \arcsin\left(\frac{Y_1}{Y_2}\right)$$ | Ellipse axes in 1st/3rd quadrant $\implies \phi$ or $360^\circ - \phi$; 2nd/4th $\implies 180^\circ \pm \phi$. |
| **CRO Lissajous: Frequency Ratio** | Tangencies: horizontal $n_h$, vertical $n_v$ | $$\frac{f_y}{f_x} = \frac{n_h}{n_v} = \frac{\text{Number of Horizontal Tangencies}}{\text{Number of Vertical Tangencies}}$$ | $f_y$ is signal to Y-plates; $f_x$ is time-base or signal to X-plates. |
| **Q-Meter: Quality Factor $Q$** | Resonant tuning cap voltage $V_c$, injected emf $E$ | $$Q = \frac{V_c}{E} = \frac{\omega L}{R}$$ | Series resonance condition $\omega L = \frac{1}{\omega C}$. Low injection resistor $R_{\text{sh}} \approx 0.02\,\Omega$. |
| **Q-Meter: Self / Distributed Capacitance ($C_d$)** | Resonant freqs $f_1, f_2 = 2f_1$; tuning caps $C_1, C_2$ | $$C_d = \frac{C_1 - 4\,C_2}{3}, \quad L = \frac{1}{4\pi^2 f_1^2 (C_1 + C_d)}$$ | Set $f_2 = 2f_1$ exactly. Then tune $C_2$ for peak. Condition check: $C_1 > 4C_2$. |
| **Q-Meter: Series Unknown ($X_s, R_s$)** | Resonant $C_1, Q_1$ (coil only); $C_2, Q_2$ (with $Z_x$) | $$X_s = \frac{C_1 - C_2}{\omega C_1 C_2}, \quad R_s = \left(\frac{C_1}{C_2}\right) \left[\frac{Q_1 - Q_2}{Q_1 Q_2 \omega C_1}\right]$$ | If $C_1 > C_2 \implies X_s > 0$ (Inductive). If $C_1 < C_2 \implies X_s < 0$ (Capacitive). |
| **Ramp-Type DVM (Gating Pulses)** | Input $V_{\text{in}}$, ramp slope $k$, clock freq $f_{\text{clock}}$ | $$\Delta t = \frac{V_{\text{in}}}{k} \implies N = f_{\text{clock}} \cdot \Delta t = \left(\frac{f_{\text{clock}}}{k}\right) V_{\text{in}}$$ | Pulse count $N$ is strictly proportional to input voltage $V_{\text{in}}$. |

---

## 1. Fundamentals, Torques, Damping & Galvanometers

### 1.1 Operating Torques in Indicating Instruments

| Torque | Role | Operating Mechanism | Condition / Equation |
| :--- | :--- | :--- | :--- |
| **Deflecting ($T_d$)** | Moves pointer from zero | Magnetic, Electrostatic, Thermal, Induction | $T_d = f(\text{Measured Quantity})$ |
| **Controlling ($T_c$)** | Opposes $T_d$; limits deflection; returns to zero | Spring Control or Gravity Control | Equilibrium at $T_d = T_c$ |
| **Damping ($T_v$)** | Prevents oscillation; halts pointer quickly | Air Friction, Fluid Friction, Eddy Current | $T_v \propto \frac{d\theta}{dt}$; vanishes at rest |

---

### 1.2 Controlling Systems: Spring vs. Gravity

![[Pasted image 20260923153649.png|442]]

*   **Spring Control:**
    *   Phosphor-bronze hairsprings (non-magnetic, low temperature coefficient).
    *   $T_c = K \theta \propto \theta$.
    *   Produces **uniform / linear scale** when $T_d \propto I$.
    *   Works in any mounting orientation. Aging and temperature affect calibration.
*   **Gravity Control:**
    *   Small adjustable control weight on moving spindle.
    *   $T_c = W \cdot l \sin\theta \propto \sin\theta$.
    *   Scale is **non-linear / cramped** at lower range.
    *   Operates **strictly in vertical orientation**. Immune to temperature and aging.

---

### 1.3 Damping Systems & Dynamics

![[Pasted image 20260923150632.png]]
![[Pasted image 20260923151916.png]]

#### Equation of Motion & Damping Classification
*   Differential equation of moving system:
    $$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + K \theta = T_d$$
    *(where $J$ = moment of inertia, $D$ = damping constant, $K$ = spring constant)*.
*   Critical damping coefficient:
    $$D_c = 2\sqrt{J K}$$
*   **Damping Ratio ($\zeta = D / D_c$):**
    *   **Underdamped ($\zeta < 1$):** Pointer oscillates about final position $\theta_F$ before settling.
    *   **Critically Damped ($\zeta = 1$):** Pointer reaches $\theta_F$ in minimum possible time **without overshoot** (**Dead-Beat Instrument**).
    *   **Overdamped ($\zeta > 1$):** Motion is non-oscillatory but sluggish.

#### Damping Methods
*   **Air Friction:** Aluminium piston moves inside closed cylinder. Used in MI & Dynamometers.
*   **Fluid Friction:** Vanes rotate inside high-viscosity mineral oil. Used in Electrostatic Voltmeters (strictly vertical).
*   **Eddy Current Damping:** Aluminium disc/former rotates through permanent magnetic field. Induced eddy currents oppose motion via Lenz's Law ($T_v \propto B^2 \frac{d\theta}{dt}$). Most efficient; used in PMMC and Induction meters.

#### Tuning an Underdamped Galvanometer to Dead-Beat
*   Total damping is sum of mechanical and electromagnetic damping:
- Induced EMF: $e = G \frac{d\theta}{dt}$, where $G = NBA$ (galvanometer constant).
- Induced current: $i = \frac{e}{R} = \frac{G}{R} \frac{d\theta}{dt}$, where $R$ is the total resistance of the closed circuit ($R = R_g + R_{\text{ext}}$).
- Counter-torque (electromagnetic braking): $T_{\text{em}} = G i = \frac{G^2}{R} \frac{d\theta}{dt}$.
Thus, the electromagnetic damping factor is:

  

$$D_{\text{em}} = \frac{G^2}{R}$$$$D = D_m + \frac{G^2}{R_{\text{total}}}$$
*   For critical damping ($\zeta = 1$), set loop resistance to **Critical Damping Resistance (CDRX)**:
    $$R_{\text{critical}} = \frac{G^2}{2\sqrt{J K} - D_m}$$
*   Adjust external shunt or series resistor until $R_{\text{total}} = R_{\text{critical}}$.

---

## 2. PMMC (Permanent Magnet Moving Coil) Instruments

![[Pasted image 20260923125718.png|531]]

### 2.1 Construction
*   **Permanent Magnet:** U-shaped Alnico magnet with soft iron pole pieces.
*   **Soft Iron Core:** Cylindrical core positioned between poles $\rightarrow$ creates **radial magnetic field** ($B \perp$ coil at all deflection angles $\theta$).
*   **Moving Coil:** Enamelled copper wire wound on light aluminium former (aluminium provides eddy current damping).
*   **Suspension / Springs:** Phosphor-bronze hairsprings provide controlling torque and supply current.

---

### 2.2 Torque Equation & Linear Scale Proof
*   Force on single active vertical side of length $l$:
    $$F_1 = B \cdot I \cdot l$$
*   Total deflecting force on coil with $N$ turns:
    $$F = N \cdot B \cdot I \cdot l$$
*   Deflecting torque couple (separated by coil width $d$):
    $$T_d = F \cdot d = B \cdot I \cdot N \cdot (l \cdot d) = B \cdot I \cdot N \cdot A$$
    Let galvanometer displacement constant $G = B \cdot N \cdot A$:
    $$\mathbf{T_d = G \cdot I}$$
*   Controlling torque from spring:
    $$T_c = K \cdot \theta$$
*   At equilibrium ($T_d = T_c$):
    $$G \cdot I = K \cdot \theta \implies \mathbf{\theta = \left(\frac{B \cdot N \cdot A}{K}\right) I = \left(\frac{G}{K}\right) I}$$
*   **Conclusion:** Deflection is strictly proportional to current ($\theta \propto I$) $\implies$ **Scale is linear / uniform**.

---

### 2.3 AC Incompatibility & Rectifier Conversion

![[Pasted image 20261010183959.png]]
![[Pasted image 20261010185510.png|498]]

#### Why PMMC Cannot Measure AC Directly
*   For sinusoidal current $i(t) = I_m \sin\omega t$:
    $$T_{d(\text{inst})} = G \cdot I_m \sin\omega t$$
*   Average deflecting torque over one full cycle:
    $$T_{d(\text{avg})} = \frac{1}{2\pi} \int_0^{2\pi} G I_m \sin\omega t \, d(\omega t) = 0$$
*   System inertia prevents needle from following $50\ \text{Hz}$ alternations $\implies$ pointer vibrates invisibly around zero or stays stationary.

#### Modification: Rectifier Instruments
*   Bridge rectifier converts AC into pulsating full-wave DC.
*   PMMC responds directly to **Average Value**:
    $$V_{\text{av}} = \frac{2}{\pi} V_m \approx 0.637 V_m$$
*   Scale is calibrated for sinusoidal **RMS Value** using the form factor ($K_f = 1.11$):
    $$\mathbf{V_{\text{rms}} = 1.11 \cdot V_{\text{av}}}$$
*   **Limitation:** Reads incorrectly for non-sinusoidal waveforms due to form-factor distortion.

---

## 3. Moving Iron (MI) Instruments

![[Pasted image 20261011172329.jpg]]

### 3.1 Types & Construction
*   **Attraction Type:** Oval-shaped soft iron disc pulled into coil where field is strongest.
*   moves in such a way so as to increase the flux of the electromagnet. RUET Bangladesh Attraction type moving iron instrument. ✓ This is because the soft iron vane tries to occupy a position of minimum reluctance.
*   **Damping:** Air friction damping (eddy current damping avoided because permanent magnet would distort field).

---

### 3.2 Torque Equation Derivation (Energy Method)
*   Stored magnetic energy in coil of inductance $L( \theta )$:
    $$W = \frac{1}{2} L I^2$$
*   Incremental input electrical energy:
    $$dW_e = I \cdot d\lambda = I \cdot d(L I) = I L \, dI + I^2 \, dL$$
*   Change in stored magnetic energy:
    $$dW = d\left(\frac{1}{2} L I^2\right) = I L \, dI + \frac{1}{2} I^2 \, dL$$
*   Mechanical work performed during displacement $d\theta$:
    $$dW_m = T_d \, d\theta$$
*   Energy Conservation ($dW_e = dW + dW_m$):
    $$I L \, dI + I^2 \, dL = \left(I L \, dI + \frac{1}{2} I^2 \, dL\right) + T_d \, d\theta$$
    $$\frac{1}{2} I^2 \, dL = T_d \, d\theta$$
    $$\mathbf{T_d = \frac{1}{2} I^2 \frac{dL}{d\theta}}$$
*   Equilibrium Deflection ($T_c = K\theta$):
    $$\mathbf{\theta = \frac{1}{2K} I^2 \frac{dL}{d\theta}}$$
*   **Key Properties:**
    *   $\theta \propto I^2 \implies$ Deflection direction independent of current polarity.
    *   Measures both **DC and AC**.
    *   On AC, reads true **RMS current**: $\theta \propto I_{\text{rms}}^2$.
    *   Scale is **non-linear / square-law** (cramped at low values, expanded at high values).

---

## 4. Electrostatic Instruments

![[Pasted image 20260923165622.png]]

### 4.1 Principle & Torque Derivation
*   Acts as a variable capacitor; operates purely on electrostatic field forces.
*   Stored electrostatic energy:
    $$W = \frac{1}{2} C V^2$$
*   Input electrical energy:
    $$dW_e = V \cdot dq = V \cdot d(C V) = V^2 \, dC + C V \, dV$$
*   Differential change in stored field energy:
    $$dW = d\left(\frac{1}{2} C V^2\right) = \frac{1}{2} V^2 \, dC + C V \, dV$$
*   Energy Conservation ($dW_e = dW + dW_m$):
    $$V^2 \, dC + C V \, dV = \left(\frac{1}{2} V^2 \, dC + C V \, dV\right) + T_d \, d\theta$$
    $$\mathbf{T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}}$$
    $$\mathbf{F_d = \frac{1}{2} V^2 \frac{dC}{dx}} \quad (\text{Linear Force})$$
*   Equilibrium Deflection ($T_c = K\theta$):
    $$\mathbf{\theta = \frac{1}{2K} V^2 \frac{dC}{d\theta}}$$

---

### 4.2 Advantages & Limitations
*   **Advantages:**
    *   True voltage sensor; consumes **zero power on DC** and negligible capacitive current on AC.
    *   Measures true **RMS voltage** on AC.
    *   No hysteresis or eddy current errors; immune to stray magnetic fields.
*   **Limitations:**
    *   Weak deflecting torque at low voltages $\implies$ restricted to high voltages ($> 100\ \text{V}$ to $\text{kV}$).
    *   Square-law non-linear scale.

---

## 5. Instrument Range Extension & Ohmmeters

### 5.1 Ammeter Range Extension (Shunt) & Voltmeter Multiplier

![[Pasted image 20261011194756.png]]

#### Ammeter Shunt ($R_{\text{sh}}$)
*   Shunt placed in parallel with meter movement ($R_m, I_m$):
    $$I_{\text{sh}} R_{\text{sh}} = I_m R_m \implies R_{\text{sh}} = \frac{I_m R_m}{I - I_m}$$
*   Multiplying power $m = I / I_m$:
    $$\mathbf{R_{\text{sh}} = \frac{R_m}{m - 1}}$$
*   **Swamping Resistance:** Non-inductive Manganin resistor placed in series with copper coil eliminates temperature coefficient errors.

#### Voltmeter Multiplier ($R_s$)
*   High non-inductive resistance placed in series with meter movement:
    $$V = I_m (R_m + R_s) \implies R_s = \frac{V}{I_m} - R_m$$
*   Voltage multiplying power $m = V / v_m$:
    $$\mathbf{R_s = R_m (m - 1)}$$
*   Sensitivity: $S = \frac{1}{I_{\text{fsd}}}\ (\Omega/\text{V})$. Total meter resistance $R_v = S \times V_{\text{range}}$.

---

### 5.2 Series-Type Ohmmeter

![[Pasted image 20261011182434.jpg]]

*   **Circuit:** Battery $E$, current-limiting $R_1$, zero-adjust shunt $R_2$, basic meter $R_m$, unknown $R_x$.
*   Equivalent parallel meter resistance:
    $$R_p = \frac{R_2 R_m}{R_2 + R_m}$$
*   Internal circuit resistance:
    $$R_h = R_1 + R_p$$
*   **Full-Scale Calibration ($R_x = 0$):**
    $$I_{\text{fsd}} = \left(\frac{E}{R_1 + R_p}\right) \left(\frac{R_2}{R_2 + R_m}\right) = \frac{E}{R_h} \left(\frac{R_2}{R_2 + R_m}\right)$$
*   **Fractional Deflection ($s = I_m / I_{\text{fsd}}$):**
    $$\mathbf{s = \frac{R_h}{R_x + R_h}}$$
*   **Half-Scale Deflection ($s = 0.5$):**
    $$\mathbf{R_{x(\text{half-scale})} = R_h = R_1 + \frac{R_2 R_m}{R_2 + R_m}}$$
*   **Unknown Resistance Formula:**
    $$\mathbf{R_x = R_h \left(\frac{1 - s}{s}\right)}$$
*   **Scale Orientation:** Inverted ($0\ \Omega$ at full scale right, $\infty\ \Omega$ at zero scale left). Best for medium/high resistance.

---

### 5.3 Shunt-Type Ohmmeter

![[Pasted image 20261011204939.jpg]]

*   Unknown $R_x$ connected in parallel across meter movement.
*   Make-break switch $S$ disconnects battery when not testing.
*   Internal Thévenin resistance:
    $$R_h = R_1 \parallel R_m = \frac{R_1 R_m}{R_1 + R_m}$$
*   **Deflection Fraction ($s = I_m / I_{\text{fsd}}$):**
    $$\mathbf{s = \frac{R_x}{R_h + R_x}}$$
*   **Half-Scale Resistance ($s = 0.5$):**
    $$\mathbf{R_{x(\text{half-scale})} = R_h = \frac{R_1 R_m}{R_1 + R_m}}$$
*   **Unknown Resistance Formula:**
    $$\mathbf{R_x = R_h \left(\frac{s}{1 - s}\right)}$$
*   **Scale Orientation:** Forward ($0\ \Omega$ at left zero deflection, $\infty\ \Omega$ at right full scale). Best for low resistance ($< 10\ \Omega$).

---

### 5.4 Clamp-on Ammeter

![[Pasted image 20261011200312.png]]

*   **Principle:** Split magnetic core clips over live current-carrying conductor (acts as 1-turn primary).
*   **Components:** Split laminated iron core with trigger release, secondary multi-turn winding, universal shunt, bridge rectifier, and PMMC indicator.
*   Measures high AC current non-invasively without circuit disconnection.

---

## 6. Electrodynamometers & Wattmeters

### 6.1 Electrodynamometer Connections

![[Pasted image 20261011233422.png]] ![[Pasted image 20261011233429.png]]
![[Pasted image 20261011233458.png]] ![[Pasted image 20261011233517.png]]

*   **Ammeter Connection:** Fixed coils and moving coil connected in series (or moving coil shunted). $T_d \propto I^2$.
*   **Voltmeter Connection:** Fixed and moving coils in series with high non-inductive resistor. $T_d \propto V^2$.
*   **Wattmeter Connection:**
    *   Fixed Coils $\to$ **Current Coil (CC)** in series with load.
    *   Moving Coil $\to$ **Pressure Coil (PC)** across voltage supply with non-inductive resistance $R_p$.

---

### 6.2 Wattmeter Deflecting Torque Derivation
*   Instantaneous currents:
    $$i_p(t) = \frac{v(t)}{R_p} = \frac{\sqrt{2} V \sin(\omega t)}{R_p} = \sqrt{2} I_p \sin(\omega t)$$
    $$i_c(t) = \sqrt{2} I \sin(\omega t - \phi)$$
*   Instantaneous torque:
    $$T_i = i_p \cdot i_c \frac{dM}{d\theta} = 2 I_p I \sin(\omega t) \sin(\omega t - \phi) \frac{dM}{d\theta}$$
    $$T_i = I_p I [\cos\phi - \cos(2\omega t - \phi)] \frac{dM}{d\theta}$$
*   Cycle average deflecting torque (double-frequency term averages to 0):
    $$\mathbf{T_d = I_p I \cos\phi \frac{dM}{d\theta} = \frac{V I \cos\phi}{R_p} \frac{dM}{d\theta}}$$
*   Equilibrium deflection ($T_c = K\theta$):
    $$\mathbf{\theta = \left(\frac{1}{K R_p} \frac{dM}{d\theta}\right) V I \cos\phi = C \cdot P}$$
*   **Result:** Deflection is strictly proportional to active power $P$ ($\theta \propto P$) when $\frac{dM}{d\theta}$ is uniform.

---

### 6.3 Alternative AC Power Measurement Methods

![[Pasted image 20261011235746.png]]

#### Three-Voltmeter Method
*   Non-inductive standard resistor $R$ placed in series with load.
*   Voltages measured: $V_1$ (total supply), $V_2$ (across $R$), $V_3$ (across load).
*   Phasor relation:
    $$V_1^2 = V_2^2 + V_3^2 + 2 V_2 V_3 \cos\phi = V_2^2 + V_3^2 + 2 (I R) V_3 \cos\phi = V_2^2 + V_3^2 + 2 R P$$
*   **Formulas:**
    $$\mathbf{P = \frac{V_1^2 - V_2^2 - V_3^2}{2R}}, \quad \mathbf{\cos\phi = \frac{V_1^2 - V_2^2 - V_3^2}{2 V_2 V_3}}$$

#### Three-Ammeter Method
*   Non-inductive standard resistor $R$ placed in parallel with load.
*   Currents measured: $I_1$ (total supply), $I_2$ (through $R$), $I_3$ (through load).
*   Phasor relation:
    $$I_1^2 = I_2^2 + I_3^2 + 2 I_2 I_3 \cos\phi = I_2^2 + I_3^2 + 2 \left(\frac{V}{R}\right) I_3 \cos\phi = I_2^2 + I_3^2 + \frac{2P}{R}$$
*   **Formulas:**
    $$\mathbf{P = \frac{(I_1^2 - I_2^2 - I_3^2) R}{2}}, \quad \mathbf{\cos\phi = \frac{I_1^2 - I_2^2 - I_3^2}{2 I_2 I_3}}$$

---

## 7. Induction Type Energy Meters

![[Pasted image 20261012000256.jpg]]
![[Pasted image 20261012005958.png]]

### 7.1 Core Components & Driving Torque
*   **Shunt Magnet (Pressure Coil):** Highly inductive coil; flux $\Phi_p \propto V$ lags voltage by angle $\Delta$.
*   **Series Magnet (Current Coil):** Few turns in series with load; flux $\Phi_s \propto I$ in phase with $I$.
*   **Aluminium Disc:** Interacts with fluxes $\Phi_p$ and $\Phi_s$ to induce eddy currents $I_{ep}$ and $I_{es}$.
*   **Driving Torque:**
    $$T_d \propto \Phi_p \Phi_s \sin(\text{angle between fluxes}) = \Phi_p \Phi_s \sin(\Delta - \phi)$$
    $$\mathbf{T_d \propto V I \sin(\Delta - \phi)}$$

---

### 7.2 The $90^\circ$ Lag Condition ($\Delta = 90^\circ$)
*   If shunt magnet flux is made to lag voltage by exactly $\mathbf{\Delta = 90^\circ}$:
    $$T_d \propto V I \sin(90^\circ - \phi) = \mathbf{V I \cos\phi = \text{Power } P}$$
*   **Copper Shading Band (Lag Coil):** Mounted on central limb of shunt magnet; adjusts $\Delta$ to precisely $90^\circ$.

---

### 7.3 Braking Torque & Speed Relation
*   Permanent magnet induces eddy currents in rotating disc:
    $$\mathbf{T_b \propto N} \quad (\text{rotor speed } N)$$
*   At steady speed: $T_d = T_b \implies N \propto P$.
*   Total rotor revolutions over time $t$:
    $$\int N \, dt \propto \int P \, dt = \mathbf{\text{Total Energy Consumed}}$$

---

### 7.4 Meter Errors & Adjustments
*   **Creeping Error:** Slow continuous rotation of disc under **no-load** condition (pressure coil only).
    *   *Cause:* Over-compensation of friction torque or excessive voltage.
    *   *Remedy:* Two small diametrically opposite holes drilled in aluminium disc $\implies$ disk stops when a hole aligns with magnet pole.
*   **Meter Constant ($K$):**
    $$K = \frac{\text{Revolutions}}{\text{kWh}}$$
    $$\text{\% Error} = \frac{\text{Registered Energy} - \text{True Energy}}{\text{True Energy}} \times 100\%$$

---

## 8. Power Factor Meters, Frequency Meters & Tachometers

### 8.1 Single-Phase Electrodynamometer Power Factor Meter

![[Pasted image 20261012032933.png]]

*   **Construction:**
    *   Fixed coils $F_1, F_2$: In series with load (carry current $I$).
    *   Moving coils $C_1, C_2$: Fixed at **$90^\circ$ to each other** on common spindle; **no controlling spring**.
    *   Coil $C_1$ connected with non-inductive resistor $R \implies I_1$ in phase with $V$.
    *   Coil $C_2$ connected with pure inductor $L \implies I_2$ lags $V$ by $90^\circ$.
*   **Working Principle:**
    *   Torque from Coil 1: $T_1 = K V I \cos\phi \sin\theta$.
    *   Torque from Coil 2: $T_2 = K V I \sin\phi \cos\theta$.
    *   At equilibrium ($T_1 = T_2$):
        $$\sin\theta \cos\phi = \cos\theta \sin\phi \implies \tan\theta = \tan\phi \implies \mathbf{\theta = \phi}$$
*   **Scale:** Pointer deflection directly equals phase angle $\phi$; scale calibrated directly in $\cos\phi$ (Lag / Lead).

---

### 8.2 Electrical Resonance Type (Ferrodynamic)

![[Pasted image 20261012015142.jpg]]
![[Pasted image 20261012024030.png]]

*   Fixed coils arranged with curved iron core and moving coil tuned via capacitor $C$.
*   **At Normal / Resonant Frequency ($f = f_0$):**
    $$X_L = X_C \implies T_d \propto \cos 90^\circ = 0 \quad (\text{Pointer at center})$$
*   **At Higher Frequency ($f > f_0$):**
    $$X_L > X_C \implies T_d \propto \cos(90^\circ + \alpha) \quad (\text{Pointer moves to "High"})$$
*   **At Lower Frequency ($f < f_0$):**
    $$X_C > X_L \implies T_d \propto \cos(90^\circ - \beta) \quad (\text{Pointer moves to "Low"})$$

---

### 8.3 DC Tachometer Generator

![[Pasted image 20261012034139.jpg]]

*   Permanent magnet stator + rotating armature shaft coupled to machine whose speed $N$ is measured.
*   Generated terminal voltage:
    $$\mathbf{E_g \propto \Phi \cdot N \propto N}$$
*   Permanent-magnet moving coil voltmeter directly indicates RPM.

---

## 9. Magnetic Measurements: Flux Meter & Ballistic Galvanometer

### 9.1 Ballistic Galvanometer (BG) Setup

![[Pasted image 20261012172022.png]]

*   Measures sudden charge discharge pulse $Q$ (requires large time period $T_0 \gg$ pulse duration).
*   First throw deflection $\theta_1$:
    $$Q = K_q \cdot \theta_1$$
*   **Measurement of Flux & Flux Density:**
    Search coil with $N_s$ turns, area $A$, total circuit resistance $R$:
    $$\Delta\Phi = \frac{Q R}{N_s} = \frac{K_q \theta_1 R}{N_s}, \quad \mathbf{B = \frac{\Delta\Phi}{A}}$$

---

### 9.2 Grassot Flux Meter

![[Pasted image 20261012043031.png|450]] ![[Pasted image 20261012045049.png]]

#### Construction vs. Standard Galvanometer
*   **Zero Restoring Torque ($K \approx 0$):** Suspended by silk thread; current enters through annealed silver strips with negligible torsion.
*   **Heavy Electromagnetic Damping:** Oversized coil with low internal resistance; completely overdamped.

#### Derivation & Independence of Time
1.  Induced EMF in search coil ($N$ turns): $e_c = -N \frac{d\Phi}{dt}$.
2.  Back EMF generated by moving coil: $e_f = G \frac{d\theta}{dt}$.
3.  Loop KVL ($R$ is loop resistance):
    $$e_c - e_f = i R \implies -N \frac{d\Phi}{dt} - G \frac{d\theta}{dt} = i R$$
4.  Since controlling torque $K \approx 0$ and inertia is negligible, driving torque $T = G i \approx 0 \implies i \approx 0$.
5.  Integrating over the flux change:
    $$-N \int_{\Phi_1}^{\Phi_2} d\Phi = G \int_{\theta_1}^{\theta_2} d\theta \implies \mathbf{N \Delta\Phi = G \Delta\theta}$$
    $$\mathbf{\Delta\Phi = \frac{G}{N} \Delta\theta}$$
*   **Crucial Property:** Deflection $\Delta\theta$ depends **solely on total flux change $\Delta\Phi$**, completely independent of time taken or speed of coil movement!

#### Range Extension (Shunt Method)

![[Pasted image 20261012173046.png|491]]

*   Non-inductive shunt $R_{\text{sh}}$ across fluxmeter movement ($R_f$):
    $$\mathbf{\text{Multiplying Factor } m = 1 + \frac{R_f}{R_{\text{sh}}}}$$

---

### 9.3 Separation of Iron Losses (Core Losses)
*   Total core loss:
    $$P_i = P_h + P_e$$
    $$P_h = k_h f B_m^x = A f \quad (\text{Hysteresis Loss})$$
    $$P_e = k_e f^2 B_m^2 = B f^2 \quad (\text{Eddy Current Loss})$$
*   Total loss per frequency:
    $$\mathbf{\frac{P_i}{f} = A + B f}$$
*   **Graphical Separation (Frequency Variation at Constant $B_m$ / Constant $V/f$):**
    *   Plot $\frac{P_i}{f}$ vs $f$.
    *   **$y$-intercept** $= A$ (Hysteresis loss coefficient).
    *   **Slope** $= B$ (Eddy current loss coefficient).
    *   At frequency $f_1$: $P_{h1} = A f_1$ and $P_{e1} = B f_1^2$.

---

## 10. Instrument Transformers (CT & PT)

![[Pasted image 20261013030657.png]]
![[Pasted image 20261013030047.png]]

### 10.1 Current Transformer (CT) Phasor Analysis & Errors
*   Turns ratio: $n = N_s / N_p$. Nominal ratio: $K_n = I_{p(\text{rated})} / I_{s(\text{rated})}$.
*   Exciting current: $I_0 = I_m + j I_c$ ($I_m$ = magnetizing, $I_c$ = core loss).
*   Burden power factor angle: $\delta$.

#### Actual Transformation Ratio ($R$)
$$\mathbf{R = \frac{I_p}{I_s} \approx n + \frac{I_0 \sin(\delta + \alpha)}{I_s} = n + \frac{I_m \sin\delta + I_c \cos\delta}{I_s}}$$
$$\text{Ratio Error \%} = \frac{K_n - R}{R} \times 100\%$$

#### Phase Angle Error ($\theta$)
$$\mathbf{\theta \approx \frac{I_m \cos\delta - I_c \sin\delta}{n I_s} \text{ rad} = \frac{180}{\pi}\left(\frac{I_m \cos\delta - I_c \sin\delta}{n I_s}\right)^\circ}$$

---

### 10.2 Safety Rule: Why CT Secondary Must Never Be Open-Circuited
1.  Under normal operation, secondary m.m.f. ($N_s I_s$) strongly opposes primary m.m.f. ($N_p I_p$), leaving tiny resultant m.m.f. ($N_p I_0$).
2.  If secondary opens ($I_s = 0$), opposing m.m.f. collapses to zero.
3.  Full primary line current acts entirely as magnetizing current $\implies$ core is driven into extreme magnetic saturation.
4.  Massive peak flux induces **lethal kilovolt voltages** across open secondary terminals (fatal shock hazard & insulation puncture).
5.  Excessive core losses cause extreme overheating, destroying the CT.

---

## 11. Cathode Ray Oscilloscope (CRO) & CRT

### 11.1 CRT Construction & Block Diagram

![[Pasted image 20261012192851.jpg]]
![[Pasted image 20261012191748.png]]

*   **Electron Gun:** Emits, accelerates, and focuses electron beam (Cathode, Control Grid, Pre-accelerating, Focusing, Accelerating Anode $V_a$).
*   **Deflection Plates:** Electrostatic $Y$-plates (vertical) and $X$-plates (horizontal).
*   **Aquadag Coating:** Graphite coating collects secondary emission electrons, preventing wall charging.
*   **Delay Line:** Delays vertical signal by $\approx 200\ \text{ns}$ to allow time base generator to trigger and stabilize first.
*   **Time-Base Generator:** Generates linear sawtooth voltage for constant-velocity horizontal sweep.

---

### 11.2 Derivation of Electrostatic Deflection ($D$)

![[Pasted image 20261012192226.png]]

1.  **Axial Velocity ($v_{ox}$):**
    Accelerated through potential $V_a$:
    $$\frac{1}{2} m v_{ox}^2 = e V_a \implies v_{ox} = \sqrt{\frac{2 e V_a}{m}}$$
2.  **Transit Time ($t_d$):**
    Length of deflecting plates $l$:
    $$t_d = \frac{l}{v_{ox}}$$
3.  **Transverse Acceleration ($a_y$):**
    Deflecting voltage $V_d$, plate spacing $d$:
    $$a_y = \frac{e E_y}{m} = \frac{e V_d}{m d}$$
4.  **Vertical Exit Velocity ($v_y$):**
    $$v_y = a_y t_d = \frac{e V_d l}{m d v_{ox}}$$
5.  **Deflection Angle ($\tan\theta$):**
    $$\tan\theta = \frac{v_y}{v_{ox}} = \frac{e V_d l}{m d v_{ox}^2} = \frac{e V_d l}{m d \left(\frac{2 e V_a}{m}\right)} = \frac{l V_d}{2 d V_a}$$
6.  **Screen Deflection ($D$):**
    Distance from plate center to screen is $L$:
    $$\mathbf{D = L \tan\theta = \frac{L l V_d}{2 d V_a}}$$
*   **Deflection Sensitivity ($S$):**
    $$\mathbf{S = \frac{D}{V_d} = \frac{L l}{2 d V_a}\ (\text{mm/V})}$$
*   **Deflection Factor ($G$):**
    $$\mathbf{G = \frac{1}{S} = \frac{2 d V_a}{L l}\ (\text{V/mm})}$$

---

### 11.3 Lissajous Patterns & Measurements

![[Pasted image 20261012202536.png]]
![[Pasted image 20261012210620.png|513]]

#### Phase Difference ($\phi$)
*   For equal-frequency sinusoidal inputs:
    *   $\phi = 0^\circ$ or $180^\circ \to$ Diagonal straight line.
    *   $\phi = 90^\circ$ or $270^\circ \to$ Circle (if amplitudes equal).
    *   Arbitrary $\phi \to$ Ellipse.
*   **Formula:**
    $$\mathbf{\sin\phi = \frac{Y_1}{Y_2} = \frac{X_1}{X_2}}$$
    *(where $Y_1$ = $y$-axis intercept; $Y_2$ = maximum vertical deflection)*.

#### Frequency Ratio (Tangency Method)
$$\mathbf{\frac{f_y}{f_x} = \frac{\text{Number of Horizontal Tangencies } (n_h)}{\text{Number of Vertical Tangencies } (n_v)}}$$

---

## 12. Q-Meter & Resonance Measurements

### 12.1 Working Principle

![[Pasted image 20261012232052.png]]

*   Based on **series resonance**:
    $$\omega_0 = \frac{1}{\sqrt{L C}} \implies X_L = X_C$$
*   At resonance, current $I_0 = E / R$.
*   Voltage across tuning capacitor:
    $$V_C = I_0 X_C = \left(\frac{E}{R}\right) \frac{1}{\omega_0 C} = E \left(\frac{\omega_0 L}{R}\right) = Q \cdot E$$
*   **Magnification Principle:**
    $$\mathbf{Q = \frac{V_C}{E}}$$
*   With known injected voltage $E$ held constant, electronic voltmeter across $C$ is calibrated directly in $Q$.

---

### 12.2 Measurement Methods

#### Series Connection (Low-Impedance $Z_s = R_s \pm j X_s$)

![[Pasted image 20261012232116.png]]

1.  **Step 1:** Work coil alone resonated at $C_1, Q_1$:
    $$\omega L = \frac{1}{\omega C_1}$$
2.  **Step 2:** Unknown $Z_s$ inserted in series; retuned at $C_2, Q_2$:
    $$\mathbf{X_s = \frac{1}{\omega C_2} - \frac{1}{\omega C_1} = \frac{C_1 - C_2}{\omega C_1 C_2}}$$
    $$\mathbf{R_s = \frac{C_1}{C_2}\left(\frac{Q_1 - Q_2}{Q_1 Q_2 \omega C_1}\right)}$$
    *(Inductive if $C_1 > C_2$; Capacitive if $C_2 > C_1$)*.

---

### 12.3 Distributed / Self-Capacitance ($C_d$) Measurement
*   **Two-Frequency Resonance Method:**
    1.  Resonate coil at frequency $f_1$ with tuning capacitance $C_1$:
        $$f_1 = \frac{1}{2\pi\sqrt{L(C_1 + C_d)}}$$
    2.  Double frequency to $f_2 = 2 f_1$; retune to resonance with capacitance $C_2$:
        $$f_2 = 2 f_1 = \frac{1}{2\pi\sqrt{L(C_2 + C_d)}}$$
    3.  Ratio of frequencies:
        $$\frac{f_2}{f_1} = 2 = \sqrt{\frac{C_1 + C_d}{C_2 + C_d}} \implies 4 = \frac{C_1 + C_d}{C_2 + C_d}$$
        $$4 C_2 + 4 C_d = C_1 + C_d \implies \mathbf{C_d = \frac{C_1 - 4 C_2}{3}}$$
*   **True Inductance ($L$):**
    $$\mathbf{L = \frac{1}{4\pi^2 f_1^2 (C_1 + C_d)}}$$

---

## 13. Digital Voltmeters (DVM) & ADCs

### 13.1 Ramp-Type DVM

![[Pasted image 20261013004517.png]]
![[Pasted image 20261013004458.png]]

*   **Principle:** Voltage-to-time conversion.
*   Linear downward ramp starts from reference voltage.
*   **Start of Count:** Comparator C1 detects coincidence between input voltage $V_{\text{in}}$ and ramp $\to$ opens gate.
*   **End of Count:** Zero Crossing Detector C2 detects ramp crossing $0\ \text{V} \to$ closes gate.
*   Gating time: $\Delta t = V_{\text{in}} / k$.
*   Total clock pulses counted:
    $$\mathbf{N = f_{\text{clock}} \cdot \Delta t \propto V_{\text{in}}}$$

---

### 13.2 Potentiometric (Servo) DVM

![[Pasted image 20261013004450.png]]

*   Continuous null-balance comparator loop.
*   Error between $V_{\text{in}}$ and internal feedback potentiometer voltage drives servomotor / stepping switches to null error. High precision, slow response.

---

### 13.3 Successive Approximation Register (SAR) DVM

![[Pasted image 20261013004916.png]]

*   **Binary Search Method:**
    *   Conversion takes exactly **$N$ clock cycles** for $N$-bit resolution.
    *   Cycle 1: Set MSB to 1 ($1000\dots$). If $V_{\text{DAC}} > V_{\text{in}} \implies$ clear bit to 0; else keep 1.
    *   Cycles $2 \dots N$: Repeat comparison sequentially down to LSB.
*   Fastest general-purpose ADC architecture for digital instruments.

---

## 14. Quick Formula & Numerical Cheat-Sheet

### 14.1 Deflecting Torques & Scale Laws

| Instrument Type | Deflecting Torque ($T_d$) | Final Deflection ($\theta$) | Scale Characteristic |
| :--- | :--- | :--- | :--- |
| **PMMC** | $T_d = BINA = G \cdot I$ | $\theta = \left(\frac{G}{K}\right) I$ | **Strictly Linear** ($\theta \propto I$) |
| **Moving Iron (MI)** | $T_d = \frac{1}{2} I^2 \frac{dL}{d\theta}$ | $\theta = \frac{1}{2K} I^2 \frac{dL}{d\theta}$ | **Square law** ($\theta \propto I_{\text{rms}}^2$) — cramped at bottom |
| **Electrostatic** | $T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}$ | $\theta = \frac{1}{2K} V^2 \frac{dC}{d\theta}$ | **Square law** ($\theta \propto V_{\text{rms}}^2$) |
| **Electrodynamometer** | $T_d = I_1 I_2 \frac{dM}{d\theta}$ | $\theta = \frac{1}{K} I_1 I_2 \cos\phi \frac{dM}{d\theta}$ | Wattmeter: Linear with active power $P$ |

---

### 14.2 Range Extension: Shunts & Multipliers

| Meter Application | Multiplying Factor ($m$) | Resistor Placement | Exact Resistance Formula |
| :--- | :--- | :--- | :--- |
| **Ammeter Shunt** | $m = \frac{I}{I_m}$ | Parallel ($R_{\text{sh}}$ across meter) | $$R_{\text{sh}} = \frac{R_m}{m - 1}$$ |
| **Voltmeter Multiplier** | $m = \frac{V}{v_m}$ | Series ($R_s$ in series with meter) | $$R_s = R_m (m - 1)$$ |

> [!tip] Practical Memory Rule
> *   Current divider (Shunt): $m - 1$ in denominator $\implies R_{\text{sh}} \ll R_m$
> *   Voltage divider (Multiplier): $m - 1$ in numerator $\implies R_s \gg R_m$

---

### 14.3 Ohmmeters: Half-Scale Deflection ($R_h$) & Unknown ($R_x$)

*   **Deflection fraction:** $s = \frac{\theta}{\theta_{\text{max}}} = \frac{I_m}{I_{\text{fsd}}}$

| Ohmmeter Type | Half-Scale Resistance ($R_h$) | Unknown Resistance $R_x(s)$ | Scale Direction |
| :--- | :--- | :--- | :--- |
| **Series Ohmmeter** | $R_h = R_1 + (R_2 \parallel R_m) \approx R_1$ | $$R_x = R_h \left( \frac{1 - s}{s} \right)$$ | $\infty$ at Left ($s=0$) $\to 0$ at Right ($s=1$) |
| **Shunt Ohmmeter** | $R_h = R_1 \parallel R_m = \frac{R_1 R_m}{R_1 + R_m}$ | $$R_x = R_h \left( \frac{s}{1 - s} \right)$$ | $0$ at Left ($s=0$) $\to \infty$ at Right ($s=1$) |

---

### 14.4 3-Meter AC Power & Power Factor Methods

| Method | Total Active Power ($P$) | Load Power Factor ($\cos\phi$) |
| :--- | :--- | :--- |
| **3-Voltmeter Method** | $$P = \frac{V_1^2 - V_2^2 - V_3^2}{2 R}$$ | $$\cos\phi = \frac{V_1^2 - V_2^2 - V_3^2}{2 V_2 V_3}$$ |
| **3-Ammeter Method** | $$P = \frac{(I_1^2 - I_2^2 - I_3^2) R}{2}$$ | $$\cos\phi = \frac{I_1^2 - I_2^2 - I_3^2}{2 I_2 I_3}$$ |

*(Where index $1 = \text{Supply}$, $2 = \text{Load}$, $3 = \text{Known standard non-inductive resistor } R$)*

---

### 14.5 Induction Energy Meter & Ballistic Flux Meter

*   **Induction Energy Meter:**
    *   Deflecting torque: $T_d \propto V \cdot I \cdot \sin(\Delta - \phi)$
    *   Lag adjustment at $\Delta = 90^\circ \implies T_d \propto V I \cos\phi = P$
    *   Braking torque: $T_B \propto N \implies$ Speed $N \propto P \implies \text{Total Revolutions} \propto \int P\,dt = \text{Energy}$
    *   **Meter Constant:**
        $$K = \frac{\text{Total Disk Revolutions}}{\text{Energy in kWh}}$$
*   **Grassot Flux Meter (Zero Control Spring):**
    *   Dynamic balance: $N \cdot \Delta\Phi = G \cdot \Delta\theta$
    *   **Flux Change:**
        $$\Delta\Phi = \frac{G}{N} \cdot \Delta\theta$$
    *   Deflection is strictly proportional to total flux linkages change, independent of duration.

---

### 14.6 CRO / CRT Electrostatic Deflection & Lissajous

*   **Screen Deflection:**
    $$D = \frac{L \cdot l \cdot V_d}{2\, d \cdot V_a}$$
    *(Where $L =$ screen distance, $l =$ plate length, $d =$ plate separation, $V_d =$ deflecting voltage, $V_a =$ accelerating anode voltage)*
*   **Sensitivity & Factor:**
    *   Deflection Sensitivity: $S = \frac{D}{V_d} = \frac{L \cdot l}{2\, d \cdot V_a}\quad [\text{mm/V}]$
    *   Deflection Factor: $G = \frac{1}{S} = \frac{2\, d \cdot V_a}{L \cdot l}\quad [\text{V/mm}]$
*   **Lissajous Pattern Analysis:**
    *   **Phase Shift ($\phi$):** $\sin\phi = \frac{Y_1}{Y_2} = \frac{X_1}{X_2}$ ($Y_1 =$ y-intercept, $Y_2 =$ y-maximum)
    *   **Frequency Ratio:** $\frac{f_y}{f_x} = \frac{\text{Horizontal Tangencies } (n_h)}{\text{Vertical Tangencies } (n_v)}$

---

### 14.7 Q-Meter (Resonance & Impedance Substitution)

*   **Quality Factor & Self-Capacitance ($C_d$):**
    $$Q = \frac{V_c}{E} = \frac{\omega L}{R}$$
    $$C_d = \frac{C_1 - 4\,C_2}{3} \quad (\text{when } f_2 = 2 f_1) \qquad\qquad L = \frac{1}{4\pi^2 f_1^2 (C_1 + C_d)}$$
*   **Unknown Impedance by Series Substitution:**
    *   **Unknown Reactance:**
        $$X_s = \frac{C_1 - C_2}{\omega\, C_1 C_2} \quad \begin{cases} > 0 & \text{Inductive } (C_1 > C_2) \\ < 0 & \text{Capacitive } (C_1 < C_2) \end{cases}$$
    *   **Unknown Resistance:**
        $$R_s = \left(\frac{C_1}{C_2}\right) \left[ \frac{Q_1 - Q_2}{Q_1 Q_2\, \omega\, C_1} \right]$$

---

### 14.8 Current Transformer (CT) Errors

*   **Actual Transformation Ratio ($R$):**
    $$R = \frac{I_p}{I_s} \approx n + \frac{I_m \sin\delta + I_c \cos\delta}{I_s}$$
    *   $\text{Ratio Error } \% = \frac{K_n - R}{R} \times 100\%$ (where $K_n =$ nominal turn ratio)
*   **Phase Angle Error ($\theta$):**
    $$\theta \approx \frac{180}{\pi} \left[ \frac{I_m \cos\delta - I_c \sin\delta}{n\, I_s} \right]\quad [\text{degrees}]$$
    *(Positive $\theta$ indicates reversed secondary current vector leads primary current vector)*
