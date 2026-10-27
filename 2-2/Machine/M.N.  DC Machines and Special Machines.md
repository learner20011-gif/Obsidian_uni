## 📌 Common Symbols & Abbreviations

| Symbol / Abbr | Meaning | Symbol / Abbr | Meaning |
| :--- | :--- | :--- | :--- |
| **DC** | Direct Current | **$\Phi$** | Magnetic flux per pole ($\text{Wb}$) |
| **EMF / Back-EMF** | Electromotive Force / $E_b$ or $E_g$ | **$B$ / $B_{\max}$** | Flux density / Max flux density ($\text{T}$) |
| **MMF** | Magnetomotive Force ($AT$) | **$Z$** | Total armature conductors ($Z = 2C$) |
| **MNA / GNA** | Magnetic / Geometric Neutral Axis | **$P$ / $A$** | Number of poles / Parallel current paths |
| **OCC** | Open Circuit Characteristic | **$N$ / $\omega$** | Rotational speed ($\text{rpm}$) / ($\text{rad/s}$) |
| **$V_t$ / $V_L$** | Terminal voltage / Line voltage | **$T$ / $T_e$** | Shaft torque / Developed torque ($\text{N}\cdot\text{m}$) |
| **$I_a$ / $I_L$** | Armature current / Load current | **$k_a$ / $K$** | Machine design constant ($\frac{P Z}{2\pi A}$) |
| **$I_f$ / $I_{sh}$ / $I_{se}$** | Field / Shunt field / Series field current | **$Y_P$ / $Y_S$** | Pole pitch / Coil span in slots |
| **$R_a$ / $R_{sh}$ / $R_{se}$** | Armature / Shunt / Series resistance | **$Y_c$ / $Y_{\text{av}}$** | Commutator pitch / Average pitch |
| **$R_d$ / $R_c$** | Diverter resistance / Critical resistance | **$Y_b$ / $Y_f$ / $Y_R$** | Back / Front / Resultant pitch |
| **$N_c$** | Critical speed ($\text{rpm}$) | **$m$** | Plex of winding ($1 = \text{simplex}, 2 = \text{duplex}$) |
| **VR / SR** | Voltage Regulation / Speed Regulation | **NVC / OLR** | No-Volt Coil / Overload Release |
| **PMDC** | Permanent Magnet DC machine | **$P_m$ / $P_{\text{dev}}$** | Developed mechanical power ($\text{W}$) |

---

## 1. Fundamentals & Core Machine Physics

### Motor vs. Generator Action

![[Working_Principles_of_a_DC_Motor.webp]]

![[Pasted image 20261026110057.png]]

![[Pasted image 20261026121217.png]]

* **Motor:** Electrical energy $\to$ Mechanical energy.
  * **Principle:** Lorentz force on current-carrying conductor in $\vec{B}$-field:
    $$F = B I L \sin\theta$$
  * **Rule:** Fleming's **Left-Hand Rule** (Thumb = Force/Motion, Index = Field, Middle = Current).
  * **Voltage Balance:** $V > E_b \implies V = E_b + I_a R_a$.
  * **Torque:** Driving torque (rotates rotor against mechanical load).

* **Generator:** Mechanical energy $\to$ Electrical energy.
  * **Principle:** Faraday’s Law of Electromagnetic Induction ($e = -d\Phi/dt$) & Lenz's Law.
  * **Rule:** Fleming's **Right-Hand Rule** (_Generato**R** = **R**ight_).
  * **Voltage Balance:** $E_g > V \implies E_g = V + I_a R_a$.
  * **Torque:** Counter / Opposing torque (magnetic drag resisting prime mover).

* **Unit Conversion:**
  $$1\text{ line (Maxwell)} = 10^{-8}\text{ Wb}$$
  $$1\text{ kiloline} = 10^3 \times 10^{-8}\text{ Wb} = 10^{-5}\text{ Wb}$$

---

### Essential Construction Parts & Materials

![[Pasted image 20260715001457.png]]

1. **Yoke (Frame):**
   * Cast steel / cast iron outer frame.
   * Mechanical protection + low-reluctance magnetic flux return path.

2. **Poles & Field Coils:**
   * **Pole Core & Shoe:** Laminated sheet steel. Shoes spread flux across air gap & support coils.
   * **Field Winding:** Copper coils. Provides main working magnetic flux ($\Phi$).

3. **Armature Core:**
   * Cylindrical slotted drum of laminated silicon steel ($0.4\text{--}0.5\text{ mm}$).
   * Houses armature winding; offers low reluctance path.

4. **Armature Winding:**
   * Insulated copper coils placed in slots.
   * Active seat of EMF generation ($E$) and torque development ($T$).

5. **Commutator:**
   * Wedge-shaped hard-drawn copper segments insulated by mica.
   * **Generator:** Mechanical rectifier (AC $\to$ DC).
   * **Motor:** Mechanical inverter (DC $\to$ AC in conductors to maintain unidirectional torque).

![[Pasted image 20261027163027.png]]

6. **Brushes & Rigging:**
   * Carbon / graphite blocks with tension springs.
   * Collects current from rotating commutator to stationary external circuit.

---

### Core Physics & Construction Reasoning

* **Why Laminated Armature Core:**
  * Core continuously cuts alternating flux ($+B_{\max} \leftrightarrow -B_{\max}$).
  * High $d\Phi/dt$ induces large eddy currents.
  * Thin insulated laminations ($t$) restrict eddy current loops:
    $$P_e \propto t^2 \implies \text{Drastically reduces } I^2R \text{ core loss and heating.}$$

* **Why Solid Field Pole Core:**
  * Excited by steady DC current $\implies$ flux is constant and unidirectional ($d\Phi/dt = 0$).
  * Eddy currents are virtually absent $\implies$ solid cast steel is sufficient.
  * *(Only pole shoes are laminated to minimize slot-pulsation losses).*

* **Why Carbon Brushes (Over Metal Brushes):**
  1. **High Contact Resistance:** Cushions current reversal $\implies$ suppresses sparking during commutation.
  2. **Self-Lubricating:** Natural graphite lubricates contact $\implies$ protects commutator from abrasive wear.
  3. **Negative Temp. Coeff. of Resistance:** Resistance drops slightly as temperature rises $\implies$ prevents excessive voltage drops under load.
  4. **Sacrificial Wear:** Carbon wears out instead of copper segments $\implies$ cheap and easy to replace.

---

### Classification of DC Machines

![[compound_iqim6l.webp|700]]

