# Master Note: Transducers, Sensors & Static Performance of Instruments

---

> [!tip] ⚡ Quick Exam Problem-Solving Cheat Sheet & Decision Matrix
> *Instant reference to solve any theoretical derivation or numerical problem from past exams & class tests in minimal time.*

### 🎯 Fast Formula & Concept Decision Matrix

| Topic / Question Target | Given Parameters | Core Formula / Exact Answer | Exam Trap / Key Insight |
| :--- | :--- | :--- | :--- |
| **Statistical Resonant Frequencies** | $n$ readings: $x_1, x_2, \dots, x_n$ | **Mean:** $\bar{x} = \frac{\sum x_i}{n}$<br>**Deviation:** $d_i = x_i - \bar{x}$<br>**Avg Dev:** $\bar{D} = \frac{\sum \|d_i\|}{n}$<br>**Std Dev:** $s = \sqrt{\frac{\sum d_i^2}{n-1}}$<br>**Variance:** $V = s^2$ | Use $n-1$ in denominator for sample standard deviation ($n < 20$). Deviation sum $\sum d_i \equiv 0$. |
| **Voltmeter Multiplier ($R_s$)** | Meter res $R_m$, Voltage $V$, Full-scale $v_m$ | $$R_s = R_m (m - 1) \quad \text{where } m = \frac{V}{v_m}$$ | Multiplier is connected in **series** with meter movement. |
| **Ammeter-Voltmeter Relative Error** | Ammeter near $R$ ($R_a$)<br>Voltmeter acrs $R$ ($R_v$) | $$\varepsilon_r = +\frac{R_a}{R} \quad \text{(Ammeter near } R\text{)}$$<br>$$\varepsilon_r \approx -\frac{R}{R_v} \quad \text{(Voltmeter acrs } R\text{)}$$ | Threshold $R_{\text{th}} = \sqrt{R_a R_v}$. If $R > R_{\text{th}}$, place ammeter near $R$. |
| **Guarantee / Limiting Error** | Nominal $A_s$, Limiting error $\delta A$ | $$\% \varepsilon_r = \pm \frac{\delta A}{A_s} \times 100\%$$ | As measured reading $A_s \downarrow$, relative percentage error $\% \varepsilon_r \uparrow$ rapidly. |
| **Capacitive Deflection ($C_2$)** | Initial $C_1, d_1$, Deflection $\Delta d$ | $$C_2 = C_1 \left( \frac{d_1}{d_1 - \Delta d} \right)$$ | For inward deflection: gap reduces to $d_2 = d_1 - \Delta d \implies C_2 > C_1$. |
| **Capacitive Area Sensitivity ($S_x, S_\theta$)** | Width $w$, gap $d$, radius $r$ | **Translational:** $S_x = \frac{\partial C}{\partial x} = \frac{\varepsilon w}{d} = \text{const}$<br>**Rotational:** $S_\theta = \frac{\partial C}{\partial \theta} = \frac{\varepsilon r^2}{2d} = \text{const}$ | Area variation yields **strictly linear** response; distance variation yields **hyperbolic / non-linear** response. |
| **LVDT Differential Voltage** | Sec voltages $E_{s1}, E_{s2}$ | $$E_o = E_{s1} - E_{s2}$$ | At null: $E_{s1} = E_{s2} \implies E_o = 0\text{ V}$. Phase shifts $180^\circ$ when core crosses null. |
| **Hall Effect Voltage ($V_H$)** | Current $I$, Flux $B$, thickness $t$ | $$V_H = \frac{K_H \cdot I \cdot B}{t}$$ | For AC or DC current measurement in cables; high precision down to $0.025\text{ mm}$ displacement. |
| **Piezoelectric Voltage ($E_o$)** | Voltage sens $g$, thickness $t$, pressure $P$ | $$E_o = g \cdot t \cdot P = \frac{d}{\varepsilon_r \varepsilon_0} t P$$ | **Cannot measure static quantities** (internal charge leaks out; DC output is 0). |
| **Strain Gauge Factor ($G_f$)** | Poisson's ratio $\nu$ (or $\mu$), res $\rho$ | $$G_f = 1 + 2\nu + \frac{\Delta \rho / \rho}{\varepsilon} \xrightarrow{\Delta \rho \to 0} 1 + 2\nu$$ | For metals without piezoresistive effect: $G_f = 1 + 2\nu \approx 2$. |
| **RTD Temperature Resistance** | Resistance $R_0$, temp coeff $\alpha_0$, $\Delta\theta$ | **Linear:** $R_\theta = R_{\theta 0} [1 + \alpha_{\theta 0} \Delta\theta]$<br>**Quadratic:** $R_\theta = R_{\theta 0} [1 + \alpha_1 \Delta\theta + \alpha_2 (\Delta\theta)^2]$ | Platinum is industry standard (inert, highly stable, wide range $-260^\circ\text{C}$ to $+1100^\circ\text{C}$). |
| **Thermal & Shot Noise** | Temp $T$, Bandwidth $\Delta f$, Current $I$ | **Johnson:** $V_n = \sqrt{4 k T R \Delta f}$<br>**Shot:** $I_n = \sqrt{2 q I \Delta f}$ | Johnson is due to thermal agitation; Shot noise is due to discrete charge carriers. |

