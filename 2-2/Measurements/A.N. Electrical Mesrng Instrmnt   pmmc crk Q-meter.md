![[Pasted image 20260923125718.png|531]]![[Pasted image 20261010183959.png]]![[Pasted image 20261010185510.png|498]]![[Pasted image 20260923150632.png]]![[Pasted image 20260923151916.png]]![[Pasted image 20260923153649.png|442]]![[Pasted image 20260923165622.png]]
![[Pasted image 20261011172329.jpg]]
![[Pasted image 20261011182434.jpg]]![[Pasted image 20261011204939.jpg]]
![[Pasted image 20261011194756.png]]
![[Pasted image 20261011200312.png]]![[Pasted image 20261011233517.png]]
![[Pasted image 20261011233422.png]]![[Pasted image 20261011233429.png]]![[Pasted image 20261011233458.png]]
![[Pasted image 20261011235746.png]]

![[Pasted image 20261012000256.jpg]]![[Pasted image 20261012005958.png]]
![[Pasted image 20261012015142.jpg]]
![[Pasted image 20261012024030.png]]
![[Pasted image 20261012032933.png]]
![[Pasted image 20261012034139.jpg]]
#### 1. System Energy Storage

- Stored electrostatic energy in the capacitor:
    
    $$W = \frac{1}{2} C V^2$$
    

#### 2. Incremental Work & Energy Balance

- Charge relation:
    
    $$q = C V$$
    
- Differential charge entering the system under change of state:
    
    $$dq = d(C V) = V \, dC + C \, dV$$
    
- Input electrical energy supplied by the source:
    
    $$dW_e = V \, dq = V(V \, dC + C \, dV) = V^2 \, dC + C V \, dV$$
    
- Differential change in stored electrostatic field energy:
    
    $$dW = d\left(\frac{1}{2} C V^2\right) = \frac{1}{2} V^2 \, dC + C V \, dV$$
    
- Mechanical work performed during angular displacement $d\theta$:
    
    $$dW_m = T_d \, d\theta$$
    

#### 3. Energy Conservation & Deflecting Torque

- Conservation of energy:
    
    $$dW_e = dW + dW_m$$
    
- Direct substitution:
    
    $$V^2 \, dC + C V \, dV = \left(\frac{1}{2} V^2 \, dC + C V \, dV\right) + T_d \, d\theta$$
    
- Simplifying and canceling identical terms:
    
    $$V^2 \, dC - \frac{1}{2} V^2 \, dC = T_d \, d\theta$$
    
    $$\frac{1}{2} V^2 \, dC = T_d \, d\theta$$
    
- Deflecting torque ($T_d$):
    
    $$T_d = \frac{1}{2} V^2 \frac{dC}{d\theta}$$
    

#### 4. Linear Deflecting Force

- For linear displacement $dx$:
    
    $$dW_m = F_d \, dx$$
    
    $$F_d = \frac{1}{2} V^2 \frac{dC}{dx}$$

#### 1. Magnetic Field Stored Energy

- Stored magnetic energy in an inductor of inductance $L$ carrying current $I$:
    
    $$W = \frac{1}{2} L I^2$$
    

#### 2. Incremental Work & Energy Balance

- Total magnetic flux linkage:
    
    $$\lambda = L I$$
    
- Differential flux linkage during angular displacement $d\theta$:
    
    $$d\lambda = d(L I) = L \, dI + I \, dL$$
    
- Induced back EMF:
    
    $$e = \frac{d\lambda}{dt}$$
    
- Input electrical energy supplied by the source over time $dt$:
    
    $$dW_e = e \cdot I \cdot dt = \left(\frac{d\lambda}{dt}\right) I \, dt = I \, d\lambda$$
    
    $$dW_e = I(L \, dI + I \, dL) = I L \, dI + I^2 \, dL$$
    
- Differential change in stored magnetic energy:
    
    $$dW = d\left(\frac{1}{2} L I^2\right) = \frac{1}{2} L (2I \, dI) + \frac{1}{2} I^2 \, dL = I L \, dI + \frac{1}{2} I^2 \, dL$$
    
- Mechanical work performed by the deflecting torque $T_d$:
    
    $$dW_m = T_d \, d\theta$$
    

#### 3. Conservation of Energy & Deflecting Torque

- Energy conservation principle:
    
    $$dW_e = dW + dW_m$$
    
- Direct substitution:
    
    $$I L \, dI + I^2 \, dL = \left(I L \, dI + \frac{1}{2} I^2 \, dL\right) + T_d \, d\theta$$
    
- Canceling and simplifying terms:
    
    $$I^2 \, dL - \frac{1}{2} I^2 \, dL = T_d \, d\theta$$
    
    $$\frac{1}{2} I^2 \, dL = T_d \, d\theta$$
    
- Deflecting torque ($T_d$):
    
    $$T_d = \frac{1}{2} I^2 \frac{dL}{d\theta}$$

