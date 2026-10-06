# 🛰️ Master Notes: Signals and Systems

---

## 📑 Module Directory
- [[#1. Signal Fundamentals & Operations]]
- [[#2. Energy & Power Signal Classification]]
- [[#3. System Properties & Classification]]
- [[#4. Laplace Transform (LT), s-Domain Circuits & ROC]]
- [[#5. Continuous-Time Fourier Transform (FT) & Parseval]]
- [[#6. Fourier Series (FS) & Circuit Analysis]]
- [[#7. Sampling, Modulation & Multiplexing]]
- [[#8. First-Order System Response & Switching Circuits]]
- [[#9. Second-Order System Response & RLC Dynamics]]
- [[#10. System Response Decompositions (ZIR/ZSR, Natural/Forced, Transient/SS)]]
- [[#11. Convolution Integral & LTI System Dynamics]]
- [[#12. Transfer Function, Pole-Zero Dynamics & Stability]]
- [[#13. Block Diagrams, State-Space & System Realizations]]
- [[#14. System Modeling & Electromechanical Analogies]]
- [[#15. Advanced Systems: Interconnected, Inverse & Distortionless]]
- [[#16. Network Synthesis (Foster, Cauer & PR Functions)]]

---

# 1. Signal Fundamentals & Operations

### 1.1. Core Signal Classifications
- **Continuous-Time (CT):** $x(t)$, defined $\forall t \in \mathbb{R}$.
- **Discrete-Time (DT):** $x[n]$, defined $\forall n \in \mathbb{Z}$.
- **Periodic:** $x(t + T) = x(t), \; \forall t$. Fundamental period $T_0 = \frac{2\pi}{\omega_0}$.
- **Causal Signal:** $x(t) = 0, \; \forall t < 0$.
- **Anti-Causal Signal:** $x(t) = 0, \; \forall t > 0$.

- **Signal Decomposition Pipeline:**
  $$x(t) = x_e(t) + x_o(t)$$
  - **Even Component:** $x_e(t) = \frac{1}{2}[x(t) + x(-t)] \implies x_e(-t) = x_e(t)$ (Symmetric across vertical axis).
  - **Odd Component:** $x_o(t) = \frac{1}{2}[x(t) - x(-t)] \implies x_o(-t) = -x_o(t)$ (Antisymmetric through origin).

---

### 1.2. Singularity & Elementary Functions

| Function | Mathematical Definition | Key Property / Relation |
| :--- | :--- | :--- |
| **Unit Impulse $\delta(t)$** | $\delta(t) = 0 \; (t \neq 0)$, $\int_{-\infty}^\infty \delta(t)dt = 1$ | $\int_{-\infty}^\infty x(t)\delta(t-t_0)dt = x(t_0)$ |
| **Unit Step $u(t)$** | $u(t) = \begin{cases} 1, & t > 0 \\ 0, & t < 0 \end{cases}$ | $\frac{d}{dt}u(t) = \delta(t)$, $\int_{-\infty}^t \delta(\tau)d\tau = u(t)$ |
| **Unit Ramp $r(t)$** | $r(t) = t \cdot u(t) = \begin{cases} t, & t \ge 0 \\ 0, & t < 0 \end{cases}$ | $\frac{d}{dt}r(t) = u(t)$, $\int_{-\infty}^t u(\tau)d\tau = r(t)$ |
| **Gate / Rectangular $\Pi(t/\tau)$** | $\text{rect}(t/\tau) = \begin{cases} 1, & \|t\| \le \tau/2 \\ 0, & \|t\| > \tau/2 \end{cases}$ | $\text{rect}(t/\tau) = u(t + \tau/2) - u(t - \tau/2)$ |
| **Signum $\text{sgn}(t)$** | $\text{sgn}(t) = \begin{cases} +1, & t > 0 \\ -1, & t < 0 \end{cases}$ | $\text{sgn}(t) = 2u(t) - 1 \implies \frac{d}{dt}\text{sgn}(t) = 2\delta(t)$ |

---

### 1.3. Impulse Properties Cheat-Sheet
- **Sifting (Sampling):** 
  $$\int_{-\infty}^{\infty} x(t)\,\delta(t - t_0)\,dt = x(t_0)$$
- **Multiplication:** 
  $$x(t)\,\delta(t - t_0) = x(t_0)\,\delta(t - t_0)$$
- **Time Scaling:** 
  $$\delta(at) = \frac{1}{|a|}\delta(t)$$
- **Even Symmetry:** 
  $$\delta(-t) = \delta(t)$$
- **Derivative of Windowed Product:**
  $$\frac{d}{dt}\big(t[u(t) - u(t-a)]\big) = [u(t) - u(t-a)] - a\,\delta(t-a)$$
  *(Note: $t\,\delta(t) = 0 \cdot \delta(0) = 0$ at origin)*

---

### 1.4. Piecewise Signal Synthesis

#### Direct Jump Rule (Flat Steps)
![[Pasted image 20260628100445.png]]

- At each transition instant $t = a$:
  $$\Delta (\text{amplitude}) = \text{Level}_{\text{new}} - \text{Level}_{\text{old}}$$
  $$\text{Term} = \Delta (\text{amplitude}) \cdot u(t - a)$$
- **Example Formulation:**
  - $t=0$: $0 \to 10 \implies +10u(t)$
  - $t=2$: $10 \to 5 \implies -5u(t-2)$
  - $t=4$: $5 \to 0 \implies -5u(t-4)$
  $$\therefore h(t) = 10u(t) - 5u(t-2) - 5u(t-4)$$

#### Direct Slope Rule (Ramps)
- At each slope change $t = b$:
  $$\Delta m = m_{\text{new}} - m_{\text{old}}$$
  $$\text{Term} = \Delta m \cdot r(t - b)$$

---

### 1.5. Signal Transformations: $x(at - b)$

- **Transformation Roadmap ($x(t) \to x(at - b)$):**
  - **Method 1 (Shift $\to$ Scale):**
    $$x(t) \xrightarrow{\text{Shift by } b} x(t - b) \xrightarrow{\text{Scale } t \to at} x(at - b)$$
    *(Compress/expand by $a$, shift remains $b$)*
  - **Method 2 (Scale $\to$ Shift):**
    $$x(t) \xrightarrow{\text{Scale } t \to at} x(at) \xrightarrow{\text{Shift } t \to t - b/a} x\left(a\left(t - \frac{b}{a}\right)\right) = x(at - b)$$
    *(Desired shift must be divided by scaling factor $a$)*
- **Direct Coordinate Mapping:**
  $$t_{\text{new}} = \frac{t_{\text{old}} + b}{a}$$
- **Time Inversion ($a < 0$):**
  - Reflect horizontally across vertical axis.

---

### 1.6. Periodicity of Summed Signals
$$x(t) = x_1(t) + x_2(t) + \dots + x_N(t)$$

1. **Condition:**
   $$\frac{T_1}{T_2} = \frac{m}{n} \in \mathbb{Q} \quad (m, n \in \mathbb{Z}^+ \text{ are coprime integers})$$
   - Rational ratio $\implies$ **Periodic**
   - Irrational ratio $\implies$ **Aperiodic (Non-periodic)**
2. **Fundamental Period ($T_0$):**
   $$T_0 = n T_1 = m T_2 = \text{LCM}(T_1, T_2)$$
3. **Examples:**
   - $\sin(2\pi t) + \sin(4\pi t)$: $T_1 = 1$, $T_2 = 0.5 \implies \frac{T_1}{T_2} = \frac{2}{1} \in \mathbb{Q} \implies T_0 = 1\text{ s}$ ✅
   - $\sin(10t) + \sin(\pi t)$: $T_1 = \frac{\pi}{5}$, $T_2 = 2 \implies \frac{T_1}{T_2} = \frac{\pi}{10} \notin \mathbb{Q} \implies$ **Aperiodic** ❌

---

# 2. Energy & Power Signal Classification

### 2.1. Fundamental Definitions

- **Total Energy ($E$):**
  $$E = \int_{-\infty}^{\infty} |x(t)|^2\,dt$$
  $$\boxed{0 < E < \infty \implies P = 0 \quad (\text{Energy Signal})}$$

- **Average Power ($P$):**
  $$P = \lim_{T \to \infty} \frac{1}{2T}\int_{-T}^T |x(t)|^2\,dt \quad \left(P = \frac{1}{T_0}\int_0^{T_0}|x(t)|^2\,dt \text{ if periodic}\right)$$
  $$\boxed{0 < P < \infty \implies E = \infty \quad (\text{Power Signal})}$$

- **Neither:** $E = \infty$ and $P = \infty$ (or $P = 0$ with $E = \infty$, e.g., $t \cdot u(t)$).
- **RMS Value:**
  $$X_{\text{rms}} = \sqrt{P}$$

---

### 2.2. Standard Signal Energy & Power Table

| Signal $x(t)$ | Type | Total Energy $E$ | Average Power $P$ | RMS Value |
| :--- | :--- | :--- | :--- | :--- |
| **DC Constant $A$** | Power | $\infty$ | $A^2$ | $\|A\|$ |
| **Sinusoid $A\cos(\omega_0 t + \theta)$** | Power | $\infty$ | $\frac{A^2}{2}$ | $\frac{A}{\sqrt{2}}$ |
| **Complex Exp $D e^{j\omega_0 t}$** | Power | $\infty$ | $\|D\|^2$ | $\|D\|$ |
| **Decaying Exp $e^{-at}u(t) \; (a > 0)$** | Energy | $\frac{1}{2a}$ | $0$ | $0$ |
| **Left-Sided Exp $e^{kt}u(-t) \; (k > 0)$** | Energy | $\frac{1}{2k}$ | $0$ | $0$ |
| **Left-Sided Exp $e^{-at}u(-t) \; (a > 0)$** | Neither | $\infty$ (blows up at $-\infty$) | $\infty$ | Undefined |
| **Pulse Rect $A\,[u(t) - u(t-\tau)]$** | Energy | $A^2 \tau$ | $0$ | $0$ |
| **Ramp $t \cdot u(t)$** | Neither | $\infty$ | $\infty$ | Undefined |

---

# 3. System Properties & Classification

### 3.1. System Property Fast-Check Matrix

- **Linearity:** Superposition check $\mathcal{T}\{a x_1 + b x_2\} \stackrel{?}{=} a y_1 + b y_2$
  - Satisfies Additivity + Homogeneity $\implies$ **Linear**
  - Fails either $\implies$ **Non-Linear**
- **Time-Invariance:** Time-shift check $\mathcal{T}\{x(t - t_0)\} \stackrel{?}{=} y(t - t_0)$
  - Identical outputs $\implies$ **Time-Invariant (TI)**
  - Differing outputs $\implies$ **Time-Variant (TV)**
- **Causality:** Temporal dependence:
  - Output depends strictly on $t \le t_{\text{present}}$ $\implies$ **Causal**
  - Output depends on any $t > t_{\text{present}}$ $\implies$ **Non-Causal**
- **Memory:** Instantaneous vs Interval dependence:
  - Output depends strictly on current instant $t = t_{\text{present}}$ $\implies$ **Memoryless (Instantaneous)**
  - Output depends on past/future or slopes/derivatives $\implies$ **Dynamic (With Memory)**
- **Invertibility:** Uniqueness of input mapping:
  - $1$-to-$1$ mapping $\implies$ **Invertible** ($x(t)$ uniquely retrievable)
  - Many-to-$1$ mapping $\implies$ **Non-Invertible**
- **BIBO Stability:** Magnitude bounding:
  - $|x(t)| \le M_x < \infty \implies |y(t)| \le M_y < \infty \implies$ **BIBO Stable**
  - Any bounded input yields unbounded output $\implies$ **Unstable**

---

### 3.2. Linearity: Physical vs Mathematical Perspective

![[Pasted image 20261006151932.png]]

- **Axioms:**
  1. **Additivity:** $\mathcal{T}\{x_1 + x_2\} = \mathcal{T}\{x_1\} + \mathcal{T}\{x_2\}$
  2. **Homogeneity (Scaling):** $\mathcal{T}\{k x\} = k \mathcal{T}\{x\}$
- **Mathematical View:** Operator $H$ satisfies $H\{a x_1 + b x_2\} = a H\{x_1\} + b H\{x_2\}$. Differential equations have only linear powers of dependent variables with no cross-products or transcendental functions.
- **Physical View:** Strict proportionality between cause and effect; no clipping, thresholds, or saturation.
- **Why Study Linear Systems:**
  - Analytical tractability: Solvable using Laplace, Fourier, convolution, and phasors.
  - Superposition: Complex signals decompose into impulses/sinusoids.
  - Real-world approximation: Most systems operate linearly in small-signal ranges.
- **Effects of Non-Linearity on Performance:**
  - **Harmonic Distortion:** Generates integer multiple harmonics $n\omega_0$.
  - **Intermodulation Distortion:** Generates sum/difference frequencies $\omega_1 \pm \omega_2$.
  - **Clipping / Saturation:** Amplitudes exceed supply rail ($V_{\text{cc}}$), destroying signal shape.
  - **Superposition Failure:** Invalidation of modal and frequency decomposition methods.

- **Classic Linearity Diagnostic Traps:**
  - $y(t) = \text{Re}\{x(t)\}$: Fails homogeneity for complex scalar $k = j$ ($j\text{Re}\{x\} \neq \text{Re}\{jx\}$) $\implies$ **Non-Linear**.
  - $y(t) = \frac{x^2(t)}{\dot{x}(t)}$: Satisfies homogeneity ($\frac{k^2 x^2}{k \dot{x}} = k y$), fails additivity $\implies$ **Non-Linear**.
  - $y(t) = x(t) + C \; (C \neq 0)$: Offset violates $H\{0\} = 0$ $\implies$ **Non-Linear**.
  - $\frac{dy}{dt} + t^2 y(t) = (2t + 3)x(t)$: Time-varying coefficients, but linear in $y, \dot{y}, x$ $\implies$ **Linear**.
  - $y(t) \frac{dy}{dt} + 3y(t) = x(t)$: Cross-product term produces $k^2$ $\implies$ **Non-Linear**.

---

### 3.3. Time-Invariance & Visual Mapping

![[Pasted image 20261006152843.png|587]]

- **Test Procedure:**
  1. Delayed input response: $y_1(t) = \mathcal{T}\{x(t - T)\}$.
  2. Delayed output: $y_2(t) = y(t - T)$ (substitute $t \to t - T$ everywhere).
  3. Equal $\implies$ **TI**; Unequal $\implies$ **TV**.
- **Inspection Rules:**
  - Explicit $t$ multiplier outside $x(\cdot)$ (e.g., $t \cdot x(t)$, $(1-t)x(t)$, $\cos(\omega_c t)x(t)$) $\implies$ **Time-Variant (TV)**.
  - Internal time scaling/inversion (e.g., $x(2t)$, $x(-t)$, $x(1-t)$) $\implies$ **Time-Variant (TV)**.
  - Constant coefficient operations (e.g., $\frac{d}{dt}x(t)$, $x(t-2)$, $2x(t)$) $\implies$ **Time-Invariant (TI)**.
- **Visual Input-Output Mapping Examples:**
  - Rectangular pulse $x(t) \in [0,1]$ maps to ramp $y(t) = t \implies y(t) = t \cdot x(t)$ $\implies$ **Linear, TV, Causal, Memoryless**.
  - Rectangular pulse $x(t) \in [0,1]$ maps to falling ramp $y(t) = 1 - t \implies y(t) = (1 - t)x(t)$ $\implies$ **Linear, TV, Causal, Memoryless**.

---

### 3.4. Causality & Memory Diagnostic Traps

- **Causality Definition:** Output at $t_0$ depends strictly on $x(t)$ for $t \le t_0$.
- **Memory Definition:** Output at $t_0$ depends strictly on $x(t_0)$ alone.
- **Diagnostics:**
  - $y_1(t) = t \cdot x(t + 1)$: At $t = 0$, requires $x(1)$ (future) $\implies$ **Non-Causal, TV, Memoryless? No (Dynamic)**.
  - $y_2(t) = x(1 - t)$: At $t = -2$, requires $x(3)$ (future) $\implies$ **Non-Causal, TV**.
  - $y(t) = x(t) - 0.5(t + 1)$: Depends strictly on present $x(t)$ $\implies$ **Causal, Memoryless, TV, Non-Linear**.
  - Ideal Differentiator $y(t) = \frac{dx}{dt}$: Requires two adjacent points in time $\implies$ **Dynamic (With Memory), Causal, Linear, TI**.
  - Ideal Integrator $y(t) = \int_{-\infty}^t x(\tau)d\tau$: Accumulates past history $\implies$ **Dynamic, Causal, Linear, TI**.

---

### 3.5. Invertibility & BIBO Stability

![[Pasted image 20261006153006.png]]

- **Invertibility Condition:** Distinct inputs produce distinct outputs (1-to-1 mapping).
  - Non-invertible: $y = x^2(t)$, $|x(t)|$, Saturation clipper, $y(t) = t \cdot x(t)$ ($x(0)$ is destroyed), Differentiator $\dot{x}(t)$ (DC constant lost).
  - Invertible: $y(t) = x(t - t_0)$, $y(t) = x(-t)$, $y(t) = 2x(t) + 5$.
- **BIBO Stability:** $|x(t)| \le M_x < \infty \implies |y(t)| \le M_y < \infty$.
  - Bounded signals: DC constant, $\sin(\omega t)$, $\cos(\omega t)$, $u(t)$.
  - Unbounded signals: $r(t) = t u(t)$, $e^{at}u(t) \; (a>0)$.
  - Example: $y(t) = t \cdot x(t)$ with bounded input $x(t) = u(t) \implies y(t) = t \cdot u(t) \to \infty$ $\implies$ **Unstable**.
  - Example: $y(t) = x(t) + 2$ with bounded input $|x(t)| \le M_x \implies |y(t)| \le M_x + 2 < \infty$ $\implies$ **Stable**.
- **Discrete Moving-Average Systems:**
  - $y[n] = \frac{1}{3}(x[n] + x[n-1] + x[n-2])$: Causal, Dynamic, Linear, TI, Stable ($|y[n]| \le M_x$).
  - $y[n] = \frac{1}{3}(x[n+1] + x[n] + x[n-1])$: **Non-Causal** (needs future $x[n+1]$), Dynamic, Linear, TI, Stable.

---

# 4. Laplace Transform (LT), s-Domain Circuits & ROC

### 4.1. Core Definitions
- **Bilateral (Two-Sided) LT:**
  $$X(s) = \int_{-\infty}^{\infty} x(t) e^{-st}\,dt, \quad s = \sigma + j\omega$$
- **Unilateral (One-Sided) LT:**
  $$X(s) = \int_{0^-}^{\infty} x(t) e^{-st}\,dt$$
- **Convergence Mechanism:** Damping factor $\sigma = \text{Re}\{s\}$ forces convergence:
  $$\int_{-\infty}^\infty |x(t)e^{-\sigma t}|\,dt < \infty$$

---

### 4.2. s-Domain Circuit Equivalent Models

![[Screenshot_20261005_023903_Xodo.jpg]]

- **Inductor ($L$):**
  - Time-Domain: $v(t) = L \frac{di}{dt}$
  - Transform: $V(s) = sL I(s) - L i(0^-)$
  - **Series Model:** Impedance $sL$ in series with voltage source $L i(0^-)$ (opposing current direction).
  - **Parallel Model:** Admittance $\frac{1}{sL}$ in parallel with current source $\frac{i(0^-)}{s}$ (pointing in current direction).
- **Capacitor ($C$):**
  - Time-Domain: $i(t) = C \frac{dv}{dt}$
  - Transform: $I(s) = sC V(s) - C v(0^-)$
  - **Series Model:** Impedance $\frac{1}{sC}$ in series with voltage source $\frac{v(0^-)}{s}$ (same polarity as $v(0^-)$).
  - **Parallel Model:** Admittance $sC$ in parallel with current source $C v(0^-)$ (pointing toward positive terminal).

---

### 4.3. Region of Convergence (ROC) Geometry

- **Poles:** ROC **NEVER** contains any poles.
- **Right-Sided Signals ($t \to +\infty$, Causal):**
  $$e^{at}u(t) \iff \frac{1}{s - a}, \quad \text{ROC: } \text{Re}\{s\} > a \quad (\text{Right-Half Plane})$$
- **Left-Sided Signals ($t \to -\infty$, Anti-Causal):**
  $$-e^{at}u(-t) \iff \frac{1}{s - a}, \quad \text{ROC: } \text{Re}\{s\} < a \quad (\text{Left-Half Plane})$$
- **Two-Sided Signals:**
  $$x(t) = x_R(t) + x_L(t) \implies \text{ROC: } \sigma_R < \text{Re}\{s\} < \sigma_L \quad (\text{Vertical Strip})$$
  *(If $\sigma_R > \sigma_L$, intersection is empty $\implies$ LT does not exist)*
- **Finite-Duration Signals:**
  $$\text{ROC: Entire } s\text{-plane} \quad (\text{except possibly } s = 0 \text{ or } s = \infty)$$
- **Stability & Causality Link:**
  - BIBO Stable $\iff$ ROC contains $j\omega$-axis ($\text{Re}\{s\} = 0$).
  - Causal + BIBO Stable $\iff$ All poles lie strictly in Left-Half Plane ($\text{Re}\{p_k\} < 0$).

---

### 4.4. Heaviside Partial Fraction Expansion (PFE) Cheat-Sheet

Applies to strictly proper rational functions $F(s) = \frac{N(s)}{D(s)}$ with $\deg(N) < \deg(D)$:

#### Case 1: Distinct Real Poles
$$D(s) = (s - p_1)(s - p_2)\dots(s - p_n) \implies F(s) = \sum_{k=1}^n \frac{A_k}{s - p_k}$$
$$A_k = \left. (s - p_k) F(s) \right|_{s = p_k}$$
- **Cover-up rule:** Cover up $(s - p_k)$ and substitute $s = p_k$ into the rest.

#### Case 2: Repeated Real Poles $(s - p)^m$
$$F(s) = \frac{A_m}{(s - p)^m} + \frac{A_{m-1}}{(s - p)^{m-1}} + \dots + \frac{A_1}{s - p} + \dots$$
$$A_{m-k} = \frac{1}{k!} \left. \frac{d^k}{ds^k}\left[ (s - p)^m F(s) \right] \right|_{s = p}, \quad k = 0, 1, \dots, m-1$$
- Highest power ($k=0$): Direct cover-up.
- Successive lower powers: Differentiate $k$ times and divide by $k!$.

#### Case 3: Complex Conjugate Poles
- Quadratic denominator: $s^2 + 2\alpha s + \omega_0^2 = (s + \alpha)^2 + \beta^2$ where $\beta = \sqrt{\omega_0^2 - \alpha^2}$.
- Decompose linear numerator: $A_1 s + A_2 = A_1 (s + \alpha) + B_1 \beta$.
  $$F(s) = \frac{A_1(s + \alpha)}{(s + \alpha)^2 + \beta^2} + \frac{B_1 \beta}{(s + \alpha)^2 + \beta^2}$$
  $$\mathcal{L}^{-1}\{F(s)\} = \left( A_1 e^{-\alpha t}\cos(\beta t) + B_1 e^{-\alpha t}\sin(\beta t) \right)u(t)$$

---

### 4.5. Laplace Transform Properties

| Property | Time Domain $x(t)$ | $s$-Domain $X(s)$ | ROC |
| :--- | :--- | :--- | :--- |
| **Linearity** | $a x_1(t) + b x_2(t)$ | $a X_1(s) + b X_2(s)$ | At least $R_1 \cap R_2$ |
| **Time Scaling** | $x(at)$ | $\frac{1}{\|a\|} X\left(\frac{s}{a}\right)$ | Scaled by $a$ |
| **Time Shift** | $x(t - t_0)u(t - t_0)$ | $e^{-s t_0} X(s)$ | Same as $X(s)$ |
| **Frequency Shift** | $e^{s_0 t} x(t)$ | $X(s - s_0)$ | Shifted by $\text{Re}\{s_0\}$ |
| **Time Derivative** | $\frac{d}{dt}x(t)$ | $s X(s) - x(0^-)$ | At least $R$ |
| **Time $n$-th Deriv**| $\frac{d^n}{dt^n}x(t)$ | $s^n X(s)$ (bilateral) | At least $R$ |
| **Time Integration** | $\int_{-\infty}^t x(\tau)d\tau$ | $\frac{1}{s}X(s)$ | $R \cap \{\text{Re}\{s\} > 0\}$ |
| **Periodic Wave** | $x(t) = x(t + T)$ | $\frac{X_1(s)}{1 - e^{-sT}}$ | $\text{Re}\{s\} > 0$ |

---

# 5. Continuous-Time Fourier Transform (FT) & Parseval

### 5.1. Core Formulas & Dirichlet Conditions
- **Forward FT:** 
  $$X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t}\,dt$$
- **Inverse FT:** 
  $$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j\omega t}\,d\omega$$
- **Dirichlet Conditions:**
  1. $\int_{-\infty}^{\infty} |x(t)|\,dt < \infty$ (absolutely integrable).
  2. Finite extrema in any finite interval.
  3. Finite number of jump discontinuities; no infinite discontinuities.

---

### 5.2. Fundamental Fourier Transform Pairs

| Signal $x(t)$ | Transform $X(\omega)$ | Notes / Derivation Trick |
| :--- | :--- | :--- |
| **Impulse $\delta(t)$** | $1$ | Sifting integral |
| **DC Constant $1$** | $2\pi \delta(\omega)$ | Duality from $\delta(t) \iff 1$ |
| **Complex Exp $e^{j\omega_0 t}$** | $2\pi \delta(\omega - \omega_0)$ | Frequency shift of DC |
| **Cosine $\cos(\omega_0 t)$** | $\pi [\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ | Euler's identity |
| **Sine $\sin(\omega_0 t)$** | $\frac{\pi}{j}[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)]$ | Euler's identity |
| **Signum $\text{sgn}(t)$** | $\frac{2}{j\omega}$ | Limit of $e^{-a\|t\|}\text{sgn}(t)$ as $a \to 0$ |
| **Unit Step $u(t)$** | $\pi \delta(\omega) + \frac{1}{j\omega}$ | $u(t) = \frac{1}{2} + \frac{1}{2}\text{sgn}(t)$ |
| **Causal Exp $e^{-at}u(t) \; (a>0)$** | $\frac{1}{a + j\omega}$ | Direct integration |
| **Double Exp $e^{-a\|t\|} \; (a>0)$** | $\frac{2a}{a^2 + \omega^2}$ | Sum of causal and anti-causal |
| **Gate / Rect $\Pi(t/\tau)$** | $\tau\,\text{sinc}\left(\frac{\omega\tau}{2}\right)$ | Sinc spectrum |
| **Bandlimited Sinc $\frac{W}{\pi}\text{sinc}(Wt)$** | $\text{rect}\left(\frac{\omega}{2W}\right)$ | Duality of rectangular pulse |

---

### 5.3. Key Properties & Theorems
- **Time Scaling:** $x(at) \iff \frac{1}{|a|}X\left(\frac{\omega}{a}\right)$ (Compression in time $\to$ Expansion in frequency).
- **Time Shifting:** $x(t - t_0) \iff e^{-j\omega t_0} X(\omega)$.
- **Modulation:** $x(t)\cos(\omega_0 t) \iff \frac{1}{2}[X(\omega - \omega_0) + X(\omega + \omega_0)]$.
- **Differentiation:** $\frac{d^n x}{dt^n} \iff (j\omega)^n X(\omega)$.
- **Integration:** $\int_{-\infty}^t x(\tau)d\tau \iff \frac{X(\omega)}{j\omega} + \pi X(0)\delta(\omega)$.
- **Duality:** $x(t) \iff X(\omega) \implies X(t) \iff 2\pi x(-\omega)$.
- **Convolution:** $x_1(t) * x_2(t) \iff X_1(\omega) X_2(\omega)$.
- **Parseval's Theorem (Rayleigh's Energy):**
  $$E = \int_{-\infty}^{\infty} |x(t)|^2\,dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(\omega)|^2\,d\omega = \int_{-\infty}^\infty |X(f)|^2\,df$$
  - Non-periodic signals: Energy distributed continuously over spectrum via Energy Spectral Density $S_{xx}(\omega) = |X(\omega)|^2$.
  - Periodic signals: Power concentrated at discrete harmonic line frequencies $n\omega_0$.
  - Band Energy: $W_{[\omega_1, \omega_2]} = \frac{1}{\pi}\int_{\omega_1}^{\omega_2} |X(\omega)|^2 d\omega$.
- **Traps:**
  - Ramp $r(t) = t u(t)$ has **no Fourier Transform** because $\int |r(t)|dt = \infty$ (violates absolute integrability).
  - Time-limited signals are **band-unlimited** (analytic function cannot be compactly supported in both domains simultaneously).

---

# 6. Fourier Series (FS) & Circuit Analysis

### 6.1. Three Representations of Fourier Series

$$\text{Trigonometric FS (TFS)} \xleftrightarrow{\text{Polar grouping}} \text{Compact / Polar FS (CFS)} \xleftrightarrow{\text{Euler identity}} \text{Complex Exponential FS (EFS)}$$

1. **Trigonometric Fourier Series (TFS):**
   $$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]$$
   $$a_0 = \frac{1}{T}\int_0^T f(t)\,dt, \quad a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t)\,dt, \quad b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t)\,dt$$
2. **Compact / Polar Fourier Series (CFS):**
   $$f(t) = a_0 + \sum_{n=1}^{\infty} A_n \cos(n\omega_0 t + \theta_n)$$
   $$A_n = \sqrt{a_n^2 + b_n^2}, \quad \theta_n = -\arctan\left(\frac{b_n}{a_n}\right), \quad \mathbf{V}_n = a_n - jb_n$$
3. **Complex Exponential Fourier Series (EFS):**
   $$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}, \quad c_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t) e^{-j n \omega_0 t}\,dt$$
   $$c_0 = a_0, \quad c_n = \frac{1}{2}(a_n - jb_n) = \frac{A_n}{2}e^{j\theta_n}, \quad |c_n| = \frac{A_n}{2}, \quad \angle c_n = \theta_n$$

---

### 6.2. Waveform Symmetries Table

| Symmetry | Definition | Eliminated Terms | Surviving Coefficients | Integration Range |
| :--- | :--- | :--- | :--- | :--- |
| **Even** | $f(-t) = f(t)$ | $b_n = 0$ | $a_0, a_n$ | $\frac{4}{T}\int_0^{T/2} f(t)\cos(n\omega_0 t)dt$ |
| **Odd** | $f(-t) = -f(t)$ | $a_0 = 0, a_n = 0$ | $b_n$ only | $\frac{4}{T}\int_0^{T/2} f(t)\sin(n\omega_0 t)dt$ |
| **Half-Wave (HWS)** | $f(t \pm T/2) = -f(t)$ | $a_0 = 0$, all even harmonics | $a_n, b_n$ for **odd $n$ only** | $\frac{4}{T}\int_0^{T/2} f(t)\cdot (\dots)dt$ |
| **Even HWS** | Even + HWS | $b_n = 0$, all even $n$ | $a_n$ for **odd $n$ only** | $\frac{8}{T}\int_0^{T/4} f(t)\cos(n\omega_0 t)dt$ |
| **Odd HWS** | Odd + HWS | $a_n = 0$, all even $n$ | $b_n$ for **odd $n$ only** | $\frac{8}{T}\int_0^{T/4} f(t)\sin(n\omega_0 t)dt$ |

---

### 6.3. Line Spectra & Circuit Frequency Response
- **Amplitude Spectrum:** Discrete plot of $|c_n|$ vs $\omega = n\omega_0$ (Even symmetry: $|c_{-n}| = |c_n|$).
- **Phase Spectrum:** Discrete plot of $\angle c_n$ vs $\omega = n\omega_0$ (Odd symmetry: $\angle c_{-n} = -\angle c_n$).
- **LTI Circuit Harmonic Response:**
  $$v_i(t) = \sum V_{i,n} \cos(n\omega_0 t + \theta_n) \implies v_o(t) = \sum |H(jn\omega_0)| V_{i,n} \cos(n\omega_0 t + \theta_n + \angle H(jn\omega_0))$$
- **Average Power in Resistor $R$:**
  $$P_{\text{avg}} = \frac{1}{R}\left[ V_{\text{dc}}^2 + \sum_{n=1}^\infty \frac{|V_{o,n}|^2}{2} \right]$$

---

# 7. Sampling, Modulation & Multiplexing

### 7.1. Sampling Theorem (Nyquist-Shannon)
- **Nyquist Rate:** $f_s \ge 2 f_{\max} = 2B$ ($\omega_s \ge 2\omega_m$).
- **Nyquist Interval:** $T_s \le \frac{1}{2B}$.
- **Sampled Spectrum:** $X_s(\omega) = \frac{1}{T_s}\sum_{k=-\infty}^\infty X(\omega - k\omega_s)$.
- **Regimes:**
  - $f_s > 2B$: Oversampling; guard band present; reconstruction with practical LPF.
  - $f_s = 2B$: Critical Nyquist rate; brick-wall ideal LPF required.
  - $f_s < 2B$: Undersampling; spectral overlap (**Aliasing**); irrecoverable distortion.

---

### 7.2. Amplitude & Angle Modulation
- **Amplitude Modulation (AM / DSB-SC):**
  $$s(t) = m(t)\cos(\omega_c t) \iff S(\omega) = \frac{1}{2}[M(\omega - \omega_c) + M(\omega + \omega_c)]$$
  - Purpose: Translates baseband signal to high-frequency bandpass; reduces antenna size ($\text{Length} \approx \lambda/4 = c/(4f)$).
  - Demerits of AM: Low power efficiency (carrier takes most power), high noise susceptibility, bandwidth waste ($2B$).
  - Demodulation: Envelope detector (diode + RC) for full AM; Coherent/synchronous detector (multiplier + LPF) for DSB-SC.
- **Angle Modulation (FM & PM):**
  - Phase Modulation: $\theta(t) = \omega_c t + k_p m(t)$.
  - Frequency Modulation: $\omega_i(t) = \omega_c + k_f m(t) \implies \theta(t) = \omega_c t + k_f \int m(\tau)d\tau$.
  - **Carson's Rule (FM Bandwidth):**
    $$B_{\text{FM}} \approx 2(\Delta f + f_m) = 2 f_m (\beta + 1)$$

---

### 7.3. Multiplexing: FDM vs TDM

| Feature | Frequency Division Multiplexing (FDM) | Time Division Multiplexing (TDM) |
| :--- | :--- | :--- |
| **Domain Sharing** | Spectrum partitioned into non-overlapping frequency slots | Time axis partitioned into non-overlapping time slots |
| **Signal Type** | Primarily Analog (requires carrier modulation) | Primarily Digital / Pulse-coded (PAM, PCM) |
| **Separation Guard** | Guard Bands (frequency intervals) | Guard Times (time intervals) |
| **Synchronization** | Carrier frequency alignment | Frame & clock timing synchronization |
| **Crosstalk Cause** | Non-linear amplifier intermodulation | Pulse spreading / imperfect timing |

---

### 7.4. Z-Transform (ZT) Fundamentals
- **Bilateral Definition:** $X(z) = \sum_{n=-\infty}^\infty x[n] z^{-n}, \quad z = r e^{j\Omega}$.
- **ROC Properties:** ROC contains **NO poles**.
  - Right-Sided (Causal): Exterior of circle $|z| > r_{\max}$.
  - Left-Sided (Anti-Causal): Interior of circle $|z| < r_{\min}$.
  - Two-Sided: Annular ring $r_1 < |z| < r_2$.
  - BIBO Stability: ROC includes the unit circle $|z| = 1$.

---

# 8. First-Order System Response & Switching Circuits

### 8.1. Governing Equation & Time Constant ($\tau$)

![[Pasted image 20261004144136.png]]

- **Standard 1st-Order DC ODE:**
  $$\frac{dx(t)}{dt} + \frac{1}{\tau}x(t) = \frac{x_\infty}{\tau}$$
- **Time Constant Definition:** Time needed for natural response to decay to $1/e \approx 36.8\%$ of initial value (or step response to reach $1 - 1/e \approx 63.2\%$).
  $$\tau = R_{\text{Th}} C \quad (\text{RC Circuit}), \qquad \tau = \frac{L}{R_{\text{Th}}} \quad (\text{RL Circuit})$$
- **5-$\tau$ Rule:** Exponential reaches $99.3\%$ of steady state after $5\tau$. Considered fully settled for practical engineering.

---

### 8.2. Universal Complete Response Formulation

$$\boxed{x(t) = x(\infty) + [x(0^+) - x(\infty)] e^{-t/\tau}, \quad t \ge 0}$$
$$\boxed{x(t) = x(\infty) + [x(t_0^+) - x(\infty)] e^{-(t - t_0)/\tau}, \quad t \ge t_0}$$

- **Continuity Constraints:**
  $$v_C(0^+) = v_C(0^-), \qquad i_L(0^+) = i_L(0^-)$$
  *(Resistor voltages, inductor voltages, and capacitor currents CAN jump discontinuously at $t = 0^+$!)*

---

### 8.3. Source-Free First-Order Topologies

![[Pasted image 20261004150543.png]] ![[Pasted image 20261004150521.png]]

- **Source-Free RC Circuit:**
  $$v_C(t) = V_0 e^{-t/RC}, \quad w_C(0) = \frac{1}{2} C V_0^2$$
- **Source-Free RL Circuit:**
  $$i_L(t) = I_0 e^{-t/(L/R)}, \quad w_L(0) = \frac{1}{2} L I_0^2$$

---

### 8.4. Step-by-Step Circuit Switching Algorithm

```
Step 1: Evaluate t = 0- (DC Steady-State)
        Capacitors -> OPEN, Inductors -> SHORT
        Calculate v_C(0-) and i_L(0-)
                  │
                  ▼
Step 2: Enforce Continuity at t = 0+
        v_C(0+) = v_C(0-), i_L(0+) = i_L(0-)
                  │
                  ▼
Step 3: Analyze t > 0 Circuit Topology
        Deactivate independent sources (Voltage -> Short, Current -> Open)
        Calculate R_Th seen by storage element (Use test source if dependent sources present)
        Compute tau = R_Th*C or tau = L/R_Th
                  │
                  ▼
Step 4: Evaluate t -> ∞ (Final DC Steady-State)
        Capacitors -> OPEN, Inductors -> SHORT
        Calculate x(∞)
                  │
                  ▼
Step 5: Assemble Complete Response Equation
        x(t) = x(∞) + [x(0+) - x(∞)] e^(-t/tau)
```

---

### 8.5. Practical Timing & Pulse Applications

#### 1. Neon Lamp Relaxation Oscillator
![[Pasted image 20261005161437.png]]
- **Mechanism:**
  - Lamp off ($R = \infty$): Capacitor charges toward DC supply $V_s$ through $R_1 + R_2$ with $\tau_{\text{charge}} = (R_1 + R_2)C$.
  - When $v_C(t) = V_{\text{fire}} = 70\text{ V}$, lamp fires and drops to $R_{\text{on}} \approx 100\ \Omega$.
  - Capacitor discharges rapidly with $\tau_{\text{discharge}} \approx R_{\text{on}} C$ until $v_C(t) = V_{\text{ext}} = 30\text{ V}$.
  - Lamp turns off; cycle repeats. Flash period $T = t_{\text{charge}} + t_{\text{discharge}}$.

#### 2. Electronic Photo-Flash Unit
![[Pasted image 20261005161421.png]]
- **Mechanism:**
  - **Position 1 (Slow Charge):** Connects to high voltage DC supply via large resistor $R_1$. Limits battery surge current; large $\tau_1 = R_1 C$.
  - **Position 2 (Fast Discharge):** Switches capacitor across flash tube via very low resistance $R_2$. Small $\tau_2 = R_2 C$ produces massive current pulse ($i = v_C / R_2$), generating intense optical burst.

#### 3. Relay Actuation Delay
- Relay coil ($R_{\text{coil}}, L_{\text{coil}}$) with pull-in current $I_{\text{close}}$:
  $$i_L(t) = \frac{V_s}{R}\left(1 - e^{-t/\tau}\right) \implies t_{\text{close}} = -\tau \ln\left(1 - \frac{I_{\text{close}}}{V_s / R}\right)$$

---

# 9. Second-Order System Response & RLC Dynamics

### 9.1. General Governing Equation & Topologies

![[Pasted image 20261004135654.png]]

- **Definition:** Contains two independent energy storage elements governed by a 2nd-order ODE:
  $$\frac{d^2 x(t)}{dt^2} + 2\alpha \frac{dx(t)}{dt} + \omega_0^2 x(t) = f(t)$$
- **Characteristic Algebraic Equation:**
  $$s^2 + 2\alpha s + \omega_0^2 = 0 \implies s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

---

### 9.2. RLC Parameters Reference Matrix

| Metric / Parameter | Series RLC Circuit | Parallel RLC Circuit |
| :--- | :--- | :--- |
| **Primary Variable** | Loop current $i_L(t)$ / Cap voltage $v_C(t)$ | Node voltage $v_C(t)$ / Ind current $i_L(t)$ |
| **Undamped Natural Freq $\omega_0$** | $\frac{1}{\sqrt{LC}}$ | $\frac{1}{\sqrt{LC}}$ |
| **Damping Factor (Neper Freq) $\alpha$** | $\frac{R}{2L}$ | $\frac{1}{2RC}$ |
| **Damping Ratio $\zeta = \alpha / \omega_0$** | $\frac{R}{2}\sqrt{\frac{C}{L}}$ | $\frac{1}{2R}\sqrt{\frac{L}{C}}$ |
| **Quality Factor $Q = \frac{\omega_0}{2\alpha} = \frac{1}{2\zeta}$** | $\frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$ | $\frac{R}{\omega_0 L} = R\sqrt{\frac{C}{L}}$ |

---

### 9.3. Four Damping Regimes Matrix

![[Pasted image 20261004193537.png]]

| Damping Regime | Condition | Roots $s_{1,2}$ | Natural Response Form $x_n(t)$ | Physical Dynamic Behavior |
| :--- | :--- | :--- | :--- | :--- |
| **Overdamped** | $\alpha > \omega_0$ ($\zeta > 1$) | Real, negative, unequal ($s_1 \neq s_2 < 0$) | $A_1 e^{s_1 t} + A_2 e^{s_2 t}$ | Sluggish non-oscillatory decay; dominated by slow root. |
| **Critically Damped** | $\alpha = \omega_0$ ($\zeta = 1$) | Real, negative, repeated ($s_{1,2} = -\alpha$) | $(A_1 + A_2 t)e^{-\alpha t}$ | Fastest recovery to equilibrium without overshoot; peaks at $t = 1/\alpha$. |
| **Underdamped** | $\alpha < \omega_0$ ($\zeta < 1$) | Complex conjugate pairs ($-\alpha \pm j\omega_d$) | $e^{-\alpha t}\left[A_1\cos(\omega_d t) + A_2\sin(\omega_d t)\right]$ | Sinusoidal oscillations inside exponential envelope; frequency $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$. |
| **Undamped** | $\alpha = 0$ ($R = 0 \text{ or } \infty$) | Pure imaginary ($\pm j\omega_0$) | $A_1\cos(\omega_0 t) + A_2\sin(\omega_0 t)$ | Sustained perpetual sinusoidal oscillation; zero dissipation (ideal LC tank). |

- **Underdamped Overshoot Formula:**
  $$M_p = e^{-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}} \times 100\%$$

---

### 9.4. Pure RC-RC & RL-RL Second-Order Networks

- Networks with two capacitors or two inductors separated by resistors:
  $$\frac{d^2 v}{dt^2} + a_1 \frac{dv}{dt} + a_0 v = f(t)$$
- **Key Properties:**
  - Energy is purely dissipated across resistors without reactive exchange between $L$ and $C$.
  - Roots $s_1, s_2$ are **strictly real and negative**.
  - System is **strictly overdamped** ($\zeta > 1, Q < 0.5$); **cannot oscillate**.
  - Cascaded 2-stage RC filter has coupling loading term:
    $$a_1 = \frac{1}{R_1 C_1} + \frac{1}{R_2 C_2} + \frac{1}{R_2 C_1}, \qquad a_0 = \frac{1}{R_1 R_2 C_1 C_2}$$

---

### 9.5. Complete Second-Order Solution Framework

$$x(t) = x(\infty) + x_n(t)$$

1. **Find Initial Conditions ($t = 0^-$ and $0^+$):** $v_C(0^+) = v_C(0^-)$, $i_L(0^+) = i_L(0^-)$.
2. **Find Initial Derivatives ($t = 0^+$):**
   $$\left.\frac{di_L}{dt}\right|_{0^+} = \frac{v_L(0^+)}{L}, \qquad \left.\frac{dv_C}{dt}\right|_{0^+} = \frac{i_C(0^+)}{C}$$
   *(Obtain $v_L(0^+)$ or $i_C(0^+)$ by writing KVL/KCL at $t=0^+$).*
3. **Find Steady-State $x(\infty)$:** Capacitors open, inductors short.
4. **Solve for Constants $A_1, A_2$:**
   $$\text{Eq 1: } x(0^+) = x(\infty) + x_n(0^+)$$
   $$\text{Eq 2: } \left.\frac{dx}{dt}\right|_{0^+} = \left.\frac{dx_n}{dt}\right|_{0^+}$$

---

### 9.6. Application: Automobile Ignition System

![[Pasted image 20261005143126.png]]

- **$t < 0$ (Switch Closed):**
  - Battery ($E = 12\text{ V}$) charges primary ignition coil ($L_1 = 8\text{ mH}$) through wiring resistance ($R = 4\ \Omega$).
  - Current reaches DC steady state: $i_L(0^-) = \frac{12}{4} = 3\text{ A}$.
  - Capacitor ($C = 1\ \mu\text{F}$) is shorted by closed switch: $v_C(0^-) = 0\text{ V}$.
  - Maximum magnetic energy stored: $w_L = \frac{1}{2}L_1 i^2$.
- **$t \ge 0$ (Breaker Switch Opens):**
  - Current diverted suddenly into capacitor $C$, forming series RLC.
  - Large $di/dt$ produces massive back-EMF pulse across primary coil:
    $$v_L(t) = -268 e^{-250t}\sin(11,180t)\text{ V}$$
  - Secondary step-up winding ($M$) magnifies pulse to tens of kilovolts:
    $$|v_{2}(t)|_{\max} = \frac{M}{L_1} \cdot Q \cdot E$$
  - High voltage arcs across spark plug gap, igniting fuel mixture.

---

# 10. System Response Decompositions (ZIR/ZSR, Natural/Forced, Transient/SS)

### 10.1. Decomposition Taxonomies Comparison

```
Total Response y(t)
 ├── By Energy Source:      Zero-Input Response (ZIR)  +  Zero-State Response (ZSR)
 ├── By Governing Physics:  Natural Response (y_n)     +  Forced Response (y_f)
 └── By Time Horizon:       Transient Response (y_tr)  +  Steady-State Response (y_ss)
```

| Classification | Component 1 | Component 2 | Mathematical Characterization |
| :--- | :--- | :--- | :--- |
| **By Energy Source** | **Zero-Input Response (ZIR)** | **Zero-State Response (ZSR)** | $y(t) = y_{\text{zir}}(t) + y_{\text{zsr}}(t)$ |
| | Input $x(t) \equiv 0$; driven solely by initial stored energy ($v_C(0^-), i_L(0^-)$). | Initial states $= 0$; driven solely by applied input signal $x(t)$. | In $s$-domain: $Y(s) = \frac{P(s)}{D(s)} + H(s)X(s)$. |
| **By Governing Physics**| **Natural Response ($y_n$)** | **Forced Response ($y_f$)** | $y(t) = y_n(t) + y_f(t)$ |
| | Homogeneous solution of ODE; determined by system poles (natural frequencies). | Particular solution of ODE; mirrors input waveform form and input frequency. | Roots from characteristic equation vs roots from excitation. |
| **By Time Horizon** | **Transient Response ($y_{\text{tr}}$)** | **Steady-State Response ($y_{\text{ss}}$)** | $y(t) = y_{\text{tr}}(t) + y_{\text{ss}}(t)$ |
| | Decays to zero as time progresses: $\lim_{t \to \infty} y_{\text{tr}}(t) = 0$. | Persists indefinitely as $t \to \infty$ (DC level or sustained sinusoid). | For stable circuits, transient $\equiv$ terms with negative real exponents. |

---

### 10.2. Ideal Integrator Decomposition Example

$$y(t) = y(0) + \int_{0}^t x(\tau)\,d\tau$$
- **Zero-Input Response:** $y_{\text{zir}}(t) = y(0)$ (constant memory of initial state).
- **Zero-State Response:** $y_{\text{zsr}}(t) = \int_{0}^t x(\tau)\,d\tau$ (integral of input with zero initial state).

---

# 11. Convolution Integral & LTI System Dynamics

### 11.1. Definition & Core Properties

$$y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau)\,d\tau = \int_{-\infty}^\infty h(\tau) x(t - \tau)\,d\tau$$

- **Commutative:** $x(t) * h(t) = h(t) * x(t)$
- **Distributive:** $x * (h_1 + h_2) = x * h_1 + x * h_2$
- **Associative:** $x * (h_1 * h_2) = (x * h_1) * h_2$
- **Time-Shift:** $x(t - t_1) * h(t - t_2) = y(t - t_1 - t_2)$
- **Impulse Sifting:** $x(t) * \delta(t - t_0) = x(t - t_0)$
- **Differentiation:** $\frac{d}{dt}[x * h] = \dot{x} * h = x * \dot{h}$
- **Step / Impulse Relationship:**
  $$s(t) = \int_{-\infty}^t h(\tau)\,d\tau \iff h(t) = \frac{ds(t)}{dt}$$

---

### 11.2. Graphical Convolution Protocol

![[Pasted image 20261005182028.png]]

- **Step 1: Transformation:** Express both signals in dummy variable $\tau \to x(\tau), h(\tau)$.
- **Step 2: Fold (Inversion):** Horizontally invert $h(\tau) \to h(-\tau)$.
- **Step 3: Shift:** Shift by time parameter $t \to h(t - \tau)$.
- **Step 4: Multiplication:** Identify overlapping intervals between $x(\tau)$ and $h(t - \tau)$.
- **Step 5: Integration:** Compute area under product curve over active overlap limits.
- **Duration / Support Rule:**
  $$\text{Duration of } y(t) = (\text{Duration of } x(t)) + (\text{Duration of } h(t))$$
  $$\text{Range: } [t_{x,\min} + t_{h,\min}, \; t_{x,\max} + t_{h,\max}]$$

---

# 12. Transfer Function, Pole-Zero Dynamics & Stability

### 12.1. Transfer Function Formalism

$$H(s) = \frac{Y(s)}{X(s)} = \frac{b_m s^m + b_{m-1} s^{m-1} + \dots + b_0}{a_n s^n + a_{n-1} s^{n-1} + \dots + a_0} = K \frac{\prod_{i=1}^m (s - z_i)}{\prod_{j=1}^n (s - p_j)}$$
- **Poles ($p_j$):** Roots of denominator $D(s)$; values where $H(s) \to \infty$.
- **Zeros ($z_i$):** Roots of numerator $N(s)$; values where $H(s) = 0$.
- **Impulse Response:** $h(t) = \mathcal{L}^{-1}\{H(s)\}$.

---

### 12.2. Pole Locations & Stability Classification

![[SmartSelect_20261006_020610_Xodo.jpg|229]]

- **BIBO Stability Theorem:** An LTI system is BIBO stable if and only if its impulse response is absolutely integrable:
  $$\int_{-\infty}^\infty |h(t)|\,dt < \infty$$
- **s-Plane Pole Placement Criteria:**
  - **Asymptotically / BIBO Stable:** All poles lie strictly in the open Left-Half Plane ($\text{Re}\{p_k\} < 0$).
  - **Unstable:** Any pole lies in the Right-Half Plane ($\text{Re}\{p_k\} > 0$), OR repeated poles lie on the $j\omega$-axis (causes $t \sin(\omega_0 t)$ term).
  - **Marginally Stable:** One or more simple (non-repeated) poles lie on the $j\omega$-axis ($\text{Re}\{p_k\} = 0$), and no poles lie in the RHP. Produces sustained oscillations (bounded response to impulse, but unbounded response to sinusoidal input at that frequency).

---

### 12.3. Routh-Hurwitz Stability Criterion (2nd Order)
$$s^2 + a_1 s + a_0 = 0 \implies \text{Stable } \iff a_1 > 0 \quad \text{and} \quad a_0 > 0$$
- **Active Filter Stability Boundaries:**
  - $H(s) = \frac{10}{s^2 + (k - 5)s + 10} \implies$ Stable for $k > 5$; Sustained oscillation for $k = 5$.
  - $G(s) = \frac{1}{s^2 + (\beta + 4)s + 4} \implies$ Stable for $\beta > -4$; Sustained oscillation for $\beta = -4$.

---

### 12.4. Cascade Stability Trap (Pole-Zero Cancellation)
- Given $H_1(s) = \frac{1}{s - 1}$ (unstable pole at $+1$) and $H_2(s) = \frac{s - 1}{s + 1}$ (zero at $+1$):
  $$H_{\text{overall}}(s) = H_1(s) H_2(s) = \frac{1}{s + 1}$$
- **The Trap:** Overall transfer function appears BIBO stable!
- **Physical Reality:** The internal state between stages blows up exponentially ($e^t$). The composite system is **internally / asymptotically unstable**. Never cancel RHP poles with zeros!

---

# 13. Block Diagrams, State-Space & System Realizations

### 13.1. Basic Interconnections

![[Pasted image 20261006141214.png]]

- **Cascade (Series):** $H(s) = H_1(s) H_2(s)$.
- **Parallel:** $H(s) = H_1(s) + H_2(s)$.
- **Negative Feedback:** $T(s) = \frac{G(s)}{1 + G(s)H(s)}$ (Positive feedback: $T(s) = \frac{G(s)}{1 - G(s)H(s)}$).

---

### 13.2. Realization Forms

![[Pasted image 20261006141659.png]] ![[Pasted image 20261006142016.png]] ![[Pasted image 20261006142634.png|411]]

- **Integrator vs Differentiator Preference:**
  - Differentiator has transfer function $s$; magnitude $|j\omega| = \omega \to \infty$ at high frequencies. Amplifies high-frequency noise and drives op-amps into saturation.
  - Integrator has transfer function $1/s$; magnitude $|1/j\omega| = 1/\omega \to 0$ at high frequencies. Naturally suppresses noise; universally preferred.
- **Direct Form I:** Realizes numerator (feedforward zeros) and denominator (feedback poles) independently; requires $2n$ integrators.
- **Direct Form II (Canonical):** Shares a single central chain of integrators; requires minimal number of integrators ($n$ for $n$-th order system).
- **Cascade Form:** Factorizes $H(s)$ into product of 1st and 2nd order sub-blocks: $H(s) = \prod H_k(s)$.
- **Parallel Form:** Expands $H(s)$ via partial fractions into sum of sub-blocks: $H(s) = c_0 + \sum \frac{A_k}{s - p_k}$.

---

### 13.3. State-Space Representation

$$\mathbf{\dot{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) \quad (\text{State Equation})$$
$$\mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) \quad (\text{Output Equation})$$

- **Definitions:**
  - **State Variables $\mathbf{x}(t)$:** Minimal set of variables whose values at $t_0$, combined with inputs for $t \ge t_0$, uniquely determine future system behavior. Standard circuit state variables: Capacitor voltages $v_C$ and Inductor currents $i_L$.
  - **State Vector:** Column vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$.
  - **System Matrix $\mathbf{A}$:** $n \times n$ matrix governing internal dynamics.
- **Transfer Function Matrix Formula:**
  $$\boxed{\mathbf{H}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}}$$

---

# 14. System Modeling & Electromechanical Analogies

### 14.1. Elements & D'Alembert's Principle

![[Pasted image 20261005235119.png]]

- **D'Alembert's Principle:** The vector sum of external applied forces and inertial resisting forces equals zero:
  $$\sum F_{\text{applied}} - \sum F_{\text{opposing}} = 0 \iff \sum F = 0$$
- **Translational Elements:**
  - Mass ($M$): $f_M = M \frac{d^2 x}{dt^2} = M \frac{dv}{dt}$.
  - Damper / Dashpot ($B$): $f_B = B \frac{dx}{dt} = B v$.
  - Spring ($K$): $f_K = K x = K \int v\,dt$.

---

### 14.2. Electrical-Mechanical Analogy Conversion Table

![[Pasted image 20261006004020.png]] ![[Pasted image 20261006004419.png]]

| Mechanical Translational | Mechanical Rotational | Force-Voltage ($F$-$V$) / Loop Analogy | Force-Current ($F$-$I$) / Nodal Analogy |
| :--- | :--- | :--- | :--- |
| **Force $f(t)$** | Torque $\tau(t)$ | Voltage $v(t)$ | Current $i(t)$ |
| **Velocity $v(t)$** | Angular Velocity $\omega(t)$ | Current $i(t)$ | Voltage $v(t)$ |
| **Displacement $x(t)$** | Angular Disp. $\theta(t)$ | Charge $q(t)$ | Magnetic Flux $\phi(t)$ |
| **Mass $M$** | Moment of Inertia $J$ | Inductance $L$ | Capacitance $C$ |
| **Friction / Damper $B$** | Torsional Damper $B$ | Resistance $R$ | Conductance $G = 1/R$ |
| **Spring Constant $K$** | Torsional Spring $K$ | Elastance $1/C$ (Reciprocal Cap) | Inverse Inductance $1/L$ |
| **Sum of Forces $\sum f = 0$**| Sum of Torques $\sum \tau = 0$ | KVL $\sum v = 0$ (Mesh loops) | KCL $\sum i = 0$ (Node junctions) |

---

### 14.3. Conversion Rules & System Drawing
1. Count independent displacements ($x_1, x_2, \dots$) $\to$ equals number of mechanical nodes / electrical loops (F-V) or nodes (F-I).
2. Elements tied to a single displacement connect between that node and ground/reference.
3. Elements shared between two displacements connect between those two nodes.
4. **F-V Analogy (Mesh Network):** Each node becomes a loop; shared elements become mutual loop impedances.
5. **F-I Analogy (Nodal Network):** Each node becomes a voltage node; shared elements become bridging admittances.

---

# 15. Advanced Systems: Interconnected, Inverse & Distortionless

### 15.1. Inverse Systems

- **Definition:** $H(s) \cdot H_{\text{inv}}(s) = 1 \implies H_{\text{inv}}(s) = \frac{1}{H(s)}$.
- **Purpose:** Channel equalization; recovers original transmitted signal $x(t)$ from distorted output $y(t)$.
- **Causality & Stability Conditions:**
  - All poles of $H_{\text{inv}}(s)$ must lie in the Left-Half Plane.
  - Since poles of $H_{\text{inv}}(s)$ are the zeros of $H(s)$, **all zeros of $H(s)$ must lie in the Left-Half Plane**.
  - Systems with both poles and zeros strictly in the LHP are called **Minimum-Phase Systems**.

---

### 15.2. Distortionless Transmission Systems

- **Definition:** Output is an exact scaled and delayed replica of input:
  $$y(t) = K x(t - t_d)$$
- **Frequency Response Criteria:**
  1. **Flat Gain (No Amplitude Distortion):**
     $$|H(\omega)| = K \quad \forall \omega$$
  2. **Linear Phase (No Phase / Delay Distortion):**
     $$\angle H(\omega) = -\omega t_d \quad \forall \omega$$
     *(Constant group delay: $t_g = -\frac{d\phi}{d\omega} = t_d$ across all frequencies)*

---

# 16. Network Synthesis (Foster, Cauer & PR Functions)

### 16.1. Positive Real (PR) Conditions

For a driving-point impedance $Z(s)$ or admittance $Y(s)$ to be realizable using passive components ($R, L, C$):
1. $Z(s)$ is real when $s$ is real ($Z(\sigma) \in \mathbb{R}$).
2. $\text{Re}\{Z(s)\} \ge 0$ for all $\text{Re}\{s\} \ge 0$ (maps RHP into RHP).
3. Poles and zeros of $Z(s)$ lie in LHP or on $j\omega$-axis.
4. Poles on $j\omega$-axis are simple with real, positive residues.
5. Degree difference between numerator and denominator $\le 1$.

---

### 16.2. Canonical Realization Forms

- **Foster Form I:** Partial fraction expansion of $Z(s)$ (Series connection of parallel tuned tanks).
- **Foster Form II:** Partial fraction expansion of $Y(s)$ (Parallel connection of series tuned branches).
- **Cauer Form I:** Continued fraction expansion of $Z(s)$ by descending powers of $s$ (Ladder network with alternating series and shunt elements).
- **Cauer Form II:** Continued fraction expansion of $Z(s)$ by ascending powers of $s$ (Ladder network).

---

*Generated based on [[2-2/signal n system/A.N system|A.N system]], [[2-2/signal n system/A.N  System Response|A.N System Response]], [[2-2/signal n system/QnA system, Application of Signals and Systems|QnA system, Application of Signals and Systems]], [[2-2/signal n system/QnA    System Response|QnA System Response]], [[2-2/signal n system/QnA  Signal|QnA Signal]], and [[2-2/signal n system/A.N signal|A.N signal]].*
