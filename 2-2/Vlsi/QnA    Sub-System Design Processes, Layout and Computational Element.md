
### **Problems in Large VLSI Systems**

#### 1. & 2. "What are the problems associated with VLSI design? Draw the basic digital processor structure." (Page 10, Q.6(a); Page 13, Q.5(c))

**Answer:**
- **Problems in Large VLSI Design:**
  1. **Interconnect & RC Delay:** Wire resistance and capacitance dominate gate delay ($RC \propto L^2$), making wiring the primary speed bottleneck.
  2. **High Power Dissipation:** Increased clock frequency and billions of switching transistors lead to extreme heat density and thermal management issues.
  3. **Clock Skew & Synchronization:** Distributing high-frequency clock signals uniformly across large silicon dies without timing skew is difficult.
  4. **Design Complexity & Verification:** Layout errors, test generation costs, and simulation time scale non-linearly with transistor count.
  5. **Routing Congestion & Silicon Area:** Wires consume up to 70-80% of chip area, reducing active transistor density.

- **Basic Digital Processor Structure:**
```
+-------------------------------------------------------------+
|                      Control Unit (FSM)                     |
+-------------------------------------------------------------+
          | Control Signals                 ^ Status / Flags
          v                                 |
+-------------------------------------------------------------+
|                  Data Path Sub-System                       |
|  +--------------------+      +---------------------------+  |
|  | Register File (RF) |<---->| Arithmetic Logic Unit(ALU)|  |
|  +--------------------+      +---------------------------+  |
|          ^                                 ^                |
|          |         System Buses            |                |
|          v      (Data / Address / Control) v                |
+-------------------------------------------------------------+
                               ^
                               v
+-------------------------------------------------------------+
|                    Memory Sub-System                        |
|                     (SRAM / Cache)                          |
+-------------------------------------------------------------+
```
- Consists of:
  - **Data Path:** Registers, ALUs, Shifters, and Multipliers for data manipulation.
  - **Control Unit:** Decodes instructions and issues timed control signals.
  - **Buses:** Parallel communication channels between registers, ALU, and Memory.
  - **Memory:** On-chip caches and registers storing instructions and operands.

---

#### 3. "Explain the problems, requirements and corresponding remedy of a Crossbar switch." (Page 24, CT-03, Q.3)

**Answer:**
- **What is a Crossbar Switch?**
  - An $N \times M$ grid connecting $N$ inputs to $M$ outputs with a switch at every intersection.
- **Problems:**
  1. **$N^2$ Hardware Complexity:** An $N$-bit crossbar requires $N^2$ individual switches (e.g., $16 \times 16 = 256$ switches).
  2. **Severe Capacitive Loading:** Each input line and output line is loaded by $N$ switch capacitances, resulting in slow switching speeds.
  3. **Wiring Congestion:** Massive layout area is consumed purely by cross-connecting metal tracks.
- **Requirements:**
  - Fast arbitrary bit-shifting and rotation without routing blockage or multi-stage delays.
- **Remedy: The Barrel Shifter:**
  - A barrel shifter connects $N$ inputs to $N$ outputs with only $N$ control lines and a single transistor delay per bit, reducing area, capacitance, and delay to $O(N)$.

---

### **Basic Bus Architectures**

#### 4. & 17. "Draw the two bus and three bus basic structures with necessary explanations. / Operating principle of one bus, two bus and three bus architecture." (Page 6, Q.4(c); Page 12, Q.7(a))

**Answer:**
- **One-Bus Architecture:**
  - A single shared global bus connects Registers, ALU inputs, and ALU output.
  - *Operation:* Highly serial. To add two numbers ($R_1 + R_2 \to R_3$), requires 3 sequential clock cycles: Cycle 1 transfers $R_1 \to \text{Temp}_A$; Cycle 2 transfers $R_2 \to \text{Temp}_B$; Cycle 3 transfers ALU Result $\to R_3$.
  - *Trade-off:* Minimum routing area, slowest throughput.
