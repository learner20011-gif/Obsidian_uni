# Topic 3: Design & Layout
---
## 3A. CMOS Logic Implementation & Compound Gates
### 1. CMOS Gate Synthesis Rules
- **PUN (Pull-Up Network):** pMOS transistors connected to $V_{DD}$.
  - Conducts when inputs are **0** (active LOW).
  - **AND ($\cdot$):** Parallel pMOS branches.
  - **OR ($+$):** Series pMOS chain.
- **PDN (Pull-Down Network):** nMOS transistors connected to $GND$.
  - Conducts when inputs are **1** (active HIGH).
  - **AND ($\cdot$):** Series nMOS chain.
  - **OR ($+$):** Parallel nMOS branches.
- **Duality:** PUN is the topological dual of PDN.
---
### 2. Compound Gate Naming & Boolean Expressions
- **AOI (AND-OR-INVERT):** Groups of series AND branches connected in parallel, inverted at output.
  - **AOI22:** $Y = \overline{(A \cdot B) + (C \cdot D)}$
  - **AOI222:** $Y = \overline{(A \cdot B) + (C \cdot D) + (E \cdot F)}$
  - **AOI23:** $Y = \overline{(A \cdot B) + (C \cdot D \cdot E)}$
  - **AOI31:** $Y = \overline{(A \cdot B \cdot C) + D}$
  - **AOI32:** $Y = \overline{(A \cdot B \cdot C) + (D \cdot E)}$
- **OAI (OR-AND-INVERT):** Groups of parallel OR branches connected in series, inverted at output.
  - **OAI31:** $Y = \overline{(A + B + C) \cdot D}$
  - **OAI33:** $Y = \overline{(A + B + C) \cdot (D + E + F)}$
  - **OAI34:** $Y = \overline{(A + B + C) \cdot (D + E + F + G)}$
  - **OAI322:** $Y = \overline{(A + B + C) \cdot (D + E) \cdot (F + G)}$
  - **OAI332:** $Y = \overline{(A + B + C) \cdot (D + E + F) \cdot (G + H)}$
  - **OAI223:** $Y = \overline{(A + B) \cdot (C + D) \cdot (E + F + G)}$
- **Non-Inverting Version (e.g., OA322):**
  - $Y = (A + B + C) \cdot (D + E) \cdot (F + G)$ (requires appending a static CMOS inverter to OAI322 output).
---
### 3. Solved Implementation Expressions
1. **$F = \overline{[(A \cdot B) + (C \cdot D) + E]}$ (Q3.5):**
   - **PDN:** Series pair $(A, B)$ in parallel with series pair $(C, D)$ in parallel with single nMOS $(E)$.
   - **PUN:** Parallel pair $(A, B)$ in series with parallel pair $(C, D)$ in series with single pMOS $(E)$.
2. **$F = \overline{(A + B \cdot C)(D \cdot E + F)}$ (Q3.16):**
   - **PDN:** $[A \text{ in par with } (B \text{ ser } C)] \text{ in series with } [(D \text{ ser } E) \text{ in par with } F]$.
   - **PUN:** $[A \text{ in ser with } (B \text{ par } C)] \text{ in par with } [(D \text{ par } E) \text{ in ser with } F]$.
3. **$Y = \overline{(A \cdot B) \cdot C + (D + E) \cdot F + G \cdot H}$ (Q3.20):**
   - **PDN:** Branch 1: $A, B, C$ in series. Branch 2: $(D \parallel E)$ in series with $F$. Branch 3: $G, H$ in series. All three branches placed in parallel to GND.
---
### 4. Euler's Path Method for Optimum Stick Diagrams
- **The Problem:** Random transistor placement requires diffusion layer breaks, increasing layout area and parasitic diffusion capacitance.
- **The Solution:** Euler's Path algorithm finds an uninterrupted sequence of gates common to both PUN and PDN.
#### Methodology:
1. Translate logic schematic into two graphs: PUN graph and PDN graph.
   - Vertices = circuit nodes ($V_{DD}$, $GND$, Output, internal junctions).
   - Edges = transistor gates ($A, B, C, \dots$).
