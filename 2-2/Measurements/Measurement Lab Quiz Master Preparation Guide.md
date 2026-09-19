# EEE 2212: Measurements & Instrumentation Sessional — Master Quiz Prep Guide

> **Target Exam:** Measurement Lab Quiz & Viva  
> **Format Breakdown:**  
> 1. **True / False** (Conceptual nuances, operating limits, polarity & safety traps)  
> 2. **One-Word / Short Theory** (Terminologies, component names, phenomena, units, materials)  
> 3. **Short Maths** (Formula substitution, multiplier calculations, percentage error, meter constants)  
> **Syllabus Reference:** Rajshahi University of Engineering & Technology (RUET) — Dept. of EEE (Course No: EEE 2212)

---

## Quick Formula & Units Master Table

| Experiment / Topic | Key Formula | Standard Units |
| :--- | :--- | :--- |
| **Wheatstone Bridge** | $R = \left(\frac{Q}{P}\right) \cdot S$ | Ohms ($\Omega$) |
| **Percentage Error** | $\%e = \frac{\|R_{\text{actual}} - R_{\text{measured}}\|}{R_{\text{actual}}} \times 100\%$ | $\%$ |
| **Coil Resistance ($R$)** | $R = \frac{W}{I^2}$ | Ohms ($\Omega$) |
| **Impedance ($Z$)** | $Z = \frac{V}{I}$ | Ohms ($\Omega$) |
| **Inductive Reactance ($X_L$)** | $X_L = \sqrt{Z^2 - R^2} = 2\pi f L$ | Ohms ($\Omega$) |
| **Inductance ($L$)** | $L = \frac{X_L}{2\pi f}$ | Henry ($H$) |
| **Capacitive Reactance ($X_C$)** | $X_C = \sqrt{Z^2 - R^2} = \frac{1}{2\pi f C}$ | Ohms ($\Omega$) |
| **Capacitance ($C$)** | $C = \frac{1}{2\pi f X_C}$ | Farad ($F$, $\mu F$) |
| **Potential Transformer Ratio** | $k_{PT} = \frac{V_p}{V_s} \approx \frac{N_1}{N_2}$ | Dimensionless |
| **Current Transformer Ratio** | $k_{CT} = \frac{I_p}{I_s} \approx \frac{N_2}{N_1}$ | Dimensionless |
| **Ammeter Shunt Resistance** | $R_{sh} = \frac{R_m}{m - 1}, \quad m = \frac{I}{I_m}$ | Ohms ($\Omega$) |
| **Voltmeter Multiplier Resistance**| $R_s = (m - 1)R_m, \quad m = \frac{V}{V_m}$ | Ohms ($\Omega$) |
| **Energy Meter Energy (True)** | $E_{\text{true}} = \frac{P \times t}{1000 \times 60}$ (where $t$ is in min, $P$ in W) | $kWh$ |
| **Energy Meter Energy (Recorded)**| $E_{\text{recorded}} = \frac{N_{\text{rev}}}{K_{\text{meter}}}$ | $kWh$ |
| **Meter Constant ($K$)** | $K = \frac{\text{Revolutions}}{kWh}$ | $\text{rev}/kWh$ |
| **True Power with CT & PT** | $P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{reading}}$ | Watts ($W$) / $kW$ |
| **Stroboscope Speed ($N$)** | $N = \frac{f_m \cdot f_1 \cdot (m - 1)}{f_m - f_1}$ | RPM |

---

# Experiment 01: Lab Safety, General Instruments & Pre-Lab Rules

### Core Concepts & Theory
1. **Instrument Categories:**
   - **Absolute (Primary) Instruments:** Give measured quantity in terms of physical constants without comparison to another meter (e.g., Tangent Galvanometer, Rayleigh Current Balance).
   - **Secondary Instruments:** Calibrated against a primary standard (e.g., PMMC, Moving Iron, Digital Multimeter). All standard lab meters are secondary instruments.
