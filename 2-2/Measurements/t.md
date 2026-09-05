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
        
          
        

## Q-Meter

- **Definition:** Specialized instrument designed to directly measure quality factor ($Q$), plus characteristics of coils and capacitors.
    
      
    
- **$Q$ Formulae:**
    
      
    - **Inductive Load:**
        
          
        
        $$Q = \frac{X_L}{R} = \frac{\omega L}{R}$$
        
          
        
    - **Capacitive Load:**
        
          
        
        $$Q = \frac{X_C}{R} = \frac{1}{\omega C R}$$