1. **Separately Excited:** Field winding energized by an independent external DC source.
2. **Self-Excited (Armature powers its own field):**
   * **Shunt Wound:** Field in parallel with armature (high resistance, many turns of fine wire).
   * **Series Wound:** Field in series with armature (low resistance, few turns of thick wire).
   * **Compound Wound:** Contains both shunt and series field coils:
     * **Cumulative:** Series flux aids shunt flux ($\Phi = \Phi_{sh} + \Phi_{se}$).
     * **Differential:** Series flux opposes shunt flux ($\Phi = \Phi_{sh} - \Phi_{se}$).
     * **Long Shunt:** Shunt field across both armature and series field.
     * **Short Shunt:** Shunt field across armature only.
3. **Permanent Magnet (PMDC):** Flux created by permanent magnets (no field windings).

---

### Circuit Equations Comparison

```
1. Separately Excited:
   V_f = I_f * R_f
   Generator: V_t = E_a - I_a*R_a
   Motor:     V_t = E_a + I_a*R_a

2. Shunt Machine:
   I_sh = V_t / R_sh
   Generator: I_a = I_L + I_sh   |   V_t = E_g - I_a*R_a
   Motor:     I_a = I_L - I_sh   |   V_t = E_b + I_a*R_a

3. Series Machine:
   I_a = I_se = I_L
   Generator: V_t = E_g - I_a*(R_a + R_se)
   Motor:     V_t = E_b + I_a*(R_a + R_se)

4. Long-Shunt Compound:
   I_sh = V_t / R_sh
   Generator: I_a = I_L + I_sh   |   V_t = E_g - I_a*(R_a + R_se)
   Motor:     I_a = I_L - I_sh   |   V_t = E_b + I_a*(R_a + R_se)

5. Short-Shunt Compound:
   Generator: V_sh = V_t + I_L*R_se  |  I_sh = V_sh / R_sh  |  I_a = I_L + I_sh  |  V_t = E_g - I_a*R_a - I_L*R_se
   Motor:     V_sh = V_t - I_L*R_se  |  I_sh = V_sh / R_sh  |  I_a = I_L - I_sh  |  V_t = E_b + I_a*R_a + I_L*R_se
```

---

## 2. Machine Governing Equations & Derivations

### EMF Equation Derivation

* **Prerequisites:**
  * Flux per pole = $\Phi\text{ Wb}$
  * Number of poles = $P$
  * Total conductors = $Z$
  * Speed = $N\text{ rpm}$
  * Parallel paths = $A$ ($A = 2$ for wave, $A = P$ for lap)

* **Step 1: Flux cut by 1 conductor in 1 revolution:**
  $$d\Phi = P \cdot \Phi\quad (\text{Wb})$$

* **Step 2: Time taken for 1 revolution:**
  $$dt = \frac{60}{N}\quad (\text{seconds})$$

