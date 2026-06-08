Here are the detailed, textbook-style solutions to the questions presented in the images.

### Q.6 (a) Differentiate between impulse and reaction turbines.

**Answer:**
The primary difference between an impulse turbine and a reaction turbine lies in how the hydraulic energy of the water is converted into mechanical energy to rotate the turbine runner.

| Feature | Impulse Turbine (e.g., Pelton Wheel) | Reaction Turbine (e.g., Francis, Kaplan) |
| :--- | :--- | :--- |
| **Energy Conversion at Inlet** | All available potential energy (head) is converted into kinetic energy by a nozzle *before* the water strikes the runner. | Only a portion of the available energy is converted to kinetic energy before entering the runner; the water enters the runner with both pressure energy and kinetic energy. |
| **Pressure throughout runner**| The pressure of the water remains constant (equal to atmospheric pressure) as it flows over the moving buckets/blades. | The pressure of the water drops continuously as it flows over the blades through the runner. |
| **Flow Medium** | The water flows in the form of a free jet striking individual buckets. The wheel does not run full. | The water completely fills all passages between the runner blades. The wheel runs full. |
| **Casing Function** | The casing is not pressure-tight. It only serves to prevent splashing and guide water to the tailrace. | A pressure-tight casing (volute) is absolutely necessary to contain the water pressure and guide it smoothly to the runner. |
| **Head and Discharge** | Typically suitable for very high heads and relatively low discharge. | Typically suitable for medium to low heads and medium to high discharge. |
| **Draft Tube** | Not required, as the water exits at atmospheric pressure. | Essential. A draft tube connects the runner exit to the tailrace to recover remaining kinetic energy and allow the turbine to be set above tailrace level without losing head. |

***

### (b) Describe the construction and working of a Pelton wheel with the help of neat diagram.

**Answer:**

*(Note: While a physical diagram cannot be drawn here, the description below matches standard textbook diagrams of a Pelton Wheel).*

**1. Construction (Main Components):**
A Pelton wheel is a tangential flow impulse turbine. Its main components are:
*   **Penstock:** A large pipe that carries water under high pressure from the reservoir/dam to the turbine.
*   **Nozzle and Spear Arrangement:** At the end of the penstock, a nozzle is fitted to convert the pressure energy of water entirely into kinetic energy, forming a high-velocity jet. A conical needle (spear) is operated inside the nozzle (manually or by a governing mechanism) to regulate the amount of water striking the runner, thus controlling the speed based on the load.
*   **Runner and Buckets:** The runner is a circular disk mounted on a rotating shaft. Onto its periphery, several evenly spaced buckets (vanes) are securely fixed. Each bucket is shaped like a double-hemispherical cup or bowl with a sharp dividing ridge in the center called a **splitter**.
*   **Casing:** A fabricated metallic cover surrounds the runner. Unlike reaction turbines, it does not hold pressure. Its main functions are to prevent splashing of water, guide the discharged water to the tailrace, and act as a safeguard in case of accidents.
*   **Breaking Jet:** When the turbine needs to be stopped quickly, simply closing the nozzle is not enough due to the high inertia of the heavy runner. A small nozzle directs a jet of water onto the back of the buckets to act as a hydraulic brake.

**2. Working Principle:**
*   Water stored at a high elevation (head) flows down through the penstock.
*   As it exits the nozzle, all its pressure energy is converted into a high-velocity jet of kinetic energy.
*   This jet strikes the buckets of the runner tangentially. The jet hits the splitter ridge of the bucket, which smoothly divides the water jet into two equal parts.
*   The hemispherical shape of the buckets deflects the water through an angle of 160° to 165° (almost turning it back on itself).
*   This massive change in momentum of the water jet exerts a powerful impulsive force on the buckets, causing the runner and its shaft to rotate.
*   The mechanical energy from the rotating shaft is then used to drive a generator to produce electricity. The water, having lost almost all its kinetic energy, falls freely into the tailrace below.

***

### (c) A Pelton wheel is to be designed for the following specifications:
Power (brake or shaft): 9560 kW
Head: 350 meter
Speed: 750 rpm
Overall efficiency: 85%
Jet diameter: not to exceed 1/6 of the wheel diameter
Determine: (i) the wheel diameter, (ii) diameter of the jet, and (iii) the number of jets required. Take, $C_v = 0.985$, speed ratio $= 0.45$.

**Answer:**

**Given Data:**
*   Shaft Power ($P$) = $9560 \text{ kW} = 9560 \times 10^3 \text{ W}$
*   Net Head ($H$) = $350 \text{ m}$
*   Speed ($N$) = $750 \text{ rpm}$
*   Overall Efficiency ($\eta_o$) = $85\% = 0.85$
*   Max Jet Ratio constraint: $d \le D / 6$
*   Coefficient of velocity ($C_v$) = $0.985$
*   Speed ratio ($K_u$) = $0.45$
*   Density of water ($\rho$) = $1000 \text{ kg/m}^3$
*   Acceleration due to gravity ($g$) = $9.81 \text{ m/s}^2$

**Step-by-Step Solution:**

**1. Calculate the Velocity of the Jet ($V_1$):**
$$V_1 = C_v \sqrt{2gH}$$
$$V_1 = 0.985 \times \sqrt{2 \times 9.81 \times 350}$$
$$V_1 = 0.985 \times \sqrt{6867}$$
$$V_1 = 0.985 \times 82.867 = 81.624 \text{ m/s}$$

**2. Calculate the Tangential Velocity of the Wheel ($u$):**
$$u = K_u \sqrt{2gH}$$
$$u = 0.45 \times \sqrt{2 \times 9.81 \times 350}$$
$$u = 0.45 \times 82.867 = 37.290 \text{ m/s}$$

