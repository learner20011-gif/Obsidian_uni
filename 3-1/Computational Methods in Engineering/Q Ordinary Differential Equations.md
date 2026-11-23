# EEE 3109 — Ordinary Differential Equations (PYQ)

**Syllabus:** Euler's method and Runge-Kutta methods, Eigen value problems, System of ordinary differential equations.

---

### **Euler's & Modified Euler's / Heun's Methods**

1. **(p. 4, (25) — Theory Questions EEE 3109)** When Euler method is said to be stable to some [solve] a different [differential] equation? Write the algorithm of Euler method.

2. **(p. 7, (40) — Theory Questions EEE 3109)** Algorithm to solve a DE using Euler method.

3. **(p. 8, (51) — Theory Questions EEE 3109)** Show that in Euler's method the error due to truncation is of order of $h^2$.

4. **(p. 22, (b) — Topic 8: Ordinary Differential Equations (Series 21))** The capacitor voltage in a buck converter follows $\frac{dv}{dt} = \frac{1}{RC}(V_{in} - V)$. Use Heum's method to estimate $V(0.01)$ for a $5\text{V}$ input and any known value of $R, C$. Compare the result with the analytical solution:
   $$v(t) = V_{in}(1 - e^{-t/RC})$$

5. **(p. 22, Q.7. (a) — Topic 8: Ordinary Differential Equations (Series 21))** Why Euler's method is the most inaccurate method for solving ODE? How Heun's method is better than Euler's method.

6. **(p. 23, (b) — Topic 8: Ordinary Differential Equations (Series 18))** Find the value of current after $2$ seconds for the equation $L\frac{di}{dt} + iR = V$, $I = 0$ when $t = 0$ where resistance $R = 20\ \Omega$, inductance $L = 50\text{ H}$ and voltage $V = 240\text{ V}$.

7. **(p. 27, Q. 7(a) — 2023 Odd Semester (EEE 3109))** Why does Euler's method pose a larger amount of error than the other methods for solving ordinary differential equations?
   *(Exact duplicate also on: p. 22, Q. 7(a) (Topic 8: Ordinary Differential Equations (Series 20)))*

8. **(p. 31, Q. 8(a) — 2020 Odd Semester (EEE 3109))** When is Euler method said to be stable to solve a differential equation?
   *(Exact duplicate also on: p. 23, Q.8 (a) (Topic 8: Ordinary Differential Equations (Series 17)))*

9. **(p. 34, Q. 8(a) — 2018 Odd Semester (EEE 3109))** Write a computer algorithm to solve a differential equation using Euler method.
   *(Exact duplicate also on: p. 23, Q.8. (a) (Topic 8: Ordinary Differential Equations (Series 15)))*

10. **(p. 38, (c) — 2016 Odd Semester (EEE 3109))** Show that, in Euler's method the errors due to truncation is of order of $h^2$.

11. **(p. 38, Q. 7(a) — 2016 Odd Semester (EEE 3109))** Graphically explain predictor-corrector method with all figures and equations.

12. **(p. 41, (b) — Semester Exam (EEE 3109, Pre-2016))** What is meant by solution of differential equation? What is the limitation of Euler's method to solve differential equation? How can this problem be minimized? What does the order of Runge-Kutta method signify?

13. **(p. 43, Q. 8(a) — 2008 Semester Exam (EEE 251))** Using Euler's method, solve the following differential equation.
   $$\frac{dy}{dx} - 1 = y^2,\ y(0) = 0.$$

14. **(p. 47, Q. 3(a) — 2006 Semester Exam (EEE 251))** What do you understand by initial value and boundary value problems? Use modified Euler's method to solve numerically the initial value problem $\frac{dy}{dx} + 2xy^2 = 0,\ y(0) = 1$, to find the value of $y$ at $x = 0.2, x = 0.4$.

15. **(p. 64, Q. 8(a) — 1998 Semester Exam (EEE 251C, 96... Series))** 'Why is it necessary to modify the Euler's method for solving differential equation?' Derive modified Euler formula

### **Runge-Kutta Methods**

16. **(p. 22, (c) — Topic 8: Ordinary Differential Equations (Series 21))** The dynamics of the moving coil of a PMMC instrument is expressed with the following $2^{\text{nd}}$ order ODE:
   $$J\frac{d^2\theta(t)}{dt^2} + b\frac{d\theta(t)}{dt} + k\theta(t) = KI(t)$$
   If $J = 0.01\text{ kgm}^2$, $b = 0.1\text{ Nm}$, $k = 1\text{Nm}$, $K = 0.5\text{ Nm/A}$, and the applied current $I(t)$ is a step input $I(t) = 2\text{A}$ for $t > 0$, Solve the ODE from $0$ to $0.2\text{ sec.}$ with a step size of $0.1$ using Runge-Kutta $4^{\text{th}}$ order method. Use initial conditions:
   $$\theta(0) = 0\text{ rad},\ \frac{d\theta(0)}{dt} = 0\text{ rad/sec}.$$