2. **Three Essential Torques in Indicating Instruments:**
   - **Deflecting Torque ($T_d$):** Causes the pointer to move from zero position (produced by magnetic, electrodynamic, thermal, or electrostatic effect).
   - **Controlling Torque ($T_c$):** Opposes $T_d$ and brings pointer to a rest when $T_c = T_d$. Provided by **spring control** (phosphor bronze hairsprings) or **gravity control**.
   - **Damping Torque ($T_d'$):** Suppresses oscillations around final steady position so pointer settles quickly. Provided by **eddy current damping** (aluminum former in PMMC), **air friction damping** (Moving Iron), or **fluid friction damping** (electrostatic voltmeters).
3. **Meter Impedance Rule (Loading Effect):**
   - **Ideal Voltmeter:** Infinite input impedance ($R_{in} = \infty$). A real voltmeter must have the highest possible resistance to draw negligible current from the test branch.
   - **Ideal Ammeter:** Zero internal resistance ($R_m = 0$). A real ammeter must have the lowest possible resistance to avoid inserting a voltage drop in the test loop.
4. **Variac (Auto-transformer):**
   - Continuously variable single-winding transformer. The common winding shares magnetic core; used to gradually ramp voltage from $0\text{ V}$ to rated voltage to prevent high inrush currents.

---

### Type 1: True / False (Exp 01)

1. **[T/F]** A secondary instrument requires prior calibration against a primary standard before use.  
   **Answer: TRUE.** Only absolute instruments do not require calibration.
2. **[T/F]** An ideal ammeter has infinite internal resistance.  
   **Answer: FALSE.** An ideal ammeter has **zero** internal resistance. Infinite resistance belongs to an ideal voltmeter.
3. **[T/F]** In a spring-controlled instrument, the controlling torque is directly proportional to deflection angle ($T_c \propto \theta$).  
   **Answer: TRUE.** For gravity control, $T_c \propto \sin\theta$.
4. **[T/F]** Eddy current damping is used in moving-iron (MI) instruments.  
   **Answer: FALSE.** Moving-iron instruments use **air friction damping** because the permanent magnet required for eddy current damping would distort the weak operating field.
5. **[T/F]** A Variac provides galvanic electrical isolation between input and output.  
   **Answer: FALSE.** An autotransformer has a single continuous winding; primary and secondary share a direct conductive connection (no electrical isolation).

---

### Type 2: One-Word / Quick Theory (Exp 01)

1. The instrument error caused by viewing a needle pointer from an angled line of sight:  
   **Parallax error**
2. The material used for hairsprings in PMMC instruments due to its non-magnetic property and low fatigue:  
   **Phosphor bronze**
3. Type of damping used in PMMC instruments:  
   **Eddy current damping**
4. The condition in which an instrument pointer settles to its final value without oscillation in the shortest possible time:  
   **Critically damped**
5. Type of instrument that can measure both AC and DC without changing calibration:  
   **Moving Iron (MI) / Electrodynamometer**
6. Property indicating how closely an instrument reading approaches the true value of the variable:  
   **Accuracy**
7. The smallest change in the input signal that an instrument can reliably detect:  
   **Resolution / Sensitivity threshold**

---

### Type 3: Short Maths (Exp 01)

**Q1:** A $0 - 300\text{ V}$ voltmeter has an accuracy rating of $\pm 1\%$ of full-scale deflection (FSD). Calculate the maximum limiting error when reading $150\text{ V}$.  
**Solution:**  
- Maximum absolute error $= 300 \times 0.01 = \pm 3\text{ V}$.  
- Percentage error at $150\text{ V} = \frac{3\text{ V}}{150\text{ V}} \times 100\% = \mathbf{\pm 2\%}$.

---

# Experiment 02: Unknown Resistance using Wheatstone Bridge

### Core Concepts & Circuit Setup
![Wheatstone Bridge](attachments/meas_exp02_wheatstone_bridge.png)

1. **Working Principle:** Null-deflection method based on balance of a bridge loop.
2. **Balance Condition:** Current through galvanometer is zero ($I_g = 0$) when the potential at opposite nodes is identical:
   $$P \cdot R = Q \cdot S \implies R = \frac{Q}{P} \cdot S$$
   - $P, Q$: Ratio arms (fixed standard precision resistors).
   - $S$: Standard variable arm (resistance box).
   - $R$: Unknown resistance under test.
3. **Limitation of Wheatstone Bridge:**
   - **Range:** Suitable for **medium resistance** ($1\,\Omega$ to $100\,k\Omega$).
   - **Why NOT for Low Resistance ($< 1\,\Omega$):** Contact resistance of terminals and lead wire resistance introduce significant percentage error. (Solution: **Kelvin Double Bridge**).
   - **Why NOT for High Resistance ($> 100\,k\Omega$):** Galvanometer current becomes too small to detect null, and insulation leakage shunts the arms. (Solution: **Megger** or Loss of Charge method).
4. **Galvanometer Sensitivity:** Defined as deflection per unit current ($S_i = \frac{\theta}{I}$ in $\text{div}/\mu\text{A}$ or $\text{mm}/\mu\text{A}$).

---

### Type 1: True / False (Exp 02)

1. **[T/F]** The Wheatstone bridge method is a deflection method.  
   **Answer: FALSE.** It is a **null-comparison** method (independent of galvanometer calibration).
2. **[T/F]** At bridge balance, interchanging the positions of battery and galvanometer leaves the balance condition unchanged.  
   **Answer: TRUE.** This is the reciprocity theorem applied to bridges.
3. **[T/F]** A Wheatstone bridge is recommended for measuring a contact resistance of $0.005\,\Omega$.  
   **Answer: FALSE.** It cannot measure low resistances accurately due to lead/contact resistance.
4. **[T/F]** The sensitivity of a Wheatstone bridge is maximum when all four arms have approximately equal resistance ($P \approx Q \approx R \approx S$).  
   **Answer: TRUE.** Bridge sensitivity drops when arm ratios differ drastically.

---

### Type 2: One-Word / Quick Theory (Exp 02)

1. State the detector used in DC Wheatstone bridge:  
   **D'Arsonval Galvanometer**
2. The bridge configuration specifically used to eliminate lead and contact resistance for measuring low resistance:  
   **Kelvin Double Bridge**
3. The arms $P$ and $Q$ of a Wheatstone bridge are collectively called:  
   **Ratio arms**
4. Unwanted emf generated at junctions of dissimilar metals inside the bridge due to temperature gradients:  
   **Thermoelectric emf (Seebeck effect)**

---

### Type 3: Short Maths (Exp 02)

**Q1:** In a balanced Wheatstone bridge, ratio arm $P = 100\,\Omega$, $Q = 1000\,\Omega$, and variable resistance $S = 47.3\,\Omega$. Find the unknown resistance $R$.  
**Solution:**  
$$R = \frac{Q}{P} \cdot S = \frac{1000}{100} \times 47.3 = 10 \times 47.3 = \mathbf{473\,\Omega}$$

**Q2:** If the nominal (actual) value of a standard resistor is $38.7\,\Omega$ and the bridge measured value is $37.0\,\Omega$, calculate the percentage error.  
**Solution:**  
$$\%e = \frac{|38.7 - 37.0|}{38.7} \times 100\% = \frac{1.7}{38.7} \times 100\% = \mathbf{4.39\%}$$

---

# Experiment 03: Inductance of an Inductor (3-Meter Method)

### Core Concepts & Circuit Setup
![Inductance Measurement Circuit](attachments/meas_exp03_inductance_circuit.png)

1. **Why three meters?** An inductor is practical, meaning it contains both inductive reactance ($X_L$) and winding copper resistance ($R$). A voltmeter gives $V$, an ammeter gives $I$, and an electrodynamometer wattmeter gives true active power ($W$).
2. **Formulas:**
   - Active copper loss: $W = I^2 R \implies R = \frac{W}{I^2}$
   - Total impedance: $Z = \frac{V}{I}$
   - Inductive reactance: $X_L = \sqrt{Z^2 - R^2}$
   - Coil Inductance: $L = \frac{X_L}{2\pi f}$
   - Power Factor: $\cos\phi = \frac{R}{Z}$
3. **Ideal vs Practical:**
   - In an **ideal inductor**, resistance $R = 0$, power loss $W = 0\text{ W}$, and $\cos\phi = 0$ (current lags voltage by $90^\circ$).
   - A **practical inductor** has winding resistance + core eddy/hysteresis losses, causing $W > 0$.
4. **Wattmeter Connection:**
   - **Current Coil (CC):** Low resistance, connected in **series** with the load.
   - **Potential Coil (PC):** High resistance, connected in **parallel** across the load.

---

### Type 1: True / False (Exp 03)

1. **[T/F]** An ideal inductor dissipates non-zero average active power in an AC circuit.  
   **Answer: FALSE.** For an ideal inductor, active power $P = VI\cos(90^\circ) = 0$.
2. **[T/F]** In the three-meter method, the wattmeter measures the reactive power ($Q = VI\sin\phi$).  
   **Answer: FALSE.** A standard wattmeter measures **active (real) power** in Watts ($P = VI\cos\phi$).
3. **[T/F]** If supply frequency increases, the inductive reactance $X_L$ increases linearly.  
   **Answer: TRUE.** Since $X_L = 2\pi f L$, reactance is directly proportional to frequency.
4. **[T/F]** The potential coil of a wattmeter has very low resistance.  
   **Answer: FALSE.** The potential coil has **very high** resistance (often with an external series non-inductive resistor) to minimize internal current draw.

---

### Type 2: One-Word / Quick Theory (Exp 03)

1. The phase angle between voltage and current in an ideal pure inductor:  
   **$90^\circ$ (current lags voltage)**
2. The property of an electric coil that opposes any change in current flowing through it:  
   **Self-inductance**
3. Type of loss measured by the wattmeter in an air-cored inductor:  
   **Copper loss ($I^2 R$)**
4. Standard frequency of AC mains in Bangladesh:  
   **$50\text{ Hz}$**

---

### Type 3: Short Maths (Exp 03)

**Q1:** A test on a choke coil at $f = 50\text{ Hz}$ gives: Voltmeter $= 200\text{ V}$, Ammeter $= 2.0\text{ A}$, Wattmeter $= 40\text{ W}$. Find $Z$, $R$, $X_L$, and $L$.  
**Solution:**  
1. $Z = \frac{V}{I} = \frac{200}{2.0} = \mathbf{100\,\Omega}$  
2. $R = \frac{W}{I^2} = \frac{40}{(2.0)^2} = \frac{40}{4} = \mathbf{10\,\Omega}$  
3. $X_L = \sqrt{Z^2 - R^2} = \sqrt{100^2 - 10^2} = \sqrt{10000 - 100} = \sqrt{9900} \approx \mathbf{99.5\,\Omega}$  
4. $L = \frac{X_L}{2\pi f} = \frac{99.5}{2 \times \pi \times 50} = \frac{99.5}{314.16} \approx \mathbf{0.317\text{ H}}$ (or $317\text{ mH}$)

---

# Experiment 04: Capacitance of a Capacitor (3-Meter Method)

### Core Concepts & Circuit Setup
![Capacitance Measurement Circuit](attachments/meas_exp04_capacitance_circuit.png)

1. **Working Principle:**
   - Impedance: $Z = \frac{V}{I}$
   - Dielectric Loss Equivalent Resistance: $R = \frac{W}{I^2}$
   - Capacitive Reactance: $X_C = \sqrt{Z^2 - R^2}$
   - Capacitance: $C = \frac{1}{2\pi f X_C} \implies C = \frac{10^6}{2\pi f X_C}\,\mu\text{F}$
2. **Ideal vs Practical Capacitor:**
   - **Ideal Capacitor:** Dissipation factor $D = 0$, $W = 0\text{ W}$, current leads voltage by exactly $90^\circ$.
   - **Practical Capacitor:** Has small dielectric leakage/loss, so wattmeter records a small power value ($W > 0$).
3. **Safety Critical Rule:** Always discharge capacitors by shorting their terminals through a resistor after turning off AC power. Capacitors can store dangerous lethal charge even after circuit disconnection!

---

### Type 1: True / False (Exp 04)

1. **[T/F]** In a pure capacitor, current leads the supply voltage by $90^\circ$.  
   **Answer: TRUE.**
2. **[T/F]** Capacitive reactance increases when the supply frequency increases.  
   **Answer: FALSE.** $X_C = \frac{1}{2\pi f C}$, so $X_C$ is inversely proportional to frequency.
3. **[T/F]** An electrolytic capacitor can be connected directly to an AC power line without damage.  
   **Answer: FALSE.** Polarized electrolytic capacitors will overheat and explode under AC; only **non-polar (bipolar) AC capacitors** must be used.
4. **[T/F]** In the three-meter capacitance test, if dielectric loss is negligible, $Z \approx X_C$.  
   **Answer: TRUE.** When $R \ll Z$, $X_C = \sqrt{Z^2 - R^2} \approx Z$.

---

### Type 2: One-Word / Quick Theory (Exp 04)

1. The unit of capacitance:  
   **Farad ($F$)**
2. Power dissipated by an ideal capacitor under sinusoidal AC:  
   **Zero Watts**
3. Ratio of equivalent series resistance (ESR) to capacitive reactance, representing dielectric quality:  
   **Dissipation factor ($\tan\delta$)**
4. The insulating medium sandwiched between the conductive plates of a capacitor:  
   **Dielectric**

---

### Type 3: Short Maths (Exp 04)

**Q1:** A capacitor draws $0.5\text{ A}$ when connected across a $200\text{ V}$, $50\text{ Hz}$ AC line. The wattmeter reading is negligible ($W \approx 0$). Calculate $X_C$ and $C$.  
**Solution:**  
- $X_C \approx Z = \frac{V}{I} = \frac{200}{0.5} = \mathbf{400\,\Omega}$  
- $C = \frac{1}{2\pi f X_C} = \frac{1}{2 \times 3.1416 \times 50 \times 400} = \frac{1}{125664} \approx 7.96 \times 10^{-6}\text{ F} = \mathbf{7.96\,\mu\text{F}}$

**Q2:** A capacitor test yields $Z = 250\,\Omega$ and $R = 15\,\Omega$. Calculate $X_C$.  
**Solution:**  
$$X_C = \sqrt{250^2 - 15^2} = \sqrt{62500 - 225} = \sqrt{62275} \approx \mathbf{249.55\,\Omega}$$

---

# Experiments 05 & 06: Potential Transformer (PT) & Current Transformer (CT)

### Core Concepts & Circuit Setup
![PT Circuit](attachments/meas_exp05_pt_circuit.png)  
*Figure: Potential Transformer (PT) Connection*

![CT Circuit](attachments/meas_exp06_ct_circuit.png)  
*Figure: Current Transformer (CT) Connection*

1. **Instrument Transformers Purpose:**
   - Step down high voltages and high currents to safe, standardized levels ($110\text{ V}$ / $100\text{ V}$ for PT; $5\text{ A}$ or $1\text{ A}$ for CT).
   - Electrically isolate delicate measuring instruments and operating personnel from dangerous high-voltage lines.
2. **Potential Transformer (PT):**
   - Basically a step-down voltage transformer ($N_1 > N_2$).
   - Primary connected in **parallel** with high voltage lines; secondary connected to a standard low-range voltmeter ($0-150\text{ V}$).
   - **Turns Ratio:** $k_{PT} = \frac{V_p}{V_s} \approx \frac{N_1}{N_2}$.
   - Secondary operates practically on open-circuit (voltmeter draws tiny current).
   - **Safety Rule:** Secondary winding **must be grounded** to protect operators if high-voltage insulation breaks down.
3. **Current Transformer (CT):**
   - Basically a step-up voltage, step-down current transformer ($N_2 > N_1$).
   - Primary has very few turns (often a single bar/conductor passed through core, $N_1 = 1$) connected in **series** with high-current line.
   - Secondary has many turns, connected to standard low-range ammeter ($0-5\text{ A}$).
   - **Nominal Ratio:** $k_{CT} = \frac{I_p}{I_s} \approx \frac{N_2}{N_1}$.
4. **CRITICAL QUIZ HAZARD — CT Secondary Open Circuit:**
   - **NEVER OPEN-CIRCUIT THE SECONDARY OF A CT WHILE THE PRIMARY IS ENERGIZED!**
   - **Reason:** Under normal operation, secondary ampere-turns ($N_2 I_2$) almost completely cancel primary ampere-turns ($N_1 I_1$), leaving a tiny magnetizing net MMF. If secondary is opened:
     1. Secondary demagnetizing MMF drops to zero.
     2. The entire primary line current becomes purely magnetizing current.
     3. Core flux explodes to saturation levels, inducing dangerously high voltage peaks (thousands of volts) across the open secondary terminals $\implies$ **Lethal shock hazard to personnel**.
     4. Extreme core losses cause rapid overheating and breakdown of winding insulation.
     5. Core gets permanently magnetized, destroying calibration accuracy.
   - Always **short-circuit** CT secondary before disconnecting the ammeter!

---

### Type 1: True / False (Exp 05 & 06)

1. **[T/F]** The secondary winding of a Current Transformer must be opened before removing the ammeter.  
   **Answer: FALSE.** It must ALWAYS be **short-circuited** before removing the ammeter.
2. **[T/F]** A Potential Transformer operates with its secondary winding near open-circuit condition.  
   **Answer: TRUE.** High voltmeter resistance means secondary current is negligibly small.
3. **[T/F]** The primary winding of a bar-type CT consists of hundreds of turns.  
   **Answer: FALSE.** A bar-type CT has only **one single turn** ($N_1 = 1$).
4. **[T/F]** Secondary windings of both CT and PT should be solidly grounded for safety.  
   **Answer: TRUE.** Prevents secondary from floating at high potential during insulation breakdown.
5. **[T/F]** The standard secondary rated current of a commercial CT is typically $5\text{ A}$ or $1\text{ A}$.  
   **Answer: TRUE.**

---

### Type 2: One-Word / Quick Theory (Exp 05 & 06)

1. Standard secondary rated voltage of a commercial Potential Transformer:  
   **$110\text{ V}$ (or $100\text{ V}$)**
2. The action required on CT secondary terminals before disconnecting the ammeter:  
   **Short-circuiting**
3. The type of error in instrument transformers caused by the phase angle between primary and reversed secondary quantities differing from $180^\circ$:  
   **Phase angle error**
4. Instrument transformer used to isolate meters from high current circuits:  
   **Current Transformer (CT)**
5. Rated burden of an instrument transformer is specified in which unit:  
   **Volt-Ampere ($VA$)**

---

### Type 3: Short Maths (Exp 05 & 06)

**Q1:** A PT has a turns ratio of $20:1$ ($k_{PT} = 20$). If the secondary voltmeter reads $110\text{ V}$, calculate the primary high voltage line voltage.  
**Solution:**  
$$V_p = k_{PT} \times V_s = 20 \times 110\text{ V} = \mathbf{2200\text{ V}}\quad (2.2\text{ kV})$$

**Q2:** A CT with ratio $100:5\text{ A}$ ($k = 20$) is connected to an ammeter that reads $3.2\text{ A}$. Find the primary line current.  
**Solution:**  
$$I_p = k_{CT} \times I_s = 20 \times 3.2\text{ A} = \mathbf{64\text{ A}}$$

---

# Experiments 07 & 08: Extension of Ammeter & Voltmeter Ranges

### Core Concepts & Circuit Setup
![Ammeter Range Extension](attachments/meas_exp07_ammeter_extension.png)  
*Figure: Ammeter Range Extension using Shunt Resistor ($R_{sh}$)*

![Voltmeter Range Extension](attachments/meas_exp08_voltmeter_extension.png)  
*Figure: Voltmeter Range Extension using Series Multiplier ($R_s$)*

#### 1. Ammeter Range Extension (Shunt Resistor)
- A low resistance **shunt ($R_{sh}$)** is connected in **parallel** with the meter movement ($R_m$).
- Let $I_m$ be full-scale meter current, $I$ be the total target line current to measure:
  $$I = I_m + I_{sh}$$
- Voltage drop across parallel branches is equal:
  $$I_{sh} R_{sh} = I_m R_m \implies (I - I_m) R_{sh} = I_m R_m$$
  $$R_{sh} = \frac{I_m R_m}{I - I_m} = \frac{R_m}{\frac{I}{I_m} - 1} = \frac{\mathbf{R_m}}{\mathbf{m - 1}}$$
- **Multiplying Factor of Shunt ($m$):**
  $$m = \frac{I}{I_m} \quad (\text{ratio of total current to meter full-scale current})$$
- **Shunt Material Requirements:**
  - Extremely low temperature coefficient of resistance.
  - Zero/negligible thermoelectric EMF with copper.
  - Standard material: **Manganin** (copper-manganese-nickel alloy).

#### 2. Voltmeter Range Extension (Series Multiplier)
- A high resistance **multiplier ($R_s$)** is connected in **series** with the meter movement ($R_m$).
- Let $V_m = I_m R_m$ be the meter original full scale voltage, $V$ be the target maximum voltage:
  $$V = I_m (R_m + R_s)$$
  $$\frac{V}{I_m} = R_m + R_s \implies R_s = \frac{V}{I_m} - R_m = \left(\frac{V}{V_m} - 1\right) R_m = \mathbf{(m - 1) R_m}$$
- **Multiplying Factor of Multiplier ($m$):**
  $$m = \frac{V}{V_m} \quad (\text{ratio of target voltage to meter full-scale voltage})$$
- **Multiplier Material:** **Manganin** or **Constantan** (high resistance stability over temperature).

---

### Comparison Summary: Shunt vs Multiplier

| Feature | Ammeter Extension (Shunt) | Voltmeter Extension (Multiplier) |
| :--- | :--- | :--- |
| **Connection** | **Parallel** with meter movement | **Series** with meter movement |
| **Resistance Value** | Very **LOW** ($R_{sh} < R_m$) | Very **HIGH** ($R_s > R_m$) |
| **Formula** | $R_{sh} = \frac{R_m}{m - 1}$ | $R_s = (m - 1) R_m$ |
| **Multiplying factor $m$** | $m = \frac{I}{I_m}$ | $m = \frac{V}{V_m}$ |
| **Preferred Material** | Manganin | Manganin / Constantan |

---

### Type 1: True / False (Exp 07 & 08)

1. **[T/F]** To extend the range of an ammeter, a high resistance is connected in series.  
   **Answer: FALSE.** A **low resistance** is connected in **parallel** (shunt).
2. **[T/F]** The multiplying factor $m$ of an ammeter shunt is always greater than 1.  
   **Answer: TRUE.** $m = I / I_m$, and the extended current $I$ is always greater than $I_m$.
3. **[T/F]** The resistance of an ammeter shunt is much lower than the meter coil resistance.  
   **Answer: TRUE.** Most current bypasses through the low-resistance shunt.
4. **[T/F]** Connecting a multiplier in series with a voltmeter reduces the overall resistance of the voltmeter circuit.  
   **Answer: FALSE.** Total resistance becomes $R_{\text{total}} = R_m + R_s$, which increases the input resistance (beneficial as it reduces the loading effect).
5. **[T/F]** Manganin is preferred for shunts because of its high positive temperature coefficient of resistance.  
   **Answer: FALSE.** Manganin is used because it has a **near-zero** temperature coefficient of resistance.

---

### Type 2: One-Word / Quick Theory (Exp 07 & 08)

1. The low resistance resistor placed in parallel to extend ammeter range:  
   **Shunt resistor**
2. The high resistance resistor placed in series to extend voltmeter range:  
   **Multiplier resistor**
3. Most commonly used alloy for shunts and multipliers due to its temperature stability:  
   **Manganin**
4. Ratio of maximum target current to meter full-scale current ($I / I_m$):  
   **Multiplying factor ($m$)**
5. Sensitivity of a voltmeter is expressed in what unit:  
   **Ohms per Volt ($\Omega/\text{V}$)**

---

### Type 3: Short Maths (Exp 07 & 08)

**Q1 (Ammeter Shunt):** A moving-coil ammeter has an internal resistance of $R_m = 25\,\Omega$ and gives a full-scale deflection with $I_m = 10\text{ mA}$ ($0.01\text{ A}$). Calculate the shunt resistance required to measure up to $10\text{ A}$.  
**Solution:**  
1. Multiplying factor: $m = \frac{I}{I_m} = \frac{10}{0.01} = 1000$  
2. Shunt resistance:  
   $$R_{sh} = \frac{R_m}{m - 1} = \frac{25}{1000 - 1} = \frac{25}{999} \approx \mathbf{0.02502\,\Omega}$$

**Q2 (Voltmeter Multiplier):** A basic meter movement with $R_m = 100\,\Omega$ and full-scale voltage $V_m = 1\text{ V}$ is to be converted into a voltmeter capable of reading up to $100\text{ V}$. Find the multiplier resistance $R_s$.  
**Solution:**  
1. Multiplying factor: $m = \frac{V}{V_m} = \frac{100}{1} = 100$  
2. Multiplier resistance:  
   $$R_s = (m - 1) R_m = (100 - 1) \times 100 = 99 \times 100 = \mathbf{9900\,\Omega}\quad (9.9\text{ k}\Omega)$$

---

# Experiment 09: Electrical Energy Consumption using Energy Meter

### Core Concepts & Circuit Setup
![Energy Meter Circuit](attachments/meas_exp09_energy_meter_circuit.png)

1. **Meter Type:** Induction type single-phase energy meter. (Operates exclusively on **AC**).
2. **Four Main Systems:**
   - **Driving System:** Consists of **Shunt Magnet** (wound with fine wire, high inductance, connected across supply voltage $V$) and **Series Magnet** (wound with thick wire, low impedance, connected in series with load current $I$).
   - **Moving System:** Light aluminum disc mounted on a vertical spindle, placed between the air gaps of shunt and series magnets.
   - **Braking System:** Permanent horseshoe magnet that induces eddy currents in the rotating aluminum disc to create an opposing **braking torque** ($T_b \propto N$).
   - **Registering (Counting) Mechanism:** Train of reduction gear wheels driven by a worm gear on the spindle that registers energy in kilowatt-hours ($kWh$).
3. **Torque Balance & Energy Equation:**
   - Driving torque: $T_d \propto V \cdot I \cdot \cos\phi = P$
   - Braking torque: $T_b \propto N$ (speed in rpm)
   - At steady rotation: $T_d = T_b \implies N \propto P$
   - Total disc revolutions: $\int N \, dt \propto \int P \, dt = \text{Energy (kWh)}$
4. **Meter Constant ($K$):**
   $$K = \frac{\text{Number of disc revolutions}}{\text{Energy consumed in kWh}} \quad [\text{rev}/kWh]$$
   - Common values stamped on nameplate: $1600\text{ rev}/kWh$, $1200\text{ rev}/kWh$, $480\text{ rev}/kWh$.
5. **Creeping Error & Prevention:**
   - **Definition:** Slow, continuous rotation of the disc under **no-load** condition (when only voltage coil is energized, load current $I = 0$).
   - **Causes:** Over-compensation for friction (frictional compensation shading loop adjusted too far), vibration, stray magnetic fields, or excessive line voltage.
   - **Prevention:** Drilling **two diametrically opposite small holes** in the aluminum disc. When a hole reaches under the shunt magnet pole, the path of eddy currents is distorted, creating an opposing reluctance force that stops the disc.

---

### Type 1: True / False (Exp 09)

1. **[T/F]** An induction type energy meter can be used to measure DC energy.  
   **Answer: FALSE.** Induction instruments operate purely on the principle of alternating magnetic fields inducing eddy currents (AC only).
2. **[T/F]** Creeping in an energy meter occurs when the load current is at maximum rating.  
   **Answer: FALSE.** Creeping is rotation at **no load** (zero load current).
3. **[T/F]** The braking torque on the aluminum disc is provided by a permanent magnet.  
   **Answer: TRUE.** Eddy currents induced by the permanent magnet create $T_b \propto \text{speed}$.
4. **[T/F]** If the permanent brake magnet is shifted radially inward toward the disc center, the disc speed increases.  
   **Answer: TRUE.** Moving the magnet inward decreases the effective radius and braking torque, causing the disc to rotate faster.
5. **[T/F]** Two diametrically opposite holes are drilled in the disc to prevent creeping.  
   **Answer: TRUE.**

---

### Type 2: One-Word / Quick Theory (Exp 09)

1. The commercial unit of electrical energy recorded by an energy meter ($1\text{ kWh}$):  
   **Board of Trade Unit (B.O.T. Unit) / Kilowatt-hour**
2. Slow continuous rotation of the energy meter disc under zero load condition:  
   **Creeping**
3. The method of testing an energy meter with separate voltage supply to PC and small low-voltage circulating current to CC to save massive energy:  
   **Phantom loading (Fictitious loading)**
4. Physical effect used to suppress the disc rotation in the braking system:  
   **Eddy current braking**
5. Stamped rating specifying revolutions per unit of energy on the meter dial:  
   **Meter constant ($K$)**

---

### Type 3: Short Maths (Exp 09)

**Q1:** An energy meter has a meter constant of $K = 1200\text{ rev}/kWh$. In a test with a $220\text{ V}$, $5\text{ A}$ unity power factor load, the disc makes $40$ revolutions in $120\text{ seconds}$. Calculate:  
(a) The recorded energy, (b) The true energy consumed, (c) The percentage error.  
**Solution:**  
1. **Recorded Energy:**  
   $$E_{\text{recorded}} = \frac{N}{K} = \frac{40}{1200} = \mathbf{0.03333\text{ kWh}}$$  
2. **True Energy:**  
   $$P = V \cdot I \cdot \cos\phi = 220 \times 5 \times 1 = 1100\text{ W} = 1.1\text{ kW}$$  
   $$t = \frac{120}{3600}\text{ hours} = \frac{1}{30}\text{ hour}$$  
   $$E_{\text{true}} = P \times t = 1.1 \times \frac{1}{30} = \mathbf{0.03667\text{ kWh}}$$  
3. **Percentage Error:**  
   $$\%e = \frac{E_{\text{recorded}} - E_{\text{true}}}{E_{\text{true}}} \times 100\% = \frac{0.03333 - 0.03667}{0.03667} \times 100\% = \mathbf{-9.11\%}\quad (\text{Meter runs slow by } 9.11\%)$$

**Q2 (From Lab Manual Data Table):** A meter with $K = 1600\text{ rev}/kWh$ runs for $10\text{ minutes}$ and makes $50$ revolutions. What is the recorded power equivalent?  
**Solution:**  
- Revolutions per hour $= \frac{50}{10} \times 60 = 300\text{ rev/hr}$.  
- Energy per hour $= \frac{300}{1600} = 0.1875\text{ kWh}$.  
- Equivalent power $= 0.1875\text{ kW} = \mathbf{187.5\text{ W}}$.

---

# Experiment 10: Measurement of Power using CT and PT

### Core Concepts & Circuit Setup
![Power Measurement with CT and PT](attachments/meas_exp10_power_ct_pt_circuit.png)

1. **Why use CT & PT with a Wattmeter?**
   - Directly connecting a wattmeter to high-voltage (e.g., $11\text{ kV}$) and high-current (e.g., $500\text{ A}$) lines is dangerous and requires bulky, expensive coils.
   - Using a CT and PT allows using an inexpensive, low-rating standard wattmeter ($110\text{ V}$, $5\text{ A}$).
2. **Connection Rules:**
   - **Current Coil (CC)** of the wattmeter is connected to the **secondary of the CT**.
   - **Potential Coil (PC)** of the wattmeter is connected to the **secondary of the PT**.
   - Secondary circuits are grounded for safety.
3. **Power Calculation Formula:**
   $$P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{measured}}$$
   where:
   - $k_{CT} = \frac{I_p}{I_s}$ (CT current ratio)
   - $k_{PT} = \frac{V_p}{V_s}$ (PT voltage ratio)
   - $W_{\text{measured}}$ is the actual power read on the wattmeter scale.

