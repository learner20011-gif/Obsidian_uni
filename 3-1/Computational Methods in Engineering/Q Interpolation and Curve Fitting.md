# EEE 3109 — Interpolation and Curve Fitting (PYQ)

**Syllabus:** Least Square Regression, Polynomial, Spline interpolation, Double interpolation.

---

### **Least Squares Regression (Linear, Polynomial & Non-Linear)**

1. **(p. 4, (21) — Theory Questions EEE 3109)** Mention the different type non-linear approaches which are used for fitting exponential and trignometric functions. Explain at least one approach for them. How is it fitted a curve?

2. **(p. 4, (22) — Theory Questions EEE 3109)** Computational algorithm of polynomial regression to fit a quadratic curve.

3. **(p. 7, (44) — Theory Questions EEE 3109)** Discuss least square curve fitting technique. Why is this technique best for curve fitting?

4. **(p. 16, (b) — Topic 5: Curve Fitting (Series 18))** Write the algorithm of linear regression method.
   *(Exact duplicate also on: p. 2, (6) (Theory Questions EEE 3109))*

5. **(p. 16, (b) — Topic 5: Curve Fitting (Series 17))** From an experiment... *(Rest of question cut off in Topic-Wise scan on p. 16; complete question appears in 2020 Odd Semester Exam Q.5(b), p. 31.)*

6. **(p. 16, (c) — Topic 5: Curve Fitting (Series 17))** **[figure Involved]** Consider the RC circuit, when the switch S is ON at $t = 0$, the voltage across the resistance is determined by the experimental setup are given below:

   | $t\text{(s)}$ | 0 | 0.3 | 0.6 | 0.9 | 1.2 | 1.5 | 1.8 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $V_R(t)$ | 20 | 10 | 5 | 2.5 | 1.25 | 0.625 | 0.375 |

   Determine the input voltage and time constant of this circuit.

   ![[attachments/fig_p16_c.png]]

7. **(p. 16, Q. 5(a) — Topic 5: Curve Fitting (Series 18))** The resonant wavelength in a fibre optic sensing system for the change in the sample refractive index is given below. Fit a second order (quadratic) polynomial to the data points.

   | Refractive index | 1.33 | 1.34 | 1.35 | 1.36 | 1.37 | 1.38 |
   | --- | --- | --- | --- | --- | --- | --- |
   | Resonant wavelength (nm) | 600 | 610 | 630 | 650 | 730 | 780 |

8. **(p. 17, Q.6 (clipped fragment) — Topic 5: Curve Fitting (Series 15))** *[Partially clipped right-hand fragment in Topic-Wise scan:]* ...points? Briefly [04] / ...technique. [04] / [table tail:] `6 | 299.5` *(Full 2018 Odd Semester questions appear on p. 33.)*

9. **(p. 27, (b) — 2023 Odd Semester (EEE 3109))** In a power system, the relationship between the load demand (in MW) and the generation cost (in \$/h) is nonlinear. The following data represents the load demand and the corresponding generation cost:

   | Load demand (MW) | 50 | 100 | 150 | 200 | 250 |
   | --- | --- | --- | --- | --- | --- |
   | Generation Cost (\$/h) | 1200 | 2400 | 4300 | 7000 | 10500 |

   Develop a second order polynomial regression model to fit the given data and determine the coefficients of the polynomial that best describes the load demand-generation cost relationship.
   *(Exact duplicate also on: p. 16, (b) (Topic 5: Curve Fitting (Series 20)))*

10. **(p. 27, (b) — 2023 Odd Semester (EEE 3109))** Write down a computational algorithm of polynomial regression to fit a quadratic curve.

11. **(p. 27, (c) — 2023 Odd Semester (EEE 3109))** The following data was taken from an experiment that measured current in a wire for various imposed voltage on the basis of a linear regression of these data. Determine current of a voltage of $3.5\text{ V}$. Plot the line and data, and then evaluate the fit.

   | $V$ (V) | 2 | 3 | 4 | 5 | 7 | 10 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $I$ (A) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 2.5 |
   *(Exact duplicate also on: p. 15, (c) (Topic 5: Curve Fitting (Series 20)))*

12. **(p. 27, Q. 5(a) — 2023 Odd Semester (EEE 3109))** Mention different non-linear approaches which are used for fitting exponential and trigonometric functions. Explain at least one approach for them. How is it fitted a curve?

