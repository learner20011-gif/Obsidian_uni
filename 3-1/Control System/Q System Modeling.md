# EEE 3105 — System Modeling (PYQ)

**Syllabus:** Transfer function, Signal flow graph, State-space, Transfer function to state variable and state variable to transfer function, Mathematical modeling of mechanical, electrical and electro-mechanical systems.

---

### **Transfer Function & Block Diagram Reduction**

1. **Page 2, Q.(02) (Handwritten Theory Questions List):** Derive the transfer function of a closed-loop system when the open loop transfer function is equal to the feedforward transfer function.

2. **Page 4, Q.(20) (Handwritten Theory Questions List):** What is transfer function?

3. **Page 5, Q.(29) (Handwritten Theory Questions List):** What assumption is made concerning initial conditions when dealing with transfer functions.

4. **Page 17, Row 2 (Question Analysis Table (Year 21)):** Determine the ratio $C(s)/R(s)$ for the following system using block diagram reduction method. **[figure Involved]**

   ![[attachments/fig_p17_row_2.png]]

5. **Page 33, Q.1(b) (RUET 2022 Odd Semester (SECTION-A)):** Prove that the output of the closed loop system clearly depends on both the closed-loop transfer function and the nature of the input. *(Exact duplicate also on: Page 9, Row 7b (Question Analysis Table (Year 19, SECTION-A)))*

6. **Page 33, Q.2(b) (RUET 2022 Odd Semester (SECTION-A)):** Determine the ratio $\frac{C(s)}{R(s)}$ for the following system using block diagram reduction method. **[figure Involved]** *(Exact duplicate also on: Page 14, Row 5 (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p33_q_2_b.png]]

7. **Page 36, Q.1(b) (RUET 2021 Odd Semester (SECTION-A)):** Derive the transfer function of a closed-loop system when the open-loop transfer function is equal to the feedforward transfer function. *(Exact duplicate also on: Page 12, Row 3 (b) (Question Analysis Table (Year 18)))*

8. **Page 36, Q.2(b) (RUET 2021 Odd Semester (SECTION-A)):** Determine the ratio $C(s)/R(s)$ for the following system using block diagram reduction method. **[figure Involved]** *(Exact duplicate also on: Page 17, Row 4 (b) (p.17-18) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p36_q_2_b.png]]

9. **Page 38, Q.1(b) (RUET 2020 Odd Examination (SECTION-A)):** What is meant by automatic control? Prove that the output of the closed-loop system clearly depends on both the closed-loop transfer function and the nature of the input. *(Exact duplicate also on: Page 12, Row 5 (b) (Question Analysis Table (Year 17)))*

10. **Page 40, Q.2(a) (RUET 2018 Odd Semester (SECTION-A)):** Define transfer function. What assumption is made concerning initial conditions when dealing with transfer functions? *(Exact duplicate also on: Page 13, Row 2 (a) (Question Analysis Table (Year 15)))*

11. **Page 43, Q.5(c) (RUET 2017 Odd Semester (SECTION-B)):** Reduce the following system to a single transfer function, $T(s) = C(s)/R(s)$. **[figure Involved]**

   ![[attachments/fig_p43_q_5_c.png]]

12. **Page 45, Q.2(a) (RUET 2016 Odd Semester (SECTION-A)):** Prove that the output of the closed-loop system clearly depends on both the closed-loop transfer function and the nature of input. *(Exact duplicate also on: Page 8, Q.(45) (Handwritten Theory Questions List))*

13. **Page 45, Q.4(b) (RUET 2016 Odd Semester (SECTION-A)):** Find the equivalent transfer function, $T(s) = \frac{C(s)}{R(s)}$, for the following system. **[figure Involved]**

   ![[attachments/fig_p45_q_4_b.png]]

14. **Page 47, Q.2(c) (RUET 2015 3rd Year 5th Semester (SECTION-A)):** Obtain transfer functions $C(s)/R(s)$ and $C(s)/D(s)$ of the system shown in the following figure. **[figure Involved]**

   ![[attachments/fig_p47_q_2_c.png]]

