

![[Screenshot_20261005_023903_Xodo.jpg]]

### second order
![[Pasted image 20261005143126.png]]

![[Pasted image 20261004135654.png]]![[Pasted image 20261004193537.png]]
### first order
![[Pasted image 20261004144136.png]]![[Pasted image 20261004150543.png]]
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

### Question Assuming that the switch in Fig. 8.52 is closed prior to $t = 0^-$, find the inductor voltage $v_L(t)$ for $t > 0$.

  ![[Pasted image 20261005143126.png]]

- **Circuit Components:**
    
      
    - DC voltage source: $V_s = 12\text{ V}$
        
          
        
          
        
    - Wiring resistance: $R = 4\ \Omega$
        
          
        
          
        
    - Ignition coil (inductor): $L = 8\text{ mH} = 8 \times 10^{-3}\text{ H}$
        
          
        
          
        
    - Breaker points capacitor (condenser): $C = 1\ \mu\text{F} = 10^{-6}\text{ F}$
        
          
        
          
        
    - Switch opening at $t = 0$
        
          
        
          
        
    - Spark plug in parallel with the ignition coil
        
          
        

#### Physical Concept of the Ignition Circuit

- **Before $t = 0$ (Switch Closed):**
    
      
    - The closed switch provides a zero-resistance path that completely shorts out the $1\ \mu\text{F}$ capacitor.
        
          
        
    - Current flows from the $12\text{ V}$ battery through the $4\ \Omega$ resistor and directly through the $8\text{ mH}$ ignition coil.
        
          
        
    - The ignition coil reaches steady state, storing maximum magnetic energy $\frac{1}{2} L i^2$.
        
          
        
    - The spark plug has a high breakdown gap and acts as an open circuit prior to arcing.
        
          
        
- **At and After $t = 0$ (Switch Opens):**
    
      
    - The switch suddenly opens, inserting the capacitor into the loop.
        
          
        
    - The inductor current cannot drop to zero instantaneously; it forces current into the capacitor, charging it rapidly.
        
          
        
    - This rapid change in magnetic flux induces a large back-EMF voltage ($v_L = L \frac{di}{dt}$) across the ignition coil.
        
          
        
    - This high voltage pulse is what normally creates the spark across the spark plug gap in an engine.
        
          
        

#### Step 1: Initial Conditions ($t < 0$ and $t = 0^+$)

- **Inductor Current at $t = 0^-$:**
    
      
    - The switch is closed for a long time prior to $t = 0^-$, reaching DC steady state.
        
          
        
    - In DC steady state, the inductor acts as an ideal short circuit ($0\text{ V}$ drop).
        
          
        
    - The closed switch bypasses the capacitor entirely, meaning the only resistance in the loop is the $4\ \Omega$ resistor:
        
          
        
        $$i(0^-) = \frac{12\text{ V}}{4\ \Omega} = 3\text{ A}$$
        
    - By current continuity across an inductor:
        
          
        
        $$i(0^+) = i(0^-) = 3\text{ A}$$
        
- **Capacitor Voltage at $t = 0^-$:**
    
      
    - Because the closed switch is connected directly across the capacitor, it holds the capacitor voltage to zero:
        
          
        
        $$v_C(0^-) = 0\text{ V}$$
        
    - By voltage continuity across a capacitor:
        
          
        
        $$v_C(0^+) = v_C(0^-) = 0\text{ V}$$
        

#### Step 2: Second-Order Circuit Parameters for $t > 0$

- **Equivalent Loop Topology:**
    
      
    - For $t > 0$, the switch is open and the spark plug behaves as an open circuit before dielectric breakdown occurs.
        
          
        
    - The battery ($12\text{ V}$), resistor ($4\ \Omega$), capacitor ($1\ \mu\text{F}$), and inductor ($8\text{ mH}$) form a series RLC circuit.
        
          
        
- **Damping Factor ($\alpha$):**
    
      
    - For a series RLC circuit:
        
          
        
        $$\alpha = \frac{R}{2L} = \frac{4}{2 \times (8 \times 10^{-3})} = \frac{4}{16 \times 10^{-3}} = 250\text{ Np/s}$$
        
