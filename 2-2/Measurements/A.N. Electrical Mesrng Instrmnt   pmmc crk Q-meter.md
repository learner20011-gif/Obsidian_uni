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
![[Pasted image 20261012043031.png|450]]
![[Pasted image 20261012045049.png]]![[Pasted image 20261012173046.png|491]]![[Pasted image 20261012172022.png]]
![[Pasted image 20261012191748.png]]
![[Pasted image 20261012192226.png]]
![[Pasted image 20261012192851.jpg]]
![[Pasted image 20261012202536.png]]
![[Pasted image 20261012210620.png|513]]
![[Pasted image 20261012232052.png]]
![[Pasted image 20261012232116.png]]
![[Pasted image 20261013004517.png]]![[Pasted image 20261013004458.png]]
![[Pasted image 20261013004450.png]]
![[Pasted image 20261013004916.png]]
![[Pasted image 20261013030047.png]]
![[Pasted image 20261013030657.png]]

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

#### Overview of the Flux Meter Derivation

- The goal of this mathematical derivation is to prove that the mechanical deflection of the flux meter pointer ($\theta$) is directly proportional to the total change in magnetic flux ($\Delta\Phi$) linking the search coil.
    
      
    
- The derivation combines two fundamental domains:
    
      
    - The **electrical circuit domain**, using Kirchhoff's Voltage Law (KVL) and Faraday's Law of Induction.
        
          
        
    - The **mechanical moving system domain**, using Newton's rotational equation of motion.
        
          
        

#### Defined Circuit and Mechanical Parameters

- $N$: Number of turns in the external search coil.
    
      
    
- $\Phi$: Instantaneous magnetic flux passing through each turn of the search coil.
    
      
    
- $R_c$: Resistance of the search coil.
    
      
    
- $L_c$: Self-inductance of the search coil.
    
      
    
- $R_f$: Internal resistance of the flux meter moving coil.
    
      
    
- $L_f$: Self-inductance of the flux meter moving coil.
    
      
    
- $i$: Instantaneous current flowing through the closed series circuit.
    
      
    
- $\theta$: Angular deflection of the meter coil at any given instant.
    
      
    
- $\omega = \frac{d\theta}{dt}$: Instantaneous angular velocity of the moving coil.
    
      
    
- $J$: Moment of inertia of the entire rotating system.
    
      
    
- $G$: Deflection torque constant (also equal to the back-EMF constant), where torque is $T_d = Gi$.
    
      
    

#### Step 1: Mechanical Equation of Motion

- Under general conditions, a suspended galvanometer coil experiences three main torques:
    
      
    - An accelerating torque given by $J \frac{d^2\theta}{dt^2}$.
        
          
        
    - An air-friction damping torque given by $D \frac{d\theta}{dt}$.
        
          
        
    - A spring-restoring control torque given by $C\theta$.
        
          
        
- These torques oppose the electromagnetic deflecting torque $T_d = Gi$, yielding the classic differential equation:
    
      
    
    $$J \frac{d^2\theta}{dt^2} + D \frac{d\theta}{dt} + C\theta = Gi$$
    
      
    
- In a true flux meter, two vital mechanical simplifications are designed into the hardware:
    
      
    - **No control springs are used ($C = 0$):** Flexible gold or silver ligaments are used instead of spiral hairsprings, meaning there is zero mechanical restoring torque.
        
          
        
    - **Negligible air friction ($D = 0$):** Damping from air friction is negligible compared to electromagnetic damping.
        
          
        
- Substituting $C = 0$ and $D = 0$ simplifies the mechanical equation to:
    
      
    
    $$J \frac{d^2\theta}{dt^2} = Gi$$
    
      
    
- Solving directly for the instantaneous current $i$:
    
      
    
    $$i = \frac{J}{G} \frac{d^2\theta}{dt^2} = \frac{J}{G} \frac{d\omega}{dt}$$
    
      
    

#### Step 2: Electrical Circuit Equations (KVL)

- When the search coil experiences a change in magnetic flux, an induced electromotive force $e_1$ appears across it by Faraday's Law:
    
      
    
    $$e_1 = -N \frac{d\Phi}{dt}$$
    
      
    
- As the flux meter's moving coil rotates through the permanent magnet's uniform field, it cuts magnetic lines, generating a back-EMF $e_2$:
    
      
    
    $$e_2 = -G \frac{d\theta}{dt}$$
    
      
    
- The total series resistance of the circuit is $(R_c + R_f)$ and the total series inductance is $(L_c + L_f)$.
    
      
    
- Writing Kirchhoff's Voltage Law around this single closed series loop gives:
    
      
    
    $$e_1 + e_2 = i(R_c + R_f) + (L_c + L_f) \frac{di}{dt}$$
    
      
    
- Substituting the exact expressions for $e_1$ and $e_2$ into the KVL loop:
    
      
    
    $$-N \frac{d\Phi}{dt} - G \frac{d\theta}{dt} = i(R_c + R_f) + (L_c + L_f) \frac{di}{dt}$$
    
      
    

#### Step 3: Coupling the Electrical and Mechanical Systems

- Now substitute the mechanical expression for current, $i = \frac{J}{G} \frac{d^2\theta}{dt^2}$, into the loop voltage equation:
    
      
    
    $$-N \frac{d\Phi}{dt} - G \frac{d\theta}{dt} = \left(\frac{J}{G} \frac{d^2\theta}{dt^2}\right)(R_c + R_f) + (L_c + L_f)\frac{d}{dt}\left(\frac{J}{G}\frac{d^2\theta}{dt^2}\right)$$
    
      
    
