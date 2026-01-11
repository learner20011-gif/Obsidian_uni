# Steam Generation (Boilers) Questions & Answers

**Source:** `mechaGoogle Gemini.pdf` (Questions 13-25)  
**References:** `russel sir Lecture 5.pdf`

---

## General Theory

### 13. Selection: What is a steam boiler? What are the factors affecting the selection of a boiler?

**Answer:**
A **Steam Boiler** (or Steam Generator) is a closed vessel in which water is converted into steam by the application of heat. The heat is usually produced by the combustion of fuel (solid, liquid, or gaseous) or by nuclear energy. Its main purpose is to transfer the heat produced by fuel to water, generating steam for power generation, heating, or industrial processes.

**Factors Affecting Selection of a Boiler:**
1.  **Working Pressure and Quality of Steam:** Whether saturated or superheated steam is required, and at what pressure.
2.  **Steam Generation Rate:** The amount of steam required per hour.
3.  **Floor Area Available:** Fire tube boilers generally require more floor area than water tube boilers for the same capacity.
4.  **Fuel and Water Availability:** The type of fuel available and quality of feedwater (water tube boilers require very pure water).
5.  **Cost:** Initial installation, operation, and maintenance costs.
6.  **Safety and Reliability:** Requirements for safe operation.
7.  **Draft System:** Natural or mechanical draft availability.

**Similar Slide References:**
*   **Slide 3, 5:** Definition of Steam generators/Boilers.
*   **Slide 11:** Requirements of a Good Boiler (related to selection criteria).

### 14. Classification: Differentiate/Distinguish between water tube boiler and fire tube boiler.

**Answer:**

| Feature | Fire Tube Boiler | Water Tube Boiler |
| :--- | :--- | :--- |
| **Position of Water/Gas** | Hot flue gases pass *inside* the tubes, water surrounds them. | Water flows *inside* the tubes, hot flue gases surround them. |
| **Operating Pressure** | Limited to lower pressures (approx. up to 20-25 bar). | Can generate very high pressures (up to 100 bar or more). |
| **Steam Generation Rate** | Lower rate of steam generation. | Higher rate of steam generation. |
| **Suitability** | Suitable for small power plants and industrial heating. | Suitable for large power plants. |
| **Risk of Explosion** | Less risk of explosion involved. | Risk of explosion is higher due to high pressure. |
| **Construction** | Relatively simple and bulky. | Complex structure but more compact for same rating. |
| **Examples** | Cochran, Lancashire, Locomotive. | Babcock & Wilcox, Benson, Stirling. |

**Similar Slide References:**
*   **Slide 7:** Classification (Fire tube vs Water tube).
*   **Slide 12, 13:** Description of Fire tube boilers.
*   **Slide 14:** Description of Water tube boilers.
*   **Slide 15:** Difference between water tube and fire tube boilers.

## Specific Boilers

### 15. Vertical Boiler: Explain the construction and working of a simple vertical boiler with suitable sketches.

**Answer:**
A **Simple Vertical Boiler** is a vertical, fire-tube boiler consisting of a cylindrical shell with a firebox at the bottom.
*   **Construction:** Ideally involves a cylindrical shell, a firebox where fuel is burnt on a grate, cross tubes (in some types) or vertical fire tubes (like in Cochran) to increase heating surface, and a chimney at the top.
*   **Working:** Fuel is burnt on the grate. The hot gases rise from the firebox, pass through the tubes (heating the water surrounding them), and escape through the chimney. Water circulates naturally due to density differences created by heating. Steam is collected at the steam space at the top of the shell.

**Similar Slide References:**
*   **Slide 7:** Mentions Vertical boilers.
*   **Slide 16-17:** Discusses Cochran Boiler (a type of vertical boiler).

### 16. Cochran Boiler: Describe the working principle of a Cochran boiler with a neat sketch.

