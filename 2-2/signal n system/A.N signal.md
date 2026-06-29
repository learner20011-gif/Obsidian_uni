## Atomic Notes: Periodicity of Continuous-Time Signals## Core Concept
A continuous-time signal $x(t)$ is periodic if it repeats itself exactly at regular intervals. Mathematically, it satisfies $x(t) = x(t + T)$ for all $t$, where $T$ is a positive constant.
## Fundamental Period ($T_0$)

* The smallest positive value of $T$ that satisfies $x(t) = x(t + T)$.
* For a standard sinusoid $x(t) = \sin(\omega t)$ or $\cos(\omega t)$, the fundamental period is:
$$T_0 = \frac{2\pi}{\omega}$$ 

------------------------------
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


