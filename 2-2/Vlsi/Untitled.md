
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