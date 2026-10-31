![[Pasted image 20261030144952.png]]![[Pasted image 20261030145836.png|512]]![[Pasted image 20261030145848.png]]![[Pasted image 20261030152056.png]]

![[Pasted image 20261030181203.png]]
![[Pasted image 20261030181357.png]]
![[This circuit is a pass-transistor Full Adder.png]]
![[Pasted image 20261030202149.png|661]]
![[Pasted image 20261030204115.png]]
![[Pasted image 20261030215042.png]]
![[Pasted image 20261030215823.png|626]]![[Pasted image 20261030222543.png|641]]![[Pasted image 20261031002811.png|642]]![[Pasted image 20261031010923.png|537]]![[Pasted image 20261031013206.png|605]]![[Pasted image 20261031123708.png|650]]![[Pasted image 20261031132224.png|599]]![[Pasted image 20261031132238.png|634]]![[Pasted image 20261031132423.png|471]]![[Pasted image 20261031181349.png|521]]![[Pasted image 20261031181402.png|516]]![[Pasted image 20261031181842.png|506]]![[Pasted image 20261031182128.png|522]]![[Pasted image 20261031182200.png]]
#### 1. Requirements for a 4-Bit Shifter

- **Purpose:** Shifts data left or right by 0 to 3 places, often wrapping around from one end to the other.
    
      
    
- **Inputs:** Takes data from a 4-line parallel bus.
    
      
    
- **Outputs:** Provides data on 4 output lines.
    
      
    
- **Function:** Connects the inputs to the outputs with any shift amount from 0 to 3 positions.
    
      
    

#### 2. Problems with Using a Crossbar Switch

- **Too Complex (Overkill):** It uses 16 individual switches where any input can connect to any output, which is far more than needed.
    
      
    
- **Risk of Short Circuit:** If all switches close at the same time, all inputs short together.
    
      
    
- **Hard to Control:** Operating 16 separate control signals is complicated and expensive.
    
      
    

#### 3. How to Solve / Reduce It (Barrel Shifter)

- **Group the Switches:** Instead of controlling 16 switches individually, group the gates into 4 control lines.
    
      
    
- **Shift Control:** Each group corresponds to a specific shift amount: 0, 1, 2, or 3 bits.
    
      
    
- **Result:** This simpler, safer design is called a **Barrel Shifter**.
    
      
    

#### 4. What is Regularity?

- **Definition:** A measure of how much a chip design reuses the same standard parts to save design time and effort.
    
      
    
- **Goal:** It should be as high as possible.
    
      
    
- Formula:
    
      
    

$$\text{Regularity} = \frac{\text{Total number of transistors on chip}}{\text{Number of transistor circuits designed in detail}}$$

- **Example:** In a $4 \times 4$ barrel shifter, there are 16 transistors made by repeating just 1 basic cell design, giving a regularity of $\frac{16}{1} = 16$.

#### 1. XOR Operation

- **Full Adder Sum:**
    
      
    

$$Sum = A \oplus B \oplus C_{in} \text{[cite: 5]}$$

- **Evaluation with $C_{in} = 0$:**
    
      
    

$$Sum = A \oplus B \oplus 0 = A \oplus B$$

#### 2. XNOR Operation

- **Full Adder Sum:**
    
      
    

$$Sum = A \oplus B \oplus C_{in} \text{[cite: 5]}$$

- **Evaluation with $C_{in} = 1$:**
    
      
    

$$Sum = A \oplus B \oplus 1 = (A \oplus B) \cdot 0 + \overline{(A \oplus B)} \cdot 1 = \overline{A \oplus B}$$

#### 3. AND Operation

- **Full Adder Carry-Out:**
    
      
    

$$C_{out} = A \cdot B + C_{in} \cdot (A \oplus B) \text{[cite: 5, 6]}$$

- **Evaluation with $C_{in} = 0$:**
    
      
    

$$C_{out} = A \cdot B + 0 \cdot (A \oplus B) = A \cdot B$$

#### 4. OR Operation

- **Full Adder Carry-Out:**
    
      
    

$$C_{out} = A \cdot B + C_{in} \cdot (A \oplus B) \text{[cite: 5, 6]}$$

- **Evaluation with $C_{in} = 1$:**
    
      
    

$$C_{out} = A \cdot B + 1 \cdot (A \oplus B)$$

$$C_{out} = A B + (A \overline{B} + \overline{A} B)$$

$$C_{out} = A(B + \overline{B}) + \overline{A} B = A + \overline{A} B = A + B$$

#### 5. Binary Addition

- **Condition:** Set $C_{in} = 0$ with operands $A$ and $B$.
    
      
    
- **Equations for bit $k$:**
    
      
    

$$S_k = A_k \oplus B_k \oplus C_{k-1} \text{[cite: 5]}$$

$$C_k = A_k B_k + C_{k-1}(A_k \oplus B_k) \text{[cite: 5, 6]}$$

