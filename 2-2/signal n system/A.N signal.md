 
 ![[Screenshot_20261005_023903_Xodo.jpg]]
 
 
 ![[Pasted image 20261004164126.png]]
 ![[Pasted image 20261003072613.png]]

### ROC curve
 ![[Pasted image 20261003091206.png]]
 ![[Pasted image 20261003091728.png]]

![[Pasted image 20261003092943.png]]

![[Pasted image 20261003094850.png]]

 ### fourier
 ![[Pasted image 20261003123308.png]]

![[Pasted image 20261003172933.png]]

![[Pasted image 20261003175017.png]]

![[Pasted image 20261003181806.png]]

![[Pasted image 20261003194227.png]]
![[Pasted image 20261003200254.png]]

![[Pasted image 20261003203421.png]]

![[Pasted image 20261003203444.png]]

![[Pasted image 20261003203500.png]]
![[Pasted image 20261003204155.png]]

![[Pasted image 20261004022816.png]]
### Qna


 #### Direct Jump Rule for $h(t)$
![[Pasted image 20260628100445.png]]
To write any piecewise flat graph directly:

- **Rule:** At every time instant $t = a$, add:
    
    $$\Delta (\text{amplitude}) \cdot u(t - a)$$
    
    where $\Delta (\text{amplitude}) = \text{New Level} - \text{Old Level}$.
    

#### 1-Line Formulation

- **At $t = 0$:** Jumps from $0 \to 10$ ($\Delta = +10$) $\implies +10u(t)$
    
- **At $t = 2$:** Drops from $10 \to 5$ ($\Delta = -5$) $\implies -5u(t - 2)$
    
- **At $t = 4$:** Drops from $5 \to 0$ ($\Delta = -5$) $\implies -5u(t - 4)$
    

$$h(t) = 10u(t) - 5u(t - 2) - 5u(t - 4)$$
 
 ## Atomic Notes: Periodicity of Continuous-Time Signals
 
## Periodicity of Summed Signals
When [[2-2/signal n system/Q signal|adding multiple periodic signals]] ($x(t) = x_1(t) + x_2(t) + \dots + x_N(t)$):
## 1. Condition for Periodicity
The combined signal is periodic if and only if the ratio of [[2-1/Mecha/IC engine Ai studio qna|any two individual periods]] is a rational number (a fraction of integers).
$$\frac{T_1}{T_2} = \frac{m}{n} \quad (\text{where } m, n \in \mathbb{Z}^+)$$ 
## 2. Finding the Combined Fundamental Period ($T_0$)
Once the ratio is simplified to [[2-1/Math 3/3d Geometry QnA|its lowest terms]] ($\frac{m}{n}$), calculate $T_0$ using cross-multiplication:
$$T_0 = n T_1 = m T_2$$ 

* Alternatively, $T_0$ is the Least Common Multiple (LCM) of the individual periods:
$$T_0 = \text{LCM}(T_1, T_2)$$ 

------------------------------
## Quick Example

* Signal: $x(t) = \sin(2\pi t) + \sin(4\pi t)$
* Periods: $T_1 = 1\text{ s}$, $T_2 = 0.5\text{ s}$
* Ratio: $\frac{T_1}{T_2} = \frac{1}{0.5} = \frac{2}{1}$ (Rational $\rightarrow$ Periodic)
* Fundamental Period: $T_0 = 1 \times T_1 = 1\text{ s}$ (or $2 \times 0.5 = 1\text{ s}$)