- **Undamped Natural Frequency ($\omega_0$):**
    
      
    - Calculated from the reactive elements:
        
          
        
        $$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{(8 \times 10^{-3}\text{ H}) \times (10^{-6}\text{ F})}} = \frac{1}{\sqrt{8 \times 10^{-9}}}$$
        
        $$\omega_0^2 = \frac{1}{8 \times 10^{-9}} = 1.25 \times 10^8\text{ (rad/s)}^2$$
        
        $$\omega_0 = \sqrt{1.25 \times 10^8} \approx 11,180.34\text{ rad/s}$$
        
- **Damping Regime:**
    
      
    - Comparing $\alpha$ and $\omega_0$:
        
          
        
        $$\alpha = 250 < \omega_0 \approx 11,180$$
        
    - Because $\alpha \ll \omega_0$, the circuit is **heavily underdamped**.
        
          
        
- **Damped Natural Frequency ($\omega_d$):**
    
      
    
    $$\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{1.25 \times 10^8 - (250)^2} = \sqrt{125,000,000 - 62,500} = \sqrt{124,937,500}$$
    
    $$\omega_d \approx 11,177.55\text{ rad/s} \approx 11,180\text{ rad/s}$$
    

#### Step 3: Determining the Loop Current $i(t)$

- **Final Steady-State Current ($t \to \infty$):**
    
      
    - As $t \to \infty$, the series capacitor charges fully and acts as a DC open circuit:
        
          
        
        $$i(\infty) = 0\text{ A}$$
        
- **General Form of Current Response:**
    
      
    
    $$i(t) = i(\infty) + i_n(t) = 0 + e^{-\alpha t} \left( A_1 \cos(\omega_d t) + A_2 \sin(\omega_d t) \right)$$
    
    $$i(t) = e^{-250t} \left( A_1 \cos(11,180t) + A_2 \sin(11,180t) \right)$$
    
- **Evaluating Constant $A_1$ using $i(0^+) = 3\text{ A}$:**
    
      
    
    $$i(0) = e^{0} \left( A_1 \cos(0) + A_2 \sin(0) \right) = A_1$$
    
    $$A_1 = 3\text{ A}$$
    
- **Determining the Initial Derivative $\left.\frac{di}{dt}\right\vert{}_{t=0^+}$ via KVL:**
    
      
    - Applying Kirchhoff's Voltage Law clockwise around the single loop for $t > 0$:
        
          
        
        $$-12 + v_R(t) + v_C(t) + v_L(t) = 0$$
        
        $$-12 + R\cdot i(t) + v_C(t) + L \frac{di(t)}{dt} = 0$$
        
    - Evaluating at $t = 0^+$ with $i(0^+) = 3\text{ A}$ and $v_C(0^+) = 0\text{ V}$:
        
          
        
        $$-12 + 4(3) + 0 + v_L(0^+) = 0$$
        
        $$-12 + 12 + v_L(0^+) = 0 \implies v_L(0^+) = 0\text{ V}$$
        
    - Since $v_L(0^+) = L \left.\frac{di}{dt}\right\vert{}_{t=0^+}$:
        
          
        
        $$\left.\frac{di}{dt}\right\vert{}_{t=0^+} = \frac{v_L(0^+)}{L} = \frac{0}{8 \times 10^{-3}} = 0\text{ A/s}$$
        
- **Evaluating Constant $A_2$:**
    
      
    - Taking the time derivative of $i(t)$:
        
          
        
        $$\frac{di}{dt} = -250 e^{-250t} \left( A_1 \cos(11,180t) + A_2 \sin(11,180t) \right) + 11,180 e^{-250t} \left( -A_1 \sin(11,180t) + A_2 \cos(11,180t) \right)$$
        
    - Evaluating at $t = 0$:
        
          
        
        $$\left.\frac{di}{dt}\right\vert{}_{t=0} = -250 A_1 + 11,180 A_2 = 0$$
        
        $$11,180 A_2 = 250 A_1$$
        
        $$A_2 = \frac{250}{11,180} A_1 = \frac{250 \times 3}{11,180} = \frac{750}{11,180} \approx 0.0671\text{ A}$$
        

#### Step 4: Inductor Voltage $v_L(t)$

- **Applying the Inductor Characteristic Equation:**
    
      
    
    $$v_L(t) = L \frac{di(t)}{dt}$$
    
- **Substituting the Full Expression for $\frac{di}{dt}$:**
    
      
    
    $$v_L(t) = L e^{-250t} \left[ (-250 A_1 + 11,180 A_2) \cos(11,180t) - (250 A_2 + 11,180 A_1) \sin(11,180t) \right]$$
    