17. **(p. 23, (a) — Topic 8: Ordinary Differential Equations (Series 18))** Given that $y'' - xy' + 4y = 0$, where $y(0) = 3,\ y'(0) = 0$. Compute $y(0.2)$ using fourth order RK method.

18. **(p. 27, (b) — 2023 Odd Semester (EEE 3109))** Show that in second order Runge-Kutta formula, the error is of order $h^3$.
   *(Exact duplicate also on: p. 22, (b) (Topic 8: Ordinary Differential Equations (Series 20)))*

19. **(p. 27, (c) — 2023 Odd Semester (EEE 3109))** **[figure Involved]** When the switch in the circuit below is closed at $t = 0$, the voltage across the capacitor is $1\text{ V}$. Calculate $V_c$ at $t = 0.1$ and $0.2$ using $4^{\text{th}}$ order Runge-Kutta method. Also, find the true error in each case from the analytical result. Let, $h = 0.1$.
   *(Exact duplicate also on: p. 22, (c) (Topic 8: Ordinary Differential Equations (Series 20)))*

   ![[attachments/fig_p27_c.png]]

20. **(p. 29, (c) — 2022 Odd Semester (EEE 3109))** Find the value of $y$ at $x = 0.2$ using Runge-Kutta fourth-order formula for the following equation:
   $$\frac{dy}{dx} = y - x,\ y(0) = 2;\text{ Use a step size of } 0.10.$$
   *(Exact duplicate also on: p. 23, (c) (Topic 8: Ordinary Differential Equations (Series 19)))*

21. **(p. 31, (c) — 2020 Odd Semester (EEE 3109))** Consider a colony of bacteria growing in an environment with limited resource. For example, there may be a scarcity of food, or space constraints on the size of the colony. In this case, it is not reasonable to expect the colony to grow exponentially: indeed, the colony will unable to grow larger than some maximum population $P_{\max}$. In this case, a common model for the growth of the colony is the logistic equation,
   $$\frac{dP}{dt} = kP\left(1 - \frac{P}{P_{\max}}\right)$$
   Let $P_{\max} = 1000000$ and $k = 2.5$ and $P_0 = 35646$. Find the population at $t = 7$ minutes numerically using Euler's modified method and fourth order Runge-Kutta method.
   *(Exact duplicate also on: p. 23, (c) (Topic 8: Ordinary Differential Equations (Series 17)))*

22. **(p. 34, (b) — 2018 Odd Semester (EEE 3109))** **[figure Involved]** When the switch in the following circuit is closed at $t = 0$, there is no current through the inductor. Determine the current flowing through the circuit as a function of time using $2^{\text{nd}}$ order Runge-Kutta method.
   *(Exact duplicate also on: p. 23, (b) (Topic 8: Ordinary Differential Equations (Series 15)))*

   ![[attachments/fig_p34_b.png]]

23. **(p. 35, (b) — 2017 Odd Semester (EEE 3109))** Show that, in $2^{\text{nd}}$ order Runge-Kutta formula the error is of order $h^3$.

24. **(p. 35, (c) — 2017 Odd Semester (EEE 3109))** **[figure Involved]** When the switch in the circuit below is closed at $t = 0$, the voltage across the capacitor is $1\text{ V}$. Calculate $V_c$ at $t = 0.1$ and $0.2$ using $4^{\text{th}}$ order Runge-Kutta method. Also find the true error in each case from the analytical result. Let, $h = 0.1$.

   ![[attachments/fig_p36_c.png]]

25. **(p. 40, Q. 3(a) — Semester Exam (EEE 3109, Pre-2016))** **[figure Involved]** When the switch in the circuit shown below is closed at $t = 0$, there is no current through the inductor. Determine the current flowing through the circuit as a function of time using $2^{\text{nd}}$ order Runge-Kutta method.

   ![[attachments/fig_p40_q_3_a.png]]

26. **(p. 44, (b) — 2008 Semester Exam (EEE 251))** **[figure Involved]** Obtain the differential equation to determine the current $i$ of the following circuit and write a computer program to solve the differential equation using Fourth or higher order Runge-Kutta method.

   ![[attachments/fig_p44_b.png]]

27. **(p. 46, (b) — 2007 Regular Exam (EEE-251))** **[figure Involved]** For the following circuit use an appropriate numerical method to determine how the current varies with time between $0$ and $0.2$ second. Use $h = 0.1$

   ![[attachments/fig_p46_b.png]]

28. **(p. 46, (c) — 2007 Regular Exam (EEE-251))** **[figure Involved]** For the following circuit calculate $V_c$ at $t = 0.1$ and $0.2$ using Runge-Kutta Fourth order method. Find the true error in each case from the analytical result

   ![[attachments/fig_p46_c.png]]

