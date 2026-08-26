# Questions on Signals & Systems (Comprehensive Collection)

### **1. System Properties**

1. **Linearity Test:** The system relationship is given by:
   $$y(t) = \text{Re}\{x(t)\}$$
   Determine whether the system satisfies both **additivity** and **homogeneity** to prove whether it is linear or non-linear.

2. **Q.1 (a) Memoryless, Causal, Linear, and Time-Invariant Analysis:** A system $H$ has its input-output pairs given. Determine whether the system could be memoryless, causal, linear, and time invariant. For all cases justify your answers. ![[Pasted image 20260626191842.png]] [Figure involved]

3. **Q.1 (b) Modulation System:** Consider the system shown in the following figure, determine is it (i) memoryless (ii) Causal (iii) time-invariant? ![[Pasted image 20260626191633.png]] [Figure involved]

4. **Q.1 (c) Differential Equation Linearity:** Determine which of the following system is linear or non-linear?
   - (i) $\frac{dy(t)}{dt} + t^2y(t) = (2t+3)x(t)$
   - (ii) $y(t)\frac{dy(t)}{dt} + 3y(t) = x(t)$

5. **Q.1 (a) Homogeneity vs. Additivity:** A system is specified by its input-output relationship as:
   $$y(t) = \frac{x^2(t)}{\frac{dx(t)}{dt}}$$
   Show that the system satisfies the homogeneity property but not the additivity property.

6. **Q.2 (a) Piecewise Saturation System:** The input-output relationship of a system is shown below:
   $$y(t) = \begin{cases} V_{cc}, & x(t) > V_{ref} \\ -V_{cc}, & x(t) < -V_{ref} \\ 2x(t), & \text{otherwise} \end{cases}$$
   Justify whether the system is (i) Invertible (ii) BIBO stable.

7. **Q.2 (a) System Classifications & Time-Varying Properties:**
   - (i) Briefly describe the following classifications of systems: (1) a causal system, and (2) a time invariant system.
   - (ii) A system has the following input-output relation: $y(t) = x(t) - 0.5(t + 1)$. Determine whether this system is time invariant and causal.

8. **Differentiator Time-Invariance:** Provide a mathematical proof to determine whether the differentiator system $y(t) = \frac{d}{dt}x(t)$ is time-invariant or time-varying.

9. **Modulated Delay System:** Prove via time-shifting whether the system $y(t) = (\sin t)x(t-2)$ is time-invariant or time-varying.

10. **Memoryless vs. Dynamic (With Memory) Classifications:** Classify each of the following systems as memoryless or dynamic (with memory):
    - (a) $y(t - 1) = 2x(t - 1)$
    - (b) $y(t) = \frac{d}{dt}x(t)$
    - (c) $y(t) = (t - 1)x(t)$

11. **Time-Reversal Causality:** Analyze whether the system $y(t) = x(-t)$ is causal or non-causal.

12. **Integrator Causality & Delay Realizability:**
    - (i) Proof of non-causality for the system: $y(t) = \int_{t-5}^{t+5} x(\tau) d\tau$.
    - (ii) Proof of realizability with a 5-second delay: $y_d(t) = y(t-5) = \int_{t-10}^t x(\tau) d\tau$.

13. **Invertibility Tests:** Determine whether each of the following systems is invertible or non-invertible:
    - (a) $y(t) = x(-t)$
    - (b) $y(t) = tx(t)$
    - (c) $y(t) = \frac{d}{dt}x(t)$

14. **BIBO Stability Worked Examples:** Determine whether the following systems are BIBO stable:
    - (i) $y(t) = t \cdot x(t)$
    - (ii) $y(t) = x(t) + 2$
    - (iii) $y(t) = \sin(t) \cdot x(t)$
    - (iv) $y(t) = x^2(t)$
    - (v) $y(t) = \frac{d}{dt}x(t)$

15. **Pg 22, CT-1 Q2:** A time limited rectangular pulse (left) is applied to a system produces an output as shown in the following figure (right). Express $y(t)$ in terms of $x(t)$. Also provide a mathematical justification whether the system is (i) Linear (ii) Time invariant and (iii) Causal. ![[Pasted image 20260712005359.png]] [Figure involved]

16. **Pg 28, CT-1 Q1:** Consider a discrete-time system whose output signal $y[n]$ is the average of the three most recent values of the input signal $x[n]$; that is:
    $$y[n] = \frac{1}{3} (x[n] + x[n-1] + x[n-2])$$
    Such a system is referred to as a moving-average system. Determine whether the system is (i) Memoryless (ii) Causal (iii) Linear (iv) Time-invariant (v) Stable.

