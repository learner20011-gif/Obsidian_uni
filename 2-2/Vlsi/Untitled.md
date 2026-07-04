### Q.1 (a) Define propagation delay. Prove the following equation: $\frac{\omega_p}{L_p} = 2.5 \frac{\omega_n}{L_n}$ where the symbols represent their usual meanings.

**Definition of Propagation Delay:**
Propagation delay typically refers to the rise time or fall time in logic gates. It is the time required for a logic gate to change its output state in response to a change at its input stage. More formally, it is often measured as the time difference between the input and output signals crossing the 50% voltage level during a transition.

**Proof of the Equation:**
The given equation represents the design condition for achieving a symmetrical CMOS inverter. A symmetrical inverter is one where the pull-up (rise time, $\tau_r$) and pull-down (fall time, $\tau_f$) characteristics are equal, meaning the pMOS and nMOS transistors have equal current driving capabilities.

The current driving capability of an MOS transistor is determined by its gain factor, denoted by $\beta$.
For the nMOS (pull-down) transistor, the gain factor is:
$$\beta_n = \mu_n C_{ox} \frac{W_n}{L_n}$$
For the pMOS (pull-up) transistor, the gain factor is:
$$\beta_p = \mu_p C_{ox} \frac{W_p}{L_p}$$
Where:
*   $\mu_n$ and $\mu_p$ are the mobilities of electrons and holes, respectively.
*   $C_{ox}$ is the gate oxide capacitance per unit area (which is the same for both transistors if they are on the same chip).
*   $W$ ($\omega$) and $L$ represent the channel width and length, respectively.

To achieve symmetrical operation (equal rise and fall times), the gain factors of the two transistors must be equal:
$$\beta_n = \beta_p$$
Substituting the expressions for $\beta$:
$$\mu_n C_{ox} \frac{W_n}{L_n} = \mu_p C_{ox} \frac{W_p}{L_p}$$
Since $C_{ox}$ is common to both, it cancels out:
$$\mu_n \frac{W_n}{L_n} = \mu_p \frac{W_p}{L_p}$$
Rearranging the equation to find the ratio of the p-device dimensions to the n-device dimensions:
$$\frac{W_p/L_p}{W_n/L_n} = \frac{\mu_n}{\mu_p}$$
The mobility of electrons ($\mu_n$) is inherently higher than the mobility of holes ($\mu_p$). In typical silicon technology, electron mobility is approximately 2.5 times the hole mobility:
$$\mu_n \approx 2.5 \mu_p$$
Substituting this ratio into our equation yields:
$$\frac{W_p/L_p}{W_n/L_n} = \frac{2.5 \mu_p}{\mu_p} = 2.5$$
$$\frac{W_p}{L_p} = 2.5 \frac{W_n}{L_n}$$
Using the symbol $\omega$ for width as given in the question prompt, we arrive at the final proved equation:
$$\frac{\omega_p}{L_p} = 2.5 \frac{\omega_n}{L_n}$$

*Rakib's note: pg 5, 63*
*Pucknell textbook: pg 63, 115*

***

### Q.1 (b) Draw the CMOS compound gates as shown below: (i) OAI31 (ii) 4×1 MUX using 2×1 MUX. (Figure involved)

**(i) OAI31 Gate:**
An OAI31 (OR-AND-INVERT) gate implements the boolean function $Y = \overline{(A + B + C) \cdot D}$. The CMOS schematic is constructed by designing the Pull-Down Network (PDN) and Pull-Up Network (PUN).
*   **Pull-Down Network (PDN) [nMOS]:** The un-inverted expression is $(A + B + C) \cdot D$. The 'OR' operation means transistors A, B, and C are connected in parallel. The 'AND' operation means this parallel group is connected in series with transistor D. Thus, between the output node and Ground, there is an nMOS transistor D in series with a parallel combination of three nMOS transistors A, B, and C.
*   **Pull-Up Network (PUN) [pMOS]:** The PUN is the topological dual of the PDN. The parallel combination of A, B, C becomes a series combination. The series connection with D becomes a parallel connection. Thus, between VDD and the output node, there is a pMOS transistor D connected in parallel with a series combination of three pMOS transistors A, B, and C.

**(ii) 4×1 MUX using 2×1 MUX:**
A 4x1 Multiplexer (MUX) can be constructed using three 2x1 Multiplexers arranged in a two-stage hierarchical tree structure. Let the data inputs be $D_0, D_1, D_2, D_3$ and the select lines be $S_1$ (MSB) and $S_0$ (LSB).
*   **Stage 1:** Consists of two 2x1 MUXes controlled by the least significant select bit, $S_0$.
    *   **MUX 1:** Takes data inputs $D_0$ and $D_1$. Its output passes $D_0$ if $S_0=0$ and $D_1$ if $S_0=1$.
    *   **MUX 2:** Takes data inputs $D_2$ and $D_3$. Its output passes $D_2$ if $S_0=0$ and $D_3$ if $S_0=1$.
*   **Stage 2:** Consists of one 2x1 MUX controlled by the most significant select bit, $S_1$.
    *   **MUX 3:** Takes the outputs from MUX 1 and MUX 2 as its inputs. If $S_1=0$, it selects the output of MUX 1 (which is either $D_0$ or $D_1$). If $S_1=1$, it selects the output of MUX 2 (which is either $D_2$ or $D_3$). The output of MUX 3 is the final output of the 4x1 MUX.

*Rakib's note: pg 12, 90*
*Pucknell textbook: pg 157-158*

***

### Q.1 (c) Implement the following equation using CMOS compound gate: $F = \overline{(A+C)(\overline{A}+\overline{C})}$. (Figure involved)

To implement the given boolean function $F = \overline{(A+C)(\overline{A}+\overline{C})}$ as a single CMOS compound gate, we deduce the structure of the Pull-Down Network (PDN) and Pull-Up Network (PUN) directly from the expression.

*   **Pull-Down Network (PDN):**
    The PDN is constructed using nMOS transistors and implements the logic of the expression under the inversion bar: $PDN\_Logic = (A+C)(\overline{A}+\overline{C})$.
    *   The term $(A+C)$ translates to two nMOS transistors with inputs $A$ and $C$ connected in parallel.
    *   The term $(\overline{A}+\overline{C})$ translates to another two nMOS transistors with inputs $\overline{A}$ and $\overline{C}$ connected in parallel.
    *   The 'AND' operation (multiplication) between the two terms means these two parallel groups are connected in series.
    Therefore, the PDN consists of a parallel pair of nMOS transistors (A, C) in series with another parallel pair of nMOS transistors ($\overline{A}$, $\overline{C}$), connected between the output node $F$ and Ground.

*   **Pull-Up Network (PUN):**
    The PUN is constructed using pMOS transistors and is the exact topological dual of the PDN. Alternatively, applying De Morgan's laws provides the PUN logic: $PUN\_Logic = (A \cdot C) + (\overline{A} \cdot \overline{C})$.
    *   The series connection of the two main blocks in the PDN becomes a parallel connection of two main branches in the PUN.
    *   The parallel transistors within each block of the PDN become series transistors within each branch of the PUN.
    Therefore, the PUN consists of two branches connected in parallel between VDD and the output node $F$. One branch contains two pMOS transistors in series with inputs $A$ and $C$. The other branch contains two pMOS transistors in series with inputs $\overline{A}$ and $\overline{C}$.

Note: This circuit requires the inverted inputs $\overline{A}$ and $\overline{C}$, which would be generated using two separate CMOS inverters if not already available. The overall logical function of this specific gate simplifies to an XNOR gate ($F = \overline{A \oplus C} = A \odot C$).

*Rakib's note: pg 11-15*
*Pucknell textbook: pg 145-146*

### Q.3 (a) Draw the circuit diagram of an improved BiCMOS inverter using MOS transistor for the base current discharge. Discuss about its demerits. (Figure involved)

**Circuit Diagram Description:**
The improved BiCMOS inverter using MOS transistors for base current discharge is designed to eliminate the static DC current path found in simpler BiCMOS configurations and to provide a fast discharge path for the bipolar transistors without relying on space-consuming on-chip resistors.
*   The circuit utilizes two bipolar npn transistors, $T_1$ (pull-down) and $T_2$ (pull-up), to drive the output load.
*   A pMOS transistor $T_4$ acts as the logic pull-up, driving the base of $T_2$ when the input is low.
*   An nMOS transistor $T_3$ acts as the logic pull-down, driving the base of $T_1$ when the input is high.
*   To address the base current discharge, two additional nMOS transistors are incorporated:
    *   **$T_5$:** Connected between the base of $T_2$ and the output node. Its gate is driven by the input signal. It turns on to rapidly discharge the base of $T_2$ when the input goes high (turning $T_2$ off).
    *   **$T_6$:** Connected between the base of $T_1$ and Ground ($GND$). Its gate is driven by the output of a secondary internal node or arranged to turn on when $T_1$ needs to turn off, providing a fast discharge path for $T_1$'s base.

**Demerits of this improved BiCMOS Inverter:**
While this arrangement improves switching speed and eliminates the need for large resistors, it has several demerits:
1.  **Increased Complexity and Area:** The addition of transistors $T_5$ and $T_6$ increases the total transistor count (to 6 devices for a basic inverter) compared to standard CMOS (2 devices) or simpler BiCMOS designs. This consumes more silicon "real estate" (area).
2.  **Fabrication Cost:** BiCMOS technology itself requires a more complex fabrication process than standard CMOS (requiring additional masks for the buried subcollector, p-base, etc.), which increases the overall manufacturing cost.
3.  **Output Voltage Swing:** Like many BiCMOS gate designs, the output logic levels may not reach the full rail-to-rail voltages ($V_{DD}$ and $GND$). The output high level is typically $V_{DD} - V_{BE}$ (where $V_{BE}$ is the base-emitter voltage drop of $T_2$, approx 0.7V), and the output low level is limited by the saturation voltage $V_{CEsat}$ of $T_1$. This slightly reduced swing can affect noise margins compared to a pure CMOS inverter.

*Rakib's note: pg 104-105*
*Pucknell textbook: pg 52 (Figure 2.20), 66-69*

***

### Q.3 (b) Define Latch-up process and explain how Bi-CMOS circuits are susceptible of latch-up.

**Definition of Latch-up Process:**
Latch-up is a destructive condition in CMOS and related integrated circuits caused by the inherent presence of parasitic bipolar transistors (npn and pnp) formed by the p-well, n-well, and substrate regions. These parasitic transistors can interact to form a cross-coupled thyristor (Silicon Controlled Rectifier, or SCR) structure.
Under certain conditions, such as glitches on supply rails or incident radiation, sufficient substrate current can flow to forward-bias one of the parasitic junctions. If the product of the current gains of the two parasitic transistors is greater than 1 ($\beta_1 \times \beta_2 > 1$), a self-sustaining, low-resistance conducting path is established directly between the power supply ($V_{DD}$) and ground ($V_{SS}$). This condition will persist until the power is removed or the current drops below a holding level, often resulting in permanent thermal damage to the chip due to excessive current flow.

**BiCMOS Susceptibility to Latch-up:**
Contrary to being highly susceptible, one of the significant benefits of the BiCMOS process is that it produces circuits which are **less likely** to suffer from latch-up problems compared to standard CMOS. This reduced susceptibility is due to several key factors inherent in the BiCMOS fabrication process:
1.  **Reduction of Substrate and Well Resistances:** The BiCMOS process incorporates a heavily doped buried $n^+$ subcollector layer. This layer significantly reduces the $n$-well resistance ($R_w$). Additionally, a low-resistivity epitaxial p-type substrate is often used, reducing substrate resistance ($R_s$). A reduction in these parasitic resistances means that a much larger lateral current is required to develop the necessary voltage drop to turn on the parasitic transistors and initiate latch-up.
2.  **Higher Holding Current:** Because the parasitic resistances are lower, a higher holding current is required to maintain the self-sustaining thyristor state even if it is momentarily triggered.
3.  **Reduced Parasitic pnp Beta ($\beta$):** The vertical parasitic pnp transistor, which is part of the n-well latch-up circuit, has its current gain ($\beta$) significantly reduced. This reduction is caused by the presence of the buried $n^+$ layer, which acts as a recombination center and reduces the carrier lifetime in the n-base region of the parasitic transistor.

*Rakib's note: pg 61-62*
*Pucknell textbook: pg 51-54*

***

### Q.4 (a) Calculate the pull-up to pull-down ratio of a pseudo-nMOS inverter. Also determine the inverter pair delay.

**Calculation of Pull-up to Pull-down Ratio ($Z_{p.u.} / Z_{p.d.}$):**
A pseudo-nMOS inverter replaces the depletion mode pull-up transistor of a standard nMOS circuit with a pMOS transistor whose gate is permanently connected to $V_{SS}$ (Ground).
To determine the required geometric ratio, we evaluate the condition where the inverter is driven by an identical inverter, aiming for an output voltage equal to the inverter threshold, $V_{inv} = 0.5 V_{DD}$.
At this operating point:
*   The nMOS (pull-down) device is in saturation (since $0 < V_{gsn} - V_{tn} < V_{dsn}$).
*   The pMOS (pull-up) device is operating in the resistive (linear) region (since $0 < V_{dsp} < V_{gsp} - V_{tp}$).

