### **1. Principles of Electromechanical Energy Conversion**

### Page 5, Q.68: Prove that the electrical power converted into mechanical power is equal to the product of the counter emf and the armature current.

**Proof:**
* **Voltage Equation of DC Motor:**
  $$V = E_b + I_a R_a$$
  *(where $V$ = applied terminal voltage, $E_b$ = counter/back EMF, $I_a$ = armature current, $R_a$ = armature resistance).*

* **Multiply both sides by $I_a$:**
  $$V I_a = E_b I_a + I_a^2 R_a$$

* **Physical Meaning of each term:**
  1. **$V I_a$:** Total electrical power supplied to the armature.
  2. **$I_a^2 R_a$:** Electrical power lost as heat (armature copper loss).
  3. **$E_b I_a$:** Remaining power after subtracting internal copper losses.

* **Conclusion:** By conservation of energy, the electrical power converted into gross mechanical power ($P_m$) is:
  $$P_m = E_b I_a$$

* **Figures involved:** None.
* **References:** Mam Slide: 222-224, Firoz Note: 80-83.

---

### Page 14, Q.3(b): Prove that the gross mechanical power developed by a DC motor is maximum when back emf is equal to half of the applied voltage.

**Proof:**
* **Gross Mechanical Power:**
  $$P_m = E_b I_a$$

* From motor voltage equation $V = E_b + I_a R_a$, isolate $I_a$:
  $$I_a = \frac{V - E_b}{R_a}$$

* Substitute $I_a$ into power equation:
  $$P_m = E_b \left(\frac{V - E_b}{R_a}\right) = \frac{V E_b - E_b^2}{R_a}$$

* **Condition for Maximum Power:** Differentiate $P_m$ with respect to $E_b$ and set to zero:
  $$\frac{dP_m}{dE_b} = \frac{V - 2E_b}{R_a} = 0$$
  $$V - 2E_b = 0 \implies 2E_b = V \implies E_b = \frac{V}{2}$$

* **Second Derivative Test:**
  $$\frac{d^2P_m}{dE_b^2} = -\frac{2}{R_a} < 0 \quad (\text{Confirms maximum})$$

* **Conclusion:** Gross mechanical power developed is maximum when back EMF equals half of the supply voltage ($E_b = V/2$).
* *(Practical Note: This condition is not used practically because efficiency is only 50% and drawing such massive current causes severe overheating).*

* **Figures involved:** None.
* **References:** Mam Slide: 225, Firoz Note: 85-86.

---

### Page 31, Q.6(c): Prove that, Pm= (1-s)P2 where the symbols have their usual meanings.

**Proof:**
* **Symbol Definitions:**
  * $P_2$ = Rotor input power (air-gap power).
  * $P_m$ = Gross mechanical power developed by rotor.
  * $P_{cr}$ = Rotor copper loss.
  * $s$ = Fractional slip.

* **Power Relationship:**
  * Rotor copper loss is directly proportional to slip:
    $$P_{cr} = s P_2$$
  * Mechanical power developed is the rotor input minus copper loss:
    $$P_m = P_2 - P_{cr}$$

* **Substitution:**
  $$P_m = P_2 - s P_2 = P_2 (1 - s)$$

* **Conclusion:**
  $$P_m = (1 - s) P_2 \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 34, Q.6(b): Explain the relationship between rotor efficiency and slip of an induction motor.

**Explanation:**
* **Definition of Rotor Efficiency:** Ratio of gross mechanical power developed ($P_m$) to rotor input power ($P_2$):
  $$\text{Rotor Efficiency} = \frac{P_m}{P_2}$$

* Since $P_m = P_2(1 - s)$:
  $$\text{Rotor Efficiency} = \frac{P_2(1 - s)}{P_2} = 1 - s \quad (\text{or } (1 - s) \times 100\%)$$

* **Key Points:**
  1. **Inverse Proportionality:** As slip ($s$) increases, rotor efficiency ($1 - s$) decreases.
  2. **At Standstill ($s = 1$):** Rotor efficiency = $0\%$ (all rotor input power converts into $I^2R$ copper loss heat).
  3. **Normal Running ($s \approx 0.02 \text{--} 0.05$):** Slip is very small, so rotor efficiency remains very high ($95\% \text{--} 98\%$).

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 38, Q.6(b): Show that, P2:Pm:Pcr=1:(1-s):s, where P2, Pm and Pcr are respectively the power delivered to the rotor, the gross mechanical power and the rotor core loss.

*(Note: In standard theory, $P_{cr}$ denotes Rotor Copper Loss ($I^2R$ loss), as rotor core losses are negligible at low slip frequencies).*

**Proof:**
* **Power Components:**
  1. Power delivered to rotor (air-gap power) = $P_2$
  2. Rotor copper loss = $P_{cr} = s P_2$
  3. Gross mechanical power = $P_m = P_2 - P_{cr} = P_2(1 - s)$

* **Set up the Ratio:**
  $$P_2 : P_m : P_{cr} = P_2 : P_2(1 - s) : s P_2$$

* **Divide throughout by $P_2$:**
  $$P_2 : P_m : P_{cr} = 1 : (1 - s) : s \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 42, Q.6(c): Explain the power flow diagram and prove that Pm=(1-S)P2, for induction motor. [Figure Involved]

**1. Power Flow Diagram Stages:**
* **Stator Input ($P_{in}$):** 3-phase electrical power supplied from grid:
  $$P_{in} = \sqrt{3} V_L I_L \cos\theta$$
* **Stator Losses:** Lost as stator copper loss ($P_{scl}$) and stator iron/core loss ($P_c$).
* **Rotor Input / Air-Gap Power ($P_2$):** Power magnetically transferred across air gap:
  $$P_2 = P_{in} - (P_{scl} + P_c)$$
* **Rotor Copper Loss ($P_{cr}$):** Heat lost in rotor conductors:
  $$P_{cr} = s P_2$$
* **Gross Mechanical Power ($P_m$):** Power converted to mechanical rotation:
  $$P_m = P_2 - P_{cr} = P_2(1 - s)$$
* **Shaft Output Power ($P_{out}$):** Useful output at shaft after subtracting mechanical losses (friction and windage, $P_{mech}$):
  $$P_{out} = P_m - P_{mech}$$

**2. Proof that $P_m = (1 - s)P_2$:**
$$P_m = P_2 - P_{cr} = P_2 - s P_2 = P_2(1 - s) \quad \text{(Proved)}$$

* **[Figure Involved]:** Power Flow Block Diagram:
  $$P_{in} \xrightarrow{-\text{Stator Losses}} P_2 \xrightarrow{-P_{cr}\,(sP_2)} P_m \xrightarrow{-\text{Friction/Windage}} P_{out}$$
* **References:** AC Induction Motors.

---

### **2. Basic Concepts and Structure of Rotating Electric Machines**

### Page 2, Q.1: What are the functions of Generators and Motors?

**1. Generator:**
* **Primary Function:** Converts mechanical energy into electrical energy.
* **Working Action:** A prime mover (turbine or engine) rotates the armature inside a magnetic field. Conductors cut magnetic flux, dynamically inducing voltage based on Faraday's Law.
* **Application:** Supplying electrical power to grids, standby plants, and battery charging systems.

