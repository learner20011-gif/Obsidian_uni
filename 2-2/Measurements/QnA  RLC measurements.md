### 1. Page 4, Q.3.(a): Describe the loss of charge method to measure high resistance.

**Solution:**
The loss of charge method is primarily used to measure very high resistances, such as the insulation resistance of cables. 

**Principle and Setup:**
In this method, the unknown high resistance ($R$) is connected in parallel with a known capacitor ($C$) and an electrostatic voltmeter ($V$). The circuit is also connected to a DC voltage source via a switch. 
*   **Figure Description:** The circuit diagram consists of a DC voltage source ($V$) on the left, connected through a switch to three parallel branches: an electrostatic voltmeter, the unknown resistance ($R$), and a capacitor ($C$). 

**Procedure and Derivation:**
1.  The switch is closed, allowing the DC source to charge the capacitor $C$ to the maximum voltage $V$.
2.  The switch is then opened. The capacitor begins to discharge its stored energy through the unknown high resistance $R$.
3.  The voltmeter measures the decaying voltage across the capacitor over a specific period of time $t$.

Mathematically, the voltage across the capacitor at any instant $t$ during the discharge is given by the exponential decay equation:
$v_c = V e^{-t/RC}$

To find the resistance $R$, we take the natural logarithm of both sides:
$\ln(v_c) = \ln(V) - \frac{t}{RC}$

Rearranging the formula to solve for $R$:
$\frac{t}{RC} = \ln(V) - \ln(v_c) = \ln\left(\frac{V}{v_c}\right)$

$R = \frac{t}{C \ln(V/v_c)}$

Converting the natural logarithm to base 10 (since $\ln(x) = 2.303 \log_{10}(x)$ and $1/2.303 \approx 0.4343$):
$R = \frac{0.4343 t}{C \log_{10}(V/v_c)}$

By knowing the initial voltage ($V$), the voltage after time $t$ ($v_c$), the time elapsed ($t$), and the capacitance ($C$), the unknown high resistance $R$ can be calculated.

*   **Reference in eee2211 slide:** Pages 71, 72, 73, 74, 75
*   **Reference in sawhney pdf:** Not covered in the provided pages.

***

### 2. Page 7, Q.1 (c): List the methods for the measurement of medium resistance. Briefly explain Carey-Foster slide wire bridge for the measurement of medium resistance.

**Solution:**
**Methods for the measurement of medium resistance (1 $\Omega$ to 100 k$\Omega$):**
1.  Wheatstone bridge method
2.  Substitution method
3.  Ammeter-Voltmeter method
4.  Ohmmeter method

**Carey-Foster Slide Wire Bridge:**
The Carey-Foster bridge is a highly accurate modification of the standard Wheatstone bridge, specifically designed to measure medium resistances or to determine the exact difference between two nearly equal resistances. 

*Principle and Operation:*
The standard Wheatstone bridge suffers from minor errors introduced by the contact resistances and the resistances of the connecting leads. The Carey-Foster bridge eliminates these errors. It utilizes a slide wire of uniform cross-section (similar to a potentiometer) placed between two ratio arms. 
To find the unknown resistance, two separate balance points are found:
1.  A standard resistor and the unknown resistor are placed in the outer gaps of the bridge. The slider is moved along the wire until the galvanometer shows zero deflection, and the balance length is noted.
2.  The positions of the standard resistor and the unknown resistor are then swapped. A new balance point is found on the slide wire.

By utilizing the difference between these two balance lengths and knowing the resistance per unit length of the slide wire, the exact difference between the standard and unknown resistance can be calculated mathematically. Because the resistors are swapped and measured using the same contacts and leads, the parasitic lead and contact resistances cancel each other out in the final calculation, yielding a highly accurate measurement of the medium resistance.

*   **Reference in eee2211 slide:** Page 31 (List of methods). The Carey-Foster bridge specifically is not detailed in the provided slides.
*   **Reference in sawhney pdf:** Not covered in the provided pages.

***

### 3. Page 7, Q.2 (c): A 4-terminal resistor of approximately 50 $\mu\Omega$ resistance was measured by means of Kelvin bridge having the following component resistances: standard resistor = 100.03 $\mu\Omega$; Inner ration arm = 100.31 $\Omega$ and 200 $\Omega$; outer ratio arms = 100.24 $\Omega$ and 200 $\Omega$; resistance of the link connecting the standard and the unknown resistance = 700 $\mu\Omega$. Calculate the unknown resistance to the nearest 0.01 $\mu\Omega$.

**Solution:**
**Given Data:**
*   Standard resistance, $S = 100.03\ \mu\Omega$
*   Outer ratio arms: $P = 100.24\ \Omega$, $Q = 200\ \Omega$
*   Inner ratio arms: $p = 100.31\ \Omega$, $q = 200\ \Omega$
*   Link resistance, $r = 700\ \mu\Omega = 700 \times 10^{-6}\ \Omega$

**Formula:**
The exact equation for a Modified Kelvin Double Bridge is:
$R = \frac{P}{Q}S + \frac{qr}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]$

**Step-by-Step Calculation:**
1. Calculate the main ratio term ($P/Q$):
$\frac{P}{Q} = \frac{100.24}{200} = 0.5012$

2. Calculate the inner ratio term ($p/q$):
$\frac{p}{q} = \frac{100.31}{200} = 0.50155$

3. Calculate the difference in ratios:
$\left[ \frac{P}{Q} - \frac{p}{q} \right] = 0.5012 - 0.50155 = -0.00035$

4. Calculate the link resistance multiplier term:
$\frac{qr}{p + q + r} = \frac{200 \times 700\ \mu\Omega}{100.31 + 200 + (700 \times 10^{-6})}$
Since $r$ is extremely small compared to $p$ and $q$, the denominator is essentially $300.31\ \Omega$.
$\frac{qr}{p + q + r} = \frac{140000\ \mu\Omega}{300.3107} \approx 466.1838\ \mu\Omega$

5. Calculate the error correction term:
$466.1838\ \mu\Omega \times (-0.00035) \approx -0.16316\ \mu\Omega$

6. Calculate the main resistance value:
$\frac{P}{Q}S = 0.5012 \times 100.03\ \mu\Omega = 50.135036\ \mu\Omega$

7. Calculate final unknown resistance $R$:
$R = 50.135036\ \mu\Omega - 0.16316\ \mu\Omega = 49.971876\ \mu\Omega$

Rounding to the nearest 0.01 $\mu\Omega$, the unknown resistance is **$49.97\ \mu\Omega$**.

*   **Reference in eee2211 slide:** Pages 55, 70
*   **Reference in sawhney pdf:** Not covered in the provided pages.

***

### 4. Page 14, Q.5. (b): Kelvin’s double bridge is used to measure an unknown resistance, where, the value of the standard resistor is 100.03 $\Omega$; inner ratio arms are 100.31 $\Omega$ and 200 $\Omega$, respectively; outer ratio arms are 100.24 $\Omega$ and 200 $\Omega$ respectively. If the resistance of the link connecting the unknown and the standard resistance is 700 $\mu\Omega$, calculate the value of the unknown resistance.

**Solution:**
*(Note: This problem uses the exact same variable numbers as Question 3, but the unit provided for the standard resistor $S$ in the prompt text is Ohms ($\Omega$) instead of micro-ohms ($\mu\Omega$). We will calculate it strictly as written, though the correction term becomes statistically negligible).*

**Given Data:**
*   Standard resistance, $S = 100.03\ \Omega = 100,030,000\ \mu\Omega$
*   Outer ratio arms: $P = 100.24\ \Omega$, $Q = 200\ \Omega$
*   Inner ratio arms: $p = 100.31\ \Omega$, $q = 200\ \Omega$
*   Link resistance, $r = 700\ \mu\Omega$

**Formula:**
$R = \frac{P}{Q}S + \frac{qr}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]$

**Step-by-Step Calculation:**
1. Main ratio term ($P/Q$): $100.24 / 200 = 0.5012$
2. Inner ratio term ($p/q$): $100.31 / 200 = 0.50155$
3. Ratio difference: $0.5012 - 0.50155 = -0.00035$
4. Error correction term (calculated identically to Question 3):
$\frac{200 \times 700\ \mu\Omega}{300.3107} \times (-0.00035) \approx -0.16316\ \mu\Omega = -0.000000163\ \Omega$
5. Main resistance value:
$\frac{P}{Q}S = 0.5012 \times 100.03\ \Omega = 50.135036\ \Omega$

6. Calculate final unknown resistance $R$:
$R = 50.135036\ \Omega - 0.000000163\ \Omega = 50.1350358\ \Omega$

The value of the unknown resistance is **$50.135\ \Omega$**. *(If the standard resistor was intended to be $100.03\ \mu\Omega$ as is standard for Kelvin Bridge measurements, the answer reverts to $49.97\ \mu\Omega$ as shown in Question 3).*

*   **Reference in eee2211 slide:** Pages 55, 70
*   **Reference in sawhney pdf:** Not covered in the provided pages.
### 5. Page 15, Q.4 (b): Explain the modified Kelvin's double bridge method of measuring low resistance.

**Solution:**
**Concept of Modified Kelvin’s Double Bridge:**
The standard Wheatstone bridge is unsuitable for measuring very low resistances (typically less than $1\ \Omega$) because the contact resistances and the resistances of the connecting leads become significant compared to the unknown resistance, introducing large errors. 

The **Kelvin Double Bridge** is a modification of the Wheatstone bridge that overcomes this problem. It incorporates a second (or "double") set of ratio arms. 
In a modified Kelvin double bridge setup, the unknown low resistance ($R$) and a standard low resistance ($S$) are connected in series with a heavy copper link (whose resistance is $r$). 

**Circuit Arrangement:**
*   **Figure Involved:** The circuit involves an outer set of ratio arms ($P$ and $Q$) and an inner set of ratio arms ($p$ and $q$). 
*   A galvanometer $G$ is connected between the junction of the outer ratio arms ($P$ and $Q$) and the junction of the inner ratio arms ($p$ and $q$).
*   The inner arms $p$ and $q$ connect to the potential terminals of the unknown resistance $R$ and the standard resistance $S$, respectively.
*   The heavy link $r$ connects the current terminals of $R$ and $S$.

**Working Principle:**
The bridge is balanced by adjusting the standard resistance $S$ or the ratio arms until the galvanometer shows zero deflection. 
At the balance condition, no current flows through the galvanometer. The inner ratio arms $p$ and $q$ are selected such that their ratio is exactly equal to the ratio of the outer arms $P$ and $Q$ (i.e., $\frac{P}{Q} = \frac{p}{q}$).

The general balance equation for the Kelvin double bridge is derived as:
$$R = \frac{P}{Q}S + \frac{qr}{p + q + r} \left[ \frac{P}{Q} - \frac{p}{q} \right]$$

When the condition $\frac{P}{Q} = \frac{p}{q}$ is strictly maintained, the second term of the equation becomes zero. The equation then simplifies to:
$$R = \frac{P}{Q}S$$

**Conclusion:**
By using this double-arm arrangement and ensuring the ratios are equal, the effect of the connecting link resistance ($r$) is completely eliminated from the final calculation. This allows for highly accurate measurements of very low resistances, independent of lead and contact resistances.

*   **Reference in eee2211 slide:** Pages 51, 52, 53, 54, 55 (Modified Kelvin Double Bridge Method).

***

### 6. Page 15, Q.4 (c): A resistance of approximately 80 $\Omega$ is to be measured by voltmeter-ammeter method using a 1A ammeter having resistance of 1.5 $\Omega$ and a 50 V voltmeter having a resistance of 4000 $\Omega$. Draw a suitable connection diagram for more accurate measurement.

**Solution:**
In the Voltmeter-Ammeter method, there are two possible connection diagrams:
1.  **Connection A (Voltmeter across the series combination of R and Ammeter):** The ammeter is connected directly in series with the unknown resistance $R$. The voltmeter is connected across both.
2.  **Connection B (Voltmeter directly across R):** The voltmeter is connected directly across the unknown resistance $R$. The ammeter measures the total current drawn by both $R$ and the voltmeter.

To find the "more accurate" connection, we must evaluate the relative error introduced by instrument resistances in both cases.

**Given:**
*   True (approximate) resistance, $R = 80\ \Omega$
*   Ammeter resistance, $R_a = 1.5\ \Omega$
*   Voltmeter resistance, $R_v = 4000\ \Omega$

**Case 1: Connection A (Ammeter in series with R)**
*   The ammeter measures the exact current $I$ flowing through $R$.
*   The voltmeter measures the voltage drop across both $R$ and $R_a$: $V_m = I(R + R_a)$.
*   Measured resistance $R_m = \frac{V_m}{I} = R + R_a$.
*   Relative Error $\epsilon_{r1} = \frac{R_m - R}{R} = \frac{R_a}{R}$
*   Calculating error: $\epsilon_{r1} = \frac{1.5}{80} = 0.01875$ or **$1.875\%$**.

**Case 2: Connection B (Voltmeter directly across R)**
*   The voltmeter measures the exact voltage $V$ across $R$.
*   The ammeter measures the current through $R$ plus the current through the voltmeter: $I_m = I_R + I_v = \frac{V}{R} + \frac{V}{R_v} = V\left(\frac{R + R_v}{R R_v}\right)$.
*   Measured resistance $R_m = \frac{V}{I_m} = \frac{R R_v}{R + R_v}$.
*   Relative Error $\epsilon_{r2} = \frac{R_m - R}{R} = \frac{\frac{R R_v}{R+R_v} - R}{R} = \frac{-R^2}{R(R+R_v)} \approx -\frac{R}{R_v}$ (since $R_v \gg R$).
*   Calculating approximate error magnitude: $|\epsilon_{r2}| \approx \frac{80}{4000} = 0.02$ or **$2.0\%$**.

**Conclusion:**
Since the error magnitude in Connection A ($1.875\%$) is smaller than in Connection B ($2.0\%$), **Connection A is more accurate** for this specific measurement. 

*   **Figure Involved:** The suitable connection diagram corresponds to "Fig. (a)" from the lecture slides. The ammeter is in series with the unknown resistance $R$, and the voltmeter is connected in parallel across the outer terminals of the ammeter and $R$ combined. 

*   **Reference in eee2211 slide:** Pages 38, 39, 40 (Ammeter Voltmeter Method, showing Fig. (a) and its error analysis).

***

### 7. Page 23, CT-02 Q2: Prove that the expression for the relative error in the ammeter-voltmeter method is $\epsilon_r = \frac{R}{R_v}$ where the symbols have their usual meanings.

**Solution:**
This expression corresponds to the connection where the **Voltmeter is connected directly across the unknown resistance $R$** (often referred to as the method for measuring low resistances, shown as Fig. (b) in the lecture slides).

**Proof:**
Let $R$ be the true value of the unknown resistance.
Let $R_v$ be the internal resistance of the voltmeter.
Let $R_m$ be the measured value of the resistance, calculated by Ohm's Law using the meter readings: $R_m = \frac{V_m}{I_m}$.

1.  In this circuit configuration, the voltmeter reads the true voltage across the resistor: $V_m = V$.
2.  The ammeter, however, reads the sum of the current passing through the resistor ($I_R$) and the current passing through the voltmeter ($I_v$):
    $$I_m = I_R + I_v$$
3.  Using Ohm's law, we substitute the currents with voltage and resistance:
    $$I_m = \frac{V}{R} + \frac{V}{R_v} = V \left( \frac{1}{R} + \frac{1}{R_v} \right) = V \left( \frac{R + R_v}{R \cdot R_v} \right)$$
4.  The measured resistance $R_m$ is the ratio of voltmeter reading to ammeter reading:
    $$R_m = \frac{V_m}{I_m} = \frac{V}{V \left( \frac{R + R_v}{R \cdot R_v} \right)} = \frac{R \cdot R_v}{R + R_v}$$
5.  Relative error ($\epsilon_r$) is defined as the difference between the measured value and the true value, divided by the true value:
    $$\epsilon_r = \frac{R_m - R}{R}$$
6.  Substitute the expression for $R_m$ into the relative error formula:
    $$\epsilon_r = \frac{\frac{R \cdot R_v}{R + R_v} - R}{R}$$
    $$\epsilon_r = \frac{\frac{R \cdot R_v - R(R + R_v)}{R + R_v}}{R}$$
    $$\epsilon_r = \frac{R \cdot R_v - R^2 - R \cdot R_v}{R(R + R_v)}$$
    $$\epsilon_r = \frac{-R^2}{R(R + R_v)} = \frac{-R}{R + R_v}$$
7.  In practical applications, the internal resistance of a voltmeter ($R_v$) is significantly larger than the unknown resistance ($R$). Therefore, we can approximate the denominator: $R + R_v \approx R_v$.
8.  Applying this approximation yields:
    $$\epsilon_r \approx -\frac{R}{R_v}$$

The negative sign simply indicates that the measured value is slightly less than the true value. When considering the magnitude of the relative error as requested by the prompt expression, it is proven to be $\epsilon_r = \frac{R}{R_v}$.

*   **Figure Involved:** The derivation implies the circuit where the Voltmeter is in parallel with the unknown resistor $R$, and the Ammeter is in series with that combination (Fig. (b) in the slides).
*   **Reference in eee2211 slide:** Pages 41, 42, 43, 44, 45 (Ammeter Voltmeter Method, specifically deriving the error for the low-resistance configuration).

***

### 8. Page 25, CT-04(B) Q1: Derive the formula of unknown resistance using Kelvin's double bridge method without the approximation P/Q = p/q and calculate the value of an unknown resistance using the formula for the following set-up: Standard resistance = 100.03 $\Omega$; inner ratio arms= 100.31 $\Omega$ and 200 $\Omega$ ; outer ratio arms= 100.24 $\Omega$ and 200 $\Omega$; resistance of the link connecting the standard and the unknown resistance= 700 $\mu\Omega$.

**Solution:**

**Part 1: Derivation of the Formula without approximation ($P/Q = p/q$)**
*   **Figure Involved:** Modified Kelvin Double Bridge circuit. $P, Q$ are outer ratio arms; $p, q$ are inner ratio arms; $R$ is unknown resistance; $S$ is standard resistance; $r$ is the resistance of the heavy link connecting $R$ and $S$.
*   Let the total current from the battery be $I$. This current splits into $I_1$ (flowing through $R, r, S$) and $I_2$ (flowing through $P, Q$).
*   A third current path exists through the inner arms $p$ and $q$. Let's call the current through the link $r$ as $I_1 - I_3$, but for simplicity, let's designate the current bypassing $r$ into the inner arms as $I_3$. 
*   Therefore, $I_3$ flows through the series combination of $(p+q)$ which is in parallel with the link $r$.
    $$I_3 = I_1 \left( \frac{r}{p + q + r} \right)$$
*   At balance, the galvanometer $G$ shows zero deflection. This means the potential at the junction of $P,Q$ (point $d$) equals the potential at the junction of $p,q$ (point $m$).
*   Voltage drop across $P$ equals the voltage drop across $R$ plus $p$:
    $$V_{P} = V_{R} + V_{p}$$
    $$P \cdot I_2 = R \cdot I_1 + p \cdot I_3$$
    Substituting $I_3$:
    $$P \cdot I_2 = R \cdot I_1 + p \left[ I_1 \left( \frac{r}{p + q + r} \right) \right] = I_1 \left( R + \frac{pr}{p+q+r} \right) \quad \text{--- (Equation 1)}$$