By equating the currents of the n-transistor and the p-transistor ($I_{dsn} = I_{dsp}$) and rearranging the expression for $V_{inv}$, the ratio can be found. Assuming standard typical values:
*   $V_{inv} = 0.5 V_{DD}$
*   $V_{tn} = |V_{tp}| = 0.2 V_{DD}$
*   $V_{DD} = 5 V$
*   The mobility of electrons is approximately 2.5 times that of holes ($\mu_n = 2.5 \mu_p$)

Applying these values to the current equations yields the required ratio:
$$Z_{p.u.} / Z_{p.d.} = 3 / 1$$
Thus, the pull-up to pull-down ratio for a pseudo-nMOS inverter is **3:1**.

**Determination of Inverter Pair Delay:**
The delay of a pseudo-nMOS inverter differs from a standard nMOS inverter due to the differing channel resistances.
*   The channel sheet resistance of the pMOS pull-up is about 2.5 times higher than that of an nMOS pull-down.
*   Allowing for the required 3:1 geometric ratio, the pseudo-nMOS inverter presents an equivalent pull-up resistance between $V_{DD}$ and $V_{SS}$ of approximately 85 k$\Omega$.
*   This is compared to a resistance of about 50 k$\Omega$ for a comparable 4:1 minimum size standard nMOS inverter.
Because of this higher pull-up resistance, it takes longer to charge load capacitances. Consequently, the inverter pair delay for pseudo-nMOS logic is larger by a factor of **8.5 : 5** (or 85/50) when compared to the delay of a 4:1 minimum size nMOS inverter pair.

*Rakib's note: pg 58-60 (for general ratio concepts), pg 163-164 textbook reference*
*Pucknell textbook: pg 163-164*

***

### Q.4 (c) Implement the following function using nMOS pass-transistor. $y = A\overline{B} + \overline{C}D$ (Figure involved)

**Implementation using nMOS Pass-Transistor Logic:**
When designing switch logic networks using pass transistors, a critical design rule is that both the logic 1 and logic 0 output conditions must be deliberately satisfied; the output node cannot be left floating. Therefore, we must implement paths to $V_{DD}$ (for logic 1) and paths to $GND$ (for logic 0) using nMOS switches.

**1. Logic 1 Path (Pull-up equivalent network):**
The output $y$ should be connected to $V_{DD}$ when the function $A\overline{B} + \overline{C}D$ is true. This consists of two parallel branches:
*   **Branch 1:** Two nMOS transistors in series. The first transistor's gate is driven by $A$, and the second transistor's gate is driven by $\overline{B}$.
*   **Branch 2:** Two nMOS transistors in series. The first transistor's gate is driven by $\overline{C}$, and the second transistor's gate is driven by $D$.
These two branches are connected in parallel between the power supply ($V_{DD}$) and the output node $y$.

**2. Logic 0 Path (Pull-down equivalent network):**
The output $y$ should be connected to $GND$ when the complement of the function is true. By applying De Morgan's theorem, the complement is:
$\overline{y} = \overline{A\overline{B} + \overline{C}D} = (\overline{A} + B) \cdot (C + \overline{D})$
This requires a series connection of two parallel groups:
*   **Parallel Group 1:** Two nMOS transistors in parallel. One gate is driven by $\overline{A}$, and the other by $B$.
*   **Parallel Group 2:** Two nMOS transistors in parallel. One gate is driven by $C$, and the other by $\overline{D}$.
These two groups are connected in series between the output node $y$ and Ground ($GND$).

*(Note: In nMOS pass-transistor logic, passing a logic '1' ($V_{DD}$) through an nMOS transistor results in a degraded high voltage level of $V_{DD} - V_{tn}$. To restore the logic level to a full $V_{DD}$, this pass-transistor network is typically followed by a restoring inverter.)*

*Rakib's note: pg 16*
*Pucknell textbook: pg 136-137, 157, 191 (Rule 7)*

### Q.5 (a) Calculate the power dissipation (on) for 2 input NAND gate with enhancement pull-up if $V_{DD} = +10$ volts.

**Solution:**

To calculate the 'ON' state power dissipation, we must determine the total resistance of the conduction path from $V_{DD}$ to Ground when all inputs are HIGH (logic '1'). 

**1. Assumptions and Standard Parameters:**
*   We assume standard nMOS design methodology where the sheet resistance ($R_s$) of the n-channel is typically $10 \text{ k}\Omega/\square$.
*   For an nMOS inverter to provide a valid logic '0' output, the standard ratio of pull-up resistance ($Z_{pu}$) to pull-down resistance ($Z_{pd}$) must be $4:1$.
*   Therefore, a standard minimum-size pull-down transistor (where Length $L$ = Width $W$) has a resistance $R_{pd} = 1 \times R_s = 10 \text{ k}\Omega$.
*   A standard pull-up transistor is sized to have a resistance $R_{pu} = 4 \times R_s = 40 \text{ k}\Omega$.

**2. Resistance Calculation for a 2-input NAND Gate:**
*   A 2-input nMOS NAND gate consists of two pull-down transistors connected in **series**.
*   When both inputs are high, both pull-down transistors are ON. Assuming they are minimum size, the total pull-down resistance is the sum of their individual resistances:
    $$R_{pd(total)} = R_{pd1} + R_{pd2} = 10 \text{ k}\Omega + 10 \text{ k}\Omega = 20 \text{ k}\Omega$$
*   To maintain the required $4:1$ ratio for the overall gate to ensure a proper output low voltage ($V_{OL}$), the pull-up transistor's resistance must be four times the total pull-down resistance:
    $$R_{pu} = 4 \times R_{pd(total)} = 4 \times 20 \text{ k}\Omega = 80 \text{ k}\Omega$$
*(Note: While the question specifies an "enhancement pull-up", which operates slightly differently than a depletion pull-up by suffering a threshold drop at the output high level, the fundamental geometric sizing ratios required to establish a solid logic '0' remain governed by this resistance relationship in standard academic problems).*

**3. Power Dissipation Calculation:**
*   In the 'ON' state (both inputs high), there is a direct DC path from $V_{DD}$ to Ground.
*   The total equivalent resistance ($R_{eq}$) of this path is:
    $$R_{eq} = R_{pu} + R_{pd(total)} = 80 \text{ k}\Omega + 20 \text{ k}\Omega = 100 \text{ k}\Omega$$
*   The power dissipation ($P_{on}$) is calculated using Joule's Law:
    $$P_{on} = \frac{V_{DD}^2}{R_{eq}}$$
*   Given $V_{DD} = 10 \text{ V}$:
    $$P_{on} = \frac{(10 \text{ V})^2}{100 \text{ k}\Omega} = \frac{100}{100,000} \text{ W}$$
    $$P_{on} = 1 \times 10^{-3} \text{ W} = 1 \text{ mW}$$

The power dissipation in the 'ON' state is **1 mW**.

*Rakib's note: pg 36, 58*
*Pucknell textbook: pg 157-159, 262-263*

***

### Q.1 (a) State Moore's $1^{st}$ law of micro-electronics and draw a comparison of speed/power performance of available technologies. (Figure involved.)

**Moore's $1^{st}$ Law:**
Moore's first law (originally formulated by Gordon Moore in the 1960s) predicts that the number of transistors that can be integrated on a single semiconductor die (chip) will double approximately every 18 to 24 months. This principle has accurately characterized the exponential growth in complexity and miniaturization of integrated circuits for decades.

**Comparison of Speed/Power Performance:**
To compare different fabrication technologies, engineers look at the "speed-power product," which evaluates the trade-off between how fast a logic gate can switch (Propagation Delay) and how much energy it consumes (Power Dissipation). 

*   **CMOS (Complementary MOS):** Characterized by extremely low static power dissipation (power is primarily consumed only during switching) and moderate-to-high speed. As technology scales down, its speed improves significantly, making it the dominant technology today.
*   **nMOS:** Historically older than widespread CMOS, it has moderate power dissipation (it draws continuous static current when the output is low) and moderate speed.
*   **BiCMOS:** Combines bipolar and CMOS technologies. It offers higher speed and better capacitive load-driving capabilities than pure CMOS, but at the cost of higher power dissipation and increased manufacturing complexity.
*   **ECL (Emitter-Coupled Logic):** A bipolar logic family that provides very high speed (very low propagation delay) but suffers from very high continuous power dissipation.
*   **GaAs (Gallium Arsenide):** Uses a different semiconductor material than silicon. It offers ultra-high speeds (due to higher electron mobility) but generally consumes more power than CMOS and is more expensive to manufacture.

**Graphical Comparison Description:**
If plotting this on a graph with **Power Dissipation per Gate (e.g., $10\mu W$ to $100mW$) on the X-axis** and **Propagation Delay per Gate (e.g., $100ps$ to $10ns$) on the Y-axis** (both on logarithmic scales):
1.  **CMOS** occupies the top-left to middle-left area (lowest power, moderate delay).
2.  **nMOS** sits to the right of CMOS (higher power, similar/slightly worse delay depending on generation).
3.  **BiCMOS** is located below and to the right of CMOS (faster, but more power).
4.  **ECL** occupies the bottom-right extreme (fastest of the silicon technologies, but highest power).
5.  **GaAs** sits at the very bottom, spanning from moderate to high power (overall lowest propagation delay).

*Rakib's note: pg 3, 5*
*Pucknell textbook: pg 4, 20, 402*

***

### Q.1 (b) Draw the CMOS compound gate and stick diagram for the expression: OAI34. (Figure involved.)

An **OAI34** (OR-AND-INVERT) gate implements a specific boolean logic function consisting of a 3-input OR group and a 4-input OR group, which are then ANDed together, and the final result is inverted.
Let the inputs be $A, B, C$ (for the 3-input group) and $D, E, F, G$ (for the 4-input group).
The boolean expression is: **$Y = \overline{(A+B+C) \cdot (D+E+F+G)}$**

**1. CMOS Compound Gate Design:**
*   **Pull-Down Network (PDN):** The PDN is built with nMOS transistors and implements the un-inverted logic expression $(A+B+C) \cdot (D+E+F+G)$. 
    *   The "+" (OR) means parallel connection. So, transistors A, B, and C are in parallel. Transistors D, E, F, and G are also in parallel.
    *   The "$\cdot$" (AND) means series connection. Therefore, the parallel group (A, B, C) is connected in series with the parallel group (D, E, F, G) between the output node ($Y$) and Ground.
*   **Pull-Up Network (PUN):** The PUN is built with pMOS transistors and is the topological dual of the PDN.
    *   Series connections in the PDN become parallel connections in the PUN.
    *   Parallel connections in the PDN become series connections in the PUN.
    *   Therefore, the PUN consists of two main branches connected in parallel between $V_{DD}$ and the output node ($Y$). One branch has pMOS transistors A, B, and C connected in series. The other branch has pMOS transistors D, E, F, and G connected in series.

**2. Stick Diagram Construction:**
A stick diagram uses color-coded lines to represent different layers of the IC (Red = Polysilicon/Gates, Green = n-diffusion, Yellow = p-diffusion, Blue = Metal, Black = Contacts).

*   **Setup:** Draw a horizontal blue line at the top for $V_{DD}$ and another at the bottom for Ground ($GND$). Draw a demarcation line horizontally through the middle (p-devices go above, n-devices below).
*   **Inputs (Gates):** Draw seven vertical red lines to represent the polysilicon inputs: A, B, C, D, E, F, G.
*   **PUN (Top Half - Yellow):**
    *   We need A, B, C in series. Draw a yellow line starting from a contact on $V_{DD}$, crossing polysilicon lines A, B, and C sequentially, and then terminating at a contact on the central Metal Output line.
    *   We need D, E, F, G in series. Draw another separate yellow line starting from $V_{DD}$, crossing polysilicon lines D, E, F, and G sequentially, and terminating at the Output line.
