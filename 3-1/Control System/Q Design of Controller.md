# EEE 3105 — Design of Controller (PYQ)

**Syllabus:** Introduction of controller, Controllability, Observability, PID controller design, PID tuning, Lead-lag compensator, Pole placement technique, and Introduction to non-linear control system.

---

### **Introduction to Controllers, Controllability, and Observability**

1. **Page 4, Q.(21) (Handwritten Theory Questions List):** What is observer?

2. **Page 29, Row 7 (Question Analysis Table (Year 21)):** For control system design purpose check the controllability and observability of the following system. $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 3 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$$ $$\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$

3. **Page 31, Q.2(c) (RUET 2023 Odd Semester (SECTION-A)):** Consider the system defined by $$\begin{bmatrix} \dot{x}_1(t) \\ \dot{x}_2(t) \\ \dot{x}_3(t) \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} u(t); \quad y(t) = \begin{bmatrix} 4 & 5 & 1 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{bmatrix} + [0]u(t).$$ Is the system completely observable? *(Exact duplicate also on: Page 29, Row 8 (c) (p.29-30) (Question Analysis Table (Year 20)))*

4. **Page 36, Q.3(a) (RUET 2021 Odd Semester (SECTION-A)):** A single input single output system is given as - $$\dot{x}(t) = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix} x(t) + \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} u(t); \quad y(t) = \begin{bmatrix} 1 & 0 & 2 \end{bmatrix} x(t)$$ Test for controllability and observability. *(Exact duplicate also on: Page 30, Row 3 (a) (Question Analysis Table (Year 18)))*

5. **Page 38, Q.3(a) (RUET 2020 Odd Examination (SECTION-A)):** What is actuator? Find the value of $K$ for which the following system will be uncontrollable. $$\begin{bmatrix} \dot{x}_1(t) \\ \dot{x}_2(t) \end{bmatrix} = \begin{bmatrix} -1 & 0.4 \\ K & -1.2 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + \begin{bmatrix} -1 \\ 2 \end{bmatrix} u; \quad y(t) = \begin{bmatrix} 1 & 3 \end{bmatrix} \begin{bmatrix} x_1(t) \\ x_2(t) \end{bmatrix} + [0]u$$ *(Exact duplicate also on: Page 30, Row 4 Q.3(a) (Question Analysis Table (Year 17)))*

6. **Page 43, Q.4(a) (RUET 2017 Odd Semester (Page 2)):** Find the controllability and observability of the following system where $v_i(t)$ is input and $v_o(t)$ is output. **[figure Involved]**

   ![[attachments/fig_p43_q_4_a.png]]

7. **Page 48, Q.5(c) (RUET 2015 3rd Year 5th Semester (Section-B)):** What is asymptote? Consider the system shown in the following figure and investigate whether it is observable or not. **[figure Involved]**

   ![[attachments/fig_p48_q_5_c.png]]

8. **Page 49, Q.6(c) (RUET 2015/Old Semester (Section-B cont.)):** Test the controllability and observability of a system when $$A = \begin{bmatrix} -0.5 & 0 \\ 0 & -2 \end{bmatrix}; \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}; \quad C = \begin{bmatrix} 0 & 1 \end{bmatrix}; \quad D = [0]$$

