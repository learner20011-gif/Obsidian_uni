Here are the concise notes based strictly on the provided document, covering pages 1 to 30, including the key mathematical derivations.

---

# Measurement & Instrumentation (Pages 1–30)

## 1. Classification of Measuring Instruments
**Essential Requirements of Measuring Instruments:**
*   Its introduction into a circuit must not alter circuit conditions.
*   Power consumed by the instrument must be small.

**Analog Instruments:**
Devices where the output/display is a continuous function of time with a constant relation to the input.
*   **By Current Kind:** DC, AC, or both (AC/DC).
*   **By Effect:** Indicating (shows magnitude), Recording (keeps a continuous record, e.g., substation voltmeter), Integrating (totalizes events over time, e.g., energy meter).
*   **By Comparison Method:** 
    *   *Direct Measuring:* Converts measurand directly to actuate the instrument (Ammeters, Voltmeters).
    *   *Comparison:* Measures by comparing with a standard (AC/DC bridges).

*Note: All analog ammeters and voltmeters (except electrostatic) depend on a deflecting torque produced by an electric current. Thus, they are essentially current-measuring devices.*

---

## 2. Galvanometer (d'Arsonval / PMMC type)
**Purpose:** Detects/measures small currents and voltages; used for null deflection in bridges and potentiometers.
**Construction:**
*   **Moving Coil:** Current-carrying part, freely moves about its vertical axis.
*   **Permanent Magnet:** Interacts with the coil's magnetic field to produce torque.
*   **Iron Core:** Provides a low reluctance flux path for a strong magnetic field.
*   **Suspension & Mirror:** Ribbon suspension carries current; mirror casts a beam of light on a scale.
*   **Torsion Head:** Adjusts zero setting.

### **Torque Equation Derivation:**
Let $l, d$ = length and width of the coil, $N$ = turns, $B$ = flux density, $i$ = current, $K$ = spring constant, $A = l \times d$ (Area).
1.  Force on each side of the coil: $F = NBil$
2.  Deflecting Torque ($T_d$) = Force × Distance: 
    $$T_d = NBild = NBAi$$
3.  Let $G$ = Displacement constant ($G = NBA = NBld$). Therefore:
    $$T_d = Gi$$
4.  Controlling Torque ($T_c$) exerted by suspension at final deflection $\theta_F$: 
    $$T_c = K\theta_F$$
5.  **Final Steady Deflection** (At balance $T_d = T_c$):
    $$Gi = K\theta_F \implies \theta_F = \frac{Gi}{K}$$

---

## 3. Permanent Magnet Moving Coil (PMMC) Instruments
**Construction:** Similar to Galvanometer but uses a rectangular aluminum former pivoted on jeweled bearings. The aluminum former provides **electromagnetic damping**. Control torque is provided by phosphor bronze hair springs.

### **Torque Equation:**
Follows the exact same derivation as the Galvanometer.
*   Deflecting Torque: $T_d = GI$
*   Controlling Torque: $T_c = K\theta$
*   **Final Deflection:** $\theta = (\frac{G}{K})I$ (Since $G$ and $K$ are constant, the scale is completely linear).

**Advantages:** High accuracy, very low power consumption, linear scale, adaptable for different ranges.
**Disadvantages:** **Used only for DC**, higher cost than other instruments, susceptible to friction and heating errors.

---

## 4. Electrostatic Instruments
**Principle:** Deflecting torque is produced by the electric field on charged conductors. Mechanism resembles a **variable capacitor**. The moving electrode tends to move to a position where **stored energy is maximum**. Essentially used as voltmeters.

### **Force & Torque Equation Derivation (Energy Conservation):**
Let $V$ = applied voltage, $C$ = capacitance, $E$ = stored energy = $\frac{1}{2}CV^2$.
If voltage increases by $dV$, plate moves distance $dx$, changing capacitance by $dC$.
1.  Input energy: $Vi dt = V^2 dC + CV dV$
2.  Change in stored energy: $d(\frac{1}{2}CV^2) = \frac{1}{2}V^2dC + CVdV$
3.  Mechanical work done = $F dx$ (Linear) or $T_d d\theta$ (Rotational)
4.  Conservation of Energy: *Input Energy = Increase in Stored Energy + Mechanical work*
    $$V^2 dC + CV dV = \frac{1}{2}V^2 dC + CV dV + F dx$$
