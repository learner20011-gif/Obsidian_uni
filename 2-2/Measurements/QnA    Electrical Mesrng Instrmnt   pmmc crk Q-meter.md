### 1. Page 2, Q.2. (b): Suppose you are working with a gavanometer that has underdamped motion. How can you modify the instrument for critically damped motion if you cannot change the spring and inertia of the instrument? Provide mathematical reasoning.
[watch this for galvanometer](https://youtu.be/7UCUGHBZXNQ?si=2C2TI95LoQr4VOpy)
**Answer:**
The dynamic behavior of a galvanometer is governed by its equation of motion, which balances the inertial, damping, and controlling torques against the deflecting torque: 
$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + K\theta = Gi$

Where:
*   $J$ = moment of inertia of the moving system
*   $D$ = total damping constant (air friction + electromagnetic damping)
*   $K$ = control spring constant
*   $G$ = displacement constant

For the system to be underdamped, the damping constant is less than the critical value, mathematically represented by the discriminant of the characteristic equation being negative: $D < 2\sqrt{JK}$.

To modify the instrument to achieve critically damped motion, the condition must become exactly $D = 2\sqrt{JK}$. Since the problem states you cannot change the spring constant ($K$) or the inertia ($J$), the only parameter you can alter is the damping constant ($D$). 

The total damping constant $D$ is primarily comprised of mechanical friction (which is negligible/fixed) and electromagnetic damping. Electromagnetic damping ($D_{em}$) is inversely proportional to the total resistance ($R$) of the galvanometer circuit. Therefore, to increase the overall damping constant $D$ up to the required critical value of $2\sqrt{JK}$, you must increase the electromagnetic damping. This is achieved by decreasing the total electrical resistance of the circuit, which can be done practically by connecting a suitable shunt resistance in parallel with the galvanometer. 

Ans related location pg number in ak slide: 75, 76.

***

### 2. Page 7, Q.5 (b): Briefly discuss the construction of Galvanometer and hence derive the torque equation.

**Answer:**
**Construction of Galvanometer:**
A Permanent Magnet Moving Coil (PMMC) or d'Arsonval galvanometer essentially consists of the following main components:
*   **Moving Coil:** The current-carrying element made of fine copper wire wound into a rectangular or circular shape. It is mounted on a vertical axis of symmetry so that it can freely rotate between the poles of a permanent magnet.
*   **Permanent Magnet & Iron Core:** A permanent magnet provides the required magnetic field. A stationary iron core is placed inside the coil to provide a low-reluctance path for the magnetic flux, ensuring a strong and uniform radial magnetic field for the coil to move in.
*   **Suspension:** The coil is suspended by a flat ribbon that also serves as the path to carry current into the coil. A lower suspension is also present, though its mechanical torque effect is negligible.
*   **Mirror & Torsion Head:** A small mirror is attached to the suspension to cast a light beam on a scale, allowing for precise measurement of deflection. The torsion head controls the coil's position and is used to adjust the zero setting.

**Derivation of Torque Equation:**
Let:
*   $l$ = length of the vertical side of the coil
*   $d$ = length of the horizontal side of the coil
*   $N$ = number of turns in the coil
*   $B$ = flux density in the air gap (in $Wb/m^2$)
*   $i$ = current flowing through the moving coil (in Amperes)

When current flows, the vertical sides of the coil experience a magnetic force. The force ($F$) on each vertical side of the coil is given by:
$F = NBil$

The deflecting torque ($T_d$) is the product of this force and the perpendicular distance between the two vertical sides (which is the width $d$):
$T_d = Force \times Distance$
$T_d = F \times d$
$T_d = (NBil) \times d$
$T_d = NBi(l \times d)$

Since the area of the coil is $A = l \times d$, the equation can be rewritten as:
$T_d = NBAi$

Letting the constants $N, B,$ and $A$ be combined into a single displacement constant $G$ ($G = NBA$), the torque equation simplifies to:
$T_d = Gi$

Ans related location pg number in ak slide: 69, 70, 72, 73.

***

### 3. Page 12, Q.8. (d): When is indicating instrument is said to be dead-beat?

**Answer:**
An indicating instrument is said to be "dead-beat" when it is critically damped. In this condition, the internal damping forces are precisely calibrated so that the moving system (the pointer and coil) responds to a change in the measured quantity by moving swiftly to its final steady-state deflection position and stopping exactly at that reading without oscillating, hunting, or overshooting. Mathematically, this corresponds to the state where the damping constant perfectly balances the inertial and control forces ($D = 2\sqrt{JK}$).

Ans related location pg number in ak slide: 67, 75, 76 (General principles of Damping).

***

### 4. Page 23, CT-01 Q1: From the equation of motion of a galvanometer, derive the condition which must be satisfied for the moving coil to have a critically damped motion.

**Answer:**
The dynamic behavior of a galvanometer is described by equating the deflecting torque to the opposing inertial, damping, and controlling spring torques. The resulting second-order differential equation of motion is:
$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + K\theta = T_d$

Where:
*   $J$ = moment of inertia of the moving system
*   $D$ = air friction and electromagnetic damping constant
*   $K$ = control spring constant
*   $\theta$ = angular deflection

To analyze the transient motion (how the pointer settles), we solve the homogeneous part of the differential equation:
$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + K\theta = 0$

This leads to the characteristic auxiliary equation:
$Jr^2 + Dr + K = 0$

Using the quadratic formula, the roots ($r_1$ and $r_2$) of this equation are:
$r_{1,2} = \frac{-D \pm \sqrt{D^2 - 4JK}}{2J}$

The physical behavior of the moving coil depends heavily on the term inside the square root (the discriminant, $D^2 - 4JK$). For the motion to be **critically damped**, the pointer must return to equilibrium as fast as possible without oscillating. Mathematically, this requires the roots of the characteristic equation to be real and equal, which happens exactly when the discriminant is zero:

$D^2 - 4JK = 0$
$D^2 = 4JK$
$D = 2\sqrt{JK}$

Therefore, the specific condition that must be satisfied for the galvanometer moving coil to have critically damped motion is $D = 2\sqrt{JK}$.

Ans related location pg number in ak slide: 76.

### 5. Page 28, Q2: Illustrate how eddy current damping works.

**Answer:**
Eddy current damping is one of the most effective methods of electromagnetic damping used in electrical measuring instruments. It operates based on two fundamental laws of electromagnetism: Faraday's Law of Electromagnetic Induction and Lenz's Law.

**Mechanism of Eddy Current Damping:**
1. **Generation of Eddy Currents:** When a non-magnetic conducting material (such as an aluminum disc or the aluminum former on which a coil is wound) moves within a stationary, uniform magnetic field, it continuously cuts the magnetic flux lines. According to Faraday’s Law, this motion induces an electromotive force (EMF) within the conducting material. Because the material is a solid conductor, it provides closed, low-resistance paths for this EMF to drive circulating currents. These localized, circular currents are called "eddy currents."
2. **Creation of Opposing Force:** These induced eddy currents generate their own magnetic field around the conductor. According to Lenz's Law, the direction of the induced eddy currents (and thus their resulting magnetic field) will always be such that it opposes the change in magnetic flux that caused it. Therefore, the magnetic field of the eddy currents interacts with the main permanent magnetic field to produce a mechanical force (or torque).
3. **Damping Action:** This resulting force acts in the exact opposite direction to the motion of the conductor. The magnitude of the induced EMF, and consequently the eddy current and opposing torque, is directly proportional to the velocity of the moving system. As the pointer approaches its final reading, its velocity decreases, meaning the damping torque smoothly approaches zero, preventing the pointer from oscillating without causing steady-state error.

Ans related location pg number in ak slide: 74, 75, 86, 95 (PMMC and Energy meter construction where this principle is applied).

***

### 6. Page 28, Q3: Demonstrate how gravity control works. Does it work for both horizontal & vertically mounted devices?

**Answer:**
**How Gravity Control Works:**
Gravity control is a method used to provide the controlling (or restoring) torque in certain indicating instruments. It is achieved by attaching a small adjustable weight to the moving system (usually attached to the pointer spindle) in such a way that it hangs vertically downwards when the instrument pointer is at the zero position. 

When the deflecting torque acts on the moving system, the pointer deflects by an angle $\theta$. As the pointer moves, the attached weight is lifted against the force of gravity. The gravitational pull on this weight creates a restoring torque that tries to pull the pointer back to the zero position.
Mathematically, if $W$ is the weight and $L$ is the distance from the pivot center to the center of gravity of the weight, the restoring torque ($T_c$) is given by:
$T_c = W \times L \times \sin(\theta)$
At the steady-state position, the deflecting torque ($T_d$) equals the controlling torque ($T_c$). Because the controlling torque is proportional to $\sin(\theta)$ rather than directly proportional to $\theta$ (as in spring control), instruments using gravity control have a non-uniform scale that is typically cramped or crowded at the lower end.

**Does it work for both horizontal & vertically mounted devices?**
No, gravity control **only works for vertically mounted devices** (e.g., panel boards mounted on walls). It does not work for horizontally mounted devices (such as a bench-top multimeter). For gravity control to function, the restoring torque relies on the weight being lifted upwards against the downward force of gravity. If the instrument is laid flat horizontally, the weight merely moves sideways horizontally when the pointer turns; it does not move against the vertical pull of gravity, and therefore no restoring torque is generated.

Ans related location pg number in ak slide: 67 (Damping/Control Systems section).

***

### 7. Page 29, Class test #1, Q1: The pointer and the winding of an AC/DC PMMC ammeter has an underdamped motion. How can you modify the instrument to get a critically damped motion? Discuss with required mathematical proof. Note that you cannot change the core, winding and magnet assembly.

**Answer:**
**Modification required:**
To change the motion from underdamped to critically damped without altering the physical properties of the core, winding, magnet assembly, or the spring, we must increase the electromagnetic damping of the instrument. This is achieved by **connecting a low-resistance shunt in parallel with the moving coil of the galvanometer.**

**Mathematical Proof:**
The dynamic equation of motion for a galvanometer is:
$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + K\theta = T_d$

Where:
*   $J$ = moment of inertia
*   $D$ = total damping constant
*   $K$ = control spring constant

The characteristic equation for the transient motion is $Jr^2 + Dr + K = 0$, giving the roots:
$r = \frac{-D \pm \sqrt{D^2 - 4JK}}{2J}$

1.  **Underdamped Condition:** The current state of the ammeter is underdamped, which mathematically means the discriminant is negative:
    $D^2 < 4JK \implies D < 2\sqrt{JK}$
2.  **Critically Damped Condition:** To achieve a critically damped motion (fastest settling time without oscillation), the roots must be real and equal. This requires the discriminant to be zero:
    $D^2 - 4JK = 0 \implies D_{critical} = 2\sqrt{JK}$
3.  **Increasing D:** Since we cannot change $J$ (moving mass/inertia) or $K$ (spring constant), we must increase $D$ to equal $2\sqrt{JK}$.
    The total damping $D$ consists of mechanical damping ($D_{mech}$, which is fixed/negligible) and electromagnetic damping ($D_{em}$).
    $D = D_{mech} + D_{em}$
    Electromagnetic damping depends on the displacement constant $G$ (which is fixed as $NBA$ because we cannot change the core, winding, or magnet) and the total resistance $R_{total}$ of the circuit:
    $D_{em} = \frac{G^2}{R_{total}}$
4.  **Conclusion:** To increase $D_{em}$ so that the total damping $D$ reaches the critical threshold $2\sqrt{JK}$, we must **decrease** the total circuit resistance $R_{total}$. By adding a shunt resistor ($R_{sh}$) in parallel with the galvanometer's internal resistance, the equivalent resistance of the circuit decreases, thereby increasing the electromagnetic damping $D_{em}$ until critical damping is achieved.

Ans related location pg number in ak slide: 75, 76.

***

### 8. Page 29, Class test #1, Q2: How eddy current is generated? Illustrate how eddy current damping works. Name an instrument you know that uses eddy current damping.

**Answer:**
**How Eddy Current is Generated:**
Eddy currents are generated when a non-magnetic, conductive material experiences a changing magnetic field. This can occur either if the magnetic field itself fluctuates over time (AC field) or if the conductor physically moves through a stationary magnetic field. According to Faraday's Law of Induction, this changing magnetic flux induces an electromotive force (EMF) across the conductor. Because the conductor is a solid piece of metal (like a disc or a former), it offers a low-resistance path, causing closed loops of electrical currents to circulate within the body of the material. These circulating loops are known as eddy currents.

**How Eddy Current Damping Works:**
1. Once the eddy currents are generated within the moving conductor, these currents create their own magnetic fields.
2. According to Lenz's law, the direction of these induced magnetic fields is such that it will oppose the very cause that created them. The "cause" is the physical motion of the conductor through the main magnetic field.
3. Therefore, an electromagnetic drag force (or damping torque) is produced that directly opposes the motion of the conductor. 
4. Because the induced EMF (and the resulting eddy current) is directly proportional to the speed of the moving conductor, this opposing damping force is also directly proportional to the speed. When the pointer moves quickly, the damping is strong; as the pointer slows down and settles on its final reading, the damping force tapers off to zero, effectively eliminating oscillation without causing steady-state friction.

**Instruments that use eddy current damping:**
*   **PMMC (Permanent Magnet Moving Coil) instruments:** The moving coil is wound on a light aluminum former. When the coil moves, the aluminum former cuts the magnetic field, generating eddy currents in the former that damp the pointer's movement.
*   **Induction type Energy Meters:** An aluminum disc rotates between the poles of a permanent "braking magnet." The eddy currents generated in the disc as it passes through the braking magnet's field provide the necessary opposing damping/braking torque.

Ans related location pg number in ak slide: 74, 75, 86, 95.

### 9. Page 29, Class test #1, Q3: Which torques act on an instrument during motion and on steady-state condition? Analyze which type of controlling torque is appropriate for both horizontal and vertically mounted PMMC instruments.

**Answer:**
**Torques acting during motion:**
When the pointer of an indicating instrument is moving towards its final reading, there are four distinct torques acting on the moving system:
1.  **Deflecting Torque ($T_d$):** The driving torque generated by the electrical quantity being measured (e.g., current or voltage). It causes the pointer to move from its zero position.
2.  **Controlling Torque ($T_c$):** The restoring torque that opposes the deflecting torque. It increases as the deflection angle increases and ensures the pointer stops at a value proportional to the measured quantity.
3.  **Damping Torque ($T_v$):** A frictional or electromagnetic drag force that opposes the motion of the pointer. It is proportional to the velocity of the pointer and acts only when the pointer is moving. It prevents oscillations.
4.  **Inertial Torque ($T_j$):** The torque due to the moment of inertia of the moving system, opposing any change in angular acceleration.

**Torques acting in steady-state condition:**
In the steady-state condition, the pointer has come to rest at its final reading. Therefore, its velocity and acceleration are zero. Consequently, the damping torque (which depends on velocity) and the inertial torque (which depends on acceleration) are both zero.
Only two torques act on the instrument in steady-state:
1.  **Deflecting Torque ($T_d$)**
2.  **Controlling Torque ($T_c$)**
At this state, they perfectly balance each other: $T_d = T_c$.

**Appropriate controlling torque for horizontal and vertical PMMC:**
There are two main types of controlling torques: Gravity control and Spring control.
*   **Gravity control** works by utilizing the weight of a small mass attached to the moving system. As the pointer deflects, the weight is lifted against gravity, creating a restoring torque. However, gravity control *only* works if the instrument is mounted vertically (so gravity can act downwards against the lifted weight). It will not work if the instrument is placed horizontally.
*   **Spring control** uses hairsprings (usually made of phosphor bronze) attached to the moving coil. The restoring torque is provided by the physical twisting (torsion) of the spring, which is entirely independent of gravity. 

Therefore, **spring control** is the only appropriate type of controlling torque for PMMC instruments that need to be used in both horizontal and vertically mounted positions.

Ans related location pg number in ak slide: 67, 72, 73, 76.

***

### 10. Page 2, Q.1. (b): Show that the electrostatic instruments are voltage sensors that work with both AC and DC. Also, comment on the uniformity of the scale of those instruments.

**Answer:**
**Working with AC and DC:**
Electrostatic instruments operate on the principle of electrostatic attraction between oppositely charged plates (one fixed and one movable). The deflecting torque ($T_d$) generated in an electrostatic instrument is derived from the rate of change of energy stored in the variable capacitance formed by these plates.
The mathematical expression for the deflecting torque is given by:
$T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}$
Where:
*   $V$ is the potential difference (voltage) applied across the plates.
*   $C$ is the capacitance of the system.
*   $\theta$ is the angular deflection.

Because the deflecting torque is proportional to the **square of the applied voltage ($V^2$)**, the torque will always act in the same direction regardless of the polarity of the voltage. 
*   If a DC voltage is applied, $V^2$ is positive, and deflection occurs in a specific direction.
*   If an AC voltage is applied, the polarity reverses constantly. However, since the square of a negative voltage is still positive, the instantaneous torque remains in the same direction. The moving system, due to its inertia, responds to the average driving torque, which corresponds to the Root Mean Square (RMS) value of the AC voltage.
Therefore, the electrostatic instrument is a true voltage sensor that works accurately for both AC and DC.

**Uniformity of the scale:**
At steady state, the deflecting torque is balanced by a spring controlling torque ($T_c = K\theta$).
Equating the two:
$K\theta = \frac{1}{2} V^2 \frac{dC}{d\theta}$
$\theta = \frac{1}{2K} V^2 \frac{dC}{d\theta}$

The deflection $\theta$ is directly proportional to the square of the voltage ($V^2$). Because of this square-law relationship, the scale of an electrostatic instrument is **non-uniform**. It is tightly cramped at the lower end (small voltages produce very little deflection) and widely expanded at the upper end (larger voltages produce rapidly increasing deflection).

Ans related location pg number in ak slide: 86, 140 (Capacitive sensor principles apply to electrostatic plates).

***

### 11. Page 4, Q.1 (b): Explain why PMMC instruments cannot measure AC quantities. How can they be modified for measuring AC current?

**Answer:**
**Why PMMC cannot measure AC:**
A Permanent Magnet Moving Coil (PMMC) instrument operates on the principle that a current-carrying coil placed in a constant magnetic field experiences a force. The deflecting torque equation is $T_d = NBAi$, where the torque is directly proportional to the instantaneous current $i$.
If an Alternating Current (AC) is passed through the moving coil, the direction of the current reverses during the negative half-cycle. Consequently, the deflecting torque also reverses direction. For a standard 50 Hz or 60 Hz AC supply, the torque changes direction 100 or 120 times per second. 
Due to the mechanical inertia of the moving coil and pointer, the system cannot respond to these rapid reversals. The pointer simply vibrates very slightly around the zero position because the average deflecting torque over a complete AC cycle is absolutely zero. Thus, a basic PMMC cannot measure AC.

**Modification for measuring AC:**
To measure AC using a PMMC movement, the AC signal must be converted into a unidirectional (DC) signal before it is fed into the moving coil. This is primarily done using **Rectifier circuits**.
By employing a half-wave or full-wave bridge rectifier (usually made of diodes) in the circuit, the AC current is converted into a pulsating DC current. The PMMC instrument will then respond to the average value of this rectified DC current. The scale of the instrument can then be calibrated to display the RMS value of the original AC waveform (assuming a pure sine wave, using a form factor of 1.11). 
Another method is using a **thermocouple**, where the AC current heats a wire, and the resulting thermoelectric DC voltage is measured by the PMMC.

Ans related location pg number in ak slide: 72, 86, 94 (AVO meters), 110 (VTVM rectifiers).

***

### 12. Page 4, Q.2 (b): The relationship between the inductance of an MI ammeter, the current and the position of the pointer is as follows:
| Reading (A) | 0.8 | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Deflection (deg.) | 16.5 | 26 | 36 | 46 | 56 | 70 | 80 |
| Inductance ($\mu$H) | 527.8 | 573.9 | 575.0 | 576.2 | 577.0 | 578.1 | 579.0 |
Calculate the deflecting torque when the current is (i) 1.5 A and (ii) 2.1 A.

**Answer:**
The deflecting torque $T_d$ of a Moving Iron (MI) instrument is given by the formula:
$T_d = \frac{1}{2} I^2 \frac{dL}{d\theta}$
Where $I$ is the current in Amperes, and $\frac{dL}{d\theta}$ is the rate of change of inductance with respect to the deflection angle in radians.

**(i) For $I = 1.5$ A:**
1.5 A lies exactly between 1.4 A and 1.6 A. We calculate the gradient $\frac{dL}{d\theta}$ for this interval.
At $I = 1.6$ A: $\theta_2 = 56^\circ$, $L_2 = 577.0 \, \mu\text{H}$
At $I = 1.4$ A: $\theta_1 = 46^\circ$, $L_1 = 576.2 \, \mu\text{H}$

Change in inductance, $\Delta L = 577.0 - 576.2 = 0.8 \, \mu\text{H} = 0.8 \times 10^{-6} \, \text{H}$
Change in angle, $\Delta \theta = 56^\circ - 46^\circ = 10^\circ$
Convert $\Delta \theta$ to radians: $10 \times \frac{\pi}{180} = 0.17453 \, \text{rad}$

$\frac{dL}{d\theta} \approx \frac{\Delta L}{\Delta \theta} = \frac{0.8 \times 10^{-6}}{0.17453} = 4.5837 \times 10^{-6} \, \text{H/rad}$

Now, calculate torque for $I = 1.5$ A:
$T_d = \frac{1}{2} \times (1.5)^2 \times (4.5837 \times 10^{-6})$
$T_d = 0.5 \times 2.25 \times 4.5837 \times 10^{-6}$
**$T_d = 5.156 \times 10^{-6} \, \text{Nm} = 5.16 \, \mu\text{Nm}$**

**(ii) For $I = 2.1$ A:**
Since the data table ends at 2.0 A, we must estimate the gradient at the upper end of the scale by using the last available interval (between 1.8 A and 2.0 A) and assuming it remains roughly constant up to 2.1 A.
At $I = 2.0$ A: $\theta_2 = 80^\circ$, $L_2 = 579.0 \, \mu\text{H}$
At $I = 1.8$ A: $\theta_1 = 70^\circ$, $L_1 = 578.1 \, \mu\text{H}$

Change in inductance, $\Delta L = 579.0 - 578.1 = 0.9 \, \mu\text{H} = 0.9 \times 10^{-6} \, \text{H}$
Change in angle, $\Delta \theta = 80^\circ - 70^\circ = 10^\circ = 0.17453 \, \text{rad}$

$\frac{dL}{d\theta} \approx \frac{\Delta L}{\Delta \theta} = \frac{0.9 \times 10^{-6}}{0.17453} = 5.1566 \times 10^{-6} \, \text{H/rad}$

Now, calculate torque for $I = 2.1$ A using this gradient:
$T_d = \frac{1}{2} \times (2.1)^2 \times (5.1566 \times 10^{-6})$
$T_d = 0.5 \times 4.41 \times 5.1566 \times 10^{-6}$
**$T_d = 11.37 \times 10^{-6} \, \text{Nm} = 11.37 \, \mu\text{Nm}$**

Ans related location pg number in ak slide: 85, 86.

***

### 13. Page 6, Q.2 b): Derive the expression for the deflection of an electrostatic type instrument.

**Answer:**
An electrostatic instrument acts as a variable capacitor. The deflection relies on the change in stored electrical energy turning into mechanical work.
Let:
*   $C$ = capacitance of the instrument plates at an initial angle
*   $V$ = applied potential difference across the plates
*   $\theta$ = initial angle of deflection

The energy stored in the electric field of the capacitor is:
$W = \frac{1}{2} C V^2$

Suppose the applied voltage $V$ causes a small increase in deflection by $d\theta$, which causes the capacitance to increase by $dC$. During this small movement, the voltage source supplies an incremental electrical energy $dE$:
$dE = V \cdot dQ$ 
Since $Q = CV$ and $V$ is kept constant, $dQ = V dC$. Therefore:
$dE = V (V dC) = V^2 dC$

This supplied energy does two things: 
1. It increases the stored energy in the capacitor.
2. It performs mechanical work to deflect the pointer.

The increase in stored energy is:
$d(\text{Stored Energy}) = d(\frac{1}{2} C V^2) = \frac{1}{2} V^2 dC$ (since V is constant)

The mechanical work done by the deflecting torque $T_d$ over angle $d\theta$ is:
$\text{Work Done} = T_d \cdot d\theta$

Applying the principle of conservation of energy:
Total Electrical Energy Supplied = Increase in Stored Energy + Mechanical Work Done
$V^2 dC = \frac{1}{2} V^2 dC + T_d \cdot d\theta$
$V^2 dC - \frac{1}{2} V^2 dC = T_d \cdot d\theta$
$\frac{1}{2} V^2 dC = T_d \cdot d\theta$

Thus, the deflecting torque is:
$T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}$

In steady state, this deflecting torque is balanced by the controlling torque $T_c$ of the spring, where $T_c = K\theta$ ($K$ being the spring constant).
$T_c = T_d$
$K\theta = \frac{1}{2} V^2 \frac{dC}{d\theta}$
**$\theta = \frac{1}{2K} V^2 \frac{dC}{d\theta}$**
This is the required expression for the deflection.

Ans related location pg number in ak slide: 140 (Capacitive principles).

***

### 14. Page 7, Q.3 (a): Develop the torque equation for a PMMC instrument and show that its scale is linear.

**Answer:**
**Torque Equation Development:**
A Permanent Magnet Moving Coil (PMMC) instrument consists of a multi-turn rectangular coil placed in a uniform radial magnetic field.
Let:
*   $l$ = length of the vertical sides of the coil (m)
*   $d$ = width of the coil (distance between vertical sides in m)
*   $N$ = number of turns of the coil
*   $B$ = flux density in the air gap ($Wb/m^2$ or Tesla)
*   $I$ = current flowing through the coil (A)

When current passes through the coil, the vertical sides experience a magnetic Lorentz force. Since the field is radial, the magnetic field is always perpendicular to the conductors.
Force on each vertical side: $F = NBIl$

The deflecting torque ($T_d$) is this force multiplied by the perpendicular distance between the two sides ($d$):
$T_d = F \times d = (NBIl) \times d$
Since Area $A = l \times d$, we can write:
$T_d = NBAI$

For a specific instrument, the number of turns ($N$), flux density ($B$), and area ($A$) are all constants. Let their product be $G = NBA$ (displacement constant).
So, **$T_d = GI$** (Deflecting Torque Equation)

**Showing the scale is linear:**
The controlling torque in a PMMC instrument is provided by hairsprings. The controlling torque ($T_c$) is directly proportional to the angle of deflection ($\theta$):
$T_c = K\theta$  (where K is the spring constant in Nm/rad)

At the steady-state final position of the pointer, the controlling torque equals the deflecting torque:
$T_c = T_d$
$K\theta = GI$
$\theta = \left(\frac{G}{K}\right) I$

Since $G$ (which is $NBA$) and $K$ are strictly constant for a given instrument, the ratio $\frac{G}{K}$ is a constant. 
Therefore, **$\theta \propto I$**.
Because the angle of deflection is directly proportional to the current, equal increments in current produce equal increments in deflection. This mathematical linear relationship proves that the scale of a PMMC instrument is uniformly divided (linear).

Ans related location pg number in ak slide: 72, 73, 86.

***

### 15. Page 9, Q.2. (a): Why PMMC is not suitable for an ac quantity measurement? Prove that the scale of PMMC type instrument is linearly divided.

**Answer:**
**Why PMMC is not suitable for AC measurement:**
The deflecting torque of a PMMC instrument is given by $T_d = NBAi$, meaning the torque directly tracks the instantaneous current $i$. When measuring an Alternating Current (AC), the current oscillates between positive and negative half-cycles. During the positive half-cycle, the torque drives the pointer in one direction, and during the negative half-cycle, the torque completely reverses and tries to drive the pointer backward. For standard AC (e.g., 50 Hz), this reversal happens 100 times per second. Because the moving coil and pointer possess mechanical inertia, they physically cannot react fast enough to swing back and forth 100 times a second. Consequently, the pointer rests at the average value of the AC cycle. Since the average value of a pure AC sine wave is strictly zero over a full cycle, a standard PMMC instrument will register zero deflection and therefore cannot be used to measure raw AC quantities.

**Proof that the scale is linearly divided:**
Let the deflecting torque be $T_d$. As per Lorentz force law on the rectangular coil:
$T_d = (N \cdot B \cdot l \cdot I) \cdot d = N B A I$ 
Let $G = NBA$. Then $T_d = GI$.

The instrument uses spring control for restoration, where the controlling torque $T_c$ is directly proportional to the angle of twist (deflection) $\theta$:
$T_c = K\theta$

When the pointer comes to a steady rest, the deflecting torque matches the controlling torque:
$T_d = T_c$
$GI = K\theta$
$\theta = \left(\frac{G}{K}\right) I$

Since $N, B, A$ (making up $G$) and $K$ are all fixed physical constants of the manufactured instrument, the deflection angle $\theta$ is directly and linearly proportional to the measured current $I$. Because $\theta \propto I$, doubling the current doubles the angle, resulting in a scale where divisions are equally spaced. This proves the scale is linearly divided.

Ans related location pg number in ak slide: 72, 73, 86.

***

### 16. Page 9, Q.4. (b): Show that the deflection of an electrostatic instrument is proportional to the square of voltage to be measured.

**Answer:**
To show this, we evaluate the energy balance in the variable capacitance system of an electrostatic instrument. Let an applied steady voltage $V$ cause an initial deflection $\theta$, giving the instrument a capacitance $C$.
Stored energy in the capacitor $W = \frac{1}{2} C V^2$.

If the voltage causes the moving system to deflect further by a small angle $d\theta$, the capacitance changes by $dC$. During this increment, the voltage source must supply an extra small amount of electrical energy $dE$:
$dE = V \cdot dQ = V \cdot d(CV)$
Since $V$ is held constant during this differential step:
$dE = V^2 dC$

This supplied electrical energy is split into two parts:
1.  **Change in stored electrostatic energy:** $d(\frac{1}{2} C V^2) = \frac{1}{2} V^2 dC$
2.  **Mechanical work done by the deflecting torque $T_d$:** $T_d \cdot d\theta$

By energy conservation: 
$V^2 dC = \frac{1}{2} V^2 dC + T_d \cdot d\theta$
Subtracting $\frac{1}{2} V^2 dC$ from both sides gives:
$\frac{1}{2} V^2 dC = T_d \cdot d\theta$
$T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}$

The instrument uses a spring to provide the controlling torque, defined as $T_c = K\theta$. 
At the final steady reading, deflecting torque equals controlling torque:
$T_c = T_d$
$K\theta = \frac{1}{2} V^2 \frac{dC}{d\theta}$
$\theta = \left( \frac{1}{2K} \frac{dC}{d\theta} \right) V^2$

Assuming the term $\frac{1}{2K}\frac{dC}{d\theta}$ behaves as a constant for a specific geometry, the equation clearly shows that the angle of deflection $\theta$ is directly proportional to the square of the applied voltage ($V^2$).
Therefore, **$\theta \propto V^2$**.

Ans related location pg number in ak slide: 140 (Capacitive formulas).

### 17. Page 17, Q.5(a): A permanent magnet moving coil instrument has a coil of dimension 15mm $\times$ 12mm. The flux density in the air is $1.8 \times 10^{-3} \text{ Wb/m}^2$ and the spring constant is $0.14 \times 10^{-6} \text{ Nm/rad}$. Determine the number of turns required to produce an angular deflection of 90 degrees when a current of 5 mA is flowing through the coil.

**Answer:**
To determine the number of turns required, we equate the deflecting torque ($T_d$) to the controlling torque ($T_c$) at the steady-state deflection position.

**Given Data:**
*   Area of the coil, $A = 15 \text{ mm} \times 12 \text{ mm} = (15 \times 10^{-3} \text{ m}) \times (12 \times 10^{-3} \text{ m}) = 180 \times 10^{-6} \text{ m}^2$
*   Flux density, $B = 1.8 \times 10^{-3} \text{ Wb/m}^2$
*   Spring constant, $K = 0.14 \times 10^{-6} \text{ Nm/rad}$
*   Current, $I = 5 \text{ mA} = 5 \times 10^{-3} \text{ A}$
*   Angular deflection, $\theta = 90^\circ$. Since the spring constant is given per radian, we must convert degrees to radians: $\theta = 90 \times \frac{\pi}{180} = \frac{\pi}{2} \approx 1.5708 \text{ rad}$.

**1. Calculate the Controlling Torque ($T_c$):**
$T_c = K \times \theta$
$T_c = (0.14 \times 10^{-6}) \times 1.5708$
$T_c \approx 0.2199 \times 10^{-6} \text{ Nm} = 219.9 \times 10^{-9} \text{ Nm}$

**2. Formulate the Deflecting Torque ($T_d$):**
The deflecting torque in a PMMC instrument is given by the formula:
$T_d = N \cdot B \cdot I \cdot A$
$T_d = N \times (1.8 \times 10^{-3}) \times (5 \times 10^{-3}) \times (180 \times 10^{-6})$
$T_d = N \times 1620 \times 10^{-12} \text{ Nm}$
$T_d = N \times 1.62 \times 10^{-9} \text{ Nm}$

**3. Equate Torques to solve for $N$:**
At steady state, $T_d = T_c$:
$N \times 1.62 \times 10^{-9} = 219.9 \times 10^{-9}$
$N = \frac{219.9 \times 10^{-9}}{1.62 \times 10^{-9}}$
$N \approx 135.74$

Since the number of turns must be a whole number, the required number of turns is approximately **136 turns**.

Ans related location pg number in ak slide: 72, 73, 86.

***

### 18. Page 18, Q.3(a): How PMMC can be used for AC quantity measurement?

**Answer:**
A basic Permanent Magnet Moving Coil (PMMC) instrument inherently responds only to DC because its deflection is directly proportional to the instantaneous current. However, it can be adapted for AC quantity measurement by using the following methods to convert the AC signal into a measurable DC signal before it enters the moving coil:

1.  **Using Rectifier Circuits:** This is the most common method. An AC signal is passed through a rectifier (either half-wave or a full-wave bridge rectifier using diodes), which converts the bidirectional alternating current into a unidirectional pulsating direct current. The PMMC instrument, due to its mechanical inertia, cannot track the rapid pulsations and instead settles at the **average value** of this rectified DC current. Since standard AC voltage and current are usually expressed in RMS (Root Mean Square) values, the scale of the PMMC is specially calibrated to display the RMS value. For a pure sine wave, this is done by multiplying the measured average value by the form factor (which is 1.11 for a full-wave rectified sine wave).
2.  **Using Thermocouple Instruments:** In this configuration, the AC current to be measured is passed through a heater wire. The heat generated ($I^2R$) is proportional to the square of the RMS value of the AC current. A thermocouple junction is placed adjacent to or welded to this heater. The heat produces a small DC thermoelectric voltage at the thermocouple terminals via the Seebeck effect. The PMMC instrument is connected to these terminals to measure the DC voltage. Because the heat depends on the RMS value, the PMMC scale can be directly calibrated to show the true RMS AC current, regardless of the waveform's shape.

Ans related location pg number in ak slide: 94, 110 (VTVM uses rectifiers with PMMC).

***

