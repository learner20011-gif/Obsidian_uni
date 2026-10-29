# QnA: Practical Aspects of Design Tools and Testability of CMOS Design

---

### **Transition Delay Calculations of Inverters**

#### 1. "Calculate the inverter delay of double pair or 4-stage CMOS circuit." (Page 3, Q.5(b))

**Answer:**
- **Inverter Delay ($\tau_{inv}$):** The average propagation delay through a single inverter stage:
  $$\tau_{inv} = \frac{\tau_{fall} + \tau_{rise}}{2}$$
- **Pair Delay ($\tau_{pair}$):** Total delay through two cascaded inverters (covers one falling and one rising transition):
  $$\tau_{pair} = \tau_{fall} + \tau_{rise} = 2 \times \tau_{inv}$$
- **Double Pair (4-Stage CMOS Circuit) Delay:**
  - A double pair consists of $N = 4$ identical cascaded inverters (2 inverter pairs).
  - Total Delay:
    $$\tau_{4-stage} = 2 \times \tau_{pair} = 2(\tau_{fall} + \tau_{rise}) = 4 \times \tau_{inv}$$
  - In a symmetrical CMOS design where $\tau_{fall} \approx \tau_{rise} = \tau$:
    $$\tau_{4-stage} = 4\tau$$

---

#### 2. "Define (i) Fan-out (ii) Inverter delay." (Page 4, Q.2(c))

**Answer:**
- **(i) Fan-out:**
  - The maximum number of standard gate inputs that the output of a single logic gate can drive reliably without exceeding delay specifications or signal degradation.
  - Expressed as capacitance ratio: $F = \frac{C_{load}}{C_{in}}$, or current ratio: $F = \frac{I_{out(max)}}{I_{in}}$.
- **(ii) Inverter Delay:**
  - The time elapsed between the 50% voltage transition of the input and the corresponding 50% transition of the output:
    $$\tau_d = \frac{\tau_{pHL} + \tau_{pLH}}{2}$$
  - Where $\tau_{pHL}$ is high-to-low delay and $\tau_{pLH}$ is low-to-high delay.

---

#### 3. "Calculate the transition delay for the following inverters [figure Involved]" (Page 6, Q.4(b))

![[attachments/Pasted image 20260717221618.png]]

**Answer:**
- **Given Circuit:** Cascaded inverters with transistor aspect ratios driving load capacitance $C_L$.
- **Transition Delay Equations:**
  1. **Fall Time ($\tau_f$):** NMOS discharges load $C_L$ from $V_{DD} \to 0$:
     $$\tau_f \approx \frac{3 C_L}{\beta_n V_{DD}} = 3 R_{on,n} C_L$$
  2. **Rise Time ($\tau_r$):** PMOS charges load $C_L$ from $0 \to V_{DD}$:
     $$\tau_r \approx \frac{3 C_L}{\beta_p V_{DD}} = 3 R_{on,p} C_L$$
  3. **Stage Delay:** $\tau_{stage} = \frac{\tau_r + \tau_f}{2}$.
  4. **Tapering Rule:** When driving a large capacitive load $C_L$ from input gate capacitance $C_{in}$ through $N$ stages, total delay is minimized when each stage is scaled by optimal step factor:
     $$f = \left(\frac{C_L}{C_{in}}\right)^{1/N} \approx e \approx 2.72$$

---

#### 4. "Derive the expression for CMOS inverter rise time and fall time." (Page 12, Q.2(b))
#### 5. "Derive the expression for CMOS inverter rise and fall time." (Page 13, Q.2(b))

**Answer:**
Let load capacitance be $C_L$ and power supply be $V_{DD}$.

1. **Fall Time ($\tau_f$):** Input steps from $0 \to V_{DD}$, NMOS pulls $V_{out}$ down from $90\% V_{DD}$ to $10\% V_{DD}$.
   - **Saturation Phase ($V_{out} = V_{DD} \to V_{DD} - V_{tn}$):**
     $$I_{ds} = \frac{\beta_n}{2}(V_{DD} - V_{tn})^2$$
     $$\tau_{f1} = \frac{C_L [V_{DD} - (V_{DD} - V_{tn})]}{I_{ds}} = \frac{2 C_L V_{tn}}{\beta_n (V_{DD} - V_{tn})^2}$$
   - **Linear Phase ($V_{out} = V_{DD} - V_{tn} \to 0.1 V_{DD}$):**
     $$-C_L \frac{dV_{out}}{dt} = \beta_n \left[(V_{DD} - V_{tn})V_{out} - \frac{V_{out}^2}{2}\right]$$
     Integrating from $V_{out} = V_{DD} - V_{tn}$ to $0.1 V_{DD}$:
     $$\tau_{f2} = \frac{C_L}{\beta_n(V_{DD}-V_{tn})} \ln\left(\frac{2(V_{DD}-V_{tn}) - 0.1V_{DD}}{0.1V_{DD}}\right)$$
   - **Total Fall Time:**
     $$\tau_f = \tau_{f1} + \tau_{f2} \approx \frac{3.7 C_L}{\beta_n V_{DD}} \approx 3 \text{ to } 4 \times R_n C_L$$

