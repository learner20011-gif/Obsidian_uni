

1. ### **Classifications of system**

2.   **Page 1, Q1(a):** A system H has its input-output pairs given. Determine whether the system could be memoryless, causal, linear, and time invariant. For all cases justify your answers. ![[Pasted image 20260829104628.png]] [Figure Involved]
3.   **Page 5, Q1(b):** Consider the system shown in the following figure, determine is it (i) memory less (ii) Causal (iii) time-invariant? ![[Pasted image 20260829104703.png]] [Figure Involved]
4.   **Page 5, Q1(c):** Determine which of the following system is linear or non-linear? 
    1. (i) $\frac{dy(t)}{dt} + t^2y(t) = (2t+3)x(t)$ 
    2. (ii) $y(t)\frac{dy(t)}{dt} + 3y(t) = x(t)$
5.   **Page 14, Q1(a):** A system is specified by its input-output relationship as $y(t) = \frac{x^2(t)}{dx/dt}$. Show that the system satisfies the homogeneity property but not the additivity property.
6.   **Page 17, Q2(a):** Briefly describe the following classifications of systems, (i) a causal system, and (ii) a time invariant system.
7. A system has the following input-output relation: $y(t) = x(t) - 0.5(t+1)$. State the justification, whether this system is time invariant and causal.
8.   **Page 20, Q1(b):** What is linearity and non-linearity of a system? How non-linearity affects on system performance?
9.   **Page 20, Q2(a):** Define zero-input response and zero-state response.
10.   **Page 22, Q2:** A time limited rectangular pulse (left) is applied to a system produces an output as shown in the following figure (right). Express y(t) in terms of x(t). Also provide a mathematical justification whether the system is (i) Linear (ii) Time invariant and (iii) Causal.![[Pasted image 20260829104752.png]] [Figure Involved]
11.   **Page 28, Q1:** Consider a discrete-time system whose output signal y[n] is the average of the three most recent values of the input signal x[n]; that is $y[n] = \frac{1}{3}(x[n] + x[n-1] + x[n-2])$. Such a system is referred as a moving-average system. Determine whether the system is (i) Memoryless (ii) Causal (iii) Linear (iv) Time-invariant (v) Stable.
12.   **Page 39, Q1:** Consider a discrete-time system whose output signal y[n] is the average of the three most recent values of the input signal x[n]; that is $y[n] = \frac{1}{3}(x[n+1] + x[n] + x[n-1])$. Such a system is referred as a moving-average system. Determine whether the system is (i) Memoryless (ii) Causal (iii) Linear (iv) Time-invariant (v) Stable with short reasoning.
13.   **Page 45, Q2:** The input and output relationship of a system is shown in the following figure. Express y(t) in terms of x(t). Also provide a mathematical justification whether the system is (i) Linear (ii) Time-variant and (iii) Causal.![[Pasted image 20260829104821.png]] [Figure Involved]
14.   **Page 48, Q.1(a) (Top):** What is linear system? Explain linear system from physical and mathematical point of view.
15.   **Page 48, Q.1(a) (Middle):** Show that the system described by the following equation is linear: $\frac{dy}{dt} + t^2y(t) = (2t+3)x(t)$
16.   **Page 48, Q.1(a) (Bottom):** Why is the linear system important to study? Explain linear system from physical point of view and mathematical point of view.
17.   **Page 48, Q.1(b):** What is system? Show that the system described by the following equation is linear. $\frac{dy}{dt} + 3y(t) = x(t)$
18. **Page 42, CT-01 Q2:** Determine whether the following systems are (i) Time-variant and (iii) Causal. (a) $y_1(t) = t x(t+1)$ (b) $y_2(t) = x(1-t)$
19. ### **Representation of systems by block diagrams**

20.   **Page 7, Q6(b):** A canonical form of the system is shown in the following figure. (i) Find the transfer function of the system. (ii) Find the impulse response of the system.![[Pasted image 20260829104849.png]] [Figure Involved]
21.   **Page 21, Q7(c):** Determine the transfer function H(s) = Vo(s)/Vi(s) of the circuit given in Fig.Q.7(c). ![[Pasted image 20260829104925.png]][Figure Involved]

22. ### **Differential and difference equations for LTI systems**

23.   **Page 6, Q3(c):** The response of an RLC circuit can be described by the following differential equation: $\frac{d^2v}{dt^2} + 6\frac{dv}{dt} + 5 = v_s(t)$ 
    1. (i) Find the impulse response of the system. 
    2. (ii) Find the response if $v_s(t)=u(t)$.
