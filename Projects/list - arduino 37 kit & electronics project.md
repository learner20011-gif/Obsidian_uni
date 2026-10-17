Transforming the **37-in-1 KY-Series Sensor Kit**, discrete electronics, **Arduino**, **ESP32/ESP8266**, **Raspberry Pi**, and a **high-end PC** into an advanced Electrical and Electronic Engineering (EEE) research laboratory requires bypassing the basic "plug-and-play" digital outputs (`DO`) on the sensor modules. By tapping directly into the raw transducer signals, building custom discrete Analog Front-Ends (AFEs) with your soldering iron, and leveraging heavy mathematical/simulation software (**MATLAB/Simulink, LabVIEW, LTSpice, KiCad, Python/PyTorch, GNU Radio, ROS2**), you can execute senior undergraduate design projects and graduate-level research experiments.

  

## Hardware Modification Prerequisite: Hacking the KY-Series for Research

Before starting these projects, apply these four hardware modifications to elevate the KY-series modules from hobbyist toys to scientific transducers:

  

- **Bypass the LM393 Comparator:** Modules like **KY-024** (Linear Hall), **KY-026** (Flame/IR Photodiode), **KY-028** (NTC), **KY-036** (Metal Touch), and **KY-037/038** (Microphone) use a low-grade LM393 comparator to generate a binary threshold. Always tap the raw analog pin (`AO`) or solder a jumper wire directly to the transducer leg before the onboard bias resistor to feed your own custom discrete op-amp instrumentation stages.
    
      
    
- **Remove Parasitic LEDs:** Many KY modules wire an indicator LED directly in parallel with the signal line, introducing non-linear voltage clamping and noise. Desolder these indicator LEDs when performing microvolt-level analog measurements.
    
      
    
- **Shielding and Star Grounding:** Solder coaxial cables (or twisted-pair wires) to acoustic (**KY-037**), optical (**KY-039**), and magnetic (**KY-024**) modules, and enclose optical modules in matte-black heat-shrink tubing to eliminate ambient 50Hz/60Hz optical mains flicker.
    
      
    
- **External ADC/DAC Upgrades:** The Arduino's 10-bit SAR ADC and ESP32's non-linear 12-bit ADC have high Integral Non-Linearity (INL). Use external discrete delta-sigma bridges, oversampling with dithering, or high-speed timer-triggered DMA transfers to maximize Effective Number of Bits (ENOB).
    
      
    

## 1. Analog Front-End (AFE) Design, Instrumentation & Mixed-Signal Circuits

- **1. Synchronous Lock-In Amplifier for Nanowatt Optical Detection**
    
      
    - **Stack:** KY-008 (Laser) or KY-005 (IR LED), KY-026 (Photodiode), Discrete Op-Amps/Analog Switches (CD4053 or BJT chopper), Arduino, MATLAB.
        
          
        
    - **Description:** Modulate the optical transmitter at a known reference carrier frequency (e.g., 5 kHz) and build a discrete phase-sensitive detector (multiplier + low-pass filter) to extract optical signals buried 40 dB below the ambient noise floor.
        
          
        
- **2. Transimpedance Amplifier (TIA) Bandwidth & Stability Compensation Study**
    
      
    - **Stack:** KY-026 (Photodiode) / KY-039 (Phototransistor), KY-008 (Laser), Discrete Op-Amps, Capacitors, LTSpice, PC Soundcard/Oscilloscope.
        
          
        
    - **Description:** Desolder the photodiode from KY-026, model its junction capacitance in LTSpice, and solder a high-speed TIA with a feedback phase-lead capacitor to eliminate gain peaking and ringing under square-wave laser excitation.
        
          
        
- **3. Precision Constant-Current Wheatstone Bridge & Three-Op-Amp Instrumentation Amplifier**
    
      
    - **Stack:** KY-013 (NTC Thermistor), KY-018 (LDR), Discrete Resistors, BJT Current Mirror, Three Op-Amps, LTSpice.
        
          
        
    - **Description:** Construct a discrete instrumentation amplifier from scratch, measure its Common-Mode Rejection Ratio (CMRR) across frequency, and interface it with a temperature-compensated Wheatstone bridge driven by a BJT Howland current source.
        
          
        
- **4. Discrete First-Order Sigma-Delta ($\Sigma\Delta$) ADC Modulator**
    
      
    - **Stack:** KY-013 (Thermistor), Discrete Integrator Op-Amp, Comparator, D-Flip-Flop (or Arduino high-speed ISR), MATLAB Simulink.
        
          
        
    - **Description:** Build a 1-bit hardware oversampling $\Sigma\Delta$ modulator on a breadboard, capture the high-frequency 1-bit bitstream on an MCU digital pin, and implement a Sinc³ decimation filter in MATLAB to achieve 16-bit resolution without using an analog pin.
        
          
        
- **5. Chopper-Stabilized Microvolt Amplifier for 1/f (Flicker) Noise Cancellation**
    
      
    - **Stack:** KY-024 (Linear Hall), Discrete MOSFETs, Op-Amps, Arduino (Clock Generator), Python (SciPy).
        
          
        
    - **Description:** Design a continuous-time modulator-demodulator (chopper) front-end that up-converts DC magnetic Hall voltages above the op-amp's $1/f$ noise corner frequency, amplifies the signal, and synchronously demodulates it back to baseband.
        
          
        
- **6. Hardware Dithering and Oversampling to Overcome ESP32 ADC Non-Linearity**
    
      
    - **Stack:** ESP32, KY-013 (NTC), KY-038 (Mic), RC DAC / White Noise Generator, Python.
        
          
        
    - **Description:** Inject controlled triangular or Gaussian white noise into the analog input of an ESP32, sample at 100 kSPS via I2S DMA, and mathematically prove and demonstrate a 3-bit increase in ENOB and reduction in harmonic distortion.
        
          
        
- **7. Programmable Gain Instrumentation Amplifier (PGIA) with Automatic Gain Control (AGC)**
    
      
    - **Stack:** KY-037 (Mic), Discrete JFET/MOSFET attenuator or R-2R network, Op-Amps, Arduino, KiCad.
        
          
        
    - **Description:** Design a closed-loop mixed-signal AGC circuit where the Arduino monitors signal envelope peaks and dynamically switches feedback resistor networks to maintain a constant RMS output amplitude over a 60 dB dynamic range.
        
          
        
- **8. Negative Impedance Converter (NIC) and Gyrator Active Filter Bank**
    
      
    - **Stack:** KY-038 (Mic), Discrete Op-Amps, Capacitors, Resistors (No physical inductors), LTSpice, MATLAB.
        
          
        
    - **Description:** Synthesize large virtual inductors using Antoniou's gyrator circuit to build a steep multi-stage Chebyshev hardware graphic equalizer and spectrum analyzer for acoustic signals.
        
          
        
- **9. Analog Logarithmic and Antilogarithmic Amplifier for Wide-Range Photometry**
    
      
    - **Stack:** KY-018 (LDR) / KY-026 (Photodiode), Matched BJT Pair, Op-Amps, KY-013 (for thermal compensation), LTSpice.
        
          
        
    - **Description:** Exploit the exponential Ebers-Moll $I_C$-$V_{BE}$ relation of a BJT in the op-amp feedback loop to compress 5 decades of optical intensity into a linear voltage scale, using KY-013 to compensate for the $V_T = kT/q$ thermal drift.
        
          
        
- **10. Sample-and-Hold (S/H) Circuit with Charge Injection & Droop Rate Compensation**
    
      
    - **Stack:** Discrete MOSFETs, Low-leakage Film Capacitors, Op-Amps, Arduino, KY-023 (Joystick/Analog Source).
        
          
        
    - **Description:** Build a discrete dual-stage S/H circuit, characterize capacitor droop rate and MOSFET gate-channel charge injection glitches, and implement dummy-switch cancellation.
        
          
        
- **11. Switched-Capacitor Filter (SCF) Driven by Arduino PWM Clock**
    
      
    - **Stack:** Discrete CMOS Switches/MOSFETs, Capacitors, Op-Amps, Arduino (Timer1 CTC mode), KY-037 (Mic).
        
          
        
    - **Description:** Replace physical resistors with rapidly switched capacitors to construct a biquad bandpass filter whose center frequency scales linearly with the Arduino's hardware timer frequency.
        
          
        
- **12. Phase-Locked Loop (PLL) Carrier Recovery from Noisy IR Signals**
    
      
    - **Stack:** KY-005 (IR TX), KY-026 (Photodiode RX), Discrete VCO + Phase Detector (or CD4046), Loop Filter, LTSpice.
        
          
        
    - **Description:** Design an analog/mixed-signal PLL to lock onto a weak, phase-jittered optical carrier, analyzing lock range, capture range, and loop damping factor in Simulink and hardware.
        
          
        

## 2. Free-Space Optical (FSO) Communications, Photonics & Laser Physics

- **13. High-Speed Free-Space Optical (FSO) OFDM Transceiver**
    
      
    - **Stack:** KY-008 (Laser Diode), KY-026 (Photodiode + custom TIA), ESP32 (I2S DAC/ADC), GNU Radio / MATLAB.
        
          
        
    - **Description:** Implement Direct-Current-Biased Optical Orthogonal Frequency Division Multiplexing (DCO-OFDM) in MATLAB, stream symbols via ESP32 DAC to modulate the KY-008 laser intensity, and evaluate Bit Error Rate (BER) vs. atmospheric turbulence (induced by a heat gun).
        
          
        
- **14. Laser Doppler Vibrometry / Optical Microphone via Speckle Interferometry**
    
      
    - **Stack:** KY-008 (Laser), KY-026 (Photodiode) or KY-039 (Phototransistor), KY-006 (Buzzer attached to a reflective membrane), Op-Amp High-Gain Bandpass, PC Audio/MATLAB.
        
          
        
    - **Description:** Bounce the KY-008 laser beam off a distant vibrating surface onto a pinhole-masked photodiode, converting nanometer-scale surface deflections into intensity variations to recover audio/vibration remotely without physical contact.
        
          
        
- **15. Optical Time-of-Flight (ToF) Phase-Shift Distance Ranging**
    
      
    - **Stack:** KY-008 (Laser), KY-026 (Photodiode), High-frequency RF Oscillator (Colpitts/Crystal), RF Mixer (Discrete BJT Gilbert Cell), Arduino, MATLAB.
        
          
        
    - **Description:** Modulate the laser at high frequency (10–30 MHz using a discrete oscillator), mix the received photodiode signal with the local oscillator to measure phase shift, and resolve sub-meter distance variations optically.
        
          
        
- **16. 4-PAM (Pulse Amplitude Modulation) Optical Link with Decision Feedback Equalizer (DFE)**
    
      
    - **Stack:** KY-005 (IR LED), KY-039 (Phototransistor), R-2R DAC on Arduino, ESP32 High-Speed ADC, Python.
        
          
        
    - **Description:** Drive the IR LED with 4-level PAM symbols beyond the phototransistor's 3 dB RC bandwidth to intentionally induce Inter-Symbol Interference (ISI), then implement a real-time LMS adaptive Decision Feedback Equalizer in Python to open the eye diagram.
        
          
        