*   **PDN (Bottom Half - Green):**
    *   We need (A||B||C) in series with (D||E||F||G).
    *   Draw a piece of horizontal metal between the nMOS transistors to act as an intermediate node (let's call it Node X).
    *   Draw green diffusion paths so that A, B, and C all individually connect the Output line to Node X (this puts them in parallel).
    *   Draw green diffusion paths so that D, E, F, and G all individually connect Node X to the GND line (this puts them in parallel, and the group is in series with the ABC group via Node X).
    *(Note: Highly optimized actual layouts would try to weave a single continuous diffusion path using Euler paths to share source/drain contacts, but the structural description above is logically accurate for a standard stick diagram).*

*Rakib's note: pg 11-15, 19-24*
*Pucknell textbook: pg 57-61, 145*

### (c) Briefly discuss about the advantages of transmission gates over pass transistor. Which is better CMOS or transmission gates in case of high-speed circuits?

**Advantages of Transmission Gates over Pass Transistors:**
A simple pass transistor (either purely nMOS or purely pMOS) suffers from a significant drawback: it cannot pass both logic levels perfectly. 
*   An **nMOS pass transistor** passes a strong logic '0' (GND) but degrades a logic '1', passing only $V_{DD} - V_{tn}$ (where $V_{tn}$ is the threshold voltage).
*   A **pMOS pass transistor** passes a strong logic '1' ($V_{DD}$) but degrades a logic '0', passing a minimum voltage of $|V_{tp}|$.

A **Transmission Gate (TG)** overcomes this by connecting an nMOS and a pMOS transistor in parallel, driven by complementary control signals. 
1.  **Full Voltage Swing:** The TG provides a full rail-to-rail output voltage swing. The pMOS transistor effectively passes the strong logic '1', and the nMOS transistor effectively passes the strong logic '0'.
2.  **Improved Noise Margin:** Because there is no threshold voltage drop across the switch, the logic levels are not degraded, leading to better noise margins in the subsequent stages.
3.  **Lower ON-Resistance:** The parallel combination of the two transistors provides a lower overall equivalent resistance during conduction compared to a single pass transistor, which can slightly improve charging/discharging times of small local capacitances.

**CMOS vs. Transmission Gates for High-Speed Circuits:**
For general high-speed circuit design, **standard static CMOS logic (restoring logic) is generally better than transmission gate logic.**
While TGs are useful for specific applications like multiplexers or XOR gates where they save transistor count, they have drawbacks for long data paths or driving significant loads:
*   **Lack of Drive Capability:** A transmission gate is a passive switch; it does not actively drive the output node to the power rails. It relies on the driving capability of the previous gate.
*   **RC Delay Accumulation:** When TGs are cascaded in series, their ON-resistances and associated node capacitances add up, resulting in a propagation delay that increases quadratically ($N^2$) with the number of stages $N$ in series. 
*   Standard CMOS gates (like inverters, NANDs, NORs) are "restoring" logic. They actively connect the output node to $V_{DD}$ or GND, providing strong drive current to quickly charge or discharge load capacitances, making them much more suitable for maintaining high speeds across complex circuits.

*Rakib's note: pg 16*
*Pucknell textbook: pg 136-137, 153-154*

***

### (d) Implement the equation $Y = \overline{((AB + CDE)F) + G}$. Write down the Boolean expression for the circuit in Fig. 1. (Figure involved)
![[image.png]]
**Part 1: Implementation of the equation $Y = \overline{((AB + CDE)F) + G}$**
To implement this using standard CMOS logic, we must design the Pull-Down Network (PDN) using nMOS transistors and the Pull-Up Network (PUN) using pMOS transistors based on the un-inverted function $f = ((AB + CDE)F) + G$.

*   **Pull-Down Network (PDN):**
    The PDN directly implements the logic of $f$.
    1.  **"AB"**: Connect two nMOS transistors (A and B) in series.
    2.  **"CDE"**: Connect three nMOS transistors (C, D, and E) in series.
    3.  **"(AB + CDE)"**: Connect the series group (A,B) in parallel with the series group (C,D,E). Let's call this Block 1.
    4.  **"((AB + CDE)F)"**: Connect an nMOS transistor F in series with Block 1. Let's call this entire combination Block 2.
    5.  **"+ G"**: Connect an nMOS transistor G in parallel with Block 2.
    Connect this entire PDN structure between the output node $Y$ and Ground ($V_{SS}$).

*   **Pull-Up Network (PUN):**
    The PUN is the topological dual of the PDN.
    1.  **"AB" dual**: Connect two pMOS transistors (A and B) in parallel.
    2.  **"CDE" dual**: Connect three pMOS transistors (C, D, and E) in parallel.
    3.  **"(AB + CDE)" dual**: Connect the parallel group (A,B) in series with the parallel group (C,D,E). Let's call this Block 1'.
    4.  **"((AB + CDE)F)" dual**: Connect a pMOS transistor F in parallel with Block 1'. Let's call this combination Block 2'.
    5.  **"+ G" dual**: Connect a pMOS transistor G in series with Block 2'.
    Connect this entire PUN structure between the power supply ($V_{DD}$) and the output node $Y$.

**Part 2: Boolean expression for the circuit in Fig. 1**
To determine the Boolean expression, it is generally most reliable to trace the paths to ground in the Pull-Down Network (PDN - bottom half of the circuit) to find the condition when $Y=0$.

Looking at the nMOS transistors in the lower half of Fig. 1:
1.  There is a direct path from the output node $Y$ to Ground through transistor **D**. Therefore, if D is ON, $Y=0$.
2.  There is another path to Ground through the left branch. Tracing from $Y$ to Ground:
    *   The path goes through transistor **A**.
    *   After A, it reaches an intermediate node.
    *   From this intermediate node, the path goes through transistor **B** to Ground.
    *   So, A and B are in series.
3.  Now observe transistor **C**. It connects the intermediate node (between A and B) to the output node $Y$. 
    *   This means transistor C provides an alternative path parallel to transistor A.
    *   Therefore, the path through the left side requires either A OR C to be ON to reach the intermediate node, and then B must be ON to reach Ground. This forms the logic $B \cdot (A + C)$.
4.  Combining the parallel paths to Ground, the PDN conducts when: $D + B \cdot (A + C)$ is true.

Since the PDN conduction pulls the output to logic '0', the Boolean function implemented by the gate is the complement of the PDN logic:
$$Y = \overline{D + B(A + C)}$$

*Rakib's note: pg 11-15*
*Pucknell textbook: pg 145-146*

***

### Q.2 (a) Draw and explain an improved BiCMOS inverter circuit to solve base current discharge problem.

**Description of the Circuit Diagram:**
An improved BiCMOS inverter is designed to overcome the limitations of the basic BiCMOS inverter, specifically the lack of a proper discharge path for the base minority carriers of the bipolar transistors when they turn off. 
The circuit consists of the following components:
1.  **Basic Logic/Drive:**
    *   A pMOS transistor ($T_4$) acts as the pull-up logic, connected between $V_{DD}$ and the base of the top bipolar transistor ($T_2$).
    *   An nMOS transistor ($T_3$) acts as the pull-down logic, connected between the base of the bottom bipolar transistor ($T_1$) and the input node (or arranged similarly to drive $T_1$).
    *   Two NPN bipolar transistors ($T_2$ for pull-up, $T_1$ for pull-down) drive the output load $C_L$.
2.  **Base Current Discharge Network (The Improvement):**
    Instead of using passive resistors (which consume large silicon area and slow down charging), MOS transistors are added to actively discharge the base nodes.
    *   **Transistor $T_5$ (nMOS):** Connected between the base of the pull-up bipolar transistor $T_2$ and the output node. Its gate is tied to the input $V_{in}$.
    *   **Transistor $T_6$ (nMOS):** Connected between the base of the pull-down bipolar transistor $T_1$ and Ground ($GND$). Its gate is suitably driven (often by the base of $T_2$ or another internal node configuration) to turn on when $T_1$ needs to be turned off.

**Explanation of Operation:**
The primary goal of $T_5$ and $T_6$ is to rapidly remove stored charge from the base of the bipolar transistors, ensuring fast turn-off times.
*   **When $V_{in}$ goes HIGH:** The pMOS $T_4$ turns OFF. The nMOS $T_5$ turns ON. $T_5$ actively shorts the base of the top bipolar $T_2$ to its emitter (the output node), rapidly discharging the base and ensuring $T_2$ turns off quickly without relying on a slow passive resistor. Concurrently, $T_3$ turns ON, driving current into the base of $T_1$, turning it ON to pull the output LOW.
*   **When $V_{in}$ goes LOW:** $T_4$ turns ON, driving $T_2$ to pull the output HIGH. $T_3$ turns OFF. To turn off $T_1$ quickly, the internal configuration ensures $T_6$ turns ON, actively shorting the base of $T_1$ to Ground, rapidly sweeping out the minority carriers and turning $T_1$ OFF.

By using active MOS transistors ($T_5$ and $T_6$) for base discharge, the circuit achieves faster switching speeds and consumes less silicon area compared to using passive discharge resistors.

*Rakib's note: pg 104-105*
*Pucknell textbook: pg 52, 67-68 (Figure 2.20)*

### Q.2 (b) What is the pull-up and pull-down ratio ($Z_{p.u.}/Z_{p.d.}$) of a pseudo nMOS inverter driven from a similar inverter? Comment on the power dissipation and inverter delay if compared to 4:1 nMOS device.

**Pull-up and Pull-down Ratio ($Z_{p.u.}/Z_{p.d.}$):**
A pseudo-nMOS inverter is constructed using an nMOS pull-down transistor and a pMOS pull-up transistor with its gate permanently connected to $V_{SS}$ (Ground), ensuring it is always conducting. 
To determine the proper geometric ratio for cascading such inverters without signal degradation, we aim for the condition where the input voltage equals the output voltage at the switching threshold, i.e., $V_{in} = V_{out} = V_{inv} = 0.5V_{DD}$.
At this operating point:
*   The nMOS pull-down device is operating in the saturation region.
*   The pMOS pull-up device is operating in the resistive (linear) region.
By equating the drain-to-source currents of both transistors ($I_{dsn} = I_{dsp}$) at this specific voltage point, and assuming typical standard parameters where electron mobility is roughly 2.5 times hole mobility ($\mu_n \approx 2.5 \mu_p$) and threshold voltages $V_{tn} = |V_{tp}| = 0.2V_{DD}$, the required impedance ratio is derived as:
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{3}{1}$$
Thus, the standard pull-up to pull-down ratio for a pseudo-nMOS inverter is **3:1**.

**Comparison with 4:1 nMOS Device:**

1.  **Power Dissipation:** 
    The power dissipation of a pseudo-nMOS inverter is **lower** than that of a comparable 4:1 standard nMOS inverter. 
    *Reasoning:* The channel sheet resistance of a pMOS transistor is about 2.5 times higher than that of an nMOS transistor. Taking the 3:1 geometric ratio into account, the pseudo-nMOS inverter presents a total equivalent resistance between $V_{DD}$ and $V_{SS}$ of approximately 85 k$\Omega$. In contrast, a comparable minimum-size 4:1 nMOS inverter presents an equivalent resistance of about 50 k$\Omega$. Since power dissipation is inversely proportional to resistance ($P = V^2/R$), the higher resistance of the pseudo-nMOS structure reduces its static power dissipation to about **60%** of the comparable nMOS device.

2.  **Inverter Delay:**
    The inverter delay of a pseudo-nMOS inverter is **larger (slower)** than that of a 4:1 standard nMOS inverter.
    *Reasoning:* The delay of an inverter is primarily determined by how quickly it can charge and discharge a load capacitance. Because the pull-up pMOS transistor in the pseudo-nMOS design has a significantly higher resistance (due to lower hole mobility and the chosen 3:1 ratio) compared to the depletion pull-up of a standard nMOS inverter, it takes longer to charge the output node from low to high. Consequently, the inverter pair delay is larger by a factor of approximately **8.5 : 5** compared to the minimum size 4:1 nMOS inverter.

*Rakib's note: pg 58-60*
*Pucknell textbook: pg 163-164*

***

### Q.2 (c) Define (i) Fan-out (ii) Inverter delay.

**(i) Fan-out:**
Fan-out is defined as the maximum number of standard logic inputs that the output of a single logic gate can reliably drive while still maintaining its specified voltage logic levels and satisfying timing constraints. In MOS technology, driving additional inputs primarily means driving additional gate capacitance. Therefore, a higher fan-out increases the capacitive load on the driving gate, which directly increases the propagation delay (slowing down the circuit) and can degrade the output voltage swing.

**(ii) Inverter delay:**
Inverter delay is the time it takes for a signal to propagate from the input of an inverter to its output. It is a measure of the switching speed of the gate. This delay is composed of two main transitions:
*   **Rise time ($\tau_r$):** The time required for the output to transition from a low logic level to a high logic level when the input goes low. It depends on the resistance of the pull-up network charging the load capacitance.
*   **Fall time ($\tau_f$):** The time required for the output to transition from a high logic level to a low logic level when the input goes high. It depends on the resistance of the pull-down network discharging the load capacitance.
The overall inverter delay is often characterized by an average propagation delay or the delay of a cascaded pair of inverters.

*Rakib's note: pg 6*
*Pucknell textbook: pg 95-98*

***

### Q.3 (a) Explain the latch-up process in CMOS circuits and suggest some methods to get rid of it.

**The Latch-up Process:**
Latch-up is a destructive failure mechanism inherent in bulk CMOS integrated circuits. It is caused by the unintended creation of parasitic bipolar transistors during the fabrication process. 
In a standard CMOS structure (e.g., p-well process), there are alternating p-type and n-type semiconductor regions. These regions form parasitic:
1.  **Vertical npn transistor:** Formed by the $n^+$ source/drain (emitter), the p-well (base), and the n-substrate (collector).
2.  **Lateral pnp transistor:** Formed by the $p^+$ source/drain (emitter), the n-substrate (base), and the p-well (collector).

These two parasitic transistors are naturally cross-coupled, meaning the collector of one feeds the base of the other. This creates a positive feedback structure equivalent to a thyristor or Silicon Controlled Rectifier (SCR). 

Normally, these parasitic transistors are turned off. However, if a transient event—such as a voltage spike on the power lines, ionizing radiation, or ringing on I/O pins—causes sufficient current to flow through the substrate or well, it can create a voltage drop across the parasitic resistances ($R_{sub}$ or $R_{well}$). If this voltage drop exceeds approx 0.7V, it can forward-bias one of the base-emitter junctions, turning on one of the parasitic transistors.
If the product of the current gains of the two transistors is greater than unity ($\beta_{npn} \times \beta_{pnp} > 1$), a self-sustaining positive feedback loop is triggered. The SCR "fires," establishing a direct, very low-resistance path between the power supply ($V_{DD}$) and Ground ($V_{SS}$). This results in a massive short-circuit current that persists even after the triggering event is gone, often leading to melting of the metal interconnects and permanent destruction of the chip.

**Methods to Get Rid of Latch-up:**
To prevent latch-up, designers aim to either break the feedback loop ($\beta_{npn} \times \beta_{pnp} < 1$) or prevent the initial forward-biasing of the junctions. Common methods include:
1.  **Guard Rings:** Highly doped $p^+$ and $n^+$ guard rings are placed around the p-well and n-well respectively. These rings act as "dummy" collectors that safely absorb injected minority carriers before they can reach the base of the parasitic transistors, effectively decoupling the SCR structure.
2.  **Increased Substrate Doping:** Using a lightly doped epitaxial layer on top of a heavily doped substrate provides a very low-resistance path for substrate currents, preventing significant voltage drops that could forward-bias the parasitic junctions.
3.  **Trench Isolation:** Deep trenches filled with insulating material (like silicon dioxide) are physically etched between the n-channel and p-channel devices, breaking the lateral current paths.
4.  **Silicon-On-Insulator (SOI):** This is the ultimate solution. The active CMOS transistors are built on a thin layer of silicon sitting on top of an insulating oxide substrate. Because the devices are completely physically isolated from each other, the parasitic bipolar transistors simply do not exist, making latch-up impossible.
5.  **Layout Rules:** Adhering strictly to layout design rules, such as maintaining minimum spacing between n-diffusions and p-diffusions, and placing frequent substrate/well contacts to keep those regions firmly tied to their supply voltages.

*Rakib's note: pg 61-62*
*Pucknell textbook: pg 51-54, 68-71*

### Q. 1(a) Explain Moore's law with graphical representation. (Figure involved.)

**Moore's Law:**
Moore's Law is a prediction made in the 1960s by Gordon Moore, one of the co-founders of Intel. He observed and predicted that the number of transistors that can be integrated onto a single dense integrated circuit (IC) or chip will approximately double every two years (sometimes stated as 18 to 24 months). This exponential growth has been the driving force behind the rapid advancement of microelectronics, leading to smaller, faster, cheaper, and more powerful computing devices over the decades. It dictates the pace of the transition from Small Scale Integration (SSI) to Ultra Large Scale Integration (ULSI) and beyond.

**Graphical Representation:**
The graphical representation of Moore's Law typically plots the "Number of transistors per chip" (often on a logarithmic scale to show exponential growth as a straight line) on the Y-axis against the "Year" of development on the X-axis. 
*   The curve usually starts from a low number in the early 1960s (e.g., 1 to 10 transistors for early logic gates).
*   It slopes upwards, showing milestones like thousands of transistors in the 1970s (LSI), millions in the late 80s/90s (VLSI/ULSI), and eventually billions in modern processors.
*   Graphs often feature two lines: a "Predicted" line based strictly on Moore's doubling formula, and an "Actual" line showing real commercial products (like specific microprocessors). Historically, the actual data points have tracked the predicted line very closely.

*Rakib's note: pg 3*
*Pucknell textbook: pg 19, 21*

***

### Q. 1(b) Design the following compound gates using CMOS: (i) $F = (ABD + A'D'B + A'BC + A'D'B')'$ (Figure involved.)

To design the CMOS compound gate for the function $F = \overline{A \cdot B \cdot D + \bar{A} \cdot \bar{D} \cdot B + \bar{A} \cdot B \cdot C + \bar{A} \cdot \bar{D} \cdot \bar{B}}$, we first need to simplify the boolean expression inside the inversion bar to minimize the required number of transistors.

**Step 1: Simplify the Boolean Expression**
Let the un-inverted function be $Y = A \cdot B \cdot D + \bar{A} \cdot \bar{D} \cdot B + \bar{A} \cdot B \cdot C + \bar{A} \cdot \bar{D} \cdot \bar{B}$
Group the second and fourth terms:
$Y = A \cdot B \cdot D + \bar{A} \cdot B \cdot C + \bar{A} \cdot \bar{D}(B + \bar{B})$
Since $(B + \bar{B}) = 1$:
$Y = A \cdot B \cdot D + \bar{A} \cdot B \cdot C + \bar{A} \cdot \bar{D}$
Now, factor out $\bar{A}$ from the last two terms:
$Y = A \cdot B \cdot D + \bar{A} \cdot (B \cdot C + \bar{D})$

So, the simplified function to implement is: **$F = \overline{A \cdot B \cdot D + \bar{A} \cdot (B \cdot C + \bar{D})}$**

**Step 2: Design the Pull-Down Network (PDN)**
The PDN uses nMOS transistors and implements the logic $Y$.
*   The term $A \cdot B \cdot D$ implies three nMOS transistors ($A, B, D$) connected in **series**. This forms Branch 1.
*   The term $\bar{A} \cdot (B \cdot C + \bar{D})$ forms Branch 2. It consists of:
    *   An nMOS transistor $\bar{A}$ in **series** with a sub-network.
    *   The sub-network implements $(B \cdot C + \bar{D})$. This means two transistors ($B, C$) in **series**, placed in **parallel** with transistor $\bar{D}$.
*   The "$+$" between the two main terms means Branch 1 and Branch 2 are connected in **parallel** between the output node $F$ and Ground ($V_{SS}$).

**Step 3: Design the Pull-Up Network (PUN)**
The PUN uses pMOS transistors and is the exact topological dual of the PDN.
*   Dual of Branch 1: Three pMOS transistors ($A, B, D$) connected in **parallel**.
*   Dual of Branch 2: A pMOS transistor $\bar{A}$ in **parallel** with a sub-network.
    *   The dual sub-network has ($B, C$) in **parallel**, placed in **series** with $\bar{D}$.
*   The two dual branches are connected in **series** between the power supply ($V_{DD}$) and the output node $F$.

*(Note: The inputs $\bar{A}$ and $\bar{D}$ require standard inverters if the complemented signals are not directly available from the system).*

*Rakib's note: pg 12-13*
*Pucknell textbook: pg 145-146*

***

### Q. 1(b) Design the following compound gates using CMOS: (ii) AOI32 (Figure involved.)

An **AOI32** (AND-OR-INVERT) gate implements a boolean function that consists of a 3-input AND group and a 2-input AND group, which are ORed together, and the entire result is inverted. Let the inputs be $A, B, C$ and $D, E$. 
The Boolean expression is: **$F = \overline{(A \cdot B \cdot C) + (D \cdot E)}$**

**1. Pull-Down Network (PDN) Design:**
The PDN uses nMOS transistors to implement the un-inverted logic $(A \cdot B \cdot C) + (D \cdot E)$.
*   The term $(A \cdot B \cdot C)$ requires three nMOS transistors with inputs $A, B,$ and $C$ connected in **series**. This is the first branch.
*   The term $(D \cdot E)$ requires two nMOS transistors with inputs $D$ and $E$ connected in **series**. This is the second branch.
*   The "$+$" (OR) operation indicates that these two branches must be connected in **parallel** between the output node $F$ and Ground ($V_{SS}$).

**2. Pull-Up Network (PUN) Design:**
The PUN uses pMOS transistors and is the topological dual of the PDN.
*   The series branch of $A, B, C$ becomes three pMOS transistors ($A, B, C$) connected in **parallel**.
*   The series branch of $D, E$ becomes two pMOS transistors ($D, E$) connected in **parallel**.
*   The parallel connection of the two main branches in the PDN becomes a **series** connection of the two parallel groups in the PUN. 
*   Therefore, the PUN consists of the parallel group ($A||B||C$) connected in series with the parallel group ($D||E$) between the supply voltage ($V_{DD}$) and the output node $F$.

*Rakib's note: pg 11-15 (concept of AOI/OAI construction)*
*Pucknell textbook: pg 145-146*

***

### Q. 1(c) Define floating Z, crowbarred and double rail logic phenomenons.

**(i) Floating Z Condition:**
A "Floating Z" (or High-Impedance) condition occurs in a CMOS circuit when both the Pull-Up Network (PUN) and the Pull-Down Network (PDN) are simultaneously turned OFF. Because there is no conducting path connecting the output node to either the power supply ($V_{DD}$) or Ground ($GND$), the output node is left electrically isolated. In this state, it cannot drive a defined logic '1' or '0' and holds its previous voltage level only temporarily via parasitic capacitance, effectively "floating" at an undefined high-impedance state denoted as 'Z'.

**(ii) Crowbarred (or Contention) Phenomenon:**
A "Crowbarred" condition (often referred to as a "Crowbanned" condition in some notes or simply "Contention") is the opposite of a floating state. It occurs when a circuit design flaw or transient timing issue causes both the Pull-Up Network (PUN) and the Pull-Down Network (PDN) to be turned ON simultaneously. This creates a direct, low-resistance short-circuit path from the power supply ($V_{DD}$) straight to Ground ($GND$). This results in a massive surge of current (short-circuit current), an undefined intermediate voltage at the output node, high power dissipation, and can potentially cause permanent thermal damage to the integrated circuit.

**(iii) Double Rail Logic:**
"Double Rail Logic" is a digital design methodology where every boolean signal is represented and routed alongside its logical complement. For every data or control line $A$, there is a parallel line carrying $\bar{A}$. This phenomenon is strictly necessary in certain logic families. For example, a CMOS transmission gate requires both the control signal and its complement to operate correctly (one to drive the nMOS gate and the inverted one to drive the pMOS gate simultaneously). Therefore, circuits heavily utilizing transmission gates inherently adopt a double rail logic routing style.

*Rakib's note: pg 11 (Floating Z & Crowbanned), pg 16 (Double Rail)*
*Pucknell textbook: pg 44-46, 136-137, 329 (conceptually)*

***

### Q. 1(c) Why do we use dynamic C-MOS logic? Draw the schematic diagram of it. (Figure involved.)

**Why we use Dynamic CMOS Logic (Advantages):**
Static CMOS logic requires $2N$ transistors to implement an $N$-input logic function ($N$ pMOS in the PUN and $N$ nMOS in the PDN). Dynamic CMOS logic was developed to overcome the area and speed limitations of static CMOS. We use it for the following primary reasons:
1.  **Reduced Transistor Count (Smaller Area):** An $N$-input dynamic CMOS gate requires only $N + 2$ transistors (one pMOS precharge transistor, one nMOS evaluate transistor, and an $N$-transistor nMOS logic evaluation block). This significantly reduces the silicon real estate required, especially for complex gates with many inputs.
2.  **Higher Switching Speed:** 
    *   The input capacitance is much lower because each input signal only has to drive a single nMOS transistor gate (instead of both an nMOS and a pMOS gate as in static CMOS).
    *   The output capacitance is also reduced because there are fewer transistors connected to the output node (the bulky pMOS PUN is replaced by a single precharge transistor).
3.  **Zero Static Power Dissipation:** Similar to static CMOS, dynamic logic ideally consumes no DC current. Power is only dissipated dynamically during switching and clock transitions.
4.  **Ratio-less Circuit:** Unlike pseudo-nMOS, dynamic CMOS logic does not rely on strict transistor size ratioing (pull-up to pull-down ratios) to determine valid output logic levels, making it easier to size for speed rather than logical correctness.

**Schematic Diagram Description:**
The basic structure of a Dynamic CMOS logic gate relies on a clock signal ($\phi$) and is divided into two phases: Precharge and Evaluate.
*   **Precharge Transistor:** A single pMOS transistor is connected between $V_{DD}$ and the Output node. Its gate is driven by the clock signal $\phi$.
*   **Evaluate Transistor:** A single nMOS transistor is connected between the bottom of the logic block and Ground. Its gate is also driven by the clock signal $\phi$.
*   **Logic Block (PDN):** An nMOS Pull-Down Network (n-block) implementing the desired logic function is placed between the Output node and the top of the Evaluate transistor.

**Operation:**
*   **Precharge Phase ($\phi = 0$):** The pMOS turns ON and the evaluate nMOS turns OFF. The output node is charged to $V_{DD}$ (logic 1), regardless of the data inputs. The logic block is isolated from ground.
*   **Evaluate Phase ($\phi = 1$):** The pMOS turns OFF and the evaluate nMOS turns ON. If the data inputs create a conducting path through the nMOS logic block, the output node discharges to Ground (logic 0). If the inputs do not create a path, the output remains high (logic 1) based on the charge stored on its parasitic capacitance.

*Rakib's note: pg 111*
*Pucknell textbook: pg 164-165*

### Q.1 (d) What is VLSI? Mentions two major advantages of VLSI.

**What is VLSI?**
VLSI stands for **Very Large Scale Integration**. It is the process of creating an integrated circuit (IC) by combining thousands (or millions) of transistors onto a single semiconductor chip. Before the advent of VLSI technology, most ICs had a limited set of functions they could perform. VLSI began in the 1970s alongside the development of complex semiconductor and communication technologies, allowing for the creation of microprocessors, memory chips, and other complex digital systems on a single piece of silicon.

**Major Advantages of VLSI:**
While there are many advantages, two of the most significant ones are:
1.  **Reduced Size and Weight:** By integrating thousands or millions of discrete components (like transistors, resistors, etc.) onto a tiny microscopic chip, the physical size and weight of electronic systems are drastically reduced. This miniaturization is what makes modern portable devices like smartphones and laptops possible.
2.  **Improved Performance and Speed:** In a VLSI circuit, the distance signals have to travel between components is microscopically small. This significantly reduces parasitic capacitance and inductance, leading to much lower propagation delays. Consequently, the operating speed and overall performance of the circuit are vastly improved compared to systems built with discrete components.

*(Other notable advantages include lower power consumption, increased reliability due to fewer external connections, and reduced cost per unit).*

*Rakib's note: pg 2*
*Pucknell textbook: pg 4 (Table 1.1), 181*

***

### Q.4 (a) Determine the pull-up and pull-down ratio ($Z_{p.u.}/Z_{p.d.}$) for an n-MOS inverter driven by another n-MOS inverter.

**Determination of the Ratio:**

Consider an arrangement where a standard nMOS inverter (Inverter 1) drives another identical nMOS inverter (Inverter 2). Both inverters use a depletion-mode pMOS transistor as the pull-up ($V_{gs} = 0$) and an enhancement-mode nMOS transistor as the pull-down. 

To cascade inverters without degrading the logic levels, we aim for symmetric operation around the inverter threshold. We set the critical point where the input voltage equals the output voltage, denoted as $V_{inv}$. For equal noise margins, we typically set:
$$V_{in} = V_{out} = V_{inv} = 0.5 V_{DD}$$

At this specific operating point ($V_{in} = 0.5 V_{DD}$), both the pull-up and pull-down transistors of the driven inverter are operating in their **saturation** regions.
Because the transistors are in series, the current flowing through both must be equal:
$$I_{ds(pull-down)} = I_{ds(pull-up)}$$

Using the saturation current equation $I_{ds} = K \frac{W}{L} \frac{(V_{gs} - V_t)^2}{2}$ and substituting $Z = L/W$, we have:
For the enhancement pull-down (p.d.) transistor:
$$I_{ds} = \frac{K}{Z_{p.d.}} \frac{(V_{inv} - V_t)^2}{2}$$
For the depletion pull-up (p.u.) transistor (where $V_{gs} = 0$):
$$I_{ds} = \frac{K}{Z_{p.u.}} \frac{(- V_{td})^2}{2}$$

Equating the two currents:
$$\frac{K}{Z_{p.d.}} \frac{(V_{inv} - V_t)^2}{2} = \frac{K}{Z_{p.u.}} \frac{(- V_{td})^2}{2}$$

Canceling common terms ($K/2$) and rearranging to solve for the ratio:
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(- V_{td})^2}{(V_{inv} - V_t)^2}$$