24.   **Page 16, Q7(b):** The input and output of a stable and causal system are related by the differential equation $\frac{d^2y(t)}{dt^2} + 6\frac{dy(t)}{dt} + 8y(t) = 2x(t)$. 
    1. (i) Find the impulse response of this system. 
    2. (ii) What is the response of this system if $x(t) = te^{-2t}u(t)$?
25.   **Page 19, Q8(a):** A causal discrete time LTI system is describe by $y[n] - \frac{3}{4}y[n-1] + \frac{1}{8}y[n-2] = x[n]$, where, x[n] and y[n] are the input and output of the system, respectively. 
    1. (i) Determine the transfer function, H(z). 
    2. (ii) Determine the impulse response h[n]. 
    3. (iii) Find the step response s[n] of the system.

26. ### **State space representations**

27.   **Page 20, Q3(a):** Define State variable and state equation. How they are important for linear system analysis?
28.   **Page 20, Q3(b):** Find the state equation for the circuit of Fig.Q.3(b).![[Pasted image 20260829105012.png]] [Figure Involved]
29.   **Page 21, Q7(b):** Consider a system having state space representation of $\dot{x} = Ax + Bu$, $y = Cx + Du$ where the symbols have their usual meaning. Find the transfer function of the system.

30. ### **Modelling of electrical, Mechanical and electromechanical system**

31.   **Page 4, Q8(b):** Draw the equivalent mechanical system for the following electrical network.![[Pasted image 20260829105045.png]] [Figure Involved]
32.   **Page 8, Q8(a):** A translational mechanical system is shown below. (i) Find the transfer function of the system. (ii) Find the impulse response if D = 0. (iii) Find the response x(t) if f(t) = u(t). Assume D = 0. ![[Pasted image 20260829105105.png]] [Figure Involved]
33.   **Page 13, Q7(a):** What is analogous system? Draw the electrical analogous for the following mechanical system using f-v analogy.![[Pasted image 20260829105135.png]] [Figure Involved]
34.   **Page 17, Q1(b):** What do you mean by analogous systems? What is intuitive mechanical analogy? Draw the analogous electrical circuit of the following mechanical system using intuitive analogy.![[Pasted image 20260829105213.png]] [Figure Involved]
35.   **Page 21, Q8(a):** What is f-v analogy? Write down the rules to draw f-v analogous Electrical circuit from Mechanical system.
36.   **Page 21, Q8(b):** Draw the equivalent Mechanical system for the circuit given in Fig. Q. 8(b). ![[Pasted image 20260829105303.png]] [Figure Involved]
37.   **Page 73, Q7(a):** What is analogous system? State D'Alembert's principle. Draw the f-v analogous electrical circuit of the following mechanical system-![[Pasted image 20260829105333.png]] [Figure Involved]
38.   **Page 73, Q7(b):** For the following mechanical system, find the transfer function X(s)/F(s). Also draw the electrical equivalent using force-current analogy. ![[Pasted image 20260829105356.png]] [Figure Involved]
39.   **Page 73, Q7(c):** Explain D'Alembert principle.
40.   **Page 74, Q4(a):** What is meant by analogous system? What are the distinct advantages to reduce systems to their analogous electrical circuits?
41.   **Page 74, Q7(b):** Find the equations that describe the motion of the mechanical system shown below. Also draw the electrical equivalent circuit using (i) Force-voltage analogy and (ii) Force-current analogy. ![[Pasted image 20260829105411.png]] [Figure Involved]
42.   **Page 74, Q8(b):** State D'Alembert's principle. Find the equations that describe the motion of the mechanical system of the following figure using (i) D'Alembert's principle and (ii) f-v analogy.![[Pasted image 20260829105432.png]] [Figure Involved]

43. ### **Transfer functions of LTI systems**

