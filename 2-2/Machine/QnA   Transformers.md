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

