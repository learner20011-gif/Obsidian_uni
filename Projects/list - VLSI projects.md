

  



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
    
      
    
- **Adder PPA Study:** Implement Ripple-Carry, Carry-Lookahead, Carry-Select, and Kogge-Stone prefix adders, tabulating area, critical path delay, and power on both Gowin FPGA and Sky130 ASIC.
    
      
    
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