### 19. Page 26, CT-04 Q2: "Electrostatic instruments are naturally voltage sensing devices."- Justify the statement.

**Answer:**
The statement is completely justified by analyzing the fundamental operating principle and the electrical characteristics of an electrostatic instrument:

1.  **Operating Principle (Dependence on Potential Difference):** Electrostatic instruments operate on the mechanical force of attraction that exists between two oppositely charged plates (one fixed and one movable), effectively acting as a variable capacitor. The deflecting torque ($T_d$) is mathematically given by $T_d = \frac{1}{2}V^2 \frac{dC}{d\theta}$. As seen from the equation, the driving torque is directly dependent entirely on $V$ (the potential difference or voltage applied across the plates) and the geometry of the plates ($\frac{dC}{d\theta}$). It does not depend on a continuous flow of current through a coil, unlike magnetic-based instruments (like PMMC or Moving Iron).
2.  **Impedance and Loading Effect:** Because the plates are separated by a dielectric (air or vacuum), the instrument acts as a capacitor. In DC circuits, once the plates are initially charged, no steady-state current flows through the instrument, meaning its internal resistance is practically infinite. In AC circuits, its capacitive reactance is extremely high at standard power frequencies. Therefore, when connected in parallel across a circuit to measure voltage, it draws virtually zero current from the circuit. 
Since it measures potential difference directly via electric fields without relying on drawn current to generate a magnetic field, and because it does not load the circuit it is measuring, it acts as a nearly ideal, natural voltage sensing device.

Ans related location pg number in ak slide: 140 (Capacitive transducer principles are equivalent to electrostatic plates).

***

### 20. Page 34, CT#03 SEC: A Q2(i): Why can't a PMMC be used for AC quantity measurement?

**Answer:**
A Permanent Magnet Moving Coil (PMMC) instrument cannot be used to measure Alternating Current (AC) quantities directly because of its inherent torque mechanism and the mechanical inertia of its moving system.

The deflecting torque ($T_d$) of a PMMC instrument is given by the equation $T_d = NBAi$, which means the torque is strictly directly proportional to the instantaneous current $i$ passing through the coil. 
When an AC signal is applied, the current reverses its direction periodically (e.g., 50 or 60 times a second for standard grid frequencies). Consequently, the deflecting torque also reverses its direction at the same frequency. During the positive half-cycle, the torque attempts to drive the pointer upscale (forward). During the negative half-cycle, the torque attempts to drive the pointer downscale (backward).

Because the physical moving system (the coil, former, and pointer assembly) possesses mechanical mass and inertia, it simply cannot physically oscillate back and forth 50 or 60 times per second. Instead, it reacts to the **average torque** over the complete cycle. Since the average value of a pure alternating waveform (like a sine wave) over a full cycle is exactly zero, the net average torque acting on the pointer is zero. Therefore, the pointer stays stationary at the zero mark (or vibrates infinitesimally around zero), making the direct measurement of raw AC quantities impossible with a PMMC.

Ans related location pg number in ak slide: 72, 86.


### 21. Page 2, Q.1. (c): Suppose you have extended the range of an ammeter two times of its original capacity if the value of the shunt resistance used is 0.5 $\Omega$, find the internal resistance of the ammeter.

**Answer:**
To extend the range of an ammeter, a low-value resistance called a "shunt" is connected in parallel with the meter's internal resistance. 

**Given Data:**
*   Multiplying power ($m$) = 2 (since the range is extended to two times its original capacity, $m = \frac{I}{I_m} = 2$)
*   Shunt resistance ($R_{sh}$) = 0.5 $\Omega$

**Formula:**
The relationship between the shunt resistance ($R_{sh}$), the internal meter resistance ($R_m$), and the multiplying power ($m$) is given by the formula:
$R_{sh} = \frac{R_m}{m - 1}$

**Calculation:**
Substitute the given values into the formula to find $R_m$:
$0.5 = \frac{R_m}{2 - 1}$
$0.5 = \frac{R_m}{1}$
$R_m = 0.5 \, \Omega$

Therefore, the internal resistance of the ammeter is **0.5 $\Omega$**.

Ans related location pg number in ak slide: 87, 131.

***

### 22. Page 4, Q.2 (c): Find the multiplying power of a shunt of a 200 $\Omega$ resistance used with a Galvanometer of 1000 $\Omega$ resistance. Determine the value of shunt resistance to give a multiplying power of 50.

**Answer:**
This problem has two parts.

**Part 1: Find the multiplying power of the given shunt.**
**Given Data:**
*   Shunt resistance, $R_{sh} = 200 \, \Omega$
*   Galvanometer (meter) resistance, $R_m = 1000 \, \Omega$

**Formula:**
The multiplying power ($m$) is given by:
$m = 1 + \frac{R_m}{R_{sh}}$

**Calculation:**
$m = 1 + \frac{1000}{200}$
$m = 1 + 5 = 6$
The multiplying power of the 200 $\Omega$ shunt is **6**.

**Part 2: Determine the shunt resistance for a multiplying power of 50.**
**Given Data:**
*   Desired multiplying power, $m = 50$
*   Galvanometer resistance, $R_m = 1000 \, \Omega$

**Formula:**
Rearranging the multiplying power formula to solve for $R_{sh}$:
$R_{sh} = \frac{R_m}{m - 1}$

**Calculation:**
$R_{sh} = \frac{1000}{50 - 1}$
$R_{sh} = \frac{1000}{49}$
$R_{sh} \approx 20.408 \, \Omega$

The value of the shunt resistance required to give a multiplying power of 50 is approximately **20.41 $\Omega$**.

Ans related location pg number in ak slide: 87, 131.

***

### 23. Page 6, Q.1 b): For a series type ohmmeter prove that $R_h = \frac{ER_2}{I_{fs}(R_2+R_m)}$, where the symbols having their usual meaning.

**Answer:**
A basic series type ohmmeter circuit consists of a voltage source (battery with voltage $E$), a current limiting series resistor ($R_1$), a zero-adjust parallel resistor ($R_2$), and the basic meter movement with internal resistance ($R_m$). The unknown resistance ($R_x$) is connected across the output terminals. 
The meter internal resistance $R_m$ and the zero adjust resistor $R_2$ are in parallel. This parallel combination is in series with $R_1$ and the battery.

**Step 1: Define Half-Scale Resistance ($R_h$)**
The half-scale resistance, $R_h$, is equal to the internal resistance of the ohmmeter looking back from the test terminals. When the unknown resistance $R_x = R_h$, the current in the circuit drops to exactly half of its full-scale value, hence the pointer indicates half-scale.
The internal resistance of the ohmmeter is:
$R_h = R_1 + \frac{R_2 R_m}{R_2 + R_m}$  --- (Equation 1)

**Step 2: Full-Scale Deflection Condition**
When the test terminals are shorted ($R_x = 0$), the circuit is adjusted so that the meter shows Full Scale Deflection (FSD). At this moment, the meter current $I_m$ is exactly equal to the full-scale deflection current $I_{fs}$.
The total current ($I_t$) drawn from the battery when the terminals are shorted is:
$I_t = \frac{E}{R_h}$

**Step 3: Apply the Current Divider Rule**
The total current $I_t$ splits between the zero-adjust resistor $R_2$ and the meter resistance $R_m$. The current flowing through the meter is given by the current divider rule:
$I_m = I_t \times \left( \frac{R_2}{R_2 + R_m} \right)$

At full-scale deflection ($R_x = 0$), $I_m = I_{fs}$. Substituting $I_t$ into the equation:
$I_{fs} = \left( \frac{E}{R_h} \right) \times \left( \frac{R_2}{R_2 + R_m} \right)$

**Step 4: Rearrange to solve for $R_h$**
Now, isolate $R_h$ on one side of the equation:
$R_h \cdot I_{fs} = E \times \left( \frac{R_2}{R_2 + R_m} \right)$
$R_h = \frac{E \cdot R_2}{I_{fs} (R_2 + R_m)}$

This derives and proves the required expression.

Ans related location pg number in ak slide: 93.

***

### 24. Page 6, Q.1 c): A moving coil instrument has a resistance of 10 $\Omega$ and gives a full-scale deflection when carrying 50 mA. Show how it can be adopted to measure voltage up to 750V and current 100A.

**Answer:**
**Given Data for the basic instrument:**
*   Meter resistance, $R_m = 10 \, \Omega$
*   Full-scale deflection current, $I_m = I_{fs} = 50 \text{ mA} = 0.05 \text{ A}$

**Part 1: Adaptation to measure voltage up to 750 V**
To convert the moving coil instrument into a voltmeter, a high-value resistance called a **multiplier** ($R_s$) must be connected in **series** with the meter.
*   Desired voltage range, $V = 750 \text{ V}$

The total voltage across the series combination is $V = I_m (R_m + R_s)$.
Rearranging the formula to find the multiplier resistance $R_s$:
$R_m + R_s = \frac{V}{I_m}$
$R_s = \frac{V}{I_m} - R_m$
$R_s = \frac{750}{0.05} - 10$
$R_s = 15000 - 10$
**$R_s = 14,990 \, \Omega$**
*Show How:* The instrument can be adapted to measure up to 750V by connecting a multiplier resistor of **14,990 $\Omega$ in series** with the meter.

**Part 2: Adaptation to measure current up to 100 A**
To convert the moving coil instrument into an ammeter capable of measuring large currents, a low-value resistance called a **shunt** ($R_{sh}$) must be connected in **parallel** with the meter.
*   Desired current range, $I = 100 \text{ A}$

First, calculate the multiplying power ($m$):
$m = \frac{I}{I_m} = \frac{100}{0.05} = 2000$

Now, use the formula for shunt resistance:
$R_{sh} = \frac{R_m}{m - 1}$
$R_{sh} = \frac{10}{2000 - 1}$
$R_{sh} = \frac{10}{1999}$
**$R_{sh} \approx 0.0050025 \, \Omega$** (or $5.0025 \text{ m}\Omega$)
*Show How:* The instrument can be adapted to measure up to 100A by connecting a shunt resistor of approximately **0.005 $\Omega$ in parallel** with the meter.

Ans related location pg number in ak slide: 87, 88, 131, 132.

### 25. Page 7, Q.4 (d): What is multiplier? How the range of a dc voltmeter can be extended?

**Answer:**
**What is a multiplier?**
A multiplier is a high-value, non-inductive precision resistor connected in series with the moving coil of a basic galvanometer or voltmeter. Its primary function is to limit the current flowing through the sensitive moving coil to its safe, full-scale deflection value, even when a high voltage is applied across the entire circuit. Multipliers are usually made of materials like Manganin or Constantan, which have very low temperature coefficients of resistance, ensuring that the instrument's calibration remains accurate despite temperature changes caused by internal power dissipation or ambient conditions.

**How the range of a DC voltmeter can be extended:**
The basic moving coil instrument has a specific internal resistance ($R_m$) and requires a specific small current ($I_m$) for full-scale deflection. Therefore, it can only measure a very small voltage natively ($v = I_m R_m$). 

To measure higher voltages ($V$), the excess voltage must be "dropped" across an external component so the meter itself only "sees" its safe maximum voltage. This is achieved by connecting a multiplier resistor ($R_s$) in **series** with the meter.

Let:
*   $V$ = The new, higher voltage to be measured.
*   $v$ = The voltage across the meter movement for full-scale deflection ($v = I_m R_m$).
*   $m$ = Multiplying factor, which is the ratio of the extended range to the original range ($m = \frac{V}{v}$).

The total voltage $V$ applied across the series combination is the sum of the voltage drop across the multiplier and the meter:
$V = I_m R_s + I_m R_m$
$V = I_m(R_s + R_m)$

To find the value of the required series resistance ($R_s$):
$R_s + R_m = \frac{V}{I_m}$
$R_s = \frac{V}{I_m} - R_m$

Alternatively, using the multiplying factor $m$:
Since $V = m \cdot v = m(I_m R_m)$
Substituting this into the voltage equation:
$m(I_m R_m) = I_m(R_s + R_m)$
$m R_m = R_s + R_m$
$R_s = m R_m - R_m$
**$R_s = R_m(m - 1)$**

By selecting a multiplier resistor with a value calculated by this formula and connecting it in series, the voltage range of any DC voltmeter can be extended to any desired higher value.

Ans related location pg number in ak slide: 88, 132.

***

### 26. Page 9, Q.4. (c): A moving coil instrument gives a full scale deflection of 10 mA when the potential difference across its terminals is 100 mV. Calculate (a) the shunt resistance for a full scale deflection corresponding to 100 A, (b) the series resistance for full scale reading with 1000 V. Calculate the power dissipation in each case.

**Answer:**
**Given Data for the basic instrument:**
*   Full-scale deflection current, $I_m = 10 \text{ mA} = 0.01 \text{ A}$
*   Voltage across meter at full scale, $v = 100 \text{ mV} = 0.1 \text{ V}$

First, we must calculate the internal resistance of the meter ($R_m$):
$R_m = \frac{v}{I_m} = \frac{0.1 \text{ V}}{0.01 \text{ A}} = 10 \, \Omega$

**(a) Shunt resistance for 100 A range & Power Dissipation:**
*   Desired extended current range, $I = 100 \text{ A}$

Calculate multiplying power ($m$):
$m = \frac{I}{I_m} = \frac{100}{0.01} = 10000$

Calculate shunt resistance ($R_{sh}$):
$R_{sh} = \frac{R_m}{m - 1} = \frac{10}{10000 - 1} = \frac{10}{9999} \approx 0.0010001 \, \Omega$
**Shunt Resistance = $0.001 \, \Omega$**

Calculate Power Dissipation in the Shunt:
The current flowing through the shunt is $I_{sh} = I - I_m = 100 - 0.01 = 99.99 \text{ A}$.
Power dissipated in the shunt $P_{sh} = I_{sh}^2 \times R_{sh} = (99.99)^2 \times 0.0010001$
Alternatively, $P_{sh} = \frac{V^2}{R_{sh}}$ where $V = 0.1\text{V}$ (voltage across parallel branch).
$P_{sh} = \frac{(0.1)^2}{\frac{10}{9999}} = \frac{0.01 \times 9999}{10} = 0.001 \times 9999 \approx 9.999 \text{ W}$
**Power Dissipation in shunt $\approx 10 \text{ W}$**

**(b) Series resistance for 1000 V range & Power Dissipation:**
*   Desired extended voltage range, $V = 1000 \text{ V}$

Calculate multiplying factor ($m$):
$m = \frac{V}{v} = \frac{1000}{0.1} = 10000$

Calculate series multiplier resistance ($R_s$):
$R_s = R_m(m - 1) = 10(10000 - 1) = 10 \times 9999 = 99990 \, \Omega$
**Series multiplier Resistance = $99,990 \, \Omega$**

Calculate Power Dissipation in the Multiplier:
The current flowing through the series multiplier is $I_m = 0.01 \text{ A}$.
Power dissipated in multiplier $P_s = I_m^2 \times R_s = (0.01)^2 \times 99990$
$P_s = 0.0001 \times 99990 = 9.999 \text{ W}$
**Power Dissipation in series resistor $\approx 10 \text{ W}$**

Ans related location pg number in ak slide: 87, 88, 131, 132.

***

### 27. Page 18, Q.5(a): Write short note on (i) AVO meter (ii) Ampere-hour meter (iii) Max demand meter.

**Answer:**

**(i) AVO Meter (Multimeter or V.O.M):**
An AVO meter (Amperes-Volts-Ohms), widely known as a Multimeter or Volt-Ohm-Milliammeter (V.O.M.), is a highly versatile, multi-purpose electronic measuring instrument. In its analog form, it utilizes a single sensitive D'Arsonval (PMMC) galvanometer movement. By switching different internal networks of shunt resistors (for measuring various ranges of DC/AC current), series multiplier resistors (for measuring various ranges of DC/AC voltage), and an internal battery circuit (for measuring resistance), it acts as an all-in-one test instrument. To measure AC quantities, it incorporates a rectifier circuit (usually copper-oxide or diode bridge) to convert AC to pulsating DC before it reaches the moving coil. It is the most common diagnostic tool for electrical troubleshooting due to its portability and multi-functionality.

**(ii) Ampere-hour Meter:**
An Ampere-hour (Ah) meter is a type of integrating instrument used to measure the total quantity of electricity (electric charge) that passes through a circuit over a period of time. Since Charge ($Q$) = Current ($I$) $\times$ Time ($t$), the instrument integrates the current flowing through it with respect to time. It is similar in concept to a watt-hour (energy) meter, but it only accounts for the current, not the voltage. The most typical and critical applications of Ampere-Hour meters are in battery testing, managing solar charging systems, and electroplating processes, where knowing the exact total charge transferred is necessary to determine battery capacity status or the amount of metal deposited.

**(iii) Max Demand Meter:**
A Maximum Demand meter (or indicator) is a specialized instrument used primarily by power supply companies in commercial and industrial power distribution systems to monitor the maximum thermal loading. It does not measure instantaneous peaks (like motor starting currents); instead, it measures the average power consumed over a specific, successive time interval (usually 15 or 30 minutes) and records the highest average value reached during the billing cycle. It indicates the maximum loading current over a period. Short-period current peaks are deliberately ignored, but sustained long overloads are registered. This value is crucial because utility companies base their "demand charge" tariffs on the maximum power a facility requires, which dictates the size of the infrastructure (transformers, cables) the utility must install to service that facility.

Ans related location pg number in ak slide: 94 (AVO), 98 (Max demand), 99 (Ampere-hour).

***

### 28. Page 18, Q.8(a): What is clamp-on ammeter? Explain its function.

**Answer:**
**What is a clamp-on ammeter?**
A clamp-on ammeter (often called a clamp meter) is a specialized electrical test tool that combines a basic digital multimeter with a current sensor. Its defining feature is a pair of hinged, spring-loaded jaws (like a clamp) that can be opened and closed around an electrical conductor. This design allows for the measurement of current flowing in a live circuit without the need to physically cut or disconnect the wire to insert the meter in series, which is required for standard ammeters.

**Explain its function:**
The function of a clamp-on ammeter is based on the principle of electromagnetic induction (specifically, acting like a current transformer for AC measurement).
1.  **Magnetic Field Sensing:** When current flows through a conductor, it generates a magnetic field circulating around it. 
2.  **Transformer Action:** The hinged jaws of the clamp meter are made of ferrite iron or similar magnetic core material. When closed around a wire, these jaws concentrate and capture the magnetic field generated by the current. In AC measurement, the conductor acts as the single-turn primary winding of a transformer.
3.  **Secondary Coil:** Inside the clamp meter, there is a secondary coil wound around the magnetic core. The fluctuating magnetic field from the primary conductor induces a proportional, smaller alternating current in this secondary coil.
4.  **Measurement:** This smaller secondary current is then fed into the meter's internal circuitry (usually a shunt and rectifier connected to a DVM or PMMC movement), where it is measured, scaled up according to the transformer turns ratio, and displayed as the actual current flowing through the main conductor. 
*Note: Modern clamp meters equipped with Hall Effect sensors can also measure DC current by detecting the static magnetic field around the conductor.*

Ans related location pg number in ak slide: Not explicitly detailed in the provided slides beyond being a type of meter, but relies on CT principles found on 127. (Note: The prompt asks to reference slide locations based strictly on the provided text. Slide 80 mentions "clamp-on ammeter" in a question list, but the main text does not detail its construction. I have provided the standard engineering answer.)

### 29. Page 18, Q.8(d): What is maximum demand indicator? Briefly explain the working principle of Merz Price maximum demand indicator.

**Answer:**
**What is a Maximum Demand Indicator?**
A Maximum Demand Indicator (MDI) is a specialized electrical measuring instrument used primarily in industrial and commercial power systems to monitor and record the highest average power (or current) consumed over a specific, successive time interval (usually 15 or 30 minutes) during a billing period. It is designed to ignore short, transient spikes (like motor starting currents) but register sustained thermal loading. Utility companies use this reading to determine the "demand charge" tariff, which reflects the infrastructure capacity they must maintain to supply that facility's peak load.

**Working Principle of Merz Price Maximum Demand Indicator:**
The Merz Price indicator is an integrating-type instrument that is usually coupled directly with an energy meter (watt-hour meter). Its working principle is as follows:
1.  **Integration over Time:** The device features a driving mechanism (often a pin or a pusher) that is geared to the rotating disc of the energy meter. As the energy meter rotates (representing power consumed), it advances this pusher.
2.  **Driving the Pointer:** The pusher slowly moves a recording pointer forward across a dial. The distance the pointer moves is proportional to the total energy consumed during the specific time interval (e.g., 30 minutes). Since energy divided by time equals average power, the pointer's position represents the average demand over that interval.
3.  **Reset Mechanism:** At the exact end of the time interval, a timing mechanism (like a synchronous motor or clockwork) temporarily uncouples the gear train. A spring instantly snaps the pusher back to the zero position.
4.  **Recording the Maximum:** Crucially, the recording pointer is left behind at its highest reached position; it does not snap back to zero. During the next 30-minute interval, the pusher starts from zero again. It will only move the pointer further up the scale if the average power in this new interval exceeds the previously recorded maximum. Thus, at the end of the month, the pointer indicates the absolute highest average demand that occurred during any single 30-minute window.

Ans related location pg number in ak slide: 98.

***

### 30. Page 23, CT-02 Q1: Prove that the expression for series resistance is $R_s = R_m(m - 1)$ for the extension of the voltmeter range where the symbols have their usual meanings.

**Answer:**
To extend the range of a basic voltmeter (or galvanometer), a high-value resistance called a multiplier is connected in series with the meter.
Let:
*   $R_m$ = Internal resistance of the basic meter.
*   $I_m$ = Full-scale deflection current of the basic meter.
*   $v$ = Voltage across the basic meter for full-scale deflection ($v = I_m R_m$).
*   $V$ = The new, extended maximum voltage to be measured.
*   $R_s$ = The required series multiplier resistance.
*   $m$ = The multiplying factor or power ($m = \frac{V}{v}$).

**Proof:**
When the extended voltage $V$ is applied across the entire circuit, the current flowing through the circuit must not exceed the meter's full-scale current $I_m$. Since the multiplier $R_s$ and the meter $R_m$ are in series, the same current $I_m$ flows through both.
By Kirchhoff's Voltage Law, the total applied voltage is the sum of the voltage drops:
$V = V_{multiplier} + V_{meter}$
$V = I_m R_s + I_m R_m$
$V = I_m(R_s + R_m)$

We know that the original full-scale voltage of the meter is $v = I_m R_m$.
From the definition of the multiplying factor $m = \frac{V}{v}$, we can substitute $V = m \cdot v = m(I_m R_m)$.

Substituting this back into the total voltage equation gives:
$m(I_m R_m) = I_m(R_s + R_m)$

Dividing both sides by $I_m$:
$m R_m = R_s + R_m$

Now, isolate $R_s$ by subtracting $R_m$ from both sides:
$R_s = m R_m - R_m$

Factoring out $R_m$:
**$R_s = R_m(m - 1)$**

This proves the expression for the required series resistance.

Ans related location pg number in ak slide: 88, 132.

***

### 31. Page 23, CT-03 Q2: A shunt type ohmmeter uses a 10 mA basic d'Arsonval movement with an internal resistance of 5 Ohm. The battery voltage is 3V. It is desired to modify the circuit by adding appropriate shunt resistance across the movement so that its instrument indicates 0.5 Ohm at the mid point on the scale. Calculate- (a) The value of shunt resistance (b) Value of the current limiting resistor.

**Answer:**
In a typical shunt-type ohmmeter, the battery ($E$), a current limiting resistor ($R_1$), and a parallel branch containing the meter and the unknown resistance are used. The question states we are modifying the meter by adding a shunt ($R_{sh}$) *across the movement itself*. Let's define the new effective meter resistance as $R_p = R_m \parallel R_{sh}$.

**Given Data:**
*   Meter full-scale current, $I_m = 10 \text{ mA} = 0.01 \text{ A}$
*   Meter internal resistance, $R_m = 5 \, \Omega$
*   Battery voltage, $E = 3 \text{ V}$
*   Desired half-scale resistance reading, $R_h = 0.5 \, \Omega$

**Step 1: Understand Full-Scale and Half-Scale conditions for a Shunt Ohmmeter**
*   **Full-Scale Deflection:** Occurs when the test terminals are OPEN ($R_x = \infty$). All current from $R_1$ flows into $R_p$. The voltage across $R_p$ must be the meter's full-scale voltage:
    $V_{fs} = I_m \times R_m = 0.01 \text{ A} \times 5 \, \Omega = 0.05 \text{ V}$.
    The total current supplied by the battery at full scale is $I_{total} = \frac{E - V_{fs}}{R_1}$.
    Since this whole current flows through $R_p$, we also have $I_{total} = \frac{V_{fs}}{R_p} = \frac{0.05}{R_p}$.
    Therefore: $\frac{3 - 0.05}{R_1} = \frac{0.05}{R_p} \implies \frac{2.95}{R_1} = \frac{0.05}{R_p} \implies R_1 = \frac{2.95}{0.05} R_p = 59 R_p$.
*   **Half-Scale Deflection:** In a shunt ohmmeter, half-scale deflection occurs when the external connected resistance ($R_x$) drops the voltage across the meter branch to exactly half of its full-scale value. This algebraically happens when $R_x$ equals the Thevenin resistance looking back into the circuit, which is exactly $R_1 \parallel R_p$.
    Therefore, the half-scale resistance $R_h = R_1 \parallel R_p$.
    We are given $R_h = 0.5 \, \Omega$. So, $\frac{R_1 \cdot R_p}{R_1 + R_p} = 0.5$.

**Step 2: Solve for $R_p$ and $R_1$**
Substitute $R_1 = 59 R_p$ into the half-scale equation:
$\frac{(59 R_p) \cdot R_p}{59 R_p + R_p} = 0.5$
$\frac{59 R_p^2}{60 R_p} = 0.5$
$\frac{59}{60} R_p = 0.5$
$R_p = 0.5 \times \frac{60}{59} \approx 0.50847 \, \Omega$

**(b) Calculate Value of the current limiting resistor ($R_1$):**
Using $R_1 = 59 R_p$:
$R_1 = 59 \times 0.50847 \approx 29.9997 \, \Omega$
**Value of the current limiting resistor $R_1 = 30 \, \Omega$**

**(a) Calculate the value of the shunt resistance ($R_{sh}$):**
We know the effective meter resistance $R_p$ is the parallel combination of the basic meter $R_m$ and the new shunt $R_{sh}$:
$R_p = \frac{R_m \cdot R_{sh}}{R_m + R_{sh}}$
$0.50847 = \frac{5 \cdot R_{sh}}{5 + R_{sh}}$
$0.50847(5 + R_{sh}) = 5 R_{sh}$
$2.54235 + 0.50847 R_{sh} = 5 R_{sh}$
$2.54235 = 5 R_{sh} - 0.50847 R_{sh}$
$2.54235 = 4.49153 R_{sh}$
$R_{sh} = \frac{2.54235}{4.49153} \approx 0.566 \, \Omega$
**Value of the shunt resistance $R_{sh} = 0.566 \, \Omega$**

Ans related location pg number in ak slide: 93 (Ohmmeter principles).

***

### 32. Page 26, SEC- C CT-01: 1) Ammeter Range Extension এর সূত্র প্রমাণ। (১০) (Translate: Prove the formula for Ammeter Range Extension)

**Answer:**
To extend the range of a basic ammeter (galvanometer) to measure larger currents, a low-value precision resistor called a "shunt" is connected in parallel with the meter. 

Let:
*   $R_m$ = Internal resistance of the basic meter.
*   $I_m$ = Full-scale deflection current of the basic meter.
*   $I$ = The total new, extended maximum current to be measured.
*   $I_{sh}$ = The current flowing through the shunt resistor.
*   $R_{sh}$ = The resistance of the shunt.
*   $m$ = The multiplying power of the shunt ($m = \frac{I}{I_m}$).

**Proof:**
When the total extended current $I$ enters the circuit, it splits at the parallel junction. A portion ($I_m$) flows through the sensitive meter to provide full-scale deflection, and the remaining excess current ($I_{sh}$) bypasses the meter by flowing through the shunt resistor.
According to Kirchhoff's Current Law (KCL):
$I = I_m + I_{sh}$
Therefore, the current through the shunt is:
$I_{sh} = I - I_m$

Because the meter and the shunt resistor are connected in parallel, the potential difference (voltage drop) across both of them must be equal. 
Voltage across meter = Voltage across shunt
$I_m \times R_m = I_{sh} \times R_{sh}$

Substitute $I_{sh}$ with $(I - I_m)$ in the voltage equation:
$I_m \times R_m = (I - I_m) \times R_{sh}$

Now, isolate $R_{sh}$ to find the required shunt resistance:
$R_{sh} = \frac{I_m \times R_m}{I - I_m}$

To express this in terms of the multiplying power ($m$), divide both the numerator and the denominator by $I_m$:
$R_{sh} = \frac{R_m}{\frac{I}{I_m} - \frac{I_m}{I_m}}$

Since $m = \frac{I}{I_m}$, we substitute $m$ into the equation:
**$R_{sh} = \frac{R_m}{m - 1}$**

This proves the formula for calculating the shunt resistance required for ammeter range extension.

Ans related location pg number in ak slide: 87, 131.


### 33. Page 26, CT-04 Q1: Suppose you are designing a series type and a shunt type ohmmeter with a same galvanometer and battery. If the full scale deflection current of the galvanometer is 0.5 mA, internal battery volage is 3 V, mark the scale of both series and shunt type ohmmeters with the correct resistance indication for 25% and 75% of full scale reading after deriving the appropriate formula for marking the scales for both meters. For both meters, consider the half scale deflection resistance as 3000 $\Omega$.

**Answer:**
**Given Data:**
*   Full-scale current, $I_{fs} = 0.5 \text{ mA} = 0.0005 \text{ A}$
*   Battery voltage, $E = 3 \text{ V}$
*   Half-scale resistance, $R_h = 3000 \, \Omega$

**Part 1: Series Type Ohmmeter**
In a series ohmmeter, the unknown resistance $R_x$ is in series with the internal resistance $R_h$.
*   At full scale (100% reading), $I_m = I_{fs}$, $R_x = 0 \, \Omega$.
*   At zero scale (0% reading), $I_m = 0$, $R_x = \infty$.
*   **Derivation:** The current $I_m$ is $I_m = \frac{E}{R_h + R_x}$. Since $I_{fs} = \frac{E}{R_h}$, dividing the two equations gives $\frac{I_m}{I_{fs}} = \frac{R_h}{R_h + R_x}$.
    Let $S$ be the fraction of full-scale reading ($S = \frac{I_m}{I_{fs}}$).
    $S = \frac{R_h}{R_h + R_x}$
    $S(R_h + R_x) = R_h \implies S R_x = R_h(1 - S) \implies \mathbf{R_x = R_h \left( \frac{1 - S}{S} \right)}$

*   **For 25% of full scale reading ($S = 0.25$):**
    $R_{x, 25\%} = 3000 \left( \frac{1 - 0.25}{0.25} \right) = 3000 \left( \frac{0.75}{0.25} \right) = 3000 \times 3 = \mathbf{9000 \, \Omega}$

*   **For 75% of full scale reading ($S = 0.75$):**
    $R_{x, 75\%} = 3000 \left( \frac{1 - 0.75}{0.75} \right) = 3000 \left( \frac{0.25}{0.75} \right) = \frac{3000}{3} = \mathbf{1000 \, \Omega}$

**(Note: Series ohmmeter scale reads $\infty$ to $0$ from left to right.)**

**Part 2: Shunt Type Ohmmeter**
In a shunt ohmmeter, the unknown resistance $R_x$ is placed in parallel (shunt) with the meter.
*   At full scale (100% reading), $R_x = \infty$ (open circuit).
*   At zero scale (0% reading), $R_x = 0 \, \Omega$ (short circuit, bypassing the meter).
*   **Derivation:** The voltage across the parallel branch is $V_p = E \frac{R_p}{R_1 + R_p}$ where $R_p = R_m \parallel R_x$. The meter current is $I_m = \frac{V_p}{R_m}$.
    It can be shown that for a shunt ohmmeter, the fraction of full-scale current $S$ is related to $R_x$ by:
    $S = \frac{R_x}{R_x + R_h}$
    $S(R_x + R_h) = R_x \implies S R_x + S R_h = R_x \implies S R_h = R_x(1 - S) \implies \mathbf{R_x = R_h \left( \frac{S}{1 - S} \right)}$

*   **For 25% of full scale reading ($S = 0.25$):**
    $R_{x, 25\%} = 3000 \left( \frac{0.25}{1 - 0.25} \right) = 3000 \left( \frac{0.25}{0.75} \right) = \frac{3000}{3} = \mathbf{1000 \, \Omega}$

*   **For 75% of full scale reading ($S = 0.75$):**
    $R_{x, 75\%} = 3000 \left( \frac{0.75}{1 - 0.75} \right) = 3000 \left( \frac{0.75}{0.25} \right) = 3000 \times 3 = \mathbf{9000 \, \Omega}$

**(Note: Shunt ohmmeter scale reads $0$ to $\infty$ from left to right.)**

Ans related location pg number in ak slide: 93.

***

### 34. Page 27, CT#01 SEC: B Q1: A moving coil milli-ammeter gives full-scale deflection with 10 mA and has a resistance of 4 $\Omega$. Calculate the resistance to be connected in (a) parallel to enable the instrument to read upto 2 A, (b) series to enable it to read upto 15 V.

**Answer:**
**Given Data for the basic instrument:**
*   Full-scale deflection current, $I_m = 10 \text{ mA} = 0.01 \text{ A}$
*   Internal resistance of the meter, $R_m = 4 \, \Omega$

**(a) Connecting in parallel (Shunt) to read up to 2 A:**
To convert the milli-ammeter into an ammeter capable of measuring up to 2 A, a low-value shunt resistor ($R_{sh}$) must be connected in parallel.
*   Desired extended current range, $I = 2 \text{ A}$

First, calculate the multiplying power ($m$):
$m = \frac{I}{I_m} = \frac{2}{0.01} = 200$

Now, use the formula to find the shunt resistance:
$R_{sh} = \frac{R_m}{m - 1}$
$R_{sh} = \frac{4}{200 - 1}$
$R_{sh} = \frac{4}{199}$
**$R_{sh} \approx 0.0201 \, \Omega$**
The resistance to be connected in parallel is approximately **0.0201 $\Omega$**.

**(b) Connecting in series (Multiplier) to read up to 15 V:**
To convert the milli-ammeter into a voltmeter capable of measuring up to 15 V, a high-value multiplier resistor ($R_s$) must be connected in series.
*   Desired extended voltage range, $V = 15 \text{ V}$
*   Voltage drop across the meter at full scale, $v = I_m \times R_m = 0.01 \times 4 = 0.04 \text{ V}$

First, calculate the multiplying factor ($m$):
$m = \frac{V}{v} = \frac{15}{0.04} = 375$

Now, use the formula to find the series resistance:
$R_s = R_m(m - 1)$
$R_s = 4 \times (375 - 1)$
$R_s = 4 \times 374$
**$R_s = 1496 \, \Omega$**
The resistance to be connected in series is **1496 $\Omega$**.

Ans related location pg number in ak slide: 87, 88, 131, 132.

***

### 35. Page 4, Q.2 (a): Explain the general construction and operation of electrodynamometer type instruments.