**(i) Determine the Wheel Diameter ($D$):**
We know the relationship between peripheral velocity, diameter, and rotational speed is:
$$u = \frac{\pi \cdot D \cdot N}{60}$$
$$37.290 = \frac{\pi \cdot D \cdot 750}{60}$$
$$D = \frac{37.290 \times 60}{\pi \times 750}$$
$$D = \frac{2237.4}{2356.19}$$
**$D = 0.9496 \text{ m}$  (Let's take it as $0.95 \text{ m}$ for further practical calculations, but keep exact for precision)**

**(ii) & (iii) Determine the Number of Jets ($n$) and actual Jet Diameter ($d$):**

First, find the total discharge ($Q$) required by the turbine using the overall efficiency formula:
$$\eta_o = \frac{\text{Shaft Power (in Watts)}}{\text{Water Power (in Watts)}} = \frac{P}{\rho \cdot g \cdot Q \cdot H}$$
$$0.85 = \frac{9560 \times 10^3}{1000 \times 9.81 \times Q \times 350}$$
$$0.85 = \frac{9560000}{3433500 \times Q}$$
$$Q = \frac{9560000}{0.85 \times 3433500}$$
$$Q = \frac{9560000}{2918475} = 3.2757 \text{ m}^3/\text{s}$$

Now, let's find the maximum allowable discharge for a single jet based on the constraint ($d \le D/6$):
Maximum allowable jet diameter ($d_{\max}$) = $\frac{D}{6} = \frac{0.9496}{6} = 0.1582 \text{ m}$
Area of maximum single jet ($a_{\max}$) = $\frac{\pi}{4} (d_{\max})^2 = \frac{\pi}{4} (0.1582)^2 = 0.01965 \text{ m}^2$
Discharge of one maximum jet ($q_{\max}$) = $a_{\max} \times V_1 = 0.01965 \times 81.624 = 1.604 \text{ m}^3/\text{s}$

Number of jets required ($n$):
$$n = \frac{\text{Total Discharge } (Q)}{\text{Discharge per maximum jet } (q_{\max})}$$
$$n = \frac{3.2757}{1.604} = 2.042$$

Since the number of jets must be a whole number, and 2 jets would require a diameter *larger* than the allowable $1/6$ of the wheel diameter, we must round up to the next whole number.
**Number of jets ($n$) = $3$**

Now, recalculate the *actual* required jet diameter ($d$) using $3$ jets:
Actual discharge per jet ($q$) = $\frac{Q}{n} = \frac{3.2757}{3} = 1.0919 \text{ m}^3/\text{s}$
Actual area per jet ($a$) = $\frac{q}{V_1} = \frac{1.0919}{81.624} = 0.01337 \text{ m}^2$
Since $a = \frac{\pi}{4} d^2$:
$$0.01337 = \frac{\pi}{4} d^2$$
$$d^2 = \frac{0.01337 \times 4}{\pi} = 0.01702$$
$$d = \sqrt{0.01702} = 0.1304 \text{ m}$$
*(Note: $0.1304 \text{ m}$ is less than the max limit of $0.1582 \text{ m}$, so this design is safe and meets all specifications).*

**Final Results Summary:**
*   **(i) Wheel diameter ($D$):** $0.9496 \text{ m}$ (or approx $950 \text{ mm}$)
*   **(ii) Diameter of the jet ($d$):** $0.1304 \text{ m}$ (or $130.4 \text{ mm}$)
*   **(iii) Number of jets required:** $3$
Based on the textbook reference provided, here are the detailed solutions to the questions in the image.

### Q.5 (a) Draw a general layout of a hydroelectric power plant using an impulse turbine and define the followings: (i) Gross head, (ii) Net head, and (iii) Hydraulic efficiency.

**Answer:**

**General Layout:**
*(Note: As I am a text-based AI, I cannot draw the physical diagram, but I will describe the standard layout of a hydroelectric power plant using a Pelton wheel (impulse turbine) as found in the text).*

A typical layout consists of the following main components from top to bottom:
1.  **Head Race / Reservoir:** The water storage area behind a dam at a high elevation.
2.  **Dam:** The structure built to store water and create the head.
3.  **Penstock:** A large pipe that carries water under pressure from the reservoir down to the turbine.
4.  **Nozzle & Spear:** Fitted at the end of the penstock to convert pressure head into a high-velocity kinetic jet.
5.  **Turbine (Pelton Wheel):** The runner with buckets that the water jet strikes.
6.  **Tail Race:** The channel that carries the water away from the turbine after it has done its work.

**Definitions:**

**(i) Gross head ($H_g$):**
The gross (total) head is the vertical difference between the water level at the reservoir (also known as the head race) and the water level at the tail race. It is denoted by $H_g$.

**(ii) Net or effective head ($H$):**
The head available at the inlet of the turbine is known as net or effective head. It is denoted by $H$ and is given by:
$$H = H_g - h_f - h$$
where,
$h_f =$ Total loss of head between the head race and entrance of the turbine (primarily friction in the penstock, $h_f = \frac{4fLV^2}{D \times 2g}$).
$h =$ Height of the nozzle above the tail race.

**(iii) Hydraulic efficiency ($\eta_h$):**
It is defined as the ratio of power developed by the runner to the power supplied by the jet at the entrance to the turbine.
Mathematically,
$$\eta_h = \frac{\text{Power developed by the runner}}{\text{Power supplied at the inlet of turbine}}$$
$$\eta_h = \frac{\rho Q (V_{w1} \pm V_{w2})u}{\rho g Q H} = \frac{(V_{w1} \pm V_{w2})u}{gH}$$

***

### (b) Which points should be considered while selecting right type of hydro turbines for hydroelectric power plant.

**Answer:**

According to the text, the following points should be considered while selecting the right type of hydraulic turbine for a hydroelectric power plant:

1.  **Specific speed:** High specific speed is essential where head is low and output is large, because otherwise the rotational speed will be low which means cost of turbo-generator and power-house will be high. On the other hand, there is practically no need of chosing a high value of specific speed for high installations.
2.  **Rotational speed:** Rotational speed depends on specific speed. Also the rotational speed of an electrical generator with which the turbine is to be directly coupled, depends on the frequency and number of pair of poles. The value of specific speed adopted should be such that it will give the synchronous speed of the generator.
3.  **Efficiency:** The turbine selected should be such that it gives the highest overall efficiency for various operating conditions.
4.  **Partload operation:** In general the efficiency at partloads and overloads is less than normal. For the sake of economy the turbine should always run with maximum possible efficiency. When the turbine has to run at part or overload conditions Deriaz turbine is employed. Similarly, for low heads, Kaplan turbine will be useful.
5.  **Cavitation:** The installation of water turbines of reaction type over the tail race is affected by cavitation. The critical value of cavitation factor must be obtained to see that the turbine works in a safe zone.
6.  **Disposition of turbine shaft:** The vertical shaft arrangement is better for large-sized reaction turbines. In case of large size impulse turbines, horizontal shaft arrangement is mostly employed.
7.  **Head Availability:**
    *   *Very high heads (350 m and above):* Pelton turbine is generally employed.
    *   *High heads (150 m to 350 m):* Either Pelton or Francis turbine.
    *   *Medium heads (60 m to 150 m):* Francis turbine is usually employed.
    *   *Low heads (below 60 m):* Both Francis and Kaplan turbines may be used (Kaplan preferred for variable loads).
    *   *Very low heads (under 15 m):* Propeller, tubular, or bulb turbines are employed.

***

### (c) A hydro-turbine is required to give 25 MW at 50 m head and 90 rpm runner speed. The laboratory facilities available permit testing of 20 kW model at 5 m head. What should be the model runner speed and model to prototype scale ratio?

**Answer:**

**Given Data:**
*   **Prototype:**
    *   Power ($P_p$) = $25\text{ MW} = 25 \times 10^3\text{ kW}$
    *   Head ($H_p$) = $50\text{ m}$
    *   Speed ($N_p$) = $90\text{ rpm}$
*   **Model:**
    *   Power ($P_m$) = $20\text{ kW}$
    *   Head ($H_m$) = $5\text{ m}$

**1. Determine Model Runner Speed ($N_m$):**

For homologous (geometrically similar) turbines, the specific speed ($N_s$) must be the same for both the prototype and the model.

Prototype specific speed, $(N_s)_p = \frac{N_p \sqrt{P_p}}{(H_p)^{5/4}}$
$$(N_s)_p = \frac{90 \times \sqrt{25 \times 10^3}}{(50)^{5/4}}$$
$$(N_s)_p = \frac{90 \times 158.11}{132.96} = 107$$

Since $(N_s)_p = (N_s)_m$, for the model we have:
$$107 = \frac{N_m \sqrt{P_m}}{(H_m)^{5/4}}$$
$$107 = \frac{N_m \sqrt{20}}{(5)^{5/4}}$$
$$N_m = \frac{107 \times (5)^{5/4}}{\sqrt{20}} = \frac{107 \times 7.476}{4.472}$$
**$N_m = 178.89\text{ r.p.m.}$ (Ans.)**

**2. Determine Model to Prototype Scale Ratio ($D_p / D_m$ or $L_r$):**

For similar turbines, the power coefficient $\frac{P}{H^{3/2}D^2}$ should be equal.
$$\frac{P_p}{H_p^{3/2} D_p^2} = \frac{P_m}{H_m^{3/2} D_m^2}$$
Rearranging to find the scale ratio ($L_r = \frac{D_p}{D_m}$):
$$\frac{D_p^2}{D_m^2} = \frac{P_p}{P_m} \times \frac{H_m^{3/2}}{H_p^{3/2}}$$
$$\frac{D_p}{D_m} = \sqrt{\frac{P_p}{P_m} \times \left(\frac{H_m}{H_p}\right)^{3/2}}$$
$$\frac{D_p}{D_m} = \sqrt{\frac{25 \times 10^3}{20} \times \left(\frac{5}{50}\right)^{3/2}}$$
$$\frac{D_p}{D_m} = \sqrt{1250 \times \left(\frac{1}{10}\right)^{1.5}}$$
$$\frac{D_p}{D_m} = \sqrt{1250 \times 0.03162}$$
$$\frac{D_p}{D_m} = \sqrt{39.52}$$
**$\frac{D_p}{D_m} = 6.287$ (Ans.)**

*(Therefore, the prototype to model scale ratio is 6.287 : 1)*
Based on the provided textbook reference, here are the detailed solutions to the questions presented in the images.

### Define cavitation. List the factors which facilitate onset of cavitation.

**Answer:**

**Definition of Cavitation:**
According to the textbook (Section 2.15), cavitation is defined as:
"The formation, growth, and collapse of vapour filled cavities or bubbles in a flowing liquid due to local fall in fluid pressure is called cavitation. When the pressure at any point in a flow field equals the vapour pressure of the liquid at that temperature vapour cavities (bubbles of vapour) begin to appear."

**Factors which facilitate onset of cavitation:**
According to the textbook (Section 3.18), the factors which facilitate the onset of cavitation are as follows:
(i) Restricted suction.
(ii) High runner speed.
(iii) Too high specific speed for optimum design parameters.
(iv) Too high temperature of the flowing liquid.

***

### Q.5 (a) What do you mean by turbo machine? Describe the characteristics of the impulse and reaction turbine.

**Answer:**

**Meaning of Turbo Machine:**
*(Note: While the provided text does not explicitly define the broad general term "turbo machine" in a standalone paragraph, it focuses specifically on "hydraulic machines", which are a sub-category. The text defines hydraulic turbines as follows, which serves as the definition in this context):*
A hydraulic turbine is a prime mover (a machine which uses the raw energy of a substance and converts it into mechanical energy) that uses the energy of flowing water and converts it into mechanical energy (in the form of rotation of the runner).

**Characteristics of Impulse and Reaction Turbines:**
Based on the text (Section 2.2 and Table 2.1), the characteristics and differences are described below:

**Characteristics of Impulse Turbines (e.g., Pelton Wheel):**
*   **Energy Conversion:** The available fluid energy (pressure head) is completely converted into kinetic energy by a nozzle *before* the fluid enters the runner.
*   **Pressure:** The pressure remains the same (atmospheric) throughout the action of water on the runner.
*   **Flow:** The water does not completely fill the wheel/turbine. It runs as a free jet, and air has free access to the buckets. Water may be allowed to enter only a part of the wheel circumference.
*   **Suitability:** Requires high head and small quantity of flow.
*   **Installation:** Always installed above the tail race. No draft tube is used.

**Characteristics of Reaction Turbines (e.g., Francis, Kaplan):**
*   **Energy Conversion:** The energy of the fluid is only partly transformed into kinetic energy before it enters the runner of the turbine.
*   **Pressure:** After entering the runner with an excess pressure, the water undergoes continuous changes both in velocity and pressure while passing through the runner.
*   **Flow:** Water completely fills all the passages between the blades and does work on the blades while flowing between inlet and outlet sections. Water is admitted over the entire circumference of the wheel.
*   **Suitability:** Requires low to medium heads and medium to high rates of flow.
*   **Installation:** The unit may be installed above or below the tail race, and the use of a draft tube is essential.

***

### (b) Derive the expression, $H = \frac{V_{w_2}U_2 - V_{w_1}U_1}{g}$ for power output of an impulse turbine.

**Answer:**

*(Important Note based on the textbook text: The question asks to derive this expression for an **impulse turbine**. However, according to the provided text, the specific formula $H = \frac{V_{w2}u_2 - V_{w1}u_1}{g}$ is the Euler momentum equation derived for a **centrifugal pump** (Eqn. 3.2). For an impulse turbine (Pelton wheel), where the tangential velocity of the wheel is the same at inlet and outlet ($u_1 = u_2 = u$), the text derives the expression for work done per unit weight as $\frac{(V_{w1} \pm V_{w2})u}{g}$. The derivation below follows the text's procedure for an **impulse turbine** as requested by the question wording.)*

**Derivation for an Impulse Turbine (Pelton Wheel) based on Section 2.3.2:**

1.  Consider a jet of water striking the buckets of a Pelton wheel. Let the velocity triangles be drawn for the inlet and outlet.
    *   $V_1$ = Absolute velocity of water at inlet.
    *   $u$ = Peripheral (or circumferential) velocity of the runner. For an impulse turbine, it is the same at the inlet and outlet mean pitch, so $u = u_1 = u_2$.
    *   $V_{w1}$ = Velocity of whirl at inlet (component of $V_1$ in the direction of motion).
    *   $V_{w2}$ = Velocity of whirl at outlet.
    *   $a$ = Area of the jet.

2.  For a Pelton wheel, the inlet velocity triangle is a straight line, where $V_{w1} = V_1$.

3.  According to momentum principles, the force exerted by the jet of water in the direction of motion is given by the mass flow rate multiplied by the change in velocity in that direction.
    $$F = (\text{mass/sec}) \times (\text{initial velocity of whirl} - \text{final velocity of whirl})$$
    As shown in the text (Eqn. 2.1), considering vector directions where the outlet whirl is in the opposite direction to the vane motion (for $\beta < 90^\circ$):
    $$F = \rho a V_1 (V_{w1} + V_{w2})$$

4.  The **power output** (Work done per second) by the jet on the runner is the force multiplied by the velocity of the wheel:
    $$\text{Work done per second} = F \times u$$
    $$\text{Power Output} = \rho a V_1 (V_{w1} + V_{w2}) \times u \quad \text{...[Eqn (2.2)]}$$

5.  The expression $H$ typically denotes "Head" representing energy or work per unit weight. The work done per second per unit weight of water striking is:
    $$H = \frac{\text{Work done per second}}{\text{Weight of water striking per second}}$$
    $$H = \frac{\rho a V_1 (V_{w1} + V_{w2}) \times u}{\rho a V_1 \times g}$$
    $$H = \frac{1}{g} (V_{w1} + V_{w2}) u \quad \text{...[Eqn 2.2(a)]}$$
    *(This is the standard expression derived in the text for an impulse turbine. If the general notation with different inlet and outlet tangential speeds were used for a general turbine, it would be formulated as $H = \frac{V_{w1}u_1 \pm V_{w2}u_2}{g}$, as seen later in the text for reaction turbines).*
Based on the textbook reference you provided, here are the detailed solutions to the questions from the images.

### Define cavitation. What are the effects of cavitation and how is it avoided? List the factors which facilitate onset of cavitation.

*(This answers the questions from both the first and third image crops)*

**Answer:**

**Definition of Cavitation:**
According to Section 2.15 and 3.18 of the text, cavitation is defined as:
"The formation, growth, and collapse of vapour filled cavities or bubbles in a flowing liquid due to local fall in fluid pressure is called cavitation. When the pressure at any point in a flow field equals the vapour pressure of the liquid at that temperature vapour cavities (bubbles of vapour) begin to appear."

**Effects of Cavitation:**
As listed in Section 3.18, the harmful effects of cavitation are:
1.  **Pitting and erosion of surface:** This occurs due to the continuous 'hammering' action of collapsing bubbles on the metal surface.
2.  **Sudden drop in performance:** There is a sudden drop in head, efficiency, and the power delivered to the fluid because the actual volume of liquid flowing through the machine is reduced by the vapour cavities.
3.  **Noise and vibration:** Produced by the violent, irregular collapse of the bubbles.

**Methods to Avoid Cavitation:**
According to Section 3.18, cavitation can be avoided or its effects reduced by:
1.  **Setting the runner properly:** The turbine/pump can be kept under water (submerged), though this makes maintenance difficult. Ensuring the suction lift is within safe limits (based on Thoma's cavitation factor) is crucial.
2.  **Selecting proper specific speed:** Avoid using a runner of too high specific speed for a given head.
3.  **Material selection:** Selecting materials that resist cavitation pitting better. Cast steel is better than cast iron, and stainless steel or alloy steel is even better.
4.  **Surface finish:** The cavitation effect can be reduced by polishing the surface (e.g., coating cast steel runners with stainless steel).
5.  **Designing cavitation-free runners:** Through extensive research and testing.

**Factors which facilitate the onset of cavitation:**
As listed in Section 3.18, these factors are:
(i) Restricted suction.
(ii) High runner speed.
(iii) Too high specific speed for optimum design parameters.
(iv) Too high temperature of the flowing liquid.

***

### (a) What is the more common term for an energy producing turbomachine? How about an energy absorbing turbomachine? Explain this terminology.

**Answer:**

Based on the introductions to the respective chapters in the textbook (Sections 2.1 and 3.1):

*   **Energy Producing Turbomachine:** The common term is a **Turbine** (specifically, a hydraulic turbine in this context).
*   **Energy Absorbing Turbomachine:** The common term is a **Pump**.

**Explanation of Terminology:**
*   **Turbine (Energy Producing):** As defined in Section 2.1, a hydraulic turbine is a prime mover "that uses the energy of flowing water and converts it into mechanical energy (in the form of rotation of the runner)." The flow takes place from a high-pressure side to a low-pressure side, meaning the machine extracts or "produces" mechanical work from the fluid's energy.
*   **Pump (Energy Absorbing):** As defined in Section 3.1, a pump is a contrivance "which provides energy to a fluid... it assists to increase the pressure energy or kinetic energy... by converting mechanical energy." In a pump, flow takes place from a low-pressure side towards a higher pressure. It must "absorb" mechanical energy from an external source (like a motor) to do work on the fluid.

***

### (b) Name and briefly discuss the differences between the two basic types of dynamic turbines.

**Answer:**

According to Section 2.2 ("Classification of Hydraulic Turbines") and Table 2.1, the two basic types of dynamic turbines based on the action of water are **Impulse Turbines** and **Reaction Turbines**.

**Differences:**

| Feature | Impulse Turbine (e.g., Pelton Wheel) | Reaction Turbine (e.g., Francis, Kaplan) |
| :--- | :--- | :--- |
| **Energy Conversion** | The available fluid energy (head) is completely converted into kinetic energy by a nozzle *before* entering the runner. | The energy of the fluid is only partly transformed into kinetic energy before it enters the runner. |
| **Pressure Changes** | The pressure remains the same (atmospheric) throughout the action of water on the runner. | The water undergoes continuous changes both in velocity and pressure while passing through the runner. |
| **Flow Characteristics** | The wheel does not run full; air has free access to the buckets. Water may hit only a part of the circumference. | Water completely fills all the passages between the blades. Water is admitted over the entire circumference. |
| **Casing Function** | Water-tight casing is required mainly to prevent splashing, but it does not hold pressure. | A pressure-tight casing is absolutely necessary to contain the water pressure. |
| **Draft Tube** | Not used. Always installed above the tail race. | Essential. Unit may be installed above or below the tail race. |

***

### (c) A pelton wheel is running under a head of 150m at the speed of 300 rpm. The overall efficiency of the turbine is 85% and the ratio of Jet to the wheel diameter is 1/10. Find the following: (i) Diameter of the wheel, (ii) Diameter of the Jet, (iii) Width of buckets, (iv) Depth of buckets, (v) Number of buckets.

**Answer:**

*Note: The problem does not provide power or discharge to calculate absolute dimensions directly. However, standard design practice for Pelton wheels allows us to find the diameter by assuming a typical "Speed Ratio" ($K_u$). Based on Section 2.3.4 of the textbook, $K_u$ varies from 0.43 to 0.48. We will assume a standard average value of $K_u = 0.45$ to solve this problem.*

**Given Data:**
*   Net Head ($H$) = $150 \text{ m}$
*   Speed ($N$) = $300 \text{ rpm}$
*   Overall efficiency ($\eta_o$) = $85\%$ *(Note: This data point is not needed for geometric calculations if power/discharge is not asked)*
*   Jet ratio ($m$) = $D/d = 10 \Rightarrow d/D = 1/10$
*   Acceleration due to gravity ($g$) = $9.81 \text{ m/s}^2$

**Assumptions based on text (Section 2.3.4):**
*   Assume Speed ratio ($K_u$) = $0.45$

**Step-by-Step Solution:**

**1. Calculate the Tangential Velocity of the Wheel ($u$):**
Using the formula from the text (Eqn 2.12):
$$u = K_u \sqrt{2gH}$$
$$u = 0.45 \times \sqrt{2 \times 9.81 \times 150}$$
$$u = 0.45 \times \sqrt{2943} = 0.45 \times 54.25$$
$$u = 24.41 \text{ m/s}$$

**(i) Diameter of the wheel ($D$):**
Using the relation between peripheral speed, diameter, and RPM (Eqn 2.13):
$$u = \frac{\pi \cdot D \cdot N}{60}$$
$$24.41 = \frac{\pi \times D \times 300}{60}$$
$$24.41 = 5 \pi D$$
$$D = \frac{24.41}{5 \pi} = 1.554 \text{ m}$$
**Answer (i): Diameter of the wheel is $1.554 \text{ m}$ (or $1554 \text{ mm}$).**

**(ii) Diameter of the Jet ($d$):**
Given the ratio $d/D = 1/10$:
$$d = \frac{D}{10} = \frac{1.554}{10} = 0.1554 \text{ m}$$
**Answer (ii): Diameter of the jet is $0.1554 \text{ m}$ (or $155.4 \text{ mm}$).**

**(iii) & (iv) Width and Depth of buckets:**
Referencing Section 2.3.4 (point 6) and Fig 2.3 for standard bucket dimensions:
*   **Width of bucket ($B$):** The text specifies $B = 3 \text{ to } 4d$. Let's assume an average value of $3.5d$.
    $$B = 3.5 \times 155.4 \text{ mm} = 543.9 \text{ mm}$$
*   **Depth of bucket ($T$):** The text specifies $T = 0.8 \text{ to } 1.2d$. Let's assume an average value of $1.0d$.
    $$T = 1.0 \times 155.4 \text{ mm} = 155.4 \text{ mm}$$
**Answer (iii): Width of buckets is approximately $543.9 \text{ mm}$ (acceptable range: 466 to 621 mm).**
**Answer (iv): Depth of buckets is approximately $155.4 \text{ mm}$ (acceptable range: 124 to 186 mm).**

**(v) Number of buckets ($Z$):**
Using the formula from the text (Eqn 2.15):
$$Z = 15 + \frac{D}{2d}$$
Since $D/d = 10$:
$$Z = 15 + \frac{10}{2} = 15 + 5 = 20$$
**Answer (v): Number of buckets is 20.**
Based on the provided textbook reference, here are the detailed solutions to the questions.

### Q.4 (a) Draw the schematic diagram of Francis turbine and explain briefly its construction and working.

**Answer:**

*(Note: As an AI, I cannot physically draw the diagram. I will describe the schematic diagram as presented in Figure 2.11 of the text, followed by the construction and working details).*

**Schematic Diagram Description:**
A typical schematic (like Fig 2.11) shows a vertical shaft connecting to a runner. Water enters through a penstock into a spiral casing that surrounds the turbine. The water then passes through stationary guide vanes (or blades) arranged in a ring, which direct the flow inward toward the runner blades. After passing through the runner, the water discharges downwards (axially) into an expanding draft tube, which leads to the tail race.

**Construction (Main Parts):**
According to Section 2.4.1, the main parts of a Francis turbine are:
1.  **Penstock:** A large size conduit which conveys water from the upstream of the dam/reservoir to the turbine runner.
2.  **Spiral/scroll casing:** It constitutes a closed passage whose cross-sectional area gradually decreases along the flow direction; area is maximum at inlet and nearly zero at exit.
3.  **Guide vanes/wicket gates:** These vanes direct the water onto the runner at an angle appropriate to the design.
4.  **Governing mechanism:** It changes the position of the guide blades/vanes to affect a variation in water flow rate, when load conditions change.
5.  **Runner and runner blades:** The driving force on the runner is both due to impulse and reaction effects. The number of runner blades usually varies between 16 to 24.
6.  **Draft tube:** It is a gradually expanding tube which discharges water, passing through the runner, to the tail race.

**Working:**
The modern Francis turbine is an inward mixed flow reaction turbine. Water under pressure enters the runner from the guide vanes towards the centre in a radial direction and discharges out of the runner axially.
The head acting on the turbine is partly transformed into kinetic energy and the rest remains as pressure head. There is a difference of pressure between the guide vanes and the runner which is called the reaction pressure and is responsible for the motion of the runner. Because the pressure at inlet is more than at outlet, the water in the turbine must flow in a closed conduit, meaning the runner is always full of water. After doing work, the water is discharged to the tail race through the draft tube, making the entire water passage completely enclosed.

***

### (b) What are the functions of a draft tube?

**Answer:**

According to Section 2.8.1 of the text, the draft tube serves the following two purposes:
1.  It allows the turbine to be set above tail-water level, without loss of head, to facilitate inspection and maintenance.
2.  It regains, by diffuse action, the major portion of the kinetic energy delivered to it from the runner (converting velocity head into pressure or potential head).

***

### (c) A reaction turbine works at 450 rpm under a head of 120 m. Its diameter at inlet is 1.2 m and the flow area is $0.4 \text{ m}^2$. The angle made by the absolute and relative velocities at inlet are $20^\circ$ and $60^\circ$ respectively with tangential velocity. Determine: (i) the volume flow rate, (ii) the power developed, (iii) the hydraulic efficiency.

**Answer:**

*(This matches Example 2.17 in the textbook text).*

**Given Data:**
*   Speed of turbine ($N$) = $450 \text{ r.p.m.}$
*   Head ($H$) = $120 \text{ m}$
*   Diameter at inlet ($D_1$) = $1.2 \text{ m}$
*   Flow area ($\pi D_1 B_1$) = $0.4 \text{ m}^2$
*   Angle made by absolute velocity ($\alpha$) = $20^\circ$
*   Angle made by relative velocity at inlet ($\theta$) = $60^\circ$
*   Assume radial discharge at outlet for typical problems of this type ($V_{w2} = 0$).

**Step-by-Step Solution:**

First, calculate the tangential velocity of the turbine at inlet ($u_1$):
$$u_1 = \frac{\pi D_1 N}{60}$$
$$u_1 = \frac{\pi \times 1.2 \times 450}{60} = 28.27 \text{ m/s}$$

From the inlet velocity triangle (as per standard text derivation):
$$\tan \alpha = \frac{V_{f1}}{V_{w1}}$$
$$\tan 20^\circ = \frac{V_{f1}}{V_{w1}}$$
$$V_{f1} = V_{w1} \tan 20^\circ = 0.364 V_{w1} \quad \text{--- (i)}$$

Also, from the inlet triangle:
$$\tan \theta = \frac{V_{f1}}{V_{w1} - u_1}$$
Substituting $\theta = 60^\circ$, $u_1 = 28.27$, and $V_{f1}$ from eqn (i):
$$\tan 60^\circ = \frac{0.364 V_{w1}}{V_{w1} - 28.27}$$
$$1.732 = \frac{0.364 V_{w1}}{V_{w1} - 28.27}$$
$$1.732 (V_{w1} - 28.27) = 0.364 V_{w1}$$
$$1.732 V_{w1} - 48.96 = 0.364 V_{w1}$$
$$1.732 V_{w1} - 0.364 V_{w1} = 48.96$$
$$1.368 V_{w1} = 48.96$$
$$V_{w1} = \frac{48.96}{1.368} = 35.79 \text{ m/s}$$

Now, substituting $V_{w1}$ back into eqn (i) to find $V_{f1}$:
$$V_{f1} = 0.364 \times 35.79 = 13.027 \text{ m/s}$$

**(i) The volume flow rate, $Q$:**
$$Q = \text{Flow area} \times V_{f1}$$
$$Q = 0.4 \times 13.027$$
**$Q = 5.211 \text{ m}^3\text{/s}$ (Ans.)**

**(ii) The power developed:**
Work done per second = $\rho Q (V_{w1}u_1)$  [Assuming $V_{w2} = 0$ for radial discharge]
$$\text{Work done} = 1000 \times 5.211 \times 35.79 \times 28.27$$
$$\text{Work done} = 5272402 \text{ J/s or W}$$
**Power developed = $5272.4 \text{ kW}$ (Ans.)**

**(iii) The hydraulic efficiency, $\eta_h$:**
$$\eta_h = \frac{V_{w1}u_1}{gH}$$
$$\eta_h = \frac{35.79 \times 28.27}{9.81 \times 120}$$
$$\eta_h = 0.8595$$
**Hydraulic efficiency = $85.95\%$ (Ans.)**

### What is the condition for hydraulic efficiency of a Pelton wheel to be maximum? Derive an expression for maximum hydraulic efficiency of a Pelton wheel.

**Answer:**

**Condition for Maximum Hydraulic Efficiency:**
The hydraulic efficiency of a Pelton wheel will be maximum when the velocity of the wheel ($u$) is half the velocity of the jet of water at inlet ($V_1$).
Mathematically, the condition is:
$$u = \frac{V_1}{2}$$

**Derivation of Expression for Maximum Hydraulic Efficiency:**
From the velocity triangles of a Pelton wheel, the work done per second per unit weight of water striking is derived as:
$$\text{Work done} = \frac{1}{g} (V_{w1} + V_{w2})u$$
The energy supplied to the jet at inlet is $\frac{V_1^2}{2g}$.
The hydraulic efficiency ($\eta_h$) is the ratio of work done to energy supplied, which after substituting the values of whirl velocities ($V_{w1} = V_1$ and $V_{w2} = K(V_1 - u)\cos\phi - u$) is given by the expression:
$$\eta_h = \frac{2[V_1 + K(V_1 - u)\cos\phi - u]u}{V_1^2}$$
$$\eta_h = \frac{2[(V_1 - u)(1 + K\cos\phi)u]}{V_1^2}$$
*(Where $K$ is the blade friction co-efficient, and $\phi$ is the blade angle at exit).*

The hydraulic efficiency will be maximum for a given value of $V_1$ when the derivative of $\eta_h$ with respect to $u$ is zero:
$$\frac{d}{du}(\eta_h) = 0$$
$$\frac{d}{du} \left[ \frac{2(V_1 - u)(1 + K\cos\phi)u}{V_1^2} \right] = 0$$
$$\frac{2(1 + K\cos\phi)}{V_1^2} \times \frac{d}{du}(V_1u - u^2) = 0$$
Since the term $\frac{2(1 + K\cos\phi)}{V_1^2}$ cannot be zero, we must have:
$$\frac{d}{du}(V_1u - u^2) = 0$$
$$V_1 - 2u = 0$$
$$u = \frac{V_1}{2}$$

To find the maximum efficiency, substitute this value of $u = \frac{V_1}{2}$ back into the main equation for $\eta_h$:
$$(\eta_h)_{\text{max}} = \frac{2 \left(V_1 - \frac{V_1}{2}\right) (1 + K\cos\phi) \left(\frac{V_1}{2}\right)}{V_1^2}$$
$$(\eta_h)_{\text{max}} = \frac{2 \left(\frac{V_1}{2}\right) (1 + K\cos\phi) \left(\frac{V_1}{2}\right)}{V_1^2}$$
$$(\eta_h)_{\text{max}} = \frac{1 + K\cos\phi}{2}$$

If the friction factor $K = 1$ (assuming no friction), the expression simplifies to:
$$(\eta_h)_{\text{max}} = \frac{1 + \cos\phi}{2}$$

***

### (ii) radial and axial flow turbines.

**Answer:**

These terms classify hydraulic turbines based on the direction of water flow through the runner.

**Radial Flow Turbines:**
In these turbines, the water flows in a radial direction relative to the turbine shaft. They can be further subdivided:
*   **Inward flow reaction turbine:** Water enters at the outer periphery, flows inward towards the centre of the turbine, and discharges at the inner periphery (or axially).
*   **Outward flow reaction turbine:** Water enters at the inner periphery, flows outward, and discharges at the outer periphery. (These are practically obsolete).
*   *Note:* While early Francis turbines were purely radial, modern Francis turbines are technically "mixed flow" turbines where water enters radially but exits axially.

**Axial Flow Turbines:**
In an axial flow turbine, the water flows parallel to the axis of the turbine shaft. The energy transfer occurs when the flow is in its axial direction.
*   These are typically reaction turbines designed for low heads and large quantities of water.
*   **Examples:** Kaplan turbine (where runner blades are adjustable) and Propeller turbine (where runner blades are fixed).

***

### An inward flow reaction turbine has external and internal diameters as 1.2 m and 0.6 m respectively. The velocity of flow through the runner is constant and is equal to 1.8 m/s. Determine (i) discharge through the runner and (ii) width at outlet if the width at inlet = 200 mm.

**Answer:**

**Given Data:**
*   External diameter (inlet for inward flow), $D_1 = 1.2 \text{ m}$
*   Internal diameter (outlet for inward flow), $D_2 = 0.6 \text{ m}$
*   Velocity of flow (constant), $V_{f1} = V_{f2} = 1.8 \text{ m/s}$
*   Width at inlet, $B_1 = 200 \text{ mm} = 0.2 \text{ m}$

*(Assuming no blade thickness blockage since no coefficient is given, i.e., $K_t = 1$)*

**(i) Discharge through the runner ($Q$):**
The discharge is given by the product of the flow area at inlet and the velocity of flow at inlet.
$$Q = \pi \times D_1 \times B_1 \times V_{f1}$$
$$Q = \pi \times 1.2 \times 0.2 \times 1.8$$
$$Q = 1.357 \text{ m}^3\text{/s}$$
**Answer (i): The discharge through the runner is $1.357 \text{ m}^3\text{/s}$.**

**(ii) Width at outlet ($B_2$):**
Using the continuity equation, the discharge at the inlet equals the discharge at the outlet.
$$Q = \pi \times D_1 \times B_1 \times V_{f1} = \pi \times D_2 \times B_2 \times V_{f2}$$
Since the velocity of flow is constant ($V_{f1} = V_{f2}$), the equation simplifies to:
$$D_1 \times B_1 = D_2 \times B_2$$
Substituting the known values:
$$1.2 \times 0.2 = 0.6 \times B_2$$
$$0.24 = 0.6 \times B_2$$
$$B_2 = \frac{0.24}{0.6}$$
$$B_2 = 0.4 \text{ m} = 400 \text{ mm}$$
**Answer (ii): The width at the outlet is $400 \text{ mm}$ (or $0.4 \text{ m}$).**
### (a) Prove that head available of water in a reaction turbine is given as $H = \frac{u_1v_{w1} - u_2v_{w2}}{g}$, where $v_{w1}$ and $v_{w2}$ = velocities of whirl at inlet and outlet, $u_1$ and $u_2$ = peripheral velocities at inlet and outlet.

**Answer:**

**Proof:**
The expression for the work done by the runner of a reaction turbine can be derived using the Euler momentum equation, which is based on Newton's Second Law of Motion applied to a rotating fluid.

1.  **Rate of change of momentum:**
    Let the mass of water flowing through the runner per second be $\dot{m} = \rho Q$.
    The momentum of water entering the runner per second in the tangential direction is $\dot{m} v_{w1} = \rho Q v_{w1}$.
    The momentum of water leaving the runner per second in the tangential direction is $\dot{m} v_{w2} = \rho Q v_{w2}$.
    *(Note: We assume $v_{w1}$ and $v_{w2}$ are both in the direction of the runner's rotation for this specific formulation. If $v_{w2}$ is in the opposite direction, it would take a negative sign in a vector sense).*

2.  **Angular Momentum and Torque:**
    Angular momentum of water entering per second $= \rho Q v_{w1} R_1$
    Angular momentum of water leaving per second $= \rho Q v_{w2} R_2$
    where $R_1$ and $R_2$ are the outer and inner radii of the runner respectively.
    
    According to Euler's momentum principle, the torque $T$ exerted by the water on the runner is equal to the rate of change of angular momentum of the water.
    $$T = \text{Initial angular momentum/sec} - \text{Final angular momentum/sec}$$
    $$T = \rho Q v_{w1} R_1 - \rho Q v_{w2} R_2$$

3.  **Work Done (Power):**
    The work done per second by the runner (Power, $P$) is the product of Torque and angular velocity ($\omega$).
    $$P = T \times \omega = (\rho Q v_{w1} R_1 - \rho Q v_{w2} R_2) \omega$$
    $$P = \rho Q (v_{w1} R_1 \omega - v_{w2} R_2 \omega)$$
    
    Since the peripheral velocities at the inlet and outlet are $u_1 = \omega R_1$ and $u_2 = \omega R_2$, we substitute these into the equation:
    $$P = \rho Q (u_1 v_{w1} - u_2 v_{w2})$$

4.  **Head Available (Euler Head):**
    The "head" $H$ (specifically, the theoretical or Euler head $H_e$) is defined as the work done per unit weight of the water.
    $$\text{Weight of water flowing per second} = \dot{m}g = \rho Q g$$
    $$H = \frac{\text{Work done per second}}{\text{Weight of water per second}} = \frac{P}{\rho Q g}$$
    $$H = \frac{\rho Q (u_1 v_{w1} - u_2 v_{w2})}{\rho Q g}$$
    $$H = \frac{u_1 v_{w1} - u_2 v_{w2}}{g}$$
    
    *(Note: This is the fundamental Euler equation. In many practical cases for radial discharge, $v_{w2} = 0$, or if the whirl at outlet is opposite to the direction of rotation, the formula is written as $\frac{u_1 v_{w1} + u_2 v_{w2}}{g}$. The derived formula strictly applies when $v_{w1}$ and $v_{w2}$ are vector components in the same direction as $u_1$ and $u_2$).*

***

### (b) Derive an expression for maximum efficiency of the pelton wheel giving the relationship between the jet speed and bucket speed.

**Answer:**

**Derivation:**
Let $V_1$ be the velocity of the jet and $u$ be the velocity of the bucket. For a Pelton wheel, $u = u_1 = u_2$.
Let $\phi$ be the angle of deflection of the bucket (vane angle at outlet).
Let $K$ be the blade friction coefficient (where $K=1$ implies no friction, $V_{r2} = V_{r1}$).

1.  **Work Done:**
    The work done per second per unit weight of water by a Pelton wheel is derived from velocity triangles as:
    $$\text{Work done per unit weight} = \frac{1}{g} (V_{w1} + V_{w2})u$$
    From the inlet velocity triangle: $V_{w1} = V_1$ and $V_{r1} = V_1 - u$.
    From the outlet velocity triangle: $V_{r2} = K \cdot V_{r1} = K(V_1 - u)$.
    The velocity of whirl at outlet is $V_{w2} = V_{r2} \cos\phi - u = K(V_1 - u)\cos\phi - u$.
    
    Substituting these into the work equation:
    $$\text{Work done} = \frac{u}{g} \left[ V_1 + K(V_1 - u)\cos\phi - u \right]$$
    $$\text{Work done} = \frac{u}{g} \left[ (V_1 - u) + K(V_1 - u)\cos\phi \right]$$
    $$\text{Work done} = \frac{u}{g} (V_1 - u)(1 + K\cos\phi)$$

2.  **Hydraulic Efficiency ($\eta_h$):**
    The kinetic energy supplied by the jet per unit weight is $\frac{V_1^2}{2g}$.
    $$\eta_h = \frac{\text{Work done per unit weight}}{\text{Kinetic energy supplied per unit weight}}$$
    $$\eta_h = \frac{\frac{u}{g} (V_1 - u)(1 + K\cos\phi)}{\frac{V_1^2}{2g}}$$
    $$\eta_h = \frac{2u(V_1 - u)(1 + K\cos\phi)}{V_1^2}$$

3.  **Condition for Maximum Efficiency:**
    For a given jet velocity $V_1$, the efficiency depends on the bucket speed $u$. To find the maximum efficiency, differentiate $\eta_h$ with respect to $u$ and equate it to zero.
    $$\frac{d\eta_h}{du} = 0$$
    $$\frac{d}{du} \left[ \frac{2(V_1u - u^2)(1 + K\cos\phi)}{V_1^2} \right] = 0$$
    Since $\frac{2(1 + K\cos\phi)}{V_1^2}$ is a constant, we must have:
    $$\frac{d}{du} (V_1u - u^2) = 0$$
    $$V_1 - 2u = 0$$
    **$u = \frac{V_1}{2}$**
    *(This is the relationship: For maximum efficiency, bucket speed should be half of the jet speed).*

4.  **Maximum Efficiency Expression:**
    Substitute $u = V_1/2$ into the efficiency equation:
    $$(\eta_h)_{\max} = \frac{2 \left(\frac{V_1}{2}\right) \left(V_1 - \frac{V_1}{2}\right) (1 + K\cos\phi)}{V_1^2}$$
    $$(\eta_h)_{\max} = \frac{V_1 \left(\frac{V_1}{2}\right) (1 + K\cos\phi)}{V_1^2}$$
    **$(\eta_h)_{\max} = \frac{1 + K\cos\phi}{2}$**
    
    If there is no friction ($K=1$), the expression becomes:
    **$(\eta_h)_{\max} = \frac{1 + \cos\phi}{2}$**

***

### (c) A pelton wheel has a mean bucket speed of $35\text{ m/s}$ with a jet of water flowing at the rate of $1\text{ m}^3\text{/sec}$ under a head of $170\text{ m}$. The buckets defect the jet through an angle of $170^\circ$. Calculate the power delivered to the runner and hydraulic efficiency of the turbine.

**Answer:**

**Given Data:**
*   Mean bucket speed ($u$) = $35\text{ m/s}$
*   Discharge ($Q$) = $1\text{ m}^3\text{/s}$
*   Net head ($H$) = $170\text{ m}$
*   Angle of deflection = $170^\circ$
*   Density of water ($\rho$) = $1000\text{ kg/m}^3$

**Step 1: Determine Jet Velocity and Angles**
Assume coefficient of velocity $C_v = 1.0$ (theoretical ideal) as no friction values are provided.
Velocity of the jet ($V_1$):
$$V_1 = \sqrt{2gH} = \sqrt{2 \times 9.81 \times 170}$$
$$V_1 = \sqrt{3335.4} \approx 57.75\text{ m/s}$$

The blade angle at exit ($\phi$) is related to the deflection angle:
$$\phi = 180^\circ - \text{Angle of deflection}$$
$$\phi = 180^\circ - 170^\circ = 10^\circ$$

**Step 2: Calculate Power Delivered to the Runner**
Assume the buckets are smooth, so the blade friction coefficient $K = 1$.
The formula for work done per second (Power, $P$) by a Pelton wheel is:
$$P = \rho Q u (V_1 - u)(1 + \cos\phi)$$

Substituting the known values:
$$P = 1000 \times 1 \times 35 \times (57.75 - 35) \times (1 + \cos 10^\circ)$$
$$P = 35000 \times 22.75 \times (1 + 0.9848)$$
$$P = 796250 \times 1.9848$$
$$P = 1580397\text{ Watts}$$
**Power delivered to runner ($P$) = $1580.4\text{ kW}$**

**Step 3: Calculate Hydraulic Efficiency ($\eta_h$)**
Hydraulic efficiency is the ratio of power developed by the runner to the kinetic energy supplied by the jet per second.
Kinetic energy supplied per second = $\frac{1}{2} \rho Q V_1^2$
$$K.E./sec = 0.5 \times 1000 \times 1 \times (57.75)^2$$
$$K.E./sec = 500 \times 3335.06 = 1667530\text{ Watts}$$

$$\eta_h = \frac{\text{Power delivered to runner}}{\text{K.E. supplied per second}}$$
$$\eta_h = \frac{1580397}{1667530}$$
$$\eta_h = 0.9477$$
**Hydraulic efficiency ($\eta_h$) = $94.77\%$**
### (c) A Pelton wheel working under a head of 500 m produces 13000 KW at 430 rpm. If the efficiency of the wheel is 85%, determine (i) discharge of turbine (ii) diameter of the wheel, (iii) diameters of nozzle. Assume suitable data.

**Answer:**

**Given Data:**
*   Net Head ($H$) = $500 \text{ m}$
*   Shaft Power ($P$) = $13000 \text{ kW} = 13000 \times 10^3 \text{ W}$
*   Speed ($N$) = $430 \text{ rpm}$
*   Overall efficiency ($\eta_o$) = $85\% = 0.85$
*   Density of water ($\rho$) = $1000 \text{ kg/m}^3$
*   Acceleration due to gravity ($g$) = $9.81 \text{ m/s}^2$

**Assumed Suitable Data (based on standard textbook design practices):**
*   Coefficient of velocity for the nozzle ($C_v$) = $0.98$
*   Speed ratio ($K_u$) = $0.46$
*   Number of jets ($n$) = $1$ (We will assume a single jet first and verify if the design is practical).

**Step-by-Step Solution:**

**(i) Discharge of turbine ($Q$):**
The overall efficiency is the ratio of shaft power to water power.
$$\eta_o = \frac{\text{Shaft Power } (P)}{\text{Water Power } (\rho \cdot g \cdot Q \cdot H)}$$
$$0.85 = \frac{13000 \times 10^3}{1000 \times 9.81 \times Q \times 500}$$
$$Q = \frac{13000 \times 10^3}{0.85 \times 1000 \times 9.81 \times 500}$$
$$Q = \frac{13000}{0.85 \times 9.81 \times 0.5}$$
$$Q = \frac{13000}{4.169}$$
**$Q \approx 3.118 \text{ m}^3\text{/s}$**

**(ii) Diameter of the wheel ($D$):**
First, calculate the theoretical velocity of the jet ($V_1$):
$$V_1 = C_v \sqrt{2gH}$$
$$V_1 = 0.98 \times \sqrt{2 \times 9.81 \times 500}$$
$$V_1 = 0.98 \times \sqrt{9810} = 0.98 \times 99.045 \approx 97.06 \text{ m/s}$$

Next, calculate the tangential velocity of the wheel ($u$):
$$u = K_u \sqrt{2gH}$$
$$u = 0.46 \times \sqrt{2 \times 9.81 \times 500}$$
$$u = 0.46 \times 99.045 \approx 45.56 \text{ m/s}$$

We know the relationship between peripheral velocity, diameter, and speed is:
$$u = \frac{\pi \cdot D \cdot N}{60}$$
$$45.56 = \frac{\pi \times D \times 430}{60}$$
$$D = \frac{45.56 \times 60}{\pi \times 430}$$
$$D = \frac{2733.6}{1350.88}$$
**$D \approx 2.02 \text{ m}$**

**(iii) Diameter of nozzle ($d$):**
Assuming a single jet ($n=1$), the total discharge $Q$ is equal to the area of the jet multiplied by its velocity.
$$Q = \text{Area of jet} \times \text{Velocity of jet}$$
$$Q = \frac{\pi}{4} d^2 \times V_1$$
$$3.118 = \frac{\pi}{4} \times d^2 \times 97.06$$
$$d^2 = \frac{3.118 \times 4}{\pi \times 97.06}$$
$$d^2 = \frac{12.472}{304.92} \approx 0.0409 \text{ m}^2$$
$$d = \sqrt{0.0409}$$
**$d \approx 0.202 \text{ m} \text{ or } 202 \text{ mm}$**
*(Note: The jet ratio $m = D/d = 2.02 / 0.202 = 10$. This is slightly below the typically adopted value of 12, but still within practical limits for a single jet. If a higher jet ratio was strictly required, one would assume 2 jets and recalculate).*

***

### Calculate the hydraulic efficiency of Pelton wheel to give 300 rpm under a head of 200 m of water. The runner diameter is 2 m. The water enters axially and the vanes are set back to make an angle of $30^\circ$ with tangent.

**Answer:**

*(Note: The problem statement contains a contradiction by stating it is a "Pelton wheel" but water "enters axially". A Pelton wheel is strictly a tangential flow turbine. We will proceed assuming it is a standard Pelton wheel with tangential entry, and the phrase "vanes are set back to make an angle of $30^\circ$" refers to the outlet bucket angle $\phi$.)*

**Given Data:**
*   Speed ($N$) = $300 \text{ rpm}$
*   Head ($H$) = $200 \text{ m}$
*   Runner diameter ($D$) = $2 \text{ m}$
*   Outlet vane angle ($\phi$) = $30^\circ$

**Assumptions (Standard Theoretical Values):**
*   Coefficient of velocity ($C_v$) = $1.0$ (assuming ideal nozzle unless stated otherwise)
*   Blade friction coefficient ($K$) = $1.0$ (assuming smooth buckets)

**Step-by-Step Solution:**

**1. Calculate Jet and Wheel Velocities:**
Velocity of the jet ($V_1$):
$$V_1 = C_v \sqrt{2gH}$$
$$V_1 = 1.0 \times \sqrt{2 \times 9.81 \times 200}$$
$$V_1 = \sqrt{3924} \approx 62.64 \text{ m/s}$$

Tangential velocity of the wheel ($u$):
$$u = \frac{\pi \cdot D \cdot N}{60}$$
$$u = \frac{\pi \times 2 \times 300}{60}$$
$$u = 10\pi \approx 31.42 \text{ m/s}$$

**2. Calculate Hydraulic Efficiency ($\eta_h$):**
The expression for hydraulic efficiency of a Pelton wheel is:
$$\eta_h = \frac{2(V_1 - u)(1 + K\cos\phi)u}{V_1^2}$$

Substituting the known and assumed values:
$$\eta_h = \frac{2(62.64 - 31.42)(1 + 1 \cdot \cos 30^\circ) \times 31.42}{62.64^2}$$
$$\eta_h = \frac{2(31.22)(1 + 0.866) \times 31.42}{3923.77}$$
$$\eta_h = \frac{62.44 \times 1.866 \times 31.42}{3923.77}$$
$$\eta_h = \frac{3661.12}{3923.77}$$
**$\eta_h \approx 0.933 \text{ or } 93.3\%$**

***

### (c) A pelton wheel is having a mean bucket diameter of 1m and is running at 1000 r.p.m. The net head on the pelton wheel is 700m. If the side clearance angle is $15^\circ$ and discharge through nozzle is $0.1 \text{ m}^3\text{/s}$, find: (i) power available at the nozzle and (ii) hydraulic efficiency of the turbine.

**Answer:**

**Given Data:**
*   Mean bucket diameter ($D$) = $1 \text{ m}$
*   Speed ($N$) = $1000 \text{ rpm}$
*   Net head ($H$) = $700 \text{ m}$
*   Side clearance angle (outlet angle $\phi$) = $15^\circ$
*   Discharge ($Q$) = $0.1 \text{ m}^3\text{/s}$

**Assumptions:**
*   Coefficient of velocity ($C_v$) = $1.0$ (theoretical ideal)
*   Blade friction factor ($K$) = $1.0$ (smooth buckets)

**Step-by-Step Solution:**

**(i) Power available at the nozzle:**
The power available at the nozzle is the water power supplied to the turbine.
$$\text{Water Power} = w \cdot Q \cdot H = \rho \cdot g \cdot Q \cdot H$$
$$\text{Power} = 1000 \text{ kg/m}^3 \times 9.81 \text{ m/s}^2 \times 0.1 \text{ m}^3\text{/s} \times 700 \text{ m}$$
$$\text{Power} = 686700 \text{ W}$$
**Power available at nozzle = $686.7 \text{ kW}$**

**(ii) Hydraulic efficiency of the turbine ($\eta_h$):**
First, find the jet velocity ($V_1$) and wheel velocity ($u$).
$$V_1 = C_v \sqrt{2gH} = 1.0 \times \sqrt{2 \times 9.81 \times 700}$$
$$V_1 = \sqrt{13734} \approx 117.19 \text{ m/s}$$

$$u = \frac{\pi \cdot D \cdot N}{60} = \frac{\pi \times 1 \times 1000}{60}$$
$$u \approx 52.36 \text{ m/s}$$

The hydraulic efficiency formula is:
$$\eta_h = \frac{2(V_1 - u)(1 + K\cos\phi)u}{V_1^2}$$

Substituting the values:
$$\eta_h = \frac{2(117.19 - 52.36)(1 + 1 \cdot \cos 15^\circ) \times 52.36}{(117.19)^2}$$
$$\eta_h = \frac{2(64.83)(1 + 0.9659) \times 52.36}{13733.5}$$
$$\eta_h = \frac{129.66 \times 1.9659 \times 52.36}{13733.5}$$
$$\eta_h = \frac{13346.5}{13733.5}$$
**$\eta_h \approx 0.9718 \text{ or } 97.18\%$**
### (a) Define specific speed. Derive an expression for the specific speed of a turbine. What is the significance of specific speed?

**Answer:**

**Definition of Specific Speed:**
The specific speed of a turbine is defined as the speed of a geometrically similar turbine that would develop $1 \text{ kW}$ power when working under a head of $1 \text{ meter}$. It is denoted by $N_s$.

**Derivation of the Expression:**
The overall efficiency ($\eta_o$) of any turbine is given by:
$$\eta_o = \frac{\text{Shaft Power } (P)}{\text{Water Power } (\rho \cdot g \cdot Q \cdot H)}$$
Therefore, $P = \eta_o \cdot \rho \cdot g \cdot Q \cdot H$
For a given homologous series of turbines, $\eta_o$, $\rho$, and $g$ are constant. Thus:
$$P \propto Q \times H \quad \text{--- (i)}$$

Let $D$ = Diameter of the runner, $N$ = Speed of the runner, $u$ = Tangential velocity, and $V$ = Absolute velocity of water.
The tangential velocity $u$ is proportional to the absolute velocity $V$, and $V \propto \sqrt{H}$.
$$u \propto \sqrt{H}$$
Also, $u = \frac{\pi D N}{60}$, which means $u \propto D \times N$.
Equating the proportionalities for $u$:
$$D \times N \propto \sqrt{H} \implies D \propto \frac{\sqrt{H}}{N} \quad \text{--- (ii)}$$

The discharge $Q$ through the turbine is given by Area $\times$ Velocity:
$$Q \propto D^2 \times V$$
Since $V \propto \sqrt{H}$, we have $Q \propto D^2 \times \sqrt{H}$.
Substituting the proportionality for $D$ from (ii):
$$Q \propto \left(\frac{\sqrt{H}}{N}\right)^2 \times \sqrt{H} \implies Q \propto \frac{H}{N^2} \times H^{1/2} \implies Q \propto \frac{H^{3/2}}{N^2}$$

Now, substitute this proportionality for $Q$ back into equation (i):
$$P \propto \left(\frac{H^{3/2}}{N^2}\right) \times H \implies P \propto \frac{H^{5/2}}{N^2}$$
Removing the proportionality sign by introducing a constant $K$:
$$P = K \frac{H^{5/2}}{N^2}$$

By definition of specific speed, if $H = 1 \text{ m}$ and $P = 1 \text{ kW}$, then the speed $N$ is the specific speed $N_s$.
Substituting these values:
$$1 = K \frac{1^{5/2}}{N_s^2} \implies K = N_s^2$$

Substitute the value of $K$ back into the power equation:
$$P = N_s^2 \frac{H^{5/2}}{N^2} \implies N_s^2 = \frac{N^2 P}{H^{5/2}}$$
$$N_s = \frac{N \sqrt{P}}{H^{5/4}}$$

**Significance of Specific Speed:**
1.  It plays a crucial role in the selection of the type of turbine for a given site (head and flow). For example, low $N_s$ indicates a Pelton wheel, medium $N_s$ indicates Francis, and high $N_s$ indicates Kaplan/Propeller.
2.  By knowing the specific speed, the general performance characteristics of the turbine can be predicted.
3.  It dictates the physical size and cost of the installation. A higher specific speed runner is generally smaller and more economical for a given power output, though it may increase the risk of cavitation if head is high.

***

### (b) A reaction turbine works at 500 rpm under a head of 100m. The diameter of turbine at inlet is 100cm and flow area is $0.35\text{m}^2$. The angles made by the absolute and relative velocities at inlet are $15^\circ$ and $60^\circ$ respectively with the tangential velocity. Determine (i) the volume flow rate (ii) The power developed and (iii) Hydraulic efficiency. Assume whirl at outlet to be zero.

**Answer:**

**Given Data:**
*   Speed ($N$) = $500 \text{ rpm}$
*   Head ($H$) = $100 \text{ m}$
*   Inlet diameter ($D_1$) = $100 \text{ cm} = 1.0 \text{ m}$
*   Flow area ($A_1$) = $0.35 \text{ m}^2$
*   Angle of absolute velocity at inlet ($\alpha$) = $15^\circ$
*   Angle of relative velocity at inlet ($\theta$) = $60^\circ$
*   Whirl velocity at outlet ($V_{w2}$) = $0$ (radial discharge)

**Step 1: Calculate Tangential Velocity at Inlet ($u_1$)**
$$u_1 = \frac{\pi D_1 N}{60} = \frac{\pi \times 1.0 \times 500}{60}$$
$$u_1 = 26.18 \text{ m/s}$$

**Step 2: Solve the Inlet Velocity Triangle**
From the inlet velocity triangle geometry:
$$\tan \alpha = \frac{V_{f1}}{V_{w1}}$$
$$\tan 15^\circ = \frac{V_{f1}}{V_{w1}} \implies V_{f1} = V_{w1} \tan 15^\circ \quad \text{--- (Eq 1)}$$

Also, for the relative velocity triangle:
$$\tan \theta = \frac{V_{f1}}{V_{w1} - u_1}$$
Substituting $\theta = 60^\circ$, $u_1 = 26.18$, and $V_{f1}$ from Eq 1:
$$\tan 60^\circ = \frac{V_{w1} \tan 15^\circ}{V_{w1} - 26.18}$$
$$1.732 = \frac{0.2679 V_{w1}}{V_{w1} - 26.18}$$
$$1.732 (V_{w1} - 26.18) = 0.2679 V_{w1}$$
$$1.732 V_{w1} - 45.344 = 0.2679 V_{w1}$$
$$1.732 V_{w1} - 0.2679 V_{w1} = 45.344$$
$$1.4641 V_{w1} = 45.344$$
$$V_{w1} = \frac{45.344}{1.4641} = 30.97 \text{ m/s}$$

Now find the flow velocity $V_{f1}$:
$$V_{f1} = 30.97 \times \tan 15^\circ = 30.97 \times 0.2679 = 8.30 \text{ m/s}$$

**(i) Volume Flow Rate ($Q$):**
$$Q = \text{Flow Area} \times V_{f1}$$
$$Q = 0.35 \times 8.30$$
**$Q = 2.905 \text{ m}^3\text{/s}$**

**(ii) Power Developed ($P$):**
Assuming density of water $\rho = 1000 \text{ kg/m}^3$. Since $V_{w2} = 0$, work done per second is:
$$P = \rho \cdot Q \cdot V_{w1} \cdot u_1$$
$$P = 1000 \times 2.905 \times 30.97 \times 26.18$$
$$P = 2355341 \text{ Watts}$$
**Power Developed = $2355.34 \text{ kW}$**

**(iii) Hydraulic Efficiency ($\eta_h$):**
$$\eta_h = \frac{V_{w1} \cdot u_1}{g \cdot H}$$
$$\eta_h = \frac{30.97 \times 26.18}{9.81 \times 100}$$
$$\eta_h = \frac{810.79}{981}$$
$$\eta_h = 0.8265$$
**Hydraulic Efficiency = $82.65\%$**

***

### Q3: A single jet Pelton wheel runs at 300 rpm under a head of 510 m. The jet diameter is 200 mm and its deflection inside the bucket is $165^\circ$. Assuming that its relative velocity is reduced by 15% due to friction, determine: (1) water power (2) resultant force on bucket and (3) overall efficiency. Take Mechanical loss = 3%, co-efficient of velocity = 0.98, and speed ratio = 0.46.

**Answer:**

**Given Data:**
*   Speed ($N$) = $300 \text{ rpm}$
*   Head ($H$) = $510 \text{ m}$
*   Jet diameter ($d$) = $200 \text{ mm} = 0.2 \text{ m}$
*   Deflection angle = $165^\circ \implies$ Blade exit angle $\phi = 180^\circ - 165^\circ = 15^\circ$
*   Relative velocity reduction = $15\% \implies V_{r2} = 0.85 V_{r1}$ (Friction coefficient $K = 0.85$)
*   Mechanical loss = $3\% \implies \text{Mechanical Efficiency } \eta_m = 1 - 0.03 = 0.97$
*   Coefficient of velocity ($C_v$) = $0.98$
*   Speed ratio ($K_u$) = $0.46$

**Step 1: Calculate Velocities**
Velocity of Jet ($V_1$):
$$V_1 = C_v \sqrt{2gH} = 0.98 \sqrt{2 \times 9.81 \times 510}$$
$$V_1 = 0.98 \times 100.02 = 98.02 \text{ m/s}$$

Velocity of Wheel ($u$):
$$u = K_u \sqrt{2gH} = 0.46 \sqrt{2 \times 9.81 \times 510}$$
$$u = 0.46 \times 100.02 = 46.01 \text{ m/s}$$

**Step 2: Calculate Whirl and Relative Velocities**
At inlet:
$$V_{w1} = V_1 = 98.02 \text{ m/s}$$
$$V_{r1} = V_1 - u = 98.02 - 46.01 = 52.01 \text{ m/s}$$

At outlet:
$$V_{r2} = 0.85 \times V_{r1} = 0.85 \times 52.01 = 44.21 \text{ m/s}$$
$$V_{w2} = u - V_{r2} \cos \phi = 46.01 - 44.21 \cos(15^\circ)$$
$$V_{w2} = 46.01 - (44.21 \times 0.9659) = 46.01 - 42.70 = 3.31 \text{ m/s}$$
*(Since $u > V_{r2} \cos\phi$, the outlet whirl velocity is in the same direction as the wheel motion, so the change in velocity is $(V_{w1} - V_{w2})$)*

**Step 3: Calculate Discharge ($Q$)**
$$Q = \text{Area of jet} \times \text{Velocity of jet} = \frac{\pi}{4} d^2 V_1$$
$$Q = \frac{\pi}{4} (0.2)^2 \times 98.02 = 0.031416 \times 98.02 = 3.079 \text{ m}^3\text{/s}$$

**(1) Water Power:**
$$\text{Water Power} = \rho \cdot g \cdot Q \cdot H$$
$$\text{Water Power} = 1000 \times 9.81 \times 3.079 \times 510$$
$$\text{Water Power} = 15404178 \text{ W}$$
**Water Power = $15404 \text{ kW}$**

**(2) Resultant force on bucket ($F$):**
$$F = \rho \cdot Q \cdot (V_{w1} - V_{w2})$$
$$F = 1000 \times 3.079 \times (98.02 - 3.31)$$
$$F = 3079 \times 94.71 = 291612 \text{ N}$$
**Resultant Force = $291.6 \text{ kN}$**

**(3) Overall efficiency ($\eta_o$):**
First, find the power developed by the runner (Runner Power):
$$\text{Runner Power} = F \times u = 291612 \times 46.01 = 13417068 \text{ W} = 13417 \text{ kW}$$

Next, find Shaft Power considering mechanical losses:
$$\text{Shaft Power} = \text{Runner Power} \times \eta_m = 13417 \times 0.97 = 13014.5 \text{ kW}$$

$$\eta_o = \frac{\text{Shaft Power}}{\text{Water Power}} = \frac{13014.5}{15404}$$
$$\eta_o = 0.8449$$
**Overall Efficiency = $84.49\%$**

***

### Q1: State the advantages and disadvantages of a reaction turbine over impulse turbine.

**Answer:**

Based on the textbook principles of hydraulic machines, the comparison between reaction turbines (like Francis or Kaplan) and impulse turbines (like Pelton) yields the following:

**Advantages of Reaction Turbines over Impulse Turbines:**
1.  **Head Control:** The variation in the operating head can be more easily controlled in a reaction turbine.
2.  **Head Range:** They can operate effectively over a wider range of heads; the ratio of maximum to minimum operating heads can be even up to two.
3.  **Tail Water Variation:** The operating head can be fully utilized even when the variation in the tail water level is relatively large, thanks to the use of a draft tube.
4.  **Wear and Efficiency:** The mechanical efficiency of a Pelton wheel decreases faster with wear compared to a Francis turbine.
5.  **Compactness:** For the same power generated, the size of the runner, generator, and powerhouse required is generally smaller and more economical if a reaction turbine is used instead of a Pelton wheel.

**Disadvantages (Drawbacks) of Reaction Turbines over Impulse Turbines:**
1.  **Water Quality Sensitivity:** Water containing debris or sand can cause very rapid wear in high-head Francis turbines compared to the relatively simpler bucket replacement on a Pelton wheel.
2.  **Maintenance:** Overhaul, inspection, and maintenance are much more difficult because the runner is enclosed in a complex, pressure-tight casing.
3.  **Cavitation:** Cavitation is an ever-present danger in reaction turbines (especially at the runner exit/draft tube inlet) which does not affect impulse turbines running at atmospheric pressure.
4.  **Water Hammer:** The water hammer effect is more troublesome and harder to mitigate due to the closed-conduit continuous flow nature of the reaction turbine.
5.  **Part-Load Efficiency:** If a Francis turbine is run below 50 percent of its design head for a long period, it loses efficiency significantly, and the danger of cavitation becomes much more serious (though Kaplan turbines mitigate part-load efficiency issues).
### Derive an expression for maximum efficiency of the pelton wheel giving the relationship between the jet and bucket speed.

**Answer:**

**Step-by-step Mathematical Derivation:**

Let,
*   $V_1$ = Absolute velocity of the jet of water at inlet.
*   $u$ = Peripheral (bucket) velocity of the runner. For a Pelton wheel, $u = u_1 = u_2$.
*   $V_{r1}$ = Relative velocity of the jet at inlet $= V_1 - u$.
*   $V_{w1}$ = Velocity of whirl at inlet. Since the jet strikes tangentially, $V_{w1} = V_1$.
*   $\phi$ = Angle made by the relative velocity at outlet with the direction of motion (vane angle at exit).
*   $K$ = Blade friction co-efficient. The relative velocity at outlet is $V_{r2} = K \cdot V_{r1} = K(V_1 - u)$. If the bucket is perfectly smooth, $K=1$.

**1. Expression for Work Done:**
From the velocity triangles, the velocity of whirl at the outlet ($V_{w2}$) is given by:
$$V_{w2} = V_{r2} \cos\phi - u = K(V_1 - u)\cos\phi - u$$

The work done per second per unit weight of water striking the buckets is given by the equation:
$$\text{Work done per unit weight} = \frac{1}{g} (V_{w1} + V_{w2})u$$

Substituting the values of $V_{w1}$ and $V_{w2}$ into this equation:
$$\text{Work done per unit weight} = \frac{u}{g} \left[ V_1 + \{ K(V_1 - u)\cos\phi - u \} \right]$$
$$\text{Work done per unit weight} = \frac{u}{g} \left[ (V_1 - u) + K(V_1 - u)\cos\phi \right]$$
$$\text{Work done per unit weight} = \frac{u}{g} (V_1 - u)(1 + K\cos\phi)$$

**2. Expression for Hydraulic Efficiency ($\eta_h$):**
The kinetic energy supplied by the jet at the inlet per unit weight of water is $\frac{V_1^2}{2g}$.

Hydraulic efficiency is the ratio of work done to the kinetic energy supplied:
$$\eta_h = \frac{\text{Work done per unit weight}}{\text{Kinetic energy supplied per unit weight}}$$
$$\eta_h = \frac{\frac{u}{g} (V_1 - u)(1 + K\cos\phi)}{\frac{V_1^2}{2g}}$$
$$\eta_h = \frac{2u(V_1 - u)(1 + K\cos\phi)}{V_1^2}$$

**3. Relationship between Jet Speed and Bucket Speed for Maximum Efficiency:**
For a given jet velocity ($V_1$), the efficiency depends on the bucket speed ($u$). To find the condition for maximum efficiency, we differentiate $\eta_h$ with respect to $u$ and equate it to zero.
$$\frac{d\eta_h}{du} = 0$$
$$\frac{d}{du} \left[ \frac{2(V_1u - u^2)(1 + K\cos\phi)}{V_1^2} \right] = 0$$

Since the term $\frac{2(1 + K\cos\phi)}{V_1^2}$ is a constant and cannot be zero, we must have:
$$\frac{d}{du}(V_1u - u^2) = 0$$
$$V_1 - 2u = 0$$
**$$u = \frac{V_1}{2}$$**
*This is the relationship: For maximum efficiency, the bucket speed must be exactly half of the jet speed.*

**4. Expression for Maximum Hydraulic Efficiency:**
Substitute the value $u = \frac{V_1}{2}$ back into the hydraulic efficiency equation:
$$(\eta_h)_{\max} = \frac{2 \left(\frac{V_1}{2}\right) \left(V_1 - \frac{V_1}{2}\right) (1 + K\cos\phi)}{V_1^2}$$
$$(\eta_h)_{\max} = \frac{V_1 \left(\frac{V_1}{2}\right) (1 + K\cos\phi)}{V_1^2}$$
**$$(\eta_h)_{\max} = \frac{1 + K\cos\phi}{2}$$**

Assuming perfectly smooth buckets (no friction, $K = 1$), the expression becomes:
**$$(\eta_h)_{\max} = \frac{1 + \cos\phi}{2}$$**

***

### Pelton Q6: Step-by-step mathematical derivation of Euler's fluid head equation.

**Answer:**

**Step-by-step Mathematical Derivation:**

The Euler momentum equation forms the basis for turbomachinery fluid head calculations. It is derived using the principle of angular momentum (moment of momentum) applied to fluid flowing through a rotor.

Let us define the following terms for fluid flowing through an impeller:
*   $W$ = Weight of fluid flowing through the impeller per second ($W = \rho g Q$).
*   $V_{w1}$ = Velocity of whirl at inlet (tangential component of absolute velocity).
*   $V_{w2}$ = Velocity of whirl at outlet.
*   $R_1$ = Radius of the impeller at inlet.
*   $R_2$ = Radius of the impeller at outlet.
*   $N$ = Rotational speed of the impeller in r.p.m.
*   $\omega$ = Angular velocity of the impeller $= \frac{2\pi N}{60}$ rad/s.
*   $u_1$ = Tangential velocity of the impeller at inlet $= \omega R_1$.
*   $u_2$ = Tangential velocity of the impeller at outlet $= \omega R_2$.

**1. Rate of Change of Moment of Momentum:**
The mass of fluid flowing per second is $\frac{W}{g}$.
Momentum of fluid at inlet per second $= \frac{W}{g} \cdot V_{w1}$
Moment of momentum of fluid at inlet $= \frac{W}{g} \cdot V_{w1} \cdot R_1$

Momentum of fluid at outlet per second $= \frac{W}{g} \cdot V_{w2}$
Moment of momentum of fluid at outlet $= \frac{W}{g} \cdot V_{w2} \cdot R_2$

According to Newton's second law applied to rotational motion, the torque ($T$) exerted on the fluid by the impeller (or vice versa) is equal to the rate of change of moment of momentum of the fluid.
Assuming a pump (where the impeller does work on the fluid), the torque is:
$$T = \text{Moment of momentum at outlet} - \text{Moment of momentum at inlet}$$
$$T = \frac{W}{g} (V_{w2}R_2) - \frac{W}{g} (V_{w1}R_1)$$
$$T = \frac{W}{g} (V_{w2}R_2 - V_{w1}R_1)$$

**2. Work Done per Second (Power):**
The work done by the impeller on the fluid per second is the product of Torque and angular velocity ($\omega$).
$$\text{Work done per second} = T \times \omega$$
$$\text{Work done per second} = \frac{W}{g} (V_{w2}R_2 - V_{w1}R_1) \times \omega$$
$$\text{Work done per second} = \frac{W}{g} (V_{w2}R_2\omega - V_{w1}R_1\omega)$$

Substituting the tangential velocities ($u_1 = \omega R_1$ and $u_2 = \omega R_2$) into the equation:
$$\text{Work done per second} = \frac{W}{g} (V_{w2}u_2 - V_{w1}u_1)$$

**3. Euler's Fluid Head Equation:**
The Euler head ($H_e$) is defined as the theoretical work done per unit weight of the fluid.
$$H_e = \frac{\text{Work done per second}}{\text{Weight of fluid flowing per second } (W)}$$
$$H_e = \frac{\frac{W}{g} (V_{w2}u_2 - V_{w1}u_1)}{W}$$
**$$H_e = \frac{1}{g} (V_{w2}u_2 - V_{w1}u_1)$$**

This derived expression $H_e = \frac{V_{w2}u_2 - V_{w1}u_1}{g}$ is known as the **Euler momentum equation for centrifugal pumps** (or Euler's fluid head equation). 

*(Note: For a turbine like a Pelton wheel, where the fluid does work on the runner and energy is extracted, the initial momentum is higher than the final momentum in the direction of rotation, making the Euler head equation $H_e = \frac{V_{w1}u_1 - V_{w2}u_2}{g}$. Since a Pelton wheel has $u_1 = u_2 = u$, this simplifies further to $H_e = \frac{u}{g}(V_{w1} \pm V_{w2})$).*