2. Identify an **Eulerian Path** (walk visiting every edge exactly once) that has the **identical gate sequence** in both graphs.
3. Place a single continuous horizontal diffusion strip for pMOS (top) and nMOS (bottom).
4. Run vertical polysilicon tracks in the exact Euler sequence across both diffusion strips.
5. Add metal interconnections and contacts according to node connections.
![[attachments/Pasted image 20261031222500.png]]
![[attachments/Pasted image 20261031223438.png]]
![[attachments/Pasted image 20261031224503.png]]
![[attachments/Pasted image 20261031225436.png]]
---
## 3B. Stick Diagrams & Mask Layouts
### 1. Stick Diagram Definition & Purpose
- **Definition:** A simplified, topological layout sketch where lines represent physical layers, and line crossings define transistors or contacts.
- **Advantages:**
  - Guides transistor placement and routing without worrying about dimensional scaling.
  - Identifies layer crossing conflicts and routing bottlenecks early.
  - Easily converted into mask geometry by expanding lines into rectangles following design rules.
---
### 2. Standard Color Encodings & Layers

| Layer                  | Stick Color     | Mask Encoding | CIF Layer   |
| :---                   | :---            | :---          | :---        |
| n-Diffusion (Active)   | Green           | Hatch 45 deg  | ND          |
| p-Diffusion (Active)   | Yellow          | Hatch 45 deg  | CAA / CPA   |
| Polysilicon 1          | Red             | Hatch 45 deg  | NP          |
| Polysilicon 2          | Orange          | Hatch 45 deg  | CPS         |
| Metal 1                | Blue            | Vert stripes  | NM          |
| Metal 2                | Purple / D-Blue | Horiz stripes | CMS         |
| Contact Cut            | Black dot       | Solid square  | NC          |
| Via (Metal 1 to 2)     | Black dot       | Cross/Square  | CVA         |
| Demarcation Line       | Brown dashed    | N/A           | CPW         |
| Depletion Implant      | Yellow outline  | Yellow rect   | NI          |
| Buried Contact         | Brown dot       | Brown cross   | NB          |

![[attachments/Pasted image 20261101200548.png]]
![[attachments/Pasted image 20261101200648.png]]
![[attachments/Pasted image 20261101201005.png]]
---
### 3. CMOS Inverter Stick Diagram & Mask Layout
#### Steps to Draw CMOS Inverter Stick:
1. Draw horizontal $V_{DD}$ (top) and $V_{SS}$ (bottom) in **Blue** (Metal 1).
2. Draw dashed **Brown** line (demarcation line) dividing p-region and n-region.
3. Draw vertical/horizontal **Yellow** line (p-diffusion) under $V_{DD}$ rail.
4. Draw vertical/horizontal **Green** line (n-diffusion) above $V_{SS}$ rail.
5. Cross both diffusion strips with a single vertical **Red** line (Polysilicon) $\to$ forms pMOS and nMOS gates ($V_{in}$).
6. Connect pMOS Source to $V_{DD}$ rail and nMOS Source to $V_{SS}$ rail using metal-diffusion contacts.
7. Connect pMOS Drain and nMOS Drain together with **Blue** line to form output $V_{out}$.
8. Place substrate tap ($p^+$ to $V_{SS}$) and well tap ($n^+$ to $V_{DD}$).
![[attachments/Pasted image 20261101194040.jpg]]
![[attachments/Pasted image 20261101200805.png]]
---
### 4. 8:1 nMOS Inverter Stick & Mask Layout (Q3.24)
- **Ratio Requirement:** $Z_{pu} : Z_{pd} = 8:1$.
  - Pull-down nMOS: $Z_{pd} = 1$ ($2\lambda \times 2\lambda$).
  - Depletion Pull-up: $Z_{pu} = 8$ (Length $= 16\lambda$, Width $= 2\lambda$).
- **Implant:** Yellow box ($6\lambda \times 6\lambda$ minimum) enclosing depletion transistor.
- **Layers:** Polysilicon input wire (Red) and polysilicon output wire (Red) as specified in exam question.
---
## 3C. Lambda Design Rules, Contacts, Poly Overhang & Silicides
### 1. Lambda ($\lambda$) Based Design Rules (Mead-Conway)
- Normalizes all physical layout dimensions to scalable parameter $\lambda$ ($2\lambda$ = minimum gate length).

