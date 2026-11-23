# EEE 3105 — Time Domain Analysis (PYQ)

**Syllabus:** Transient and steady-state responses of first, second and multi-order dynamic systems, Steady state errors, Control of transient response, Basic control actions and their effects on transient and steady state responses.

---

### **Transient and Steady-State Responses of First, Second, and Multi-Order Dynamic Systems**

1. **Page 20, Row 1 (Question Analysis Table (Year 21)):** The unit step response of a linear control system is shown below: (i) Find the transfer function of a $2^{\text{nd}}$ order system. (ii) Find the delay time, rise time, and settling time. **[figure Involved]**

   ![[attachments/fig_p20_row_1.png]]

2. **Page 37, Q.4(a) (RUET 2021 Odd Semester (Page 2/2)):** The unit step response of a linear control system in shown below: (i) Find the transfer function of a $2^{nd}$ order system. (ii) Find the rise time and settling time. **[figure Involved]** *(Exact duplicate also on: Page 20, Row 9 Q.1(a) (p.20-21) (Question Analysis Table (Year 18)); Page 59, Q2 (CT#03 on EEE 3105 (Section: A)))*

   ![[attachments/fig_p37_q_4_a.png]]

3. **Page 40, Q.1(c) (RUET 2018 Odd Semester (SECTION-A)):** A series circuit in the following figure consisting of resistance R and an inductance L is connected to a supply $v(t)$. Find the expression of the current in S domain. Also, calculate the value of current at $t = 0.5\text{ ms}$ with $R = 1\times 10^3\,\Omega$, $L = 25\text{ mH}$ and supply is a step voltage of $50\text{ V}$. Neglect initial condition. **[figure Involved]** *(Exact duplicate also on: Page 12, Row 8 (c) (p.12-13) (Question Analysis Table (Year 15, SECTION-A)))*

   ![[attachments/fig_p40_q_1_c.png]]

4. **Page 48, Q.3(c) (RUET 2015 3rd Year 5th Semester (Page 2 of 2)):** The unit-step response of a linear control system is shown in the following figure. Find the transfer function of a second-order prototype system to model the system. Also find rise time. **[figure Involved]**

   ![[attachments/fig_p48_q_3_c.png]]

5. **Page 51, Q.4(a) (RUET 2014 3rd Year 6th Semester (Page 2 of 2)):** [For the] unit step response shown in following figure, find rise time, peak time, maximum overshoot and [settling time]. **[figure Involved]**

   ![[attachments/fig_p51_q_4_a.png]]

6. **Page 52, Q.2(c) (RUET 2013 3rd Year 6th Semester (SECTION A)):** Discuss about different types of test signals for designing a control system. Why are these signals used as test signals?

7. **Page 61, Q2 (CT#02 on EEE 3105 (Section: B (21 Series))):** The unit step response of a linear control system in shown below: Find the rise time, maximum overshoot, and settling time. **[figure Involved]**

   ![[attachments/fig_p61_q2.png]]

8. **Page 69, Q1 (Class Test (Page 2)):** For the following dynamic system determine: $$T(s) = \frac{s+1}{s^2+4}$$ (i) Order and type of the system. (ii) The nature of stability of the system. (iii) The nature of response of the system with unity step input.

### **Damping Ratio, Pole Locations, and Time-Domain Specifications**

9. **Page 3, Q.(07) (Handwritten Theory Questions List):** Mathematically prove that for a zero damping ratio, the system response will be oscillatory when subjected to a unit step input.

10. **Page 3, Q.(08) (Handwritten Theory Questions List):** Write short notes about the followings: (i) Absolute stability (ii) damping ratio (iii) frequency response (iv) under-damped system

11. **Page 4, Q.(22) (Handwritten Theory Questions List):** Define undamped natural frequency and damping ratio.

12. **Page 5, Q.(25) (Handwritten Theory Questions List):** What are the effects of adding pole and zero on a system?

13. **Page 5, Q.(30) (Handwritten Theory Questions List):** Short notes on (i) undamped system; (ii) Overdamped system; (iii) transition matrix; (iv) Detour

14. **Page 6, Q.(32) (Handwritten Theory Questions List):** What is the effect of feedback on time constant of a control system? Draw a typical transient response output for an under-damped 2nd order system and show the locations of all the transient response specifications.

15. **Page 8, Q.(48) (Handwritten Theory Questions List):** Short notes on (i) critically damped system, (ii) over damped system.

16. **Page 8, Q.(49) (Handwritten Theory Questions List):** What is damping?

17. **Page 9, Row 3 (Question Analysis Table (Year 21)):** How does the location of poles affect system performance in terms of stability, settling time, and overshoot?

18. **Page 9, Row 4 (Question Analysis Table (Year 21)):** Explain the effect of damping ratio on the unit step response of a typical second order system.

19. **Page 20, Row 4 (Question Analysis Table (Year 20)):** Consider the closed-loop system given by $\frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$. Determine the values of $\zeta$ and $\omega_n$ so that the system responds to a step input with approximately 5% overshoot and with a settling time of 2 sec (use the 2% criterion).

20. **Page 20, Row 7 (a) (Question Analysis Table (Year 19)):** Prove that the maximum overshoot occurs at $t_m = \frac{\cos^{-1}\zeta}{\omega_n\sqrt{1-\zeta^2}}$ for the case of transient response analysis of a second order system with impulse excitation.

21. **Page 31, Q.3(c) (RUET 2023 Odd Semester (SECTION-A)):** Mathematically prove that for a zero damping ratio the system response will be oscillatory when subjected to a unit step input. *(Exact duplicate also on: Page 37, Q.4(b) (RUET 2021 Odd Semester (Page 2/2)); Page 20, Row 3 (Question Analysis Table (Year 20)); Page 21, Row 2 (b) (Question Analysis Table (Year 18)))*

22. **Page 32, Q.4(a) (RUET 2023 Odd Semester (Page 2/2)):** Consider the closed-loop system given by $\frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$. Determine the values of $\zeta$ and $\omega_n$, so that the system responds to a step input with approximately 5% overshoot and with a settling time of 2 sec (use the 2% criterion).

23. **Page 32, Q.4(b) (RUET 2023 Odd Semester (Page 2/2)):** Define: (i) Undamped, (ii) underdamped, (iii) over-damped, and (iv) critically damped. Also show the roots positions. *(Exact duplicate also on: Page 20, Row 5 (Question Analysis Table (Year 20)))*

24. **Page 32, Q.5(b) (RUET 2023 Odd Semester (SECTION-B)):** Prove that settling time of a second order dynamic system is $t_s = \frac{4}{\zeta\omega_n}$ for 2% tolerance band. *(Exact duplicate also on: Page 20, Row 6 (Question Analysis Table (Year 20)))*

25. **Page 32, Q.6(a) (RUET 2023 Odd Semester (SECTION-B)):** What are the effects of adding a pole and a zero in a system? *(Exact duplicate also on: Page 59, Q2 (CT#04 on EEE 3105 (Section: A)); Page 22, Row 5 (Question Analysis Table (Year 20)))*

26. **Page 34, Q.3(a) (RUET 2022 Odd Semester (Page 2 of 3)):** Prove that the maximum overshoot occurs at $t_m = \frac{\cos^{-1}\zeta}{\omega_n\sqrt{1-\zeta^2}}$ for the case of transient response analysis of a second order system with impulse excitation. Here, $\zeta$ is damping ratio and $\omega_n$ is undamped natural frequency.

27. **Page 37, Q.4(c) (RUET 2021 Odd Semester (Page 2/2)):** Write short notes about the followings: (i) Absolute stability, (ii) damping ratio, (iii) frequency response, (iv) under-damped system. *(Exact duplicate also on: Page 9, Row 10 (c) (Question Analysis Table (Year 18)))*

28. **Page 38, Q.4(a) (RUET 2020 Odd Examination (SECTION-A)):** Consider the closed-loop system given by $\frac{C(s)}{R(s)} = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ Determine the values of $\zeta$ and $\omega_n$ so that the system responds to a step input with approximately 5% overshoot and with a settling time of 2 sec (Use the 2% criterion). *(Exact duplicate also on: Page 21, Row 3 Q.4(a) (Question Analysis Table (Year 17)))*

29. **Page 39, Q.4(b) (RUET 2020 Odd Examination (Page 2/2)):** Write short notes about the followings: (a) critically damped system, (b) over damped system, (c) transition matrix, and (d) relative stability. *(Exact duplicate also on: Page 9, Row 13 (b) (Question Analysis Table (Year 17)))*

30. **Page 39, Q.5(a) (RUET 2020 Odd Examination (SECTION-B)):** What is damping ratio and natural angular frequency? Explain the effect of damping ratio on the unit step response of a typical second order system. *(Exact duplicate also on: Page 21, Row 4 (a) (Question Analysis Table (Year 17)))*

31. **Page 39, Q.5(b) (RUET 2020 Odd Examination (SECTION-B)):** When the system, shown in figure below, is subjected to a unit step input, the maximum overshoot and the peak time obtained are 25.4% and 3 sec, respectively. Determine the values of K and T. **[figure Involved]** *(Exact duplicate also on: Page 21, Row 5 (b) (Question Analysis Table (Year 17)); Page 57, Q1 (CT#02 on EEE 3105 (Section: B)))*

   ![[attachments/fig_p39_q_5_b.png]]

32. **Page 40, Q.3(a) (RUET 2018 Odd Semester (SECTION-A)):** Write short notes about the followings: (i) Undamped system, (ii) Overdamped system, (iii) Transition matrix, and (iv) Detour *(Exact duplicate also on: Page 9, Row 14 (a) (Question Analysis Table (Year 15)))*

33. **Page 41, Q.4(a) (RUET 2018 Odd Semester (Page 2)):** What is the effect of feedback on time constant of a control system? Draw a typical transient response output for an underdamped second order system and show the locations of all the transient response specifications. *(Exact duplicate also on: Page 21, Row 7 (a) (Question Analysis Table (Year 15)))*

34. **Page 41, Q.4(b) (RUET 2018 Odd Semester (Page 2)):** Explain the relationship between damping ratio and % overshoot. For a system having transfer function, $\frac{C(s)}{R(s)} = \frac{64}{s^2 + 5s + 64}$; determine: (i) $\omega_n$, (ii) $\zeta$, and (iii) $\omega_d$. *(Exact duplicate also on: Page 21, Row 7 (b) (Question Analysis Table (Year 15)))*

35. **Page 41, Q.4(c) (RUET 2018 Odd Semester (Page 2)):** Find the values of $K_1$ and $K_2$ so that $M_p = 25\%$ and $T_p = 4\text{s}$ for the control system shown in the following figure. Assume, unit step input. **[figure Involved]**

   ![[attachments/fig_p41_q_4_c.png]]

36. **Page 42, Q.2(a) (RUET 2017 Odd Semester (SECTION-A)):** Find the followings for the system shown below: (i) The equivalent single block that represents the transfer function, $T(s) = C(s)/R(s)$. (ii) The damping ratio, natural frequency, percent overshoot, settling time, peak time, rise time, and damped frequency of oscillation. **[figure Involved]**

   ![[attachments/fig_p42_q_2_a.png]]

37. **Page 42, Q.2(c) (RUET 2017 Odd Semester (SECTION-A)):** What is the difference between the natural frequency and the damped frequency of oscillation? *(Exact duplicate also on: Page 7, Q.(40) (Handwritten Theory Questions List))*

38. **Page 45, Q.3(b) (RUET 2016 Odd Semester (SECTION-A)):** Write short notes about the followings: (i) critically damped system, (ii) over damped system, and (iii) transition matrix.

39. **Page 46, Q.4(c) (RUET 2016 Odd Semester (Page 2)):** Design the value of gain K, for the following feedback control system, so that the system will respond with a 10% overshoot. **[figure Involved]**

   ![[attachments/fig_p46_q_4_c.png]]

40. **Page 46, Q.8(b) (RUET 2016 Odd Semester (SECTION-B)):** What is the effect of adding a pole and zero in a system? What is detouring?

41. **Page 48, Q.4(b) (RUET 2015 3rd Year 5th Semester (Page 2 of 2)):** A servo system is given by the following block diagram. Determine the value of $K_1$ and $K_2$, so that the maximum overshoot is 30% of a unit step response and the peak time is 2.2 sec. **[figure Involved]**

   ![[attachments/fig_p48_q_4_b.png]]

42. **Page 48, Q.4(c) (RUET 2015 3rd Year 5th Semester (Page 2 of 2)):** Explain the critically damped and overdamped conditions.

43. **Page 49, Q.6(a) (RUET 2015/Old Semester (Section-B cont.)):** Describe the effect of adding a pole and a zero to a closed-loop transfer function on system performance. *(Exact duplicate also on: Page 53, Q.5(c) (RUET 2013 3rd Year 6th Semester (SECTION B)))*

44. **Page 50, Q.3(b) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Define rise time and peak time. Show that the maximum % overshoot of a second order system for unit step response is $\% M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}} \times 100$.

45. **Page 50, Q.3(c) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** A system has shown in following figure. Determine the value of k, where the system has a damping ratio of $\zeta$ of [faint value, ~0.7] and undamped natural frequency $\omega_n$ of 4 rad/sec. **[figure Involved]**

   ![[attachments/fig_p50_q_3_c.png]]

46. **Page 51, Q.7(c) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** What are effects of adding poles and zeros in the system?

47. **Page 52, Q.3(c) (RUET 2013 3rd Year 6th Semester (SECTION A)):** Show graphically the unit step response of the second order system for different values of damping ratio.

48. **Page 53, Q.4(a) (RUET 2013 3rd Year 6th Semester (Page 2)):** Consider the system [shown in the figure below so] that the system has a damping ratio $\zeta$ of 0.7 and an undamped natural frequency $\omega_n$ of 4 rad/sec. Then obtain the rise time $t_r$, peak time $t_p$, maximum overshoot $M_p$ and settling time $t_s$ in the unit-step response. **[figure Involved]**

   ![[attachments/fig_p53_q_4_a.png]]

49. **Page 55, Q.1 (CT-02/21-Series/B-Section):** Consider the following system, (a) determine the Rise time($t_r$), Peak time($t_p$), maximum overshoot($M_p$) and the settling time($t_s$) in the unit step response. (b) Determine the steady state error for the unit-step response, unit-ramp response, unit-Parabolic response. $$\frac{C(s)}{R(s)} = \frac{9}{s^2+5s+9}$$

50. **Page 57, Q2 (CT#02 on EEE 3105 (Section: B)):** Write short notes on maximum overshoot and settling time with suitable figures.

51. **Page 59, Q1 (CT#03 on EEE 3105 (Section: A)):** What is meant by time response? Differentiate between critically damped and over-damped system.

52. **Page 61, Q1 (CT#02 on EEE 3105 (Section: B (21 Series))):** Prove that the expression of maximum overshoot of a second order dynamic system is $M_p = e^{-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}} \times 100$ where the symbols have their usual meaning.

53. **Page 64, Q1 (CT#02 on EEE 3105 (Section: A, 21 Series)):** A unity-feedback control system has the open-loop transfer function $$G(s) = \frac{K}{s(Ts+1)}$$ If the system responds to a unit step input with a peak time of 3 seconds and a maximum overshoot of 25.4%, determine the system parameters $K$ and $T$.

54. **Page 64, Q2 (CT#02 on EEE 3105 (Section: A, 21 Series)):** Derive the expression for the settling time of a second-order dynamic system in response to a unit step input, assuming a 4% tolerance band.

55. **Page 66, Q.1 (CT-03/20-Series/C-Section):** Discuss and draw with neat sketch the following terms: (i) undamped, (ii) underdamped, (iii) critical damped, (iv) overdamped, with roots positions

56. **Page 66, Q.2 (CT-03/20-Series/C-Section):** Show that the rise time $t_r = \frac{\pi - \beta}{\omega_d}$, where symbols have their usual meanings.

57. **Page 69, Q2 (Class Test (Page 2)):** Differentiate between over damped and critically damped system.

### **Steady-State Errors & Static Error Constants**

58. **Page 2, Q.(06) (Handwritten Theory Questions List):** Define steady-state error.

59. **Page 14, Row 6 (clipped) (Question Analysis Table (Year 19)):** Evaluate the dynamic error co-efficient when the system is subjected to r(t). [Partially clipped in table scan]

60. **Page 21, Row 6 (c) (Question Analysis Table (Year 17)):** Evaluate the dynamic error co-efficients whose $G(s) = \frac{10}{0.1s^2 + 10s}$ and $H(s) = 1$ Input $r(t) = A_0 + A_1 t + \frac{A_2}{2}t^2$.

61. **Page 23, Row 5 (Question Analysis Table (Year 21)):** In steady state curve, find the following system's steady state error value for different input types. **[figure Involved]**

   ![[attachments/fig_p23_row_5.png]]

62. **Page 32, Q.4(c) (RUET 2023 Odd Semester (Page 2/2)):** Define steady-state error. Find the steady-state error of the following system for different types of inputs. **[figure Involved]** *(Exact duplicate also on: Page 23, Row 6 (Question Analysis Table (Year 20)))*

   ![[attachments/fig_p32_q_4_c.png]]

63. **Page 34, Q.3(b) (RUET 2022 Odd Semester (Page 2 of 3)):** Find the steady-state error of the following system for unit step input. **[figure Involved]** *(Exact duplicate also on: Page 24, Row 1 (Fig. 3b) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p34_q_3_b.png]]

64. **Page 34, Q.4(a) (RUET 2022 Odd Semester (Page 2 of 3)):** Consider the system whose $G(s) = \frac{10}{0.1s^2 + 10s}$, $H(s) = 1$ and $r(t) = A_0 + A_1 t + \frac{A_2}{2}t^2$. Evaluate the dynamic error co-efficient when the system is subjected to $r(t)$. *(Exact duplicate also on: Page 20, Row 8 (Question Analysis Table (Year 19)))*

65. **Page 36, Q.3(c) (RUET 2021 Odd Semester (SECTION-A)):** Define steady-state error. Find the steady-state error of the following system for different types of inputs. **[figure Involved]** *(Exact duplicate also on: Page 24, Row 2 (c) (Question Analysis Table (Year 18)))*

   ![[attachments/fig_p36_q_3_c.png]]

66. **Page 38, Q.3(c) (RUET 2020 Odd Examination (SECTION-A)):** Consider a unity feedback control system with the closed-loop transfer function $$\frac{C(s)}{R(s)} = \frac{Ks+b}{s^2+as+b}$$ Determine the open-loop transfer function. Also determine the steady-state error for the unit ramp response. *(Exact duplicate also on: Page 12, Row 7 (c) (Question Analysis Table (Year 17)); Page 24, Row 3 (c) (Question Analysis Table (Year 17)))*

67. **Page 39, Q.5(c) (RUET 2020 Odd Examination (SECTION-B)):** Evaluate the dynamic error co-efficients whose $G(s) = \frac{10}{0.1s^2+10s}$ and $H(s) = 1$ Input $r(t) = A_0 + A_1 t + \frac{A_2}{2}t^2$.

68. **Page 43, Q.4(b) (RUET 2017 Odd Semester (Page 2)):** A unity feedback system has the following forward transfer function. $$G(s) = \frac{K(s+2)}{(s+14)(s+18)}$$ Find the value of K to yield a 10% error in the steady state?

69. **Page 43, Q.4(c) (RUET 2017 Odd Semester (Page 2)):** Find the system type of the following system. **[figure Involved]**

   ![[attachments/fig_p43_q_4_c.png]]

70. **Page 45, Q.3(c) (RUET 2016 Odd Semester (SECTION-A)):** What is damping? Consider a unity feedback control system with the closed-loop transfer function $$\frac{C(s)}{R(s)} = \frac{Ks+b}{s^2+as+b}$$ Determine the open-loop transfer function. Also, determine the steady state error for the unit ramp response.

71. **Page 48, Q.4(a) (RUET 2015 3rd Year 5th Semester (Page 2 of 2)):** Define steady state error. A unit feedback control system has the following transfer function $$G(s) = \frac{K_1}{s(s+1)(0.5s+1)}.$$ Determine the steady state error for the input $r(t) = 3t$ and $K_1 = 3$.

72. **Page 51, Q.5(a) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Define steady state error, find the steady state error of the following system for different types of inputs. **[figure Involved]**

   ![[attachments/fig_p51_q_5_a.png]]

73. **Page 66, Q.3 (CT-03/20-Series/C-Section):** Find out dynamics error coefficients and dynamic series of the system the system having $G(s) = \frac{100}{s(s+10)}$ and $H(s) = 1$ for the inputs $r(t) = A + At^3$

### **Control of Transient Response & Basic Control Actions**

74. **Page 3, Q.(09) (Handwritten Theory Questions List):** Integral control provides better improvement over proportional control in terms of elimination of steady-state error. Mathematically prove it.

75. **Page 25, Row 1b (Question Analysis Table (Year 21)):** "Integral control provides better improvement over proportional control in terms of elimination of steady-state error." Mathematically prove it.

76. **Page 35, Q.8(c) (RUET 2022 Odd Semester (Page 3 of 3)):** Explain the effectiveness of integral controller over proportional control for compensating steady-state error. *(Exact duplicate also on: Page 25, Row 4 (Question Analysis Table (Year 19)))*

77. **Page 37, Q.5(c) (RUET 2021 Odd Semester (SECTION-B)):** "Integral control provides better improvement over proportional control in terms of elimination of steady-state error"- Mathematically prove it. *(Exact duplicate also on: Page 25, Row 5 (c) (Question Analysis Table (Year 18)))*

78. **Page 59, Q1 (CT#04 on EEE 3105 (Section: A)):** Explain the effectiveness of PD controller over P controller to control a system with inertia load with suitable block diagram and response curves for unit-step input.

79. **Page 62, Q.1 (CT#03 on EEE 3105 (Section: A)):** Mathematically justify the effectiveness of an integral controller compared to a proportional-derivative controller in compensating for steady-state error.