#### 1. Flux Linkages & Total Electrical Input Energy

- **Definitions:**
    
      
    - $i_1, i_2$ = instantaneous currents in fixed coil 1 and moving coil 2
        
          
        
    - $L_1, L_2$ = self-inductances of fixed and moving coils
        
          
        
    - $M$ = mutual inductance between the coils
        
          
        
- Total flux linkages of each coil:
    
      
    
    $$\lambda_1 = L_1 i_1 + M i_2$$
    
      
    
    $$\lambda_2 = L_2 i_2 + M i_1$$
    
      
    
- Induced electromotive forces:
    
      
    
    $$e_1 = \frac{d\lambda_1}{dt}, \quad e_2 = \frac{d\lambda_2}{dt}$$
    
      
    
- Differential electrical input energy supplied by sources:
    
      
    
    $$dW_e = e_1 i_1 \, dt + e_2 i_2 \, dt = i_1 \, d\lambda_1 + i_2 \, d\lambda_2$$
    
      
    
    $$dW_e = i_1 \, d(L_1 i_1 + M i_2) + i_2 \, d(L_2 i_2 + M i_1)$$
    
      
    
- Expanding differentials:
    
      
    
    $$dW_e = i_1 L_1 \, di_1 + i_1^2 \, dL_1 + i_1 i_2 \, dM + i_1 M \, di_2 + i_2 L_2 \, di_2 + i_2^2 \, dL_2 + i_1 i_2 \, dM + i_2 M \, di_1 \quad \text{--- (I)}$$
    
      
    

#### 2. Magnetic Stored Energy & Mechanical Work

- Energy stored in the magnetic field of coupled coils:
    
      
    
    $$W = \frac{1}{2} L_1 i_1^2 + \frac{1}{2} L_2 i_2^2 + i_1 i_2 M$$
    
      
    
- Differential change in stored energy:
    
      
    
    $$dW = d\left(\frac{1}{2} L_1 i_1^2 + \frac{1}{2} L_2 i_2^2 + i_1 i_2 M\right)$$
    
      
    
    $$dW = i_1 L_1 \, di_1 + \frac{1}{2} i_1^2 \, dL_1 + i_2 L_2 \, di_2 + \frac{1}{2} i_2^2 \, dL_2 + i_1 M \, di_2 + i_2 M \, di_1 + i_1 i_2 \, dM \quad \text{--- (II)}$$
    
      
    
- Principle of conservation of energy:
    
      
    
    $$\text{Electrical Input Energy } (dW_e) = \text{Change in Stored Energy } (dW) + \text{Mechanical Work Done } (dW_m)$$
    
      
    
    $$dW_m = dW_e - dW$$
    
      
    
- Subtracting Equation (II) from Equation (I):
    
      
    
    $$dW_m = \frac{1}{2} i_1^2 \, dL_1 + \frac{1}{2} i_2^2 \, dL_2 + i_1 i_2 \, dM$$
    
      
    
- Since self-inductances $L_1$ and $L_2$ are geometrically constant ($dL_1 = 0$, $dL_2 = 0$):
    
      
    
    $$dW_m = i_1 i_2 \, dM$$
    
      
    
- Expressing mechanical work in terms of deflecting torque $T_i$ and angular displacement $d\theta$:
    
      
    
    $$dW_m = T_i \, d\theta$$
    
      
    
    $$T_i \, d\theta = i_1 i_2 \, dM$$
    
      
    
- Instantaneous deflecting torque:
    
      
    
    $$T_i = i_1 i_2 \frac{dM}{d\theta}$$
    
      
    

#### 3. DC Operation & Steady-State Deflection

- For direct current ($i_1 = I_1$ and $i_2 = I_2$):
    
      
    
    $$T_d = I_1 I_2 \frac{dM}{d\theta}$$
    
      
    
- Restoring torque of control spring ($K$ = spring constant):
    
      
    
    $$T_c = K \theta$$
    
      
    
- Equilibrium condition ($T_d = T_c$):
    
      
    
    $$I_1 I_2 \frac{dM}{d\theta} = K \theta$$
    
      
    
- Steady-state deflection angle ($\theta$):
    
      
    
    $$\theta = \frac{I_1 I_2}{K} \frac{dM}{d\theta}$$
    
      
    

#### 4. AC Operation under Sinusoidal Currents

- Sinusoidal currents with phase difference $\phi$:
    
      
    
    $$i_1 = I_{m1} \sin(\omega t)$$
    
      
    
    $$i_2 = I_{m2} \sin(\omega t - \phi)$$
    
      
    