5.  **Linear Force:** $F = \frac{1}{2}V^2 \frac{dC}{dx}$
6.  **Rotational Torque:** $T_d = \frac{1}{2}V^2 \frac{dC}{d\theta}$
7.  **Final Deflection** (Spring controlled $T_c = K\theta$):
    $$\theta = \frac{1}{2K}V^2 \frac{dC}{d\theta}$$

**Advantages:** Can be used for AC and DC, low power consumption, free from hysteresis and eddy current loss.
**Disadvantages:** Suitable only for low voltages (per slide text).

---

## 5. Moving Iron (MI) Instruments
**Principle:** A soft iron vane moves in a magnetic field produced by a stationary coil. When excited, the iron moves to increase the flux/inductance (moves from weaker to stronger field, seeking minimum reluctance).

### **General Torque Equation Derivation:**
Let $I$ = initial current, $L$ = inductance, $\theta$ = deflection. Current increases by $dI$, causing deflection $d\theta$ and inductance change $dL$.
1.  Electrical energy supplied = $I^2dL + LIdI$
2.  Change in stored energy = $\frac{1}{2}(I+dI)^2(L+dL) - \frac{1}{2}I^2L \approx LIdI + \frac{1}{2}I^2dL$
3.  Conservation of Energy: *Supplied = Stored + Mechanical Work ($T_d d\theta$)*
    $$I^2dL + LIdI = LIdI + \frac{1}{2}I^2dL + T_d d\theta$$
4.  **Deflecting Torque:** 
    $$T_d = \frac{1}{2}I^2 \frac{dL}{d\theta}$$
5.  **Final Deflection** (Spring controlled $T_c = K\theta$):
    $$\theta = \frac{1}{2K}I^2 \frac{dL}{d\theta}$$
*(Deflection is proportional to the square of the RMS value of the current).*

**Advantages:** Universal use (AC & DC), less friction error, cheap, robust, industrial/precision accuracy.
**Disadvantages:** Non-linear scale, errors due to hysteresis/frequency/stray fields, waveform errors, difference between AC and DC calibrations.

---

## 6. Rectifier Type Instruments
**Principle:** Uses a full-wave bridge rectifier to convert AC to pulsating DC, which drives a PMMC movement.
*   Because of moving coil inertia, the meter indicates steady deflection proportional to the **average value**.
*   It is practically calibrated to display **RMS values** for a sine wave.
*   **Form Factor:** relates RMS to Average ($Form Factor = 1.11$ for a sinusoidal wave).
*   **Limitation:** Highly erroneous if reading non-sinusoidal waveforms.

---

Here are the concise notes based strictly on pages 30 to 53 of the document, complete with all mathematical derivations.

---

# Electrodynamometer Type Instruments (Pages 30–40)

## 1. Introduction & Principle
*   **Need:** Overcomes Moving Iron instrument limitations (calibration differences between AC and DC).
*   **Transfer Instrument:** Can be calibrated on DC and then "transferred" accurately to AC measurements. Used for AC voltmeters, ammeters, wattmeters, power factor meters, etc.
*   **Principle:** If used on AC, a normal PMMC meter would just vibrate at zero due to inertia. In an electrodynamometer, the field flux is reversed simultaneously with the moving coil current (by connecting the fixed and movable coils in series), producing torque in the same direction for both halves of the AC cycle.

## 2. Construction
*   **Fixed Coils:** Produce the field. Divided into two sections for a uniform field. Wound with heavy wire for ammeters/wattmeters or fine wire for voltmeters. Mounted on ceramics to avoid eddy currents.
*   **Moving Coil:** Wound on a non-metallic former (metallic formers induce eddy currents). Both fixed and moving coils are air-cored.
*   **Control & Damping:** Spring control provides restoring torque and acts as current leads. Air friction damping is used via aluminum vanes in sector-shaped chambers.
*   **Shielding:** Because the air-cored magnetic field is weak, stray/earth magnetic fields can cause errors. Protected by enclosing in a double casing of high permeability alloy.

## 3. Torque Equation Derivation (DC Operation)
Let $i_1, i_2$ = instantaneous currents in fixed and moving coils.
$L_1, L_2$ = self-inductances of coils; $M$ = mutual inductance.
1.  **Flux Linkages:** 
    $\lambda_1 = L_1 i_1 + M i_2$
    $\lambda_2 = L_2 i_2 + M i_1$
