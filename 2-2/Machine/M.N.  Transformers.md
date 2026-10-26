---
share_link: https://share.note.sx/gqkw3jdg
share_updated: 2026-10-26T23:04:06+06:00
---

## 📌 Common Symbols & Abbreviations

| Symbol / Abbr | Meaning | Symbol / Abbr | Meaning |
| :--- | :--- | :--- | :--- |
| **XFR / TX** | Transformer | **$\Phi_m$ / $B_m$** | Max core flux / Flux density |
| **prim / sec** | Primary / Secondary winding | **$I_0$** | No-load excitation current |
| **HV / LV** | High Voltage / Low Voltage | **$I_m$ / $I_w$** | Magnetizing / Core-loss current |
| **FL / NL** | Full Load / No Load | **$P_i$ / $P_{cu}$** | Iron (core) loss / Copper loss |
| **EMF / MMF** | Electromotive / Magnetomotive force | **$R_{01}, X_{01}$** | Equiv. resistance / reactance (prim) |
| **VR** | Voltage Regulation | **$R_{02}, X_{02}$** | Equiv. resistance / reactance (sec) |
| **PF / UPF** | Power Factor / Unity Power Factor | **$K$ / $a$** | Transformation ratio / Turns ratio |
| **CT / PT** | Current / Potential Transformer | **$S$ / $\eta$** | Apparent power (kVA) / Efficiency |

---

## 1. Fundamentals & Ideal Transformer

### Core Concept & Working Principle
* **Definition:** Static electromagnetic device; transfers AC power across circuits at constant frequency ($f$).
* **Working Law:** Faraday’s Law of Mutual Induction ($e = -N \frac{d\Phi}{dt}$).
* **Operation Steps:**
  1. Alternating $V_1$ drives alternating magnetizing current.
  2. Alternating core flux ($\Phi = \Phi_m \sin\omega t$) links both windings.
  3. Induces counter-EMF $E_1$ in prim & mutual EMF $E_2$ in sec.
  4. Closed sec circuit $\implies$ drives load current $I_2$.

![[attachments/Pasted image 20261023171933.jpg]]

### Construction Essentials
* **Magnetic Core:** Thin laminated silicon-steel ($0.35\text{--}0.5\text{ mm}$ thick) $\implies$ $\downarrow$ eddy current & $\downarrow$ hysteresis losses; provides low-reluctance path.
* **Windings:** High-conductivity electrolytic copper; insulated by enamel, paper, or oil.
* **Rating:** Rated in **kVA**, not **kW**!
  * **Reason:** $P_i$ depends on voltage ($V$); $P_{cu}$ depends on current ($I$).
  * Total loss depends on $V \times I$, completely independent of load PF ($\cos\phi$).

---

### EMF Equation Derivation
* **Prerequisites:** 
  * Sinusoidal flux: $\Phi(t) = \Phi_m \sin(\omega t) = \Phi_m \sin(2\pi f t)$.
  * Faraday’s & Lenz’s Law: $e(t) = -N \frac{d\Phi(t)}{dt}$.

$$\begin{aligned}
e_1(t) &= -N_1 \frac{d}{dt}\left[\Phi_m \sin(\omega t)\right] \\
&= -N_1 \omega \Phi_m \cos(\omega t) \\
&= N_1 \omega \Phi_m \sin\left(\omega t - \frac{\pi}{2}\right)
\end{aligned}$$

* **Peak EMF:**
$$E_{1,\max} = N_1 \omega \Phi_m = 2\pi f N_1 \Phi_m$$

* **RMS EMF:**
$$E_1 = \frac{E_{1,\max}}{\sqrt{2}} = \frac{2\pi}{\sqrt{2}} f N_1 \Phi_m = \sqrt{2}\pi f N_1 \Phi_m \approx 4.44 f N_1 \Phi_m$$

$$\mathbf{E_1 = 4.44 f N_1 \Phi_m} \quad \text{and} \quad \mathbf{E_2 = 4.44 f N_2 \Phi_m}$$

* **Average Rate of Change Method:**
  * Flux changes from $0 \to \Phi_m$ in $t = T/4 = \frac{1}{4f}\text{ s}$.
  * $\left(\frac{d\Phi}{dt}\right)_{\text{avg}} = \frac{\Phi_m}{1/(4f)} = 4 f \Phi_m\text{ Wb/s}$.
  * Form factor for sine wave: $k_f = \frac{\text{RMS}}{\text{Avg}} = 1.11$.
  * $E_{\text{turn}} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m\text{ V/turn}$.

---

### Transformation Ratio ($K$) vs Turns Ratio ($a$)

$$\mathbf{K = \frac{V_2}{V_1} \approx \frac{E_2}{E_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}} \quad \Longleftrightarrow \quad \mathbf{a = \frac{N_1}{N_2} = \frac{1}{K}}$$

* **MMF Balance (Ideal Core $\mu \to \infty$):**
$$\mathcal{F}_{\text{net}} = N_1 I_1 - N_2 I_2 = 0 \implies N_1 I_1 = N_2 I_2 \implies \frac{I_2}{I_1} = \frac{N_1}{N_2}$$

* **Step-Up vs Step-Down:**

| Parameter | Step-Up XFR | Step-Down XFR |
| :--- | :--- | :--- |
| **Turns Ratio** | $N_2 > N_1 \implies K > 1$ | $N_2 < N_1 \implies K < 1$ |
| **Voltage** | $V_2 > V_1$ | $V_2 < V_1$ |
| **Current** | $I_2 < I_1$ | $I_2 > I_1$ |
| **Main Use** | Power stations (Transmission: $11\text{ kV} \to 132/400\text{ kV}$) | Distribution substations ($11\text{ kV} \to 400/230\text{ V}$) |