13. **(p. 29, (b) — 2022 Odd Semester (EEE 3109))** The data below represents the bacterial growth in a liquid culture over a number of days.

   | Day | 0 | 4 | 8 | 12 | 16 | 20 |
   | --- | --- | --- | --- | --- | --- | --- |
   | Amount $\times 10^6$ | 67 | 84 | 98 | 125 | 149 | 185 |

   Find a best-fit equation to the data trend. Try several possibilities-(i) linear, (ii) parabolic, and (iii) exponential. Also predict the amount of bacteria after $40$ days.
   *(Exact duplicate also on: p. 16, (b) (Topic 5: Curve Fitting (Series 19)))*

14. **(p. 31, (b) — 2020 Odd Semester (EEE 3109))** From an experimental setup the data of terminal voltage versus speed of a dc motor is recorded below. From those data, $(210, 1190)$ is more reliable than others, so prescribe a weight of $10$ to this point and all other weight are taken as unity.

   | Terminal voltage (v) | 180 | 190 | 200 | 205 | 210 | 220 | 230 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | Speed (rpm) | 1050 | 1120 | 1150 | 1180 | 1190 | 1197 | 1201 |

   Estimate the speed when terminal voltage is $202\text{ V}$ using linear weighted least-square curve fitting.

15. **(p. 31, (c) — 2020 Odd Semester (EEE 3109))** **[figure Involved]** Consider the RC circuit, when the switch S is ON at $t = 0$, the voltage across the resistance is determined by the experimental setup are given below:

   | $t\text{(s)}$ | 0 | 0.3 | 0.6 | 0.9 | 1.2 | 1.5 | 1.8 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $V_R(t)$ | 20 | 10 | 5 | 2.5 | 1.25 | 0.625 | 0.375 |

   Determine the input voltage and time constant of this circuit.
   Hint: Use curve fitting technique.

   ![[attachments/fig_p31_c_2.png]]

16. **(p. 31, Q. 5(a) — 2020 Odd Semester (EEE 3109))** What are the differences between least-square curve fitting and weighted least-square curve fitting? Which one gives better results and why?
   *(Exact duplicate also on: p. 16, Q.5 (a) (Topic 5: Curve Fitting (Series 17)))*

17. **(p. 33, (c) — 2018 Odd Semester (EEE 3109))** *[Prompt line above table clipped by page seam in scan:]*

   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $y$ | 1.5 | 4.6 | 13.9 | 40.1 | 125.1 | 299.5 |

   Find the best values of '$a$' and '$b$'.

18. **(p. 33, Q. 6(a) — 2018 Odd Semester (EEE 3109))** What are the approaches used for fitting a curve to a given set of data points? Briefly explain at least one approaches.

19. **(p. 35, Q. 4(a) — 2017 Odd Semester (EEE 3109))** Discuss least square curve fitting technique. Why this technique is the best for curve fitting?

20. **(p. 37, Q. 3(a) — 2016 Odd Semester (EEE 3109))** What are the approaches for fitting a curve to a given set of data points? Give a short description about them.

21. **(p. 41, (b) — Semester Exam (EEE 3109, Pre-2016))** What is meant by curve fitting? Develop algorithm to fit
   (i) an exponential curve
   (ii) a trigonometric function.

22. **(p. 41, Q. 5(a) — Semester Exam (EEE 3109, Pre-2016))** An experiment is performed to determine the percentage (%) elongation of electrical conducting material as function of temperature. The resulting data is:

   | Temp $^{\circ}\text{C}$ | 200 | 250 | 300 | 375 | 425 | 475 | 525 | 600 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | % elongation | 11 | 13 | 13 | 15 | 17 | 19 | 20 | 23 |

   Predict the % elongation for a temperature of $400^{\circ}\text{C}$ (Use Linear Regression).

23. **(p. 43, (b) — 2008 Semester Exam (EEE 251))** You are working as an engineer for a utility company. Your job responsibility is to forecast the population $5$ years into the future in order to anticipate the demand for power. Employ an exponential model and linear regression to make this prediction. The population is given over a $20$ year period.

   | $t$ | 0 | 5 | 10 | 15 | 20 |
   | --- | --- | --- | --- | --- | --- |
   | $P$ | 100 | 212 | 448 | 949 | 2009 |