---

## 3. Transducer Fundamentals & Classifications

### 3.1 Sensor vs. Transducer
* **Sensor:** An input element that detects a physical parameter and generates a corresponding physical/electrical signal (usually low-level and unconditioned).
* **Transducer:** A complete device that converts energy from one form into another (most commonly non-electrical into proportional electrical quantity), incorporating sensing + signal conditioning (amplification, filtering).

| Parameter | Sensor | Transducer |
| :--- | :--- | :--- |
| **Function** | Senses physical input. | Converts input energy into electrical output. |
| **Components** | Single sensing element (e.g., bare LDR, diaphragm). | Sensor + amplifier + signal conditioning circuit. |
| **Output Level** | Very weak, cannot drive loads directly. | Conditioned, standardized voltage/current output. |

### 3.2 Inverse Transducer
* **Definition:** A device that converts an electrical signal into a non-electrical physical quantity (displacement, force, sound, pressure).
* **Examples:** Piezoelectric crystal (electrical voltage $\to$ mechanical vibration/ultrasound), loudspeaker coil, servomotor, galvanometer movement.
* **Role in Feedback Control Systems:**
  * In a closed loop, the **Transducer** measures the plant output and feeds an electrical signal back to the comparator.
  * The **Inverse Transducer** acts as the actuator (e.g., servomotor or piezo positioner) converting the controller's electrical output into physical mechanical motion to correct the process.

### 3.3 Primary vs. Secondary Transducer
* **Primary Transducer:** Detects the physical parameter directly and converts it into an intermediate mechanical displacement (e.g., Bourdon tube, diaphragm, bellows).
* **Secondary Transducer:** Converts the intermediate mechanical signal into an electrical signal (e.g., LVDT, strain gauge, capacitive plate).

![[attachments/transducer_classification_tree.png|650]]

---

## 4. Linear Variable Differential Transformer (LVDT)

![[attachments/lvdt_construction_and_schematic.png|550]]
![[Pasted image 20261014044948.png]]
### 4.1 Construction
1. **Former:** Hollow cylindrical insulating bobbin.
2. **Windings:**
   * One **Primary winding ($P$)** placed at the center, excited by an alternating voltage source ($1\text{ to }10\text{ V}$, $50\text{ Hz to }20\text{ kHz}$).
   * Two identical **Secondary windings ($S_1, S_2$)** symmetrically placed on either side of $P$, having an identical number of turns.
   * Windings $S_1$ and $S_2$ are connected in **series opposition**.
3. **Core:** High-permeability soft iron core that slides inside the former. It is **slotted longitudinally** to reduce eddy current losses.

### 4.2 Operating Principle & Output Voltage
* An AC excitation in $P$ generates an alternating flux linking $S_1$ and $S_2$, inducing voltages $E_{s1}$ and $E_{s2}$.
* Because secondaries are in series opposition:
  $$
  E_o = E_{s1} - E_{s2}
  $$

