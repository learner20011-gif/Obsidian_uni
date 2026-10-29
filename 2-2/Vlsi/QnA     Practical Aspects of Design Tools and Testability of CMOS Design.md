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
![[attachments/Pasted image 20261029165824.png]]

**Answer:**
- **Standard Unit Conventions (nMOS Depletion-Load Model):**
  - Minimum standard transistor ($2\lambda \times 2\lambda$) has channel sheet resistance $1\,R_s$ and unit gate capacitance $C_{IN0} = 1\Box C_g$.
  - Basic transit time: $\tau = 1\,R_s \times 1\Box C_g$.
  - Transistor channel resistance: $R = \left(\frac{L}{W}\right) R_s$.
  - Transistor gate capacitance: $C_g = \left(\frac{L \times W}{2\lambda \times 2\lambda}\right)\Box C_g = \left(\frac{L \cdot W}{4}\right)\Box C_g$ (for dimensions in $\lambda$).

- **Case (i):**
  1. **Previous Stage Channel Resistances:**
     - Pull-up ($\text{p.u} = 16 \times 2$): $R_{pu1} = \frac{16}{2}\,R_s = 8\,R_s$
     - Pull-down ($\text{p.d} = 2 \times 2$): $R_{pd1} = \frac{2}{2}\,R_s = 1\,R_s$
  2. **Capacitance at Output Node:**
     - Next stage pull-down ($\text{p.d} = 8 \times 2$): $C_{g2} = \frac{8 \times 2}{4}\Box C_g = 4\Box C_g$.
     - Stray capacitance given: $C_S = 6\Box C_g$.
     - Total load capacitance: $C_{total} = C_S + C_{g2} = 6\Box C_g + 4\Box C_g = 10\Box C_g$.
  3. **Transition Delay Calculations:**
     - **Pull-up Transition Delay (charging load via pull-up):**
       $$\tau_{pu} = R_{pu1} \times C_{total} = 8\,R_s \times 10\Box C_g = \mathbf{80\tau}$$
     - **Pull-down Transition Delay (discharging load via pull-down):**
       $$\tau_{pd} = R_{pd1} \times C_{total} = 1\,R_s \times 10\Box C_g = \mathbf{10\tau}$$
     - *(Note: If taking $C_{IN} = 1\Box C_g$ directly without area scaling, $C_{total} = 6 + 1 = 7\Box C_g \implies \tau_{pu} = 8 \times 7 = 56\tau$, $\tau_{pd} = 7\tau$.)*

- **Case (ii):**
  1. **Previous Stage Channel Resistances:**
     - Pull-up ($\text{p.u} = 16 \times 2$): $R_{pu1} = \frac{16}{2}\,R_s = 8\,R_s$
     - Pull-down ($\text{p.d} = 2 \times 2$): $R_{pd1} = \frac{2}{2}\,R_s = 1\,R_s$
  2. **Capacitance at Output Node:**
     - Next stage pull-down ($\text{p.d} = 2 \times 8$): $C_{g2} = \frac{2 \times 8}{4}\Box C_g = 4\Box C_g$.
     - Stray capacitance given: $C_S = 5\Box C_g$.
     - Total load capacitance: $C_{total} = C_S + C_{g2} = 5\Box C_g + 4\Box C_g = 9\Box C_g$.
  3. **Transition Delay Calculations:**
     - **Pull-up Transition Delay (charging load via pull-up):**
       $$\tau_{pu} = R_{pu1} \times C_{total} = 8\,R_s \times 9\Box C_g = \mathbf{72\tau}$$
     - **Pull-down Transition Delay (discharging load via pull-down):**
       $$\tau_{pd} = R_{pd1} \times C_{total} = 1\,R_s \times 9\Box C_g = \mathbf{9\tau}$$
     - *(Note: If taking $C_{IN} = 1\Box C_g$ directly without area scaling, $C_{total} = 5 + 1 = 6\Box C_g \implies \tau_{pu} = 8 \times 6 = 48\tau$, $\tau_{pd} = 6\tau$. Case (ii) achieves $16\times$ lower Next-stage pull-down resistance $R_{pd2} = \frac{2}{8}R_s = 0.25\,R_s$ vs $4\,R_s$ in Case (i) for the exact same input load capacitance $4\Box C_g$.)*

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