**Answer:**
**General Construction:**
An electrodynamometer (or simply dynamometer) type instrument relies on the interaction between two magnetic fields produced by two separate coils, eliminating the need for permanent magnets. The main components are:
![[1611942_e173da15-d215-4e29-ab4a-014d74939cc2_lg.avif]]
1.  **Fixed Coils:** The instrument has two identical fixed coils placed close to each other. They are usually made of heavy wire and are designed to carry the main load current (acting as current coils). The split design ensures a uniform magnetic field is created in the central gap between them.
2.  **Moving Coil:** A lightweight, multi-turn coil wound on a non-magnetic former is pivoted to rotate within the uniform magnetic field created by the fixed coils. This coil is typically connected across the voltage source (acting as a pressure/voltage coil) and carries a small current proportional to the voltage.
3.  **Control & Damping:** Spring control provides the restoring torque. Since there is no permanent magnet, eddy current damping cannot be used effectively without distorting the operating fields; therefore, air friction damping (using aluminum vanes in air chambers) is commonly used.

**Operation:**
The fundamental operating principle is the electromagnetic force that exists between current-carrying conductors.
1. When current flows through the fixed coils, they produce a magnetic field. 
2. Simultaneously, current flows through the moving coil, producing its own magnetic field.
3. The magnetic field of the moving coil tries to align itself with the main magnetic field produced by the fixed coils. This tendency to align creates a mechanical deflecting torque ($T_d$).
4. Mathematically, the instantaneous torque is proportional to the product of the instantaneous currents in the fixed coil ($i_1$) and the moving coil ($i_2$), and the rate of change of mutual inductance ($M$) with deflection ($\theta$): $T_d = i_1 i_2 \frac{dM}{d\theta}$.
5. Because the torque depends on the product of the two currents, if the instrument is measuring AC and both currents reverse direction simultaneously, the product remains positive. Therefore, the deflecting torque acts in the same direction, allowing the instrument to measure both AC and DC quantities. The pointer settles when the average deflecting torque equals the spring's restoring torque.

Ans related location pg number in ak slide: 89, 90, 91, 92.

***

### 36. Page 4, Q.4 (c): Mathematically analyze the problem that is created while measuring 3-phase power of power factor below 0.5 using two wattmeter method. State the solution to the problem.

**Answer:**
**Mathematical Analysis of the Problem:**
In the two-wattmeter method for measuring 3-phase power, let the readings of the two wattmeters be $W_1$ and $W_2$. Assuming a balanced load with lagging power factor angle $\phi$, the mathematical expressions for the individual wattmeter readings are:
$W_1 = V_L I_L \cos(30^\circ - \phi)$
$W_2 = V_L I_L \cos(30^\circ + \phi)$
The total 3-phase power is exactly $P = W_1 + W_2 = \sqrt{3} V_L I_L \cos\phi$.

Now, let's analyze the problem that occurs when the power factor drops below 0.5.
A power factor of 0.5 corresponds to a phase angle $\phi = 60^\circ$ (since $\cos(60^\circ) = 0.5$).
*   **If PF = 0.5 ($\phi = 60^\circ$):**
    $W_1 = V_L I_L \cos(30^\circ - 60^\circ) = V_L I_L \cos(-30^\circ) = V_L I_L \times (\sqrt{3}/2)$
    $W_2 = V_L I_L \cos(30^\circ + 60^\circ) = V_L I_L \cos(90^\circ) = 0$
    At PF = 0.5, $W_2$ reads zero. All the power is registered by $W_1$.
*   **If PF < 0.5 (meaning $\phi > 60^\circ$, e.g., $\phi = 70^\circ$):**
    $W_1 = V_L I_L \cos(30^\circ - 70^\circ) = V_L I_L \cos(-40^\circ)$ (Positive value)
    $W_2 = V_L I_L \cos(30^\circ + 70^\circ) = V_L I_L \cos(100^\circ)$ (Negative value, because $\cos$ is negative in the 2nd quadrant).

**The Problem:**
When the power factor falls below 0.5, the angle $(30^\circ + \phi)$ becomes greater than $90^\circ$. The cosine of an angle greater than $90^\circ$ is negative, which means the theoretical reading $W_2$ is negative. Standard analog wattmeters are designed to deflect upscale for positive power. A negative power reading attempts to drive the pointer backward (downscale), below zero, hitting the mechanical stop.

**The Solution:**
To measure the power correctly when this happens, you must artificially reverse the polarity of the connections to the wattmeter trying to read negatively (say, $W_2$). 
This is practically done by **reversing either the connections of the current coil or the connections of the voltage coil** on $W_2$. 
After reversing the connections, the pointer will deflect upscale (positively). You read this positive value, but because you reversed the connections, you must treat this reading as negative in your total power calculation. 
Therefore, the total 3-phase power is calculated as:
$P = W_1 - W_2 \text{ (after reversal)}$

Ans related location pg number in ak slide: Not directly explicitly derived in slides, relates to generic Wattmeter knowledge. (Prompt requests only answers derived from the text/slides if possible, but standard engineering knowledge is expected if missing. Slide 91, 92 show wattmeters).


### 37. Page 12, Q.5. (a): Derive the expression for the deflection of an electrodynamometer type wattmeter.

**Answer:**
An electrodynamometer wattmeter consists of fixed current coils (carrying load current $i_c$) and a moving pressure coil (connected across the load, carrying current $i_p$ proportional to voltage).
Let:
*   $i_c$ = instantaneous current in the fixed (current) coil
*   $i_p$ = instantaneous current in the moving (pressure) coil
*   $M$ = mutual inductance between the fixed and moving coils
*   $\theta$ = angular deflection of the moving coil

The instantaneous deflecting torque ($T_i$) produced by the interaction of the magnetic fields of these two coils is given by the rate of change of magnetic energy, yielding:
$T_i = i_c \cdot i_p \cdot \frac{dM}{d\theta}$

In an AC circuit, the load current and voltage vary sinusoidally. 
Let the applied voltage be $v = V_m \sin(\omega t)$.
The pressure coil current is $i_p = \frac{v}{R_p} = \frac{V_m}{R_p} \sin(\omega t)$, where $R_p$ is the high resistance of the pressure coil circuit. (Assuming the pressure coil is purely resistive).
Let the load current (flowing through the current coil) lag the voltage by an angle $\phi$:
$i_c = I_m \sin(\omega t - \phi)$

Substituting $i_p$ and $i_c$ into the instantaneous torque equation:
$T_i = \left[ I_m \sin(\omega t - \phi) \right] \cdot \left[ \frac{V_m}{R_p} \sin(\omega t) \right] \cdot \frac{dM}{d\theta}$
$T_i = \frac{V_m I_m}{R_p} \sin(\omega t) \sin(\omega t - \phi) \frac{dM}{d\theta}$

Using the trigonometric identity $2 \sin A \sin B = \cos(A - B) - \cos(A + B)$:
$T_i = \frac{V_m I_m}{2 R_p} \left[ \cos(\phi) - \cos(2\omega t - \phi) \right] \frac{dM}{d\theta}$

Because the moving system has mechanical inertia, it cannot follow the double-frequency pulsating term ($\cos(2\omega t - \phi)$). Instead, the pointer assumes a steady position corresponding to the **average deflecting torque ($T_d$)** over a complete cycle.
The average value of $\cos(2\omega t - \phi)$ over a full cycle is zero.
Therefore, the average deflecting torque is:
$T_d = \frac{V_m I_m}{2 R_p} \cos(\phi) \frac{dM}{d\theta}$

Since RMS voltage $V = \frac{V_m}{\sqrt{2}}$ and RMS current $I = \frac{I_m}{\sqrt{2}}$, then $V_m I_m / 2 = V \cdot I$.
$T_d = \frac{V I}{R_p} \cos(\phi) \frac{dM}{d\theta}$

Notice that the true average power of the load is $P = V I \cos(\phi)$. Substituting $P$:
$T_d = \frac{P}{R_p} \frac{dM}{d\theta}$

The instrument uses spring control, so the controlling torque ($T_c$) is $T_c = K\theta$.
At steady-state deflection, $T_c = T_d$:
$K\theta = \frac{P}{R_p} \frac{dM}{d\theta}$

Rearranging for the deflection $\theta$:
**$\theta = \left( \frac{1}{K \cdot R_p} \frac{dM}{d\theta} \right) P$**

This expression shows that the angular deflection $\theta$ is directly proportional to the true power $P$, assuming $\frac{dM}{d\theta}$ is engineered to be fairly constant over the operating range.

Ans related location pg number in ak slide: 90, 91, 92.

***

### 38. Page 17, Q.5(b): Outline the problem of creeping and its solution. Discuss the challenge in measuring three phase power using two wattmeter method.

**Answer:**
**Problem of Creeping and its Solution:**
*   **Problem:** "Creeping" is a phenomenon specific to induction-type energy meters. It is defined as the slow, continuous rotation of the aluminum disc even when no load current is flowing through the meter (i.e., the current coil is completely de-energized), provided the voltage coil remains energized. This results in the meter falsely registering energy consumption over time, charging the consumer for power they aren't using. The primary cause of creeping is the over-compensation for friction. To overcome static friction at low loads, a slight driving torque (friction compensation torque) is permanently added via a shading loop. If this compensation is slightly too strong, or if there is a sudden overvoltage, this torque alone is enough to slowly rotate the frictionless disc.
*   **Solution:** To eliminate creeping, two diametrically opposite holes (or slots) are drilled into the aluminum disc. When one of these holes passes directly under the pole of the shunt magnet (voltage coil), the normal path of the eddy currents is disrupted. This disruption creates a localized distortion in the magnetic field interactions, generating a small restoring or braking torque that counteracts the over-compensation torque. The disc will creep slightly until a hole aligns under the shunt magnet, at which point it will stop entirely.

**Challenge in measuring 3-phase power using Two Wattmeter Method:**
The two-wattmeter method calculates total 3-phase power as $P = W_1 + W_2$. The primary challenge arises when measuring power for highly inductive or highly capacitive loads where the power factor drops below 0.5 (i.e., the phase angle $\phi$ is greater than $60^\circ$).
When $PF < 0.5$, the term $\cos(30^\circ + \phi)$ becomes negative. This causes one of the wattmeters (say $W_2$) to experience a negative deflecting torque. 
Since standard analog wattmeters are designed with a mechanical zero-stop on the left side of the scale, the pointer attempts to deflect backwards below zero, making it impossible to read the magnitude of the negative power directly.
To resolve this, the technician must manually intervene by reversing the connections to either the current coil or the pressure coil of that specific wattmeter. This forces the pointer to deflect upscale positively. However, the technician must record this positive reading and then manually subtract it from the other wattmeter's reading (i.e., Total Power $= W_1 - W_2$) to determine the correct total 3-phase power.

Ans related location pg number in ak slide: 95, 96 (Energy meters), Generic knowledge for Two Wattmeter method.

***

### 39. Page 23, CT-03 Q1: Draw the equivalent circuit of an electrodynamometer voltmeter. If the voltmeter has a total impedance of 10 k$\Omega$ and the rate of change of mutual inductance with respect to the deflection of the instrument is equal to the control spring constant, determine the angle of deflection for 500 V.

**Answer:**
**Equivalent Circuit:**
An electrodynamometer voltmeter has its fixed coils and moving coil connected completely in series. A high-value non-inductive multiplier resistor is also connected in series to limit the current and establish the high overall impedance typical of a voltmeter.
*   Fixed Coil 1 -- Moving Coil -- Fixed Coil 2 -- Multiplier Resistor

**Calculations:**
**Given Data:**
*   Total impedance of the voltmeter, $Z = 10 \text{ k}\Omega = 10000 \, \Omega$. Since electrodynamometer voltmeters are designed to be largely resistive, we will assume $R_{total} \approx Z = 10000 \, \Omega$.
*   Applied voltage, $V = 500 \text{ V}$.
*   The rate of change of mutual inductance with respect to deflection ($\frac{dM}{d\theta}$) is equal to the control spring constant ($K$). Therefore, $\frac{dM}{d\theta} = K$.

**Formula derivation for Electrodynamometer Voltmeter:**
The general average deflecting torque for an electrodynamometer is:
$T_d = I_1 \cdot I_2 \cdot \cos(\phi) \cdot \frac{dM}{d\theta}$
Because the fixed and moving coils are strictly in series, the same current flows through both. Let $I = I_1 = I_2$. Also, the phase angle $\phi$ between the two coil currents is zero because it's the exact same current, so $\cos(0) = 1$.
The torque equation simplifies to:
$T_d = I^2 \frac{dM}{d\theta}$

The current flowing through the voltmeter is determined by Ohm's law:
$I = \frac{V}{Z} = \frac{500 \text{ V}}{10000 \, \Omega} = 0.05 \text{ A}$

Now, calculate the deflecting torque based on current:
$T_d = (0.05)^2 \times \frac{dM}{d\theta}$
$T_d = 0.0025 \times \frac{dM}{d\theta}$

At steady state, the deflecting torque equals the controlling torque ($T_c = K\theta$):
$T_c = T_d$
$K\theta = 0.0025 \times \frac{dM}{d\theta}$

We are given that $\frac{dM}{d\theta} = K$. Substitute $K$ for $\frac{dM}{d\theta}$:
$K\theta = 0.0025 \times K$

Divide both sides by $K$ (assuming $K \neq 0$):
$\theta = 0.0025 \text{ radians}$

To convert radians to degrees:
$\theta_{\text{degrees}} = 0.0025 \times \frac{180}{\pi} \approx 0.143^\circ$

The angle of deflection is **$0.0025 \text{ radians}$** (or roughly $0.143^\circ$).

Ans related location pg number in ak slide: 90, 91, 92.

***

### 40. Page 26, SEC- C CT-03: 1. Measurement of power using three ammeter. (8)

**Answer:**
The "Three Ammeter Method" is a technique used to measure the power consumed by a single-phase load when a standard wattmeter is unavailable. It relies purely on current and voltage readings and the phase relationships derived from Kirchhoff's Current Law.

**Circuit Configuration:**
1.  A known, purely non-inductive resistor ($R$) is connected in parallel with the unknown load ($Z_L$) whose power is to be measured.
2.  Three ammeters are used:
    *   **Ammeter 1 ($A_1$):** Connected in the main line to measure the total current ($I_1$) supplied by the AC source.
    *   **Ammeter 2 ($A_2$):** Connected in series with the known non-inductive resistor to measure the current through it ($I_2$).
    *   **Ammeter 3 ($A_3$):** Connected in series with the unknown load to measure the current flowing through it ($I_3$).
3.  A voltmeter ($V$) is typically connected across the parallel combination to verify the voltage, but mathematically, the power can be derived solely from the three current readings and the value of $R$.

**Phasor Diagram and Derivation:**
Let $V$ be the voltage across the parallel combination. Let's take $V$ as the reference phasor ($V \angle 0^\circ$).
*   The current $I_2$ through the purely resistive branch $R$ is in phase with voltage $V$.
*   The current $I_3$ through the inductive load lags the voltage $V$ by some angle $\phi$.
*   By KCL, the total current $I_1$ is the phasor sum of $I_2$ and $I_3$: $\vec{I_1} = \vec{I_2} + \vec{I_3}$

Using the law of cosines on the phasor triangle formed by $I_1$, $I_2$, and $I_3$:
$I_1^2 = I_2^2 + I_3^2 + 2 I_2 I_3 \cos(\phi)$

The total active power ($P$) consumed by the unknown load is:
$P = V I_3 \cos(\phi)$

From Ohm's law applied to the purely resistive branch, we know the voltage is $V = I_2 R$. Substitute this into the power equation:
$P = (I_2 R) I_3 \cos(\phi) = R (I_2 I_3 \cos\phi)$

Now, rearrange the phasor triangle equation to solve for $(I_2 I_3 \cos\phi)$:
$2 I_2 I_3 \cos(\phi) = I_1^2 - I_2^2 - I_3^2$
$I_2 I_3 \cos(\phi) = \frac{I_1^2 - I_2^2 - I_3^2}{2}$

Finally, substitute this term back into the power equation:
$P = R \left[ \frac{I_1^2 - I_2^2 - I_3^2}{2} \right]$
**$P = \frac{R}{2} (I_1^2 - I_2^2 - I_3^2)$**

Thus, by reading the three ammeters ($I_1, I_2, I_3$) and knowing the value of $R$, the active power consumed by the load can be precisely calculated without a wattmeter.

Ans related location pg number in ak slide: Not explicitly derived in slides. (Standard AC measurements topic).


### 41. Page 29, Class test #2 Q12: Illustrate how an electrodynamometer type instrument works with both AC and DC.

**Answer:**
An electrodynamometer instrument operates on the principle that mechanical torque is produced by the interaction of magnetic fields generated by two sets of coils (fixed and moving) when current passes through them. 

The instantaneous deflecting torque ($T_i$) is directly proportional to the product of the instantaneous currents flowing in the fixed coil ($i_1$) and the moving coil ($i_2$):
$T_i \propto i_1 \cdot i_2$

**Working with DC:**
When Direct Current (DC) is applied, the currents $i_1$ and $i_2$ are steady and do not change direction.
Let $i_1 = I_1$ and $i_2 = I_2$.
The resulting torque is steady and proportional to their product: $T_d \propto I_1 \cdot I_2$. 
The fixed coils create a constant magnetic field, and the moving coil creates a constant magnetic field. The moving coil rotates to align itself with the fixed magnetic field, providing a steady upscale deflection.

**Working with AC:**
When Alternating Current (AC) is applied, both currents $i_1$ and $i_2$ oscillate, changing their magnitude and reversing their direction simultaneously (usually 50 or 60 times a second).
Let $i_1 = I_{m1} \sin(\omega t)$ and $i_2 = I_{m2} \sin(\omega t)$. (Assuming they are in phase for simplicity, like in an ammeter or voltmeter configuration).
The instantaneous torque becomes:
$T_i \propto [I_{m1} \sin(\omega t)] \cdot [I_{m2} \sin(\omega t)]$
$T_i \propto I_{m1} \cdot I_{m2} \cdot \sin^2(\omega t)$

The crucial point here is the term **$\sin^2(\omega t)$**. Because the square of any real number (positive or negative) is always positive, the instantaneous deflecting torque $T_i$ is **always positive**, meaning it constantly acts in the same forward direction regardless of whether the AC cycle is in its positive or negative half.

During the positive half-cycle, both magnetic fields have a certain polarity, producing a forward torque. During the negative half-cycle, the currents in *both* coils reverse simultaneously. Because *both* interacting magnetic fields reverse at the exact same time, the direction of the resulting force (torque) remains unchanged (similar to how reversing both magnets in an interaction maintains the same attraction/repulsion dynamic).

Due to the mechanical inertia of the moving system, the pointer cannot vibrate at twice the supply frequency. Instead, it assumes a steady deflection proportional to the **average** value of this constantly forward-acting torque, which correctly corresponds to the RMS values of the measured AC quantities. Therefore, the electrodynamometer works perfectly for both AC and DC.

Ans related location pg number in ak slide: 89, 90.

***

### 42. Page 34, CT#03 SEC: A Q2(ii): Why is the current coil in a wattmeter split into two parts?

**Answer:**
In an electrodynamometer type wattmeter, the current coil (fixed coil) is almost always split into two identical, separated halves. There are two primary reasons for this specific design:

1.  **Creation of a Uniform Magnetic Field:** The moving pressure coil must rotate within the magnetic field generated by the fixed current coils. If the current coil were a single solid block, the magnetic field would be strongest at its center and rapidly weaken towards the edges, meaning the torque would vary non-linearly depending on the moving coil's exact position. By splitting the fixed coil into two parts and leaving a precise gap between them (often approximating a Helmholtz coil configuration), the magnetic fields from the two halves overlap and sum together to create a highly **uniform and homogenous radial magnetic field** in the central central space. This ensures that the deflecting torque remains strictly proportional to the currents regardless of the pointer's angle of deflection.
2.  **Physical Space for the Moving System:** The moving coil must be mounted on a vertical spindle so it can rotate freely. This spindle must be supported by jewel bearings at the top and bottom. Splitting the fixed current coil into two distinct halves provides the necessary physical gap in the center of the instrument. This allows the spindle to pass directly through the central axis of the magnetic field, providing the necessary mechanical clearance for the moving coil assembly, pointer, and damping vanes to operate without physical interference.

Ans related location pg number in ak slide: 89, 91.

***

### 43. Page 2, Q.4. (a): Describe the working principle of an induction type energy meter.

**Answer:**
An induction type energy meter (commonly known as a watt-hour meter) is an integrating instrument that measures total electrical energy consumed over time. It operates entirely on the principle of electromagnetic induction, specifically the interaction between alternating magnetic fluxes and the eddy currents they induce in a conductive, non-magnetic rotating disc.

**Working Principle:**
1.  **Magnetic Fields Generation:** The meter has two electromagnets. 
    *   The **Series Magnet (Current Coil):** Wound with thick wire and connected in series with the load. It produces an alternating magnetic flux ($\Phi_{se}$) proportional to and strictly in phase with the load current ($I$).
    *   The **Shunt Magnet (Voltage Coil):** Wound with fine wire and connected in parallel across the supply voltage. Due to high inductance (enhanced by copper shading bands), it produces an alternating magnetic flux ($\Phi_{sh}$) that lags the supply voltage ($V$) by exactly 90 degrees.
2.  **Induction of Eddy Currents:** Both of these alternating magnetic fluxes pass through a lightweight aluminum disc located in the air gap between the magnets. According to Faraday’s Law, these changing fluxes induce electromotive forces (EMFs) within the disc. These EMFs cause circulating "eddy currents" to flow within the aluminum disc.
    *   Flux $\Phi_{se}$ induces eddy current $I_{se}$.
    *   Flux $\Phi_{sh}$ induces eddy current $I_{sh}$.
3.  **Production of Driving Torque:** The driving mechanism relies on the interaction between the fluxes and the eddy currents. Specifically, the flux from the series magnet ($\Phi_{se}$) interacts with the eddy current induced by the shunt magnet ($I_{sh}$), and the flux from the shunt magnet ($\Phi_{sh}$) interacts with the eddy current induced by the series magnet ($I_{se}$). 
    Because of the carefully engineered 90-degree phase shift between the two fluxes, these two interactions produce mechanical forces that do not cancel out but sum together to create a continuous, unidirectional driving torque ($T_d$). Mathematically, this torque is proportional to $V \cdot I \cdot \cos(\phi)$, which is the true active power ($P$) consumed by the load.
4.  **Braking and Integration:** A permanent braking magnet is positioned at the edge of the disc. As the disc rotates, it cuts the permanent magnetic field, generating separate eddy currents that produce a braking torque ($T_b$) directly proportional to the disc's rotational speed ($N$). 
    When the driving torque equals the braking torque ($T_d = T_b$), the disc spins at a constant steady speed. Since $T_d \propto \text{Power}$ and $T_b \propto \text{Speed}$, then $\text{Speed} \propto \text{Power}$. The total number of revolutions over time is thus the integral of power over time, which equals the total Energy consumed.

Ans related location pg number in ak slide: 95, 96, 97.

***

### 44. Page 12, Q.8. (c): What is creeping? What are the effects of voltage variations on the energy meter reading?

**Answer:**
**What is Creeping?**
"Creeping" in an induction-type energy meter is a highly undesirable phenomenon where the aluminum disc continues to rotate very slowly even when there is absolutely **no load connected** (i.e., no current flows through the series/current coil), as long as the shunt/voltage coil remains energized by the main supply. If left uncorrected, a creeping meter will continuously register false energy consumption, resulting in the consumer being billed for electricity they did not use. The primary cause of creeping is the slight over-compensation of the friction compensating device (usually shading loops on the central limb of the shunt magnet), which produces a tiny driving torque. This is exacerbated by vibrations, stray magnetic fields, or supply overvoltages. It is prevented by drilling two diametrically opposite holes in the aluminum disc to disrupt eddy currents when they pass under the electromagnet poles.

**Effects of Voltage Variations on Energy Meter Reading:**
Supply voltage variations affect the accuracy of an induction energy meter in conflicting ways:
1.  **Effect on Driving Torque (Over-registration tendency):** An increase in supply voltage ($V$) causes a proportional increase in the shunt magnet flux ($\Phi_{sh}$). Since the driving torque is proportional to the product of voltage and current ($V \cdot I \cdot \cos\phi$), a higher voltage theoretically causes a proportionately higher driving torque. Furthermore, if the magnetic core of the shunt magnet approaches saturation due to high voltage, the flux waveform may become distorted, changing the precise 90-degree phase relationship and leading to further errors.
2.  **Effect on Braking Torque (Under-registration tendency):** The braking torque is supposed to be provided entirely by the permanent braking magnet. However, the shunt magnet flux ($\Phi_{sh}$) also acts as a secondary, albeit weaker, braking magnet. As it cuts the rotating disc, it generates additional braking eddy currents. Since braking torque is proportional to the square of the flux ($\Phi^2$), an increase in voltage causes an exponential increase in this secondary braking effect.

**Net Effect:** Because the secondary braking effect (proportional to $V^2$) increases faster than the driving effect (proportional to $V$), a significant increase in supply voltage generally causes the meter to run slightly slower than it should, leading to **under-registration** (a negative error). Conversely, a drop in voltage usually leads to slight over-registration.

Ans related location pg number in ak slide: 95, 96, 97.

### 45. Page 25, CT-03(B) Q1: (a) Draw a simplified diagram of an induction type energy meter and show the flux and eddy current distributions within the rotating disk. (b) Draw the phasor diagram of the energy meter and establish the relationship between total no. of revolution and the energy consumed. [figure Involved - note reference to simplified diagram/phasor]

**Answer:**

**(a) Simplified Diagram & Flux/Eddy Current Distribution:**

*(Note: While I cannot literally "draw" an image, I will describe the required figures in detail as requested by the prompt structure.)*

**Simplified Diagram Description:**
The diagram should depict the two main electromagnets and the disc:
*   **Top Magnet (Shunt Magnet):** An E-shaped laminated iron core. The fine-wire voltage coil is wound on the central limb. It is connected across the supply voltage (V). Copper shading bands are shown on the lower portion of the central limb.
*   **Bottom Magnet (Series Magnet):** A U-shaped laminated iron core. The thick-wire current coil is wound on both limbs, connected in series with the load.
*   **Disc:** A thin aluminum disc is positioned horizontally in the air gap between the top E-magnet and the bottom U-magnet, mounted on a vertical spindle.
*   **Braking Magnet:** A permanent C-shaped magnet positioned at the outer edge of the disc opposite the electromagnets.

**Flux and Eddy Current Distribution Description [Figure Involved]:**
A top-down view of the aluminum disc is required.
1.  **Flux Penetration:** Show three distinct circular regions where the magnetic fluxes perpendicularly pierce the disc.
    *   One central region representing the alternating flux $\Phi_p$ (or $\Phi_{sh}$) from the central limb of the upper shunt magnet.
    *   Two regions flanking the center, representing the alternating flux $\Phi_s$ (or $\Phi_{se}$) returning through the two limbs of the lower series magnet.
2.  **Eddy Currents:**
    *   Surrounding the central $\Phi_p$ flux penetration area, draw circulating current lines representing the induced eddy current $I_{ep}$.
    *   Surrounding the two flanking $\Phi_s$ flux areas, draw circulating current lines representing the induced eddy currents $I_{es}$.
3.  **Interaction:** The key is to show that the eddy current $I_{ep}$ (induced by the voltage magnet) physically intersects and flows through the magnetic field $\Phi_s$ (from the current magnet), and vice-versa. This intersection is what generates the driving Lorentz force.

**(b) Phasor Diagram and Relationship Establishment:**

**Phasor Diagram Description [Figure Involved]:**
1.  Draw the reference phasor horizontally representing the supply voltage $V$.
2.  Draw the load current phasor $I$ lagging $V$ by an angle $\phi$ (representing an inductive load).
3.  The series magnet flux $\Phi_s$ (or $\Phi_{se}$) is directly proportional to and exactly in phase with the load current $I$. Draw $\Phi_s$ superimposed on the $I$ phasor.
4.  The voltage applied to the highly inductive shunt coil generates a current $I_p$ that lags $V$ by almost $90^\circ$. Draw $I_p$ pointing downwards.
5.  The shunt magnet flux $\Phi_p$ (or $\Phi_{sh}$) is produced by $I_p$. Due to core losses, it wouldn't naturally lag by exactly $90^\circ$. However, the copper shading bands force it to lag $V$ by exactly $90^\circ$ ($\Delta = 90^\circ$). Draw $\Phi_p$ lagging $V$ by exactly $90^\circ$, pointing straight down.
6.  The induced eddy EMFs ($E_{es}$ and $E_{ep}$) lag their respective inducing fluxes ($\Phi_s$ and $\Phi_p$) by $90^\circ$.
7.  The resulting eddy currents ($I_{es}$ and $I_{ep}$) lag their respective EMFs by a small angle $\alpha$ due to the self-inductance of the aluminum disc.

**Establishing the Relationship:**
The instantaneous driving torque $T_i$ is proportional to the interaction of fluxes and opposing eddy currents:
$T_i \propto (\Phi_p \cdot i_{es}) - (\Phi_s \cdot i_{ep})$

Using the phasor relationships derived above, the average driving torque $T_d$ over a cycle is:
$T_d \propto \Phi_p \cdot I \cos(\alpha) \sin(\Delta - \phi)$
Since $\Phi_p \propto V$ and we designed the shading bands so that $\Delta = 90^\circ$:
$T_d \propto V \cdot I \cos(\alpha) \sin(90^\circ - \phi)$
$T_d \propto V \cdot I \cos(\phi) \cos(\alpha)$
Since $\alpha$ is constant for a given disc, $\cos(\alpha)$ is a constant ($K_1$).
$T_d = K_1 \cdot V \cdot I \cos(\phi) = K_1 \cdot \text{True Power } (P)$

The permanent braking magnet creates a braking torque $T_b$ proportional to the disc's rotational speed $N$:
$T_b = K_2 \cdot N$

At steady running speed, the driving torque equals the braking torque:
$T_d = T_b$
$K_1 \cdot P = K_2 \cdot N$
$N = \left( \frac{K_1}{K_2} \right) \cdot P$
Therefore, the speed $N$ is directly proportional to the Power $P$.

To find the total number of revolutions ($\text{Total Revs}$), we integrate speed over time ($t$):
$\text{Total Revs} = \int N \, dt = \int \left( \frac{K_1}{K_2} \right) P \, dt$
$\text{Total Revs} = \left( \frac{K_1}{K_2} \right) \int P \, dt$
Since the integral of power over time is total Energy consumed:
$\text{Total Revs} = K \cdot \text{Energy}$
This establishes that the total number of revolutions is strictly proportional to the total electrical energy consumed.

Ans related location pg number in ak slide: 95, 96, 97.

***

### 46. Page 2, Q.6. (b): Mention the conditions for synchronization of an AC generator to a power system.

**Answer:**
To safely and smoothly connect (synchronize) an incoming AC generator (alternator) to an active, running power system (busbars or infinite bus), several strict electrical conditions must be met simultaneously. If these conditions are not met, connecting the generator can result in catastrophic circulating currents, severe mechanical damage to the generator shaft, and disruption of the power grid.

The mandatory conditions for synchronization are:
1.  **Equal Voltage Magnitude (Terminal Voltage):** The terminal voltage of the incoming generator must be exactly equal to the voltage of the power system (busbars). This is usually verified using voltmeters and adjusted by changing the generator's field excitation current.
2.  **Equal Frequency:** The frequency of the incoming generator must be exactly equal to the frequency of the power system. This is verified using a frequency meter or a synchroscope and is adjusted by changing the mechanical speed of the generator's prime mover (e.g., the steam or hydro turbine).
3.  **Phase Sequence Match:** The phase sequence (the order in which the voltage peaks occur, e.g., A-B-C or R-Y-B) of the incoming generator must perfectly match the phase sequence of the power system. If they are reversed (e.g., A-B-C vs. A-C-B), closing the breaker will result in a massive short circuit on two phases.
4.  **Zero Phase Angle Difference:** The phase angle between the corresponding phases of the incoming generator and the power system must be exactly zero at the instant the connection switch (circuit breaker) is closed. This means the voltage waveforms of both systems must peak at the exact same millisecond. This is visually verified using a synchroscope.

Ans related location pg number in ak slide: Not explicitly listed in bullet points in the slides, but fundamentally relates to the use of a synchroscope mentioned on 101.

***

### 47. Page 2, Q.6. (c): Show how a synchroscope with an electro-dynamometer movement can decide if a synchronous generator to be connected to the power system is slower or faster.

**Answer:**
An electro-dynamometer (Weston-type) synchroscope consists of a three-limbed fixed magnetic circuit and a moving system comprising two coils (coil A and coil B) mounted on the same spindle at exactly $90^\circ$ to each other. 

**Circuit Connections:**
*   The fixed coil (wound on the central limb) is connected across one phase of the **busbars (running system)**, usually via an inductor, so its current and resulting magnetic flux lag the busbar voltage by $90^\circ$. Let the busbar frequency be $f_b$.
*   The moving coils are connected across the corresponding phase of the **incoming generator**. 
    *   Moving coil A is connected via a purely resistive circuit, so its current is in phase with the incoming generator voltage.
    *   Moving coil B is connected via a highly inductive circuit, so its current lags the incoming generator voltage by $90^\circ$.
    *   Let the incoming generator frequency be $f_g$.

**How it determines "Slower" or "Faster":**
The operating principle relies on the interaction between the alternating magnetic field of the fixed coil and the alternating magnetic fields of the two moving coils.
The instantaneous torque on the moving system depends on the phase difference between the busbar voltage and the incoming generator voltage.

1.  **When Frequencies are exactly Equal ($f_g = f_b$):** The phase difference between the two voltages is constant. The torques on coils A and B balance each other out, and the pointer assumes a stationary, steady position. If the voltages are exactly in phase (the perfect moment for synchronization), the pointer points straight up to the 12 o'clock mark.
2.  **When the Incoming Generator is Faster ($f_g > f_b$):** The incoming generator's voltage phasor is rotating slightly faster than the busbar's voltage phasor. Consequently, the phase angle between them is continuously changing, specifically advancing in the positive direction. This continuously changing phase angle causes the torque balance point between coil A and coil B to continuously shift in one direction. As a result, the pointer rotates continuously in the **"Fast" (usually clockwise)** direction. The speed of rotation indicates how much faster the generator is running.
3.  **When the Incoming Generator is Slower ($f_g < f_b$):** The incoming generator's voltage phasor is rotating slower than the busbar's phasor. The phase angle is continuously retarding (moving negatively). The shifting torque balance now moves in the opposite direction. Consequently, the pointer rotates continuously in the **"Slow" (usually counter-clockwise)** direction.

By observing the direction of the pointer's rotation, the operator immediately knows whether they need to increase or decrease the speed of the generator's turbine before closing the breaker.

Ans related location pg number in ak slide: Not fully derived in slides, relates to generic synchroscope principles implied in speed/frequency measurement section.

***

### 48. Page 4, Q.4 (a): Explain the structure and operation of a frequency meter.

**Answer:**
A frequency meter is an instrument designed to measure the frequency of an alternating current (AC) supply, typically displaying the result directly in Hertz (Hz). There are several types (e.g., mechanical resonance/reed type, electrical resonance type), but the most common analog type used in power applications is the **Electrical Resonance (Ferrodynamic) type**.