---

### Supply Anomalies & Frequency Effects

#### 1. DC Supply Applied to AC XFR
* **Physics:** DC $\implies \frac{d\Phi}{dt} = 0 \implies$ Back-EMF $E_1 = 0$.
* **Impedance:** Only low winding resistance opposes current ($Z_1 = R_1 < 1\ \Omega$).
$$I_{\text{dc}} = \frac{V_{\text{dc}}}{R_1} \gg I_{\text{rated}}$$
* **Outcome:** Massive overcurrent $\to$ core deep saturation $\to$ violent buzzing $\to$ insulation burn-out in seconds.

#### 2. 60 Hz XFR on 50 Hz Supply ($V$ constant)
* **Governing Relation:** $\Phi_m \propto \frac{V}{f}$.
* **Flux Impact:** $f \downarrow$ by $16.7\% \implies \Phi_m \uparrow$ by $20\%$.
* **Consequences:** Deep magnetic saturation $\implies$ magnetizing current $I_m$ surges $\implies P_h \uparrow$ ($P_h \propto f^{-0.6}$) $\implies$ extreme overheating.
* **Remedy:** Derate applied voltage: $V_{\text{new}} = \frac{50}{60} V_{\text{rated}} = 83.3\% V_{\text{rated}}$.

#### 3. 50 Hz XFR on 60 Hz Supply ($V$ constant)
* **Flux Impact:** $f \uparrow \implies \Phi_m \downarrow$ by $16.7\%$ ($83.3\%$ of original).
* **Consequences:** Core operates comfortably below saturation; $I_m \downarrow$; core runs cooler.
* **Loss Profile:** $P_e$ unchanged; $P_h \downarrow$ slightly.
* **Regulation:** $X = 2\pi f L \uparrow \implies$ slightly higher reactance drop. Completely safe to operate.

---

## 2. Phasor Diagrams (No-Load & On-Load)