24. **(p. 43, Q. 7(a) — 2008 Semester Exam (EEE 251))** What is the criterion for a best fit for a curve? Fit a $2^{\text{nd}}$ order polynomial to the data given in the following table:

   | $i$ (Amp) | 0 | 1 | 2 | 3 | 4 | 5 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $v = f(i)$ Volts | 2.1 | 7.7 | 13.6 | 27.2 | 40.9 | 61.1 |

25. **(p. 45, (b) — 2007 Regular Exam (EEE-251))** The following data was taken from an experiment that measured the current in a wire for various imposed voltages :

   | $V$ (volts) | 2 | 3 | 4 | 5 | 7 | 10 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $I$ (amps) | 5.2 | 7.8 | 10.7 | 13 | 19.3 | 27.5 |

   On the basis of a linear regression of this data, determine current for a voltage of $6\text{ v}$. Plot the line and the data and evaluate the fit.

26. **(p. 45, Q. 4(a) — 2007 Regular Exam (EEE-251))** (i) What are the two general approaches of curve fitting ? Distinguish them.
   (ii) What is spline ? In which cases the spline method of interpolation is preferable to other techniques ?
   (iii) Derive normal equation for quadratic regression.
   (iv) Write down the condition for cubic spline.

27. **(p. 47, Q. 2(a) — 2006 Semester Exam (EEE 251))** What is the 'criteria of best fit' used in least square regression? Use the least squares method and determines the exponential fit $y = ce^{Ax}$ for five data points $(0, 1.5), (1, 2.5), (2, 3.5), (3, 5.0)$ and $(4, 7.5)$.

28. **(p. 48, (c) — 2005 Regular Exam (EEE-251C))** Fit a curve of the type $ae^{bx}$ for the data given in the following table.

   | $x$ | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $y$ | 3.1 | 1.7 | 1.0 | 0.68 | 0.42 | 0.26 | 0.14 | 0.09 |

29. **(p. 48, Q. 1(a) — 2005 Regular Exam (EEE-251C))** What do you mean by curve fitting? What is meant by best fitting? How is curve fitting useful to engineers?

30. **(p. 51, (b) — 2003 Semester Exam (EEE-251C))** **[figure Involved]** Consider a R-L circuit, when the switch 'S' is on at $t = 0$, the voltage across the inductor is determined by the experimental set-up are given below:

   | $t$ | 0 | 0.3 | 0.6 | 0.9 | 1.2 | 1.5 | 1.8 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $V_L(t)$ | 20 | 10 | 5 | 2.5 | 1.25 | 0.625 | 0.375 |

   ![[attachments/fig_p51_b.png]]

31. **(p. 51, Q. 4(a) — 2003 Semester Exam (EEE-251C))** Write a computer program to fit the voltage across the inductance of a R-L circuit. Data's are given below:

   | $t\text{(s)}$ | 0 | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 | 2.4 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $V(t)$ | 10 | 6 | 3 | 2 | 1 | 0.5 | 0.1 |

32. **(p. 52, Q. 6(a) — 2003 Semester Exam (EEE-251C))** Find the least square approximation of second degree for the discrete data:

   | $x$ | -2 | -1 | 0 | 1 | 2 |
   | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 15 | 1 | 1 | 3 | 19 |

33. **(p. 58, (b) — 2001 Regular Exam (EEE-251C))** Obtain the best fit equation of a second degree polynomial for the following set of data

   | $X$ | 1 | 2 | 3 | 4 |
   | --- | --- | --- | --- | --- |
   | $Y$ | 2 | 5 | 6 | 7 |

34. **(p. 58, Q. 7(a) — 2001 Regular Exam (EEE-251C))** Write a suitable computer program for the least square quadratic fits for discrete data
   $$(x_i, f_i),\quad i = 0, 1, 2, \dots, N.$$

35. **(p. 59, (b) — 2000 Regular Exam (EEE-251C, 98 Series))** Derive the least square quadratic fits for a discrete data $(x_i, f_i),\ i = 0, 1, 2, \dots, N.$

36. **(p. 59, (c) — 2000 Regular Exam (EEE-251C, 98 Series))** Find the least square approximation of second degree for the discrete data

   | $X$ | -2 | -1 | 0 | 1 | 2 |
   | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 15 | 1 | 1 | 3 | 19 |

