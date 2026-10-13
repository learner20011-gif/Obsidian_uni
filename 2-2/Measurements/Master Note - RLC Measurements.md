# Master Note: RLC Measurements, Bridges & Cable Faults

---

> [!tip] ⚡ Quick Formula Cheat-Sheet (Exam Problem Solver)
> *Instant reference when a numerical problem appears. Identify the problem type / given values $\to$ pick the formula.*

### 🎯 Problem-Solving Formula Decision Matrix

| Problem / Target Question                                   | Given Variables                                                     | Core Formula to Use                                                                                             | Key Trap / Tip                                                                                                                                                                            |
| :---------------------------------------------------------- | :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ammeter-Voltmeter Method (Which connection?)**            | $R_a$ (ammeter), $R_v$ (voltmeter)                                  | Threshold $R_{\text{th}} = \sqrt{R_a R_v}$                                                                      | $R_x > R_{\text{th}} \implies$ Connect v acrs src ($R_{\text{meas}} = R_x + R_a$)<br>$R_x < R_{\text{th}} \implies$ Connect voltmeter across load ($R_{\text{meas}} = R_x \parallel R_v$) |
| **Wheatstone Unbalance Voltage ($E_{\text{Th}}$ or $E_o$)** | Battery $E$, Nominal arm $R$, Deviation $\Delta R$                  | $$E_o = E \left[ \frac{\Delta R}{4R + 2\Delta R} \right] \approx \frac{E}{4} \left(\frac{\Delta R}{R}\right)$$  | Exact form uses $4R + 2\Delta R$; linear approx uses $4R$.                                                                                                                                |
| **Galvanometer Deflection ($\theta$ or $d$)**               | Voltage sens. $S_v$ or Current sens. $S_i$, $R_{\text{Th}}, G$      | $$\theta = S_v \cdot E_o \quad\text{or}\quad I_g = \frac{E_o}{R_{\text{Th}} + G}, \ \theta = S_i I_g$$          | $R_{\text{Th}} = \frac{P R}{P+R} + \frac{Q S}{Q+S} = R$ (for equal arms $R$).                                                                                                             |
| **Carey-Foster Bridge Difference ($X - Y$)**                | Slide wire res/length $\rho$, Balance lengths $l_1, l_2$            | $$X - Y = \rho (l_2 - l_1)$$                                                                                    | Eliminates end lead resistance without knowing absolute end values!                                                                                                                       |
| **Kelvin Double Bridge (Exact Low $R$)**                    | Standard $S$, link $r$, ratios $P/Q$, $p/q$                         | $$R = \frac{P}{Q}S + \frac{qr}{p+q+r}\left( \frac{P}{Q} - \frac{p}{q} \right)$$                                 | Link error disappears if $\frac{P}{Q} = \frac{p}{q}$ or link resistance $r \to 0$.                                                                                                        |
| **Loss of Charge (Insulation $R$)**                         | Cap $C$, time $t$, initial $V_1$, final $V_2$                       | $$R = \frac{t}{C \ln(V_1 / V_2)} = \frac{0.4343\, t}{C \log_{10}(V_1 / V_2)}$$                                  | If cap itself leaks ($R_1$): $\frac{1}{R_{\text{meas}}} = \frac{1}{R_{\text{ins}}} + \frac{1}{R_1}$.                                                                                      |
| **Earth Resistance Fall of Potential**                      | Current $I$, Potential probe voltage $V$                            | $$R_E = \frac{V}{I}$$                                                                                           | True resistance plateau at distance $d \approx 61.8\%$ of total spacing.                                                                                                                  |
| **Murray Loop: Ground Fault ($x$)**                         | Route length $L$, Bridge ratio arms $P, Q$                          | $$x = \left(\frac{Q}{P+Q}\right) 2L$$                                                                           | Fault on sound loop return side. If $P=Q \implies x = L$.                                                                                                                                 |
| **Murray Loop: Different Cable Resistances**                | Length $L$, sound rate $r_s$, fault rate $r_f$, $P, Q$              | $$x = \left(\frac{Q}{P+Q}\right) \left[ \frac{L(r_s + r_f)}{r_f} \right]$$                                      | Remember $r_s, r_f$ in $\Omega/\text{km}$; $x$ comes out in same units as $L$.                                                                                                            |
| **Varley Loop: Fault Distance ($x$)**                       | Loop test $R_{\text{loop}}$, balance $S_2$, ratio $P, Q$, cable $r$ | $$R_x = \frac{Q R_{\text{loop}} - P S_2}{P + Q} \implies x = \frac{R_x}{r}$$                                    | If equal arms ($P=Q$): $R_x = \frac{S_1 - S_2}{2}$ (where $S_1 = R_{\text{loop}}$).                                                                                                       |
| **Maxwell-Wien Bridge ($L_1, R_1, Q$)**                     | $R_2, R_3, R_4, C_4, \omega$                                        | $$L_1 = R_2 R_3 C_4, \quad R_1 = \frac{R_2 R_3}{R_4}, \quad Q = \omega C_4 R_4$$                                | **Medium $Q$ only ($1 \le Q \le 10$)**. Balance independent of frequency.                                                                                                                 |
| **Hay's Bridge ($L_1, R_1, Q$)**                            | $R_2, R_3, R_4, C_4, \omega$                                        | $$L_1 = \frac{R_2 R_3 C_4}{1 + (1/Q^2)} \approx R_2 R_3 C_4, \quad Q = \frac{1}{\omega C_4 R_4}$$               | **High $Q$ coils ($Q > 10$)**. Series $R_4-C_4$ arm. Frequency dependent!                                                                                                                 |
| **Owen's Bridge ($L_1, R_1, Q$)**                           | $R_2, R_3, C_2, C_4, \omega$                                        | $$R_1 = \left(\frac{C_4}{C_2}\right)R_3, \quad L_1 = R_2 R_3 C_4, \quad Q = \omega C_2 R_2$$                    | Ideal for iron-cored coils & magnetic specimens over wide range.                                                                                                                          |
| **De Sauty's Bridge (Capacitance $C_1$)**                   | Standard $C_2$, resistors $R_3, R_4$                                | $$C_1 = C_2 \left(\frac{R_4}{R_3}\right)$$                                                                      | Lossless caps only. For lossy caps: $\frac{R_1+r_1}{R_2+r_2} = \frac{R_3}{R_4} = \frac{C_2}{C_1}$.                                                                                        |
| **Wien's Bridge (Unknown Frequency $f$)**                   | $R_1, R_2, C_1, C_2$                                                | $$f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}} \quad \xrightarrow{R_1=R_2, C_1=C_2} \quad f = \frac{1}{2\pi R C}$$ | Arm ratio must satisfy: $\frac{R_4}{R_3} = \frac{C_1}{C_2} + \frac{R_2}{R_1} = 2$.                                                                                                        |
| **Compensated Attenuator (Voltage Divider)**                | Resistors $R_1, R_2$, Capacitors $C_1, C_2$                         | $$R_1 C_1 = R_2 C_2 \implies C_1 = \frac{R_2 C_2}{R_1}$$                                                        | Frequency-independent attenuation ratio $\frac{V_o}{V_{\text{in}}} = \frac{R_2}{R_1 + R_2}$.                                                                                              |

