
## 1. Resistance Classification & Overview

| Class | Value Range | Major Measurement Methods | Dominant Error / Challenge |
| :--- | :--- | :--- | :--- |
| **Low** | $< 1\ \Omega$ | Kelvin Double Bridge, Ammeter-Voltmeter (Low $R$), Potentiometer | Contact & lead resistance ($r$) |
| **Medium** | $1\ \Omega - 100\ \text{k}\Omega$ | Wheatstone Bridge, Carey-Foster Bridge, Substitution, Ammeter-Voltmeter | Contact resistance at lower limit |
| **High** | $> 100\ \text{k}\Omega$ | Loss of Charge, Megger, Direct Deflection, Megaohm Bridge | Insulation leakage currents |

---

## 2. Measurement of Medium Resistance

### 2.1 Methods Summary
*   **Wheatstone Bridge:** Precision null method for $1\ \Omega - 100\ \text{k}\Omega$.
*   **Carey-Foster Slide-Wire Bridge:** Difference of two nearly equal resistances; eliminates lead errors.
*   **Substitution Method:** Replaces $R$ with standard $S$ until $I$ matches; avoids meter calibration error.
*   **Ammeter-Voltmeter Method:** Simple; needs correction for meter internal resistances.
*   **Ohmmeter:** Quick, rough estimate ($\pm 5\%$).

---

### 2.2 Substitution Method

![[Pasted image 20260922140749.png|469]]

#### Circuit & Working
*   **Components:** DC source, regulating rheostat $r$, ammeter $A$, switch, unknown $R$, standard decade box $S$.
*   **Step 1:** Switch $\rightarrow$ Pos 1 (connect $R$). Adjust $r$ for deflection $I$:
    $$I = \frac{E}{R + r + R_a}$$
*   **Step 2:** Switch $\rightarrow$ Pos 2 (connect $S$). Adjust $S$ until ammeter reads same $I$:
    $$I = \frac{E}{S + r + R_a}$$
*   **Result:**
    $$R = S$$
*   **Advantage:** Eliminates ammeter calibration errors completely.
*   **Condition:** Supply $E$ and rheostat $r$ must remain strictly constant.

---

### 2.3 Ammeter-Voltmeter Method (Error Analysis)

![[Pasted image 20260922163156.png]]

#### Comparison of Connections

| Parameter | Connection (a): Ammeter Near $R$ | Connection (b): Voltmeter Across $R$ |
| :--- | :--- | :--- |
| **Diagram** | Voltmeter measures $(V_a + V_R)$; Ammeter measures $I_R$ | Ammeter measures $(I_v + I_R)$; Voltmeter measures $V_R$ |
| **Measured Value** | $R_m = \frac{V}{I} = R + R_a$ | $R_m = \frac{V}{I} = \frac{R R_v}{R + R_v}$ |
| **True Value** | $R = R_m - R_a$ | $R = \frac{R_m R_v}{R_v - R_m} = \frac{R_m}{1 - (R_m / R_v)}$ |
| **Relative Error $\varepsilon_r$** | $\varepsilon_r = \frac{R_m - R}{R} = +\frac{R_a}{R}$ | $\varepsilon_r = \frac{R_m - R}{R} \approx -\frac{R}{R_v}$ |
| **Best Suited For** | **High / Upper-Medium $R$** ($R \gg R_a$) | **Low / Lower-Medium $R$** ($R \ll R_v$) |

#### Threshold Resistance Criterion
*   Equate magnitudes of relative errors:
    $$\frac{R_a}{R} = \frac{R}{R_v} \implies R^2 = R_a R_v \implies R_{\text{cross}} = \sqrt{R_a R_v}$$
*   **Decision Rule:**
    *   If $R > \sqrt{R_a R_v} \longrightarrow$ Use **Connection (a)**.
    *   If $R < \sqrt{R_a R_v} \longrightarrow$ Use **Connection (b)**.

> [!EXAMPLE] Selection Example
> *Given:* $R \approx 80\ \Omega$, $R_a = 1.5\ \Omega$, $R_v = 4000\ \Omega$.
> *Criterion:* $\sqrt{R_a R_v} = \sqrt{1.5 \times 4000} = \sqrt{6000} \approx 77.46\ \Omega$.
> *Decision:* Since $80\ \Omega > 77.46\ \Omega \implies$ **Connection (a)** gives smaller relative error.

---

### 2.4 Wheatstone Bridge Sensitivity & Galvanometer Equations

#### Bridge Balance Condition
$$\frac{P}{Q} = \frac{R}{S} \implies R = \frac{P}{Q} S$$