44.   **Page 2, Q3(c):** A second order active filter is shown below. (i) Find the transfer function. (ii) Find the impulse response. ![[Pasted image 20260829105534.png]] [Figure Involved]
45.   **Page 4, Q8(a):** The step response of the following system is $v_o(t) = 5e^{-4t}\sin(2t)u(t)$. (i) Find the transfer function H(s). (ii) Comment on the stability of the system.![[Pasted image 20260829105601.png]][Figure Involved]
46.   **Page 10, Q4(a):** The transfer function of a certain circuit is $H(s) = \frac{5}{s+1} - \frac{3}{s+2} + \frac{6}{s+4}$. Find the impulse response of the circuit.
47.   **Page 14, Q1(b):** Write the input-output relationship for an ideal integrator. Determine the zero-input and zero-state components of the response.
48.   **Page 15, Q4(a):** A system has the transfer function $H(s) = \frac{s}{(s+1)(s+2)}$. (i) Find the impulse response of the system. (ii) Determine the output y(t), given the input is x(t) = u(t).
49.   **Page 16, Q7(a):** Consider an LTI system S with impulse response $h(t) = \frac{\sin(4(t-1))}{\pi(t-1)}$. Determine the output of S for each of the following inputs; (i) $x_1(t) = \cos(6t+\pi/2)$ (ii) $x_2(t) = \frac{\sin(4(t+1))}{\pi(t+1)}$.
50.   **Page 24, Q1:** For the following circuit, find the transfer function. Also find iL(t) if (i) it(t) = δ(t) (ii) it(t) = u(t) and (iii) it(t) = e^{-t}u(t). Assume τ = 1s. ![[Pasted image 20260829105630.png]][Figure Involved]
51.   **Page 63, Q7(a):** A linear system's transfer function has a pole at s = -6 and a zero at s = 0. Find the response of the system due to input $45e^{-3t}u(t)$ and its impulse response.
  
52. **Page 35, Q2:** For the following circuit, express the transfer function, H(s) in terms of time constant, $\tau$. Find $v_0(t)$ when (i) $v_i(t) = \delta(t)$ (ii) $v_i(t) = u(t)$ and (iii) $v_i(t) = e^{-t}u(t)$. Assume $\tau = 1s$.![[Pasted image 20260829105710.png]] [Figure Involved] 
53. **Page 41, Q1:** For the circuit (i) Find the transfer function H(s)=V2(s)/V1(s) (ii) Draw the pole-zero plot of H(s). (iii) Find the step response. (2 Marks) (iv) Comment on the stability of the system. (2 Marks)![[Pasted image 20260829105815.png]] [Figure Involved] 
54. **Page 58, Q.4(b):** For the following circuit, find the transfer function. Also find $i_o(t)$ when (i) $i_s(t) = e^{-t}u(t)$ and (ii) $i_s(t) = \sin t$. ![[Pasted image 20260829105849.png]] [Figure Involved] 
55. **Page 62, Q.6(a):** Find the transfer function $H(s) = \frac{I_o(s)}{I_s(s)}$ referring to the following network. ![[Pasted image 20260829105913.png]] [Figure Involved]
56. ### **Pole-zero diagram and system stability**

57.   **Page 2, Q3(a):** The circuit in the following Fig. contains a current controlled voltage source. What restriction must be placed on the gain R of this dependent source to guarantee stability? ![[Pasted image 20260829105958.png]] [Figure Involved]
58.   **Page 3, Q5(b):** For the following circuit (i) Find the transfer function G(s) = V2(s)/V1(s). (ii) Select values of R and L so that the transfer function has a zero at S = -120 and a pole at S = -80.![[Pasted image 20260829110016.png]]  [Figure Involved]
59.   **Page 7, Q5(b):** The input to a linear circuit is the voltage vi. The output is the voltage vo. The transfer function of the circuit is H(s) = Vo(s)/Vi(s). The poles and zeros of H(s) are shown in the following pole-zero diagram. (i) Find the transfer function of the system. (ii) Find the step response. (iii) Comment on the stability of the system. ![[Pasted image 20260829110040.png]] [Figure Involved]
60.   **Page 10, Q4(b):** The transfer function of a circuit is $H(s) = \frac{(s+2)}{s^2 - 2s + 2}$. Plot the poles and zeros on the s-plane and determine whether the circuit is stable.
61.   **Page 24, Q2:** A second-order active filter has the transfer function, $G(s) = \frac{1}{s^2 + (\beta+4)s + 4}$. 
    1. (i) Find the response g(t) if β = 0. 
    2. (ii) Sketch g(t) if β = -4. 
    3. (iii) Plot poles and zeros in the complex S plane if β = 4. 
    4. (iv) Find the range of β for which the filter becomes stable.
62.   **Page 44, Q1:** A second order filter circuit has the following transfer function: Find the range of k so that (i) The filter becomes stable. (ii) The filter provides oscillation. $H(s) = \frac{10}{s^2 + (k-5)s + 10}$
  