**Answer:**
The **Cochran Boiler** is a vertical, multi-tubular, internal fired, fire-tube boiler.
*   **Construction:** It consists of a vertical cylindrical shell with a hemispherical crown. The firebox is also hemispherical. It has a combustion chamber lined with firebricks and a series of horizontal fire tubes.
*   **Working Principle:**
    1.  Fuel is burnt on the grate in the firebox.
    2.  Hot flue gases pass from the firebox to the combustion chamber via a short flue pipe.
    3.  From the combustion chamber, gases travel through the horizontal fire tubes to the smoke box at the front.
    4.  Finally, gases are discharged through the chimney.
    5.  Heat is transferred from the gases to the water surrounding the firebox and tubes.
    6.  Natural circulation of water occurs; hot water rises, and steam is collected at the top hemispherical space.

**Similar Slide References:**
*   **Slide 16, 17:** Cochran Boiler details and working.

## Mountings & Accessories

### 17. Difference: Distinguish between boiler mountings and boiler accessories.

**Answer:**

| Boiler Mountings | Boiler Accessories |
| :--- | :--- |
| **Definition** | Components mounted on the boiler body primarily for **safety** and **control** of operation. | Devices installed to increase the **efficiency** of the boiler plant. |
| **Necessity** | Essential/Mandatory for operating the boiler. | Optional (integral mostly in high-pressure plants) but not strictly mandatory for steam generation itself. |
| **Examples** | Safety Valve, Water Level Indicator, Pressure Gauge. | Economizer, Superheater, Air Preheater. |

**Similar Slide References:**
*   **Slide 34:** Boiler Mountings definition.
*   **Slide 44:** Boiler Accessories definition.

### 18. List Items: Name any four mountings and four accessories.

**Answer:**
**Mountings:**
1.  Safety Valve
2.  Water Level Indicator
3.  Pressure Gauge
4.  Steam Stop Valve (or Fusible Plug, Feed Check Valve)

**Accessories:**
1.  Economizer
2.  Superheater
3.  Air Preheater
4.  Feed Pump (or Steam Separator, Steam Trap)

**Similar Slide References:**
*   **Slide 34:** List of Mountings.
*   **Slide 44:** List of Accessories.

### 19. Specific Functions: Discuss the function of the flowing items.

**Answer:**
*   **Economiser:** A device to heat feedwater using the waste heat of flue gases before it enters the boiler, improving efficiency. (**Slide 45-47**)
*   **Superheater:** Heats saturated steam from the boiler to a higher temperature (superheated steam) using flue gas heat. It increases plant capacity and turbine efficiency. (**Slide 51-52**)
*   **Feed Check Valve:** A non-return valve that allows water supply from the feed pump to the boiler and prevents backflow when the pump is stopped. (**Slide 40**)
*   **Air Preheater:** Recovers waste heat from flue gases to heat air before it enters the furnace, aiding combustion and efficiency. (**Slide 48-50**)
*   **Safety Valves:** Automatically release steam when the pressure inside the boiler exceeds the safe working limit, preventing explosions. (**Slide 35-36**)
*   **Blow-off Cock:** Used to discharge mud/sediments from the bottom of the boiler or to empty the boiler. (**Slide 42**)
*   **Water Level Indicator:** Indicates the water level inside the boiler to ensure it doesn't fall below a safe level. (**Slide 37**)

## Numerical Problems

*(Note: Numerical solution methods are based on the formulas provided in the lectures)*

### Formulas (from Lecture 5, Slides 29-32, 56-57):
*   **Actual Evaporation ($m_a$):** $\frac{\text{Mass of steam generated}}{\text{Mass of fuel burnt}}$
*   **Equivalent Evaporation ($m_e$):** $\frac{m_a (h - h_f)}{2257}$ or $\frac{\dot{m}_s (h - h_f)}{2257}$ (Total kg/hr)
    *   Where $h$ = Enthalpy of steam produced, $h_f$ = Enthalpy of feedwater.
    *   $2257$ kJ/kg is the latent heat of vaporization at $100^{\circ}C$.