17. **Pg 33, CT-2 Q1:** The input-output relationship of a system is shown in the following figure. Provide a mathematical justification whether the system is (i) Linear and (ii) Invertible. ![[Pasted image 20260712005701.png]] [Figure involved]

18. **Pg 34, CT-2 Q1:** The input-output relationship of two systems are shown in the following figure. Provide a mathematical justification whether the system shown in figure (i) is linear, and (ii) invertible. For both systems the slope is unity. ![[Pasted image 20260712005710.png]] [Figure involved]

19. **Pg 39, CT-1 Q1:** Consider a discrete-time system whose output signal $y[n]$ is the average of the three most recent values of the input signal $x[n]$; that is:
    $$y[n] = \frac{1}{3} (x[n+1] + x[n] + x[n-1])$$
    Such a system is referred to as a moving-average system. Determine whether the system is (i) Memoryless (ii) Causal (iii) Linear (iv) Time-invariant (v) Stable with short reasoning.

20. **Pg 41, CT-01 Q2:** Determine whether the following systems are (i) Time-variant and (ii) Causal:
    - (a) $y_1(t) = t \cdot x(t+1)$
    - (b) $y_2(t) = x(1-t)$

21. **Pg 44, CT-01 Q2:** The input and output relationship of a system is shown in the following figure. Express $y(t)$ in terms of $x(t)$. Also provide a mathematical justification whether the system is (i) Linear (ii) Time-variant and (iii) Causal. ![[Pasted image 20260712010339.png]] [Figure involved]

---

### **2. Energy and Power Signals**

22. **Q.1 (b) Energy/Power Classification & Computation:** Provide a mathematical justification whether the following signals are energy or power signal or neither:
    - (i) $e^{kt} u(-t), \quad k>0$
    - (ii) $u(t+2) - u(t-2)$
    Also compute the energy and power of them.

23. **Q.1 (a) Energy and Power Definitions & Classification:** Define energy signal and power signal. Determine whether the following signals are energy signals, power signals or neither:
    - (i) $x_1(t) = e^{-at} u(t)$
    - (ii) $x_2(t) = A\cos(\omega t+\theta)$
    - (iii) $x_3(t) = t u(t)$

24. **Complex Exponential Signal Power & RMS:** For a complex exponential signal of the form $x(t) = D e^{j\omega_0 t}$ (where $D$ is a complex constant), compute the average power $P_x$ and find its root-mean-square (RMS) value.

25. **Constant / DC Signal:** For a DC signal $x(t) = A$, determine whether it is an energy or power signal, and compute its total energy $E$ and average power $P$.

26. **Pg 22, CT-1 Q1:** For the following signal, sketch (i) $y_1(t)=x(t+1)$ and (ii) $y_2(t)=x(t+1)r(t-1)$. Justify whether $y_2(t)$ is energy signal or power signal or neither? Also compute the energy and power of $y_2(t)$. ![[Pasted image 20260712005325.png]] [Figure involved]

27. **Pg 28, CT-1 Q2:** Draw the following signal and comment whether the signal is energy, power or neither energy nor power signal:
    - (i) $e^{-at} u(-t)$ and $a$ is real (evaluating $a > 0$, $a < 0$, and $a = 0$)
    - (ii) $t u(t)$

28. **Pg 31, CT-1 Q1:** Determine the energy and power of the following signals:
    - (i) $k e^{\beta t}, \quad k>0, \beta<0$
    - (ii) $k e^{\beta t}, \quad k>0, \beta=-2j$
    - (iii) $\cos(10\pi t)u(-t)$
    - (iv) $\text{rect}(t/4) = u(t+2) - u(t-2)$

29. **Pg 32, CT-1 Q1:** Determine whether the following signals are energy signal, power signal or neither. Also compute the energy and power of each signals:
    - (i) $e^{\sigma t}u(-t), \quad \sigma>0$
    - (ii) $e^{\sigma t}u(-t), \quad \sigma<0$
    - (iii) $t[u(t+4)-u(t-4)]$
    - (iv) $3\cos(5t+\pi/4)$

30. **Pg 39, CT-1 Q2:** Draw the following signal and comment whether the signal is energy, power or neither energy nor power signal:
    - (i) $e^{-at} u(-t)$ and $a$ is real.

