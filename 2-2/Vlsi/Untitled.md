
```
LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY Full_Adder IS
    PORT (
        a, b, cin : IN  std_logic;
        s, cout   : OUT std_logic
    );
END Full_Adder;

ARCHITECTURE dataflow OF Full_Adder IS
BEGIN
    s    <= a XOR b XOR cin;
    cout <= (a AND b) OR (a AND cin) OR (b AND cin);
END dataflow;






LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY mux8to1 IS
    PORT (
        a, b, c, d, e, f, g, h : IN  std_logic;
        sel                    : IN  std_logic_vector(2 DOWNTO 0);
        y                      : OUT std_logic
    );
END mux8to1;

ARCHITECTURE mux_arch OF mux8to1 IS
BEGIN
    y <= a WHEN sel = "000" ELSE
         b WHEN sel = "001" ELSE
         c WHEN sel = "010" ELSE
         d WHEN sel = "011" ELSE
         e WHEN sel = "100" ELSE
         f WHEN sel = "101" ELSE
         g WHEN sel = "110" ELSE
         h;
END mux_arch;





--------------------------------------------------------------------------------
-- Standard IEEE Library Declaration
--------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL; -- Imports standard multi-value logic types (STD_LOGIC)

--------------------------------------------------------------------------------
-- Entity Declaration (Empty Entity)
-- A testbench models the testing environment itself, not a physical chip.
-- Because of this, it has NO external inputs or outputs (no port list).
--------------------------------------------------------------------------------
entity tb_half_adder is
end entity tb_half_adder;

--------------------------------------------------------------------------------
-- Architecture Body
-- Contains the testing logic, signal wiring, device instantiation, and stimuli.
--------------------------------------------------------------------------------
architecture sim of tb_half_adder is

    -- Step 1: Internal Signal Declarations (Virtual Wires)
    -- These signals act as physical jumper wires inside the test environment.
    
    -- Inputs to the DUT: Initialized to '0' to avoid undefined states at time 0 ns
    
    signal a_in      : STD_LOGIC := '0'; -- Drives port 'a' of the half adder
    signal b_in      : STD_LOGIC := '0'; -- Drives port 'b' of the half adder
    
    -- Outputs from the DUT: These capture the results produced by the circuit
    signal sum_out   : STD_LOGIC;        -- Reads the 'sum' output
    signal carry_out : STD_LOGIC;        -- Reads the 'carry' output

begin

    ----------------------------------------------------------------------------
    -- Step 2: Device Under Test (DUT / UUT) Instantiation
    -- Places one instance of the half_adder design into this testbench.
    -- 'work' refers to the current project working library where half_adder lives.
    ----------------------------------------------------------------------------
    uut: entity work.half_adder
        port map (
            a     => a_in,       -- Connects test signal a_in to half_adder input 'a'
            b     => b_in,       -- Connects test signal b_in to half_adder input 'b'
            sum   => sum_out,    -- Connects half_adder output 'sum' to sum_out
            carry => carry_out   -- Connects half_adder output 'carry' to carry_out
        );

    ----------------------------------------------------------------------------
    -- Step 3: Stimulus Process (Signal Generator)
    -- Runs sequentially to apply all 4 binary input combinations over time.
    ----------------------------------------------------------------------------
    stim_proc: process
    begin
        -- Case 1: 0 + 0 = Sum: 0, Carry: 0
        a_in <= '0'; 
        b_in <= '0'; 
        wait for 10 ns; -- Holds inputs stable for 10 ns so the output settles

        -- Case 2: 0 + 1 = Sum: 1, Carry: 0
        a_in <= '0'; 
        b_in <= '1'; 
        wait for 10 ns; -- Holds inputs for another 10 ns

        -- Case 3: 1 + 0 = Sum: 1, Carry: 0
        a_in <= '1'; 
        b_in <= '0'; 
        wait for 10 ns; -- Holds inputs for another 10 ns

        -- Case 4: 1 + 1 = Sum: 0, Carry: 1
        a_in <= '1'; 
        b_in <= '1'; 
        wait for 10 ns; -- Holds inputs for another 10 ns

        -- Halts execution: A plain 'wait;' with no condition pauses the process
        -- forever. Without this, the process loops back to the top indefinitely.
        wait; 
    end process stim_proc;

end architecture sim;

```

