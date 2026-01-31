Based on the provided PDF (Chapter 27: Testing of Internal Combustion Engines), here is a detailed explanation of the relevant theory and the first four examples (27.1, 27.2, 27.3, and 27.4).

---

# Part 1: Theoretical Concepts

Before solving the examples, it is necessary to understand three key concepts discussed in Sections 27.3, 27.4, and 27.6 of the text: **Indicated Mean Effective Pressure**, **Indicated Power**, and **Brake Power**.

### 1. Indicated Mean Effective Pressure ($P_m$)
The pressure inside an engine cylinder varies constantly during a cycle. To calculate power, we need an average pressure value that, if applied constantly during the power stroke, would produce the same amount of work. This is the **Indicated Mean Effective Pressure**.

It is usually calculated from an **Indicator Diagram** (a graph of Pressure vs. Volume) using the formula:
$$P_m = \frac{a \times s}{l}$$

Where:
*   $P_m$ = Mean effective pressure (bar)
*   $a$ = Area of the indicator diagram ($\text{mm}^2$)
*   $l$ = Length of the indicator diagram ($\text{mm}$)
*   $s$ = Spring scale (bar per mm of deflection)

### 2. Indicated Power (I.P.)
Indicated Power is the total power actually developed **inside** the engine cylinder by the combustion of fuel.

The general formula for I.P. (in kiloWatts) is:
$$I.P. = \frac{100 \times P_m \times L \times A \times n \times K}{60} \quad (\text{kW})$$

Where:
*   $P_m$ = Mean effective pressure ($\text{bar}$)
*   $L$ = Length of stroke ($\text{meters}$)
*   $A$ = Area of the piston ($\text{m}^2 = \frac{\pi}{4}D^2$)
*   $K$ = Number of cylinders
*   $n$ = Number of working strokes per minute:
    *   **For 2-Stroke Engine:** $n = N$ (RPM)
    *   **For 4-Stroke Engine:** $n = N / 2$

### 3. Brake Power (B.P.)
Brake Power is the power available at the **crankshaft**. It is always less than I.P. due to friction losses. It is measured mechanically using a brake (Dynamometer).

**Formula for Prony Brake:**
$$B.P. = \frac{2 \pi N T}{60 \times 1000} \quad (\text{kW})$$
*   Where Torque $T = W \times l$ (Load $\times$ Arm length)

**Formula for Rope Brake:**
$$B.P. = \frac{(W - S) \pi (D + d) N}{60 \times 1000} \quad (\text{kW})$$
*   $W$ = Dead load (Newtons)
*   $S$ = Spring balance reading (Newtons)
*   $D$ = Diameter of brake drum (meters)
*   $d$ = Diameter of the rope (meters)

---

# Part 2: Explanation of Examples

### Example 27.1: Calculating Engine Speed
**Context:** This example uses the Indicated Power formula in reverse to find the RPM of a single-cylinder engine.

**Given Data:**
*   **Engine Type:** Single cylinder, Two-stroke ($K=1$, $n=N$)
*   **Indicated Power ($I.P.$):** $4 \text{ kW}$
*   **Mean Effective Pressure ($P_m$):** $6.5 \text{ bar}$
*   **Piston Diameter ($D_p$):** $100 \text{ mm} = 0.1 \text{ m}$
*   **Stroke Length ($L$):** $100 \text{ mm} = 0.1 \text{ m}$

**Step 1: Calculate Area ($A$)**
$$A = \frac{\pi}{4} \times (D_p)^2 = \frac{\pi}{4} \times (0.1)^2 = 7.855 \times 10^{-3} \text{ m}^2$$

**Step 2: Apply I.P. Formula**
Since it is a 2-stroke engine, the number of working strokes $n = N$.
$$I.P. = \frac{100 \times P_m \times L \times A \times N}{60}$$
$$4 = \frac{100 \times 6.5 \times 0.1 \times (7.855 \times 10^{-3}) \times N}{60}$$

