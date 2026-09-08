### 1. Page 17, Q.1(a): What is transformer? Briefly describe the basic construction and working principle of a transformer.

#### **Definition of a Transformer**
A **transformer** is a static (or stationary) piece of electrical apparatus by means of which electric power in one circuit is transformed into electric power of the same frequency in another circuit. It can raise or lower the voltage in an alternating current (a.c.) circuit with a corresponding decrease or increase in current. 

In brief, a transformer is a device that:
1. Transfers electrical energy from one electrical circuit to another.
2. Accomplishes energy transfer without a change in frequency.
3. Operates on the principle of electromagnetic induction (mutual induction).
4. Links two electrical circuits that are not conductively connected, but are under mutual inductive influence of each other.

---

#### **Working Principle of a Transformer**
The physical basis of a transformer is **mutual induction** between two magnetically coupled coils:

```
          Alternating Flux Φ
       ┌──────────────────────┐
       │   Laminated Core     │
       │  ┌────────────────┐  │
       │  │                │  │
Primary│  │                │  │ Secondary
Winding│  │                │  │ Winding
  (N₁) ╞══╡                ╞══╡ (N₂)
       │  │                │  │
  V₁ ~ ╞══╡                ╞══╡ ~ V₂ (Load)
       │  │                │  │
       │  └────────────────┘  │
       └──────────────────────┘
```

1. **Primary Excitation:** When the primary winding is connected to an alternating voltage source $V_1$, an alternating current flows through it, establishing an alternating magnetic flux $\Phi$ in the laminated steel core.
2. **Mutual Flux Linkage:** Most of this flux is confined within the high-permeability, low-reluctance magnetic path provided by the core and links with both the primary and secondary windings.
3. **Induced EMF:** According to **Faraday's Law of Electromagnetic Induction**, the rate of change of flux linkages induces:
   - A self-induced electromotive force (e.m.f.) $E_1$ in the primary winding:
     $$e_1 = -N_1 \frac{d\Phi}{dt}$$
   - A mutually-induced electromotive force $E_2$ in the secondary winding:
     $$e_2 = -N_2 \frac{d\Phi}{dt}$$
4. **Energy Transfer:** If the secondary circuit is closed across a load, the induced e.m.f. $E_2$ causes a secondary current $I_2$ to flow, thereby delivering electrical energy to the load entirely magnetically without any physical electrical contact between primary and secondary circuits.

---

#### **Basic Construction of a Transformer**
A transformer consists of the following primary parts:

1. **Magnetic Core:**
   - Built of high-grade silicon steel laminations (typically $0.35\text{ mm}$ to $0.5\text{ mm}$ thick) insulated from each other by varnish or oxide coating to reduce **eddy current losses**.
   - Made of cold-rolled grain-oriented (CRGO) silicon steel to ensure high permeability and low **hysteresis loss**.
   - Depending on core arrangement, transformers are classified as:
     - **Core-Type:** The windings surround a considerable part of the core.
     - **Shell-Type:** The core surrounds a considerable portion of the windings.

2. **Windings:**
   - Composed of high-conductivity electrolytic copper conductors, insulated with paper, enamel, or cloth tape.
   - The winding connected to the higher voltage supply is the **High-Voltage (H.V.) winding**, and the one connected to the lower voltage is the **Low-Voltage (L.V.) winding**. The L.V. winding is placed closest to the core to minimize insulation requirements.

3. **Insulation Medium and Tank:**
   - The core and coil assembly is placed inside a sheet-steel container filled with purified **transformer insulating oil**, which serves two vital purposes:
     - Providing high dielectric insulation between windings and tank.
     - Dissipating heat generated inside the core and windings by natural convection/circulation to the tank walls and cooling tubes.

4. **Bushings and Terminals:**
   - Porcelain or capacitor-type bushings are mounted on the tank cover to bring out the winding leads safely without flashover to the grounded tank body.

---

### 2. Page 17, Q.1(c): By mistake, you have connected a DC supply to a transformer. What will be the effects on transformer in that condition?

Connecting a continuous direct current (D.C.) supply across the primary winding of a transformer leads to serious destructive consequences:

#### **1. Absence of Counter E.M.F. (Back E.M.F.)**
In normal A.C. operation, the alternating magnetic flux induces a back e.m.f. $E_1$ that opposes the applied voltage $V_1$, limiting the primary current to a very small magnetizing value:
$$I_1 = \frac{V_1 - E_1}{Z_1}$$
When a D.C. voltage $V_{\text{dc}}$ is applied, the resulting current is steady and unidirectional. Since direct current has zero frequency ($f = 0$), the magnetic flux produced in the core is constant:
$$\frac{d\Phi}{dt} = 0 \implies E_1 = -N_1 \frac{d\Phi}{dt} = 0$$
No self-induced back e.m.f. is developed to oppose the applied voltage.

#### **2. Abnormally High Primary Current**
In the absence of inductive reactance ($X_L = 2\pi f L = 0$), the primary current is limited solely by the very small ohmic resistance $R_1$ of the primary winding:
$$I_{\text{dc}} = \frac{V_{\text{dc}}}{R_1}$$
Because $R_1$ is intentionally designed to be extremely small (typically a fraction of an ohm or a few ohms), this current will be **many times (20 to 50 times) higher** than the normal rated full-load alternating current.

#### **3. Overheating and Burnout of Winding**
The excessive current causes tremendous $I^2R$ copper losses in the primary winding:
- Severe and rapid heat generation occurs.
- The winding insulation chars and breaks down completely.
- The transformer gets permanently damaged or burns out within seconds unless cleared instantly by protection fuses or circuit breakers.

#### **4. Core Saturation and Zero Secondary Output**
- The high direct current drives the iron core deep into heavy magnetic saturation.
- Because the flux is stationary ($\frac{d\Phi}{dt} = 0$), no e.m.f. is induced in the secondary winding ($E_2 = 0$). Hence, no electrical power is transferred to the secondary side.

---

### 3. Page 17, Q.1(d): Define voltage transformation ratio. What will happen if 60 Hz transformer is connected to 50 Hz supply.

#### **Definition of Voltage Transformation Ratio ($K$)**
The **voltage transformation ratio** (denoted by $K$) is defined as the ratio of the secondary induced e.m.f. to the primary induced e.m.f. (or the ratio of secondary turns to primary turns):

$$K = \frac{E_2}{E_1} = \frac{N_2}{N_1}$$

On no-load, assuming negligible internal voltage drops ($V_1 \approx E_1$ and $V_2 \approx E_2$):
$$K = \frac{V_2}{V_1} = \frac{N_2}{N_1}$$

- **Step-up Transformer:** If $N_2 > N_1$ ($K > 1$), then $V_2 > V_1$, and the transformer steps up the voltage.
- **Step-down Transformer:** If $N_2 < N_1$ ($K < 1$), then $V_2 < V_1$, and the transformer steps down the voltage.

---

#### **Effects of Operating a 60 Hz Transformer on a 50 Hz Supply**
When a transformer designed for rated operation at $60\text{ Hz}$ is connected to a $50\text{ Hz}$ supply at the same rated voltage ($V$):

1. **Increase in Core Flux Density ($B_m$):**
   From the transformer e.m.f. equation, $V \approx E = 4.44 f N B_m A$, meaning:
   $$B_m \propto \frac{V}{f}$$
   Since frequency decreases from $60\text{ Hz}$ to $50\text{ Hz}$ while voltage remains constant, the maximum flux density increases:
   $$B_{m(50)} = B_{m(60)} \times \left(\frac{60}{50}\right) = 1.20 \, B_{m(60)}$$
   The core flux density increases by **$20\%$**.

2. **Heavy Core Saturation & Excessive Magnetizing Current ($I_\mu$):**
   Standard transformer cores are operated near the knee of their $B\text{-}H$ magnetization curve. A $20\%$ increase pushes the core deep into saturation, resulting in a disproportionately large surge in the no-load magnetizing current $I_\mu$ (often increasing several-fold) and causing poor no-load power factor.

3. **Increase in Core Losses:**
   - **Hysteresis Loss ($W_h$):**
     $$W_h \propto B_m^{1.6} f \propto \left(\frac{V}{f}\right)^{1.6} f \propto V^{1.6} f^{-0.6}$$
     $$W_{h(50)} = W_{h(60)} \times \left(\frac{60}{50}\right)^{0.6} \approx 1.115 \, W_{h(60)} \quad (\approx 11.5\% \text{ increase})$$
   - **Eddy Current Loss ($W_e$):**
     $$W_e \propto B_m^2 f^2 \propto \left(\frac{V}{f}\right)^2 f^2 \propto V^2 \quad (\text{remains practically constant})$$
   - Consequently, the total iron loss ($W_i = W_h + W_e$) increases, leading to excessive core heating.

4. **Reduction in kVA Rating:**
   Because of higher core losses and higher no-load copper heating, the allowable full-load current must be reduced to keep the overall temperature rise within permissible limits. Hence, the safe output kVA rating of the transformer decreases by roughly $1/1.2 \approx 17\% - 20\%$.

5. **Poorer Voltage Regulation:**
   The higher magnetizing current causes larger internal voltage drops, leading to poorer voltage regulation.

---

### 4. Page 18, Q.1(b): Prove that, v1/v2 = N1/N2 = I2/I1 where symbols have their usual meanings.

#### **Derivation:**

Let:
- $V_1, V_2 =$ Primary and secondary terminal voltages respectively
- $E_1, E_2 =$ Induced e.m.f. in primary and secondary windings respectively
- $N_1, N_2 =$ Number of turns on primary and secondary windings respectively
- $I_1, I_2 =$ Primary and secondary full-load currents respectively
- $\Phi_m =$ Maximum value of core flux in Webers
- $f =$ Frequency of the A.C. supply in Hz

---

#### **Step 1: Relation between Induced E.M.F. and Turns Ratio**
During each cycle of an alternating sine wave of frequency $f$, the magnetic flux $\Phi$ changes from $0$ to its peak value $\Phi_m$ in one quarter of a time period, i.e., in $t = \frac{T}{4} = \frac{1}{4f}\text{ second}$.

The average rate of change of flux per turn is:
$$\text{Average rate of change of flux} = \frac{\Phi_m}{1/(4f)} = 4 f \Phi_m \text{ Wb/s (or Volts)}$$

Since form factor for a sinusoidal wave is:
$$\text{Form Factor} = \frac{\text{R.M.S. Value}}{\text{Average Value}} = 1.11$$

The R.M.S. value of induced e.m.f. per turn is:
$$\text{R.M.S. e.m.f. per turn} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m \text{ Volts}$$

Thus, the total induced e.m.f. in primary and secondary windings are:
$$E_1 = 4.44 f N_1 \Phi_m \tag{1}$$
$$E_2 = 4.44 f N_2 \Phi_m \tag{2}$$

Dividing Equation (1) by Equation (2):
$$\frac{E_1}{E_2} = \frac{4.44 f N_1 \Phi_m}{4.44 f N_2 \Phi_m} = \frac{N_1}{N_2} \tag{3}$$

For an ideal transformer (or on no-load condition where winding resistance and magnetic leakage are negligible):
$$V_1 = E_1 \quad \text{and} \quad V_2 = E_2$$

Therefore:
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} \tag{4}$$

---

#### **Step 2: Relation between Voltages and Currents**
For an ideal transformer, there are no core or copper losses, meaning efficiency is $100\%$. Therefore, the total input apparent power in volt-amperes ($\text{VA}$) is equal to the output apparent power:

$$\text{Input Volt-Amperes} = \text{Output Volt-Amperes}$$
$$V_1 I_1 = V_2 I_2$$

Rearranging the terms:
$$\frac{V_1}{V_2} = \frac{I_2}{I_1} \tag{5}$$

---

#### **Conclusion:**
Equating Equations (4) and (5):
$$\frac{V_1}{V_2} = \frac{N_1}{N_2} = \frac{I_2}{I_1}$$

*(Hence proved.)*

### 5. Page 19, Q.1(a): Show that the emf induced in the secondary winding of a transformer is E2 = 4.44 f N2 φm, where symbols have their usual meanings.

#### **Derivation:**

Let:
- $N_2 =$ Number of turns in the secondary winding
- $\Phi_m =$ Maximum value of the alternating core flux in Webers ($\text{Wb}$)
- $f =$ Frequency of the alternating input supply in Hertz ($\text{Hz}$)
- $T =$ Time period of the alternating supply wave in seconds $= \frac{1}{f}$
- $E_2 =$ R.M.S. value of the e.m.f. induced in the secondary winding (in Volts)

---

#### **Step 1: Flux Variation over a Cycle**
Assuming a sinusoidal alternating voltage applied to the primary, the magnetic flux $\Phi$ established in the core varies sinusoidally with time:
$$\Phi = \Phi_m \sin(\omega t) = \Phi_m \sin(2\pi f t)$$

As shown below, the core flux increases from its zero value to its maximum value $\Phi_m$ in **one-quarter of a cycle**:

```
        Flux (Φ)
          ▲
      +Φm ┼           ┌───┐
          │         /       \
          │       /           \
        0 ┼──────┼─────────────┼──────────────► Time (t)
          │    T/4 = 1/(4f)     \            /
          │                       \        /
      -Φm ┼                         └───┘
          │◄──────────────── T = 1/f ────────►│
```

$$\text{Time taken to reach peak flux } \Phi_m = \frac{T}{4} = \frac{1}{4f} \text{ second}$$

---

#### **Step 2: Average Rate of Change of Flux**
According to Faraday's Law of Electromagnetic Induction, the e.m.f. induced per turn is equal to the rate of change of flux linkages.

$$\text{Average rate of change of flux} = \frac{\text{Change in flux}}{\text{Time taken}} = \frac{\Phi_m - 0}{1/(4f)} = 4 f \Phi_m \text{ Wb/s (or Volts)}$$

Therefore, the **average e.m.f. induced per turn** is:
$$\text{Average e.m.f./turn} = 4 f \Phi_m \text{ Volts}$$

---

#### **Step 3: R.M.S. Value of Induced E.M.F. per Turn**
For a purely sinusoidal wave, the **Form Factor** is given by:
$$\text{Form Factor} = \frac{\text{R.M.S. Value}}{\text{Average Value}} = 1.11$$

$$\text{R.M.S. value of e.m.f./turn} = 1.11 \times \text{Average e.m.f./turn}$$
$$\text{R.M.S. value of e.m.f./turn} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m \text{ Volts}$$

---

#### **Step 4: Total Induced E.M.F. in Secondary Winding ($E_2$)**
Since the secondary winding consists of $N_2$ turns connected in series, the total R.M.S. e.m.f. induced in the secondary winding is:

$$E_2 = (\text{R.M.S. e.m.f./turn}) \times N_2$$
$$E_2 = 4.44 f N_2 \Phi_m \text{ Volts}$$

If $B_m$ is the maximum flux density in $\text{Wb/m}^2$ (or Tesla) and $A$ is the effective cross-sectional area of the core in $\text{m}^2$, then $\Phi_m = B_m \times A$. The equation can also be written as:
$$E_2 = 4.44 f N_2 B_m A \text{ Volts}$$

*(Hence proved.)*

---

### 6. Page 23, Q.9: Define step-up and step-down transformer.

#### **1. Step-Up Transformer**
A **step-up transformer** is a transformer that increases (steps up) the alternating voltage from the primary winding to the secondary winding while decreasing the current proportionately to keep the apparent power constant.

```
       Primary (Low V, High I)         Secondary (High V, Low I)
            ┌──┐                             ┌──┐
            │  │ (Fewer Turns, N₁)           │  │ (More Turns, N₂)
       V₁ ~ │  │ ───►                  V₂ ~  │  │ (V₂ > V₁)
            │  │      Magnetic Core          │  │
            └──┘                             └──┘
```

- **Key Characteristics:**
  - Secondary voltage is greater than primary voltage: $V_2 > V_1$ ($E_2 > E_1$).
  - Secondary turns are greater than primary turns: $N_2 > N_1$.
  - Voltage transformation ratio: $K = \frac{N_2}{N_1} > 1$.
  - Secondary current is less than primary current: $I_2 < I_1$.
  - The low-voltage winding (primary) has fewer turns of thicker conductor, while the high-voltage winding (secondary) has more turns of thinner conductor.
- **Application:** Used at generating power stations to raise generated voltage (e.g., $11\text{ kV}$ to $132\text{ kV}, 275\text{ kV}, 400\text{ kV}$) to minimize transmission line $I^2R$ losses over long distances.

---

#### **2. Step-Down Transformer**
A **step-down transformer** is a transformer that decreases (steps down) the alternating voltage from the primary winding to the secondary winding while increasing the current proportionately.

```
       Primary (High V, Low I)         Secondary (Low V, High I)
            ┌──┐                             ┌──┐
            │  │ (More Turns, N₁)            │  │ (Fewer Turns, N₂)
       V₁ ~ │  │ ───►                  V₂ ~  │  │ (V₂ < V₁)
            │  │      Magnetic Core          │  │
            └──┘                             └──┘
```

- **Key Characteristics:**
  - Secondary voltage is less than primary voltage: $V_2 < V_1$ ($E_2 < E_1$).
  - Secondary turns are fewer than primary turns: $N_2 < N_1$.
  - Voltage transformation ratio: $K = \frac{N_2}{N_1} < 1$.
  - Secondary current is greater than primary current: $I_2 > I_1$.
  - The high-voltage winding (primary) consists of many turns of thin wire, while the low-voltage winding (secondary) consists of fewer turns of thick wire.
- **Application:** Used at distribution substations and consumer service entrances to step down high transmission voltages to standard safe utilization levels (e.g., $11\text{ kV}$ to $400\text{ V} / 230\text{ V}$) for domestic, commercial, and industrial loads.

---

### 7. Page 23, Q.10: Derive the equation of induced e.m.f. in the whole of primary winding of a transformer with net diagram. [Figure Involved]

#### **Derivation of Primary Induced E.M.F. ($E_1$):**

Let:
- $N_1 =$ Number of turns in the primary winding
- $\Phi_m =$ Peak value of core flux in Webers ($\text{Wb}$)
- $f =$ Supply frequency in Hertz ($\text{Hz}$)
- $B_m =$ Maximum flux density in Tesla ($\text{Wb/m}^2$)
- $A =$ Effective cross-sectional area of the magnetic core in $\text{m}^2$

---

#### **Diagrams:**

**1. Transformer Core & Primary Circuit:**
```
            Alternating Flux Φ
         ┌───────────────────────┐
         │     Laminated Core    │
         │   ┌───────────────┐   │
         │   │               │   │
  Primary│   │               │   │
  Winding│   │               │   │
    (N₁) ╞═══╡               │   │
         │   │               │   │
   V₁  ~ ╞═══╡               │   │
 (Applied│   │               │   │
 Voltage)│   │               │   │
         │   └───────────────┘   │
         └───────────────────────┘
```

**2. Flux Waveform and Time Relations:**
```
     Core Flux (Φ)
         ▲
     +Φm ┼           ┌─────┐
         │         /    |    \
         │       /      |      \
       0 ┼──────┼───────┼───────┼───────► Time (t)
         │      │  T/4  │  T/2  │   T
         │      │◄─────►│       │
     -Φm ┼      │       │       │ ┌─────┐
         │      │       │       │/       \
         └──────┴───────┴───────┴─────────►
```

---

#### **Step-by-Step Derivation:**

1. **Change of Flux in One-Quarter Cycle:**
   The flux is alternating sinusoidally at frequency $f$. In every cycle, the flux starts from zero and reaches its maximum value $\Phi_m$ in one-fourth of the time period ($T/4$):
   $$\Delta t = \frac{T}{4} = \frac{1}{4f} \text{ seconds}$$
   $$\Delta \Phi = \Phi_m - 0 = \Phi_m \text{ Wb}$$

2. **Average Induced E.M.F. per Turn:**
   From Faraday's Law, the magnitude of average induced e.m.f. per turn is:
   $$\text{Average e.m.f./turn} = \frac{\Delta \Phi}{\Delta t} = \frac{\Phi_m}{1/(4f)} = 4 f \Phi_m \text{ Volts}$$

3. **R.M.S. Value of Induced E.M.F. per Turn:**
   For a sinusoidal waveform, the relation between R.M.S. value and average value is defined by the Form Factor:
   $$\text{Form Factor} = \frac{\text{R.M.S. Value}}{\text{Average Value}} = 1.11$$
   $$\text{R.M.S. e.m.f./turn} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m \text{ Volts}$$

