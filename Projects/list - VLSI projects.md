

  
To turn every project on your list into a job-ready portfolio piece, treat every single module like a mini silicon tapeout. Follow this **7-Stage VLSI Engineering Pipeline** from start to finish for every project.
### Copy-Paste Prompt to Stop AI From Giving You Toy Code

Whenever you start a new project from your roadmap, paste this prompt into your AI assistant first:


> **Role & Execution Rules:**
> 
> You are my Senior Staff VLSI & ASIC/FPGA Design Mentor. I am building **[PROJECT NAME]** as part of my VLSI engineering portfolio targeting a **Tang Nano 9K** (Gowin GW1NR-9 FPGA via Yosys + `nextpnr-himbaechl` + `openFPGALoader`, validated on real hardware via Raspberry Pi/Arduino) and **SkyWater Sky130 ASIC** (via OpenLane 2 + OpenSTA + KLayout).
> 
> **Strict Rules for How You Teach Me:**
> 
> 1. **No Passive Theory Walls:** Never just dump theory or tell me to "look at waveforms." Every single stage must give me **concrete, hands-on steps** I execute on my computer: exact terminal commands (`mkdir`, `git`, `verilator`, `pytest`, `sby`, `yosys`, `nextpnr-himbaechl`, `openFPGALoader`, `openlane`, `klayout`), exact files to create, and what tool output to verify.
>     
> 2. **Explain "Why" in Simple Words:** Before or right after every command, file, or design choice, explain _why_ we are doing it in plain, practical engineering terms (e.g., why separating `always_ff` and `always_comb` prevents latches, or why `REG_OUT` isolates setup/hold paths in OpenSTA).
>     
> 3. **One Stage at a Time:** Walk me through **one stage at a time**, ending with a clear verification checklist of deliverables for that stage, and **stop and wait for my approval** before moving to the next stage.
>     
> 
> ### Follow My 7-Stage Universal VLSI Project Pipeline:
> 
> - **Stage 1: Architecture, Paper Design & Repo Setup (Before Writing Code)**
>     
>     - **Goal:** Prove the hardware is engineered intentionally before writing line 1 of RTL.
>         
>     - **Hands-On Actions:** Initialize the standardized repository folder structure (`rtl/`, `tb/`, `formal/`, `fpga/`, `asic/`, `docs/`, `scripts/`) and root `Makefile` skeleton; define parameters, ports, bit-widths, latency, throughput, and edge cases in `docs/spec.md`; guide me step-by-step to draw and export the complete datapath block diagram (`docs/architecture.png`) and FSM diagram if applicable (`docs/fsm.png`) using Draw.io/Excalidraw/WaveDrom.
>         
>     - **Deliverables:** `docs/spec.md`, `docs/architecture.png` (and `docs/fsm.png` if needed), and initialized repo folders.
>         
> - **Stage 2: Clean, Lint-Free Synthesizable RTL**
>     
>     - **Goal:** Write industry-standard, parameterizable Verilog/SystemVerilog with zero latches, width mismatches, or combinational loops.
>         
>     - **Hands-On Actions:** Create parameterizable RTL in `rtl/` separating sequential (`always_ff` / `always @(posedge clk)`) and combinational (`always_comb` / `always @(*)`) blocks; run exact `verilator --lint-only -Wall` and `yosys -p "read_verilog ...; hierarchy -check"` commands to verify zero warnings.
>         
>     - **Deliverables:** Lint-clean RTL in `rtl/` and a passing `make lint` target.
>         
> - **Stage 3: Automated Self-Checking Verification + SVA**
>     
>     - **Goal:** Prove correctness automatically across thousands of edge cases without manually eyeballing waveforms.
>         
>     - **Hands-On Actions:** Write a Python Golden Reference Model and a Cocotb + Verilator testbench (`tb/`) testing directed corner cases (zeros, max values, signed/unsigned overflows, resets) plus 10,000+ constrained-random vectors with automatic cycle-by-cycle assertions; embed SystemVerilog Assertions (SVA) for illegal states/handshakes.
>         
>     - **Deliverables:** Automated test suite in `tb/` where `make sim` executes 10,000+ tests and prints `100% PASS`.
>         
> - **Stage 4: Formal Verification (Mathematical Proof)**
>     
>     - **Goal:** Mathematically prove zero deadlocks, livelocks, or protocol/flag violations across all reachable states.
>         
>     - **Hands-On Actions:** Create a formal wrapper (`formal/*.sv`) with `assume` and `assert` properties plus a SymbiYosys config (`formal/*.sby`); run `sby -f` with Z3/Boolector for Bounded Model Checking (BMC) and k-induction.
>         
>     - **Deliverables:** Passing `make formal` target with formal proof logs.
>         
> - **Stage 5: FPGA Synthesis, Timing & Real Hardware Validation (Tang Nano 9K)**
>     
>     - **Goal:** Meet real-world clock timing and validate on physical silicon via Hardware-in-the-Loop (HIL).
>         
>     - **Hands-On Actions:** Write Tang Nano 9K physical constraints (`fpga/tang_nano_9k.cst`) and top-level wrapper; synthesize and PnR with `yosys` + `nextpnr-himbaechl`; inspect STA reports for $F_{\max}$, setup slack, and LUT4/BSRAM usage; flash via `openFPGALoader`; run a Python host script over Raspberry Pi/Arduino (UART/SPI/GPIO) to test real silicon against the golden model.
>         
>     - **Deliverables:** `make fpga` bitstream, STA $F_{\max}$ & resource numbers, and passing HIL hardware test capture.
>         
> - **Stage 6: ASIC Physical Design & PPA Signoff (SkyWater Sky130)**
>     
>     - **Goal:** Execute full RTL-to-GDSII physical design and extract signoff Power, Performance, and Area (PPA).
>         
>     - **Hands-On Actions:** Create OpenLane 2 config (`asic/config.json`) and timing constraints (`asic/base.sdc`); run OpenLane 2 targeting `sky130A`; verify zero DRC and zero LVS errors; open final GDSII in KLayout to export `docs/gdsii.png`; extract silicon area ($\mu\text{m}^2$), worst setup/hold slack across Slow/Typical/Fast corners, and dynamic/leakage power ($\text{mW}$) from OpenSTA reports.
>         
>     - **Deliverables:** `make asic` clean GDSII, `docs/gdsii.png`, and complete PPA signoff table.
>         
> - **Stage 7: Portfolio Packaging & Bug Documentation**
>     
>     - **Goal:** Make the GitHub repo effortless for a VLSI hiring manager to review in 60 seconds.
>         
>     - **Hands-On Actions:** Finalize unified `Makefile` (`make lint`, `make sim`, `make formal`, `make fpga`, `make asic`); build a sharp `README.md` with Architecture Diagram, FPGA vs. Sky130 PPA Comparison Table, annotated GTKWave screenshot, KLayout GDSII render, and a **"Bugs Caught & Fixed"** engineering log.
>         
>     - **Deliverables:** Complete, reproducible GitHub portfolio repository.
>         
> 
> **Project Specification for This Session:**
> 
> - **[PROJECT NAME]:** Parameterized ALU — Design a configurable arithmetic logic unit supporting arithmetic (`ADD`, `SUB`), bitwise logic (`AND`, `OR`, `XOR`, `NOR`), shifts (`SLL`, `SRL`, `SRA`), comparisons (`SLT`, `SLTU`), `PASS_B`, and status flags (`Zero`, `Carry`, `Overflow`, `Negative`) with a registered output option (`REG_OUT`).
>     
> 
> **Start with Stage 1 ONLY.** Give me the exact step-by-step  instructions with simple explanations of why, and wait for my approval before moving to Stage 2.