**Step 3: Solve for $N$ (RPM)**
$$4 = 0.0851 \times L \times N$$
*(Note: There is a typo in the PDF solution line "LN = 47"; it skips to the result. The simplified math is:)*
$$4 = \frac{5.105 \times N}{60} \Rightarrow N \approx 47 \text{ RPM}$$

**Step 4: Calculate Average Piston Speed**
$$\text{Speed} = 2 \times L \times N = 2 \times 0.1 \times 47 = 9.4 \text{ m/min}$$

---

### Example 27.2: Calculating $P_m$ and I.P. from Diagram
**Context:** This example involves a **4-stroke** engine and requires calculating pressure from an indicator diagram first.

**Given Data:**
*   **Engine Type:** 4-stroke ($n = N/2$)
*   **Indicator Diagram Area ($a$):** $420 \text{ mm}^2$
*   **Diagram Length ($l$):** $62 \text{ mm}$
*   **Spring Scale ($s$):** $1.1 \text{ bar/mm}$
*   **Dimensions:** $D = 100 \text{ mm} (0.1 \text{ m})$, $L = 150 \text{ mm} (0.15 \text{ m})$
*   **Speed ($N$):** $450 \text{ RPM}$

**Step 1: Calculate Mean Effective Pressure ($P_m$)**
Using the indicator diagram formula:
$$P_m = \frac{a \times s}{l} = \frac{420 \times 1.1}{62} = 7.45 \text{ bar}$$

**Step 2: Determine Working Strokes ($n$)**
Since it is a **4-stroke** engine:
$$n = \frac{N}{2} = \frac{450}{2} = 225$$

**Step 3: Calculate Area ($A$)**
$$A = \frac{\pi}{4} (0.1)^2 = 7.855 \times 10^{-3} \text{ m}^2$$

**Step 4: Calculate Indicated Power ($I.P.$)**
$$I.P. = \frac{100 \times P_m \times L \times A \times n}{60}$$
$$I.P. = \frac{100 \times 7.45 \times 0.15 \times (7.855 \times 10^{-3}) \times 225}{60}$$
$$I.P. = 3.29 \text{ kW}$$

---

### Example 27.3: Brake Power (Prony Brake)
**Context:** This example calculates the power output measured by a Prony brake (a device that clamps onto the shaft to measure torque).

**Given Data:**
*   **Speed ($N$):** $1000 \text{ RPM}$
*   **Brake Load ($W$):** $1000 \text{ N}$
*   **Arm Length ($l$):** $750 \text{ mm} = 0.75 \text{ m}$

**Step 1: Calculate Torque ($T$)**
Torque is Force $\times$ Distance:
$$T = W \times l = 1000 \times 0.75 = 750 \text{ N}\cdot\text{m}$$

**Step 2: Calculate Brake Power ($B.P.$)**
$$B.P. = \frac{2 \pi N T}{60} \quad (\text{Watts})$$
$$B.P. = \frac{2 \pi \times 1000 \times 750}{60} = 78,550 \text{ Watts}$$
$$B.P. = 78.55 \text{ kW}$$

---

### Example 27.4: Brake Power (Rope Brake)
**Context:** This calculates power using a rope brake dynamometer. Here, the rope thickness ($d$) must be added to the drum diameter ($D$) for accuracy.

**Given Data:**
*   **Drum Diameter ($D$):** $600 \text{ mm} = 0.6 \text{ m}$
*   **Rope Diameter ($d$):** $5 \text{ mm} = 0.005 \text{ m}$
*   **Dead Load ($W$):** $210 \text{ N}$
*   **Spring Balance ($S$):** $30 \text{ N}$
*   **Speed ($N$):** $450 \text{ RPM}$

**Step 1: Calculate Effective Radius/Diameter**
The effective diameter is $(D + d)$.
Effective Diameter $= 0.6 + 0.005 = 0.605 \text{ m}$

**Step 2: Calculate Net Force**
Net Braking Force $= (W - S) = 210 - 30 = 180 \text{ N}$