![[attachments/lvdt_characteristic_curve.png|500]]

* **Three Core States:**
  1. **Null Position (Center):** Flux linkage is equal $\implies E_{s1} = E_{s2} \implies \mathbf{E_o = 0\text{ V}}$.
  2. **Core Moved Left:** Flux linking $S_1 > S_2 \implies E_{s1} > E_{s2} \implies \mathbf{E_o = (E_{s1} - E_{s2})}$, in phase with primary.
  3. **Core Moved Right:** Flux linking $S_2 > S_1 \implies E_{s2} > E_{s1} \implies \mathbf{E_o = (E_{s2} - E_{s1})}$, **$180^\circ$ out of phase** with primary.
* Magnitude of $E_o$ is directly proportional to core displacement.

### 4.3 Pressure Measurement Using LVDT & Bourdon Tube

![[attachments/bourdon_tube_lvdt_pressure.png|550]]

* **Integration:**
  * **Primary Stage:** Pressure $P$ enters the fixed end of a C-type Bourdon tube. The closed free end deflects linearly with pressure.
  * **Secondary Stage:** The free end is linked via a mechanical rod/pulley to the soft iron core of the LVDT.
  * The LVDT converts mechanical deflection into differential AC output voltage $E_o \propto \text{Pressure } P$.

### 4.4 Merits & Limitations
* **Merits:** High linear range ($\pm 1.25\text{ mm}$ to $\pm 250\text{ mm}$), frictionless (infinite mechanical life, no wear and tear), low power consumption, high sensitivity ($40\text{ V/mm}$), negligible hysteresis.
* **Limitations:** Sensitive to stray magnetic fields (requires shielding), dynamic performance limited by core mass, vibration-sensitive, residual voltage exists at null due to harmonics and phase shifts.

### 4.5 LVDT vs. Hall Effect for Very Small Displacement
* For micro-displacements ($< 0.1\text{ mm}$):
  * **Hall Effect Transducer is more precise:** Capable of resolving displacements down to $0.025\text{ mm}$ without mechanical linkage contact, completely immune to mechanical friction and inertia.
  * **LVDT** requires physical attachment of the core, which introduces inertial loading and mechanical friction at microscopic displacements.

---

## 5. Capacitive Transducers

### 5.1 Working Principle
A parallel-plate capacitor has capacitance:
$$
C = \frac{\varepsilon A}{d} = \frac{\varepsilon_r \varepsilon_0 A}{d}
$$
Transduction occurs by varying: (1) plate separation $d$, (2) overlapping area $A$, or (3) dielectric permittivity $\varepsilon$.

![[attachments/capacitive_distance_variation_curve.png|600]]

### 5.2 Linearity Analysis: Distance ($d$) vs. Area ($A$)

#### 1. Variation of Distance between Plates ($d$) — Non-Linear
* Let initial distance be $d$. As $d$ varies:
  $$
  C \propto \frac{1}{d} \implies \frac{\partial C}{\partial d} = -\frac{\varepsilon A}{d^2}
  $$
* The relationship between $C$ and displacement $x$ is **hyperbolic (strictly non-linear)**. Sensitivity increases drastically as plates come closer.

#### 2. Variation of Overlapping Area (Translational $x$) — Linear
![[attachments/capacitive_linear_area_displacement.png|550]]
* Overlapping area $A = w \cdot x$ (width $w$, overlap length $x$):
  $$
  C = \frac{\varepsilon w x}{d} \implies \text{Sensitivity } S_x = \frac{\partial C}{\partial x} = \frac{\varepsilon w}{d} = \mathbf{\text{Constant}}
  $$
* Constant sensitivity $\implies$ **strictly linear relationship** between capacitance and linear displacement.

