# QnA: Ultra-Fast VLSI, VHDL, and FPGA

---

### **Ultra-Fast VLSI Circuits and Systems**

#### 1., 2. & 11. "Explain why GaAs technology is faster than Si and Ge ones." / "Precisely explain the reasons for superior electron mobility of GaAs in VLSI technology." (Page 3, Q.8(c); Page 6, Q.6(c); Page 21, Q.8(a))

**Answer:**
GaAs (Gallium Arsenide) is fundamentally faster than Silicon (Si) and Germanium (Ge) due to the following physical properties:
1. **Much Higher Electron Mobility ($\mu_n$):**
   - In GaAs, electron mobility $\mu_n \approx 8500\text{ cm}^2/(\text{V}\cdot\text{s})$, compared to Silicon ($\mu_n \approx 1400\text{ cm}^2/(\text{V}\cdot\text{s})$) and Germanium ($\mu_n \approx 3900\text{ cm}^2/(\text{V}\cdot\text{s})$).
   - This represents a **5 to 6 times higher mobility** than Silicon.
2. **Lower Effective Electron Mass ($m^*$):**
   - The conduction band minimum in GaAs has a very steep parabolic curvature:
     $$m^* \approx 0.067 \, m_0 \quad (\text{GaAs}) \quad \text{vs} \quad m^* \approx 0.26 \, m_0 \quad (\text{Si})$$
   - Since acceleration $a = \frac{qE}{m^*}$ and mobility $\mu = \frac{q\tau_c}{m^*}$, lighter effective mass gives electrons much higher acceleration and drift velocity for the same electric field.
3. **Higher Peak Drift Velocity:**
   - GaAs reaches a peak electron velocity of $\approx 2 \times 10^7\text{ cm/s}$ at a low threshold field ($\approx 3.5\text{ kV/cm}$), compared to Silicon's saturation velocity of $\approx 1 \times 10^7\text{ cm/s}$ at $\approx 20\text{ kV/cm}$.
4. **Semi-Insulating Substrate:**
   - Undoped GaAs acts as a semi-insulating substrate with resistivity $\rho > 10^7 \, \Omega\cdot\text{cm}$, reducing interconnect-to-substrate parasitic capacitances by orders of magnitude compared to Silicon.

---

#### 3. & 6. "Compare the basic properties Si and GaAs semiconductors. Which one is better? Why?" (Page 8, Q.7(b); Page 9, Q.7(b))

**Answer:**
**Property Comparison Table:**

| Property | Silicon (Si) | Gallium Arsenide (GaAs) | Advantage |
| :--- | :--- | :--- | :--- |
| **Bandgap ($E_g$)** | $1.12\text{ eV}$ (Indirect) | $1.42\text{ eV}$ (Direct) | GaAs (Higher temp limit, optical emission) |
| **Electron Mobility ($\mu_n$)** | $\approx 1400\text{ cm}^2/(\text{V}\cdot\text{s})$ | $\approx 8500\text{ cm}^2/(\text{V}\cdot\text{s})$ | GaAs ($5\times$ faster electron speed) |
| **Hole Mobility ($\mu_p$)** | $\approx 450\text{ cm}^2/(\text{V}\cdot\text{s})$ | $\approx 400\text{ cm}^2/(\text{V}\cdot\text{s})$ | Si (Better for PMOS/CMOS complementary pairs) |
| **Native Oxide** | High-quality $\text{SiO}_2$ (stable, insoluble) | No stable native oxide (arsenic evaporates) | Si (Enables easy MOSFET fabrication) |
| **Substrate Resistivity** | Moderate ($\approx 10^3 \, \Omega\cdot\text{cm}$) | Semi-insulating ($> 10^7 \, \Omega\cdot\text{cm}$) | GaAs (Negligible substrate capacitance) |
| **Cost & Wafer Size** | Inexpensive, up to $300\text{ mm}$ wafers | Fragile, toxic, expensive, small wafers ($\le 150\text{ mm}$) | Si (Massive economic advantage) |

**Which is better and why?**
- **Silicon is better for general VLSI / ULSI systems:** Due to low cost, mature fabrication, large mechanical wafer diameter, and superior native oxide ($\text{SiO}_2$) essential for reliable CMOS logic.
- **GaAs is better for ultra-high-speed & RF/Microwave circuits:** Ideal for radar, satellite communication, and optical emitters/detectors where raw electron switching speed ($> 50\text{ GHz}$) and direct bandgap light emission are mandatory.