**Structure (Electrical Resonance Type):**
The instrument resembles an electro-dynamometer but has specific modifications.
1.  **Fixed Coil (Magnetizing Coil):** It consists of a fixed magnetizing coil wound on a laminated iron core to increase the magnetic flux. This fixed coil is connected directly across the AC supply whose frequency is to be measured.
2.  **Moving Coil:** A lightweight moving coil is pivoted to rotate within the magnetic field of the fixed coil. Attached to the spindle of this moving coil is the pointer.
3.  **Resonant Circuit:** The critical feature is that the moving coil is connected in series with a specific, carefully calibrated capacitor ($C$). This combination of the moving coil's inductance ($L$) and the external capacitor ($C$) forms a series resonant circuit.
4.  **No Mechanical Control:** Unlike voltmeters or ammeters, this instrument **does not have a control spring**. The restoring torque is purely electromagnetic. 

**Operation:**
The operation is based on the principle of electrical resonance. The series circuit (moving coil $L$ + capacitor $C$) is designed to resonate at a specific "normal" frequency (e.g., exactly 50 Hz). At resonance, the inductive reactance ($X_L = 2\pi f L$) exactly equals the capacitive reactance ($X_C = \frac{1}{2\pi f C}$).

1.  **At Normal Frequency:** When the supply frequency is exactly at the resonant frequency, the circuit is purely resistive. The current $I_m$ in the moving coil is perfectly in phase with the voltage induced in it by the fixed coil. The resulting deflecting torque ($T_d$) is zero. Since there is no control spring, the pointer rests exactly in the center of the scale, marking the normal frequency.
2.  **Above Normal Frequency (High Frequency):** If the supply frequency increases above the resonant frequency, the inductive reactance ($X_L$) becomes greater than the capacitive reactance ($X_C$). The moving coil circuit becomes predominantly inductive. The current $I_m$ now lags the induced voltage. This phase shift creates a specific deflecting torque that drives the pointer in one direction (usually to the right, marked "Higher"). The iron core is specially shaped so its cross-section varies over the length; as the pointer moves, the inductance changes until a new torque balance is found without a spring.
3.  **Below Normal Frequency (Low Frequency):** If the supply frequency drops below resonance, $X_C$ becomes greater than $X_L$. The circuit becomes predominantly capacitive, and $I_m$ leads the induced voltage. This opposite phase relationship creates a deflecting torque in the opposite direction, driving the pointer to the left, marked "Lower".

Ans related location pg number in ak slide: 102, 103.

### 49. Page 6, Q.8 b): Describe the construction and operation principle of Weston frequency meter.

**Answer:**
*(Note: A Weston frequency meter typically refers to the moving-iron crossed-coil type. The provided slides detail the Ferrodynamic / Electrical Resonance type frequency meter. I will describe the standard Weston crossed-coil type as requested by the specific historical instrument name, but note that slide 102 covers the Ferrodynamic resonance type which is often functionally synonymous in typical exam contexts if the "Weston" name is loosely applied to dynamometer types.)*

**Construction of a Weston (Crossed-Coil) Frequency Meter:**
1.  **Fixed Coils:** The instrument features two fixed coils (Coil A and Coil B) which are fixed at right angles ($90^\circ$) to each other. 
2.  **Moving Element:** The moving system consists of a soft iron needle or a small iron core pivoted precisely at the center of the crossed coils. A pointer is attached to this spindle. Notably, **there is no control spring**; the pointer's position is determined entirely by the magnetic fields.
3.  **Circuit Connections:** The meter is connected across the supply voltage.
    *   **Coil A** is connected in series with a highly inductive choke ($L_A$) and an external resistor ($R_A$).
    *   **Coil B** is connected in series with a non-inductive resistor ($R_B$) and an external inductor ($L_B$). 
    *   The entire circuit forms a parallel bridge network designed to resonate at the normal supply frequency (e.g., 50 Hz).

**Operation Principle:**
The operating principle is based on the interaction of the magnetic fields produced by the two crossed coils and their relative strength, which changes based on the supply frequency.

1.  **At Normal Frequency (e.g., 50 Hz):** The inductances and resistances are calibrated such that at exactly 50 Hz, the impedance of the Coil A branch equals the impedance of the Coil B branch. Consequently, equal currents flow through both coils ($I_A = I_B$). They produce equal magnetic fields at right angles. The resultant magnetic field sits exactly at $45^\circ$ between them. The soft iron needle aligns itself perfectly with this resultant field, placing the pointer in the exact center of the scale marked "50 Hz."
2.  **Above Normal Frequency ($>50$ Hz):** If the supply frequency increases, the inductive reactance ($X_L = 2\pi f L$) of the choke $L_A$ in Coil A's branch increases, reducing the current $I_A$. Conversely, in Coil B's branch, the relative effect changes differently depending on the exact tuning circuit used, but fundamentally, the current $I_B$ becomes significantly larger than $I_A$. The magnetic field of Coil B becomes stronger than Coil A's field. The resultant magnetic field vector shifts toward Coil B. The iron needle aligns with this new field, moving the pointer upscale toward higher frequency markings.
3.  **Below Normal Frequency ($<50$ Hz):** If the frequency decreases, the inductive reactance drops. Current $I_A$ increases while $I_B$ decreases comparatively. The magnetic field of Coil A becomes dominant. The resultant magnetic field vector shifts toward Coil A. The iron needle tracks this shift, moving the pointer downscale toward lower frequency markings.

Because the final position of the pointer depends entirely on the *ratio* of the currents in the two coils (which is frequency-dependent) and not on the absolute magnitude of the voltage, the reading is relatively independent of normal supply voltage fluctuations.

Ans related location pg number in ak slide: 102, 103 (Covers Electrical Resonance type, functionally related).

***

### 50. Page 9, Q.3. (c): Explain the construction and working principle of an electrical resonance (ferrodynamic type) frequency meter.

**Answer:**
**Construction:**
The electrical resonance (ferrodynamic) frequency meter consists of a stationary part and a moving part, but relies on a specially shaped magnetic core and a tuned circuit.
1.  **Magnetizing Coil & Core:** A fixed magnetizing coil is wound around a laminated iron core. This coil is connected across the AC supply whose frequency is to be measured. A crucial feature is the shape of the iron core: its cross-section is not uniform. It varies over its length, being maximum at one end (where the magnetizing coil is located) and minimum at the other end.
2.  **Moving Coil:** A lightweight moving coil is pivoted to move over the variable cross-section part of the iron core. The pointer is attached to this moving coil.
3.  **Tuning Capacitor:** The moving coil is connected in series with a fixed capacitor $C$. The inductance $L$ of the moving coil and this capacitor $C$ form a series resonant circuit.
4.  **No Mechanical Control:** Like most frequency meters, it has no control spring. The position is dictated by electromagnetic torques balancing out.

**Working Principle:**
The principle is based on the moving coil striving to find a position where the deflecting torque is zero. The deflecting torque $T_d$ depends on the phase angle between the magnetic flux $\Phi$ (produced by the fixed coil) and the current $I_m$ flowing in the moving coil. 

1.  **Magnetizing Flux:** The fixed coil carries current $I$ which produces a flux $\Phi$ that is in phase with $I$. This flux induces an EMF ($E$) in the moving coil. Since induced EMF lags flux by $90^\circ$, $E$ lags $\Phi$ by $90^\circ$.
2.  **Current in Moving Coil ($I_m$):** The phase of $I_m$ relative to $E$ depends entirely on the impedance of the moving coil circuit (which contains $L$ and $C$).
    *   If the circuit is inductive, $I_m$ lags $E$.
    *   If the circuit is capacitive, $I_m$ leads $E$.
    *   If the circuit is at resonance ($X_L = X_C$), it is purely resistive, and $I_m$ is in phase with $E$.
3.  **Deflecting Torque Equation:** The torque $T_d$ is proportional to $I_m \cos(90^\circ + \alpha)$, where $\alpha$ is the phase angle of the moving coil circuit.
    *   $T_d = I_m \cos(90^\circ + \alpha)$ if the coil is inductive.
    *   $T_d = I_m \cos(90^\circ - \beta)$ if the coil is capacitive.
    *   $T_d = 0$ if the coil is purely resistive (at resonance).
4.  **How it finds balance:** The circuit is designed to be resonant at the normal frequency (e.g., 50 Hz) when the coil is exactly in the center position. 
    *   If the supply frequency changes, say it increases, the moving coil circuit goes out of resonance and becomes inductive. A torque is produced. 
    *   This torque forces the coil to move. As it moves along the specially shaped, tapering iron core, the inductance $L$ of the moving coil physically changes. 
    *   The coil will continue to move until its changing inductance $L$ re-tunes the circuit back to resonance ($X_L = X_C$) at the new frequency. Once resonant again, the torque drops to zero, and the pointer stops. 
    *   Therefore, every physical position on the dial corresponds to a specific frequency that makes the coil resonant.

Ans related location pg number in ak slide: 102, 103.

***

### 51. Page 9, Q.6. (a): Describe a single phase electrodynamometer type of power factor meter and show that the displacement of moving system is equal to the phase angle of the system.

**Answer:**
**Description:**
A single-phase electrodynamometer power factor meter operates similarly to a wattmeter but features two moving coils instead of one, and lacks a control spring.
1.  **Fixed Coils (Current Coils):** The instrument has a split fixed coil, connected in series with the load. It carries the load current ($I$) and produces a magnetic field proportional to $I$.
2.  **Moving System:** Two identical, lightweight moving coils (Coil A and Coil B) are mounted on the same central spindle. Crucially, they are fixed rigidly at an exact angle of $90^\circ$ relative to each other. The pointer is attached to this spindle. There are no control springs.
3.  **Connections:** Both moving coils are connected in parallel across the supply voltage ($V$).
    *   **Coil A** is connected in series with a high-value non-inductive resistor ($R$). The current $I_A$ in this coil is in phase with the supply voltage $V$.
    *   **Coil B** is connected in series with a highly inductive choke ($L$). The current $I_B$ in this coil lags the supply voltage $V$ by nearly $90^\circ$ (ideally exactly $90^\circ$).

**Showing displacement equals phase angle:**
Let the load current $I$ lag the supply voltage $V$ by the power factor angle $\phi$.
The fixed coil creates a magnetic field proportional to $I$.
*   **Torque on Coil A ($T_A$):** Coil A carries current $I_A$ (in phase with $V$). The torque is proportional to the product of $I$, $I_A$, the cosine of the phase angle between them (which is $\phi$), and the physical angle of the coil. If the coil is at an angle $\theta$ from the vertical plane of reference:
    $T_A = K \cdot V \cdot I \cdot \cos(\phi) \cdot \sin(\theta)$
*   **Torque on Coil B ($T_B$):** Coil B carries current $I_B$ (lagging $V$ by $90^\circ$). The phase angle between $I$ and $I_B$ is $(90^\circ - \phi)$. Coil B is mounted $90^\circ$ away from Coil A, so its physical angle is $(90^\circ + \theta)$.
    $T_B = K \cdot V \cdot I \cdot \cos(90^\circ - \phi) \cdot \sin(90^\circ + \theta)$
    $T_B = K \cdot V \cdot I \cdot \sin(\phi) \cdot \cos(\theta)$

Since there are no control springs, the moving system will rotate until the two opposing torques completely balance each other:
$T_A = T_B$
$K \cdot V \cdot I \cdot \cos(\phi) \cdot \sin(\theta) = K \cdot V \cdot I \cdot \sin(\phi) \cdot \cos(\theta)$

Canceling common terms ($K, V, I$):
$\cos(\phi) \cdot \sin(\theta) = \sin(\phi) \cdot \cos(\theta)$

Divide both sides by $\cos(\phi) \cdot \cos(\theta)$:
$\frac{\sin(\theta)}{\cos(\theta)} = \frac{\sin(\phi)}{\cos(\phi)}$
$\tan(\theta) = \tan(\phi)$
**$\theta = \phi$**

This mathematical proof shows that the physical angle of deflection ($\theta$) of the pointer is exactly equal to the electrical phase angle ($\phi$) of the load circuit. The scale is typically calibrated in terms of $\cos(\phi)$ to read the Power Factor directly.

Ans related location pg number in ak slide: 101.

***

### 52. Page 11, Q.2. (a): For an electrodynamometer type power factor meter prove that, the deflection of the instrument is a measure of phase angle of the circuit.

**Answer:**
*This question requires the exact same derivation as the previous question (Q51). I will provide the proof directly.*

**Proof:**
An electrodynamometer power factor meter uses a fixed current coil carrying load current $I$, and two moving pressure coils (A and B) fixed at $90^\circ$ to each other. Coil A is resistive (current $I_A$ in phase with voltage $V$), and Coil B is inductive (current $I_B$ lags $V$ by $90^\circ$). The pointer rests where the torques on Coil A and Coil B balance, as there is no mechanical control spring.

Let:
*   $\phi$ = electrical phase angle of the load (angle by which $I$ lags $V$).
*   $\theta$ = mechanical angle of deflection of the moving system from the reference plane.

1.  **Deflecting Torque on Coil A ($T_A$):** 
    Current $I_A$ is proportional to $V$ and is in phase with $V$. 
    The phase difference between fixed coil current $I$ and moving coil current $I_A$ is $\phi$.
    The mechanical torque equation for a dynamometer involves the sine of the mechanical deflection angle.
    $T_A \propto V \cdot I \cdot \cos(\phi) \cdot \sin(\theta)$
2.  **Deflecting Torque on Coil B ($T_B$):**
    Current $I_B$ is proportional to $V$ but lags $V$ by $90^\circ$.
    The phase difference between fixed coil current $I$ and moving coil current $I_B$ is $(90^\circ - \phi)$.
    Because Coil B is mechanically mounted $90^\circ$ away from Coil A, its mechanical angle is $(90^\circ + \theta)$.
    $T_B \propto V \cdot I \cdot \cos(90^\circ - \phi) \cdot \sin(90^\circ + \theta)$
    Using trigonometric identities ($\cos(90-x) = \sin x$ and $\sin(90+x) = \cos x$):
    $T_B \propto V \cdot I \cdot \sin(\phi) \cdot \cos(\theta)$
3.  **Equilibrium Condition:**
    The moving system comes to rest when the two torques are exactly equal and opposite:
    $T_A = T_B$
    $V \cdot I \cdot \cos(\phi) \cdot \sin(\theta) = V \cdot I \cdot \sin(\phi) \cdot \cos(\theta)$
4.  **Solving for $\theta$:**
    Cancel $V \cdot I$ from both sides:
    $\cos(\phi) \cdot \sin(\theta) = \sin(\phi) \cdot \cos(\theta)$
    Divide by $\cos(\phi) \cos(\theta)$:
    $\frac{\sin(\theta)}{\cos(\theta)} = \frac{\sin(\phi)}{\cos(\phi)}$
    $\tan(\theta) = \tan(\phi)$
    **$\theta = \phi$**

This confirms that the mechanical deflection angle ($\theta$) is a direct measure of the electrical phase angle ($\phi$) of the circuit. The scale is calibrated to read Power Factor ($\cos\phi$) rather than degrees.

Ans related location pg number in ak slide: 101.

### 53. Page 12, Q.5. (c): What is frequency meter? Explain the operating principle of an electrodynamometer type frequency meter.

**Answer:**
**What is a frequency meter?**
A frequency meter is an electrical indicating instrument used to measure and display the frequency of an alternating current (AC) power supply, usually in Hertz (Hz). They are critical in power generation and distribution, as system frequency must be maintained within very tight tolerances (e.g., $50 \text{ Hz} \pm 0.05 \text{ Hz}$).

**Operating principle of an electrodynamometer type frequency meter:**
*(Note: As clarified in previous answers, the standard dynamometer-based frequency meter is the Electrical Resonance or Ferrodynamic type, which utilizes a tuned circuit and an un-sprung moving coil to find a torque balance point.)*

1.  **Components:** The meter consists of a fixed magnetizing coil wound on a laminated iron core of varying cross-section, and a moving coil pivoted over this core. The moving coil is connected in series with a capacitor $C$, forming a resonant circuit. Crucially, there are no control springs to provide a mechanical restoring torque.
2.  **Creation of Torques:** The fixed coil is connected across the supply and carries current $I$, generating flux $\Phi$. This flux induces an EMF ($E$) in the moving coil that lags $\Phi$ by $90^\circ$. The resulting current in the moving coil ($I_m$) depends on the impedance of its series $L-C$ circuit.
    *   If the supply frequency is at the circuit's resonant frequency ($X_L = X_C$), the circuit is resistive. $I_m$ is in phase with $E$, and the resulting average deflecting torque is zero.
    *   If frequency rises, the circuit becomes inductive ($X_L > X_C$), $I_m$ lags $E$, producing a torque in one direction.
    *   If frequency falls, the circuit becomes capacitive ($X_C > X_L$), $I_m$ leads $E$, producing a torque in the opposite direction.
3.  **Achieving Balance:** Because there is no spring, the torque caused by an off-resonance frequency forces the moving coil to rotate. As the coil moves along the specially shaped (tapered) iron core, its physical position changes its inductance $L$. 
4.  **The Principle:** The coil continues to move until its changing inductance $L$ automatically re-tunes the $L-C$ circuit back to resonance at the new supply frequency. Once resonance is re-established, the torque drops back to zero, and the pointer stops. Therefore, the pointer's physical resting position directly indicates the frequency required to make that specific physical location resonant.

Ans related location pg number in ak slide: 102, 103.

***

### 54. Page 20, Q.7(a): Illustrate the operation of a Weston type synchroscope.

**Answer:**
A Weston type synchroscope is an electro-dynamometer instrument designed to indicate whether an incoming AC generator is running faster, slower, or at the exact same frequency as the main power grid (busbars), and to indicate the exact moment of phase alignment for safe synchronization.

**Illustration of Operation:**
1.  **Internal Structure:** It resembles a dynamometer power factor meter. It features a stationary field coil (connected to the busbars) and a moving system comprised of two crossed coils, Coil A and Coil B, fixed at exactly $90^\circ$ to each other on a central spindle (connected to the incoming generator). It has no control springs.
2.  **Phase Shifting Network:** 
    *   The fixed coil current is made to lag the busbar voltage by $90^\circ$ (via an inductor).
    *   Moving Coil A is in a resistive circuit, so its current is in phase with the incoming generator voltage.
    *   Moving Coil B is in an inductive circuit, so its current lags the incoming generator voltage by $90^\circ$.
3.  **Torque Generation:** The interaction between the magnetic field of the fixed coil and the fields of the two moving coils generates deflecting torques on the moving system. The pointer's behavior depends entirely on the frequency difference between the busbar ($f_b$) and the generator ($f_g$).
4.  **"Fast" or "Slow" Indication:** 
    *   If the frequencies are unequal ($f_g \neq f_b$), the phase angle between the two voltages is continuously changing. This causes the resultant magnetic field of the moving coils to physically rotate. The iron armature/pointer attempts to align with this rotating field, causing the pointer to spin continuously around the dial. 
    *   If $f_g > f_b$, the phase angle advances, and the pointer rotates in the "Fast" direction (usually clockwise).
    *   If $f_g < f_b$, the phase angle retards, and the pointer rotates in the "Slow" direction (usually counter-clockwise). The speed of rotation indicates the magnitude of the frequency difference.
5.  **Synchronization Point:** When the operator adjusts the generator speed so that $f_g$ exactly equals $f_b$, the phase angle becomes constant. The pointer stops spinning and points to a fixed position. The operator then makes microscopic speed adjustments until the pointer stands perfectly still at the 12 o'clock (0 degrees) mark. At this exact moment, the frequencies are equal, and the voltages are perfectly in phase, allowing the circuit breaker to be closed safely.

Ans related location pg number in ak slide: Relies on dynamometer and phase measurement principles (Slide 101), though the specific Weston synchroscope structure is classic generic knowledge.

***

### 55. Page 25, CT-03(B) Q2: Draw the schematic diagram of a ferrodynamic type frequency meter and show the phasor diagrams for nominal, over, and under frequency.

**Answer:**

**Schematic Diagram Description:**
1.  Draw an AC power source terminals marked 'Supply'.
2.  Draw a fixed magnetizing coil. This coil is wound around a uniquely shaped iron core (often drawn as a tapered or step-shaped block). Connect this fixed coil across the Supply terminals.
3.  Draw a moving coil positioned such that it can pivot and slide over/around the shaped iron core. Attach a pointer to the axis of this moving coil.
4.  Connect a capacitor ($C$) in series with the moving coil.
5.  Connect this series combination (moving coil + capacitor) across the same Supply terminals, in parallel with the fixed coil.
6.  *Crucial detail:* Do not draw any control springs on the moving coil axis.

**Phasor Diagrams Description:**
Let $\Phi$ be the main flux produced by the fixed coil. The induced EMF ($E$) in the moving coil lags $\Phi$ by $90^\circ$. Let $I_m$ be the current in the moving coil. The torque $T_d \propto I_m \cos(90^\circ \pm \text{phase angle})$.

1.  **Nominal Frequency (Resonance):**
    *   At the normal frequency, the moving coil's $L$-$C$ circuit is at resonance ($X_L = X_C$). It acts purely resistively.
    *   **Phasor:** Draw $\Phi$ horizontally to the right. Draw $E$ pointing straight down (lagging $\Phi$ by $90^\circ$). Because the circuit is resistive, draw $I_m$ perfectly superimposed on $E$ (in phase).
    *   **Result:** The angle between $\Phi$ and $I_m$ is exactly $90^\circ$. $\cos(90^\circ) = 0$. Torque is zero. Pointer remains at center.

2.  **Over Frequency ($f > f_{nominal}$):**
    *   When frequency increases, $X_L$ increases and $X_C$ decreases. The $L$-$C$ circuit becomes inductive.
    *   **Phasor:** Draw $\Phi$ horizontally right. Draw $E$ pointing straight down. Because the circuit is inductive, the current $I_m$ lags the voltage $E$ by an angle $\alpha$. Draw $I_m$ pointing down and slightly to the left.
    *   **Result:** The angle between $\Phi$ and $I_m$ is $(90^\circ + \alpha)$. $\cos(90^\circ + \alpha)$ is negative. This produces a torque in one direction, moving the coil to a position with lower inductance to re-establish resonance.

3.  **Under Frequency ($f < f_{nominal}$):**
    *   When frequency decreases, $X_L$ decreases and $X_C$ increases. The $L$-$C$ circuit becomes capacitive.
    *   **Phasor:** Draw $\Phi$ horizontally right. Draw $E$ pointing straight down. Because the circuit is capacitive, the current $I_m$ leads the voltage $E$ by an angle $\beta$. Draw $I_m$ pointing down and slightly to the right.
    *   **Result:** The angle between $\Phi$ and $I_m$ is $(90^\circ - \beta)$. $\cos(90^\circ - \beta)$ is positive. This produces a torque in the opposite direction, moving the coil to a position with higher inductance to re-establish resonance.

Ans related location pg number in ak slide: 102, 103 (Shows the exact schematic and three phasor diagrams).

***

### 56. Page 26, SEC- C CT-03: 2. Working principle of Electrical resonance type frequency meter. (12)

**Answer:**
*This question is essentially identical to Q50 and Q53. I will provide a streamlined explanation focusing on the core principle.*

**Working Principle:**
The electrical resonance (ferrodynamic) frequency meter relies entirely on the principle of series $L$-$C$ resonance to find a mechanical balance point without using any control springs.

1.  **The Setup:** The instrument has a fixed coil connected across the supply, producing an alternating magnetic flux. A moving coil (with inductance $L$) is placed in this flux and connected in series with a fixed capacitor ($C$). The moving coil can physically slide along a specially tapered iron core, which means its inductance $L$ changes depending on its physical position.
2.  **Torque Generation:** The fixed coil's flux induces an EMF in the moving coil. The resulting current in the moving coil interacts with the main flux to produce a deflecting torque. 
    *   If the $L$-$C$ circuit is purely resistive, the induced current is exactly $90^\circ$ out of phase with the main flux, resulting in zero average torque.
    *   If the $L$-$C$ circuit is reactive (either inductive or capacitive), a phase shift occurs, and a non-zero average torque is produced.
3.  **The Resonance Seeking Action:** 
    *   The meter is designed so that at the standard frequency (e.g., 50 Hz), the moving coil is in the center of the core, and its inductance exactly balances the capacitor ($X_L = X_C$). It is in resonance, torque is zero, and the pointer stays at "50".
    *   If the supply frequency changes (e.g., goes up to 51 Hz), the fixed capacitor and the current coil inductance are no longer matched. The circuit becomes inductive ($X_L > X_C$). This phase shift instantly creates a magnetic torque on the moving coil.
    *   This torque pushes the moving coil along the tapered iron core towards the end with a smaller cross-section. As it moves there, its physical inductance $L$ decreases.
    *   It continues moving until $L$ has decreased just enough that the new, lower $X_L$ once again exactly matches the new, higher $X_C$ at 51 Hz. 
    *   Once $X_L = X_C$ again, the circuit is back in resonance, the torque returns to zero, and the pointer stops precisely at the "51" mark on the dial.

Ans related location pg number in ak slide: 102, 103.

### 57. Page 34, CT#03 SEC: A Q1: Explain the working of a frequency meter that operates based on the phenomenon of electrical resonance.

**Answer:**
*This question is fundamentally identical to Q50, Q53, and Q56. Here is a concise explanation focusing purely on the resonance phenomenon.*

A frequency meter operating on the phenomenon of electrical resonance (the Ferrodynamic type) determines frequency by automatically adjusting its own internal circuitry until it hits a resonant state. 

**Working Mechanism:**
1.  **The Resonant Circuit:** The core of the instrument is a moving coil connected in series with a fixed capacitor ($C$). The moving coil possesses inductance ($L$). Crucially, this moving coil surrounds a stationary, specifically tapered (wedge-shaped) iron core. Because the core is tapered, the inductance $L$ of the moving coil changes depending on its physical position along the core.
2.  **Interaction:** A fixed magnetizing coil, connected to the AC supply, creates an alternating magnetic field. This field induces an EMF in the moving coil. The phase of the current flowing in the moving coil relative to the main magnetic field determines whether a mechanical torque is generated.
3.  **The Role of Resonance:** 
    *   **At Resonance:** If the supply frequency $f$ is such that the inductive reactance exactly equals the capacitive reactance ($2\pi f L = \frac{1}{2\pi f C}$), the circuit is at resonance. At this exact point, the current in the moving coil aligns such that the net deflecting torque acting on it is absolutely **zero**.
    *   **Off Resonance:** If the frequency changes, the delicate balance of $X_L = X_C$ is broken. The circuit becomes either net-inductive or net-capacitive. This phase shift creates a physical, deflecting torque on the moving coil.
4.  **Auto-Tuning:** Because there are no control springs holding the pointer in place, this new torque forces the moving coil to physically slide along the tapered iron core. 
    *   If frequency rose ($X_L > X_C$), the torque pushes the coil toward the narrower part of the core, *decreasing* its inductance $L$.
    *   If frequency fell ($X_C > X_L$), the torque pulls the coil toward the thicker part of the core, *increasing* its inductance $L$.
5.  **Finding the Reading:** The coil keeps moving, constantly changing its own $L$, until the condition $2\pi f L = \frac{1}{2\pi f C}$ is mathematically satisfied again for the *new* frequency $f$. Once it hits this new resonant point, torque becomes zero, and the pointer stops. The scale behind the pointer is simply calibrated to read the frequency that corresponds to that specific physical resonant position.

Ans related location pg number in ak slide: 102, 103.

***

### 58. Page 2, Q.3. (c): Describe briefly the operating principle of flux meter and hence prove that $\phi = (G/N)\theta$, where the symbols have their usual meanings.

**Answer:**
**Operating Principle:**
A flux meter is a specialized, highly damped form of a ballistic galvanometer used to measure constant magnetic flux. It consists of a moving coil suspended freely between the poles of a permanent magnet by a silk thread, utilizing a very weak or virtually zero control spring (meaning controlling torque $T_c \approx 0$). It is heavily damped electromagnetically because it is connected in a closed, low-resistance circuit with a search coil. 
When the search coil is rapidly introduced into or removed from a magnetic field, the change in flux linkages induces an EMF. This EMF drives a current through the flux meter coil, causing it to deflect. Because the controlling torque is zero and electromagnetic damping is very high, the final deflection angle of the pointer is directly proportional to the total change in flux linkages, entirely independent of the speed at which the flux changed.

**Proof that $\phi = (G/N)\theta$:**
*(Note: The prompt asks to prove $\phi = (G/N)\theta$. In standard texts, $G$ is the displacement constant of the flux meter, $N$ is turns of the search coil, $\phi$ is the flux, and $\theta$ is deflection. Let's align with the provided slide derivation on pg 82, which uses slightly different standard notation but arrives at the same physical relationship).*

Let:
*   $\Phi$ = Change in flux linking the search coil
*   $N$ = Number of turns in the search coil
*   $R$ = Total resistance of the flux meter circuit
*   $G$ = Displacement constant of the flux meter (equivalent to $N_{meter} B A$)
*   $\theta$ = Final angular deflection of the flux meter pointer

When flux $\Phi$ changes, an EMF $e$ is induced in the search coil:
$e = N \frac{d\Phi}{dt}$

This induces a current $i$ in the circuit:
$i = \frac{e}{R} = \frac{N}{R} \frac{d\Phi}{dt}$

The total charge $Q$ passing through the flux meter is the integral of this current over the time $t$ it takes for the flux to change:
$Q = \int i \, dt = \int \frac{N}{R} \frac{d\Phi}{dt} dt = \frac{N}{R} \int d\Phi = \frac{N \Phi}{R}$

For a ballistic galvanometer/flux meter, the total charge $Q$ is proportional to the deflection $\theta$. The charge indicated by the instrument is:
$Q = K_q \theta$ 
Where $K_q$ is the ballistic constant of the galvanometer. 
The ballistic constant $K_q$ is related to the displacement constant $G$ and circuit resistance $R$ by $K_q = \frac{G}{R}$ (in an ideal flux meter with no mechanical control, the electromagnetic damping dominates, making deflection proportional to total flux change).

Equating the two expressions for charge $Q$:
$\frac{N \Phi}{R} = K_q \theta$

Substituting $K_q = \frac{G}{R}$ (from the operational physics of the flux meter balancing impulsive torque against electromagnetic damping torque):
$\frac{N \Phi}{R} = \frac{G}{R} \theta$

Cancel $R$ from both sides:
$N \Phi = G \theta$

Rearranging to solve for $\Phi$:
**$\Phi = \left(\frac{G}{N}\right) \theta$**

This proves that the change in flux $\Phi$ is directly proportional to the deflection $\theta$, with $\frac{G}{N}$ acting as the proportionality constant.

Ans related location pg number in ak slide: 74, 75, 76, 81, 82. (The slides use a reversal technique leading to $2N\Phi$, but the fundamental proportionality requested in the prompt is derived here based on the general physics presented).

***

### 59. Page 3, Q.7(c): A test conducted on a sample of sheet laminations gave the following results at a maximum flux density of 1.0 $\text{wb/m}^2$ with the waveform purely sinusoidal. Use the data of the table below:
| Frequency, Hz | 25 | 40 | 50 | 75 |
| :--- | :--- | :--- | :--- | :--- |
| Iron loss, W/kg | 2.32 | 4.39 | 6.0 | 10.9 |
Determine-
(i) Hysteresis and eddy current loss in W/kg at 50 Hz and 1 $\text{Wb/m}^2$ and
(ii) At a maximum flux density of 1.2 $\text{Wb/m}^2$ when the frequency is 60 Hz and the form factor of the flux wave is 1.2. assume Steinmetz index as 1.6.

**Answer:**
Total Iron Loss ($P_i$) is the sum of Hysteresis Loss ($P_h$) and Eddy Current Loss ($P_e$).
$P_i = P_h + P_e$
We know:
$P_h = K_h f B_{max}^{1.6}$ (using Steinmetz index 1.6)
$P_e = K_e f^2 B_{max}^2 t^2$
For a given material at a constant $B_{max}$ ($1.0 \text{ Wb/m}^2$), the terms $K_h B_{max}^{1.6}$ and $K_e B_{max}^2 t^2$ are constants. Let's call them $A$ and $B$.
So, $P_i = A f + B f^2$
Dividing by $f$, we get a linear equation:
$\frac{P_i}{f} = A + B f$

Let's use the given data to find constants $A$ and $B$:
At $f_1 = 25 \text{ Hz}$, $P_{i1} = 2.32 \text{ W/kg} \implies \frac{P_{i1}}{f_1} = \frac{2.32}{25} = 0.0928$
At $f_2 = 50 \text{ Hz}$, $P_{i2} = 6.0 \text{ W/kg} \implies \frac{P_{i2}}{f_2} = \frac{6.0}{50} = 0.12$

We have two equations:
1) $A + 25B = 0.0928$
2) $A + 50B = 0.12$

Subtract (1) from (2):
$25B = 0.12 - 0.0928 = 0.0272$
$B = \frac{0.0272}{25} = 0.001088$

Substitute $B$ into (1) to find $A$:
$A + 25(0.001088) = 0.0928$
$A + 0.0272 = 0.0928$
$A = 0.0928 - 0.0272 = 0.0656$

**(i) Hysteresis and eddy current loss at 50 Hz and 1 $\text{Wb/m}^2$:**
*   Hysteresis Loss ($P_h$) $= A \times f = 0.0656 \times 50 =$ **$3.28 \text{ W/kg}$**
*   Eddy Current Loss ($P_e$) $= B \times f^2 = 0.001088 \times (50)^2 = 0.001088 \times 2500 =$ **$2.72 \text{ W/kg}$**
*(Check: Total Loss $= 3.28 + 2.72 = 6.0 \text{ W/kg}$, which matches the table data).*

**(ii) Losses at $B_{max} = 1.2 \text{ Wb/m}^2$, $f = 60 \text{ Hz}$, Form Factor ($k_f$) = 1.2:**
We need to determine the fundamental constants $K_h$ and $K_e$.
From part (i), at $B_{max} = 1.0$:
$A = K_h B_{max}^{1.6} \implies 0.0656 = K_h (1.0)^{1.6} \implies K_h = 0.0656$

For Eddy current loss, the generalized formula including Form Factor ($k_f$) is:
$P_e = K_e' \cdot k_f^2 \cdot f^2 \cdot B_{max}^2$
In part (i), the waveform was "purely sinusoidal", meaning $k_f = 1.11$.
$P_e(\text{at 50Hz, 1.0T}) = 2.72 = K_e' \cdot (1.11)^2 \cdot (50)^2 \cdot (1.0)^2$
$2.72 = K_e' \cdot 1.2321 \cdot 2500 \cdot 1$
$K_e' = \frac{2.72}{3080.25} \approx 0.000883$

Now, calculate new losses at $B_{max} = 1.2$, $f = 60$, $k_f = 1.2$:
*   **New Hysteresis Loss ($P_{h2}$):**
    $P_{h2} = K_h \cdot f \cdot B_{max}^{1.6}$
    $P_{h2} = 0.0656 \times 60 \times (1.2)^{1.6}$
    $P_{h2} \approx 3.936 \times 1.338$
    **$P_{h2} \approx 5.267 \text{ W/kg}$**
