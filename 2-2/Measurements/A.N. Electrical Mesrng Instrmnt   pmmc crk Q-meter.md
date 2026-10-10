![[Pasted image 20260923125718.png|531]]![[Pasted image 20261010183959.png]]![[Pasted image 20261010185510.png|498]]![[Pasted image 20260923150632.png]]![[Pasted image 20260923151916.png]]![[Pasted image 20260923153649.png|442]]![[Pasted image 20260923165622.png]]





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