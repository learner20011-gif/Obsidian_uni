Here are the detailed solutions for the first 4 questions from your provided syllabus list. 

### 1. Page 4, Q.52: Explain the principle of operation of a DC motor.

**Solution:**
A DC motor is an electromechanical energy conversion device that converts electrical energy from a DC supply into mechanical energy. 

**Principle of Operation:**
The fundamental principle of a DC motor is based on the electromagnetic force exerted on a current-carrying conductor. When a current-carrying conductor is placed in a magnetic field, it experiences a mechanical force. 

1. **Force Generation:** The magnitude of the induced force in the conductor is proportional to the magnetic flux density ($B$), the conductor current ($I$), and the effective length of the conductor ($L$). It is given by the equation:
   $$F = B \cdot I \cdot L \cdot \sin\theta$$
   (Where $\theta$ is the angle between the conductor and the magnetic field).
2. **Direction of Force:** The direction of this force is determined by **Fleming's Left-Hand Rule**. If you extend your left hand such that the index finger points in the direction of the magnetic field (North to South) and the middle finger points in the direction of the current, then the thumb will point in the direction of the exerted mechanical force.
3. **Torque Production:** In a DC motor, the armature (rotor) consists of a coil with multiple conductors. When DC voltage is supplied to the motor, current flows through the field windings (creating a constant magnetic field) and the armature windings. The conductors on opposite sides of the armature coil experience forces in opposite directions, creating a rotational torque.
4. **Commutator Action:** As the coil rotates and passes the magnetic neutral plane, the commutator (acting as a mechanical rectifier/inverter) automatically reverses the direction of the current in the coil. This ensures that the force on the conductors always acts in the same rotational direction, keeping the motor spinning continuously.

* **Reference in Mam Slide:** 20, 214, 215, 216
* **Reference in Firoz Note:** 2, 72, 74, 76

---

### 2. Page 5, Q.71: How will you change the direction of rotation of a d.c motor?

**Solution:**
The direction of rotation in a DC motor is determined by the direction of the mechanical force acting on its armature conductors. According to Fleming's Left-Hand Rule, the direction of this force depends entirely on two factors:
1. The direction of the main magnetic field (Flux).
2. The direction of the current flowing through the armature conductors.

To change the direction of rotation of a DC motor, you must reverse the direction of the torque. This can be achieved by reversing exactly **one** of the above two factors:
* **Method 1 (Reversing Armature Current):** By interchanging the electrical connections of the armature terminals at the supply, the current flows in the opposite direction through the rotor. While the field polarity remains unchanged, the resulting force and torque are reversed, causing the motor to rotate in the opposite direction.
* **Method 2 (Reversing Field Current):** By interchanging the connections of the field winding terminals, the magnetic poles (North and South) are swapped. If the armature current direction is kept the same, the reversed magnetic flux will reverse the direction of the torque, thereby reversing the motor's rotation.

*Note:* If you reverse *both* the armature connections and the field connections simultaneously, the two reversals will cancel each other out, and the motor will continue to rotate in its original direction.

* **Reference in Mam Slide:** 214, 295
* **Reference in Firoz Note:** 91, 114

---

### 3. Page 9, Q.5(a): Describe the construction and working principle of DC motor.

**Solution:**
**Construction of DC Motor:**
The internal construction of a DC motor is virtually identical to that of a DC generator. It consists of the following primary components:
1. **Stator / Yoke:** The outer stationary frame of the motor. It provides mechanical support, protects the inner parts, and carries the magnetic flux produced by the poles. It is usually made of cast iron or steel.
2. **Field System (Pole Core, Pole Shoe, and Field Windings):** The electromagnets attached to the inner wall of the yoke. The field windings (made of copper) are energized by DC excitation to produce a constant magnetic field. The pole shoes spread the flux evenly across the air gap.
3. **Armature (Rotor):** The rotating, cylindrical part of the machine made of highly permeable laminated silicon steel to reduce eddy current losses. It has slots on its periphery that house the **armature windings** where the current is run to create a secondary magnetic field.
4. **Commutator:** Mounted on the rotor shaft, it is made of copper segments insulated from each other by mica. It connects the rotating armature coils to the stationary external circuit and reverses the current in the armature coils as they cross the magnetic neutral axis.
5. **Brushes:** Stationary graphite or carbon blocks that press against the commutator. They supply the incoming DC current from the power source to the rotating commutator.
* **Figure Involved:** Cross-sectional diagram of a DC Machine showing the Stator, Rotor, Yoke, Poles, Armature conductors, Commutator, and Shaft.

**Working Principle:**
As described in Q.52, when a DC supply is connected across the motor terminals, current passes through the field windings establishing a stationary magnetic field. Simultaneously, current is passed into the armature through the brushes and commutator. The current-carrying armature conductors interact with the main magnetic field, experiencing a mechanical force determined by $F=BLI\sin\theta$. Using Fleming's Left-Hand Rule, we can see that conductors under the North pole are pushed in one direction, while those under the South pole are pushed in the opposite direction, creating a rotational torque. The commutator periodically reverses the armature current to keep the torque acting in a single, unidirectional continuous motion.

* **Reference in Mam Slide:** 10, 11, 12, 61, 62, 63, 65, 236
* **Reference in Firoz Note:** 72, 74, 78

---

### 4. Page 4, Q.54: Define counter EMF. Explain the significance of counter EMF of a dc motor.

*(Note: In the syllabus document, this falls under section "4. 2. Back E.M.F.")*

**Solution:**
**Definition of Counter EMF (Back EMF):**
When a DC motor's armature rotates within the magnetic field produced by the stator poles, the armature conductors "cut" the magnetic flux lines. According to Faraday's Law of Electromagnetic Induction, this cutting action induces an electromotive force (EMF) inside the rotating armature conductors. According to Lenz’s Law, the direction of this induced EMF opposes the original supply voltage ($V_t$) that caused the rotation. Because it acts against the applied terminal voltage, this induced voltage is called **Counter EMF** or **Back EMF** ($E_b$). 

Its magnitude is calculated exactly like a generator's EMF: 
$$E_b = \frac{P \Phi Z N}{60 A}$$ 
*(where P = poles, $\Phi$ = flux per pole, Z = total conductors, N = speed in RPM, A = parallel paths).*

**Significance of Counter EMF ($E_b$):**
1. **Limits Armature Current:** The net voltage driving current through the armature is the difference between the supply voltage and the back EMF ($V_t - E_b$). Because the armature resistance ($R_a$) is extremely low, if $E_b$ did not exist, a destructively high current would flow. Counter EMF restricts the armature current ($I_a$) to a safe operating limit: $I_a = \frac{V_t - E_b}{R_a}$.
2. **Makes the Motor Self-Regulating (Governor Action):** Back EMF allows the DC motor to automatically adjust its armature current to meet the mechanical load requirements:
   * **When load is added:** The motor temporarily slows down. A lower speed ($N$) reduces the back EMF ($E_b \propto N$). The lower $E_b$ allows a higher net voltage ($V_t - E_b$), which pushes a larger current ($I_a$) into the armature. This increased current generates the higher torque needed to drive the heavier load.
   * **When load is removed:** The motor speeds up, increasing $E_b$. This chokes off the net voltage, reducing the armature current ($I_a$) and torque until it perfectly matches the new, lighter load. 
3. **Energy Conversion:** The mechanical power developed by the motor ($P_m$) is directly equal to the electrical power required to overcome the back EMF ($P_m = E_b \cdot I_a$). Therefore, the presence of counter EMF is the fundamental reason electrical energy is successfully converted into mechanical work.

* **Reference in Mam Slide:** 220, 221, 222
* **Reference in Firoz Note:** 80, 81, 82
Here are the detailed solutions for the next 4 questions from your syllabus list (Items 6, 7, 8, and 9).

### 6. Page 4, Q.56: What is back EMF in a dc motor? What will happen if the back EMF (Eb) is equal to the terminal voltage (V) of a dc motor?

**Solution:**

**What is Back EMF:**
When the armature of a DC motor rotates in the magnetic field produced by the stator, the armature conductors cut the magnetic flux lines. According to Faraday's Law of Electromagnetic Induction, an electromotive force (EMF) is induced in these moving conductors. By Lenz's Law, the direction of this induced EMF always opposes the original applied terminal voltage that caused the current to flow. Because this induced voltage acts against the supply voltage, it is referred to as **Back EMF** or **Counter EMF** ($E_b$).

**What happens if $E_b = V$:**
The armature current ($I_a$) in a DC motor is determined by the difference between the applied terminal voltage ($V$) and the back EMF ($E_b$), limited only by the armature resistance ($R_a$):
$$I_a = \frac{V - E_b}{R_a}$$

If the back EMF becomes exactly equal to the terminal voltage ($E_b = V$), the numerator of the equation becomes zero. Consequently:
$$I_a = \frac{V - V}{R_a} = 0 \text{ A}$$
If the armature current drops to zero, the electromagnetic torque developed by the motor ($T \propto \Phi I_a$) will also drop to zero. Without any torque being generated, the motor cannot overcome internal friction, windage, and mechanical losses, causing it to slow down. Therefore, practically, $E_b$ can never be exactly equal to $V$ in a running motor. A motor must always draw a small amount of current to produce enough torque to keep itself spinning, meaning $E_b$ will always be slightly less than $V$.

* **Reference in Mam Slide:** 220, 221
* **Reference in Firoz Note:** 80, 81
* **Figure Involved:** None

---

### 7. Page 5, Q.67: For a dc motor, prove that the gross mechanical power developed by a motor is maximum when back emf is equal to half of the applied voltage.

**Solution:**

**Proof:**
The fundamental voltage equation for a DC motor is:
$$V = E_b + I_a R_a$$
Where:
*   $V$ = Applied terminal voltage
*   $E_b$ = Back EMF
*   $I_a$ = Armature current
*   $R_a$ = Armature resistance

To find the gross mechanical power developed ($P_m$), we multiply the entire voltage equation by the armature current $I_a$:
$$V I_a = E_b I_a + I_a^2 R_a$$
In this power equation:
*   $V I_a$ = Total electrical input power to the armature.
*   $I_a^2 R_a$ = Copper loss dissipated as heat in the armature.
*   $E_b I_a$ = Gross mechanical power developed by the motor ($P_m$).

Thus, the mechanical power is:
$$P_m = V I_a - I_a^2 R_a$$

To find the condition for maximum mechanical power, we assume $V$ and $R_a$ are constants and differentiate $P_m$ with respect to the variable $I_a$, then set the derivative equal to zero:
$$\frac{dP_m}{dI_a} = \frac{d}{dI_a} (V I_a - I_a^2 R_a) = 0$$
$$V - 2 I_a R_a = 0$$
$$2 I_a R_a = V \implies I_a R_a = \frac{V}{2}$$

Now, substitute $I_a R_a = \frac{V}{2}$ back into the original voltage equation ($V = E_b + I_a R_a$):
$$V = E_b + \frac{V}{2}$$
$$E_b = V - \frac{V}{2}$$
$$E_b = \frac{V}{2}$$

**Conclusion:** The gross mechanical power developed by a DC motor is maximum when the back EMF ($E_b$) is exactly half of the applied terminal voltage ($V$). *(Note: While true theoretically, this condition is never achieved in practical motors because it implies 50% electrical efficiency, causing the motor to burn out from excessive $I_a^2 R_a$ heat).*

* **Reference in Mam Slide:** 225
* **Reference in Firoz Note:** 85, 86
* **Figure Involved:** None

---

### 8. Page 8, Q.7(c): The armature resistance of a shunt motor is 0.08 Ω. When connected to 220 V supply, a counter EMF of 200 V is developed. Find (i) the armature current, (ii) the armature current when the armature is not rotating, and (iii) counter EMF when the armature current is 9.0 A.

**Solution:**

**Given Data:**
*   Applied terminal voltage, $V = 220 \text{ V}$
*   Armature resistance, $R_a = 0.08 \, \Omega$
*   Initial counter EMF, $E_{b1} = 200 \text{ V}$

**(i) Find the armature current:**
Using the voltage equation of a DC motor: $V = E_{b1} + I_{a1} R_a$.
Rearranging for armature current $I_{a1}$:
$$I_{a1} = \frac{V - E_{b1}}{R_a}$$
$$I_{a1} = \frac{220 - 200}{0.08} = \frac{20}{0.08} = 250 \text{ A}$$
**Answer (i): The armature current is 250 A.**

**(ii) Find the armature current when the armature is not rotating:**
When the armature is stationary (e.g., at the exact moment of starting), the rotational speed $N = 0$. Since back EMF is directly proportional to speed ($E_b \propto N$), the counter EMF is zero ($E_b = 0 \text{ V}$).
$$I_{a(start)} = \frac{V - 0}{R_a} = \frac{220}{0.08} = 2750 \text{ A}$$
**Answer (ii): The starting armature current is 2750 A.**

**(iii) Find the counter EMF when the armature current is 9.0 A:**
Let the new armature current be $I_{a2} = 9.0 \text{ A}$.
Using the voltage equation $V = E_{b2} + I_{a2} R_a$ and rearranging for $E_{b2}$:
$$E_{b2} = V - I_{a2} R_a$$
$$E_{b2} = 220 - (9.0 \times 0.08)$$
$$E_{b2} = 220 - 0.72 = 219.28 \text{ V}$$
**Answer (iii): The counter EMF is 219.28 V.**

* **Reference in Mam Slide:** 222
* **Reference in Firoz Note:** 81
* **Figure Involved:** None

---

### 9. Page 14, Q.4(a): What is meant by back emf? Prove that the gross power developed by a dc motor is maximum when the back emf (Eb) is equal to half of the applied voltage (V).

**Solution:**

**What is meant by Back EMF:**
When a DC motor is supplied with electrical energy, its armature rotates inside a magnetic field. As the armature conductors move, they cut the magnetic flux lines. According to Faraday's Law of Electromagnetic Induction, an electromotive force (EMF) is induced within these rotating conductors. According to Lenz's law, the direction of this induced voltage acts in opposition to the applied terminal voltage that drives the motor. Because it pushes back against the supply, this induced voltage is called the **Back EMF** or **Counter EMF** ($E_b$).

**Proof for maximum power:**
The fundamental voltage equation of a DC motor is given by:
$$V = E_b + I_a R_a$$
Multiply the entire equation by the armature current $I_a$ to convert it into a power equation:
$$V I_a = E_b I_a + I_a^2 R_a$$
The term $E_b I_a$ represents the gross mechanical power ($P_m$) developed by the motor armature. Rearranging for $P_m$:
$$P_m = V I_a - I_a^2 R_a$$
To find the condition for maximum mechanical power, we take the derivative of $P_m$ with respect to $I_a$ and set it to zero:
$$\frac{dP_m}{dI_a} = V - 2 I_a R_a = 0$$
$$2 I_a R_a = V \implies I_a R_a = \frac{V}{2}$$
Substituting $I_a R_a = \frac{V}{2}$ back into the basic voltage equation:
$$V = E_b + \frac{V}{2}$$
$$E_b = V - \frac{V}{2} = \frac{V}{2}$$
Thus, it is proven that the gross mechanical power developed by a DC motor reaches its mathematical maximum when the back EMF ($E_b$) is exactly equal to half of the applied voltage ($V$). 

* **Reference in Mam Slide:** 220, 221, 225
* **Reference in Firoz Note:** 80, 81, 85, 86
* **Figure Involved:** None
Here are the detailed solutions for the next 4 questions from your syllabus list (Items 6, 7, 8, and 9).

### 6. Page 4, Q.56: What is back EMF in a dc motor? What will happen if the back EMF (Eb) is equal to the terminal voltage (V) of a dc motor?

**Solution:**

**What is Back EMF:**
When the armature of a DC motor rotates in the magnetic field produced by the stator, the armature conductors cut the magnetic flux lines. According to Faraday's Law of Electromagnetic Induction, an electromotive force (EMF) is induced in these moving conductors. By Lenz's Law, the direction of this induced EMF always opposes the original applied terminal voltage that caused the current to flow. Because this induced voltage acts against the supply voltage, it is referred to as **Back EMF** or **Counter EMF** ($E_b$).

**What happens if $E_b = V$:**
The armature current ($I_a$) in a DC motor is determined by the difference between the applied terminal voltage ($V$) and the back EMF ($E_b$), limited only by the armature resistance ($R_a$):
$$I_a = \frac{V - E_b}{R_a}$$

If the back EMF becomes exactly equal to the terminal voltage ($E_b = V$), the numerator of the equation becomes zero. Consequently:
$$I_a = \frac{V - V}{R_a} = 0 \text{ A}$$
If the armature current drops to zero, the electromagnetic torque developed by the motor ($T \propto \Phi I_a$) will also drop to zero. Without any torque being generated, the motor cannot overcome internal friction, windage, and mechanical losses, causing it to slow down. Therefore, practically, $E_b$ can never be exactly equal to $V$ in a running motor. A motor must always draw a small amount of current to produce enough torque to keep itself spinning, meaning $E_b$ will always be slightly less than $V$.

* **Reference in Mam Slide:** 220, 221
* **Reference in Firoz Note:** 80, 81
* **Figure Involved:** None

---

### 7. Page 5, Q.67: For a dc motor, prove that the gross mechanical power developed by a motor is maximum when back emf is equal to half of the applied voltage.

**Solution:**

**Proof:**
The fundamental voltage equation for a DC motor is:
$$V = E_b + I_a R_a$$
Where:
*   $V$ = Applied terminal voltage
*   $E_b$ = Back EMF
*   $I_a$ = Armature current
*   $R_a$ = Armature resistance

To find the gross mechanical power developed ($P_m$), we multiply the entire voltage equation by the armature current $I_a$:
$$V I_a = E_b I_a + I_a^2 R_a$$
In this power equation:
*   $V I_a$ = Total electrical input power to the armature.
*   $I_a^2 R_a$ = Copper loss dissipated as heat in the armature.
*   $E_b I_a$ = Gross mechanical power developed by the motor ($P_m$).

Thus, the mechanical power is:
$$P_m = V I_a - I_a^2 R_a$$

To find the condition for maximum mechanical power, we assume $V$ and $R_a$ are constants and differentiate $P_m$ with respect to the variable $I_a$, then set the derivative equal to zero:
$$\frac{dP_m}{dI_a} = \frac{d}{dI_a} (V I_a - I_a^2 R_a) = 0$$
$$V - 2 I_a R_a = 0$$
$$2 I_a R_a = V \implies I_a R_a = \frac{V}{2}$$

Now, substitute $I_a R_a = \frac{V}{2}$ back into the original voltage equation ($V = E_b + I_a R_a$):
$$V = E_b + \frac{V}{2}$$
$$E_b = V - \frac{V}{2}$$
$$E_b = \frac{V}{2}$$

**Conclusion:** The gross mechanical power developed by a DC motor is maximum when the back EMF ($E_b$) is exactly half of the applied terminal voltage ($V$). *(Note: While true theoretically, this condition is never achieved in practical motors because it implies 50% electrical efficiency, causing the motor to burn out from excessive $I_a^2 R_a$ heat).*

* **Reference in Mam Slide:** 225
* **Reference in Firoz Note:** 85, 86
* **Figure Involved:** None

---

### 8. Page 8, Q.7(c): The armature resistance of a shunt motor is 0.08 Ω. When connected to 220 V supply, a counter EMF of 200 V is developed. Find (i) the armature current, (ii) the armature current when the armature is not rotating, and (iii) counter EMF when the armature current is 9.0 A.

**Solution:**

**Given Data:**
*   Applied terminal voltage, $V = 220 \text{ V}$
*   Armature resistance, $R_a = 0.08 \, \Omega$
*   Initial counter EMF, $E_{b1} = 200 \text{ V}$

**(i) Find the armature current:**
Using the voltage equation of a DC motor: $V = E_{b1} + I_{a1} R_a$.
Rearranging for armature current $I_{a1}$:
$$I_{a1} = \frac{V - E_{b1}}{R_a}$$
$$I_{a1} = \frac{220 - 200}{0.08} = \frac{20}{0.08} = 250 \text{ A}$$
**Answer (i): The armature current is 250 A.**

**(ii) Find the armature current when the armature is not rotating:**
When the armature is stationary (e.g., at the exact moment of starting), the rotational speed $N = 0$. Since back EMF is directly proportional to speed ($E_b \propto N$), the counter EMF is zero ($E_b = 0 \text{ V}$).
$$I_{a(start)} = \frac{V - 0}{R_a} = \frac{220}{0.08} = 2750 \text{ A}$$
**Answer (ii): The starting armature current is 2750 A.**

**(iii) Find the counter EMF when the armature current is 9.0 A:**
Let the new armature current be $I_{a2} = 9.0 \text{ A}$.
Using the voltage equation $V = E_{b2} + I_{a2} R_a$ and rearranging for $E_{b2}$:
$$E_{b2} = V - I_{a2} R_a$$
$$E_{b2} = 220 - (9.0 \times 0.08)$$
$$E_{b2} = 220 - 0.72 = 219.28 \text{ V}$$
**Answer (iii): The counter EMF is 219.28 V.**