> _"I am building [PROJECT NAME] as part of a VLSI engineering portfolio targeting a Tang Nano 9K (Gowin FPGA, Yosys/nextpnr) and SkyWater Sky130 ASIC (OpenLane 2). Do NOT just give me basic RTL and tell me to look at waveforms. Walk me through this in structured stages:_ _1. Microarchitecture & interface spec (ports, bit-widths, latency, edge cases)._ _2. Clean, parameterizable, Verilator-lint-clean Verilog RTL._ _3. A self-checking Cocotb testbench in Python with a golden reference model and constrained-random stimulus._ _4. SystemVerilog Assertions (SVA) and a SymbiYosys formal verification config._ _5. Synthesis constraints (SDC) and key timing/PPA metrics I should verify in Yosys and OpenLane._ _Let's start with Stage 1 only and wait for my approval before moving to Stage 2."_

### The 7-Stage Universal VLSI Project Pipeline

### Stage 1: Architecture & Paper Design (Before Writing Code)

- **The Goal:** Prove you engineered the hardware intentionally rather than guessing until it compiled.
    
- **What to Do:**
    
    - Draw a complete datapath block diagram showing every register, mux, bit-width, and control signal (use Draw.io, Excalidraw, or WaveDrom).
        
    - If the module uses control logic, draw the Finite State Machine (FSM) bubble diagram with exact transition conditions.
        
    - Calculate fixed-point bit-widths, latency cycles, and throughput targets on paper first.
        
- **Deliverable:** `docs/architecture.png` and `docs/fsm.png` saved in your repo before you write line 1 of Verilog.
    

### Stage 2: Clean, Lint-Free Synthesizable RTL

- **The Goal:** Write industry-standard Verilog/SystemVerilog that synthesizes cleanly without latches, combinational loops, or width mismatches.
    
- **What to Do:**
    
    - Separate sequential logic (`always_ff` / `always @(posedge clk)`) from combinational logic (`always_comb` / `always @(*)`).
        
    - Run **Verilator with `--lint-only -Wall`** and **Yosys `hierarchy -check`** to catch every subtle width mismatch or inferred latch.
        
    - Parameterize bit-widths and depths (`parameter WIDTH = 32`) so your module is reusable across later projects.
        
