![[Pasted image 20261102000924.png|499]]![[Pasted image 20261102001105.png|503]]![[Pasted image 20261102010909.png]]![[Pasted image 20261102005917.png]]![[Pasted image 20261102005939.png]]![[Pasted image 20261102005954.png]]![[Pasted image 20261102010049.png]]![[Pasted image 20261102010144.png]]![[Pasted image 20261102012332.png]]![[Pasted image 20261102012727.png]]![[Pasted image 20261102014814.png]]![[Pasted image 20261102014848.png]]![[Pasted image 20261102014937.png]]![[Pasted image 20261102021918.png]]



#### 1. CMOS Latch-Up & Prevention (Q.1.37 / Q.1.35)

- **Definition:** An abnormal, low-impedance short-circuit between $V_{DD}$ and $V_{SS}$ caused by the unintentional turning-on of a parasitic four-layer ($p\text{-}n\text{-}p\text{-}n$) SCR (thyristor) structure.
    
- **Mechanism:**
    
    - Formed by two cross-coupled parasitic BJTs: a vertical PNP (PMOS source – n-well – p-substrate) and a lateral NPN (NMOS source – p-substrate – n-well).
        
    - A transient noise spike or current glitch drops $> 0.7\text{ V}$ across substrate resistance ($R_{sub}$) or well resistance ($R_{well}$), turning one BJT ON.
        
    - The collector of each transistor drives the base of the other, forming a regenerative positive feedback loop.
        
    - If the loop gain $\beta_{npn} \times \beta_{pnp} \ge 1$, the circuit latches into permanent high-current conduction, causing thermal destruction.
        
- **Prevention Methods:**
    
    - **Guard Rings:** Place $n^+$ (to $V_{DD}$) and $p^+$ (to $V_{SS}$) rings around MOS devices to collect stray carriers.
        
    - **Heavily Doped Substrate / Epi-Wafer:** Reduces $R_{sub}$ and $R_{well}$ so the voltage drop cannot reach $0.7\text{ V}$.
        
    - **Increase Spacing:** Separate PMOS and NMOS further apart to lower parasitic BJT gains ($\beta$).
        
    - **Trench Isolation / SOI:** Use oxide trenches or Silicon-on-Insulator to physically break the parasitic $p\text{-}n\text{-}p\text{-}n$ path.
#### BiCMOS Inverter: Base Current Discharge (Q.1.33)

- **The Problem:** When an NPN transistor turns OFF, minority carriers trapped in its base take time to recombine. Without a discharge path, this causes long turn-off delays and excessive dynamic power dissipation.
    
- **Resistor vs. MOS Discharge:**
    
    - **Resistor Discharge:** Connects bleed resistors from base to GND. However, it causes continuous static DC current flow and dissipates standby power.
        
    - **MOS Discharge (No Static Current):** Uses active NMOS switches to bleed base charge quickly. The NMOS gates turn off in steady state, cutting the DC current path completely.
        
- **Which is Better & Why:**
    
    - **MOS-based discharge is better.**
        
    - **Zero Static Power:** Eliminates DC power leakage during steady logic states.
        
    - **Faster Switching:** Active MOS switches provide a low-resistance path to clear base charges much faster than passive resistors.
        
    - **Smaller Silicon Area:** Active MOS transistors occupy far less silicon area than large diffusion resistors.