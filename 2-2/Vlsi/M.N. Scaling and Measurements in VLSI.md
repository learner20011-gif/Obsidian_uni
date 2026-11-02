# Topic 2: Measurements + Scaling
---
## 2A. Inverter Delay, Pull-Up/Pull-Down Ratio & Power Dissipation
### 1. Pull-Up to Pull-Down Ratio ($Z_{pu} / Z_{pd}$)
![[Pasted image 20261102210244.png|370]]
#### Case I: nMOS Inverter Driven Directly by Another nMOS Inverter
![[Pasted image 20261102210349.png]]
- **General Saturation Current:**
    

$$I_{ds} = K \frac{W}{L} \frac{(V_{gs} - V_t)^2}{2}$$

- **Depletion Pull-Up ($V_{gs} = 0$):**
    

$$I_{ds} = K \frac{W_{p.u.}}{L_{p.u.}} \frac{(-V_{td})^2}{2}$$

- **Enhancement Pull-Down ($V_{gs} = V_{inv}$):**
    

$$I_{ds} = K \frac{W_{p.d.}}{L_{p.d.}} \frac{(V_{inv} - V_t)^2}{2}$$

- **Equate Currents ($I_{p.u.} = I_{p.d.}$):**
    

$$\frac{W_{p.d.}}{L_{p.d.}} (V_{inv} - V_t)^2 = \frac{W_{p.u.}}{L_{p.u.}} (-V_{td})^2$$

- **Substitute Aspect Ratios ($Z = \frac{L}{W}$):**
    

$$\frac{1}{Z_{p.d.}} (V_{inv} - V_t)^2 = \frac{1}{Z_{p.u.}} (-V_{td})^2$$

- **Take Square Root:**
    

$$V_{inv} - V_t = \frac{-V_{td}}{\sqrt{Z_{p.u.} / Z_{p.d.}}}$$

- **Rearrange for $V_{inv}$:**
    

$$V_{inv} = V_t - \frac{V_{td}}{\sqrt{Z_{p.u.} / Z_{p.d.}}}$$

- **Substitute Standard Values ($V_t = 0.2 V_{DD}$, $V_{td} = -0.6 V_{DD}$, $V_{inv} = 0.5 V_{DD}$):**
    

$$0.5 = 0.2 + \frac{0.6}{\sqrt{Z_{p.u.} / Z_{p.d.}}}$$

$$0.3 = \frac{0.6}{\sqrt{Z_{p.u.} / Z_{p.d.}}}$$

$$\sqrt{\frac{Z_{p.u.}}{Z_{p.d.}}} = \frac{0.6}{0.3} = 2$$

- **Final Ratio:**
    

$$\frac{Z_{p.u.}}{Z_{p.d.}} = 2^2 = \frac{4}{1}$$
$$\mathbf{\frac{Z_{pu}}{Z_{pd}} = \frac{L_{pu}/W_{pu}}{L_{pd}/W_{pd}} = 4:1} \quad (\text{Direct Inverter Drive})$$
---
#### Case II: nMOS Inverter Driven Through One or More Pass Transistors
![[Pasted image 20261102205256.png]]

- **Input Voltages:**
    
    - Inverter 1: $V_{in1} = V_{DD}$
        
    - Inverter 2: $V_{in2} = V_{DD} - V_{tp}$
        
- **Pull-Down Resistance (Linear Region):**
    
- Inverter 1:
        

$$R_1 \approx \frac{1}{K} Z_{p.d.1} \left(\frac{1}{V_{DD} - V_t}\right)$$

- Inverter 2:
    

$$R_2 \approx \frac{1}{K} Z_{p.d.2} \left(\frac{1}{V_{DD} - V_{tp} - V_t}\right)$$

- **Pull-Up Current (Saturation Region):**
    

$$I_1 = K \frac{1}{Z_{p.u.1}} \frac{(-V_{td})^2}{2}$$

$$I_2 = K \frac{1}{Z_{p.u.2}} \frac{(-V_{td})^2}{2}$$

- **Output Voltages ($V_{out} = I \cdot R$):**
    

$$V_{out1} = I_1 R_1 = \frac{Z_{p.d.1}}{Z_{p.u.1}} \left(\frac{1}{V_{DD} - V_t}\right) \frac{(-V_{td})^2}{2}$$