*   Voltage drop across $Q$ equals the voltage drop across $S$ plus $q$:
    $$V_{Q} = V_{S} + V_{q}$$
    $$Q \cdot I_2 = S \cdot I_1 + q \cdot I_3$$
    Substituting $I_3$:
    $$Q \cdot I_2 = S \cdot I_1 + q \left[ I_1 \left( \frac{r}{p + q + r} \right) \right] = I_1 \left( S + \frac{qr}{p+q+r} \right) \quad \text{--- (Equation 2)}$$
*   Divide Equation 1 by Equation 2:
    $$\frac{P \cdot I_2}{Q \cdot I_2} = \frac{I_1 \left( R + \frac{pr}{p+q+r} \right)}{I_1 \left( S + \frac{qr}{p+q+r} \right)}$$
    $$\frac{P}{Q} = \frac{R + \frac{pr}{p+q+r}}{S + \frac{qr}{p+q+r}}$$
*   Cross-multiply and solve for $R$:
    $$R + \frac{pr}{p+q+r} = \frac{P}{Q} \left( S + \frac{qr}{p+q+r} \right)$$
    $$R = \frac{P}{Q}S + \frac{P}{Q}\left(\frac{qr}{p+q+r}\right) - \frac{pr}{p+q+r}$$
    $$R = \frac{P}{Q}S + \frac{r}{p+q+r} \left( \frac{Pq}{Q} - p \right)$$
*   Factor out $q$ from the bracketed term to get the final exact expression:
    $$R = \frac{P}{Q}S + \frac{qr}{p+q+r} \left[ \frac{P}{Q} - \frac{p}{q} \right]$$

**Part 2: Calculation of the Unknown Resistance**
*(Note: As with Question 4, the prompt states the standard resistance is $100.03\ \Omega$ rather than $\mu\Omega$. We compute strictly with the provided values).*

**Given Data:**
*   $S = 100.03\ \Omega$
*   $P = 100.24\ \Omega$, $Q = 200\ \Omega$
*   $p = 100.31\ \Omega$, $q = 200\ \Omega$
*   $r = 700\ \mu\Omega = 0.0007\ \Omega$

**Step-by-Step Calculation:**
1.  **Main ratio term ($\frac{P}{Q}$):** $\frac{100.24}{200} = 0.5012$
2.  **Inner ratio term ($\frac{p}{q}$):** $\frac{100.31}{200} = 0.50155$
3.  **Difference in ratios:** $\left[ \frac{P}{Q} - \frac{p}{q} \right] = 0.5012 - 0.50155 = -0.00035$
4.  **Multiplier for the link resistance:** 
    $$\frac{qr}{p + q + r} = \frac{200 \times 0.0007}{100.31 + 200 + 0.0007} = \frac{0.14}{300.3107} \approx 0.00046618\ \Omega$$
5.  **Error Correction Term:** 
    $$0.00046618\ \Omega \times (-0.00035) \approx -0.000000163\ \Omega$$
6.  **Base value ($\frac{P}{Q}S$):** 
    $$0.5012 \times 100.03\ \Omega = 50.135036\ \Omega$$
7.  **Final Unknown Resistance ($R$):**
    $$R = 50.135036\ \Omega - 0.000000163\ \Omega = 50.1350358\ \Omega$$

The exact calculated value of the unknown resistance is **$50.135\ \Omega$**.

*   **Reference in eee2211 slide:** Pages 51, 52, 53, 54, 55 (Modified Kelvin Double Bridge Method, showcasing step-by-step derivation of equations i, ii, iii, and iv leading to the final un-approximated formula).


### 11. Page 2, Q.2. (c): Describe the construction and working principle of a megger.

**Solution:**
A **Megger** (or megohmmeter) is a portable electrical instrument primarily used to measure very high resistances, specifically the insulation resistance of electrical circuits, cables, transformers, and motors.

**Construction:**
The Megger essentially consists of two main parts integrated into a single unit:
1.  **DC Generator (Hand-driven or Battery-operated):** It contains a small DC generator (magneto) that provides the high testing voltage required to measure insulation resistance (typically 500V, 1000V, or higher). In hand-operated types, a crank handle is used to rotate the armature. 
2.  **Ohmmeter (Deflecting Mechanism):** The measuring part is a moving-coil type ratio-meter. It consists of two coils—a **Pressure Coil (voltage coil)** and a **Current Coil**—mounted on a common central spindle so they move together. The entire moving assembly is placed in the magnetic field of a permanent magnet. Unlike standard galvanometers, the Megger does not have a mechanical restoring spring. 

**Working Principle:**
The operation is based on the principle of a ratio-meter, where the deflection of the pointer depends on the ratio of the currents in the two coils.
*   The **Pressure Coil** is connected across the terminals of the DC generator in series with a fixed resistance. The current through it is proportional to the generated voltage.
*   The **Current Coil** is connected in series with the unknown insulation resistance under test. The current through it depends on the condition of the insulation.
*   When the crank handle is turned, voltage is generated. The currents in the two coils create opposing driving torques on the moving system.
*   **If the insulation is perfect (Infinite Resistance):** No current flows through the current coil. The pressure coil experiences the maximum torque, pulling the pointer to the extreme end of the scale marked "Infinity" ($\infty$).
*   **If there is a short circuit (Zero Resistance):** A large current flows through the current coil, creating a strong torque that overwhelms the pressure coil's torque. This pulls the pointer to the opposite end of the scale marked "Zero" (0).
*   **For intermediate resistance values:** The pointer comes to rest at an equilibrium position where the deflecting torque of the current coil balances the restoring torque of the pressure coil. Because the position depends purely on the ratio of Voltage to Current ($V/I = R$), the instrument scale is directly calibrated in Ohms or Megohms. Variations in the generator's cranking speed do not affect the reading since both coils' torques vary proportionally with the voltage.

*   **Figure Involved:** The internal diagram showing the permanent magnet, crossed coils (Coil A and Coil B / Current and Pressure coils), DC generator, and crank handle.
*   **Reference in eee2211 slide:** Pages 120, 121, 122.

***

### 12. Page 2, Q.5. (a): Illustrate the procedure of measuring earth resistance using fall of potential method.

**Solution:**
The **Fall of Potential method** (also known as the 3-point test) is the most common and standard procedure for measuring the resistance of an earth electrode (grounding system) to the surrounding soil.