- Moving the back-EMF term $G \frac{d\theta}{dt}$ to the right-hand side gives:
    
      
    
    $$-N \frac{d\Phi}{dt} = G \frac{d\theta}{dt} + \frac{J(R_c + R_f)}{G}\frac{d^2\theta}{dt^2} + \frac{J(L_c + L_f)}{G}\frac{d^3\theta}{dt^3}$$
    
      
    
- Expressing the higher derivatives in terms of angular velocity $\omega = \frac{d\theta}{dt}$ and current $i$:
    
      
    - Note that $\frac{d^2\theta}{dt^2} = \frac{d\omega}{dt}$.
        
          
        
    - Note that $\frac{J}{G}\frac{d^3\theta}{dt^3} = \frac{di}{dt}$.
        
          
        
- The equation can therefore be cleanly rewritten as:
    
      
    
    $$-N \frac{d\Phi}{dt} = G \frac{d\theta}{dt} + \frac{J(R_c + R_f)}{G} \frac{d\omega}{dt} + (L_c + L_f) \frac{di}{dt}$$
    
      
    

#### Step 4: Definite Integration Over Time

- Multiply the entire differential expression by $dt$ to eliminate time differentials:
    
      
    
    $$-N \, d\Phi = G \, d\theta + \frac{J(R_c + R_f)}{G} \, d\omega + (L_c + L_f) \, di$$
    
      
    
- Integrate each individual term from the beginning of the flux change ($t = t_1$) to the completion of the movement ($t = t_2$):
    
      
    
    $$-N \int_{\Phi_1}^{\Phi_2} d\Phi = G \int_{\theta_1}^{\theta_2} d\theta + \frac{J(R_c + R_f)}{G} \int_{\omega_1}^{\omega_2} d\omega + (L_c + L_f) \int_{i_1}^{i_2} di$$
    
      
    
- Evaluating the definite integrals yields:
    
      
    
    $$N(\Phi_1 - \Phi_2) = G(\theta_2 - \theta_1) + \frac{J(R_c + R_f)}{G}(\omega_2 - \omega_1) + (L_c + L_f)(i_2 - i_1)$$
    
      
    

#### Step 5: Applying Boundary Conditions

- **Initial State ($t_1$):**
    
      
    - Before the flux change begins, the search coil and moving system are completely stationary: $\omega_1 = 0$.
        
          
        
    - No induced voltage exists, so no current flows: $i_1 = 0$.
        
          
        
- **Final State ($t_2$):**
    
      
    - After the flux change concludes, the moving coil settles and comes to rest due to electromagnetic damping: $\omega_2 = 0$.
        
          
        
    - All transient induced voltages vanish, returning the current to zero: $i_2 = 0$.
        
          
        
- Substituting these boundary conditions ($\omega_1 = \omega_2 = 0$ and $i_1 = i_2 = 0$) causes the last two terms to vanish completely:
    
      
    
    $$\frac{J(R_c + R_f)}{G}(0 - 0) = 0$$
    
      
    
    $$(L_c + L_f)(0 - 0) = 0$$
    
      
    
- This leaves only the primary flux and deflection terms:
    
      
    
    $$N(\Phi_1 - \Phi_2) = G(\theta_2 - \theta_1)$$
    
      
    

#### Final Relationship and Physical Meaning

- Let the total change in magnetic flux linking one turn be $\Delta\Phi = (\Phi_1 - \Phi_2)$.
    
      
    
- Let the total angular pointer deflection be $\Delta\theta = (\theta_2 - \theta_1)$.
    
      
    
- Rearranging the balanced expression gives:
    
      
    
    $$\Delta\Phi = \frac{G}{N} \Delta\theta$$
    
      
    
- Alternatively, expressing the angular deflection directly:
    
      
    
    $$\Delta\theta = \frac{N}{G} \Delta\Phi$$
    
      
    
- **Why the result is unique and powerful:**
    
      
    - The total deflection $\Delta\theta$ depends strictly on the net change in flux ($\Delta\Phi$) and is completely independent of the resistance of the search coil or the speed at which the coil is moved.
        
          
        
    - Because $N$ and $G$ are constant physical parameters, the relationship between deflection and flux change is linear, giving the flux meter a uniform scale.

#### Parameter Definitions

- $\Phi$: Magnetic flux established inside the magnetic specimen core and linking each turn of the search coil (measured in Webers, $\text{Wb}$).
    
      
    
- $N$: Number of turns wound on the secondary search coil (also called the B-coil).
    
      
    
- $R$: Total electrical resistance of the complete ballistic galvanometer closed circuit (measured in Ohms, $\Omega$).
    
      
    
- $t$: Time duration taken for the commutator/reversing switch to completely reverse the magnetizing current and magnetic flux (measured in seconds, $\text{s}$).
    
      
    
- $e$: Average electromotive force (EMF) induced across the terminals of the search coil during the flux reversal (measured in Volts, $\text{V}$).
    
      
    
- $i$: Average transient current flowing through the ballistic galvanometer circuit during the switching interval (measured in Amperes, $\text{A}$).
    
      
    
- $Q$: Total quantity of electric charge displaced through the galvanometer movement during the entire reversal transient (measured in Coulombs, $\text{C}$).
    
      
    
- $\theta_1$: First maximum peak deflection or angular throw of the ballistic galvanometer pointer/light spot.
    
      
    
- $K_q$: Galvanometer ballistic sensitivity constant (expressed in Coulombs per unit deflection, $\text{C/division}$ or $\text{C/rad}$).
    
      
    
- $A_s$: Effective cross-sectional area of the ring specimen covered by the search coil (measured in square meters, $\text{m}^2$).
    
      
    
- $B$: Magnetic flux density within the specimen material (measured in $\text{Wb/m}^2$ or Tesla, $\text{T}$).
    
      
    

#### Step 1: Net Change in Magnetic Flux ($\Delta\Phi$)