* **Reference in Mam Slide:** 222
* **Reference in Firoz Note:** 81
* **Figure Involved:** None

---

### 9. Page 14, Q.4(a): What is meant by back emf? Prove that the gross power developed by a dc motor is maximum when the back emf (Eb) is equal to half of the applied voltage (V).

**Solution:**

**What is meant by Back EMF:**
When a DC motor is supplied with electrical energy, its armature rotates inside a magnetic field. As the armature conductors move, they cut the magnetic flux lines. According to Faraday's Law of Electromagnetic Induction, an electromotive force (EMF) is induced within these rotating conductors. According to Lenz's law, the direction of this induced voltage acts in opposition to the applied terminal voltage that drives the motor. Because it pushes back against the supply, this induced voltage is called the **Back EMF** or **Counter EMF** ($E_b$).

**Proof for maximum power:**
The fundamental voltage equation of a DC motor is given by:
$$V = E_b + I_a R_a$$
Multiply the entire equation by the armature current $I_a$ to convert it into a power equation:
$$V I_a = E_b I_a + I_a^2 R_a$$
The term $E_b I_a$ represents the gross mechanical power ($P_m$) developed by the motor armature. Rearranging for $P_m$:
$$P_m = V I_a - I_a^2 R_a$$
To find the condition for maximum mechanical power, we take the derivative of $P_m$ with respect to $I_a$ and set it to zero:
$$\frac{dP_m}{dI_a} = V - 2 I_a R_a = 0$$
$$2 I_a R_a = V \implies I_a R_a = \frac{V}{2}$$
Substituting $I_a R_a = \frac{V}{2}$ back into the basic voltage equation:
$$V = E_b + \frac{V}{2}$$
$$E_b = V - \frac{V}{2} = \frac{V}{2}$$
Thus, it is proven that the gross mechanical power developed by a DC motor reaches its mathematical maximum when the back EMF ($E_b$) is exactly equal to half of the applied voltage ($V$). 

* **Reference in Mam Slide:** 220, 221, 225
* **Reference in Firoz Note:** 80, 81, 85, 86
* **Figure Involved:** None
Here are the detailed solutions for the next 4 questions from your syllabus list (Items 10, 12, 13, and 14).

*(Note: Item 11 in your list is just a section heading: "3. Types of DC motors", so I have skipped it and moved to the next actual question).*

### 10. Page 14, Q.4(d): The armature resistance of a shunt motor is 0.09Ω. When connected to a 230V supply a counter-emf of 222.8V is developed. Find the armature current, the armature current when the armature is not rotating and counter-emf when the armature current is 100A.

**Solution:**

**Given Data:**
*   Applied terminal voltage, $V = 230 \text{ V}$
*   Armature resistance, $R_a = 0.09 \, \Omega$
*   Initial counter-emf (back EMF), $E_{b1} = 222.8 \text{ V}$

**(i) Find the armature current:**
From the fundamental voltage equation of a DC motor ($V = E_b + I_a R_a$), we can calculate the initial armature current ($I_{a1}$):
$$I_{a1} = \frac{V - E_{b1}}{R_a}$$
$$I_{a1} = \frac{230 - 222.8}{0.09} = \frac{7.2}{0.09} = 80 \text{ A}$$
**Answer (i): The armature current is 80 A.**

**(ii) Find the armature current when the armature is not rotating:**
When the motor is stationary (at standstill), its speed $N = 0$. Since counter-emf is directly proportional to speed ($E_b \propto N$), the counter-emf is zero ($E_b = 0 \text{ V}$). 
$$I_{a(start)} = \frac{V - 0}{R_a} = \frac{230}{0.09} \approx 2555.56 \text{ A}$$
**Answer (ii): The armature current when not rotating is 2555.56 A.** *(This highlights why a starter is necessary for DC motors).*

**(iii) Find the counter-emf when the armature current is 100 A:**
Let the new armature current be $I_{a2} = 100 \text{ A}$. Using the voltage equation and solving for the new counter-emf ($E_{b2}$):
$$V = E_{b2} + I_{a2} R_a$$
$$E_{b2} = V - I_{a2} R_a$$
$$E_{b2} = 230 - (100 \times 0.09)$$
$$E_{b2} = 230 - 9.0 = 221 \text{ V}$$
**Answer (iii): The counter-emf is 221 V.**

* **Reference in Mam Slide:** 222, 267 (Starter necessity)
* **Reference in Firoz Note:** 81, 114
* **Figure Involved:** None

---

### 12. Page 4, Q.55: Write applications of all DC motors.

**Solution:**

Different types of DC motors have distinct torque-speed characteristics, making them suitable for different industrial applications. 

**1. DC Shunt Motor:**
*   **Characteristics:** It is considered a constant-speed motor because its speed drops only slightly from no-load to full-load. It has a medium starting torque.
*   **Applications:** Used where constant speed is required regardless of the load. Examples include:
    *   Lathe machines and machine tools.
    *   Centrifugal pumps and blowers.
    *   Fans, spinning, and weaving machines.

**2. DC Series Motor:**
*   **Characteristics:** It has a highly variable speed (inverse relationship with load) and develops an exceptionally high starting torque. It must never be started on no-load because it will accelerate to dangerously high speeds.
*   **Applications:** Used where huge starting torque is required and speed variations are acceptable. Examples include:
    *   Electric traction (trains, trams, and trolleybuses).
    *   Cranes, hoists, and elevators.
    *   Heavy-duty linked forklift trucks.

**3. DC Compound Motor:**
*   **Cumulative Compound Motor:** Combines the high starting torque of a series motor with the safe no-load speed limit of a shunt motor.
    *   *Applications:* Rolling mills, heavy shears, punches, presses, and heavy planers where sudden heavy loads are applied for a short duration.
*   **Differential Compound Motor:** Has a tendency to maintain a strictly constant speed or even slightly increasing speed with load. Due to instability issues, it is rarely used.
    *   *Applications:* Limited specialized applications where absolutely constant speed is required despite load fluctuations (though largely replaced by advanced closed-loop controlled drives today).

* **Reference in Mam Slide:** 8, 9, 235
* **Reference in Firoz Note:** 111, 112
* **Figure Involved:** None

---

### 13. Page 8, Q.8(b): Define universal motor. Differentiate universal motor from a dc series motor and also mention its applications.

**Solution:**

**Definition of Universal Motor:**
A universal motor is a special type of series-wound motor that is designed to operate on either a Direct Current (DC) supply or a single-phase Alternating Current (AC) supply at roughly the same speed and output. 

**Differentiation between Universal Motor and DC Series Motor:**
Although a universal motor is physically and electrically similar to a DC series motor, several design modifications are made to allow it to run efficiently on AC:
1.  **Lamination:** In a standard DC series motor, only the armature is usually laminated. In a universal motor, the entire magnetic circuit (stator core, poles, and armature) is fully laminated to minimize eddy current losses caused by the alternating flux.
2.  **Field Windings:** A universal motor has fewer turns in its series field winding compared to a standard DC series motor. This is done to reduce the inductive reactance drop when operating on AC, which helps maintain a higher power factor.
3.  **Armature Windings:** To compensate for the weaker magnetic field (due to fewer field turns), the universal motor has a greater number of armature conductors to maintain the required torque.
4.  **Compensating Windings:** Universal motors often include compensating windings to neutralize the high armature reaction and improve commutation under AC operation, which is not strictly necessary for smaller DC series motors.
5.  **Brushes:** High-resistance carbon brushes are used in universal motors to reduce sparking during AC operation.

**Applications of Universal Motor:**
Because they offer high speed (often exceeding 10,000 RPM) and high power-to-weight ratios, they are widely used in fractional horsepower applications, such as:
*   Portable power tools (drills, saws, grinders).
*   Domestic appliances (vacuum cleaners, blenders, food mixers, sewing machines).
*   Hair dryers and trimming machines.

* **Reference:** Standard Electrical Machines theory (This specific special machine topic is not directly detailed in the provided DC Machines/Transformers PDF slides, but relies on fundamental AC/DC machine differentiation).
* **Figure Involved:** None

---

### 14. Page 10, Q.8(c): What is stepper motor? What are its applications? Draw the truth table and corresponding applied voltage waveforms to make the stepper motor step 30^0. [Figure Involved]

**Solution:**

**Definition of Stepper Motor:**
A stepper motor (or step motor) is a brushless DC electric motor that divides a full rotation into a number of equal, discrete angular steps. Unlike continuous rotation motors, the motor's shaft rotates through a specific electrical angle (step angle) for each electrical pulse received by its control circuit. 

**Applications:**
Because it allows for precise open-loop position and speed control, it is highly utilized in:
*   CNC machines and 3D printers.
*   Robotics (actuator positioning).
*   Computer peripherals (hard disk drives, flatbed scanners, optical disc drives).
*   Medical equipment (syringe pumps, automated imaging).
*   Camera lenses (autofocus and zoom mechanisms).

**Truth Table and Waveforms for a $30^\circ$ Step:**
To achieve a step angle of exactly $30^\circ$, a common configuration is a **3-Phase Variable Reluctance (VR) Stepper Motor** with 6 stator teeth and 4 rotor teeth ($N_s = 6, N_r = 4$). 
Step Angle calculation: $\theta_s = \frac{360^\circ}{m \times N_r} = \frac{360^\circ}{3 \times 4} = 30^\circ$ per step.

Let the three phases of the stator be A, B, and C. By energizing the phases sequentially one at a time (Full-step 1-phase ON mode), the rotor aligns with the energized stator teeth, advancing exactly $30^\circ$ each time.

**Truth Table (1-Phase ON Sequence):**

| Step No. | Phase A | Phase B | Phase C | Rotor Angle ($\theta$) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1 (ON) | 0 (OFF) | 0 (OFF) | $0^\circ$ |
| 2 | 0 (OFF) | 1 (ON) | 0 (OFF) | $30^\circ$ |
| 3 | 0 (OFF) | 0 (OFF) | 1 (ON) | $60^\circ$ |
| 4 | 1 (ON) | 0 (OFF) | 0 (OFF) | $90^\circ$ |
*(The sequence A $\rightarrow$ B $\rightarrow$ C repeats)*

**[Figure Involved - Applied Voltage Waveforms]**
*Description of the waveform drawing to reproduce in the exam:*
1.  Draw three horizontal axes representing time (or steps) for Phase A, Phase B, and Phase C voltages ($V_A, V_B, V_C$).
2.  **Phase A Waveform:** Draw a square pulse (Logic HIGH/Voltage $V$) for the duration of Step 1. It remains at zero for Step 2 and Step 3.
3.  **Phase B Waveform:** Stays at zero for Step 1. Jumps to a square pulse (Logic HIGH/Voltage $V$) for the duration of Step 2. Goes back to zero for Step 3.
4.  **Phase C Waveform:** Stays at zero for Step 1 and Step 2. Jumps to a square pulse (Logic HIGH/Voltage $V$) for the duration of Step 3.
5.  This staggered, non-overlapping sequence represents the applied voltage commands that pull the rotor $30^\circ$ forward per pulse.

* **Reference:** Standard Electrical Machines theory (Special Machines chapter).
* **Figure Involved:** Yes, you must draw the 3-phase staggered square-wave timing diagram described above.


Here are the detailed step-by-step solutions for the next 4 questions (Items 16, 17, 18, and 19) from your syllabus list.

*(Note: Item 15 in your provided list is a section heading "4. Equivalent circuit of a DC motor", so I have skipped it and solved the next 4 actual questions).*

### 16. Page 9, Q.6(c): The following values were obtained from the test data of a motor: line voltage, 120 V; line current 30 A; motor speed 186 rad/s; armature resistance 0.25 Ω; field resistance 90 Ω. Determine (i) the field current (ii) armature current (iii) counter – emf (iv) developed kW.

**Solution:**

**Given Data:**
Since the motor has both an armature resistance and a field resistance connected to a line voltage, we treat this as a standard DC Shunt Motor.
*   Line voltage (Terminal voltage), $V_T = 120 \text{ V}$
*   Line current, $I_L = 30 \text{ A}$
*   Motor speed, $\omega_m = 186 \text{ rad/s}$
*   Armature resistance, $R_a = 0.25 \, \Omega$
*   Field resistance, $R_f = 90 \, \Omega$

**(i) Field Current ($I_f$):**
In a shunt motor, the field winding is connected in parallel with the supply.
$$I_f = \frac{V_T}{R_f}$$
$$I_f = \frac{120}{90} = 1.333 \text{ A}$$
**Answer (i): The field current is 1.333 A.**

**(ii) Armature Current ($I_a$):**
By Kirchhoff's Current Law, the total line current splits into the armature and field currents: $I_L = I_a + I_f$.
$$I_a = I_L - I_f$$
$$I_a = 30 - 1.333 = 28.667 \text{ A}$$
**Answer (ii): The armature current is 28.667 A.**

**(iii) Counter-EMF ($E_b$):**
Using the voltage equation for a DC motor: $V_T = E_b + I_a R_a$.
$$E_b = V_T - I_a R_a$$
$$E_b = 120 - (28.667 \times 0.25)$$
$$E_b = 120 - 7.16675 = 112.833 \text{ V}$$
**Answer (iii): The counter-emf is 112.833 V.**

**(iv) Developed Power ($P_{dev}$) in kW:**
The gross mechanical power developed by the armature is the product of the back EMF and the armature current.
$$P_{dev} = E_b \times I_a$$
$$P_{dev} = 112.833 \times 28.667 = 3234.6 \text{ W}$$
To convert to kW, divide by 1000:
$$P_{dev} = \frac{3234.6}{1000} = 3.235 \text{ kW}$$
**Answer (iv): The developed power is 3.235 kW.**

*   **Reference in Mam Slide:** 247 (Equivalent circuit and formulas)
*   **Reference in Firoz Note:** 202, 203
*   **Figure Involved:** None required (unless asked to draw the equivalent circuit).

---

### 17. Page 14, Q.3(c): The following information was obtained from the nameplate of a shunt motor: 5Hp, 240V DC, full-load current 20.4A, field resistance 202Ω. If the armature resistance is 0.71Ω, determine (i) power delivered to motor, (ii) power dissipated in shunt field, (iii) power dissipated in armature circuit, (iv) electrical power converted into mechanical power.

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 240 \text{ V}$
*   Full-load line current, $I_L = 20.4 \text{ A}$
*   Field resistance, $R_f = 202 \, \Omega$
*   Armature resistance, $R_a = 0.71 \, \Omega$

**(i) Power delivered to the motor (Input Power, $P_{in}$):**
The total electrical power supplied to the motor is the product of the terminal voltage and the total line current.
$$P_{in} = V_T \times I_L$$
$$P_{in} = 240 \times 20.4 = 4896 \text{ W}$$
**Answer (i): The power delivered to the motor is 4896 W.**

**(ii) Power dissipated in the shunt field ($P_f$):**
First, find the field current:
$$I_f = \frac{V_T}{R_f} = \frac{240}{202} \approx 1.19 \text{ A}$$
The power dissipated as heat in the field winding (copper loss):
$$P_f = V_T \times I_f \quad \text{or} \quad P_f = I_f^2 R_f$$
$$P_f = 240 \times 1.19 = 285.6 \text{ W}$$
**Answer (ii): The power dissipated in the shunt field is 285.6 W.**

**(iii) Power dissipated in the armature circuit ($P_a$):**
First, find the armature current. For a shunt motor, $I_a = I_L - I_f$.
$$I_a = 20.4 - 1.19 = 19.21 \text{ A}$$
The power dissipated as heat in the armature winding (copper loss):
$$P_a = I_a^2 \times R_a$$
$$P_a = (19.21)^2 \times 0.71 = 369.02 \times 0.71 = 262 \text{ W}$$
**Answer (iii): The power dissipated in the armature circuit is 262 W.**

**(iv) Electrical power converted into mechanical power ($P_{dev}$):**
This is the gross mechanical power developed. It can be found by subtracting the copper losses from the input power (Power flow method), or by using $E_b \times I_a$. 
*Method 1 (Subtraction):*
$$P_{dev} = P_{in} - P_f - P_a$$
$$P_{dev} = 4896 - 285.6 - 262 = 4348.4 \text{ W}$$
*Method 2 (Using Back EMF):*
$$E_b = V_T - I_a R_a = 240 - (19.21 \times 0.71) = 240 - 13.64 = 226.36 \text{ V}$$
$$P_{dev} = E_b \times I_a = 226.36 \times 19.21 = 4348.4 \text{ W}$$
**Answer (iv): The electrical power converted into mechanical power is 4348.4 W (or 4.35 kW).**

*   **Reference in Mam Slide:** 224 (Example 8.5), 247
*   **Reference in Firoz Note:** 83, 84, 85 (Matches Example 8.5)
*   **Figure Involved:** None.

---

### 18. Page 14, Q.3(d): A 25kW, 250V dc shunt generator has armature and field resistances of 0.08Ω and 110Ω respectively. Determine the total armature power developed when working (i) as a generator delivering 25kW output and (ii) as a motor taking 25kW input.

**Solution:**

**Given Data:**
*   Machine voltage rating, $V_T = 250 \text{ V}$
*   Armature resistance, $R_a = 0.08 \, \Omega$
*   Field resistance, $R_f = 110 \, \Omega$
*   Field Current, $I_f = \frac{V_T}{R_f} = \frac{250}{110} = 2.27 \text{ A}$ (This remains the same for both cases as the terminal voltage is 250V).

**(i) Working as a Generator delivering 25kW output:**
*   Output Power, $P_{out} = 25 \text{ kW} = 25000 \text{ W}$
*   Line current delivered to the load, $I_L = \frac{P_{out}}{V_T} = \frac{25000}{250} = 100 \text{ A}$
*   In a generator, the armature supplies *both* the load current and the field current. 
    $$I_a = I_L + I_f = 100 + 2.27 = 102.27 \text{ A}$$
*   Generated EMF ($E_g$) equation for a generator:
    $$E_g = V_T + I_a R_a$$
    $$E_g = 250 + (102.27 \times 0.08) = 250 + 8.18 = 258.18 \text{ V}$$
*   Total power developed in the armature ($P_{dev}$):
    $$P_{dev} = E_g \times I_a$$
    $$P_{dev} = 258.18 \times 102.27 = 26404 \text{ W} = 26.4 \text{ kW}$$
**Answer (i): The total armature power developed as a generator is 26.4 kW.**

**(ii) Working as a Motor taking 25kW input:**
*   Input Power, $P_{in} = 25 \text{ kW} = 25000 \text{ W}$
*   Line current drawn from the supply, $I_L = \frac{P_{in}}{V_T} = \frac{25000}{250} = 100 \text{ A}$
*   In a motor, the total line current splits into the armature and the field.
    $$I_a = I_L - I_f = 100 - 2.27 = 97.73 \text{ A}$$
*   Back EMF ($E_b$) equation for a motor:
    $$E_b = V_T - I_a R_a$$
    $$E_b = 250 - (97.73 \times 0.08) = 250 - 7.82 = 242.18 \text{ V}$$
*   Total gross mechanical power developed in the armature ($P_{dev}$):
    $$P_{dev} = E_b \times I_a$$
    $$P_{dev} = 242.18 \times 97.73 = 23668 \text{ W} = 23.67 \text{ kW}$$
**Answer (ii): The total armature power developed as a motor is 23.67 kW.**

*   **Reference in Mam Slide:** 129 (Generator eq), 247 (Motor eq)
*   **Reference in Firoz Note:** 28, 29, 98, 99
*   **Figure Involved:** None.

---

### 19. Page 15, Q.3(c): A 220 V, dc shunt motor having an armature resistance of 0.2 Ω, and a field resistance of 110 Ω takes 4 A of line current while running at 1200 rpm on no load. On load, the input to the motor is 15 kW; calculate the speed and the developed torque.

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 220 \text{ V}$
*   Armature resistance, $R_a = 0.2 \, \Omega$
*   Field resistance, $R_f = 110 \, \Omega$
*   Field current, $I_f = \frac{V_T}{R_f} = \frac{220}{110} = 2 \text{ A}$

**Step 1: Analyze the No-Load Condition:**
*   No-load line current, $I_{L0} = 4 \text{ A}$
*   No-load speed, $N_0 = 1200 \text{ rpm}$
*   No-load armature current, $I_{a0} = I_{L0} - I_f = 4 - 2 = 2 \text{ A}$
*   No-load Back EMF, $E_{b0}$:
    $$E_{b0} = V_T - I_{a0} R_a$$
    $$E_{b0} = 220 - (2 \times 0.2) = 220 - 0.4 = 219.6 \text{ V}$$