M-02:
$$x(t) = \sin(10t) + \sin(\pi t)$$ 
$$T_1 = \frac{2\pi}{10} = \frac{\pi}{5} \quad ; \quad T_2 = \frac{2\pi}{\pi} = 2$$ 
$$\downarrow \text{ it is irrational (অমূলদ)}$$ 
$$\text{(So, it's a non-periodic signal)}$$
### Atomic Notes: Signal Transformations ($x(2t - 6)$)

### **Method 1: Shift First, Then Scale**

1. **Shift:** Delay $x(t)$ by **6**.
    
    $$\to x(t - 6)$$
    
2. **Scale:** Compress by **2** (replace $t$ with $2t$).
    
    $$\to \mathbf{x(2t - 6)}$$
    

- **Rule:** Scaling applies _only_ to the variable $t$, leaving the shift value untouched.
    

### **Method 2: Scale First, Then Shift**

1. **Scale:** Compress $x(t)$ by **2**.
    
    $$\to x(2t)$$
    
2. **Shift:** Delay by **3** (replace $t$ with $t - 3$).
    
    $$\to x(2(t - 3)) = \mathbf{x(2t - 6)}$$
    

- **Rule:** Shifting a pre-scaled signal requires dividing the desired shift by the scaling factor ($\frac{6}{2} = 3$).


## Stable and Unstable Systems

### BIBO Stability

**BIBO** = Bounded Input, Bounded Output

- **Stable System:** Every bounded input produces a bounded output for all time.
    
- **Unstable System:** At least one bounded input produces an unbounded output.
    

### Bounded Signal

A signal is bounded if its amplitude always remains finite.

**Examples:**

- **Constant (DC):** $y(t) = 6$
    
- **Sine/Cosine:** $\sin(t)$, $\cos(t)$ (amplitude range: $-1$ to $1$)
    
- **Unit Step:** $u(t)$ (values: $0$ or $1$)
    

## Stability Test Procedure

1. **Apply** a known bounded input (e.g., $u(t)$, a constant, or $\sin(t)$).
    
2. **Find** the resulting output equation.
    
3. **Check the limit:**
    
    - If the output remains finite $\to$ **Stable**
        
    - If the output goes to $\infty$ as $t \to \infty$ $\to$ **Unstable**
        

### Worked Examples

- **Example 1:** $y(t) = t \cdot x(t)$
    
    - _Input:_ $x(t) = u(t)$ (bounded)
        
    - _Output:_ $y(t) = t \cdot u(t)$ (ramp function)
        
    - _Analysis:_ As $t \to \infty$, the output $y(t) \to \infty$.
        
    - _Result:_ ❌ **Unstable**
        
- **Example 2:** $y(t) = x(t) + 2$
    
    - _Input:_ $x(t) = 4$ (bounded)
        
    - _Output:_ $y(t) = 6$
        
    - _Analysis:_ The output remains finite for all time.
        
    - _Result:_ ✅ **Stable**
        
**Example 3:** $y(t) = \sin(t) \cdot x(t)$

- _Input:_ Let $x(t)$ be any bounded input such that $\vert{}x(t)\vert{} \le M < \infty$.
    
- _Output:_ $y(t) = \sin(t) \cdot x(t)$
    
- _Analysis:_ Take the absolute value of both sides:
    
    $$\vert{}y(t)\vert{} = \vert{}\sin(t) \cdot x(t)\vert{} = \vert{}\sin(t)\vert{} \cdot \vert{}x(t)\vert{}$$
    
    Since $\vert{}\sin(t)\vert{} \le 1$ for all time, we can write:
    
    $$\vert{}y(t)\vert{} \le 1 \cdot M \to \vert{}y(t)\vert{} \le M$$
    
    Because $M$ is finite, the output is guaranteed to remain finite.
    
- _Result:_ ✅ **Stable**
- 
==, absolute integrability of the impulse response means the system is BIBO stable.==

For a Linear Time-Invariant (LTI) system, absolute integrability is the necessary and sufficient condition for BIBO stability.



If an LTI system has an impulse response h(t), the system is guaranteed to be BIBO stable if and only if:

$$\int_{-\infty}^{\infty} \vert{}h(t)\vert{} \, dt < M < \infty$$

Where M is a finite maximum value.


## Quick Memory Tricks

- $\text{Bounded} \times \text{Bounded} = \text{Bounded}$ ✅
    
- $\text{Growing function (e.g., } t, e^t\text{)} \times \text{Bounded} \to$ Can become Unbounded ❌
    
- Adding a finite constant does not affect stability. ✅
    

> **Exam Definition:** A system is BIBO stable if and only if every bounded input produces a bounded output for all time.

---


$$\left\vert{}e^{j\omega t}\right\vert{} = \sqrt{\cos^2(\omega t) + \sin^2(\omega t)} = 1$$

### Bilateral Laplace Transform & Convergence Basics

#### Core Definition & Role of $\sigma$

- The bilateral Laplace transform converts a continuous-time signal into the complex frequency domain via $X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} \, dt$.
    
      
    
- The complex variable is defined as $s = \sigma + j\omega$, splitting the transform into an attenuation factor $e^{-\sigma t}$ and an oscillation factor $e^{-j\omega t}$.
    
      
    
- Signals that blow up or fail Dirichlet conditions for Fourier analysis can converge if the real damping factor $\sigma = \text{Re}\{s\}$ neutralizes their growth.
    
      
    
- Because $\vert{}e^{-j\omega t}\vert{} = 1$, convergence depends strictly on $\sigma$ satisfying $\int_{-\infty}^{\infty} \vert{}x(t) e^{-\sigma t}\vert{} \, dt < \infty$.
    
      
    

#### Region of Convergence (ROC)

- The ROC defines the set of all values of $s$ in the complex plane for which the Laplace integral converges.
    
      
    
- Two distinct time-domain signals can share the identical algebraic expression $X(s)$; the ROC uniquely specifies the inverse transform.
    
      
    
- The ROC forms vertical strips or half-planes parallel to the $j\omega$-axis because convergence is independent of $\omega$.
    
      
    
- No poles can exist within an ROC because the integral diverges to infinity at a pole.
    
      
    

### Signal Classification & ROC Geometry

#### Right-Sided Signals ($t \to +\infty$)

- A causal or right-sided signal is zero prior to a starting point, represented fundamentally by $x(t) = e^{at}u(t)$.
    
      
    
- Computing the integral yields $X(s) = \left[ \frac{e^{-(s-a)t}}{-(s-a)} \right]_{0}^{\infty} = \frac{1}{s-a} - \lim_{t \to \infty} \frac{e^{-(\sigma-a)t}e^{-j\omega t}}{s-a}$.
    
      
    
- For the limit at $t \to \infty$ to vanish, the real exponent must be negative: $-(\sigma - a) < 0 \implies \sigma > a$.
    
      
    
- This produces a lower bound and a right-half plane ROC: $\text{Re}\{s\} > \sigma_R$.
    
      
    

#### Left-Sided Signals ($t \to -\infty$)

- An anti-causal or left-sided signal extends into the past, modeled as $x(t) = -e^{at}u(-t)$.
    
      
    
- Substituting $\tau = -t$ maps the past to $+\infty$, leading to $X(s) = -\int_{0}^{\infty} e^{(s-a)\tau} \, d\tau = \frac{1}{s-a} - \lim_{\tau \to \infty} \frac{e^{(\sigma-a)\tau}e^{j\omega \tau}}{s-a}$.
    
      
    
- For the limit at $\tau \to \infty$ to vanish, the growth rate must dominate $\sigma$: $(\sigma - a) < 0 \implies \sigma < a$.
    
      
    
- This produces an upper bound and a left-half plane ROC: $\text{Re}\{s\} < \sigma_L$.
    
      
    

#### Two-Sided & Finite Signals

- A two-sided signal is the sum of causal and anti-causal parts: $x(t) = x_R(t) + x_L(t)$.
    
      
    
- Its total ROC is the intersection $\text{ROC}_R \cap \text{ROC}_L$, forming an open vertical strip $\sigma_R < \text{Re}\{s\} < \sigma_L$ bounded by poles.
    
      
    
- If $\sigma_R > \sigma_L$, no overlapping region exists, and the bilateral Laplace transform does not exist for the signal.
    
      
    
- Finite-duration signals converge everywhere over the finite integration interval, giving an ROC of the entire $s$-plane (excluding possibly $s = \pm\infty$).
    
      
    

### Stability & Transform Relationships

#### System Stability (BIBO)

- An LTI system is bounded-input bounded-output (BIBO) stable if and only if its impulse response $h(t)$ is absolutely integrable.
    
      
    
- In the complex $s$-plane, absolute integrability occurs if and only if the ROC of the transfer function $H(s)$ includes the imaginary axis ($\text{Re}\{s\} = 0$).
    
      
    
- For causal LTI systems, stability requires all system poles to lie strictly in the open left-half plane ($\text{Re}\{p_k\} < 0$).
    
      
    

#### Relationship to Fourier Transform

- When $\sigma = 0$ ($s = j\omega$), the damping factor becomes $e^0 = 1$, reducing the Laplace transform directly to the continuous-time Fourier transform.
    
      
    
- The Fourier transform exists if and only if the Laplace ROC contains the $j\omega$-axis.

## 1. Fundamental Concepts and Dirichlet Conditions

A periodic function $f(t)$ with fundamental period $T$ satisfies:

  

$$f(t + T) = f(t), \quad \forall t$$

The fundamental angular frequency $\omega_0$ is defined as:

  

$$\omega_0 = \frac{2\pi}{T} = 2\pi f_0$$

A function $f(t)$ can be expanded into a convergent Fourier series if it satisfies **Dirichlet's Conditions** over any period:

  

- $f(t)$ is absolutely integrable over the period $T$:
    
      
    
    $$\int_{t_0}^{t_0 + T} \vert{}f(t)\vert{}\, dt < \infty$$
    
- $f(t)$ has a finite number of finite maxima and minima within any single period.
    
      
    
- $f(t)$ has a finite number of jump discontinuities within any single period, with no infinite discontinuities.
    
      
    

## 2. Trigonometric Fourier Series (Standard Form)

### General Period $T$ (Frequency $\omega_0 = \frac{2\pi}{T}$)

The trigonometric expansion is given by:

  

$$f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]$$

