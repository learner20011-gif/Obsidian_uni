### **1. Overview of construction**

### 1. Page 2, Q.12: Name the different essential parts of a dc machine.

![[Pasted image 20260715001457.png]]

A DC machine consists of the following essential components:
1. **Yoke (Magnetic Frame):** Outer protective cast steel/iron frame that provides mechanical support and carries magnetic flux.
2. **Magnetic Poles:**
   * **Pole Core:** Carries field coils to create magnetic flux.
   * **Pole Shoe:** Spreads flux uniformly across the air gap and supports field coils.
3. **Field Winding:** Copper coils wound on pole cores to establish main working flux ($\Phi$).
4. **Armature Core:** Cylindrical laminated silicon-steel drum with slots that houses armature conductors and offers low reluctance path for flux.
5. **Armature Winding:** Insulated copper coils in slots where EMF is induced (generator) or torque is developed (motor).
6. **Commutator:** Cylindrical assembly of wedge-shaped copper segments insulated by mica; converts AC to DC (generator) or DC to AC (motor).
7. **Brushes & Brush Holders:** Carbon/graphite blocks that collect current from the rotating commutator to the external circuit.
8. **Bearings & Shaft:** Support the rotating assembly with minimal friction.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 4, 5, 6, 7, 8, 9, 10, 11 | Firoz Note: Page 129, 130 | Rosenblatt: Section 3-1, 3-2, 3-3, 3-4, 3-5, Pages 13-17 | Theraja Vol II: PDF Pages 32-34

***

### 2. Page 2, Q.13: What are the purposes of Field winding, Armature winding and brushes in d.c machine?

* **Field Winding:** Carries DC excitation current to produce the main working magnetic field ($\Phi$) across the air gap.
* **Armature Winding:** Serves as the active circuit where energy conversion occurs—flux cutting induces EMF (generator) or interaction with field flux produces mechanical torque (motor).
* **Brushes:** Form sliding electrical contact on the rotating commutator segments to collect current for external load (generator) or feed current into the armature (motor) without twisting external leads.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 7, 8, 10 | Firoz Note: Page 129, 130 | Rosenblatt: Section 3-2, 3-4, 3-5, Pages 14-17 | Theraja Vol II: PDF Pages 32-34

***

### 3. Page 2, Q.14: Why are carbon brushes preferred for dc machines?

Carbon (or electrographite) brushes are preferred over metal brushes for four key reasons:
1. **High Contact Resistance:** Smooths current reversal during commutation and suppresses spark formation.
2. **Self-Lubricating Property:** Soft graphite structure naturally lubricates contact, polishing the commutator and preventing abrasive wear.
3. **Negative Temperature Coefficient of Resistance:** Contact resistance decreases slightly as temperature rises, preventing excessive voltage drops under normal operating currents.
4. **Sacrificial Wear:** Carbon wears out gradually instead of eroding the expensive copper commutator segments, making replacements cheap and easy.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 10 | Firoz Note: Page 130 | Rosenblatt: Section 3-5, Page 17 | Theraja Vol II: PDF Page 34

***

### 4. Page 2, Q.15: Why the armature core in d.c machines is constructed with laminated steel sheets instead of solid steel sheets?

* **Cause:** The rotating armature continuously cuts magnetic flux, inducing internal eddy currents in the conducting iron core.
* **Loss Equation:** Eddy current loss is proportional to lamination thickness squared:
  $$P_e = k_e B_{\max}^2 f^2 t^2 V$$
* **Function of Laminations:** Thin sheets (0.4–0.5 mm) coated with insulating varnish break the core into high-resistance slices perpendicular to eddy current flow:
  * Restricts eddy currents to small loops within each sheet.
  * Drastically reduces $I^2R$ power loss and core heating.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 8 | Firoz Note: Page 129 | Rosenblatt: Section 3-3, Pages 14-15 | Theraja Vol II: PDF Pages 33-34

***

### 5. Page 2, Q.16: Why the armature core but not the magnetic pole core of a dc machine must be laminated?

* **Armature Core (Must be laminated):** Rotates past alternate North and South poles, subjecting the core iron to continuously alternating flux ($+B_{\max}$ to $-B_{\max}$). This high $d\Phi/dt$ induces massive eddy currents, necessitating thin laminated sheets.
* **Pole Core (Does not require lamination):** Fixed to the frame and excited by steady DC current, producing a constant, unidirectional magnetic flux. Since $d\Phi/dt \approx 0$, eddy currents are practically absent, so solid cast steel/forged steel is used (only pole shoes may be laminated to reduce slot-ripple losses).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 7, 8 | Firoz Note: Page 129, 130 | Rosenblatt: Section 3-2, 3-3, Pages 14-16 | Theraja Vol II: PDF Pages 32-34

***

### 6. Page 2, Q.17: Classify dc machines.

DC machines are classified based on field excitation method:
1. **Separately Excited DC Machines:** Field winding is energized by an independent external DC source.
2. **Self-Excited DC Machines:** Field winding is powered by the machine's own armature output:
   * **Shunt Wound:** Field winding in parallel with armature (high resistance, many turns of fine wire).
   * **Series Wound:** Field winding in series with armature (low resistance, few turns of thick wire).
   * **Compound Wound:** Contains both shunt and series field coils:
     * **Cumulative Compound:** Series flux aids shunt flux ($\Phi_{\text{total}} = \Phi_{sh} + \Phi_{se}$).
     * **Differential Compound:** Series flux opposes shunt flux ($\Phi_{\text{total}} = \Phi_{sh} - \Phi_{se}$).
     * **Connection Types:** Long Shunt (shunt across both armature and series field) vs. Short Shunt (shunt across armature only).
3. **Permanent Magnet DC Machines (PMDC):** Field flux provided by permanent magnets (no field coils).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 12, 13, 14, 15, 16 | Firoz Note: Page 132 | Rosenblatt: Section 4-2, 4-3, 4-4, 4-5, Pages 32-38 | Theraja Vol II: PDF Pages 35-37

***

### **2. Types of DC machines**

### 7. Page 2, Q.18: Name and describe the features of different types of dc generators.

| Generator Type | Field Connection | Terminal Voltage Characteristic | Primary Applications |
|---|---|---|---|
| **Separately Excited** | External DC source | Drops slightly with load due to $I_a R_a$ & armature reaction | Laboratory testing, Ward-Leonard speed control |
| **Shunt Generator** | Field parallel to armature | Drops moderately with load; requires residual magnetism to build up | Battery charging, ordinary lighting power |
| **Series Generator** | Field in series with armature | Rises steeply with load current; zero voltage at no-load | DC distribution boosters, constant-current arc lighting |
| **Cumulative Compound** | Series field aids shunt field | Voltage rises (Over), stays constant (Flat), or drops slightly (Under) | Power supply for long feeders, heavy industrial plant |
| **Differential Compound** | Series field opposes shunt field | Voltage collapses rapidly as load current increases | Arc welding (inherent short-circuit current limiting) |

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 12-16 | Firoz Note: Page 132 | Rosenblatt: Section 4-2 to 4-5, Pages 32-38 | Theraja Vol II: PDF Pages 35-37

***

### **3. Equivalent circuit of a DC generator**

### 8. Page 2, Q.19: Draw the equivalent electrical circuit of a dc generator. [Figure Involved]

#### Equivalent Circuits & Governing Equations

```
1. Separately Excited:
   +---[ Rf ]---+          +---(  Ea  )---+---[ Ra ]---+ (+ Vt)
   |            |          |     Gen      |            |
   +---( Vf )---+          +--------------+------------+ (- Vt)
   Vf = If * Rf            Vt = Ea - Ia*Ra - Vbrush

2. Shunt Generator:
        +-----------+---[ Ra ]---+---(+ Vt)
        |           |            |
      [Rsh]      (  Ea )         [ Load ]
        |           |            |
        +-----------+------------+---(- Vt)
   Ish = Vt / Rsh;  Ia = IL + Ish;  Vt = Ea - Ia*Ra

3. Long-Shunt Compound Generator:
        +---[ Rse ]---+---[ Ra ]---+---(+ Vt)
        |                          |
      [Rsh]                     (  Ea )
        |                          |
        +--------------------------+---(- Vt)
   Ia = IL + Ish;  Vt = Ea - Ia*(Ra + Rse)
```

* **Induced EMF:** $E_a = \frac{\Phi Z N P}{60 A}$
* **Terminal Voltage:** $V_t = E_a - I_a R_a - V_{\text{brush}}$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 17, 18, 19 | Firoz Note: Page 133, 134 | Rosenblatt: Section 4-2 to 4-5, Pages 32-38 | Theraja Vol II: PDF Pages 36-37

***

### **4. Lap and wave windings**

### 12. Page 3, Q.36: What is the pitch factor of a coil and commutator pitch?

* **Pitch Factor (Coil Pitch / Chording Factor $k_p$):** Ratio of vector EMF induced in a short-pitch coil to the EMF induced in a full-pitch coil:
  $$k_p = \cos\left(\frac{\alpha}{2}\right)$$
  *(where $\alpha$ is the chording angle by which coil span falls short of $180^\circ$ electrical).*
* **Commutator Pitch ($Y_c$):** Number of commutator segments spanned between the two ends of an armature coil:
  * For **Simplex Lap Winding:** $Y_c = \pm 1$ ($+1$ for progressive, $-1$ for retrogressive).
  * For **Simplex Wave Winding:** $Y_c = \frac{C \pm 1}{P/2}$ (where $C$ is number of coils, $P$ is poles).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 103, 115, 116 | Firoz Note: Page 147, 148 | Rosenblatt: Section 3-10, 3-14, Pages 22-28 | Theraja Vol II: PDF Pages 38, 47

***

### 13. Page 3, Q.37: Mention the two types of winding used in the dc machines. How do lap widings differ from wave windings?

The two standard types of armature windings are **Lap Winding** and **Wave Winding**.

| Feature | Lap Winding | Wave Winding |
|---|---|---|
| **Coil Connection** | Coil ends connect to adjacent commutator segments ($Y_c = \pm 1$) | Coil ends connect segments two pole pitches apart ($Y_c \approx 2C/P$) |
| **Parallel Paths ($A$)** | $A = m \cdot P$ ($A = P$ for simplex) | $A = 2 \cdot m$ ($A = 2$ for simplex, regardless of $P$) |
| **Current / Voltage** | High current, low voltage | Low current, high voltage |
| **Number of Brushes** | Equals number of poles ($P$) | Only 2 brushes required (can use $P$ for better current collection) |
| **Equalizer Rings** | Required to balance unequal parallel path currents | Not needed (conductors distribute evenly under all poles) |

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 100, 111 | Firoz Note: Page 142, 147 | Rosenblatt: Section 3-11, 3-14, Pages 23, 27 | Theraja Vol II: PDF Pages 40-49

***

### 14. Page 3, Q.38: What is the basic difference between lap winding and wave winding? Explain frog-leg winding.

* **Basic Difference:**
  * **Lap Winding:** Conductors form $P$ parallel paths ($A = P$); designed for low voltage, high current machines.
  * **Wave Winding:** Conductors form 2 parallel paths ($A = 2$); designed for high voltage, low current machines.
* **Frog-Leg Winding:**
  * A composite winding combining a **simplex lap winding** and a **multiplex wave winding** in the same armature slots, connected to the same commutator.
  * The wave winding acts as an internal, distributed equalizer network for the lap winding.
  * **Advantage:** Completely eliminates the need for external equalizer rings while retaining high current capacity and sparkless commutation.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 120 | Firoz Note: Page 149 | Rosenblatt: Section 3-16, Pages 28-29 | Theraja Vol II: PDF Page 50