9. **Page 62, Q.2 (CT#03 on EEE 3105 (Section: A)):** Consider the system defined by $$\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \\ \dot{x}_3 \end{bmatrix} = \begin{bmatrix} -1 & -2 & -2 \\ 0 & -1 & 1 \\ 1 & 0 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix} u; \quad y = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + [0]u;$$ Is the system completely state controllable?

### **PID Controller Design & PID Tuning**

10. **Page 5, Q.(27) (Handwritten Theory Questions List):** What are the advantages of using PID controller over PI and PD controllers?

11. **Page 6, Q.(35) (Handwritten Theory Questions List):** Draw a PID controller and write down the controller expression. How will you select between PI, PD and PID controller when used as compensators?

12. **Page 32, Q.7(a) (RUET 2023 Odd Semester (SECTION-B)):** Draw the PI, PD and PID controller with op-amp and write down the controller expression. *(Exact duplicate also on: Page 25, Row 2 (Question Analysis Table (Year 20)))*

13. **Page 35, Q.8(b) (RUET 2022 Odd Semester (Page 3 of 3)):** Draw an op-amp circuit which will ensure the PID controller. Also derive its transfer function. *(Exact duplicate also on: Page 37, Q.7(a) (RUET 2021 Odd Semester (SECTION-B)); Page 25, Row 1a (Question Analysis Table (Year 21)); Page 25, Row 3 (Question Analysis Table (Year 19)); Page 25, Row 6 Q.7(a) (Question Analysis Table (Year 18)); Page 3, Q.(12) (Handwritten Theory Questions List))*

14. **Page 37, Q.7(c) (RUET 2021 Odd Semester (SECTION-B)):** Why derivative controller is never used alone? *(Exact duplicate also on: Page 25, Row 7 (c) (Question Analysis Table (Year 18)); Page 4, Q.(13) (Handwritten Theory Questions List))*

15. **Page 39, Q.8(a) (RUET 2020 Odd Examination (SECTION-B)):** Draw an Op-Amp circuit which will ensure the PID control design and action. *(Exact duplicate also on: Page 25, Row 8 (a) (Question Analysis Table (Year 17)))*

16. **Page 41, Q.7(a) (RUET 2018 Odd Semester (SECTION-B)):** Draw a PID controller and write down the controller expression. How will you select between PI, PD, and PID controller when used as compensators? *(Exact duplicate also on: Page 25, Row 9 (a) (Question Analysis Table (Year 15)))*

17. **Page 46, Q.8(a) (RUET 2016 Odd Semester (SECTION-B)):** Write short notes on PID controller.

18. **Page 49, Q.8(a) (RUET 2015/Old Semester (Section-B cont.)):** What is PID controller? Write down the expression of a PID controller. What are the advantages of PID controller over PI or PD controller?

19. **Page 51, Q.6(a) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Draw an Op-amp circuit which will ensure the PID control action. Write down the advantages of using PID controller.

20. **Page 54, Q.8(b) (RUET 2013 3rd Year 6th Semester (Page 3)):** Mention the special features of PI, PD and PID controller.

### **Lead-Lag Compensator Design**

*(No explicit questions found in the provided PYQ PDF for this subtopic.)*

### **Pole Placement Technique & State Feedback**

21. **Page 20, Row 2 (Question Analysis Table (Year 21)):** Derive the state-feedback gain Matrix $k$ for a given $2^{\text{nd}}$ order system to place closed-loop poles at desired locations.

22. **Page 32, Q.6(c) (RUET 2023 Odd Semester (SECTION-B)):** How pole placement technique is used to design a state feedback controller? *(Exact duplicate also on: Page 22, Row 6 (Question Analysis Table (Year 20)))*

### **Introduction to Non-Linear Control Systems**

23. **Page 4, Q.(19) (Handwritten Theory Questions List):** Why most of the system are non-linear in nature? Explain with example.

24. **Page 35, Q.8(d) (RUET 2022 Odd Semester (Page 3 of 3)):** Why most of the systems are non-linear in nature? Explain with example. *(Exact duplicate also on: Page 38, Q.1(d) (RUET 2020 Odd Examination (SECTION-A)); Page 9, Row 2 (Question Analysis Table (Year 21)); Page 9, Row 8 (d) (Question Analysis Table (Year 19)); Page 9, Row 11 (d) (Question Analysis Table (Year 17)))*

25. **Page 41, Q.3(c) (RUET 2018 Odd Semester (Page 2)):** Differentiate between linear and nonlinear control. *(Exact duplicate also on: Page 10, Row 1 (c) (Question Analysis Table (Year 15)); Page 6, Q.(31) (Handwritten Theory Questions List))*

26. **Page 42, Q.3(a) (RUET 2017 Odd Semester (SECTION-A)):** Why most of the systems are non-linear in nature? Explain.

27. **Page 43, Q.6(c) (RUET 2017 Odd Semester (SECTION-B)):** Write short note about nonlinear control system.

28. **Page 45, Q.1(c) (RUET 2016 Odd Semester (SECTION-A)):** Write short notes on nonlinear control. What is continuous time and discrete time system?