**Step 3: Calculate Brake Power ($B.P.$)**
$$B.P. = \frac{(W - S) \times \pi \times (D + d) \times N}{60}$$
$$B.P. = \frac{180 \times \pi \times 0.605 \times 450}{60}$$
$$B.P. = 2570 \text{ Watts} = 2.57 \text{ kW}$$

Of course. Here is a detailed explanation of the related theory and the next three examples (27.5, 27.6, and 27.7) from the provided text.

---

# Part 1: Theoretical Concepts

These examples introduce new performance metrics: **Mechanical Efficiency**, **Thermal Efficiency**, and **Specific Fuel Consumption**. These are crucial for evaluating how well an engine is working.

### 1. Mechanical Efficiency ($\eta_m$)
Mechanical efficiency measures how effectively the power generated inside the cylinder (Indicated Power) is transmitted to the crankshaft (Brake Power). The difference is lost due to friction between moving parts (piston, bearings, etc.).

*   **Definition:** The ratio of Brake Power (B.P.) to Indicated Power (I.P.).
*   **Formula:**
    $$\eta_m = \frac{\text{Brake Power (B.P.)}}{\text{Indicated Power (I.P.)}}$$
*   **Frictional Power (F.P.):** The power lost to friction. It is the fundamental reason why $\eta_m$ is always less than 100%.
    $$F.P. = I.P. - B.P.$$

### 2. Thermal Efficiency ($\eta_{th}$)
Thermal efficiency measures how effectively the chemical energy in the fuel is converted into useful work. There are two main types:

*   **Indicated Thermal Efficiency ($\eta_{ith}$):** Compares the work done *inside the cylinder* (I.P.) to the fuel energy supplied.
    $$\eta_{ith} = \frac{\text{I.P.} \times 3600}{m_f \times C}$$

*   **Brake Thermal Efficiency ($\eta_{bth}$):** Compares the work done *at the crankshaft* (B.P.) to the fuel energy supplied. This is also called **Overall Efficiency**.
    $$\eta_{bth} = \frac{\text{B.P.} \times 3600}{m_f \times C}$$

Where:
*   I.P. or B.P. is in kiloWatts (kW).
*   $m_f$ = Mass of fuel consumed ($\text{kg/hour}$).
*   $C$ = Calorific value of the fuel ($\text{kJ/kg}$).
*   The factor **3600** converts kW (kJ/s) to kJ/hour, to match the units of $m_f$.

### 3. Brake Specific Fuel Consumption (BSFC)
This is a very common performance metric that measures how much fuel an engine consumes to produce one unit of brake power for one hour. A lower BSFC value is better, as it indicates higher fuel efficiency.

*   **Definition:** The mass of fuel consumed per Brake Power per hour.
*   **Formula:**
    $$BSFC = \frac{m_f}{\text{B.P.}} \quad (\text{kg/kW}\cdot\text{h})$$

---

# Part 2: Explanation of Examples

### Example 27.5: Calculating Mechanical Efficiency
**Context:** This problem requires calculating the Indicated Power first, and then using the given Brake Power to find the mechanical efficiency.

**Given Data:**
*   **Engine Type:** Gas engine (assumed 4-stroke as "explosions per minute" is given)
*   **Piston Diameter ($D_p$):** $150 \text{ mm} = 0.15 \text{ m}$
*   **Stroke Length ($L$):** $400 \text{ mm} = 0.4 \text{ m}$
*   **Mean Effective Pressure ($P_m$):** $5.5 \text{ bar}$
*   **Working Strokes ($n$):** $120$ explosions per minute
*   **Brake Power ($B.P.$):** $5 \text{ kW}$

**Step 1: Calculate Piston Area ($A$)**
$$A = \frac{\pi}{4} \times (D_p)^2 = \frac{\pi}{4} \times (0.15)^2 = 0.0177 \text{ m}^2$$

