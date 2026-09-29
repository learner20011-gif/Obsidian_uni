
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