**Step 2: Analyze the On-Load Condition:**
*   Power input on load, $P_{in} = 15 \text{ kW} = 15000 \text{ W}$
*   Loaded line current, $I_{L1} = \frac{P_{in}}{V_T} = \frac{15000}{220} = 68.18 \text{ A}$
*   Loaded armature current, $I_{a1} = I_{L1} - I_f = 68.18 - 2 = 66.18 \text{ A}$
*   Loaded Back EMF, $E_{b1}$:
    $$E_{b1} = V_T - I_{a1} R_a$$
    $$E_{b1} = 220 - (66.18 \times 0.2) = 220 - 13.236 = 206.764 \text{ V}$$

**Step 3: Calculate the New Speed ($N_1$):**
For a shunt motor, the flux ($\Phi$) remains constant since $I_f$ is constant (ignoring armature reaction). The back EMF is directly proportional to speed ($E_b \propto N$).
$$\frac{E_{b1}}{E_{b0}} = \frac{N_1}{N_0}$$
$$N_1 = N_0 \times \frac{E_{b1}}{E_{b0}}$$
$$N_1 = 1200 \times \frac{206.764}{219.6} = 1129.85 \text{ rpm}$$

**Step 4: Calculate the Developed Torque ($T_d$):**
*   Mechanical power developed, $P_{dev} = E_{b1} \times I_{a1}$
    $$P_{dev} = 206.764 \times 66.18 = 13683.4 \text{ W}$$
*   Angular velocity, $\omega = \frac{2 \pi N_1}{60}$
    $$\omega = \frac{2 \pi \times 1129.85}{60} = 118.318 \text{ rad/s}$$
*   Developed Torque, $T_d = \frac{P_{dev}}{\omega}$
    $$T_d = \frac{13683.4}{118.318} = 115.65 \text{ N-m}$$

**Answer: The loaded speed is 1129.85 rpm, and the developed torque is 115.65 N-m.**

*   **Reference in Mam Slide:** 249, 250 (Motor equations and torque-speed relationships)
*   **Reference in Firoz Note:** 204, 205 (Exact matched problem)
*   **Figure Involved:** None.
Here are the detailed step-by-step solutions for the next 4 questions (Items 20, 22, 23, and 24) from your syllabus list. 

*(Note: Item 21 is a section heading: "5. Torque of DC motor", so it is skipped to answer the actual questions).*

### 20. Page 25, CT-03 Q.2: The following values were obtained from the test data of a motor: line voltage 125V, line current 39A, motor speed, 186 rad/s, armature resistance, 0.25Ω, field resistance, 90Ω. Determine (a) the field current, (b) armature current, (c) counter-emf, (d) developed kW, (e) developed torque.

**Solution:**

**Given Data:**
*   Line/Terminal voltage, $V_T = 125 \text{ V}$
*   Line current, $I_L = 39 \text{ A}$
*   Motor speed, $\omega_m = 186 \text{ rad/s}$
*   Armature resistance, $R_a = 0.25 \, \Omega$
*   Field resistance, $R_f = 90 \, \Omega$

*(Since both field and armature resistances are given parallel to the supply, we treat this as a standard DC Shunt Motor).*

**(a) The field current ($I_f$):**
For a shunt motor, the field winding is connected directly across the supply line.
$$I_f = \frac{V_T}{R_f} = \frac{125}{90} \approx 1.389 \text{ A}$$
**Answer (a): The field current is 1.389 A.**

**(b) The armature current ($I_a$):**
By Kirchhoff's Current Law, the total line current is the sum of the armature and field currents ($I_L = I_a + I_f$).
$$I_a = I_L - I_f = 39 - 1.389 = 37.611 \text{ A}$$
**Answer (b): The armature current is 37.611 A.**

**(c) The counter-emf ($E_b$):**
Using the voltage equation of the DC motor: $V_T = E_b + I_a R_a$.
$$E_b = V_T - I_a R_a$$
$$E_b = 125 - (37.611 \times 0.25) = 125 - 9.403 = 115.597 \text{ V}$$
**Answer (c): The counter-emf is 115.597 V.**

**(d) The developed power in kW ($P_{dev}$):**
The gross mechanical power developed by the motor is the product of back EMF and armature current.
$$P_{dev} = E_b \times I_a$$
$$P_{dev} = 115.597 \times 37.611 = 4347.7 \text{ W}$$
To convert to kilowatts (kW):
$$P_{dev} = \frac{4347.7}{1000} \approx 4.348 \text{ kW}$$
**Answer (d): The developed power is 4.348 kW.**

**(e) The developed torque ($T_{dev}$):**
The relationship between developed power, torque, and angular speed is $P_{dev} = T_{dev} \times \omega_m$.
$$T_{dev} = \frac{P_{dev}}{\omega_m} = \frac{4347.7}{186} \approx 23.37 \text{ N-m}$$
**Answer (e): The developed torque is 23.37 N-m.**

*   **Reference in Mam Slide:** 247 (Formulas for DC Shunt Motor)
*   **Reference in Firoz Note:** 202, 203 (Similar math problem)

---

### 22. Page 4, Q.53: Derive the expression of induced torque for a real motor.

**Solution:**

**Derivation of Induced Torque:**
1. **Force on a single conductor:**
   When a current-carrying conductor of length $L$ is placed in a magnetic field of flux density $B$, the force $F$ exerted on it is given by:
   $$F = B \cdot I_c \cdot L$$
   Where $I_c$ is the current flowing through that specific individual conductor. If the motor has $A$ parallel paths and a total armature current of $I_a$, the current per conductor is $I_c = \frac{I_a}{A}$.
   So, $F = B \cdot \left(\frac{I_a}{A}\right) \cdot L$

2. **Torque on a single conductor:**
   Torque ($t_c$) is the product of force and the radial distance ($r$) from the center of rotation.
   $$t_c = F \cdot r = B \cdot \left(\frac{I_a}{A}\right) \cdot L \cdot r$$

3. **Total torque for all conductors:**
   If the armature has a total of $Z$ conductors, the total induced gross torque ($T_{ind}$) is the sum of the torques of all $Z$ conductors:
   $$T_{ind} = Z \cdot t_c = Z \cdot B \cdot \left(\frac{I_a}{A}\right) \cdot L \cdot r$$

4. **Expressing in terms of Magnetic Flux ($\Phi$):**
   The total magnetic flux produced by $P$ poles is $P \cdot \Phi$.
   The surface area of the cylindrical armature is $2 \pi r L$.
   The average magnetic flux density $B$ over the surface of the armature is:
   $$B = \frac{\text{Total Flux}}{\text{Area}} = \frac{P \Phi}{2 \pi r L}$$

5. **Final Substitution:**
   Substitute the expression for $B$ back into the total torque equation:
   $$T_{ind} = Z \cdot \left( \frac{P \Phi}{2 \pi r L} \right) \cdot \left(\frac{I_a}{A}\right) \cdot L \cdot r$$
   Notice that $L$ and $r$ cancel out:
   $$T_{ind} = \frac{P \cdot Z \cdot \Phi \cdot I_a}{2 \pi A}$$
   
   Since $P$ (number of poles), $Z$ (total conductors), and $A$ (parallel paths), and $2\pi$ are physical constants for a given manufactured machine, they can be combined into a single machine constant $K$:
   $$K = \frac{P Z}{2 \pi A}$$
   **Final Expression:**
   $$T_{ind} = K \Phi I_a$$

*   **Reference in Mam Slide:** 218, 219, 240
*   **Reference in Firoz Note:** 109, 110

---

### 23. Page 10, Q.7(d): A 400V, 25 hp, 450 rpm dc shunt motor is braked by plugging when running on full load. Determine the braking resistance necessary if the maximum braking current is not to exceed twice the full load current. Determine also the maximum braking torque when the motor is just reaching zero speed. The efficiency of the motor is 74.6% and the armature resistance is 0.2 Ω.

**Solution:**

**Given Data:**
*   Terminal voltage, $V = 400 \text{ V}$
*   Output power, $P_{out} = 25 \text{ hp} = 25 \times 746 \text{ W} = 18650 \text{ W}$
*   Speed, $N = 450 \text{ rpm}$
*   Efficiency, $\eta = 74.6\% = 0.746$
*   Armature resistance, $R_a = 0.2 \, \Omega$

**Step 1: Calculate Full-Load Current and Initial Back EMF**
1.  **Input Power:** $P_{in} = \frac{P_{out}}{\eta} = \frac{18650}{0.746} = 25000 \text{ W}$
2.  **Full Load Current ($I_{FL}$):** Assuming shunt field current is negligible (or treating $I_L \approx I_a$ as per standard convention for this problem class):
    $$I_a = \frac{P_{in}}{V} = \frac{25000}{400} = 62.5 \text{ A}$$
3.  **Initial Back EMF ($E_b$) before braking:**
    $$E_b = V - I_a R_a = 400 - (62.5 \times 0.2) = 400 - 12.5 = 387.5 \text{ V}$$

**Step 2: Determine the Braking Resistance ($R_b$) for Plugging**
In "plugging" (reverse current braking), the armature terminals are reversed. The applied voltage $V$ and the back EMF $E_b$ now act in the *same* direction, severely increasing the current.
1.  **Maximum Allowable Braking Current ($I_{b(max)}$):**
    $$I_{b(max)} = 2 \times I_{FL} = 2 \times 62.5 = 125 \text{ A}$$
2.  **Total Circuit Resistance Required ($R_{total}$):**
    $$I_{b(max)} = \frac{V + E_b}{R_{total}}$$
    $$R_{total} = \frac{400 + 387.5}{125} = \frac{787.5}{125} = 6.3 \, \Omega$$
3.  **External Braking Resistance ($R_b$):**
    $$R_b = R_{total} - R_a = 6.3 - 0.2 = 6.1 \, \Omega$$
    **Answer (i): The required braking resistance is $6.1 \, \Omega$.**

**Step 3: Determine Maximum Braking Torque at Zero Speed**
1.  **Calculate Initial Gross Torque ($T_g$):**
    Angular speed, $\omega = \frac{2 \pi N}{60} = \frac{2 \pi \times 450}{60} = 47.124 \text{ rad/s}$
    Gross Power, $P_{dev} = E_b \times I_a = 387.5 \times 62.5 = 24218.75 \text{ W}$
    Full Load Gross Torque, $T_g = \frac{P_{dev}}{\omega} = \frac{24218.75}{47.124} = 513.9 \text{ N-m}$
2.  **Current at Zero Speed ($I_{b0}$):**
    When the motor just reaches zero speed, it has stopped rotating, so $E_b = 0 \text{ V}$.
    $$I_{b0} = \frac{V + 0}{R_{total}} = \frac{400}{6.3} = 63.49 \text{ A}$$
3.  **Torque at Zero Speed ($T_{b0}$):**
    Since torque is directly proportional to armature current ($T \propto I_a$) in a constant-flux shunt motor:
    $$\frac{T_{b0}}{T_g} = \frac{I_{b0}}{I_a}$$
    $$T_{b0} = 513.9 \times \left(\frac{63.49}{62.5}\right) = 522 \text{ N-m}$$
    **Answer (ii): The maximum braking torque when reaching zero speed is 522 N-m.**

*   **Reference in Mam Slide:** 295, 296 (Plugging theory)
*   **Reference in Firoz Note:** 209, 210 (Exact matched problem)

---

### 24. Page 14, Q.3(b): Draw the load versus induced torque characteristic of different dc motors. [Figure Involved]

**Solution:**

In DC motor analysis, the "load" is generally represented by the Armature Current ($I_a$). Therefore, the "load versus induced torque" characteristic is mathematically the **Torque vs. Armature Current ($T_a$ vs. $I_a$)** curve. To provide a complete comparative answer, it is standard to plot the four main DC motors (Series, Shunt, Cumulative Compound, and Differential Compound) on the same graph.

**Explanation of the Characteristics:**
1.  **Shunt Motor:** Torque is strictly proportional to armature current ($T \propto \Phi I_a$). Because the flux $\Phi$ is essentially constant, the curve is a straight line passing through the origin.
2.  **Series Motor:** At light loads (before magnetic saturation), the flux $\Phi$ is directly proportional to $I_a$. Therefore, Torque $T \propto I_a^2$. The curve starts as a parabola. After saturation, $\Phi$ becomes constant, and the curve becomes a straight line.
3.  **Cumulative Compound Motor:** The series field assists the shunt field. As load ($I_a$) increases, the total flux increases. Thus, its torque rises faster than a shunt motor but slower than a series motor. The curve lies between the shunt and series curves.
4.  **Differential Compound Motor:** The series field opposes the shunt field. As load ($I_a$) increases, the net flux decreases. Therefore, the torque increases at a much slower rate than a shunt motor. 

**[Figure Involved - Torque vs. Armature Current (Load) Curves]**
*(Instruction for drawing the graph in the exam):*
*   **X-axis:** Armature Current ($I_a$) representing the Load.
*   **Y-axis:** Induced Torque ($T$).
*   Draw a straight diagonal line starting from the origin; label this **"Shunt"**.
*   Draw a parabolic curve starting from the origin that swoops upwards sharply, crossing the Shunt line; label this **"Series"**.
*   Draw a curve that sits exactly between the Series parabola and the Shunt straight line; label this **"Cumulative Compound"**.
*   Draw a line starting from the origin that droops below the Shunt straight line; label this **"Differential Compound"**.

*(Note: Sometimes "Load vs Torque" is alternatively interpreted as "Speed vs Torque". If you have time in the exam, drawing the Speed vs Torque curve—where Series drops exponentially, Shunt is relatively flat, Cumulative drops steadily, and Differential rises dangerously—is highly recommended as a supplementary figure).*

*   **Reference in Mam Slide:** 242 (Definition), 259 (Figure 8.14)
*   **Reference in Firoz Note:** 111 (Torque vs current graph), 112 (Combined graphs)
Here are the detailed step-by-step solutions for the next 4 questions (Items 25, 26, 28, and 29) from your syllabus list. 

*(Note: Item 27 is a section heading: "6. Characteristics of a DC shunt motor", so I have skipped it and solved the next 4 actual questions).*

### 25. Page 15, Q.4(c): A 230 V, 10 hp, dc shunt motor delivers power to a load at 1200 r/min. The armature current drawn by the motor is 200 A. The armature circuit resistance of the motor is 0.2 Ω and the field resistance is 115 Ω. If the rotational losses are 500 W, what is the value of load torque?

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 230 \text{ V}$
*   Motor speed, $N = 1200 \text{ r/min (rpm)}$
*   Armature current, $I_a = 200 \text{ A}$
*   Armature resistance, $R_a = 0.2 \, \Omega$
*   Field resistance, $R_f = 115 \, \Omega$ *(Note: Because $I_a$ is directly given, we do not need $R_f$ to find $I_a$, but it is useful if we needed the input line current).*
*   Rotational losses, $P_{rot} = 500 \text{ W}$

**Step 1: Calculate the Angular Speed ($\omega_m$)**
$$\omega_m = \frac{2 \pi N}{60} = \frac{2 \pi \times 1200}{60} = 40\pi \approx 125.66 \text{ rad/s}$$

**Step 2: Calculate the Back EMF ($E_b$)**
Using the voltage equation for a DC motor:
$$E_b = V_T - I_a R_a$$
$$E_b = 230 - (200 \times 0.2) = 230 - 40 = 190 \text{ V}$$

**Step 3: Calculate Gross Mechanical Power Developed ($P_{dev}$)**
The power developed in the armature before mechanical losses is:
$$P_{dev} = E_b \times I_a$$
$$P_{dev} = 190 \times 200 = 38,000 \text{ W}$$

**Step 4: Calculate the Net Output Power ($P_{out}$)**
The actual power delivered to the load is the gross developed power minus the rotational (mechanical + iron) losses:
$$P_{out} = P_{dev} - P_{rot}$$
$$P_{out} = 38,000 - 500 = 37,500 \text{ W}$$
*(Note: The 10 hp rating is the nominal label rating, but the motor is currently delivering 37.5 kW based on the given 200A current condition).*

**Step 5: Calculate the Load Torque ($\tau_{load}$)**
The load torque (or shaft torque) is the output power divided by the angular speed:
$$\tau_{load} = \frac{P_{out}}{\omega_m}$$
$$\tau_{load} = \frac{37,500}{125.66} \approx 298.4 \text{ N-m}$$

**Answer: The value of the load torque is 298.4 N-m.**

*   **Reference in Mam Slide:** 222 (Voltage equation), 223 (Power distribution)
*   **Reference in Firoz Note:** 82 (Power flow), 83 (Torque and power equations)
*   **Figure Involved:** None

---

### 26. Page 16, Q.4(c): A dc series motor takes 40 A at 220 V and runs at 1000 rpm. If the armature and the field resistance are 0.2 Ω and 0.1 Ω respectively and the iron and friction losses are 500 W, find the torque developed in the armature. What will be the output of the motor?

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 220 \text{ V}$
*   Line current, $I_L = 40 \text{ A}$ (For a series motor, Line Current = Armature Current = Series Field Current, so $I_a = 40 \text{ A}$)
*   Motor speed, $N = 1000 \text{ rpm}$
*   Armature resistance, $R_a = 0.2 \, \Omega$
*   Series field resistance, $R_{se} = 0.1 \, \Omega$
*   Rotational losses (iron + friction), $P_{rot} = 500 \text{ W}$

**Step 1: Calculate the Angular Speed ($\omega_m$)**
$$\omega_m = \frac{2 \pi N}{60} = \frac{2 \pi \times 1000}{60} = \frac{2000\pi}{60} \approx 104.72 \text{ rad/s}$$

**Step 2: Calculate the Back EMF ($E_b$)**
For a series motor, the voltage drop occurs across both the armature and the series field resistors:
$$E_b = V_T - I_a (R_a + R_{se})$$
$$E_b = 220 - 40 \times (0.2 + 0.1)$$
$$E_b = 220 - 40 \times 0.3 = 220 - 12 = 208 \text{ V}$$

**Step 3: Calculate the Gross Mechanical Power Developed ($P_{dev}$)**
$$P_{dev} = E_b \times I_a$$
$$P_{dev} = 208 \times 40 = 8320 \text{ W}$$

**Step 4: Find the Torque Developed in the Armature ($\tau_{dev}$)**
The developed torque (also called induced or gross torque) corresponds to the power developed before taking losses into account:
$$\tau_{dev} = \frac{P_{dev}}{\omega_m}$$
$$\tau_{dev} = \frac{8320}{104.72} \approx 79.45 \text{ N-m}$$
**Answer 1: The torque developed in the armature is 79.45 N-m.**

**Step 5: Find the Output of the Motor ($P_{out}$)**
The net output power delivered to the shaft is the developed power minus the rotational losses:
$$P_{out} = P_{dev} - P_{rot}$$
$$P_{out} = 8320 - 500 = 7820 \text{ W}$$
**Answer 2: The output of the motor is 7820 W (or 7.82 kW).**

*   **Reference in Mam Slide:** 260 (Series motor equation), 204 (Power stages)
*   **Reference in Firoz Note:** 107 (Series motor circuit), 138, 139 (Power flow)
*   **Figure Involved:** None

---

### 28. Page 4, Q.58: Why the field circuit of dc motor should never be opened while power is applied to the motor?

**Solution:**

The field circuit of a DC motor is responsible for creating the main magnetic flux ($\Phi$). The relationship governing the speed ($N$) of a DC motor is given by the equation:
$$N \propto \frac{E_b}{\Phi} \implies N = \frac{V_T - I_a R_a}{K \Phi}$$

If the field circuit is accidentally or intentionally opened while power is still applied to the armature:
1.  **Flux collapse:** The field current ($I_f$) drops immediately to zero, causing the main magnetic flux ($\Phi$) to collapse to a very tiny residual value ($\Phi_{res}$).
2.  **Runaway Speed:** Because the speed $N$ is inversely proportional to the flux $\Phi$, as the flux becomes nearly zero, the motor's speed attempts to increase to an infinitely high value to generate the necessary back EMF to balance the supply voltage. 
3.  **Mechanical Destruction:** This dangerously high speed (known as a "runaway" condition) exerts massive centrifugal forces on the rotor. It can cause the armature windings to be physically ripped out of their slots and destroy the commutator, destroying the motor.
4.  **Excessive Current:** Concurrently, since the back EMF ($E_b$) temporarily drops to almost zero, the armature current $I_a = (V_T - E_b)/R_a$ becomes dangerously high, which can melt the armature windings or blow the protective fuses.

For these reasons, proper protective equipment (like no-field release coils or overload relays) is necessary to immediately cut the armature power if the field circuit breaks.

*   **Reference in Mam Slide:** 227
*   **Reference in Firoz Note:** 90, 91
*   **Figure Involved:** None

---

### 29. Page 5, Q.59: What will happen if the field of a dc shunt motor is disconnected on running condition?

**Solution:**

This question explores the exact same phenomenon as Q.58, but specifically in the context of a motor that is already running under load. The sequence of events is highly destructive:

1.  **Loss of Magnetic Field:** When the field circuit disconnects, the field current $I_f$ becomes zero. The magnetic flux drastically drops to only the residual magnetism ($\Phi_{res}$).
2.  **Sharp Drop in Counter-EMF:** The counter-EMF ($E_b$) is proportional to flux ($E_b = K\Phi\omega$). Because the flux vanishes almost instantly, the back EMF crashes to nearly zero.
3.  **Massive Inrush of Armature Current:** With $E_b$ gone, there is no voltage opposing the supply voltage $V_T$. The armature current spikes to a short-circuit level: $I_a = \frac{V_T}{R_a}$. Since $R_a$ is very small, a devastatingly large current flows through the armature.
4.  **Torque Surge and Runaway Acceleration:** Initially, the massive spike in armature current outpaces the drop in flux, generating a huge transient torque ($T = K \Phi_{res} I_{a(huge)}$). This forces the motor to accelerate violently. As $N \propto \frac{V_T}{\Phi_{res}}$, the motor accelerates toward infinite speed.
5.  **Ultimate Failure:** One of two things will happen immediately:
    *   **Electrical Failure:** The massive armature current will blow the supply fuses, trip the circuit breakers, or burn out the armature windings.
    *   **Mechanical Failure:** If the circuit breakers fail to trip fast enough, the extreme centrifugal forces from the runaway speed will tear the armature apart, throwing windings out of the slots and shattering the commutator.

*   **Reference in Mam Slide:** 227
*   **Reference in Firoz Note:** 90, 91
*   **Figure Involved:** None
Here are the detailed solutions for the next 4 questions from your syllabus list (Items 30, 31, 33, and 34). 

*(Note: Item 32 in your list is a section heading: "7. Characteristics of a DC series motor", so I have skipped it and solved the actual questions).*

### 30. Page 5, Q.66: Explain the effects on speed, counter emf, armature current and torque of a dc shunt motor when load applied to that motor.

**Solution:**

When a mechanical load is applied to the shaft of a running DC shunt motor, a specific chain of automatic adjustments occurs due to the motor's self-regulating property (governor action of back EMF). Here is the step-by-step effect on each parameter:

1.  **Effect on Speed ($N$):** When the mechanical load increases, the load torque ($T_{load}$) temporarily becomes greater than the electromagnetic torque ($T_{ind}$) currently being generated by the motor. Because the opposing load is stronger, the motor begins to **slow down (speed decreases)**.
2.  **Effect on Counter EMF ($E_b$):** The counter EMF is directly proportional to the motor's speed ($E_b = K\Phi\omega$). In a shunt motor, the field flux ($\Phi$) is practically constant. Therefore, as the motor slows down, the rate at which armature conductors cut the magnetic flux decreases, causing the **counter EMF ($E_b$) to drop**.
3.  **Effect on Armature Current ($I_a$):** The armature current is determined by the equation $I_a = \frac{V_T - E_b}{R_a}$. Since the terminal supply voltage ($V_T$) and armature resistance ($R_a$) are constant, the drop in counter EMF ($E_b$) increases the net driving voltage ($V_T - E_b$). This forces a larger current through the armature. Thus, **armature current increases**.
4.  **Effect on Torque ($T_{ind}$):** The induced electromagnetic torque is directly proportional to the armature current ($T_{ind} = K\Phi I_a$). As the armature current rises, the **induced torque increases**. 

**Conclusion:** This cycle continues until the newly increased induced torque exactly matches the new mechanical load torque ($T_{ind} = T_{load}$). At this point of equilibrium, the motor stops decelerating and runs steadily at a slightly lower speed, drawing a higher armature current, generating a lower counter EMF, and producing a higher torque.

*   **Reference in Mam Slide:** 248, 251
*   **Reference in Firoz Note:** 96
*   **Figure Involved:** None required (A flow chart of this sequence is often drawn).

---

### 31. Page 14, Q.3(a): A dc shunt motor operating from a constant voltage supply is running steadily on no-load. Explain how the motor will adjust itself on application of load.

**Solution:**