| Feature / Layer          | Minimum Width | Minimum Spacing / Clearance |
| :---                     | :---          | :---                        |
| Polysilicon              | 2 lambda      | 2 lambda                    |
| n-Diffusion / p-Diffusion| 2 lambda      | 3 lambda                    |
| Poly to Diffusion        | -             | 1 lambda                    |
| Metal 1                  | 3 lambda      | 3 lambda                    |
| Metal 2                  | 4 lambda      | 4 lambda                    |
| Contact Cut              | 2 x 2 lambda  | 2 lambda to another cut     |
| Via                      | 2 x 2 lambda  | 2 lambda to another via     |

![[attachments/Pasted image 20261101203546.png]]
---
### 2. Why Polysilicon Must Overhang Gate by $2\lambda$ (Q3.36, Q3.37)
- **The Physics:** The polysilicon gate serves as a self-aligned mask during Source/Drain ion implantation.
- **The Risk:** During photolithography, mask misalignment occurs (up to $\pm 1\lambda$).
- **Failure Mechanism:** If poly does not overhang, misalignment causes the poly edge to fall inside the channel. The $n^+$ implant will enter the gap, bridging Source and Drain $\to$ **catastrophic permanent short circuit!**
- **Safety Rule:** Extending polysilicon $\ge \mathbf{2\lambda}$ past diffusion boundary guarantees complete channel coverage despite maximum lateral misalignment.
---
### 3. Contact Cut vs. Via (Q3.36, Q3.38)

| Parameter          | Contact Cut                | Via                  |
| :---               | :---                       | :---                 |
| Layers Connected   | Metal 1 to Poly/Diffusion  | Metal 1 to Metal 2   |
| Interconnect Level | Lowest silicon interface   | Upper routing levels |
| Cut Dimensions     | 2 x 2 lambda               | 2 x 2 lambda         |
| Surrounding Flange | 4 x 4 lambda Metal 1 pad   | 4 x 4 lambda overlap |
| Fabrication Step   | High aspect-ratio etch     | Inter-metal via etch |

![[attachments/Pasted image 20261101203606.png]]
![[attachments/Pasted image 20261101204207.png]]
![[attachments/Pasted image 20261101204403.png]]
- **Butting Contact:** Directly connects polysilicon and diffusion using an overlying Metal 1 cap ($4\lambda \times 6\lambda$). Saves area, but prone to reliability issues.
- **Buried Contact:** Direct silicon-to-polysilicon ohmic contact ($2\lambda \times 2\lambda$ cut) without metal layer.
---
### 4. Silicides (Q3.42)
- **Definition:** Intermetallic compound formed by sintering a refractory metal (Titanium, Tantalum, Tungsten, Platinum) with silicon at high temperature ($600-800^\circ\text{C}$).
- **Comparison:**
  - Standard Polysilicon: $R_s = 15 - 100\,\Omega/\Box$.
  - Silicide (Polycide / Salicide): $R_s = \mathbf{2 - 4\,\Omega/\Box}$ ($10\times$ to $50\times$ lower!).
- **Pros:**
  - Drastically lowers $RC$ delay along long interconnect lines and word lines.
  - Enhances high-frequency clock distribution.
  - Low contact resistance to aluminum.
- **Cons:**
  - Extra deposition and high-temperature furnace/anneal steps $\to$ increases processing cost.
  - Mechanical stress at silicide-silicon interface $\to$ potential defect generation.
---
## 3D. Pass-Transistor Logic, Multiplexers & Encoders
### 1. Pass-Transistor Logic (PTL) Basics & XOR Gate
![[attachments/Pasted image 20261101221401.jpg]]
![[attachments/Pasted image 20261101221540.png]]
- **XOR Gate Synthesis:**
  - Equation: $F = A \overline{B} + \overline{A} B$.
  - PTL Implementation: Uses only 2 nMOS pass transistors + input inverters:
    - Pass $B$ when gate $= \overline{A}$.
    - Pass $\overline{B}$ when gate $= A$.
---
### 2. Arbitrary Logic Implementation with Pass Transistors (Q3.45)
- **Function:** $y = A \overline{B} + \overline{C} D$
- **Implementation:**
  - Transistor 1 (nMOS): Input $= A$, Gate $= \overline{B}$.
  - Transistor 2 (nMOS): Input $= D$, Gate $= \overline{C}$.
  - Common output node drives a CMOS inverter buffer to restore degraded voltage level ($V_{DD} - V_{tn} \to V_{DD}$).