37. **(p. 61, (b) — 1999 Semester Exam (EEE-251C, 97 Series))** Find the least square approximation of the second order for the descrete data

   | $x$ | -2 | -1 | 0 | 1 | 2 |
   | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 15 | 1 | 1 | 3 | 19 |

   using a computer program.

38. **(p. 63, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** Explain how a set of given data can be fitted to a sinusoidal curve.

39. **(p. 63, (c) — 1998 Semester Exam (EEE 251C, 96... Series))** Plot $y$ versus $x$ for the following set of experimental data. Guess the nature of the curve from the plot. Use least square method to fit the curve

   | $x$ | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $y$ | 7.6 | 13.2 | 27.4 | 43.0 | 62.5 | 86.4 | 115.1 | 147.0 | 182.2 |

40. **(p. 63, Q. 4(a) — 1998 Semester Exam (EEE 251C, 96... Series))** What is curve fitting? How is it useful to engineers?

41. **(p. 67, 3. — Class test #2, EEE' 20 (A) (02/09/2024))** Fit the following data with the power model ($y = ax^b$). Use the resulting power equation to predict $y$ at $x = 9$.

   | $x$ | 2.5 | 3.5 | 5 | 6 | 7.5 | 10 | 12.5 | 15 | 17.5 | 20 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $y$ | 13 | 11 | 8.5 | 8.2 | 7.2 | 6.2 | 5.2 | 4.8 | 4.6 | 4.3 |

42. **(p. 67, 4. — Class test #2, EEE' 20 (A) (02/09/2024))** Use multiple linear regression to fit

   | $x_1$ | 0 | 0 | 1 | 2 | 0 | 1 | 2 | 2 | 1 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $x_2$ | 0 | 2 | 2 | 4 | 4 | 6 | 6 | 2 | 1 |
   | $y$ | 14 | 21 | 11 | 12 | 23 | 23 | 14 | 6 | 11 |

43. **(p. 69, 1, 2 & 3 — Class test #3, EEE' 20 (B) (03/08/2024))** In a power system, the relationship between the load demand (in MW) and the generation cost (in \$/h) is nonlinear. The following data represents the load demand and the corresponding generation cost:

   | Load Demand (MW) | 50 | 100 | 150 | 200 | 250 |
   | --- | --- | --- | --- | --- | --- |
   | Generation Cost (\$/h) | 1200 | 2400 | 4300 | 7000 | 10500 |

   1. Develop a third-order (cubic) polynomial regression model to fit the given data and determine the coefficients of the polynomial that best describes the load demand-generation cost relationship.
   2. Use linear regression to solve the above problem.
   3. Compare the effectiveness of third order polynomial regression model and linear regression model based on the sum of squared error at the given data points.

44. **(p. 76, 1. — Class test #3, EEE' 21 (C) (13/05/2025))** Outline the steps to perform multiple linear regression with mathematical explanations.

45. **(p. 76, 2. — Class test #3, EEE' 21 (C) (13/05/2025))** In a power system, the relationship between the load demand (in MW) and the generation cost (in \$/h) is nonlinear. The following data represents the load demand and the corresponding generation cost:

   | Load Demand (MW) | 50 | 100 | 150 | 200 | 250 |
   | --- | --- | --- | --- | --- | --- |
   | Generation Cost (\$/h) | 1200 | 2400 | 4300 | 7000 | 10500 |

   Develop a second-order polynomial regression model to fit the given data and determine the coefficients of the polynomial that best describes the load demand-generation cost relationship..

### **Polynomial Interpolation (Newton's Divided-Difference, Lagrange, Forward/Backward)**

46. **(p. 4, (20) — Theory Questions EEE 3109)** Define extrapolation. What type difference table is used in extrapolation? Discuss the selection criteria of forward, backward and central interpolation.

47. **(p. 5, (35) — Theory Questions EEE 3109)** Algorithm of Lagrange's interpolation formula for unevenly spaced data points.

48. **(p. 8, (49) — Theory Questions EEE 3109)** Deduce Newton's forward difference interpolation formula.

49. **(p. 8, (55) — Theory Questions EEE 3109)** Basic concept of numerical interpolation with suitable example.

50. **(p. 8, (56) — Theory Questions EEE 3109)** Difference between divided difference table and difference table of interpolation technique.

51. **(p. 17, (b) — Topic 6: Interpolation (Series 21))** A resistor's temperature coefficient causes its resistance to vary with temperature. The resistance R (in $\Omega$) of a certain thermistor is measured at different temperatures T (in $^{\circ}\text{C}$) as shown in the following table:

   | Temperature, $T$ ($^{\circ}\text{C}$) | Resistance, $R$ ($\Omega$) |
   | --- | --- |
   | 20 | 120 |
   | 40 | 100 |
   | 60 | 80 |

   Use a second-order Lagrange-interpolating polynomial, estimate the resistance at $T = 50\ ^{\circ}\text{C}$.

52. **(p. 17, Q. 4(a) — Topic 6: Interpolation (Series 18))** Find the Lagrange interpolation polynomial which agrees with the following data

   | $x$ | 1.0 | 1.1 | 1.2 |
   | --- | --- | --- | --- |
   | $\cos(x)$ | 0.5403 | 0.4536 | 0.3624 |

   Use it to estimate $\cos(1.15)$

53. **(p. 18, (b) — Topic 6: Interpolation (Series 18))** Estimate the value of $\ln(3.5)$ using Newton-Gregory forward difference formula from the following data.

   | $x$ | 1.0 | 2.0 | 3.0 | 4.0 |
   | --- | --- | --- | --- | --- |
   | $\ln(x)$ | 0.0 | 0.6931 | 1.0986 | 1.3863 |

54. **(p. 18, (c) — Topic 6: Interpolation (Series 18))** Deduce the expression of Newton-Gregory forward interpolation formula. Why is it better than Lagrange formula?
   *(Exact duplicate also on: p. 2, (5) (Theory Questions EEE 3109))*

55. **(p. 18, (c) — Topic 6: Interpolation (Series 17))** **[figure Involved]** Consider a RL circuit, when the switch 'S' is on at $t = 0$ the voltage across the inductor is determined by the following network setup. Determine the voltage across the inductor when $t = 1.75\text{ s}$ using any numerical interpolation technique.

   | $t\text{(s)}$ | 0 | 0.30 | 0.60 | 0.90 | 1.20 | 1.50 | 1.80 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $v_L(s)$ | 20 | 10 | 5 | 2.5 | 1.25 | 0.625 | 0.375 |

   ![[attachments/fig_p18_c.png]]

56. **(p. 27, (c) — 2023 Odd Semester (EEE 3109))** For the same relationship between the load demand and the generation cost as mentioned in the data table of Question 6(b), develop the Newton's divided-difference interpolating polynomial. Also, compare the effectiveness of the second-order polynomial regression model and the fourth order Newton's divided difference interpolating polynomial model based on the sum of squared error at the given data points. *(Refers to the Load demand vs. Generation Cost table in Q.6(b), p. 27.)*

57. **(p. 28, (b) — 2022 Odd Semester (EEE 3109))** If $y(1) = 3, y(3) = 9, y(4) = 30$ and $y(6) = 32$, find the four point Lagrange interpolation polynomial that takes the same values as the function of $y$ at those given points.
   *(Exact duplicate also on: p. 17, (b) (Topic 6: Interpolation (Series 19)))*

58. **(p. 28, (c) — 2022 Odd Semester (EEE 3109))** The following set of data is obtained in an experiment that shows the variation of voltage at different instant of time of a R-C circuit. Estimate the voltage at $t = 1.22\text{ s}$ by an interpolation technique using Newton's backward formula.

   | $t$: sec | 0 | 0.3 | 0.6 | 0.9 | 1.2 | 1.5 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $v(t)$: volt | 0.2 | 0.6 | 0.8 | 1.2 | 1.3 | 1.4 |
   *(Exact duplicate also on: p. 17, (c) (Topic 6: Interpolation (Series 19)))*

59. **(p. 31, (b) — 2020 Odd Semester (EEE 3109))** Prove that, Lagrange's interpolation formula for $n^{\text{th}}$ order is $L_n(x) = \sum_{i=0}^{n} \frac{\pi_{n+1}(x)}{(x - x_i)\pi'_{n+1}(x_i)} y_i$ ; where symbols have their usual meaning.
   *(Exact duplicate also on: p. 18, (b) (Topic 6: Interpolation (Series 17)))*

60. **(p. 31, (c) — 2020 Odd Semester (EEE 3109))** **[figure Involved]** Consider a RL circuit, when the switch 'S' is on at $t = 0$ the voltage across the inductor is determined by the following network setup. Determine the voltage across the inductor when $t = 1.75\text{ s}$ using any numerical interpolation technique.

   | $t\text{(s)}$ | 0 | 0.30 | 0.60 | 0.90 | 1.20 | 1.50 | 1.80 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $v_L(t)$ | 20 | 10 | 5 | 2.5 | 1.25 | 0.625 | 0.375 |

   ![[attachments/fig_p31_c.png]]

61. **(p. 31, Q. 4(a) — 2020 Odd Semester (EEE 3109))** Prove that, the error in polynomial interpolation is $y(x) - \varphi_n(x) = \frac{\pi_{n+1}(x)}{(n+1)!} y^{(n+1)}(\xi)$, $x_0 < \xi < x_n$ where symbols have their usual meaning.

62. **(p. 33, (b) — 2018 Odd Semester (EEE 3109))** Write down the algorithm of Lagrange's interpolation formula for unevenly spaced data points.
   *(Exact duplicate also on: p. 18, (b) (Topic 6: Interpolation (Series 15)))*

63. **(p. 33, (c) — 2018 Odd Semester (EEE 3109))** The upward velocity of a rocket is given as a function of time in the following table. Find the velocity at $t = 16\text{s}$ using Newton divided difference method for linear interpolation.

   Table: Velocity as a function of time

   | $t\text{(s)}$ | 0 | 10 | 15 | 20 | 22.5 | 30 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $v(t)\ (\text{m/s})$ | 0 | 227.04 | 362.78 | 517.35 | 602.97 | 901.67 |
   *(Exact duplicate also on: p. 18, (c) (Topic 6: Interpolation (Series 15)))*

64. **(p. 33, (c) [Q.5(c)] — 2018 Odd Semester (EEE 3109))** What are the difference tables used in interpolation? Briefly discuss the choosing criteria of using them.
   *(Exact duplicate also on: p. 18, (b) [difference tables] (Topic 6: Interpolation (Series 15)))*

65. **(p. 33, Q. 4(a) — 2018 Odd Semester (EEE 3109))** Starting from a polynomial approximation, derive the Newton-Gregory forward interpolation formula.
   *(Exact duplicate also on: p. 18, Q.4. (a) (Topic 6: Interpolation (Series 15)))*

66. **(p. 35, (b) — 2017 Odd Semester (EEE 3109))** Derive the Newton-Gregory Forward difference interpolation formula.

67. **(p. 35, (c) — 2017 Odd Semester (EEE 3109))** **[figure Involved]** From the following circuit arrangement construct a table of voltage versus current. Hence obtain the current for any unknown voltage (not tabulated) using a numerical method.

   ![[attachments/fig_p35_c_3.png]]

68. **(p. 37, (b) — 2016 Odd Semester (EEE 3109))** The following values are taken from the table of cubes. Find $(6.36)^3$ and $(6.61)^3$.

   | $x$ | 6.1 | 6.2 | 6.3 | 6.4 | 6.5 | 6.6 | 6.7 |
   | --- | --- | --- | --- | --- | --- | --- | --- |
   | $y = x^3$ | 226.981 | 238.328 | 250.047 | 262.144 | 274.625 | 287.496 | 300.763 |

69. **(p. 37, (b) — 2016 Odd Semester (EEE 3109))** What are the difference tables used in interpolation? Discuss the choosing criteria of using them.

70. **(p. 37, (c) — 2016 Odd Semester (EEE 3109))** What is the difference between divided difference table and difference table for interpolation? Derive Newton's forward difference interpolation formula.

71. **(p. 37, (c) — 2016 Odd Semester (EEE 3109))** A voltage is measured as in the table below:

   | $\omega t$ | 0.15 | 0.17 | 0.19 | 0.21 | 0.23 |
   | --- | --- | --- | --- | --- | --- |
   | $V_m\sin(\omega t)$ | 0.14944 | 0.16918 | 0.18886 | 0.20846 | 0.22789 |

   Obtain the voltage at $\omega t = 0.24$ using a Newton-Gregory interpolation formula.

72. **(p. 37, Q. 4(a) — 2016 Odd Semester (EEE 3109))** Deduce the expression of Newton-Gregory forward interpolation formula.

73. **(p. 40, (b) — Semester Exam (EEE 3109, Pre-2016))** Find the Lagrange interpolating polynomial of degree $2$ approximating the function $y = \ln(x)$ defined by the following table values. Hence determine the value of $\ln(2.7)$

   | $x$ | 2 | 2.5 | 3.0 |
   | --- | --- | --- | --- |
   | $y = \ln(x)$ | 0.69315 | 0.91629 | 1.09861 |

74. **(p. 47, (b) — 2006 Semester Exam (EEE 251))** The current in a wire is measured with great precision as function of time:

   | $t$ (sec) | 0 | 0.125 | 0.250 | 0.375 | 0.500 |
   | --- | --- | --- | --- | --- | --- |
   | $i$ (amp) | 0 | 6.2402 | 7.7880 | 4.8599 | 0.0000 |

   Estimate $i$ at $t = 0.22$ using Lagranges polynomial of third order. Write a computer program to solve the problem.

75. **(p. 48, Q. 2(a) — 2005 Regular Exam (EEE-251C))** Deduce Newton's formula for forward interpolation. Express the formula in a form where the co-efficients $\Delta$'s are the binomial co-efficients.

76. **(p. 51, (b) — 2003 Semester Exam (EEE-251C))** The following set of data is obtained in an experiment that shows the variation of voltage at different instant of time of a R-C circuit. Estimate the voltage at $t = 1.24\text{ s}$ by an interpolation technique using Newton's backward formula.

   | $t$ | 0 | 0.3 | 0.6 | 0.9 | 1.2 | 1.5 |
   | --- | --- | --- | --- | --- | --- | --- |
   | $V(t)$ | 0.2 | 0.6 | 0.8 | 1.2 | 1.3 | 1.4 |

77. **(p. 52, (c) — 2003 Semester Exam (EEE-251C))** For the following data, calculate the differences and obtain forward and backward difference polynomials interpolate at $x = 0.25$

   | $x$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 |
   | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 1.4 | 1.56 | 1.76 | 2.0 | 2.28 |

78. **(p. 55, (b) — 2002 Semester Exam (EEE251C, 2000 Series))** Derive Lagrange's interpolation formula of the $n$th order.

79. **(p. 55, (c) — 2002 Semester Exam (EEE251C, 2000 Series))** The following set of data is obtained in an experimental which shows the variation of voltage at different instants of time. Estimate the voltage at $t = 12$ seconds by an interpolation method.

   | $t$ | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $v$ | 19 | 37 | 61 | 75 | 85 | 92 | 98 | 102 | 105 |

80. **(p. 55, Q. 7(a) — 2002 Semester Exam (EEE251C, 2000 Series))** What is interpolation? What is extrapolation? What assumption is made during interpolation and extrapolation?
   *(Exact duplicate also on: p. 63, Q. 5(a) (1998 Semester Exam (EEE 251C, 96... Series)))*

81. **(p. 59, (c) — 2000 Regular Exam (EEE-251C, 98 Series))** What is interpolation? How does it differ from curve fitting?

82. **(p. 61, Q. 7(a) — 1999 Semester Exam (EEE-251C, 97 Series))** Using the following data, calculate the differences and obtain the forward difference polynomial and interpolate at $x = 0.25$

   | $x$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 |
   | --- | --- | --- | --- | --- | --- |
   | $f(x)$ | 1.4 | 1.56 | 1.76 | 2.00 | 2.28 |

83. **(p. 63, (b) — 1998 Semester Exam (EEE 251C, 96... Series))** If $y(1) = -3$, $y(3) = 9$, $y(4) = 30$ and $y(6) = 132$, find the four point Lagrange interpolation polynomial that takes the same values as the function of $y$ at the given points.

84. **(p. 63, (c) — 1998 Semester Exam (EEE 251C, 96... Series))** The following set of data is obtained in an experiment which shows the variation of voltage at different instants of time. (i) Estimate the voltage at $t = 12$ second by using Newton's difference formula (ii) Can you guess at what instant of time the voltage attained at $100$ volt?

   | $t$ in sec | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | $v$ in volt | 19 | 37 | 61 | 75 | 85 | 92 | 98 | 102 | 105 |

85. **(p. 65, Q. 1 — CT#3 (C) (EEE 3109))** Suppose, the third year students under the Department of Electrical and Electronic Engineering, Rajshahi University of Engineering & Technology sat for the class test of Computational Methods in Engineering course. The marks distribution with respect the students are given below.

   Table 1: Relation between mark obtained and no. of students.

   | Marks Obtained | 0 | 4 | 8 | 12 | 16 | 20 |
   | --- | --- | --- | --- | --- | --- | --- |
   | No. of Students | 5 | 3 | 7 | 14 | 18 | 6 |

   Problem: Find the no. of students those who will get 15.
   Criteria 1: Use any interpolation technique to solve the problem. (Use Table 1)
   Criteria 2: Carefully follow the each elements of the table. Prepare the table by replacing the element 8 by 9 & 16 by 17. Now, solve the problem using any interpolation technique.

86. **(p. 69, 1. — Class test #4, EEE' 20 (B) (18/09/2024))** The power output of a solar panel is measured at different irradiance levels (solar intensity), as shown below:

   | Irradiance, $I$ ($\text{Watt/m}^2$) | 200 | 400 | 600 | 800 | 1000 |
   | --- | --- | --- | --- | --- | --- |
   | Power, $P$ (Watts) | 34 | 75 | 105 | 130 | 150 |

   Use Newton's divided difference method to find the interpolation polynomial that models the power output $P$ as a function of irradiance $I$.

87. **(p. 69, 2. — Class test #4, EEE' 20 (B) (18/09/2024))** **[figure Involved]** The daily electrical load (in kW) of a restaurant is recorded in an hourly basis which is illustrated in the figure and table below. Select a set of suitable data points from the table considering the load curve and prepare a load forecasting model using Lagrange interpolating polynomial.

   | Hour | Load | Hour | Load | Hour | Load |
   | --- | --- | --- | --- | --- | --- |
   | 1 | 2 | 9 | 4 | 17 | 6 |
   | 2 | 1.5 | 10 | 5 | 18 | 8 |
   | 3 | 1 | 11 | 6 | 19 | 12 |
   | 4 | 1 | 12 | 7 | 20 | 15 |
   | 5 | 1.5 | 13 | 8 | 21 | 18 |
   | 6 | 2 | 14 | 9 | 22 | 16 |
   | 7 | 2.5 | 15 | 8 | 23 | 12 |
   | 8 | 3 | 16 | 7 | 24 | 6 |

   ![[attachments/fig_p69_2.png]]

### **Spline Interpolation & Double Interpolation**

88. **(p. 7, (37) — Theory Questions EEE 3109)** What is B-splines curve fitting?

89. **(p. 17, Q.6. (a) — Topic 6: Interpolation (Series 21))** Briefly explain the procedure with necessary conditions those are required to evaluate the unknowns while fitting quadratic splines to a set of data.

90. **(p. 27, Q. 6(a) — 2023 Odd Semester (EEE 3109))** Illustrate the necessity of spline interpolation through an example.

91. **(p. 28, Q. 4(a) — 2022 Odd Semester (EEE 3109))** Discuss about double interpolation.
   *(Exact duplicate also on: p. 17, Q.4. (a) (Topic 6: Interpolation (Series 19)))*

92. **(p. 33, (b) — 2018 Odd Semester (EEE 3109))** What is B-Splines curve fitting? Write a computational algorithm of linear regression technique.

93. **(p. 47, Q. 4(a) — 2006 Semester Exam (EEE 251))** What are the conditions satisfied for cubic spline interpolation?

94. **(p. 59, Q. 7(a) — 2000 Regular Exam (EEE-251C, 98 Series))** What is Spline interpolation? Discuss it's advantages over other methods.

95. **(p. 61, (b) — 1999 Semester Exam (EEE-251C, 97 Series))** For the given set of data, derive the cubic spline equations and determine the value of $y$ at $x = 3.8$

   | $x$ | 1 | 2 | 3 | 4 | 5 |
   | --- | --- | --- | --- | --- | --- |
   | $y$ | 6 | -4 | 0 | 2 | -6 |

96. **(p. 61, Q. 6(a) — 1999 Semester Exam (EEE-251C, 97 Series))** What is spline interpolation ? Derive the necessary equations for spline interpolation. Compare spline interpolation with other interpolation methods.
