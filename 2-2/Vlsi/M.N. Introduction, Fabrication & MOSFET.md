# Topic 1: Introduction, Fabrication & MOSFET Basics

---

## 1A. VLSI Basics, Moore's Law & IC Packages

### VLSI Overview & Advantages
- **VLSI (Very Large Scale Integration):** $> 10^5$ transistors per single silicon chip.
- **Key Advantages:**
  - **High Packing Density:** Smaller footprint, lower system weight.
  - **Low Power:** Shorter interconnects $\to$ drastically lower parasitic capacitance.
  - **High Speed:** Shorter transit paths $\to$ higher clock frequency.
  - **Low Per-Function Cost:** Batch fabrication of millions of devices simultaneously.
  - **High Reliability:** Monolithic silicon replaces failure-prone solder joints / external wiring.

```
+------------------------------------------------------------------------+
| Level  | Transistor Count | Gate Count  | Typical Applications         |
| :---   | :---             | :---        | :---                         |
| SSI    | 1 - 100          | 1 - 10      | Logic gates (AND, OR, NOT)   |
| MSI    | 100 - 1,000      | 10 - 100    | Adders, MUX, Decoders        |
| LSI    | 1k - 100k        | 100 - 3k    | 8-bit $\mu$P, Small Memories |
| VLSI   | 100k - 1M        | 3k - 100k   | 32/64-bit CPUs, DSPs         |
| ULSI   | 1M - 100M        | 100k - 10M  | Multi-core Processors, GPUs  |
| GSI    | > 100M           | > 10M       | Modern SoCs, AI Accelerators |
+------------------------------------------------------------------------+
```

---

### Moore's Law
- **Moore's 1st Law (1965):**
  - Transistor count on a microchip doubles approximately every **18 to 24 months**.
  - System performance doubles while cost per transistor falls exponentially.

![[attachments/Pasted image 20261102000924.png]]

---

### Speed vs. Power Performance Comparison
- **Speed Metric:** Gate delay ($\tau$ or $t_{pd}$ in ns/ps) $\to$ lower is faster.
- **Power Metric:** Power dissipation per gate ($P_d$ in $\mu\text{W}$/$\text{mW}$) $\to$ lower is cooler.

![[attachments/Pasted image 20261102001105.png]]

```
+------------------------------------------------------------------------+
| Technology | Delay / Gate    | Power / Gate    | Key Characteristic    |
| :---       | :---            | :---            | :---                  |
| CMOS       | 1 - 10 ns       | 10 - 100 uW     | Ultra-low static power|
| BiCMOS     | 0.1 - 1 ns      | 1 - 5 mW        | High capacitive drive |
| nMOS       | 2 - 20 ns       | 0.1 - 1 mW      | High static power     |
| ECL        | < 0.5 ns        | 10 - 100 mW     | Fastest Si, hot       |
| GaAs       | 10 - 100 ps     | 0.1 - 2 mW      | Ultra-fast, expensive |
+------------------------------------------------------------------------+
```

---

### IC Packaging
- **4 Main Functions:**
  1. **Mechanical Protection:** Shields silicon die against mechanical shocks and handling stress.
  2. **Electrical Interconnect:** Provides low-resistance conductive pinout from chip pads to PCB.
  3. **Heat Dissipation:** Conducts internal thermal energy away to heatsinks / environment.
  4. **Environmental Sealing:** Hermetically seals wafer against moisture, ionic impurities, and oxidation.

#### Package Types
- **DIP (Dual-In-Line Package):**
  - Through-hole mounting, two parallel rows of pins (standard 100-mil spacing).
  - High lead inductance, bulky, pin-count limited ($\le 64$ pins).
- **TO (Transistor Outline):**
  - Metal-can package with circular pin header ($2\text{ to }12$ pins).
  - Hermetic seal, excellent thermal conduction, for discrete power devices / RF.
- **Flip-Chip (FC) Packaging:**
  - Die flipped face-down; solder bumps placed directly across die surface connect directly to substrate.
  - **Advantages over Wire Bonding:**
    - **Shorter Interconnects:** Near-zero wire length $\to$ lowest parasitic $L$ and $C$ $\to$ highest operating speed.
    - **Massive I/O Density:** Uses entire surface area (area array) rather than perimeter pads only.
    - **Superior Heat Transfer:** Direct thermal contact to substrate and back-side lid.
    - **Compact Footprint:** Package size nearly equal to die size.