15. **Page 50, Q.2(b) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Find out the transfer function by using block diagram representation method. **[figure Involved]**

   ![[attachments/fig_p50_q_2_b.png]]

16. **Page 52, Q.3(a) (RUET 2013 3rd Year 6th Semester (SECTION A)):** Find out the transfer function $Y(s) = \frac{V(s)}{R(s)}$ by using block diagram simplification method **[figure Involved]**

   ![[attachments/fig_p52_q_3_a.png]]

17. **Page 58, Q1 (CT#01 on EEE 3105):** Prove that the output of the closed-loop system clearly depends on both the closed-loop transfer function and the nature of the input.

18. **Page 65, Q.1 (CT-02 (20 Series, C-Section)):** Findout Transfer function $Y/R$ by block diagram representation method **[figure Involved]**

   ![[attachments/fig_p65_q_1.png]]

### **Signal Flow Graph & Mason's Gain Formula**

19. **Page 8, Q.(47) (Handwritten Theory Questions List):** State Mason's rule.

20. **Page 18, Row 2 (Question Analysis Table (Year 21)):** For the given signal flow graph find $C(S)/R(S)$. **[figure Involved]**

   ![[attachments/fig_p18_row_2.png]]

21. **Page 31, Q.3(a) (RUET 2023 Odd Semester (SECTION-A)):** What is the importance of signal flow graph? *(Exact duplicate also on: Page 18, Row 3 (a) (Question Analysis Table (Year 20)))*

22. **Page 31, Q.3(b) (RUET 2023 Odd Semester (SECTION-A)):** For the given signal flow graph find the ration $C(s)/R(s)$. **[figure Involved]** *(Exact duplicate also on: Page 18, Row 3 (b) (Question Analysis Table (Year 20)))*

   ![[attachments/fig_p31_q_3_b.png]]

23. **Page 33, Q.2(c) (RUET 2022 Odd Semester (SECTION-A)):** For the given signal flow graph find $\frac{C(s)}{R(s)}$. **[figure Involved]** *(Exact duplicate also on: Page 18, Row 4 (Fig. 2c, p.18-19) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p33_q_2_c.png]]

24. **Page 36, Q.2(a) (RUET 2021 Odd Semester (SECTION-A)):** What is signal flow graph? Describe the importance of signal flow graph in control system. *(Exact duplicate also on: Page 19, Row 2 (a) (Question Analysis Table (Year 18)); Page 2, Q.(05) (Handwritten Theory Questions List))*

25. **Page 36, Q.2(c) (RUET 2021 Odd Semester (SECTION-A)):** For the given signal flow graph find $C(s)/R(s)$. **[figure Involved]** *(Exact duplicate also on: Page 19, Row 3 (c) (Question Analysis Table (Year 18)))*

   ![[attachments/fig_p36_q_2_c.png]]

26. **Page 38, Q.3(b) (RUET 2020 Odd Examination (SECTION-A)):** Determine $C(s)/R(s)$ of the following system by using Mason's rule. **[figure Involved]** *(Exact duplicate also on: Page 19, Row 4 (b) (Question Analysis Table (Year 17)))*

   ![[attachments/fig_p38_q_3_b.png]]

27. **Page 40, Q.3(b) (RUET 2018 Odd Semester (SECTION-A)):** State how type and order of a control system is determined? Obtain the transfer function $C/R$ from the signal flow graph shown in the following figure. **[figure Involved]** *(Exact duplicate also on: Page 19, Row 5 (b) (Question Analysis Table (Year 15)))*

   ![[attachments/fig_p40_q_3_b.png]]

28. **Page 42, Q.2(b) (RUET 2017 Odd Semester (SECTION-A)):** Draw an SFG for the following state equation. $$\dot{x} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 3 & 1 \\ -2 & -4 & -4 \end{bmatrix} x + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} r; \quad y = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix} x$$ [Note: B vector and some matrix entries are partially faded in the original photocopy.]