---

## 1. Resistance Classification & Overview

| Class            | Value Range                         | Major Measurement Methods                                                                             | Dominant Error / Challenge        |
| :--------------- | :---------------------------------- | :---------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Low**    | $< 1\ \Omega$                     | Kelvin Double Bridge, Ammeter-Voltmeter (Low$R$), Potentiometer | Contact & lead resistance ($r$) |                                   |
| **Medium** | $1\ \Omega - 100\ \text{k}\Omega$ | Wheatstone Bridge, Carey-Foster Bridge, Substitution, Ammeter-Voltmeter                               | Contact resistance at lower limit |
| **High**   | $> 100\ \text{k}\Omega$           | Loss of Charge, Megger, Direct Deflection, Megaohm Bridge                                             | Insulation leakage currents       |

---

## 2. Measurement of Medium Resistance

### 2.1 Methods Summary

* **Wheatstone Bridge:** Precision null method for $1\ \Omega - 100\ \text{k}\Omega$.
* **Carey-Foster Slide-Wire Bridge:** Difference of two nearly equal resistances; eliminates lead errors.
* **Substitution Method:** Replaces $R$ with standard $S$ until $I$ matches; avoids meter calibration error.
* **Ammeter-Voltmeter Method:** Simple; needs correction for meter internal resistances.
* **Ohmmeter:** Quick, rough estimate ($\pm 5\%$).

---

### 2.2 Substitution Method

![[Pasted image 20260922140749.png|469]]

#### Circuit & Working

* **Components:** DC source, regulating rheostat $r$, ammeter $A$, switch, unknown $R$, standard decade box $S$.
* **Step 1:** Switch $\rightarrow$ Pos 1 (connect $R$). Adjust $r$ for deflection $I$:
  $$
  I = \frac{E}{R + r + R_a}
  $$
* **Step 2:** Switch $\rightarrow$ Pos 2 (connect $S$). Adjust $S$ until ammeter reads same $I$:
  $$
  I = \frac{E}{S + r + R_a}
  $$
* **Result:**
  $$
  R = S
  $$
* **Advantage:** Eliminates ammeter calibration errors completely.
* **Condition:** Supply $E$ and rheostat $r$ must remain strictly constant.

---

### 2.3 Ammeter-Voltmeter Method (Error Analysis)

![[Pasted image 20260922163156.png]]

#### Comparison of Connections

| Parameter                                  | Connection (a): Ammeter Near$R$                           | Connection (b): Voltmeter Across$R$                           |
| :----------------------------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------- |
| **Diagram**                          | Voltmeter measures$(V_a + V_R)$; Ammeter measures $I_R$ | Ammeter measures$(I_v + I_R)$; Voltmeter measures $V_R$     |
| **Measured Value**                   | $R_m = \frac{V}{I} = R + R_a$                             | $R_m = \frac{V}{I} = \frac{R R_v}{R + R_v}$                   |
| **True Value**                       | $R = R_m - R_a$                                           | $R = \frac{R_m R_v}{R_v - R_m} = \frac{R_m}{1 - (R_m / R_v)}$ |
| **Relative Error $\varepsilon_r$** | $\varepsilon_r = \frac{R_m - R}{R} = +\frac{R_a}{R}$      | $\varepsilon_r = \frac{R_m - R}{R} \approx -\frac{R}{R_v}$    |
| **Best Suited For**                  | **High / Upper-Medium $R$** ($R \gg R_a$)         | **Low / Lower-Medium $R$** ($R \ll R_v$)              |

#### Threshold Resistance Criterion

* Equate magnitudes of relative errors:
  $$
  \frac{R_a}{R} = \frac{R}{R_v} \implies R^2 = R_a R_v \implies R_{\text{cross}} = \sqrt{R_a R_v}
  $$
* **Decision Rule:**
  * If $R > \sqrt{R_a R_v} \longrightarrow$ Use **Connection (a)**.
  * If $R < \sqrt{R_a R_v} \longrightarrow$ Use **Connection (b)**.

> [!EXAMPLE] Selection Example
> *Given:* $R \approx 80\ \Omega$, $R_a = 1.5\ \Omega$, $R_v = 4000\ \Omega$.
> *Criterion:* $\sqrt{R_a R_v} = \sqrt{1.5 \times 4000} = \sqrt{6000} \approx 77.46\ \Omega$.
> *Decision:* Since $80\ \Omega > 77.46\ \Omega \implies$ **Connection (a)** gives smaller relative error.

---

### 2.4 Wheatstone Bridge Sensitivity & Galvanometer Equations

#### Bridge Balance Condition

$$
\frac{P}{Q} = \frac{R}{S} \implies R = \frac{P}{Q} S
$$

#### Bridge Sensitivity ($S_B$)