- **Deliverable:** Zero-warning RTL files in `rtl/` that pass strict Verilator linting.
    

### Stage 3: Automated Self-Checking Verification (No Eyeballing Waveforms)

- **The Goal:** Prove your design works across thousands of edge cases automatically, because nobody manually inspects 50,000 clock cycles in GTKWave.
    
- **What to Do:**
    
    - Write a **Python Golden Model** (using NumPy or pure Python) that calculates the exact expected mathematical output.
        
    - Build a **Cocotb testbench** driven by Verilator that feeds directed edge cases (zeros, max values, overflows, back-to-back resets) plus 10,000+ constrained-random inputs into your RTL.
        
    - Compare RTL outputs against your Python Golden Model automatically on every clock cycle—your testbench must print `PASS` or throw an assertion error on failure.
        
    - Add **SystemVerilog Assertions (SVA)** inside your RTL to catch illegal states (like FIFO overflow or invalid bus handshakes) the exact cycle they happen.
        
- **Deliverable:** Automated test suite in `tb/` where running `make sim` executes thousands of tests and reports `100% PASS`.
    

### Stage 4: Formal Verification (Mathematical Proof)

- **The Goal:** Catch rare 1-in-a-billion corner-case bugs (deadlocks, livelocks, protocol violations) that random simulation misses.
    
- **What to Do:**
    
    - Write a small formal wrapper (`formal/`) with `assume` (valid inputs) and `assert` (properties that must never break).
        
    - Run **SymbiYosys (sby)** with an SMT solver (Z3 or Boolector) for 20–50 clock cycles of Bounded Model Checking (BMC) and k-induction.
        
- **Deliverable:** A passing `make formal` target proving your block cannot deadlock or violate interface rules.
    

### Stage 5: FPGA Synthesis, Timing & Real Hardware Validation

- **The Goal:** Prove your design meets real-world clock speeds and works on physical silicon, not just in a simulator.
    
- **What to Do:**
    
    - Synthesize and Place-and-Route your design for the **Tang Nano 9K** using **Yosys + nextpnr-himbaechl** (and compare against Gowin EDA).
        
    - Read the **Static Timing Analysis (STA)** report: check your Maximum Clock Frequency (`Fmax`), setup slack, and LUT4/BSRAM usage. Fix critical paths if `Fmax` is too low.
        
    - Flash the bitstream to the Tang Nano 9K using `openFPGALoader`.
        
    - Use your **Raspberry Pi** (via GPIO/SPI/UART) or **Arduino** to send real test vectors to the FPGA and verify the hardware output against Python.
        
- **Deliverable:** FPGA resource & `Fmax` numbers, plus a photo/capture of the Tang Nano 9K passing hardware-in-the-loop tests.
    

### Stage 6: ASIC Physical Design & PPA Signoff (Sky130)

- **The Goal:** Show VLSI employers you understand physical silicon—standard cells, floorplanning, clock trees, parasitics, and power.
    
- **What to Do:**
    
    - Push your verified RTL through **OpenLane 2** targeting the **SkyWater Sky130 PDK** on your high-end PC.
        
    - Inspect the final **GDSII chip layout** in **KLayout** and verify **zero DRC (Design Rule Check)** and **zero LVS (Layout vs. Schematic)** errors.
        
    - Extract your **PPA (Power, Performance, Area)** metrics from the OpenLane/OpenSTA reports: silicon area (μm2\mu m^2μm2), worst setup/hold slack across Slow/Typical/Fast corners, and dynamic/leakage power (mW).
        
- **Deliverable:** High-resolution KLayout GDSII render (`docs/gdsii.png`) and a complete PPA summary table.
    

### Stage 7: Portfolio Packaging & Bug Documentation

- **The Goal:** Make your repository effortless for a hiring manager to evaluate in 60 seconds.
    
- **What to Do:**
    
    - Standardize every repo with a single `Makefile` (`make lint`, `make sim`, `make formal`, `make fpga`, `make asic`).
        
    - Write a sharp `README.md` containing: Block Diagram, PPA Comparison Table (FPGA vs. Sky130 ASIC), Annotated GTKWave screenshot showing a key transaction, and KLayout GDSII image.
        
    - **Write a "Bugs Caught & Fixed" section:** Document 1 or 2 real bugs you encountered (e.g., an off-by-one pipeline hazard or a timing violation) with before-and-after waveforms. Interviewers _love_ asking about bugs you debugged.
        
- **Deliverable:** A clean, reproducible GitHub repository ready to link on your resume.
    

### Summary Checklist: "Homework Mode" vs. "VLSI Job-Ready Mode"

