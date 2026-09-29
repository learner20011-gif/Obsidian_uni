
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

```

