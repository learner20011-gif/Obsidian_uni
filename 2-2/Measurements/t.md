### **Core Topics in the L05 Lecture PDF**

The lecture slide document **"L05_EEE_2211_Instrumentation_ak.pdf"** introduces the syllabus topic of **Instrumentation** under the name **Chapter Name: Instrument Transformer**, designed to accompany the textbook **A.K. Sawhney**. The core topics covered in this lecture include:

1. **Introduction to Instrument Transformers**:
    - Definition of **Instrument Transformers** as transformers used in conjunction with measuring instruments.
    - Distinction between **Current Transformers (C.T.)** (used for current measurement) and **Voltage/Potential Transformers (P.T.)** (used for voltage measurement).
2. **Use of Instrument Transformers**:
    - Why they are essential: Stepping down very large alternating currents and high voltages to safe, moderate standard levels (standardized at **5 A** for C.T. secondaries and **100 V to 120 V** for P.T. secondaries).
    - Benefits: Safety, electrical isolation, and permitting the use of standard, inexpensive instruments of moderate size.
3. **Burden of Instrument Transformers**:
    - Definition of **Burden**: Expressing the load across secondary terminals as the volt-ampere (VA) output at the rated secondary voltage.
    - Definition of **Rated Burden**: The volt-ampere loading permissible without exceeding the errors allowed for a specific accuracy class.
    - Mathematical formulas for **Total Secondary Burden** (including secondary winding impedance) and **Secondary Burden due to load**.
4. **Current Transformers (C.T.) Theory & Relationships**:
    - Equivalent circuit diagram of a C.T.
    - Phasor diagram under inductive/resistive loads
    - Derivation of the **Transformation Ratio (\(R\))**: \[R = n + \frac{I_0}{I_s}\sin(\delta + \alpha) = n + \frac{I_m\sin\delta + I_e\cos\delta}{I_s}\]
    - Derivation of the **Phase Angle (\(\theta\))**: \[\theta \approx \frac{180}{\pi} \left[ \frac{I_m\cos\delta - I_e\sin\delta}{n I_s} \right] \text{ degrees}\]
5. **Errors in C.T. and P.T.**:
    - **Ratio Error**: Introduced because the actual transformation ratio differs from the turns ratio (\(n\)).
    - **Phase Angle Error**: Introduced because the secondary current is not exactly \(180^\circ\) out of phase with the primary current.
    - Approximate error formulas when the instrument burden is largely resistive (\(\sin\delta \approx 0\) and \(\cos\delta \approx 1\)): \[R \approx n + \frac{I_e}{I_s} \quad \text{and} \quad \theta \approx \frac{180}{\pi}\left[\frac{I_m}{n I_s}\right] \text{ degrees}\]
6. **Safety Precaution (Secondary Open Circuit of a C.T.)**:
    - Critical warning of **why the secondary of a C.T. must never be open-circuited** while the primary carries current.
    - Explanation: If open-circuited, opposing secondary mmf reduces to zero while primary mmf remains the same. This forces all of primary current to act as exciting current, producing a dangerously high core flux density. This results in massive core heating, dangerous high voltages across secondary terminals, and permanent magnetization of the core (which severely degrades ratio and phase errors).

---

### **Related Solved Examples from A.K. Sawhney Book (Chapter 9)**

All solved examples under **Chapter 9: Instrument Transformers** in A.K. Sawhney's book directly relate to the lecture topics above:

#### **Example 9.1**