- Time-averaged deflecting torque over period $T$:
    
      
    
    $$T_d = \frac{1}{T} \int_{0}^{T} T_i \, dt = \frac{dM}{d\theta} \cdot \frac{1}{T} \int_{0}^{T} I_{m1} \sin(\omega t) \cdot I_{m2} \sin(\omega t - \phi) \, dt$$
    
      
    
    $$T_d = \frac{dM}{d\theta} \cdot \frac{I_{m1} I_{m2}}{2\pi} \int_{0}^{2\pi} \sin(\omega t) \sin(\omega t - \phi) \, d(\omega t)$$
    
      
    
    $$T_d = \frac{I_{m1} I_{m2}}{2} \cos\phi \frac{dM}{d\theta}$$
    
      
    
- Using RMS values ($I_1 = \frac{I_{m1}}{\sqrt{2}}$ and $I_2 = \frac{I_{m2}}{\sqrt{2}}$):
    
      
    
    $$T_d = I_1 I_2 \cos\phi \frac{dM}{d\theta}$$
    
      
    
- Equilibrium steady-state deflection ($T_d = T_c = K\theta$):
    
      
    
    $$\theta = \frac{I_1 I_2}{K} \cos\phi \frac{dM}{d\theta}$$
    
      
    

#### 5. Electrodynamometer Wattmeter: Instantaneous Torque

- Voltage applied to the pressure coil (P.C.) circuit:
    
      
    
    $$v = \sqrt{2} V \sin(\omega t)$$
    
      
    
- Current in purely resistive pressure coil ($R_p \gg \omega L_p$):
    
      
    
    $$i_p = \frac{v}{R_p} = \frac{\sqrt{2} V}{R_p} \sin(\omega t) = \sqrt{2} I_p \sin(\omega t) \quad \left(\text{where } I_p = \frac{V}{R_p}\right)$$
    
      
    
- Current in current coil (C.C.) lagging voltage by angle $\phi$:
    
      
    
    $$i_c = \sqrt{2} I \sin(\omega t - \phi)$$
    
      
    
- Instantaneous torque equation:
    
      
    
    $$T_i = i_p \, i_c \frac{dM}{d\theta} = \left[\sqrt{2} I_p \sin(\omega t)\right] \left[\sqrt{2} I \sin(\omega t - \phi)\right] \frac{dM}{d\theta}$$
    
      
    
    $$T_i = 2 I_p I \sin(\omega t) \sin(\omega t - \phi) \frac{dM}{d\theta}$$
    
      
    
- Using trigonometric identity $2 \sin A \sin B = \cos(A - B) - \cos(A + B)$:
    
      
    
    $$T_i = I_p I [\cos\phi - \cos(2\omega t - \phi)] \frac{dM}{d\theta}$$
    
      
    

#### 6. Wattmeter Average Deflecting Torque ($T_d$)

- Average deflecting torque integrated over cycle period $T$:
    
      
    
    $$T_d = \frac{1}{T} \int_{0}^{T} T_i \, d(\omega t)$$
    
      
    
    $$T_d = \frac{1}{T} \int_{0}^{T} I_p I [\cos\phi - \cos(2\omega t - \phi)] \frac{dM}{d\theta} \, d(\omega t)$$
    
      
    
- The double-frequency term $\cos(2\omega t - \phi)$ averages to zero over a full cycle:
    
      
    
    $$\frac{1}{T} \int_{0}^{T} \cos(2\omega t - \phi) \, d(\omega t) = 0$$
    
- Deflecting torque resulting from constant component:
    
      
    
    $$T_d = I_p I \cos\phi \frac{dM}{d\theta}$$
    
      
    
- Substituting $I_p = \frac{V}{R_p}$:
    
      
    
    $$T_d = \frac{V I}{R_p} \cos\phi \frac{dM}{d\theta}$$
    
      
    

#### 7. Wattmeter Scale Deflection & Measured Power

- Spring controlling torque:
    
      
    
    $$T_c = K \theta$$
    
      
    
- Equating average deflecting torque to restoring torque ($T_d = T_c$):
    
      
    
    $$K \theta = I_p I \cos\phi \frac{dM}{d\theta} = \frac{V I}{R_p} \cos\phi \frac{dM}{d\theta}$$
    
      
    
- Solving for steady deflection angle $\theta$:
    
      
    
    $$\theta = \frac{V I \cos\phi}{R_p K} \frac{dM}{d\theta}$$
    
      
    
- Defining instrument constant $K_1 = \frac{1}{R_p K}$:
    
      
    
    $$\theta = K_1 V I \cos\phi \frac{dM}{d\theta}$$
    
      
    
- Expressing in terms of true electrical power $P = V I \cos\phi$:
    
      
    
    $$\theta = \left(K_1 \frac{dM}{d\theta}\right) P$$
    
    $$\theta \propto P \quad \left(\text{for uniform } \frac{dM}{d\theta}\right)$$
#### 1. Lorentz Force on a Single Conductor

- Force on one vertical active conductor of length $l$ carrying current $I$ in magnetic flux density $B$:
    
    $$F_1 = B \cdot I \cdot l$$
    

#### 2. Total Force on Multi-Turn Coil

- For a rectangular coil having $N$ turns (giving $2N$ active vertical sides):
    
    $$F = N \cdot B \cdot I \cdot l$$
    