![[attachments/Pasted image 20261101221744.png]]
---
### 3. Multiplexers (MUX) & Demultiplexers (DEMUX)
![[attachments/Pasted image 20261101213014.png]]
![[attachments/Pasted image 20261101215752.png]]
![[attachments/Pasted image 20261101213607.png]]
- **$2\times 1$ MUX using Transmission Gates:**
  - Two TGs connected to output $Y$.
  - TG0 passes $A$ when $S=0, \overline{S}=1$.
  - TG1 passes $B$ when $S=1, \overline{S}=0$.
- **$4\times 1$ MUX using Pass Transistors:**
  - 4 parallel paths, each having 2 series nMOS transistors controlled by $(S_0, S_1)$ combinations:
    $$Y = I_0 \overline{S_1} \overline{S_0} + I_1 \overline{S_1} S_0 + I_2 S_1 \overline{S_0} + I_3 S_1 S_0$$
- **$8\times 1$ MUX using Transmission Gates:**
  - 3-level binary tree: Level 1 (8 to 4, driven by $S_0$), Level 2 (4 to 2, driven by $S_1$), Level 3 (2 to 1, driven by $S_2$).
- **$1\times 4$ DEMUX using pMOS Pass Transistors:**
  - Single input routed to 4 outputs using pMOS switches activated by active-LOW control signals ($\overline{S_1}, \overline{S_0}$).
- **$8\times 3$ Priority Encoder:**
  - Encodes 8 active input lines into 3-bit binary code ($Y_2, Y_1, Y_0$) using an nMOS pass-transistor wired-OR matrix.
---
### 4. Regularity Calculation for $8\times 1$ MUX (Q3.52)
$$\mathbf{\text{Regularity} = \frac{\text{Total Transistors}}{\text{Designed Transistors}}}$$
- Total transistors in $8\times 1$ pass-transistor array: $8 \text{ paths} \times 3 \text{ transistors} = 24$ transistors.
- Distinct cells designed in detail: 1 basic pass-transistor switch.
- **Regularity:** $\frac{24}{1} = \mathbf{24}$.
---
## 3E. Bus Structures & Comparators
### 1. Processor Bus Architectures Comparison (Q3.53, Q3.54, Q3.57)
![[attachments/Pasted image 20261030181203.png]]
![[attachments/Pasted image 20261030181357.png]]

| Feature              | One-Bus Architecture | Two-Bus Architecture | Three-Bus Architecture|
| :---                 | :---                 | :---                 | :---                  |
| Bus Lines            | 1 shared bus         | 2 buses (Bus A, B)   | 3 buses (A, B, C)     |
| Silicon Area Cost    | Minimal              | Moderate             | Highest               |
| Multiplexing Logic   | High (time-shared)   | Moderate             | Low                   |
| Clock Cycles / Op    | 3 cycles             | 2 cycles             | 1 cycle (Single clock)|
| Throughput / Speed   | Slowest              | Intermediate         | Fastest               |
| Bottleneck           | Severe bus contention| Moderate             | No contention         |

- **Execution Sequence:**
  - **One-Bus:** Cycle 1: Fetch Operand A to ALU input latch. Cycle 2: Fetch Operand B. Cycle 3: Write result back to register.
  - **Two-Bus:** Cycle 1: Fetch Operand A and B simultaneously. Cycle 2: Execute ALU and write result back.
  - **Three-Bus:** Operand A on Bus A, Operand B on Bus B $\to$ ALU executes $\to$ result returned via Bus C **all in the same single clock cycle**.
---
### 2. CMOS Magnitude Comparator (Q3.55, Q3.56)
![[attachments/Pasted image 20261031182128.png]]
![[attachments/Pasted image 20261031182200.png]]
- **Architecture:** Iterative cascade of identical 1-bit comparator cells evaluated from MSB ($i=n-1$) down to LSB ($i=0$).
- **Inputs & Outputs for stage $i$:**
  - Bit inputs: $A_i, B_i$.
  - Cascade inputs from stage $i+1$: $C_{i+1}$ (indicates $A > B$), $D_{i+1}$ (indicates $A < B$).
  - Cascade outputs to stage $i-1$: $C_i, D_i$.