#### Bridge Sensitivity ($S_B$)
*   **Definition:** Galvanometer deflection per unit fractional change in unknown $R$:
    $$S_B = \frac{\theta}{\Delta R / R}$$
*   **Voltage Sensitivity of Galvanometer:** $S_v = \frac{\theta}{E_o}\ (\text{mm/V or deg/V})$.

#### Derivation of General Bridge Sensitivity
1.  **Unbalance Thevenin Voltage ($E_o$):**
    $$E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{P}{P + Q} \right]$$
    At initial balance: $\frac{P}{P+Q} = \frac{R}{R+S}$.
    $$E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{R}{R + S} \right] = \frac{E \cdot S \cdot \Delta R}{(R + S)^2 + \Delta R(R + S)}$$
    For small unbalance ($\Delta R \ll R+S$):
    $$E_o \approx \frac{E \cdot S \cdot \Delta R}{(R + S)^2}$$
2.  **Galvanometer Deflection ($\theta$):**
    $$\theta = S_v \cdot E_o = S_v \frac{E \cdot S \cdot \Delta R}{(R + S)^2}$$
3.  **Bridge Sensitivity Formula:**
    $$S_B = \frac{\theta}{\Delta R / R} = \frac{S_v \cdot E \cdot S \cdot R}{(R + S)^2} = \frac{S_v E}{\frac{(R + S)^2}{SR}} = \frac{S_v E}{\frac{R}{S} + 2 + \frac{S}{R}}$$
    Substitute balance ratio $\frac{R}{S} = \frac{P}{Q}$ and $\frac{S}{R} = \frac{Q}{P}$:
    $$\mathbf{S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}}$$

#### Equal-Arm Condition ($P = Q = R = S$)
$$S_B = \frac{S_v E}{1 + 1 + 2} = \mathbf{\frac{S_v E}{4}}$$
*   **Condition for Maximum Sensitivity:** $\frac{P}{Q} = 1$ (equal ratio arms).

#### Galvanometer Current ($I_g$) for Small Unbalance
*   **Thevenin Resistance ($R_o$):**
    $$R_o = (P \parallel Q) + (R \parallel S) = \frac{PQ}{P + Q} + \frac{RS}{R + S}$$
*   **Equal Arms ($P = Q = R = S$):**
    $$R_o = \frac{R}{2} + \frac{R}{2} = R, \quad E_o \approx \frac{E \Delta R}{4R}$$
*   **Galvanometer Current:**
    $$\mathbf{I_g = \frac{E_o}{R_o + G} = \frac{E \cdot \Delta R}{4R (R + G)}}$$
    *(Exact unbalance voltage: $E_o = E \frac{\Delta R}{4R + 2\Delta R}$)*.

#### Advantages & Limitations of Wheatstone Bridge
*   **Advantages:**
    *   Null measurement $\implies$ independent of galvanometer calibration.
    *   High precision for medium resistances ($1\ \Omega - 100\ \text{k}\Omega$).
*   **Limitations:**
    *   Fails at Low $R$ ($< 1\ \Omega$) due to lead & contact resistances.
    *   Fails at High $R$ ($> 100\ \text{k}\Omega$) due to low current / insufficient sensitivity.
    *   $I^2 R$ heating shifts resistor values.
    *   Thermoelectric EMFs at bimetallic junctions introduce offset.

---

### 2.5 Carey-Foster Slide-Wire Bridge

![[Pasted image 20260922141505.png|391]]

#### Objective & Setup
*   **Purpose:** Measure small difference between two nearly equal medium resistances $(R - S)$.
*   **Feature:** Eliminates end contact resistances ($\alpha, \beta$) and connecting lead resistance.
*   **Parameters:**
    *   $P, Q$: Nearly equal ratio arms.
    *   $R, S$: Resistors under comparison (placed in outer gaps).
    *   $L$: Slide wire length ($100\ \text{cm}$).
    *   $\rho$: Resistance per unit length of slide wire ($\Omega/\text{cm}$).
    *   $\alpha, \beta$: End corrections at left and right extremes.

#### Working & Derivation
1.  **First Balance (Null length $l_1$ with $R$ left, $S$ right):**
    $$\frac{P}{Q} = \frac{R + \alpha + l_1 \rho}{S + \beta + (L - l_1)\rho}$$
    Add 1 to both sides (componendo):
    $$\frac{P + Q}{Q} = \frac{R + S + \alpha + \beta + L\rho}{S + \beta + (L - l_1)\rho} \quad \text{--- (1)}$$