---

#### 4., 7. & 8. "What is 'doping'? Give a list of the materials used for doping in Si and GaAs. Also justify why these materials are chosen." (Page 8, Q.7(c); Page 9, Q.8(a); Page 11, Q.7(b))

**Answer:**
- **Definition of Doping:**
  - The intentional introduction of tiny amounts of specific impurity atoms into an intrinsic semiconductor crystal to increase its electrical conductivity by creating excess free electrons (n-type) or holes (p-type).
- **Dopants in Silicon (Group IV):**
  - **n-type dopants (Group V):** Phosphorus (P), Arsenic (As), Antimony (Sb).
    - *Justification:* Have 5 valence electrons. 4 bond with Si, the 5th easily ionizes at room temperature to provide conduction electrons.
  - **p-type dopants (Group III):** Boron (B).
    - *Justification:* Has 3 valence electrons. Accepts an electron from the Si lattice, creating mobile holes.
- **Dopants in GaAs (Compound III-V):**
  - **n-type dopants:** Tellurium (Te), Selenium (Se), Silicon (Si on Ga site).
    - *Justification:* Group VI atoms (Te, Se) replace Group V Arsenic, donating an extra electron.
  - **p-type dopants:** Zinc (Zn), Beryllium (Be), Magnesium (Mg), Silicon (Si on As site).
    - *Justification:* Group II atoms (Zn, Be) replace Group III Gallium, acting as acceptors to produce holes.
  - **Amphoteric Dopant (Silicon):** Silicon is a Group IV element; when it occupies a Ga site it acts as a donor (n-type), but on an As site it acts as an acceptor (p-type), controlled by growth temperature and arsenic pressure.

---

#### 5. & 9. "Explain the difference between Elementary semiconductor and Compound semiconductor. Give examples. Why compound semiconductors are getting importance in VLSI technology?" (Page 9, Q.7(a); Page 11, Q.8(b))

**Answer:**
- **Differences:**

| Feature | Elementary Semiconductor | Compound Semiconductor |
| :--- | :--- | :--- |
| **Composition** | Composed of a single chemical element from Group IV | Composed of two or more elements (Groups III-V, II-VI, IV-IV) |
| **Examples** | Silicon (Si), Germanium (Ge) | GaAs, InP, GaN, SiC, InGaAs |
| **Bandgap Nature** | Indirect bandgap (requires phonon for recombination) | Direct bandgap (photon emitted directly on recombination) |
| **Mobility** | Moderate electron mobility | Exceptionally high electron mobility |

- **Why Compound Semiconductors Are Gaining Importance in VLSI:**
  1. **Ultra-High Operating Frequency:** Essential for 5G/6G RF front-ends, radar, and millimeter-wave communication (operates at $> 100\text{ GHz}$).
  2. **Optoelectronics Integration:** Direct bandgap enables monolithic lasers, LEDs, and photodetectors on chips (optical interconnects).
  3. **High Power & Breakdown Fields:** Materials like GaN and SiC tolerate much higher electric breakdown fields and temperatures, ideal for power VLSI and electric vehicle converters.

---

#### 10. "Discuss about the energy band structure of GaAs. What is MESFET?" (Page 19, Q.(c))

![[attachments/gaas_mesfet.png]]

**Answer:**
- **Energy Band Structure of GaAs:**
  - **Direct Bandgap:** The conduction band minimum and valence band maximum occur at the exact same crystal momentum ($k = 0$, the $\Gamma$-point), with an energy gap of $E_g = 1.42\text{ eV}$.
  - **Multi-Valley Conduction Band:**
    - **Central $\Gamma$-Valley:** Light effective mass ($m^* = 0.067 m_0$), extremely high mobility ($\mu_n \approx 8500\text{ cm}^2/\text{V}\cdot\text{s}$).
    - **Satellite $L$-Valleys:** Located $0.31\text{ eV}$ higher, with heavier effective mass ($m^* \approx 0.55 m_0$) and low mobility ($\mu_n \approx 100\text{ cm}^2/\text{V}\cdot\text{s}$).
    - Under strong electric fields ($> 3.5\text{ kV/cm}$), electrons scatter from the high-mobility $\Gamma$-valley into the low-mobility $L$-valley, causing **Negative Differential Mobility (Gunn Effect)** used in microwave oscillators.
