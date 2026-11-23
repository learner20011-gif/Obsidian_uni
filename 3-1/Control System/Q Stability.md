# EEE 3105 — Stability (PYQ)

**Syllabus:** Basics of stability, Classification, Routh-Hurwitz criterion, Root-locus.

---

### **Basics & Classification of Stability**

1. **Page 22, Row 1 (Question Analysis Table (Year 21)):** Explain the effects of adding poles and zeros on the stability of a system.

2. **Page 41, Q.6(a) (RUET 2018 Odd Semester (SECTION-B)):** State and explain stability criterion. *(Exact duplicate also on: Page 10, Row 2 (a) (Question Analysis Table (Year 15)); Page 6, Q.(34) (Handwritten Theory Questions List))*

3. **Page 53, Q.6(a) (RUET 2013 3rd Year 6th Semester (SECTION B)):** Define Absolute stability and relative stability. How relative stability can be measured by using Routh's stability criterion and Nyquist stability criterion.

4. **Page 56, Q.3 (CT-03/21-Series/B-Section):** Explain the significance of eigenvalue in a system's stability.

5. **Page 67, Q.1 (CT-2/EEE/19-A (20 B CT 3)):** If you add a pole or a zero in the stabilized system, what happens to stability?

### **Routh-Hurwitz Stability Criterion**

6. **Page 22, Row 2 (Question Analysis Table (Year 21)):** For the following unity feedback system finds the number of poles in the left half-plane, the right half-plane and on the $j\omega$-axis. Draw the conclusion about the stability of the closed-loop system. **[figure Involved]**

   ![[attachments/fig_p22_row_2.png]]

7. **Page 22, Row 3 (Question Analysis Table (Year 21)):** For applying conventional controllers, consider the following characteristics equation: $s^4 + 2s^3 + s^2 + 9s + k + 4 = 0$. (i) Determine the range of $k$ for stability. (ii) Find the value of $k$ for which the system is marginally stable.

8. **Page 32, Q.5(a) (RUET 2023 Odd Semester (SECTION-B)):** Consider the closed-loop system shown in the following figure. Determine the range of $K$ for stability. Assume that $K > 0$. **[figure Involved]** *(Exact duplicate also on: Page 22, Row 4 (Question Analysis Table (Year 20)))*

   ![[attachments/fig_p32_q_5_a.png]]

9. **Page 32, Q.5(c) (RUET 2023 Odd Semester (SECTION-B)):** Define stability. What does the Routh Hurwitz criteria tell us?

10. **Page 34, Q.4(c) (RUET 2022 Odd Semester (Page 2 of 3)):** Open-loop transfer function of certain unity feedback system is $G(s) = \frac{K(s+1)}{s(s-1)(s+6)}$ Determine: (i) The range of values of K for which the system is stable. (ii) The value of K that will result in the system being marginally stable. (iii) The location of the roots of the characteristics equation for the value of K found in (ii). *(Exact duplicate also on: Page 22, Row 7 (c) (Question Analysis Table (Year 19)))*

11. **Page 34, Q.5(c) (RUET 2022 Odd Semester (SECTION-B)):** Write down the limitations and conditions of Routh's stability criterion. What is meant by breakaway and break-in point? *(Exact duplicate also on: Page 22, Row 8 (c) (Question Analysis Table (Year 19)))*

12. **Page 37, Q.5(b) (RUET 2021 Odd Semester (SECTION-B)):** For the following unity feedback system finds the number of poles in the left half plane, the right half plane, on the $j\omega$ axis. Draw the conclusion about the stability of the closed-loop system. **[figure Involved]** *(Exact duplicate also on: Page 23, Row 1 (b) (Question Analysis Table (Year 18)))*

   ![[attachments/fig_p37_q_5_b.png]]

13. **Page 37, Q.6(c) (RUET 2021 Odd Semester (SECTION-B)):** Write down the limitation and conditions of Routh's stability criterion. *(Exact duplicate also on: Page 23, Row 2 (c) (Question Analysis Table (Year 18)); Page 3, Q.(11) (Handwritten Theory Questions List))*

14. **Page 39, Q.6(a) (RUET 2020 Odd Examination (SECTION-B)):** Write down the limitations and conditions of Routh's stability criterion. *(Exact duplicate also on: Page 23, Row 3 (a) (Question Analysis Table (Year 17)))*

15. **Page 39, Q.6(b) (RUET 2020 Odd Examination (SECTION-B)):** Determine the stability of a system with the following characteristic equation. $$s^5 + 4s^4 + 2s^3 + 8s^2 + s + 4 = 0$$ *(Exact duplicate also on: Page 23, Row 3 (b) (Question Analysis Table (Year 17)))*

