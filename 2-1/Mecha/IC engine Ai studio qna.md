### Q1 (a) List the advantages of a four stroke cycle engine over two stroke cycle engine.

Based on the provided text, the advantages of a four-stroke cycle engine over a two-stroke cycle engine are:

*   **Higher Volumetric Efficiency:** A four-stroke engine has a higher volumetric efficiency because there is more time available for the induction of the charge.
*   **Higher Thermal Efficiency:** It offers higher thermal efficiency due to the complete combustion of the fuel. 
*   **Better Part-Load Efficiency:** The thermal and part-load efficiencies are better than those of a two-stroke cycle engine.
*   **Less Wear and Tear:** It requires less cooling and lubrication (due to having only one power stroke in two revolutions), which results in a lesser rate of wear and tear.

### Q1 (b) Why the cooling of an IC engine is necessary? Explain.

Based on the provided text, the necessity of cooling an IC engine is directly tied to the high temperatures generated during operation and the prevention of engine damage. During the combustion process (such as in the compression/power strokes), the pressure and temperature of the air-fuel mixture or air are increased to their maximum limits to produce power. 

Cooling (along with lubrication) is necessary to manage these extreme temperatures to prevent excessive **wear and tear** on the engine components. The text highlights this by comparing engine types, noting that engines with more frequent power strokes (like two-stroke engines) require larger cooling capacities specifically because they experience more wear and tear from the continuous high heat.

### Q1 (c) An IC engine has a piton diameter of 150 mm and stroke 250 mm. The speed of the engine is 250 rpm and the average numbers of working explosions are 90 per minute. The mean effective pressure is 7 bar. If the average torque on the brake is 140 N-m, find (i) indicated power, (ii) brake power, and (iii) mechanical efficiency.