- The primary magnetizing coil initially carries a steady direct current $I$, which establishes a steady initial magnetic flux $+\Phi$ through the cross-section of the specimen core.
    
      
    
- When the reversing switch is operated, the direction of the magnetizing current flips instantaneously, reversing the direction of magnetic flux to $-\Phi$.
    
      
    
- The total net change in magnetic flux linking the search coil is calculated by finding the absolute difference between the initial and final flux states:
    
      
    
    $$\Delta\Phi = \Phi_{\text{initial}} - \Phi_{\text{final}} = \Phi - (-\Phi) = 2\Phi$$
    
      
    

#### Step 2: Average Induced EMF ($e$)

- According to Faraday's Law of Electromagnetic Induction, the magnitude of induced electromotive force in a coil is proportional to the time rate of change of magnetic flux linkages:
    
      
    
    $$e = N \frac{d\Phi}{dt}$$
    
      
    
- Substituting the finite change in total flux $\Delta\Phi = 2\Phi$ over the time interval $\Delta t = t$:
    
      
    
    $$e = N \left(\frac{\Delta\Phi}{\Delta t}\right) = N \left(\frac{2\Phi}{t}\right)$$
    
      
    
- Simplifying into standard form gives the average induced EMF:
    
      
    
    $$e = \frac{2N\Phi}{t}$$
    
      
    

#### Step 3: Average Induced Current ($i$)

- By applying Ohm's Law to the closed secondary circuit consisting of the search coil and the ballistic galvanometer having a total series resistance $R$:
    
      
    
    $$i = \frac{e}{R}$$
    
      
    
- Substituting the expression for the average induced EMF $e = \frac{2N\Phi}{t}$ into Ohm's Law:
    
      
    
    $$i = \frac{\left(\frac{2N\Phi}{t}\right)}{R}$$
    
      
    
- Simplifying the fraction gives the instantaneous average current passing through the galvanometer coil:
    
      
    
    $$i = \frac{2N\Phi}{Rt}$$
    
      
    

#### Step 4: Total Electric Charge ($Q$) Transmitted

- The total quantity of electricity or electrical charge ($Q$) swept through the galvanometer circuit is defined as the integral of electric current over the discharge time interval:
    
      
    
    $$Q = \int_{0}^{t} i \, dt = i \times t$$
    
      
    
- Substituting the expression for average current $i = \frac{2N\Phi}{Rt}$ into the charge relationship:
    
      
    
    $$Q = \left(\frac{2N\Phi}{Rt}\right) \times t$$
    
      
    
- Cancelling out the time duration parameter $t$ reveals that the total charge displaced is entirely independent of how fast or slow the switching occurs:
    
      
    
    $$Q = \frac{2N\Phi}{R}$$
    
      
    

#### Step 5: Charge Indicated by the Ballistic Galvanometer

- A ballistic galvanometer operates by integrating rapid current pulses into an instantaneous mechanical impulse before the moving system appreciably deflects.
    
      
    
- The resulting initial angular throw ($\theta_1$) is directly proportional to the total electrical charge passing through its moving coil:
    
      
    
    $$Q = K_q \theta_1$$
    
      
    
- Equating the charge calculated from circuit induction to the charge measured mechanically by the ballistic galvanometer:
    
      
    
    $$\frac{2N\Phi}{R} = K_q \theta_1$$
    
      
    
- Multiplying both sides by the circuit resistance $R$ gives:
    
      
    
    $$2N\Phi = R K_q \theta_1$$
    
      
    
- Isolating the total core magnetic flux $\Phi$:
    
      
    
    $$\Phi = \frac{R K_q \theta_1}{2N}$$
    
      
    

#### Step 6: Calculation of Magnetic Flux Density ($B$)

- Magnetic flux density $B$ represents the concentration of magnetic flux per unit perpendicular cross-sectional area of the core material:
    
      
    
    $$B = \frac{\text{Flux}}{\text{Area}} = \frac{\Phi}{A_s}$$
    
      
    
- Substituting the derived value of $\Phi = \frac{R K_q \theta_1}{2N}$ into the density definition:
    
      
    
    $$B = \frac{\left(\frac{R K_q \theta_1}{2N}\right)}{A_s}$$
    
      
    
- Simplifying into the final governing equation (Equation 18.1):
    
      
    
    $$B = \frac{R K_q \theta_1}{2 N A_s}$$
    
      
    
- **Physical Significance:** Since $R$, $K_q$, $N$, and $A_s$ are known, fixed physical constants of the test configuration, the magnetic flux density $B$ is found directly by observing the first throw $\theta_1$ on the galvanometer scale.
#### 1. Extension of Flux Meter Range (Shunt Method)
![[Pasted image 20261012173046.png]]
- **Purpose:** When measuring very large magnetic flux, the pointer can deflect beyond full-scale even with a 1-turn search coil.
    
- **Solution:** Connect a low-resistance **shunt ($R_s$)** in parallel across the flux meter terminals to bypass a fraction of the current.
    
- **Circuit Connections:**
    
    - Search coil ($R_c, L_c$) supplies total current $i_c$.
        
    - At junction, current splits: $i_f$ enters the flux meter ($R_f, L_f$) and $i_s$ passes through the shunt resistor ($R_s$):
        
        $$i_c = i_f + i_s$$
        
- **Multiplying Factor ($m$):**
    
    - Voltage across the parallel branches is equal:
        
        $$i_s R_s \approx i_f R_f \implies i_s = i_f \left(\frac{R_f}{R_s}\right)$$
        
    - Substituting $i_s$:
        
        $$i_c = i_f \left(1 + \frac{R_f}{R_s}\right) = m \cdot i_f$$
        
    - Here, $m = \left(1 + \frac{R_f}{R_s}\right)$ is the **multiplying factor**; the true flux is obtained by multiplying the measured reading by $m$.