---

### Type 1: True / False (Exp 10)

1. **[T/F]** In power measurement using CT and PT, the wattmeter current coil is connected to the PT secondary.  
   **Answer: FALSE.** The current coil (CC) connects to the **CT secondary**; the potential coil (PC) connects to the **PT secondary**.
2. **[T/F]** The true load power is obtained by multiplying the wattmeter reading by both the CT ratio and the PT ratio.  
   **Answer: TRUE.**
3. **[T/F]** Phase angle errors of CT and PT do not affect power measurement at low power factors.  
   **Answer: FALSE.** Phase angle errors cause significant errors in active power measurement, especially when the load power factor is low.

---

### Type 2: One-Word / Quick Theory (Exp 10)

1. The overall multiplication factor to convert wattmeter reading to true system power ($k_{CT} \times k_{PT}$):  
   **Overall multiplying factor / Instrument transformer ratio product**
2. Coil of the wattmeter that carries the scaled-down line current:  
   **Current Coil (CC)**
3. Coil of the wattmeter that experiences the scaled-down line voltage:  
   **Potential Coil (PC) / Voltage Coil**

---

### Type 3: Short Maths (Exp 10)

**Q1:** A wattmeter is connected via a CT with ratio $24:1$ and a PT with ratio $2:1$. The wattmeter indicates $384\text{ W}$. Find the true power consumed by the load.  
**Solution:**  
$$P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{meter}} = 24 \times 2 \times 384\text{ W} = 48 \times 384 = \mathbf{18432\text{ W}}\quad (18.432\text{ kW})$$

