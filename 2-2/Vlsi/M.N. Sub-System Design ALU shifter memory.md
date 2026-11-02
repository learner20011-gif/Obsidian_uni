# Topic 4: Shifter, ALU, Memory & Registers
---
## 4A. Barrel Shifter, Crossbar Switch & Regularity
### 1. Crossbar Switch vs. Barrel Shifter
#### Crossbar Switch ($N \times N$ Matrix)
- **Concept:** $N \times N$ array of pass transistors connecting any input line to any output line.
- **Problems:**
  1. **Overkill / Hardware Overhead:** Requires $N^2$ separate switches and $N^2$ independent control lines (16 switches for $4\times 4$).
  2. **Short-Circuit Risk:** If $>1$ switch in any row/column turns ON simultaneously, multiple data inputs short together $\to$ **chip damage!**
  3. **High Capacitive Loading:** Every line crosses $N$ drains/sources $\to$ slow switching speed.
![[attachments/Pasted image 20261030144952.png]]
---
#### Barrel Shifter (The Optimal Remedy)
- **Concept:** Reorganizes switch connections along diagonal patterns driven by $N$ mutually exclusive shift control lines ($sh0, sh1, sh2, \dots$).
- **Advantages over Crossbar:**
  1. **Zero Short-Circuit Danger:** Only ONE shift line is HIGH at any time $\to$ short circuits are physically impossible.
  2. **Minimal Control Lines:** Only $N$ control lines (vs. $N^2$).
  3. **Single-Stage Delay:** Data passes through exactly **ONE** transistor switch regardless of shift distance ($0$ to $N-1$ bits).
  4. **High Layout Regularity:** Single identical switch cell stepped and repeated.
![[attachments/Pasted image 20261030145836.png]]
![[attachments/Pasted image 20261030145848.png]]

| Feature              | Crossbar Switch          | Barrel Shifter       |
| :---                 | :---                     | :---                 |
| Number of Switches   | N^2 (16 for 4x4)         | N^2 (16 for 4x4)     |
| Control Signals      | N^2 individual lines     | N lines (sh0 - sh3)  |
| Control Decoding     | Complex N^2 decoder      | Simple N-line select |
| Risk of Short Circuit| High (accidental overlap)| ZERO (mutually excl.)|
| Signal Delay         | Variable RC              | 1 transistor switch  |
| Shifting Capability  | Arbitrary routing        | Cyclic rotation (0-N)|

---
### 2. $4\times 4$ Barrel Shifter Operations & Transistor Activation

| Control Line | Shift Count | Output Bits (O3, O2, O1, O0)   |
| :---         | :---        | :---                           |
| sh0          | 0 (No shift)| I3, I2, I1, I0                 |
| sh1          | 1 bit right | I0, I3, I2, I1                 |
| sh2          | 2 bits right| I1, I0, I3, I2                 |
| sh3          | 3 bits right| I2, I1, I0, I3                 |

![[attachments/Pasted image 20261030152056.png]]
- **Example 1: Initial $1101 \to$ Shifted $0111$ (Q4.3, Q4.14):**
  - Input: $I_3=1, I_2=1, I_1=0, I_0=1$.
  - Output: $O_3=0, O_2=1, O_1=1, O_0=1$.
  - Shift amount $= 1$ place right ($sh1$ line active) or cyclic permutation.
  - Active transistors: diagonal switches along the $sh1$ control bus ($M_{01}, M_{12}, M_{23}, M_{30}$).
- **Example 2: Initial $0110 \to$ Shifted $1001$ (Q4.10):**
  - Shift $= 3$ places right (or 1 left) $\to sh3$ line active.
- **Example 3: Input ACDB $\to$ Output BACD (Q4.1):**
  - Cyclic rotation by 1 position $\to sh1$ line active.