- **17. Optical Chaos Communication Using Synchronized Lorenz/Chua Circuits**
    
      
    - **Stack:** Two Discrete Chua's Circuits (Op-Amps, Diodes, Inductors, Capacitors), KY-008 (Laser), KY-026 (Photodiode), LTSpice, Oscilloscope/PC.
        
          
        
    - **Description:** Build two chaotic analog oscillators, mask an audio signal inside the chaotic state variable of the transmitter, transmit it optically via the laser, and achieve chaos synchronization at the receiver to strip away the chaotic carrier.
        
          
        
- **18. Wavelength-Division Multiplexing (WDM) Over a Single Optical Path**
    
      
    - **Stack:** KY-008 (650nm Red Laser), KY-005 (940nm IR LED), KY-016 (RGB LED - Blue/Green), KY-018 (LDR - visible peak), KY-026 (IR Photodiode - 940nm peak), ESP32, MATLAB.
        
          
        
    - **Description:** Simultaneously transmit three independent data streams on red, blue, and near-infrared wavelengths through a shared free-space channel, using spectral responsivity differences and MIMO matrix inversion to demultiplex the channels and cancel cross-talk.
        
          
        
- **19. Manchester-Encoded Full-Duplex TCP/IP Stack Over Laser/IR**
    
      
    - **Stack:** Two Raspberry Pis, Two KY-008 (Lasers), Two KY-026 (Photodiodes + Comparator), Linux Kernel `slcan` / Custom TUN/TAP Network Interface.
        
          
        
    - **Description:** Write a custom Linux user-space TUN/TAP network daemon in C that encapsulates raw IP packets into Manchester-encoded frames with CRC-32 and Reed-Solomon Forward Error Correction (FEC), allowing two Raspberry Pis to SSH and stream video over laser beams.
        
          
        
- **20. Optical Beam Tracking and Alignment System (FSO Pointing, Acquisition, and Tracking)**
    
      
    - **Stack:** KY-008 (Laser), Four Photodiodes/LDRs arranged as a Quadrant Detector (KY-018 + discrete LDRs), KY-023 (Joystick/Servos), Arduino, Simulink.
        
          
        
    - **Description:** Construct a 4-quadrant optical position sensor that computes horizontal and vertical beam deflection error ratios $(\Delta X, \Delta Y)$ to keep a communication laser locked onto a moving receiver target.
        
          
        
- **21. Non-Destructive Optical Absorption Spectroscopy & Beer-Lambert Concentration Analyzer**
    
      
    - **Stack:** KY-016 (RGB LED), KY-005 (IR LED), KY-008 (Laser), KY-026 (Photodiode), KY-018 (LDR), Arduino, Python (Scikit-Learn).
        
          
        
    - **Description:** Sequentially pulse multiple narrowband wavelengths through liquid samples in a cuvette, measure optical absorbance across the visible and NIR spectrum, and train a Partial Least Squares (PLS) regression model to estimate solute concentration.
        
          
        
- **22. Direct Sequence Spread Spectrum (DSSS) Optical Link Immune to Jamming**
    
      
    - **Stack:** KY-005 (IR LED), KY-026 (Photodiode), KY-032 (Jamming IR source), ESP32, MATLAB.
        
          
        
    - **Description:** Multiply low-rate telemetry data by a high-rate Pseudo-Random Noise (PRN) Gold code before optical transmission, demonstrating complete signal recovery even when an interfering IR source (KY-032) saturates the environment with pulsed noise.
        
          
        
- **23. Hanbury Brown and Twiss (HBT) Optical Intensity Correlation Experiment**
    
      
    - **Stack:** KY-008 (Laser passing through rotating ground-glass diffuser), Two Photodiodes (KY-026 + discrete), High-speed Dual ADC (ESP32/RPi), Python.
        
          
        
    - **Description:** Split a pseudo-thermal laser speckle field onto two spatially separated photodetectors and compute the second-order intensity correlation function $g^{(2)}(\tau)$ as a function of detector separation and temporal delay.
        
          
        
- **24. Rolling-Shutter Optical Camera Communication (OCC)**
    
      
    - **Stack:** KY-009 (SMD RGB LED), Mosfet Driver, Arduino (High-frequency FSK/OOK modulator), Raspberry Pi Camera / PC Webcam, OpenCV.
        
          
        
    - **Description:** Modulate the RGB LED at frequencies between 1 kHz and 10 kHz to create dark/bright horizontal striation bands across a CMOS camera's rolling shutter frame, decoding data packets in real time using OpenCV image processing.
        
          
        

## 3. Biomedical Engineering, Physiological Signal Processing & Bio-Instrumentation

- **25. Cuffless Continuous Blood Pressure Estimation via Pulse Transit Time (PTT)**
    
      
    - **Stack:** KY-039 (PPG Heartbeat Sensor), KY-036 (Modified into a dry-electrode ECG lead with discrete Instrumentation Amp), ESP32, Python (BioSPPy / SciPy).
        
          
        
    - **Description:** Simultaneously acquire the R-peak of an Electrocardiogram (ECG) and the systolic foot of the finger Photoplethysmogram (PPG) at 1 kHz, calculating Pulse Transit Time (PTT) and applying the Moens-Korteweg arterial stiffness model to estimate systolic/diastolic blood pressure.
        
          
        
- **26. Reflection vs. Transmission Dual-Wavelength Pulse Oximetry ($SpO_2$) From Scratch**
    
      
    - **Stack:** KY-039 (940nm IR LED + Phototransistor), KY-008 or KY-011 (660nm Red LED), Time-Multiplexed H-Bridge/Driver, Arduino, MATLAB.
        
          
        
    - **Description:** Time-multiplex red (660 nm) and infrared (940 nm) illumination through a fingertip, separate AC pulsatile arterial absorption from DC venous/tissue absorption using digital IIR filtering, and compute the ratio-of-ratios $R$ to calibrate blood oxygen saturation ($SpO_2$).
        
          
        
- **27. Heart Rate Variability (HRV) Autonomic Nervous System Analyzer**
    
      
    - **Stack:** KY-039 (PPG Sensor), Custom Active Bandpass Filter (0.5 Hz – 8 Hz), Arduino, Python.
        
          
        
    - **Description:** Extract beat-to-beat R-R / P-P tachograms from the KY-039 sensor, compute time-domain metrics (RMSSD, SDNN), non-linear Poincaré plots ($SD_1/SD_2$), and Lomb-Scargle periodograms to quantify sympathetic vs. parasympathetic nervous activity (LF/HF ratio).
        
          
        
- **28. Motion Artifact Cancellation in Wearable PPG Using LMS/RLS Adaptive Filtering**
    
      
    - **Stack:** KY-039 (PPG), KY-002 / KY-031 (Piezo/Vibration reference mounted on finger), ESP32, MATLAB.
        
          
        
    - **Description:** Use the vibration/piezo sensor as a correlated motion noise reference $n(k)$ and implement a real-time Recursive Least Squares (RLS) adaptive filter to subtract motion artifacts from the corrupted PPG waveform during hand movement.
        
          
        
- **29. Digital Stethoscope & Phonocardiogram (PCG) Valvular Anomaly Classifier**
    
      
    - **Stack:** KY-037 / KY-038 (Electret Mic acoplado to a 3D-printed/plastic bell housing), Discrete Sallen-Key Low-Pass Filter (20 Hz – 500 Hz), Raspberry Pi, PyTorch.
        
          
        
    - **Description:** Capture heart sounds ($S_1, S_2$ lub-dub and systolic/diastolic murmurs), compute continuous wavelet transform (CWT) scalograms using Morlet wavelets, and run a Convolutional Neural Network (CNN) on Raspberry Pi to detect simulated murmurs.
        
          
        
- **30. Ballistocardiography (BCG) Non-Contact Cardiorespiratory Monitor**
    
      
    - **Stack:** KY-031 (Piezo Knock Sensor element) or KY-024 (Linear Hall + spring-suspended magnet), Charge Amplifier (Op-Amp), Arduino, MATLAB.
        
          
        
    - **Description:** Couple a high-sensitivity charge amplifier to the piezo element placed under a chair cushion or wrist strap to detect the mechanical recoil of the body caused by blood ejection into the aorta at each heartbeat.
        
          
        
- **31. Surface Electromyography (sEMG) Prosthetic Control Interface**
    
      
    - **Stack:** KY-036 (Darlington/MOSFET front-end modified into differential instrumentation amp + Driven Right Leg circuit), Op-Amps, ESP32, Python.
        
          
        
    - **Description:** Build an analog bio-potential amplifier with a 50Hz/60Hz Twin-T notch filter, extract muscle contraction envelopes (RMS, Zero-Crossing Rate, Mean Absolute Value) from forearm flexors, and classify hand gestures in real time.
        
          
        
- **32. Galvanic Skin Response (GSR) / Electrodermal Activity (EDA) Sympathetic Arousal Tracker**
    
      
    - **Stack:** KY-036 (Touch pads), Sub-microampere Constant-Voltage Source (0.5V), Low-Pass Op-Amp Stage, Arduino, LabVIEW.
        
          
        
    - **Description:** Measure skin conductance conductance levels (SCL) and phasic skin conductance responses (SCR) in microsiemens ($\mu\text{S}$), using LabVIEW to deconvolve tonic baseline drift from acute sympathetic nervous spikes during cognitive stress tests.
        
          
        
- **33. Thermal Respiration Rate and Apnea Detection Flowmeter**
    
      
    - **Stack:** KY-013 (NTC Thermistor with glass bead exposed), KY-015 (DHT11), Wheatstone Bridge, Differentiator Op-Amp, ESP32.
        
          
        
    - **Description:** Place the low-thermal-mass NTC thermistor in a nasal/oral airflow path, using an analog differentiator circuit to track the derivative $dT/dt$ of inhaled vs. exhaled air, eliminating ambient room temperature drift.
        
          
        
- **34. Bio-Impedance Spectroscopy (BIS) Tissue Composition Phantom Analyzer**
    
      
    - **Stack:** Arduino/ESP32 (DDS Sine Wave Generator via DAC), Discrete Howland Current Pump, Instrumentation Amp, Phase Detector, Saline/Agar Phantom.
        
          
        
    - **Description:** Inject a constant sub-milliamp AC current swept from 1 kHz to 100 kHz across four electrodes in a biological phantom, measuring magnitude and phase impedance to plot the Cole-Cole impedance locus.
        
          
        
- **35. Optoelectronic Tremor Quantifier for Parkinsonian Kinematics**
    
      
    - **Stack:** KY-008 (Laser), KY-033 (Reflective IR), KY-024 (Linear Hall), Arduino, MATLAB.
        
          
        
    - **Description:** Measure 4–6 Hz resting vs. postural finger tremors using high-speed optical reflection and magnetic displacement sensing, performing Welch's power spectral density estimation to track tremor amplitude and frequency stability.
        
          
        