- **Simplifying the Cosine and Sine Coefficients:**
    
      
    - The cosine coefficient is identically zero because $-250 A_1 + 11,180 A_2 = \left.\frac{di}{dt}\right\vert{}_{t=0^+} = 0$:
        
          
        
        $$\text{Cosine term} = 0$$
        
    - Evaluating the sine amplitude:
        
          
        
        $$250 A_2 + 11,180 A_1 = 250(0.0671) + 11,180(3) = 16.775 + 33,540 \approx 33,540$$
        
    - Multiplying by inductance $L = 8 \times 10^{-3}\text{ H}$:
        
          
        
        $$L \times 33,540 = (8 \times 10^{-3}) \times 33,540 \approx 268.32\text{ V} \approx 268\text{ V}$$
        
- **Final Closed-Form Expression for $v_L(t)$:**
    
    $$v_L(t) = -268 e^{-250t} \sin(11,180t)\text{ V} \quad \text{for } t > 0$$
##

* A second-order circuit is characterized by a second-order differential equation. It consists of resistors and the equivalent of **two energy storage elements.**
* The time constant of a circuit is the time required for the response to decay to a factor of 1eor 36.8 percent of its initial value.
* The Key to Working with a Source-Free RCCircuit Is Finding: 1. The initial voltage across the capacitor. 2. The time constant t. v(0)
* The Key to Working with a Source-Free RLCircuit Is to Find: 1. The initial current through the inductor. 2. The time constant of the circuit. 
* 1. The initial capacitor voltage 2. The final capacitor voltage 3. The time constant t. 
* The 5-Tau Rule : Because the growth or decay follows an exponential curve rather than a linear line, a circuit never theoretically reaches 100% of its final state. However, for all practical engineering applications, a circuit is considered **fully charged or discharged after 5 time constants (5τ)**, where it reaches **99.3%** of its final steady-state value
* Any first-order RC or RL circuit driven by a constant DC source can be described by the standard differential equation:

$$\frac{dx(t)}{dt} + \frac{1}{\tau}x(t) = \frac{x_\infty}{\tau}$$

- $x(t)$: The circuit variable of interest (capacitor voltage $v_C(t)$ or inductor current $i_L(t)$).
- $\tau$: The circuit time constant ($RC$ for RC circuits, or $\frac{L}{R}$ for RL circuits).
- $x_\infty$: The final steady-state value of the variable as $t \to \infty$.


$$x(t) = x_\infty + [x(0^+) - x_\infty]e^{-t/\tau}$$

* This formula is the standard **complete response formula** for a first-order circuit ($RC$ or $RL$), modified for when a switch flips at some time $t_0$ instead of $t = 0$.
$$v(t) = v(\infty) + [v(t_0) - v(\infty)]e^{-(t - t_0)/\tau}, \quad t \ge t_0$$




  
In any linear circuit, **every voltage and current in the network** satisfies the exact same characteristic differential equation:
$$\frac{d^2 x(t)}{dt^2} + 2\alpha \frac{dx(t)}{dt} + \omega_0^2 x(t) = f(t)$$

where $x(t)$ represents current or voltage, $\alpha$ is the damping factor (attenuation factor), and $\omega_0$ is the undamped natural frequency.

  

### Core Governing Parameters and Definitions

- **Undamped Natural Frequency ($\omega_0$):**
    
      
    - Determined entirely by the reactive elements:
        
          
        
        $$\omega_0 = \frac{1}{\sqrt{LC}} \quad \text{(rad/s)}$$
        
- **Neper Frequency / Damping Factor ($\alpha$):**
    
      
    - Quantifies the rate of energy dissipation:
        
          
        - **Series RLC:** $\alpha = \frac{R}{2L}$
            
              
            
        - **Parallel RLC:** $\alpha = \frac{1}{2RC}$
            
              
            
- **Damping Ratio ($\zeta$):**
    
      
    - A dimensionless measure of system damping:
        
          
        
        $$\zeta = \frac{\alpha}{\omega_0}$$
        The maximum percentage overshoot ($M_p$) for a second-order underdamped system is:

$$M_p = e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}} \times 100\%$$
- **Quality Factor ($Q$):**
    
      
    - Relates peak energy stored to energy dissipated per radian:
        
          
        
        $$Q = \frac{\omega_0}{2\alpha} = \frac{1}{2\zeta}$$
        
        - **Series RLC:** $Q = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_0 L}{R}$
            
              
            
        - **Parallel RLC:** $Q = R\sqrt{\frac{C}{L}} = \frac{R}{\omega_0 L}$
            
              
            