$$V_{out2} = I_2 R_2 = \frac{Z_{p.d.2}}{Z_{p.u.2}} \left(\frac{1}{V_{DD} - V_{tp} - V_t}\right) \frac{(-V_{td})^2}{2}$$

- **Equate Output Voltages ($V_{out1} = V_{out2}$):**
    

$$\frac{Z_{p.d.1}}{Z_{p.u.1} (V_{DD} - V_t)} = \frac{Z_{p.d.2}}{Z_{p.u.2} (V_{DD} - V_{tp} - V_t)}$$

- **Rearrange for the Second Inverter Ratio:**
    

$$\frac{Z_{p.u.2}}{Z_{p.d.2}} = \frac{Z_{p.u.1}}{Z_{p.d.1}} \frac{(V_{DD} - V_t)}{(V_{DD} - V_{tp} - V_t)}$$

- **Substitute Standard Values ($V_t = 0.2 V_{DD}$, $V_{tp} = 0.3 V_{DD}$, $\frac{Z_{p.u.1}}{Z_{p.d.1}} = 4$):**
    

$$\frac{V_{DD} - 0.2 V_{DD}}{V_{DD} - 0.3 V_{DD} - 0.2 V_{DD}} = \frac{0.8 V_{DD}}{0.5 V_{DD}} = 1.6 \approx 2$$

- **Final Ratio:**
    

$$\frac{Z_{p.u.2}}{Z_{p.d.2}} = 2 \times \frac{Z_{p.u.1}}{Z_{p.d.1}} = 2 \times 4 = \frac{8}{1}$$
---
#### Case III: Pseudo-nMOS Inverter Ratio
![[Pasted image 20261102212220.png]]
- **Structure:** pMOS pull-up with gate permanently tied to $GND$ ($V_{gs} = -V_{DD}$); nMOS pull-down.
- **Mobility Difference:** $\mu_n \approx 2.5 \mu_p \to$ pMOS delivers less current per square than nMOS.
- **Ratio:** To ensure low $V_{OL} \le 0.1 V_{DD}$:
$$\mathbf{\frac{Z_{pu}}{Z_{pd}} \approx 3:1 \text{ to } 4:1}$$
- **Power vs. Delay Comparison (Pseudo-nMOS vs. 4:1 Depletion nMOS):**
  - **Power Dissipation:** Higher in pseudo-nMOS because pMOS pull-up stays strongly ON ($V_{gs} = -V_{DD}$) during LOW output, causing large continuous static DC power.
  - **Inverter Delay:** Faster pull-up rise time ($t_r$) due to strong pMOS channel conductance without depletion body-effect limitations.
---
### 2. Delay Definitions & Fundamentals
- **Fan-Out:** The number of standard load gate inputs driven by the output of a single logic gate.
- **Fundamental Delay Unit ($\tau$):** The $RC$ time constant of a minimum-size ($2\lambda \times 2\lambda$) nMOS transistor driving a standard unit gate capacitance $\Box C_g$:
$$\mathbf{\tau = R_s(\text{n-channel}) \times \Box C_g}$$
- **For $5\,\mu\text{m}$ technology:**
  $$\tau = (10^4\,\Omega) \times (0.01\,\text{pF}) = 10^{-10}\text{ s} = \mathbf{0.1\text{ ns}}$$
![[attachments/Pasted image 20261102142254.png]]
---
### 3. Inverter Pair Delays
#### 4:1 nMOS Inverter Pair Delay ($5\tau$)
- **Pull-down discharge (Fall: $1 \to 0$):**
  $$t_f = 1 R_s \times 1\Box C_g = \mathbf{1\tau}$$
- **Pull-up charge (Rise: $0 \to 1$):**
  $$t_r = 4 R_s \times 1\Box C_g = \mathbf{4\tau}$$
- **Total Inverter Pair Delay:**
  $$t_{pair} = t_f + t_r = \left(1 + \frac{Z_{pu}}{Z_{pd}}\right)\tau = 1\tau + 4\tau = \mathbf{5\tau}$$
![[attachments/Pasted image 20261102144632.png]]
---
#### Minimum-Size CMOS Inverter Pair Delay ($7\tau$)
- **Input Load Capacitance:** Gate connects to both nMOS and pMOS:
  $$C_{in} = 1\Box C_g + 1\Box C_g = \mathbf{2\Box C_g}$$
