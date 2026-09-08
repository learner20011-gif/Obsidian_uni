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