* **Definition:** Galvanometer deflection per unit fractional change in unknown $R$:
  $$
  S_B = \frac{\theta}{\Delta R / R}
  $$
* **Voltage Sensitivity of Galvanometer:** $S_v = \frac{\theta}{E_o}\ (\text{mm/V or deg/V})$.

#### Derivation of General Bridge Sensitivity

1. **Unbalance Thevenin Voltage ($E_o$):**

   $$
   E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{P}{P + Q} \right]
   $$

   At initial balance: $\frac{P}{P+Q} = \frac{R}{R+S}$.
   $$
   E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{R}{R + S} \right] = \frac{E \cdot S \cdot \Delta R}{(R + S)^2 + \Delta R(R + S)}
   $$

   For small unbalance ($\Delta R \ll R+S$):
   $$
   E_o \approx \frac{E \cdot S \cdot \Delta R}{(R + S)^2}
   $$
2. ✅**Galvanometer Deflection ($\theta$):**

   $$
   \theta = S_v \cdot E_o = S_v \frac{E \cdot S \cdot \Delta R}{(R + S)^2}
   $$
3. **Bridge Sensitivity Formula:**

   $$
   S_B = \frac{\theta}{\Delta R / R} = \frac{S_v \cdot E \cdot S \cdot R}{(R + S)^2} = \frac{S_v E}{\frac{(R + S)^2}{SR}} = \frac{S_v E}{\frac{R}{S} + 2 + \frac{S}{R}}
   $$

   Substitute balance ratio $\frac{R}{S} = \frac{P}{Q}$ and $\frac{S}{R} = \frac{Q}{P}$:
   ✅$$
   \mathbf{S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}}
   $$

#### Equal-Arm Condition ($P = Q = R = S$)

$$
S_B = \frac{S_v E}{1 + 1 + 2} = \mathbf{\frac{S_v E}{4}}
$$

* **Condition for Maximum Sensitivity:** $\frac{P}{Q} = 1$ (equal ratio arms).

#### Galvanometer Current ($I_g$) for Small Unbalance

* **Thevenin Resistance ($R_o$):**
  $$
  R_o = (P \parallel Q) + (R \parallel S) = \frac{PQ}{P + Q} + \frac{RS}{R + S}
  $$
* **Equal Arms ($P = Q = R = S$):**
  $$
  R_o = \frac{R}{2} + \frac{R}{2} = R, \quad E_o \approx \frac{E \Delta R}{4R}
  $$
* **Galvanometer Current:**
  $$
  \mathbf{I_g = \frac{E_o}{R_o + G} = \frac{E \cdot \Delta R}{4R (R + G)}}
  $$

  *(Exact unbalance voltage: $E_o = E \frac{\Delta R}{4R + 2\Delta R}$)*.

#### Advantages & Limitations of Wheatstone Bridge

* **Advantages:**
  * Null measurement $\implies$ independent of galvanometer calibration.
  * High precision for medium resistances ($1\ \Omega - 100\ \text{k}\Omega$).
* **Limitations:**
  * Fails at Low $R$ ($< 1\ \Omega$) due to lead & contact resistances.
  * Fails at High $R$ ($> 100\ \text{k}\Omega$) due to low current / insufficient sensitivity.
  * $I^2 R$ heating shifts resistor values.
  * Thermoelectric EMFs at bimetallic junctions introduce offset.

---

### 2.5 Carey-Foster Slide-Wire Bridge

![[Pasted image 20260922141505.png|391]]

#### Objective & Setup

* **Purpose:** Measure small difference between two nearly equal medium resistances $(R - S)$.
* **Feature:** Eliminates end contact resistances ($\alpha, \beta$) and connecting lead resistance.
* **Parameters:**
  * $P, Q$: Nearly equal ratio arms.
  * $R, S$: Resistors under comparison (placed in outer gaps).
  * $L$: Slide wire length ($100\ \text{cm}$).
  * $\rho$: Resistance per unit length of slide wire ($\Omega/\text{cm}$).
  * $\alpha, \beta$: End corrections at left and right extremes.

#### Working & Derivation

1. **First Balance (Null length $l_1$ with $R$ left, $S$ right):**

   $$
   \frac{P}{Q} = \frac{R + \alpha + l_1 \rho}{S + \beta + (L - l_1)\rho}
   $$

   Add 1 to both sides (componendo):
   $$
   \frac{P + Q}{Q} = \frac{R + S + \alpha + \beta + L\rho}{S + \beta + (L - l_1)\rho} \quad \text{--- (1)}
   $$
2. **Second Balance (Swap $R$ and $S$; Null length $l_2$):**

   $$
   \frac{P}{Q} = \frac{S + \alpha + l_2 \rho}{R + \beta + (L - l_2)\rho}
   $$

   Add 1 to both sides:
   $$
   \frac{P + Q}{Q} = \frac{R + S + \alpha + \beta + L\rho}{R + \beta + (L - l_2)\rho} \quad \text{--- (2)}
   $$
3. **Equating Denominators of (1) and (2):**

   $$
   S + \beta + (L - l_1)\rho = R + \beta + (L - l_2)\rho
   $$

   $$
   S - l_1 \rho = R - l_2 \rho
   $$

   $$
   \mathbf{R - S = (l_2 - l_1)\rho}
   $$

* **Result:** $\alpha, \beta$, and $P, Q$ values drop out entirely.

---

## 3. Measurement of Low Resistance

### 3.1 Four-Terminal Resistor

* Two **Current Terminals** (outer): Carry main circuit current; contact drop excluded from measurement.
* Two **Potential Terminals** (inner): Connect to voltage detector; carry negligible current $\implies$ zero drop across contacts.

---

### 3.2 Modified Kelvin Double Bridge

![[Pasted image 20260922155604.png]]

#### Circuit Elements

* $R$: Unknown low resistance.
* $S$: Standard low resistance.
* $P, Q$: Outer ratio arms.
* $p, q$: Inner ratio arms.
* $r$: Resistance of connecting link between $R$ and $S$.
* $G$: Sensitive galvanometer.