Now, we substitute typical threshold voltage values for an nMOS process:
*   Inverter threshold: $V_{inv} = 0.5 V_{DD}$
*   Enhancement p.d. threshold: $V_t = 0.2 V_{DD}$
*   Depletion p.u. threshold: $V_{td} = -0.6 V_{DD}$

Substituting these values into the ratio equation:
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(-(-0.6 V_{DD}))^2}{(0.5 V_{DD} - 0.2 V_{DD})^2}$$
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(0.6 V_{DD})^2}{(0.3 V_{DD})^2}$$
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \left(\frac{0.6}{0.3}\right)^2 = 2^2 = 4$$

Thus, the required pull-up to pull-down ratio for an nMOS inverter driven directly by another nMOS inverter is **$4:1$** (or $\geq 4/1$).

*Rakib's note: pg 58*
*Pucknell textbook: pg 54-55*

***

### Q.6 (a) Why do we use dynamic CMOS logic? Draw the schematic diagram and explain operation of it. (Figure involved.)

**Why do we use Dynamic CMOS logic?**
Dynamic CMOS logic is used primarily to overcome some of the disadvantages of standard static CMOS logic, particularly when designing complex gates. 
1.  **Reduced Transistor Count and Area:** A standard static CMOS gate with $N$ inputs requires $2N$ transistors ($N$ pMOS and $N$ nMOS). A dynamic CMOS gate requires only $N + 2$ transistors (an $N$-transistor logic evaluation block, plus one precharge pMOS and one evaluate nMOS). This provides a massive saving in silicon area for complex functions.
2.  **Higher Operating Speed:** Because there are fewer transistors, the input capacitance is significantly reduced (each input drives only one nMOS gate instead of a pMOS/nMOS pair). Additionally, the output node has lower capacitance because the entire bulky pMOS pull-up network is replaced by a single transistor. This allows for much faster switching speeds.
3.  **Low Static Power:** Like static CMOS, dynamic logic relies on capacitive storage and ideally draws no DC static current from the supply rails (except for minimal leakage).
4.  **Ratio-less:** Unlike pseudo-nMOS, dynamic logic does not depend on the geometric ratios of pull-up to pull-down transistors to achieve valid logic levels.