- **Channel Resistances:**
  - nMOS: $R_n = 1 R_s = 10\text{ k}\Omega$
  - pMOS: $R_p = 2.5 R_s = 25\text{ k}\Omega$ ($\because \mu_p \approx \mu_n / 2.5$)
- **Fall Delay ($t_f$):** Load discharges through nMOS:
  $$t_f = R_n \times C_L = (1 R_s) \times (2\Box C_g) = \mathbf{2\tau}$$
- **Rise Delay ($t_r$):** Load charges through pMOS:
  $$t_r = R_p \times C_L = (2.5 R_s) \times (2\Box C_g) = \mathbf{5\tau}$$
- **CMOS Inverter Pair Delay:**
  $$\mathbf{t_{pair} = t_f + t_r = 2\tau + 5\tau = 7\tau}$$
- **Double Pair (4-Stage Cascaded CMOS) Delay:**
  $$t_{4\text{-stage}} = 2 \times t_{pair} = 2 \times 7\tau = \mathbf{14\tau}$$
![[attachments/Pasted image 20261102144641.png]]
---
### 4. General Delay Calculation Formula for Arbitrary Sizing
$$t_{fall} = Z_{pd} \times \left(\frac{C_{load}}{\Box C_g}\right) \times \tau$$
$$t_{rise} = Z_{pu} \times \left(\frac{C_{load}}{\Box C_g}\right) \times \tau$$
#### Solved Example (Q2.11):
- **Stage 1:** $L_{pu}=16\lambda, W_{pu}=2\lambda \implies Z_{pu1} = 8$; $L_{pd}=2\lambda, W_{pd}=2\lambda \implies Z_{pd1} = 1$.
- **Stage 2:** $L_{pu}=2\lambda, W_{pu}=2\lambda \implies Z_{pu2} = 1$; $L_{pd}=2\lambda, W_{pd}=8\lambda \implies Z_{pd2} = 0.25$.
- **Load between stages:** Gate area of Stage 2 $= (L_{pu} W_{pu} + L_{pd} W_{pd}) / 4\lambda^2 = (4 + 16)/4 = 5\Box C_g$.
- **Pair delay:** Sum of transition times evaluated directly using stage aspect ratios and node capacitances.
---
### 5. Gate Power Dissipation Calculations
$$\mathbf{P_{on} = \frac{V_{DD}^2}{R_{total}}}$$
1. **2-Input NAND Gate with Enhancement Pull-Up ($V_{DD} = 10\text{ V}$):**
   - ON state occurs when both inputs $A=B=1$.
   - Pull-down path: 2 identical series nMOS $\to 2 R_{pd}$.
   - Pull-up load: Enhancement nMOS $\to R_{pu}$.
   - Total series resistance: $R_{total} = R_{pu} + 2 R_{pd}$.
   - Power: $P_{on} = \frac{(10\text{ V})^2}{R_{pu} + 2 R_{pd}} = \frac{100}{R_{total}}\text{ W}$.
2. **2-Input NOR Gate with Depletion Pull-Up ($V_{DD} = 10\text{ V}$):**
   - ON state occurs when either input is HIGH.
   - Pull-down path: 1 active nMOS $\to R_{pd}$.
   - Pull-up load: Depletion nMOS $\to R_{pu}$.
   - Total series resistance: $R_{total} = R_{pu} + R_{pd}$.
   - Power: $P_{on} = \frac{(10\text{ V})^2}{R_{pu} + R_{pd}} = \frac{100}{R_{total}}\text{ W}$.
---
## 2B. Resistance & Capacitance Calculations
### 1. Sheet Resistance ($R_s$)
- **Formula:**
  $$R = \frac{\rho \cdot L}{\text{Area}} = \frac{\rho \cdot L}{t \cdot W} = \left(\frac{\rho}{t}\right)\left(\frac{L}{W}\right)$$
$$\mathbf{R_s = \frac{\rho}{t}} \quad [\Omega/\Box] \qquad \mathbf{Z = \frac{L}{W}} \quad [\text{squares}] \qquad \mathbf{R = R_s \cdot Z}$$
- **Key Insight:** Resistance of any square slab ($L = W \implies Z = 1$) is always $R_s$, regardless of dimension!
![[attachments/Pasted image 20261102140032.png]]

