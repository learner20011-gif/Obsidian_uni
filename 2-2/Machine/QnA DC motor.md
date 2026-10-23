### **1. Working principle of motor**

### 1. Page 4, Q.52: Explain the principle of operation of a DC motor.

**Principle of Operation:**
* **Energy Conversion:** Converts direct-current (DC) electrical energy into mechanical rotational energy.
* **Lorentz Force Principle:** When a current-carrying conductor is placed in a magnetic field, it experiences a mechanical force:
  $$F = B \cdot I \cdot L \cdot \sin\theta$$
  *(where $B$ = magnetic flux density, $I$ = conductor current, $L$ = active length, $\theta$ = angle between conductor and flux lines).*
* **Direction of Force:** Determined by **Fleming's Left-Hand Rule** (Thumb = Force/Motion, Forefinger = Magnetic Field, Middle finger = Current).
* **Torque Production:** Conductors on opposite sides of the armature carry current in opposite directions, producing equal and opposite forces that create a continuous rotational torque ($T = k \Phi I_a$).
* **Commutator Action:** As coils rotate past the magnetic neutral plane, the commutator reverses current direction in each coil, ensuring unidirectional and continuous torque.

* **Reference in Mam Slide:** 20, 214, 215, 216
* **Reference in Firoz Note:** 2, 72, 74, 76
* **Reference in Rosenblatt:** Sections 7-1, 7-2, 7-3, Pages 72-74
* **Reference in Theraja Vol II:** PDF Page 139

---

### 2. Page 5, Q.71: How will you change the direction of rotation of a d.c motor?