63. **Page 12, Q.4(c):** For what value of $\beta$ is the following circuit stable? ![[Pasted image 20260829110126.png]]  [Figure Involved] 
64. **Page 15, Q.4(c):** A certain network has an input admittance Y(s). The admittance has a pole at s = -3, a zero at s = -1, and Y($\infty$) = 0.25 S. (i) Find Y(s). (ii) An 8 V battery is connected to the network via a switch. If the switch is closed at t = 0, find the current i(t) through Y(s) using the Laplace transform. 
65. **Page 40, Q1:** For the circuit (i) Find the characteristics equation and characteristics roots (ii) Plot the roots on s-plane (iii) Find the type of damping provided by the system (iv) Find $v_0(t)$ and sketch the waveform (v) What should the value of $R_1$ to obtain an undamped response. ![[Pasted image 20260829110216.png]] [Figure Involved]
66. ### **Realization of system using direct, cascade, and parallel forms**

67.   **Page 3, Q5(c):** Given a transfer function $G(s) = \frac{s^2}{s^2 + 4s + 10}$, synthesize the network. Assume L= 1H.
68.   **Page 4, Q7(b):** A given transfer function can be realized in many different ways. A transfer function can be realized by using integrators or differentiators along with adders and multipliers. Generally differentiator is avoided to realize a transfer function. 
    1. (i) State the reason of preferring integrator over differentiator in system realization. 
    2. (ii) Realize the following transfer function by any one of the following forms. Canonic direct, series and parallel forms. $H(s) = \frac{s(s+2)}{(s+1)(s+3)(s+4)}$
69.   **Page 7, Q5(c):** Design an op-amp circuit using the figure that will realize the following transfer function. Choose $C_1 = 10\mu F$, determine $R_1$, $R_2$, and $C_2$. $\frac{V_0(s)}{V_i(s)} = \frac{-(s+1000)}{2(s+4000)}$ ![[Pasted image 20260829110248.png]] [Figure Involved]
70.   **Page 12, Q5(a):** Realize the function $G(s) = \frac{V_2(s)}{V_1(s)} = \frac{4s}{s^2 + 4s + 20}$ using the following circuit. Select R = 2Ω, and determine L and C. ![[Pasted image 20260829110318.png]]  [Figure Involved]
71.   **Page 18, Q6(b):** What is network synthesis? Synthesis the function $T(s) = \frac{V_0(s)}{V_i(s)} = \frac{-2s}{s^2+6s+10}$ using the topology in the following figure. ![[Pasted image 20260829110345.png]]  [Figure Involved]

72. ### **Interconnection of system**

73.   **Page 3, Q6(a):** A system is formed by cascading two systems as shown. Given that the impulse response of the system are $h_1(t) = 3e^{-t}u(t)$, $h_2(t) = e^{-4t}u(t)$. ![[Pasted image 20260829110417.png]]
    1. (i) Obtain the impulse response of the overall system H(s) and h(t). 
    2. (ii) Pole-zero plot of the overall system. 
    3. (iii) Check if the overall system is stable. [Figure Involved]
74.   **Page 8, Q6(c):** Figure shows a cascade connection of two LTIC systems. The transfer function of these system are $H_1(s) = \frac{1}{s-1}$ and $H_2(s) = \frac{s-1}{s+1}$. Determine the BIBO and asymptotic stability of the composite system. ![[Pasted image 20260829110433.png]] [Figure Involved]

75. ### **Basic feedback system**

76.   **Page 21, Q8(c):** Write down the name of processes to determine the stability of a system. Find the value of K for the closed-loop system given in Fig. Q. 8(c) so that the closed-loop system is stable. ![[Pasted image 20260829110502.png]] [Figure Involved]

77. ### **Inverse system**

78.   **Page 5, Q2(a):** The input-output relationship of a system is shown below. 
    1. $y(t) = V_{cc}, x(t) > V_{ref}$
    2. $y(t) = -V_{cc}, x(t) < -V_{ref}$
    3. $y(t) = 2x(t), \text{otherwise}$
    4. Justify whether the system is (i) Invertible (ii) BIBO stable