***

### 15. Page 4, Q.39: What are equalizers? Why are they needed on lap-wound machine but not on a wave-wound machine?

* **Equalizer Rings:** Low-resistance copper conductors connecting points in an armature winding that are at equal potential.
* **Why Needed in Lap Winding ($A = P$):**
  * Minor variations in air-gap reluctance, bearing wear, or pole strengths induce unequal EMFs across the parallel paths.
  * This voltage imbalance drives large **circulating currents** through brushes, causing heavy sparking, commutator pitting, and core overheating. Equalizer rings bypass the brushes and equalize potential.
* **Why NOT Needed in Wave Winding ($A = 2$):**
  * Each parallel path consists of coil series distributed symmetrically under all magnetic poles.
  * Localized magnetic imbalances affect both paths identically, so path voltages remain equal and no circulating currents arise.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 109, 110 | Firoz Note: Page 145, 146 | Rosenblatt: Section 3-13, Pages 26-27 | Theraja Vol II: PDF Pages 44-46

***

### 16. Page 7, Q.4(c): Determine all the pitches for a duplex wave winding that is to be mounted on an armature with 139 slots that is to be installed in a dynamo with 6 poles.

**Given Data:**
* Winding type: Duplex wave winding ($m = 2$)
* Slots ($S$) = 139 $\implies$ Coils ($C$) = 139
* Poles ($P$) = 6

**Step 1: Commutator Pitch ($Y_c$)**
$$Y_c = \frac{C \pm m}{P/2} = \frac{139 \pm 2}{6/2} = \frac{139 \pm 2}{3}$$
* Progressive ($+$): $Y_c = \frac{141}{3} = \mathbf{47}$ (Integer $\implies$ valid)
* Retrogressive ($-$): $Y_c = \frac{137}{3} = 45.67$ (Non-integer $\implies$ invalid)

**Step 2: Average Pitch ($Y_A$)**
$$Y_A = Y_c = \mathbf{47}$$

**Step 3: Back Pitch ($Y_b$) and Front Pitch ($Y_f$)**
$$Y_A = \frac{Y_b + Y_f}{2} \implies Y_b + Y_f = 2 \times 47 = 94$$
Both $Y_b$ and $Y_f$ must be odd integers:
$$\mathbf{Y_b = 47, \quad Y_f = 47}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 115, 116 | Firoz Note: Page 147, 148 (Formula basis). | Rosenblatt: Section 3-14, Pages 27-28 | Theraja Vol II: PDF Pages 47-49

***

### 17. Page 12, Q.1(d): What is the essential difference between lap and wave windings? The armature of a 4 pole dc shunt generator is lap-wound and generates 216V when running at 600 rpm. Armature has 144 slots, with 6 conductors per slot. If this armature rewound to wave-connected, find the emf generated with the same flux per pole but running at 500 rpm.

![[Armature-Windings-of-DC-Generator-Lap-Wave-pptx-5-2048.webp]]

* **Essential Difference:** Lap winding has $A = P$ parallel paths (high-current, low-voltage), whereas wave winding has $A = 2$ parallel paths (high-voltage, low-current).

**Numerical Solution:**
* **EMF Formula:** $E = \frac{\Phi Z N P}{60 A} \implies E \propto \frac{N}{A}$ (since $\Phi, Z, P$ are constant).

**Given Data:**
* Case 1 (Lap): $P = 4$, $A_1 = P = 4$, $N_1 = 600\text{ rpm}$, $E_1 = 216\text{ V}$
* Case 2 (Wave): $A_2 = 2$, $N_2 = 500\text{ rpm}$, $E_2 = ?$

**Calculation:**
$$\frac{E_2}{E_1} = \left(\frac{N_2}{N_1}\right) \times \left(\frac{A_1}{A_2}\right)$$
$$\frac{E_2}{216} = \left(\frac{500}{600}\right) \times \left(\frac{4}{2}\right) = \left(\frac{5}{6}\right) \times 2 = \frac{10}{6}$$
$$E_2 = 216 \times \frac{10}{6} = \mathbf{360\text{ V}}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 100, 111, 125, 126 (EMF Equation) | Firoz Note: Page 25, 26. | Rosenblatt: Section 3-11, Page 23; Section 4-1, Pages 30-31 | Theraja Vol II: PDF Pages 57-58

***

### 18. Page 12, Q.2(a): Differentiate between lap winding and wave winding of a DC machine.

| Parameter | Lap Winding | Wave Winding |
|---|---|---|
| **Parallel Paths ($A$)** | $A = P$ (equals poles) | $A = 2$ (constant) |
| **Commutator Pitch ($Y_c$)** | $Y_c = \pm 1$ | $Y_c = \frac{C \pm 1}{P/2}$ |
| **Voltage & Current** | Low voltage, high current | High voltage, low current |
| **Equalizer Rings** | Essential to suppress circulating currents | Not required |
| **Brush Sets** | Requires $P$ brush sets | Only 2 brush sets strictly required |
| **EMF Generated** | Lower ($E \propto 1/P$) | Higher ($E \propto 1/2$) |

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 100, 111 | Firoz Note: Page 142, 147 | Rosenblatt: Section 3-11, 3-14, Pages 23, 27 | Theraja Vol II: PDF Pages 40-49

***

### 19. Page 25, CT#1 Q.2: Differentiate between lap and wave winding.

* **Lap Winding:**
  * Coil ends connect to adjacent commutator segments ($Y_c = \pm 1$).
  * Number of parallel paths $A = P$.
  * Best suited for **high current, low voltage** ratings.
  * Requires equalizer connections.
* **Wave Winding:**
  * Coil ends connect to segments approximately two pole pitches apart.
  * Number of parallel paths $A = 2$ regardless of poles.
  * Best suited for **high voltage, low current** ratings.
  * Does not require equalizer connections.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 100, 111 | Firoz Note: Page 142, 147 | Rosenblatt: Section 3-11, 3-14, Pages 23, 27 | Theraja Vol II: PDF Pages 40-49

***

### 20. Page 27, Q.2: A triplex wave winding is to be installed in a ... Determine all the pitches for a retrogressive winding. (Note: Text is partially cut off in the source image)

**General Formula & Solution Procedure:**
* **Given Parameters:** Triplex wave winding $\implies m = 3$; retrogressive $\implies$ minus sign ($-$).

1. **Commutator Pitch ($Y_c$):**
   $$Y_c = \frac{C - m}{P/2} = \frac{C - 3}{P/2}$$
   *(Must evaluate to an integer for a valid winding design).*
2. **Average Pitch ($Y_A$):**
   $$Y_A = Y_c$$
3. **Back & Front Pitches ($Y_b, Y_f$):**
   $$Y_b + Y_f = 2 Y_A$$
   * Select $Y_b$ and $Y_f$ as **odd integers** close to the pole pitch ($Z/P$).
   * If $Y_A$ is odd $\implies Y_b = Y_f = Y_A$.
   * If $Y_A$ is even $\implies Y_b = Y_A + 1$ and $Y_f = Y_A - 1$.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 115, 116 | Firoz Note: Page 147, 148. | Rosenblatt: Section 3-14, Pages 27-28 | Theraja Vol II: PDF Page 47

***

### **5. EMF equation of DC machines**

### 22. Page 2, Q.11: Show that the voltage generated by a dc generator is given by E =kφS where the symbols have their usual meaning.

**Derivation:**
* Let:
  * $\Phi$ = Flux per pole in Webers (Wb)
  * $P$ = Number of poles
  * $Z$ = Total number of armature conductors
  * $A$ = Number of parallel paths
  * $S$ = Armature speed in revolutions per second (rps) = $N/60$

1. **Flux cut by one conductor in one revolution:**
   $$d\Phi = P \cdot \Phi \text{ Wb}$$
2. **Time taken for one revolution:**
   $$dt = \frac{1}{S} \text{ seconds}$$
