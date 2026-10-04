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
### Question In the circuit shown in Fig. 7.19, find $i_o$, $v_o$, and $i$ for all time, assuming that the switch was open for a long time.

![[Pasted image 20261004160328.png]]
#### Solution

- **For $t < 0$ (DC Steady State before Switch Closes):**
    ![[Pasted image 20261004160341.png]]
      
    - The switch is open, and under dc steady state, the inductor acts like a short circuit.
        
          
        
    - Because the inductor short-circuits the $6\ \Omega$ resistor, no current flows through it:
        
          
        
        $$i_o = 0\text{ A}$$
        
          
        
    - The inductor current is determined by the series path with the $2\ \Omega$ and $3\ \Omega$ resistors:
        
          
        
        $$i(t) = \frac{10}{2 + 3} = 2\text{ A}$$
        
          
        
    - The initial inductor current is therefore:
        
          
        
        $$i(0) = i(0^-) = 2\text{ A}$$
        
          
        
    - The voltage across the $3\ \Omega$ resistor is:
        
          
        
        $$v_o(t) = 3 \times i(t) = 3 \times 2 = 6\text{ V}$$
        
          
        

- **For $t > 0$ (Source-Free Response after Switch Closes):**
    ![[Pasted image 20261004160351.png]]
      
    - When the switch closes at $t = 0$, the $10\text{ V}$ independent source and $2\ \Omega$ resistor are isolated from the inductor loop, resulting in a source-free $RL$ circuit.
        
          
        
    - The equivalent resistance seen at the inductor terminals is the parallel combination of the $3\ \Omega$ and $6\ \Omega$ resistors:
        
          
        
        $$R_{\text{Th}} = 3 \parallel 6 = \frac{3 \times 6}{3 + 6} = 2\ \Omega$$
        
          
        
    - The time constant $\tau$ of the circuit is:
        
          
        
        $$\tau = \frac{L}{R_{\text{Th}}} = \frac{2\text{ H}}{2\ \Omega} = 1\text{ s}$$
        
          
        
    - The inductor current for $t > 0$ decays exponentially:
        
          
        
        $$i(t) = i(0)e^{-t/\tau} = 2e^{-t}\text{ A}$$
        
          
        
    - The voltage across the inductor $v_L(t)$ is given by:
        
          
        
        $$v_L(t) = L\frac{di}{dt} = 2 \times \frac{d}{dt}(2e^{-t}) = -4e^{-t}\text{ V}$$
        
    - Looking at the reference polarity of $v_o$, it is connected in parallel with the inductor but with opposite polarity ($v_o = -v_L$):
        
          
        
        $$v_o(t) = -v_L(t) = 4e^{-t}\text{ V}$$
        
          
        
    - The current $i_o(t)$ flowing downward through the $6\ \Omega$ resistor corresponds directly to $v_L/6$:
        
          
        
        $$i_o(t) = \frac{v_L(t)}{6} = \frac{-4e^{-t}}{6} = -\frac{2}{3}e^{-t}\text{ A}$$
        
          
        

- **Complete Expressions for All Time:**
    
      
    - **Inductor Current $i(t)$:**
        
          
        
        $$i(t) = \begin{cases} 2\text{ A}, & t < 0 \\ 2e^{-t}\text{ A}, & t \ge 0 \end{cases}$$
        
          
        
    - **Resistor Voltage $v_o(t)$:**
        
          
        
        $$v_o(t) = \begin{cases} 6\text{ V}, & t < 0 \\ 4e^{-t}\text{ V}, & t > 0 \end{cases}$$
        
          
        
    - **Resistor Current $i_o(t)$:**
        
          
        
        $$i_o(t) = \begin{cases} 0\text{ A}, & t < 0 \\ -\dfrac{2}{3}e^{-t}\text{ A}, & t > 0 \end{cases}$$

### Practice Problem 7.10: Find $v(t)$ for $t > 0$ and $v(0.5)$
  
![[Pasted image 20261004171539.png]]
- **Initial Voltage $v(0)$ ($t < 0$):**
    
      
    - The switch is open, disconnecting the right branch.
        
          
        
    - At steady state, the capacitor behaves as an open circuit.
        
          
        
    - With no current flowing through the $2\ \Omega$ resistor, the entire source voltage drops across the capacitor:
        
          
        
        $$v(0^-) = v(0^+) = 15\text{ V}$$
        
          
        
- **Final Voltage $v(\infty)$ ($t \to \infty$):**
    
      
    - The switch closes at $t = 0$.
        
          
        
    - At steady state, the capacitor is again treated as an open circuit.
        
          
        
    - Using nodal analysis at the capacitor node with reference to the bottom rail:
        
          
        
        $$\frac{v(\infty) - 15}{2} + \frac{v(\infty) - (-7.5)}{6} = 0$$
        
          
        
    - Multiplying the entire equation by $6$:
        
          
        
        $$3[v(\infty) - 15] + [v(\infty) + 7.5] = 0$$
        
        $$4v(\infty) - 45 + 7.5 = 0 \implies 4v(\infty) = 37.5 \implies v(\infty) = 9.375\text{ V}$$
        
