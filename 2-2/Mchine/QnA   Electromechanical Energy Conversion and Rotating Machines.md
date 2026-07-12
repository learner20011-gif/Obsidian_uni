

***

### Page 5, Q.68: Prove that the electrical power converted into mechanical power is equal to the product of the counter emf and the armature current.

**Solution:**
In a DC motor, the applied terminal voltage ($V$) must overcome both the back electromotive force (counter EMF, $E_b$) and the internal voltage drop across the armature resistance ($I_aR_a$). This relationship is expressed by the fundamental voltage equation of a DC motor:
$V = E_b + I_aR_a$

To determine the power distribution within the motor, we multiply the entire voltage equation by the armature current ($I_a$):
$VI_a = E_bI_a + I_a^2R_a$

By analyzing this power equation, we can define each term:
1. **$VI_a$**: This represents the total electrical power supplied to the armature from the external source.
2. **$I_a^2R_a$**: This represents the electrical power lost as heat due to the internal resistance of the armature windings (armature copper loss).
3. **$E_bI_a$**: According to the law of conservation of energy, the total input power minus the internal heat losses must equal the useful power developed. Therefore, the remaining term, $E_bI_a$, represents the electrical power that is successfully converted into gross mechanical power ($P_m$) within the armature.

Thus, it is proven that the mechanical power developed by the motor is exactly equal to the product of the counter EMF and the armature current ($P_m = E_bI_a$).

**Figures involved:** None.
**References:** Mam Slide: 222-224, Firoz Note: 80-83.

***

### Page 14, Q.3(b): Prove that the gross mechanical power developed by a DC motor is maximum when back emf is equal to half of the applied voltage.

**Solution:**
The gross mechanical power ($P_m$) developed by a DC motor is the product of the back EMF ($E_b$) and the armature current ($I_a$):
$P_m = E_bI_a$

From the standard voltage equation of a DC motor ($V = E_b + I_aR_a$), we can isolate the armature current:
$I_a = \frac{V - E_b}{R_a}$

Substituting this current expression back into the mechanical power equation gives:
$P_m = E_b \left( \frac{V - E_b}{R_a} \right) = \frac{VE_b - E_b^2}{R_a}$

To find the mathematical condition for maximum mechanical power, we take the first derivative of $P_m$ with respect to $E_b$ (treating $V$ and $R_a$ as constants) and set it to zero:
$\frac{dP_m}{dE_b} = \frac{V - 2E_b}{R_a} = 0$

Solving for $E_b$:
$V - 2E_b = 0 \implies 2E_b = V \implies E_b = \frac{V}{2}$

Taking the second derivative ($\frac{d^2P_m}{dE_b^2} = -\frac{2}{R_a}$) yields a negative result, confirming that this point is indeed a mathematical maximum. Therefore, the gross mechanical power developed by a DC motor reaches its theoretical peak when the counter EMF is exactly half of the supply voltage. *(Note: In practical operation, this state is avoided because achieving it requires drawing an enormous armature current, which would cause terrible efficiency and likely overheat the motor).*

**Figures involved:** None.
**References:** Mam Slide: 225, Firoz Note: 85-86.

***

### Page 31, Q.6(c): Prove that, Pm= (1-s)P2 where the symbols have their usual meanings.

**Solution:**
This question explores the power flow within an AC Induction Motor. The standard symbols are defined as:
*   **$P_2$**: Total power transferred across the air-gap to the rotor (Rotor Input Power).
*   **$P_m$**: Gross mechanical power developed by the rotor.
*   **$P_{cr}$**: Rotor copper loss (heat loss in the rotor windings).
*   **$s$**: Fractional slip of the motor.

In an induction motor, the rotor copper loss is directly tied to the slip. Specifically, it is equal to the slip multiplied by the total rotor input power:
$P_{cr} = s P_2$

According to the basic power flow sequence, the gross mechanical power developed is the power remaining after the rotor copper losses have been subtracted from the air-gap power. Therefore:
$P_m = P_2 - P_{cr}$

Substituting the relationship for rotor copper loss into this equation:
$P_m = P_2 - sP_2$

Factoring out $P_2$ yields:
$P_m = P_2(1 - s)$

This proves that the gross mechanical power developed ($P_m$) is equal to $(1-s)$ times the original rotor input power ($P_2$).

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 34, Q.6(b): Explain the relationship between rotor efficiency and slip of an induction motor.

**Solution:**
Rotor efficiency in an induction motor measures how effectively the rotor converts its electrical input power into mechanical output power. It is defined as the ratio of the gross mechanical power developed ($P_m$) to the total power input to the rotor ($P_2$):
$\text{Rotor Efficiency} = \frac{P_m}{P_2}$

From the induction motor power flow relationships, we know that the mechanical power developed is a specific fraction of the rotor input power:
$P_m = P_2(1 - s)$ 

Substituting this mechanical power expression into the efficiency equation gives:
$\text{Rotor Efficiency} = \frac{P_2(1 - s)}{P_2} = 1 - s$

This formula reveals a direct, inverse relationship between rotor efficiency and slip:
1. **Direct Calculation:** The theoretical maximum efficiency of the rotor itself is simply $(1 - s)$. (To get a percentage, multiply by 100).
2. **Inverse Proportionality:** As the slip ($s$) increases, the value of $(1 - s)$ decreases. Therefore, higher slip results in lower rotor efficiency.
3. **Physical Meaning:** Slip represents the relative difference between the synchronous speed and the actual rotor speed. A higher slip means more relative motion, which induces higher currents and drastically increases the $I^2R$ heat losses in the rotor ($sP_2$). To maintain high efficiency, an induction motor is designed to operate at a very low slip under normal operating conditions.

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

Here are the detailed solutions for the next four questions from your syllabus/PYQ list. 

*Note: The first two questions in this set deal with AC Induction Motors, which are not covered in the provided "Mam slide" or "Firoz note" documents (which focus entirely on DC machines). I have provided the standard electrical engineering solutions for these AC machine questions. The latter two questions cover basic principles found in your provided DC machine documents.*

***

### Page 38, Q.6(b): Show that, P2:Pm:Pcr=1:(1-s):s, where P2, Pm and Pcr are respectively the power delivered to the rotor, the gross mechanical power and the rotor core loss.

**Solution:**
*Correction Note: In standard induction motor theory, $P_{cr}$ denotes "Rotor Copper Loss" ($I^2R$ loss), not "rotor core loss". Rotor core losses are generally negligible under running conditions because the rotor frequency ($sf$) is very low. The derivation below proceeds using $P_{cr}$ as Rotor Copper Loss, as this is the standard relationship the formula represents.*

To show the ratio $P_2 : P_m : P_{cr} = 1 : (1-s) : s$, we must define the power flow in the rotor of an induction motor:
1.  **$P_2$ (Rotor Input Power):** This is the air-gap power transferred from the stator to the rotor.
2.  **$P_{cr}$ (Rotor Copper Loss):** The power dissipated as heat in the rotor windings. It is a fundamental property of induction motors that the rotor copper loss is equal to the fractional slip ($s$) multiplied by the rotor input power.
    $P_{cr} = s \times P_2$
3.  **$P_m$ (Gross Mechanical Power):** This is the actual mechanical power developed by the rotor. It is the remaining power after the rotor copper losses have been subtracted from the rotor input power.
    $P_m = P_2 - P_{cr}$

By substituting $P_{cr} = sP_2$ into the mechanical power equation:
$P_m = P_2 - sP_2$
$P_m = P_2(1 - s)$

Now, we can set up the ratio of these three power components:
Ratio = $P_2 : P_m : P_{cr}$

Substitute the expressions derived above into the ratio:
Ratio = $P_2 : P_2(1 - s) : sP_2$

By dividing the entire ratio by $P_2$, we get the final proven relationship:
**Ratio = $1 : (1 - s) : s$**

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 42, Q.6(c): Explain the power flow diagram and prove that Pm=(1-S)P2, for induction motor. [Figure Involved]

**Solution:**
**Explanation of the Power Flow Diagram:**
The power flow diagram of an induction motor illustrates how electrical power drawn from the supply is converted step-by-step into useful mechanical power at the shaft, accounting for losses at each stage.
1.  **Stator Input Power ($P_{in}$):** Three-phase electrical power is supplied to the stator. $P_{in} = \sqrt{3}V_LI_L\cos\theta$.
2.  **Stator Losses:** A portion of $P_{in}$ is lost as heat in the stator windings (Stator Copper Loss, $P_{scl}$) and in the stator core due to hysteresis and eddy currents (Stator Core Loss, $P_{core}$).
3.  **Rotor Input Power / Air-gap Power ($P_2$):** The remaining power is transferred magnetically across the air gap to the rotor. $P_2 = P_{in} - P_{scl} - P_{core}$.
4.  **Rotor Losses:** As power enters the rotor, a portion is lost as heat in the rotor windings (Rotor Copper Loss, $P_{cr}$). As established, $P_{cr} = sP_2$.
5.  **Gross Mechanical Power ($P_m$):** The power left after rotor copper losses is converted into mechanical power.
6.  **Useful Output Power ($P_{out}$):** Finally, mechanical losses (friction and windage) are subtracted from $P_m$ to give the net shaft power available to drive the load.

**Proof that $P_m = (1-s)P_2$:**
From the power flow explained above, the gross mechanical power developed is the difference between the power entering the rotor and the power lost as heat within the rotor's conductors:
$P_m = P_2 - P_{cr}$

We know that the rotor copper loss ($P_{cr}$) is directly proportional to the slip ($s$) and the rotor input power ($P_2$):
$P_{cr} = s \cdot P_2$

Substitute $sP_2$ for $P_{cr}$ in the mechanical power equation:
$P_m = P_2 - sP_2$

Factor out $P_2$:
$P_m = P_2(1 - s)$ (Proved).

**Figures involved:** A block diagram showing the flow of power from Electrical Input $\rightarrow$ Stator Losses $\rightarrow$ Air-gap Power ($P_2$) $\rightarrow$ Rotor Cu Losses $\rightarrow$ Mechanical Power ($P_m$) $\rightarrow$ Friction/Windage Losses $\rightarrow$ Mechanical Output.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 2, Q.1: What are the functions of Generators and Motors?

**Solution:**
Generators and motors are the two primary types of rotating electrical machines, serving opposite functions in energy conversion systems.

**Functions of a Generator:**
*   **Energy Conversion:** The primary function of a generator is to convert mechanical energy into electrical energy.
*   **Power Source:** It acts as a means of supplying electrical power to industrial, commercial, and domestic networks. 
*   **Operation:** A prime mover (such as a diesel engine, steam turbine, wind mill, or mountain stream/hydro plant) provides the mechanical rotation. The generator uses this motion to cut magnetic flux, thereby dynamically inducing an electromotive force (EMF) based on Faraday's law to produce electricity.
*   *Note on DC Generators:* While AC generators (alternators) dominate modern power grids, DC generators are still used in small backup/standby generating plants to provide uninterrupted power supply.

**Functions of a Motor:**
*   **Energy Conversion:** The primary function of a motor is to convert electrical energy into mechanical energy.
*   **Driving Loads:** It is used to drive mechanical loads, creating motion. 
*   **Operation:** When an electric current is supplied to the motor's conductors sitting within a magnetic field, it creates an electromagnetic force (according to Fleming's Left-Hand Rule) that causes the rotor to turn.
*   *Applications:* DC motors are specifically used in applications where large magnitude and precisely controlled torque and wide speed control are required, such as in rolling mills, overhead cranes, electric trains (traction), fork lifts, fans, blowers, and actuators.

**Figures involved:** Simple energy conversion block diagrams (Input: Mechanical Energy $\rightarrow$ Generator $\rightarrow$ Output: Electrical Energy; and Input: Electrical Energy $\rightarrow$ Motor $\rightarrow$ Output: Mechanical Energy).
**References:** 
*   **Mam Slide:** 7, 8, 18
*   **Firoz Note:** 2, 4

***

### Page 2, Q.2: State and Explain Lenz’s law and Faraday’s law of electromagnetic induction.

**Solution:**
These two laws form the fundamental basis for the operation of all rotating electrical machinery.

**Faraday's Law of Electromagnetic Induction:**
Faraday's law explains *how* voltage is induced in a conductor. It consists of two parts:
1.  **First Law:** Whenever the magnetic flux linked with a circuit changes, an electromotive force (e.m.f.) is always induced in it. Alternatively stated: Whenever a conductor cuts across magnetic lines of flux, an e.m.f. is dynamically induced in that conductor.
2.  **Second Law:** The magnitude of the induced e.m.f. is directly proportional (or equal) to the rate of change of flux linkages.
    *   **Explanation:** In a DC generator, the energy conversion relies on this dynamically induced e.m.f. To satisfy Faraday's law, three conditions must be met: (1) a conductor, (2) a magnetic field, and (3) relative motion between the conductor and the magnetic field that produces the "cutting" of flux lines. The magnitude is given by $e = Blv \sin\theta$.

**Lenz's Law:**
Lenz's law determines the *direction* of the induced effects. 
*   **Statement:** "When a conductor is moved through a magnetic field, a voltage is induced in the conductor. If the circuit is closed, the induced voltage will cause a current to flow. The magnetic field produced by this induced current will always *oppose* the motion or the change in flux that produced it."
*   **Explanation:** Lenz's law is a consequence of the conservation of energy. In a generator, the induced current creates a magnetic force that opposes the rotation of the prime mover (this is why turning a loaded generator takes mechanical effort). In a motor, it manifests as the "back e.m.f." or "counter e.m.f." The motor's rotation through its own magnetic field induces a voltage that directly opposes the applied terminal voltage, regulating the amount of current the motor draws.

**Figures involved:** 
*   Faraday's Law: A simple loop rotating between magnetic poles showing cutting of flux. (Mam slide 14, 15)
*   Lenz's Law: Diagrams showing a magnetic North pole moving towards/away from a coil, with the induced current creating a magnetic field to repel/attract the magnet to oppose the motion. (Mam slide 17, 32; Firoz Note 11).
**References:** 
*   **Mam Slide:** 14, 15, 17, 25, 26, 32
*   **Firoz Note:** 6, 11

Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 2, Q.3: How Faradays electromagnetic induction law is related to dc generator?

**Solution:**
Faraday’s law of electromagnetic induction is the fundamental underlying principle of operation for a DC generator. It explains exactly how mechanical energy is converted into electrical energy.

**The Relationship:**
1.  **Creation of EMF (First Law):** Faraday's First Law states that whenever a conductor cuts across magnetic flux, an electromotive force (EMF) is induced in it. In a DC generator, a prime mover (like a turbine or diesel engine) mechanically rotates the armature (which contains a system of copper conductors) inside a stationary magnetic field produced by the stator poles. Because the armature is rotating, its conductors continuously "cut" the magnetic lines of flux. This relative motion strictly satisfies Faraday's condition, causing an alternating EMF to be dynamically induced in the armature windings.
2.  **Magnitude of EMF (Second Law):** Faraday's Second Law dictates that the magnitude of this induced EMF is proportional to the rate at which the magnetic flux is cut. For a single conductor moving in a uniform magnetic field, this is expressed mathematically as $e = Blv \sin\theta$ (where $B$ is flux density, $l$ is conductor length, $v$ is velocity, and $\theta$ is the angle of motion relative to the flux). In the context of the whole generator, this translates to the EMF equation $E = K\phi\omega$ or $E = \frac{\phi Z N}{60} \times (\frac{P}{A})$, showing that the generated voltage depends directly on the magnetic flux ($\phi$) and the speed of rotation ($N$ or $\omega$).

While Faraday's law produces *alternating* current (AC) internally within the rotating loop, the DC generator utilizes a mechanical component called a commutator to rectify this AC into the direct current (DC) that appears at the machine's external terminals.

**Figures involved:** A simple rotating loop between curved magnetic pole faces (N and S) showing the cutting of field lines to induce voltage.
**References:** 
*   **Mam Slide:** 14, 18, 25, 27, 29, 30
*   **Firoz Note:** 6, 7

***

### Page 2, Q.4: State Fleming’s left hand rule and Fleming’s right hand rule. How these rules affect generator and motor actions?

**Solution:**
Fleming's hand rules are mnemonic devices used to determine the direction of induced voltage/current or the direction of motion/force in electromagnetic machines.

**Fleming's Right-Hand Rule (Used for Generator Action):**
*   **Statement:** Stretch the thumb, forefinger (index finger), and middle finger of your *right hand* so that they are mutually perpendicular to each other. If the **forefinger** points in the direction of the magnetic field (North to South) and the **thumb** points in the direction of the motion of the conductor, then the **middle finger** will point in the direction of the induced electromotive force (EMF) or current.
*   **Effect on Generator Action:** In a generator, the magnetic field and the mechanical rotation (motion) are the known inputs. Fleming's Right-Hand Rule determines the output: the direction of the dynamically induced current flowing through the armature conductors. 

**Fleming's Left-Hand Rule (Used for Motor Action):**
*   **Statement:** Stretch the thumb, forefinger, and middle finger of your *left hand* so that they are mutually perpendicular to each other. If the **forefinger** points in the direction of the magnetic field (North to South) and the **middle finger** points in the direction of the current flowing through the conductor, then the **thumb** will point in the direction of the induced mechanical force (motion).
*   **Effect on Motor Action:** In a motor, the magnetic field and the electrical current are the known inputs. Fleming's Left-Hand Rule determines the output: the direction of the force exerted on the armature conductors, which consequently dictates the direction of the motor's mechanical rotation.

**Figures involved:** Diagrams of the right hand and left hand with the thumb, index, and middle fingers extended orthogonally, labeled with Motion/Force, Field, and Current (or EMF).
**References:** 
*   **Mam Slide:** 16, 20, 31, 216
*   **Firoz Note:** 11, 74

***

### Page 2, Q.5: Write down the conditions or requirements to be fulfilled for generator and motor actions.

**Solution:**
For a rotating DC machine to perform the energy conversion necessary to act as either a generator or a motor, specific physical and electrical conditions must be met.