| **Feature / Aspect**        | **VHDL**                                                                                                                     | **Verilog**                                                                                                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Origin & Ancestry**       | Derived from **Ada** and Pascal; developed by the U.S. Department of Defense (IEEE 1076).                                    | Derived from the **C** programming language; developed by Gateway Design Automation (IEEE 1364).                                |
| **Case Sensitivity**        | **Case-insensitive** (`Sum` and `sum` refer to the same identifier).                                                         | **Case-sensitive** (`Sum` and `sum` are two completely different identifiers).                                                  |
| **Typing System**           | **Strongly typed**; strict type rules require explicit conversion functions between types (e.g., `std_logic`, `integer`).    | **Weakly typed**; implicit type conversion and flexible bit-vector handling.                                                    |
| **Syntax Complexity**       | Verbose and highly structured; requires explicit design unit separation (`entity`, `architecture`, `package`).               | Compact, terse, and familiar to C-programmers; encapsulated directly within `module ... endmodule`.                             |
| **Structural Design Style** | Explicit separation of interface (`entity`) and implementation (`architecture`). One entity can have multiple architectures. | Single declaration block where inputs, outputs, and internal behavior reside inside the same `module`.                          |
| **Data Types**              | Highly extensible with rich user-defined types, enumerated types, and records.                                               | Fixed set of predefined types: `wire`, `reg`, `integer`, `time`, etc.                                                           |
| **Learning Curve**          | Steeper learning curve due to verbosity and strict compiler checks, but catches semantic bugs earlier.                       | Gentler learning curve for engineers familiar with C; faster prototyping, but easier to introduce subtle simulation mismatches. |
| **Industry Usage**          | Widely used in aerospace, defense, telecom, and European industries.                                                         | Predominant in commercial ASIC, consumer electronics, and semiconductor firms (especially in the US and Asia).                  |
![[Pasted image 20260930020128.png]]

![[Pasted image 20260930020210.png]]

### 1. Dynamic RAM (DRAM) Storage Cells

- **3-Transistor (3T) Dynamic Cell:**
    
      
    - **Circuit:** Uses three transistors: $T_1$ (write switch), $T_2$ (storage device), and $T_3$ (read switch).
        
          
        
    - **Storage Node:** Holds data dynamically as an electric charge on the internal gate capacitance ($C_g$) of $T_2$.
        
          
        
    - **Write Operation:** Write line ($WR$) goes high during $\phi_1$, turning $T_1$ ON to transfer data from the shared bus directly onto $C_g$.
        
          
        
    - **Read Operation:** Read line ($RD$) turns $T_3$ ON; if a logic `1` is stored, $T_2$ conducts, pulling the precharged bus down to ground (inverted data readout).
        
          
        
    - **Readout Type:** Non-destructive; reading does not wipe the stored gate charge.
        
          
        
    - **Layout Footprint:** Occupies roughly $1000\,\lambda^2$ (or $500\lambda^2$ in optimized cells), allowing $>48\text{ kbits}$ (or $\approx 5\text{ kbits}$ per $16\text{ mm}^2$ chip).
        
          
        
- **1-Transistor (1T) Dynamic Cell:**
    
      
    - **Circuit:** Uses exactly one access transistor ($M_1$) and one storage capacitor ($C_s$).
        
          
        
    - **Storage Capacitor Construction:** Formed using a polysilicon plate over diffusion connected to $V_{DD}$ to obtain sufficient capacitance ($\approx 0.125\text{ pF}$) within a minimal area.
        
          
        
    - **Write Operation:** Activating the Row-select line turns $M_1$ ON, driving $C_s$ to $V_{DD}$ for a `1` or Ground for a `0`.
        
          
        
    - **Read Operation:** Precharging the bit line to $V_{DD}/2$ and turning $M_1$ ON causes charge-sharing between $C_s$ and bit line capacitance ($C_{BL}$), detected via a sense amplifier.
        
          
        
    - **Readout Type:** Destructive; every read cycle dumps the charge and requires an immediate rewrite.
        
          
        
    - **Layout Footprint:** Requires only $\approx 200\,\lambda^2$ ($1250\ \mu\text{m}^2$ at $\lambda = 2.5\ \mu\text{m}$), accommodating up to $128\text{ kbits}$ of raw capacity on a $4\text{ mm} \times 4\text{ mm}$ die.
        
          
        
    - **Volatility:** Leakage currents drain $C_s$ in $\le 1\text{ to }2\text{ ms}$, requiring periodic refresh cycles.
        
          
        

### 2. Pseudo-Static RAM / Register Cell

- **Operating Principle:**
    
      
    - Built from two cascaded inverters with a gated feedback loop controlled by a two-phase clock ($\phi_1, \phi_2$).
        
          
        
    - Uses dynamic gate storage during active cycles, but acts static because it automatically refreshes its own data every clock cycle via feedback.
        
          
        
- **Phase-by-Phase Operation:**
    
      
    - **Write / Read ($\phi_1$):** Input data enters on $WR \cdot \phi_1$; output is placed onto the bus on $RD \cdot \phi_1$.
        
          
        
    - **Refresh ($\phi_2$):** Feedback switch $T_3$ closes, feeding the inverted-and-restored output of Inverter 2 back to the gate of Inverter 1 to replenish leaked charge.
        
          
        