#### Derivation (Without $P/Q = p/q$ Approximation)

1. **Current in Inner Divider:**
   Link resistance $r$ is in parallel with $(p + q)$:

   $$
   I_3 = I_1 \frac{r}{p + q + r}
   $$
2. **Voltage Drop Balance:**
   At null ($I_g = 0$): $V_{ab} = V_{amd}$ and $V_{bc} = V_{dnc}$.

   $$
   P I_2 = R I_1 + p I_3 = R I_1 + \frac{p \cdot r \cdot I_1}{p + q + r}
   $$

   $$
   Q I_2 = S I_1 + q I_3 = S I_1 + \frac{q \cdot r \cdot I_1}{p + q + r}
   $$
3. **Divide Equations:**

   $$
   \frac{P}{Q} = \frac{R + \frac{p \cdot r}{p + q + r}}{S + \frac{q \cdot r}{p + q + r}}
   $$

   $$
   P \left[ S + \frac{q r}{p + q + r} \right] = Q \left[ R + \frac{p r}{p + q + r} \right]
   $$

   $$
   Q R = P S + \frac{P q r - Q p r}{p + q + r} = P S + \frac{Q q r}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]
   $$
4. **General Expression:**

   $$
   \mathbf{R = \frac{P}{Q} S + \frac{q \cdot r}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]}
   $$
5. **Elimination of Link Resistance ($r$):**
   If ratio arms are precisely matched such that $\mathbf{\frac{P}{Q} = \frac{p}{q}}$:

   $$
   \mathbf{R = \frac{P}{Q} S}
   $$

   *Effect of connecting lead resistance $r$ is completely eliminated.*

---

## 4. Measurement of High Resistance & Insulation

### 4.1 Loss of Charge Method

![[Pasted image 20260922133614.png|458]]

#### Principle & Derivation

* **Concept:** Capacitor $C$ charges to voltage $V$, then discharges through unknown high resistance $R$.
* **Discharge Equation:**
  $$
  v_c = V e^{-t / RC}
  $$
* **Solving for $R$:**
  $$
  \ln\left(\frac{V}{v_c}\right) = \frac{t}{RC} \implies R = \frac{t}{C \ln(V / v_c)}
  $$
* **Base-10 Form:**
  $$
  \mathbf{R = \frac{0.4343 \cdot t}{C \log_{10}(V / v_c)}}
  $$

#### Accounting for Capacitor Leakage Resistance ($R_1$)

* Capacitor has internal leakage $R_1$; combined discharge path is $R' = R \parallel R_1$.

1. **Test 1 (Capacitor alone):**
   $$
   R_1 = \frac{0.4343 \cdot t_1}{C \log_{10}(V / v_1)}
   $$
2. **Test 2 (Capacitor in parallel with unknown $R$):**
   $$
   R' = \frac{0.4343 \cdot t_2}{C \log_{10}(V / v_2)}
   $$