The Fourier coefficients are evaluated over any interval of length $T$ (typically $[0, T]$ or $[-T/2, T/2]$):

  

- **DC / Average Value:**
    
      
    
    $$a_0 = \frac{1}{T} \int_{0}^{T} f(t)\, dt$$
    
- **Cosine Coefficients:**
    
      
    
    $$a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(n\omega_0 t)\, dt, \quad n = 1, 2, 3, \dots$$
    
- **Sine Coefficients:**
    
      
    
    $$b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t)\, dt, \quad n = 1, 2, 3, \dots$$
    

_(Alternative convention: If defined as $f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$, then $a_0 = \frac{2}{T} \int_0^T f(t)\, dt$ is unified with the formula for $a_n$ at $n=0$.)_

  
## 3. Compact (Harmonic / Polar) Fourier Series

The individual sine and cosine terms can be combined into single phase-shifted sinusoids:

  

### Cosine Form

$$f(t) = a_0 + \sum_{n=1}^{\infty} A_n \cos(n\omega_0 t + \theta_n)$$

or with phase delay:

  

$$f(t) = a_0 + \sum_{n=1}^{\infty} C_n \cos(n\omega_0 t - \phi_n)$$

### Conversion Relations

- **Harmonic Amplitude:**
    
      
    
    $$A_n = C_n = \sqrt{a_n^2 + b_n^2}$$
    