---
### 3. Regularity in VLSI Systems
$$\mathbf{\text{Regularity} = \frac{\text{Total Number of Transistors on Chip}}{\text{Number of Transistor Circuits Designed in Detail}}}$$
- **Importance:** Measures design productivity. High regularity minimizes engineering design time, DRC/LVS verification overhead, and mask generation errors.
- **$4\times 4$ Barrel Shifter:**
  $$\text{Regularity} = \frac{16\text{ transistors}}{1\text{ basic switch cell}} = \mathbf{16}$$
- **$16\times 16$ Barrel Shifter (Q4.12):**
  $$\text{Regularity} = \frac{16 \times 16}{1} = \mathbf{256}$$
---
## 4B. ALU, Adders & Arithmetic Circuits
### 1. Full Adder as a Universal ALU Element
- **Standard Full Adder Equations:**
  $$\mathbf{Sum = A \oplus B \oplus C_{in}}$$
  $$\mathbf{C_{out} = A \cdot B + C_{in} \cdot (A \oplus B)}$$
#### Mathematical Proofs for ALU Functions:
1. **XOR Operation (Q4.18, Q4.32, Q4.33):**
   - Set $C_{in} = 0$:
     $$Sum = A \oplus B \oplus 0 = \mathbf{A \oplus B}$$
2. **XNOR Operation (Q4.30, Q4.33, Q4.34):**
   - Set $C_{in} = 1$:
     $$Sum = A \oplus B \oplus 1 = \overline{A \oplus B} = \mathbf{A \odot B}$$
3. **AND Operation (Q4.29):**
   - Set $C_{in} = 0$, tap $C_{out}$:
     $$C_{out} = A \cdot B + 0 \cdot (A \oplus B) = \mathbf{A \cdot B}$$
4. **OR Operation (Q4.32, Q4.34, Q4.49):**
   - Set $C_{in} = 1$, tap $C_{out}$:
     $$C_{out} = A \cdot B + 1 \cdot (A \overline{B} + \overline{A} B) = A(B + \overline{B}) + \overline{A} B = A + \overline{A} B = \mathbf{A + B}$$
5. **Binary Addition ($A + B$):**
   - Let carries ripple normally; set initial $C_{in} = 0$:
     $$Sum = A + B$$
6. **Binary Subtraction ($A - B$) via Two's Complement:**
   - Identity: $A - B = A + (-B) = A + \overline{B} + 1$.
   - **Hardware configuration:** Invert input $B \to \overline{B}$; set initial carry-in $C_{in} = 1$:
     $$Sum = A + \overline{B} + 1 = \mathbf{A - B}$$
---
### 2. 4-Bit Complete ALU Architecture (Figure 8.12)
![[attachments/Pasted image 20261030204115.png]]
- **4 Key Components:**
  1. **4 Adder Elements:** 1-bit full adders stacked for bits $0, 1, 2, 3$.
  2. **B-Input Conditioning Switches:** Inverters with bypass switches feeding either $B_k$ (for addition/logic) or $\overline{B_k}$ (for subtraction).
  3. **Carry-Line Isolation Switches:**
     - **Arithmetic Mode:** Switches close $\to$ carries ripple from stage to stage.
     - **Logic Mode:** Switches open $\to$ carries isolated; carry inputs forced to fixed $0$ (for XOR/AND) or $1$ (for XNOR/OR).
  4. **Output Selection Switches (MUX):** Multiplexer selects either $Sum$ line or $C_{out}$ line as the final ALU output bit.
---
### 3. Circuit Implementations of Full Adders
#### Multiplexer-Based Adder Logic (nMOS Pass Transistors)
- Computes half-sum $H_k = A_k \oplus B_k$:
  - If $A_k = B_k \implies H_k = 0 \implies S_k = C_{k-1}, \quad C_k = A_k$.
  - If $A_k \neq B_k \implies H_k = 1 \implies S_k = \overline{C_{k-1}}, \quad C_k = C_{k-1}$.