**Q2:** A load on a $6.6\text{ kV}$ line drawing $100\text{ A}$ is monitored by a PT of ratio $6600/110\text{ V}$ and a CT of ratio $100/5\text{ A}$. What is the multiplying factor of the wattmeter setup?  
**Solution:**  
- $k_{PT} = \frac{6600}{110} = 60$  
- $k_{CT} = \frac{100}{5} = 20$  
- Setup Multiplying Factor $= k_{PT} \times k_{CT} = 60 \times 20 = \mathbf{1200}$.  
*(If meter reads $250\text{ W}$, actual power $= 250 \times 1200 = 300\text{ kW}$)*.

---

# Experiment 11: Speed of a Rotating Body using Stroboscope

### Core Concepts & Circuit Setup
![Strobotron Circuit](attachments/meas_exp11_strobotron_circuit.png)  
*Figure: Strobotron Flasher Circuit*

![Stroboscope Shaft and Disc](attachments/meas_exp11_stroboscope_shaft.png)  
*Figure: Flashing Light on Shaft Reference Mark*

![Stroboscope Multiple Images](attachments/meas_exp11_stroboscope_images.png)  
*Figure: Patterns at $f = N$, $N/2$, $N/3$, and Multiple Patterns*

1. **Principle of Operation:**
   - Non-contact speed measurement based on **persistence of vision** ($1/16^{\text{th}}$ to $1/10^{\text{th}}$ of a second) and periodic flashing light.
   - When flashing frequency $f$ matches rotating speed $N$ ($f = N$), the reference mark is illuminated at the exact same physical position each revolution $\implies$ appears **stationary with a single mark**.