![[attachments/Pasted image 20261029165902.png]]

**Answer:**
- **Inverter Delay Definition:**
  - The time elapsed between the 50% transition of the input voltage and the corresponding 50% transition of the output voltage of a single inverter stage:
    $$\tau_{inv} = \frac{\tau_{pHL} + \tau_{pLH}}{2}$$
- **nMOS Inverter Pair Delay Calculation from Figure:**
  1. **Circuit Parameters from Figure:**
     - Both Stage 1 and Stage 2 have:
       - Depletion pull-up transistor labeled **$1:1$** ($L:W = 1:1 \implies Z_{pu} = 1$).
         $$R_{pu} = 1\,R_s$$
       - Enhancement pull-down transistor labeled **$1:4$** ($L:W = 1:4 \implies Z_{pd} = 1/4 = 0.25$).
         $$R_{pd} = 0.25\,R_s$$
         $$Z_{pu} / Z_{pd} = \frac{1}{0.25} = 4:1 \text{ (standard } 4:1 \text{ inverter ratio)}$$
     - Gate capacitance of the $1:4$ pull-down ($L=2\lambda, W=8\lambda$):
       $$C_{g,pd} = \frac{2\lambda \times 8\lambda}{2\lambda \times 2\lambda}\Box C_g = 4\Box C_g$$
  2. **Inter-stage Load Capacitance ($C_{out1}$):**
     - Output of Stage 1 drives the gate of Stage 2 pull-down: $C_{out1} = 4\Box C_g$.
     - Similarly, assuming Stage 2 drives an identical subsequent stage ($C_{out2} = 4\Box C_g$):
  3. **Pair Delay ($\tau_{pair}$):**
     - When $V_{in}$ steps $0 \to 1$: Stage 1 pulls down $C_{out1}$, then Stage 2 pulls up $C_{out2}$:
       $$\tau_{pd1} = R_{pd1} \times C_{out1} = 0.25\,R_s \times 4\Box C_g = 1\tau$$
       $$\tau_{pu2} = R_{pu2} \times C_{out2} = 1\,R_s \times 4\Box C_g = 4\tau$$
       $$\tau_{pair} = \tau_{pd1} + \tau_{pu2} = 1\tau + 4\tau = \mathbf{5\tau}$$
     - When $V_{in}$ steps $1 \to 0$: Stage 1 pulls up ($4\tau$) and Stage 2 pulls down ($1\tau$), yielding the exact same:
       $$\tau_{pair} = 4\tau + 1\tau = \mathbf{5\tau}$$
  4. **Pair Delay in Nanoseconds (ns):**
     - Using standard $5\,\mu\text{m}$ ($\lambda = 2.5\,\mu\text{m}$) nMOS textbook transit time $\tau = 0.1\text{ ns}$:
       $$\tau_{pair} = 5 \times 0.1\text{ ns} = \mathbf{0.5\text{ ns}}$$
     - *(Note: In practical layout including stray routing capacitance where $\tau \approx 0.2\text{ ns}$, $\tau_{pair} = 5 \times 0.2\text{ ns} = 1.0\text{ ns}$. If $C_{out2}$ is a single $1\Box C_g$ gate, $\tau_{pair} = 1\tau + 1\tau = 2\tau = 0.2\text{ ns}$.)*

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
![[attachments/Pasted image 20261029170014.png]]
![[attachments/cif_primitives_q9.png]]

**Answer:**
From the given table:
| Primitive | (L) | (W) | (C) Center | (D) Direction |
| :--- | :---: | :---: | :---: | :---: |
| **$B_1$** | 50 | 30 | (20, 25) | NA |
| **$B_2$** | 40 | 20 | (50, 70) | (-30, 30) |
| **Wire** | 12 | 70 90 | 95 90 | 95 80 |

1. **Box $B_1$ (Unrotated Box):**
   - **CIF Command:** `B 50 30 20 25;`
   - **Center:** $C = (20, 25)$, Length $L = 50$ (along $X$), Width $W = 30$ (along $Y$).
   - **Bounding Extents:**
     - $X \in [20 - 25, 20 + 25] = [-5, 45]$
     - $Y \in [25 - 15, 25 + 15] = [10, 40]$
   - **Corner Vertices:** $(-5, 10)$, $(45, 10)$, $(45, 40)$, $(-5, 40)$.