2. **Rise Time ($\tau_r$):** Input steps from $V_{DD} \to 0$, PMOS pulls $V_{out}$ up from $10\% V_{DD}$ to $90\% V_{DD}$.
   - Symmetrically, replacing NMOS parameters with PMOS parameters ($\beta_p, |V_{tp}|$):
     $$\tau_r \approx \frac{3.7 C_L}{\beta_p V_{DD}} \approx 3 \text{ to } 4 \times R_p C_L$$
   - Since hole mobility is lower ($\mu_n \approx 2.5 \mu_p$), equal rise and fall times ($\tau_r = \tau_f$) require sizing:
     $$\left(\frac{W}{L}\right)_p \approx 2.5 \times \left(\frac{W}{L}\right)_n$$

---

#### 6. "Define inverter delay. Find the nMOS inverter pair delay in ns of the following figure. [figure Involved]" (Page 16, Q.3(a))

**Answer:**
- **Inverter Delay Definition:** The propagation delay of a single inverter gate, measured between the 50% points of input and output signals.
- **nMOS Inverter Pair Delay Calculation:**
  - An nMOS inverter pair consists of two consecutive stages:
    - Stage 1 transition is pull-down ($\tau_{pHL}$), where NMOS driver discharges load: $R_{pd} = 10\text{ k}\Omega = 1 R_s$.
    - Stage 2 transition is pull-up ($\tau_{pLH}$), where depletion/resistor load charges gate: $R_{pu} = 40\text{ k}\Omega = 4 R_s$ (for a 4:1 inverter ratio).
  - Total pair delay in units of transit time $\tau$:
    $$\tau_{pair} = \tau_{pHL} + \tau_{pLH} = (1 + 4)\tau = 5\tau$$
  - Given basic transit time $\tau = 0.1\text{ ns}$ (or technology value from figure):
    $$\tau_{pair} = 5 \times 0.1\text{ ns} = 0.5\text{ ns}$$

---

#### 7. "Find the gate delay of a cascaded pair of pseudo NMOS inverter driven by another same type of inverter. Also calculate their ratios. [figure Involved]" (Page 26, Class Test: 02, Set: A, Q.1)

**Answer:**
- **Pseudo-NMOS Inverter Concept:**
  - Pull-up consists of a single PMOS transistor with its gate permanently tied to Ground (always ON).
  - Pull-down consists of an NMOS logic transistor.
- **Sizing Ratio ($Z_{pu}/Z_{pd}$):**
  - To produce an acceptable logic LOW voltage ($V_{OL} \le 0.1 V_{DD}$), NMOS pull-down must significantly overpower PMOS pull-up:
    $$\frac{Z_{pu}}{Z_{pd}} = \frac{(L/W)_p}{(L/W)_n} = \frac{\mu_n}{\mu_p} \approx 3:1 \text{ to } 4:1$$
- **Gate Delay of Cascaded Pair:**
  - Pull-down delay $\tau_{pHL}$: NMOS conducts, sinking load current plus PMOS static current:
    $$\tau_{pHL} \approx \frac{C_L V_{DD}}{I_{D,n} - I_{D,p}}$$
  - Pull-up delay $\tau_{pLH}$: NMOS turns OFF, weak PMOS charges load alone:
    $$\tau_{pLH} \approx \frac{C_L V_{DD}}{I_{D,p}}$$
  - Cascaded pair delay:
    $$\tau_{pair} = \tau_{pHL} + \tau_{pLH}$$
  - Pseudo-NMOS has asymmetric delay ($\tau_{pLH} \gg \tau_{pHL}$) and consumes static DC power when input is HIGH, but saves layout area over CMOS.

---

### **CIF Code and Geometric CIF Primitives**

#### 8. "Define DRC, LVS and CIF code." (Page 6, Q.5(c))
#### 10. & 11. "Define DRC, LVS and CIF code." (Page 6, Q.5(c))

**Answer:**
- **DRC (Design Rule Checker):**
  - A CAD verification tool that verifies the layout geometry complies with foundry physical design rules (minimum wire width, minimum spacing, extension, enclosure, overlap) to prevent lithographic defects and circuit failure.