| Layer                       | Sheet Resistance (R_s) in 5 um Tech      |
| :---                        | :---                                     |
| Metal                       | 0.03 ohm / sq                            |
| Diffusion (n+)              | 10 - 50 ohm / sq                         |
| Silicide (on poly)          | 2 - 4 ohm / sq                           |
| Polysilicon                 | 15 - 100 ohm / sq                        |
| n-Transistor Channel (ON)   | 10^4 ohm / sq = 10 k-ohm / sq            |
| p-Transistor Channel (ON)   | 2.5 x 10^4 ohm / sq = 25 k-ohm / sq      |

---
### 2. Inverter "ON" Resistance from $V_{DD}$ to $GND$ ($R_{on}$)
$$\mathbf{R_{on} = R_{pu} + R_{pd} = (Z_{pu} \cdot R_{s,pu}) + (Z_{pd} \cdot R_{s,pd})}$$
- **For $5\,\mu\text{m}$ technology ($R_{s,n} = 10\text{ k}\Omega/\Box$):**
  - **If $Z_{pu}:Z_{pd} = 4:1$ ($Z_{pu}=4, Z_{pd}=1$):**
    $$R_{on} = 4(10\text{ k}\Omega) + 1(10\text{ k}\Omega) = \mathbf{50\text{ k}\Omega}$$
  - **If $Z_{pu}:Z_{pd} = 3:1$ ($Z_{pu}=3, Z_{pd}=1$):**
    $$R_{on} = 3(10\text{ k}\Omega) + 1(10\text{ k}\Omega) = \mathbf{40\text{ k}\Omega}$$
  - **Q2.20 ($L_{pu}:W_{pu} = 8:2 \implies Z_{pu} = 4$; $L_{pd}:W_{pd} = 16:2 \implies Z_{pd} = 8$):**
    $$R_{on} = 4(10\text{ k}\Omega) + 8(10\text{ k}\Omega) = \mathbf{120\text{ k}\Omega}$$
  - **Q2.21 ($L_{pu}:W_{pu} = 4:2 \implies Z_{pu} = 2$; $L_{pd}:W_{pd} = 12:2 \implies Z_{pd} = 6$):**
    $$R_{on} = 2(10\text{ k}\Omega) + 6(10\text{ k}\Omega) = \mathbf{80\text{ k}\Omega}$$
---
### 3. Area Capacitance & Standard Gate Unit ($\Box C_g$)
$$\mathbf{\Box C_g = C_{ox} \cdot (2\lambda \times 2\lambda) = 4\lambda^2 \cdot C_{ox}}$$
- **Typical Standard Values for $\Box C_g$:**
  - **$5\,\mu\text{m}$ technology** ($\lambda = 2.5\,\mu\text{m}$, Area $= 25\,\mu\text{m}^2$):
    $$\Box C_g = (4 \times 10^{-4}\,\text{pF}/\mu\text{m}^2) \times 25\,\mu\text{m}^2 = \mathbf{0.01\text{ pF}}$$
  - **$2\,\mu\text{m}$ technology** ($\lambda = 1.0\,\mu\text{m}$, Area $= 4\,\mu\text{m}^2$):
    $$\Box C_g = (8 \times 10^{-4}\,\text{pF}/\mu\text{m}^2) \times 4\,\mu\text{m}^2 = \mathbf{0.0032\text{ pF}}$$
  - **$1.2\,\mu\text{m}$ technology** ($\lambda = 0.6\,\mu\text{m}$, Area $= 1.44\,\mu\text{m}^2$):
    $$\Box C_g = (16 \times 10^{-4}\,\text{pF}/\mu\text{m}^2) \times 1.44\,\mu\text{m}^2 \approx \mathbf{0.0023\text{ pF}}$$
![[attachments/Pasted image 20261102135722.png]]

| Layer Capacitance          | 5 um Tech [rel] | 2 um Tech [rel] | 1.2 um|
| :---                       | :---            | :---            | :---  |
| Gate to channel            | 4.0 (1.0)       | 8.0 (1.0)       | 16.0  |
| Diffusion (active)         | 1.0 (0.25)      | 1.75 (0.22)     | 3.75  |
| Polysilicon to substrate   | 0.4 (0.1)       | 0.6 (0.075)     | 0.60  |
| Metal 1 to substrate       | 0.3 (0.075)     | 0.33 (0.04)     | 0.33  |
| Metal 2 to substrate       | 0.2 (0.05)      | 0.17 (0.02)     | 0.17  |
| Metal 2 to Metal 1         | 0.4 (0.1)       | 0.5 (0.06)      | 0.50  |
| Metal 2 to Polysilicon     | 0.3 (0.075)     | 0.3 (0.038)     | 0.30  |

