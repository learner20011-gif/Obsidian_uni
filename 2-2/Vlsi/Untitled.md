1. Dynamic RAM (DRAM) Storage Cells
 * 3-Transistor (3T) Dynamic Cell:
   * Circuit: Uses three transistors: T_1 (write switch), T_2 (storage device), and T_3 (read switch).
   * Storage Node: Holds data dynamically as an electric charge on the internal gate capacitance (C_g) of T_2.
   * Write Operation: Write line (WR) goes high during \phi_1, turning T_1 ON to transfer data from the shared bus directly onto C_g.
   * Read Operation: Read line (RD) turns T_3 ON; if a logic 1 is stored, T_2 conducts, pulling the precharged bus down to ground (inverted data readout).
   * Readout Type: Non-destructive; reading does not wipe the stored gate charge.
   * Layout Footprint: Occupies roughly 1000\,\lambda^2 (or 500\lambda^2 in optimized cells), allowing >48\text{ kbits} (or \approx 5\text{ kbits} per 16\text{ mm}^2 chip).
 * 1-Transistor (1T) Dynamic Cell:
   * Circuit: Uses exactly one access transistor (M_1) and one storage capacitor (C_s).
   * Storage Capacitor Construction: Formed using a polysilicon plate over diffusion connected to V_{DD} to obtain sufficient capacitance (\approx 0.125\text{ pF}) within a minimal area.
   * Write Operation: Activating the Row-select line turns M_1 ON, driving C_s to V_{DD} for a 1 or Ground for a 0.
   * Read Operation: Precharging the bit line to V_{DD}/2 and turning M_1 ON causes charge-sharing between C_s and bit line capacitance (C_{BL}), detected via a sense amplifier.
   * Readout Type: Destructive; every read cycle dumps the charge and requires an immediate rewrite.
   * Layout Footprint: Requires only \approx 200\,\lambda^2 (1250\ \mu\text{m}^2 at \lambda = 2.5\ \mu\text{m}), accommodating up to 128\text{ kbits} of raw capacity on a 4\text{ mm} \times 4\text{ mm} die.
   * Volatility: Leakage currents drain C_s in \le 1\text{ to }2\text{ ms}, requiring periodic refresh cycles.
2. Pseudo-Static RAM / Register Cell
 * Operating Principle:
   * Built from two cascaded inverters with a gated feedback loop controlled by a two-phase clock (\phi_1, \phi_2).
   * Uses dynamic gate storage during active cycles, but acts static because it automatically refreshes its own data every clock cycle via feedback.
 * Phase-by-Phase Operation:
   * Write / Read (\phi_1): Input data enters on WR \cdot \phi_1; output is placed onto the bus on RD \cdot \phi_1.
   * Refresh (\phi_2): Feedback switch T_3 closes, feeding the inverted-and-restored output of Inverter 2 back to the gate of Inverter 1 to replenish leaked charge.
 * Essential Design Constraints:
   * WR and RD are mutually exclusive and must never activate at the same time.
   * Reading must never occur during clock phase \phi_2 to prevent destructive charge sharing between the bus line and storage node.
   * Cells must be layout-stackable horizontally and vertically, allowing bus lines to route straight through.
 * Area & Power Consumption:
   * Single-bus area is \approx 1750\lambda^2 (\approx 10{,}000\ \mu\text{m}^2 at \lambda = 2.5\ \mu\text{m}), yielding \approx 1.4\text{ kbits} on a 4\text{ mm} \times 4\text{ mm} die.
   * With an 8:1 (90\text{ k}\Omega) and 4:1 (45\text{--}50\text{ k}\Omega) inverter pair, average current draw is \approx 80\ \mu\text{A} at 5\text{ V}.
   * Dissipation per bit is 400\ \mu\text{W}, leading to \approx 560\text{ mW} total power for a 1.4\text{ kbit} array.
3. Dynamic Storage Elements & Shifters
 * Inverting Dynamic Cell:
   * Comprises a pass transistor (nMOS, 3 transistors total) or transmission gate (CMOS, 4 transistors total) feeding a single inverter.
   * Data clocked in during \phi charges C_g, presenting a stable complemented output (\overline{V_{\text{in}}}) until C_g discharges.
 * Non-Inverting Dynamic Cell:
   * Places two clocked inverting stages in series.
   * First stage clocks in data during \phi_1; second stage samples and inverts it again during \phi_2, outputting the true (uncomplemented) bit.
 * 4-Bit Dynamic Shift Register:
   * Connects 4 bit-cells (8 inverters total) in series using alternating non-overlapping clocks (\phi_1 and \phi_2).
   * Data steps rightward through the stages one inverter pair per clock period (\phi_1 \rightarrow \phi_2).
4. N-Bit Iterative CMOS Comparator
 * Inputs & Outputs per Cell (i):
   * Local Bit Inputs: A_i and B_i.
   * Cascading Inputs from Higher Stage (i+1): C_{i+1} (A > B) and D_{i+1} (A < B).
   * Stage Outputs: C_i (A > B) and D_i (A < B).
 * Truth Table Logic:
   * Higher Bit Precedence: If C_{i+1}D_{i+1} = 10, then C_iD_i = 10; if C_{i+1}D_{i+1} = 01, then C_iD_i = 01 (local inputs are "Don't Care").
   * Tie-Breaking (C_{i+1}D_{i+1} = 00):
     * A_i = B_i \implies C_iD_i = 00 (equality preserved).
     * A_i = 1, B_i = 0 \implies C_iD_i = 10 (A > B).
     * A_i = 0, B_i = 1 \implies C_iD_i = 01 (A < B).
5. Memory Sizing & Unit Conversion Summary
 * Binary vs. Decimal Kilo:
   * Binary Kilo (1024 = 2^{10}): Used for physical memory addressing and hardware bit capacities.
   * Decimal Kilo (1000 = 10^3): Used for rough power estimations (1.4\text{ kbits} \times 1000 = 1400\text{ bits} \implies 1400 \times 400\ \mu\text{W} = 560\text{ mW}).
 * Worked Chip Area Problem (10 kbits of 3T DRAM):
   * Bit cell area = 500\lambda^2 = 500 \times (2.5\ \mu\text{m})^2 = 3125\ \mu\text{m}^2.
   * Reference 4\text{ mm} \times 4\text{ mm} (16\text{ mm}^2) chip holds:
     
   * Area required to hold 10\text{ kbits}:
  