#### 3. Deflecting Torque ($T_d$)

- Deflecting torque produced by the force couple separated by coil width $d$:
    
    $$T_d = F \cdot d = (N \cdot B \cdot I \cdot l) \cdot d$$
    
- Area of the rectangular coil ($A = l \cdot d$):
    
    $$T_d = B \cdot I \cdot N \cdot A$$
    
- Defining the galvanometer displacement/torque constant $G = B \cdot N \cdot A$:
    
    $$T_d = G \cdot I$$
    

#### 4. Controlling Torque ($T_c$)

- Restoring torque exerted by the control spring with torsion constant $K$:
    
    $$T_c = K \cdot \theta$$
    

#### 5. Steady-State Equilibrium Deflection

- Equilibrium condition between deflecting and controlling torques:
    
    $$T_d = T_c$$
    
- Equating torque expressions:
    
    $$B \cdot I \cdot N \cdot A = K \cdot \theta$$
    
    $$G \cdot I = K \cdot \theta$$
    
- Steady-state angular deflection ($\theta$):
    
    $$\theta = \left(\frac{B \cdot N \cdot A}{K}\right) I = \left(\frac{G}{K}\right) I$$
    
- Current sensitivity ($S_i$):
    
    $$S_i = \frac{\theta}{I} = \frac{B \cdot N \cdot A}{K}$$

#### 1. Circuit Parameters & Notation

- Battery terminal voltage:
    
      
    
    $$E$$
    
- Basic meter internal resistance and meter current:
    
      
    
    $$R_m, \quad I_m$$
    
- Full-scale deflection (FSD) current of the meter movement:
    
      
    
    $$I_{fsd}$$
    
- Current limiting resistor:
    
      
    
    $$R_1$$
    
- Zero-adjusting parallel shunt resistor:
    
      
    
    $$R_2$$
    
- Unknown test resistor connected between terminals $A$ and $B$:
    
      
    
    $$R_x$$
    
- Equivalent parallel resistance of the meter and zero-adjust shunt $R_2$:
    
      
    
    $$R_p = \frac{R_2 R_m}{R_2 + R_m}$$
    

#### 2. Total Circuit Current & Meter Current Relation

- Current divider relation between meter current $I_m$ and total current $I_1$
- Meter current in terms of total current $I_1$:
    
      
    
    $$I_m = I_1 \left(\frac{R_2}{R_2 + R_m}\right)$$
    
- Total loop current $I_1$ with unknown resistor $R_x$ in series:   $R_h = R_1 + R_p$:
    
      
    
    $$I_1 = \frac{E}{R_x + R_1 + R_p}$$
    
- Resulting meter current:
    
      
    
    $$I_m = \left(\frac{E}{R_x + R_1 + R_p}\right) \left(\frac{R_2}{R_2 + R_m}\right)$$
    

#### 3. Full-Scale Deflection Condition ($R_x = 0$)

- Terminals $A$ and $B$ are shorted ($R_x = 0$) to set zero-resistance calibration ($I_m = I_{fsd}$):   $R_h = R_1 + R_p$:
    
      
    
    $$I_{1(0)} = \frac{E}{R_1 + R_p}$$
    
- Condition for meter pointer to indicate zero resistance at full-scale deflection: $R_h = R_1 + R_p$:
    
      
    
    $$I_{fsd} = I_{1(0)} \left(\frac{R_2}{R_2 + R_m}\right) = \left(\frac{E}{R_1 + R_p}\right) \left(\frac{R_2}{R_2 + R_m}\right)$$
    
- Solving for current-limiting resistor $R_1$:
    
      
    
    $$R_1 = \frac{E}{I_{fsd}} \left(\frac{R_2}{R_2 + R_m}\right) - R_p$$
    
    $$R_1 = \frac{E}{I_{1(0)}} - \frac{R_2 R_m}{R_2 + R_m}$$
    

#### 4. Fractional Scale Deflection ($s$)

- Ratio of meter current at unknown resistance $R_x$ to full-scale current ($s = I_m / I_{fsd}$):
    
      
    
    $$s = \frac{I_m}{I_{fsd}} = \frac{\left(\frac{E}{R_x + R_1 + R_p}\right) \left(\frac{R_2}{R_2 + R_m}\right)}{\left(\frac{E}{R_1 + R_p}\right) \left(\frac{R_2}{R_2 + R_m}\right)}$$
    
- Simplifying the ratio by defining the internal circuit resistance $R_h = R_1 + R_p$:
    
      
    
    $$s = \frac{R_1 + R_p}{R_x + R_1 + R_p} = \frac{R_h}{R_x + R_h}$$
    

#### 5. Half-Scale Deflection & Unknown Resistance ($R_x$)

- At half-scale deflection, $s = 0.5$ ($I_m = 0.5 \, I_{fsd}$):
    
      
    
    $$0.5 = \frac{R_h}{R_x + R_h}$$
    
    $$R_x + R_h = 2 R_h \implies R_x = R_h$$
    