#### 1. Basic Loss Equations

- **Hysteresis Loss Per Unit Volume ($p_h$):**
    
      
    - Derived from the area of the B-H loop times frequency:
        
          
        
        $$p_h = \eta f B_m^k \quad [\text{W/m}^3]$$
        
          
        
    - $\eta$: Hysteresis coefficient
        
          
        
    - $f$: Frequency in Hz
        
          
        
    - $B_m$: Maximum flux density in $\text{Wb/m}^2$
        
          
        
          
        
    - $k$: Steinmetz exponent (ranges from $1.6$ to $2.0$)
        
          
        
- **Eddy Current Loss Per Unit Volume ($p_e$):**
    
      
    - For laminated magnetic sheets:
        
          
        
        $$p_e = \frac{4 K_f^2 f^2 B_m^2 t^2}{3\rho} \quad [\text{W/m}^3]$$
        
          
        
    - $K_f$: Form factor of the voltage waveform
        
          
        
    - $t$: Lamination thickness in meters
        
          
        
    - $\rho$: Electrical resistivity of core material in $\Omega\cdot\text{m}$
        
          
        
          
        

#### 2. Total Iron Loss ($P_i$)

- Total loss per unit volume is the sum of both components:
    
      
    
    $$p_i = p_h + p_e = \eta f B_m^k + \frac{4 K_f^2 f^2 B_m^2 t^2}{3\rho}$$
    
      
    
- Multiplying by the core volume $V$ gives the total iron loss $P_i$:
    
      
    
    $$P_i = V \cdot p_i = V \left(\eta f B_m^k + \frac{4 K_f^2 f^2 B_m^2 t^2}{3\rho}\right)$$
    
      
    
- For a given test specimen, volume $V$, thickness $t$, and resistivity $\rho$ are constant. Combining these constants into $K_h$ and $K_e$:
    
      
    
    $$P_i = K_h f B_m^k + K_e K_f^2 f^2 B_m^2$$
    
      
    
    _(where $K_h = V\eta$ and $K_e = \frac{4 V t^2}{3\rho}$)_.
    
      
    

#### 3. Method 1: Separation by Frequency Variation

- **Condition:** Maintain form factor $K_f$ and peak flux density $B_m$ constant while varying frequency $f$.
    
      
    
- **Step 1: Simplify into Constants**
    
      
    - Group the constant factors:
        
          
        
        $$K_1 = K_h B_m^k \quad \text{and} \quad K_2 = K_e K_f^2 B_m^2$$
        
          
        
    - Rewrite total iron loss:
        
          
        
        $$P_i = K_1 f + K_2 f^2$$
        
          
        
- **Step 2: Linearize the Equation**
    
      
    - Divide the entire equation by frequency $f$:
        
          
        
        $$\frac{P_i}{f} = K_1 + K_2 f$$
        
          
        
- **Step 3: Graphical Separation ($y = mx + c$)**
    
      
    - Plot $\frac{P_i}{f}$ along the y-axis against $f$ along the x-axis, which produces a straight line:
        
          
        - **Vertical Intercept ($c$):** equals $K_1$, giving the hysteresis component per cycle.
            
              
            
        - **Slope ($m$):** equals $K_2$, giving the eddy current component coefficient.
            
              
            
    - At any operating frequency $f_1$:
        
          
        
        $$\text{Hysteresis Loss} = K_1 f_1$$
        
          
        
        $$\text{Eddy Current Loss} = K_2 f_1^2$$
        
          
        

#### 4. Method 2: Separation by Form Factor Variation

- **Condition:** Maintain peak flux density $B_m$ and frequency $f$ constant while varying waveform form factor $K_f$.
    
      
    
- **Step 1: Simplify into Constants**
    
      
    - Group the constant terms:
        
          
        
        $$K_3 = K_h f B_m^k \quad \text{and} \quad K_4 = K_e f^2 B_m^2$$
        
          
        
    - Total iron loss equation becomes:
        
          
        
        $$P_i = K_3 + K_4 K_f^2$$
        
          
        
- **Step 2: Graphical Separation ($y = mx + c$)**
    
      
    - Plot $P_i$ along the y-axis against $K_f^2$ along the x-axis, yielding a straight line:
        
          
        - **Vertical Intercept ($c$):** equals $K_3$, giving the constant hysteresis loss.
            
              
            
        - **Slope ($m$):** equals $K_4$, giving the eddy current loss rate.
            
              
            
    - For a given form factor $K_{f1}$:
        
          
        
        $$\text{Hysteresis Loss} = K_3$$
        
          
        
        $$\text{Eddy Current Loss} = K_4 K_{f1}^2$$

#### 4. crt cro Step-by-Step Derivation of Electrostatic Deflection

- **Step 1: Axial Velocity ($v_{ox}$) from Anode Acceleration**
    
    - Electrons emitted from the cathode are accelerated across the potential difference $V_a$.
        
    - The potential energy lost by an electron equals the kinetic energy gained:
        
        $$e V_a = \frac{1}{2} m v_{ox}^2$$
        
    - Solving for the axial velocity $v_{ox}$ entering the deflecting plate assembly:
        
        $$v_{ox}^2 = \frac{2 e V_a}{m} \implies v_{ox} = \sqrt{\frac{2 e V_a}{m}}$$
        