4. **Total Induced E.M.F. in the Whole Primary Winding ($E_1$):**
   The total induced e.m.f. in the entire primary winding is obtained by multiplying the R.M.S. e.m.f. per turn by the total primary turns $N_1$:
   $$E_1 = (\text{R.M.S. e.m.f./turn}) \times N_1$$
   $$E_1 = 4.44 f N_1 \Phi_m \text{ Volts}$$

Substituting $\Phi_m = B_m \times A$:
$$E_1 = 4.44 f N_1 B_m A \text{ Volts}$$

*(Hence derived.)*

---

### 8. Page 23, Q.11: What is voltage transformation ratio or turns ratio? Why it is important?

#### **1. Voltage Transformation Ratio ($K$)**
The **voltage transformation ratio** (denoted by $K$) is defined as the ratio of the secondary induced electromotive force to the primary induced electromotive force:

$$K = \frac{E_2}{E_1} = \frac{N_2}{N_1}$$

Under ideal or no-load conditions where internal winding drops are negligible ($V_1 \approx E_1$ and $V_2 \approx E_2$):
$$K = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1}{I_2}$$

---

#### **2. Turns Ratio**
The **turns ratio** of a transformer is defined as the ratio of the number of turns in the primary winding to the number of turns in the secondary winding:

$$\text{Turns Ratio} = \frac{N_1}{N_2} = \frac{1}{K}$$

*(Note: Depending on context, turns ratio is sometimes defined as $N_1/N_2$ and transformation ratio as $N_2/N_1$.)*

---

#### **3. Importance of Transformation / Turns Ratio**
The transformation ratio is a fundamental design and operating parameter of a transformer for the following reasons:

1. **Classification of Transformer Action:**
   - If $K > 1$ ($N_2 > N_1$), the unit functions as a **step-up transformer**.
   - If $K < 1$ ($N_2 < N_1$), the unit functions as a **step-down transformer**.
   - If $K = 1$ ($N_2 = N_1$), it acts as a **$1:1$ isolation transformer**.

2. **Impedance Transformation (Parameter Shifting):**
   It allows resistances, reactances, and load impedances on one side to be transferred to the other side for simplified network analysis and equivalent circuit representation:
   - Secondary resistance referred to primary: $R_2' = \frac{R_2}{K^2}$
   - Primary resistance referred to secondary: $R_1' = K^2 R_1$
   - Load impedance referred to primary: $Z_L' = \frac{Z_L}{K^2}$

3. **Current and Power Ratings Determination:**
   It defines the inverse scaling of line and phase currents ($I_1 = K I_2$), allowing proper sizing of conductor cross-sectional areas and protection switchgear.

4. **Essential Requirement for Parallel Operation:**
   For two or more transformers to operate in parallel successfully without destructive circulating currents on no-load, their voltage transformation ratios must be strictly equal.

5. **Design of Core and Windings:**
   It allows the designer to fix the number of primary and secondary turns for a specified volt-per-turn value dictated by core flux and magnetic flux density limits.

### 9. Page 23, Q.12: What will happen if a 60 Hz transformer is connected to 50 Hz supply?

When a transformer designed and rated for **$60\text{ Hz}$** operation is connected to a **$50\text{ Hz}$** supply at the same rated primary voltage ($V$), several critical operational changes occur:

---

#### **1. Increase in Maximum Core Flux Density ($B_m$)**
From the transformer e.m.f. equation:
$$V \approx E = 4.44 f N B_m A \implies B_m = \frac{V}{4.44 f N A} \propto \frac{V}{f}$$

Since the applied voltage $V$ remains constant while frequency $f$ decreases from $60\text{ Hz}$ to $50\text{ Hz}$:
$$B_{m(50)} = B_{m(60)} \times \left(\frac{60}{50}\right) = 1.20 \, B_{m(60)}$$

The peak magnetic flux density in the iron core increases by **$20\%$**.

---

#### **2. Core Saturation and Surge in Magnetizing Current ($I_\mu$)**
- Standard commercial transformers are designed to operate near the knee point of the magnetic saturation curve ($B\text{-}H$ curve).
- A $20\%$ increase in $B_m$ drives the core deep into the non-linear saturation region.
- Consequently, the **magnetizing current ($I_\mu$)** shoots up drastically (often by several hundred percent), resulting in a heavily distorted, non-sinusoidal primary current waveform and a very poor no-load power factor.

---

#### **3. Increase in Core Losses (Iron Losses)**
The total iron loss consists of hysteresis and eddy current losses:
- **Hysteresis Loss ($W_h$):**
  $$W_h = \eta B_m^{1.6} f V_{\text{core}} \propto \left(\frac{V}{f}\right)^{1.6} f \propto V^{1.6} f^{-0.6}$$
  $$W_{h(50)} = W_{h(60)} \times \left(\frac{60}{50}\right)^{0.6} = 1.115 \, W_{h(60)}$$
  Hysteresis loss increases by **$11.5\%$**.
- **Eddy Current Loss ($W_e$):**
  $$W_e = K_e B_m^2 f^2 t^2 V_{\text{core}} \propto \left(\frac{V}{f}\right)^2 f^2 \propto V^2$$
  Eddy current loss depends purely on voltage magnitude and remains practically unchanged.
- **Total Iron Loss ($W_i$):** Increases, causing higher steady-state core temperatures.

---

#### **4. Derating of Output kVA Capacity**
To avoid overheating caused by higher core losses and large no-load currents:
- The permissible load current must be reduced.
- The transformer's safe continuous power delivery capacity must be derated by approximately **$15\%\text{ to }20\%$**:
  $$\text{Safe kVA at } 50\text{ Hz} \approx \frac{50}{60} \times (\text{Rated kVA at } 60\text{ Hz}) = 0.833 \times \text{kVA}_{60}$$

---

#### **5. Voltage Regulation**
Due to higher magnetizing current and increased primary winding resistive drops, the voltage regulation becomes poorer (higher percentage voltage drop under load).

---

### 10. Page 36, Q.1(b): What will happen if a dc source of rated value is applied across the primary coil of a transformer?

Applying a continuous direct current (D.C.) supply of rated voltage magnitude across the primary coil of a transformer produces catastrophic effects:

---

#### **1. Absence of Counter E.M.F. (Back E.M.F.)**
Under alternating current (A.C.) operation, the alternating magnetic flux induces a back e.m.f. $E_1$ in the primary according to Faraday’s law:
$$E_1 = -N_1 \frac{d\Phi}{dt}$$
This back e.m.f. opposes the applied voltage $V_1$ at every instant and limits the primary current to a small safe value.

When a steady D.C. voltage $V_{\text{dc}}$ is applied:
- The current produces a stationary (time-invariant) magnetic flux in the core.
- The rate of change of flux is zero:
  $$\frac{d\Phi}{dt} = 0 \implies E_1 = 0$$
- No opposing counter e.m.f. is established.

---

#### **2. Abnormally High Current Flow**
With zero frequency ($f = 0$), the inductive reactance is zero ($X_L = 2\pi f L = 0$). The current drawn by the primary is limited strictly by its internal ohmic resistance $R_1$:
$$I_{\text{dc}} = \frac{V_{\text{dc}}}{R_1}$$

Because primary windings are constructed with thick, highly conductive copper to keep resistance very low (often less than $1\,\Omega$), the resulting D.C. current will be **$20\text{ to }50\text{ times}$ greater** than the rated full-load current.

---

#### **3. Severe Overheating and Destruction (Burnout)**
- The primary copper loss increases as the square of the current ($P_{\text{Cu}} = I_{\text{dc}}^2 R_1$).
- Extreme heat is released almost instantaneously.
- The winding insulation chars, smokes, and melts, leading to an inter-turn short-circuit and complete burnout of the transformer within seconds.

---

#### **4. Zero Energy Transfer to Secondary**
Because the magnetic flux in the core is constant ($\frac{d\Phi}{dt} = 0$), no mutual e.m.f. is induced in the secondary winding:
$$E_2 = -N_2 \frac{d\Phi}{dt} = 0\text{ V}$$
Thus, no voltage or electric power appears across the secondary terminals.

---

### 11. Page 36, Q.1(c): What will happen if a transformer rated at 50 Hz is operated on 60 Hz supply line?

Operating a transformer designed for **$50\text{ Hz}$** on a **$60\text{ Hz}$** system at its rated voltage is generally safe and offers several operating advantages:

---

#### **1. Reduction in Maximum Core Flux Density ($B_m$)**
From $B_m \propto \frac{V}{f}$, with voltage $V$ held constant and frequency increased from $50\text{ Hz}$ to $60\text{ Hz}$:
$$B_{m(60)} = B_{m(50)} \times \left(\frac{50}{60}\right) = 0.833 \, B_{m(50)}$$
The maximum core flux density decreases by **$16.7\%$**.

---

#### **2. Substantial Decrease in Magnetizing Current ($I_\mu$)**
- Because the core flux density $B_m$ is reduced, the core operates well below its magnetic saturation knee, well into the linear region of the magnetization curve.
- The magnetizing current $I_\mu$ drops noticeably, improving the no-load power factor.

---

#### **3. Reduction in Total Core (Iron) Losses**
- **Hysteresis Loss ($W_h$):**
  $$W_h \propto B_m^{1.6} f \propto \left(\frac{V}{f}\right)^{1.6} f \propto V^{1.6} f^{-0.6}$$
  $$W_{h(60)} = W_{h(50)} \times \left(\frac{50}{60}\right)^{0.6} = 0.896 \, W_{h(50)}$$
  Hysteresis loss decreases by about **$10.4\%$**.
- **Eddy Current Loss ($W_e$):**
  $$W_e \propto B_m^2 f^2 \propto \left(\frac{V}{f}\right)^2 f^2 \propto V^2$$
  Eddy current loss remains constant since applied voltage is unchanged.
- **Total Iron Loss ($W_i = W_h + W_e$):** Decreases overall, meaning the transformer operates **cooler** at no-load.

---

#### **4. Output kVA Rating and Efficiency**
- Lower core losses and reduced magnetizing current result in higher overall operational efficiency.
- Because of lower total thermal stress, the transformer can safely carry its full rated kVA without overheating (and can even deliver up to $10\%\text{ to }15\%$ higher kVA capacity if secondary voltage is adjusted proportionately).

---

#### **5. Increase in Leakage Reactance & Voltage Drop**
- The leakage reactance of the windings increases linearly with frequency:
  $$X_L = 2\pi f L \propto f$$
  $$X_{L(60)} = 1.20 \, X_{L(50)}$$
- The inductive reactance increases by **$20\%$**, causing a slightly larger internal reactive voltage drop ($I X_L$) under lagging power factor loads, which results in slightly higher percentage voltage regulation.

---

### 12. Page 40, Q.1(a): Does transformer draw any current when secondary is open? Why? Derive the emf equation of single phase transformer

#### **Part 1: Current Drawn on No-Load and Reason**
**Yes**, a transformer draws a small current when its secondary winding is open-circuited. This current is known as the **No-Load Primary Current ($I_0$)**, and it typically constitutes about **$2\%\text{ to }10\%$** of the rated full-load primary current.

---

#### **Why does it draw current?**
Even with the secondary circuit open (secondary current $I_2 = 0$), the primary winding remains connected across the alternating voltage supply $V_1$. The primary must draw $I_0$ to perform two functions:

1. **Magnetizing Component ($I_\mu$):**
   - It sets up and sustains the required alternating magnetic flux $\Phi$ in the high-permeability iron core.
   - It is in phase with the core flux $\Phi$ and lags behind the applied voltage $V_1$ by $90^\circ$ (wattless or reactive component):
     $$I_\mu = I_0 \sin \phi_0$$

2. **Active or Working Component ($I_w$ or $I_c$):**
   - It supplies the power needed to overcome **iron/core losses** (hysteresis loss and eddy current loss in the laminated core) along with a negligible amount of no-load primary copper loss ($I_0^2 R_1$).
   - It is in phase with the applied voltage $V_1$ (wattful component):
     $$I_w = I_0 \cos \phi_0$$

The total no-load current is the phasor sum of these two perpendicular components:
$$I_0 = \sqrt{I_w^2 + I_\mu^2}$$

```
                V₁ (Applied Voltage)
                 ▲
                 │
                 │ \
                 │  \
              Iw ┼───\ I₀
                 │ θ₀ \
                 │     \
                 └──────┼──────────► Φ (Core Flux)
                        │
                        │ Iμ
```

---

#### **Part 2: Derivation of the E.M.F. Equation of a Single-Phase Transformer**

Let:
- $N_1 =$ Number of primary turns
- $N_2 =$ Number of secondary turns
- $\Phi_m =$ Maximum value of magnetic flux in the core in Webers ($\text{Wb}$)
- $f =$ Frequency of the A.C. supply in Hertz ($\text{Hz}$)
- $B_m =$ Peak magnetic flux density in $\text{Wb/m}^2$
- $A =$ Net cross-sectional area of the core in $\text{m}^2$ ($\Phi_m = B_m \times A$)

---

#### **1. Rate of Change of Flux:**
In a sinusoidal wave of frequency $f$, the time period of one complete cycle is $T = \frac{1}{f}\text{ seconds}$.

The flux changes from zero to its maximum positive value $\Phi_m$ in **one quarter of a cycle**:
$$\text{Time taken, } \Delta t = \frac{T}{4} = \frac{1}{4f}\text{ s}$$

$$\text{Average rate of change of flux} = \frac{\Delta \Phi}{\Delta t} = \frac{\Phi_m}{1/(4f)} = 4 f \Phi_m \text{ Wb/s (or Volts)}$$

---

#### **2. Induced E.M.F. per Turn:**
By Faraday's Law, the average e.m.f. induced in each turn is equal to the average rate of change of flux:
$$\text{Average e.m.f. per turn} = 4 f \Phi_m \text{ Volts}$$

For a sinusoidal alternating waveform, the Form Factor is:
$$\text{Form Factor} = \frac{\text{R.M.S. Value}}{\text{Average Value}} = 1.11$$

$$\text{R.M.S. value of e.m.f. per turn} = 1.11 \times 4 f \Phi_m = 4.44 f \Phi_m \text{ Volts}$$

---

#### **3. Total Induced E.M.F. in Primary and Secondary Windings:**
- **In Primary Winding ($N_1$ turns):**
  $$E_1 = (\text{R.M.S. e.m.f./turn}) \times N_1$$
  $$E_1 = 4.44 f N_1 \Phi_m = 4.44 f N_1 B_m A \text{ Volts}$$

- **In Secondary Winding ($N_2$ turns):**
  $$E_2 = (\text{R.M.S. e.m.f./turn}) \times N_2$$
  $$E_2 = 4.44 f N_2 \Phi_m = 4.44 f N_2 B_m A \text{ Volts}$$

This is the standard **E.M.F. Equation of a Transformer**.

### 13. Page 40, Q.1(c): A single phase transformer has 1000 turns on the primary and 200 turns on the secondary. The no load current is 3 amp at a pf of 0.2 lagging. Calculate the primary current and power factor when the secondary current is 280 amp at a p.f of 0.80 lagging.

#### **Given Data:**
- Primary turns, $N_1 = 1000$
- Secondary turns, $N_2 = 200$
- No-load current, $I_0 = 3\text{ A}$
- No-load power factor, $\cos \phi_0 = 0.2\text{ lagging}$
- Secondary load current, $I_2 = 280\text{ A}$
- Secondary load power factor, $\cos \phi_2 = 0.80\text{ lagging}$

---

#### **Step-by-Step Solution:**

1. **Transformation Ratio ($K$):**
   $$K = \frac{N_2}{N_1} = \frac{200}{1000} = 0.2 = \frac{1}{5}$$

