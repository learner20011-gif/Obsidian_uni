## Atomic Notes: Periodicity of Continuous-Time Signals
 
## Periodicity of Summed Signals
When adding multiple periodic signals ($x(t) = x_1(t) + x_2(t) + \dots + x_N(t)$):
## 1. Condition for Periodicity
The combined signal is periodic if and only if the ratio of any two individual periods is a rational number (a fraction of integers).
$$\frac{T_1}{T_2} = \frac{m}{n} \quad (\text{where } m, n \in \mathbb{Z}^+)$$ 
## 2. Finding the Combined Fundamental Period ($T_0$)
Once the ratio is simplified to its lowest terms ($\frac{m}{n}$), calculate $T_0$ using cross-multiplication:
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

## Quick Memory Tricks

- $\text{Bounded} \times \text{Bounded} = \text{Bounded}$ ✅
    
- $\text{Growing function (e.g., } t, e^t\text{)} \times \text{Bounded} \to$ Can become Unbounded ❌
    
- Adding a finite constant does not affect stability. ✅
    

> **Exam Definition:** A system is BIBO stable if and only if every bounded input produces a bounded output for all time.