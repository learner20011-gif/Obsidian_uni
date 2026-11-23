# EEE 3109 — Partial Differential Equations (PYQ)

**Syllabus:** Finite difference (FD) methods, Numerical stability, Implicit FD method.

---

### **Finite Difference Methods for PDEs (Elliptic, Parabolic, Hyperbolic)**

1. **(p. 4, (26) — Theory Questions EEE 3109)** Classify linear 2nd order partial differential eqn and give example from electrical from electrical engineering domain for each class.

2. **(p. 4, (27) — Theory Questions EEE 3109)** Describe the procedure to solve elliptic PDE's for irregular boundaries.

3. **(p. 24, (c) — Topic 9: Partial Differential Equations (Series 18))** Define partial differential equation. Explain any computational method to solve partial differential equation with example.
   *(Exact duplicate also on: p. 3, (11) (Theory Questions EEE 3109))*

4. **(p. 24, (c) — Topic 9: Partial Differential Equations (Series 21))** A square PCB is discretized into a $3\times 3$ grid. The boundry temperatures are fixed at $100\ ^{\circ}\text{C}$ on the left and $0^{\circ}\text{C}$ elsewhere. If the steady state temperature distribution abides by Laplace's equation, solve for the temperature at the interior nodes.

5. **(p. 24, Q.8. (a) — Topic 9: Partial Differential Equations (Series 21))** Discuss how finite difference approximation of PDE can be formed with an example of the Laplace's equation.

6. **(p. 27, (b) — 2023 Odd Semester (EEE 3109))** Consider a steel plate of size $15\text{ cm} \times 15\text{ cm}$. If two of the sides are held at $100^{\circ}\text{C}$, and other two sides are held at $0^{\circ}\text{C}$, what are the steady state temperature at interior points assuming a grid size of $5\text{ cm} \times 5\text{ cm}$.
   *(Exact duplicate also on: p. 24, (b) (Topic 9: Partial Differential Equations (Series 20)))*

7. **(p. 29, (b) — 2022 Odd Semester (EEE 3109))** **[figure Involved]** Use Liebmann's method to solve the 2D Laplace equation that satisfy the following equation: $\nabla^2 T = \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0$. The geometry, the mesh grid and the boundary values are shown in following figure. Consider $\Delta x = \Delta y$, $\alpha_1 = \beta_1 = 0.732$, and $\alpha_2 = \beta_2 = 1$ and employ over-relaxation with a value of $1.5$. Perform only two iterations.
   *(Exact duplicate also on: p. 24, (b) (Topic 9: Partial Differential Equations (Series 19)))*

   ![[attachments/fig_p29_b.png]]

8. **(p. 31, (b) — 2020 Odd Semester (EEE 3109))** Explain any computational method to solve partial differential equation with a suitable example.
   *(Exact duplicate also on: p. 24, (b) (Topic 9: Partial Differential Equations (Series 17)))*

9. **(p. 34, (c) — 2018 Odd Semester (EEE 3109))** **[figure Involved]** Solve the differential equation $u_{xx} + u_{yy} = 0$ in the domain of figure below using finite difference (FD) method.
   *(Exact duplicate also on: p. 24, (c) (Topic 9: Partial Differential Equations (Series 15)))*

   ![[attachments/fig_p34_c.png]]

10. **(p. 36, (b) — 2017 Odd Semester (EEE 3109))** Derive Laplacian difference equation to solve Laplace equation.

11. **(p. 36, (c) — 2017 Odd Semester (EEE 3109))** **[figure Involved]** Solve the partial differential equation
   $$\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0$$
   in the domain of the following figure by Liebmann's method. Use successive over-relaxation factor in the process. Proceed to three iterations.

   ![[attachments/fig_p36_c_2.png]]

12. **(p. 36, Q. 8(a) — 2017 Odd Semester (EEE 3109))** Write down the names of the methods to solve partial differential equation.

