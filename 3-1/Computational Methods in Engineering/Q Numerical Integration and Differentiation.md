# EEE 3109 — Numerical Integration and Differentiation (PYQ)

**Syllabus:** Newton methods, Trapezoidal method, Simpson's methods, Romberg integration, Double integration, Boole's method.

---

### **Numerical Differentiation (Finite Differences & Richardson Extrapolation)**

1. **(p. 20, (c) — Topic 7: Numerical Integration & Differentiation (Series 18))** The distance travelled by an electron inside a conductor in different times are given below

   | $t$ | 0.00 | 0.10 | 0.20 | 0.30 | 0.40 | 0.50 | 0.60 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $x$ | 2.01 | 2.19 | 2.29 | 2.39 | 2.45 | 3.38 | 3.31 |

   Find out the acceleration of the electron at $t = 0.25\text{ s}$ using a suitable Newton difference method.

2. **(p. 21, (c) — Topic 7: Numerical Integration & Differentiation (Series 18))** Why are numerical differentiation and integration used for solving electrical engineering problem?
   *(Exact duplicate also on: p. 3, (10) (Theory Questions EEE 3109))*

3. **(p. 26, (b) — 2023 Odd Semester (EEE 3109))** State the formulas for forward, backward, and centered divided differences for the first derivative and analyze which one of them offers the least amount of error for the same step size.
   *(Exact duplicate also on: p. 20, (b) (Topic 7: Numerical Integration & Differentiation (Series 20)))*

4. **(p. 29, (c) — 2022 Odd Semester (EEE 3109))** **[figure Involved]** The switch of the following circuit is closed at $t = 0$. After closing the switch, recorded voltages across the capacitor for different times are tabulated as follows:

   | $t$: sec | 0 | 2 | 4 | 6 | 8 | 10 | 12 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $v_c(t)$: volt | 0 | 10 | 20 | 35 | 50 | 65 | 50 |

   Find the source voltage at $t = 10\text{ sec}$.
   *(Exact duplicate also on: p. 20, (c) (Topic 7: Numerical Integration & Differentiation (Series 19)))*

   ![[attachments/fig_p29_c.png]]

