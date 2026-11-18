


### overflow: 
Assume a **4-bit signed box** (Two's Complement), which can only hold numbers from **-8 to +7**.

### Addition Examples

- **Overflow (`5 + 4 = 9`):** `9` is too big for the box.
    
    - `0101` (+5) + `0100` (+4) = `1001` (**-7**)
        
    - **Why it overflowed:** Two positives gave a **negative** answer.
        
- **No Overflow (`3 + 4 = 7`):** `7` fits right at the limit.
    
    - `0011` (+3) + `0100` (+4) = `0111` (**+7**)
        
    - **Why it's fine:** Two positives gave a **positive** answer.
        

### Subtraction Examples

_(Computers subtract by flipping the second number's sign and adding: `A - B` becomes `A + (-B)`)_

- **Overflow (`-6 - 4` → `-6 + (-4) = -10`):** `-10` is too small for the box.
    
    - `1010` (-6) + `1100` (-4) = `1 0110` → drop extra carry → `0110` (**+6**)
        
    - **Why it overflowed:** Two negatives gave a **positive** answer.
        
- **No Overflow (`5 - 3` → `5 + (-3) = 2`):** `2` fits easily.
    
    - `0101` (+5) + `1101` (-3) = `1 0010` → drop extra carry → `0010` (**+2**)
        
    - **Why it's fine:** Opposite signs (`+` and `-`) **never** overflow.
- **Positive + Positive = Negative** → Overflow
    
- **Negative + Negative = Positive** → Overflow
    
- **Positive + Negative** → Never overflows (the sign is always accurate)
-         unique case (alu_op)
            OP_ADD: begin
                result   = add_ext[WIDTH-1:0];
                carry    = add_ext[WIDTH];
                overflow = (a[WIDTH-1] == b[WIDTH-1]) && (result[WIDTH-1] != a[WIDTH-1]);
            end

            OP_SUB: begin
                result   = sub_ext[WIDTH-1:0];
                carry    = sub_ext[WIDTH]; // 1 indicates unsigned borrow (a < b)
                overflow = (a[WIDTH-1] != b[WIDTH-1]) && (result[WIDTH-1] != a[WIDTH-1]);
            end