2.  **Electrical Input Energy:**
    $e_1 i_1 dt + e_2 i_2 dt = i_1 d\lambda_1 + i_2 d\lambda_2$
    $= i_1 d(L_1 i_1 + M i_2) + i_2 d(L_2 i_2 + M i_1)$
    Expanding gives:
    $Input = i_1 L_1 di_1 + i_1^2 dL_1 + i_1 i_2 dM + i_1 M di_2 + i_2 L_2 di_2 + i_2^2 dL_2 + i_2 M di_1 + i_1 i_2 dM$  *(Eq. I)*
3.  **Change in Stored Magnetic Energy:**
    Stored Energy $E = \frac{1}{2} i_1^2 L_1 + \frac{1}{2} i_2^2 L_2 + i_1 i_2 M$
    Differentiating:
    $dE = i_1 L_1 di_1 + \frac{1}{2} i_1^2 dL_1 + i_2 L_2 di_2 + \frac{1}{2} i_2^2 dL_2 + i_1 M di_2 + i_2 M di_1 + i_1 i_2 dM$ *(Eq. II)*
4.  **Conservation of Energy:**
    *Input Energy = Change in Stored Energy + Mechanical Energy*
    Mechanical Energy = Eq. I – Eq. II = $\frac{1}{2} i_1^2 dL_1 + \frac{1}{2} i_2^2 dL_2 + i_1 i_2 dM$
    Since coils are rigid, self-inductances $L_1, L_2$ are constant ($dL_1 = 0, dL_2 = 0$):
    Mechanical Energy = $i_1 i_2 dM$
5.  **Deflecting Torque ($T_i$):**
    Work done = $T_i d\theta = i_1 i_2 dM \implies T_i = i_1 i_2 \frac{dM}{d\theta}$
6.  **For DC (Steady Currents $I_1, I_2$):**
    $T_d = I_1 I_2 \frac{dM}{d\theta}$
    At equilibrium, $T_d = T_c = K\theta$.
    **Final Deflection:** $\theta = \frac{I_1 I_2}{K} \frac{dM}{d\theta}$

## 4. Torque Equation Derivation (AC / Sinusoidal Operation)
Let $i_1 = I_{m1} \sin \omega t$ and $i_2 = I_{m2} \sin(\omega t - \phi)$ (phase difference $\phi$).
1.  **Average Torque ($T_d$):**
    $T_d = \frac{1}{T} \int_0^T i_1 i_2 \frac{dM}{d\theta} dt$
    $T_d = \frac{dM}{d\theta} \frac{1}{T} \int_0^T I_{m1} \sin \omega t \cdot I_{m2} \sin(\omega t - \phi) dt$
    $T_d = \frac{dM}{d\theta} \frac{I_{m1} I_{m2}}{2\pi} \int_0^{2\pi} \sin \omega t \sin(\omega t - \phi) d(\omega t)$
2.  **Solving Integral:**
    $T_d = \frac{I_{m1} I_{m2}}{2} \cos \phi \frac{dM}{d\theta} = I_1 I_2 \cos \phi \frac{dM}{d\theta}$ (where $I_1, I_2$ are RMS values).
3.  **Final Deflection (At Equilibrium $T_d = K\theta$):**
    $\theta = \frac{I_1 I_2}{K} \cos \phi \frac{dM}{d\theta}$

## 5. Advantages & Disadvantages
*   **Advantages:** Free from hysteresis/eddy current errors (air-cored), precision accuracy (40–500 Hz), acts as AC/DC transfer instrument, measures true RMS regardless of waveform.
*   **Disadvantages:** Low sensitivity (low torque/weight ratio), higher cost, sensitive to overloads/impacts, high power consumption (needs high current for field), non-uniform scale, impractical at very low frequencies (5-15 Hz).

---

# Extension of Range (Pages 41–46)

