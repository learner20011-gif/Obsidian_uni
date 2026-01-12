

### **1. Fundamentals of Steam**
*   **Definition:** Gaseous phase of water.
*   **Primary Use:** Power generation (Nuclear/Thermal).
*   **Energy Flow:**
    Fuel $\rightarrow$ Heat $\rightarrow$ Water $\rightarrow$ Steam $\rightarrow$ Turbine (Mech. Energy) $\rightarrow$ Generator (Elec. Power).

---

### **2. Phase Diagram (P vs T)**
*   **Zones:**
    *   Ice (Solid)
    *   Water (Liquid)
    *   Steam (Gas)
*   **Critical Point:** Point where Liquid & Gas phases merge.
*   **Steam Types:**
    *   **Wet:** Contains water droplets.
    *   **Saturated:** Equilibrium (Gas + Liquid).
    *   **Superheated:** Temp $>$ Saturation Temp (at constant P). Lower density, higher energy.

---

### **3. Boiler Definition**
*   **Function:** Apparatus to produce steam by transferring heat from fuel to water.
*   **3 Key Systems:**
    1.  **Heat Source:** Furnace / Combustion.
    2.  **Heat Transfer:** Tubes / Shell.
    3.  **Phase Change:** Water $\rightarrow$ Steam.

---

### **4. Classifications of Boilers**

**A. By Tube Contents**
*   **Fire Tube (FT):** Fire inside tubes, water outside.
*   **Water Tube (WT):** Water inside tubes, fire outside.

**B. By Pressure ($P$)**
*   **Low P:** $< 80$ bar.
*   **High P:** $> 80$ bar.
*   **Super Critical:** $\ge 221.2$ bar.

**C. By Circulation**
*   **Natural:** Caused by density diff ($\Delta \rho$) between hot/cold water.
*   **Forced:** Uses a Pump.

**D. By Firing**
*   **Internally Fired:** Furnace inside shell (e.g., Lancashire).
*   **Externally Fired:** Furnace outside shell (e.g., Babcock & Wilcox).

---

### **5. Requirements of a Good Boiler**
*   $\uparrow$ Thermal Efficiency ($\eta$).
*   $\downarrow$ Cost (Install/Running).
*   Safe at High P.
*   Easy maintenance (access).
*   Flexible load response.

---

### **6. Comparison: Fire Tube vs. Water Tube**

| Feature | Water Tube (WT) | Fire Tube (FT) |
| :--- | :--- | :--- |
| **Flow** | Water in tube | Fire in tube |
| **Safety** | Safer (small tube rupture) | Risk of shell explosion |
| **Pressure** | High P possible | Limited ($\approx 20$ bar) |
| **Size** | Large Power Plants | Small industries |
| **Steam Rate**| Very High | Low |
| **Water** | Requires Treatment (Scale risk) | Less sensitive |

---

### **7. Specific Boiler Types**

#### **A. Cochran Boiler**
*   **Type:** Vertical, Fire Tube, Multi-tubular.
*   **Firing:** Internal.
*   **Shape:** Cylindrical shell + **Hemispherical Dome** (Max strength).
*   **Process:** Furnace $\rightarrow$ Comb Chamber $\rightarrow$ Horizontal Fire Tubes $\rightarrow$ Smoke Box $\rightarrow$ Chimney.

#### **B. Babcock & Wilcox (B&W)**
*   **Type:** Horizontal, Water Tube.
*   **Firing:** External.
*   **Key Features:**
    *   **Inclined Tubes:** Promotes natural circulation ($\approx 15^\circ$).
    *   **Headers:** Uptake & Downtake headers connect tubes to drum.
    *   **Baffles:** Deflect gas for max contact (Zig-zag flow).
    *   **Superheater:** Often included.

#### **C. Locomotive Boiler**
*   **Type:** Horizontal, Fire Tube, Mobile.
*   **Constraint:** Mobile = Short Chimney = **Low Natural Draft**.
*   **Solution:** **Artificial Draft**.
    *   Exhaust steam blasted up chimney $\rightarrow$ Creates vacuum $\rightarrow$ Pulls air.
*   **Components:** Fire Box (Fuel) $\rightarrow$ Barrel (Water/Tubes) $\rightarrow$ Smoke Box.

#### **D. Lancashire Boiler**
*   **Type:** Horizontal, Stationary, Fire Tube.
*   **Key Feature:** **Two** large internal flues.
*   **Application:** Steady loads (Textile/Sugar mills).
*   **Gas Path (3-Pass System):**
    1.  Front $\rightarrow$ Back (Inside internal flues).
    2.  Back $\rightarrow$ Front (Via **Bottom** flue).
    3.  Front $\rightarrow$ Back (Via **Side** flues) $\rightarrow$ Chimney.
*   **Goal:** Maximize heat transfer by heating bottom and sides of shell.

#### **E. Cornish Boiler**
*   **Design:** Same as Lancashire.
*   **Difference:** **One** internal flue only.

### **1. Boiler Performance Metrics**

**A. Evaporative Capacity**
*   **Measurement:** Amount of steam produced.
*   **Units:**
    *   kg/hr (Mass rate).
    *   kg/kg fuel (Fuel efficiency).
    *   kg/m² (Surface intensity).

**B. Equivalent Evaporation ($m_e$)**
*   **Purpose:** Standardizes performance to compare boilers working at different $P$ and $T$.
*   **Standard:** Evaporation **"From and At $100^\circ\text{C}$"**.
*   **Logic:** Converts actual heat added to standard Latent Heat ($2257 \text{ kJ/kg}$ or $540 \text{ kCal/kg}$).
*   **Formula (kJ):** $m_e = \frac{m_a (h - h_f)}{2257}$
*   **Formula (kCal):** $M_e = \frac{M_s (h - h_f)}{540}$ (Total rate)
    *   $M_s$: Total steam rate (kg/hr).
    *   $h, h_f$: Enthalpy in kCal/kg.