- **36. Real-Time Biofeedback Coherence Loop with Respiratory Sinus Arrhythmia (RSA) Pacing**
    
      
    - **Stack:** KY-039 (PPG), KY-016 (RGB LED), KY-006 (Passive Buzzer), ESP32, Python GUI.
        
          
        
    - **Description:** Compute real-time cross-spectral coherence between a guided breathing visual pacer (RGB LED sine wave) and the user's instantaneous heart rate oscillations, dynamically adjusting the breathing frequency to maximize vagal tone resonance (~0.1 Hz).
        
          
        

## 4. Control Systems, Mechatronics & State-Space Estimation

- **37. Electromagnetic Levitation (MagLev) System with State-Space LQR & PID Control**
    
      
    - **Stack:** KY-024 or KY-035 (Linear Hall Sensor), Custom Hand-Wound Electromagnet (or modified KY-019 relay coil with armature removed), Power MOSFET + Flyback Diode, Arduino/ESP32, MATLAB/Simulink.
        
          
        
    - **Description:** Linearize the highly unstable, non-linear magnetic force equation $F \propto I^2 / x^2$ around an equilibrium point using Jacobian matrices, implement a high-speed PID or Linear Quadratic Regulator (LQR) with a Luenberger state observer, and levitate a neodymium magnet in mid-air.
        
          
        
- **38. Optical Levitation / Aerodynamic Ping-Pong Ball Tube Balancer**
    
      
    - **Stack:** KY-032 (IR Obstacle) or KY-033 (Reflective IR array), PC Cooling Fan + MOSFET PWM Driver, KY-040 (Rotary Encoder for setpoint), Arduino, LabVIEW.
        
          
        
    - **Description:** Build a vertical acrylic/cardboard wind tunnel, calibrate the non-linear inverse-square optical reflection from KY-033 to measure ball height, and implement cascade PID control with anti-windup and derivative filtering in LabVIEW.
        
          
        
- **39. Pendulum-on-a-Cart / Furuta Rotary Inverted Pendulum Stabilization**
    
      
    - **Stack:** KY-040 (Rotary Encoder for pendulum angle), DC Motor + Optical Slotted Disk with KY-010 (Photo-interrupter for motor velocity/position), H-Bridge, ESP32, Simulink.
        
          
        
    - **Description:** Execute an energy-based swing-up controller that transitions smoothly into a full-state feedback LQR controller to balance an inverted pendulum attached to the KY-040 rotary encoder shaft.
        
          
        
- **40. System Identification via Pseudo-Random Binary Sequence (PRBS) Excitation**
    
      
    - **Stack:** Any Thermal (KY-013 + Heater Resistor) or Electromechanical plant, Arduino, MATLAB System Identification Toolbox.
        
          
        
    - **Description:** Inject a maximal-length LFSR (Linear Feedback Shift Register) PRBS signal into a physical plant, log the input-output time series, and identify ARX, ARMAX, and Box-Jenkins transfer functions in MATLAB.
        
          
        
- **41. Extended Kalman Filter (EKF) Multi-Sensor Fusion for 1D/2D Kinematics**
    
      
    - **Stack:** KY-040 (Rotary Encoder), KY-010 (Optical Interrupter), KY-024 (Linear Hall), KY-033 (IR Reflective), ESP32, Python.
        
          
        
    - **Description:** Fuse high-drift, high-rate velocity measurements with low-rate, noisy absolute position updates inside an Extended Kalman Filter to track position, velocity, and acceleration under severe sensor dropout.
        
          
        
- **42. Sliding Mode Control (SMC) for a Non-Linear Thermal Chamber**
    
      
    - **Stack:** KY-001 (DS18B20), KY-013 (NTC), Power Resistor / Peltier Heater (driven via MOSFET), Fan (disturbance generator), Arduino, MATLAB.
        
          
        
    - **Description:** Design a variable-structure Sliding Mode Controller with a hyperbolic tangent boundary layer (to suppress chattering) that maintains sub-0.1°C thermal stability even when a fan introduces sudden convective heat-loss disturbances.
        
          
        
- **43. Hardware-in-the-Loop (HIL) Real-Time Plant Emulator**
    
      
    - **Stack:** Raspberry Pi or ESP32 (emulating a physical aircraft pitch or power converter plant via DAC), Arduino (running the embedded controller), Simulink.
        
          
        
    - **Description:** Solve differential equations of a virtual dynamic system in real time on the ESP32 using 4th-order Runge-Kutta (RK4) integration, output the state variables as analog voltages to the Arduino ADC, and close the control loop via PWM.
        
          
        
- **44. Model Predictive Control (MPC) on an Embedded Microcontroller**
    
      
    - **Stack:** ESP32, KY-013 (NTC), KY-018 (LDR), Heater + LED coupled plant (MIMO), Python / C++ Eigen Library.
        
          
        
    - **Description:** Build a coupled Multi-Input Multi-Output (MIMO) plant where an incandescent/high-power bulb produces both light (measured by KY-018) and heat (measured by KY-013), and run a constrained Quadratic Programming (QP) MPC solver on the ESP32 to decouple and control both states independently.
        
          
        
- **45. High-Precision Quadrature Encoder Velocity Estimation via M/T Method & Phase-Locked Observer**
    
      
    - **Stack:** KY-040 (Rotary Encoder) or KY-010 (Dual Photo-interrupters on slotted wheel), Arduino (Input Capture Unit ICP1), MATLAB.
        
          
        
    - **Description:** Overcome quantization noise at both ultra-low and ultra-high speeds by combining pulse counting ($M$-method) and high-frequency clock period timing ($T$-method) with a software tracking loop observer.
        
          
        
- **46. Fuzzy Logic vs. Relay Auto-Tuned Åström-Hägglund PID Controller**
    
      
    - **Stack:** Arduino, KY-019 (Relay) or MOSFET, KY-013 (NTC), Heater Plant, Python GUI.
        
          
        
    - **Description:** Implement an automated relay-feedback experiment that induces a controlled limit cycle to identify the ultimate gain ($K_u$) and ultimate period ($T_u$) automatically, computing Ziegler-Nichols and Tyreus-Luyben parameters on the fly and benchmarking them against a Mamdani Fuzzy Logic controller.
        
          
        
- **47. Iterative Learning Control (ILC) for Repetitive Trajectory Tracking**
    
      
    - **Stack:** DC Motor + KY-010 (Optical Encoder) + KY-024 (Hall index), H-Bridge, Arduino, MATLAB.
        
          
        
    - **Description:** Implement an Arimoto-type Iterative Learning Control law $u_{k+1}(t) = u_k(t) + \Gamma \dot{e}_k(t)$ that learns from tracking errors on previous periodic passes to reduce trajectory error to zero despite unmodeled friction.
        
          
        
- **48. Haptic Force-Feedback Master-Slave Bilateral Teleoperation System**
    
      
    - **Stack:** KY-023 (Joystick), KY-040 (Rotary Encoder + DC Motor as haptic actuator), KY-032/033 (Remote proximity sensor), Two ESP32s (linked via ESP-NOW), Simulink.
        
          
        
    - **Description:** Build a 1-DOF bilateral teleoperation link where obstacle proximity measured at the remote slave robot generates virtual spring-damper impedance forces felt physically by the operator on the master rotary actuator.
        
          
        

## 5. Acoustic Array Processing, Ultrasonics & Structural Health Monitoring

- **49. 2D Acoustic Beamforming & Time-Difference-of-Arrival (TDOA) Sound Source Localization**
    
      
    - **Stack:** 3 to 4 Microphones (KY-037 + KY-038 + discrete electrets), Multi-channel simultaneous/interleaved ADC (ESP32 / RPi + external ADC), Python (NumPy/SciPy).
        
          
        
    - **Description:** Implement the Generalized Cross-Correlation with Phase Transform (GCC-PHAT) algorithm and Delay-and-Sum / MUSIC beamforming across a planar microphone array to compute the azimuth and elevation angle of an acoustic source in real time.
        
          
        
- **50. Active Noise Cancellation (ANC) Duct Using Filtered-x Least Mean Squares (FxLMS)**
    
      
    - **Stack:** KY-037 (Reference Mic), KY-038 (Error Mic), KY-006 / Speaker (Anti-noise actuator), PVC Pipe Acoustic Duct, ESP32 (DSP loop), MATLAB.
        
          
        
    - **Description:** Build a 1D acoustic waveguide inside a PVC tube, estimate the secondary path transfer function $\hat{S}(z)$ offline, and run a real-time FxLMS adaptive filter on the ESP32 to create a zone of destructive acoustic interference.
        
          
        
- **51. Continuous-Wave (CW) Acoustic Doppler Radar / Velocity Sonar**
    
      
    - **Stack:** KY-006 (Passive Piezo Buzzer driven at ultrasonic resonance ~20–25 kHz), KY-037 (Mic with high-gain ultrasonic bandpass), ESP32, Python.
        
          
        
    - **Description:** Drive the passive piezo element with a pure high-frequency sinusoid, capture the backscattered acoustic wave from moving targets, perform IQ quadrature demodulation and Short-Time Fourier Transform (STFT), and plot real-time micro-Doppler velocity spectrograms.
        
          
        
- **52. Structural Health Monitoring (SHM) & Experimental Modal Analysis of a Cantilever Beam**
    
      
    - **Stack:** KY-031 (Piezo Knock Sensor element bonded to a metal ruler/beam), KY-024 (Linear Hall + tip magnet), KY-002 (Vibration), Arduino/PC Soundcard, MATLAB.
        
          
        
    - **Description:** Excite a cantilever beam with an impulse hammer tap, record ring-down vibrations via the piezo strain sensor and Hall displacement sensor, compute Frequency Response Functions (FRFs), and extract natural resonant frequencies ($\omega_n$) and damping ratios ($\zeta$) to detect structural cracks or added mass.
        
          
        
- **53. Acoustic Impulse Response & Room Reverberation ($RT_{60}$) Analyzer via Exponential Sine Sweep**
    
      
    - **Stack:** KY-038 (Mic), Speaker/KY-006, Raspberry Pi, Python.
        
          
        
    - **Description:** Generate a Farina logarithmic sine sweep, deconvolve the recorded room response using an inverse filter to separate linear room impulse response (RIR) from non-linear harmonic distortion, and compute the Schroeder backward integration curve to extract $RT_{60}$.
        
          
        
- **54. Solid-Plate Acoustic Touch Localization via Dispersive Lamb Wave Triangulation**
    
      
    - **Stack:** Three Piezo/Vibration Elements (KY-031, KY-002, KY-006 used as sensor) glued to corners of an acrylic/glass plate, High-speed Comparator/ADC on ESP32, Python.
        
          
        
    - **Description:** Convert any ordinary glass or acrylic sheet into a touch-screen interface by capturing the arrival times of bending waves (Lamb waves) generated when a finger taps the surface, solving hyperbolic triangulation equations.
        
          
        
- **55. Ultrasonic Chirp Pulse-Compression Sonar (Matched Filtering)**
    
      
    - **Stack:** KY-006 (Piezo Transmitter), KY-037 (Mic Receiver), Op-Amp Bandpass, ESP32, MATLAB.
        
          
        
    - **Description:** Transmit a Linear Frequency Modulated (LFM) chirp pulse (12 kHz to 22 kHz) and correlate the weak echo with the complex conjugate of the transmitted waveform (matched filtering) to achieve high range resolution and high SNR simultaneously.
        
          
        
