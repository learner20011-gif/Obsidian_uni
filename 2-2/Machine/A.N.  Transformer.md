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