* **Step 3: Average EMF induced per conductor (Faraday's Law):**
  $$e_{\text{avg}} = \frac{d\Phi}{dt} = \frac{P \Phi}{60 / N} = \frac{P \Phi N}{60}\quad (\text{V})$$

* **Step 4: Total EMF ($E$):**
  * Conductors connected in series per parallel path $= \frac{Z}{A}$.
  $$E = e_{\text{avg}} \times \left(\frac{Z}{A}\right) = \mathbf{\frac{P \Phi Z N}{60 A}}\quad (\text{Volts})$$

* **Angular Velocity Formulation ($\omega$):**
  $$\omega = \frac{2\pi N}{60} \implies N = \frac{60\omega}{2\pi}$$
  $$E = \frac{P \Phi Z}{60 A}\left(\frac{60\omega}{2\pi}\right) = \left(\frac{P Z}{2\pi A}\right)\Phi\omega = \mathbf{k_a \Phi \omega} \quad \left(k_a = \frac{P Z}{2\pi A}\right)$$

* **Frequency / RPS Formulation ($S = N/60$):**
  $$E = \left(\frac{P Z}{A}\right) \Phi S = \mathbf{k \Phi S} \quad \left(k = \frac{P Z}{A}\right)$$

---

### Electromagnetic Torque Equation Derivation

* **Prerequisites:**
  * Armature radius = $r$, active conductor length = $L$.
  * Total armature current = $I_a \implies$ Current per conductor $= I_a / A$.

* **Step 1: Force on a single conductor (Biot-Savart / Lorentz):**
  $$f_c = B \cdot I_{\text{cond}} \cdot L = B \left(\frac{I_a}{A}\right) L$$

* **Step 2: Average flux density ($B$):**
  $$B = \frac{\text{Total Flux}}{\text{Cylindrical Area}} = \frac{P \Phi}{2\pi r L}$$

* **Step 3: Torque on 1 conductor:**
  $$T_c = f_c \times r = \left(\frac{P \Phi}{2\pi r L}\right)\left(\frac{I_a}{A}\right) L \times r = \frac{P \Phi I_a}{2\pi A}$$

* **Step 4: Total torque for all $Z$ conductors:**
  $$T_e = Z \cdot T_c = \mathbf{\frac{P Z \Phi I_a}{2\pi A}} = \mathbf{k_a \Phi I_a}\quad (\text{N}\cdot\text{m}) \quad \left(k_a = \frac{P Z}{2\pi A}\right)$$

* **Power-Torque Equivalence Check:**
  $$P_{\text{mech}} = T_e \cdot \omega = (k_a \Phi I_a)\cdot \omega = (k_a \Phi \omega)\cdot I_a = \mathbf{E_b I_a}$$

---

### Back-EMF ($E_b$) Physics & Governors

* **Definition:** Induced counter-voltage in rotating armature opposing terminal voltage $V$ (by Lenz’s law):
  $$E_b = \frac{P \Phi Z N}{60 A} < V$$

* **Current Limiting Function:**
  $$I_a = \frac{V - E_b}{R_a}$$
  * At standstill ($N = 0 \implies E_b = 0$): $I_{\text{start}} = \frac{V}{R_a}$ (destructive inrush $\sim 15\text{--}30 \times I_{\text{FL}}$).
  * Running: $E_b \approx V \implies I_a$ stays safe.

* **Automatic Self-Governing Mechanism:**
  * Load $\uparrow \implies N \downarrow \implies E_b \downarrow \implies (V - E_b) \uparrow \implies I_a \uparrow \implies T_e \uparrow$ (matches load).
  * Load $\downarrow \implies N \uparrow \implies E_b \uparrow \implies (V - E_b) \downarrow \implies I_a \downarrow \implies T_e \downarrow$.

* **Condition if $E_b = V$:**
  $$I_a = \frac{V - V}{R_a} = 0 \implies T_e = 0$$
  * Rotor cannot overcome bearing friction/windage $\implies$ motor decelerates immediately.

---

### Proof: Condition for Maximum Mechanical Power

* **Voltage Equation:**
  $$V = E_b + I_a R_a$$

* **Multiply by $I_a$ (Power balance):**
  $$V I_a = E_b I_a + I_a^2 R_a \implies P_m = V I_a - I_a^2 R_a$$

* **Differentiate w.r.t. $I_a$ & set to 0:**
  $$\frac{dP_m}{dI_a} = V - 2 I_a R_a = 0 \implies I_a R_a = \frac{V}{2}$$

* **Substitute back into voltage equation:**
  $$V = E_b + \frac{V}{2} \implies \mathbf{E_b = \frac{V}{2}}$$

* **Practical Note:** Efficiency at this point is $< 50\%$ with massive $I^2R$ heating; motors are **never** operated at this theoretical limit.

---

## 3. DC Armature Windings & Calculations

### Lap vs. Wave Winding Comparison

![[Introductions-to-DC-Machines20.jpg]]

![[Armature-Windings-of-DC-Generator-Lap-Wave-pptx-5-2048.webp]]

![[simplex-duplex.webp]]

| Parameter | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Coil Progression** | Loops back onto adjacent segment | Advances continuously forward like a wave |
| **Parallel Paths ($A$)** | **$A = m \cdot P$** ($A = P$ for simplex) | **$A = 2 \cdot m$** ($A = 2$ for simplex) |
| **Commutator Pitch ($Y_c$)** | $Y_c = \pm m$ ($\pm 1$ for simplex) | $Y_c = \frac{2(C \pm m)}{P}$ |
| **Voltage & Current Rating** | **High current, Low voltage** | **Low current, High voltage** |
| **Number of Brushes** | Must equal poles ($P$) | Only 2 required (can use $P$ to reduce brush length) |
| **Equalizer Connections** | **Mandatory** (bypasses circulating currents) | **Not needed** (paths symmetrically distributed) |
| **EMF Generated ($E \propto 1/A$)**| Lower ($E \propto 1/P$) | Higher ($E \propto 1/2$) |

---

### Winding Pitch Geometry & Formulas

![[Pasted image 20261027122917.jpg|314]]

![[Copied_Item_1793051782353.png|607]]

![[Pasted image 20261027124521.png]]

* **Pole Pitch ($Y_P$):**
  $$Y_P = \frac{S}{P}\quad (\text{slots/pole}) = \frac{Z}{P}\quad (\text{conductors/pole})$$

* **Coil Span / Slot Pitch ($Y_S$):**
  $$Y_S = \lfloor Y_P \rfloor \quad (\text{nearest integer } \le Y_P)$$

* **Back Pitch ($Y_b$) & Front Pitch ($Y_f$):**
  * Must both be **odd integers** (connects top odd conductor to bottom even conductor).
  * $Y_b \approx \frac{Z}{P} = 2 Y_S + 1$.

* **Resultant Pitch ($Y_R$):**
  * **Lap Winding:** $Y_R = Y_b - Y_f = \pm 2m$
  * **Wave Winding:** $Y_R = Y_b + Y_f = 2 Y_c$

* **Average Pitch ($Y_{\text{av}}$):**
  $$Y_{\text{av}} = \frac{Y_b + Y_f}{2} = Y_c = \frac{C \pm m}{P/2}$$

* **Pitch / Chording Factor ($k_p$):**
  $$k_p = \cos\left(\frac{\alpha}{2}\right) \quad (\alpha = \text{chording angle})$$

![[Pasted image 20261027123925.png]]

![[Pasted image 20261027124147.png|611]]

![[Pasted image 20261027130713.png|622]]

---

### Equalizer Rings & Frog-Leg Winding

* **Equalizer Rings:**
  * Low-resistance copper jumpers connecting points intended to be at equipotential in Lap windings.
  * **Why Needed in Lap ($A = P$):** Slight air gap eccentricity or bearing wear causes unequal path flux $\implies$ unequal induced EMFs $\implies$ large circulating currents flow through brushes $\implies$ severe sparking and overheating. Equalizers bypass brushes.
  * **Why NOT in Wave ($A = 2$):** Both paths pass through coils distributed under all poles equally $\implies$ magnetic imbalances cancel naturally.

* **Frog-Leg Winding:**
  * Composite winding: combines **simplex lap** and **multiplex wave** in the identical slots.
  * Wave winding acts as an internal, distributed equalizer network for lap winding.
  * Eliminates external equalizer rings entirely.
  * **Parallel Paths Formula:**
    $$\mathbf{a = 2 P m_{\text{lap}}}$$

---

### Winding Calculations Walkthrough

#### 1. Pitch Calculation (Duplex Wave, 139 Slots, 6 Poles)
* Given: $S = 139 \implies C = 139$; $P = 6$; Duplex $\implies m = 2$.
* Commutator Pitch ($Y_c$):
  $$Y_c = \frac{C \pm m}{P/2} = \frac{139 \pm 2}{3}$$
  * Progressive ($+$): $Y_c = \frac{141}{3} = \mathbf{47}$ (Valid integer).
  * Retrogressive ($-$): $Y_c = \frac{137}{3} = 45.67$ (Invalid).
* Pitches: $Y_{\text{av}} = Y_c = 47 \implies Y_b + Y_f = 2 \times 47 = 94$.
  $$\mathbf{Y_b = 47, \quad Y_f = 47}\quad (\text{both odd integers})$$

#### 2. Rewinding Lap to Wave Voltage Scaling
* Formula: $E \propto \frac{N}{A} \implies \frac{E_2}{E_1} = \left(\frac{N_2}{N_1}\right)\left(\frac{A_1}{A_2}\right)$
* Lap: $P = 4 \implies A_1 = 4$; $N_1 = 600\text{ rpm}$; $E_1 = 216\text{ V}$.
* Wave: $A_2 = 2$; $N_2 = 500\text{ rpm}$.
  $$E_2 = 216 \times \left(\frac{500}{600}\right) \times \left(\frac{4}{2}\right) = 216 \times \frac{5}{6} \times 2 = \mathbf{360\text{ V}}$$

---

## 4. Armature Reaction & Mitigation

### Armature Reaction Physics & Effects

![[Pasted image 20261027135344.png]]

![[Pasted image 20261027134722.jpg|540]]

![[Pasted image 20261027134931.jpg]]

![[Pasted image 20260715003637.png]]

* **Definition:** Distortion and weakening of main field flux ($\Phi$) caused by armature magnetic field.

* **Core Mechanisms & Effects:**
  1. **Cross-Magnetizing Distortion:**
     * Distorts field across pole faces.
     * Shifts **Magnetic Neutral Axis (MNA)**:
       * **Generator:** MNA shifts **forward** (in direction of rotation).
       * **Motor:** MNA shifts **backward** (opposite to direction of rotation).
     * Moving away from GNA causes coils undergoing commutation to cut flux $\implies$ brush sparking.
  2. **Demagnetizing Effect (Net Flux Drop):**
     * **Generator:** Armature flux aids main flux at trailing tip (saturates); opposes flux at leading tip (weakens).
     * Saturation prevents trailing tip from gaining as much flux as leading tip loses:
       $$\text{Flux lost at leading tip} > \text{Flux gained at trailing tip} \implies \mathbf{\Phi_{\text{net}} \downarrow \implies E_g \downarrow}$$
     * **Motor:** Leading tip saturates; trailing tip weakens.
  3. **Commutator Flashover:** Voltage peaks between adjacent segments spark over, creating catastrophic arc flash across brush arms.

---

### Neutralizing Armature Reaction

![[Pasted image 20261027140456.png|651]]

![[Pasted image 20261027141328.png]]

1. **Compensating Windings:**
   * Embedded in slots in the **main pole shoes**, connected in **series with the armature**.
   * Carries current in the **opposite direction** to conductors directly underneath.
   * Cancels armature MMF beneath pole face at all load levels ($AT_{\text{comp}} \approx AT_{\text{armature, pole-arc}}$).

2. **Interpoles (Commutating Poles):**
   * Narrow auxiliary poles placed in the interpolar axis between main poles.
   * Connected in **series with the armature**.
   * Cancels cross-magnetizing flux in the neutral commutation zone, fixing MNA to GNA.

3. **Chamfered Pole Shoes:**
   * Increasing air gap at pole tips increases magnetic reluctance $\implies$ prevents flux crowding.

4. **Brush Shift:**
   * Shift brushes to match new MNA (only works for one fixed load; introduces direct demagnetizing MMF band $2\theta_m$).

---

## 5. Commutation & Reactance Voltage ($L di/dt$)

### Commutation Mechanism & The $L di/dt$ Problem

![[Pasted image 20261027141908.jpg|679]]

![[Pasted image 20261027143726.png]]

* **Definition:** Reversal of current in an armature coil from $+I_c \to -I_c$ during the brief time interval ($T_c$) it is short-circuited by a brush.
* **The $L di/dt$ Reactance Voltage Problem:**
  * Armature coils possess self-inductance ($L$).
  * Rapid current reversal produces high rate of change ($di/dt = 2I_c / T_c$).
  * Self-induced **reactance voltage**:
    $$e_r = L \frac{di}{dt}$$
  * Lenz's law delays current decay $\implies$ **delayed (under) commutation**.
  * Coil current fails to reach $-I_c$ before brush breaks contact $\implies$ remaining current forced to arc across air gap to brush edge $\implies$ pitting & brush burn-out.

---

### Methods of Improving Commutation

![[Pasted image 20261027141022.png|552]]

1. **Resistance Commutation (Carbon Brushes):**
   * Contact area with leaving segment shrinks $\implies$ contact resistance surges.
   * High resistance forces current to reverse smoothly across the next segment instead of jumping as an arc.

2. **Voltage Commutation (Interpoles):**
   * Interpoles induce a dynamic rotational voltage ($e_c = B_{\text{int}} l v$) that directly opposes $e_r$.
   * Since both $e_c \propto I_a$ and $e_r \propto I_a$, automatic sparkless commutation is achieved from no-load to full-load.
   * **Interpole Polarity Rules:**
     * **Generator:** Same polarity as the main pole **ahead** in direction of rotation.
     * **Motor:** Same polarity as the main pole **behind** in direction of rotation.

---

## 6. Voltage Build-Up in Self-Excited Generators

### Physics of Voltage Build-Up

![[Pasted image 20260715035244.png|646]]

![[Pasted image 20261027153722.png|552]]

![[Pasted image 20261027154818.png|571]]

* **Residual Magnetism ($\Phi_{\text{res}}$):**
  * Hysteresis leaves remnant flux $\implies$ induces seed voltage $E_{\text{res}} \approx 2\text{--}12\text{ V}$ at $I_f = 0$.

* **Step-by-Step Cumulative Build-Up:**
  1. Residual flux induces seed EMF $E_0$.
  2. $E_0$ drives small field current $I_{f1} = E_0 / R_f$.
  3. Proper connection produces aiding flux ($\Phi = \Phi_{\text{res}} + \Delta \Phi$).
  4. Higher flux induces higher voltage $E_1$.
  5. Cumulative growth continues climbing the OCC curve.
  6. **Equilibrium:** Process stabilizes at intersection of OCC curve and field resistance line ($V = I_f R_f$). Iron core saturation prevents runaway voltage.

* **4 Mandatory Conditions for Build-Up:**
  1. $\Phi_{\text{res}} > 0$ (Residual magnetism present).
  2. Field MMF aids residual flux (proper polarity).
  3. **$R_f < R_c$** (Field circuit resistance < Critical resistance).
  4. **$N > N_c$** (Speed > Critical speed).

---

### Critical Resistance ($R_c$) & Critical Speed ($N_c$)

* **Critical Resistance ($R_c$):**
  * Maximum field resistance at which the generator will build up voltage.
  * Graphically: **Slope of the tangent (air-gap line)** to the initial linear portion of the OCC:
    $$R_c = \frac{\Delta E_a}{\Delta I_f}\quad (\Omega)$$
  * If $R_f > R_c$: Machine fails to build up (outputs only $E_{\text{res}}$).
  * Direct speed proportionality:
    $$\mathbf{R_c \propto N}$$

* **Critical Speed ($N_c$):**
  * Speed for which given field resistance $R_f$ becomes critical:
    $$\frac{N_c}{N_{\text{rated}}} = \frac{R_f}{R_c} \implies \mathbf{N_c = N_{\text{rated}} \times \left(\frac{R_f}{R_c}\right)}$$

* **Why Shunt Generator Fails to Build Up & Quick Remedies:**

| Failure Cause | Root Reason | Quick Remedy |
| :--- | :--- | :--- |
| **No Residual Flux** | Shock, heat, prolonged idle | **Field Flashing:** Flash field with external DC battery |
| **Reversed Field Lead** | Field MMF destroys residual flux | Swap field leads ($F_1, F_2$) |
| **Reversed Rotation** | Inverted induced EMF polarity | Reverse rotation or swap field leads |
| **$R_f > R_c$** | Field rheostat too high | Reduce field rheostat resistance |
| **$N < N_c$** | Prime mover running slow | Increase speed to rated rpm |
| **Loaded at Startup** | Load pulls terminal voltage down | Start on **open-circuit (no-load)** |

---

## 7. DC Generator Characteristics & Voltage Regulation

### External Characteristics Comparison ($V_t$ vs. $I_L$)

![[Pasted image 20260715010455.png|700]]

![[Pasted image 20260715021010.png]]

![[Pasted image 20260715015707.png|627]]

![[Pasted image 20260715021142.png]]

![[Pasted image 20260715021424.png|628]]

![[Pasted image 20260715024155.png]]

![[Pasted image 20260715024337.png|619]]

![[Pasted image 20260715024213.png|251]]

![[Pasted image 20260715024741.png|395]]

![[Pasted image 20260715025633.png]]

![[Pasted image 20260715025654.png]]

![[Pasted image 20260715025820.png]]

| Generator Type | External Curve Behavior | Physical Reason |
| :--- | :--- | :--- |
| **Over-Compound** | Voltage rises with load ($V_{\text{FL}} > V_{\text{NL}}$) | Series MMF overcompensates $I_a R_a$ drop & armature reaction |
| **Flat-Compound** | Voltage constant ($V_{\text{FL}} = V_{\text{NL}}$) | Series MMF exactly balances internal drops |
| **Under-Compound** | Voltage drops slightly ($V_{\text{FL}} < V_{\text{NL}}$) | Series MMF partially balances internal drops |
| **Separately Excited**| Moderate droop | Drops only by $I_a R_a$ & armature reaction ($I_f$ is constant) |
| **Shunt Generator** | Significant droop; breakdown knee | $V_t$ drop reduces $I_{sh} = V_t/R_{sh}$, causing compounding collapse |
| **Differential Compound**| Plummets steeply to zero | Series flux opposes shunt flux ($\Phi = \Phi_{sh} - \Phi_{se}$) |
| **Series Generator**| Starts near 0, rises steeply, droops past knee | Field in series ($I_{se} = I_L$); saturates at high load |

* **Why $V_t$ drops even above the knee of OCC:**
  1. Ohmic drop $I_a R_a$.
  2. Localized saturation at trailing pole tips reduces net flux per pole ($\Phi$).
  3. Lower $V_t$ weakens shunt excitation ($I_{sh} \downarrow$).

---

### Voltage Regulation & Compounding Control

* **Voltage Regulation Formula:**
  $$\mathbf{\%\,\text{VR} = \frac{V_{\text{NL}} - V_{\text{FL}}}{V_{\text{FL}}} \times 100\%}$$

* **Desirability of Small %VR:**
  * General power/lighting: Minimum VR ($\approx 0\%$, Flat compound) ideal $\implies$ constant consumer voltage without rheostat adjustments.
  * **Negative %VR ($V_{\text{FL}} > V_{\text{NL}}$):** Over-compounded generators $\implies$ cancels line resistance drop ($I R_{\text{line}}$) over long transmission feeders.
  * **High Positive %VR (Steep Collapse):** Differential compound $\implies$ arc welding (limits short-circuit current during electrode contact).

* **Series Field Diverter Resistor ($R_d$):**
  * Variable resistor in parallel with series field winding to tune compounding level.
  * **Calculation Steps:**
    1. Additional MMF required: $\Delta AT = \Delta I_{sh} \times N_{sh}$.
    2. Required series current: $I_{se} = \frac{\Delta AT}{N_{se}}$.
    3. Diverter current: $I_d = I_a - I_{se}$.
    4. Diverter resistance:
       $$I_d R_d = I_{se} R_{se} \implies \mathbf{R_d = \frac{I_{se} R_{se}}{I_d}}$$

---

### Applications Summary of DC Generators

* **Shunt:** Battery charging, ordinary DC lighting, exciter for synchronous alternators.
* **Series:** Line voltage boosters in DC transmission, constant-current arc lamps.
* **Cumulative Compound:** Long-distance distribution feeders (Over), industrial loads / commercial plants (Flat).
* **Differential Compound:** Electric arc welding (inherent current limiter).
* **Separately Excited:** Testing laboratories, Ward-Leonard wide-range speed drives.

---

## 8. Parallel Operation of DC Generators

### Shunt Generators (Inherently Stable)

![[Parallel-Operation-of-DC-Shunt-Generator.webp]]

![[Pasted image 20261027185116.png]]

* **Incoming Generator Setting:**
  * Voltage set **$1\text{--}2\text{ V}$ higher** than busbar voltage before closing breaker.
  * Prevents machine from drawing reverse current and **motoring** against prime mover.
  * Guarantees smooth positive load pick-up.

* **Load Sharing Stability Mechanism:**
  * Shunt generators have **drooping** characteristics ($V_t \downarrow$ as $I_a \uparrow$).
  * If Gen 1 grabs extra load:
    $$I_{a1} \uparrow \implies V_{t1} \downarrow \implies I_{a1} = \frac{E_{a1} - V_{\text{bus}}}{R_a} \downarrow$$
  * Automatically sheds excess load back to Gen 2 $\implies$ **inherently stable negative feedback**.

---

### Compound Generators (Inherently Unstable) & Equalizer Bar

![[Pasted image 20261027195423.png]]

* **Why Unstable:**
  * Over-compound generators have **rising** characteristics.
  * If Gen 1 grabs extra load:
    $$I_{a1} \uparrow \implies I_{se1} \uparrow \implies \Phi_{se1} \uparrow \implies E_{a1} \uparrow \implies \text{Grabs more current (Runaway!)}$$
  * Gen 1 trips on overcurrent; Gen 2 reverses current, motoring as differential compound motor with risk of destruction.

* **Equalizer Bar Stabilization:**
  * Heavy low-resistance copper bar connecting armature-series field junctions.
  * Places both series fields in **parallel**.
  * Any current fluctuation divides between series fields in inverse ratio of their resistances, independent of which armature supplies it.
  * Keeps field strengths locked together $\implies$ guarantees stable parallel operation.

---

## 9. DC Motor Operating Characteristics & Dynamics

### Motor Speed Formula & Control Variables

![[Pasted image 20260921070011.png]]

* **Governing Speed Equation:**
  $$\mathbf{N = \frac{V - I_a R_a}{k_a \Phi} \propto \frac{E_b}{\Phi}\quad (\text{rpm})} \quad \Longleftrightarrow \quad \mathbf{\omega = \frac{V - I_a R_a}{k_a \Phi}\quad (\text{rad/s})}$$

* **3 Speed Control Variables:**
  1. **Field Flux ($\Phi$):** $N \propto \frac{1}{\Phi}$ (Rheostat in field circuit).
  2. **Armature Resistance ($R_a$):** $N \propto (V - I_a R_{\text{total}})$ (External series resistor).
  3. **Terminal Voltage ($V$):** $N \propto V$ (Adjustable supply).

---

### Terminal Characteristics Derivations

#### 1. DC Shunt Motor ($\omega$ vs. $\tau_{\text{ind}}$)
* Armature KVL: $V_T = E_b + I_a R_a$.
* Substitute $E_b = k_a \Phi \omega$ and $I_a = \frac{\tau_{\text{ind}}}{k_a \Phi}$:
  $$V_T = k_a \Phi \omega + \left(\frac{\tau_{\text{ind}}}{k_a \Phi}\right) R_a$$
  $$\mathbf{\omega = \frac{V_T}{k_a \Phi} - \frac{R_a}{(k_a \Phi)^2} \tau_{\text{ind}}}$$
* **Curve:** Linear, slightly drooping straight line (3–5% drop from no-load to full-load $\implies$ practically constant speed).

#### 2. DC Series Motor ($\omega$ vs. $\tau_{\text{ind}}$)
* Armature KVL: $V_T = E_b + I_a (R_a + R_{se})$.
* Flux proportional to current before saturation: $\Phi = c I_a$.
* Torque: $\tau_{\text{ind}} = k_a \Phi I_a = k_a c I_a^2 \implies I_a = \sqrt{\frac{\tau_{\text{ind}}}{k_a c}}$.
* Substitute $E_b = k_a c I_a \omega$:
  $$V_T = k_a c I_a \omega + I_a (R_a + R_{se}) = \sqrt{k_a c\, \tau_{\text{ind}}}\,\omega + \frac{R_a + R_{se}}{\sqrt{k_a c}}\sqrt{\tau_{\text{ind}}}$$
  $$\mathbf{\omega = \frac{V_T}{\sqrt{k_a c}}\frac{1}{\sqrt{\tau_{\text{ind}}}} - \frac{R_a + R_{se}}{k_a c}}$$
* **Curve:** Rectangular hyperbola ($\omega \propto 1/\sqrt{\tau_{\text{ind}}}$). High torque at low speed; speed approaches $\infty$ at light load.

---

### Motor Operating Characteristics Comparison

![[Pasted image 20260729015156.png]]

![[Pasted image 20261026134333.png|700]]

![[Pasted image 20260729013256.png]]

![[Pasted image 20261027164333.png|635]]

![[Pasted image 20260729030609.png]]

![[Pasted image 20261027164403.png|636]]

![[Pasted image 20261027164643.png]]

![[Pasted image 20261026134258.png]]

| Motor Type | Torque vs. Current ($T\text{-}I_a$) | Speed vs. Current ($N\text{-}I_a$) | Speed vs. Torque ($N\text{-}T$) | Primary Applications |
| :--- | :--- | :--- | :--- | :--- |
| **Shunt** | Straight line ($T \propto I_a$) | Nearly constant (droops 3–5%) | Flat droop | Machine tools, lathes, fans, centrifugal pumps |
| **Series** | Parabolic ($T \propto I_a^2$), linear post-sat | Steep hyperbola ($N \propto 1/I_a$) | Hyperbolic | Traction, trains, hoists, cranes, car starters |
| **Cumulative Compound** | Steeper than shunt | Droops noticeably | Intermediate droop | Punch presses, rolling mills, shears, elevators |
| **Differential Compound** | Flattens / drops | Rises with load (**negative SR**) | Unstable / hunting | Rarely used (experimental only) |

* **Why Series Motor MUST be Geared/Coupled to Load:**
  * At no load ($I_a \approx 0 \implies \Phi \to \Phi_{\text{res}} \approx 0$).
  * $N \propto 1/\Phi \to \infty$ (**Runaway speed**).
  * Centrifugal forces shatter commutator, burst windings, bend shaft.
  * **Rule:** Must never be belt-driven (belt may slip/snap).

* **Danger of Opening Shunt Field While Running:**
  * $\Phi \to \Phi_{\text{res}} \implies N \to \infty$ on light load (mechanical explosion).
  * On full load: Motor stalls $\implies E_b = 0 \implies I_a = V/R_a$ (massive short-circuit burns armature).

---

## 10. Speed Control Methods & Electric Braking

### Speed Control Zones & Methods

![[Pasted image 20260921072920.jpg]]

![[Pasted image 20260921073646.jpg]]

![[Pasted image 20261026154346.png]]

* **Base Speed:** Rated operating speed at rated voltage, rated field current, and rated full load.

* **Below Base Speed (Armature Voltage Control):**
  * Keep field flux maximum ($\Phi = \Phi_{\text{rated}}$).
  * Vary armature terminal voltage ($0 \to V_{\text{rated}}$).
  * **Constant Torque Mode:** $T_{\max} = k_a \Phi_{\text{rated}} I_{a,\text{rated}} = \text{Constant}$.
  * *Why not field control below base speed:* Core is already saturated; increasing $I_f$ overheats field with zero flux gain.

* **Above Base Speed (Field Flux Weakening):**
  * Keep armature voltage at rated ($V = V_{\text{rated}}$).
  * Increase resistance in shunt field rheostat $\implies I_f \downarrow \implies \Phi \downarrow \implies N \uparrow$.
  * **Constant Power Mode:** $P_{\max} = E_b I_a \approx V I_a = \text{Constant}$ (Torque drops as speed rises).
  * *Why not armature voltage above base speed:* Higher voltage destroys insulation and causes commutator flashover.

* **Armature Resistance Control (Inefficient):**
  * Insert series rheostat in armature $\implies$ drops $V' = V - I_a R_{\text{ext}} \implies N \downarrow$.
  * Large $I_a^2 R_{\text{ext}}$ power loss, poor speed regulation.

---

### Ward-Leonard System & Solid-State Thyristor Control

![[Pasted image 20261027165607.png|621]]

* **Ward-Leonard Drive:**
  * AC motor drives variable-voltage DC generator; generator feeds main DC motor armature.
  * Generator & motor fields excited from independent constant-voltage exciter.
  * **Below base speed:** Generator field rheostat adjusts armature voltage smoothly from $0 \to V$.
  * **Above base speed:** Main motor field rheostat weakens flux.
  * **Reversal:** Swap generator field polarity $\implies$ smooth 4-quadrant speed reversal without heavy power switches.

* **Solid-State Thyristor Control:**
  * Phase-controlled SCR bridge converts AC to variable DC:
    $$V_{\text{dc}} = \frac{2 V_m}{\pi}\cos\alpha \quad (\alpha = \text{firing angle})$$
  * Adjusting $\alpha$ ($0^\circ \to 90^\circ$) smoothly controls armature voltage below base speed with high efficiency.

---

### Electric Braking Methods

![[Pasted image 20261026183323.png]]

| Feature | Electric Braking | Mechanical Braking |
| :--- | :--- | :--- |
| **Mechanism** | Motor acts as generator; converts kinetic energy to electrical | Friction shoes press on rotating drum |
| **Wear & Tear** | Zero mechanical wear | High lining wear; frequent replacement |
| **Heat Location** | External resistor or fed back to grid | Directly on brake drum (fire hazard) |
| **Holding Rest** | **Cannot hold load at zero speed** ($T_{\text{brake}} \to 0$) | **Holds stationary load securely** (parking) |

1. **Regenerative Braking ($E_b > V$):**
   * Overhauling load drives motor above no-load speed $\implies E_b > V$.
   * $I_a = \frac{E_b - V}{R_a}$ reverses direction $\implies$ feeds power back to grid.

2. **Dynamic (Rheostatic) Braking:**
   * Disconnect armature from supply; close across braking resistor $R_B$ (field remains energized).
   * Driving voltage $= E_b$. Kinetic energy dissipated as heat in $R_B$.
   * Braking current: $I_{\text{brake}} = \frac{E_b}{R_a + R_B}$.

3. **Plugging (Reverse Current Braking):**
   * Armature terminal polarity suddenly reversed while running.
   * Net driving voltage:
     $$\mathbf{V_{\text{net}} = V + E_b \approx 2V}$$
   * Requires series resistor: $R_{\text{ext}} = \frac{V + E_b}{I_{\text{brake, max}}} - R_a$.
   * **Proof: Plugging produces double torque of dynamic braking:**
     $$V_{\text{plug}} \approx 2 E_b \approx 2 \times V_{\text{dyn}} \implies I_{\text{plug}} \approx 2 I_{\text{dyn}} \implies \mathbf{T_{\text{plug}} \approx 2 T_{\text{dyn}}}$$

---

## 11. Starting of DC Motors & Starters

### Why a Starter is Mandatory

* Standstill: $N = 0 \implies E_b = 0$.
* Starting current:
  $$I_{a,\text{start}} = \frac{V - 0}{R_a} = \frac{V}{R_a}$$
* Since $R_a \ll 1\,\Omega$, starting current is **$15\text{--}30 \times$ rated full-load current**.
* **Destructive Consequences:**
  1. Burnout of armature winding insulation within seconds.
  2. Severe commutator segment pitting and brush flashover.
  3. Excessive torque shock shears mechanical shafts and couplings.
  4. Large supply voltage dip trips upstream circuit protection.
* **Function of Starter:** Inserts external resistance at start; cuts out steps as $E_b$ builds up.

---

### Starter Types & Schematics

![[Pasted image 20260729092319.png]]

![[Pasted image 20260729092231.png|480]]

![[Pasted image 20260729083801.jpg]]

![[Pasted image 20260729084236.png]]

![[Three-Point-Starter.-3-Point-Starter.webp]]

![[Pasted image 20260921071012.jpg]]

![[Pasted image 20261026195752.png]]

![Circuit Diagram for 3-Point Starter|595](attachments/fig5_1_circuit_3point_starter.png)

![[Pasted image 20260729085814.jpg]]

![[Pasted image 20260921081553.jpg]]

![[Pasted image 20261026193118.png]]

* **2-Point Starter:** Used exclusively for DC series motors.
* **3-Point Starter:**
  * Terminals: Line ($L$), Armature ($A$), Field ($F$).
  * Shunt field connects to brass arc directly across supply $\implies$ guarantees **100% full field flux** at startup.
  * Maximum starting torque with low speed.
  * **Drawback:** **No-Volt Coil (NVC)** is in series with shunt field. Field weakening speed control drops $I_f \implies$ NVC releases handle to OFF!
* **4-Point Starter:**
  * Solves 3-point drawback: NVC placed in an **independent 4th branch ($N$)** with a protective series resistor across the line.
  * NVC current is constant regardless of field rheostat adjustments.
  * Limitation: Does not trip if field circuit accidentally opens internally.

---

## 12. Losses, Power Flow & Maximum Efficiency

### Classification of Losses

![[Copied_Item_1793051120342.png]]

1. **Copper Losses ($I^2R$):**
   * Armature loss: $I_a^2 R_a$ (variable with load, 30–40% total loss).
   * Shunt field loss: $I_{sh}^2 R_{sh}$ (constant).
   * Series field loss: $I_{se}^2 R_{se}$ (variable).
   * Brush contact loss: $V_{\text{brush}} \times I_a \approx 2\text{ V} \times I_a$.

2. **Core / Iron Losses (Constant at rated speed/flux):**
   * **Hysteresis Loss (Steinmetz):** $W_h = \eta B_{\max}^{1.6} f V_{\text{core}}$.
   * **Eddy Current Loss:** $W_e = k_e B_{\max}^2 f^2 t^2 V_{\text{core}}$.

3. **Mechanical Losses (Constant):**
   * Bearing friction, brush friction, windage.

4. **Stray Load Losses:** Flux distortion losses under load ($\sim 1\%$ output).

---

### Proof: Condition for Maximum Efficiency

* **Generator Output:** $P_{\text{out}} = V I_L$.
* **Total Losses:**
  $$\text{Losses} = I_a^2 R_a + W_c \approx I_L^2 R_a + W_c$$
  *(where $W_c = \text{constant losses: iron} + \text{friction} + \text{shunt field loss}$)*

* **Efficiency ($\eta$):**
  $$\eta = \frac{V I_L}{V I_L + I_L^2 R_a + W_c} = \frac{1}{1 + \frac{I_L R_a}{V} + \frac{W_c}{V I_L}}$$

* **Maximize by minimizing denominator:**
  $$\frac{d}{dI_L}\left(1 + \frac{I_L R_a}{V} + \frac{W_c}{V I_L}\right) = \frac{R_a}{V} - \frac{W_c}{V I_L^2} = 0$$
  $$\frac{R_a}{V} = \frac{W_c}{V I_L^2} \implies \mathbf{I_L^2 R_a = W_c}$$
  $$\mathbf{\text{Variable Copper Loss} = \text{Constant Loss}}$$

* **Load Current for Maximum Efficiency:**
  $$\mathbf{I_{L(\max\,\eta)} = \sqrt{\frac{W_c}{R_a}}}$$

---

## 13. Special Machines

### Universal Motor

* **Definition:** Commutated series motor capable of operating on either single-phase AC or DC at similar speed and torque.

* **Modifications from Standard DC Series Motor:**

| Feature | Universal Motor | Standard DC Series Motor |
| :--- | :--- | :--- |
| **Magnetic Core** | **Fully laminated** stator yoke and poles (minimizes AC core losses) | Solid cast steel stator frame |
| **Field Winding** | Fewer turns to reduce inductive reactance ($X_L = 2\pi f L$) | Many turns to maximize flux |
| **Air Gap** | Extremely small (lowers magnetizing reluctance & current) | Moderate air gap |
| **Commutation** | Compensating winding + high-resistance brushes (curbs AC transformer sparking) | Standard carbon brushes |

* **Applications:** Vacuum cleaners, food processors/blenders, electric hand drills, circular saws, sewing machines.

---

### Stepper Motor

* **Definition:** Brushless DC electromechanical actuator converting digital electrical pulses into precise discrete angular movements ($\beta$).

* **Step Angle Formula:**
  $$\mathbf{\beta = \frac{360^\circ}{m \cdot N_r} = \frac{|N_s - N_r|}{N_s N_r} \times 360^\circ}$$
  *(where $m$ = phases, $N_s$ = stator poles, $N_r$ = rotor teeth).*

* **Design for $30^\circ$ Step Angle (3-Phase VR Stepper):**
  * Stator poles ($N_s$) = 6 $\implies$ Pole pitch $= 360^\circ / 6 = 60^\circ$.
  * Rotor teeth ($N_r$) = 4 $\implies$ Tooth pitch $= 360^\circ / 4 = 90^\circ$.
  * Step angle: $\beta = |60^\circ - 90^\circ| = \mathbf{30^\circ}$.

* **Truth Table (3-Phase Full-Step Sequence: A $\to$ B $\to$ C):**

| Step | Phase A | Phase B | Phase C | Rotor Angle |
| :---: | :---: | :---: | :---: | :---: |
| **1** | **1** | 0 | 0 | $0^\circ$ |
| **2** | 0 | **1** | 0 | $30^\circ$ |
| **3** | 0 | 0 | **1** | $60^\circ$ |
| **4** | **1** | 0 | 0 | $90^\circ$ |

* **Applied Voltage Waveforms:**
```
Phase A: [ +V ]--------+               +--------[ +V ]--------+
         |             |               |                      |
      0V-+             +---------------+                      +-------

Phase B:               +--------[ +V ]-+
                       |               |
      0V---------------+               +------------------------------

Phase C:                               +--------[ +V ]--------+
                                       |                      |
      0V-------------------------------+                      +-------
         |<- Step 1 ->|<- Step 2 ->|<- Step 3 ->|<- Step 4 ->|
```

* **Applications:** 3D printers, CNC routers, robotic arms, disk drive head actuators, optical scanners, camera zoom/autofocus.

---

## 14. Master Formula & Numerical Cheat-Sheet

| Formula | Description / Purpose | Key Conditions |
| :--- | :--- | :--- |
| **$E = \frac{P \Phi Z N}{60 A}$** | Induced EMF / Back-EMF equation | $A = P$ (Lap), $A = 2$ (Wave) |
| **$E = k_a \Phi \omega$** | Electromechanical EMF equation | $k_a = \frac{P Z}{2\pi A}$, $\omega = \frac{2\pi N}{60}$ |
| **$T = k_a \Phi I_a$** | Developed electromagnetic torque | $T$ in $\text{N}\cdot\text{m}$ |
| **$V = E_b + I_a R_a$** | DC Motor voltage balance equation | $E_b < V$ |
| **$E_g = V + I_a R_a$** | DC Generator voltage balance equation | $E_g > V$ |
| **$P_m = E_b I_a = T \cdot \omega$** | Gross mechanical power developed | Electrical-mechanical interface |
| **$N \propto \frac{E_b}{\Phi}$** | Motor rotational speed governing relation | Governs speed controls |
| **$\omega = \frac{V_T}{k_a \Phi} - \frac{R_a}{(k_a \Phi)^2} \tau$** | Shunt motor terminal characteristic | Drooping straight line |
| **$\omega \propto \frac{1}{\sqrt{\tau}}$** | Series motor terminal characteristic | Hyperbola |
| **$Y_c = \frac{2(C \pm m)}{P}$** | Commutator pitch for wave winding | $+m$ (progressive), $-m$ (retrogressive) |
| **$a = 2 P m_{\text{lap}}$** | Current paths in Frog-Leg winding | Composite lap + wave |
| **$R_c = \frac{\Delta E_a}{\Delta I_f}$** | Critical resistance of shunt generator | Slope of OCC air-gap line |
| **$N_c = N_{\text{rated}} \frac{R_f}{R_c}$** | Critical speed for shunt generator | Below $N_c$, fails to excite |
| **$R_d = \frac{I_{se} R_{se}}{I_d}$** | Diverter resistance for compounding | Sets degree of compounding |
| **$R_{\text{ext}} = \frac{V + E_b}{I_{\text{brake}}} - R_a$** | Braking resistor for plugging | Driving voltage $\approx 2V$ |
| **$I^2 R_a = W_c$** | Maximum efficiency operating condition | Variable loss = Constant loss |
| **$I_{\max\,\eta} = \sqrt{\frac{W_c}{R_a}}$** | Current for maximum machine efficiency | Maximum efficiency point |
| **$\beta = \frac{360^\circ}{m \cdot N_r}$** | Step angle for stepper motor | Digital pulse increment |