#### 3. Variation of Overlapping Area (Angular $\theta$) — Linear
![[attachments/capacitive_angular_displacement.png|450]]
* For semi-circular plates of radius $r$ at angle $\theta$ (rad):
  $$
  A = \frac{1}{2} r^2 \theta \implies C = \frac{\varepsilon r^2 \theta}{2 d} \implies \text{Sensitivity } S_\theta = \frac{\partial C}{\partial \theta} = \frac{\varepsilon r^2}{2 d} = \mathbf{\text{Constant}}
  $$
* Yields **strictly linear relationship** between capacitance and angular displacement.

---

### 5.3 Force / Pressure Measurement (Diaphragm Type)
![[attachments/capacitive_pressure_diaphragm.png|350]]
* A flexible conductive diaphragm acts as the movable plate separated from a fixed static plate by distance $d$.
* Applied fluid pressure deflects the diaphragm center by $\Delta d$, decreasing plate separation to $(d - \Delta d)$ and increasing $C$. Measured via an AC bridge.

---

### 5.4 Solved Exam Numerical Problems

#### Problem 1 (Page 3, Q.8 c):
> Two quartz diaphragms of area $750\text{ mm}^2$ separated by $3.5\text{ mm}$. Applied pressure $900\text{ kN/m}^2$ produces a deflection of $0.6\text{ mm}$. Initial capacitance $C_1 = 370\text{ pF}$. Find capacitance after pressure application.

* **Solution:**
  * Initial separation $d_1 = 3.5\text{ mm}$.
  * Deflection $\Delta d = 0.6\text{ mm} \implies$ New separation $d_2 = d_1 - \Delta d = 3.5 - 0.6 = 2.9\text{ mm}$.
  * Since $C = \frac{\varepsilon A}{d}$, and $\varepsilon, A$ are constant:
    $$
    C_2 = C_1 \left( \frac{d_1}{d_2} \right) = 370\text{ pF} \times \left( \frac{3.5\text{ mm}}{2.9\text{ mm}} \right) = 370 \times 1.2069 = \mathbf{446.55\text{ pF}}
    $$

#### Problem 2 (Page 5, Q.7 c & Page 29, CT#4 Q2):
> Variable capacitance transducer: diaphragms $20\text{ mm}$ diameter, $4\text{ mm}$ apart. Pressure produces average deflection of $0.25\text{ mm}$. Initial capacitance $C_1 = 400\text{ pF}$. Calculate capacitance after force is applied.

* **Solution:**
  * Initial separation $d_1 = 4.0\text{ mm}$.
  * Deflection $\Delta d = 0.25\text{ mm} \implies$ New separation $d_2 = 4.0 - 0.25 = 3.75\text{ mm}$.
  * New capacitance:
    $$
    C_2 = C_1 \left( \frac{d_1}{d_2} \right) = 400\text{ pF} \times \left( \frac{4.0\text{ mm}}{3.75\text{ mm}} \right) = \mathbf{426.67\text{ pF}}
    $$

---

## 6. Hall Effect Transducers

![[attachments/hall_effect_principle.png|450]]

### 6.1 Principle of Operation
* **Hall Effect:** When a current-carrying conductor or semiconductor strip is placed in a transverse magnetic field, a transverse potential difference (Hall voltage $V_H$) is developed across the opposite edges of the strip.
* **Formula:**
  $$
  \mathbf{V_H = \frac{K_H \cdot I \cdot B}{t}}
  $$
  *(where $K_H$ = Hall coefficient, $I$ = current, $B$ = magnetic flux density, $t$ = strip thickness).*

### 6.2 Measurement of Current in a Cable / Very High Currents
```
      [ Current-Carrying Conductor I ]
                  (●)
               /       \
      ┌───────/         \───────┐
      │  Ferromagnetic Slotted   │
      │       Core Ring         │
      └───────\  [Air]  /───────┘
               \ [Gap] /
                 [===]  <-- Hall Effect Sensor Element
                   │
                   └──> Output Hall Voltage V_H ∝ I
```
* **Method:** A ferromagnetic split-toroid core is clamped around the conductor carrying current $I$.
* The current creates magnetic flux in the core: $B = \frac{\mu I}{2\pi r}$.
* A Hall element is inserted inside the air gap of the core and biased with a constant reference current $I_c$.
* Output voltage $V_H \propto B \propto I$. Gives direct, isolated measurement of cable current.