- **Two-Bus Architecture:**
  - Uses two shared buses (Bus A and Bus B).
  - *Operation:* Both operand registers ($R_1$ and $R_2$) output onto Bus A and Bus B simultaneously during Cycle 1. The ALU computes and places the result onto Bus A in Cycle 2 to be latched into destination $R_3$.
  - *Trade-off:* Intermediate area and execution speed (2 clock cycles per ALU operation).
- **Three-Bus Architecture:**
  - Uses two dedicated source source buses (Bus A and Bus B) and one dedicated destination bus (Bus C).
  - *Operation:* Complete ALU operations execute in **a single clock cycle**:
    - Bus A feeds Operand 1 directly into ALU Input 1.
    - Bus B feeds Operand 2 directly into ALU Input 2.
    - Bus C immediately routes the ALU output back to the destination register.
  - *Trade-off:* Maximum speed and throughput; consumes highest wiring area.

---

### **4-Bit Shifter & 4x4 Barrel Shifter**

![[attachments/barrel_shifter_4x4.png]]

#### 5., 7., 8., 9., 10., 11., 12., 13., 14. & 15. "Design/draw a 4-bit and 4x4 barrel shifter... Why barrel shifter is preferred over crossbar switch?" (Pages 3, 5, 10, 12, 19, 23, 27, 28)

![[attachments/Pasted image 20261029170637.png]]

**Answer:**
- **Operating Principle of 4x4 Barrel Shifter:**
  - Consists of a 2D cross-bar matrix of 4 horizontal input data lines ($In_3, In_2, In_1, In_0$) and 4 vertical output data lines ($Out_3, Out_2, Out_1, Out_0$).
  - At diagonal grid crossings, single MOS pass-transistors connect inputs to outputs.
  - Four shift control lines ($sh_0, sh_1, sh_2, sh_3$) run diagonally.
  - **Only one shift control line is activated HIGH at any given time ($O(1)$ single-transistor propagation delay):**
    - $sh_0 = 1 \implies$ Zero shift (Output = Input): $Out_i = In_i$.
    - $sh_1 = 1 \implies$ 1-bit circular shift: $Out_3 \gets In_2,\; Out_2 \gets In_1,\; Out_1 \gets In_0,\; Out_0 \gets In_3$.
    - $sh_2 = 1 \implies$ 2-bit circular shift: $Out_3 \gets In_1,\; Out_2 \gets In_0,\; Out_1 \gets In_3,\; Out_0 \gets In_2$.
    - $sh_3 = 1 \implies$ 3-bit circular shift (or 1-bit right circular shift): $Out_3 \gets In_0,\; Out_2 \gets In_3,\; Out_1 \gets In_2,\; Out_0 \gets In_1$.

- **Exam-Specific Case Solutions:**
  1. **Case: Initial Bits `0110`, Shifted Bits `1001` (Page 5, Q.5(b) - Figure Involved):**
     - Initial bit vector: $(In_3, In_2, In_1, In_0) = (0, 1, 1, 0)$.
     - Desired shifted vector: $(Out_3, Out_2, Out_1, Out_0) = (1, 0, 0, 1)$.
     - Mapping analysis:
       $$Out_3 = 1 = In_1, \quad Out_2 = 0 = In_0, \quad Out_1 = 0 = In_3, \quad Out_0 = 1 = In_2$$
     - This is a **2-bit circular shift (rotate by 2 bits)**:
       $$\mathbf{sh_2 = 1 \quad (\text{with } sh_0 = sh_1 = sh_3 = 0)}$$
  2. **Case: Initial Bits `1101`, Shifted Bits `0111` (Page 27, CT-03, Q.3):**
     - Initial: $(In_3, In_2, In_1, In_0) = (1, 1, 0, 1)$.
     - Desired shifted vector: $(Out_3, Out_2, Out_1, Out_0) = (0, 1, 1, 1)$.
     - Mapping: $Out_3 = In_1 (0)$, $Out_2 = In_0 (1)$, $Out_1 = In_3 (1)$, $Out_0 = In_2 (1)$.
     - This is identically obtained by activating **$sh_2 = 1$**.
  3. **Case: Input `ACDB` $\to$ Output `BACD` (Page 28, CT-03, Q.1):**
     - Input: $(In_3, In_2, In_1, In_0) = (A, C, D, B)$.
     - Output: $(Out_3, Out_2, Out_1, Out_0) = (B, A, C, D)$.
     - Mapping: $Out_3 = In_0 (B)$, $Out_2 = In_3 (A)$, $Out_1 = In_2 (C)$, $Out_0 = In_1 (D)$.
     - This is a 1-bit circular right shift (or 3-bit circular left shift): activated by **$sh_3 = 1$** (or $sh_1$ right-shift line).