2. **Secondary Current Referred to Primary ($I_2'$):**
   $$I_2' = K \times I_2 = \frac{1}{5} \times 280 = 56\text{ A}$$

3. **Phase Angles:**
   - For no-load current:
     $$\phi_0 = \cos^{-1}(0.2) = 78.46^\circ \approx 78.5^\circ$$
     $$\sin \phi_0 = \sqrt{1 - (0.2)^2} = \sqrt{1 - 0.04} = \sqrt{0.96} \approx 0.9798$$
   
   - For secondary load current:
     $$\phi_2 = \cos^{-1}(0.80) = 36.87^\circ$$
     $$\sin \phi_2 = \sqrt{1 - (0.8)^2} = 0.60$$

---

4. **Resolution into Rectangular Components (Taking Voltage Vector as Reference):**

   - **No-load current phasor ($\vec{I}_0$):**
     $$\vec{I}_0 = I_0 \cos \phi_0 - j I_0 \sin \phi_0$$
     $$\vec{I}_0 = 3(0.2) - j 3(0.9798) = 0.6 - j 2.94\text{ A}$$

   - **Reflected load current phasor ($\vec{I}_2'$):**
     $$\vec{I}_2' = I_2' \cos \phi_2 - j I_2' \sin \phi_2$$
     $$\vec{I}_2' = 56(0.80) - j 56(0.60) = 44.8 - j 33.6\text{ A}$$

---

5. **Total Primary Current ($\vec{I}_1$):**
   The total primary current is the phasor sum of the no-load current and the reflected secondary load current:
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$$
   $$\vec{I}_1 = (0.6 - j 2.94) + (44.8 - j 33.6)$$
   $$\vec{I}_1 = (0.6 + 44.8) - j (2.94 + 33.6) = 45.4 - j 36.54\text{ A}$$

---

6. **Magnitude of Primary Current ($I_1$):**
   $$I_1 = \sqrt{(45.4)^2 + (-36.54)^2} = \sqrt{2061.16 + 1335.17} = \sqrt{3396.33} \approx \mathbf{58.28\text{ A}}$$

---

7. **Primary Power Factor ($\cos \phi_1$):**
   $$\tan \phi_1 = \frac{36.54}{45.4} = 0.8048 \implies \phi_1 = \tan^{-1}(0.8048) = 38.83^\circ$$
   $$\text{Primary Power Factor} = \cos \phi_1 = \cos(38.83^\circ) = \mathbf{0.779\text{ lagging (or } 0.78\text{ lagging)}}$$

---

### 15. Page 7, Q.1(a): Draw the vector diagram of a 1-φ transformer connected with unity p.f., lagging p.f., and leading p.f load. [Figure Involved]

When a single-phase transformer is loaded, the secondary current $I_2$ flows and sets up a demagnetizing m.m.f. $N_2 I_2$. To neutralize this, the primary draws an additional load current $I_2' = K I_2$ in exact phase opposition to $I_2$. The total primary current is $\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$.

---

#### **1. Phasor Diagram for Unity Power Factor Load ($\cos \phi_2 = 1$):**
- Secondary current $I_2$ is in phase with secondary terminal voltage $V_2$ ($\phi_2 = 0^\circ$).

```
                 V₁ (Applied Voltage)
                  ▲
                  │  / I₁ (Primary Current)
           -E₁ ───┼─/
                  │/
            I₂' ◄─┼───► I₀ (No-load current)
                  │
        ──────────┼──────────► Φ (Mutual Core Flux)
                  │
                  │
             E₂ ──┼──► V₂, I₂ (Secondary side in phase)
                  ▼
```

---

#### **2. Phasor Diagram for Lagging Power Factor Load ($\cos \phi_2\text{ lagging, Inductive Load}$):**
- Secondary current $I_2$ lags secondary voltage $V_2$ by angle $\phi_2$.
- Primary reflected current $I_2'$ is in anti-phase to $I_2$.

```
                 V₁
                  ▲
                  │   / I₁
           -E₁ ───┼──/
                  │ /
            I₂' ◄─┼/───► I₀
             \    │
              \   │
        ───────\──┼──────────► Φ
                \ │
                 \│  ▲ V₂
             E₂ ──┼─/
                  │/  (Lags by φ₂)
                  ▼ I₂
```

---

#### **3. Phasor Diagram for Leading Power Factor Load ($\cos \phi_2\text{ leading, Capacitive Load}$):**
- Secondary current $I_2$ leads secondary voltage $V_2$ by angle $\phi_2$.
- Primary reflected current $I_2'$ leads in anti-phase.

```
                 V₁
                  ▲
             I₂'  │  / I₁
              \   │ /
               \──┼/───► I₀
           -E₁ ───┼
                  │
        ──────────┼──────────► Φ
                  │   / I₂ (Leads by φ₂)
                  │  /
             E₂ ──┼─/──► V₂
                  ▼
```

---

### 16. Page 17, Q.2(b): Draw the on-load phasor diagram of a practical transformer with capacitive load. [Figure Involved]

For a **practical transformer** supplying a **capacitive (leading p.f.) load**, the effects of primary winding resistance $R_1$, primary leakage reactance $X_1$, secondary winding resistance $R_2$, and secondary leakage reactance $X_2$ are fully taken into account.

---

#### **Phasor Equations:**
1. **Secondary Side:**
   $$\vec{E}_2 = \vec{V}_2 + \vec{I}_2 R_2 + j \vec{I}_2 X_2 = \vec{V}_2 + \vec{I}_2 Z_2$$
   *(Since $I_2$ leads $V_2$, the reactive drop $j I_2 X_2$ can cause the terminal voltage $V_2$ to be higher than induced e.m.f. $E_2$.)*

2. **Primary Current:**
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2' \quad \text{where } \vec{I}_2' = -K \vec{I}_2$$

3. **Primary Applied Voltage:**
   $$\vec{V}_1 = -\vec{E}_1 + \vec{I}_1 R_1 + j \vec{I}_1 X_1 = -\vec{E}_1 + \vec{I}_1 Z_1$$

---

#### **Complete On-Load Phasor Diagram (Capacitive / Leading Load):**

```
                         V₁ ◄────────────────┐ (j I₁X₁)
                         ▲                  /
                         │                 / (I₁R₁)
                         │  / I₁          /
                  -E₁ ───┼─/─────────────┘
                    \    │/
                I₂'  \   ┼────► I₀
                      \  │
        ───────────────\─┼──────────────► Φ (Core Flux)
                        \│       / I₂ (Leads V₂ by φ₂)
                         │      /
                         │     /
                         │    /   ┌────► V₂
                         │   /   /    /
                         │  /   /    / (j I₂X₂)
                    E₂ ──┼─/───┴────┘ (I₂R₂)
                         ▼
```

---

#### **Description of Phasor Quantities:**
- $\Phi =$ Mutual magnetic flux vector chosen along the horizontal axis.
- $E_1, E_2 =$ Induced e.m.f. in primary and secondary windings, both lagging the flux $\Phi$ by $90^\circ$.
- $-E_1 =$ Equal and opposite counter e.m.f. vector required on the primary side.
- $V_2 =$ Secondary terminal voltage.
- $I_2 =$ Secondary load current leading $V_2$ by angle $\phi_2$.
- $I_2 R_2 =$ Resistive voltage drop in secondary in phase with $I_2$.
- $I_2 X_2 =$ Reactive voltage drop in secondary leading $I_2$ by $90^\circ$.
- $I_0 =$ No-load current comprising magnetizing current $I_\mu$ (in phase with $\Phi$) and core loss current $I_w$ (in phase with $-E_1$).
- $I_2' =$ Secondary current reflected to primary, drawn $180^\circ$ out of phase with $I_2$.
- $I_1 =$ Vector sum of $I_0$ and $I_2'$.
- $I_1 R_1 =$ Resistive voltage drop in primary in phase with $I_1$.
- $I_1 X_1 =$ Reactive voltage drop in primary leading $I_1$ by $90^\circ$.
- $V_1 =$ Total primary applied voltage obtained by adding drops $I_1 R_1$ and $j I_1 X_1$ to $-E_1$.

---

### 17. Page 18, Q.1(c): Draw the possible vector diagrams of a transformer for different types of load. [Figure Involved]

A practical transformer on load has internal winding resistances ($R_1, R_2$) and leakage reactances ($X_1, X_2$). The phasor relationships differ depending on the type of load connected to the secondary:

---

#### **Case 1: Non-Inductive Load (Resistive Load, Unity Power Factor, $\cos \phi_2 = 1$)**
- $\vec{I}_2$ is in phase with $\vec{V}_2$.
- Drop $\vec{I}_2 R_2$ is parallel to $\vec{I}_2$, and $\vec{I}_2 X_2$ leads $\vec{I}_2$ by $90^\circ$.

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                       │  / I₁        /
                -E₁ ───┼─/───────────┘
                       │/
                 I₂' ◄─┼───► I₀
                       │
      ─────────────────┼────────────────► Φ
                       │
                       │          ┌─────► V₂
                       │          │    / (j I₂X₂)
                  E₂ ──┼──────────┴───┘ (I₂R₂)
                       ▼           ► I₂ (In phase with V₂)
```

---

#### **Case 2: Inductive Load (Lagging Power Factor, $\cos \phi_2\text{ lagging}$)**
- $\vec{I}_2$ lags secondary terminal voltage $\vec{V}_2$ by phase angle $\phi_2$.
- The secondary terminal voltage $V_2$ drops significantly below $E_2$ due to both $I_2 R_2$ and $I_2 X_2$.

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                       │   / I₁       /
                -E₁ ───┼──/──────────┘
                       │ /
                 I₂' ◄─┼/────► I₀
                  \    │
      ─────────────\───┼────────────────► Φ
                    \  │
                     \ │   ▲ V₂
                  E₂ ─\┼──/  (Lags by φ₂)
                       ▼ /
                        ▼ I₂ ──► I₂R₂ ──► j I₂X₂
```

---

#### **Case 3: Capacitive Load (Leading Power Factor, $\cos \phi_2\text{ leading}$)**
- $\vec{I}_2$ leads secondary terminal voltage $\vec{V}_2$ by phase angle $\phi_2$.
- The reactive drop $j I_2 X_2$ is directed such that $V_2$ can exceed the induced e.m.f. $E_2$ (negative voltage regulation).

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                  I₂'  │  / I₁        /
                   \   │ /           /
                    \──┼/───────────┘
                -E₁ ───┼─────► I₀
                       │
      ─────────────────┼────────────────► Φ
                       │    / I₂ (Leads V₂ by φ₂)
                       │   /
                       │  /     ┌─────► V₂
                  E₂ ──┼─/──────┴────┘ (j I₂X₂)
                       ▼       (I₂R₂)
```

---

#### **Summary of Mathematical Phasor Relationships for all cases:**
$$\vec{E}_2 = \vec{V}_2 + \vec{I}_2(R_2 + jX_2)$$
$$\vec{I}_1 = \vec{I}_0 + \vec{I}_2' = \vec{I}_0 + (-K \vec{I}_2)$$
$$\vec{V}_1 = -\vec{E}_1 + \vec{I}_1(R_1 + jX_1)$$

### 18. Page 23, Q.8: Sketch the phasor diagram of an ideal transformer with no-load conditions. [Figure Involved]

#### **Characteristics of an Ideal Transformer on No-Load:**
An ideal transformer possesses the following ideal properties:
1. **Zero Winding Resistance:** The primary and secondary coils have zero resistance ($R_1 = 0, R_2 = 0$), meaning there are no copper losses ($I^2R = 0$).
2. **Lossless Magnetic Core:** The core has infinite permeability ($\mu \to \infty$) and zero core loss (zero hysteresis and eddy current losses).
3. **Zero Magnetic Leakage:** All magnetic flux $\Phi$ is completely confined within the core and links both windings ($X_1 = 0, X_2 = 0$).
4. **Purely Inductive Behavior:** Because the secondary is open-circuited ($I_2 = 0$), the primary winding acts as a pure inductance. It draws only a wattless **magnetizing current ($I_\mu$)** to establish the core flux $\Phi$.

---

#### **Phasor Relationships:**
- The magnetizing current $I_\mu$ lags the applied primary voltage $V_1$ by exactly $90^\circ$.
- The alternating flux $\Phi$ is in phase with the magnetizing current $I_\mu$.
- The induced e.m.f. in the primary winding ($E_1$) and secondary winding ($E_2$) lag behind the core flux $\Phi$ by $90^\circ$ (by Faraday's Law: $e = -N \frac{d\Phi}{dt}$).
- Hence, $E_1$ and $E_2$ are in phase with each other and are directly $180^\circ$ out of phase with the applied voltage $V_1$ (i.e., $V_1 = -E_1$).
- On no-load, the secondary terminal voltage $V_2$ is equal to $E_2$.

---

#### **Phasor Diagram of an Ideal Transformer on No-Load:**

```
                        V₁ (Applied Voltage)
                         ▲
                         │
                         │
                         │
                         │       90°
     ────────────────────┼────────────────► Φ (Mutual Core Flux), Iμ (Magnetizing Current)
                         │
                         │       90°
                         │
                         │
                         ▼ E₁ (Primary Induced EMF)
                         ▼ E₂, V₂ (Secondary Induced EMF & Terminal Voltage)
```

---

### 19. Page 23, Q.13: Describe a practical transformer on no-load with net phasor diagram. [Figure Involved]

#### **Description of Practical Transformer on No-Load:**
When a practical transformer is on no-load (secondary winding open-circuited), its primary current is not purely reactive because real power is required to supply the internal core losses.

The primary draws a small **no-load current ($I_0$)**, which usually ranges between **$2\%\text{ to }10\%$** of the rated full-load current. This current lags the applied primary voltage $V_1$ by an angle $\phi_0 < 90^\circ$ (typical no-load power factor $\cos \phi_0 \approx 0.2\text{ to }0.35$).

---

#### **Components of No-Load Current ($I_0$):**

```
                 V₁ (Primary Voltage)
                  ▲
                  │\
                  │ \
               Iw ┼──\ I₀ (No-load Current)
                  │ φ₀\
                  │    \
    ──────────────┴─────┼─────────────► Φ (Core Flux)
                        │
                        │ Iμ
                        │
                        ▼ E₁
                        ▼ E₂
```

The no-load primary current $I_0$ is resolved into two mutually perpendicular components:

1. **Active / Working / Core-Loss Component ($I_w$ or $I_c$):**
   - It is in phase with the applied primary voltage $V_1$.
   - It supplies the **iron losses** (hysteresis and eddy current losses) in the core and a negligible primary copper loss:
     $$I_w = I_0 \cos \phi_0$$
     $$\text{No-load power input, } W_0 = V_1 I_0 \cos \phi_0 \approx \text{Iron Loss } W_i$$

2. **Magnetizing Component ($I_\mu$ or $I_m$):**
   - It is in phase with the core magnetic flux $\Phi$ and in quadrature ($90^\circ$ lagging) with the applied voltage $V_1$.
   - It sustains the alternating magnetic flux in the core:
     $$I_\mu = I_0 \sin \phi_0$$

The total no-load current is the vector sum:
$$\vec{I}_0 = \vec{I}_w + \vec{I}_\mu \implies I_0 = \sqrt{I_w^2 + I_\mu^2}$$
$$\text{No-load power factor, } \cos \phi_0 = \frac{I_w}{I_0} = \frac{W_0}{V_1 I_0}$$

---

### 20. Page 23, Q.14: Describe a practical transformer on load with no winding resistance and leakage flux. Also draw the phasor diagrams with resistive load, inductive load and capacitive load on those conditions. [Figure Involved]

#### **Description:**
Here, we consider a transformer that has magnetic core losses and magnetizing current ($I_0 \neq 0$), but its winding resistances and magnetic leakage reactances are assumed to be zero ($R_1 = R_2 = 0$ and $X_1 = X_2 = 0$).

1. **Core Action Under Load:**
   - When a load is connected to the secondary, a secondary current $I_2$ flows, creating a demagnetizing secondary m.m.f. $N_2 I_2$.
   - This tends to reduce the mutual core flux $\Phi$.
   - To counteract this demagnetizing effect and keep the main core flux constant at its no-load value, the primary winding immediately draws an additional load current $I_2'$ (reflected secondary current) from the supply such that:
     $$N_1 I_2' = N_2 I_2 \implies I_2' = \left(\frac{N_2}{N_1}\right) I_2 = K I_2$$
   - This current $I_2'$ is in direct phase opposition ($180^\circ$ out of phase) to $I_2$.
2. **Total Primary Current:**
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$$
3. **Terminal Voltages:**
   Because internal resistance and leakage drops are zero:
   $$V_1 = -E_1 \quad \text{and} \quad V_2 = E_2$$

---

#### **Phasor Diagrams Under Different Load Conditions:**

#### **(a) Resistive Load (Unity Power Factor, $\cos \phi_2 = 1$):**
- Secondary current $I_2$ is in phase with $V_2$ ($E_2$).
- Reflected current $I_2'$ is in phase with $-E_1$ ($V_1$).

```
                 V₁ = -E₁
                  ▲
                  │  / I₁ = I₀ + I₂'
            I₂' ◄─┼─/
                  │/
                  ┼────► I₀
                  │
     ─────────────┼──────────────► Φ
                  │
                  │
                  ▼ E₂ = V₂, I₂
```

---

#### **(b) Inductive Load (Lagging Power Factor, $\cos \phi_2\text{ lagging}$):**
- $I_2$ lags $V_2$ ($E_2$) by load angle $\phi_2$.
- $I_2'$ leads in anti-phase to $I_2$.

```
                 V₁ = -E₁
                  ▲
                  │   / I₁
            I₂' ◄─┼──/
             \    │ /
              \   ┼/────► I₀
               \  │
     ───────────\─┼──────────────► Φ
                 \│  ▲ V₂ = E₂
                  │ /
                  ▼/  (Lags by φ₂)
                   I₂
```

---

#### **(c) Capacitive Load (Leading Power Factor, $\cos \phi_2\text{ leading}$):**
- $I_2$ leads $V_2$ ($E_2$) by load angle $\phi_2$.
- $I_2'$ is reflected in anti-phase.

```
                 V₁ = -E₁
                  ▲
             I₂'  │  / I₁
              \   │ /
               \──┼/────► I₀
                  │
     ─────────────┼──────────────► Φ
                  │   / I₂ (Leads by φ₂)
                  │  /
                  ▼─/──► V₂ = E₂
```

---

### 21. Page 23, Q.15: Describe a practical transformer on load with winding resistance and leakage flux. Also draw the phasor diagrams with resistive load, inductive load and capacitive load on those conditions. [Figure Involved]

#### **Description:**
In an actual practical transformer, the windings possess both finite ohmic resistance and magnetic leakage flux:
- **Primary Resistance ($R_1$) and Leakage Reactance ($X_1$):** Cause a primary voltage drop $\vec{I}_1(R_1 + jX_1) = \vec{I}_1 Z_1$.
- **Secondary Resistance ($R_2$) and Leakage Reactance ($X_2$):** Cause a secondary internal voltage drop $\vec{I}_2(R_2 + jX_2) = \vec{I}_2 Z_2$.

---

#### **Governing Vector Equations:**
1. **Secondary Terminal Voltage:**
   $$\vec{E}_2 = \vec{V}_2 + \vec{I}_2 R_2 + j \vec{I}_2 X_2 = \vec{V}_2 + \vec{I}_2 Z_2$$
   $$\vec{V}_2 = \vec{E}_2 - \vec{I}_2 R_2 - j \vec{I}_2 X_2$$

2. **Primary Line Current:**
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2' \quad \text{where } \vec{I}_2' = -K \vec{I}_2$$

3. **Primary Applied Voltage:**
   $$\vec{V}_1 = -\vec{E}_1 + \vec{I}_1 R_1 + j \vec{I}_1 X_1 = -\vec{E}_1 + \vec{I}_1 Z_1$$

---

#### **Phasor Diagrams:**

#### **1. Non-Inductive Load (Resistive, Unity Power Factor):**
- $I_2$ is drawn in phase with terminal voltage $V_2$.
- Secondary drop $I_2 R_2$ is parallel to $I_2$, and $I_2 X_2$ leads $I_2$ by $90^\circ$.

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                       │  / I₁        /
                -E₁ ───┼─/───────────┘
                       │/
                 I₂' ◄─┼───► I₀
                       │
      ─────────────────┼────────────────► Φ
                       │
                       │          ┌─────► V₂
                       │          │    / (j I₂X₂)
                  E₂ ──┼──────────┴───┘ (I₂R₂)
                       ▼           ► I₂ (In phase with V₂)
```

---

#### **2. Inductive Load (Lagging Power Factor):**
- $I_2$ lags $V_2$ by $\phi_2$.
- $I_2 R_2$ is parallel to $I_2$, $j I_2 X_2$ is perpendicular (leading $I_2$ by $90^\circ$).

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                       │   / I₁       /
                -E₁ ───┼──/──────────┘
                       │ /
                 I₂' ◄─┼/────► I₀
                  \    │
      ─────────────\───┼────────────────► Φ
                    \  │
                     \ │   ▲ V₂
                  E₂ ─\┼──/  (Lags by φ₂)
                       ▼ /
                        ▼ I₂ ──► I₂R₂ ──► j I₂X₂
```

---

#### **3. Capacitive Load (Leading Power Factor):**
- $I_2$ leads $V_2$ by $\phi_2$.
- The reactive drop vector adds such that the terminal voltage $V_2$ may exceed induced e.m.f. $E_2$.

```
                       V₁ ◄─────────────┐ (j I₁X₁)
                       ▲               / (I₁R₁)
                  I₂'  │  / I₁        /
                   \   │ /           /
                    \──┼/───────────┘
                -E₁ ───┼─────► I₀
                       │
      ─────────────────┼────────────────► Φ
                       │    / I₂ (Leads V₂ by φ₂)
                       │   /
                       │  /     ┌─────► V₂
                  E₂ ──┼─/──────┴────┘ (j I₂X₂)
                       ▼       (I₂R₂)
```
### 22. Page 28, Q.No.1: Draw the vector diagram of a loaded transformer with resistance and magnetic leakage, assuming lagging p.f. [Figure Involved]

#### **Description:**
When a practical transformer supplies an inductive load (lagging power factor $\cos \phi_2$), the secondary current $I_2$ lags behind the secondary terminal voltage $V_2$ by the phase angle $\phi_2$. 

The transformer has:
- Primary winding resistance $R_1$ and primary leakage reactance $X_1$
- Secondary winding resistance $R_2$ and secondary leakage reactance $X_2$
- Core-loss resistance $R_0$ and magnetizing reactance $X_0$

---

#### **Vector Equations:**
1. **Secondary Induced E.M.F. ($\vec{E}_2$):**
   $$\vec{E}_2 = \vec{V}_2 + \vec{I}_2 R_2 + j\vec{I}_2 X_2$$
   - $\vec{I}_2 R_2$ is the resistive voltage drop in phase with $\vec{I}_2$.
   - $j\vec{I}_2 X_2$ is the reactive voltage drop leading $\vec{I}_2$ by $90^\circ$.

2. **Primary Current ($\vec{I}_1$):**
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$$
   - $\vec{I}_0 = \vec{I}_w + \vec{I}_\mu$ (no-load current).
   - $\vec{I}_2' = -K\vec{I}_2$ (secondary load current reflected onto primary, drawn $180^\circ$ out of phase with $\vec{I}_2$).

3. **Primary Applied Voltage ($\vec{V}_1$):**
   $$\vec{V}_1 = -\vec{E}_1 + \vec{I}_1 R_1 + j\vec{I}_1 X_1$$
   - $-\vec{E}_1$ is the voltage required to overcome the primary counter e.m.f.
   - $\vec{I}_1 R_1$ is the primary resistive drop drawn parallel to $\vec{I}_1$.
   - $j\vec{I}_1 X_1$ is the primary reactive drop drawn perpendicular (leading $\vec{I}_1$ by $90^\circ$).

---

#### **Vector Diagram (Lagging Power Factor):**

```
                            V₁ ◄────────────────┐ (j I₁X₁)
                            ▲                  /
                            │                 / (I₁R₁)
                            │   / I₁         /
                     -E₁ ───┼──/────────────┘
                            │ /
                      I₂' ◄─┼/────► I₀
                       \    │
     ───────────────────\───┼────────────────► Φ (Mutual Core Flux)
                         \  │
                          \ │   ▲ V₂
                       E₂ ─\┼──/  (Lags by φ₂)
                            ▼ /
                             ▼ I₂ ────► I₂R₂ ────► j I₂X₂
```

---

### 23. Page 36, Q.2(a): Draw the full load phasor diagram and explain why an increase in load current causes an increase in primary current in a transformer. [Figure Involved]

#### **1. Full Load Phasor Diagram (Lagging Load):**

```
                            V₁ ◄────────────────┐ (j I₁X₁)
                            ▲                  /
                            │                 / (I₁R₁)
                            │   / I₁         /
                     -E₁ ───┼──/────────────┘
                            │ /
                      I₂' ◄─┼/────► I₀
                       \    │
     ───────────────────\───┼────────────────► Φ (Core Flux)
                         \  │
                          \ │   ▲ V₂
                       E₂ ─\┼──/  (Lags by φ₂)
                            ▼ /
                             ▼ I₂ ────► I₂R₂ ────► j I₂X₂
```

---

#### **2. Why an Increase in Load Current Causes an Increase in Primary Current:**

A transformer operates as a self-regulating magnetic device that automatically balances primary power input with secondary power demand. The step-by-step physical process occurs as follows:

```
 Load Demand Increases (I₂ ↑)
           │
           ▼
 Demagnetizing M.M.F. Produced (N₂ I₂ ↑)
           │
           ▼
 Mutual Core Flux Momentarily Reduced (Φ ↓)
           │
           ▼
 Primary Back E.M.F. Decreases Slightly (E₁ ↓)
           │
           ▼
 Net Primary Driving Voltage Increases (V₁ - E₁ ↑)
           │
           ▼
 Primary Draws Additional Current (I₂' = K I₂ ↑)
           │
           ▼
 Balancing M.M.F. Created (N₁ I₂' = N₂ I₂), Flux Restored (Φ = Constant)
           │
           ▼
 Total Primary Current Increases: Ī₁ = Ī₀ + Ī₂'
```

1. **Initial Steady State on No-Load:**
   With the secondary circuit open, the primary draws only the small no-load current $I_0$. This current sets up the working core flux $\Phi$, which induces a primary back e.m.f. $E_1$ almost exactly equal and opposite to the applied voltage $V_1$ ($V_1 \approx -E_1$).

2. **Demagnetizing Effect of Load Current:**
   When a load is connected across the secondary terminals, secondary current $I_2$ flows through the $N_2$ secondary turns, setting up a **secondary demagnetizing m.m.f.** ($N_2 I_2$). According to Lenz's law, this m.m.f. directly opposes the main core flux $\Phi$.

3. **Momentary Reduction of Core Flux ($\Phi$) and Back E.M.F. ($E_1$):**
   The opposing m.m.f. momentarily weakens the mutual core flux $\Phi$. Since primary induced back e.m.f. is proportional to flux ($E_1 = 4.44 f N_1 \Phi$), $E_1$ decreases slightly.

4. **Surge in Primary Current ($I_2'$):**
   The primary current is governed by:
   $$\vec{I}_1 = \frac{\vec{V}_1 - \vec{E}_1}{\vec{Z}_1}$$
   Because the internal impedance $Z_1$ is very small, even a minute reduction in $E_1$ creates a significant net voltage difference $(V_1 - E_1)$, causing the primary winding to immediately draw an additional load component current $I_2'$ from the supply.

5. **Restoration of Mutual Flux Equilibrium:**
   This additional primary current $I_2'$ produces a primary m.m.f. ($N_1 I_2'$) that is equal in magnitude and opposite in direction to the secondary m.m.f. ($N_2 I_2$):
   $$N_1 I_2' = N_2 I_2 \implies I_2' = \left(\frac{N_2}{N_1}\right) I_2 = K I_2$$
   The primary load m.m.f. completely cancels out the demagnetizing secondary m.m.f., thereby maintaining the main core flux $\Phi$ virtually constant at all load levels.

6. **Conclusion:**
   As the secondary load current $I_2$ increases, $I_2'$ increases proportionately, which in turn increases the total primary current $\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$.

---

### 25. Page 7, Q.2(a): Prove that R02 = R2 + k^2 R1, where the symbols have their usual meaning.

#### **Proof:**

Let:
- $R_1 =$ Resistance of the primary winding
- $R_2 =$ Resistance of the secondary winding
- $I_1 =$ Primary full-load current
- $I_2 =$ Secondary full-load current
- $K =$ Voltage transformation ratio $= \frac{N_2}{N_1} \approx \frac{E_2}{E_1} \approx \frac{I_1}{I_2}$
- $R_1' =$ Equivalent primary resistance referred to the secondary side
- $R_{02} =$ Total equivalent resistance of the transformer referred to the secondary side

---

#### **Step 1: Equating Copper Losses**
When the primary resistance $R_1$ is transferred to the secondary side, its equivalent value $R_1'$ must cause the exact same copper loss when carrying the secondary current $I_2$ as the actual resistance $R_1$ causes when carrying the primary current $I_1$.

$$\text{Copper loss produced by } R_1' \text{ in secondary} = \text{Copper loss produced by } R_1 \text{ in primary}$$
$$I_2^2 R_1' = I_1^2 R_1$$

Solving for $R_1'$:
$$R_1' = \left(\frac{I_1}{I_2}\right)^2 R_1 \tag{1}$$

---

#### **Step 2: Substituting Transformation Ratio ($K$)**
Neglecting the small no-load current $I_0$, the current transformation relation gives:
$$\frac{I_1}{I_2} = K$$

Substituting this into Equation (1):
$$R_1' = K^2 R_1 \tag{2}$$

---

#### **Step 3: Total Equivalent Resistance Referred to Secondary ($R_{02}$)**
The total equivalent resistance referred to the secondary side ($R_{02}$) is the sum of the actual secondary winding resistance $R_2$ and the transferred primary resistance $R_1'$:

$$R_{02} = R_2 + R_1'$$
$$R_{02} = R_2 + K^2 R_1$$

*(Hence proved.)*

---

### 26. Page 9, Q.2(c): Draw the approximate equivalent circuit of a loaded transformer referred to primary. [Figure Involved]

#### **Description:**
In the **approximate equivalent circuit referred to the primary**, the parallel exciting branch (comprising core-loss resistance $R_0$ and magnetizing reactance $X_0$) is shifted across the input supply terminals $V_1$. 

This simplification is justified because the no-load current $I_0$ is very small ($2\%\text{ to }10\%$ of full-load current), so the voltage drop produced by $I_0$ across primary impedance $(R_1 + jX_1)$ is negligible.

---

#### **Parameters Referred to Primary Side:**
1. **Equivalent Resistance referred to Primary ($R_{01}$):**
   $$R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}$$
2. **Equivalent Leakage Reactance referred to Primary ($X_{01}$):**
   $$X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{K^2}$$
3. **Total Equivalent Impedance referred to Primary ($Z_{01}$):**
   $$Z_{01} = \sqrt{R_{01}^2 + X_{01}^2}$$
4. **Reflected Secondary Load Current ($I_2'$):**
   $$I_2' = K I_2$$
5. **Reflected Secondary Terminal Voltage ($V_2'$):**
   $$V_2' = \frac{V_2}{K}$$
6. **Reflected Load Impedance ($Z_L'$):**
   $$Z_L' = \frac{Z_L}{K^2}$$

---

#### **Approximate Equivalent Circuit Diagram (Referred to Primary):**

```
     I₁ ──►      R₀₁ = R₁ + R₂/K²     X₀₁ = X₁ + X₂/K²       I₂' ──►
      ───────┬────██████████───────────UUUUUUUU──────────────┬────────
             │                                               │
             │   I₀                                          │
             ├───►──┐                                        │
             │      │                                        │
             │   ┌──┴──┐                                   ┌─┴─┐
             │   │     │                                   │   │
        V₁   │  [R₀]  [X₀]                                 │Z'L│ V₂' = V₂/K
        ~    │   │     │                                   │   │
             │   └──┬──┘                                   └─┬─┘
             │      │                                        │
             │      │                                        │
      ───────┴──────┴────────────────────────────────────────┴────────
```


### 27. Page 17, Q.3(a): Construct the simplified equivalent circuit diagram of a 1-φ transformer. [Figure Involved]

#### **Explanation:**
In an exact equivalent circuit of a transformer, the parallel exciting branch (comprising core-loss resistance $R_0$ and magnetizing reactance $X_0$) is located between the primary and secondary series impedances. 

However, because the no-load current $I_0$ is very small (only $1\%\text{ to }3\%$ of the full-load primary current), the voltage drop across the primary series impedance $(R_1 + jX_1)$ caused by $I_0$ is negligible. Therefore, without introducing any serious error, the exciting branch can be shifted directly across the input supply terminals $V_1$. 

Furthermore, if the small no-load current $I_0$ is omitted entirely, the circuit simplifies into a single series impedance loop connected to the load.

---

#### **1. Approximate Equivalent Circuit (Referred to Primary):**

```
     I₁ ──►      R₀₁ = R₁ + R₂/K²     X₀₁ = X₁ + X₂/K²       I₂' ──►
      ───────┬────██████████───────────UUUUUUUU──────────────┬────────
             │                                               │
             │   I₀                                          │
             ├───►──┐                                        │
             │      │                                        │
             │   ┌──┴──┐                                   ┌─┴─┐
             │   │     │                                   │   │
        V₁   │  [R₀]  [X₀]                                 │Z'L│ V₂' = V₂/K
        ~    │   │     │                                   │   │
             │   └──┬──┘                                   └─┬─┘
             │      │                                        │
             │      │                                        │
      ───────┴──────┴────────────────────────────────────────┴────────
```

---

#### **2. Further Simplified Equivalent Circuit (Neglecting $I_0$):**

When no-load current $I_0$ is neglected ($I_1 \approx I_2'$):

```
     I₁ ≈ I₂' ──►       R₀₁                X₀₁
      ───────────────██████████──────────UUUUUUUU────────────┬────────
                                                             │
                                                           ┌─┴─┐
                                                           │   │
        V₁ ~                                               │Z'L│ V₂' = V₂/K
                                                           │   │
                                                           └─┬─┘
                                                             │
      ───────────────────────────────────────────────────────┴────────
```

---

#### **Key Circuit Parameter Formulas:**
- **Equivalent Primary Resistance:** $R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}$
- **Equivalent Primary Leakage Reactance:** $X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{K^2}$
- **Total Equivalent Primary Impedance:** $Z_{01} = \sqrt{R_{01}^2 + X_{01}^2}$
- **Referred Secondary Voltage:** $V_2' = \frac{V_2}{K}$
- **Referred Secondary Current:** $I_2' = K I_2$
- **Referred Load Impedance:** $Z_L' = \frac{Z_L}{K^2}$

---

### 28. Page 17, Q.3(b): Show that R01 = R1 + R2/k^2 and R02 = R2 + K^2R1 where the symbols have their usual meanings.

#### **Derivation:**

Let:
- $R_1 =$ Ohmic resistance of the primary winding
- $R_2 =$ Ohmic resistance of the secondary winding
- $I_1 =$ Primary full-load current
- $I_2 =$ Secondary full-load current
- $K =$ Voltage transformation ratio $= \frac{N_2}{N_1} \approx \frac{I_1}{I_2}$
- $R_2' =$ Secondary resistance referred to the primary side
- $R_1' =$ Primary resistance referred to the secondary side
- $R_{01} =$ Total equivalent resistance of the transformer referred to primary
- $R_{02} =$ Total equivalent resistance of the transformer referred to secondary

---

#### **Part 1: Proof for $R_{01} = R_1 + \frac{R_2}{K^2}$**
When the secondary winding resistance $R_2$ is transferred to the primary side, its equivalent resistance $R_2'$ must produce the same copper loss when carrying the primary current $I_1$ as the actual resistance $R_2$ produces when carrying the secondary current $I_2$:

$$\text{Copper loss in primary by } R_2' = \text{Copper loss in secondary by } R_2$$
$$I_1^2 R_2' = I_2^2 R_2$$

Solving for $R_2'$:
$$R_2' = \left(\frac{I_2}{I_1}\right)^2 R_2$$

Since $\frac{I_1}{I_2} = K \implies \frac{I_2}{I_1} = \frac{1}{K}$:
$$R_2' = \left(\frac{1}{K}\right)^2 R_2 = \frac{R_2}{K^2}$$

The total equivalent resistance referred to the primary side ($R_{01}$) is:
$$R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}$$

*(Hence proved.)*

---

#### **Part 2: Proof for $R_{02} = R_2 + K^2 R_1$**
When the primary winding resistance $R_1$ is transferred to the secondary side, its equivalent resistance $R_1'$ must produce the same copper loss when carrying the secondary current $I_2$ as the actual resistance $R_1$ produces when carrying the primary current $I_1$:

$$\text{Copper loss in secondary by } R_1' = \text{Copper loss in primary by } R_1$$
$$I_2^2 R_1' = I_1^2 R_1$$

Solving for $R_1'$:
$$R_1' = \left(\frac{I_1}{I_2}\right)^2 R_1$$

Substituting $\frac{I_1}{I_2} = K$:
$$R_1' = K^2 R_1$$

The total equivalent resistance referred to the secondary side ($R_{02}$) is:
$$R_{02} = R_2 + R_1' = R_2 + K^2 R_1$$

*(Hence proved.)*

---

#### **Relation Between $R_{01}$ and $R_{02}$:**
$$R_{02} = K^2 \left(R_1 + \frac{R_2}{K^2}\right) = K^2 R_{01}$$

---

### 29. Page 17, Q.2(a) (lower half): Explain why an increase in secondary current causes an increase in primary current in a transformer.

A transformer operates on the principle of magnetic balance, which automatically maintains a constant working core flux $\Phi$ irrespective of load variations. The physical mechanism operates through the following steps:

```
 Secondary Current Increases (I₂ ↑)
               │
               ▼
 Opposing M.M.F. Produced: (N₂ I₂)
               │
               ▼
 Main Core Flux Momentarily Decreases (Φ ↓)
               │
               ▼
 Primary Induced Back E.M.F. Decreases (E₁ ↓)
               │
               ▼
 Voltage Difference (V₁ - E₁) Increases
               │
               ▼
 Primary Draws Counter-Balancing Current: I₂' = (N₂/N₁) · I₂ = K I₂
               │
               ▼
 Opposing M.M.F.s Cancel: (N₁ I₂' = N₂ I₂) ──► Flux Φ Restored
               │
               ▼
 Total Primary Current Increases: Ī₁ = Ī₀ + Ī₂'
```

---

#### **Step-by-Step Explanation:**

1. **Equilibrium at No-Load:**
   On no-load ($I_2 = 0$), the primary winding draws only the small no-load current $I_0$. This current establishes the mutual magnetic flux $\Phi$ in the core. The flux induces a primary back e.m.f. $E_1$ that almost completely opposes and balances the applied supply voltage $V_1$ ($V_1 \approx -E_1$).

2. **Demagnetizing M.M.F. of the Load Current:**
   When a load is connected across the secondary, a secondary current $I_2$ begins to flow through the secondary winding of $N_2$ turns. This sets up a **demagnetizing magnetomotive force (m.m.f.)** equal to $N_2 I_2$. By Lenz’s law, this m.m.f. opposes the main magnetic flux $\Phi$.

3. **Reduction of Primary Back E.M.F. ($E_1$):**
   The demagnetizing m.m.f. momentarily weakens the core flux $\Phi$. Because the primary induced back e.m.f. is directly proportional to flux ($E_1 = 4.44 f N_1 \Phi$), $E_1$ drops slightly.

4. **Primary Current Surge:**
   The primary current is given by:
   $$\vec{I}_1 = \frac{\vec{V}_1 - \vec{E}_1}{\vec{Z}_1}$$
   Because the internal impedance $\vec{Z}_1$ of the primary winding is very small, even a fractional decrease in $E_1$ causes a large net driving voltage $(V_1 - E_1)$, prompting the primary winding to draw an additional load current $I_2'$ from the supply mains.

5. **Restoration of Core Flux:**
   This additional primary current $I_2'$ creates a neutralizing primary m.m.f. $N_1 I_2'$ that exactly opposes and cancels the secondary demagnetizing m.m.f. $N_2 I_2$:
   $$N_1 I_2' = N_2 I_2 \implies I_2' = \left(\frac{N_2}{N_1}\right) I_2 = K I_2$$
   As a result, the net core flux $\Phi$ is immediately restored to its constant rated value.

6. **Conclusion:**
   The total primary current is the phasor sum of the no-load current and this reflected load current:
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$$
   Therefore, any increase in the secondary load current $I_2$ directly causes a proportional increase in the primary current $I_1$.

---

### 30. Page 23, Q.16: What is impedance ratio? How impedances in a transformer can be shifted with referred to primary or with referred to secondary?

#### **1. Impedance Ratio**
The **impedance ratio** of a transformer is defined as the ratio of the impedance of the secondary winding (or circuit) to the impedance of the primary winding (or circuit), or vice-versa. 

It is equal to the **square of the voltage transformation ratio ($K^2$)**:

$$\text{Impedance Ratio} = \frac{Z_2}{Z_1} = K^2 = \left(\frac{N_2}{N_1}\right)^2 = \left(\frac{V_2}{V_1}\right)^2$$

---

#### **2. Shifting Impedances from Secondary to Primary:**
To transfer any secondary resistance, leakage reactance, or external load impedance ($R_2, X_2, Z_2, Z_L$) to the primary side:

- **Rule:** **Divide by $K^2$** (or multiply by $(N_1/N_2)^2$).

$$\text{Secondary Resistance referred to Primary: } R_2' = \frac{R_2}{K^2} = R_2 \left(\frac{N_1}{N_2}\right)^2$$
$$\text{Secondary Reactance referred to Primary: } X_2' = \frac{X_2}{K^2} = X_2 \left(\frac{N_1}{N_2}\right)^2$$
$$\text{Secondary Impedance referred to Primary: } Z_2' = \frac{Z_2}{K^2} = Z_2 \left(\frac{N_1}{N_2}\right)^2$$
$$\text{Load Impedance referred to Primary: } Z_L' = \frac{Z_L}{K^2} = Z_L \left(\frac{N_1}{N_2}\right)^2$$

---

#### **3. Shifting Impedances from Primary to Secondary:**
To transfer any primary resistance, leakage reactance, or impedance ($R_1, X_1, Z_1$) to the secondary side:

- **Rule:** **Multiply by $K^2$** (or multiply by $(N_2/N_1)^2$).

$$\text{Primary Resistance referred to Secondary: } R_1' = K^2 R_1 = R_1 \left(\frac{N_2}{N_1}\right)^2$$
$$\text{Primary Reactance referred to Secondary: } X_1' = K^2 X_1 = X_1 \left(\frac{N_2}{N_1}\right)^2$$
$$\text{Primary Impedance referred to Secondary: } Z_1' = K^2 Z_1 = Z_1 \left(\frac{N_2}{N_1}\right)^2$$

---

#### **4. Summary of Shifting Rules:**

| Parameter Shifted | Mathematical Operation | Justification / Physical Basis |
| :--- | :--- | :--- |
| **Primary $\to$ Secondary** | **Multiply by $K^2$** | Preserves copper loss: $I_2^2 (K^2 R_1) = I_1^2 R_1$ |
| **Secondary $\to$ Primary** | **Divide by $K^2$** | Preserves copper loss: $I_1^2 \left(\frac{R_2}{K^2}\right) = I_2^2 R_2$ |
| **Voltage $\to$ Other side** | Multiply / Divide by $K$ | Follows $V_2 = K V_1$ |
| **Current $\to$ Other side** | Divide / Multiply by $K$ | Follows $I_2 = \frac{I_1}{K}$ |

### 31. Page 23, Q.17: What is the importance of shifting impedances?

#### **Importance and Advantages of Shifting Impedances:**

In an actual transformer, the primary and secondary windings are electrically isolated and operate at different voltage and current levels. Shifting (or transferring) the resistances and reactances from one winding to another offers several critical practical advantages:

---

1. **Elimination of Magnetic Coupling in Analysis:**
   - Shifting impedances eliminates the magnetic link (mutual induction) and allows the two isolated electrical circuits to be combined into a **single, continuous, equivalent electrical circuit**.

2. **Great Simplification of Calculations:**
   - Instead of solving simultaneous coupled differential/phasor equations for both sides, all resistances are combined into a single total equivalent resistance ($R_{01}$ or $R_{02}$) and all reactances into a single equivalent reactance ($X_{01}$ or $X_{02}$).
   - The engineer only needs to perform calculations on one winding side.

3. **Direct Evaluation of Total Copper Loss:**
   - The total full-load copper loss of the entire transformer can be calculated directly in one step using the current of a single winding:
     $$\text{Total Cu Loss} = I_1^2 R_{01} = I_2^2 R_{02}$$

4. **Simplified Calculation of Voltage Drop and Voltage Regulation:**
   - Total approximate voltage drop can be computed using a single formula:
     $$\text{Voltage Drop (referred to secondary)} = I_2(R_{02} \cos \phi_2 \pm X_{02} \sin \phi_2)$$
     $$\text{Voltage Drop (referred to primary)} = I_1(R_{01} \cos \phi_1 \pm X_{01} \sin \phi_1)$$

5. **Power System and Fault Modeling:**
   - In large power network studies, transmission lines, transformers, and generators must all be represented on a common reference voltage base. Shifting impedances makes per-unit and impedance-based system protection calculations straightforward.

6. **Invariance of Physical Power and Voltage Drops:**
   - Because impedances are scaled by $K^2 = (N_2/N_1)^2$, the actual power losses ($I^2 R$), reactive energy stored ($I^2 X$), and percentage impedance drops remain completely invariant regardless of which side they are referred to.

---

### 32. Page 23, Q.18: Draw the exact equivalent circuit of a loaded transformer, where the symbols have their usual meanings. [Figure Involved]

#### **Description:**
In the **exact equivalent circuit**, the primary winding impedance ($R_1 + jX_1$) and secondary winding impedance ($R_2 + jX_2$) are shown separately, with the shunt exciting branch placed between them across the primary induced e.m.f. $E_1$.

---

#### **1. Exact Equivalent Circuit with Ideal Transformer:**

```
     I₁ ──►      R₁          X₁              I₂' ──►         R₂          X₂          I₂ ──►
      ────────████████────UUUUUUUU────┬───────────────────████████────UUUUUUUU────┬────────
                                      │        ││   ││                            │
                                      │        ││   ││                            │
                                  I₀  │        ││   ││                          ┌─┴─┐
                                  ├───►        ││   ││                          │   │
                                  │   │        ││   ││                          │   │
        V₁                        │ ┌─┴─┐      ││   ││                     V₂   │ZL │ (Load)
        ~                        [R₀] [X₀]  E₁ ││ : ││ E₂                   ~   │   │
                                  │ └─┬─┘      ││   ││                          │   │
                                  │   │        ││   ││                          └─┬─┘
                                  └───┴────────││───││────────────────────────────┴────────
                                          Ideal Transformer (N₁ : N₂)
```

---

#### **2. Exact Equivalent Circuit (Referred to Primary Side):**
When the secondary parameters and load impedance are transferred to the primary side, the ideal transformer is removed:

```
     I₁ ──►      R₁          X₁              I₂' ──►      R₂' = R₂/K²   X₂' = X₂/K²
      ────────████████────UUUUUUUU────┬───────────────────████████────UUUUUUUU────┬────────
                                      │                                           │
                                  I₀  │                                         ┌─┴─┐
                                  ├───►                                         │   │
                                  │   │                                         │Z'L│
        V₁                        │ ┌─┴─┐                                       │   │ V₂' = V₂/K
        ~                        [R₀] [X₀]  E₁                                  │   │
                                  │ └─┬─┘                                       └─┬─┘
                                  │   │                                           │
      ────────────────────────────┴───┴───────────────────────────────────────────┴────────
```

---

#### **Definition of Symbols:**
- $V_1 =$ Primary supply terminal voltage
- $I_1 =$ Total primary line current
- $R_1, X_1 =$ Primary winding resistance and leakage reactance
- $I_0 =$ No-load current
- $R_0, X_0 =$ Core-loss resistance and magnetizing reactance representing the shunt exciting branch
- $E_1, E_2 =$ Induced e.m.f. in primary and secondary windings
- $I_2' =$ Secondary load current referred to primary ($I_2' = K I_2$)
- $R_2', X_2' =$ Secondary resistance and reactance referred to primary ($R_2' = R_2/K^2, X_2' = X_2/K^2$)
- $Z_L' =$ Load impedance referred to primary ($Z_L' = Z_L/K^2$)
- $V_2' =$ Secondary terminal voltage referred to primary ($V_2' = V_2/K$)

---

### 33. Page 23, Q.19: Simplify the equivalent circuit of a loaded transformer (i) referred to primary (ii) referred to secondary, with suitable equations and net diagram. [Figure Involved]

#### **Reason for Simplification:**
Because the no-load current $I_0$ is only $1\%\text{ to }3\%$ of the full-load current, the voltage drop produced by $I_0$ in the primary impedance $(R_1 + jX_1)$ is extremely small. Hence, negligible error is introduced by shifting the shunt exciting branch directly across the input supply terminals.

---

#### **(i) Simplified Equivalent Circuit Referred to Primary:**

```
     I₁ ──►      R₀₁ = R₁ + R₂/K²     X₀₁ = X₁ + X₂/K²       I₂' ──►
      ───────┬────██████████───────────UUUUUUUU──────────────┬────────
             │                                               │
             │   I₀                                        ┌─┴─┐
             ├───►──┐                                      │   │
             │      │                                      │Z'L│ V₂' = V₂/K
        V₁   │   ┌──┴──┐                                   │   │
        ~    │  [R₀]  [X₀]                                 └─┬─┘
             │   └──┬──┘                                     │
             │      │                                        │
      ───────┴──────┴────────────────────────────────────────┴────────
```

**Governing Equations:**
- **Equivalent Primary Resistance:** $R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}$
- **Equivalent Primary Leakage Reactance:** $X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{K^2}$
- **Equivalent Primary Impedance:** $Z_{01} = \sqrt{R_{01}^2 + X_{01}^2}$
- **Total Primary Current:** $\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$
- **Primary Applied Voltage:** $\vec{V}_1 = \vec{V}_2' + \vec{I}_2'(R_{01} + jX_{01})$

---

#### **(ii) Simplified Equivalent Circuit Referred to Secondary:**

```
     I₁' ──►     R₀₂ = R₂ + K²R₁      X₀₂ = X₂ + K²X₁        I₂ ──►
      ───────┬────██████████───────────UUUUUUUU──────────────┬────────
             │                                               │
             │   I₀'                                       ┌─┴─┐
             ├───►──┐                                      │   │
             │      │                                      │ZL │ V₂ (Terminal Voltage)
      K·V₁   │   ┌──┴──┐                                   │   │
        ~    │ [R₀']  [X₀']                                └─┬─┘
             │   └──┬──┘                                     │
             │      │                                        │
      ───────┴──────┴────────────────────────────────────────┴────────
```

**Governing Equations:**
- **Equivalent Secondary Resistance:** $R_{02} = R_2 + R_1' = R_2 + K^2 R_1$
- **Equivalent Secondary Leakage Reactance:** $X_{02} = X_2 + X_1' = X_2 + K^2 X_1$
- **Equivalent Secondary Impedance:** $Z_{02} = \sqrt{R_{02}^2 + X_{02}^2}$
- **Shunt Parameters referred to Secondary:** $R_0' = K^2 R_0$, $X_0' = K^2 X_0$
- **Secondary Voltage Equation:** $K\vec{V}_1 = \vec{V}_2 + \vec{I}_2(R_{02} + jX_{02})$

---

### 34. Page 23, Q.20: Draw the approximate equivalent circuit of a loaded transformer (i) referred to primary (ii) referred to secondary. [Figure Involved]

#### **Description:**
For standard load and voltage drop calculations, the small no-load exciting current is omitted altogether. The transformer is modeled as a lumped series impedance connected between the supply and the load.

---

#### **(i) Approximate Equivalent Circuit (Referred to Primary):**

```
     I₁ ≈ I₂' ──►       R₀₁                X₀₁
      ───────────────██████████──────────UUUUUUUU────────────┬────────
                                                             │
                                                           ┌─┴─┐
                                                           │   │
        V₁ ~                                               │Z'L│ V₂' = V₂/K
                                                           │   │
                                                           └─┬─┘
                                                             │
      ───────────────────────────────────────────────────────┴────────
```

**Formulas (Referred to Primary):**
$$R_{01} = R_1 + \frac{R_2}{K^2}$$
$$X_{01} = X_1 + \frac{X_2}{K^2}$$
$$Z_{01} = R_{01} + jX_{01} = \sqrt{R_{01}^2 + X_{01}^2}$$
$$V_2' = \frac{V_2}{K}, \quad I_2' = K I_2, \quad Z_L' = \frac{Z_L}{K^2}$$

---

#### **(ii) Approximate Equivalent Circuit (Referred to Secondary):**

```
     I₂ ──►             R₀₂                X₀₂
      ───────────────██████████──────────UUUUUUUU────────────┬────────
                                                             │
                                                           ┌─┴─┐
                                                           │   │
       K·V₁ ~                                              │ZL │ V₂ (Load Voltage)
                                                           │   │
                                                           └─┬─┘
                                                             │
      ───────────────────────────────────────────────────────┴────────
```

**Formulas (Referred to Secondary):**
$$R_{02} = R_2 + K^2 R_1$$
$$X_{02} = X_2 + K^2 X_1$$
$$Z_{02} = R_{02} + jX_{02} = \sqrt{R_{02}^2 + X_{02}^2}$$
$$R_{02} = K^2 R_{01}, \quad X_{02} = K^2 X_{01}, \quad Z_{02} = K^2 Z_{01}$$

### 35. Page 26, CT-04 Q.1: Define-(i) leakage reactance, (ii) magnetizing current, (iii) leakage flux, (iv) mutual flux, (v) core loss current.

#### **(i) Leakage Reactance ($X_1, X_2$)**
**Leakage reactance** is the inductive reactance associated with the magnetic leakage flux in a transformer winding. Since the leakage flux passes mostly through air, it sets up a self-induced e.m.f. that behaves as if an inductive coil were connected in series with the winding:
- **Primary Leakage Reactance:** $X_1 = \frac{e_{L1}}{I_1} = 2\pi f L_1$
- **Secondary Leakage Reactance:** $X_2 = \frac{e_{L2}}{I_2} = 2\pi f L_2$
It causes an internal reactive voltage drop ($I_1 X_1$ in primary, $I_2 X_2$ in secondary) which affects the transformer's voltage regulation.

---

#### **(ii) Magnetizing Current ($I_\mu$ or $I_m$)**
**Magnetizing current** is the purely reactive (wattless) component of the primary no-load current. 
- It is in phase with the mutual magnetic flux $\Phi$ and lags behind the applied primary voltage $V_1$ by $90^\circ$.
- Its sole function is to establish and sustain the alternating magnetic flux in the ferromagnetic core:
  $$I_\mu = I_0 \sin \phi_0$$
  where $I_0$ is the no-load current and $\phi_0$ is the no-load power factor angle.

---

#### **(iii) Leakage Flux ($\Phi_{L1}, \Phi_{L2}$)**
**Leakage flux** is that portion of the magnetic flux produced by a winding that completes its magnetic circuit through the surrounding air, insulation, or oil and links **only with that winding itself**, without linking the other winding.
- **Primary Leakage Flux ($\Phi_{L1}$):** Links only the primary winding.
- **Secondary Leakage Flux ($\Phi_{L2}$):** Links only the secondary winding.
Leakage flux does not contribute to the transfer of power between primary and secondary circuits.

---

#### **(iv) Mutual Flux ($\Phi$)**
**Mutual flux** (or working flux) is the common magnetic flux that is confined within the high-permeability laminated steel core and links **both the primary and secondary windings simultaneously**.
- It is established by the primary magnetizing m.m.f. and serves as the medium for transferring electrical energy from the primary to the secondary winding through electromagnetic mutual induction.

---

#### **(v) Core Loss Current ($I_w$ or $I_c$)**
**Core loss current** (also known as the active or working component of no-load current) is the in-phase component of the primary no-load current:
- It is in phase with the applied primary voltage $V_1$.
- It accounts for the real active power drawn by the transformer at no-load to supply the core losses (hysteresis and eddy current losses) in the iron core along with a negligible primary copper loss:
  $$I_w = I_0 \cos \phi_0$$
  $$\text{Core Loss, } W_i \approx V_1 I_w = V_1 I_0 \cos \phi_0$$

---

### 36. Page 32, Q.1(b): Briefly describe the effect of variation of load on core flux and primary current of a transformer.

#### **1. Effect of Load Variation on Core Flux ($\Phi$):**
The mutual core flux $\Phi$ in a transformer remains **practically constant from no-load to full-load** (varying by only $1\%\text{ to }3\%$):

```
 Load Increases (I₂ ↑) ──► Secondary Demagnetizing M.M.F. (N₂ I₂ ↑)
                                    │
                                    ▼
                     Core Flux Momentarily Weakens (Φ ↓)
                                    │
                                    ▼
                     Primary Back E.M.F. Drops (E₁ ↓)
                                    │
                                    ▼
                 Primary Draws Balancing Current (I₂' = K I₂ ↑)
                                    │
                                    ▼
             Balancing M.M.F. (N₁ I₂' = N₂ I₂) Restores Core Flux
                                    │
                                    ▼
                      Net Core Flux Φ = CONSTANT
```

- **Explanation:** When the secondary load increases, the secondary current $I_2$ sets up an opposing demagnetizing m.m.f. $N_2 I_2$. This momentarily weakens the core flux $\Phi$, which reduces the primary induced back e.m.f. $E_1$. 
- The resulting voltage difference $(V_1 - E_1)$ immediately causes the primary to draw an extra current $I_2'$ from the supply. This sets up a compensating m.m.f. $N_1 I_2'$ that exactly cancels the secondary m.m.f. ($N_1 I_2' = N_2 I_2$).
- Thus, the net magnetizing m.m.f. in the core remains unchanged, keeping the mutual core flux practically constant across all load levels.

---

#### **2. Effect of Load Variation on Primary Current ($I_1$):**
The total primary current is the phasor sum of the no-load exciting current and the reflected load current:
$$\vec{I}_1 = \vec{I}_0 + \vec{I}_2' = \vec{I}_0 + K \vec{I}_2$$

- **At No-Load ($I_2 = 0$):** The primary draws only the small no-load current $I_0$ ($2\%\text{ to }10\%$ of rated current) at a very low power factor ($\cos \phi_0 \approx 0.2\text{ lagging}$).
- **As Load Increases ($I_2 > 0$):** The reflected load component $I_2' = K I_2$ increases in direct proportion to the secondary current. Since $I_2'$ is much larger than $I_0$, the total primary current $I_1$ increases almost linearly with the load.
- **Power Factor Shift:** The phase angle $\phi_1$ of the primary current shifts from the no-load angle $\phi_0$ towards the load power factor angle $\phi_2$.

---

### 37. Page 41, Q.3(a): Why is current increase in primary with the load increase in secondary? Explain.

#### **Physical and Magnetic Reason:**

A transformer is a self-regulating electrical machine that maintains an automatic energy balance between its primary input and secondary output. The primary current increases with secondary load through the following sequence of events:

---

1. **Equilibrium at No-Load:**
   On no-load, the primary current is restricted to a small no-load current $I_0$. This current establishes the working flux $\Phi$ in the core. The flux induces a primary back e.m.f. $E_1$ that almost completely opposes and balances the applied terminal voltage $V_1$:
   $$V_1 \approx -E_1$$

2. **Demagnetizing M.M.F. Produced by Secondary:**
   When the secondary load is increased, a larger secondary current $I_2$ flows through the $N_2$ secondary turns. According to Lenz's law, this sets up a **demagnetizing magnetomotive force (m.m.f.)** $N_2 I_2$ that directly opposes the main magnetic flux $\Phi$.

3. **Reduction in Induced Back E.M.F. ($E_1$):**
   The demagnetizing effect of $N_2 I_2$ momentarily reduces the mutual core flux $\Phi$. Because the primary induced back e.m.f. is directly proportional to flux ($E_1 = 4.44 f N_1 \Phi$), $E_1$ decreases slightly.

4. **Surge in Primary Current ($I_2'$):**
   The net voltage driving current into the primary winding is $(\vec{V}_1 - \vec{E}_1)$. The primary current is given by:
   $$\vec{I}_1 = \frac{\vec{V}_1 - \vec{E}_1}{\vec{Z}_1}$$
   Because the internal primary impedance $\vec{Z}_1$ is very small, even a minute drop in $E_1$ produces a large voltage difference, prompting the primary winding to immediately draw an additional load current $I_2'$ from the supply.

5. **M.M.F. Cancellation and Flux Restoration:**
   This additional primary current $I_2'$ creates a primary neutralizing m.m.f. $N_1 I_2'$ that perfectly counterbalances the secondary demagnetizing m.m.f.:
   $$N_1 I_2' = N_2 I_2 \implies I_2' = \left(\frac{N_2}{N_1}\right) I_2 = K I_2$$
   This restores the net core flux $\Phi$ back to its constant working level.

6. **Conclusion:**
   The total primary current is:
   $$\vec{I}_1 = \vec{I}_0 + \vec{I}_2'$$
   Therefore, whenever the secondary load current $I_2$ increases, the primary winding must draw a proportionally larger current $I_1$ to supply the required energy and maintain magnetic equilibrium.

---

### 39. Page 9, Q.1(d): Calculate the percentage of voltage regulation of a transformer in which the percentage resistance drop is 1% and percentage reactance drop is 5% when p.f. is (i) 0.8 lagging (ii) unity and (iii) 0.8 leading.

#### **Given Data:**
- Percentage resistance drop, $v_r = 1.0\%$
- Percentage reactance drop, $v_x = 5.0\%$

---

#### **Formula:**
The approximate percentage voltage regulation ($\mu$) is given by:
$$\% \text{ Voltage Regulation } (\mu) = v_r \cos \phi \pm v_x \sin \phi$$
- Use **$+$ sign** for **lagging power factor**
- Use **$-$ sign** for **leading power factor**

---

#### **Calculations:**

#### **(i) At $0.8$ Power Factor Lagging:**
- $\cos \phi = 0.8$
- $\sin \phi = \sqrt{1 - (0.8)^2} = 0.6$

$$\mu = v_r \cos \phi + v_x \sin \phi$$
$$\mu = (1.0 \times 0.8) + (5.0 \times 0.6) = 0.8 + 3.0 = \mathbf{+3.8\%}$$

---

#### **(ii) At Unity Power Factor ($\text{u.p.f.}$):**
- $\cos \phi = 1.0$
- $\sin \phi = 0.0$

$$\mu = v_r \cos \phi \pm v_x \sin \phi$$
$$\mu = (1.0 \times 1.0) + (5.0 \times 0.0) = \mathbf{+1.0\%}$$

---

#### **(iii) At $0.8$ Power Factor Leading:**
- $\cos \phi = 0.8$
- $\sin \phi = 0.6$

$$\mu = v_r \cos \phi - v_x \sin \phi$$
$$\mu = (1.0 \times 0.8) - (5.0 \times 0.6) = 0.8 - 3.0 = \mathbf{-2.2\%}$$

*(Note: The negative regulation sign indicates a voltage rise at full load under leading power factor conditions).*

---

#### **Summary of Results:**
1. At **$0.8$ p.f. lagging:** **$+3.8\%$**
2. At **Unity p.f.:** **$+1.0\%$**
3. At **$0.8$ p.f. leading:** **$-2.2\%$**


### 40. Page 19, Q.2(d): Define voltage regulation. Is it possible to have negative voltage regulation of a transformer?

#### **1. Definition of Voltage Regulation:**
The **voltage regulation** of a transformer is defined as the change in secondary terminal voltage when the rated full load at a given power factor is thrown off (reduced to zero/no-load), keeping the primary supply voltage constant, expressed as a fraction or percentage of the rated terminal voltage.

- **Percentage Regulation 'Down':**
  $$\% \text{ Regulation (Down)} = \frac{{}_0V_2 - V_2}{{}_0V_2} \times 100$$

- **Percentage Regulation 'Up':**
  $$\% \text{ Regulation (Up)} = \frac{{}_0V_2 - V_2}{V_2} \times 100$$

where:
- ${}_0V_2 =$ Secondary terminal voltage on no-load ($= E_2 = K V_1$)
- $V_2 =$ Secondary terminal voltage on full-load

Using the percentage resistive drop ($v_r$) and reactive drop ($v_x$):
$$\% \text{ Regulation } \approx v_r \cos \phi_2 \pm v_x \sin \phi_2$$

---

#### **2. Is it possible to have Negative Voltage Regulation?**
**Yes, it is entirely possible to have negative voltage regulation.**

#### **Reason and Explanation:**
Negative voltage regulation occurs when the transformer is connected to a **leading power factor (capacitive) load**.

```
 Under Leading Power Factor (Capacitive Load):
 Voltage Drop = I₂ R₀₂ cos φ₂ - I₂ X₀₂ sin φ₂
 If (I₂ X₀₂ sin φ₂ > I₂ R₀₂ cos φ₂) ──► Net Voltage Drop is NEGATIVE
                                       │
                                       ▼
                       Full-Load Voltage V₂ > No-Load Voltage ₀V₂
                                       │
                                       ▼
               % Regulation = [(₀V₂ - V₂)/₀V₂] × 100  < 0  (NEGATIVE)
```

1. **Mathematical Condition:**
   For a leading power factor load, the voltage drop expression contains a negative sign:
   $$\text{Voltage Drop} = I_2 R_{02} \cos \phi_2 - I_2 X_{02} \sin \phi_2$$
   Whenever the reactive voltage boost term ($I_2 X_{02} \sin \phi_2$) exceeds the resistive voltage drop term ($I_2 R_{02} \cos \phi_2$), the net voltage drop becomes negative:
   $$I_2 X_{02} \sin \phi_2 > I_2 R_{02} \cos \phi_2 \implies \tan \phi_2 > \frac{R_{02}}{X_{02}}$$

2. **Physical Meaning:**
   A negative voltage regulation means that the **secondary terminal voltage on full-load ($V_2$) is actually greater than the secondary terminal voltage on no-load (${}_0V_2$)**. The terminal voltage rises as the capacitive load is applied due to the leading current providing capacitive voltage boosting across the leakage reactance.

---

### 41. Page 23, Q.21: Find the approximate voltage drop in a transformer with net phasor diagram. [Figure Involved]

#### **Derivation of Approximate Voltage Drop:**

Let all quantities be referred to the secondary side:
- $V_2 =$ Secondary terminal voltage on full-load
- ${}_0V_2 = E_2 =$ Secondary no-load terminal voltage ($= K V_1$)
- $I_2 =$ Secondary full-load current lagging behind $V_2$ by angle $\phi_2$
- $R_{02} =$ Total equivalent resistance referred to secondary $= R_2 + K^2 R_1$
- $X_{02} =$ Total equivalent leakage reactance referred to secondary $= X_2 + K^2 X_1$

---

#### **Phasor Diagram for Lagging Power Factor:**

```
                                               C
                                             / │
                                 I₂Z₀₂     /   │
                                         /     │
                                       /       │
                                     /         │ I₂X₀₂
                       ₀V₂ = E₂    /           │
                                 /             │
                               /   I₂R₀₂       │
                             /  ┌──────────────B
                           /    │             /│
                         /      │           /  │
                       /        │         /    │
                     /          │       /      │
                   /     φ₂     │     /        │
                 O──────────────A───D──────────N
                       V₂        I₂ (Reference)
```

---

#### **Geometric Analysis:**
1. From the origin $O$, draw vector $OA = V_2$ along the horizontal axis.
2. Draw the current phasor $I_2$ lagging $V_2$ by angle $\phi_2$.
3. From point $A$, draw $AB = I_2 R_{02}$ parallel to $I_2$.
4. From point $B$, draw $BC = I_2 X_{02}$ perpendicular to $AB$ (leading $I_2$ by $90^\circ$).
5. Join $OC$ to represent the no-load voltage ${}_0V_2 = E_2$.
6. With $O$ as center and radius $OC$, draw an arc cutting $OA$ produced at $M$. The total voltage drop is:
   $$\text{Exact Drop} = OC - OA = AM$$
7. Draw $BD \perp OA$ produced, and $CN \perp OA$ produced. Since the angle between $OC$ and $OA$ is very small in practice, $AM \approx AN$.

---

#### **Mathematical Expression:**
From the geometry of the figure:
$$\text{Approximate Voltage Drop} = AN = AD + DN$$

- From right-angled triangle $ABD$:
  $$AD = AB \cos \phi_2 = I_2 R_{02} \cos \phi_2$$

- From right-angled triangle $BCN$ (or by projecting $BC$ onto $OA$):
  $$DN = BC \sin \phi_2 = I_2 X_{02} \sin \phi_2$$

Substituting these components:
$$\text{Approximate Voltage Drop (Lagging p.f.)} = I_2 R_{02} \cos \phi_2 + I_2 X_{02} \sin \phi_2$$

For a general load (lagging or leading):
$$\text{Approximate Voltage Drop} = I_2 (R_{02} \cos \phi_2 \pm X_{02} \sin \phi_2)$$
*(use $+$ for lagging p.f. and $-$ for leading p.f.)*

Similarly, when referred to the primary side:
$$\text{Approximate Voltage Drop} = I_1 (R_{01} \cos \phi_1 \pm X_{01} \sin \phi_1)$$

---

### 42. Page 23, Q.22: Define voltage regulation of a transformer?

#### **Definition:**
The **voltage regulation** of a transformer is defined as the arithmetic difference between the secondary no-load terminal voltage (${}_0V_2$) and the secondary full-load terminal voltage ($V_2$) at a specified power factor, expressed as a percentage of the no-load (or full-load) secondary voltage, while the primary applied voltage is maintained constant.

---

#### **Mathematical Formulas:**

1. **Percentage Voltage Regulation:**
   $$\% \text{ Regulation} = \frac{{}_0V_2 - V_2}{{}_0V_2} \times 100$$

2. **In Terms of Equivalent Circuit Constants:**
   $$\% \text{ Regulation} = \frac{I_2 R_{02} \cos \phi \pm I_2 X_{02} \sin \phi}{{}_0V_2} \times 100$$
   $$\% \text{ Regulation} = v_r \cos \phi \pm v_x \sin \phi$$

where:
- $v_r = \frac{I_2 R_{02}}{{}_0V_2} \times 100 = \text{Percentage resistive drop}$
- $v_x = \frac{I_2 X_{02}}{{}_0V_2} \times 100 = \text{Percentage reactive drop}$
- Use **$+$ sign** for **lagging power factor**
- Use **$-$ sign** for **leading power factor**

---

#### **Important Operating Conditions:**

1. **Condition for Maximum Voltage Regulation (Worst Regulation):**
   Occurs at a lagging power factor when:
   $$\frac{d(\% \text{ regn})}{d\phi} = 0 \implies \tan \phi = \frac{v_x}{v_r} = \frac{X_{02}}{R_{02}}$$
   $$\text{Maximum } \% \text{ Regulation} = \sqrt{v_r^2 + v_x^2} = \% Z$$

2. **Condition for Zero Voltage Regulation (Perfect Regulation):**
   Occurs only at a leading power factor when:
   $$v_r \cos \phi - v_x \sin \phi = 0 \implies \tan \phi = \frac{v_r}{v_x} = \frac{R_{02}}{X_{02}}$$

---

### 43. Page 27, CT-04 Q.2: Calculate voltage regulation at (i) unity pf, (ii) 0.8 leading pf, (iii) 0.7 lagging pf. If the transformer is operated as step-down one, giving rated voltage at full load, unity power factor, what is the secondary open-circuit voltage when the load is removed?

#### **Given Parameters:**
- Percentage resistance drop, $v_r = 1.0\%$
- Percentage reactance drop, $v_x = 5.0\%$

---

#### **Part 1: Voltage Regulation Calculations**

The formula for percentage voltage regulation is:
$$\% \text{ Regulation } (\mu) = v_r \cos \phi \pm v_x \sin \phi$$

---

#### **(i) At Unity Power Factor ($\text{u.p.f.}$):**
- $\cos \phi = 1.0$
- $\sin \phi = 0.0$

$$\mu = (1.0 \times 1.0) + (5.0 \times 0.0) = \mathbf{+1.0\%}$$

---

#### **(ii) At $0.8$ Power Factor Leading:**
- $\cos \phi = 0.8$
- $\sin \phi = \sqrt{1 - (0.8)^2} = 0.6$

$$\mu = v_r \cos \phi - v_x \sin \phi$$
$$\mu = (1.0 \times 0.8) - (5.0 \times 0.6) = 0.8 - 3.0 = \mathbf{-2.2\%}$$

---

#### **(iii) At $0.7$ Power Factor Lagging:**
- $\cos \phi = 0.7$
- $\sin \phi = \sqrt{1 - (0.7)^2} = \sqrt{1 - 0.49} = \sqrt{0.51} \approx 0.7141$

$$\mu = v_r \cos \phi + v_x \sin \phi$$
$$\mu = (1.0 \times 0.7) + (5.0 \times 0.7141) = 0.7 + 3.5705 = \mathbf{+4.27\%}$$

---

#### **Part 2: Secondary Open-Circuit Voltage on Removal of Load**

When the transformer operates as a step-down transformer delivering rated full-load voltage $V_2$ at unity power factor:
- At unity p.f., the percentage regulation is:
  $$\% \text{ Regulation} = \frac{{}_0V_2 - V_2}{V_2} \times 100 = 1.0\%$$

- Solving for secondary open-circuit voltage (${}_0V_2$):
  $${}_0V_2 - V_2 = 0.01 \, V_2$$
  $${}_0V_2 = V_2 + 0.01 \, V_2 = \mathbf{1.01 \, V_2}$$

#### **Conclusion:**
When the full load at unity power factor is removed, the secondary open-circuit voltage will be **$1.01\text{ times}$ the rated full-load voltage (i.e., $101\%$ of rated secondary voltage $V_2$)**.

### 44. Page 33, Q.2(c): Discuss the effect of change in frequency on transformer’s (i) core loss, (ii) Cu loss, and (iii) voltage regulation.

When the supply frequency ($f$) of a transformer changes while the applied terminal voltage ($V$) is maintained constant, its performance parameters are affected as follows:

---

#### **(i) Effect on Core Loss (Iron Loss):**
From the transformer e.m.f. equation, the maximum core flux density is inversely proportional to frequency:
$$V \approx 4.44 f N B_m A \implies B_m \propto \frac{V}{f}$$

The total core loss comprises two parts:
1. **Hysteresis Loss ($W_h$):**
   $$W_h = \eta B_m^{1.6} f \propto \left(\frac{V}{f}\right)^{1.6} f \propto V^{1.6} f^{-0.6}$$
   - Hysteresis loss is inversely proportional to $f^{0.6}$. 
   - A **decrease in frequency** increases hysteresis loss (e.g., at $50\text{ Hz}$, $W_h$ is about $11\%$ higher than at $60\text{ Hz}$).
   - An **increase in frequency** decreases hysteresis loss.

2. **Eddy Current Loss ($W_e$):**
   $$W_e = K_e B_m^2 f^2 \propto \left(\frac{V}{f}\right)^2 f^2 \propto V^2$$
   - Eddy current loss is **independent of frequency** when voltage is held constant.

**Conclusion:** Total core loss ($W_i = W_h + W_e$) **increases as frequency decreases**, causing the transformer to run hotter at lower frequencies.

---

#### **(ii) Effect on Copper Loss (Cu Loss):**
Full-load copper loss is determined by the winding currents and their ohmic resistances:
$$W_{\text{Cu}} = I_1^2 R_1 + I_2^2 R_2$$
- The ohmic resistance of copper conductors depends only on temperature and geometry.
- Neglecting minor skin effect at standard power frequencies ($50\text{ Hz}$ / $60\text{ Hz}$), the winding resistance remains constant.

**Conclusion:** For a given load current, **copper loss is independent of supply frequency**.

---

#### **(iii) Effect on Voltage Regulation:**
The approximate voltage drop in a transformer is:
$$\Delta V = I (R \cos \phi \pm X \sin \phi)$$

The leakage reactance $X$ is directly proportional to frequency:
$$X = 2\pi f L \propto f$$

1. **At Unity Power Factor ($\cos \phi = 1, \sin \phi = 0$):**
   - Voltage drop depends solely on resistive drop ($I R$).
   - Voltage regulation is **unaffected by changes in frequency**.

2. **At Lagging/Leading Power Factor:**
   - As frequency **increases**, leakage reactance $X$ increases, increasing the reactive drop ($I X \sin \phi$). This results in a **poorer (larger) voltage regulation** for lagging loads.
   - As frequency **decreases**, leakage reactance $X$ decreases, leading to a smaller reactive drop and **improved (smaller) voltage regulation** for lagging loads.

---

### 45. Page 41, Q.4(a): What is meant by regulation of a transformer? Which transformer is better when regulation of one transformer is 0.04% and another is 0.05% and why?

#### **1. Meaning of Voltage Regulation:**
The **voltage regulation** of a transformer represents the change in secondary terminal voltage when rated full-load is removed (i.e., from full-load to no-load condition) while maintaining the primary supply voltage constant. It is expressed as a percentage of the secondary terminal voltage:

$$\% \text{ Voltage Regulation} = \frac{{}_0V_2 - V_2}{{}_0V_2} \times 100$$

where:
- ${}_0V_2 =$ Secondary terminal voltage on no-load ($= E_2 = K V_1$)
- $V_2 =$ Secondary terminal voltage at rated full-load

---

#### **2. Comparison of Transformers ($0.04\%$ vs $0.05\%$):**
Between the two transformers:
- Transformer 1: Voltage Regulation $= 0.04\%$
- Transformer 2: Voltage Regulation $= 0.05\%$

**The transformer with $0.04\%$ voltage regulation is BETTER.**

---

#### **Why?**
1. **Closer to Ideal Performance:** An ideal transformer has $0\%$ voltage regulation (constant terminal voltage under all load conditions). A regulation of $0.04\%$ is closer to zero than $0.05\%$.
2. **Superior Voltage Stability:** A smaller voltage regulation value indicates smaller internal impedance drops ($I R_{02}$ and $I X_{02}$). The secondary terminal voltage will remain substantially more stable from no-load to full-load.
3. **Protection of Connected Loads:** Industrial and domestic equipment, lighting systems, and electronic appliances perform more efficiently and have longer lifespans when supplied with a steady voltage free from noticeable voltage sags under load changes.

---

### 47. Page 7, Q.1(c): A 10 kVA, 1-φ, 50 Hz 400/200 V transformer gave the following test results: O.C. Test (LV side) 200 V 3.0 A 200 W. S.C. Test (HV side) 15 V 30 A 300 W. Calculate efficiency and regulation at full load, 0.8 p.f lagging.

#### **Given Data:**
- Transformer Rating $= 10\text{ kVA} = 10,000\text{ VA}$
- Primary Voltage (H.V.), $V_1 = 400\text{ V}$
- Secondary Voltage (L.V.), $V_2 = 200\text{ V}$
- Frequency, $f = 50\text{ Hz}$
- O.C. Test (L.V. side): $V_0 = 200\text{ V}, I_0 = 3.0\text{ A}, W_0 = 200\text{ W}$
- S.C. Test (H.V. side): $V_{sc} = 15\text{ V}, I_{sc} = 30\text{ A}, W_{sc} = 300\text{ W}$
- Load Power Factor, $\cos \phi = 0.8\text{ lagging}$ ($\sin \phi = 0.6$)

---

#### **Step-by-Step Solution:**

#### **1. Rated Currents:**
- Rated H.V. (Primary) Current:
  $$I_{1\text{(FL)}} = \frac{\text{kVA} \times 1000}{V_1} = \frac{10,000}{400} = 25\text{ A}$$
- Rated L.V. (Secondary) Current:
  $$I_{2\text{(FL)}} = \frac{10,000}{200} = 50\text{ A}$$

---

#### **2. Losses Determination:**
- **Constant Iron Loss ($W_i$):**
  From the Open-Circuit (O.C.) test at rated voltage:
  $$W_i = W_0 = 200\text{ W}$$

- **Full-Load Copper Loss ($W_{\text{Cu(FL)}}$):**
  The S.C. test was conducted at $I_{sc} = 30\text{ A}$, which is higher than rated current ($25\text{ A}$).
  Equivalent resistance referred to H.V. side:
  $$R_{01} = \frac{W_{sc}}{I_{sc}^2} = \frac{300}{(30)^2} = \frac{300}{900} = \frac{1}{3}\,\Omega = 0.3333\,\Omega$$

  Full-load copper loss at rated primary current ($I_{1\text{(FL)}} = 25\text{ A}$):
  $$W_{\text{Cu(FL)}} = I_{1\text{(FL)}}^2 R_{01} = (25)^2 \times \frac{1}{3} = \frac{625}{3} = 208.33\text{ W}$$

---

#### **3. Efficiency at Full-Load, 0.8 p.f. Lagging:**
- Full-load Output Power:
  $$P_{\text{out}} = \text{kVA} \times \cos \phi = 10 \times 0.8 = 8\text{ kW} = 8,000\text{ W}$$

- Total Full-load Losses:
  $$\text{Total Losses} = W_i + W_{\text{Cu(FL)}} = 200 + 208.33 = 408.33\text{ W}$$

- Full-load Input Power:
  $$P_{\text{in}} = P_{\text{out}} + \text{Total Losses} = 8,000 + 408.33 = 8,408.33\text{ W}$$

- Efficiency ($\eta$):
  $$\eta = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100 = \frac{8,000}{8,408.33} \times 100 = \mathbf{95.14\%}$$

---

#### **4. Voltage Regulation at Full-Load, 0.8 p.f. Lagging:**
From S.C. test parameters referred to H.V. side:
- Total Equivalent Impedance:
  $$Z_{01} = \frac{V_{sc}}{I_{sc}} = \frac{15}{30} = 0.5\,\Omega$$

- Total Equivalent Reactance:
  $$X_{01} = \sqrt{Z_{01}^2 - R_{01}^2} = \sqrt{(0.5)^2 - (0.3333)^2} = \sqrt{0.25 - 0.1111} = \sqrt{0.1389} = 0.3727\,\Omega$$

- Total Voltage Drop referred to Primary:
  $$\Delta V_1 = I_{1\text{(FL)}} (R_{01} \cos \phi + X_{01} \sin \phi)$$
  $$\Delta V_1 = 25 \times (0.3333 \times 0.8 + 0.3727 \times 0.6) = 25 \times (0.2667 + 0.2236) = 25 \times 0.4903 = 12.26\text{ V}$$

- Percentage Voltage Regulation:
  $$\% \text{ Regulation} = \frac{\Delta V_1}{V_1} \times 100 = \frac{12.26}{400} \times 100 = \mathbf{3.065\%} \approx \mathbf{3.07\%}$$

---

### 48. Page 7, Q.1(d): Why is generally low voltage side shorted for short-circuit test of a transformer?

In performing the **short-circuit (impedance) test** of a transformer, the low-voltage (L.V.) side is solidly short-circuited while all measuring instruments (voltmeter, ammeter, wattmeter) and the variable power source are connected to the high-voltage (H.V.) side for the following major technical and practical reasons:

---

1. **Lower Rated Current on H.V. Side (Standard Metering Range):**
   - The rated current on the high-voltage side is small ($I_{\text{HV}} = K \cdot I_{\text{LV}}$).
   - Standard laboratory ammeters, wattmeters, and variacs (typically rated for $5\text{ A}$ to $20\text{ A}$) can be connected directly into the circuit without requiring expensive, high-current instrument transformers (C.T.s).

2. **Availability and Control of Test Voltage:**
   - To circulate full-load current under short-circuit conditions, only about **$5\%\text{ to }10\%$ of rated voltage** is required.
   - When energized from the H.V. side, this required voltage (e.g., $5\%\text{ of } 3300\text{ V} = 165\text{ V}$) is within an easily controllable and measurable range on standard laboratory variable a.c. supplies.
   - If energized from the L.V. side, $5\%$ of a low voltage (e.g., $5\%\text{ of } 220\text{ V} = 11\text{ V}$) would be very difficult to regulate and measure accurately with standard meters.

3. **Ease and Safety of Short-Circuiting the L.V. Side:**
   - Shorting the low-voltage terminals with a thick copper link or bar is simple, safe, and mechanically robust.
   - The voltage across the shorted L.V. terminals is zero, eliminating insulation breakdown and shock hazards on the secondary side during the test.

4. **Measurement Accuracy:**
   - Placing instruments on the H.V. side ensures that the measured impedance and loss values fall well within the optimal scale deflection ranges of voltmeters and wattmeters, minimizing instrument reading errors.
### 49. Page 17, Q.2(a) (upper half): Why the open-circuit test of transformer gives core loss, while the short-circuit test of a transformer gives copper loss?

#### **1. Why the Open-Circuit (O.C.) Test Gives Core Loss:**
In an open-circuit test, rated normal alternating voltage at rated frequency is applied to one winding (usually the low-voltage winding), while the other winding is kept open-circuited ($I_2 = 0$).

```
 Open-Circuit Test:
 Applied Voltage = Rated V₁ ──► Rated Core Flux Density Bm ──► FULL Core Loss (Wi) Occurs
 Primary Current = I₀ (2% to 10% of FL) ──► Cu Loss = I₀² R₁ ≈ 0 (NEGLIGIBLE)
 ════════════════════════════════════════════════════════════════════════════════════════
 Wattmeter Reading (W₀) = Wi (Core Loss Only)
```

- **Rated Core Flux:** Since rated voltage is applied, the mutual magnetic flux in the core attains its full normal rated peak value ($\Phi_m \propto \frac{V_1}{f}$). Therefore, the full normal **core losses (hysteresis and eddy current losses)** take place in the iron core.
- **Negligible Copper Loss:** The secondary current is zero, producing zero secondary copper loss. The primary winding draws only the tiny no-load current $I_0$ ($2\%\text{ to }10\%$ of full-load current). The primary copper loss is:
  $$P_{\text{Cu(no-load)}} = I_0^2 R_1 \approx (0.05)^2 \times P_{\text{Cu(FL)}} \approx 0.0025 \times P_{\text{Cu(FL)}}$$
  This is entirely negligible (less than a fraction of $1\%$ of the wattmeter reading).
- **Conclusion:** The wattmeter reading $W_0$ in the O.C. test measures **practically only the core (iron) loss ($W_i$)**.

---

#### **2. Why the Short-Circuit (S.C.) Test Gives Copper Loss:**
In a short-circuit test, the secondary (usually L.V.) winding is solidly shorted with a thick copper bar, and a very small reduced voltage ($5\%\text{ to }10\%$ of rated voltage) is applied to the primary (H.V.) winding to circulate full rated currents in both windings.

```
 Short-Circuit Test:
 Applied Voltage = Vsc (5% to 10% of Rated V₁) ──► Core Flux Φsc ≈ 0 ──► Core Loss Wi ≈ 0 (NEGLIGIBLE)
 Winding Currents = Rated Full-Load Currents ──► FULL Copper Loss (Wcu = I₁² R₀₁) Occurs
 ════════════════════════════════════════════════════════════════════════════════════════
 Wattmeter Reading (Wsc) = Wcu (Full-Load Copper Loss Only)
```

- **Rated Copper Loss:** Because rated full-load currents $I_1$ and $I_2$ circulate through the primary and secondary windings, the total full-load ohmic copper loss occurs:
  $$W_{\text{Cu}} = I_1^2 R_1 + I_2^2 R_2 = I_1^2 R_{01}$$
- **Negligible Core Loss:** The voltage $V_{sc}$ required to circulate full-load current under short-circuit is extremely low (only $5\%\text{ to }10\%$ of rated voltage). Since core flux is directly proportional to applied voltage ($\Phi \propto V_{sc}$), the core flux is only a fraction ($1/10\text{th}\text{ to }1/20\text{th}$) of its normal operating value. Because core losses vary approximately as $\Phi^2$, the iron loss in this test is:
  $$W_{i(sc)} \propto V_{sc}^2 \approx (0.05)^2 \times W_i \approx 0.0025 \times W_i$$
  This is completely negligible.
- **Conclusion:** The wattmeter reading $W_{sc}$ in the S.C. test measures **practically only the full-load copper loss ($W_{\text{Cu}}$)**.

---

### 50. Page 17, Q.2(b): Describe the open-circuit test of a transformer with suitable connection diagram. Why high voltage winding is usually left open in this test? [Figure Involved]

#### **1. Description and Purpose of the Test:**
The **open-circuit (O.C.) or no-load test** is conducted on a transformer to determine:
- The constant **core/iron loss ($W_i$)**
- The **no-load current ($I_0$)** and **no-load power factor ($\cos \phi_0$)**
- The shunt exciting branch parameters: **core-loss resistance ($R_0$)** and **magnetizing reactance ($X_0$)**
- The voltage transformation ratio ($K$)

---

#### **2. Connection Diagram:**

```
     A.C. Supply           W (Wattmeter)
     (Rated V & f)     ┌────[CC]────┐
       o───────────────┤            ├─────────────┬───────────┐
                       │            │             │           │
                       │    [PC]    │             │           │
                      (V)    │     (A)            │           │
                       │     │      │            ┌┴┐         ┌┴┐
                       │     └──────┤        L.V.│ │     H.V.│ │ (Open
                       │            │     Winding│ │  Winding│ │  Circuited)
       o───────────────┴────────────┴────────────┴┬┘         └┬┘
                                                  │           │
                                                  └───────────┘
```

---

#### **3. Test Procedure:**
1. The low-voltage (L.V.) winding is connected to its rated voltage and frequency supply through an ammeter ($A$), a wattmeter ($W$), and a voltmeter ($V$).
2. The high-voltage (H.V.) winding is kept open-circuited.
3. The applied voltage is adjusted to the rated voltage of the L.V. winding.
4. The voltmeter reading ($V_1$), ammeter reading ($I_0$), and wattmeter reading ($W_0$) are recorded.

---

#### **4. Parameter Determination:**
- **No-load Power Factor:**
  $$\cos \phi_0 = \frac{W_0}{V_1 I_0}$$
- **Core-Loss (Working) Component:**
  $$I_w = I_0 \cos \phi_0 = \frac{W_0}{V_1}$$
- **Magnetizing Component:**
  $$I_\mu = \sqrt{I_0^2 - I_w^2} = I_0 \sin \phi_0$$
- **Core-Loss Resistance:**
  $$R_0 = \frac{V_1}{I_w} = \frac{V_1^2}{W_0}$$
- **Magnetizing Reactance:**
  $$X_0 = \frac{V_1}{I_\mu}$$

---

#### **5. Why the High-Voltage (H.V.) Winding is Usually Left Open:**
1. **Convenience of Supply Voltage:** The L.V. winding rated voltage (e.g., $110\text{ V}, 230\text{ V}, 400\text{ V}$) is readily available in testing laboratories, whereas the high voltage (e.g., $6.6\text{ kV}, 11\text{ kV}, 33\text{ kV}$) requires special step-up sources.
2. **Measurement Accuracy:** On the L.V. side, the no-load current $I_0$ ($2\%\text{ to }10\%$ of rated current) is large enough to be accurately read on standard laboratory ammeters. On the H.V. side, $I_0$ would be extremely small (often in milliamperes) and difficult to measure accurately.
3. **Personnel and Equipment Safety:** Keeping the high-voltage winding open and de-energized minimizes insulation stress and eliminates the risk of high-voltage shock hazard during instrument adjustments.

---

### 51. Page 17, Q.2(c) (upper half): Obtain the equivalent circuit of a 10kVA, 450/120 V, 50Hz transformer from the following test data: O.C. Test: 120V, 4.2A, 80W – on L.V. side S.C. Test: 9.65V, 22.2A, 120W – on H.V. side.

#### **Given Data:**
- Rating $= 10\text{ kVA} = 10,000\text{ VA}$
- High-Voltage (Primary), $V_1 = 450\text{ V}$
- Low-Voltage (Secondary), $V_2 = 120\text{ V}$
- Frequency, $f = 50\text{ Hz}$
- **O.C. Test (on L.V. side):** $V_0 = 120\text{ V}, I_0 = 4.2\text{ A}, W_0 = 80\text{ W}$
- **S.C. Test (on H.V. side):** $V_{sc} = 9.65\text{ V}, I_{sc} = 22.2\text{ A}, W_{sc} = 120\text{ W}$

---

#### **Step-by-Step Calculation:**

#### **1. Transformation Ratio ($K$):**
$$K = \frac{V_{\text{LV}}}{V_{\text{HV}}} = \frac{120}{450} = \frac{4}{15} \approx 0.2667$$

---

#### **2. Shunt Branch Parameters from O.C. Test (L.V. Side):**
- No-load power factor on L.V. side:
  $$\cos \phi_0 = \frac{W_0}{V_0 I_0} = \frac{80}{120 \times 4.2} = \frac{80}{504} = 0.1587 \approx 0.159$$
- $\sin \phi_0$:
  $$\sin \phi_0 = \sqrt{1 - (0.1587)^2} = \sqrt{1 - 0.0252} = 0.9873$$
- Core-loss component of current on L.V. side:
  $$I_{w\text{(LV)}} = I_0 \cos \phi_0 = 4.2 \times 0.1587 = 0.6667\text{ A}$$
- Magnetizing component of current on L.V. side:
  $$I_{\mu\text{(LV)}} = I_0 \sin \phi_0 = 4.2 \times 0.9873 = 4.147\text{ A}$$
- Shunt resistance on L.V. side:
  $$R_{0\text{(LV)}} = \frac{V_0}{I_{w\text{(LV)}}} = \frac{120}{0.6667} = 180\,\Omega$$
- Shunt reactance on L.V. side:
  $$X_{0\text{(LV)}} = \frac{V_0}{I_{\mu\text{(LV)}}} = \frac{120}{4.147} = 28.94\,\Omega$$

**Referring Shunt Parameters to H.V. (Primary) Side:**
$$R_0 = \frac{R_{0\text{(LV)}}}{K^2} = \frac{180}{(4/15)^2} = 180 \times \frac{225}{16} = \mathbf{2531.25\,\Omega \approx 2530\,\Omega}$$
$$X_0 = \frac{X_{0\text{(LV)}}}{K^2} = \frac{28.94}{(4/15)^2} = 28.94 \times \frac{225}{16} = \mathbf{406.97\,\Omega \approx 409\,\Omega}$$

---

#### **3. Series Parameters from S.C. Test (H.V. Side):**
Since S.C. test was conducted directly on the H.V. side, all calculated parameters are directly referred to the primary:
- Total Equivalent Impedance referred to Primary ($Z_{01}$):
  $$Z_{01} = \frac{V_{sc}}{I_{sc}} = \frac{9.65}{22.2} = \mathbf{0.4347\,\Omega \approx 0.435\,\Omega}$$
- Total Equivalent Resistance referred to Primary ($R_{01}$):
  $$R_{01} = \frac{W_{sc}}{I_{sc}^2} = \frac{120}{(22.2)^2} = \frac{120}{492.84} = \mathbf{0.2435\,\Omega \approx 0.243\,\Omega}$$
- Total Equivalent Leakage Reactance referred to Primary ($X_{01}$):
  $$X_{01} = \sqrt{Z_{01}^2 - R_{01}^2} = \sqrt{(0.4347)^2 - (0.2435)^2} = \sqrt{0.1890 - 0.0593} = \sqrt{0.1297} = \mathbf{0.3601\,\Omega \approx 0.361\,\Omega}$$

---

#### **4. Equivalent Circuit Diagram (Referred to H.V. Primary Side):**

```
     I₁ ──►                                    R₀₁ = 0.243 Ω    X₀₁ = 0.361 Ω       I₂' ──►
      ──────────────┬────────────────────────────████████─────────UUUUUUUU─────────────┬──────
                    │                                                                   │
                    │   I₀                                                            ┌─┴─┐
                    ├───►──┐                                                          │   │
                    │      │                                                          │Z'L│
               V₁   │   ┌──┴──┐                                                       │   │ V₂'
             450 V  │  [R₀]  [X₀]                                                     └─┬─┘
               ~    │ 2530 Ω 409 Ω                                                      │
                    │   └──┬──┘                                                         │
                    │      │                                                            │
      ──────────────┴──────┴────────────────────────────────────────────────────────────┴──────
```

---

### 52. Page 17, Q.2(c) (lower half): What are the objectives of short circuit test? Describe the short circuit test with suitable diagram. [Figure Involved]

#### **1. Objectives of the Short-Circuit (S.C.) Test:**
The primary objectives of conducting the short-circuit (or impedance) test on a transformer are:
1. **Determination of Full-Load Copper Loss ($W_{\text{Cu}}$):** To measure the ohmic $I^2R$ power loss of both primary and secondary windings combined under full-load condition.
2. **Determination of Equivalent Series Resistance ($R_{01}$ or $R_{02}$):** To calculate the lumped winding resistance referred to either side.
3. **Determination of Equivalent Leakage Reactance ($X_{01}$ or $X_{02}$):** To find the total leakage reactance of the transformer.
4. **Determination of Equivalent Impedance ($Z_{01}$ or $Z_{02}$):** To find total impedance for short-circuit fault current calculations.
5. **Predetermination of Voltage Regulation:** To calculate the percentage voltage drop and regulation at any desired load current and power factor without actually loading the transformer.
6. **Efficiency Calculation:** To compute the overall efficiency of the transformer at any fractional load.

---

#### **2. Connection Diagram:**

```
     Variable A.C.         W (Wattmeter)
     Supply (0-10% V)  ┌────[CC]────┐
       o───────────────┤            ├─────────────┬───────────┐
                       │            │             │           │
                       │    [PC]    │             │           │
                      (V)    │     (A)            │           │
                       │     │      │            ┌┴┐         ┌┴┐
                       │     └──────┤        H.V.│ │     L.V.│ │ Solid Short
                       │            │     Winding│ │  Winding│ │ Circuit
       o───────────────┴────────────┴────────────┴┬┘         └┬┘ (Thick Link)
                                                  │           │
                                                  └───────────┘
```

---

#### **3. Description of the Test:**
1. The low-voltage (L.V.) winding is solidly short-circuited using a thick copper strip or bar.
2. Measuring instruments (voltmeter, ammeter, and wattmeter) are connected to the high-voltage (H.V.) winding.
3. A low alternating voltage (typically $5\%\text{ to }10\%$ of rated H.V. voltage) at rated frequency is applied to the H.V. winding using a variable auto-transformer (variac).
4. The applied voltage is gradually increased from zero until the ammeter indicates the rated full-load current of the H.V. winding ($I_{sc} = I_{1\text{(FL)}}$).
5. The readings of the short-circuit voltage ($V_{sc}$), short-circuit current ($I_{sc}$), and short-circuit power input ($W_{sc}$) are noted.

---

#### **4. Mathematical Relations (Referred to H.V. Side):**
- **Total Full-Load Copper Loss:**
  $$W_{\text{Cu(FL)}} = W_{sc}$$
- **Equivalent Impedance:**
  $$Z_{01} = \frac{V_{sc}}{I_{sc}}$$
- **Equivalent Resistance:**
  $$R_{01} = \frac{W_{sc}}{I_{sc}^2}$$
- **Equivalent Leakage Reactance:**
  $$X_{01} = \sqrt{Z_{01}^2 - R_{01}^2}$$
- **Short-Circuit Power Factor:**
  $$\cos \phi_{sc} = \frac{R_{01}}{Z_{01}} = \frac{W_{sc}}{V_{sc} I_{sc}}$$
### 53. Page 17, Q.2(d): Find the equivalent winding resistance, reactance and impedance referred to the (i) high voltage side and (ii) the low voltage side. (from a 30 KVA, 2400/120 V, 50 Hz transformer).

#### **Given Data:**
- Transformer Rating $= 30\text{ kVA}$
- Primary High-Voltage (H.V.), $V_1 = 2400\text{ V}$
- Secondary Low-Voltage (L.V.), $V_2 = 120\text{ V}$
- Frequency, $f = 50\text{ Hz}$
- High-voltage winding resistance, $R_1 = 0.1\,\Omega$
- High-voltage winding leakage reactance, $X_1 = 0.22\,\Omega$
- Low-voltage winding resistance, $R_2 = 0.035\,\Omega$
- Low-voltage winding leakage reactance, $X_2 = 0.012\,\Omega$

---

#### **Step-by-Step Calculations:**

#### **1. Transformation Ratio ($K$):**
$$K = \frac{V_2}{V_1} = \frac{120}{2400} = \frac{1}{20} = 0.05$$
$$K^2 = \left(\frac{1}{20}\right)^2 = \frac{1}{400} = 0.0025$$

---

#### **(i) Values Referred to High-Voltage (H.V. / Primary) Side:**

1. **Equivalent Resistance ($R_{01}$):**
   $$R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{K^2}$$
   $$R_{01} = 0.1 + \frac{0.035}{(1/20)^2} = 0.1 + (0.035 \times 400) = 0.1 + 14.0 = \mathbf{14.1\,\Omega}$$

2. **Equivalent Leakage Reactance ($X_{01}$):**
   $$X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{K^2}$$
   $$X_{01} = 0.22 + \frac{0.012}{(1/20)^2} = 0.22 + (0.012 \times 400) = 0.22 + 4.80 = \mathbf{5.02\,\Omega}$$

3. **Equivalent Impedance ($Z_{01}$):**
   $$Z_{01} = \sqrt{R_{01}^2 + X_{01}^2} = \sqrt{(14.1)^2 + (5.02)^2} = \sqrt{198.81 + 25.2004} = \sqrt{224.01} = \mathbf{14.97\,\Omega \approx 15.0\,\Omega}$$

---

#### **(ii) Values Referred to Low-Voltage (L.V. / Secondary) Side:**

1. **Equivalent Resistance ($R_{02}$):**
   $$R_{02} = R_2 + R_1' = R_2 + K^2 R_1$$
   $$R_{02} = 0.035 + \left(\frac{1}{400}\right) \times 0.1 = 0.035 + 0.00025 = \mathbf{0.03525\,\Omega}$$
   *(Alternatively: $R_{02} = K^2 R_{01} = \frac{14.1}{400} = 0.03525\,\Omega$)*

2. **Equivalent Leakage Reactance ($X_{02}$):**
   $$X_{02} = X_2 + X_1' = X_2 + K^2 X_1$$
   $$X_{02} = 0.012 + \left(\frac{1}{400}\right) \times 0.22 = 0.012 + 0.00055 = \mathbf{0.01255\,\Omega}$$
   *(Alternatively: $X_{02} = K^2 X_{01} = \frac{5.02}{400} = 0.01255\,\Omega$)*

3. **Equivalent Impedance ($Z_{02}$):**
   $$Z_{02} = \sqrt{R_{02}^2 + X_{02}^2} = \sqrt{(0.03525)^2 + (0.01255)^2} = \sqrt{0.00124256 + 0.00015750} = \mathbf{0.0374\,\Omega}$$
   *(Alternatively: $Z_{02} = K^2 Z_{01} = \frac{14.97}{400} = 0.0374\,\Omega$)*

---

### 54. Page 17, Q.4(a): Why is all-day efficiency preferred rather than commercial efficiency?

#### **1. Commercial / Ordinary Efficiency vs. Real Operating Conditions:**
**Commercial efficiency** is defined at an instantaneous point in time under a steady power level:
$$\text{Commercial Efficiency} = \frac{\text{Output Power in Watts}}{\text{Input Power in Watts}}$$

While commercial efficiency is suitable for **power transformers** (which operate near full load continuously at power stations), it does not accurately measure the performance of **distribution transformers** because of their distinct operating cycle:

```
                  DISTRIBUTION TRANSFORMER 24-HOUR CYCLE
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Primary connected to grid 24 hrs ──► Core Loss occurs CONTINUOUSLY     │
 │                                                                        │
 │ Secondary load varies wildly:                                          │
 │   - Peak load for only 4-6 evening hours                               │
 │   - Light / No-load for remaining 18-20 hours                          │
 │   ──► Copper Loss (I²R) occurs ONLY when load flows                    │
 └────────────────────────────────────────────────────────────────────────┘
```

---

#### **2. Why All-Day Efficiency is Preferred:**

1. **Continuous Core Loss vs. Intermittent Copper Loss:**
   - The primary winding remains energized for all $24\text{ hours}$ of the day, so **core/iron loss ($W_i$) is dissipated continuously**.
   - The secondary load fluctuates (e.g., heavy during evening residential peak, nearly zero after midnight). Therefore, **copper loss ($I^2R$) varies with the square of the fractional load ($x^2 W_{\text{Cu}}$)**.

2. **True Measure of Energy Consumption:**
   - Commercial efficiency calculated at full load suggests high performance (e.g., $98\%$), but in reality, if the transformer sits lightly loaded for most of the day, total daily energy loss will be dominated by continuous iron losses.
   - **All-day efficiency (or energy efficiency)** computes the true energy balance over a complete 24-hour cycle:
     $$\eta_{\text{all-day}} = \frac{\text{Energy Output in 24 Hours (kWh)}}{\text{Energy Input in 24 Hours (kWh)}} = \frac{\text{Output (kWh)}}{\text{Output (kWh)} + W_i\text{-energy (kWh)} + W_{\text{Cu}}\text{-energy (kWh)}}$$

3. **Optimal Design Criterion for Distribution Transformers:**
   - Distribution transformers are intentionally engineered with a very high iron-to-copper ratio to make **core losses extremely low**, placing their maximum efficiency point at around $50\%\text{ to }70\%$ of full load to maximize the 24-hour all-day energy efficiency.

---

### 55. Page 17, Q.4(c): Find ‘all-day’ efficiency of a transformer having maximum efficiency of 98% at 15kVA at unity p.f and loaded as follows: 12 Hrs – 2kW at 0.5 p.f lagging; 6 hrs – 12kW at 0.8 p.f lagging; 6 hrs – at no load.

#### **Given Data:**
- Maximum efficiency, $\eta_{\max} = 98\% = 0.98$ at $15\text{ kVA}$ at unity power factor ($\cos \phi = 1.0$)
- 24-hour load cycle:
  - **Period 1 (12 hours):** $2\text{ kW}$ at $0.5\text{ p.f. lagging}$
  - **Period 2 (6 hours):** $12\text{ kW}$ at $0.8\text{ p.f. lagging}$
  - **Period 3 (6 hours):** No load

---

#### **Step-by-Step Solution:**

#### **1. Loss Evaluation at Maximum Efficiency:**
- Output power at $\eta_{\max} = 15\text{ kVA} \times 1.0 = 15\text{ kW}$
- Input power $= \frac{\text{Output}}{\eta_{\max}} = \frac{15}{0.98} = 15.3061\text{ kW}$
- Total losses $= \text{Input} - \text{Output} = 15.3061 - 15 = 0.3061\text{ kW} = 306.1\text{ W}$

At maximum efficiency:
$$\text{Copper Loss } (W_{\text{Cu}}) = \text{Iron Loss } (W_i) = \frac{306.1}{2} = 153.06\text{ W} = 0.1531\text{ kW}$$

- Full-load copper loss at $15\text{ kVA}$, $W_{\text{Cu(FL)}} = 0.1531\text{ kW}$
- Constant core loss, $W_i = 0.1531\text{ kW}$

---

#### **2. Core Loss Energy in 24 Hours:**
Since the core loss is continuous:
$$\text{Core loss in 24 hours} = 24 \times 0.1531\text{ kW} = \mathbf{3.6744\text{ kWh}}$$

---

#### **3. Load Energy Output and Copper Losses for Each Period:**

- **Period 1 ($12\text{ hours}$):**
  - $\text{kVA}_1 = \frac{2\text{ kW}}{0.5} = 4\text{ kVA}$
  - Load fraction, $x_1 = \frac{4}{15}$
  - Output energy $= 2\text{ kW} \times 12\text{ h} = 24\text{ kWh}$
  - Copper loss rate $= x_1^2 \times W_{\text{Cu(FL)}} = \left(\frac{4}{15}\right)^2 \times 0.1531 = 0.010887\text{ kW}$
  - Copper loss energy $= 0.010887\text{ kW} \times 12\text{ h} = \mathbf{0.1306\text{ kWh}}$

- **Period 2 ($6\text{ hours}$):**
  - $\text{kVA}_2 = \frac{12\text{ kW}}{0.8} = 15\text{ kVA}$
  - Load fraction, $x_2 = \frac{15}{15} = 1.0$ (Full load)
  - Output energy $= 12\text{ kW} \times 6\text{ h} = 72\text{ kWh}$
  - Copper loss rate $= (1.0)^2 \times 0.1531 = 0.1531\text{ kW}$
  - Copper loss energy $= 0.1531\text{ kW} \times 6\text{ h} = \mathbf{0.9186\text{ kWh}}$

- **Period 3 ($6\text{ hours}$ at No-Load):**
  - Output energy $= 0\text{ kWh}$
  - Copper loss energy $= 0\text{ kWh}$

---

#### **4. Daily Totals:**
- **Total Output Energy:**
  $$\text{Total Output (kWh)} = 24 + 72 + 0 = \mathbf{96\text{ kWh}}$$

- **Total Copper Loss Energy:**
  $$\text{Total } W_{\text{Cu}}\text{ (kWh)} = 0.1306 + 0.9186 + 0 = \mathbf{1.0492\text{ kWh}}$$

- **Total Energy Losses:**
  $$\text{Total Losses} = 3.6744\text{ (Iron)} + 1.0492\text{ (Copper)} = \mathbf{4.7236\text{ kWh}}$$

- **Total Input Energy:**
  $$\text{Total Input (kWh)} = 96 + 4.7236 = \mathbf{100.7236\text{ kWh}}$$

---

#### **5. All-Day Efficiency ($\eta_{\text{all-day}}$):**
$$\eta_{\text{all-day}} = \frac{\text{Total Output (kWh)}}{\text{Total Input (kWh)}} \times 100 = \frac{96}{100.7236} \times 100 = \mathbf{95.31\%}$$

---

### 56. Page 18, Q.1(a): What is a transformer? Prove that the efficiency of a transformer will be maximum when copper loss is equal to iron loss.

#### **1. Definition of a Transformer:**
A **transformer** is a static piece of electrical equipment that transfers alternating-current electric energy from one circuit to another at the same frequency through electromagnetic mutual induction, usually changing the values of voltage and current.

---

#### **2. Proof: Condition for Maximum Efficiency ($\text{Copper Loss} = \text{Iron Loss}$):**

Let:
- $V_1 =$ Primary applied voltage
- $I_1 =$ Primary current
- $\cos \phi_1 =$ Primary load power factor
- $R_{01} =$ Total equivalent resistance referred to the primary side
- $W_i =$ Total core (iron) loss (constant with load)
- $W_{\text{Cu}} = I_1^2 R_{01} =$ Total copper loss (variable with load)

---

#### **Efficiency Expression:**
$$\text{Efficiency } (\eta) = \frac{\text{Output Power}}{\text{Input Power}} = \frac{\text{Input Power} - \text{Total Losses}}{\text{Input Power}}$$
$$\eta = \frac{V_1 I_1 \cos \phi_1 - I_1^2 R_{01} - W_i}{V_1 I_1 \cos \phi_1}$$

Dividing numerator terms individually by $V_1 I_1 \cos \phi_1$:
$$\eta = 1 - \frac{I_1 R_{01}}{V_1 \cos \phi_1} - \frac{W_i}{V_1 I_1 \cos \phi_1}$$

---

#### **Differentiating with Respect to Load Current ($I_1$):**
For a given terminal voltage and load power factor, efficiency $\eta$ is a function of the variable load current $I_1$. To find the condition for maximum efficiency, differentiate $\eta$ with respect to $I_1$ and equate the derivative to zero:

$$\frac{d\eta}{dI_1} = 0 - \frac{R_{01}}{V_1 \cos \phi_1} - \left( -\frac{W_i}{V_1 I_1^2 \cos \phi_1} \right) = 0$$

$$\frac{R_{01}}{V_1 \cos \phi_1} = \frac{W_i}{V_1 I_1^2 \cos \phi_1}$$

Cancelling $(V_1 \cos \phi_1)$ from both denominators:
$$R_{01} = \frac{W_i}{I_1^2}$$

Multiplying both sides by $I_1^2$:
$$I_1^2 R_{01} = W_i$$

$$\mathbf{\text{Variable Copper Loss } (W_{\text{Cu}}) = \text{Constant Iron Loss } (W_i)}$$

*(Hence proved.)*

---

#### **Corollaries:**
1. **Load Current at Maximum Efficiency ($I_{2m}$):**
   $$I_{2m} = \sqrt{\frac{W_i}{R_{02}}}$$
2. **Fractional Load ($x$) for Maximum Efficiency:**
   $$x = \sqrt{\frac{\text{Iron Loss}}{\text{Full-Load Copper Loss}}} = \sqrt{\frac{W_i}{W_{\text{Cu(FL)}}}}$$
3. **kVA Load at Maximum Efficiency:**
   $$\text{kVA}_{\max} = \text{Rated Full-Load kVA} \times \sqrt{\frac{W_i}{W_{\text{Cu(FL)}}}}$$
### 57. Page 18, Q.1(c): A 10 kVA, 2200/220 V, 50 Hz transformer is tested on open and short circuit tests. If the following readings are obtained, determine the values of maximum power and the loads at which they occur for unity pf. Open circuit test – high side open: v = 220 V, i = 1.5 A, w = 153 W; Short circuit test – low side shorted: v = 115 V, i = rated, w = 224 W.

#### **Given Data:**
- Transformer Rating $= 10\text{ kVA} = 10,000\text{ VA}$
- Primary Voltage (H.V.), $V_1 = 2200\text{ V}$
- Secondary Voltage (L.V.), $V_2 = 220\text{ V}$
- Frequency, $f = 50\text{ Hz}$
- **O.C. Test (L.V. side, H.V. open):** $V_0 = 220\text{ V}, I_0 = 1.5\text{ A}, W_0 = 153\text{ W}$
  $$\implies \text{Constant Core/Iron Loss } (W_i) = 153\text{ W} = 0.153\text{ kW}$$
- **S.C. Test (H.V. side, L.V. shorted at rated current):** $V_{sc} = 115\text{ V}, I_{sc} = I_{\text{rated}}, W_{sc} = 224\text{ W}$
  $$\implies \text{Full-Load Copper Loss } (W_{\text{Cu(FL)}}) = 224\text{ W} = 0.224\text{ kW}$$

---

#### **Step-by-Step Solution:**

#### **1. Fractional Load ($x$) for Maximum Efficiency:**
Maximum efficiency occurs when the variable copper loss equals the constant iron loss:
$$x^2 \times W_{\text{Cu(FL)}} = W_i$$
$$x = \sqrt{\frac{W_i}{W_{\text{Cu(FL)}}}} = \sqrt{\frac{153}{224}} = \sqrt{0.68304} = \mathbf{0.8265} \quad (82.65\% \text{ of Full-Load})$$

---

#### **2. Load (kVA) at which Maximum Efficiency Occurs:**
$$\text{kVA at } \eta_{\max} = x \times \text{Rated kVA} = 0.8265 \times 10\text{ kVA} = \mathbf{8.265\text{ kVA}}$$

---

#### **3. Maximum Power Output at Unity Power Factor ($\cos \phi = 1.0$):**
$$\text{Output Power } (P_{\text{out}}) = \text{kVA at } \eta_{\max} \times \cos \phi = 8.265 \times 1.0 = \mathbf{8.265\text{ kW}} = \mathbf{8,265\text{ W}}$$

---

#### **4. Maximum Efficiency Value ($\eta_{\max}$):**
At maximum efficiency:
$$\text{Total Losses} = 2 \times W_i = 2 \times 153\text{ W} = 306\text{ W} = 0.306\text{ kW}$$
$$\text{Total Input Power} = P_{\text{out}} + \text{Total Losses} = 8.265 + 0.306 = 8.571\text{ kW}$$

$$\eta_{\max} = \frac{P_{\text{out}}}{\text{Input}} \times 100 = \frac{8.265}{8.571} \times 100 = \mathbf{96.43\%}$$

---

### 58. Page 18, Q.3(c): Obtain the equivalent circuit of a 200/400 V, 50 Hz, 1-phase transformer from the following test data: O.C. Test: 200 V, 0.7 A, 70 W – on L.V. side S.C. Test: 15 V, 10 A, 85 W – on H.V. side Calculate the secondary voltage when delivering 5 kW at 0.8 pf. Lagging, the primary voltage being 200 V.

#### **Given Data:**
- Primary Voltage (L.V.), $V_1 = 200\text{ V}$
- Secondary Voltage (H.V.), $V_2 = 400\text{ V}$
- Frequency, $f = 50\text{ Hz}$
- Transformation ratio, $K = \frac{V_2}{V_1} = \frac{400}{200} = 2$
- **O.C. Test (L.V. Primary Side):** $V_0 = 200\text{ V}, I_0 = 0.7\text{ A}, W_0 = 70\text{ W}$
- **S.C. Test (H.V. Secondary Side):** $V_{sc} = 15\text{ V}, I_{sc} = 10\text{ A}, W_{sc} = 85\text{ W}$

---

#### **Step 1: Shunt Branch Parameters from O.C. Test (Primary L.V. Side)**
- No-load power factor:
  $$\cos \phi_0 = \frac{W_0}{V_0 I_0} = \frac{70}{200 \times 0.7} = \frac{70}{140} = 0.5$$
- $\sin \phi_0 = \sqrt{1 - (0.5)^2} = 0.866$
- Core loss current component:
  $$I_w = I_0 \cos \phi_0 = 0.7 \times 0.5 = 0.35\text{ A}$$
- Magnetizing current component:
  $$I_\mu = I_0 \sin \phi_0 = 0.7 \times 0.866 = 0.606\text{ A}$$
- Core loss resistance:
  $$R_0 = \frac{V_0}{I_w} = \frac{200}{0.35} = \mathbf{571.4\,\Omega}$$
- Magnetizing reactance:
  $$X_0 = \frac{V_0}{I_\mu} = \frac{200}{0.606} = \mathbf{330\,\Omega}$$

---

#### **Step 2: Series Parameters from S.C. Test (Secondary H.V. Side)**
Since S.C. test was conducted on H.V. (secondary), parameters are directly obtained referred to secondary:
- Total secondary impedance:
  $$Z_{02} = \frac{V_{sc}}{I_{sc}} = \frac{15}{10} = \mathbf{1.5\,\Omega}$$
- Total secondary resistance:
  $$R_{02} = \frac{W_{sc}}{I_{sc}^2} = \frac{85}{(10)^2} = \mathbf{0.85\,\Omega}$$
- Total secondary reactance:
  $$X_{02} = \sqrt{Z_{02}^2 - R_{02}^2} = \sqrt{(1.5)^2 - (0.85)^2} = \sqrt{2.25 - 0.7225} = \sqrt{1.5275} = \mathbf{1.24\,\Omega}$$

**Series Parameters Referred to Primary (L.V.) Side ($K=2$):**
- $R_{01} = \frac{R_{02}}{K^2} = \frac{0.85}{4} = \mathbf{0.21\,\Omega}$
- $X_{01} = \frac{X_{02}}{K^2} = \frac{1.24}{4} = \mathbf{0.31\,\Omega}$
- $Z_{01} = \frac{Z_{02}}{K^2} = \frac{1.5}{4} = \mathbf{0.375\,\Omega}$

---

#### **Equivalent Circuit Diagram (Referred to Primary L.V. Side):**

```
     I₁ ──►                                    R₀₁ = 0.21 Ω     X₀₁ = 0.31 Ω        I₂' ──►
      ──────────────┬────────────────────────────████████─────────UUUUUUUU─────────────┬──────
                    │                                                                   │
                    │   I₀                                                            ┌─┴─┐
                    ├───►──┐                                                          │   │
                    │      │                                                          │Z'L│
               V₁   │   ┌──┴──┐                                                       │   │ V₂'
             200 V  │  [R₀]  [X₀]                                                     └─┬─┘
               ~    │ 571.4Ω 330 Ω                                                      │
                    │   └──┬──┘                                                         │
                    │      │                                                            │
      ──────────────┴──────┴────────────────────────────────────────────────────────────┴──────
```

---

#### **Step 3: Calculation of Secondary Terminal Voltage ($V_2$)**
- Load Delivered $= 5\text{ kW}$ at $\cos \phi_2 = 0.8\text{ lagging}$ ($\sin \phi_2 = 0.6$)
- Apparent Load Power $= \frac{5\text{ kW}}{0.8} = 6.25\text{ kVA} = 6,250\text{ VA}$
- Secondary Load Current:
  $$I_2 \approx \frac{\text{Load VA}}{V_2} = \frac{6,250}{400} = 15.625\text{ A} \approx 15.6\text{ A}$$
- Secondary Voltage Drop:
  $$\Delta V_2 = I_2 (R_{02} \cos \phi_2 + X_{02} \sin \phi_2)$$
  $$\Delta V_2 = 15.6 \times (0.85 \times 0.8 + 1.24 \times 0.6) = 15.6 \times (0.68 + 0.744) = 15.6 \times 1.424 = \mathbf{22.2\text{ V}}$$
- Secondary Terminal Voltage on Load:
  $$V_2 = {}_0V_2 - \Delta V_2 = 400 - 22.2 = \mathbf{377.8\text{ V}}$$

---

### 59. Page 19, Q.2(b): Why are iron losses constant at all loads in a transformer?

#### **Physical and Mathematical Explanation:**

The iron loss (core loss) in a transformer is composed of **hysteresis loss ($W_h$)** and **eddy current loss ($W_e$)**:

1. **Hysteresis Loss:**
   $$W_h = \eta B_m^{1.6} f V_{\text{core}}$$
2. **Eddy Current Loss:**
   $$W_e = K_e B_m^2 f^2 t^2 V_{\text{core}}$$

Both components depend exclusively on:
- Maximum core flux density ($B_m$) or peak mutual flux ($\Phi_m$)
- Supply frequency ($f$)
- Core volume and magnetic material properties

---

#### **Why Flux Density ($B_m$) Remains Constant with Load:**
From the e.m.f. equation, the peak core flux is determined by the applied voltage and frequency:
$$V_1 \approx E_1 = 4.44 f N_1 \Phi_m \implies \Phi_m \approx \frac{V_1}{4.44 f N_1}$$

1. **Constant Grid Supply:** The transformer is connected to a supply of constant voltage $V_1$ and constant frequency $f$.
2. **Self-Balancing M.M.F. Action:** When a secondary load current $I_2$ flows, it sets up an opposing secondary m.m.f. $N_2 I_2$ that momentarily reduces the core flux. The primary back e.m.f. $E_1$ falls slightly, causing the primary winding to immediately draw a balancing current $I_2'$ from the supply such that:
   $$N_1 I_2' = N_2 I_2$$
   The primary load m.m.f. neutralizes the secondary demagnetizing m.m.f. at every instant.
3. **Negligible Flux Variation:** The mutual core flux $\Phi_m$ is maintained at its original value, varying by only **$1\%\text{ to }3\%$** from no-load to full-load due to minor primary winding impedance drop.

**Conclusion:** Because the core flux density $B_m$ and supply frequency $f$ remain practically constant under all loading conditions, **iron losses remain constant at all loads**.

---

### 60. Page 19, Q.2(c): “Transformer full load test is performed only for copper loss, while low voltage side is shorted” - why? Comment on your answer.

#### **Comment on the Statement:**
The statement is **entirely correct and describes standard engineering practice**. The short-circuit test (often called the impedance or copper-loss test) is specifically designed to determine the full-load copper loss and series leakage parameters while keeping the low-voltage winding shorted.

---

#### **Detailed Justifications:**

#### **1. Why the Test Measures Only Copper Loss:**
- **Full-Load Currents Circulate:** The applied voltage is adjusted until rated full-load currents flow through both primary and secondary windings ($I_1 = I_{\text{1(FL)}}, I_2 = I_{\text{2(FL)}}$). Therefore, the total full-load ohmic $I^2R$ copper loss of both windings is fully developed:
  $$W_{\text{Cu}} = I_1^2 R_1 + I_2^2 R_2 = I_1^2 R_{01}$$
- **Negligible Core Loss:** Because the windings are short-circuited, the voltage $V_{sc}$ required to drive rated current is very small—only **$5\%\text{ to }10\%$ of rated voltage**. Since core flux is directly proportional to applied voltage ($\Phi \propto V_{sc}$), core flux is reduced to $1/10\text{th}\text{ to }1/20\text{th}$ of normal value. Since iron loss varies as $\Phi^2$, the iron loss during the test is:
  $$W_{i(sc)} \approx (0.05)^2 \times W_i \approx 0.0025 \times W_i \approx 0$$
  Hence, the wattmeter reading represents **purely the full-load copper loss**.

---

#### **2. Why the Low-Voltage (L.V.) Side is Short-Circuited:**
1. **Manageable Meter Currents:** The high-voltage (H.V.) winding has a much smaller rated current ($I_{\text{HV}} = K \cdot I_{\text{LV}}$). Placing the instruments on the H.V. side allows standard laboratory meters (e.g., $5\text{ A}$ to $20\text{ A}$) to be used directly without requiring bulky current transformers (C.T.s).
2. **Accurate and Controllable Test Voltage:** $5\%\text{ to }10\%$ of the H.V. rated voltage (e.g., $5\%\text{ of } 2200\text{ V} = 110\text{ V}$) is easily provided and finely adjusted using a standard laboratory auto-transformer (variac). If performed on the L.V. side, $5\%$ of $220\text{ V} = 11\text{ V}$ would be too low to regulate and measure with high precision.
3. **Safety:** Shorting the low-voltage terminals with a thick copper bar is safe, robust, and maintains zero potential across the short-circuit terminals.