- **LVS (Layout Versus Schematic):**
  - A tool that extracts the transistor netlist directly from layout geometries and performs a 1-to-1 isomorphism match against the schematic netlist to verify component counts, pin connections, and device sizes ($W/L$).
- **CIF (Caltech Intermediate Form):**
  - A standard human-readable, geometry-based text file format used to describe physical mask layers and geometric primitives for integrated circuit fabrication.

---

#### 9. "Draw the graphical representation of CIF primitives for the table below: [figure Involved]" (Page 7, Q.7(b))

![[attachments/Pasted image 20260717221106.png]]

**Answer:**
CIF primitives describe 2D shapes on physical mask layers:
1. **Box (B):**
   - Syntax: `B Length Width X Y [Direction_X Direction_Y]`
   - Visual: Rectangle of specified Length and Width centered at coordinate $(X, Y)$.
2. **Polygon (P):**
   - Syntax: `P X1 Y1 X2 Y2 X3 Y3 ...`
   - Visual: Filled polygon formed by connecting coordinate vertices $(X_1, Y_1) \to (X_2, Y_2) \to \dots \to (X_n, Y_n)$ in sequence.
3. **Wire (W):**
   - Syntax: `W Width X1 Y1 X2 Y2 ...`
   - Visual: Path of uniform Width connecting center-line points with rounded or squared endpoints.
4. **Round Flash (R):**
   - Syntax: `R Diameter X Y`
   - Visual: Filled circle of given Diameter centered at $(X, Y)$ (typically used for circular contact cuts and via holes).

---

### **Rule of Ten in VLSI Systems Test Costs**

#### 12. "What is rule of 10 in VLSI system? Give an example of cost associated with the rule of 10." (Page 7, Q.7(c))

**Answer:**
- **Rule of 10 Definition:**
  - A commercial empirical rule stating that the cost to detect, isolate, and repair a defect increases by a factor of approximately **10** (one order of magnitude) at each subsequent packaging and integration level.
- **Cost Progression Example:**

| Testing Stage | Typical Cost per Fault Detected |
| :--- | :--- |
| **Wafer Level (Die Test)** | \$0.10 to \$0.50 |
| **Packaged Chip Level** | \$1.00 to \$5.00 |
| **Printed Circuit Board (PCB) Level** | \$10.00 to \$50.00 |
| **System Integration Level** | \$100.00 to \$500.00 |
| **Field / Customer Site Level** | \$1,000.00 to \$5,000.00+ |

- **Importance:** Investing in chip-level Design for Testability (DFT) saves millions by detecting defects before packaging and board assembly.

---

### **Sensitized Path-Based Testing**

![[attachments/sensitized_path_testing.png]]

#### 13. "Construct the test vectors for z: SA1 in the following Fig. and explain in details using path sensitized model. [figure Involved]" (Page 3, Q.6(b))
#### 14. "Is it possible to construct test vectors in Fig.8.1 and Fig. 8.2? Find the test vectors using sensitized path based testing. [figure Involved]" (Page 5, Q.8(b))
#### 15. "Determine whether the fault below is detectable or undetectable? Explain with proper stages of sensitized path-based testing and test vectors. [figure Involved]" (Page 6, Q.5(a))
#### 16. "Construct the test vectors for x : SA1 and y : SA1 in following figure and explain in detail using path sensitized model [figure Involved]" (Pages 20 & 21, Q.(c))
#### 17. "1. sensitized path based testing er math -------- 05" (Page 23, CT-04, Q.1)