3. **True Insulation Resistance ($R$):**
   $$
   \frac{1}{R} = \frac{1}{R'} - \frac{1}{R_1} \implies \mathbf{R = \frac{R' R_1}{R_1 - R'}}
   $$

---

### 4.2 Megger (Insulation Tester)

![[Pasted image 20260922172757.png|414]] ![[Pasted image 20260922173151.png|425]]

#### Construction

* **Hand-Driven DC Generator:** Permanent magnet, $100\ \text{V} - 2500\ \text{V}$; centrifugal clutch maintains constant speed.
* **Permanent Magnet Moving System (Ratio Meter):**
  * No controlling spring; torque exerted entirely electrodynamically.
  * **Control Coil (Pressure Coil B):** Connected in  series with $R_2$ and parallel across generator terminals; produces **counter clockwise torque towards $\infty$**.
  * **Deflecting Coil (Current Coil A):** Connected in series with $R_1$ and test terminals ($L$ and $E$); produces **clockwise torque towards $0$**.
* **Guard Terminal ($G$):** Intercepts surface leakage current over cable insulation; shunts it directly back to generator, bypassing Coil A.

#### Working Principle & Equations

* Deflecting torque: $T_d \propto I_A \propto \frac{V}{R_x + R_1}$.
* Controlling torque: $T_c \propto I_B \propto \frac{V}{R_2}$.
* At equilibrium:
  $$
  \theta \propto \frac{I_A}{I_B} \propto \frac{R_2}{R_x + R_1}
  $$
* **Key Property:** Ratio is independent of generator output voltage $V$.
* **Extreme Cases:**
  * $R_x = \infty$ (Open): $I_A = 0 \implies$ Pointer rests at $\mathbf{\infty}$.
  * $R_x = 0$ (Short): $I_A$ maximum $\implies$ Pointer swings to $\mathbf{0}$.

---

### 4.3 Earth Resistance (Fall of Potential Method)

![[Pasted image 20260922181539.png|252]] ![[Pasted image 20260922181650.png]]
![[Pasted image 20260922181913.png|470]]

#### Factors Affecting Earth Resistance

* Soil resistivity ($\rho_s$), moisture content, soil temperature, depth & area of electrode, chemical salts in soil.

#### Three-Electrode Fall of Potential Procedure

* **Electrodes:**
  * $E$ (Electrode 1): Earth electrode under test.
  * $B$ / $C$ (Electrode 2): Current spike (fixed at distance $D$, typically $30 - 50\ \text{m}$).
  * $A$ / $P$ (Electrode 3): Potential spike (movable, placed at distance $X$ between $E$ and $B$).
* **Operation:**
  * Inject current $I$ between $E$ and $B$.
  * Measure potential $V$ between $E$ and $A$.
  * Compute $R = V / I$ for various positions $X$.
* **Plateau Concept:**
  * Near $E$: Potential rises steeply (resistance zone of $E$).
  * Near $B$: Potential rises steeply (resistance zone of $B$).
  * **Middle Plateau Zone:** Flat curve where overlapping field gradient $\approx 0$.
  * True earth resistance $\mathbf{R_E}$ is measured in this flat region (theoretical neutral point at $X \approx 0.618 \cdot D$).

---

## 5. Localization of Cable Faults

### 5.1 Cable Fault Types

1. **Ground / Earth Fault:** Conductor insulation breaks down to earth/sheath.
2. **Short-Circuit Fault:** Insulation breaks down between two conductors.
3. **Open-Circuit Fault:** Conductor physically breaks (break in continuity).

---

### 5.2 Murray Loop Test

![[Pasted image 20260922191511.png]]

#### Setup & Operation

* Requires a **sound cable** running parallel to the **faulty cable**.
* Far end: Sound cable and faulty cable bridged with low-resistance shorting jumper.
* Test end: Ratio arms $P$ (or $R_1$) and $Q$ (or $R_2$) form Wheatstone bridge with cable loop.
* $L$: Cable length ($\text{m}$ or $\text{km}$).
* $x$: Distance to fault from testing end.
* $r$: Resistance per unit length. Total loop resistance $R_{\text{loop}} = 2 r L$.

#### Derivation (Ground Fault)

* Arm 1: $P$
* Arm 2: $Q$
* Arm 3 (Fault to jumper + sound cable): $r(L - x) + r L = r(2L - x)$
* Arm 4 (Test end to fault): $r x$
* Bridge balance:

  $$
  \frac{P}{Q} = \frac{r(2L - x)}{r x} = \frac{2L - x}{x}
  $$

  $$
  \frac{P + Q}{Q} = \frac{2L}{x}
  $$

  ✅$$
  \mathbf{x = \frac{Q}{P + Q} \cdot 2L}
  $$

  *(Note: If arms configured with $P$ adjacent to $r x$: $x = \frac{P}{P + Q} \cdot 2L$).*

#### Case of Cables with Different Resistances

* Faulty cable resistance: $r_f\ (\Omega/\text{km})$. Sound cable resistance: $r_s\ (\Omega/\text{km})$.
* Total loop resistance: $R_{\text{loop}} = (r_s + r_f) L$.
* Resistance to fault: $R_x = r_f x$.
$$\frac{P}{Q} = \frac{R_{\text{rem}}}{R_x}$$

To express this in terms of the total loop resistance $R_{\text{loop}}$, apply the componendo rule (adding 1 to both sides):

$$\frac{P}{Q} + 1 = \frac{R_{\text{rem}}}{R_x} + 1$$

$$\frac{P + Q}{Q} = \frac{R_{\text{rem}} + R_x}{R_x}$$

Since $R_{\text{rem}} + R_x = R_{\text{loop}}$:
  $$
  \frac{P + Q}{Q} = \frac{R_{\text{loop}}}{R_x} \implies R_x = \frac{Q}{P + Q} (r_s + r_f) L
  $$

  $$
  \mathbf{x = \frac{Q}{P + Q} \cdot \frac{(r_s + r_f)}{r_f} L}
  $$

#### Short-Circuit Fault Setup

* Battery connected to the second faulty core instead of earth. Equations remain identical.


---

### 5.3 Varley Loop Test

![[Pasted image 20260922192210.png|517]]

#### Feature

* Ratio arms $P$ and $Q$ remain **fixed** (often $P = Q$).
* Balance achieved using variable standard resistor $S$.

#### Procedure (Two-Step Test)

* **Step 1 (Switch $K \rightarrow 2$, Loop Resistance Test):**
  Battery grounded through switch at terminal $D$. Loop resistance $R_{\text{loop}}$ measured:


$$
  \frac{P}{Q} = \frac{R_{\text{loop}}}{ S_1}
  $$
* **Step 2 (Switch $K \rightarrow 1$, Fault Localization):**
  Battery grounded through earth fault. Bridge balanced at setting $S_2$:

* ✅**General Case ($P \neq Q$):**

  $$
  \mathbf{R_x = \frac{Q \cdot R_{\text{loop}} - P \cdot S_2}{P + Q}}
  $$

---

## 6. AC Bridges (Inductance, Capacitance & Frequency)

### 6.1 General AC Bridge Balance Condition

$$
Z_1 Z_4 = Z_2 Z_3
$$

* **Magnitude Condition:** $|Z_1||Z_4| = |Z_2||Z_3|$
* **Phase Condition:** $\angle \theta_1 + \angle \theta_4 = \angle \theta_2 + \angle \theta_3$
* *Two independent balance conditions required (Real and Imaginary parts).*

---

### 6.2 Bridge Comparison Guide

| Bridge                       | Primary Use        | Standard Element                  | Unknown Expression                                                                                       | $Q$-Factor / Frequency Range    |
| :--------------------------- | :----------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| **Maxwell Inductance** | Inductance         | Variable$L_2$                   | $L_1 = \frac{R_3}{R_4} L_2$                                                                            | Medium$Q$                       |
| **Maxwell-Wien**       | Inductance         | Parallel$C_4, R_4$              | $L_1 = R_2 R_3 C_4$                                                                                    | Medium$Q$ ($1 < Q < 10$)      |
| **Hay's**              | Inductance         | Series$C_4, R_4$                | $L_1 \approx R_2 R_3 C_4$                                                                              | **High $Q$** ($Q > 10$) |
| **Owen's**             | Inductance / Steel | Series$C_2, R_2$ & pure $C_4$ | $L_1 = R_2 R_3 C_4$                                                                                    | Wide range, incremental$\mu$    |
| **De Sauty's**         | Capacitance        | Pure$C_2$                       | $C_1 = \frac{R_4}{R_3} C_2$                                                                            | Lossless capacitors only          |
| **Modified De Sauty**  | Capacitance        | Series$C_2, R_2$                | $\frac{C_1}{C_2} = \frac{R_4}{R_3}$ | Imperfect capacitors ($D_1 - D_2$)                             |                                   |
| **Wien's**             | Frequency          | $R, C$ network                  | $f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}$ | Audio frequencies ($100\ \text{Hz} - 100\ \text{kHz}$) |                                   |

---

### 6.3 Maxwell's Inductance Bridge

![[Pasted image 20260922235031.png|431]] ![[Pasted image 20260922235234.png|432]]

#### Balance Equations

$$
L_1 = \frac{R_3}{R_4} L_2, \quad R_1 = \frac{R_3}{R_4}(R_2 + r_2)
$$

* **Drawback:** Requires a calibrated standard variable mutual/self inductor $L_2$ (bulky, expensive).

---

### 6.4 Maxwell-Wien (Capacitance) Bridge

![[Pasted image 20260922235307.png|457]] ![[Pasted image 20260922235319.png]]
![[Pasted image 20260707154328.png]]

#### Derivation

* $Z_1 = R_1 + j\omega L_1$, $Z_2 = R_2$, $Z_3 = R_3$, $Z_4$.
* Balance: $Z_1 Z_4= Z_2 Z_3$:
* **Balance Formulas:**
  $$
  \mathbf{R_1 = \frac{R_2 R_3}{R_4}}, \quad \mathbf{L_1 = R_2 R_3 C_4}
  $$
* **Storage Factor ($Q$):**
  $$
  Q = \frac{\omega L_1}{R_1} = \omega C_4 R_4
  $$

#### Why Unsuitable for High $Q$ ($Q > 10$)?

* For High $Q$, $R_4 = \frac{Q}{\omega C_4} \propto Q$.
* If $Q > 10$, $R_4$ becomes extremely large (several megaohms) $\implies$ expensive, bulky, prone to stray capacitive leakage.

#### Why Unsuitable for Low $Q$ ($Q < 1$)?

* Severe sliding balance occurs (balance controls interact excessively).

---

### 6.5 Hay's Bridge (High $Q$ Coils, $Q > 10$)

![[Pasted image 20260923000043.png|656]]

#### Setup & Derivation

* Arm 4 uses $C_4$ in **series** with $R_4 \implies Z_4 = R_4 - \frac{j}{\omega C_4}$.
* Balance: $Z_1 Z_4 = Z_2 Z_3$:

  $$
  (R_1 + j\omega L_1)\left( R_4 - \frac{j}{\omega C_4} \right) = R_2 R_3
  $$

  $$
  R_1 R_4 + \frac{L_1}{C_4} + j \left( \omega L_1 R_4 - \frac{R_1}{\omega C_4} \right) = R_2 R_3
  $$
* **Equating Imaginary Parts:**

  $$
  \omega L_1 R_4 = \frac{R_1}{\omega C_4} \implies \mathbf{Q = \frac{\omega L_1}{R_1} = \frac{1}{\omega C_4 R_4}}
  $$
* **Equating Real Parts:**

  $$
  R_1 R_4 + \frac{L_1}{C_4} = R_2 R_3
  $$

  Substitute $R_1 = \frac{\omega L_1}{Q} = \omega^2 L_1 C_4 R_4$:
  $$
  L_1 \left[ \frac{1 + \omega^2 C_4^2 R_4^2}{C_4} \right] = R_2 R_3 \implies \mathbf{L_1 = \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2} = \frac{R_2 R_3 C_4}{1 + (1/Q^2)}}
  $$

  $$
  \mathbf{R_1 = \frac{\omega^2 C_4^2 R_4 R_2 R_3}{1 + \omega^2 C_4^2 R_4^2} = \frac{R_2 R_3 / R_4}{1 + Q^2}}
  $$

