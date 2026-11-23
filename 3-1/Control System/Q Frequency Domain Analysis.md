# EEE 3105 — Frequency Domain Analysis (PYQ)

**Syllabus:** Introduction of frequency response, Bode diagram, Polar plot, Nyquist Plot, and Nichols chart.

---

### **Introduction to Frequency Response & Specifications**

1. **Page 6, Q.(37) (Handwritten Theory Questions List):** What is nonminium phase system?

2. **Page 32, Q.7(b) (RUET 2023 Odd Semester (SECTION-B)):** Define: (i) Gain margin, (ii) Phase margin. *(Exact duplicate also on: Page 27, Row 2 (b) (Question Analysis Table (Year 20)))*

3. **Page 34, Q.6(a) (RUET 2022 Odd Semester (SECTION-B)):** Write short notes on: (i) Gain margin, (ii) Phase margin, (iii) critically damped system, (iv) non-minimum phase system. *(Exact duplicate also on: Page 27, Row 3 (a) (Question Analysis Table (Year 19)))*

4. **Page 37, Q.8(a) (RUET 2021 Odd Semester (SECTION-B)):** Define gain margin and phase margin. *(Exact duplicate also on: Page 28, Row 2 Q.8(a) (Question Analysis Table (Year 18)); Page 4, Q.(14) (Handwritten Theory Questions List))*

5. **Page 39, Q.7(a) (RUET 2020 Odd Examination (SECTION-B)):** Define (i) phase margin and (ii) gain margin with net sketch. *(Exact duplicate also on: Page 28, Row 3 (a) (Question Analysis Table (Year 17)))*

6. **Page 41, Q.8(b) (RUET 2018 Odd Semester (SECTION-B)):** Define frequency response. What are advantages of frequency response? *(Exact duplicate also on: Page 10, Row 3 (b) (Question Analysis Table (Year 15)); Page 6, Q.(36) (Handwritten Theory Questions List))*

7. **Page 41, Q.8(c) (RUET 2018 Odd Semester (SECTION-B)):** What is nonminimum phase system? *(Exact duplicate also on: Page 10, Row 3 (c) (Question Analysis Table (Year 15)))*

8. **Page 43, Q.5(b) (RUET 2017 Odd Semester (SECTION-B)):** Define (i) Gain margin and (ii) Phase margin.

9. **Page 44, Q.8(c) (RUET 2017 Odd Semester (Page 3)):** Define frequency response. Write down the advantages of frequency response.

10. **Page 44, Q.8(d) (RUET 2017 Odd Semester (Page 3)):** Define the followings: (i) Nonminimum phase system (ii) Transition matrix (iii) corner frequency

11. **Page 46, Q.7(a) (RUET 2016 Odd Semester (SECTION-B)):** Define frequency response. What are the advantages of frequency response?

12. **Page 56, Q.1 (CT-4/EEE/21-C):** Define Gain margin and Phase margin with a net sketch

13. **Page 67, Q.1 (CT-02/20-Series/B-Section (20 B CT 4)):** Define Gain crossover frequency, phase crossover frequency, gain margin, and phase margin.

### **Bode Diagram**

14. **Page 7, Q.(41) (Handwritten Theory Questions List):** Write a note on Bode plot. How does it help design a system?

15. **Page 27, Row 1 (Question Analysis Table (Year 21)):** For control system design purpose check the stability of the following system using Bode-plot: $$G(s) = \frac{50}{s(1+0.25s)(1+0.1s)}$$

16. **Page 32, Q.7(c) (RUET 2023 Odd Semester (SECTION-B)):** Draw the Bode diagram of the following system. Is this system stable or not? $$G(s) = \frac{10(s+3)}{s(s+2)(s^2+s+2)}.$$ *(Exact duplicate also on: Page 41, Q.8(a) (RUET 2018 Odd Semester (SECTION-B)); Page 27, Row 2 (c) (Question Analysis Table (Year 20)); Page 28, Row 4 (a) (Question Analysis Table (Year 15)))*

17. **Page 35, Q.7(b) (RUET 2022 Odd Semester (Page 3 of 3)):** For control system design purpose, check the stability of the following system using Bode Plot: $$G(s) = \frac{1000}{(1+0.1s)(1+0.001s)}$$ *(Exact duplicate also on: Page 27, Row 4 (b) (Question Analysis Table (Year 19)))*

