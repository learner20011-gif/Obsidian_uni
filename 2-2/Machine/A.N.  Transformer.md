![[Pasted image 20261023171933.jpg]]

![[Pasted image 20260908231027.png]]
![[Pasted image 20260908231224.png]]
![[Pasted image 20260908231042.png]]
![[Pasted image 20260908231137.png]]
![[Pasted image 20260908234257.png]]![[Pasted image 20261023181304.png]]

![[Pasted image 20261023190508.png]]
![[Pasted image 20261023220144.png|409]]

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