- **What is a MESFET (Metal-Semiconductor Field-Effect Transistor)?**
  - A field-effect transistor where a **metallic Schottky barrier contact** replaces the insulated MOS gate oxide.
  - **Structure:** Built on a semi-insulating GaAs substrate with a thin n-type GaAs channel layer, ohmic Source/Drain contacts, and a metal Schottky Gate (Gold/Platinum).
  - **Operation:** Modulating the reverse-bias gate voltage expands or contracts the depletion region under the Schottky barrier, controlling channel current without oxide interface defects.

---

### **Introduction and Application of VHDL**

#### 12., 13. & 19. "Write a VHDL code of full adder circuit. / Derive the truth table and write the corresponding VHDL code." (Page 3, Q.8(b); Page 5, Q.5(c); Page 25, CT-04, Q.4)

**Answer:**
- **Truth Table:**

| $A$ | $B$ | $C_{in}$ | $Sum$ | $C_{out}$ |
| :-: | :-: | :------: | :---: | :-------: |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

- **Boolean Equations:**
  $$Sum = A \oplus B \oplus C_{in}$$
  $$C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$$

- **VHDL Code:**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity full_adder is
    Port ( A, B, Cin : in  STD_LOGIC;
           Sum, Cout : out STD_LOGIC);
end full_adder;

architecture dataflow of full_adder is
begin
    Sum  <= A xor B xor Cin;
    Cout <= (A and B) or (Cin and (A xor B));
end dataflow;
```

---

#### 14. "Write down the VHDL code for 8:1 MUX." (Page 6, Q.6(b))

**Answer:**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux8to1 is
    Port ( D   : in  STD_LOGIC_VECTOR(7 downto 0); -- 8 data inputs
           SEL : in  STD_LOGIC_VECTOR(2 downto 0); -- 3 select lines
           Y   : out STD_LOGIC);
end mux8to1;

architecture behavioral of mux8to1 is
begin
    process(D, SEL)
    begin
        case SEL is
            when "000" => Y <= D(0);
            when "001" => Y <= D(1);
            when "010" => Y <= D(2);
            when "011" => Y <= D(3);
            when "100" => Y <= D(4);
            when "101" => Y <= D(5);
            when "110" => Y <= D(6);
            when "111" => Y <= D(7);
            when others => Y <= '0';
        end case;
    end process;
end behavioral;
```

---

#### 15. & 18. "What are the basic differences between VHDL and Verilog? Design a half adder using the dataflow style of modeling." (Page 12, Q.8(a); Page 25, CT-04, Q.3)

**Answer:**
- **Differences Between VHDL and Verilog:**

| Feature | VHDL | Verilog |
| :--- | :--- | :--- |
| **Origin / Syntax** | Based on Ada; verbose and explicit | Based on C language; compact and concise |
| **Typing System** | **Strongly typed** (strict type conversions required) | **Weakly typed** (automatic type coercion) |
| **Learning Curve** | Steeper learning curve; high syntax overhead | Easier for C programmers to learn quickly |
| **Case Sensitivity**| **Case-insensitive** | **Case-sensitive** |
| **Best Use Case** | Large aerospace, defense, and system-level specs | Commercial ASIC design and quick prototyping |

- **Half Adder (Dataflow Style):**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity half_adder is
    Port ( A, B      : in  STD_LOGIC;
           Sum, Carry : out STD_LOGIC);
end half_adder;

architecture dataflow of half_adder is
begin
    Sum   <= A xor B;
    Carry <= A and B;
end dataflow;
```

---

#### 16. "Write down a VHDL code for half adder circuit." (Page 22, Q.7(a))

**Answer:**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity half_adder is
    Port ( a : in  STD_LOGIC;
           b : in  STD_LOGIC;
           s : out STD_LOGIC;
           c : out STD_LOGIC);
end half_adder;

architecture behavioral of half_adder is
begin
    s <= a xor b;
    c <= a and b;
end behavioral;
```

---

