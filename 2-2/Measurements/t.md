
![[Pasted image 20260905234213.png]]
![[Pasted image 20260905234152.png]]
![[Pasted image 20260905233856.png]]
![[Pasted image 20260905233837.png]]![[Pasted image 20260905233951.png]]
## Microphones

- **Definition:** Pressure transducer converting acoustic energy (sound waves) $\to$ electrical energy.
    
      
    
- **Core Sensor:** Diaphragm.
    
      
    
- **Sensitivity Formula:**
    
      
    
    $$\text{Sensitivity (dB)} = 20\log_{10}(\text{voltage output}) + 74\text{ dB}$$
    
      
    - Reference condition: $-20\text{ dB} \implies 0.1\text{ V}$ output at $74\text{ dB}$ sound pressure.
        
          
        

### Types of Microphones

#### 1. Carbon Microphone

- **Mechanism:** Sound waves $\to$ diaphragm flexes $\to$ compresses carbon granules $\to$ resistance $R$ changes.
    
      
    
- **Power:** External constant-DC voltage source required.
    
      
    
- **Specs:**
    
      
    - Range: $\le 5\text{ kHz}$.
        
          
        
    - Impedance: Low.
        
          
        
    - Sensitivity: High ($\approx 400\text{ dB}$).
        
          
        
    - Application: Telephony.
        
          
        

#### 2. Capacitive Microphone

- **Mechanism:** Diaphragm forms one plate of a capacitor.
    
      
    
    $$\text{Sound pressure} \implies \Delta d \implies \Delta C = \frac{\varepsilon A}{d} \implies \Delta V$$
    
      
    
- **Power:** Requires $200\text{--}500\text{ V}$ bias (phantom power).
    
      
    
- **Specs:**
    
      
    - Range: Up to $50\text{ kHz}$.
        
          
        
    - Sensitivity: $\approx -50\text{ dB}$.
        
          
        
    - Role: Standards, precision lab measurement (expensive, highly accurate).
        
          
        

#### 3. Dynamic (Electromagnetic) Microphone