- **56. Acoustic Levitation Standing-Wave Node Characterization**
    
      
    - **Stack:** Ultrasonic Piezo Transducers / Driven KY-006 array, MOSFET H-Bridge Driver, KY-037 (Sub-wavelength acoustic probe mic), Arduino, Ansys/MATLAB.
        
          
        
    - **Description:** Generate a high-intensity acoustic standing wave between a transducer and a reflector, using a pinhole-masked microphone attached to a lead-screw/encoder (KY-040) to map the spatial pressure nodes and antinodes.
        
          
        
- **57. Acoustic Cryptography & Covert Near-Ultrasonic Data Exfiltration**
    
      
    - **Stack:** KY-006 (Passive Buzzer), KY-037 (Mic), Raspberry Pi, GNU Radio.
        
          
        
    - **Description:** Transmit encrypted data payloads across an air-gapped room in the 18.5 kHz – 21 kHz near-ultrasonic band (inaudible to most adults) using Frequency-Hopping Spread Spectrum (FHSS) orPSK modulation.
        
          
        
- **58. Non-Destructive Testing (NDT) of Concrete/Wood via Ultrasonic Pulse Velocity (UPV)**
    
      
    - **Stack:** KY-006 (Piezo Pulser driven by high-voltage BJT avalanche/boost pulse), KY-031 (Piezo Receiver), High-speed Timer on ESP32/Arduino.
        
          
        
    - **Description:** Measure the microsecond propagation delay of longitudinal stress waves through solid materials to detect internal voids, honeycombing, or density anomalies.
        
          
        
- **59. Helmholtz Resonator & Acoustic Metamaterial Transmission Loss Testbed**
    
      
    - **Stack:** KY-006 (Sound Source), KY-037 & KY-038 (Two-microphone impedance tube setup), Arduino/PC, MATLAB.
        
          
        
    - **Description:** Implement the ISO 10534-2 two-microphone transfer-function method inside a tube to measure normal-incidence sound absorption coefficients and complex acoustic impedance of 3D-printed/cardboard Helmholtz resonators.
        
          
        
- **60. Phase-Vocoder Pitch Shifting & Real-Time Guitar/Voice DSP Effects Pedal**
    
      
    - **Stack:** KY-038 (Mic / Audio Preamp), KY-040 (Rotary Encoder for parameter control), KY-023 (Joystick for 2D wah/modulation control), ESP32 (I2S ADC/DAC), C++.
        
          
        
    - **Description:** Write circular DMA ring-buffer DSP algorithms on the ESP32 to implement fractional-delay flanging, biquad wah-wah filtering controlled in 2D by the joystick, and FFT overlap-add pitch shifting.
        
          
        

## 6. Electromagnetics, Power Electronics & Magnetic Sensing

- **61. Closed-Loop Synchronous Buck/Boost DC-DC Converter with Hall-Effect Current Mode Control**
    
      
    - **Stack:** Discrete Power MOSFETs, Toroidal Inductor, Schottky Diodes, Capacitors, KY-024 (Linear Hall placed inside a gapped ferrite toroid core), ESP32/Arduino (High-speed PWM), LTSpice.
        
          
        
    - **Description:** Cut a small air gap in a ferrite toroid inductor, insert the KY-024 Hall element to measure instantaneous inductor current $i_L(t)$ from DC to 50 kHz without resistive insertion loss, and implement Peak Current Mode Control.
        
          
        
- **62. Automated Ferromagnetic B-H Hysteresis Curve Tracer**
    
      
    - **Stack:** Custom Primary Excitation Coil & Secondary Sense Coil wound on a core, KY-024 (Linear Hall in air gap), Op-Amp Analog Integrator, Power Amplifier, Arduino, Python.
        
          
        
    - **Description:** Drive a ferromagnetic core into saturation with a low-frequency AC current, measure $H(t)$ via current shunt and $B(t)$ via both the KY-024 Hall sensor and an analog RC integrator on the secondary winding ($\int V dt$), and plot remanence ($B_r$), coercivity ($H_c$), and core loss area.
        
          
        
- **63. Eddy-Current Non-Destructive Crack & Coating Thickness Probe**
    
      
    - **Stack:** Hand-wound search coil + KY-024 (Linear Hall) or Colpitts Oscillator tank circuit, Arduino, MATLAB.
        
          
        
    - **Description:** Excite a small coil with a 50–200 kHz AC signal to induce eddy currents in adjacent conductive plates (aluminum/copper/steel), using the Hall sensor or oscillator frequency/amplitude shift to map sub-surface cracks and non-conductive coating thickness.
        
          
        
- **64. Zero-Crossing Hybrid Solid-State Circuit Breaker (HSSCB) Eliminating Contact Arcing**
    
      
    - **Stack:** KY-019 (5V Mechanical Relay), Parallel Power MOSFET / Triac, Zero-Crossing Detector (Op-Amp), KY-024 (Hall Current Fault Sensor), Arduino.
        
          
        
    - **Description:** Synchronize the mechanical opening and closing of the KY-019 relay with a parallel semiconductor switch so the semiconductor absorbs the turn-on inrush and turn-off inductive arc, while the mechanical relay carries steady-state current with zero conduction drop.
        
          
        
- **65. Resonant Inductive Wireless Power Transfer (WPT) with Automated Frequency Tracking**
    
      
    - **Stack:** Discrete MOSFET Half-Bridge Inverter, Series-Parallel Resonant LC Coils, KY-024 (Magnetic Flux Monitor), KY-013 (Thermal monitor), ESP32, LTSpice.
        
          
        
    - **Description:** Build a magnetic resonant coupling link, observe frequency splitting phenomena when coils are over-coupled, and implement a perturbation-and-observe (P&O) frequency controller on ESP32 to maintain Zero-Voltage Switching (ZVS) as coil distance varies.
        
          
        
- **66. Vector Magnetometer & 3-Axis Helmholtz Coil Earth Field Nulling System**
    
      
    - **Stack:** Three Linear Hall Sensors (KY-024, KY-035, plus discrete Hall or rotated single sensor), Three orthogonal square/circular coils, Op-Amp Current Drivers, Arduino.
        
          
        
    - **Description:** Construct a 1-axis or 3-axis Helmholtz coil cage, calibrate coil constants in Gauss/Ampere, and run a closed-loop feedback controller to cancel external magnetic disturbances and create a zero-field chamber.
        
          
        
- **67. Brushless DC (BLDC) / Switched Reluctance Motor From Scratch Using Hall Commutation**
    
      
    - **Stack:** KY-003 (Hall Switch), KY-021/025 (Reed Switches), KY-024 (Linear Hall), Hand-wound Stator Coils, Neodymium Rotor on Bearing, MOSFET 3-Phase Bridge, Arduino.
        
          
        
    - **Description:** Build an axial-flux or radial-flux electromagnetic motor from scratch, using KY-003/KY-024 for rotor position sensing to compare 6-step trapezoidal commutation against sinusoidal Field-Oriented Control (FOC).
        
          
        
- **68. Contactless AC/DC Smart Grid Current & Power Quality Analyzer (THD & Power Factor)**
    
      
    - **Stack:** KY-024 (Linear Hall clamped around AC wire), Resistive Voltage Divider / Small Transformer, ESP32, Python.
        
          
        
    - **Description:** Simultaneously sample line voltage and contactless Hall-effect current waveforms at 10 kHz, computing Real Power ($P$), Reactive Power ($Q$), Apparent Power ($S$), Displacement vs. True Power Factor, and Total Harmonic Distortion (THD) up to the 50th harmonic.
        
          
        
- **69. Capacitive & Inductive Proximity Tomography Array**
    
      
    - **Stack:** KY-036 (Touch/Capacitive), Multi-coil Inductive Array, Multiplexer, Arduino, MATLAB.
        
          
        
    - **Description:** Measure mutual capacitance and inductance variations across a planar electrode/coil array and apply Tikhonov-regularized inverse reconstruction algorithms to image metallic and dielectric objects hidden behind a non-metallic wall.
        
          
        
- **70. Flyback / Boost High-Voltage Pulse Generator & Marx Bank Simulator**
    
      
    - **Stack:** Discrete MOSFET, Inductor/Transformer, Diode-Capacitor Cockcroft-Walton Voltage Multiplier, KY-026 (UV/IR Arc Flash Detector), KY-037 (Acoustic discharge detector), LTSpice.
        
          
        
    - **Description:** Design a low-current, high-voltage Cockcroft-Walton cascade driven by an Arduino PWM boost stage, using optical (KY-026) and acoustic (KY-037) sensors to detect partial discharge (corona) onset before breakdown.
        
          
        
- **71. Maximum Power Point Tracking (MPPT) Solar Emulator & Perturb-and-Observe Converter**
    
      
    - **Stack:** Discrete Power Transistor configured as an Active I-V Solar Curve Emulator, KY-018 (LDR for irradiance modeling), KY-013 (NTC for cell temperature modeling), Buck Converter, Arduino, Simulink.
        
          
        
    - **Description:** Build an active electronic circuit whose I-V output curve dynamically mimics a solar panel based on real-time light (KY-018) and temperature (KY-013) readings, then test Incremental Conductance vs. P&O MPPT algorithms against it.
        
          
        
- **72. Magnetic Flux Leakage (MFL) Pipeline/Steel Wire Rope Defect Scanner**
    
      
    - **Stack:** Permanent Neodymium Magnets (Magnetic Yoke), KY-024 & KY-035 (Differential Linear Hall pair), KY-040 (Rotary Encoder Odometer), Arduino, Python.
        
          
        
    - **Description:** Magnetize a steel bar or wire rope near saturation using permanent magnets, scan along its length with a differential Hall sensor pair coupled to a rotary encoder wheel, and localize pitting or broken strands via flux leakage dipole signatures.
        
          
        

## 7. RF, Wireless Systems, Wi-Fi CSI & Software-Defined Networking

- **73. Device-Free Wi-Fi Channel State Information (CSI) Respiration & Presence Radar**
    
      
    - **Stack:** Two ESP32s (configured for raw 802.11 OFDM subcarrier CSI extraction), KY-039 (PPG) & KY-013 (Nasal Thermistor) as ground-truth wearables, Raspberry Pi, Python (PyTorch).
        
          
        
    - **Description:** Extract complex amplitude and phase across 52 Wi-Fi OFDM subcarriers between two ESP32s, apply Hampel outlier filtering and PCA denoising to detect human breathing and walking through walls, and validate accuracy against ground-truth physiological sensors.
        
          
        
- **74. Ultra-Low-Power Ambient Wi-Fi / RF Backscatter Communication Tag**
    
      
    - **Stack:** Discrete RF Diode/Transistor Switch, Dipole Antenna (soldered copper wire), Arduino (modulating antenna radar cross-section via KY-013/KY-018 data), ESP32 (Wi-Fi TX/RX), MATLAB.
        
          
        
    - **Description:** Build a battery-less/low-power backscatter tag that transmits sensor telemetry by switching the load impedance of a wire antenna between reflective and absorptive states, decoding the resulting Wi-Fi RSSI/CSI variations on an ESP32 receiver.
        
          
        