---

## 1B. Fabrication Processes

### 1. nMOS Fabrication (8 Steps)
1. **Lightly Doped p-Substrate:** Silicon wafer cleaned and prepared.
2. **Thick Oxide ($\text{SiO}_2$):** $\approx 1\,\mu\text{m}$ thermally grown ($1000^\circ\text{C}$).
3. **Thinox / Active Area (Mask 1):** Photolithography + acid etch exposes bare Si for channel/source/drain.
4. **Thin Gate Oxide + CVD Polysilicon:** Thin gate $\text{SiO}_2$ ($\sim 0.1\,\mu\text{m}$) grown; heavily doped poly deposited via CVD.
5. **Gate Patterning (Mask 2):** Photolithography defines polysilicon gate electrode.
6. **Self-Aligned $n^+$ Source/Drain Diffusion:** Arsenic / Phosphorus implanted; poly gate masks channel automatically.
7. **Contact Cuts (Mask 3):** Thick $\text{SiO}_2$ deposited; contact holes etched to S, D, and Gate.
8. **Metallization (Mask 4):** Aluminum deposited and etched into interconnection lines.

![[attachments/Pasted image 20261102010909.png]]

---

### 2. pMOS Fabrication
- **Substrate:** Lightly doped n-type silicon.
- **Source/Drain:** $p^+$ dopants (Boron) diffused/implanted.
- **Physics:** Holes carry current $\to$ mobility $\mu_p \approx \frac{1}{2.5} \mu_n \to$ channel resistance $2.5\times$ higher than nMOS for same size.

---

### 3. CMOS n-Well Process Steps
- **Substrate:** Lightly doped p-type wafer.
- **nMOS:** Formed directly in p-substrate.
- **pMOS:** Formed inside a diffused n-well.

#### Process Sequence:
1. **Oxidation & Photoresist Coating:** Thermal oxide grown; PR applied.
2. **Mask 1 (n-Well Formation):** Window opened; Phosphorus/Arsenic implanted and driven deep at high temperature.
3. **Mask 2 (Thinox / Active Areas):** Defines transistor active regions; field oxide grown outside (LOCOS/STI).
4. **Thin Gate Oxide & Polysilicon CVD:** Thin oxide grown; poly deposited.
5. **Mask 3 (Gate Patterning):** Poly etched to create nMOS and pMOS gates simultaneously.
6. **Mask 4 ($p^+$ Implant):** Boron implanted to form pMOS Source/Drain + p-substrate tap ($p^+$).
7. **Mask 5 ($n^+$ Implant):** Arsenic implanted to form nMOS Source/Drain + n-well tap ($n^+$).
8. **Inter-Layer Dielectric & Mask 6 (Contact Cuts):** Oxide passivation deposited; contact vias opened.
9. **Mask 7 (Metallization):** Aluminum sputtered; etched to form $V_{DD}$, $GND$, and signal routes.

![[attachments/Pasted image 20261102005917.png]]
![[attachments/Pasted image 20261102005939.png]]
![[attachments/Pasted image 20261102005954.png]]
![[attachments/Pasted image 20261102010049.png]]
![[attachments/Pasted image 20261102010144.png]]

---

### 4. Comparison: n-Well vs. p-Well CMOS

```
+------------------------------------------------------------------------+
| Parameter          | n-Well CMOS              | p-Well CMOS            |
| :---               | :---                     | :---                   |
| Starting Substrate | p-type silicon           | n-type silicon         |
| Well Type          | n-well (for pMOS)        | p-well (for nMOS)      |
| Native Transistor  | nMOS (in p-sub)          | pMOS (in n-sub)        |
| Device Performance | Optimized nMOS (higher u)| Optimized pMOS         |
| Fabrication Origin | Compatible with nMOS line| Compatible with BJT line|
| Industry Adoption  | High (standard modern)   | Low (historic)         |
+------------------------------------------------------------------------+
```

---

### 5. Twin-Tub CMOS Process
- **Substrate:** High-resistivity $n^-/p^-$ epitaxial layer on heavily doped $n^+/p^+$ wafer.
- **Tubs:** Two separate tubs diffused side-by-side:
  - **n-tub:** Hosts pMOS transistors.
  - **p-tub:** Hosts nMOS transistors.