|Step|What Basic AI Tells You to Do|What You Must Do for a VLSI Job|
|---|---|---|
|**Design**|Jump straight into coding Verilog|Draw block diagram & FSM states first|
|**Coding**|Write quick RTL, ignore warnings|Parameterized RTL + zero Verilator `--lint-only` warnings|
|**Testing**|Write a manual `initial` block, stare at waves|Python Golden Model + Cocotb randomized tests + SVA|
|**Proof**|None|SymbiYosys formal proof of no deadlocks/overflows|
|**FPGA**|Run Vivado behavioral sim|Yosys/nextpnr PnR on Tang Nano 9K + Pi/Arduino HIL test|
|**ASIC**|None|OpenLane Sky130 flow → GDSII + PPA & STA signoff|
|**Portfolio**|Upload raw `.v` files|`Makefile` + Block Diagram + PPA Table + Real Bug Log|

### How to Adapt This Pipeline Across Your Curriculum

Not every project in your list is a pure digital RTL block. Adjust Stages 5 & 6 depending on the track:

- **Digital Foundations, Processors & DSP:** Run all 7 stages identically. Compare different architectures in your PPA table (e.g., Ripple-Carry vs. Kogge-Stone adder area, delay, and power on both Tang Nano 9K and Sky130).
    
- **FPGA Interfacing & Hardware-Software Co-Design:** Focus heavily on **Stage 5**. Use your Raspberry Pi as a automated `pytest` controller over SPI/UART/GPIO, and wire up your **INA219 sensor** to measure real milliwatts on the Tang Nano 9K power rail.
    
- **ASIC Physical Design:** Start with an already-verified RTL block from Phase 1/3, then spend your energy on **Stage 6**—sweeping clock constraints, floorplan utilization, and clock tree synthesis in OpenROAD to fix negative slack.
    
- **Analog & Mixed-Signal VLSI:** Replace Stages 2–5 with **Xschem schematic capture →\rightarrow→ Ngspice PVT/Monte Carlo simulation →\rightarrow→ Magic custom layout →\rightarrow→ DRC/LVS & parasitic extraction**, then unite digital + analog in Stage 6/7.
    



**Hardware Allocation**

  

|**Platform**|**Primary Role**|**Capacity Limit**|**Target Workloads**|
|---|---|---|---|
|**Tang Nano 9K**|RTL prototyping|8,640 LUT4s|Pipelined RV32I, interfaces, HDMI, small DSP|
|**High-End PC**|ASIC and simulation|Workstation RAM/CPU|OpenLane GDSII, UVM, SPICE, superscalar cores|
|**Raspberry Pi**|HIL host controller|Linux GPIO speed|Automated Cocotb/pytest regression, SPI master|
|**Arduino**|Mixed-signal stimulus|16 MHz MCU|ADC sensor streaming, fault-injection target|
|**Discrete Parts**|Physical instrumentation|Breadboard parasitics|R-2R DAC, INA219 power rig, shunt side-channel|

The table above maps each piece of your hardware kit to its highest-value engineering role so you never bottleneck a large ASIC design on a small FPGA.

  

**Toolchain Setup**

  

- **RTL Simulation:** Install Verilator, Icarus Verilog, GTKWave, and Cocotb on Linux (or WSL2) to run cycle-accurate C++ and Python testbenches before touching hardware.
    
      
    
- **Open FPGA Flow:** Configure Yosys, nextpnr-himbaechl, Project Apicula, and openFPGALoader alongside vendor Gowin EDA to compare open-source versus proprietary synthesis results.
    
      
    
- **ASIC Physical Flow:** Deploy OpenLane 2, OpenROAD, SkyWater Sky130 PDK, Magic, KLayout, and Netgen in Docker to take any verified Verilog module all the way to fabrication-ready GDSII layout.
    
      
    
- **Analog SPICE Suite:** Set up Xschem and Ngspice linked to Sky130 device models for transistor-level schematic capture, DC/AC/transient simulation, and parasitic extraction.
    
      
    
- **Automation Stack:** Standardize every project with GNU Make, TCL synthesis scripts, Python golden models, and Git version control to mirror professional EDA workflows.
    
      
    

**Digital Foundations**

  

- **Parameterized ALU:** Design a configurable arithmetic logic unit supporting arithmetic, bitwise logic, shifts, and status flags (Zero, Carry, Overflow, Negative) with a self-checking testbench.
    
      
    
- **Barrel Shifter Library:** Build single-cycle logarithmic barrel shifters, priority encoders, and leading-zero counters optimized for minimal combinational logic depth.
    
      
    
- **Adder PPA Study:** Implement Ripple-Carry, Carry-Lookahead, Carry-Select, and Kogge-Stone prefix adders, tabulating area, critical path delay, and power oAn both Gowin FPGA and Sky130 ASIC.
    
      
    
- **Multiplier Comparison:** Synthesize Array, Wallace Tree, and Radix-4 Booth multipliers, comparing LUT fabric usage against hard Gowin 18x18 DSP slices and Sky130 standard cells.
    
      
    