31. **Pg 42, CT-01 Q1:** For the following signal $x(t)$, sketch (i) $y_1(t)=x(2t-5)$ and (ii) $y_3(t)=x(t)r(t)$. Provide a mathematical justification whether $y_2(t)$ is an energy signal or power signal or neither? Also compute the energy and power of $y_2(t)$. ![[Pasted image 20260712010221.png]] [Figure involved]

32. **Pg 44, CT-01 Q1:** Sketch the signals:
    - (i) $u(4-t)$
    - (ii) $u(t-6)-u(t-8)$
    - (iii) $\sin(\pi t)[\delta(t+0.5)+\delta(t-0.5)]$
    - (iv) $5\cos(10\pi t - \pi/3)$
    Analytically determine whether the signal $u(t-4)-u(t-6)$ is energy or power signal? Also compute energy and power of that signal.

---

### **3. Signal Fundamentals & Operations**

33. **Q.1 (c) Inverse Transformation & Analytical Expression:** The output $y(t)$ of the following figure is obtained by the transformation $y(t)= x(2t-4)$.
    - (i) Sketch the input, $x(t)$.
    - (ii) Analytically express, $x(t)$. ![[Pasted image 20260626191823.png]] [Figure involved]

34. **Q.1 (a) Impulse Function Definition & Sketch:** What is impulse function? Draw the following function:
    $$f(t) = 5\delta(t+2) + 10\delta(t) - 4\delta(t-3)$$

35. **Gate Function & Switching Functions Representation (Set 1):** Define gate function. Express the following signal in terms of switching functions. ![[Pasted image 20260628100238.png]] [Figure involved]

36. **Gate Function & Switching Functions Representation (Set 2):** Define gate function. Express the following signal in terms of switching functions. ![[Pasted image 20260628171225.png]] [Figure involved]

37. **Derivatives of Standard Signals & Switching Functions:**
    - (i) Express the $\text{sgn}(t)$ function in terms of the step function $u(t)$.
    - (ii) Find the first derivatives of the following signals and sketch the signals and their derivatives:
      - (1) $x(t) = u(t) - u(t - a), \quad a > 0$
      - (2) $y(t) = t[u(t) - u(t - a)], \quad a > 0$
    - (iii) Define switching functions with examples. Express the following signals in terms of switching functions: $v_1(t)$ and $v_2(t)$. ![[Pasted image 20260628170559.png]] [Figure involved]

38. **Current Pulse Step Expression & Integral:** Express the current pulse given in Fig. Q. 3(c) in terms of unit step and find its integral. ![[Pasted image 20260628170939.png]] [Figure involved]

39. **Sifting Property Evaluation:** Show that:
    $$\int_{-\infty}^{\infty} e^{-2(x-t)}\delta(2 - t) dt = e^{-2(x-2)}$$

40. **Pg 29, CT-1 Q3:** Given the signal in the following figure. Sketch the following signals derived from $x(t)$:
    - (i) $x(2t+1)$
    - (ii) $x(t+1)u(-t)$
    - (iii) $x(-t+1)u(t)$
    - (iv) $x(t-1)+x(-t-1)$
    - (v) $x(t)\delta(t-1)$ ![[Pasted image 20260712005603.png]] [Figure involved]

41. **Pg 31, CT-1 Q2:** Sketch the following signal:
    $$x(t) = \begin{cases} e^{2t}, & -4 \le t \le -2 \\ 2, & -2 \le t \le 2 \\ e^{-2t}, & 2 \le t \le 4 \\ 0, & \text{otherwise} \end{cases}$$
    Also sketch $y(t)=x(\alpha t+\beta)$ when (i) $\alpha=-2, \beta=0$, (ii) $\alpha=2, \beta=-4$, and (iii) $\alpha=-1, \beta=4$.

42. **Pg 32, CT-1 Q2:** For the following signal:
    $$x(t) = \begin{cases} t, & 0 \le t \le 2 \\ 2, & 2 \le t \le 4 \\ 0, & \text{otherwise} \end{cases}$$
    sketch: (i) $x(t/2)$, (ii) $x(t+4)$, (iii) $x(4-t)$, and (iv) $x(2t+6)$.

43. **Pg 39, CT-1 Q3:** Given the signal $x(t)$ in the following figure. Sketch the following signals derived from $x(t)$:
    - (i) $x(2t-1)$
    - (ii) $x(t+1)u(-t)$
    - (iii) $x(-t+1)u(t)$
    - (iv) $x(t)[u(t-1)-u(t-2)]$
    - (v) $x(t)\delta(t-2)$ ![[Pasted image 20260712005941.png]] [Figure involved]

---