2. **Box $B_2$ (Rotated Box):**
   - **CIF Command:** `B 40 20 50 70 -30 30;`
   - **Center:** $C = (50, 70)$, Length $L = 40$, Width $W = 20$.
   - **Direction Vector:** $D = (-30, 30) \implies \theta = \text{atan2}(30, -30) = 135^\circ$ ($45^\circ$ diagonal tilt into Quadrant II).
   - **Unit Vectors:**
     $$\hat{u}_L = \left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right), \qquad \hat{u}_W = \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$$
   - **Vertices ($C \pm 20\,\hat{u}_L \pm 10\,\hat{u}_W$):**
     1. $(50 - 15\sqrt{2}, 70 + 5\sqrt{2}) \approx (28.79, 77.07)$
     2. $(50 - 5\sqrt{2}, 70 + 15\sqrt{2}) \approx (42.93, 91.21)$
     3. $(50 + 15\sqrt{2}, 70 - 5\sqrt{2}) \approx (71.21, 62.93)$
     4. $(50 + 5\sqrt{2}, 70 - 15\sqrt{2}) \approx (57.07, 48.79)$

3. **Wire:**
   - **CIF Command:** `W 12 70 90 95 90 95 80;`
   - **Width:** $W = 12$ (extends $\pm 6$ units on each side of centerline with radius $R = 6$ rounded/extended end caps).
   - **Centerline Path:** $(70, 90) \longrightarrow (95, 90) \longrightarrow (95, 80)$.
   - Forms an L-shaped track starting at $(70, 90)$, travelling horizontally $25$ units to $(95, 90)$, and turning downward $10$ units to $(95, 80)$.

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

**The 3 Stages of Sensitized Path Method:**
1. **Stage 1 (Fault Activation / Excitation):** Apply inputs to drive the target node to the value opposite to the stuck fault (set to `0` for SA1, set to `1` for SA0).
2. **Stage 2 (Fault Propagation):** Establish a sensitized path to a primary output by holding side inputs of gates along the path to non-controlling values (AND/NAND $\to 1$, OR/NOR $\to 0$).
3. **Stage 3 (Line Justification):** Backtrack to find primary inputs satisfying all required internal states without contradiction. If a contradiction arises, the fault is **undetectable (redundant)**.

---

#### 13. "Construct the test vectors for z: SA1 in the following Fig. and explain in details using path sensitized model. [figure Involved]" (Page 3, Q.6(b))

![[attachments/Pasted image 20261029170044.png]]

**Answer:**
- **Circuit Analysis:**
  - Top gate: 2-input AND gate with inputs $A$ and upper branch of $B$ (labeled $z$). Output $G_1 = A \cdot z$.
  - Bottom gates: 2-input NAND gate (inputs $B, C$) followed by an Inverter. Output $G_3 = \overline{\overline{BC}} = BC$.
  - Output gate: 2-input NOR gate. Output $F = \overline{G_1 + G_3} = \overline{Az + BC}$.
  - Target fault: **$z : \text{SA1}$** (upper branch of $B$ feeding the AND gate is stuck-at-1).