29. **Page 42, Q.3(b) (RUET 2017 Odd Semester (SECTION-A)):** State Mason's rule. Determine $C(s)/R(s)$ of the following system by using Mason's rule. **[figure Involved]**

   ![[attachments/fig_p42_q_3_b.png]]

30. **Page 45, Q.3(a) (RUET 2016 Odd Semester (SECTION-A)):** State Mason's rule. Determine $C(s)/R(s)$ of the following system by using Mason's rule. **[figure Involved]**

   ![[attachments/fig_p45_q_3_a.png]]

31. **Page 47, Q.2(b) (RUET 2015 3rd Year 5th Semester (SECTION-A)):** Write down Mason's gain formula. Find the transfer function, $C(s)/R(s)$, for signal flow graph in Fig. 2(b) using Mason's gain formula. **[figure Involved]**

   ![[attachments/fig_p47_q_2_b.png]]

32. **Page 47, Q.3(a) (RUET 2015 3rd Year 5th Semester (SECTION-A)):** Draw the block diagram and find out the transfer function $C(s)/R(s)$ of the following system by using block diagram representation method. **[figure Involved]**

   ![[attachments/fig_p47_q_3_a.png]]

33. **Page 50, Q.2(c) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Define forward path & nontouching loop. State the Mason's rule.

34. **Page 50, Q.3(a) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Consider the following system. Determine the $\frac{Y_6}{Y_1}$, $\frac{Y_4}{Y_1}$, & $\frac{Y_3}{Y_1}$ by using Mason's rule. **[figure Involved]**

   ![[attachments/fig_p50_q_3_a.png]]

35. **Page 53, Q.4(b) (RUET 2013 3rd Year 6th Semester (Page 2)):** In connection to signal flow graph (SFG) define Non-touching loops, self loop, mixed node.

36. **Page 53, Q.4(c) (RUET 2013 3rd Year 6th Semester (Page 2)):** Draw the signal flow graph and determine transfer function by using Mason's gain formula for the following block diagram. **[figure Involved]**

   ![[attachments/fig_p53_q_4_c.png]]

37. **Page 55, Q.2 (CT-02/21-Series/B-Section):** Draw the signal flow graph, find out the transfer function using Mason's Rule. **[figure Involved]**

   ![[attachments/fig_p55_q_2.png]]

38. **Page 65, Q.2 (CT-02 (20 Series, C-Section)):** Draw the signal Flow graph. Find out transfer function by Mason's Rule. **[figure Involved]**

   ![[attachments/fig_p65_q_2.png]]

### **State-Space Representation & State Transition Matrix**

39. **Page 4, Q.(23) (Handwritten Theory Questions List):** Define state and state vector.

40. **Page 4, Q.(24) (Handwritten Theory Questions List):** Define eigen values and eigen vectors.

41. **Page 8, Q.(46) (Handwritten Theory Questions List):** Differentiate between transfer function and state-space.

42. **Page 34, Q.4(b) (RUET 2022 Odd Semester (Page 2 of 3)):** Define state transition matrix. Prove that, $\varphi(t) = \mathcal{L}^{-1}[(sI - A)^{-1}]$, where symbols have their usual meanings. *(Exact duplicate also on: Page 14, Row 7 (b) (p.14-15) (Question Analysis Table (Year 19)))*

43. **Page 34, Q.5(b) (RUET 2022 Odd Semester (SECTION-B)):** Define state vector. Find out the eigen values and eigen vector of the following system. $$A = \begin{bmatrix} 0.5 & 1 \\ 0 & 2 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = [0]$$ Is this system controllable or not? *(Exact duplicate also on: Page 15, Row 3 (Question Analysis Table (Year 19)); Page 30, Row 2 (Question Analysis Table (Year 19)))*

44. **Page 48, Q.5(a) (RUET 2015 3rd Year 5th Semester (Section-B)):** Consider the following system: $$A = \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}; \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}; \quad C = \begin{bmatrix} 1 & 1 \end{bmatrix}; \quad D = [0]$$ (i) Find out Eigen values and Eigen vectors. (ii) Is this system controllable?