- **Key Advantages:**
  - Independent control of $V_{tn}$ and $V_{tp}$ threshold voltages.
  - Independent doping optimization $\to$ optimizes both electron and hole mobilities.
  - Epitaxial substrate drastically reduces substrate resistance $\to$ **eliminates latch-up**.

![[attachments/twin_tub_cmos.png]]

---

## 1C. MOS Transistor Operation & Logic Styles

### E-Type nMOS Drain Current Derivation
- **Channel Charge per unit area:**
  $$Q(x) = C_{ox} [V_{gs} - V_{tn} - V(x)]$$
- **Drift Velocity:**
  $$v(x) = \mu_n E(x) = \mu_n \frac{dV}{dx}$$
- **Current Equation:**
  $$I_{ds} = W \cdot Q(x) \cdot v(x) = W \mu_n C_{ox} [V_{gs} - V_{tn} - V(x)] \frac{dV}{dx}$$
- **Integration across channel ($x = 0 \to L$, $V = 0 \to V_{ds}$):**
  $$\int_0^L I_{ds} dx = W \mu_n C_{ox} \int_0^{V_{ds}} [V_{gs} - V_{tn} - V(x)] dV$$
  $$I_{ds} L = W \mu_n C_{ox} \left[ (V_{gs} - V_{tn})V_{ds} - \frac{V_{ds}^2}{2} \right]$$

$$\mathbf{I_{ds} = \mu_n C_{ox} \left(\frac{W}{L}\right) \left[ (V_{gs} - V_{tn})V_{ds} - \frac{V_{ds}^2}{2} \right]} \quad (\text{Linear Region: } V_{ds} < V_{gs} - V_{tn})$$

- **Saturation Region ($V_{ds} \ge V_{gs} - V_{tn}$):**
  - Pinch-off at drain; substitute $V_{ds} = V_{gs} - V_{tn}$:
$$\mathbf{I_{ds,sat} = \frac{1}{2} \mu_n C_{ox} \left(\frac{W}{L}\right) (V_{gs} - V_{tn})^2}$$

---

### Strong vs. Degraded Logic Levels

#### 1. nMOS Switch:
- **Passing '0' ($V_{in} = 0\text{ V}$, $V_g = 5\text{ V}$):**
  - $V_{gs} = V_g - V_{out} = 5 - 0 = 5\text{ V} \ge V_{tn}$ ($1\text{ V}$).
  - Conducts all the way to $0\text{ V} \implies$ **Strong '0'**.
- **Passing '1' ($V_{in} = 5\text{ V}$, $V_g = 5\text{ V}$):**
  - As $V_{out}$ rises, $V_{gs} = V_g - V_{out} = 5 - V_{out}$.
  - Conduction stops when $V_{gs} = V_{tn} \implies 5 - V_{out} = 1\text{ V} \implies V_{out} = 4\text{ V}$.
  - Cannot reach full $V_{DD} \implies$ **Degraded (Weak) '1'** ($V_{out} = V_{DD} - V_{tn}$).

#### 2. pMOS Switch:
- **Passing '1' ($V_{in} = 5\text{ V}$, $V_g = 0\text{ V}$):**
  - $|V_{gs}| = |0 - 5| = 5\text{ V} \ge |V_{tp}|$ ($1\text{ V}$).
  - Conducts all the way to $5\text{ V} \implies$ **Strong '1'**.
- **Passing '0' ($V_{in} = 0\text{ V}$, $V_g = 0\text{ V}$):**
  - As $V_{out}$ drops, $|V_{gs}| = |V_g - V_{out}| = V_{out}$.
  - Conduction stops when $V_{out} = |V_{tp}| = 1\text{ V}$.
  - Cannot reach $0\text{ V} \implies$ **Degraded (Weak) '0'** ($V_{out} = |V_{tp}|$).

![[attachments/Pasted image 20261102012727.png]]

---

### Pass Transistor (PT) vs. Transmission Gate (TG)

![[attachments/Pasted image 20261030215042.png]]