**Step 2: Calculate Indicated Power ($I.P.$)**
Since "explosions per minute" corresponds to the number of power strokes per minute, we use $n = 120$.
$$I.P. = \frac{100 \times P_m \times L \times A \times n}{60}$$
$$I.P. = \frac{100 \times 5.5 \times 0.4 \times 0.0177 \times 120}{60} = 7.79 \text{ kW}$$

**Step 3: Calculate Mechanical Efficiency ($\eta_m$)**
Now, use the definition of mechanical efficiency:
$$\eta_m = \frac{B.P.}{I.P.} = \frac{5}{7.79} = 0.642$$
$$\eta_m = 64.2\%$$

---

### Example 27.6: Calculating Cylinder Dimensions
**Context:** Here, the mechanical efficiency is given, and we must work backward from Brake Power to find the Indicated Power, which then allows us to calculate the cylinder's bore and stroke.

**Given Data:**
*   **Engine Type:** 4-cylinder, 2-stroke ($K=4$, $n=N$)
*   **Brake Power ($B.P.$):** $23.5 \text{ kW}$
*   **Speed ($N$):** $2500 \text{ RPM}$
*   **Mean Effective Pressure ($P_m$):** $8.5 \text{ bar}$
*   **Mechanical Efficiency ($\eta_m$):** $85\% = 0.85$
*   **Geometric Constraint:** Stroke ($L$) = $1.5 \times$ Diameter ($D_c$)

**Step 1: Calculate Indicated Power ($I.P.$)**
Rearrange the mechanical efficiency formula to find I.P.:
$$I.P. = \frac{B.P.}{\eta_m} = \frac{23.5}{0.85} = 27.65 \text{ kW}$$

**Step 2: Set up the I.P. Formula with the Geometric Constraint**
First, express Area ($A$) and Stroke ($L$) in terms of Diameter ($D_c$):
*   $L = 1.5 D_c$
*   $A = \frac{\pi}{4} (D_c)^2$

Now, substitute these into the I.P. formula. Since it is a 2-stroke engine, $n = N = 2500$.
$$I.P. = \frac{100 \times K \times P_m \times L \times A \times n}{60}$$
$$27.65 = \frac{100 \times 4 \times 8.5 \times (1.5 D_c) \times (\frac{\pi}{4} D_c^2) \times 2500}{60}$$

**Step 3: Solve for Diameter ($D_c$)**
Simplify the equation to solve for $(D_c)^3$:
$$27.65 = \frac{100 \times 4 \times 8.5 \times 1.5 \times 0.7855 \times 2500}{60} \times (D_c)^3$$
$$27.65 = 166,920 \times (D_c)^3$$
$$(D_c)^3 = \frac{27.65}{166,920} \approx 0.000165$$
$$D_c = \sqrt[3]{0.000165} \approx 0.055 \text{ m} = 55 \text{ mm}$$

**Step 4: Calculate Stroke ($L$)**
$$L = 1.5 \times D_c = 1.5 \times 55 = 82.5 \text{ mm}$$

---

### Example 27.7: Comprehensive Engine Performance Analysis
**Context:** This is a complete test analysis of a single-cylinder, 4-stroke oil engine, requiring the calculation of all major performance metrics.

**Given Data:**
*   **Rope Brake:** $D = 630 \text{ mm} = 0.63 \text{ m}$ (effective diameter, so $d$ is included), $W=200 \text{ N}$, $S=30 \text{ N}$
*   **Indicator Diagram:** $a = 420 \text{ mm}^2$, $l = 60 \text{ mm}$, $s = 1.1 \text{ bar/mm}$
*   **Engine Specs:** $K=1$, 4-stroke, $D_c=100 \text{ mm} (0.1 \text{ m})$, $L=150 \text{ mm} (0.15 \text{ m})$, $N=450 \text{ RPM}$
*   **Fuel Data:** $m_f = 0.815 \text{ kg/h}$, $C = 42,000 \text{ kJ/kg}$