2. **Submultiples and Multiple Images (Ambiguity):**
   - **Submultiples ($f = N/2, N/3, \dots$):** The shaft completes 2 or 3 revolutions between flashes, so the mark still appears in the same spot $\implies$ **single stationary image**.
   - **Harmonics ($f = 2N, 3N, \dots$):** The lamp flashes twice or three times during a single revolution $\implies$ produces **two or three stationary marks** evenly spaced around the circle.
3. **Ambiguity Resolution Formula (When Speed is Unknown):**
   - If consecutive flashing frequencies $f_m$ (highest) down to $f_1$ (lowest) each produce a single stationary image, and $m$ is the total count of such observed frequencies:
     $$N = \frac{\mathbf{f_m \cdot f_1 \cdot (m - 1)}}{\mathbf{f_m - f_1}}$$
   - For two consecutive flashing frequencies $f_1$ and $f_2$ ($m = 2$):
     $$N = \frac{f_2 \cdot f_1}{f_2 - f_1}$$
4. **Key Advantage:** Non-contact method; imposes zero mechanical load/drag on small motors or fragile shafts.

---

### Type 1: True / False (Exp 11)

1. **[T/F]** A stroboscope imposes mechanical loading on the rotating shaft under test.  
   **Answer: FALSE.** It is a completely optical, **non-contact** instrument.