### **4. Laplace Transform**

44. **Laplace Transform of Linear Ramp:** Find the Laplace transform of the following function $h(t) = 2t[u(t)-u(t-1)]$. ![[Pasted image 20260628100212.png]] [Figure involved]

45. **Laplace Transform of Triangular Waveform:** Find the Laplace transform of the following function $h(t)$. ![[Pasted image 20260628171238.png]] [Figure involved]

46. **Laplace Transform of Symmetric Triangular Signal:** Find the Laplace transform of the following signal using the properties of Laplace transform. ![[Pasted image 20260628100524.png]] [Figure involved]

47. **Q.2 (a) Laplace Transform Properties:** Explain the following properties of the Laplace transform:
    - (i) Scaling
    - (ii) Time shift
    - (iii) Frequency shift

48. **Q.2 (b) Multi-Step Waveform Laplace Transform:** Find the Laplace transform of the function $h(t)$ in the figure below. ![[Pasted image 20260628100445.png]] [Figure involved]

49. **Q.3 (a) Periodic Sawtooth Waveform Laplace Transform:** Calculate the Laplace transform of the following periodic function. ![[Pasted image 20260628100339.png]] [Figure involved]

50. **Q.4 (a) ROC Sketching & Laplace Transformability:** Sketch the ROC of each of the following signals and also identify whether they are Laplace transformable or not?
    - (i) $e^{at} u(-t)$
    - (ii) $e^{-at} u(-t)+ e^{bt} u(t)$

51. **Pg 35, CT-3 Q1:** Find the Laplace transform of (i) $e^{3t} u(-t)$ and (ii) $e^{-3t} u(t) + e^{3t} u(-t)$. Also sketch ROC of them.

52. **Pg 36, CT-3 Q1:** Using the differentiation property, find the Laplace transform of the following function. ![[Pasted image 20260712005827.png]] [Figure involved]

53. **Pg 42, CT-3 Q2:** Sketch the Region of Convergence (ROC) in the complex s-plane of the following signals. Clearly indicate the boundaries of the ROC and the locations of the poles:
    - (i) $f(t)=e^{-at} u(-t)+e^{bt} u(t)$ (for cases $b < -a$ and $b > -a$)
    - (ii) $f(t)=e^{at} u(t)+e^{bt} u(-t), \quad b>a$
    - (iii) $f(t)=e^{-2t} u(t) + e^{-3t} u(t)$

---

### **5. Fourier Transform**

54. **Differentiation Property & Signum Fourier Transform:** Given that the Fourier Transform of $x(t)$ is $X(\omega)$, the differentiation property of the Fourier transform states that:
    $$\frac{dx(t)}{dt} \Leftrightarrow j\omega X(\omega)$$
    The signum function, $\text{sgn}(t)$ is defined as:
    $$\text{sgn}(t) = \begin{cases} 1, & t > 0 \\ -1, & t < 0 \end{cases}$$
    By applying the differentiation property, or otherwise, show that the Fourier transform of $\text{sgn}(t)$ is:
    $$\text{sgn}(t) \Leftrightarrow \frac{2}{j\omega}$$

55. **Circuit Output Current Fourier Transform:** Determine the Fourier transform of $i_o(t)$ in the following network. ![[Pasted image 20260628170652.png]] [Figure involved]

56. **Q.4 (c) Fourier Transform via Differentiation Property:** Using differentiation property, find the Fourier transform of the following function. ![[Pasted image 20260626191754.png]] [Figure involved]

57. **Q.6 (b) Time-Limited vs. Band-Unlimited Duality:** Why a time limited signal is band unlimited in frequency domain? Explain.

58. **Sine-Wave Pulse Fourier Transform:** Find and draw the Fourier transform of the following sine-wave pulse $f(t) = \sin(\omega_0 t)[u(t) - u(t - T_0)]$. ![[Pasted image 20260628100321.png]] [Figure involved]

59. **Parseval's Theorem:** State and explain Parseval's theorem.

60. **Q.7 (a) Asymmetric Waveform Fourier Transform:** Determine the Fourier transform of the function in the following figure. ![[Pasted image 20260628100406.png]] [Figure involved]

61. **Elementary Function Fourier Transforms:** Find the Fourier transform of the following functions:
    - (i) $\delta(t)$
    - (ii) $e^{j\omega_0 t}$
    - (iii) $\text{sgn}(t)$

62. **Ramp Non-Transformability & Parseval's Theorem:** Why it is not possible to find the Fourier transform of ramp signal? State and explain Parseval's theorem.