18. **Page 35, Q.7(c) (RUET 2022 Odd Semester (Page 3 of 3)):** Evaluate the transfer function from the following asymptotic log-magnitude plot. **[figure Involved]** *(Exact duplicate also on: Page 27, Row 5 (Fig. 7c) (Question Analysis Table (Year 19)))*

   ![[attachments/fig_p35_q_7_c.png]]

19. **Page 37, Q.7(b) (RUET 2021 Odd Semester (SECTION-B)):** Draw the asymptotic Bode diagram of the system: $$G(j\omega) = \frac{6\left\{1 + j\left(\frac{\omega}{2}\right)\right\}}{j\omega(1+j2\omega)\left\{1 + j0.4\left(\frac{\omega}{8}\right) - \left(\frac{\omega}{8}\right)^2\right\}}$$ Determine whether the system is stable or not? *(Exact duplicate also on: Page 27, Row 6 (b) (p.27-28) (Question Analysis Table (Year 18)))*

20. **Page 39, Q.7(b) (RUET 2020 Odd Examination (SECTION-B)):** Draw the bode diagram for the following system and also determine (i) gain and phase cross over frequency, (ii) gain and phase margins, and (iii) stability of the system. $$G(j\omega) = \frac{100(s+10)}{s(s+0.5)(4s+1)^2}; \quad H(s) = 1.$$ *(Exact duplicate also on: Page 28, Row 3 (b) (Question Analysis Table (Year 17)))*

21. **Page 43, Q.6(a) (RUET 2017 Odd Semester (SECTION-B)):** Write a note on Bode plot. How does it help of system design?

22. **Page 43, Q.6(b) (RUET 2017 Odd Semester (SECTION-B)):** Draw the Bode diagram of the following system where feedback is unity. $$G(s) = \frac{50}{s(1+0.25s)(1+0.1s)}$$ Check the stability of the system

23. **Page 46, Q.5(b) (RUET 2016 Odd Semester (SECTION-B)):** Draw the Bode plots for the following system Where, $G(s) = \frac{K(s+3)}{s(s+1)(s+2)}$. **[figure Involved]**

   ![[attachments/fig_p46_q_5_b.png]]

24. **Page 46, Q.6(b) (RUET 2016 Odd Semester (SECTION-B)):** Find the transfer function $G(s)$ from the following magnitude plot. **[figure Involved]**

   ![[attachments/fig_p46_q_6_b.png]]

25. **Page 46, Q.7(b) (RUET 2016 Odd Semester (SECTION-B)):** What is corner frequency? *(Exact duplicate also on: Page 7, Q.(43) (Handwritten Theory Questions List))*

26. **Page 46, Q.7(c) (RUET 2016 Odd Semester (SECTION-B)):** Draw the bode diagram of the following system. Is this system stable or not? $$G(s) = \frac{4\left(1 + \frac{s}{2}\right)}{s(1+2s)\left[1 + 0.4\left(\frac{s}{8}
ight) + \left(\frac{s}{8}
ight)^2\right]}$$

27. **Page 51, Q.8(a) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Draw the bode diagram for the following system and also determine (i) gain and phase cross over frequencies, (ii) the gain margin and phase margin, (iii) the stability of the system. $$G(s)H(s) = \frac{20(s+20)}{s(2s+1)(s^2+4s+2)}$$ [Note: numerator/constant term partially faded in scan]

28. **Page 54, Q.8(a) (RUET 2013 3rd Year 6th Semester (Page 3)):** Draw the Bode plot for the transfer function $$G(s) = \frac{50}{s(1+0.25s)(1+0.1s)}.$$ From the graph determine: (i) Gain crossover frequency (ii) Phase crossover frequency (iii) Gain Margin and Phase Margin (iv) Stability of the system.

29. **Page 56, Q.2 (CT-4/EEE/21-C):** Consider the system is $G(s) = \frac{10(s+2)}{s(s+3)(s^2+16)}$ Draw the complete Bode Diagram. Find out the stability of this System

