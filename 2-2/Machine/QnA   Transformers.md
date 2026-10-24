### **1. Ideal transformer - transformation ratio**
*(Reference Ranges: **Theraja Vol. II:** pp. 1115–1120 | **Chapman 5th Ed.:** pp. 69–76 | **Slides:** Slides 1–17)*

### 1. Page 17, Q.1(a): What is transformer? Briefly describe the basic construction and working principle of a transformer.

* **Definition:** A static electrical device that transfers AC electrical energy from one circuit to another at the same frequency through electromagnetic induction, usually stepping voltage up or down.
* **Basic Construction:**
  * **Magnetic Core:** Built from thin laminated silicon-steel sheets to minimize eddy current and hysteresis losses; provides a low-reluctance path for magnetic flux.
  * **Primary Winding:** Connected to the AC input source; receives electrical energy.
  * **Secondary Winding:** Connected to the load; delivers transformed energy.
* **Working Principle:**
  1. Alternating voltage $V_1$ applied to the primary winding drives an alternating magnetizing current.
  2. This produces an alternating mutual magnetic flux ($\Phi = \Phi_m \sin\omega t$) in the iron core.
  3. By Faraday's Law, this alternating flux links both windings, inducing self-induced EMF $E_1$ in the primary and mutually induced EMF $E_2$ in the secondary:
     $$e = -N \frac{d\Phi}{dt}$$
  4. When a closed load is connected to the secondary, $E_2$ drives secondary load current $I_2$.

* **Reference in Theraja (Vol. II):** pp. 1115–1117
* **Reference in Chapman (5th Ed.):** pp. 69–71
* **Reference in Slide PDF:** Slides 1–5

---

### 2. Page 17, Q.1(c): By mistake, you have connected a DC supply to a transformer. What will be the effects on transformer in that condition?

* **No Dynamic Induction:** DC voltage produces a constant, unidirectional magnetic flux ($d\Phi/dt = 0$).
* **Zero Counter-EMF:** By Faraday's Law, back-EMF is zero ($E_1 = 0$) once steady state is reached.
* **Massive Current Draw:** Only primary winding resistance ($R_1$, typically $< 1\ \Omega$) opposes current flow:
  $$I_{\text{dc}} = \frac{V_{\text{dc}}}{R_1} \gg I_{\text{rated}}$$
* **Disastrous Consequences:**
  * Extreme $I^2 R$ heating burns the primary winding insulation within seconds.
  * The iron core enters deep magnetic saturation, producing heavy buzzing and severe smoke/fire hazard.
  * Overcurrent protective devices (breakers/fuses) will trip immediately.

* **Reference in Theraja (Vol. II):** p. 1118
* **Reference in Chapman (5th Ed.):** p. 72
* **Reference in Slide PDF:** Slide 6

---

### 3. Page 17, Q.1(d): Define voltage transformation ratio. What will happen if 60 Hz transformer is connected to 50 Hz supply.

* **Voltage Transformation Ratio ($K$):**
  $$K = \frac{E_2}{E_1} \approx \frac{V_2}{V_1} = \frac{N_2}{N_1}$$
  *(Ratio of secondary induced EMF/turns to primary induced EMF/turns).*
* **Connecting a 60 Hz Transformer to a 50 Hz Supply ($V$ constant):**
  1. **Core Flux Increases:** From $E \approx 4.44 f N \Phi_m \implies \Phi_m \propto \frac{V}{f}$. As frequency drops from 60 Hz to 50 Hz ($f \downarrow$ by $16.7\%$), maximum core flux $\Phi_m$ increases by $\approx 20\%$.
  2. **Core Saturation & High No-Load Current:** Core iron is pushed deep into magnetic saturation, causing a disproportionate spike in magnetizing current ($I_m$) and primary copper losses.
  3. **Hysteresis Loss Spikes:** $P_h \propto f B_m^{1.6} \propto f (1/f)^{1.6} = f^{-0.6}$. Core loss and operating temperature increase significantly.
  4. **Derating Requirement:** The transformer must be operated at reduced input voltage ($V_{\text{new}} = \frac{50}{60} V = 83.3\% V_{\text{rated}}$) to avoid overheating.

* **Reference in Theraja (Vol. II):** pp. 1118–1120
* **Reference in Chapman (5th Ed.):** pp. 74–76
* **Reference in Slide PDF:** Slides 14–17

---

### 4. Page 18, Q.1(b): Prove that, v1/v2 = N1/N2 = I2/I1 where symbols have their usual meanings.

**Proof:**
1. **Voltage & Turns Ratio:**
   * Instantaneous induced EMFs linked by mutual core flux $\Phi$:
     $$e_1 = -N_1 \frac{d\Phi}{dt}, \quad e_2 = -N_2 \frac{d\Phi}{dt}$$
   * Taking RMS values for an ideal transformer (zero winding resistance and zero leakage, so $V_1 = E_1$ and $V_2 = E_2$):
     $$\frac{V_1}{V_2} = \frac{E_1}{E_2} = \frac{N_1}{N_2}$$
2. **Current Ratio (MMF Balance):**
   * An ideal transformer core has infinite permeability ($\mu \rightarrow \infty$), requiring zero net MMF to maintain flux:
     $$\mathcal{F}_{\text{net}} = N_1 I_1 - N_2 I_2 = 0 \implies N_1 I_1 = N_2 I_2$$
     $$\frac{I_2}{I_1} = \frac{N_1}{N_2}$$
3. **Combined Identity:**
   $$\mathbf{\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}}$$

* **Reference in Theraja (Vol. II):** pp. 1118–1119
* **Reference in Chapman (5th Ed.):** pp. 72–74
* **Reference in Slide PDF:** Slides 9–13

---

### 5. Page 19, Q.1(a): Show that the emf induced in the secondary winding of a transformer is E2 = 4.44 f N2 φm, where symbols have their usual meanings.

**Derivation:**
1. Let sinusoidal core flux be:
   $$\Phi = \Phi_m \sin(\omega t) = \Phi_m \sin(2\pi f t)$$
2. Induced secondary EMF by Faraday's Law:
   $$e_2 = -N_2 \frac{d\Phi}{dt} = -N_2 \frac{d}{dt}[\Phi_m \sin(2\pi f t)] = -2\pi f N_2 \Phi_m \cos(2\pi f t)$$
3. Maximum induced secondary EMF:
   $$E_{2m} = 2\pi f N_2 \Phi_m$$
4. RMS value for sinusoidal waveform:
   $$E_2 = \frac{E_{2m}}{\sqrt{2}} = \frac{2\pi}{\sqrt{2}} f N_2 \Phi_m = \sqrt{2}\pi f N_2 \Phi_m$$
   Since $\sqrt{2}\pi \approx 1.4142 \times 3.1416 \approx 4.4428$:
   $$\mathbf{E_2 = 4.44 f N_2 \Phi_m}$$

* **Reference in Theraja (Vol. II):** pp. 1117–1118
* **Reference in Chapman (5th Ed.):** pp. 71–72
* **Reference in Slide PDF:** Slides 7–9

---

### 6. Page 23, Q.9: Define step-up and step-down transformer.

* **Step-Up Transformer:**
  * Increases voltage from primary to secondary ($V_2 > V_1$).
  * $N_2 > N_1$ (transformation ratio $K > 1$).
  * Secondary current is lower than primary current ($I_2 < I_1$).
  * *Application:* Generating stations to step up generation voltage (e.g., 11 kV to 132/400 kV) for efficient long-distance transmission.
* **Step-Down Transformer:**
  * Decreases voltage from primary to secondary ($V_2 < V_1$).
  * $N_2 < N_1$ (transformation ratio $K < 1$).
  * Secondary current is higher than primary current ($I_2 > I_1$).
  * *Application:* Distribution substations to step down transmission voltage to consumer levels (e.g., 11 kV to 400 V / 230 V).

* **Reference in Theraja (Vol. II):** p. 1118
* **Reference in Chapman (5th Ed.):** pp. 73–74
* **Reference in Slide PDF:** Slides 10–12

---

### 7. Page 23, Q.10: Derive the equation of induced e.m.f. in the whole of primary winding of a transformer with net diagram. [Figure Involved]

#### Core Diagram
```
     +----------- Core (Flux Phi) -----------+
     |                                       |
  [Primary]                               [Secondary]
  N1 Turns                                N2 Turns
  Input V1 ~                              Output V2
     |                                       |
     +---------------------------------------+
```

**Derivation:**
1. In one cycle ($T = 1/f$), flux rises from 0 to $\Phi_m$ in a quarter period ($t = T/4 = \frac{1}{4f}\text{ s}$).
2. Average rate of change of flux:
   $$\left(\frac{d\Phi}{dt}\right)_{\text{avg}} = \frac{\Phi_m}{1/(4f)} = 4 f \Phi_m \text{ Wb/s}$$
3. Average EMF induced per turn:
   $$e_{\text{avg/turn}} = 4 f \Phi_m \text{ Volts}$$
4. For a pure sine wave, Form Factor $k_f = \frac{\text{RMS}}{\text{Average}} = 1.11$:
   $$e_{\text{RMS/turn}} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m \text{ Volts}$$
5. Total RMS induced primary EMF for $N_1$ turns:
   $$\mathbf{E_1 = 4.44 f N_1 \Phi_m}$$

* **Reference in Theraja (Vol. II):** pp. 1117–1118
* **Reference in Chapman (5th Ed.):** pp. 71–72
* **Reference in Slide PDF:** Slides 7–9

---

### 8. Page 23, Q.11: What is voltage transformation ratio or turns ratio? Why it is important?

* **Definitions:**
  * **Voltage Transformation Ratio ($K$):** $K = \frac{V_2}{V_1} = \frac{E_2}{E_1} = \frac{N_2}{N_1}$
  * **Turns Ratio ($a$):** $a = \frac{N_1}{N_2} = \frac{1}{K}$
* **Importance:**
  1. **Voltage & Current Scaling:** Dictates exact voltage step-up or step-down levels and reciprocal current scaling ($I_1 = K I_2$).
  2. **Impedance Matching:** Determines reflected impedance across windings:
     $$Z_1' = a^2 Z_2 = \frac{Z_2}{K^2}$$
  3. **Parallel Operation:** Paralleled transformers must possess identical turns ratios to avoid massive circulating currents.

* **Reference in Theraja (Vol. II):** pp. 1118–1120
* **Reference in Chapman (5th Ed.):** pp. 73–75
* **Reference in Slide PDF:** Slides 10–13

---

### 9. Page 23, Q.12: What will happen if a 60 Hz transformer is connected to 50 Hz supply?

* **Flux Increase:** Since $\Phi_m \propto V/f$, at rated voltage, lowering frequency from 60 Hz to 50 Hz increases core flux by:
  $$\frac{60}{50} = 1.20 \implies +20\%$$
* **Magnetic Saturation:** Core operates beyond knee $\implies$ magnetizing current $I_m$ surges up to several times rated value.
* **Overheating:** Iron core losses and primary copper losses ($I_0^2 R_1$) increase, causing severe insulation thermal stress.
* **Remedy:** Reduce operating voltage to $V_{50} = \frac{50}{60} V_{60} = 0.833 V_{60}$.

* **Reference in Theraja (Vol. II):** pp. 1119–1120
* **Reference in Chapman (5th Ed.):** pp. 75–76
* **Reference in Slide PDF:** Slides 14–17

---

### 10. Page 36, Q.1(b): What will happen if a dc source of rated value is applied across the primary coil of a transformer?

* **Zero Induced Back-EMF:** DC creates steady flux $\implies d\Phi/dt = 0 \implies E_1 = 0$.
* **Excessive Current:** Primary winding current is limited solely by low winding resistance $R_1$:
  $$I_{\text{dc}} = \frac{V_{\text{rated}}}{R_1} \gg I_{\text{rated}}$$
* **Failure:** Rapid overheating burns insulation, trips protection breakers, and hazards core fire.

* **Reference in Theraja (Vol. II):** p. 1118
* **Reference in Chapman (5th Ed.):** p. 72
* **Reference in Slide PDF:** Slide 6

---

### 11. Page 36, Q.1(c): What will happen if a transformer rated at 50 Hz is operated on 60 Hz supply line?

* **Flux Density Decreases:** $\Phi_m \propto V/f \implies$ at 60 Hz, core flux drops by $50/60 = 83.3\%$ of original rating.
* **Core Operates Cooler:** Lower flux density keeps iron comfortably below saturation; magnetizing current $I_m$ decreases.
* **Loss Profile:**
  * Eddy current loss ($P_e \propto f^2 B_m^2 \propto f^2 (1/f)^2$) remains unchanged.
  * Hysteresis loss ($P_h \propto f B_m^{1.6} \propto f^{-0.6}$) decreases slightly.
* **Reactance Increases:** Leakage reactance increases ($X = 2\pi f L \uparrow$), causing slightly poorer voltage regulation.
* **Safe Operation:** Completely safe to operate without risk of thermal burnout.

* **Reference in Theraja (Vol. II):** pp. 1119–1120
* **Reference in Chapman (5th Ed.):** pp. 75–76
* **Reference in Slide PDF:** Slides 14–17

---

### 12. Page 40, Q.1(a): Does transformer draw any current when secondary is open? Why? Derive the emf equation of single phase transformer

* **Yes, it draws No-Load Current ($I_0$):**
  * Even with secondary open-circuited, the primary draws small no-load current $I_0$ (typically 2–5% of full-load current).
  * **Why:** Needed to:
    1. Establish working mutual flux in the core (**Magnetizing component**, $I_m = I_0 \sin\phi_0$).
    2. Supply hysteresis and eddy current iron losses (**Core-loss component**, $I_w = I_0 \cos\phi_0$).
* **EMF Equation Derivation:**
  * Let $\Phi = \Phi_m \sin(\omega t)$.
  * Induced EMF: $e = -N \frac{d\Phi}{dt} = -N \omega \Phi_m \cos(\omega t) = 2\pi f N \Phi_m \sin(\omega t - 90^\circ)$.
  * Peak EMF: $E_m = 2\pi f N \Phi_m$.
  * RMS EMF: $E = \frac{E_m}{\sqrt{2}} = \frac{2\pi}{\sqrt{2}} f N \Phi_m = \mathbf{4.44 f N \Phi_m}$.

* **Reference in Theraja (Vol. II):** pp. 1117–1118, 1120–1121
* **Reference in Chapman (5th Ed.):** pp. 71–72, 76–78
* **Reference in Slide PDF:** Slides 7–9, 18–20

---

### 13. Page 40, Q.1(c): A single phase transformer has 1000 turns on the primary and 200 turns on the secondary. The no load current is 3 amp at a pf of 0.2 lagging. Calculate the primary current and power factor when the secondary current is 280 amp at a p.f of 0.80 lagging.

**Given Data:**
* $N_1 = 1000$, $N_2 = 200 \implies K = \frac{N_2}{N_1} = \frac{200}{1000} = 0.2$
* $I_0 = 3\text{ A}$, $\cos\phi_0 = 0.2$ lagging $\implies \sin\phi_0 = \sqrt{1 - (0.2)^2} \approx 0.9798$
* $I_2 = 280\text{ A}$, $\cos\phi_2 = 0.8$ lagging $\implies \sin\phi_2 = 0.6$