- **Step 2: Electrostatic Force and Upward Acceleration ($a_y$)**
    
    - The uniform electric field established between two parallel plates separated by distance $d$ under voltage $V_d$ is:
        
        $$\mathcal{E} = \frac{V_d}{d}$$
        
    - The upward electrostatic force experienced by the electron within this field is:
        
        $$F_y = e \mathcal{E} = e \frac{V_d}{d}$$
        
    - Applying Newton's second law of motion ($F_y = m a_y$), the vertical acceleration along the Y-axis is:
        
        $$a_y = \frac{F_y}{m} = \frac{e V_d}{m d}$$
        
- **Step 3: Transit Time ($t$) Across the Deflection Plates**
    
    - No electric field acts along the horizontal X-axis, meaning the horizontal velocity $v_{ox}$ remains strictly constant throughout the plate region.
        
    - The time $t$ required for an electron to traverse a horizontal distance $x$ is:
        
        $$t = \frac{x}{v_{ox}}$$
        
    - For the complete plate length $l$, the total transit time inside the field is:
        
        $$t = \frac{l}{v_{ox}}$$
        
- **Step 4: Electron Trajectory Inside the Plates (Parabolic Path)**
    
    - Since the electron enters horizontally with zero initial vertical velocity ($v_{oy} = 0$), its vertical position $y$ at horizontal distance $x$ follows kinematic motion:
        
        $$y = \frac{1}{2} a_y t^2 = \frac{1}{2} a_y \left(\frac{x}{v_{ox}}\right)^2$$
        
    - Substituting $a_y = \frac{e V_d}{m d}$ into the trajectory expression:
        
        $$y = \frac{1}{2} \left(\frac{e V_d}{m d}\right) \frac{x^2}{v_{ox}^2}$$
        
    - Because all terms except $x^2$ are constants, $y \propto x^2$, which proves that the electron travels along a **parabolic path** inside the deflecting field.
        
    - At the exit edge of the plates where $x = l$, the internal vertical displacement $y_1$ is:
        
        $$y_1 = \frac{1}{2} \left(\frac{e V_d}{m d}\right) \left(\frac{l}{v_{ox}}\right)^2 = \frac{e V_d l^2}{2 m d v_{ox}^2}$$
        
- **Step 5: Exit Velocity ($v_y$) and Deflection Angle ($\theta$)**
    
    - The vertical velocity $v_y$ gained by the electron at the instant it leaves the plates is:
        
        $$v_y = a_y t = \left(\frac{e V_d}{m d}\right) \left(\frac{l}{v_{ox}}\right) = \frac{e V_d l}{m d v_{ox}}$$
        
    - The slope or tangent of the deflection angle $\theta$ upon exit is given by the velocity ratio:
        
        $$\tan\theta = \frac{v_y}{v_{ox}} = \frac{\left(\frac{e V_d l}{m d v_{ox}}\right)}{v_{ox}} = \frac{e V_d l}{m d v_{ox}^2}$$
        
    - Substitute $v_{ox}^2 = \frac{2 e V_a}{m}$ from Step 1 into this equation:
        
        $$\tan\theta = \frac{e V_d l}{m d \left(\frac{2 e V_a}{m}\right)}$$
        
    - Cancelling the specific charge ratio $\frac{e}{m}$ simplifies the deflection angle to:
        
        $$\tan\theta = \frac{l V_d}{2 d V_a}$$
        
- **Step 6: Total Deflection on the Fluorescent Screen ($D$)**
    
    - Beyond the plates, the electric field is zero, so the electron travels in a straight line along the exit tangent until it strikes the screen.
        
    - Projecting this straight-line tangent backward shows that it intersects the central horizontal axis exactly at the midpoint of the plates ($x = l/2$).
        
    - Thus, the effective distance from this apparent origin of deflection to the screen is $L$.
        
    - From the geometry of the resulting right-angled triangle:
        
        $$\tan\theta = \frac{D}{L} \implies D = L \tan\theta$$
        
    - Substituting the derived value of $\tan\theta = \frac{l V_d}{2 d V_a}$ into the screen deflection formula:
        
        $$D = L \left(\frac{l V_d}{2 d V_a}\right)$$
        
    - Rearranging into standard form gives the final expression for spot deflection:
        
        $$D = \frac{l L V_d}{2 d V_a}$$
        

#### 5. Deflection Sensitivity and Deflection Factor

- **Deflection Sensitivity ($S$):**
    
    - Defined as the screen deflection produced per unit deflecting voltage applied across the plates:
        
        $$S = \frac{D}{V_d} = \frac{l L}{2 d V_a} \quad [\text{m/V} \text{ or } \text{mm/V}]$$
        
    - A higher sensitivity means a smaller voltage produces a large, easily readable spot movement.
        
    - Sensitivity can be increased by:
        
        - Increasing plate length $l$.
            
        - Increasing distance to the screen $L$.
            
        - Decreasing plate separation $d$.
            
        - Decreasing accelerating anode voltage $V_a$ (though reducing $V_a$ lowers beam intensity/brightness).
            
- **Deflection Factor ($G$):**
    
    - Defined as the reciprocal of deflection sensitivity, representing the deflecting voltage needed to cause unit displacement on the screen:
        
        $$G = \frac{1}{S} = \frac{V_d}{D} = \frac{2 d V_a}{l L} \quad [\text{V/m} \text{ or } \text{V/mm}]$$
        

#### 6. Key Conclusions

- **Linear Response:** For fixed CRT physical dimensions ($l, L, d$) and a stable accelerating voltage ($V_a$), all parameters except $V_d$ are constant:
    
    $$D \propto V_d$$
    
- This direct linear proportionality allows the CRT to function as an accurate, linear voltage-indicating device.
    
- As the applied deflecting voltage varies continuously in time, the luminous spot traces an exact, faithful visual reproduction of the input waveform across the calibrated screen.

#### 1. Overview of the CRO Block Diagram

- A **Cathode Ray Oscilloscope (CRO)** takes an electrical input signal and displays it visually as a graph of voltage versus time on a screen.
    
      
    