**Schematic Diagram Description:**
The basic structure of a Dynamic CMOS logic gate relies on a single-phase clock signal ($\phi$).
*   **Precharge Transistor:** A single pMOS transistor ($M_p$) connects the output node to $V_{DD}$. Its gate is driven by the clock $\phi$.
*   **Evaluate Transistor:** A single nMOS transistor ($M_e$) connects the bottom of the logic network to Ground ($GND$). Its gate is also driven by the clock $\phi$.
*   **Logic Block (PDN):** An nMOS Pull-Down Network (PDN), exactly like the one used in static CMOS, sits between the output node and the top of the evaluate transistor. The inputs ($in_1, in_2, \dots$) are applied to the gates of this block.

**Explanation of Operation:**
The operation is divided into two distinct phases controlled by the clock ($\phi$):
1.  **Precharge Phase ($\phi = 0$):**
    When the clock is low, the pMOS precharge transistor ($M_p$) is turned ON, and the nMOS evaluate transistor ($M_e$) is turned OFF. The path to ground is completely cut off by $M_e$, regardless of the state of the inputs. The output node is actively charged to $V_{DD}$ (Logic 1) through the pMOS transistor. During this phase, the output is held high, and the inputs to the logic block are allowed to change and settle.
2.  **Evaluation Phase ($\phi = 1$):**
    When the clock goes high, the pMOS precharge transistor ($M_p$) turns OFF, disconnecting the output from $V_{DD}$. Simultaneously, the nMOS evaluate transistor ($M_e$) turns ON, completing the path from the bottom of the logic block to ground.
    *   If the input signals to the PDN create a conducting path through the logic block, the charge stored on the output node's capacitance will discharge to ground, resulting in an output of Logic 0.
    *   If the inputs do *not* create a conducting path, the output node remains at $V_{DD}$ (Logic 1) due to the charge stored on its parasitic capacitance. 
    Therefore, the logic function is evaluated only during this phase based on the inputs applied.

*Rakib's note: pg 111*
*Pucknell textbook: pg 164-165*


### Q. 1(a) What are the differences between PMOS and NMOS? Explain the main steps in typical N-WELL process.

**Differences between PMOS and NMOS:**

1.  **Charge Carriers:** In an NMOS transistor, the majority charge carriers forming the channel are electrons. In a PMOS transistor, the majority charge carriers are holes.
2.  **Carrier Mobility:** The mobility of electrons ($\mu_n$) is approximately 2.5 to 3 times higher than the mobility of holes ($\mu_p$) in silicon.
3.  **Switching Speed:** Due to the higher mobility of electrons, NMOS transistors are inherently faster than PMOS transistors of the same dimensions.
4.  **On-Resistance:** For a given size, an NMOS transistor has a lower ON-resistance compared to a PMOS transistor because of the higher electron mobility. To achieve the same ON-resistance and current driving capability, a PMOS transistor must be made roughly 2.5 times wider than a corresponding NMOS transistor.
5.  **Substrate/Body:** NMOS transistors are built in a p-type substrate (or p-well). PMOS transistors are built in an n-type substrate (or n-well).
6.  **Active Area Doping:** NMOS uses heavily doped $n^+$ regions for the source and drain. PMOS uses heavily doped $p^+$ regions for the source and drain.
7.  **Threshold Voltage and Conduction:** An enhancement-mode NMOS turns ON when a positive gate-to-source voltage ($V_{gs} > V_{tn}$) is applied. An enhancement-mode PMOS turns ON when a negative gate-to-source voltage ($V_{gs} < V_{tp}$, or $V_{sg} > |V_{tp}|$) is applied.

**Main Steps in a Typical N-WELL Process:**

The N-well process is used to fabricate CMOS circuits where n-type wells are created in a p-type substrate to house the PMOS transistors, while the NMOS transistors are built directly in the native p-type substrate. The main steps are:

1.  **Substrate Preparation:** Start with a lightly doped p-type silicon wafer.
2.  **Formation of N-well Regions:** A mask is used to define the regions where PMOS transistors will be placed. Phosphorus (or another n-type dopant) is implanted into these unmasked areas to create the deep n-wells. This is usually followed by a high-temperature drive-in step.
3.  **Active Area Definition (Thinox):** A layer of silicon nitride ($Si_3N_4$) is deposited over a thin pad oxide and patterned to define the "active" areas where transistors (both NMOS and PMOS) will be formed. Thick field oxide (FOX) is grown in the areas not covered by nitride to isolate the devices. The nitride is then removed, leaving the active areas exposed.
4.  **Gate Oxidation:** A very thin, high-quality layer of silicon dioxide ($SiO_2$), known as the gate oxide, is grown over the exposed active areas.
5.  **Polysilicon Deposition and Patterning:** Polysilicon is deposited over the entire wafer and then patterned using a mask to form the gates of all transistors. This also defines the interconnects routed on the polysilicon layer.
6.  **$p^+$ Diffusion/Implantation:** A mask shields the NMOS areas and exposes the PMOS active areas (inside the n-wells). Boron (or another p-type dopant) is implanted to form the $p^+$ source and drain regions for the PMOS transistors. The polysilicon gates act as a self-aligning mask.
7.  **$n^+$ Diffusion/Implantation:** A complementary mask shields the PMOS areas and exposes the NMOS active areas (in the p-substrate). Arsenic or Phosphorus is implanted to form the $n^+$ source and drain regions for the NMOS transistors, again self-aligned to the gates.
8.  **Contact Cuts:** A thick layer of insulating oxide (often phosphorus-doped glass, PSG) is deposited over the entire wafer. A mask is used to etch contact holes (cuts) down to the polysilicon, $n^+$, and $p^+$ regions where electrical connections are needed.
9.  **Metallization:** A layer of metal (typically aluminum) is deposited over the wafer and patterned using a mask to create the required interconnection wires.
10. **Overglass/Passivation:** A final protective layer of oxide or silicon nitride is deposited to protect the chip from physical damage and contamination. A final mask is used to etch openings over the bonding pads for external package connections.

*Rakib's note: pg 108*
*Pucknell textbook: pg 25 (Mobility differences), pg 32-33 (n-well process)*

***

### Q. 3(a) Draw the gate level circuit for the function $f = A'B + AB'$ using NOT, AND and OR gates. (Figure involved.)

**Description of the Circuit Diagram:**

The function $f = A'B + AB'$ represents an Exclusive-OR (XOR) operation. To implement this using basic logic gates (NOT, AND, OR), the circuit is constructed as follows:

1.  **Inputs and Inverters (NOT Gates):**
    *   Take the input signal **A** and pass it through a NOT gate to generate **$A'$** (or $\overline{A}$).
    *   Take the input signal **B** and pass it through a second NOT gate to generate **$B'$** (or $\overline{B}$).

