![[Pasted image 20260829111327.png]]

### **Order Calculation ($N$)**

Using the standard Butterworth order formula:

$$N \ge \frac{\log \sqrt{\frac{10^{-0.1 \alpha_s} - 1}{10^{-0.1 \alpha_p} - 1}}}{\log \left(\frac{\omega_s}{\omega_p}\right)}$$

cutoff frequency $\omega_c$ can be determined from either passband or stopband specification:

$$\omega_c = \frac{\omega_p}{\left(10^{0.1 A_p} - 1\right)^{1 / 2N}} \quad \text{or} \quad \frac{\omega_s}{\left(10^{0.1 A_s} - 1\right)^{1 / 2N}}$$The normalized 4th-order Butterworth polynomial is given by:

$$H(s)_{\text{norm}} = \frac{1}{\left(s^2 + 0.7654s + 1\right)\left(s^2 + 1.8478s + 1\right)}$$

- **Unity-Gain buffer configuration ($K = 1$):**
    
    - Op-amp output connected directly to the inverting input:
        
        $$H(s) = \frac{\frac{1}{R_1 R_2 C_1 C_2}}{s^2 + s\left(\frac{1}{R_1 C_1} + \frac{1}{R_2 C_1}\right) + \frac{1}{R_1 R_2 C_1 C_2}}$$
        
- **Comparison with standard second-order stage:**
    
    $$H(s) = \frac{\omega_c^2}{s^2 + b_k \omega_c s + \omega_c^2}$$
    
    $$\omega_c^2 = \frac{1}{R_1 R_2 C_1 C_2}$$
    
    $$b_k \omega_c = \frac{1}{C_1}\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$$
- Step 1: Look up or calculate normalized values ($R = 1\,\Omega, \omega_c = 1\text{ rad/s}$):
    
    $$C_{1,\text{norm}} = \frac{2}{b_k}$$
    
    $$C_{2,\text{norm}}$$
    
- Step 2: Define impedance scaling factor ($k_m$) and frequency scaling factor ($k_f$):
    
    $$k_m = R_{\text{actual}}$$
    
    $$k_f = \omega_c = 2\pi f_c$$
    
- Step 3: Compute actual scaled components:
    
    $$R' = k_m \times R_{\text{norm}} = k_m$$
    
    $$C' = \frac{C_{\text{norm}}}{k_m \times k_f}$$