- The system is divided into two primary processing paths:
    
      
    - **Vertical Channel:** Handles the input signal amplitude to move the beam up and down.
        
          
        
    - **Horizontal Channel:** Synchronizes and sweeps the electron beam from left to right at a steady pace.
        
          
        
- Both channels feed into the central display unit, the **Cathode Ray Tube (CRT)**.
    
      
    

#### 2. The Seven Main Functional Blocks

- **(i) Vertical Amplifier:**
    
      
    - **Purpose:** Boosts weak electrical input signals.
        
          
        
    - **How it works:** Input test signals are often in the millivolt range, which is too weak to visibly steer high-speed electrons. The vertical amplifier amplifies the signal voltage to a usable level strong enough to deflect the electron beam up and down on the screen.
        
          
        
- **(ii) Delay Line:**
    
      
    - **Purpose:** Delays the vertical signal by a few nanoseconds.
        
          
        
    - **Why it is necessary:** The input signal splits into two paths: one heads to the vertical plates, and the other triggers the horizontal sweep. Processing the horizontal sweep through the trigger circuit, time-base generator, and horizontal amplifier takes a fraction of time.
        
          
        
    - The delay line holds the vertical signal back just enough so that both horizontal sweeping and vertical signal display arrive at the deflection plates at the exact same instant, preventing the leading edge of the waveform from being cut off.
        
          
        
- **(iii) Trigger Circuit:**
    
      
    - **Purpose:** Provides synchronization between the vertical and horizontal movements.
        
          
        
    - **How it works:** It monitors the incoming signal and sends a trigger pulse at a specific voltage level. This ensures the horizontal sweep begins at the exact same point of each cycle, keeping the displayed waveform frozen and stationary instead of flickering or drifting.
        
          
        
- **(iv) Time-Base Generator:**
    
      
    - **Purpose:** Generates a linear **sawtooth waveform** voltage.
        
          
        
    - **How it works:** The voltage rises steadily and linearly with time to sweep the electron beam across the screen from left to right at a constant speed, then drops rapidly to snap the spot back to the left side (retrace).
        
          
        
- **(v) Horizontal Amplifier:**
    
      
    - **Purpose:** Amplifies the sawtooth voltage from the time-base generator.
        
          
        
    - **How it works:** It increases the voltage of the sawtooth signal to provide enough electrostatic force across the horizontal ($X$) deflection plates for the spot to cover the full width of the screen.
        
          
        
- **(vi) Power Supply Block:**
    
      
    - **Purpose:** Delivers proper electrical power to all internal stages.
        
          
        
    - **High-Voltage (HV) Supply:** Delivers high positive DC voltages (thousands of volts) needed by the CRT anodes to accelerate the electron beam.
        
          
        
    - **Low-Voltage (LV) Supply:** Provides lower DC operating voltages needed by the electronic circuits (vertical amplifier, trigger circuit, time-base generator, and heater filament).
        
          
        
- **(vii) Cathode Ray Tube (CRT):**
    
      
    - **The Heart of the Instrument:** Houses all mechanical and electrostatic elements in a high-vacuum tube.
        
          
        
    - **Key Functions:**
        
          
        - Generates a focused beam of electrons via thermionic emission.
            
              
            
        - Accelerates electrons to high velocities using accelerating anodes.
            
              
            
        - Deflects the beam horizontally and vertically to form the visible waveform.
            
              
            
        - Strikes the phosphor screen to convert the kinetic energy of electrons into visible light.
#### 1. Setup

- **Inputs:** Connect the unknown frequency ($f_y$) to the **Y-input** (vertical) and the known standard generator ($f_x$) to the **X-input** (horizontal).
    
- **Mode:** Turn off the internal sweep and switch the CRO to **X-Y mode**.
    

#### 2. Procedure

- **Adjust:** Slowly tune the known frequency generator until the moving loop locks into a **stationary pattern**.
    
- **Count Tangencies:** Imagine two tangent lines touching the edges of the pattern:
    
    - $n_h$ = Number of loops/touchpoints along the **horizontal** top line.
        
    - $n_v$ = Number of loops/touchpoints along the **vertical** side line.
        

#### 3. Formula

$$\frac{f_y}{f_x} = \frac{n_h}{n_v}$$

$$\implies f_y = f_x \times \left(\frac{n_h}{n_v}\right)$$

- $f_y$: Unknown frequency (Y-plates)
    
- $f_x$: Known frequency (X-plates)
    
- $n_h$: Horizontal points of contact
    
- $n_v$: Vertical points of contact
    

#### 4. Quick Example

- **Given:** A stable figure-8 pattern touches the top line twice ($n_h = 2$) and the side line once ($n_v = 1$), with $f_x = 1000\text{ Hz}$.
    
- **Calculation:**
    
    $$\frac{f_y}{1000} = \frac{2}{1} \implies f_y = 2000\text{ Hz}$$


#### Overview and Working Principle

The **Q-meter** measures the quality factor ($Q$) of RF circuits, coils, and capacitors directly based on the principle of **series resonance**.

- **Definition of $Q$ factor:**
    
    - For inductive components: $Q = \frac{X_L}{R} = \frac{\omega L}{R}$
        
    - For capacitive components: $Q = \frac{X_C}{R} = \frac{1}{\omega C R}$
        
- **Series Resonance Condition:**
    
    - At resonance, inductive reactance equals capacitive reactance:
        
        $$X_L = X_C$$
        
    - Total circuit impedance reduces to resistance $R$, making the current:
        
        $$I = \frac{E}{R}$$
        
    - Voltage across the resonating capacitor ($E_C$):
        
        $$E_C = I X_C = I X_L$$
        
    - Relating $E_C$ to applied oscillator voltage $E$:
        
        $$Q = \frac{X_L}{R} = \frac{X_C}{R} = \frac{I X_C}{I R} = \frac{E_C}{E}$$
        
        $$E_C = Q \cdot E$$
        