- **Thevenin Resistance $R_{\text{th}}$ and Time Constant $\tau$ ($t > 0$):**
    
      
    - Deactivating the independent voltage sources (replacing them with short circuits):
        
          
        
        $$R_{\text{th}} = 2\ \Omega \parallel 6\ \Omega = \frac{2 \times 6}{2 + 6} = \frac{12}{8} = 1.5\ \Omega$$
        
          
        
    - The capacitor has capacitance $C = \frac{1}{3}\text{ F}$:
        
          
        
        $$\tau = R_{\text{th}}C = 1.5 \times \frac{1}{3} = 0.5\text{ s}$$
        
        $$\frac{1}{\tau} = \frac{1}{0.5} = 2\text{ s}^{-1}$$
        
- **Voltage Response $v(t)$ for $t > 0$:**
    
      
    - Applying the standard first-order step response formula:
        
          
        
        $$v(t) = v(\infty) + [v(0) - v(\infty)]e^{-t/\tau}$$
        
        $$v(t) = 9.375 + (15 - 9.375)e^{-2t} = (9.375 + 5.625e^{-2t})\text{ V}$$
        
          
        
- **Value at $t = 0.5\text{ s}$:**
    
      
    - Substituting $t = 0.5$:
        
          
        
        $$v(0.5) = 9.375 + 5.625e^{-2(0.5)} = 9.375 + 5.625e^{-1} \approx 9.375 + 5.625(0.36788) \approx 11.44\text{ V}$$

### Example 7.13: Find $i(t)$ for $t > 0$, and Calculate $i(2)$ and $i(5)$

  ![[Pasted image 20261004175239.png]]

- **Initial State ($t < 0$):**
    
      
    - Switches $S_1$ and $S_2$ are both open, disconnecting sources from the inductor.
        
          
        
    - Inductor current: $i(0^-) = i(0^+) = 0\text{ A}$.
        
          
        
- **Interval $0 \le t \le 4\text{ s}$ ($S_1$ closed, $S_2$ open):**
    
      
    - The $4\ \Omega$ and $6\ \Omega$ resistors are in series with the $40\text{ V}$ source:
        
          
        
        $$R_{\text{th}} = 4 + 6 = 10\ \Omega, \quad i(\infty) = \frac{40}{10} = 4\text{ A}$$
        
          
        
    - Time constant:
        
          
        
        $$\tau = \frac{L}{R_{\text{th}}} = \frac{5}{10} = 0.5\text{ s} \implies \frac{1}{\tau} = 2\text{ s}^{-1}$$
        
          
        
    - Inductor current response:
        
          
        
        $$i(t) = 4(1 - e^{-2t})\text{ A} \quad (0 \le t \le 4)$$
        
          
        
- **Switching at $t = 4\text{ s}$:**
    
      
    - Initial current entering the next interval:
        
          
        
        $$i(4) = 4(1 - e^{-8}) \approx 4\text{ A}$$
        
          
        
- **Interval $t \ge 4\text{ s}$ ($S_1$ and $S_2$ both closed):**
    
      
    - Steady-state current via nodal analysis at node $P$ (with inductor as a short circuit):
        
          
        
        $$\frac{40 - v}{4} + \frac{10 - v}{2} = \frac{v}{6} \implies v = \frac{180}{11}\text{ V}$$
        
          
        
        $$i(\infty) = \frac{v}{6} = \frac{30}{11} \approx 2.727\text{ A}$$
        
          
        
    - Thevenin resistance seen by the inductor:
        
          
        
        $$R_{\text{th}} = (4 \parallel 2) + 6 = \frac{4 \times 2}{4 + 2} + 6 = \frac{22}{3}\ \Omega$$
        
          
        
    - Time constant:
        
          
        
        $$\tau = \frac{L}{R_{\text{th}}} = \frac{5}{22/3} = \frac{15}{22}\text{ s} \implies \frac{1}{\tau} = \frac{22}{15} \approx 1.4667\text{ s}^{-1}$$
        
          
        
    - Inductor current response:
        
          
        
        $$i(t) = i(\infty) + [i(4) - i(\infty)]e^{-(t - 4)/\tau}$$
        
          
        
        $$i(t) = 2.727 + 1.273e^{-1.4667(t - 4)}\text{ A} \quad (t \ge 4)$$
        
          
        
- **Values at Specific Times:**
    
      
    - At $t = 2\text{ s}$ (falls in $0 \le t \le 4$):
        
          
        
        $$i(2) = 4(1 - e^{-4}) \approx \mathbf{3.93\text{ A}}$$
        
          
        
    - At $t = 5\text{ s}$ (falls in $t \ge 4$):
        
          
        
        $$i(5) = 2.727 + 1.273e^{-1.4667(5 - 4)} \approx \mathbf{3.02\text{ A}}$$

### *second order*

##

* A second-order circuit is characterized by a second-order differential equation. It consists of resistors and the equivalent of **two energy storage elements.**
* The time constant of a circuit is the time required for the response to decay to a factor of 1eor 36.8 percent of its initial value.
* The Key to Working with a Source-Free RCCircuit Is Finding: 1. The initial voltage across the capacitor. 2. The time constant t. v(0)
* The Key to Working with a Source-Free RLCircuit Is to Find: 1. The initial current through the inductor. 2. The time constant of the circuit. 
* 1. The initial capacitor voltage 2. The final capacitor voltage 3. The time constant t. 
* This formula is the standard **complete response formula** for a first-order circuit ($RC$ or $RL$), modified for when a switch flips at some time $t_0$ instead of $t = 0$.
$$v(t) = v(\infty) + [v(t_0) - v(\infty)]e^{-(t - t_0)/\tau}, \quad t \ge t_0$$