- **Essential Design Constraints:**
    
      
    - $WR$ and $RD$ are mutually exclusive and must never activate at the same time.
        
          
        
    - Reading must never occur during clock phase $\phi_2$ to prevent destructive charge sharing between the bus line and storage node.
        
          
        
    - Cells must be layout-stackable horizontally and vertically, allowing bus lines to route straight through.
        
          
        
- **Area & Power Consumption:**
    
      
    - Single-bus area is $\approx 1750\lambda^2$ ($\approx 10{,}000\ \mu\text{m}^2$ at $\lambda = 2.5\ \mu\text{m}$), yielding $\approx 1.4\text{ kbits}$ on a $4\text{ mm} \times 4\text{ mm}$ die.
        
          
        
    - With an $8:1$ ($90\text{ k}\Omega$) and $4:1$ ($45\text{--}50\text{ k}\Omega$) inverter pair, average current draw is $\approx 80\ \mu\text{A}$ at $5\text{ V}$.
        
          
        
    - Dissipation per bit is $400\ \mu\text{W}$, leading to $\approx 560\text{ mW}$ total power for a $1.4\text{ kbit}$ array.
        
          
        

### 3. Dynamic Storage Elements & Shifters

- **Inverting Dynamic Cell:**
    
      
    - Comprises a pass transistor (nMOS, 3 transistors total) or transmission gate (CMOS, 4 transistors total) feeding a single inverter.
        
          
        
    - Data clocked in during $\phi$ charges $C_g$, presenting a stable complemented output ($\overline{V_{\text{in}}}$) until $C_g$ discharges.
        
          
        
- **Non-Inverting Dynamic Cell:**
    
      
    - Places two clocked inverting stages in series.
        
          
        
    - First stage clocks in data during $\phi_1$; second stage samples and inverts it again during $\phi_2$, outputting the true (uncomplemented) bit.
        
          
        
- **4-Bit Dynamic Shift Register:**
    
      
    - Connects 4 bit-cells (8 inverters total) in series using alternating non-overlapping clocks ($\phi_1$ and $\phi_2$).
        
          
        
    - Data steps rightward through the stages one inverter pair per clock period ($\phi_1 \rightarrow \phi_2$).
        
          
        

### 4. N-Bit Iterative CMOS Comparator

- **Inputs & Outputs per Cell ($i$):**
    
      
    - **Local Bit Inputs:** $A_i$ and $B_i$.
        
          
        
    - **Cascading Inputs from Higher Stage ($i+1$):** $C_{i+1}$ ($A > B$) and $D_{i+1}$ ($A < B$).
        
          
        
    - **Stage Outputs:** $C_i$ ($A > B$) and $D_i$ ($A < B$).
        
          
        
- **Truth Table Logic:**
    
      
    - **Higher Bit Precedence:** If $C_{i+1}D_{i+1} = 10$, then $C_iD_i = 10$; if $C_{i+1}D_{i+1} = 01$, then $C_iD_i = 01$ (local inputs are "Don't Care").
        
          
        
    - **Tie-Breaking ($C_{i+1}D_{i+1} = 00$):**
        
          
        - $A_i = B_i \implies C_iD_i = 00$ (equality preserved).
            
              
            
        - $A_i = 1, B_i = 0 \implies C_iD_i = 10$ ($A > B$).
            
              
            
        - $A_i = 0, B_i = 1 \implies C_iD_i = 01$ ($A < B$).
            
              
            

### 5. Memory Sizing & Unit Conversion Summary

- **Binary vs. Decimal Kilo:**
    
      
    - **Binary Kilo ($1024 = 2^{10}$):** Used for physical memory addressing and hardware bit capacities.
        
          
        
    - **Decimal Kilo ($1000 = 10^3$):** Used for rough power estimations ($1.4\text{ kbits} \times 1000 = 1400\text{ bits} \implies 1400 \times 400\ \mu\text{W} = 560\text{ mW}$).
        
          
        
- **Worked Chip Area Problem (10 kbits of 3T DRAM):**
    
      
    - Bit cell area = $500\lambda^2 = 500 \times (2.5\ \mu\text{m})^2 = 3125\ \mu\text{m}^2$.
        
          
        
    - Reference $4\text{ mm} \times 4\text{ mm}$ ($16\text{ mm}^2$) chip holds:
        
          
        
        $$\frac{16 \times 10^{-6}\text{ m}^2}{3125 \times 10^{-12}\text{ m}^2} = 5120\text{ bits} = \frac{5120}{1024} = 5\text{ kbits} \text{[cite: 5]}$$
        
    - Area required to hold $10\text{ kbits}$:
        
        $$\text{Area} = \frac{10\text{ kbits}}{5\text{ kbits}} \times 16\text{ mm}^2 = \mathbf{32\text{ mm}^2} = \mathbf{5{,}120{,}000\lambda^2} \text{[cite: 5]}$$