- Half-scale resistance identity:
    
      
    
    $$R_h = R_{x(\text{half-scale})} = R_1 + \frac{R_2 R_m}{R_2 + R_m}$$
    
- General expression for unknown resistance $R_x$ as a function of deflection fraction $s$:
    
      
    
    $$R_x = R_h \left(\frac{1 - s}{s}\right)$$
    

#### 6. Zero Meter Current Condition ($R_x = \infty$)

- Terminals $A$ and $B$ are open-circuited ($R_x \to \infty$):
    
      
    
    $$I_1 = \lim_{R_x \to \infty} \frac{E}{R_x + R_h} = 0$$
    
    $$I_m = 0$$
    
- Scale mapping:
    
      
    - $R_x = 0 \implies I_m = I_{fsd}$ (Full-scale deflection on the right)
        
          
        
    - $R_x = R_h \implies I_m = 0.5 \, I_{fsd}$ (Half-scale deflection at center)
        
          
        
    - $R_x = \infty \implies I_m = 0$ (Zero deflection on the left)
#### shunt type ohmmeter
- Defining the Thévenin equivalent internal resistance looking back from the meter terminals:
    
    $$R_h = R_1 \parallel R_m = \frac{R_1 R_m}{R_1 + R_m}$$
    
- Deflection fraction in terms of $R_h$:
    
    $$s = \frac{R_x}{R_h + R_x}$$
    

#### 5. Half-Scale Deflection Condition ($s = 0.5$)

- At mid-scale deflection, meter current is half of full scale:
    
    $$I_m = 0.5 \, I_{fsd} \implies s = 0.5$$
    
- Equating with the fractional deflection expression:
    
    $$0.5 = \frac{R_x}{R_h + R_x}$$
    
    $$0.5(R_h + R_x) = R_x$$
    
    $$0.5 R_h + 0.5 R_x = R_x$$
    
    $$0.5 R_h = 0.5 R_x$$
    
    $$R_x = R_h$$
    
- Half-scale calibration resistance identity:
    
    $$R_h = R_{x(\text{half-scale})} = \frac{R_1 R_m}{R_1 + R_m}$$
    

#### 6. Mathematical Expression for Unknown Resistance ($R_x$)

- Starting from fractional deflection relation:
    
    $$s(R_h + R_x) = R_x$$
    
    $$s R_h + s R_x = R_x$$
    
    $$s R_h = R_x(1 - s)$$
    
- Unknown test resistance as a function of deflection fraction $s$:
    
    $$R_x = R_h \left(\frac{s}{1 - s}\right)$$
#### 1. The Big Picture: How the Meter Works

- **The Goal of the Meter:**
    
      
    - It measures the total amount of electrical energy consumed by a household or circuit over time.
        
          
        
    - It behaves like a tiny electric motor that spins an aluminium disc.
        
          
        
    - The spinning speed of the disc is made to match the real electrical power being used at that exact moment.
        
          
        

#### 2. Creating the Two Magnetic Fluxes

- **Voltage Magnet (Pressure Coil):**
    
      
    - Connected across the main supply voltage $V$.
        
          
        
    - It has many fine wire turns and high magnetic inductance.
        
          
        
    - This coil produces an alternating magnetic flux $\Phi_p$ that is proportional to voltage $V$ and lags behind it by an angle $\Delta$ (which is designed to be close to $90^\circ$).
        
          
        
- **Current Magnet (Current Coil):**
    
      
    - Connected in series with the load.
        
          
        
    - The actual load current $I$ passes directly through it.
        
          
        
    - It produces a magnetic flux $\Phi_s$ that is directly proportional to and in step (in phase) with the load current $I$.
        
          
        

#### 3. Why the Disc Spins (Eddy Currents & Forces)

- **Inducing Eddy Currents in the Disc:**
    
      
    - Both alternating fluxes ($\Phi_p$ and $\Phi_s$) shoot downward through the flat aluminium disc.
        
          
        
    - Because these magnetic fields are constantly changing, they induce small swirling loops of electric current inside the metal disc, called **eddy currents**.
        
          
        
    - Flux $\Phi_p$ induces eddy current $I_{ep}$, while flux $\Phi_s$ induces eddy current $I_{es}$.
        
          
        
- **Cross-Action Push (Driving Torque):**
    
      
    - The eddy current $I_{es}$ gets pushed sideways by the magnetic field $\Phi_p$.
        
          
        
    - At the same time, the eddy current $I_{ep}$ gets pushed in the reverse direction by the magnetic field $\Phi_s$.
        
          
        
    - These two opposing forces act at different spots on the disc.
        
          
        
    - The overall difference between these two pushes creates a net twisting force called the **driving torque** ($T_d$), which forces the disc to rotate.
        
          
        

#### 4. The Driving Torque Formula Step-by-Step