2.  **AND Gates:**
    *   Use a 2-input AND gate (let's call it AND1). Connect the signal **$A'$** and the original input signal **B** to its inputs. The output of AND1 is **$A'B$**.
    *   Use a second 2-input AND gate (let's call it AND2). Connect the original input signal **A** and the signal **$B'$** to its inputs. The output of AND2 is **$AB'$**.

3.  **OR Gate:**
    *   Take the outputs from AND1 ($A'B$) and AND2 ($AB'$) and connect them to the inputs of a 2-input OR gate.
    *   The final output of this OR gate is **$f = A'B + AB'$**.

*(In a graphical drawing, you would see lines branching from inputs A and B, passing through triangular NOT gates with circles, feeding into D-shaped AND gates, which then feed into a curved OR gate to produce the final output 'f'.)*

*Rakib's note: pg 65 (Standard half-adder logic context)*
*Pucknell textbook: pg 179 (Figure 6.28 shows exactly this arrangement)*

***

### Q.3 (c): Explain the use of transmission gate.

**Explanation of the Use of a Transmission Gate:**

A transmission gate (TG) is a fundamental CMOS circuit element used as an electronic switch. It consists of an nMOS transistor and a pMOS transistor connected in parallel, with their gates driven by complementary control signals (e.g., a control signal $C$ for the nMOS and $\overline{C}$ for the pMOS).

**Primary Use and Advantages:**
The primary use of a transmission gate is to overcome the fundamental limitations of using a single pass transistor (either purely nMOS or purely pMOS) to route logic signals. 

1.  **Perfect Logic Transmission (No Threshold Drop):** 
    *   A single nMOS pass transistor is excellent at passing a logic '0' (GND) but is poor at passing a logic '1'. When passing $V_{DD}$, the output voltage is degraded and only reaches $V_{DD} - V_{tn}$ (where $V_{tn}$ is the threshold voltage).
    *   Conversely, a single pMOS pass transistor passes a strong logic '1' ($V_{DD}$) perfectly but degrades a logic '0', passing only $|V_{tp}|$ instead of a solid 0V.
    *   **The transmission gate combines the strengths of both.** When the TG is turned ON (control signal is high), the pMOS transistor strongly pulls the output up to a full $V_{DD}$ for a logic '1', and the nMOS transistor strongly pulls the output down to a full $GND$ for a logic '0'. This ensures a full rail-to-rail voltage swing without any signal degradation.

2.  **Bidirectional Switching:** A transmission gate acts as a true bidirectional switch. Data can flow in either direction through the parallel source/drain terminals of the paired transistors, making it highly versatile for complex routing paths.

3.  **Lower ON-Resistance:** When turned on, the parallel combination of the nMOS and pMOS channels results in a lower overall ON-resistance compared to a single pass transistor, which can help in slightly reducing the delay when charging or discharging small local capacitances.

**Common Applications:**
Because they do not degrade logic levels, transmission gates are widely used in VLSI design to build various structures efficiently:
*   **Multiplexers (MUX):** TGs are ideal for creating data selectors where signals need to be routed cleanly without buffering every stage.
*   **Latches and Flip-Flops:** They are heavily used in forming the feedback loops and input sampling stages of static and dynamic memory elements (like D flip-flops and SRAM cells).
*   **XOR/XNOR Gates:** TGs can be used to implement these functions with fewer transistors than standard complementary CMOS logic.

*Rakib's note: pg 16*
*Pucknell textbook: pg 136-137, 154*

### Q.2 (a) Determine the pull-up to pull-down ratio ($Z_{p.u.}/Z_{p.d.}$) for an nMOS inverter driven by another nMOS inverter.

**Determination of the Ratio:**

To cascade inverters without degrading the logic levels, we aim for symmetric operation around the inverter threshold. Consider an arrangement where a standard nMOS inverter (Inverter 1) drives another identical nMOS inverter (Inverter 2). Both inverters use a depletion-mode nMOS transistor as the pull-up ($V_{gs} = 0$) and an enhancement-mode nMOS transistor as the pull-down.

We set the critical point where the input voltage equals the output voltage, denoted as the inverter threshold $V_{inv}$. For equal noise margins, we typically set:
$$V_{in} = V_{out} = V_{inv} = 0.5 V_{DD}$$

At this specific operating point ($V_{in} = 0.5 V_{DD}$), both the pull-up (p.u.) and pull-down (p.d.) transistors of the driven inverter are operating in their **saturation** regions. Because the transistors are in series, the current flowing through both must be equal:
$$I_{ds(p.u.)} = I_{ds(p.d.)}$$

Using the saturation current equation $I_{ds} = K \frac{W}{L} \frac{(V_{gs} - V_t)^2}{2}$ and substituting impedance $Z = L/W$, we have:

For the enhancement pull-down transistor (where $V_{gs} = V_{inv}$):
$$I_{ds(p.d.)} = \frac{K}{Z_{p.d.}} \frac{(V_{inv} - V_t)^2}{2}$$

For the depletion pull-up transistor (where $V_{gs} = 0$):
$$I_{ds(p.u.)} = \frac{K}{Z_{p.u.}} \frac{(- V_{td})^2}{2}$$

Equating the two currents:
$$\frac{K}{Z_{p.d.}} \frac{(V_{inv} - V_t)^2}{2} = \frac{K}{Z_{p.u.}} \frac{(- V_{td})^2}{2}$$

Canceling common terms ($K/2$) and rearranging to solve for the geometric ratio:
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(- V_{td})^2}{(V_{inv} - V_t)^2}$$

Now, we substitute typical threshold voltage values for an nMOS process:
*   Inverter threshold: $V_{inv} = 0.5 V_{DD}$
*   Enhancement p.d. threshold: $V_t = 0.2 V_{DD}$
*   Depletion p.u. threshold: $V_{td} = -0.6 V_{DD}$

Substituting these values into the ratio equation:
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(-(-0.6 V_{DD}))^2}{(0.5 V_{DD} - 0.2 V_{DD})^2}$$
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \frac{(0.6 V_{DD})^2}{(0.3 V_{DD})^2}$$
$$\frac{Z_{p.u.}}{Z_{p.d.}} = \left(\frac{0.6}{0.3}\right)^2 = 2^2 = 4$$

Thus, the required pull-up to pull-down ratio for an nMOS inverter driven directly by another nMOS inverter is **$4:1$** (or $\ge 4/1$).

*Rakib's note: pg 58-59*
*Pucknell textbook: pg 54-55*

***

### (c) Explain briefly about dc characteristics of C-MOS inverter.

**DC Characteristics of a CMOS Inverter:**

The DC characteristics of a CMOS inverter describe the steady-state relationship between the input voltage ($V_{in}$) and the output voltage ($V_{out}$). This relationship is graphically represented by the Voltage Transfer Characteristic (VTC) curve. The operation of the CMOS inverter can be divided into five distinct regions based on the states of the pMOS (pull-up) and nMOS (pull-down) transistors as $V_{in}$ sweeps from $0$ to $V_{DD}$.

1.  **Region 1 ($V_{in} < V_{tn}$):** 
    The input voltage is below the threshold voltage of the nMOS transistor ($V_{tn}$). The nMOS is completely **Cut-off** (OFF). The pMOS is strongly turned ON and operates in the **Linear** region (though no current flows since the nMOS is off). The output voltage is pulled entirely to the supply rail: $V_{out} = V_{DD}$.

2.  **Region 2 ($V_{tn} \le V_{in} < V_{DD}/2$):** 
    The input voltage exceeds $V_{tn}$, so the nMOS turns ON and begins conducting in the **Saturation** region. The pMOS remains ON but transitions into the **Linear** region. A small steady-state current flows from $V_{DD}$ to Ground. The output voltage $V_{out}$ begins to drop slightly from $V_{DD}$ but remains high.

3.  **Region 3 ($V_{in} \approx V_{DD}/2$):** 
    This is the transition region where the inverter switches states rapidly. Both the nMOS and pMOS transistors are in **Saturation**. Because both act as current sources in series, the circuit is inherently unstable in this region, resulting in a very steep slope (high gain). A small change in $V_{in}$ causes a massive change in $V_{out}$. The exact midpoint where $V_{in} = V_{out}$ is the inverter threshold voltage ($V_{inv}$).

4.  **Region 4 ($V_{DD}/2 < V_{in} \le V_{DD} - |V_{tp}|$):** 
    The input voltage continues to rise. The nMOS transistor is now fully ON and enters the **Linear** region. The pMOS transistor remains ON but is pushed into **Saturation** as the voltage across it increases. The output voltage $V_{out}$ approaches Ground rapidly.

5.  **Region 5 ($V_{in} > V_{DD} - |V_{tp}|$):** 
    The input voltage is high enough that the gate-to-source voltage of the pMOS ($V_{DD} - V_{in}$) is less than its threshold magnitude $|V_{tp}|$. The pMOS is completely **Cut-off** (OFF). The nMOS is strongly ON in the **Linear** region. With the pMOS off, no current flows, and the output is pulled entirely to ground: $V_{out} = 0V$.

In an ideal, symmetrically designed CMOS inverter (where $\beta_n = \beta_p$), the VTC is perfectly symmetrical, and the switching threshold $V_{inv}$ is exactly $V_{DD}/2$, maximizing noise margins.

*Rakib's note: pg 60 (Mentions regions conceptually during ratio calculations)*
*Pucknell textbook: pg 61-63*

***

### Q.6 (b): Why do we use Dynamic C-MOS logic? Draw the schematic diagram of it. (Figure involved.)

**Why do we use Dynamic CMOS logic?**

Dynamic CMOS logic is utilized primarily to overcome the area, speed, and capacitance limitations associated with standard static CMOS logic, especially when implementing complex multi-input logic gates. The main advantages are:
1.  **Reduced Transistor Count (Smaller Area):** A standard static CMOS gate requires $2N$ transistors for an $N$-input function ($N$ pMOS and $N$ nMOS). A dynamic CMOS gate requires only $N + 2$ transistors (an $N$-transistor nMOS logic evaluation block, plus one pMOS precharge transistor and one nMOS evaluate transistor). This saves significant silicon area.
2.  **Higher Operating Speed:** The input capacitance is drastically reduced because each input signal only drives one transistor gate (an nMOS) rather than two (an nMOS and a pMOS). The output capacitance is also lower because the large pMOS pull-up network is replaced by a single precharge transistor.
3.  **Low Static Power:** Like static CMOS, dynamic logic ideally consumes no DC static power. Power is dissipated only dynamically during switching and clocking.
4.  **Ratio-less Design:** Dynamic logic does not rely on strict pull-up to pull-down geometric ratios to determine valid output logic levels (unlike pseudo-nMOS), simplifying the design process.

**Schematic Diagram Description:**

The basic structure of a Dynamic CMOS logic gate relies on a single clock signal ($\phi$) and consists of three main parts:
*   **Precharge Transistor:** A single pMOS transistor connected between the power supply ($V_{DD}$) and the Output node. Its gate is driven by the clock signal ($\phi$).
*   **Evaluate Transistor:** A single nMOS transistor connected between the bottom of the logic evaluation block and Ground ($GND$). Its gate is also driven by the clock signal ($\phi$).
*   **Logic Block (PDN):** An nMOS Pull-Down Network (n-block) that implements the desired Boolean logic function. It is placed between the Output node and the drain of the Evaluate transistor.

**Operation:**
*   **Precharge Phase ($\phi = 0$):** The pMOS turns ON, charging the output node to $V_{DD}$. The nMOS evaluate transistor is OFF, preventing any path to ground.
*   **Evaluate Phase ($\phi = 1$):** The pMOS turns OFF. The nMOS evaluate transistor turns ON. If the input data creates a conducting path through the nMOS logic block, the output discharges to $0V$. If no path exists, the output remains floating HIGH at $V_{DD}$ due to stored parasitic charge.

*Rakib's note: pg 111*
*Pucknell textbook: pg 164-165*

***

### Q.6 (d): Make a comparative aspects of key parameters of CMOS and bipolar transistor.

**Comparative Aspects of Key Parameters:**

CMOS (Complementary Metal-Oxide-Semiconductor) and Bipolar technologies each possess distinct characteristics that make them suitable for different applications. Below is a comparison of their key parameters:

1.  **Power Dissipation:**
    *   **CMOS:** Very low static power dissipation. Power is primarily consumed only during switching (dynamic power).
    *   **Bipolar:** High static power dissipation. It draws continuous current during operation.
2.  **Input Impedance / Drive Current:**
    *   **CMOS:** Extremely high input impedance (essentially acts as a capacitor). Requires very low drive current.
    *   **Bipolar:** Low input impedance. Requires a continuous base drive current to maintain operation.
3.  **Output Drive Capability:**
    *   **CMOS:** Relatively low output drive current capability. Driving large capacitive loads significantly increases delay.
    *   **Bipolar:** High output drive current capability. Excellent for driving heavy capacitive loads quickly.
4.  **Packing Density:**
    *   **CMOS:** High packing density. Transistors can be scaled down easily, allowing for millions of gates on a single chip (ideal for VLSI).
    *   **Bipolar:** Low packing density. Bipolar transistors are physically larger and generate more heat, limiting integration density.
5.  **Transconductance ($g_m$):**
    *   **CMOS:** Low transconductance. It is linearly proportional to the input voltage ($g_m \propto V_{in}$).
    *   **Bipolar:** High transconductance. It is exponentially dependent on the input voltage ($g_m \propto e^{V_{in}}$), allowing for high gain and fast switching with small voltage swings.
6.  **Switching Device Characteristics:**
    *   **CMOS:** Acts as a near-ideal bidirectional switch (the source and drain are physically interchangeable).
    *   **Bipolar:** Essentially unidirectional devices; not ideal for pass-transistor type switching logic.
7.  **Voltage Swing / Noise Margin:**
    *   **CMOS:** Full rail-to-rail voltage swing (from $GND$ to $V_{DD}$), providing high noise margins.
    *   **Bipolar:** Lower voltage swing logic (like ECL), resulting in lower noise margins.
8.  **Delay Sensitivity to Load:**
    *   **CMOS:** High delay sensitivity to load capacitance (fan-out limitations are strict).
    *   **Bipolar:** Low delay sensitivity to load capacitance.

*Rakib's note: pg 104-105*
*Pucknell textbook: pg 37 (Table 1.2), 48-49*

### Q. 1 (a) What are pass transistors and transmission gates? Sketch a static CMOS gate computing $Y = (A + B + C).D$ (Figure involved.)

**Pass Transistors:**
A pass transistor is a single MOSFET (typically an nMOS transistor, but can be a pMOS) used as a switch to pass logic levels between nodes in a circuit. It is driven by a control signal at its gate. 
*   An **nMOS pass transistor** is an excellent conductor for a logic '0' (passes a "strong 0") but is a poor conductor for a logic '1'. When passing a $V_{DD}$ (logic 1) signal, the output is degraded to $V_{DD} - V_{tn}$ (where $V_{tn}$ is the threshold voltage).
*   Similarly, a **pMOS pass transistor** passes a "strong 1" but a degraded "weak 0" ($|V_{tp}|$).

**Transmission Gates (TG):**
A transmission gate is an electronic switch constructed by connecting an nMOS transistor and a pMOS transistor in parallel. The gates of these two transistors are driven by complementary control signals (e.g., $C$ for nMOS and $\overline{C}$ for pMOS).
*   Because the nMOS passes a strong '0' and the pMOS passes a strong '1', the parallel combination can pass **both logic levels perfectly without any voltage degradation**. It provides a full rail-to-rail voltage swing, making it a superior switch compared to a single pass transistor, though it requires more area and complementary control signals.