#### Logic Equations:
$$\mathbf{C_i = C_{i+1} + \overline{D_{i+1}} \cdot A_i \cdot \overline{B_i}} \quad (\text{Propagates / Generates } A > B)$$
$$\mathbf{D_i = D_{i+1} + \overline{C_{i+1}} \cdot \overline{A_i} \cdot B_i} \quad (\text{Propagates / Generates } A < B)$$
$$\mathbf{E_i = \overline{C_i + D_i}} \quad (\text{Equality } A = B)$$
- **Operation Principle:**
  - If any higher-order stage finds an inequality ($C_{i+1}=1$ or $D_{i+1}=1$), it ripples straight through to the final output.
  - The current bit pair $(A_i, B_i)$ is evaluated only if all previous higher bits were equal ($C_{i+1} = D_{i+1} = 0$).


## Core Structure of a VHDL Code

A complete VHDL design entity consists of three mandatory structural blocks:

  

- **Library and Use Clause:** Specifies the pre-compiled packages containing standard data types, operators, and logic systems. The standard IEEE package `IEEE.STD_LOGIC_1164.ALL` is required for standard digital logic values (`'0'`, `'1'`, `'Z'`, `'X'`).
    
      
    
- **Entity Declaration:** Defines the external hardware interface (black box view) of the component. It lists all input and output pins, their directions (`in`, `out`, `inout`, `buffer`), and their data types via the `port` statement.
    
      
    
- **Architecture Body:** Specifies the internal logic, circuit functionality, and implementation of the entity. An architecture can be modeled using:
    
      
    - _Dataflow style:_ Uses concurrent signal assignments and Boolean equations (e.g., `when-else`).
        
          
        
    - _Behavioral style:_ Uses sequential algorithms within `process` blocks (e.g., `if-then-else`, `case-when`).
        
          
        
    - _Structural style:_ Instantiates and interconnects lower-level sub-components using internal signals.
        
          
        

## 1. Half Adder

### Truth Table and Logic Equations

|**A**|**B**|**Sum (S)**|**Carry (C)**|
|---|---|---|---|
|0|0|0|0|
|0|1|1|0|
|1|0|1|0|
|1|1|0|1|

- **Boolean Expressions:**
    
      
    - $\text{Sum} = A \oplus B$
        
          
        
    - $\text{Carry} = A \cdot B$
        
          
        

### VHDL Code

VHDL

```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity half_adder is
    Port ( 
        A     : in  STD_LOGIC;
        B     : in  STD_LOGIC;
        Sum   : out STD_LOGIC;
        Carry : out STD_LOGIC
    );
end half_adder;

architecture Dataflow of half_adder is
begin
    Sum   <= A xor B;
    Carry <= A and B;
end Dataflow;
```

## 2. Full Adder Circuit

### Truth Table and Logic Equations

|**A**|**B**|**Cin​**|**Sum (S)**|**Cout​**|
|---|---|---|---|---|
|0|0|0|0|0|
|0|0|1|1|0|
|0|1|0|1|0|
|0|1|1|0|1|
|1|0|0|1|0|
|1|0|1|0|1|
|1|1|0|0|1|
|1|1|1|1|1|

- **Boolean Expressions:**
    
      
    - $\text{Sum} = A \oplus B \oplus C_{in}$
        
          
        
    - $C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B)) = (A \cdot B) + (B \cdot C_{in}) + (A \cdot C_{in})$
        
          
        

### VHDL Code (Dataflow Modeling)

VHDL

```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity full_adder is
    Port ( 
        A     : in  STD_LOGIC;
        B     : in  STD_LOGIC;
        Cin   : in  STD_LOGIC;
        Sum   : out STD_LOGIC;
        Cout  : out STD_LOGIC
    );
end full_adder;

architecture Dataflow of full_adder is
begin
    Sum  <= A xor B xor Cin;
    Cout <= (A and B) or (Cin and (A xor B));
end Dataflow;
```

## 3. 4×1 Multiplexer (4:1 MUX)

### Function and Truth Table

- Select lines $S_1, S_0$ route one of the four data inputs ($I_0, I_1, I_2, I_3$) to output $Y$.
    
      
    

|**S1​**|**S0​**|**Output (Y)**|
|---|---|---|
|0|0|$I_0$|
|0|1|$I_1$|
|1|0|$I_2$|
|1|1|$I_3$|

### VHDL Code Using `when` Logic (Conditional Signal Assignment)

VHDL