- **Measurement rule:** By keeping the input oscillator voltage $E$ constant, the voltage across the capacitor $E_C$ is directly proportional to $Q$.
#### Series Connection Method (Low Impedance)

Used for measuring low-impedance unknown loads ($Z_S = R_S + j X_S$).

- **Step 1: Reference Measurement (Unknown Shorted)**
    
    - A stable work coil is placed in the circuit, and the unknown impedance $Z$ is short-circuited.
        
    - The circuit is resonated at frequency $\omega$ using tuning capacitor $C_1$, noting the quality factor $Q_1$:
        
        $$X_L = X_{C1} = \frac{1}{\omega C_1}$$
        
        $$R_1 = \frac{X_{C1}}{Q_1} = \frac{1}{\omega C_1 Q_1}$$
        
- **Step 2: Second Measurement (Unknown Inserted)**
    
    - The shorting strap is removed, placing $Z_S$ in series.
        
    - The circuit is retuned to resonance by adjusting the capacitor to $C_2$, recording the new quality factor $Q_2$:
        
        $$X_S + X_L = X_{C2}$$
        
        $$R_2 = \frac{X_{C2}}{Q_2} = \frac{1}{\omega C_2 Q_2}$$
        
- **Step 3: Derivation of Unknown Reactance ($X_S$)**
    
    - Substitute $X_L = \frac{1}{\omega C_1}$ and $X_{C2} = \frac{1}{\omega C_2}$:
        
        $$X_S = X_{C2} - X_L = \frac{1}{\omega C_2} - \frac{1}{\omega C_1}$$
        
        $$X_S = \frac{C_1 - C_2}{\omega C_1 C_2}$$
        
    - _Nature of load:_ If $C_1 > C_2$, $X_S$ is **inductive** ($+j X_S$). If $C_1 < C_2$, $X_S$ is **capacitive** ($-j X_S$).
        
- **Step 4: Derivation of Unknown Resistance ($R_S$)**
    
    - Since the total resistance in step 2 is $R_2 = R_1 + R_S$:
        
        $$R_S = R_2 - R_1 = \frac{1}{\omega C_2 Q_2} - \frac{1}{\omega C_1 Q_1}$$
        
        $$R_S = \frac{C_1 Q_1 - C_2 Q_2}{\omega C_1 C_2 Q_1 Q_2}$$
        
- **Step 5: Derivation of Quality Factor ($Q_S$)**
    
    - Dividing reactance by resistance:
        
        $$Q_S = \frac{X_S}{R_S} = \frac{\frac{C_1 - C_2}{\omega C_1 C_2}}{\frac{C_1 Q_1 - C_2 Q_2}{\omega C_1 C_2 Q_1 Q_2}} = \frac{(C_1 - C_2) Q_1 Q_2}{C_1 Q_1 - C_2 Q_2}$$
        
- **Special Cases:**
    
    - **Pure Resistor:** If $C_1 = C_2$, reactance is zero:
        
        $$R_S = \frac{Q_1 - Q_2}{\omega C_1 Q_1 Q_2} = \frac{\Delta Q}{\omega C_1 Q_1 Q_2}$$
        
    - **Small Inductor ($X_S = \omega L_S$):**
        
        $$L_S = \frac{X_S}{\omega} = \frac{C_1 - C_2}{\omega^2 C_1 C_2}$$
        
    - **Large Capacitor ($X_S = \frac{1}{\omega C_S}$):**
        
        $$C_S = \frac{C_1 C_2}{C_2 - C_1}$$

#### Measurement of Distributed Capacitance ($C_d$) source of error

The distributed (self) capacitance $C_d$ of a coil causes measurement errors and must be determined via two-frequency resonance.

- **Step 1: First Resonance**
    
    - The coil under test is tuned to resonance at frequency $f_1$ using capacitor value $C_1$:
        
        $$f_1 = \frac{1}{2\pi \sqrt{L(C_1 + C_d)}}$$
        
- **Step 2: Second Resonance**
    
    - The oscillator frequency is doubled ($f_2 = 2f_1$).
        
    - The circuit is returned to resonance by adjusting the capacitor to a smaller value $C_2$:
        
        $$f_2 = \frac{1}{2\pi \sqrt{L(C_2 + C_d)}}$$
        
- **Step 3: Mathematical Derivation of $C_d$**
    
    - Take the ratio $\frac{f_2}{f_1}$:
        
        $$\frac{f_2}{f_1} = \frac{\frac{1}{2\pi \sqrt{L(C_2 + C_d)}}}{\frac{1}{2\pi \sqrt{L(C_1 + C_d)}}} = \sqrt{\frac{C_1 + C_d}{C_2 + C_d}}$$
        
    - Since $f_2 = 2f_1$, substitute $\frac{f_2}{f_1} = 2$:
        
        $$2 = \sqrt{\frac{C_1 + C_d}{C_2 + C_d}}$$
        
    - Square both sides:
        
        $$4 = \frac{C_1 + C_d}{C_2 + C_d}$$
        
    - Cross-multiply and expand:
        
        $$4(C_2 + C_d) = C_1 + C_d$$
        
        $$4 C_2 + 4 C_d = C_1 + C_d$$
        
    - Group $C_d$ terms:
        
        $$4 C_d - C_d = C_1 - 4 C_2$$
        
        $$3 C_d = C_1 - 4 C_2$$
        
        $$C_d = \frac{C_1 - 4 C_2}{3}$$

#### Transformation Ratio Derivation ($R$)