**Step 1: Reflected Secondary Current on Primary ($I_2'$)**
$$I_2' = K I_2 = 0.2 \times 280 = 56\text{ A}$$

**Step 2: Component Breakdown (Taking $-V_1'$ as reference)**
* In-phase components (horizontal):
  $$I_{1x} = I_0 \cos\phi_0 + I_2' \cos\phi_2 = (3 \times 0.2) + (56 \times 0.8) = 0.6 + 44.8 = 45.4\text{ A}$$
* Quadrature lagging components (vertical):
  $$I_{1y} = I_0 \sin\phi_0 + I_2' \sin\phi_2 = (3 \times 0.9798) + (56 \times 0.6) = 2.94 + 33.6 = 36.54\text{ A}$$

**Step 3: Total Primary Current ($I_1$)**
$$I_1 = \sqrt{I_{1x}^2 + I_{1y}^2} = \sqrt{(45.4)^2 + (36.54)^2} = \sqrt{2061.16 + 1335.17} = \sqrt{3396.33} \approx \mathbf{58.28\text{ A}}$$

**Step 4: Primary Power Factor ($\cos\phi_1$)**
$$\cos\phi_1 = \frac{I_{1x}}{I_1} = \frac{45.4}{58.28} \approx \mathbf{0.779\text{ lagging}}$$

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–26

---

### **2. No-load and load vector diagrams**
*(Reference Ranges: **Theraja Vol. II:** pp. 1120–1126 | **Chapman 5th Ed.:** pp. 76–86 | **Slides:** Slides 18–26)*

### 15. Page 7, Q.1(a): Draw the vector diagram of a 1-φ transformer connected with unity p.f., lagging p.f., and leading p.f load. [Figure Involved]

![[Pasted image 20260908231027.png]]
![[Pasted image 20260908231224.png]]
![[Pasted image 20260908231042.png]]
![[Pasted image 20260908231137.png]]

* **Phasor Relationships:**
  * Core flux $\Phi$ is reference along horizontal axis.
  * Induced EMFs $E_1, E_2$ lag flux $\Phi$ by $90^\circ$.
  * Primary applied voltage $-E_1$ opposes $E_1$ by $180^\circ$.
  * Total primary current: $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.
  * **Unity PF:** $I_2$ in phase with $V_2$.
  * **Lagging PF:** $I_2$ lags $V_2$ by $\phi_2$.
  * **Leading PF:** $I_2$ leads $V_2$ by $\phi_2$.

* **Reference in Theraja (Vol. II):** pp. 1122–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 21–25

---

### 16. Page 17, Q.2(b): Draw the on-load phasor diagram of a practical transformer with capacitive load. [Figure Involved]

* **Key Characteristics of Capacitive (Leading PF) Phasor Diagram:**
  1. Secondary current $I_2$ leads terminal voltage $V_2$ by phase angle $\phi_2$.
  2. Impedance drops on secondary: $\vec{E_2} = \vec{V_2} + \vec{I_2} R_2 + j \vec{I_2} X_2$. Due to leading current, terminal voltage $V_2$ may exceed induced EMF $E_2$ (negative voltage regulation).
  3. Reflected load current $\vec{I_2'} = -K \vec{I_2}$ added vectorially to no-load current $\vec{I_0}$ yields primary current $\vec{I_1}$.
  4. Primary supply voltage: $\vec{V_1} = -\vec{E_1} + \vec{I_1} R_1 + j \vec{I_1} X_1$.

* **Reference in Theraja (Vol. II):** pp. 1125–1126
* **Reference in Chapman (5th Ed.):** pp. 84–86
* **Reference in Slide PDF:** Slide 25

---

### 17. Page 18, Q.1(c): Draw the possible vector diagrams of a transformer for different types of load. [Figure Involved]

* **1. Resistive Load ($\cos\phi_2 = 1.0$):** $I_2$ aligned with $V_2$; voltage drop primarily resistive.
* **2. Inductive Load ($\cos\phi_2\text{ lagging}$):** $I_2$ lags $V_2$; reactive drop causes notable voltage drop ($V_2 < E_2$).
* **3. Capacitive Load ($\cos\phi_2\text{ leading}$):** $I_2$ leads $V_2$; reactive drop partially cancels resistive drop, causing voltage rise ($V_2 > E_2$).

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–25

---

### 18. Page 23, Q.8: Sketch the phasor diagram of an ideal transformer with no-load conditions. [Figure Involved]
![[Pasted image 20261023181304.png]]
![[Pasted image 20260908234257.png]]

* **Ideal No-Load Features:**
  * Zero winding resistance ($R_1 = R_2 = 0$) and zero leakage flux ($X_1 = X_2 = 0$).
  * Zero core loss ($I_w = 0$).
  * No-load current $I_0 = I_m$ purely magnetizing, lagging applied voltage $V_1$ by exactly $90^\circ$ and in phase with core flux $\Phi$.
  * Induced EMFs $E_1, E_2$ lag flux $\Phi$ by $90^\circ$ ($180^\circ$ out of phase with $V_1$).

* **Reference in Theraja (Vol. II):** pp. 1120–1121
* **Reference in Chapman (5th Ed.):** pp. 76–78
* **Reference in Slide PDF:** Slides 18–19

---

### 19. Page 23, Q.13: Describe a practical transformer on no-load with net phasor diagram. [Figure Involved]

* **Behavior on No-Load:**
  * Primary draws small no-load current $I_0$ at angle $\phi_0$ ($70^\circ\text{--}75^\circ$ lagging $V_1$).
  * $I_0$ splits into two components:
    1. **Magnetizing Component ($I_m = I_0 \sin\phi_0$):** In phase with flux $\Phi$; creates core magnetic field.
    2. **Active / Core-Loss Component ($I_w = I_0 \cos\phi_0$):** In phase with $V_1$; supplies hysteresis and eddy current power losses:
       $$P_0 = V_1 I_0 \cos\phi_0$$
* **Phasor Summary:** $\vec{I_0} = \vec{I_w} + \vec{I_m}$, with $\vec{E_1}$ and $\vec{E_2}$ lagging $\Phi$ by $90^\circ$.

* **Reference in Theraja (Vol. II):** pp. 1121–1122
* **Reference in Chapman (5th Ed.):** pp. 78–80
* **Reference in Slide PDF:** Slides 19–20

---

### 20. Page 23, Q.14: Describe a practical transformer on load with no winding resistance and leakage flux. Also draw the phasor diagrams with resistive load, inductive load and capacitive load on those conditions. [Figure Involved]
![[Pasted image 20260908231027.png]]
* **Condition:** Ideal windings ($R_1=R_2=0$, $X_1=X_2=0$), but practical core ($I_0 \neq 0$).
* **Equations:** $V_1 = -E_1$, $V_2 = E_2$, $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.
* **Load Phasor Responses:**
  * **Unity PF:** $I_2$ in phase with $E_2$; reflected current $I_2'$ directly opposes $E_2$ (in phase with $V_1$).
  * **Lagging PF:** $I_2$ lags $E_2$; $I_2'$ lags $V_1$.
  * **Leading PF:** $I_2$ leads $E_2$; $I_2'$ leads $V_1$.

* **Reference in Theraja (Vol. II):** pp. 1123–1124
* **Reference in Chapman (5th Ed.):** pp. 81–83
* **Reference in Slide PDF:** Slides 21–22

---

### 21. Page 23, Q.15: Describe a practical transformer on load with winding resistance and leakage flux. Also draw the phasor diagrams with resistive load, inductive load and capacitive load on those conditions. [Figure Involved]

* **Real Transformer Equations:**
  $$\vec{V_1} = -\vec{E_1} + \vec{I_1} R_1 + j \vec{I_1} X_1$$
  $$\vec{V_2} = \vec{E_2} - \vec{I_2} R_2 - j \vec{I_2} X_2$$
  $$\vec{I_1} = \vec{I_0} + \vec{I_2'}$$
* **Phasor Construction Steps:**
  1. Draw reference flux vector $\vec{\Phi}$.
  2. Draw $\vec{E_1}, \vec{E_2}$ lagging $\vec{\Phi}$ by $90^\circ$; draw $-\vec{E_1}$ opposite to $\vec{E_1}$.
  3. Set $\vec{V_2}$ and plot $\vec{I_2}$ based on load power factor angle $\phi_2$.
  4. Add $\vec{I_2} R_2$ (**parallel to** $\vec{I_2}$) and $j \vec{I_2} X_2$ ($90^\circ$ leading $\vec{I_2}$) to $\vec{V_2}$ to obtain $\vec{E_2}$.
  5. Reflect $\vec{I_2}$ to primary as $\vec{I_2'}$; add $\vec{I_0}$ to get $\vec{I_1}$.
  6. Add $\vec{I_1} R_1$ and $j \vec{I_1} X_1$ to $-\vec{E_1}$ to obtain primary supply voltage $\vec{V_1}$.

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–26

---

### 22. Page 28, Q.No.1: Draw the vector diagram of a loaded transformer with resistance and magnetic leakage, assuming lagging p.f. [Figure Involved]

* **Lagging PF Construction:**
  * Secondary current $\vec{I_2}$ lags $\vec{V_2}$ by $\phi_2$.
  * Secondary EMF: $\vec{E_2} = \vec{V_2} + \vec{I_2}(R_2 + j X_2)$.
  * Primary current: $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.
  * Primary applied voltage: $\vec{V_1} = -\vec{E_1} + \vec{I_1}(R_1 + j X_1)$.

* **Reference in Theraja (Vol. II):** pp. 1124–1125
* **Reference in Chapman (5th Ed.):** pp. 83–85
* **Reference in Slide PDF:** Slides 23–24

---

### 23. Page 36, Q.2(a): Draw the full load phasor diagram and explain why an increase in load current causes an increase in primary current in a transformer. [Figure Involved]

* **Why Primary Current Increases with Load:**
  1. In an unloaded transformer, core flux is established by no-load current $I_0$.
  2. When load is added, secondary current $I_2$ flows, setting up a demagnetizing MMF ($N_2 I_2$) that opposes the main mutual flux $\Phi$.
  3. This momentarily weakens the core flux, causing primary counter-EMF $E_1$ to decrease slightly.
  4. The momentary difference $(V_1 - E_1)$ drives an additional load-compensating current $I_2'$ through the primary winding such that:
     $$N_1 I_2' = N_2 I_2 \implies I_2' = \left(\frac{N_2}{N_1}\right) I_2$$
  5. This restored MMF perfectly balances the demagnetizing secondary MMF, keeping core flux practically constant:
     $$\vec{I_1} = \vec{I_0} + \vec{I_2'}$$

* **Reference in Theraja (Vol. II):** pp. 1123–1124
* **Reference in Chapman (5th Ed.):** pp. 81–83
* **Reference in Slide PDF:** Slides 21–23

---

### **3. Actual transformer - equivalent circuit**
*(Reference Ranges: **Theraja Vol. II:** pp. 1126–1132 | **Chapman 5th Ed.:** pp. 86–95 | **Slides:** Slides 27–38)*

### 25. Page 7, Q.2(a): Prove that R02 = R2 + k^2 R1, where the symbols have their usual meaning.

**Proof:**
1. Let primary winding resistance be $R_1$. Power loss in $R_1$ is $I_1^2 R_1$.
2. When transferred to secondary, let equivalent resistance be $R_1'$. To preserve total copper loss:
   $$I_2^2 R_1' = I_1^2 R_1 \implies R_1' = R_1 \left(\frac{I_1}{I_2}\right)^2$$
3. Since transformation ratio $K = \frac{I_1}{I_2} = \frac{N_2}{N_1}$:
   $$R_1' = K^2 R_1$$
4. Total equivalent resistance referred to secondary ($R_{02}$):
   $$\mathbf{R_{02} = R_2 + R_1' = R_2 + K^2 R_1}$$

* **Reference in Theraja (Vol. II):** pp. 1126–1127
* **Reference in Chapman (5th Ed.):** pp. 88–90
* **Reference in Slide PDF:** Slides 28–30

---

### 26. Page 9, Q.2(c): Draw the approximate equivalent circuit of a loaded transformer referred to primary. [Figure Involved]

```
(+) V1 ----[ R01 ]----[ X01 ]----+----------------------- (+) V2' = V2/K
                                 |                      
                              [ Load' ] (ZL' = ZL / K^2)
                                 |                      
(-) -----------------------------+----------------------- (-)
Where: R01 = R1 + R2/K^2,  X01 = X1 + X2/K^2
```
* Core exciting branch ($R_c \parallel X_m$) is shifted directly across input terminals $V_1$ or omitted for load calculations, introducing negligible error while simplifying analysis.

* **Reference in Theraja (Vol. II):** pp. 1128–1130
* **Reference in Chapman (5th Ed.):** pp. 91–93
* **Reference in Slide PDF:** Slides 32–34

---

### 27. Page 17, Q.3(a): Construct the simplified equivalent circuit diagram of a 1-φ transformer. [Figure Involved]

* The simplified circuit lumps series primary and reflected secondary impedances:
  * Equivalent resistance: $R_{01} = R_1 + R_2' = R_1 + R_2 / K^2$
  * Equivalent leakage reactance: $X_{01} = X_1 + X_2' = X_1 + X_2 / K^2$
  * Shunt magnetizing branch ($R_0, X_0$) placed at the input terminals.

* **Reference in Theraja (Vol. II):** pp. 1128–1130
* **Reference in Chapman (5th Ed.):** pp. 91–93
* **Reference in Slide PDF:** Slides 32–34

---

### 28. Page 17, Q.3(b): Show that R01 = R1 + R2/k^2 and R02 = R2 + K^2R1 where the symbols have their usual meanings.

**Proof:**
* Let transformation ratio $K = \frac{N_2}{N_1} = \frac{I_1}{I_2}$.
* **1. Referred to Primary ($R_{01}$):**
  * Equating secondary copper loss to equivalent primary loss:
    $$I_1^2 R_2' = I_2^2 R_2 \implies R_2' = R_2 \left(\frac{I_2}{I_1}\right)^2 = \frac{R_2}{K^2}$$
    $$\mathbf{R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}}$$
* **2. Referred to Secondary ($R_{02}$):**
  * Equating primary copper loss to equivalent secondary loss:
    $$I_2^2 R_1' = I_1^2 R_1 \implies R_1' = R_1 \left(\frac{I_1}{I_2}\right)^2 = K^2 R_1$$
    $$\mathbf{R_{02} = R_2 + R_1' = R_2 + K^2 R_1}$$

* **Reference in Theraja (Vol. II):** pp. 1126–1128
* **Reference in Chapman (5th Ed.):** pp. 88–91
* **Reference in Slide PDF:** Slides 28–31

---

### 29. Page 17, Q.2(a) (lower half): Explain why an increase in secondary current causes an increase in primary current in a transformer.

1. When secondary current $I_2$ increases, secondary MMF ($N_2 I_2$) exerts an opposing demagnetizing effect on the core mutual flux $\Phi$.
2. Reduction in core flux momentarily reduces primary counter-EMF $E_1$.
3. The increased net potential $(V_1 - E_1)$ drives extra current $I_2'$ from the supply mains until $N_1 I_2' = N_2 I_2$.
4. This restores core flux to its original steady-state value, raising total primary current: $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.

* **Reference in Theraja (Vol. II):** pp. 1123–1124
* **Reference in Chapman (5th Ed.):** pp. 81–83
* **Reference in Slide PDF:** Slides 21–23

---

### 30. Page 23, Q.16: What is impedance ratio? How impedances in a transformer can be shifted with referred to primary or with referred to secondary?

* **Impedance Ratio:** Ratio of equivalent impedance referred to primary to impedance referred to secondary:
  $$\frac{Z_{01}}{Z_{02}} = \left(\frac{N_1}{N_2}\right)^2 = \frac{1}{K^2} = a^2$$
* **Shifting Rules:**
  * **Secondary to Primary:** Divide by $K^2$ (or multiply by $a^2$):
    $$R_2' = \frac{R_2}{K^2}, \quad X_2' = \frac{X_2}{K^2}, \quad Z_2' = \frac{Z_2}{K^2}$$
  * **Primary to Secondary:** Multiply by $K^2$ (or divide by $a^2$):
    $$R_1' = K^2 R_1, \quad X_1' = K^2 X_1, \quad Z_1' = K^2 Z_1$$

* **Reference in Theraja (Vol. II):** pp. 1127–1128
* **Reference in Chapman (5th Ed.):** pp. 88–90
* **Reference in Slide PDF:** Slides 29–31

---

### 31. Page 23, Q.17: What is the importance of shifting impedances?

1. **Eliminates Magnetic Coupling:** Replaces two magnetically coupled circuits separated by an insulating barrier with a single, continuous electrical circuit.
2. **Simplifies Analysis:** Standard Ohm's and Kirchhoff's laws can be directly applied to calculate overall voltage drops, regulation, and efficiency.
3. **Facilitates Multi-Machine System Modeling:** Essential for modeling interconnected power networks and per-unit calculations.

* **Reference in Theraja (Vol. II):** p. 1128
* **Reference in Chapman (5th Ed.):** pp. 88–89
* **Reference in Slide PDF:** Slide 31

---

### 32. Page 23, Q.18: Draw the exact equivalent circuit of a loaded transformer, where the symbols have their usual meanings. [Figure Involved]

```
     Primary Winding                     Secondary Winding
(+) V1 ---[ R1 ]---[ X1 ]---+--------+     +---[ R2 ]---[ X2 ]--- (+) V2
                            |        |     |
                          [ R0 ]   [ X0 ] (E1:E2 = N1:N2)       [ ZL ]
                            |        |     |
(-) ------------------------+--------+     +--------------------- (-)
Where: R0 = Core loss resistance, X0 = Magnetizing reactance
```

* **Reference in Theraja (Vol. II):** pp. 1128–1129
* **Reference in Chapman (5th Ed.):** pp. 86–88
* **Reference in Slide PDF:** Slides 27–28

---

### 33. Page 23, Q.19: Simplify the equivalent circuit of a loaded transformer (i) referred to primary (ii) referred to secondary, with suitable equations and net diagram. [Figure Involved]

* **(i) Referred to Primary:**
  * Shift all secondary components to primary:
    $$R_{01} = R_1 + \frac{R_2}{K^2}, \quad X_{01} = X_1 + \frac{X_2}{K^2}, \quad Z_{01} = R_{01} + j X_{01}$$
    $$V_2' = \frac{V_2}{K}, \quad I_2' = K I_2, \quad Z_L' = \frac{Z_L}{K^2}$$
* **(ii) Referred to Secondary:**
  * Shift all primary components to secondary:
    $$R_{02} = R_2 + K^2 R_1, \quad X_{02} = X_2 + K^2 X_1, \quad Z_{02} = R_{02} + j X_{02}$$
    $$V_1' = K V_1, \quad I_1' = \frac{I_1}{K}, \quad R_0' = K^2 R_0, \quad X_0' = K^2 X_0$$

* **Reference in Theraja (Vol. II):** pp. 1129–1131
* **Reference in Chapman (5th Ed.):** pp. 90–93
* **Reference in Slide PDF:** Slides 32–35

---

### 34. Page 23, Q.20: Draw the approximate equivalent circuit of a loaded transformer (i) referred to primary (ii) referred to secondary. [Figure Involved]

* Approximate model relocates the shunt exciting branch ($R_0 \parallel X_0$) across the input terminals, combining winding impedances into a single series branch ($R_{01} + jX_{01}$ or $R_{02} + jX_{02}$).

* **Reference in Theraja (Vol. II):** pp. 1129–1130
* **Reference in Chapman (5th Ed.):** pp. 91–93
* **Reference in Slide PDF:** Slides 32–34

---

### 35. Page 26, CT-04 Q.1: Define-(i) leakage reactance, (ii) magnetizing current, (iii) leakage flux, (iv) mutual flux, (v) core loss current.

1. **Leakage Flux ($\Phi_l$):** Flux that links only one winding without passing through the other; closes path through air.
2. **Leakage Reactance ($X = 2\pi f L_l$):** Fictitious inductive reactance representing the self-induced voltage drop caused by leakage flux.
3. **Mutual Flux ($\Phi_m$):** Common magnetic flux confined within the iron core that links both primary and secondary windings.
4. **Magnetizing Current ($I_m$):** Reactive component of no-load current ($I_0 \sin\phi_0$) required to establish mutual flux in the core.
5. **Core Loss Current ($I_w$ or $I_c$):** Active in-phase component of no-load current ($I_0 \cos\phi_0$) that supplies core iron losses (hysteresis + eddy current).

* **Reference in Theraja (Vol. II):** pp. 1121, 1126
* **Reference in Chapman (5th Ed.):** pp. 76–78, 86–88
* **Reference in Slide PDF:** Slides 18–20, 27–29

---

### 36. Page 32, Q.1(b): Briefly describe the effect of variation of load on core flux and primary current of a transformer.

* **Core Flux Remains Virtually Constant:** Core flux is governed by primary induced EMF: $\Phi_m \approx \frac{V_1}{4.44 f N_1}$. Since supply voltage $V_1$ and frequency $f$ are constant, core flux drops by less than 1–3% from no-load to full-load.
* **Primary Current Scales Proportionally with Load:** When secondary load current $I_2$ increases, its demagnetizing MMF ($N_2 I_2$) draws an equal and opposite counteracting current ($I_2' = \frac{N_2}{N_1} I_2$) from the supply, increasing primary current: $\vec{I_1} = \vec{I_0} + \vec{I_2'}$.

* **Reference in Theraja (Vol. II):** pp. 1123–1124
* **Reference in Chapman (5th Ed.):** pp. 81–83
* **Reference in Slide PDF:** Slides 21–23

---

### 37. Page 41, Q.3(a): Why is current increase in primary with the load increase in secondary? Explain.

* Secondary load current $I_2$ produces secondary MMF $N_2 I_2$ that opposes core mutual flux $\Phi$.
* This momentary flux reduction lowers primary back-EMF $E_1$, widening $(V_1 - E_1)$.
* The excess voltage drives additional load current $I_2'$ through the primary winding such that $N_1 I_2' = N_2 I_2$, maintaining constant core flux and satisfying energy conservation ($V_1 I_1 \cos\phi_1 \approx V_2 I_2 \cos\phi_2$).

* **Reference in Theraja (Vol. II):** pp. 1123–1124
* **Reference in Chapman (5th Ed.):** pp. 81–83
* **Reference in Slide PDF:** Slides 21–23

---

### **4. Regulation**
*(Reference Ranges: **Theraja Vol. II:** pp. 1132–1136 | **Chapman 5th Ed.:** pp. 101–105 | **Slides:** Slides 39–44)*

### 39. Page 9, Q.1(d): Calculate the percentage of voltage regulation of a transformer in which the percentage resistance drop is 1% and percentage reactance drop is 5% when p.f. is (i) 0.8 lagging (ii) unity and (iii) 0.8 leading.

**Given Data:**
* Percentage resistance drop: $v_r = 1\%$
* Percentage reactance drop: $v_x = 5\%$

**Formula:**
$$\% \text{VR} = v_r \cos\phi \pm v_x \sin\phi \quad \text{(}+\text{ for lagging, }-\text{ for leading)}$$

**(i) At 0.8 Lagging Power Factor ($\cos\phi = 0.8, \sin\phi = 0.6$):**
$$\% \text{VR} = (1 \times 0.8) + (5 \times 0.6) = 0.8 + 3.0 = \mathbf{+3.8\%}$$

**(ii) At Unity Power Factor ($\cos\phi = 1.0, \sin\phi = 0$):**
$$\% \text{VR} = (1 \times 1.0) + (5 \times 0) = \mathbf{+1.0\%}$$

**(iii) At 0.8 Leading Power Factor ($\cos\phi = 0.8, \sin\phi = 0.6$):**
$$\% \text{VR} = (1 \times 0.8) - (5 \times 0.6) = 0.8 - 3.0 = \mathbf{-2.2\%}$$

* **Reference in Theraja (Vol. II):** pp. 1134–1135
* **Reference in Chapman (5th Ed.):** pp. 103–105
* **Reference in Slide PDF:** Slides 41–43

---

### 40. Page 19, Q.2(d): Define voltage regulation. Is it possible to have negative voltage regulation of a transformer?

![[Pasted image 20260909024726.png]]
![[Pasted image 20260909024750.png]]

* **Definition:** The fractional or percentage change in secondary terminal voltage from no-load to full-load, expressed as a fraction of full-load (or no-load) voltage:
  $$\% \text{VR} = \frac{V_{\text{NL}} - V_{\text{FL}}}{V_{\text{FL}}} \times 100\% = \frac{{}_0V_2 - V_2}{V_2} \times 100\%$$
* **Is Negative Voltage Regulation Possible?**
  * **Yes, under capacitive (leading PF) loads.**
  * For leading loads: $\% \text{VR} \propto (I_2 R_{02} \cos\phi_2 - I_2 X_{02} \sin\phi_2)$.
  * When $I_2 X_{02} \sin\phi_2 > I_2 R_{02} \cos\phi_2$, the voltage drop becomes negative, meaning full-load terminal voltage exceeds no-load voltage ($V_2 > {}_0V_2$).

* **Reference in Theraja (Vol. II):** pp. 1132–1134
* **Reference in Chapman (5th Ed.):** pp. 101–103
* **Reference in Slide PDF:** Slides 39–42

---

### 41. Page 23, Q.21: Find the approximate voltage drop in a transformer with net phasor diagram. [Figure Involved]

![[Pasted image 20260909021932.png]]

**Derivation:**
* From secondary phasor diagram for a lagging load ($I_2$ lags $V_2$ by $\phi_2$):
  $${}_0V_2 = \sqrt{(V_2 \cos\phi_2 + I_2 R_{02})^2 + (V_2 \sin\phi_2 + I_2 X_{02})^2}$$
* Expanding and neglecting small second-order terms:
  $${}_0V_2 - V_2 \approx I_2 R_{02} \cos\phi_2 + I_2 X_{02} \sin\phi_2$$
* General expression for any power factor:
  $$\mathbf{\text{Approximate Voltage Drop} = I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2}$$
  *(Use $+$ for lagging PF, $-$ for leading PF).*

* **Reference in Theraja (Vol. II):** pp. 1133–1134
* **Reference in Chapman (5th Ed.):** pp. 102–104
* **Reference in Slide PDF:** Slides 40–42

---

### 42. Page 23, Q.22: Define voltage regulation of a transformer?

* **Definition:** The change in secondary terminal voltage when rated full-load at a specified power factor is removed, while keeping primary input voltage and frequency constant:
  $$\% \text{VR} = \frac{{}_0V_2 - V_2}{V_2} \times 100\%$$
* **Significance:** Measures the transformer's ability to maintain a steady terminal voltage across changing consumer load levels (lower $\% \text{VR}$ is superior).

* **Reference in Theraja (Vol. II):** p. 1132
* **Reference in Chapman (5th Ed.):** pp. 101–102
* **Reference in Slide PDF:** Slides 39–40

---

### 43. Page 27, CT-04 Q.2: Calculate voltage regulation at (i) unity pf, (ii) 0.8 leading pf, (iii) 0.7 lagging pf. If the transformer is operated as step-down one, giving rated voltage at full load, unity power factor, what is the secondary open-circuit voltage when the load is removed?

**Given Parameters:**
* $v_r = 1.0\%$, $v_x = 5.0\%$

#### Part 1: Voltage Regulation Calculations
* Formula: $\% \text{VR} = v_r \cos\phi \pm v_x \sin\phi$
* **(i) Unity PF ($\cos\phi = 1.0, \sin\phi = 0$):**
  $$\% \text{VR} = (1.0 \times 1.0) + (5.0 \times 0) = \mathbf{+1.0\%}$$
* **(ii) 0.8 Leading PF ($\cos\phi = 0.8, \sin\phi = 0.6$):**
  $$\% \text{VR} = (1.0 \times 0.8) - (5.0 \times 0.6) = 0.8 - 3.0 = \mathbf{-2.2\%}$$
* **(iii) 0.7 Lagging PF ($\cos\phi = 0.7, \sin\phi = \sqrt{1 - 0.49} \approx 0.7141$):**
  $$\% \text{VR} = (1.0 \times 0.7) + (5.0 \times 0.7141) = 0.7 + 3.5705 = \mathbf{+4.27\%}$$

#### Part 2: Secondary Open-Circuit Voltage on Removal of Load
* At unity power factor, $\% \text{VR} = 1.0\%$:
  $$\frac{{}_0V_2 - V_2}{V_2} = 0.01 \implies {}_0V_2 = V_2(1 + 0.01) = \mathbf{1.01 V_2}$$
* **Conclusion:** The secondary open-circuit voltage will be **$1.01 \text{ times}$ the rated full-load voltage ($101\% \text{ of } V_2$)**.

* **Reference in Theraja (Vol. II):** pp. 1133–1135
* **Reference in Chapman (5th Ed.):** pp. 102–104
* **Reference in Slide PDF:** Slides 40–42

---

### 44. Page 33, Q.2(c): Discuss the effect of change in frequency on transformer’s (i) core loss, (ii) Cu loss, and (iii) voltage regulation.

1. **Core Loss:**
   * Hysteresis loss: $P_h \propto f B_m^{1.6} \propto f \left(\frac{V}{f}\right)^{1.6} \propto f^{-0.6}$. Increases if frequency decreases; decreases if frequency increases.
   * Eddy current loss: $P_e \propto f^2 B_m^2 \propto f^2 \left(\frac{V}{f}\right)^2 \propto V^2$ (independent of frequency if voltage is constant).
   * *Net Core Loss:* Increases when frequency decreases; decreases when frequency increases.
2. **Copper Loss ($I^2 R$):**
   * Practically independent of frequency (increases negligibly at higher frequencies due to skin and proximity effects).
3. **Voltage Regulation:**
   * Leakage reactance is proportional to frequency ($X = 2\pi f L$).
   * Higher frequency increases reactance drop, worsening voltage regulation (higher $\% \text{VR}$).
   * Lower frequency reduces reactance drop, improving voltage regulation.

* **Reference in Theraja (Vol. II):** pp. 1119–1120, 1134–1136
* **Reference in Chapman (5th Ed.):** pp. 75–76, 103–105
* **Reference in Slide PDF:** Slides 14–17, 41–44

---

### 45. Page 41, Q.4(a): What is meant by regulation of a transformer? Which transformer is better when regulation of one transformer is 0.04% and another is 0.05% and why?

* **Definition:** Percentage drop in secondary terminal voltage from no-load to full-load relative to rated voltage.
* **Comparison:**
  * **The transformer with 0.04% regulation is superior.**
* **Why:**
  * Smaller regulation indicates that secondary voltage fluctuates less across varying load levels.
  * It delivers a more constant, reliable voltage to connected consumer appliances, minimizing equipment strain and eliminating the need for bulky voltage stabilization hardware.

* **Reference in Theraja (Vol. II):** p. 1132
* **Reference in Chapman (5th Ed.):** pp. 101–102
* **Reference in Slide PDF:** Slides 39–40

---

### **5. Short circuit and open circuit tests (Transformer-tests)**
*(Reference Ranges: **Theraja Vol. II:** pp. 1136–1145 | **Chapman 5th Ed.:** pp. 91–101 | **Slides:** Slides 35–38, 45–54)*

### ✅️47. Page 7, Q.1(c): A 10 kVA, 1-φ, 50 Hz 400/200 V transformer gave the following test results: O.C. Test (LV side) 200 V 3.0 A 200 W. S.C. Test (HV side) 15 V 30 A 300 W. Calculate efficiency and regulation at full load, 0.8 p.f lagging.

**Given Data:**
* Rating = 10 kVA, $V_1 = 400\text{ V}$ (HV), $V_2 = 200\text{ V}$ (LV), $f = 50\text{ Hz}$
* OC Test (LV): $V_0 = 200\text{ V}, I_0 = 3.0\text{ A}, W_0 = 200\text{ W} \implies P_i = 200\text{ W}$
* SC Test (HV): $V_{sc} = 15\text{ V}, I_{sc} = 30\text{ A}, W_{sc} = 300\text{ W}$
* Load: Full load, $\cos\phi = 0.8\text{ lagging}$ ($\sin\phi = 0.6$)

**Step 1: Rated Currents & Parameter Scaling**
* Rated HV current:
  $$I_{1\text{(FL)}} = \frac{10,000}{400} = 25\text{ A}$$
* Equivalent resistance on HV side:
  $$R_{01} = \frac{W_{sc}}{I_{sc}^2} = \frac{300}{(30)^2} = \frac{1}{3} \approx 0.3333\ \Omega$$
* Full-load Copper Loss:
  $$P_{cu\text{(FL)}} = I_{1\text{(FL)}}^2 R_{01} = (25)^2 \times \frac{1}{3} = \frac{625}{3} \approx 208.33\text{ W}$$

**Step 2: Full-Load Efficiency ($\eta$) at 0.8 p.f. Lagging**
* Output Power: $P_{\text{out}} = 10 \times 0.8 = 8\text{ kW} = 8,000\text{ W}$
* Total Losses: $P_{\text{loss}} = P_i + P_{cu\text{(FL)}} = 200 + 208.33 = 408.33\text{ W}$
* Input Power: $P_{\text{in}} = 8000 + 408.33 = 8408.33\text{ W}$
$$\eta = \left(\frac{8000}{8408.33}\right) \times 100\% = \mathbf{95.14\%}$$

**Step 3: Full-Load Voltage Regulation at 0.8 p.f. Lagging**
* Equivalent impedance (HV): $Z_{01} = \frac{V_{sc}}{I_{sc}} = \frac{15}{30} = 0.5\ \Omega$
* Equivalent reactance (HV): $X_{01} = \sqrt{(0.5)^2 - (0.3333)^2} = \sqrt{0.25 - 0.1111} \approx 0.3727\ \Omega$
* Voltage drop:
  $$\Delta V_1 = I_{1\text{(FL)}} (R_{01} \cos\phi + X_{01} \sin\phi) = 25 \times (0.3333 \times 0.8 + 0.3727 \times 0.6) = 25 \times 0.4903 = 12.26\text{ V}$$
* Voltage Regulation:
  $$\% \text{VR} = \left(\frac{12.26}{400}\right) \times 100\% = \mathbf{3.07\%}$$
- **Impedances Referred to Secondary ($R_{02}, X_{02}$):** Moving from HV to LV means multiplying by $K^2 = 0.25$ (or dividing by $4$):
    
    - $R_{02} = R_{01} \times K^2 = 0.3333 \times 0.25 \approx 0.08333\ \Omega$
        
    - $X_{02} = X_{01} \times K^2 = 0.3727 \times 0.25 \approx 0.09318\ \Omega$
        
- **Secondary Voltage Drop ($\Delta V_2$):**
    
    $$\Delta V_2 = I_{2\text{(FL)}} (R_{02} \cos\phi + X_{02} \sin\phi) = 50 \times (0.08333 \times 0.8 + 0.09318 \times 0.6)$$
    
    $$\Delta V_2 = 50 \times (0.06666 + 0.05591) = 50 \times 0.12257 = \mathbf{6.13\text{ V}}$$
    
- **Percentage Voltage Regulation ($\%\text{VR}$) on Secondary Side:**
    
    $$\%\text{VR} = \left(\frac{\Delta V_2}{V_2}\right) \times 100\% = \left(\frac{6.13}{200}\right) \times 100\% = \mathbf{3.07\%}$$
    

#### 2. Algebraic Proof: Why Referring to Secondary is Not Required

- **Primary vs. Secondary Relations:** By definition of transformer referral:
    
    $$I_2 = \frac{I_1}{K}, \quad R_{02} = K^2 R_{01}, \quad X_{02} = K^2 X_{01}, \quad V_2 = K V_1$$
    
- **Substituting into Secondary Regulation Formula:**
    
    $$\%\text{VR} = \frac{I_2 (R_{02} \cos\phi + X_{02} \sin\phi)}{V_2} \times 100\%$$
    
    $$\%\text{VR} = \frac{\left(\frac{I_1}{K}\right) (K^2 R_{01} \cos\phi + K^2 X_{01} \sin\phi)}{K V_1} \times 100\%$$

* **Reference in Theraja (Vol. II):** pp. 1138–1142
* **Reference in Chapman (5th Ed.):** pp. 91–94
* **Reference in Slide PDF:** Slides 35–37

---

### 48. Page 7, Q.1(d): Why is generally low voltage side shorted for short-circuit test of a transformer?

1. **Safety & Current Capability:** Shorting the LV winding means the instruments and variable supply are connected to the **HV side**. The HV rated current is significantly smaller ($I_{\text{HV}} = I_{\text{LV}} / K$), allowing standard laboratory variacs, ammeters, and wattmeters to safely handle the test current.
2. **Better Voltage Measurement Resolution:** Circulating rated current requires only 5–10% of rated voltage. On the HV side, this yields a convenient measurable voltage (e.g., 20–50 V), whereas on the LV side it would be dangerously small (1–5 V), causing large instrument percentage errors.

* **Reference in Theraja (Vol. II):** pp. 1138–1139
* **Reference in Chapman (5th Ed.):** pp. 94–95
* **Reference in Slide PDF:** Slide 37

---

### 49. Page 17, Q.2(a) (upper half): Why the open-circuit test of transformer gives core loss, while the short-circuit test of a transformer gives copper loss?

* **Open-Circuit Test $\implies$ Core Loss Only:**
  * Rated voltage is applied $\implies$ normal rated core flux ($\Phi_m \propto V_1/f$) is established $\implies$ full normal core iron loss occurs.
  * Secondary is open; primary draws only no-load current $I_0$ (2–5% of full-load current). Copper loss ($I_0^2 R_1 \propto 0.04^2 \approx 0.16\%$) is negligible. Hence wattmeter reads pure core loss.
* **Short-Circuit Test $\implies$ Copper Loss Only:**
  * Secondary is shorted; full rated current circulates through both windings $\implies$ full-load copper loss ($I^2 R$) is generated.
  * To limit current to rated value, input voltage is very low ($V_{sc} \approx 5\text{--}10\% V_{\text{rated}}$). Since iron loss is proportional to voltage squared ($P_i \propto V^2$), core loss is less than $1\%$ of normal and negligible. Hence wattmeter reads pure copper loss.

* **Reference in Theraja (Vol. II):** pp. 1136–1139
* **Reference in Chapman (5th Ed.):** pp. 93–96
* **Reference in Slide PDF:** Slides 35–38

---

### 50. Page 17, Q.2(b): Describe the open-circuit test of a transformer with suitable connection diagram. Why high voltage winding is usually left open in this test? [Figure Involved]

#### Connection Diagram
```
AC Supply (Rated V) ---> [ Variac ] ---> [ Wattmeter (W) ] ---> [ Ammeter (A) ] ---> LV Winding | | HV Winding
                                              |                                            (Open Circuit)
                                         [ Voltmeter (V) ]
```

* **Procedure:**
  * Apply rated voltage at rated frequency to the **LV side**; leave the **HV side open-circuited**.
  * Record Voltmeter ($V_0$), Ammeter ($I_0$), and Wattmeter ($W_0$).
  * Core loss: $P_i = W_0$.
  * Core resistance: $R_0 = \frac{V_0^2}{W_0}$.
  * Magnetizing reactance: $X_0 = \frac{V_0}{I_m}$, where $I_m = \sqrt{I_0^2 - I_w^2}$ and $I_w = \frac{W_0}{V_0}$.
* **Why HV Winding is Left Open:**
  1. Rated voltage of the LV side is safely manageable with standard supply lines.
  2. Operating on the HV side would require dangerous, high-voltage test sources and specialized high-voltage meters.

* **Reference in Theraja (Vol. II):** pp. 1136–1138
* **Reference in Chapman (5th Ed.):** pp. 93–94
* **Reference in Slide PDF:** Slides 35–36

---

### 51. Page 17, Q.2(c) (upper half): Obtain the equivalent circuit of a 10kVA, 450/120 V, 50Hz transformer from the following test data: O.C. Test: 120V, 4.2A, 80W – on L.V. side S.C. Test: 9.65V, 22.2A, 120W – on H.V. side.

**Given Data:** 10 kVA, 450/120 V, 50 Hz. Transformation ratio $K = \frac{120}{450} = \frac{4}{15} \approx 0.2667$.

**Step 1: Shunt Branch Parameters from OC Test (on LV side)**
* No-load power factor: $\cos\phi_0 = \frac{W_0}{V_0 I_0} = \frac{80}{120 \times 4.2} = \frac{80}{504} \approx 0.1587$
* Core-loss current: $I_w = I_0 \cos\phi_0 = \frac{80}{120} \approx 0.667\text{ A}$
* Magnetizing current: $I_m = \sqrt{I_0^2 - I_w^2} = \sqrt{(4.2)^2 - (0.667)^2} = \sqrt{17.64 - 0.445} \approx 4.147\text{ A}$
* Core-loss resistance (LV): $R_{0(\text{LV})} = \frac{V_0}{I_w} = \frac{120}{0.667} \approx \mathbf{180\ \Omega}$
* Magnetizing reactance (LV): $X_{0(\text{LV})} = \frac{V_0}{I_m} = \frac{120}{4.147} \approx \mathbf{28.94\ \Omega}$
* Referred to HV side:
  $$R_{0(\text{HV})} = \frac{R_{0(\text{LV})}}{K^2} = \frac{180}{(4/15)^2} = 180 \times \frac{225}{16} \approx \mathbf{2531.25\ \Omega}$$
  $$X_{0(\text{HV})} = \frac{X_{0(\text{LV})}}{K^2} = \frac{28.94}{(4/15)^2} \approx \mathbf{406.97\ \Omega}$$

**Step 2: Series Branch Parameters from SC Test (on HV side)**
* Equivalent resistance: $R_{01} = \frac{W_{sc}}{I_{sc}^2} = \frac{120}{(22.2)^2} = \frac{120}{492.84} \approx \mathbf{0.2435\ \Omega}$
* Equivalent impedance: $Z_{01} = \frac{V_{sc}}{I_{sc}} = \frac{9.65}{22.2} \approx \mathbf{0.4347\ \Omega}$
* Equivalent leakage reactance:
  $$X_{01} = \sqrt{Z_{01}^2 - R_{01}^2} = \sqrt{(0.4347)^2 - (0.2435)^2} = \sqrt{0.1890 - 0.0593} \approx \mathbf{0.3601\ \Omega}$$

* **Reference in Theraja (Vol. II):** pp. 1139–1142
* **Reference in Chapman (5th Ed.):** pp. 94–97
* **Reference in Slide PDF:** Slides 37–38

---

### 52. Page 17, Q.2(c) (lower half): What are the objectives of short circuit test? Describe the short circuit test with suitable diagram. [Figure Involved]

* **Objectives:**
  1. Determine total equivalent winding resistance ($R_{01}$ or $R_{02}$).
  2. Determine total equivalent leakage reactance ($X_{01}$ or $X_{02}$) and impedance ($Z_{01}$ or $Z_{02}$).
  3. Determine full-load copper loss ($P_{cu\text{(FL)}}$).
  4. Pre-determine voltage regulation under any load current and power factor.
* **Test Diagram & Method:**
  ```
  Variable AC Supply ---> [ W ] ---> [ A ] ---> HV Winding | | LV Winding (Solid Short)
                             |
                            [ V ]
  ```
  * Solidly short the LV terminals with a thick copper lead.
  * Apply a reduced AC voltage (5–10% rated) to the HV terminals until the ammeter reads rated HV current.
  * Record $V_{sc}, I_{sc}, W_{sc}$. Compute:
    $$R_{01} = \frac{W_{sc}}{I_{sc}^2}, \quad Z_{01} = \frac{V_{sc}}{I_{sc}}, \quad X_{01} = \sqrt{Z_{01}^2 - R_{01}^2}$$

* **Reference in Theraja (Vol. II):** pp. 1138–1140
* **Reference in Chapman (5th Ed.):** pp. 94–96
* **Reference in Slide PDF:** Slides 36–38

---

### 53. Page 17, Q.2(d): Find the equivalent winding resistance, reactance and impedance referred to the (i) high voltage side and (ii) the low voltage side. (from a 30 KVA, 2400/120 V, 50 Hz transformer).

**General Procedure & Formulas:**
* Rating: 30 kVA, $V_1 = 2400\text{ V}$ (HV), $V_2 = 120\text{ V}$ (LV)
* Transformation ratio: $K = \frac{V_2}{V_1} = \frac{120}{2400} = \frac{1}{20} = 0.05$
* **(i) Referred to High Voltage (HV) Side:**
  $$R_{01} = R_1 + \frac{R_2}{K^2} = R_1 + (20)^2 R_2 = R_1 + 400 R_2$$
  $$X_{01} = X_1 + \frac{X_2}{K^2} = X_1 + 400 X_2$$
  $$Z_{01} = \sqrt{R_{01}^2 + X_{01}^2}$$
* **(ii) Referred to Low Voltage (LV) Side:**
  $$R_{02} = R_2 + K^2 R_1 = R_2 + (0.05)^2 R_1 = R_2 + \frac{R_1}{400} = K^2 R_{01}$$
  $$X_{02} = X_2 + K^2 X_1 = X_2 + \frac{X_1}{400} = K^2 X_{01}$$
  $$Z_{02} = \sqrt{R_{02}^2 + X_{02}^2} = K^2 Z_{01}$$

* **Reference in Theraja (Vol. II):** pp. 1126–1128
* **Reference in Chapman (5th Ed.):** pp. 88–91
* **Reference in Slide PDF:** Slides 28–31

---

### 54. Page 17, Q.4(a): Why is all-day efficiency preferred rather than commercial efficiency?

* **Commercial (Power) Efficiency ($\eta$):** Measured instantaneously at a specific load and power factor:
  $$\eta = \frac{\text{Output Power (kW)}}{\text{Input Power (kW)}}$$
* **Why All-Day (Energy) Efficiency is Preferred for Distribution Transformers:**
  1. **Continuous 24/7 Core Energization:** A distribution transformer is connected to the grid 24 hours a day, so **core iron loss is constant 24 hours** regardless of loading.
  2. **Fluctuating Load Demand:** The secondary supplies domestic/commercial loads that vary dramatically (heavy load for 4–6 peak hours, light or zero load during the remaining 18–20 hours).
  3. **True Energy Accounting:** All-day efficiency computes actual energy consumed over 24 hours:
     $$\eta_{\text{all-day}} = \frac{\text{Energy Output (kWh in 24 hrs)}}{\text{Energy Input (kWh in 24 hrs)}}$$
     This is the only accurate benchmark for revenue, losses, and utility economic evaluation.

* **Reference in Theraja (Vol. II):** pp. 1144–1145
* **Reference in Chapman (5th Ed.):** pp. 98–101
* **Reference in Slide PDF:** Slides 49–51

---

### 55. Page 17, Q.4(c): Find ‘all-day’ efficiency of a transformer having maximum efficiency of 98% at 15kVA at unity p.f and loaded as follows: 12 Hrs – 2kW at 0.5 p.f lagging; 6 hrs – 12kW at 0.8 p.f lagging; 6 hrs – at no load.

**Given Data:**
* $\eta_{\max} = 98\%$ at $15\text{ kVA}$ and $\text{u.p.f.}$:
  $$\text{Total loss at max efficiency} = \frac{15 \times 10^3 \times (1 - 0.98)}{0.98} \approx 306.12\text{ W}$$
  Since iron loss equals copper loss at max efficiency:
  $$P_i = P_{cu\text{(15kVA)}} = \frac{306.12}{2} = 153.06\text{ W} = 0.15306\text{ kW}$$

**Step 1: Energy Output over 24 Hours**
* Period 1 (12 h, 2 kW): $E_1 = 12 \times 2 = 24\text{ kWh}$
* Period 2 (6 h, 12 kW): $E_2 = 6 \times 12 = 72\text{ kWh}$
* Period 3 (6 h, no load): $E_3 = 0\text{ kWh}$
* **Total Energy Output:** $E_{\text{out}} = 24 + 72 + 0 = \mathbf{96.0\text{ kWh}}$

**Step 2: 24-Hour Iron Loss Energy**
$$E_{\text{iron}} = P_i \times 24\text{ h} = 0.15306 \times 24 = \mathbf{3.673\text{ kWh}}$$

**Step 3: 24-Hour Copper Loss Energy**
* Period 1: $\text{kVA}_1 = \frac{2\text{ kW}}{0.5} = 4\text{ kVA}$. Copper loss: $P_{cu1} = \left(\frac{4}{15}\right)^2 \times 0.15306 \approx 0.01088\text{ kW}$.
  $$E_{cu1} = 12 \times 0.01088 = 0.1306\text{ kWh}$$
* Period 2: $\text{kVA}_2 = \frac{12\text{ kW}}{0.8} = 15\text{ kVA}$ (Rated full load). Copper loss: $P_{cu2} = 0.15306\text{ kW}$.
  $$E_{cu2} = 6 \times 0.15306 = 0.9184\text{ kWh}$$
* Period 3: No load $\implies E_{cu3} = 0\text{ kWh}$.
* **Total Copper Loss Energy:** $E_{cu} = 0.1306 + 0.9184 = \mathbf{1.049\text{ kWh}}$

**Step 4: All-Day Efficiency**
$$E_{\text{in}} = E_{\text{out}} + E_{\text{iron}} + E_{cu} = 96.0 + 3.673 + 1.049 = 100.722\text{ kWh}$$
$$\eta_{\text{all-day}} = \left(\frac{96.0}{100.722}\right) \times 100\% \approx \mathbf{95.31\%}$$

* **Reference in Theraja (Vol. II):** pp. 1144–1145
* **Reference in Chapman (5th Ed.):** pp. 99–101
* **Reference in Slide PDF:** Slides 50–52

---

### 56. Page 18, Q.1(a): What is a transformer? Prove that the efficiency of a transformer will be maximum when copper loss is equal to iron loss.

* **Definition:** A static electromagnetic machine that transforms alternating voltage and current between circuits at constant frequency.
* **Proof of Condition for Maximum Efficiency:**
  1. Efficiency expression at load current $I_2$:
     $$\eta = \frac{V_2 I_2 \cos\phi_2}{V_2 I_2 \cos\phi_2 + P_i + I_2^2 R_{02}}$$
  2. Divide numerator and denominator by $I_2$:
     $$\eta = \frac{V_2 \cos\phi_2}{V_2 \cos\phi_2 + \frac{P_i}{I_2} + I_2 R_{02}}$$
  3. Efficiency is maximum when the denominator is minimum. Differentiating denominator with respect to $I_2$ and setting to zero:
     $$\frac{d}{dI_2}\left(V_2 \cos\phi_2 + \frac{P_i}{I_2} + I_2 R_{02}\right) = 0$$
     $$0 - \frac{P_i}{I_2^2} + R_{02} = 0$$
     $$\frac{P_i}{I_2^2} = R_{02} \implies P_i = I_2^2 R_{02}$$
  4. Since $I_2^2 R_{02} = P_{cu}$:
     $$\mathbf{P_i = P_{cu}} \quad \text{(Iron Loss = Copper Loss)}$$

* **Reference in Theraja (Vol. II):** pp. 1142–1144
* **Reference in Chapman (5th Ed.):** pp. 96–98
* **Reference in Slide PDF:** Slides 45–48

---

### 57. Page 18, Q.1(c): A 10 kVA, 2200/220 V, 50 Hz transformer is tested on open and short circuit tests. If the following readings are obtained, determine the values of maximum power and the loads at which they occur for unity pf. Open circuit test – high side open: v = 220 V, i = 1.5 A, w = 153 W; Short circuit test – low side shorted: v = 115 V, i = rated, w = 224 W.

**Given Data:**
* Rating = 10 kVA, $\cos\phi = 1.0$
* Iron loss: $P_i = 153\text{ W}$ (from OC test at rated voltage)
* Full-load Copper loss: $P_{cu\text{(FL)}} = 224\text{ W}$ (from SC test at rated current)

**Step 1: Fraction of Full Load for Maximum Efficiency ($x$)**
$$x = \sqrt{\frac{P_i}{P_{cu\text{(FL)}}}} = \sqrt{\frac{153}{224}} \approx \sqrt{0.6830} \approx \mathbf{0.8265}$$

**Step 2: Load at Maximum Efficiency**
* Load kVA: $S_{\max} = 0.8265 \times 10\text{ kVA} = \mathbf{8.265\text{ kVA}}$
* Load Power (at unity pf): $P_{\max\text{-load}} = 8.265 \times 1.0 = \mathbf{8.265\text{ kW}}$

**Step 3: Maximum Efficiency Value**
* At this load: $P_{cu} = P_i = 153\text{ W} \implies \text{Total losses} = 153 + 153 = 306\text{ W} = 0.306\text{ kW}$
$$\eta_{\max} = \left(\frac{8.265}{8.265 + 0.306}\right) \times 100\% = \left(\frac{8.265}{8.571}\right) \times 100\% = \mathbf{96.43\%}$$

* **Reference in Theraja (Vol. II):** pp. 1143–1144
* **Reference in Chapman (5th Ed.):** pp. 97–99
* **Reference in Slide PDF:** Slides 47–49

---

### 58. Page 18, Q.3(c): Obtain the equivalent circuit of a 200/400 V, 50 Hz, 1-phase transformer from the following test data: O.C. Test: 200 V, 0.7 A, 70 W – on L.V. side S.C. Test: 15 V, 10 A, 85 W – on H.V. side Calculate the secondary voltage when delivering 5 kW at 0.8 pf. Lagging, the primary voltage being 200 V.

**Given Data:** 200/400 V, 50 Hz. $K = 400/200 = 2$.
* OC (LV side): $V_0 = 200\text{ V}, I_0 = 0.7\text{ A}, W_0 = 70\text{ W}$
* SC (HV side): $V_{sc} = 15\text{ V}, I_{sc} = 10\text{ A}, W_{sc} = 85\text{ W}$

**Step 1: Equivalent Circuit Parameters**
* **Shunt branch on LV (Primary):**
  $$R_0 = \frac{V_0^2}{W_0} = \frac{(200)^2}{70} \approx \mathbf{571.43\ \Omega}$$
  $$I_w = \frac{70}{200} = 0.35\text{ A} \implies I_m = \sqrt{(0.7)^2 - (0.35)^2} \approx 0.606\text{ A}$$
  $$X_0 = \frac{200}{0.606} \approx \mathbf{330.03\ \Omega}$$
* **Series branch on HV (Secondary):**
  $$R_{02} = \frac{W_{sc}}{I_{sc}^2} = \frac{85}{(10)^2} = \mathbf{0.85\ \Omega}$$
  $$Z_{02} = \frac{V_{sc}}{I_{sc}} = \frac{15}{10} = 1.50\ \Omega$$
  $$X_{02} = \sqrt{(1.5)^2 - (0.85)^2} = \sqrt{2.25 - 0.7225} \approx \mathbf{1.236\ \Omega}$$

**Step 2: Secondary Voltage for 5 kW at 0.8 Lagging PF**
* No-load secondary voltage: ${}_0V_2 = K V_1 = 2 \times 200 = 400\text{ V}$
* Secondary load current:
  $$I_2 \approx \frac{P_{\text{load}}}{{}_0V_2 \cos\phi} = \frac{5000}{400 \times 0.8} = 15.625\text{ A}$$
* Voltage drop on secondary:
  $$\Delta V_2 = I_2(R_{02}\cos\phi + X_{02}\sin\phi) = 15.625 \times (0.85 \times 0.8 + 1.236 \times 0.6) = 15.625 \times (0.68 + 0.7416) \approx 22.21\text{ V}$$
* Secondary Terminal Voltage:
  $$V_2 = {}_0V_2 - \Delta V_2 = 400 - 22.21 = \mathbf{377.79\text{ V}}$$

* **Reference in Theraja (Vol. II):** pp. 1139–1142
* **Reference in Chapman (5th Ed.):** pp. 91–95
* **Reference in Slide PDF:** Slides 37–38, 41–43

---

### 59. Page 19, Q.2(b): Why are iron losses constant at all loads in a transformer?

* **Governing EMF Formula:** The primary induced EMF is:
  $$E_1 = 4.44 f N_1 \Phi_m \implies \Phi_m = \frac{E_1}{4.44 f N_1}$$
* **Constant Core Flux:**
  * For a normal supply, terminal voltage $V_1$ and frequency $f$ are constant.
  * Internal primary impedance drop ($I_1 Z_1$) is very small (1–3% of $V_1$), so $E_1 \approx V_1 \approx \text{constant}$.
  * Thus, maximum core flux $\Phi_m$ remains virtually identical from no-load to full-load.
* **Iron Loss Dependence:**
  * Hysteresis loss ($P_h \propto f B_m^{1.6}$) and eddy current loss ($P_e \propto f^2 B_m^2$) depend strictly on flux density $B_m$ and frequency $f$.
  * Since $B_m$ and $f$ do not change with load current, **iron loss is constant at all loads**.

* **Reference in Theraja (Vol. II):** p. 1136
* **Reference in Chapman (5th Ed.):** pp. 96–97
* **Reference in Slide PDF:** Slide 45

---

### 60. Page 19, Q.2(c): “Transformer full load test is performed only for copper loss, while low voltage side is shorted” - why? Comment on your answer.

* **Why LV Side is Shorted:**
  * Shorting the LV winding allows the test to be performed on the HV side. The HV winding carries smaller rated current, permitting standard laboratory ammeters and supply variacs to be utilized safely.
* **Why Only Copper Loss is Measured:**
  * To circulate full rated current through shorted windings, only 5–10% of rated voltage ($V_{sc}$) is needed.
  * Because core loss varies with voltage squared ($P_i \propto V^2$), the core loss during the SC test is less than $(0.1)^2 = 1\%$ of normal, which is negligible.
  * Hence, the wattmeter reading represents **pure full-load copper loss** ($I^2 R$).

* **Reference in Theraja (Vol. II):** pp. 1138–1139
* **Reference in Chapman (5th Ed.):** pp. 94–96
* **Reference in Slide PDF:** Slides 36–38

---

### 61. Page 19, Q.2(d): The corrected instrument readings obtained from open-circuit and short circuit tests on 10 kVA, 450/120 V, 50 Hz transformer are: O.C. Test: V1 = 120V, I1 = 4.2A, W1 = 80W; S.C. Test: Vsc = 9.65V, Isc = 22.2A, Wsc = 120W; with low-voltage winding short circuited. Compute: (i) the equivalent circuit constants, (ii) the efficiency and voltage regulation for 80% lagging p.f. load.

**Given Data:** 10 kVA, 450/120 V, 50 Hz. $K = 120/450 = 4/15$.

**Part (i): Equivalent Circuit Constants (Referred to HV / Primary)**
* From SC Test (HV side, rated $I_1 = 10,000/450 = 22.22\text{ A}$):
  $$R_{01} = \frac{W_{sc}}{I_{sc}^2} = \frac{120}{(22.2)^2} \approx \mathbf{0.2435\ \Omega}$$
  $$Z_{01} = \frac{V_{sc}}{I_{sc}} = \frac{9.65}{22.2} \approx \mathbf{0.4347\ \Omega}$$
  $$X_{01} = \sqrt{(0.4347)^2 - (0.2435)^2} \approx \mathbf{0.3601\ \Omega}$$
* From OC Test (LV side, shifted to HV side):
  $$R_{0(\text{LV})} = \frac{120^2}{80} = 180\ \Omega \implies R_{0(\text{HV})} = \frac{180}{(4/15)^2} \approx \mathbf{2531.25\ \Omega}$$
  $$I_w = 80/120 = 0.667\text{ A} \implies I_m = \sqrt{4.2^2 - 0.667^2} = 4.147\text{ A}$$
  $$X_{0(\text{LV})} = \frac{120}{4.147} = 28.94\ \Omega \implies X_{0(\text{HV})} = \frac{28.94}{(4/15)^2} \approx \mathbf{406.97\ \Omega}$$

**Part (ii): Efficiency & Regulation at Full-Load 80% (0.8) Lagging PF**
* Output Power: $P_{\text{out}} = 10 \times 0.8 = 8\text{ kW} = 8,000\text{ W}$
* Total Losses: $P_{\text{loss}} = P_i + P_{cu} = 80 + 120 = 200\text{ W}$
* Efficiency:
  $$\eta = \left(\frac{8000}{8000 + 200}\right) \times 100\% = \left(\frac{8000}{8200}\right) \times 100\% \approx \mathbf{97.56\%}$$
* Full-load Voltage Drop (referred to HV):
  $$\Delta V_1 = I_1(R_{01}\cos\phi + X_{01}\sin\phi) = 22.2 \times (0.2435 \times 0.8 + 0.3601 \times 0.6) = 22.2 \times (0.1948 + 0.2161) = 9.12\text{ V}$$
* Voltage Regulation:
  $$\% \text{VR} = \left(\frac{9.12}{450}\right) \times 100\% \approx \mathbf{2.03\%}$$

* **Reference in Theraja (Vol. II):** pp. 1139–1142
* **Reference in Chapman (5th Ed.):** pp. 91–95
* **Reference in Slide PDF:** Slides 37–38, 41–44

---

### 62. Page 23, Q.23-28: (List covers objectives of tests, separation of core losses, and why HV side is left open in OC test).

1. **Objectives of OC Test:** Find core iron loss ($P_i$) and shunt branch parameters ($R_0, X_0$).
2. **Objectives of SC Test:** Find full-load copper loss ($P_{cu}$) and series impedance parameters ($R_{01}, X_{01}, Z_{01}$).
3. **Why HV Side is Open in OC Test:** Lower voltage on LV side allows safe operation using standard low-voltage lab instruments.
4. **Separation of Core Losses ($P_h$ and $P_e$):**
   * Core loss equation: $P_i = P_h + P_e = A f + B f^2 \implies \frac{P_i}{f} = A + B f$.
   * Perform tests at variable frequency while keeping flux density constant ($V/f = \text{constant}$).
   * Plot $P_i/f$ vs $f$: intercept gives hysteresis constant $A$, slope gives eddy current constant $B$.

* **Reference in Theraja (Vol. II):** pp. 1136–1142
* **Reference in Chapman (5th Ed.):** pp. 93–96
* **Reference in Slide PDF:** Slides 35–38

---

### 63. Page 24, Q.29-35: (List covers transformer rating in kVA, efficiency, output equation for max efficiency, all-day efficiency, and cooling).

1. **Why Rated in kVA, Not kW:** Iron loss depends on voltage ($V$), and copper loss depends on current ($I$), independent of load power factor ($\cos\phi$). Since manufacturer cannot predict user load pf, rating is specified in apparent power ($S = V \times I$ in kVA).
2. **Condition for Maximum Efficiency:** Copper loss equals iron loss ($P_{cu} = P_i$).
3. **Load for Maximum Efficiency:** $x = \sqrt{\frac{P_i}{P_{cu\text{(FL)}}}} \implies \text{kVA}_{\max} = \text{kVA}_{\text{rated}} \times \sqrt{\frac{P_i}{P_{cu\text{(FL)}}}}$.
4. **All-Day Efficiency:** Ratio of daily energy output (kWh) to daily energy input (kWh) over 24 hours.
5. **Transformer Cooling Methods:** ONAN (Oil Natural Air Natural), ONAF (Oil Natural Air Forced), OFAF (Oil Forced Air Forced).

* **Reference in Theraja (Vol. II):** pp. 1118, 1142–1145, 1150–1152
* **Reference in Chapman (5th Ed.):** pp. 74, 96–101
* **Reference in Slide PDF:** Slides 13, 45–54

---

### 64. Page 26, CT-04 Q.2: The following are the readings taken for the short circuit and open circuit test of a 10-kVA, 600/240V, and 50Hz transformer. SC: V = 22.5V, I = rated, W=200 W. O.C. V = 240V, I = 1.8 A, W = 65W Calculate the maximum efficiency at unity p..f load and at 0.8 lagging p.f. load.

**Given Data:**
* Rating = 10 kVA, $P_i = 65\text{ W}$, $P_{cu\text{(FL)}} = 200\text{ W}$

**Step 1: Fraction of Full Load for Max Efficiency ($x$)**
$$x = \sqrt{\frac{P_i}{P_{cu\text{(FL)}}}} = \sqrt{\frac{65}{200}} = \sqrt{0.325} \approx \mathbf{0.5701}$$
$$\text{Load kVA at } \eta_{\max} = 0.5701 \times 10\text{ kVA} = \mathbf{5.701\text{ kVA}}$$
Total losses at $\eta_{\max}$: $P_{\text{loss}} = 2 \times P_i = 2 \times 65 = 130\text{ W} = 0.13\text{ kW}$.

**Step 2: Maximum Efficiency at Unity Power Factor**
* Output Power: $P_{\text{out}} = 5.701 \times 1.0 = 5.701\text{ kW}$
$$\eta_{\max(\text{upf})} = \left(\frac{5.701}{5.701 + 0.13}\right) \times 100\% = \left(\frac{5.701}{5.831}\right) \times 100\% \approx \mathbf{97.77\%}$$

**Step 3: Maximum Efficiency at 0.8 Lagging Power Factor**
* Output Power: $P_{\text{out}} = 5.701 \times 0.8 = 4.5608\text{ kW}$
$$\eta_{\max(0.8)} = \left(\frac{4.5608}{4.5608 + 0.13}\right) \times 100\% = \left(\frac{4.5608}{4.6908}\right) \times 100\% \approx \mathbf{97.23\%}$$

* **Reference in Theraja (Vol. II):** pp. 1143–1144
* **Reference in Chapman (5th Ed.):** pp. 97–99
* **Reference in Slide PDF:** Slides 47–49

---

### 65. Page 28, Q.No.2: If P1 and P2 be the iron and copper losses of a transformer on full load, find the ratio of P1 and P2 such that maximum efficiency occurs at 75% full load.

**Derivation:**
* At fraction $x$ of full load, total copper loss is $x^2 P_2$.
* Maximum efficiency occurs when:
  $$P_1 = x^2 P_2$$
* Given $x = 75\% = 0.75 = \frac{3}{4}$:
  $$P_1 = (0.75)^2 P_2 = \frac{9}{16} P_2$$
$$\mathbf{\frac{P_1}{P_2} = \frac{9}{16} = 0.5625}$$

* **Reference in Theraja (Vol. II):** p. 1143
* **Reference in Chapman (5th Ed.):** pp. 97–98
* **Reference in Slide PDF:** Slide 47

---

### 66. Page 28, Q.No.3 (second one): A 40kVA distribution transformer has a total losses of 800W at maximum efficiency. The transformer is supplying a lighting load (unity p.f.). The load cycle is as under: Full-load for 4 hrs, half-load for 8 hrs and no-load for 12 hrs. Calculate all day efficiency.

**Given Data:**
* Rating = 40 kVA, $\cos\phi = 1.0$
* Total losses at $\eta_{\max} = 800\text{ W} \implies P_i = P_{cu} = 400\text{ W} = 0.4\text{ kW}$.
  *(Assuming max efficiency occurs at full load, $P_{cu\text{(FL)}} = 0.4\text{ kW}$).*

**Step 1: 24-Hour Energy Output**
* Full load (4 h): $40\text{ kW} \times 4\text{ h} = 160\text{ kWh}$
* Half load (8 h): $20\text{ kW} \times 8\text{ h} = 160\text{ kWh}$
* No load (12 h): $0\text{ kWh}$
* **Total Energy Output:** $E_{\text{out}} = 160 + 160 = \mathbf{320\text{ kWh}}$

**Step 2: 24-Hour Energy Losses**
* Iron Loss Energy (24 h continuous):
  $$E_{\text{iron}} = 0.4\text{ kW} \times 24\text{ h} = \mathbf{9.6\text{ kWh}}$$
* Copper Loss Energy:
  * Full load (4 h): $0.4\text{ kW} \times 4\text{ h} = 1.6\text{ kWh}$
  * Half load (8 h): $(0.5)^2 \times 0.4\text{ kW} \times 8\text{ h} = 0.1 \times 8 = 0.8\text{ kWh}$
  * No load (12 h): $0\text{ kWh}$
  * Total Cu Energy: $E_{cu} = 1.6 + 0.8 = \mathbf{2.4\text{ kWh}}$
* Total Losses: $E_{\text{loss}} = 9.6 + 2.4 = \mathbf{12.0\text{ kWh}}$

**Step 3: All-Day Efficiency**
$$\eta_{\text{all-day}} = \left(\frac{320}{320 + 12}\right) \times 100\% = \left(\frac{320}{332}\right) \times 100\% = \mathbf{96.39\%}$$

* **Reference in Theraja (Vol. II):** pp. 1144–1145
* **Reference in Chapman (5th Ed.):** pp. 99–101
* **Reference in Slide PDF:** Slides 50–52

---

### 67. Page 28, Q.No.3: A single-phase transformer with a ratio of 400/100 takes a no load current of 5A at 0.25 power factor lagging. If the secondary supplies a current of 120 A at a p.f. of 0.8 lagging, determine the current taken by the primary.

**Given Data:**
* $V_1/V_2 = 400/100 \implies K = 100/400 = 0.25$
* $I_0 = 5\text{ A}, \cos\phi_0 = 0.25 \implies \sin\phi_0 = \sqrt{1 - (0.25)^2} \approx 0.9682$
* $I_2 = 120\text{ A}, \cos\phi_2 = 0.8 \implies \sin\phi_2 = 0.6$

**Step 1: Reflected Secondary Current on Primary ($I_2'$)**
$$I_2' = K I_2 = 0.25 \times 120 = 30\text{ A}$$

**Step 2: Component Resolution**
* Horizontal (in-phase with $-V_1'$):
  $$I_{1x} = I_0 \cos\phi_0 + I_2' \cos\phi_2 = (5 \times 0.25) + (30 \times 0.8) = 1.25 + 24 = 25.25\text{ A}$$
* Vertical (lagging in quadrature):
  $$I_{1y} = I_0 \sin\phi_0 + I_2' \sin\phi_2 = (5 \times 0.9682) + (30 \times 0.6) = 4.841 + 18 = 22.841\text{ A}$$

**Step 3: Primary Current Magnitude**
$$I_1 = \sqrt{(25.25)^2 + (22.841)^2} = \sqrt{637.56 + 521.71} = \sqrt{1159.27} \approx \mathbf{34.05\text{ A}}$$

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–26

---

### 68. Page 28, Q.No.4: A 1-φ transformer with a ratio of 400/100 takes a no load current of 5A at 0.2 p.f. lagging. If the secondary supplies a current of 100A at a p.f. of 0.8 lagging, estimate the current taken by the primary.

**Given Data:**
* $K = 100/400 = 0.25$
* $I_0 = 5\text{ A}, \cos\phi_0 = 0.2 \implies \sin\phi_0 \approx 0.9798$
* $I_2 = 100\text{ A}, \cos\phi_2 = 0.8 \implies \sin\phi_2 = 0.6$

**Step 1: Reflected Secondary Current ($I_2'$)**
$$I_2' = 0.25 \times 100 = 25\text{ A}$$

**Step 2: Component Resolution**
* $I_{1x} = (5 \times 0.2) + (25 \times 0.8) = 1.0 + 20.0 = 21.0\text{ A}$
* $I_{1y} = (5 \times 0.9798) + (25 \times 0.6) = 4.899 + 15.0 = 19.899\text{ A}$

**Step 3: Primary Current Magnitude**
$$I_1 = \sqrt{(21.0)^2 + (19.899)^2} = \sqrt{441 + 395.97} = \sqrt{836.97} \approx \mathbf{28.93\text{ A}}$$

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–26

---

### 69. Page 40, Q.2(a): What are the different losses occurring in a transformer? Derive the condition for maximum efficiency in a transformer.

* **Transformer Losses:**
  1. **Core / Iron Losses ($P_i$):**
     * *Hysteresis Loss:* $P_h = k_h B_m^{1.6} f V$ (energy lost aligning magnetic domains).
     * *Eddy Current Loss:* $P_e = k_e B_m^2 f^2 t^2 V$ (circulating currents in laminated core).
  2. **Copper Losses ($P_{cu} = I_1^2 R_1 + I_2^2 R_2$):** Ohmic $I^2 R$ heat dissipated in windings.
  3. **Stray & Dielectric Losses:** Leakage flux inducing currents in tank metal and insulation leakage (very small).
* **Derivation for Maximum Efficiency:**
  * Efficiency: $\eta = \frac{V_2 I_2 \cos\phi}{V_2 I_2 \cos\phi + P_i + I_2^2 R_{02}} = \frac{V_2 \cos\phi}{V_2 \cos\phi + \frac{P_i}{I_2} + I_2 R_{02}}$.
  * Differentiating denominator w.r.t. $I_2$:
    $$\frac{d}{dI_2}\left(V_2 \cos\phi + \frac{P_i}{I_2} + I_2 R_{02}\right) = -\frac{P_i}{I_2^2} + R_{02} = 0 \implies \mathbf{P_i = I_2^2 R_{02} = P_{cu}}$$
  * Condition: Maximum efficiency occurs when **variable copper loss equals constant iron loss**.

* **Reference in Theraja (Vol. II):** pp. 1136, 1142–1144
* **Reference in Chapman (5th Ed.):** pp. 96–98
* **Reference in Slide PDF:** Slides 45–48

---

### 70. Page 40, Q.2(c): Find the all day efficiency of a 500kVA, distribution transformer whose iron loss and full load copper loss are 1.5kW and 6kW respectively. In a day it is loaded as follows: Duration(h) 6, 10, 4, 4; Output(KW) 400, 300, 100, 0; Power factor 0.80, 0.75, 0.80, #.

**Given Data:**
* Rating = 500 kVA, $P_i = 1.5\text{ kW}$, $P_{cu\text{(FL)}} = 6.0\text{ kW}$
* Total hours = $6 + 10 + 4 + 4 = 24\text{ hours}$

**Step 1: Energy Output in 24 Hours**
* Period 1 (6 h, 400 kW): $400 \times 6 = 2400\text{ kWh}$
* Period 2 (10 h, 300 kW): $300 \times 10 = 3000\text{ kWh}$
* Period 3 (4 h, 100 kW): $100 \times 4 = 400\text{ kWh}$
* Period 4 (4 h, 0 kW): $0\text{ kWh}$
* **Total Output:** $E_{\text{out}} = 2400 + 3000 + 400 + 0 = \mathbf{5800\text{ kWh}}$

**Step 2: Iron Loss Energy in 24 Hours**
$$E_{\text{iron}} = 1.5\text{ kW} \times 24\text{ h} = \mathbf{36.0\text{ kWh}}$$

**Step 3: Copper Loss Energy**
* Period 1: $\text{kVA}_1 = \frac{400}{0.8} = 500\text{ kVA}$ (Full load). $P_{cu1} = 6.0\text{ kW} \implies E_{cu1} = 6.0 \times 6 = 36.0\text{ kWh}$.
* Period 2: $\text{kVA}_2 = \frac{300}{0.75} = 400\text{ kVA}$. $P_{cu2} = \left(\frac{400}{500}\right)^2 \times 6.0 = 0.64 \times 6.0 = 3.84\text{ kW} \implies E_{cu2} = 3.84 \times 10 = 38.4\text{ kWh}$.
* Period 3: $\text{kVA}_3 = \frac{100}{0.8} = 125\text{ kVA}$. $P_{cu3} = \left(\frac{125}{500}\right)^2 \times 6.0 = \frac{6.0}{16} = 0.375\text{ kW} \implies E_{cu3} = 0.375 \times 4 = 1.5\text{ kWh}$.
* Period 4: No load $\implies E_{cu4} = 0\text{ kWh}$.
* **Total Copper Loss Energy:** $E_{cu} = 36.0 + 38.4 + 1.5 = \mathbf{75.9\text{ kWh}}$

**Step 4: All-Day Efficiency**
$$E_{\text{in}} = 5800 + 36.0 + 75.9 = 5911.9\text{ kWh}$$
$$\eta_{\text{all-day}} = \left(\frac{5800}{5911.9}\right) \times 100\% = \mathbf{98.11\%}$$

* **Reference in Theraja (Vol. II):** pp. 1144–1145
* **Reference in Chapman (5th Ed.):** pp. 99–101
* **Reference in Slide PDF:** Slides 50–52

---

### 71. Page 44, Q.1(c): A 400/200V, 1-Φ transformer is supplying a load of 0.25A at a p.f. of 0.866 lagging. On no load the current and power factor are 2A and 0.208 respectively. Calculate the current taken from the supply line.

**Given Data:**
* $V_1/V_2 = 400/200 \implies K = 200/400 = 0.5$
* Load: $I_2 = 0.25\text{ A}, \cos\phi_2 = 0.866 \implies \sin\phi_2 = 0.5$
* No-load: $I_0 = 2\text{ A}, \cos\phi_0 = 0.208 \implies \sin\phi_0 = \sqrt{1 - (0.208)^2} \approx 0.9781$

**Step 1: Reflected Secondary Current ($I_2'$)**
$$I_2' = K I_2 = 0.5 \times 0.25 = 0.125\text{ A}$$

**Step 2: Component Resolution**
* Horizontal (in-phase):
  $$I_{1x} = I_0 \cos\phi_0 + I_2' \cos\phi_2 = (2 \times 0.208) + (0.125 \times 0.866) = 0.416 + 0.10825 = 0.52425\text{ A}$$
* Vertical (quadrature lagging):
  $$I_{1y} = I_0 \sin\phi_0 + I_2' \sin\phi_2 = (2 \times 0.9781) + (0.125 \times 0.5) = 1.9562 + 0.0625 = 2.0187\text{ A}$$

**Step 3: Primary Supply Current Magnitude**
$$I_1 = \sqrt{(0.52425)^2 + (2.0187)^2} = \sqrt{0.2748 + 4.0751} = \sqrt{4.3499} \approx \mathbf{2.086\text{ A}}$$

* **Reference in Theraja (Vol. II):** pp. 1124–1126
* **Reference in Chapman (5th Ed.):** pp. 83–86
* **Reference in Slide PDF:** Slides 23–26

---

### **6. Auto-transformer and instrument transformers: (C.T. and P.T.)**
*(Reference Ranges: **Theraja Vol. II:** pp. 1145–1150, 1152–1156 | **Chapman 5th Ed.:** pp. 105–114, 119–123 | **Slides:** Slides 55–65, 75–82)*

### 73. Page 17, Q.3(c): What are the advantages and disadvantages of an auto-transformer compared to a conventional two-winding transformer?

* **Advantages:**
  1. **Copper Saving:** Substantial reduction in conductor weight and cost ($\Delta W = K W_{\text{two}}$).
  2. **Higher Efficiency:** Lower total copper loss ($I^2 R$) and lower core loss.
  3. **Superior Voltage Regulation:** Lower leakage impedance ($R_{01}, X_{01}$) produces smaller internal voltage drop.
  4. **Compact & Lightweight:** Smaller overall frame size and reduced oil/cooling requirements.
  5. **Higher kVA Capacity:** Power is transferred both **conductively** and **inductively**, increasing kVA throughput.
* **Disadvantages:**
  1. **Loss of Electrical Isolation:** Direct metallic connection between primary and secondary; no electrical barrier.
  2. **High Shock Hazard (When $K \ll 1$):** If the common lower winding opens, full high voltage appears directly across low-voltage load terminals.
  3. **Higher Short-Circuit Current:** Reduced internal leakage impedance results in much larger, destructive short-circuit fault currents.

* **Reference in Theraja (Vol. II):** pp. 1146–1148
* **Reference in Chapman (5th Ed.):** pp. 108–110
* **Reference in Slide PDF:** Slides 57–59

---

### 74. Page 17, Q.4(b): Why is an auto-transformer not suitable for use as a distribution transformer?

1. **Safety Hazard on Low-Voltage Consumer Side:** Distribution systems step down primary distribution (e.g., 11 kV) to domestic levels (230 V / 400 V). Since $K \ll 1$, an accidental open circuit in the common winding exposes domestic consumers and appliances to lethal 11 kV potentials.
2. **Transfer of High-Voltage Surges:** Without electrical isolation, lightning surges and primary switching transients conduct directly into secondary consumer circuits.
3. **Severe Fault Levels:** Lower internal impedance yields extraordinarily high short-circuit currents during line faults, exceeding standard domestic circuit breaker ratings.

* **Reference in Theraja (Vol. II):** p. 1148
* **Reference in Chapman (5th Ed.):** p. 110
* **Reference in Slide PDF:** Slide 60

---

### 75. Page 17, Q.4(d): Explain the principle of operation of a Current Transformer (CT) and Potential Transformer (PT).

* **Current Transformer (CT):**
  * **Function:** Steps down large AC power line currents to a standardized measurable value (typically 5 A or 1 A) for meters and protection relays.
  * **Principle:** Primary winding has very few turns of thick bar connected in **series** with the line. Secondary has many turns of fine wire connected across a low-impedance ammeter or relay coil (operates under virtually short-circuited condition):
    $$I_2 = I_1 \left(\frac{N_1}{N_2}\right)$$
* **Potential Transformer (PT):**
  * **Function:** Steps down high system voltages to a standardized safe value (typically 110 V or 100 V).
  * **Principle:** Connected in **parallel** across the high-voltage lines. Designed as an extremely high-accuracy, low-power step-down transformer operating under virtually open-circuit conditions (burden is a high-impedance voltmeter coil):
    $$V_2 = V_1 \left(\frac{N_2}{N_1}\right)$$

* **Reference in Theraja (Vol. II):** pp. 1152–1155
* **Reference in Chapman (5th Ed.):** pp. 119–122
* **Reference in Slide PDF:** Slides 75–80

---

### 76. Page 17, Q.3(d): Explain the dangers of using auto-transformer for the transformation ratio of K << 1.

* **Metallic Connection Danger:** Auto-transformers share a common winding section between HV and LV circuits.
* **Risk of High-Voltage Exposure:** When $K \ll 1$ (e.g., $11,000\text{ V} \rightarrow 230\text{ V}$), if the common grounded winding portion breaks or opens:
  * The voltage divider action collapses.
  * The full **11,000 V primary potential appears directly across the 230 V load terminals**.
  * Results in instant insulation flashover, catastrophic equipment fires, and fatal electrocution of personnel.

* **Reference in Theraja (Vol. II):** p. 1148
* **Reference in Chapman (5th Ed.):** p. 110
* **Reference in Slide PDF:** Slide 60

---

### 77. Page 18, Q.2(a): Define auto-transformer. Prove that less copper is used in auto-transformer than in an ordinary transformer.

* **Definition:** A transformer in which a single continuous winding serves as both primary and secondary, with part of the winding common to both circuits.
* **Proof of Copper Saving:**
  1. Weight of copper winding is proportional to (length $\times$ cross-section) $\propto (\text{Turns } N \times \text{Current } I) = \text{Ampere-Turns (AT)}$.
  2. **Two-Winding Transformer ($W_{\text{two}}$):**
     $$W_{\text{two}} \propto N_1 I_1 + N_2 I_2 = 2 N_1 I_1 \quad (\text{since } N_1 I_1 = N_2 I_2)$$
  3. **Step-Down Auto-Transformer ($W_{\text{auto}}$):**
     * Section $AB$ (series part, $N_1 - N_2$ turns): carries current $I_1$.
     * Section $BC$ (common part, $N_2$ turns): carries current $(I_2 - I_1)$.
     $$W_{\text{auto}} \propto (N_1 - N_2) I_1 + N_2 (I_2 - I_1) = N_1 I_1 - N_2 I_1 + N_2 I_2 - N_2 I_1$$
     Substitute $N_2 I_2 = N_1 I_1$:
     $$W_{\text{auto}} \propto 2 N_1 I_1 - 2 N_2 I_1 = 2 N_1 I_1 \left(1 - \frac{N_2}{N_1}\right) = W_{\text{two}} (1 - K)$$
  4. **Copper Saved ($\Delta W$):**
     $$\mathbf{\Delta W = W_{\text{two}} - W_{\text{auto}} = K \cdot W_{\text{two}}}$$
     *(Saving is directly proportional to transformation ratio $K$; maximum when $K \approx 1$).*

* **Reference in Theraja (Vol. II):** pp. 1146–1147
* **Reference in Chapman (5th Ed.):** pp. 106–108
* **Reference in Slide PDF:** Slides 55–57

---

### 78. Page 18, Q.2(b): With the help of additive and subtracting polarity of transformer, show that KVA capacity of auto-transformer increases compared to two winding transformer with same voltage rating.

* **Two-Winding Base Rating:** $S_{\text{two}} = V_1 I_1 = V_2 I_2$.
* **Reconnection as Auto-Transformer:**
  * **Additive Polarity (Series-Boost):** High voltage becomes $V_{\text{high}} = V_1 + V_2$.
    $$S_{\text{auto}} = (V_1 + V_2) I_2 = V_1 I_2 + V_2 I_2 = \frac{V_1}{V_2}(V_2 I_2) + S_{\text{two}} = \left(1 + \frac{V_1}{V_2}\right) S_{\text{two}} > S_{\text{two}}$$
  * **Subtractive Polarity:** High voltage is $V_1$; secondary is tapped at $V_2$:
    $$S_{\text{auto}} = \frac{1}{1 - K} S_{\text{two}}$$
* **Physical Reason for Increase:**
  * In a two-winding transformer, 100% of power is transferred **inductively** via magnetic flux.
  * In an auto-transformer, power is divided into **inductive power** and **conductive power** (directly conducted through the copper connection):
    $$\text{Inductive Power} = (1 - K) S_{\text{auto}} = S_{\text{two}}$$
    $$\text{Conductive Power} = K \cdot S_{\text{auto}}$$
  * Because core and windings only need to be sized for the inductive portion, total throughput capacity increases by factor $\frac{1}{1 - K}$.

* **Reference in Theraja (Vol. II):** pp. 1148–1150
* **Reference in Chapman (5th Ed.):** pp. 107–110
* **Reference in Slide PDF:** Slides 61–64

---

### 79. Page 18, Q.2(c): What should be the problem of personnel for using high voltage step-down auto-transformer, when transformation ratio K<<1.

* When $K \ll 1$, the common winding comprises very few turns compared to the series section.
* If a mechanical break or loose connection occurs in the common winding:
  * The neutral/ground reference is lost.
  * The full high voltage (e.g., 33 kV or 11 kV) passes straight through the series winding into the low-voltage output leads.
* Operating personnel handling secondary equipment rated for 230 V receive immediate, lethal electric shocks.

* **Reference in Theraja (Vol. II):** p. 1148
* **Reference in Chapman (5th Ed.):** p. 110
* **Reference in Slide PDF:** Slide 60

---

### 80. Page 19, Q.4(a): Define the term autotransformer. A two winding 440/110 V transformer is to be connected as a step down transformer, (i) show all possible connections for accomplishing this, and (ii) give the actual high side and low side voltages as well as the voltage ratio for each connection. [Figure Involved]

* **Definition:** A transformer having a single continuous winding tapped to provide two voltage levels, with part of the winding shared mutually.
* **Possible Step-Down Connections (for 440/110 V two-winding unit):**

| Connection Scheme | Polarity Setup | High-Side Voltage ($V_H$) | Low-Side Voltage ($V_L$) | Voltage Ratio ($V_H / V_L$) |
|---|---|---|---|---|
| **Scheme 1: Additive Series** | 440 V + 110 V in series; output across 110 V | **550 V** | **110 V** | $550/110 = \mathbf{5.00}$ |
| **Scheme 2: Additive Intermediate** | 440 V + 110 V in series; output across 440 V | **550 V** | **440 V** | $550/440 = \mathbf{1.25}$ |
| **Scheme 3: Subtractive Tapped** | Input across 440 V; output tapped across 110 V | **440 V** | **110 V** | $440/110 = \mathbf{4.00}$ |
| **Scheme 4: Subtractive Opposing** | Input across 440 V; output across $(440 - 110)\text{ V}$ | **440 V** | **330 V** | $440/330 = \mathbf{1.33}$ |

* **Reference in Theraja (Vol. II):** pp. 1148–1150
* **Reference in Chapman (5th Ed.):** pp. 106–109
* **Reference in Slide PDF:** Slides 61–64

---

### 81. Page 19, Q.4(b): Draw the connection diagrams of instrument transformer to measure (i) voltage, (ii) current and (iii) power of high voltage-high current system with laboratory meters. [Figure Involved]

```
High Voltage Line 1 =================[ Primary CT ]================================== Load
                                         |     |
                                       [ P1   P2 ]
                                         |     |
                                    +----+-----+
                                    | [CT Sec] |
                                    |    |     |
                                    |   (A)    |
                                    |    |     |
                                    |  [ W_I ] | (Current Coil of Wattmeter)
                                    +----+-----+
                                         |
                                      (Earth)

High Voltage Line 1 ---------+                                            
                             |                                            
                        [ Primary PT ]                                    
                             |                                            
High Voltage Line 2 ---------+                                            
                             |                                            
                        [ Secondary ]                                     
                             |                                            
                       +-----+-----+                                      
                       |    (V)    | (Voltmeter)                          
                       |  [ W_V ]  | (Pressure Coil of Wattmeter)        
                       +-----+-----+                                      
                             |                                            
                          (Earth)                                         
```

* **Instruments Used:**
  1. **Voltmeter ($V$):** Connected across PT secondary ($110\text{ V}$ range). Line voltage $= V \times (\text{PT Ratio})$.
  2. **Ammeter ($A$):** Connected in series with CT secondary ($5\text{ A}$ range). Line current $= A \times (\text{CT Ratio})$.
  3. **Wattmeter ($W$):** Current coil connected in series with CT secondary; pressure coil connected across PT secondary. Total power $= W \times (\text{CT Ratio}) \times (\text{PT Ratio})$.

* **Reference in Theraja (Vol. II):** pp. 1152–1156
* **Reference in Chapman (5th Ed.):** pp. 119–123
* **Reference in Slide PDF:** Slides 75–82

---

### 82. Page 19, Q.4(c): Why secondary of a current transformer can never be opened?

* **Normal Operation:**
  * Primary is in series with the high-voltage line, carrying line current $I_1$ dictated entirely by the external power system.
  * Secondary is closed across low-impedance ammeter/relay coil.
  * Secondary MMF ($N_2 I_2$) opposes primary MMF ($N_1 I_1$), leaving a very small net magnetizing MMF:
    $$\mathcal{F}_{\text{net}} = N_1 I_1 - N_2 I_2 = N_1 I_0 \approx 1\text{--}2\% \text{ of } N_1 I_1$$
* **When Secondary is Opened ($I_2 = 0$):**
  1. **Vanishing Counter-MMF:** Opposing secondary MMF disappears completely. The entire heavy line current becomes pure magnetizing current.
  2. **Deep Core Saturation:** Core flux surges to maximum saturation levels. Large hysteresis and eddy current losses rapidly heat the core, burning winding insulation.
  3. **Lethal High Voltage:** The extremely steep rate of change of flux ($d\Phi/dt$) induces dangerously high peak voltage pulses (**several thousand volts**) across the open secondary terminals, presenting a fatal electrocution hazard to personnel.

* **Reference in Theraja (Vol. II):** p. 1154
* **Reference in Chapman (5th Ed.):** pp. 121–122
* **Reference in Slide PDF:** Slides 77–79

---

### 83. Page 21, Q.4(c): What are the instrument transformers? Explain how they operate? Where are they used? A transformer that is used to measure electrical quantities like current, voltage is known as an instrument transformer.

* **Definition:** Precision transformers used in conjunction with standard low-range laboratory instruments (5 A ammeters, 110 V voltmeters) to measure high voltages, high currents, and high power in AC systems.
* **Operation:**
  * **Current Transformer (CT):** Series-connected; steps down high line current proportionally ($I_2 = I_1 / K_i$).
  * **Potential Transformer (PT):** Shunt-connected; steps down high transmission voltage proportionally ($V_2 = V_1 / K_v$).
* **Applications:**
  * Electrical metering and revenue billing in substations.
  * Feeding signals into protective relays (differential, overcurrent, distance relays).
  * Providing complete electrical isolation between lethal high-voltage lines and control room operators.

* **Reference in Theraja (Vol. II):** pp. 1152–1155
* **Reference in Chapman (5th Ed.):** pp. 119–122
* **Reference in Slide PDF:** Slides 75–80

---

### 84. Page 24, Q.36-40: (List covers theory of step-down and step-up auto-transformer, math validation of copper saving, advantages/disadvantages, applications, and conversion technique of two-winding to auto-transformer).

1. **Step-Down / Step-Up Theory:** Single continuous tapped winding; $V_1/V_2 = N_1/N_2$.
2. **Copper Saving:** $\text{Saving} = K \cdot W_{\text{two}}$ (higher saving when $K \rightarrow 1$).
3. **Key Applications:**
   * Induction motor starting compensators (starters).
   * Laboratory variacs (smooth, continuously variable AC voltage).
   * Grid interconnecting transformers (e.g., 400 kV to 220 kV or 132 kV to 66 kV).
   * Feeder booster transformers.

* **Reference in Theraja (Vol. II):** pp. 1145–1150
* **Reference in Chapman (5th Ed.):** pp. 105–112
* **Reference in Slide PDF:** Slides 55–65

---

### 85. Page 28, Q.No.1: How efficiency and kVA capacity of two-winding transformer can be increased by an auto-transformer connection? Explain with suitable example.

* **Mechanism:**
  * Reconnecting a two-winding transformer as an auto-transformer introduces **conductive power transfer** alongside magnetic induction.
  * Rating scales up by factor:
    $$\text{Capacity Multiplier} = \frac{1}{1 - K}$$
* **Example:**
  * Consider a 10 kVA, 2000/200 V two-winding transformer ($K = 0.1$).
  * Connect windings in series aiding to form a 2200/2000 V auto-transformer:
    * New transformation ratio: $K' = \frac{2000}{2200} = \frac{10}{11} \approx 0.909$.
    * New kVA Capacity:
      $$S_{\text{auto}} = \frac{S_{\text{two}}}{1 - K'} = \frac{10\text{ kVA}}{1 - (10/11)} = 10 \times 11 = \mathbf{110\text{ kVA}}$$
    * Capacity increases **11-fold** using the exact same physical copper and core!
    * Because core and winding losses remain identical (sized for 10 kVA), total efficiency jumps from e.g. 96% to **over 99.6%**.

* **Reference in Theraja (Vol. II):** pp. 1148–1150
* **Reference in Chapman (5th Ed.):** pp. 107–110
* **Reference in Slide PDF:** Slides 61–64

---

### 86. Page 44, Q.4(b): Define auto transformer? Why are single winding auto transformer not normally used in high voltage transformation with transformation ratio K<<1?

* **Definition:** A transformer possessing a single continuous winding shared between primary and secondary circuits.
* **Why Not Used for $K \ll 1$:**
  1. **Minimal Copper Saving:** Saving is $K \cdot W_{\text{two}}$; when $K \ll 1$, copper savings are practically zero.
  2. **Catastrophic High-Voltage Hazard:** If the shared common winding opens, the entire primary voltage appears on the secondary side, causing fatal electric shocks and fires.
  3. **High Short-Circuit Risk:** Extremely low leakage reactance permits massive fault currents during downstream short circuits.

* **Reference in Theraja (Vol. II):** pp. 1145, 1148
* **Reference in Chapman (5th Ed.):** pp. 105, 110
* **Reference in Slide PDF:** Slides 55, 60

---

### **7. Parallel operation of transformers**
*(Reference Ranges: **Theraja Vol. II:** pp. 1157–1165 | **Chapman 5th Ed.:** pp. 123–128 | **Slides:** Slides 205–211)*

### 88. Page 7, Q.1(b): What are the conditions to be fulfilled to operate transformers successfully in parallel with proper division of load?

* **Mandatory Conditions (Must be strictly satisfied):**
  1. **Identical Voltage Ratios & Voltage Ratings:** Prevents circulating currents on no-load.
  2. **Identical Polarity:** Connecting opposite polarities produces a dead short circuit, destroying windings.
  3. **Identical Phase Sequence & Zero Relative Phase Displacement (for 3-Phase):** Must belong to the same vector group.
* **Desirable Conditions (For proportional load sharing):**
  4. **Per-Unit Impedances Inversely Proportional to kVA Ratings:** Ensures transformers share total load in exact proportion to their capacities without overloading any unit.
  5. **Identical $X/R$ Ratio:** Ensures operating power factors are identical, preventing circulating reactive currents.

* **Reference in Theraja (Vol. II):** pp. 1157–1159
* **Reference in Chapman (5th Ed.):** pp. 123–125
* **Reference in Slide PDF:** Slides 205–207

---

### 89. Page 7, Q.2(c): Two 1-φ transformers A and B are connected in parallel. They have same kVA rating but their resistances are respectively 0.005 and 0.01 p.u. and their leakage reactances are 0.05 and 0.04 p.u. If A is operated on full-load at a p.f of 0.75 lagging, what will be the load and p.f. of B?

**Given Data:**
* $\vec{Z}_A = 0.005 + j 0.05\text{ p.u.} = 0.05025\angle 84.29^\circ\text{ p.u.}$
* $\vec{Z}_B = 0.01 + j 0.04\text{ p.u.} = 0.04123\angle 75.96^\circ\text{ p.u.}$
* Transformer A load: $\vec{S}_A = 1.0\angle -41.41^\circ\text{ p.u.}$ ($\cos\phi_A = 0.75\text{ lag}$)

**Calculation:**
* Load sharing with equal voltage ratios:
  $$\frac{\vec{S}_B}{\vec{S}_A} = \frac{\vec{Z}_A}{\vec{Z}_B} = \frac{0.05025\angle 84.29^\circ}{0.04123\angle 75.96^\circ} = 1.2188\angle 8.33^\circ$$
  $$\vec{S}_B = (1.0\angle -41.41^\circ) \times (1.2188\angle 8.33^\circ) = \mathbf{1.219\angle -33.08^\circ\text{ p.u.}}$$

**Results:**
1. **Load on Transformer B:** **$1.219\times \text{Rating}$ ($121.9\%$ of full-load rating; 21.9% overload)**.
2. **Power Factor of Transformer B:** $\cos(33.08^\circ) = \mathbf{0.838\text{ lagging}}$.

* **Reference in Theraja (Vol. II):** pp. 1163–1165
* **Reference in Chapman (5th Ed.):** pp. 127–128
* **Reference in Slide PDF:** Slide 210

---

### 90. Page 9, Q.4(a): Explain the condition of parallel operation of 3- transformers.

1. **Identical Line Voltage Ratios:** Prevents no-load circulating currents.
2. **Correct Polarity:** Windings must be paired with matching polarity markings.
3. **Identical Phase Sequence:** Rotational sequence of line voltages ($R\text{-}Y\text{-}B$) must be identical.
4. **Zero Relative Phase Displacement (Same Vector Group):** Transformers must have compatible internal angular shifts (e.g., $0^\circ$ for Y-Y and $\Delta$-$\Delta$; $30^\circ$ for Y-$\Delta$ and $\Delta$-Y). A Y-Y transformer cannot be paralleled with a Y-$\Delta$ transformer.
5. **Per-Unit Impedance Matching:** Per-unit impedances should be inversely proportional to kVA ratings with equal $X/R$ ratios.

* **Reference in Theraja (Vol. II):** pp. 1215–1217
* **Reference in Chapman (5th Ed.):** pp. 124–126
* **Reference in Slide PDF:** Slides 206–208

---

### 91. Page 19, Q.2(a): Why is parallel operation required for transformers? Write down the conditions of connecting two transformers in parallel.

* **Why Parallel Operation is Required:**
  1. **Higher Reliability & Continuity of Service:** If one unit fails or undergoes scheduled maintenance, power supply is maintained via remaining units.
  2. **High Operating Efficiency:** Individual transformers can be energized or de-energized matching daily load demand, ensuring units always operate near peak efficiency.
  3. **Future System Expansion:** Additional capacity can be installed incrementally as load grows, avoiding large upfront capital expenditures.
  4. **Transportation & Size Limits:** Substation sites can accommodate multiple medium units when a single massive transformer exceeds highway/rail transport limits.
* **Conditions for Parallel Connection:**
  * Same voltage ratios, same polarity, identical per-unit impedances, and equal $X/R$ ratios.

* **Reference in Theraja (Vol. II):** pp. 1157–1159
* **Reference in Chapman (5th Ed.):** pp. 123–125
* **Reference in Slide PDF:** Slides 205–207

---

### 92. Page 19, Q.2(b): Two single-phase transformer A and B of equal voltage ratio are running in parallel and supply a load of 1000 A at 0.8 p.f. lagging. The equivalent impedance of the two transformers are (2 + j3) and (2.5 + j5) ohms, respectively. Calculate the current supplied by each transformer and the ratio of the kW output of the two transformers.

**Given Data:**
* Total current: $\vec{I} = 1000(0.8 - j0.6) = 800 - j600\text{ A}$
* $\vec{Z}_A = 2 + j3\ \Omega$, $\vec{Z}_B = 2.5 + j5\ \Omega$

**Step 1: Current Ratio**
$$\frac{\vec{Z}_B}{\vec{Z}_A} = \frac{2.5 + j5}{2 + j3} = \frac{(2.5 + j5)(2 - j3)}{4 + 9} = \frac{5 - j7.5 + j10 + 15}{13} = \frac{20 + j2.5}{13} \approx 1.5385 + j0.1923$$
$$\vec{I}_A = \vec{I}_B (1.5385 + j0.1923)$$
$$\vec{I} = \vec{I}_A + \vec{I}_B = \vec{I}_B(2.5385 + j0.1923)$$

**Step 2: Transformer Currents**
* Current supplied by Transformer B:
  $$\vec{I}_B = \frac{800 - j600}{2.5385 + j0.1923} \approx \mathbf{294.6 - j259.5\text{ A}}$$
  $$I_B = \sqrt{(294.6)^2 + (259.5)^2} \approx \mathbf{392.6\text{ A}} \quad (\cos\phi_B = 0.75\text{ lag})$$
* Current supplied by Transformer A:
  $$\vec{I}_A = \vec{I} - \vec{I}_B = (800 - 294.6) - j(600 - 259.5) = \mathbf{505.4 - j340.5\text{ A}}$$
  $$I_A = \sqrt{(505.4)^2 + (340.5)^2} \approx \mathbf{609.5\text{ A}} \quad (\cos\phi_A = 0.83\text{ lag})$$

**Step 3: Ratio of kW Outputs**
* Real power is proportional to active (real) current components:
  $$\frac{P_A}{P_B} = \frac{I_{Ax}}{I_{Bx}} = \frac{505.4}{294.6} \approx \mathbf{1.716 : 1}$$

* **Reference in Theraja (Vol. II):** pp. 1162–1164
* **Reference in Chapman (5th Ed.):** pp. 127–128
* **Reference in Slide PDF:** Slide 210

---

### 93. Page 19, Q.3(b): If two transformers are connected in parallel, show that the loads are divided between them in inverse proportion to their equivalent impedances when their turn’s ratios are equal.

**Proof:**
1. Let two transformers A and B be connected across common busbars with equal no-load voltages ($E_A = E_B$).
2. Both feed a common load at terminal voltage $V$:
   $$V = E_A - \vec{I}_A \vec{Z}_A = E_B - \vec{I}_B \vec{Z}_B$$
3. Since $E_A = E_B$:
   $$\vec{I}_A \vec{Z}_A = \vec{I}_B \vec{Z}_B \implies \frac{\vec{I}_A}{\vec{I}_B} = \frac{\vec{Z}_B}{\vec{Z}_A}$$
4. Multiply both sides by terminal voltage $V$:
   $$\frac{V \vec{I}_A^*}{V \vec{I}_B^*} = \frac{\vec{S}_A}{\vec{S}_B} = \frac{\vec{Z}_B^*}{\vec{Z}_A^*}$$
5. In terms of magnitude:
   $$\mathbf{\frac{S_A}{S_B} = \frac{Z_B}{Z_A}}$$
   *(Loads shared are strictly inversely proportional to their internal equivalent impedances).*

* **Reference in Theraja (Vol. II):** pp. 1160–1162
* **Reference in Chapman (5th Ed.):** pp. 126–127
* **Reference in Slide PDF:** Slides 208–209

---

### 94. Page 24, Q.41: What are the reasons for connecting transformers in parallel? Mention the conditions for satisfactory parallel operation.

* **Reasons:** Service reliability, maintenance flexibility, high seasonal operating efficiency, physical transportation limits.
* **Conditions:**
  1. Identical voltage ratios and polarity.
  2. Equal per-unit impedances with identical $X/R$ ratios.
  3. Identical phase sequence and zero angular displacement (same vector group for 3-phase).

* **Reference in Theraja (Vol. II):** pp. 1157–1159
* **Reference in Chapman (5th Ed.):** pp. 123–125
* **Reference in Slide PDF:** Slides 205–207

---

### **8. Three phase transformer and its connections**
*(Reference Ranges: **Theraja Vol. II:** pp. 1205–1220 | **Chapman 5th Ed.:** pp. 110–119 | **Slides:** Slides 83–102)*

### 96. Page 7, Q.2(b): What will happen if one winding of a 3-φ transformer is not connected properly in regard to polarity? Show with corresponding vector diagram. [Figure Involved]

* **In Delta ($\Delta$) Connection:**
  * Under proper polarities, the vector sum of voltages around the closed mesh is zero:
    $$\vec{V}_{ab} + \vec{V}_{bc} + \vec{V}_{ca} = 0$$
  * If one phase (say phase $C$) is reversed:
    $$\vec{V}_{\text{resultant}} = \vec{V}_{ab} + \vec{V}_{bc} - \vec{V}_{ca} = 2 \vec{V}_{ph}$$
  * A resultant EMF of **twice the phase voltage** acts inside the low-impedance closed delta, producing a destructive short-circuit current that instantly burns the windings.
* **In Star (Y) Connection:**
  * Reversing one phase produces unbalanced line voltages ($V_L = V_{ph}$ instead of $\sqrt{3} V_{ph}$) and shifts the neutral potential, causing severe phase unbalance.

* **Reference in Theraja (Vol. II):** pp. 1207–1209
* **Reference in Chapman (5th Ed.):** pp. 112–114
* **Reference in Slide PDF:** Slides 88–90

---

### 97. Page 9, Q.1(b): Explain with the help of vector diagram how three 1-φ transformers can be used to design a 3-φ transformer. [Figure Involved]

* **Bank of Three 1-Phase Units:**
  * Three identical single-phase transformers have their primaries and secondaries interconnected externally to form a 3-phase bank.
  * Connections can be Star-Star (Y-Y), Delta-Delta ($\Delta$-$\Delta$), Star-Delta (Y-$\Delta$), or Delta-Star ($\Delta$-Y).
* **Phasor Alignment:**
  * Core fluxes in the three units are displaced in time by $120^\circ$ electrical.
  * Resulting phase voltages are displaced by $120^\circ$:
    $$\vec{V}_A = V_{ph}\angle 0^\circ, \quad \vec{V}_B = V_{ph}\angle -120^\circ, \quad \vec{V}_C = V_{ph}\angle +120^\circ$$
* **Advantage:** If one single-phase unit fails in a $\Delta$-$\Delta$ bank, it can be removed and the remaining two units continue supplying 3-phase power in Open-Delta (V-V) connection.

* **Reference in Theraja (Vol. II):** pp. 1205–1207
* **Reference in Chapman (5th Ed.):** pp. 110–113
* **Reference in Slide PDF:** Slides 83–87

---

### 98. Page 9, Q.1(c): What will happen if one winding of a 3-φ, Δ-connected transformer is not connected properly in regard to polarity?

* A closed delta winding forms a closed loop.
* Reversing one winding lead reverses that phase voltage vector by $180^\circ$.
* Instead of summing to zero, the three phase voltages sum to:
  $$\vec{E}_{\text{net}} = \vec{E}_1 + \vec{E}_2 - \vec{E}_3 = 2 E_{ph}$$
* This massive resultant voltage drives an immense short-circuit circulating current limited only by internal winding impedances ($I_{sc} = 2 E_{ph} / 3 Z_{ph}$), destroying the transformer windings within cycles.

* **Reference in Theraja (Vol. II):** pp. 1207–1209
* **Reference in Chapman (5th Ed.):** pp. 112–114
* **Reference in Slide PDF:** Slides 88–90

---

### 99. Page 9, Q.4(b): Suppose one winding of Δ-connected transformer is suddenly burnout during operation (i) Does it possible to operate using remaining two windings. (ii) Is it possible to supply balanced load, if yes show with corresponding vector diagram. [Figure Involved]

* **(i) Yes, it is possible:**
  * The damaged winding is isolated, leaving the remaining two units connected in **Open-Delta (V-V) connection**.
* **(ii) Yes, it can supply a balanced 3-phase load:**
  * Line voltages $V_{AB}, V_{BC}, V_{CA}$ maintain full balanced $120^\circ$ relationships across all three load phases.
  * **Capacity Derating:** Total 3-phase power handling capacity is reduced to:
    $$\mathbf{57.7\% \text{ of original } \Delta\text{-}\Delta \text{ bank rating}} \quad \left(\frac{1}{\sqrt{3}} \approx 0.577\right)$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 100. Page 9, Q.4(c): Two T-connected transformer are used to supply a 440 V, 33 kVA balanced load from a balanced 3- supply of 3300 V. Calculate (i) Voltage and current rating of each coil (ii) kVA ratting of the main and teaser transformer (iii) Find the position of neutral point in teaser winding.

**Given Data:** $V_{L1} = 3300\text{ V}$, $V_{L2} = 440\text{ V}$, Balanced load $= 33\text{ kVA}$.

**Step 1: Line Currents**
* Primary: $I_{L1} = \frac{33,000}{\sqrt{3} \times 3300} = \mathbf{5.77\text{ A}}$
* Secondary: $I_{L2} = \frac{33,000}{\sqrt{3} \times 440} = \mathbf{43.30\text{ A}}$

**Part (i): Ratings of Each Coil**
* **Main Transformer:**
  * Primary: $V = 3300\text{ V}$, $I = 5.77\text{ A}$
  * Secondary: $V = 440\text{ V}$, $I = 43.30\text{ A}$
* **Teaser Transformer:**
  * Primary: $V = \frac{\sqrt{3}}{2} \times 3300 = \mathbf{2858\text{ V}}$, $I = \mathbf{5.77\text{ A}}$
  * Secondary: $V = \frac{\sqrt{3}}{2} \times 440 = \mathbf{381\text{ V}}$, $I = \mathbf{43.30\text{ A}}$

**Part (ii): kVA Ratings**
* Main Transformer: $S_{\text{main}} = 3300 \times 5.77 \times 10^{-3} = \mathbf{19.05\text{ kVA}}$
* Teaser Transformer: $S_{\text{teaser}} = 2858 \times 5.77 \times 10^{-3} = \mathbf{16.50\text{ kVA}}$

**Part (iii): Position of Neutral Point ($N$) in Teaser Winding**
* Neutral divides the teaser primary winding in a **$2 : 1$ ratio**:
  * Distance from line apex terminal $A$: $\frac{2}{3}$ of total turns ($V_{AN} = \frac{3300}{\sqrt{3}} = \mathbf{1905.3\text{ V}}$).
  * Distance from center-tap point $D$: $\frac{1}{3}$ of total turns ($V_{ND} = \mathbf{952.7\text{ V}}$).

* **Reference in Theraja (Vol. II):** pp. 1226–1228
* **Reference in Chapman (5th Ed.):** pp. 128–130
* **Reference in Slide PDF:** Slide 214

---

### 101. Page 11, Q.4(a) (lower): What are the disadvantages in a three phase Y-Y connected transformer without the neutral grounding?

1. **Floating Neutral (Neutral Inversion):** Unbalanced loads cause the neutral point to shift off-center, producing severely distorted and unequal phase voltages across loads.
2. **Third-Harmonic Voltage Distortion:** Third-harmonic magnetizing currents cannot flow in an ungrounded 3-wire star system. This forces a large third-harmonic flux in the core, inducing substantial third-harmonic voltages ($3f$) that stress winding insulation and cause telephone line interference.
3. **Overvoltage Risk:** An accidental ground fault on one phase shifts line-to-ground voltage on healthy phases up to full line voltage ($\sqrt{3} V_{ph}$).

* **Reference in Theraja (Vol. II):** pp. 1209–1211
* **Reference in Chapman (5th Ed.):** pp. 113–115
* **Reference in Slide PDF:** Slides 91–93

---

### 102. Page 11, Q.4(b) (bottom): Explain why Δ-Δ connected three-phase transformer is rerated to 57.7% of its power rating when one of the phases is damaged and removed.

**Derivation:**
1. In closed delta ($\Delta$-$\Delta$), total rated capacity is:
   $$S_{\Delta} = 3 V_{ph} I_{ph} = 3 V_L \left(\frac{I_L}{\sqrt{3}}\right) = \sqrt{3} V_L I_L$$
2. In open delta (V-V), the secondary line current passes directly through the single remaining phase winding ($I_L = I_{ph}$).
3. To avoid thermal overloading of the two remaining transformers, line current must not exceed rated phase current:
   $$I_{L(\text{open})} = I_{ph} = \frac{I_L}{\sqrt{3}}$$
4. Total 3-phase power delivered in open delta:
   $$S_{\text{V}} = \sqrt{3} V_L I_{L(\text{open})} = \sqrt{3} V_L \left(\frac{I_L}{\sqrt{3}}\right) = V_L I_L$$
5. Ratio of Open-Delta to Closed-Delta capacity:
   $$\mathbf{\frac{S_{\text{V}}}{S_{\Delta}} = \frac{V_L I_L}{\sqrt{3} V_L I_L} = \frac{1}{\sqrt{3}} \approx 0.577 = 57.7\%}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 103. Page 11, Q.4(a) (bottom): What are problems in a three phase Y-Y connected transformer, without the neutral grounding? Draw the connection and wiring diagrams of Y-Δ three phase transformer. [Figure Involved]

* **Problems Without Neutral Grounding:** Neutral shift under unbalanced loads, high third-harmonic voltage distortion, and lack of ground return path for fault clearing.
* **Y-$\Delta$ Connection:**
  ```
  Primary (Star):                      Secondary (Delta):
       A -----[ N1 ]-----+                  a -----[ N2 ]-----+--- c'
                         |                                    |
       B -----[ N1 ]-----+ (Neutral)        b -----[ N2 ]-----+--- a'
                         |                                    |
       C -----[ N1 ]-----+                  c -----[ N2 ]-----+--- b'
  ```
  * Star primary handles high line transmission voltages with reduced phase insulation ($V_{ph} = V_L/\sqrt{3}$).
  * Delta secondary traps third-harmonic circulating currents, providing sinusoidal output voltage without third-harmonic distortion.

* **Reference in Theraja (Vol. II):** pp. 1210–1213
* **Reference in Chapman (5th Ed.):** pp. 113–116
* **Reference in Slide PDF:** Slides 91–95

---

### 104. Page 12, Q.3(b): Explain how a third harmonic voltage affects a Y-Y transformer bank? Why is grounding the neutral of a Y-Y transformer bank desirable?

* **Effects of Third Harmonic Voltages:**
  * Third-harmonic magnetizing currents are in-phase across all three limbs ($3 \times 120^\circ = 360^\circ \equiv 0^\circ$).
  * In an ungrounded Y-Y bank, these currents have no return path and cannot flow.
  * Suppressing third-harmonic current produces heavily peaked, flat-topped flux containing large third-harmonic components, inducing voltages up to 50–70% of fundamental.
  * Causes severe insulation stress and inductive interference in neighboring communication lines.
* **Why Neutral Grounding is Desirable:**
  * Grounding the primary neutral provides a closed path through earth for third-harmonic magnetizing currents.
  * This restores sinusoidal mutual core flux, completely eliminating third-harmonic voltage distortion.

* **Reference in Theraja (Vol. II):** pp. 1209–1211
* **Reference in Chapman (5th Ed.):** pp. 113–115
* **Reference in Slide PDF:** Slides 91–93

---

### 105. Page 24, Q.42-57: (Comprehensive list asking to describe construction, advantages of 3-phase over three 1-phase, various connections like Y-Y, Δ-Δ, Y-Δ, Δ-Y, V-V, T-T, their applications, and power handling capacity).

1. **Core-Type vs. Shell-Type:** 3-limb laminated core merges magnetic returns, saving 33% iron.
2. **Advantages over Three 1-Phase Units:** 15% lower weight, 20% smaller space, higher efficiency, lower cost.
3. **Summary of Standard Connections:**
   * **Y-Y:** High voltage, small currents; requires neutral grounding.
   * **$\Delta$-$\Delta$:** Low voltage, heavy currents; operates in V-V if one phase fails.
   * **Y-$\Delta$:** Generating stations (step-up) and transmission ends (step-down).
   * **$\Delta$-Y:** Commercial distribution systems providing 3-phase 4-wire supplies (400 V / 230 V).
   * **V-V (Open-Delta):** Emergency 2-unit operation at 57.7% bank rating.
   * **T-T (Scott):** 3-phase to 3-phase or 3-phase to 2-phase conversion.

* **Reference in Theraja (Vol. II):** pp. 1205–1220
* **Reference in Chapman (5th Ed.):** pp. 110–119
* **Reference in Slide PDF:** Slides 83–102

---

### 106. Page 41, Q.3(b): How can three phase power transform be accomplished using only two single phase transformers? What type of connections can be used?

Two distinct connection schemes can transform balanced 3-phase power using only two single-phase transformers:
1. **Open-Delta (V-V) Connection:**
   * Made by connecting two single-phase units across two phases of a 3-phase line.
   * Delivers balanced 3-phase voltage at **57.7% capacity** of a 3-unit delta bank (or **86.6% utilization** of the two installed transformers).
2. **T-T (Scott) Connection:**
   * Composed of a **Main Transformer** (center-tapped at 50%) and a **Teaser Transformer** (tapped at $86.6\% = \frac{\sqrt{3}}{2}$).
   * Provides balanced 3-phase to 3-phase transformation with smaller phase unbalance than V-V.

* **Reference in Theraja (Vol. II):** pp. 1218–1222, 1226–1228
* **Reference in Chapman (5th Ed.):** pp. 115–118, 128–130
* **Reference in Slide PDF:** Slides 96–100, 214

---

### **9. Phase conversion**
*(Reference Ranges: **Theraja Vol. II:** pp. 1225–1232 | **Chapman 5th Ed.:** pp. 128–134 | **Slides:** Slides 212–216)*

### 108. Page 7, Q.3(a): With neat diagram show that the power handing capacity of a V-V circuit is 57.7% of the capacity of a complete Δ-Δ circuit of the same transformer. [Figure Involved]

#### Circuit Diagram
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

**Proof:**
* Let $V_L$ = line voltage, $I_{\text{ph}}$ = rated phase current of each transformer.
* **Closed-Delta ($\Delta$-$\Delta$) Rating:**
  $$S_{\Delta} = 3 V_{\text{ph}} I_{\text{ph}} = 3 V_L I_{\text{ph}} = \sqrt{3} V_L (\sqrt{3} I_{\text{ph}}) = \sqrt{3} V_L I_L$$
* **Open-Delta (V-V) Rating:**
  * Secondary line current is restricted to transformer phase current rating ($I_L = I_{\text{ph}}$):
    $$S_{\text{V}} = \sqrt{3} V_L I_{\text{ph}}$$
* **Capacity Ratio:**
  $$\mathbf{\frac{S_{\text{V}}}{S_{\Delta}} = \frac{\sqrt{3} V_L I_{\text{ph}}}{3 V_L I_{\text{ph}}} = \frac{1}{\sqrt{3}} \approx 0.577 = 57.7\%}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 109. Page 7, Q.3(b): How 3-φ, 4 wire connection can be obtained from scoot-connection? Explain with necessary circuit diagram. [Figure Involved]

* **Scott Connection Configuration:**
  * Uses two transformers: **Main Transformer** and **Teaser Transformer**.
  * Main primary is connected between lines $B$ and $C$, with center-tap $D$ ($50\%$ turns).
  * Teaser primary has $86.6\%$ turns ($\frac{\sqrt{3}}{2} N_1$), connected between line $A$ and center-tap $D$.
* **Deriving the 4th Wire (Neutral $N$):**
  * A neutral point $N$ is located on the teaser winding at a distance of **one-third of total teaser turns up from tap $D$** (or two-thirds down from terminal $A$):
    $$V_{AN} = \frac{2}{3} V_{\text{teaser}} = \frac{2}{3}\left(\frac{\sqrt{3}}{2} V_L\right) = \frac{V_L}{\sqrt{3}} = V_{\text{phase}}$$
  * Bringing out a lead from $N$ provides a true balanced 4-wire neutral point for 3-phase 4-wire systems.

* **Reference in Theraja (Vol. II):** pp. 1226–1228
* **Reference in Chapman (5th Ed.):** pp. 128–130
* **Reference in Slide PDF:** Slide 214

---

### 110. Page 11, Q.4(b) (lower): Show with connection diagram how 3-φ 4-wire connection can be achieved for T-connection. [Figure Involved]

* In a T-T connection, the neutral terminal $N$ is tapped at $\frac{1}{3}$ of the teaser winding length from the junction with the main transformer.
* This neutral point $N$ provides equal star-line potentials ($V_{AN} = V_{BN} = V_{CN} = V_L/\sqrt{3}$), creating a completely symmetrical 3-phase 4-wire supply for mixed 3-phase industrial and 1-phase residential lighting loads.

* **Reference in Theraja (Vol. II):** pp. 1226–1228
* **Reference in Chapman (5th Ed.):** pp. 128–130
* **Reference in Slide PDF:** Slide 214

---

### 111. Page 12, Q.4(b): Prove that closed – Δ kVA is √3 times higher that open – Δ kVA.

**Proof:**
1. Open-Delta kVA capacity:
   $$S_{\text{V}} = \sqrt{3} V_L I_{ph}$$
2. Closed-Delta kVA capacity:
   $$S_{\Delta} = 3 V_{ph} I_{ph} = 3 V_L I_{ph}$$
3. Taking the ratio:
   $$\frac{S_{\Delta}}{S_{\text{V}}} = \frac{3 V_L I_{ph}}{\sqrt{3} V_L I_{ph}} = \frac{3}{\sqrt{3}} = \mathbf{\sqrt{3}} \approx 1.732$$
   $$\mathbf{S_{\Delta} = \sqrt{3} \times S_{\text{V}}}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 112. Page 12, Q.4(c): Two transformers connected in open – Δ, supply a 400 kVA balanced load operating at 0.866 p.f. (lagging). The load voltage is 440 V. What is the (i) kVA supplied by each transformer? (ii) kW supplied by each transformer?

**Given Data:**
* Load kVA = 400 kVA, $\cos\theta = 0.866\text{ lagging} \implies \theta = 30^\circ$

**Part (i): kVA Supplied by Each Transformer**
* In open delta, each transformer carries the full line current:
  $$S_1 = S_2 = \frac{S_{\text{total}}}{\sqrt{3}} = \frac{400}{\sqrt{3}} \approx \mathbf{230.94\text{ kVA}}$$

**Part (ii): kW Supplied by Each Transformer**
* The operating power factors of the two units are:
  $$\cos\phi_1 = \cos(\theta - 30^\circ) = \cos(30^\circ - 30^\circ) = \cos(0^\circ) = \mathbf{1.0}$$
  $$\cos\phi_2 = \cos(\theta + 30^\circ) = \cos(30^\circ + 30^\circ) = \cos(60^\circ) = \mathbf{0.5}$$
* Real Power Output:
  * Transformer 1: $P_1 = S_1 \cos\phi_1 = 230.94 \times 1.0 = \mathbf{230.94\text{ kW}}$
  * Transformer 2: $P_2 = S_2 \cos\phi_2 = 230.94 \times 0.5 = \mathbf{115.47\text{ kW}}$
  * *Check:* $P_{\text{total}} = 230.94 + 115.47 = 346.41\text{ kW} = 400 \times 0.866$.

* **Reference in Theraja (Vol. II):** pp. 1219–1221
* **Reference in Chapman (5th Ed.):** pp. 116–118
* **Reference in Slide PDF:** Slide 99

---

### 113. Page 12, Q.3(c): Two 20 kVA transformers are connected in open - Δ to supply 230 V balanced 3-φ load. (i) what is the total load that can be supplied without overloading either transformer? (ii) when the Δ is closed by the addition of a third 20 kVA transformer, what total load can now be supplied?

**Part (i): Maximum Load in Open-Delta**
$$S_{\text{V}} = \sqrt{3} \times S_{\text{unit}} = \sqrt{3} \times 20\text{ kVA} \approx \mathbf{34.64\text{ kVA}}$$

**Part (ii): Maximum Load in Closed-Delta**
$$S_{\Delta} = 3 \times S_{\text{unit}} = 3 \times 20\text{ kVA} = \mathbf{60.00\text{ kVA}}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 114. Page 12, Q.5(a): Explain with necessary diagram, How 3-Φ, 4-wire connection can be used in T-connection. [Figure Involved]

* The primary and secondary windings are connected in T-configuration.
* Tapping the teaser winding at $\frac{1}{3}$ height from the junction with the main transformer creates the neutral terminal $N$.
* This neutral point provides equal phase voltages to all three line terminals, permitting standard 3-phase 4-wire power distribution.

* **Reference in Theraja (Vol. II):** pp. 1226–1228
* **Reference in Chapman (5th Ed.):** pp. 128–130
* **Reference in Slide PDF:** Slide 214

---

### 115. Page 40, Q.2(b): Prove that open-delta connection of transformer can be used for balanced 3-Φ supply, but capacity reduced to 57.7% compared to close-Δ connection.

* Refer to the step-by-step derivation in **Q.102** and **Q.108**:
  $$\frac{S_{\text{V}}}{S_{\Delta}} = \frac{\sqrt{3} V_L I_{ph}}{3 V_L I_{ph}} = \frac{1}{\sqrt{3}} \approx \mathbf{57.7\%}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---

### 116. Page 44, Q.2(c): Two transformers are required for a Scott connection operating from a 400V,3-Φ supply for supplying two 1-Φ furnaces at 220V on the 2-Φ side. If the total output is 150kVA.Calculate the secondary to primary turn ratio and the winding currents of each transformer.

**Given Data:**
* 3-Phase supply: $V_{L1} = 400\text{ V}$
* 2-Phase load: $V_2 = 220\text{ V}$, Total load $= 150\text{ kVA} \implies \text{Power per furnace} = 75\text{ kVA}$

**Step 1: Current Calculations**
* Secondary current of each transformer:
  $$I_2 = \frac{75,000}{220} = \mathbf{340.91\text{ A}}$$
* Primary line current:
  $$I_{L1} = \frac{150,000}{\sqrt{3} \times 400} = \mathbf{216.51\text{ A}}$$

**Step 2: Main Transformer Parameters**
* Primary voltage: $V_{1\text{M}} = 400\text{ V}$
* Turn ratio ($N_2/N_1$):
  $$K_{\text{Main}} = \frac{220}{400} = \mathbf{0.55}$$
* Primary current: $I_{1\text{M}} = \mathbf{216.51\text{ A}}$
* Secondary current: $I_{2\text{M}} = \mathbf{340.91\text{ A}}$

**Step 3: Teaser Transformer Parameters**
* Primary voltage: $V_{1\text{T}} = \frac{\sqrt{3}}{2} \times 400 = 346.41\text{ V}$
* Turn ratio ($N_2/N_1$):
  $$K_{\text{Teaser}} = \frac{220}{346.41} = \frac{0.55}{0.866} \approx \mathbf{0.635}$$
* Primary current: $I_{1\text{T}} = I_{L1} = \mathbf{216.51\text{ A}}$
* Secondary current: $I_{2\text{T}} = \mathbf{340.91\text{ A}}$

* **Reference in Theraja (Vol. II):** pp. 1228–1229
* **Reference in Chapman (5th Ed.):** pp. 131–132
* **Reference in Slide PDF:** Slide 214

---

### 117. Page 45, Q.4(c): Two 25 kVA transformer are connected in open-Δ to supply a 220V balanced 3-Φ load. (i) What is the total load that can be supplied without overloading either transformer? (ii) When the Δ is closed by the addition of a third 25 kVA transformer, what total load can now be supplied?

**Part (i): Maximum Load in Open-Delta**
$$S_{\text{V}} = \sqrt{3} \times 25\text{ kVA} \approx \mathbf{43.30\text{ kVA}}$$

**Part (ii): Maximum Load in Closed-Delta**
$$S_{\Delta} = 3 \times 25\text{ kVA} = \mathbf{75.00\text{ kVA}}$$

* **Reference in Theraja (Vol. II):** pp. 1218–1220
* **Reference in Chapman (5th Ed.):** pp. 115–118
* **Reference in Slide PDF:** Slides 96–100

---
