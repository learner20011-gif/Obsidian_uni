![[Pasted image 20261023171933.jpg]]

![[Pasted image 20260908231027.png]]
![[Pasted image 20260908231224.png]]
![[Pasted image 20260908231042.png]]
![[Pasted image 20260908231137.png]]
![[Pasted image 20260908234257.png]]![[Pasted image 20261023181304.png]]

![[Pasted image 20261023190508.png]]
![[Pasted image 20261023220144.png|409]]
![[Pasted image 20261024001740.png]]
![[Pasted image 20260909024726.png]]
![[Pasted image 20261024014932.png]]
![[Pasted image 20261024023820.png]]
* **Real Transformer Equations:**
  $$\vec{V_1} = -\vec{E_1} + \vec{I_1} R_1 + j \vec{I_1} X_1$$
  $$\vec{V_2} = \vec{E_2} - \vec{I_2} R_2 - j \vec{I_2} X_2$$
  $$\vec{I_1} = \vec{I_0} + \vec{I_2'}$$
- **Instantaneous Induced EMF:** According to Faraday’s law and Lenz’s law, the back EMF $e_1(t)$ induced in the primary winding of $N_1$ turns opposes the rate of change of flux:
    
    $$e_1(t) = -N_1 \frac{d\phi(t)}{dt} = -N_1 \frac{d}{dt}\left[\Phi_m \sin(\omega t)\right]$$
    
    $$e_1(t) = -N_1 \omega \Phi_m \cos(\omega t) = N_1 \omega \Phi_m \sin\left(\omega t - \frac{\pi}{2}\right)$$
    
- **Peak and RMS Values:**
    
    - The maximum (peak) induced voltage is:
        
        $$E_{1,\text{max}} = N_1 \omega \Phi_m = 2\pi f N_1 \Phi_m$$
        
    - For a sinusoidal waveform, the root-mean-square ($\text{RMS}$) value $E_1$ is obtained by dividing the peak value by $\sqrt{2}$:
        
        $$E_1 = \frac{E_{1,\text{max}}}{\sqrt{2}} = \frac{2\pi f N_1 \Phi_m}{\sqrt{2}} = \sqrt{2}\pi \cdot f \cdot N_1 \cdot \Phi_m$$

- From secondary phasor diagram for a lagging load ($I_2$ lags $V_2$ by $\phi_2$):
  $${}_0V_2 = \sqrt{(V_2 \cos\phi_2 + I_2 R_{02})^2 + (V_2 \sin\phi_2 + I_2 X_{02})^2}$$
- $$E_2 \approx V_2 + I_2 R_{02} \cos \phi \pm I_2 X_{02} \sin \phi$$

$$E_2 - V_2 \approx I_2 R_{02} \cos \phi \pm I_2 X_{02} \sin \phi$$

$$\%\text{VR} = \frac{E_2 - V_2}{V_2} \times 100\%$$

$$\%\text{VR} = \left(\frac{I_2 R_{02} \cos \phi \pm I_2 X_{02} \sin \phi}{V_2}\right) \times 100\%$$

$$\%\text{VR} = \left(\frac{I_2 R_{02}}{V_2} \times 100\%\right) \cos \phi \pm \left(\frac{I_2 X_{02}}{V_2} \times 100\%\right) \sin \phi$$

$$v_r = \frac{I_2 R_{02}}{V_2} \times 100\%$$

$$v_x = \frac{I_2 X_{02}}{V_2} \times 100\%$$

$$\%\text{VR} = v_r \cos \phi \pm v_x \sin \phi$$

#### 1. The Word Trick: "SH - OL" (or "SHOE")

- **S - H**: **S**hort-Circuit Test $\rightarrow$ Instruments on **H**V side.
    
- **O - L**: **O**pen-Circuit Test $\rightarrow$ Instruments on **L**V side.
    
- **How to recall:** Remember the word **"SHOL"** (pronounced like "Soul" or "Shoal") or **"SHOE"** (**SH**ort on High, **O**pen on Low).
- **Current Handling:** The SC test requires circulating **rated full-load current** through the windings.
- **Voltage Availability:** The OC test requires **rated voltage** to produce rated magnetic flux in the core.
#### Open-Circuit (OC) Test Procedure

- **Setup:** Apply full rated voltage to the low-voltage (LV) side and leave the high-voltage (HV) side open-circuited.
    
      
    
- **Measurements:** Record the open-circuit Voltmeter ($V_0$), Ammeter ($I_0$), and Wattmeter ($W_0$) readings.
    
      
    
- **Core Loss ($P_i$):**
    
      
    
    $$P_i = W_0$$
    
- **Core Resistance ($R_0$ or $R_C$):** Calculated directly from power and voltage (parallel branch):
    
      
    
    $$R_0 = \frac{V_0^2}{W_0}$$
    
- **Magnetizing Reactance ($X_0$ or $X_M$):** Found using the working current ($I_w$) and magnetizing current ($I_m$):
    
      
    
    $$X_0 = \frac{V_0}{I_m} \quad \text{where} \quad I_w = \frac{W_0}{V_0} \quad \text{and} \quad I_m = \sqrt{I_0^2 - I_w^2}$$
    
    _(Or directly from power and resistance: $X_0 = \frac{V_0}{\sqrt{I_0^2 - (W_0/V_0)^2}}$)_
    
      
    **Step 1: Shunt Branch Parameters from OC Test (on LV side)**
* No-load power factor: $\cos\phi_0 = \frac{W_0}{V_0 I_0} = \frac{80}{120 \times 4.2} = \frac{80}{504} \approx 0.1587$
* Core-loss current: $I_w = I_0 \cos\phi_0 = \frac{80}{120} \approx 0.667\text{ A}$
* Magnetizing current: $I_m = \sqrt{I_0^2 - I_w^2} = \sqrt{(4.2)^2 - (0.667)^2} = \sqrt{17.64 - 0.445} \approx 4.147\text{ A}$
* Core-loss resistance (LV): $R_{0(\text{LV})} = \frac{V_0}{I_w} = \frac{120}{0.667} \approx \mathbf{180\ \Omega}$
* Magnetizing reactance (LV): $X_{0(\text{LV})} = \frac{V_0}{I_m} = \frac{120}{4.147} \approx \mathbf{28.94\ \Omega}$

#### Short-Circuit (SC) Test Procedure

- **Setup:** Short-circuit the low-voltage (LV) terminals and apply a low variable voltage (2%–12% of rated voltage) to the high-voltage (HV) side until rated current flows.
    
      
    
- **Measurements:** Record the short-circuit Voltmeter ($V_{SC}$), Ammeter ($I_{SC}$), and Wattmeter ($W_{SC}$) readings.
    
      
    
- **Copper Loss ($P_{cu}$):**
    
      
    
    $$P_{cu} = W_{SC}$$
    
- **Equivalent Resistance ($R_{eq}$):** Calculated directly from power and current (series branch):
    
      
    
    $$R_{eq} = \frac{W_{SC}}{I_{SC}^2}$$
    
- **Equivalent Reactance ($X_{eq}$):** Found using the total series impedance ($Z_{SE}$) and resistance ($R_{eq}$):
    
      
    
    $$X_{eq} = \sqrt{Z_{SE}^2 - R_{eq}^2} \quad \text{where} \quad Z_{SE} = \frac{V_{SC}}{I_{SC}}$$
#### Open-Circuit Test (OCT)

- **Purpose:** Finds core loss resistance ($R_C$) and magnetizing reactance ($X_M$) connected in parallel. Usually tested on the low-voltage side.
    
      
    
- **Step 1 (Admittance Magnitude):**
    
      
    
    $$\vert{}Y_E\vert{} = \frac{I_{OC}}{V_{OC}}$$
    
      
    
- **Step 2 (Power Factor Angle):**
    
      
    
    $$\theta = \arccos\left(\frac{P_{OC}}{V_{OC} I_{OC}}\right)$$
    
      
    
- **Step 3 (Admittance in Rectangular Form):**
    
      
    
    $$Y_E = \vert{}Y_E\vert{} \angle -\theta = G_C - j B_M$$
    
      
    
- **Step 4 (Component Values):**
    
      
    
    $$R_C = \frac{1}{G_C}, \quad X_M = \frac{1}{B_M}$$
    
      
    

#### Short-Circuit Test (SCT)

- **Purpose:** Finds total series winding resistance ($R_{eq}$) and leakage reactance ($X_{eq}$) connected in series. Usually tested on the high-voltage side.
    
      
    
- **Step 1 (Impedance Magnitude):**
    
      
    
    $$\vert{}Z_{SE}\vert{} = \frac{V_{SC}}{I_{SC}}$$
    
      
    
- **Step 2 (Power Factor Angle):**
    
      
    
    $$\theta = \arccos\left(\frac{P_{SC}}{V_{SC} I_{SC}}\right)$$
    
      
    
- **Step 3 (Impedance in Rectangular Form):**
    
      
    
    $$Z_{SE} = \vert{}Z_{SE}\vert{} \angle \theta = R_{eq} + j X_{eq}$$
    
      
    
- **Step 4 (Component Values):**
    
      
    
    $$R_{eq} = \vert{}Z_{SE}\vert{}\cos\theta, \quad X_{eq} = \vert{}Z_{SE}\vert{}\sin\theta$$
    #### 1. Transformer Efficiency ($\eta$) Formula

- **Basic Equation:** Efficiency is output power divided by input power (output + losses):
    
    $$\eta = \frac{\text{Output Power}}{\text{Input Power}} = \frac{V_2 I_2 \cos\theta_2}{V_2 I_2 \cos\theta_2 + P_c + I_2^2 r_{e2}}$$
    
- **Variables:**
    
    - $V_2 I_2 \cos\theta_2 =$ Output power
        
    - $P_c =$ Constant core (iron) loss
        
    - $I_2^2 r_{e2} =$ Variable copper (ohmic) loss
        

#### 2. Condition for Maximum Efficiency (With Variable Load Current $I_2$)

- **Step 1 (Set up Efficiency Equation):** In the efficiency formula, core loss ($P_c$), secondary voltage ($V_2$), and power factor ($\cos\theta_2$) are constant, while load current ($I_2$) varies.
    
- **Step 2 (Differentiate with respect to $I_2$):** For maximum efficiency, set $\frac{d\eta}{dI_2} = 0$ using the quotient rule:
    
    $$\frac{d\eta}{dI_2} = \frac{(V_2 I_2 \cos\theta_2 + P_c + I_2^2 r_{e2})(V_2 \cos\theta_2) - (V_2 I_2 \cos\theta_2)(V_2 \cos\theta_2 + 2 I_2 r_{e2})}{(V_2 I_2 \cos\theta_2 + P_c + I_2^2 r_{e2})^2} = 0$$
    
- **Step 3 (Simplify Numerator = 0):** Multiply the denominator by zero and divide both terms by $V_2 \cos\theta_2$:
    
    $$(V_2 I_2 \cos\theta_2 + P_c + I_2^2 r_{e2}) = I_2 (V_2 \cos\theta_2 + 2 I_2 r_{e2})$$
    
    $$V_2 I_2 \cos\theta_2 + P_c + I_2^2 r_{e2} = V_2 I_2 \cos\theta_2 + 2 I_2^2 r_{e2}$$
    
- **Step 4 (Final Condition):** Cancel $V_2 I_2 \cos\theta_2$ and subtract $I_2^2 r_{e2}$ from both sides:
    
    $$I_2^2 r_{e2} = P_c$$
    
    (Rule: Maximum efficiency occurs when **Variable Copper Loss = Constant Core Loss**.)
    

#### 3. Load Current & kVA at Maximum Efficiency

- **Load Current ($I_2$) at $\eta_{\max}$:** Solve $I_2^2 r_{e2} = P_c$ for $I_2$, and relate it to full-load current ($I_{fl}$):
    
    $$I_2 = \sqrt{\frac{P_c}{r_{e2}}} = I_{fl} \sqrt{\frac{P_c}{I_{fl}^2 r_{e2}}} = I_{fl} \sqrt{\frac{\text{Core Loss}}{\text{Full-Load Copper Loss}}}$$
    
- **kVA Load at $\eta_{\max}$:** Multiply both sides by $\frac{E_2}{1000}$:
    
    $$\text{kVA}_{\max\text{-}\eta} = \text{Rated kVA} \times \sqrt{\frac{P_c}{I_{fl}^2 r_{e2}}} = \text{Rated kVA} \times \sqrt{\frac{\text{Core Loss}}{\text{Full-Load Copper Loss}}}$$
    
**Fractional Load Multiplier ($x$):** If a transformer operates at a fraction $x$ of a reference load ($\text{kVA}_{\text{ref}}$):

$$x = \frac{\text{Operating kVA}}{\text{Reference kVA}} = \frac{S}{S_{\text{ref}}}$$

$$P_{cu}(x) = x^2 \times P_{cu(\text{ref})} = \left(\frac{S}{S_{\text{ref}}}\right)^2 \times P_{cu(\text{ref})}$$
#### 4. Condition for Maximum Efficiency (With Variable Power Factor $\cos\theta_2$)

- **Step 1 (Constant Current Setup):** If load current ($I_2$) is kept constant, both core loss ($P_c$) and copper loss ($P_{sc}$) are constant. Let total constant loss $C = P_c + P_{sc}$:
    
    $$\eta = \frac{V_2 I_2 \cos\theta_2}{V_2 I_2 \cos\theta_2 + C}$$
    
- **Step 2 (Differentiate with respect to $\theta_2$):** For maximum efficiency, set $\frac{d\eta}{d\theta_2} = 0$:
    
    $$\frac{d\eta}{d\theta_2} = \frac{(V_2 I_2 \cos\theta_2 + C)(-V_2 I_2 \sin\theta_2) - (V_2 I_2 \cos\theta_2)(-V_2 I_2 \sin\theta_2)}{(V_2 I_2 \cos\theta_2 + C)^2} = 0$$
    
- **Step 3 (Simplify Numerator = 0):**
    
    $$-(V_2 I_2)^2 \sin\theta_2 \cos\theta_2 - C V_2 I_2 \sin\theta_2 + (V_2 I_2)^2 \sin\theta_2 \cos\theta_2 = 0$$
    
    $$C V_2 I_2 \sin\theta_2 = 0 \implies \sin\theta_2 = 0$$
    
- **Step 4 (Final Condition):** Since $\sin\theta_2 = 0$, the phase angle is $\theta_2 = 0^\circ$:
    
    $$\cos\theta_2 = 1 \quad (\text{Unity Power Factor})$$
    
- **Key Takeaways:**
    
    - The **load current ($I_2$)** at which $\eta_{\max}$ occurs does **not** depend on power factor (since $P_c$ and $r_{e2}$ don't change with p.f.).
        
    - Lowering the power factor reduces output power ($V_2 I_2 \cos\theta_2$), which lowers the overall efficiency curve.