- **Hardware Dividers:** Architect restoring, non-restoring, and SRT radix-2 fixed-point dividers with early termination logic, analyzing latency-versus-area trade-offs.
    
      
    
- **Pipelined CORDIC:** Build iterative and pipelined Coordinate Rotation Digital Computer cores to compute sine, cosine, arctangent, and vector rotations using only shifts and adds.
    
      
    
- **IEEE-754 FPU:** Design a 32-bit floating-point adder and multiplier supporting subnormal numbers, four rounding modes, and hardware exception flags.
    
      
    
- **Three-Block FSMs:** Write clean, synthesizable finite state machines (traffic controller or packet parser) using distinct state, next-state, and output blocks, then formally prove deadlock freedom.
    
      
    
- **CDC Lab:** Build two-flip-flop synchronizers, pulse synchronizers, and req-ack handshakes, intentionally injecting setup/hold violations in simulation to observe metastability failures.
    
      
    
- **Async Gray-Code FIFO:** Architect a dual-clock FIFO using Gray-code pointers and two-stage synchronizers to safely stream data between unrelated Raspberry Pi and FPGA clock domains.
    
      
    
- **CRC and PRBS Engine:** Create a parallelizable Cyclic Redundancy Check (CRC-32) generator paired with an LFSR Pseudo-Random Binary Sequence (PRBS) link tester.
    
      
    

**FPGA Interfacing**

  

- **UART with Flow Control:** Build a full-duplex UART transceiver with programmable baud generators, hardware RTS/CTS handshaking, majority-vote noise filtering, and internal FIFOs.
    
      
    
- **High-Speed SPI Core:** Design a configurable SPI master and slave supporting all four clock polarity/phase modes, validated at 50 MHz against a Raspberry Pi traffic generator.
    
      
    
- **Multi-Master I2C:** Implement a state-machine I2C controller supporting clock stretching, bus arbitration, and multi-byte bursts to read real-time data from discrete IMU or temperature sensors.
    
      
    
- **Dead-Time PWM Driver:** Architect a multi-channel PWM motor and inverter controller featuring programmable dead-time insertion and hardware fault-shutdown inputs.
    
      
    
- **Bare-Metal HDMI Engine:** Write an 8b/10b TMDS serializer from scratch on the Tang Nano 9K to output 720p video test patterns, Conway's Game of Life, and zoomable Mandelbrot fractals.
    
      
    
- **Hardware Sprite Terminal:** Design a VGA/HDMI text terminal and 2D tile graphics engine using character ROMs, hardware collision detection, and alpha blending.
    
      
    
- **On-Chip Logic Analyzer:** Build an internal triggerable logic analyzer that samples internal FPGA signals into Gowin BSRAM and streams captured waveforms over UART to GTKWave.
    
      
    
- **Digital Oscilloscope:** Combine an external high-speed SPI ADC, hardware trigger logic, dual-port video RAM, and your HDMI engine to build a real-time storage oscilloscope.
    
      
    
- **PSRAM Memory Controller:** Write a custom delay-locked state machine to initialize and execute burst reads and writes on the Tang Nano 9K's onboard 64 Mbit PSRAM.
    
      
    
- **Reciprocal Frequency Meter:** Implement a high-precision frequency and period counter using reciprocal counting across a reference PLL clock and external signal input.
    
      
    
- **PLL Jitter Lab:** Configure the Gowin rPLL to synthesize multiple clock domains, perform dynamic phase shifting, and measure real-world clock jitter on an external scope.
    
      
    

**Processor Microarchitecture**

  

- **Single-Cycle RV32I:** Design a baseline 32-bit RISC-V processor in Verilog executing the full RV32I base integer instruction set, verified with programs compiled via the RISC-V GNU toolchain.
    
      
    
- **Five-Stage Pipelined Core:** Upgrade your RV32I CPU into a five-stage pipeline with full data-forwarding multiplexers, load-use hazard stall logic, and branch flush control.
    
      
    
- **Branch Predictor Study:** Implement static, 2-bit saturating counter BHT, and Gshare branch predictors with a Branch Target Buffer (BTB), benchmarking Instructions Per Cycle (IPC) across Dhrystone loops.
    
      
    
- **RV32IM Hardware Extension:** Integrate your custom Booth multiplier and non-restoring divider into the pipeline execution stage to support the standard M-extension ISA.
    
      
    
- **L1 Cache Hierarchy:** Build direct-mapped instruction and two-way set-associative write-back data caches using BSRAM, complete with LRU replacement, dirty bits, and hit/miss performance counters.
    
      
    
- **Bus Interconnect Fabric:** Architect an AXI4-Lite or Wishbone crossbar switch and an APB peripheral bridge with round-robin arbitration and memory-mapped address decoding.
    
      
    
- **Scatter-Gather DMA:** Design a Direct Memory Access engine coupled with an ECC (SECDED Hamming code) memory controller to move sensor bursts into RAM without CPU intervention.
    
      
    