- Minimal transistor count; buffered sum output.
![[attachments/This circuit is a pass-transistor Full Adder.png]]
![[attachments/Pasted image 20261030202149.png]]
---
#### Pass / Generate Adder Element (Q4.35, Q4.36, Q4.47)
- **Propagate (Pass):** $P_k = A_k \oplus B_k$.
- **Generate:** $G_k = A_k \cdot B_k$.
- **Carry Logic:** If $P_k = 1$, carry ripples through transmission gate ($C_k = C_{k-1}$). If $P_k = 0$, carry is generated ($C_k = G_k$).
![[attachments/Pasted image 20261030215823.png]]
---
#### Manchester Carry Chain (MCC) (Q4.40, Q4.41)
- Uses precharged dynamic logic to propagate carry bits across series pass transistors.
- **Circuit Operation:**
  - **Precharge ($\phi = 0$):** Carry nodes precharged to $V_{DD}$.
  - **Evaluate ($\phi = 1$):** If $G_k = 1$, carry node pulled to $GND$. If $P_k = 1$, pass transistor connects carry from previous stage.
- **The Problem:** Pass transistors placed in series create an $RC$ ladder network.
  - Delay grows **quadratically** with chain length:
    $$T_{delay} \propto N^2$$
  - For $N > 4$, carry delay becomes unacceptably large!
- **The Remedy:** Break the chain every 4 stages and insert a **static CMOS non-inverting buffer pair** to isolate parasitic capacitances and restore linear delay ($T \propto N$).
![[attachments/Pasted image 20261030222543.png]]
![[attachments/manchester_carry_chain.png]]
---
#### Carry Lookahead Adder (CLA) (Q4.42)
- **Necessity:** Ripple carry adders have delay linear with word length ($O(N)$), creating the primary ALU speed bottleneck.
- **CLA Principle:** Computes all carry bits in parallel in $O(1)$ time using Generate ($G_i = A_i B_i$) and Propagate ($P_i = A_i \oplus B_i$):
  $$C_1 = G_0 + P_0 C_0$$
  $$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
  $$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
  $$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
---
## 4C. Multipliers
### 1. Multiplier Fundamentals ($N \times M$ Bits)
$$\mathbf{\text{AND Gates} = N \times M} \qquad \mathbf{\text{Half Adders (HA)} = M} \qquad \mathbf{\text{Full Adders (FA)} = M(N - 2)}$$

| Multiplier Size      | AND Gates (N x M) | Half Adders (M) | Full Adders (M(N-2)) |
| :---                 | :---              | :---            | :---                 |
| 2 x 2 Bit            | 4                 | 2               | 0                    |
| 3 x 3 Bit            | 9                 | 3               | 3                    |
| 4 x 4 Bit            | 16                | 4               | 8                    |
| 4 x 2 Bit            | 8                 | 2               | 4                    |
| 5 x 3 Bit            | 15                | 3               | 9                    |

![[attachments/Pasted image 20261031132238.png]]
![[attachments/Pasted image 20261031132224.png]]
![[attachments/Pasted image 20261031132423.png]]
---
### 2. Serial-Parallel Multiplier (Q4.50, Q4.51, Q4.52, Q4.53, Q4.55, Q4.58)
- **Architecture:** Multiplicand ($A$) loaded in parallel; multiplier bits ($B$) fed serially one bit per clock cycle.
- **Role of D Flip-Flop (DFF) (Q4.52):**
  1. Stores and accumulates partial product bits from each stage.
  2. Latches carry bits between consecutive clock cycles.
  3. Acts as pipelining registers to synchronize serial data movement.
![[attachments/Pasted image 20261031002811.png]]
---
### 3. Array Multipliers & Signed Multiplication
#### Braun Multiplier (Unsigned Array Multiplier)
- Regular array of identical cells (AND gate + Full Adder) propagating sums downward and carries diagonally.
![[attachments/Pasted image 20261031010923.png]]
---
#### Baugh-Wooley Multiplier (Signed / Two's Complement) (Q4.54)
- **Problem:** Conventional array multipliers only handle positive unsigned numbers.
- **Solution:** Direct multiplication of signed two's complement numbers without sign-magnitude conversion.
- **Mechanism:**
  - MSB partial product bits have negative weight ($-2^{N-1}$).
  - Inverts NAND partial products for sign bits and adds fixed binary correction constants ($1$) into the array.
