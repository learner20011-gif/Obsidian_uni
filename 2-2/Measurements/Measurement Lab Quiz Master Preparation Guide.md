# EEE 2212: Measurements & Instrumentation Sessional — Master Quiz & Theory Guide

> **Syllabus:** Rajshahi University of Engineering & Technology (RUET) — Dept. of EEE  
> **Course:** EEE 2212 (Measurements and Instrumentation Sessional)  
> **Focus:** Comprehensive Core Theory, Practical Intuition, and All Short Maths / Numerical Problems in simple, easy-to-understand language.

---

## ⚡ Quick Master Formula Sheet

| Experiment / Parameter | Formula | Key Units & Notes |
| :--- | :--- | :--- |
| **Wheatstone Bridge Balance** | $R = \left(\frac{Q}{P}\right) \cdot S$ | $R, S, P, Q$ in $\Omega$. Null method ($I_g = 0$). |
| **Percentage Error** | $\%e = \frac{|R_{\text{actual}} - R_{\text{measured}}|}{R_{\text{actual}}} \times 100\%$ | Unit: $\%$ |
| **Impedance ($Z$)** | $Z = \frac{V}{I}$ | Ohms ($\Omega$) |
| **Winding / Loss Resistance ($R$)** | $R = \frac{W}{I^2}$ | Ohms ($\Omega$) ($W$ is wattmeter reading) |
| **Inductive Reactance ($X_L$)** | $X_L = \sqrt{Z^2 - R^2} = 2\pi f L$ | Ohms ($\Omega$) |
| **Inductance ($L$)** | $L = \frac{X_L}{2\pi f}$ | Henry ($H$ or $mH$) |
| **Capacitive Reactance ($X_C$)** | $X_C = \sqrt{Z^2 - R^2} = \frac{1}{2\pi f C}$ | Ohms ($\Omega$) |
| **Capacitance ($C$)** | $C = \frac{1}{2\pi f X_C}$ | Farads ($F$ or $\mu F$) |
| **Power Factor ($\cos\phi$)** | $\cos\phi = \frac{R}{Z} = \frac{W}{V \cdot I}$ | Dimensionless ($0 \le \cos\phi \le 1$) |
| **Potential Transformer Ratio ($k_{PT}$)** | $k_{PT} = \frac{V_p}{V_s} \approx \frac{N_1}{N_2}$ | Step-down voltage, $V_s \approx 110\text{ V}$ |
| **Current Transformer Ratio ($k_{CT}$)** | $k_{CT} = \frac{I_p}{I_s} \approx \frac{N_2}{N_1}$ | Step-down current, $I_s \approx 5\text{ A}$ or $1\text{ A}$ |
| **Ammeter Shunt Resistance ($R_{sh}$)** | $R_{sh} = \frac{R_m}{m - 1} \quad \text{where } m = \frac{I}{I_m}$ | Low resistance in parallel ($\Omega$) |
| **Voltmeter Multiplier ($R_s$)** | $R_s = (m - 1)R_m \quad \text{where } m = \frac{V}{V_m}$ | High resistance in series ($\Omega$) |
| **True Power with CT & PT** | $P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{reading}}$ | Watts ($W$) or $kW$ |
| **Energy Meter Constant ($K$)** | $K = \frac{\text{Revolutions}}{kWh}$ | $\text{rev}/kWh$ (e.g. 1600 or 1200) |
| **Recorded Energy ($E_{\text{rec}}$)** | $E_{\text{rec}} = \frac{N_{\text{revolutions}}}{K}$ | $kWh$ |
| **True Energy Consumed ($E_{\text{true}}$)** | $E_{\text{true}} = \frac{P \times t}{1000} = \frac{V \cdot I \cdot \cos\phi \times t_{\text{hours}}}{1000}$ | $kWh$ |
| **Stroboscope Speed ($N$)** | $N = \frac{f_m \cdot f_1 \cdot (m - 1)}{f_m - f_1}$ | $RPM$ ($f_m$ = max, $f_1$ = min flash rate) |
| **Minimum Safe Insulation ($R_{\text{ins}}$)** | $R_{\text{ins}} \ge (\text{Rated kV} + 1)\text{ M}\Omega$ | Megohms ($M\Omega$), minimum $1\text{ M}\Omega$ |

---

# Experiment 01: Lab Safety, General Instruments & Pre-Lab Rules

### 1. Core Theory & Everyday Intuition
Measurement is comparing an unknown physical quantity with an accepted standard unit. In an electrical lab, instruments are broadly split into two classes:
- **Absolute (Primary) Instruments:** They directly give the magnitude of the electrical quantity in terms of physical constants without needing comparison with another meter (e.g., Tangent Galvanometer, Rayleigh Current Balance). They are used in national calibration standards laboratories, not routine labs.
- **Secondary Instruments:** The meters we actually use in the lab (PMMC, Moving-Iron, Digital Multimeters, Wattmeters). Their deflection must be calibrated beforehand against an absolute standard.

#### The Three Essential Torques in Indicating Instruments
To make an analog needle pointer move and give a steady, trustworthy reading, three distinct forces (torques) must work together:
1. **Deflecting Torque ($T_d$):**
   - The force that pulls the pointer away from zero when current flows.
   - It is produced using different physical effects: magnetic (PMMC), electromagnetic (Moving-Iron), electrodynamic (Wattmeter), or thermal/electrostatic.
2. **Controlling (Restoring) Torque ($T_c$):**
   - Without a controlling force, the pointer would slam into maximum scale even for a tiny current and would never return to zero when power is shut off.
   - $T_c$ opposes $T_d$ and grows stronger as the pointer deflects further. The needle comes to rest precisely when **$T_d = T_c$**.
   - **How it is produced:**
     - **Spring Control (Most Common):** Two hairsprings made of **Phosphor Bronze** (non-magnetic, zero magnetic distortion, very low mechanical fatigue). Here, $T_c \propto \theta$ (deflection angle is linear).
     - **Gravity Control:** Small adjustable weights on the spindle. Here, $T_c \propto \sin\theta$ (produces a cramped, non-linear scale at the bottom). Must be kept strictly vertical.