```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1 is
    Port ( 
        I   : in  STD_LOGIC_VECTOR (3 downto 0); -- Inputs: I(0), I(1), I(2), I(3)
        Sel : in  STD_LOGIC_VECTOR (1 downto 0); -- Select lines: Sel(1 downto 0)
        Y   : out STD_LOGIC
    );
end mux4to1;

architecture Conditional of mux4to1 is
begin
    Y <= I(0) when (Sel = "00") else
         I(1) when (Sel = "01") else
         I(2) when (Sel = "10") else
         I(3) when (Sel = "11") else
         '0';
end Conditional;
```

## 4. 8×1 Multiplexer (8:1 MUX)

### Function Table

|**S2​**|**S1​**|**S0​**|**Output (Y)**|
|---|---|---|---|
|0|0|0|$I_0$|
|0|0|1|$I_1$|
|0|1|0|$I_2$|
|0|1|1|$I_3$|
|1|0|0|$I_4$|
|1|0|1|$I_5$|
|1|1|0|$I_6$|
|1|1|1|$I_7$|

### VHDL Code (Selected Signal Assignment / with-select)

VHDL

```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux8to1 is
    Port ( 
        I   : in  STD_LOGIC_VECTOR (7 downto 0);
        Sel : in  STD_LOGIC_VECTOR (2 downto 0);
        Y   : out STD_LOGIC
    );
end mux8to1;

architecture Behavioral of mux8to1 is
begin
    with Sel select
        Y <= I(0) when "000",
             I(1) when "001",
             I(2) when "010",
             I(3) when "011",
             I(4) when "100",
             I(5) when "101",
             I(6) when "110",
             I(7) when "111",
             '0'  when others;
end Behavioral;
```

## 5. HDL Test Bench Concepts and Configurations

### Concept of an HDL Test Bench

- **Definition:** An HDL test bench is a dedicated simulation environment written in HDL used to verify the functional correctness of a hardware design module (Device Under Test / DUT) without fabricating physical silicon.
    
      
    
- **Portless Entity:** A test bench entity contains no hardware input or output pins (`entity testbench is end entity;`). It serves as an isolated test wrapper.
    
      
    
- **Instantiating the DUT:** The Design Under Test is instantiated as a component inside the test bench architecture.
    
      
    
- **Stimulus Generation:** Test benches generate clock cycles, reset pulses, and dynamic input vectors using simulation constructs (`wait for`, delay operators, loops) not meant for hardware synthesis.
    
      
    
- **Response Verification:** Outputs produced by the DUT are monitored, logged, or automatically evaluated against expected golden vectors.
    
      
    

```
       +-------------------------------------------------------+
       |                  HDL Test Bench Wrapper               |
       |                                                       |
       |   +-------------------+       +-------------------+   |
       |   | Stimulus / Vector | ----> | Device Under Test |   |
       |   |    Generator      |       |    (DUT / UUT)    |   |
       |   +-------------------+       +-------------------+   |
       |                                         |             |
       |                                         v             |
       |                               +-------------------+   |
       |                               | Response Monitor  |   |
       |                               |   & Verification  |   |
       |                               +-------------------+   |
       +-------------------------------------------------------+
```

### Off-line vs. On-line Test Bench Configurations

#### 1. Off-line Test Bench Configuration

- **Working Principle:**
    
      
    - Stimulus vectors are generated independently prior to simulation and stored in external memory or data files (e.g., text/hex files).
        
          
        
    - The test bench reads these pre-computed vectors sequentially, feeds them into the DUT, and records the raw output vectors into an external output file or waveform dump.
        
          
        
    - Verification takes place **after** the simulation run is completely finished using external comparison scripts (e.g., Python, MATLAB, diff utilities) against a golden reference file.

- **Characteristics:**
    
      
    - High execution speed during simulation because no runtime checking logic runs concurrently.
        
          
        
    - Inflexible: cannot dynamically adjust input stimuli based on the intermediate internal state of the DUT.
        
          
        

#### 2. On-line (Interactive / Closed-Loop) Test Bench Configuration

- **Working Principle:**
    
      
    - Stimulus generation and functional response evaluation happen **concurrently** during active simulation.
        
          
        
### VHDL Test Bench Code Example (Full Adder DUT)

VHDL