16. **Page 41, Q.5(a) (RUET 2018 Odd Semester (SECTION-B)):** Define stability and classify it. What does the Routh Hurwitz criteria tell us? *(Exact duplicate also on: Page 23, Row 4 (a) (Question Analysis Table (Year 15)); Page 6, Q.(33) (Handwritten Theory Questions List))*

17. **Page 41, Q.5(b) (RUET 2018 Odd Semester (SECTION-B)):** Using Routh Hurwitz criterion find the range of K for stability of the following system. $$G(s) = \frac{K(s+2)}{s(s+1)(s+3)(s+5)}; \quad H(s) = 1.$$ *(Exact duplicate also on: Page 23, Row 4 (b) (Question Analysis Table (Year 15)))*

18. **Page 43, Q.7(a) (p.43-44) (RUET 2017 Odd Semester (SECTION-B)):** Find the number of poles in the left half plane, the right-half plane, and on the $j\omega$ axis for the following system. **[figure Involved]**

   ![[attachments/fig_p43_q_7_a_p_43_44.png]]

19. **Page 46, Q.5(a) (RUET 2016 Odd Semester (SECTION-B)):** Use the Routh-Hurwitz criterion to find how many poles of the following closed-loop system, $T(s)$ are in the rhp, in the lhp, and on the $j\omega$-axis. $$T(s) = \frac{s^3 + 7s^2 + 21s + 10}{s^6 + s^5 - 6s^4 - s^2 - s + 6}.$$

20. **Page 46, Q.6(a) (RUET 2016 Odd Semester (SECTION-B)):** Find the range of gain K, for the following system that will cause the system to be stable, unstable, and marginally stable. Assume $K > 0$. **[figure Involved]**

   ![[attachments/fig_p46_q_6_a.png]]

21. **Page 48, Q.5(b) (RUET 2015 3rd Year 5th Semester (Section-B)):** The open loop transfer function of a unity feedback control system is given by $$G(s) = \frac{K}{(s+2)(s+4)(s^2+6s+25)}$$ By applying Routh criterion, discuss the stability of the closed loop system as a function of K. Determine the value of K which will cause sustained oscillations in the closed loop system. What are the corresponding oscillation frequencies?

22. **Page 51, Q.6(b) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Find the range of gain k, for the following system, that will cause the system to be stable, unstable and marginally stable. Assume $k > 0$. **[figure Involved]**

   ![[attachments/fig_p51_q_6_b.png]]

23. **Page 51, Q.6(c) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Write down limitations and conditions of Routh's stability criterion

24. **Page 53, Q.6(b) (RUET 2013 3rd Year 6th Semester (SECTION B)):** Using Routh's stability criterion determine the absolute stability of the closed loop transfer function $T(s) = \frac{10}{s^5 + 2s^4 + 3s^3 + 6s^2 + 5s + 3}$

25. **Page 53, Q.6(c) (RUET 2013 3rd Year 6th Semester (SECTION B)):** Consider the system below and let $p = 0$. (i) Determine conditions on K and z so that the system is stable. (ii) Determine all possible conditions on K and z so that the system will have sustained oscillation. Find the oscillation frequency. **[figure Involved]**

   ![[attachments/fig_p53_q_6_c.png]]

26. **Page 54, Q.7(c) (RUET 2013 3rd Year 6th Semester (Page 3)):** For a unity feedback system with forward path transfer function $G(s) = \frac{K}{s(s+3)(s+5)}$ Find the range of gain K for stability, instability and marginal stability.

### **Root-Locus Method**

27. **Page 5, Q.(26) (Handwritten Theory Questions List):** What is root-locus? How can a system's stability be checked from the root-locus plot.

28. **Page 25, Row 10 (Question Analysis Table (Year 21)):** For the unity feedback system the open-loop transfer function is given by $$G(s) = \frac{4s+1}{s^2(s+1)(2s+1)}$$ Sketch the root-locus.

29. **Page 32, Q.6(b) (RUET 2023 Odd Semester (SECTION-B)):** For the following system: $G(s)H(s) = \frac{K}{s(s^2+4s+8)}$. (i) Plot the complete the root-locus. (ii) Find the value of $K$ for the system just oscillates. (iii) For $K = 32$, find $\zeta$. *(Exact duplicate also on: Page 25, Row 11 (Question Analysis Table (Year 20)))*

30. **Page 35, Q.6(b) (RUET 2022 Odd Semester (Page 3 of 3)):** 'Root loci are continuous curves'-justify the statement. For the unity feedback system the open-loop transfer function is given by $$G(s) = \frac{K(s+9)}{s(s^2+4s+11)}$$ Sketch the root-locus. *(Exact duplicate also on: Page 26, Row 1 (Question Analysis Table (Year 19)))*