### 6.3 Comparison: Hall Effect Transducer vs. Clamp-On Ammeter
| Feature | Hall Effect Transducer | Clamp-On Ammeter (Current Transformer) |
| :--- | :--- | :--- |
| **Current Type** | Measures **both AC and DC**. | Measures **AC only** (relies on $d\Phi/dt$). |
| **Frequency Range** | DC up to high frequencies (hundreds of kHz). | Power frequencies ($50/60\text{ Hz}$). |
| **Saturation** | Wide linear range; low core loss. | Susceptible to core saturation and phase error. |
| **Convenience** | Highly versatile for modern DC/inverter drives. | Convenient for purely AC grid cables. |

### 6.4 Measurement of Displacement
![[attachments/hall_effect_displacement_measurement.png|550]]
* A permanent magnet and a ferromagnetic plate establish a magnetic field across a gap containing a Hall element.
* As the plate or magnet moves, the gap flux density $B$ changes, varying $V_H$.
* Resolves displacements as minute as **$0.025\text{ mm}$**.

---

## 7. Piezoelectric Transducers

![[attachments/piezoelectric_effect_compression.png|550]]

### 7.1 Principle & Materials
* **Piezoelectric Effect:** When mechanical stress/force is applied to asymmetrical crystalline materials, an electric charge appears across opposite faces. Conversely, applying voltage produces mechanical strain (inverse effect).
* **Common Materials:** PZT (Lead Zirconate Titanate), Quartz, Rochelle Salt, Lithium Sulphate, Barium Titanate.

### 7.2 Mathematical Derivations: Charge & Voltage Sensitivities

#### 1. Charge Generated ($Q$):
$$
Q = d \cdot F
$$
*(where $d$ = crystal charge sensitivity in $\text{C/N}$, $F$ = applied force).*

#### 2. Mechanical Strain & Force:
From Young's Modulus $E = \frac{\text{Stress}}{\text{Strain}} = \frac{F / A}{\Delta t / t}$:
$$
F = \frac{A \cdot E}{t} \Delta t \implies Q = d \cdot A \cdot E \frac{\Delta t}{t}
$$

#### 3. Output Voltage ($E_o$):
The crystal acts as a parallel plate capacitor: $C_p = \varepsilon_r \varepsilon_0 \frac{A}{t}$.
$$
E_o = \frac{Q}{C_p} = \frac{d \cdot F}{\varepsilon_r \varepsilon_0 \frac{A}{t}} = \left( \frac{d}{\varepsilon_r \varepsilon_0} \right) \cdot t \cdot \left(\frac{F}{A}\right)
$$
Defining **Voltage Sensitivity $g$**:
$$
g = \frac{d}{\varepsilon_r \varepsilon_0} = \frac{E_o / t}{P} = \frac{\text{Electric Field Intensity}}{\text{Pressure (Stress)}} \quad (\text{V}\cdot\text{m/N})
$$
$$
\mathbf{E_o = g \cdot t \cdot P} \quad \blacksquare
$$

### 7.3 Equivalent Circuit & Why It Cannot Measure Static Quantities
![[attachments/piezoelectric_equivalent_circuit.png|500]]

* **Equivalent Circuit:** An ideal voltage source $V_s$ in series with crystal capacitance $C_p$ and internal leakage resistance $R_s$, connected across load $R_L$.
* **Why Static Measurement is Impossible:**
  * Under static force, charge $Q$ is generated once.
  * The charge leaks away immediately through the finite internal resistance $R_s$ and external load $R_L$ with time constant $\tau = R C$.
  * For steady state ($\omega = 0$, DC), steady output voltage drops to zero:
    $$
    e_o(t) \to 0
    $$
  * Hence, piezoelectric transducers are strictly useful for **dynamic measurements** (vibration, shock, fast transients).