- **Problem**: A C.T. has a single-turn primary and a 200-turn secondary winding. The secondary supplies a current of 5 A to a non-inductive burden of \(1\ \Omega\) resistance. The requisite flux is set up in the core by an mmf of 80 AT. Frequency is 50 Hz and core area is \(1000\ \text{mm}^2\). Calculate the ratio and phase angle, and the flux density in the core. Neglect magnetic leakage, iron losses, and copper losses.
- **Solution Summary**:
    - Since secondary leakage and iron losses are neglected, secondary burden phase angle \(\delta = 0^\circ\) and loss current component \(I_e = 0\).
    - Magnetizing current \(I_m = \frac{80\text{ AT}}{1\text{ turn}} = 80\ \text{A}\).
    - Reflected secondary current \(n I_s = 200 \times 5 = 1000\ \text{A}\).
    - Primary current \(I_p = \sqrt{(n I_s)^2 + I_m^2} = \sqrt{1000^2 + 80^2} = 1003.2\ \text{A}\).
    - **Actual transformation ratio (\(R\))** \(= \frac{1003.2}{5} =\) **\(200.64\)**.
    - **Phase angle (\(\theta\))** \(= \tan^{-1}\left(\frac{I_m}{n I_s}\right) = \tan^{-1}\left(\frac{80}{1000}\right) \approx\) **\(4^\circ 35'\)**.
    - **Maximum flux density (\(B_m\))** \(=\) **\(0.1125\ \text{Wb/m}^2\)**.

#### **Example 9.2**

- **Problem**: The magnetizing current of a ring-core current transformer of ratio 1000/5 A, when operating at full primary current and with a secondary burden of non-inductive resistance of \(1\ \Omega\) is 1 A at a power factor of 0.4. (Calculates actual ratio and phase angle).
- **Key Results**:
    - **Actual Ratio (\(R\))** \(=\) **\(200.08\)**
    - **Ratio Error** \(=\) **\(-0.04%\)**
    - **Phase Angle (\(\theta\))** \(=\) **\(3^\circ 9'\) (or \(0.0525^\circ\))**.

#### **Example 9.3**

- **Problem**: A 1000/5 A, 50 Hz C.T. has a secondary burden comprising a non-inductive burden of \(1.6\ \Omega\). The primary winding has one turn. Calculate the flux in the core and ratio error at full load. Neglect leakage reactance and assume core iron loss to be 1.5 W at full load.
- **Solution Summary**:
    - Secondary induced voltage \(E_s = 5 \times 1.6 = 8\ \text{V}\). Since \(n = 200\), primary induced voltage \(E_p = \frac{E_s}{n} = 0.04\ \text{V}\).
    - Loss current component \(I_e = \frac{\text{Iron Loss}}{E_p} = \frac{1.5}{0.04} = 37.5\ \text{A}\). Magnetizing component \(I_m = 0\) (no data given).
    - **Flux in the core (\(\Phi_m\))** \(=\) **\(0.18 \times 10^{-3}\ \text{Wb}\)**.
    - **Actual Ratio (\(R\))** \(= 200 + \frac{37.5}{5} =\) **\(207.5\)**.
    - **Ratio Error** \(=\) **\(-3.61%\)**.

#### **Example 9.4**

- **Problem**: A current transformer with a bar primary has 300 turns in its secondary winding. The resistance and reactance of the secondary circuit are \(1.5\ \Omega\) and \(1.0\ \Omega\) respectively (including secondary winding). With 5 A flowing in the secondary, the magnetizing mmf is 100 AT and iron loss is 1.2 W. Determine the ratio and phase angle errors.
- **Key Results**:
    - Turns ratio \(n = 300\), secondary burden phase angle \(\delta = 33^\circ 41'\).
    - Core loss component \(I_e = 40\ \text{A}\), magnetizing component \(I_m = 100\ \text{A}\).
    - **Actual Ratio (\(R\))** \(=\) **\(317.7\)**.
    - **Ratio Error** \(=\) **\(-5.57%\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(1.8^\circ\) (or \(1^\circ 48'\))**.

#### **Example 9.5**

- **Problem**: A C.T. has a bar primary and 200 secondary turns. Secondary burden is an ammeter of resistance \(1\ \Omega\) and reactance \(0.5\ \Omega\). Secondary winding has resistance \(0.2\ \Omega\) and reactance \(0.3\ \Omega\). Core requires equivalent of 100 AT for magnetization and 50 AT for core loss.
    - (i) Find primary current and ratio error when secondary indicates 5 A.
    - (ii) By how many turns could the secondary winding be reduced to make the ratio error zero?
- **Key Results**:
    - Total secondary circuit resistance \(R = 1.2\ \Omega\), reactance \(X = 0.8\ \Omega\), giving \(\delta = 33^\circ 41'\).
    - Primary current magnetizing component \(I_m = 100\ \text{A}\), loss component \(I_e = 50\ \text{A}\).
    - **Primary Current (\(I_p\))** \(=\) **\(1093\ \text{A}\)**.
    - **Ratio Error** \(=\) **\(-8.5%\)**.
    - **Turns reduction required** \(=\) **\(19\) turns** (reducing secondary turns to 181).

#### **Example 9.6**

- **Problem**: The primary exciting current of a C.T. with a bar primary, nominal ratio 100/1 A, operating on an external non-inductive burden of \(1.6\ \Omega\) (secondary winding resistance being \(0.2\ \Omega\)) is 1.9 A, lagging \(40.6^\circ\) to the secondary voltage reversed. Secondary turns \(= 100\). With 1 A in secondary, calculate (i) actual ratio, and (ii) phase angle in minutes.
- **Key Results**:
    - **Actual Ratio (\(R\))** \(=\) **\(101.44\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(42^\circ 5'\) (or \(0.708^\circ\))**.

#### **Example 9.7**

- **Problem**: A 1000/5 A, 50 Hz current transformer has a bar primary and a rated secondary burden of 12.5 VA. The secondary winding has 196 turns and a leakage inductance of 0.96 mH. With a purely resistive burden at rated full load, the magnetization mmf is 16 A and the loss excitation requires 12 A. Find the ratio and phase angle errors.
- **Key Results**:
    - Total secondary impedance \(Z = 0.583\ \Omega\) (with \(R = 0.5\ \Omega\) and \(X = 0.3\ \Omega\)), giving \(\delta = 31^\circ\).
    - Magnetizing current \(I_m = 16\ \text{A}\), loss current \(I_e = 12\ \text{A}\).
    - **Actual Ratio (\(R\))** \(=\) **\(199.72\)**.
    - **Ratio Error** \(=\) **\(+0.14%\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(0.274^\circ\) (or \(16.4'\))**.

#### **Example 9.8**

- **Problem**: A C.T. with nominal ratio 1000/5 A has turns ratio \(n = 199\). Magnetizing current \(I_m = 7\ \text{A}\), loss component \(I_e = 4\ \text{A}\). For a secondary burden power factor of \(0.8\) lagging and \(0.8\) leading, calculate ratio error and phase angle.
- **Key Results**:
    - **For \(0.8\) lagging power factor**:
        - **Actual Ratio (\(R\))** \(=\) **\(200.48\)**.
        - **Ratio Error** \(=\) **\(-0.24%\)**.
        - **Phase Angle (\(\theta\))** \(=\) **\(+11'\) (or \(+0.185^\circ\))**.
    - **For \(0.8\) leading power factor**:
        - **Actual Ratio (\(R\))** \(=\) **\(198.8\)**.
        - **Ratio Error** \(=\) **\(+0.603%\)**.
        - **Phase Angle (\(\theta\))** \(=\) **\(+27.6'\) (or \(0.46^\circ\))**.

#### **Example 9.9**

- **Problem**: A current transformer having a 1-turn primary is rated at 500/5 A, 50 Hz with an output of 15 VA. At rated load with non-inductive burden, the in-phase and quadrature components (referred to flux) of exciting mmf are 8 A and 10 A respectively. Secondary turns \(= 98\). Secondary winding resistance is \(0.35\ \Omega\) and leakage reactance is \(0.3\ \Omega\). Calculate actual ratio, ratio error, and phase angle.
- **Key Results**:
    - Total secondary circuit resistance \(= 0.95\ \Omega\) and reactance \(= 0.3\ \Omega\), giving \(\delta = 17.5^\circ\).
    - Exciting components: \(I_e = 10\ \text{A}\), \(I_m = 8\ \text{A}\).
    - **Actual Ratio (\(R\))** \(=\) **\(100.38\)**.
    - **Ratio Error** \(=\) **\(-0.38%\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(0.537^\circ\)**.

#### **Example 9.10**

- **Problem**: At its rated load of 25 VA, a 100/5 A current transformer has an iron loss of 0.2 W and a magnetizing current of 1.5 A. Calculate its ratio error and phase angle when supplying rated output to a meter having a ratio of resistance to reactance of 5.
- **Key Results**:
    - Induced secondary voltage \(E_s \approx V_s = 5\ \text{V}\).
    - Core loss component \(I_e = \frac{0.2\text{ W}}{0.25\text{ V}} = 0.8\ \text{A}\). Magnetizing current \(I_m = 1.5\ \text{A}\).
    - **Ratio Error** \(=\) **\(-2.2%\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(0.73^\circ\) (or \(44'\))**.

#### **Example 9.11**

- **Problem**: The resistance and leakage reactance of the secondary winding of a 500/5 A current transformer are \(0.02\ \Omega\) and \(0.03\ \Omega\) respectively. Magnetization characteristics are provided as a table of secondary induced EMF (\(E_s\)) versus primary magnetizing (\(I_m\)) and core loss (\(I_e\)) currents. An ammeter (resistance \(0.04\ \Omega\), reactance \(0.06\ \Omega\)) and a wattmeter current coil (resistance \(0.06\ \Omega\), reactance \(0.08\ \Omega\)) are connected in series with the secondary. Calculate the ratio and phase angle errors of the C.T. at 5 A secondary current with no turns compensation, and find the turns ratio required to minimize ratio error.
- **Key Results**:
    - Total secondary circuit resistance \(= 0.12\ \Omega\), reactance \(= 0.12\ \Omega\), giving \(\delta = 45^\circ\). Total secondary impedance \(= 0.17\ \Omega\), giving secondary induced EMF \(E_s = 5 \times 0.17 = 0.85\ \text{V}\).
    - Interpolated exciting components: \(I_e = 2.4\ \text{A}\), \(I_m = 2.26\ \text{A}\).
    - **Actual Ratio (\(R\))** \(=\) **\(100.66\)**.
    - **Ratio Error** \(=\) **\(-0.66%\)**.
    - **Phase Angle (\(\theta\))** \(=\) **\(0.378^\circ\) (or \(22.7'\))**.
    - **Turns ratio to minimize ratio error** \(=\) **\(99.34\)** (equivalent to 198.7 turns).

#### **Example 9.12**

- **Problem**: The range of a thermocouple instrument is extended by an iron-cored current transformer. Calculate the value of secondary winding current if the primary current is \(500\ \mu\text{A}\), the primary, secondary, and mutual inductances are 50, 500, and \(100\ \mu\text{H}\) respectively. Frequency is 1 MHz and secondary circuit resistance is \(50\ \Omega\).
- **Key Results**:
    - Secondary quality factor \(Q_s = \frac{\omega L_s}{R_s} = 20\pi \approx 62.8\).
    - Since \(1/Q_s^2 \ll 1\), current ratio \(R \approx \frac{L_s}{M} = \frac{500}{100} = 5\).
    - **Secondary Current (\(I_s\))** \(=\) **\(100\ \mu\text{A}\)**.

#### **Example 9.13**

- **Problem**: A potential transformer, ratio 1000/100 V, has the following constants: Primary resistance \(= 94.5\ \Omega\); Secondary resistance \(= 0.86\ \Omega\); Primary reactance \(= 66.2\ \Omega\); Total equivalent reactance referred to primary side \(= 110\ \Omega\); Magnetizing current \(= 0.02\ \text{A}\) at 0.4 power factor. Calculate: (i) phase angle error at no load, (ii) load in VA at unity power factor at which the phase angle will be zero.
- **Key Results**:
    - At no load (\(I_s = 0\)), \(I_e = 0.008\ \text{A}\), \(I_m = 0.01834\ \text{A}\).
    - (i) **Phase Angle at No-Load (\(\theta\))** \(=\) **\(-4.1'\)**.
    - (ii) **Zero Phase Angle Load** \(=\) **\(10.9\ \text{VA}\)**.

#### **Example 9.14**

- **Problem**: A potential transformer rated 6900/115 V has 22,500 turns in the primary winding and 375 turns in the secondary winding. With 6900 V applied to primary and secondary open-circuited, primary current is 0.005 A lagging the voltage by \(73.7^\circ\). With a particular burden, primary current is 0.0125 A, lagging primary voltage by \(53.1^\circ\). Calculate (i) secondary terminal voltage, (ii) actual ratio, and (iii) the primary turns reduction required to make actual ratio equal to nominal.
- **Key Results**:
    - (i) **Secondary Voltage (\(V_s\))** \(=\) **\(114.49\ \text{V}\)** (lagging primary voltage reversed by \(0.09^\circ\)).
    - (ii) **Actual Ratio (\(R\))** \(=\) **\(60.27\)**.
    - (iii) **Primary turns reduction** \(=\) **\(101\) turns** (new primary turns \(= 22,399\)).

#### **Example 9.15**

- **Problem**: Two current transformers of the same nominal ratio 500/5 A are tested by Silsbee's method. With the secondary current of the standard C.T. adjusted to rated value, the current in the middle conductor is \(\Delta I = 0.05 e^{-j126.9^\circ}\ \text{A}\) referred to standard secondary current. Standard C.T. has RCF \(= 1.0015\) and phase error \(+8'\). Find the RCF and phase angle of the test transformer.
- **Key Results**:
    - Standard actual ratio \(R_s = 100.15\).
    - **RCF of test transformer** \(=\) **\(0.9955\)**.
    - **Phase angle of test transformer (\(\theta_x\))** \(=\) **\(+35.3'\)**.

#### **Example 9.16**

- **Problem**: A P.T. of nominal ratio 24,000/120 V is tested by comparison with a calibrated P.T. of the same ratio. Standard P.T. has RCF \(= 0.9985\) and phase error \(+12'\). The secondary difference voltage is \(0.5 \angle 216.9^\circ\ \text{V}\) with respect to standard secondary voltage. Compute the RCF and phase angle of the test P.T..
- **Key Results**:
    - **RCF of test transformer** \(=\) **\(1.0018\)**.
    - **Phase angle of test transformer (\(\theta_x\))** \(=\) **\(-20.6'\)**.

---

### **Related Unsolved Problems from A.K. Sawhney Book (Chapter 9)**

The following unsolved problems from the book correspond directly to the topics in C.T. and P.T. analysis, errors, and burden calculation:

- **Problem 9.1**: A ring-core current transformer with a nominal ratio of 500/5 A and a bar primary has a secondary resistance of \(0.5\ \Omega\) and negligible secondary reactance. The resultant of magnetizing and iron loss components of the primary current associated with a full-load secondary current of 5 A in a burden of \(1.0\ \Omega\) (non-inductive) is 3 A at a power factor of 0.4. Calculate the true ratio and the phase angle error of the transformer on full load. Calculate also the total flux in the core assuming a frequency of 50 Hz.
    - **[Ans: \(100.24\); \(0.314^\circ\); \(3.37 \times 10^{-4}\ \text{Wb}\)]**.
- **Problem 9.2**: An 8/1 current transformer has an accurate current ratio when the secondary is short-circuited. The inductance of secondary is 60 mH and its resistance is \(0.5\ \Omega\), and the frequency is 50 Hz. Estimate the current ratio and phase angle error when the instrument load resistance is \(0.4\ \Omega\) and inductance is 0.7 mH. Assume no iron loss and magnetizing current equal to 1 percent of primary current. The permeability remains constant.
    - **[Ans: \(8.001\); \(0.2^\circ\)]**.
- **Problem 9.3**: A current transformer with 5 primary turns has a secondary burden consisting of a resistance of \(0.16\ \Omega\) and an inductive reactance of \(0.12\ \Omega\). When the primary current is 200 A, the magnetizing current is 1.5 A and the iron loss current is 0.4 A. Determine any expressions used, the number of secondary turns needed to make the current ratio 100.1, and also the phase angle under these conditions.
    - **[Ans: \(49.7\) turns; \(0.275^\circ\)]**.
- **Problem 9.4**: A current transformer of nominal ratio 1000/5 A is operating with total secondary impedance of \(0.4 + j0.3\ \Omega\). At rated current, the components of primary current associated with core-magnetizing and core loss effects are respectively 6 A and 1.5 A. The primary has 4 turns. Calculate the ratio error and phase angle at rated primary current if the secondary has (a) 800 turns, (b) 795 turns.
    - **[Ans: (a) \(-0.48%\); \(13'\), (b) \(+0.14%\); \(13'\)]**.
- **Problem 9.5**: A bar-type current transformer of toroidal construction requires 400 A to magnetize it, and 300 A to supply the iron loss for each volt per turn induced in the secondary winding at rated frequency. Across the secondary terminal is connected an impedance of \(2\ \Omega\) with a phase angle \(\Delta\), and the resistance of secondary winding is \(0.5\ \Omega\). The nominal ratio is 1000/5 A, and it is required to minimize both ratio and phase errors. Determine the necessary values of secondary turns and phase angle \(\Delta\).
    - **[Ans: \(194\) turns; \(64^\circ 40'\)]**.
- **Problem 9.6**: The resistance and reactance of the secondary of a 500/5 A current transformer are \(0.02\ \Omega\) and \(0.03\ \Omega\) respectively, and the transformer characteristics are given as a function of secondary emf. An ammeter, a wattmeter current coil, and an induction relay are connected in series. Calculate the ratio and phase angle error (a) when all instruments are in circuit, (b) when only the wattmeter is in circuit. Calculate the load VA in each case.
    - **[Ans: (a) \(1.4%\), \(1.25'\), \(64\ \text{VA}\); (b) \(-0.601%\), \(2.5'\), \(1.96\ \text{VA}\)]**.
- **Problem 9.7**: A single-phase potential transformer has a turns ratio of 3810/63. The nominal secondary voltage is 63 V and the total equivalent resistance and leakage reactance referred to the secondary side are \(2\ \Omega\) and \(1\ \Omega\) respectively. Calculate the ratio and phase angle errors when the transformer is supplying a burden of \(100 + j200\ \Omega\). State the assumptions made.
    - **[Ans: \(-0.80%\); \(-0.338^\circ\)]**.
- **Problem 9.8**: A 500/100 V potential transformer has the following constants: Primary resistance \(= 47.25\ \Omega\); Secondary resistance \(= 0.43\ \Omega\); Primary reactance \(= 33.1\ \Omega\); Secondary reactance is negligible; no-load primary current \(= 0.1\ \text{A}\) at 0.6 p.f. Calculate (a) the no-load angle between primary and reversed secondary voltages, (b) the value of secondary current at unity p.f. when the phase angle is zero.
    - **[Ans: (a) \(12^\circ 20'\), (b) \(0.0271\ \text{A}\)]**.

---

💡 **Next Step**: Would you like me to create a structured study report covering the step-by-step derivations for C.T. ratio and phase angle errors, or would you prefer a practice quiz based on these exact Chapter 9 numerical problems?