- **Step-by-Step Sensitized Path Method:**
  1. **Fault Activation:**
     - To activate $z : \text{SA1}$, drive $z = 0$.
     - Since $z$ originates from input $B$, set **$B = 0$**. Line $z$ carries $0/1$ ($0$ in good circuit, $1$ in faulty circuit).
  2. **Fault Propagation:**
     - To propagate through the top AND gate ($G_1$): set side input **$A = 1$** (non-controlling value for AND).
       $$G_1 = 1 \cdot (0/1) = 0/1$$
     - To propagate $G_1 = 0/1$ through the output NOR gate ($F$): set side input $G_3 = 0$ (non-controlling value for NOR).
       $$F = \overline{G_1 + 0} = \overline{0/1} = 1/0 \quad (\text{Good } F=1, \text{Faulty } F=0)$$
  3. **Line Justification:**
     - We require $G_3 = 0$ at the inverter output $\implies$ NAND gate output $G_2 = 1$.
     - NAND gate inputs are $B$ and $C$: $G_2 = \overline{B \cdot C}$.
     - Since we already set **$B = 0$** during fault activation, $G_2 = \overline{0 \cdot C} = 1$ is **satisfied for any value of $C$** ($C = X$, don't care)!
     - No contradictions occur.

- **Resulting Test Vectors:**
  - $(A, B, C) = (1, 0, X)$
  - **Test Vectors: `100` and `101`**
  - *Verification:*
    - Fault-free ($B=0$): $G_1 = 1 \cdot 0 = 0$, $G_3 = 0 \cdot C = 0 \implies F = \overline{0 + 0} = \mathbf{1}$.
    - Faulty ($z=1$): $G_1 = 1 \cdot 1 = 1$, $G_3 = 0 \implies F = \overline{1 + 0} = \mathbf{0} \neq 1$ (Detected!).

---

#### 14. "Is it possible to construct test vectors in Fig.8.1 and Fig. 8.2? Find the test vectors using sensitized path based testing. [figure Involved]" (Page 5, Q.8(b))

![[attachments/Pasted image 20261029170122.png]]

**Answer:**
- **Analysis of Fig. 8.1:**
  - Top gate: 2-input AND gate with inputs $A$ and upper branch of $B$ (fault site: **SA0**). Output $G_1 = A \cdot B$.
  - Bottom gate: 2-input NOR gate with inputs $B, C$. Output $G_2 = \overline{B + C}$.
  - Output gate: 2-input NAND gate. Output $F = \overline{G_1 \cdot G_2}$.
  - **Sensitized Path Testing for SA0 on upper branch of $B$:**
    1. *Fault Activation:* Drive upper branch to $1 \implies$ requires **$B = 1$**.
    2. *Fault Propagation:*
       - Through top AND gate: requires side input **$A = 1$** ($G_1 = 1/0$).
       - Through output NAND gate: requires side input $G_2 = 1$ (non-controlling value for NAND).
    3. *Line Justification:*
       - For bottom NOR gate to output $G_2 = 1$, **both** inputs must be $0 \implies$ requires **$B = 0$** and **$C = 0$**.
       - **Contradiction:** Line justification requires $B = 0$, but fault activation requires $B = 1$!
       - *Boolean Verification:* $F = \overline{(AB)\cdot\overline{B+C}} = \overline{AB\overline{B}\overline{C}} = \overline{0} = 1$. The output is permanently $1$ for all inputs regardless of the fault.
    4. **Conclusion for Fig. 8.1:** It is **NOT possible** to construct a test vector. The SA0 fault is **undetectable (redundant)**.

- **Analysis of Fig. 8.2:**
  - Circuit has an Inverter added after the top AND gate: $G_1' = \overline{AB}$.
  - Output NAND gate: $F = \overline{G_1' \cdot G_2} = \overline{\overline{AB}\cdot\overline{B+C}} = AB + B + C = B + C$ (by absorption $B + AB = B$).
  - **Sensitized Path Testing for SA0 on upper branch of $B$:**
    1. *Fault Activation:* Set $B = 1$.
    2. *Fault Propagation:* Top AND requires $A = 1 \implies G_1 = 1/0$; Inverter gives $G_1' = 0/1$. To propagate through output NAND gate, bottom input $G_2$ must be $1$.
    3. *Line Justification:* $G_2 = \overline{B + C} = 1 \implies$ requires $B = 0, C = 0$, directly contradicting $B = 1$!
    4. *Boolean Verification:* Fault-free $F = B + C$; Faulty with upper branch SA0 gives $F_{faulty} = (A \cdot 0) + B + C = B + C \equiv F_{good}$.
    5. **Conclusion for Fig. 8.2:** It is **NOT possible** to construct a test vector for SA0 as drawn (the fault is redundant and **undetectable**).
    - *(Note: If the fault were instead SA1, setting $B = 0, A = 1, C = 0$ gives $G_2 = 1$, enabling propagation to detect SA1 with test vector `ABC = 100`.)*

---

#### 15. "Determine whether the fault below is detectable or undetectable? Explain with proper stages of sensitized path-based testing and test vectors. [figure Involved]" (Page 6, Q.5(a))

![[attachments/Pasted image 20261029170144.png]]

**Answer:**
- **Circuit Identification:**
  - Primary inputs: $A$ (line 1), $B$ (line 2, branches to line 5 & 6), $C$ (line 3), $D$ (line 4).
  - Bottom-left gate: 3-input OR gate with inputs lines 6 ($B$), 3 ($C$), 4 ($D$). Output is line 7 ($L_7 = B + C + D$).
  - Line 7 fans out to: line 9 (input to 3-input AND gate) and line 8 (input to Inverter).
  - Inverter: input line 8, output line 10 ($L_{10} = \overline{L_7}$).
  - Top gate: 3-input AND gate with inputs line 1 ($A$), line 5 ($B$), line 9 ($L_7$). Output is line 11 ($L_{11} = A \cdot B \cdot L_7$).
  - Output gate: 2-input NOR gate. Output $F = \overline{L_{11} + L_{10}}$.
  - Fault: **Line 4 ($D$) is Stuck-at-0 (SA0 Fault)**.

- **Stages of Sensitized Path-Based Testing:**
  1. **Stage 1: Fault Activation:**
     - To activate SA0 on line 4, apply **$D = 1$**. Line 4 carries $1/0$ ($D$).
  2. **Stage 2: Fault Propagation:**
     - *Through 3-input OR gate to line 7:* Side inputs lines 6 and 3 must be non-controlling (`0`):
       $$\text{Line } 6 = 0 \implies \mathbf{B = 0}, \qquad \text{Line } 3 = 0 \implies \mathbf{C = 0}$$
       $$\text{Line } 7 = 0 + 0 + (1/0) = 1/0$$
     - *Path Selection at Fanout (Line 7):*
       - Along upper path (line 9 $\to$ 3-input AND gate): Since we already set **$B = 0$**, input line 5 is $0$. This blocks the AND gate, forcing line 11 permanently to **$0$** ($L_{11} = A \cdot 0 \cdot L_9 = 0$).
       - Along lower path (line 8 $\to$ Inverter $\to$ line 10):
         $$\text{Line } 10 = \overline{1/0} = 0/1$$
       - *Through output NOR gate ($F$):* The side input is line 11 $= 0$ (which is the non-controlling value `0` of a NOR gate!).
         $$F = \overline{L_{11} + L_{10}} = \overline{0 + (0/1)} = 1/0 \quad (\text{Good } F = 1, \text{Faulty } F = 0)$$
  3. **Stage 3: Line Justification:**
     - Requirements on primary inputs:
       - $D = 1$ (activation)
       - $B = 0, C = 0$ (sensitize OR gate; $B=0$ also sensitizes output NOR gate by holding line 11 at 0)
       - $A = X$ (don't care, since line 5 $= 0$ already disables line 11).
     - No contradictions exist!

- **Conclusion:**
  - The fault is **DETECTABLE**.
  - **Sensitized Path:** Line $4 \to$ Line $7 \to$ Line $8 \to$ Line $10 \to$ Output $F$.
  - **Test Vectors:** $(A, B, C, D) = (X, 0, 0, 1)$, giving **`0001`** and **`1001`**.

---

#### 16. "Construct the test vectors for x : SA1 and y : SA1 in following figure and explain in detail using path sensitized model [figure Involved]" (Pages 20 & 21, Q.(c))

![[attachments/Pasted image 20261029170259.png]]

**Answer:**
*(The circuit diagram corresponds to the same topology as Q.13 with inputs $A, B, C$, where $x$ represents the upper fanout branch of $B$ feeding the AND gate, and $y$ represents the lower branch feeding the NAND gate, or the intermediate lines).*

1. **For $x : \text{SA1}$ (Upper branch of $B$ stuck-at-1):**
   - **Activation:** Set $x = 0 \implies \mathbf{B = 0}$. ($x = 0/1$).
   - **Propagation:**
     - Top AND gate: set side input $\mathbf{A = 1}$ (non-controlling for AND) $\implies G_1 = 0/1$.
     - Output NOR gate: set side input $G_3 = 0$ (non-controlling for NOR) $\implies F = \overline{(0/1) + 0} = 1/0$.
   - **Justification:** $G_3 = 0 \implies G_2 = \overline{BC} = 1$. Since $B = 0$, $G_2 = \overline{0 \cdot C} = 1$ holds for any $C$ ($C = X$).
   - **Test Vectors for $x : \text{SA1}$:** **`ABC = 100` and `101`** ($(1, 0, X)$).

2. **For $y : \text{SA1}$ (Lower branch of $B$ stuck-at-1):**
   - **Activation:** Set $y = 0 \implies \mathbf{B = 0}$. ($y = 0/1$).
   - **Propagation:**
     - Bottom NAND gate ($G_2 = \overline{y \cdot C}$): set side input $\mathbf{C = 1}$ (non-controlling for NAND) $\implies G_2 = \overline{(0/1) \cdot 1} = 1/0$.
     - Inverter: $G_3 = \overline{1/0} = 0/1$.
     - Output NOR gate: set side input $G_1 = 0$ (non-controlling for NOR).
   - **Justification:** $G_1 = A \cdot B = A \cdot 0 = 0$, which is already satisfied for any $A$ ($A = X$).
   - **Test Vectors for $y : \text{SA1}$:** **`ABC = 001` and `101`** ($(X, 0, 1)$).

---

#### 17. "1. sensitized path based testing er math -------- 05" (Page 23, CT-04, Q.1)

**Answer:**
Refer to the systematic 3-stage derivation detailed in Questions 13, 14, and 15 above:
1. Drive node to opposite logic level (Fault Activation: `0` for SA1, `1` for SA0).
2. Propagate error $D/\overline{D}$ to primary output by setting along-path side inputs to non-controlling values.
3. Justify internal requirements backwards to primary inputs; confirm consistency or detect contradiction.

---

### **SA0 and SA1 Faults in Combinational Logic Testing**

#### 18. "Determine the test vector for the given circuit in Fig. 7. [figure Involved]" (Page 5, Q.7(b))

![[attachments/Pasted image 20261029170350.png]]

**Answer:**
- **Circuit Analysis of Fig. 7:**
  - Primary inputs: $A$ (1), $B$ (2), $C$ (3), $D$ (4).
  - 3-input OR gate: inputs lines 6 ($B$), 3 ($C$), 4 ($D$). Output line 7 ($L_7 = B + C + D$).
  - Fanout at line 7:
    - **Line 8 (Target fault: `SA1`):** feeds 3-input AND gate.
    - Line 9: feeds Inverter.
  - 3-input AND gate: inputs line 1 ($A$), line 5 ($B$), line 8 ($L_8$). Output is line 10 ($L_{10} = A \cdot B \cdot L_8$).
  - Inverter: input line 9, output is line 11 ($L_{11} = \overline{L_7}$).
  - Output gate: 2-input NOR gate. Output $F = \overline{L_{10} + L_{11}}$.
  - Fault: **Line 8 is Stuck-at-1 (SA1)**.

- **Sensitized Path Analysis for Line 8 SA1:**
  1. **Fault Activation:**
     - To activate Line 8 SA1, drive line 8 to logic `0` $\implies L_7 = B + C + D = 0$.
     - For an OR gate output to be `0`, all its inputs must be `0`:
       $$\mathbf{B = 0, \quad C = 0, \quad D = 0}$$
     - Line 8 carries $0/1$ ($\overline{D}$).
  2. **Fault Propagation:**
     - Line 8 enters the 3-input AND gate.
     - To propagate through the AND gate, side inputs line 1 ($A$) and line 5 ($B$) must both be set to the non-controlling value `1`:
       $$\mathbf{A = 1, \quad B = 1}$$
  3. **Line Justification — Contradiction:**
     - Fault activation **required $B = 0$** (to keep line $7 = 0$).
     - Fault propagation **required $B = 1$** (to enable the AND gate via line 5).
     - Furthermore, with line $7 = 0$, line $9 = 0 \implies$ line 11 (Inverter output) $= 1$, which places a controlling `1` at the output NOR gate, forcing $F = 0$ regardless of line 10.
  4. **Boolean Proof:**
     $$L_{10} = A \cdot B \cdot (B + C + D) = A \cdot B \quad (\text{by Absorption Law } B(B+C+D) = B)$$
     - With line 8 stuck at 1: $L_{10(\text{SA1})} = A \cdot B \cdot 1 = A \cdot B$.
     - Thus $L_{10} \equiv L_{10(\text{SA1})}$ and $F_{good} \equiv F_{SA1}$ for all 16 input combinations!

- **Conclusion:**
  - The fault Line 8 SA1 is **UNDETECTABLE (redundant)**.
  - **No test vector exists** to detect this fault.

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