30. **Page 64, Q.2 (CT#04 on EEE 3105 (Section: A)):** Using Bode plots, explain how to determine whether a dynamic system is stable, unstable, or marginally stable based on gain and phase margins.

31. **Page 66, Q.3 (CT-02/20-Series/B-Section):** Find out the transfer function from the following bode plot. **[figure Involved]**

   ![[attachments/fig_p66_q_3.png]]

32. **Page 67, Q.2 (CT-02/20-Series/B-Section (20 B CT 4)):** Consider the system $\frac{10(j\omega+2)}{j\omega(j\omega+0.5)[(j\omega)^2+16]}$ Draw the complete bode diagram and find out the stability of this system.

33. **Page 67, Q.3 (CT-02/20-Series/B-Section (20 B CT 4)):** Find out the transfer function from the bode plot. **[figure Involved]**

   ![[attachments/fig_p67_q_3.png]]

34. **Page 68, Q.1 (CT-4/EEE/19-A):** Mention the importance of Bode plot?

35. **Page 68, Q.2 (CT-4/EEE/19-A):** Consider the system is $G(s) = \frac{10(s+2)}{s(s+1)(s+3)(s+4)}$ Draw the complete Bode Diagram. Find out the stability of this System

36. **Page 68, Q.3 (CT-4/EEE/19-A):** Find out the transfer function by using following curves **[figure Involved]**

   ![[attachments/fig_p68_q_3.png]]

### **Polar Plot**

37. **Page 32, Q.8(c) (RUET 2023 Odd Semester (SECTION-B)):** Sketch polar plot for (i) $G(s) = \frac{K}{(1+sT_1)(1+sT_2)}$ and (ii) $G(s)H(s) = \frac{K}{s(s+1)(s+5)}$. *(Exact duplicate also on: Page 28, Row 7 (c) (Question Analysis Table (Year 20)))*

38. **Page 35, Q.7(a) (RUET 2022 Odd Semester (Page 3 of 3)):** Sketch the Polar Plot for $G(s) = \frac{K}{s^2(1+sT)}$ *(Exact duplicate also on: Page 28, Row 8 (a) (Question Analysis Table (Year 19)))*

39. **Page 37, Q.8(d) (RUET 2021 Odd Semester (SECTION-B)):** Sketch polar plot for $G(s) = \frac{K}{(1+sT_1)(1+sT_2)}$. *(Exact duplicate also on: Page 29, Row 2 (d) (Question Analysis Table (Year 18)))*

40. **Page 41, Q.6(c) (RUET 2018 Odd Semester (SECTION-B)):** Sketch the polar plot of the following systems: (i) $G(s)H(s) = \frac{K}{s^2(Ts+1)}$, (ii) $G(s)H(s) = \frac{K}{(T_1 s + 1)(T_2 s + 1)}$. *(Exact duplicate also on: Page 29, Row 6 (c) (Question Analysis Table (Year 15)))*

41. **Page 44, Q.7(c) (RUET 2017 Odd Semester (Page 3)):** Sketch the poles plot of the followings:- (i) $G(s) = \frac{10(s+1)}{s+10}$; (ii) $G(s) = \frac{20s}{(s+1)(s+10)}$

42. **Page 49, Q.7(b) (RUET 2015/Old Semester (Section-B cont.)):** Sketch the polar plot of (i) $G(s) = \frac{10}{s(s+1)}$ (ii) $G(s) = \frac{20}{s(s+1)(s+2)}$

43. **Page 54, Q.7(b) (RUET 2013 3rd Year 6th Semester (Page 3)):** Sketch the expected polar plot of $G_1(s) = \frac{K}{s(1+sT_1)(1+sT_2)}$ [and] $G_2(s) = \frac{K}{s^2(1+sT_1)(1+sT_2)}$

44. **Page 56, Q.3 (CT-4/EEE/21-C):** Draw the polar plot $\omega = -\infty$ to $\infty$ [for $G(s)$ in Q.2: $G(s) = \frac{10(s+2)}{s(s+3)(s^2+16)}$]

### **Nyquist Plot & Nyquist Stability Criterion**

45. **Page 4, Q.(15) (Handwritten Theory Questions List):** What are the conditions and limitations for stability of a system subjected to Nyquist stability criterion.

46. **Page 8, Q.(53) (Handwritten Theory Questions List):** What is asymtote? How to examine the stability of a linear control system using Nyquist stability criterion?

47. **Page 28, Row 5 (Question Analysis Table (Year 21)):** A system has the following open-loop transfer function $G(s)H(s) = \frac{K}{s^2(T_1 s + 1)}$. Check the stability of this system with and without derivative control using Nyquist plot.

48. **Page 32, Q.8(a) (RUET 2023 Odd Semester (SECTION-B)):** Consider the following unity feedback system: $G(s) = \frac{K(1-s)}{(s+1)}$ Determine the stability of the system using Nyquist plot for two cases: (i) the gain $K$ is small and (ii) $K$ is large. *(Exact duplicate also on: Page 28, Row 6 Q.8(a) (Question Analysis Table (Year 20)))*

49. **Page 32, Q.8(b) (RUET 2023 Odd Semester (SECTION-B)):** What is meant by detour? Why the Nyquist criterion is called a frequency response method? *(Exact duplicate also on: Page 28, Row 7 (b) (Question Analysis Table (Year 20)))*

50. **Page 35, Q.8(a) (RUET 2022 Odd Semester (Page 3 of 3)):** Consider the following unity feedback system: $$G(s) = \frac{K}{s(1+sT_1)(1+sT_2)}$$ Determine the stability of the system using Nyquist plot for two cases: (i) the gain K is small and (ii) K is large. *(Exact duplicate also on: Page 28, Row 9 (a) (Question Analysis Table (Year 19)))*

51. **Page 37, Q.8(b) (RUET 2021 Odd Semester (SECTION-B)):** What are the conditions and limitations for stability of a system subjected to Nyquist stability criterion?

52. **Page 37, Q.8(c) (RUET 2021 Odd Semester (SECTION-B)):** Consider the unity feedback system: $G(s) = \frac{K(1-s)}{s+1}$ Determine the stability of the system using Nyquist plot for two cases: (i) the gain K is small and (ii) K is large. *(Exact duplicate also on: Page 28, Row 10 (c) (p.28-29) (Question Analysis Table (Year 18)))*

53. **Page 39, Q.8(b) (RUET 2020 Odd Examination (SECTION-B)):** What are the conditions and limitations for stability of a system subjected to Nyquist criterion? *(Exact duplicate also on: Page 29, Row 4 (b) (Question Analysis Table (Year 17)))*

54. **Page 39, Q.8(c) (RUET 2020 Odd Examination (SECTION-B)):** For the following unity feedback system determine the stability using Nyquist stability criterion. $$G(s) = \frac{4s+1}{s^2(s+1)(2s+1)}$$ *(Exact duplicate also on: Page 29, Row 4 (c) (Question Analysis Table (Year 17)))*

55. **Page 41, Q.6(b) (RUET 2018 Odd Semester (SECTION-B)):** For the following unity feedback system determine the stability using Nyquist stability criterion. $$G(s)H(s) = \frac{K}{s(T_1 s + 1)(T_2 s + 1)}; \text{ where K is large.}$$ *(Exact duplicate also on: Page 29, Row 6 (b) (Question Analysis Table (Year 15)))*

56. **Page 43, Q.5(a) (RUET 2017 Odd Semester (SECTION-B)):** Plot the Nyquist diagram for the following system. Also find the stability. **[figure Involved]**

   ![[attachments/fig_p43_q_5_a.png]]

57. **Page 49, Q.6(b) (RUET 2015/Old Semester (Section-B cont.)):** A system having the following open-loop transfer function- $$G(s)H(s) = \frac{1}{s(1+2s)(1+s)}.$$ Determine whether the closed-loop system is stable or not using Nyquist criterion.

58. **Page 49, Q.8(b) (RUET 2015/Old Semester (Section-B cont.)):** State and explain Nyquist stability criterion.

59. **Page 49, Q.8(c) (RUET 2015/Old Semester (Section-B cont.)):** How to examine the stability of a linear control system using Nyquist stability criterion?

60. **Page 51, Q.8(b) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** What are the limitations and conditions of using Nyquist stability criterion of a system?

61. **Page 51, Q.8(c) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** By completing the Nyquist diagram, investigate stability for the following plot. **[figure Involved]**

   ![[attachments/fig_p51_q_8_c.png]]

62. **Page 54, Q.8(c) (RUET 2013 3rd Year 6th Semester (Page 3)):** What is mapping of contour? Use Nyquist criterion, determine whether the closed loop system having the following open loop transfer function is stable or not. If not how many closed loop poles lie in the right half s-plane? $$G(s)H(s) = \frac{1+4s}{s^2(1+2s)(1+s)}$$

### **Nichols Chart**

63. **Page 39, Q.7(c) (RUET 2020 Odd Examination (SECTION-B)):** Check the stability of the following unity feedback system by using Nichol's plot. $$G(s) = \frac{10}{s(s+3)(s+4)}$$ *(Exact duplicate also on: Page 29, Row 3 (c) (Question Analysis Table (Year 17)))*

64. **Page 41, Q.5(c) (RUET 2018 Odd Semester (SECTION-B)):** Check the stability of the following unity feedback system by using Nichol's plot. $$G(s) = \frac{5}{s(s+2)(s+3)}.$$ *(Exact duplicate also on: Page 29, Row 5 (c) (Question Analysis Table (Year 15)))*