- **Mechanism:** Diaphragm moves attached coil inside permanent magnet field $\implies \text{induced emf}$ (Faraday's Law).
    
      
    
- **Type:** Self-generating (no bias needed).
    
      
    
- **Specs:**
    
      
    - Range: $\le 20\text{ kHz}$.
        
          
        
    - Sensitivity: Low ($\approx -80\text{ dB}$).
        
          
        
    - Impedance: Low.
        
          
        
    - Application: Field/vocal use; not for precision calibration.
        
          
        

#### 4. Inductive Microphone

- **Mechanism:** Diaphragm alters core magnetic properties $\implies \Delta\text{dimension} \implies$ sensed by displacement transducer.
    
      
    
- **Specs:** Low $Z_{\text{out}}$, low sensitivity ($-100\text{ dB}$), ultrasonic band.
    
      
    
- **Application:** Underwater acoustic transducers.
    
      
    

#### 5. Piezoelectric Microphone

- **Mechanism:** Pressure on piezoelectric crystal produces voltage directly.
    
      
    
- **Type:** Self-generating.
    
      
    
- **Drawbacks:** High $Z_{\text{out}}$, temperature drift, vibration sensitivity.
    
      
    
- **Specs:** Sensitivity: $-50 \text{ to } -100\text{ dB}$; highly linear over wide amplitude range.
    
      
    

## Cameras

- **Origin:** Greek _camera obscura_ ("dark chamber").
    
      
    
- **Definition:** Optical instrument capturing light onto photosensitive surfaces/sensors.
    
      
    

### Core Architecture & Flowchart

$$\text{Subject} \xrightarrow{\text{Light}} \text{Lens} \xrightarrow{\text{Aperture}} \text{Shutter} \xrightarrow{\text{Sensor/Film}} \text{Image File/Negative}$$

  

- **Reflex Optical Path (Viewing Mode):**
    
      
    
    $$\text{Lens} \to \text{Diaphragm} \to \text{Mirror (Down, } 45^\circ) \to \text{Pentaprism} \to \text{Viewfinder}$$
    
      
    
- **Capture Path (Exposure Mode):**
    
      
    
    $$\text{Shutter Release Pressed} \to \text{Mirror Flips UP} \to \text{Shutter Opens} \to \text{Sensor/Film Exposed}$$
    
      
    

### Core Components & Subsystems

- **Camera Body:** Light-tight protective enclosure housing internal electronics, mirror, and sensor.
    
      
    
- **Lens:** System of optical glass elements; gathers and converges light onto the image focal plane.
    
      
    
- **Pentaprism:** $45^\circ$ roof prism system; redirects and un-reverses image to the eye-level viewfinder (eliminates looking downward).
    
      
    
- **Viewfinder / LCD:** Framing monitor (optical window or live digital screen).
    
      
    
- **Shutter & Release:** Opaque mechanical curtain or electronic gate; opened via shutter release button for calibrated duration.
    
      
    
- **Hot Shoe Mount:** Top bracket with electrical contacts for synchronizing external strobe/flash units.
    
      
    
- **Lens Ring Mount:** Front metal bayonet with release button for mounting interchangeable lenses.
    
      
    
- **Film Compartment:** Light-tight rear chamber with motorized/manual rewind spool (must rewind before opening to prevent fogging).
    
      
    

### Exposure Controls

#### 1. Focus

- **Concept:** Adjusts lens-to-sensor distance to render subject details sharpest.
    
      
    

#### 2. Aperture ($f$-stop)

- **Concept:** Adjustable diaphragm opening size inside the lens.
    
      
    
- **Rule:**
    
      
    
    $$\text{Small } f\text{-number (e.g., } f/2.8) \iff \text{Large Opening} \iff \text{High Light} \iff \text{Shallow Depth of Field (DOF)}$$
    
      
    
    $$\text{Large } f\text{-number (e.g., } f/22) \iff \text{Small Opening} \iff \text{Low Light} \iff \text{Deep / Greatest DOF}$$
    
      
    

#### 3. Shutter Speed

- **Concept:** Duration the sensor/film is exposed to light.
    
      
    
- **Display Notation:** Fractional denominator (e.g., "$60$" $= 1/60\text{ s}$).
    
      
    
- **Dynamics:**
    
      
    - Fast (e.g., $1/1000\text{ s}$): Freezes high-speed motion.
        
          
        
    - Slow (e.g., $1/4\text{ s}$): Blurs motion; accumulates ambient light.
        
          
        

#### 4. ISO (Film Speed / Sensor Gain)

- **Concept:** Digital sensor amplification or film sensitivity rating.
    
      
    
- **Rule:**
    
      
    - Low ISO ($100$): Low sensitivity $\implies$ Clean image, minimum noise/grain.
        
          
        
    - High ISO ($800+$): High sensitivity $\implies$ Works in low light, introduces grain/noise.
        
          
        

Based on the provided text, the derivation for measuring high-impedance components using a **parallel connection** in a Q meter is structured as follows:

### 1. Circuit Setup and Initial Resonance (Reference Condition)

A high-impedance component (such as a high-value resistor, certain inductors, or small capacitors) is connected in parallel across the tuning capacitor of the Q-meter circuit.

  

Before connecting the unknown component under test, the circuit is resonated using a suitable working coil ($L$) to establish reference values:

- **Tuning capacitance:** $C_1$
- **Circuit Q:** $Q_1$

At this initial resonance condition, the inductive reactance of the working coil ($\omega L$) equals the capacitive reactance of the tuning capacitor:

  

$$\omega L = \frac{1}{\omega C_1} \quad \text{}$$

  

The reference Q factor is expressed as:

  

$$Q_1 = \frac{\omega L}{R} = \frac{1}{\omega C_1 R} \quad \text{}$$

  

_(where $R$ is the resistance of the working coil)_

### 2. Second Resonance (With Unknown Connected)

When the unknown impedance is connected into the circuit in parallel, the capacitor is readjusted to bring the circuit back to resonance. This yields new circuit values:

- **New tuning capacitance:** $C_2$
- **New circuit Q:** $Q_2$

At this new resonant state, the reactance of the working coil ($X_L$) equals the parallel combination of the reactances of the adjusted tuning capacitor ($X_{C_2}$) and the unknown component ($X_p$):

  

$$X_L = \frac{(X_{C_2})(X_p)}{X_{C_2} + X_p} \quad \text{}$$

  

Solving this relationship for the unknown parallel reactance component ($X_p$) reduces to:

  

$$X_p = \frac{1}{\omega(C_1 - C_2)} \quad \text{}$$

- **If the unknown is inductive:** $X_p = \omega L_p$, which yields the parallel inductance value:
    
      
    
    $$L_p = \frac{1}{\omega^2(C_1 - C_2)} \quad \text{}$$
- **If the unknown is capacitive:** $X_p = \frac{1}{\omega C_p}$, which yields the parallel capacitance value:
    
      
    
    $$C_p = C_1 - C_2 \quad \text{}$$

### 3. Derivation of Parallel Resistance ($R_p$)

To find the resistive component ($R_p$) of the unknown parallel impedance, total circuit conductances are computed:

  

$$\text{Let } G_T = \text{total conductance}, \quad G_p = \text{conductance of unknown}, \quad G_L = \text{conductance of working coil} \quad \text{}$$

  

The relationship between conductances at resonance is:

  

$$G_T = G_p + G_L \implies G_p = G_T - G_L \quad \text{}$$

  

In a parallel resonant circuit, the total resistance at resonance ($R_T$) equals the product of the circuit Q ($Q_2$) and the reactance of the coil ($X_L$). Substituting $\omega L = \frac{1}{\omega C_1}$, we get:

  

$$R_T = Q_2 X_L = \frac{Q_2}{\omega C_1} \quad \text{}$$

  

Therefore, the total conductance ($G_T$) is:

  

$$G_T = \frac{1}{R_T} = \frac{\omega C_1}{Q_2} \quad \text{}$$

  

By definition, the conductance of the unknown component is $\frac{1}{R_p}$. Substituting the circuit details, the expression becomes:

  

$$\frac{1}{R_p} = \frac{\omega C_1}{Q_2} - \frac{R}{R^2 + \omega^2L^2} = \frac{\omega C_1}{Q_2} - \frac{1}{RQ_1^2} \quad \text{}$$

  

By substituting the initial reference equation $Q_1 = \frac{1}{\omega C_1 R}$ into the expression, it simplifies to:

  

$$\frac{1}{R_p} = \frac{\omega C_1}{Q_2} - \frac{\omega C_1}{Q_1} \quad \text{}$$

  

Simplifying further to solve directly for the parallel resistance ($R_p$) gives:

  

$$R_p = \frac{Q_1 Q_2}{\omega C_1 (Q_1 - Q_2)} = \frac{Q_1 Q_2}{\omega C_1 \Delta Q} \quad \text{}$$

  

_(where $\Delta Q$ is the change in the circuit Q value, $Q_1 - Q_2$)_

### 4. Derivation of the Unknown Component's Q ($Q_p$)

Finally, using the definitions derived for $R_p$ and $X_p$, the storage factor (Q) of the unknown parallel component is determined via $Q_p = \frac{R_p}{X_p}$:

  

$$Q_p = \frac{(C_1 - C_2)(Q_1 Q_2)}{C_1(Q_1 - Q_2)} = \frac{(C_1 - C_2)(Q_1 Q_2)}{C_1 \Delta Q} \quad \text{}$$