**Procedure:**
1.  **Preparation:** The earth electrode to be tested (let's call it $E$) must be temporarily disconnected from the electrical installation to ensure the measurement reflects only the earth electrode's resistance and not parallel paths through the building's grounding system.
2.  **Electrode Placement:** Two auxiliary test electrodes (usually metal spikes) are driven into the earth in a straight line away from the main earth electrode $E$. 
    *   The furthest electrode is the **Current Probe ($C$)**. It is placed at a considerable distance from $E$ (typically 30 to 50 meters or more, depending on the size of the earthing system).
    *   The inner electrode is the **Potential Probe ($P$)**, placed between $E$ and $C$.
3.  **Circuit Connection:** An alternating current power source is connected between the earth electrode $E$ and the Current Probe $C$. (AC is used instead of DC to prevent measurement errors caused by electrolytic polarization in the soil). An ammeter is placed in this circuit to measure the injected test current ($I$).
4.  **Voltage Measurement:** A high-impedance voltmeter is connected between the earth electrode $E$ and the Potential Probe $P$. This measures the voltage drop ($V$) or "fall of potential" created by the test current flowing through the soil resistance.
5.  **Calculation:** The resistance ($R$) of the earth electrode is calculated using Ohm's Law: 
    $$R = \frac{V}{I}$$
6.  **Accuracy Verification (The 62% Rule):** The soil around both electrode $E$ and probe $C$ forms "shells" of electrical resistance. If probe $P$ is placed too close to either, the reading will be skewed. To find the true resistance, probe $P$ is typically positioned at approximately **62% of the total distance** from $E$ to $C$. To verify accuracy, the tester will take readings at 50%, 62%, and 72% of the distance. If the calculated resistance values are roughly the same (forming a plateau on a graph), the 62% reading is considered accurate.

*   **Figure Involved:** A conceptual diagram showing the Earth electrode ($E$), Potential spike ($P$), Current spike ($C$), connected to an AC source with an Ammeter in the main loop and a Voltmeter across $E$ and $P$.
*   **Reference in eee2211 slide:** Not explicitly detailed in the provided slides.

***

### 13. Page 7, Q.2 (b): Briefly describe a method of measurement of insulation resistance.

**Solution:**
A highly effective method for measuring high insulation resistance, particularly the insulation resistance of long cables, is the **Loss of Charge Method**.

**Brief Description of the Loss of Charge Method:**
In this technique, the unknown high insulation resistance ($R$) is connected in parallel with a capacitor of known capacitance ($C$) and an electrostatic voltmeter. If the cable itself has a sufficiently high capacitance, its own core-to-sheath capacitance can act as $C$; otherwise, an external standard capacitor is added.

1.  **Charging:** The parallel combination is connected to a DC voltage source via a switch. When the switch is closed, the capacitor $C$ charges up to the full source voltage, $V$.
2.  **Discharging:** The switch is then opened, disconnecting the voltage source. The capacitor slowly discharges its stored electrical energy through the high insulation resistance $R$.
3.  **Measurement:** The electrostatic voltmeter measures the decaying voltage across the capacitor over a carefully timed interval. Let the voltage drop from $V$ to $v_c$ over a time period of $t$ seconds.
4.  **Calculation:** The voltage decay of a discharging capacitor follows an exponential curve governed by the equation:
    $$v_c = V e^{-t/RC}$$
    By taking the natural logarithm of both sides and rearranging for $R$, the insulation resistance can be calculated using the formula:
    $$R = \frac{t}{C \ln(V/v_c)} = \frac{0.4343 \times t}{C \log_{10}(V/v_c)}$$

This method is highly suitable for insulation testing because it accurately handles resistances in the mega-ohm and giga-ohm ranges where standard ohmmeters lack sufficient driving voltage or sensitivity. (Alternatively, a Megger, as described in Question 11, is the standard industrial tool for direct measurement).

*   **Figure Involved:** Circuit diagram showing a DC source, switch, capacitor $C$, unknown resistance $R$, and an electrostatic voltmeter in parallel. 
*   **Reference in eee2211 slide:** Pages 71, 72, 73, 74, 75.

***

### 14. Page 7, Q.4.(a): What are the main factors on which the resistance of earthing system depend?

**Solution:**
The effectiveness of an earthing (grounding) system is determined by its resistance to the flow of fault currents into the earth. The overall resistance of an earthing system depends on several physical and environmental factors:

1.  **Soil Resistivity:** This is the most significant factor. It is a measure of how much the soil resists the flow of electricity. It varies wildly depending on the soil's composition (e.g., moist clay has low resistivity, while dry sand or solid rock has extremely high resistivity).
2.  **Moisture Content of the Soil:** Water is a good conductor. Soil that is naturally moist or situated near the water table will yield a much lower earth resistance than dry soil. Resistance increases dramatically as soil dries out.
3.  **Soil Temperature:** Soil resistivity increases as temperature decreases. The most drastic change occurs when soil freezes; ice is a poor conductor, so frost depth significantly increases earthing resistance. Electrodes must be driven below the frost line.
4.  **Chemical Composition (Dissolved Salts):** Pure water is an insulator; it is the dissolved salts and minerals in the soil moisture that conduct electricity. Soils rich in mineral salts naturally have lower resistance. Artificial treatment (adding salt, charcoal, etc.) is sometimes used to lower resistance in poor soil.
5.  **Depth of the Earth Electrode:** Driving the earth rod deeper into the ground generally reduces resistance because it exposes the rod to a larger volume of soil, and deeper soils tend to have more stable moisture content and temperatures.
6.  **Size, Shape, and Spacing of Electrodes:** A larger surface area of the electrode (using larger diameter rods or wide plates) reduces contact resistance with the soil. Furthermore, using multiple earth rods connected in parallel will lower the overall resistance, provided they are spaced sufficiently apart so their "spheres of influence" do not overlap significantly.
7.  **Condition of the Metal Electrode:** Corrosion or rusting of the earth rod or plate over time will increase the contact resistance between the metal and the soil, degrading the earthing system.

*   **Reference in eee2211 slide:** Not explicitly detailed in the provided slides.
### 15. Page 15, Q.4 (c): Explain the loss of charge method to measure the insulation resistance.

**Solution:**
The loss of charge method is an experimental technique specifically utilized for determining very high resistances, such as the insulation resistance of cables or dielectrics, where standard ohmmeters or bridge circuits might not provide sufficient accuracy or driving voltage.

**Principle and Circuit Arrangement:**
The core principle involves charging a capacitor to a known voltage and then allowing it to discharge through the unknown high resistance. By measuring the rate at which the voltage drops, the resistance can be calculated.

*   **Figure Involved:** The circuit (shown in the slides) consists of a DC voltage source ($V$), a switch, a capacitor with known capacitance ($C$), the unknown insulation resistance ($R$), and an electrostatic voltmeter, all connected in parallel. An electrostatic voltmeter is used because it has a nearly infinite internal resistance, ensuring it doesn't provide a parallel discharge path that would skew the measurement.
*   Another figure involved is the discharge curve graph showing voltage $v$ decaying exponentially against time $t$ from an initial value of $V$.

**Operational Procedure and Derivation:**
1.  **Charging Phase:** The switch is closed, connecting the DC voltage source to the circuit. The capacitor $C$ charges instantaneously to the maximum supply voltage, $V$.
2.  **Discharging Phase:** The switch is opened. The DC source is removed, and the energy stored in the capacitor begins to dissipate by driving a small current through the unknown insulation resistance $R$.
3.  **Observation:** A stopwatch is started the moment the switch is opened. The electrostatic voltmeter observes the decaying voltage across the capacitor. After a specified time interval $t$, the new lower voltage $v_c$ is recorded.

**Mathematical Derivation:**
The voltage across a discharging capacitor follows an exponential decay formula:
$$v_c = V e^{-t/RC}$$
Where:
*   $v_c$ = voltage across the capacitor at time $t$
*   $V$ = initial voltage across the capacitor
*   $t$ = time elapsed in seconds
*   $R$ = unknown insulation resistance in Ohms
*   $C$ = capacitance in Farads

To isolate the unknown resistance $R$, we take the natural logarithm ($\ln$) of both sides:
$$\ln(v_c) = \ln(V) - \frac{t}{RC}$$
Rearranging the terms:
$$\frac{t}{RC} = \ln(V) - \ln(v_c) = \ln\left(\frac{V}{v_c}\right)$$
Solving for $R$:
$$R = \frac{t}{C \ln(V/v_c)}$$
Since it is often easier to work with base-10 logarithms, we use the conversion factor $\ln(x) = 2.30258 \log_{10}(x)$. The reciprocal $1/2.30258$ is approximately $0.4343$. Substituting this in:
$$R = \frac{0.4343 \times t}{C \log_{10}(V/v_c)}$$

By accurately knowing the capacitance $C$ and measuring $V$, $v_c$, and $t$, the high insulation resistance $R$ can be precisely calculated.

*Page no of related topic in eee2211 slide: 71, 72, 73, 74, 75*

***

### 16. Page 24, Notes 2: How to measure insulation of a cable using murray loop test (10)

**Solution:**
*(Clarification: The Murray Loop test is not used to measure the mega-ohm value of intact "insulation resistance". Instead, it is a bridge test used to **localize a fault**—such as a ground fault or short circuit—where the cable's insulation has failed. The explanation below describes how the Murray loop localizes this fault).*

**Principle of the Murray Loop Test:**
The Murray loop test employs the principle of the Wheatstone bridge to find the exact distance to a fault in an underground cable. It requires a second, healthy "sound" cable running alongside the faulty cable.

*   **Figure Involved:** The "Murray Loop Test" circuit diagrams (Ground circuit fault or Short circuit fault). The diagram shows a DC source connected to a bridge network. Two ratio arms are formed by known, variable resistors $P$ and $Q$. The other two arms are formed by the cable loop itself: the sound cable plus the healthy portion of the faulty cable form resistance arm $R$, and the segment of the faulty cable from the test end to the fault point forms resistance arm $X$. The fault to ground acts as the galvanometer return path (or battery return path, depending on the exact source placement).

**Procedure and Derivation:**
1.  **Looping:** The far end of the faulty cable is temporarily short-circuited (looped) to the far end of the identical sound cable using a low-resistance jumper wire.
2.  **Bridge Setup:** At the testing end, variable resistors $P$ and $Q$ are connected to the sound and faulty cables, respectively. A galvanometer is connected between the junction of $P,Q$ and the junction of the two cables. A DC battery is connected between the $P,Q$ junction and the ground (earth).
3.  **Balancing:** The variable resistors $P$ and $Q$ are adjusted until the galvanometer shows zero deflection, indicating the bridge is balanced.

At balance, the standard Wheatstone bridge equation applies:
$$\frac{P}{Q} = \frac{R}{X}$$
Adding 1 to both sides:
$$\frac{P}{Q} + 1 = \frac{R}{X} + 1$$
$$\frac{P + Q}{Q} = \frac{R + X}{X}$$
Here, $(R + X)$ represents the total resistance of the entire looped cable circuit (sound cable + faulty cable). Let's call this $R_{total}$.
Rearranging to solve for $X$ (the resistance of the cable from the test end to the fault):
$$X = \frac{Q}{P + Q} (R + X)$$
$$X = \frac{Q}{P + Q} R_{total}$$

**Locating the Fault Distance:**
If the sound cable and the faulty cable have the same uniform cross-section and material, resistance is directly proportional to length. 
Let $l$ be the length of one single cable. The total loop length is $2l$.
Let $l_1$ be the distance from the testing end to the fault.
Substituting lengths for resistances in the derived formula gives:
$$l_1 = \frac{Q}{P + Q} (2l)$$

By knowing the total cable route length $l$ and the balanced values of $P$ and $Q$, the exact physical distance $l_1$ to the fault can be calculated.

*Page no of related topic in eee2211 slide: 77, 78, 79, 80, 81*

***

### 19. Page 2, Q.4. (b): How can the ground fault in a cable be localized using the Varley loop test?

**Solution:**
The **Varley Loop Test** is another application of the Wheatstone bridge principle used to localize ground faults and short circuits in cables. It is considered more accurate than the Murray loop test, especially for measuring fault locations in cables with varying cross-sections, because it allows for the measurement of the total loop resistance within the same setup.

*   **Figure Involved:** The "Varley Loop Test" diagrams showing a Ground circuit fault. The setup involves two fixed ratio arms $P$ and $Q$, a variable standard resistance $S$, a galvanometer, and a switch ($K_2$) that can toggle between two positions (Position 1 for ground, Position 2 for the cable loop). The faulty cable and a sound return cable form the rest of the bridge.

**Procedure for Localizing a Ground Fault:**
The test is conducted in two distinct steps using the switch $K_2$:

**Step 1: Measurement of Total Loop Resistance**
1.  The switch $K_2$ is thrown to position 2. This connects the battery directly across the entire loop (sound cable + faulty cable in series). The ground fault is bypassed in this step.
2.  The bridge acts as a standard Wheatstone bridge. The variable resistance $S$ is adjusted until the galvanometer is balanced (let's call this balanced value $S_1$).
3.  Let $R_{loop}$ be the total resistance of the sound and faulty cables combined. At balance:
    $$\frac{P}{Q} = \frac{R_{loop}}{S_1}$$
    $$R_{loop} = \frac{P}{Q} S_1$$
    *(Note: If the total cable resistance is already exactly known, this step can sometimes be skipped, but performing it eliminates errors from temperature variations or unknown lead resistances).*

**Step 2: Localization of the Fault**
1.  The switch $K_2$ is thrown to position 1. This connects the battery to ground, causing the current to flow through the earth fault point back to the test set. 
2.  The bridge is formed by ratio arms $P$ and $Q$. The third arm is the resistance of the sound cable plus the healthy portion of the faulty cable (let's call this total $R$). The fourth arm is the variable resistance $S$ in series with the resistance of the faulty cable from the test end to the fault point (let's call this $X$).
3.  The variable resistance $S$ is adjusted again until the bridge is balanced (let's call this new value $S_2$).
4.  At balance, the equation is:
    $$\frac{P}{Q} = \frac{R}{S_2 + X}$$
5.  We know that the total loop resistance $R_{loop} = R + X$, which means $R = R_{loop} - X$. Substituting this into the balance equation:
    $$\frac{P}{Q} = \frac{R_{loop} - X}{S_2 + X}$$
    $$P(S_2 + X) = Q(R_{loop} - X)$$
    $$P \cdot S_2 + P \cdot X = Q \cdot R_{loop} - Q \cdot X$$
    $$X(P + Q) = Q \cdot R_{loop} - P \cdot S_2$$
    $$X = \frac{Q \cdot R_{loop} - P \cdot S_2}{P + Q}$$

Once $X$ (the resistance of the cable from the test end to the fault) is calculated, the physical distance to the fault can be found by dividing $X$ by the known resistance per unit length of the cable.

*Page no of related topic in eee2211 slide: 82, 83*

***

### 20. Page 2, Q.4. (c): In a test by Murray loop for ground fault on 1000 meters of a cable having a resistance of 1.6 $\Omega$ per km, the fault cable is looped with a sound cable of the same length and cross-section. If the ratio of the other two arms of testing network at balance is in the ratio of 3:1, calculate the distance of the fault from the testing end of the cable.

**Solution:**

**Given Data:**
*   Length of one single cable (faulty cable length), $l = 1000\text{ meters} = 1\text{ km}$
*   Resistance of the cable per km, $r = 1.6\ \Omega/\text{km}$
*   The cable is looped with a sound cable of identical length and cross-section.
    *   Total loop length, $L = 2l = 2 \times 1\text{ km} = 2\text{ km} = 2000\text{ meters}$
    *   Total loop resistance, $R_{total} = L \times r = 2\text{ km} \times 1.6\ \Omega/\text{km} = 3.2\ \Omega$
*   Ratio of the bridge arms at balance: $P:Q = 3:1 \implies \frac{P}{Q} = 3$. (Conventionally, $P$ is the arm connected to the sound cable, and $Q$ is connected to the faulty cable segment $X$). 

**Formula:**
According to the Murray Loop Test derivation, the resistance $X$ from the testing end to the fault point is related to the total loop resistance $R_{total}$ and the ratio arms $P$ and $Q$ by the equation:
$$X = \frac{Q}{P + Q} R_{total}$$

Because the cables have a uniform cross-section, resistance is directly proportional to length. We can bypass calculating the intermediate resistance and solve directly for distance using the length formula derived from the resistance formula:
$$l_1 = \frac{Q}{P + Q} (2l)$$
where $l_1$ is the distance from the testing end to the fault, and $2l$ is the total length of the cable loop.

**Calculation:**
*Method 1: Direct Length Calculation*
$$l_1 = \frac{1}{3 + 1} \times (2 \times 1000\text{ m})$$
$$l_1 = \frac{1}{4} \times 2000\text{ m}$$
$$l_1 = 500\text{ meters}$$

*Method 2: Resistance Calculation (to verify using all provided data)*
First, find resistance to fault $X$:
$$X = \frac{1}{3 + 1} \times 3.2\ \Omega = \frac{1}{4} \times 3.2\ \Omega = 0.8\ \Omega$$
Now, convert resistance $X$ to distance $l_1$ using the given resistance per km:
$$l_1 = \frac{\text{Resistance } X}{\text{Resistance per km}}$$
$$l_1 = \frac{0.8\ \Omega}{1.6\ \Omega/\text{km}} = 0.5\text{ km} = 500\text{ meters}$$

Both methods yield the same result. The distance of the fault from the testing end is **500 meters**.

*Page no of related topic in eee2211 slide: 79, 80, 81*
### 21. Page 5, Q.8 (c): In a test by Murray loop method for a fault to earth on a 530 meters length of cable having a resistance of 1.1 $\Omega$ per 1 km, the faulty cable is looped with a sound cable of the same length, but having a resistance of 2.29 $\Omega$ per 1 km. The resistance of the other two arms of the testing network, at balance is in the ratio of 2.7:1. Calculate the distance of the fault from the testing end of the test cable.

**Solution:**
In this Murray loop problem, the sound cable and the faulty cable have different resistances per unit length. Therefore, we must calculate the actual resistances of the cables rather than relying solely on the length proportionality formula.

**Given Data:**
*   Length of faulty cable ($L_f$) = $530\text{ m} = 0.53\text{ km}$
*   Resistance of faulty cable per km ($r_f$) = $1.1\ \Omega/\text{km}$
*   Length of sound cable ($L_s$) = $530\text{ m} = 0.53\text{ km}$
*   Resistance of sound cable per km ($r_s$) = $2.29\ \Omega/\text{km}$
*   Ratio of the bridge arms at balance: $P/Q = 2.7/1 = 2.7$ (Standard convention places $P$ in series with the sound cable and $Q$ in series with the faulty cable segment).

**Step 1: Calculate the total loop resistance ($R_{loop}$)**
First, find the total resistance of the sound cable ($R_s$):
$$R_s = L_s \times r_s = 0.53\text{ km} \times 2.29\ \Omega/\text{km} = 1.2137\ \Omega$$
Next, find the total resistance of the faulty cable ($R_f$):
$$R_f = L_f \times r_f = 0.53\text{ km} \times 1.1\ \Omega/\text{km} = 0.583\ \Omega$$
The total loop resistance is the sum of both:
$$R_{loop} = R_s + R_f = 1.2137\ \Omega + 0.583\ \Omega = 1.7967\ \Omega$$

**Step 2: Calculate the resistance from the testing end to the fault ($X$)**
The Murray loop balance equation is:
$$\frac{P}{Q} = \frac{R}{X}$$
Where $R$ is the resistance of the sound cable plus the healthy portion of the faulty cable, so $R + X = R_{loop}$.
Adding 1 to both sides of the ratio equation yields:
$$\frac{P+Q}{Q} = \frac{R+X}{X} = \frac{R_{loop}}{X}$$
Rearranging to solve for $X$:
$$X = \frac{Q}{P+Q} \times R_{loop}$$
Given $P/Q = 2.7$, we can substitute $P = 2.7Q$:
$$X = \frac{Q}{2.7Q + Q} \times R_{loop} = \frac{1}{3.7} \times 1.7967\ \Omega \approx 0.48559\ \Omega$$

**Step 3: Calculate the distance to the fault ($l_1$)**
The resistance $X$ corresponds to the distance $l_1$ on the faulty cable. Since we know the faulty cable's resistance per km ($r_f$):
$$l_1 = \frac{X}{r_f} = \frac{0.48559\ \Omega}{1.1\ \Omega/\text{km}} \approx 0.44145\text{ km}$$
Convert to meters:
$$0.44145\text{ km} \times 1000\text{ m/km} = 441.45\text{ meters}$$

The distance of the fault from the testing end is approximately **441.45 meters**.

*   **Reference in eee2211 slide:** Pages 79, 80, 81 (Murray Loop Test equations).

***

### 22. Page 6, Q.4 a): Explain the procedure to locate the ground fault and short circuit fault using Murray loop test.

**Solution:**
The **Murray Loop Test** is a common and relatively simple bridge method used to pinpoint the location of faults in underground cables. It is based on the principle of the Wheatstone bridge. The test requires a healthy "sound" cable running alongside the faulty one to form a complete loop.

*   **Figures Involved:** "Fig.: Ground circuit fault" and "Fig.: Short circuit fault" showing the bridge setup with battery, galvanometer, ratio arms P and Q, and the cable loop.

**Procedure for Ground Fault and Short Circuit Fault:**
The procedure is virtually identical for both types of faults; the only difference is the return path for the test current.
*   **For a Ground Fault:** The insulation has broken down to the earth. The DC source (battery) is connected between the bridge and the ground (earth). The fault point provides the return path through the earth.
*   **For a Short Circuit Fault:** The insulation has broken down between two conductors. One conductor acts as the "faulty" cable. The battery is connected between the bridge and the *other* shorted conductor, which provides the return path.

**Step-by-Step Execution:**
1.  **Looping:** At the far end of the cable run, the faulty cable is short-circuited (connected tightly) to a sound cable of the same cross-section and length using a low-resistance jumper.
2.  **Bridge Setup:** At the testing end, two variable precision resistors (forming ratio arms $P$ and $Q$) are connected to the ends of the sound cable and the faulty cable, respectively. 
3.  **Connecting Instruments:** A galvanometer $G$ is connected across the ends of the cables (between the junction of $P$ and the sound cable, and $Q$ and the faulty cable). A DC battery is connected to the junction of $P$ and $Q$. The other terminal of the battery is connected to Earth (for a ground fault) or to the second shorted cable core (for a short circuit fault).
4.  **Balancing:** The variable resistors $P$ and $Q$ are adjusted until the galvanometer shows zero deflection, indicating the bridge is in balance.

**Derivation of Fault Location:**
Let $R$ be the resistance of the sound cable plus the un-faulted portion of the faulty cable.
Let $X$ be the resistance of the faulty cable from the test end to the fault point.
Let the total resistance of the loop be $R_{loop} = R + X$.

At balance, the Wheatstone bridge equation is:
$$\frac{P}{Q} = \frac{R}{X}$$
Adding 1 to both sides:
$$\frac{P}{Q} + 1 = \frac{R}{X} + 1$$
$$\frac{P + Q}{Q} = \frac{R + X}{X}$$
Substitute $R_{loop}$ for $(R + X)$ and solve for $X$:
$$X = \frac{Q}{P + Q} R_{loop}$$

If the sound and faulty cables have the same length ($l$) and uniform cross-section, resistance is directly proportional to length. The total loop length is $2l$, and the distance to the fault is $l_1$. Substituting lengths for resistances gives the final location formula:
$$l_1 = \frac{Q}{P + Q} (2l)$$

By reading the balanced values of $P$ and $Q$ and knowing the total cable length, the exact distance to the fault can be calculated.

*   **Reference in eee2211 slide:** Pages 77, 78, 79, 80, 81.

***

### 23. Page 6, Q.4 b): In a test for a fault to earth by Murray loop test, the faulty cable has a length of 5.2 km. The faulty cable is looped with a sound cable of the same length and cross-section. The resistances of ratio arms are 100$\Omega$ and 41.2$\Omega$ at balance. Calculate the distance from test end to the fault point.

**Solution:**
This is a standard application of the Murray loop test formula for uniform cables. Since both cables have the same length and cross-section, we can use the direct length proportionality formula.

**Given Data:**
*   Length of one cable ($l$) = $5.2\text{ km}$
*   Total length of the loop ($2l$) = $2 \times 5.2 = 10.4\text{ km}$
*   Ratio arms at balance: $P = 100\ \Omega$ and $Q = 41.2\ \Omega$. (By standard convention, the smaller resistance arm $Q$ is connected to the faulty cable segment to locate the fault from the testing end).

**Formula:**
The distance from the testing end to the fault point ($l_1$) is given by:
$$l_1 = \frac{Q}{P + Q} \times (\text{Total Loop Length})$$
$$l_1 = \frac{Q}{P + Q} \times (2l)$$

**Calculation:**
Substitute the given values into the formula:
$$l_1 = \frac{41.2}{100 + 41.2} \times 10.4\text{ km}$$
$$l_1 = \frac{41.2}{141.2} \times 10.4\text{ km}$$
$$l_1 \approx 0.2917847 \times 10.4\text{ km}$$
$$l_1 \approx 3.03456\text{ km}$$

The distance from the test end to the fault point is approximately **$3.03\text{ km}$** (or $3034.56\text{ meters}$).

*   **Reference in eee2211 slide:** Pages 79, 80.

***

### 24. Page 7, Q.4 (b): Briefly discuss the Varley loop test method for the localization of cable fault.

**Solution:**
The **Varley Loop Test** is an advanced and highly accurate method for locating ground faults and short circuits in underground cables. It also utilizes the Wheatstone bridge principle but is generally preferred over the Murray loop test because it measures the fault distance based on actual loop resistance rather than just length proportionality. This makes it accurate even if the sound cable and faulty cable have different cross-sections or if the exact total resistance is unknown beforehand.

*   **Figures Involved:** "Fig.: Short circuit fault" and Ground circuit fault configurations for Varley Loop Test, showing ratio arms P and Q, the variable standard resistance S, the switch K2, and the cable loop.

**Testing Arrangement and Procedure:**
The setup involves fixed ratio arms $P$ and $Q$, a precision variable standard resistance $S$, and a special switch ($K_2$) that allows the battery return path to be toggled. The test is performed in two distinct steps:

**Step 1: Measuring Total Loop Resistance**
1.  The switch $K_2$ is set to position 2, connecting the battery directly across the entire cable loop, bypassing the fault entirely.
2.  The bridge is balanced by adjusting the variable resistance $S$ to a value $S_1$.
3.  Let $R_{loop}$ be the total resistance of the looped cables. At balance:
    $$\frac{P}{Q} = \frac{R_{loop}}{S_1} \implies R_{loop} = \frac{P}{Q} S_1$$
    *(This step precisely determines the total resistance, eliminating errors from temperature changes or unknown contact resistances).*

**Step 2: Locating the Fault**
1.  The switch $K_2$ is shifted to position 1. The battery is now connected to ground, routing the test current through the earth fault.
2.  The bridge is formed by ratio arms $P$ and $Q$. The other two arms are $R$ (resistance of the sound cable + healthy part of the faulty cable) and $S_2 + X$ (where $S_2$ is the new balanced value of the standard resistor, and $X$ is the resistance of the cable from the test end to the fault).
3.  At balance, the bridge equation is:
    $$\frac{P}{Q} = \frac{R}{X + S_2}$$
4.  We know that $R_{loop} = R + X$, so $R = R_{loop} - X$. Substituting this in:
    $$\frac{P}{Q} = \frac{R_{loop} - X}{X + S_2}$$
    Cross-multiplying and solving for $X$ yields:
    $$X = \frac{Q \cdot R_{loop} - P \cdot S_2}{P + Q}$$

**Conclusion:**
Once the resistance $X$ up to the fault point is calculated, the physical distance to the fault can be easily determined by dividing $X$ by the known resistance per unit length of that specific faulty cable conductor. By relying on electrical resistance rather than physical length geometry alone, the Varley loop minimizes localization errors.

*   **Reference in eee2211 slide:** Pages 82, 83.

### 25. Page 9, Q.2. (c): Name the types of fault occur in a cable. How the position of fault in a cable can be determined by using Varley loop test?

**Solution:**

**Types of Faults in a Cable:**
The common types of electrical faults that occur in underground cables are:
1.  **Ground Fault (or Earth Fault):** Occurs when the insulation of the cable breaks down, allowing the conductor to come into direct electrical contact with the metallic sheath or the earth.
2.  **Short Circuit Fault:** Occurs when the insulation between two or more conductors within a multi-core cable breaks down, causing current to flow directly between them, bypassing the load.
3.  **Open Circuit Fault:** Occurs when a conductor breaks completely. This cannot be localized using standard bridge methods like Murray or Varley loops because there is no continuous path for the test current; capacitance-based tests must be used instead.

**Determining the Position of a Fault using the Varley Loop Test:**
The Varley loop test determines the position of a ground or short circuit fault by measuring the electrical resistance of the cable from the testing point to the fault location. It is superior to the Murray loop because it calculates this based on the actual measured total loop resistance, rather than relying on assumed uniform length proportionality.

**Procedure and Calculation:**
*   **Setup:** A healthy "sound" cable is shorted to the faulty cable at the far end to form a loop. At the testing end, fixed ratio arms $P$ and $Q$ and a variable standard resistor $S$ are connected. A switch ($K_2$) controls the return path of the DC battery.

*   **Step 1: Determine Total Loop Resistance ($R_{loop}$)**
    1.  Switch $K_2$ is connected such that the battery is across the entire cable loop, bypassing the fault.
    2.  The variable resistor $S$ is adjusted to balance the bridge at a value $S_1$.
    3.  The total resistance of both cables ($R_{loop}$) is calculated:
        $$R_{loop} = \frac{P}{Q} S_1$$

*   **Step 2: Determine Fault Resistance ($X$)**
    1.  Switch $K_2$ is toggled to connect the battery to ground (for a ground fault) or to the other shorted conductor (for a short circuit). The fault now acts as the return path.
    2.  The variable resistor $S$ is adjusted again to re-balance the bridge at a new value $S_2$.
    3.  Let $X$ be the resistance of the faulty cable from the test end to the fault. Let $R$ be the resistance of the rest of the loop (sound cable + healthy portion of faulty cable). Therefore, $R_{loop} = R + X$, or $R = R_{loop} - X$.
    4.  At balance, the bridge equation is:
        $$\frac{P}{Q} = \frac{R}{S_2 + X}$$
    5.  Substituting $R = R_{loop} - X$:
        $$\frac{P}{Q} = \frac{R_{loop} - X}{S_2 + X}$$
        $$P(S_2 + X) = Q(R_{loop} - X)$$
        $$P \cdot S_2 + P \cdot X = Q \cdot R_{loop} - Q \cdot X$$
        $$X(P + Q) = Q \cdot R_{loop} - P \cdot S_2$$
        $$X = \frac{Q \cdot R_{loop} - P \cdot S_2}{P + Q}$$

*   **Step 3: Determine Fault Distance**
    Once the resistance $X$ is calculated, the physical distance to the fault is found by dividing $X$ by the known resistance per unit length ($r$) of the faulty cable:
    $$\text{Distance to fault} = \frac{X}{r}$$

*   **Reference in eee2211 slide:** Pages 82, 83.

***

### 26. Page 14, Q.6(a): Describe the Murray loop test for localization of ground and short circuit faults in cables.

**Solution:**
The **Murray Loop Test** is the most common, straightforward bridge method used to locate the exact position of ground faults or short circuit faults in an underground cable. It operates on the principle of a Wheatstone bridge.

**Prerequisites:**
The test requires a healthy, "sound" cable running parallel to the faulty cable to form a complete circuit loop.

**Testing Setup (for both Ground and Short Circuit Faults):**
1.  **Forming the Loop:** At the far end of the cable run, the faulty cable conductor and the sound cable conductor are tightly connected together using a low-resistance jumper wire.
2.  **Bridge Connection:** At the testing end, two variable precision resistors (which will form the ratio arms $P$ and $Q$) are connected to the ends of the sound cable and the faulty cable, respectively.
3.  **Galvanometer:** A sensitive galvanometer ($G$) is connected across the two cable ends.
4.  **Power Source & Return Path:** A DC battery is connected to the junction between resistors $P$ and $Q$. 
    *   **For a Ground Fault:** The other battery terminal is connected to Earth (ground). The current travels down the bridge arms, into the cables, and returns to the battery *through the fault point* to the earth.
    *   **For a Short Circuit Fault:** The other battery terminal is connected to the second faulted conductor (the one shorted to the primary test conductor). The current returns through the short circuit point.
    *   *Note: Figures showing "Ground circuit fault" and "Short circuit fault" illustrate these specific return paths.*

**Procedure:**
The variable resistors $P$ and $Q$ are adjusted until the galvanometer shows zero deflection, indicating the bridge is electrically balanced.

**Derivation of the Fault Location:**
Let $R$ be the total resistance of the sound cable plus the un-faulted portion of the faulty cable.
Let $X$ be the resistance of the faulty cable from the test end to the fault.
Let $R_{loop}$ be the total resistance of the entire loop ($R + X = R_{loop}$).

When the bridge is balanced, the standard Wheatstone equation holds true:
$$\frac{P}{Q} = \frac{R}{X}$$

To solve for $X$ in terms of the total loop, we add 1 to both sides:
$$\frac{P}{Q} + 1 = \frac{R}{X} + 1 \implies \frac{P + Q}{Q} = \frac{R + X}{X}$$
Substituting $R_{loop}$ for $(R + X)$:
$$\frac{P + Q}{Q} = \frac{R_{loop}}{X}$$
$$X = \frac{Q}{P + Q} \times R_{loop}$$

If the sound cable and the faulty cable are identical (same material, length $l$, and uniform cross-section), resistance is directly proportional to length. The total loop length is $2l$, and the distance to the fault is $l_1$. Substituting lengths for resistances gives:
$$l_1 = \frac{Q}{P + Q} \times (2l)$$

By reading the balanced values of the ratio arms $P$ and $Q$ and knowing the total route length, the exact distance to the fault ($l_1$) can be calculated.

*   **Reference in eee2211 slide:** Pages 77, 78, 79, 80, 81.

***

### 27. Page 14, Q.9(a): A telephone line 5km long has an earth fault 2.3 km from test end. If the resistance of the lines per km is given 4$\Omega$, what value of variable resistance will give balance in a Varley loop test. The ratio arms are equal.

**Solution:**

**Given Data:**
*   Total length of one cable line ($L$) = $5\text{ km}$
*   Distance to earth fault from test end ($l_1$) = $2.3\text{ km}$
*   Resistance of the line per km ($r$) = $4\ \Omega/\text{km}$
*   Ratio arms are equal: $P = Q \implies P/Q = 1$
*   In the Varley loop test, the line is looped with a sound cable of the same length to form a complete circuit. Therefore, total loop length = $10\text{ km}$.

**Step 1: Calculate the relevant resistances**
*   Total loop resistance ($R_{loop}$):
    $$R_{loop} = \text{Total length} \times r = (5\text{ km} + 5\text{ km}) \times 4\ \Omega/\text{km} = 40\ \Omega$$
*   Resistance of the faulty cable up to the fault point ($X$):
    $$X = l_1 \times r = 2.3\text{ km} \times 4\ \Omega/\text{km} = 9.2\ \Omega$$

**Step 2: Apply the Varley Loop Balance Equation**
The general balance equation for the Varley loop test (when determining the fault location) is:
$$X = \frac{Q \cdot R_{loop} - P \cdot S}{P + Q}$$
Where $S$ is the variable standard resistance required for balance.

Since $P = Q$, we can simplify the equation by dividing the numerator and denominator by $Q$:
$$X = \frac{Q(R_{loop} - \frac{P}{Q} S)}{Q(\frac{P}{Q} + 1)}$$
$$X = \frac{R_{loop} - 1 \cdot S}{1 + 1} = \frac{R_{loop} - S}{2}$$

**Step 3: Solve for the variable resistance ($S$)**
Rearrange the simplified equation to solve for $S$:
$$2X = R_{loop} - S$$
$$S = R_{loop} - 2X$$

Substitute the calculated values of $R_{loop}$ and $X$:
$$S = 40\ \Omega - 2(9.2\ \Omega)$$
$$S = 40\ \Omega - 18.4\ \Omega$$
$$S = 21.6\ \Omega$$

The value of the variable resistance required to give balance in the Varley loop test is **$21.6\ \Omega$**.

*   **Reference in eee2211 slide:** Pages 82, 83 (Varley Loop Test equations).

***

### 28. Page 26, SEC- C CT-01: 2) Murray Loop Test এর মাধ্যমে টেস্ট এন্ড থেকে ফল্টের distance বের করতে হবে। (১০) (Translate: Find the distance of the fault from the test end via Murray Loop Test.)

**Solution:**
*(Note: As this is a generic descriptive question from a class test asking to derive or explain the formula, the solution outlines the mathematical derivation of the distance formula).*

To find the distance of a fault from the test end using the Murray Loop Test, we derive the relationship between the bridge resistances and the physical length of the cable.

**Assumptions:**
1.  A sound cable is available alongside the faulty cable.
2.  Both the sound cable and the faulty cable have the exact same length ($l$), material, and uniform cross-sectional area. This means their resistance is directly proportional to their length. Let $r$ be the resistance per unit length.

**Circuit Configuration:**
*   The far ends of the sound and faulty cables are shorted together.
*   At the test end, variable ratio arms $P$ and $Q$ are connected to the sound and faulty cables, respectively.
*   A galvanometer is across the bridge, and a DC source is applied between the $P,Q$ junction and the ground/shorted fault.

**Derivation:**
1.  **Define Resistances:**
    *   Let $R$ be the resistance of the sound cable plus the resistance of the healthy portion of the faulty cable.
    *   Let $X$ be the resistance of the faulty cable from the test end to the fault point.
    *   The total loop resistance $R_{loop} = R + X$.
    *   Since total length is $2l$, the total loop resistance is also $R_{loop} = 2l \cdot r$.

2.  **Bridge Balance Equation:**
    At balance (zero galvanometer deflection), the Wheatstone bridge equation is:
    $$\frac{P}{Q} = \frac{R}{X}$$

3.  **Solve for Fault Resistance ($X$):**
    Add 1 to both sides:
    $$\frac{P}{Q} + 1 = \frac{R}{X} + 1$$
    $$\frac{P + Q}{Q} = \frac{R + X}{X}$$
    Substitute $R_{loop}$ for $(R + X)$:
    $$\frac{P + Q}{Q} = \frac{R_{loop}}{X}$$
    $$X = \frac{Q}{P + Q} R_{loop}$$

4.  **Convert Resistance to Distance:**
    Let $l_1$ be the distance from the test end to the fault.
    The resistance $X$ is proportional to this distance: $X = l_1 \cdot r$.
    We also know $R_{loop} = 2l \cdot r$.
    Substitute these into the equation for $X$:
    $$l_1 \cdot r = \frac{Q}{P + Q} (2l \cdot r)$$
    The resistance per unit length ($r$) cancels out from both sides:
    $$l_1 = \frac{Q}{P + Q} (2l)$$

**Conclusion:**
The formula $l_1 = \frac{Q}{P + Q} (2l)$ calculates the exact distance from the test end to the fault point. You only need to know the total length of one single cable run ($l$) and the balanced values of the ratio arms ($P$ and $Q$).

*   **Reference in eee2211 slide:** Pages 79, 80.
### 29.  ✅ Page 29, Class test #3 Q1: Suppose, you are assigned to localize a short circuit fault using Murray loop test. Unlike the conventional test set-up, where a sound cable identical to the faulty cable is used as one of the bridge arms, here, a resistance equal to the sound cable resistance is inserted in that bridge arm instead of the actual cable. The connecting wire resistance is negligible. (c) Derive the equation for finding the fault location for the above situation. (d) Given, the sound cable resistance = 10 $\Omega$, resistance of the ratio arms, P= 30 $\Omega$, Q= 10 $\Omega$, length of the cable= 10 km. Find the location of the fault.

**Solution:**

**Part (c): Derivation of the Equation**
In a conventional Murray loop test, the faulty cable and a sound cable are joined at the far end to form a loop. The bridge consists of ratio arms $P$ and $Q$, with the cable loop forming the other two arms. 
In this modified setup, instead of a physical sound cable returning to the test site, a fixed standard resistor ($R_s$) equal to the sound cable's resistance is used at the test end. A low-resistance return wire (negligible resistance) connects the far end of the faulty cable to this resistor $R_s$.

*   Let the resistance of the fixed resistor be $R_s$.
*   Let the total resistance of the faulty cable be $R_f$.
*   Let $X$ be the resistance of the faulty cable from the testing end up to the short-circuit fault point.
*   The resistance of the faulty cable beyond the fault point is $(R_f - X)$.

When the bridge is balanced, the ratio of the arms is equal. The arms of the bridge are $P, Q, X$, and $[R_s + (R_f - X)]$.
$$\frac{P}{Q} = \frac{R_s + (R_f - X)}{X}$$
Add 1 to both sides:
$$\frac{P}{Q} + 1 = \frac{R_s + R_f - X}{X} + 1$$
$$\frac{P + Q}{Q} = \frac{R_s + R_f - X + X}{X}$$
$$\frac{P + Q}{Q} = \frac{R_s + R_f}{X}$$
Rearranging to solve for $X$:
$$X = \frac{Q}{P + Q} (R_s + R_f)$$

To find the distance ($l_x$), we relate resistance to length. Let the total length of the faulty cable be $l$. Since resistance is proportional to length for a uniform cable, the resistance per unit length is $r = R_f / l$.
The distance to the fault is $l_x = X / r$.
$$l_x = \frac{X}{R_f / l} = X \times \frac{l}{R_f}$$
Substitute the expression for $X$:
$$l_x = \frac{Q}{P + Q} \left( \frac{R_s + R_f}{R_f} \right) l$$
*Note: This acts functionally identical to the standard Murray loop derivation where total loop resistance $R_{loop} = R_s + R_f$.*

**Part (d): Calculation**
**Given Data:**
*   Fixed resistance (simulating sound cable), $R_s = 10\ \Omega$
*   Since the prompt implies the original standard setup used an "identical" sound cable, the faulty cable's total resistance is equal to the sound cable's resistance: $R_f = 10\ \Omega$
*   Total loop resistance, $R_{loop} = R_s + R_f = 10 + 10 = 20\ \Omega$
*   Ratio arms: $P = 30\ \Omega$, $Q = 10\ \Omega$
*   Length of the faulty cable, $l = 10\text{ km}$

**Step 1: Find the resistance to the fault ($X$)**
Using the derived formula:
$$X = \frac{Q}{P + Q} (R_s + R_f)$$
$$X = \frac{10}{30 + 10} (20)$$
$$X = \frac{10}{40} \times 20 = 0.25 \times 20 = 5\ \Omega$$

**Step 2: Find the distance to the fault ($l_x$)**
The total resistance of the 10 km cable is $10\ \Omega$. Therefore, the resistance per km ($r$) is:
$$r = \frac{10\ \Omega}{10\text{ km}} = 1\ \Omega/\text{km}$$
The distance to the fault is:
$$l_x = \frac{X}{r} = \frac{5\ \Omega}{1\ \Omega/\text{km}} = 5\text{ km}$$

The location of the fault is **5 km** from the testing end.

*   **Reference in eee2211 slide:** Pages 79, 80, 81 (Murray Loop Test equations).

***

### 30. Page 29, Class test #3 Q2: In a Varley loop test for localization of cable earth fault, the total resistances of the identical sound cable and faulty cable is 8 $\Omega$. The ratio arms are set at P= 5 $\Omega$ and Q= 10 $\Omega$. When a switch in the bridge connects the negative pole of the battery to the ground, the value of standard resistance S required for bridge balance is 7 $\Omega$. If the per km resistance of the cable is 0.4 $\Omega$/km, find the location of the fault.

**Solution:**

**Given Data:**
*   Total loop resistance of both cables combined, $R_{loop} = 8\ \Omega$
*   Ratio arm $P = 5\ \Omega$
*   Ratio arm $Q = 10\ \Omega$
*   Variable standard resistance at balance (fault testing step), $S = 7\ \Omega$
*   Cable resistance per km, $r = 0.4\ \Omega/\text{km}$

**Step 1: Calculate the resistance of the cable up to the fault point ($X$)**
The Varley loop test operates in two steps. The problem provides the data for the second step (switch connected to ground), which is used to locate the fault. 

Let $R$ be the resistance of the sound cable plus the healthy portion of the faulty cable.
Let $X$ be the resistance from the testing end to the fault.
We know that $R + X = R_{loop}$.
The balance equation for this configuration is:
$$\frac{P}{Q} = \frac{R}{S + X}$$

Substitute $R = R_{loop} - X$:
$$\frac{P}{Q} = \frac{R_{loop} - X}{S + X}$$
Cross-multiply:
$$P(S + X) = Q(R_{loop} - X)$$
$$PS + PX = QR_{loop} - QX$$
Rearrange to solve for $X$:
$$PX + QX = QR_{loop} - PS$$
$$X(P + Q) = QR_{loop} - PS$$
$$X = \frac{Q \cdot R_{loop} - P \cdot S}{P + Q}$$

Plug in the given values:
$$X = \frac{(10 \times 8) - (5 \times 7)}{5 + 10}$$
$$X = \frac{80 - 35}{15}$$
$$X = \frac{45}{15}$$
$$X = 3\ \Omega$$

**Step 2: Calculate the location of the fault**
We have the resistance of the cable up to the fault ($3\ \Omega$) and the resistance per km ($0.4\ \Omega/\text{km}$).
$$\text{Distance to fault } (l_x) = \frac{\text{Resistance to fault } (X)}{\text{Resistance per km } (r)}$$
$$l_x = \frac{3\ \Omega}{0.4\ \Omega/\text{km}}$$
$$l_x = 7.5\text{ km}$$

The location of the earth fault is **7.5 km** from the testing end.

*   **Reference in eee2211 slide:** Pages 82, 83 (Varley Loop Test equations).

***

### 33. Page 2, Q.3. (a): Explain why Hay's bridge is useful for measuring the inductance of coils with a storage factor Q>10.

**Solution:**
Hay's bridge is a modification of Maxwell's inductance-capacitance bridge. While Maxwell's bridge connects the standard capacitor and variable resistor in parallel, **Hay's bridge connects them in series**. This topological difference makes Hay's bridge uniquely suited for measuring high-Q coils.

*   **Figure Involved:** Circuit diagram of Hay's Bridge. Arm 1: Unknown $R_1, L_1$. Arm 2: $R_2$. Arm 3: $R_3$. Arm 4: $R_4$ and $C_4$ in series. 

**Mathematical Justification:**
The balance conditions for Hay's bridge yield the following expressions for unknown inductance $L_1$ and resistance $R_1$:
1.  $R_1 = \frac{\omega^2 R_2 R_3 R_4 C_4^2}{1 + \omega^2 C_4^2 R_4^2}$
2.  $L_1 = \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2}$

The storage factor (Quality factor, $Q$) of the unknown coil is defined as $Q = \frac{\omega L_1}{R_1}$.
Substituting the expressions for $L_1$ and $R_1$:
$$Q = \frac{\omega \left( \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2} \right)}{\left( \frac{\omega^2 R_2 R_3 R_4 C_4^2}{1 + \omega^2 C_4^2 R_4^2} \right)} = \frac{1}{\omega C_4 R_4}$$

From this, we can substitute $\omega C_4 R_4 = 1/Q$ into the $L_1$ equation:
$$L_1 = \frac{R_2 R_3 C_4}{1 + (\frac{1}{Q})^2}$$

**Why it is useful for $Q > 10$:**
1.  **Simplification of the Inductance Formula:** If the coil has a high Q-factor (greater than 10), then the term $(1/Q)^2$ becomes less than $(1/10)^2 = 0.01$. This value is very small compared to 1. Therefore, the denominator $(1 + 1/Q^2)$ becomes approximately equal to 1. The equation simplifies to:
    $$L_1 \approx R_2 R_3 C_4$$
    This means for high-Q coils, the measured inductance simply depends on fixed bridge arms and is practically independent of the test frequency ($\omega$). 
2.  **Practical Component Values:** For a high-Q coil, the internal resistance $R_1$ is very small. In Maxwell's bridge (where $Q = \omega C_4 R_4$), measuring a high-Q coil requires a correspondingly very high value for the parallel resistance $R_4$. High-value precision variable resistors are expensive, bulky, and prone to error. 
    In Hay's bridge (where $Q = \frac{1}{\omega C_4 R_4}$), a high Q-factor means $R_4$ must be a **small** value. It is much easier, cheaper, and more accurate to construct a precision low-value variable resistor box than a high-value one.

*   **Reference in eee2211 slide:** Pages 95, 96, 97 (Hay's Bridge and its advantages).

***

### 34. Page 2, Q.3. (b): An Owen's bridge is used to measure the properties of a sample of sheet steel at 2 kHz. At balance the various values are: $R_2 = 834\ \Omega$, $R_3 = 100\ \Omega$, $C_2 = 0.124\ \mu\text{F}$ and $C_4 = 0.1\ \mu\text{F}$. Derive the balance conditions and calculate the effective impedance of the specimen under test conditions.

**Solution:**

**Part 1: Derivation of Balance Conditions for Owen's Bridge**
*   **Figure Involved:** Circuit diagram of Owen's Bridge. 
    *   Arm 1 ($ab$): Unknown specimen with effective series resistance $R_1$ and inductance $L_1$ $\implies Z_1 = R_1 + j\omega L_1$
    *   Arm 2 ($ad$): Resistor $R_2$ in series with capacitor $C_2$ $\implies Z_2 = R_2 - j\frac{1}{\omega C_2}$
    *   Arm 3 ($bc$): Fixed resistor $R_3$ $\implies Z_3 = R_3$
    *   Arm 4 ($cd$): Fixed capacitor $C_4$ $\implies Z_4 = - j\frac{1}{\omega C_4}$

The general equation for an AC bridge at balance is:
$$Z_1 Z_4 = Z_2 Z_3$$
Substitute the impedances:
$$(R_1 + j\omega L_1) \left( -j\frac{1}{\omega C_4} \right) = \left( R_2 - j\frac{1}{\omega C_2} \right) R_3$$
$$-j\frac{R_1}{\omega C_4} - j^2\frac{\omega L_1}{\omega C_4} = R_2 R_3 - j\frac{R_3}{\omega C_2}$$
Since $j^2 = -1$:
$$-j\frac{R_1}{\omega C_4} + \frac{L_1}{C_4} = R_2 R_3 - j\frac{R_3}{\omega C_2}$$

Equate the real and imaginary parts separately:
**Real parts:**
$$\frac{L_1}{C_4} = R_2 R_3 \implies L_1 = R_2 R_3 C_4$$
**Imaginary parts:**
$$-\frac{R_1}{\omega C_4} = -\frac{R_3}{\omega C_2} \implies R_1 = R_3 \frac{C_4}{C_2}$$

**Part 2: Calculation of Effective Impedance**
**Given Data:**
*   $f = 2\text{ kHz} = 2000\text{ Hz}$
*   $\omega = 2\pi f = 2 \pi (2000) = 4000\pi\text{ rad/s}$
*   $R_2 = 834\ \Omega$
*   $R_3 = 100\ \Omega$
*   $C_2 = 0.124\ \mu\text{F} = 0.124 \times 10^{-6}\text{ F}$
*   $C_4 = 0.1\ \mu\text{F} = 0.1 \times 10^{-6}\text{ F}$

**Step 1: Calculate $R_1$**
$$R_1 = R_3 \frac{C_4}{C_2} = 100 \times \frac{0.1 \times 10^{-6}}{0.124 \times 10^{-6}}$$
$$R_1 = 100 \times \frac{0.1}{0.124} \approx 80.645\ \Omega$$

**Step 2: Calculate $L_1$**
$$L_1 = R_2 R_3 C_4 = 834 \times 100 \times (0.1 \times 10^{-6})$$
$$L_1 = 83400 \times 10^{-7} = 0.00834\text{ H} = 8.34\text{ mH}$$

**Step 3: Calculate the inductive reactance ($X_L$)**
$$X_L = \omega L_1 = (4000\pi) \times 0.00834$$
$$X_L = 33.36 \pi \approx 104.805\ \Omega$$

**Step 4: Calculate the effective impedance ($|Z_1|$)**
The impedance of the test specimen is $Z_1 = R_1 + jX_L$.
The magnitude of the effective impedance is:
$$|Z_1| = \sqrt{R_1^2 + X_L^2}$$
$$|Z_1| = \sqrt{80.645^2 + 104.805^2}$$
$$|Z_1| = \sqrt{6503.616 + 10984.088}$$
$$|Z_1| = \sqrt{17487.704} \approx 132.24\ \Omega$$

The effective impedance of the specimen is **$132.24\ \Omega$**.

*   **Reference in eee2211 slide:** Pages 99, 100 (Owen's Bridge derivation and equations).

### 35. Page 4, Q.4 (b): What value should $C_1$ have for $V_0$ to be equal to $0.1V_i$ for the circuit shown in following figure? 

[figure Involved] -  ![[Pasted image 20260722082537.png]] The figure shows a voltage divider circuit. The top arm has a resistor $900\text{ k}\Omega$ in parallel with capacitor $C_1$. The bottom arm has a resistor $100\text{ k}\Omega$ in parallel with a capacitor $45\text{ pF}$. The input voltage $V_i$ is across the entire combination, and output voltage $V_0$ is across the bottom arm.

**Solution:**
This circuit is a compensated voltage divider, exactly like the ones used in oscilloscope probes to step down high frequency signals without distorting their shape. 

For the output voltage to be an exact, scaled replica of the input voltage regardless of the frequency (i.e., for the attenuation to be independent of frequency), the time constant of the upper parallel $RC$ network must equal the time constant of the lower parallel $RC$ network.

Let's break down the given parameters:
*   $R_1$ (top resistor) = $900\text{ k}\Omega = 900 \times 10^3\ \Omega$
*   $C_1$ (top capacitor) = Unknown
*   $R_2$ (bottom resistor) = $100\text{ k}\Omega = 100 \times 10^3\ \Omega$
*   $C_2$ (bottom capacitor) = $45\text{ pF} = 45 \times 10^{-12}\text{ F}$

First, let's check the DC attenuation (where capacitors act as open circuits):
$$\frac{V_0}{V_i} = \frac{R_2}{R_1 + R_2} = \frac{100\text{ k}\Omega}{900\text{ k}\Omega + 100\text{ k}\Omega} = \frac{100\text{ k}\Omega}{1000\text{ k}\Omega} = 0.1$$
The resistive divider already naturally provides the required $0.1$ attenuation ratio.

To maintain this $0.1$ ratio for AC signals across all frequencies, the capacitive voltage divider must also have the exact same ratio. The condition for a frequency-compensated attenuator is that the time constants are equal:
$$\tau_1 = \tau_2$$
$$R_1 \cdot C_1 = R_2 \cdot C_2$$

Now, solve for $C_1$:
$$C_1 = \frac{R_2 \cdot C_2}{R_1}$$
$$C_1 = \frac{(100 \times 10^3\ \Omega) \times 45\text{ pF}}{900 \times 10^3\ \Omega}$$
$$C_1 = \left( \frac{100}{900} \right) \times 45\text{ pF}$$
$$C_1 = \frac{1}{9} \times 45\text{ pF}$$
$$C_1 = 5\text{ pF}$$

The value of $C_1$ must be **$5\text{ pF}$** to ensure $V_0 = 0.1 V_i$ at all frequencies.

*   **Reference in eee2211 slide:** Not explicitly detailed in the provided slides (relates to CRO probes).

***

### 36. Page 5, Q.8 (a): Illustrate the concept of dissipation factor of a capacitor with proper phasor diagram.

**Solution:**
**Concept of Dissipation Factor:**
An ideal capacitor has purely reactive impedance and does not dissipate any active real power. However, practical real-world capacitors have inherent resistive losses due to dielectric imperfections, leakage current, and the resistance of the connecting leads. 

The **Dissipation Factor ($D$)** is a measure of these losses. It is defined as the ratio of the active power dissipated (resistive loss) to the reactive power stored in the capacitor when subjected to an AC voltage. It is also the reciprocal of the Quality factor ($Q$).
$$D = \frac{\text{Active Power}}{\text{Reactive Power}} = \frac{1}{Q}$$

**Equivalent Circuits and Phasor Diagrams:**
A practical capacitor can be modeled mathematically in two ways: as an ideal capacitor in series with a small resistor, or as an ideal capacitor in parallel with a large resistor.

**1. Series Equivalent Circuit Model:**
*   **Circuit:** An ideal capacitor $C_s$ in series with a small equivalent series resistance $R_s$.
*   **Phasor Diagram (Figure Involved):** 
    *   The series current $I$ is taken as the reference phasor (horizontal axis).
    *   The voltage drop across the resistor ($V_R = I \cdot R_s$) is in phase with the current $I$.
    *   The voltage drop across the ideal capacitor ($V_C = I \cdot X_C = I / \omega C_s$) lags the current $I$ by exactly $90^\circ$.
    *   The total applied voltage ($V$) is the vector sum of $V_R$ and $V_C$.
    *   The angle between the total voltage $V$ and the ideal capacitive voltage $V_C$ is called the **loss angle, $\delta$**.
    *   The angle between the total voltage $V$ and the current $I$ is the phase angle, $\theta$ (where $\theta = 90^\circ - \delta$).
*   **Mathematical Expression:** 
    From the phasor diagram, the dissipation factor $D$ is the tangent of the loss angle $\delta$:
    $$D = \tan(\delta) = \frac{V_R}{V_C} = \frac{I \cdot R_s}{I / (\omega C_s)} = \omega R_s C_s$$

**2. Parallel Equivalent Circuit Model:**
*   **Circuit:** An ideal capacitor $C_p$ in parallel with a large equivalent parallel resistance $R_p$.
*   **Phasor Diagram (Figure Involved):**
    *   The parallel voltage $V$ is taken as the reference phasor.
    *   The current through the resistor ($I_R = V / R_p$) is in phase with $V$.
    *   The current through the capacitor ($I_C = V \cdot \omega C_p$) leads $V$ by $90^\circ$.
    *   The total current $I$ is the vector sum of $I_R$ and $I_C$.
    *   The loss angle $\delta$ is the angle between the ideal capacitive current $I_C$ and the total current $I$.
*   **Mathematical Expression:**
    $$D = \tan(\delta) = \frac{I_R}{I_C} = \frac{V / R_p}{V \cdot \omega C_p} = \frac{1}{\omega R_p C_p}$$

In both models, for a high-quality capacitor, the loss angle $\delta$ is very small, making $D$ very small, indicating minimal power dissipation.

*   **Reference in eee2211 slide:** Not explicitly detailed in the provided slides (slides focus on Q-factor of coils rather than D-factor of capacitors).

***

### 37. Page 5, Q.8 (b): Analyze how Hay's bridge is more advantages over Maxwell's inductance bridge for measurement of inductance of high Q-coils.

**Solution:**
To analyze why Hay's bridge is superior for measuring high-Q coils, we must compare the balance equations and physical component requirements of both bridges.

**Maxwell's Inductance-Capacitance Bridge:**
In Maxwell's bridge, the unknown inductance $L_1$ and resistance $R_1$ are balanced against a standard capacitor $C_4$ in **parallel** with a variable resistor $R_4$.
The balance equations are:
*   $L_1 = R_2 R_3 C_4$
*   $R_1 = \frac{R_2 R_3}{R_4}$
The Q-factor of the unknown coil is $Q = \frac{\omega L_1}{R_1} = \omega C_4 R_4$.

**Hay's Bridge:**
Hay's bridge is a topological modification of Maxwell's bridge where the standard capacitor $C_4$ is in **series** with the variable resistor $R_4$.
The balance equations are:
*   $L_1 = \frac{R_2 R_3 C_4}{1 + (\omega C_4 R_4)^2}$
*   $R_1 = \frac{\omega^2 R_2 R_3 R_4 C_4^2}{1 + (\omega C_4 R_4)^2}$
The Q-factor is $Q = \frac{\omega L_1}{R_1} = \frac{1}{\omega C_4 R_4}$.

**Analysis of Advantages for High-Q Coils ($Q > 10$):**

1.  **Practicality of Component Values:**
    *   A high-Q coil implies that its internal resistance $R_1$ is very low relative to its inductive reactance. 
    *   In **Maxwell's bridge**, $Q$ is directly proportional to $R_4$ ($Q = \omega C_4 R_4$). To measure a high $Q$, $R_4$ must be an extremely **large** value (often hundreds of kilo-ohms or mega-ohms). Manufacturing a variable, high-precision, non-inductive resistor of such a large value is expensive and physically difficult. High-value resistors also introduce parasitic shunt capacitance, causing severe measurement errors.
    *   In **Hay's bridge**, $Q$ is inversely proportional to $R_4$ ($Q = 1 / (\omega C_4 R_4)$). Therefore, measuring a high $Q$ requires a very **small** value of $R_4$. It is much easier and cheaper to build a high-precision, low-value variable resistor box without parasitic capacitance issues.

2.  **Simplification of the Inductance Formula:**
    *   Looking at the $L_1$ formula for Hay's bridge, the denominator is $1 + (\omega C_4 R_4)^2$. 
    *   Since $Q = \frac{1}{\omega C_4 R_4}$, we can substitute to get $1 + (\frac{1}{Q})^2$.
    *   If the coil has a high Q-factor (e.g., $Q > 10$), then $(1/Q)^2$ is less than $1/100 = 0.01$. 
    *   This makes the term $(1/Q)^2$ negligible compared to 1. The denominator approaches exactly 1.
    *   Thus, for high-Q coils, Hay's bridge formula simplifies to:
        $$L_1 \approx R_2 R_3 C_4$$
    *   This is highly advantageous because it removes the frequency term ($\omega$) from the inductance calculation, making the measurement independent of minor variations in the power supply frequency. 

**Conclusion:** 
Hay's bridge is more advantageous because it requires cheap, easily obtainable low-value resistors for the balance arm and provides a simplified, frequency-independent equation for calculating the inductance of high-Q coils.

*   **Reference in eee2211 slide:** Pages 94, 97.

***

### 38. Page 6, Q.3 a): Describe the principle of self-inductance measurement using Hay's bridge.

**Solution:**
**Principle of Hay's Bridge:**
Hay's bridge is an AC bridge circuit used to measure an unknown self-inductance and its effective series resistance. It works by balancing the voltage drops across four arms of a network until a null detector (like a galvanometer) registers zero current, meaning the potential difference across the center nodes is zero.

*   **Figure Involved:** The circuit diagram of Hay's Bridge. 
    *   **Arm 1 (ab):** Contains the unknown inductor $L_1$ and its internal resistance $R_1$. Impedance $Z_1 = R_1 + j\omega L_1$.
    *   **Arm 2 (ad):** Contains a standard non-inductive resistor $R_2$. Impedance $Z_2 = R_2$.
    *   **Arm 3 (bc):** Contains a standard non-inductive resistor $R_3$. Impedance $Z_3 = R_3$.
    *   **Arm 4 (cd):** Contains a standard capacitor $C_4$ in **series** with a variable non-inductive resistor $R_4$. Impedance $Z_4 = R_4 - j\frac{1}{\omega C_4}$.

**Derivation of Balance Conditions:**
The general balance condition for an AC bridge is that the products of the opposite arm impedances must be equal:
$$Z_1 Z_4 = Z_2 Z_3$$

Substitute the specific impedances of Hay's bridge:
$$(R_1 + j\omega L_1) \left( R_4 - j\frac{1}{\omega C_4} \right) = R_2 R_3$$

Expand the left side of the equation:
$$R_1 R_4 - j\frac{R_1}{\omega C_4} + j\omega L_1 R_4 - j^2 \frac{\omega L_1}{\omega C_4} = R_2 R_3$$

Since $j^2 = -1$, the term $-j^2 \frac{L_1}{C_4}$ becomes $+\frac{L_1}{C_4}$. Group the real and imaginary parts:
$$\left( R_1 R_4 + \frac{L_1}{C_4} \right) + j\left( \omega L_1 R_4 - \frac{R_1}{\omega C_4} \right) = R_2 R_3 + j0$$

For the bridge to be balanced, both the real and imaginary parts on both sides of the equation must be equal.

**1. Equating Imaginary Parts:**
$$\omega L_1 R_4 - \frac{R_1}{\omega C_4} = 0$$
$$\omega L_1 R_4 = \frac{R_1}{\omega C_4}$$
Solving for $R_1$:
$$R_1 = \omega^2 L_1 C_4 R_4 \quad \text{--- (Equation A)}$$

**2. Equating Real Parts:**
$$R_1 R_4 + \frac{L_1}{C_4} = R_2 R_3$$
Substitute $R_1$ from Equation A into this real part equation:
$$(\omega^2 L_1 C_4 R_4) R_4 + \frac{L_1}{C_4} = R_2 R_3$$
$$\omega^2 L_1 C_4 R_4^2 + \frac{L_1}{C_4} = R_2 R_3$$
Multiply the entire equation by $C_4$ to eliminate the fraction:
$$\omega^2 L_1 C_4^2 R_4^2 + L_1 = R_2 R_3 C_4$$
Factor out $L_1$:
$$L_1 (1 + \omega^2 C_4^2 R_4^2) = R_2 R_3 C_4$$
Solve for unknown Inductance **$L_1$**:
$$L_1 = \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2}$$

**3. Solving for Resistance $R_1$:**
Substitute the derived formula for $L_1$ back into Equation A:
$$R_1 = \omega^2 \left( \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2} \right) C_4 R_4$$
$$R_1 = \frac{\omega^2 R_2 R_3 R_4 C_4^2}{1 + \omega^2 C_4^2 R_4^2}$$

Through these derivations, if the frequency ($\omega$) and the values of the standard balancing components ($R_2, R_3, R_4, C_4$) are known, the exact self-inductance and internal resistance of the coil can be measured.

*   **Reference in eee2211 slide:** Pages 95, 96.
### 39. Page 6, Q.3 b): An Owen bridge is used to measure the properties of a sample of sheet steel at 2 kHz. At balance, arm ab is test specimen; arm bc is $R_3 = 100\Omega$, arm cd is $C_4 = 0.1\mu F$ and arm da is $R_2 = 834\Omega$ in series with $C_2 = 0.124\mu F$. Derive balance conditions and calculate the effective impedance of the specimen under test conditions.

**Solution:**

**Part 1: Derivation of Balance Conditions for Owen's Bridge**
*   **Figure Involved:** The circuit diagram of an Owen's Bridge.
Based on the prompt's arm assignments, we can map the impedances:
*   **Arm ab ($Z_1$):** Test specimen with unknown effective series resistance $R_1$ and inductance $L_1$. $\implies Z_1 = R_1 + j\omega L_1$
*   **Arm bc ($Z_3$):** Fixed non-inductive resistor $R_3$. $\implies Z_3 = R_3$
*   **Arm cd ($Z_4$):** Fixed standard capacitor $C_4$. $\implies Z_4 = -j\frac{1}{\omega C_4}$
*   **Arm da ($Z_2$):** Variable resistor $R_2$ in series with a variable capacitor $C_2$. $\implies Z_2 = R_2 - j\frac{1}{\omega C_2}$

*(Note: The standard bridge balance equation is $Z_1 Z_4 = Z_2 Z_3$. Let's substitute the values into this equation).*
$$(R_1 + j\omega L_1) \left( -j\frac{1}{\omega C_4} \right) = \left( R_2 - j\frac{1}{\omega C_2} \right) R_3$$

Expand the left side:
$$-j\frac{R_1}{\omega C_4} - j^2\frac{\omega L_1}{\omega C_4} = R_2 R_3 - j\frac{R_3}{\omega C_2}$$
Since $j^2 = -1$:
$$\frac{L_1}{C_4} - j\frac{R_1}{\omega C_4} = R_2 R_3 - j\frac{R_3}{\omega C_2}$$

For the bridge to be balanced, the real parts and imaginary parts on both sides must be equal.
**Equating Real Parts:**
$$\frac{L_1}{C_4} = R_2 R_3 \implies L_1 = R_2 R_3 C_4$$
**Equating Imaginary Parts:**
$$-\frac{R_1}{\omega C_4} = -\frac{R_3}{\omega C_2} \implies R_1 = R_3 \frac{C_4}{C_2}$$

**Part 2: Calculation of Effective Impedance**
**Given Data:**
*   Frequency, $f = 2\text{ kHz} = 2000\text{ Hz}$
*   Angular frequency, $\omega = 2\pi f = 2 \pi (2000) = 4000\pi\text{ rad/s}$
*   $R_2 = 834\ \Omega$
*   $R_3 = 100\ \Omega$
*   $C_2 = 0.124\ \mu\text{F} = 0.124 \times 10^{-6}\text{ F}$
*   $C_4 = 0.1\ \mu\text{F} = 0.1 \times 10^{-6}\text{ F}$

**Step 1: Calculate Effective Resistance ($R_1$)**
$$R_1 = R_3 \left( \frac{C_4}{C_2} \right) = 100 \times \left( \frac{0.1 \times 10^{-6}}{0.124 \times 10^{-6}} \right)$$
$$R_1 = 100 \times \left( \frac{0.1}{0.124} \right) \approx 80.645\ \Omega$$

**Step 2: Calculate Effective Inductance ($L_1$)**
$$L_1 = R_2 R_3 C_4 = 834 \times 100 \times (0.1 \times 10^{-6})$$
$$L_1 = 83400 \times 10^{-7} = 0.00834\text{ H} = 8.34\text{ mH}$$

**Step 3: Calculate Inductive Reactance ($X_L$)**
$$X_L = \omega L_1 = (4000\pi) \times 0.00834$$
$$X_L = 33.36\pi \approx 104.805\ \Omega$$

**Step 4: Calculate Effective Impedance ($|Z_1|$)**
The total impedance of the specimen is $Z_1 = R_1 + jX_L$. Its magnitude is:
$$|Z_1| = \sqrt{R_1^2 + X_L^2}$$
$$|Z_1| = \sqrt{(80.645)^2 + (104.805)^2}$$
$$|Z_1| = \sqrt{6503.616 + 10984.088} = \sqrt{17487.704}$$
$$|Z_1| \approx 132.24\ \Omega$$

The effective impedance of the specimen under test conditions is **$132.24\ \Omega$**.

*   **Reference in eee2211 slide:** Pages 99, 100 (Owen's Bridge).

***

### 40. Page 6, Q.5 a): What is dissipation factor? Describe the principle of modified De-Sauty's bridge and show the measurement procedure of dissipation factor with appropriate phasor diagram.

**Solution:**

**1. What is Dissipation Factor?**
An ideal capacitor has purely reactive impedance and zero power loss. However, practical capacitors have internal resistive losses due to dielectric imperfections and lead resistance. The **Dissipation Factor ($D$)** is a metric of these losses. It is defined as the ratio of the active power dissipated (resistive loss) to the reactive power stored in the capacitor.
$$D = \frac{\text{Active Power}}{\text{Reactive Power}} = \tan(\delta) = \frac{1}{Q}$$
Where $\delta$ is the loss angle (the angle by which the current leads the voltage falls short of the ideal $90^\circ$), and $Q$ is the quality factor. For a series $RC$ model of a capacitor, $D = \omega C R_s$.

**2. Principle of Modified De-Sauty's Bridge:**
The basic De-Sauty’s bridge compares two capacitors by equating their reactances against pure ratio arms. However, as noted in the slides, the basic De-Sauty's bridge *only works if both capacitors are perfect (lossless)*. If the capacitors have unequal dielectric losses, perfect balance cannot be achieved. 

The **Modified De-Sauty's bridge** overcomes this limitation by adding non-inductive variable resistors in series with the capacitors in both arms. This allows the bridge to balance both the reactive (capacitive) components and the active (resistive loss) components simultaneously.

*   **Figure Involved:** The circuit diagram of a Modified De-Sauty's Bridge.
    *   **Arm 1:** Unknown capacitor $C_1$ with its internal loss resistance $r_1$, in series with an external variable resistor $R_1$.
    *   **Arm 2:** Standard capacitor $C_2$ with internal loss $r_2$, in series with an external variable resistor $R_2$.
    *   **Arm 3 & 4:** Non-inductive fixed resistors $R_3$ and $R_4$.

**Measurement Procedure and Equations:**
At balance, the bridge equation is $Z_1 Z_4 = Z_2 Z_3$:
$$(R_1 + r_1 - j\frac{1}{\omega C_1}) R_4 = (R_2 + r_2 - j\frac{1}{\omega C_2}) R_3$$

**Equating the imaginary parts** gives the capacitance:
$$-j\frac{R_4}{\omega C_1} = -j\frac{R_3}{\omega C_2} \implies C_1 = C_2 \frac{R_4}{R_3}$$

**Equating the real parts** gives the resistance:
$$(R_1 + r_1) R_4 = (R_2 + r_2) R_3 \implies r_1 = \frac{R_3}{R_4}(R_2 + r_2) - R_1$$

The dissipation factor of the unknown capacitor ($D_1$) is $\omega C_1 r_1$. Substituting $r_1$:
$$D_1 = \omega C_1 \left[ \frac{R_3}{R_4}(R_2 + r_2) - R_1 \right]$$
Since $C_1 \frac{R_3}{R_4} = C_2$, we substitute this into the first term:
$$D_1 = \omega C_2(R_2 + r_2) - \omega C_1 R_1$$
If the standard capacitor $C_2$ is highly ideal (like an air capacitor), its internal loss $r_2 \approx 0$, and its dissipation factor $D_2 = \omega C_2 r_2 \approx 0$.
Therefore, the dissipation factor $D_1$ is measured as:
$$D_1 = \omega C_2 R_2 - \omega C_1 R_1$$

**3. Phasor Diagram (Figure Involved):**
*   The voltage across Arm 3 ($V_3 = I_2 R_3$) and Arm 4 ($V_4 = I_1 R_4$) are in phase with their respective currents. At balance, $V_3 = V_4$.
*   The current $I_1$ in Arm 1 causes a voltage drop across the resistive part $(R_1+r_1)$ that is in phase with $I_1$, and a voltage drop across the ideal capacitance $C_1$ that lags $I_1$ by $90^\circ$.
*   The total voltage $V_1$ is the vector sum of these drops. The small angle between the pure capacitive voltage drop and the total $V_1$ is the loss angle $\delta_1$, where $\tan(\delta_1) = D_1$.

*   **Reference in eee2211 slide:** Pages 101, 102 (Basic De Sauty’s bridge and its limitations, which necessitate the Modified version described here).

***

### 41. Page 7, Q.4 (c): A Maxwell's capacitance bridge is used to measure an unknown inductance in comparison with capacitance. The various values at balance are: $R_2 = 400\ \Omega$, $R_3 = 600\ \Omega$, $R_4 = 1000\ \Omega$, and $C_4 = 0.5\ \mu F$. Calculate the values of $R_1$ and $L_1$. Also, calculate the value of Q.

**Solution:**

**Given Data:**
*   $R_2 = 400\ \Omega$
*   $R_3 = 600\ \Omega$
*   $R_4 = 1000\ \Omega$
*   $C_4 = 0.5\ \mu\text{F} = 0.5 \times 10^{-6}\text{ F}$
*   Frequency ($f$) = *Not provided in the prompt.*

**Formulas for Maxwell's Inductance-Capacitance Bridge:**
From the derivation of Maxwell's bridge balance condition:
1.  Unknown Resistance: $R_1 = \frac{R_2 R_3}{R_4}$
2.  Unknown Inductance: $L_1 = R_2 R_3 C_4$
3.  Quality Factor: $Q = \frac{\omega L_1}{R_1} = \omega C_4 R_4 = 2\pi f C_4 R_4$

**Step 1: Calculate Unknown Resistance ($R_1$)**
$$R_1 = \frac{400 \times 600}{1000}$$
$$R_1 = \frac{240000}{1000}$$
$$R_1 = 240\ \Omega$$

**Step 2: Calculate Unknown Inductance ($L_1$)**
$$L_1 = 400 \times 600 \times (0.5 \times 10^{-6})$$
$$L_1 = 240000 \times 0.5 \times 10^{-6}$$
$$L_1 = 120000 \times 10^{-6}\text{ H}$$
$$L_1 = 0.12\text{ H} = 120\text{ mH}$$

**Step 3: Calculate the value of Q**
Because the frequency ($f$) is not provided in the problem statement, a numerical value for Q cannot be definitively calculated. We must express Q as a function of the unknown angular frequency $\omega$.

$$Q = \omega C_4 R_4$$
$$Q = \omega \times (0.5 \times 10^{-6}\text{ F}) \times 1000\ \Omega$$
$$Q = \omega \times (0.5 \times 10^{-3})$$
$$Q = 0.0005 \omega$$

*(Note: If a standard test frequency of $1000\text{ Hz}$ is assumed—which is common in these specific textbook problems—then $\omega = 2\pi(1000) = 2000\pi$. The Q factor would be $Q = 0.0005 \times 2000\pi = \pi \approx 3.14$. However, strictly based on the provided text, it must be left in terms of $\omega$ or $f$.)*

**Answers:**
*   $R_1 = 240\ \Omega$
*   $L_1 = 0.12\text{ H}$
*   $Q = 0.0005\omega$ (requires frequency to evaluate numerically)

*   **Reference in eee2211 slide:** Pages 92, 93 (Maxwell's Inductance-Capacitance Bridge).

***

### 42. Page 7, Q.5 (d): An Owen's bridge is used to measure the properties of a simple of sheet steel at 2 KHz. At balance, arm ab is test specimen; arm bc is $R_3 = 100\ \Omega$, arm cd is $C_4 = 0.1\ \mu F$, and arm da is $R_2 = 834\ \Omega$ in series with $C_2 = 0.124\ \mu F$. Calculate the effective impedance of the specimen under test condition.

*(Note: This is the exact same numerical problem as Q39, restated slightly differently in the source document. The solution process is identical).*

**Solution:**

**Given Data:**
*   Frequency, $f = 2\text{ kHz} = 2000\text{ Hz}$
*   Angular frequency, $\omega = 2\pi(2000) = 4000\pi\text{ rad/s}$
*   $R_3 = 100\ \Omega$
*   $C_4 = 0.1\ \mu\text{F} = 0.1 \times 10^{-6}\text{ F}$
*   $R_2 = 834\ \Omega$
*   $C_2 = 0.124\ \mu\text{F} = 0.124 \times 10^{-6}\text{ F}$

**Formulas for Owen's Bridge:**
As derived in Q39, the balance conditions for an Owen's bridge yield:
1.  $R_1 = R_3 \left( \frac{C_4}{C_2} \right)$
2.  $L_1 = R_2 R_3 C_4$

**Step 1: Calculate Effective Resistance ($R_1$)**
$$R_1 = 100 \times \left( \frac{0.1 \times 10^{-6}}{0.124 \times 10^{-6}} \right)$$
$$R_1 = \frac{10}{0.124} \approx 80.645\ \Omega$$

**Step 2: Calculate Effective Inductance ($L_1$)**
$$L_1 = 834 \times 100 \times (0.1 \times 10^{-6})$$
$$L_1 = 8340 \times 10^{-6}\text{ H}$$
$$L_1 = 0.00834\text{ H} = 8.34\text{ mH}$$

**Step 3: Calculate Inductive Reactance ($X_L$)**
$$X_L = \omega L_1 = 4000\pi \times 0.00834$$
$$X_L = 33.36\pi \approx 104.805\ \Omega$$

**Step 4: Calculate Effective Impedance ($|Z_1|$)**
The specimen's impedance is $Z_1 = R_1 + jX_L$. The magnitude is calculated using the Pythagorean theorem:
$$|Z_1| = \sqrt{R_1^2 + X_L^2}$$
$$|Z_1| = \sqrt{(80.645)^2 + (104.805)^2}$$
$$|Z_1| = \sqrt{6503.616 + 10984.088}$$
$$|Z_1| = \sqrt{17487.704}$$
$$|Z_1| \approx 132.24\ \Omega$$

The effective impedance of the sheet steel specimen is **$132.24\ \Omega$**.

*   **Reference in eee2211 slide:** Pages 99, 100 (Owen's Bridge).


### 43. Page 9, Q.3. (a): What are the limitations of De Sauty's bridge? Draw the modified De Sauty's bridge and show that the dissipation factor cannot be determined accurately using this bridge.

**Solution:**

**Limitations of the Basic De Sauty's Bridge:**
The basic De Sauty's bridge is the simplest method for comparing two capacitances. However, its primary limitation is that it assumes both capacitors are **perfect (lossless)**. Real capacitors have internal dielectric losses (equivalent to a series resistance). If the two capacitors being compared have different loss angles, a perfect null (zero deflection on the galvanometer) cannot be achieved. The sound in the headphones (or reading on the meter) will reach a minimum but will not become zero, making accurate measurement impossible.

**Modified De Sauty's Bridge:**
To overcome this, the **Modified De Sauty's bridge** is used. It introduces non-inductive variable resistors in series with the capacitors in both arms to balance the resistive losses along with the capacitive reactances.

*   **Figure Involved:** The circuit consists of four arms.
    *   Arm 1: Unknown capacitor $C_1$ (with internal loss resistance $r_1$) in series with external variable resistor $R_1$.
    *   Arm 2: Standard capacitor $C_2$ (with internal loss resistance $r_2$) in series with external variable resistor $R_2$.
    *   Arms 3 & 4: Pure, non-inductive fixed ratio resistors $R_3$ and $R_4$.

**Showing Why Dissipation Factor Cannot Be Determined Accurately:**
At the balance condition, the bridge equation is $Z_1 Z_4 = Z_2 Z_3$:
$$(R_1 + r_1 - j\frac{1}{\omega C_1}) R_4 = (R_2 + r_2 - j\frac{1}{\omega C_2}) R_3$$

Equating the imaginary parts:
$$-j\frac{R_4}{\omega C_1} = -j\frac{R_3}{\omega C_2} \implies C_1 = C_2 \frac{R_4}{R_3}$$

Equating the real parts:
$$(R_1 + r_1) R_4 = (R_2 + r_2) R_3 \implies r_1 = \frac{R_3}{R_4}(R_2 + r_2) - R_1$$

The dissipation factor for the unknown capacitor is defined as $D_1 = \tan \delta_1 = \omega C_1 r_1$, and for the standard capacitor, $D_2 = \omega C_2 r_2$.
Multiply the real-part equation by $\omega C_1$:
$$\omega C_1 r_1 = \omega C_1 \left[ \frac{R_3}{R_4}(R_2 + r_2) \right] - \omega C_1 R_1$$

Substitute $D_1$ for $\omega C_1 r_1$. From the imaginary equation, we know $C_1 \frac{R_3}{R_4} = C_2$. Substitute this into the bracketed term:
$$D_1 = \omega C_2 (R_2 + r_2) - \omega C_1 R_1$$
$$D_1 = \omega C_2 R_2 + \omega C_2 r_2 - \omega C_1 R_1$$

Substitute $D_2$ for $\omega C_2 r_2$:
$$D_1 = \omega C_2 R_2 + D_2 - \omega C_1 R_1$$
Rearranging gives the final measurement equation:
$$D_1 - D_2 = \omega C_2 R_2 - \omega C_1 R_1$$

**Why it is inaccurate:**
1.  **Measures Difference, Not Absolute Value:** The equation shows that the bridge only yields the *difference* between the dissipation factors ($D_1 - D_2$). Unless the standard capacitor $C_2$ is a perfect, zero-loss air capacitor (making $D_2 = 0$), the absolute dissipation factor $D_1$ cannot be determined.
2.  **Difference of Large Quantities:** For high-quality capacitors, $D_1$ and $D_2$ are very small values. The bridge measures them by finding the difference between two relatively large quantities ($\omega C_2 R_2$ and $\omega C_1 R_1$). In experimental physics, calculating a small number by subtracting two large numbers is highly susceptible to massive percentage errors if there are even tiny inaccuracies in measuring $R_1, R_2, C_1,$ or $C_2$.

Because of these inherent inaccuracies in measuring small dissipation factors, the Schering Bridge is practically used instead of the modified De Sauty bridge.

*   **Reference in eee2211 slide:** Pages 101, 102 (De Sauty's bridge limitations).

***

### 44. Page 11, Q.3. (a): What is dissipation factor? Draw the modified De Sauty's bridge and show that the dissipation factor cannot be determined accurately using this bridge.

*(Note: This question is functionally identical to Question 43 with the addition of asking for the definition of the Dissipation factor first. We will define it and summarize the proof from Q43).*

**Solution:**

**1. What is Dissipation Factor?**
In an ideal capacitor, the current leads the voltage by exactly $90^\circ$, meaning it stores and releases energy without any real power loss. However, practical capacitors have internal resistive losses due to dielectric imperfections, leakage, and lead resistance. 
The **Dissipation Factor (D)** is a measure of these losses. It is defined as the ratio of the active power dissipated (resistive loss) to the reactive power stored in the capacitor.
$$D = \frac{\text{Active Power}}{\text{Reactive Power}} = \tan(\delta)$$
Where $\delta$ is the "loss angle," which is the angle by which the current falls short of the ideal $90^\circ$ lead. For a capacitor modeled with an equivalent series resistance ($r$), the dissipation factor is $D = \omega C r$.

**2. Modified De Sauty's Bridge and its Inaccuracy:**
*   **Figure Involved:** The Modified De Sauty bridge diagram. Arm 1 has the unknown lossy capacitor ($C_1, r_1$) in series with a variable resistor $R_1$. Arm 2 has the standard lossy capacitor ($C_2, r_2$) in series with a variable resistor $R_2$. Arms 3 and 4 have fixed resistors $R_3$ and $R_4$.

**Proof of Inaccuracy:**
As derived in detail in the previous solution (Q43), setting the bridge balance condition ($Z_1 Z_4 = Z_2 Z_3$) and separating the real and imaginary parts yields the following relationship for the internal resistances:
$$r_1 = \frac{R_3}{R_4}(R_2 + r_2) - R_1$$

By multiplying this entire equation by $\omega C_1$ and using the capacitance balance ratio ($C_1 = C_2 \frac{R_4}{R_3}$), we get the equation for the dissipation factors:
$$D_1 - D_2 = \omega C_2 R_2 - \omega C_1 R_1$$

This equation proves that the modified De Sauty's bridge **cannot accurately determine the absolute dissipation factor ($D_1$)**. 
1. It only provides the difference between the two dissipation factors. The exact internal loss of the standard capacitor ($D_2$) must be perfectly known to find $D_1$, which is practically difficult unless $C_2$ is an expensive perfect air capacitor.
2. Even if $D_2$ is known, $D_1$ is evaluated by taking the difference between two large quantities ($\omega C_2 R_2$ and $\omega C_1 R_1$). For small dissipation factors, minor measurement errors in the bridge arm resistors or frequency will result in severe relative errors in the final calculated value of $D_1$.

*   **Reference in eee2211 slide:** Pages 101, 102.

***

### 45. Page 11, Q.3. (c): A Maxwell's capacitance bridge shown in the figure below is used to measure an unknown inductance in comparison with capacitance. The various values at balance are: $R_2 = 400\ \Omega$, $R_3 = 600\ \Omega$, $R_4 = 1000\ \Omega$, $C_4 = 0.5\ \mu F$. Calculate the values of $R_1$ and $L_1$. Calculate also the value of storage factor of coil if frequency is 1000 Hz.

**Solution:**
![[Pasted image 20260722091443.png]]
*(Note: This is the exact same electrical setup as Question 41, but this prompt explicitly provides the frequency ($1000\text{ Hz}$) needed to calculate the storage/Q-factor numerically).*

**Given Data:**
*   $R_2 = 400\ \Omega$
*   $R_3 = 600\ \Omega$
*   $R_4 = 1000\ \Omega$
*   $C_4 = 0.5\ \mu\text{F} = 0.5 \times 10^{-6}\text{ F}$
*   Frequency, $f = 1000\text{ Hz}$

**Step 1: Calculate Unknown Resistance ($R_1$)**
For a Maxwell's Inductance-Capacitance bridge, the balance equation for the real part is:
$$R_1 = \frac{R_2 \cdot R_3}{R_4}$$
$$R_1 = \frac{400 \times 600}{1000}$$
$$R_1 = \frac{240000}{1000}$$
$$R_1 = 240\ \Omega$$

**Step 2: Calculate Unknown Inductance ($L_1$)**
The balance equation for the imaginary part is:
$$L_1 = R_2 \cdot R_3 \cdot C_4$$
$$L_1 = 400 \times 600 \times (0.5 \times 10^{-6})$$
$$L_1 = 240000 \times 0.5 \times 10^{-6}$$
$$L_1 = 120000 \times 10^{-6}\text{ H}$$
$$L_1 = 0.12\text{ H} = 120\text{ mH}$$

**Step 3: Calculate the Storage Factor (Q-factor)**
The storage factor $Q$ of a coil is the ratio of its inductive reactance to its resistance.
$$Q = \frac{\omega L_1}{R_1}$$
For the Maxwell bridge, substituting the formulas for $L_1$ and $R_1$ gives the bridge-specific Q formula:
$$Q = \omega C_4 R_4$$
First, calculate the angular frequency $\omega$:
$$\omega = 2\pi f = 2 \cdot \pi \cdot 1000 = 2000\pi\text{ rad/s}$$
Now calculate $Q$:
$$Q = (2000\pi) \times (0.5 \times 10^{-6}) \times 1000$$
$$Q = 2000\pi \times 0.0005$$
$$Q = \pi$$
$$Q \approx 3.1416$$

**Final Answers:**
*   **$R_1 = 240\ \Omega$**
*   **$L_1 = 0.12\text{ H}$ (or $120\text{ mH}$)**
*   **$Q = 3.14$**

*   **Reference in eee2211 slide:** Pages 92, 93 (Maxwell's Inductance-Capacitance Bridge).

***

### 46. Page 11, Q.4. (a): Differentiate between Maxwell's bridge and Hay's bridge on the basis of Q-factor.

**Solution:**
Both Maxwell's capacitance bridge and Hay's bridge are used to measure unknown inductances using a standard capacitor. However, their physical topologies differ slightly to optimize them for coils with different Quality factors (Q-factors).

**1. Topological Difference:**
*   **Maxwell's Bridge:** The standard capacitor ($C_4$) is connected in **parallel** with the variable tuning resistor ($R_4$).
*   **Hay's Bridge:** The standard capacitor ($C_4$) is connected in **series** with the variable tuning resistor ($R_4$).

**2. Q-Factor Formulas:**
The Storage Factor or Q-factor of a coil is defined as $Q = \omega L_1 / R_1$. When deriving this using the respective bridge balance conditions:
*   **Maxwell's Bridge:** $Q = \omega C_4 R_4$
*   **Hay's Bridge:** $Q = \frac{1}{\omega C_4 R_4}$

**3. Differentiation based on Application and Suitability:**
*   **Maxwell's Bridge is suitable for Medium-Q coils ($1 < Q < 10$):**
    Because $Q$ is directly proportional to $R_4$ in Maxwell's bridge, measuring a high-Q coil requires $R_4$ to be very large (e.g., $100\text{ k}\Omega$ to several $\text{M}\Omega$). Precision variable resistor boxes of such high values are physically bulky, expensive, and subject to severe errors caused by parasitic shunt capacitances between the resistor coils. Therefore, Maxwell's bridge becomes impractical and inaccurate for $Q > 10$.
*   **Hay's Bridge is suitable for High-Q coils ($Q > 10$):**
    Because $Q$ is inversely proportional to $R_4$ in Hay's bridge, measuring a high-Q coil requires a correspondingly very **small** value for $R_4$. It is much easier, cheaper, and structurally reliable to construct a high-precision, low-value variable resistor without introducing parasitic capacitance errors.
    Furthermore, for a high-Q coil ($Q > 10$), the term $(1/Q)^2$ becomes $\le 0.01$, which is negligible. This simplifies Hay's complex inductance formula $L_1 = \frac{R_2 R_3 C_4}{1 + (1/Q)^2}$ down to $L_1 \approx R_2 R_3 C_4$. This simplified form makes the inductance measurement independent of the supply frequency, which is a major advantage for high-Q measurements.

**Summary:**
| Feature | Maxwell's Bridge | Hay's Bridge |
| :--- | :--- | :--- |
| **Capacitor Connection** | Parallel with $R_4$ | Series with $R_4$ |
| **Q-Factor Equation** | $Q = \omega C_4 R_4$ | $Q = 1 / (\omega C_4 R_4)$ |
| **Suitability** | Medium Q coils ($1 < Q < 10$) | High Q coils ($Q > 10$) |
| **For High-Q, $R_4$ is...**| Impractically Large | Conveniently Small |

*   **Reference in eee2211 slide:** Pages 92, 93 (Maxwell's Bridge), Pages 95, 96, 97 (Hay's Bridge).



### 47. Page 11, Q.4. (b): An Owen's bridge is used to measure the properties of a sample of sheet steel at 2 kHz. At balance condition the value of fixed non-inductive resistance $R_3 = 100\ \Omega$, fixed standard capacitor $C_4 = 0.1\ \mu F$, variable non-inductive resistance $R_2 = 834\ \Omega$ in series with variable standard capacitor $C_2 = 0.124\ \mu F$. Derive the balance conditions and calculate the effective impedance of the specimen under test conditions. Also calculate the Q-factor.

**Solution:**

**Part 1: Derivation of Balance Conditions**
*(Note: The derivation is identical to the one provided in the solution for Question 39, as the bridge configuration is exactly the same).*
For Owen's Bridge, equating the real and imaginary parts of the general balance equation $Z_1 Z_4 = Z_2 Z_3$ yields:
*   **Effective Resistance:** $R_1 = R_3 \frac{C_4}{C_2}$
*   **Effective Inductance:** $L_1 = R_2 R_3 C_4$

**Part 2: Calculation of Effective Impedance and Q-Factor**
**Given Data:**
*   Frequency, $f = 2\text{ kHz} = 2000\text{ Hz}$
*   Angular frequency, $\omega = 2\pi f = 2 \pi (2000) = 4000\pi\text{ rad/s}$
*   $R_2 = 834\ \Omega$
*   $R_3 = 100\ \Omega$
*   $C_2 = 0.124\ \mu\text{F} = 0.124 \times 10^{-6}\text{ F}$
*   $C_4 = 0.1\ \mu\text{F} = 0.1 \times 10^{-6}\text{ F}$

**Step 1: Calculate Effective Resistance ($R_1$)**
$$R_1 = 100 \times \left( \frac{0.1 \times 10^{-6}}{0.124 \times 10^{-6}} \right)$$
$$R_1 \approx 80.645\ \Omega$$

**Step 2: Calculate Effective Inductance ($L_1$)**
$$L_1 = 834 \times 100 \times (0.1 \times 10^{-6})$$
$$L_1 = 0.00834\text{ H} = 8.34\text{ mH}$$

**Step 3: Calculate Inductive Reactance ($X_L$)**
$$X_L = \omega L_1 = (4000\pi) \times 0.00834$$
$$X_L \approx 104.805\ \Omega$$

**Step 4: Calculate Effective Impedance ($|Z_1|$)**
$$|Z_1| = \sqrt{R_1^2 + X_L^2}$$
$$|Z_1| = \sqrt{(80.645)^2 + (104.805)^2}$$
$$|Z_1| = \sqrt{6503.616 + 10984.088} = \sqrt{17487.704}$$
$$|Z_1| \approx 132.24\ \Omega$$

**Step 5: Calculate Q-Factor**
The Quality factor ($Q$) of the inductive specimen is the ratio of its inductive reactance to its resistance.
$$Q = \frac{X_L}{R_1} = \frac{\omega L_1}{R_1}$$
Substitute the previously calculated values:
$$Q = \frac{104.805}{80.645}$$
$$Q \approx 1.2996$$

**Final Answers:**
*   Effective Impedance ($Z_1$) = **$132.24\ \Omega$**
*   Q-Factor = **$1.30$**

*   **Reference in eee2211 slide:** Pages 99, 100 (Owen's Bridge).

***

### 48. Page 16, Q.4. (a): Explain how Wien's bridge can be used for experimental determination of frequency. Derive the expression for frequency in terms of bridge parameters.

**Solution:**
**Concept of Wien's Bridge:**
Unlike Maxwell's or Hay's bridges which are used to measure unknown inductances or capacitances using a known frequency source, **Wien's bridge** is primarily designed to measure the frequency of an unknown AC source using known resistors and capacitors. It is highly sensitive to frequency changes.

**Circuit Arrangement:**
*   **Figure Involved:** A standard 4-arm bridge.
    *   **Arm 1 ($Z_1$):** A resistor $R_1$ in **series** with a capacitor $C_1$. $\implies Z_1 = R_1 - j\frac{1}{\omega C_1}$
    *   **Arm 2 ($Z_2$):** A purely resistive arm $R_2$. $\implies Z_2 = R_2$
    *   **Arm 3 ($Z_3$):** A resistor $R_3$ in **parallel** with a capacitor $C_3$. $\implies Y_3 = \frac{1}{R_3} + j\omega C_3 \implies Z_3 = \frac{R_3}{1 + j\omega C_3 R_3}$
    *   **Arm 4 ($Z_4$):** A purely resistive arm $R_4$. $\implies Z_4 = R_4$

**Procedure:**
To determine an unknown frequency, the components $R_1, C_1, R_3, C_3, R_2,$ and $R_4$ are adjusted until the null detector indicates a balanced bridge.

**Derivation of Frequency Expression:**
At balance, the general bridge equation is:
$$Z_1 Z_4 = Z_2 Z_3$$
It is mathematically simpler to use admittance for the parallel arm 3, so we rewrite the balance equation as:
$$\frac{Z_1}{Z_2} = \frac{Z_3}{Z_4} \implies \frac{Z_1}{Z_2} = \frac{1}{Y_3 Z_4} \implies Z_1 Y_3 = \frac{Z_2}{Z_4}$$

Substitute the impedances and admittances into this rearranged form:
$$\left( R_1 - j\frac{1}{\omega C_1} \right) \left( \frac{1}{R_3} + j\omega C_3 \right) = \frac{R_2}{R_4}$$

Expand the left side:
$$\frac{R_1}{R_3} + j\omega C_3 R_1 - j\frac{1}{\omega C_1 R_3} - j^2 \frac{\omega C_3}{\omega C_1} = \frac{R_2}{R_4}$$
Since $j^2 = -1$, the last term becomes $+ \frac{C_3}{C_1}$. Group real and imaginary parts:
$$\left( \frac{R_1}{R_3} + \frac{C_3}{C_1} \right) + j \left( \omega C_3 R_1 - \frac{1}{\omega C_1 R_3} \right) = \frac{R_2}{R_4} + j0$$

To satisfy the balance condition, the imaginary part must be zero:
$$\omega C_3 R_1 - \frac{1}{\omega C_1 R_3} = 0$$
$$\omega C_3 R_1 = \frac{1}{\omega C_1 R_3}$$
$$\omega^2 = \frac{1}{R_1 R_3 C_1 C_3}$$
$$\omega = \frac{1}{\sqrt{R_1 R_3 C_1 C_3}}$$
Since $\omega = 2\pi f$, we can substitute to find the frequency $f$:
$$2\pi f = \frac{1}{\sqrt{R_1 R_3 C_1 C_3}}$$
$$f = \frac{1}{2\pi \sqrt{R_1 R_3 C_1 C_3}}$$

If the bridge is designed symmetrically such that $R_1 = R_3 = R$ and $C_1 = C_3 = C$, the formula simplifies significantly:
$$f = \frac{1}{2\pi \sqrt{R^2 C^2}} = \frac{1}{2\pi R C}$$

Thus, by reading the values of the balanced components, the exact frequency of the power source driving the bridge is determined.

*   **Reference in eee2211 slide:** Not explicitly detailed in the provided slides.

***

### 49. Page 16, Q.5 (b): Why Maxwell's bridge is not suitable for the measurement of high Q? Explain.

**Solution:**
Maxwell's Inductance-Capacitance bridge is unsuitable for measuring coils with a high Quality Factor ($Q > 10$) due to the physical and electrical limitations of the variable resistors required for balancing.

**Explanation:**
1.  **The Q-Factor Equation:** In Maxwell's bridge, the standard capacitor ($C_4$) is placed in **parallel** with the variable tuning resistor ($R_4$). The balance equations establish that the Q-factor of the unknown coil is directly proportional to this resistance:
    $$Q = \omega C_4 R_4$$

2.  **Requirement for Extremely High Resistance:** To measure a coil with a high Q-factor (e.g., $Q = 100$), the variable resistor $R_4$ must be adjusted to a very large value. Depending on the frequency and capacitance $C_4$, this could require $R_4$ to be in the range of hundreds of kilo-ohms to several mega-ohms.

3.  **Physical Limitations (Parasitic Capacitance):** Manufacturing a high-precision, continuously variable resistor box (a decade box) that reaches into the mega-ohm range is physically difficult and expensive. More importantly, large wire-wound or composite resistors inherently suffer from **stray (parasitic) shunt capacitance** between the resistive elements and to the ground casing.

4.  **Measurement Error:** The theoretical balance equations of Maxwell's bridge assume $R_4$ is a purely resistive element. If $R_4$ is very large, the stray capacitance begins to act as a parallel AC pathway. The bridge is no longer balancing against pure $R_4$, but against a complex impedance. This completely invalidates the simple balance equations ($L_1 = R_2 R_3 C_4$ and $R_1 = \frac{R_2 R_3}{R_4}$), leading to massive errors in calculating the unknown inductance and resistance.

For these reasons, Hay's bridge (where $Q \propto 1/R_4$) is used instead for high-Q coils, as it requires a conveniently small value for $R_4$ to balance, thereby avoiding the parasitic capacitance issues associated with large resistors.

*   **Reference in eee2211 slide:** Pages 93, 94.

***

### 50. Page 16, Q.5 (c) [Repeated Below]: Draw the connection diagram and the phasor diagram of Hay's Bridge and derive necessary equations.

**Solution:**

**1. Connection Diagram:**
*   **Figure Involved:** The circuit consists of four arms connected in a diamond shape.
    *   **Arm 1 (Unknown):** Inductor $L_1$ and its internal series resistance $R_1$.
    *   **Arm 2 (Ratio Arm):** Pure non-inductive resistor $R_2$.
    *   **Arm 3 (Ratio Arm):** Pure non-inductive resistor $R_3$.
    *   **Arm 4 (Standard Arm):** A standard capacitor $C_4$ connected in **series** with a variable non-inductive resistor $R_4$.
*   An AC source is connected between the junction of Arms 1-4 and Arms 2-3. A null detector is connected between the junction of Arms 1-2 and Arms 3-4.

**2. Derivation of Necessary Equations:**
The general balance condition for an AC bridge is $Z_1 Z_4 = Z_2 Z_3$.
Substitute the arm impedances:
$$(R_1 + j\omega L_1) \left( R_4 - j\frac{1}{\omega C_4} \right) = R_2 R_3$$

Expanding the left side and substituting $j^2 = -1$:
$$R_1 R_4 - j\frac{R_1}{\omega C_4} + j\omega L_1 R_4 + \frac{L_1}{C_4} = R_2 R_3$$
Group real and imaginary terms:
$$\left( R_1 R_4 + \frac{L_1}{C_4} \right) + j\left( \omega L_1 R_4 - \frac{R_1}{\omega C_4} \right) = R_2 R_3 + j0$$

**Equating Imaginary Parts:**
$$\omega L_1 R_4 - \frac{R_1}{\omega C_4} = 0 \implies \omega L_1 R_4 = \frac{R_1}{\omega C_4}$$
$$R_1 = \omega^2 L_1 C_4 R_4 \quad \text{--- (Eq. A)}$$

**Equating Real Parts:**
$$R_1 R_4 + \frac{L_1}{C_4} = R_2 R_3$$
Substitute $R_1$ from Eq. A:
$$(\omega^2 L_1 C_4 R_4) R_4 + \frac{L_1}{C_4} = R_2 R_3$$
Multiply by $C_4$:
$$\omega^2 L_1 C_4^2 R_4^2 + L_1 = R_2 R_3 C_4$$
Factor out $L_1$ and solve:
$$L_1 (1 + \omega^2 C_4^2 R_4^2) = R_2 R_3 C_4$$
$$L_1 = \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2}$$

Now solve for $R_1$ by substituting $L_1$ back into Eq. A:
$$R_1 = \omega^2 \left( \frac{R_2 R_3 C_4}{1 + \omega^2 C_4^2 R_4^2} \right) C_4 R_4$$
$$R_1 = \frac{\omega^2 R_2 R_3 R_4 C_4^2}{1 + \omega^2 C_4^2 R_4^2}$$

**3. Phasor Diagram:**
*   **Figure Involved:** 
    *   Start with the current $I_1$ (flowing through Arm 1 and Arm 2 at balance) as the reference vector on the x-axis.
    *   The voltage drop across $R_1$ ($I_1 R_1$) is in phase with $I_1$.
    *   The voltage drop across $L_1$ ($I_1 \omega L_1$) leads $I_1$ by $90^\circ$.
    *   The total voltage drop across Arm 1 is $E_1 = I_1 R_1 + jI_1 \omega L_1$.
    *   Because Arm 2 is purely resistive, $E_2 = I_1 R_2$, which is in phase with $I_1$.
    *   At balance, $E_1 = E_4$ and $E_2 = E_3$. The total supply voltage $E = E_1 + E_2 = E_3 + E_4$.
    *   For the standard arm (Arm 4), let the current be $I_2$. The voltage drop $E_4$ consists of the drop across $R_4$ ($I_2 R_4$ in phase with $I_2$) and the drop across $C_4$ ($I_2 / \omega C_4$ lagging $I_2$ by $90^\circ$).
    *   Since $E_1 = E_4$, the vector sum of ($I_2 R_4$) and ($I_2 / \omega C_4$) must equal the vector sum of ($I_1 R_1$) and ($I_1 \omega L_1$). The phasor diagram graphically represents this equality of complex voltages.

*   **Reference in eee2211 slide:** Pages 95, 96 (Hay's Bridge connection diagram and equations).
### 51. Page 24, Notes 1: Why Q< 10 is not suited in hays bridge(10)

**Solution:**
Hay's bridge is specifically designed to overcome the limitations of Maxwell's bridge when measuring high-Q coils, but it introduces significant complexities and errors if used for low-Q coils (where $Q < 10$).

**Explanation:**
1.  **Complexity of the Inductance Equation:**
    The derived balance equation for the unknown inductance $L_1$ in a Hay's bridge is:
    $$L_1 = \frac{R_2 R_3 C_4}{1 + (\omega C_4 R_4)^2}$$
    The Q-factor of the circuit is defined as $Q = \frac{1}{\omega C_4 R_4}$. Substituting this into the inductance formula gives:
    $$L_1 = \frac{R_2 R_3 C_4}{1 + (1/Q)^2}$$
    
    *   **For High-Q coils ($Q > 10$):** The term $(1/Q)^2$ becomes less than $1/100$ ($0.01$), which is negligible compared to $1$. The denominator approximates to $1$, and the equation simplifies beautifully to $L_1 \approx R_2 R_3 C_4$. This simplified equation is independent of the operating frequency ($\omega$).
    *   **For Low-Q coils ($Q < 10$):** The term $(1/Q)^2$ is no longer negligible. For example, if $Q = 2$, then $(1/Q)^2 = 0.25$. Ignoring this would introduce a massive 25% error. Therefore, the full, complex equation must be used.

2.  **Frequency Dependence:**
    Because the full equation $L_1 = \frac{R_2 R_3 C_4}{1 + (\omega C_4 R_4)^2}$ must be used for $Q < 10$, the measurement becomes highly dependent on the operating angular frequency ($\omega = 2\pi f$). Any slight fluctuation or harmonic distortion in the AC power supply frequency will directly cause errors in the calculated inductance. 

3.  **Impractical Resistor Values:**
    In Hay's bridge, $Q = \frac{1}{\omega C_4 R_4}$. To measure a low $Q$ value, the variable balancing resistor $R_4$ must be adjusted to a very **large** value. As discussed with Maxwell's bridge, precision high-value variable resistors are expensive, physically bulky, and suffer from stray parasitic capacitance, which destroys the accuracy of the bridge. 

For these reasons, Maxwell's bridge is preferred for $Q < 10$ (because its $L_1$ formula never depends on frequency), and Hay's bridge is strictly reserved for $Q > 10$.

*   **Reference in eee2211 slide:** Page 98 (Hay's Bridge Disadvantages).

***

### 54. Page 2, Q.5. (c): A Wheatstone bridge is balanced with resistance of equal values P = Q = R = S = 10 $\Omega$ . A 9 V battery is driving the bridge. If the sensitivity of the detector galvanometer is $15^\circ$/V and there is an increase in measuring resistance by 1 $\Omega$, determine the angle of deflection shown by the galvanometer due to the unbalanced condition.

**Solution:**

**Given Data:**
*   Equal arm resistances: $P = Q = R = S = 10\ \Omega$
*   Input voltage: $E = 9\text{ V}$
*   Galvanometer voltage sensitivity: $S_V = 15^\circ/\text{V}$
*   Change in measuring resistance (unbalance): $\Delta R = 1\ \Omega$

**Step 1: Calculate the Unbalance Voltage ($E_o$ or $e$)**
When the resistance $R$ is changed to $R + \Delta R$, the bridge becomes unbalanced. The exact voltage difference between the galvanometer nodes (from the Thevenin equivalent circuit) is given by the formula:
$$E_o = E \frac{\Delta R}{4R + 2\Delta R}$$

Substitute the given values into the exact formula:
$$E_o = 9 \times \frac{1}{4(10) + 2(1)}$$
$$E_o = 9 \times \frac{1}{40 + 2}$$
$$E_o = 9 \times \frac{1}{42}$$
$$E_o = \frac{9}{42} \approx 0.21428\text{ V}$$

*(Note: The slides also show an approximation $E_o \approx \frac{E \Delta R}{4R}$ when $\Delta R \ll R$. However, since $1\ \Omega$ is $10\%$ of $10\ \Omega$, it is not strictly "much less than" $R$, so using the exact formula provides the most accurate result).*

**Step 2: Calculate the Angle of Deflection ($\theta$)**
The deflection of the galvanometer is the product of its voltage sensitivity and the unbalance voltage applied across it:
$$\theta = S_V \times E_o$$
$$\theta = 15^\circ/\text{V} \times 0.21428\text{ V}$$
$$\theta \approx 3.214^\circ$$

The angle of deflection shown by the galvanometer is approximately **$3.21^\circ$**.

*   **Reference in eee2211 slide:** Pages 62, 67 (Bridge Sensitivity & Wheatstone Bridge unbalance equations).

***

### 55. Page 6, Q.2 a): What is bridge sensitivity? Derive the expression of bridge sensitivity for a Wheatstone bridge with equal arms.

**Solution:**

**1. What is Bridge Sensitivity?**
Bridge sensitivity ($S_B$) is defined as the ratio of the deflection of the galvanometer ($\theta$) to the per-unit fractional change in the unknown resistance ($\Delta R / R$) that caused the unbalance. It measures how noticeably the bridge reacts to a tiny change in the component being measured.
$$S_B = \frac{\theta}{\Delta R / R}$$

**2. Derivation for a Wheatstone Bridge with Equal Arms:**
*   **Figure Involved:** A standard Wheatstone bridge diagram where arms $P, Q, R, S$ are initially balanced. Then, $R$ is changed to $R + \Delta R$, creating an unbalance voltage $e$ between the center nodes $d$ and $b$.

**Step A: Find the unbalance voltage ($e$)**
When $R$ changes to $R + \Delta R$, the voltage at node $d$ ($E_{ad}$) and node $b$ ($E_{ab}$) become:
$$E_{ad} = E \frac{R + \Delta R}{R + \Delta R + S}$$
$$E_{ab} = E \frac{P}{P + Q}$$
The voltage difference across the galvanometer is $e = E_{ad} - E_{ab}$. For a balanced bridge, $\frac{P}{P+Q} = \frac{R}{R+S}$.
Substituting and simplifying (as shown in the lecture notes) gives the approximate unbalance voltage for a very small $\Delta R$:
$$e \approx \frac{E S \Delta R}{(R + S)^2}$$

**Step B: Relate to Galvanometer Deflection ($\theta$)**
The galvanometer deflection is proportional to the unbalance voltage $e$, governed by its voltage sensitivity $S_v$:
$$\theta = S_v \times e$$
Substitute the expression for $e$:
$$\theta = S_v \frac{E S \Delta R}{(R + S)^2}$$

**Step C: Derive General Bridge Sensitivity ($S_B$)**
Divide the deflection by the fractional change $\Delta R / R$:
$$S_B = \frac{\theta}{\Delta R / R} = \frac{S_v \frac{E S \Delta R}{(R + S)^2}}{\frac{\Delta R}{R}}$$
$$S_B = \frac{S_v E S R}{(R + S)^2}$$
Divide numerator and denominator by $S R$:
$$S_B = \frac{S_v E}{\frac{(R+S)^2}{SR}} = \frac{S_v E}{\frac{R^2 + 2RS + S^2}{SR}} = \frac{S_v E}{\frac{R}{S} + 2 + \frac{S}{R}}$$
Since at balance $\frac{R}{S} = \frac{P}{Q}$, we can write:
$$S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}$$

**Step D: Apply "Equal Arms" Condition**
For a bridge with equal arms, $P = Q = R = S$. Therefore, the ratio $P/Q = 1$ and $Q/P = 1$.
Substitute these into the general equation:
$$S_B = \frac{S_v E}{1 + 1 + 2}$$
$$S_B = \frac{S_v E}{4}$$

This is the final expression for the bridge sensitivity of a Wheatstone bridge with equal arms.

*   **Reference in eee2211 slide:** Pages 56, 61, 62, 63.

***

### 56. Page 7, Q.2 (a): Derive the equation of bridge sensitivity of Wheatstone bridge. What are the advantages and limitations of Wheatstone bridge?

**Solution:**

**1. Derivation of the Equation of Bridge Sensitivity:**
*(Note: This derivation is identical to Steps A through C in Question 55).*
*   **Definition:** Bridge sensitivity is $S_B = \frac{\theta}{\Delta R / R}$.
*   **Unbalance Voltage:** When resistance $R$ changes by a small amount $\Delta R$, the voltage across the galvanometer becomes $e \approx \frac{E S \Delta R}{(R + S)^2}$.
*   **Deflection:** The galvanometer deflection is $\theta = S_v \times e = S_v \frac{E S \Delta R}{(R + S)^2}$.
*   **Sensitivity Equation:** 
    $$S_B = \frac{\theta}{\Delta R / R} = \frac{S_v \frac{E S \Delta R}{(R + S)^2}}{\frac{\Delta R}{R}} = \frac{S_v E S R}{(R + S)^2}$$
    By expanding the denominator and substituting the balance ratio $\frac{R}{S} = \frac{P}{Q}$, the general expression is derived as:
    $$S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}$$

**2. Advantages of Wheatstone Bridge:**
*   **High Accuracy:** Because it is a "null" measurement method, the accuracy is independent of the exact calibration of the galvanometer (which only needs to accurately detect zero) and is highly immune to minor fluctuations in the supply voltage $E$.
*   **Wide Range:** It can measure a fairly wide range of medium resistances (typically from $1\ \Omega$ to several $\text{M}\Omega$) with high precision.
*   **Simplicity:** The circuit is relatively simple to construct and operate.

**3. Limitations of Wheatstone Bridge:**
As explicitly outlined in the course materials:
*   **Component Tolerances:** The actual value of the fixed resistances $P, Q,$ and $S$ may be slightly different from their marked (nominal) values, introducing systemic errors.
*   **Galvanometer Sensitivity:** If the galvanometer is not sufficiently sensitive, a small unbalance will not produce a visible deflection, making it impossible to find the exact null point.
*   **Contact and Lead Resistance:** The contact resistances of the binding posts and the resistance of the connecting leads add to the unknown resistance $R$. While negligible for high resistances, this causes severe errors when trying to measure low resistances (below $1\ \Omega$).
*   **Heating Errors ($I^2R$ Loss):** The current flowing through the bridge arms causes $I^2R$ power dissipation, which heats the resistors. If they have a high temperature coefficient, their resistance values will change during the measurement, drifting the balance point.
*   **Not suitable for very high resistances:** For extremely high resistances (like insulation), the current becomes too small for the galvanometer to detect unbalance effectively.

*   **Reference in eee2211 slide:** Page 35 (Limitations), Pages 56, 61, 62, 63 (Sensitivity Derivation).
### 57. Page 9, Q.1. (c): Define bridge sensitivity. Find the expression for current through the galvanometer for a small unbalance in the Wheatstone bridge.

**Solution:**

**1. Definition of Bridge Sensitivity:**
Bridge sensitivity ($S_B$) is defined as the ratio of the deflection of the galvanometer ($\theta$) to the per-unit fractional change in the unknown resistance ($\Delta R / R$) that caused the bridge to become unbalanced. 
$$S_B = \frac{\theta}{\Delta R / R}$$
It indicates how responsive the bridge is to tiny variations in the component being measured.

**2. Expression for Current through the Galvanometer for a Small Unbalance:**
To find the current through the galvanometer when the bridge is slightly unbalanced, we apply Thevenin's theorem across the galvanometer terminals.

*   **Figure Involved:** A standard Wheatstone bridge circuit. Arms $P$ and $Q$ form one side; arms $R$ and $S$ form the other. The battery $E$ is applied across the top and bottom nodes. The galvanometer $G$ is connected between the center nodes $a$ and $c$.

**Step A: Find the Thevenin Equivalent Voltage ($E_o$)**
Assume the bridge is initially balanced ($P/Q = R/S$). Then, resistance $R$ is changed by a small amount $\Delta R$. The voltage difference between the galvanometer terminals (with the galvanometer removed) is the Thevenin voltage $E_o$.
As derived in the slides, the exact unbalance voltage is:
$$E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{P}{P + Q} \right]$$
Since the bridge was initially balanced, $\frac{P}{P+Q} = \frac{R}{R+S}$. Substituting this:
$$E_o = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{R}{R + S} \right]$$
$$E_o = E \left[ \frac{(R + \Delta R)(R + S) - R(R + \Delta R + S)}{(R + \Delta R + S)(R + S)} \right]$$
$$E_o = E \left[ \frac{R^2 + RS + R\Delta R + S\Delta R - R^2 - R\Delta R - RS}{(R + \Delta R + S)(R + S)} \right]$$
$$E_o = \frac{E S \Delta R}{(R + S)^2 + \Delta R(R + S)}$$
For a *small* unbalance, $\Delta R$ is very small compared to $(R+S)$. Therefore, the term $\Delta R(R+S)$ in the denominator can be neglected. The approximated Thevenin voltage is:
$$E_o \approx \frac{E S \Delta R}{(R + S)^2}$$
*(Note: If the bridge has equal arms $P=Q=R=S$, this simplifies further to $E_o \approx \frac{E \Delta R}{4R}$).*

**Step B: Find the Thevenin Equivalent Resistance ($R_{th}$ or $R_o$)**
To find the Thevenin resistance, short-circuit the voltage source $E$ and look into the circuit from the galvanometer terminals. 
The resistance consists of arm $P$ in parallel with $Q$, in series with arm $(R+\Delta R)$ in parallel with $S$.
$$R_o = \frac{PQ}{P+Q} + \frac{(R+\Delta R)S}{(R+\Delta R)+S}$$
Since the unbalance is small ($\Delta R \ll R$), we can ignore $\Delta R$ in this resistance calculation for simplicity. Furthermore, if we assume a bridge with equal arms ($P=Q=R=S$), the Thevenin resistance simplifies to:
$$R_o = \frac{R \cdot R}{R+R} + \frac{R \cdot R}{R+R} = \frac{R}{2} + \frac{R}{2} = R$$

**Step C: Calculate the Galvanometer Current ($I_g$)**
According to Thevenin's theorem, the current through the galvanometer is the Thevenin voltage divided by the total series resistance (Thevenin resistance + Galvanometer resistance $G$):
$$I_g = \frac{E_o}{R_o + G}$$

Substituting the expressions for a generic small unbalance:
$$I_g = \frac{\frac{E S \Delta R}{(R + S)^2}}{R_o + G}$$

If specifically requested for an **equal arm bridge** ($P=Q=R=S$):
Substitute $E_o = \frac{E \Delta R}{4R}$ and $R_o = R$:
$$I_g = \frac{\frac{E \Delta R}{4R}}{R + G} = \frac{E \Delta R}{4R(R + G)}$$

*   **Reference in eee2211 slide:** Pages 56 (Definition), Pages 68, 69 (Thevenin derivation and current formula).

***

### 58. Page 27, CT#04 SEC: C Q2: Derive the expression for the galvanometer current in a Wheatstone Bridge.

**Solution:**
*(Note: This question asks for the same derivation as the second part of Q57. We will present the full Thevenin derivation specifically focused on the general case, leading up to the equal-arm simplification).*

To find the current $I_g$ flowing through the galvanometer of resistance $G$ in an unbalanced Wheatstone bridge, we use Thevenin's Theorem.

*   **Figure Involved:** 
    1.  The standard Wheatstone bridge circuit with arms $P, Q, R, S$, galvanometer $G$, and battery $E$.
    2.  The Thevenin equivalent circuit showing a voltage source $E_o$ in series with the Thevenin resistance $R_o$ and the galvanometer $G$.

**Step 1: Determine Thevenin Voltage ($E_o$)**
Remove the galvanometer. The voltage $E_o$ is the open-circuit potential difference between the center nodes $a$ and $c$ (or $d$ and $b$ depending on node naming).
Let the arm $R$ change by a small amount $\Delta R$ to create the unbalance.
The voltage at the left node is determined by the voltage divider of $(R+\Delta R)$ and $S$:
$$V_{left} = E \left[ \frac{R + \Delta R}{(R + \Delta R) + S} \right]$$
The voltage at the right node is determined by the voltage divider of $P$ and $Q$:
$$V_{right} = E \left[ \frac{P}{P + Q} \right]$$
The open-circuit Thevenin voltage is the difference:
$$E_o = V_{left} - V_{right} = E \left[ \frac{R + \Delta R}{R + S + \Delta R} - \frac{P}{P + Q} \right]$$
If the bridge was initially balanced ($\frac{P}{P+Q} = \frac{R}{R+S}$), this simplifies (as shown in previous derivations) to:
$$E_o = \frac{E S \Delta R}{(R + S)^2 + \Delta R(R + S)}$$
For a small unbalance ($\Delta R \rightarrow 0$), the $\Delta R$ term in the denominator is negligible:
$$E_o \approx \frac{E S \Delta R}{(R + S)^2}$$

**Step 2: Determine Thevenin Resistance ($R_o$)**
Short-circuit the battery $E$. Looking into the bridge from the galvanometer nodes, the resistance $P$ is in parallel with $Q$, and the resistance $(R+\Delta R)$ is in parallel with $S$. These two parallel combinations are in series with each other.
$$R_o = \left( \frac{PQ}{P + Q} \right) + \left( \frac{(R + \Delta R)S}{R + \Delta R + S} \right)$$
For a small unbalance, we ignore $\Delta R$ in this calculation:
$$R_o \approx \frac{PQ}{P + Q} + \frac{RS}{R + S}$$

**Step 3: Calculate Galvanometer Current ($I_g$)**
Connect the galvanometer $G$ back into the Thevenin equivalent circuit. The current $I_g$ is the Thevenin voltage divided by the total circuit resistance.
$$I_g = \frac{E_o}{R_o + G}$$
Substituting the general expressions:
$$I_g = \frac{\frac{E S \Delta R}{(R + S)^2}}{\left( \frac{PQ}{P + Q} + \frac{RS}{R + S} \right) + G}$$

**Simplification for Equal Arms ($P=Q=R=S$):**
If all arms are equal to $R$:
*   $E_o \approx \frac{E \cdot R \cdot \Delta R}{(R + R)^2} = \frac{E R \Delta R}{4R^2} = \frac{E \Delta R}{4R}$
*   $R_o \approx \frac{R \cdot R}{R + R} + \frac{R \cdot R}{R + R} = \frac{R}{2} + \frac{R}{2} = R$
*   Therefore, $I_g = \frac{\frac{E \Delta R}{4R}}{R + G} = \frac{E \Delta R}{4R(R + G)}$

*   **Reference in eee2211 slide:** Pages 68, 69.

***

### 59. Page 30, CT#01 SEC: A QB: Prove that the bridge sensitivity of a Wheatstone bridge, [blank space/missing formula]; where the symbols having their usual meaning.

*(Note: The prompt indicates a missing formula. Based on the standard curriculum for this topic, the intended question is to prove the general bridge sensitivity formula: $S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}$. We will provide the proof for this).*

**Solution:**

**Objective:** Prove that the bridge sensitivity $S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}$

**Definition:**
Bridge sensitivity is defined as the ratio of galvanometer deflection to the fractional change in the unknown resistance:
$$S_B = \frac{\theta}{\Delta R / R}$$

**Proof:**
1.  **Unbalance Voltage ($e$):** Let a balanced Wheatstone bridge (where $P/Q = R/S$) be unbalanced by changing resistance $R$ to $R + \Delta R$. As established in previous derivations, the exact unbalance voltage $e$ across the galvanometer is:
    $$e = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{P}{P + Q} \right]$$
    Substitute $\frac{P}{P+Q} = \frac{R}{R+S}$ (from the initial balance condition):
    $$e = E \left[ \frac{R + \Delta R}{R + \Delta R + S} - \frac{R}{R + S} \right]$$
    Finding a common denominator and simplifying the numerator:
    $$e = E \left[ \frac{(R + \Delta R)(R + S) - R(R + \Delta R + S)}{(R + \Delta R + S)(R + S)} \right]$$
    $$e = E \left[ \frac{R^2 + RS + R\Delta R + S\Delta R - R^2 - R\Delta R - RS}{(R + \Delta R + S)(R + S)} \right]$$
    $$e = \frac{E S \Delta R}{(R + \Delta R + S)(R + S)}$$
    For a very small unbalance, $\Delta R \ll (R+S)$, so we can drop $\Delta R$ from the denominator term $(R + \Delta R + S)$:
    $$e \approx \frac{E S \Delta R}{(R + S)^2}$$

2.  **Galvanometer Deflection ($\theta$):** The deflection is proportional to the unbalance voltage, scaled by the galvanometer's voltage sensitivity $S_v$:
    $$\theta = S_v \cdot e = S_v \frac{E S \Delta R}{(R + S)^2}$$

3.  **Substitute into Sensitivity Formula:**
    $$S_B = \frac{\theta}{\Delta R / R} = \frac{S_v \frac{E S \Delta R}{(R + S)^2}}{\frac{\Delta R}{R}}$$
    $$S_B = \frac{S_v E S R \Delta R}{\Delta R (R + S)^2}$$
    $$S_B = \frac{S_v E S R}{(R + S)^2}$$

4.  **Algebraic Manipulation:**
    Divide the numerator and the denominator by the term $(SR)$:
    $$S_B = \frac{S_v E}{\frac{(R + S)^2}{SR}}$$
    Expand the squared term in the denominator:
    $$S_B = \frac{S_v E}{\frac{R^2 + 2RS + S^2}{SR}}$$
    Divide each term in the denominator by $SR$:
    $$S_B = \frac{S_v E}{\frac{R^2}{SR} + \frac{2RS}{SR} + \frac{S^2}{SR}}$$
    $$S_B = \frac{S_v E}{\frac{R}{S} + 2 + \frac{S}{R}}$$

5.  **Final Substitution:**
    Since the bridge was initially balanced, we know that $\frac{R}{S} = \frac{P}{Q}$. It therefore follows that the inverse is also true: $\frac{S}{R} = \frac{Q}{P}$.
    Substitute these ratios into the equation:
    $$S_B = \frac{S_v E}{\frac{P}{Q} + 2 + \frac{Q}{P}}$$
    Rearranging the terms in the denominator yields the final proven formula:
    $$S_B = \frac{S_v E}{\frac{P}{Q} + \frac{Q}{P} + 2}$$

*   **Reference in eee2211 slide:** Pages 61, 62, 63.