45. **Page 51, Q.4(b) (RUET 2014 3rd Year 6th Semester (Page 2 of 2)):** Define state vector and state transition matrix.

46. **Page 51, Q.5(b) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Consider a linear control system $$\dot{x}_1 = -x_1 + 2u$$ $$\dot{x}_2 = -2x_2 + u$$ $$y_1 = -3x_1$$ $$y_2 = x_1 + x_2$$ [Note: signs/coefficients on y1, y2 are partially faded in the scan] (i) Determine Eigen values and Eigen vectors. (ii) Determine state transition matrix.

47. **Page 53, Q.5(b) (RUET 2013 3rd Year 6th Semester (SECTION B)):** Consider a linear control system given by the following state space model. $$\dot{x} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix} x + \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix} u \qquad y = \begin{bmatrix} 1 & -1 & 1 \end{bmatrix} x$$ (i) Determine the characteristic values (eigen values) of the system. (ii) Determine the controllability of the system.

48. **Page 56, Q.2 (CT-03/21-Series/B-Section):** For the following systems $$A = \begin{bmatrix} -1 & 0 \\ 3 & 2 \end{bmatrix}; \quad B = \begin{bmatrix} 0 \\ 2 \end{bmatrix}; \quad C = \begin{bmatrix} 4 & 0 \end{bmatrix}; \quad D = [0]$$ i) Draw a state diagram. ii) Find the transfer function. iii) Find the eigen values and eigen vectors. iv) Determine the state transition matrix. v) Is this system controllable or not?

### **Transfer Function to State Variable & State Variable to Transfer Function**

49. **Page 12, Row 4 Q.5(a) (Question Analysis Table (Year 18)):** Consider the following system: $$A = \begin{bmatrix} 1 & -1 \\ 0 & -1 \end{bmatrix}; \quad B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}; \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}; \quad D = \begin{bmatrix} 0 \end{bmatrix}$$ (i) Find out the transfer function. (ii) Determine eigen values and eigen vectors.

50. **Page 15, Row 6 Q.5(a) (Question Analysis Table (Year 18)):** Consider the following system: $$A = \begin{bmatrix} 1 & -1 \\ 0 & -1 \end{bmatrix}; \quad B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}; \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}; \quad D = [0]$$ (i) Find out the transfer function. (ii) Determine eigen values and eigen vectors.

51. **Page 37, Q.5(a) (RUET 2021 Odd Semester (SECTION-B)):** Consider the following system: $$A = \begin{bmatrix} 1 & -1 \\ 0 & -1 \end{bmatrix}; \quad B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}; \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix} \quad D = [0]$$ (i) Find out the transfer function. (ii) Determine eigen values and eigen vectors.

52. **Page 38, Q.2(c) (RUET 2020 Odd Examination (SECTION-A)):** Obtain the transfer function of the system defined by the following state-space equations: $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -5 & -25 & -5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 0 \\ 25 \\ -120 \end{bmatrix} u; \quad y = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + [0]u;$$ *(Exact duplicate also on: Page 15, Row 7 (c) (Question Analysis Table (Year 17)))*

53. **Page 51, Q.4(c) (RUET 2014 3rd Year 6th Semester (Page 2 of 2)):** Obtain the state space representation of the following system. **[figure Involved]**

   ![[attachments/fig_p51_q_4_c.png]]

54. **Page 68, Q.1 (Handwritten) (Faruk Sir CT):** $$A = \begin{bmatrix} -1 & 2 \\ 0 & 1 \end{bmatrix} \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix} \quad D = [0]$$ (i) Derive state Diagram & Transfer function (ii) Construct state transition Matrix. (iii) Find Eigen values and Eigen Vector (iv) Is the system observeable?

55. **Page 69, Q3 (Class Test (Page 2)):** Write the expression of transfer function in terms of the state-space elements.

### **Mathematical Modeling of Mechanical, Electrical, and Electro-Mechanical Systems**

56. **Page 2, Q.(03) (Handwritten Theory Questions List):** Express the dynamics of a mass-spring damper system in state space form. Also represent it in block diagram form.