2.  **Second Balance (Swap $R$ and $S$; Null length $l_2$):**
    $$\frac{P}{Q} = \frac{S + \alpha + l_2 \rho}{R + \beta + (L - l_2)\rho}$$
    Add 1 to both sides:
    $$\frac{P + Q}{Q} = \frac{R + S + \alpha + \beta + L\rho}{R + \beta + (L - l_2)\rho} \quad \text{--- (2)}$$
3.  **Equating Denominators of (1) and (2):**
    $$S + \beta + (L - l_1)\rho = R + \beta + (L - l_2)\rho$$
    $$S - l_1 \rho = R - l_2 \rho$$
    $$\mathbf{R - S = (l_2 - l_1)\rho}$$
*   **Result:** $\alpha, \beta$, and $P, Q$ values drop out entirely.

---

## 3. Measurement of Low Resistance

### 3.1 Four-Terminal Resistor
*   Two **Current Terminals** (outer): Carry main circuit current; contact drop excluded from measurement.
*   Two **Potential Terminals** (inner): Connect to voltage detector; carry negligible current $\implies$ zero drop across contacts.

---

### 3.2 Modified Kelvin Double Bridge

![[Pasted image 20260922155604.png]]

#### Circuit Elements
*   $R$: Unknown low resistance.
*   $S$: Standard low resistance.
*   $P, Q$: Outer ratio arms.
*   $p, q$: Inner ratio arms.
*   $r$: Resistance of connecting link between $R$ and $S$.
*   $G$: Sensitive galvanometer.

#### Derivation (Without $P/Q = p/q$ Approximation)
1.  **Current in Inner Divider:**
    Link resistance $r$ is in parallel with $(p + q)$:
    $$I_3 = I_1 \frac{r}{p + q + r}$$
2.  **Voltage Drop Balance:**
    At null ($I_g = 0$): $V_{ab} = V_{amd}$ and $V_{bc} = V_{dnc}$.
    $$P I_2 = R I_1 + p I_3 = R I_1 + \frac{p \cdot r \cdot I_1}{p + q + r}$$
    $$Q I_2 = S I_1 + q I_3 = S I_1 + \frac{q \cdot r \cdot I_1}{p + q + r}$$
3.  **Divide Equations:**
    $$\frac{P}{Q} = \frac{R + \frac{p \cdot r}{p + q + r}}{S + \frac{q \cdot r}{p + q + r}}$$
    $$P \left[ S + \frac{q r}{p + q + r} \right] = Q \left[ R + \frac{p r}{p + q + r} \right]$$
    $$Q R = P S + \frac{P q r - Q p r}{p + q + r} = P S + \frac{Q q r}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]$$
4.  **General Expression:**
    $$\mathbf{R = \frac{P}{Q} S + \frac{q \cdot r}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]}$$
5.  **Elimination of Link Resistance ($r$):**
    If ratio arms are precisely matched such that $\mathbf{\frac{P}{Q} = \frac{p}{q}}$:
    $$\mathbf{R = \frac{P}{Q} S}$$
    *Effect of connecting lead resistance $r$ is completely eliminated.*

---

## 4. Measurement of High Resistance & Insulation

### 4.1 Loss of Charge Method

![[Pasted image 20260922133614.png|458]]

#### Principle & Derivation
*   **Concept:** Capacitor $C$ charges to voltage $V$, then discharges through unknown high resistance $R$.
*   **Discharge Equation:**
    $$v_c = V e^{-t / RC}$$
*   **Solving for $R$:**
    $$\ln\left(\frac{V}{v_c}\right) = \frac{t}{RC} \implies R = \frac{t}{C \ln(V / v_c)}$$
*   **Base-10 Form:**
    $$\mathbf{R = \frac{0.4343 \cdot t}{C \log_{10}(V / v_c)}}$$

#### Accounting for Capacitor Leakage Resistance ($R_1$)
*   Capacitor has internal leakage $R_1$; combined discharge path is $R' = R \parallel R_1$.
1.  **Test 1 (Capacitor alone):**
    $$R_1 = \frac{0.4343 \cdot t_1}{C \log_{10}(V / v_1)}$$
2.  **Test 2 (Capacitor in parallel with unknown $R$):**
    $$R' = \frac{0.4343 \cdot t_2}{C \log_{10}(V / v_2)}$$