- **Tang Nano RISC-V SoC:** Integrate your pipelined core, cache, bus fabric, UART, SPI, timer, and PLIC/CLINT interrupt controllers on the Tang Nano 9K, booting bare-metal C firmware.
    
      
    
- **Custom ISA Extension:** Add custom SIMD dot-product or bit-manipulation instructions to your RISC-V decode/execute stages, modifying the assembler to emit custom opcodes.
    
      
    
- **Core Benchmarking Study:** Synthesize open-source SERV (bit-serial) and PicoRV32 cores alongside your custom CPU on the Tang Nano 9K and Sky130 to compare LUTs, Fmax, and energy per instruction.
    
      
    
- **Out-of-Order Simulator:** Use your PC to design and simulate a Tomasulo-based out-of-order execution engine in SystemVerilog featuring Reservation Stations, register renaming, and a Reorder Buffer.
    
      
    
- **Superscalar & Vector Unit:** Architect a dual-issue superscalar pipeline or a 4-lane SIMD vector co-processor with a custom Python assembler for parallel matrix workloads.
    
      
    

**DSP and Accelerators**

  

- **FIR Filter Architectures:** Build Direct, Transposed, Symmetric, and multiplierless Distributed Arithmetic FIR filters, analyzing fixed-point quantization noise against floating-point Python models.
    
      
    
- **IIR Biquad Equalizer:** Design a cascaded fixed-point IIR audio filter, studying coefficient sensitivity, overflow saturation logic, and zero-input limit-cycle oscillations.
    
      
    
- **Streaming Radix-2 FFT:** Implement a 64-point pipelined Fast Fourier Transform spectrum analyzer fed by an external microphone/ADC and rendered in real time over HDMI.
    
      
    
- **CIC Decimation Chain:** Build a Cascaded Integrator-Comb filter and polyphase FIR decimator to downsample high-rate bitstream data from an I2S MEMS microphone.
    
      
    
- **Sigma-Delta ADC/DAC:** Model a first-order and second-order Sigma-Delta modulator in Verilog paired with an external discrete RC low-pass stage to perform analog-to-digital conversion.
    
      
    
- **Systolic Array Engine:** Construct a 4x4 or 8x8 weight-stationary systolic array using Gowin DSP slices to perform parallel matrix multiplication with local register-to-register routing.
    
      
    
- **Quantized CNN Accelerator:** Build an INT8 or Binarized Neural Network (XNOR-popcount) inference engine with hardware ReLU/Sigmoid LUTs and zero-skipping sparsity logic for MNIST classification.
    
      
    
- **Streaming Vision Pipeline:** Use FPGA line buffers to compute real-time 3x3 Sobel edge detection and Gaussian blur convolutions on incoming video frames with zero frame-buffer latency.
    
      
    
- **Cryptographic Cores:** Implement iterative and pipelined AES-128, ChaCha20 stream cipher, and SHA-256 hash engines, validating throughput against NIST test vectors.
    
      
    
- **Forward Error Correction:** Design a hardware Hamming SECDED, Reed-Solomon, or hard-decision Viterbi convolutional decoder to correct burst errors over noisy communication links.
    
      
    
- **SDR Baseband Modem:** Combine a Direct Digital Synthesizer (DDS/NCO), digital mixer, and matched filter to modulate and demodulate FSK and BPSK baseband signals in hardware.
    
      
    

**Hardware-Software Co-Design**

  

- **Multi-Sensor Fusion Hub:** Acquire concurrent data from multiple I2C/SPI accelerometers and gyroscopes on the FPGA, run a fixed-point hardware Kalman filter, and stream fused orientation to the Raspberry Pi.
    
      
    
- **High-Speed Pi-to-FPGA Link:** Build a custom packetized SPI protocol with hardware CRC-32 checking and DMA storage to stream megabits per second between your Raspberry Pi and Tang Nano 9K.
    
      
    
- **Arduino Stimulus Generator:** Program your Arduino to act as a deterministic mixed-signal waveform, protocol-error, and asynchronous interrupt injector for FPGA stress testing.
    
      
    
- **FOC Motor Controller:** Implement Field-Oriented Control hardware blocks (Clarke transform, Park transform, and Space Vector PWM) in Verilog to drive a brushless DC motor with ultra-low loop latency.
    
      
    
- **Edge-AI PPA Shootout:** Run the exact same quantized neural network or PID control loop across your Arduino, Raspberry Pi, and Tang Nano 9K, publishing a latency, throughput, and joules-per-inference comparison table.
    
      
    
- **INA219 Power Rig:** Wire an INA219 current-sensing module onto the Tang Nano 9K power rail, logging real dynamic versus static power dissipation via Arduino/Pi across varying clock frequencies.
    
      
    
- **Hardware Security Lab:** Use your power-measurement rig and FPGA PLL delay lines to build a Ring Oscillator PUF, a metastable TRNG, a Side-Channel Correlation Power Analysis (CPA) rig, and a clock-glitch fault injector.
    
      
    