**C. Factor of Evaporation ($F_e$)**
*   **Formula:**
    $$ F_e = \frac{h - h_f}{2257} $$

**D. Boiler Efficiency ($\eta$)**
*   **Definition:** Ratio of Heat Utilized to Heat Supplied.
*   **Formula:**
    $$ \eta = \frac{m_a (h - h_f)}{CV} \times 100 \text{ or } \eta = \frac{M_s (h - h_f)}{M_f \times C} \times 100 $$

**E. Specific Equivalent Evaporation ($E$)**
*   **Definition:** Ratio of equivalent steam produced to fuel consumed.
*   **Formula:** $E = \frac{M_e}{M_f}$ (expressed as kg steam/kg fuel).

---

### **2. Boiler Mountings**
*   **Definition:** Mandatory safety & control devices on boiler shell.

**A. Safety Valve**
*   **Function:** Release steam if $P > P_{working}$.
*   **Mechanism (Spring Loaded):**
    *   Spring Force $\downarrow$ dowward vs Steam Force $\uparrow$ upwards .
    *   If Steam Force $>$ Spring Force $\rightarrow$ Valve lifts.

**B. Water Level Indicator**
*   **Qty:** 2 per boiler.
*   **Safety Feature:** Contains metal balls.
    *   Glass breaks $\rightarrow$ $\Delta P$ pushes balls to seal opening $\rightarrow$ Prevents scalding.

**C. Pressure Gauge (Bourdon Tube)**
*   **Principle:** Oval tube straightens when pressurized.
* ![[instrumentationtools.com_pressure-gauge-animation.gif]]
*   **Mechanism:** Tube moves Link $\rightarrow$ Quadrant Gear $\rightarrow$ Pinion $\rightarrow$ Pointer.
*   **Protection:** **U-Tube Siphon** holds water condensate to protect gauge internals from live steam heat.

**D. Feed Check Valve**
*   **Function:** One-way valve (Non-return) for feed water.
*   **Condition:** Opens only if $P_{pump} > P_{boiler}$.
*   **Safety:** Prevents backflow if pump fails.

**E. Steam Stop Valve**
*   **Location:** Highest point (Steam space).
*   **Function:** Manual control (Open/Close) of steam to plant.

**F. Blow-off Cock**
*   **Location:** Lowest point.
*   **Function:** Drain sediments/mud; Empty boiler.
*   **Type:** Plug valve (Rotary).

**G. Fusible Plug**
*   **Location:** Furnace Crown (Firebox).![[Pasted image 20260112094538.png]]
*   **Material:** Low melting point alloy (Lead/Tin).
*   **Logic:**
    *   Submerged (Water) $\rightarrow$ Cool.
    *   Exposed (Low Level) $\rightarrow$ Overheats $\rightarrow$ Melts $\rightarrow$ Steam rushes in $\rightarrow$ Extinguishes fire.

---

### **3. Boiler Accessories**
*   **Definition:** Devices to increase **Efficiency** ($\eta$).

**A. Economizer**
*   **Function:** Preheats Feed Water using flue gas.
*   **Flow:** Boiler $\rightarrow$ Flue Gas $\rightarrow$ **Economizer** $\rightarrow$ Chimney.
*   **Water Path:** High P Pump $\rightarrow$ **Economizer** $\rightarrow$ Boiler.
*   **Mechanism:** Vertical tubes with **mechanical scrapers** (removes soot/insulation).
*   **Gain:** $\approx 1\% \eta$ for every $6-10^\circ\text{C}$ rise. Decreases thermal shock.

**B. Air Preheater**
*   **Function:** Preheats Combustion Air using flue gas.
*   **Location:** After Economizer, before Chimney.
*   **Pros:** $\uparrow$ Combustion temp, burns low-grade fuel.
*   **Cons:** Requires Fans (Forced/Induced Draft) due to airflow resistance.

**C. Superheater**
*   **Function:** Heats steam *beyond* saturation temp.
*   **Location:** In hottest flue gas path.
*   **Benefits:**
    *   Zero moisture $\rightarrow$ Protects Turbine Blades (No erosion).
    *   Higher thermal efficiency.

**D. Feed Pump**
*   **Rule:** $P_{discharge} > P_{boiler}$.
*   **Types:** Centrifugal (Large plants), Reciprocating (Small), Injector (Locos).

**E. Steam Separator**
*   **Function:** Removes water droplets from steam line.
*   **Mechanism:** **Baffles**.
    *   High inertia water hits baffle $\rightarrow$ drops down.
    *   Steam turns corner $\rightarrow$ continues.

---

### **4. Numerical Problem Logic (Recap)**

**Typical Calculation Steps:**
1.  **Find Enthalpies ($h$):** Use Steam Tables (at given $P$).
    *   If Wet: $h = h_f + x(h_{fg})$.
    *   If Feed Water: $h_w = C_p \times T$.
2.  **Find Mass Ratio ($m_a$):**
    *   $m_a = \frac{\text{Total Steam}}{\text{Total Fuel}}$.
3.  **Apply Formula:**
    *   Solve for $\eta$ or $m_e$.

**Grate Area Design Logic:**
1.  **Load:** Engine kW $\times$ Steam Rate = Total Steam (kg/hr).
2.  **Energy:** Total Steam $\times$ $(h_{steam} - h_{feed})$.
3.  **Fuel:** $\frac{\text{Energy Required}}{\text{CV} \times \eta_{overall}}$ = Total Coal (kg/hr).
4.  **Area:** $\frac{\text{Total Coal}}{\text{Burn Rate per } m^2}$ = Grate Area ($m^2$).