3. **Damping Torque ($T_d'$):**
   - Because the moving system has inertia and springs are bouncy, the needle wants to oscillate back and forth around the steady reading for a long time. Damping stops this bouncing quickly without altering the final reading.
   - **Eddy Current Damping:** Aluminum former moving in a strong permanent magnetic field creates eddy currents that oppose motion (Lenz's Law). **Used exclusively in PMMC instruments**.
   - **Air Friction Damping:** A light aluminum vane moves inside a sealed air chamber. **Used in Moving-Iron (MI) and Electrodynamometer instruments** (because permanent magnets used for eddy damping would distort their weak operating fields).
   - **Fluid Friction Damping:** Vanes dip into high-viscosity damping oil (used in high-voltage electrostatic voltmeters).
   - **Damping State:** Instruments are designed to be **critically damped** (or slightly under-damped) so the needle reaches its final position in the shortest time without lingering oscillations.

#### Why Meters Affect the Circuit: The "Loading Effect"
Whenever you attach an instrument to a circuit, the instrument itself consumes a tiny bit of electrical energy, which can change the circuit voltages and currents you are trying to measure:
- **Voltmeter Connection Rule:** A voltmeter is connected in **parallel** across two nodes.
  - To avoid stealing current from the circuit branch, an ideal voltmeter must have **infinite input resistance ($R_{in} = \infty$)**.
  - A real voltmeter must have the highest possible resistance (expressed as sensitivity in $\Omega/\text{V}$). If its resistance is too low, it "loads" the circuit, pulling extra current through source resistances and showing a lower voltage than was actually there.
- **Ammeter Connection Rule:** An ammeter is connected in **series** inside a wire branch.
  - To avoid introducing an accidental resistance that chokes the line current, an ideal ammeter must have **zero internal resistance ($R_m = 0$)**.
  - Connecting an ammeter in parallel across a voltage line is catastrophic: its near-zero resistance creates a **dead short circuit**, blowing fuses or destroying the meter movement.

#### The Variac (Auto-Transformer)
A Variac is an autotransformer with a single continuous copper winding wrapped around a toroidal iron core, with a movable carbon brush riding along bare turns.
- It allows you to adjust AC output smoothly from $0\text{ V}$ up to rated line voltage (e.g. $220\text{ V}$ or $250\text{ V}$).
- **Crucial Safety Note:** Because primary and secondary share the same physical winding, **a Variac offers NO galvanic isolation**. If the neutral or live wire is inverted, touching the secondary circuit can cause a lethal electric shock. Always start tests with the knob turned down to zero.

---

### 2. Maths & Numerical Problems (Exp 01)

#### Formula & Concept: Limiting Error & Guarantee Accuracy
Instrument manufacturers specify accuracy as a percentage of Full-Scale Deflection (FSD):
$$\text{Max Absolute Error} = \pm (\% \text{Accuracy}) \times \text{Full Scale Value}$$
$$\text{Percentage Limiting Error at a Reading } V = \frac{\text{Max Absolute Error}}{V} \times 100\%$$
*Key Insight:* The absolute error stays constant over the whole dial. Therefore, reading a small quantity near the low end of a large-scale meter produces a huge percentage error. Always choose a meter where your expected reading falls in the **upper half or top third of the scale**.

**Problem 1.1:**  
A $0 - 300\text{ V}$ analog voltmeter has a guaranteed accuracy of $\pm 1.5\%$ of full scale.  
1. Calculate the maximum absolute error in Volts.  
2. If the voltmeter reads $60\text{ V}$, what is the true limiting percentage error of this measurement?  
3. If it reads $250\text{ V}$, what is the limiting percentage error?

**Step-by-Step Solution:**  
1. $\text{Max Absolute Error} = \pm \left(\frac{1.5}{100}\right) \times 300\text{ V} = \mathbf{\pm 4.5\text{ V}}$.  
2. At $60\text{ V}$ reading:  
   $$\% \text{Error} = \frac{\pm 4.5\text{ V}}{60\text{ V}} \times 100\% = \mathbf{\pm 7.5\%} \quad (\text{Very poor accuracy!})$$  
3. At $250\text{ V}$ reading:  
   $$\% \text{Error} = \frac{\pm 4.5\text{ V}}{250\text{ V}} \times 100\% = \mathbf{\pm 1.8\%} \quad (\text{Much higher accuracy!})$$

---

# Experiment 02: Unknown Resistance using Wheatstone Bridge

### 1. Core Theory & Everyday Intuition
![Wheatstone Bridge](attachments/meas_exp02_wheatstone_bridge.png)

The Wheatstone bridge is the gold standard for measuring **medium resistance** (from $1\,\Omega$ up to roughly $100\,k\Omega$).

#### Why it is Far Better than a Simple Ohmmeter: The Null Principle
A typical ohmmeter measures resistance by passing current from an internal battery through a meter coil and observing the pointer deflection. If the battery gets old, or the meter springs weaken, the reading is wrong.  
A Wheatstone bridge works on the **null-deflection comparison principle**:
- You adjust a calibrated variable resistor $S$ until the sensitive galvanometer between the bridge arms reads **exactly zero ($I_g = 0$)**.
- Because no current flows through the detector at balance, the measurement does **not depend on battery voltage**, internal battery resistance, or galvanometer calibration. It depends purely on the precision of the passive ratio arms!

#### Working Principle & Balance Condition
The circuit has four resistance arms arranged in a closed diamond loop:
- **Ratio arms:** $P$ and $Q$ (precision fixed resistors).
- **Standard arm:** $S$ (calibrated decade resistance box).
- **Unknown arm:** $R$ (resistor being measured).
- A DC voltage source ($V_s$) is connected across one pair of opposing diagonal junctions, and a sensitive D'Arsonval Galvanometer ($G$) is connected across the other pair.

When current in the galvanometer branch is zero, the voltage drop across arm $P$ equals the drop across arm $Q$, and the voltage drop across arm $R$ equals the drop across arm $S$:
$$I_1 P = I_2 Q \quad \text{and} \quad I_1 R = I_2 S$$
Dividing these two expressions gives the universal balance equation:
$$\frac{P}{R} = \frac{Q}{S} \implies P \cdot R = Q \cdot S \implies \mathbf{R = \left(\frac{Q}{P}\right) \cdot S}$$

#### Key Practical Insights & Exam Traps:
1. **Reciprocity:** If you swap the battery and the galvanometer terminals, the bridge balance condition remains completely unchanged ($P \cdot R = Q \cdot S$).
2. **Maximum Sensitivity Rule:** The galvanometer shows the biggest, easiest-to-see deflection for a tiny change in $R$ when all four arms have roughly equal resistance ($P \approx Q \approx R \approx S$).
3. **Why NOT used for Low Resistance ($< 1\,\Omega$):** The resistance of the connecting lead wires and terminal binding posts is typically $0.005\,\Omega$ to $0.05\,\Omega$. If you try to measure a $0.1\,\Omega$ shunt resistor, lead resistance adds directly to $R$, causing a huge error of $10\%$ to $50\%$. *(For low resistance, we use the **Kelvin Double Bridge**)*.
4. **Why NOT used for High Resistance ($> 100\,k\Omega$):** The total bridge resistance becomes so gigantic that the current drawn from the battery is in fractions of a micro-ampere. The galvanometer barely moves even when the bridge is heavily unbalanced, making it impossible to pinpoint the null point. Furthermore, insulation leakage across the circuit board shunts the bridge arms. *(For high resistance, we use a **Megger** or Loss of Charge method)*.
5. **Thermoelectric EMF Error:** When different metals in the circuit meet at slightly different temperatures, a tiny thermal battery (Seebeck voltage) is formed. This is eliminated by taking two readings with reversed battery polarity and averaging them.

---

### 2. Maths & Numerical Problems (Exp 02)

#### Master Formula:
$$R = \left(\frac{Q}{P}\right) \cdot S$$
$$\text{Percentage Error } \%e = \frac{|R_{\text{actual}} - R_{\text{measured}}|}{R_{\text{actual}}} \times 100\%$$

**Problem 2.1 (Direct Lab Bridge Calculation):**  
In a lab experiment, ratio arms are set to $P = 100\,\Omega$ and $Q = 1000\,\Omega$. When standard resistance $S$ is adjusted to $37.4\,\Omega$, the galvanometer needle points exactly to zero.  
1. Determine the unknown resistance $R$.  
2. If the manufacturer's nominal value marked on the resistor body is $38.0\,\Omega$, calculate the percentage measurement error.

**Step-by-Step Solution:**  
1. Using the balance equation:  
   $$R = \frac{Q}{P} \cdot S = \frac{1000}{100} \times 37.4\,\Omega = 10 \times 37.4\,\Omega = \mathbf{374\,\Omega}$$  
2. Percentage error:  
   $$\%e = \frac{|38.0 - 37.4|}{38.0} \times 100\% = \frac{0.6}{38.0} \times 100\% = \mathbf{1.58\%}$$

**Problem 2.2 (Bridge Arm Voltage Drops):**  
A Wheatstone bridge has $P = 1000\,\Omega$, $Q = 100\,\Omega$, $S = 50\,\Omega$, and is connected across a $10\text{ V}$ DC supply. Calculate the value of $R$ at balance, and the current drawn from the battery.  
**Step-by-Step Solution:**  
1. At balance: $R = \frac{P}{Q} \cdot S = \frac{1000}{100} \times 50 = \mathbf{500\,\Omega}$.  
2. Equivalent resistance of branch 1 ($P + R$ in series): $R_{b1} = 1000 + 500 = 1500\,\Omega$.  
3. Equivalent resistance of branch 2 ($Q + S$ in series): $R_{b2} = 100 + 50 = 150\,\Omega$.  
4. Total bridge resistance:  
   $$R_{\text{total}} = \frac{R_{b1} \times R_{b2}}{R_{b1} + R_{b2}} = \frac{1500 \times 150}{1500 + 150} = \frac{225000}{1650} \approx \mathbf{136.36\,\Omega}$$  
5. Battery current:  
   $$I_{\text{total}} = \frac{V_s}{R_{\text{total}}} = \frac{10\text{ V}}{136.36\,\Omega} \approx \mathbf{0.0733\text{ A}}\quad (73.3\text{ mA})$$

---

# Experiment 03: Inductance of an Inductor (3-Meter Method)

### 1. Core Theory & Everyday Intuition
![Inductance Circuit](attachments/meas_exp03_inductance_circuit.png)

#### Why Can't We Just Use a Voltmeter and Ammeter?
In a pure AC inductor, current is limited only by inductive reactance: $X_L = 2\pi f L$. If inductors were ideal, you could simply calculate $L = \frac{V}{2\pi f I}$.  
However, **every real inductor is a coil of physical copper wire wound on a core**. This wire has real internal resistance ($R$), and if an iron core is present, there are hysteresis and eddy current core losses.
- Voltmeter gives total terminal voltage $V$.
- Ammeter gives total RMS circuit current $I$.
- The ratio $\frac{V}{I}$ gives the **total impedance ($Z$)**, NOT the pure reactance $X_L$!
- To separate the resistive copper loss from the inductive storage, we need a **Wattmeter** ($W$).

#### How the 3 Meters Work Together:
1. An electrodynamometer wattmeter measures **active real power**:
   $$W = I^2 R \implies \mathbf{R = \frac{W}{I^2}}$$
   *(This gives the effective AC resistance of the coil winding!)*
2. The voltmeter and ammeter together give the magnitude of total opposition:
   $$\mathbf{Z = \frac{V}{I}}$$
3. By the AC impedance triangle ($Z^2 = R^2 + X_L^2$), the inductive reactance is:
   $$\mathbf{X_L = \sqrt{Z^2 - R^2}}$$
4. Knowing line frequency ($f = 50\text{ Hz}$ in Bangladesh), inductance in Henrys is isolated:
   $$X_L = 2\pi f L \implies \mathbf{L = \frac{X_L}{2\pi f}}$$
5. The coil power factor is:
   $$\cos\phi = \frac{R}{Z} = \frac{W}{V \cdot I} \quad (\text{Lagging})$$

#### Essential Meter Connections & Practical Rules:
- **Wattmeter Current Coil (CC):** Low resistance, thick wire. Connected in **series** with the line to carry full load current.
- **Wattmeter Potential Coil (PC):** High resistance, fine wire. Connected in **parallel** across the load to sense voltage.
- **Variac Role:** Connected at the AC input. Allows raising voltage slowly from $0\text{ V}$. An inductor has very low resistance to DC; even under AC, sudden application of full voltage can cause high transient inrush currents.
- **Ideal Inductor Reality Check:** If the coil were ideal ($R = 0$), the wattmeter reading would be exactly $0\text{ W}$, and $\cos\phi = 0$ (current lags voltage by a full $90^\circ$). In our lab, the wattmeter reads positive watts because of real copper resistance!

---

### 2. Maths & Numerical Problems (Exp 03)

#### Calculation Workflow:
1. $Z = \frac{V}{I}$
2. $R = \frac{W}{I^2}$
3. $X_L = \sqrt{Z^2 - R^2}$
4. $L = \frac{X_L}{2\pi f} = \frac{X_L}{314.16}$ (for $50\text{ Hz}$)
5. $\cos\phi = \frac{R}{Z}$

**Problem 3.1 (Direct Lab Data Calculation):**  
In a $50\text{ Hz}$ measurement test on a choke coil (similar to the lab manual data table), the meters record:
- Voltmeter: $V = 220\text{ V}$
- Ammeter: $I = 3.0\text{ A}$
- Wattmeter: $W = 68\text{ W}$  
Calculate the winding resistance, impedance, inductive reactance, inductance, and power factor.

**Step-by-Step Solution:**  
1. **Total Impedance ($Z$):**  
   $$Z = \frac{V}{I} = \frac{220\text{ V}}{3.0\text{ A}} = \mathbf{73.33\,\Omega}$$  
2. **Winding Resistance ($R$):**  
   $$R = \frac{W}{I^2} = \frac{68}{(3.0)^2} = \frac{68}{9} = \mathbf{7.56\,\Omega}$$  
3. **Inductive Reactance ($X_L$):**  
   $$X_L = \sqrt{Z^2 - R^2} = \sqrt{(73.33)^2 - (7.56)^2} = \sqrt{5377.29 - 57.15} = \sqrt{5320.14} = \mathbf{72.94\,\Omega}$$  
4. **Inductance ($L$):**  
   $$L = \frac{X_L}{2\pi f} = \frac{72.94}{2 \times \pi \times 50} = \frac{72.94}{314.16} \approx \mathbf{0.232\text{ H}}\quad (232\text{ mH})$$  
5. **Power Factor ($\cos\phi$):**  
   $$\cos\phi = \frac{R}{Z} = \frac{7.56}{73.33} \approx \mathbf{0.103\text{ lagging}}$$

---

# Experiment 04: Capacitance of a Capacitor (3-Meter Method)

### 1. Core Theory & Everyday Intuition
![Capacitance Circuit](attachments/meas_exp04_capacitance_circuit.png)

#### Why Does a Capacitor Need a 3-Meter Method?
In an ideal capacitor, the dielectric material is a perfect insulator. Current leads voltage by exactly $90^\circ$, meaning average active power consumed is zero ($W = 0$).  
In any physical capacitor:
- There is a small leakage current passing through the dielectric material, plus dielectric molecular friction (dielectric hysteresis).
- These effects are modeled as an **Equivalent Series Resistance (ESR)** or parallel leakage resistance.
- The wattmeter measures this tiny active power loss ($W = I^2 R$).

#### Mathematical Separation:
1. Total Impedance: $\mathbf{Z = \frac{V}{I}}$
2. Effective Loss Resistance: $\mathbf{R = \frac{W}{I^2}}$
3. Capacitive Reactance: $\mathbf{X_C = \sqrt{Z^2 - R^2}}$
4. Capacitance: Since $X_C = \frac{1}{2\pi f C}$, we get:
   $$\mathbf{C = \frac{1}{2\pi f X_C} = \frac{10^6}{2\pi f X_C} \quad [\mu\text{F}]}$$
5. Dissipation Factor ($\tan\delta$): Ratio of loss resistance to reactance:
   $$\tan\delta = \frac{R}{X_C}$$
   *(For high quality power capacitors, $R \approx 0$, so $\tan\delta \approx 0$ and $X_C \approx Z$)*.

#### Crucial Lab Safety Rules for Capacitors:
- **Polarity Warning:** Only **non-polar (bipolar) AC capacitors** (e.g., oil-filled, paper, or metallized polypropylene) can be used. Ordinary polarized electrolytic capacitors will internally short, vent gas, and explode if subjected to AC!
- **Lethal Shock Hazard:** Capacitors store electrostatic energy ($E = \frac{1}{2} C V^2$). When you switch off the AC power, the capacitor may remain charged at the peak voltage ($V_{\text{peak}} = \sqrt{2} \times 220\text{ V} \approx 311\text{ V}$). Always short-circuit the capacitor terminals through a discharge resistor before touching any wires!

---

### 2. Maths & Numerical Problems (Exp 04)

**Problem 4.1 (From Lab Manual Data Table):**  
A capacitor connected to a $50\text{ Hz}$ supply gives the following meter readings:
- Voltmeter: $V = 100\text{ V}$
- Ammeter: $I = 0.4\text{ A}$
- Wattmeter: $W = 3.0\text{ W}$  
Calculate the equivalent loss resistance, impedance, capacitive reactance, and capacitance in microfarads ($\mu\text{F}$).

**Step-by-Step Solution:**  
1. **Total Impedance ($Z$):**  
   $$Z = \frac{V}{I} = \frac{100\text{ V}}{0.4\text{ A}} = \mathbf{250\,\Omega}$$  
2. **Loss Resistance ($R$):**  
   $$R = \frac{W}{I^2} = \frac{3.0}{(0.4)^2} = \frac{3.0}{0.16} = \mathbf{18.75\,\Omega}$$  
3. **Capacitive Reactance ($X_C$):**  
   $$X_C = \sqrt{Z^2 - R^2} = \sqrt{(250)^2 - (18.75)^2} = \sqrt{62500 - 351.56} = \sqrt{62148.44} = \mathbf{249.29\,\Omega}$$  
4. **Capacitance ($C$):**  
   $$C = \frac{1}{2\pi f X_C} = \frac{1}{2 \times \pi \times 50 \times 249.29} = \frac{1}{78318.5} \approx 12.76 \times 10^{-6}\text{ F} = \mathbf{12.76\,\mu\text{F}}$$

---

# Experiments 05 & 06: Potential Transformer (PT) & Current Transformer (CT)

### 1. Core Theory & Everyday Intuition
![PT Circuit](attachments/meas_exp05_pt_circuit.png)  
*Potential Transformer (PT) Circuit Setup*

![CT Circuit](attachments/meas_exp06_ct_circuit.png)  
*Current Transformer (CT) Circuit Setup*

#### Why Do We Need Instrument Transformers?
In electrical power grids, voltages reach $11\text{ kV}, 33\text{ kV}, 132\text{ kV}$ and currents reach $500\text{ A}$ to $2000\text{ A}$.  
Building an ammeter with wires thick enough to handle $1000\text{ A}$, or a voltmeter with enough insulation to withstand $33\text{ kV}$, would make instruments huge, dangerous, and absurdly expensive.  
**Instrument transformers solve this with two core benefits:**
1. **Standardization:** They step high values down to safe, universally standardized meter levels:
   - **PT secondary standard:** Always **$110\text{ V}$** (or $100\text{ V}$).
   - **CT secondary standard:** Always **$5\text{ A}$** (or $1\text{ A}$).
2. **Safety Isolation:** They create galvanic magnetic isolation between dangerous high-voltage lines and the operator holding the meters.

---

#### Detailed Breakdown: Potential Transformer (PT)
- **What it is:** A high-precision, low-power **step-down voltage transformer** ($N_1 > N_2$).
- **Connection:** Primary connects in **parallel** across the high voltage line. Secondary connects across a standard $0 - 150\text{ V}$ voltmeter.
- **Operating Condition:** Because the voltmeter has very high input resistance, the secondary winding operates practically on **open circuit**.
- **Voltage Transformation Ratio:**
  $$k_{PT} = \frac{V_p}{V_s} \approx \frac{N_1}{N_2}$$
- **Grounding Safety Requirement:** One terminal of the secondary winding **must be solidly connected to earth ground**. If the internal primary-to-secondary winding insulation ever punctures, the ground wire directs the high-voltage fault current straight to earth, preventing $11\text{ kV}$ from appearing on the switchboard meters.

---

#### Detailed Breakdown: Current Transformer (CT)
- **What it is:** A specialized **step-up voltage, step-down current transformer** ($N_2 \gg N_1$).
- **Connection:** Primary winding has very few turns of heavy conductor (frequently a **single straight bar** passing through a toroid core, where $N_1 = 1$) connected in **series** with the load line. Secondary winding has many turns of fine wire connected across a low-resistance $0 - 5\text{ A}$ ammeter.
- **Operating Condition:** Because an ammeter has near-zero internal resistance, the CT operates practically in a **continuous short-circuit condition**.
- **Current Transformation Ratio:**
  $$k_{CT} = \frac{I_p}{I_s} \approx \frac{N_2}{N_1}$$

---

#### ⚠️ THE NUMBER ONE EXAM QUESTION: Why Must a CT Secondary NEVER Be Opened While Energized?
This is the most asked viva and quiz question in electrical engineering:
1. **Under Normal Operation:**  
   Primary current $I_1$ produces primary ampere-turns ($N_1 I_1$). The secondary current $I_2$ produces a counter-MMF ($N_2 I_2$) that directly opposes the primary MMF. The net flux in the core is the small difference:
   $$\text{Net MMF} = N_1 I_1 - N_2 I_2 \approx \text{Very Small (Magnetizing MMF)}$$
   The core operates safely far below magnetic saturation.
2. **What Happens if Secondary is Open-Circuited ($I_2 = 0$):**
   - The opposing counter-MMF immediately vanishes ($N_2 I_2 = 0$).
   - **The entire primary line current (which is fixed by the external power system load) now acts as pure, unopposed magnetizing current!**
   - The magnetic flux in the core explodes to extreme saturation levels.
3. **The Catastrophic Consequences:**
   - **Lethal Voltage Spike:** Because flux alternates and the secondary has hundreds or thousands of turns ($N_2$), Faraday's Law ($e_2 = -N_2 \frac{d\Phi}{dt}$) induces **dangerously high peak voltages (several kilovolts)** across the open secondary terminals, presenting a lethal shock risk to anyone nearby.
   - **Violent Overheating:** Severe core saturation causes huge eddy current and hysteresis losses, rapidly cooking and burning the winding insulation.
   - **Permanent Core Magnetization:** The core is left with high residual magnetism, permanently ruining its calibration ratio and accuracy.
- **Golden Rule:** Always **short-circuit the CT secondary terminals** with a link before removing or replacing an ammeter!

---

### 2. Maths & Numerical Problems (Exp 05 & 06)

**Problem 5.1 (PT Voltage Calculation):**  
A Potential Transformer rated at $11000/110\text{ V}$ is connected to a substation voltmeter. The voltmeter scale reads $104.5\text{ V}$. Find:
1. The transformer turns ratio ($k_{PT}$).
2. The actual high voltage on the transmission line.

**Step-by-Step Solution:**  
1. Turns ratio:  
   $$k_{PT} = \frac{V_{\text{rated, pri}}}{V_{\text{rated, sec}}} = \frac{11000}{110} = \mathbf{100}$$  
2. Actual primary line voltage:  
   $$V_{\text{actual}} = k_{PT} \times V_{\text{measured}} = 100 \times 104.5\text{ V} = \mathbf{10450\text{ V}}\quad (10.45\text{ kV})$$

**Problem 6.1 (CT Current Calculation):**  
A bar-type CT has a single primary turn ($N_1 = 1$) and $200$ secondary turns ($N_2 = 200$). The secondary ammeter reads $3.8\text{ A}$.  
1. What is the current transformation ratio ($k_{CT}$)?  
2. What is the actual current flowing in the main busbar?

**Step-by-Step Solution:**  
1. Transformation ratio:  
   $$k_{CT} \approx \frac{N_2}{N_1} = \frac{200}{1} = \mathbf{200}$$  
2. Busbar primary current:  
   $$I_p = k_{CT} \times I_s = 200 \times 3.8\text{ A} = \mathbf{760\text{ A}}$$

---

# Experiments 07 & 08: Extension of Ammeter & Voltmeter Ranges

### 1. Core Theory & Everyday Intuition
![Ammeter Extension](attachments/meas_exp07_ammeter_extension.png)  
*Ammeter Extension with Shunt ($R_{sh}$)*

![Voltmeter Extension](attachments/meas_exp08_voltmeter_extension.png)  
*Voltmeter Extension with Multiplier ($R_s$)*

Every basic analog meter movement (specifically a Permanent Magnet Moving Coil - PMMC) is naturally a delicate micro-ammeter or milli-ammeter. Its tiny hairsprings and fine coil wire can only tolerate a tiny current (e.g., $1\text{ mA}$ or $10\text{ mA}$) before burning up.  
To measure large industrial currents (e.g., $50\text{ A}$) or large voltages (e.g., $500\text{ V}$), we modify the circuit around the movement.

---

#### 1. Ammeter Range Extension (The Shunt)
- **Concept:** Connect a very **low resistance (Shunt, $R_{sh}$)** in **parallel** with the meter coil ($R_m$).
- **Current Division:** The large line current $I$ splits at the node: a tiny safe fraction $I_m$ flows through the meter coil, while the vast majority $I_{sh} = I - I_m$ safely bypasses through the low-resistance shunt.
- **Mathematical Derivation:**
  Because both branches are in parallel, their voltage drops are identical:
  $$V_{\text{drop}} = I_m R_m = I_{sh} R_{sh} = (I - I_m) R_{sh}$$
  $$R_{sh} = \frac{I_m R_m}{I - I_m} = \frac{R_m}{\frac{I}{I_m} - 1}$$
  Defining the **Multiplying Factor ($m$)** as the ratio of total target current to meter full-scale current:
  $$\mathbf{m = \frac{I}{I_m}} \implies \mathbf{R_{sh} = \frac{R_m}{m - 1}}$$
- **Material Selection for Shunt:**
  The shunt **must be made of Manganin** (an alloy of $84\%$ Copper, $12\%$ Manganese, $4\%$ Nickel).
  - *Why not Copper?* Copper has a high positive temperature coefficient of resistance ($+0.00393/\text{^\circ C}$). As large currents heat up a copper shunt, its resistance would rise, forcing extra current into the meter coil and ruining accuracy.
  - *Why Manganin?* Manganin has a **virtually zero temperature coefficient of resistance** and zero thermoelectric voltage when joined to copper terminals!

---

#### 2. Voltmeter Range Extension (The Multiplier)
- **Concept:** Connect a very **high resistance (Multiplier, $R_s$)** in **series** with the meter movement ($R_m$).
- **Voltage Division:** The total voltage $V$ is shared between the multiplier and the coil. The multiplier drops almost the entire line voltage, leaving only a tiny millivolt drop ($V_m = I_m R_m$) across the fragile meter coil.
- **Mathematical Derivation:**
  The same full-scale current $I_m$ passes through both series elements:
  $$V = I_m (R_m + R_s)$$
  $$\frac{V}{I_m} = R_m + R_s \implies R_s = \frac{V}{I_m} - R_m = \left(\frac{V}{I_m R_m} - 1\right) R_m$$
  Since $V_m = I_m R_m$ is the original full-scale voltage of the basic movement, defining the **Multiplying Factor ($m$):**
  $$\mathbf{m = \frac{V}{V_m}} \implies \mathbf{R_s = (m - 1) R_m}$$
- **Material Selection:** Non-inductively wound wire made of **Manganin** or **Constantan**.
- **Added Benefit:** Adding a high multiplier resistance increases total voltmeter resistance ($R_{\text{total}} = R_m + R_s$), which dramatically **reduces circuit loading error**!

---

### Summary Comparison Table: Shunt vs Multiplier

| Feature | Ammeter Extension (Shunt) | Voltmeter Extension (Multiplier) |
| :--- | :--- | :--- |
| **How It Connects** | **Parallel** with the meter coil | **Series** with the meter coil |
| **Resistance Magnitude**| **Extremely LOW** ($R_{sh} \ll R_m$) | **Extremely HIGH** ($R_s \gg R_m$) |
| **Core Formula** | $R_{sh} = \frac{R_m}{m - 1}$ | $R_s = (m - 1)R_m$ |
| **Multiplying Factor ($m$)** | $m = \frac{I_{\text{target}}}{I_{\text{meter}}}$ | $m = \frac{V_{\text{target}}}{V_{\text{meter}}}$ |
| **Standard Material** | **Manganin** (near-zero temp coefficient) | **Manganin** or **Constantan** |

---

### 2. Maths & Numerical Problems (Exp 07 & 08)

**Problem 7.1 (Ammeter Shunt Design):**  
A moving-coil milliammeter has an internal coil resistance of $R_m = 20\,\Omega$ and gives full-scale deflection with a current of $I_m = 5\text{ mA}$ ($0.005\text{ A}$). Calculate the shunt resistance required to convert it into an ammeter reading up to $10\text{ A}$.

**Step-by-Step Solution:**  
1. **Find Multiplying Factor ($m$):**  
   $$m = \frac{I}{I_m} = \frac{10\text{ A}}{0.005\text{ A}} = \mathbf{2000}$$  
2. **Calculate Shunt Resistance ($R_{sh}$):**  
   $$R_{sh} = \frac{R_m}{m - 1} = \frac{20\,\Omega}{2000 - 1} = \frac{20}{1999} \approx \mathbf{0.010005\,\Omega}\quad (\approx 10\text{ m}\Omega)$$

**Problem 8.1 (Voltmeter Multiplier Design):**  
A basic moving-coil movement has a resistance of $R_m = 50\,\Omega$ and produces full-scale deflection with $2\text{ mA}$ ($0.002\text{ A}$). It is desired to use this movement as a voltmeter reading up to $250\text{ V}$.  
1. Find the original full-scale voltage rating of the bare movement ($V_m$).  
2. Calculate the required series multiplier resistance ($R_s$).  
3. Determine the sensitivity of the resulting voltmeter in $\Omega/\text{V}$.

**Step-by-Step Solution:**  
1. **Bare movement voltage:**  
   $$V_m = I_m \times R_m = 0.002\text{ A} \times 50\,\Omega = \mathbf{0.1\text{ V}}\quad (100\text{ mV})$$  
2. **Multiplying factor ($m$):**  
   $$m = \frac{V}{V_m} = \frac{250\text{ V}}{0.1\text{ V}} = \mathbf{2500}$$  
3. **Multiplier resistance ($R_s$):**  
   $$R_s = (m - 1) R_m = (2500 - 1) \times 50 = 2499 \times 50 = \mathbf{124950\,\Omega}\quad (124.95\text{ k}\Omega)$$  
4. **Voltmeter Sensitivity ($S$):**  
   $$S = \frac{1}{I_{\text{FSD}}} = \frac{1}{0.002\text{ A}} = \mathbf{500\,\Omega/\text{V}}$$  
   *(Check: Total resistance $= S \times V_{\text{range}} = 500 \times 250 = 125000\,\Omega = R_s + R_m$)*.

---

# Experiment 09: Electrical Energy Consumption using Energy Meter

### 1. Core Theory & Everyday Intuition
![Energy Meter Circuit](attachments/meas_exp09_energy_meter_circuit.png)

An electrical energy meter measures the total integral of power consumed over time:
$$\text{Energy} = \int P \, dt = \int V \cdot I \cdot \cos\phi \, dt \quad [\text{in Kilowatt-hours, } kWh]$$
One commercial unit of electricity = **$1\text{ kWh} = 1000\text{ Watts for 1 hour} = 3.6 \times 10^6\text{ Joules}$** (also called 1 Board of Trade Unit).

#### The 4 Mechanical Systems Inside the Meter:
1. **Driving System:**
   - **Shunt Magnet (Voltage Coil):** Wound with many turns of thin wire, highly inductive. Connected directly across line voltage $V$. Its magnetic flux $\Phi_{sh}$ is proportional to $V$ and lags $V$ by nearly $90^\circ$.
   - **Series Magnet (Current Coil):** Wound with few turns of thick wire, very low impedance. Connected in series with load current $I$. Its magnetic flux $\Phi_{se}$ is in phase with line current $I$.
   - These two alternating fluxes penetrate an aluminum disc, inducing circulating **eddy currents**. The interaction between fluxes and eddy currents produces a continuous **deflecting/driving torque ($T_d$)**:
     $$\mathbf{T_d \propto V \cdot I \cdot \cos\phi \propto \text{Active Power } (P)}$$
2. **Moving System:**
   - A light, flat aluminum disc mounted on a vertical spindle resting on a jewel sapphire bearing to minimize mechanical friction.
3. **Braking System:**
   - A permanent horseshoe magnet placed near the edge of the aluminum disc.
   - As the disc spins through this steady magnetic field, eddy currents are induced in the disc. According to Lenz's law, these eddy currents exert an opposing retarding force:
     $$\mathbf{T_b \propto N} \quad (\text{Braking torque is directly proportional to disc speed } N \text{ in RPM})$$
   - **Crucial Balance:** When disc speed stabilizes, driving torque equals braking torque:
     $$T_d = T_b \implies P \propto N \implies \int P \, dt \propto \int N \, dt \implies \mathbf{\text{Energy} \propto \text{Total Revolutions}}$$
4. **Registering System:**
   - A train of small gear wheels with a worm screw attached to the spindle that turns decimal number dials, reading energy directly in $kWh$.

---

#### ⚠️ THE KEY LAB HAZARD: Creeping Error & How to Fix It
- **What is Creeping?**  
  Creeping is the slow, continuous rotation of the aluminum disc when **there is NO electrical load connected** (load current $I = 0$), but the voltage coil remains energized across the line. (The user is being billed even with all switches off!).
- **What Causes It?**
  1. **Over-compensation for mechanical friction:** To help the meter start smoothly on tiny loads, technicians add a small adjustable copper shading loop on the shunt magnet to produce an artificial forward torque. If this compensation is slightly too aggressive, the disc turns by itself without any load!
  2. Stray magnetic fields, vibration, or excessive supply line voltage.
- **How Engineers Prevent Creeping:**  
  By drilling **two small diametrically opposite holes** in the aluminum disc.
  - *How it works:* When one hole rotates directly under the pole of the shunt magnet, the high-reluctance hole distorts the path of the eddy currents. This creates a small magnetic pull that traps the hole under the pole, stalling the disc against the slight friction-compensating torque. Once a real load turns on, the driving torque easily overcomes this notch, and normal measurement resumes.

#### Testing Method: Phantom (Fictitious) Loading
Testing a large commercial energy meter ($220\text{ V}, 50\text{ A}$) at full rated load for hours would waste $11\text{ kW}$ of real power.  
Instead, labs use **Phantom Loading**:
- The voltage coil (high resistance) is energized from the normal $220\text{ V}$ line (drawing negligible current).
- The current coil (very low resistance) is energized from an independent low-voltage source (e.g. $4\text{ V}$ to $6\text{ V}$) that can push the full $50\text{ A}$ through the coil without dissipating large power. Total power used during testing is a tiny fraction of normal operation!

---

### 2. Maths & Numerical Problems (Exp 09)

#### Formulas:
1. **Meter Constant ($K$):**  
   $$K = \frac{\text{Total Revolutions}}{\text{Energy in } kWh} \quad [\text{rev}/kWh]$$
2. **Recorded Energy from Disc Revolutions:**  
   $$E_{\text{recorded}} = \frac{N_{\text{revolutions}}}{K} \quad [kWh]$$
3. **True Energy Consumed:**  
   $$E_{\text{true}} = \frac{P \times t}{1000} = \frac{V \cdot I \cdot \cos\phi \times \left(\frac{t_{\text{seconds}}}{3600}\right)}{1000} \quad [kWh]$$
4. **Percentage Error:**  
   $$\%e = \frac{E_{\text{recorded}} - E_{\text{true}}}{E_{\text{true}}} \times 100\%$$
   - A **positive error ($+e$)** means the meter runs **FAST** (over-registering).
   - A **negative error ($-e$)** means the meter runs **SLOW** (under-registering).

**Problem 9.1 (Lab Calibration Test):**  
An energy meter has a nameplate rating of $K = 1200\text{ rev}/kWh$. In a calibration test, it is connected to a $220\text{ V}$ supply and carries a current of $5\text{ A}$ at unity power factor ($\cos\phi = 1.0$). The disc makes $38$ revolutions in $100\text{ seconds}$.  
1. Calculate the true energy consumed in $kWh$.  
2. Calculate the energy recorded by the meter in $kWh$.  
3. Calculate the percentage error of the meter. Is it running fast or slow?

**Step-by-Step Solution:**  
1. **True Energy Consumed ($E_{\text{true}}$):**  
   $$P = V \cdot I \cdot \cos\phi = 220 \times 5 \times 1.0 = 1100\text{ W} = 1.1\text{ kW}$$  
   Time in hours: $t = \frac{100}{3600}\text{ hr} = 0.02778\text{ hr}$  
   $$E_{\text{true}} = 1.1\text{ kW} \times 0.02778\text{ hr} \approx \mathbf{0.03056\text{ kWh}}$$  
2. **Recorded Energy ($E_{\text{recorded}}$):**  
   $$E_{\text{recorded}} = \frac{N}{K} = \frac{38}{1200} \approx \mathbf{0.03167\text{ kWh}}$$  
3. **Percentage Error:**  
   $$\%e = \frac{0.03167 - 0.03056}{0.03056} \times 100\% = \frac{+0.00111}{0.03056} \times 100\% = \mathbf{+3.63\%}$$  
   **Result:** The meter is running **FAST by $3.63\%$**.

---

# Experiment 10: Measurement of Power using CT and PT

### 1. Core Theory & Everyday Intuition
![Power with CT and PT](attachments/meas_exp10_power_ct_pt_circuit.png)

When monitoring high-power transmission or industrial loads (e.g. $11\text{ kV}$ line carrying $400\text{ A}$), you cannot connect an ordinary wattmeter directly to the lines.  
By pairing the wattmeter with both an instrument Potential Transformer (PT) and Current Transformer (CT):
- **Wattmeter Current Coil (CC):** Connects to the **secondary of the CT** ($0 - 5\text{ A}$ range).
- **Wattmeter Potential Coil (PC):** Connects to the **secondary of the PT** ($0 - 110\text{ V}$ range).
- The small benchtop wattmeter now operates at safe, low values while reflecting the high power drawn by the load.

#### Calculation of True System Power:
$$\mathbf{P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{measured}}}$$
where:
- $k_{CT} = \frac{I_{\text{primary}}}{I_{\text{secondary}}}$ (Current Transformation Ratio)
- $k_{PT} = \frac{V_{\text{primary}}}{V_{\text{secondary}}}$ (Potential Transformation Ratio)
- $W_{\text{measured}}$ is the raw power reading on the wattmeter dial.

---

### 2. Maths & Numerical Problems (Exp 10)

**Problem 10.1 (Lab Manual Numerical):**  
In the measurement of power, a CT with turns ratio $k_{CT} = 24$ and a PT with turns ratio $k_{PT} = 2$ are connected to a wattmeter. The wattmeter indicates $384\text{ W}$.  
Calculate the actual power consumed by the load.

**Step-by-Step Solution:**  
$$P_{\text{true}} = k_{CT} \times k_{PT} \times W_{\text{measured}}$$  
$$P_{\text{true}} = 24 \times 2 \times 384\text{ W} = 48 \times 384\text{ W} = \mathbf{18432\text{ W}} \quad (18.432\text{ kW})$$

**Problem 10.2 (Substation Busbar Power):**  
A 3-phase high-voltage feeder at $33\text{ kV}$ uses two wattmeters to measure power. Each wattmeter uses a PT rated at $33000/110\text{ V}$ and a CT rated at $300/5\text{ A}$.  
1. Find the individual ratios $k_{PT}$ and $k_{CT}$.  
2. What is the overall multiplying factor to convert raw wattmeter readings to actual megawatts?  
3. If wattmeter 1 reads $180\text{ W}$ and wattmeter 2 reads $120\text{ W}$, find total line power.

**Step-by-Step Solution:**  
1. **Ratios:**  
   $$k_{PT} = \frac{33000}{110} = \mathbf{300}, \quad k_{CT} = \frac{300}{5} = \mathbf{60}$$  
2. **Overall Multiplying Factor ($MF$):**  
   $$MF = k_{PT} \times k_{CT} = 300 \times 60 = \mathbf{18000}$$  
3. **Total Power:**  
   $$W_{\text{total, raw}} = W_1 + W_2 = 180 + 120 = 300\text{ W}$$  
   $$P_{\text{true}} = 300\text{ W} \times 18000 = 5,400,000\text{ W} = \mathbf{5.4\text{ MW}}$$

---

# Experiment 11: Speed of a Rotating Body using Stroboscope

### 1. Core Theory & Everyday Intuition
![Strobotron Circuit](attachments/meas_exp11_strobotron_circuit.png)  
*Strobotron Flashing Oscillator Circuit*

![Stroboscope Shaft and Disc](attachments/meas_exp11_stroboscope_shaft.png)  
*Illuminating a Reference Mark on a Spinning Shaft*

![Stroboscope Multiple Patterns](attachments/meas_exp11_stroboscope_images.png)  
*Observed Patterns: Single Stationary Mark ($f = N$) vs Submultiples and Multiples*

#### What is a Stroboscope?
A stroboscope is an optical instrument that measures the rotational speed (RPM) of spinning machinery **without physical contact**.
- Traditional contact tachometers press a rubber tip against the shaft, which imposes mechanical friction and slows down fractional-horsepower motors or delicate mechanisms.
- A stroboscope uses a variable-frequency flashing gas discharge tube (**Strobotron** or **Xenon flash tube**) triggered by an electronic oscillator.

#### How It Works: Persistence of Vision
The human retina holds an image for approximately $\frac{1}{16}^{\text{th}}$ of a second (**persistence of vision**).
- A single distinct reference mark (such as a white chalk line or triangle) is drawn on the rotor disc.
- When the flashing frequency ($f$ in flashes/min or RPM) matches the shaft speed ($N$ in RPM):
  $$\mathbf{f = N}$$
- Every time the lamp flashes, the shaft has completed exactly one full revolution, illuminating the reference mark in the **exact same physical position**. To human eyes, the mark appears completely **frozen in place as a single stationary image**!

#### Resolving Ambiguity: Why Multiple Stationary Images Appear
A stroboscope has an inherent optical ambiguity that every student must understand:
1. **At Submultiples ($f = \frac{N}{2}, \frac{N}{3}, \dots$):**  
   The shaft makes 2 or 3 complete revolutions between flashes. The mark is still illuminated at the same angular position, so you still see a **single stationary image**, but the flashing frequency is lower than the true speed.
2. **At Harmonics ($f = 2N, 3N, \dots$):**  
   The lamp flashes twice per single shaft revolution (once at $0^\circ$ and once at $180^\circ$). Because of persistence of vision, you see **TWO stationary marks** located $180^\circ$ apart! At $f = 3N$, you see **three stationary marks** spaced $120^\circ$ apart.

#### The Master Formula: How to Find True Speed When $N$ is Unknown
If you don't know the shaft speed, start at the highest flashing rate and tune downward:
- Note the highest flashing frequency $f_m$ where a **single stationary mark** appears.
- Continue lowering the frequency and count how many frequencies $m$ produce a single stationary mark, down to the lowest observed frequency $f_1$.
- The true rotational speed $N$ is:
  $$\mathbf{N = \frac{f_m \cdot f_1 \cdot (m - 1)}{f_m - f_1}}$$
- For two consecutive flashing frequencies $f_1$ and $f_2$ ($m = 2$):
  $$\mathbf{N = \frac{f_2 \cdot f_1}{f_2 - f_1}}$$

---

### 2. Maths & Numerical Problems (Exp 11)

**Problem 11.1 (Lab Manual Numerical):**  
In a lab test to measure the speed of a ceiling fan, the stroboscope is tuned downward:
- Highest flashing frequency giving a single sharp stationary mark: $f_m = 2577\text{ rpm}$
- Lowest flashing frequency giving a single sharp stationary mark: $f_1 = 874.1\text{ rpm}$
- Total number of consecutive single-image frequencies observed: $m = 3$  
Calculate the true rotational speed $N$ of the fan.

**Step-by-Step Solution:**  
1. Apply the master multi-frequency formula:  
   $$N = \frac{f_m \cdot f_1 \cdot (m - 1)}{f_m - f_1}$$  
2. Substitute the values:  
   $$N = \frac{2577 \times 874.1 \times (3 - 1)}{2577 - 874.1} = \frac{2577 \times 874.1 \times 2}{1702.9}$$  
3. Numerator calculation:  
   $$2577 \times 874.1 \times 2 = 4,505,111.4$$  
4. Final Speed:  
   $$N = \frac{4,505,111.4}{1702.9} \approx \mathbf{2645.5\text{ RPM}}$$

**Problem 11.2 (Two Consecutive Flashes):**  
A spinning motor shaft shows a single frozen mark at $1800\text{ flashes/min}$ and again at the next lower setting of $1200\text{ flashes/min}$. No single mark appears in between. Find the true shaft speed.  
**Step-by-Step Solution:**  
Here $m = 2$, $f_2 = 1800$, $f_1 = 1200$:  
$$N = \frac{f_2 \cdot f_1}{f_2 - f_1} = \frac{1800 \times 1200}{1800 - 1200} = \frac{2,160,000}{600} = \mathbf{3600\text{ RPM}}$$

---

# Experiment 12: Insulation Resistance Measurement using Megger

### 1. Core Theory & Everyday Intuition
![Megger Cross Coil](attachments/meas_exp12_megger_cross_coil.png)  
*Megger Internal Cross-Coil (Ratiometer) Mechanism*

![Megger Cable Testing](attachments/meas_exp12_megger_cable_testing.png)  
*Cable Insulation Testing Setup Showing the Vital Guard (G) Connection*

#### What is a Megger?
A Megger (Mega-Ohmmeter) is a specialized portable instrument designed to measure **very high electrical resistance** (insulation resistance in Mega-ohms $M\Omega$ or Giga-ohms $G\Omega$).
- Normal battery ohmmeters operate at $1.5\text{ V}$ or $9\text{ V}$. An insulation fault (such as a microscopic crack in cable plastic) may look completely healthy at $9\text{ V}$, but flash over and leak current at $220\text{ V}$ or $11\text{ kV}$.
- A Megger contains a **built-in high-voltage DC generator** (hand-cranked or motorized battery-inverter), producing test voltages of **$500\text{ V}, 1000\text{ V},$ or $2500\text{ V}$** to test insulation under real electrical stress.

---

#### The Cross-Coil (Ratiometer) Principle: Why Crank Speed Doesn't Matter!
A Megger movement has two coils (Coil A and Coil B) rigidly mounted together on a common spindle inside a permanent magnet field:
1. **Control Coil (Pressure Coil - Coil A):** Connected in series with a fixed resistor $R_1$ straight across the generator. It exerts a torque driving the pointer toward **Infinity ($\infty$)**.
2. **Deflecting Coil (Current Coil - Coil B):** Connected in series with the unknown insulation under test ($R_x$). It exerts an opposing torque driving the pointer toward **Zero ($0$)**.

**The Mathematical Beauty of the Ratiometer:**  
The torque produced by Coil A is proportional to generator voltage $V$: $T_A \propto V$.  
The torque produced by Coil B is proportional to the leakage current through the insulation: $T_B \propto \frac{V}{R_x}$.  
When the pointer reaches equilibrium ($T_A = T_B$):
$$\theta \propto \frac{T_B}{T_A} \propto \frac{\left(\frac{V}{R_x}\right)}{V} = \mathbf{\frac{1}{R_x}}$$
- **Notice that $V$ completely cancels out!**
- This means whether you crank the handle at $140\text{ RPM}$ or $180\text{ RPM}$, the ratio remains constant, and **the needle reading is completely independent of generator voltage or hand-crank speed!**
- A centrifugal slipping clutch inside the crank handle prevents excessive over-speeding.

#### Why There are NO Control Hairsprings:
Meggers **do not have mechanical controlling hairsprings**. When the Megger is sitting in a tool bag with the handle stationary, the pointer can rest freely at any random position on the dial. It only springs to life when you crank the handle!

---

#### The Three Terminals & The Guard Wire ($G$)
A Megger has three terminals:
- **Line Terminal (L):** Connected to the central copper conductor of the cable.
- **Earth Terminal (E):** Connected to the external metallic armor or earth ground.
- **Guard Terminal (G):** Wrapped around the exposed outer surface of the insulation.

#### ⚠️ KEY EXAM QUESTION: What is the Purpose of the Guard Terminal?
When testing a high-voltage cable on a humid or dusty day, electricity leaks across the **surface** of the exposed insulation ends (surface leakage), in addition to leaking through the **volume** of the insulation (bulk volume leakage).
- If you don't use the Guard terminal, the surface leakage flows through the current coil (Coil B), causing the Megger to register a falsely low insulation reading (a healthy cable will fail the test!).
- The **Guard wire** collects this surface leakage current and routes it **directly back to the generator negative terminal, completely bypassing the deflecting coil (Coil B)**.
- As a result, the Megger measures **only pure internal volume insulation resistance**!

---

#### Routine Megger Health Check Before Testing:
1. **Open Circuit Test:** Keep test leads L and E separated in the air $\implies$ Crank handle $\implies$ Pointer must indicate **$\mathbf{\infty}$ (Infinity)**.
2. **Short Circuit Test:** Touch leads L and E firmly together $\implies$ Turn handle gently $\implies$ Pointer must swing cleanly to **$\mathbf{0}$ (Zero)**.

#### General Safety Rule for Minimum Insulation Resistance:
$$\mathbf{R_{\text{insulation}} \ge (\text{Rated kV} + 1)\text{ M}\Omega} \quad \text{with an absolute minimum of } \mathbf{1.0\text{ M}\Omega}$$

---

### 2. Maths & Numerical Problems (Exp 12)

**Problem 12.1 (Transformer Insulation Assessment):**  
A $33\text{ kV}$ three-phase distribution transformer is tested with a $2500\text{ V}$ Megger between the high-voltage winding and the transformer steel tank (earth).  
1. What is the minimum acceptable insulation resistance recommended by standard safety codes?  
2. If the Megger reads $2500\text{ M}\Omega$ (as in the lab manual data sheet), state with reason whether the transformer insulation is acceptable.

**Step-by-Step Solution:**  
1. Minimum acceptable insulation resistance:  
   $$R_{\text{min}} = (\text{Rated kV} + 1)\text{ M}\Omega = (33 + 1)\text{ M}\Omega = \mathbf{34\text{ M}\Omega}$$  
2. **Assessment:**  
   The measured insulation resistance is $2500\text{ M}\Omega = 2.5\text{ G}\Omega$.  
   Since $2500\text{ M}\Omega \gg 34\text{ M}\Omega$, the insulation is in **excellent, healthy condition** and the transformer is completely safe to energize.

**Problem 12.2 (Leakage Current Calculation):**  
A high-voltage power cable is tested at $1000\text{ V}$ DC using a Megger. The instrument records an insulation resistance of $500\text{ M}\Omega$. Calculate the steady-state bulk insulation leakage current flowing through the cable dielectric.

**Step-by-Step Solution:**  
$$I_{\text{leakage}} = \frac{V_{\text{test}}}{R_{\text{insulation}}} = \frac{1000\text{ V}}{500 \times 10^6\,\Omega} = \frac{1000}{5 \times 10^8} = 2 \times 10^{-6}\text{ A} = \mathbf{2.0\,\mu\text{A}}$$