*(Note: The underlying physics is the exact same as Q.66, but framed as an explanation of the motor's "adjustment" process).*

When a DC shunt motor runs steadily on no-load, it only draws a very small armature current—just enough to generate the slight torque needed to overcome internal friction and windage losses. Because the speed is high, the back EMF ($E_b$) is almost equal to the applied terminal voltage ($V_T$).

**Adjustment Mechanism upon Application of Load:**
1.  **Initial Imbalance:** The moment a mechanical load is applied to the motor shaft, the required mechanical torque suddenly exceeds the small electromagnetic torque currently being developed by the motor. 
2.  **Deceleration:** Due to this torque deficit, the rotor cannot sustain its no-load speed and begins to decelerate.
3.  **Back EMF Reduction:** Back EMF is essentially a generator effect inside the motor ($E_b \propto N$). As the speed ($N$) drops, the back EMF decreases.
4.  **Current Intake:** The motor armature circuit obeys Ohm's law: $I_a = \frac{V_T - E_b}{R_a}$. Because $E_b$ has decreased while $V_T$ is constant, the difference between them grows. This pushes a larger surge of current from the constant voltage supply into the armature.
5.  **Restoring Equilibrium:** The increased armature current creates a stronger magnetic interaction with the constant shunt field, causing the developed electromagnetic torque to rise ($T \propto I_a$). 
6.  **Steady State:** The torque continues to rise as speed falls until the developed torque exactly balances the new mechanical load torque. Once balanced, the motor stops slowing down and runs steadily at this new, slightly reduced speed. 

Through this automatic adjustment (dictated by the Back EMF), the shunt motor successfully pulls the exact electrical power needed from the supply to drive the newly applied mechanical load.

*   **Reference in Mam Slide:** 248, 251
*   **Reference in Firoz Note:** 96
*   **Figure Involved:** None

---

### 33. Page 5, Q.60: Explain why the series motor must be started with a mechanical load coupled to its armature.

**Solution:**

A DC series motor must never be started without a mechanical load because it will accelerate to a dangerously high speed, potentially destroying the machine. 

**Reasoning:**
1.  In a DC series motor, the field winding is connected in series with the armature. Therefore, the field current is the same as the armature current ($I_f = I_a$).
2.  The magnetic flux ($\Phi$) produced by the field poles is directly proportional to this current ($\Phi \propto I_a$, prior to magnetic saturation).
3.  The speed ($N$) of any DC motor is inversely proportional to the magnetic flux: 
    $$N \propto \frac{E_b}{\Phi} \propto \frac{V_T - I_a(R_a + R_{se})}{I_a}$$
4.  If the motor is started at **no-load**, the only torque it needs to generate is to overcome its own minor friction and windage. Consequently, it draws a very tiny armature current ($I_a \approx 0$).
5.  Because $I_a$ is extremely small, the series field flux ($\Phi$) is also extremely small. 
6.  Looking at the speed equation, dividing by an extremely small flux value causes the speed ($N$) to approach infinity. 

In reality, the motor will rapidly accelerate to a "runaway" speed. The immense centrifugal forces generated at this hyper-speed will physically tear the heavy copper windings out of the armature slots and shatter the commutator, destroying the motor. Therefore, a mechanical load must be coupled to the armature before starting to ensure the motor draws sufficient current, creating enough flux to keep the starting speed at a safe, controlled level.

*   **Reference in Mam Slide:** 262, 263
*   **Reference in Firoz Note:** 110, 111
*   **Figure Involved:** Speed vs. Armature Current curve for a Series Motor (showing speed approaching infinity as current approaches zero).

---

### 34. Page 5, Q.61: Why a dc series motor shaft should be firmly coupled with its load?

**Solution:**

This is a direct safety consequence of the extreme no-load characteristics of a DC series motor (as explained in Q.60). 

Even if you correctly start a series motor with a load attached, the *method* of attaching that load is critical. 
1.  If a series motor is connected to its load via a **belt drive**, there is a constant risk that the belt could snap, slip off the pulley, or break during operation.
2.  If the motor is connected via a weak or standard **friction clutch**, the clutch might accidentally disengage.
3.  If any of these failures occur while the motor is running, the motor is instantly disconnected from its load. It immediately enters a **no-load condition**.
4.  As soon as the load is removed, the armature current drops drastically. Since the field is in series with the armature, the magnetic flux also drops drastically.
5.  Because motor speed is inversely proportional to flux ($N \propto 1/\Phi$), the sudden loss of flux causes the motor to accelerate uncontrollably to infinite (runaway) speeds. The centrifugal forces will rip the motor apart, causing severe damage to the equipment and posing a lethal hazard to nearby operators.

**Conclusion:** 
To prevent accidental un-loading during operation, a DC series motor shaft must be **firmly and directly coupled** to its load using rigid mechanisms that cannot snap or slip, such as **gear drives** or **solid direct-shaft couplings** (as seen in trains, cranes, and hoists).

*   **Reference in Mam Slide:** 262, 263
*   **Reference in Firoz Note:** 110
*   **Figure Involved:** None required (Conceptual explanation).


Here are the detailed solutions for the next 4 questions from your syllabus list (Items 35, 36, 37, and 39). 

*(Note: Item 38 in your list is a section heading: "8. Characteristics of a DC compound motor / All DC Motors", so I have skipped it and provided the next actual question).*

### 35. Page 5, Q.62: “Series motors are never used unless they are directly connected to load”-why?

**Solution:**

A DC series motor has its field winding connected in series with the armature. This configuration leads to a unique and potentially dangerous speed characteristic at no-load.

**Reasoning:**
1. **The Speed Equation:** The speed of any DC motor is given by the relation:
   $$N \propto \frac{V_T - I_a(R_a + R_{se})}{\Phi}$$
2. **Flux Dependency:** Because the field is in series with the armature, the field current is equal to the armature current ($I_f = I_a$). Therefore, before magnetic saturation, the magnetic flux is directly proportional to the armature current ($\Phi \propto I_a$).
3. **No-Load Condition:** If a series motor is started without a load, or if the load is accidentally removed, the motor only needs to overcome its own minimal internal friction. Thus, it draws a very tiny armature current ($I_a \approx 0$).
4. **Runaway Speed:** Since $\Phi \propto I_a$, an extremely small armature current results in an extremely small magnetic flux. Looking at the speed equation, dividing the voltage by an almost zero flux causes the speed ($N$) to shoot toward infinity.
5. **Physical Danger:** The motor will accelerate uncontrollably to a "runaway" speed. The massive centrifugal forces generated at this speed will physically tear the heavy copper windings out of the armature slots and shatter the commutator, destroying the machine and endangering personnel.

**Why "Directly Connected":**
To prevent this catastrophic no-load condition, a series motor must **always** be started with a mechanical load. Furthermore, it cannot be connected to the load using belts or standard friction clutches, because if a belt breaks or a clutch slips during operation, the motor instantly becomes unloaded and runs away. Therefore, series motors are strictly "directly connected" to their loads using solid couplings or robust gear trains (like in train locomotives or cranes) where accidental detachment is impossible.

* **Reference in Mam Slide:** 262, 263
* **Reference in Firoz Note:** 110

---

### 36. Page 5, Q.63: Derive the terminal characteristics of a dc series motor. Explain with necessary figures, why these types of motors are suitable for starting high inertia load. [Figure Involved]

**Solution:**

The terminal characteristic of a motor is the relationship between its output torque ($\tau_{ind}$) and its speed ($\omega$).

**Derivation:**
1. The basic voltage equation for a series motor is:
   $$V_T = E_A + I_A(R_A + R_S)$$
2. The back EMF ($E_A$) can be expressed as:
   $$E_A = K\Phi\omega$$
3. In a series motor, flux is directly proportional to armature current (prior to saturation):
   $$\Phi = c I_A$$ (where $c$ is a constant of proportionality).
4. The induced torque is $\tau_{ind} = K\Phi I_A$. Substituting $\Phi = c I_A$:
   $$\tau_{ind} = K(c I_A)I_A = K c I_A^2$$
   Rearranging this to solve for $I_A$:
   $$I_A = \sqrt{\frac{\tau_{ind}}{Kc}}$$
5. Now, substitute $E_A = K(c I_A)\omega$ into the voltage equation:
   $$V_T = K c I_A \omega + I_A(R_A + R_S)$$
   Solve for speed ($\omega$):
   $$K c I_A \omega = V_T - I_A(R_A + R_S)$$
   $$\omega = \frac{V_T}{K c I_A} - \frac{R_A + R_S}{K c}$$
6. Finally, substitute the expression for $I_A$ derived in step 4 into this speed equation:
   $$\omega = \frac{V_T}{\sqrt{K c} \sqrt{\tau_{ind}}} - \frac{R_A + R_S}{K c}$$
   This is the final equation for the terminal characteristic of a DC series motor. It shows an inverse-square-root relationship between speed and torque.

**Why suitable for high inertia loads:**
High inertia loads (like trains or heavy cranes) require a massive initial starting torque to begin moving. 
In a shunt motor, torque is proportional to current ($T \propto I$). To get a huge starting torque, a shunt motor must draw a massive, potentially damaging current. 
However, in a series motor, torque is proportional to the *square* of the current ($T \propto I^2$). A moderate increase in starting current produces a massive, exponential surge in starting torque. Additionally, as the heavy load begins to accelerate and the required torque drops, the motor automatically and safely speeds up (as seen in the derived inverse equation). 

**[Figure Involved - Torque-Speed Characteristic of Series DC Motor]**
*Description of the graph for the exam:*
*   **X-axis:** Induced Torque ($\tau_{ind}$).
*   **Y-axis:** Speed ($\omega_m$).
*   Draw a steeply falling curve (resembling a hyperbola $y = 1/\sqrt{x}$). The curve drops rapidly from a very high speed at near-zero torque and gradually levels out to a low speed at high torque. Label a dashed line marking "No-load speed goes to infinity".

* **Reference in Mam Slide:** 260, 262
* **Reference in Firoz Note:** 108, 111

---

### 37. Page 15, Q.4(a): What are the principle characteristics of a dc series motor? What are its uses?

**Solution:**

**Principle Characteristics:**
The performance of a DC series motor is defined by three fundamental characteristic curves:
1. **Torque vs. Armature Current ($T_a$ vs $I_a$) / Electrical Characteristic:**
   Since flux ($\Phi$) is proportional to $I_a$ before saturation, the torque equation $T_a \propto \Phi I_a$ becomes $T_a \propto I_a^2$. The characteristic is a parabola initially, meaning torque increases quadratically with current. After magnetic saturation, $\Phi$ becomes constant, and torque increases linearly ($T_a \propto I_a$). 
2. **Speed vs. Armature Current ($N$ vs $I_a$):**
   Speed is inversely proportional to flux ($N \propto 1/\Phi$). Since $\Phi \propto I_a$, speed is inversely proportional to current ($N \propto 1/I_a$). This creates a hyperbolic curve. At light loads (low $I_a$), the speed becomes dangerously high. At heavy loads, the speed drops significantly.
3. **Speed vs. Torque ($N$ vs $T_a$) / Mechanical Characteristic:**
   Derived from the above two, this curve shows a steep drooping nature. When high torque is demanded, the motor speed is very low. When torque demand is low, the speed is exceptionally high. 

**Uses of a DC Series Motor:**
Because of its extraordinarily high starting torque and variable speed nature (where it automatically slows down for heavy loads and speeds up for light loads), the DC series motor is specifically used in heavy-duty applications:
*   **Electric Traction:** Railway locomotives, trams, and trolleybuses.
*   **Lifting Equipment:** Cranes, heavy hoists, and elevators.
*   **Industrial machinery:** Large conveyors and winches.

* **Reference in Mam Slide:** 264
* **Reference in Firoz Note:** 109, 110

---

### 39. Page 5, Q.64: Explain briefly speed versus armature current and torque versus armature current characteristics of all dc motors.

**Solution:**

This question requires comparing the performance of Shunt, Series, Cumulative Compound, and Differential Compound motors on two main graphs.

**1. Speed versus Armature Current ($N$ vs $I_a$) Characteristics:**
The fundamental governing equation is $N \propto \frac{V_T - I_a R_a}{\Phi}$.
*   **Shunt Motor:** The flux ($\Phi$) is constant. As load ($I_a$) increases, the only change is a slight increase in the $I_a R_a$ voltage drop. Therefore, the speed drops only very slightly. It is considered a constant-speed motor.
*   **Series Motor:** The flux ($\Phi$) is directly proportional to $I_a$. As load increases, the denominator ($\Phi$) increases significantly, causing the speed to drop sharply. At near-zero $I_a$, the speed approaches infinity (hyperbolic curve).
*   **Cumulative Compound Motor:** The series field assists the shunt field. As $I_a$ increases, the total flux ($\Phi$) increases. This causes the speed to drop more than a shunt motor, but it has a definitive no-load speed limit unlike a series motor.
*   **Differential Compound Motor:** The series field opposes the shunt field. As $I_a$ increases, the total flux ($\Phi$) decreases. This decreasing denominator causes the speed to actually *increase* with load. This leads to instability, which is why this motor is rarely used.

**2. Torque versus Armature Current ($T$ vs $I_a$) Characteristics:**
The fundamental governing equation is $T \propto \Phi I_a$.
*   **Shunt Motor:** Because $\Phi$ is constant, torque is strictly proportional to $I_a$ ($T \propto I_a$). The graph is a straight diagonal line passing through the origin.
*   **Series Motor:** Because $\Phi \propto I_a$, torque is proportional to the square of the current ($T \propto I_a^2$). The graph is an upward-curving parabola (until magnetic saturation is reached, after which it becomes linear).
*   **Cumulative Compound Motor:** Because flux increases as load increases, torque rises faster than a straight line. The curve sits between the shunt (straight line) and series (parabola) curves.
*   **Differential Compound Motor:** Because flux decreases as load increases, the torque does not increase proportionally with current. Its curve droops below the straight line of the shunt motor.
Here are the detailed solutions for the next 4 questions from your syllabus list (Items 40, 41, 42, and 44). 

*(Note: Item 43 in your list is a section heading: "9. Speed of a DC machine", so I have skipped it to solve the actual questions).*

### 40. Page 5, Q.65: Draw and explain the mechanical characteristics of DC series and shunt motor. [Figure Involved]

**Solution:**

The **mechanical characteristic** of a DC motor refers specifically to the relationship between its **Speed ($N$) and Induced Torque ($T$)**. It is derived from the electrical characteristics and the fundamental speed equation.

**1. DC Shunt Motor Mechanical Characteristic:**
*   **Equation:** The speed equation is $N = \frac{V - I_a R_a}{K\Phi}$. Since $T = K\Phi I_a$, we can substitute $I_a = \frac{T}{K\Phi}$. This gives:
    $$N = \frac{V}{K\Phi} - \frac{R_a}{(K\Phi)^2}T$$
*   **Explanation:** In a shunt motor, the terminal voltage ($V$) and field flux ($\Phi$) are practically constant. The equation above takes the form of a straight line ($y = c - mx$). At no-load ($T=0$), the speed is maximum. As the mechanical torque load increases, the speed drops linearly but very slightly (due to the small value of $R_a$). Therefore, the shunt motor is considered a constant-speed motor.

**2. DC Series Motor Mechanical Characteristic:**
*   **Equation:** For a series motor, flux is proportional to current ($\Phi = c I_a$) before saturation. From $T = K\Phi I_a$, we get $T = Kc I_a^2$, meaning $I_a \propto \sqrt{T}$. Substituting this into the speed equation $N \propto \frac{V}{\Phi}$:
    $$N \approx \frac{V}{K_2 \sqrt{T}}$$
*   **Explanation:** The speed is inversely proportional to the square root of the torque. When the torque is very small (no-load), the speed approaches infinity, which is why a series motor must never run without a load. As the torque load increases, the speed drops rapidly in a hyperbolic curve, eventually leveling out.

**[Figure Involved - Mechanical Characteristics]**
*(Instruction for drawing the graph in the exam):*
*   **X-axis:** Torque ($T$).
*   **Y-axis:** Speed ($N$).
*   **Shunt Curve:** Draw a nearly horizontal, straight line starting high on the Y-axis and drooping very slightly as it moves right.
*   **Series Curve:** Draw a steep, sweeping curve (hyperbola) that drops from very high up on the Y-axis (asymptotically) and flattens out as torque increases on the X-axis.

*   **Reference in Mam Slide:** 242 (Definition), 250 (Shunt curve), 262 (Series curve)
*   **Reference in Firoz Note:** 103 (Shunt $N$ vs $T_a$), 111 (Series $N$ vs $T_a$), 112 (Combined graphs)

---

### 41. Page 9, Q.6(a): Draw and explain the torque and speed characteristic of shunt motor, cumulative compound motor and differential compound motor. [Figure Involved]

**Solution:**

This question asks for the **Speed vs. Torque characteristic** (often called the torque-speed characteristic) specifically for Shunt, Cumulative Compound, and Differential Compound motors.

**Explanation of the Characteristics:**
1.  **Shunt Motor:** As derived in the previous question, the field flux ($\Phi$) is independent of the load. As torque increases, the speed drops only very slightly due to the armature resistance voltage drop ($I_a R_a$). It acts as the "baseline" constant-speed reference.
2.  **Cumulative Compound Motor:** In this motor, the series field winding is connected such that its flux *adds* to the shunt field flux ($\Phi_{total} = \Phi_{shunt} + \Phi_{series}$). As the mechanical torque load increases, the motor draws more current, which increases the series field flux. Since speed is inversely proportional to total flux ($N \propto 1/\Phi_{total}$), the increasing flux causes the speed to drop much more significantly than in a purely shunt motor. It effectively combines the safe no-load speed of a shunt motor with the heavy-load lugging power of a series motor.
3.  **Differential Compound Motor:** Here, the series field is connected to *oppose* the shunt field ($\Phi_{total} = \Phi_{shunt} - \Phi_{series}$). As torque and current increase, the opposing series flux reduces the total net flux. Because the denominator in the speed equation ($N \propto 1/\Phi_{total}$) gets smaller, the motor speed actually *increases* as the load increases. This creates a highly unstable, "runaway" condition under load, making differential compound motors unsuitable for almost any practical application.

**[Figure Involved - Torque and Speed Characteristics]**
*(Instruction for drawing the graph in the exam):*
*   **X-axis:** Torque ($T$).
*   **Y-axis:** Speed ($N$).
*   Start all three curves from the exact same point on the Y-axis (representing identical no-load speed).
*   **Shunt Curve:** Draw a slightly drooping straight line.
*   **Cumulative Compound Curve:** Draw a line that curves downwards, drooping significantly below the Shunt line.
*   **Differential Compound Curve:** Draw a curve that sweeps *upwards*, rising above the initial no-load speed.

*   **Reference in Mam Slide:** 255, 258, 266 (Comparing all motors)
*   **Reference in Firoz Note:** 112

---

### 42. Page 14, Q.3(a): Draw speed versus armature current and torque versus armature current characteristics of all DC motors. [Figure Involved]

**Solution:**

This requires outlining the electrical characteristics (Torque vs $I_a$ and Speed vs $I_a$) for all four major DC motor types: Shunt, Series, Cumulative Compound, and Differential Compound.

**1. Speed versus Armature Current ($N$ vs $I_a$):**
*   **Shunt:** Flux is constant. Speed drops very slightly due to $I_a R_a$ drop. (Straight, slightly declining line).
*   **Series:** Flux $\Phi \propto I_a$. Thus $N \propto 1/I_a$. It drops sharply in a hyperbolic curve and is dangerously high at $I_a \approx 0$.
*   **Cumulative:** Series flux aids shunt flux. Total flux increases with $I_a$. Speed drops more than the shunt motor but does not go to infinity at no-load. (Curve dropping moderately between shunt and series).
*   **Differential:** Series flux opposes shunt flux. Total flux decreases as $I_a$ increases. The speed rises upward with load.

**2. Torque versus Armature Current ($T$ vs $I_a$):**
*   **Shunt:** $T \propto \Phi I_a$. Since $\Phi$ is constant, $T \propto I_a$. (A straight diagonal line through the origin).
*   **Series:** $\Phi \propto I_a$, so $T \propto I_a^2$. The torque rises exponentially as a parabola (until magnetic saturation).
*   **Cumulative:** The added series flux causes torque to rise faster than a straight line. (Curve rising upward, sitting between the shunt straight line and the series parabola).
*   **Differential:** The opposing series flux weakens the total field. The torque increases at a slower rate. (Curve drooping below the shunt straight line).

**[Figure Involved - Dual Characteristics]**
*(Instruction for drawing the graphs in the exam):*
*   **Graph 1 ($N$ vs $I_a$):** Y-axis = Speed, X-axis = Armature Current. Draw the Shunt (slight droop), Cumulative (moderate droop), Differential (rising curve), and Series (hyperbolic drop from the top axis).
*   **Graph 2 ($T$ vs $I_a$):** Y-axis = Torque, X-axis = Armature Current. Draw the Shunt (straight diagonal), Series (steep parabola), Cumulative (curve between shunt and series), and Differential (drooping below shunt).

*   **Reference in Mam Slide:** 264, 265, 266
*   **Reference in Firoz Note:** 111, 112

---

### 44. Page 8, Q.7(b): Define the base speed of a dc motor. Describe how motor speed can be decreased and increased from the base speed.

**Solution:**

**Definition of Base Speed:**
The **base speed** (or rated speed) of a DC motor is defined as the speed at which the motor runs when full rated voltage is applied to its armature, and full rated current/voltage is applied to its field winding (with no external resistances added to either circuit). It is the standard operating speed found on the motor's nameplate.

**How to Alter Motor Speed:**
The speed of a DC motor is governed by the equation:
$$N = \frac{V_T - I_a R_a}{K\Phi}$$
From this equation, we can control speed either by changing the applied armature voltage/resistance (numerator) or by changing the magnetic flux (denominator).

**1. Decreasing Speed Below Base Speed (Armature/Rheostatic Control):**
*   To run the motor slower than its base speed, we must decrease the numerator of the speed equation. 
*   This is achieved by inserting a variable external resistance (rheostat) in **series with the armature circuit**.
*   As the external resistance increases, the voltage drop across the armature circuit increases, which reduces the back EMF ($E_b$) and, consequently, lowers the motor's speed.
*   *Limitation:* This method is inefficient because a large amount of power ($I_a^2 R_{ext}$) is wasted as heat in the external resistor.

**2. Increasing Speed Above Base Speed (Field/Flux Control):**
*   To run the motor faster than its base speed, we must decrease the denominator ($\Phi$) of the speed equation.
*   This is achieved by inserting a variable external resistance in **series with the shunt field circuit**.
*   Increasing the field resistance reduces the field current ($I_f = V_T / R_{f(total)}$). A lower field current creates a weaker magnetic field flux ($\Phi$). 
*   Since speed is inversely proportional to flux ($N \propto 1/\Phi$), weakening the field causes the motor to accelerate to a speed higher than the base speed.
*   *Limitation:* The field cannot be weakened indefinitely; if the flux is reduced too much, the motor will lose torque capability and commutation problems (sparking) will occur.

*   **Reference in Mam Slide:** 280, 281, 282, 283
*   **Reference in Firoz Note:** 88, 89

Here are the detailed step-by-step solutions for the next 4 questions (Items 45, 47, 48, and 49) from your syllabus list. 

*(Note: Item 46 in your list is a section heading: "10. Speed control of DC motors (and Braking)", so I have skipped it to solve the actual questions).*

### 45. Page 9, Q.5(c): What is meant by negative speed regulation? Which motor exhibits negative speed regulation?

**Solution:**

**Definition of Negative Speed Regulation:**
Speed regulation is a measure of how much a motor's speed changes when the mechanical load is applied, compared to its full-load speed. The mathematical formula for percent speed regulation is:
$$ \% \text{ Speed Regulation} = \frac{N_{NL} - N_{FL}}{N_{FL}} \times 100\% $$
Where $N_{NL}$ is the No-Load speed and $N_{FL}$ is the Full-Load speed.
*   A **positive** speed regulation means the motor's speed drops when a load is applied ($N_{NL} > N_{FL}$). This is standard for most motors.
*   A **negative** speed regulation means the motor's speed actually **increases** when a mechanical load is applied ($N_{FL} > N_{NL}$). This results in a rising torque-speed characteristic. 

**Which Motor Exhibits Negative Speed Regulation:**
The **Differential Compound DC Motor** is the only standard DC motor that exhibits negative speed regulation. 

**Reasoning:**
In a differential compound motor, the series field winding is connected such that its magnetic flux opposes the flux generated by the shunt field ($\Phi_{total} = \Phi_{shunt} - \Phi_{series}$). 
When a mechanical load is added, the armature current ($I_a$) increases. This causes the opposing series field flux ($\Phi_{series}$) to strengthen, which in turn reduces the net magnetic flux ($\Phi_{total}$) in the motor. Since the speed of a DC motor is inversely proportional to the net flux ($N \propto \frac{1}{\Phi_{total}}$), this significant reduction in flux causes the motor's speed to dangerously accelerate as more load is applied. Because the loaded speed becomes higher than the no-load speed, the calculation yields a negative speed regulation.

*   **Reference in Mam Slide:** 234 (Definition of speed regulation), 258 (Differential motor characteristics)
*   **Reference in Firoz Note:** 93 (Positive and Negative regulation rules), 112 (Graph of characteristics)
*   **Figure Involved:** None required (but a Speed vs Load graph showing a rising curve can be drawn for clarity).

---

### 47. Page 5, Q.75: Name the different methods of electrical breaking of dc motors and explain.

**Solution:**

Electrical braking is used to bring a motor to a quick, smooth stop by using electromagnetic forces rather than mechanical friction pads. There are three primary methods of electrical braking for DC motors:

**1. Rheostatic or Dynamic Braking:**
*   **Mechanism:** The armature of the running motor is suddenly disconnected from the DC power supply and immediately connected across a variable external braking resistor ($R_b$). The field winding remains connected to the supply (in shunt motors).
*   **Explanation:** Due to inertia, the rotor continues to spin. With the field still active, the motor acts as a DC generator, driven by the kinetic energy of the rotating load. It generates a current that flows through the external resistor. The kinetic energy is rapidly dissipated as $I^2R$ heat in the resistor, generating an opposing electromagnetic torque that brings the motor to a smooth halt.

**2. Plugging (or Reverse Current Braking):**
*   **Mechanism:** While the motor is running, the connections to the armature terminals are intentionally reversed. 
*   **Explanation:** By reversing the armature, the applied terminal voltage ($V$) and the motor's existing Back EMF ($E_b$) no longer oppose each other; instead, they add together in the same direction ($V + E_b$). This creates an enormous reverse current in the armature, which produces an immediate and violent reverse torque, bringing the motor to a very sudden stop. Because the current would be dangerously high ($I_a = \frac{V + E_b}{R_a}$), a heavy external resistor must be inserted into the circuit during plugging to limit the current. The motor must be disconnected from the supply the exact moment it hits zero speed, otherwise, it will start spinning in reverse.

**3. Regenerative Braking:**
*   **Mechanism:** This occurs when the motor's load forces the rotor to spin faster than its rated no-load speed (for example, an electric train going down a steep hill, or a descending elevator cage).
*   **Explanation:** Under these "overhauling load" conditions, the physical speed increases so much that the Back EMF ($E_b$) becomes strictly greater than the supply voltage ($V$). Because $E_b > V$, the direction of the armature current reverses. The motor automatically turns into a generator and pumps electrical power *back into the supply grid*. This reverse power generation creates a strong braking torque that prevents the load from accelerating out of control, while simultaneously recovering energy.

*   **Reference in Mam Slide:** 293, 294 (Dynamic), 295 (Plugging), 297 (Regenerative)
*   **Reference in Firoz Note:** Not explicitly covered in the provided Firoz notes.
*   **Figure Involved:** Circuit diagrams showing the connections for Dynamic braking (armature across a resistor) and Plugging (reversed armature terminals with series resistor).

---

### 48. Page 5, Q.76: Explain the different methods used for the speed control of D.C. shunt motor.

**Solution:**

The speed of a DC shunt motor is governed by the equation:
$$N = \frac{V_T - I_a R_a}{K\Phi}$$
Based on this equation, there are three primary ways to control the speed:

**1. Flux Control Method (Field Control):**
*   **How it works:** A variable resistor (field rheostat) is inserted in **series with the shunt field winding**.
*   **Explanation:** By increasing the field resistance, the field current ($I_f$) decreases. A lower field current weakens the magnetic flux ($\Phi$). Since speed is inversely proportional to flux ($N \propto 1/\Phi$), decreasing the flux causes the motor speed to **increase**.
*   **Result:** This method is highly efficient (since field current is small, $I^2R$ power loss is minimal) and is strictly used to achieve speeds **above the base (rated) speed**.

**2. Armature Control Method (Rheostatic Control):**
*   **How it works:** A variable high-power resistor is inserted in **series with the armature circuit**.
*   **Explanation:** This external resistance increases the total voltage drop in the armature circuit. The net voltage reaching the armature ($V_T - I_a(R_a + R_{ext})$) is severely reduced. As a result, the motor slows down. 
*   **Result:** This method is used exclusively to achieve speeds **below the base (rated) speed**. It is inefficient because a massive amount of power is wasted as heat in the external armature resistor.

**3. Applied Voltage Control (Ward-Leonard System):**
*   **How it works:** Instead of using wasteful resistors, the main terminal voltage ($V_T$) supplied to the motor armature is directly varied using a separate dedicated motor-generator set (or modern solid-state thyristor rectifiers). 
*   **Explanation:** The field of the main motor is kept constant, but the voltage applied to its armature is smoothly increased or decreased. 
*   **Result:** This method provides exceptionally smooth, highly efficient, and precise speed control over a massive range, both **above and below the base speed**, as well as in both forward and reverse directions.

*   **Reference in Mam Slide:** 281, 282 (Flux & Armature Control), 286, 287 (Voltage / Ward-Leonard Control)
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** Circuit diagrams for (a) Field Control (rheostat on the field branch), (b) Armature Control (rheostat on the armature branch), and (c) Ward-Leonard system layout.

---

### 49. Page 5, Q.77: Why in a dc shunt motor speed adjustment below the rated one is not done using field current control and above the rated one is not done using armature voltage control?

**Solution:**

This constraint comes down to the physical and electrical limits of the motor's design and safety ratings.

**1. Why speed adjustment BELOW rated speed is NOT done using Field Current Control:**
*   To decrease the speed using field control, you would have to **increase** the magnetic flux ($\Phi$), because speed is inversely proportional to flux ($N \propto 1/\Phi$).
*   To increase the flux, you would have to force a **higher field current** ($I_f$) through the field windings than the motor was designed for.
*   **The Problem:** The field windings are already designed to operate at their maximum safe rated voltage and current when the motor is running at base speed. Attempting to force extra current through them would cause severe $I^2R$ overheating, burning out the field coils. Furthermore, the magnetic iron core reaches "saturation"; meaning pushing more current yields no extra flux anyway. Therefore, field control can only be safely used to *weaken* the field, making the motor go faster, never slower.

**2. Why speed adjustment ABOVE rated speed is NOT done using Armature Voltage Control:**
*   To increase the speed using armature voltage control, you would have to supply a terminal voltage ($V_T$) that is **greater** than the motor's rated nameplate voltage.
*   **The Problem:** Applying a voltage higher than the motor's design limits will break down the dielectric insulation of the motor windings, causing short circuits and catastrophic electrical failure. It would also force excessive current through the armature, causing overheating and massive commutator sparking. Therefore, armature control can only be safely used to apply *less* voltage than the rated limit, making the motor go slower, never faster.

*   **Reference in Mam Slide:** 282, 283 (Notes stating field is for above normal speed, armature is for below normal speed)
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** None


* **Reference in Mam Slide:** 259, 264
* **Reference in Firoz Note:** 111, 112


Here are the detailed step-by-step solutions for the next 4 questions (Items 50, 51, 52, and 53) from your syllabus list.

### 50. Page 5, Q.78: Explain why inserting a resistor in series with the armature of a dc motor causes a decrease in speed.

**Solution:**

The speed of a DC motor is fundamentally governed by the equation:
$$N = \frac{V_T - I_a R_a}{K \Phi}$$
Where:
*   $N$ = Motor speed
*   $V_T$ = Applied terminal voltage
*   $I_a$ = Armature current
*   $R_a$ = Inherent armature resistance
*   $\Phi$ = Magnetic flux per pole

**Explanation:**
1.  **Increased Voltage Drop:** When an external variable resistor ($R_{ext}$) is inserted in series with the armature circuit, the total resistance of the armature path becomes $(R_a + R_{ext})$. 
2.  **Reduction in Back EMF:** The voltage drop across the armature circuit increases from $(I_a R_a)$ to $I_a(R_a + R_{ext})$. According to the motor voltage equation, the Back EMF ($E_b$) must decrease to satisfy Kirchhoff's Voltage Law:
    $$E_b = V_T - I_a(R_a + R_{ext})$$
3.  **Speed Response:** Because Back EMF is directly proportional to speed ($E_b \propto N \Phi$) and the magnetic flux ($\Phi$) remains constant (in a shunt motor), the only way for the motor to physically reduce its Back EMF is to **slow down**.
4.  **Conclusion:** The insertion of the resistor chokes the actual voltage reaching the armature. Since the armature "sees" a lower operating voltage, it runs at a proportionally lower speed. The greater the external resistance added, the slower the motor will run.

*   **Reference in Mam Slide:** 283, 284, 285 (Armature / Rheostatic Control Method)
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** Circuit diagram showing a variable resistor in series with the armature.

---

### 51. Page 5, Q.79: What are the factors that control the speed of a dc motor? Explain Ward-Leonard system to control speed of a dc motor.

**Solution:**

**Factors controlling the speed of a DC motor:**
From the speed equation $N \propto \frac{V_T - I_a R_a}{\Phi}$, there are three main factors that can be adjusted to control the speed:
1.  **Terminal Voltage ($V_T$):** Varying the applied armature voltage (Voltage Control).
2.  **Magnetic Flux ($\Phi$):** Varying the field current to change the magnetic field strength (Field Control).
3.  **Armature Resistance ($R_a$):** Adding external resistance to the armature circuit (Rheostatic Control).

**Explanation of the Ward-Leonard System:**
The Ward-Leonard system is an extremely precise **Voltage Control** method used to achieve a vast and smooth range of speed control, in both directions (forward and reverse), without the massive energy waste associated with armature resistors.

**How it works:**
1.  **The Setup:** The system requires a dedicated Motor-Generator (M-G) set to drive the main DC motor. It consists of three machines:
    *   An **AC driving motor** (usually an induction motor) connected to the grid.
    *   A **DC Generator (G)**, which is mechanically driven by the AC motor.
    *   The **Main DC Motor (M)**, whose speed we want to control.
2.  **The Connection:** The armature of the DC Generator is electrically connected directly to the armature of the main DC Motor. The field windings of both the generator and the main motor are excited by an independent DC source.
3.  **Speed Control Operation:** The field of the main motor is kept constant. To control the speed, the operator adjusts the field current of the *DC generator* via a field regulator.
    *   If the generator's field current is increased, it generates a higher voltage. This higher voltage is fed directly to the main motor, making it run faster.
    *   If the generator's field current is decreased to zero, the motor stops smoothly.
    *   If the polarity of the generator's field current is reversed, the generator outputs a negative voltage, causing the main DC motor to instantly smoothly reverse its direction of rotation.

**Advantages:** Exceptionally smooth speed control from zero to maximum speed, highly efficient, and provides built-in regenerative braking.

*   **Reference in Mam Slide:** 280 (Factors), 287 (Ward-Leonard System)
*   **Reference in Firoz Note:** 88
*   **Figure Involved:** Block diagram of the Ward-Leonard system showing the AC Motor coupled to the DC Generator, which is electrically wired to the Main DC Motor.

---

### 52. Page 6, Q.80: Explain how the speed of dc motor can be controlled by using thyristor.

**Solution:**

Thyristor (Solid-State Electronic) speed control has largely replaced bulky mechanical systems like the Ward-Leonard system. It uses power electronics to efficiently regulate the voltage and current supplied to the DC motor.

**How Thyristor Control Works:**
1.  **Phase-Controlled Rectifiers:** In industrial settings, the available power is usually AC. Thyristors (also known as Silicon Controlled Rectifiers, or SCRs) are used to build a controlled bridge rectifier circuit. This circuit converts the incoming AC voltage into a pulsating DC voltage.
2.  **Firing Angle ($\alpha$) Adjustment:** A thyristor acts like a switch that only turns on when a small "trigger" pulse is sent to its gate terminal. By delaying the exact moment this pulse is fired during the AC sine wave (a delay known as the firing angle, $\alpha$), we can chop off parts of the AC wave. 
3.  **Varying the Average Voltage:** 
    *   If the thyristors are fired early (small firing angle, $\alpha \approx 0^\circ$), almost the entire AC wave is allowed through, producing a **high average DC voltage**. This makes the motor run at **high speed**.
    *   If the thyristors are fired late (large firing angle, $\alpha$ approaching $180^\circ$), only a tiny sliver of the wave is allowed through, resulting in a **low average DC voltage**. This makes the motor run at **low speed**.
4.  **Armature vs. Field Control:** 
    *   A primary thyristor bridge can be connected to the armature to provide voltage control (for speeds from zero up to base speed).
    *   A secondary, smaller thyristor bridge can be connected to the field winding to provide flux control (for speeds above base speed).

**Advantages:** High efficiency (no $I^2R$ resistor waste), compact size, no moving parts, and extremely fast, accurate digital response.

*   **Reference in Mam Slide:** 300, 302, 303, 304 (Electronic Speed Control)
*   **Reference in Firoz Note:** Not heavily detailed in handwritten notes, mostly in slides.
*   **Figure Involved:** Circuit diagram of a thyristor (SCR) bridge rectifier connected to a DC motor, and waveforms showing the "chopped" AC voltage output.

---

### 53. Page 10, Q.7(b): Distinguish between electric braking and mechanical breaking.

**Solution:**

Braking is the process of bringing a running motor to a stop. This can be done physically (mechanical) or electromagnetically (electrical). 

| Feature | Electric Braking | Mechanical Braking |
| :--- | :--- | :--- |
| **Basic Principle** | The motor acts as a generator, converting kinetic energy into electrical energy, producing an opposing electromagnetic torque. | Physical friction is applied to the rotating shaft via brake shoes or pads pressed against a brake drum/disc. |
| **Wear and Tear** | **None.** There is no physical contact or friction involved, hence no wear and tear on mechanical parts. | **High.** Friction pads wear out quickly over time and require frequent replacement and adjustment. |
| **Energy Dissipation** | Kinetic energy is dissipated as $I^2R$ heat in external electrical resistors, or returned efficiently to the supply grid (Regenerative braking). | Kinetic energy is dissipated entirely as heat and dust directly at the brake drum friction surface. |
| **Smoothness** | Braking is exceptionally smooth and jar-free, easily controlled by varying electrical resistance or voltage. | Braking can be sudden, jerky, and harsh, depending on the mechanical pressure applied. |
| **Holding Ability** | **Cannot hold the motor at a dead stop.** Once speed reaches zero, electrical braking torque ceases to exist. | **Excellent holding ability.** Essential for keeping a load stationary (e.g., an elevator parked at a floor) after it has stopped. |
| **Applications** | Used to rapidly and safely slow down heavy, high-speed loads (trains, heavy machinery). | Used for final stopping and securely holding the load in place. |

**Conclusion:** In modern industrial systems, both methods are used together. Electric braking is used to smoothly decelerate the massive load, reducing wear, and mechanical braking is applied at the very end to physically lock the rotor in place.

*   **Reference in Mam Slide:** 293 (Electric Braking introduction)
*   **Reference in Firoz Note:** N/A
*   **Figure Involved:** None required (Table format is best).

Here are the detailed step-by-step solutions for the next 4 questions (Items 54, 55, 56, and 57) from your syllabus list.

### 54. Page 14, Q.4(c): Explain the field weakening method used for the speed control of DC shunt motor.

**Solution:**

The **Field Weakening Method** (also known as the Flux Control Method) is a highly efficient technique used to increase the speed of a DC shunt motor above its rated (base) speed.

**1. Principle of Operation:**
The speed of a DC motor is governed by the equation:
$$N = \frac{V_T - I_a R_a}{K\Phi}$$
From this equation, it is clear that motor speed ($N$) is inversely proportional to the magnetic field flux ($\Phi$). 
To reduce (weaken) the flux, a variable resistor (field rheostat) is connected in **series** with the shunt field winding. By increasing the resistance of this rheostat, the field current ($I_f = V_T / R_{f(total)}$) decreases. A smaller field current creates a weaker magnetic flux. Because the flux in the denominator of the speed equation decreases, the speed of the motor increases.

**2. Key Characteristics:**
*   **Speeds Above Base Speed:** This method can only be used to achieve speeds higher than the normal full-field speed. You cannot increase flux beyond its rated saturation point to slow the motor down safely.
*   **Constant Power Drive:** As flux decreases, the motor's maximum torque-producing capability decreases ($T \propto \Phi I_a$). However, because speed increases proportionally, the overall mechanical power ($P = T \cdot \omega$) remains relatively constant.
*   **High Efficiency:** The shunt field current is very small (typically less than 5% of the total motor current). Therefore, the $I^2R$ power loss in the control rheostat is negligible, making this a highly efficient method.

**3. Limitations:**
If the field is weakened too much, the armature reaction becomes prominent, which distorts the weak main field and causes severe sparking at the commutator brushes. Furthermore, the motor loses significant torque, which may cause it to stall if driving a heavy load.

*   **Reference in Mam Slide:** 281, 282
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** A circuit diagram of a DC shunt motor with a variable resistor ($R_{ext}$) placed in the field branch.

---

### 55. Page 15, Q.4(b): Explain two common ways in which the speed of a dc shunt motor is controlled.

**Solution:**

The speed of a DC shunt motor is primarily dictated by the formula $N \propto \frac{V_T - I_a R_a}{\Phi}$. Based on this, the two most common ways to control its speed are:

**1. Flux Control Method (Field Weakening):**
*   **How it works:** A variable resistance (rheostat) is connected in series with the shunt field winding. Increasing this resistance decreases the field current ($I_f$), which in turn decreases the magnetic flux ($\Phi$). Since speed is inversely proportional to flux, the motor speed increases.
*   **Application:** Used specifically for obtaining speeds **above** the base/rated speed.
*   **Advantages:** It is highly efficient because the field circuit only carries a small fraction of the total current, meaning very little power is wasted as heat in the rheostat. It is compact and inexpensive.

**2. Armature Resistance Control Method (Rheostatic Control):**
*   **How it works:** A heavy-duty variable resistance is connected in series with the armature circuit. As this resistance is increased, the voltage drop across the armature circuit ($I_a R_{ext}$) increases, reducing the actual voltage available to the motor's armature to generate back EMF. 
*   **Application:** Used specifically for obtaining speeds **below** the base/rated speed.
*   **Disadvantages:** It is highly inefficient. Because the entire load-bearing armature current ($I_a$) must pass through this external resistor, a massive amount of power is wasted as $I_a^2 R$ heat. The speed also fluctuates heavily if the load changes. It is generally only used for short durations (like starting the motor or brief adjustments).

*   **Reference in Mam Slide:** 281, 282 (Flux Control), 283, 284 (Armature Control)
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** Two circuit diagrams: one showing a rheostat in the field branch, and another showing a rheostat in the armature branch.

---

### 56. Page 15, Q.4(c): A 250 V dc shunt motor has armature resistance of 0.2 Ω. It takes an armature current of 50 A while running with a load at 750 rpm. To change the speed of the motor, the main field flux is reduced by 10% by changing the motor shunt field resistance. What will be the new speed of the motor?

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 250 \text{ V}$
*   Armature resistance, $R_a = 0.2 \, \Omega$
*   Initial armature current, $I_{a1} = 50 \text{ A}$
*   Initial speed, $N_1 = 750 \text{ rpm}$
*   New flux, $\Phi_2 = \Phi_1 - 0.10\Phi_1 = 0.90\Phi_1$

*(Assumption: Unless otherwise stated, it is standard practice in such problems to assume the mechanical load torque remains constant).*

**Step 1: Determine initial Back EMF ($E_{b1}$)**
$$E_{b1} = V_T - I_{a1} R_a$$
$$E_{b1} = 250 - (50 \times 0.2) = 250 - 10 = 240 \text{ V}$$

**Step 2: Find the new armature current ($I_{a2}$)**
Since the load torque is assumed constant: $T_1 = T_2$
We know that Torque $T \propto \Phi I_a$, therefore:
$$\Phi_1 I_{a1} = \Phi_2 I_{a2}$$
Substituting $\Phi_2 = 0.9 \Phi_1$:
$$\Phi_1 \times 50 = 0.9 \Phi_1 \times I_{a2}$$
$$I_{a2} = \frac{50}{0.9} = 55.55 \text{ A}$$
*(Notice that as flux weakened, the armature current had to increase to maintain the same torque).*

**Step 3: Determine the new Back EMF ($E_{b2}$)**
$$E_{b2} = V_T - I_{a2} R_a$$
$$E_{b2} = 250 - (55.55 \times 0.2)$$
$$E_{b2} = 250 - 11.11 = 238.89 \text{ V}$$

**Step 4: Calculate the new speed ($N_2$)**
We use the speed proportionality relation: $N \propto \frac{E_b}{\Phi}$
$$\frac{N_2}{N_1} = \frac{E_{b2}}{E_{b1}} \times \frac{\Phi_1}{\Phi_2}$$
$$N_2 = N_1 \times \left(\frac{E_{b2}}{E_{b1}}\right) \times \left(\frac{\Phi_1}{0.9 \Phi_1}\right)$$
$$N_2 = 750 \times \left(\frac{238.89}{240}\right) \times \left(\frac{1}{0.9}\right)$$
$$N_2 = 750 \times 0.995375 \times 1.1111$$
$$N_2 = 829.48 \text{ rpm}$$

**Answer: The new speed of the motor will be 829.48 rpm.**

*   **Reference in Mam Slide:** 282 (Flux control theory)
*   **Reference in Firoz Note:** 86, 87 (Speed ratio mathematical relationship)
*   **Figure Involved:** None

---

### 57. Page 16, Q.4(b): When the Ward Leonard System of speed control is used, why should the shunt fields be connected to a separate supply source?

**Solution:**

The Ward-Leonard system controls the speed of the main DC motor by applying a highly variable voltage across its armature, from zero volts up to its maximum rated voltage. 

If the main motor were wired as a normal self-excited shunt motor, its field winding would be connected in parallel directly across its own armature. Under this arrangement, using the Ward-Leonard system would create severe operational problems:

1.  **Simultaneous Field Weakening:** As you decrease the voltage supplied to the motor's armature to slow it down, you would simultaneously be decreasing the voltage applied to its field winding. 
2.  **Opposing Effects on Speed:** A lower field voltage results in a smaller field current and weaker magnetic flux ($\Phi$). Since motor speed is inversely proportional to flux ($N \propto 1/\Phi$), a weaker flux naturally forces the motor to *speed up*. This directly fights your attempt to slow the motor down by lowering the armature voltage, making linear speed control impossible.
3.  **Loss of Torque Capability:** Torque is directly proportional to flux ($T \propto \Phi I_a$). If the field flux drops drastically because you lowered the supply voltage to run at a slow speed, the motor will lose its ability to generate turning force. It would likely stall under any significant load.

**Why Separate Excitation is Required:**
To achieve stable, smooth, and predictable speed control from zero to base speed, the motor's magnetic flux must remain at its full, absolute maximum strength at all times. Therefore, the shunt field must be disconnected from the variable armature supply and wired to an independent, **separate constant-voltage DC supply**. This ensures the motor maintains 100% of its torque-producing capability regardless of how low the armature voltage is dropped.

*   **Reference in Mam Slide:** 287 (Ward-Leonard System Diagram clearly showing separate excitation)
*   **Reference in Firoz Note:** N/A (Standard application theory)
*   **Figure Involved:** None required (but a schematic of a separately excited motor could be helpful).

Here are the detailed step-by-step solutions for the next 4 questions (Items 58, 59, 61, and 62) from your syllabus list.

*(Note: Item 60 in your list is a section heading: "11. Starting of DC motors", so I have skipped it to solve the actual questions).*

### 58. Page 28, Q.No.1: What are the merits and demerits of field control method for dc motor speed control?

**Solution:**

The field control method (also known as flux control) adjusts the speed of a DC motor by connecting a variable resistor (rheostat) in series with the shunt field winding to vary the magnetic flux ($\Phi$).

**Merits (Advantages):**
1.  **High Efficiency:** Because the shunt field current is very small (usually a fraction of the total motor current), the power wasted as heat in the control rheostat ($I_f^2 R$) is extremely small. Therefore, this method is highly economical and efficient.
2.  **Compact Equipment:** Since the rheostat only handles the small field current, it can be physically small, inexpensive, and very convenient to adjust.
3.  **Smooth Speed Control:** It provides a very smooth and precise variation of speed.
4.  **Constant Power Output:** As speed increases (due to field weakening), the torque proportionally decreases. This makes the field control method excellent for constant-power drive applications.

**Demerits (Disadvantages):**
1.  **Speeds Only Above Base Speed:** By adding resistance, you can only decrease the field current and weaken the flux. Since speed is inversely proportional to flux ($N \propto 1/\Phi$), this method can only be used to obtain speeds *above* the motor's normal rated (base) speed. It cannot be used to run the motor slower than its base speed.
2.  **Commutation Problems:** At very high speeds (when the field is significantly weakened), the main magnetic field becomes very weak. This allows the *armature reaction* to severely distort the main field, leading to unsatisfactory commutation and severe sparking at the brushes.
3.  **Decreased Torque:** The torque developed by the motor is directly proportional to the flux ($T \propto \Phi I_a$). A weakened field significantly reduces the torque-producing capability of the motor.

*   **Reference in Mam Slide:** 292 (Advantages of Field Control Method)
*   **Reference in Firoz Note:** 88, 89
*   **Figure Involved:** None

---

### 59. Page 28, Q.No.2: Prove that plugging provide more braking torque then dynamic braking.

**Solution:**

To prove this, we must compare the mathematical formulas for the braking torque generated by both methods. The electromagnetic torque ($T_B$) developed by a DC motor is given by:
$$T_B = \frac{1}{2\pi} \cdot \Phi \cdot Z \left(\frac{P}{A}\right) \cdot I_a$$
Where $I_a$ is the armature current during the braking process.

**1. Dynamic (Rheostatic) Braking:**
In dynamic braking, the armature is disconnected from the supply voltage ($V$) and connected across a braking resistor ($R$). The only voltage driving the armature current is the motor's own Back EMF ($E_b = \frac{\Phi Z N P}{60 A}$).
The braking current is:
$$I_a = \frac{E_b}{R + R_a} = \frac{k_1 \Phi N}{R + R_a}$$
Substituting this $I_a$ into the torque equation:
$$T_{dynamic} = \frac{1}{2\pi} \Phi Z \left(\frac{P}{A}\right) \cdot \left[ \frac{\Phi Z N (P/A)}{R + R_a} \right] = k_2 \Phi^2 N$$
*Observation:* Dynamic braking torque is strictly proportional to the speed ($N$). As the motor slows down, the braking torque decreases, reaching zero when the motor stops.

**2. Plugging (Reverse Current Braking):**
In plugging, the armature terminals are reversed while the motor is running. The supply voltage ($V$) and the Back EMF ($E_b$) now act in the *same* direction, adding up to drive the current.
The braking current is:
$$I_a = \frac{V + E_b}{R + R_a}$$
Substituting this $I_a$ into the torque equation:
$$T_{plugging} = \frac{1}{2\pi} \Phi Z \left(\frac{P}{A}\right) \cdot \left[ \frac{V + E_b}{R + R_a} \right]$$
Since $E_b \propto \Phi N$, we can break this into two parts:
$$T_{plugging} = \frac{1}{2\pi} \Phi Z \left(\frac{P}{A}\right) \left[ \frac{V}{R + R_a} \right] + \frac{1}{2\pi} \Phi Z \left(\frac{P}{A}\right) \left[ \frac{\Phi Z N (P/A)}{R + R_a} \right]$$
$$T_{plugging} = k_4 \Phi + k_5 \Phi^2 N$$

**Conclusion / Proof:**
Comparing the two torque equations:
*   $T_{dynamic} = k_2 \Phi^2 N$
*   $T_{plugging} = k_4 \Phi + T_{dynamic}$

The plugging torque equation contains an additional constant term ($k_4 \Phi$) that comes from the power drawn directly from the supply voltage ($V$). Because of this extra term, **Plugging always yields a strictly greater braking torque than dynamic braking.** Furthermore, even when the motor reaches zero speed ($N = 0$), plugging still exerts a braking torque equal to $k_4 \Phi$, whereas dynamic braking torque drops completely to zero.

*   **Reference in Mam Slide:** 294, 295, 296 (Plugging and Dynamic equations)
*   **Reference in Firoz Note:** Not explicitly detailed
*   **Figure Involved:** None required (but writing out the equations clearly is mandatory).

---

### 61. Page 4, Q.57: What will happen if a shunt motor is directly connected to the supply line?

**Solution:**

If a DC shunt motor is connected directly to the full supply voltage without using a starter, the consequences will be violently destructive due to the massive inrush of armature current.

**Explanation:**
1.  **Zero Initial Back EMF:** The armature current of a DC motor is determined by the formula: 
    $$I_a = \frac{V - E_b}{R_a}$$
    When the motor is at rest (stationary), its speed ($N$) is zero. Because Back EMF is directly proportional to speed ($E_b = K\Phi N$), the Back EMF at the moment of starting is completely zero ($E_b = 0$).
2.  **Short-Circuit Condition:** Since $E_b = 0$, the equation becomes simply $I_a = \frac{V}{R_a}$. The armature resistance ($R_a$) of a typical DC motor is exceptionally small (often between 0.1 $\Omega$ and 0.5 $\Omega$). 
3.  **Massive Current Spike:** If a standard supply voltage (e.g., 440 V) is applied across a very low resistance (e.g., 0.25 $\Omega$), the starting current will be astronomically high. 
    *Example:* $I_a = \frac{440}{0.25} = 1760 \text{ Amperes}$. This is often 20 to 35 times greater than the motor's safe full-load current rating.
4.  **Destructive Consequences:** 
    *   The massive current will produce extreme $I^2R$ heat, instantly melting the armature copper windings.
    *   It will cause severe sparking and flashover at the commutator, destroying the commutator segments and the carbon brushes.
    *   The enormous sudden magnetic force will create a mechanical shock (jerk) that could snap the motor shaft or destroy the coupled load.
    *   Before the motor is destroyed, it will likely blow the facility's fuses or trip the heavy-duty circuit breakers, shutting down the power line.

To prevent this, a starter (a temporary high-power external resistance) must be placed in series with the armature to choke the current until the motor spins up and generates enough natural Back EMF to defend itself.

*   **Reference in Mam Slide:** 267 (Necessity of a Starter)
*   **Reference in Firoz Note:** 103, 110, 114
*   **Figure Involved:** None

---

### 62. Page 14, Q.4(b): A dc motor fails to start when switched ON. What could be the best possible reasons and remedies?

**Solution:**

When a DC motor fails to start upon applying power, the issue usually falls into one of three categories: electrical supply faults, magnetic field faults, or severe mechanical overloads.

**Possible Reasons and Remedies:**

1.  **Reason: Open Armature Circuit or Blown Fuses.** 
    If the main supply line is disconnected, a fuse is blown, or the carbon brushes are worn out and not making contact with the commutator, no current can flow into the armature ($I_a = 0$). Without armature current, no torque is generated.
    *   **Remedy:** Check the main switch, replace blown fuses, reset circuit breakers. Inspect the carbon brushes and spring tension; replace brushes or clean the commutator if necessary.

2.  **Reason: Open Field Circuit.**
    If the field winding is broken or the field rheostat is disconnected, no field current flows. This means there is no magnetic flux ($\Phi = 0$). Since torque $T \propto \Phi I_a$, zero flux means zero starting torque, and the motor will hum but not spin.
    *   **Remedy:** Use a multimeter to check the continuity of the field winding and the field regulator. Reconnect broken wires or replace the damaged field coil.

3.  **Reason: Excessive Starter Resistance.**
    The starting resistor box might be jammed, or the resistance might be set improperly high. If the resistance is too large, it limits the armature current so much that the motor cannot generate enough torque to overcome static friction.
    *   **Remedy:** Inspect the starter box. Move the starter handle smoothly to cut out initial resistance until the motor turns, or repair open circuits inside the starter.

4.  **Reason: Excessive Mechanical Load or Locked Rotor.**
    The mechanical load coupled to the shaft might simply be too heavy for the motor's starting torque capabilities. Alternatively, the bearings might be jammed/seized, physically preventing the shaft from turning.
    *   **Remedy:** Decouple the mechanical load from the motor and try to turn the shaft by hand. If it is jammed, replace or lubricate the motor bearings. If it turns freely, the external load must be reduced before starting.

5.  **Reason: Low Supply Voltage.**
    The applied terminal voltage might be severely dropped due to a line fault, meaning it cannot push enough starting current through the machine.
    *   **Remedy:** Measure the terminal voltage wit
    * 
    * Here are the detailed step-by-step solutions for the next 4 questions (Items 64, 65, 66, and 67) from your syllabus list. 

*(Note: Item 63 is a section heading: "12. Three point and four point starter with its advantages and disadvantages", so I have skipped it to solve the actual questions).*

### 64. Page 5, Q.72: What are the purposes of starter used in a dc motor? Describe the working of the three-point starter for DC shunt motor with neat diagram. [Figure Involved]

**Solution:**

**Purposes of a Starter in a DC Motor:**
1.  **To Limit Excessive Starting Current:** At the moment of starting ($N = 0$), the back EMF ($E_b$) is zero. The armature current is only limited by the very small armature resistance ($I_a = V/R_a$). This causes a massive, destructive inrush of current. The primary purpose of the starter is to insert a high external resistance in series with the armature to limit this current to a safe value.
2.  **Overload Protection:** Starters contain an Overload Release (OLR) mechanism to protect the motor from drawing excessive current during continuous mechanical overloading.
3.  **No-Voltage/Under-Voltage Protection:** Starters contain a No-Volt Release (NVR) mechanism that disconnects the motor if the power supply fails, preventing the motor from restarting unexpectedly when power returns.

**Working of a Three-Point Starter:**
A 3-point starter connects to the motor circuit via three terminals: **L (Line)**, **F (Field)**, and **A (Armature)**.
*   **Construction:** It consists of a graded starting resistance divided into several studs. A spring-loaded metallic handle is used to sweep across these studs. The starter incorporates two electromagnets: the No-Volt Release (NVR) coil and the Overload Release (OLR) coil.
*   **Starting Operation:** 
    1. The operator turns on the main supply and pushes the handle against the spring tension to **Stud 1**.
    2. At Stud 1, the *entire* starting resistance is connected in series with the armature, safely limiting the starting current. Simultaneously, the field winding is connected directly to the full supply voltage through the brass arc and NVR coil, providing maximum starting flux.
    3. As the motor accelerates, it builds up back EMF ($E_b$). The operator manually sweeps the handle across the subsequent studs (2, 3, 4...), gradually cutting the resistance out of the armature circuit as the motor reaches full speed.
*   **Holding Operation:** At the final "RUN" position, all starting resistance is removed from the armature. The handle is physically held in the "RUN" position by the magnetic pull of the **NVR coil**, which is wired in series with the shunt field.
*   **Protective Operation:**
    *   *No-Volt Protection:* If the power supply fails or the field circuit breaks, the NVR coil loses its magnetism. The spring instantly pulls the handle back to the "OFF" position, safely disconnecting the motor.
    *   *Overload Protection:* If the motor draws too much current, the **OLR coil** (wired in series with the line) becomes highly magnetized. It pulls a small metal lever that short-circuits the NVR coil. This kills the NVR's magnetism, causing the spring to snap the handle back to "OFF".

**[Figure Involved - Three-Point Starter Diagram]**
*(Instruction for drawing):*
*   Draw the DC supply connected to terminal **L**.
*   Route **L** through the OLR coil to the pivot of the movable Handle.
*   Draw a series of resistor coils connected between contact studs.
*   The last stud connects to terminal **A** (which goes to the motor armature).
*   The Handle has a soft iron piece. When at the "RUN" position, it touches an electromagnet (NVR coil).
*   The NVR coil connects the first stud to terminal **F** (which goes to the motor shunt field).
*   Show a small lever below the NVR coil that can short-circuit it, operated by the magnetic pull of the OLR coil.

*   **Reference in Mam Slide:** 268 (Purposes), 270 (3-point diagram)
*   **Reference in Firoz Note:** 114, 115

---

### 65. Page 5, Q.73: Which characteristics of three-point starter make it unpopular? How those problems can be resolved using four-point starter?

**Solution:**

**Why the Three-Point Starter is Unpopular:**
The main drawback of the 3-point starter arises when it is used with motors that require **speed control above base speed** using the field weakening method.
1.  In a 3-point starter, the No-Volt Release (NVR) electromagnet coil is wired in **series** with the motor's shunt field circuit.
2.  To increase the motor's speed, an external rheostat is used to add resistance to the field circuit, which decreases the field current ($I_f$).
3.  Because the NVR coil is in the same series loop, the current flowing through the NVR coil also decreases drastically.
4.  If the speed is increased too much, the magnetic pull of the NVR coil becomes weaker than the tension of the handle's return spring.
5.  Consequently, the handle will unexpectedly snap back to the "OFF" position, shutting down the motor during normal operation. This "unwanted tripping" makes the 3-point starter unsuitable for variable-speed applications.

**Resolution Using a Four-Point Starter:**
The 4-point starter solves this problem by mechanically and electrically isolating the NVR coil from the field circuit.
1.  **Structural Change:** A 4th terminal (usually labeled $N$ or $L_2$) is added. The NVR coil is removed from the field circuit series loop.
2.  **Parallel Circuit:** Instead, the NVR coil is connected in parallel with the field and armature, directly across the main supply lines, usually in series with its own fixed current-limiting protective resistor.
3.  **How it Resolves the Issue:** Because the NVR coil is now on an independent parallel branch, changing the field resistance to control the motor's speed no longer has any effect on the current flowing through the NVR coil. 
4.  The NVR coil maintains a constant, strong magnetic pull regardless of how much the field is weakened, ensuring the handle stays securely in the "RUN" position at all operational speeds.

*   **Reference in Mam Slide:** 271 (Why 3-point is unpopular), 272 (4-point diagram)
*   **Reference in Firoz Note:** 115 (Drawbacks of 3-point), 116, 117 (Four-point starter)

---

### 66. Page 5, Q.74: Name Different types of starters.

**Solution:**

Based on the construction, control mechanisms, and the specific types of DC motors they operate, the different types of starters are:

1.  **Three-Point Starter:** Used manually for DC shunt and compound motors (best for constant-speed applications).
2.  **Four-Point Starter:** Used manually for DC shunt and compound motors (specifically designed for variable-speed applications requiring field control).
3.  **Series Motor Starter (Two-Point Starter):** Used specifically for DC series motors. They generally feature a No-Load release or No-Voltage release mechanism.
4.  **Definite-Time Starter:** An automatic starter that cuts out starting resistance in fixed, pre-set time intervals using timers, regardless of the motor's actual speed.
5.  **Counter-EMF Starter:** An automatic starter where magnetic contactors monitor the motor's rising Back EMF and automatically cut out steps of resistance as the $E_b$ reaches specific voltage thresholds.
6.  **Across-The-Line Starter:** A simple contactor system used to connect very small fractional-horsepower DC motors directly to the supply line without starting resistors, as their internal resistance is high enough, and inertia low enough, to prevent damage.

*   **Reference in Mam Slide:** 270, 272, 273, 274, 275, 276
*   **Reference in Firoz Note:** 114, 116, 120, 122, 123, 124

---

### 67. Page 8, Q.7(a): Explain how a 3-point starter can be used to start a DC motor with low speed but high starting torque

**Solution:**

To understand how a 3-point starter achieves this specific mechanical starting condition, we must look at the fundamental formulas for torque and speed:
*   **Torque Equation:** $T \propto \Phi \cdot I_a$
*   **Speed Equation:** $N \propto \frac{V_{terminal} - I_a R_{total}}{\Phi}$

When the handle of a 3-point starter is moved to the very first "ON" position (Stud 1), the electrical circuitry forces the motor into a state that naturally yields high torque and low speed:

1.  **High Starting Torque Generation:**
    *   To get maximum torque, we need maximum magnetic flux ($\Phi$). 
    *   In a 3-point starter, the moment the handle touches Stud 1, the shunt field winding is connected directly to the full supply voltage (via the brass arc and the NVR coil). This ensures the field current ($I_f$) is at its absolute maximum, generating **maximum magnetic flux ($\Phi$)**.
    *   Simultaneously, the starting resistance is sized to allow a safely large armature current ($I_a$) to flow (typically 1.5 to 2 times the full-load rated current).
    *   Because both $\Phi$ (maximum) and $I_a$ (high) are maximized, their product ($T \propto \Phi \cdot I_a$) generates an extraordinarily **high starting torque**, allowing the motor to easily overcome heavy mechanical inertia.

2.  **Low Starting Speed Maintenance:**
    *   While the motor generates heavy torque, it must not instantly accelerate to dangerous speeds.
    *   At Stud 1, the *entire* series of heavy starting resistors ($R_{start}$) is placed in series with the armature.
    *   The effective voltage actually reaching the armature is drastically reduced due to the massive voltage drop across these resistors: $V_{armature} = V_T - I_a R_{start}$.
    *   Looking at the speed equation, the numerator ($V_{terminal} - I_a R_{total}$) is very small, while the denominator ($\Phi$) is at its maximum value. 
    *   A small numerator divided by a large denominator results in a very **low speed ($N$)**.

Therefore, the circuit architecture of the 3-point starter at the initial switch-on mathematically forces the machine to produce high starting torque while physically constraining the rotational speed to a slow, manageable crawl until the operator sweeps the handle further.

*   **Reference in Mam Slide:** 270 (3-point starter operation)
*   **Reference in Firoz Note:** 114 (Operation analysis)
* 
* h a voltmeter and correct the power supply issue at the source.

*   **Reference in Mam Slide:** General motor torque theory ($T \propto \Phi I_a$) and starter principles (Slides 267, 268)
*   **Reference in Firoz Note:** General DC machine principles.
*   **Figure Involved:** None
Here are the detailed step-by-step solutions for the next 4 questions (Items 64, 65, 66, and 67) from your syllabus list. 

*(Note: Item 63 is a section heading: "12. Three point and four point starter with its advantages and disadvantages", so I have skipped it to solve the actual questions).*

### 64. Page 5, Q.72: What are the purposes of starter used in a dc motor? Describe the working of the three-point starter for DC shunt motor with neat diagram. [Figure Involved]

**Solution:**

**Purposes of a Starter in a DC Motor:**
1.  **To Limit Excessive Starting Current:** At the moment of starting ($N = 0$), the back EMF ($E_b$) is zero. The armature current is only limited by the very small armature resistance ($I_a = V/R_a$). This causes a massive, destructive inrush of current. The primary purpose of the starter is to insert a high external resistance in series with the armature to limit this current to a safe value.
2.  **Overload Protection:** Starters contain an Overload Release (OLR) mechanism to protect the motor from drawing excessive current during continuous mechanical overloading.
3.  **No-Voltage/Under-Voltage Protection:** Starters contain a No-Volt Release (NVR) mechanism that disconnects the motor if the power supply fails, preventing the motor from restarting unexpectedly when power returns.

**Working of a Three-Point Starter:**
A 3-point starter connects to the motor circuit via three terminals: **L (Line)**, **F (Field)**, and **A (Armature)**.
*   **Construction:** It consists of a graded starting resistance divided into several studs. A spring-loaded metallic handle is used to sweep across these studs. The starter incorporates two electromagnets: the No-Volt Release (NVR) coil and the Overload Release (OLR) coil.
*   **Starting Operation:** 
    1. The operator turns on the main supply and pushes the handle against the spring tension to **Stud 1**.
    2. At Stud 1, the *entire* starting resistance is connected in series with the armature, safely limiting the starting current. Simultaneously, the field winding is connected directly to the full supply voltage through the brass arc and NVR coil, providing maximum starting flux.
    3. As the motor accelerates, it builds up back EMF ($E_b$). The operator manually sweeps the handle across the subsequent studs (2, 3, 4...), gradually cutting the resistance out of the armature circuit as the motor reaches full speed.
*   **Holding Operation:** At the final "RUN" position, all starting resistance is removed from the armature. The handle is physically held in the "RUN" position by the magnetic pull of the **NVR coil**, which is wired in series with the shunt field.
*   **Protective Operation:**
    *   *No-Volt Protection:* If the power supply fails or the field circuit breaks, the NVR coil loses its magnetism. The spring instantly pulls the handle back to the "OFF" position, safely disconnecting the motor.
    *   *Overload Protection:* If the motor draws too much current, the **OLR coil** (wired in series with the line) becomes highly magnetized. It pulls a small metal lever that short-circuits the NVR coil. This kills the NVR's magnetism, causing the spring to snap the handle back to "OFF".

**[Figure Involved - Three-Point Starter Diagram]**
*(Instruction for drawing):*
*   Draw the DC supply connected to terminal **L**.
*   Route **L** through the OLR coil to the pivot of the movable Handle.
*   Draw a series of resistor coils connected between contact studs.
*   The last stud connects to terminal **A** (which goes to the motor armature).
*   The Handle has a soft iron piece. When at the "RUN" position, it touches an electromagnet (NVR coil).
*   The NVR coil connects the first stud to terminal **F** (which goes to the motor shunt field).
*   Show a small lever below the NVR coil that can short-circuit it, operated by the magnetic pull of the OLR coil.

*   **Reference in Mam Slide:** 268 (Purposes), 270 (3-point diagram)
*   **Reference in Firoz Note:** 114, 115

---

### 65. Page 5, Q.73: Which characteristics of three-point starter make it unpopular? How those problems can be resolved using four-point starter?

**Solution:**

**Why the Three-Point Starter is Unpopular:**
The main drawback of the 3-point starter arises when it is used with motors that require **speed control above base speed** using the field weakening method.
1.  In a 3-point starter, the No-Volt Release (NVR) electromagnet coil is wired in **series** with the motor's shunt field circuit.
2.  To increase the motor's speed, an external rheostat is used to add resistance to the field circuit, which decreases the field current ($I_f$).
3.  Because the NVR coil is in the same series loop, the current flowing through the NVR coil also decreases drastically.
4.  If the speed is increased too much, the magnetic pull of the NVR coil becomes weaker than the tension of the handle's return spring.
5.  Consequently, the handle will unexpectedly snap back to the "OFF" position, shutting down the motor during normal operation. This "unwanted tripping" makes the 3-point starter unsuitable for variable-speed applications.

**Resolution Using a Four-Point Starter:**
The 4-point starter solves this problem by mechanically and electrically isolating the NVR coil from the field circuit.
1.  **Structural Change:** A 4th terminal (usually labeled $N$ or $L_2$) is added. The NVR coil is removed from the field circuit series loop.
2.  **Parallel Circuit:** Instead, the NVR coil is connected in parallel with the field and armature, directly across the main supply lines, usually in series with its own fixed current-limiting protective resistor.
3.  **How it Resolves the Issue:** Because the NVR coil is now on an independent parallel branch, changing the field resistance to control the motor's speed no longer has any effect on the current flowing through the NVR coil. 
4.  The NVR coil maintains a constant, strong magnetic pull regardless of how much the field is weakened, ensuring the handle stays securely in the "RUN" position at all operational speeds.

*   **Reference in Mam Slide:** 271 (Why 3-point is unpopular), 272 (4-point diagram)
*   **Reference in Firoz Note:** 115 (Drawbacks of 3-point), 116, 117 (Four-point starter)

---

### 66. Page 5, Q.74: Name Different types of starters.

**Solution:**

Based on the construction, control mechanisms, and the specific types of DC motors they operate, the different types of starters are:

1.  **Three-Point Starter:** Used manually for DC shunt and compound motors (best for constant-speed applications).
2.  **Four-Point Starter:** Used manually for DC shunt and compound motors (specifically designed for variable-speed applications requiring field control).
3.  **Series Motor Starter (Two-Point Starter):** Used specifically for DC series motors. They generally feature a No-Load release or No-Voltage release mechanism.
4.  **Definite-Time Starter:** An automatic starter that cuts out starting resistance in fixed, pre-set time intervals using timers, regardless of the motor's actual speed.
5.  **Counter-EMF Starter:** An automatic starter where magnetic contactors monitor the motor's rising Back EMF and automatically cut out steps of resistance as the $E_b$ reaches specific voltage thresholds.
6.  **Across-The-Line Starter:** A simple contactor system used to connect very small fractional-horsepower DC motors directly to the supply line without starting resistors, as their internal resistance is high enough, and inertia low enough, to prevent damage.

*   **Reference in Mam Slide:** 270, 272, 273, 274, 275, 276
*   **Reference in Firoz Note:** 114, 116, 120, 122, 123, 124

---

### 67. Page 8, Q.7(a): Explain how a 3-point starter can be used to start a DC motor with low speed but high starting torque

**Solution:**

To understand how a 3-point starter achieves this specific mechanical starting condition, we must look at the fundamental formulas for torque and speed:
*   **Torque Equation:** $T \propto \Phi \cdot I_a$
*   **Speed Equation:** $N \propto \frac{V_{terminal} - I_a R_{total}}{\Phi}$

When the handle of a 3-point starter is moved to the very first "ON" position (Stud 1), the electrical circuitry forces the motor into a state that naturally yields high torque and low speed:

1.  **High Starting Torque Generation:**
    *   To get maximum torque, we need maximum magnetic flux ($\Phi$). 
    *   In a 3-point starter, the moment the handle touches Stud 1, the shunt field winding is connected directly to the full supply voltage (via the brass arc and the NVR coil). This ensures the field current ($I_f$) is at its absolute maximum, generating **maximum magnetic flux ($\Phi$)**.
    *   Simultaneously, the starting resistance is sized to allow a safely large armature current ($I_a$) to flow (typically 1.5 to 2 times the full-load rated current).
    *   Because both $\Phi$ (maximum) and $I_a$ (high) are maximized, their product ($T \propto \Phi \cdot I_a$) generates an extraordinarily **high starting torque**, allowing the motor to easily overcome heavy mechanical inertia.

2.  **Low Starting Speed Maintenance:**
    *   While the motor generates heavy torque, it must not instantly accelerate to dangerous speeds.
    *   At Stud 1, the *entire* series of heavy starting resistors ($R_{start}$) is placed in series with the armature.
    *   The effective voltage actually reaching the armature is drastically reduced due to the massive voltage drop across these resistors: $V_{armature} = V_T - I_a R_{start}$.
    *   Looking at the speed equation, the numerator ($V_{terminal} - I_a R_{total}$) is very small, while the denominator ($\Phi$) is at its maximum value. 
    *   A small numerator divided by a large denominator results in a very **low speed ($N$)**.

Therefore, the circuit architecture of the 3-point starter at the initial switch-on mathematically forces the machine to produce high starting torque while physically constraining the rotational speed to a slow, manageable crawl until the operator sweeps the handle further.

*   **Reference in Mam Slide:** 270 (3-point starter operation)
*   **Reference in Firoz Note:** 114 (Operation analysis)

Here are the detailed solutions for the next 4 questions from your syllabus list (Items 68, 69, 70, and 71). These questions focus heavily on the necessity, operation, and comparison of DC motor starters.

### 68. Page 9, Q.6(b): Why starter is required for DC motor? What is the drawback of three point starter? Explain how this drawback can be overcome in four point starter.

**Solution:**

**1. Why a Starter is Required:**
The armature current of a DC motor is determined by the equation $I_a = \frac{V - E_b}{R_a}$. 
At the exact moment of starting, the motor's rotor is stationary ($N = 0$). Since back EMF ($E_b$) is directly proportional to speed, the back EMF is zero ($E_b = 0$). 
This reduces the equation to $I_a = \frac{V}{R_a}$. Because the armature resistance ($R_a$) is extremely small (typically less than $0.5 \, \Omega$), applying the full line voltage will result in a massive, destructive surge of starting current (often 20 to 30 times the rated full-load current). This excessive current will burn the armature windings, cause severe commutator sparking, and mechanically shock the shaft. A starter is required to insert a temporary high resistance in series with the armature to choke this starting current to a safe limit.

**2. Drawback of the Three-Point Starter:**
The three-point starter works perfectly for motors running at normal speeds. However, its major drawback appears when it is used with a variable-speed motor utilizing the **field weakening method** (adding resistance to the field circuit to increase speed).
In a 3-point starter, the holding electromagnet—the No-Volt Release (NVR) coil—is wired in **series** with the motor's shunt field. When the operator increases the field resistance to achieve higher speeds, the field current drops significantly. Consequently, the magnetic pull of the NVR coil weakens. If the field current drops too much, the NVR coil can no longer overcome the tension of the handle's return spring, causing the handle to snap back to the "OFF" position and unintentionally shutting down the motor.

**3. Overcoming the Drawback in a Four-Point Starter:**
The four-point starter overcomes this by decoupling the NVR coil from the field circuit entirely. 
A fourth terminal is added to the starter. The NVR coil is removed from the field branch and placed in its own independent parallel circuit directly across the supply lines (usually in series with a fixed current-limiting resistor). 
Because the NVR coil is on a separate circuit, manipulating the field rheostat to increase motor speed changes the field current but has absolutely **no effect on the current flowing through the NVR coil**. The holding electromagnet remains strong, and the motor runs smoothly at high speeds without the handle accidentally tripping.

*   **Reference in Mam Slide:** 267 (Necessity), 271 (3-point drawback), 272 (4-point diagram)
*   **Reference in Firoz Note:** 114, 115, 116, 117

---

### 69. Page 10, Q.7(a): Explain with neat sketch, how 3-point starter can start dc motor with heavy starting torque but with low speed. [Figure Involved]

**Solution:**

*(Note: This is conceptually identical to question 67, but explicitly asks for the explanation to be tied to the sketch of the 3-point starter).*

**[Figure Involved - 3-Point Starter Sketch Instructions]**
To answer this, you must draw the 3-point starter diagram:
1.  Draw the supply lines (+ and -). The positive line goes to the **L (Line)** terminal of the starter.
2.  From **L**, the circuit passes through the Overload Release (OLR) coil and attaches to the pivot of the movable starting handle.
3.  Draw a series of resistance coils connected to brass studs (Stud 1, 2, 3... RUN). 
4.  The last "RUN" stud connects to the **A (Armature)** terminal, which goes to the motor armature.
5.  Draw a continuous brass arc under the studs. When the handle hits Stud 1, it also touches this arc. The arc connects to the No-Volt Release (NVR) coil, which then connects to the **F (Field)** terminal, going to the motor's shunt field.

**Explanation (How it achieves High Torque and Low Speed):**
The mechanical output of the motor is dictated by two equations:
*   **Torque:** $T \propto \Phi \cdot I_a$
*   **Speed:** $N \propto \frac{V_{net}}{\Phi}$

When the operator pulls the handle to the very first position (**Stud 1**), two critical electrical connections are made simultaneously that force the motor into a high-torque/low-speed state:

1.  **High Starting Torque:** At Stud 1, the handle makes contact with the brass arc, which sends full supply voltage directly to the shunt field winding (via the NVR coil). This ensures maximum field current ($I_f$), thereby producing the **maximum magnetic flux ($\Phi$)**. At the same time, the starting resistance allows a safely high starting current ($I_a$) to pass into the armature. Since Torque = $K \cdot \Phi \cdot I_a$, maximizing the flux while allowing a heavy starting current generates a massive starting torque capable of turning heavy loads.
2.  **Low Starting Speed:** At Stud 1, the *entire* starting resistance is physically in series with the armature. This causes a massive voltage drop ($I_a R_{start}$). Therefore, the actual voltage reaching the armature ($V_{net} = V - I_a R_{start}$) is very small. Looking at the speed equation, a very small net voltage in the numerator divided by a maximum flux ($\Phi$) in the denominator guarantees that the motor's initial rotational speed ($N$) will be very low and safe.

*   **Reference in Mam Slide:** 270
*   **Reference in Firoz Note:** 114

---

### 70. Page 14, Q.3(c): What are the functions of 4-point starter to start a dc motor?

**Solution:**

The four-point starter performs all the standard protective duties of a basic starter, but with one critical added function for advanced motor control. Its primary functions are:

1.  **Limiting Starting Current:** Just like a 3-point starter, it inserts a high graded resistance in series with the armature circuit at standstill. This prevents the destructive inrush of current when the back EMF is zero, ensuring the motor accelerates safely without burning out the armature.
2.  **Facilitating High-Speed Control (The Primary Function):** This is the unique function of the 4-point starter. By separating the No-Volt Release (NVR) coil from the motor's field circuit and putting it on an independent 4th parallel line, the starter allows the operator to severely weaken the field (to achieve speeds high above the base speed) without the risk of the NVR coil losing its magnetism and accidentally shutting off the motor.
3.  **Under-Voltage / No-Voltage Protection:** If the main power grid fails, the independent NVR coil loses power and demagnetizes. A return spring pulls the starting handle back to the "OFF" position. This prevents the motor from violently restarting on its own when the power grid comes back online.
4.  **Overload Protection:** It contains an Overload Release (OLR) coil in series with the main line. If the motor is subjected to an excessive mechanical load and draws too much current, the OLR coil becomes strongly magnetized. It pulls a lever that short-circuits the NVR coil, causing the handle to release and shutting the motor down before it overheats.

*   **Reference in Mam Slide:** 272 (4-point diagram)
*   **Reference in Firoz Note:** 116, 117

---

### 71. Page 25, CT-03 Q.1: Why is starter required in starting DC motor? Write the advantages and limitations of three-point starter and four-point starter.

**Solution:**

**Why a Starter is Required:**
When a DC motor is off, speed $N = 0$, so back EMF $E_b = 0$. According to Ohm's law for a motor armature ($I_a = \frac{V - E_b}{R_a}$), applying full line voltage $V$ directly to the very low resistance of the armature ($R_a$) results in a catastrophic short-circuit-level current. A starter is required to insert temporary resistance in the armature circuit to keep $I_a$ within safe limits until the motor spins up and generates its own protective back EMF.

**Three-Point Starter:**
*   **Advantages:** 
    *   Simple, robust, and cost-effective construction.
    *   Provides excellent No-Voltage and Overload protection.
    *   **Built-in Field Failure Protection:** Because the holding coil (NVR) is in series with the field, if the field winding accidentally breaks, the NVR coil instantly loses power and shuts off the motor. This safely prevents the motor from accelerating to infinite "runaway" speeds due to loss of flux.
*   **Limitations:**
    *   Unsuitable for variable-speed applications. If a field rheostat is used to reduce field current to increase motor speed, the NVR coil (being in the same series circuit) weakens and drops the handle, shutting down the motor unexpectedly.

**Four-Point Starter:**
*   **Advantages:**
    *   Solves the 3-point starter's limitation by placing the NVR coil on a separate, independent circuit.
    *   Allows for complete, uninterrupted speed control (via severe field weakening) without the risk of the starter handle accidentally tripping to the OFF position.
*   **Limitations:**
    *   **Loss of Open-Field Protection:** Because the NVR holding coil is totally independent of the motor's field circuit, it cannot "sense" if the field winding breaks. If the field circuit breaks while running, the motor will accelerate to a destructive runaway speed, but the 4-point starter will *not* trip to protect it. (To fix this, an additional "no-field relay" must be installed externally).

*   **Reference in Mam Slide:** 267, 270, 271, 272
*   **Reference in Firoz Note:** 114, 115, 116, 117

Here are the detailed step-by-step solutions for the next 4 questions (Items 72, 74, 75, and 76) from your syllabus list. 

*(Note: Item 73 in your list is a section heading: "13. Losses in DC machines (and Power flow diagram)", so I have skipped it and moved to the actual questions).*

### 72. Page 26, CT-02 Q.No.3: Why is starter needed for starting dc motor? How four point starter overcome the difficulties of three point starter?

**Solution:**

**Why a Starter is Needed:**
The current drawn by the armature of a DC motor is given by the equation:
$$I_a = \frac{V - E_b}{R_a}$$
When the motor is just turned on (at standstill), the speed is zero ($N = 0$). Since the Back EMF ($E_b$) is generated by the physical rotation of the armature cutting through flux ($E_b \propto N$), the Back EMF is strictly **zero volts** at starting.
The equation then becomes $I_a = \frac{V}{R_a}$. Because the internal armature resistance ($R_a$) is designed to be very small (to minimize heat losses during normal operation, typically $0.1 \, \Omega$ to $0.5 \, \Omega$), applying the full supply voltage ($V$) will force a catastrophic short-circuit-level current through the machine. This massive current will burn out the armature windings and severely damage the commutator. A starter is needed to insert a large external resistance in series with the armature to safely choke this initial current until the motor spins up and generates its own protective Back EMF.

**Difficulties of the Three-Point Starter:**
The 3-point starter has a major flaw when used with motors requiring **field-weakening speed control**. In its design, the holding electromagnet (the No-Volt Release or NVR coil) is wired in **series** with the motor's shunt field circuit. If the operator wants to increase the motor's speed, they must add resistance to the field circuit to reduce the field current. Because they are in series, reducing the field current also reduces the current flowing through the NVR coil. If the speed is pushed too high, the magnetic pull of the NVR coil becomes too weak to hold the starter handle, and the spring violently snaps the handle back to the "OFF" position, shutting down the motor mid-operation.

**How the Four-Point Starter Overcomes This:**
The 4-point starter overcomes this problem by electrically separating the NVR holding coil from the motor's field circuit entirely. 
By adding a fourth terminal, the NVR coil is wired into its own independent, **parallel** circuit directly across the main supply lines (usually protected by its own fixed resistor). Because the NVR coil is no longer on the same branch as the field winding, manipulating the field rheostat to change the motor's speed has absolutely no effect on the current flowing through the NVR coil. The holding magnet remains at full strength regardless of how much the motor's field is weakened, preventing unwanted tripping.

*   **Reference in Mam Slide:** 267, 271, 272
*   **Reference in Firoz Note:** 114, 115, 116, 117

---

### 74. Page 5, Q.68: Prove that the electrical power converted into mechanical power is equal to the product of the counter emf and the armature current.

**Solution:**

**Proof:**

1.  **Start with the Voltage Equation:**
    For any operating DC motor, the applied terminal voltage ($V$) must overcome the opposing Counter EMF (or Back EMF, $E_b$) and the voltage drop caused by the armature resistance ($I_a R_a$). By Kirchhoff’s Voltage Law:
    $$V = E_b + I_a R_a$$

2.  **Convert to a Power Equation:**
    To find the power distribution within the armature, multiply every term in the voltage equation by the armature current ($I_a$):
    $$V \cdot I_a = (E_b + I_a R_a) \cdot I_a$$
    $$V I_a = E_b I_a + I_a^2 R_a$$

3.  **Analyze the Power Terms:**
    *   **$V I_a$:** This is the total electrical power supplied from the grid directly to the armature of the motor.
    *   **$I_a^2 R_a$:** This is the power wasted as heat within the copper windings of the armature (Armature Copper Loss). This energy is completely lost to the environment and cannot be used for mechanical work.
    *   **$E_b I_a$:** According to the Law of Conservation of Energy, the total power input ($V I_a$) minus the power lost to heat ($I_a^2 R_a$) must equal the remaining useful power. This remaining power is what physically rotates the shaft. 

4.  **Conclusion:**
    Therefore, the term $E_b I_a$ mathematically represents the gross electrical power that has been successfully converted into internal mechanical power ($P_m$).
    $$P_m = V I_a - I_a^2 R_a$$
    $$P_m = E_b I_a$$
    *(Hence, proved).*

*   **Reference in Mam Slide:** 223, 224
*   **Reference in Firoz Note:** 82, 83

---

### 75. Page 5, Q.69: Explain in detail what are the losses in DC machine?

**Solution:**

Losses in a DC machine dictate its efficiency and operating temperature. The total losses are broadly classified into three main categories: Copper Losses, Iron (Magnetic) Losses, and Mechanical Losses.

**1. Copper Losses ($I^2R$ Losses):**
These are electrical losses caused by the resistance of the copper windings in the machine when current flows through them. They are **variable losses** because they change directly with the load current.
*   **Armature Copper Loss ($I_a^2 R_a$):** The most significant loss, accounting for 30% to 40% of full-load losses. It varies with the square of the armature current.
*   **Field Copper Loss:** 
    *   *Shunt Field Loss ($I_{sh}^2 R_{sh}$ or $V \cdot I_{sh}$):* Considered practically constant since the shunt field voltage/current is usually constant. Accounts for 20% to 30% of losses.
    *   *Series Field Loss ($I_{se}^2 R_{se}$):* A variable loss depending on load current.
*   *Brush Contact Loss:* The power lost due to the resistance between the carbon brushes and the commutator segments. Often lumped together with armature copper loss.

**2. Iron (Magnetic or Core) Losses:**
These occur in the armature core due to its rotation within the magnetic field. They are largely considered **constant losses** and consist of:
*   **Hysteresis Loss ($W_h$):** As the armature rotates, its magnetic domains are continuously forced to align and realign with the alternating North and South poles. This constant molecular friction generates heat. It is calculated by Steinmetz’s formula ($W_h = \eta B_{max}^{1.6} f V$). It is minimized by using high-grade silicon steel.
*   **Eddy Current Loss ($W_e$):** When the solid iron core cuts through the magnetic flux, small circulating "eddy" currents are induced within the core itself, causing $I^2R$ heating. It is minimized by constructing the armature core out of thin, insulated laminated sheets rather than a solid block of iron.

**3. Mechanical Losses:**
These are physical friction losses caused by the rotation of the machine. They are also considered **constant losses** (provided speed is fairly constant).
*   **Friction Loss:** Occurs at the physical contact points, namely the mechanical bearings supporting the shaft and the friction between the carbon brushes pressing against the commutator.
*   **Windage Loss:** The aerodynamic friction (air drag) caused by the armature spinning rapidly through the air inside the machine casing.

*(Note: Iron losses and Mechanical losses combined are collectively referred to as **Stray Losses** or **Rotational Losses**).*

*   **Reference in Mam Slide:** 198, 199, 200, 201, 202, 203
*   **Reference in Firoz Note:** 125 (Power flow), 128, 129, 130, 131

---

### 76. Page 5, Q.70: Prove that the efficiency of a dc generator will be maximum when the load current is such that variable loss is equal to the constant loss.

**Solution:**

**Proof:**

1.  **Define Generator Efficiency ($\eta$):**
    The efficiency of a DC generator is the ratio of output power to input power.
    $$\eta = \frac{\text{Output Power}}{\text{Input Power}} = \frac{\text{Output Power}}{\text{Output Power} + \text{Total Losses}}$$
    
2.  **Express in terms of Current and Voltage:**
    Let $V$ = Terminal voltage, $I$ = Load current, $R_a$ = Armature resistance.
    *   **Output Power** = $VI$
    *   **Variable Losses** = Armature copper loss $\approx I^2 R_a$ (assuming $I_a \approx I$ for simplicity in derivation).
    *   **Constant Losses** = $W_c$ (Includes iron, friction, windage, and shunt field copper losses).
    
    Substitute these into the efficiency equation:
    $$\eta = \frac{V I}{V I + I^2 R_a + W_c}$$

3.  **Simplify the Equation:**
    Divide the numerator and the denominator by $I$:
    $$\eta = \frac{V}{V + I R_a + \frac{W_c}{I}}$$

4.  **Maximize the Efficiency:**
    For the efficiency ($\eta$) to be at its maximum, the denominator of this fraction must be at its minimum. Since $V$ is practically constant, we must minimize the variable part of the denominator with respect to the load current $I$.
    To find the minimum, we take the derivative of the denominator with respect to $I$ and set it to zero:
    $$\frac{d}{dI} \left( V + I R_a + \frac{W_c}{I} \right) = 0$$
    The derivative of a constant ($V$) is zero. The derivative of $I R_a$ is $R_a$. The derivative of $W_c I^{-1}$ is $-W_c I^{-2}$.
    $$0 + R_a - \frac{W_c}{I^2} = 0$$
    $$R_a = \frac{W_c}{I^2}$$
    $$I^2 R_a = W_c$$

5.  **Conclusion:**
    *   $I^2 R_a$ represents the **Variable Losses**.
    *   $W_c$ represents the **Constant Losses**.
    
    Therefore, we have mathematically proven that the efficiency of a DC generator is maximum when its operating load current is such that the **Variable Loss is exactly equal to the Constant Loss**.

*   **Reference in Mam Slide:** 205 (Efficiency derivation)
*   **Reference in Firoz Note:** 140, 141 (Condition for maximum efficiency)

Here are the detailed step-by-step solutions for the final 2 questions (Items 77 and 78) from your syllabus list.

### 77. Page 25, CT-03 Q.3: Shortly describe the losses occurring in dynamo.

**Solution:**

A dynamo is an older, broader term used to describe a DC generator (and by extension, the same physics applies to DC motors). The losses occurring in a dynamo dictate its efficiency and cause the machine to heat up during operation. These losses are broadly classified into three main categories: Copper Losses, Iron (Magnetic) Losses, and Mechanical Losses.

**1. Copper Losses (Electrical / $I^2R$ Losses):**
These are the power losses that occur as heat due to the inherent electrical resistance of the copper wire windings when current flows through them. These are primarily considered **variable losses** because they change as the load on the machine changes.
*   **Armature Copper Loss ($I_a^2 R_a$):** The most significant loss, causing about 30% to 40% of the total full-load losses. It varies with the square of the armature current.
*   **Field Copper Loss:** 
    *   *Shunt Field Loss ($I_{sh}^2 R_{sh}$ or $V \cdot I_{sh}$):* Considered a constant loss since the shunt field voltage is generally constant. Accounts for 20% to 30% of full-load losses.
    *   *Series Field Loss ($I_{se}^2 R_{se}$):* A variable loss that fluctuates with the load current.

**2. Iron Losses (Magnetic or Core Losses):**
These losses occur in the iron core of the armature due to its continuous rotation within the stationary magnetic field. They are considered **constant losses** at a constant speed and voltage.
*   **Hysteresis Loss ($W_h$):** As the armature rotates, its magnetic domains are continuously forced to realign with the alternating North and South poles. This molecular "friction" generates heat. It depends on the volume of the core, the frequency of magnetic reversals, and the maximum flux density (calculated using Steinmetz’s formula).
*   **Eddy Current Loss ($W_e$):** When the solid iron core cuts through the magnetic flux, tiny circulating "eddy" voltages are induced within the core itself, causing localized $I^2R$ heating. This is minimized by building the armature core out of thin, insulated laminations instead of a solid block of steel.

**3. Mechanical Losses:**
These are physical friction losses caused by the mechanical rotation of the machine. They are also considered **constant losses** as long as the motor runs at a relatively constant speed.
*   **Friction Loss:** Occurs due to physical contact, specifically the mechanical bearings supporting the heavy rotating shaft, and the sliding friction of the carbon brushes pressing against the commutator.
*   **Windage Loss:** The aerodynamic friction (air drag) caused by the armature spinning rapidly and churning the air inside the machine casing.

*(Note: Iron losses and Mechanical losses are usually grouped together and referred to as **Stray Losses** or **Rotational Losses**).*

*   **Reference in Mam Slide:** 198, 199, 200, 201, 202, 203
*   **Reference in Firoz Note:** 125, 128, 129, 130, 131
*   **Figure Involved:** None required (A tree-diagram showing Total Losses splitting into Copper, Iron, and Mechanical is often drawn for clarity).

---

### 78. Page 27, CT-02 Q.No.3: A 220V shunt motor takes a total current of 80A and runs at a speed of 800 rpm. Shunt field resistance and armature resistance are 50 ohm and 0.1 ohm respectively. If iron and friction losses amount to 1600 W, find the efficiency of the motor.

**Solution:**

**Given Data:**
*   Terminal voltage, $V_T = 220 \text{ V}$
*   Total line current drawn, $I_L = 80 \text{ A}$
*   Motor speed, $N = 800 \text{ rpm}$ *(Note: This value is provided for context but is not mathematically required to calculate the efficiency).*
*   Shunt field resistance, $R_{sh} = 50 \, \Omega$
*   Armature resistance, $R_a = 0.1 \, \Omega$
*   Rotational losses (Iron + Friction/Windage), $P_{rot} = 1600 \text{ W}$

**Step 1: Calculate the Total Input Power ($P_{in}$)**
The total electrical power supplied to the motor from the grid:
$$P_{in} = V_T \times I_L$$
$$P_{in} = 220 \text{ V} \times 80 \text{ A} = 17,600 \text{ W}$$

**Step 2: Calculate the Currents in the Motor Branches**
*   **Shunt Field Current ($I_{sh}$):** 
    Because the shunt field is connected directly across the supply line:
    $$I_{sh} = \frac{V_T}{R_{sh}} = \frac{220}{50} = 4.4 \text{ A}$$
*   **Armature Current ($I_a$):**
    By Kirchhoff's Current Law, the total line current splits into the field and the armature:
    $$I_a = I_L - I_{sh} = 80 - 4.4 = 75.6 \text{ A}$$

**Step 3: Calculate the Electrical Copper Losses**
*   **Shunt Field Copper Loss ($P_{f\_loss}$):**
    $$P_{f\_loss} = V_T \times I_{sh} \quad \text{or} \quad I_{sh}^2 \times R_{sh}$$
    $$P_{f\_loss} = 220 \times 4.4 = 968 \text{ W}$$
*   **Armature Copper Loss ($P_{a\_loss}$):**
    $$P_{a\_loss} = I_a^2 \times R_a$$
    $$P_{a\_loss} = (75.6)^2 \times 0.1 = 5715.36 \times 0.1 = 571.536 \text{ W}$$

**Step 4: Calculate the Total Losses ($P_{loss\_total}$)**
The total losses are the sum of the copper losses and the given rotational (iron + friction) losses:
$$P_{loss\_total} = P_{f\_loss} + P_{a\_loss} + P_{rot}$$
$$P_{loss\_total} = 968 \text{ W} + 571.536 \text{ W} + 1600 \text{ W}$$
$$P_{loss\_total} = 3139.536 \text{ W}$$

**Step 5: Calculate the Output Power ($P_{out}$)**
The net mechanical power available at the motor shaft is the input power minus the total losses:
$$P_{out} = P_{in} - P_{loss\_total}$$
$$P_{out} = 17600 \text{ W} - 3139.536 \text{ W} = 14460.464 \text{ W}$$

*(Alternative Step 5 using Back EMF method for verification):*
*   *Back EMF, $E_b = V_T - I_a R_a = 220 - (75.6 \times 0.1) = 220 - 7.56 = 212.44 \text{ V}$*
*   *Gross Mechanical Power, $P_m = E_b \times I_a = 212.44 \times 75.6 = 16060.464 \text{ W}$*
*   *Net Output Power, $P_{out} = P_m - P_{rot} = 16060.464 - 1600 = 14460.464 \text{ W}$ (Match!)*

**Step 6: Calculate the Efficiency ($\eta$)**
Efficiency is the ratio of output power to input power, expressed as a percentage:
$$\eta = \frac{P_{out}}{P_{in}} \times 100\%$$
$$\eta = \frac{14460.464}{17600} \times 100\%$$
$$\eta \approx 0.821617 \times 100\% = 82.16\%$$

**Answer: The efficiency of the motor is 82.16%.**

*   **Reference in Mam Slide:** 204 (Power stages), 205 (Efficiency formula), 224
*   **Reference in Firoz Note:** 140 (Efficiency of DC machines)
*   **Figure Involved:** None required (but a power flow diagram is helpful conceptually).