- **Phasor Representation:**
    
    - From the phasor diagram of the Current Transformer (CT), the primary current vector $\vec{I}_p$ is the vector sum of the reversed secondary current referred to primary ($n\vec{I}_s$) and the exciting current ($\vec{I}_0$):
        
        $$I_p = \sqrt{(n I_s)^2 + I_0^2 + 2(n I_s) I_0 \cos(90^\circ - \alpha - \delta)}$$
        
    - Since $\cos(90^\circ - (\alpha + \delta)) = \sin(\alpha + \delta)$:
        
        $$I_p = \sqrt{(n I_s)^2 + I_0^2 + 2 n I_s I_0 \sin(\alpha + \delta)}$$
        
- **Actual Transformation Ratio ($R$):**
    
    - The actual transformation ratio is defined as $R = \frac{I_p}{I_s}$:
        
        $$R = \frac{\sqrt{(n I_s)^2 + I_0^2 + 2 n I_s I_0 \sin(\alpha + \delta)}}{I_s}$$
        
- **Mathematical Approximation:**
    
    - The no-load excitation current $I_0$ is very small compared to $n I_s$ ($I_0 \ll n I_s$).
        
    - Replacing $I_0^2$ with $[I_0 \sin(\alpha + \delta)]^2$ introduces negligible error:
        
        $$R \approx \frac{\sqrt{(n I_s)^2 + [I_0 \sin(\alpha + \delta)]^2 + 2 n I_s I_0 \sin(\alpha + \delta)}}{I_s}$$
        
    - Factoring the perfect square:
        
        $$R \approx \frac{\sqrt{[n I_s + I_0 \sin(\alpha + \delta)]^2}}{I_s} = \frac{n I_s + I_0 \sin(\alpha + \delta)}{I_s}$$
        
        $$R \approx n + \frac{I_0}{I_s}\sin(\alpha + \delta)$$
        
- **Component Expansion:**
    
    - Expanding $\sin(\alpha + \delta) = \sin\alpha \cos\delta + \cos\alpha \sin\delta$:
        
        $$I_0 \sin(\alpha + \delta) = (I_0 \sin\alpha)\cos\delta + (I_0 \cos\alpha)\sin\delta$$
        
    - Using core-loss component $I_w = I_0 \sin\alpha$ (or $I_c$) and magnetizing component $I_m = I_0 \cos\alpha$:
        
        $$R \approx n + \frac{I_w \cos\delta + I_m \sin\delta}{I_s}$$
        

#### Phase Angle Error Derivation ($\theta$)

- **Trigonometric Setup:**
    
    - From the right-angled triangle $O-b-c$ in the phasor diagram:
        
        $$\tan\theta = \frac{bc}{Ob} = \frac{I_0 \sin(90^\circ - \alpha - \delta)}{Oa + ab}$$
        
        $$\tan\theta = \frac{I_0 \cos(\alpha + \delta)}{n I_s + I_0 \sin(\alpha + \delta)}$$
        
- **Small Angle & Value Approximations:**
    
    - Because the phase deviation $\theta$ is very small, $\tan\theta \approx \theta$ (in radians).
        
    - Neglecting the small term in the denominator ($I_0 \sin(\alpha + \delta) \ll n I_s$):
        
        $$\theta \approx \frac{I_0 \cos(\alpha + \delta)}{n I_s}$$
        
- **Expansion into Current Components:**
    
    - Expanding the trigonometric identity $\cos(\alpha + \delta) = \cos\alpha \cos\delta - \sin\alpha \sin\delta$:
        
        $$\theta = \frac{I_0 \cos\alpha \cos\delta - I_0 \sin\alpha \sin\delta}{n I_s}$$
        
    - Substituting $I_m = I_0 \cos\alpha$ and $I_w = I_0 \sin\alpha$:
        
        $$\theta = \frac{I_m \cos\delta - I_w \sin\delta}{n I_s} \text{ radians}$$
        
    - Converting to degrees:
        
        $$\theta = \frac{180}{\pi} \left[ \frac{I_m \cos\delta - I_w \sin\delta}{n I_s} \right]^\circ$$
        

#### CT Burden and Measurement Errors

- **Burden Definitions:**
    
    - **Burden:** The total load across secondary terminals expressed in volt-amperes ($\text{VA}$) at rated secondary current and voltage.
        
    - **Rated Burden:** The maximum permissible $\text{VA}$ loading without exceeding accuracy limits for a specific class.
        
    - **Total Secondary Burden:**
        
        $$\text{Total Burden} = I_s^2 \cdot Z_{\text{secondary total}} = \frac{E_s^2}{Z_{\text{secondary total}}}$$
        
    - **External Secondary Load Burden:**
        
        $$\text{Load Burden} = \frac{V_s^2}{Z_{\text{load}}}$$
        
- **Sources and Formulas of Errors:**
    
    - **Ratio Error:** Arises because actual ratio $R$ deviates from nominal ratio $K_n$ (or turns ratio $n$) due to magnetizing current:
        
        $$\text{Percentage Ratio Error} = \frac{\text{Nominal Ratio} - \text{Actual Ratio}}{\text{Actual Ratio}} \times 100 = \frac{K_n - R}{R} \times 100$$
        
    - **Phase Angle Error ($\theta$):** Occurs because the secondary current is not displaced by exactly $180^\circ$ relative to the primary current.
        
    - **Resistive Burden Simplification:** When burden is predominantly resistive ($\delta \approx 0^\circ \implies \sin\delta \approx 0, \cos\delta \approx 1$):
        
        $$R \approx n + \frac{I_w}{I_s}, \quad \theta \approx \frac{180}{\pi}\left[\frac{I_m}{n I_s}\right]^\circ$$