57. **Page 5, Q.(28) (Handwritten Theory Questions List):** Derive the transfer function of a DC motor when $V_i(s)$ is input, $\theta(s)$ is output. Also express the transfer function in terms of the state-space elements.

58. **Page 14, Row 1 (Question Analysis Table (Year 21)):** What is state-space representation? Represent the dynamics of a DC motor in state-space form.

59. **Page 14, Row 2 (Question Analysis Table (Year 21)):** Find the state-space equations of the given circuit, where the outputs are the current through the resistor and the voltage across the inductor. **[figure Involved]**

   ![[attachments/fig_p14_row_2.png]]

60. **Page 17, Row 1 (Question Analysis Table (Year 21)):** Draw the block diagram of the following network. Is this system an open loop or a closed loop control system? Explain why? **[figure Involved]**

   ![[attachments/fig_p17_row_1.png]]

61. **Page 31, Q.1(c) (RUET 2023 Odd Semester (SECTION-A)):** Draw the block diagram and determine the transfer function of the following circuit. **[figure Involved]** *(Exact duplicate also on: Page 17, Row 3 (Question Analysis Table (Year 20)))*

   ![[attachments/fig_p31_q_1_c.png]]

62. **Page 31, Q.2(b) (RUET 2023 Odd Semester (SECTION-A)):** Find the state-space equation of the following circuit when the outputs are the current through the resistor and voltage across the capacitor. **[figure Involved]** *(Exact duplicate also on: Page 14, Row 3 (Question Analysis Table (Year 20)))*

   ![[attachments/fig_p31_q_2_b.png]]

63. **Page 33, Q.1(c) (RUET 2022 Odd Semester (SECTION-A)):** Show the open loop transfer function for the DC servomotor is $$\frac{\omega_o(s)}{v_i(s)} = \frac{k_t k_f}{R_f R_a (1+s\tau_a)(1+s\tau_f)[s] + \frac{k_b k_t}{R_a(1+s\tau_a)}]$$ Where, $\tau_a = \frac{L_a}{R_a}$; $\tau_f = \frac{L_f}{R_f}$; $k_f =$ generator constant, volts/field amp; $k_t =$ motor torque constant, N-m/armature amp; $k_b =$ motor emf constant, volt/rad/sec, and $J =$ total inertia of the load & motor, kg-m$^2$. **[figure Involved]** *(Exact duplicate also on: Page 11, Row 4 (Fig. 1c) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p33_q_1_c.png]]

64. **Page 33, Q.2(a) (RUET 2022 Odd Semester (SECTION-A)):** What is state-space? Represent the dynamics of mass-spring-damper system in state-space term. *(Exact duplicate also on: Page 14, Row 4 (Question Analysis Table (Year 19)))*

65. **Page 34, Q.3(c) (RUET 2022 Odd Semester (Page 2 of 3)):** Determine the transfer function of the following system- **[figure Involved]** *(Exact duplicate also on: Page 11, Row 5 (Fig. 3c, p.11-12) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p34_q_3_c.png]]

66. **Page 34, Q.5(a) (RUET 2022 Odd Semester (SECTION-B)):** For the following electrical network find a state-space representation if the output is the voltage across the capacitor and the resistor. **[figure Involved]** *(Exact duplicate also on: Page 15, Row 2 (a) (Question Analysis Table (Year 19, SECTION-B)))*

   ![[attachments/fig_p34_q_5_a.png]]

67. **Page 36, Q.1(c) (RUET 2021 Odd Semester (SECTION-A)):** Express the dynamics of a mass-spring-damper system in state-space form. Also represent it in block diagram form. *(Exact duplicate also on: Page 15, Row 4 (c) (Question Analysis Table (Year 18)))*

68. **Page 36, Q.3(b) (RUET 2021 Odd Semester (SECTION-A)):** Find the state-space of the following circuit when the outputs are the voltage across the capacitor and current through the inductor. **[figure Involved]** *(Exact duplicate also on: Page 15, Row 5 (b) (Question Analysis Table (Year 18)))*

   ![[attachments/fig_p36_q_3_b.png]]

