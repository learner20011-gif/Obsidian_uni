
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