- **General Torque Formula:**
    
      
    - For any induction instrument, the twisting torque created between two alternating fluxes is given by:
        
          
        
        $$T_d \propto \Phi_1 \Phi_2 \frac{f}{Z} \sin\beta \cos\alpha$$
        
          
        
    - Here, the two working fluxes are $\Phi_p$ and $\Phi_s$.
        
          
        
    - The angle between these two magnetic fluxes on the phasor diagram is $\beta = (\Delta - \phi)$, where $\phi$ is the phase angle of the load.
        
          
        
- **Putting in Voltage and Current:**
    
      
    - The pressure coil flux depends on voltage ($\Phi_p \propto V$).
        
          
        
    - The current coil flux depends on current ($\Phi_s \propto I$).
        
          
        
    - Substituting these relationships into the torque formula gives:
        
          
        
        $$T_d = K_3 V I \frac{f}{Z} \sin(\Delta - \phi) \cos\alpha$$
        
          
        
- **Simplifying the Constants:**
    
      
    - In a standard electrical grid, the supply frequency $f$, disc impedance $Z$, and internal disc phase angle $\alpha$ stay constant.
        
          
        
    - Combining them into a single constant $K_3$ simplifies the driving torque equation to:
        
          
        
        $$T_d = K_3 V I \sin(\Delta - \phi)$$
        
          
        

#### 5. Balancing Speed with the Brake Magnet

- **Why a Brake is Needed:**
    
      
    - Without resistance, the driving torque would make the disc spin faster and faster without stopping.
        
          
        
    - A permanent magnet placed near the rim creates a resisting **braking torque** ($T_b$).
        
          
        
- **Braking Torque Proportional to Speed:**
    
      
    - The faster the disc spins at speed $N$, the stronger the braking resistance becomes:
        
          
        
        $$T_b = K_4 N$$
        
          
        
- **Reaching Steady Speed:**
    
      
    - When the forward drive torque matches the backward braking torque ($T_d = T_b$):
        
          
        
        $$K_4 N = K_3 V I \sin(\Delta - \phi)$$
        
          
        
    - Solving for the disc rotational speed $N$:
        
          
        
        $$N = K V I \sin(\Delta - \phi)$$
        
          
        

#### 6. Why the $90^\circ$ Condition ($\Delta = 90^\circ$) Matters

- **Matching Real Electrical Power:**
    
      
    - The actual electrical power used by any AC appliance is:
        
          
        
        $$\text{Power} = V I \cos\phi$$
        
          
        
    - To make the disc speed $N$ directly reflect real power, the term $\sin(\Delta - \phi)$ must become equal to $\cos\phi$.
        
          
        
    - From basic trigonometry, $\sin(90^\circ - \phi) = \cos\phi$.
        
          
        
- **Adjusting to Exactly $90^\circ$:**
    
      
    - Copper shading bands on the voltage core are adjusted so that the flux lags voltage by exactly $\Delta = 90^\circ$.
        
          
        
    - When $\Delta = 90^\circ$, the speed equation becomes:
        
          
        
        $$N = K V I \sin(90^\circ - \phi) = K V I \cos\phi$$
        
          
        
        $$N = K \times (\text{Power})$$
        
          
        
    - **Result:** The rotational speed of the disc is directly proportional to the true power consumed.
        
          
        

#### 7. Recording Total Energy Consumed

- **Total Revolutions as Energy:**
    
      
    - Energy is simply power consumed multiplied by time.
        
          
        
    - Adding up all disc rotations over time gives the total number of revolutions:
        
          
        
        $$\text{Total Revolutions} = \int N \, dt = K \int V I \cos\phi \, dt$$
        
          
        
        $$\text{Total Revolutions} = K \int (\text{Power}) \, dt = K \times (\text{Energy})$$
        
          
        
- **Reading the Value:**
    
      
    - Every single turn of the disc represents a fixed fraction of energy.
        
          
        
    - A gear system connected to the spindle turns the dial pointers to register the total kilowatt-hours ($\text{kWh}$) used.
#### 1. What This Meter Does & Basic Concept

- **Purpose:** This instrument measures the electrical frequency of an AC power supply by using electrical resonance.
    
- **No Spring Needed:** Unlike ordinary meters, it has no control hairsprings to hold or restore the pointer.
    
- **Self-Balancing Mechanism:** The moving coil naturally glides along an iron core until electrical resonance ($X_L = X_C$) is reached, where all mechanical torque drops to zero.
    

#### 2. Key Components (Construction)

- **Magnetizing Coil (Fixed Coil):**
    
    - Connected across the AC supply line whose frequency is being measured.
        
    - It acts as the primary field coil and sets up an alternating magnetic flux $\Phi$.
        
- **Tapered Laminated Iron Core:**
    
    - Placed inside the magnetizing coil.
        
    - Its cross-sectional thickness varies gradually along its length: it is thickest near the magnetizing coil and thinnest at the outer free end.
        