**Solution:**
Torque direction depends on two quantities (Fleming's Left-Hand Rule):
1. Direction of main field flux ($\Phi$).
2. Direction of armature current ($I_a$).

To reverse motor rotation, reverse **either one (and only one)** of the two:
* **Method 1 (Reverse Armature Terminals):** Interchange the armature leads ($A_1, A_2$). Field flux remains unchanged $\rightarrow$ net torque reverses $\rightarrow$ motor runs in reverse. *(Preferred method)*.
* **Method 2 (Reverse Field Terminals):** Interchange the field winding leads ($F_1, F_2$). Field polarity flips while armature current remains unchanged $\rightarrow$ net torque reverses.
* **Caution:** If you reverse the main supply leads (both armature and field simultaneously), the two reversals cancel each other out, and the motor continues rotating in its original direction.

* **Reference in Mam Slide:** 214, 295
* **Reference in Firoz Note:** 91, 114
* **Reference in Rosenblatt:** Section 7-3, Pages 73-74
* **Reference in Theraja Vol II:** PDF Page 139

---

### 3. Page 9, Q.5(a): Describe the construction and working principle of DC motor.

**1. Essential Construction Parts:**
* **Yoke / Stator Frame:** Outer cast iron/steel cylindrical frame; protects internal parts and provides a low-reluctance magnetic return path.
* **Poles & Field Coils:** Laminated pole cores and pole shoes carrying copper field windings to produce the main working flux ($\Phi$).
* **Armature (Rotor):** Laminated silicon steel cylindrical core with peripheral slots to house the armature coils; rotates on bearings.
* **Commutator:** Wedge-shaped hard-drawn copper segments insulated by mica; periodically reverses coil currents to maintain unidirectional torque.
* **Brushes:** Carbon/graphite blocks riding on the commutator to transfer DC power between stationary supply and rotating armature.
* **[Figure Involved]:** Cross-sectional diagram of DC machine showing yoke, poles, armature conductors, commutator, and brushes.

**2. Working Principle:**
* Current supplied to field coils creates stationary magnetic flux ($B$).
* Current supplied through brushes and commutator into armature coils creates Lorentz forces:
  $$F = B I L \sin\theta$$
* Opposing forces on opposite coil sides generate net electromagnetic torque:
  $$T = k \Phi I_a$$
* Commutator continuously switches current direction as conductors cross the neutral plane, maintaining smooth continuous rotation.

* **Reference in Mam Slide:** 10, 11, 12, 61, 62, 63, 65, 236
* **Reference in Firoz Note:** 72, 74, 78
* **Reference in Rosenblatt:** Sections 2-2, 2-3, 2-4, 2-5, 7-1, 7-2, 7-3, 7-4, Pages 14-15, 72-78
* **Reference in Theraja Vol II:** PDF Page 139

---

### **2. Back E.M.F.**

### 4. Page 4, Q.54: Define counter EMF. Explain the significance of counter EMF of a dc motor.

**1. Definition of Counter EMF (Back EMF):**
* As the armature rotates, its conductors cut the main magnetic field lines.
* By Faraday's Law, an electromotive force (EMF) is induced in the rotating armature.
* By Lenz's Law, this induced voltage acts in direct opposition to the applied supply voltage ($V$). Hence it is called **Back EMF** or **Counter EMF** ($E_b$):
  $$E_b = \frac{P \Phi Z N}{60 A}$$
  *(where $P$ = poles, $\Phi$ = flux/pole, $Z$ = conductors, $N$ = speed in rpm, $A$ = parallel paths).*

**2. Significance of Back EMF:**
* **Limits Armature Current:** The net driving voltage across the armature is $(V - E_b)$. Since armature resistance ($R_a$) is very small:
  $$I_a = \frac{V - E_b}{R_a}$$
  Without $E_b$, destructive currents would burn the armature windings.
* **Automatic Governor (Self-Regulation):** 
  * *Load added* $\rightarrow$ motor slows down ($N \downarrow$) $\rightarrow E_b \downarrow \rightarrow I_a \uparrow \rightarrow$ torque increases ($T \uparrow$) to match the heavier load.
  * *Load removed* $\rightarrow$ motor speeds up ($N \uparrow$) $\rightarrow E_b \uparrow \rightarrow I_a \downarrow \rightarrow$ torque decreases ($T \downarrow$) to prevent overspeeding.
* **Determines Mechanical Power Conversion:**
  $$P_m = E_b I_a$$

* **Reference in Mam Slide:** 220, 221, 222
* **Reference in Firoz Note:** 80, 81, 82
* **Reference in Rosenblatt:** Section 7-5, Pages 78-79
* **Reference in Theraja Vol II:** PDF Pages 141-142

---

### 6. Page 4, Q.56: What is back EMF in a dc motor? What will happen if the back EMF (Eb) is equal to the terminal voltage (V) of a dc motor?

**1. Definition:**
* Back EMF ($E_b$) is the self-induced voltage generated in the rotating armature conductors that opposes the applied terminal voltage ($V$) in accordance with Lenz's Law.

**2. What happens if $E_b = V$:**
* Armature current equation:
  $$I_a = \frac{V - E_b}{R_a}$$
* If $E_b = V$, then:
  $$I_a = \frac{V - V}{R_a} = 0\text{ A}$$
* Developed torque drops to zero:
  $$T \propto \Phi I_a = 0$$
* **Consequence:** Without torque, the motor cannot overcome its internal friction and windage losses, so it decelerates immediately.
* **Conclusion:** In a practical running motor, $E_b$ is always slightly less than $V$ ($E_b < V$) to draw the small no-load current needed to sustain rotation.

* **Reference in Mam Slide:** 220, 221
* **Reference in Firoz Note:** 80, 81
* **Reference in Rosenblatt:** Section 7-5, Pages 78-79
* **Reference in Theraja Vol II:** PDF Page 141
* **Figure Involved:** None

---

### 7. Page 5, Q.67: For a dc motor, prove that the gross mechanical power developed by a motor is maximum when back emf is equal to half of the applied voltage.

**Proof:**
1. Motor voltage equation:
   $$V = E_b + I_a R_a$$
2. Multiply by armature current $I_a$ to get the power equation:
   $$V I_a = E_b I_a + I_a^2 R_a$$
   * $V I_a$ = Electrical power input to armature.
   * $E_b I_a = P_m$ = Gross mechanical power developed.
   * $I_a^2 R_a$ = Armature copper loss.
3. Express mechanical power in terms of $I_a$:
   $$P_m = V I_a - I_a^2 R_a$$
4. For maximum mechanical power, differentiate with respect to $I_a$ and equate to zero:
   $$\frac{dP_m}{dI_a} = V - 2 I_a R_a = 0 \implies I_a R_a = \frac{V}{2}$$
5. Substitute $I_a R_a = \frac{V}{2}$ back into the voltage equation:
   $$V = E_b + \frac{V}{2} \implies E_b = \frac{V}{2}$$
* **Conclusion:** Maximum mechanical power occurs when $E_b = \frac{V}{2}$.
* *(Practical Note: This condition yields only 50% efficiency and causes dangerous heating, so motors are never operated at this point).*

* **Reference in Mam Slide:** 225
* **Reference in Firoz Note:** 85, 86
* **Reference in Rosenblatt:** Section 7-6, Pages 79-81
* **Reference in Theraja Vol II:** PDF Page 142
* **Figure Involved:** None

---

### 8. Page 8, Q.7(c): The armature resistance of a shunt motor is 0.08 Ω. When connected to 220 V supply, a counter EMF of 200 V is developed. Find (i) the armature current, (ii) the armature current when the armature is not rotating, and (iii) counter EMF when the armature current is 9.0 A.

**Given Data:**
* $V = 220\text{ V}$, $R_a = 0.08\,\Omega$, $E_{b1} = 200\text{ V}$.

**(i) Armature Current at Normal Operation:**
$$I_{a1} = \frac{V - E_{b1}}{R_a} = \frac{220 - 200}{0.08} = \frac{20}{0.08} = \mathbf{250\text{ A}}$$

**(ii) Armature Current at Standstill ($N = 0$):**
* At standstill, speed is zero $\rightarrow E_b = 0\text{ V}$:
$$I_{a(\text{start})} = \frac{V - 0}{R_a} = \frac{220}{0.08} = \mathbf{2750\text{ A}}$$
*(Illustrates the necessity of a starting resistor).*

**(iii) Counter EMF when $I_{a2} = 9.0\text{ A}$:**
$$E_{b2} = V - I_{a2} R_a = 220 - (9.0 \times 0.08) = 220 - 0.72 = \mathbf{219.28\text{ V}}$$

* **Reference in Mam Slide:** 222
* **Reference in Firoz Note:** 81
* **Reference in Rosenblatt:** Sections 7-5, 7-6, Pages 78-81
* **Reference in Theraja Vol II:** PDF Pages 141-143
* **Figure Involved:** None

---

### 9. Page 14, Q.4(a): What is meant by back emf? Prove that the gross power developed by a dc motor is maximum when the back emf (Eb) is equal to half of the applied voltage (V).

**1. Definition:**
* **Back EMF ($E_b$):** The voltage induced in the armature conductors as they rotate through the magnetic field, acting in opposition to the terminal voltage $V$ (Lenz's Law).

**2. Proof of $E_b = V/2$ for Maximum Power:**
* Gross mechanical power: $P_m = E_b I_a = V I_a - I_a^2 R_a$.
* Differentiating with respect to $I_a$:
  $$\frac{dP_m}{dI_a} = V - 2 I_a R_a = 0 \implies I_a R_a = \frac{V}{2}$$
* Substituting into voltage equation $V = E_b + I_a R_a$:
  $$V = E_b + \frac{V}{2} \implies E_b = \frac{V}{2} \quad \text{(Hence proved.)}$$

* **Reference in Mam Slide:** 220, 221, 225
* **Reference in Firoz Note:** 80, 81, 85, 86
* **Reference in Rosenblatt:** Sections 7-5, 7-6, Pages 78-81
* **Reference in Theraja Vol II:** PDF Pages 141-142
* **Figure Involved:** None

---

### 10. Page 14, Q.4(d): The armature resistance of a shunt motor is 0.09Ω. When connected to a 230V supply a counter-emf of 222.8V is developed. Find the armature current, the armature current when the armature is not rotating and counter-emf when the armature current is 100A.

**Given Data:**
* $V = 230\text{ V}$, $R_a = 0.09\,\Omega$, $E_{b1} = 222.8\text{ V}$.

**(i) Armature Current:**
$$I_{a1} = \frac{V - E_{b1}}{R_a} = \frac{230 - 222.8}{0.09} = \frac{7.2}{0.09} = \mathbf{80\text{ A}}$$

**(ii) Armature Current at Standstill ($N = 0 \implies E_b = 0$):**
$$I_{a(\text{start})} = \frac{V - 0}{R_a} = \frac{230}{0.09} = \mathbf{2555.56\text{ A}}$$

**(iii) Counter EMF when $I_{a2} = 100\text{ A}$:**
$$E_{b2} = V - I_{a2} R_a = 230 - (100 \times 0.09) = 230 - 9.0 = \mathbf{221\text{ V}}$$

* **Reference in Mam Slide:** 222, 267
* **Reference in Firoz Note:** 81, 114
* **Reference in Rosenblatt:** Sections 7-5, 7-6, Pages 78-81
* **Reference in Theraja Vol II:** PDF Pages 141-143
* **Figure Involved:** None

---

### **3. Types of DC motors**

### 12. Page 4, Q.55: Write applications of all DC motors.

**Applications Summary:**
* **DC Shunt Motor (Constant Speed):**
  * *Features:* Nearly flat speed-load curve; medium starting torque.
  * *Applications:* Lathes, centrifugal pumps, fans, blowers, machine tools, printing presses.
* **DC Series Motor (High Starting Torque, Variable Speed):**
  * *Features:* Torque $\propto I_a^2$; speed dangerously high on no-load.
  * *Applications:* Electric traction (trains, trams), cranes, hoists, elevators, automobile starters.
* **Cumulative Compound Motor (High Starting Torque with Safe No-Load Speed):**
  * *Features:* Series field adds to shunt field; will not run away on no-load.
  * *Applications:* Rolling mills, punch presses, shears, heavy planers, elevators.
* **Differential Compound Motor (Unstable / Speed Increases with Load):**
  * *Features:* Rarely used due to severe instability under heavy load.
  * *Applications:* Experimental laboratory setups requiring constant speed over narrow load ranges.

* **Reference in Mam Slide:** 241, 252, 256
* **Reference in Firoz Note:** 92, 101, 105
* **Reference in Rosenblatt:** Sections 8-2, 8-5, 8-7, Pages 90, 95, 98
* **Reference in Theraja Vol II:** PDF Page 155

---

### 13. Page 8, Q.8(b): Define universal motor. Differentiate universal motor from a dc series motor and also mention its applications.

**1. Definition:**
* A **Universal Motor** is a commutated series-wound motor designed to operate efficiently on either single-phase AC or DC supply at approximately the same speed and output.

**2. Differences from a Standard DC Series Motor:**
* **Laminated Stator Core:** Universal motor has fully laminated stator poles and yoke to minimize AC eddy current and hysteresis losses (DC series motor often uses solid steel poles).
* **Compensating Windings:** Universal motors have compensating windings and fewer field turns to reduce high inductive reactance ($X_L = 2\pi f L$) on AC.
* **High Resistance Commutator Brushes:** Universal motor uses specialized high-resistance brushes to limit transformer-action sparking during AC commutation.

**3. Applications:**
* Portable power tools (drills, circular saws), domestic appliances (vacuum cleaners, food blenders, sewing machines, hair dryers).

* **Reference in Mam Slide:** Special Machines Section
* **Reference in Rosenblatt:** Chapter 16, Pages 250-255
* **Reference in Theraja Vol II:** PDF Pages 360-363

---

### 14. Page 10, Q.8(c): What is stepper motor? What are its applications? Draw the truth table and corresponding applied voltage waveforms to make the stepper motor step 30^0. [Figure Involved]

**1. Definition:**
* A **Stepper Motor** is a brushless DC electromechanical device that converts digital electrical input pulses into discrete mechanical angular movements (steps).

**2. Applications:**
* CNC machines, 3D printers, robotic arms, computer hard disk head positioning, medical imaging scanners, camera autofocus mechanisms.

**3. Operation for 30° Step Angle:**
* For a 3-phase, 12-pole variable reluctance or permanent magnet stepper motor with step angle $\beta = 30^\circ$:
  $$\beta = \frac{360^\circ}{m \cdot N_r} = 30^\circ$$

**Truth Table (Wave Drive / 1-Phase ON Sequence):**
| Step | Phase A | Phase B | Phase C | Rotor Angle |
| :---: | :---: | :---: | :---: | :---: |
| **1** | **1** | 0 | 0 | $0^\circ$ |
| **2** | 0 | **1** | 0 | $30^\circ$ |
| **3** | 0 | 0 | **1** | $60^\circ$ |
| **4** | **1** | 0 | 0 | $90^\circ$ |

**Applied Voltage Waveforms:**
```
Phase A: ┌──────┐                ┌──────┐
         │      │                │      │
         └──────┴────────────────┴──────┴─────► Time
Phase B:        ┌──────┐                ┌─────
                │      │                │
         ───────┴──────┴────────────────┴─────► Time
Phase C:               ┌──────┐
                       │      │
         ──────────────┴──────┴───────────────► Time
         ◄─30°─►◄─30°─►◄─30°─►
```

* **Reference in Mam Slide:** Special Machines Section (Stepper Motors)
* **Reference in Rosenblatt:** Chapter 17, Pages 265-272
* **Reference in Theraja Vol II:** PDF Pages 370-375

---

### **4. Equivalent circuit of a DC motor**

### 16. Page 9, Q.6(c): The following values were obtained from the test data of a motor: line voltage, 120 V; line current 30 A; motor speed 186 rad/s; armature resistance 0.25 Ω; field resistance 90 Ω. Determine (i) the field current (ii) armature current (iii) counter – emf (iv) developed kW.

**Given Data:**
* $V = 120\text{ V}$, $I_L = 30\text{ A}$, $\omega = 186\text{ rad/s}$, $R_a = 0.25\,\Omega$, $R_f = 90\,\Omega$.

**(i) Field Current ($I_f$):**
$$I_f = \frac{V}{R_f} = \frac{120}{90} = \mathbf{1.33\text{ A}}$$

**(ii) Armature Current ($I_a$):**
$$I_a = I_L - I_f = 30 - 1.33 = \mathbf{28.67\text{ A}}$$

**(iii) Counter EMF ($E_b$):**
$$E_b = V - I_a R_a = 120 - (28.67 \times 0.25) = 120 - 7.17 = \mathbf{112.83\text{ V}}$$

**(iv) Developed Mechanical Power ($P_{\text{dev}}$):**
$$P_{\text{dev}} = E_b I_a = 112.83 \times 28.67 = 3234.8\text{ W} = \mathbf{3.235\text{ kW}}$$

* **Reference in Mam Slide:** 222, 223
* **Reference in Firoz Note:** 81, 82
* **Reference in Rosenblatt:** Section 7-5, Pages 78-79
* **Reference in Theraja Vol II:** PDF Pages 141-143

---

### 17. Page 14, Q.3(c): The following information was obtained from the nameplate of a shunt motor: 5Hp, 240V DC, full-load current 20.4A, field resistance 202Ω. If the armature resistance is 0.71Ω, determine (i) power delivered to motor, (ii) power dissipated in shunt field, (iii) power dissipated in armature circuit, (iv) electrical power converted into mechanical power.

**Given Data:**
* $P_{\text{rated}} = 5\text{ hp}$, $V = 240\text{ V}$, $I_L = 20.4\text{ A}$, $R_f = 202\,\Omega$, $R_a = 0.71\,\Omega$.

**(i) Power Delivered to Motor ($P_{\text{in}}$):**
$$P_{\text{in}} = V \times I_L = 240 \times 20.4 = \mathbf{4896\text{ W}}\quad (4.896\text{ kW})$$

**(ii) Power Dissipated in Shunt Field ($P_f$):**
$$I_f = \frac{V}{R_f} = \frac{240}{202} \approx 1.188\text{ A}$$
$$P_f = V \times I_f = 240 \times 1.188 = \mathbf{285.15\text{ W}}$$

**(iii) Power Dissipated in Armature Circuit ($P_a$):**
$$I_a = I_L - I_f = 20.4 - 1.188 = 19.212\text{ A}$$
$$P_a = I_a^2 R_a = (19.212)^2 \times 0.71 = \mathbf{262.06\text{ W}}$$

**(iv) Electrical Power Converted into Mechanical Power ($P_m$):**
$$P_m = P_{\text{in}} - P_f - P_a = 4896 - 285.15 - 262.06 = \mathbf{4348.79\text{ W}}\quad (\approx 4.35\text{ kW})$$
*(Alternatively: $E_b = 240 - 19.212 \times 0.71 = 226.36\text{ V} \implies P_m = E_b I_a = 226.36 \times 19.212 = \mathbf{4348.8\text{ W}}$).*

* **Reference in Mam Slide:** 222, 223
* **Reference in Firoz Note:** 81, 82
* **Reference in Rosenblatt:** Sections 7-5, 7-6, Pages 78-81
* **Reference in Theraja Vol II:** PDF Pages 141-143

---

### 18. Page 14, Q.3(d): A 25kW, 250V dc shunt generator has armature and field resistances of 0.08Ω and 110Ω respectively. Determine the total armature power developed when working (i) as a generator delivering 25kW output and (ii) as a motor taking 25kW input.

**Common Parameters:**
* $V = 250\text{ V}$, $R_a = 0.08\,\Omega$, $R_f = 110\,\Omega$.
* Field current: $I_f = \frac{V}{R_f} = \frac{250}{110} = 2.273\text{ A}$.

**(i) Working as a Generator (Delivering $25\text{ kW}$):**
* Line current delivered: $I_L = \frac{25000}{250} = 100\text{ A}$.
* Armature current: $I_a = I_L + I_f = 100 + 2.273 = 102.273\text{ A}$.
* Induced EMF: $E_g = V + I_a R_a = 250 + (102.273 \times 0.08) = 258.18\text{ V}$.
* Armature power developed:
  $$P_{\text{dev(gen)}} = E_g I_a = 258.18 \times 102.273 = \mathbf{26404.8\text{ W}} = \mathbf{26.405\text{ kW}}$$

**(ii) Working as a Motor (Taking $25\text{ kW}$ Input):**
* Line current drawn: $I_L = \frac{25000}{250} = 100\text{ A}$.
* Armature current: $I_a = I_L - I_f = 100 - 2.273 = 97.727\text{ A}$.
* Back EMF: $E_b = V - I_a R_a = 250 - (97.727 \times 0.08) = 242.18\text{ V}$.
* Armature power developed:
  $$P_{\text{dev(motor)}} = E_b I_a = 242.18 \times 97.727 = \mathbf{23667.5\text{ W}} = \mathbf{23.668\text{ kW}}$$

* **Reference in Mam Slide:** 223, 224
* **Reference in Firoz Note:** 82, 83
* **Reference in Rosenblatt:** Section 7-5, Pages 78-79
* **Reference in Theraja Vol II:** PDF Page 143

---

### 19. Page 15, Q.3(c): A 220 V, dc shunt motor having an armature resistance of 0.2 Ω, and a field resistance of 110 Ω takes 4 A of line current while running at 1200 rpm on no load. On load, the input to the motor is 15 kW; calculate the speed and the developed torque.

**Given Data:**
* $V = 220\text{ V}$, $R_a = 0.2\,\Omega$, $R_f = 110\,\Omega$.
* Field current: $I_f = \frac{220}{110} = 2\text{ A}$ (constant).

**1. No-Load Condition:**
* $I_{L0} = 4\text{ A}$, $N_0 = 1200\text{ rpm}$.
* $I_{a0} = I_{L0} - I_f = 4 - 2 = 2\text{ A}$.
* $E_{b0} = V - I_{a0} R_a = 220 - (2 \times 0.2) = 219.6\text{ V}$.

**2. Loaded Condition ($P_{\text{in}} = 15\text{ kW}$):**
* $I_L = \frac{15000}{220} = 68.182\text{ A}$.
* $I_a = I_L - I_f = 68.182 - 2 = 66.182\text{ A}$.
* $E_b = V - I_a R_a = 220 - (66.182 \times 0.2) = 206.764\text{ V}$.

**3. Speed on Load ($N$):**
* Since $\Phi$ is constant:
  $$\frac{N}{N_0} = \frac{E_b}{E_{b0}} \implies N = 1200 \times \frac{206.764}{219.6} = \mathbf{1129.86\text{ rpm}}$$

**4. Developed Torque ($T_{\text{dev}}$):**
$$\omega = \frac{2\pi N}{60} = \frac{2\pi \times 1129.86}{60} = 118.32\text{ rad/s}$$
$$T_{\text{dev}} = \frac{E_b I_a}{\omega} = \frac{206.764 \times 66.182}{118.32} = \mathbf{115.65\text{ N}\cdot\text{m}}$$

* **Reference in Mam Slide:** 228, 230
* **Reference in Firoz Note:** 88, 89
* **Reference in Rosenblatt:** Section 7-7, Pages 82-84
* **Reference in Theraja Vol II:** PDF Pages 146-148

---

### 20. Page 25, CT-03 Q.2: The following values were obtained from the test data of a motor: line voltage 125V, line current 39A, motor speed, 186 rad/s, armature resistance, 0.25Ω, field resistance, 90Ω. Determine (a) the field current, (b) armature current, (c) counter-emf, (d) developed kW, (e) developed torque.

**Given Data:**
* $V = 125\text{ V}$, $I_L = 39\text{ A}$, $\omega = 186\text{ rad/s}$, $R_a = 0.25\,\Omega$, $R_f = 90\,\Omega$.

**(a) Field Current ($I_f$):**
$$I_f = \frac{V}{R_f} = \frac{125}{90} = \mathbf{1.389\text{ A}}$$

**(b) Armature Current ($I_a$):**
$$I_a = I_L - I_f = 39 - 1.389 = \mathbf{37.611\text{ A}}$$

**(c) Counter EMF ($E_b$):**
$$E_b = V - I_a R_a = 125 - (37.611 \times 0.25) = 125 - 9.403 = \mathbf{115.60\text{ V}}$$

**(d) Developed Mechanical Power ($P_{\text{dev}}$):**
$$P_{\text{dev}} = E_b I_a = 115.60 \times 37.611 = 4347.8\text{ W} = \mathbf{4.348\text{ kW}}$$

**(e) Developed Torque ($T_{\text{dev}}$):**
$$T_{\text{dev}} = \frac{P_{\text{dev}}}{\omega} = \frac{4347.8}{186} = \mathbf{23.38\text{ N}\cdot\text{m}}$$

* **Reference in Mam Slide:** 222, 228
* **Reference in Firoz Note:** 81, 88
* **Reference in Rosenblatt:** Section 7-5, Pages 78-79
* **Reference in Theraja Vol II:** PDF Pages 141-143

---

### **5. Torque of DC motor**

### 22. Page 4, Q.53: Derive the expression of induced torque for a real motor.

**Derivation:**
1. Let:
   * $P$ = number of poles, $\Phi$ = flux per pole (Wb).
   * $Z$ = total number of active armature conductors.
   * $A$ = number of parallel paths ($A = 2$ for wave, $A = P$ for lap).
   * $r$ = radius of armature (m), $L$ = active conductor length (m).
   * $I_a$ = total armature current $\rightarrow$ current per conductor $= I_a / A$.
2. Force on each conductor:
   $$f_c = B \cdot \left(\frac{I_a}{A}\right) \cdot L$$
3. Average flux density:
   $$B = \frac{\text{Total Flux}}{\text{Core Surface Area}} = \frac{P \Phi}{2\pi r L}$$
4. Force on one conductor:
   $$f_c = \left(\frac{P \Phi}{2\pi r L}\right) \cdot \left(\frac{I_a}{A}\right) \cdot L = \frac{P \Phi I_a}{2\pi r A}$$
5. Torque developed by one conductor:
   $$T_c = f_c \times r = \frac{P \Phi I_a}{2\pi A}$$
6. Total torque for all $Z$ conductors:
   $$T = Z \times T_c = \frac{P Z \Phi I_a}{2\pi A} = \left(\frac{P Z}{2\pi A}\right) \Phi I_a$$
   $$\mathbf{T = k \Phi I_a}\quad \text{N}\cdot\text{m}$$
   *(where $k = \frac{P Z}{2\pi A}$ is a constant fixed by machine design).*

* **Reference in Mam Slide:** 226, 227
* **Reference in Firoz Note:** 86, 87
* **Reference in Rosenblatt:** Section 7-4, Pages 76-78
* **Reference in Theraja Vol II:** PDF Pages 144-145

---

### 23. Page 10, Q.7(d): A 400V, 25 hp, 450 rpm dc shunt motor is braked by plugging when running on full load. Determine the baking resistance necessary if the maximum braking current is not to exceed twice the full load current. Determine also the maximum braking torque when the motor is just reaching zero speed. The efficiency of the motor is 74.6% and the armature resistance is 0.2 Ω.

**Given Data:**
* $V = 400\text{ V}$, $P_{\text{out}} = 25\text{ hp} = 25 \times 746 = 18650\text{ W}$, $N = 450\text{ rpm}$.
* $\eta = 74.6\% = 0.746$, $R_a = 0.2\,\Omega$, $I_{\text{brake, max}} = 2 \times I_{\text{FL}}$.

**1. Full-Load Current ($I_{\text{FL}}$):**
$$P_{\text{in}} = \frac{P_{\text{out}}}{\eta} = \frac{18650}{0.746} = 25000\text{ W}$$
$$I_{\text{FL}} = \frac{P_{\text{in}}}{V} = \frac{25000}{400} = 62.5\text{ A}\quad (\approx I_{a\text{FL}})$$
$$I_{\text{brake, max}} = 2 \times 62.5 = 125\text{ A}$$

**2. Full-Load Back EMF ($E_b$):**
$$E_b = V - I_{\text{FL}} R_a = 400 - (62.5 \times 0.2) = 400 - 12.5 = 387.5\text{ V}$$

**3. Total Circuit Resistance during Plugging:**
* In plugging, terminal voltage is reversed, so net voltage is $V + E_b$:
  $$V_{\text{net}} = 400 + 387.5 = 787.5\text{ V}$$
  $$R_{\text{total}} = \frac{V + E_b}{I_{\text{brake, max}}} = \frac{787.5}{125} = 6.30\,\Omega$$
* **Braking Resistance Necessary ($R_{\text{ext}}$):**
  $$R_{\text{ext}} = R_{\text{total}} - R_a = 6.30 - 0.2 = \mathbf{6.10\,\Omega}$$

**4. Braking Torque at Zero Speed ($N = 0 \implies E_b = 0$):**
* At $N = 0$, net voltage is only $V = 400\text{ V}$:
  $$I_{a(\text{at zero speed})} = \frac{V}{R_{\text{total}}} = \frac{400}{6.30} = 63.49\text{ A}$$
* Full-load torque:
  $$T_{\text{FL}} = \frac{P_{\text{dev}}}{\omega} = \frac{E_b I_{\text{FL}}}{2\pi N / 60} = \frac{387.5 \times 62.5}{2\pi \times 450 / 60} = \frac{24218.75}{47.12} = 513.98\text{ N}\cdot\text{m}$$
* Since flux is constant, torque $\propto I_a$:
  $$T_{\text{brake(at zero speed)}} = T_{\text{FL}} \times \left(\frac{I_{a(0)}}{I_{\text{FL}}}\right) = 513.98 \times \left(\frac{63.49}{62.5}\right) = \mathbf{522.12\text{ N}\cdot\text{m}}$$

* **Reference in Mam Slide:** 288, 289
* **Reference in Firoz Note:** 118, 119
* **Reference in Rosenblatt:** Section 9-3, Pages 112-114
* **Reference in Theraja Vol II:** PDF Pages 176-178

---

### 24. Page 14, Q.3(b): Draw the load versus induced torque characteristic of different dc motors. [Figure Involved]

**Characteristic Summary:**
* **Shunt Motor:** Torque is directly proportional to armature current ($T \propto I_a$) because flux $\Phi$ is constant. The curve is a straight line through the origin.
* **Series Motor:** Before magnetic saturation, $\Phi \propto I_a$, so $T \propto I_a^2$ (parabolic curve). After saturation, $\Phi \approx \text{const}$, so $T \propto I_a$ (straight line).
* **Cumulative Compound Motor:** Torque curve lies between series and shunt. Series field adds flux as load increases, giving higher torque than shunt for the same current.
* **Differential Compound Motor:** Series field opposes shunt field, so $\Phi$ drops with load, resulting in lowest torque.

![[Pasted image 20260729015156.png]]
![[Pasted image 20260729023239.png]]
![[Screenshot_20260729-111713_WPS Office.png]]
![[Pasted image 20260729030609.png]]
![[Pasted image 20260729013256.png]]

* **Reference in Mam Slide:** 241, 246, 252
* **Reference in Firoz Note:** 92, 95, 101
* **Reference in Rosenblatt:** Sections 8-2, 8-4, 8-5, Pages 90-95
* **Reference in Theraja Vol II:** PDF Pages 152-154

---

### 25. Page 15, Q.4(c): A 230 V, 10 hp, dc shunt motor delivers power to a load at 1200 r/min. The armature current drawn by the motor is 200 A. The armature circuit resistance of the motor is 0.2 Ω and the field resistance is 115 Ω. If the rotational losses are 500 W, what is the value of load torque?

**Given Data:**
* $V = 230\text{ V}$, $N = 1200\text{ rpm}$, $I_a = 200\text{ A}$, $R_a = 0.2\,\Omega$, $R_f = 115\,\Omega$, $P_{\text{rot}} = 500\text{ W}$.

**1. Back EMF ($E_b$):**
$$E_b = V - I_a R_a = 230 - (200 \times 0.2) = 230 - 40 = 190\text{ V}$$

**2. Gross Developed Mechanical Power ($P_{\text{dev}}$):**
$$P_{\text{dev}} = E_b I_a = 190 \times 200 = 38000\text{ W}$$

**3. Useful Shaft Output Power ($P_{\text{shaft}}$):**
$$P_{\text{shaft}} = P_{\text{dev}} - P_{\text{rot}} = 38000 - 500 = 37500\text{ W}$$

**4. Load Torque ($T_{\text{load}}$):**
$$\omega = \frac{2\pi N}{60} = \frac{2\pi \times 1200}{60} = 40\pi \approx 125.66\text{ rad/s}$$
$$T_{\text{load}} = \frac{P_{\text{shaft}}}{\omega} = \frac{37500}{125.66} = \mathbf{298.42\text{ N}\cdot\text{m}}$$

* **Reference in Mam Slide:** 227, 228
* **Reference in Firoz Note:** 87, 88
* **Reference in Rosenblatt:** Section 7-7, Pages 82-84
* **Reference in Theraja Vol II:** PDF Pages 145-147

---

### 26. Page 16, Q.4(c): A dc series motor takes 40 A at 220 V and runs at 1000 rpm. If the armature and the field resistance are 0.2 Ω and 0.1 Ω respectively and the iron and friction losses are 500 W, find the torque developed in the armature. What will be the output of the motor?

**Given Data:**
* $V = 220\text{ V}$, $I_a = I_{se} = 40\text{ A}$, $N = 1000\text{ rpm}$, $R_a = 0.2\,\Omega$, $R_{se} = 0.1\,\Omega$, $P_{\text{rot}} = 500\text{ W}$.

**1. Back EMF ($E_b$):**
$$E_b = V - I_a (R_a + R_{se}) = 220 - 40 \times (0.2 + 0.1) = 220 - 12 = 208\text{ V}$$

**2. Developed Mechanical Power ($P_{\text{dev}}$):**
$$P_{\text{dev}} = E_b I_a = 208 \times 40 = 8320\text{ W}$$

**3. Torque Developed in Armature ($T_{\text{dev}}$):**
$$\omega = \frac{2\pi N}{60} = \frac{2\pi \times 1000}{60} \approx 104.72\text{ rad/s}$$
$$T_{\text{dev}} = \frac{P_{\text{dev}}}{\omega} = \frac{8320}{104.72} = \mathbf{79.45\text{ N}\cdot\text{m}}$$

**4. Net Output Power ($P_{\text{out}}$):**
$$P_{\text{out}} = P_{\text{dev}} - P_{\text{rot}} = 8320 - 500 = \mathbf{7820\text{ W}} = \mathbf{7.82\text{ kW}}\quad (\approx 10.48\text{ hp})$$

* **Reference in Mam Slide:** 227, 228
* **Reference in Firoz Note:** 87, 88
* **Reference in Rosenblatt:** Section 7-7, Pages 82-84
* **Reference in Theraja Vol II:** PDF Pages 145-147

---

### **6. Characteristics of a DC shunt motor**

### 28. Page 4, Q.58: Why the field circuit of dc motor should never be opened while power is applied to the motor?

**Consequence of Opening Shunt Field Circuit:**
* **Speed Equation:**
  $$N \propto \frac{E_b}{\Phi}$$
* When the field circuit is opened ($I_f \to 0$), the working flux drops instantly to only a very tiny **residual magnetism** ($\Phi_{\text{res}} \approx 0$).
* **Dangerous Runaway Speed:** Because $\Phi$ is in the denominator, the speed rushes to dangerously high levels ($N \to \infty$).
* **Mechanical Destruction:** The tremendous centrifugal forces shatter the armature windings, blow out the commutator bars, and destroy the bearings.
* **Severe Electrical Flashover:** Simultaneously, because the motor cannot immediately develop full speed, $E_b$ drops close to zero, causing an enormous short-circuit armature current ($I_a \approx V/R_a$) that trips breakers or burns out the commutator.

* **Reference in Mam Slide:** 244
* **Reference in Firoz Note:** 93, 94
* **Reference in Rosenblatt:** Section 8-3, Page 92
* **Reference in Theraja Vol II:** PDF Page 153

---

### 29. Page 5, Q.59: What will happen if the field of a dc shunt motor is disconnected on running condition?

**Two Immediate Outcomes:**
1. **On No-Load or Light Load:**
   * Flux collapses to residual flux ($\Phi \approx \Phi_{\text{res}}$).
   * Motor accelerates dangerously to an uncontrollable overspeed ("runaway" condition), risking complete mechanical disintegration due to centrifugal forces.
2. **On Full Load:**
   * The weak residual flux cannot develop sufficient torque ($T = k \Phi I_a$) to drive the heavy load.
   * The motor stalls or pulls up rapidly.
   * Since $N = 0 \implies E_b = 0$, the armature draws a massive stall current ($I_a = V/R_a$), causing heavy flashover at the brushes and burning out the armature within seconds unless disconnected.

* **Reference in Mam Slide:** 244
* **Reference in Firoz Note:** 93, 94
* **Reference in Rosenblatt:** Section 8-3, Page 92
* **Reference in Theraja Vol II:** PDF Page 153

---

### 30. Page 5, Q.66: Explain the effects on speed, counter emf, armature current and torque of a dc shunt motor when load applied to that motor.

**Sequence of Events when Load is Applied:**
1. **Speed ($N$):** Mechanical load increases $\rightarrow$ motor momentarily decelerates $\rightarrow$ **speed slightly drops** (typically by 3% to 5%).
2. **Counter EMF ($E_b$):** Since $E_b = k \Phi N$ and flux is constant, **$E_b$ decreases** proportionally with speed.
3. **Armature Current ($I_a$):** A small drop in $E_b$ produces a large increase in net driving voltage $(V - E_b)$:
   $$I_a = \frac{V - E_b}{R_a} \quad \implies \mathbf{I_a \text{ increases significantly}}$$
4. **Torque ($T$):** Because $T \propto \Phi I_a$, the increased current **boosts the electromagnetic torque** until it matches the new higher load torque, restoring steady equilibrium.

* **Reference in Mam Slide:** 242, 243
* **Reference in Firoz Note:** 92, 93
* **Reference in Rosenblatt:** Section 8-2, Pages 90-91
* **Reference in Theraja Vol II:** PDF Pages 151-152

---

### 31. Page 14, Q.3(a): A dc shunt motor operating from a constant voltage supply is running steadily on no-load. Explain how the motor will adjust itself on application of load.

**Self-Governing Mechanism:**
* **Initial State:** On no-load, motor runs at steady speed $N_0$ where $E_b \approx V$ and $I_a$ is just enough to overcome rotational losses.
* **Step 1 (Load Applied):** Load torque exceeds motor torque ($T_L > T$) $\rightarrow$ rotor slows down momentarily.
* **Step 2 (Drop in Back EMF):** Speed decrease reduces back EMF ($E_b \propto N$).
* **Step 3 (Surge in Armature Current):** The drop in $E_b$ increases $(V - E_b)$, causing $I_a = \frac{V - E_b}{R_a}$ to increase sharply.
* **Step 4 (Torque Balance):** The larger $I_a$ generates larger torque ($T = k \Phi I_a$) until $T = T_L$.
* The motor settles at a new steady speed only slightly lower than no-load speed (making it practically a constant-speed motor).

* **Reference in Mam Slide:** 242, 243
* **Reference in Firoz Note:** 92, 93
* **Reference in Rosenblatt:** Section 8-2, Pages 90-91
* **Reference in Theraja Vol II:** PDF Pages 151-152

---

### **7. Characteristics of a DC series motor**

### 33. Page 5, Q.60: Explain why the series motor must be started with a mechanical load coupled to its armature.

**Reason:**
* In a DC series motor, the field winding is in series with the armature, so field flux is proportional to load current: $\Phi \propto I_a$.
* **Speed Relationship:**
  $$N \propto \frac{E_b}{\Phi} \approx \frac{V}{k I_a}$$
* **At No-Load:** The motor draws only a tiny no-load current ($I_a \approx 0$).
* This makes the flux $\Phi$ extremely small (residual flux only).
* Consequently, the speed accelerates to **dangerously high, destructive levels** ($N \to \infty$).
* **Conclusion:** To prevent mechanical disintegration from runaway speed, a series motor must **always** be mechanically coupled (via gears or direct coupling, never a belt that could slip) to its load before starting.

* **Reference in Mam Slide:** 248, 249
* **Reference in Firoz Note:** 97, 98
* **Reference in Rosenblatt:** Section 8-4, Pages 93-95
* **Reference in Theraja Vol II:** PDF Pages 153-154

---

### 34. Page 5, Q.61: Why a dc series motor shaft should be firmly coupled with its load?

**Key Reasons:**
* **Runaway Prevention:** If the load becomes disconnected (e.g., if a belt breaks or slips off), the motor loses its load, $I_a$ drops to almost zero, and the motor runs away to destructive overspeed.
* **Solid Mechanical Drive:** Direct solid coupling (flange coupling) or positive gear drive ensures that the motor can never operate in an uncoupled, zero-load state.
* **High Starting Torque Transfer:** Because series motors generate tremendous starting torque ($T \propto I_a^2$), friction belts would easily slip, burn, or break.

* **Reference in Mam Slide:** 248, 249
* **Reference in Firoz Note:** 97, 98
* **Reference in Rosenblatt:** Section 8-4, Pages 93-95
* **Reference in Theraja Vol II:** PDF Pages 153-154

---

### 35. Page 5, Q.62: “Series motors are never used unless they are directly connected to load”-why?

**Explanation:**
* As established by $N \propto \frac{V - I_a R}{\Phi}$, when $I_a$ is very small, $\Phi \to \Phi_{\text{res}}$, driving $N \to \infty$.
* Centrifugal force on the rotor is proportional to $N^2$. At runaway speeds:
  * Commutator segments lift and fly out.
  * Armature copper windings burst out of their slots.
  * Shaft bends and bearings seize.
* Therefore, safety regulations mandate that series motors must be permanently geared or directly coupled to their load, and must never use belt or friction clutch drives.

* **Reference in Mam Slide:** 248, 249
* **Reference in Firoz Note:** 97, 98
* **Reference in Rosenblatt:** Section 8-4, Pages 93-95
* **Reference in Theraja Vol II:** PDF Pages 153-154

---

### 36. Page 5, Q.63: Derive the terminal characteristics of a dc series motor. Explain with necessary figures, why these types of motors are suitable for starting high inertia load. [Figure Involved]

**1. Derivation of Speed-Torque Terminal Characteristic:**
* Voltage equation: $V = E_b + I_a (R_a + R_{se})$.
* Back EMF: $E_b = k_1 \Phi \omega$.
* Before magnetic saturation: $\Phi = k_2 I_a$.
* Torque: $T = k_1 \Phi I_a = k_1 k_2 I_a^2 \implies I_a = \sqrt{\frac{T}{k_1 k_2}}$.
* Substitute into voltage equation:
  $$V = k_1 (k_2 I_a) \omega + I_a R_{\text{total}} = k_1 k_2 \sqrt{\frac{T}{k_1 k_2}} \omega + \sqrt{\frac{T}{k_1 k_2}} R_{\text{total}}$$
* Rearranging for speed ($\omega$):
  $$\omega = \frac{V}{\sqrt{k_1 k_2} \sqrt{T}} - \frac{R_{\text{total}}}{k_1 k_2}$$
* This yields a **hyperbolic** speed-torque characteristic: as torque increases, speed drops sharply; at small torque, speed approaches infinity.

**2. Why Suitable for High-Inertia Loads:**
* Accelerating heavy inertia requires massive starting torque ($T_{\text{accel}} = J \frac{d\omega}{dt}$).
* In series motors, $T \propto I_a^2$. Drawing twice the rated current produces **four times the rated torque**.
* It provides enormous breakaway torque without drawing excessively high current compared to other motor types, making it ideal for cranes, trains, and hoists.

* **Reference in Mam Slide:** 247, 248, 250
* **Reference in Firoz Note:** 96, 97, 99
* **Reference in Rosenblatt:** Section 8-4, Pages 93-95
* **Reference in Theraja Vol II:** PDF Pages 153-155

---

### 37. Page 15, Q.4(a): What are the principle characteristics of a dc series motor? What are its uses?

**1. Principal Characteristics:**
* **Torque vs Armature Current ($T\text{-}I_a$):**
  * Before saturation: $T \propto I_a^2$ (parabolic rise).
  * After saturation: $T \propto I_a$ (linear rise).
* **Speed vs Armature Current ($N\text{-}I_a$):**
  * $N \propto \frac{1}{I_a}$ (inverse hyperbolic curve). Speed drops drastically as load increases.
* **Speed vs Torque ($N\text{-}T$):**
  * High torque at low speed; dangerous overspeed at zero torque.

**2. Uses:**
* Traction systems (locomotives, trams, subways, trolleybuses).
* Cranes, hoists, winches, conveyors, and vehicle starters.

* **Reference in Mam Slide:** 246, 247, 252
* **Reference in Firoz Note:** 95, 96, 101
* **Reference in Rosenblatt:** Sections 8-4, 8-5, Pages 93-95
* **Reference in Theraja Vol II:** PDF Pages 153-155

---

### **8. Characteristics of a DC compound motor / All DC Motors**

### 39. Page 5, Q.64: Explain briefly speed versus armature current and torque versus armature current characteristics of all dc motors.

**1. Speed vs Armature Current ($N\text{-}I_a$):**
* **Shunt Motor:** Speed drops only slightly (3–5%) from no-load to full-load due to small $I_a R_a$ drop ($\Phi \approx \text{const}$).
* **Series Motor:** Speed drops sharply in an inverse curve as $I_a$ increases ($N \propto 1/I_a$); dangerously high speed at small $I_a$.
* **Cumulative Compound:** Speed drops more than shunt but less than series because series flux adds to shunt flux.
* **Differential Compound:** Speed actually rises with load because series flux opposes shunt flux, weakening net field.

**2. Torque vs Armature Current ($T\text{-}I_a$):**
* **Series Motor:** Curve starts as a parabola ($T \propto I_a^2$) and becomes linear after saturation. Highest starting torque.
* **Cumulative Compound:** Rises faster than shunt motor due to adding series field flux.
* **Shunt Motor:** Perfectly straight line ($T \propto I_a$) since $\Phi$ is constant.
* **Differential Compound:** Lowest torque curve; series field subtracts flux, causing torque to flatten or drop.

* **Reference in Mam Slide:** 254, 255
* **Reference in Firoz Note:** 103, 104
* **Reference in Rosenblatt:** Section 8-7, Pages 97-98
* **Reference in Theraja Vol II:** PDF Pages 154-156

---

### 40. Page 5, Q.65: Draw and explain the mechanical characteristics of DC series and shunt motor. [Figure Involved]

**Explanation of Mechanical Characteristics ($N\text{ vs }T$):**
* **DC Shunt Motor:**
  * Speed equation: $N = \frac{V - I_a R_a}{k \Phi}$.
  * Since flux is constant and $T \propto I_a$: $N = N_0 - m T$.
  * The curve is a slightly drooping straight line (speed regulation 5–8%).
* **DC Series Motor:**
  * Speed equation: $N \propto \frac{1}{\sqrt{T}}$.
  * The curve is a rectangular hyperbola: very high speed at light loads, dropping steadily as torque increases.

```
Speed (N)
▲
│ Shunt Motor (Nearly Constant Speed)
│ ──────────────────────────────
│       Series Motor (Hyperbolic)
│ ──┐
│   │
│    \
│     \───────►
└────────────────────────► Torque (T)
```

* **Reference in Mam Slide:** 243, 247
* **Reference in Firoz Note:** 93, 96
* **Reference in Rosenblatt:** Sections 8-2, 8-4, Pages 90-94
* **Reference in Theraja Vol II:** PDF Pages 152-154

---

### 41. Page 9, Q.6(a): Draw and explain the torque and speed characteristic of shunt motor, cumulative compound motor and differential compound motor. [Figure Involved]

**Summary Comparison:**
1. **Speed vs Load ($N\text{-}I_a$ or $N\text{-}T$):**
   * **Differential Compound:** Speed rises with load (negative speed regulation) $\rightarrow$ prone to unstable hunting.
   * **Shunt:** Slight drop in speed (stable constant-speed operation).
   * **Cumulative Compound:** Noticeable drop in speed with load, ensuring high stability against shock loads.
2. **Torque vs Load ($T\text{-}I_a$):**
   * **Cumulative Compound:** Produces high torque ($T \propto (\Phi_{sh} + \Phi_{se})I_a$) for heavy starting loads without overspeeding at no-load.
   * **Shunt:** Linear torque ($T \propto \Phi_{sh} I_a$).
   * **Differential Compound:** Produces poor torque ($T \propto (\Phi_{sh} - \Phi_{se})I_a$).

* **Reference in Mam Slide:** 254, 255
* **Reference in Firoz Note:** 103, 104
* **Reference in Rosenblatt:** Section 8-7, Pages 97-98
* **Reference in Theraja Vol II:** PDF Pages 154-156

---

### 42. Page 14, Q.3(a): Draw speed versus armature current and torque versus armature current characteristics of all DC motors. [Figure Involved]

* **Speed vs Armature Current:** Shunt (flat, slight droop) > Cumulative Compound (moderate droop) > Series (steep hyperbolic droop). Differential compound rises above shunt.
* **Torque vs Armature Current:** Series (steepest, $T \propto I_a^2$) > Cumulative Compound > Shunt (linear straight line) > Differential Compound (lowest).

* **Reference in Mam Slide:** 254, 255
* **Reference in Firoz Note:** 103, 104
* **Reference in Rosenblatt:** Section 8-7, Pages 97-98
* **Reference in Theraja Vol II:** PDF Pages 154-156

---

### **9. Speed of a DC machine**

### 44. Page 8, Q.7(b): Define the base speed of a dc motor. Describe how motor speed can be decreased and increased from the base speed.

**1. Definition of Base Speed:**
* **Base Speed** is the rated operating speed of a DC motor at rated armature voltage, rated field current, and rated full load.

**2. Speed Adjustment:**
* General speed equation:
  $$N = \frac{V - I_a R_a}{k \Phi}$$
* **To Decrease Speed (Below Base Speed):**
  * **Armature Voltage Control:** Reduce the voltage applied to the armature while keeping field flux $\Phi$ at its rated maximum. This provides constant torque capability.
  * **Armature Resistance Control:** Add external resistance in series with armature circuit (inefficient due to heat losses).
* **To Increase Speed (Above Base Speed):**
  * **Field Weakening Control:** Insert resistance in the shunt field circuit to reduce $I_f$ and weaken flux $\Phi$. Since $N \propto 1/\Phi$, speed increases above base speed (constant power capability).

* **Reference in Mam Slide:** 260, 261, 262
* **Reference in Firoz Note:** 108, 109, 110
* **Reference in Rosenblatt:** Sections 9-1, 9-2, Pages 104-108
* **Reference in Theraja Vol II:** PDF Pages 160-162

---

### 45. Page 9, Q.5(c): What is meant by negative speed regulation? Which motor exhibits negative speed regulation?

**1. Definition of Negative Speed Regulation:**
* Speed regulation is defined as:
  $$\% \text{ Speed Regulation} = \frac{N_{\text{no-load}} - N_{\text{full-load}}}{N_{\text{full-load}}} \times 100$$
* A **negative speed regulation** occurs when the motor's full-load speed is **higher** than its no-load speed ($N_{\text{FL}} > N_{\text{NL}}$).

**2. Which Motor Exhibits It:**
* The **Differential Compound DC Motor**.
* *Reason:* The series field opposes the shunt field ($\Phi_{\text{net}} = \Phi_{sh} - \Phi_{se}$). As load current $I_a$ increases, the series demagnetizing mmf increases, weakening the total flux $\Phi_{\text{net}}$. Because $N \propto 1/\Phi_{\text{net}}$, the reduction in flux causes the motor speed to rise with load.

* **Reference in Mam Slide:** 254
* **Reference in Firoz Note:** 103, 104
* **Reference in Rosenblatt:** Section 8-7, Page 98
* **Reference in Theraja Vol II:** PDF Page 155

---

### **10. Speed control of DC motors (and Braking)**

### 47. Page 5, Q.75: Name the different methods of electrical breaking of dc motors and explain.

**Three Methods of Electric Braking:**
1. **Regenerative Braking:**
   * Motor speed rises above no-load speed (e.g., train going downhill) $\rightarrow E_b > V$.
   * Armature current reverses direction ($I_a = \frac{E_b - V}{R_a}$).
   * The machine behaves as a generator and feeds electrical power back into the supply grid, creating retarding braking torque.
2. **Dynamic (Rheostatic) Braking:**
   * The armature is disconnected from the supply mains and reconnected across a variable braking resistor ($R_B$), while the field remains energized.
   * Kinetic energy of the rotating rotor is converted into electrical energy and dissipated as heat in $R_B$.
3. **Plugging (Reverse Current Braking):**
   * Armature terminal connections are suddenly reversed while motor is running.
   * Net voltage across armature becomes $V + E_b \approx 2V$.
   * A large braking resistor is inserted to limit current.
   * Generates powerful braking torque to bring motor to a quick stop.

* **Reference in Mam Slide:** 284, 285, 286, 287
* **Reference in Firoz Note:** 115, 116, 117, 118
* **Reference in Rosenblatt:** Section 9-3, Pages 110-114
* **Reference in Theraja Vol II:** PDF Pages 174-177

---

### 48. Page 5, Q.76: Explain the different methods used for the speed control of D.C. shunt motor.

**Methods of Speed Control:**
1. **Flux Control (Field Weakening):**
   * Variable rheostat connected in series with shunt field winding.
   * Increasing resistance lowers $I_f \rightarrow$ weakens $\Phi \rightarrow$ increases speed above base speed ($N \propto 1/\Phi$).
   * High efficiency, small rheostat, constant-power drive.
2. **Armature Rheostatic Control:**
   * Variable resistance inserted in series with the armature.
   * Increases armature voltage drop $I_a R_{\text{ext}} \rightarrow$ reduces voltage across armature terminals $\rightarrow$ decreases speed below base speed.
   * Disadvantage: High power loss in resistor ($I_a^2 R_{\text{ext}}$), poor speed regulation.
3. **Armature Voltage Control (Ward-Leonard System):**
   * Supplies variable DC voltage to the armature from an adjustable generator.
   * Provides smooth, highly efficient speed control from zero to base speed in both directions.

* **Reference in Mam Slide:** 260, 261, 262, 263
* **Reference in Firoz Note:** 108, 109, 110, 111
* **Reference in Rosenblatt:** Sections 9-1, 9-2, Pages 104-108
* **Reference in Theraja Vol II:** PDF Pages 160-164

---

### 49. Page 5, Q.77: Why in a dc shunt motor speed adjustment below the rated one is not done using field current control and above the rated one is not done using armature voltage control?

**Why Not Below Rated Using Field Control:**
* To reduce speed below base speed via field control, one must *increase* flux $\Phi$ ($N \propto 1/\Phi$).
* Increasing flux requires significantly higher field current ($I_f$).
* However, the iron core is already magnetically saturated at rated field current. Attempting to force higher current causes **heavy core saturation**, overheating, and potential insulation burnout of the field coils with virtually zero increase in flux.

**Why Not Above Rated Using Armature Voltage Control:**
* To raise speed above base speed via voltage control, applied armature voltage $V_a$ must be increased above rated voltage ($N \propto V_a$).
* Exceeding rated voltage stresses the winding insulation beyond its dielectric rating, risking **insulation breakdown, flashover at commutator segments, and dielectric failure**.

* **Reference in Mam Slide:** 261, 263
* **Reference in Firoz Note:** 109, 111
* **Reference in Rosenblatt:** Section 9-2, Pages 106-108
* **Reference in Theraja Vol II:** PDF Pages 161, 164

---

### 50. Page 5, Q.78: Explain why inserting a resistor in series with the armature of a dc motor causes a decrease in speed.

**Explanation:**
1. Speed equation:
   $$N = \frac{V - I_a (R_a + R_{\text{ext}})}{k \Phi}$$
2. Adding external resistor $R_{\text{ext}}$ in the armature circuit causes an additional ohmic voltage drop $I_a R_{\text{ext}}$.
3. The net voltage available across the armature is reduced to $V' = V - I_a R_{\text{ext}}$.
4. This directly lowers the back EMF ($E_b = V' - I_a R_a$).
5. Since $N \propto E_b$ (with constant flux $\Phi$), the motor must slow down to maintain equilibrium at the lower back EMF.

* **Reference in Mam Slide:** 261
* **Reference in Firoz Note:** 109
* **Reference in Rosenblatt:** Section 9-1, Pages 104-105
* **Reference in Theraja Vol II:** PDF Page 160

---

### 51. Page 5, Q.79: What are the factors that control the speed of a dc motor? Explain Ward-Leonard system to control speed of a dc motor.

**1. Factors Controlling Speed:**
* From $N = \frac{V - I_a R_a}{k \Phi}$:
  1. **Applied Armature Voltage ($V$):** Speed is directly proportional to armature voltage.
  2. **Armature Circuit Resistance ($R_a$):** Higher resistance reduces net voltage and decreases speed.
  3. **Field Flux ($\Phi$):** Speed is inversely proportional to magnetic flux.

**2. Ward-Leonard System:**
* **Setup:** Consists of an AC drive motor driving a variable-voltage DC generator, which directly feeds the armature of the main DC motor. Both generator and motor fields are separately excited from an independent exciter.
* **Operation Below Base Speed:** Keep the motor field flux at maximum; vary generator field current to smoothly change generator output voltage from $0$ to rated $V$. Motor speed varies smoothly from $0$ to base speed with constant torque.
* **Operation Above Base Speed:** Keep armature voltage at rated maximum; weaken the main motor field to achieve speeds above base speed with constant power.
* **Reversal:** Reversing generator field current reverses generator output polarity, smoothly reversing motor rotation without any power contactors.

* **Reference in Mam Slide:** 264, 265
* **Reference in Firoz Note:** 112, 113
* **Reference in Rosenblatt:** Section 9-2, Pages 108-110
* **Reference in Theraja Vol II:** PDF Pages 164-166

---

### 52. Page 6, Q.80: Explain how the speed of dc motor can be controlled by using thyristor.

**Operation:**
* **Thyristor Phase-Controlled Converter:** Connects between AC mains and the DC motor armature.
* **Phase-Angle Triggering:** By adjusting the thyristor firing angle ($\alpha$), the average DC output voltage is controlled:
  * For 1-phase fully-controlled bridge: $V_{\text{dc}} = \frac{2 V_m}{\pi} \cos\alpha$.
* **Speed Variation:** Changing $\alpha$ from $0^\circ$ to $90^\circ$ smoothly varies the armature terminal voltage from maximum to zero, thereby controlling motor speed below base speed ($N \propto V_{\text{dc}}$).
* **Advantages:** Compact solid-state system, high efficiency (no large resistor losses), fast dynamic response, easily automated with microcontrollers.

* **Reference in Mam Slide:** Power Electronics / Speed Control Section
* **Reference in Firoz Note:** 113
* **Reference in Rosenblatt:** Chapter 10, Pages 120-130
* **Reference in Theraja Vol II:** PDF Pages 168-170

---

### 53. Page 10, Q.7(b): Distinguish between electric braking and mechanical breaking.

| Feature | Electric Braking | Mechanical Braking |
| :--- | :--- | :--- |
| **Braking Mechanism** | Motor acts as generator; converts kinetic energy into electrical energy. | Friction pads/shoes press against a rotating brake drum or disc. |
| **Wear and Tear** | No physical friction $\rightarrow$ practically zero mechanical wear. | High mechanical wear on brake linings; requires frequent maintenance. |
| **Heat Dissipation** | Dissipated in external resistors or regenerated back to grid. | Heat generated directly at brake drum/shoes, risking overheating. |
| **Holding at Rest** | Cannot hold a stopped load at rest (torque drops as speed $\to 0$). | Can securely hold a stationary load at rest (parking brake). |
| **Smoothness** | Exceptionally smooth, continuous, easily controlled. | Rougher, jerky, prone to mechanical shock and skidding. |

* **Reference in Mam Slide:** 284
* **Reference in Firoz Note:** 115
* **Reference in Rosenblatt:** Section 9-3, Page 110
* **Reference in Theraja Vol II:** PDF Page 174

---

### 54. Page 14, Q.4(c): Explain the field weakening method used for the speed control of DC shunt motor.

**Principle:**
* Speed is inversely proportional to flux: $N \propto \frac{1}{\Phi}$.
* A variable rheostat ($R_{\text{field}}$) is inserted in series with the shunt field winding.
* **Procedure:**
  1. Increasing $R_{\text{field}}$ decreases the field current: $I_f = \frac{V}{R_f + R_{\text{field}}}$.
  2. Lower $I_f$ reduces the working field flux ($\Phi$).
  3. Lower $\Phi$ momentarily reduces $E_b$, causing a surge in $I_a$ that produces accelerating torque until speed rises to a new higher equilibrium.
* **Key Traits:** Provides speed control **above base speed**; operates in the **constant power** mode ($T \propto \Phi \downarrow$ while $N \uparrow$); highly efficient since field current is only 2–5% of total current.

* **Reference in Mam Slide:** 260
* **Reference in Firoz Note:** 108
* **Reference in Rosenblatt:** Section 9-1, Pages 105-106
* **Reference in Theraja Vol II:** PDF Pages 161-162

---

### 55. Page 15, Q.4(b): Explain two common ways in which the speed of a dc shunt motor is controlled.

**Two Common Methods:**
1. **Field Control Method (Flux Weakening):**
   * Adjusts series rheostat in the shunt field circuit to change flux $\Phi$.
   * Used for speeds **above rated speed**.
   * Highly efficient, economical, constant-power drive.
2. **Armature Voltage Control Method:**
   * Adjusts the DC terminal voltage applied to the armature circuit (via variable source or thyristor converter) while keeping field flux at maximum.
   * Used for speeds **from zero up to rated speed**.
   * Excellent speed regulation, high efficiency, constant-torque drive.

* **Reference in Mam Slide:** 260, 263
* **Reference in Firoz Note:** 108, 111
* **Reference in Rosenblatt:** Sections 9-1, 9-2, Pages 104-108
* **Reference in Theraja Vol II:** PDF Pages 160-164

---

### 56. Page 15, Q.4(c): A 250 V dc shunt motor has armature resistance of 0.25 Ω. It takes an armature current of 50 A while running with a load at 750 rpm. To change the speed of the motor, the main field flux is reduced by 10% by changing the motor shunt field resistance. What will be the new speed of the motor?

**Given Data:**
* $V = 250\text{ V}$, $R_a = 0.25\,\Omega$, $I_{a1} = 50\text{ A}$, $N_1 = 750\text{ rpm}$.
* $\Phi_2 = 0.90\,\Phi_1$ (flux reduced by 10%).

**1. Initial Back EMF ($E_{b1}$):**
$$E_{b1} = V - I_{a1} R_a = 250 - (50 \times 0.25) = 250 - 12.5 = 237.5\text{ V}$$

**2. New Armature Current ($I_{a2}$):**
* Assuming constant load torque ($T_1 = T_2$):
  $$T \propto \Phi I_a \implies \Phi_1 I_{a1} = \Phi_2 I_{a2}$$
  $$I_{a2} = I_{a1} \times \left(\frac{\Phi_1}{\Phi_2}\right) = \frac{50}{0.90} \approx 55.56\text{ A}$$

**3. New Back EMF ($E_{b2}$):**
$$E_{b2} = V - I_{a2} R_a = 250 - (55.56 \times 0.25) = 250 - 13.89 = 236.11\text{ V}$$

**4. New Speed ($N_2$):**
$$\frac{N_2}{N_1} = \left(\frac{E_{b2}}{E_{b1}}\right) \times \left(\frac{\Phi_1}{\Phi_2}\right)$$
$$N_2 = 750 \times \left(\frac{236.11}{237.5}\right) \times \left(\frac{1}{0.90}\right) = 750 \times 0.9941 \times 1.1111 = \mathbf{828.46\text{ rpm}}$$

* **Reference in Mam Slide:** 260, 261
* **Reference in Firoz Note:** 108, 109
* **Reference in Rosenblatt:** Section 9-1, Pages 105-106
* **Reference in Theraja Vol II:** PDF Pages 161-163

---

### 57. Page 16, Q.4(b): When the Ward Leonard System of speed control is used, why should the shunt fields be connected to a separate supply source?

**Reasons:**
* **Stable Field Flux:** If the main motor field were excited from the variable generator voltage, reducing generator voltage to slow the motor would simultaneously weaken the motor field, defeating the constant-torque armature voltage control.
* **Full Flux at Low Speeds:** A separate constant-voltage exciter guarantees the motor field remains at its rated maximum regardless of armature voltage, providing maximum torque capability at zero and low speeds.
* **Independent Control:** Allows independent field weakening of the motor for speeds above base speed, and clean polarity reversal of the generator field for reversing rotation.

* **Reference in Mam Slide:** 264, 265
* **Reference in Firoz Note:** 112, 113
* **Reference in Rosenblatt:** Section 9-2, Pages 108-110
* **Reference in Theraja Vol II:** PDF Pages 164-166

---

### 58. Page 28, Q.No.1: What are the merits and demerits of field control method for dc motor speed control?

**Merits:**
* **High Efficiency:** Field current is very small (2–5% of full-load current), so power losses in the field rheostat are negligible.
* **Compact & Cheap Equipment:** Small, inexpensive rheostat since it handles minimal current.
* **Smooth Speed Control:** Provides smooth, stepless speed adjustment above base speed.
* **Good Speed Regulation:** Speed remains relatively stable with changing load.

**Demerits:**
* **Only Above Base Speed:** Cannot reduce speed below rated base speed.
* **Commutation Difficulties:** Weakening the main flux magnifies the distorting effect of armature reaction, causing severe brush sparking at higher speeds.
* **Mechanical Speed Limit:** High centrifugal stresses limit how fast the motor can safely spin.
* **Reduced Torque:** Because $\Phi$ is reduced, torque capacity drops ($T \propto \Phi$).

* **Reference in Mam Slide:** 260
* **Reference in Firoz Note:** 108
* **Reference in Rosenblatt:** Section 9-1, Pages 105-106
* **Reference in Theraja Vol II:** PDF Pages 161-162

---

### 59. Page 28, Q.No.2: Prove that plugging provide more braking torque then dynamic braking.

**Proof:**
1. **Dynamic Braking:**
   * Armature is disconnected from supply $V$ and closed across resistor $R_B$.
   * Net voltage driving braking current:
     $$V_{\text{dyn}} = E_b$$
   * Braking current: $I_{\text{brake(dyn)}} = \frac{E_b}{R_a + R_B}$.
   * Initial braking torque:
     $$T_{\text{dyn}} \propto \Phi \cdot \left(\frac{E_b}{R_a + R_B}\right)$$

2. **Plugging (Reverse Current Braking):**
   * Supply polarity to armature is reversed while motor is running.
   * Net voltage driving braking current:
     $$V_{\text{plug}} = V + E_b$$
   * Braking current: $I_{\text{brake(plug)}} = \frac{V + E_b}{R_a + R_{\text{ext}}}$.
   * Initial braking torque:
     $$T_{\text{plug}} \propto \Phi \cdot \left(\frac{V + E_b}{R_a + R_{\text{ext}}}\right)$$

3. **Comparison:**
   * Because $V \approx E_b$, the driving voltage during plugging is roughly twice that of dynamic braking:
     $$V_{\text{plug}} = V + E_b \approx 2 E_b = 2 \times V_{\text{dyn}}$$
   * For the same total circuit resistance, $I_{\text{brake(plug)}} \approx 2 \times I_{\text{brake(dyn)}}$.
   * Therefore, **plugging produces roughly double the initial braking torque** of dynamic braking ($T_{\text{plug}} > T_{\text{dyn}}$).

* **Reference in Mam Slide:** 286, 287
* **Reference in Firoz Note:** 116, 117
* **Reference in Rosenblatt:** Section 9-3, Pages 111-114
* **Reference in Theraja Vol II:** PDF Pages 175-177

---

### **11. Starting of DC motors**

### 61. Page 4, Q.57: What will happen if a shunt motor is directly connected to the supply line?

**Consequences of Direct Starting:**
* At the moment of starting, rotor speed is zero ($N = 0$), so back EMF is zero ($E_b = 0$).
* Initial starting current is limited only by armature resistance:
  $$I_{a(\text{start})} = \frac{V - 0}{R_a} = \frac{V}{R_a}$$
* Since $R_a$ is very small (often $< 0.5\,\Omega$), $I_{a(\text{start})}$ reaches **15 to 30 times rated full-load current**.
* **Direct Results:**
  1. Excessive $I^2R$ heating burns out armature winding insulation within seconds.
  2. Severe arcing and mechanical pitting destroy the commutator segments and carbon brushes.
  3. Enormous initial torque shock shears shafts, gears, or couplings.
  4. Large supply voltage dip trips circuit breakers and disrupts other equipment on the power line.

* **Reference in Mam Slide:** 266, 267
* **Reference in Firoz Note:** 114
* **Reference in Rosenblatt:** Section 9-4, Pages 114-115
* **Reference in Theraja Vol II:** PDF Pages 170-171

---

### 62. Page 14, Q.4(b): A dc motor fails to start when switched ON. What could be the best possible reasons and remedies?

| Potential Cause | Practical Remedy |
| :--- | :--- |
| **Blown Fuse or Tripped Circuit Breaker** | Replace fuse with correct rating or reset breaker after checking for short circuits. |
| **Open Circuit in Starting Resistor / Starter** | Inspect starter studs and faceplate resistance coils; repair broken wire. |
| **Brushes Not Seated or Stuck in Holders** | Clean brush holders, free jammed brushes, check spring tension, and reseat brushes. |
| **Open Shunt Field Circuit** | Test field continuity; reconnect broken lead to prevent runaway risk. |
| **Excessive Mechanical Overload or Jammed Rotor** | Disconnect load coupling; turn shaft by hand to check for mechanical seizure or bearing failure. |
| **Severe Low Supply Voltage** | Measure terminal voltage with voltmeter; restore rated voltage. |

* **Reference in Mam Slide:** Troubleshooting Section
* **Reference in Rosenblatt:** Chapter 14, Pages 220-225

---

### **12. Three point and four point starter with its advantages and disadvantages**

### 64. Page 5, Q.72: What are the purposes of starter used in a dc motor? Describe the working of the three-point starter for DC shunt motor with neat diagram. [Figure Involved]

**1. Purposes of a Starter:**
* Inserts external resistance in series with armature at start to restrict starting current to safe limits ($1.5 \times I_{\text{FL}}$).
* Progressively cuts out resistance as motor accelerates and builds up back EMF ($E_b$).
* Incorporates safety protection: **No-Volt Coil (NVC)** against line voltage failure, and **Overload Release (OLR)** against excessive load.

**2. Working of 3-Point Starter:**
* **Terminals:** Three external terminals: Line ($L$), Field ($F$), Armature ($A$).
* **Starting:** Moving the starting handle from OFF to stud 1 puts full starting resistance in series with armature, while field gets full voltage.
* **Running:** As motor speeds up, handle is moved across studs, gradually cutting out resistance.
* **Hold Position:** At final stud, handle is held magnetically against a spring by the NVC (electromagnet in series with shunt field).
* **Release:** If supply voltage fails, NVC demagnetizes and the spring snaps the handle back to OFF.

![[Pasted image 20260729083801.jpg]]
![[Pasted image 20260729084236.png]]

* **Reference in Mam Slide:** 268, 269
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 115-117
* **Reference in Theraja Vol II:** PDF Pages 171-173

---

### 65. Page 5, Q.73: Which characteristics of three-point starter make it unpopular? How those problems can be resolved using four-point starter?

**1. Drawback of 3-Point Starter:**
* The No-Volt Coil (NVC) is wired in **direct series** with the shunt field winding.
* When the motor speed is increased above base speed by weakening the field (increasing field rheostat resistance), field current $I_f$ drops significantly.
* The weak current reduces the magnetic pull of the NVC.
* The spring overpowers the weak magnet and **accidently releases the handle back to OFF**, shutting down the running motor.

**2. Solution with 4-Point Starter:**
* Separates the NVC circuit from the field winding circuit.
* Creates a 4th terminal ($N$), wiring the NVC in an **independent parallel circuit** with its own protective resistor directly across the supply line.
* Any changes to the field current rheostat now have zero effect on the current flowing through the NVC.

![[Pasted image 20260729085814.jpg]]

* **Reference in Mam Slide:** 270, 271
* **Reference in Firoz Note:** 115
* **Reference in Rosenblatt:** Section 9-4, Pages 117-119
* **Reference in Theraja Vol II:** PDF Pages 173-174

---

### 66. Page 5, Q.74: Name Different types of starters.

**Types of DC Motor Starters:**
1. **Manual Starters:**
   * **Two-Point Starter:** Used exclusively for DC series motors.
   * **Three-Point Starter:** Used for DC shunt and cumulative compound motors.
   * **Four-Point Starter:** Used for variable-speed DC shunt/compound motors (with field rheostats).
2. **Automatic Starters:**
   * Counter-EMF (voltage-drop) accelerated starters.
   * Current-limit (series relay) accelerated starters.
   * Definite time-delay contactor starters.

![[Pasted image 20260729090917.png]]
![[Pasted image 20260729092319.png]]
![[Pasted image 20260729092231.png]]

* **Reference in Mam Slide:** 268, 270, 272
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 115-120
* **Reference in Theraja Vol II:** PDF Pages 171-174

---

### 67. Page 8, Q.7(a): Explain how a 3-point starter can be used to start a DC motor with low speed but high starting torque

**Explanation:**
* **Low Starting Speed:** On stud 1, the entire series resistance is inserted in the armature circuit, creating a large $I_a R_{\text{start}}$ drop that restricts the armature voltage, holding initial speed low.
* **High Starting Torque:**
  * In the 3-point starter, the shunt field circuit is connected directly to the incoming supply line ahead of the armature resistance.
  * Thus, the shunt field receives full rated terminal voltage from the instant of startup, establishing **full maximum field flux ($\Phi_{\text{max}}$)**.
  * Since $T = k \Phi I_a$, combining full flux with controlled starting current ($1.5 \times I_{\text{FL}}$) produces **maximum permissible starting torque** at low initial speed.

* **Reference in Mam Slide:** 268, 269
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 115-117
* **Reference in Theraja Vol II:** PDF Pages 171-173

---

### 68. Page 9, Q.6(b): Why starter is required for DC motor? What is the drawback of three point starter? Explain how this drawback can be overcome in four point starter.

**1. Why Starter is Required:**
* At standstill ($N = 0 \implies E_b = 0$). Low armature resistance ($R_a$) would allow destructive inrush currents ($I_a = V/R_a = 15\text{–}30 \times I_{\text{FL}}$), burning windings and commutator.
* A starter limits this inrush current to safe levels ($1.25\text{–}1.5 \times I_{\text{FL}}$).

**2. Drawback of 3-Point Starter:**
* NVC is in series with the field winding. Weakening field current for high-speed operation demagnetizes NVC, causing the spring to trip the starter to OFF.

**3. Solution via 4-Point Starter:**
* NVC is taken out of the field circuit and placed in an independent circuit across the line in series with a fixed current-limiting resistor. NVC current remains constant regardless of field rheostat adjustments.

* **Reference in Mam Slide:** 266, 270
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 114-119
* **Reference in Theraja Vol II:** PDF Pages 170-174

---

### 69. Page 10, Q.7(a): Explain with neat sketch, how 3-point starter can start dc motor with heavy starting torque but with low speed. [Figure Involved]

* **Full Flux Provision:** Shunt field connects directly to the supply line via a brass arc behind the contact studs, guaranteeing 100% rated flux ($\Phi$).
* **Armature Resistance Control:** All starting resistance steps ($R_1 \dots R_5$) are in series with the armature, holding starting current to safe limits and starting speed to near zero.
* **Heavy Torque:** Because $\Phi$ is maximum and $I_a$ is controlled at $1.5 \times I_{\text{FL}}$, maximum starting torque is developed.
* **[Figure Involved]:** Wiring schematic of 3-point starter showing $L$, $A$, $F$ terminals, starting arm, studs, NVC, OLR, and brass arc.

* **Reference in Mam Slide:** 268, 269
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 115-117
* **Reference in Theraja Vol II:** PDF Pages 171-173

---

### 70. Page 14, Q.3(c): What are the functions of 4-point starter to start a dc motor?

**Key Functions:**
1. **Current Inrush Limitation:** Provides step-by-step external resistance to limit starting current to safe levels ($1.5 \times I_{\text{FL}}$).
2. **Speed-Independent Hold-In:** Isolates the No-Volt Coil (NVC) in an independent branch so field weakening speed control does not trip the starter handle.
3. **No-Voltage Protection:** If main supply fails, NVC de-energizes and a spiral spring pulls the handle back to OFF, preventing direct line startup on power restoration.
4. **Overload Protection:** Overload release (OLR) coil short-circuits the NVC when current exceeds safety thresholds, triggering an automatic shutoff.

* **Reference in Mam Slide:** 270, 271
* **Reference in Firoz Note:** 115
* **Reference in Rosenblatt:** Section 9-4, Pages 117-119
* **Reference in Theraja Vol II:** PDF Pages 173-174

---

### 71. Page 25, CT-03 Q.1: Why is starter required in starting DC motor? Write the advantages and limitations of three-point starter and four-point starter.

**1. Why Starter is Required:**
* At start ($N = 0 \implies E_b = 0$). Starting current $I_{\text{start}} = V/R_a$ is dangerously high without external starting resistance.

**2. Comparison of Starters:**
* **3-Point Starter:**
  * *Advantage:* Simple, economical, provides automatic no-voltage and overload protection.
  * *Limitation:* Cannot be used for high-speed field weakening because NVC drops out when field current is reduced.
* **4-Point Starter:**
  * *Advantage:* Operates reliably across wide speed ranges; field rheostat adjustments never trip the handle.
  * *Limitation:* More complex wiring (requires 4th wire and extra current-limiting resistor); does not protect against an open circuit in the field winding itself.

* **Reference in Mam Slide:** 266, 268, 270
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 114-119
* **Reference in Theraja Vol II:** PDF Pages 170-174

---

### 72. Page 26, CT-02 Q.No.3: Why is starter needed for starting dc motor? How four point starter overcome the difficulties of three point starter?

* **Necessity:** Standstill back EMF is zero ($E_b = 0$). With low $R_a$, starting current is $15\text{–}30 \times I_{\text{FL}}$, causing destructive heating and brush flashover.
* **How 4-Point Overcomes Difficulty:**
  * 3-point starter places NVC in series with field $\rightarrow$ field weakening causes premature tripping.
  * 4-point starter separates the NVC and connects it in a dedicated branch across the supply through a fixed current-limiting resistor. The NVC current stays constant regardless of field rheostat position, eliminating nuisance trips.

* **Reference in Mam Slide:** 266, 270
* **Reference in Firoz Note:** 114, 115
* **Reference in Rosenblatt:** Section 9-4, Pages 114-119
* **Reference in Theraja Vol II:** PDF Pages 170-174

---

### **13. Losses in DC machines (and Power flow diagram)**

### 74. Page 5, Q.68: Prove that the electrical power converted into mechanical power is equal to the product of the counter emf and the armature current.

**Proof:**
1. Voltage equation of DC motor:
   $$V = E_b + I_a R_a$$
2. Multiply by armature current $I_a$:
   $$V I_a = E_b I_a + I_a^2 R_a$$
3. Physical interpretation of each term:
   * $V I_a$ = Total electrical power supplied to the armature.
   * $I_a^2 R_a$ = Power lost as heat in armature resistance (copper loss).
4. By conservation of energy, useful mechanical power developed ($P_m$) is:
   $$P_m = \text{Total Input Power} - \text{Copper Losses} = V I_a - I_a^2 R_a$$
5. From the equation above:
   $$V I_a - I_a^2 R_a = E_b I_a$$
   $$\mathbf{P_m = E_b I_a}\quad \text{(Hence proved.)}$$

* **Reference in Mam Slide:** 222, 223
* **Reference in Firoz Note:** 81, 82
* **Reference in Rosenblatt:** Section 7-6, Pages 79-80
* **Reference in Theraja Vol II:** PDF Page 142

---

### 75. Page 5, Q.69: Explain in detail what are the losses in DC machine?

**Classification of Losses:**
1. **Copper Losses ($I^2R$ Losses):**
   * Armature copper loss: $I_a^2 R_a$ (variable with load, 30–40% of total losses).
   * Shunt field copper loss: $I_{sh}^2 R_{sh}$ (practically constant).
   * Series field copper loss: $I_{se}^2 R_{se}$ (variable with load).
   * Brush contact resistance loss: $V_{\text{brush}} \times I_a$ ($\approx 2\text{ V} \times I_a$).
2. **Magnetic / Core / Iron Losses:**
   * **Hysteresis Loss:** $W_h = \eta B_m^{1.6} f V_{\text{core}}$ (due to continuous reversal of magnetization in armature core).
   * **Eddy Current Loss:** $W_e = k B_m^2 f^2 t^2 V_{\text{core}}$ (minimized by thin laminations).
3. **Mechanical Losses:**
   * Friction loss (bearings and brush friction on commutator).
   * Windage loss (air resistance to rotating rotor).
4. **Stray Load Losses:**
   * Caused by flux distortion from armature reaction (typically taken as 1% of full load).

* **Reference in Mam Slide:** 276, 277, 278
* **Reference in Firoz Note:** 128, 129, 130
* **Reference in Rosenblatt:** Section 11-1, Pages 140-144
* **Reference in Theraja Vol II:** PDF Pages 180-183

---

### 76. Page 5, Q.70: Prove that the efficiency of a dc generator will be maximum when the load current is such that variable loss is equal to the constant loss.

**Proof:**
1. Generator output power: $P_{\text{out}} = V I$.
2. Total losses:
   $$\text{Total Losses} = I_a^2 R_a + W_c \approx I^2 R_a + W_c$$
   *(where $I^2 R_a$ = variable copper loss, $W_c$ = constant losses including iron, friction, and shunt field losses).*
3. Generator efficiency ($\eta$):
   $$\eta = \frac{P_{\text{out}}}{P_{\text{out}} + \text{Losses}} = \frac{V I}{V I + I^2 R_a + W_c} = \frac{1}{1 + \frac{I R_a}{V} + \frac{W_c}{V I}}$$
4. For maximum efficiency, the denominator must be minimum. Differentiating the denominator with respect to $I$ and setting to zero:
   $$\frac{d}{dI}\left(1 + \frac{I R_a}{V} + \frac{W_c}{V I}\right) = \frac{R_a}{V} - \frac{W_c}{V I^2} = 0$$
   $$\frac{R_a}{V} = \frac{W_c}{V I^2} \implies I^2 R_a = W_c$$
   $$\mathbf{\text{Variable Loss} = \text{Constant Loss}}$$
* **Conclusion:** Maximum efficiency occurs when the variable copper losses equal the constant losses. Load current for maximum efficiency is $I = \sqrt{\frac{W_c}{R_a}}$.

* **Reference in Mam Slide:** 280, 281
* **Reference in Firoz Note:** 131, 132
* **Reference in Rosenblatt:** Section 11-3, Pages 146-148
* **Reference in Theraja Vol II:** PDF Pages 184-185

---

### 77. Page 25, CT-03 Q.3: Shortly describe the losses occurring in dynamo.

**Summary of Dynamo Losses:**
* **Copper Losses ($I^2R$):** Armature copper loss ($I_a^2 R_a$), shunt field loss ($I_{sh}^2 R_{sh}$), and brush contact drop loss.
* **Iron Losses (Core Losses):**
  * *Hysteresis Loss:* Energy lost as heat due to molecular magnetic friction as core rotates through alternating pole fields ($W_h \propto B_m^{1.6} f$).
  * *Eddy Current Loss:* Induced circulating currents within the core mass; restricted by insulating laminations ($W_e \propto B_m^2 f^2 t^2$).
* **Mechanical Losses:** Bearing friction, brush friction on commutator, and air windage.
* **Constant vs Variable:** Core and mechanical losses are considered constant ($W_c$); armature copper loss varies with the square of the load current ($I_a^2 R_a$).

* **Reference in Mam Slide:** 276, 277
* **Reference in Firoz Note:** 128, 129
* **Reference in Rosenblatt:** Section 11-1, Pages 140-144
* **Reference in Theraja Vol II:** PDF Pages 180-183

---

### 78. Page 27, CT-02 Q.No.3: A 220V shunt motor takes a total current of 80A and runs at a speed of 800 rpm. Shunt field resistance and armature resistance are 50 ohm and 0.1 ohm respectively. If iron and friction losses amount to 1600 W, find the efficiency of the motor.

**Given Data:**
* $V = 220\text{ V}$, $I_L = 80\text{ A}$, $N = 800\text{ rpm}$, $R_f = 50\,\Omega$, $R_a = 0.1\,\Omega$, $P_{\text{const(iron+friction)}} = 1600\text{ W}$.

**1. Total Input Power ($P_{\text{in}}$):**
$$P_{\text{in}} = V \times I_L = 220 \times 80 = \mathbf{17600\text{ W}}$$

**2. Currents:**
* Shunt field current: $I_f = \frac{V}{R_f} = \frac{220}{50} = \mathbf{4.4\text{ A}}$.
* Armature current: $I_a = I_L - I_f = 80 - 4.4 = \mathbf{75.6\text{ A}}$.

**3. Copper Losses:**
* Armature copper loss: $P_{a(\text{cu})} = I_a^2 R_a = (75.6)^2 \times 0.1 = 571.536 \times 0.1 = \mathbf{571.54\text{ W}}$.
* Shunt field copper loss: $P_{f(\text{cu})} = V \times I_f = 220 \times 4.4 = \mathbf{968\text{ W}}$.
* Total copper loss: $571.54 + 968 = \mathbf{1539.54\text{ W}}$.

**4. Total Losses:**
$$\text{Total Losses} = P_{\text{cu}} + P_{\text{const}} = 1539.54 + 1600 = \mathbf{3139.54\text{ W}}$$

**5. Output Power ($P_{\text{out}}$):**
$$P_{\text{out}} = P_{\text{in}} - \text{Total Losses} = 17600 - 3139.54 = \mathbf{14460.46\text{ W}}\quad (\approx 19.38\text{ hp})$$

**6. Motor Efficiency ($\eta$):**
$$\eta = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100 = \frac{14460.46}{17600} \times 100 = \mathbf{82.16\%}$$

* **Reference in Mam Slide:** 280, 281
* **Reference in Firoz Note:** 131, 132
* **Reference in Rosenblatt:** Section 11-2, Pages 144-146
* **Reference in Theraja Vol II:** PDF Pages 184-186