**Requirements for Generator Action (Mechanical to Electrical):**
The energy conversion is based on the principle of dynamically induced EMF (Faraday's Law). The three primary requirements are:
1.  **A Uniform Magnetic Field ($\beta$ or $\phi$):** There must be a magnetic field present, typically produced by stator field windings (electromagnets) or permanent magnets.
2.  **A System of Conductors ($l$):** There must be a circuit or winding (the armature) usually made of copper or aluminum bars placed in the slots of a cylindrical rotor.
3.  **Relative Motion ($v$):** There must be relative motion between the magnetic field and the conductors so that the conductors "cut" the flux lines. This motion is provided mechanically by a prime mover (like a steam turbine, wind turbine, or diesel engine) turning the rotor shaft.

**Requirements for Motor Action (Electrical to Mechanical):**
The energy conversion is based on the principle that a current-carrying conductor in a magnetic field experiences a mechanical force. The two main conditions are:
1.  **A Magnetic Field (flux):** Similar to the generator, a constant magnetic field must be established by the main stator poles.
2.  **A Current-Carrying Conductor:** The armature conductors must have an electrical current flowing through them, which is supplied by an external electrical power source.
*When these two conditions interact, a force ($F = BIl \sin\theta$) is generated according to Fleming's Left-Hand rule, resulting in the rotation of the motor.*

**Figures involved:** Block diagrams showing prime mover input for generators and electrical supply input for motors.
**References:** 
*   **Mam Slide:** 14, 18, 20, 27, 29
*   **Firoz Note:** 7, 72

***

### Page 2, Q.8: Write the functions of commutator and brushes.

**Solution:**
The commutator and brushes are critical mechanical components in DC machines that interface the rotating armature with the stationary external circuitry. 

**Functions of the Commutator:**
*   **Mechanical Rectification (Generator):** In a DC generator, the EMF induced inside the rotating armature coils is inherently alternating (AC) because the conductors pass alternately under North and South poles. The primary function of the commutator is to act as a mechanical rectifier, converting this internal alternating current into a unidirectional (DC) current at the external terminals.
*   **Current Reversal (Motor):** In a DC motor, the commutator's job is to reverse the direction of the current flowing through each armature coil at the exact moment the coil passes from the influence of a North pole to a South pole. This continuous reversal ensures that the torque produced is always in the same direction, allowing for continuous, unidirectional rotation.
*   **Structure:** It is mounted on the shaft and consists of hard-drawn copper segments insulated from each other (and from the shaft) by thin layers of mica.

**Functions of the Brushes:**
*   **Current Collection (Generator):** In a generator, the brushes are held stationary against the rotating commutator. Their function is to collect the generated DC current from the commutator segments and deliver it to the external load circuit.
*   **Current Injection (Motor):** In a motor, the brushes function in reverse. They transfer electrical current from the stationary external DC power supply into the rotating commutator segments, feeding the armature coils.
*   **Structure:** Brushes are typically made of carbon, graphite, or a copper-carbon mix because these materials provide good electrical conductivity while possessing self-lubricating properties, which minimizes wear and tear on the rotating commutator.

**Figures involved:** Split-ring commutator diagrams showing copper segments and mica insulation; diagrams showing stationary brushes riding on the rotating commutator.
**References:** 
*   **Mam Slide:** 44, 45, 62, 63, 76, 78, 186
*   **Firoz Note:** 20, 21, 77
Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 2, Q.9: Explain the working principle of dc generator.

**Solution:**
The working principle of a DC generator is based on **Faraday’s Law of Electromagnetic Induction**, which states that a dynamically induced electromotive force (EMF) is generated in a conductor when it cuts through magnetic lines of flux.

**Detailed Working Principle:**
1.  **Magnetic Field and Motion:** A DC generator consists of a stationary magnetic field (produced by the stator's field windings or permanent magnets) and a rotating armature (a cylindrical rotor containing copper coils) placed within this field. A prime mover (such as a turbine or engine) mechanically rotates the armature.
2.  **Cutting the Flux:** As the armature rotates, its conductors cut across the magnetic field lines. According to Faraday's law, this relative motion induces an alternating EMF within the armature conductors. 
3.  **Direction of Induced EMF:** The direction of this induced current can be determined using **Fleming’s Right-Hand Rule**. As a loop rotates, a specific conductor moves upward past a North pole, and later moves downward past a South pole, causing the induced current to reverse direction internally every half revolution. Therefore, the current generated *inside* the armature is strictly Alternating Current (AC).
4.  **Conversion to DC (Commutation):** To obtain Direct Current (DC) for the external circuit, a mechanical rectifier called a **commutator** is used. The ends of the armature coils are connected to split copper rings (commutator segments) that rotate with the shaft. 
5.  **Brush Action:** Stationary carbon brushes rest against the rotating commutator. The commutator segments are arranged so that just as the internal current in a coil reverses direction, the commutator segment connected to that coil swaps contact from one stationary brush to the other. Consequently, the external circuit connected to the brushes always receives current flowing in one constant direction (unidirectional current). 

**Figures involved:** A schematic of a simple single-loop generator showing the N and S poles, the rotating loop, the split-ring commutator, and the brushes with output waveform graphs showing the transition from internal AC to external DC.
**References:** 
*   **Mam Slide:** 18, 29, 30, 41-43, 45, 46
*   **Firoz Note:** 6, 20

***

### Page 2, Q.12: Name the different essential parts of a dc machine.

**Solution:**
A DC machine (whether acting as a motor or generator) has the same basic construction. It is broadly divided into two main sections: the stationary part (Stator) and the rotating part (Rotor).

The essential parts are:

**A. Stator (Stationary Parts):**
1.  **Yoke (Frame):** The outer protective cover that provides mechanical support and a low-reluctance path for the magnetic flux.
2.  **Pole Cores and Pole Shoes:** The solid or laminated iron structures attached to the yoke that spread the magnetic flux uniformly in the air gap.
3.  **Field Windings (Exciting Coils):** Coils of copper wire wound around the pole cores. When current passes through them, they create the main working magnetic field.
4.  **Brushes and Brush Gear:** Stationary blocks (usually carbon or graphite) held by springs against the commutator to collect or deliver current to the rotating armature.

**B. Rotor (Rotating Parts):**
5.  **Armature Core:** A cylindrical structure keyed to the shaft, made of laminated silicon steel to reduce eddy current losses. It houses the armature windings and provides a low-reluctance path for the flux.
6.  **Armature Windings:** The network of copper coils placed in the slots of the armature core where the actual energy conversion (EMF induction or torque generation) takes place.
7.  **Commutator:** A mechanical rectifier mounted on the shaft, made of wedge-shaped copper segments insulated by mica. It connects the rotating armature coils to the stationary brushes.
8.  **Shaft and Bearings:** The mechanical link that transfers mechanical power (to or from the machine), supported by bearings to ensure free, low-friction rotation.

**Figures involved:** Cutaway view or cross-sectional diagram of a DC machine labeling the yoke, poles, field windings, armature core, commutator, and brushes.
**References:** 
*   **Mam Slide:** 10, 12, 61-66, 67 (Cross-section view)
*   **Firoz Note:** Not explicitly listed in a single consolidated list, but individual components are analyzed throughout the DC machine notes (e.g., commutator on pg 20).

***

### Page 2, Q.13: What are the purposes of Field winding, Armature winding and brushes in d.c machine?

**Solution:**
These three components are the most critical electrical and interface elements of a DC machine.

1.  **Field Winding:**
    *   **Purpose:** Its primary function is to produce the main working magnetic flux ($\phi$) in the air gap of the machine. 
    *   **Explanation:** Wound around the stationary pole cores, these coils act as electromagnets when a direct current (excitation current) is passed through them. Without the magnetic field produced by the field winding, electromagnetic induction (for a generator) or electromagnetic force (for a motor) cannot occur.

2.  **Armature Winding:**
    *   **Purpose:** This is the main energy-converting component of the machine where the actual "work" gets done.
    *   **Explanation:** Housed in the slots of the rotating armature core, it is the circuit that cuts the magnetic flux. In a **generator**, the armature winding is where the electromotive force (EMF) is dynamically induced. In a **motor**, it is the circuit that receives electrical current from the supply; interacting with the main magnetic field to develop the driving mechanical torque.

3.  **Brushes:**
    *   **Purpose:** They provide a sliding electrical connection between the stationary external circuit and the rotating internal circuitry (the commutator).
    *   **Explanation:** In a **generator**, the brushes physically slide against the spinning commutator to *collect* the generated unidirectional current and deliver it to the external load. In a **motor**, they *deliver* the input DC current from an external source to the rotating commutator, which then feeds the armature windings.

**Figures involved:** Diagrams highlighting the locations of the field coils (on stator poles), armature coils (on rotor), and brushes (touching the commutator).
**References:** 
*   **Mam Slide:** 62, 63, 71, 72, 75, 78
*   **Firoz Note:** 27, 28 (Circuit equivalents showing field and armature).

***

### Page 2, Q.14: Why are carbon brushes preferred for dc machines?

**Solution:**
Brushes in DC machines must maintain excellent electrical contact with a rapidly spinning copper commutator without causing excessive friction, wear, or electrical sparking. Carbon (or carbon-graphite mixtures) is overwhelmingly preferred over metals (like copper) for several reasons:

1.  **Self-Lubricating Properties:** Carbon is relatively soft and naturally lubricating. As the commutator rubs against the brush, it creates a thin, smooth patina on the commutator surface. This drastically reduces mechanical friction and prevents the commutator from wearing out quickly.
2.  **Protection of the Commutator:** Because carbon is softer than the hard-drawn copper of the commutator, the brushes wear down instead of the expensive, difficult-to-replace commutator. Replacing a worn carbon brush is cheap and easy.
3.  **High Contact Resistance (Improves Commutation):** Carbon has a higher electrical resistance than copper. During the commutation process, a coil is momentarily short-circuited by the brush. The higher contact resistance of the carbon brush helps limit this short-circuit current, significantly reducing sparking and leading to smoother, "sparkless" commutation.
4.  **Negative Temperature Coefficient:** Unlike most metals, carbon has a negative temperature coefficient of resistance. As friction and electrical currents cause the brush to heat up during normal operation, its resistance actually *decreases*. This helps prevent excessive voltage drops at the brush contacts under heavy load conditions.
5.  **Thermal Stability:** Carbon can withstand the high localized temperatures caused by friction and occasional sparking without melting or fusing (welding) to the copper commutator.

**Figures involved:** None directly necessary, though an image of a brush holder and carbon block could be illustrative.
**References:** 
*   **Mam Slide:** 62, 78 (Mentions materials used for brushes: Carbon, Carbon graphite).
*   **Firoz Note:** 53 (Mentions brush contact resistance in the context of commutation).
Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 2, Q.15: Why the armature core in d.c machines is constructed with laminated steel sheets instead of solid steel sheets?

**Solution:**
The armature core is constructed using thin, laminated steel sheets to drastically reduce **eddy current losses**, which would otherwise cause severe overheating and a massive drop in efficiency.

**Explanation:**
1.  **The Cause of Eddy Currents:** The armature of a DC machine rotates within a stationary magnetic field (produced by the stator poles). Because the armature core is made of a conducting magnetic material (iron/steel) and is rotating, it constantly "cuts" through the magnetic flux. According to Faraday's law of induction, this changing magnetic flux induces an electromotive force (EMF) not only in the copper windings but also in the solid iron body of the core itself.
2.  **The Problem with a Solid Core:** If the armature core were a solid block of steel, it would offer a very low electrical resistance. The induced EMF would cause large, localized circulating currents—called eddy currents—to flow in closed loops throughout the core's volume. Since power loss as heat is calculated by $I^2R$, these massive currents would generate an enormous amount of wasted heat. The formula for eddy current loss is $W_e = k B_{max}^2 f^2 t^2 v$, where $t$ is the thickness of the material.
3.  **The Solution (Laminations):** To solve this, the core is built from many thin slices (laminations) of steel, rather than a solid block. Each lamination is electrically insulated from the adjacent ones by a very thin coating of varnish or an oxide layer. 
4.  **The Result:** This lamination effectively breaks up the large conducting paths into many narrow ones. Because the laminations are thin ($t$ is small), the resistance of the path for the eddy currents becomes very high. This restricts the eddy currents to a very small magnitude, dramatically reducing the $I^2R$ heating loss. 

**Figures involved:** Diagrams showing large circulating eddy currents in a solid block versus restricted, small eddy currents in a laminated block.
**References:**
*   **Mam Slide:** 74, 201 (Equation $W_e \propto t^2$, stating $t$ should be kept as small as possible).
*   **Firoz Note:** 128, 129, 130.

***

### Page 2, Q.16: Why the armature core but not the magnetic pole core of a dc machine must be laminated?

**Solution:**
This comes down to the fundamental requirement for inducing eddy currents: there must be a *changing* magnetic flux ($d\phi/dt$).

**Why the Armature MUST be Laminated:**
As explained in the previous question, the armature is mechanically rotating. As it spins, any specific spot on the armature core continuously moves past North poles and South poles in rapid succession. This means the magnetic flux passing through the armature core is constantly reversing direction. Because the armature core experiences a highly alternating, changing magnetic flux, eddy currents will be induced. Therefore, it absolutely must be laminated to prevent overheating.

**Why the Main Pole Core DOES NOT strictly need Lamination:**
In a standard DC machine, the main stator poles are excited by a steady Direct Current (DC). Consequently, they produce a constant, stationary magnetic field. The magnetic flux passing through the body of the main pole core does *not* change direction or magnitude over time ($d\phi/dt = 0$). Since there is no changing flux within the main pole core body, there is no induced EMF, and therefore no eddy currents are generated within it. Because there are no eddy currents, a solid block of iron or steel is theoretically perfectly fine for the main pole core.

*(Practical Note: While the main body of the pole doesn't need it, the inner face of the pole—the "pole shoe"—is often laminated in modern machines. This is because the slotted armature spinning past the pole face causes tiny, rapid fluctuations in the air-gap flux (called flux pulsations or tufting), which can induce minor eddy currents locally at the pole face).*

**Figures involved:** None.
**References:**
*   **Mam Slide:** Concept derived from the nature of DC field excitation (Slide 71, 74).
*   **Firoz Note:** 129, 130.

***

### Page 3, Q.35: Explain the concept of electrical degrees. How is the electrical angle of the voltage in a rotor conductor related to the mechanical angle of the machine’s shaft?

**Solution:**
In electrical rotating machines, we must distinguish between the physical rotation of the machine and the cycles of the voltage/current generated within it.

**Concept of Electrical Degrees ($\theta_e$):**
Electrical degrees refer to the angle or phase of the alternating current (AC) waveform induced in the machine's conductors. One complete cycle of an AC waveform (a full positive peak and a full negative peak) spans exactly **360 electrical degrees**. In a rotating machine, one full electrical cycle is completed every time a conductor passes under exactly one pair of poles (one North pole and one South pole). 

**Concept of Mechanical Degrees ($\theta_m$):**
Mechanical degrees refer to the actual, physical spatial rotation of the machine's rotor shaft. One complete physical revolution of the rotor is always exactly **360 mechanical degrees**.

**The Relationship:**
The relationship between them depends entirely on how many magnetic poles ($P$) the machine has.
*   In a **2-pole machine** (1 North, 1 South): One full physical revolution ($360^\circ$ mechanical) passes exactly one pair of poles. This generates one full AC cycle ($360^\circ$ electrical). Here, $\theta_e = \theta_m$.
*   In a **4-pole machine** (2 Norths, 2 Souths): One full physical revolution ($360^\circ$ mechanical) passes *two* pairs of poles. This generates *two* full AC cycles. Therefore, 360 mechanical degrees equals 720 electrical degrees ($360^\circ \times 2$).

**Mathematical Equation:**
Because every pair of poles (which is $P/2$) produces 360 electrical degrees for every 360 mechanical degrees of rotation, the general relationship is given by the formula:
**$\theta_e = \frac{P}{2} \times \theta_m$**
*(Where $\theta_e$ is the electrical angle, $\theta_m$ is the mechanical angle, and $P$ is the total number of poles).*

**Figures involved:** 
*   Diagrams of 2-pole, 4-pole, and 6-pole stators alongside sine waves, proving that a 4-pole machine creates 2 electrical cycles per 1 mechanical rotation.
**References:**
*   **Mam Slide:** 87, 88, 89, 91, 92.
*   **Firoz Note:** 19.

***

### Page 3, Q.36: What is the pitch factor of a coil and commutator pitch?

**Solution:**
These are specific terms used in the design of the armature windings.

**1. Pitch Factor ($p$ or $k_p$):**
The pitch factor (also related to coil pitch or coil span) describes how wide a single armature coil is compared to the physical distance between two adjacent magnetic poles. 
*   A "pole pitch" is exactly 180 electrical degrees (the distance from the center of a North pole to the center of the adjacent South pole). 
*   If an armature coil is wound so that its two sides are exactly one pole pitch apart, it is a **full-pitch coil**. The voltages induced in both sides of the coil perfectly add up.
*   If a coil is wound to be slightly narrower than a pole pitch, it is a **fractional-pitch** or **chorded** coil. 
*   The **Pitch Factor** is the ratio of the actual electrical angle spanned by the coil to the full 180-degree pole pitch, expressed as:
    $p = \frac{\text{electrical angle of coil}}{180^\circ}$ (Often multiplied by 100%). It is used to improve commutation and save copper in the winding overhangs.

**2. Commutator Pitch ($Y_c$):**
Commutator pitch is a physical measurement related strictly to the commutator segments on the end of the rotor shaft. 
*   It is defined as the distance—measured in the number of commutator segments—between the two segments to which the starting end and the finishing end of a single armature coil are connected.
*   **For a Lap Winding:** The ends of the coil are connected to adjacent segments. Therefore, the commutator pitch is $Y_c = \pm 1$ (Progressive or Retrogressive).
*   **For a Wave Winding:** The ends of the coil are connected to segments that are roughly two pole-pitches apart. The formula is $Y_c = \frac{2C \pm 1}{P/2}$, where $C$ is the number of coils and $P$ is the number of poles.

**Figures involved:** 
*   Coil span diagram showing 180 degree full pitch (Mam slide 94).
*   Armature winding diagrams showing coil ends connecting to commutator blocks $1$ and $2$ (Lap) vs connecting blocks far apart (Wave).
**References:**
*   **Mam Slide:** 93 (Pitch Factor equation), 107-109 (Commutator pitch $Y_c$).
*   **Firoz Note:** 147 (Definition of Commutator pitch).

Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 3, Q.37: Mention the two types of winding used in the dc machines. How do lap windings differ from wave windings?

**Solution:**
The two basic sequences of armature winding connections used in the rotors of DC machines are **Lap Winding** and **Wave Winding**. (A third, less common hybrid type is the frog-leg winding).

**Differences between Lap and Wave Windings:**

| Feature | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Connection Method** | The finishing end of one coil is connected to the starting end of the adjacent coil under the same pole. The coil "laps" back on itself. | The finishing end of one coil connects to the starting end of another coil under the next pole of the same polarity. It "waves" forward around the armature. |
| **Commutator Pitch ($y_c$)**| Ends connect to adjacent segments: $y_c = \pm 1$ | Ends connect to segments far apart: $y_c = \frac{2C \pm 1}{P/2}$ |
| **Number of Parallel Paths ($A$)**| $A = P$ (Parallel paths always equal the number of poles). | $A = 2$ (There are always exactly 2 parallel paths, regardless of the number of poles). |
| **Voltage & Current Rating**| Designed for **low voltage, high current** machines (because the current splits across many parallel paths, but the voltage is only that of one path). | Designed for **high voltage, low current** machines (because many coils are in series per path building up voltage, but there are only two paths for current). |
| **Equalizer Rings** | **Required** in large machines to balance unequal voltages caused by slight magnetic unbalances between the many parallel paths. | **Not required** (No necessity for equalizer rings as there are only two paths). |
| **Dummy Coils** | Not required. | **May require dummy coils** to mechanically balance the rotor if the number of slots doesn't perfectly fit the wave winding math. |

**Figures involved:** 
*   Winding diagrams showing coils lapping backwards (Lap) vs. waving forwards (Wave).
*   Schematic representation showing coils in parallel (Lap) vs series (Wave).
*   Summary comparison table.
**References:** 
*   **Mam Slide:** 98-100, 104, 111, 118-120
*   **Firoz Note:** Not explicitly detailed in the provided handwritten notes.

***

### Page 3, Q.38: What is the basic difference between lap winding and wave winding? Explain frog-leg winding.

**Solution:**
**Basic Difference:**
As established in the previous question, the fundamental difference lies in how the coils are interconnected and the resulting number of parallel paths ($A$). 
*   **Lap winding** ($A=P$) connects coils in parallel, making it suitable for high-current, low-voltage applications.
*   **Wave winding** ($A=2$) connects coils in series, making it suitable for high-voltage, low-current applications.

**Explanation of Frog-Leg Winding:**
A frog-leg winding is a specialized type of armature winding that is essentially a combination of both a multiplex wave winding and a multiplex lap winding placed on the exact same rotor, in the same slots, and connected to the same commutator.
*   **The Name:** It is called a "frog-leg" winding because the shape of the individual coils used in this setup resembles the legs of a frog.
*   **The Purpose (Self-Equalizing):** The major drawback of standard lap windings in large machines is the absolute necessity of installing external copper "equalizer rings" to prevent destructive circulating currents caused by minor magnetic imbalances. The wave winding portion of a frog-leg setup naturally spans multiple poles, inherently tying together points of equal potential under successive poles. 
*   **Function:** Therefore, the wave winding acts as a built-in equalizer for the lap winding. A frog-leg winding is **100% self-equalizing**, entirely eliminating the need for expensive and complex external equalizer rings.
*   **Number of Paths:** The number of parallel paths in a frog-leg winding is $A = 2 \times P \times m_{lap}$ (where $m_{lap}$ is the plex of the lap winding).

**Figures involved:** Diagram showing the specific "frog-leg" shape of the combined coil.
**References:** 
*   **Mam Slide:** 98, 122, 123
*   **Firoz Note:** 148 (brief mention).

***

### Page 4, Q.40: What is neutral plane? Explain why the brushes of a dc machine must be located in the neutral plane?

**Solution:**
**What is the Neutral Plane?**
*   **Magnetic Neutral Plane (MNP):** In a two-pole machine, this is the geometric axis that is exactly perpendicular (90 electrical degrees) to the main axis of the magnetic flux. 
*   When an armature conductor rotates and passes exactly through this plane, it is moving parallel to the magnetic field lines. Because it is not *cutting* any flux at that precise instant, the dynamically induced voltage in that conductor is exactly **zero**.

**Why Brushes Must be Located in the Neutral Plane:**
The placement of the carbon brushes on the commutator is critical for the smooth operation of the machine. The primary reason they must be placed on the MNP (also called the commutating plane) is to ensure **sparkless commutation**.

1.  **The Commutation Process:** As the armature rotates, the current in any given coil must completely reverse direction as it passes from the influence of a North pole to a South pole. This reversal is facilitated by the commutator segment passing under the stationary brush. During this brief moment, the brush bridges two adjacent commutator segments, effectively **short-circuiting** the coil attached to them.
2.  **The Problem with Off-Neutral Placement:** If the brushes were placed anywhere else, the coil being short-circuited would be actively cutting magnetic flux. Therefore, it would have an active voltage induced in it. Short-circuiting a coil that has an active voltage causes a massive surge of current to flow through the coil and the brush. When the brush finally breaks contact, this large current is interrupted, causing severe, destructive electrical arcing (sparking) at the brush/commutator interface.
3.  **The Solution:** By placing the brushes exactly on the Magnetic Neutral Plane, the coils are only short-circuited at the precise instant when their induced voltage is naturally zero. This allows the current reversal to happen smoothly, without massive short-circuit currents, thereby preventing sparking and prolonging the life of the machine.

*(Note: Under load, a phenomenon called "Armature Reaction" physically twists the magnetic field, causing the MNP to shift. Modern machines use "interpoles" to counteract this and keep the effective neutral plane stationary).*

**Figures involved:** 
*   Diagrams showing the neutral plane perpendicular to the main flux. 
*   Diagrams of brush placement relative to the short-circuited coils.
**References:** 
*   **Mam Slide:** 183-185, 187
*   **Firoz Note:** 56, 57, 58, 62

***

### Page 4, Q.52: Explain the principle of operation of a DC motor.

**Solution:**
The principle of operation of a DC motor is based on the electromagnetic interaction between a magnetic field and a current-carrying conductor.

**Detailed Principle of Operation:**
1.  **The Fundamental Law:** A DC motor operates on the principle that whenever a current-carrying conductor is placed in a magnetic field, it experiences a mechanical force.
2.  **Establishing the Field:** The stator of the motor contains field windings (or permanent magnets). When DC power is supplied to these windings, they create a strong, steady, main magnetic field (flux, $\phi$) across the air gap.
3.  **Applying Armature Current:** The rotating armature consists of many copper coils. The external DC power supply is connected to the stationary brushes, which slide against the rotating commutator. The commutator feeds this current ($I_a$) into the armature coils.
4.  **Generation of Force:** We now have current-carrying conductors sitting inside a magnetic field. According to **Fleming's Left-Hand Rule**, an electromagnetic force is exerted on these conductors. The magnitude of this force on a single conductor is $F = BIl \sin\theta$.
5.  **Generation of Torque:** Because the armature is a cylinder mounted on a central shaft, the force on the conductors on one side of the armature pushes upwards, while the force on the conductors on the opposite side pushes downwards. This creates a twisting force, or **Torque ($\tau$)**, which causes the armature to begin rotating.
6.  **The Role of the Commutator:** As the armature rotates, the conductors that were under a North pole move under a South pole. If the current direction remained the same, the force would reverse, and the motor would stop or oscillate. The commutator acts as a mechanical switch. It physically reverses the direction of the current in each coil just as it crosses the neutral plane between poles. This ensures that the force exerted on the conductors always pushes in the same rotational direction, resulting in continuous, unidirectional rotation.
7.  **Counter-EMF:** Once the motor is spinning, the armature conductors are cutting through the magnetic field. According to Faraday's law, this generates an internal voltage. By Lenz's law, this voltage *opposes* the supply voltage that is causing the rotation. This is called the "Back EMF" or "Counter-EMF" ($E_b$), and it acts as a natural governor, regulating the amount of current the motor draws based on the mechanical load.

**Figures involved:** 
*   Diagram illustrating Fleming's Left-Hand Rule.
*   Cross-section of a 2-pole motor showing current directions (crosses and dots) and the resulting rotational force.
**References:** 
*   **Mam Slide:** 20, 21, 214-216, 218-221
*   **Firoz Note:** 72, 74-78

Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 8, Q.8(b): Define universal motor. Differentiate universal motor from a dc series motor and also mention its applications.

**Solution:**
*Note: Universal motors are a specific subset of AC/DC machines. While not heavily detailed in the core DC machine notes provided, standard electrical engineering definitions apply here.*

**Definition of a Universal Motor:**
A Universal motor is a type of electric motor that is designed to operate on either direct current (DC) or single-phase alternating current (AC) power at approximately the same speed and output. It is essentially a specially modified DC series motor. Because the armature windings and field windings are connected in series, the current flowing through both reverses simultaneously when operated on AC. Therefore, the magnetic torque remains in the same direction, allowing the motor to spin continuously.

**Differentiation from a Standard DC Series Motor:**
While identical in basic circuit topology (armature in series with the field), a universal motor has specific design modifications to allow it to run efficiently on AC:
1.  **Laminated Stator:** A standard DC series motor usually has a solid yoke/stator core because the field flux is constant. A universal motor **must** have its entire magnetic circuit (stator pole cores and yoke) laminated to reduce severe eddy current losses caused by the alternating magnetic flux.
2.  **Fewer Field Turns:** Universal motors are wound with fewer turns on the field poles to reduce the overall inductance (and therefore inductive reactance) of the machine, which helps maintain a higher power factor when running on AC.
3.  **Compensating Windings:** To counteract the heavy armature reaction and improve poor commutation caused by the AC operation, larger universal motors often employ compensating windings embedded in the pole faces.
4.  **Air Gap:** The air gap is generally kept smaller in a universal motor to reduce the reluctance of the magnetic path, compensating for the weaker field (due to fewer turns).

**Applications of Universal Motors:**
Universal motors are characterized by high starting torque, very high operating speeds (often exceeding 10,000 RPM), and compact size. They are widely used in portable appliances where high power-to-weight ratios are needed:
*   Portable power tools (drills, circular saws, routers, grinders).
*   Domestic appliances (vacuum cleaners, blenders, food mixers, sewing machines).
*   Hair dryers.

**Figures involved:** None directly necessary, though a simple schematic showing series connection is standard.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 9, Q.5(a): Describe the construction and working principle of DC motor.

**Solution:**
*(Note: This is a synthesis of previous answers regarding the structure and operation of DC machines).*

**A. Construction of a DC Motor:**
A DC motor consists of two main assemblies: a stationary stator and a rotating rotor.
1.  **Stator (Stationary Part):**
    *   **Yoke:** The outer cylindrical frame providing mechanical protection and a path for the magnetic flux.
    *   **Poles and Pole Shoes:** Iron cores attached to the yoke that project inwards, spreading flux evenly across the air gap.
    *   **Field Windings:** Copper coils wrapped around the poles. When fed with DC, they act as electromagnets to create the main stationary magnetic field.
    *   **Brushes:** Carbon blocks held stationary against the commutator, used to supply external DC power into the rotating machine.
2.  **Rotor (Rotating Part):**
    *   **Armature Core:** A cylindrical, laminated steel drum with slots cut into its periphery to hold the windings. Lamination reduces eddy current losses.
    *   **Armature Windings:** The copper coils placed in the slots where the electromagnetic force is generated.
    *   **Commutator:** A mechanical cylinder made of insulated copper segments mounted on the shaft. It acts as a rotary switch.

**B. Working Principle of a DC Motor:**
1.  **The Core Principle:** When a current-carrying conductor is placed within a magnetic field, it experiences a mechanical force. The direction of this force is given by **Fleming's Left-Hand Rule**.
2.  **Operation:** 
    *   DC power is supplied to the field windings, establishing a constant magnetic field (N to S).
    *   DC power is simultaneously supplied via the brushes and commutator to the armature windings.
    *   The interaction of the armature current and the main magnetic field produces an electromagnetic force ($F=BIl$) on the armature conductors. 
    *   Conductors under the North pole are pushed in one direction, while those under the South pole are pushed in the opposite direction. This opposing pair of forces creates a twisting moment, or **torque**, causing the armature to rotate.
3.  **The Commutator's Role:** To keep the motor spinning continuously in one direction, the current in each individual armature coil must reverse right as the coil passes the neutral plane between the N and S poles. The rotating commutator automatically breaks and reconnects the circuit with the stationary brushes at precisely the right moment to reverse this current, ensuring constant, unidirectional torque.
4.  **Back EMF:** As the motor spins, its conductors cut the magnetic field, generating a voltage that opposes the supply voltage (Lenz's Law). This Counter-EMF limits the current drawn by the motor, effectively regulating its speed based on the mechanical load applied to the shaft.

**Figures involved:** Cross-sectional diagram of a DC machine; diagram illustrating Fleming's Left-Hand rule and the generation of torque on a loop.
**References:** 
*   **Mam Slide:** 62, 63, 65 (Construction); 20, 21, 214-221 (Working Principle).
*   **Firoz Note:** 72, 74-78.

***

### Page 12, Q.1(d): What is the essential difference between lap and wave windings? The armature of a 4 pole dc shunt generator is lap-wound and generates 216V when running at 600 rpm. Armature has 144 slots, with 6 conductors per slot. If this armature rewound to wave-connected, find the emf generated with the same flux per pole but running at 500 rpm.

**Solution:**

**Part 1: Essential Difference between Lap and Wave Windings**
The fundamental difference lies in how the coils are connected to the commutator, which dictates the number of parallel paths ($A$) the current can take through the armature.
*   **Lap Winding:** The coils overlap. It creates a number of parallel paths equal to the number of magnetic poles ($A = P$). It is used for **low voltage, high current** machines.
*   **Wave Winding:** The coils progress forward in a wave-like manner. It creates exactly **two** parallel paths ($A = 2$) regardless of the number of poles. It is used for **high voltage, low current** machines.

**Part 2: Calculation**
We use the standard EMF equation for a DC generator:
$E = \frac{\phi Z N P}{60 A}$

**Given Initial Parameters (Lap Wound):**
*   Poles ($P$) = 4
*   Winding Type: Lap $\Rightarrow$ Parallel paths ($A_1$) = $P = 4$
*   Generated EMF ($E_1$) = 216 V
*   Speed ($N_1$) = 600 rpm
*   Total Conductors ($Z$) = Slots $\times$ Conductors/slot = $144 \times 6 = 864$

**Step A: Find the flux per pole ($\phi$) using the initial lap winding state.**
$E_1 = \frac{\phi Z N_1 P}{60 A_1}$
$216 = \frac{\phi \times 864 \times 600 \times 4}{60 \times 4}$
$216 = \phi \times 864 \times 10$
$216 = 8640 \phi$
$\phi = \frac{216}{8640} = 0.025$ Webers (Wb)

**Given New Parameters (Wave Wound):**
*   Poles ($P$) = 4 (unchanged)
*   Winding Type: Wave $\Rightarrow$ Parallel paths ($A_2$) = 2
*   Speed ($N_2$) = 500 rpm
*   Total Conductors ($Z$) = 864 (unchanged)
*   Flux ($\phi$) = 0.025 Wb (unchanged)

**Step B: Calculate the new generated EMF ($E_2$) for the wave winding state.**
$E_2 = \frac{\phi Z N_2 P}{60 A_2}$
$E_2 = \frac{0.025 \times 864 \times 500 \times 4}{60 \times 2}$
$E_2 = \frac{43200}{120}$
**$E_2 = 360$ Volts**

**Alternative (Ratio) Method:**
Since $Z$, $P$, and $\phi$ are constant, $E \propto \frac{N}{A}$.
$\frac{E_2}{E_1} = \frac{N_2 / A_2}{N_1 / A_1} = \left(\frac{N_2}{N_1}\right) \times \left(\frac{A_1}{A_2}\right)$
$\frac{E_2}{216} = \left(\frac{500}{600}\right) \times \left(\frac{4}{2}\right) = \left(\frac{5}{6}\right) \times 2 = \frac{10}{6}$
$E_2 = 216 \times \left(\frac{10}{6}\right) = 36 \times 10 = \mathbf{360 \text{ V}}$

**Figures involved:** None required for the calculation.
**References:** 
*   **Mam Slide:** 100, 111, 119 (Winding differences), 125, 126 (EMF Equation).
*   **Firoz Note:** 25, 26.

***

### Page 12, Q.2(a): Differentiate between lap winding and wave winding of a DC machine.

**Solution:**
*(Note: This is a direct duplicate of the core concepts asked in Page 3, Q.37 and the first half of Page 12, Q.1(d). The standard tabular differentiation is the expected answer format here).*

Here is a summary table differentiating the two winding types used in DC armatures:

| Parameter | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Connection geometry** | Coils overlap each other; finishing end connects to starting end of adjacent coil. | Coils progress forward around the armature; finishing end connects to a coil under the next pole. |
| **Parallel Paths ($A$)** | $A = P$ (Number of paths equals number of magnetic poles). | $A = 2$ (Always two paths, regardless of the number of poles). |
| **Number of Brushes** | Requires brushes equal to the number of poles ($P$). | Strictly requires only 2 brushes (though $P$ brushes are often used in large machines to reduce current density per brush). |
| **Application** | Ideal for **low voltage, high current** machines (e.g., automobile starter motors). | Ideal for **high voltage, low current** machines (e.g., small generators). |
| **Equalizer Rings** | **Required** in large machines to prevent circulating currents caused by slight magnetic unbalances between the many paths. | **Not required**. |
| **Dummy Coils** | Not required. | Sometimes required to achieve mechanical balance if slots aren't completely filled. |

**Figures involved:** None strictly required, though a comparison table is standard.
**References:** 
*   **Mam Slide:** 98-100, 104, 111, 118-120
*   **Firoz Note:** Not explicitly detailed in the provided handwritten notes.


Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

*Note: The first two questions are identical to concepts covered previously but are answered fully here for your convenience. The last two questions deal with AC Induction Motors, which are not covered in the provided "Mam slide" or "Firoz note" documents (which focus entirely on DC machines). I have provided the standard electrical engineering solutions for these AC machine questions.*

***

### Page 25, CT#1 Q.1: Explain – (i) Faraday’s law of electromagnetic induction, (ii) Lenz’s law, (iii) Flemming’s right hand rule.

**Solution:**
These three fundamental laws form the basis for the operation of all rotating electromagnetic generators and motors.

**(i) Faraday’s Law of Electromagnetic Induction:**
Faraday's law explains how a voltage (EMF) is generated in a magnetic field. It is divided into two parts:
*   **First Law:** Whenever the magnetic flux linked with a closed circuit changes, an electromotive force (EMF) is induced in it. Alternatively, if a conductor physically moves through a magnetic field and "cuts" the flux lines, an EMF is dynamically induced in that conductor.
*   **Second Law:** The magnitude of the induced EMF is directly proportional to the rate of change of flux linkages. Mathematically, $E = N \frac{d\phi}{dt}$ (where $N$ is the number of turns and $d\phi/dt$ is the rate of change of flux). In a rotating machine, this is equivalent to $E = Blv\sin\theta$.

**(ii) Lenz’s Law:**
Lenz's law determines the direction of the effect produced by Faraday's law. It is a direct consequence of the conservation of energy.
*   **Statement:** The direction of an induced EMF (and the resulting induced current, if the circuit is closed) will always be such that the magnetic field it creates will *oppose* the change in flux or the physical motion that produced it. 
*   **Explanation:** In a generator, the current induced in the armature creates a magnetic force that physically resists the rotation of the prime mover. In a motor, the rotation of the armature induces a "back EMF" that pushes against the applied supply voltage.

**(iii) Fleming’s Right Hand Rule:**
This is a visual mnemonic used to find the direction of the dynamically induced current in a **generator**.
*   **Statement:** Hold your right hand and extend the thumb, forefinger (index finger), and middle finger so that they are all mutually perpendicular to one another (at 90-degree angles). 
*   If the **Forefinger** points in the direction of the magnetic **Field** (North to South), and the **Thumb** points in the direction of the **Motion** of the conductor, then the **Middle finger** will point in the direction of the induced **Current** (or EMF).

**Figures involved:** 
*   Diagrams of a loop cutting flux for Faraday's law.
*   A magnet approaching/receding from a coil for Lenz's law. 
*   An illustration of a right hand with the thumb (Motion), index (Field), and middle finger (Current) extended at right angles.
**References:** 
*   **Mam Slide:** 14, 15, 16, 17, 25, 26, 31, 32
*   **Firoz Note:** 6, 11, 74

***

### Page 25, CT#1 Q.2: Differentiate between lap and wave winding.

**Solution:**
Lap and wave windings are the two primary ways to interconnect the armature coils to the commutator in a DC machine. The primary difference lies in the resulting number of parallel paths ($A$) for the armature current.

| Feature | Lap Winding | Wave Winding |
| :--- | :--- | :--- |
| **Connection Method** | The finishing end of one coil connects to the starting end of the adjacent coil under the same pole. The winding folds or "laps" back on itself. | The finishing end of one coil connects to the starting end of a coil located under the next pole of the same polarity. It travels forward in a "wave". |
| **Number of Parallel Paths ($A$)** | $A = P$ (The number of parallel paths is always equal to the number of magnetic poles). | $A = 2$ (There are always exactly two parallel paths, regardless of how many poles the machine has). |
| **Commutator Pitch ($Y_c$)** | $Y_c = \pm 1$ (Connected to adjacent commutator segments). | $Y_c = \frac{2C \pm 1}{P/2}$ (Connected to segments that are nearly two pole-pitches apart). |
| **Current and Voltage Rating** | Used for **high-current, low-voltage** machines. (Total current splits across many parallel paths, but voltage is limited to one path). | Used for **low-current, high-voltage** machines. (Many coils are in series boosting the voltage, but current capacity is limited to only two paths). |
| **Number of Brushes** | Requires brushes equal to the number of poles ($P$). | Only 2 brushes are strictly required (though more are often used in large machines to reduce current density at the brush contact). |
| **Equalizer Rings** | **Required** in large machines to balance circulating currents caused by slight differences in flux between the multiple parallel paths. | **Not required**. |
| **Dummy Coils** | Not required. | May be required to mechanically balance the rotor if the number of slots doesn't perfectly match the winding calculation. |

**Figures involved:** Winding diagrams showing the "lapping" backward shape versus the "waving" forward shape.
**References:** 
*   **Mam Slide:** 98-100, 104, 111, 118-120
*   **Firoz Note:** Not explicitly covered in the provided handwritten notes.

***

### Page 34, Q.5(a): Does the induction motor rotates at the synchronous speed? Comment your answer.

**Solution:**
**No, an induction motor never rotates at the synchronous speed.** 

**Detailed Comment/Explanation:**
The operation of an induction motor relies entirely on the principle of electromagnetic induction (Faraday's Law). 
1.  When 3-phase AC power is applied to the stator, it creates a rotating magnetic field that spins at a specific speed called the **synchronous speed ($N_s$)**.
2.  This rotating magnetic field sweeps past the stationary rotor conductors, "cutting" them. This cutting action induces an EMF in the rotor conductors.
3.  Because the rotor circuit is closed (short-circuited), this induced EMF causes a rotor current to flow. This current generates its own magnetic field, which interacts with the stator's rotating field to produce torque, causing the rotor to spin in the same direction as the magnetic field at a speed $N_r$.
4.  **Why $N_r$ can never equal $N_s$:** If the rotor were to somehow accelerate and reach the exact same speed as the rotating magnetic field ($N_r = N_s$), the relative speed between the rotor conductors and the magnetic field would drop to zero. 
5.  If the relative speed is zero, the rotor conductors are no longer "cutting" any magnetic flux lines. According to Faraday's law, the induced EMF in the rotor drops to zero.
6.  With zero induced EMF, the rotor current drops to zero. Consequently, the electromagnetic torque drops to zero. 
7.  Without torque to overcome mechanical friction and the load, the rotor will immediately slow down. As it slows down ($N_r < N_s$), the relative speed increases again, flux is cut, EMF is induced, torque is generated, and the motor continues to spin.

The difference between the synchronous speed and the actual rotor speed is called **slip**. An induction motor *must* have a positive slip to produce torque, meaning it must always rotate slightly slower than synchronous speed.

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 38, Q.6(a): What are the differences between a squirrel cage and wound rotor induction motor?

**Solution:**
Both are types of 3-phase AC induction motors, but they differ fundamentally in the construction of their rotors.

**1. Squirrel Cage Induction Motor:**
*   **Rotor Construction:** The rotor consists of a laminated cylindrical iron core with slots. Instead of wire windings, heavy solid bars of aluminum or copper are placed in the slots. These bars are permanently short-circuited at both ends by heavy metallic "end rings." The resulting structure looks like a hamster wheel or "squirrel cage."
*   **External Resistance:** Because the rotor bars are permanently shorted by the end rings, it is impossible to add any external resistance to the rotor circuit.
*   **Starting Characteristics:** It has a relatively low starting torque and draws a very high starting current (typically 5 to 7 times the full-load current).
*   **Speed Control:** Speed control is difficult and limited.
*   **Maintenance & Cost:** Very simple, incredibly rugged, virtually maintenance-free (no brushes or slip rings to wear out), and cheaper to manufacture.

**2. Wound Rotor (Slip Ring) Induction Motor:**
*   **Rotor Construction:** The rotor has a laminated core with slots, but it contains a proper 3-phase distributed winding made of insulated copper wire, similar to the stator winding. The winding is typically Y-connected.
*   **External Resistance:** The three ends of the rotor winding are brought out along the shaft and connected to three insulated slip rings. Stationary carbon brushes press against these slip rings, allowing the rotor circuit to be connected to an external 3-phase variable resistor bank.
*   **Starting Characteristics:** By adding high external resistance to the rotor circuit during startup, the starting current is drastically reduced, and the starting torque is significantly increased (it can reach maximum torque at startup). As the motor speeds up, this external resistance is gradually shorted out.
*   **Speed Control:** Better speed control can be achieved by varying the external resistance in the rotor circuit.
*   **Maintenance & Cost:** More complex construction, higher initial cost, and requires regular maintenance due to the wear and tear of the slip rings and carbon brushes.

**Figures involved:** None required, though diagrams of a squirrel cage rotor vs. a wound rotor with slip rings are standard for this comparison.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

Here are the detailed solutions for the next four questions from your syllabus/PYQ list. 

*Note: The first question in this set deals with an AC Induction Motor, which is not covered in the provided "Mam slide" or "Firoz note" documents (as they focus entirely on DC machines). I have provided the standard electrical engineering solution for it. The subsequent three questions return to the fundamental principles of DC machines.*

***

### Page 41, Q.5(a): Develop an equivalent circuit for three phase induction motor. State the difference between exact and approximate equivalent circuit. [Figure Involved]

**Solution:**
**Developing the Equivalent Circuit:**
An induction motor is essentially a rotating transformer where the stator acts as the primary winding and the rotor acts as a short-circuited secondary winding.
1.  **Stator Circuit:** When 3-phase voltage ($V_1$) is applied to the stator, it draws a current. The stator winding has its own resistance ($R_1$) and leakage reactance ($X_1$). It also draws a no-load excitation current to establish the magnetic core flux and overcome core losses; this is represented by a shunt magnetizing branch consisting of a core loss resistance ($R_c$) in parallel with a magnetizing reactance ($X_m$).
2.  **Rotor Circuit:** The rotating magnetic field induces an EMF in the rotor ($E_2$). The rotor has its own resistance ($R_2$) and leakage reactance ($X_2$). Because the rotor is turning at a slip $s$, the frequency of the rotor currents is $sf$, which means the actual rotor reactance is $sX_2$ and the induced voltage is $sE_2$.
3.  **Combining (Referring to Stator):** To make calculations easier, the rotor parameters are "referred" to the stator side (just like secondary values are referred to the primary in a transformer) using the effective turns ratio. By dividing the rotor voltage equation by slip $s$, we can represent the mechanical load as a purely electrical resistance. The equivalent rotor resistance becomes $R_2'/s$. This can be split into two parts: $R_2'$ (the actual rotor copper loss) and $R_2'(\frac{1-s}{s})$ (a fictitious resistance representing the mechanical power output).

**Difference Between Exact and Approximate Equivalent Circuit:**
*   **Exact Equivalent Circuit:** In the exact circuit, the shunt magnetizing branch ($R_c$ and $X_m$) is placed *between* the stator impedance ($R_1 + jX_1$) and the referred rotor impedance. This is physically accurate because the voltage that drives the magnetizing branch is the air-gap voltage ($E_1$), which is the terminal voltage $V_1$ minus the drop across the stator impedance. However, calculating parallel branches in the middle of the circuit makes manual mathematical analysis tedious.
*   **Approximate Equivalent Circuit:** To drastically simplify calculations, the shunt magnetizing branch is shifted to the very front of the circuit, placing it directly across the supply terminals ($V_1$). 
    *   *Why this is acceptable:* In large motors, the voltage drop across $R_1$ and $X_1$ due to the small no-load current is very small. Assuming the magnetizing branch sees the full $V_1$ instead of $E_1$ introduces only a tiny error but makes the series branch ($R_1, X_1, R_2', X_2'$) an easily solvable single series-parallel loop.

**Figures involved:** 
1. The **Exact Equivalent Circuit** showing the shunt branch in the middle.
2. The **Approximate Equivalent Circuit** showing the shunt branch shifted to the input terminals.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 2, Q.6: Show that the voltage induced in a conductor rotating in a magnetic field is alternating in nature. How the alternating voltage induced in the conductor can be made unidirectional? Show by neat sketch. [Figure Involved]

**Solution:**
**1. Why the induced voltage is alternating in nature:**
Consider a single rectangular coil of wire rotating at a constant speed within a uniform, stationary magnetic field (between a North and a South pole). 
*   As the coil rotates, the conductors on one side of the loop move *upward* through the magnetic flux (e.g., passing the North pole). According to Faraday's Law and Fleming's Right-Hand Rule, this induces an EMF in a specific direction (let's say, 'positive').
*   When the coil rotates exactly 180 degrees later, that very same conductor is now passing the South pole and moving *downward* through the magnetic flux. Because the direction of physical motion relative to the magnetic field has reversed, Fleming's Right-Hand Rule dictates that the induced EMF must also reverse its direction ('negative').
*   Because the conductor continually alternates between passing a North pole and a South pole, the induced voltage smoothly rises to a positive peak, falls to zero at the neutral axis, drops to a negative peak, and returns to zero. This forms a complete, alternating sinusoidal (AC) wave.

**2. Making the voltage unidirectional (DC):**
To convert this internal AC voltage into unidirectional (DC) voltage for an external circuit, a mechanical device called a **split-ring commutator** is used. 
*   Instead of solid slip rings, the ends of the coil are connected to a single ring that is split into two insulated halves. 
*   Two stationary carbon brushes press against these rotating split rings.
*   The split rings are aligned so that at the exact moment the coil passes the neutral axis (where the internal voltage drops to zero and is about to reverse its direction), the rotating gap between the split rings passes the stationary brushes. 
*   This means the brush connection swaps from one end of the coil to the other just as the current reverses. The "positive" brush is always in contact with whichever coil side is moving upward, and the "negative" brush is always in contact with the coil side moving downward. As a result, the external circuit only ever sees a pulsating, but strictly unidirectional (DC) voltage.

**Figures involved:** 
1. Sketch of a simple rotating loop with slip-rings producing a sine-wave AC output.
2. Sketch of the same loop with a split-ring commutator producing a pulsating unidirectional (DC) output. 
**References:** 
*   **Mam Slide:** 35-43 (especially 41, 42, 43, 45)
*   **Firoz Note:** 20, 21

***

### Page 2, Q.7: How can a commutator convert ac voltages on a machine’s armature to dc voltages at its terminals?

**Solution:**
A commutator achieves the conversion of AC to DC through a synchronized mechanical switching action. It acts as a mechanical rotary rectifier.

**The Conversion Process:**
1.  **Internal AC Generation:** As established, the armature coils of a DC generator physically rotate through alternating North and South magnetic poles. This causes the induced current *inside* the armature coils to constantly alternate back and forth (AC).
2.  **Commutator Construction:** The commutator is a cylinder mounted on the rotor shaft, consisting of multiple hard-drawn copper segments insulated from one another by thin strips of mica. Each segment is soldered to the ends of the armature coils.
3.  **Stationary Brushes:** Carbon brushes are fixed in space and press against the outer surface of the rotating commutator. They act as the electrical bridge to the external load.
4.  **The Switching Action (Commutation):** The brushes are strategically positioned exactly on the Magnetic Neutral Plane (MNP). The MNP is the point in rotation where the armature coil is moving parallel to the magnetic field, meaning its induced voltage is momentarily zero and is just about to reverse direction.
5.  **Reversing the Connection:** As the armature rotates past this neutral plane, the internal current in a specific coil begins to reverse. Simultaneously, because the commutator is rotating with the armature, the commutator segments attached to that specific coil slide past the stationary brushes. The brush breaks contact with one segment and makes contact with the next one.
6.  **Unidirectional Output:** Because the switching of the physical connection (via the commutator segments sliding under the brushes) happens at the exact same instant that the internal current direction reverses, the output delivered to the stationary brushes never reverses. One brush will always collect current flowing *out* of the armature, and the other will always deliver current flowing *into* the armature, resulting in a steady, unidirectional (DC) voltage at the terminals.

**Figures involved:** A sequence of diagrams showing a coil connected to a split-ring commutator at different rotational angles, illustrating how the brushes swap segments to keep the external current flowing in one direction.
**References:** 
*   **Mam Slide:** 42, 43, 44, 45, 46
*   **Firoz Note:** 20, 21, 77

***

### Page 2, Q.10: Prove that, E = Blvsinθ, where the symbols have their usual meaning.

**Solution:**
This proof relies on Faraday's Law of Electromagnetic Induction, which states that the induced EMF is equal to the rate at which magnetic flux is cut by a conductor.

**Proof:**
1.  **Define the variables:**
    *   $B$: Magnetic flux density (in Tesla or Webers/m²).
    *   $l$: Active length of the conductor situated within the magnetic field (in meters).
    *   $v$: Linear velocity of the conductor moving through the field (in meters/second).
    *   $\theta$: The angle between the direction of the conductor's motion (velocity vector) and the direction of the magnetic field lines.
2.  **Determine Flux Cut:** Imagine the conductor moving a tiny distance $dx$ in a small increment of time $dt$. Because velocity $v = \frac{dx}{dt}$, the distance moved is $dx = v \cdot dt$.
3.  **Determine Area Swept:** As the conductor moves, it sweeps out a certain area in the magnetic field. However, only the component of motion strictly perpendicular to the magnetic field lines results in flux cutting. The effective perpendicular distance moved is $dx \cdot \sin\theta = v \cdot dt \cdot \sin\theta$.
    Therefore, the effective Area swept ($A$) by the conductor length $l$ in time $dt$ is:
    $A = l \cdot (v \cdot dt \cdot \sin\theta)$
4.  **Calculate Change in Flux ($d\Phi$):** Magnetic flux $\Phi$ is the product of Flux Density ($B$) and Area ($A$). 
    The small amount of flux cut by the conductor in time $dt$ is:
    $d\Phi = B \cdot A = B \cdot (l \cdot v \cdot dt \cdot \sin\theta)$
5.  **Apply Faraday's Law:** Faraday's law states the magnitude of induced EMF ($E$) is the rate of change of flux linkages ($\frac{d\Phi}{dt}$).
    $E = \frac{d\Phi}{dt} = \frac{B \cdot l \cdot v \cdot \sin\theta \cdot dt}{dt}$
6.  **Final Equation:** The $dt$ terms cancel out, leaving the final expression for motional EMF:
    **$E = Blv \sin\theta$**

*(Note: In vector calculus terms, as shown in the notes, this is the scalar magnitude derived from the cross product of velocity and magnetic field vectors dotted with the length vector: $e_{ind} = (\vec{v} \times \vec{B}) \cdot \vec{l}$ ).*

**Figures involved:** A diagram showing a straight conductor of length $l$ moving at velocity $v$ at an angle $\theta$ relative to parallel magnetic field lines $B$.
**References:** 
*   **Mam Slide:** 18, 50
*   **Firoz Note:** 8, 9, 10


Here are the detailed solutions for the next four questions from your syllabus/PYQ list. 

*Note: The first two questions deal with the fundamental EMF equations of DC machines (covered in your provided course materials). The last two questions relate to AC Induction Motors, which are not present in the provided "Mam slide" or "Firoz note" documents. I have provided the standard engineering solutions for those two regardless.*

***

### Page 2, Q.11: Show that the voltage generated by a dc generator is given by E =kφS where the symbols have their usual meaning.

**Solution:**
This requires deriving the fundamental Electromotive Force (EMF) equation for a DC generator and then grouping the physical constants of the machine.

**Step-by-step Derivation:**
Let us define the standard symbols:
*   $\phi$ = Useful magnetic flux produced per pole (in Webers, Wb).
*   $P$ = Total number of magnetic poles in the generator.
*   $Z$ = Total number of active armature conductors.
*   $A$ = Number of parallel paths in the armature winding (For Lap winding, $A=P$; for Wave winding, $A=2$).
*   $S$ = Speed of rotation of the armature (in revolutions per minute, rpm). 

1. **Calculate the flux cut in one revolution:**
When a single armature conductor completes one full mechanical revolution, it passes under all $P$ poles. Therefore, the total magnetic flux cut by one conductor in one revolution is:
$d\Phi = P \times \phi$ 

2. **Calculate the time taken for one revolution:**
Since the armature rotates at $S$ revolutions per minute, the time required to complete just one revolution is:
$dt = \frac{60}{S}$ seconds

3. **Calculate the average EMF induced in a single conductor:**
According to Faraday's Law of Electromagnetic Induction, the average induced voltage in one conductor is the rate of change of flux:
$e_{cond} = \frac{d\Phi}{dt} = \frac{P\phi}{60/S} = \frac{P\phi S}{60}$ Volts

4. **Calculate total generated voltage ($E$):**
The total generated EMF of the generator is the voltage across any one of its parallel paths. The total number of conductors $Z$ is divided equally among the $A$ parallel paths. Therefore, the number of conductors connected in series in each path is $\frac{Z}{A}$.
The total induced voltage is the voltage per conductor multiplied by the number of conductors in series:
$E = e_{cond} \times \left(\frac{Z}{A}\right)$
$E = \left(\frac{P\phi S}{60}\right) \times \left(\frac{Z}{A}\right)$
**$E = \frac{P\phi Z S}{60 A}$**

5. **Simplifying to $E = k\phi S$:**
Once a DC machine is built, the number of poles ($P$), the total number of conductors ($Z$), and the number of parallel paths ($A$) are fixed physical constants. We can lump these together into a single "machine constant" denoted by $k$:
$k = \frac{P Z}{60 A}$
Substituting this constant back into the EMF equation gives:
**$E = k\phi S$** (Proved)

**Figures involved:** None.
**References:** 
*   **Mam Slide:** 125, 126
*   **Firoz Note:** 24, 25, 26

***

### Page 12, Q.1(b): Show that the voltage generated by a dc generator is given by E = Kφω, where symbols have their usual meanings.

**Solution:**
This is the exact same fundamental derivation as the previous question, but expressed in terms of **angular velocity ($\omega$)** instead of speed in revolutions per minute ($S$ or $N$).

**Derivation:**
1. Start with the standard DC generator EMF equation derived above (using $N$ for rpm to avoid confusion with seconds):
$E = \frac{P Z \phi N}{60 A}$

2. We need to express the mechanical speed $N$ (rpm) in terms of angular velocity $\omega$ (radians per second).
Since one revolution is $2\pi$ radians, and there are 60 seconds in a minute, the conversion is:
$\omega = \frac{2\pi N}{60}$ rad/s

3. Rearrange this conversion to solve for $N$:
$N = \frac{60 \omega}{2\pi}$

4. Substitute this expression for $N$ back into the original EMF equation:
$E = \frac{P Z \phi}{60 A} \times \left(\frac{60 \omega}{2\pi}\right)$

5. Cancel out the '60' in the numerator and denominator:
$E = \frac{P Z}{2\pi A} \phi \omega$

6. Once again, since the number of poles ($P$), total conductors ($Z$), and parallel paths ($A$) are permanently fixed physical constants of the constructed machine, we can group them into a new machine constant $K$:
$K = \frac{P Z}{2\pi A}$

7. Substituting $K$ into the equation yields the final relationship:
**$E = K\phi \omega$** (Proved)

**Figures involved:** None.
**References:** 
*   **Mam Slide:** 238 (Equation 8-38 uses this exact format)
*   **Firoz Note:** 21, 26

***

### Page 31, Q.7(a): Explain how induction motor can be used as an asynchronous generator?

**Solution:**
*Note: This question relates to AC machine theory.*

An induction motor inherently becomes an induction generator (also known as an asynchronous generator) when its rotor is mechanically driven faster than the synchronous speed of the stator's rotating magnetic field. 

**Explanation of Operation:**
1.  **Initial State:** The stator of the induction machine must be connected to a 3-phase AC power grid. This supply draws magnetizing current to establish the rotating magnetic field, which spins at synchronous speed ($N_s = \frac{120f}{P}$).
2.  **Applying a Prime Mover:** A mechanical prime mover (such as a wind turbine, steam turbine, or hydro rotor) is coupled to the motor's shaft. 
3.  **Negative Slip:** The prime mover accelerates the rotor until its physical speed ($N_r$) is greater than the synchronous speed of the magnetic field ($N_s$). 
    Because Slip $s = \frac{N_s - N_r}{N_s}$, when $N_r > N_s$, the **slip becomes negative**.
4.  **Reversal of Current and Torque:** Because the rotor is now spinning *faster* than the magnetic field, the relative motion between the rotor conductors and the magnetic flux is reversed compared to normal motor operation. According to Faraday's and Lenz's laws, this reverses the direction of the induced rotor EMF and the resulting rotor current.
5.  **Generating Power:** The reversed rotor current creates a reversed electromagnetic torque that pushes *against* the prime mover (mechanical braking). The mechanical energy from the prime mover overcoming this opposing torque is converted into electrical energy. The machine now feeds active electrical power (kW) back into the 3-phase AC grid.

*(Crucial Note: An asynchronous generator cannot generate its own reactive power. It must remain connected to the grid or a capacitor bank to provide the leading reactive power (kVAR) needed to maintain its internal magnetic field).*

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 39, Q.7(b): What is meant by plugging of an induction motor? How does a 3-Φ induction motor operate as a generator?

**Solution:**
*Note: This question relates to AC machine theory.*

**Part 1: What is meant by plugging of an induction motor?**
Plugging (also known as reverse-current braking) is a method used to rapidly stop or rapidly reverse the direction of a running induction motor.
*   **How it is done:** While the motor is running normally, the phase sequence of the 3-phase AC supply connected to the stator is suddenly changed. This is simply done by interchanging any two of the three supply leads (e.g., swapping Phase B with Phase C).
*   **The Effect:** Swapping two phases instantly reverses the direction of the stator's rotating magnetic field. However, due to mechanical inertia, the rotor is still spinning at high speed in the original (now "backward") direction.
*   **The Resulting Braking:** Because the field and rotor are spinning in opposite directions, the relative speed between them becomes immense. The slip ($s$) becomes greater than 1 (specifically, $s \approx 2$). This induces an massive EMF and current in the rotor, producing a very severe braking torque that opposes the rotor's momentum. The motor quickly decelerates to zero. (To prevent it from starting up in the reverse direction, a zero-speed switch must disconnect the power the moment the shaft stops).

**Part 2: How does a 3-Φ induction motor operate as a generator?**
*(This part is identical to the concept explained in the previous question, Page 31, Q.7a).*

To operate as a generator:
1.  The stator must remain connected to the 3-phase AC grid to supply the necessary reactive magnetizing current to create the rotating magnetic field (spinning at $N_s$).
2.  A mechanical source (prime mover) must drive the rotor at a speed ($N_r$) that is *greater* than the synchronous speed ($N_r > N_s$).
3.  This creates a state of **negative slip**. The relative motion between the rotor and the magnetic field reverses, causing the induced rotor current to reverse its direction.
4.  This reversed current pumps active electrical power out of the stator and back into the grid, thus functioning as an asynchronous generator.

**Figures involved:** None.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

Here are the detailed solutions for the next four questions from your syllabus/PYQ list. 

*Note: All four of these questions deal with Alternating Current (AC) machines—specifically rotating magnetic fields and Induction Motors. These topics are not present in the provided "Mam slide" or "Firoz note" documents, which are focused entirely on Direct Current (DC) machines. I have provided the standard electrical engineering derivations and explanations for these AC concepts.*

***

### Page 31, Q.5(c): Show with necessary figures that if a three phase set of currents, each of equal magnitude and differing in phase by 120°, flows in a three phase winding consisting of three separate windings spaced 120 electrical degrees apart around the surface of a machine, then it will produce a rotating magnetic field of constant magnitude. [Figure Involved]

**Solution:**
When balanced three-phase currents are fed into balanced three-phase windings (separated by 120° in space), they produce individual magnetic fluxes. Because the currents are time-displaced by 120° and the coils are space-displaced by 120°, their resultant magnetic field rotates at a constant speed (synchronous speed) and maintains a constant magnitude.

**Step-by-Step Demonstration:**
Let the three phases be Red (R), Yellow (Y), and Blue (B).
1.  **The Currents:** The alternating currents in the three windings are:
    $i_R = I_m \sin(\omega t)$
    $i_Y = I_m \sin(\omega t - 120^\circ)$
    $i_B = I_m \sin(\omega t - 240^\circ)$
2.  **The Individual Fluxes:** These currents produce corresponding alternating fluxes along their respective spatial axes:
    $\phi_R = \phi_m \sin(\omega t)$ (Directed along the reference $0^\circ$ axis)
    $\phi_Y = \phi_m \sin(\omega t - 120^\circ)$ (Directed along the $120^\circ$ axis)
    $\phi_B = \phi_m \sin(\omega t - 240^\circ)$ (Directed along the $240^\circ$ axis)
    *(where $\phi_m$ is the maximum flux produced by any single phase).*

**Analyzing the Resultant Flux ($\Phi_r$) at different instants:**
We find the resultant flux by taking the vector sum of $\phi_R$, $\phi_Y$, and $\phi_B$ at different points in time ($\omega t$).

*   **Case 1: At $\omega t = 0^\circ$**
    $\phi_R = \phi_m \sin(0^\circ) = 0$
    $\phi_Y = \phi_m \sin(-120^\circ) = -0.866 \phi_m$
    $\phi_B = \phi_m \sin(-240^\circ) = +0.866 \phi_m$
    Vector addition of $\phi_Y$ and $\phi_B$ (which are 60° apart due to the negative sign of $\phi_Y$) yields:
    $\Phi_r = 2 \times (0.866 \phi_m) \times \cos(30^\circ) = 2 \times \frac{\sqrt{3}}{2}\phi_m \times \frac{\sqrt{3}}{2} = 1.5 \phi_m$.
    *Direction: Perpendicular to the R-axis.*

*   **Case 2: At $\omega t = 60^\circ$**
    $\phi_R = \phi_m \sin(60^\circ) = +0.866 \phi_m$
    $\phi_Y = \phi_m \sin(-60^\circ) = -0.866 \phi_m$
    $\phi_B = \phi_m \sin(-180^\circ) = 0$
    Vector addition of $\phi_R$ and $\phi_Y$ yields:
    $\Phi_r = 2 \times (0.866 \phi_m) \times \cos(30^\circ) = 1.5 \phi_m$.
    *Direction: Rotated exactly 60° clockwise from Case 1.*

*   **Case 3: At $\omega t = 120^\circ$**
    $\phi_R = \phi_m \sin(120^\circ) = +0.866 \phi_m$
    $\phi_Y = \phi_m \sin(0^\circ) = 0$
    $\phi_B = \phi_m \sin(-120^\circ) = -0.866 \phi_m$
    Vector addition yields:
    $\Phi_r = 1.5 \phi_m$.
    *Direction: Rotated exactly 120° clockwise from Case 1.*

**Conclusion:**
As time $\omega t$ progresses, the magnitude of the resultant flux strictly remains $1.5 \phi_m$, but its spatial direction rotates uniformly around the machine.

**Figures involved:** 
1. A cross-section of a stator showing 3 coils ($R, Y, B$) displaced by 120 degrees in space.
2. Three separate phasor addition diagrams representing Case 1 ($\omega t = 0^\circ$), Case 2 ($\omega t = 60^\circ$), and Case 3 ($\omega t = 120^\circ$), visually proving the vector sum always equals $1.5\phi_m$ and rotates.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 31, Q.6(a): Prove that for 3-Φ induction motor the resultant flux is 1.5 times of the maximum value of the induced flux in any phase.

**Solution:**
This is the formal mathematical proof of the phenomenon demonstrated graphically in the previous question.

**Proof:**
Let the three individual phase fluxes be directed along three spatial axes separated by 120°. We can resolve these three flux vectors into horizontal ($X$) and vertical ($Y$) components. Let the R-phase flux lie along the X-axis.

1.  **Define the Flux Equations:**
    $\phi_R = \phi_m \sin(\omega t)$ at angle $0^\circ$
    $\phi_Y = \phi_m \sin(\omega t - 120^\circ)$ at angle $120^\circ$
    $\phi_B = \phi_m \sin(\omega t - 240^\circ)$ at angle $240^\circ$

2.  **Resolve components along the X-axis:**
    $\Phi_x = \phi_R + \phi_Y \cos(120^\circ) + \phi_B \cos(240^\circ)$
    $\Phi_x = \phi_m \sin(\omega t) - 0.5 \phi_m \sin(\omega t - 120^\circ) - 0.5 \phi_m \sin(\omega t - 240^\circ)$
    Using the trigonometric identity $\sin(A-B) = \sin A\cos B - \cos A\sin B$:
    $\Phi_x = \phi_m [ \sin\omega t - 0.5(-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t) - 0.5(-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t) ]$
    $\Phi_x = \phi_m [ \sin\omega t + \frac{1}{4}\sin\omega t + \frac{\sqrt{3}}{4}\cos\omega t + \frac{1}{4}\sin\omega t - \frac{\sqrt{3}}{4}\cos\omega t ]$
    $\Phi_x = \phi_m [ \sin\omega t + \frac{1}{2}\sin\omega t ]$
    **$\Phi_x = 1.5 \phi_m \sin(\omega t)$**

3.  **Resolve components along the Y-axis:**
    $\Phi_y = 0 + \phi_Y \sin(120^\circ) + \phi_B \sin(240^\circ)$
    $\Phi_y = \phi_m \frac{\sqrt{3}}{2} \sin(\omega t - 120^\circ) - \phi_m \frac{\sqrt{3}}{2} \sin(\omega t - 240^\circ)$
    $\Phi_y = \phi_m \frac{\sqrt{3}}{2} [ (-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t) - (-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t) ]$
    $\Phi_y = \phi_m \frac{\sqrt{3}}{2} [ -\sqrt{3} \cos\omega t ]$
    **$\Phi_y = -1.5 \phi_m \cos(\omega t)$**

4.  **Calculate the Resultant Flux ($\Phi_r$):**
    The magnitude of the total resultant flux is the vector sum of the X and Y components:
    $\Phi_r = \sqrt{\Phi_x^2 + \Phi_y^2}$
    $\Phi_r = \sqrt{(1.5 \phi_m \sin\omega t)^2 + (-1.5 \phi_m \cos\omega t)^2}$
    $\Phi_r = 1.5 \phi_m \sqrt{\sin^2\omega t + \cos^2\omega t}$
    Since $\sin^2\theta + \cos^2\theta = 1$, the equation simplifies to:
    **$\Phi_r = 1.5 \phi_m$** (Proved).

The resultant flux magnitude is strictly constant and is exactly 1.5 times the maximum flux produced by any single phase.

**Figures involved:** None required for the pure mathematical proof.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 32, Q.8(b): By using double-revolving field theory explain how a single phase induction motor develops its torque after starting. Explain why the forward field becomes higher than the backward field at 0<S<1.

**Solution:**
**1. Double-Revolving Field Theory (DRFT) & Torque Development:**
A single-phase AC current passing through a single stator winding produces a *pulsating* magnetic field, not a rotating one. DRFT states that any alternating, pulsating magnetic field of maximum magnitude $\Phi_m$ can be mathematically and physically resolved into two distinct magnetic fields, each of half the magnitude ($\frac{\Phi_m}{2}$), rotating in opposite directions at the same synchronous speed ($N_s$).
*   Let's call the field rotating in the direction of the rotor the **Forward Field**.
*   Let's call the field rotating opposite to the rotor the **Backward Field**.

*At standstill ($s=1$)*: The forward and backward fields produce equal but opposite torques. Net torque = 0, which is why a single-phase induction motor is not inherently self-starting.
*After starting*: If the motor is given an initial push (e.g., via a starting capacitor/auxiliary winding), the rotor starts spinning in the forward direction. Once moving, the torque produced by the forward field becomes much greater than the torque produced by the backward field, resulting in a net positive torque that keeps the motor running.

**2. Why the Forward Field becomes higher than the Backward Field ($0 < s < 1$):**
This is due to how the rotor circuits react to the differing slip speeds of the two fields once the motor is spinning.
*   Let the motor spin at speed $N$ in the forward direction.
*   **Forward Slip ($s_f$):** The slip relative to the forward field is $s_f = \frac{N_s - N}{N_s} = s$. During normal operation ($0 < s < 1$), this slip is very small (e.g., 0.05).
*   **Backward Slip ($s_b$):** The slip relative to the backward field (which is spinning at $-N_s$) is $s_b = \frac{N_s - (-N)}{N_s} = \frac{N_s + N}{N_s} = 2 - s$. This slip is very large (e.g., 1.95).

**The Effect on the Fields:**
*   Because the backward slip ($2-s$) is nearly 2, the frequency of the voltage induced by the backward field into the rotor is very high (almost $2 \times$ line frequency). 
*   Because rotor reactance $X_r = 2\pi f_r L_r$, this high frequency creates a massive inductive reactance in the rotor circuit for the backward field. 
*   This highly inductive rotor current severely *demagnetizes* the backward rotating field. 
*   Conversely, the forward slip ($s$) is small, so the forward rotor current is largely resistive and moderate, leaving the forward rotating field largely intact.
*   **Conclusion:** The demagnetizing effect of the high-frequency backward rotor currents heavily suppresses the backward magnetic field. Therefore, under running conditions, the Forward Field is significantly stronger than the Backward Field, allowing the motor to sustain rotation and drive a load.

**Figures involved:** 
*   A torque-speed curve showing the forward torque curve, the backward torque curve, and the resultant net torque curve which passes through zero at $N=0$.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 35, Q.8(a): Explain double field revolving theory. Also explain, why a single-phase transformer is not self starting.

**Solution:**
*(Note: The second part of this question is a classic electrical engineering "trick" question. A transformer is a static device without a rotor, so asking why it doesn't "start" is addressing a misconception. I will explain it in the context of why a single-phase induction motor at standstill behaves identically to a transformer.)*

**1. Explanation of Double Field Revolving Theory (DRFT):**
As outlined in the previous answer, when a single-phase alternating current flows through a single stator winding, it creates a pulsating magnetic field. The flux alternates purely along one physical axis, growing to a maximum, shrinking to zero, and growing in the opposite direction. 
*   **DRFT** postulates that this pulsating stationary field of amplitude $\Phi_{max}$ can be represented by two separate magnetic fields, each of amplitude $\frac{\Phi_{max}}{2}$, rotating in opposite directions (one clockwise, one counter-clockwise) at the exact same synchronous speed ($N_s$).
*   Because they rotate at the same speed in opposite directions, their components perpendicular to the coil axis cancel each other out at every instant, while their components along the coil axis add together, perfectly recreating the original stationary pulsating field. 

**2. Why a "Single-Phase Transformer" (or Single-Phase Motor at standstill) is not self-starting:**
*   A **Transformer** is a completely static device. It operates purely on the principle of mutual induction between two stationary coils. It has no air gap, no rotor, and no mechanical moving parts. It cannot "start" because it is not designed to produce mechanical motion.
*   **The connection to Motors (The probable intent of the question):** If we look at a single-phase induction motor at standstill (speed $N = 0$), it behaves exactly like a single-phase transformer with a short-circuited secondary. 
    *   The single-phase AC creates a pulsating magnetic field (just like the primary of a transformer).
    *   This pulsating field induces a voltage and current in the stationary rotor bars (just like the secondary of a transformer).
    *   According to Lenz's law, the rotor current creates a magnetic field that simply opposes the stator field along the exact same physical axis. 
    *   Because the force is pushing perfectly straight across the diameter of the rotor, no rotational twisting force (Torque) is created. 
    *   Using DRFT, at standstill ($s=1$), the forward rotating field produces a torque $+T$, and the backward rotating field produces a torque $-T$. The net torque is perfectly $0$.
    *   Therefore, without an auxiliary starting winding to create an initial phase shift (a simulated second phase), the rotor will just hum and heat up, unable to rotate.

**Figures involved:** A vector diagram showing two vectors of magnitude $\Phi_m/2$ rotating in opposite directions, and their vector sum always oscillating along the vertical Y-axis.
**References:** Not explicitly covered in the provided DC Machine slides or notes.
Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

*Note: All four of these questions deal with Alternating Current (AC) machines—specifically rotating magnetic fields and Induction Motors. These topics are not present in the provided "Mam slide" or "Firoz note" documents, which are focused entirely on Direct Current (DC) machines. I have provided the standard electrical engineering derivations and explanations for these AC concepts.*

***

### Page 39, Q.8(b): State the concept of double field revolving theory for a 1-Φ induction motor and derive the equations of forward and backward torques.

**Solution:**
**1. Concept of Double Field Revolving Theory (DRFT):**
The Double Field Revolving Theory states that any alternating (pulsating) magnetic field produced by a single-phase stationary winding can be resolved into two separate rotating magnetic fields of equal magnitude but rotating in opposite directions at synchronous speed.
*   If the alternating magnetic flux has a maximum amplitude of $\Phi_m$, it is split into a **Forward rotating field** ($\Phi_f = \Phi_m / 2$) and a **Backward rotating field** ($\Phi_b = \Phi_m / 2$).
*   These two fields induce their own respective currents in the rotor, generating two opposing torques: a forward torque ($T_f$) and a backward torque ($T_b$).

**2. Derivation of Forward and Backward Torques:**
Let the motor be running at a speed $N$ in the forward direction. The synchronous speed of the magnetic fields is $N_s$.

*   **Slip for the Forward Field ($s_f$):**
    The forward field is rotating in the same direction as the rotor. Therefore, the slip relative to the forward field is the standard slip $s$:
    $s_f = \frac{N_s - N}{N_s} = s$

*   **Slip for the Backward Field ($s_b$):**
    The backward field is rotating in the exact opposite direction to the rotor (speed is $-N_s$). The slip relative to this backward field is:
    $s_b = \frac{N_s - (-N)}{N_s} = \frac{N_s + N}{N_s}$
    Since $N = N_s(1 - s)$, we can substitute this in:
    $s_b = \frac{N_s + N_s(1 - s)}{N_s} = 1 + (1 - s) = 2 - s$

*   **Forward Torque ($T_f$):**
    The power transferred across the air gap by the forward field ($P_{gf}$) is dissipated in the forward rotor resistance. The effective rotor resistance for the forward field is $\frac{R_2}{2s}$.
    $P_{gf} = I_2^2 \left( \frac{R_2}{2s} \right)$
    Torque is air-gap power divided by synchronous angular velocity ($\omega_s$):
    **$T_f = \frac{1}{\omega_s} I_2^2 \left( \frac{R_2}{2s} \right)$**

*   **Backward Torque ($T_b$):**
    Similarly, the power transferred across the air gap by the backward field ($P_{gb}$) acts on the backward rotor resistance, which is $\frac{R_2}{2(2-s)}$.
    $P_{gb} = I_2^2 \left( \frac{R_2}{2(2-s)} \right)$
    **$T_b = \frac{1}{\omega_s} I_2^2 \left( \frac{R_2}{2(2-s)} \right)$**

*   **Net Torque ($T_{net}$):**
    The net torque developed by the single-phase motor is the difference between the forward and backward torques:
    $T_{net} = T_f - T_b = \frac{I_2^2 R_2}{2\omega_s} \left[ \frac{1}{s} - \frac{1}{2-s} \right]$

**Figures involved:** None specifically requested, but a torque-speed graph showing forward, backward, and resultant torque curves is standard.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 41, Q.4(b): Explain the double field revolving theory for operation of single phase induction motor.

**Solution:**
*(Note: This is a conceptual application of the theory derived in the previous question, focusing on the motor's operational states).*

The operation of a single-phase induction motor is thoroughly explained by analyzing it through the lens of the Double Field Revolving Theory (DRFT).

**1. Operation at Standstill (Starting):**
*   When a single-phase supply is applied to the stator, it produces a pulsating magnetic field. DRFT splits this into a forward-rotating field and a backward-rotating field.
*   At standstill, the rotor speed $N = 0$. 
*   Therefore, the forward slip $s_f = \frac{N_s - 0}{N_s} = 1$.
*   The backward slip $s_b = \frac{N_s - (-0)}{N_s} = 1$.
*   Since the slips are equal ($s_f = s_b = 1$), the effective rotor resistances are equal. Thus, the forward torque $T_f$ and backward torque $T_b$ are exactly equal in magnitude but opposite in direction. 
*   **Net Torque = 0.** This explains why a pure single-phase induction motor is **not self-starting**. It simply hums and vibrates without turning.

**2. Operation under Running Conditions:**
*   Suppose the rotor is given an initial mechanical spin (or an auxiliary starter winding is used momentarily) in the forward direction. The rotor is now spinning at a speed $N$ close to $N_s$.
*   The forward slip $s$ becomes very small (e.g., $s = 0.05$).
*   The backward slip becomes very large ($2 - s = 1.95$).
*   Looking at the torque formulas from the previous question, torque is inversely proportional to slip. Because $s$ is very small, $\frac{1}{s}$ becomes a very large number, generating a huge **Forward Torque ($T_f$)**.
*   Because $(2-s)$ is very large (nearly 2), $\frac{1}{2-s}$ becomes a very small number, generating only a tiny **Backward Torque ($T_b$)**.
*   Therefore, $T_f \gg T_b$. The motor develops a strong net positive torque in the forward direction, which overcomes mechanical load and friction, allowing the motor to run continuously on just a single phase.

**Figures involved:** A torque-speed characteristic curve for a single-phase induction motor, illustrating the $T_f$ curve in the positive quadrant, the $T_b$ curve in the negative quadrant, and the Resultant Torque curve passing perfectly through the origin ($0$ torque at $0$ speed).
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 41, Q.5(b): Discuss graphically how a rotating field is produced in the air gap of three phase induction motor. [Figure Involved]

**Solution:**
A rotating magnetic field of constant magnitude is naturally produced when a balanced 3-phase supply is connected to a balanced 3-phase stator winding spaced 120° apart. 

**Graphical Discussion:**
Imagine a stator with three coils: Red (R), Yellow (Y), and Blue (B), positioned spatially at 0°, 120°, and 240° around the air gap. The currents flowing through them are sine waves, time-displaced by 120°.

1.  **Instant 1 ($\omega t = 0^\circ$):** 
    *   Looking at the current sine waves, the current in phase R is 0. 
    *   The current in phase Y is negative (flowing inwards). 
    *   The current in phase B is positive (flowing outwards).
    *   Graphically drawing the resulting magnetic flux vectors: Phase Y produces a flux vector pointing down-left, and Phase B produces a flux vector pointing up-left. When we add these two vectors graphically using the parallelogram law, the resultant flux ($\Phi_R$) points perfectly horizontally to the left.

2.  **Instant 2 ($\omega t = 60^\circ$):**
    *   The current in phase R is positive.
    *   The current in phase Y is negative.
    *   The current in phase B has dropped to 0.
    *   Graphically drawing the vectors: Phase R flux points straight up. Phase Y flux points down-left. Adding these vectors graphically yields a resultant flux ($\Phi_R$) that is exactly the same length as in Instant 1, but it has rotated **60° clockwise**.

3.  **Instant 3 ($\omega t = 120^\circ$):**
    *   The current in phase R is positive.
    *   The current in phase Y is 0.
    *   The current in phase B is negative.
    *   Graphically drawing the vectors: Phase R points straight up. Phase B points down-right. The graphical vector addition yields a resultant flux ($\Phi_R$) of the same length, rotated another **60° clockwise** (total 120° from the start).

**Conclusion:** By plotting the flux vectors at sequential time intervals, the graphical method clearly shows that the resultant magnetic field vector never shrinks or grows (it maintains a constant magnitude of $1.5\Phi_{max}$), but its tip traces a perfect circle in the air gap, proving it is a purely rotating magnetic field.

**Figures involved:** 
*   A graph showing three 120° displaced sine waves (representing currents $i_R, i_Y, i_B$).
*   Three separate spatial vector diagrams corresponding to the specific time instants ($0^\circ, 60^\circ, 120^\circ$), showing the addition of the phase fluxes to create a rotating resultant flux vector.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 45, Q.5(b): Prove that, for a poly phase induction motor, the resultant revolving flux is 1.5 times the maximum value of the flux due to any phase.

**Solution:**
*(Note: This is the mathematical proof of the graphical phenomenon discussed in the previous question).*

Let the three individual phase fluxes ($\phi_1, \phi_2, \phi_3$) have a maximum amplitude of $\Phi_m$. Because they are fed by a 3-phase supply, they are displaced in time by 120°. Because the coils are distributed around the stator, they are displaced in space by 120°. 

The flux equations are:
$\phi_1 = \Phi_m \sin(\omega t)$  (Assume this acts along the reference X-axis: 0°)
$\phi_2 = \Phi_m \sin(\omega t - 120^\circ)$ (Acts along the 120° axis)
$\phi_3 = \Phi_m \sin(\omega t - 240^\circ)$ (Acts along the 240° axis)

To find the resultant, we resolve these three vectors into horizontal (X) and vertical (Y) components.

**1. Summing the X-components:**
$\Phi_x = \phi_1 \cos(0^\circ) + \phi_2 \cos(120^\circ) + \phi_3 \cos(240^\circ)$
$\Phi_x = \Phi_m \sin(\omega t)(1) + \Phi_m \sin(\omega t - 120^\circ)(-\frac{1}{2}) + \Phi_m \sin(\omega t - 240^\circ)(-\frac{1}{2})$
$\Phi_x = \Phi_m \left[ \sin\omega t - \frac{1}{2}(\sin\omega t \cos 120^\circ - \cos\omega t \sin 120^\circ) - \frac{1}{2}(\sin\omega t \cos 240^\circ - \cos\omega t \sin 240^\circ) \right]$
$\Phi_x = \Phi_m \left[ \sin\omega t - \frac{1}{2}(-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t) - \frac{1}{2}(-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t) \right]$
$\Phi_x = \Phi_m \left[ \sin\omega t + \frac{1}{4}\sin\omega t + \frac{\sqrt{3}}{4}\cos\omega t + \frac{1}{4}\sin\omega t - \frac{\sqrt{3}}{4}\cos\omega t \right]$
$\Phi_x = \Phi_m \left[ \sin\omega t + \frac{1}{2}\sin\omega t \right] = \mathbf{1.5 \Phi_m \sin(\omega t)}$

**2. Summing the Y-components:**
$\Phi_y = \phi_1 \sin(0^\circ) + \phi_2 \sin(120^\circ) + \phi_3 \sin(240^\circ)$
$\Phi_y = 0 + \Phi_m \sin(\omega t - 120^\circ)(\frac{\sqrt{3}}{2}) + \Phi_m \sin(\omega t - 240^\circ)(-\frac{\sqrt{3}}{2})$
$\Phi_y = \frac{\sqrt{3}}{2} \Phi_m \left[ (-\frac{1}{2}\sin\omega t - \frac{\sqrt{3}}{2}\cos\omega t) - (-\frac{1}{2}\sin\omega t + \frac{\sqrt{3}}{2}\cos\omega t) \right]$
$\Phi_y = \frac{\sqrt{3}}{2} \Phi_m \left[ -\sqrt{3} \cos\omega t \right] = \mathbf{-1.5 \Phi_m \cos(\omega t)}$

**3. Calculating the Resultant Magnitude ($\Phi_R$):**
The total resultant flux is the vector sum of the orthogonal X and Y components:
$\Phi_R = \sqrt{\Phi_x^2 + \Phi_y^2}$
$\Phi_R = \sqrt{(1.5 \Phi_m \sin\omega t)^2 + (-1.5 \Phi_m \cos\omega t)^2}$
$\Phi_R = 1.5 \Phi_m \sqrt{\sin^2(\omega t) + \cos^2(\omega t)}$
Since $\sin^2\theta + \cos^2\theta = 1$, the equation simplifies completely to:
**$\Phi_R = 1.5 \Phi_m$**

Thus, it is proven that the magnitude of the resultant revolving flux is constant and exactly 1.5 times the maximum value of the flux produced by any single phase.

**Figures involved:** None strictly required for the mathematical proof, though a 3-axis vector layout helps define the initial angles.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

Here are the detailed solutions for the next four questions from your syllabus/PYQ list. 

*Note: The first two questions relate to Alternating Current (AC) machines (Single-Phase Induction Motors). These topics are not present in the provided "Mam slide" or "Firoz note" documents, so I have provided the standard electrical engineering derivations for them. The last two questions return to the core principles of DC machines, and their answers are sourced directly from your provided materials.*

***

### Page 46, Q.8(b): With the help of double field revolving theory, prove that for the case of 1-Φ induction motor, under running condition V >> Vb, where the symbols have their usual meanings.

**Solution:**
*Note: In the context of the Double Revolving Field Theory (DRFT) equivalent circuit for a single-phase induction motor, the symbol $V$ (or $V_f$) typically denotes the voltage drop across the forward-rotating rotor impedance, and $V_b$ denotes the voltage drop across the backward-rotating rotor impedance.*

**Proof:**
According to DRFT, the pulsating magnetic field of a single-phase induction motor is split into a forward-rotating field and a backward-rotating field. These fields induce currents in the rotor, which can be represented by two series-connected rotor impedances in the motor's equivalent circuit.

1.  **Define the Slips:**
    Let the motor run at a speed $N$ in the forward direction. 
    *   Slip with respect to the forward field: $s_f = s$
    *   Slip with respect to the backward field: $s_b = 2 - s$

2.  **Define the Rotor Impedances:**
    In the equivalent circuit, the rotor resistance is divided by the respective slip for each field.
    *   Forward rotor impedance: $Z_f = \frac{R_2}{2s} + j\frac{X_2}{2}$
    *   Backward rotor impedance: $Z_b = \frac{R_2}{2(2-s)} + j\frac{X_2}{2}$

3.  **Analyze Under Normal Running Conditions:**
    During normal running conditions, the motor spins at a speed close to synchronous speed, meaning the forward slip $s$ is very small (e.g., $s = 0.05$).
    *   Because $s$ is very small, the denominator in the real part of $Z_f$ is very small, making the forward impedance **$Z_f$ very large**.
    *   Conversely, $(2 - s)$ is approximately $1.95$ (nearly 2). This relatively large denominator makes the real part of the backward impedance **$Z_b$ very small**.
    *   Therefore, $Z_f \gg Z_b$.

4.  **Voltage Drops:**
    In the equivalent circuit, the stator current $I_1$ flows through both the forward and backward parallel branches (combining the magnetizing reactance $X_m$ and rotor impedances).
    *   The voltage drop across the forward field network is $V_f$ (often just denoted as $V$ in some texts representing the dominant forward voltage).
    *   The voltage drop across the backward field network is $V_b$.
    *   Since voltage drop is proportional to impedance ($V = IZ$), and the forward equivalent impedance is massively larger than the backward equivalent impedance ($Z_{eq\_f} \gg Z_{eq\_b}$), it mathematically follows that the voltage across the forward branch is much greater than the voltage across the backward branch.

**Conclusion:**
Under normal running conditions, because $s$ is small and $(2-s)$ is near 2, $Z_f \gg Z_b$, which strictly proves that **$V_f \gg V_b$** (or $V \gg V_b$).

**Figures involved:** None strictly required, though drawing the DRFT series equivalent circuit showing $V_f$ and $V_b$ clarifies the proof.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 46, Q.8(c): State and explain double field revolving theory as applied to 1-Φ induction motor.

**Solution:**
*(Note: This explores the core concept used in the mathematical derivations above).*

**Statement of the Theory:**
The Double Field Revolving Theory (DRFT) states that any stationary, pulsating (alternating) magnetic field can be resolved into two separate magnetic fields of equal magnitude, rotating in opposite directions at the same synchronous speed.

**Explanation applied to a 1-$\Phi$ Induction Motor:**
1.  **The Stator Field:** When a single-phase AC supply is connected to the single main winding of the motor, it creates a magnetic field that pulsates along a single spatial axis. It grows to a North pole, shrinks to zero, and grows into a South pole. It does *not* rotate.
2.  **Applying DRFT:** According to the theory, we can represent this pulsating flux ($\Phi_{max}$) as two distinct rotating fluxes:
    *   A **Forward Flux ($\Phi_f$)** of magnitude $\frac{\Phi_{max}}{2}$ rotating at synchronous speed $+N_s$.
    *   A **Backward Flux ($\Phi_b$)** of magnitude $\frac{\Phi_{max}}{2}$ rotating at synchronous speed $-N_s$.
3.  **Operation at Standstill:** When power is first applied, the rotor is stationary ($N = 0$). The relative speed (and thus the slip) between the rotor and both the forward and backward fields is exactly the same ($s=1$). Therefore, the forward field induces a forward torque ($+T$), and the backward field induces an identical backward torque ($-T$). The net torque is zero, which is why the motor cannot start itself.
4.  **Operation while Running:** If the rotor is mechanically spun in the forward direction, the dynamic changes. The slip relative to the forward field ($s$) becomes very small, generating a massive forward torque. Simultaneously, the slip relative to the backward field ($2-s$) becomes very large. This high relative speed induces high-frequency currents in the rotor that demagnetize and suppress the backward field, reducing its torque to almost nothing.
5.  **Result:** The forward torque overwhelmingly dominates the backward torque, resulting in a net positive torque that keeps the single-phase motor running.

**Figures involved:** A vector diagram showing a vertical pulsating vector resolved into two oppositely rotating vectors of half the length.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 4, Q.53: Derive the expression of induced torque for a real motor.

**Solution:**
The expression for the induced torque ($\tau_{ind}$) of a real DC motor can be derived using the fundamental principle of electrical-to-mechanical power conversion.

**Derivation:**
1.  **Define Power Conversion:** In any DC motor, the total electrical power supplied to the armature that is successfully converted into gross mechanical power is given by the product of the internal Counter-EMF ($E_A$) and the total armature current ($I_A$).
    $P_{conv} = E_A I_A$

2.  **Define Mechanical Power:** From classical mechanics, rotational mechanical power is equal to the product of the induced torque ($\tau_{ind}$) and the mechanical angular velocity of the rotor ($\omega_m$, measured in radians per second).
    $P_{conv} = \tau_{ind} \omega_m$

3.  **Equate the two Power Expressions:** Because the electrical power converted must perfectly equal the gross mechanical power developed:
    $\tau_{ind} \omega_m = E_A I_A$

4.  **Substitute the EMF Equation:** We know the fundamental equation for the generated voltage (Back EMF) in a real DC machine is:
    $E_A = \frac{Z P \Phi \omega_m}{2 \pi A}$
    Where:
    *   $Z$ = Total number of armature conductors
    *   $P$ = Number of magnetic poles
    *   $\Phi$ = Flux per pole
    *   $A$ = Number of parallel paths in the winding

5.  **Solve for Torque:** Substitute the $E_A$ equation back into the power equivalence equation:
    $\tau_{ind} \omega_m = \left( \frac{Z P \Phi \omega_m}{2 \pi A} \right) I_A$

6.  **Simplify:** The angular velocity ($\omega_m$) appears on both sides of the equation and can be canceled out:
    $\tau_{ind} = \frac{Z P \Phi I_A}{2 \pi A}$

7.  **Final Expression:** Since the number of poles ($P$), total conductors ($Z$), and parallel paths ($A$) are fixed physical constants for a manufactured machine, they can be grouped into a single machine constant, $K = \frac{Z P}{2 \pi A}$.
    Substituting $K$ into the equation yields the final, simplified expression for induced torque:
    **$\tau_{ind} = K \Phi I_A$**

**Figures involved:** None strictly required for the mathematical derivation.
**References:** 
*   **Mam Slide:** 238, 240
*   **Firoz Note:** 76, 78, 82

***

### Page 5, Q.64: Explain briefly speed versus armature current and torque versus armature current characteristics of all dc motors.

**Solution:**
The operating behavior of a DC motor is defined by how its torque ($\tau_{ind} = K\Phi I_A$) and speed ($N \propto \frac{V - I_A R_A}{\Phi}$) change as the mechanical load—and therefore the armature current ($I_A$)—changes.

**1. Torque versus Armature Current ($T$ vs $I_A$) Characteristics:**
This shows the mechanical pulling power of the motor as it draws more current.
*   **Shunt Motor:** The field winding is in parallel with the supply, so the flux ($\Phi$) is practically constant. Because $T \propto \Phi I_A$, and $\Phi$ is constant, the torque increases directly and linearly with the armature current. *Graph: A straight line starting from the origin.*
*   **Series Motor:** The field winding is in series with the armature, so the flux is directly proportional to the armature current ($\Phi \propto I_A$) until the iron core saturates. Therefore, $T \propto I_A \times I_A \Rightarrow T \propto I_A^2$. The torque rises exponentially at first. After magnetic saturation, $\Phi$ becomes constant, and the curve becomes a straight line. *Graph: A rising parabola that straightens out at high currents.*
*   **Cumulative Compound Motor:** The series field flux adds to the constant shunt field flux ($\Phi_{total} = \Phi_{sh} + \Phi_{se}$). As current increases, total flux increases. Its torque rises faster than a pure shunt motor but slower than a pure series motor. *Graph: A curve rising between the shunt and series characteristics.*
*   **Differential Compound Motor:** The series field flux opposes the shunt field flux. As current increases, total flux decreases. Therefore, torque barely increases and eventually drops off. *Graph: A curve falling significantly below the linear shunt line.*

**2. Speed versus Armature Current ($N$ vs $I_A$) Characteristics:**
This shows how well the motor maintains its rotational speed under load.
*   **Shunt Motor:** As load ($I_A$) increases, the voltage drop across the armature resistance ($I_A R_A$) increases. Since $N \propto V - I_A R_A$, the speed drops slightly. However, this drop is very small, so the shunt motor is considered a "constant speed" motor. *Graph: A relatively flat, slightly drooping straight line.*
*   **Series Motor:** Speed is inversely proportional to flux ($N \propto 1/\Phi$). Because $\Phi \propto I_A$, then $N \propto 1/I_A$. At very low currents (no load), the flux is tiny, causing the speed to shoot up to dangerously infinite levels. As load increases, flux increases, and the speed drops sharply. *Graph: A steep hyperbola.* (This is why series motors must never be started without a load).
*   **Cumulative Compound Motor:** As current increases, the added series flux increases total flux ($\Phi$), causing the speed to drop more noticeably than a shunt motor, but without the danger of "running away" at no-load like a series motor. *Graph: A curve drooping steeper than the shunt line.*
*   **Differential Compound Motor:** As load increases, the opposing series field *decreases* the total flux. A decrease in flux causes the speed to *increase*. This creates a dangerous positive feedback loop where increased load causes increased speed, making the motor highly unstable. *Graph: A curve rising upward with load.*

**Figures involved:** 
1. **$T$ vs $I_A$ Graph:** A single plot showing the straight line (Shunt), parabola (Series), and intermediate curves (Compound).
2. **$N$ vs $I_A$ Graph:** A single plot showing the flat droop (Shunt), steep hyperbola (Series), steep droop (Cumulative), and rising curve (Differential).
**References:** 
*   **Mam Slide:** 242, 248-251 (Shunt), 255 (Compound), 260, 262 (Series)
*   **Firoz Note:** 103 (Speed vs Ia), 109 (Torque vs Ia), 111 (Speed vs Torque combined)

Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

***

### Page 5, Q.65: Draw and explain the mechanical characteristics of DC series and shunt motor. [Figure Involved]

**Solution:**
In DC motor terminology, the "Mechanical Characteristic" specifically refers to the **Speed versus Torque ($N$ vs. $\tau$) curve**. It illustrates how the mechanical speed of the motor adjusts as the mechanical load (and thus the required torque) changes.

**1. Mechanical Characteristic of a DC Shunt Motor:**
*   **Explanation:** In a shunt motor, the field winding is connected in parallel with the supply voltage, so the magnetic flux ($\Phi$) is considered practically constant. 
*   We know that torque $\tau \propto \Phi I_a$ (so $I_a \propto \tau$) and speed $N \propto \frac{V - I_a R_a}{\Phi}$. 
*   Because $\Phi$ is constant, speed is purely dependent on the armature voltage drop ($I_a R_a$). As the load torque increases, the motor draws more armature current ($I_a$). This increases the $I_a R_a$ drop, causing a slight, linear decrease in speed. 
*   However, because the armature resistance $R_a$ is very small, this drop in speed is minimal. Therefore, a shunt motor is considered a "constant-speed" motor.
*   **Figure involved:** A graph with Torque ($\tau$) on the X-axis and Speed ($N$ or $\omega$) on the Y-axis. The curve is a straight line starting from the no-load speed on the Y-axis and drooping slightly downward as it moves to the right.

**2. Mechanical Characteristic of a DC Series Motor:**
*   **Explanation:** In a series motor, the field winding is in series with the armature, meaning the field current equals the armature current ($I_f = I_a$). Therefore, before magnetic saturation, the flux is directly proportional to the torque-producing current ($\Phi \propto I_a$).
*   Because $\tau \propto \Phi I_a$ and $\Phi \propto I_a$, we get $\tau \propto I_a^2$, which means $I_a \propto \sqrt{\tau}$.
*   The speed equation is $N \propto \frac{V - I_a(R_a + R_s)}{\Phi}$. Since $\Phi \propto I_a$, we can substitute $I_a$ with $\sqrt{\tau}$ to see that $N \propto \frac{1}{\sqrt{\tau}}$.
*   This creates an inverse relationship: at light loads (low torque), the speed is dangerously high. As torque increases, the speed drops drastically. 
*   **Figure involved:** A graph with Torque ($\tau$) on the X-axis and Speed ($N$) on the Y-axis. The curve is a steep hyperbola that starts extremely high on the Y-axis (approaching infinity at zero torque) and curves sharply downward, flattening out as torque becomes very high.

**References:** 
*   **Mam Slide:** 242 (Defines mechanical characteristic), 250 (Shunt $N$ vs $\tau$), 262 (Series $N$ vs $\tau$)
*   **Firoz Note:** 111 (Combined Speed vs Torque graph)

***

### Page 5, Q.66: Explain the effects on speed, counter emf, armature current and torque of a dc shunt motor when load applied to that motor.

**Solution:**
When a mechanical load is suddenly applied to the shaft of a running DC shunt motor, a specific sequence of self-regulating electrical and mechanical events occurs to accommodate the new load.

Here is the step-by-step explanation of the effects:
1.  **Effect on Speed ($N$):** Initially, the motor is spinning at a steady speed. When a load is applied, the new mechanical load torque ($\tau_{load}$) instantly exceeds the motor's currently developed electromagnetic torque ($\tau_{ind}$). Because the opposing force is greater than the driving force, the motor **starts to slow down** (speed $N$ decreases).
2.  **Effect on Counter EMF ($E_b$):** The counter EMF (Back EMF) generated within the armature is directly proportional to the motor's speed and magnetic flux ($E_b = K\Phi N$). Because the flux ($\Phi$) in a shunt motor is constant, the decrease in speed directly causes the internal **Counter EMF ($E_b$) to drop**.
3.  **Effect on Armature Current ($I_a$):** The armature current is determined by the difference between the supply voltage ($V$) and the Counter EMF, divided by the armature resistance: $I_a = \frac{V - E_b}{R_a}$. Since the supply voltage $V$ is constant and $E_b$ has just decreased, the numerator ($V - E_b$) becomes larger. This causes the **armature current ($I_a$) to rapidly increase**.
4.  **Effect on Induced Torque ($\tau_{ind}$):** The electromagnetic torque developed by the motor is directly proportional to the armature current ($\tau_{ind} = K\Phi I_a$). Because the armature current has just surged upward, the **induced torque increases** correspondingly.
5.  **Equilibrium Reached:** The induced torque will continue to rise until it perfectly matches the new, heavier mechanical load torque ($\tau_{ind} = \tau_{load}$). At this point, the motor stops decelerating and settles at a new steady state, running continuously at a slightly lower speed, drawing a higher continuous armature current, and developing a higher torque.

**Figures involved:** None required for this theoretical sequence.
**References:** 
*   **Mam Slide:** 248 (Details this exact sequential phenomenon)
*   **Firoz Note:** 101

***

### Page 8, Q.8(a): Define speed regulation. Draw and explain the torque and speed versus armature current characteristics of DC motors. [Figure Involved]

**Solution:**
**1. Definition of Speed Regulation:**
Speed regulation is a measure of a motor's ability to maintain its speed when a load is applied. It is defined as the change in speed when the load on the motor is reduced from its rated (full) value to zero, expressed as a percentage of the rated full-load speed.
$$\% \text{ Speed Regulation (SR)} = \frac{\text{No Load Speed } (N_{NL}) - \text{Full Load Speed } (N_{FL})}{\text{Full Load Speed } (N_{FL})} \times 100\%$$
*   A motor with a *positive* speed regulation (like a shunt motor) experiences a speed drop under load.
*   A motor with a *negative* speed regulation (like a differential compound motor) experiences a speed increase under load.

**2. Torque vs. Armature Current Characteristics ($\tau$ vs $I_a$):**
Also known as the *Electrical Characteristic*, this shows how pulling power scales with current.
*   **Shunt Motor:** Flux ($\Phi$) is constant. Since $\tau \propto \Phi I_a$, torque increases perfectly linearly with armature current. 
*   **Series Motor:** Flux ($\Phi$) is proportional to $I_a$ before saturation. Since $\tau \propto \Phi I_a \propto I_a^2$, the torque increases exponentially (a parabola) at lower currents. After the iron core saturates, flux becomes constant, and the curve straightens into a linear slope.
*   **Compound Motors:** Cumulative compound torque rises faster than shunt but slower than series (because series field aids shunt field). Differential compound torque drops below the shunt line (because series field opposes shunt field).

**3. Speed vs. Armature Current Characteristics ($N$ vs $I_a$):**
This shows how speed reacts to the current drawn.
*   **Shunt Motor:** $N \propto V - I_a R_a$. As $I_a$ increases, the $I_aR_a$ voltage drop increases, causing a very slight, linear drop in speed. 
*   **Series Motor:** $N \propto \frac{1}{\Phi} \propto \frac{1}{I_a}$. Speed is inversely proportional to current. At near-zero current, speed is dangerously high. As current increases, speed drops very rapidly (hyperbolic curve).
*   **Compound Motors:** Cumulative compound speed drops more sharply than shunt but avoids the dangerous no-load runaway of a series motor. Differential compound speed actually *rises* as current increases due to the severe demagnetization of the opposing series field, leading to severe instability.

**Figures involved:** 
1. **Torque vs $I_a$ Plot:** Shows a straight line for Shunt, a parabola for Series, and the two compound curves acting as intermediate bounds.
2. **Speed vs $I_a$ Plot:** Shows the flat droop of Shunt, the steep hyperbolic decay of Series, the sharp droop of Cumulative, and the rising curve of Differential.
**References:** 
*   **Mam Slide:** 234 (Speed Regulation formula), 242, 260, 264
*   **Firoz Note:** 93, 94 (Speed Regulation), 103, 109

***

### Page 9, Q.6(a): Draw and explain the torque and speed characteristic of shunt motor, cumulative compound motor and differential compound motor. [Figure Involved]

**Solution:**
*(Note: As defined in DC machine theory, "Torque and Speed characteristic" specifically points to the **Mechanical Characteristic**, which is the plot of Speed ($N$) on the Y-axis versus Torque ($\tau$) on the X-axis).*

This characteristic compares how these three types of motors react mechanically to increasing physical loads.

**1. Shunt Motor:**
*   **Explanation:** In a shunt motor, the main flux is constant. As mechanical torque increases, the motor draws more current, creating a slightly larger internal voltage drop ($I_a R_a$). This results in a very slight, linear decrease in speed. 
*   **Characteristic:** It is practically a constant-speed motor, showing only a minimal droop from no-load to full-load.

**2. Cumulative Compound Motor:**
*   **Explanation:** In this motor, the series field winding is connected so that its magnetic flux *adds* to the shunt field flux ($\Phi_{total} = \Phi_{shunt} + \Phi_{series}$). As the mechanical load (and torque) increases, the motor draws more current. This increased current flows through the series field, making the total magnetic flux stronger.
*   Because speed is inversely proportional to flux ($N \propto 1/\Phi$), this strengthening of the magnetic field causes the speed to drop significantly more than it would in a pure shunt motor. 
*   **Characteristic:** The curve droops more steeply than the shunt motor, acting as a compromise between a shunt and a series motor. It provides higher starting torque than a shunt motor but avoids the dangerous infinite no-load speed of a series motor.

**3. Differential Compound Motor:**
*   **Explanation:** In this motor, the series field is connected so that its magnetic flux *opposes* the shunt field flux ($\Phi_{total} = \Phi_{shunt} - \Phi_{series}$). As load and torque increase, the rising current strengthens the opposing series field, which actively *weakens* the total magnetic flux of the machine.
*   Because a weaker flux forces a DC motor to spin faster to generate the necessary back EMF, the speed of the motor actually *increases* as the load increases.
*   **Characteristic:** The curve rises upward. This creates a highly unstable, dangerous positive feedback loop (more load $\rightarrow$ less flux $\rightarrow$ more speed $\rightarrow$ more current $\rightarrow$ even less flux). It tends to "run away" and is virtually never used in practical applications.

**Figures involved:** A single set of axes with Torque ($\tau$) on the horizontal axis and Speed ($N$ or $\omega$) on the vertical axis. 
*   The **Shunt** curve is a nearly flat, gently sloping downward line.
*   The **Cumulative** curve slopes downward much more steeply.
*   The **Differential** curve hooks aggressively upwards.
**References:** 
*   **Mam Slide:** 255 (Torque-speed comparison graph for Cumulative, Series, and Shunt), 258 (Differential torque-speed text and graph).
*   **Firoz Note:** 111 (Speed vs Torque combined graph showing all variations).
Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

*Note: The first two questions deal with the operational characteristics of DC motors and are covered in your provided documents. The last two questions deal with AC Induction Motors. Since AC machines are not covered in the provided "Mam slide" or "Firoz note" documents, I have provided the standard electrical engineering explanations for them.*

***

### Page 14, Q.3(a): Draw speed versus armature current and torque versus armature current characteristics of all dc motors. [Figure Involved]

**Solution:**
These characteristics define how the pulling power (torque) and rotational speed of a DC motor behave as the mechanical load (which dictates the armature current, $I_a$) increases. 

**1. Torque versus Armature Current ($\tau$ vs $I_a$) Characteristics:**
The fundamental torque equation is $\tau \propto \Phi I_a$.
*   **Shunt Motor:** The field winding is connected in parallel to the supply, making the field current and the resulting flux ($\Phi$) constant. Therefore, torque is directly proportional to armature current ($\tau \propto I_a$). 
    *   *Curve:* A straight diagonal line starting from the origin.
*   **Series Motor:** The field winding is in series with the armature, so the flux is proportional to the armature current ($\Phi \propto I_a$) before magnetic saturation. Therefore, $\tau \propto I_a \times I_a \Rightarrow \tau \propto I_a^2$. 
    *   *Curve:* A parabola that rises exponentially. After heavy loads cause the iron core to magnetically saturate, flux $\Phi$ becomes constant, and the curve straightens out into a linear line.
*   **Cumulative Compound Motor:** The series field flux adds to the constant shunt field flux. As $I_a$ increases, the total flux increases. 
    *   *Curve:* Rises faster than a shunt motor but slower than a series motor, sitting between the two curves.
*   **Differential Compound Motor:** The series field opposes the shunt field. As $I_a$ increases, the total flux decreases.
    *   *Curve:* Rises slower than a shunt motor and eventually flattens or drops off.

**2. Speed versus Armature Current ($N$ vs $I_a$) Characteristics:**
The fundamental speed equation is $N \propto \frac{V - I_a R_a}{\Phi}$.
*   **Shunt Motor:** Because $\Phi$ is constant, speed only depends on the voltage drop across the armature resistance ($I_a R_a$). As load increases, this drop increases slightly, causing a very small decrease in speed.
    *   *Curve:* A slightly drooping, nearly horizontal straight line. It is considered a constant-speed motor.
*   **Series Motor:** Speed is inversely proportional to flux ($N \propto 1/\Phi$). Since $\Phi \propto I_a$, speed is inversely proportional to current ($N \propto 1/I_a$). At practically zero current (no load), the speed shoots toward infinity. As load current increases, speed drops very sharply.
    *   *Curve:* A steep hyperbolic curve. 
*   **Cumulative Compound Motor:** The total flux increases with load current. Because $N \propto 1/\Phi$, this increasing flux causes the speed to drop significantly more than a shunt motor, but without the danger of "running away" to infinite speeds at no-load.
    *   *Curve:* Droops downward more steeply than the shunt motor curve.
*   **Differential Compound Motor:** The total flux decreases with load current. A decreasing denominator in the speed equation causes the speed to actively increase.
    *   *Curve:* Rises upward. This is highly unstable.

**[Figure Involved]:** 
1. **$\tau$ vs $I_a$ graph:** Showing a straight line (Shunt), a rising parabola (Series), and intermediate curves for compound motors.
2. **$N$ vs $I_a$ graph:** Showing a slightly drooping line (Shunt), a steep inverse hyperbola (Series), a steeper droop (Cumulative), and an upward rising curve (Differential).

**References:**
*   **Mam Slide:** 242, 260, 264
*   **Firoz Note:** 103, 109

***

### Page 15, Q.4(a): Derive the expression for induced torque of a real motor. Why a dc series motor should be firmly coupled with its load?

*(Note: The prompt text says "dc series motor shunt". This is a typographical error in the source material. A motor is either series or shunt. The context of the mechanical coupling danger specifically applies to a DC series motor).*

**Solution:**
**Part 1: Derivation of Induced Torque ($\tau_{ind}$)**
1.  In any DC motor, the electrical power that is successfully converted into gross mechanical power is given by the product of the Back EMF ($E_A$) and the armature current ($I_A$):
    $P_{conv} = E_A \times I_A$
2.  From physical mechanics, rotational mechanical power is equal to the induced torque ($\tau_{ind}$) multiplied by the mechanical angular velocity ($\omega_m$ in rad/s):
    $P_{conv} = \tau_{ind} \times \omega_m$
3.  Equating the electrical and mechanical power:
    $\tau_{ind} \times \omega_m = E_A \times I_A$
4.  The standard generated voltage (Back EMF) equation for a DC machine is:
    $E_A = \frac{Z P \Phi \omega_m}{2 \pi A}$
    (where $Z$=conductors, $P$=poles, $\Phi$=flux, $A$=parallel paths).
5.  Substitute the $E_A$ equation into the power equivalence equation:
    $\tau_{ind} \times \omega_m = \left( \frac{Z P \Phi \omega_m}{2 \pi A} \right) \times I_A$
6.  Cancel $\omega_m$ from both sides to isolate torque:
    $\tau_{ind} = \frac{Z P \Phi I_A}{2 \pi A}$
7.  Since $Z, P$, and $A$ are fixed physical design constants of the machine, they can be grouped into a single machine constant $K = \frac{Z P}{2 \pi A}$.
    **Result:** $\tau_{ind} = K \Phi I_A$

**Part 2: Why a DC Series Motor Must be Firmly Coupled with its Load**
*   The speed of a DC motor is inversely proportional to the magnetic flux ($N \propto \frac{1}{\Phi}$).
*   In a DC series motor, the field winding is in series with the armature, so the flux relies entirely on the load current ($\Phi \propto I_A$).
*   If a series motor is started without a load, or if the load is suddenly removed (e.g., a driving belt breaks or slips), the motor needs almost zero torque to spin. Therefore, it draws practically zero armature current ($I_A \approx 0$).
*   If the current is zero, the series field flux ($\Phi$) also drops to nearly zero (leaving only a tiny residual magnetism).
*   Because $N \propto \frac{1}{\text{nearly zero}}$, the speed of the motor shoots up to an infinitely dangerous level.
*   This "runaway" speed generates massive centrifugal forces that will physically tear the armature windings out of their slots and destroy the commutator. Therefore, a DC series motor must **never** be connected to a load via a belt; it must always be firmly connected using direct gears or solid mechanical couplings to ensure it never operates at no-load.

**[Figure Involved]:** None required for the derivation.
**References:**
*   **Mam Slide:** 238, 240 (Torque derivation); 262 (Series motor runaway danger).
*   **Firoz Note:** 76, 78, 82 (Torque derivation); 110 (Runaway danger).

***

### Page 31, Q.6(b): With the necessary diagram determine the average torque of 3-Φ induction motor when load is assumed inductive. [Figure Involved]

**Solution:**
*(Note: This is an AC machine question. DC machine notes do not cover this).*

In a 3-phase induction motor, torque is produced by the interaction of the rotating stator magnetic flux ($\Phi$) and the currents induced in the rotor ($I_2$). 

**Torque Determination:**
1.  **Rotor Circuit Nature:** The rotor of an induction motor consists of windings placed in steel slots. Because it consists of coils wrapped in iron, the rotor possesses both resistance ($R_2$) and a significant inductive reactance ($X_2$). Therefore, the rotor circuit is inherently **inductive**.
2.  **Phase Shift:** When the rotating magnetic flux ($\Phi$) cuts the rotor, it induces an alternating EMF ($E_2$) in the rotor conductors. Because the rotor circuit is inductive, the resulting alternating rotor current ($I_2$) does not peak at the same time as the EMF. Instead, the current $I_2$ **lags** the induced voltage $E_2$ by a phase angle $\theta_2$.
    *   $\cos\theta_2 = \frac{R_2}{\sqrt{R_2^2 + X_2^2}}$ (This is the rotor power factor).
3.  **Instantaneous Torque:** The instantaneous torque on any conductor is proportional to the product of the instantaneous flux and the instantaneous current.
4.  **Average Torque:** Because the current lags the voltage (and thus lags the flux wave), there are moments during the AC cycle where the flux is positive but the current is still negative. This produces momentary "negative torque" (a reverse push). 
    However, the positive torque periods are much larger than the negative torque periods. The net **average torque ($T$)** produced by the motor is proportional to the in-phase component of the current.
    $T \propto \Phi \cdot I_2 \cdot \cos\theta_2$
5.  Since the induced rotor voltage $E_2$ is directly proportional to the stator flux $\Phi$ ($E_2 \propto \Phi$), we can write:
    $T \propto E_2 I_2 \cos\theta_2$
    Replacing the proportionality with a constant $K$:
    **$T = K E_2 I_2 \cos\theta_2$**
    This proves that the average torque depends heavily on the rotor's power factor ($\cos\theta_2$). If the rotor were *too* inductive (very large $\theta_2$), the current would lag heavily, generating large negative torque loops and drastically reducing the average forward torque.

**[Figure Involved]:** 
A waveform diagram showing three superimposed AC sine waves across time/space:
1. The Flux wave ($\Phi$).
2. The induced Rotor Voltage wave ($E_2$), which is in phase with the flux.
3. The Rotor Current wave ($I_2$), which is shifted to the right, lagging behind $E_2$ by angle $\theta_2$.
The diagram should shade the areas where Flux and Current have the same sign (Positive Torque) and different signs (Negative Torque), visually demonstrating the average net positive torque.

**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 34, Q.5(b): Why the induction motor with squirrel cage rotor not useful where motor has to start against heavy load?

**Solution:**
*(Note: This is an AC machine question. DC machine notes do not cover this).*

An induction motor with a squirrel cage rotor is unsuitable for starting heavy, high-inertia loads because of its inherently **low starting torque** and **excessively high starting current**. 

**Detailed Explanation:**
1.  **The Starting Torque Equation:** The starting torque ($T_{st}$) of an induction motor is heavily dependent on the resistance of the rotor circuit. The formula for starting torque is proportional to:
    $T_{st} \propto \frac{E_2^2 R_2}{R_2^2 + X_{20}^2}$
    To obtain the maximum possible starting torque, the rotor resistance ($R_2$) must mathematically equal the rotor standstill reactance ($X_{20}$). 
2.  **The Squirrel Cage Design Problem:** In a squirrel cage rotor, the conductors are thick, solid aluminum or copper bars that are permanently short-circuited by heavy end-rings at both ends. 
    *   This construction is permanent. The rotor resistance ($R_2$) is fixed at a very **low** value by design (which is necessary to keep efficiency high and slip low during normal running conditions).
    *   Because the rotor is permanently short-circuited, it is physically impossible to connect external variable resistors into the rotor circuit to temporarily increase $R_2$ during startup.
3.  **The Consequence (Low Torque):** Because $R_2$ is fixed at a value much smaller than $X_{20}$, the starting torque produced is very low (often only 1.5 times the full-load torque). If the motor is connected to a heavy load (like a loaded conveyor belt or a large crane) that requires a massive initial "breakaway" torque, the motor will simply stall and fail to turn.
4.  **The Consequence (High Current):** At standstill (slip $s=1$), the relative speed of the magnetic field cutting the stationary rotor is at its absolute maximum. This induces a massive voltage and, due to the extremely low resistance of the short-circuited cage, draws a massive inrush current from the stator (typically 5 to 7 times the normal full-load current) at a very poor power factor.
5.  If the motor fails to turn because of the heavy load, this massive starting current will persist, rapidly overheating the stator windings and burning out the motor.

*(For heavy starting loads, a **Wound Rotor / Slip Ring Induction Motor** is used instead, because external resistors can be temporarily connected via the slip rings to maximize starting torque while limiting starting current).*

**[Figure Involved]:** None required.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

*Note: All four of these questions deal with Alternating Current (AC) machines—specifically 3-Phase Induction Motors. These topics are not present in the provided "Mam slide" or "Firoz note" documents, which are focused entirely on Direct Current (DC) machines and Transformers. I have provided the standard electrical engineering mathematical derivations and explanations for these AC machine concepts.*

***

### Page 34, Q.5(c): For an induction motor, prove that maximum torque under running condition varies directly as the square of the applied voltage.

**Solution:**
**Proof:**
1.  **General Torque Equation:** The electromagnetic torque ($T$) developed by a 3-phase induction motor under running conditions is given by the standard formula:
    $$T = \frac{3}{\omega_s} \cdot \frac{s E_2^2 R_2}{R_2^2 + (sX_2)^2}$$
    Where:
    *   $\omega_s$ = Synchronous angular velocity
    *   $s$ = Fractional slip
    *   $E_2$ = Rotor induced EMF per phase at standstill
    *   $R_2$ = Rotor resistance per phase
    *   $X_2$ = Rotor standstill reactance per phase

2.  **Condition for Maximum Torque:** By differentiating the torque equation with respect to slip ($s$) and equating it to zero ($\frac{dT}{ds} = 0$), we find the condition for maximum torque. The maximum torque occurs at a specific slip where:
    $$R_2 = sX_2 \implies s = \frac{R_2}{X_2}$$

3.  **Substituting to find $T_{max}$:** Substitute this value of $s$ back into the general torque equation:
    $$T_{max} = \frac{3}{\omega_s} \cdot \frac{\left(\frac{R_2}{X_2}\right) E_2^2 R_2}{R_2^2 + \left(\frac{R_2}{X_2} \cdot X_2\right)^2}$$
    $$T_{max} = \frac{3}{\omega_s} \cdot \frac{\frac{R_2^2}{X_2} E_2^2}{R_2^2 + R_2^2}$$
    $$T_{max} = \frac{3}{\omega_s} \cdot \frac{\frac{R_2^2}{X_2} E_2^2}{2R_2^2}$$
    $$T_{max} = \frac{3}{2 \omega_s X_2} \cdot E_2^2$$

4.  **Relating to Applied Voltage:** The rotor induced EMF at standstill ($E_2$) is induced by the stator flux, which is directly proportional to the applied stator supply voltage ($V$). Therefore, $E_2 \propto V$ (or $E_2 = k_1 V$).
    Substituting this into the maximum torque equation:
    $$T_{max} = \frac{3}{2 \omega_s X_2} \cdot (k_1 V)^2$$
    Since $3, 2, \omega_s, X_2$, and $k_1$ are all constants for a given motor:
    **$T_{max} \propto V^2$**

Thus, it is mathematically proven that the maximum breakdown torque developed by an induction motor varies directly as the square of the applied supply voltage.

**Figures involved:** None required for the pure mathematical proof.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is AC Induction Motors).

***

### Page 34, Q.6(a): With the helps of neat sketch, determine the average torque of an induction motor if the rotor is assumed to be fully inductive. [Figure Involved]

**Solution:**
**Determination:**
If the rotor of an induction motor is assumed to be **fully inductive** (meaning rotor resistance $R_2 = 0$), the average torque developed by the motor will be exactly **zero**. The motor would not turn.

**Explanation:**
1.  **The Phase Angle:** In an AC circuit, the nature of the impedance determines the phase angle between the voltage and the current. If the rotor circuit is purely inductive ($R_2 = 0$), the induced rotor current ($I_2$) will lag the induced rotor voltage ($E_2$) by exactly $90^\circ$ electrical.
2.  **Torque Equation:** The instantaneous torque developed by the rotor is proportional to the product of the instantaneous magnetic flux ($\Phi$) and the instantaneous rotor current ($I_2$). 
    The *average* torque ($T_{avg}$) over a full cycle depends on the power factor of the rotor circuit ($\cos \theta_2$):
    $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos \theta_2$$
3.  **Applying the Assumption:** Since the current lags the voltage by $90^\circ$ in a purely inductive circuit, the phase angle $\theta_2 = 90^\circ$.
    $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos(90^\circ)$$
    Because $\cos(90^\circ) = 0$:
    **$T_{avg} = 0$**

**[Figure Involved]:**
A waveform sketch is required here:
*   Draw an X-axis representing time (or electrical angle).
*   Draw a sine wave representing the Air-Gap Flux ($\Phi$). The induced EMF ($E_2$) is perfectly in phase with this flux.
*   Draw a second sine wave representing the Rotor Current ($I_2$) shifted to the right by exactly $90^\circ$ (it crosses zero when the Flux is at its peak).
*   Multiply the two waveforms point-by-point to draw the Torque wave. You will see that for the first 90 degrees, flux is positive but current is negative $\rightarrow$ Negative Torque. For the next 90 degrees, both are positive $\rightarrow$ Positive Torque. 
*   Because the phase shift is exactly 90 degrees, the area of the positive torque loops will perfectly match the area of the negative torque loops. They cancel each other out completely, resulting in an average net torque of zero.

**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 38, Q.5(b): What are the effect of rotor resistance on the developed torque of an induction motor under both starting and running conditions?

**Solution:**
The rotor resistance ($R_2$) has a dramatic, yet differing, effect on the motor's torque depending on whether the motor is just starting or running normally.

**1. Effect on Starting Torque ($s = 1$):**
*   At starting, the rotor is stationary, so slip $s = 1$. The starting torque ($T_{st}$) equation is:
    $$T_{st} \propto \frac{R_2}{R_2^2 + X_2^2}$$
*   Because the standstill reactance ($X_2$) is typically much larger than the inherent rotor resistance ($R_2$) in a standard motor, the denominator is dominated by $X_2^2$. Therefore, initially, increasing $R_2$ causes the numerator to grow faster than the denominator.
*   **Effect:** Increasing rotor resistance significantly **increases** the starting torque. The starting torque reaches its absolute maximum when $R_2$ is made equal to $X_2$. (This is why wound-rotor induction motors use external resistor banks during startup to achieve massive starting torque).

**2. Effect on Running Torque ($s$ is very small):**
*   Under normal running conditions, the motor spins close to synchronous speed. Slip $s$ is very small (e.g., $0.02$ to $0.05$).
*   The running torque equation is:
    $$T \propto \frac{s E_2^2 R_2}{R_2^2 + (sX_2)^2}$$
*   Because $s$ is tiny, the term $(sX_2)^2$ becomes negligibly small compared to $R_2^2$. We can ignore it, simplifying the proportionality to:
    $$T \propto \frac{s E_2^2 R_2}{R_2^2} \implies T \propto \frac{s E_2^2}{R_2}$$
*   **Effect:** Under running conditions, torque is *inversely* proportional to rotor resistance. If $R_2$ is artificially kept high while running, the motor produces less torque for a given speed. To maintain the torque required by the load, the motor must increase its slip (slow down). Therefore, high rotor resistance leads to poor speed regulation and high $I^2R$ copper losses (poor efficiency) during normal running.

**Summary:** High rotor resistance is excellent for starting (high torque, low inrush current) but terrible for running (low efficiency, poor speed regulation). 

**Figures involved:** None required.
**References:** Not explicitly covered in the provided DC Machine slides or notes.

***

### Page 39, Q.8(d): The following impedances in ohms per phase referred to the stator circuit of a 460V, 25 hp, 60 Hz, 4 pole, Y connected wound rotor induction motor are: R1=0.641Ω , R2=0.332Ω , X1=1.106Ω , X2=0.464Ω , Xm= 26.3Ω. (i) What is the maximum torque of this motor? At what speed and slip does it occur? (ii) When the rotor resistance is doubled, what is the speed at which maximum torque occurs? What is the new starting torque of the motor?

**Solution:**
This requires the application of the Thevenin Equivalent Circuit for an induction motor. 

**Given Data:**
*   $V_{LL} = 460$ V $\implies$ Phase Voltage $V_{\phi} = \frac{460}{\sqrt{3}} \approx 265.58$ V
*   Poles $P = 4$, Freq $f = 60$ Hz
*   $N_s = \frac{120 \times 60}{4} = 1800$ rpm $\implies \omega_s = \frac{1800 \times 2\pi}{60} = 188.5$ rad/s
*   $R_1 = 0.641\Omega$, $X_1 = 1.106\Omega$
*   $R_2 = 0.332\Omega$, $X_2 = 0.464\Omega$
*   $X_m = 26.3\Omega$

**Step 1: Calculate Thevenin Equivalent Voltage ($V_{th}$) & Impedance ($R_{th}, X_{th}$)**
Using standard approximations to refer the stator to the magnetizing branch:
$$V_{th} \approx V_{\phi} \frac{X_m}{X_1 + X_m} = 265.58 \times \frac{26.3}{1.106 + 26.3} = 265.58 \times 0.9596 \approx \mathbf{254.85 \text{ V}}$$
$$R_{th} \approx R_1 \left( \frac{X_m}{X_1 + X_m} \right)^2 = 0.641 \times (0.9596)^2 \approx \mathbf{0.590 \, \Omega}$$
$$X_{th} \approx X_1 = \mathbf{1.106 \, \Omega}$$

**(i) Maximum Torque, Speed, and Slip**
*   **Slip at Max Torque ($S_{max}$):**
    $$S_{max} = \frac{R_2}{\sqrt{R_{th}^2 + (X_{th} + X_2)^2}} = \frac{0.332}{\sqrt{0.59^2 + (1.106 + 0.464)^2}}$$
    $$S_{max} = \frac{0.332}{\sqrt{0.348 + (1.57)^2}} = \frac{0.332}{\sqrt{0.348 + 2.4649}} = \frac{0.332}{1.677} \approx \mathbf{0.198}$$
    **Answer: Slip at max torque is 19.8% (0.198).**

*   **Speed at Max Torque ($N_{max}$):**
    $$N_{max} = N_s(1 - S_{max}) = 1800(1 - 0.198) = 1800 \times 0.802 = \mathbf{1443.6 \text{ rpm}}$$
    **Answer: Speed at max torque is 1443.6 rpm.**

*   **Maximum Torque ($T_{max}$):**
    $$T_{max} = \frac{3 V_{th}^2}{2 \omega_s \left[ R_{th} + \sqrt{R_{th}^2 + (X_{th} + X_2)^2} \right]}$$
    $$T_{max} = \frac{3 \times (254.85)^2}{2 \times 188.5 \times \left[ 0.590 + 1.677 \right]} = \frac{194845}{377 \times 2.267} = \frac{194845}{854.6} \approx \mathbf{228.0 \text{ N-m}}$$
    **Answer: Maximum torque is 228.0 N-m.**

**(ii) When Rotor Resistance is Doubled ($R_2' = 2 \times 0.332 = 0.664 \, \Omega$)**
*Note: Changing rotor resistance does NOT change the magnitude of the maximum torque, it only shifts the speed/slip at which it happens.*

*   **New Slip at Max Torque ($S_{max}'$):**
    Because $S_{max} \propto R_2$, if resistance doubles, the slip at max torque doubles.
    $$S_{max}' = 2 \times 0.198 = \mathbf{0.396}$$
*   **New Speed at Max Torque ($N'_{max}$):**
    $$N'_{max} = N_s(1 - S_{max}') = 1800(1 - 0.396) = 1800 \times 0.604 = \mathbf{1087.2 \text{ rpm}}$$
    **Answer: The speed at which maximum torque occurs is now 1087.2 rpm.**

*   **New Starting Torque ($T_{start}$):**
    At starting, slip $s = 1$. Use the Thevenin torque equation with $s=1$ and the new doubled $R_2'$:
    $$T_{start} = \frac{3 V_{th}^2 \left( \frac{R_2'}{1} \right)}{\omega_s \left[ (R_{th} + R_2')^2 + (X_{th} + X_2)^2 \right]}$$
    $$T_{start} = \frac{3 \times (254.85)^2 \times 0.664}{188.5 \left[ (0.590 + 0.664)^2 + (1.57)^2 \right]}$$
    $$T_{start} = \frac{194845 \times 0.664}{188.5 \left[ (1.254)^2 + 2.4649 \right]}$$
    $$T_{start} = \frac{129377}{188.5 \left[ 1.572 + 2.4649 \right]} = \frac{129377}{188.5 \times 4.037} = \frac{129377}{760.9} \approx \mathbf{170.0 \text{ N-m}}$$
    **Answer: The new starting torque is 170.0 N-m.**

**Figures involved:** None required for the calculation.
**References:** Not explicitly covered in the provided DC Machine slides or notes.


Here are the detailed solutions for the next four questions from your syllabus/PYQ list.

*Note: All four of these questions deal with Alternating Current (AC) machines—specifically 3-Phase Induction Motors. These topics are not present in the provided "Mam slide" or "Firoz note" documents, which are focused entirely on Direct Current (DC) machines and Transformers. I have provided the standard electrical engineering mathematical derivations and explanations for these AC machine concepts.*

***

### Page 42, Q.6(b): Prove that the rotor torque at any slip S can be expressed by the following equation: T = Tb[ 2 / ((Sb/S) + (S/Sb)) ] where the symbols have their usual meanings.

**Solution:**
**Proof:**
This derivation relates the torque at any slip ($T$) to the maximum breakdown torque ($T_b$) and the slip at which breakdown torque occurs ($S_b$).

1.  **General Torque Equation:** The electromagnetic torque of a 3-phase induction motor at any slip $S$ is given by:
    $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 + (S X_2)^2}$$
    *(where $k$ is a constant, $E_2$ is rotor induced EMF at standstill, $R_2$ is rotor resistance, and $X_2$ is rotor standstill reactance).*

2.  **Condition for Maximum Torque ($T_b$):** The maximum breakdown torque occurs at a specific slip ($S_b$) where the rotor resistance equals the slip reactance:
    $$R_2 = S_b X_2 \implies X_2 = \frac{R_2}{S_b}$$

3.  **Substituting $X_2$ into the General Torque Equation:**
    Replace $X_2$ in the general torque equation with $\frac{R_2}{S_b}$:
    $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 + \left(S \frac{R_2}{S_b}\right)^2}$$
    $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 + R_2^2 \left(\frac{S}{S_b}\right)^2}$$
    Factor out $R_2^2$ in the denominator:
    $$T = \frac{k \cdot S \cdot E_2^2 \cdot R_2}{R_2^2 \left[1 + \left(\frac{S}{S_b}\right)^2\right]} = \frac{k \cdot S \cdot E_2^2}{R_2 \left[1 + \left(\frac{S}{S_b}\right)^2\right]}$$

4.  **Find the Breakdown Torque ($T_b$):**
    To find the expression for maximum torque $T_b$, substitute $S = S_b$ into the general torque equation:
    $$T_b = \frac{k \cdot S_b \cdot E_2^2 \cdot R_2}{R_2^2 + (S_b X_2)^2}$$
    Since $S_b X_2 = R_2$:
    $$T_b = \frac{k \cdot S_b \cdot E_2^2 \cdot R_2}{R_2^2 + R_2^2} = \frac{k \cdot S_b \cdot E_2^2 \cdot R_2}{2 R_2^2} = \frac{k \cdot S_b \cdot E_2^2}{2 R_2}$$
    From this, we can isolate the constant terms:
    $$\frac{k \cdot E_2^2}{R_2} = \frac{2 T_b}{S_b}$$

5.  **Final Substitution:**
    Substitute $\frac{k \cdot E_2^2}{R_2}$ back into the simplified torque equation from Step 3:
    $$T = \left( \frac{2 T_b}{S_b} \right) \cdot \frac{S}{\left[1 + \left(\frac{S}{S_b}\right)^2\right]}$$
    $$T = \frac{2 T_b \left(\frac{S}{S_b}\right)}{1 + \frac{S^2}{S_b^2}}$$
    Divide the numerator and the denominator by $\left(\frac{S}{S_b}\right)$:
    $$T = \frac{2 T_b}{\frac{1}{\left(\frac{S}{S_b}\right)} + \frac{\frac{S^2}{S_b^2}}{\left(\frac{S}{S_b}\right)}}$$
    $$T = \frac{2 T_b}{\frac{S_b}{S} + \frac{S}{S_b}}$$
    **$T = T_b \left[ \frac{2}{\frac{S_b}{S} + \frac{S}{S_b}} \right]$** (Proved)

**Figure involved:** None required for the mathematical proof.
*   **Mam Slide:** N/A (Topic is AC Induction Motors; slides cover only DC machines).
*   **Firoz Note:** N/A (Topic is AC Induction Motors; notes cover only DC machines & Transformers).

***

### Page 45, Q.6(a): With the help of neat sketch determine the average torque of an induction motor if the rotor is assumed fully inductive. [Figure Involved]

**Solution:**
*(Note: This is fundamentally the same question as Page 34, Q.6(a), which asks for the determination of average torque for a fully inductive rotor).*

**Determination:**
If the rotor circuit of an induction motor is assumed to be **fully inductive** (meaning its resistance $R_2 = 0 \Omega$), the average torque developed by the motor will be **zero**, and it will fail to rotate.

**Explanation:**
1.  **Phase Relationship:** The electromagnetic torque developed in an induction motor depends on the interaction between the air-gap magnetic flux ($\Phi$) and the induced rotor current ($I_2$). 
    The average torque is proportional to the real power factor of the rotor circuit: 
    $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos \theta_2$$
    where $\theta_2$ is the phase angle between the induced rotor EMF ($E_2$) and the rotor current ($I_2$).
2.  **Pure Inductance:** If the rotor is fully inductive ($R_2 = 0$), the circuit is purely reactive. In a purely inductive AC circuit, the current lags the voltage by exactly 90 electrical degrees. Therefore, $\theta_2 = 90^\circ$.
3.  **Average Torque Calculation:** 
    Substitute $\theta_2 = 90^\circ$ into the torque proportionality:
    $$T_{avg} \propto \Phi \cdot I_2 \cdot \cos(90^\circ)$$
    Since $\cos(90^\circ) = 0$:
    **$T_{avg} = 0$**
    This means the motor produces equal amounts of forward (positive) torque and backward (negative) torque during every electrical cycle, completely canceling each other out.

**[Figure Involved]:**
You must draw a waveform diagram showing three superimposed waves over one full cycle (0 to $360^\circ$):
1.  **Air-Gap Flux ($\Phi$) wave:** A standard sine wave starting at 0.
2.  **Rotor EMF ($E_2$) wave:** A sine wave perfectly in-phase with the flux wave.
3.  **Rotor Current ($I_2$) wave:** A sine wave that is shifted to the right, lagging the $E_2$ wave by exactly $90^\circ$ (crossing zero when $E_2$ is at its peak).
*   Below these, sketch the **Torque ($T$) wave** by multiplying the $\Phi$ and $I_2$ waves point-by-point. The result will be a double-frequency sine wave centered perfectly on the horizontal axis. Shade the positive loops (above the axis) and negative loops (below the axis). The graph visually demonstrates that the positive area equals the negative area, yielding a net average torque of zero.

*   **Mam Slide:** N/A (Topic is AC Induction Motors; slides cover only DC machines).
*   **Firoz Note:** N/A (Topic is AC Induction Motors; notes cover only DC machines & Transformers).

***

### Page 45, Q.6(b): Show that, for obtaining maximum torque of an induction motor at starting ,total resistance must be equal to rotor reactance.

**Solution:**
**Proof:**
1.  **General Torque Equation:** The torque of a 3-phase induction motor is given by:
    $$T = \frac{k \cdot s \cdot E_2^2 \cdot R_2}{R_2^2 + (sX_2)^2}$$
    where $s$ is slip, $E_2$ is standstill rotor EMF, $R_2$ is rotor resistance, and $X_2$ is standstill rotor reactance.

2.  **Starting Torque Equation:** At the exact moment of starting, the rotor is stationary, which means the synchronous speed relative to the rotor is at its maximum. Therefore, the slip at starting is $s = 1$.
    Substitute $s = 1$ into the general torque equation to get the Starting Torque ($T_{st}$):
    $$T_{st} = \frac{k \cdot (1) \cdot E_2^2 \cdot R_2}{R_2^2 + (1 \cdot X_2)^2}$$
    $$T_{st} = \frac{k \cdot E_2^2 \cdot R_2}{R_2^2 + X_2^2}$$

3.  **Finding the Maximum:** To find the mathematical condition that yields the maximum possible starting torque with respect to the rotor resistance ($R_2$), we must take the derivative of $T_{st}$ with respect to $R_2$ and equate it to zero:
    $$\frac{dT_{st}}{dR_2} = 0$$

4.  **Differentiating the Equation:** Using the quotient rule $\frac{u'v - uv'}{v^2}$ on the term $\frac{R_2}{R_2^2 + X_2^2}$ (treating $k E_2^2$ as a constant):
    $$\frac{d}{dR_2} \left[ \frac{k E_2^2 R_2}{R_2^2 + X_2^2} \right] = k E_2^2 \left[ \frac{(R_2^2 + X_2^2) \cdot \frac{d}{dR_2}(R_2) - R_2 \cdot \frac{d}{dR_2}(R_2^2 + X_2^2)}{(R_2^2 + X_2^2)^2} \right]$$
    $$0 = k E_2^2 \left[ \frac{(R_2^2 + X_2^2)(1) - R_2(2R_2)}{(R_2^2 + X_2^2)^2} \right]$$

5.  **Solving for $R_2$:** For the entire expression to equal zero, the numerator inside the bracket must equal zero:
    $$R_2^2 + X_2^2 - 2R_2^2 = 0$$
    $$X_2^2 - R_2^2 = 0$$
    $$R_2^2 = X_2^2$$
    **$R_2 = X_2$**

Thus, it is mathematically proven that to achieve the absolute maximum possible torque at the moment of starting ($s=1$), the total per-phase rotor resistance must be made exactly equal to the per-phase standstill rotor reactance. (This is physically accomplished in wound-rotor motors by inserting external resistor banks during startup).

**Figure involved:** None required for the mathematical proof.
*   **Mam Slide:** N/A (Topic is AC Induction Motors; slides cover only DC machines).
*   **Firoz Note:** N/A (Topic is AC Induction Motors; notes cover only DC machines & Transformers).

***

### Page 46, Q.7(a): Draw the complete torque-slip curve of an induction machine. [Figure Involved]

**Solution:**
The complete torque-slip curve graphs the electromagnetic torque developed by an induction machine across all possible ranges of slip (from $s < 0$ to $s > 1$). This illustrates the machine's ability to act as a motor, a generator, or a brake.

**Explanation of the Three Regions:**
1.  **Motoring Region ($0 < s < 1$):**
    *   This is the normal operating region. The rotor is spinning in the same direction as the magnetic field, but slightly slower ($0 < N < N_s$).
    *   At $s = 0$ (synchronous speed), Torque $= 0$.
    *   As load is applied, the motor slows down, slip increases, and torque rises almost linearly.
    *   Torque reaches a peak called the Breakdown Torque ($T_{max}$) at a specific slip ($s_{max} = R_2/X_2$).
    *   If slip increases beyond $s_{max}$ towards $s=1$ (standstill), the curve droops downward to the Starting Torque value.

2.  **Generating Region ($s < 0$):**
    *   In this region, the rotor is mechanically driven by a prime mover *faster* than the synchronous speed ($N > N_s$).
    *   Because the rotor is moving faster than the field, the slip becomes negative.
    *   The induced torque reverses direction (becomes negative). It acts as a mechanical braking force against the prime mover, converting mechanical energy into electrical energy fed back to the grid (Asynchronous Generator).
    *   The curve mirrors the motoring region but in the negative torque/negative slip quadrant.

3.  **Braking / Plugging Region ($s > 1$):**
    *   This occurs if the rotor is spinning in the *opposite* direction to the rotating magnetic field (e.g., if two phases of the supply are suddenly swapped while running).
    *   Since $N$ is negative, $s = \frac{N_s - (-N)}{N_s} > 1$.
    *   The torque remains positive (pushing in the direction of the magnetic field), but because the rotor is physically moving backward, this acts as a massive mechanical brake, rapidly decelerating the machine. The torque steadily decreases as slip increases beyond 1.

**[Figure Involved]:**
You must sketch a complete continuous graph with **Slip ($s$) on the X-axis** and **Torque ($T$) on the Y-axis**.
*   **X-axis mapping:** Mark $s=0$ in the middle. Moving to the right: $s=1$, then $s=2$. Moving to the left: $s=-1$.
*   *(Note: The corresponding speed $N$ runs in reverse on the X-axis. $N=N_s$ is at $s=0$; $N=0$ is at $s=1$; $N=-N_s$ is at $s=2$).*
*   **The Curve:**
    *   **Right Side (Motoring):** From $s=0, T=0$, draw a curve rising steeply upward into the positive Y quadrant, peaking at $T_{max}$, then drooping down to a positive $T_{start}$ value at $s=1$. Mark this area "$0 < s < 1$: Motoring".
    *   **Far Right Side (Braking):** From $s=1$, continue the curve drooping gently downward as it approaches $s=2$. Mark this area "$s > 1$: Braking/Plugging".
    *   **Left Side (Generating):** From $s=0, T=0$, draw the curve dipping steeply downward into the negative Y quadrant, reaching a negative peak ($-T_{max}$), and then sloping back up toward the X-axis as slip becomes more negative. Mark this area "$s < 0$: Generating".

*   **Mam Slide:** N/A (Topic is AC Induction Motors; slides cover only DC machines).
*   **Firoz Note:** N/A (Topic is AC Induction Motors; notes cover only DC machines & Transformers).

*Note: There is only **one** question remaining from the original list of PYQs you provided in your first prompt. I have provided its detailed mathematical solution below, which completely concludes the entire list of questions you uploaded.*

***

### Page 46, Q.7(c): A 3-Φ, 440V, 50 Hz. 40-pole Y-connected induction motor has rotor resistance of 0.1 ohm and reactance 0.9 ohm per phase. The ratio of stator to rotor turns is 3.5. Calculate (i) gross output at a slip of 5% (ii) the maximum torque in synchronous watts and corresponding slip.

**Solution:**
This problem requires calculating the mechanical power output and maximum torque properties using the equivalent circuit parameters of the induction motor rotor.

**Given Data:**
*   Supply Line Voltage ($V_L$) = 440 V
*   Frequency ($f$) = 50 Hz
*   Number of poles ($P$) = 40
*   Rotor resistance per phase ($R_2$) = 0.1 $\Omega$
*   Rotor standstill reactance per phase ($X_2$) = 0.9 $\Omega$
*   Stator to rotor turns ratio ($a = N_1/N_2$) = 3.5
*   Operating slip ($s$) = 5% = 0.05

**Step 1: Calculate the Rotor Phase Voltage at Standstill ($E_2$)**
Since the stator is Y-connected, the stator phase voltage ($V_{1\phi}$) is:
$$V_{1\phi} = \frac{V_L}{\sqrt{3}} = \frac{440}{\sqrt{3}} \approx 254.03 \text{ V}$$
Assuming the stator voltage is directly proportional to the induced rotor voltage by the turns ratio, the rotor phase voltage at standstill ($E_2$) is:
$$E_2 = \frac{V_{1\phi}}{a} = \frac{254.03}{3.5} \approx 72.58 \text{ V per phase}$$

---

**(i) Calculate Gross Output at a slip of 5% ($s = 0.05$)**

**Step 2: Calculate the Rotor Current ($I_2$) at 5% slip**
The formula for rotor current at any slip $s$ is:
$$I_2 = \frac{s \cdot E_2}{\sqrt{R_2^2 + (sX_2)^2}}$$
$$I_2 = \frac{0.05 \times 72.58}{\sqrt{0.1^2 + (0.05 \times 0.9)^2}}$$
$$I_2 = \frac{3.629}{\sqrt{0.01 + (0.045)^2}}$$
$$I_2 = \frac{3.629}{\sqrt{0.01 + 0.002025}} = \frac{3.629}{\sqrt{0.012025}} = \frac{3.629}{0.10966} \approx \mathbf{33.09 \text{ A}}$$

**Step 3: Calculate the Gross Mechanical Output Power ($P_m$)**
The gross mechanical power developed by all 3 phases is given by:
$$P_m = 3 \times I_2^2 \times R_2 \times \left( \frac{1 - s}{s} \right)$$
$$P_m = 3 \times (33.09)^2 \times 0.1 \times \left( \frac{1 - 0.05}{0.05} \right)$$
$$P_m = 3 \times 1094.95 \times 0.1 \times \left( \frac{0.95}{0.05} \right)$$
$$P_m = 328.485 \times 19 \approx \mathbf{6241.2 \text{ Watts or } 6.24 \text{ kW}}$$

**Answer (i): The gross output power is 6.24 kW.**

---

**(ii) Calculate the Maximum Torque in Synchronous Watts and Corresponding Slip**

**Step 4: Calculate the Corresponding Slip for Maximum Torque ($s_m$)**
Maximum torque occurs when the rotor resistance equals the slip reactance ($R_2 = s_m X_2$).
$$s_m = \frac{R_2}{X_2} = \frac{0.1}{0.9} = \frac{1}{9} \approx \mathbf{0.1111 \text{ (or } 11.11\%)}$$

**Step 5: Calculate Maximum Torque in Synchronous Watts**
Torque expressed in "synchronous watts" is numerically equal to the air-gap power ($P_g$). The formula for maximum air-gap power (ignoring stator impedance as is standard when only rotor parameters are given) is:
$$T_{max (syn \, watts)} = 3 \times \frac{E_2^2}{2 X_2}$$
$$T_{max (syn \, watts)} = 3 \times \frac{(72.58)^2}{2 \times 0.9}$$
$$T_{max (syn \, watts)} = 3 \times \frac{5267.85}{1.8} = \frac{15803.55}{1.8} \approx \mathbf{8780 \text{ Synchronous Watts}}$$

**Answer (ii): The maximum torque is 8780 Synchronous Watts, occurring at a slip of 11.11%.**

**Figures involved:** None required for the calculation.
**References:** Not explicitly covered in the provided DC Machine slides or notes (Subject matter is purely mathematical AC Induction Motor analysis).








