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


##

* A second-order circuit is characterized by a second-order differential equation. It consists of resistors and the equivalent of **two energy storage elements.**
* The time constant of a circuit is the time required for the response to decay to a factor of 1eor 36.8 percent of its initial value.
* The Key to Working with a Source-Free RCCircuit Is Finding: 1. The initial voltage across the capacitor. 2. The time constant t. v(0)
* The Key to Working with a Source-Free RLCircuit Is to Find: 1. The initial current through the inductor. 2. The time constant of the circuit.