### 7.4 Potentiometric Type Accelerometer
* Operates with a seismic mass $M$ attached to a spring $k$ and damper $c$. The mass drives a wiper across a linear potentiometer wire.
* Under acceleration $a$, inertial force $F = M a$ deflects the spring ($x = M a / k$). The wiper displacement changes output voltage $V_o \propto a$.

---

## 8. Strain Gauges & Piezoresistive Effect

![[attachments/strain_gauge_construction.png|450]]

### 8.1 Working Principle & Construction
* A strain gauge is a thin metallic foil/wire grid bonded to an insulating backing. When bonded to a structure under stress, the wire undergoes mechanical elongation/compression, altering its electrical resistance.

![[attachments/strain_gauge_elongation_piezoresistive.png|500]]

### 8.2 Derivation of Gauge Factor ($G_f$)
Resistance of a round wire:
$$
R = \rho \frac{L}{A}
$$
Differentiating with respect to applied stress $s$:
$$
\frac{dR}{ds} = \frac{\rho}{A} \frac{\partial L}{\partial s} - \frac{\rho L}{A^2} \frac{\partial A}{\partial s} + \frac{L}{A} \frac{\partial \rho}{\partial s}
$$
Dividing throughout by $R = \rho L / A$:
$$
\frac{1}{R} \frac{dR}{ds} = \frac{1}{L} \frac{\partial L}{\partial s} - \frac{1}{A} \frac{\partial A}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s}
$$
For a circular wire with diameter $D$, $A = \frac{\pi}{4} D^2 \implies \frac{\partial A}{\partial s} = 2 \frac{\pi}{4} D \frac{\partial D}{\partial s} \implies \frac{1}{A} \frac{\partial A}{\partial s} = \frac{2}{D} \frac{\partial D}{\partial s}$.
Using Poisson's ratio:
$$
\nu = -\frac{\partial D / D}{\partial L / L} \implies \frac{1}{D} \frac{\partial D}{\partial s} = -\nu \frac{1}{L} \frac{\partial L}{\partial s}
$$
Substitute into the equation:
$$
\frac{1}{R} \frac{dR}{ds} = \frac{1}{L} \frac{\partial L}{\partial s} + 2\nu \frac{1}{L} \frac{\partial L}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s}
$$
For small finite changes:
$$
\frac{\Delta R}{R} = \frac{\Delta L}{L} (1 + 2\nu) + \frac{\Delta \rho}{\rho}
$$
Dividing by axial strain $\varepsilon = \Delta L / L$:
$$
\mathbf{G_f = \frac{\Delta R / R}{\Delta L / L} = 1 + 2\nu + \frac{\Delta \rho / \rho}{\varepsilon}}
$$
Where:
* $1$: Resistance change due to length change.
* $2\nu$: Resistance change due to cross-sectional area change.
* $\frac{\Delta \rho / \rho}{\varepsilon}$: Resistance change due to **Piezoresistive Effect** (change in resistivity with strain).
* When piezoresistive effect is neglected ($\Delta \rho \approx 0$):
  $$
  \mathbf{G_f = 1 + 2\nu \quad (\text{or } 1 + 2\mu)} \quad \blacksquare
  $$

### 8.3 Gas Pressure Measurement in an LPG Cylinder
1. **Principle:** Internal gas pressure $P$ produces circumferential (hoop) tensile stress in the thin cylinder walls:
   $$
   \sigma_h = \frac{P \cdot D_c}{2 t_c} \implies \text{Hoop Strain } \varepsilon_h = \frac{P D_c}{2 t_c E} \left(1 - \frac{\nu}{2}\right)
   $$
2. **Mounting:** An active strain gauge $R_1$ is bonded circumferentially on the external surface of the cylinder. A dummy gauge $R_2$ is mounted unstrained nearby on an identical metal block for temperature compensation.
3. **Bridge Connection:** Gauges are connected into a Wheatstone bridge. The unbalance voltage $V_{\text{out}} \propto \varepsilon_h \propto P$.

---

## 9. Temperature Transducers (RTD, Thermocouple, Thermistor)