29. **(p. 46, Q. 5(a) — 2007 Regular Exam (EEE-251))** Solve the following first order equation $\frac{dy}{dx} = x^2 + y^2$ by Runge-Kutta ($4^{\text{th}}$ order) method with the initial condition $x = 0, y = 1$. Compute the first three lines of a tabular solution taking $h = 0.1$.

30. **(p. 47, Q. 7(a) — 2006 Semester Exam (EEE 251))** **[figure Involved]** When the switch in the circuit shown bellow is closed at $t = 0$, there is no voltage across the capacitor. Determine voltage across the capacitor and current through the circuit as a function of time using second order Runge-Kutta method.

   ![[attachments/fig_p47_q_7_a.png]]

31. **(p. 49, Q. 3(a) — 2005 Regular Exam (EEE-251C))** **[figure Involved]** When the switch in the circuit shown below is closed at $t = 0$, there is no voltage across the capacitor. Determine voltage across the capacitor and current through the circuit as a function of time by using any of the Runge-Kutta method.

   ![[attachments/fig_p49_q_3_a.png]]

32. **(p. 55, (b) — 2002 Semester Exam (EEE251C, 2000 Series))** **[figure Involved]** When the switch in the circuit shown below is closed at $t = 0$. There is no voltage across the capacitor. Determine voltage across the capacitor and current through the circuit as a function of time, by forth order Runge-Kutta method.

   ![[attachments/fig_p55_b.png]]

33. **(p. 55, Q. 6(a) — 2002 Semester Exam (EEE251C, 2000 Series))** Describe the fourth order Runge-Kutta method for solving differential equations.

34. **(p. 56, (b) — 2002 Semester Exam (EEE251C, 2000 Series))** **[figure Involved]** Write a computer program to determine the current through an R-L-C series circuit shown below if voltage is suddenly brought to $15\text{ V}$ and maintained steadily. Use an appropriate numerical method to determine how the current varies with time between $0$ and $0.2$ second if $C = 100\ \mu\text{F}$, $L = 50\text{ mH}$ and $R = 4.7\ \Omega$. If the calculations are repeated but with the resistance value increased, the oscillation will damped out more quickly; at what condition the oscillation should disappear.

   ![[attachments/fig_p56_b.png]]

35. **(p. 58, Q. 8(a) — 2001 Regular Exam (EEE-251C))** Solve the initial value problem
   $$u' = -2tu^2,\quad u(0) = 1$$
   with $h = 0.2$ on the interval $[0, 1]$. Use the fourth order classical Runge-Kutta method.

36. **(p. 59, (b) — 2000 Regular Exam (EEE-251C, 98 Series))** Write a computer program to solve the following initial value problem using Runge-Kutta $4^{\text{th}}$ order method.
   $$u' = t^2 + u^2,\quad u(0) = 0$$
   $$h = 0.1\quad\text{and}\quad t_1 = 5$$

37. **(p. 59, Q. 3(a) — 2000 Regular Exam (EEE-251C, 98 Series))** Discuss the advantages of Runge-Kutta method over predictor corrector method in solving differential equations.

38. **(p. 61, Q. 4(a) — 1999 Semester Exam (EEE-251C, 97 Series))** Derive the equation for the Runge-Kutta fourth order method of numerical solution of differential equations. Discuss its usefulness over other methods.

