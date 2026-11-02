![[Pasted image 20261102140032.png|318]]
![[Pasted image 20261102135722.png]]




#### Sheet Resistance ($R_s$) Concept and Formula

- **The Basic Idea**: Every layer in an integrated circuit (metal, polysilicon, diffusion) resists the flow of electric current.
    
- **Resistance of a Strip**: For a block of material with length $L$, width $W$, thickness $t$, and resistivity $\rho$:
    

$$R = \frac{\rho \cdot L}{\text{Area}} = \frac{\rho \cdot L}{t \cdot W} = \left(\frac{\rho}{t}\right)\left(\frac{L}{W}\right)$$

- **Definition of Sheet Resistance ($R_s$)**: Because the thickness $t$ is fixed during chip fabrication, we combine $\rho / t$ into a single term:
    

$$R_s = \frac{\rho}{t}$$

The unit of $R_s$ is **ohms per square** ($\Omega/\Box$).

- **Aspect Ratio ($Z$)**:
    

$$Z = \frac{L}{W}$$

This represents the number of squares of dimension $W \times W$ laid end-to-end.

- **Total Resistance**:
    

$$R = R_s \cdot Z = R_s \left(\frac{L}{W}\right)$$

- **Why Squares Matter**: If a shape is a square ($L = W$), then $Z = 1$ and $R = R_s$. The resistance across two opposite sides of any square is always $R_s$, regardless of whether the square is $1\ \mu\text{m} \times 1\ \mu\text{m}$ or $10\ \mu\text{m} \times 10\ \mu\text{m}$.
#### Area Capacitance and the Standard Unit ($\Box C_g$)

- **Area Capacitance**: Every conductive layer separated by an oxide layer forms a parallel-plate capacitor:
    

$$C = \frac{\epsilon \cdot A}{d}$$

where $A$ is area, $d$ is oxide thickness, and $\epsilon$ is dielectric permittivity.

- **Standard Capacitance Unit ($\Box C_g$)**: To keep calculations simple, VLSI designers define $\Box C_g$ as the gate-to-channel capacitance of a standard minimum square transistor ($2\lambda \times 2\lambda$).
    

$$\Box C_g = C_{ox} \times (2\lambda \times 2\lambda) = 4\lambda^2 \cdot C_{ox}$$
**Typical Values for $\Box C_g$**:

- $5\ \mu\text{m}$ technology ($\lambda = 2.5\ \mu\text{m}$): $\Box C_g \approx 0.01\ \text{pF}$.
#### Area Capacitance Calculation

- **Concept:**
    
    - To find the total parasitic capacitance of a wire or path, count how many minimum squares ($2\lambda \times 2\lambda$) fit in that wire.
        
    - Multiply that square count by the layer's relative capacitance factor.
        
- **Math Steps:**
    
    1. Find wire area:
        

$$\text{Area} = L \times W$$

2. Convert area into units of standard gate squares:
    

$$\text{Number of squares } N = \frac{L \times W}{2\lambda \times 2\lambda}$$

3. Total capacitance in terms of $\square C_g$:
    

$$C_{\text{total}} = N \times (\text{Relative Value}) \times \square C_g$$
#### The Basic Delay Unit ($\tau$) and Inverter Delay

- **Definition of $\tau$**: The fundamental delay unit $\tau$ is the RC time constant formed by one standard minimum square n-channel transistor charging one standard unit load capacitance:
    

$$\tau = R_s(\text{n-channel}) \times \Box C_g$$

- **Typical Numerical Value**:
    
    - For $5\ \mu\text{m}$ technology:
        

$$\tau = (10^4\ \Omega) \times (0.01 \times 10^{-12}\ \text{F}) = 10^{-10}\ \text{s} = 0.1\ \text{ns}$$

- **Inverter Switching Times**:
    
    - **Discharge (Output Falling $1 \to 0$)**: The load discharges through the pull-down transistor ($Z = 1$, resistance $= 1 R_s$). The delay is:
        

$$t_{fall} \approx 1\tau$$

- **Charge (Output Rising $0 \to 1$)**: The load charges through the pull-up transistor ($Z = 4$, resistance $= 4 R_s$). The delay is:
    

$$t_{rise} \approx 4\tau$$

- **Inverter Pair Delay**: The total delay for a signal passing through two consecutive inverters (one rise + one fall) is:
    

$$t_{pair} = t_{rise} + t_{fall} = 4\tau + 1\tau = 5\tau$$