**Answer:**
**The 3 Stages of Sensitized Path Method:**
1. **Fault Activation:**
   - Force the faulty node to the value *opposite* to the targeted stuck-at fault:
     - For **SA1 (Stuck-At-1):** Drive node to logic **0** (faulty line stays 1, producing error $D'$).
     - For **SA0 (Stuck-At-0):** Drive node to logic **1** (faulty line stays 0, producing error $D$).
2. **Fault Propagation:**
   - Create a sensitized path from the fault site to a primary output by setting all side inputs of intermediate gates to **non-controlling values**:
     - **AND / NAND gates:** Side inputs must be **1**.
     - **OR / NOR gates:** Side inputs must be **0**.
     - **XOR / XNOR gates:** Side inputs must be a fixed logic level (**0** or **1**).
3. **Line Justification:**
   - Backtrack from the gate inputs toward primary inputs to find input values $(A, B, C, \dots)$ that produce the required internal node states.
   - **Detectability:**
     - If consistent primary inputs exist without contradictions $\implies$ Fault is **Detectable**, inputs form the **Test Vector**.
     - If contradictory assignments occur (e.g., node simultaneously requires $A=0$ and $A=1$) $\implies$ Fault is **Undetectable (Redundant)**.

---

### **SA0 and SA1 Faults in Combinational Logic Testing**

#### 18. "Determine the test vector for the given circuit in Fig. 7. [figure Involved]" (Page 5, Q.7(b))

**Answer:**
- **Step-by-Step Procedure:**
  1. **Identify the target fault:** Determine the fault site and type (e.g., Line $K$ SA0 or SA1).
  2. **Activate fault:**
     - If SA0 $\implies$ set $K = 1$.
     - If SA1 $\implies$ set $K = 0$.
  3. **Sensitize propagation path:** Follow the signal path from line $K$ to the output pin. Set all off-path inputs of along-path AND/NAND gates to $1$, and OR/NOR gates to $0$.
  4. **Justify lines:** Solve for primary inputs $(A, B, C, \dots)$ by back-tracing.
  5. The resulting binary assignment $(A, B, C, \dots)$ is the test vector.

---

#### 19. & 22. "What are the different types of faults that occur in manufacturing of chips? Explain with examples." (Page 7, Q.8(b); Page 10, Q.5(c))

**Answer:**
1. **Stuck-At Faults (Logical):**
   - Signal line permanently fixed at logic 0 (**Stuck-at-0, SA0**) or logic 1 (**Stuck-at-1, SA1**).
   - *Example:* Short circuit from a poly signal track to Ground ($V_{SS}$) causes SA0.
2. **Bridging Faults:**
   - Unintended short circuit between two adjacent parallel signal lines.
   - *Example:* Metal sliver shorts data line A and B, creating a wired-AND or wired-OR condition.
3. **Stuck-Open Faults:**
   - Transistor branch is permanently broken / open circuit (e.g., missing contact window).
   - *Example:* Open NMOS transistor in a CMOS NOR gate causes output to retain previous charge (acts like dynamic memory).
4. **Stuck-On Faults:**
   - Transistor permanently conducts regardless of gate voltage (e.g., gate oxide breakdown).
   - *Example:* NMOS stuck-on causes large DC leakage current from $V_{DD}$ to Ground ($I_{DDQ}$ defect).
5. **Delay / Transition Faults:**
   - Logic functions correctly, but gate propagation delay exceeds timing limits ($t_{pd} > T_{clk}$).

---

#### 20. "Discuss the technique for testing a VLSI circuit under system level and chip level." (Page 10, Q.5(a))

**Answer:**
- **Chip Level Testing:**
  - Performed directly on the wafer/die or individual package using Automated Test Equipment (ATE).
  - **Techniques:**
    - *Parametric Testing:* Verifies electrical characteristics ($V_{th}$, input/output leakage, drive current, $I_{DDQ}$).
    - *Scan Design (Internal Scan):* Replaces regular flip-flops with scan flip-flops chained into shift registers (Scan-In/Scan-Out) to make sequential circuits testable as combinational logic.
    - *BIST (Built-In Self-Test):* On-chip pattern generator (LFSR) and signature analyzer (MISR) test internal blocks at full chip speed.
- **System Level Testing:**
  - Tests multiple assembled chips interacting on a motherboard / printed circuit board (PCB).
  - **Techniques:**
    - *Boundary Scan (IEEE 1149.1 / JTAG):* Tests inter-chip board wiring connections, solder opens, and short circuits via standard 4-wire test bus (TDI, TDO, TCK, TMS).
    - *System Diagnostics / Firmware Self-Test:* Executes software routines (POST, memory march tests, bus loopback tests).

---

#### 21. "What is the significance of design for testability for VLSI system? Mention the differences between stuck-open and stuck on faults." (Page 10, Q.5(b))

**Answer:**
- **Significance of Design for Testability (DFT):**
  - **Enhances Controllability:** Makes it easy to set internal nodes to desired states from external input pins.
  - **Enhances Observability:** Makes internal node states easily measurable at external output pins.
  - **Economic Benefit:** Drastically reduces test generation time, cuts expensive tester usage, and prevents defective parts from reaching higher system levels (per Rule of 10).

- **Differences: Stuck-Open vs Stuck-On Faults:**

| Feature | Stuck-Open Fault | Stuck-On Fault |
| :--- | :--- | :--- |
| **Physical Defect** | Open circuit / broken conductor in transistor branch | Short circuit / punctured gate oxide causing permanent conduction |
| **Transistor State** | Permanently **OFF** (no current flows) | Permanently **ON** (current always flows) |
| **Circuit Impact** | Dynamic charge retention converts combinational circuit into sequential memory | Pull-up and pull-down networks conduct simultaneously, causing high static current |
| **Testing Approach** | Requires a **two-pattern test sequence** (Initialization vector $T_1$, then test vector $T_2$) | Readily detected using **$I_{DDQ}$ current testing** (static supply current measurement) |