*   **Boiler Efficiency ($\eta$):** $\frac{\text{Heat utilized}}{\text{Heat supplied}} = \frac{m_a (h - h_f)}{C}$ or $\frac{\dot{m}_s (h - h_f)}{\dot{m}_f \times C}$
    *   $C$ = Calorific Value of fuel.

### 20. Lancashire Boiler Problem
**Statement:** Generates 2400 kg/hr steam at 11 bar. Coal burnt 90 kg/m²... Determine Actual evaporation, Equivalent evaporation, Efficiency.
*   **Method:**
    1.  **Actual Evaporation:** Requires total coal consumption. If "90 kg/m²" is given, you need the Grate Area to find Total Coal ($\dot{m}_f$). Then $m_a = 2400 / \dot{m}_f$.
    2.  **Equivalent Evaporation:** Use $m_e = \frac{2400(h - h_f)}{2257}$. Look up $h$ at 11 bar (steam tables) and $h_f$ for feed water temp.
    3.  **Efficiency:** $\eta = \frac{2400(h - h_f)}{\dot{m}_f \times C}$.
*   **Reference:** Similar formulas in **Slide 58, 59**.

### 21. Boiler Trial (400kg coal)
**Statement:** Coal consumed 400 kg/hr. Steam 3200 kg. Find Equivalent evaporation and Thermal efficiency.
*   **Method:**
    1.  $\dot{m}_s = 3200$ kg, $\dot{m}_f = 400$ kg.
    2.  Actual Evap ($m_a$) = $3200/400 = 8$ kg steam/kg coal.
    3.  Given working pressure/temp, find $h$ and $h_f$.
    4.  **Equivalent Evaporation:** $m_e = \frac{m_a (h - h_f)}{2257}$ (kg/kg fuel) or total $\frac{3200(h-h_f)}{2257}$ kg/hr.
    5.  **Efficiency:** $\frac{m_a(h-h_f)}{C_{value}}$.
*   **Reference:** **Slide 58** (Problem 2 is very similar).

### 22. Boiler Trial (250kg coal) & 23. Boiler Trial (500kg coal)
*   **Method:** Same as Q21. Use $\dot{m}_s$ and $\dot{m}_f$ to find $m_a$, then apply formulas.

### 24. Battery of Boilers
**Statement:** Observations for a battery of 6 Lancashire boilers and an economizer... Find efficiency of boiler alone and whole plant.
*   **Method:**
    1.  **Boiler Efficiency:** $\eta_{boiler} = \frac{\text{Heat gained by water in boiler}}{\text{Heat supplied by fuel}}$.
        *   Heat gained = $\dot{m}_s (h_{steam} - h_{feed\_after\_economizer})$.
    2.  **Plant Efficiency:** $\eta_{plant} = \frac{\text{Heat gained by water in plant}}{\text{Heat supplied by fuel}}$.
        *   Heat gained = $\dot{m}_s (h_{steam} - h_{feed\_inlet\_to\_economizer})$.
    *   The economizer preheats the water, adding efficiency to the whole plant.
*   **Reference:** **Slide 46** mentions economizer increases efficiency. **Slide 57** for efficiency formula.

### 25. Coal Consumption
**Statement:** Steam used by turbine is 5.4 kg/kWh... Boiler efficiency 80%... How many kg of coal required?
*   **Method:**
    1.  Determine Steam Rate per hour if Power is given, or leave as per kWh.
    2.  Heat Output required in Steam = $\text{Steam Mass} \times (h - h_f)$.
    3.  Heat Input from Fuel = $\frac{\text{Heat Output}}{0.80}$.
    4.  Coal Required = $\frac{\text{Heat Input}}{\text{Calorific Value}}$.
*   **Reference:** **Slide 59** (Problem involves design calculations close to this).