```
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_full_adder is
-- Test bench entities have no external ports
end tb_full_adder;

architecture Behavioral of tb_full_adder is

    -- 1. Component declaration of the Device Under Test (DUT)
    component full_adder
        Port ( 
            A     : in  STD_LOGIC;
            B     : in  STD_LOGIC;
            Cin   : in  STD_LOGIC;
            Sum   : out STD_LOGIC;
            Cout  : out STD_LOGIC
        );
    end component;

    -- 2. Internal test signals connected to the DUT
    signal A_tb    : STD_LOGIC := '0';
    signal B_tb    : STD_LOGIC := '0';
    signal Cin_tb  : STD_LOGIC := '0';
    signal Sum_tb  : STD_LOGIC;
    signal Cout_tb : STD_LOGIC;

begin

    -- 3. Instantiate the DUT
    uut: full_adder 
        port map (
            A    => A_tb,
            B    => B_tb,
            Cin  => Cin_tb,
            Sum  => Sum_tb,
            Cout => Cout_tb
        );

    -- 4. Stimulus process
    stim_proc: process
    begin
        -- Vector 0: 0 + 0 + 0 = Sum: 0, Cout: 0
        A_tb <= '0'; B_tb <= '0'; Cin_tb <= '0'; wait for 20 ns;

        -- Vector 1: 0 + 0 + 1 = Sum: 1, Cout: 0
        A_tb <= '0'; B_tb <= '0'; Cin_tb <= '1'; wait for 20 ns;

        -- Vector 2: 0 + 1 + 0 = Sum: 1, Cout: 0
        A_tb <= '0'; B_tb <= '1'; Cin_tb <= '0'; wait for 20 ns;

        -- Vector 3: 0 + 1 + 1 = Sum: 0, Cout: 1
        A_tb <= '0'; B_tb <= '1'; Cin_tb <= '1'; wait for 20 ns;

        -- Vector 4: 1 + 0 + 0 = Sum: 1, Cout: 0
        A_tb <= '1'; B_tb <= '0'; Cin_tb <= '0'; wait for 20 ns;

        -- Vector 5: 1 + 0 + 1 = Sum: 0, Cout: 1
        A_tb <= '1'; B_tb <= '0'; Cin_tb <= '1'; wait for 20 ns;

        -- Vector 6: 1 + 1 + 0 = Sum: 0, Cout: 1
        A_tb <= '1'; B_tb <= '1'; Cin_tb <= '0'; wait for 20 ns;

        -- Vector 7: 1 + 1 + 1 = Sum: 1, Cout: 1
        A_tb <= '1'; B_tb <= '1'; Cin_tb <= '1'; wait for 20 ns;

        -- Terminate simulation
        wait;
    end process;

end Behavioral;
```

## 6. Comparison: Verilog vs. VHDL

|**Feature / Metric**|**VHDL (VHSIC Hardware Description Language)**|**Verilog HDL**|
|---|---|---|
|**Origin & Standardization**|Commissioned by the U.S. Department of Defense; standardized under IEEE 1076.|Developed by Gateway Design Automation; standardized under IEEE 1364 (later merged into SystemVerilog IEEE 1800).|
|**Syntactic Ancestry**|Derived from **Ada** and **Pascal**; highly verbose and strictly structured.|Derived from the **C programming language**; compact, concise, and familiar to software programmers.|
|**Type Strictness**|**Strongly typed:** Conversions between `integer`, `std_logic_vector`, `signed`, and `unsigned` require explicit casting functions. Errors are flagged at compile time.|**Weakly typed:** Supports automatic implicit casting and truncation across integer and vector assignments.|
|**Case Sensitivity**|**Case-insensitive:** `Signal_A` and `signal_a` refer to the identical object.|**Case-sensitive:** `Wire_A` and `wire_a` denote two completely distinct signals.|
|**Design Hierarchy**|Clear separation between interface (`entity`) and implementation (`architecture`). One entity can have multiple architectures.|Single consolidated module wrapper (`module ... endmodule`) containing both pin declarations and logic.|
|**System-Level Modeling**|Excellent high-level abstract data types, records, enumeration, and user-defined package support.|Historically weaker abstract types in standard Verilog (addressed later in SystemVerilog).|
|**Low-Level Gate Modeling**|Does not have built-in switch-level primitives; requires explicit gate-level component instantiations.|Built-in native gate and transistor-level switch primitives (`and`, `or`, `nand`, `cmos`, `pmos`, `tran`).|
|**Industry Adoption**|Predominant in European industries, aerospace, defense, military, telecommunications, and FPGA designs.|Predominant in North American commercial semiconductor, ASIC/VLSI design, and chip fabrication houses.|