*   **New Eddy Current Loss ($P_{e2}$):**
    $P_{e2} = K_e' \cdot k_f^2 \cdot f^2 \cdot B_{max}^2$
    $P_{e2} = 0.000883 \times (1.2)^2 \times (60)^2 \times (1.2)^2$
    $P_{e2} = 0.000883 \times 1.44 \times 3600 \times 1.44$
    **$P_{e2} \approx 6.59 \text{ W/kg}$**

Ans related location pg number in ak slide: 83 mentions Separation of Iron losses, generic magnetic measurement problem.

***

### 60. Page 6, Q.5 b): What are the sources of inaccuracies in magnetic measurement? How can we determine the flux density of a specimen using ballistic galvanometer?

**Answer:**
**Sources of inaccuracies in magnetic measurement:**
Magnetic measurements, especially those using search coils and ballistic galvanometers, are prone to several errors:
1.  **Errors in the Ballistic Galvanometer:** 
    *   Incorrect calibration of the ballistic constant ($K_q$).
    *   Errors reading the exact maximum "throw" (deflection) of the pointer.
    *   Changes in the galvanometer's damping constant due to temperature variations or changes in external circuit resistance.
2.  **Errors in the Search Coil:**
    *   Imperfect alignment: The search coil must be exactly perpendicular to the magnetic flux lines. Any tilt reduces the effective area and leads to under-measurement.
    *   Inaccurate measurement of the cross-sectional area ($A$) of the specimen or the search coil.
    *   Inaccurate counting of the number of turns ($N$) in the search coil.
3.  **Flux Leakage:** Not all flux generated by the magnetizing coil passes cleanly through the search coil. Stray magnetic fields and fringing at the edges of the specimen can cause the search coil to measure less or more flux than is truly present in the bulk material.
4.  **Timing Errors:** For a ballistic measurement to be valid, the entire change in flux must occur before the moving coil has time to move significantly from its zero position. If the flux change is too slow (e.g., slowly pulling a magnet out), the ballistic equations become invalid, and the reading will be erroneously low.

**Determining flux density ($B$) using a ballistic galvanometer:**
To determine the flux density inside a specimen (like an iron ring):
1.  **Setup:** A secondary "search coil" (with $N$ turns and known cross-sectional area $A$) is wound tightly around the specimen. The search coil is connected in a closed circuit with a ballistic galvanometer and a current-limiting resistor.
2.  **Induction:** A primary magnetizing coil wound around the same specimen is connected to a DC supply. The current ($I$) in the primary coil is suddenly reversed (flipped from $+I$ to $-I$) using a reversing switch.
3.  **Measurement:** Reversing the current causes the magnetic flux inside the specimen to change from $+\Phi$ to $-\Phi$, making a total flux change of $2\Phi$. This rapid change in flux linkages ($2N\Phi$) induces a short, intense pulse of current (a charge $Q$) in the search coil circuit.
4.  **Deflection:** This pulse of charge causes the ballistic galvanometer to "throw" or swing to a maximum deflection angle $\theta_1$. The charge $Q$ is proportional to this deflection: $Q = K_q \theta_1$, where $K_q$ is the ballistic constant.
5.  **Calculation:** The total charge $Q$ is also related to the flux change by the circuit equation: $Q = \frac{2N\Phi}{R}$, where $R$ is the total resistance of the search coil circuit.
    Equating the two: $\frac{2N\Phi}{R} = K_q \theta_1$
    Solving for the flux $\Phi$: $\Phi = \frac{R K_q \theta_1}{2N}$
    Since Flux Density ($B$) is Flux divided by Area ($A$), $B = \frac{\Phi}{A}$:
    **$B = \frac{R K_q \theta_1}{2 N A}$**
    By knowing $R, K_q, N, A$, and reading $\theta_1$, the flux density $B$ is determined.

Ans related location pg number in ak slide: 80, 81, 82.

### 61. Page 6, Q.6 a): Define iron loss and describe the method of separation of iron loss of a metalic sheet.

**Answer:**
**Definition of Iron Loss:**
Iron loss (also known as core loss) is the continuous dissipation of electrical energy into heat that occurs within the magnetic core (made of iron or steel) of electrical machines like transformers and motors when they are subjected to an alternating magnetic field. This total loss is the sum of two distinct components:
1.  **Hysteresis Loss ($P_h$):** The energy lost due to the continuous molecular friction and realignment of magnetic domains within the iron as the alternating magnetic field repeatedly magnetizes and demagnetizes the core. It is proportional to the frequency ($f$).
2.  **Eddy Current Loss ($P_e$):** The energy lost due to localized, circulating $I^2R$ heating currents induced within the body of the iron core by the alternating magnetic flux. It is proportional to the square of the frequency ($f^2$).
Therefore, Total Iron Loss $P_i = P_h + P_e$.

**Method of Separation of Iron Loss:**
The separation of iron losses involves determining the individual values of hysteresis and eddy current losses from the total measured iron loss. This is done by testing the metallic sheet at two different frequencies while keeping the maximum flux density ($B_{max}$) strictly constant.

**Procedure:**
1.  **Mathematical Basis:** 
    We know $P_i = P_h + P_e$.
    Using empirical formulas:
    $P_h = A \cdot f$  (where $A$ is a constant $K_h B_{max}^x$)
    $P_e = B \cdot f^2$ (where $B$ is a constant $K_e B_{max}^2 t^2$)
    So, $P_i = A \cdot f + B \cdot f^2$.
    Dividing the entire equation by frequency $f$, we get a linear equation:
    **$\frac{P_i}{f} = A + B \cdot f$**
    This is an equation of a straight line ($y = c + mx$), where $y = \frac{P_i}{f}$, the y-intercept is $A$, and the slope is $B$.
2.  **Testing:** 
    *   The metallic sheet is formed into a test core (like an Epstein square).
    *   It is energized with an AC supply. The total power loss ($P_{i1}$) is measured at a known frequency ($f_1$) using a wattmeter, ensuring $B_{max}$ is kept at a specific target value.
    *   The frequency is then changed to a new value ($f_2$). The supply voltage is carefully adjusted simultaneously to ensure that $B_{max}$ remains exactly the same as in the first test. The new total power loss ($P_{i2}$) is measured.
3.  **Calculation (Separation):**
    You now have two equations with two unknowns ($A$ and $B$):
    $\frac{P_{i1}}{f_1} = A + B \cdot f_1$
    $\frac{P_{i2}}{f_2} = A + B \cdot f_2$
    By solving these two simultaneous equations, you determine the constants $A$ and $B$.
4.  **Final Result:**
    Once $A$ and $B$ are known for that specific $B_{max}$:
    *   **Hysteresis Loss at any frequency $f$** $= A \times f$
    *   **Eddy Current Loss at any frequency $f$** $= B \times f^2$
    This successfully separates the total loss into its two physical components.

Ans related location pg number in ak slide: 83 mentions Separation of Iron losses.

***

### 62. Page 7, Q.5 (a): Proof that the change in the value of flux is directly proportional to the change in the deflection in a flux meter.

**Answer:**
A flux meter is a specially designed, heavily damped ballistic galvanometer with virtually zero controlling torque (no control springs). 

Let:
*   $\Delta \Phi$ = Total change in flux linking the search coil
*   $N$ = Number of turns in the search coil
*   $R$ = Total resistance of the flux meter circuit (meter + search coil)
*   $G$ = Displacement constant of the flux meter ($N_{meter} B A$)
*   $D$ = Electromagnetic damping constant
*   $J$ = Moment of inertia of the moving system
*   $\theta$ = Deflection angle of the pointer

**Proof:**
1.  **Induced EMF and Current:** When the flux changes by $\Delta \Phi$ over a time $dt$, an EMF $e$ is induced in the search coil:
    $e = N \frac{d\Phi}{dt}$
    This drives a current $i$ through the flux meter circuit:
    $i = \frac{e}{R} = \frac{N}{R} \frac{d\Phi}{dt}$
2.  **Equation of Motion:** The deflecting torque $T_d$ is $G \cdot i$. Because there is no control spring ($K=0$), the equation of motion for the pointer is balanced entirely by inertia and damping:
    $T_d = J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt}$
    $G \cdot i = J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt}$
3.  **Substituting Current:** Replace $i$ with $\frac{N}{R} \frac{d\Phi}{dt}$:
    $\frac{GN}{R} \frac{d\Phi}{dt} = J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt}$
4.  **Integration over time:** To find the total deflection after the flux change has completed (and the pointer has stopped moving, so final velocity is zero), we integrate the entire equation with respect to time from $t=0$ (start of flux change, $\theta=0$, velocity=0) to $t=\infty$ (flux change complete, final deflection $\theta$, velocity=0):
    $\int_{0}^{\infty} \frac{GN}{R} \frac{d\Phi}{dt} dt = \int_{0}^{\infty} J \frac{d}{dt}\left(\frac{d\theta}{dt}\right) dt + \int_{0}^{\infty} D \frac{d\theta}{dt} dt$
    
    $\frac{GN}{R} [\Phi]_{initial}^{final} = J \left[ \frac{d\theta}{dt} \right]_{0}^{\infty} + D [\theta]_{0}^{\theta_{final}}$
5.  **Evaluating the Integral:**
    *   $[\Phi]_{initial}^{final}$ is the total change in flux, $\Delta \Phi$.
    *   The initial and final velocities ($\frac{d\theta}{dt}$) are both zero, so the inertia term $J [0 - 0] = 0$.
    *   The change in angle is from $0$ to $\theta$.
    
    Therefore, the integrated equation simplifies to:
    $\frac{GN}{R} \Delta \Phi = 0 + D \cdot \theta$
    $\Delta \Phi = \left( \frac{D \cdot R}{GN} \right) \theta$

In a flux meter, the electromagnetic damping $D$ is overwhelmingly dominant and is directly related to the circuit resistance and displacement constant ($D \approx \frac{G^2}{R}$). 
Replacing $D$ with $\frac{G^2}{R}$:
$\Delta \Phi = \left( \frac{\frac{G^2}{R} \cdot R}{GN} \right) \theta$
$\Delta \Phi = \left( \frac{G^2}{GN} \right) \theta$
$\Delta \Phi = \left( \frac{G}{N} \right) \theta$

Since $G$ (meter constant) and $N$ (search coil turns) are fixed constants, we have proven that:
**$\Delta \Phi \propto \theta$**
The change in flux is directly proportional to the change in deflection.

Ans related location pg number in ak slide: 74, 75, 76, 81, 82.

***

### 63. Page 7, Q.5 (c): Why separation of iron losses is important?

**Answer:**
Separation of iron losses (dividing the total core loss into its constituent Hysteresis loss and Eddy Current loss) is crucial in electrical engineering and the design of magnetic materials for several reasons:

1.  **Material Selection and Improvement:** Hysteresis loss depends entirely on the metallurgical composition and atomic structure of the magnetic material (e.g., carbon content, grain orientation). Eddy current loss depends largely on the physical geometry and electrical resistivity of the material (e.g., lamination thickness, silicon doping). By separating the losses, metallurgists and engineers know exactly *which* property of the steel needs to be improved. If hysteresis is high, they must improve the alloy composition. If eddy currents are high, they must use thinner laminations or increase resistivity.
2.  **Predicting Performance under Different Operating Conditions:** Machines often operate at varying frequencies or voltages (e.g., variable frequency drives, transformers under different grid conditions). Because hysteresis loss scales linearly with frequency ($\propto f$) while eddy current loss scales quadratically ($\propto f^2$), knowing the separated values allows designers to accurately mathematically predict total iron loss and cooling requirements at any given frequency, which is impossible if only the combined total loss is known.
3.  **Design Optimization:** In designing transformers and motors, engineers must strike a balance between manufacturing cost (e.g., ultra-thin laminations are expensive to cut and stack) and operational efficiency. Knowing the exact ratio of the two losses helps determine if the extra cost of thinner laminations is actually justified by the reduction in eddy current loss for a specific application.

Ans related location pg number in ak slide: 83.

***

### 64. Page 11, Q.3. (b): Explain the measurement of flux density in ring specimens using ballistic test. Hence show that $B = \frac{Rk_q\theta_1}{2N A_s}$, where the symbols have their usual meaning.

**Answer:**
**Measurement Explanation:**
The ballistic test is used to measure the magnetic properties (like flux density $B$) of a solid piece of ferromagnetic material formed into a continuous closed ring (a Rowland ring). This closed shape ensures there is no air gap, preventing magnetic flux leakage and allowing for highly accurate measurements of the material itself.
1.  The ring is uniformly wound with a primary **magnetizing coil**. This coil is connected to a DC power supply through a reversing switch, an ammeter, and a variable resistor to control the magnetizing current $I$.
2.  A secondary **search coil** (with $N$ turns) is wound tightly over a small section of the ring. This search coil is connected in a closed circuit with a ballistic galvanometer and a current-limiting resistance $R$.
3.  A steady current $I$ is established in the primary, creating a steady magnetic flux $+\Phi$ in the ring. The galvanometer rests at zero.
4.  The reversing switch is quickly thrown. This rapidly changes the primary current from $+I$ to $-I$. Consequently, the flux inside the ring collapses from $+\Phi$ to zero, and builds up in the opposite direction to $-\Phi$.
5.  This massive, rapid change in flux linkages induces a pulse of EMF and current in the search coil, passing a discrete pulse of charge $Q$ through the ballistic galvanometer.
6.  The galvanometer pointer "throws" to a maximum first deflection, $\theta_1$.

**Proof of the formula:**
Let:
*   $N$ = Number of turns in the search coil
*   $A_s$ = Cross-sectional area of the ring specimen
*   $R$ = Total resistance of the ballistic galvanometer circuit
*   $K_q$ = Ballistic constant of the galvanometer (charge per unit deflection)
*   $\Phi$ = Magnetic flux established in the ring

1.  **Change in Flux:** When the current is reversed, the flux changes from $+\Phi$ to $-\Phi$. 
    Total change in flux, $d\Phi = \Phi - (-\Phi) = 2\Phi$.
2.  **Charge Equation (Circuit Side):** According to Faraday's law, the induced EMF $e = N \frac{d\Phi}{dt}$. 
    The instantaneous current $i = \frac{e}{R} = \frac{N}{R} \frac{d\Phi}{dt}$.
    The total charge $Q$ pushed through the circuit is the integral of current:
    $Q = \int i \, dt = \int \frac{N}{R} \frac{d\Phi}{dt} dt = \frac{N}{R} \int d\Phi$
    Substitute the total change in flux ($2\Phi$) into the integral:
    $Q = \frac{N(2\Phi)}{R}$
3.  **Charge Equation (Galvanometer Side):** For a ballistic galvanometer, the total charge $Q$ passing through it is directly proportional to its first maximum deflection (throw), $\theta_1$:
    $Q = K_q \theta_1$
4.  **Equating and Solving:**
    Equate the two expressions for charge $Q$:
    $\frac{2N\Phi}{R} = K_q \theta_1$
    Solve for total flux $\Phi$:
    $\Phi = \frac{R K_q \theta_1}{2N}$
5.  **Calculating Flux Density ($B$):**
    Flux density $B$ is defined as flux per unit area, $B = \frac{\Phi}{A_s}$.
    Substitute the expression for $\Phi$ into this definition:
    **$B = \frac{R K_q \theta_1}{2 N A_s}$**
    This completes the proof.

Ans related location pg number in ak slide: 80, 81, 82.

### 65. Page 17, Q.8(a): Illustrate the separation of iron loss of ferromagnetic materials by variation of frequency.

**Answer:**
The total iron loss ($P_i$) in a ferromagnetic material subjected to an alternating magnetic field is the sum of Hysteresis loss ($P_h$) and Eddy Current loss ($P_e$).
$P_i = P_h + P_e$

According to theoretical equations:
*   Hysteresis loss: $P_h = K_h f B_{max}^x$
*   Eddy current loss: $P_e = K_e f^2 B_{max}^2 t^2$

Where $f$ is frequency, $B_{max}$ is maximum flux density, $K_h, K_e$ are material constants, $x$ is Steinmetz's constant, and $t$ is lamination thickness.

If we conduct tests on a specific sample (so $t$ is constant) and strictly maintain $B_{max}$ at a constant value during testing, the terms containing $B_{max}$ and $t$ become constants.
Let $a = K_h B_{max}^x$ and $b = K_e B_{max}^2 t^2$.
The total iron loss equation simplifies to a function of frequency:
$P_i = a \cdot f + b \cdot f^2$

To separate the losses, we divide the entire equation by $f$:
**$\frac{P_i}{f} = a + b \cdot f$**

**Illustration by Variation of Frequency:**
This equation is in the linear form $y = c + mx$, where:
*   y-axis variable = $\frac{P_i}{f}$ (Total energy loss per cycle)
*   x-axis variable = $f$ (Frequency)
*   y-intercept = $a$ (Hysteresis loss coefficient)
*   slope = $b$ (Eddy current loss coefficient)

**Experimental Procedure & Graphical Illustration:**
1.  **Testing:** We take the ferromagnetic specimen and test it at various different frequencies (e.g., 20 Hz, 30 Hz, 40 Hz, 50 Hz, 60 Hz). For *every* test, we must meticulously adjust the supply voltage to ensure that the maximum flux density ($B_{max}$) remains exactly the same. We measure the total iron loss $P_i$ at each frequency using a wattmeter.
2.  **Data Processing:** For each data point, calculate the value $\frac{P_i}{f}$.
3.  **Plotting:** Plot a graph with frequency $f$ on the horizontal x-axis and $\frac{P_i}{f}$ on the vertical y-axis.
4.  **Analysis:** Draw the best-fit straight line through the plotted points.
5.  **Separation:** 
    *   Extend the straight line backwards until it intersects the y-axis (where $f=0$). The value at this intercept is the constant **$a$**.
    *   Calculate the slope (gradient) of the straight line. This slope is the constant **$b$**.
6.  **Final Calculation:** Once $a$ and $b$ are found from the graph, you can calculate the individual losses for *any* frequency (say, $50\text{ Hz}$) at that specific $B_{max}$:
    *   Hysteresis Loss at 50Hz = $a \times 50$
    *   Eddy Current Loss at 50Hz = $b \times 50^2$

This graphical method clearly illustrates how varying the frequency while keeping $B_{max}$ constant allows the linear separation of the two loss components.

Ans related location pg number in ak slide: 83 mentions Separation of Iron losses.

***

### 66. Page 20, Q.5(c): A ring specimen of mild steel has a cross-section area of $600 \text{ mm}^2$ and a mean periphery of $0.25 \text{ m}$. It is uniformly wound with two coils, A and B having 80 and 300 turns, respectively. Coil B is connected to a ballistic galvanometer having a constant of $12 \times 10^{-9}$ coulomb per division; the total resistance of this circuit is $0.2 \text{ M}\Omega$. When a current of 2.2 A through the coil is reversed the galvanometer gives a maximum deflection of 180 divisions. Neglecting the damping of the galvanometer calculate flux density in the iron.

**Answer:**
This is a standard ballistic test problem. Coil A acts as the primary magnetizing coil, and Coil B acts as the secondary search coil.

**Given Data:**
*   Cross-sectional area of ring, $A_s = 600 \text{ mm}^2 = 600 \times 10^{-6} \text{ m}^2$
*   Mean periphery (length), $l = 0.25 \text{ m}$ (Not needed for calculating $B$ directly with given info, but useful for calculating $H$ or $\mu$).
*   Primary turns (Coil A), $N_1 = 80$ (Not needed for calculating $B$ directly).
*   Secondary turns (Coil B, search coil), $N_2 = 300$
*   Ballistic constant of galvanometer, $K_q = 12 \times 10^{-9} \text{ C/div}$
*   Total resistance of secondary circuit, $R = 0.2 \text{ M}\Omega = 0.2 \times 10^6 \, \Omega = 200,000 \, \Omega$
*   Primary current reversed, $I = 2.2 \text{ A}$
*   Galvanometer deflection (throw), $\theta_1 = 180 \text{ divisions}$

**Goal:** Calculate the flux density $B$ in the iron.

**1. Calculate the total charge ($Q$) passing through the galvanometer:**
The ballistic constant $K_q$ is given in Coulombs per division.
$Q = K_q \times \theta_1$
$Q = (12 \times 10^{-9} \text{ C/div}) \times 180 \text{ div}$
$Q = 2160 \times 10^{-9} \text{ Coulombs} = 2.16 \times 10^{-6} \text{ C}$

**2. Relate Charge to Flux Change:**
When the primary current is reversed, the flux inside the ring changes from $+\Phi$ to $-\Phi$.
Total change in flux, $\Delta \Phi = 2\Phi$
The charge $Q$ induced in the secondary (search coil) circuit is given by the formula:
$Q = \frac{N_2 \cdot \Delta \Phi}{R} = \frac{N_2 \cdot (2\Phi)}{R}$

**3. Solve for Flux ($\Phi$):**
Rearranging the formula to solve for $\Phi$:
$\Phi = \frac{Q \cdot R}{2 \cdot N_2}$
Substitute the values:
$\Phi = \frac{(2.16 \times 10^{-6} \text{ C}) \times (200,000 \, \Omega)}{2 \times 300}$
$\Phi = \frac{0.432}{600}$
$\Phi = 0.00072 \text{ Webers} = 7.2 \times 10^{-4} \text{ Wb}$

**4. Calculate Flux Density ($B$):**
Flux density is the flux per unit area.
$B = \frac{\Phi}{A_s}$
Substitute the values:
$B = \frac{7.2 \times 10^{-4} \text{ Wb}}{600 \times 10^{-6} \text{ m}^2}$
$B = \frac{7.2}{6}$
**$B = 1.2 \text{ Wb/m}^2$ (or Tesla)**

The flux density in the iron is **1.2 Tesla**.

Ans related location pg number in ak slide: 80, 81, 82 (Ballistic test equations).

***

### 67. Page 23, CT-01 Q2: Through deriving the relationship between the amount of flux and the angle of deflection, show that a flux meter has uniform scale.

**Answer:**
A flux meter is an inherently heavily damped ballistic galvanometer designed specifically with no mechanical control springs, meaning the restoring torque $T_c = 0$.

Let:
*   $\Delta \Phi$ = Total change in flux linking the search coil
*   $N$ = Number of turns in the search coil
*   $R$ = Total resistance of the flux meter circuit
*   $G$ = Displacement constant of the flux meter
*   $D$ = Electromagnetic damping constant of the flux meter
*   $\theta$ = Final angular deflection of the pointer

**Derivation:**
1.  **Induced EMF:** A change in flux $\Delta \Phi$ over time $dt$ induces an EMF $e$ in the search coil: $e = N \frac{d\Phi}{dt}$.
2.  **Current:** This induces a current $i$ in the circuit: $i = \frac{e}{R} = \frac{N}{R} \frac{d\Phi}{dt}$.
3.  **Torque Balance:** The driving deflecting torque is $T_d = G \cdot i$. Since there is no control spring, this torque is entirely opposed by the inertial torque ($J \frac{d^2\theta}{dt^2}$) and the damping torque ($D \frac{d\theta}{dt}$).
    $G \cdot i = J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt}$
    Substituting $i$:
    $\frac{GN}{R} \frac{d\Phi}{dt} = J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt}$
4.  **Integration:** We integrate this equation over the entire time $t$ from the start of the flux change to when the pointer comes to a complete rest at its final deflection $\theta$.
    $\int \frac{GN}{R} d\Phi = \int J \, d\left(\frac{d\theta}{dt}\right) + \int D \, d\theta$
    $\frac{GN}{R} \Delta \Phi = J(\text{final velocity} - \text{initial velocity}) + D(\theta - 0)$
    Since the pointer starts from rest and finishes at rest, both initial and final velocities are zero. The inertia term disappears.
    $\frac{GN}{R} \Delta \Phi = D\theta$
5.  **Relating Damping to Constants:** In a flux meter, electromagnetic damping is designed to be dominant. The electromagnetic damping constant $D$ is related to the displacement constant $G$ and circuit resistance $R$ by the relation $D = \frac{G^2}{R}$.
    Substitute $D = \frac{G^2}{R}$ into the equation:
    $\frac{GN}{R} \Delta \Phi = \left(\frac{G^2}{R}\right) \theta$
6.  **Simplifying:**
    Multiply both sides by $\frac{R}{G}$:
    $N \Delta \Phi = G \theta$
    Rearranging for $\theta$:
    **$\theta = \left(\frac{N}{G}\right) \Delta \Phi$**

**Conclusion regarding uniform scale:**
In the derived equation $\theta = \left(\frac{N}{G}\right) \Delta \Phi$, the term $\left(\frac{N}{G}\right)$ consists entirely of fixed physical constants (Number of turns in the search coil, and the displacement constant of the instrument). Let this ratio be a constant $k$.
So, $\theta = k \cdot \Delta \Phi$.
This shows a strict, linear mathematical relationship. The angle of deflection ($\theta$) is directly proportional to the amount of flux change ($\Delta \Phi$) to the power of 1. Because the relationship is purely linear, equal increments in flux will produce equal increments in angular deflection across the entire range of motion. Therefore, the scale of a flux meter is evenly and uniformly divided.

Ans related location pg number in ak slide: 74, 75, 76, 81, 82.

***

### 68. Page 28, Q1: "The shape of scale of a flux meter is uniform and it's angle of deflection does not depend on the inductance of both the search coil & the galvanometer." - Justify the statement with proper mathematical proof. [10]

**Answer:**
A flux meter is a special type of ballistic galvanometer featuring very heavy electromagnetic damping and no control spring. 

Let:
*   $\Phi$ = Flux linking the search coil
*   $N$ = Turns in the search coil
*   $G$ = Displacement constant of the flux meter
*   $R$ = Total resistance of the circuit
*   $L$ = Total self-inductance of the circuit (search coil + galvanometer)
*   $J$ = Moment of inertia of the moving system
*   $D$ = Air friction damping constant (assumed very small)
*   $\theta$ = Deflection angle

**Mathematical Proof:**
1.  **Circuit Equation including Inductance:** When flux $\Phi$ changes, the induced EMF $e = N\frac{d\Phi}{dt}$. 
    By Kirchhoff's voltage law for the closed circuit, this EMF must overcome the resistive voltage drop ($iR$), the back-EMF from the moving coil acting as a generator ($G\frac{d\theta}{dt}$), and the self-inductive voltage drop ($L\frac{di}{dt}$):
    $N\frac{d\Phi}{dt} = iR + G\frac{d\theta}{dt} + L\frac{di}{dt}$
    Rearranging for $iR$:
    $iR = N\frac{d\Phi}{dt} - G\frac{d\theta}{dt} - L\frac{di}{dt}$  --- (Equation A)

2.  **Mechanical Equation of Motion:** The driving torque ($Gi$) is opposed by inertia ($J\frac{d^2\theta}{dt^2}$) and air friction damping ($D\frac{d\theta}{dt}$). (Note: spring control $K=0$).
    $Gi = J\frac{d^2\theta}{dt^2} + D\frac{d\theta}{dt}$
    Isolating current $i$:
    $i = \frac{J}{G}\frac{d^2\theta}{dt^2} + \frac{D}{G}\frac{d\theta}{dt}$ --- (Equation B)

3.  **Substituting $i$:** Substitute Equation B into the left side of Equation A ($iR$):
    $R \left( \frac{J}{G}\frac{d^2\theta}{dt^2} + \frac{D}{G}\frac{d\theta}{dt} \right) = N\frac{d\Phi}{dt} - G\frac{d\theta}{dt} - L\frac{di}{dt}$

4.  **Integration over Time:** We integrate this entire equation over the time interval from $t=0$ (before flux changes, everything is zero) to $t=\infty$ (after flux has changed by $\Delta\Phi$, pointer has stopped at final deflection $\theta$).
    $\int_0^\infty \frac{RJ}{G} \frac{d^2\theta}{dt^2} dt + \int_0^\infty \frac{RD}{G} \frac{d\theta}{dt} dt = \int_0^\infty N \frac{d\Phi}{dt} dt - \int_0^\infty G \frac{d\theta}{dt} dt - \int_0^\infty L \frac{di}{dt} dt$

    Evaluating the integrals:
    *   $\int \frac{d^2\theta}{dt^2} dt$ evaluates to change in velocity. Since initial and final velocities are zero, this term is $0$.
    *   $\int \frac{di}{dt} dt$ evaluates to change in current. Since initial and final currents are zero, this term is $0$.
    *   $\int \frac{d\theta}{dt} dt$ evaluates to the final deflection $\theta$.
    *   $\int \frac{d\Phi}{dt} dt$ evaluates to the total change in flux $\Delta\Phi$.

    Applying these evaluations to the integrated equation:
    $0 + \frac{RD}{G}\theta = N \Delta\Phi - G\theta - 0$
    
    Notice that the term involving inductance ($L\frac{di}{dt}$) completely vanished during the integration because the current starts and ends at zero.

5.  **Final Simplification:**
    Rearrange the surviving terms:
    $G\theta + \frac{RD}{G}\theta = N \Delta\Phi$
    $\theta \left( G + \frac{RD}{G} \right) = N \Delta\Phi$
    
    In a well-designed flux meter, the air friction damping $D$ is deliberately made extremely small (negligible) compared to the electromagnetic damping. Therefore, the term $\frac{RD}{G}$ is approximately 0.
    $G\theta \approx N \Delta\Phi$
    **$\theta = \left(\frac{N}{G}\right) \Delta\Phi$**

**Justification:**
1.  **Uniform Scale:** The final equation $\theta = \left(\frac{N}{G}\right) \Delta\Phi$ shows that deflection $\theta$ is strictly directly proportional to the flux change $\Delta\Phi$ (to the power of 1). Since $N$ and $G$ are constants, the relationship is perfectly linear, proving the scale is uniform.
2.  **Independence from Inductance:** The self-inductance term $L$ was present in the initial differential equation. However, because the measurement depends on the *integral* of the entire event from a state of rest (zero current) back to a state of rest (zero current), the integral of the inductive voltage drop ($\int L \frac{di}{dt} dt = L \cdot \Delta i$) evaluates to exactly zero. Therefore, the final deflection equation mathematically contains no $L$ term, proving that the reading is entirely independent of the inductance of both the search coil and the galvanometer.

Ans related location pg number in ak slide: 76 (Theory of Flux meter equations).

### 69. Page 4, Q.3 (c): A current transformer with a bar primary has 300 turns in the secondary winding. The resistance and reactance of the secondary circuit are $1.5 \, \Omega$ and $1 \, \Omega$ respectively including the transformer winding. With 5 A flowing in the secondary winding, the magnetizing mmf is 100 A and the iron loss is 1.2 W. Determine the ratio and phase angle errors.

**Answer:**
**Given Data:**
*   Primary turns, $N_p = 1$ (Bar primary)
*   Secondary turns, $N_s = 300$
*   Nominal turn ratio, $n = \frac{N_s}{N_p} = 300$
*   Nominal Ratio, $K_n = 300$
*   Secondary resistance, $R_s = 1.5 \, \Omega$
*   Secondary reactance, $X_s = 1 \, \Omega$
*   Secondary current, $I_s = 5 \text{ A}$
*   Magnetizing mmf $= 100 \text{ A-turns}$. Since $N_p = 1$, the magnetizing current $I_m = \frac{100}{1} = 100 \text{ A}$.
*   Iron loss, $P_i = 1.2 \text{ W}$

**Step 1: Calculate the secondary circuit phase angle ($\Delta$) and parameters.**
Total secondary impedance, $Z_s = \sqrt{R_s^2 + X_s^2} = \sqrt{1.5^2 + 1^2} = \sqrt{2.25 + 1} = \sqrt{3.25} \approx 1.8028 \, \Omega$
$\sin \Delta = \frac{X_s}{Z_s} = \frac{1}{1.8028} \approx 0.5547$
$\cos \Delta = \frac{R_s}{Z_s} = \frac{1.5}{1.8028} \approx 0.8320$

**Step 2: Calculate the core loss component of primary current ($I_c$).**
The iron loss ($P_i$) is caused by the primary induced EMF ($E_p$).
First, calculate the secondary induced EMF ($E_s$):
$E_s = I_s \times Z_s = 5 \times 1.8028 = 9.014 \text{ V}$
Primary induced EMF ($E_p$) is related to $E_s$ by the turn ratio:
$E_p = \frac{E_s}{n} = \frac{9.014}{300} \approx 0.030047 \text{ V}$
The core loss component ($I_c$) is derived from the power loss equation ($P_i = E_p I_c$):
$I_c = \frac{P_i}{E_p} = \frac{1.2}{0.030047} \approx 39.937 \text{ A}$

**Step 3: Determine the Actual Ratio ($R$).**
Using the standard approximation formula for the actual transformation ratio of a CT:
$R \approx n + \frac{I_m \sin \Delta + I_c \cos \Delta}{I_s}$
$R \approx 300 + \frac{(100 \times 0.5547) + (39.937 \times 0.8320)}{5}$
$R \approx 300 + \frac{55.47 + 33.228}{5}$
$R \approx 300 + \frac{88.698}{5}$
$R \approx 300 + 17.74 = 317.74$

**Step 4: Calculate the Ratio Error.**
Ratio Error (%) $= \frac{\text{Nominal Ratio} (K_n) - \text{Actual Ratio} (R)}{\text{Actual Ratio} (R)} \times 100$
Ratio Error (%) $= \frac{300 - 317.74}{317.74} \times 100 = \frac{-17.74}{317.74} \times 100 \approx \mathbf{-5.58\%}$

**Step 5: Calculate the Phase Angle Error ($\theta$).**
Using the standard approximation formula for phase angle error (in radians):
$\theta \approx \frac{I_m \cos \Delta - I_c \sin \Delta}{n I_s} \text{ radians}$
$\theta \approx \frac{(100 \times 0.8320) - (39.937 \times 0.5547)}{300 \times 5}$
$\theta \approx \frac{83.20 - 22.153}{1500} = \frac{61.047}{1500} \approx 0.0407 \text{ radians}$
Convert radians to degrees:
$\theta (\text{degrees}) = 0.0407 \times \left(\frac{180}{\pi}\right) \approx \mathbf{2.33^\circ}$

Ans related location pg number in ak slide: 127, 128, 129, 130.

***

### 70. Page 6, Q.6 b): A single phase potential transformer has a turns ratio of 3810/63. The nominal secondary voltage is 63V and the total equivalent resistance and leakage reactance referred to the secondary side are $2 \, \Omega$ and $1 \, \Omega$, respectively. Calculate the ratio and phase angle errors when the transformer is supplying a burden of $(100 + j200)\Omega$.

**Answer:**
**Given Data:**
*   Nominal Turns Ratio, $n = \frac{3810}{63} = 60.476$
*   Nominal Secondary Voltage, $V_s = 63 \text{ V}$
*   Equivalent resistance (referred to secondary), $R_{es} = 2 \, \Omega$
*   Equivalent reactance (referred to secondary), $X_{es} = 1 \, \Omega$
*   Internal secondary impedance, $Z_{es} = 2 + j1 \, \Omega$
*   Load Burden, $Z_L = 100 + j200 \, \Omega$