69. **Page 38, Q.1(c) (RUET 2020 Odd Examination (SECTION-A)):** Express the dynamics of a dc motor in state-space form. Also express it in transfer function form in terms of the state-space elements. *(Exact duplicate also on: Page 12, Row 5 (c) (Question Analysis Table (Year 17)))*

70. **Page 38, Q.2(b) (RUET 2020 Odd Examination (SECTION-A)):** Define transfer function. Find the transfer function, $I_1(s)/V(s)$ of the following circuit. **[figure Involved]** *(Exact duplicate also on: Page 12, Row 6 (b) (Question Analysis Table (Year 17)))*

   ![[attachments/fig_p38_q_2_b.png]]

71. **Page 39, Q.4(c) (RUET 2020 Odd Examination (Page 2/2)):** Find the state-space equation of the following circuit when the output current is taken through the resistor. **[figure Involved]** *(Exact duplicate also on: Page 15, Row 8 (c) (p.15-16) (Question Analysis Table (Year 17)))*

   ![[attachments/fig_p39_q_4_c.png]]

72. **Page 40, Q.1(b) (RUET 2018 Odd Semester (SECTION-A)):** Derive the transfer function of a DC motor when $V_i(s)$ is the input, $\theta(s)$ is the output of the system. Also, express the transfer function in terms of the state-space elements. *(Exact duplicate also on: Page 12, Row 8 (b) (Question Analysis Table (Year 15, SECTION-A)))*

73. **Page 40, Q.2(b) (RUET 2018 Odd Semester (SECTION-A)):** Find the transfer function, $V_o(s)/V_i(s)$, for the following circuit. **[figure Involved]** *(Exact duplicate also on: Page 13, Row 2 (b) (Question Analysis Table (Year 15)))*

   ![[attachments/fig_p40_q_2_b.png]]

74. **Page 40, Q.2(c) (RUET 2018 Odd Semester (SECTION-A)):** Find the state-space model of the following circuit when the output is the current through the capacitor. **[figure Involved]** *(Exact duplicate also on: Page 16, Row 2 (c) (Question Analysis Table (Year 15)))*

   ![[attachments/fig_p40_q_2_c.png]]

75. **Page 42, Q.1(c) (RUET 2017 Odd Semester (SECTION-A)):** Represent the dynamics of a DC motor in a block diagram form which is compatible in SIMULINK platform.

76. **Page 42, Q.3(c) (RUET 2017 Odd Semester (SECTION-A)):** Find the state-space representation of the electrical network shown in the figure below. The output is $v_o(t)$. **[figure Involved]**

   ![[attachments/fig_p42_q_3_c.png]]

77. **Page 44, Q.8(a) (RUET 2017 Odd Semester (Page 3)):** Draw the block diagram representation of the following system. **[figure Involved]**

   ![[attachments/fig_p44_q_8_a.png]]

78. **Page 45, Q.1(b) (RUET 2016 Odd Semester (SECTION-A)):** Derive the transfer function of a DC motor when $V_i(s)$ is the input and $\omega(s)$ is the output of the system. Also, express the transfer function in terms of the state-space elements.

79. **Page 45, Q.2(b) (RUET 2016 Odd Semester (SECTION-A)):** Differentiate between transfer function and state-space. Find the state-space of the following circuit when the output is the current through the resistor. **[figure Involved]**

   ![[attachments/fig_p45_q_2_b.png]]

80. **Page 45, Q.2(c) (RUET 2016 Odd Semester (SECTION-A)):** Find the transfer function, $I_2(s)/V(s)$ of the following circuit. **[figure Involved]**

   ![[attachments/fig_p45_q_2_c.png]]

81. **Page 47, Q.1(c) (RUET 2015 3rd Year 5th Semester (SECTION-A)):** Determine the transfer function and draw the block diagram of the following circuit. **[figure Involved]**

   ![[attachments/fig_p47_q_1_c.png]]