- **75. Deterministic TDMA Wireless Sensor Network Over ESP-NOW with Sub-Millisecond Sync**
    
      
    - **Stack:** Multiple ESP8266/ESP32 nodes, Raspberry Pi Gateway, KY-Series Sensors, Wireshark / Python.
        
          
        
    - **Description:** Bypass the standard Wi-Fi TCP/IP stack to build a custom Time-Division Multiple Access (TDMA) MAC layer on top of raw 802.11 action frames (ESP-NOW), achieving collision-free high-rate telemetry with beacon-based clock drift compensation.
        
          
        
- **76. Acoustic/Ultrasonic Software-Defined Radio (SDR) & QAM-16 Modem**
    
      
    - **Stack:** KY-006 (Buzzer TX), KY-037 (Mic RX), PC Soundcard / Raspberry Pi, GNU Radio.
        
          
        
    - **Description:** Use the acoustic channel as a proxy for RF propagation to build a complete 16-QAM transceiver in GNU Radio Companion—complete with Root-Raised-Cosine (RRC) pulse shaping, Costas loop carrier phase recovery, Mueller & Müller clock recovery, and constellation plotting.
        
          
        
- **77. Hybrid RF-Optical Handover Protocol (Wi-Fi + Free-Space Laser Fallback)**
    
      
    - **Stack:** ESP32 (Wi-Fi), KY-008 (Laser TX), KY-026 (Photodiode RX), Raspberry Pi, Python.
        
          
        
    - **Description:** Implement a vertical link-layer handover algorithm that continuously monitors RF packet loss/jamming and seamlessly switches real-time telemetry streams between 2.4 GHz Wi-Fi and the 650 nm optical laser channel with zero packet drops.
        
          
        
- **78. Automated 2D Radiation Pattern Antenna Range Using Rotary Encoder & RSSI/Detector**
    
      
    - **Stack:** ESP32/ESP8266 (RF Source + Receiver), Custom Soldered Yagi-Uda / Patch / Dipole Antennas, KY-040 (Rotary Encoder turntable), Arduino, MATLAB Polar Plotter.
        
          
        
    - **Description:** Mount custom-soldered 2.4 GHz antennas on a turntable indexed by the KY-040 encoder, measure directional gain and Front-to-Back ratio across 360°, and compare measured polar radiation patterns against Ansys HFSS / NEC2 electromagnetic simulations.
        
          
        
- **79. Discrete Colpitts/Hartley RF Oscillator & Varactor/BJT Frequency Modulator (FM)**
    
      
    - **Stack:** Discrete BJTs, Hand-wound air-core inductors, Capacitors, Reverse-biased LED/Diode used as a Varactor, KY-038 (Mic), LTSpice.
        
          
        
    - **Description:** Exploit the voltage-dependent junction capacitance of a reverse-biased diode/LED to frequency-modulate a discrete VHF/HF Colpitts oscillator with audio from the KY-038 microphone, analyzing phase noise and harmonic spurs in LTSpice.
        
          
        
- **80. Indoor Multipath Localization via Fingerprinting & Extended Kalman Filter (RSSI + Optical + Magnetic)**
    
      
    - **Stack:** ESP32 (Wi-Fi/BLE RSSI), KY-024 (Magnetic anomaly sensing), KY-018 (Luminaires flicker signature), Raspberry Pi, Python (Scikit-Learn).
        
          
        
    - **Description:** Fuse spatially varying indoor magnetic field distortions, LED lighting modulation signatures, and Wi-Fi RSSI using a Particle Filter or k-NN classifier to achieve sub-meter indoor localization without GPS.
        
          
        
- **81. LoRa / Long-Range Chirp Spread Spectrum (CSS) Physical Layer Emulator**
    
      
    - **Stack:** ESP32, KY-005 (IR) or KY-006 (Acoustic), MATLAB.
        
          
        
    - **Description:** Code the mathematical physical layer of LoRa modulation (cyclic shifted up-chirps and down-chirp multiplication followed by FFT peak detection) from scratch in MATLAB and C++, validating processing gain at negative SNR (-10 dB).
        
          
        
- **82. Distributed Consensus Clock Synchronization (Flooding Time Sync Protocol - FTSP)**
    
      
    - **Stack:** 3+ Arduino/ESP32 nodes, KY-008/KY-026 (Optical 1-PPS reference), Logic Analyzer (RPi GPIO), C++.
        
          
        
    - **Description:** Implement linear regression skew and offset estimation across wireless nodes to synchronize local hardware timers, using a Simultaneous Optical Flash (KY-008) detected by photodiodes on all nodes to quantify synchronization jitter down to microseconds.
        
          
        
- **83. Cognitive Radio Dynamic Spectrum Access & Jamming Evasion Simulator**
    
      
    - **Stack:** Two ESP32s, Acoustic/Optical Multi-band Transducers, GNU Radio / Python Reinforcement Learning.
        
          
        
    - **Description:** Train a Q-Learning agent that performs real-time power spectral density sensing across multiple frequency bands, dynamically hopping carrier frequencies whenever a swept-frequency jammer enters its active channel.
        
          
        
- **84. Time-Domain Reflectometry (TDR) Coaxial Cable Fault & Impedance Analyzer**
    
      
    - **Stack:** Fast Schmitt-Trigger / BJT Avalanche Pulse Generator, High-Speed Comparator (or oscilloscope/fast ADC), Coaxial Cable Under Test, KY-013 (Termination load), MATLAB.
        
          
        
    - **Description:** Inject a sub-10-nanosecond rising-edge step pulse into a transmission line, measure the reflected wave timing and polarity for open, short, capacitive, and inductive terminations, and compute the distance to cable faults using velocity factor.
        
          
        

## 8. Thermodynamics, Metrology, Sensor Linearization & Environmental Physics

