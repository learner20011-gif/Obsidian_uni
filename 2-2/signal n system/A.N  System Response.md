### second order

![[Pasted image 20261004135654.png]]
### first order
![[Pasted image 20261004144136.png]]

![[Pasted image 20261004150543.png]]
![[Pasted image 20261004150521.png]]

## Qna 

### Question The switch in the circuit has been closed for a long time and is opened at $t = 0$. Find $v(t)$ for $t \ge 0$, and calculate the initial energy stored in the capacitor.

  ![[Pasted image 20261004145754.png]]

#### Solution
![[Pasted image 20261004145803.png]]
- **Initial Voltage ($t < 0$):**
    
      
    - The switch is closed and the circuit reaches dc steady state, making the capacitor act as an open circuit.
        
          
        
    - By voltage division across the $9\ \Omega$ resistor:
        
          
        
        $$v(0) = v_C(0^-) = \frac{9}{9 + 3} \times 20\text{ V} = 15\text{ V}$$
        
          
        
- **Equivalent Resistance and Time Constant ($t > 0$):**
    
      
    - The switch opens, disconnecting the $20\text{ V}$ source and $3\ \Omega$ resistor to form a source-free $RC$ circuit.
        
          
        
    - Equivalent resistance seen by the capacitor:
        
          
        
        $$R_{\text{eq}} = 1\ \Omega + 9\ \Omega = 10\ \Omega$$
        
          
        
    - Time constant ($\tau$):
        
          
        
        $$\tau = R_{\text{eq}}C = 10 \times (20 \times 10^{-3}) = 0.2\text{ s}$$
        
          
        
- **Capacitor Voltage $v(t)$ for $t \ge 0$:**
    
      
    
    $$v(t) = v_C(0) e^{-t/\tau} = 15 e^{-t/0.2} = 15 e^{-5t}\text{ V}$$
    
      
    
- **Initial Stored Energy:**
    
      
    
    $$w_C(0) = \frac{1}{2} C v_C(0)^2 = \frac{1}{2} \times (20 \times 10^{-3}) \times (15)^2 = 2.25\text{ J}$$

### Question Assuming that $i(0) = 10\text{ A}$, calculate $i(t)$ and $i_x(t)$ for $t > 0$ in the source-free $RL$ circuit containing a $0.5\text{ H}$ inductor, a $2\ \Omega$ resistor, a $4\ \Omega$ resistor, and a dependent voltage source $3i$.

  ![[Pasted image 20261004153834.png]]

#### Solution

- **Method 1: Equivalent Resistance & Time Constant**
    ![[Pasted image 20261004153844.png]]
      
    - Connect an independent test source $v_o = 1\text{ V}$ across terminals $a$-$b$ in place of the inductor to find the Thévenin resistance $R_{\text{eq}}$.
        
          
        
    - Loop 1 KVL:
        
          
        
        $$2(i_1 - i_2) + 1 = 0 \implies i_1 - i_2 = -\frac{1}{2}$$
        
          
        
    - Loop 2 KVL (with $i = -i_1$):
        
          
        
        $$6i_2 - 2i_1 - 3i_1 = 0 \implies i_2 = \frac{5}{6}i_1$$
        
          
        
    - Solving for currents:
        
          
        
        $$i_1 - \frac{5}{6}i_1 = -\frac{1}{2} \implies i_1 = -3\text{ A}$$
        
          
        
        $$i_o = -i_1 = 3\text{ A}$$
        
          
        
    - Equivalent resistance and time constant:
        
          
        
        $$R_{\text{eq}} = \frac{v_o}{i_o} = \frac{1}{3}\ \Omega$$
        
          
        
        $$\tau = \frac{L}{R_{\text{eq}}} = \frac{0.5}{1/3} = \frac{3}{2}\text{ s}$$
        
          
        
    - Inductor current $i(t)$ for $t > 0$:
        
          
        
        $$i(t) = i(0)e^{-t/\tau} = 10e^{-(2/3)t}\text{ A}$$
        
          
        

- **Method 2: Direct Differential Equation (KVL)**
    ![[Pasted image 20261004153854.png]]
      
    - Apply KVL directly to the two loops with the inductor in place ($i_1 = i$):
        
          
        - Loop 1:
            
              
            
            $$L\frac{di_1}{dt} + 2(i_1 - i_2) = 0 \implies \frac{di_1}{dt} + 4i_1 - 4i_2 = 0$$
            
              
            
        - Loop 2:
            
              
            
            $$4i_2 + 3i + 2(i_2 - i_1) = 0 \implies i_2 = \frac{5}{6}i_1$$
            
              
            
    - Substitute $i_2$ into the Loop 1 equation:
        
          
        
        $$\frac{di_1}{dt} + \frac{2}{3}i_1 = 0 \implies \frac{di}{i} = -\frac{2}{3}dt$$
        
          
        
    - Integrate with the initial condition $i(0) = 10\text{ A}$:
        
          
        
        $$\ln\frac{i(t)}{10} = -\frac{2}{3}t \implies i(t) = 10e^{-(2/3)t}\text{ A}$$
        
          
        

- **Finding $i_x(t)$ (for both methods):**
    
      
    - The voltage across the parallel combination is equal to the inductor voltage:
        
          
        
        $$v = L\frac{di}{dt} = 0.5 \times 10\left(-\frac{2}{3}\right)e^{-(2/3)t} = -\frac{10}{3}e^{-(2/3)t}\text{ V}$$
        
          
        
    - Current $i_x(t)$ flowing downward through the $2\ \Omega$ resistor:
        
          
        
        $$i_x(t) = \frac{v}{2} = -\frac{5}{3}e^{-(2/3)t} \approx -1.6667e^{-(2/3)t}\text{ A}\quad (t > 0)$$

##

* A second-order circuit is characterized by a second-order differential equation. It consists of resistors and the equivalent of **two energy storage elements.**
* The time constant of a circuit is the time required for the response to decay to a factor of 1eor 36.8 percent of its initial value.
* The Key to Working with a Source-Free RCCircuit Is Finding: 1. The initial voltage across the capacitor. 2. The time constant t. v(0)
* The Key to Working with a Source-Free RLCircuit Is to Find: 1. The initial current through the inductor. 2. The time constant of the circuit.