**Step 1: Calculate the Secondary Current ($I_s$) and Phase Angle.**
Taking the secondary terminal voltage $V_s$ as the reference phasor: $V_s = 63 \angle 0^\circ \text{ V}$.
The load current $I_s$ flows through the burden $Z_L$:
$I_s = \frac{V_s}{Z_L} = \frac{63 \angle 0^\circ}{100 + j200}$
Convert $Z_L$ to polar form: $Z_L = \sqrt{100^2 + 200^2} \angle \arctan(\frac{200}{100}) = 223.6 \angle 63.43^\circ \, \Omega$
$I_s = \frac{63 \angle 0^\circ}{223.6 \angle 63.43^\circ} = 0.2817 \angle -63.43^\circ \text{ A}$
In rectangular form:
$I_s = 0.2817 (\cos(-63.43^\circ) + j\sin(-63.43^\circ)) = 0.126 - j0.252 \text{ A}$

**Step 2: Calculate the primary voltage referred to secondary ($V_p/n$).**
The primary voltage referred to the secondary side must overcome both the terminal voltage and the internal voltage drop across $Z_{es}$:
$\frac{V_p}{n} = V_s + I_s Z_{es}$
$\frac{V_p}{n} = (63 + j0) + (0.126 - j0.252)(2 + j1)$
$\frac{V_p}{n} = 63 + (0.126 \times 2 - (-0.252) \times 1) + j(0.126 \times 1 + (-0.252) \times 2)$
$\frac{V_p}{n} = 63 + (0.252 + 0.252) + j(0.126 - 0.504)$
$\frac{V_p}{n} = 63 + 0.504 - j0.378$
$\frac{V_p}{n} = 63.504 - j0.378 \text{ V}$

**Step 3: Find the magnitude and phase of $V_p/n$.**
Magnitude $\left| \frac{V_p}{n} \right| = \sqrt{63.504^2 + (-0.378)^2} \approx 63.505 \text{ V}$
Phase angle $\theta = \arctan\left(\frac{-0.378}{63.504}\right) \approx -0.341^\circ$

**Step 4: Calculate the Actual Ratio ($R$) and Ratio Error.**
The actual transformation ratio $R$ is defined as $V_p / V_s$:
$V_p = n \times 63.505 = \left(\frac{3810}{63}\right) \times 63.505 \approx 3840.54 \text{ V}$
Actual Ratio, $R = \frac{V_p}{V_s} = \frac{3840.54}{63} = \mathbf{60.96}$
(Alternatively, $R = n \times \frac{|V_p/n|}{V_s} = 60.476 \times \frac{63.505}{63} \approx 60.96$)

Ratio Error (%) $= \frac{\text{Nominal Ratio} (K_n) - \text{Actual Ratio} (R)}{\text{Actual Ratio} (R)} \times 100$
Ratio Error (%) $= \frac{60.476 - 60.96}{60.96} \times 100 = \frac{-0.484}{60.96} \times 100 \approx \mathbf{-0.794\%}$

**Step 5: Phase Angle Error.**
The phase angle error is the angle between the reversed secondary voltage vector and the primary voltage vector. This corresponds to the angle of $\frac{V_p}{n}$ relative to $V_s$.
From Step 3, the angle is $\mathbf{-0.341^\circ}$. (The negative sign indicates $V_s$ leads the reversed $V_p$, which is a conventional designation for a negative phase angle error).

Ans related location pg number in ak slide: Relates to the general Instrument Transformer chapter spanning 126-130.

***

### 71. Page 6, Q.7 a): What is meant by instrument transformer? Why the secondary of CT never should be opened?

**Answer:**
**What is meant by an instrument transformer?**
Instrument transformers are high-accuracy, specialized electrical transformers (either Current Transformers - CTs, or Potential Transformers - PTs) used to step down excessively high voltages or high currents to safely measurable, standardized low levels (typically 110V for PTs and 5A or 1A for CTs). They serve two critical purposes in power systems:
1.  They provide accurate scaled-down replicas of the main line current/voltage for metering (ammeters, voltmeters, wattmeters) and protective relays.
2.  They safely electrically isolate the measuring instruments and the operating personnel from the dangerously high voltage power grid.

**Why the secondary of a CT should never be opened:**
The primary winding of a Current Transformer (CT) is connected in series with the main high-power line. Therefore, the primary current ($I_p$) flowing through it is dictated entirely by the load on the main line, not by the CT's secondary circuit. 
In normal operation, the primary current generates a massive magnetomotive force (MMF). However, the current circulating in the shorted secondary winding generates a counter-MMF that directly opposes the primary MMF. Because these two forces almost entirely cancel each other out, only a tiny "magnetizing current" remains to actually flux the core.

If the secondary circuit is accidentally or deliberately opened while the primary is energized:
1.  The secondary current ($I_s$) instantly drops to zero.
2.  The opposing secondary counter-MMF completely vanishes.
3.  The *entire* massive primary current ($I_p$) now acts solely as the magnetizing current.
4.  This generates an extremely high, unopposed magnetic flux that deeply saturates the iron core. This extreme flux variation induces a lethally **high voltage** across the open secondary terminals, which can critically shock operating personnel, arc across the terminals, and destroy the instrument's insulation.
5.  Additionally, the saturated core will undergo extreme hysteresis and eddy current losses, producing intense heat that can physically melt or ignite the transformer. Therefore, a CT secondary must always be short-circuited or connected to a low-impedance burden before it is energized.

Ans related location pg number in ak slide: 126, 127.

***

### 72. Page 7, Q.7 (b): A current transformer has a single turn primary and a 200 turns secondary winding. The secondary winding supplies a current of 5 A to a non-inductive burden of $1 \, \Omega$ resistance. The requisite flux is setup in the core by an mmf of 80 A. The frequency is 50 Hz and net cross-section of the core is $1000 \text{ mm}^2$. Calculate the ratio and phase angle of the transformer. Neglect the effect of magnetic, leakage, iron losses, and $I^2R$ losses.

**Answer:**
**Given Data:**
*   Primary turns, $N_p = 1$
*   Secondary turns, $N_s = 200$
*   Nominal turn ratio, $n = \frac{200}{1} = 200$
*   Secondary current, $I_s = 5 \text{ A}$
*   Secondary burden, $R_b = 1 \, \Omega$ (Non-inductive, so reactance $X_b = 0$). Note: Because the problem states to neglect leakage and $I^2R$ (copper) losses, we ignore the internal impedance of the secondary winding itself.
*   Magnetizing mmf $= 80 \text{ A-turns}$. Since $N_p = 1$, Magnetizing current $I_m = \frac{80}{1} = 80 \text{ A}$.
*   Iron losses are neglected, so the core loss current $I_c = 0 \text{ A}$.

**Step 1: Determine the phase angle ($\Delta$) of the secondary circuit.**
Because the burden is purely non-inductive (resistive) and internal reactances are neglected, the secondary current $I_s$ is perfectly in phase with the secondary induced EMF $E_s$.
Therefore, the secondary phase angle $\Delta = 0^\circ$.
This means $\sin \Delta = 0$ and $\cos \Delta = 1$.

**Step 2: Calculate the Exact Primary Current ($I_p$).**
Using the primary current phasor relationship:
$I_p = \sqrt{(n I_s \cos \Delta + I_c)^2 + (n I_s \sin \Delta + I_m)^2}$
Substitute the known values ($I_c = 0$, $\Delta = 0^\circ$):
$I_p = \sqrt{(n I_s \times 1 + 0)^2 + (n I_s \times 0 + I_m)^2}$
$I_p = \sqrt{(n I_s)^2 + (I_m)^2}$
$I_p = \sqrt{(200 \times 5)^2 + (80)^2}$
$I_p = \sqrt{(1000)^2 + (80)^2} = \sqrt{1,000,000 + 6400} = \sqrt{1,006,400}$
$I_p \approx 1003.195 \text{ A}$

**Step 3: Calculate the Actual Ratio ($R$).**
The actual transformation ratio is $R = \frac{I_p}{I_s}$:
$R = \frac{1003.195}{5} = \mathbf{200.639}$

**Step 4: Calculate the Phase Angle ($\theta$).**
The phase angle $\theta$ (the angle by which the reversed secondary current phasor leads the primary current phasor) is calculated using the formula:
$\tan \theta = \frac{n I_s \sin \Delta + I_m}{n I_s \cos \Delta + I_c}$
Substitute the known values:
$\tan \theta = \frac{(200 \times 5 \times 0) + 80}{(200 \times 5 \times 1) + 0} = \frac{80}{1000} = 0.08$
$\theta = \arctan(0.08) \approx \mathbf{4.57^\circ}$

*(Note: The area and frequency provided in the prompt are extraneous information not required to solve for the ratio and phase angle under these neglected conditions).*

Ans related location pg number in ak slide: 127, 128, 129, 130.

### 73. Page 9, Q.5. (b): Derive the expression of ration error of a CT by sketching the vector diagram clearly. [figure Involved - note reference to vector diagram]

**Answer:**
**Derivation of Ratio Error:**

