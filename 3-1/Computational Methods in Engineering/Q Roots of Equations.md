# EEE 3109 — Roots of Equations (PYQ)

**Syllabus:** Bracketing method- Bisection method and false-position method; Open method- Fixed point iteration, the Newton-Raphson method, Secant method, Brent's method, Finding multiple roots, Systems of non-linear equations. Roots of polynomials: Muller's method and Baristow's Method.

---

### **Bracketing Methods (Bisection & False-Position)**

1. **(p. 2, (3) — Theory Questions EEE 3109)** What is transcendental equation?

2. **(p. 3, (16) — Theory Questions EEE 3109)** Classify the iterative method.

3. **(p. 3, (17) — Theory Questions EEE 3109)** Algorithm of bisection method.

4. **(p. 7, (46) — Theory Questions EEE 3109)** What are bracketing methods?

5. **(p. 10, (b) — Topic 2: Bracketing Methods (Series 21))** A power amplifier is driving a load through an RLC circuit. The input impedance seen by the amplifier is
   $$z(\omega) = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}$$
   To match impedance, $z(\omega) = 50\ \Omega$ is needed. Given, $R = 10\ \Omega$, $L = 1\text{ mH}$, $C = 1\ \mu\text{F}$. Compute the frequency using false position method. Assume the initial interval $\omega \in [5000, 10000]\text{ rad/s}$. Perform three iteration.

6. **(p. 11, (c) — Topic 2: Bracketing Methods (Series 18))** What is transcendental equation? Use bisection method to find a real root of the equation $x \sin x - 1 = 0$.

7. **(p. 11, (c) [2nd] — Topic 2: Bracketing Methods (Series 18))** Determine the two smallest roots of the following equation: $f(x) = x \sin x + \cos x = 0$ to $3$ significant digits using false position method.

8. **(p. 26, (b) — 2023 Odd Semester (EEE 3109))** Both the Secant and False Position methods use two points as initial guesses. How are they methodologically different?
   *(Exact duplicate also on: p. 11, (b) (Topic 2: Bracketing Methods (Series 20)))*

9. **(p. 26, (c) — 2023 Odd Semester (EEE 3109))** Find a root of the following equation using bisection method.
   $$\log x - \cos x = 0$$
   *(Exact duplicate also on: p. 11, (c) (Topic 2: Bracketing Methods (Series 20)))*

10. **(p. 28, (c) — 2022 Odd Semester (EEE 3109))** Consider the following equation:
   $$f(x) = 3x + \sin x - e^x = 0$$
   Find the root of the above equation using False-position method with initial guesses of $0$ and $1$. Perform $4$ iterations.
   *(Exact duplicate also on: p. 11, (c) (Topic 2: Bracketing Methods (Series 19)))*

11. **(p. 35, (b) — 2017 Odd Semester (EEE 3109))** For 10k 3A Betatherm thermistor, the relationship between the resistor R of the thermistor and the temperature is given by
   $$\frac{1}{T} = 1.129241 \times 10^{-3} + 2.341077 \times 10^{-4}\ln(R) + 8.775468 \times 10^{-8}[\ln(R)]^3$$
   where $T$ is in Kelvin and $R$ is in ohm.
   Use False position method to find the resistance, $R$, at $18.99^{\circ}\text{C}$. Conduct three iterations to estimate $R$. Also find the relative approximate error at the end of each iteration.

12. **(p. 35, Q. 2(a) — 2017 Odd Semester (EEE 3109))** For Bisection method, if $|b - a| = 1$ and $\epsilon = 0.0005$, then show that $n > 10$, where symbols have their usual meanings.

13. **(p. 37, (b) — 2016 Odd Semester (EEE 3109))** What are bracketing methods? You are designing a spherical tank to hold water. The volume of liquid it can hold can be computed as,
   $$V = \pi h^2 \frac{[3R - h]}{3}$$
   $V =$ volume $[\text{ft}^3]$, $h =$ depth of water in tank $[\text{ft}]$ and $R =$ tank radius $[\text{ft}]$. If $R = 3\text{ m}$, what depth must the tank be filled to so that it holds $30\text{ m}^3$? Use a bracketing method to get an answer correct to three significant figures.