### 9.1 Resistance Temperature Detector (RTD)
* **Principle:** Positive temperature coefficient (PTC) of metals—resistance increases predictably with temperature.
* **Requirements:** High temperature coefficient, high resistivity (compact size), stable and linear $R-T$ relationship.
* **Materials:** **Platinum** (industry benchmark: $-260^\circ\text{C}$ to $1100^\circ\text{C}$, inert, non-corrosive), Copper ($0\text{ to }180^\circ\text{C}$), Nickel (high sensitivity, non-linear above $300^\circ\text{C}$).

![[attachments/rtd_characteristics_and_table.png|600]]

* **Approximations:**
  * **Linear Approximation:** Over small temperature spans:
    $$
    R_\theta = R_{\theta 0} [1 + \alpha_{\theta 0} (\theta - \theta_0)] \quad \text{where } \alpha_{\theta 0} = \frac{1}{R_{\theta 0}} \left( \frac{R_{\theta 2} - R_{\theta 1}}{\theta_2 - \theta_1} \right)
    $$
  * **Quadratic Approximation:** For broader, precision spans:
    $$
    R_\theta = R_{\theta 0} [1 + \alpha_1 \Delta\theta + \alpha_2 (\Delta\theta)^2]
    $$

---

### 9.2 Thermocouple
![[attachments/thermocouple_temperature_circuit.png|500]]

* **Seebeck Effect:** When two dissimilar metal conductors are joined to form two junctions held at different temperatures ($T_{\text{hot}}$ and $T_{\text{cold}}$), a thermoelectric emf is produced:
  $$
  E = a(T_h - T_c) + b(T_h - T_c)^2
  $$
* **Pros:** Rugged, wide range (up to $2000^\circ\text{C}$), no external power (active), fast response.
* **Cons:** Low voltage output ($\mu\text{V/}^\circ\text{C}$), non-linear, requires cold-junction reference compensation.

---

### 9.3 Thermistor
![[attachments/thermistor_ntc_vs_platinum_curve.png|550]]

* **Construction:** Sintered compact mixtures of semiconductor metallic oxides (Manganese, Nickel, Cobalt, Copper, Iron).
* **Characteristics:** High **Negative Temperature Coefficient (NTC)**; resistance drops exponentially as temperature rises:
  $$
  R_T = R_0 \exp \left[ \beta \left( \frac{1}{T} - \frac{1}{T_0} \right) \right]
  $$
* Extremely sensitive (10x more sensitive than Platinum RTD), range $-100^\circ\text{C}$ to $+300^\circ\text{C}$.

#### Air Conditioner Temperature Control Circuit with Relay:
```
       +Vcc
        │
        ├──[ Fixed Resistor R1 ]──┐
        │                         ├───(+) Non-Inverting Input
        ├──[ NTC Thermistor ]─────┘       [ Op-Amp Comparator ]───[ Rb ]─── B [ NPN Transistor ]
        │                                 /                                      │ C
        ├──[ Potentiometer Vref ]─────────(-) Inverting Input                     ├──[ Relay Coil ]── +Vcc
        │                                                                        │  (Flyback Diode ||)
       GND                                                                      E
                                                                                 │
                                                                                GND
```
* **Operation:**
  1. $R_1$ and NTC thermistor form a potential divider connected to the Op-Amp (+).
  2. As room temperature increases, NTC resistance drops $\implies$ Voltage at (+) rises.
  3. When $V_{(+)} > V_{\text{ref}}$, Op-amp output switches HIGH $\to$ forward-biases the NPN transistor into saturation.
  4. The transistor energizes the relay coil, closing contact switches to start the AC cooling compressor.

---

## 10. Optical & Proximity Transducers

### 10.1 Photoconductive Cell / LDR
![[attachments/ldr_photoconductive_curve_and_circuit.png|600]]

* **Principle:** Uses semiconductor elements (CdS, Ge, Se). Incident photon energy exceeds bandgap, generating electron-hole pairs. Conductivity rises; resistance drops from $\sim 1\text{ M}\Omega$ (dark) to $< 100\ \Omega$ (bright light).