![[attachments/Pasted image 20261031013206.png]]
---
#### Systolic Array Multiplier (Pipelined Array) (Q4.56)
- 2D grid of identical Gated Full Adder (GFA) cells interconnected with local register latches.
- Eliminates global broadcast wires; throughput is 1 multiplication per clock cycle.
![[attachments/Pasted image 20261031123708.png]]
---
## 4D. Memory Cells, Shift Registers & Chip Sizing Calculations
### 1. Dynamic Storage Cells & Shift Registers
#### Inverting & Non-Inverting Dynamic Storage Cells
![[attachments/Pasted image 20261031181349.png]]
![[attachments/Pasted image 20261031181402.png]]
- **Inverting Dynamic Cell:** 1 pass switch + 1 inverter gate capacitance ($C_g$).
  - Storage: Charge trapped on gate capacitance $C_g$ holds $\overline{V_{in}}$ temporarily.
  - Transistor count: 3 transistors in nMOS, 4 in CMOS.
- **Non-Inverting Dynamic Cell:** 2 cascaded inverting stages controlled by non-overlapping clocks $\phi_1, \phi_2$.
- **Why Called "Dynamic"? (Q4.61, Q4.62, Q4.63):**
  - Data is stored purely as **electrostatic charge** on tiny parasitic gate capacitance $C_g$.
  - Charge leaks away over time through reverse-biased junction leakage currents ($I_{leak}$).
  - Requires **periodic refresh clocking** to prevent data loss.
---
#### 4-Bit Dynamic Shift Register (nMOS) (Q4.60, Q4.61, Q4.63)
- Cascade of 4 non-inverting dynamic cells (8 inverter stages + 8 pass switches).
- Data shifts 1 bit right per clock cycle $(\phi_1, \phi_2)$.
![[attachments/Pasted image 20261031181842.png]]
---
### 2. DRAM Cells: 3T vs. 1T DRAM

![[attachments/Pasted image 20261031190946.png]]
![[attachments/Pasted image 20261031191126.png]]

| Parameter          | 3T Dynamic RAM Cell        | 1T Dynamic RAM Cell  |
| :---               | :---                       | :---                 |
| Transistor Count   | 3 MOS transistors          | 1 Access Transistor  |
| Storage Element    | Gate cap of T2             | Dedicated capacitor Cs|
| Read Operation     | Non-destructive read       | Destructive read     |
| Sense Amplifier    | Standard inverter threshold| Highly sensitive diff|
| Rewrite Required?  | No                         | YES (After every read)|
| Cell Area          | ~ 500 - 1750 lambda^2      | ~ 100 - 250 lambda^2 |
| Density            | Medium                     | Maximum (Industry std)|

- **3T Cell vs. 3-Bit Shift Register (Q4.78, Q4.80):**
  - **3T DRAM Cell:** Stores **1 single bit** using 3 transistors at an addressable memory location (random access).
  - **3-Bit Dynamic Shift Register:** Stores **3 sequential bits** using 6 inverters and 6 pass gates (18 to 24 transistors) with serial shifting.
---
### 3. Improving DRAM Storage Capacity (Q4.76)
1. **Trench Capacitors:** Etch deep vertical trenches ($>5\,\mu\text{m}$) into silicon substrate $\to$ huge plate area within tiny footprint.
2. **Stacked Capacitors:** Fabricate 3D fin/crown capacitor plates vertically above the access transistor in inter-metal dielectric layers.
3. **High-$k$ Dielectrics:** Replace $\text{SiO}_2$ ($\kappa \approx 3.9$) with high dielectric constants like $\text{HfO}_2$ ($\kappa \approx 25$) or $\text{ZrO}_2$ $\to$ higher capacitance per area.
---
### 4. Pseudo-Static RAM (PSRAM) (Q4.59, Q4.72, Q4.73, Q4.81)
![[attachments/Pasted image 20261031191221.png]]
- **Circuit Structure:** 2 cross-coupled inverters forming a bistable latch, with a pass transistor $T_{\phi2}$ in the feedback loop.
- **Working Principle:**
  - During read/write ($\phi_1$): Feedback switch opens; cell acts as dynamic storage.
  - During inactive phase ($\phi_2$): Feedback switch closes; cross-coupled inverters actively restore and refresh logic levels.
