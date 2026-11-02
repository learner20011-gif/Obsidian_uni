





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