2. **[T/F]** If the flashing frequency is twice the shaft speed ($f = 2N$), two stationary marks appear $180^\circ$ apart.  
   **Answer: TRUE.**
3. **[T/F]** A single stationary image appears only at $f = N$ and never at submultiples.  
   **Answer: FALSE.** Single stationary images also appear at submultiples ($N/2, N/3, \dots$) because the mark returns to the exact same position on each flash.
4. **[T/F]** The flashing gas-discharge tube traditionally used in stroboscopes is the Strobotron tube (or Xenon flash lamp).  
   **Answer: TRUE.**

---

### Type 2: One-Word / Quick Theory (Exp 11)

1. Physiological phenomenon of the human eye that enables the stroboscopic effect:  
   **Persistence of vision**
2. The gas discharge tube used to produce high-intensity, short-duration light pulses:  
   **Strobotron (or Xenon flash tube)**
3. The number of stationary marks visible on a shaft disc when flashing frequency is equal to true shaft speed ($f = N$):  
   **Single mark (1 image)**
4. Number of stationary marks observed when flashing frequency is three times the true shaft speed ($f = 3N$):  
   **Three marks**

---

### Type 3: Short Maths (Exp 11)

**Q1 (Lab Manual Numerical):** In a stroboscope speed measurement, the highest flashing frequency producing a single stationary pattern is $f_m = 2577\text{ rpm}$, and the lowest is $f_1 = 874.1\text{ rpm}$, with $m = 3$ consecutive single-image frequencies observed. Calculate the true shaft speed $N$.  
**Solution:**  
$$N = \frac{f_m \cdot f_1 \cdot (m - 1)}{f_m - f_1} = \frac{2577 \times 874.1 \times (3 - 1)}{2577 - 874.1} = \frac{2577 \times 874.1 \times 2}{1702.9}$$  
$$N = \frac{4505111.4}{1702.9} \approx \mathbf{2645.5\text{ rpm}}$$  
*(Manual check: $\frac{2577 \times 874.1 \times 2}{1702.9} \approx 2645.5\text{ rpm}$)*

**Q2 (Two consecutive frequencies):** Two consecutive flashing frequencies giving a single stationary mark are $f_1 = 1200\text{ rpm}$ and $f_2 = 1500\text{ rpm}$. Find the shaft speed.  
**Solution:**  
$$N = \frac{f_2 \cdot f_1}{f_2 - f_1} = \frac{1500 \times 1200}{1500 - 1200} = \frac{1800000}{300} = \mathbf{6000\text{ rpm}}$$

---

# Experiment 12: Insulation Resistance Measurement using Megger

### Core Concepts & Circuit Setup
![Megger Cross Coil Movement](attachments/meas_exp12_megger_cross_coil.png)  
*Figure: Internal Working Principle of Megger (Cross-Coil Movement)*

![Megger Cable Testing](attachments/meas_exp12_megger_cable_testing.png)  
*Figure: Cable Insulation Testing with Guard Terminal Connection*

1. **Definition & Purpose:**
   - A **Megger** (Mega-ohmmeter) measures very high resistances (insulation resistance in Mega-ohms $M\Omega$ or Giga-ohms $G\Omega$).
   - Used for testing cable insulation, motor/transformer windings, and busbars.