#### Why Hay's Bridge Excels for $Q > 10$:

1. **Small Resistance Needed:** $R_4 = \frac{1}{\omega C_4 Q} \implies$ For high $Q$, $R_4$ is very small (easily realized).
2. **Frequency Independence Approximation:**
   For $Q > 10 \implies \frac{1}{Q^2} < \frac{1}{100} = 0.01 \ll 1$:
   $$
   1 + \frac{1}{Q^2} \approx 1 \implies \mathbf{L_1 \approx R_2 R_3 C_4}
   $$

   Inductance calculation becomes independent of frequency!

#### Why Unsuited for $Q < 10$:

* $(1/Q^2)$ term cannot be neglected $\implies L_1$ computation strictly depends on source frequency $\omega$. Supply harmonics cause severe balance errors.

---

### 6.6 Owen's Bridge

![[Pasted image 20260923001741.png|662]]

#### Setup & Derivation

* $Z_1 = R_1 + j\omega L_1$, $Z_2 = R_2 + \frac{1}{j\omega C_2}$, $Z_3 = R_3$, $Z_4 = \frac{1}{j\omega C_4}$.
* Balance: $Z_1 Z_4 = Z_2 Z_3$:

  $$
  (R_1 + j\omega L_1)\left( \frac{1}{j\omega C_4} \right) = \left( R_2 - \frac{j}{\omega C_2} \right) R_3
  $$

  $$
  \frac{R_1}{j\omega C_4} + \frac{L_1}{C_4} = R_2 R_3 - \frac{j R_3}{\omega C_2}
  $$

  Multiply both sides by $j\omega C_4$:
  $$
  R_1 + j\omega L_1 = \frac{C_4}{C_2} R_3 + j\omega C_4 R_2 R_3
  $$
* **Balance Equations:**

  $$
  \mathbf{R_1 = \frac{C_4}{C_2} R_3}, \quad \mathbf{L_1 = R_2 R_3 C_4}
  $$
* **Quality Factor ($Q$):**

  $$
  Q = \frac{\omega L_1}{R_1} = \omega C_2 R_2
  $$
* **Key Advantage:** Completely independent balance controls ($R_2$ varies $L_1$ only; $C_2$ varies $R_1$ only). Excellent for measuring magnetic core loss at audio frequencies.

---

### 6.7 Capacitor Dissipation Factor & De Sauty's Bridge

#### Dissipation Factor ($D$) Concept