- **Why Barrel Shifter is Preferred Over Crossbar Switch:**

| Metric | Crossbar Switch | Barrel Shifter |
| :--- | :--- | :--- |
| **Switch Count** | $N^2$ switches | $N \times N$ matrix with only $N$ pass switches active |
| **Propagation Delay** | Multi-stage cascading delay ($O(N)$ or $O(N^2)$) | **Single MOS transistor delay ($O(1)$)** |
| **Control Complexity** | Requires $N^2$ independent control lines | Requires only $N$ decoded shift control lines |
| **Layout Regularity** | Low, irregular cross-wiring | Extremely high, compact standard repetitive cell |

---

### **Regularity in VLSI Systems**

#### 16. & 18. "What do you mean by regularity in VLSI system? What is the value of regularity of a 16x16 barrel shifter diagram? Define regularity. Draw Manchester carry-chain element." (Page 6, Q.5(b); Page 12, Q.7(a); Page 27, CT-04, Q.2)

**Answer:**
- **Definition of Regularity ($R$):**
  - Regularity is the ratio of the total number of transistors in a VLSI circuit to the number of uniquely designed (manually drawn) transistors:
    $$R = \frac{\text{Total Number of Transistors on Chip}}{\text{Number of Uniquely Hand-Drawn Transistors}}$$
  - High regularity minimizes design time, verification errors, and engineering cost by reusing standard modular leaf cells.
- **Regularity of a 16x16 Barrel Shifter:**
  - A 16x16 barrel shifter contains $16 \times 16 = 256$ pass transistors in total.
  - The entire array is constructed by tiling a single 1-transistor cross-point cell ($1$ unique cell):
    $$R = \frac{256}{1} = 256 \quad (\text{or per-column regularity } R = 16)$$

---

### **Design of an ALU Sub-System**

#### 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29. & 30. "Design of an ALU sub-system / Prove adder circuit can be used as ALU..." (Pages 3, 5, 8, 10, 12, 23, 25, 28)