### No-Load Behavior & Phasor Diagram
* **No-Load Current ($I_0$):** Small current ($2\text{--}5\%$ of $I_{\text{FL}}$) drawn with sec open.
* **Two Orthogonal Components:**
  1. **Magnetizing Component ($I_m$):** In phase with flux $\Phi$; sets up core flux ($I_m = I_0 \sin\phi_0$).
  2. **Core-Loss Component ($I_w$ or $I_c$):** In phase with $-E_1$ ($V_1'$); supplies iron losses ($I_w = I_0 \cos\phi_0$).

$$\vec{I_0} = \vec{I_w} + \vec{I_m} = I_0 \cos\phi_0 + j I_0 \sin\phi_0$$
$$I_0 = \sqrt{I_w^2 + I_m^2}, \quad \text{No-load PF: } \cos\phi_0 = \frac{I_w}{I_0} \approx 0.1\text{--}0.25\text{ lag}$$

| Ideal XFR No-Load | Practical XFR No-Load & Hysteresis |
| :---: | :---: |
| ![[attachments/Pasted image 20261023181304.png]] | ![[attachments/Pasted image 20260908234257.png]] |

---

### On-Load Phasor Diagrams (Without $R$ & $X$)
* Ideal windings ($R=0, X=0$), practical core ($I_0 \neq 0$).
* **Equations:** $\vec{V_1} = -\vec{E_1}$, $\vec{V_2} = \vec{E_2}$, $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.

![[attachments/Pasted image 20260908231027.png]]

---

### Practical Transformer On-Load Phasors (With $R_1, X_1, R_2, X_2$)

* **Governing Phasor Equations:**
$$\vec{V_1} = -\vec{E_1} + \vec{I_1} R_1 + j \vec{I_1} X_1 = -\vec{E_1} + \vec{I_1}\vec{Z_1}$$
$$\vec{E_2} = \vec{V_2} + \vec{I_2} R_2 + j \vec{I_2} X_2 = \vec{V_2} + \vec{I_2}\vec{Z_2}$$
$$\vec{I_1} = \vec{I_0} + \vec{I_2'} \quad \text{where } \vec{I_2'} = K \vec{I_2} \angle 180^\circ$$

* **Phasor Construction Steps:**
  1. Horizontal axis = mutual flux $\vec{\Phi}$.
  2. Plot $\vec{E_1}, \vec{E_2}$ lagging $\vec{\Phi}$ by $90^\circ$; plot counter-EMF $-\vec{E_1}$ at $+90^\circ$.
  3. Plot terminal voltage $\vec{V_2}$ as reference; plot $\vec{I_2}$ at angle $\phi_2$ relative to $\vec{V_2}$.
  4. Add $\vec{I_2} R_2$ ($\parallel \vec{I_2}$) and $j \vec{I_2} X_2$ ($\perp \vec{I_2}$ leading by $90^\circ$) to $\vec{V_2} \to$ yields $\vec{E_2}$.
  5. Reverse $\vec{I_2}$ to primary as $\vec{I_2'} = K I_2$; add $\vec{I_0} \to$ yields primary current $\vec{I_1}$.
  6. Add $\vec{I_1} R_1$ ($\parallel \vec{I_1}$) and $j \vec{I_1} X_1$ ($\perp \vec{I_1}$) to $-\vec{E_1} \to$ yields applied voltage $\vec{V_1}$.

| Unity Power Factor Load | Lagging Power Factor Load | Leading Power Factor Load |
| :---: | :---: | :---: |
| ![[attachments/Pasted image 20260908231042.png]] | ![[attachments/Pasted image 20260908231224.png]] | ![[attachments/Pasted image 20260908231137.png]] |

---

### Physics: Why $I_1 \uparrow$ When $I_2 \uparrow$ (Self-Regulating Action)
```
Secondary load increases (I2 increases)
  │
  ▼
Secondary demagnetizing MMF (N2·I2) opposes core flux Φ
  │
  ▼
Core flux Φ momentarily weakens
  │
  ▼
Primary back-EMF E1 decreases (E1 = 4.44 f N1 Φ)
  │
  ▼
Net driving voltage (V1 - E1) increases
  │
  ▼
Draws extra reflected current I2' from supply mains (N1·I2' = N2·I2)
  │
  ▼
Counter-MMF cancels demagnetizing effect ──▶ Core flux Φ restored to CONSTANT!
```

$$\mathbf{\vec{I_1} = \vec{I_0} + \vec{I_2'}}$$

---

## 3. Actual Transformer & Equivalent Circuit

### Leakage Flux & Leakage Reactance
* **Leakage Flux ($\Phi_{l1}, \Phi_{l2}$):** Flux lines closing through air, linking only one winding.
* **Leakage Reactance ($X_1, X_2$):** Fictitious inductive reactances modeling inductive drop from leakage flux ($X = 2\pi f L_l$).

### Impedance Shifting Derivation
* **Equating Copper Losses:**
$$I_2^2 R_1' = I_1^2 R_1 \implies R_1' = R_1 \left(\frac{I_1}{I_2}\right)^2 = K^2 R_1$$
$$I_1^2 R_2' = I_2^2 R_2 \implies R_2' = R_2 \left(\frac{I_2}{I_1}\right)^2 = \frac{R_2}{K^2} = a^2 R_2$$

* **Equating Reactive Energy Stored:**
$$X_1' = K^2 X_1 \quad \text{and} \quad X_2' = \frac{X_2}{K^2} = a^2 X_2$$

![[attachments/Pasted image 20261023220144.png]]

* **Total Equivalent Parameters:**

| Parameter | Referred to Primary (HV/LV) | Referred to Secondary (LV/HV) |
| :--- | :--- | :--- |
| **Resistance** | $\mathbf{R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}}$ | $\mathbf{R_{02} = R_2 + R_1' = R_2 + K^2 R_1}$ |
| **Reactance** | $\mathbf{X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{K^2}}$ | $\mathbf{X_{02} = X_2 + X_1' = X_2 + K^2 X_1}$ |
| **Impedance** | $\mathbf{Z_{01} = \sqrt{R_{01}^2 + X_{01}^2}}$ | $\mathbf{Z_{02} = \sqrt{R_{02}^2 + X_{02}^2} = K^2 Z_{01}}$ |
| **Ratio** | $\mathbf{\frac{Z_{01}}{Z_{02}} = \left(\frac{N_1}{N_2}\right)^2 = \frac{1}{K^2} = a^2}$ | $\mathbf{\frac{Z_{02}}{Z_{01}} = K^2}$ |

* **Why Shift Impedances?**
  1. Replaces magnetic coupling barrier with a continuous, single electrical circuit.
  2. Simplifies loop/node analysis via direct Ohm’s and Kirchhoff’s Laws.

---

### Equivalent Circuit Diagrams
![[attachments/Pasted image 20261023190508.png]]

* **Approximate Phasor Model:**
![[attachments/Pasted image 20261024014932.png]]

---

## 4. Voltage Regulation (VR)

### Definitions & Formulas
* **Definition:** Percentage change in sec terminal voltage from no-load to rated full-load at fixed prim voltage & frequency.

| Formula | Description |
| :--- | :--- |
| $\mathbf{\%VR = \frac{V_{\text{NL}} - V_{\text{FL}}}{V_{\text{FL}}} \times 100\% = \frac{{}_0V_2 - V_2}{V_2} \times 100\%}$ | Regulation Down (IEC standard, industrial basis) |
| $\mathbf{\%VR = \frac{V_{\text{NL}} - V_{\text{FL}}}{V_{\text{NL}}} \times 100\% = \frac{V_1/a - V_{2,\text{fl}}}{V_1/a} \times 100\%}$ | Regulation Up (All-day basis) |

![[attachments/Pasted image 20260909024726.png]]

---

### Approximate Voltage Drop Derivation
* **Geometry from Secondary Phasor Diagram:**

![[attachments/Pasted image 20260909021932.png]]

$$\begin{aligned}
{}_0V_2 &= \sqrt{(V_2 \cos\phi_2 + I_2 R_{02})^2 + (V_2 \sin\phi_2 \pm I_2 X_{02})^2} \\
&\approx V_2 + I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2
\end{aligned}$$

$$\Delta V = {}_0V_2 - V_2 \approx \mathbf{I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2}$$
$$\text{Sign Rule: } \mathbf{+} \text{ for Lagging PF (Inductive)}, \quad \mathbf{-} \text{ for Leading PF (Capacitive)}$$

* **Per-Unit / Percentage Expression:**
$$\%VR = \left(\frac{I_2 R_{02} \cos\phi \pm I_2 X_{02} \sin\phi}{V_2}\right) \times 100\%$$

$$\mathbf{\%VR = v_r \cos\phi \pm v_x \sin\phi}$$
$$\text{where } v_r = \frac{I_2 R_{02}}{V_2} \times 100\% \quad (\% \text{ resistance drop}), \quad v_x = \frac{I_2 X_{02}}{V_2} \times 100\% \quad (\% \text{ reactance drop})$$

---

### Critical Conditions for Voltage Regulation

| Condition | Mathematical Derivation | Power Factor Nature |
| :--- | :--- | :--- |
| **Max Voltage Drop** | $\frac{d(\%VR)}{d\phi} = -v_r \sin\phi + v_x \cos\phi = 0 \implies \tan\phi = \frac{v_x}{v_r} = \frac{X_{02}}{R_{02}}$ | **Lagging PF** ($\cos\phi = \frac{R_{02}}{Z_{02}}$) |
| **Zero Voltage Drop** | $v_r \cos\phi - v_x \sin\phi = 0 \implies \tan\phi = \frac{v_r}{v_x} = \frac{R_{02}}{X_{02}}$ | **Leading PF** ($\cos\phi = \frac{X_{02}}{Z_{02}}$) |
| **Negative VR** | $v_x \sin\phi > v_r \cos\phi \implies V_2 > {}_0V_2$ (Voltage Rise) | **Leading PF (Capacitive)** |

* **Quality Rule:** Lower $\%VR$ is superior ($\implies$ steadier output voltage across variable loads).

![[attachments/Pasted image 20261024001740.png]]

---

## 5. Transformer Testing, Losses & Efficiency

### Core Losses & Separation
* **Hysteresis Loss:** Energy lost reversing core magnetic domains:
  $$P_h = k_h B_m^{1.6} f V_{\text{core}} \propto f^{-0.6} \quad (\text{for constant } V)$$
* **Eddy Current Loss:** Circulating currents induced in steel sheets:
  $$P_e = k_e B_m^2 f^2 t^2 V_{\text{core}} \propto V^2 \quad (\text{independent of } f \text{ for constant } V)$$
* **Why Iron Loss is Constant at All Loads:**
  $$\Phi_m \approx \frac{V_1}{4.44 f N_1} \approx \text{constant} \implies B_m \approx \text{constant} \implies P_i = \text{constant}$$

* **Core Loss Separation Method:**
$$P_i = P_h + P_e = A f + B f^2 \implies \mathbf{\frac{P_i}{f} = A + B f}$$
* Test at variable frequency with $V/f = \text{const}$; plot $P_i/f$ vs $f$:
  * $y$-intercept = $A$ (Hysteresis constant)
  * Slope = $B$ (Eddy current constant)

---

### Test Procedures: Open-Circuit (OC) & Short-Circuit (SC)

#### Memory Trick: "SHOL"
* **SH**: **S**hort-circuit test $\to$ meters on **H**V side (LV shorted).
* **OL**: **O**pen-circuit test $\to$ meters on **L**V side (HV open).

![[attachments/Pasted image 20261024023820.png]]

---

### Test Parameter Extraction Comparison

| Feature | Open-Circuit (OC) Test | Short-Circuit (SC) Test |
| :--- | :--- | :--- |
| **Energized Side** | **LV side** (Rated $V_0$, rated $f$) | **HV side** (Reduced $V_{sc} \approx 5\text{--}10\% V_{\text{rated}}$) |
| **Opposite Side** | **HV side** left open-circuit | **LV side** solidly short-circuited |
| **Target Loss** | Core iron loss ($P_i$) | Full-load copper loss ($P_{cu}$) |
| **Meter Reading** | $W_0 \approx P_i$ ($I_0^2 R_1 \approx 0$ negligible) | $W_{sc} \approx P_{cu}$ ($P_i \approx 0$ negligible due to low $V_{sc}$) |
| **Why Side Chosen?** | LV voltage safe & standard in lab; HV has dangerous kV | HV rated current is small; won't overload lab meters/variacs |
| **Extracted Model** | Shunt exciting branch ($R_0 \parallel X_0$ or $G_c \parallel B_m$) | Series branch ($R_{eq} + j X_{eq}$) |

---

#### 1. Shunt Parameter Calculations (from OC Test on LV)

* **Step 1 — No-Load PF:**
  $$\cos\phi_0 = \frac{W_0}{V_0 I_0} \implies \sin\phi_0 = \sqrt{1 - \cos^2\phi_0}$$

* **Step 2 — Component Currents:**
  $$I_w = I_0 \cos\phi_0 = \frac{W_0}{V_0} \quad (\text{Core loss component})$$
  $$I_m = I_0 \sin\phi_0 = \sqrt{I_0^2 - I_w^2} \quad (\text{Magnetizing component})$$

* **Step 3 — Core Resistances & Reactances (Parallel Branch):**
  $$\mathbf{R_0 = \frac{V_0}{I_w} = \frac{V_0^2}{W_0}} \qquad \mathbf{X_0 = \frac{V_0}{I_m} = \frac{V_0}{\sqrt{I_0^2 - I_w^2}}}$$

* **Alternative Admittance Method:**
  $$\vert Y_E \vert = \frac{I_0}{V_0}, \quad \theta_0 = \arccos\left(\frac{W_0}{V_0 I_0}\right)$$
  $$Y_E = \vert Y_E \vert \angle -\theta_0 = G_c - j B_m \implies \mathbf{R_c = \frac{1}{G_c}}, \quad \mathbf{X_m = \frac{1}{B_m}}$$

---

#### 2. Series Parameter Calculations (from SC Test on HV)

* **Step 1 — Equivalent Resistance:**
  $$\mathbf{R_{eq} = \frac{W_{sc}}{I_{sc}^2}}$$

* **Step 2 — Equivalent Impedance Magnitude:**
  $$\mathbf{Z_{eq} = \frac{V_{sc}}{I_{sc}}}$$

* **Step 3 — Equivalent Leakage Reactance:**
  $$\mathbf{X_{eq} = \sqrt{Z_{eq}^2 - R_{eq}^2}}$$

* **Alternative Impedance Method:**
  $$\theta_{sc} = \arccos\left(\frac{W_{sc}}{V_{sc} I_{sc}}\right)$$
  $$Z_{SE} = \vert Z_{SE} \vert \angle \theta_{sc} = R_{eq} + j X_{eq} \implies \mathbf{R_{eq} = \vert Z_{SE} \vert \cos\theta_{sc}}, \quad \mathbf{X_{eq} = \vert Z_{SE} \vert \sin\theta_{sc}}$$

---

### Polarity Test: Additive vs Subtractive
* Connect HV ($V_A$) & LV ($V_B$) adjacent terminals together; read voltmeter $V_C$ across remaining ends:
  * **Additive Polarity:** $V_C = V_A + V_B \implies$ Windings wound in opposite directions.
  * **Subtractive Polarity:** $V_C = V_A - V_B \implies$ Windings wound in same direction (Standard for power XFRs).

![[attachments/Pasted image 20261024203401.png]]

---

### Efficiency ($\eta$) & Maximum Efficiency Derivation
* **General Efficiency:**
$$\eta = \frac{P_{\text{out}}}{P_{\text{in}}} = \frac{V_2 I_2 \cos\phi_2}{V_2 I_2 \cos\phi_2 + P_i + I_2^2 R_{02}}$$

* **Condition for Maximum Efficiency (w.r.t. $I_2$):**
  1. Divide numerator & denominator by $I_2$:
     $$\eta = \frac{V_2 \cos\phi_2}{V_2 \cos\phi_2 + \frac{P_i}{I_2} + I_2 R_{02}}$$
  2. Maximize $\eta \implies$ minimize denominator:
     $$\frac{d}{dI_2}\left(V_2 \cos\phi_2 + \frac{P_i}{I_2} + I_2 R_{02}\right) = 0 \implies -\frac{P_i}{I_2^2} + R_{02} = 0$$
  3. Result:
     $$\mathbf{I_2^2 R_{02} = P_i \quad \Longleftrightarrow \quad P_{cu} = P_i}$$
     $$\text{Rule: } \mathbf{\text{Variable Copper Loss} = \text{Constant Iron Loss}}$$

* **Load Fraction ($x$) for Maximum Efficiency:**
$$x = \frac{I_{\max}}{I_{\text{FL}}} = \sqrt{\frac{P_i}{P_{cu(\text{FL})}}}$$

* **Operating kVA at $\eta_{\max}$:**
$$\mathbf{S_{\max\text{-}\eta} = S_{\text{rated}} \times \sqrt{\frac{P_i}{P_{cu(\text{FL})}}}}$$

* **Condition for Maximum Efficiency w.r.t. Power Factor:**
$$\frac{d\eta}{d\phi_2} = 0 \implies \sin\phi_2 = 0 \implies \mathbf{\cos\phi_2 = 1.0 \quad (\text{Unity PF})}$$

---

### All-Day Efficiency ($\eta_{\text{all-day}}$)
* **Definition:** Energy efficiency evaluated over a 24-hour duty cycle:
$$\mathbf{\eta_{\text{all-day}} = \frac{\text{Energy Output (kWh in 24 h)}}{\text{Energy Input (kWh in 24 h)}} = \frac{E_{\text{out}}}{E_{\text{out}} + E_{\text{iron}} + E_{\text{cu}}}}$$
  * $E_{\text{iron}} = P_i \times 24\text{ h}$ (Constant 24/7).
  * $E_{\text{cu}} = \sum x_k^2 P_{cu(\text{FL})} t_k$.

* **Why Preferred for Distribution Transformers?**
  * Grid-connected 24/7 $\implies$ iron losses run uninterrupted for 24 hours.
  * Load varies dramatically (peak load for only 4–6 hrs, light/no-load for remaining 18 hrs).
  * Designed with max $\eta$ at $50\text{--}70\%$ load by keeping iron losses very low.

---

## 6. Autotransformers & Instrument Transformers

### Autotransformer Principle
* **Definition:** Single continuous tapped winding shared mutually between primary and secondary.
* **Dual Power Transfer Mechanism:**
  * **Inductive (Transformed) Power ($S_{\text{ind}}$):** Handled magnetically across core.
  * **Conductive (Direct) Power ($S_{\text{cond}}$):** Transferred galvanically via metallic conduction.

| Core & Tapping Schematic | Chapman Equivalent & Power Formulas |
| :---: | :---: |
| ![[attachments/Pasted image 20261024172210.jpg]] | ![[attachments/Pasted image 20261024195744.png]] |

---

### Copper Saving Derivation
* **Weight of Copper:** $W \propto (\text{Turns } N \times \text{Current } I) = \text{Ampere-Turns (AT)}$.
* **Two-Winding ($W_{\text{two}}$):** $W_{\text{two}} \propto N_1 I_1 + N_2 I_2 = 2 N_1 I_1$.
* **Autotransformer ($W_{\text{auto}}$):**
  * Series section ($N_1 - N_2$ turns): carries current $I_1$.
  * Common section ($N_2$ turns): carries current $(I_2 - I_1)$.
  $$W_{\text{auto}} \propto (N_1 - N_2) I_1 + N_2 (I_2 - I_1) = 2 N_1 I_1 - 2 N_2 I_1 = W_{\text{two}}(1 - K)$$

$$\mathbf{\text{Copper Saved: } \Delta W = W_{\text{two}} - W_{\text{auto}} = K \cdot W_{\text{two}}}$$
$$\text{Proportion: } \mathbf{\frac{W_{\text{auto}}}{W_{\text{two}}} = 1 - K}$$

---

### Power Transformed vs Power Conducted

$$\mathbf{S_{\text{ind}} = (1 - K) S_{\text{auto}} = S_{\text{two}}}$$
$$\mathbf{S_{\text{cond}} = K \cdot S_{\text{auto}}}$$
$$\mathbf{\text{Capacity Multiplier: } \frac{S_{\text{auto}}}{S_{\text{two}}} = \frac{1}{1 - K}}$$

* **Rule:** When $K \to 1$, $S_{\text{auto}} \gg S_{\text{two}}$ and copper saving $\Delta W \approx 100\%$.

---

### Step-Down Connection Reconfigurations (for 440/110 V Unit)

| Connection Scheme | High-Side ($V_H$) | Low-Side ($V_L$) | Voltage Ratio ($V_H/V_L$) |
| :--- | :--- | :--- | :--- |
| **Additive Series** | $440 + 110 = \mathbf{550\text{ V}}$ | $\mathbf{110\text{ V}}$ | $5.00$ |
| **Additive Intermediate** | $440 + 110 = \mathbf{550\text{ V}}$ | $\mathbf{440\text{ V}}$ | $1.25$ |
| **Subtractive Tapped** | $\mathbf{440\text{ V}}$ | $\mathbf{110\text{ V}}$ | $4.00$ |
| **Subtractive Opposing** | $\mathbf{440\text{ V}}$ | $440 - 110 = \mathbf{330\text{ V}}$ | $1.33$ |

---

### Pros, Cons & Hazards of Autotransformers

* **Advantages:**
  * Substantial copper & core material savings.
  * Higher capacity ($S_{\text{auto}} \gg S_{\text{two}}$) and higher efficiency ($> 99\%$).
  * Lower internal impedance $\implies$ superior voltage regulation.
* **Disadvantages & Extreme Hazards when $K \ll 1$:**
  * **No Electrical Isolation:** Direct electrical connection between HV and LV.
  * **Lethal Voltage Hazard:** If common winding breaks/opens, **full high voltage appears directly at low-voltage consumer terminals** $\to$ electrocution & fires.
  * **Massive Short-Circuit Current:** Very low leakage reactance leads to destructive fault levels.
  * **Rule:** NEVER use autotransformers for high-ratio distribution ($11\text{ kV} \to 230\text{ V}$).

---

### Instrument Transformers (CT & PT)

| Parameter | Current Transformer (CT) | Potential Transformer (PT) |
| :--- | :--- | :--- |
| **Primary Connection** | Connected in **Series** with line | Connected in **Parallel** across lines |
| **Secondary Load** | Low impedance (Ammeter coil $\approx 0\ \Omega$) | High impedance (Voltmeter coil $\approx \infty$) |
| **Operating State** | Virtual **Short Circuit** | Virtual **Open Circuit** |
| **Standard Output** | **$5\text{ A}$** or **$1\text{ A}$** | **$110\text{ V}$** or **$100\text{ V}$** |
| **Core Flux** | Varies widely with line current | Constant (dictated by line voltage) |

![[attachments/Pasted image 20261024192854.jpg]]

* **CRITICAL SAFETY RULE: Never Open-Circuit CT Secondary!**
  * Normal: $\mathcal{F}_{\text{net}} = N_1 I_1 - N_2 I_2 = N_1 I_0 \approx 1\text{--}2\% \text{ of } N_1 I_1$.
  * If opened ($I_2 = 0$): Opposing MMF vanishes $\implies$ entire heavy line current becomes magnetizing current.
  * Core drives into extreme saturation $\to$ massive iron loss $\to$ winding burns.
  * Extremely steep $\frac{d\Phi}{dt}$ induces lethal voltage spikes (**several thousand volts**) across secondary terminals $\to$ deadly electrocution hazard.

---

## 7. Parallel Operation of Transformers

### Reasons for Paralleling
1. **Service Continuity:** Maintenance/fault in one unit doesn't disrupt system power.
2. **Maximum Operating Efficiency:** Energize/de-energize units according to load demand.
3. **Incremental Expansion:** Add units as load grows without replacing entire substation.
4. **Physical Limits:** Overcomes transportation size/weight limits of huge single units.

![[attachments/Pasted image 20261024204228.png]]

---

### Paralleling Conditions

| Classification | Condition | Penalty if Violated |
| :--- | :--- | :--- |
| **MANDATORY** | 1. **Identical Voltage Ratios** ($E_A = E_B$) | Continuous circulating currents on no-load; excessive copper loss |
| **MANDATORY** | 2. **Identical Polarity** | Dead short-circuit across busbars; catastrophic explosion |
| **MANDATORY (3-$\Phi$)** | 3. **Identical Phase Sequence & Vector Group** ($0^\circ$ relative shift) | Massive circulating currents between non-coincident phases |
| **DESIRABLE** | 4. **Equal Per-Unit Impedances** ($Z_{puA} = Z_{puB}$) | Transformers share load proportionally to their kVA ratings |
| **DESIRABLE** | 5. **Identical $X/R$ Ratios** | Units operate at identical power factors; no cross-reactive currents |

---

### Load Sharing Derivation (Equal Voltage Ratios)
* **Busbar KVL:**
$$V_L = E - \vec{I}_A \vec{Z}_A = E - \vec{I}_B \vec{Z}_B \implies \vec{I}_A \vec{Z}_A = \vec{I}_B \vec{Z}_B$$

$$\mathbf{\frac{\vec{I}_A}{\vec{I}_B} = \frac{\vec{Z}_B}{\vec{Z}_A} \quad \Longleftrightarrow \quad \frac{S_A}{S_B} = \frac{Z_B}{Z_A}}$$

* **Current Supplied by Each:**
$$\mathbf{\vec{I}_A = \vec{I}_L \left(\frac{\vec{Z}_B}{\vec{Z}_A + \vec{Z}_B}\right)} \quad \text{and} \quad \mathbf{\vec{I}_B = \vec{I}_L \left(\frac{\vec{Z}_A}{\vec{Z}_A + \vec{Z}_B}\right)}$$

* **Active Real Power Ratio:**
$$\mathbf{\frac{P_A}{P_B} = \frac{I_A \cos\phi_A}{I_B \cos\phi_B}}$$

* **Circulating Current (Unequal Ratios $E_A \neq E_B$ on No-Load):**
$$\mathbf{\vec{I}_c = \frac{\vec{E}_A - \vec{E}_B}{\vec{Z}_A + \vec{Z}_B}}$$

---

## 8. Three-Phase Transformers & Connections

### 3-Phase Bank vs Three-Phase Unit
* **Three 1-$\Phi$ Bank:** Modular, easy transport, emergency spare is cheap (replace only 1 phase).
* **Single 3-$\Phi$ Unit:** $15\%$ lighter, $20\%$ smaller footprint, $33\%$ less core steel, cheaper, higher efficiency.

### Polarity Errors in 3-Phase
* **Delta Connection:** Proper polarity: $\vec{E}_A + \vec{E}_B + \vec{E}_C = 0$.
  * If one phase reversed: $\vec{E}_{\text{resultant}} = \vec{E}_A + \vec{E}_B - (-\vec{E}_C) = \mathbf{2 E_{ph}}$.
  * Result: $2 E_{ph}$ shorted inside closed delta mesh $\implies$ instant burnout.
* **Star Connection:** Neutral shifts; line voltages unbalanced ($V_L = V_{ph}$ instead of $\sqrt{3} V_{ph}$).

---

### Standard Connections Summary

| Connection | Characteristics | Key Applications |
| :--- | :--- | :--- |
| **Star-Star (Y-Y)** | Small currents, high voltage; requires neutral ground | High-voltage transmission ties |
| **Delta-Delta ($\Delta$-$\Delta$)** | Heavy currents, low voltage; traps 3rd harmonics; operates V-V | Low-voltage industrial loads |
| **Star-Delta (Y-$\Delta$)** | $\pm 30^\circ$ shift; stable neutral; traps 3rd harmonics | Generating station step-up ($11 \to 132\text{ kV}$) |
| **Delta-Star ($\Delta$-Y)** | $\pm 30^\circ$ shift; provides neutral for 4-wire supply | Commercial/domestic distribution ($400/230\text{ V}$) |

* **Y-Y Problems Without Neutral Ground:**
  1. **Floating Neutral:** Unbalanced loads cause neutral shift $\to$ severe phase voltage distortion.
  2. **Third-Harmonic Overvoltages:** 3rd harmonic currents cannot flow in 3-wire star $\to$ flux peaks heavily ($3f$) $\to$ insulation stress + telephone interference.
  3. **Neutral Grounding Solution:** Restores closed path for 3rd harmonic currents $\to$ flux stays sinusoidal.

---

### Open-Delta (V-V) Connection

```
   A o-----------+                 +-----------o a
                 |                 |
                [ T1 ]            [ T1 ]
                 |                 |
   B o-----------+-----+     +-----+-----------o b
                       |     |
                      [ T2 ] [ T2 ]
                       |     |
   C o-----------------+     +-----------------o c
```

* **Emergency Concept:** One unit damaged/removed from $\Delta$-$\Delta$ bank $\implies$ remaining two units continue supplying balanced 3-$\Phi$ power.
* **Capacity Derating Derivation:**
  * Closed-Delta: $S_{\Delta} = 3 V_{ph} I_{ph} = \sqrt{3} V_L I_L = 3 V_L I_{ph}$.
  * Open-Delta: Line current flows directly through single phase winding ($I_L = I_{ph}$):
    $$S_V = \sqrt{3} V_L I_{ph}$$
  * Capacity Ratio:
    $$\mathbf{\frac{S_V}{S_\Delta} = \frac{\sqrt{3} V_L I_{ph}}{3 V_L I_{ph}} = \frac{1}{\sqrt{3}} \approx 0.577 = \mathbf{57.7\%}}$$
    $$\mathbf{S_\Delta = \sqrt{3} \times S_V \approx 1.732 \times S_V}$$
  * Bank Utilization Factor: $\frac{S_V}{2 \times S_{\text{unit}}} = \frac{\sqrt{3} V_L I_{ph}}{2 V_L I_{ph}} = \frac{\sqrt{3}}{2} = \mathbf{86.6\%}$.

* **Internal $\pm 30^\circ$ Phase Shift & Unequal kW Power Sharing:**
  * Even with balanced load at PF angle $\theta$:
    $$\cos\phi_1 = \cos(\theta - 30^\circ) \quad \text{and} \quad \cos\phi_2 = \cos(\theta + 30^\circ)$$
  * **At UPF ($\theta = 0^\circ$):** $\cos\phi_1 = \cos(-30^\circ) = 0.866$, $\cos\phi_2 = \cos(+30^\circ) = 0.866$.
  * **At 0.866 Lagging ($\theta = 30^\circ$):**
    $$P_1 = S_1 \cos(0^\circ) = \mathbf{1.0 \cdot S_1}, \quad P_2 = S_2 \cos(60^\circ) = \mathbf{0.5 \cdot S_2}$$

---

## 9. Phase Conversion & Special Connections

### Scott Connection (3-$\Phi$ to 2-$\Phi$ Conversion)
* **Goal:** Converts balanced 3-phase supply to balanced 2-phase supply (or vice versa).
* **Two Transformers Used:**
  1. **Main Transformer:** Center-tapped at point $D$ ($50\%$ turns), connected between lines $Y$ and $B$.
  2. **Teaser Transformer:** Connected between line $R$ and center-tap $D$.

![[attachments/Pasted image 20261025005420.png]]

---

### Mathematical Proof of Scott Connection Geometry

* **Step 1: Main Primary Voltage ($V_{YB}$):**
$$V_{\text{main}} = V_{YB} = V_L \implies V_{YD} = V_{DB} = \frac{1}{2} V_L$$

* **Step 2: Teaser Primary Voltage ($V_{RD}$):**
  * From right triangle $\Delta RDY$:
    $$V_{RY}^2 = V_{YD}^2 + V_{RD}^2 \implies V_L^2 = \left(\frac{1}{2}V_L\right)^2 + V_{RD}^2$$
    $$V_{RD}^2 = V_L^2 - \frac{1}{4}V_L^2 = \frac{3}{4} V_L^2$$
    $$\mathbf{V_{RD} = \frac{\sqrt{3}}{2} V_L \approx 0.866 V_L}$$

* **Step 3: Orthogonality ($90^\circ$ Phase Shift):**
  * $\angle RDY = 90^\circ \implies \vec{V}_{RD} \perp \vec{V}_{YB}$.
  * Phasor representation:
    $$\vec{V}_{YB} = V_L \angle 0^\circ \quad \text{and} \quad \vec{V}_{RD} = \left(\frac{\sqrt{3}}{2} V_L\right)\angle 90^\circ$$

* **Step 4: Turns Compensation for Equal Secondary Voltages:**
  * To obtain equal secondary voltages ($|V_{2t}| = |V_{2m}|$):
    $$V_{2m} = V_L \left(\frac{N_S}{N_P}\right)$$
    $$V_{2t} = V_{RD} \left(\frac{N_S}{N_{Pt}}\right) = \left(\frac{\sqrt{3}}{2} V_L\right) \left(\frac{N_S}{N_{Pt}}\right) = V_L \left(\frac{N_S}{N_P}\right)$$
    $$\mathbf{N_{Pt} = \frac{\sqrt{3}}{2} N_P \approx 0.866 N_P}$$

---

### Deriving 3-$\Phi$, 4-Wire Neutral Point ($N$)
* **Neutral Point Position:** Tapped on teaser primary winding at **$1/3$ from junction $D$** (or **$2/3$ down from apex $R$**).

![[attachments/Pasted image 20261025143750.png]]

* **Proof of Neutral Potential:**
$$V_{RN} = \frac{2}{3} V_{RD} = \frac{2}{3}\left(\frac{\sqrt{3}}{2} V_L\right) = \mathbf{\frac{V_L}{\sqrt{3}} = V_{\text{phase}}}$$
$$V_{DN} = \frac{1}{3} V_{RD} = \frac{1}{3}\left(\frac{\sqrt{3}}{2} V_L\right) = \frac{V_L}{2\sqrt{3}}$$
* Line-to-neutral voltages for all three lines are perfectly balanced:
$$\mathbf{V_{AN} = V_{BN} = V_{CN} = \frac{V_L}{\sqrt{3}} = V_{\text{phase}}}$$
* Provides a balanced neutral for 3-phase 4-wire power & lighting distribution.

---

## 📌 Master Equation Reference Table

| Phenomenon / Parameter | Governing Formula | Key Conditions / Remarks |
| :--- | :--- | :--- |
| **RMS Induced EMF** | $E = 4.44 f N \Phi_m$ | $\Phi_m = B_m A_{\text{core}}$ |
| **Impedance Reflection** | $R_{01} = R_1 + R_2/K^2$, $R_{02} = R_2 + K^2 R_1$ | $K = N_2/N_1 = 1/a$ |
| **Voltage Drop** | $\Delta V = I_2 R_{02} \cos\phi \pm I_2 X_{02} \sin\phi$ | $+$ for lag, $-$ for lead |
| **$\%$ Voltage Regulation** | $\%VR = v_r \cos\phi \pm v_x \sin\phi$ | $v_r = \frac{I_2 R_{02}}{V_2}\%$, $v_x = \frac{I_2 X_{02}}{V_2}\%$ |
| **Condition for Max $\eta$** | $P_i = P_{cu} \implies I_2^2 R_{02} = P_i$ | Occurs at $\cos\phi = 1.0$ |
| **Load at Max $\eta$** | $S_{\max\text{-}\eta} = S_{\text{FL}} \times \sqrt{P_i / P_{cu(\text{FL})}}$ | $x = \sqrt{P_i / P_{cu}}$ |
| **All-Day Efficiency** | $\eta_{\text{all-day}} = \frac{\sum P_{\text{out}} t}{\sum P_{\text{out}} t + 24 P_i + \sum P_{cu} t}$ | Evaluated in kWh over 24 h |
| **Autoxmer Cu Saving** | $\Delta W = K \cdot W_{\text{two}}$ | Maximum savings when $K \to 1$ |
| **Autoxmer Capacity** | $S_{\text{auto}} = \frac{S_{\text{two}}}{1 - K}$ | Conductive: $K S_{\text{auto}}$; Inductive: $(1-K) S_{\text{auto}}$ |
| **Parallel Load Sharing** | $\vec{I}_A = \vec{I}_L \left(\frac{\vec{Z}_B}{\vec{Z}_A + \vec{Z}_B}\right)$ | $\frac{S_A}{S_B} = \frac{Z_B}{Z_A}$ |
| **Open-Delta Capacity** | $S_V = \frac{1}{\sqrt{3}} S_\Delta \approx 57.7\% S_\Delta$ | Utilization = $86.6\%$ |
| **Scott Teaser Voltage** | $V_{\text{teaser}} = \frac{\sqrt{3}}{2} V_L \approx 0.866 V_L$ | $N_{\text{teaser}} = 0.866 N_{\text{main}}$ |
| **Scott Neutral Tap** | $V_{AN} = \frac{2}{3} V_{\text{teaser}} = \frac{V_L}{\sqrt{3}}$ | $1/3$ from tap $D$, $2/3$ from apex |