| Series Model                                | Parallel Model                                                                            |                                                                         |
| :------------------------------------------ | :---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| ![[Pasted image 20260923010052.png]]        |                                                                                           | Dielectric loss creates phase shift angle$\delta$ from ideal $90^\circ$ |
| $Z = r_s - \frac{j}{\omega C_s}$            | $D = \tan \delta = \frac{\text{Energy dissipated / cycle}}{\text{Energy stored / cycle}}$ |                                                                         |
| $\mathbf{D = \tan \delta = \omega C_s r_s}$ | $Q = \frac{1}{D} = \frac{1}{\omega C_s r_s}$                                              |                                                                         |
|                                             |                                                                                           |                                                                         |
|                                             |                                                                                           |                                                                         |
*   The total applied voltage ($V$) is the vector sum of $V_R$ and $V_C$.
*   The angle between the total voltage $V$ and the ideal capacitive voltage $V_C$ is called the **loss angle, $\delta$**.

$$D = \tan(\delta) = \frac{V_R}{V_C} = \frac{I \cdot R_s}{I / (\omega C_s)} = \omega R_s C_s$$
---

#### Modified De Sauty's Bridge

![[Pasted image 20260923011652.png]]

* Internal dielectric losses represented by $r_1, r_2$. External series resistors $R_1, R_2$.

* **Dissipation Factor Difference:**
  $$D_1 = \omega C_1 \left[ \frac{R_3}{R_4}(R_2 + r_2) - R_1 \right]$$
$$D_1 - D_2 = \omega C_2 R_2 - \omega C_1 R_1$$
  
* **Why $D$ Cannot Be Accurately Determined:**
  * Yields only the **difference** $(D_1 - D_2)$; requires knowing standard capacitor's loss angle $\delta_2$ accurately.
  * Small errors in external large resistances $R_1, R_2$ overwhelm tiny internal resistances $r_1, r_2$.

---

### 6.8 Wien's Bridge (Frequency Measurement)

![[Pasted image 20260923013716.png]]

#### Derivation

* $Y_1 = \frac{1}{R_1} + j\omega C_1$, $Z_2 = R_2 - \frac{j}{\omega C_2}$, $Z_3 = R_3$, $Z_4 = R_4$.
* Balance: $Z_2 Y_1 = \frac{R_4}{R_3}$:

  $$
  \left( R_2 - \frac{j}{\omega C_2} \right)\left( \frac{1}{R_1} + j\omega C_1 \right) = \frac{R_4}{R_3}
  $$

  $$
  \frac{R_2}{R_1} + \frac{C_1}{C_2} + j \left( \omega C_1 R_2 - \frac{1}{\omega C_2 R_1} \right) = \frac{R_4}{R_3}
  $$
* **Equating Real Parts:**

  $$
  \mathbf{\frac{R_4}{R_3} = \frac{R_2}{R_1} + \frac{C_1}{C_2}}
  $$
* **Equating Imaginary Parts:**

  $$
  \omega C_1 R_2 = \frac{1}{\omega C_2 R_1} \implies \omega^2 = \frac{1}{R_1 R_2 C_1 C_2}
  $$

  $$
  \mathbf{f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}}
  $$
* **Standard Symmetrical Case ($R_1 = R_2 = R,\ C_1 = C_2 = C$):**

  $$
  R_4 = 2 R_3, \quad \mathbf{f = \frac{1}{2\pi R C}}
  $$

---

### 6.9 Compensated Attenuator (Voltage Divider Bridge)

![[Pasted image 20260722082519.png]]![[Pasted image 20261013050355.jpg|193]]

* **Criterion for Frequency Independence:** Equal arm time constants:
  $$
  R_1 C_1 = R_2 C_2
  $$
* **Transfer Ratio:**
  $$
  \frac{V_0}{V_i} = \frac{R_2}{R_1 + R_2} = \frac{C_1}{C_1 + C_2}
  $$
* **Calculation Example:**
  *Given:* $R_1 = 900\ \text{k}\Omega$, $R_2 = 100\ \text{k}\Omega$, $C_2 = 45\ \text{pF}$, $\frac{V_0}{V_i} = 0.1$.
  $$
  C_1 = \frac{R_2 C_2}{R_1} = \frac{100\ \text{k}\Omega \times 45\ \text{pF}}{900\ \text{k}\Omega} = \mathbf{5\ \text{pF}}
  $$

---

## 7. Numerical Problem Cheat-Sheet

> [!example] 1. Kelvin Double Bridge — Link Correction & Exact $R$
> **Core Formula:**
> $$R = \frac{P}{Q} S + \frac{qr}{p + q + r} \left( \frac{P}{Q} - \frac{p}{q} \right)$$
> *   **Given:**
>     *   Standard resistance: $S = 100.03\ \mu\Omega$
>     *   Link resistance: $r = 700\ \mu\Omega$
>     *   Outer arms: $P = 100.24\ \Omega$, $Q = 200\ \Omega \implies \frac{P}{Q} = 0.501200$
>     *   Inner arms: $p = 100.31\ \Omega$, $q = 200\ \Omega \implies \frac{p}{q} = 0.501550$
> *   **Step-by-Step Calculation:**
>     *   $\text{Main Term} = \frac{P}{Q} S = 0.501200 \times 100.03\ \mu\Omega = 50.1350\ \mu\Omega$
>     *   $\text{Correction Term} = \left[ \frac{200 \times 700\ \mu\Omega}{100.31 + 200 + 0.0007} \right] \times (0.501200 - 0.501550) = \frac{140000}{300.31} \times (-0.000350) = -0.1632\ \mu\Omega$
>     *   $R = 50.1350\ \mu\Omega - 0.1632\ \mu\Omega = \mathbf{49.97\ \mu\Omega}$