**Verification Engineering**

  

- **Constrained-Random Cocotb:** Write Python-driven randomized testbenches in Cocotb that stress-test your ALU, caches, and DSP cores against golden NumPy and PyCryptodome models.
    
      
    
- **SystemVerilog UVM Lite:** Build a modular SystemVerilog verification environment in Verilator featuring drivers, monitors, agents, scoreboards, and functional coverage collection.
    
      
    
- **Assertion-Based SVA:** Embed concurrent SystemVerilog Assertions directly into your AXI/Wishbone interconnects and FIFOs to catch protocol violations on the exact offending clock cycle.
    
      
    
- **Formal Verification Suite:** Use SymbiYosys and Z3/Boolector SMT solvers on your PC to mathematically prove that your FIFOs never overflow, arbiters never starve, and cryptographic keys never leak.
    
      
    
- **Bug-Injection Study:** Intentionally seed ten subtle architectural bugs (off-by-one counters, missing forwarding paths, CDC races) into your RTL and document your testbench's bug-detection rate.
    
      
    
- **Stuck-At Fault Simulator:** Run gate-level fault simulation to measure what percentage of single stuck-at-0 and stuck-at-1 manufacturing defects your verification vectors successfully detect.
    
      
    
- **Automated HIL Regression:** Connect your Raspberry Pi GPIO pins to the Tang Nano 9K to run overnight pytest hardware-in-the-loop regressions that verify millions of physical silicon cycles.
    
      
    

**ASIC Physical Design**

  

- **First RTL-to-GDSII Tapeout:** Push your parameterized ALU and CORDIC cores through OpenLane 2 on the Sky130 PDK, generating a clean GDSII layout with zero DRC or LVS errors.
    
      
    
- **Multi-Corner STA Signoff:** Analyze setup and hold timing across Slow-Slow, Typical-Typical, and Fast-Fast PVT corners in OpenSTA, writing SDC constraints for false paths and multicycle paths.
    
      
    
- **Timing Closure Lab:** Intentionally over-constrain your clock period to induce negative slack, then fix timing violations by pipelining RTL, resizing buffers, and restructuring combinational cones.
    
      
    
- **Floorplan and PDN Exploration:** Sweep core utilization percentages, aspect ratios, pin placements, and Power Distribution Network metal stripe pitches in OpenROAD to minimize IR drop and congestion.
    
      
    
- **Clock Tree Synthesis Study:** Compare H-tree and mesh clock distribution networks, logging clock skew, insertion delay, and clock-tree buffer power dissipation.
    
      
    
- **Low-Power Implementation:** Apply architectural clock gating, operand isolation, and multi-threshold-voltage cell swapping, quantifying dynamic and leakage power savings in OpenSTA.
    
      
    
- **DFT Scan-Chain Insertion:** Replace standard flip-flops with scan-enabled flops, stitch a full boundary and internal scan chain, and generate ATPG test patterns using open-source DFT tools.
    
      
    
- **Tiny Tapeout Silicon Submission:** Package your best compact design (such as a custom RISC-V peripheral or DSP core) into the Tiny Tapeout harness to have it fabricated on a real multi-project wafer.
    
      
    

**Analog and Circuit VLSI**

  

- **CMOS Inverter & Ring Oscillator:** Characterize CMOS inverter Voltage Transfer Curves (VTC), noise margins, and a 7-stage ring oscillator across PVT corners using Xschem and Ngspice on Sky130.
    
      
    
- **Custom Standard-Cell Library:** Hand-draw physical layouts for NAND2, NOR2, XOR2, and D-Flip-Flop cells in Magic/KLayout, run DRC/LVS, extract RC parasitics, and characterize a Liberty timing model.
    
      
    
- **gm/Id Op-Amp Design:** Design a two-stage Miller-compensated differential operational amplifier using the modern transconductance-efficiency (gm/Id) methodology rather than square-law approximations.
    
      
    
- **Bandgap and LDO Regulator:** Architect a temperature-independent CMOS bandgap voltage reference paired with a low-dropout (LDO) linear voltage regulator, verifying line/load regulation and loop stability.
    
      
    
- **6T SRAM Bitcell & Monte Carlo:** Design a 6-transistor SRAM cell with sense amplifiers and precharge circuitry, running 1,000-point Monte Carlo process-variation simulations to plot Read/Write butterfly curves.
    
      
    
- **Mixed-Signal SAR ADC & PLL:** Co-simulate a transistor-level dynamic latched comparator and capacitive DAC (or charge-pump VCO) in Ngspice alongside digital SAR control logic in Verilog.
    
      
    

**EDA and CAD Algorithms**

  

- **Event-Driven Logic Simulator:** Write a gate-level digital logic simulator in C++ or Python supporting inertial/transport delays, four-state logic (0, 1, X, Z), and VCD waveform output.
    
      
    
