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