- **85. Constant-Temperature Hot-Thermistor Anemometer (CTA) for Fluid Velocity**
    
      
    - **Stack:** KY-013 (NTC #1 self-heated at 50mW), KY-028 (NTC #2 ambient cold reference), Discrete Op-Amp Wheatstone Bridge + BJT Current Driver, Arduino, MATLAB.
        
          
        
    - **Description:** Drive an NTC thermistor into self-heating inside an active feedback bridge that maintains its resistance (and thus temperature) constant; measure the required bridge heating voltage and apply King's Law ($P = A + B v^n$) to measure airflow velocity down to centimeters per second.
        
          
        
- **86. Precision Steinhart-Hart 3-Point Calibration & Uncertainty Propagation Metrology**
    
      
    - **Stack:** KY-001 (DS18B20 digital reference), KY-013 & KY-028 (NTC Thermistors), Constant-Current Source, 16-bit Oversampled ADC, Python.
        
          
        
    - **Description:** Calibrate non-linear NTC thermistors across an ice bath, ambient bath, and heated bath against the DS18B20 reference, solving the 3x3 system for Steinhart-Hart coefficients ($A, B, C$) and performing a full GUM (Guide to the Expression of Uncertainty in Measurement) Monte Carlo error analysis.
        
          
        
- **87. Ångström's Method for Measuring Thermal Diffusivity of Metal Rods**
    
      
    - **Stack:** Metal Rod (Copper/Aluminum), Power MOSFET + Heater Resistor at one end, Two Temperature Sensors (KY-001 + KY-013) spaced at distance $L$ along the rod, Arduino, MATLAB.
        
          
        
    - **Description:** Apply a periodic sinusoidal heat wave to one end of a metal bar, measure the amplitude attenuation and phase lag of the thermal wave travelling between the two temperature sensors, and calculate the material's exact thermal diffusivity $\alpha = \frac{k}{\rho c_p}$.
        
          
        
- **88. Psychrometric Chart State Estimator: Wet-Bulb, Dew Point, & Specific Enthalpy**
    
      
    - **Stack:** KY-015 (DHT11), KY-001 (DS18B20 Dry Bulb), KY-013 (NTC wrapped in wet cotton wick with fan airflow = Wet Bulb), ESP32, Python.
        
          
        
    - **Description:** Build a true aspirated psychrometer using dry-bulb and wet-bulb thermistors, apply the Magnus-Tetens and Arden Buck equations to compute vapor pressure, dew point, humidity ratio, and air enthalpy, and use it to correct the hysteresis and drift of the cheap DHT11 sensor via Kalman fusion.
        
          
        
- **89. Stefan-Boltzmann Radiative Heat Transfer & Emissivity Spectrometer**
    
      
    - **Stack:** KY-026 (NIR Photodiode), KY-013 (Contact Thermistor), Heated Matte-Black vs. Polished Metal Surfaces, Chopper Wheel (KY-010 + Motor), Lock-in Amplifier, MATLAB.
        
          
        
    - **Description:** Chop the thermal radiation emitted by heated surfaces of different finishes using a rotating slotted wheel monitored by KY-010, measure the radiative flux with KY-026, and verify the $T^4$ radiation law and surface emissivity ratios.
        
          
        
- **90. Transient Hot-Wire / Hot-Bead Thermal Conductivity Probe for Liquids & Soils**
    
      
    - **Stack:** KY-013 (NTC Thermistor), Precision Constant-Current Source, Differential Op-Amp, Arduino, Python.
        
          
        
    - **Description:** Immerse the thermistor in different liquids or granular media (sand, oil, water), apply a step current pulse, and fit the linear region of temperature vs. $\ln(t)$ to determine the thermal conductivity $k$ of the surrounding medium.
        
          
        
- **91. Optical Nephelometer & Mie Scattering Particulate Matter ($PM_{2.5}/PM_{10}$) Sensor**
    
      
    - **Stack:** KY-008 (650nm Laser), KY-005 (940nm IR LED), KY-026 (Photodiode placed at a 90° and 30° scattering angle inside a dark baffle chamber), High-gain TIA, ESP32, Python.
        
          
        
    - **Description:** Construct a light-trap optical scattering chamber with a small convection heater resistor at the bottom to draw air upward, counting individual dust/smoke particle light-scattering pulses and discriminating particle size via dual-wavelength Mie scattering ratios.
        
          
        
- **92. Allan Variance & Noise Power Spectral Density Characterization of Sensor Arrays**
    
      
    - **Stack:** KY-001, KY-013, KY-018, KY-024, KY-035, Arduino/ESP32, MATLAB.
        
          
        
    - **Description:** Record 24-hour continuous stationary time-series data from every analog and digital sensor in your kit inside a thermally insulated box, and plot log-log Allan Deviation ($\sigma_y(\tau)$) curves to decompose Quantization Noise, Angle/Velocity Random Walk, Bias Instability ($1/f$), and Rate Ramp.
        
          
        
- **93. Speed of Sound vs. Temperature & Humidity Acoustic Thermometer**
    
      
    - **Stack:** KY-006 (Acoustic Pulser), KY-037 (Mic Receiver) separated by a fixed 1.000m invar/PVC rod, KY-001 (DS18B20), KY-015 (DHT11), ESP32 (240MHz cycle counter), Python.
        
          
        
    - **Description:** Measure the acoustic time-of-flight over a fixed path with sub-microsecond precision to derive absolute virtual air temperature $c = 331.3 \sqrt{1 + T/273.15}$ acoustically—achieving zero thermal lag compared to contact thermistors.
        
          
        
- **94. Analog Polynomial Hardware Linearizer for Non-Linear Transducers**
    
      
    - **Stack:** KY-013 (NTC) or KY-018 (LDR), Discrete Analog Multiplier / Log-Antilog BJT Stages, Op-Amps, LTSpice.
        
          
        
    - **Description:** Design a pure analog signal conditioning circuit that implements an inverse mathematical curve in hardware so the output voltage is strictly linear ($10\text{ mV/}^\circ\text{C}$ or $10\text{ mV/Lux}$) prior to digitization.
        
          
        
- **95. Flame Flicker Tomographic Frequency & Radiometric Fire Detector**
    
      
    - **Stack:** KY-026 (NIR Flame Photodiode), KY-018 (Visible LDR), KY-013 (Ambient Temp), ESP32, Python.
        
          
        
    - **Description:** Eliminate false alarms from sunlight and incandescent lamps (which saturate basic KY-026 modules) by analyzing the characteristic 1 Hz – 20 Hz hydrodynamic puffing flicker spectrum of real hydrocarbon flames alongside the NIR-to-Visible irradiance ratio.
        
          
        
- **96. Phase-Change Material (PCM) Latent Heat & Differential Thermal Analysis (DTA) Rig**
    
      
    - **Stack:** Two identical test tubes (Reference water/oil vs. Sample wax/salt hydrate), KY-001 & KY-013 inside each tube, Controlled Heated Bath, Arduino, MATLAB.
        
          
        
    - **Description:** Build a Differential Thermal Analyzer that ramps bath temperature linearly and plots the differential temperature $\Delta T = T_{\text{sample}} - T_{\text{ref}}$ to pinpoint endothermic melting plateaus, supercooling nucleation points, and latent heat of fusion.
        
          
        

## 9. TinyML, Edge AI, Neuromorphic Computing & Anomaly Detection

- **97. Bearing & Rotating Machinery Fault Diagnosis via TinyML on ESP32**
    
      
    - **Stack:** DC/Cooling Fan Motor (with induced imbalance/bearing rub), KY-031 (Piezo Accelerometer), KY-024 (Hall Stray Flux Sensor), KY-037 (Acoustic Mic), ESP32, TensorFlow Lite Micro / Edge Impulse.
        
          
        
    - **Description:** Fuse tri-modal data (vibration, acoustic emission, and motor stray magnetic flux), compute MFCCs and spectral kurtosis on the ESP32, and deploy an int8-quantized 1D-CNN to classify normal operation, rotor imbalance, misalignment, and bearing outer-race faults in real time.
        
          
        
- **98. Neuromorphic Leaky Integrate-and-Fire (LIF) Silicon Neuron & Spike Encoder**
    
      
    - **Stack:** Discrete MOSFETs, Capacitors, Op-Amps/Comparators, KY-018 (Retina photoreceptor proxy) or KY-036 (Tactile receptor), Arduino, Python (Brian2 / SNNTorch).
        
          
        
    - **Description:** Solder a biological neuron circuit on a breadboard that integrates sensor currents onto a membrane capacitor and fires action-potential voltage spikes whose inter-spike interval encodes stimulus intensity, feeding the spike train into a Spiking Neural Network (SNN).
        
          
        
- **99. Non-Intrusive Load Monitoring (NILM) Appliance Disaggregation via Autoencoders**
    
      
    - **Stack:** KY-024 (Linear Hall on main power strip cord), Voltage Sensor, ESP32 (High-speed VI trajectory sampler), Raspberry Pi, PyTorch.
        
          
        
    - **Description:** Sample aggregate current and voltage from a multi-outlet power strip, construct high-frequency V-I Lissajous trajectories and harmonic vectors, and train a Deep Denoising Autoencoder on Raspberry Pi to identify which individual appliances (soldering iron, fan, monitor, charger) are switched on.
        
          
        
- **100. Federated Learning Testbed Across Distributed Edge Microcontrollers**
    
      
    - **Stack:** Multiple ESP32s (client nodes with KY-013, KY-018, KY-037), Raspberry Pi (Central Parameter Server), Python / C++.
        
          
        
    - **Description:** Train local neural network anomaly detectors directly on multiple ESP32 microcontrollers using on-device backpropagation, transmitting only gradient weights over MQTT to the Raspberry Pi for Federated Averaging (`FedAvg`) without ever sharing raw sensor data.
        
          
        
- **101. Physics-Informed Neural Network (PINN) for Thermal & Magnetic Field Extrapolation**
    
      
    - **Stack:** Sparse array of KY-001/KY-013 (Thermal) or KY-024 (Magnetic), Arduino, PC (PyTorch).
        
          
        
    - **Description:** Embed PDE constraints (Fourier's Heat Diffusion equation $\frac{\partial T}{\partial t} = \alpha \nabla^2 T$ or Laplace's equation $\nabla^2 \Phi = 0$) directly into the PyTorch loss function to reconstruct full 2D continuous temperature/magnetic fields from only 3 sparse point sensors.
        
          
        
- **102. Reservoir Computing / Echo State Network (ESN) Using a Physical Nonlinear Optical-Thermal Loop**
    
      
    - **Stack:** KY-008 (Laser) / Heater, KY-018 (LDR) / KY-013 (NTC), Nonlinear Delay Feedback Loop on Arduino, PC (Python).
        
          
        
    - **Description:** Use the intrinsic physical non-linearity and hysteresis of an opto-thermal hardware loop as a physical dynamical "reservoir," training only a simple linear ridge-regression readout layer to perform chaotic Mackey-Glass time-series prediction.
        
          
        
- **103. Keystroke Dynamics Biometric Authentication & Acoustic Keyboard Snooping**
    
      
    - **Stack:** KY-004 (Pushbutton), KY-031 (Piezo Vibration on desk), KY-037 (Mic), ESP32, Python (Scikit-Learn / PyTorch).
        
          
        
    - **Description:** Capture both the mechanical desk shockwave arrival times and acoustic click spectrograms when a user types on a PC keyboard, training a Siamese Neural Network to either authenticate the typist's biometric rhythm or reconstruct typed keys acoustically.
        
          
        
- **104. Reinforcement Learning (DQN / PPO) Hardware Pendulum or Thermal Controller**
    
      
    - **Stack:** Physical Thermal or Motor-Encoder Plant (KY-040 + KY-010 + Motor), Arduino (Hardware Interface), PC (PyTorch Gymnasium custom environment).
        
          
        
    - **Description:** Wrap a real physical breadboard circuit as a custom OpenAI Gymnasium environment via high-speed serial, allowing a Proximal Policy Optimization (PPO) agent on your PC to learn optimal control policies from scratch through live physical interaction.
        
          
        
- **105. Online Concept Drift Detection & Self-Healing Sensor Array**
    
      
    - **Stack:** Redundant Sensor Array (KY-001, KY-013, KY-015, KY-028), Arduino (Fault Injector), Raspberry Pi, Python.
        
          
        
    - **Description:** Intentionally inject sensor degradation faults (bias drift, stuck-at faults, scaling errors) into one sensor and use a Mahalanobis-distance / PCA residual observer to automatically isolate the faulty transducer and reconstruct its missing signal via virtual sensing.
        
          
        
- **106. Edge-AI Optical Gesture & Hand-Pose Recognition Using Sparse IR Photodiode Array**
    
      
    - **Stack:** KY-005 (IR LEDs), KY-026, KY-032, KY-033 (Sparse Photodiode/Reflective Array), ESP32, TensorFlow Lite Micro.
        
          
        
    - **Description:** Arrange multiple infrared emitters and receivers in a cross-grid, capture temporal shadow/reflection profiles at 500 Hz as a hand sweeps overhead, and classify 10 complex 3D hand gestures using a lightweight GRU/LSTM recurrent network on ESP32.
        
          
        
- **107. Compressive Sensing & Sparse Signal Recovery ($L_1$-Minimization) on MCU**
    
      
    - **Stack:** KY-038 (Mic) or KY-039 (PPG), Arduino (Random Sub-Nyquist Timer Trigger), MATLAB / Python (`cvxpy`).
        
          
        
    - **Description:** Sample a sparse periodic physiological or acoustic signal at random intervals well below the Nyquist rate on an resource-constrained Arduino, then perfectly reconstruct the full-bandwidth signal on the PC using Basis Pursuit / Orthogonal Matching Pursuit (OMP).
        
          
        
- **108. TinyML Wake-Word & Acoustic Event Detector with Analog Wake-Up Front-End**
    
      
    - **Stack:** KY-037 (Mic + LM393 comparator wakeup), ESP32 (Deep Sleep uA mode → Active DSP mode), Edge Impulse.
        
          
        
    - **Description:** Configure the ESP32 to remain in microamp deep sleep until the KY-037 hardware comparator triggers an external GPIO wake-up interrupt on sound onset, immediately booting into DMA audio capture and running an int8 Keyword Spotting CNN.
        
          
        

## 10. Hardware Security, Cryptography & Side-Channel Analysis

- **109. Differential & Correlation Power Analysis (DPA/CPA) Side-Channel Attack Lab**
    
      
    - **Stack:** Arduino Uno (Target running AES-128 encryption), $10\,\Omega$ Shunt Resistor in the Arduino's $V_{CC}$ or GND path, Discrete High-Speed AC-Coupled Instrumentation Amp, ESP32/PC Oscilloscope, Python (`ChipWhisperer` algorithms).
        
          
        
    - **Description:** Measure the micro-fluctuations in power consumption across a shunt resistor while the Arduino encrypts thousands of plaintexts, and apply Pearson correlation against a Hamming-Weight power model of the AES S-Box to extract the secret 128-bit cryptographic key in minutes.
        
          
        
- **110. Electromagnetic Fault Injection (EMFI) & Side-Channel Probe on Microcontroller**
    
      
    - **Stack:** KY-024 (Hall Probe) + Hand-wound micro-pickup coil (EM Side-Channel), High-current MOSFET + Mini Ferrite Coil (EM Glitcher), Arduino Target, Python.
        
          
        
    - **Description:** Position a miniature inductive pickup coil directly over the decapsulated or plastic package of an ATmega328P to sniff instruction-dependent electromagnetic emissions, and fire a nanosecond magnetic pulse to skip a password-verification `if` branch (glitch attack).
        
          
        
- **111. Laser Optical Fault Injection (OFI) on Decapsulated Semiconductor / Phototransistor Logic**
    
      
    - **Stack:** KY-008 (650nm Focused Laser Diode + MOSFET nanosecond pulse driver), Discrete Transistor SRAM Cell / Exposed Silicon IC, KY-023 (X-Y stage control), Arduino.
        
          
        
    - **Description:** Build a precision pulsed laser fault-injection rig that fires focused optical pulses onto photosensitive semiconductor junctions to induce Single-Event Upsets (SEUs) and bit-flips in discrete Flip-Flop/SRAM cells.
        
          
        
- **112. Analog/Silicon Physical Unclonable Function (PUF) for Unclonable Device Identity**
    
      
    - **Stack:** Array of tolerances in KY-013/028 (NTCs), KY-018 (LDRs), Discrete Transistor Ring Oscillators, or Arduino SRAM startup states, ESP32, Python.
        
          
        
    - **Description:** Exploit microscopic manufacturing variations in discrete component tolerances and uninitialized SRAM power-up states to generate a cryptographic Challenge-Response Pair (CRP) fingerprint, applying Fuzzy Extractors and Bose-Chaudhuri-Hocquenghem (BCH) error-correcting codes for 100% reproducibility across temperature.
        
          
        
- **113. Hardware True Random Number Generator (TRNG) Using BJT Reverse Avalanche Noise & Chaos**
    
      
    - **Stack:** Two NPN BJTs (Reverse-biased Base-Emitter avalanche breakdown at ~9–12V), Op-Amp Amplifier, KY-018/037 (Secondary environmental entropy), Arduino, NIST SP 800-22 Statistical Test Suite.
        
          
        
    - **Description:** Construct a quantum-mechanical shot/avalanche noise generator using a reverse-biased BJT junction, apply Von Neumann whitening and SHA-256 conditioning, and validate cryptographic randomness against all 15 tests of the NIST SP 800-22 suite.
        
          
        
- **114. Tempest / Van Eck Phreaking: Eavesdropping on Display/Cable EM Emissions**
    
      
    - **Stack:** KY-024 / Inductive Loop Probe + High-Gain RF/VHF Amplifier, KY-026 (High-speed optical display flicker probe), SDR / PC Soundcard, Python.
        
          
        
    - **Description:** Capture unintentional electromagnetic or optical intensity emanations from a monitor or serial data cable and reconstruct the transmitted data frame or image raster using synchronization recovery in Python.
        
          
        
- **115. Acoustic & Thermal Covert Channel Between Processes on a Raspberry Pi**
    
      
    - **Stack:** Raspberry Pi (Multi-core CPU), KY-001 / KY-013 (bonded to CPU heatsink), KY-024 (near RPi voltage regulator inductor), Python.
        
          
        
    - **Description:** Write an unprivileged user-space script on the Raspberry Pi that modulates CPU core utilization in a binary pattern (heating the SoC and modulating regulator inductor whine), and decode the leaked secret data externally using a thermistor on the heatsink or a Hall/coil probe near the power rail.
        
          
        
- **116. Ultrasonic / Optical Sensor Spoofing & Active Defense against Autonomous Systems**
    
      
    - **Stack:** KY-032 (IR Obstacle Sensor), KY-005 (Spoofing IR Transmitter), KY-008 (Blinding Laser), Arduino, MATLAB.
        
          
        
    - **Description:** Demonstrate how autonomous vehicle/robot obstacle sensors (like KY-032) can be spoofed into seeing phantom obstacles or blinded to real obstacles using phase-locked out-of-phase IR injection, then implement randomized pulse-interval authentication to defeat the attack.
        
          
        
- **117. Timing Side-Channel Attack & Constant-Time Firmware Verification**
    
      
    - **Stack:** Arduino (Target), ESP32 (Sub-microsecond hardware timer attacker), Logic Shifter, Python.
        
          
        
    - **Description:** Execute an automated timing attack against a vulnerable string-comparison or RSA modular exponentiation routine running on the Arduino by measuring execution time via GPIO/power drop down to 62.5 ns clock cycles, then rewrite the assembly/C code for strict constant-time execution.
        
          
        
- **118. Hardware Tamper-Detection Mesh with Time-Domain Capacitance & Optical Integrity**
    
      
    - **Stack:** KY-036 (Capacitive mesh monitor), KY-008 + KY-018 (Internal optical scatter enclosure), KY-002 (Vibration), KY-021 (Reed magnetic tamper), Arduino (Battery-backed SRAM zeroization).
        
          
        
    - **Description:** Build a FIPS 140-3 Level 4 style physical security enclosure that monitors changes in enclosure internal optical speckle (KY-008/KY-018), capacitive wire-mesh impedance, and magnetic field intrusion, instantly zeroizing cryptographic keys in RAM within 10 microseconds of physical probing.
        
          
        

## 11. Bare-Metal Embedded Architecture, RTOS & Linux Kernel Engineering

- **119. Custom Linux Kernel Industrial I/O (IIO) Subsystem Driver for Raspberry Pi**
    
      
    - **Stack:** Raspberry Pi, KY-001 (1-Wire), KY-040 (Rotary Encoder), KY-032 (IR), C (Linux Kernel Headers, Device Tree Overlays `.dts`).
        
          
        
    - **Description:** Write a production-grade loadable Linux Kernel Module (`.ko`) and Device Tree Overlay in C that registers KY-series sensors directly into the Linux `/sys/bus/iio/devices` subsystem with hardware interrupt triggers and kernel ring buffers.
        
          
        
- **120. Bare-Metal Cooperative & Preemptive Real-Time Operating System (RTOS) From Scratch on AVR**
    
      
    - **Stack:** Arduino Uno (ATmega328P), KY-040, KY-013, KY-016, AVR-GCC / Inline Assembly (No Arduino IDE libraries).
        
          
        
    - **Description:** Write a preemptive round-robin context-switching scheduler from scratch in C and AVR assembly (saving and restoring all 32 CPU registers `r0–r31`, `SREG`, and the Stack Pointer `SP` inside a `TIMER0_COMPA_vect` naked ISR) to run multiple sensor threads concurrently.
        
          
        
- **121. Zero-CPU-Overhead Peripheral Reflex System via DMA & Hardware Timers**
    
      
    - **Stack:** ESP32 (I2S DMA, RMT, PCNT, LEDC peripherals) or Arduino (Timer1 + ADC Auto-Trigger), KY-038, KY-009.
        
          
        
    - **Description:** Configure a complete signal chain where a hardware timer triggers ADC conversions, DMA moves samples into a ping-pong buffer, and hardware pulse-counter (`PCNT`) / remote-control (`RMT`) peripherals decode/encode protocols while the main CPU cores are stalled or executing heavy math.
        
          
        
- **122. Custom Secure Bootloader with Over-the-Air (OTA) / Optical Firmware Updates**
    
      
    - **Stack:** Arduino Uno (Bootloader section flash programming via `SPM` instruction), ESP32 / Raspberry Pi (Host), KY-008 (Laser) + KY-022/026 (Optical RX).
        
          
        
    - **Description:** Write a custom 512-byte AVR bootloader residing at `0x7E00` that receives new compiled `.hex` application firmware pages over an optical laser/IR link, verifies an HMAC/CRC signature, and self-programs the Flash memory using `boot_page_write()`.
        
          
        
- **123. Hard Real-Time Linux (`PREEMPT_RT`) Jitter Benchmark & Deterministic Control**
    
      
    - **Stack:** Raspberry Pi (compiled with `PREEMPT_RT` kernel patch), Arduino (High-precision pulse timing analyzer), KY-010 (Optical interrupt source), Python/C (`cyclictest`).
        
          
        
    - **Description:** Compile a real-time Linux kernel on the Raspberry Pi, lock memory pages with `mlockall()`, isolate CPU cores (`isolcpus`), and use the Arduino as an external sub-microsecond logic timer to plot interrupt latency histograms under 100% stress load.
        
          
        
- **124. Software-Implemented USB 1.1 / 1-Wire / NEC IR Protocol Analyzer & Bit-Banged Stack**
    
      
    - **Stack:** Arduino / ESP32, KY-001 (Dallas 1-Wire), KY-005 & KY-022 (IR), KY-015 (DHT single-bus), Logic Analyzer GUI (`sigrok` / PulseView on PC).
        
          
        
    - **Description:** Turn the ESP32 into an 8-channel, 20 MHz SUMP-compatible logic analyzer connected to `sigrok`/PulseView on your PC, and write deterministic cycle-counted assembly decoders to dissect setup/hold times and protocol framing violations on 1-Wire and DHT buses.
        
          
        
- **125. Lock-Free Ring Buffers, Priority Inversion Demonstration & Priority Inheritance Mutexes**
    
      
    - **Stack:** ESP32 (Dual-Core FreeRTOS), KY-004 (Button interrupt), KY-016 (RGB Status), KY-040 (Encoder), C++.
        
          
        
    - **Description:** Intentionally engineer a classic Mars Pathfinder Priority Inversion deadlock across three FreeRTOS tasks handling high-, medium-, and low-priority sensors, capture the execution trace in Percepio Tracealyzer / Segger SystemView, and resolve it using Priority Inheritance Mutexes and lock-free atomic ring buffers.
        
          
        
- **126. Dynamic Frequency & Voltage Scaling (DVFS) Energy-Proportional Sensor Node**
    
      
    - **Stack:** Arduino (Clock Prescaler `CLKPR` + Sleep Modes) or ESP32, Shunt Resistor + High-side Op-Amp Current Integrator (Coulomb Counter), KY-Series Sensors.
        
          
        
    - **Description:** Build a hardware Coulomb counter to measure microjoules consumed per sensor transaction, and implement an adaptive DVFS governor that dynamically scales the MCU clock between 125 kHz and 16 MHz based on real-time signal derivative activity.
        
          
        
- **127. Custom Bytecode Virtual Machine (VM) & PLC Ladder-Logic Runtime on Arduino**
    
      
    - **Stack:** Arduino, KY-019 (Relay Output), KY-004/020/021/036 (Digital Inputs), KY-013/024 (Analog Inputs), PC Compiler in Python.
        
          
        
    - **Description:** Design an instruction-set architecture (ISA) and stack-based Virtual Machine in C for the Arduino, paired with a Python compiler on your PC that compiles IEC 61131-3 PLC Ladder Logic or Structured Text into compact bytecode streamed over serial without reflashing the MCU.
        
          
        
- **128. Distributed ROS2 (Robot Operating System) Micro-ROS Hardware Bridge**
    
      
    - **Stack:** ESP32 running `micro-ROS` over Wi-Fi/Serial, Raspberry Pi / PC running ROS2 Jazzy/Humble, RViz2, KY-023, KY-040, KY-032, KY-033.
        
          
        
    - **Description:** Publish KY sensor telemetry as native ROS2 topics (`sensor_msgs/Range`, `sensor_msgs/Joy`, `sensor_msgs/JointState`) from the ESP32 using XRCE-DDS, visualizing transformations (`tf2`) inside RViz2 on your PC.
        
          
        
- **129. Fault-Tolerant Triple Modular Redundancy (TMR) Voting Architecture**
    
      
    - **Stack:** Arduino + ESP8266 + ESP32 (Three heterogeneous processors executing control calculations in parallel), Raspberry Pi (Hardware Voter), KY-024/013.
        
          
        
    - **Description:** Feed identical analog sensor signals to three distinct microcontroller architectures, synchronize their execution frames, and implement an aerospace-grade majority-voting and Byzantine fault detection plane on the Raspberry Pi.
        
          
        
- **130. Cycle-Accurate AVR/RISC-V Emulator & Co-Simulation With Spice**
    
      
    - **Stack:** PC (`simavr` or Verilator + ngspice/LTSpice), Physical Arduino for hardware verification, KY-013, KY-016.
        
          
        
    - **Description:** Link a cycle-accurate instruction-set simulator (`simavr`) directly with an analog SPICE circuit simulator so your compiled C firmware interacts with simulated op-amps and thermistors, comparing the co-simulation waveforms against your physical breadboard.
        
          
        

## 12. Digital Twins, Industrial IoT (IIoT), SCADA & Automated Test Equipment (ATE)

- **131. Automated Semiconductor Curve Tracer & Parameter Extractor ($I_C$-$V_{CE}$, $I_D$-$V_{DS}$, Early Voltage)**
    
      
    - **Stack:** Arduino/ESP32, Dual DACs (or filtered PWM + Op-Amp buffers), Current Sense Amplifiers, KY-013 (Attached to transistor case for thermal derating tests), Python / LabVIEW GUI.
        
          
        
    - **Description:** Build a full PC-controlled Automated Test Equipment (ATE) curve tracer that steps base current $I_B$ (or gate voltage $V_{GS}$) while sweeping collector/drain voltage, automatically plotting family of curves and extracting $\beta_{DC}$, transconductance $g_m$, threshold voltage $V_{th}$, and Early Voltage $V_A$ across temperature.
        
          
        
- **132. Automated Bode Plotter / Vector Network Frequency Response Analyzer (FRA)**
    
      
    - **Stack:** ESP32 (DAC Sine Sweeper + Dual-Channel Simultaneous ADC), Device Under Test (Active Filter / Amplifier), Python / MATLAB GUI.
        
          
        
    - **Description:** Sweep a sinusoidal excitation from 1 Hz to 40 kHz through any analog filter or control circuit, perform digital quadrature cross-correlation at each frequency step to reject harmonics, and automatically plot Magnitude (dB) and Phase (°) Bode plots and Nyquist diagrams.
        
          
        
- **133. Industrial SCADA System with OPC-UA, Modbus RTU/TCP, InfluxDB & Grafana**
    
      
    - **Stack:** Arduino (Modbus RTU Slave over RS-485/UART), ESP32 (Modbus TCP Bridge), Raspberry Pi (OPC-UA Server + InfluxDB + Grafana), KY-019, KY-001, KY-015, KY-024.
        
          
        
    - **Description:** Architect a complete multi-tier industrial automation stack where field sensors on the Arduino communicate via deterministic Modbus RTU registers to an ESP32 gateway, exposing an encrypted OPC-UA address space logged into a time-series database with real-time statistical process control (SPC) alarms.
        
          
        
- **134. Real-Time 3D Physics Digital Twin in MATLAB Simscape / Unity3D**
    
      
    - **Stack:** Physical Mechatronic Assembly (KY-040 Encoder, KY-023 Joystick, KY-020 Tilt, KY-024 Hall, KY-001 Temp), ESP32 (Low-latency WebSockets/UDP), PC (Unity3D or MATLAB Simscape Multibody).
        
          
        
    - **Description:** Synchronize a physical breadboard/mechanical setup with a 3D physics-rendered Digital Twin at 120 Hz, overlaying invisible physical fields (thermal gradients from KY-001/013 and magnetic flux lines from KY-024) as real-time 3D volumetric shaders over the CAD model.
        
          
        
- **135. Automated Battery Management System (BMS) Cyclical Tester & State-of-Charge (SoC) Estimator**
    
      
    - **Stack:** Rechargeable Li-ion / NiMH Cell, MOSFET Programmable Constant-Current Electronic Load & Charger, KY-001/013 (Cell Surface Temp), KY-024 (Hall Current Sensor), KY-019 (Safety Cutoff Relay), ESP32, MATLAB.
        
          
        
    - **Description:** Build a programmable battery cycler that executes Hybrid Pulse Power Characterization (HPPC) tests to identify the Thevenin equivalent circuit parameters ($R_0, R_1, C_1$) of a battery cell, using an Unscented Kalman Filter (UKF) to estimate State of Charge (SoC) and State of Health (SoH).
        
          
        
- **136. Automated Optical & Electrical PCB / Component Quality Assurance Sorting Station**
    
      
    - **Stack:** KY-008 (Laser), KY-018/026 (Optical transmission/reflection), KY-024 (Inductive/Magnetic metal signature), KY-036 (Capacitance), KY-040 (Conveyor indexer), Raspberry Pi (OpenCV), Python.
        
          
        
    - **Description:** Combine computer vision on Raspberry Pi with multi-physics sensor signatures (magnetic permeability, optical reflectivity, capacitance) to automatically classify, test, and reject out-of-spec electronic components on a rotary indexing table.
        
          
        
- **137. Precision LCR Meter Using Phase-Sensitive Auto-Balancing Bridge**
    
      
    - **Stack:** ESP32 / PC Soundcard (Quadrature Sine Generator), Discrete Op-Amp Auto-Balancing Bridge, Precision Reference Resistors, Python GUI.
        
          
        
    - **Description:** Build an auto-balancing impedance bridge that measures the complex voltage and current vectors across unknown inductors, capacitors, and resistors at multiple test frequencies, calculating $L, C, R$, Dissipation Factor ($D$), and Quality Factor ($Q$).
        
          
        
- **138. Hardware-Assisted Monte Carlo Circuit Tolerance & Yield Analyzer**
    
      
    - **Stack:** Analog Filter Circuit with digitally switched resistor/capacitor banks (via MOSFETs/KY-019/Multiplexers), KY-013 (Thermal chamber), Arduino, LTSpice + Python automation.
        
          
        
    - **Description:** Automate LTSpice from Python to run 10,000 Monte Carlo tolerance simulations of an analog circuit, and validate the statistical yield distributions on hardware by thermally stressing the physical breadboard circuit and switching component tolerances dynamically.
        
          
        
- **139. Smart Microgrid Synchronization (Synchroscope) & Islanding Detection Testbed**
    
      
    - **Stack:** Two Independent Oscillators / Inverters (Grid vs. Distributed Generator), Zero-Crossing Phase Comparators, KY-019 (Grid Tie Breaker Relay), KY-011/016 (LED Synchroscope), Arduino, Simulink.
        
          
        
    - **Description:** Build a microgrid grid-tie controller that monitors slip frequency, voltage magnitude difference, and phase angle difference ($\Delta f, \Delta V, \Delta \phi$) between two AC sources, closing the tie relay only at the exact zero-phase synchronization window and implementing Rate-of-Change-of-Frequency (ROCOF) anti-islanding protection.
        
          
        
- **140. High-Speed Stroboscopic Tachometer & Optical Motion Freeze-Frame Imaging System**
    
      
    - **Stack:** KY-009 / High-Power LED + MOSFET Pulse Driver, KY-010 (Optical Interrupter) or KY-037 (Acoustic trigger), KY-040 (Fine phase-angle encoder), Arduino, Rotating Fan/Motor.
        
          
        
    - **Description:** Phase-lock microsecond high-current LED flashes to the rotation frequency of a high-speed blade or vibrating string, using the KY-040 rotary encoder to shift the strobe firing phase angle in 0.5° increments to visually freeze or slow-motion inspect mechanical resonances.
        
          
        
- **141. Multi-Sensor Data Fusion Fire & Hazard Early-Warning Matrix Using Dempster-Shafer Theory**
    
      
    - **Stack:** KY-026 (IR Flame), KY-015 (Humidity), KY-001/013 (Temperature + $dT/dt$), KY-008 + KY-018 (Optical smoke obscuration), ESP32, Python.
        
          
        
    - **Description:** Implement Dempster-Shafer Evidence Theory (belief and plausibility mass functions) across four heterogeneous physical modalities to distinguish true incipient electrical fires from steam, dust, or sunlight with zero false positives.
        
          
        
- **142. Automated PID & Control Loop Frequency-Domain Stability Margin Tester**
    
      
    - **Stack:** Any Closed-Loop Hardware Controller (e.g., MagLev or Thermal Loop), ESP32 (Digital Signal Injector placed inside the feedback loop), MATLAB.
        
          
        
    - **Description:** Break a physical closed-loop control system virtually by summing a swept perturbation signal $d(t)$ into the actuator command and measuring the loop return ratio $L(j\omega)$ while the system remains operating in closed-loop, automatically computing Gain Margin and Phase Margin.
        
          
        
- **143. Sub-Millimeter Laser Triangulation 3D Surface Profilometer & Point-Cloud Scanner**
    
      
    - **Stack:** KY-008 (Laser with cylindrical lens / glass rod to project a laser line), KY-040 (Rotary turntable encoder), Webcam / Raspberry Pi Camera, Python (OpenCV + Open3D).
        
          
        
    - **Description:** Project a structured laser plane across an object mounted on a turntable indexed by the KY-040 encoder, calibrate camera intrinsic/extrinsic matrices, and apply sub-pixel center-of-mass laser stripe extraction to generate a dense 3D `.ply` mesh point cloud.
        
          
        
- **144. End-to-End Custom Mixed-Signal PCB Capstone: From Breadboard Prototype to KiCad 4-Layer Design**
    
      
    - **Stack:** Your top chosen AFE + Sensor + ESP32/Arduino architecture, LTSpice, KiCad, Soldering Iron, Python.
        
          
        
    - **Description:** Take any of the above multi-stage systems, simulate the analog stages in LTSpice, design a 4-layer mixed-signal PCB in KiCad with split analog/digital ground planes, guard rings around high-impedance nodes, impedance-controlled RF traces, and EMI stitching vias, and assemble/validate the final instrument.
        

## Suggested Mastery Progression Roadmap

|**Phase**|**Target Engineering Focus**|**Recommended Starting Projects**|**Primary Software Stack**|
|---|---|---|---|
|**Phase 1: Analog & Physics Foundations**|Op-amp AFEs, noise floors, bridge linearization, transducer physics|**#1** (Lock-in Amp), **#3** (In-Amp Bridge), **#85** (Hot-Thermistor Anemometer), **#86** (Steinhart-Hart)|LTSpice, MATLAB, Python (SciPy)|
|**Phase 2: DSP, Signals & Acoustics**|Sampling theory, adaptive filtering, modulation, array processing|**#13** (Optical OFDM), **#28** (LMS PPG), **#49** (TDOA Beamforming), **#50** (FxLMS ANC)|MATLAB DSP Toolbox, GNU Radio, Python|
|**Phase 3: Control, Power & Electromagnetics**|State-space control, switching converters, magnetic circuits|**#37** (MagLev LQR), **#41** (EKF Fusion), **#61** (Buck Hall Control), **#62** (B-H Curve Tracer)|Simulink, LabVIEW, LTSpice, Ansys|
|**Phase 4: Embedded Systems, AI & Security**|Bare-metal C, Linux kernel drivers, TinyML, side-channel attacks|**#97** (TinyML Bearing Faults), **#109** (AES Power Attack), **#119** (Linux IIO Driver), **#131** (Curve Tracer)|AVR-GCC, FreeRTOS, PyTorch, KiCad|