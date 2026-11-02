![[Pasted image 20261102140032.png|318]]
![[Pasted image 20261102135722.png]]

![[Pasted image 20261102142254.png]]
![[Pasted image 20261102144632.png]]
![[Pasted image 20261102144641.png]]
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
#### Transit Time vs. $\tau$ and Practical Delays

- **Transit Time ($\tau_{sd}$)**: Time taken by electrons to cross from source to drain:
    

$$\tau_{sd} = \frac{L^2}{\mu V_{ds}}$$

- **Calculation for $5\ \mu\text{m}$**:
    
    - Using average $V_{ds} = 3\ \text{V}$, electron mobility $\mu = 650\ \text{cm}^2/\text{V}\cdot\text{s}$, and $L = 5\ \mu\text{m}$:
        

$$\tau_{sd} = \frac{25 \times 10^{-8}\ \text{cm}^2}{650 \times 3} \approx 0.13\ \text{ns}$$

- This matches closely with $\tau \approx 0.1\ \text{ns}$
#### nMOS Inverter Delays

- **Resistances in a 4:1 Inverter**:
    
    - Pull-down transistor ($Z_{pd} = 1$): $R_{pd} = 1 R_s = 10\ \text{k}\Omega$.
        
    - Pull-up transistor ($Z_{pu} = 4$): $R_{pu} = 4 R_s = 40\ \text{k}\Omega$.
        
- **Asymmetric Switching**:
    
    - Output falling ($1 \to 0$): Discharges through pull-down $\to \text{delay} = 1\tau$.
        
    - Output rising ($0 \to 1$): Charges through pull-up $\to \text{delay} = 4\tau$.
        
- **Inverter Pair Delay**:
    
    - Passing a signal through two inverters covers both one rise and one fall:
        

$$\tau_d = \left(1 + \frac{Z_{pu}}{Z_{pd}}\right)\tau = (1 + 4)\tau = 5\tau$$

#### Figure 4.7: nMOS Inverter Pair Delay

- **The Setup**: Figure 4.7 shows two cascaded 4:1 nMOS inverters driving each other.
    
- **Load Capacitance**: Each inverter stage drives the gate of the next stage, which has a load capacitance of $1\Box C_g$.
    
- **Asymmetric Single Stage Delay**:
    
    - **Falling output ($1 \to 0$)**: The load discharges through the minimum pull-down transistor ($1 R_s$), taking $1\tau$.
        
    - **Rising output ($0 \to 1$)**: The load charges through the longer pull-up transistor ($4 R_s$), taking $4\tau$.
        
- **Total Pair Delay ($5\tau$)**:
    
    - A signal passing through two consecutive inverters always undergoes exactly one fall and one rise, regardless of whether the input starts high or low.
        
    - Total pair delay formula:
        

$$\tau_d = \left(1 + \frac{Z_{pu}}{Z_{pd}}\right)\tau = 1\tau + 4\tau = 5\tau$$

#### Figure 4.8: Minimum Size CMOS Inverter Pair Delay

- **The Setup**: Figure 4.8 shows two cascaded minimum-size CMOS inverters.
    
- **Double Load Capacitance ($2\Box C_g$)**:
    
    - Each CMOS input connects to both an n-transistor gate and a p-transistor gate.
        
    - The input capacitance is twice that of an nMOS inverter: $C_{in} = 1\Box C_g + 1\Box C_g = 2\Box C_g$.
        
- **Resistance Difference**:
    
    - **n-transistor**: Resistance is $1 R_s = 10\ \text{k}\Omega$.
        
    - **p-transistor**: Holes have lower mobility than electrons, so a minimum-size p-device has a higher resistance of $2.5 R_s = 25\ \text{k}\Omega$.
        
- **Single Stage Delays**:
    
    - **Fall time ($t_f$)**: The $2\Box C_g$ load discharges through the n-channel transistor ($1 R_s$), giving:
        

$$t_f = 1 R_s \times 2\Box C_g = 2\tau$$

- **Rise time ($t_r$)**: The $2\Box C_g$ load charges through the p-channel transistor ($2.5 R_s$), giving:
    

$$t_r = 2.5 R_s \times 2\Box C_g = 5\tau$$

- **Total Pair Delay ($7\tau$)**:
    
    - Passing through the pair causes one fall ($2\tau$) and one rise ($5\tau$).
        
    - Total CMOS pair delay:
        

$$\text{Pair Delay} = 2\tau + 5\tau = 7\tau$$

#### CMOS Inverter Delays and Sizing

- **Input Capacitance**:
    
    - A CMOS gate connects to both an nMOS and a pMOS transistor gate.
        
    - Total input capacitance is double: $C_{in} = 2 \Box C_g$.
        
- **Resistance Asymmetry**:
    
    - Holes move slower than electrons, so a minimum-size pMOS has about $2.5\times$ higher resistance ($25\ \text{k}\Omega$) than an nMOS ($10\ \text{k}\Omega$).
        
- **Making Delays Symmetrical**:
    
    - **Fix**: Make the pMOS channel 2 to 3 times wider ($W_p \approx 2.5 W_n$).
        
    - **Trade-off**: Lower resistance balances rise/fall speeds, but increases gate capacitance. It still improves overall speed because external wiring capacitance stays fixed
- #### What is a Silicide?

- **Definition**: A silicide is a compound made by placing a layer of metal onto polysilicon and heating them together (a process called sintering).
    
- **Why It Is Used**: As chip features shrink, regular polysilicon causes high sheet resistance and slow $RC$ signal delay. Silicide is used as a faster replacement.
    

#### Sheet Resistance Comparison