- **Graph-Based STA Engine:** Build a custom Static Timing Analyzer in Python that parses a synthesized Verilog netlist and Liberty file, builds a Directed Acyclic Graph, and calculates arrival/required times and slack.
    
      
    
- **BDD & SAT Equivalence Checker:** Implement a Reduced Ordered Binary Decision Diagram (ROBDD) package or PySAT-based miter circuit tool to formally prove two netlists are boolean-equivalent.
    
      
    
- **Simulated Annealing Placer:** Code a standard-cell placement tool in C++ that minimizes Half-Perimeter Wirelength (HPWL) via simulated annealing, exporting live animations of cell convergence.
    
      
    
- **Lee / A-Star Maze Router:** Build a multi-layer grid router that routes multi-terminal nets around blockages while enforcing preferred metal layer directions and via penalties.
    
      
    
- **Python Hardware Generator:** Use Amaranth HDL, MyHDL, or Chisel to build a highly parameterized hardware generator that emits optimized SystemVerilog for arbitrary filter taps or matrix dimensions.
    
      
    

**Flagship Capstones**

  

- **Capstone A (Full-Stack RISC-V SoC & Tapeout):** Boot C firmware on your pipelined RV32IM SoC on the Tang Nano 9K, verify it with Cocotb/Formal, and push the CPU core through OpenLane Sky130 to GDSII with full PPA signoff.
    
      
    
- **Capstone B (Edge-AI Accelerator & Quantization Flow):** Train a quantized neural network in PyTorch, export INT8 weights to a custom systolic array on the Tang Nano 9K, measure real power via INA219, and generate the Sky130 ASIC layout.
    
      
    
- **Capstone C (Mixed-Signal SAR ADC IC):** Design a complete 8-bit charge-redistribution SAR ADC with transistor-level comparator/CDAC in Magic/Ngspice and synthesized digital calibration/control logic in OpenLane.
    
      
    
- **Capstone D (Hardware Security & Cryptoprocessor SoC):** Integrate AES-128, SHA-256, TRNG, and a Ring Oscillator PUF into an AXI4-Lite peripheral block, paired with a real side-channel CPA attack and mitigation report.
    
      
    
- **Capstone E (Custom Superscalar / Out-of-Order Core + EDA Flow):** Design a dual-issue or Tomasulo out-of-order RISC-V processor on your PC accompanied by a custom Python assembler, UVM-style scoreboard, and Sky130 macro synthesis.
    
      
    

**Execution Roadmap**

  

|**Phase**|**Months**|**Primary Domain**|**Target Hardware**|**Milestone Deliverable**|
|---|---|---|---|---|
|**Phase 1**|1 to 2|Toolchain and RTL Foundations|PC + Tang Nano 9K|ALU, Adders, Booth, CORDIC, Async FIFO|
|**Phase 2**|3 to 4|FPGA Interfaces and Verification|Tang Nano + Pi/Arduino|UART, SPI, I2C, PSRAM, HDMI, Cocotb/Formal|
|**Phase 3**|5 to 7|Computer Architecture|Tang Nano + PC|5-Stage RV32IM SoC, Cache, Bus, C Firmware|
|**Phase 4**|8 to 10|ASIC Physical Flow and Analog|High-End PC (Sky130)|OpenLane GDSII, STA closure, 6T SRAM, Op-Amp|
|**Phase 5**|11 to 12|Accelerators, EDA, and Capstone|Full Stack Lab|Systolic CNN or Tapeout SoC + IEEE Paper|

Run verification (Cocotb + SymbiYosys) and ASIC synthesis (OpenLane PPA reports) continuously inside every phase rather than saving them for the final months.

  

**Portfolio Standards**

  

- **GitHub Repository Structure:** Give every project a clean directory layout (`rtl/`, `tb/`, `formal/`, `asic/`, `docs/`, `Makefile`) so recruiters can clone and run your simulations with a single command.
    
      
    
- **Mandatory README Visuals:** Include a high-resolution architectural block diagram, finite-state-machine diagram, annotated GTKWave timing screenshots, and KLayout GDSII renders in every project README.
    
      
    
- **Quantitative PPA Tables:** Report concrete engineering numbers for every block—LUT4 count, BSRAM usage, Fmax (MHz), Sky130 cell area (square micrometers), static/dynamic power (milliwatts), and IPC.
    
      
    
- **Failure and Bug Logs:** Dedicate a section in each README to real bugs you caught (such as an async FIFO Gray-code glitch or setup-time violation) and show the before-and-after waveforms.
    
      
    
- **Technical Writing & Open Source:** Publish three deep-dive engineering blog posts, write an IEEE-format conference paper for your capstone, and submit documentation or bug fixes to Yosys, Cocotb, or OpenLane.
    
      
    
- **Core Reference Textbooks:** Keep Harris & Harris (Digital Design and Computer Architecture), Weste & Harris (CMOS VLSI Design), Razavi (Design of Analog CMOS Integrated Circuits), and Patterson & Hennessy (RISC-V Edition) beside your workstation.