- **Why Preferred over DRAM/SRAM? (Q4.63):**
  - **Overcomes Volatility:** Self-refreshes automatically every clock cycle $\to$ no external DRAM refresh controller needed.
  - **Smaller than SRAM:** Far fewer transistors and routing wires than full 6T static SRAM cells.
---
### 5. Master Formulas for Chip Sizing & Power
#### Formula 1: Physical Cell Area
$$\mathbf{A_{\text{cell}} = (\text{Cell Area in }\lambda^2) \times \lambda^2} \quad [\mu\text{m}^2]$$
#### Formula 2: Memory Capacity on Chip
$$\mathbf{\text{Total Bits} = \frac{\text{Usable Chip Area}}{A_{\text{cell}}} = \frac{\text{Length} \times \text{Width}}{(\text{Cell Area in }\lambda^2) \times \lambda^2}}$$
#### Formula 3: Required Chip Area for $N$ Bits
$$\mathbf{\text{Chip Area} = N \times A_{\text{cell}} = N \times [(\text{Cell Area in }\lambda^2) \times \lambda^2]}$$
$$\mathbf{\text{Chip Side} = \sqrt{\text{Chip Area}}}$$
#### Formula 4: Power Dissipation
$$\mathbf{P_{\text{total}} = N \times P_{\text{bit}} = N \times \left(\frac{V_{DD}^2}{R_{\text{cell}}}\right)}$$
---
### 6. Fully Solved Numerical Exam Problems
#### Problem 1: PSRAM in $5\text{ mm} \times 5\text{ mm}$ Chip (Q4.59)
- Given: Cell area $= 1750\lambda^2$, $\lambda = 2\,\mu\text{m}$, Chip $= 5\text{ mm} \times 5\text{ mm} = 25\text{ mm}^2 = 25 \times 10^6\,\mu\text{m}^2$.
- Cell Area in $\mu\text{m}^2$:
  $$A_{cell} = 1750 \times (2\,\mu\text{m})^2 = 1750 \times 4\,\mu\text{m}^2 = \mathbf{7000\,\mu\text{m}^2}$$
- Number of Bits:
  $$\text{Capacity} = \frac{25 \times 10^6\,\mu\text{m}^2}{7000\,\mu\text{m}^2} \approx \mathbf{3571\text{ bits}} \approx \mathbf{3.57\text{ Kbits}}$$
---
#### Problem 2: Dynamic Shift Register in $5\text{ mm} \times 5\text{ mm}$ Chip (Q4.60)
- Given: Cell area $= 1200\lambda^2$, $\lambda = 2\,\mu\text{m}$, Chip $= 5\text{ mm} \times 5\text{ mm}$.
- Cell Area:
  $$A_{cell} = 1200 \times 4\,\mu\text{m}^2 = \mathbf{4800\,\mu\text{m}^2}$$
- Number of Bits:
  $$\text{Capacity} = \frac{25 \times 10^6\,\mu\text{m}^2}{4800\,\mu\text{m}^2} \approx \mathbf{5208\text{ bits}} \approx \mathbf{5.2\text{ Kbits}}$$
---
#### Problem 3: 3T DRAM in $4\text{ mm} \times 4\text{ mm}$ Chip (Q4.64)
- Given: Feature size $= 32\lambda \times 42\lambda = 1344\lambda^2$, $\lambda = 2.5\,\mu\text{m}$, Chip $= 4\text{ mm} \times 4\text{ mm} = 16 \times 10^6\,\mu\text{m}^2$.
- Cell Area:
  $$A_{cell} = 1344 \times (2.5)^2 = 1344 \times 6.25 = \mathbf{8400\,\mu\text{m}^2}$$