- **Moving Coil & Pointer:**
    
    - A light coil free to slide along the tapered iron core.
        
    - A pointer is attached to it to indicate the frequency value on a dial.
        
- **Tuning Capacitor ($C$):**
    
    - Connected directly across the terminals of the moving coil to create a series resonant $L\text{--}C$ circuit.
        

#### 3. How the Moving Coil Generates Torque

- **Induced Voltage:**
    
    - The magnetizing coil creates an alternating flux $\Phi$ that cuts the moving coil.
        
    - This induces an alternating EMF $E$ in the moving coil that lags the flux $\Phi$ by $90^\circ$.
        
- **Induced Current ($I_2$):**
    
    - The induced voltage drives an internal circulating current $I_2$ through the moving coil and capacitor $C$.
        
    - The phase of $I_2$ depends on the balance between inductive reactance ($X_L$) and capacitive reactance ($X_C$).
        
- **Torque Under Three Circuit Conditions:**
    
    - **Inductive ($X_L > X_C$):** Current $I_2$ lags voltage $E$, producing a forward deflecting torque:
        
        $$T_d = I I_2 \cos(90^\circ + \alpha)$$
        
    - **Capacitive ($X_L < X_C$):** Current $I_2$ leads voltage $E$, producing a reverse deflecting torque:
        
        $$T_d = I I_2 \cos(90^\circ - \beta)$$
        
    - **Resonance ($X_L = X_C$):** Circuit is purely resistive, making $I_2$ perfectly in phase with $E$ ($90^\circ$ away from flux $\Phi$).
        
        $$T_d = I I_2 \cos(90^\circ) = 0$$
        
    - **Key takeaway:** The net deflecting torque on the moving coil is **zero** whenever $X_L = X_C$.
        

#### 4. The Role of the Tapered Iron Core

- **Constant Capacitance vs. Variable Inductance:**
    
    - For a given supply frequency, capacitor reactance $X_C = \frac{1}{2\pi f C}$ remains constant.
        
    - However, the inductance $L$ of the moving coil depends on its exact physical position along the tapered core.
        
- **Position Determines Inductance:**
    
    - When the moving coil sits near the magnetizing coil (thick core area), the magnetic path is heavy, making $L$ and $X_L$ maximum.
        
    - When the moving coil moves away toward the narrow end (thin core area), $L$ and $X_L$ decrease to a minimum.
        
- **Center Calibration:**
    
    - The value of capacitor $C$ is chosen so that at normal rated frequency (e.g., $50\text{ Hz}$), resonance ($X_L = X_C$) occurs exactly when the coil rests at the center of the core.
        
    - At this center spot, torque is zero, keeping the pointer steady at the center "Normal Frequency" mark.
        

#### 5. How It Measures Frequency Changes

- **When Frequency Rises Above Normal ($f \uparrow$):**
    
    - Inductive reactance increases ($X_L = 2\pi f L \uparrow$) and capacitive reactance drops ($X_C = \frac{1}{2\pi f C} \downarrow$), making $X_L > X_C$.
        
    - The circuit becomes inductive, generating a torque that repels the moving coil away from the magnetizing coil.
        
    - As the coil slides toward the thinner end of the core, its inductance $L$ naturally decreases.
        
    - Movement stops once $X_L$ drops enough to equal $X_C$ again ($T_d = 0$), pointing to a higher frequency reading.
        
- **When Frequency Drops Below Normal ($f \downarrow$):**
    
    - Capacitive reactance increases and inductive reactance drops, making $X_C > X_L$.
        
    - The circuit becomes capacitive, generating an opposite torque that pulls the coil closer toward the magnetizing coil.
        
    - Moving onto the thicker core section raises its inductance $L$.
        
    - The coil stops moving once $X_L$ rises to match $X_C$ again ($T_d = 0$), pointing to a lower frequency reading.
#### 4. Pointer Deflection and Scale Alignment

- **Mechanical Pivot Dynamics:**
    
    - The moving system is supported by a central pivot located above the core.
        
    - The moving coil assembly extends below the pivot, while the pointer needle extends upward to the dial scale.
        
    - This configuration functions as a lever about the pivot point:
        
        - When measuring a **lower frequency**, the moving coil shifts rightward toward the magnetizing coil (thicker section). The pointer tip above the pivot tilts to the left, pointing to the **"Lower"** marking on the scale.
            
        - When measuring a **higher frequency**, the moving coil shifts leftward toward the free end (thinner section). The pointer tip above the pivot tilts to the right, pointing to the **"Higher"** marking on the scale.
#### What is a Power Factor Meter?

- A **Power Factor Meter** measures the phase difference between alternating current and voltage in an electrical circuit, telling you how efficiently electrical power is being used.
    
      
    
- Instead of calculating current, voltage, and power separately, this instrument directly indicates whether the circuit's power factor is **leading**, **lagging**, or at **unity (1.0)**.
    
      
    