31. **Page 37, Q.6(a) (RUET 2021 Odd Semester (SECTION-B)):** What are the effects of adding pole and zero on the root locus? *(Exact duplicate also on: Page 26, Row 2 Q.6(a) (Question Analysis Table (Year 18)); Page 3, Q.(10) (Handwritten Theory Questions List))*

32. **Page 37, Q.6(b) (RUET 2021 Odd Semester (SECTION-B)):** Consider the system $G(s) = \frac{K}{s(s+3)(s+4)}$ (i) Draw the complete root locus. (ii) Find the values of $K$ for which the system just oscillates. (iii) For $K = 84$, find the value of $\zeta$. *(Exact duplicate also on: Page 26, Row 3 (b) (Question Analysis Table (Year 18)))*

33. **Page 39, Q.6(c) (RUET 2020 Odd Examination (SECTION-B)):** Consider the following system $G(s) = \frac{K}{s(s+2)(s+3)}; \ H(s) = 1$ (i) Draw the complete root locus. (ii) Find the value of K for which the system just oscillates. (iii) Find the value of $\zeta$ for $K = 6$. *(Exact duplicate also on: Page 26, Row 4 (c) (Question Analysis Table (Year 17)))*

34. **Page 41, Q.7(b) (RUET 2018 Odd Semester (SECTION-B)):** Consider a unity feedback control system with the following feedforward transfer function $$G(s) = \frac{K}{s(s^2+4s+8)}.$$ Plot the root locii for the system. *(Exact duplicate also on: Page 26, Row 5 (b) (Question Analysis Table (Year 15)))*

35. **Page 41, Q.7(c) (RUET 2018 Odd Semester (SECTION-B)):** What can you tell from the root locus if the settling time does not change over a region of gain? *(Exact duplicate also on: Page 26, Row 5 (c) (Question Analysis Table (Year 15)))*

36. **Page 44, Q.7(b) (RUET 2017 Odd Semester (Page 3)):** What is root locus? How would you determine whether or not a root locus plot crossed the real axis?

37. **Page 46, Q.8(c) (RUET 2016 Odd Semester (SECTION-B)):** A unity feedback system has a loop transfer function $$G_c(s)G(s) = \frac{K(s+1)}{s(s-1)(s+4)}$$ (i) Sketch the root locus. (ii) Determine range of K for stability, and (iii) Determine the [cut off at bottom of scan]

38. **Page 49, Q.7(a) (RUET 2015/Old Semester (Section-B cont.)):** Consider a unity feedback control system with the following feed forward transfer function- $$G(s) = \frac{K}{s(s^2+4s+8)}$$ (i) Draw the root locus. (ii) Find out the value of K for which the system just oscillates. (iii) For K=32, find the value of $\zeta$.

39. **Page 51, Q.7(a) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** Prove that "Root loci are symmetrical".

40. **Page 51, Q.7(b) (RUET 2014 3rd Year 6th Semester (SECTION-B)):** A unity feedback control system has the following transfer function $$G(s) = \frac{k(s+2)}{s(s+3)(s+4)}$$ (i) Sketch the root locus. (ii) Symmetry of the root locus. (iii) For what values of k does the system become unstable?

41. **Page 54, Q.7(a) (RUET 2013 3rd Year 6th Semester (Page 3)):** [For] a unity feedback system the open-loop transfer function is [given by] $$G(s) = \frac{K}{s(s+1)(s^2+4s+5)}$$ (i) sketch the root locus for $0 < K < \infty$. (ii) At what value of K the system become unstable. (iii) At this point of instability determine the frequency of oscillation of the system.

42. **Page 64, Q.1 (CT#04 on EEE 3105 (Section: A)):** A unity feedback system has a loop transfer function $$G(s) = \frac{K}{s(s+3)(s+8)}$$ (i) Sketch the root locus and (ii) Determine the range of K for stability

43. **Page 66, Q.1 (CT-02/20-Series/B-Section):** Consider the following system $$G(s)H(s) = \frac{k(s+2)}{s(2s+1)(s^2+8s+7)}$$ (i) Draw the complete root locus and determine the stability. (ii) Sketch the Bode diagram, determine the gain & phase margin, and stability. (iii) Find the value of k for the system just oscillates.

44. **Page 67, Q.2 (CT-2/EEE/19-A (20 B CT 3)):** The closed-loop transfer function of a control system is $$\frac{C(s)}{R(s)} = \frac{k}{s(s+3)(s+4)}$$ (i) What is the Type and Order of this system? (ii) Draw the complete root locus. (iii) Find the value of k for the system just oscillates (iv) Find $\xi$ at $k = 84$.

45. **Page 68, CT-3 (Faruk Sir CT-3):** Draw a complete Root Locus for Any Transfer function which have at least one zeros and predict the stability.
