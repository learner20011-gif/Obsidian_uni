![[Pasted image 20260923125718.png|531]]![[Pasted image 20261010183959.png]]![[Pasted image 20261010185510.png|498]]![[Pasted image 20260923150632.png]]![[Pasted image 20260923151916.png]]![[Pasted image 20260923153649.png|442]]![[Pasted image 20260923165622.png]]
![[Pasted image 20261011172329.jpg]]
![[Pasted image 20261011182434.jpg]]
![[Pasted image 20261011194756.png]]
![[Pasted image 20261011200312.png]]

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