**Sketching a static CMOS gate for $Y = (A + B + C).D$:**
Standard static CMOS compound gates inherently implement *inverting* logic functions. The given function $Y = (A + B + C) \cdot D$ is non-inverting. Therefore, to implement this using static CMOS, we must first design a gate to compute the inverted function $\overline{Y} = \overline{(A + B + C) \cdot D}$, and then cascade it with a standard CMOS inverter to obtain the final true output $Y$.

1.  **Stage 1: OAI Gate for $\overline{Y}$**
    *   **Pull-Down Network (PDN) [nMOS]:** The un-inverted expression for the first stage is $(A+B+C) \cdot D$. The OR operation ($+$) implies a parallel connection, so nMOS transistors A, B, and C are connected in parallel. The AND operation ($\cdot$) implies a series connection, so this entire parallel group (A||B||C) is connected in series with nMOS transistor D to Ground.
    *   **Pull-Up Network (PUN) [pMOS]:** The PUN is the topological dual of the PDN. The parallel group (A||B||C) becomes a series group of pMOS transistors A, B, and C. The series connection with D becomes a parallel connection. So, the series group (A-B-C) is placed in parallel with pMOS transistor D, connected to $V_{DD}$.
    *   The output of this stage is $\overline{Y}$.

2.  **Stage 2: Inverter**
    *   Connect the intermediate output $\overline{Y}$ to the input of a standard CMOS inverter (one pMOS in PUN, one nMOS in PDN).
    *   The output of this inverter is the final desired function $Y = (A + B + C) \cdot D$.

*(In a schematic sketch, you would draw the PUN and PDN for Stage 1 connected to intermediate node $\overline{Y}$, which then connects to the gates of a basic CMOS inverter whose output is $Y$.)*

*Rakib's note: pg 16 (pass transistor/TG), pg 11-15 (compound gates)*
*Pucknell textbook: pg 34, 136-137 (pass transistor/TG), pg 145-146 (logic gates)*

***

### Q. 1 (b) State Moor's law. What do you mean by the integrated circuits (ICs)? Sketch a 3-input NAND gate using CMOS. (Figure involved.)

**Moore's Law:**
Moore's Law is an empirical observation and prediction made by Gordon Moore (co-founder of Intel). It states that the number of transistors that can be densely integrated onto a single semiconductor chip approximately doubles every 18 to 24 months. This principle has accurately described the exponential trend of miniaturization and increasing computational power in the semiconductor industry for decades.

**Integrated Circuits (ICs):**
An Integrated Circuit (IC), often referred to as a chip or microchip, is a miniaturized electronic circuit consisting of active devices (like transistors) and passive devices (like resistors and capacitors) fabricated together on a single, small piece of semiconductor material (usually silicon). The IC era began to replace discrete component electronics because ICs offer drastically reduced size, lower power consumption, higher reliability, and massive improvements in speed and complex functionality.

**Sketch of a 3-input NAND gate using CMOS:**
A 3-input NAND gate implements the boolean function $Y = \overline{A \cdot B \cdot C}$.
*   **Pull-Down Network (PDN):** The logic under the inversion bar is $A \cdot B \cdot C$ (AND logic). In the PDN, AND translates to a **series** connection. Therefore, three nMOS transistors with inputs A, B, and C are connected in series between the output node $Y$ and Ground ($V_{SS}$).
*   **Pull-Up Network (PUN):** The PUN is the dual of the PDN. A series connection in the PDN becomes a **parallel** connection in the PUN. Therefore, three pMOS transistors with inputs A, B, and C are connected in parallel between the power supply ($V_{DD}$) and the output node $Y$.

*(In a schematic sketch, three pMOS transistors are drawn side-by-side at the top connected to $V_{DD}$, and their drains all tie to output $Y$. Three nMOS transistors are drawn stacked vertically at the bottom, connecting $Y$ to Ground.)*