### Characteristic Equation and Roots

Setting the input source $f(t) = 0$ yields the characteristic algebraic equation:

  

$$s^2 + 2\alpha s + \omega_0^2 = 0$$

Solving with the quadratic formula gives the natural frequencies (characteristic roots):

  

$$s_{1, 2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

The physical behavior of the natural response $x_n(t)$ depends entirely on the sign of the discriminant $(\alpha^2 - \omega_0^2)$:

  

- **1. Overdamped Response ($\alpha > \omega_0 \implies \zeta > 1$):**
    
      
    - Roots are real, negative, and unequal: $s_1 \neq s_2 < 0$.
        
          
        
    - Form:
        
          
        
        $$x_n(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$
        
    - Behavior: Non-oscillatory decay; slow return to equilibrium due to high dissipation.
        
          
        
- **2. Critically Damped Response ($\alpha = \omega_0 \implies \zeta = 1$):**
    
      
    - Roots are real, negative, and repeated: $s_1 = s_2 = -\alpha$.
        
          
        
    - Form:
        
          
        
        $$x_n(t) = (A_1 + A_2 t)e^{-\alpha t}$$
        
    - Behavior: Fastest non-oscillatory return to equilibrium without overshoot.
        
          
        
- **3. Underdamped Response ($\alpha < \omega_0 \implies \zeta < 1$):**
    
      
    - Roots are complex conjugate pairs: $s_{1, 2} = -\alpha \pm j\omega_d$.
        
          
        
    - Damped natural frequency:
        
          
        
        $$\omega_d = \sqrt{\omega_0^2 - \alpha^2}$$
        
    - Form:
        
          
        
        $$x_n(t) = e^{-\alpha t} \left( A_1 \cos(\omega_d t) + A_2 \sin(\omega_d t) \right)$$
        
    - Behavior: Sinusoidal oscillations decaying within an exponential envelope $e^{-\alpha t}$.
        
          
        
- **4. Undamped Response ($\alpha = 0 \implies R = 0 \text{ or } \infty$):**
    
      
    - Roots are purely imaginary: $s_{1, 2} = \pm j\omega_0$.
        
          
        
    - Form:
        
          
        
        $$x_n(t) = A_1 \cos(\omega_0 t) + A_2 \sin(\omega_0 t)$$
        
    - Behavior: Sustained oscillations at frequency $\omega_0$ with zero energy loss.
        
          
        

### Complete Solution Framework
finding charachteristics eqn how? then alpha  w. then output signal eqn. 
For circuits with constant DC independent sources switched at $t = 0$:

  

$$x(t) = x_{\text{forced}}(t) + x_{\text{natural}}(t) = x(\infty) + x_n(t)$$

- **Step 1: Determine initial states at $t = 0^-$ and $t = 0^+$:**
    
      
    - Continuity laws for reactive components:
        
          
        
        $$i_L(0^+) = i_L(0^-), \quad v_C(0^+) = v_C(0^-)$$
        
- **Step 2: Find initial derivatives at $t = 0^+$:**
    
      
    - Relate capacitor currents and inductor voltages via device equations:
        
          
        
        $$\frac{dv_C(0^+)}{dt} = \frac{i_C(0^+)}{C}, \quad \frac{di_L(0^+)}{dt} = \frac{v_L(0^+)}{L}$$
        
- **Step 3: Determine the final steady-state value $x(\infty)$:**
    
      
    - For DC inputs at $t \to \infty$, replace capacitors with open circuits and inductors with short circuits.
        
          
        
- **Step 4: Solve for arbitrary constants ($A_1, A_2$):**
    
      
    - Evaluate the complete equation at $t = 0^+$:
        
          
        
        $$x(0^+) = x(\infty) + x_n(0^+)$$
        
    - Differentiate the complete equation and evaluate at $t = 0^+$:
        
          
        
        $$\left. \frac{dx}{dt} \right\vert{}_{t=0^+} = \left. \frac{dx_n}{dt} \right\vert{}_{t=0^+}$$
        
    - Solve the resulting $2 \times 2$ system of linear equations for $A_1$ and $A_2$.
        
          
        

### Formulas for Common Topologies

#### 1. Series RLC Circuit

- Primary variable: Loop current $i(t)$ or capacitor voltage $v_C(t)$.
    
      
    
- Differential equation in terms of $i(t)$:
    
      
    
    $$L\frac{d^2 i}{dt^2} + R\frac{di}{dt} + \frac{1}{C}i = \frac{dv_s}{dt}$$
    
- Parameter relationships:
    
      
    
    $$\alpha = \frac{R}{2L}, \quad \omega_0 = \frac{1}{\sqrt{LC}}, \quad \zeta = \frac{R}{2}\sqrt{\frac{C}{L}}$$
    

#### 2. Parallel RLC Circuit

- Primary variable: Node voltage $v(t)$ or inductor current $i_L(t)$.
    
      
    
- Differential equation in terms of $v(t)$:
    
      
    
    $$C\frac{d^2 v}{dt^2} + \frac{1}{R}\frac{dv}{dt} + \frac{1}{L}v = \frac{di_s}{dt}$$
    
- Parameter relationships:
    
      
    
    $$\alpha = \frac{1}{2RC}, \quad \omega_0 = \frac{1}{\sqrt{LC}}, \quad \zeta = \frac{1}{2R}\sqrt{\frac{L}{C}}$$
    

#### 3. Pure RC and RL Second-Order Circuits (Two Like Reactive Elements)

Circuits containing two capacitors or two inductors separated by resistors (e.g., cascaded RC filters, ladder networks) form second-order systems governed by:

  

$$\frac{d^2 v}{dt^2} + a_1 \frac{dv}{dt} + a_0 v = f(t)$$

- **Characteristics of Two-Capacitor (RC-RC) or Two-Inductor (RL-RL) Networks:**
    
      
    - Energy is dissipated through resistive elements without reactive energy exchange (sloshing) between $L$ and $C$.
        
          
        
    - The roots $s_1, s_2$ are **always real and negative** (strictly non-oscillatory).
        
          
        
    - These circuits are inherently **overdamped** (or critically damped in degenerate limiting cases), never underdamped ($\zeta \ge 1$ always).
        
          
        
- **Example (Cascaded Two-Stage RC Low-Pass Filter):**
    
      
    - Stage 1 ($R_1, C_1$) connected to Stage 2 ($R_2, C_2$):
        
          
        
        $$\frac{d^2 v_2}{dt^2} + \left(\frac{1}{R_1 C_1} + \frac{1}{R_2 C_2} + \frac{1}{R_2 C_1}\right)\frac{dv_2}{dt} + \frac{1}{R_1 R_2 C_1 C_2} v_2 = \frac{v_{in}}{R_1 R_2 C_1 C_2}$$
        
    - Notice the coupling term $\frac{1}{R_2 C_1}$ representing the loading effect of stage 2 on stage 1.
        

### Summary Comparison Table

|**Metric / Parameter**|**Series RLC**|**Parallel RLC**|**Cascaded RC-RC**|
|---|---|---|---|
|**State Variables**|$i_L(t), v_C(t)$|$v_C(t), i_L(t)$|$v_{C1}(t), v_{C2}(t)$|
|**$\omega_0$**|$\frac{1}{\sqrt{LC}}$|$\frac{1}{\sqrt{LC}}$|$\frac{1}{\sqrt{R_1 R_2 C_1 C_2}}$|
|**Damping Factor ($\alpha$)**|$\frac{R}{2L}$|$\frac{1}{2RC}$|$\frac{1}{2}\left(\frac{1}{R_1 C_1} + \frac{1}{R_2 C_2} + \frac{1}{R_2 C_1}\right)$|
|**Quality Factor ($Q$)**|$\frac{1}{R}\sqrt{\frac{L}{C}}$|$R\sqrt{\frac{C}{L}}$|$< 0.5$ (Cannot oscillate)|
|**Possible Regimes**|Over / Critical / Under / Undamped|Over / Critical / Under / Undamped|Strictly Overdamped|
|**Root Locations**|Anywhere in Left Half Plane|Anywhere in Left Half Plane|Strictly Negative Real Axis|



Heaviside’s Cover-Up Method is an algebraic shortcut to find the coefficients (residues) of a Partial Fraction Expansion (PFE) directly without solving systems of simultaneous linear equations.

It applies to any strictly proper rational function:

$$F(s) = \frac{N(s)}{D(s)}, \quad \text{where } \deg(N) < \deg(D)$$

### Case 1: Distinct (Simple) Real Poles

When the denominator consists of non-repeated linear factors:

$$D(s) = (s - p_1)(s - p_2)\cdots(s - p_n)$$

The expansion is:

$$F(s) = \frac{A_1}{s - p_1} + \frac{A_2}{s - p_2} + \dots + \frac{A_n}{s - p_n}$$

- **General Formula:**
    
    $$A_k = \left. (s - p_k) F(s) \right\vert{}_{s = p_k}$$
    
- **Intuition ("Cover-Up"):**
    
    - Cover up the factor $(s - p_k)$ in the denominator of $F(s)$.
        
    - Substitute $s = p_k$ into the remaining expression to evaluate $A_k$.
        
- **Worked Example:**
    
    $$F(s) = \frac{2s + 5}{(s + 1)(s + 3)} = \frac{A_1}{s + 1} + \frac{A_2}{s + 3}$$
    
    - Find $A_1$ (at pole $s = -1$):
        
        $$A_1 = \left. \frac{2s + 5}{s + 3} \right\vert{}_{s = -1} = \frac{2(-1) + 5}{-1 + 3} = \frac{3}{2}$$
        
    - Find $A_2$ (at pole $s = -3$):
        
        $$A_2 = \left. \frac{2s + 5}{s + 1} \right\vert{}_{s = -3} = \frac{2(-3) + 5}{-3 + 1} = \frac{-1}{-2} = \frac{1}{2}$$
        
    - Result:
        
        $$F(s) = \frac{3/2}{s + 1} + \frac{1/2}{s + 3}$$
        

### Case 2: Repeated (Multiple) Real Poles

When the denominator contains a factor repeated $m$ times: $(s - p)^m$.

The expansion for that factor has $m$ terms:

$$F(s) = \frac{A_m}{(s - p)^m} + \frac{A_{m-1}}{(s - p)^{m-1}} + \dots + \frac{A_1}{s - p} + \dots$$

- **General Derivative Formula:**
    
    $$A_{m-k} = \frac{1}{k!} \left. \frac{d^k}{ds^k} \left[ (s - p)^m F(s) \right] \right\vert{}_{s = p}, \quad \text{for } k = 0, 1, \dots, m-1$$
    
- **Order of Evaluation:**
    
    - **Highest power ($k = 0$):** Standard cover-up (no derivative):
        
        $$A_m = \left. (s - p)^m F(s) \right\vert{}_{s = p}$$
        
    - **Next lower power ($k = 1$):** First derivative:
        
        $$A_{m-1} = \left. \frac{d}{ds} \left[ (s - p)^m F(s) \right] \right\vert{}_{s = p}$$
        
    - **General lower power ($k$):** $k$-th derivative divided by $k!$:
        
        $$A_{m-k} = \frac{1}{k!} \left. \frac{d^k}{ds^k} \left[ (s - p)^m F(s) \right] \right\vert{}_{s = p}$$
        
- **Worked Example:**
    
    $$F(s) = \frac{s^2 + 1}{(s + 1)^2(s + 2)} = \frac{A_2}{(s + 1)^2} + \frac{A_1}{s + 1} + \frac{B}{s + 2}$$
    
    - Find $B$ (distinct pole at $s = -2$):
        
        $$B = \left. \frac{s^2 + 1}{(s + 1)^2} \right\vert{}_{s = -2} = \frac{(-2)^2 + 1}{(-2 + 1)^2} = \frac{5}{1} = 5$$
        
    - Find $A_2$ (highest repeated power at $s = -1$):
        
        $$A_2 = \left. \frac{s^2 + 1}{s + 2} \right\vert{}_{s = -1} = \frac{(-1)^2 + 1}{-1 + 2} = \frac{2}{1} = 2$$
        
    - Find $A_1$ (first derivative at $s = -1$):
        
        $$\frac{d}{ds}\left[ \frac{s^2 + 1}{s + 2} \right] = \frac{2s(s + 2) - (s^2 + 1)(1)}{(s + 2)^2} = \frac{s^2 + 4s - 1}{(s + 2)^2}$$
        
        $$A_1 = \left. \frac{s^2 + 4s - 1}{(s + 2)^2} \right\vert{}_{s = -1} = \frac{(-1)^2 + 4(-1) - 1}{(-1 + 2)^2} = \frac{1 - 4 - 1}{1} = -4$$
        
    - Result:
        
        $$F(s) = \frac{2}{(s + 1)^2} - \frac{4}{s + 1} + \frac{5}{s + 2}$$