39. **(p. 64, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** Write a computer program to solve the differential equation $dy/dx = 1 + y^2$, $y = 0$ when $x = 0$ using Runge-kutta fourth order formula. Show the result in the display window

40. **(p. 64, Q. 7(a) — 1998 Semester Exam (EEE 251C, 96... Series))** Describe the Runge-Kutta fourth order method of numerical solution of differential equations. Why is it superior to other methods?

### **Systems of ODEs & Boundary-Value / Eigenvalue Problems**

41. **(p. 22, (b) [non-insulated rod] — Topic 8: Ordinary Differential Equations (Series 21))** A $10\text{ m}$ long non-insulated rod has a temperature distribution described by the following differential equation:
   $$\frac{d^2T}{dx^2} + h(T_a - T) = 0$$
   Given, $T(0) = 40$, $T(10) = 200$, $T_a = 20$, $h = 0.01$. Now, determine the temperature at four interior nodes with a segment length of $\Delta x = 2\text{ m}$ using finite difference method.

42. **(p. 23, Q.8. (a) — Topic 8: Ordinary Differential Equations (Series 19))** A boundary-value problem is defined by
   $$\frac{d^2i}{dt^2} + \frac{1}{RC}\frac{di}{dt} + \frac{i}{LC} = \frac{I_s}{LC},\ 0 \le t \le 2\text{ sec}\text{ with } i(0) = 0\text{ A}\text{ and } i(2) = 5\text{ A}.\text{ Given, } L = 1\text{ H},$$
   $C = 1\text{ F}$, and $R = 1\Omega$, and $I_s = 10\text{ A}$. With $h = 0.5$, use the finite-difference method to determine the value of $i(t)$ at $t = 1.5\text{ sec}$.

43. **(p. 27, Q. 8(a) — 2023 Odd Semester (EEE 3109))** A boundary value problem is defined by $\frac{d^2i}{dt^2} + \frac{1}{RC}\frac{di}{dt} + \frac{i}{LC} = \frac{I_s}{LC}$, $0 \le t \le 2\text{ sec}$ with $i(0) = 0\text{ A}$ and $i(2) = 5\text{ A}$. Given, $L = 1\text{ H}$, $C = 1\text{ F}$ and $R = 1\ \Omega$ and $I_s = 10\text{ A}$. With $h = 0.5$, use finite deference method to determine the value of $i(t)$ at $t = 1.5\text{ sec}$.
   *(Exact duplicate also on: p. 23, Q. 8(a) (Topic 8: Ordinary Differential Equations (Series 20)))*

44. **(p. 29, Q. 8(a) — 2022 Odd Semester (EEE 3109))** A boundary-value problem is defined by
   $$\frac{d^2i}{dt^2} + \frac{1}{RC}\frac{di}{dt} + \frac{i}{LC} = \frac{I_s}{LC},\ 0 \le t \le 2\text{ sec}\text{ with } i(0) = 0\text{ A}\text{ and } i(2) = 5\text{ A}.\text{ Given, } L = 1\text{ H},$$
   $C = 1\text{ F}$, and $R = 1\ \Omega$, and $I_s = 10\text{ A}$. With $h = 0.5$, use the finite-difference method to determine the value of $i(t)$ at $t = 1.5\text{ sec}$.

45. **(p. 38, (b) — 2016 Odd Semester (EEE 3109))** Solve $\frac{d^2y}{dx^2} + 2\frac{dy}{dx} + y = 0$;
   $$y(0) = 0,\ \frac{dy}{dx}(0) = 1.$$
   Evaluate the values of $y$ up to $0.1$ in steps of $0.05$.

46. **(p. 41, Q. 7(a) — Semester Exam (EEE 3109, Pre-2016))** Write a computer program to solve the system of equations
   $$u' = -3u + 2v,\ u(0) = 0$$
   $$v' = 3u - 4v,\ v(0) = \frac{1}{2}$$
   with $h = 0.2$ on the interval $[0, 1]$.

47. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** Write a computer program to solve the following equation
   $$\frac{d^3y}{dt^3} - 2\frac{d^2y}{dt^2} + (1 - y^2)t\frac{dy}{dt} + t^2 y = 0$$

48. **(p. 49, (b) — 2005 Regular Exam (EEE-251C))** Solve the following differential equation using any numerical method.
   $$\ddot{y} + 2\dot{y} + y = 0;\quad y(0) = 0,\ \dot{y}(0) = 1$$

49. **(p. 52, (b) — 2003 Semester Exam (EEE-251C))** Solve the system of equation
   $$u' = -3u + 2v,\quad u(0) = 0$$
   $$v' = 3u - 4v,\quad v(0) = 1/2$$
   with $h = 0.2$ on the interval $[0, 1]$. Use the modified Euler's method.

50. **(p. 52, Q. 8(a) — 2003 Semester Exam (EEE-251C))** Write a computer program to solve the following differential equation
   $$\ddot{x} = 3\dot{x} + 4(x^2 - 1) + 5x\quad\text{given, } \dot{x}(0) = 0\text{ and } x(0) = 1.$$

51. **(p. 60, (b) — 2000 Regular Exam (EEE-251C, 98 Series))** Discuss how higher order differential equations can be solved by numerical method.

52. **(p. 60, Q. 8(a) — 2000 Regular Exam (EEE-251C, 98 Series))** Solve the following simultaneous differential equation for $x = 0$ to $x = 0.5$
   $$dy/dx = x^2 - yz,\quad dz/dx = y - z^2$$
   $$Y(0) = 0,\ Z(0) = 1.0$$

53. **(p. 61, (b) — 1999 Semester Exam (EEE-251C, 97 Series))** Write a computer program to solve the following Vander Pol equation
   $$\ddot{x} + (1 - x^2)\dot{x} + x = 0$$

54. **(p. 64, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** Solve the following differential equation by any suitable numerical technique
   $d^2y/dx^2 + 2dy/dx + 3y = 0$, initial values are $y(0) = 1,\ dy/dx(0) = 1$. Solution is required between $x = 0$ to $x = 5$ at a step of $h = 1$. Obtain an equation of $y$ as a function of $x$ by using numerical solution obtained above