82. **Page 48, Q.3(b) (RUET 2015 3rd Year 5th Semester (Page 2 of 2)):** Draw the electric analogous circuit and find $X_o(s)/X_i(s)$ for the following figure. **[figure Involved]**

   ![[attachments/fig_p48_q_3_b.png]]

83. **Page 50, Q.1(c) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Define the block diagram and transfer function. For the following system, show that the open loop transfer function $$\frac{\omega_o(s)}{V_i(s)} = \frac{k_t k_f}{R_f R_a (1+s\tau_f)(1+s\tau_a)\left[sJ + \frac{k_t k_b}{R_a(1+s\tau_a)}\right]}$$ Where, $\tau_a = \frac{L_a}{R_a}$, & $\tau_f = \frac{L_f}{R_f}$, $k_f =$ generator constant, $k_b =$ motor emf constant, $k_t =$ motor torque constant and $J =$ total inertia of the load and motor. **[figure Involved]**

   ![[attachments/fig_p50_q_1_c.png]]

84. **Page 50, Q.2(a) (RUET 2014 3rd Year 6th Semester (SECTION-A)):** Obtain the transfer function $\frac{X_1(s)}{U(s)}$ and $\frac{X_2(s)}{U(s)}$ of the mechanical system shown in following figure. **[figure Involved]**

   ![[attachments/fig_p50_q_2_a.png]]

85. **Page 52, Q.2(b) (RUET 2013 3rd Year 6th Semester (SECTION A)):** Find out the transfer function of a armature control d.c motor shown in figure below. **[figure Involved]**

   ![[attachments/fig_p52_q_2_b.png]]

86. **Page 52, Q.3(b) (RUET 2013 3rd Year 6th Semester (SECTION A)):** Draw the block diagram of the circuit shown below **[figure Involved]**

   ![[attachments/fig_p52_q_3_b.png]]

87. **Page 53, Q.5(a) (RUET 2013 3rd Year 6th Semester (SECTION B)):** Draw the free body diagram of the following system and obtain a state-space representation of the system. **[figure Involved]**

   ![[attachments/fig_p53_q_5_a.png]]

88. **Page 55, Q.4 (Class Test-01):** Draw the block diagram and find out the transfer function $T(s) = \frac{\omega_0(s)}{V_f(s)}$. **[figure Involved]**

   ![[attachments/fig_p55_q_4.png]]

89. **Page 56, Q.2 (second) (CT-01 (20 Series, C-Section)):** Define Block diagram and Transfer function. Find the equivalent transfer function $\theta(s)/V_a(s)$ of the following system. **[figure Involved]**

   ![[attachments/fig_p56_q_2_second.png]]

90. **Page 57, Q2 (CT#01 on EEE 3105):** Find the transfer function, $I_1(s)/V(s)$ of the following circuit. **[figure Involved]**

   ![[attachments/fig_p57_q2.png]]

91. **Page 58, Q2 (CT#01 on EEE 3105):** Define transfer function. Determine the transfer function of the following system **[figure Involved]**

   ![[attachments/fig_p58_q2.png]]

92. **Page 58, Q1 (CT#02 on EEE 3105 (Section: A)):** Find the state-space equation of the following circuit when the outputs are the voltages across the resistor and the capacitor. **[figure Involved]**

   ![[attachments/fig_p58_q1.png]]

93. **Page 58, Q2 (CT#02 on EEE 3105 (Section: A)):** Express the dynamic of a mass-spring-damper system in conventional technique using the elements of modern control technique.

94. **Page 60, Q2 (CT#01 on EEE 3105 (Section: B (21 Series))):** Determine the transfer function of the following system when the output is the current through the resistor. **[figure Involved]** *(Exact duplicate also on: Page 65, Q2 (CT#01 on EEE 3105 (Section: B, 21 Series)))*

   ![[attachments/fig_p60_q2.png]]

95. **Page 63, Q2 (CT#01 on EEE 3105 (Section: A, 21 Series)):** Determine the transfer function $\frac{V(s)}{I(s)}$ of the following system **[figure Involved]**

   ![[attachments/fig_p63_q2.png]]