13. **(p. 38, (b) — 2016 Odd Semester (EEE 3109))** **[figure Involved]** Solve the equation $\frac{\partial^2 E(x, y)}{\partial x^2} + \frac{\partial^2 E(x, y)}{\partial y^2} = 0$ in the domain of the following figure by
   (i) Jacobi's method
   (ii) Gauss-Seidal's method
   (iii) Successive Over Relaxation method.
   Obtain seven iterations for (i), five iterations for (ii) and three iterations for (iii). Hence comment on the results.

   ![[attachments/fig_p38_b.png]]

14. **(p. 38, Q. 5(a) — 2016 Odd Semester (EEE 3109))** Why FDTD method is used? Derive the 1 dimensional FDTD updating equations for electric and magnetic field.

15. **(p. 38, Q. 8(a) — 2016 Odd Semester (EEE 3109))** Discuss briefly in text the solving process of partial differential equation using a numerical iterative technique.

16. **(p. 41, (b) — Semester Exam (EEE 3109, Pre-2016))** **[figure Involved]** Use Liebmann's method to find the potential distribution of the interior grid points:

   ![[attachments/fig_p42_b.png]]

17. **(p. 41, Q. 8(a) — Semester Exam (EEE 3109, Pre-2016))** Classify second order partial differential equations in two variables.
   *(Exact duplicate also on: p. 48, Q. 8(a) (2006 Semester Exam (EEE 251)))*

18. **(p. 42, (b) — 2008 Semester Exam (EEE 251))** Solve the Poission equation $\nabla^2 f = 2x^2 y^2$ over the square domain $0 \le x \le 3$ and $0 \le y \le 3$ with $f = 0$ on the boundary and $h = 1$.

19. **(p. 42, Q. 2(a) — 2008 Semester Exam (EEE 251))** **[figure Involved]** Find the potential distribution at the interior nodes. Find from the banded matrix and then solve the system using efficient Thomas algorithm.

   ![[attachments/fig_p42_q_2_a.png]]

20. **(p. 46, (b) — 2007 Regular Exam (EEE-251))** Differentiate between Dirichlet and Neumann boundary condition. Derive Laplacian difference equation for Neumann boundary condition at right and top edges and Dirichlet boundary condition at left and bottom edges for a rectangular plate.

21. **(p. 46, (c) — 2007 Regular Exam (EEE-251))** **[figure Involved]** In the following figure find the potential distribution at the interior grid points using liebmann interactive method. Use relaxation parameter $\lambda = 1.5$

   ![[attachments/fig_p47_c.png]]

22. **(p. 46, Q. 8(a) — 2007 Regular Exam (EEE-251))** Classify linear second order partial differential equation and give example from electrical engineering domain for each class.

23. **(p. 48, (b) — 2006 Semester Exam (EEE 251))** **[figure Involved]** The potential function $V$ satisfies Laplace's equation in two dimensions. Compute the potentials at the nodes $a,b,c,d$ shown in figure below, which also shows the potentials at the boundaries.

   ![[attachments/fig_p48_b.png]]

24. **(p. 48, (c) — 2006 Semester Exam (EEE 251))** Derive Laplacian difference equation for Neumann boundary condition.

25. **(p. 49, (b) — 2005 Regular Exam (EEE-251C))** Derive the solving equation of PDE (Laplace type) for irregular boundaries.

26. **(p. 49, (c) — 2005 Regular Exam (EEE-251C))** **[figure Involved]** A region surrounded by four metal plates that are maintained at potential indicated in the following figure. Find the potential distribution inside the region.

   ![[attachments/fig_p49_c.png]]

27. **(p. 49, Q. 4(a) — 2005 Regular Exam (EEE-251C))** Write down the general form of linear second order partial differential equation for two variables. How can this equation be classified?

### **Numerical Stability, Explicit & Implicit FD Methods**

28. **(p. 8, (52) — Theory Questions EEE 3109)** Discuss the solving process of partial D.E using a numerical iterative technique.

29. **(p. 42, (c) — Semester Exam (EEE 3109, Pre-2016))** What is the condition for convergence and stability in explicit methods for solving parabolic PDE?
   *(Exact duplicate also on: p. 42, (c) (2008 Semester Exam (EEE 251)))*