**Answer:**
- **What is an ALU?**
  - The central arithmetic and logic execution block of a microprocessor.
  - **Operations Performed:**
    - *Arithmetic:* ADD, SUB (Add with 2's complement), INCREMENT, DECREMENT.
    - *Logical:* AND, OR, XOR, XNOR, NOT, Pass $A$, Pass $B$.
- **Proving an Adder Can Be Used as an ALU:**
  - A full adder computes:
    $$Sum = A \oplus B \oplus C_{in}$$
    $$C_{out} = AB + C_{in}(A \oplus B)$$
  - By placing a combinational conditioning logic block (MUX or function select logic) in front of inputs $A$, $B$, and $C_{in}$, we configure the adder to perform any logical or arithmetic operation:
    1. **XOR Operation:** Set $C_{in} = 0$, input $A$ and $B \implies Sum = A \oplus B \oplus 0 = A \oplus B$.
    2. **XNOR Operation:** Set $C_{in} = 1$, input $A$ and $B \implies Sum = A \oplus B \oplus 1 = \overline{A \oplus B}$.
    3. **AND Operation:** $C_{out}$ with $C_{in} = 0 \implies C_{out} = A \cdot B$.
    4. **OR Operation:** By De Morgan's on Carry or configuring input conditioning.
    5. **Addition:** Set $C_{in} = 0$, inputs $A$ and $B \implies A + B$.
    6. **Subtraction:** Invert $B$ ($\bar{B}$) and set $C_{in} = 1 \implies A + \bar{B} + 1 = A - B$ (2's complement).
- **Role of Multiplexers (MUX) in ALU:**
  - Selects which operation (Add, Sub, AND, OR, XOR) is routed to the final output based on the control code ($OP\_CODE$).
  - Selects whether input $B$ passes directly or inverted for subtraction.

---

### **Adder Architectures & Carry Chains**

![[attachments/manchester_carry_chain.png]]

#### 31., 32., 33., 34., 37., 38., 39., 40., 41. & 42. "Design an adder element based on pass/generate concept. Manchester Carry Chain. Carry Lookahead Adder." (Pages 5, 8, 9, 12, 19, 25, 26)

**Answer:**
1. **Pass / Generate Concept:**
   - For bit stage $i$ with inputs $A_i, B_i$:
     - **Generate ($G_i$):** $G_i = A_i \cdot B_i$ (Stage produces a carry-out unconditionally).
     - **Propagate ($P_i$):** $P_i = A_i \oplus B_i$ (Stage passes carry-in directly to carry-out).
     - **Kill / Delete ($K_i$):** $K_i = \overline{A_i} \cdot \overline{B_i}$ (Stage absorbs carry; $C_{out} = 0$).

2. **Manchester Carry Chain (MCC):**
   - **Operation:**
     - Dynamic 2-phase clocking ($\phi_1, \phi_2$).
     - *Phase 1 (Precharge):* PMOS transistor precharges carry line nodes HIGH ($\overline{C_i} = 1$).
     - *Phase 2 (Evaluate):*
       - If $G_i = 1$, NMOS pull-down discharges carry line to Ground (Generates carry, $\overline{C_{i+1}} = 0$).
       - If $P_i = 1$, NMOS pass transistor turns ON, propagating carry state from previous stage.
   - **Problems Associated with MCC:**
     - *RC Delay Scaling:* Series NMOS pass transistors form a distributed RC ladder where delay increases quadratically: $\tau \propto n^2$ ($n$ = number of stages).
     - *Charge Sharing & Threshold Loss:* Degrades signal levels along the chain.
   - **Remedies:**
     - Insert restoring inverters/buffers every 3 to 4 stages to isolate RC delay ($\tau \propto n$ instead of $n^2$).

3. **Carry Lookahead Adder (CLA):**
   - Eliminates ripple carry propagation by computing all carry signals in parallel:
     $$C_1 = G_0 + P_0 C_0$$
     $$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
     $$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
     $$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
   - **Speed vs Area Trade-Off:**
     - *Ripple Carry Adder (RCA):* Smallest area ($O(N)$), slowest delay ($O(N)$).
     - *Carry Lookahead Adder (CLA):* Highest speed ($O(\log N)$ delay), higher silicon area and high fan-in gate complexity ($O(N \log N)$ area).

4. **Full Adder Implementation Using nMOS Pass Transistors:**
   - Uses multiplexer-based pass transistor logic:
     - 1 pass gate network computes $P = A \oplus B$.
     - 2nd stage computes $Sum = P \oplus C_{in}$ and $C_{out} = P \cdot C_{in} + \bar{P} \cdot A$.
   - Uses only 10 to 14 transistors compared to 28 transistors in conventional static CMOS.

---

### **Serial-Parallel Multipliers**

#### 43., 44., 45., 46., 47., 48. & 49. "Serial-parallel multipliers: 3-bit, 4-bit, 5x3 bit, systolic array multiplier, role of D-FF." (Pages 3, 5, 13, 23, 24, 25, 26)

**Answer:**
- **Serial-Parallel Multiplier Working Principle:**
  - Multiplies an $M$-bit parallel word $A = (A_{M-1} \dots A_0)$ by an $N$-bit serial bitstream $X = (X_0, X_1, \dots)$.
  - In each clock cycle:
    1. One bit of the serial multiplier $X_k$ enters the circuit.
    2. An array of AND gates forms partial products $P_i = A_i \cdot X_k$.
    3. Full adders add current partial products to accumulated running partial sums.
    4. Carry bits and running sum bits are latched and shifted right.
- **Purpose of D Flip-Flops:**
  - Acts as pipeline storage elements to hold carry and partial sum bits between successive clock cycles.
  - Guarantees race-free synchronization and prevents clock skew hazards.
- **Systolic Array Multiplier (Pipelined Array):**
  - A 2D regular matrix of identical Processing Elements (PEs), each containing a 1-bit full adder, AND gate, and latches.
  - Data flows synchronously along row and column channels in a rhythmic ("systolic") beat, achieving high clock throughput ($O(1)$ cycle time regardless of bit length).

---

### **System Timing & Transit Time Considerations**

#### 50., 51., 52. & 53. "If max carrier drift velocity is $1 \times 10^7$ cm/s and depletion width is $10^{-1}\,\mu$m. Calculate transit time ($\tau$) and mobility. Inverter pair delay." (Pages 2, 16, 27)

![[attachments/Pasted image 20261029165902.png]]

**Answer:**
1. **Transit Time ($\tau$) Calculation:**
   - Formula:
     $$\tau = \frac{L}{v_d}$$
   - Given:
     - Drift velocity $v_d = 1 \times 10^7\text{ cm/s} = 10^5\text{ m/s}$
     - Channel length / depletion width $L = 10^{-1}\,\mu\text{m} = 0.1\,\mu\text{m} = 10^{-7}\text{ m} = 10^{-5}\text{ cm}$
   - Calculation:
     $$\tau = \frac{10^{-5}\text{ cm}}{1 \times 10^7\text{ cm/s}} = 10^{-12}\text{ s} = 1\text{ ps} \quad (0.001\text{ ns})$$

2. **Mobility ($\mu$) Per Unit Electric Field:**
   - Velocity $v_d = \mu E \implies \mu = \frac{v_d}{E}$.
   - Electric field $E = \frac{V}{L}$. Effective mobility $\mu = \frac{v_d}{E}$.

3. **Inverter Pair Delay Calculation (Page 16, Q.3(a) & Q.4(b) - from Figure):**
   - Transistor dimensions:
     - Pull-up transistors: $L:W = 1:1 \implies R_{pu} = 1\,R_s$
     - Pull-down transistors: $L:W = 1:4 \implies R_{pd} = 0.25\,R_s$; Gate capacitance $C_g = 4\Box C_g$.
   - Inter-stage load capacitance: $C_{out1} = 4\Box C_g$ (gate of Stage 2 pull-down), and load $C_{out2} = 4\Box C_g$.
   - **Pair Delay:**
     $$\tau_{pair} = \tau_{pd1} + \tau_{pu2} = (0.25\,R_s \times 4\Box C_g) + (1\,R_s \times 4\Box C_g) = 1\tau + 4\tau = \mathbf{5\tau}$$
   - With textbook standard transit time $\tau = 0.1\text{ ns}$:
     $$\tau_{pair} = 5 \times 0.1\text{ ns} = \mathbf{0.5\text{ ns}}$$

---

### **Memory Cells & Dynamic Register Elements**

![[attachments/dram_1t_cell.png]]
![[attachments/dram_3t_cell.png]]

#### 54., 55., 56. & 57. "Dynamic register element, 3-bit dynamic shift register. Why dynamic? Power dissipation math." (Pages 4, 12, 23, 26)

**Answer:**
- **Dynamic Register Element:**
  - Stores a bit dynamically as electrostatic charge on the parasitic gate capacitance ($C_g$) of an MOS transistor instead of a bistable feedback latch.
  - **Why called 'dynamic'?**
    - The stored charge leaks away over time (due to reverse junction leakage and subthreshold current).
    - It must be refreshed periodically ($< 1\text{ ms}$) to prevent data loss.
- **Pseudo-Static RAM / Register Cell:**
  - Uses cross-coupled inverters with weak feedback or clocked pass-gates ($\phi_1, \phi_2$) to periodically refresh stored charge, retaining data indefinitely as long as the clock runs.
- **3-Transistor vs 3-Bit Dynamic Shift Register:**
  - A **3-Transistor (3T) Cell** stores **1 bit** in RAM using 3 transistors (Read, Write, and Storage).
  - A **3-Bit Dynamic Shift Register** stores **3 sequential bits** across 3 cascaded master-slave stages (requires $3 \times 4 = 12$ to 18 transistors clocked by non-overlapping $\phi_1, \phi_2$).

---

#### 58., 59., 60., 61., 62., 63., 64., 65., 66., 67. & 68. "3T vs 1T DRAM cells. Operation, chip size calculations for 15k, 20k, 25k bits." (Pages 3, 6, 8, 10, 12, 13, 19, 24, 25)

**Answer:**
- **Comparison: 1T vs 3T DRAM Cells:**

| Metric | 1-Transistor (1T) DRAM | 3-Transistor (3T) DRAM |
| :--- | :--- | :--- |
| **Cell Area** | Smallest ($\approx 20 \text{ to } 50 \, \lambda^2$) | Moderate ($\approx 500 \text{ to } 1200 \, \lambda^2$) |
| **Transistor Count** | 1 Access Transistor + 1 Trench/Stack Cap | 3 MOS Transistors ($T_1$ Write, $T_2$ Store, $T_3$ Read) |
| **Read Process** | **Destructive Read** (Charge sharing requires write-back) | **Non-Destructive Read** ($T_2$ gate modulates current) |
| **Sense Amplifier** | Highly sensitive differential sense amplifier needed | Simple single-ended sense amplifier |
| **Volatility** | Dynamic (Needs periodic refresh) | Dynamic (Needs periodic refresh) |

- **Chip Size Calculation Examples:**
  1. **Accommodate bits on a $4\text{ mm} \times 4\text{ mm}$ chip with $500\lambda^2$ cell area ($\lambda = 1\,\mu\text{m}$):**
     - Chip Area $= 4\text{ mm} \times 4\text{ mm} = 16\text{ mm}^2 = 1.6 \times 10^7\,\mu\text{m}^2$.
     - Cell Area $= 500 \times (1\,\mu\text{m})^2 = 500\,\mu\text{m}^2$.
     - Maximum Bits $= \frac{1.6 \times 10^7}{500} = 32,000\text{ bits} = 32\text{ kbits}$.
  2. **Chip size for 20 kbits in 1T DRAM ($50\lambda^2$ per cell, $\lambda = 1\,\mu\text{m}$):**
     $$\text{Area} = 20,000 \times 50 \times (1\,\mu\text{m})^2 = 1.0 \times 10^6\,\mu\text{m}^2 = 1.0\text{ mm}^2$$
  3. **Chip size for 15 kbits in 3T DRAM ($600\lambda^2$) vs 1T DRAM ($50\lambda^2$):**
     - $3\text{T DRAM Area} = 15,000 \times 600\lambda^2 = 9.0 \times 10^6\,\lambda^2$.
     - $1\text{T DRAM Area} = 15,000 \times 50\lambda^2 = 7.5 \times 10^5\,\lambda^2$ ($12\times$ smaller!).

---

### **Dynamic and Static Flip-Flops & Latches**

![[attachments/sram_6t_cell.png]]

#### 69. & 70. "Differences between latches and flip-flops? Sketch 4:1 MUX. Differentiate dynamic and static flip-flops." (Page 12, Q.3(b); Page 13, Q.7(c))

**Answer:**
- **Latches vs Flip-Flops:**

| Feature | Latch | Flip-Flop |
| :--- | :--- | :--- |
| **Clock Triggering** | **Level-sensitive** (transparent while clock is HIGH or LOW) | **Edge-triggered** (samples data on clock rising or falling edge) |
| **Structure** | Single bistable element or pair of cross-coupled gates | Master-Slave configuration (two latches in series) |
| **Timing Hazards** | Prone to race-around conditions when clock pulse is wide | Eliminates race-around conditions; robust synchronous timing |

- **Dynamic vs Static Flip-Flops:**

| Feature | Static Flip-Flop | Dynamic Flip-Flop |
| :--- | :--- | :--- |
| **Storage Mechanism** | Cross-coupled inverter feedback loop (bistable) | Parasitic gate capacitance ($C_g$) of MOS transistors |
| **Clock Frequency Limit** | Operates down to DC (zero clock frequency) | Minimum clock frequency required ($> 1\text{ kHz}$) to prevent charge leakage |
| **Transistor Count** | Higher ($12 \text{ to } 16$ transistors) | Lower ($6 \text{ to } 8$ transistors) |
| **Power Consumption** | Higher gate count, static leakage only | Lower clock load, zero static leakage |