#### Main Parts and Construction

- **Fixed Coil (Current Coil):**
    
      
    - Placed in a stationary position and split into two equal halves.
        
          
        
    - Connected in series with the load so that it carries the entire circuit current.
        
          
        
    - Produces an alternating magnetic field that is directly proportional to the load current.
        
          
        
- **Moving Coils (Pressure / Voltage Coils A and B):**
    
      
    - Two identical coils mounted together on a central rotating spindle at a right angle ($90^\circ$) to each other.
        
          
        
    - Both coils are connected in parallel across the main supply voltage.
        
          
        
    - A pointer is attached to this moving spindle to sweep across the calibrated scale.
        
          
        
- **Auxiliary Circuit Elements:**
    
      
    - **Coil A** is connected in series with a pure **resistor ($R$)**, making the current through Coil A ($I_A$) stay in phase with the voltage.
        
          
        
    - **Coil B** is connected in series with an **inductor/choke coil ($L$)**, making the current through Coil B ($I_B$) lag behind the voltage by $90^\circ$.
        
          
        
    - The components are matched such that $R = \omega L$, ensuring equal current magnitudes pass through both coils under normal operating frequency.
        
          
        
- **Absence of Control Springs:**
    
      
    - Unlike ordinary meters, this meter has **no control spring**.
        
          
        
    - Current is led into the moving coils using extremely thin, flexible silver or gold strips (ligaments) that exert negligible controlling torque.
        
          
        
    - The pointer's position is governed entirely by electrical torques.
        
          
        

#### Working Principle and Theory

- **Two Competing Torques:**
    
      
    - When current flows, the magnetic field of the fixed coil interacts with the magnetic fields produced by coils **A** and **B**.
        
          
        
    - This interaction creates two rotational forces (deflecting torques), $T_A$ and $T_B$.
        
          
        
    - The coils are wound in opposite directions, causing $T_A$ to push the pointer in a **clockwise direction** and $T_B$ to push it in a **counter-clockwise direction**.
        
          
        
- **Deflection Torque Equations (Lagging Power Factor $\cos\phi$):**
    
      
    - Torque on Coil A:
        
          
        
        $$T_A = K V I M_{\max} \cos\phi \sin\theta$$
        
          
        
    - Torque on Coil B:
        
          
        
        $$T_B = K V I M_{\max} \cos(90^\circ - \phi) \sin(90^\circ + \theta) = K V I M_{\max} \sin\phi \cos\theta$$
        
          
        
    - Here, $V$ is supply voltage, $I$ is circuit current, $\phi$ is the phase angle of the load, $\theta$ is the angle of pointer deflection, and $M_{\max}$ is the maximum mutual inductance.
        
          
        
- **Balance Condition (Equilibrium):**
    
      
    - The moving system rotates until the two opposing torques perfectly balance each other ($T_A = T_B$):
        
          
        
        $$K V I M_{\max} \cos\phi \sin\theta = K V I M_{\max} \sin\phi \cos\theta$$
        
          
        
    - Dividing both sides by $K V I M_{\max}$ and rearranging gives:
        
          
        
        $$\frac{\sin\theta}{\cos\theta} = \frac{\sin\phi}{\cos\phi} \implies \tan\theta = \tan\phi$$
        
    - Therefore:
        
          
        
        $$\theta = \phi$$
        
          
        

#### Key Takeaway

- The physical angle of rotation of the pointer ($\theta$) is directly equal to the phase angle of the circuit ($\phi$).
    
      
    
- When the circuit is purely resistive ($\phi = 0^\circ$), the pointer rests at **1.0 (Unity)**.
    
      
    
- If current lags voltage ($\phi > 0^\circ$), the pointer deflects toward the **Lag** side; if it leads, the pointer deflects toward the **Lead** side.
#### 2. Stroboscopic Method Basics

- **Concept:**
    
    - Uses a variable-frequency flashing light directed at a rotating shaft carrying a distinctive mark.
        
    - When the shaft rotates exactly once (or an integer multiple of revolutions) between flashes, the mark is illuminated at the exact same physical spot each time, appearing **stationary** to the human eye.
        
- **Single-Mark Condition:**
    
    - Appears stationary as a single image when:
        
        $$n = f$$
        
        _(where $n$ is shaft speed in rps, and $f$ is flashing frequency in Hz)_.
        
    - A single stationary image also occurs whenever the shaft speed is an exact integer multiple of flash frequency ($n = 2f, 3f, \dots$).
        
    - If flash frequency exceeds shaft speed ($f > n$), multiple stationary images appear simultaneously (e.g., if $f = 2n$, two diametrically opposite images appear).
    - the shaft speed $n$:

$$n = \frac{f_{H} f_{L} (m - 1)}{f_{H} - f_{L}}$$

_(where $m$ is the number of freeze points/patterns passed, $f_H$ is the higher flash rate, and $f_L$ is the lower flash rate)_.