3.  **True Insulation Resistance ($R$):**
    $$\frac{1}{R} = \frac{1}{R'} - \frac{1}{R_1} \implies \mathbf{R = \frac{R' R_1}{R_1 - R'}}$$

---

### 4.2 Megger (Insulation Tester)

![[Pasted image 20260922172757.png|414]] ![[Pasted image 20260922173151.png|425]]

#### Construction
*   **Hand-Driven DC Generator:** Permanent magnet, $100\ \text{V} - 2500\ \text{V}$; centrifugal clutch maintains constant speed.
*   **Permanent Magnet Moving System (Ratio Meter):**
    *   No controlling spring; torque exerted entirely electrodynamically.
    *   **Control Coil (Pressure Coil B):** Connected in series with $R_2$ across generator terminals; produces clockwise torque towards $\infty$.
    *   **Deflecting Coil (Current Coil A):** Connected in series with $R_1$ and test terminals ($L$ and $E$); produces counter-clockwise torque towards $0$.
*   **Guard Terminal ($G$):** Intercepts surface leakage current over cable insulation; shunts it directly back to generator, bypassing Coil A.

#### Working Principle & Equations
*   Deflecting torque: $T_d \propto I_A \propto \frac{V}{R_x + R_1}$.
*   Controlling torque: $T_c \propto I_B \propto \frac{V}{R_2}$.
*   At equilibrium:
    $$\theta \propto \frac{I_A}{I_B} \propto \frac{R_2}{R_x + R_1}$$
*   **Key Property:** Ratio is independent of generator output voltage $V$.
*   **Extreme Cases:**
    *   $R_x = \infty$ (Open): $I_A = 0 \implies$ Pointer rests at $\mathbf{\infty}$.
    *   $R_x = 0$ (Short): $I_A$ maximum $\implies$ Pointer swings to $\mathbf{0}$.

---

### 4.3 Earth Resistance (Fall of Potential Method)

![[Pasted image 20260922181539.png|252]] ![[Pasted image 20260922181650.png]]
![[Pasted image 20260922181913.png|470]]

#### Factors Affecting Earth Resistance
*   Soil resistivity ($\rho_s$), moisture content, soil temperature, depth & area of electrode, chemical salts in soil.

#### Three-Electrode Fall of Potential Procedure
*   **Electrodes:**
    *   $E$ (Electrode 1): Earth electrode under test.
    *   $B$ / $C$ (Electrode 2): Current spike (fixed at distance $D$, typically $30 - 50\ \text{m}$).
    *   $A$ / $P$ (Electrode 3): Potential spike (movable, placed at distance $X$ between $E$ and $B$).
*   **Operation:**
    *   Inject current $I$ between $E$ and $B$.
    *   Measure potential $V$ between $E$ and $A$.
    *   Compute $R = V / I$ for various positions $X$.
*   **Plateau Concept:**
    *   Near $E$: Potential rises steeply (resistance zone of $E$).
    *   Near $B$: Potential rises steeply (resistance zone of $B$).
    *   **Middle Plateau Zone:** Flat curve where overlapping field gradient $\approx 0$.
    *   True earth resistance $\mathbf{R_E}$ is measured in this flat region (theoretical neutral point at $X \approx 0.618 \cdot D$).

---

## 5. Localization of Cable Faults

### 5.1 Cable Fault Types
1.  **Ground / Earth Fault:** Conductor insulation breaks down to earth/sheath.
2.  **Short-Circuit Fault:** Insulation breaks down between two conductors.
3.  **Open-Circuit Fault:** Conductor physically breaks (break in continuity).

---

### 5.2 Murray Loop Test

![[Pasted image 20260922191511.png]]

#### Setup & Operation
*   Requires a **sound cable** running parallel to the **faulty cable**.
*   Far end: Sound cable and faulty cable bridged with low-resistance shorting jumper.
*   Test end: Ratio arms $P$ (or $R_1$) and $Q$ (or $R_2$) form Wheatstone bridge with cable loop.
*   $L$: Cable length ($\text{m}$ or $\text{km}$).
*   $x$: Distance to fault from testing end.
*   $r$: Resistance per unit length. Total loop resistance $R_{\text{loop}} = 2 r L$.

#### Derivation (Ground Fault)
*   Arm 1: $P$
*   Arm 2: $Q$
*   Arm 3 (Fault to jumper + sound cable): $r(L - x) + r L = r(2L - x)$
*   Arm 4 (Test end to fault): $r x$
*   Bridge balance:
    $$\frac{P}{Q} = \frac{r(2L - x)}{r x} = \frac{2L - x}{x}$$
    $$\frac{P + Q}{Q} = \frac{2L}{x}$$
    $$\mathbf{x = \frac{Q}{P + Q} \cdot 2L}$$
    *(Note: If arms configured with $P$ adjacent to $r x$: $x = \frac{P}{P + Q} \cdot 2L$).*

#### Case of Cables with Different Resistances
*   Faulty cable resistance: $r_f\ (\Omega/\text{km})$. Sound cable resistance: $r_s\ (\Omega/\text{km})$.
*   Total loop resistance: $R_{\text{loop}} = (r_s + r_f) L$.
*   Resistance to fault: $R_x = r_f x$.
    $$\frac{P + Q}{Q} = \frac{R_{\text{loop}}}{R_x} \implies R_x = \frac{Q}{P + Q} (r_s + r_f) L$$
    $$\mathbf{x = \frac{Q}{P + Q} \cdot \frac{(r_s + r_f)}{r_f} L}$$

#### Short-Circuit Fault Setup
*   Battery connected to the second faulty core instead of earth. Equations remain identical.

#### Modified Setup (Known Resistor $R_{\text{ext}}$ Replaces Sound Cable)
*   Balance condition:
    $$\frac{P}{Q} = \frac{R_{\text{ext}} + r(L - x)}{r x} \implies \mathbf{x = \frac{Q (R_{\text{ext}} + r L)}{r (P + Q)}}$$

---

### 5.3 Varley Loop Test

![[Pasted image 20260922192210.png|517]]

#### Feature
*   Ratio arms $P$ and $Q$ remain **fixed** (often $P = Q$).
*   Balance achieved using variable standard resistor $S$.

#### Procedure (Two-Step Test)
*   **Step 1 (Switch $K \rightarrow 2$, Loop Resistance Test):**
    Battery grounded through switch at terminal $D$. Loop resistance $R_{\text{loop}}$ measured:
    For $P = Q$:
    $$R_{\text{loop}} = S_1$$
*   **Step 2 (Switch $K \rightarrow 1$, Fault Localization):**
    Battery grounded through earth fault. Bridge balanced at setting $S_2$:
    $$\frac{P}{Q} = \frac{R_{\text{loop}} - R_x}{R_x + S_2}$$
    For $P = Q$:
    $$R_{\text{loop}} - R_x = R_x + S_2 \implies 2 R_x = R_{\text{loop}} - S_2 = S_1 - S_2$$
    $$\mathbf{R_x = \frac{S_1 - S_2}{2}}$$
*   **Distance to Fault ($x$):**
    $$\mathbf{x = \frac{R_x}{r} = \frac{S_1 - S_2}{2 r}}$$
*   **General Case ($P \neq Q$):**
    $$\mathbf{R_x = \frac{Q \cdot R_{\text{loop}} - P \cdot S_2}{P + Q}}$$

---

## 6. AC Bridges (Inductance, Capacitance & Frequency)

### 6.1 General AC Bridge Balance Condition
$$Z_1 Z_4 = Z_2 Z_3$$
*   **Magnitude Condition:** $|Z_1||Z_4| = |Z_2||Z_3|$
*   **Phase Condition:** $\angle \theta_1 + \angle \theta_4 = \angle \theta_2 + \angle \theta_3$
*   *Two independent balance conditions required (Real and Imaginary parts).*

---

### 6.2 Bridge Comparison Guide

| Bridge | Primary Use | Standard Element | Unknown Expression | $Q$-Factor / Frequency Range |
| :--- | :--- | :--- | :--- | :--- |
| **Maxwell Inductance** | Inductance | Variable $L_2$ | $L_1 = \frac{R_3}{R_4} L_2$ | Medium $Q$ |
| **Maxwell-Wien** | Inductance | Parallel $C_4, R_4$ | $L_1 = R_2 R_3 C_4$ | Medium $Q$ ($1 < Q < 10$) |
| **Hay's** | Inductance | Series $C_4, R_4$ | $L_1 \approx R_2 R_3 C_4$ | **High $Q$** ($Q > 10$) |
| **Owen's** | Inductance / Steel | Series $C_2, R_2$ & pure $C_4$ | $L_1 = R_2 R_3 C_4$ | Wide range, incremental $\mu$ |
| **De Sauty's** | Capacitance | Pure $C_2$ | $C_1 = \frac{R_4}{R_3} C_2$ | Lossless capacitors only |
| **Modified De Sauty**| Capacitance | Series $C_2, R_2$ | $\frac{C_1}{C_2} = \frac{R_4}{R_3}$ | Imperfect capacitors ($D_1 - D_2$) |
| **Wien's** | Frequency | $R, C$ network | $f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}$ | Audio frequencies ($100\ \text{Hz} - 100\ \text{kHz}$) |

---

### 6.3 Maxwell's Inductance Bridge

![[Pasted image 20260922235031.png|431]] ![[Pasted image 20260922235234.png|432]]

#### Balance Equations
$$L_1 = \frac{R_3}{R_4} L_2, \quad R_1 = \frac{R_3}{R_4}(R_2 + r_2)$$
*   **Drawback:** Requires a calibrated standard variable mutual/self inductor $L_2$ (bulky, expensive).

---

### 6.4 Maxwell-Wien (Capacitance) Bridge

![[Pasted image 20260922235307.png|457]] ![[Pasted image 20260922235319.png]]
![[Pasted image 20260707154328.png]]

#### Derivation
*   $Z_1 = R_1 + j\omega L_1$, $Z_2 = R_2$, $Z_3 = R_3$, $Y_4 = \frac{1}{R_4} + j\omega C_4$.
*   Balance: $Z_1 = Z_2 Z_3 Y_4$:
    $$R_1 + j\omega L_1 = R_2 R_3 \left( \frac{1}{R_4} + j\omega C_4 \right)$$
*   **Balance Formulas:**
    $$\mathbf{R_1 = \frac{R_2 R_3}{R_4}}, \quad \mathbf{L_1 = R_2 R_3 C_4}$$
*   **Storage Factor ($Q$):**
    $$Q = \frac{\omega L_1}{R_1} = \omega C_4 R_4$$

#### Why Unsuitable for High $Q$ ($Q > 10$)?
*   For High $Q$, $R_4 = \frac{Q}{\omega C_4} \propto Q$.
*   If $Q > 10$, $R_4$ becomes extremely large (several megaohms) $\implies$ expensive, bulky, prone to stray capacitive leakage.
#### Why Unsuitable for Low $Q$ ($Q < 1$)?
*   Severe sliding balance occurs (balance controls interact excessively).

---

### 6.5 Hay's Bridge (High $Q$ Coils, $Q > 10$)

![[Pasted image 20260923000043.png|656]]

#### Setup & Derivation
*   Arm 4 uses $C_4$ in **series** with $R_4 \implies Z_4 = R_4 - \frac{j}{\omega C_4}$.
*   Balance: $Z_1 Z_4 = Z_2 Z_3$:
    $$(R_1 + j\omega L_1)\left( R_4 - \frac{j}{\omega C_4} \right) = R_2 R_3$$
    $$R_1 R_4 + \frac{L_1}{C_4} + j \left( \omega L_1 R_4 - \frac{R_1}{\omega C_4} \right) = R_2 R_3$$
*   **Equating Imaginary Parts:**
    $$\omega L_1 R_4 = \frac{R_1}{\omega C_4} \implies \mathbf{Q = \frac{\omega L_1}{R_1} = \frac{1}{\omega C_4 R_4}}$$
*   **Equating Real Parts:**
    $$R_1 R_4 + \frac{L_1}{C_4} = R_2 R_3$$
    Substitute $R_1 = \frac{\omega L_1}{Q} = \omega^2 L_1 C_4 R_4$:
    $$L_1 \left[ \frac{1 + \omega^2 C_4^2 R_4^2}{C_4} \right] = R_2 R_3 \implies \mathbf{L_1 = \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2} = \frac{R_2 R_3 C_4}{1 + (1/Q^2)}}$$
    $$\mathbf{R_1 = \frac{\omega^2 C_4^2 R_4 R_2 R_3}{1 + \omega^2 C_4^2 R_4^2} = \frac{R_2 R_3 / R_4}{1 + Q^2}}$$