14. **(p. 37, Q. 2(a) — 2016 Odd Semester (EEE 3109))** Why do we use bisection method? Is it iterative? Discuss the answer.
   *(Exact duplicate also on: p. 7, (48) (Theory Questions EEE 3109))*

15. **(p. 40, Q. 2(a) — Semester Exam (EEE 3109, Pre-2016))** The power pattern ($U$) of an antenna is given by the following equation
   $$U(\theta) = \cos^2(\theta)\cos^2(3\theta);\text{ where } 0^{\circ} \le \theta \le 90^{\circ}.$$
   The Half-Power Beam Width ($\text{HPBW}$) is given by $\text{HPBW} = 2\theta_h$ where $\theta_h$ is the value of $\theta$ when $U$ is half of the maximum value. Use bisection method to find HPBW of the antenna. Show three iterations.

16. **(p. 43, Q. 5(a) — 2008 Semester Exam (EEE 251))** Discuss the pitfalls of false position method.

17. **(p. 45, (c) — 2007 Regular Exam (EEE-251))** **[figure Involved]** The impedance ($z$) of the following circuit satisfies the equation
   $$\frac{1}{z} = \sqrt{\frac{1}{R^2} + \left(\omega C - \frac{1}{\omega L}\right)^2}$$
   *(Handwritten values on figure: $R = 225\ \Omega,\ C = 0.6 \times 10^{-6}\text{ F},\ L = 0.5\text{ H}$)*
   Find the angular frequency ($\omega$) that results in an impedance of $100\ \Omega$ using bisection method.

   ![[attachments/fig_p45_c.png]]

18. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** What is meant by iterative method? Describe the method of false position graphically to find the roots of equations.

19. **(p. 51, (b) — 2003 Semester Exam (EEE-251C))** What do you mean by Trial and error method?

20. **(p. 56, (c) — 2001 Regular Exam (EEE-251C))** Write a computer program to solve the following equations using the method of false position.
   $$f(x) = \cos x - xe^x$$

21. **(p. 59, (c) — 2000 Regular Exam (EEE-251C, 98 Series))** Write the initialization program for the bisection method to solve numerical problems.

22. **(p. 70, 1. — Class Test (Blue Sheet, EEE 3109))** An oscillating phenomenon in an electric circuit is given by $i(t) = 4e^{-t}\sin t - 1 = 0$. Find a root of the equation by Bolzano's method given that the root lies between $0$ and $0.5$.

### **Open Methods (Fixed-Point Iteration, Newton-Raphson, Secant, Brent's Method)**

23. **(p. 5, (32) — Theory Questions EEE 3109)** Algorithm of secant method to solve a nonlinear transcendental eqn.

24. **(p. 7, (42) — Theory Questions EEE 3109)** Prove that N-R method has a quadratic convergence.

25. **(p. 8, (54) — Theory Questions EEE 3109)** Using Taylor series expansion obtain the Newton-Raphson formula.

26. **(p. 11, (c) [2nd] — Topic 3: Open Methods (Series 21))** Use the modified secant method to estimate the root of $f(x) = e^{-x} - x$. Use a value of $0.01$ for $\delta$ and start with $x_0 = 1.0$. The true root is $0.56714329$. Continue iterations until $|\epsilon_a| = 2.365 \times 10^{-5}\%$.

27. **(p. 11, Q.2. (a) — Topic 3: Open Methods (Series 21))** Starting from the Taylor series expansion, explain with necessary mathematical derivation that the Newton-Raphson method exhibits quadratic convergence.

28. **(p. 12, (b) — Topic 3: Open Methods (Series 18))** Make a table of performance comparison among iterative methods considering formulae, order of convergence, evaluation of functions per iteration and reliability of convergence
   *(Exact duplicate also on: p. 2, (4) (Theory Questions EEE 3109))*