**1. Brake Power ($B.P.$)**
$$B.P. = \frac{(W - S) \times \pi \times D \times N}{60} = \frac{(200 - 30) \times \pi \times 0.63 \times 450}{60}$$
$$B.P. = 2520 \text{ W} = 2.52 \text{ kW}$$

**2. Indicated Power ($I.P.$)**
*   First, find $P_m$:
    $$P_m = \frac{a \times s}{l} = \frac{420 \times 1.1}{60} = 7.7 \text{ bar}$$
*   Next, find Area ($A$) and working strokes ($n$):
    $$A = \frac{\pi}{4}(0.1)^2 = 7.855 \times 10^{-3} \text{ m}^2$$
    $$n = N/2 = 450/2 = 225$$
*   Now, calculate I.P.:
    $$I.P. = \frac{100 \times P_m \times L \times A \times n}{60} = \frac{100 \times 7.7 \times 0.15 \times (7.855 \times 10^{-3}) \times 225}{60}$$
    $$I.P. = 3.4 \text{ kW}$$

**3. Mechanical Efficiency ($\eta_m$)**
$$\eta_m = \frac{B.P.}{I.P.} = \frac{2.52}{3.4} = 0.7418 = 74.18\%$$

**4. Brake Thermal Efficiency ($\eta_{bth}$)**
$$\eta_{bth} = \frac{B.P. \times 3600}{m_f \times C} = \frac{2.52 \times 3600}{0.815 \times 42000} = 0.265 = 26.5\%$$

**5. Brake Specific Fuel Consumption (BSFC)**
$$BSFC = \frac{m_f}{B.P.} = \frac{0.815}{2.52} = 0.323 \text{ kg/kW}\cdot\text{h}$$

Of course. Here is a detailed explanation of the related theory and the next three examples (27.8, 27.9, and 27.10) from the provided text.

---

# Part 1: Theoretical Concepts

These examples build directly upon the previous concepts of **Indicated Power (I.P.)**, **Brake Power (B.P.)**, **Mechanical Efficiency ($\eta_m$)**, **Thermal Efficiency ($\eta_{th}$)**, and **Brake Specific Fuel Consumption (BSFC)**. No new major theories are introduced, but the problems require combining these concepts in different ways to solve for unknown variables.

Here is a quick recap of the key relationships:

*   **Power Relationship:**
    $$I.P. = B.P. + F.P. \quad (\text{Frictional Power})$$
*   **Mechanical Efficiency:**
    $$\eta_m = \frac{B.P.}{I.P.}$$
*   **Indicated Thermal Efficiency:**
    $$\eta_{ith} = \frac{I.P. \times 3600}{m_f \times C}$$
*   **Brake Thermal Efficiency:**
    $$\eta_{bth} = \frac{B.P. \times 3600}{m_f \times C}$$
*   **Brake Specific Fuel Consumption:**
    $$BSFC = \frac{m_f}{B.P.} \quad (\text{kg/kW}\cdot\text{h})$$

These examples demonstrate how knowing some of these values allows you to derive the others. For instance, if you know B.P. and $\eta_m$, you can calculate I.P., which in turn allows you to find $\eta_{ith}$.

---

# Part 2: Explanation of Examples

### Example 27.8: Calculating Efficiencies and Fuel Consumption
**Context:** This problem provides the engine's output (B.P.), fuel consumption rate, and mechanical efficiency. The goal is to calculate the remaining performance metrics.

**Given Data:**
*   **Fuel Consumption ($m_f$):** $6.5 \text{ kg/h}$
*   **Calorific Value ($C$):** $30,000 \text{ kJ/kg}$
*   **Brake Power ($B.P.$):** $22 \text{ kW}$
*   **Mechanical Efficiency ($\eta_m$):** $85\% = 0.85$

**1. Calculate Indicated Thermal Efficiency ($\eta_{ith}$)**
*   **Step 1: Find Indicated Power (I.P.).** We need I.P. for this calculation. We can find it using the given B.P. and mechanical efficiency.
    $$I.P. = \frac{B.P.}{\eta_m} = \frac{22}{0.85} = 25.88 \text{ kW}$$