## 1. Ammeters (Shunts)
To measure heavy currents, a low resistance **shunt ($R_{sh}$)** is placed in parallel with the meter resistance ($R_m$).
*   **Derivation:**
    1.  Voltages across parallel branches are equal: $I_{sh} R_{sh} = I_m R_m$
    2.  $R_{sh} = \frac{I_m R_m}{I_{sh}}$
    3.  Total current $I = I_{sh} + I_m \implies I_{sh} = I - I_m$
    4.  Substitute $I_{sh}$: $R_{sh} = \frac{I_m R_m}{I - I_m}$
    5.  Divide by $I_m$: $\frac{R_m}{R_{sh}} = \frac{I}{I_m} - 1 \implies \frac{I}{I_m} = 1 + \frac{R_m}{R_{sh}}$
*   **Multiplying Power of Shunt ($m$):** 
    $m = \frac{I}{I_m} = 1 + \frac{R_m}{R_{sh}}$
*   **Required Shunt Resistance:** $R_{sh} = \frac{R_m}{m - 1}$

## 2. Voltmeters (Multipliers)
To extend voltage range, a high series resistance **multiplier ($R_s$)** is added to limit current.
*   **Derivation:**
    1.  Voltage across meter alone: $v = I_m R_m$
    2.  Full range voltage: $V = I_m (R_m + R_s)$
    3.  Solve for $R_s$: $R_s = \frac{V - I_m R_m}{I_m} = \frac{V}{I_m} - R_m$
*   **Multiplying Factor ($m$):**
    $m = \frac{V}{v} = \frac{I_m(R_m + R_s)}{I_m R_m} = 1 + \frac{R_s}{R_m}$
*   **Required Multiplier Resistance:** $R_s = (m - 1)R_m$
*   *Requirements for Multipliers:* Must not change with time or temperature; must be non-inductively wound for AC.

---

# Ohmmeters & Multimeters (Pages 47–53)

## 1. Ohmmeters
Direct reading devices for approximate resistance measurement.
*   **Series Type Construction:** A d'Arsonval movement is in parallel with an adjustable shunt $R_2$. This block is in series with resistance $R_1$, battery $E$, and unknown resistor $R_x$ (terminals A & B).
*   **Operation:**
    *   $R_x = 0$ (shorted): Max current flows. $R_2$ is adjusted so meter reads full scale ($I_{fs}$). Scale is marked **"0 $\Omega$"**.
    *   $R_x = \infty$ (open): Zero current. Scale is marked **"$\infty$"**.

## 2. Series Ohmmeter Design Derivation (Half-Scale Deflection)
The design centers around the unknown resistance $R_h$ that causes exactly half-scale deflection.
1.  At half-scale, $R_x = R_h$. $R_h$ equals the internal resistance looking into A & B:
    $R_h = R_1 + \frac{R_2 R_m}{R_2 + R_m}$  *(Eq. 8.29)*
2.  Battery current at half-scale: $I_h = \frac{E}{2 R_h}$
3.  Full-scale battery current (when $R_x = 0$): $I_1 = 2 I_h = \frac{E}{R_h}$  *(Eq. 8.32)*
4.  Shunt current at full-scale: $I_2 = I_1 - I_{fs}$  *(Eq. 8.33)*
5.  Voltages across parallel meter and shunt are equal: $I_2 R_2 = I_{fs} R_m \implies R_2 = \frac{I_{fs} R_m}{I_2}$
6.  Substitute (8.33) and (8.32) into $R_2$:
    $R_2 = \frac{I_{fs} R_m}{I_1 - I_{fs}} = \frac{I_{fs} R_m R_h}{E - I_{fs} R_h}$  *(Eq. 8.34)*
7.  Solve (8.29) for $R_1$: 
    $R_1 = R_h - \frac{R_2 R_m}{R_2 + R_m}$
8.  Substitute (8.34) into $R_1$:
    $R_1 = R_h - \frac{I_{fs} R_m R_h}{E}$
    *(Alternatively derived equation: $R_h = \frac{E R_2}{I_{fs}(R_2 + R_m)}$)*

## 3. Multimeter (V.O.M / AVO Meter)
*   **Volt-Ohm-Milli-Ammeter:** Combines ammeter, voltmeter, and ohmmeter functions into one instrument using a single basic d'Arsonval movement.
*   **Mechanism:** A selector/function switch routes the circuit through the appropriate internal shunts or multipliers depending on the measurement mode and range.
*   *Example:* Simpson Model 260 includes specific external jacks for high ranges (e.g., "DC 5000 V").