2. **Construction:**
   - Built-in hand-cranked DC generator (typically $500\text{ V}, 1000\text{ V},$ or $2500\text{ V}$) equipped with a centrifugal clutch to maintain constant generator speed.
   - **Cross-Coil Movement (Ratiometer):** Contains two coils mounted at an angle on the same moving spindle:
     - **Control Coil / Pressure Coil (Coil A):** Connected in series with resistance $R_1$ across the generator. Produces torque tending to drive the pointer to **Infinity ($\infty$)**.
     - **Deflecting Coil / Current Coil (Coil B):** Connected in series with the unknown insulation resistance $R_x$ across the generator. Produces torque tending to drive pointer to **Zero ($0$)**.
   - Deflection angle is proportional to the **ratio of currents** ($I_B / I_A$):
     $$\theta \propto \frac{I_B}{I_A} \propto \frac{1}{R_x}$$
   - **Crucial Feature:** Because both coils receive voltage from the same generator, voltage fluctuations cancel out. The reading is **independent of hand-crank speed**!
3. **No Controlling Spring:** The pointer rests at arbitrary positions when the Megger is idle (no restoring hairsprings).
4. **Three Terminals:**
   - **Line (L):** Connected to the conductor core.
   - **Earth (E):** Connected to the outer metallic sheath or earth ground.
   - **Guard (G):** Wrapped around the outer surface of the insulation.
5. **Purpose of Guard Terminal ($G$):**
   - Surface leakage current flows across dirt/moisture on the outer cable surface.
   - The Guard wire collects this surface leakage and diverts it directly back to the generator negative terminal, **bypassing the current coil (Coil B)**.
   - This ensures the Megger measures **only true volume leakage**, preventing false low readings.
6. **Pre-Test Check (Routine Health Test):**
   - **Open-Circuit Test:** Terminals disconnected $\implies$ Rotate handle $\implies$ Pointer must indicate **$\mathbf{\infty}$ (Infinity)**.
   - **Short-Circuit Test:** Terminals L and E shorted together $\implies$ Rotate handle slowly $\implies$ Pointer must indicate **$\mathbf{0}$ (Zero)**.
7. **Safe Insulation Value Rule (IEEE Standard):**
   $$R_{\text{insulation}} \ge 1\text{ M}\Omega \quad (\text{Minimum rule for equipment up to } 1\text{ kV})$$
   $$\text{General Rule: } R_{\text{ins}} \ge (\text{Rated kV} + 1)\text{ M}\Omega$$

---

### Type 1: True / False (Exp 12)

1. **[T/F]** A Megger utilizes phosphor bronze control springs to return the pointer to zero.  
   **Answer: FALSE.** A Megger has **no controlling spring**; controlling torque is produced electrically by the control coil.
2. **[T/F]** The reading of a hand-cranked Megger changes significantly if the crank speed varies slightly above slipping speed.  
   **Answer: FALSE.** The centrifugal clutch ensures constant generator speed, and the cross-coil ratiometer design makes deflection dependent only on current ratio, not voltage.
3. **[T/F]** Before conducting an insulation test, the equipment under test must be completely de-energized and grounded.  
   **Answer: TRUE.** Testing energized circuits will destroy the Megger and create shock hazards.
4. **[T/F]** The Guard terminal in a Megger is used to bypass surface leakage currents.  
   **Answer: TRUE.**
5. **[T/F]** When testing a healthy, uncharged long cable, the Megger pointer initially swings toward zero and then slowly creeps up toward infinity.  
   **Answer: TRUE.** This is due to initial capacitive charging current; pointer rises as the cable capacitance charges.

---

### Type 2: One-Word / Quick Theory (Exp 12)

1. The terminal on a Megger designed to eliminate surface leakage errors:  
   **Guard terminal (G)**
2. Pointer indication of a Megger during an open-circuit health test:  
   **Infinity ($\infty$)**
3. Pointer indication of a Megger during a short-circuit health test:  
   **Zero ($0$)**
4. Type of movement in a Megger where deflection depends on the ratio of two coil currents:  
   **Cross-coil movement / Ratiometer / Ohmmeter movement**
5. Mechanism inside a hand-cranked Megger that prevents the generator shaft from exceeding design speed:  
   **Centrifugal clutch**
6. Minimum acceptable insulation resistance for low-voltage residential/industrial wiring:  
   **$1\text{ M}\Omega$**

---

### Type 3: Short Maths (Exp 12)

**Q1:** An insulation test on a $33\text{ kV}$ distribution line transformer using a $2500\text{ V}$ Megger shows an insulation resistance of $2500\text{ M}\Omega$. The minimum recommended insulation resistance by standard formula is $R_{\text{min}} = (\text{Rated kV} + 1)\text{ M}\Omega$. Does this transformer pass the test?  
**Solution:**  
- $R_{\text{min}} = (33 + 1) = \mathbf{34\text{ M}\Omega}$.  
- Measured value $= 2500\text{ M}\Omega$.  
- Since $2500\text{ M}\Omega \gg 34\text{ M}\Omega$, the transformer **easily passes the insulation test** (healthy insulation).

**Q2:** A cable insulation test at $500\text{ V}$ DC yields a steady leakage current of $0.5\,\mu\text{A}$ through the insulation bulk. What is the insulation resistance?  
**Solution:**  
$$R_{\text{ins}} = \frac{V}{I_{\text{leakage}}} = \frac{500\text{ V}}{0.5 \times 10^{-6}\text{ A}} = 1000 \times 10^6\,\Omega = \mathbf{1000\text{ M}\Omega}\quad (1\text{ G}\Omega)$$

---

# Rapid-Fire Quiz Mega Bank (All Topics Combined)

### 30 Rapid-Fire True / False

| # | Statement | Ans | One-Line Explanation |
|---|---|:---:|---|
| 1 | PMMC instruments can directly measure AC currents without a rectifier. | **F** | PMMC responds to average value, which is zero for symmetrical AC. |
| 2 | An ammeter should always be connected in series with the load. | **T** | Connecting it in parallel causes a dead short circuit. |
| 3 | A voltmeter should have the lowest possible resistance. | **F** | It needs very high resistance to minimize the loading error. |
| 4 | Bridge methods are null methods and don't depend on meter calibration. | **T** | Balance depends only on passive arm ratios. |
| 5 | Kelvin double bridge is used for measuring high insulation resistance. | **F** | Kelvin double bridge is for **low** resistance ($< 1\,\Omega$). |
| 6 | An ideal inductor consumes zero average active power. | **T** | Phase difference $\phi = 90^\circ \implies \cos(90^\circ) = 0$. |
| 7 | In an RC series AC circuit, current leads voltage by $90^\circ$ always. | **F** | Leads by $0^\circ < \theta < 90^\circ$; leads by $90^\circ$ only if $R = 0$. |
| 8 | Potential transformers step down high voltage to standard $110\text{ V}$. | **T** | Standard secondary rating is $110\text{ V}$. |
| 9 | A CT secondary should be left open when primary carries full load. | **F** | Lethal high voltage and explosive core saturation occur. |
| 10| Shunts are made of copper because copper has low resistance. | **F** | Shunts are made of **Manganin** (low temperature coefficient). |
| 11| Voltmeter multiplier resistance is calculated by $R_s = (m - 1)R_m$. | **T** | Derived from $V = I_m(R_m + R_s)$. |
| 12| Creeping in an energy meter can be prevented by two opposite holes. | **T** | Holes distort eddy current paths to create stopping torque. |
| 13| Energy meter brake torque is inversely proportional to disc speed. | **F** | Braking torque is directly proportional to speed ($T_b \propto N$). |
| 14| Phantom loading saves substantial energy during meter calibration. | **T** | High current is supplied from a low-voltage auxiliary source. |
| 15| Stroboscope is a direct contact mechanical speed measuring meter. | **F** | It is completely optical / non-contact. |
| 16| At stroboscope flashing rate $f = 2N$, two stationary marks appear. | **T** | Shaft flashes twice per revolution. |
| 17| Megger deflection depends heavily on hand crank rotating speed. | **F** | Ratio of currents in cross-coil cancels voltage fluctuations. |
| 18| Megger Guard terminal bypasses surface leakage to ground directly. | **F** | Bypasses leakage to generator negative, skipping current coil. |
| 19| Damping torque in PMMC is produced by air friction damping. | **F** | PMMC uses **eddy current damping** in its aluminum former. |
| 20| A 3-meter method measures $R$ by $W/I^2$. | **T** | Wattmeter measures true copper loss $I^2 R$. |
| 21| Moving Iron (MI) meters have a linear, uniform scale. | **F** | MI scale is non-linear / cramped at bottom ($T_d \propto I^2$). |
| 22| PMMC instruments have a linear, evenly spaced scale. | **T** | Deflection $\theta \propto I$. |
| 23| Connecting an ammeter across a $220\text{ V}$ line will trip circuit breakers. | **T** | Extremely low resistance causes short-circuit current. |
| 24| Meter constant unit is $kWh/\text{revolution}$. | **F** | It is $\text{revolutions}/kWh$. |
| 25| An autotransformer has two physically separate windings. | **F** | It has a single continuous tapped winding. |
| 26| Dielectric loss causes a practical capacitor to dissipate small power. | **T** | Dielectric heating creates equivalent series resistance (ESR). |
| 27| Secondary of a PT must be grounded for personal safety. | **T** | Prevents secondary line from rising to HV during breakdown. |
| 28| If a Megger pointer rests at random positions at rest, it is broken. | **F** | Normal behavior; Meggers do not use mechanical hairsprings. |
| 29| A CT is effectively a step-up voltage transformer. | **F** | Step-up for voltage, step-down for current ($N_2 > N_1$). |
| 30| Wattmeter Multiplying Factor $= \frac{\text{Current Range} \times \text{Voltage Range} \times \cos\phi_{\text{rated}}}{\text{FSD}}$. | **T** | Used to scale reading on generic graduated dials. |