---
### 4. Multilayer Capacitance Calculation Steps
1. **Calculate Area in standard squares ($N$):**
   $$N = \frac{\text{Length} \times \text{Width}}{2\lambda \times 2\lambda} = \frac{L \times W}{4\lambda^2}$$
2. **Multiply by Layer Relative Factor:**
   $$C_{\text{layer}} = N \times (\text{Relative Value}) \times \Box C_g$$
3. **Total Capacitance:**
   $$C_{total} = \sum C_{\text{layer}}$$
4. **Convert to absolute pF (if required):**
   $$C\text{ [pF]} = C\text{ [in }\Box C_g\text{]} \times \Box C_g\text{ (pF value for that tech)}$$
---
## 2C. Scaling, Miniaturization, Transit Time & Doping
### 1. Scaling Models: Constant Field vs. Constant Voltage

| Dimension / Parameter    | General | Constant Field (beta=alpha) | Const V (beta=1)|
| :---                     | :---    | :---                        | :---            |
| Length, Width (L, W)     | 1/alpha | 1/alpha                     | 1/alpha         |
| Oxide Thickness (D)      | 1/beta  | 1/alpha                     | 1               |
| Supply Voltage (V_DD)    | 1/beta  | 1/alpha                     | 1 (Constant)    |
| Electric Field (E)       | alpha/beta | 1 (Constant)             | alpha (Increases)|

---
### 2. Comprehensive Device Parameter Scaling Table

| Parameter                     | General | Const Field (b=a)| Const Volt (b=1) |
| :---                          | :---    | :---             | :---             |
| Gate Area ($A_g$)             | 1/a^2   | 1/a^2            | 1/a^2            |
| Gate Cap / Area ($C_{ox}$)    | b       | a                | 1                |
| Gate Capacitance ($C_g$)      | b/a^2   | 1/a              | 1/a^2            |
| Parasitic Capacitance ($C_x$) | 1/a     | 1/a              | 1/a              |
| Carrier Density ($Q_{on}$)    | 1       | 1                | a                |
| Channel ON Resistance ($R_{on}$)| 1     | 1                | 1/a              |
| Saturation Current ($I_{dss}$) | 1/b    | 1/a              | a                |
| Current Density ($J$)         | a^2/b   | a                | a^3 (DANGEROUS!) |
| Gate Delay ($T_d$)            | b/a^2   | 1/a              | 1/a^2            |
| Max Clock Freq ($f_0$)        | a^2/b   | a                | a^2              |
| Power / Gate ($P_g$)          | 1/b^2   | 1/a^2            | 1                |
| Power Density ($P_a$)         | a^2/b^2 | 1                | a^2 (HEAT WALL!) |
| Switching Energy ($E_g$)      | 1/(a^2 b)| 1/a^3           | 1/a^2            |
| Power-Delay Product ($P_T$)   | 1/(a^2 b)| 1/a^3           | 1/a^2            |
| Substrate Doping ($N_B$)      | a^2/b   | a                | a^2              |