#### 17. "Derive the truth table and write the corresponding VHDL code for a 4×1 MUX using when logic" (Page 24, CT-04, Q.4)

**Answer:**
- **Truth Table:**

| $S_1$ | $S_0$ | Output ($Y$) |
| :---: | :---: | :----------: |
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

- **VHDL Code using `when...else` (Conditional Signal Assignment):**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4to1 is
    Port ( I   : in  STD_LOGIC_VECTOR(3 downto 0);
           SEL : in  STD_LOGIC_VECTOR(1 downto 0);
           Y   : out STD_LOGIC);
end mux4to1;

architecture dataflow of mux4to1 is
begin
    Y <= I(0) when (SEL = "00") else
         I(1) when (SEL = "01") else
         I(2) when (SEL = "10") else
         I(3) when (SEL = "11") else
         '0';
end dataflow;
```

---

#### 20., 21., 22. & 23. "What is HDL test bench? Draw and describe the block diagram of off-line and on-line configuration of HDL test bench." (Page 7, Q.8(a); Page 8, Q.8(b); Page 9, Q.6(b); Page 10, Q.8(b))

**Answer:**
- **What is an HDL Test Bench?**
  - A top-level simulation environment (written in VHDL/Verilog) with no physical I/O ports. It instantiates the **Unit Under Test (UUT)**, applies input test vectors (stimulus), and observes/verifies output waveforms.

- **On-Line Configuration:**
  - The stimulus generator dynamically produces vectors during simulation, and the verifier evaluates responses interactively against golden models.
![[attachments/Pasted image 20260930020128.png]]

- **Off-Line Configuration:**
  - Test vectors and expected golden outputs are prepared in advance and stored in disk files. The testbench reads stimulus from an input file and logs results to an output file.
![[attachments/Pasted image 20260930020210.png]]

---

### **FPGA (Field Programmable Gate Array)**

![[attachments/fpga_architecture.png]]

#### 24. & 25. "Determine the configuration bits of the following circuit. Assume, you have a 2×2 FPGA. / Determine the configuration bits in Fig.8.3 with I/O constraints." (Page 3, Q.8(a); Page 5, Q.8(c))

**Answer:**
- **Configuration Bits in an FPGA:**
  1. **LUT Truth Table Bits:** For a $k$-input Look-Up Table (LUT), $2^k$ SRAM configuration bits store the output column of the truth table.
     - *Example:* A 2-input LUT implementing $Y = A \cdot B$ has configuration bits `0, 0, 0, 1` (stored in SRAM cells 00, 01, 10, 11).
  2. **Interconnect Switch Matrix Bits:** SRAM pass-transistors or multiplexer select bits programmed to connect vertical routing channels to horizontal channels.
  3. **I/O Block (IOB) Bits:** Programmed to configure pad direction (Input, Output, or Tristate) and drive strength.
- **2x2 FPGA Programming Method:**
  - Identify the target logic function for each of the 4 Configurable Logic Blocks (CLBs).
  - Fill the 4-bit truth table entries for each CLB's 2-input LUT.
  - Set switch box pass-transistor bits (1 = closed switch, 0 = open) to route inputs from chip boundary pins to CLB inputs, and CLB outputs to designated output pins.

---

#### 26. "What is FPGA? Draw and explain the basic structure of FPGA." (Page 13, Q.8(a))

**Answer:**
- **What is an FPGA?**
  - A Field Programmable Gate Array is an integrated circuit designed to be configured by a customer or designer after manufacturing using Hardware Description Languages (VHDL/Verilog).
- **Basic Internal Architecture:**
  1. **Configurable Logic Blocks (CLBs):**
     - The functional logic core. Each CLB contains:
       - **LUTs (Look-Up Tables):** SRAM-based memories implementing arbitrary $k$-input truth tables.
       - **Flip-Flops / Latches:** For registering sequential states.
       - **Multiplexers & Carry Chains:** For arithmetic acceleration.
  2. **Programmable Interconnects:**
     - Horizontal and vertical wiring channels with **Switch Boxes (SBs)** and **Connection Boxes (CBs)** containing programmable pass-transistors to route signals between any two CLBs.
  3. **I/O Blocks (IOBs):**
     - Perimeter interface pads configured as inputs, outputs, or bidirectional pins with programmable voltage thresholds and pull-up/pull-down resistors.
