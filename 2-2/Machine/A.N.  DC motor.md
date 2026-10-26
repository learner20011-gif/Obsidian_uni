![[Pasted image 20261026110057.png]]






#### Core Conceptual Differences

|**Parameter**|**Electric Motor**|**Electric Generator**|
|---|---|---|
|**Energy Conversion**|Electrical $\to$ Mechanical|Mechanical $\to$ Electrical|
|**Operating Principle**|Biot-Savart / Lorentz force on current-carrying conductor in a $\vec{B}$-field|Faraday’s Law of Induction & Lenz’s Law|
|**Direction Rule**|**Fleming's Left-Hand Rule**|**Fleming's Right-Hand Rule** (_Generato**R** = **R**ight_)|
|**Drive Source**|Connected power supply / voltage source|External prime mover (turbine, engine, crank)|
|**EMF Type**|**Back-EMF ($E_b$)** (opposes supply voltage $V$)|**Generated EMF ($E_g$)** (drives load current)|
|**Voltage Relation**|**$V > E_b$**|**$E_g > V$**|
|**Torque Role**|**Driving Torque** (rotates the rotor against load)|**Opposing/Counter Torque** (resists the prime mover)|

#### Voltage & Current Equations (DC Machine)

#### Motor

- **Voltage Balance:**
    
      
    
    $$V = E_b + I_a R_a$$
    
- **Armature Current:**
    
      
    
    $$I_a = \frac{V - E_b}{R_a}$$
    
- _At start ($N = 0 \implies E_b = 0$):_ $I_{\text{start}} = \frac{V}{R_a}$ _(very high; requires starter)_
* shunt Armature current: $I_a = I_L - I_f$.
      
    

#### Generator

- **Voltage Balance:**
    
      
    
    $$E_g = V + I_a R_a$$
    
- **Armature Current:**
    
      
    
    $$I_a = \frac{E_g - V}{R_a}$$
    
- _Terminal Voltage under load:_ $V = E_g - I_a R_a$
* shunt Armature current: $I_a = I_L + I_f$.
      
    

#### Governing Machine Equations (Identical Form, Opposite Roles)

#### Induced EMF Equation (Both)

$$E = \frac{P \Phi Z N}{60 A}$$

- $P$ = number of poles
    
      
    
- $\Phi$ = flux per pole ($\text{Wb}$)
    
      
    
- $Z$ = total armature conductors
    
      
    
- $N$ = rotational speed ($\text{rpm}$)
    
      
    
- $A$ = parallel paths ($A = 2$ for wave, $A = P$ for lap)
    
      
    
- **Motor ($E_b$):** Governs speed $\to N \propto \frac{E_b}{\Phi}$
    
      
    
- **Generator ($E_g$):** Governs open-circuit voltage $\to E_g \propto \Phi N$
    
      
    

#### Electromagnetic Torque Equation (Both)

$$T_e = \frac{P Z \Phi I_a}{2 \pi A} \propto \Phi I_a$$

- **Motor:** $T_e$ drives rotation in the direction of motion.
    
      
    
- **Generator:** $T_e$ is counter-torque (electromagnetic drag) opposing the prime mover.
    
      
    

#### Power Flow & Efficiency

#### Motor Power Flow

$$\text{Electrical Input } (V I_a) = \text{Mechanical Developed } (E_b I_a) + \text{Copper Loss } (I_a^2 R_a)$$

- **Efficiency:**
    
      
    
    $$\eta_m = \frac{P_{\text{mech, out}}}{P_{\text{elec, in}}} = \frac{T_{\text{shaft}} \cdot \omega}{V I_L}$$
    

#### Generator Power Flow

$$\text{Mechanical Input } (T_{\text{shaft}} \cdot \omega) \to \text{Electrical Developed } (E_g I_a) = \text{Electrical Output } (V I_a) + \text{Copper Loss } (I_a^2 R_a)$$

- **Efficiency:**
    
      
    
    $$\eta_g = \frac{P_{\text{elec, out}}}{P_{\text{mech, in}}} = \frac{V I_L}{T_{\text{shaft}} \cdot \omega}$$
    

#### Quick Hand-Rule Memory Aid

#### Fleming's Left-Hand Rule (Motor)

- **Thumb:** **T**hrust / Force / Motion
    
      
    
- **First Finger:** **F**ield ($\vec{B}$)
    
      
    
- **Second Finger:** **C**urrent ($\vec{I}$)
    
      
    

#### Fleming's Right-Hand Rule (Generator)

- **Thumb:** Motion of conductor (from prime mover)
    
      
    
- **First Finger:** **F**ield ($\vec{B}$)
    
      
    
- **Second Finger:** Induced **C**urrent ($\vec{I}$)