- **Polysilicon**: High resistance, typically $R_s = 15\text{ to }100\ \Omega/\Box$.
    
- **Silicide**: Much lower resistance, around $R_s = 2\text{ to }4\ \Omega/\Box$.
    
- **Benefit**: Lower sheet resistance means faster circuit speed and much smaller delay.
    
- **Drawback**: Making silicides requires extra fabrication steps, which increases manufacturing cost and complexity.
    

#### Methods of Deposition

- **Sputtering or Evaporation**: Direct deposition of metal onto the polysilicon surface before heating.
    
- **Co-sputtering**: Sputtering both metal and silicon together over the polysilicon layer.
    
- **Co-evaporating**: Evaporating both pure elements at the same time onto the wafer.

#### 5.2.1 Gate Area ($A_g$)

- **Formula:** $A_g = L \times W$
    
      
    
- **Scaling:** Both $L$ and $W$ scale by $1/\alpha$ $\rightarrow$ Scaled by $\mathbf{1/\alpha^2}$
    
      
    

#### 5.2.2 Gate Capacitance Per Unit Area ($C_0$ or $C_{ox}$)

- **Formula:** $C_0 = \frac{\varepsilon_{ox}}{D}$
    
      
    
- **Scaling:** Oxide thickness $D$ scales by $1/\beta$ $\rightarrow$ Scaled by $\mathbf{\beta}$
    
      
    

#### 5.2.3 Gate Capacitance ($C_g$)

- **Formula:** $C_g = C_0 L W$
    
      
    
- **Scaling:** Scaled by $\beta \times \left(\frac{1}{\alpha^2}\right) = \mathbf{\frac{\beta}{\alpha^2}}$
    
      
    

#### 5.2.4 Parasitic Capacitance ($C_x$)

- **Formula:** $C_x \propto \frac{A_x}{d}$
    
      
    
- **Scaling:** Depletion area $A_x$ scales by $1/\alpha^2$ and depletion width $d$ scales by $1/\alpha$ $\rightarrow$ Scaled by $\mathbf{1/\alpha}$
    
      
    

#### 5.2.5 Carrier Density in Channel ($Q_{on}$)

- **Formula:** $Q_{on} = C_0 \cdot V_{gs}$
    
      
    
- **Scaling:** $C_0$ scales by $\beta$, $V_{gs}$ scales by $1/\beta$ $\rightarrow$ Scaled by $\mathbf{1}$ (unchanged)
    
      
    

#### 5.2.6 Channel Resistance ($R_{on}$)

- **Formula:** $R_{on} = \frac{L}{W} \frac{1}{Q_{on} \mu}$
    
      
    
- **Scaling:** Geometric ratio $\frac{L}{W}$ and carrier density $Q_{on}$ scale by $1$ $\rightarrow$ Scaled by $\mathbf{1}$ (unchanged)
    
      
    

#### 5.2.7 Gate Delay ($T_d$)

- **Formula:** $T_d \propto R_{on} \cdot C_g$
    
      
    
- **Scaling:** Scaled by $1 \times \frac{\beta}{\alpha^2} = \mathbf{\frac{\beta}{\alpha^2}}$
    
      
    

#### 5.2.8 Maximum Operating Frequency ($f_0$)

- **Formula:** $f_0 \propto \frac{1}{T_d}$
    
      
    
- **Scaling:** Inversely proportional to gate delay $\rightarrow$ Scaled by $\mathbf{\frac{\alpha^2}{\beta}}$
    
      
    

#### 5.2.9 Saturation Current ($I_{dss}$)

- **Formula:** $I_{dss} = \frac{C_0 \mu}{2} \frac{W}{L} (V_{gs} - V_t)^2$
    
      
    
- **Scaling:** Voltages scale by $1/\beta$ and $C_0$ scales by $\beta$ $\rightarrow$ Scaled by $\beta \left(\frac{1}{\beta}\right)^2 = \mathbf{1/\beta}$
    
      
    

#### 5.2.10 Current Density ($J$)

- **Formula:** $J = \frac{I_{dss}}{A}$
    
      
    
- **Scaling:** Channel cross-section $A$ scales by $1/\alpha^2$ $\rightarrow$ Scaled by $\frac{1/\beta}{1/\alpha^2} = \mathbf{\frac{\alpha^2}{\beta}}$
    
      
    

#### 5.2.11 Switching Energy Per Gate ($E_g$)

- **Formula:** $E_g = \frac{1}{2} C_g (V_{DD})^2$
    
      
    
- **Scaling:** Scaled by $\left(\frac{\beta}{\alpha^2}\right) \left(\frac{1}{\beta^2}\right) = \mathbf{\frac{1}{\alpha^2 \beta}}$
    
      
    

#### 5.2.12 Power Dissipation Per Gate ($P_g$)

- **Formula:** $P_g = P_{gs} + P_{gd}$ (static + dynamic power)
    
      
    
- **Scaling:** Both static and dynamic components scale identically $\rightarrow$ Scaled by $\mathbf{1/\beta^2}$
    
      
    

#### 5.2.13 Power Dissipation Per Unit Area ($P_a$)

- **Formula:** $P_a = \frac{P_g}{A_g}$
    
      
    
- **Scaling:** Scaled by $\frac{1/\beta^2}{1/\alpha^2} = \mathbf{\frac{\alpha^2}{\beta^2}}$
    
      
    

#### 5.2.14 Power-Speed Product ($P_T$)

- **Formula:** $P_T = P_g \cdot T_d$
    
      
    
- **Scaling:** Scaled by $\left(\frac{1}{\beta^2}\right) \left(\frac{\beta}{\alpha^2}\right) = \mathbf{\frac{1}{\alpha^2 \beta}}$