5. **(p. 31, (b) — 2020 Odd Semester (EEE 3109))** **[figure Involved]** The switch in the following circuit is closed at $t = 0$. After closing the switch, recorder currents for different times are tabulated as follows:

   | $t\text{(sec)}$ | 0 | 2 | 4 | 6 | 8 |
   | --- | --- | --- | --- | --- | --- |
   | $I\text{(Amp)}$ | 0 | 0.632 | 0.864 | 0.992 | 0.174 |

   Obtain the source voltage at time $t = 2\text{ sec}$ using suitable numerical method.
   *(Exact duplicate also on: p. 21, (b) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

   ![[attachments/fig_p31_b.png]]

6. **(p. 31, (c) — 2020 Odd Semester (EEE 3109))** The input of a differentiator circuit is given by $g(x) = x^3 + 3x$. Calculate the output at $x = 2$ for $h = 0.1$ by using forward and central difference quotient and compare the results.
   *(Exact duplicate also on: p. 21, (c) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

7. **(p. 31, (d) — 2020 Odd Semester (EEE 3109))** Current $i_L$ through an inductor is tabulated as follows:

   | $\omega t$ | 0.25 | 0.26 | 0.27 | 0.28 | 0.29 |
   | --- | --- | --- | --- | --- | --- |
   | $i_L$ | 0.2474 | 0.2571 | 0.2667 | 0.2764 | 0.2860 |

   Find the voltage across the inductor using a numerical Simpson's 1/3 technique. Assume $1\text{ mH}$ inductance.
   *(Exact duplicate also on: p. 21, (d) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

8. **(p. 31, Q. 6(a) — 2020 Odd Semester (EEE 3109))** How to obtain the numerical differentiation from interpolation formula?
   *(Exact duplicate also on: p. 21, Q.6 (a) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

9. **(p. 33, Q. 7(a) — 2018 Odd Semester (EEE 3109))** How does the numerical differentiation obtain from interpolation formula? Explain.
   *(Exact duplicate also on: p. 21, Q.7. (a) (Topic 7: Numerical Integration & Differentiation (Series 15)); p. 7, (38) (Theory Questions EEE 3109))*

10. **(p. 35, (b) — 2017 Odd Semester (EEE 3109))** Write down six numerical differentiation formula.

11. **(p. 35, (c) — 2017 Odd Semester (EEE 3109))** **[figure Involved]** The switch in the following circuit is closed at $t = 0$. After closing the switch, recorded currents for different times are tabulated as follows:

   | $t\text{(sec)}$ | 0 | 1 | 2 | 3 | 4 |
   | --- | --- | --- | --- | --- | --- |
   | $I\text{(amp)}$ | 0 | 0.391 | 0.632 | 0.776 | 0.864 |

   Obtain the source voltage at time $t = 2$ second using numerical method.

   ![[attachments/fig_p35_c_4.png]]

12. **(p. 35, Q. 5(a) — 2017 Odd Semester (EEE 3109))** Derive a second derivative formula for numerical differentiation.

13. **(p. 35, Q. 7(a) — 2017 Odd Semester (EEE 3109))** Prove that, central difference approach to approximate the first derivative of a function has better result than both forward and backward difference approaches.

14. **(p. 38, (b) — 2016 Odd Semester (EEE 3109))** How to obtain numerical differentiation from interpolation formula? The distances travelled by a rocket at different times are-

   | $t$ | 0 | 1 | 2 | 3 | 4 | 5 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $s$ | 0 | 3 | 7 | 15 | 38 | 50 |

   Estimate the rocket's velocity and acceleration at $t = 3\text{ sec}$.

15. **(p. 40, Q. 4(a) — Semester Exam (EEE 3109, Pre-2016))** A jet fighter's position on an aircraft carrier's runway was timed during landing:

   | $t$, sec | 0 | 0.52 | 1.04 | 1.75 | 2.37 | 3.25 | 3.83 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $x$, meter | 153 | 185 | 210 | 249 | 261 | 271 | 273 |

   where $x$ is the distance from the end of the carrier Estimate velocity and acceleration using numerical differentiation.

16. **(p. 42, Q. 4(a) — 2008 Semester Exam (EEE 251))** A plane is being tracked by a radar and data is taken every second in polar co-ordinates $\theta$ and $r$.

   | $t\text{(sec)}$ | 101 | 102 | 103 | 104 | 105 | 106 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $\theta\text{(rad)}$ | 0.72 | 0.70 | 0.68 | 0.67 | 0.66 | 0.65 |
   | $r\text{(ft)}$ | 5370 | 5560 | 5800 | 6030 | 6240 | 6350 |

   At $103$ seconds, use the centered finite difference to find $v$ and $a$ given by
   $$\vec{v} = \dot{r}\hat{a}_r + r\dot{\theta}\hat{a}_\theta$$
   $$a = (\ddot{r} - r\dot{\theta}^2)\hat{a}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{a}_\theta$$

17. **(p. 43, (b) — 2008 Semester Exam (EEE 251))** Use forward and backward different approximations of $O(h)$ and a centered difference method of $O(h^2)$ to estimate the first derivative of
   $$f(x) = -0.1x^4 - 0.1x^3 - 0.5x^2 - 0.2x + 1.2$$
   at $x = 0.5$ using $h = 0.5$. Repeat computation using $h = 0.25$. Comment on the result. Compare the result with true derivative.

18. **(p. 46, (b) — 2007 Regular Exam (EEE-251))** Estimate the first derivative of
   $f(x) = -0.1x^4 - 0.15x^3 - 0.5x^2 - 0.25x + 1.2$ at $x = 0.5$ using a step size of $h = 0.5$. Use forward, backward, and centered approximations of order $O(h)$, $O(h)$ and $O(h^2)$ respectively. Calculate true error and show how this error can be minimized when we halve the step size.

19. **(p. 46, (c) — 2007 Regular Exam (EEE-251))** Faradays law characterizes the voltage drop across an inductor as $V_L = L\frac{di}{dt}$.
   Determine the voltage drop as a function of time from the following data for an inductance of $4\text{ H}$.

   | $T$ (sec) | 0 | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $I$ (am0) | 0 | 0.15 | 0.3 | 0.55 | 0.8 | 1.9 |

20. **(p. 46, Q. 6(a) — 2007 Regular Exam (EEE-251))** Use Taylors series to develop forward, backward and centered divided difference approaches to approximate the first derivative of a function. Among them which one is the best and why ?

21. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** Discuss the forward, backward and central difference method approximating the derivative. Use the most accurate method among these to estimate $f'(1.2)$ where $f(x) = \sin(\sqrt{x}) - x$, using step size of $h = 0.2$.

22. **(p. 48, (b) — 2005 Regular Exam (EEE-251C))** From the following table of values, obtain $dV/dt$ for $t = 2.3$, using a numerical method.-

   | $t$ | 1.0 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.2 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $V$ | 2.7183 | 3.3201 | 4.0552 | 4.9530 | 6.0496 | 7.3891 | 9.0250 |

23. **(p. 52, (b) — 2003 Semester Exam (EEE-251C))** From the following experimental data's determine $\frac{d^2i}{dt^2}$, and $\frac{di}{dt}$, $t$ for $t = 1.2$

   | $t$ | 1 | 1.2 | 1.4 | 1.6 | 1.8 | 2.0 | 2.2 | 2.4 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $i(t)$ | 2.5 | 3.3 | 4.2 | 5.3 | 6.2 | 7.3 | 8.6 | 9.5 |

24. **(p. 52, Q. 7(a) — 2003 Semester Exam (EEE-251C))** What are the limitations of numerical differentiation?

25. **(p. 58, (c) — 2001 Regular Exam (EEE-251C))** Differential the following function over a range of $x = 0$ to $x = 10$ by applying any numerical technique. Choose an appropriate step length $h$.
   $$y = 4x^3 - 2x^2 + 5x + 9$$

26. **(p. 64, Q. 6(a) — 1998 Semester Exam (EEE 251C, 96... Series))** Derive Newton's forward difference formula of numerical differentiation. What are the limitations of numerical differentiation?

### **Trapezoidal, Simpson's & Boole's Rules (Newton-Cotes)**

27. **(p. 4, (23) — Theory Questions EEE 3109)** Prove that total error of the trapezoidal integration formula is $E = \frac{-(b-a)}{12} h^2 y''(\bar{x})$;

28. **(p. 7, (39) — Theory Questions EEE 3109)** Deduce Weddle's rule $\int_{x_0}^{x_6} y\,dx = \frac{3h}{10}(y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6)$

29. **(p. 8, (57) — Theory Questions EEE 3109)** Deduce the expression of composite Simpson's $1/3$ rd rule for numerical integration.

30. **(p. 18, Q.4. (a) — Topic 7: Numerical Integration & Differentiation (Series 21))** The function $f(x) = 2e^{-1.5x}$ can be used to generate the following table of data;

   | $x$ | 0 | 0.05 | 0.15 | 0.25 | 0.35 | 0.475 | 0.6 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 2 | 1.8555 | 1.5970 | 1.3746 | 1.1831 | 0.9808 | 0.8131 |

   Evaluate the integral from $a = 0$ to $b = 0.6$ using (i) the trapezoidal and (ii) Simpson's rules; employ Simpson's rule wherever possible to obtain the highest accuracy.

31. **(p. 19, (c) — Topic 7: Numerical Integration & Differentiation (Series 21))** A control engineer applies Simpson's 1/3 rule on irregularly spaced data and gets incorrect results. Expalin why this happens and how the integration should be handled.

32. **(p. 19, Q. 4(a) — Topic 7: Numerical Integration & Differentiation (Series 20))** Will the accuracy of numerical integration by the trapezoidal method keep increasing if the step size keeps decreasing? Provide reasoning in favor of your answer.

33. **(p. 20, (b) — Topic 7: Numerical Integration & Differentiation (Series 18))** Graphically explain the Simpson's $1/3$ rule. Also deduce its mathematical expression.
   *(Exact duplicate also on: p. 2, (8) (Theory Questions EEE 3109))*

34. **(p. 20, (c) [car speed] — Topic 7: Numerical Integration & Differentiation (Series 18))** The table below shows the speed of a car at various intervals of time. Find the distance travelled by the car at the end of 2 hours.

   | Time (hr) | 0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 |
   | --- | --- | --- | --- | --- | --- | --- |
   | Speed (kM/hr) | 0 | 40 | 60 | 50 | 45 | 65 |

35. **(p. 21, (a) — Topic 7: Numerical Integration & Differentiation (Series 18))** Write the algorithm of trapezoidal rule for numerical integration.
   *(Exact duplicate also on: p. 3, (9) (Theory Questions EEE 3109))*

36. **(p. 21, (b) — Topic 7: Numerical Integration & Differentiation (Series 18))** The outflow concentration from a reactor is measured at a number of time instants over 24 hr period.

   | Time (h) | 0 | 4 | 8 | 12 | 16 | 20 | 24 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | C (mg/L) | 1 | 2 | 2.3 | 4 | 5.5 | 3 | 1.2 |

   The flow rate of the outflow in $\text{m}^3/\text{s}$ can be computed with the following equation
   $$Q(t) = 20t \times 10\sin\left\{\frac{2\pi}{24}(t - 10)\right\}$$
   Use the Simpson's $1/3$ method to determine the flow weighted average concentration living the reactor over the 24 hour period using,
   $$\bar{C} = \frac{\int_0^t Q(t)C(t)\,dt}{\int_0^t Q(t)\,dt}$$

37. **(p. 26, (c) — 2023 Odd Semester (EEE 3109))** Analyze the validity of the statement that the numerical integral obtained by Simpson's $1/3$ rule is accurate if the function is a polynomial of order $3$ or less.
   *(Exact duplicate also on: p. 19, (c) (Topic 7: Numerical Integration & Differentiation (Series 20)))*

38. **(p. 26, Q. 4(a) — 2023 Odd Semester (EEE 3109))** Will the accuracy of numerical integration by the trapezoidal method keep increasing if the step-size keeps decreasing? Provide reasoning in favor of your answer.

39. **(p. 29, Q. 7(a) — 2022 Odd Semester (EEE 3109))** Why is Simpson's $1/3$ rule more accurate than trapezoidal rule? Explain graphically.
   *(Exact duplicate also on: p. 20, Q.7. (a) (Topic 7: Numerical Integration & Differentiation (Series 19)))*

40. **(p. 31, (b) — 2020 Odd Semester (EEE 3109))** Why are the numerical differentiation and integration used? Write the algorithm of trapezoidal rule.
   *(Exact duplicate also on: p. 21, (b) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

41. **(p. 33, (b) — 2018 Odd Semester (EEE 3109))** Deduce Weddle's rule $\int_{x_0}^{x_6} y\,dx = \frac{3h}{10}(y_0 + 5y_1 + y_2 + 6y_3 + y_4 + 5y_5 + y_6)$ and use it to obtain an approximate value of $\pi$ from the formula $\frac{\pi}{4} = \int_0^1 \frac{1}{1+x^2}\,dx$ with $h = \frac{1}{6}$. Evaluate the above integral by using Simpson's $\left(\frac{1}{3}\right)\text{rd}$ rule with nine ordinates and compare the results.
   *(Exact duplicate also on: p. 21, (b) (Topic 7: Numerical Integration & Differentiation (Series 15)))*

42. **(p. 33, Q. 5(a) — 2018 Odd Semester (EEE 3109))** Why is numerical integration important for electrical engineers? Discuss the trapezoidal rule for integration.
   *(Exact duplicate also on: p. 21, Q.5 (a) (Topic 7: Numerical Integration & Differentiation (Series 15)); p. 5, (36) (Theory Questions EEE 3109))*

43. **(p. 34, (c) [Q.7(c)] — 2018 Odd Semester (EEE 3109))** The velocities of a car (running on a straight road) at intervals of $2$ minutes are given below.

   | Time in minutes | 0 | 2 | 4 | 6 | 8 | 10 | 12 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | Velocity in km/hr | 0 | 22 | 30 | 27 | 18 | 7 | 0 |

   Apply Simpson's $\left(\frac{3}{8}\right)\text{th}$ rule to find the distance covered by the car.
   *(Exact duplicate also on: p. 22, (c) (Topic 7: Numerical Integration & Differentiation (Series 15)))*

44. **(p. 35, (c) — 2017 Odd Semester (EEE 3109))** Integrate $\int_0^3 (x^2 - 3x + 2)\,dx$ using numerical technique.

45. **(p. 38, (b) — 2016 Odd Semester (EEE 3109))** A circuit is giving following output voltage equation:
   $$v_o = -\frac{1}{RC}\int v_i(t)\,dt$$
   Where $R = 10\text{ k}\Omega$, $C = 1\ \mu\text{F}$, and the value of input is tabulated as follows.

   | $t$ | 0 | 0.25 | 0.50 | 0.75 | 1 | 1.25 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $v_i(t)$ | 1 | 0.9793 | 0.9195 | 0.8261 | 0.7081 | 0.6201 |

   Obtain the value of $v_o$ when $t = 1.25$. Simpson's 1/3 rule should be used for the integration unless other method is needed.

46. **(p. 41, (b) — Semester Exam (EEE 3109, Pre-2016))** Derive Simpson's $1/3$ rule. Apply trapezoidal and Simpson's rule to the integral
   $$I = \int_0^1 \sqrt{1 - x^2}\,dx$$
   continually halving the interval $h$ for better accuracy.

47. **(p. 41, Q. 6(a) — Semester Exam (EEE 3109, Pre-2016))** Suppose that, the current through a resistor is described by the function
   $$i(t) = (60 - t)^2 + (60 - t)\sin\sqrt{t}$$
   and the resistance is a function of the current
   $$R = 12i + 2i^{2/3}$$
   Compute the average voltage over $t = 0$ to $60$ using the multiple-segment Simpson's $1/3$ rule.

48. **(p. 43, Q. 6(a) — 2008 Semester Exam (EEE 251))** The capacitor initially holds no charge. The voltage across *[corner folded in scan]* is computed as $v(t) = \frac{1}{C} \int_0^t i(t)\,dt,\ C = 10^{-5}\text{ F}$.
   Use the following current data to develop a plot of voltage versus time.

   | $t\text{(s)}$ | 0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 | 1.2 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $i\text{(mA)}$ | 0.2 | 0.3683 | 0.3819 | 0.2282 | 0.0486 | 0.0082 | 0.1441 |

49. **(p. 45, (b) — 2007 Regular Exam (EEE-251))** Estimate the value of the following integral by simpson's one third rule
   $$\int_0^{0.8} (0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5)\,dx$$

50. **(p. 48, (b) — 2005 Regular Exam (EEE-251C))** Write down the computer program to solve the following integral by Simpson's $1/3$ rule.
   $$\int_0^1 e^{-x^2}\,dx$$

51. **(p. 52, (b) — 2003 Semester Exam (EEE-251C))** Determine the voltage across the capacitor with respect to time. The experimental data's are given in the following table.

   | $t$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $i(t)$ | 0 | 2 | 3 | 5 | 7 | 8 | 10 | 11 |

52. **(p. 52, (c) — 2003 Semester Exam (EEE-251C))** Write a computer program to evaluate the integral $I = \int_{-1}^{1} (1 - x^2)\cos x\,dx$ using Simpson's $1/3$ rule.

53. **(p. 52, Q. 5(a) — 2003 Semester Exam (EEE-251C))** Starting from Newton's general formula, derive the Trapezoidal rule for numerical integration.
   *(Exact duplicate also on: p. 59, Q. 4(a) (2000 Regular Exam (EEE-251C, 98 Series)))*

54. **(p. 55, Q. 8(a) — 2002 Semester Exam (EEE251C, 2000 Series))** A rocket is launched from the ground. Its acceleration measured every $5$-sec is tabulated below. Find the velocity and the position of the rocket at $t = 40$ sec. Use trapezoidal rule.

   | $t$ | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $a(t)$ | 40 | 45.25 | 48.5 | 51.25 | 54.35 | 59.48 | 61.5 | 64.3 | 68.7 |

55. **(p. 58, (b) — 2001 Regular Exam (EEE-251C))** Integrate the following function over a range of $x = 1$ to $x = 9$. Use Simpson's $1/3^{\text{rd}}$ rule for (i) $h = 1$ and (ii) $h = 2$. Determine the value of the integration by analytical method also and compare the result with that obtained by numerical method.
   $$\int(2x^2 + 3x + 10)\,dx$$

56. **(p. 59, (b) — 2000 Regular Exam (EEE-251C, 98 Series))** Evaluate
   $$I = \int_0^1 \frac{1}{1 + x}\,dx$$
   Correct to three decimal places Use both simpsons and trapezoidal rules and compare their results with comments.

57. **(p. 60, (b) — 1999 Semester Exam (EEE-251C, 97 Series))** Derive Simpson's rule for numerical integration. Write a computer program to evaluate the integral
   $$I = \int_{x_0}^{x_n} y\,dx = \frac{h}{2}\left(y_0 + 2(y_1 + y_2 + \dots) + y_n\right)$$
   using trapezoidal rule

58. **(p. 64, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** Show that the error in Simpson's $1/3$ rule is given by
   $$-\frac{(b - a)}{180} h^4 y^{\text{iv}}(\bar{x})$$

59. **(p. 64, (c) — 1998 Semester Exam (EEE 251C, 96... Series))** A rocket is launched from the ground. Its acceleration is measured at every $5$ seconds as shown in the table below. Find the velocity and position of the rocket at $t = 35$ second. Use Trapezoidal as well as Simpson's rule and comment on the difference of the two results

   | $t$ in sec | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $a(t)$ in km/sec | 40.00 | 45.25 | 48.5 | 51.25 | 54.35 | 59.48 | 61.5 | 64.3 |

60. **(p. 68, Example 5.3.1 — Handwritten Class Problem (ALL CT QUESTION))** The outflow concentration from a reactor is measured at a number of time instants over 24 hrs period.

   | time (h) | 0 | 4 | 8 | 12 | 16 | 20 | 24 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $C$ (mg/L) | 1 | 2 | 2.3 | 4 | 5.5 | 3 | 1.2 |

   The flow rate of the outflow in $\text{m}^3/\text{s}$ can be computed with the following eqn
   $$Q(t) = 20 + 10\sin\left\{\frac{2\pi}{24}(t - 10)\right\}$$
   Using the Simpson's $1/3$ method, determine the flow weighted average concentration leaving the reactor over the $24$ hour period using
   $$\bar{C} = \frac{\int_0^t Q(t)C(t)\,dt}{\int_0^t Q(t)\,dt}.$$

### **Romberg Integration, Gauss Quadrature & Double Integration**

61. **(p. 4, (24) — Theory Questions EEE 3109)** What is the basis of Romberg's integration? Why is this integration technique used?

62. **(p. 19, (b) — Topic 7: Numerical Integration & Differentiation (Series 21))** A separately excited DC generator having a winding inductance of $1\text{ H}$ is feeding a $10\ \Omega$ resistive load. The current voltage relationship is given by -
   $$E(t) = L\frac{dI(t)}{dt} + RI(t)$$
   Solving the above equation, the inductor current is calculated for $6\text{ sec.}$ with an interval of $0.5\text{ sec.}$

   | $t$ | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 | 4.5 | 5 | 5.5 | 6 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $I(t)$ | 0 | 3.93 | 6.32 | 7.77 | 8.65 | 9.18 | 9.50 | 9.70 | 9.82 | 9.89 | 9.93 | 9.96 | 9.98 |

   Now, find the energy consumed by the resistor by performing Romberg integration up to level $3$, so that the order of error is $O(h^6)$.

63. **(p. 20, 6(a) — Topic 7: Numerical Integration & Differentiation (Series 18))** Deduce the expression of Romberg integration.
   *(Exact duplicate also on: p. 2, (7) (Theory Questions EEE 3109))*

64. **(p. 27, (c) — 2023 Odd Semester (EEE 3109))** A series RL circuit consists of an inductor (L) of $1\text{ H}$, a resistor of $1\ \Omega$, and a DC voltage source (E) of $10\text{ V}$ has the following inductor current dynamics:
   $$E(t) = L\frac{dT(t)}{dt} + RI(t)$$
   Solve the above equation, the inductor current is calculated for $6\text{ sec}$ with an interval of $0.5\text{ sec}$.

   | $t$ | 0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 | 6.0 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $I(t)$ | 0 | 3.93 | 6.32 | 7.77 | 8.65 | 9.18 | 9.50 | 9.70 | 9.82 | 9.89 | 9.93 | 9.96 | 9.98 |

   Now, find the energy consumed by the resistor by performing Romberg integration upto level $3$, so the order of error is $O(h^6)$.
   *(Exact duplicate also on: p. 20, (c) (Topic 7: Numerical Integration & Differentiation (Series 20)))*

65. **(p. 29, (b) — 2022 Odd Semester (EEE 3109))** The finite sheet $0 \le x \le 1, 0 \le y \le 1$ on the $z = 0$ plane has a charge density $\rho_s = xy(x^2 + y^2 + 25)^{3/2}\ \text{nC/m}^2$. Find the total charge using both trapezoidal and Simpson's methods.
   Hint: Use surface integration technique.
   *(Exact duplicate also on: p. 20, (b) (Topic 7: Numerical Integration & Differentiation (Series 19)))*

66. **(p. 29, Q. 6(a) — 2022 Odd Semester (EEE 3109))** For Romberg integration, show that, $I\left(h, \frac{h}{2}\right) = \frac{1}{3}\left[4I\left(\frac{h}{2}\right) - I(h)\right]$; where symbols have their usual meaning.
   *(Exact duplicate also on: p. 20, Q.6. (a) (Topic 7: Numerical Integration & Differentiation (Series 19)))*

67. **(p. 31, Q. 7(a) — 2020 Odd Semester (EEE 3109))** What is the basis of Romberg integration? Why is this integration technique used?
   *(Exact duplicate also on: p. 38, (c) (2016 Odd Semester (EEE 3109)); p. 21, Q.7 (a) (Topic 7: Numerical Integration & Differentiation (Series 17)))*

68. **(p. 33, (b) — 2018 Odd Semester (EEE 3109))** Integrate $\int_0^{\frac{\pi}{4}} \sqrt{\cos x}\,dx$ using Gauss quadrature method.
   *(Exact duplicate also on: p. 21, (b) (Topic 7: Numerical Integration & Differentiation (Series 15)))*

69. **(p. 35, (b) — 2017 Odd Semester (EEE 3109))** Deduce the expression of Two-point Gauss-Legendre formula for numerical integration.

70. **(p. 35, Q. 6(a) — 2017 Odd Semester (EEE 3109))** Deduce the expression for error in trapezoidal rule. Hence deduce the expression of Romberg integration.

71. **(p. 38, (d) — 2016 Odd Semester (EEE 3109))** **[figure Involved]** Derive the 2-point Gauss-Quadrature formula for numerical integration. Hence obtain the average value of the following waveform using the formula.

   ![[attachments/fig_p38_d.png]]

72. **(p. 43, (b) — 2008 Semester Exam (EEE 251))** Evaluate $I = \int_0^1 \int_0^1 e^{x+y}\,dx\,dy$ using trapezoidal rule and Simpson's rule. Consider $h = 0.5$. Make a comment on the results obtained by two methods.

73. **(p. 46, (b) — 2007 Regular Exam (EEE-251))** Evaluate the double integral
   $$\int_{x=0}^{8}\int_{y=0}^{6}(2xy + 2x - x^2 - 2y^2 + 72)\,dx\,dy$$

74. **(p. 46, (c) — 2007 Regular Exam (EEE-251))** Determine the rms value of the voltage $v = 10\sin(2\pi \times 50t)$ using Romberg integration formula. Check your result comforming $V_{\text{rms}} = V_m/\sqrt{2}$

75. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** Evaluate the integral of $f(x) = 0.2 + 25x - 200x^2$ from $a = 0$ to $b = 0.8$ using Romberg integration.

76. **(p. 47, Q. 5(a) — 2006 Semester Exam (EEE 251))** Evaluate the integral $I = \int_1^2 \int_1^3 \frac{dx\,dy}{x + y}$ using the trapezoidal rule with $h = k = 0.5$, where $h$ and $k$ are intervals for variables of $x$ and $y$ respectively.