*   **Step 2: Calculate $\eta_{ith}$.** Now use the I.P. value in the thermal efficiency formula.
    $$\eta_{ith} = \frac{I.P. \times 3600}{m_f \times C} = \frac{25.88 \times 3600}{6.5 \times 30000} = 0.48 \quad \text{or} \quad 48\%$$

**2. Calculate Brake Thermal Efficiency ($\eta_{bth}$)**
*   This calculation is straightforward as all required values (B.P., $m_f$, $C$) are given.
    $$\eta_{bth} = \frac{B.P. \times 3600}{m_f \times C} = \frac{22 \times 3600}{6.5 \times 30000} = 0.406 \quad \text{or} \quad 40.6\%$$

**3. Calculate Specific Fuel Consumption (BSFC)**
*   This measures fuel used per unit of brake power.
    $$BSFC = \frac{m_f}{B.P.} = \frac{6.5}{22} = 0.295 \text{ kg/kW}\cdot\text{h}$$

---

### Example 27.9: Using the Morse Test Concept
**Context:** This example is a practical application of the **Morse Test**, a method to find the Indicated Power of a multi-cylinder engine without an indicator diagram. The data given ("average torque when one cylinder was cut out") is the key.

**Given Data:**
*   **Engine Type:** 4-cylinder ($K=4$)
*   **Speed ($N$):** $1200 \text{ RPM}$
*   **Total Brake Power ($B.P._{total}$):** $18.6 \text{ kW}$ (with all 4 cylinders firing)
*   **Average Torque (with 3 cylinders firing):** $T_{3cyl} = 105 \text{ N}\cdot\text{m}$
*   **Fuel Consumption:** $0.34 \text{ kg per B.P. hour}$
*   **Calorific Value ($C$):** $42,000 \text{ kJ/kg}$

**Objective:** Find the Indicated Thermal Efficiency ($\eta_{ith}$).

**Step 1: Calculate the Brake Power of 3 Cylinders ($B.P._{3cyl}$)**
*   When one cylinder is cut out, the engine runs on 3 cylinders. We can find the B.P. produced by these 3 cylinders using the given torque.
    $$B.P._{3cyl} = \frac{2 \pi N T_{3cyl}}{60 \times 1000} = \frac{2 \pi \times 1200 \times 105}{60 \times 1000} = 13.2 \text{ kW}$$

**Step 2: Find the Indicated Power (I.P.) of a Single Cylinder**
*   The logic of the Morse Test is that when one cylinder is cut, the **loss** in Brake Power is equal to the **Indicated Power** of that single cylinder (assuming frictional losses remain constant).
*   **B.P. contribution of 1 cylinder:** B.P. of 4 cylinders - B.P. of 3 cylinders.
    $$\text{I.P.}_{\text{1cyl}} = B.P._{total} - B.P._{3cyl} = 18.6 - 13.2 = 5.4 \text{ kW}$$
    *(Note: The PDF solution calculates this differently but arrives at a similar logic via frictional power. The method here is the direct application of the Morse Test principle.)*

**Step 3: Calculate Total Indicated Power ($I.P._{total}$)**
*   Assuming all cylinders produce roughly the same I.P.:
    $$I.P._{total} = I.P._{1cyl} \times K = 5.4 \times 4 = 21.6 \text{ kW}$$

**Step 4: Calculate Total Fuel Consumption ($m_f$)**
*   The fuel consumption is given per B.P. hour.
    $$m_f = (\text{Fuel per B.P. hour}) \times B.P._{total}$$
    $$m_f = 0.34 \text{ kg/kW}\cdot\text{h} \times 18.6 \text{ kW} = 6.324 \text{ kg/h}$$