#### Why Hay's Bridge Excels for $Q > 10$:
1.  **Small Resistance Needed:** $R_4 = \frac{1}{\omega C_4 Q} \implies$ For high $Q$, $R_4$ is very small (easily realized).
2.  **Frequency Independence Approximation:**
    For $Q > 10 \implies \frac{1}{Q^2} < \frac{1}{100} = 0.01 \ll 1$:
    $$1 + \frac{1}{Q^2} \approx 1 \implies \mathbf{L_1 \approx R_2 R_3 C_4}$$
    Inductance calculation becomes independent of frequency!

#### Why Unsuited for $Q < 10$:
*   $(1/Q^2)$ term cannot be neglected $\implies L_1$ computation strictly depends on source frequency $\omega$. Supply harmonics cause severe balance errors.

---

### 6.6 Owen's Bridge

![[Pasted image 20260923001741.png|662]]

#### Setup & Derivation
*   $Z_1 = R_1 + j\omega L_1$, $Z_2 = R_2 + \frac{1}{j\omega C_2}$, $Z_3 = R_3$, $Z_4 = \frac{1}{j\omega C_4}$.
*   Balance: $Z_1 Z_4 = Z_2 Z_3$:
    $$(R_1 + j\omega L_1)\left( \frac{1}{j\omega C_4} \right) = \left( R_2 - \frac{j}{\omega C_2} \right) R_3$$
    $$\frac{R_1}{j\omega C_4} + \frac{L_1}{C_4} = R_2 R_3 - \frac{j R_3}{\omega C_2}$$
    Multiply both sides by $j\omega C_4$:
    $$R_1 + j\omega L_1 = \frac{C_4}{C_2} R_3 + j\omega C_4 R_2 R_3$$