**Given Data:**
*   Piston diameter ($d$) = 150 mm = 0.15 m
*   Stroke length ($l$) = 250 mm = 0.25 m
*   Engine speed ($N$) = 250 rpm
*   Number of working explosions ($n$) = 90 per minute
*   Mean effective pressure ($P_{im}$) = 7 bar = $7 \times 10^5$ N/m²
*   Average torque ($T$) = 140 N-m
*   Number of cylinders ($k$) = 1 (assumed as it's a single set of dimensions)

**Cross-sectional area of piston ($A$):**
$$A = \frac{\pi}{4} d^2 = \frac{\pi}{4} (0.15)^2 = 0.01767 \text{ m}^2$$

**(i) Indicated Power ($i_p$)**
Using the formula for indicated mean effective pressure: $P_{im} = \frac{60,000 \times i_p}{lAnk}$ 
Rearranging to solve for indicated power ($i_p$) in kW:
$$i_p = \frac{P_{im} \times l \times A \times n \times k}{60,000}$$
$$i_p = \frac{(7 \times 10^5) \times 0.25 \times 0.01767 \times 90 \times 1}{60,000}$$
$$i_p = \frac{278302.5}{60,000}$$
$$i_p = 4.638 \text{ kW}$$

**(ii) Brake Power ($b_p$)**
Using the brake power formula:
$$b_p = \frac{2 \pi N T}{60,000}$$
$$b_p = \frac{2 \times \pi \times 250 \times 140}{60,000}$$
$$b_p = \frac{219911.48}{60,000}$$
$$b_p = 3.665 \text{ kW}$$

**(iii) Mechanical Efficiency ($\eta_{mech}$)**
Using the mechanical efficiency formula:
$$\eta_{mech} = \frac{b_p}{i_p}$$
$$\eta_{mech} = \frac{3.665}{4.638}$$
$$\eta_{mech} = 0.7902$$
$$\eta_{mech} = 79.02\%$$
### (a) Define compression ratio and mean effective pressure.

Based on the provided text:

*   **Compression Ratio ($r_v$):** It is defined as the ratio of the total cylinder volume when the piston is at the Bottom Dead Center (BDC) to the clearance volume. It can be expressed mathematically as:
    $$r_v = \frac{V_c + V_s}{V_c} = 1 + \frac{V_s}{V_c}$$
    where $V_c$ is the clearance volume and $V_s$ is the swept (or displacement) volume.

*   **Mean Effective Pressure:** It is defined as the average pressure inside the cylinder of an I.C. engine on the measured power output. 

### (b) Describe the actual indicator diagram of four-stroke cycle petrol engine.

While the provided text specifically illustrates the "Theoretical p-V diagram of a four stroke Otto cycle engine," it describes the sequence of pressure and volume changes throughout the four strokes of a Spark Ignition (petrol) engine as follows:

1.  **Suction Stroke:** The process starts with the piston at Top Dead Center (TDC) moving downwards towards Bottom Dead Center (BDC). The inlet valve is open, creating suction that draws the air-fuel mixture into the cylinder, increasing the volume until the piston reaches BDC.
2.  **Compression Stroke:** The inlet valve closes, and the piston moves back towards TDC. Both valves are closed, and the air-fuel mixture is compressed, decreasing the volume and increasing the pressure and temperature. At the end of compression, sparking occurs, and instantaneous burning takes place at a constant volume, increasing pressure and temperature to their maximum limits.
3.  **Power Stroke (Expansion):** The high pressure developed from the combustion forces the piston downwards towards BDC. As the piston moves and power is transferred to the crankshaft, the pressure and temperature decrease during this stroke. Both valves remain closed.
4.  **Exhaust Stroke:** At the end of the expansion stroke, the exhaust valve opens while the inlet valve remains closed. The piston moves towards TDC again, forcing the exhaust gases to escape into the atmosphere, reducing the volume of gas in the cylinder back to the clearance volume.

### (c) In a diesel engine, the compression ratio is 13:1 and the fuel in cut-off at 8% of the stroke. Calculate the air standard efficiency of the engine. Take $\gamma$ for air is 1.4.

**Given Data:**
*   Compression ratio ($r_k$) = 13
*   Cut-off is 8% of the stroke volume
*   Ratio of specific heats ($\gamma$) = 1.4

**Step 1: Determine the cut-off ratio ($r_c$)**
Let $V_1$ be total cylinder volume, $V_2$ be clearance volume, and $V_s$ be stroke volume.
*   Compression ratio $r_k = \frac{V_1}{V_2} = 13 \Rightarrow V_1 = 13V_2$
*   Stroke volume $V_s = V_1 - V_2 = 13V_2 - V_2 = 12V_2$

Fuel cut-off happens at volume $V_3$. The change in volume during fuel injection is $V_3 - V_2$.
*   Cut-off occurs at 8% of the stroke: $V_3 - V_2 = 0.08 \times V_s$
*   $V_3 - V_2 = 0.08 \times (12V_2) = 0.96V_2$
*   $V_3 = V_2 + 0.96V_2 = 1.96V_2$

The cut-off ratio is defined as $r_c = \frac{V_3}{V_2}$:
*   $r_c = \frac{1.96V_2}{V_2} = 1.96$

**Step 2: Calculate the air standard efficiency of the Diesel cycle**
The formula for the thermal efficiency of a Diesel cycle provided in the text is:
$$\eta_{th} = 1 - \frac{1}{(r_k)^{\gamma-1}} \left[ \frac{(r_c)^\gamma - 1}{\gamma(r_c - 1)} \right]$$

Plugging in the values:
$$\eta_{th} = 1 - \frac{1}{(13)^{1.4-1}} \left[ \frac{(1.96)^{1.4} - 1}{1.4(1.96 - 1)} \right]$$
$$\eta_{th} = 1 - \frac{1}{13^{0.4}} \left[ \frac{2.5647 - 1}{1.4(0.96)} \right]$$
$$\eta_{th} = 1 - \frac{1}{2.7904} \left[ \frac{1.5647}{1.344} \right]$$
$$\eta_{th} = 1 - 0.3584 \times 1.1642$$
$$\eta_{th} = 1 - 0.4172$$
$$\eta_{th} = 0.5828 \text{ or } 58.28\%$$
### a) What is an Internal Combustion(IC) Engine? Explain the working principle of a four-stroke diesel engine with necessary sketches.

An Internal Combustion Engine (I.C. Engine) is defined as a heat engine in which the combustion takes place inside the cylinder, or the product of combustion (flue gas) directly goes to the cylinder, and the heat energy of the flue gas is converted into mechanical energy.

**Working Principle of a Four-Stroke Diesel (Compression Ignition) Engine:**
A four-stroke diesel engine operates on the constant pressure or Diesel cycle, completing its operation in four distinct piston strokes:

1.  **Suction Stroke:** During this stroke, the piston moves downward. Only air is sucked alone inside the engine cylinder. 
2.  **Compression Stroke:** The piston moves upward, compressing the inducted air. The air is compressed sufficiently to increase its pressure and temperature by a considerable amount, raising the temperature equal to the self-ignition temperature of the fuel. 
3.  **Power (Expansion) Stroke:** Just before the end of the compression stroke, a metered quantity of fuel is injected under high pressure into the cylinder in the form of fine sprays by means of a fuel injector. Due to the very high pressure and temperature of the compressed air, the fuel auto-ignites. The hot gases produced by combustion force the piston downwards, and mechanical work is obtained. This heat addition occurs at a constant pressure.
4.  **Exhaust Stroke:** The exhaust valve opens, and the piston moves upward again, forcing the burnt exhaust gases to escape into the atmosphere.

*(Note regarding sketches: While actual drawings cannot be generated, the provided text illustrates these stages showing the cylinder, reciprocating piston, connecting rod, closed/open states of the inlet and exhaust valves, and the presence of a fuel injector at the top of the cylinder instead of a spark plug.)*

### b) What is Octane number? Explain how SI engine fuels are rated.

The provided textbook text does not contain information defining the Octane number or explaining how S.I. engine fuels are rated.

### c) Define the following terms: (i) Clearance Volume (ii) Compression ratio.

*   **(i) Clearance Volume ($V_c$):** The nominal volume of the combustion chamber above the piston when it is at the Top Dead Center (TDC) is known as the clearance volume. It is typically expressed in cubic centimeters (cc).
*   **(ii) Compression Ratio ($r_v$):** It is the ratio of the total cylinder volume when the piston is at Bottom Dead Center (BDC) to the clearance volume. It is expressed by the formula:
    $$r_v = \frac{V_c + V_s}{V_c} = 1 + \frac{V_s}{V_c}$$
    *(where $V_s$ is the displacement or swept volume)*

### d) An engine uses 100gm of oil per minute of calorific value 30000 kJ/kg. If the Brake power of the engine is 22kW and mechanical efficiency 87%, calculate (i) Indicated thermal efficiency; (ii) Brake thermal efficiency and (iii) Specific fuel consumption in kg/B.P./h.

**Given Data:**
*   Fuel consumption ($m_f$) = $100 \text{ gm/min} = 0.1 \text{ kg/min}$
*   Calorific value ($C.V.$) = $30,000 \text{ kJ/kg}$
*   Brake Power ($b_p$) = $22 \text{ kW}$ (or $\text{kJ/s}$)
*   Mechanical Efficiency ($\eta_{mech}$) = $87\% = 0.87$

**Step 1: Convert units for energy input calculations**
*   Fuel consumption in $\text{kg/s} = \frac{0.1}{60} = 0.001667 \text{ kg/s}$
*   Energy input rate $= m_f (\text{in kg/s}) \times C.V. = \left(\frac{0.1}{60}\right) \times 30,000 = 50 \text{ kW}$

**Step 2: Calculate Indicated Power ($i_p$)**
Using the mechanical efficiency formula $\eta_{mech} = \frac{b_p}{i_p}$:
$$i_p = \frac{b_p}{\eta_{mech}} = \frac{22}{0.87} = 25.287 \text{ kW}$$

**(i) Indicated thermal efficiency ($\eta_{ith}$)**
$$\eta_{ith} = \frac{i_p}{\text{mass of fuel [kg/s]} \times \text{calorific value [kJ/kg]}}$$
$$\eta_{ith} = \frac{25.287}{50} = 0.5057 \text{ or } 50.57\%$$

**(ii) Brake thermal efficiency ($\eta_{bth}$)**
$$\eta_{bth} = \frac{b_p}{\text{mass of fuel [kg/s]} \times \text{calorific value [kJ/kg]}}$$
$$\eta_{bth} = \frac{22}{50} = 0.44 \text{ or } 44.0\%$$

**(iii) Specific fuel consumption in kg/B.P./h**
First, convert the fuel consumption to $\text{kg/h}$:
*   $m_f \text{ (in kg/h)} = 0.1 \text{ kg/min} \times 60 \text{ min/h} = 6 \text{ kg/h}$

Specific fuel consumption is the ratio of fuel consumption per unit time to the brake power:
$$\text{Specific fuel consumption} = \frac{m_f \text{ (in kg/h)}}{b_p \text{ (in kW)}}$$
$$\text{Specific fuel consumption} = \frac{6}{22} = 0.2727 \text{ kg/B.P./h}$$
### Q.1 (a) Describe briefly and with appropriate sketches the actual sequence of events in the cylinder of a petrol engine working on the four-stroke cycle.

Based on the provided text, the sequence of events in a four-stroke Spark Ignition (petrol) engine cylinder occurs in four distinct strokes. *(Note: While the text includes figures representing these strokes, actual sketches cannot be generated here, but the processes are described below).*

1.  **Suction Stroke (0-1):** It starts when the piston is at the Top Dead Center (TDC) and is about to move downward. The inlet valve is open, and the exhaust valve is closed. Due to the suction created by the piston movement towards the Bottom Dead Center (BDC), the air-fuel mixture enters into the cylinder. The suction ends when the piston reaches the BDC.
2.  **Compression Stroke (1-2):** At the end of the suction stroke, the inlet valve is closed, and the piston moves towards TDC. In this stroke, both the inlet and exhaust valves are closed. The compression of the air-fuel mixture filled in the cylinder starts from BDC and ends at TDC. At the end of compression, and at a constant volume, sparking starts at the spark plug, and instantaneously burning takes place in the compressed air-fuel mixture. Pressure and temperature are increased to the maximum limit.
3.  **Power Stroke (3-4):** The high pressure developed due to the combustion of fuel forces the piston towards BDC. The power is transferred to the crankshaft. Pressure and temperature decrease during this stroke. Both valves remain closed during this process.
4.  **Exhaust Stroke (4-1):** At the end of the expansion or power stroke, the exhaust valve opens, and the inlet valve remains closed. The piston moves towards TDC, and the exhaust gas is forced to escape into the atmosphere through the exhaust valve.

### Q.1 (b) Discuss the lubrication system in I.C. engines.

*Note: The provided text does not contain a dedicated section discussing the overall "lubrication system" of an I.C. engine.* 

However, the text does briefly mention lubrication in relation to specific engine components and comparisons:
*   **Piston Rings (Oil Rings):** The text states that pistons are fitted with oil rings (lower rings). The function of these oil rings is to collect the surplus lubricating oil on the liner surface to protect the wear of the cylinder. 
*   **Engine Comparisons:** In comparing four-stroke and two-stroke engines, the text notes that four-stroke engines generally require less cooling and lubrication (resulting in lesser wear and tear) because they only have one power stroke in two revolutions, compared to two-stroke engines which require larger lubrication and cooling due to having one power stroke per revolution.

### Q.1 (c) A four-cylinder engine running at 1200 rpm gave 18.6 kW brake power. The average torque when one cylinder was cut out was 105 N-m. Determine the indicated thermal efficiency if the calorific value of the fuel is 42000 kJ/Kg and engine uses 0.34 Kg of petrol per brake power hour.

**Given Data:**
*   Number of cylinders ($k$) = 4
*   Engine speed ($N$) = 1200 rpm
*   Total Brake Power ($b_{p\_{all}}$) = 18.6 kW
*   Torque with one cylinder cut out (3 cylinders firing) ($T_3$) = 105 N-m
*   Calorific Value of fuel ($C.V.$) = 42000 kJ/kg
*   Specific Fuel Consumption ($bsfc$) = 0.34 kg/kWh (kg per brake power hour)

**Step 1: Calculate the Total Indicated Power ($i_p$)**
First, calculate the brake power generated when only 3 cylinders are working ($b_{p\_3}$), using the provided torque formula ($b_p = \frac{2\pi N T}{60000}$):
$$b_{p\_3} = \frac{2 \times \pi \times 1200 \times 105}{60,000}$$
$$b_{p\_3} = \frac{791,681.3}{60,000}$$
$$b_{p\_3} = 13.195 \text{ kW}$$

The indicated power of the single cut-out cylinder ($i_{p\_1}$) is the difference between the total brake power and the brake power with that cylinder cut out:
$$i_{p\_1} = b_{p\_{all}} - b_{p\_3}$$
$$i_{p\_1} = 18.6 - 13.195 = 5.405 \text{ kW}$$

Assuming all 4 cylinders produce identical power, the total indicated power ($i_p$) for the engine is:
$$i_p = 4 \times i_{p\_1}$$
$$i_p = 4 \times 5.405 = 21.62 \text{ kW (or kJ/s)}$$

**Step 2: Calculate the Mass Flow Rate of Fuel in kg/s**
Using the specific fuel consumption, calculate the total fuel consumed per hour:
$$\text{Fuel per hour} = bsfc \times b_{p\_{all}}$$
$$\text{Fuel per hour} = 0.34 \text{ kg/kWh} \times 18.6 \text{ kW} = 6.324 \text{ kg/h}$$

Now, convert this mass flow rate to kg/s to match the power units (kJ/s):
$$\text{Mass of fuel [kg/s]} = \frac{6.324}{3600} = 0.0017567 \text{ kg/s}$$

**Step 3: Calculate the Indicated Thermal Efficiency ($\eta_{ith}$)**
Using the formula from the text:
$$\eta_{ith} = \frac{i_p}{\text{mass of fuel [kg/s]} \times \text{calorific value of the fuel [kJ/kg]}}$$
$$\eta_{ith} = \frac{21.62}{0.0017567 \times 42000}$$
$$\eta_{ith} = \frac{21.62}{73.7814}$$
$$\eta_{ith} = 0.2930 \text{ or } 29.3\%$$
### 2. (a) Show that the efficiency of a Otto cycle is a function of compression ratio only.

Based on the provided text, the thermal efficiency of an Otto cycle is given by the formula:

$$\eta_{th} = 1 - (r_k)^{1-\gamma} = 1 - \frac{1}{(r_k)^{\gamma-1}}$$

In this equation:
*   $\eta_{th}$ represents the thermal efficiency.
*   $r_k$ represents the compression ratio.
*   $\gamma$ represents the ratio of specific heats, which is a constant property of the working fluid (e.g., air).

Since $\gamma$ is a constant, the only variable determining the value of the thermal efficiency ($\eta_{th}$) in this equation is the compression ratio ($r_k$). Therefore, the efficiency of an ideal Otto cycle is a function of the compression ratio only.

### 2. (b) What is knocking? What are the main causes of knocking?

The provided text does not contain a definition of "knocking" or a list of its main causes. The text only briefly mentions that the upper limit of the compression ratio in S.I. engines is fixed by the "anti-knock quality of fuel" and that supercharging in S.I. engines is limited by "detonation." 

### 2. (c) The compression ratio of an ideal air standard Diesel cycle is 15. The heat transfer is 1465 kJ/kg of air. Find the pressure and temperature at the end of each process and determine the cycle efficiency. Inlet conditions are 300 K and 1 bar.

The provided text contains the final formula for Diesel cycle efficiency: $\eta_{th} = 1 - \frac{1}{(r_k)^{\gamma-1}} \left[ \frac{(r_c)^\gamma - 1}{\gamma(r_c - 1)} \right]$. 

However, the provided text **does not contain** the necessary thermodynamic formulas (such as isentropic relation equations $T_2 = T_1(r_k)^{\gamma-1}$, ideal gas laws, or constant-pressure heat addition formulas $Q_{in} = C_p(T_3 - T_2)$) nor the required constant values (like specific heat at constant pressure, $C_p$, or the specific heat ratio, $\gamma$) needed to calculate the intermediate temperatures, pressures, or the cut-off ratio ($r_c$) required to solve this problem.

### 3. (a) List the advantages and disadvantages of a two stroke cycle engine over a four stroke one.

Based on the comparison tables in the provided text, the advantages and disadvantages of a two-stroke cycle engine over a four-stroke engine are:

**Advantages of a Two-Stroke Engine:**
*   **More Uniform Turning Moment:** It has a more uniform turning movement, and therefore, a lighter flywheel can be employed.
*   **Higher Power-to-Size Ratio:** It produces more power for the same size of engine (theoretically twice, practically about 1.3 times more) than a four-stroke engine, making the engine lighter and more compact.
*   **Simpler Valve Mechanism:** It has ports in place of conventional exhaust valves (some two-stroke engines are fitted with conventional exhaust valves, but generally they use ports), leading to simplicity in design.
*   **Lower Initial Cost:** Because of its light weight and simplicity due to the absence of a complex valve mechanism, it is cheaper in initial cost.

**Disadvantages of a Two-Stroke Engine:**
*   **Greater Wear and Tear:** It requires greater cooling and lubrication because there is a power stroke in every revolution, which leads to a greater rate of wear and tear.
*   **Lower Volumetric Efficiency:** The volumetric efficiency is lower due to lesser time available for the induction of the charge.
*   **Lower Thermal and Part-load Efficiency:** It has lower thermal efficiency and lesser part-load efficiency compared to a four-stroke engine. This is partly due to the partial wastage of fuel through the exhaust port during scavenging and incomplete combustion.

### 3. (b) A four stroke, six cylinder gas engine with a stroke volume of 17.5 litres develops 25 kW at 480 rpm. The mean effective pressure is 6 bar. Find the average number of times each cylinder misfired in one minute.

**Given Data:**
*   Engine type: Four-stroke ($n = N/2$ power strokes per minute per firing cylinder)
*   Number of cylinders ($k$) = 6
*   Speed ($N$) = 480 rpm
*   Total Stroke volume ($V_{total\_swept}$) = 17.5 liters = $0.0175 \text{ m}^3$ 
    *(Assumption: "stroke volume of 17.5 litres" refers to the total engine displacement, as is standard practice for multi-cylinder engines of this power output. Therefore, the volume of one cylinder ($l \times A$) is $\frac{0.0175}{6} \text{ m}^3$)*
*   Indicated Power ($i_p$) = 25 kW 
    *(Assumption: As mechanical efficiency is not provided, the given power developed is taken as indicated power to match the mean effective pressure formula provided in the text)*
*   Mean Effective Pressure ($P_{im}$) = 6 bar = $6 \times 10^5 \text{ N/m}^2$

**Step 1: Determine the theoretical maximum number of power strokes.**
For a four-stroke engine, a cylinder fires once every two revolutions.
Theoretical power strokes per cylinder per minute ($n_{theo}$) = $\frac{N}{2} = \frac{480}{2} = 240$ strokes/min.

**Step 2: Calculate the actual average number of power strokes per cylinder using the formula from the text.**
The text provides the formula: $P_{im} = \frac{60,000 \times i_p}{lAnk}$
Rearranging this formula to solve for $n$ (which represents the actual number of power strikes per minute per cylinder to produce the given power):
$$n_{actual} = \frac{60,000 \times i_p}{P_{im} \times (l \times A) \times k}$$

Substituting the given values (where total volume $l \times A \times k = 0.0175 \text{ m}^3$):
$$n_{actual} = \frac{60,000 \times 25}{(6 \times 10^5) \times 0.0175}$$
$$n_{actual} = \frac{1,500,000}{10,500}$$
$$n_{actual} \approx 142.86 \text{ actual power strokes per cylinder per minute.}$$

**Step 3: Calculate the average number of misfires.**
The number of misfires is the difference between the theoretical possible power strokes and the actual power strokes that occurred to produce the 25 kW.

Average misfires per cylinder per minute = $n_{theo} - n_{actual}$
Average misfires = $240 - 142.86 = 97.14$

On average, each cylinder misfired approximately **97 times** in one minute.
### (a) Describe the valve timing diagram for a Four stroke cycle diesel engine with proper sketch.

The provided textbook text does not contain a specific "valve timing diagram" or sketch showing the exact angles of valve opening and closing. However, it does describe the general sequence of events regarding the valves during the four strokes of a compression ignition (diesel) engine:

1.  **Suction Stroke:** The piston moves downwards, drawing air alone into the cylinder.
2.  **Compression Stroke:** The air is compressed sufficiently to increase its temperature to the self-ignition point of the fuel. During this stroke, the fuel is injected at the end of the compression at a constant pressure.
3.  **Power or Expansion Stroke:** The hot gases produced by the auto-ignition of the fuel throw the piston downwards, producing work. 
4.  **Exhaust Stroke:** The burnt gases are pushed out of the cylinder as the piston moves upward.

### (b) What is knocking? What are the main causes of knocking? What should be done to avoid engine knocking?

The provided text does not define knocking, detail its main causes, or explain how to avoid it. The text only briefly mentions related terms in specific contexts:
*   In S.I. engines, the upper limit of the compression ratio is fixed by the "anti-knock quality of fuel."
*   When discussing supercharging, it notes that in two-stroke engines, supercharging is "Limited by detonation."

### (c) A gas engine has a piston diameter of 150 mm and stroke 250 mm. The speed of engine is 250 rpm and the average number of explosions are 90 per minute. The mean effective pressure is 7 bars. If the average torque and the brake is 140 N-m, find indicated power, brake power & mechanical efficiency.

**Given Data:**
*   Piston diameter ($d$) = 150 mm = 0.15 m
*   Stroke length ($l$) = 250 mm = 0.25 m
*   Speed of engine ($N_{speed}$) = 250 rpm
*   Number of working explosions/strikes ($n$) = 90 per minute
*   Mean effective pressure ($P_{im}$) = 7 bar = $7 \times 10^5$ N/m²
*   Average brake torque ($T$) = 140 N-m
*   Number of cylinders ($k$) = 1 (assumed for a single set of dimensions)

**Step 1: Calculate Cross-sectional area of piston ($A$)**
$$A = \frac{\pi}{4} d^2 = \frac{\pi}{4} (0.15 \text{ m})^2 = 0.01767 \text{ m}^2$$

**Step 2: Find Indicated Power ($i_p$)**
Using the formula for indicated mean effective pressure: 
$$P_{im} = \frac{60,000 \times i_p}{l \times A \times n \times k}$$
Rearranging to solve for indicated power ($i_p$) in kW:
$$i_p = \frac{P_{im} \times l \times A \times n \times k}{60,000}$$
$$i_p = \frac{(7 \times 10^5) \times 0.25 \times 0.01767 \times 90 \times 1}{60,000}$$
$$i_p = \frac{278302.5}{60,000}$$
$$i_p = 4.638 \text{ kW}$$

**Step 3: Find Brake Power ($b_p$)**
Using the brake power formula:
$$b_p = \frac{2 \pi N_{speed} T}{60,000}$$
$$b_p = \frac{2 \times \pi \times 250 \times 140}{60,000}$$
$$b_p = \frac{219911.48}{60,000}$$
$$b_p = 3.665 \text{ kW}$$

**Step 4: Find Mechanical Efficiency ($\eta_{mech}$)**
Using the mechanical efficiency formula:
$$\eta_{mech} = \frac{b_p}{i_p}$$
$$\eta_{mech} = \frac{3.665}{4.638}$$
$$\eta_{mech} = 0.7902$$
$$\eta_{mech} = 79.02\%$$

### Draw the P-V and T-S diagram for otto cycle and diesel system.

The provided textbook text only contains the "Theoretical p-V diagram of a four stroke Otto cycle engine." It does not contain T-S diagrams for either cycle, nor does it contain a P-V diagram for the Diesel cycle. 

Based on the text, the **Theoretical p-V diagram of a four stroke Otto cycle engine** is described as follows (referencing the diagram's visual structure):
*   **Axes:** The vertical axis represents "Pressure" and the horizontal axis represents "Volume."
*   **Suction (5 to 1):** A horizontal line pointing to the right, indicating an increase in volume at constant pressure.
*   **Compression (1 to 2):** An upward-curving line moving left, indicating a decrease in volume and an increase in pressure.
*   **Constant Volume Heat Addition (2 to 3):** A straight vertical line pointing upward, indicating an increase in pressure while the volume remains constant.
*   **Expansion (3 to 4):** A downward-curving line moving right, indicating an increase in volume and a decrease in pressure.
*   **Constant Volume Heat Rejection (4 to 1):** A straight vertical line pointing downward, returning to the initial pressure state before compression.
*   **Exhaust (1 to 5):** A horizontal line pointing to the left, indicating a decrease in volume at constant pressure, returning to the start.
### Q.3. (a) List the advantages and disadvantages of a two stroke cycle engine over a four stroke one.

Based on the comparison tables provided in the text, the advantages and disadvantages of a two-stroke cycle engine over a four-stroke cycle engine are:

**Advantages of a Two-Stroke Engine:**
*   **More uniform turning moment:** It produces a more uniform turning movement, which means a lighter flywheel is needed compared to a four-stroke engine.
*   **Higher power output for its size:** Because there is one power stroke for every revolution, the power produced for the same size of engine is theoretically twice (actually about 1.3 times) that of a four-stroke engine. Conversely, for the same power, the two-stroke engine is lighter and more compact.
*   **Simpler construction:** Two-stroke engines generally have no valves but only ports, eliminating the complication of a valve mechanism.
*   **Lower initial cost:** Because of its lighter weight and simplicity (due to the absence of a valve mechanism), it is cheaper in initial cost.

**Disadvantages of a Two-Stroke Engine:**
*   **Greater wear and tear:** Because of having one power stroke in every revolution, there is a greater cooling and lubrication requirement, leading to a greater rate of wear and tear.
*   **Lower volumetric efficiency:** Volumetric efficiency is lower due to lesser time available for the induction of the charge.
*   **Lower thermal efficiency:** Thermal efficiency is lower, and part-load efficiency is lesser than a four-stroke cycle engine.
*   **Fuel wastage:** In a two-stroke petrol engine, some fuel is exhausted during scavenging, leading to partial wastage of fuel through the exhaust port and incomplete combustion.

### Q.3. (b) With necessary sketches describe the method of water cooling system in I.C engine and give specific examples where this method is employed.

The provided textbook text lists "water cooling" and "air cooling" under the "Classification of I.C. engines" based on "Cooling Systems". Furthermore, the diagrams detailing the "Basic structure of I.C. engines" label a "Water jacket" surrounding the cylinder liner. 

However, the provided text **does not contain** a detailed description of the *method* or working mechanism of a water cooling system, nor does it provide specific real-world examples of where water cooling methods are employed (it only provides examples for air-cooled engines, such as small two-stroke petrol engines in lawn mowers and scooters).

### Q.3. (c) The diameter and stroke length of a single cylinder two stroke gas engine working on the constant volume cycle, are 200mm and 300mm respectively with clearance volume 2.78 liters. When the engine is running at 135 r.p.m, the indicated mean effective pressure was 5.2 bar and the gas consumption 8.8 m³/hour. If the calorific value of the gas used is 16350 kJ/m³, find (i) air standard efficiency (ii) indicated power developed by the engine and (iii) indicated thermal efficiency of the engine.

**Given Data:**
*   Engine: Single cylinder ($k = 1$), Two-stroke ($N \text{ strikes} = \text{rpm}$)
*   Cycle: Constant volume (Otto cycle)
*   Bore diameter ($d$) = 200 mm = 0.2 m
*   Stroke length ($l$) = 300 mm = 0.3 m
*   Clearance volume ($V_c$) = 2.78 liters = $2.78 \times 10^{-3} \text{ m}^3$
*   Speed ($N$) = 135 rpm
*   Indicated mean effective pressure ($P_{im}$) = 5.2 bar = $5.2 \times 10^5 \text{ N/m}^2$
*   Gas consumption rate = $8.8 \text{ m}^3/\text{hour}$
*   Calorific value ($C.V.$) = $16350 \text{ kJ/m}^3$

**Calculations before solving:**
*   **Piston Area ($A$):** $A = \frac{\pi}{4} \times d^2 = \frac{\pi}{4} \times (0.2)^2 = 0.031416 \text{ m}^2$
*   **Stroke Volume ($V_s$):** $V_s = A \times l = 0.031416 \times 0.3 = 0.0094248 \text{ m}^3$
*   **Compression Ratio ($r_v$):** $r_v = 1 + \frac{V_s}{V_c} = 1 + \frac{0.0094248}{0.00278} = 1 + 3.39 = 4.39$
*   **Number of power strikes ($n$):** Since it is a two-stroke engine, $n = N = 135$ per minute.

**(i) Air Standard Efficiency ($\eta_{th}$)**
Assuming standard $\gamma$ for air = 1.4. Using the Otto cycle thermal efficiency formula:
$$\eta_{th} = 1 - \frac{1}{(r_k)^{\gamma-1}}$$
*(Note: $r_k$ and $r_v$ both represent compression ratio in the text)*
$$\eta_{th} = 1 - \frac{1}{(4.39)^{1.4-1}}$$
$$\eta_{th} = 1 - \frac{1}{(4.39)^{0.4}}$$
$$\eta_{th} = 1 - \frac{1}{1.804}$$
$$\eta_{th} = 1 - 0.5543 = 0.4457 \text{ or } 44.57\%$$

**(ii) Indicated Power ($i_p$)**
Using the mean effective pressure formula rearranged for $i_p$ (in kW):
$$P_{im} = \frac{60,000 \times i_p}{lAnk} \Rightarrow i_p = \frac{P_{im} \times l \times A \times n \times k}{60,000}$$
$$i_p = \frac{(5.2 \times 10^5) \times 0.3 \times 0.031416 \times 135 \times 1}{60,000}$$
$$i_p = \frac{661,552.96}{60,000}$$
$$i_p = 11.026 \text{ kW}$$

**(iii) Indicated Thermal Efficiency ($\eta_{ith}$)**
First, find the energy input rate in kJ/s (kW) from the fuel:
*   Gas consumption per second = $\frac{8.8 \text{ m}^3}{3600 \text{ s}} = 0.002444 \text{ m}^3/\text{s}$
*   Energy input rate = Volume rate $\times C.V. = 0.002444 \text{ m}^3/\text{s} \times 16350 \text{ kJ/m}^3 = 39.96 \text{ kW}$

Using the efficiency formula (adapted for volume instead of mass):
$$\eta_{ith} = \frac{i_p}{\text{Energy input rate}}$$
$$\eta_{ith} = \frac{11.026}{39.96}$$
$$\eta_{ith} = 0.2759 \text{ or } 27.59\%$$

### In an Otto cycle, the temperature at the beginning and end of the isentropic compression are 316K and 596K, respectively. Determine the air standard efficiency and compression ratio. Take $\gamma = 1.4$.

**Given Data:**
*   Cycle: Constant volume (Otto cycle)
*   Temperature at beginning of compression ($T_1$) = 316 K
*   Temperature at end of compression ($T_2$) = 596 K
*   Ratio of specific heats ($\gamma$) = 1.4

**Step 1: Determine the Compression Ratio ($r_k$)**
According to the Otto cycle formulas provided in the text, the relationship between temperatures and volumes during isentropic compression is:
$$\frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma-1}$$
Since the compression ratio $r_k = \frac{V_1}{V_2}$, we can substitute:
$$\frac{T_2}{T_1} = (r_k)^{\gamma-1}$$
$$\frac{596}{316} = (r_k)^{1.4-1}$$
$$1.886 = (r_k)^{0.4}$$
To isolate $r_k$, raise both sides to the power of $\frac{1}{0.4}$ (which is 2.5):
$$r_k = (1.886)^{2.5}$$
$$r_k = 4.88$$

**Step 2: Determine the Air Standard Efficiency ($\eta_{th}$)**
The thermal efficiency formula for the Otto cycle is:
$$\eta_{th} = 1 - \frac{1}{(r_k)^{\gamma-1}}$$
Since we already established that $(r_k)^{\gamma-1} = \frac{T_2}{T_1} = 1.886$, we can substitute this value directly:
$$\eta_{th} = 1 - \frac{1}{1.886}$$
$$\eta_{th} = 1 - 0.5302$$
$$\eta_{th} = 0.4698 \text{ or } 46.98\%$$
### Q 1. Draw a schematic diagram of an IC engine and mention its main parts.

*(Note: While actual drawings cannot be generated, the provided text details the schematic layout and lists the main parts of an I.C. engine).*

Based on the provided text, the main parts of an internal combustion engine are:

**Parts common to both petrol and diesel engines:**
*   Cylinder
*   Piston
*   Gudgeon pin
*   Crank
*   Engine bearing
*   Flywheel
*   Valves and valve gears (Inlet and Exhaust valves)
*   Cylinder head
*   Piston rings (Compression ring and Oil rings)
*   Connecting rod
*   Crankshaft
*   Crankcase
*   Governor
*   Cylinder Liner
*   Cams and Camshaft

**Parts for petrol (S.I.) engines only:**
*   Spark plugs
*   Fuel pump
*   Carburettor

**Parts for Diesel (C.I.) engines only:**
*   Fuel pump
*   Injector

### Q 2. Explain the different strokes of a four-stroke diesel engine with an actual indicator diagram.

*(Note: The provided text does not contain an "actual indicator diagram" or a theoretical p-V diagram for a Diesel engine. It only contains a p-V diagram for an Otto cycle. The explanation of the strokes based on the text is provided below).*

According to the text, the four strokes of a Compression Ignition (Diesel) engine operate on the constant pressure cycle as follows:

1.  **Suction Stroke:** During this stroke, the piston moves downward, and only air is sucked alone inside the engine cylinder.
2.  **Compression Stroke:** The air is compressed sufficiently to increase its pressure and temperature by a considerable amount. The temperature is increased to equal the self-ignition temperature of the fuel.
3.  **Power (Expansion) Stroke:** Just before the end of the compression stroke, a metered quantity of fuel is injected under high pressure into the cylinder by a fuel injector. Due to the very high pressure and temperature of the air, the fuel auto-ignites. The hot gases produced force the piston downwards, and mechanical work is obtained.
4.  **Exhaust Stroke:** The piston moves upward, and the exhaust gases are forced out of the cylinder.

### Q 3. Differentiate between petrol engine and diesel engine.

Based on the comparison tables in the provided text, the differences are:

*   **Thermodynamic Cycle:** Petrol engines work on the Otto cycle (constant volume heat addition), while diesel engines work on the Diesel cycle (constant pressure heat addition).
*   **Suction:** In a petrol engine, an air-petrol mixture is sucked into the cylinder during the suction stroke. In a diesel engine, only air is sucked in.
*   **Ignition:** Petrol engines use a spark plug to produce spark ignition. Diesel engines employ an injector and rely on compression ignition (autoignition due to high-temperature compressed air).
*   **Fuel Supply:** Petrol engines use a carburettor for fuel supply (a cheaper method). Diesel engines use an injection pump and injector (an explosive method).
*   **Compression Ratio:** The compression ratio in petrol engines ranges from 6 to 10. In diesel engines, it ranges from 16 to 20.
*   **Thermal Efficiency:** Petrol engines have a lower thermal efficiency (up to 25%). Diesel engines have a higher thermal efficiency (up to 40%) due to the higher compression ratio.
*   **Weight and Space:** Petrol engines are light in weight and occupy less space. Diesel engines are heavy in weight and occupy more space.
*   **Running Cost and Fuel:** Petrol engines have a higher running cost and use costlier, highly volatile fuel. Diesel engines have a lower running cost and use cheaper, non-volatile fuel.
*   **Operating Speed:** Petrol engines operate at high speeds (2000 to 6000 r.p.m.). Diesel engines generally operate at lower to medium speeds (400 to 3500 r.p.m.).
*   **Applications:** Petrol engines are used in cars and motorcycles. Diesel engines are used in heavy-duty vehicles like trucks, buses, and heavy machinery.

### Q 4. Describe the main function of the flywheel, crankshaft, and piston.

Based on the provided text, the main functions are:

*   **Flywheel:** It is a heavy wheel mounted on the crankshaft to minimize cyclic variations in speed. It absorbs energy during the power stroke and releases it during the non-power strokes. By employing a flywheel, the turning moment becomes uniform at the crankshaft.
*   **Crankshaft:** It is the principal rotating part of the engine which controls the sequence of reciprocating motion of the pistons. It receives the rotary motion transferred from the connecting rod.
*   **Piston:** The main function of the piston is to reciprocate inside the cylinder and transfer the power produced by the combustion of the fuel to the crankshaft (via the connecting rod).

### Explain the principle of supercharging and turbocharging in an IC engine.

The provided text does not explain the principles of supercharging or turbocharging. It only briefly mentions "supercharging" in a comparison table, noting that in two-stroke engines it is "Limited by blower power and mechanical and thermal stresses," and in S.I. engines it is "Limited by detonation." Turbocharging is not mentioned in the text.

### Describe the valve timing diagram of a four-stroke SI engine.

*(Note: The provided text does not contain a specific "valve timing diagram" showing crank angles. However, it describes the valve states during the four strokes of an S.I. engine as follows):*

*   **Suction Stroke:** The inlet valve is open, and the exhaust valve is closed as the piston moves downward towards BDC, allowing the air-fuel mixture to enter.
*   **Compression Stroke:** Both the inlet and exhaust valves are closed as the piston moves towards TDC to compress the mixture.
*   **Power Stroke:** Both valves remain closed while the high pressure from combustion forces the piston towards BDC.
*   **Exhaust Stroke:** The exhaust valve opens, and the inlet valve remains closed as the piston moves towards TDC, forcing the exhaust gas to escape.