#### Automatic Night Light (LDR + NPN Transistor + LED Circuit):
```
      +Vcc
       │
       ├──[ Fixed Resistor R1 ]──┐
       │                         ├─── Base (B) [ NPN Transistor ]
       ├──[ LDR Sensor ]─────────┘         │ Collector (C)
       │                                   ├──[ Current Limit Rc ]──[ LED ]── +Vcc
      GND                                 Emitter (E)
                                           │
                                          GND
```
* **Circuit Analysis:**
  * **Daylight (Bright):** Light hits LDR $\implies R_{\text{LDR}} \ll R_1$. Base voltage $V_B = V_{CC} \frac{R_{\text{LDR}}}{R_1 + R_{\text{LDR}}} < 0.7\text{ V}$. Transistor remains in **Cutoff** $\implies$ LED is **OFF**.
  * **Darkness (Night):** $R_{\text{LDR}}$ shoots up to hundreds of $\text{k}\Omega \implies V_B > 0.7\text{ V}$. Transistor switches into **Saturation** $\implies$ Collector current flows, turning LED **ON**.

---

### 10.2 Proximity Transducers: Inductive vs. Capacitive vs. Photoelectric

![[attachments/inductive_proximity_sensor_operation.png|500]]

#### 1. Inductive (Eddy-Current Killed Oscillator):
* Core with coil radiates RF electromagnetic field ($100\text{ kHz}-1\text{ MHz}$).
* When a **conductive metallic target** approaches, eddy currents are induced in the target, absorbing energy and **lowering the oscillator amplitude**. A Schmitt trigger detects amplitude drop and flips the digital output switch.

#### 2. Capacitive Proximity Sensor:
* Sensing plate forms one plate of an open capacitor; earth ground forms the second.
* When **any target (metallic or non-metallic/liquid)** enters the field, capacitance increases, initiating or altering oscillator frequency to trigger output.

#### 3. Comparison: Photo-Electric vs. Oscillation Proximity Transducers
| Parameter | Photo-Electric Transducer | Oscillation (Inductive/Capacitive) Transducers |
| :--- | :--- | :--- |
| **Sensing Principle** | Light beam interruption / reflection (Photodiodes/LDR). | RF electromagnetic / electrostatic field perturbation. |
| **Target Material** | Any opaque/reflective object (color-sensitive). | Inductive: Metals only. Capacitive: Any dielectric. |
| **Environment** | Vulnerable to dust, dirt, smoke, oil splashes on optical lens. | **Extremely rugged**, immune to dirt, water, oil, grease. |
| **Sensing Distance** | Long range (up to tens of meters with reflector). | Short range ($1\text{ mm to }50\text{ mm}$). |
| **Wear & Life** | High life; optical degradation over time. | Solid-state, hermetically sealed, virtually indefinite life. |

---

## 11. Measurement of Velocity & Speed

### 11.1 Linear Velocity
* **Electromagnetic Moving-Coil / Moving-Magnet Pickup:**
  * A permanent magnet moves inside a stationary coil attached to the moving member.
  * Induced emf:
    $$
    e = B \cdot l \cdot v
    $$
    *(Directly proportional to linear velocity $v$, self-generating active transducer).*

### 11.2 Angular Velocity & Speed
1. **DC / AC Tachometer Generator:**
   * Permanent magnet DC generator coupled to rotating shaft.
   * Generated DC emf:
     $$
     E_g = \left( \frac{P \cdot Z \cdot \Phi}{60 \cdot A} \right) N = k_t \cdot \omega
     $$
2. **Digital Magnetic / Optical Pulse Pickup (Toothed Wheel Counter):**
   * Ferromagnetic toothed wheel with $P$ teeth rotates on shaft past a variable reluctance sensor.
   * Each passing tooth generates an electrical pulse.
   * For shaft speed $N$ (rpm), output frequency:
     $$
     f = \frac{P \cdot N}{60} \implies \mathbf{N = \frac{60 \cdot f}{P}\text{ rpm}}
     $$