63. **Pg 25, CT-4 Q2:** Using differentiation property, find the Fourier transform of the following function. ![[Pasted image 20260712005508.png]] [Figure involved]

64. **Pg 27, CT-3 Q3:** Use the time-differentiation property to find the Fourier transform of the triangle pulse illustrated in Fig. Hints: first draw the first derivative and second derivative of the given function and then use the time-differentiation property. ![[Pasted image 20260712005539.png]] [Figure involved]

---

### **6. Fourier Series & Spectrums**

65. **Active Filter Response to Square Wave:** The square wave in the following waveform is applied to the following network. Find the Fourier series of $v_o(t)$. ![[Pasted image 20260628170311.png]] [Figure involved]

66. **Exponential Fourier Series & Spectrum:** Find the exponential series of the following signal. Also draw the spectrum of that signal. ![[Pasted image 20260628170514.png]] [Figure involved]

67. **Full-Wave Rectified Waveform Fed to Filter Circuit:** A full wave rectified signal having the following Fourier series expansion is used as the input of the circuit shown below:
    $$e(t) = \frac{2\times100}{\pi}\left(1 + \frac{2}{3}\cos 2\omega t - \frac{2}{15}\cos 4\omega t + \frac{2}{35}\cos 6\omega t \dots\right)$$
    where $\omega = 377$.
    Find:
    - (i) The Fourier series expression for the voltage $v_o(t)$ (first three terms only).
    - (ii) Average power delivered to the $1 \text{ k}\Omega$ resistor. ![[Pasted image 20260628100513.png]] [Figure involved]

68. **Half-Wave Rectified Cosine Fourier Series:** Determine the Fourier series for the half wave rectified cosine function of period 4 and amplitude 1.

69. **Trigonometric Fourier Series for Bipolar Square Wave:** Find the trigonometric Fourier series for the square wave signal of Fig. Q. 4(b). ![[Pasted image 20260628170926.png]] [Figure involved]

70. **Q.5 (a) Frequency Spectrum of Periodic Sawtooth:** Obtain and draw the frequency spectrum of the following waveform. ![[Pasted image 20260628100434.png]] [Figure involved]

71. **Q.5 (a) Multitone Periodic Current Analysis:** A certain band-limited periodic current has only three frequencies in its Fourier series representation: dc, 50 Hz, and 100 Hz. The current may be represented as:
    $$i(t) = 4 + 6\sin(100\pi t) + 8\cos(100\pi t) - 3\sin(200\pi t) - 4\cos(200\pi t)\text{ A}$$
    - (i) Express $i(t)$ in amplitude-phase form.
    - (ii) If $i(t)$ flows through a 2 $\Omega$ resistor, how many watt of average power will be dissipated?

72. **Q.6 (a) Spectral & Network Definitions:** Define the following terms:
    - (i) Amplitude spectrum
    - (ii) Phase spectrum
    - (iii) Ladder network

73. **Q.7 (c) Sawtooth Waveform Applied to Filter:** If the sawtooth waveform shown in following Fig. is applied to a filter with the given transfer function:
    - (i) Find the Fourier series expansion of the sawtooth wave.
    - (ii) Determine the output of the filter. ![[Pasted image 20260626191714.png]] [Figure involved]

74. **Pg 27, CT-3 Q2:** Find the Fourier series of the square wave in following Fig. Plot the amplitude and phase spectra. ![[Pasted image 20260712005529.png]] [Figure involved]

---

### **7. Sampling and Modulation**

75. **Fourier Transform Applications in AM and Sampling:** Discuss amplitude modulation and sampling as the application scenarios of Fourier transform.

76. **Q.7 (a) Sampling of Triangular Baseband Spectrum:** Consider a band limited signal $x(t)$ with a Fourier transform $X(\omega)$ shown in the following figure. Draw the Fourier transform of the sampled signal if the sampling frequency is:
    - (i) 5 KHz
    - (ii) 10 kHz
    - (iii) 20 kHz ![[Pasted image 20260626191739.png]] [Figure involved]

---

### **8. Z-Transform**

77. **Significance of Region of Convergence (ROC):** The Z-transform of discrete time signal $x(n)$ must be represented by $X(Z)$ with its ROC - Explain.

78. **Z-Transform of Discrete Pulse Train:** For a discrete time signal as shown in the Fig. 8(c), show that:
    $$X(Z) = \frac{1-z^{-m}}{1-z^{-1}}$$
    ![[Pasted image 20260628170808.png]] [Figure involved]