*   **Balance Equations:**
    $$\mathbf{R_1 = \frac{C_4}{C_2} R_3}, \quad \mathbf{L_1 = R_2 R_3 C_4}$$
*   **Quality Factor ($Q$):**
    $$Q = \frac{\omega L_1}{R_1} = \omega C_2 R_2$$
*   **Key Advantage:** Completely independent balance controls ($R_2$ varies $L_1$ only; $C_2$ varies $R_1$ only). Excellent for measuring magnetic core loss at audio frequencies.

---

### 6.7 Capacitor Dissipation Factor & De Sauty's Bridge

#### Dissipation Factor ($D$) Concept

| Series Model                                | Parallel Model                                                                            |                                                                          |
| :------------------------------------------ | :---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| ![[Pasted image 20260923010052.png          | 666]]                                                                                     | Dielectric loss creates phase shift angle $\delta$ from ideal $90^\circ$ |
| $Z = r_s - \frac{j}{\omega C_s}$            | $D = \tan \delta = \frac{\text{Energy dissipated / cycle}}{\text{Energy stored / cycle}}$ |                                                                          |
| $\mathbf{D = \tan \delta = \omega C_s r_s}$ | $Q = \frac{1}{D} = \frac{1}{\omega C_s r_s}$                                              |                                                                          |