79.   **Page 33, Q1:** The input-output relationship of a system is shown in the following figure. Provide a mathematical justification whether the system is (i) Linear and (ii) Invertible.![[Pasted image 20260829110534.png]]  [Figure Involved]
80.   **Page 34, Q1:** The input-output relationship of two systems are shown the following figure. Provide a mathematical justification whether the system shown in figure (i) linear, and (ii) invertible. For both systems the slope is unity.![[Pasted image 20260829110552.png]] [Figure Involved]

81. ### **Distortion less system**
82. **Page 20, Q.4(c):** Explain Harmonic Distortion in an Amplifier with necessary diagram.
83. *(No specific questions matching purely "distortion less system" criteria were explicitly found in this PDF's text).*





84. Based on the provided PDF, here are the full texts of the questions related to the requested topics under **Application of Signals and Systems in Communication**, organized accordingly. Exact word-for-word duplicates have been filtered to keep only one instance.

85. ### **Signal and carrier**
86. *(No specific questions purely asking to define or differentiate "signal" vs "carrier" outside of the AM modulation questions below were found in this PDF).*

87. ### **Bandwidth and spectrum allocation**

88.   **Page 10, Q.5(a):** Obtain and draw the frequency spectrum of the following waveform. ![[Pasted image 20260829110626.png]] [Figure Involved]
89.   **Page 13, Q.6(a):** Define the following terms: (i) Amplitude spectrum, (ii) Phase spectrum, and (iii) Ladder network.
90.   **Page 13, Q.6(b):** Why a time limited signal is band unlimited in frequency domain? Explain
91.   **Page 16, Q.7(c):** Find the exponential series of the following signal. Also draw the spectrum of that signal. ![[Pasted image 20260829110652.png]] [Figure Involved]
92.   **Page 18, Q.4(a):** If the periodic voltage as shown in the following figure is applied to the following network; Draw the frequency spectrum of $i_0(t)$. ![[Pasted image 20260829110719.png]] [Figure Involved]
93.   **Page 18, Q.4(b):** A spectrum analyzer indicates that a signal made up of three components only: 640 kHz at 2 V, 644 kHz at 1 V, 636kHz at 1 V. If the signal is applied across a 10 $\Omega$ resistor, what is the average power absorbed by the resistor.
94.   **Page 27, Q2:** Find the Fourier series of the square wave in following Fig. Plot the amplitude and phase spectra. ![[Pasted image 20260829110758.png]] [Figure Involved]
95.   **Page 37, Q1:** The following input signal is applied to an ideal band pass filer with gain, |H| = 1 and lower cutoff frequency, $\omega_1 = 6$ rad/s and upper cutoff frequency, $\omega_2 = 12$ rad/s. (a) Determine the output signal. (b) What would be the range of bandwidth and the corner frequency so that the filter allows only the fundamental component. ![[Pasted image 20260829110818.png]] [Figure Involved]
96.   **Page 65, Q(a) (Top):** Show that the energy associated with a non-periodic signal is spread over the entire frequency spectrum, whereas the energy of a periodic signal is concentrated at the frequencies of its harmonic components.
97.   **Page 65, Q.6(b):** Draw the amplitude spectrum of the following waveform.![[Pasted image 20260829110845.png]]  [Figure Involved]
98.   **Page 66, Q(b) (Middle):** Plot the amplitude and phase spectra of the following waveform.![[Pasted image 20260829110911.png]]  [Figure Involved]
99.   **Page 68, Q(c) (Middle):** Derive the Fourier transform of the rectangular pulse as shown in the figure below. Also graphically illustrate that with increasing pulse width, the amplitude spectrum is congested.![[Pasted image 20260829110932.png]] [Figure Involved]
100.   **Page 68, Q(b) (Bottom):** Draw the frequency spectrum for the following signal.![[Pasted image 20260829110946.png]] [Figure Involved]

101. ### **Modulation schemes: AM, FM and PM**

102.   **Page 8, Q.7(b):** Discuss amplitude modulation and sampling as the application scenarios of Fourier transform.
103.   **Page 21, Q.5(b):** What is modulation? Explain amplitude modulation. What are the demerits of amplitude modulation?
104.   **Page 67, Q.5(c):** Explain the amplitude modulation property of Fourier transform.

105. ### **Modulators and demodulators**
106. *(No questions specifically asking for the circuit design, block diagrams, or mathematical analysis of modulator/demodulator hardware were found in this PDF).*

107. ### **Time division and Frequency division multiplexing**

108.   **Page 21, Q.5(a):** Define and explain frequency division multiplexing and time division multiplexing.