---
### 3. Key Scaling Derivations
#### Gate Delay ($T_d$):
$$T_d \propto R_{on} \cdot C_g = (1) \times \left(\frac{\beta}{\alpha^2}\right) = \mathbf{\frac{\beta}{\alpha^2}}$$
- **Constant Field ($\beta = \alpha$):** $T_d$ scales by $1/\alpha$ ($\downarrow$ delay $\to$ faster).
- **Constant Voltage ($\beta = 1$):** $T_d$ scales by $\mathbf{1/\alpha^2}$ ($\downarrow\downarrow$ super fast).
#### Current Density ($J$):
$$J = \frac{I_{dss}}{A_{cross}} = \frac{1/\beta}{1/\alpha^2} = \mathbf{\frac{\alpha^2}{\beta}}$$
- **Constant Field ($\beta = \alpha$):** $J$ scales by $\alpha$ ($\uparrow$ linear increase).
- **Constant Voltage ($\beta = 1$):** $J$ scales by $\mathbf{\alpha^3}$ ($\uparrow\uparrow\uparrow$ explosive increase $\to$ electromigration wire failure!).
#### Power Dissipation per Unit Area ($P_a$):
$$P_a = \frac{P_g}{A_g} = \frac{1/\beta^2}{1/\alpha^2} = \mathbf{\frac{\alpha^2}{\beta^2}}$$
- **Constant Field ($\beta = \alpha$):** $P_a$ scales by $\mathbf{1}$ (heat density stays constant!).
- **Constant Voltage ($\beta = 1$):** $P_a$ scales by $\mathbf{\alpha^2}$ ($\uparrow\uparrow$ chips overheat rapidly!).
---
### 4. Transit Time ($\tau_{sd}$) Calculation
$$\mathbf{\tau_{sd} = \frac{L^2}{\mu V_{ds}} = \frac{d}{v_{drift}}}$$
- **Numerical Problem (Q2.28, Q2.29):**
  - Drift velocity $v_d = 1 \times 10^7\text{ cm/s}$
  - Depletion width $d = 10^{-1}\,\mu\text{m} = 10^{-5}\text{ cm}$
  - **Transit time:**
    $$\tau = \frac{d}{v_d} = \frac{10^{-5}\text{ cm}}{1 \times 10^7\text{ cm/s}} = 10^{-12}\text{ s} = \mathbf{1\text{ ps}}$$
  - **Mobility per unit field:**
    $$\mu = \frac{v_d}{E} = \frac{v_d}{V/d}$$
---
### 5. Substrate Doping Level ($N_B$) & Channel Formation
- **Derivation of Scaling Factor:**
  - Depletion layer thickness: $d \propto \sqrt{\frac{2\varepsilon V}{q N_B}} \implies d^2 \propto \frac{V}{N_B} \implies N_B \propto \frac{V}{d^2}$.
  - Scaling $V$ by $1/\beta$ and $d$ by $1/\alpha$:
    $$\mathbf{N_B \propto \frac{1/\beta}{(1/\alpha)^2} = \frac{\alpha^2}{\beta}}$$
  - **Constant Field:** $N_B$ scales by $\alpha$ ($\uparrow$).
  - **Constant Voltage:** $N_B$ scales by $\alpha^2$ ($\uparrow\uparrow$).
- **Why Channel Cannot Form at Excessively High $N_B$ (Q2.30, Q2.31):**
  1. **Depletion Width Shrinks:** Heavy substrate doping forces depletion layer $d$ to become extremely narrow.
  2. **Threshold Voltage Explosion:** Threshold voltage increases drastically ($V_t \propto \sqrt{N_B}$); gate voltage cannot induce strong inversion.
  3. **Premature Junction Breakdown:** Extreme internal electric field triggers Zener tunneling or avalanche breakdown across the $p\text{-}n$ junction before an inversion channel can form.
---
### 6. Limits of Miniaturization
1. **Subthreshold Leakage:**
   - Subthreshold swing $S = \left(\frac{kT}{q}\right) \ln(10) \left(1 + \frac{C_d}{C_{ox}}\right) \approx 60-90\text{ mV/decade}$ depends on temperature $T$, **does not scale** with $\alpha$.
   - Lowering $V_t$ causes exponential OFF-state leakage current ($I_{leak} \propto e^{-V_t / (kT/q)}$).
2. **Gate Oxide Tunneling:**
   - When $\text{SiO}_2$ thickness $D < 1.5\text{ nm}$ ($\approx 4-5$ atomic layers), electrons quantum-tunnel directly through the insulator $\to$ gate leakage destroys insulation.
3. **Source-Drain Punch-Through & DIBL:**
   - Depletion regions of source and drain merge under short channel lengths $\to$ gate loses control of channel.
4. **Interconnect $RC$ Bottleneck & Electromigration:**
   - Wire cross-section shrinks by $1/\alpha^2 \to$ wire resistance skyrockets by $\alpha^2$.
   - Current density $J \propto \alpha^3$ causes atoms to migrate physically along aluminum wires, creating voids and shorts.
5. **Thermal Power Wall:**
   - Heat generated per $\text{cm}^2$ exceeds heatsink air-cooling limits ($\sim 100\text{ W/cm}^2$).