*Rakib's note: pg 3 (Moore's Law), pg 2-4 (IC), pg 10, 22 (NAND)*
*Pucknell textbook: pg 4, 19, 21 (Moore's Law, IC), pg 138 (NAND)*

***

### Q. 1 (c) What do you mean by SSI, MSI, LSI and VLSI of chips? Write down the basic difference between ECL, TTL and CMOS families.

**Meaning of SSI, MSI, LSI, and VLSI:**
These terms refer to the scale of integration, categorizing semiconductor chips based on their complexity and the number of electronic components (specifically transistors or logic gates) integrated onto a single die.
*   **SSI (Small Scale Integration):** The earliest generation of ICs. Typically contains fewer than 10 to 100 logic gates or a maximum of about 100 transistors per chip. Examples include basic logic gates and flip-flops.
*   **MSI (Medium Scale Integration):** Contains tens to hundreds of logic gates, roughly 100 to 1,000 transistors per chip. Examples include multiplexers, decoders, and simple counters.
*   **LSI (Large Scale Integration):** Contains hundreds to thousands of logic gates, roughly ranging from 500 to 20,000 transistors per chip. Examples include early microprocessors, ROM, and RAM chips.
*   **VLSI (Very Large Scale Integration):** Contains tens of thousands to millions of logic gates, typically from 20,000 to over 1,000,000 transistors per chip. Examples include advanced microprocessors, digital signal processors, and large memory arrays.

**Basic Differences Between ECL, TTL, and CMOS Families:**

| Feature | CMOS (Complementary Metal-Oxide-Semiconductor) | TTL (Transistor-Transistor Logic) | ECL (Emitter-Coupled Logic) |
| :--- | :--- | :--- | :--- |
| **Base Component** | Uses Field Effect Transistors (MOSFETs: pMOS and nMOS). | Uses Bipolar Junction Transistors (BJTs) operating in saturation. | Uses BJTs operating in the active (non-saturated) region. |
| **Power Dissipation** | **Very Low.** Consumes power primarily only during switching (dynamic power); static power is almost negligible. | **Moderate.** Draws continuous static current. | **Very High.** Draws large continuous currents to maintain high speeds. |
| **Operating Speed** | **Moderate to High.** Highly dependent on technology node (scaling improves speed significantly). | **Moderate.** Faster than early CMOS, but slower than modern CMOS and ECL. | **Very High (Fastest).** Avoiding BJT saturation eliminates charge storage delays. |
| **Packing Density** | **Very High.** Transistors are very small, allowing millions per chip (Ideal for VLSI). | **Low to Moderate.** BJTs and resistors take up significant area. | **Low.** Components are large, and high power dissipation limits how closely they can be packed. |
| **Noise Margin** | **Excellent.** Full rail-to-rail voltage swing ($V_{DD}$ to Ground). | **Good.** | **Poor.** Low voltage swing makes it susceptible to noise. |

*Rakib's note: pg 3-4 (Integration scales), pg 5-6, 104 (Tech comparisons)*
*Pucknell textbook: pg 4, 22 Table 1.1 (Integration scales), pg 20, 37 Table 1.2 (Tech comparisons)*
### Q.2 (a): Explain the operation of Bi-CMOS inverter. Clearly specify its characteristics. (figure involved)

The Bi-CMOS inverter utilizes both CMOS and bipolar technology to combine the low power dissipation and high input impedance of CMOS with the high current driving capability of bipolar transistors. A basic Bi-CMOS inverter consists of two bipolar transistors ($T_1$ and $T_2$) forming the output push-pull stage, one nMOS transistor ($T_3$), and one pMOS transistor ($T_4$).

**Operation:**
*   **Logic 1 Input ($V_{in} = V_{DD}$ or $+5V$):** When the input is high, the pMOS transistor $T_4$ is turned OFF, and the nMOS transistor $T_3$ is turned ON. Because $T_4$ is OFF, no base current is supplied to the top bipolar transistor $T_2$, rendering it non-conducting. The ON transistor $T_3$ supplies current to the base of the bottom bipolar transistor $T_1$, turning it ON. $T_1$ then acts as a strong current sink, rapidly discharging the load capacitance $C_L$ towards ground ($0V$). The output voltage falls to $0V$ plus the small saturation voltage ($V_{CEsat}$) across the collector to emitter of $T_1$.
*   **Logic 0 Input ($V_{in} = 0V$ or GND):** When the input is low, the nMOS transistor $T_3$ is turned OFF, which cuts off the base current to $T_1$, making $T_1$ non-conducting. Simultaneously, the pMOS transistor $T_4$ is turned ON. $T_4$ supplies current to the base of $T_2$, turning it ON. $T_2$ acts as a strong current source, rapidly charging the load capacitance $C_L$ towards $V_{DD}$. The output voltage rises to $V_{DD}$ less the base-emitter voltage drop ($V_{BE} \approx 0.7V$) of $T_2$.

**Characteristics:**
1.  **High Output Drive Capability:** The bipolar output transistors can source and sink large currents, allowing the inverter to drive large capacitive loads with short propagation delays compared to standard CMOS.
2.  **Low Output Impedance:** The bipolar transistors present a low impedance when turned on, which facilitates fast charging and discharging of loads.
3.  **High Input Impedance:** The input signal drives the gates of the MOS transistors, resulting in very low steady-state input current.
4.  **Good Logic Levels:** The output logic levels are close to the power supply rails, although slightly degraded by the $V_{CEsat}$ drop for a low output and the $V_{BE}$ drop for a high output.
5.  **High Noise Margins:** Similar to CMOS, Bi-CMOS circuits offer good immunity to noise.
6.  **Compact Area for High Drive:** It achieves high current drive while occupying a relatively small silicon area compared to purely MOS-based super-buffers.

Location: Pucknell textbook, page 49-50.

***

### (a) Differentiate between restoring circuits and non-restoring circuits. Briefly explain the working principle of a tri-state inverter. (figure involved)

**Differentiation between Restoring and Non-restoring Circuits:**

*   **Restoring Circuits:** These are logic circuits designed to actively drive their output nodes to the full power supply rail voltages ($V_{DD}$ for logic '1' and Ground for logic '0'). Even if an input signal is slightly degraded (e.g., slightly below $V_{DD}$ or slightly above $0V$ but still within valid logic thresholds), a restoring circuit will regenerate a clean, full-swing logic level at its output. Standard CMOS logic gates such as inverters, NAND, and NOR gates are restoring circuits because their active pull-up and pull-down networks provide direct, low-resistance paths to the power rails.
*   **Non-restoring Circuits:** These circuits do not actively restore output signals to the full rail voltages and can introduce voltage degradation as the signal passes through them. A common example is pass-transistor logic. For instance, when a logic '1' ($V_{DD}$) is passed through a single nMOS pass transistor, the output voltage drops to $V_{DD} - V_t$ (where $V_t$ is the threshold voltage). If this degraded signal passes through multiple non-restoring stages, it can eventually fall out of the valid logic range, requiring a restoring gate (like an inverter) to pull the signal back to full strength.

**Working Principle of a Tri-state Inverter:**

A tri-state inverter operates like a standard logic inverter but includes an additional "enable" control that allows its output to be effectively disconnected from the circuit. It has three possible output states: logic '1' (High), logic '0' (Low), and a High-Impedance state ('Z'). It receives a data input (A) and an enable input (EN).

*   **Enabled State (EN = 1):** When the enable signal is active, the inverter functions normally. It actively drives the output line. If the input A is '0', the active pull-up path drives the output to '1' ($V_{DD}$). If the input A is '1', the active pull-down path drives the output to '0' (GND).
*   **Disabled/High-Impedance State (EN = 0):** When the enable signal is inactive, the internal connections to both the $V_{DD}$ and GND rails are severed. The output is left electrically isolated or "floating." In this 'Z' state, the inverter behaves as an open circuit; it neither supplies current to nor draws current from the output line. This is crucial for bus architectures where multiple devices share a single communication line, ensuring only one device actively drives the bus at any given time while others remain in the high-impedance state.

Location: Pucknell textbook, page 137. Rakib's note, page 18.

***

### (b) Derive the expression for CMOS inverter rise time and fall time. (figure involved)

The propagation delay of a CMOS inverter can be estimated by calculating the time required to charge or discharge a load capacitance $C_L$. 

**Rise-time ($\tau_r$) Estimation:**
During the rise time, the input transitions from High to Low, causing the pMOS transistor to turn ON and the nMOS transistor to turn OFF. The pMOS transistor charges the load capacitance $C_L$. To simplify the analysis, we assume the pMOS device remains in the saturation region for the entire charging period.
The saturation current for the p-transistor is:
$I_{dsp} = \frac{\beta_p (V_{gs} - |V_{tp}|)^2}{2}$
Assuming this charging current is approximately constant, the relationship between voltage, current, capacitance, and time is:
$V_{out} = \frac{I_{dsp} \cdot t}{C_L}$
Substituting the expression for $I_{dsp}$ into this equation and rearranging to solve for time ($t$):
$t = \frac{2 C_L V_{out}}{\beta_p (V_{gs} - |V_{tp}|)^2}$
We define the rise time $t = \tau_r$ as the time it takes for the output voltage $V_{out}$ to reach the full supply voltage $+V_{DD}$. During this charging phase, the input is at $0V$, making the gate-to-source voltage of the pMOS transistor $V_{gs} = V_{DD}$.
$\tau_r = \frac{2 V_{DD} C_L}{\beta_p (V_{DD} - |V_{tp}|)^2}$
For a typical CMOS process, the threshold voltage $|V_{tp}|$ is approximately $0.2V_{DD}$. Substituting this approximation simplifies the expression:
$\tau_r = \frac{2 V_{DD} C_L}{\beta_p (V_{DD} - 0.2V_{DD})^2} = \frac{2 V_{DD} C_L}{\beta_p (0.8 V_{DD})^2} = \frac{2 C_L}{0.64 \beta_p V_{DD}}$
This is commonly approximated to:
$\tau_r \approx \frac{3 C_L}{\beta_p V_{DD}}$

**Fall-time ($\tau_f$) Estimation:**
A similar derivation applies to the fall time, where the input transitions from Low to High, turning the nMOS ON and the pMOS OFF. The nMOS transistor discharges $C_L$ to ground. Assuming the nMOS operates primarily in saturation during discharge:
The saturation current is $I_{dsn} = \frac{\beta_n (V_{gs} - V_{tn})^2}{2}$
Following the same steps as above, setting the final condition for fall time and using the approximation $V_{tn} \approx 0.2V_{DD}$, the fall time $\tau_f$ is estimated as:
$\tau_f \approx \frac{3 C_L}{\beta_n V_{DD}}$

Location: Pucknell textbook, pages 97-98.

***

### (c) Write short notes on: Noise margin, Fan in and Fan out.

**Noise Margin:**
Noise margin is a measure of a logic circuit's tolerance to unwanted noise voltages. It defines the maximum noise voltage amplitude that can be superimposed on a valid input logic signal without causing the gate to incorrectly interpret the state and produce an erroneous output. 
*   **High-level noise margin ($NMH$):** Calculated as $V_{OHmin} - V_{IHmin}$, it is the difference between the minimum guaranteed voltage of a logic '1' output and the minimum input voltage recognized as a logic '1'.
*   **Low-level noise margin ($NML$):** Calculated as $V_{ILmax} - V_{OLmax}$, it is the difference between the maximum input voltage recognized as a logic '0' and the maximum guaranteed voltage of a logic '0' output.
A larger noise margin indicates a more robust and reliable circuit design.

**Fan-in:**
Fan-in refers to the total number of input terminals a specific logic gate has. For instance, a 3-input NAND gate has a fan-in of 3. In CMOS circuit design, increasing the fan-in generally degrades performance. A higher fan-in requires adding more transistors either in series (which increases the overall resistance of the pull-up or pull-down network) or in parallel (which increases the parasitic capacitance at the input or output nodes). Both of these factors contribute to increased propagation delays.

**Fan-out:**
Fan-out is defined as the maximum number of subsequent standard logic gate inputs that a single driving gate's output can reliably connect to. If a gate's fan-out limit is exceeded, it may no longer be able to maintain its output voltage within specified logic levels, or its switching speed may slow down unacceptably. In CMOS technology, the input to a gate is primarily capacitive. Therefore, driving multiple gates means the driver must charge and discharge a larger total load capacitance ($C_L$). A higher fan-out directly leads to increased rise and fall times, thereby increasing the propagation delay of the driving circuit.

Location: Pucknell textbook, page 268, 20. Rakib's note, page 6.


### (c) Sketch an inverter circuit using nMOS. How does it work? Enlist the drawbacks of using nMOS inverter circuit. (figure involved)

**Circuit Description:**
A basic nMOS inverter circuit consists of two n-channel MOS transistors. The lower transistor is an enhancement-mode nMOS, which acts as the pull-down switch. Its source is connected to the ground ($GND$), and its gate serves as the input terminal ($V_{in}$). The upper transistor is a depletion-mode nMOS, which acts as the pull-up load. Its drain is connected to the positive supply voltage ($V_{DD}$), and its gate and source are tied together. The common connection point between the source of the pull-up transistor and the drain of the pull-down transistor forms the output terminal ($V_{out}$). 

**How it works:**
The operation of the nMOS inverter relies on the switching action of the enhancement-mode pull-down transistor against the constant current source-like behavior of the depletion-mode pull-up transistor.
*   **Logic 0 Input ($V_{in} = 0V$):** When the input voltage is low (below the threshold voltage $V_t$ of the enhancement transistor), the pull-down transistor is turned OFF and conducts essentially zero current. The depletion-mode pull-up transistor, having its gate tied to its source ($V_{gs} = 0V$), is always in a conducting state because its threshold voltage is negative. It acts as a pull-up resistor, charging the output node to the full supply voltage. Therefore, the output is a logic '1' ($V_{out} = V_{DD}$).
*   **Logic 1 Input ($V_{in} = V_{DD}$):** When the input voltage is high, the pull-down enhancement transistor turns ON and begins to conduct. The pull-up transistor is also ON. The two transistors form a voltage divider between $V_{DD}$ and ground. To ensure that the output voltage is recognized as a valid logic '0', the "ON" resistance of the pull-down transistor must be made significantly smaller than the effective resistance of the pull-up transistor. When properly ratioed, the pull-down transistor sinks the current provided by the pull-up transistor and pulls the output node down near ground. Therefore, the output is a logic '0' ($V_{out} \approx 0V$).

**Drawbacks of using an nMOS inverter circuit:**
1.  **High Static Power Dissipation:** When the input is at logic '1' and the output is at logic '0', both the pull-up and pull-down transistors are actively conducting. This creates a direct DC current path from the supply ($V_{DD}$) to ground, resulting in continuous and significant static power consumption.
2.  **Asymmetric Switching Speeds:** The inverter exhibits unequal rise and fall times. Because the pull-up transistor must have a higher resistance than the pull-down transistor to achieve a good logic '0' level, charging a load capacitance through the high-resistance pull-up (rise time) is much slower than discharging it through the low-resistance pull-down (fall time).
3.  **Ratioed Logic Requirement:** The correct operation of the gate relies on the physical dimensions (the $Z = L/W$ ratio) of the pull-up and pull-down transistors being strictly controlled. Typically, a $Z_{p.u.} / Z_{p.d.}$ ratio of 4:1 is required. This complicates design and limits how small the gate can be made.
4.  **Degraded Logic '0' Level:** The output voltage for a logic '0' never quite reaches perfect ground ($0V$) because it is determined by the voltage divider action of the two conducting transistors. It will always be slightly above $0V$.

Location: Pucknell textbook, pages 52-54. Rakib's note, page 58.

***

### Q. 2(a) & (c): Explain the dc characteristics of CMOS inverter. With neat sketch explain the transfer characteristics of a CMOS inverter. (figure involved)

The DC transfer characteristics of a CMOS inverter describe the steady-state relationship between the input voltage ($V_{in}$) and the output voltage ($V_{out}$). 

**Transfer Characteristic Curve Description:**
A plot of the transfer characteristic shows $V_{in}$ on the horizontal axis (from $0V$ to $V_{DD}$) and $V_{out}$ on the vertical axis (from $0V$ to $V_{DD}$). The curve starts flat at $V_{out} = V_{DD}$ for low inputs, then transitions sharply downwards in the middle, and ends flat at $V_{out} = 0V$ for high inputs. This curve is divided into five distinct regions based on the operating states of the component nMOS and pMOS transistors.

**Operating Regions:**

*   **Region 1: $0 \le V_{in} < V_{tn}$ (Logic 0 Input)**
    In this region, the input voltage is lower than the threshold voltage of the n-channel transistor ($V_{tn}$). 
    *   **nMOS:** OFF (Cut-off region), as $V_{gsn} < V_{tn}$.
    *   **pMOS:** ON and operating in the linear (resistive) region, as its gate-source voltage is highly negative ($V_{gsp} = V_{in} - V_{DD}$).
    Since the nMOS is off, no current flows through the inverter from $V_{DD}$ to ground. The pMOS transistor actively pulls the output node entirely up to the supply voltage. Thus, $V_{out} = V_{DD}$.

*   **Region 2: $V_{tn} \le V_{in} < V_{inv}$**
    The input voltage just exceeds the threshold of the nMOS transistor, but is below the inverter's switching threshold ($V_{inv} \approx V_{DD}/2$).
    *   **nMOS:** Conducts and operates in the saturation region. It has a small $V_{gs}$ and a large $V_{ds}$ (since $V_{out}$ is still high).
    *   **pMOS:** Still conducting but remains in the linear region because the voltage across it ($V_{DD} - V_{out}$) is still small.
    A small current begins to flow from $V_{DD}$ to ground. The output voltage $V_{out}$ starts to fall slightly from $V_{DD}$.

*   **Region 3: $V_{in} \approx V_{inv}$ (Transition Region)**
    The input voltage is approximately half the supply voltage.
    *   **nMOS:** Operates in the saturation region.
    *   **pMOS:** Also operates in the saturation region.
    In this narrow region, both transistors act as current sources in series. The circuit is highly unstable and exhibits its maximum voltage gain. A very small change in $V_{in}$ causes a very large and rapid change in $V_{out}$, causing the sharp drop in the transfer curve. Maximum current flows through the inverter in this state.

*   **Region 4: $V_{inv} < V_{in} \le V_{DD} - |V_{tp}|$**
    The input voltage is now high, but slightly less than $V_{DD}$ minus the magnitude of the pMOS threshold voltage.
    *   **nMOS:** Now operates in the linear region, as $V_{ds}$ (which is $V_{out}$) has fallen to a small value.
    *   **pMOS:** Is driven into the saturation region.
    The output voltage $V_{out}$ continues to drop, approaching $0V$.

*   **Region 5: $V_{in} > V_{DD} - |V_{tp}|$ (Logic 1 Input)**
    The input voltage is very close to or equal to $V_{DD}$.
    *   **nMOS:** ON and operating strongly in the linear region, providing a low-resistance path to ground.
    *   **pMOS:** OFF (Cut-off region), because its gate-source voltage ($V_{gsp} = V_{in} - V_{DD}$) is less negative than its threshold voltage $V_{tp}$.
    Again, no steady-state current flows. The nMOS transistor actively pulls the output node entirely down to ground. Thus, $V_{out} = 0V$.

Location: Pucknell textbook, pages 61-62.

***

### (b) Determine the pull-up to pull-down ratio ($Z_{pu}/Z_{pd}$) for an nMOS inverter driven by another nMOS inverter. (figure involved)

To determine the required ratio of the pull-up to pull-down channel dimensions ($Z_{pu}/Z_{pd}$) for an nMOS inverter driven by an identical nMOS inverter, we analyze the condition where the output of the first inverter (which is the input to the second) is at the switching threshold voltage, $V_{inv}$.

Let us establish the following conditions:
1.  We aim for symmetrical noise margins, which implies the inverter threshold voltage $V_{inv}$ should be set to half the supply voltage: $V_{inv} = 0.5 V_{DD}$.
2.  At this operating point, $V_{in} = V_{out} = V_{inv}$.
3.  Under this condition, we assume both the pull-up depletion transistor and the pull-down enhancement transistor are operating in their saturation regions.
4.  Since the transistors are in series, the drain-to-source current ($I_{ds}$) must be the same for both.

The current equation for a MOS transistor in saturation is:
$I_{ds} = \frac{K}{Z} \cdot \frac{(V_{gs} - V_t)^2}{2}$
where $Z = L/W$ is the length-to-width ratio, $V_t$ is the threshold voltage, and $K = \mu \epsilon_{ins} \epsilon_0 / D$.

**For the depletion-mode pull-up transistor:**
The gate is connected to the source, so $V_{gs} = 0$. Let its threshold voltage be $V_{td}$ (which is a negative value).
$I_{pu} = \frac{K}{Z_{pu}} \cdot \frac{(0 - V_{td})^2}{2} = \frac{K}{Z_{pu}} \cdot \frac{(-V_{td})^2}{2}$

**For the enhancement-mode pull-down transistor:**
The gate-to-source voltage is the input voltage, so $V_{gs} = V_{inv}$. Let its threshold voltage be $V_t$ (a positive value).
$I_{pd} = \frac{K}{Z_{pd}} \cdot \frac{(V_{inv} - V_t)^2}{2}$

Equating the currents ($I_{pu} = I_{pd}$):
$\frac{K}{Z_{pu}} \cdot \frac{(-V_{td})^2}{2} = \frac{K}{Z_{pd}} \cdot \frac{(V_{inv} - V_t)^2}{2}$

Canceling common terms and rearranging to find the ratio $Z_{pu}/Z_{pd}$:
$\frac{Z_{pu}}{Z_{pd}} = \frac{(-V_{td})^2}{(V_{inv} - V_t)^2} = \left[ \frac{-V_{td}}{V_{inv} - V_t} \right]^2$

Now, we substitute typical parameter values for an nMOS process:
*   $V_{inv} = 0.5 V_{DD}$ (our design goal for equal margins)
*   $V_t = 0.2 V_{DD}$ (typical enhancement threshold)
*   $V_{td} = -0.6 V_{DD}$ (typical depletion threshold)

Substituting these values into the equation:
$\frac{Z_{pu}}{Z_{pd}} = \left[ \frac{-(-0.6 V_{DD})}{0.5 V_{DD} - 0.2 V_{DD}} \right]^2$
$\frac{Z_{pu}}{Z_{pd}} = \left[ \frac{0.6 V_{DD}}{0.3 V_{DD}} \right]^2$
$\frac{Z_{pu}}{Z_{pd}} = (2)^2 = 4$

Therefore, the required pull-up to pull-down ratio $Z_{pu}/Z_{pd}$ for an nMOS inverter driven directly by another identical inverter is **4:1**.

Location: Pucknell textbook, pages 54-55. Rakib's note, page 58.