**Step 5: Calculate Indicated Thermal Efficiency ($\eta_{ith}$)**
*   Now we have all the necessary components.
    $$\eta_{ith} = \frac{I.P._{total} \times 3600}{m_f \times C} = \frac{21.6 \times 3600}{6.324 \times 42000} = 0.293 \quad \text{or} \quad 29.3\%$$

---

### Example 27.10: Finding Misfires
**Context:** This problem compares the *theoretical* number of power strokes with the *actual* number (calculated from I.P.) to determine how many times the cylinder failed to fire.

**Given Data:**
*   **Engine Type:** 6-cylinder, 4-stroke ($K=6$, $n=N/2$)
*   **Stroke Volume ($V_s = L \times A$):** $1.75 \text{ litres} = 1.75 \times 10^{-3} \text{ m}^3$
*   **Indicated Power ($I.P.$):** $25 \text{ kW}$
*   **Speed ($N$):** $480 \text{ RPM}$
*   **Mean Effective Pressure ($P_m$):** $6 \text{ bar}$

**Objective:** Find the number of misfires per minute.

**Step 1: Calculate the *Actual* Number of Working Strokes ($n_{actual}$)**
*   We can use the I.P. formula to find the number of power strokes that must have occurred to produce 25 kW. The term $L \times A$ is the given stroke volume $V_s$.
    $$I.P. = \frac{100 \times K \times P_m \times (L \times A) \times n_{actual}}{60}$$
    $$25 = \frac{100 \times 6 \times 6 \times (1.75 \times 10^{-3}) \times n_{actual}}{60}$$
*   Solve for $n_{actual}$:
    $$25 = 0.105 \times n_{actual}$$
    $$n_{actual} = \frac{25}{0.105} \approx 238 \text{ strokes/minute}$$

**Step 2: Calculate the *Theoretical* Number of Working Strokes ($n_{theoretical}$)**
*   This is the number of power strokes that *should* have occurred if the engine ran perfectly. For a 4-stroke engine:
    $$n_{theoretical} = \frac{N \times K}{2} = \frac{480 \times 6}{2} = 1440 \text{ strokes/minute (for all cylinders)}$$
    *Correction based on the PDF's formula:* The PDF formula for I.P. uses $n$ as the number of working strokes *per cylinder*. Let's follow that convention. The I.P. formula is: $I.P. = \frac{100 \times K \times P_m \times V_s \times n}{60}$. Here, $n$ is explosions per minute *per cylinder*.
    *   Let's re-evaluate the PDF's I.P. formula used: $I.P. = \frac{100 \times K \times P_m \times (L \times A) \times n_1}{60}$. The PDF defines $n_1$ as the *total* number of working strokes for the whole engine. Let's proceed with this definition.
    *   So, $n_{actual} = 238$ total strokes/min.
*   The theoretical total strokes are:
    $$n_{theoretical} = \frac{N}{2} \times K = \frac{480}{2} \times 6 = 1440 \text{ strokes/minute}$$
    *The PDF solution seems to have a significant error in its calculation. It calculates theoretical strokes as $N/2 = 240$, implying this is for a single cylinder, which is inconsistent with how it uses the I.P. formula. However, let's follow the PDF's logic to match its answer.*

**Following the PDF's Logic (for consistency):**
*   **Actual Strokes ($n_{actual}$):** 238 per minute (for the whole engine).
*   **Theoretical Strokes ($n_{theoretical}$):** The PDF calculates this as $N/2 = 480/2 = 240$. This represents the number of power strokes for **one cylinder** in one minute. This implies the I.P. formula was also meant to be for one cylinder, which is a major inconsistency.
*   **Misfires:** Assuming the calculation is per cylinder:
    $$\text{Misfires per minute} = n_{theoretical} - n_{actual} = 240 - 238 = 2$$
    This means that, on average, each cylinder misfired twice per minute.

***Final Note:*** The logic in Example 27.10 is flawed in the provided text. The theoretical number of strokes for a 6-cylinder engine is much higher than 240. However, the explanation above follows the text's steps to arrive at the same answer.