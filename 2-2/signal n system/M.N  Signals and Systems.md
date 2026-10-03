# 🛰️ Master Notes: Signals and Systems

---

## 📑 Module Directory
- [[#1. Signal Fundamentals & Operations]]
- [[#2. Energy & Power Signal Classification]]
- [[#3. System Properties & Classification]]
- [[#4. Laplace Transform (LT) & ROC]]
- [[#5. Continuous-Time Fourier Transform (FT)]]
- [[#6. Fourier Series (FS) & Circuit Analysis]]
- [[#7. Sampling, Modulation & Z-Transform]]

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
| **Gate / Rectangular $\Pi(t/\tau)$** | $\text{rect}(t/\tau) = \begin{cases} 1, & |t| \le \tau/2 \\ 0, & |t| > \tau/2 \end{cases}$ | $\text{rect}(t/\tau) = u(t + \tau/2) - u(t - \tau/2)$ |
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

### 3.2. Detailed Property Tests & Logic

#### 1. Linearity (Superposition)
- **Condition:** 
  $$\mathcal{T}\{a\,x_1(t) + b\,x_2(t)\} = a\,\mathcal{T}\{x_1(t)\} + b\,\mathcal{T}\{x_2(t)\}$$
- **Key Traps & Counterexamples:**
  - $y(t) = \text{Re}\{x(t)\}$:
    - Additivity: $\text{Re}\{x_1 + x_2\} = \text{Re}\{x_1\} + \text{Re}\{x_2\}$ ✅
    - Homogeneity: For complex scalar $k = j$, $j\text{Re}\{x\} = jx_r \neq \text{Re}\{jx\} = -x_i$ ❌
    - $\therefore$ **Non-Linear** over complex field.
  - $y(t) = \frac{x^2(t)}{\dot{x}(t)}$:
    - Homogeneity: $\frac{(kx)^2}{k\dot{x}} = k\frac{x^2}{\dot{x}}$ ✅
    - Additivity: $\frac{(x_1+x_2)^2}{\dot{x}_1+\dot{x}_2} \neq \frac{x_1^2}{\dot{x}_1} + \frac{x_2^2}{\dot{x}_2}$ ❌
    - $\therefore$ **Non-Linear**.
  - Differential Equations:
    - $\frac{dy}{dt} + t^2 y(t) = (2t+3)x(t) \implies$ **Linear** (coefficients depend only on independent variable $t$).
    - $y(t)\frac{dy}{dt} + 3y(t) = x(t) \implies$ **Non-Linear** (cross-product of $y$ and its derivative produces $k^2$).
  - Graphical Rule:
    - Must be a straight line through origin $(0,0)$.
    - $y(t) = x(t) + 4 \implies$ **Non-Linear** (nonzero offset).
    - Saturation / Clipper $\implies$ **Non-Linear**.

---

#### 2. Time-Invariance (TI)
- **Test Procedure:**
  1. Find response to delayed input: $y_1(t) = \mathcal{T}\{x(t - t_0)\}$.
  2. Delay original output: $y_2(t) = y(t - t_0)$ (substitute $t \to t - t_0$ everywhere).
  3. Compare: $y_1(t) \stackrel{?}{=} y_2(t)$.
- **Quick Inspection Rules:**
  - Explicit $t$ multiplier/function outside $x(\cdot)$ (e.g., $t \cdot x(t)$, $\sin(t)x(t-2)$, $x(t) - 0.5(t+1)$) $\implies$ **Time-Variant (TV)**.
  - Internal scaling or sign flip (e.g., $x(2t)$, $x(-t)$, $x(1-t)$) $\implies$ **Time-Variant (TV)**.
  - Constant coefficient operations (e.g., $\frac{d}{dt}x(t)$, $x(t-2)$, $2x(t)$) $\implies$ **Time-Invariant (TI)**.

---

#### 3. Causality
- **Definition:** Output $y(t_0)$ depends ONLY on input $x(t)$ for $t \le t_0$.
- **Diagnostic Examples:**
  - $y(t) = x(-t)$: At $t = -2$, $y(-2) = x(2)$ (requires future input) $\implies$ **Non-Causal**.
  - $y(t) = x(1 - t)$: At $t = -1$, $y(-1) = x(2)$ (future) $\implies$ **Non-Causal**.
  - $y(t) = \int_{t-5}^{t+5} x(\tau) d\tau$: Upper limit $t+5 > t \implies$ **Non-Causal**.
    - Delaying by 5 s yields $y_d(t) = \int_{t-10}^t x(\tau)d\tau \implies$ **Causal** (physically realizable).
  - $y[n] = \frac{1}{3}(x[n+1] + x[n] + x[n-1]) \implies$ **Non-Causal** ($x[n+1]$ is future).
  - $y[n] = \frac{1}{3}(x[n] + x[n-1] + x[n-2]) \implies$ **Causal**.

---

#### 4. Memory (Instantaneous vs Dynamic)
- **Memoryless (Instantaneous):** Output $y(t)$ depends ONLY on input at the exact same instant $t$.
  - $y(t) = \cos(\omega_c t)x(t) \implies$ **Memoryless**.
  - $y(t-1) = 2x(t-1) \implies$ **Memoryless** (evaluated at $t'=t-1$).
  - $y(t) = (t-1)x(t) \implies$ **Memoryless**.
- **Dynamic (With Memory):** Output depends on past or future inputs.
  - $y(t) = \frac{d}{dt}x(t) = \lim_{T \to 0} \frac{x(t) - x(t-T)}{T} \implies$ **Dynamic** (requires two adjacent points in time).
  - Integrator $\int x(\tau)d\tau$, delays $x(t-1)$, moving averages $\implies$ **Dynamic**.

---

#### 5. Invertibility
- **Condition:** Distinct inputs produce distinct outputs (1-to-1 mapping). $x(t) = \mathcal{T}^{-1}\{y(t)\}$.
- **Non-Invertible Systems:**
  - Saturation / Limiter: Multiple inputs above saturation threshold map to identical $V_{\text{cc}}$ ❌.
  - $y(t) = t \cdot x(t)$: At $t = 0$, $y(0) = 0 \cdot x(0) = 0$; $x(0)$ is permanently lost ❌.
  - Differentiator $y(t) = \frac{d}{dt}x(t)$: DC constant lost ($\frac{d}{dt}(C) = 0$) ❌.
  - Even powers: $y(t) = x^2(t)$ or $|x(t)|$ (sign lost) ❌.
- **Invertible Systems:**
  - $y(t) = x(-t) \implies x(t) = y(-t)$ ✅.
  - $y(t) = x(t) + 4 \implies x(t) = y(t) - 4$ ✅.

---

#### 6. BIBO Stability
- **Definition:** Bounded input $|x(t)| \le M_x < \infty \implies$ Bounded output $|y(t)| \le M_y < \infty$.
- **LTI System Condition:**
  $$\int_{-\infty}^{\infty} |h(t)|\,dt < \infty \quad \text{or} \quad \sum_{n=-\infty}^\infty |h[n]| < \infty$$
- **Quick Stability Memory Rules:**
  - $\text{Bounded} \times \text{Bounded} = \text{Bounded}$ ✅ ($y(t) = \sin(t)x(t) \le 1 \cdot M_x \implies$ Stable).
  - $\text{Growing function } (t, e^t) \times \text{Bounded} \implies$ **Unstable** ($y(t) = t \cdot u(t) \to \infty$ as $t \to \infty$).
  - Differentiator $\frac{d}{dt}x(t)$ with $x(t) = u(t) \implies y(t) = \delta(t) \to \infty \implies$ **Unstable**.
  - Moving average $y[n] = \frac{1}{3}\sum_{k=0}^2 x[n-k] \le M_x \implies$ **Stable**.
  - Piecewise saturation limiter: $|y(t)| \le V_{\text{cc}} \implies$ **Stable**.

---

# 4. Laplace Transform (LT) & ROC

### 4.1. Core Definitions
- **Bilateral (Two-Sided) LT:**
  $$X(s) = \int_{-\infty}^{\infty} x(t) e^{-st}\,dt, \quad s = \sigma + j\omega$$
- **Unilateral (One-Sided) LT:**
  $$X(s) = \int_{0^-}^{\infty} x(t) e^{-st}\,dt$$
- **Role of $\sigma = \text{Re}\{s\}$:**
  $$e^{-st} = e^{-\sigma t}e^{-j\omega t}, \quad |e^{-j\omega t}| = 1$$
  Convergence depends strictly on damping factor $\sigma$:
  $$\int_{-\infty}^\infty |x(t)e^{-\sigma t}|\,dt < \infty$$

---

### 4.2. Region of Convergence (ROC) Geometry

- **ROC Geometry & Topography Rules:**
  - **Poles:** ROC **NEVER** contains any poles (integral blows up at poles).
  - **Right-Sided Signals ($t \to +\infty$, Causal):**
    $$x(t) = e^{at}u(t) \iff \frac{1}{s - a}, \quad \text{ROC: } \text{Re}\{s\} > a \quad (\text{Right-Half Plane / RHP})$$
  - **Left-Sided Signals ($t \to -\infty$, Anti-Causal):**
    $$-e^{at}u(-t) \iff \frac{1}{s - a}, \quad \text{ROC: } \text{Re}\{s\} < a \quad (\text{Left-Half Plane / LHP})$$
    *(Or $e^{at}u(-t) \iff -\frac{1}{s - a}, \; \text{Re}\{s\} < a$)*
  - **Two-Sided Signals ($-\infty < t < \infty$):**
    $$x(t) = x_R(t) + x_L(t) \implies \text{ROC: } \sigma_R < \text{Re}\{s\} < \sigma_L \quad (\text{Vertical Strip})$$
    *(Note: If $\sigma_R > \sigma_L$, intersection is empty $\implies$ LT does not exist!)*
  - **Finite-Duration Signals:**
    $$\text{ROC: Entire } s\text{-plane} \quad (\text{excluding possibly } s = 0 \text{ or } s = \infty)$$

- **Stability & Causality in $s$-Domain:**
  - **BIBO Stable:** ROC contains imaginary axis ($\text{Re}\{s\} = 0$).
  - **Causal + Stable:** All poles lie strictly in open Left-Half Plane ($\text{Re}\{p_k\} < 0$).
  - **Fourier Connection:** $X(j\omega) = \left.X(s)\right|_{s=j\omega}$ exists $\iff$ ROC contains $j\omega$-axis.

---

### 4.3. Laplace Transform Properties

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

### 4.4. Piecewise Waveforms via Derivative Property

$$\mathcal{L}\left\{\frac{d^2 x}{dt^2}\right\} = s^2 X(s) = \sum A_i e^{-s t_i} \implies X(s) = \frac{1}{s^2}\sum A_i e^{-s t_i}$$

1. Differentiate piecewise linear graph until it reduces to impulses $\delta(t - t_i)$.
2. Apply $\mathcal{L}\{\delta(t - t_i)\} = e^{-s t_i}$.
3. Divide by $s^2$ (or $s$ for step jumps).

---

# 5. Continuous-Time Fourier Transform (FT)

### 5.1. Core Formulas & Dirichlet Conditions
- **Forward FT:** 
  $$X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t}\,dt$$
- **Inverse FT:** 
  $$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j\omega t}\,d\omega$$
- **Dirichlet Conditions for Existence:**
  1. $\int_{-\infty}^{\infty} |x(t)|\,dt < \infty$ (absolutely integrable).
  2. Finite number of maxima and minima within any finite interval.
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
| **Gate / Rect $\Pi(t/\tau)$** | $\tau\,\text{sinc}\left(\frac{\omega\tau}{2}\right) = \tau \frac{\sin(\omega\tau/2)}{\omega\tau/2}$ | Sinc spectrum |
| **Bandlimited Sinc $\frac{W}{\pi}\text{sinc}(Wt)$** | $\text{rect}\left(\frac{\omega}{2W}\right)$ | Duality of rectangular pulse |

---

### 5.3. Key Properties of Fourier Transform

- **Time Scaling:** 
  $$x(at) \iff \frac{1}{|a|}X\left(\frac{\omega}{a}\right)$$
  *(Time compression $\to$ Frequency expansion).*
- **Time Shifting:** 
  $$x(t - t_0) \iff e^{-j\omega t_0} X(\omega)$$
- **Modulation (Freq Shift):** 
  $$x(t)\cos(\omega_0 t) \iff \frac{1}{2}[X(\omega - \omega_0) + X(\omega + \omega_0)]$$
- **Time Differentiation:** 
  $$\frac{d^n x}{dt^n} \iff (j\omega)^n X(\omega)$$
  - Derivative trick for piecewise waveforms:
    $$x''(t) = \sum A_i \delta(t - t_i) \implies -\omega^2 X(\omega) = \sum A_i e^{-j\omega t_i} \implies X(\omega) = -\frac{1}{\omega^2}\sum A_i e^{-j\omega t_i}$$
- **Time Integration:** 
  $$\int_{-\infty}^t x(\tau)d\tau \iff \frac{X(\omega)}{j\omega} + \pi X(0)\delta(\omega)$$
- **Duality (Symmetry):** 
  $$x(t) \iff X(\omega) \implies X(t) \iff 2\pi x(-\omega)$$
- **Convolution:** 
  $$x_1(t) * x_2(t) \iff X_1(\omega) X_2(\omega)$$
  $$x_1(t) \cdot x_2(t) \iff \frac{1}{2\pi}[X_1(\omega) * X_2(\omega)]$$

---

### 5.4. Parseval's Theorem & Energy Calculations
- **Parseval's Theorem (Rayleigh's Energy):**
  $$E = \int_{-\infty}^{\infty} |x(t)|^2\,dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(\omega)|^2\,d\omega = \int_{-\infty}^\infty |X(f)|^2\,df$$
- **Energy Spectral Density (ESD):** 
  $$S_{xx}(\omega) = |X(\omega)|^2$$
- **Resistor Energy Dissipation:**
  $$W_{1\Omega} = E, \quad W_R = \frac{1}{R}\int_{-\infty}^\infty v^2(t)\,dt = R\int_{-\infty}^\infty i^2(t)\,dt$$
- **Band Energy:**
  $$W_{[\omega_1, \omega_2]} = \frac{1}{\pi} \int_{\omega_1}^{\omega_2} |X(\omega)|^2\,d\omega \quad (\text{for real signals})$$

---

### 5.5. Essential Concepts & Traps
- **Why Ramp $r(t) = t u(t)$ has NO Fourier Transform:**
  - $r(t) \to \infty$ as $t \to \infty$. Violates absolute integrability $\int |r(t)|dt = \infty$. Cannot be stabilized with delta distributions.
- **Why Time-Limited Signals are Band-Unlimited:**
  - Compact support in time $\implies$ Analytic Fourier transform everywhere in frequency plane $\implies$ cannot be compactly supported in frequency without vanishing identically.

---

# 6. Fourier Series (FS) & Circuit Analysis

### 6.1. Three Representations of Fourier Series

- **Fourier Series Inter-Conversion Pipeline:**
  $$\text{Trigonometric FS (TFS)} \xleftrightarrow{\text{Polar grouping}} \text{Compact / Polar FS (CFS)} \xleftrightarrow{\text{Euler identity}} \text{Complex Exponential FS (EFS)}$$

#### 1. Trigonometric Fourier Series (TFS)
$$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]$$
- Fundamental Frequency: $\omega_0 = \frac{2\pi}{T}$.
- Coefficients:
  $$a_0 = \frac{1}{T}\int_0^T f(t)\,dt$$
  $$a_n = \frac{2}{T}\int_0^T f(t)\cos(n\omega_0 t)\,dt$$
  $$b_n = \frac{2}{T}\int_0^T f(t)\sin(n\omega_0 t)\,dt$$

#### 2. Compact / Polar Fourier Series
$$f(t) = a_0 + \sum_{n=1}^{\infty} A_n \cos(n\omega_0 t + \theta_n) \quad \text{or} \quad a_0 + \sum_{n=1}^\infty C_n \cos(n\omega_0 t - \phi_n)$$
- $A_n = C_n = \sqrt{a_n^2 + b_n^2}$
- Phase angles: $\theta_n = -\arctan\left(\frac{b_n}{a_n}\right)$, $\phi_n = \arctan\left(\frac{b_n}{a_n}\right) = -\theta_n$
- **Universal Phasor Formula:**
  $$\mathbf{V}_n = a_n - jb_n$$

#### 3. Complex Exponential Fourier Series (EFS)
$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}$$
- Coefficients:
  $$c_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t) e^{-j n \omega_0 t}\,dt$$
- Conversion Relations:
  $$c_0 = a_0$$
  $$c_n = \frac{1}{2}(a_n - jb_n) = \frac{A_n}{2}e^{j\theta_n}$$
  $$c_{-n} = c_n^* = \frac{1}{2}(a_n + jb_n)$$
  $$a_n = 2\text{Re}(c_n), \quad b_n = -2\text{Im}(c_n)$$
  $$|c_n| = \frac{A_n}{2}, \quad \angle c_n = \theta_n$$

---

### 6.2. Waveform Symmetries Table

| Symmetry | Definition | Eliminated Terms | Surviving Coefficients | Integration Range |
| :--- | :--- | :--- | :--- | :--- |
| **Even** | $f(-t) = f(t)$ | $b_n = 0$ | $a_0, a_n$ | $\frac{4}{T}\int_0^{T/2} f(t)\cos(n\omega_0 t)dt$ |
| **Odd** | $f(-t) = -f(t)$ | $a_0 = 0, a_n = 0$ | $b_n$ only | $\frac{4}{T}\int_0^{T/2} f(t)\sin(n\omega_0 t)dt$ |
| **Half-Wave (HWS)** | $f(t \pm T/2) = -f(t)$ | $a_0 = 0$, Even harmonics ($a_{\text{even}} = b_{\text{even}} = 0$) | $a_n, b_n$ for **odd $n$ only** | $\frac{4}{T}\int_0^{T/2} f(t)\cdot (\dots)dt$ |
| **Even HWS** | Even + HWS | $b_n = 0$, all even $n$ | $a_n$ for **odd $n$ only** | $\frac{8}{T}\int_0^{T/4} f(t)\cos(n\omega_0 t)dt$ |
| **Odd HWS** | Odd + HWS | $a_n = 0$, all even $n$ | $b_n$ for **odd $n$ only** | $\frac{8}{T}\int_0^{T/4} f(t)\sin(n\omega_0 t)dt$ |
| **Quarter-Wave** | HWS + Symmetry around $T/4$ | All even $n$ | Single term ($a_n$ or $b_n$, odd $n$) | Spans $[0, T/4]$ only |

---

### 6.3. Line Spectra
- **Amplitude Spectrum:** Discrete plot of $|c_n|$ (or $A_n$) vs $\omega = n\omega_0$. **Even symmetry** ($|c_{-n}| = |c_n|$).
- **Phase Spectrum:** Discrete plot of $\angle c_n$ (or $\theta_n$) vs $\omega = n\omega_0$. **Odd symmetry** ($\angle c_{-n} = -\angle c_n$).

---

### 6.4. Circuit Frequency Response with FS Inputs

- **Circuit Response Analysis Flow:**
  $$\boxed{\text{Input } v_i(t) = \sum V_n \cos(n\omega_0 t + \theta_n)} \xrightarrow{H(j\omega) = \frac{V_o(j\omega)}{V_i(j\omega)}} \boxed{\text{Output } v_o(t) = \sum |H(jn\omega_0)|\,V_n \cos\big(n\omega_0 t + \theta_n + \angle H(jn\omega_0)\big)}$$

1. Express periodic input as Fourier series.
2. Determine circuit transfer function $H(s) = \frac{V_o(s)}{V_i(s)}$.
3. For each harmonic frequency $\omega_n = n\omega_0$:
   $$V_{o, n} = V_{i, n} \cdot H(j n\omega_0)$$
   $$|V_{o, n}| = |V_{i, n}| \cdot |H(j n\omega_0)|, \quad \angle V_{o, n} = \angle V_{i, n} + \angle H(j n\omega_0)$$
4. Sum all output harmonic sinusoids.
5. **Average Power in Resistor $R$:**
   $$P_{\text{avg}} = \frac{1}{R}\left[ V_{o, \text{dc}}^2 + \sum_{n=1}^\infty \frac{|V_{o, n}|^2}{2} \right]$$

---

# 7. Sampling, Modulation & Z-Transform

### 7.1. Amplitude Modulation (AM)
- **Principle (DSB-SC):**
  $$s(t) = m(t)\cos(\omega_c t) \iff S(\omega) = \frac{1}{2}[M(\omega - \omega_c) + M(\omega + \omega_c)]$$
- **Purpose:** Translates baseband message $m(t)$ to passband around carrier frequency $\omega_c$. Allows radiation with manageable antenna size ($\text{Length} \propto \lambda = c/f$).
- **Demodulation:** Multiply by $\cos(\omega_c t)$ and pass through Low-Pass Filter (LPF).

---

### 7.2. Sampling Theorem (Nyquist-Shannon)

- **Sampling Regimes ($f_s$ vs $2B$):**
  - **Over-Sampling ($f_s > 2B$):** Guard band exists between replica spectra; easily reconstructible with simple filter.
  - **Nyquist Rate ($f_s = 2B$):** Critically sampled; replica spectra touch at edges without overlap; reconstructible with ideal low-pass filter (LPF).
  - **Under-Sampling ($f_s < 2B$):** Aliasing occurs (spectral overlap); high frequencies irreversibly fold into baseband.

- **Nyquist Rate:** 
  $$f_s \ge 2 f_{\max} = 2B \quad (\omega_s \ge 2\omega_m)$$
- **Nyquist Interval:** 
  $$T_s \le \frac{1}{2B}$$
- **Sampled Spectrum:** 
  $$X_s(\omega) = \frac{1}{T_s}\sum_{k=-\infty}^\infty X(\omega - k\omega_s)$$
- **Aliasing Diagnosis ($B = 10\text{ kHz} \implies f_{\text{Nyquist}} = 20\text{ kHz}$):**
  - $f_s = 5\text{ kHz} < 20\text{ kHz} \implies$ Severe aliasing (overlap $\Delta f = 15\text{ kHz}$).
  - $f_s = 10\text{ kHz} < 20\text{ kHz} \implies$ Aliasing (overlap $\Delta f = 10\text{ kHz}$).
  - $f_s = 20\text{ kHz} \implies$ Exact boundary match; perfect recovery via ideal LPF ($B = 10\text{ kHz}$).

---

### 7.3. Z-Transform (ZT) Fundamentals
- **Bilateral Definition:**
  $$X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}, \quad z = r e^{j\Omega}$$
- **ROC Significance & Rules:**
  - $X(z)$ is incomplete without its ROC. Distinct sequences can share identical $X(z)$.
  - ROC contains **NO poles**.
  - **Right-Sided (Causal):** ROC is exterior of a circle: $|z| > r_{\max}$.
  - **Left-Sided (Anti-Causal):** ROC is interior of a circle: $|z| < r_{\min}$.
  - **Two-Sided:** ROC is an annular ring: $r_1 < |z| < r_2$.
  - **BIBO Stability:** ROC contains the unit circle ($|z| = 1$).
- **Finite Discrete Pulse Train:**
  $$x[n] = 1, \quad n = 0, 1, \dots, m-1$$
  $$X(z) = \sum_{n=0}^{m-1} z^{-n} = \frac{1 - z^{-m}}{1 - z^{-1}}, \quad \text{ROC: Entire } z\text{-plane except } z = 0$$

---
*Generated based on [[2-2/signal n system/QnA  Signal|QnA  Signal]] and [[2-2/signal n system/A.N signal|A.N signal]].*