**1. Reference to Vector Diagram [figure Involved]:**
*(Note: Please refer to the phasor diagram on slide 128/129 for the visual representation).*
*   The main magnetic flux ($\Phi$) is taken as the horizontal reference vector.
*   The primary induced EMF ($E_p$) and secondary induced EMF ($E_s$) lag the flux by $90^\circ$ (pointing downwards).
*   The secondary current ($I_s$) lags $E_s$ by the secondary phase angle $\delta$ (determined by the burden and internal impedance).
*   The reversed secondary current ($nI_s$ or $I_s'$) is drawn in the second quadrant, leading $\Phi$ by $(90^\circ - \delta)$.
*   The exciting current ($I_o$) is composed of the magnetizing component ($I_m$ in phase with $\Phi$) and the core loss component ($I_c$ leading $\Phi$ by $90^\circ$). $I_o$ leads $\Phi$ by angle $\alpha$.
*   The total primary current ($I_p$) is the vector sum of $I_o$ and $nI_s$.

**2. Derivation of Primary Current ($I_p$):**
To find the magnitude of $I_p$, we project $nI_s$ and $I_o$ onto a common horizontal and vertical axis (taking $nI_s$ as the primary reference is mathematically easier).
The angle between $nI_s$ and $I_o$ is $(90^\circ - \alpha - \delta)$.
Using the geometric projection method from the phasor diagram (slide 129):
Let's define the components parallel and perpendicular to $nI_s$:
*   Component of $I_o$ parallel to $nI_s$: $I_o \cos(90^\circ - \alpha - \delta) = I_o \sin(\alpha + \delta)$
*   Component of $I_o$ perpendicular to $nI_s$: $I_o \sin(90^\circ - \alpha - \delta) = I_o \cos(\alpha + \delta)$

We know from the diagram that $I_o \sin\alpha = I_c$ and $I_o \cos\alpha = I_m$.
Expanding the parallel term:
$I_o \sin(\alpha + \delta) = I_o (\sin\alpha \cos\delta + \cos\alpha \sin\delta) = I_c \cos\delta + I_m \sin\delta$
Expanding the perpendicular term:
$I_o \cos(\alpha + \delta) = I_o (\cos\alpha \cos\delta - \sin\alpha \sin\delta) = I_m \cos\delta - I_c \sin\delta$

The magnitude of $I_p$ is:
$I_p = \sqrt{[nI_s + I_o \sin(\alpha + \delta)]^2 + [I_o \cos(\alpha + \delta)]^2}$

**3. Approximation for Actual Ratio ($R$):**
Since the exciting current $I_o$ is very small compared to the primary current $I_p$, the perpendicular component $[I_o \cos(\alpha + \delta)]^2$ is negligible.
Therefore, $I_p \approx nI_s + I_o \sin(\alpha + \delta)$
$I_p \approx nI_s + I_m \sin\delta + I_c \cos\delta$

The actual transformation ratio $R = \frac{I_p}{I_s}$:
**$R = \frac{nI_s + I_m \sin\delta + I_c \cos\delta}{I_s} = n + \frac{I_m \sin\delta + I_c \cos\delta}{I_s}$**

**4. Defining Ratio Error:**
Ratio Error is defined as the deviation of the actual ratio ($R$) from the nominal ratio ($K_n$, which is typically the turn ratio $n$), expressed as a percentage of the actual ratio.
Ratio Error (%) $= \left( \frac{K_n - R}{R} \right) \times 100\%$

Substituting the approximate value of $R$:
Since $R \approx K_n$, the denominator is often just taken as $R$ or $n$ for practical percentage calculations. 
The absolute error is $(K_n - R) \approx n - (n + \frac{I_m \sin\delta + I_c \cos\delta}{I_s}) = - \left(\frac{I_m \sin\delta + I_c \cos\delta}{I_s}\right)$.
Therefore, the Ratio Error formula becomes:
**Ratio Error (%) $\approx - \frac{I_m \sin\delta + I_c \cos\delta}{I_s \cdot R} \times 100\%$**

Ans related location pg number in ak slide: 128, 129.

***

### 74. Page 17, Q.8(c): Mention the advantages of instrument transformer. Clarify why the secondary of a CT can not be kept open while energized.

**Answer:**
**Advantages of Instrument Transformers:**
1.  **Safety & Isolation:** They electrically isolate the delicate measuring instruments, relays, and operating personnel from the high-voltage, high-power primary circuits, ensuring safety.
2.  **Standardization:** They allow the standardization of measuring instruments. Because CTs universally step down current to 5A or 1A, and PTs step down voltage to 110V, standard ammeters and voltmeters can be manufactured regardless of the actual grid voltage, lowering costs and simplifying replacements.
3.  **Measurement of High Quantities:** They enable the measurement of extremely high voltages and currents that would be practically and economically impossible to route directly through the physical coils of standard meters.
4.  **Remote Monitoring:** Because the secondary signals are low power (5A, 110V), the measuring instruments can be located safely on control panels far away from the actual high-voltage equipment.
5.  **Multiple Connections:** A single instrument transformer can feed multiple instruments or relays simultaneously, provided the total burden remains within the transformer's rated capacity.

**Why the secondary of a CT cannot be kept open while energized:**
*(This is identical to the second part of Q71).*
A CT's primary winding is in series with the main power line, so its primary current ($I_p$) is dictated solely by the main load, completely independent of the CT's secondary circuit. 
Normally, the primary current generates a large magnetomotive force (MMF). However, the current circulating in the shorted secondary winding generates a counter-MMF that almost perfectly cancels the primary MMF. This leaves only a very small net magnetizing current to flux the core.

If the secondary circuit is opened while the primary is carrying current:
1.  The secondary current instantly drops to zero, and the opposing secondary counter-MMF disappears.
2.  The *entire* primary current now acts as the magnetizing current ($I_p = I_m$).
3.  This massive, unopposed magnetizing force drives the iron core into deep magnetic saturation, creating a highly distorted, flat-topped flux waveform.
4.  Because induced voltage is proportional to the *rate of change* of flux ($e = N \frac{d\Phi}{dt}$), the steep sides of this distorted flux waveform induce an extremely **high, lethal voltage spike** across the open secondary terminals. This can easily break down the transformer's insulation, cause arc flashes, and be fatal to personnel.
5.  The saturated core also experiences extreme hysteresis and eddy current losses, producing intense heat that can quickly physically destroy the transformer. Therefore, a CT secondary must always be shorted before disconnecting any burden.

Ans related location pg number in ak slide: 126, 127.

***

### 75. Page 4, Q.4 (b): What value should $C_1$ have for $V_0$ to be equal to $0.1V_i$ for the circuit shown in following figure? [figure Involved]

**Answer:**
**Understanding the Circuit [Figure Involved]:**
The figure shown in the prompt represents an **Attenuator probe** circuit, which is commonly used to connect signals to a Cathode Ray Oscilloscope (CRO) while stepping down the voltage. 
The circuit is a voltage divider composed of two parallel $RC$ branches connected in series.
*   **Top Branch:** Resistor $R_1$ ($900 \text{ k}\Omega$) in parallel with an unknown variable capacitor $C_1$.
*   **Bottom Branch:** Resistor $R_2$ ($100 \text{ k}\Omega$) in parallel with a fixed capacitor $C_2$ ($45 \text{ pF}$).
*   $V_i$ is the input voltage applied across the entire series combination.
*   $V_0$ is the output voltage taken across the bottom branch ($R_2 || C_2$).

**Goal:** We need to find $C_1$ such that the attenuation ratio is exactly 10:1 (i.e., $V_0 = 0.1 V_i$), independent of the frequency of the input signal.

**Condition for Frequency-Independent Attenuation:**
For a compensated attenuator probe to provide a consistent division ratio across all frequencies (from DC to high-frequency AC), the time constants of the two $RC$ parallel branches must be exactly equal. This ensures that the capacitive voltage divider ratio precisely matches the resistive voltage divider ratio.

The resistive division ratio is:
$\frac{V_0}{V_i} = \frac{R_2}{R_1 + R_2} = \frac{100\text{k}}{900\text{k} + 100\text{k}} = \frac{100\text{k}}{1000\text{k}} = 0.1$
The circuit is already designed for a 0.1 resistive attenuation.

To make it frequency-independent, we must equate the time constants:
$\tau_1 = \tau_2$
**$R_1 \times C_1 = R_2 \times C_2$**

**Calculation:**
Substitute the given values into the equation:
$R_1 = 900 \times 10^3 \, \Omega$
$R_2 = 100 \times 10^3 \, \Omega$
$C_2 = 45 \text{ pF} = 45 \times 10^{-12} \text{ F}$

$(900 \times 10^3) \times C_1 = (100 \times 10^3) \times (45 \times 10^{-12})$
$900,000 \times C_1 = 4,500,000 \times 10^{-12}$
$C_1 = \frac{4,500,000 \times 10^{-12}}{900,000}$
$C_1 = 5 \times 10^{-12} \text{ F}$

**$C_1 = 5 \text{ pF}$**

For $V_0$ to be equal to $0.1 V_i$ consistently, the variable capacitor $C_1$ must be tuned to exactly **$5 \text{ pF}$**.

Ans related location pg number in ak slide: Not explicitly derived in slides, standard CRO probe compensation problem.

***

### 76. Page 5, Q.8 (a): Illustrate the concept of dissipation factor of a capacitor with proper phasor diagram.

**Answer:**
**Concept of Dissipation Factor ($D$):**
In an ideal capacitor, the current leads the voltage by exactly $90^\circ$, meaning it stores and releases energy with 100% efficiency and zero power loss. However, practical capacitors always have some internal energy losses (due to dielectric heating, leakage current, and lead resistance). 
These losses mean the current leads the voltage by an angle slightly less than $90^\circ$. 
Let $\phi$ be the actual phase angle. The small angle by which the current falls short of the ideal $90^\circ$ lead is called the **loss angle ($\delta$)**. Therefore, $\phi + \delta = 90^\circ$.
The **Dissipation Factor ($D$)** is a measure of these energy losses and is defined mathematically as the tangent of the loss angle:
**$D = \tan(\delta)$**

**Illustration with Phasor Diagram:**
A practical "lossy" capacitor can be modeled electrically as an ideal, lossless capacitor ($C$) connected in series with a small equivalent series resistance ($R_s$) representing the losses.

1.  **Phasor Construction:**
    *   Let the current $I$ be the horizontal reference phasor.
    *   The voltage drop across the ideal capacitor part ($V_C$) lags the current $I$ by exactly $90^\circ$. Draw $V_C$ pointing straight down.
    *   The voltage drop across the equivalent series resistance ($V_R$) is perfectly in phase with the current $I$. Draw $V_R$ horizontally along the $I$ axis.
    *   The total applied voltage ($V$) is the vector sum of $V_R$ and $V_C$.
2.  **Identifying the Angles:**
    *   The angle between the total voltage $V$ and the current $I$ is the actual phase angle **$\phi$**.
    *   The angle between the total voltage $V$ and the ideal capacitor voltage $V_C$ is the loss angle **$\delta$**.
3.  **Relating to the Formula:**
    From the right-angled triangle formed by the voltage phasors ($V, V_R, V_C$):
    $\tan(\delta) = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{V_R}{V_C}$
    Since $V_R = I \cdot R_s$ and $V_C = I \cdot X_C = I \cdot (\frac{1}{\omega C})$:
    $\tan(\delta) = \frac{I \cdot R_s}{I \cdot (\frac{1}{\omega C})} = \frac{R_s}{\frac{1}{\omega C}}$
    **$D = \tan(\delta) = \omega C R_s$**

This illustrates that the dissipation factor is directly proportional to the series resistance (representing the physical losses) and the operating frequency. A lower $D$ indicates a higher quality, more efficient capacitor. (Note: $D$ is also the inverse of the Quality Factor, $Q$).

Ans related location pg number in ak slide: Not explicitly derived in slides, generic AC bridge/capacitor theory.

### 77. Page 5, Q.5 (a): Graphically analyze the Lissajous patterns generated in the CRO when two sinusoid at voltages of equal magnitude and frequency are applied to the vertical and horizontal deflection plates, but the signal at vertical deflection plate has the following phase angle: (i) $0^\circ$ (ii) $45^\circ$ and (iii) $90^\circ$

**Answer:**
Lissajous patterns are generated on a CRO screen when two sinusoidal signals are applied simultaneously to the X (horizontal) and Y (vertical) deflection plates. 
Let the horizontal signal be $V_x = V_m \sin(\omega t)$.
Let the vertical signal be $V_y = V_m \sin(\omega t + \phi)$, where $\phi$ is the phase angle difference.

**(i) Phase angle $\phi = 0^\circ$:**
Both signals are perfectly in phase: $V_x = V_m \sin(\omega t)$ and $V_y = V_m \sin(\omega t)$.
Since $V_x = V_y$ at every instant in time, the electron beam is deflected equally in both the horizontal and vertical directions simultaneously.
*   At $t=0$, $V_x=0, V_y=0$ (spot is at origin).
*   As $t$ increases, $V_x$ and $V_y$ increase equally and positively.
*   At $t = \frac{T}{4}$ (peak), $V_x = V_m, V_y = V_m$ (spot is at top right).
*   During the negative half-cycle, the spot moves to the bottom left.
*   **Resulting Pattern:** A **straight diagonal line** passing through the origin in the first and third quadrants, with a positive slope of 1 (a $45^\circ$ angle relative to the X-axis).
*(See slide 122 for visual reference).*

**(ii) Phase angle $\phi = 45^\circ$:**
The vertical signal leads the horizontal by $45^\circ$ (or $\pi/4$ radians): $V_x = V_m \sin(\omega t)$ and $V_y = V_m \sin(\omega t + 45^\circ)$.
*   At $\omega t = 0^\circ$: $V_x = 0$, $V_y = V_m \sin(45^\circ) \approx 0.707 V_m$. The spot is on the positive Y-axis.
*   At $\omega t = 45^\circ$: $V_x = 0.707 V_m$, $V_y = V_m \sin(90^\circ) = V_m$. The spot is at maximum Y deflection.
*   At $\omega t = 90^\circ$: $V_x = V_m$, $V_y = V_m \sin(135^\circ) \approx 0.707 V_m$. The spot is at maximum X deflection.
*   **Resulting Pattern:** As the cycle continues, the spot traces an **ellipse** whose major axis lies in the first and third quadrants.
*(See slide 124 for visual reference of a general $\phi$ angle ellipse).*

**(iii) Phase angle $\phi = 90^\circ$:**
The vertical signal leads the horizontal by exactly $90^\circ$: $V_x = V_m \sin(\omega t)$ and $V_y = V_m \sin(\omega t + 90^\circ) = V_m \cos(\omega t)$.
*   At $\omega t = 0^\circ$: $V_x = 0$, $V_y = V_m \cos(0) = V_m$. The spot is at the top of the Y-axis.
*   At $\omega t = 90^\circ$: $V_x = V_m$, $V_y = V_m \cos(90^\circ) = 0$. The spot is at the far right of the X-axis.
*   At $\omega t = 180^\circ$: $V_x = 0$, $V_y = V_m \cos(180^\circ) = -V_m$. The spot is at the bottom of the Y-axis.
*   At $\omega t = 270^\circ$: $V_x = -V_m$, $V_y = V_m \cos(270^\circ) = 0$. The spot is at the far left of the X-axis.
*   Since $\sin^2(\omega t) + \cos^2(\omega t) = 1$, we have $(V_x / V_m)^2 + (V_y / V_m)^2 = 1$, which is the equation of a circle with radius $V_m$.
*   **Resulting Pattern:** A perfect **circle**.
*(See slide 123 for visual reference).*

Ans related location pg number in ak slide: 122, 123, 124.

***

### 78. Page 5, Q.5 (b): "For a given accelerating voltage, and for particular dimensions of CRT, the deflection of the electron beam is directly proportional to the deflecting voltage."- Justify the statement mathematically.

**Answer:**
Let's analyze the path of an electron traveling through the electrostatic deflection plates of a CRT.
Let:
*   $v_{ox}$ = axial velocity of the electron upon entering the deflecting plates. This is determined by the accelerating voltage ($E_a$). $v_{ox} = \sqrt{\frac{2e E_a}{m}}$
*   $E_d$ = potential difference (deflecting voltage) applied across the deflection plates.
*   $d$ = distance between the deflecting plates.
*   $l_d$ = length of the deflecting plates.
*   $L$ = distance from the center of the deflecting plates to the fluorescent screen.
*   $e$ = charge of an electron.
*   $m$ = mass of an electron.
*   $D$ = total vertical deflection of the spot on the screen.

**Mathematical Justification:**
1.  **Electric Field and Force:** The deflecting voltage creates a uniform electric field $E = \frac{E_d}{d}$ between the plates. This field exerts a constant vertical force on the electron: $F_y = eE = \frac{e E_d}{d}$.
2.  **Vertical Acceleration:** This force causes a constant vertical acceleration ($a_y$) while the electron is between the plates: $a_y = \frac{F_y}{m} = \frac{e E_d}{m d}$.
3.  **Time in Plates:** The horizontal velocity $v_{ox}$ remains constant. The time ($t$) the electron spends between the plates is $t = \frac{l_d}{v_{ox}}$.
4.  **Vertical Velocity:** Upon exiting the plates, the electron has acquired a vertical velocity component ($v_y$):
    $v_y = a_y t = \left( \frac{e E_d}{m d} \right) \left( \frac{l_d}{v_{ox}} \right)$
5.  **Deflection Angle:** The electron leaves the plates at an angle $\theta$ relative to the horizontal axis. 
    $\tan \theta = \frac{v_y}{v_{ox}} = \frac{e E_d l_d}{m d v_{ox}^2}$
6.  **Total Screen Deflection ($D$):** Geometrically, if we trace the angled path straight back, it intersects the axis exactly at the center of the deflecting plates. Therefore, the total deflection $D$ on the screen is formed by a large right triangle with adjacent side $L$ and opposite side $D$.
    $\tan \theta = \frac{D}{L}$
    Equating the two expressions for $\tan \theta$:
    $\frac{D}{L} = \frac{e E_d l_d}{m d v_{ox}^2}$
    $D = \frac{L l_d e E_d}{m d v_{ox}^2}$
7.  **Substituting Accelerating Voltage:** We know the kinetic energy gained from the accelerating voltage is $\frac{1}{2} m v_{ox}^2 = e E_a$, so $v_{ox}^2 = \frac{2 e E_a}{m}$. Substituting this into the deflection equation:
    $D = \frac{L l_d e E_d}{m d \left( \frac{2 e E_a}{m} \right)} = \frac{L l_d E_d}{2 d E_a}$

**Conclusion:**
Looking at the final equation: **$D = \left( \frac{L l_d}{2 d E_a} \right) E_d$**
The term in the parentheses consists entirely of the fixed physical dimensions of the CRT ($L, l_d, d$) and the constant accelerating voltage ($E_a$). 
Therefore, if these parameters are given and held constant, the total deflection $D$ is directly, linearly proportional to the applied deflecting voltage $E_d$. 
$D \propto E_d$
This mathematically justifies the statement.

Ans related location pg number in ak slide: 121 (Electrostatic deflection diagram).

***

### 79. Page 5, Q.5 (c): Describe the operation of a time base generator circuit for CRO.

**Answer:**
**Function of a Time Base Generator:**
In order for a Cathode Ray Oscilloscope (CRO) to display a signal's amplitude plotted against time, the electron beam must be swept horizontally across the screen at a constant, known velocity. The Time Base Generator (also called a Sweep Generator) is the internal circuit responsible for creating the specific voltage waveform required to produce this linear horizontal motion.

**Operation:**
1.  **Required Waveform:** To move the spot steadily from the left side of the screen to the right, a voltage that increases linearly with time must be applied to the horizontal deflection plates. Once the spot reaches the far right, the voltage must abruptly drop back to its starting value to snap the spot instantly back to the left side to begin the next sweep. This creates a **sawtooth waveform** (or ramp waveform).
2.  **Basic Circuit (Ramp Generation):** The fundamental component of a time base generator is usually a capacitor charging through a resistor (or more accurately, a constant current source) from a DC supply. If charged by a constant current, the voltage across the capacitor rises perfectly linearly over time ($V_c = \frac{1}{C} \int I dt$). This rising voltage is amplified and applied to the horizontal plates, causing the "sweep" or "trace" period where the signal is drawn on the screen.
3.  **Discharge (Flyback):** When the capacitor voltage reaches a predetermined threshold corresponding to the right edge of the screen, an electronic switch (like a specialized transistor, UJT, or thyristor) is instantly triggered. This switch acts as a short circuit across the capacitor, causing it to discharge almost instantly. This rapid voltage drop is applied to the horizontal plates, yanking the electron beam rapidly back to the left side of the screen. This brief period is called the "flyback" or "retrace" period. During flyback, the beam is usually "blanked" (turned off) so the rapid retrace line doesn't clutter the display.
4.  **Synchronization:** For a stable, stationary image of a repeating AC signal, the start of the time base sweep must be perfectly synchronized with the input signal being measured. A trigger circuit monitors the incoming vertical signal. When the signal crosses a specific voltage threshold, it sends a pulse to the time base generator, telling it to start charging the capacitor exactly at that moment. This ensures every sweep starts at the exact same point on the waveform, painting a steady picture.
5.  **Control:** The user can control the rate at which the capacitor charges (by switching in different values of $R$ or $C$). This changes the slope of the ramp, which changes the speed of the horizontal sweep. This is the "Time/Div" control on the front panel of the CRO.

Ans related location pg number in ak slide: Not explicitly detailed in slides (general CRO internal knowledge).

***

### 80. Page 6, Q.7 (c): What is Lissajous pattern? Write short notes on clamp-on ammeter.

**Answer:**
**What is a Lissajous pattern?**
A Lissajous pattern is a complex, closed-curve figure displayed on the screen of a Cathode Ray Oscilloscope (CRO). It is generated when two continuous sinusoidal voltages are applied simultaneously to the two sets of deflection plates—one signal driving the beam horizontally (X-axis) and the other driving it vertically (Y-axis). The exact shape of the resulting pattern (which can range from straight lines and circles to intricate interconnected loops) is uniquely determined by three factors:
1.  The ratio of the frequencies of the two signals ($f_y / f_x$).
2.  The phase angle difference ($\phi$) between the two signals.
3.  The ratio of their amplitudes.
Lissajous patterns are highly useful tools for accurately determining an unknown frequency by comparing it against a known standard frequency, or for precisely measuring the phase shift between two signals of the same frequency.

**Short note on clamp-on ammeter:**
*(This is identical to Q28).*
A clamp-on ammeter (or clamp meter) is a versatile electrical test instrument primarily used for measuring AC current flowing through a live conductor without requiring the circuit to be physically broken or disconnected. It features a pair of hinged, spring-loaded magnetic jaws that open and close around the wire being tested. 
**Operation:** It operates on the principle of a current transformer. When clamped around an AC-carrying conductor, that conductor acts as a single-turn primary winding. The fluctuating magnetic field surrounding the conductor is captured by the iron core of the jaws and induces a proportionately smaller alternating current in a secondary coil wound inside the meter. This smaller secondary current is then measured, scaled according to the transformer ratio, and displayed as the main current value. While traditionally for AC, modern clamp meters utilizing Hall Effect sensors within the gap of the jaws can also measure DC magnetic fields, allowing for non-contact DC current measurement.

Ans related location pg number in ak slide: 122-125 (Lissajous patterns). Clamp-on ammeter is generic knowledge requested in the prompt list.

### 81. Page 7, Q.6 (b): Prove that the path of an electron traveling through an electric field with constant intensity is nonlinear.

**Answer:**
Let's analyze the trajectory of an electron as it passes between two parallel deflecting plates in a Cathode Ray Tube (CRT). 

Let:
*   $e$ = charge of an electron
*   $m$ = mass of an electron
*   $v_{ox}$ = constant horizontal velocity of the electron as it enters the field
*   $E_d$ = potential difference applied across the plates
*   $d$ = distance between the plates
*   $E$ = electric field intensity between the plates ($E = E_d / d$)

**Proof:**
1.  **Initial State:** The electron enters the field at the origin $(0,0)$ with a purely horizontal velocity $v_{ox}$. Therefore, the initial vertical velocity is $v_{oy} = 0$.
2.  **Horizontal Motion:** Because the electric field is strictly vertical, no horizontal forces act on the electron. According to Newton's first law, the horizontal velocity $v_{ox}$ remains constant.
    The horizontal distance $x$ traveled at any time $t$ is:
    $x = v_{ox} \cdot t$  =>  $t = \frac{x}{v_{ox}}$  --- (Equation 1)
3.  **Vertical Motion:** The constant vertical electric field $E$ exerts a constant vertical force $F_y = eE$ on the electron. This causes a constant vertical acceleration $a_y$:
    $a_y = \frac{F_y}{m} = \frac{eE}{m}$
    Using the kinematic equation for displacement ($s = ut + \frac{1}{2}at^2$) with initial vertical velocity $u = 0$, the vertical distance $y$ traveled at time $t$ is:
    $y = \frac{1}{2} a_y t^2 = \frac{1}{2} \left( \frac{eE}{m} \right) t^2$ --- (Equation 2)
4.  **Trajectory Equation:** To find the path equation (y as a function of x), we substitute the expression for $t$ from Equation 1 into Equation 2:
    $y = \frac{1}{2} \left( \frac{eE}{m} \right) \left( \frac{x}{v_{ox}} \right)^2$
    $y = \left( \frac{eE}{2 m v_{ox}^2} \right) x^2$

**Conclusion:**
In the final equation, the term in parentheses $\left( \frac{eE}{2 m v_{ox}^2} \right)$ is entirely composed of constants (for a given setup). Let this constant be $k$.
The equation simplifies to:
**$y = k x^2$**

This is the standard mathematical equation for a parabola. A parabola is a non-linear curve. Therefore, we have proven mathematically that the path of an electron traveling through a constant, uniform electric field is parabolic and non-linear.

Ans related location pg number in ak slide: 121 (The diagram shows the parabolic path).

***

### 82. Page 7, Q.7 (a): Derive an expression for vertical deflection of an electron beam in a CRT.

**Answer:**
*(This derivation is fundamentally identical to Q78. I will reproduce the standard derivation).*

Let:
*   $v_{ox}$ = axial (horizontal) velocity of the electron entering plates
*   $E_a$ = accelerating voltage in the electron gun
*   $E_d$ = deflecting voltage across the Y-plates
*   $d$ = distance between the Y-plates
*   $l_d$ = length of the Y-plates
*   $L$ = distance from the center of the Y-plates to the screen
*   $e$ = charge of an electron
*   $m$ = mass of an electron
*   $D$ = total vertical deflection on the screen

**Derivation:**
1.  **Velocity of Electron:** The kinetic energy gained from the accelerating anode is $\frac{1}{2}mv_{ox}^2 = eE_a$. Therefore, $v_{ox}^2 = \frac{2eE_a}{m}$.
2.  **Force and Acceleration:** The uniform electric field between the plates is $E = \frac{E_d}{d}$. This exerts a vertical force $F_y = eE = \frac{eE_d}{d}$. The vertical acceleration is $a_y = \frac{F_y}{m} = \frac{eE_d}{md}$.
3.  **Time in Field:** The electron travels horizontally through the plates at constant speed $v_{ox}$. The time spent between the plates is $t = \frac{l_d}{v_{ox}}$.
4.  **Deflection Velocity:** The vertical velocity $v_y$ acquired just as the electron exits the plates is $v_y = a_y t = \left(\frac{eE_d}{md}\right) \left(\frac{l_d}{v_{ox}}\right)$.
5.  **Deflection Angle:** The angle $\theta$ at which the electron exits the plates is given by $\tan \theta = \frac{v_y}{v_{ox}}$.
    Substituting $v_y$:
    $\tan \theta = \frac{eE_d l_d}{m d v_{ox}^2}$
6.  **Screen Deflection Geometry:** If you trace the exit trajectory backwards, it appears to originate exactly from the center of the deflecting plates. This forms a large right triangle to the screen, where the adjacent side is $L$ and the opposite side is the total deflection $D$.
    Therefore, $\tan \theta = \frac{D}{L}$.
7.  **Final Expression:** Equate the two expressions for $\tan \theta$:
    $\frac{D}{L} = \frac{e E_d l_d}{m d v_{ox}^2}$
    $D = \frac{L l_d e E_d}{m d v_{ox}^2}$
    Substitute $v_{ox}^2 = \frac{2eE_a}{m}$ into the denominator:
    $D = \frac{L l_d e E_d}{m d \left( \frac{2eE_a}{m} \right)}$
    $D = \frac{L l_d e E_d}{2 d e E_a}$
    **$D = \frac{L \cdot l_d \cdot E_d}{2 \cdot d \cdot E_a}$**

This is the final expression for the vertical deflection $D$ on the CRT screen.

Ans related location pg number in ak slide: 121.

***

### 83. Page 10, Q.6 (c): An electrically deflected CRT has a final anode voltage of 2000 V and parallel deflecting plates 1.5 cm long and 5 mm apart. If the screen is 50 cm from the centre of deflecting plates, find (i) beam speed, (ii) the deflection sensitivity of the tube and (iii) the deflection factor of the tube.

**Answer:**
**Given Data:**
*   Accelerating voltage (anode voltage), $E_a = 2000 \text{ V}$
*   Length of deflecting plates, $l_d = 1.5 \text{ cm} = 0.015 \text{ m}$
*   Distance between plates, $d = 5 \text{ mm} = 0.005 \text{ m}$
*   Distance from center of plates to screen, $L = 50 \text{ cm} = 0.5 \text{ m}$
*   Charge of an electron, $e \approx 1.6 \times 10^{-19} \text{ C}$
*   Mass of an electron, $m \approx 9.1 \times 10^{-31} \text{ kg}$

**(i) Beam Speed ($v_{ox}$):**
The kinetic energy $\frac{1}{2}mv_{ox}^2 = eE_a$.
$v_{ox} = \sqrt{\frac{2eE_a}{m}}$
$v_{ox} = \sqrt{\frac{2 \times (1.6 \times 10^{-19}) \times 2000}{9.1 \times 10^{-31}}}$
$v_{ox} = \sqrt{\frac{6.4 \times 10^{-16}}{9.1 \times 10^{-31}}}$
$v_{ox} = \sqrt{0.703 \times 10^{15}}$
$v_{ox} = \sqrt{7.03 \times 10^{14}}$
**$v_{ox} \approx 2.65 \times 10^7 \text{ m/s}$**

**(ii) Deflection Sensitivity ($S$):**
Deflection sensitivity is defined as the physical deflection on the screen per unit of deflecting voltage ($D / E_d$).
From the deflection formula $D = \frac{L l_d E_d}{2 d E_a}$:
$S = \frac{D}{E_d} = \frac{L \cdot l_d}{2 \cdot d \cdot E_a}$
$S = \frac{0.5 \times 0.015}{2 \times 0.005 \times 2000}$
$S = \frac{0.0075}{20}$
$S = 0.000375 \text{ m/V}$
To convert to more standard units (mm/V):
$S = 0.000375 \times 1000 \text{ mm/V}$
**$S = 0.375 \text{ mm/V}$**

**(iii) Deflection Factor ($G$):**
Deflection factor is the reciprocal of deflection sensitivity. It indicates how many volts are required to produce a unit of deflection ($E_d / D$).
$G = \frac{1}{S}$
$G = \frac{1}{0.375 \text{ mm/V}}$
**$G \approx 2.667 \text{ V/mm}$**

Ans related location pg number in ak slide: 121 (Based on the geometry shown).

***

### 84. Page 10, Q.7 (b): What is Lissajous pattern? Describe how the frequency can be measured with the use of a CRO.

**Answer:**
**What is a Lissajous pattern?**
*(This is identical to Q80).*
A Lissajous pattern is a stationary or slowly moving curve displayed on a CRO screen, created by applying two sinusoidal AC voltages simultaneously to the horizontal (X) and vertical (Y) deflection plates. The resulting shape (which could be a line, circle, ellipse, or complex figure-8 shape) is determined entirely by the ratio of the frequencies of the two signals, their relative phase difference, and their relative amplitudes. It is a powerful visual tool for analyzing the relationship between two signals.

**How frequency can be measured using Lissajous patterns:**
To measure an unknown frequency ($f_y$) using a CRO, you use a Lissajous pattern to compare it against a known, highly accurate standard frequency ($f_x$).
1.  **Setup:** 
    *   Connect the signal with the **unknown frequency** to the **Vertical (Y-axis)** input of the CRO.
    *   Connect a signal generator producing a **known, adjustable frequency** to the **Horizontal (X-axis)** input.
    *   Set the CRO's internal time base (sweep generator) to the 'OFF' or 'X-Y' mode, so the horizontal movement is driven entirely by the external signal generator.
2.  **Tuning:** Turn on both signals. Adjust the frequency dial on the known signal generator ($f_x$) until a stable, stationary pattern appears on the screen. A stationary pattern only forms when the ratio of the two frequencies is an exact rational fraction (e.g., 1:1, 1:2, 3:2).
3.  **Calculation Method:** Once the pattern is perfectly stationary, draw imaginary horizontal and vertical tangent lines enclosing the pattern.
    *   Count the number of times the pattern intersects the top horizontal tangent line. Let this be $n_h$ (number of horizontal tangencies or loops).
    *   Count the number of times the pattern intersects the side vertical tangent line. Let this be $n_v$ (number of vertical tangencies or loops).
4.  **The Formula:** The fundamental relationship governing Lissajous figures is:
    $\frac{\text{Unknown Frequency } (f_y)}{\text{Known Frequency } (f_x)} = \frac{\text{Number of horizontal tangencies } (n_h)}{\text{Number of vertical tangencies } (n_v)}$
5.  **Example:** If the pattern looks like a figure-8 lying on its side. It touches the top horizontal line twice ($n_h=2$) and the vertical side line once ($n_v=1$). If your known frequency is set to 1000 Hz:
    $\frac{f_y}{1000} = \frac{2}{1} \implies f_y = 2000 \text{ Hz}$.

Ans related location pg number in ak slide: 122-125.
### 85. Page 12, Q.6 (a): What is CRO? Draw the block diagram of a CRO and explain the functions of the each block.

**Answer:**
**What is CRO?**
A Cathode Ray Oscilloscope (CRO) is a highly versatile, fast-responding electronic measuring instrument used primarily to visualize, measure, and analyze the waveforms of electrical signals over time. It essentially acts as an extremely fast X-Y plotter, where the incoming signal's amplitude is typically plotted on the vertical (Y) axis against time on the horizontal (X) axis. It allows engineers to "see" voltage changes that happen in fractions of a microsecond.

**Block Diagram of a CRO:**
*(Note: I will describe the standard block diagram required for this question).*
1.  **Vertical (Y) Input & Attenuator:** The signal to be measured enters here. The attenuator is a voltage divider that scales down high-voltage signals so they don't overload the internal amplifiers or drive the beam off-screen.
2.  **Vertical Amplifier:** A wide-band, high-gain amplifier. It boosts the weak, attenuated input signal to a voltage level high enough to drive the vertical deflection plates of the CRT. It often contains a delay line to give the horizontal sweep circuit time to start before the vertical signal hits the plates.
3.  **Trigger Circuit:** This circuit samples a tiny portion of the vertical input signal. It generates a sharp trigger pulse when the input signal crosses a specific, user-defined voltage threshold (trigger level). This ensures the horizontal sweep always starts at exactly the same point on the waveform, creating a stable, stationary image on the screen.
4.  **Time Base Generator (Sweep Generator):** Triggered by the pulse from the Trigger Circuit, it generates a perfectly linear sawtooth (ramp) voltage waveform. 
5.  **Horizontal Amplifier:** Amplifies the sawtooth voltage from the Time Base Generator (or an external X-input signal) to a level sufficient to drive the horizontal deflection plates.
6.  **Cathode Ray Tube (CRT):** The heart of the instrument. 
    *   *Electron Gun:* Heats a cathode to boil off electrons, then focuses and accelerates them into a tight, high-speed beam.
    *   *Deflection Plates:* Two sets of parallel plates (Vertical and Horizontal). The amplified voltages applied here create electric fields that bend the electron beam up/down and left/right.
    *   *Fluorescent Screen:* Coated with phosphor. When the high-speed electrons strike it, their kinetic energy is converted into visible light, creating the glowing trace we see.
7.  **Power Supply:** Consists of two parts. A Low Voltage supply powers the amplifiers, trigger, and sweep circuits. A High Voltage (HV) supply (often several thousand volts) is applied to the accelerating anodes in the CRT to give the electron beam its necessary speed and brightness.

Ans related location pg number in ak slide: 119 (Basic definition and CRT parts).

***

### 86. Page 12, Q.6 (b): Differentiate between the digital and conventional CRO. Prove that the path of an electron traveling through an electric field with constant intensity in nonlinear.

**Answer:**
**Differentiate between the digital and conventional CRO:**
| Feature | Conventional (Analog) CRO | Digital Storage Oscilloscope (DSO) |
| :--- | :--- | :--- |
| **Basic Operation** | Applies the amplified input voltage directly to the CRT deflection plates. The trace is "real-time." | Samples the analog input, converts it to digital data (ADC), stores it in memory, and then mathematically reconstructs the wave on a display. |
| **Storage Capability** | Cannot store waveforms. Relies on the persistence of the phosphor screen to view fast transient events. | Can store waveforms in digital memory indefinitely. Allows for viewing pre-trigger data and single-shot events perfectly. |
| **Display Type** | Uses a traditional Cathode Ray Tube (CRT) with a phosphor screen. | Uses modern digital displays like LCD, LED, or TFT screens. |
| **Measurement & Math** | Measurements are taken manually by visually counting graticule divisions on the screen. | Microprocessors automatically calculate and display Vpp, Frequency, RMS, Rise time, and can perform FFTs (Fourier Transforms). |
| **Bandwidth/Speed** | Limited primarily by the physical bandwidth of the vertical amplifier and CRT deflection sensitivity. | Limited by the sample rate of the Analog-to-Digital Converter (ADC) and microprocessor speed. |
| **Cost & Size** | Generally bulky, heavy, and less expensive (historically). | Compact, lightweight, highly featured, and generally more expensive. |

**Prove that the path of an electron traveling through an electric field with constant intensity is nonlinear:**
*(This is identical to Q81. I will provide the proof again for completeness).*
Let an electron (charge $e$, mass $m$) enter a uniform vertical electric field ($E$) with a constant horizontal velocity ($v_{ox}$).
1.  **Horizontal Motion:** There is no horizontal force. Horizontal velocity is constant.
    Distance $x = v_{ox} t \implies t = \frac{x}{v_{ox}}$
2.  **Vertical Motion:** The constant electric field exerts a constant vertical force $F_y = eE$. 
    Vertical acceleration is $a_y = \frac{eE}{m}$.
    Starting with zero initial vertical velocity, the vertical distance $y$ after time $t$ is:
    $y = \frac{1}{2} a_y t^2 = \frac{1}{2} \left( \frac{eE}{m} \right) t^2$
3.  **Path Equation:** Substitute $t = \frac{x}{v_{ox}}$ into the $y$ equation:
    $y = \frac{1}{2} \left( \frac{eE}{m} \right) \left( \frac{x}{v_{ox}} \right)^2$
    **$y = \left( \frac{eE}{2 m v_{ox}^2} \right) x^2$**
    Since $\left( \frac{eE}{2 m v_{ox}^2} \right)$ is a constant ($k$), the equation is $y = k x^2$. This is the standard equation of a parabola, which is definitively a non-linear curve.

Ans related location pg number in ak slide: 119 (CRO definition), 121 (Path of electron). Digital vs Analog is general knowledge implied by the syllabus context.

***

### 87. Page 12, Q.6 (c): What is Lissajous pattern? Write short note on clam-on ammeter. *(Note: transcribed exactly as written)*

**Answer:**
*(This is identical to Q80 and Q84. I will provide a concise version).*

**What is a Lissajous pattern?**
A Lissajous pattern is a stationary or dynamic complex geometric figure displayed on the screen of an oscilloscope. It is generated exclusively in the "X-Y mode" of the CRO, where the internal time base is disabled. Instead, one continuous AC signal is fed directly to the horizontal (X) deflection plates, and a second continuous AC signal is fed simultaneously to the vertical (Y) deflection plates. The resulting shape of the trace (which can be a straight line, ellipse, circle, or complex loops) is mathematically dictated by three parameters: the ratio of the frequencies of the two signals, their relative phase shift, and their relative peak amplitudes. By analyzing the shape, one can accurately deduce an unknown frequency or measure phase angles.

**Short note on clamp-on ammeter:**
A clamp-on ammeter (or clamp meter) is a non-invasive electrical testing instrument used to measure current. Its defining physical feature is a pair of spring-loaded, hinged jaws that can open and close around a live electrical wire. 
It operates fundamentally on the principle of a current transformer. When clamped around an AC-carrying conductor, that conductor acts as a single-turn primary coil. The alternating magnetic field surrounding the conductor is concentrated by the iron core of the jaws. This induces a small, proportional alternating current in a secondary coil wound inside the meter body. This secondary current is rectified, measured, and displayed as the actual current flowing in the main wire. The primary advantage is safety and convenience; it allows for high-current measurement without needing to cut the wire, shut off power, or insert a traditional ammeter in series.

Ans related location pg number in ak slide: 122-125 (Lissajous). Clamp-on ammeter is generic.

***

### 88. Page 20, Q.5 a) [Lower section]: Draw the internal structure of a CRT and explain the functions of each block.

**Answer:**
**Internal Structure of a CRT [Reference slide 120]:**
A Cathode Ray Tube is an evacuated glass envelope shaped like a funnel, containing the following main components from narrow neck to wide face:
1.  **Electron Gun Assembly:**
    *   **Heater & Cathode:** A filament heats the cathode cylinder, causing it to emit a cloud of electrons via thermionic emission.
    *   **Control Grid:** A metallic cylinder with a tiny hole, placed over the cathode. It is kept at a negative potential relative to the cathode. By varying this negative voltage, it repels electrons, controlling how many pass through the hole. This controls the intensity (brightness) of the beam on the screen.
    *   **Accelerating & Focusing Anodes:** A series of cylindrical anodes (Pre-accelerating, Focusing, Accelerating) maintained at very high positive potentials (thousands of volts). They act as electrostatic lenses. They aggressively pull the electrons forward, accelerating them to immense speeds, and simultaneously force the diverging cloud into a tight, sharp, focused beam.
2.  **Deflection Plate Assembly:**
    *   **Vertical Deflection Plates (Y-plates):** Two horizontal metal plates. A voltage applied here creates a vertical electric field, bending the electron beam up or down.
    *   **Horizontal Deflection Plates (X-plates):** Two vertical metal plates located just after the Y-plates. A voltage applied here bends the beam left or right.
3.  **Fluorescent Screen:**
    The inside of the wide, flat end of the glass tube is coated with a phosphor material. When the high-speed electron beam strikes this coating, the kinetic energy of the electrons is converted into visible light (fluorescence), creating the glowing spot we see.
4.  **Aquadag Coating:**
    A conductive graphite coating on the inside of the funnel-shaped part of the glass tube. It is connected to the final high-voltage anode. Its primary function is to collect the secondary electrons that bounce off the phosphor screen when the main beam hits it, preventing a negative charge buildup on the screen that would repel the incoming beam.

Ans related location pg number in ak slide: 120.


### 89. Page 20, Q.5 c) [Lower section]: A CRT has an anode voltage of 2000V and parallel deflecting plates 2cm long and 5mm apart. The screen is 30cm from the centre of the plates. Find the input voltage required to deflect beam through 3cm. The input voltage is applied to the deflecting plates through amplifiers having an overall gain of 100.

**Answer:**
**Given Data:**
*   Accelerating anode voltage, $E_a = 2000 \text{ V}$
*   Length of deflecting plates, $l_d = 2 \text{ cm} = 0.02 \text{ m}$
*   Distance between plates, $d = 5 \text{ mm} = 0.005 \text{ m}$
*   Distance from plate center to screen, $L = 30 \text{ cm} = 0.3 \text{ m}$
*   Desired total deflection on screen, $D = 3 \text{ cm} = 0.03 \text{ m}$
*   Overall amplifier gain, $A_v = 100$

**Goal:** Find the input voltage ($V_{in}$) to the amplifier.

**Step 1: Calculate the required Deflecting Voltage ($E_d$) across the plates.**
We use the standard electrostatic deflection formula for a CRT:
$D = \frac{L \cdot l_d \cdot E_d}{2 \cdot d \cdot E_a}$

We need to solve for $E_d$:
$E_d = \frac{D \cdot 2 \cdot d \cdot E_a}{L \cdot l_d}$

Substitute the given values into the rearranged formula:
$E_d = \frac{0.03 \times 2 \times 0.005 \times 2000}{0.3 \times 0.02}$
$E_d = \frac{0.06 \times 10}{0.006}$
$E_d = \frac{0.6}{0.006}$
**$E_d = 100 \text{ V}$**

This means 100 Volts must be applied directly across the physical deflecting plates to bend the beam 3 cm on the screen.

**Step 2: Calculate the required Input Voltage ($V_{in}$).**
The problem states that this deflecting voltage ($E_d$) is provided by an amplifier with a gain of 100. The amplifier takes a small input voltage ($V_{in}$) and multiplies it by the gain to produce the output deflecting voltage ($E_d$).
Gain ($A_v$) = $\frac{\text{Output Voltage}}{\text{Input Voltage}} = \frac{E_d}{V_{in}}$

Therefore:
$V_{in} = \frac{E_d}{A_v}$
$V_{in} = \frac{100 \text{ V}}{100}$
**$V_{in} = 1 \text{ V}$**

The input voltage required to deflect the beam through 3 cm is **1 Volt**.

Ans related location pg number in ak slide: 121 (Deflection formula).

***

### 90. Page 21, Q.7 (b) [First block]: What is CRO? Draw the internal structure of a CRT and explain the functions of the each block.

**Answer:**
*(This question is a combination of exactly what was answered in Q85 and Q88. I will provide a synthesized response).*

**What is CRO?**
A Cathode Ray Oscilloscope (CRO) is a fast-responding electronic testing instrument that visually displays electrical signals. It acts essentially as a high-speed graph plotter, most commonly displaying signal voltage amplitude (on the Y-axis) against time (on the X-axis). It allows engineers to observe waveform shapes, measure frequencies, phase angles, and peak-to-peak voltages of fast-changing AC or pulsed DC signals.

**Internal Structure of a CRT and Block Functions:**
The Cathode Ray Tube (CRT) is the central display component of the CRO. It is a vacuum glass tube.
*(Refer to diagram on slide 120)*
1.  **Electron Gun:** This assembly generates, controls, and focuses the electron beam.
    *   **Heater & Cathode:** A heated filament warms the cathode, causing it to emit electrons via thermionic emission.
    *   **Control Grid:** A negatively biased cylinder with a small aperture. It controls the number of electrons passing through (beam current), thereby controlling the **intensity (brightness)** of the spot on the screen.
    *   **Focusing & Accelerating Anodes:** These are cylindrical metal electrodes kept at highly positive voltages. They act as electrostatic lenses. They aggressively accelerate the electrons towards the screen and simultaneously pinch the diverging electron cloud into a tightly **focused, sharp beam**.
2.  **Deflection Plates:** Once the beam is formed, it passes through two pairs of parallel plates.
    *   **Vertical (Y) Deflection Plates:** Mounted horizontally. When a voltage is applied, they create a vertical electric field that moves the electron beam up or down. The signal you are trying to measure is applied here (after amplification).
    *   **Horizontal (X) Deflection Plates:** Mounted vertically. A voltage applied here moves the beam left or right. The internal time-base (sweep) generator's sawtooth wave is usually applied here to move the beam steadily across the screen to create the time axis.
3.  **Fluorescent Screen:** The inside face of the tube is coated with phosphor. The immense kinetic energy of the high-speed electrons striking this coating excites the phosphor atoms, causing them to emit visible light, creating the visible trace.
4.  **Aquadag:** A conductive graphite layer inside the glass envelope, connected to the highest positive voltage. It collects the secondary electrons that are knocked off the screen when the main beam hits it, preventing the screen from building up a negative charge that would eventually repel the beam.

Ans related location pg number in ak slide: 119, 120.

***

### 91. Page 21, Q.7 (c) [First block]: What is Lissajous pattern? How Lissajous patterns can be used for accurate measurement of frequency? -Explain.

**Answer:**
*(This is functionally identical to Q84. I will provide a slightly differently phrased explanation).*

**What is a Lissajous pattern?**
A Lissajous pattern is a stationary or dynamic geometric shape produced on an oscilloscope screen when two different sinusoidal voltage signals are applied simultaneously to the vertical (Y) and horizontal (X) deflection plates, while the internal time-base sweep is disabled. The exact geometry of the resulting pattern—ranging from diagonal lines and circles to complex multi-looped shapes—depends entirely on the mathematical ratio between the frequencies of the two signals, their relative phase angle, and their relative amplitudes.

**How to use Lissajous patterns for accurate measurement of frequency:**
1.  **The Setup:** 
    *   Connect the signal with the **Unknown Frequency ($f_y$)** to the Vertical (CH1 or Y) input of the CRO.
    *   Connect a highly accurate Signal Generator producing a **Known Frequency ($f_x$)** to the Horizontal (CH2 or X) input.
    *   Switch the CRO to "X-Y mode" to allow the external signal generator to drive the horizontal axis instead of the internal time base.
2.  **Generating the Pattern:** Turn on both signals. Initially, the pattern on the screen will likely be a rapidly moving, jumbled blur. 
3.  **Tuning for Stability:** Carefully tune the frequency dial of the Known Signal Generator ($f_x$). As $f_x$ approaches a harmonic relationship with $f_y$ (like 1:1, 1:2, 2:3, etc.), the pattern will slow down. When the ratio of $f_y / f_x$ is an exact rational fraction, the pattern will become perfectly stationary and stable.
4.  **Analyzing the Pattern:** Once a stable pattern is achieved, imagine a box tightly enclosing the pattern.
    *   Count the maximum number of times the curve touches the top horizontal edge of the imaginary box. This is the number of **horizontal tangencies ($N_h$)**.
    *   Count the maximum number of times the curve touches the side vertical edge of the imaginary box. This is the number of **vertical tangencies ($N_v$)**.
5.  **The Calculation:** The frequencies and the tangencies relate according to this fundamental formula:
    $\frac{\text{Unknown Frequency } (f_y)}{\text{Known Frequency } (f_x)} = \frac{\text{Number of Horizontal Tangencies } (N_h)}{\text{Number of Vertical Tangencies } (N_v)}$
    By simply rearranging the formula:
    **$f_y = f_x \times \left( \frac{N_h}{N_v} \right)$**
    Because the known frequency generator can be highly precise, and counting tangencies is unambiguous, this method provides an extremely accurate measurement of the unknown frequency.

Ans related location pg number in ak slide: 122-125.

***

### 92. Page 36, CT#04 SEC: A Q1: Sketch the Lissajous patterns of sinusoidal signals with the relationships $\omega_1 = \omega_2$, $\phi = \pi/4$ and $\phi = \pi/2$.

**Answer:**
The problem asks for sketches of Lissajous patterns where the frequencies are exactly equal ($\omega_1 = \omega_2$, meaning the frequency ratio is 1:1), but with two different phase shifts ($\phi$).
Let the horizontal signal be $X = A \sin(\omega t)$.
Let the vertical signal be $Y = B \sin(\omega t + \phi)$.

**(a) Sketch for $\phi = \pi/4$ (or $45^\circ$):**
*   **Mathematical behavior:** The Y signal leads the X signal by $45^\circ$. 
    *   At $\omega t = 0$, $X=0$, but $Y = B \sin(45^\circ) = 0.707 B$. The spot is on the positive Y-axis.
    *   At $\omega t = 45^\circ$, $X = 0.707 A$, $Y = B \sin(90^\circ) = B$. The spot is at its highest point.
    *   At $\omega t = 90^\circ$, $X = A$, $Y = B \sin(135^\circ) = 0.707 B$. The spot is at its furthest right point.
*   **The Sketch:** The resulting pattern is an **ellipse**. Because the phase shift is positive $45^\circ$ (between $0^\circ$ and $90^\circ$), the major axis of the ellipse lies in the first and third quadrants (bottom-left to top-right diagonal).
    *   *Imagine drawing an oval tilted at a $45^\circ$ angle.*

**(b) Sketch for $\phi = \pi/2$ (or $90^\circ$):**
*   **Mathematical behavior:** The Y signal leads the X signal by $90^\circ$. 
    *   $X = A \sin(\omega t)$
    *   $Y = B \sin(\omega t + 90^\circ) = B \cos(\omega t)$
    *   If we square both and divide by their amplitudes: $(X/A)^2 + (Y/B)^2 = \sin^2(\omega t) + \cos^2(\omega t) = 1$. This is the standard equation for an ellipse aligned with the axes. 
    *   If the amplitudes are equal ($A = B$), this simplifies to $X^2 + Y^2 = A^2$, which is the equation of a circle.
*   **The Sketch:** Assuming equal amplitudes for simplicity, the resulting pattern is a perfect **circle** centered on the origin. If amplitudes are unequal, it is an ellipse whose major and minor axes fall perfectly on the X and Y coordinate axes.
    *   *Imagine drawing a perfect circle centered on the crosshairs.*

Ans related location pg number in ak slide: 123 (Shows 90 degrees), 124 (Shows a general phase shift ellipse which applies to 45 degrees).


### 93. Page 36, CT#04 SEC: A Q2: Prove that the path of an electron travelling through an electric field with constant intensity is parabolic.

**Answer:**
*(This is functionally identical to Q81 and Q86. I will provide the proof again).*

Let an electron (charge $e$, mass $m$) enter a region between two parallel deflection plates of a CRT.
*   The electric field $E$ between the plates is uniform and constant in the vertical (Y) direction.
*   The electron enters horizontally (along the X-axis) with a constant initial velocity $v_{ox}$.

**1. Equation of Motion in the X-direction (Horizontal):**
Since the electric field acts entirely in the vertical direction, there is zero force acting on the electron in the horizontal direction.
Therefore, horizontal acceleration $a_x = 0$.
According to Newton's first law, the horizontal velocity remains constant: $v_x = v_{ox}$.
The horizontal distance $x$ traveled in time $t$ is:
$x = v_{ox} \cdot t$
Rearranging for time $t$:
**$t = \frac{x}{v_{ox}}$**  --- (Equation 1)

**2. Equation of Motion in the Y-direction (Vertical):**
The constant vertical electric field $E$ exerts a constant vertical force on the electron:
$F_y = e \cdot E$
This force causes a constant vertical acceleration $a_y$ according to Newton's second law ($F = ma$):
$a_y = \frac{F_y}{m} = \frac{e \cdot E}{m}$
The initial vertical velocity is zero ($u_y = 0$).
Using the kinematic equation for displacement ($s = ut + \frac{1}{2}at^2$), the vertical distance $y$ traveled in time $t$ is:
$y = 0 \cdot t + \frac{1}{2} a_y t^2$
**$y = \frac{1}{2} \left( \frac{e \cdot E}{m} \right) t^2$** --- (Equation 2)

**3. Deriving the Path Equation:**
To find the equation of the trajectory (the path), we need $y$ as a function of $x$. We do this by substituting the expression for $t$ from Equation 1 into Equation 2:
$y = \frac{1}{2} \left( \frac{e \cdot E}{m} \right) \left( \frac{x}{v_{ox}} \right)^2$
$y = \left( \frac{e \cdot E}{2 \cdot m \cdot v_{ox}^2} \right) \cdot x^2$

**4. Conclusion:**
For a given CRT geometry and operating voltage, the terms $e, E, m,$ and $v_{ox}$ are all constants. 
Let $k = \left( \frac{e \cdot E}{2 \cdot m \cdot v_{ox}^2} \right)$.
The path equation simplifies to:
**$y = k \cdot x^2$**
This is the standard mathematical equation for a parabola. Thus, we have proven that the path of the electron through the constant electric field is parabolic.

Ans related location pg number in ak slide: 121 (The diagram visually shows this parabolic curve).

***

### 94. Page 5, Q.7 (b): Discuss the factors that decide whether to choose a digital instrument or analog one. Also, list the advantages of digital instruments over the analog one.

**Answer:**
**Factors deciding the choice between Digital and Analog instruments:**
1.  **Resolution & Precision Requirements:** Digital instruments offer far higher resolution (e.g., 4.5 or 5.5 digits), allowing for precise readings of minute changes. Analog meters are limited by the physical scale markings and the user's ability to interpolate between lines.
2.  **Nature of the Signal:** For rapidly fluctuating or continuously varying signals, an analog pointer is often easier for the human eye to track to perceive trends or instability (like tuning a circuit to a peak). Digital displays may just blur or update too quickly with unreadable numbers if the signal is unstable.
3.  **Viewing Environment:** Digital displays (especially backlit LCDs/LEDs) are far easier to read in low light or from a distance. Analog scales require good lighting and must be viewed straight-on to avoid parallax error.
4.  **Data Processing & Storage:** If the measurement data needs to be logged, stored in memory, sent to a computer, or mathematically processed (like calculating RMS or frequency), a digital instrument is mandatory. Analog meters simply indicate a value and require manual recording.
5.  **Cost and Durability:** Historically, basic analog meters were cheaper and didn't require internal batteries for voltage/current measurement. However, digital multimeters are now extremely cheap and physically more robust against drops, as they lack the delicate jewel bearings and moving coils of analog meters.

**Advantages of Digital Instruments over Analog ones:**
1.  **Higher Accuracy and Precision:** Digital processing minimizes internal circuit loading effects and component drift, leading to inherently more accurate readings.
2.  **Elimination of Human Reading Errors:** Digital displays present a clear, unambiguous number. They completely eliminate parallax error (reading the pointer from an angle) and interpolation errors (guessing the value between scale marks).
3.  **Higher Resolution:** They can display very small variations in the measured quantity (down to microvolts or microamps depending on the ADC).
4.  **Lower Power Consumption:** Modern digital instruments (especially those using LCDs) draw significantly less power from the circuit under test, minimizing loading effects compared to the power required to physically move a coil and pointer.
5.  **Multi-functionality and Processing:** They can easily auto-range, store maximum/minimum values, perform internal math, and interface directly with computer systems for automated data logging.

Ans related location pg number in ak slide: 105 (Lists Advantages and Disadvantages of Digital Instruments).

***

### 95. Page 6, Q.7 (b): What is DVM? Draw the block diagram and explain the working principle of a potentiometric type DVM.

**Answer:**
**What is a DVM?**
A Digital Voltmeter (DVM) is an electronic measuring instrument that converts an analog voltage input into a discrete digital representation and displays the value numerically on a digital readout (like an LED or LCD screen). It operates based on the principle of Analog-to-Digital Conversion (ADC) or quantization.

**Block Diagram of Potentiometric Type DVM:**
*(Refer to slide 109 for the diagram. Here is the description of the necessary blocks).*
*   **Unknown Voltage ($V_x$):** The input signal applied to the positive terminal of a Comparator.
*   **Reference Voltage Source:** A highly stable internal DC voltage supply.
*   **Sliding Contact / Potentiometer Adjustment Device:** A voltage divider across the Reference Source that outputs a variable **Feedback Voltage ($V_f$)**.
*   **Comparator:** An operational amplifier that compares $V_x$ against $V_f$. It outputs an **Error Signal**.
*   **Error Amplifier:** Amplifies the Error Signal to a level sufficient to drive the adjustment device.
*   **Adjustment Device (Motor/Logic):** Driven by the error amplifier, it mechanically or electronically moves the sliding contact on the potentiometer.
*   **Readout:** Digitally displays the position of the sliding contact.

**Working Principle:**
The Potentiometric DVM operates on a null-balance or voltage comparison technique.
1.  The unknown analog voltage ($V_x$) is applied to one input of the comparator.
2.  A known, highly stable internal reference voltage is applied across a precision potentiometer. The wiper of this potentiometer taps off a specific fraction of the reference voltage, creating a feedback voltage ($V_f$).
3.  This feedback voltage ($V_f$) is applied to the other input of the comparator.
4.  The comparator calculates the difference between the two voltages ($V_{error} = V_x - V_f$).
5.  This error signal is amplified. The amplified error signal drives an adjustment device (which could be a servomotor in older continuous-balance types, or solid-state switching logic in modern versions).
6.  The adjustment device automatically moves the sliding contact on the potentiometer in the direction that reduces the error. 
    *   If $V_x > V_f$, it moves the wiper to increase $V_f$.
    *   If $V_x < V_f$, it moves the wiper to decrease $V_f$.
7.  This process continues continuously until $V_f$ exactly equals $V_x$. At this exact moment, the error signal drops to zero, and the sliding contact stops moving. This is the "null" condition.
8.  Because the potentiometer is highly precise and calibrated, the physical (or electronic) position of the sliding contact perfectly represents the value of the unknown voltage. This position is then converted to a digital number and shown on the Readout.

Ans related location pg number in ak slide: 106, 109.

***

### 96. Page 7, Q.6 (a): What is DVM? Draw the block diagram, and explain the working principle of a ramp type DVM.

**Answer:**
**What is DVM?**
*(Identical to the previous answer).* A Digital Voltmeter (DVM) is an instrument that expresses the measurement of DC and AC voltages in discrete digital numerals rather than by the deflection of a pointer on a continuous analog scale.

**Block Diagram of Ramp Type DVM:**
*(Refer to slide 107 for the diagram. Here is the description).*
*   **Attenuator Circuit:** Scales the unknown input voltage ($V_{in}$) to a usable level.
*   **Ramp Generator:** Produces a perfectly linear, negatively sloping sawtooth voltage waveform starting from a positive value.
*   **Input Comparator (C1):** Compares the attenuated input voltage with the ramp voltage.
*   **Ground/Zero-Crossing Comparator (C2):** Compares the ramp voltage with zero volts (ground).
*   **Oscillator:** Generates a continuous train of high-frequency clock pulses.
*   **Gate:** A logic circuit (AND gate) that allows clock pulses to pass only when it is "open."
*   **Counter & Display:** Counts the pulses passed by the gate and displays the final count.
*   **Sample Rate Multivibrator:** Controls the timing of the entire measurement cycle, resetting the ramp and counter.

**Working Principle:**
The basic principle of the Ramp-type DVM is Voltage-to-Time conversion. It measures an unknown voltage by measuring the time it takes for a linear ramp voltage to fall from the level of the unknown voltage down to zero.
1.  **Initiation:** The Sample Rate Multivibrator initiates a measurement cycle. It resets the Counter to zero and triggers the Ramp Generator to start producing a linearly decreasing negative ramp voltage.
2.  **Start of Count:** The Input Comparator (C1) continuously compares the falling ramp voltage to the unknown DC input voltage. At the exact instant the falling ramp voltage equals the unknown input voltage, Comparator C1 generates a "Start" pulse. This pulse opens the Gate.
3.  **Counting:** While the Gate is open, high-frequency clock pulses from the Oscillator pass through and are tallied by the Counter.
4.  **End of Count:** The ramp voltage continues to fall linearly. The Zero-Crossing Comparator (C2) continuously compares the ramp voltage to 0V (ground). At the exact instant the ramp voltage crosses zero volts, Comparator C2 generates a "Stop" pulse. This pulse closes the Gate, stopping the flow of clock pulses to the Counter.
5.  **Result:** Because the slope of the ramp is perfectly linear and constant, the time interval ($\Delta t$) between the "Start" pulse and the "Stop" pulse is strictly, directly proportional to the magnitude of the unknown input voltage.
6.  Since the Oscillator produces pulses at a constant, known rate, the total number of pulses ($n$) counted during time $\Delta t$ is a direct digital representation of the unknown voltage. The display shows this count.

Ans related location pg number in ak slide: 106, 107, 108

### 97. Page 9, Q.3. (b): What is VTVM? Describe the operation of a diode type VTVM with suitable circuit diagram.

**Answer:**
**What is a VTVM?**
A Vacuum Tube Voltmeter (VTVM) is an electronic measuring instrument that uses vacuum tubes (or thermionic valves) in its internal circuitry to amplify the input signal before it is applied to a standard moving-coil (PMMC) meter. The primary advantage of a VTVM over a standard analog multimeter is its extremely high input impedance (often 10 Megohms or more). Because of this high impedance, it draws virtually zero current from the circuit under test, virtually eliminating the "loading effect" that can cause standard multimeters to read inaccurate, artificially low voltages in high-resistance circuits.

**Operation of an Average Diode Type VTVM:**
*(Note: Refer to the circuit diagram on slide 110).*

**Circuit Diagram Description:**
The basic circuit consists of:
*   An AC input supply terminal.
*   A vacuum tube diode. The anode (plate) is connected to the positive side of the input.
*   The cathode of the diode is connected in series with a high-value load resistor ($R$) and a standard PMMC (Permanent Magnet Moving Coil) meter.
*   The circuit is completed back to the negative side of the AC supply.

**Operation:**
1.  **Rectification:** The core function of this VTVM configuration is to measure AC voltage using a DC-only PMMC meter. It achieves this by using the vacuum tube diode as a half-wave rectifier.
2.  **Positive Half-Cycle:** Let the applied AC input voltage be $e = E_m \sin(\omega t)$. During the positive half-cycle of the AC waveform, the anode (plate) of the diode becomes positive relative to the cathode. The diode is forward-biased and conducts. A current ($i_p$, plate current) flows through the diode, the resistor $R$, and the PMMC meter.
3.  **Negative Half-Cycle:** During the negative half-cycle, the anode becomes negative relative to the cathode. The diode is reverse-biased and blocks current flow. The current $i_p$ drops to zero.
4.  **Meter Response:** The resulting current flowing through the PMMC meter consists of a series of unidirectional (DC) pulses, occurring only during the positive half-cycles. 
    Because the PMMC meter movement has mechanical inertia, it cannot track these rapid individual pulses. Instead, the pointer deflects to a steady position proportional to the **average value** ($I_{av}$) of these half-wave rectified current pulses.
5.  **Calibration:** The average current is directly proportional to the peak voltage ($E_m$) of the AC input. Since AC voltages are typically specified in RMS (Root Mean Square) values, the scale of the PMMC meter is specifically calibrated to indicate the RMS value of a pure sine wave, assuming a fixed form factor relationship between the average rectified current and the RMS voltage.

Ans related location pg number in ak slide: 110.

***

### 98. Page 9, Q.6. (b): Why digital voltmeter is better than analog one? Describe a ramp type digital voltmeter.

**Answer:**
**Why a Digital Voltmeter (DVM) is better than an analog one:**
*(This is functionally similar to Q94).*
1.  **Elimination of Human Error:** DVMs display exact numerical values, completely eliminating parallax errors (reading a needle from an angle) and interpolation errors (guessing the value between scale tick marks) that are common with analog meters.
2.  **Higher Resolution and Accuracy:** DVMs can provide much higher resolution (e.g., displaying millivolts or microvolts with 4.5 or 5.5 digits). They are inherently more accurate because they rely on precise digital quantization rather than the mechanical tolerances of springs and magnetic fields.
3.  **Higher Input Impedance:** DVMs generally have a significantly higher input impedance (often $>10 \text{ M}\Omega$) compared to standard analog VOMs. This means they draw virtually no current from the circuit under test, preventing the "loading effect" which alters the voltage being measured.
4.  **Auto-Ranging and Polarity:** Most DVMs automatically select the best measurement range and automatically display the correct polarity (+ or -). Analog meters require manual range switching and can be damaged if connected backward.
5.  **Data Logging:** Digital outputs can be easily interfaced with microprocessors or computers for automated data recording and complex mathematical processing.

**Description of a Ramp Type Digital Voltmeter:**
*(This is functionally identical to Q96. I will summarize briefly).*
A Ramp-type DVM measures voltage by converting the voltage magnitude into a proportional time interval.
1.  **The Ramp:** A generator creates a linear "ramp" voltage that decreases steadily from a positive value down to zero.
2.  **The Measurement Cycle:** The process starts, resetting a digital counter to zero.
3.  **Start Counting:** A comparator continuously compares this falling ramp voltage to the unknown input voltage. At the exact instant the ramp crosses the unknown voltage level, a gate opens, allowing high-frequency clock pulses from an internal oscillator to flow into the counter.
4.  **Stop Counting:** A second comparator watches the ramp voltage. When the ramp hits exactly 0 Volts (ground), it closes the gate, stopping the clock pulses.
5.  **The Result:** Because the ramp falls at a constant, linear rate, the time between the "start" (crossing the input voltage) and "stop" (crossing zero) is strictly proportional to the magnitude of the input voltage. The final number of clock pulses tallied by the counter represents this time interval and thus represents the voltage, which is then displayed on the digital screen.

Ans related location pg number in ak slide: 105 (Advantages), 106, 107, 108 (Ramp DVM).

***

### 99. Page 21, Q.6 (a) [Second block]: Classify digital instruments. Explain the construction and operation of a VTVM.

**Answer:**
**Classification of Digital Instruments:**
Digital instruments can be broadly classified based on the analog-to-digital conversion (ADC) technique they employ. Common classifications include:
1.  **Ramp type DVM:** Converts voltage to a time interval using a linear ramp voltage.
2.  **Potentiometric (or Null-Balance) DVM:** Compares the unknown voltage against a known reference voltage using an automated balancing mechanism.
3.  **Integrating type DVM (e.g., Dual-Slope):** Converts the input voltage to a frequency or integrates it over a fixed time to determine the average value, offering excellent noise rejection.
4.  **Continuous balance DVM:** Uses a servo-driven potentiometer to continuously track and balance the input voltage.
5.  **Successive approximation DVM:** Uses a binary search algorithm to rapidly narrow down the voltage value by comparing it to internal reference levels generated by a DAC.

**Construction and Operation of a VTVM (Vacuum Tube Voltmeter):**
*(Note: A VTVM is an ANALOG instrument, not a digital one. The question pairs classification of digital instruments with explaining an analog one. I will explain the average diode type VTVM based on slide 110).*

**Construction:**
The fundamental construction includes an input terminal, a vacuum tube diode acting as a half-wave rectifier, a high-value load resistor ($R$), and a sensitive Permanent Magnet Moving Coil (PMMC) meter, all connected in series back to the supply ground.

**Operation:**
The purpose of the diode type VTVM is to allow a DC-only PMMC meter to measure an AC voltage.
1.  When an alternating voltage ($e = E_m \sin\omega t$) is applied, the vacuum tube diode acts as a one-way valve.
2.  During the positive half-cycle of the AC wave, the diode's anode is positive relative to the cathode. The diode conducts, allowing a pulse of current ($i_p$) to flow through the resistor and the PMMC meter.
3.  During the negative half-cycle, the anode is negative. The diode is reverse-biased and blocks all current flow.
4.  The PMMC meter receives a rapid sequence of unidirectional (DC) pulses. Because the moving coil has physical mass and inertia, it cannot vibrate with these pulses. Instead, the pointer deflects to a steady position that corresponds to the **average value** ($I_{av}$) of the pulsating half-wave current.
5.  Since this average current is strictly proportional to the peak of the AC input voltage, the meter's analog scale can be specifically calibrated to read the Root Mean Square (RMS) value of the AC voltage (assuming a pure sine wave input). The primary benefit of using the vacuum tube is its extremely high input impedance, preventing circuit loading.

Ans related location pg number in ak slide: 106 (Classification list), 110 (VTVM operation).

***

### 100. Page 21, Q.7 (b) [Second block]: What is DVM? Explain the operating principle of an potentiometric DVM.

**Answer:**
*(This is functionally identical to Q95. I will provide a slightly different wording for variety, but the core technical content remains the same based on slide 109).*

**What is a DVM?**
A Digital Voltmeter (DVM) is an electronic test instrument that takes an analog voltage signal as an input, converts that continuous signal into a discrete digital number using an Analog-to-Digital Converter (ADC), and presents the measurement on a numerical display (like an LCD).

**Operating Principle of a Potentiometric DVM:**
A Potentiometric DVM determines an unknown voltage by continuously comparing it to a known, adjustable internal reference voltage until the two are exactly equal (a "null" balance).

1.  **The Components:** It utilizes a highly stable internal DC reference voltage source connected across a precision precision potentiometer. The position of the sliding contact on this potentiometer dictates a specific feedback voltage ($V_f$).
2.  **The Comparison:** The unknown analog input voltage ($V_x$) is fed into one side of a Comparator circuit. The feedback voltage ($V_f$) from the potentiometer is fed into the other side.
3.  **Generating the Error:** The Comparator continuously subtracts $V_f$ from $V_x$. It generates an "Error Signal" that represents both the magnitude and polarity of the difference between the two voltages.
4.  **The Balancing Loop:** This error signal is fed into an Error Amplifier, which in turn drives the "Adjustment Device" (historically a small motor, now digital logic networks).
5.  **Achieving Null:** The adjustment device physically or electronically moves the sliding contact on the potentiometer in whatever direction reduces the error signal. 
    *   If $V_x$ is higher than $V_f$, the wiper moves up to increase $V_f$.
    *   If $V_x$ is lower than $V_f$, the wiper moves down to decrease $V_f$.
6.  **The Reading:** The wiper continues to move until $V_f$ exactly matches the unknown voltage $V_x$. At this point, the error signal is zero, and the system reaches equilibrium ("null"). Because the potentiometer is precisely calibrated, the final physical or logical position of the sliding contact represents the exact numerical value of the unknown voltage. This position is converted into digital numbers and sent to the Readout display.

Ans related location pg number in ak slide: 106, 109.

### 101. Page 6, Q.2 c): What is the source of error in Q measurement and how it can be measured?

**Answer:**
**Source of Error in Q Measurement:**
The most significant and often overlooked source of error when measuring the Quality factor (Q) of a coil using a Q-meter is the **distributed capacitance (or self-capacitance, $C_d$)** of the measuring circuit and the coil itself. 
Every physical inductor has some inherent capacitance between its adjacent turns and layers. When a coil is placed in a resonant circuit, this distributed capacitance ($C_d$) acts in parallel with the coil's inductance ($L$) and resistance ($R$). The external tuning capacitor ($C$) in the Q-meter is also in parallel with this combination.
This internal distributed capacitance $C_d$ changes the effective inductance and the effective total resistance of the coil at high frequencies. Consequently, the Q value indicated by the Q-meter (the "effective Q" or $Q_e$) will differ from the true Q ($Q_t$) of the coil. The indicated Q is generally lower than the true Q.

**How it can be measured (Determining Distributed Capacitance $C_d$):**
To measure $C_d$, the resonant frequency formula is utilized. We measure the resonant state at two different frequencies, typically one being double the other.
The resonant frequency of the $LC$ circuit (including $C_d$) is given by: $f = \frac{1}{2\pi\sqrt{L(C + C_d)}}$

1.  **First Measurement:** Connect the coil and set the oscillator to a known frequency $f_1$. Tune the external capacitor until resonance is achieved. Note the value of the tuning capacitor as $C_1$.
    The resonant frequency is: $f_1 = \frac{1}{2\pi\sqrt{L(C_1 + C_d)}}$
2.  **Second Measurement:** Increase the oscillator frequency to exactly double the first frequency: $f_2 = 2f_1$. Re-tune the external capacitor until resonance is achieved again. Note the new value of the tuning capacitor as $C_2$.
    The new resonant frequency is: $f_2 = \frac{1}{2\pi\sqrt{L(C_2 + C_d)}}$
3.  **Calculation:** Since $f_2 = 2f_1$, we substitute the frequency equations:
    $\frac{1}{2\pi\sqrt{L(C_2 + C_d)}} = 2 \left( \frac{1}{2\pi\sqrt{L(C_1 + C_d)}} \right)$
    Squaring both sides and canceling the common terms ($1/4\pi^2L$):
    $\frac{1}{C_2 + C_d} = \frac{4}{C_1 + C_d}$
    $C_1 + C_d = 4(C_2 + C_d)$
    $C_1 + C_d = 4C_2 + 4C_d$
    $C_1 - 4C_2 = 3C_d$
    **$C_d = \frac{C_1 - 4C_2}{3}$**
By performing these two measurements and using this formula, the distributed capacitance $C_d$ (the source of the error) can be accurately determined.

Ans related location pg number in ak slide: 117, 118.

***

### 102. Page 9, Q.2. (b): What is resonance? What is the source of error in Q measurement and how it can be measured?

**Answer:**
*(The second half of this question is identical to Q101. I will address the first part and summarize the second).*

**What is resonance?**
Electrical resonance occurs in an AC circuit containing both inductance ($L$) and capacitance ($C$) when the frequency of the applied alternating voltage causes the inductive reactance ($X_L = 2\pi f L$) to exactly equal the capacitive reactance ($X_C = \frac{1}{2\pi f C}$).
*   **In a Series Circuit:** When $X_L = X_C$, the two reactive components cancel each other out ($X_L - X_C = 0$). The total impedance of the circuit drops to its absolute minimum, equal only to the pure resistance ($Z = R$). At this resonant frequency, the circuit draws maximum current, and the current is perfectly in phase with the applied voltage (Power Factor = 1). The voltage across the inductor and capacitor can be much larger than the supply voltage (voltage magnification), which is the principle behind the Q-meter.

**Source of Error in Q Measurement:**
The primary source of error is the **distributed (or self) capacitance ($C_d$)** of the coil being measured. This internal capacitance acts in parallel with the coil's inductance, altering its effective impedance and causing the Q-meter to display an "effective Q" that differs from the coil's "true Q".

**How it can be measured (Determining $C_d$):**
*(Summary of Q101)*
The distributed capacitance $C_d$ is calculated by finding the tuning capacitor values required for resonance at two specific frequencies, where the second frequency is exactly double the first ($f_2 = 2f_1$).
1. Tune to resonance at frequency $f_1$; record tuning capacitor value $C_1$.
2. Tune to resonance at frequency $f_2$ (where $f_2 = 2f_1$); record tuning capacitor value $C_2$.
3. Calculate $C_d$ using the derived formula based on the resonance equations:
   **$C_d = \frac{C_1 - 4C_2}{3}$**

Ans related location pg number in ak slide: 112 (Resonance principles), 117, 118 (Error source and measurement).

***

### 103. Page 20, Q.2 b): Mathematically explain the Q-meter measurement of low impedance components in series connection.

**Answer:**
To measure an unknown low impedance component ($Z_s = R_s + jX_s$) using a Q-meter, the "Series Connection" method is used. This involves two distinct resonant measurements using a stable, high-Q reference "work coil" ($L, R$).

**1. First Measurement (Initial Resonance):**
*   The unknown component $Z_s$ is short-circuited (bypassed by a heavy strap).
*   The circuit consists only of the work coil ($L, R$) and the tuning capacitor.
*   The oscillator is set to the desired test frequency ($\omega$).
*   The tuning capacitor is adjusted to value $C_1$ to achieve resonance.
*   At resonance, inductive reactance equals capacitive reactance: $X_{C1} = X_L$
    $\frac{1}{\omega C_1} = \omega L$
*   The indicated Quality factor at this state is $Q_1$. By definition of a series resonant circuit:
    $Q_1 = \frac{\omega L}{R} = \frac{1}{\omega C_1 R}$

**2. Second Measurement (With Unknown Component):**
*   The shorting strap is removed, and the unknown impedance $Z_s$ (which consists of unknown resistance $R_s$ and unknown reactance $X_s$) is placed in series with the work coil.
*   The frequency remains exactly the same ($\omega$).
*   The tuning capacitor is adjusted to a new value $C_2$ to restore resonance.
*   The new indicated Quality factor is $Q_2$.
*   The new total resistance of the circuit is $(R + R_s)$.
*   At the new resonance point, the total capacitive reactance must equal the total inductive (or reactive) components:
    $X_{C2} = X_L + X_s$

**3. Mathematical Extraction of Unknowns:**
*   **Finding Unknown Reactance ($X_s$):**
    From the second measurement: $X_s = X_{C2} - X_L$
    Substitute $X_L = X_{C1}$ from the first measurement:
    $X_s = X_{C2} - X_{C1}$
    **$X_s = \frac{1}{\omega C_2} - \frac{1}{\omega C_1} = \frac{C_1 - C_2}{\omega C_1 C_2}$**
    *(Note: If $C_1 > C_2$, $X_s$ is positive, meaning the unknown component is inductive. If $C_1 < C_2$, $X_s$ is negative, meaning it is capacitive).*

*   **Finding Unknown Resistance ($R_s$):**
    From the definition of Q in the two states:
    $R = \frac{X_1}{Q_1} = \frac{1}{\omega C_1 Q_1}$
    The total resistance in the second state is $(R + R_s) = \frac{X_2}{Q_2} = \frac{1}{\omega C_2 Q_2}$
    Therefore, the unknown resistance is the difference between total resistance and initial resistance:
    $R_s = (R + R_s) - R$
    $R_s = \frac{1}{\omega C_2 Q_2} - \frac{1}{\omega C_1 Q_1}$
    **$R_s = \frac{C_1 Q_1 - C_2 Q_2}{\omega C_1 C_2 Q_1 Q_2}$**

*   **Finding Unknown Q ($Q_s$):**
    The quality factor of the unknown component itself is $Q_s = \frac{X_s}{R_s}$.
    Substitute the derived expressions for $X_s$ and $R_s$:
    $Q_s = \frac{\frac{C_1 - C_2}{\omega C_1 C_2}}{\frac{C_1 Q_1 - C_2 Q_2}{\omega C_1 C_2 Q_1 Q_2}}$
    **$Q_s = \frac{(C_1 - C_2) Q_1 Q_2}{C_1 Q_1 - C_2 Q_2}$**

Ans related location pg number in ak slide: 114, 115, 116.

***

### 104. Page 20, Q.2 c): In a Q-meter, a coil with a resistance of 10 $\Omega$ is connected in the direct measurement mode. Resonance occurs when the oscillator frequency is 1MHz and the resonating capacitor is set at 65pF. Find the percentage error introduced in the calculated value of Q by the 0.02 $\Omega$ insertion resistance.

**Answer:**
**Understanding the Insertion Resistance Error:**
In the direct measurement mode of a Q-meter, an internal small resistor (often part of a thermocouple or an injection transformer) is used to inject the oscillator voltage $E$ into the series resonant circuit. This resistor is called the "insertion resistance" ($R_{sh}$).
Because this resistance is physically in series with the coil being measured, the total resistance at resonance is not just the coil's resistance ($R$), but $(R + R_{sh})$. 
The Q-meter actually measures the quality factor of the *entire* circuit, which is the "Indicated Q" ($Q_{ind}$).
The "True Q" ($Q_{true}$) is the quality factor of the coil alone.

**Given Data:**
*   Coil resistance, $R = 10 \, \Omega$
*   Oscillator frequency, $f = 1 \text{ MHz} = 10^6 \text{ Hz}$
*   Resonating capacitance, $C = 65 \text{ pF} = 65 \times 10^{-12} \text{ F}$
*   Insertion resistance, $R_{sh} = 0.02 \, \Omega$
*   Angular frequency, $\omega = 2\pi f = 2\pi \times 10^6 \text{ rad/s}$

**Step 1: Calculate the Reactance ($X_L$ or $X_C$) at Resonance.**
At resonance, inductive reactance $X_L$ equals capacitive reactance $X_C$. We calculate $X_C$ since $C$ is known:
$X_C = \frac{1}{\omega C} = \frac{1}{2\pi \times 10^6 \times 65 \times 10^{-12}}$
$X_C = \frac{1}{2\pi \times 65 \times 10^{-6}}$
$X_C = \frac{10^6}{130\pi} \approx \frac{1000000}{408.407} \approx 2448.54 \, \Omega$
So, the inductive reactance of the coil $X_L \approx 2448.54 \, \Omega$.

**Step 2: Calculate the True Q ($Q_{true}$) of the coil.**
True Q considers only the coil's own resistance.
$Q_{true} = \frac{X_L}{R} = \frac{2448.54}{10} = \mathbf{244.854}$

**Step 3: Calculate the Indicated Q ($Q_{ind}$) measured by the instrument.**
Indicated Q considers the total resistance of the resonant circuit, which includes the insertion resistance.
Total Resistance = $R + R_{sh} = 10 + 0.02 = 10.02 \, \Omega$
$Q_{ind} = \frac{X_L}{R + R_{sh}} = \frac{2448.54}{10.02} \approx \mathbf{244.365}$

**Step 4: Calculate the Percentage Error.**
The error is the difference between the true value and the indicated value, relative to the true value.
Error (%) $= \frac{Q_{true} - Q_{ind}}{Q_{true}} \times 100\%$
*(Note: Sometimes error is defined relative to the measured value depending on standard conventions, but "error introduced in the calculated value" usually implies deviation from truth).*
Error (%) $= \frac{244.854 - 244.365}{244.854} \times 100\%$
Error (%) $= \frac{0.489}{244.854} \times 100\%$
Error (%) $\approx 0.001997 \times 100\%$
**Error (%) $\approx 0.1997\%$**

The insertion resistance introduces an error of approximately **0.2%** in the Q measurement.

Ans related location pg number in ak slide: 111 (Q definition). The concept of insertion resistance error is general Q-meter theory.

### 105. Page 20, Q.4 a): What is meant by distributed capacitance?

**Answer:**
**Distributed Capacitance** (also known as self-capacitance) refers to the inherent, unavoidable parasitic capacitance that exists within any physical inductor or coil. 

Whenever an insulated wire is wound into a coil, adjacent turns of wire lie close to each other, separated by the insulation and a thin layer of air. Because there is a potential difference between adjacent turns when a current flows, and they are separated by a dielectric, they inadvertently act as the tiny plates of a capacitor. Similar capacitive effects exist between different layers of windings and between the windings and the physical core or chassis.

These numerous, infinitesimally small individual capacitances are distributed throughout the entire physical length of the coil. In circuit analysis, to simplify calculations, all these tiny distributed capacitances are "lumped" together and modeled as a single equivalent capacitor ($C_d$) connected in parallel with the ideal inductance ($L$) and series resistance ($R$) of the coil. 

This distributed capacitance becomes highly significant at high frequencies (like Radio Frequencies). It causes the coil to exhibit a self-resonant frequency, meaning at a specific high frequency, the coil's own inductance will resonate with its own distributed capacitance without any external capacitors connected. Furthermore, it introduces significant errors in Q-meter measurements because it alters the effective inductance and resistance of the coil.

Ans related location pg number in ak slide: 117.

***

### 106. Page 20, Q.4 b): A circuit consisting of an unknown coil, a resistance and a variable capacitor in series is tuned to resonance using a Q meter. If the frequency is 450 kHz and the resonating capacitor is set at 250 pF, determine the effective inductance and resistance of unknown coil. The Q meter indicates 105 and the resistance is $0.75\Omega$.

**Answer:**
**Clarification of the Problem Statement:**
The phrasing "a circuit consisting of an unknown coil, a resistance and a variable capacitor... The Q meter indicates 105 and the resistance is $0.75\Omega$" implies a direct measurement setup where an external resistance is present, perhaps as an insertion resistor or a known added series resistor. 
Let's assume the standard Q-meter direct measurement model where the total circuit resistance includes the coil's resistance ($R_L$) and this given added/insertion resistance ($R_{add} = 0.75 \Omega$). The Q-meter measures the Q of the *entire* resonant circuit.

**Given Data:**
*   Resonant frequency, $f = 450 \text{ kHz} = 450 \times 10^3 \text{ Hz}$
*   Tuning capacitance, $C = 250 \text{ pF} = 250 \times 10^{-12} \text{ F}$
*   Indicated Q of the circuit, $Q_{ind} = 105$
*   Known added/insertion resistance, $R_{add} = 0.75 \, \Omega$
*   Angular frequency, $\omega = 2\pi f = 2\pi \times 450 \times 10^3 \approx 2.827 \times 10^6 \text{ rad/s}$

**Step 1: Calculate the Effective Inductance ($L_e$)**
At resonance, the inductive reactance equals the capacitive reactance: $X_L = X_C$.
$\omega L_e = \frac{1}{\omega C}$
$L_e = \frac{1}{\omega^2 C}$
$L_e = \frac{1}{(2\pi \times 450 \times 10^3)^2 \times (250 \times 10^{-12})}$
$L_e = \frac{1}{(7.994 \times 10^{12}) \times (250 \times 10^{-12})}$
$L_e = \frac{1}{1998.5}$
$L_e \approx 0.0005004 \text{ H} = \mathbf{500.4 \, \mu\text{H}}$

**Step 2: Calculate the Total Circuit Resistance ($R_{total}$)**
The indicated Q is based on the total resistance of the resonant circuit:
$Q_{ind} = \frac{\omega L_e}{R_{total}} = \frac{1}{\omega C R_{total}}$
Rearranging for $R_{total}$:
$R_{total} = \frac{1}{\omega C Q_{ind}}$
Since we already know $\frac{1}{\omega C} = \omega L_e \approx (2.827 \times 10^6) \times (0.0005004) \approx 1414.7 \, \Omega$ (This is $X_L$ or $X_C$)
$R_{total} = \frac{1414.7}{105} \approx 13.47 \, \Omega$

**Step 3: Calculate the Effective Resistance of the unknown coil ($R_e$)**
The total resistance is the sum of the coil's effective resistance and the known added resistance:
$R_{total} = R_e + R_{add}$
$13.47 = R_e + 0.75$
$R_e = 13.47 - 0.75$
**$R_e = 12.72 \, \Omega$**

*(Note: "Effective" values are calculated because this single-frequency measurement does not separate out the effects of distributed capacitance, which slightly alters the apparent inductance and resistance. The values calculated are what the circuit "sees" at 450 kHz).*

Ans related location pg number in ak slide: 111, 112 (Q definition and resonance equations).

***

### 107. Page 21, Q.6 (b) [Second block]: Why Q meter is important? Calculate the value of self-capacitance of a coil when the following measurements are made: At the frequency of 2 MHz, the tuning capacitor is set at 450 pF. When the frequency is increased to 5 MHz, the tuning capacitor is tuned at 60 pF.

**Answer:**
**Why is a Q meter important?**
A Q-meter is a vital instrument in radio-frequency (RF) engineering and electronics because it provides a direct, highly accurate method to measure the "Quality Factor" ($Q$) of coils and capacitors. The Q factor determines the sharpness of resonance (selectivity), bandwidth, and efficiency of tuned circuits. High-Q components are essential for designing sharp filters and stable oscillators in transmitters and receivers. Furthermore, a Q-meter is incredibly versatile; beyond just measuring Q, it is routinely used to precisely measure unknown inductances, very small capacitances, effective resistances at high frequencies, and crucially, the hidden distributed (self) capacitance of coils, which cannot be measured easily by standard low-frequency bridges.

**Calculate the value of self-capacitance ($C_d$):**
This involves the standard two-frequency measurement technique to find distributed capacitance.
The resonant frequency formula is $f = \frac{1}{2\pi\sqrt{L(C + C_d)}}$.
Squaring this gives $f^2 = \frac{1}{4\pi^2 L (C + C_d)}$, which can be rearranged to $\frac{1}{f^2} = 4\pi^2 L (C + C_d)$.

**Given Data:**
*   Measurement 1: $f_1 = 2 \text{ MHz}$, $C_1 = 450 \text{ pF}$
*   Measurement 2: $f_2 = 5 \text{ MHz}$, $C_2 = 60 \text{ pF}$

We can set up a ratio since $4\pi^2 L$ is constant for both measurements:
$\frac{1/f_1^2}{1/f_2^2} = \frac{C_1 + C_d}{C_2 + C_d}$
$\frac{f_2^2}{f_1^2} = \frac{C_1 + C_d}{C_2 + C_d}$

Substitute the frequency values (we can leave them in MHz as the units cancel):
$\frac{5^2}{2^2} = \frac{450 + C_d}{60 + C_d}$
$\frac{25}{4} = \frac{450 + C_d}{60 + C_d}$
$6.25 = \frac{450 + C_d}{60 + C_d}$

Multiply both sides by the denominator:
$6.25 \times (60 + C_d) = 450 + C_d$
$375 + 6.25 C_d = 450 + C_d$

Rearrange to solve for $C_d$:
$6.25 C_d - C_d = 450 - 375$
$5.25 C_d = 75$
$C_d = \frac{75}{5.25}$
**$C_d \approx 14.28 \text{ pF}$**

The self-capacitance of the coil is approximately **14.28 pF**.

*(Note: This uses the general two-frequency method. The simpler formula $C_d = (C_1 - 4C_2)/3$ derived in Q101 only works strictly when $f_2 = 2f_1$. Since $5\text{MHz} \neq 2 \times 2\text{MHz}$, the general ratio method must be used).*

Ans related location pg number in ak slide: 111, 117, 118 (General $C_d$ measurement theory).

***

### 108. Page 5, Q.6 (b): Write an Arduino program for an air conditioner that uses a thermistor as a temperature sensor. The air conditioner should turn on when the temperature above 25 $^\circ$C and it should turn off when the temperature is below 22 $^\circ$C. Use the Steinhart-Hart equation to convert resistance to temperature, where $A = 10^{-3}$, $B = 2 \times 10^{-4}$, and $C = 9 \times 10^{-8}$.

**Answer:**
To write this program, we assume a standard voltage divider circuit where the thermistor ($R_{th}$) is in series with a known fixed resistor ($R_{fixed}$, e.g., 10k$\Omega$), connected between 5V and Ground. The analog pin reads the voltage at the junction between them.

The Steinhart-Hart equation relates thermistor resistance to temperature in Kelvin:
$\frac{1}{T} = A + B \ln(R_{th}) + C (\ln(R_{th}))^3$

```cpp
// Define pins
const int analogPin = A0;      // Pin connected to the voltage divider
const int acControlPin = 8;    // Pin to control the AC relay/transistor

// Known variables for the voltage divider
const float Vcc = 5.0;         // Arduino supply voltage
const float R_fixed = 10000.0; // Known fixed resistor value in Ohms (e.g., 10k)

// Steinhart-Hart Coefficients (Given in the problem)
const float A = 1.0e-3;
const float B = 2.0e-4;
const float C = 9.0e-8;

// AC State variable
bool acIsOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(acControlPin, OUTPUT);
  digitalWrite(acControlPin, LOW); // Ensure AC is off initially
}

void loop() {
  // 1. Read the Analog Value (0 to 1023)
  int rawADC = analogRead(analogPin);
  
  // Prevent division by zero if reading is 0
  if (rawADC == 0) return; 

  // 2. Calculate the Voltage across the fixed resistor
  float V_out = rawADC * (Vcc / 1023.0);

  // 3. Calculate Thermistor Resistance (R_th)
  // Assuming configuration: 5V -> R_fixed -> AnalogPin -> R_th -> GND
  // Voltage divider equation: V_out = Vcc * (R_th / (R_th + R_fixed))
  // Rearranged for R_th:
  float R_th = R_fixed * (V_out / (Vcc - V_out));

  // 4. Calculate Temperature using Steinhart-Hart Equation
  float logR = log(R_th);
  float tempK = 1.0 / (A + (B * logR) + (C * logR * logR * logR)); // Temp in Kelvin
  float tempC = tempK - 273.15; // Convert Kelvin to Celsius

  // Print for debugging
  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");

  // 5. Control Logic (Hysteresis/Bang-Bang Control)
  if (tempC > 25.0 && !acIsOn) {
    digitalWrite(acControlPin, HIGH); // Turn AC ON
    acIsOn = true;
    Serial.println("AC TURNED ON");
  } 
  else if (tempC < 22.0 && acIsOn) {
    digitalWrite(acControlPin, LOW);  // Turn AC OFF
    acIsOn = false;
    Serial.println("AC TURNED OFF");
  }

  // Small delay before next reading
  delay(1000); 
}
```

**Explanation of the Code:**
1.  **Read and convert ADC:** The raw analog value (0-1023) is converted to an actual voltage ($V_{out}$).
2.  **Calculate Resistance:** Using the standard voltage divider formula, the actual resistance of the thermistor ($R_{th}$) at that moment is calculated. *(Note: The formula used assumes the thermistor is connected to ground. If it's connected to 5V, the formula slightly changes, but the principle holds).*
3.  **Steinhart-Hart Equation:** The given coefficients $A$, $B$, and $C$ are plugged into the mathematical formula to find the absolute temperature in Kelvin. This is then converted to Celsius by subtracting 273.15.
4.  **Hysteresis Control Logic:** This is the core logic. 
    *   If temperature > $25^\circ\text{C}$, the AC turns ON.
    *   If temperature < $22^\circ\text{C}$, the AC turns OFF.
    *   If the temperature is between $22^\circ\text{C}$ and $25^\circ\text{C}$, the AC *maintains its current state*. This deadband (hysteresis) prevents the AC unit from rapidly clicking on and off when the temperature hovers right around a single setpoint, which would damage the compressor.

Ans related location pg number in ak slide: 139 (Thermistor section, though specific Arduino programming is usually supplementary lab knowledge).