---

#### Modified De Sauty's Bridge

![[Pasted image 20260923011652.png]]

*   Internal dielectric losses represented by $r_1, r_2$. External series resistors $R_1, R_2$.
*   Balance:
    $$\mathbf{\frac{C_1}{C_2} = \frac{R_4}{R_3} = \frac{R_2 + r_2}{R_1 + r_1}}$$
*   **Dissipation Factor Difference:**
    $$D_1 - D_2 = \omega C_1 r_1 - \omega C_2 r_2 = \mathbf{\omega C_1 \left( \frac{R_3}{R_4} R_2 - R_1 \right)}$$
*   **Why $D$ Cannot Be Accurately Determined:**
    *   Yields only the **difference** $(D_1 - D_2)$; requires knowing standard capacitor's loss angle $\delta_2$ accurately.
    *   Small errors in external large resistances $R_1, R_2$ overwhelm tiny internal resistances $r_1, r_2$.

---

### 6.8 Wien's Bridge (Frequency Measurement)

![[Pasted image 20260923013716.png]]

#### Derivation
*   $Y_1 = \frac{1}{R_1} + j\omega C_1$, $Z_2 = R_2 - \frac{j}{\omega C_2}$, $Z_3 = R_3$, $Z_4 = R_4$.
*   Balance: $Z_2 Y_1 = \frac{R_4}{R_3}$:
    $$\left( R_2 - \frac{j}{\omega C_2} \right)\left( \frac{1}{R_1} + j\omega C_1 \right) = \frac{R_4}{R_3}$$
    $$\frac{R_2}{R_1} + \frac{C_1}{C_2} + j \left( \omega C_1 R_2 - \frac{1}{\omega C_2 R_1} \right) = \frac{R_4}{R_3}$$
*   **Equating Real Parts:**
    $$\mathbf{\frac{R_4}{R_3} = \frac{R_2}{R_1} + \frac{C_1}{C_2}}$$
*   **Equating Imaginary Parts:**
    $$\omega C_1 R_2 = \frac{1}{\omega C_2 R_1} \implies \omega^2 = \frac{1}{R_1 R_2 C_1 C_2}$$
    $$\mathbf{f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}}$$
*   **Standard Symmetrical Case ($R_1 = R_2 = R,\ C_1 = C_2 = C$):**
    $$R_4 = 2 R_3, \quad \mathbf{f = \frac{1}{2\pi R C}}$$

---

### 6.9 Compensated Attenuator (Voltage Divider Bridge)

![[Pasted image 20260722082519.png]]

*   **Criterion for Frequency Independence:** Equal arm time constants:
    $$R_1 C_1 = R_2 C_2$$
*   **Transfer Ratio:**
    $$\frac{V_0}{V_i} = \frac{R_2}{R_1 + R_2} = \frac{C_1}{C_1 + C_2}$$
*   **Calculation Example:**
    *Given:* $R_1 = 900\ \text{k}\Omega$, $R_2 = 100\ \text{k}\Omega$, $C_2 = 45\ \text{pF}$, $\frac{V_0}{V_i} = 0.1$.
    $$C_1 = \frac{R_2 C_2}{R_1} = \frac{100\ \text{k}\Omega \times 45\ \text{pF}}{900\ \text{k}\Omega} = \mathbf{5\ \text{pF}}$$