- **Phase Angles:**
    
      
    
    $$\theta_n = -\tan^{-1}\left(\frac{b_n}{a_n}\right) \quad \text{or} \quad \phi_n = \tan^{-1}\left(\frac{b_n}{a_n}\right) = -\theta_n$$
    
- **Inverse Relations:**
    
      
    
    $$a_n = A_n \cos\theta_n = C_n \cos\phi_n$$
    
    $$b_n = -A_n \sin\theta_n = C_n \sin\phi_n$$
    
#### Scenario 1: Target Form is $A_n \cos(nt - \theta_n)$ (Phase Lag / Circuit Standard)

- **Goal:** Group into $\cos(nt - \theta)$
    
- **Identity:** $\cos(nt - \theta) = \cos nt \cos\theta + \sin nt \sin\theta$
    
- **Phasor Formula:**
    
    $$\mathbf{V}_n = a_n - jb_n= A_n \angle -\theta_n$$
#### Scenario 2: Target Form is $A_n \cos(nt + \phi_n)$ (Phase Lead / DSP Standard)

- **Goal:** Group into $\cos(nt + \phi)$
    
- **Identity:** $\cos(nt + \phi) = \cos nt \cos\phi - \sin nt \sin\phi$
    
- **Phasor Formula:**
    
    $$\mathbf{V}_n = a_n - jb_n = A_n \angle \phi_n$$