3. **Average EMF induced per conductor (Faraday's Law):**
   $$e_{\text{avg}} = \frac{d\Phi}{dt} = \frac{P\Phi}{1/S} = P \Phi S \text{ Volts}$$
4. **Total Generated EMF ($E$):**
   Since conductors in each parallel path are connected in series, number of conductors per path is $Z/A$:
   $$E = e_{\text{avg}} \times \left(\frac{Z}{A}\right) = (P \Phi S) \left(\frac{Z}{A}\right) = \left(\frac{P Z}{A}\right) \Phi S$$
5. Setting machine design constant $k = \frac{P Z}{A}$:
   $$\mathbf{E = k \Phi S}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 125, 126 | Firoz Note: Page 25, 26 | Rosenblatt: Section 4-1, Pages 30-31 | Theraja Vol II: PDF Pages 57-58

***

### 23. Page 12, Q.1(b): Show that the voltage generated by a dc generator is given by E = Kφω, where symbols have their usual meanings.

**Derivation:**
1. Standard EMF equation in terms of speed $N$ (rpm):
   $$E = \frac{\Phi Z N P}{60 A}$$
2. Angular velocity $\omega$ in rad/s:
   $$\omega = \frac{2\pi N}{60} \implies N = \frac{60 \omega}{2\pi}$$
3. Substitute $N$ into the EMF equation:
   $$E = \frac{\Phi Z P}{60 A} \left(\frac{60 \omega}{2\pi}\right) = \left(\frac{P Z}{2\pi A}\right) \Phi \omega$$
4. Defining machine constant $K = \frac{P Z}{2\pi A}$:
   $$\mathbf{E = K \Phi \omega}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 125, 126 | Firoz Note: Page 25, 26 | Rosenblatt: Section 4-1, Pages 30-31 | Theraja Vol II: PDF Pages 57-58

***

### 24. Page 12, Q.2(d): A simplex wave winding containing a total of 752 conductors is mounted on an armature rotating at 1800 r/min. If the dynamo has four poles, each with a flux of 600 kilolines, determine the generated voltage.

**Given Data:**
* Winding = Simplex wave $\implies A = 2$
* Conductors ($Z$) = 752
* Speed ($N$) = 1800 rpm
* Poles ($P$) = 4
* Flux ($\Phi$) = $600\text{ kilolines} = 600 \times 10^3 \times 10^{-8}\text{ Wb} = 0.006\text{ Wb}$

**Calculation:**
$$E = \frac{\Phi Z N P}{60 A} = \frac{0.006 \times 752 \times 1800 \times 4}{60 \times 2}$$
$$E = \frac{0.006 \times 752 \times 7200}{120} = 0.006 \times 752 \times 60 = \mathbf{270.72\text{ V}}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 125, 126 | Firoz Note: Page 25, 26. | Rosenblatt: Section 4-1, Pages 30-31 | Theraja Vol II: PDF Page 58

***

### 25. Page 26, Q.No.4: The armature of a 4 pole generator having simplex lap winding is rotating at 1200 rpm. If the total number of armature conductors is 2500 and the flux per pole is 250 kilolines, determine the generated voltage of a dc generator.

**Given Data:**
* Poles ($P$) = 4
* Winding = Simplex lap $\implies A = P = 4$
* Speed ($N$) = 1200 rpm
* Conductors ($Z$) = 2500
* Flux ($\Phi$) = $250\text{ kilolines} = 250 \times 10^3 \times 10^{-8}\text{ Wb} = 0.0025\text{ Wb}$

**Calculation:**
$$E = \frac{\Phi Z N P}{60 A} = \frac{0.0025 \times 2500 \times 1200 \times 4}{60 \times 4}$$
Since $A = P = 4$:
$$E = \frac{0.0025 \times 2500 \times 1200}{60} = 0.0025 \times 2500 \times 20 = 6.25 \times 20 = \mathbf{125\text{ V}}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 125, 126 | Firoz Note: Page 25, 26 | Rosenblatt: Section 4-1, Pages 30-31 | Theraja Vol II: PDF Page 58

***

### **6. Armature reaction in DC generators**

### 27. Page 4, Q.41: How does the armature reaction affect the performance of a dc machine? How do we avoid its effect in a dc machine?

![[Pasted image 20260714231849.png]]

![[Pasted image 20260715002834.png]]

* **Definition:** The distorting and weakening effect of armature MMF on the main field magnetic flux.
* **Effects on Performance:**
  1. **Flux Distortion (Cross-Magnetizing):** Weakens flux at leading pole tips and strengthens it at trailing pole tips. This shifts the Magnetic Neutral Axis (MNA) forward in the direction of rotation, causing severe brush sparking.
  2. **Net Flux Reduction (Demagnetizing):** Due to magnetic saturation at trailing pole tips, the flux gain is less than the flux lost at leading tips. This decreases total flux per pole, reducing generated EMF and terminal voltage under load.
  3. **Flashover Risk:** High voltage peaks between adjacent commutator segments can ignite an arc bridging segments.
* **Methods to Avoid/Mitigate:**
  * **Interpoles (Commutating Poles):** Neutralize cross-magnetizing armature flux in the interpolar commutation zone.
  * **Compensating Windings:** Embedded in pole shoes to directly cancel armature MMF under pole faces.
  * **Brush Shift:** Advance brushes to the new MNA (effective only at one fixed load).
  * **Increased Air Gap & Chamfered Pole Shoes:** Increases reluctance at pole tips to curb flux crowding.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 133, 134, 137, 138, 140 | Firoz Note: Page 150-153 | Rosenblatt: Section 5-1, 5-2, 5-3, Pages 42-45 | Theraja Vol II: PDF Pages 63-66

***

### 28. Page 4, Q.42: If the brushes are shifted to the new magnetic neutral, explain any effects or changes in the main-field flux.

![[Pasted image 20260715003637.png]]

When brushes are advanced by forward angle $\theta_m$ to align with the new MNA:
1. **Armature Conductors Divide into Two Groups:**
   * **Demagnetizing Conductors:** Contained within a total angle of $2\theta_m$ at both top and bottom axes. Their MMF acts in direct opposition ($180^\circ$) to the main pole field MMF:
     $$\text{Demagnetizing Ampere-Turns/pole: } AT_d = Z I_c \left(\frac{\theta_m}{360^\circ}\right)$$
   * **Cross-Magnetizing Conductors:** Contained within $(180^\circ - 2\theta_m)$. Their MMF acts at $90^\circ$ to distort the main field.
2. **Net Effect on Main Flux:**
   * Direct demagnetization occurs, actively reducing the main field flux ($\Phi$).
   * As a result, the generated voltage drops with increased load current.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 136, 137 | Firoz Note: Page 151, 152 | Rosenblatt: Section 5-2, Pages 43-44 | Theraja Vol II: PDF Pages 64-66

***

### 29. Page 4, Q.43: How compensating winding and interpoles can be used to minimize armature reaction?

* **Compensating Windings (Neutralize Cross-Magnetization under Pole Faces):**
  * Embedded in slots in the main pole shoes and connected in **series with the armature**.
  * Carries current in the **opposite direction** to the adjacent armature conductors.
  * Since armature current flows through both, compensating MMF automatically balances armature MMF at all loads, preventing field distortion and flux crowding.
* **Interpoles (Neutralize Cross-Magnetization in the Commutation Zone):**
  * Small auxiliary poles placed between main poles, connected in series with the armature.
  * Produces an MMF opposing armature MMF in the neutral zone, restoring local MNA to the geometric neutral axis.
  * Induces a rotational voltage in the commutating coil that exactly opposes the reactance voltage ($L di/dt$), ensuring sparkless commutation.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 138, 140, 144 | Firoz Note: Page 153, 155 | Rosenblatt: Section 5-3, 5-6, Pages 45-48 | Theraja Vol II: PDF Pages 66, 70-71

***

### 30. Page 8, Q.5(b): Define armature reaction. Describe its effects on a loaded generator.

* **Definition:** The interaction between the magnetic field produced by current-carrying armature conductors and the main magnetic field produced by field poles.
* **Effects on a Loaded Generator:**
  1. **Shifts MNA:** Shifts the Magnetic Neutral Axis in the direction of generator rotation, moving coil reversal away from the brushes and inducing sparking.
  2. **Demagnetization:** Magnetic saturation at pole tips reduces total flux per pole, causing generated EMF ($E_a$) and terminal voltage ($V_t$) to drop.
  3. **Commutator Flashover:** Distorted flux density creates high voltage spikes across adjacent segments, risking flashover arcs.
  4. **Iron Loss Increase:** Localized flux crowding at trailing tips increases iron core losses and heating.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 133, 134 | Firoz Note: Page 150 | Rosenblatt: Section 5-1, Pages 42-43 | Theraja Vol II: PDF Pages 63-65

***

### 31. Page 16, Q.4(a): How compensating winding and interpoles can be used to reduce armature reaction?

* **Compensating Winding:**
  * Located in pole face slots; connected in series with the armature.
  * Conductors carry current opposite to nearby armature conductors.
  * Directly neutralizes armature cross-magnetizing MMF beneath the pole shoes at all load levels, preventing flux distortion and saturation.
* **Interpoles:**
  * Narrow poles placed in the interpolar space between main poles.
  * Provide equal and opposite MMF to the armature in the commutation zone, pulling the MNA back to the geometric axis and neutralizing $L di/dt$ reactance voltage for clean commutation.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 138, 140, 144 | Firoz Note: Page 153, 155 | Rosenblatt: Section 5-3, 5-6, Pages 45-48 | Theraja Vol II: PDF Pages 66, 70-71

***

### 32. Page 25, CT-02 Q1: What is armature reaction? Describe three techniques of minimizing armature reaction.

* **Armature Reaction:** The effect of the armature magnetic field on the distribution and magnitude of the main field flux.
* **Three Techniques to Minimize:**
  1. **Interpoles (Commutating Poles):** Narrow auxiliary poles in the interpolar axis connected in series with the armature to cancel armature cross-field in the commutation region.
  2. **Compensating Windings:** Windings embedded in main pole faces carrying armature current in the opposite direction, canceling armature MMF directly beneath pole faces.
  3. **High Reluctance Pole Tips / Chamfered Shoes:** Chamfering pole shoe tips increases the air gap at the edges, curbing flux crowding and minimizing distortion.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 133, 138, 140 | Firoz Note: Page 150, 153 | Rosenblatt: Section 5-1, 5-3, Pages 42-45 | Theraja Vol II: PDF Pages 63-66

***

### 33. Page 26, Q.No.3: How compensating winding can be used to reduce armature reaction?

* **Principle:** Compensating windings are embedded in slots in the faces of the main pole shoes and connected in **series with the armature winding**.
* **Cancellation Mechanism:**
  * The windings carry current in the opposite direction to the armature conductors directly beneath them.
  * Because $I_{\text{comp}} \propto I_a$, the compensating MMF precisely matches and opposes the armature cross-magnetizing MMF at all load currents:
    $$AT_{\text{comp}} \approx AT_{\text{armature, pole-arc}}$$
  * This prevents flux distortion, eliminates flux crowding, and maintains uniform flux distribution across the pole shoe regardless of load variations.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 138, 140 | Firoz Note: Page 153 | Rosenblatt: Section 5-3, Pages 45-46 | Theraja Vol II: PDF Page 66

***

### **7. Commutation and methods of improving commutation**

### 35. Page 4, Q.44: What is commutation? Explain the methods to improve commutation.

* **Definition:** The process of reversing the direction of current in an armature coil as it is short-circuited by a brush and passes through the magnetic neutral zone.
* **Methods to Improve Commutation:**
  1. **Resistance Commutation (Using High-Resistance Brushes):**
     * Replacing copper brushes with **carbon/graphite brushes**.
     * As the brush leaves a segment, contact area shrinks, raising contact resistance. This forces short-circuit current to reverse smoothly through the leaving segment instead of arcing.
  2. **Voltage Commutation (Neutralizing Reactance Voltage):**
     * **Interpoles (Commutating Poles):** Auxiliary poles placed between main poles induce a speed voltage that opposes and cancels self-induced reactance voltage ($L di/dt$).
     * **Brush Shift:** Advancing brushes slightly beyond the MNA induces a small reversing voltage from the next pole (valid only for a specific fixed load).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 141, 142, 143, 144 | Firoz Note: Page 154, 155 | Rosenblatt: Section 5-4, 5-5, 5-6, Pages 46-49 | Theraja Vol II: PDF Pages 67-71

***

### 36. Page 4, Q.45: What happens to the magnitude and direction of the current in a coil as it undergoes commutation?

* **Initial State (Before Brush Contact):** Coil carries full path current $+I_c$ in one direction.
* **During Commutation Period ($T_c$):**
  * Brush short-circuits the coil across adjacent commutator segments.
  * Current decays from $+I_c$ to zero, then reverses direction toward $-I_c$.
* **Final State (After Brush Separates):**
  * Current reaches full magnitude in the opposite direction ($-I_c$).
* **Ideal vs. Poor Commutation:**
  * **Linear (Ideal) Commutation:** Current changes at a steady rate; achieves $-I_c$ exactly when brush leaves segment $\implies$ zero sparking.
  * **Under-Commutation (Delayed):** Coil inductance delays reversal. When brush separates, remaining current must jump across the air gap as an intense spark.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 141, 142 | Firoz Note: Page 154 | Rosenblatt: Section 5-4, Pages 46-47 | Theraja Vol II: PDF Pages 67-68

***

### 37. Page 4, Q.46: Explain the Ldi/dt voltage problem in conductors undergoing commutation. How can this problem be cancelled over a broad range of load?

* **The $L di/dt$ Problem (Reactance Voltage):**
  * An armature coil possesses self-inductance ($L$).
  * Reversing current from $+I_c$ to $-I_c$ in the brief commutation time $T_c$ creates a high rate of change ($di/dt = 2I_c / T_c$).
  * By Lenz's law, this induces a self-induced **reactance voltage**:
    $$e_r = L \frac{di}{dt}$$
  * This voltage opposes current reversal, delaying full commutation. When the brush disconnects from the segment, the trapped current arcs across the commutator bar edge, pitting the copper and causing severe brush wear.
* **Cancellation Over a Broad Range of Load:**
  * Install **Interpoles (Commutating Poles)** in the interpolar axis connected in **series with the armature**.
  * Interpoles induce a dynamic commutating voltage ($e_c = B_{\text{interpole}} l v$) in the coil that directly opposes $e_r$.
  * Since both $e_c \propto I_a$ and $e_r \propto I_a$, the opposing voltage automatically scales with load current, providing complete, automatic sparkless commutation from no-load to full-load.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 143, 144 | Firoz Note: Page 155 | Rosenblatt: Section 5-5, 5-6, Pages 47-49 | Theraja Vol II: PDF Pages 69-71

***

### 38. Page 12, Q.2(b): Explain the L di/dt voltage problem in conductors undergoing commutation.

* **Cause:** Armature coils are embedded in iron slots and have significant self-inductance $L$.
* **Mechanism:**
  * During commutation period $T_c$, current must reverse from $+I_c$ to $-I_c$.
  * The rapid change induces a reactance voltage:
    $$e_{\text{reactance}} = L \frac{di}{dt} = L \left(\frac{2I_c}{T_c}\right)$$
* **Consequence:** This EMF opposes the decay and reversal of current (Lenz's Law), resulting in **delayed (retarded) commutation**. The unreversed current is forced to jump across the retreating brush edge as a destructive spark.
* **Remedy:** Interpoles carrying armature current induce an equal and opposite voltage in the coil, neutralizing $L di/dt$ at all loads.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 143, 144 | Firoz Note: Page 155 | Rosenblatt: Section 5-5, 5-6, Pages 47-49 | Theraja Vol II: PDF Pages 69-71

***

### **8. Characteristics of DC generators**

### 40. Page 3, Q.31: Draw and explain the no-load (generated emf at no load versus field current) and load (generated emf at on load versus armature current) characteristics of DC shunt, series and compound generators. [Figure Involved]

![[Pasted image 20260715010455.png]]

#### 1. No-Load Magnetization Characteristic ($E_0$ vs. $I_f$)
* Common to all DC generators when run at constant rated speed with armature open.
* Starts at a non-zero voltage ($E_{\text{res}}$) due to **residual magnetism**.
* Increases linearly at low $I_f$ (air gap reluctance dominates).
* Bends over at the "knee" and flattens out due to **magnetic saturation** of iron cores.

#### 2. Load Characteristics ($E$ vs. $I_a$ or $V_t$ vs. $I_L$)

* **Shunt Generator:**
  ![[Pasted image 20260715021010.png]]
  ![[Pasted image 20260715015707.png]]
  * Voltage drops slightly as load increases due to:
    1. Armature resistance drop ($I_a R_a$).
    2. Armature reaction demagnetization.
    3. Drop in terminal voltage further reduces field current ($I_f = V_t / R_{sh}$), accelerating the voltage drop.

* **Series Generator:**
  ![[Pasted image 20260715021142.png]]
  ![[Pasted image 20260715021424.png]]
  * At no-load, voltage is only residual voltage ($E_{\text{res}}$).
  * As load current increases, field excitation rises ($I_{se} = I_L$), causing voltage to rise steeply until saturation.
  * Beyond saturation, voltage drops due to $I_a(R_a + R_{se})$ drop and armature reaction.

* **Compound Generator:**
  ![[Pasted image 20260715024155.png]]![[Pasted image 20260715024337.png]]
  * **Cumulative Compound:** Series flux aids shunt flux ($\Phi = \Phi_{sh} + \Phi_{se}$).
    * *Over-compounded:* Full-load voltage > No-load voltage.
    * *Flat-compounded:* Full-load voltage = No-load voltage.
    * *Under-compounded:* Full-load voltage < No-load voltage.
  * **Differential Compound:** Series flux opposes shunt flux ($\Phi = \Phi_{sh} - \Phi_{se}$).
    ![[Pasted image 20260715024213.png]]
    ![[Pasted image 20260715024741.png]]
    * Voltage drops drastically as load current increases; acts as a self-limiting constant-current source.

* **Figure involved:** Yes (Curves embedded above).
* **Related Topics:** Mam Slide: 147, 148, 149, 150, 151, 152 | Firoz Note: Page 27, 28, 29, 30 | Rosenblatt: Section 4-2, 4-3, 4-4, Pages 31-38 | Theraja Vol II: PDF Pages 118-124

***

### 41. Page 3, Q.32: Draw the terminal characteristics (Vt versus IL) curves for various types of dc generator in a single graph and compare them. [Figure Involved]

#### Terminal Characteristics Comparison ($V_t$ vs. $I_L$)

| Generator Type | Characteristic Curve Behavior | Reason |
|---|---|---|
| **Over-Compound** | Voltage rises with load ($V_{\text{FL}} > V_{\text{NL}}$) | Series field MMF overcompensates for $I_a R_a$ drop and armature reaction |
| **Flat-Compound** | Voltage remains constant ($V_{\text{FL}} = V_{\text{NL}}$) | Series field MMF exactly balances internal drops |
| **Under-Compound** | Voltage drops slightly ($V_{\text{FL}} < V_{\text{NL}}$) | Series field MMF partially compensates internal drops |
| **Separately Excited** | Moderate voltage droop | Drops only by $I_a R_a$ and armature reaction ($I_f$ is independent of $V_t$) |
| **Shunt Generator** | Significant voltage droop | $V_t$ drop lowers $I_f$, causing compound drop; breaks down past breakdown point |
| **Differential Compound** | Voltage collapses steeply | Series field opposes shunt field, destroying net flux as $I_L$ rises |
| **Series Generator** | Starts near zero, rises steeply, then droops past knee | Field excitation is proportional to load current $I_L$ |

![[Pasted image 20260715025633.png]]![[Pasted image 20260715025654.png]]
![[Pasted image 20260715025820.png]]

* **Figure involved:** Yes (Curves embedded above).
* **Related Topics:** Mam Slide: 153, 154 | Firoz Note: Page 31, 32 | Rosenblatt: Section 4-5, Pages 37-38 | Theraja Vol II: PDF Pages 123-125

***

### 42. Page 12, Q.1(c): Draw the terminal voltage versus load current curves of various types of dc generator in a single graph and compare them. [Figure Involved]

* **Comparison of External Characteristics ($V_t$ vs. $I_L$):**
  1. **Over-compounded:** $V_t$ rises above no-load voltage as $I_L$ increases (compensates line drop in distant loads).
  2. **Flat-compounded:** $V_t$ remains virtually constant from no-load to full-load.
  3. **Under-compounded:** $V_t$ falls slightly with load.
  4. **Shunt:** $V_t$ drops moderately due to $I_a R_a$, armature reaction, and decreasing shunt excitation.
  5. **Differential Compound:** $V_t$ plummets sharply due to opposing series field flux; ideal for electric arc welding.
  6. **Series:** $V_t$ starts from residual voltage and rises sharply with $I_L$ before saturation curvature.

* **Figure involved:** None (Refer to graphs in Q.41).
* **Related Topics:** Mam Slide: 153, 154 | Firoz Note: Page 31, 32 | Rosenblatt: Section 4-5, Pages 37-38 | Theraja Vol II: PDF Pages 123-125

***

### **9. Separately excited DC generator**

### 44. Page 2, Q.20: What do you mean by residual flux in DC generator? Explain magnetization characteristics of a separately excited dc generator?

* **Residual Flux:** The small remnant magnetic flux ($\Phi_{\text{res}}$) retained in the ferromagnetic field poles when field excitation current is zero ($I_f = 0$), caused by magnetic hysteresis.
* **Magnetization Characteristic (OCC Curve, $E_0$ vs. $I_f$):**
  * Obtained by running generator at constant rated speed with open-circuit armature while varying $I_f$ via external source.
  * **Initial Residual Point ($I_f = 0$):** Induces small residual voltage $E_{\text{res}} \approx 2\text{--}10\text{ V}$.
  * **Linear Region:** Air gap dominates magnetic reluctance; flux $\Phi \propto I_f \implies E_0 \propto I_f$.
  * **Knee & Saturation Region:** Field iron begins to saturate; incremental $I_f$ produces diminishing flux gains, causing curve to bend horizontally.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 128, 129, 130 | Firoz Note: Page 26, 27 | Rosenblatt: Section 4-2, Pages 31-33 | Theraja Vol II: PDF Pages 114-115

***

### 45. Page 3, Q.21: Why is the emf not zero when the field current is reduced to zero in dc generator?

* **Cause (Magnetic Retentivity / Hysteresis):**
  * The field pole cores are made of ferromagnetic materials (cast steel or forged iron).
  * Due to magnetic retentivity, magnetic dipoles do not completely randomize when excitation current drops to zero.
  * A small **residual magnetic flux** ($\Phi_{\text{res}}$) remains locked in the pole iron.
* **Resulting EMF:**
  * As the armature is driven by the prime mover at rated speed $N$, it cuts this residual flux.
  * By Faraday's Law, an EMF is induced:
    $$E_{\text{res}} = \frac{\Phi_{\text{res}} Z N P}{60 A} > 0$$
  * Typically yields a residual terminal voltage of **2 to 12 Volts**.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 128, 129 | Firoz Note: Page 26 | Rosenblatt: Section 4-2, Page 31 | Theraja Vol II: PDF Page 114

***

### **10. Voltage build-up in self-excited generator**

### 47. Page 3, Q.22: What are the conditions to be fulfilled for a shunt generator to build up voltage?

![[Pasted image 20260715035244.png]]

Four mandatory conditions must be fulfilled:
1. **Residual Magnetism:** Pole cores must possess sufficient residual magnetic flux ($\Phi_{\text{res}} > 0$).
2. **Proper Polarity (Aiding Flux):** Field coils must be connected such that current produced by residual EMF creates flux that **aids** (reinforces) residual flux.
3. **Field Resistance < Critical Resistance ($R_f < R_c$):** Total field circuit resistance must be strictly less than the critical resistance at operating speed.
4. **Speed > Critical Speed ($N > N_c$):** Prime mover speed must exceed the critical speed for the given field resistance.

* **Figure involved:** Yes (Diagram embedded above).
* **Related Topics:** Mam Slide: 168 | Firoz Note: Page 33 | Rosenblatt: Section 4-3, Pages 33-35 | Theraja Vol II: PDF Pages 116-117

***

### 48. Page 3, Q.23: With necessary sketch, describe the voltage build-up process of a self-excited dc generator. [Figure Involved]

#### Voltage Build-Up Mechanism (Step-by-Step)
1. **Initial Voltage:** Armature rotates through residual flux $\Phi_{\text{res}}$, inducing small voltage $E_0$ (2–10 V).
2. **Initial Current:** $E_0$ forces small current $I_{f1} = E_0 / R_f$ through the shunt field winding.
3. **Flux Reinforcement:** Field connections ensure $I_{f1}$ creates aiding MMF, increasing total flux to $\Phi_1$.
4. **Higher EMF:** The larger flux $\Phi_1$ induces higher armature voltage $E_1$.
5. **Cumulative Growth:** Higher $E_1$ forces larger field current $I_{f2}$, producing further flux gain. This cumulative process continues climbing the OCC curve.
6. **Equilibrium Point:** Growth terminates at point $P$ where the field resistance line ($V = I_f R_f$) intersects the OCC curve. At this point, the generated EMF exactly matches the voltage drop across field resistance ($E_a = I_f R_f$). Iron core saturation prevents infinite voltage buildup.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 169, 170 | Firoz Note: Page 33, 34 | Rosenblatt: Section 4-3, Pages 33-35 | Theraja Vol II: PDF Pages 115-116

***

### 49. Page 3, Q.24: What is meant by critical resistance? What is the significance of critical resistance in a self excited shunt generator?

* **Definition:** Critical field resistance ($R_c$) is the maximum field circuit resistance at which a self-excited generator will build up voltage at a given speed. Graphically, it is the **slope of the tangent** drawn from the origin to the initial linear portion of the OCC.
* **Significance:**
  * **Threshold for Voltage Build-up:**
    * If $R_f < R_c$: Field line intersects OCC in the saturation region $\implies$ Generator builds up to rated voltage.
    * If $R_f > R_c$: Field line lies above the OCC and only intersects near the origin $\implies$ Generator fails to build up and remains at residual voltage ($E_{\text{res}}$).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 171, 172 | Firoz Note: Page 34 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Pages 116-117

***

### 50. Page 3, Q.25: Why critical resistance is important? How it helps in the voltage buildup process?

* **Why Important:** It defines the physical boundary condition for self-excitation. It dictates the maximum external rheostat resistance allowable in the field loop during machine start-up.
* **Role in Voltage Build-up:**
  * For voltage build-up, each increment of induced EMF must exceed the $I_f R_f$ drop:
    $$\Delta E = E_{\text{induced}} - I_f R_f > 0$$
  * Ensuring $R_f < R_c$ guarantees that the OCC curve sits above the field resistance line in the linear zone, producing a positive net voltage ($\Delta E$) that drives additional field current until saturation is reached.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 171, 172 | Firoz Note: Page 34 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Pages 116-117

***

### 51. Page 3, Q.26: Explain why a dc generator fails to build-up voltage on starting. How can these problems be minimized?

| Failure Cause | Root Mechanism | Remedy / Minimization |
|---|---|---|
| **No Residual Magnetism** | Core completely demagnetized by heat, vibration, or prolonged idle | **Field Flashing:** Connect field briefly to an external DC battery to restore residual flux |
| **Reversed Field Connections** | Field flux opposes residual flux, driving net flux to zero | Reverse the shunt field winding lead connections |
| **Reversed Direction of Rotation** | Induces reverse EMF, canceling residual flux | Reverse rotation or swap field terminals |
| **Field Resistance > Critical Resistance ($R_f > R_c$)** | Field line slope exceeds linear OCC slope; cannot intersect saturation | Reduce field rheostat resistance until $R_f < R_c$ |
| **Speed Below Critical Speed ($N < N_c$)** | Flattens OCC curve below field line | Increase prime mover speed to rated value |

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 173 | Firoz Note: Page 35 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Page 117

***

### 52. Page 3, Q.27: Explain the process of determining the critical value of field resistance of a shunt generator from its magnetization curve.

1. **Plot the OCC Curve:** Run the generator at rated constant speed on open circuit. Plot induced voltage ($E_0$) on the vertical axis versus field current ($I_f$) on the horizontal axis.
2. **Draw Tangent Line (Air-Gap Line):** From the origin $(0,0)$, draw a straight line tangent to the initial linear, unsaturated portion of the OCC curve.
3. **Calculate Slope:** Select any convenient point $(I_f, E_0)$ on this tangent line.
4. **Determine $R_c$:** The critical resistance equals the slope of this tangent line:
   $$R_c = \frac{E_0}{I_f} \quad (\Omega)$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 171, 172 | Firoz Note: Page 34 | Rosenblatt: Section 4-3, Page 34 | Theraja Vol II: PDF Pages 116-117

***

### 53. Page 7, Q.4(a): Explain the voltage build-up procedure of a self-excited DC generator.

* **Mechanism:**
  1. Driven by prime mover at rated speed, residual flux $\Phi_{\text{res}}$ generates initial EMF ($E_0 \approx 2\text{--}10\text{ V}$).
  2. $E_0$ circulates small current $I_f = E_0 / R_f$ through the field coils.
  3. Proper field connection produces aiding flux ($\Phi_{\text{total}} = \Phi_{\text{res}} + \Delta \Phi$), raising induced voltage to $E_1$.
  4. Increased $E_1$ drives higher $I_{f2}$, initiating cumulative voltage growth along the OCC.
  5. Voltage stabilizes where field resistance line ($V = I_f R_f$) intersects the saturated portion of the OCC curve.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 169, 170 | Firoz Note: Page 33, 34 | Rosenblatt: Section 4-3, Pages 33-35 | Theraja Vol II: PDF Pages 115-116

***

### 54. Page 7, Q.4(b): What are the reasons a DC generator may fails to build up and what are its remedies.

* **Reasons & Remedies:**
  1. **Absence of Residual Magnetism:**
     * *Remedy:* Flash the field by applying DC voltage from a battery across the field winding for a few seconds.
  2. **Reversed Field Connections:**
     * *Remedy:* Disconnect and reverse the field terminal leads ($F_1$ and $F_2$).
  3. **Reversed Rotation:**
     * *Remedy:* Reverse prime mover direction or swap field terminals.
  4. **Field Resistance Too High ($R_f > R_c$):**
     * *Remedy:* Cut out resistance from the field rheostat.
  5. **Speed Too Low ($N < N_c$):**
     * *Remedy:* Bring prime mover up to rated speed.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 173 | Firoz Note: Page 35 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Page 117

***

### 55. Page 8, Q.6(a): Define critical resistance. Explain the significance of critical resistance in a self-excited shunt generator.

* **Definition:** The maximum permissible total resistance of the field circuit at a specified speed above which the generator fails to self-excite. It equals the slope of the tangent to the open-circuit magnetization curve.
* **Significance:**
  * If $R_f < R_c$: System is unstable at low voltages and drives itself up to stable intersection in the saturation zone.
  * If $R_f > R_c$: Voltage buildup cannot start; machine only outputs residual voltage.
  * Formula relation: $R_c \propto N$ (critical resistance varies directly with speed).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 171, 172 | Firoz Note: Page 34 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Pages 116-117

***

### 56. Page 9, Q.3(a): Explain no load magnetization curve.

* **Definition:** Graph showing relationship between no-load generated voltage ($E_0$) and field exciting current ($I_f$) at a constant rotational speed.
* **Key Regions:**
  1. **Residual EMF:** At $I_f = 0$, $E_0 > 0$ due to residual magnetism.
  2. **Air-Gap Line (Linear Zone):** Reluctance of air gap dominates $\implies$ flux is directly proportional to field MMF ($E_0 \propto I_f$).
  3. **Knee:** Magnetic saturation begins in teeth and pole shoes.
  4. **Saturation Zone:** Iron reluctance dominates; curve bends sharply and flattens.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 128-130 | Firoz Note: Page 26-27 | Rosenblatt: Section 4-2, Pages 31-33 | Theraja Vol II: PDF Pages 114-115

***

### 57. Page 12, Q.1(a): What part does the residual magnetism play in “build-up” process? When does “build-up” process stop?

* **Role of Residual Magnetism:**
  * It provides the initial "seed" magnetic flux needed to generate the starting EMF ($E_0$).
  * Without this seed voltage, no initial field current can flow in a self-excited generator, making self-excitation impossible.
* **When Build-Up Stops:**
  * Stops at the intersection point of the OCC curve and the field resistance line ($V = I_f R_f$).
  * Beyond this point, magnetic saturation limits generated EMF such that additional field current would require more voltage than the machine generates ($E_a < I_f R_f$).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 168-170 | Firoz Note: Page 33-34 | Rosenblatt: Section 4-3, Pages 33-35 | Theraja Vol II: PDF Pages 115-116

***

### 58. Page 12, Q.1(c): The open circuit characteristic (OCC) of a dc machine when running at 1000 rpm is given below: Field current (A) If : 0, 0.5, 1, 2, 3, 4, 5. Induced voltage (V) Ea : 10, 60, 120, 200, 232, 248, 258. (i) What is the source of induced voltage at zero field current? What do we do if there is no induced voltage at zero field current in the operation of shunt generator? (ii) What is critical resistance? Find the critical resistance of the shunt generator having the OCC given above. (iii) Determine the shunt field resistance required to obtain an open circuit voltage of 250 V.

#### (i) Source of Voltage at Zero Field Current & Remedy
* **Source:** The 10 V induced at $I_f = 0\text{ A}$ originates from **residual magnetism** retained in the iron poles from earlier operation.
* **Remedy if Absent:** Perform **field flashing**—briefly connect an external DC battery to the field winding to re-magnetize the pole cores.

#### (ii) Critical Resistance ($R_c$) Calculation
* **Definition:** Maximum field resistance for voltage build-up, equal to the slope of the linear tangent from the origin.
* **From OCC Data (Linear portion):**
  * At $I_f = 0.5\text{ A}$, $E_a = 60\text{ V}$
  * At $I_f = 1.0\text{ A}$, $E_a = 120\text{ V}$
* **Calculation:**
  $$R_c = \frac{\Delta E_a}{\Delta I_f} = \frac{120\text{ V}}{1.0\text{ A}} = \mathbf{120\ \Omega}$$

#### (iii) Field Resistance Required for Open Circuit Voltage of 250 V
* From the OCC data:
  * At $I_f = 4\text{ A} \implies E_a = 248\text{ V}$
  * At $I_f = 5\text{ A} \implies E_a = 258\text{ V}$
* Linear interpolation for $E_a = 250\text{ V}$:
  $$I_{f(250)} = 4 + \left(\frac{250 - 248}{258 - 248}\right) \times (5 - 4) = 4 + \frac{2}{10} = 4.2\text{ A}$$
* Operating field resistance:
  $$R_f = \frac{V}{I_f} = \frac{250\text{ V}}{4.2\text{ A}} \approx \mathbf{59.52\ \Omega}$$

* **Figure involved:** Yes (Plotting OCC and resistance lines recommended).
* **Related Topics:** Mam Slide: 130, 133, 172 | Firoz Note: Page 33, 34 | Rosenblatt: Sections 4-2, 4-5, Pages 31-33, 35-36 | Theraja Vol II: PDF Pages 115-117

***

### 59. Page 13, Q.1(a): What are the causes of a DC shunt generator not to build-up voltage? How can these problems be minimized?

* **Causes & Solutions:**
  1. **Loss of Residual Magnetism:** Re-establish flux via **field flashing** from a DC source.
  2. **Field Connections Reversed:** Swap shunt field winding leads ($F_1, F_2$) so field flux aids residual flux.
  3. **High Field Resistance ($R_f > R_c$):** Reduce field rheostat resistance below $R_c$.
  4. **Low Speed ($N < N_c$):** Increase prime mover speed to rated value.
  5. **Load Connected During Start:** Start generator on **no-load (open circuit)** to prevent load current from pulling terminal voltage down before excitation builds up.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 173 | Firoz Note: Page 35 | Rosenblatt: Section 4-3, Pages 34-35 | Theraja Vol II: PDF Page 117

***

### **11. DC shunt, DC series and DC compound generator characteristics**

### 61. Page 3, Q.28: “Though the dc generator operates above the knee of the magnetization curve, yet the terminal voltage reduces with the increased load”-why?

Terminal voltage ($V_t = E_a - I_a R_a$) decreases under load due to three distinct factors:
1. **Armature Circuit Resistance Drop ($I_a R_a$):** Ohmic internal voltage drop increases directly with load current $I_a$.
2. **Armature Reaction Demagnetization:** While the machine operates above the saturation knee, cross-magnetization causes severe localized saturation at trailing pole tips. The flux gained at saturated trailing tips is less than the flux lost at unsaturated leading tips, causing a net reduction in working flux per pole ($\Phi$) and lowering $E_a$.
3. **Decreased Field Excitation (in Shunt Generators):** As terminal voltage droops, shunt field current ($I_{sh} = V_t / R_{sh}$) drops simultaneously, causing a secondary decline in main field flux.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 147, 148 | Firoz Note: Page 27, 28 | Rosenblatt: Section 4-3, Pages 33-35 | Theraja Vol II: PDF Page 118

***

### 62. Page 3, Q.29: “The generator with the smallest percent voltage regulation is generally more desirable”- do you agree with this statement? Comment on your answer.

* **Agreement for General Power Supply:**
  * **Agreed:** For general lighting, residential, and commercial distribution, **minimum percent voltage regulation** (ideal = 0%, as in Flat-Compounded generators) is highly desirable because terminal voltage remains constant without requiring active field rheostat adjustments as consumer loads turn on and off.
* **Exceptions Where High or Negative Regulation is Desirable:**
  1. **Electric Arc Welding (Differential Compound):** Requires very high **positive voltage regulation** (steep voltage collapse) to limit short-circuit current when the electrode touches the workpiece.
  2. **Long-Distance Feeders (Over-Compound):** Requires **negative voltage regulation** ($V_{\text{FL}} > V_{\text{NL}}$) so the voltage rise at generator terminals compensates for the ohmic line drop ($I R_{\text{line}}$) along distant transmission cables.
  3. **Distribution Boosters (Series Generator):** High rising characteristic is required to boost line voltage proportionally with load current.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 153, 154 | Firoz Note: Page 31, 32 | Rosenblatt: Section 4-5, 4-13, Pages 37-38, 45-46 | Theraja Vol II: PDF Pages 123-125

***

### 63. Page 3, Q.30: Explain how can you determine whether the generator is connected as a differential compound generator or as a cumulative compound generator.

* **Method 1: Load Test (Observation of Terminal Voltage)**
  * Run the generator at rated speed and record no-load voltage $V_{\text{NL}}$.
  * Gradually apply electrical load.
  * **Cumulative Compound:** Terminal voltage remains constant (flat), rises (over), or drops slightly (under).
  * **Differential Compound:** Terminal voltage drops **drastically and rapidly** even under modest loads.
* **Method 2: Separate Winding Polarity Test**
  * Disconnect the series field and run machine as a pure shunt generator; observe polarity of induced terminal voltage.
  * Disconnect shunt field and run machine temporarily as a series generator (or excite series field with a battery); observe terminal voltage polarity.
  * If both windings produce identical terminal polarity $\implies$ **Cumulative Compound**.
  * If polarities oppose each other $\implies$ **Differential Compound**.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 150, 151, 152 | Firoz Note: Page 29, 30 | Rosenblatt: Section 4-4, Pages 36-37 | Theraja Vol II: PDF Pages 122-124

***

### 64. Page 3, Q.33: What causes the extraordinarily fast voltage drop with increasing load in differentially compounded dc generator?

* **Opposing Flux Alignment:** The series field winding is connected such that its MMF directly opposes the shunt field MMF:
  $$\Phi_{\text{net}} = \Phi_{sh} - \Phi_{se}$$
* **Rapid Collapse Mechanism:**
  1. As load current ($I_L \approx I_a$) increases, series field current rises directly.
  2. The opposing series flux $\Phi_{se} = N_{se} I_a / \mathcal{R}$ increases proportionally.
  3. This drastically subtracts from the shunt flux, collapsing total flux per pole ($\Phi_{\text{net}}$).
  4. Induced EMF ($E_a \propto \Phi_{\text{net}} N$) plunges, which in turn reduces terminal voltage $V_t$.
  5. The collapsed $V_t$ further weakens the shunt field current ($I_{sh} = V_t / R_{sh}$), completely collapsing the machine voltage.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 151 | Firoz Note: Page 30 | Rosenblatt: Section 4-4, Pages 36-37 | Theraja Vol II: PDF Page 123

***

### 65. Page 3, Q.34: Write down applications of all DC generators.

1. **DC Shunt Generator:**
   * Battery charging and emergency power banks.
   * Ordinary lighting loads and general local DC power supplies.
   * Field exciter for synchronous alternators.
2. **DC Series Generator:**
   * Line voltage boosters in DC transmission systems.
   * Constant-current series street arc-lighting systems.
3. **Cumulative Compound Generator:**
   * **Over-compounded:** Heavy industrial plants and power transmission over long distribution feeders to cancel line drops.
   * **Flat-compounded:** Office buildings, schools, and hospitals requiring constant supply voltage without external regulators.
4. **Differential Compound Generator:**
   * Electric arc welding (inherent self-limiting short-circuit current).
5. **Separately Excited DC Generator:**
   * Electrical testing laboratories and Ward-Leonard motor speed control drives requiring wide-range voltage control.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 155 | Firoz Note: Page 32 | Rosenblatt: Section 4-14, Pages 46-47 | Theraja Vol II: PDF Page 126

***

### 66. Page 8, Q.5(c): A shunt generator supplies 96 A at a terminal voltage of 200 V. The armature and shunt field resistances are 0.1 $\Omega$ and 50 $\Omega$ respectively. The iron and frictional losses are 2500 W. Find (i) EMF generated (ii) Cu losses (iii) Commercial efficiency

**Given Data:**
* Terminal Voltage ($V_t$) = 200 V
* Load Current ($I_L$) = 96 A
* Armature Resistance ($R_a$) = 0.1 $\Omega$
* Shunt Field Resistance ($R_{sh}$) = 50 $\Omega$
* Stray Losses (Iron + Friction) = 2500 W

**Step 1: Current Calculations**
* Shunt field current:
  $$I_{sh} = \frac{V_t}{R_{sh}} = \frac{200}{50} = 4\text{ A}$$
* Armature current:
  $$I_a = I_L + I_{sh} = 96 + 4 = 100\text{ A}$$

**Part (i): Generated EMF ($E_g$)**
$$E_g = V_t + I_a R_a = 200 + (100 \times 0.1) = 200 + 10 = \mathbf{210\text{ V}}$$

**Part (ii): Copper Losses**
* Armature Cu loss:
  $$P_{cu,a} = I_a^2 R_a = (100)^2 \times 0.1 = 10,000 \times 0.1 = 1000\text{ W}$$
* Shunt field Cu loss:
  $$P_{cu,sh} = V_t \times I_{sh} = 200 \times 4 = 800\text{ W}$$
* Total Copper Loss:
  $$P_{cu,\text{total}} = 1000 + 800 = \mathbf{1800\text{ W}}$$

**Part (iii): Commercial Efficiency ($\eta_c$)**
* Electrical output power:
  $$P_{\text{out}} = V_t \times I_L = 200 \times 96 = 19,200\text{ W}$$
* Total losses:
  $$P_{\text{loss}} = \text{Cu Loss} + \text{Stray Loss} = 1800 + 2500 = 4300\text{ W}$$
* Total input mechanical power:
  $$P_{\text{in}} = P_{\text{out}} + P_{\text{loss}} = 19,200 + 4300 = 23,500\text{ W}$$
* Efficiency:
  $$\eta_c = \left(\frac{P_{\text{out}}}{P_{\text{in}}}\right) \times 100\% = \left(\frac{19200}{23500}\right) \times 100\% \approx \mathbf{81.7\%}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 145, 199, 204, 205 | Firoz Note: Page 36, 126 | Rosenblatt: Section 10-2, Pages 108-109 | Theraja Vol II: PDF Page 70

***

### 67. Page 8, Q.6(c): Briefly Describe the characteristics of shunt, over compound, flat compound, under compound and differential compound generator.

* **Shunt Generator:** Terminal voltage falls moderately with increasing load due to $I_a R_a$ drop, armature reaction, and accompanying reduction in shunt field excitation.
* **Over-Compound Generator:** Series field MMF is stronger than internal voltage drops. Terminal voltage at full load is higher than at no load ($V_{\text{FL}} > V_{\text{NL}}$), compensating for line drops.
* **Flat-Compound Generator:** Series field MMF exactly balances armature resistance drop and armature reaction. Terminal voltage remains practically constant from no-load to full-load ($V_{\text{FL}} = V_{\text{NL}}$).
* **Under-Compound Generator:** Series field MMF only partially compensates internal drops. Terminal voltage falls slightly with load ($V_{\text{FL}} < V_{\text{NL}}$), but less than in a pure shunt generator.
* **Differential Compound Generator:** Series field opposes shunt field ($\Phi_{\text{net}} = \Phi_{sh} - \Phi_{se}$). Terminal voltage collapses steeply with load, providing an inherently safe, self-limiting current profile.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 153, 154 | Firoz Note: Page 31, 32 | Rosenblatt: Section 4-5, Pages 37-38 | Theraja Vol II: PDF Pages 123-125

***

### 68. Page 8, Q.6(d): A 100 kW, 600 V compound generator requires an increment of 2.3 A shunt field current to raise the terminal voltage to 625 V while supplying a current of 13 A. If the shunt field has 400 turns per pole and series field has 7.5 turns per pole. If the series field resistance 0.009 $\Omega$, calculate the resistance of the diverter.

**Analysis of Typographical Data in Prompt:**
* Full-load rated current of a 100 kW, 600 V generator is $I_{\text{FL}} = 100,000 / 600 = 166.67\text{ A}$. The "13 A" text in the exam paper is a typo for full load ($166.67\text{ A}$) or $130\text{ A}$. Both solutions are provided below.

**Given Parameters:**
* $\Delta I_{sh} = 2.3\text{ A}$
* $N_{sh} = 400\text{ turns/pole}$
* $N_{se} = 7.5\text{ turns/pole}$
* $R_{se} = 0.009\ \Omega$

**Step 1: Required Additional Ampere-Turns (AT)**
$$\Delta AT = \Delta I_{sh} \times N_{sh} = 2.3 \times 400 = 920\text{ AT/pole}$$

**Step 2: Required Series Field Current ($I_{se}$)**
$$I_{se} = \frac{\Delta AT}{N_{se}} = \frac{920}{7.5} = 122.67\text{ A}$$

**Step 3: Diverter Resistance ($R_d$) Calculation**
* **Case A: Assuming rated full-load current ($I_{\text{total}} = 166.67\text{ A}$):**
  * Current through diverter:
    $$I_d = I_{\text{total}} - I_{se} = 166.67 - 122.67 = 44.0\text{ A}$$
  * Parallel circuit equality ($I_d R_d = I_{se} R_{se}$):
    $$R_d = \frac{I_{se} R_{se}}{I_d} = \frac{122.67 \times 0.009}{44.0} = \frac{1.104}{44.0} \approx \mathbf{0.0251\ \Omega}$$
* **Case B: Assuming intended load was 130 A:**
  * $I_d = 130 - 122.67 = 7.33\text{ A}$
  * $R_d = \frac{1.104}{7.33} \approx \mathbf{0.1506\ \Omega}$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 161, 289, 290 | Firoz Note: Page 49, 50 (Similar numerical Example 5.7). | Rosenblatt: Section 4-13, Pages 45-46 | Theraja Vol II: PDF Pages 129-131

***

### 69. Page 10, Q.8(a): What do you mean by negative voltage regulation? Which generator tends to exhibit negative voltage regulation?

* **Definition:** Voltage regulation is defined as:
  $$\% \text{VR} = \frac{V_{\text{NL}} - V_{\text{FL}}}{V_{\text{FL}}} \times 100\%$$
  **Negative Voltage Regulation** occurs when the terminal voltage at full load exceeds the terminal voltage at no load ($V_{\text{FL}} > V_{\text{NL}}$), resulting in a negative percentage value.
* **Generator Exhibiting Negative Voltage Regulation:**
  * **Over-Compounded DC Generator:** The series field winding adds sufficient MMF under load to not only counteract armature drops but actively raise the working magnetic flux, driving terminal voltage higher as load current increases.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 153 | Firoz Note: Page 31 | Rosenblatt: Section 4-5, Page 37 | Theraja Vol II: PDF Page 123

***

### 70. Page 10, Q.8(d): A long shunt compound generator has a shunt field winding of 1000 turns/pole and series field winding of 4 turns/pole and resistance of 0.05 $\Omega$. In order to obtain the rated voltage both at no-load and full-load for operation as shunt generator, it is necessary to increase field current by 0.2 A. The full load armature current of compound generator is 80 A. Calculate the driver [diverter] resistance connected in parallel with series field to obtain flat compound operation.

**Given Data:**
* $N_{sh} = 1000\text{ turns/pole}$
* $N_{se} = 4\text{ turns/pole}$
* $R_{se} = 0.05\ \Omega$
* $\Delta I_f = 0.2\text{ A}$
* Full-load armature current ($I_a$) = 80 A

**Step 1: Additional Ampere-Turns Required for Flat Compounding**
$$\Delta AT = \Delta I_f \times N_{sh} = 0.2 \times 1000 = 200\text{ AT/pole}$$

**Step 2: Series Field Current Required ($I_{se}$)**
$$I_{se} = \frac{\Delta AT}{N_{se}} = \frac{200}{4} = 50\text{ A}$$

**Step 3: Diverter Current ($I_d$)**
$$I_d = I_a - I_{se} = 80 - 50 = 30\text{ A}$$

**Step 4: Diverter Resistance ($R_d$)**
Since the diverter is in parallel with the series field winding:
$$I_d R_d = I_{se} R_{se}$$
$$30 \times R_d = 50 \times 0.05 = 2.5\text{ V}$$
$$R_d = \frac{2.5}{30} \approx \mathbf{0.0833\ \Omega}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 161, 289, 290 | Firoz Note: Page 49, 50 | Rosenblatt: Section 4-13, Pages 45-46 | Theraja Vol II: PDF Pages 129-131

***

### 71. Page 12, Q.1(b): Why does the field winding of a series dc machine have less number of turns than that of dc shunt machine?

* **Design Basis (MMF Requirement: $AT = I \times N$):**
  * **Series Machine:** Field winding is connected in series with the armature and carries the entire heavy load current ($I_{se} = I_L \approx 20\text{--}500\text{ A}$). Because current is already massive, very few turns ($N_{se}$) are needed to produce the required magnetic flux. Furthermore, few turns of thick wire keep winding resistance and internal $I^2 R_{se}$ voltage drop minimal.
  * **Shunt Machine:** Field winding is connected across the full terminal voltage ($V_t$). To prevent drawing excessive power and overheating, the winding must have a high resistance. This is achieved by using **thousands of turns ($N_{sh}$) of very fine copper wire**, drawing only a small current (1–5% of rated current).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 7, 13, 14 | Firoz Note: Page 129, 132 | Rosenblatt: Section 3-2, 4-3, 4-4, Pages 14, 33-36 | Theraja Vol II: PDF Page 35

***

### 72. Page 12, Q.2(c): Explain the control procedures of terminal voltage of cumulatively compounded DC Generator.

Terminal voltage of a cumulatively compounded generator is controlled via three primary methods:
1. **Shunt Field Rheostat Adjustment:**
   * Adjusting the rheostat in series with the shunt field controls $I_{sh}$, setting the base no-load terminal voltage ($V_{\text{NL}}$).
2. **Series Field Diverter Resistor (Degree of Compounding):**
   * A variable low-resistance diverter resistor ($R_d$) placed in parallel with the series field controls the fraction of armature current bypassed away from the series coils.
   * Decreasing diverter resistance weakens series compounding (transitions from over-compounded to flat or under-compounded); increasing diverter resistance strengthens series boost.
3. **Prime Mover Speed Variation:**
   * Adjusting generator rotational speed alters both induced EMF ($E_a \propto N$) and terminal voltage directly.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 161 | Firoz Note: Page 49, 50 | Rosenblatt: Section 4-13, Pages 45-46 | Theraja Vol II: PDF Pages 129-131

***

### 73. Page 12, Q.2(d): In a long-shunt compound generator, the terminal voltage is 230 V when generator delivers 150 A. determine (i) Induced emf, & (ii) distribution of generator power. Given that, shunt field, series field, diverter, and armature resistance are 92 $\Omega$, 0.015 $\Omega$, 0.03 $\Omega$, and 0.032 $\Omega$, respectively.

**Given Data:**
* $V_t = 230\text{ V}$, $I_L = 150\text{ A}$
* $R_{sh} = 92\ \Omega$, $R_{se} = 0.015\ \Omega$, $R_{\text{div}} = 0.03\ \Omega$, $R_a = 0.032\ \Omega$

**Step 1: Circuit Current Calculations**
* Shunt field current:
  $$I_{sh} = \frac{V_t}{R_{sh}} = \frac{230}{92} = 2.5\text{ A}$$
* Total armature current:
  $$I_a = I_L + I_{sh} = 150 + 2.5 = 152.5\text{ A}$$
* Equivalent parallel resistance of series field and diverter:
  $$R_p = \frac{R_{se} \times R_{\text{div}}}{R_{se} + R_{\text{div}}} = \frac{0.015 \times 0.03}{0.015 + 0.03} = \frac{0.00045}{0.045} = 0.01\ \Omega$$

**Part (i): Induced EMF ($E_g$)**
$$E_g = V_t + I_a(R_a + R_p) = 230 + 152.5 \times (0.032 + 0.01) = 230 + (152.5 \times 0.042) = 230 + 6.405 = \mathbf{236.405\text{ V}}$$

**Part (ii): Distribution of Generator Power**
1. **Total Armature Power Generated:**
   $$P_{\text{gen}} = E_g \times I_a = 236.405 \times 152.5 = \mathbf{36,051.76\text{ W}} \quad (36.05\text{ kW})$$
2. **Useful Electrical Power Delivered to Load:**
   $$P_{\text{out}} = V_t \times I_L = 230 \times 150 = \mathbf{34,500.00\text{ W}} \quad (34.50\text{ kW})$$
3. **Internal Power Losses:**
   * Armature Copper Loss:
     $$P_{cu,a} = I_a^2 R_a = (152.5)^2 \times 0.032 = 23,256.25 \times 0.032 = \mathbf{744.20\text{ W}}$$
   * Series Field & Diverter Combined Loss:
     $$P_{cu,se} = I_a^2 R_p = (152.5)^2 \times 0.01 = \mathbf{232.56\text{ W}}$$
   * Shunt Field Copper Loss:
     $$P_{cu,sh} = V_t \times I_{sh} = 230 \times 2.5 = \mathbf{575.00\text{ W}}$$
   * *Check:* $P_{\text{out}} + \text{Losses} = 34,500 + 744.20 + 232.56 + 575.00 = 36,051.76\text{ W} = P_{\text{gen}}$.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 145, 161 | Firoz Note: Page 36, 49 | Rosenblatt: Section 4-13, Pages 45-46 | Theraja Vol II: PDF Page 70

***

### 74. Page 13, Q.1(c): A 250 kW, 230 V, four-pole shunt generator requires a field excitation of 2.7 A when delivering a rated load of 150 A. A field current of 5.0 A is necessary to raise the terminal voltage to desired value at rated load. If the shunt field has 500 turns/pole and series field 10 turns/pole, find the value of diverted resistance when the generator is to operate as a cumulative compound generator. Assume resistance of series field is 0.006 $\Omega$.

**Given Data:**
* Rated load current ($I_L$) = 150 A
* Initial field current ($I_{f1}$) = 2.7 A
* Required field current ($I_{f2}$) = 5.0 A
* $\Delta I_f = 5.0 - 2.7 = 2.3\text{ A}$
* $N_{sh} = 500\text{ turns/pole}$, $N_{se} = 10\text{ turns/pole}$
* $R_{se} = 0.006\ \Omega$

**Step 1: Additional MMF Required**
$$\Delta AT = \Delta I_f \times N_{sh} = 2.3 \times 500 = 1150\text{ AT/pole}$$

**Step 2: Required Series Field Current ($I_{se}$)**
$$I_{se} = \frac{\Delta AT}{N_{se}} = \frac{1150}{10} = 115\text{ A}$$

**Step 3: Diverter Current ($I_d$)**
$$I_d = I_L - I_{se} = 150 - 115 = 35\text{ A}$$

**Step 4: Diverter Resistance ($R_d$)**
$$I_d R_d = I_{se} R_{se}$$
$$35 \times R_d = 115 \times 0.006 = 0.69\text{ V}$$
$$R_d = \frac{0.69}{35} \approx \mathbf{0.0197\ \Omega}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 161, 289, 290 | Firoz Note: Page 49, 50 | Rosenblatt: Section 4-13, Pages 45-46 | Theraja Vol II: PDF Pages 129-131

***

### 75. Page 14, Q.3(d): A 25kW, 250V dc shunt generator has armature and field resistances of 0.08$\Omega$ and 110$\Omega$ respectively. Determine the total armature power developed when working (i) as a generator delivering 25kW output and (ii) as a motor taking 25kW input.

**Given Data:**
* Rated Power ($P$) = 25,000 W, Terminal Voltage ($V_t$) = 250 V
* $R_a = 0.08\ \Omega$, $R_{sh} = 110\ \Omega$
* Line current: $I_L = 25000 / 250 = 100\text{ A}$
* Shunt field current: $I_{sh} = 250 / 110 \approx 2.273\text{ A}$

#### Case (i): Generator Delivering 25 kW Output
* Armature current:
  $$I_a = I_L + I_{sh} = 100 + 2.273 = 102.273\text{ A}$$
* Generated EMF:
  $$E_g = V_t + I_a R_a = 250 + (102.273 \times 0.08) = 250 + 8.182 = 258.182\text{ V}$$
* Total Armature Power Developed:
  $$P_{g,\text{dev}} = E_g \times I_a = 258.182 \times 102.273 \approx \mathbf{26,405\text{ W}} \quad (26.405\text{ kW})$$

#### Case (ii): Motor Taking 25 kW Input
* Armature current:
  $$I_a = I_L - I_{sh} = 100 - 2.273 = 97.727\text{ A}$$
* Back EMF:
  $$E_b = V_t - I_a R_a = 250 - (97.727 \times 0.08) = 250 - 7.818 = 242.182\text{ V}$$
* Total Armature Power Developed (Mechanical Power):
  $$P_{m,\text{dev}} = E_b \times I_a = 242.182 \times 97.727 \approx \mathbf{23,667\text{ W}} \quad (23.667\text{ kW})$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 145, 224, 247 | Firoz Note: Page 36, 80, 83 | Rosenblatt: Section 10-3, Page 109 | Theraja Vol II: PDF Page 70

***

### 76. Page 25, CT-02 Q.2: A shunt generator delivers 190 A at terminal voltage 250V, the armature resistance and shunt field resistance are 0.02$\Omega$ and 60$\Omega$, respectively. Find the generated EMF, Cu losses and efficiency of the generator.

**Given Data:**
* $V_t = 250\text{ V}$, $I_L = 190\text{ A}$, $R_a = 0.02\ \Omega$, $R_{sh} = 60\ \Omega$

**Step 1: Current Calculations**
* $I_{sh} = \frac{V_t}{R_{sh}} = \frac{250}{60} \approx 4.167\text{ A}$
* $I_a = I_L + I_{sh} = 190 + 4.167 = 194.167\text{ A}$

**Part (i): Generated EMF ($E_g$)**
$$E_g = V_t + I_a R_a = 250 + (194.167 \times 0.02) = 250 + 3.883 = \mathbf{253.883\text{ V}}$$

**Part (ii): Copper Losses**
* Armature Cu loss: $P_{cu,a} = I_a^2 R_a = (194.167)^2 \times 0.02 \approx 754.02\text{ W}$
* Shunt field Cu loss: $P_{cu,sh} = V_t \times I_{sh} = 250 \times 4.167 \approx 1041.75\text{ W}$
* Total Copper Losses:
  $$P_{cu,\text{total}} = 754.02 + 1041.75 = \mathbf{1795.77\text{ W}} \quad (\approx 1.80\text{ kW})$$

**Part (iii): Electrical Efficiency ($\eta$)**
* Output Power: $P_{\text{out}} = V_t \times I_L = 250 \times 190 = 47,500\text{ W}$
* Input Power (neglecting stray losses): $P_{\text{in}} = P_{\text{out}} + P_{cu} = 47,500 + 1795.77 = 49,295.77\text{ W}$
* Efficiency:
  $$\eta = \left(\frac{47,500}{49,295.77}\right) \times 100\% \approx \mathbf{96.36\%}$$

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 145, 199, 204, 205 | Firoz Note: Page 36, 126 | Rosenblatt: Sections 10-2, 10-8, Pages 108-109, 113-114 | Theraja Vol II: PDF Page 70

***

### **12. Parallel operation of DC generators**

### 78. Page 4, Q.47: Why the terminal voltage of the incoming generator is a few volts greater than that of the running generator?

* **Prevention of Motoring Action:** If the incoming generator's voltage were equal to or slightly lower than the busbar voltage, closing the paralleling switch would cause it to draw current from the busbars, turning it into a motor that drives its prime mover (potentially damaging the engine/turbine).
* **Smooth Load Pick-Up:** Setting the incoming EMF 1 to 2 Volts higher ensures that upon switch closure, it immediately delivers a small positive forward current into the system, establishing stable generator operation.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 174, 175 | Firoz Note: Page 39 | Rosenblatt: Section 4-15, Pages 47-49 | Theraja Vol II: PDF Pages 132-133

***

### 79. Page 4, Q.48: With an aid of a circuit diagram, describe the procedure for paralleling two DC shunt generators and for transferring the load from one machine to the other. [Figure Involved]

#### Circuit Diagram

```
(+) Busbar =============================================== (+)
                   |                                 |
                 [CB1]                             [CB2]
                   |                                 |
            +------+------+                   +------+------+
            |             |                   |             |
          (Ea1)         [Rsh1]              (Ea2)         [Rsh2]
            |      (Running) |                |     (Incoming)|
            +------+------+                   +------+------+
                   |                                 |
(-) Busbar =============================================== (-)
```

#### Paralleling Procedure
1. **Speed Up:** Bring incoming machine (Gen 2) up to rated speed via prime mover.
2. **Voltage Match:** Adjust field rheostat of Gen 2 until its terminal voltage is 1–2 V higher than the common busbar voltage.
3. **Connect to Bus:** Close the circuit breaker (CB2). Gen 2 floats on the busbars, delivering minimal current.

#### Load Transfer Procedure
* To transfer load from Gen 1 to Gen 2:
  1. Strengthen Gen 2 field rheostat (raises induced EMF $E_{a2}$), increasing its share of load current.
  2. Simultaneously weaken Gen 1 field rheostat (lowers $E_{a1}$), decreasing its current.
  3. Maintain constant busbar voltage throughout the adjustment.
  4. Continue until Gen 1 delivers zero current, then safely open CB1 to remove Gen 1 from service.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 174, 175, 176 | Firoz Note: Page 39, 40 | Rosenblatt: Section 4-15, Pages 47-49 | Theraja Vol II: PDF Pages 132-134

***

### 80. Page 4, Q.49: “Load sharing of shunt generator is inherently stable”- justify the statement.

* **Inherent Drooping Characteristic:** DC shunt generators have a naturally drooping terminal voltage characteristic ($V_t$ drops as $I_a$ increases).
* **Self-Stabilizing Mechanism:**
  * Suppose two identical shunt generators operate in parallel. If Gen 1 momentarily attempts to grab more load current:
    $$\Delta I_{a1} \uparrow \implies V_{t1} \downarrow$$
  * Because the machines are tied to common busbars ($V_{\text{bus}}$), a reduction in Gen 1's terminal EMF causes its share of load current to drop:
    $$I_{a1} = \frac{E_{a1} - V_{\text{bus}}}{R_{a1}} \downarrow$$
  * The excess load automatically shifts over to Gen 2.
* **Conclusion:** Any load disturbance is naturally and automatically dampened out, ensuring inherently stable parallel operation without requiring auxiliary equalizers.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 177 | Firoz Note: Page 41 | Rosenblatt: Section 4-16, Pages 49-50 | Theraja Vol II: PDF Page 134

***

### 81. Page 4, Q.50: What are the requirements of connecting two over compound generators in parallel?

1. **Equal Terminal Voltage & Polarity:** Open-circuit voltages must match busbar voltage, with identical polarity.
2. **Identical External Characteristics:** Generators should have identical percentage voltage regulation so load divides proportionally.
3. **Equalizer Bus (Mandatory):** A low-resistance equalizer connection must join the armature-series field junctions of both machines.
4. **Series Field Placement:** Series field windings of both machines must be connected on the same side of the armature (either all on the positive side or all on the negative side).

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 178, 179 | Firoz Note: Page 42, 43 | Rosenblatt: Section 4-17, Pages 50-52 | Theraja Vol II: PDF Pages 135-136

***

### 82. Page 4, Q.51: Show that the load sharing of compound generators is not stable. How stability can be achieved?

* **Why Unstable (Cumulative Runaway):**
  * Over-compound generators have a **rising terminal voltage characteristic**.
  * If Gen 1 takes slightly more load current ($I_{a1} \uparrow$):
    $$I_{se1} \uparrow \implies \Phi_{se1} \uparrow \implies E_{a1} \uparrow \implies V_{t1} \uparrow$$
  * Higher voltage forces Gen 1 to take even more load, while Gen 2 sheds load.
  * This cumulative process continues until Gen 1 trips on over-current, and Gen 2 reverses current, running as a differential compound motor with risk of runaway destruction.
* **How Stability is Achieved (Equalizer Bar):**
  * Install an **Equalizer Bus**—a heavy, low-resistance copper bar connecting the junction between armature and series winding of both machines.
  * The equalizer places both series field windings in **parallel with each other**.
  * Any sudden surge in load current divides between the series windings in inverse proportion to their resistances, regardless of which armature produced the current.
  * This prevents either machine from increasing its field strength relative to the other, guaranteeing stable parallel operation.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 178, 179 | Firoz Note: Page 42, 43 | Rosenblatt: Section 4-17, Pages 50-52 | Theraja Vol II: PDF Pages 135-136

***

### 83. Page 8, Q.5(a): Shunt generator parallel operation is inherently stable but compound generators are not – why? How it can be made stable?

* **Shunt Generators (Inherently Stable):** Drooping voltage characteristics create self-correcting negative feedback: if a generator takes more load, its terminal voltage drops, automatically shedding excess load back to the other machine.
* **Compound Generators (Inherently Unstable):** Rising voltage characteristics create positive feedback: taking more load increases series flux, raising voltage and drawing even more load until one generator motors and trips the system.
* **Stabilization:** Connecting an **Equalizer Bus** across the series field windings forces current surges to divide equally across both series fields, neutralizing voltage runaway and stabilizing load sharing.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 177, 178 | Firoz Note: Page 41, 42 | Rosenblatt: Section 4-16, 4-17, Pages 49-52 | Theraja Vol II: PDF Pages 134-136

***

### 84. Page 10, Q.8(b): The parallel operation of shunt generators is inherently stable; however compound generators are not – why. How the parallel operation of compound generator can make stable?

* **Shunt Machine Stability:** Drooping external characteristic ($V_t$ drops as $I_L$ rises) ensures automatic load redistribution if one generator surges.
* **Compound Machine Instability:** Rising external characteristic causes positive feedback: higher current $\implies$ higher series field flux $\implies$ higher EMF $\implies$ runaway load grabbing.
* **Remedy:** Connect a low-resistance **equalizer connection** connecting the positive brushes (or armature-series field junctions) of both machines. This ensures both series coils share any current fluctuations equally.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 177, 178 | Firoz Note: Page 41, 42 | Rosenblatt: Section 4-16, 4-17, Pages 49-52 | Theraja Vol II: PDF Pages 134-136

***

### 85. Page 13, Q.4(c): Explain how can you determine whether the generator is connected as a differential compound generator or as a cumulative compound generator. Load sharing of compound generators is not stable. How can this be made stable?

* **Part 1: Determining Compounding Type:**
  * Apply load to the generator while running at rated speed:
    * If terminal voltage stays flat, rises, or droops gently $\implies$ **Cumulative Compound**.
    * If terminal voltage drops abruptly and dramatically to zero $\implies$ **Differential Compound**.
* **Part 2: Stabilizing Parallel Compound Generators:**
  * Cumulative compound generators in parallel are unstable due to their rising voltage characteristics.
  * **Stability Solution:** Connect an **Equalizer Bus** of negligible resistance across the armature-series field junctions. This puts the series fields in parallel, forcing load changes to distribute equally across both field windings and eliminating runaway.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: 151, 152, 178, 179 | Firoz Note: Page 30, 42, 43 | Rosenblatt: Section 4-4, 4-17, Pages 36-37, 50-52 | Theraja Vol II: PDF Pages 123, 135-136

***

### **1. Universal motor**

### 87. Page 8, Q.8(b): Define universal motor. Differentiate universal motor from a dc series motor and also mention its applications.

* **Definition:** A modified series-wound motor designed to operate with similar performance and speed-torque characteristics on either direct current (DC) or single-phase alternating current (AC).
* **Key Differences from Standard DC Series Motor:**

| Feature | Universal Motor | DC Series Motor |
|---|---|---|
| **Core Construction** | Both stator and rotor cores are fully laminated to minimize AC eddy current losses | Stator yoke and poles are solid cast steel (only armature is laminated) |
| **Field Winding** | Fewer turns to minimize inductive reactance ($X_L$) and improve power factor on AC | Many turns to maximize field flux |
| **Air Gap** | Extremely small air gap to minimize magnetic reluctance and magnetizing current | Moderate air gap |
| **Commutation** | Uses compensating windings and high-resistance brushes to suppress AC transformer sparking | Relies primarily on resistance commutation |

* **Applications:**
  * Domestic appliances: blenders, food processors, vacuum cleaners, sewing machines.
  * Portable power tools: electric drills, circular saws, angle grinders, routers.

* **Figure involved:** None.
* **Related Topics:** Mam Slide: N/A | Firoz Note: Page 156-158 | Rosenblatt: Section 17-1, 17-2, Pages 195-198 | Theraja Vol II: PDF Pages 1400-1405

***

### **2. Stepper motor**

### 89. Page 10, Q.8(c): What is stepper motor? What are its applications? Draw the truth table and corresponding applied voltage waveforms to make the stepper motor step 30^0. [Figure Involved]

* **Definition:** An electromechanical device that converts digital electrical pulses into precise, discrete mechanical angular increments (steps) in open-loop systems without feedback encoders.
* **Applications:**
  * 3D printers and CNC engraving machines.
  * Robotics joints and pick-and-place automation arms.
  * Computer disk drive head actuators and optical scanners.
  * Camera autofocus and zoom lens mechanisms.

#### Design for $30^\circ$ Step Angle
* **Configuration:** 3-Phase Variable Reluctance (VR) Stepper Motor with 6 stator poles and 4 rotor teeth:
  * Stator Pole Pitch: $360^\circ / 6 = 60^\circ$
  * Rotor Tooth Pitch: $360^\circ / 4 = 90^\circ$
  * Step Angle: $\beta = |60^\circ - 90^\circ| = \mathbf{30^\circ}$

#### Truth Table (3-Phase Full-Step Sequence: A $\rightarrow$ B $\rightarrow$ C)

| Step | Phase A | Phase B | Phase C | Rotor Position |
|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | $0^\circ$ |
| **2** | 0 | 1 | 0 | $30^\circ$ |
| **3** | 0 | 0 | 1 | $60^\circ$ |
| **4** | 1 | 0 | 0 | $90^\circ$ |
| **5** | 0 | 1 | 0 | $120^\circ$ |

#### Applied Voltage Waveforms

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

* **Figure involved:** Yes (Timing waveforms and truth table illustrated above).
* **Related Topics:** Mam Slide: N/A | Firoz Note: N/A | Rosenblatt: Chapter 18 | Theraja Vol II: Special Machines Chapter

***