```
+------------------------------------------------------------------------+
| Feature              | Pass Transistor (PT)     | Transmission Gate (TG)|
| :---                 | :---                     | :---                  |
| Device Count         | 1 (nMOS or pMOS)         | 2 (nMOS + pMOS par.)  |
| Control Signals      | 1 line ($C$)             | 2 lines ($C$ and ~C)  |
| Signal Range         | 0 to V_DD - V_tn (lossy) | Full 0 to V_DD (rail) |
| On-Resistance        | Variable with signal     | Nearly constant & low |
| Silicon Area         | Minimal                  | ~ 2x larger           |
| High-Speed Circuits  | Slower (poor drive)      | Faster full-swing     |
+------------------------------------------------------------------------+
```

- **CMOS vs. TG in High-Speed Circuits:**
  - TG is purely **passive** (no voltage/current amplification; signal attenuates across stages).
  - CMOS logic is **active** (regenerates logic levels, restores slew rates, provides high capacitive drive).
  - **Verdict:** Buffered CMOS is superior for long cascaded high-speed paths; TGs are best for compact multiplexing.

---

### Double Rail Logic
- Distributes both true and inverted logic signals ($A$ and $\overline{A}$) over dedicated parallel rails.
- **Why Used:**
  - Directly drives transmission gates ($C$ and $\overline{C}$).
  - Eliminates separate inverter delays inside critical logic blocks.
  - Essential for differential / domino logic and multiplexer arrays.

---

## 1D. Inverter Loads, BiCMOS & Latch-Up

### Pull-Up (PU) Load Types Comparison
1. **Resistive Load:** Simple, passive; occupies massive silicon area ($R \propto \text{Area}$); obsolete.
2. **Enhancement nMOS Load ($V_{gs} = V_{ds}$):** Compact; but $V_{OH} = V_{DD} - V_{tn}$ (loss of high level); non-zero static power when output is low.
3. **Depletion nMOS Load ($V_{gs} = 0$):** Gate connected to source; acts as constant current source; pulls full $V_{OH} = V_{DD}$; requires $Z_{pu}:Z_{pd} = 4:1$; dissipates static power when output is LOW.
4. **Pseudo-nMOS Load:** pMOS transistor with gate grounded; simpler fabrication than depletion nMOS; fast pull-up; draws constant static DC current when output is LOW.
5. **Complementary CMOS Load:** pMOS pull-up + nMOS pull-down; **zero static power**; rail-to-rail swing ($0\text{ to }V_{DD}$); highest noise margins.

![[attachments/Pasted image 20261101214449.png]]

---

### BiCMOS Inverter Circuits & Base Discharge

```
               V_DD
                |
          +-----+-----+
          |           |
        [T4] pMOS   [T2] NPN (Pull-up)
          |           |
Vin ------+-----+     +-----> Vout
          |     |     |
        [T3] nMOS   [T1] NPN (Pull-down)
          |           |
         GND         GND
```

![[attachments/Pasted image 20261102014814.png]]
![[attachments/Pasted image 20261102014848.png]]
![[attachments/Pasted image 20261102014937.png]]

#### Base Charge Discharge Comparison:
- **The Problem:** BJTs store minority carriers in their base regions. When turning OFF, trapped charge delays switching and creates dynamic power spikes.
- **Bleed Resistors ($R_1, R_2$):** Provide passive discharge path $\to$ causes continuous static DC leakage current.
- **Active MOS Switches ($T_5, T_6$):**
  - MOS transistors turn ON only during transitions to rapidly short BJT bases to GND/Vout.
  - In steady states, MOS switches turn OFF completely $\implies$ **ZERO static DC current**.
  - **Verdict:** Active MOS discharge is superior: zero static power, faster turn-off, smaller area than large resistors.

---

### CMOS & BiCMOS Latch-Up

![[attachments/Pasted image 20261102021918.png]]

- **Definition:** Latch-up is a catastrophic, low-impedance short circuit between $V_{DD}$ and $V_{SS}$ triggered by unintentional turn-on of parasitic $p\text{-}n\text{-}p\text{-}n$ SCR (thyristor).
- **Parasitic Structure:**
  - Vertical PNP: $p^+$ Source (PMOS) – n-well – p-substrate.
  - Lateral NPN: $n^+$ Source (NMOS) – p-substrate – n-well.
  - $R_{well}$ and $R_{sub}$: Well and substrate parasitic resistances.