---

## 7. Numerical Problem Cheat-Sheet

```
+---------------------------------------------------------------------------------------------------+
| 1. Kelvin Bridge Link Correction                                                                  |
|    R = (P/Q)*S + [q*r / (p + q + r)] * [(P/Q) - (p/q)]                                            |
|    S = 100.03 uOhm, P = 100.24 Ohm, Q = 200 Ohm, p = 100.31 Ohm, q = 200 Ohm, r = 700 uOhm      |
|    -> P/Q = 0.501200, p/q = 0.501550                                                              |
|    -> Term 1 = 0.501200 * 100.03 uOhm = 50.1350 uOhm                                              |
|    -> Term 2 = [200 * 700 / 300.31] * [0.501200 - 0.501550] = -0.1632 uOhm                        |
|    -> R = 50.1350 - 0.1632 = 49.97 uOhm                                                           |
+---------------------------------------------------------------------------------------------------+
| 2. Murray Loop Test (Ground Fault)                                                                |
|    x = [Q / (P + Q)] * 2L                                                                         |
|    (a) L = 1000 m, P:Q = 3:1 -> x = [1 / (3 + 1)] * 2000 = 500 m                                  |
|    (b) Different cables: x = [Q / (P + Q)] * [L * (r_s + r_f) / r_f]                              |
|        L = 530 m, r_f = 1.1 Ohm/km, r_s = 2.29 Ohm/km, P:Q = 2.7:1                                |
|        x = [1 / 3.7] * [530 * (2.29 + 1.1) / 1.1] = 441.2 m                                       |
+---------------------------------------------------------------------------------------------------+
| 3. Varley Loop Test (Fault Distance)                                                              |
|    R_x = (S1 - S2) / 2        x = R_x / r                                                         |
|    General: R_x = (Q*R_loop - P*S2) / (P + Q)                                                     |
|    Given: R_loop = 8 Ohm, P = 5 Ohm, Q = 10 Ohm, S2 = 7 Ohm, r = 0.4 Ohm/km                       |
|    -> R_x = [10*(8) - 5*(7)] / (5 + 10) = 45 / 15 = 3 Ohm                                         |
|    -> x = 3 / 0.4 = 7.5 km                                                                        |
+---------------------------------------------------------------------------------------------------+
| 4. Owen's Bridge (Sheet Steel Sample)                                                             |
|    R1 = (C4 / C2) * R3        L1 = R2 * R3 * C4                                                   |
|    R2 = 834 Ohm, R3 = 100 Ohm, C2 = 0.124 uF, C4 = 0.1 uF, f = 2 kHz                             |
|    -> R1 = (0.1 / 0.124) * 100 = 80.65 Ohm                                                        |
|    -> L1 = 834 * 100 * 0.1 uF = 8.34 mH                                                           |
|    -> w = 2*pi*2000 = 12566.4 rad/s                                                              |
|    -> w*L1 = 12566.4 * 8.34e-3 = 104.8 Ohm                                                        |
|    -> |Z1| = sqrt(80.65^2 + 104.8^2) = 132.25 Ohm                                                 |
|    -> Q = w * C2 * R2 = 12566.4 * 0.124e-6 * 834 = 1.30                                           |
+---------------------------------------------------------------------------------------------------+
| 5. Maxwell's Capacitance Bridge                                                                   |
|    R1 = (R2 * R3) / R4        L1 = R2 * R3 * C4        Q = w * C4 * R4                            |
|    R2 = 400 Ohm, R3 = 600 Ohm, R4 = 1000 Ohm, C4 = 0.5 uF, f = 1000 Hz                            |
|    -> R1 = (400 * 600) / 1000 = 240 Ohm                                                           |
|    -> L1 = 400 * 600 * 0.5e-6 = 0.12 H = 120 mH                                                   |
|    -> Q = 2*pi*1000 * 0.5e-6 * 1000 = pi = 3.142                                                 |
+---------------------------------------------------------------------------------------------------+
| 6. Wheatstone Bridge Unbalance Deflection                                                         |
|    E_o = E * [ dR / (4R + 2*dR) ]        theta = S_v * E_o                                        |
|    P = Q = R = S = 10 Ohm, E = 9 V, S_v = 15 deg/V, dR = 1 Ohm                                    |
|    -> E_o = 9 * [ 1 / (40 + 2) ] = 9 / 42 = 0.2143 V                                              |
|    -> theta = 15 * 0.2143 = 3.21 deg                                                              |
+---------------------------------------------------------------------------------------------------+
```