**2. Motor:**
* **Primary Function:** Converts electrical energy into mechanical rotational energy.
* **Working Action:** When current is supplied to armature conductors placed in a magnetic field, Lorentz forces act on them (Fleming's Left-Hand Rule), producing driving torque.
* **Application:** Driving mechanical loads like cranes, fans, pumps, electric vehicles, and rolling mills.

* **Figures involved:** Simple energy flow block diagrams (Mechanical $\rightarrow$ Generator $\rightarrow$ Electrical; Electrical $\rightarrow$ Motor $\rightarrow$ Mechanical).
* **References:** Mam Slide: 7, 8, 18; Firoz Note: 2, 4.

---

### Page 2, Q.2: State and Explain Lenz’s law and Faraday’s law of electromagnetic induction.

**1. Faraday’s Law of Electromagnetic Induction:**
* **First Law:** Whenever magnetic flux linked with a circuit changes, or a conductor cuts magnetic flux, an electromotive force (EMF) is induced.
* **Second Law:** The magnitude of induced EMF is proportional to the rate of change of flux linkages:
  $$e = -N \frac{d\Phi}{dt} \quad \text{or for a moving conductor: } e = B l v \sin\theta$$
* **Explanation:** Requires 3 elements: magnetic field ($B$), conductor length ($l$), and relative motion ($v$).

**2. Lenz’s Law:**
* **Statement:** The direction of an induced EMF (and resulting current) always opposes the change in flux or motion that produces it.
* **Explanation (Conservation of Energy):**
  * *In Generator:* Induced current creates an opposing magnetic force (counter-torque) that resists rotation; mechanical work must be done to drive it.
  * *In Motor:* Rotation induces Back EMF ($E_b$) that opposes the supply voltage, regulating current draw.

* **Figures involved:** Magnet moving into coil (Lenz's law); rotating loop cutting field lines (Faraday's law).
* **References:** Mam Slide: 14, 15, 17, 25, 26, 32; Firoz Note: 6, 11.

---

### Page 2, Q.3: How Faradays electromagnetic induction law is related to dc generator?

**Relationship:**
* **Underlying Principle:** Faraday's Law is the direct operational foundation of a DC generator.
* **Dynamic Induction:** A prime mover rotates the armature coils within the stator's stationary magnetic field. The conductors continuously cut flux lines, satisfying Faraday's 1st Law by dynamically inducing voltage:
  $$e = B l v \sin\theta$$
* **Voltage Magnitude:** By Faraday's 2nd Law, induced voltage is proportional to the rate of flux cutting:
  $$E = \frac{\Phi Z N P}{60 A}$$
  *(Directly proportional to flux $\Phi$ and rotational speed $N$).*
* **Role of Commutator:** Faraday's law produces alternating current (AC) inside the rotating coils. A commutator mechanically rectifies it into direct current (DC) at the terminals.

* **Figures involved:** Simple loop rotating between N-S pole faces showing flux cutting.
* **References:** Mam Slide: 14, 18, 25, 27, 29, 30; Firoz Note: 6, 7.

---

### Page 2, Q.4: State Fleming’s left hand rule and Fleming’s right hand rule. How these rules affect generator and motor actions?

**1. Fleming’s Right-Hand Rule (Generator Action):**
* **Statement:** Stretch the thumb, forefinger, and middle finger of the **right hand** mutually perpendicular:
  * **Forefinger:** Magnetic Field ($N \rightarrow S$).
  * **Thumb:** Motion / Force on conductor.
  * **Middle finger:** Direction of induced EMF / Current.
* **Effect on Generator:** Inputs are Field and Motion; output is the direction of induced current generated in the armature.

**2. Fleming’s Left-Hand Rule (Motor Action):**
* **Statement:** Stretch the thumb, forefinger, and middle finger of the **left hand** mutually perpendicular:
  * **Forefinger:** Magnetic Field ($N \rightarrow S$).
  * **Middle finger:** Current supplied to conductor.
  * **Thumb:** Direction of resulting Force / Motion.
* **Effect on Motor:** Inputs are Field and Current; output is the direction of electromagnetic force that produces rotation.

* **Figures involved:** Orthogonal hand diagrams labeled Motion/Thumb, Field/Forefinger, Current/Middle finger.
* **References:** Mam Slide: 16, 20, 31, 216; Firoz Note: 11, 74.

---

### Page 2, Q.5: Write down the conditions or requirements to be fulfilled for generator and motor actions.

**Requirements for Generator Action (Mechanical $\rightarrow$ Electrical):**
1. **Magnetic Field ($\Phi$):** A working magnetic field produced by stator field poles.
2. **Conductor System ($l$):** Armature windings placed in rotor slots.
3. **Relative Motion ($v$):** Mechanical rotation supplied by a prime mover to cut flux lines ($e = Blv\sin\theta$).

**Requirements for Motor Action (Electrical $\rightarrow$ Mechanical):**
1. **Magnetic Field ($\Phi$):** A steady magnetic field produced by stator field poles.
2. **Current-Carrying Conductors ($I$):** Armature conductors fed with DC current from an external supply.
3. **Spatial Angle ($\theta > 0^\circ$):** Conductors positioned at an angle to field lines to generate Lorentz force ($F = BIl\sin\theta$).

* **Figures involved:** Basic block diagrams of energy conversion inputs and outputs.
* **References:** Mam Slide: 14, 18, 20, 27, 29; Firoz Note: 7, 72.

---

### Page 2, Q.8: Write the functions of commutator and brushes.

**1. Commutator:**
* **In Generator:** Acts as a mechanical rectifier; converts alternating EMF (AC) generated in armature coils into unidirectional voltage (DC) at the terminals.
* **In Motor:** Reverses current direction in each coil as it crosses the neutral plane, ensuring that torque always acts in the same rotational direction.
* **Structure:** Cylinder of hard-drawn copper wedge segments insulated from each other by mica.

**2. Brushes:**
* **In Generator:** Collects DC current from rotating commutator segments and delivers it to the load.
* **In Motor:** Delivers DC current from external supply into the rotating commutator segments.
* **Material:** Carbon or graphite (provides high contact resistance to reduce sparking, low friction, and natural self-lubrication).

* **Figures involved:** Split-ring commutator with stationary brushes riding on its surface.
* **References:** Mam Slide: 44, 45, 62, 63, 76, 78; Firoz Note: 20, 21, 77.

---

### Page 2, Q.9: Explain the working principle of dc generator.

**Principle:** Faraday's Law of Electromagnetic Induction.

**Working Steps:**
1. **Field Setup:** Stator poles produce a stationary magnetic field across the air gap.
2. **Flux Cutting:** A prime mover spins the armature rotor; conductors cut magnetic flux lines.
3. **EMF Generation:** An alternating EMF is induced in each coil ($e = Blv\sin\theta$, direction by Fleming's Right-Hand Rule).
4. **Commutation:** Armature coils connect to split copper commutator segments.
5. **Rectification:** Just as coil current reverses every half turn, commutator segments swap contact under stationary carbon brushes.
6. **DC Output:** Brushes collect unidirectional (DC) current and feed it to the external circuit.

* **Figures involved:** Single-loop generator with split-ring commutator, showing AC coil waveform converting to pulsating DC output.
* **References:** Mam Slide: 18, 29, 30, 41-46; Firoz Note: 6, 20.

---

### Page 2, Q.12: Name the different essential parts of a dc machine.

**A. Stator (Stationary Assembly):**
1. **Yoke (Frame):** Outer protective cast-iron/steel casing; supports poles and provides a low-reluctance magnetic flux return path.
2. **Pole Cores & Pole Shoes:** Steel cores projecting inwards; pole shoes support field coils and distribute flux evenly in the air gap.
3. **Field Windings:** Copper coils wound on pole cores to establish the main working flux.
4. **Brushes & Brush Gear:** Carbon blocks in holders riding on commutator to transfer current.

**B. Rotor (Rotating Assembly):**
5. **Armature Core:** Laminated silicon steel cylinder with axial slots; houses windings and reduces eddy current losses.
6. **Armature Windings:** Insulated copper coils where EMF induction or torque creation occurs.
7. **Commutator:** Mica-insulated copper segments mounted on shaft; acts as mechanical rectifier/switch.
8. **Shaft & Bearings:** Supports rotating parts and transmits mechanical torque.

* **Figures involved:** Cross-sectional diagram of DC machine labeling yoke, poles, field coils, armature core, commutator, and brushes.
* **References:** Mam Slide: 10, 12, 61-67; Firoz Note: 20.

---

### Page 2, Q.13: What are the purposes of Field winding, Armature winding and brushes in d.c machine?

* **Field Winding:** Produces the main working magnetic flux ($\Phi$) across the air gap when energized with direct current.
* **Armature Winding:** The main power-converting winding:
  * *In Generator:* Cuts magnetic flux to induce generated voltage ($E$).
  * *In Motor:* Carries armature current ($I_a$) within the magnetic field to produce electromagnetic torque ($T = K\Phi I_a$).
* **Brushes:** Form a sliding electrical bridge between stationary external wiring and rotating commutator segments to collect (generator) or feed (motor) direct current.

* **Figures involved:** Machine layout showing field coils on stator, armature coils on rotor, and brushes on commutator.
* **References:** Mam Slide: 62, 63, 71, 72, 75, 78; Firoz Note: 27, 28.

---

### Page 2, Q.14: Why are carbon brushes preferred for dc machines?

**Reasons for Preference:**
1. **Self-Lubricating:** Soft graphite forms a smooth film on commutator, minimizing mechanical friction and wear.
2. **Protects Commutator:** Carbon is softer than copper; inexpensive brushes wear out rather than the costly commutator.
3. **Improves Commutation:** High contact resistance limits short-circuit current in coils bridged during commutation, suppressing sparking.
4. **Negative Temperature Coefficient:** Resistance drops as temperature rises, preventing excessive voltage drops under heavy load.
5. **Thermal Stability:** Withstands localized heating and minor arcing without melting or welding to copper segments.

* **Figures involved:** Brush holder assembly and carbon brush contacting commutator.
* **References:** Mam Slide: 62, 78; Firoz Note: 53.

---

### Page 2, Q.15: Why the armature core in d.c machines is constructed with laminated steel sheets instead of solid steel sheets?

**Explanation:**
* **Cause of Eddy Currents:** The rotating armature core is a conducting iron body that continuously cuts magnetic flux. By Faraday's Law, this induces internal voltages within the iron itself.
* **Problem with Solid Core:** A solid steel block has very low electrical resistance. Induced voltages would drive massive circulating eddy currents, causing severe heat loss ($P = I^2R$) and dangerous overheating.
* **Lamination Solution:** The core is built from thin steel sheets ($0.35 \text{--} 0.5\text{ mm}$) insulated from each other by varnish or oxide coating.
* **Result:** Laminations break the eddy current paths and drastically increase resistance. Since eddy current loss is proportional to thickness squared ($W_e \propto t^2$), thin laminations reduce heating loss to a minimal level.

* **Figures involved:** Large circulating eddy current loops in a solid core vs. small, restricted loops in a laminated core.
* **References:** Mam Slide: 74, 201; Firoz Note: 128-130.

---

### Page 2, Q.16: Why the armature core but not the magnetic pole core of a dc machine must be laminated?

**Reason:**
* **Armature Core MUST be Laminated:** As the armature rotates, every section of the core passes alternately under North and South poles. The magnetic flux in the core continuously alternates direction ($d\Phi/dt \neq 0$), inducing strong eddy currents that require lamination.
* **Pole Core DOES NOT require full Lamination:** The field coils are energized by steady Direct Current (DC). Consequently, the flux inside the main pole core is static and constant ($d\Phi/dt = 0$). No eddy currents are induced in the core body, so solid steel is sufficient.
* *(Note: Pole shoes are laminated only to reduce minor surface eddy currents caused by flux ripple as armature teeth sweep past).*

* **Figures involved:** None.
* **References:** Mam Slide: 71, 74; Firoz Note: 129, 130.

---

### Page 3, Q.35: Explain the concept of electrical degrees. How is the electrical angle of the voltage in a rotor conductor related to the mechanical angle of the machine’s shaft?

**1. Concepts:**
* **Mechanical Degrees ($\theta_m$):** Spatial rotation of the rotor shaft ($1\text{ complete physical revolution} = 360^\circ_m$).
* **Electrical Degrees ($\theta_e$):** Phase angle of the generated AC voltage ($1\text{ full cycle } (N\text{-to-}S) = 360^\circ_e$).

**2. Relationship:**
* Passing one pair of poles (1 North + 1 South, which is $P/2$ pole pairs) generates 1 full electrical cycle ($360^\circ_e$).
* **Formula:**
  $$\theta_e = \frac{P}{2} \cdot \theta_m$$
  *(where $P$ = total number of magnetic poles).*
* **Examples:**
  * In a 2-pole machine ($P = 2$): $\theta_e = \theta_m$ ($360^\circ_m = 360^\circ_e$).
  * In a 4-pole machine ($P = 4$): $\theta_e = 2\theta_m$ ($360^\circ_m = 720^\circ_e$, two AC cycles per mechanical revolution).

* **Figures involved:** Diagram showing 4 poles around rotor matching 2 full sine-wave AC cycles.
* **References:** Mam Slide: 87-92; Firoz Note: 19.

---

### Page 3, Q.36: What is the pitch factor of a coil and commutator pitch?

**1. Pitch Factor ($k_p$ or $p$):**
* **Definition:** The ratio of the voltage induced in a fractional-pitch coil to the voltage that would be induced in a full-pitch coil:
  $$k_p = \cos\left(\frac{\alpha}{2}\right) = \frac{\text{Electrical angle spanned by coil}}{180^\circ_e}$$
  *(where $\alpha$ = chording angle).*
* *Full-pitch coil:* Spans $180^\circ_e$ (one pole pitch), $k_p = 1$.
* *Fractional-pitch coil:* Spans $< 180^\circ_e$, $k_p < 1$ (used to eliminate harmonics and save copper in coil overhangs).

**2. Commutator Pitch ($Y_c$):**
* **Definition:** The distance measured in number of commutator segments between the start and finish leads of a single armature coil.
* *Lap Winding:* Ends connect to adjacent segments: $Y_c = \pm 1$.
* *Wave Winding:* Ends connect to segments roughly two pole pitches apart: $Y_c = \frac{2C \pm 1}{P/2}$ *(where $C$ = total coils, $P$ = poles).*

* **Figures involved:** Coil span showing full pitch ($180^\circ$) vs chorded pitch; commutator segment connections for lap and wave.
* **References:** Mam Slide: 93, 107-109; Firoz Note: 147.

---

### Page 3, Q.37: Mention the two types of winding used in the dc machines. How do lap windings differ from wave windings?

**Two Types:** **Lap Winding** and **Wave Winding**.

**Differences:**

| Feature | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Connection Method** | Coil ends connect to adjacent segments ($Y_c = \pm 1$). Coils "lap" back on each other. | Coil ends connect across poles ($Y_c \approx 2\text{ pole pitches}$). Progresses in a "wave". |
| **Parallel Paths ($A$)** | $A = P$ (equal to number of poles). | $A = 2$ (always exactly 2 paths). |
| **Voltage & Current** | High current, low voltage rating. | Low current, high voltage rating. |
| **Number of Brushes** | Requires brushes equal to poles ($P$). | Requires only 2 brushes minimum. |
| **Equalizer Rings** | **Required** in large machines to prevent circulating path currents. | **Not required**. |
| **Dummy Coils** | Never needed. | Sometimes needed for mechanical balance. |

* **Figures involved:** Winding diagrams showing overlapping lap coils vs forward progressing wave coils.
* **References:** Mam Slide: 98-100, 104, 111, 118-120.

---

### Page 3, Q.38: What is the basic difference between lap winding and wave winding? Explain frog-leg winding.

**1. Basic Difference:**
* **Lap Winding:** $A = P$ parallel paths $\implies$ suitable for high current, low voltage.
* **Wave Winding:** $A = 2$ parallel paths $\implies$ suitable for low current, high voltage.

**2. Frog-Leg Winding:**
* **Definition:** A hybrid armature winding that combines a multiplex wave winding and a multiplex lap winding placed in the **same slots** and connected to the **same commutator**.
* **Appearance:** Individual combined coils resemble frog legs.
* **Key Function (Self-Equalizing):** Lap windings normally require external equalizer rings to eliminate circulating currents caused by magnetic imbalance. The wave winding portion naturally links points of equal potential under successive poles, making the winding **100% self-equalizing** without external equalizer rings.
* **Parallel Paths:** $A = 2 \times P \times m_{lap}$.

* **Figures involved:** Diagram of a frog-leg coil showing lap and wave sections together.
* **References:** Mam Slide: 98, 122, 123; Firoz Note: 148.

---

### Page 4, Q.40: What is neutral plane? Explain why the brushes of a dc machine must be located in the neutral plane?

**1. Neutral Plane:**
* **Magnetic Neutral Plane (MNP):** The axis perpendicular to the main magnetic flux lines.
* When conductors rotate through this plane, they move parallel to flux lines, cutting zero flux $\implies$ induced EMF = **zero**.

**2. Why Brushes Must be Located on MNP:**
* **Commutation Short-Circuit:** As the commutator rotates, a brush briefly bridges two adjacent segments, momentary **short-circuiting** the coil attached between them.
* **Sparkless Operation:**
  * If brushes are placed on the MNP, the short-circuited coil has **zero induced EMF**, so short-circuit current is zero $\rightarrow$ smooth, sparkless commutation.
  * If brushes are placed off the MNP, the coil has active induced EMF, driving large short-circuit currents that produce destructive sparking and commutator pitting when interrupted.

* **Figures involved:** Geometric Neutral Axis (GNA) and Magnetic Neutral Axis (MNA) showing perpendicularity to field flux; brush short-circuiting coil at MNP.
* **References:** Mam Slide: 183-187; Firoz Note: 56-62.

---

### Page 4, Q.52: Explain the principle of operation of a DC motor.

**Principle:** Lorentz force on a current-carrying conductor in a magnetic field.

**Working Steps:**
1. **Magnetic Field:** Stator field windings or permanent magnets produce flux density $B$.
2. **Current Feed:** External DC voltage delivers current $I_a$ into armature coils through brushes and commutator.
3. **Lorentz Force:** Conductors experience mechanical force:
   $$F = B I l \sin\theta \quad (\text{Fleming's Left-Hand Rule})$$
4. **Torque Generation:** Conductors on opposite sides of the rotor experience equal and opposite forces, creating driving torque:
   $$T = K \Phi I_a$$
5. **Continuous Rotation:** The commutator reverses current direction in each coil as it crosses the neutral plane, maintaining unidirectional torque.
6. **Back EMF ($E_b$):** Rotating armature conductors cut flux, inducing Counter-EMF ($E_b = \frac{P\Phi Z N}{60 A}$) that opposes supply voltage (Lenz's Law) and self-regulates armature current ($I_a = \frac{V - E_b}{R_a}$).

* **Figures involved:** Fleming's Left-Hand Rule diagram and cross-section of 2-pole motor showing conductor current directions and rotational force couple.
* **References:** Mam Slide: 20, 214-221; Firoz Note: 72-78.

---

### Page 8, Q.8(b): Define universal motor. Differentiate universal motor from a dc series motor and also mention its applications.

**1. Definition:**
A Universal Motor is a commutator-type series motor designed to operate efficiently on either single-phase AC or DC supply at similar speed and torque.

**2. Differences from DC Series Motor:**

| Feature | DC Series Motor | Universal Motor |
| :--- | :--- | :--- |
| **Stator Core** | Solid cast iron/steel yoke | Entirely laminated to prevent severe AC eddy current losses |
| **Field Turns** | Many turns (high inductance) | Fewer turns (lowers reactance to improve AC power factor) |
| **Compensating Windings**| Rare | Often embedded in pole faces to counteract AC armature reaction |
| **Air Gap** | Moderate | Very small to maximize flux with fewer field turns |

**3. Applications:**
High-speed, compact appliances needing high power-to-weight ratios: vacuum cleaners, portable drills, blenders, mixers, circular saws, hair dryers, sewing machines.

* **Figures involved:** Schematic diagram showing series connection of armature and field.
* **References:** AC/DC Special Machines.

---

### Page 9, Q.5(a): Describe the construction and working principle of DC motor.

**1. Essential Construction Parts:**
* **Yoke:** Outer steel frame; protective enclosure and magnetic return path.
* **Poles & Field Coils:** Laminated pole shoes carrying copper windings that produce main flux $\Phi$.
* **Armature (Rotor):** Laminated silicon-steel slotted drum housing insulated armature coils.
* **Commutator:** Mica-insulated copper segments mounted on shaft; periodically reverses coil current.
* **Brushes:** Carbon blocks resting on commutator to transfer current from external DC supply.

**2. Working Principle:**
* Current $I_a$ supplied to armature conductors situated in magnetic field $B$ produces mechanical force:
  $$F = B I l \sin\theta \quad (\text{Fleming's Left-Hand Rule})$$
* Opposing forces across the rotor diameter generate continuous torque:
  $$T = K \Phi I_a$$
* Commutator reverses current at each neutral crossing to keep rotation unidirectional.
* Self-regulation achieved via Back EMF:
  $$I_a = \frac{V - E_b}{R_a}$$

* **Figures involved:** Cross-sectional diagram of DC motor showing stator, rotor, and brush assembly.
* **References:** Mam Slide: 10-12, 61-65, 214-221; Firoz Note: 72-78.

---

### Page 12, Q.1(d): What is the essential difference between lap and wave windings? The armature of a 4 pole dc shunt generator is lap-wound and generates 216V when running at 600 rpm. Armature has 144 slots, with 6 conductors per slot. If this armature rewound to wave-connected, find the emf generated with the same flux per pole but running at 500 rpm.

**Part 1: Essential Difference:**
* **Lap Winding:** $A = P$ parallel paths $\implies$ high current, low voltage.
* **Wave Winding:** $A = 2$ parallel paths $\implies$ low current, high voltage.

**Part 2: Calculation:**
* **Given Data:**
  * Poles $P = 4$
  * Slots = 144, Conductors/slot = 6 $\implies$ Total conductors $Z = 144 \times 6 = 864$
  * Initial (Lap): $A_1 = P = 4$, $N_1 = 600\text{ rpm}$, $E_1 = 216\text{ V}$
  * Rewound (Wave): $A_2 = 2$, $N_2 = 500\text{ rpm}$, Flux $\Phi$ unchanged

* **Step 1: Find Flux per pole ($\Phi$) from Lap State:**
  $$E_1 = \frac{\Phi Z N_1 P}{60 A_1}$$
  $$216 = \frac{\Phi \times 864 \times 600 \times 4}{60 \times 4} = 8640 \Phi \implies \Phi = \frac{216}{8640} = 0.025\text{ Wb}$$

* **Step 2: Find Generated EMF ($E_2$) in Wave State:**
  $$E_2 = \frac{\Phi Z N_2 P}{60 A_2} = \frac{0.025 \times 864 \times 500 \times 4}{60 \times 2} = \frac{43200}{120} = \mathbf{360\text{ V}}$$

* *(Quick Ratio Check: $E_2 = E_1 \times \frac{N_2}{N_1} \times \frac{A_1}{A_2} = 216 \times \frac{500}{600} \times \frac{4}{2} = 216 \times \frac{5}{3} = \mathbf{360\text{ V}}$).*

* **Answer:** The generated EMF is **360 V**.
* **References:** Mam Slide: 100, 111, 125, 126; Firoz Note: 25, 26.

---

### Page 12, Q.2(a): Differentiate between lap winding and wave winding of a DC machine.

| Feature | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Coil Progression** | Overlaps backward ($Y_c = \pm 1$). | Waves forward ($Y_c \approx 2\text{ pole pitches}$). |
| **Parallel Paths ($A$)** | $A = P$ (equal to poles). | $A = 2$ (always 2). |
| **Ratings** | Low voltage, high current. | High voltage, low current. |
| **Number of Brushes** | Equals number of poles ($P$). | Only 2 brushes strictly required. |
| **Equalizer Rings** | Essential in large machines. | Not required. |
| **Dummy Coils** | Not needed. | Sometimes needed for mechanical balance. |

* **Figures involved:** Comparative coil connection sketches.
* **References:** Mam Slide: 98-100, 104, 111, 118-120.

---

### Page 25, CT#1 Q.1: Explain – (i) Faraday’s law of electromagnetic induction, (ii) Lenz’s law, (iii) Flemming’s right hand rule.

**1. Faraday’s Law:**
* *First Law:* When magnetic flux linked with a circuit changes, or a conductor cuts flux, an EMF is induced.
* *Second Law:* Induced EMF is proportional to the rate of change of flux linkages:
  $$E = -N \frac{d\Phi}{dt} \quad (\text{or } e = B l v \sin\theta)$$

**2. Lenz’s Law:**
* The direction of induced EMF/current always opposes the change in magnetic flux or relative motion that caused it (satisfying conservation of energy).

**3. Fleming’s Right-Hand Rule (Generator):**
* Stretch Thumb, Forefinger, and Middle finger of the right hand mutually perpendicular:
  * **Forefinger:** Magnetic Field ($N \rightarrow S$).
  * **Thumb:** Motion of conductor.
  * **Middle finger:** Direction of induced Current.

* **Figures involved:** Right-hand diagram with labeled orthogonal axes.
* **References:** Mam Slide: 14-17, 25, 26, 31, 32; Firoz Note: 6, 11, 74.

---

### Page 25, CT#1 Q.2: Differentiate between lap and wave winding.

| Comparison Point | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Parallel Paths** | $A = P$ | $A = 2$ |
| **Commutator Pitch** | $Y_c = \pm 1$ | $Y_c = \frac{2C \pm 1}{P/2}$ |
| **Voltage / Current** | Low Voltage, High Current | High Voltage, Low Current |
| **Brushes Needed** | $P$ brushes | 2 brushes |
| **Equalizer Rings** | Required | Not required |

* **Figures involved:** None.
* **References:** Mam Slide: 98-100, 104, 111, 118-120.

---

### Page 34, Q.5(a): Does the induction motor rotates at the synchronous speed? Comment your answer.

**Answer:** **No, an induction motor never rotates at synchronous speed ($N_r < N_s$).**

**Reasoning:**
1. **Torque Mechanism:** Torque is produced only when the stator's rotating magnetic field cuts rotor conductors, inducing rotor EMF and current (Faraday's Law).
2. **If $N_r = N_s$:**
   * Relative speed between rotating field and rotor $= 0$.
   * Rate of flux cutting $= 0 \implies$ induced rotor EMF $= 0 \implies$ rotor current $= 0$.
   * Electromagnetic torque drops to **zero**.
3. **Deceleration:** Without driving torque, mechanical friction and load immediately slow the rotor down below synchronous speed.
4. **Slip Requirement:** A non-zero positive slip ($s = \frac{N_s - N_r}{N_s} > 0$) is mandatory to produce driving torque.

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 38, Q.6(a): What are the differences between a squirrel cage and wound rotor induction motor?

| Feature | Squirrel Cage Induction Motor | Wound Rotor (Slip Ring) Induction Motor |
| :--- | :--- | :--- |
| **Rotor Construction** | Solid copper/aluminum bars permanently shorted by end rings. | Distributed 3-phase insulated winding brought out to 3 slip rings. |
| **External Resistance** | Cannot be connected. | External resistor bank can be connected via brushes and slip rings. |
| **Starting Torque** | Moderate/low ($1.5\times$ full load). | High (can achieve maximum torque at startup by inserting resistance). |
| **Starting Current** | High ($5 \text{--} 7\times$ full load). | Low (limited by external starting resistance). |
| **Speed Control** | Limited / difficult. | Smooth speed control by varying rotor resistance. |
| **Maintenance & Cost** | Very low cost, rugged, maintenance-free. | Higher cost, requires slip ring and brush maintenance. |

* **Figures involved:** Sketches of squirrel cage rotor vs wound rotor with slip rings.
* **References:** AC Induction Motors.

---

### Page 41, Q.5(a): Develop an equivalent circuit for three phase induction motor. State the difference between exact and approximate equivalent circuit. [Figure Involved]

**1. Equivalent Circuit Development:**
* Operates like a transformer with a rotating, short-circuited secondary.
* **Stator:** Stator winding resistance $R_1$, leakage reactance $X_1$, and shunt magnetizing branch ($R_c \parallel X_m$).
* **Rotor (referred to stator):** Rotor leakage reactance $X_2'$ and effective resistance $R_2'/s$.
* **Mechanical Load Representation:** The rotor resistance is split into copper loss ($R_2'$) and mechanical power developed ($R_L'$):
  $$R_L' = R_2' \left(\frac{1 - s}{s}\right)$$

**2. Exact vs. Approximate Equivalent Circuit:**
* **Exact Circuit:** Shunt magnetizing branch ($R_c \parallel X_m$) is connected between stator impedance ($R_1 + jX_1$) and rotor impedance ($R_2'/s + jX_2'$). Accurately driven by air-gap voltage ($E_1$).
* **Approximate Circuit:** Shunt magnetizing branch is moved to the input terminals directly across supply voltage $V_1$.
  * *Justification:* Stator impedance drop at no-load is negligible ($< 5\%$ error), and moving it simplifies analysis into a single series-parallel circuit.

* **[Figure Involved]:**
  1. Exact circuit diagram (shunt branch in middle).
  2. Approximate circuit diagram (shunt branch at supply input).
* **References:** AC Induction Motors.

---

### **3. Generated Voltage in AC (and DC) Rotating Machines**

### Page 2, Q.6: Show that the voltage induced in a conductor rotating in a magnetic field is alternating in nature. How the alternating voltage induced in the conductor can be made unidirectional? Show by neat sketch. [Figure Involved]

**1. Why Induced Voltage is Alternating in Nature:**
* As a rectangular coil rotates at constant speed in a stationary magnetic field:
  * *First half-turn ($0^\circ \text{ to } 180^\circ$):* A conductor sweeps downward past the North pole, cutting flux lines and inducing a positive EMF (Fleming's Right-Hand Rule).
  * *Second half-turn ($180^\circ \text{ to } 360^\circ$):* The same conductor sweeps upward past the South pole. Since its motion relative to the field reverses, the induced EMF reverses polarity (negative).
* The induced EMF smoothly transitions from zero $\rightarrow$ positive peak $\rightarrow$ zero $\rightarrow$ negative peak $\rightarrow$ zero, naturally forming an **alternating sinusoidal (AC) wave**.

**2. How it is made Unidirectional (DC):**
* By replacing solid slip rings with a **split-ring commutator**.
* The ends of the coil connect to two insulated semicircular copper segments that rotate with the shaft.
* Stationary carbon brushes press against the segments.
* As the coil passes through the neutral axis (where induced EMF is zero), the split rings swap contact between the stationary brushes.
* The positive brush always contacts the conductor moving under the North pole, ensuring the terminal voltage is always in one direction (**pulsating DC**).

* **[Figure Involved]:**
  1. Sketch of rotating loop with slip rings producing a sinusoidal AC wave.
  2. Sketch of loop with split-ring commutator producing a full-wave rectified DC wave.
* **References:** Mam Slide: 35-43, 45; Firoz Note: 20, 21.

---

### Page 2, Q.7: How can a commutator convert ac voltages on a machine’s armature to dc voltages at its terminals?

**Working Mechanism:**
1. **Internal AC Induction:** Armature coils rotate through alternating N and S poles, generating purely alternating voltage inside the coils.
2. **Rotating Split Segments:** The ends of each coil connect to insulated copper commutator segments mounted on the rotor shaft.
3. **Stationary Brushes on MNP:** Stationary carbon brushes rest against the commutator, aligned along the Magnetic Neutral Plane (MNP).
4. **Synchronized Commutation:** At the exact moment the induced voltage in a rotating coil crosses zero and is about to reverse polarity, the commutator segments attached to that coil slide past the stationary brushes.
5. **Connection Inversion:** This sliding action swaps the connection of the coil terminals to the external load circuit simultaneously with the internal current reversal.
6. **Unidirectional Result:** Because the connection reversal cancels the polarity reversal, the current flowing out of the positive brush into the load never changes direction, producing unidirectional (DC) terminal voltage.

* **Figures involved:** Sequence diagrams showing a coil rotating through $0^\circ, 90^\circ, 180^\circ$ with brush-commutator swapping.
* **References:** Mam Slide: 42-46; Firoz Note: 20, 21, 77.

---

### Page 2, Q.10: Prove that, E = Blvsinθ, where the symbols have their usual meaning.

**Proof:**
* **Definitions:**
  * $B$ = Magnetic flux density (Tesla or $\text{Wb/m}^2$).
  * $l$ = Active length of conductor in magnetic field (m).
  * $v$ = Velocity of conductor motion (m/s).
  * $\theta$ = Angle between conductor velocity vector and magnetic field lines.

* **Derivation Steps:**
  1. In a small time interval $dt$, the conductor moves a distance:
     $$dx = v \cdot dt$$
  2. Only the component of motion perpendicular to the magnetic field cuts flux lines:
     $$dx_\perp = dx \sin\theta = v \sin\theta \cdot dt$$
  3. The effective area swept through the flux by conductor length $l$:
     $$dA = l \cdot dx_\perp = l \cdot v \sin\theta \cdot dt$$
  4. The magnetic flux cut in time $dt$:
     $$d\Phi = B \cdot dA = B l v \sin\theta \cdot dt$$
  5. By Faraday's Law, the dynamically induced EMF ($E$) is:
     $$E = \frac{d\Phi}{dt} = \frac{B l v \sin\theta \cdot dt}{dt} = B l v \sin\theta \quad \text{(Proved)}$$

* *(Vector notation: $e = (\vec{v} \times \vec{B}) \cdot \vec{l}$).*
* **Figures involved:** Conductor of length $l$ moving at velocity $v$ at angle $\theta$ through uniform parallel flux lines $B$.
* **References:** Mam Slide: 18, 50; Firoz Note: 8-10.

---

### Page 2, Q.11: Show that the voltage generated by a dc generator is given by E =kφS where the symbols have their usual meaning.

**Proof:**
* **Symbols:**
  * $\Phi$ = Useful flux per pole (Wb).
  * $P$ = Total number of poles.
  * $Z$ = Total number of armature conductors.
  * $A$ = Number of parallel paths ($A = P$ for lap, $A = 2$ for wave).
  * $S$ = Rotational speed in revolutions per minute (rpm).

* **Derivation Steps:**
  1. Magnetic flux cut by 1 conductor in 1 revolution:
     $$d\Phi = P \cdot \Phi$$
  2. Time taken for 1 revolution:
     $$dt = \frac{60}{S} \text{ seconds}$$
  3. Average EMF induced in 1 conductor:
     $$e_{cond} = \frac{d\Phi}{dt} = \frac{P \Phi}{60/S} = \frac{P \Phi S}{60}$$
  4. Number of conductors connected in series per parallel path:
     $$\text{Conductors per path} = \frac{Z}{A}$$
  5. Total generated EMF ($E$):
     $$E = e_{cond} \times \left(\frac{Z}{A}\right) = \frac{P \Phi Z S}{60 A}$$
  6. Define machine design constant $k = \frac{P Z}{60 A}$:
     $$E = k \Phi S \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** Mam Slide: 125, 126; Firoz Note: 24-26.

---

### Page 12, Q.1(b): Show that the voltage generated by a dc generator is given by E = Kφω, where symbols have their usual meanings.

**Proof:**
* **Symbols:** $\omega$ = angular velocity in rad/s, $\Phi$ = flux/pole, $P$ = poles, $Z$ = conductors, $A$ = parallel paths.
* **Derivation Steps:**
  1. From the standard DC generator EMF equation:
     $$E = \frac{P \Phi Z N}{60 A}$$
  2. The relationship between speed in rpm ($N$) and angular velocity ($\omega$) is:
     $$\omega = \frac{2\pi N}{60} \implies N = \frac{60\omega}{2\pi}$$
  3. Substitute $N$ into the EMF equation:
     $$E = \frac{P \Phi Z}{60 A} \left(\frac{60\omega}{2\pi}\right) = \left(\frac{P Z}{2\pi A}\right) \Phi \omega$$
  4. Define machine constant $K = \frac{P Z}{2\pi A}$:
     $$E = K \Phi \omega \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** Mam Slide: 238; Firoz Note: 21, 26.

---

### Page 31, Q.7(a): Explain how induction motor can be used as an asynchronous generator?

**Explanation:**
1. **Grid Connection:** The stator must remain connected to a 3-phase AC power line to supply the reactive magnetizing power required to establish the rotating magnetic field (spinning at synchronous speed $N_s = 120f/P$).
2. **Prime Mover Drive:** A mechanical prime mover (e.g., wind turbine or hydro turbine) is coupled to the rotor and drives it faster than synchronous speed:
   $$N_r > N_s$$
3. **Negative Slip:**
   $$s = \frac{N_s - N_r}{N_s} < 0$$
4. **Reversal of Current & Torque:** Because the rotor moves faster than the stator field, the direction of relative flux cutting reverses. This reverses the induced rotor EMF and rotor current.
5. **Power Delivery:** The reversed rotor currents produce an opposing electromagnetic braking torque against the prime mover. The mechanical power spent overcoming this counter-torque is converted into active electrical power (kW) and delivered back into the AC grid.

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 39, Q.7(b): What is meant by plugging of an induction motor? How does a 3-Φ induction motor operate as a generator?

**1. Plugging (Reverse-Current Braking):**
* **Definition:** An electric braking technique used to rapidly bring an induction motor to an immediate stop or reversal.
* **Method:** While the motor is running, two of the three stator supply leads are suddenly interchanged (e.g., swapping Phase B and Phase C).
* **Operation & Effect:**
  * Swapping phases instantly reverses the rotational direction of the stator magnetic field.
  * Due to mechanical inertia, the rotor continues spinning in the original direction.
  * Slip becomes:
    $$s = \frac{N_s - (-N_r)}{N_s} = \frac{N_s + N_r}{N_s} \approx 2 - s \approx 2$$
  * High slip induces massive currents and develops intense counter-torque that rapidly decelerates the rotor to zero (a zero-speed switch disconnects power to prevent starting in reverse).

**2. Operation as a Generator:**
* Connect stator to 3-phase grid for excitation.
* Prime mover drives rotor above synchronous speed ($N_r > N_s$), producing **negative slip ($s < 0$)**.
* Relative flux cutting reverses $\rightarrow$ rotor current reverses $\rightarrow$ machine supplies active power (kW) to the grid.

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### **4. Rotating Magnetic Field**

### Page 31, Q.5(c): Show with necessary figures that if a three phase set of currents, each of equal magnitude and differing in phase by 120°, flows in a three phase winding consisting of three separate windings spaced 120 electrical degrees apart around the surface of a machine, then it will produce a rotating magnetic field of constant magnitude. [Figure Involved]

**Demonstration:**
* Let balanced 3-phase currents flow through 3 windings displaced by $120^\circ$ in space:
  * $i_R = I_m \sin(\omega t)$ (along $0^\circ$ axis)
  * $i_Y = I_m \sin(\omega t - 120^\circ)$ (along $120^\circ$ axis)
  * $i_B = I_m \sin(\omega t - 240^\circ)$ (along $240^\circ$ axis)
* Corresponding phase fluxes:
  * $\phi_R = \Phi_m \sin(\omega t)$
  * $\phi_Y = \Phi_m \sin(\omega t - 120^\circ)$
  * $\phi_B = \Phi_m \sin(\omega t - 240^\circ)$

**Evaluating Resultant Flux ($\Phi_r$) at Sequential Instants:**
1. **At $\omega t = 0^\circ$:**
   * $\phi_R = 0$
   * $\phi_Y = \Phi_m \sin(-120^\circ) = -\frac{\sqrt{3}}{2}\Phi_m$
   * $\phi_B = \Phi_m \sin(-240^\circ) = +\frac{\sqrt{3}}{2}\Phi_m$
   * Vector sum: $\Phi_r = 2 \times \left(\frac{\sqrt{3}}{2}\Phi_m\right) \cos(30^\circ) = 2 \times \frac{\sqrt{3}}{2}\Phi_m \times \frac{\sqrt{3}}{2} = \mathbf{1.5 \Phi_m}$ (directed horizontally).
2. **At $\omega t = 60^\circ$:**
   * $\phi_R = +\frac{\sqrt{3}}{2}\Phi_m$
   * $\phi_Y = -\frac{\sqrt{3}}{2}\Phi_m$
   * $\phi_B = 0$
   * Vector sum: $\Phi_r = \mathbf{1.5 \Phi_m}$ (rotated exactly $60^\circ$ clockwise).
3. **At $\omega t = 120^\circ$:**
   * $\phi_R = +\frac{\sqrt{3}}{2}\Phi_m$
   * $\phi_Y = 0$
   * $\phi_B = -\frac{\sqrt{3}}{2}\Phi_m$
   * Vector sum: $\Phi_r = \mathbf{1.5 \Phi_m}$ (rotated another $60^\circ$, total $120^\circ$).

**Conclusion:** The resultant magnetic field has a **constant magnitude of $1.5\Phi_m$** and **rotates at constant synchronous speed** ($N_s = \frac{120f}{P}$).

* **[Figure Involved]:**
  1. Stator winding cross-section showing R, Y, B coils spaced at $120^\circ$.
  2. Three phasor diagrams at $\omega t = 0^\circ, 60^\circ, 120^\circ$ demonstrating that the resultant vector length stays constant at $1.5\Phi_m$ while rotating.
* **References:** AC Induction Motors.

---

### Page 31, Q.6(a): Prove that for 3-Φ induction motor the resultant flux is 1.5 times of the maximum value of the induced flux in any phase.

**Proof:**
* Let the 3 spatial axes be separated by $120^\circ$, with R-phase along the horizontal X-axis:
  * $\phi_R = \Phi_m \sin(\omega t)$ at $0^\circ$
  * $\phi_Y = \Phi_m \sin(\omega t - 120^\circ)$ at $120^\circ$
  * $\phi_B = \Phi_m \sin(\omega t - 240^\circ)$ at $240^\circ$

* **1. Resolve along the Horizontal (X) Axis:**
  $$\Phi_x = \phi_R \cos(0^\circ) + \phi_Y \cos(120^\circ) + \phi_B \cos(240^\circ)$$
  $$\Phi_x = \Phi_m \sin(\omega t) - 0.5\Phi_m \sin(\omega t - 120^\circ) - 0.5\Phi_m \sin(\omega t - 240^\circ)$$
  *Expanding using $\sin(A - B)$:*
  $$\Phi_x = \Phi_m \left[\sin\omega t - 0.5\left(-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t\right) - 0.5\left(-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t\right)\right]$$
  $$\Phi_x = \Phi_m \left[\sin\omega t + \frac{1}{4}\sin\omega t + \frac{1}{4}\sin\omega t\right] = \mathbf{1.5 \Phi_m \sin(\omega t)}$$

* **2. Resolve along the Vertical (Y) Axis:**
  $$\Phi_y = \phi_R \sin(0^\circ) + \phi_Y \sin(120^\circ) + \phi_B \sin(240^\circ)$$
  $$\Phi_y = 0 + \frac{\sqrt{3}}{2}\Phi_m \sin(\omega t - 120^\circ) - \frac{\sqrt{3}}{2}\Phi_m \sin(\omega t - 240^\circ)$$
  $$\Phi_y = \frac{\sqrt{3}}{2}\Phi_m \left[\left(-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t\right) - \left(-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t\right)\right]$$
  $$\Phi_y = \frac{\sqrt{3}}{2}\Phi_m [-\sqrt{3}\cos\omega t] = \mathbf{-1.5 \Phi_m \cos(\omega t)}$$

* **3. Resultant Flux Magnitude ($\Phi_r$):**
  $$\Phi_r = \sqrt{\Phi_x^2 + \Phi_y^2} = \sqrt{(1.5\Phi_m \sin\omega t)^2 + (-1.5\Phi_m \cos\omega t)^2}$$
  $$\Phi_r = 1.5 \Phi_m \sqrt{\sin^2(\omega t) + \cos^2(\omega t)} = \mathbf{1.5 \Phi_m} \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 32, Q.8(b): By using double-revolving field theory explain how a single phase induction motor develops its torque after starting. Explain why the forward field becomes higher than the backward field at 0<S<1.

**1. Double-Revolving Field Theory (DRFT) & Torque Development:**
* A single-phase stator winding produces an alternating, pulsating magnetic field $\Phi_m$.
* DRFT states that this field resolves into two equal magnetic fields, each of magnitude $\frac{\Phi_m}{2}$, rotating in opposite directions at synchronous speed:
  * **Forward Field ($\Phi_f$):** Rotates in direction of rotor motion; slip $s_f = s$.
  * **Backward Field ($\Phi_b$):** Rotates opposite to rotor motion; slip $s_b = 2 - s$.
* *At Standstill ($s = 1$):* $s_f = s_b = 1 \implies T_f = T_b \implies T_{net} = 0$ (motor cannot start itself).
* *After Starting ($0 < s < 1$):* When spun forward, $T_f$ becomes much larger than $T_b$, producing a strong net forward torque ($T_{net} = T_f - T_b$) that keeps the motor accelerating and running.

**2. Why the Forward Field Becomes Much Higher than the Backward Field ($0 < s < 1$):**
* **Forward Slip is Small ($s \approx 0.05$):** Rotor induced frequency ($sf$) is low $\rightarrow$ rotor reactance is small $\rightarrow$ rotor impedance is high and predominantly resistive $\rightarrow$ weak rotor demagnetizing effect $\rightarrow$ **Forward field remains strong**.
* **Backward Slip is Large ($2 - s \approx 1.95$):** The backward field sweeps past the rotor at nearly twice synchronous speed $\rightarrow$ rotor induced frequency is very high ($f_b \approx 2f$) $\rightarrow$ rotor inductive reactance ($X_r = 2\pi f_b L$) is massive $\rightarrow$ large, highly lagging rotor currents produce a severe **demagnetizing effect** that suppresses the backward flux.
* **Conclusion:** The high-frequency rotor reaction heavily demagnetizes the backward field, making $\Phi_f \gg \Phi_b$ and $T_f \gg T_b$.

* **Figures involved:** Torque-speed curves of single-phase induction motor showing $T_f$, $T_b$, and the resultant torque passing through zero at $N = 0$.
* **References:** AC Induction Motors.

---

### Page 35, Q.8(a): Explain double field revolving theory. Also explain, why a single-phase transformer is not self starting.

**1. Double Field Revolving Theory (DRFT):**
* Any stationary pulsating magnetic field alternating as $\Phi = \Phi_m \cos\omega t$ can be mathematically resolved into two rotating fields of half the amplitude ($\Phi_m/2$), rotating at synchronous speed in opposite directions:
  $$\Phi = \frac{\Phi_m}{2}e^{j\omega t} + \frac{\Phi_m}{2}e^{-j\omega t}$$
* These two fields rotate symmetrically; their transverse components cancel while their axial components add, maintaining the pulsating wave.

**2. Why a "Single-Phase Transformer" (or Single-Phase Motor at Standstill) is Not Self-Starting:**
* **Transformer Definition:** A transformer is a completely static device with no moving parts or air gap; mechanical rotation is fundamentally inapplicable.
* **Standstill Motor Analogy:** At rest ($N = 0$), a single-phase induction motor is identical to a short-circuited transformer:
  1. The single-phase stator winding acts as the primary, producing a pulsating flux along a single spatial axis.
  2. This flux induces voltages and currents in the rotor bars (secondary).
  3. By Lenz's Law, the rotor creates an opposing flux along the **exact same physical axis**.
  4. Because both magnetic forces act directly across the diameter without angular displacement, **no rotational torque is produced**.
  5. By DRFT, forward torque equals backward torque ($T_f = T_b$), giving net starting torque = 0.

* **Figures involved:** Phasor diagram of two counter-rotating vectors of length $\Phi_m/2$ adding along a vertical axis.
* **References:** AC Induction Motors.

---

### Page 39, Q.8(b): State the concept of double field revolving theory for a 1-Φ induction motor and derive the equations of forward and backward torques.

**1. Concept:**
A single-phase pulsating magnetic flux ($\Phi_m$) resolves into:
* Forward field: $\Phi_f = \Phi_m/2$ rotating at $+N_s$.
* Backward field: $\Phi_b = \Phi_m/2$ rotating at $-N_s$.

**2. Derivation of Torques:**
* Let rotor run at speed $N$ in forward direction:
  * **Forward Slip:** $s_f = \frac{N_s - N}{N_s} = s$
  * **Backward Slip:** $s_b = \frac{N_s - (-N)}{N_s} = \frac{N_s + N_s(1 - s)}{N_s} = 2 - s$

* **Rotor Resistances:**
  * Forward branch rotor resistance: $\frac{R_2}{2s}$
  * Backward branch rotor resistance: $\frac{R_2}{2(2 - s)}$

* **Torque Expressions:**
  * Air-gap power converted into torque ($T = P_g / \omega_s$):
    $$T_f = \frac{1}{\omega_s} I_2^2 \left(\frac{R_2}{2s}\right)$$
    $$T_b = \frac{1}{\omega_s} I_2^2 \left(\frac{R_2}{2(2 - s)}\right)$$

* **Net Torque ($T_{net}$):**
  $$T_{net} = T_f - T_b = \frac{I_2^2 R_2}{2\omega_s} \left[\frac{1}{s} - \frac{1}{2 - s}\right]$$

* **Figures involved:** Torque-speed curve for single-phase motor.
* **References:** AC Induction Motors.

---

### Page 41, Q.4(b): Explain the double field revolving theory for operation of single phase induction motor.

**Operational Analysis via DRFT:**
1. **At Standstill ($N = 0$):**
   * $s_f = s = 1$, $s_b = 2 - s = 1$.
   * Since slips are identical, the forward torque equals the backward torque:
     $$T_f = T_b \implies T_{net} = 0$$
   * The motor produces zero net starting torque and **cannot start on its own**.
2. **Under Running Condition ($N > 0$):**
   * When given an initial rotation forward, slip $s$ becomes very small ($s \approx 0.05$).
   * Backward slip becomes large: $s_b = 2 - s \approx 1.95$.
   * Since torque is roughly proportional to $1/s$:
     * $T_f \propto \frac{1}{0.05} = 20$ (very large forward torque).
     * $T_b \propto \frac{1}{1.95} \approx 0.51$ (tiny backward torque).
   * Result: $T_f \gg T_b \implies T_{net} > 0$. The motor accelerates and smoothly drives its mechanical load.

* **Figures involved:** Resultant torque-slip curve crossing zero at $s = 1$.
* **References:** AC Induction Motors.

---

### Page 41, Q.5(b): Discuss graphically how a rotating field is produced in the air gap of three phase induction motor. [Figure Involved]

**Graphical Demonstration:**
Consider three identical stator coils displaced by $120^\circ$ in space carrying balanced 3-phase currents:
* $i_R = I_m \sin(\omega t)$
* $i_Y = I_m \sin(\omega t - 120^\circ)$
* $i_B = I_m \sin(\omega t - 240^\circ)$

**Vector Addition at Successive Time Instants:**
1. **Instant 1 ($\omega t = 0^\circ$):**
   * $i_R = 0$, $i_Y = -0.866 I_m$, $i_B = +0.866 I_m$.
   * Flux vectors: $\phi_R = 0$, $\phi_Y$ directed opposite to Y-axis, $\phi_B$ along B-axis.
   * Graphical vector sum points **horizontally to the left**, magnitude $= 1.5\Phi_m$.
2. **Instant 2 ($\omega t = 60^\circ$):**
   * $i_R = +0.866 I_m$, $i_Y = -0.866 I_m$, $i_B = 0$.
   * Graphical sum of $\phi_R$ and reversed $\phi_Y$ yields the same length ($1.5\Phi_m$), rotated **$60^\circ$ clockwise**.
3. **Instant 3 ($\omega t = 120^\circ$):**
   * $i_R = +0.866 I_m$, $i_Y = 0$, $i_B = -0.866 I_m$.
   * Graphical sum yields magnitude $1.5\Phi_m$, rotated another **$60^\circ$ clockwise** ($120^\circ$ total).

**Conclusion:** The graphical vector plot proves the resultant air-gap field has a constant length ($1.5\Phi_m$) whose tip traces a circle, rotating smoothly at synchronous speed.

* **[Figure Involved]:**
  * Current waveforms for the 3 phases.
  * Three vector addition diagrams for $\omega t = 0^\circ, 60^\circ, 120^\circ$ showing clockwise rotation.
* **References:** AC Induction Motors.

---

### Page 45, Q.5(b): Prove that, for a poly phase induction motor, the resultant revolving flux is 1.5 times the maximum value of the flux due to any phase.

**Trigonometric Proof:**
Let the 3 individual phase fluxes be space-displaced by $120^\circ$:
$$\phi_1 = \Phi_m \sin(\omega t) \quad (\text{along } 0^\circ)$$
$$\phi_2 = \Phi_m \sin(\omega t - 120^\circ) \quad (\text{along } 120^\circ)$$
$$\phi_3 = \Phi_m \sin(\omega t - 240^\circ) \quad (\text{along } 240^\circ)$$

1. **Sum of X-Components:**
   $$\Phi_x = \phi_1 + \phi_2 \cos(120^\circ) + \phi_3 \cos(240^\circ)$$
   $$\Phi_x = \Phi_m \sin\omega t - \frac{1}{2}\Phi_m \sin(\omega t - 120^\circ) - \frac{1}{2}\Phi_m \sin(\omega t - 240^\circ)$$
   $$\Phi_x = \Phi_m \left[\sin\omega t + \frac{1}{4}\sin\omega t + \frac{1}{4}\sin\omega t\right] = \mathbf{1.5 \Phi_m \sin(\omega t)}$$

2. **Sum of Y-Components:**
   $$\Phi_y = \phi_1(0) + \phi_2 \sin(120^\circ) + \phi_3 \sin(240^\circ)$$
   $$\Phi_y = \frac{\sqrt{3}}{2}\Phi_m \sin(\omega t - 120^\circ) - \frac{\sqrt{3}}{2}\Phi_m \sin(\omega t - 240^\circ)$$
   $$\Phi_y = \frac{\sqrt{3}}{2}\Phi_m [-\sqrt{3}\cos\omega t] = \mathbf{-1.5 \Phi_m \cos(\omega t)}$$

3. **Resultant Flux Magnitude ($\Phi_r$):**
   $$\Phi_r = \sqrt{\Phi_x^2 + \Phi_y^2} = \sqrt{(1.5\Phi_m \sin\omega t)^2 + (-1.5\Phi_m \cos\omega t)^2}$$
   $$\Phi_r = 1.5\Phi_m \sqrt{\sin^2\omega t + \cos^2\omega t} = \mathbf{1.5 \Phi_m} \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 46, Q.8(b): With the help of double field revolving theory, prove that for the case of 1-Φ induction motor, under running condition V >> Vb, where the symbols have their usual meanings.

**Proof:**
* In the DRFT equivalent circuit, the stator voltage drops across the forward rotor impedance branch ($V_f$) and backward rotor impedance branch ($V_b$) connected in series.
* **Rotor Impedance Formulas:**
  $$Z_f = \frac{R_2}{2s} + j\frac{X_2}{2}$$
  $$Z_b = \frac{R_2}{2(2 - s)} + j\frac{X_2}{2}$$
* **Under Running Conditions:**
  * Motor spins near synchronous speed $\implies$ slip $s$ is very small ($s \approx 0.05$).
  * Since $s$ is very small, $\frac{R_2}{2s}$ is very large $\implies \mathbf{Z_f \text{ is very large}}$.
  * Backward slip is large ($2 - s \approx 1.95$), making $\frac{R_2}{2(2 - s)}$ very small $\implies \mathbf{Z_b \text{ is very small}}$.
* **Comparing Impedances:**
  $$Z_f \gg Z_b$$
* **Voltage Division:**
  * Since the same current $I_1$ flows through both series branches:
    $$V_f = I_1 Z_f \quad \text{and} \quad V_b = I_1 Z_b$$
  * Because $Z_f \gg Z_b$, it strictly follows that:
    $$\mathbf{V_f \gg V_b} \quad (\text{or } V \gg V_b) \quad \text{(Proved)}$$

* **Figures involved:** DRFT series equivalent circuit showing $V_f$ and $V_b$.
* **References:** AC Induction Motors.

---

### Page 46, Q.8(c): State and explain double field revolving theory as applied to 1-Φ induction motor.

**1. Statement:**
Any alternating pulsating magnetic field of maximum value $\Phi_m$ produced by a single-phase AC winding can be resolved into two rotating fields of equal magnitude ($\frac{\Phi_m}{2}$) rotating in opposite directions at synchronous speed ($+N_s$ and $-N_s$).

**2. Explanation Applied to 1-$\Phi$ Motor:**
* **Pulsating Stator Flux:** AC current in the main winding produces a stationary magnetic field that alternates polarity along one axis without rotating.
* **Two Virtual Fields:**
  * *Forward Field ($\Phi_f$):* Rotates clockwise at $N_s$ with slip $s$.
  * *Backward Field ($\Phi_b$):* Rotates counter-clockwise at $N_s$ with slip $2 - s$.
* **At Rest ($N = 0$):** Both slips equal 1 ($s_f = s_b = 1$), producing identical opposing torques ($T_f = T_b$). Net torque $= 0 \implies$ motor is **not self-starting**.
* **While Running ($N > 0$):** Once spun in the forward direction:
  * $s$ becomes small $\rightarrow T_f$ increases sharply.
  * $2 - s$ becomes large $\rightarrow$ high-frequency rotor currents demagnetize the backward field $\rightarrow T_b$ becomes negligible.
  * Net torque ($T_f - T_b > 0$) sustains smooth rotation.

* **Figures involved:** Phasor diagram of pulsating vector resolved into counter-rotating components.
* **References:** AC Induction Motors.

---

### **5. Machine Torque (General & Cylindrical Air Gaps)**

### Page 4, Q.53: Derive the expression of induced torque for a real motor.

**Proof:**
1. **Power Conversion Equivalence:**
   In a DC motor, electrical power converted into mechanical power equals mechanical power developed:
   $$P_{conv} = E_a I_a = \tau_{ind} \omega_m$$
   *(where $E_a$ = back EMF, $I_a$ = armature current, $\tau_{ind}$ = induced torque, $\omega_m$ = angular speed in rad/s).*

2. **Substitute Generated Voltage (Back EMF) Equation:**
   $$E_a = \frac{Z P \Phi \omega_m}{2 \pi A}$$
   *(where $Z$ = conductors, $P$ = poles, $\Phi$ = flux/pole, $A$ = parallel paths).*

3. **Equate and Solve for Torque:**
   $$\tau_{ind} \omega_m = \left(\frac{Z P \Phi \omega_m}{2 \pi A}\right) I_a$$
   $$\tau_{ind} = \left(\frac{Z P}{2 \pi A}\right) \Phi I_a$$

4. **Define Machine Constant $K$:**
   Let $K = \frac{Z P}{2 \pi A}$:
   $$\mathbf{\tau_{ind} = K \Phi I_a} \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** Mam Slide: 238, 240; Firoz Note: 76, 78, 82.

---

### Page 5, Q.64: Explain briefly speed versus armature current and torque versus armature current characteristics of all dc motors.

**1. Torque vs. Armature Current ($T$ vs $I_a$) Characteristics:**
* **General Formula:** $T \propto \Phi I_a$.
* **Shunt Motor:** Flux $\Phi$ is constant $\implies T \propto I_a$. *Linear straight line from origin.*
* **Series Motor:** Flux $\Phi \propto I_a$ (before saturation) $\implies T \propto I_a^2$. *Parabolic curve that bends into a straight line after saturation.*
* **Cumulative Compound Motor:** $\Phi = \Phi_{sh} + \Phi_{se}$. Rises faster than shunt, slower than series.
* **Differential Compound Motor:** $\Phi = \Phi_{sh} - \Phi_{se}$. Total flux decreases with load $\implies$ curve drops below shunt line.

**2. Speed vs. Armature Current ($N$ vs $I_a$) Characteristics:**
* **General Formula:** $N \propto \frac{V - I_a R_a}{\Phi}$.
* **Shunt Motor:** $\Phi$ is constant. As $I_a$ rises, $I_a R_a$ drop increases slightly $\implies$ *slight linear droop (practically constant speed)*.
* **Series Motor:** $N \propto 1/\Phi \propto 1/I_a$. *Steep hyperbolic curve.* At no-load ($I_a \approx 0$), speed reaches dangerous, destructive runaway values.
* **Cumulative Compound Motor:** Flux increases with load $\implies$ speed drops more than shunt, but stays stable and safe at no-load.
* **Differential Compound Motor:** Opposing series flux reduces total flux as load increases $\implies$ *speed actually increases with load*, causing dangerous instability.

* **Figures involved:** 
  1. $T$ vs $I_a$ graph (straight line for Shunt, parabola for Series, compound curves in-between).
  2. $N$ vs $I_a$ graph (flat droop for Shunt, hyperbola for Series, steep droop for Cumulative, rising curve for Differential).
* **References:** Mam Slide: 242-262; Firoz Note: 103, 109, 111.

---

### Page 5, Q.65: Draw and explain the mechanical characteristics of DC series and shunt motor. [Figure Involved]

**Definition:** Mechanical characteristic is the **Speed vs. Torque ($N$ vs $\tau$) curve**.

**1. DC Shunt Motor:**
* **Relation:** $\Phi \approx \text{constant}$, $I_a \propto \tau$, and $N \propto \frac{V - I_a R_a}{\Phi}$.
* **Behavior:** As load torque increases, $I_a R_a$ voltage drop causes a very small, linear drop in speed ($< 5\%$ from no-load to full-load).
* **Curve:** Nearly flat, slightly drooping line.

**2. DC Series Motor:**
* **Relation:** $\Phi \propto I_a \implies \tau \propto I_a^2 \implies I_a \propto \sqrt{\tau}$.
* **Speed Equation:** $N \propto \frac{1}{\Phi} \propto \frac{1}{\sqrt{\tau}}$.
* **Behavior:** Speed varies inversely with torque. At low torque, speed is dangerously high; as torque increases, speed drops sharply.
* **Curve:** Steep rectangular hyperbola.

* **[Figure Involved]:** Plot of Speed ($N$, Y-axis) vs. Torque ($\tau$, X-axis):
  * Shunt: Horizontal straight line with minor droop.
  * Series: Steep hyperbola approaching infinity at zero torque.
* **References:** Mam Slide: 242, 250, 262; Firoz Note: 111.

---

### Page 5, Q.66: Explain the effects on speed, counter emf, armature current and torque of a dc shunt motor when load applied to that motor.

**Step-by-Step Self-Regulating Sequence:**
1. **Speed ($N$):** When mechanical load is applied, load torque exceeds motor torque $\rightarrow$ rotor momentarily decelerates (**speed decreases**).
2. **Counter EMF ($E_b$):** Since $E_b = K \Phi N$ and flux $\Phi$ is constant, the drop in speed causes **Counter EMF ($E_b$) to decrease**.
3. **Armature Current ($I_a$):** From $I_a = \frac{V - E_b}{R_a}$, the reduced $E_b$ increases the net driving voltage $(V - E_b)$. Since $R_a$ is small, **armature current ($I_a$) rises significantly**.
4. **Induced Torque ($\tau_{ind}$):** Since $\tau_{ind} = K \Phi I_a$, the current surge directly causes **induced torque to increase**.
5. **New Equilibrium:** The torque increases until $\tau_{ind} = \tau_{load}$, stabilizing the motor at a new steady state running at slightly lower speed with higher current and torque.

* **Figures involved:** None.
* **References:** Mam Slide: 248; Firoz Note: 101.

---

### Page 8, Q.8(a): Define speed regulation. Draw and explain the torque and speed versus armature current characteristics of DC motors. [Figure Involved]

**1. Definition of Speed Regulation:**
* Percentage change in motor speed from no-load to full-load, relative to full-load speed:
  $$\%\text{SR} = \frac{N_{NL} - N_{FL}}{N_{FL}} \times 100\%$$
  *(where $N_{NL}$ = no-load speed, $N_{FL}$ = full-load speed).*

**2. Torque vs. Armature Current ($T$ vs $I_a$):**
* *Shunt:* Linear straight line ($T \propto I_a$).
* *Series:* Parabolic curve ($T \propto I_a^2$) bending linear after saturation.
* *Cumulative Compound:* Rises steeper than shunt, below series.
* *Differential Compound:* Flattens out due to flux reduction.

**3. Speed vs. Armature Current ($N$ vs $I_a$):**
* *Shunt:* Minor linear droop (constant speed).
* *Series:* Steep hyperbolic drop ($N \propto 1/I_a$); unsafe at no-load.
* *Cumulative Compound:* Drops steeper than shunt, safe at no-load.
* *Differential Compound:* Rises with load (unstable).

* **[Figure Involved]:** Two plots:
  1. $T$ vs $I_a$ for Shunt, Series, Cumulative, and Differential.
  2. $N$ vs $I_a$ showing flat droop (Shunt), hyperbola (Series), steep droop (Cumulative), rising curve (Differential).
* **References:** Mam Slide: 234, 242, 260; Firoz Note: 93, 94, 103, 109.

---

### Page 9, Q.6(a): Draw and explain the torque and speed characteristic of shunt motor, cumulative compound motor and differential compound motor. [Figure Involved]

**Explanation of Mechanical Characteristics ($N$ vs $\tau$):**

1. **Shunt Motor:**
   * Main flux $\Phi$ is constant.
   * Speed drops only due to small internal $I_a R_a$ drop: $N \propto V - I_a R_a$.
   * *Characteristic:* Nearly horizontal, gentle droop (constant-speed machine).

2. **Cumulative Compound Motor:**
   * Series field aids shunt field: $\Phi_{total} = \Phi_{sh} + \Phi_{se}$.
   * As load torque increases, current increases, strengthening total flux.
   * Since $N \propto 1/\Phi_{total}$, speed drops noticeably more than in a shunt motor.
   * *Characteristic:* Moderate droop; provides high starting torque with safe no-load speed limit.

3. **Differential Compound Motor:**
   * Series field opposes shunt field: $\Phi_{total} = \Phi_{sh} - \Phi_{se}$.
   * As load torque increases, rising current weakens the net magnetic field.
   * Since $N \propto 1/\Phi_{total}$, reducing flux forces the motor to speed up.
   * *Characteristic:* Speed increases with load; positive feedback creates dangerous runaway instability (never used in practice).

* **[Figure Involved]:** Single plot of Speed ($N$, Y-axis) vs. Torque ($\tau$, X-axis) showing:
  * Shunt: Gentle downward slope.
  * Cumulative Compound: Steeper downward slope.
  * Differential Compound: Sharp upward hook.
* **References:** Mam Slide: 255, 258; Firoz Note: 111.

---

### Page 14, Q.3(a): Draw speed versus armature current and torque versus armature current characteristics of all dc motors. [Figure Involved]

**1. Torque vs. Armature Current ($T$ vs $I_a$):**
* Based on $T \propto \Phi I_a$:
  * **Shunt:** Constant flux $\implies$ straight diagonal line.
  * **Series:** $\Phi \propto I_a \implies$ parabolic curve ($T \propto I_a^2$) before saturation; linear after saturation.
  * **Cumulative Compound:** Intermediate curve above shunt line.
  * **Differential Compound:** Curves below shunt line, flattening at heavy load.

**2. Speed vs. Armature Current ($N$ vs $I_a$):**
* Based on $N \propto \frac{V - I_a R_a}{\Phi}$:
  * **Shunt:** Slight linear downward droop.
  * **Series:** Inverse hyperbola ($N \propto 1/I_a$); extreme overspeeding at no-load.
  * **Cumulative Compound:** Stable downward curve, steeper than shunt.
  * **Differential Compound:** Upward rising curve (unstable).

* **[Figure Involved]:** Combined plots of $T$ vs $I_a$ and $N$ vs $I_a$ labeled with Shunt, Series, Cumulative, and Differential.
* **References:** Mam Slide: 242, 260, 264; Firoz Note: 103, 109.

---

### Page 15, Q.4(a): Derive the expression for induced torque of a real motor. Why a dc series motor should be firmly coupled with its load?

**Part 1: Derivation of Induced Torque ($\tau_{ind}$)**
1. Electrical power converted into gross mechanical power:
   $$P_{conv} = E_a I_a = \tau_{ind} \omega_m$$
2. Substitute generated voltage equation $E_a = \frac{Z P \Phi \omega_m}{2\pi A}$:
   $$\tau_{ind} \omega_m = \left(\frac{Z P \Phi \omega_m}{2\pi A}\right) I_a$$
3. Cancel $\omega_m$ and substitute $K = \frac{Z P}{2\pi A}$:
   $$\mathbf{\tau_{ind} = K \Phi I_a} \quad \text{(Proved)}$$

**Part 2: Why a DC Series Motor Must be Firmly Coupled with its Load**
* **Speed Equation:** $N \propto \frac{V - I_a(R_a + R_{se})}{\Phi} \propto \frac{1}{\Phi}$.
* In a series motor, field current equals armature current ($I_f = I_a$), so flux depends directly on load: $\Phi \propto I_a$.
* **At No-Load (or broken belt):** Load torque $\approx 0 \implies I_a \approx 0 \implies \Phi \approx 0$ (only tiny residual flux remains).
* **Runaway Danger:**
  $$N \propto \frac{1}{\text{residual } \Phi} \rightarrow \infty$$
* Speed shoots up to dangerously destructive levels. The resulting centrifugal forces physically destroy armature windings and the commutator.
* **Safety Rule:** A DC series motor must **never be belt-driven**; it must always be firmly coupled to its load using direct gears or solid mechanical couplings.

* **Figures involved:** None.
* **References:** Mam Slide: 238, 240, 262; Firoz Note: 76, 78, 110.

---

### Page 31, Q.6(b): With the necessary diagram determine the average torque of 3-Φ induction motor when load is assumed inductive. [Figure Involved]

**Determination:**
1. **Rotor Inductance:** The rotor conductors are embedded in iron slots, possessing both resistance ($R_2$) and standstill reactance ($X_2$).
2. **Phase Lag:** Because the rotor circuit is inductive, induced rotor current ($I_2$) lags behind induced rotor EMF ($E_2$) by a phase angle $\theta_2$:
   $$\cos\theta_2 = \frac{R_2}{\sqrt{R_2^2 + (sX_2)^2}} \quad (\text{Rotor Power Factor})$$
3. **Instantaneous Torque:** Proportional to product of instantaneous flux and current: $t \propto \Phi \cdot i_2$.
4. **Average Torque ($T_{avg}$):**
   * During portions of the cycle where flux and current have opposite signs, negative torque is generated.
   * Positive torque loops exceed negative torque loops, yielding net positive torque proportional to the in-phase current component:
     $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos\theta_2$$
   * Since $E_2 \propto \Phi$:
     $$\mathbf{T_{avg} = K E_2 I_2 \cos\theta_2}$$

* **[Figure Involved]:**
  * Superimposed AC sine waves: Flux wave $\Phi$, in-phase voltage wave $E_2$, and lagging current wave $I_2$ (shifted right by $\theta_2$).
  * Resulting Torque wave showing shaded positive areas and smaller negative areas, highlighting average net torque.
* **References:** AC Induction Motors.

---

### Page 34, Q.5(b): Why the induction motor with squirrel cage rotor not useful where motor has to start against heavy load?

**Reasons:**
1. **Low Starting Torque:**
   * Starting torque formula: $T_{st} \propto \frac{R_2}{R_2^2 + X_2^2}$. Maximum starting torque requires $R_2 = X_2$.
   * In a squirrel cage rotor, conductors are solid metal bars permanently short-circuited by end rings.
   * $R_2$ is fixed at a very low value by design to maintain low slip and high efficiency during normal running.
   * Consequently, $R_2 \ll X_2$, resulting in a very low starting torque (only $1.5\times$ full-load torque), which fails to overcome heavy breakaway loads.
2. **Inability to Add External Resistance:** Because the cage is permanently closed, external resistors cannot be connected to increase $R_2$ during starting.
3. **High Inrush Current:** Drawing $5 \text{--} 7\times$ rated current at a poor power factor while stalled under heavy load causes rapid overheating and insulation damage.
* *(Solution: Wound rotor / slip-ring induction motors are used for heavy starting loads).*

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 34, Q.5(c): For an induction motor, prove that maximum torque under running condition varies directly as the square of the applied voltage.

**Proof:**
1. **General Torque Equation:**
   $$T = \frac{3}{\omega_s} \cdot \frac{s E_2^2 R_2}{R_2^2 + (sX_2)^2}$$
   *(where $\omega_s$ = synchronous speed, $s$ = slip, $E_2$ = rotor standstill EMF, $R_2$ = rotor resistance, $X_2$ = rotor standstill reactance).*

2. **Condition for Maximum Torque:**
   Differentiating $T$ with respect to slip $s$ gives maximum breakdown torque at:
   $$s_{max} = \frac{R_2}{X_2}$$

3. **Substitute $s_{max}$ into Torque Equation:**
   $$T_{max} = \frac{3}{\omega_s} \cdot \frac{\left(\frac{R_2}{X_2}\right) E_2^2 R_2}{R_2^2 + \left(\frac{R_2}{X_2} \cdot X_2\right)^2} = \frac{3}{\omega_s} \cdot \frac{\frac{R_2^2}{X_2} E_2^2}{2 R_2^2}$$
   $$T_{max} = \frac{3}{2 \omega_s X_2} \cdot E_2^2$$

4. **Relationship to Supply Voltage ($V$):**
   Rotor induced voltage $E_2$ is directly proportional to stator terminal voltage ($E_2 \propto V$).
   Substituting $E_2 = c V$:
   $$T_{max} = \frac{3 c^2}{2 \omega_s X_2} \cdot V^2$$
   $$\mathbf{T_{max} \propto V^2} \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 34, Q.6(a): With the helps of neat sketch, determine the average torque of an induction motor if the rotor is assumed to be fully inductive. [Figure Involved]

**Determination:**
If the rotor is assumed **fully inductive** ($R_2 = 0$), the average torque developed is **identically zero ($T_{avg} = 0$)**, and the motor cannot turn.

**Explanation:**
1. In a purely inductive rotor circuit, rotor current ($I_2$) lags induced rotor voltage ($E_2$) by exactly $90^\circ$ ($\theta_2 = 90^\circ$).
2. Average torque is proportional to the rotor power factor:
   $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos\theta_2 = \Phi \cdot I_2 \cdot \cos(90^\circ)$$
3. Since $\cos(90^\circ) = 0$:
   $$\mathbf{T_{avg} = 0}$$

* **[Figure Involved]:**
  * Plot Flux wave $\Phi$ (in phase with $E_2$) and Current wave $I_2$ lagging by $90^\circ$.
  * Multiply waves point-by-point to show Torque wave: positive loops ($0^\circ \text{ to } 90^\circ$, $180^\circ \text{ to } 270^\circ$) exactly equal negative loops ($90^\circ \text{ to } 180^\circ$, $270^\circ \text{ to } 360^\circ$).
  * Equal shaded positive and negative areas cancel completely, proving net average torque is zero.
* **References:** AC Induction Motors.

---

### Page 38, Q.5(b): What are the effect of rotor resistance on the developed torque of an induction motor under both starting and running conditions?

**1. Effect on Starting Torque ($s = 1$):**
* Starting torque formula:
  $$T_{st} \propto \frac{R_2}{R_2^2 + X_2^2}$$
* In normal motors, $R_2 \ll X_2$. Increasing $R_2$ improves the starting power factor ($\cos\theta_2$) faster than it increases total impedance.
* **Effect:** Increasing rotor resistance **substantially increases starting torque**, reaching absolute maximum torque when $R_2 = X_2$.

**2. Effect on Running Torque ($s \ll 1$):**
* At normal running speeds, slip is very small ($s \approx 0.02 \text{--} 0.05$), so $(sX_2)^2 \approx 0$:
  $$T \propto \frac{s E_2^2 R_2}{R_2^2} = \frac{s E_2^2}{R_2}$$
* **Effect:** Running torque is *inversely proportional* to rotor resistance. Increasing $R_2$ **decreases running torque** for a given slip; the motor must slow down (higher slip) to deliver load torque, causing higher $I^2R$ copper losses and poor operating efficiency.

* **Figures involved:** Torque-slip family curves for different values of $R_2$.
* **References:** AC Induction Motors.

---

### Page 39, Q.8(d): The following impedances in ohms per phase referred to the stator circuit of a 460V, 25 hp, 60 Hz, 4 pole, Y connected wound rotor induction motor are: R1=0.641Ω , R2=0.332Ω , X1=1.106Ω , X2=0.464Ω , Xm= 26.3Ω. (i) What is the maximum torque of this motor? At what speed and slip does it occur? (ii) When the rotor resistance is doubled, what is the speed at which maximum torque occurs? What is the new starting torque of the motor?

**Solution:**

**Given Parameters (per phase):**
* $V_{LL} = 460\text{ V} \implies V_\phi = \frac{460}{\sqrt{3}} = 265.58\text{ V}$
* $P = 4$, $f = 60\text{ Hz} \implies N_s = \frac{120 \times 60}{4} = 1800\text{ rpm}$, $\omega_s = \frac{1800 \times 2\pi}{60} = 188.5\text{ rad/s}$
* $R_1 = 0.641\,\Omega$, $X_1 = 1.106\,\Omega$, $R_2 = 0.332\,\Omega$, $X_2 = 0.464\,\Omega$, $X_m = 26.3\,\Omega$

**Thevenin Equivalent Calculations:**
$$V_{th} \approx V_\phi \left(\frac{X_m}{X_1 + X_m}\right) = 265.58 \times \frac{26.3}{1.106 + 26.3} = 265.58 \times 0.9596 = \mathbf{254.85\text{ V}}$$
$$R_{th} \approx R_1 \left(\frac{X_m}{X_1 + X_m}\right)^2 = 0.641 \times (0.9596)^2 = \mathbf{0.590\,\Omega}$$
$$X_{th} \approx X_1 = \mathbf{1.106\,\Omega}$$

---

**(i) Maximum Torque, Slip, and Speed:**
* **Slip at Maximum Torque ($S_{max}$):**
  $$S_{max} = \frac{R_2}{\sqrt{R_{th}^2 + (X_{th} + X_2)^2}} = \frac{0.332}{\sqrt{0.590^2 + (1.106 + 0.464)^2}} = \frac{0.332}{\sqrt{0.348 + 2.465}} = \frac{0.332}{1.677} = \mathbf{0.198 \text{ (19.8\%)}}$$
* **Speed at Maximum Torque ($N_{max}$):**
  $$N_{max} = N_s(1 - S_{max}) = 1800(1 - 0.198) = 1800 \times 0.802 = \mathbf{1443.6\text{ rpm}}$$
* **Maximum Torque ($T_{max}$):**
  $$T_{max} = \frac{3 V_{th}^2}{2 \omega_s \left[R_{th} + \sqrt{R_{th}^2 + (X_{th} + X_2)^2}\right]} = \frac{3 \times (254.85)^2}{2 \times 188.5 \times [0.590 + 1.677]} = \frac{194845}{377 \times 2.267} = \mathbf{228.0\text{ N-m}}$$

---

**(ii) When Rotor Resistance is Doubled ($R_2' = 2 \times 0.332 = 0.664\,\Omega$):**
*(Note: Maximum torque magnitude remains unchanged at 228.0 N-m).*
* **New Slip at Maximum Torque ($S_{max}'$):**
  $$S_{max}' = 2 \times S_{max} = 2 \times 0.198 = \mathbf{0.396 \text{ (39.6\%)}}$$
* **New Speed at Maximum Torque ($N_{max}'$):**
  $$N_{max}' = N_s(1 - S_{max}') = 1800(1 - 0.396) = 1800 \times 0.604 = \mathbf{1087.2\text{ rpm}}$$
* **New Starting Torque ($T_{start}'$ at $s = 1$):**
  $$T_{start}' = \frac{3 V_{th}^2 R_2'}{\omega_s \left[(R_{th} + R_2')^2 + (X_{th} + X_2)^2\right]} = \frac{3 \times (254.85)^2 \times 0.664}{188.5 \left[(0.590 + 0.664)^2 + (1.570)^2\right]}$$
  $$T_{start}' = \frac{129377}{188.5 \times [1.572 + 2.465]} = \frac{129377}{188.5 \times 4.037} = \frac{129377}{761.0} = \mathbf{170.0\text{ N-m}}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 42, Q.6(b): Prove that the rotor torque at any slip S can be expressed by the following equation: T = Tb[ 2 / ((Sb/S) + (S/Sb)) ] where the symbols have their usual meanings.

**Proof:**
1. **Torque at any Slip $S$:**
   $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 + (S X_2)^2}$$
2. **Breakdown Torque ($T_b$) Condition:**
   Occurs at breakdown slip $S_b$ where $R_2 = S_b X_2 \implies X_2 = \frac{R_2}{S_b}$.
3. **Substitute $X_2$ into General Torque Equation:**
   $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 + \left(S \frac{R_2}{S_b}\right)^2} = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 \left[1 + \left(\frac{S}{S_b}\right)^2\right]} = \frac{k \cdot S \cdot E_2^2}{R_2 \left[1 + \left(\frac{S}{S_b}\right)^2\right]}$$
4. **Express Breakdown Torque ($T_b$):**
   Substitute $S = S_b$:
   $$T_b = \frac{k \cdot S_b \cdot E_2^2 \cdot R_2}{R_2^2 + (S_b X_2)^2} = \frac{k \cdot S_b \cdot E_2^2 \cdot R_2}{2 R_2^2} = \frac{k \cdot S_b \cdot E_2^2}{2 R_2} \implies \frac{k E_2^2}{R_2} = \frac{2 T_b}{S_b}$$
5. **Combine Equations:**
   $$T = \left(\frac{2 T_b}{S_b}\right) \frac{S}{1 + \left(\frac{S}{S_b}\right)^2} = \frac{2 T_b \left(\frac{S}{S_b}\right)}{1 + \left(\frac{S}{S_b}\right)^2}$$
   Divide numerator and denominator by $\left(\frac{S}{S_b}\right)$:
   $$\mathbf{T = T_b \left[\frac{2}{\frac{S_b}{S} + \frac{S}{S_b}}\right]} \quad \text{(Proved)}$$

* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 45, Q.6(a): With the help of neat sketch determine the average torque of an induction motor if the rotor is assumed fully inductive. [Figure Involved]

**Determination:**
When rotor resistance $R_2 = 0$ (fully inductive), the average developed torque is **identically zero ($T_{avg} = 0$)**.

**Explanation:**
1. A purely inductive circuit causes rotor current $I_2$ to lag induced EMF $E_2$ by $90^\circ$ ($\theta_2 = 90^\circ$).
2. Average torque is:
   $$T_{avg} = K \Phi I_2 \cos\theta_2 = K \Phi I_2 \cos(90^\circ) = 0$$

* **[Figure Involved]:**
  * Draw Flux sine wave $\Phi$ (in phase with $E_2$).
  * Draw Current sine wave $I_2$ lagging by $90^\circ$.
  * Draw Torque wave by multiplying $\Phi \times I_2$: produces symmetrical double-frequency loops where positive area equals negative area, canceling out to zero average torque.
* **References:** AC Induction Motors.

---

### Page 45, Q.6(b): Show that, for obtaining maximum torque of an induction motor at starting ,total resistance must be equal to rotor reactance.

**Proof:**
1. **Starting Torque Equation ($s = 1$):**
   $$T_{st} = \frac{k E_2^2 R_2}{R_2^2 + X_2^2}$$
2. **Condition for Maximum:** Differentiate $T_{st}$ with respect to $R_2$ and equate to zero:
   $$\frac{dT_{st}}{dR_2} = 0$$
3. **Apply Quotient Rule:**
   $$\frac{d}{dR_2} \left[\frac{R_2}{R_2^2 + X_2^2}\right] = \frac{(R_2^2 + X_2^2)(1) - R_2(2R_2)}{(R_2^2 + X_2^2)^2} = 0$$
4. **Equate Numerator to Zero:**
   $$R_2^2 + X_2^2 - 2R_2^2 = 0$$
   $$X_2^2 - R_2^2 = 0 \implies R_2^2 = X_2^2$$
   $$\mathbf{R_2 = X_2} \quad \text{(Proved)}$$

* **Conclusion:** To get maximum torque at start ($s=1$), per-phase rotor resistance must equal per-phase standstill reactance.
* **Figures involved:** None.
* **References:** AC Induction Motors.

---

### Page 46, Q.7(a): Draw the complete torque-slip curve of an induction machine. [Figure Involved]

**Explanation of the Three Regions:**
1. **Motoring Region ($0 < s < 1$):**
   * Normal motor operation ($0 < N < N_s$).
   * Starts at $T_{st}$ ($s = 1$), peaks at Breakdown Torque $T_{max}$ ($s_{max} = R_2/X_2$), and drops to zero at synchronous speed ($s = 0$).
2. **Generating Region ($s < 0$):**
   * Driven by prime mover faster than synchronous speed ($N > N_s$).
   * Slip is negative $\implies$ torque reverses (negative torque). Machine supplies electrical power back to grid.
3. **Braking / Plugging Region ($s > 1$):**
   * Stator field reversed while rotor continues spinning forward ($N < 0$).
   * High opposing torque decelerates the motor rapidly to a stop.

* **[Figure Involved]:** Complete Torque vs. Slip curve spanning:
  * $s < 0$ (Generating region, negative quadrant).
  * $0 < s < 1$ (Motoring region, positive quadrant, peaking at $T_{max}$).
  * $s > 1$ (Braking region, positive torque opposing negative speed).
* **References:** AC Induction Motors.

---

### Page 46, Q.7(c): A 3-Φ, 440V, 50 Hz. 40-pole Y-connected induction motor has rotor resistance of 0.1 ohm and reactance 0.9 ohm per phase. The ratio of stator to rotor turns is 3.5. Calculate (i) gross output at a slip of 5% (ii) the maximum torque in synchronous watts and corresponding slip.

**Solution:**

**Given Data:**
* $V_L = 440\text{ V}$, Frequency $f = 50\text{ Hz}$, Poles $P = 40$
* Turns ratio $a = \frac{N_1}{N_2} = 3.5$
* $R_2 = 0.1\,\Omega$, $X_2 = 0.9\,\Omega$
* Operating slip $s = 5\% = 0.05$

**Step 1: Rotor Phase Voltage at Standstill ($E_2$):**
$$V_{1\phi} = \frac{V_L}{\sqrt{3}} = \frac{440}{\sqrt{3}} = 254.03\text{ V}$$
$$E_2 = \frac{V_{1\phi}}{a} = \frac{254.03}{3.5} = \mathbf{72.58\text{ V per phase}}$$

---

**(i) Gross Mechanical Output at $s = 0.05$:**
* **Rotor Current ($I_2$):**
  $$I_2 = \frac{s E_2}{\sqrt{R_2^2 + (sX_2)^2}} = \frac{0.05 \times 72.58}{\sqrt{(0.1)^2 + (0.05 \times 0.9)^2}} = \frac{3.629}{\sqrt{0.01 + 0.002025}} = \frac{3.629}{0.10966} = \mathbf{33.09\text{ A}}$$
* **3-Phase Gross Mechanical Power ($P_m$):**
  $$P_m = 3 \times I_2^2 R_2 \left(\frac{1 - s}{s}\right) = 3 \times (33.09)^2 \times 0.1 \times \left(\frac{1 - 0.05}{0.05}\right)$$
  $$P_m = 3 \times 1095 \times 0.1 \times 19 = \mathbf{6241.5\text{ W (or 6.24 kW)}}$$

---

**(ii) Maximum Torque and Corresponding Slip:**
* **Slip at Maximum Torque ($s_m$):**
  $$s_m = \frac{R_2}{X_2} = \frac{0.1}{0.9} = \frac{1}{9} = \mathbf{0.1111 \text{ (or 11.11\%)}}$$
* **Maximum Torque in Synchronous Watts ($T_{max}$):**
  $$T_{max} = 3 \times \frac{E_2^2}{2 X_2} = 3 \times \frac{(72.58)^2}{2 \times 0.9} = 3 \times \frac{5267.86}{1.8} = \mathbf{8780\text{ Synchronous Watts}}$$

* **Final Answers:**
  1. Gross mechanical output $= \mathbf{6.24\text{ kW}}$.
  2. Maximum torque $= \mathbf{8780\text{ Synchronous Watts}}$ at slip $= \mathbf{11.11\%}$.
* **Figures involved:** None.
* **References:** AC Induction Motors.