- **Latching Condition:**
  - Regenerative positive feedback occurs if:
    $$\beta_{npn} \times \beta_{pnp} \ge 1 \quad \text{and} \quad I_{trigger} \cdot R_{sub/well} \ge 0.7\text{ V}$$
- **Why BiCMOS is More Susceptible:**
  - Contains heavily doped buried layers and real NPN BJTs $\to$ lower breakdown voltages, higher carrier lifetimes, higher parasitic loop gains.

#### Prevention Methods:
1. **Guard Rings:** Diffuse $n^+$ rings (to $V_{DD}$) and $p^+$ rings (to $GND$) around transistors to collect stray injected carriers.
2. **Epitaxial Wafer / Low-Resistance Substrate:** Heavily doped substrate under thin epi-layer shorts $R_{sub} \to$ voltage cannot reach $0.7\text{ V}$.
3. **Physical Spacing:** Increase PMOS-to-NMOS separation $\to$ drastically cuts parasitic bipolar gain $\beta$.
4. **Trench Isolation / SOI (Silicon-on-Insulator):** Physical $\text{SiO}_2$ dielectric barriers sever parasitic $p\text{-}n\text{-}p\text{-}n$ path completely.

---

## 1E. Logic Styles & Circuit Concepts

### Glue Logic
- Simple interconnecting circuits (logic gates, latches, address decoders, buffers) used to interface major VLSI functional blocks (CPU, ALU, Memory, Bus).

---

### Tri-State Buffer & Inverter

![[attachments/Pasted image 20261102012332.png]]

```
+-------------------------------------------------------------+
| EN  | Input (A) | Inverter Output (Y) | Buffer Output (Y)   |
| :--- | :---      | :---                | :---                |
| 0   | 0         | Z (High-Impedance)  | Z (High-Impedance)  |
| 0   | 1         | Z (High-Impedance)  | Z (High-Impedance)  |
| 1   | 0         | 1 (High)            | 0 (Low)             |
| 1   | 1         | 0 (Low)             | 1 (High)            |
+-------------------------------------------------------------+
```

---

### Circuit Phenomena
- **Floating Z (High Impedance):** Output node disconnected from both $V_{DD}$ and $V_{SS}$. Voltage floats on parasitic node capacitance; easily corrupted by capacitive crosstalk or leakage.
- **Crowbar Current:** Transient short-circuit current spike from $V_{DD}$ directly to $GND$ when input voltage is near midpoint ($V_{tn} < V_{in} < V_{DD} - |V_{tp}|$), turning both pull-up and pull-down networks ON simultaneously.

---

### Dynamic CMOS Logic
- **Architecture:** 
  - pMOS Precharge transistor (clocked by $\phi$) connected to $V_{DD}$.
  - nMOS Evaluation network implementing logic function.
  - nMOS Foot transistor (clocked by $\phi$) connected to $GND$.

```
               V_DD
                |
              [pMOS] <-- Clock (phi)
                |
          +-----+-----> Output (C_L)
          |
     [ nMOS Logic ] <-- Data Inputs (A, B, C)
          |
        [nMOS]       <-- Clock (phi)
          |
         GND
```

- **Two-Phase Operation:**
  1. **Precharge ($\phi = 0$):** Precharge pMOS ON, foot nMOS OFF. Output node capacitor $C_L$ charges to $V_{DD}$.
  2. **Evaluate ($\phi = 1$):** Precharge pMOS OFF, foot nMOS ON. Output conditionally discharges to $GND$ if logic inputs create a conducting path.
- **Key Advantages:**
  - Only $N + 2$ transistors needed (compared to $2N$ in static CMOS).
  - Lower input gate capacitance $\to$ higher switching speed and density.
  - Zero static power dissipation.
- **Drawbacks:**
  - Charge leakage across reverse-biased junctions $\to$ requires minimum clock frequency.
  - Charge sharing between output node and internal parasitic nodes.
  - Strictly non-inverting cascading limitations (requires Domino logic / inverters between stages).

---

### Parity Generator
- Detects single-bit transmission errors by evaluating odd or even numbers of 1s in a data stream.
- **Block Diagram:** Cascade of XOR gates:
  $$P = D_0 \oplus D_1 \oplus D_2 \oplus \dots \oplus D_{n-1}$$
- If total 1s is odd $\to P = 1$; if even $\to P = 0$.