> [!example] 2. Murray Loop Test — Ground Fault Location
> **Core Formula:**
> $$x = \left( \frac{Q}{P + Q} \right) 2L \quad \text{(identical cables)} \qquad\Big|\qquad x = \left( \frac{Q}{P + Q} \right) \cdot \frac{L(r_s + r_f)}{r_f} \quad \text{(different cables)}$$
> *   **(a) Identical sound & faulty cables:**
>     *   **Given:** Length $L = 1000\ \text{m}$, ratio $\frac{P}{Q} = \frac{3}{1} \implies P = 3Q$
>     *   **Result:**
>         $$x = \left(\frac{1}{3 + 1}\right) \times (2 \times 1000\ \text{m}) = \frac{2000}{4} = \mathbf{500\ \text{m}}$$
> *   **(b) Different cable sizes / resistances:**
>     *   **Given:** $L = 530\ \text{m}$, fault cable $r_f = 1.1\ \Omega/\text{km}$, sound cable $r_s = 2.29\ \Omega/\text{km}$, ratio $\frac{P}{Q} = 2.7 \implies Q = 1, P = 2.7$
>     *   **Result:**
>         $$x = \left( \frac{1}{2.7 + 1} \right) \left[ 530 \times \frac{2.29 + 1.1}{1.1} \right] = \frac{1}{3.7} \times \left[ 530 \times \frac{3.39}{1.1} \right] = \mathbf{441.2\ \text{m}}$$

> [!example] 3. Varley Loop Test — Fault Resistance & Distance
> **Core Formula:**
> $$R_x = \frac{Q \cdot R_{\text{loop}} - P \cdot S_2}{P + Q} \qquad\text{and}\qquad x = \frac{R_x}{r}$$
> *(For equal ratio arms $P = Q \implies R_x = \frac{S_1 - S_2}{2}$)*
> *   **Given:**
>     *   Loop resistance: $R_{\text{loop}} = 8\ \Omega$ (measured in loop test)
>     *   Ratio arms: $P = 5\ \Omega$, $Q = 10\ \Omega$
>     *   Variable resistance at balance: $S_2 = 7\ \Omega$
>     *   Conductor resistance: $r = 0.4\ \Omega/\text{km}$
> *   **Step-by-Step Calculation:**
>     *   $R_x = \frac{(10 \times 8) - (5 \times 7)}{5 + 10} = \frac{80 - 35}{15} = \frac{45}{15} = 3\ \Omega$
>     *   Fault distance: $x = \frac{R_x}{r} = \frac{3\ \Omega}{0.4\ \Omega/\text{km}} = \mathbf{7.5\ \text{km}}$

> [!example] 4. Owen's Bridge — Sheet Steel Sample Analysis
> **Core Formulas:**
> $$R_1 = \left( \frac{C_4}{C_2} \right) R_3 \qquad L_1 = R_2 R_3 C_4 \qquad Q = \omega C_2 R_2$$
> *   **Given:**
>     *   $R_2 = 834\ \Omega$, $R_3 = 100\ \Omega$
>     *   $C_2 = 0.124\ \mu\text{F}$, $C_4 = 0.1\ \mu\text{F}$, $f = 2\ \text{kHz}$
>     *   $\omega = 2\pi f = 2\pi \times 2000 = 12566.4\ \text{rad/s}$
> *   **Step-by-Step Calculation:**
>     *   $R_1 = \left(\frac{0.1\ \mu\text{F}}{0.124\ \mu\text{F}}\right) \times 100\ \Omega = \mathbf{80.65\ \Omega}$
>     *   $L_1 = 834 \times 100 \times 0.1 \times 10^{-6}\ \text{H} = 8.34 \times 10^{-3}\ \text{H} = \mathbf{8.34\ \text{mH}}$
>     *   $\omega L_1 = 12566.4 \times 8.34 \times 10^{-3} = 104.8\ \Omega$
>     *   Sample impedance: $|Z_1| = \sqrt{R_1^2 + (\omega L_1)^2} = \sqrt{80.65^2 + 104.8^2} = \mathbf{132.25\ \Omega}$
>     *   Quality factor: $Q = \omega C_2 R_2 = 12566.4 \times 0.124 \times 10^{-6} \times 834 = \mathbf{1.30}$

> [!example] 5. Maxwell's Inductance-Capacitance Bridge
> **Core Formulas:**
> $$R_1 = \frac{R_2 R_3}{R_4} \qquad L_1 = R_2 R_3 C_4 \qquad Q = \omega C_4 R_4 = \frac{\omega L_1}{R_1}$$
> *   **Given:**
>     *   $R_2 = 400\ \Omega$, $R_3 = 600\ \Omega$, $R_4 = 1000\ \Omega$
>     *   $C_4 = 0.5\ \mu\text{F}$, $f = 1000\ \text{Hz} \implies \omega = 2\pi(1000) = 6283.18\ \text{rad/s}$
> *   **Step-by-Step Calculation:**
>     *   $R_1 = \frac{400 \times 600}{1000} = \mathbf{240\ \Omega}$
>     *   $L_1 = 400 \times 600 \times (0.5 \times 10^{-6}) = 0.12\ \text{H} = \mathbf{120\ \text{mH}}$
>     *   $Q = 2\pi \times 1000 \times (0.5 \times 10^{-6}) \times 1000 = \pi \approx \mathbf{3.142}$

> [!example] 6. Wheatstone Bridge Unbalance & Galvanometer Deflection
> **Core Formulas:**
> $$E_{\text{Th}} = E_o = E \left[ \frac{\Delta R}{4R + 2\Delta R} \right] \qquad \theta = S_v \cdot E_o$$
> *   **Given:**
>     *   Nominal bridge arms: $P = Q = R = S = 10\ \Omega$
>     *   Bridge battery: $E = 9\ \text{V}$
>     *   Detector voltage sensitivity: $S_v = 15^\circ/\text{V}$
>     *   Resistance deviation: $\Delta R = 1\ \Omega$
> *   **Step-by-Step Calculation:**
>     *   Open-circuit output voltage:
>         $$E_o = 9 \times \left[ \frac{1}{4(10) + 2(1)} \right] = 9 \times \frac{1}{42} = \mathbf{0.2143\ \text{V}}$$
>     *   Galvanometer deflection:
>         $$\theta = 15^\circ/\text{V} \times 0.2143\ \text{V} = \mathbf{3.21^\circ}$$