29. **(p. 12, Q. 2(a) — Topic 3: Open Methods (Series 18))** An oscillating current in an electric circuit is described by $i = 9e^{-t}\sin(2\pi t)$, where $t$ is in seconds. Determine the lowest value of a Secant method using $t$ such that $i = 3.6\text{ A}$.

30. **(p. 28, (b) — 2022 Odd Semester (EEE 3109))** Show that fixed point iteration method is linearly convergent. From the analysis, comment on the condition of convergence and divergence using a graphical illustration.
   *(Exact duplicate also on: p. 12, (b) (Topic 3: Open Methods (Series 19)))*

31. **(p. 28, Q. 2(a) — 2022 Odd Semester (EEE 3109))** Derive the expression for the next approximation of a root of the non-linear equation $f(x) = 0$ at a particular iteration stage by Newton-Raphson method. Briefly describe the limitations of this method to find the root.
   *(Exact duplicate also on: p. 12, Q.2. (a) (Topic 3: Open Methods (Series 19)))*

32. **(p. 30, (b) — 2020 Odd Semester (EEE 3109))** For Newton-Raphson method, prove that $\epsilon_{n+1} \cong \frac{1}{2} \epsilon_n^2 \frac{f''(\xi)}{f'(\xi)}$ ; where symbols have their usual meaning.
   *(Exact duplicate also on: p. 12, (b) (Topic 3: Open Methods (Series 17)))*

33. **(p. 30, (c) — 2020 Odd Semester (EEE 3109))** **[figure Involved]** Following figures shows a separately excited dc generator under load condition.
   After calculation, transfer function of this circuit is
   $$T(s) = \frac{V_t(s)}{E_f(s)} = \frac{Kg}{(1 + s\tau_f)(1 + s\tau_a)}\text{ ; where } \tau_f = \frac{L_f}{R_f};\ \tau_a = \frac{L_a}{R_a + Z_L(s)};\ g = \frac{Z_L(s)}{R_a + Z_L(s)};\ k = \frac{k_f}{R_f};$$
   $E_g = K_f I_f(s)$. Find the root of the characteristic equation of this system by using Secant method and comment that the system is stable or not. Let, $k = 3$, $g = 2$, $\tau_f = 2$ and, $\tau_a = 0.5$.
   *(Exact duplicate also on: p. 12, (c) (Topic 3: Open Methods (Series 17)))*

   ![[attachments/fig_p30_c.png]]

34. **(p. 33, (b) — 2018 Odd Semester (EEE 3109))** Write down the computational algorithm of secant method to solve a nonlinear transcendental equation.
   *(Exact duplicate also on: p. 12, (b) (Topic 3: Open Methods (Series 15)))*

35. **(p. 33, (c) — 2018 Odd Semester (EEE 3109))** A total charge $Q$ is uniformly distributed around a ring shaped conductor with radius '$a$'. A charge $q$ is located at a distance '$x$' from the center of the ring. The force exerted on the charge by the ring is given by
   $$F = \frac{qQx}{4\pi\varepsilon_0\left(x^2 + a^2\right)^{3/2}}$$
   where, $\varepsilon_0 = 8.854 \times 10^{-12}\ \text{C}^2/\text{N}\cdot\text{m}^2$. Find the distance '$x$' where the force is $1\text{ N}$ if $q$ and $Q$ are $2 \times 10^{-5}\text{ C}$ for a ring with a radius of $0.9\text{ m}$. Use Newton-Raphson method.
   *(Exact duplicate also on: p. 12, (c) (Topic 3: Open Methods (Series 15)))*

36. **(p. 33, Q. 2(a) — 2018 Odd Semester (EEE 3109))** Compare the iterative methods and hence write the steps of a good practical way to solve nonlinear equation.
   *(Exact duplicate also on: p. 10, Q.2 (a) (Topic 1: Introduction & Error Analysis (Series 15)); p. 5, (31) (Theory Questions EEE 3109))*

37. **(p. 35, (c) — 2017 Odd Semester (EEE 3109))** **[figure Involved]** An unity feedback control system is given below. Find a root of the characteristics equations by using Secant method.

   ![[attachments/fig_p35_c.png]]

38. **(p. 35, Q. 3(a) — 2017 Odd Semester (EEE 3109))** Prove that, Newton-Raphson method has a quadratic convergence.

39. **(p. 37, (c) — 2016 Odd Semester (EEE 3109))** **[figure Involved]** Find a real root of the current in the equation obtained from the figure below using Regula-Falsi and Newton-Raphson methods. Hence decide which one is better.

   ![[attachments/fig_p37_c.png]]

40. **(p. 40, (b) — Semester Exam (EEE 3109, Pre-2016))** What is meant by numerical method? Describe the method of secant graphically to find roots of equations.

41. **(p. 42, (c) — 2008 Semester Exam (EEE 251))** What is meant by open method? Explain the viability of bracketing and open methods to find roots of polynomials. Graphically depict and describe three cases where Newton Raphson method exhibits poor convergence.

42. **(p. 43, (b) — 2008 Semester Exam (EEE 251))** Use the Secant method to estimate the root of $f(x) = e^{-x} - x$. Start with initial estimate of $x_{-1} = 0$ and $x_0 = 1$.

43. **(p. 43, (c) — 2008 Semester Exam (EEE 251))** An oscillating current in an electric circuit is described by $I = 9e^{-t}\sin(2\pi t)\text{ Amp}$, where $t$ is in seconds. Determine all values of $t$ such that $I = 3.5\text{ Amp}$.

44. **(p. 45, Q. 2(a) — 2007 Regular Exam (EEE-251))** Write a computer algorithm to implement Newton-Raphson (NR) method for finding roots of an equation. Discuss some pitfalls of NR method. Upon which factors the convergence of NR method depend ?

45. **(p. 47, (c) — 2006 Semester Exam (EEE 251))** Compare the following methods (i) Bisection (ii) False position (iii) Secant, and (iv) Newton-Raphson.

46. **(p. 49, (b) — 2005 Regular Exam (EEE-251C))** Write down a program to solve the following equation by secant method.
   $$\cos x - xe^x = 0$$

47. **(p. 49, Q. 6(a) — 2005 Regular Exam (EEE-251C))** Using graphical representation, obtain the equation
   $$x_{k+1} = x_k - \frac{f_k}{f'_k}$$ for Newton-Raphson method.

48. **(p. 51, (c) — 2003 Semester Exam (EEE-251C))** **[figure Involved]** Consider the following system:
   Find the roots of the characteristic equation of the system by using Secant method.

   ![[attachments/fig_p51_c.png]]

49. **(p. 51, Q. 1(a) — 2003 Semester Exam (EEE-251C))** Write down the advantages and disadvantages of Newton-Raphson method over other methods.

50. **(p. 51, Q. 2(a) — 2003 Semester Exam (EEE-251C))** Given the equation: $x - e^{-x} = 0$. Determine the initial approximations. Use these to find the roots correct to two decimal places with the Secant method.

51. **(p. 54, (b) — 2002 Semester Exam (EEE251C, 2000 Series))** **[figure Involved]** An unity feedback control system is given below, find the roots of the characteristics equation by Newton-Raphson method and comments about the state system (i, e', stable, unstable or marginally stable).

   ![[attachments/fig_p54_b.png]]

52. **(p. 54, Q. 2(a) — 2002 Semester Exam (EEE251C, 2000 Series))** What is an iterative method? Describe the procedure of Newton-Raphson method to find the roots of a polynomial.

53. **(p. 54, Q. 4(a) — 2002 Semester Exam (EEE251C, 2000 Series))** Compare the rate of convergence and computational effort required in the following methods.
   (i) Bisection, (ii) False position, (iii) Secant and (iv) Newton-Raphson

54. **(p. 56, (b) — 2001 Regular Exam (EEE-251C))** Find the root of the following transcendental equation using Newton-Raphson method.
   $$x^2 + 4\cos x = 1$$

55. **(p. 56, (b) — 2001 Regular Exam (EEE-251C))** Write a computer program to solve the following equation using secant method.
   $$\cos x = 3x - 1$$

56. **(p. 57, (b) — 2001 Regular Exam (EEE-251C))** Write a computer program to solve the following equation using Newton's method
   $$e^{-x} - x = 0$$

57. **(p. 57, Q. 4(a) — 2001 Regular Exam (EEE-251C))** Compare the rate of convergence and computational effort required in the following methods.
   i. Bisection
   ii. False-Position
   iii. Secant and
   iv. Newton-Raphson.

58. **(p. 59, (b) — 2000 Regular Exam (EEE-251C, 98 Series))** Find a real root of the equation $\cos x = 3x - 1$
   Correct to $4$ decimal places using secant method

59. **(p. 59, Q. 2(a) — 2000 Regular Exam (EEE-251C, 98 Series))** Find the root of the following transcendental equation using Newton-Raphson method
   $$2x^2 + 3\sin x = 0$$

60. **(p. 60, (b) — 1999 Semester Exam (EEE-251C, 97 Series))** Find the root which lies between $1.4$ and $1.5$ of the following polynomial using Newton-Raphson method.
   $$x^6 - x^4 - x^3 - 1 = 0$$

61. **(p. 60, (c) — 1999 Semester Exam (EEE-251C, 97 Series))** Write a computer program to determine the roots of the equation $x^3 - x - 4 = 0$, correct to four decimal places using secant method

62. **(p. 62, (c) — 1998 Semester Exam (EEE 251C, 96... Series))** Find the real root of the following transcendental equation using Newton-Raphson method, correct to four decimal places.
   $$x^2 + 4\sin x = 0$$

63. **(p. 62, Q. 2(a) — 1998 Semester Exam (EEE 251C, 96... Series))** Derive Newton-Raphson formula for single equation

64. **(p. 67, 1. — Class test #1, EEE' 20 (A) (12/05/2024))** You are designing a spherical tank to hold water for a small village in a developing country. The volume of liquid it can hold can be computed as
   $$V = \pi h^2\left(\frac{3R - h}{3}\right)$$
   where $V =$ volume $[\text{m}^3]$, $h =$ depth of water in tank $[\text{m}]$, and $R =$ the tank radius $[\text{m}]$.
   (a) If $R = 3\text{ m}$, to what depth must the tank be filled so that it holds $30\text{ m}^3$? Use three iterations of the Newton-Raphson method to determine your answer. Determine the approximate relative error after each iteration.
   (b) Determine the approximate number of iterations if the problem above is to be sloved by bisection method, when the boundary is required to be narrowed from $5$ to $0.001$.

65. **(p. 67, 2. — Class test #1, EEE' 20 (A) (12/05/2024))** Comment under which conditions the Newton-Raphson may fail. How the Secant method is advantageous over Newton-Raphson method?

66. **(p. 70, 2. — Class test #1, EEE' 21 (A) (22/04/2025))** A series DC circuit consists of a DC source having source voltage $V_S$, a diode, and a resistor $R$. As the diode current (found from the Shockley's equation) is equal to the current through the resistor, the following equation is satisfied,
   $$f(V_D) = I_s\left(e^{\frac{V_D}{n V_T}} - 1\right) - \frac{V_S - V_D}{R} = 0$$
   Now, solve for the diode voltage $V_D$ using two iterations of Newton-Raphson method.
   Given, $I_s = 10^{-12}\text{ A},\ V_T = 25\text{ mV},\ n = 1,\ V_S = 5\text{ V},\ R = 5000\ \Omega$.
   *(Exact duplicate also on: p. 70, 2. [copy 2] (Class test #1, EEE' 21 (A) (22/04/2025) [duplicate copy on p. 70]))*

67. **(p. 70, 2. — Class Test (Blue Sheet, EEE 3109))** Graphically illustrate the limitations of Newton Raphson method

68. **(p. 70, 3. — Class Test (Blue Sheet, EEE 3109))** (a) Apply the Newton-Raphson method to the function $f(x) = \tanh(x^2 - 9)$ to evaluate its known real root at $x = 3$. Use an initial guess of $x_0 = 3.2$ and take a minimum of four iterations..
   (b) Did the method exhibit convergence onto its real root?

### **Multiple Roots & Systems of Non-Linear Equations**

69. **(p. 11, (b) — Topic 3: Open Methods (Series 21))** In a simple series circuit containing a DC voltage source $V_S$, a resistor $R$ and a diode with non-linear I-V characteristics, two modeling equations are found.
   One is the Shockley's equation for diode current-
   $$I = I_s\left(e^{\frac{V_D}{n V_T}} - 1\right)$$
   Here, $I_s$ is the reverse saturation current of the diode, $V_D$ is the voltage across the diode, $V_T$ is the thermal voltage.
   Another equation is the KVL for the circuit -
   $$V_s = I R + V_D$$
   Now develop a framework for solving this system of two equation using Newton-Rapson method.

70. **(p. 11, (c) — Topic 3: Open Methods (Series 21))** Solve the system of two equations for $I$ and $V_D$ in Q.1(b) according to the developed frame-work of Newton-Raphson method. Show two iteration with a logically small step size. The parameters are given as - $V_S = 10\text{ V}$, $R = 1\text{ k}\Omega$, $I_S = 20\text{ nA}$, $n = 1$, and $V_T = 26\text{ mV}$. Use $V_D = 0.7\text{ V}$ and $I = 9.3\text{ mA}$ as the initial guess.

71. **(p. 12, (b) [2nd] — Topic 3: Open Methods (Series 19))** Solve the following systems of nonlinear equations using Newton-Raphson (NR) iterative method, with initial estimate $(0, 1, 1)$. Perform 3 iterations.
   $$xy - \cos x + z^2 = 3.6$$
   $$x^2 - 2y^2 + z = 2.8$$
   $$3x + y \sin z = 2.8$$

72. **(p. 12, (c) [3rd] — Topic 3: Open Methods (Series 21))** Use the multiple-equation Newton-Raphson method to determine roots of the following system of nonlinear equations.
   $$u(x, y) = x^2 + xy - 10 = 0$$
   $$v(x, y) = y + 3xy^2 - 57 = 0$$
   Note that, a correct pair of roots is $x = 2$ and $y = 3$. Initiate the computation with guesses of $x = 1.5$ and $y = 3.5$. Perform only one iteration.

73. **(p. 29, (b) — 2022 Odd Semester (EEE 3109))** Solve the following systems of nonlinear equations using Newton-Raphson (NR) iterative method, with initial estimate $(0, 1, 1)$. Perform $3$ iterations.
   $$xy - \cos x + z^2 = 3.6$$
   $$x^2 - 2y^2 + z = 2.8$$
   $$3x + y\sin z = 2.8$$

74. **(p. 30, Q. 2(a) — 2020 Odd Semester (EEE 3109))** Discuss at least three difficulties for many numerical methods to find a root of a nonlinear function which contains multiple roots.
   Hint: A multiple root corresponds to a point where a function is tangent to the x-axis.
   *(Exact duplicate also on: p. 12, Q.2 (a) (Topic 3: Open Methods (Series 17)))*

75. **(p. 40, (b) — Semester Exam (EEE 3109, Pre-2016))** Starting with the initial values $x_1 = 0.5$ and $x_2 = -1$, solve the following system of equations using Newton-Raphson method. Fill the following table for two iterations:
   $$x_1^2 + x_2^2 = 4$$
   $$e^{x_1} + x_2 = 1$$

   | Iteration | $\Delta C$ | $J$ | $\Delta x$ | $x$ |
   | --- | --- | --- | --- | --- |
   | 01 | | | | |
   | 02 | | | | |

76. **(p. 42, (b) — 2008 Semester Exam (EEE 251))** Determine the roots of the simultaneous nonlinear equations
   $$y = x^2 + 1$$
   $$y = 3\cos x$$

77. **(p. 46, Q. 7(a) — 2007 Regular Exam (EEE-251))** Write a computer program to solve the following nonlinear set of equations using Gauss-Seidal method.
   $$2x_1 + x_1 x_2 - 1 = 0\quad\text{and}\quad 2x_2 - x_1 x_2 + 1 = 0$$
   Initial values are: $x_1 = 0$ and $x_2 = 0$

78. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** Solve the following equations using Gauss-Seidal method. Consider $x_0 = 1$ and $y_0 = 1$.
   $$y = \sin(x + y),\quad x = \cos(y - x).$$

79. **(p. 47, Q. 6(a) — 2006 Semester Exam (EEE 251))** Write a computer program to solve the following equations using Newton-Raphson method.
   $$x^2 + y^2 = 4,\quad xy = 1.$$

80. **(p. 50, Q. 7(a) — 2005 Regular Exam (EEE-251C))** Solve the following system of equations by any iterative method.
   $$x^2 + y^2 = 1.12$$
   $$xy = 0.23$$

81. **(p. 55, (b) — 2002 Semester Exam (EEE251C, 2000 Series))** Solve the simultaneous non-linear equations
   $$x^2 + y^2 = 4$$
   $$xy = 1$$
   Using Newton-Raphson method with initial values $x_0 = 2,\ y_0 = 0$.

82. **(p. 56, Q. 2(a) — 2001 Regular Exam (EEE-251C))** The system of equations
   $$y\cos(xy) + 1 = 0$$
   $$\sin(xy) + x - y = 0$$
   Has one solution close to $x = 1,\ y = 2$. Calculate this solution correct to $2$ decimal places.
   Use Gauss's method.

83. **(p. 57, (b) — 2001 Regular Exam (EEE-251C))** Solve the simultaneous nonlinear equations:
   $$x^2 + y^2 = 4$$
   $$xy = 1$$
   Using Newton-Raphson method. Use the starting values $X_0 = 2,\ Y_0 = 0$.

84. **(p. 57, Q. 3(a) — 2001 Regular Exam (EEE-251C))** Solve the following equations using Gauss-Seidal method. Show the result after $5^{\text{th}}$ iteration
   $$2x_1 + x_1 x_2 - 1 = 0$$
   $$2x_2 - x_1 x_2 + 1 = 0$$
   Consider $X_1(1) = 0;\ X_2(1) = 0$

85. **(p. 60, Q. 2(a) — 1999 Semester Exam (EEE-251C, 97 Series))** Solve the following equations using Gauss-Seidal method.
   $$2x_1 + x_1 x_2 - 1 = 0$$
   $$2x_2 - x_1 x_2 + 1 = 0$$

86. **(p. 62, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** Write a computer program to find the real roots of the equations $x^2 - y^2 = 4$ and $x^2 + y^2 = 16$, using Newton-Raphson method

87. **(p. 70, 1. — Class test #1, EEE' 21 (A) (22/04/2025))** Outline the steps to solve system of nonlinear equations using Newton-Raphson method.
   *(Exact duplicate also on: p. 70, 1. [copy 2] (Class test #1, EEE' 21 (A) (22/04/2025) [duplicate copy on p. 70]))*

### **Roots of Polynomials (Muller's & Bairstow's Method)**

88. **(p. 49, (c) — 2005 Regular Exam (EEE-251C))** How will you calculate $b_i$'s and $c_i$'s for Bairstow's method to find a quadratic factor from a polynomial equation, (where $b_i$'s and $c_i$'s indicate their usual meanings). Extract a quadratic factor from-
   $$x^4 + x^3 + 2x^2 + x + 1 = 0$$