always (v.i.):
$$\mathbf{V}_n = a_n - jb_n $$
## 4. Complex Exponential Fourier Series

The most compact mathematical representation uses complex exponentials:

  

$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}$$

### Coefficient Formula

$$c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-j n \omega_0 t}\, dt, \quad n = 0, \pm 1, \pm 2, \dots$$

### Inter-conversion Between Forms

For real-valued signals $f(t)$:

  

- $$c_0 = a_0$$
    
- $$c_n = \frac{1}{2}(a_n - j b_n) = \frac{1}{2} A_n e^{j \theta_n}, \quad n > 0$$
    
- $$c_{-n} = c_n^* = \frac{1}{2}(a_n + j b_n)$$
    
- $$a_n = 2 \operatorname{Re}(c_n) = c_n + c_{-n}$$
    
- $$b_n = -2 \operatorname{Im}(c_n) = j(c_n - c_{-n})$$
    
- $$\vert{}c_n\vert{} = \frac{1}{2} \sqrt{a_n^2 + b_n^2} = \frac{A_n}{2}, \quad \angle c_n = \theta_n$$
    

## 5. Waveform Symmetries and Simplifications

Exploiting waveform symmetry halves integration intervals and eliminates entire sets of coefficients:

  

|**Symmetry Type**|**Condition**|**Coefficients**|**Notes**|
|---|---|---|---|
|**Even (Symmetric)**|$f(-t) = f(t)$|$b_n = 0$<br><br>  <br>  <br><br>$a_0 = \frac{2}{T}\int_0^{T/2} f(t)dt$<br><br>  <br>  <br><br>$a_n = \frac{4}{T}\int_0^{T/2} f(t)\cos(n\omega_0 t)dt$|Contains only cosine terms and DC.|
|**Odd (Antisymmetric)**|$f(-t) = -f(t)$|$a_0 = 0$, $a_n = 0$<br><br>  <br>  <br><br>$b_n = \frac{4}{T}\int_0^{T/2} f(t)\sin(n\omega_0 t)dt$|Contains only sine terms (no DC component).|
|**Half-Wave Symmetry (HWS)**|$f(t \pm T/2) = -f(t)$|$a_0 = 0$<br><br>  <br>  <br><br>$a_n = b_n = 0$ for **even** $n$<br><br>  <br>  <br><br>$a_n = \frac{4}{T}\int_0^{T/2} f(t)\cos(n\omega_0 t)dt$ ($n$ odd)<br><br>  <br>  <br><br>$b_n = \frac{4}{T}\int_0^{T/2} f(t)\sin(n\omega_0 t)dt$ ($n$ odd)|Contains **odd harmonics only** ($n = 1, 3, 5, \dots$).|
|**Even Half-Wave**|Even + HWS|$a_n \neq 0$ for odd $n$ only<br><br>  <br>  <br><br>$b_n = 0$ for all $n$|$a_n = \frac{8}{T}\int_0^{T/4} f(t)\cos(n\omega_0 t)dt$ ($n$ odd)|
|**Odd Half-Wave**|Odd + HWS|$b_n \neq 0$ for odd $n$ only<br><br>  <br>  <br><br>$a_n = 0$ for all $n$|$b_n = \frac{8}{T}\int_0^{T/4} f(t)\sin(n\omega_0 t)dt$ ($n$ odd)|
|**Quarter-Wave Symmetry**|HWS + Even/Odd|Defined by symmetry about $T/4$.|Integrals only span $[0, T/4]$.|