- **Result:**
    
      
    

$$\text{Result} = A + B$$

#### 6. Binary Subtraction (Two's Complement)

- **Identity:** Subtracting $B$ is equivalent to adding its two's complement:
    
      
    

$$A - B = A + (-B)$$

- **Two's Complement Formulation:**
    
      
    

$$-B = \overline{B} + 1$$

- **Hardware Mapping:** Invert input $B$ to obtain $\overline{B}$, and set initial carry-in $C_{in} = 1$:
    

$$Sum = A + \overline{B} + C_{in} = A + \overline{B} + 1 = A - B$$


#### **Figure 8.12 shows how a 4-bit adder is modified into a complete 4-bit Arithmetic Logic Unit (ALU)** using simple switches instead of building separate logic circuits.

  

- **4 Adder Elements:**
    
      
    - Four 1-bit full-adder blocks are stacked together, one for each bit position ($0$ to $3$).
        
          
        
- **Input Conditioning on $B$:**
    
      
    - Each $B$ input passes through an inverter with a switch.
        
          
        
    - This allows the circuit to feed either the original bit $B$ (for addition and logic) or the inverted bit $\overline{B}$ (for two's complement subtraction).
        
          
        
- **Carry-Line Switching:**
    
      
    - Switches are placed along the carry path between the adder blocks.
        
          
        
    - **In Arithmetic Mode:** The switches connect the carry lines together, letting carries ripple from one stage to the next for normal multi-bit addition or subtraction.
        
          
        
    - **In Logic Mode:** The switches isolate the carry lines and force them to fixed values ($0$ or $1$) so that each cell independently computes logic functions.
        
          
        
- **Output Selection Switches:**
    
      
    - Switches on the outputs allow the ALU to pick either the sum line ($S_k$) or the carry line ($C_k$) as the final result bit:
        
          
        - **Sum Output ($S_k$):** Delivers Addition, Subtraction, **XOR** (when carry is held at $0$), or **XNOR** (when carry is held at $1$).
            
              
            
        - **Carry Output ($C_k$):** Delivers **AND** (when carry is held at $0$) or **OR** (when carry is held at $1$).
    - **Arithmetic Reason ($A - B$):**
    
    - Subtraction is defined in hardware as $A - B$.
        
    - In two's complement arithmetic:
        

$$A - B = A + \overline{B} + 1$$

#### Inverting Dynamic Storage Cell

- **How it works:** A clock signal ($\phi$) opens a switch (an nMOS pass transistor or CMOS transmission gate) to pass input data, which charges the gate capacitance ($C_g$) of an inverter.
    
      
    
- **Storage mechanism:** The charge trapped on the gate capacitor temporarily holds the voltage, keeping the inverted output ($\overline{V_{in}}$) stable until charge leakage occurs.
    
      
    
- **Transistor count:** Requires **3 transistors** in nMOS (1 pass switch + 2 in the inverter) and **4 transistors** in CMOS (2 for the transmission gate + 2 for the inverter).
    
      
    

#### Non-Inverting Dynamic Storage Cell

- **How it works:** Cascades two inverting stages back-to-back using a two-phase non-overlapping clock ($\phi_1$ and $\phi_2$).
    
      
    
- **Step 1 ($\phi_1$):** Input data charges the first capacitor ($C_{g1}$), and the first inverter flips the signal.
    
      
    
- **Step 2 ($\phi_2$):** The inverted signal passes to the second stage, charging capacitor ($C_{g2}$); the second inverter flips it back to its original (uncomplemented) form.
    
      
    

#### 4-Bit Dynamic Shift Register (nMOS)

- **Architecture:** Formed by linking four non-inverting cells (Bit 3 down to Bit 0) in series.
    
      
    
- **Data movement:** Alternating clock pulses ($\phi_1$ and $\phi_2$) move data stage by stage to the right without collisions.
    
      
    
- **Timing:** Data is clocked into the first half of a bit during $\phi_1$ and transferred to the second half during $\phi_2$, taking one full clock cycle per single-bit shift.
    
      
    

#### N-Bit CMOS Magnitude Comparator

- **Architecture:** An iterative chain of identical 1-bit comparator blocks comparing bits from most significant (MSB) to least significant (LSB).
    
      
    
- **Inputs & Outputs:** Each cell takes bit inputs $A_i, B_i$ along with results from the previous higher-order stage ($C_{i+1}, D_{i+1}$), producing updated status outputs ($C_i, D_i$):
    
      
    

$C_i = 1$: Indicates $A > B$.

  

$D_i = 1$: Indicates $A < B$.

  

$C_i = D_i = 0$: Indicates both bits are equal ($A = B$).

  

- **Priority logic:** If an earlier stage already found an inequality ($C_{i+1} = 1$ or $D_{i+1} = 1$), that result carries straight through; current bits are only evaluated if all higher bits were equal.