- Capacity:
  $$\text{Total Bits} = \frac{16 \times 10^6\,\mu\text{m}^2}{8400\,\mu\text{m}^2} \approx \mathbf{1904\text{ bits}} \approx \mathbf{1.9\text{ Kbits}}$$
---
#### Problem 4: 3T DRAM Cell of $500\lambda^2$ on $4\text{ mm} \times 4\text{ mm}$ Chip (Q4.66)
- Given: Cell area $= 500\lambda^2$, $\lambda = 2.5\,\mu\text{m}$.
- Cell Area:
  $$A_{cell} = 500 \times 6.25 = \mathbf{3125\,\mu\text{m}^2}$$
- Capacity:
  $$\text{Total Bits} = \frac{16 \times 10^6\,\mu\text{m}^2}{3125\,\mu\text{m}^2} = \mathbf{5120\text{ bits}} \approx \mathbf{5.12\text{ Kbits}}$$
---
#### Problem 5: Chip Size to Store 10 Kbits in 3T DRAM (Q4.65)
- Given: $N = 10\text{ Kbits} = 10 \times 1024 = 10240\text{ bits}$ (or $10000$ bits), cell area $\approx 1750\lambda^2$, $\lambda = 2.5\,\mu\text{m}$.
- $A_{cell} = 1750 \times 6.25 = 10937.5\,\mu\text{m}^2$.
- Chip Area:
  $$\text{Chip Area} = 10240 \times 10937.5\,\mu\text{m}^2 \approx 1.12 \times 10^8\,\mu\text{m}^2 = \mathbf{112\text{ mm}^2}$$
- Chip Side:
  $$\text{Side} = \sqrt{112\text{ mm}^2} \approx \mathbf{10.58\text{ mm}}$$
---
#### Problem 6: Chip Size to Store 20 Kbits in 1T DRAM (Q4.67, Q4.69)
- Given: $N = 20\text{ Kbits} = 20480\text{ bits}$, 1T cell area $\approx 250\lambda^2$, $\lambda = 2.5\,\mu\text{m}$.
- $A_{cell} = 250 \times (2.5\,\mu\text{m})^2 = 1562.5\,\mu\text{m}^2$.
- Total Chip Area:
  $$\text{Area} = 20480 \times 1562.5\,\mu\text{m}^2 = 3.2 \times 10^7\,\mu\text{m}^2 = \mathbf{32\text{ mm}^2}$$
- Chip Side:
  $$\text{Side} = \sqrt{32\text{ mm}^2} \approx \mathbf{5.66\text{ mm}}$$
---
#### Problem 7: Chip Size to Store 15 Kbits in 3T DRAM vs. 1T DRAM (Q4.75, Q4.83)
- Given: $N = 15\text{ Kbits} = 15360\text{ bits}$, $\lambda = 2.5\,\mu\text{m}$.
- **1. For 1T DRAM ($A_{cell} \approx 250\lambda^2 = 1562.5\,\mu\text{m}^2$):**
  $$\text{Chip Area} = 15360 \times 1562.5 = 2.4 \times 10^7\,\mu\text{m}^2 = \mathbf{24\text{ mm}^2} \implies \mathbf{\text{Side} \approx 4.9\text{ mm}}$$
- **2. For 3T DRAM ($A_{cell} \approx 1000\lambda^2 = 6250\,\mu\text{m}^2$):**
  $$\text{Chip Area} = 15360 \times 6250 = 9.6 \times 10^7\,\mu\text{m}^2 = \mathbf{96\text{ mm}^2} \implies \mathbf{\text{Side} \approx 9.8\text{ mm}}$$
- **Conclusion:** 1T DRAM achieves $4\times$ smaller chip area for identical capacity.