---

### 30 Rapid-Fire One-Word / Quick Theory

| # | Question / Clue | One-Word / Short Answer |
|---|---|---|
| 1 | Principle on which PMMC works: | **Motor principle (Lorentz force)** |
| 2 | Type of damping used in moving-iron instruments: | **Air friction damping** |
| 3 | Material used for non-inductive standard shunt resistors: | **Manganin** |
| 4 | Detector used in low-frequency AC bridges: | **Vibration Galvanometer / Headphones** |
| 5 | Term for zero-load slow rotation of an energy meter disc: | **Creeping** |
| 6 | Disc material in an induction energy meter: | **Aluminum** |
| 7 | Number of windings in an autotransformer / Variac: | **One (Single tapped winding)** |
| 8 | Standard secondary current rating for CT: | **$5\text{ A}$ (or $1\text{ A}$)** |
| 9 | Standard secondary voltage rating for PT: | **$110\text{ V}$ (or $100\text{ V}$)** |
| 10| What happens to CT secondary if opened on load: | **Extremely high lethal voltage** |
| 11| Instrument used for testing cable insulation: | **Megger** |
| 12| Purpose of Guard terminal in Megger: | **Eliminate surface leakage error** |
| 13| Resistance between Megger terminals during short-circuit test: | **Zero ($0\,\Omega$)** |
| 14| Human eye property utilized by stroboscopes: | **Persistence of vision** |
| 15| Gas filled inside stroboscope flashing tube: | **Xenon** |
| 16| Formula for multiplying factor of ammeter shunt: | **$m = I / I_m$** |
| 17| Formula for ammeter shunt resistance: | **$R_{sh} = R_m / (m - 1)$** |
| 18| Formula for voltmeter multiplier resistance: | **$R_s = (m - 1)R_m$** |
| 19| Unit of energy meter constant: | **$\text{rev}/kWh$** |
| 20| Bridge used for measuring very low resistance ($< 1\,\Omega$): | **Kelvin Double Bridge** |
| 21| Bridge used for measuring capacitance and dielectric loss: | **Scherin Bridge** |
| 22| Bridge used for measuring unknown inductance in terms of capacitance: | **Maxwell's / Hay's Bridge** |
| 23| Formula for true power using CT and PT: | **$k_{CT} \times k_{PT} \times W$** |
| 24| Unit of reactive power: | **VAR (Volt-Ampere Reactive)** |
| 25| Unit of apparent power: | **VA (Volt-Ampere)** |
| 26| Power factor of an ideal pure inductor: | **Zero lagging** |
| 27| Power factor of an ideal pure capacitor: | **Zero leading** |
| 28| Phase angle between current and voltage in a pure resistor: | **$0^\circ$ (in phase)** |
| 29| Coil in wattmeter carrying circuit voltage: | **Potential Coil (PC)** |
| 30| Coil in wattmeter carrying load current: | **Current Coil (CC)** |

---

### High-Yield Short Math Drills

#### Drill 1: Shunt Resistance Mental Calculation
- **Given:** A galvanometer has $R_m = 99\,\Omega$ and full-scale deflection of $1\text{ mA}$. You need to measure $100\text{ mA}$.
- **Fast Step:**  
  $m = \frac{100\text{ mA}}{1\text{ mA}} = 100$  
  $R_{sh} = \frac{R_m}{m - 1} = \frac{99}{100 - 1} = \frac{99}{99} = \mathbf{1.0\,\Omega}$.

#### Drill 2: Voltmeter Multiplier Mental Calculation
- **Given:** A $50\text{ mV}$ meter movement with $R_m = 10\,\Omega$ is to read $50\text{ V}$.
- **Fast Step:**  
  $m = \frac{50\text{ V}}{50\text{ mV}} = 1000$  
  $R_s = (m - 1)R_m = (1000 - 1) \times 10 = 999 \times 10 = \mathbf{9990\,\Omega}\quad (9.99\text{ k}\Omega)$.

#### Drill 3: Inductance Reactance & Value
- **Given:** In $50\text{ Hz}$ test, $V = 100\text{ V}$, $I = 1\text{ A}$, $W = 0\text{ W}$.
- **Fast Step:**  
  $Z = 100/1 = 100\,\Omega$. Since $W = 0 \implies R = 0$, $X_L = Z = 100\,\Omega$.  
  $L = \frac{X_L}{2\pi f} = \frac{100}{2 \times \pi \times 50} = \frac{100}{314.16} = \mathbf{0.318\text{ H}}$.

#### Drill 4: Energy Meter Disc Revolutions
- **Given:** A meter constant is $600\text{ rev}/kWh$. How many revolutions will the disc complete if a $500\text{ W}$ heater runs for $30\text{ minutes}$?
- **Fast Step:**  
  $\text{Energy} = 0.5\text{ kW} \times 0.5\text{ hr} = 0.25\text{ kWh}$.  
  $\text{Revolutions} = K \times \text{Energy} = 600 \times 0.25 = \mathbf{150\text{ revolutions}}$.

#### Drill 5: Stroboscope Fast Calculation
- **Given:** Highest flashing frequency giving single mark is $3000\text{ rpm}$, next lower frequency giving single mark is $1500\text{ rpm}$.
- **Fast Step:**  
  Here $m = 2$.  
  $N = \frac{3000 \times 1500}{3000 - 1500} = \frac{4500000}{1500} = \mathbf{3000\text{ rpm}}$.
