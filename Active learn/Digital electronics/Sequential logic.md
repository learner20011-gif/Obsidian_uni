Here are the first 5 problems from the **Problems** section at the end of Chapter 6 (page 223), along with short, easy-to-follow answers.

---

### **Problem 6-1**
**Question:**
Show the logic diagram of a clocked *RS* flip-flop with four NAND gates.

**Easy Answer:**
Use two 2-input NAND gates at the input (gated by $CP$) feeding a basic 2-input NAND latch:

```text
  S ──┬──[ NAND 1 ]───┬──[ NAND 3 ]──┬── Q
      │               │      ┌───────┘
 CP ──┼───┐           │    ┌─┴─┐
      │   │           └────┼───┼─┐
      │   │                └─┬─┘ │
  R ──┼───┴──[ NAND 2 ]──────┴───┼──[ NAND 4 ]──┬── Q'
      │                          └──────────────┘
```
*(Wait—let's make the cross-coupling cleaner to read)*:
* **NAND 1:** inputs = $S, CP$ $\rightarrow$ output goes to **NAND 3**
* **NAND 2:** inputs = $R, CP$ $\rightarrow$ output goes to **NAND 4**
* **NAND 3:** inputs = (output of NAND 1), $Q'$ $\rightarrow$ output is **$Q$**
* **NAND 4:** inputs = (output of NAND 2), $Q$ $\rightarrow$ output is **$Q'$**

---

### **Problem 6-2**
**Question:**
Show the logic diagram of a clocked *D* flip-flop with AND and NOR gates.

**Easy Answer:**
Take the clocked *RS* flip-flop made of two AND gates + two cross-coupled NOR gates (Fig. 6-4a), and feed $D$ to $S$ and $D'$ to $R$ (using a NOR gate with both inputs tied to $D$ as an inverter):

* **Inverter (NOR 1):** inputs = $D, D$ $\rightarrow$ output is $D'$
* **AND 1:** inputs = $D, CP$ $\rightarrow$ output is $S_{int}$
* **AND 2:** inputs = $D', CP$ $\rightarrow$ output is $R_{int}$
* **NOR 2:** inputs = $R_{int}, Q'$ $\rightarrow$ output is **$Q$**
* **NOR 3:** inputs = $S_{int}, Q$ $\rightarrow$ output is **$Q'$**

---

### **Problem 6-3**
**Question:**
Show that the clocked *D* flip-flop of Fig. 6-5(a) can be reduced by one gate.

**Easy Answer:**
In Fig. 6-5(a), **gate 5** (the inverter on $D$) can be removed by connecting the **output of gate 3** ($\overline{D \cdot CP}$) directly to the input of **gate 4** instead of $D'$:

* **Proof:** Gate 4's output becomes:
  $$\overline{(\overline{D \cdot CP}) \cdot CP} = \overline{(D' + CP') \cdot CP} = \overline{D' \cdot CP}$$
* This is the exact same output as before ($\overline{D' \cdot CP}$), so **gate 5 is unnecessary** (reducing 5 NAND gates to 4).

---

### **Problem 6-4**
**Question:**
Consider a $JK'$ flip-flop, i.e., a *JK* flip-flop with an inverter between external input $K'$ and internal input $K$.
(a) Obtain the flip-flop characteristic table.
(b) Obtain the characteristic equation.
(c) Show that tying the two external inputs together forms a *D* flip-flop.

**Easy Answer:**
Since external input $K'$ is inverted, internal $K = (K')'$.

**(a) Characteristic Table:**

| $J$ | $K'$ | Internal $K$ | $Q(t+1)$ |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 1 | $0$ |
| 0 | 1 | 0 | $Q(t)$ |
| 1 | 0 | 1 | $Q'(t)$ |
| 1 | 1 | 0 | $1$ |

**(b) Characteristic Equation:**
Substitute $K_{internal} = (K')'$ into $Q(t+1) = JQ' + K_{internal}'Q$:
$$Q(t+1) = JQ' + K'Q$$

**(c) Tying $J$ and $K'$ together to $D$ ($J = K' = D$):**
$$Q(t+1) = DQ' + DQ = D(Q' + Q) = D$$
This is the characteristic equation of a **D flip-flop**.

---

### **Problem 6-5**
**Question:**
A set-dominate flip-flop has a set and a reset input. It differs from a conventional *RS* flip-flop in that an attempt to simultaneously set and reset results in setting the flip-flop.
(a) Obtain the characteristic table and characteristic equation for the set-dominate flip-flop.
(b) Obtain a logic diagram for an asynchronous set-dominate flip-flop.

**Easy Answer:**

**(a) Characteristic Table & Equation:**

| $S$ | $R$ | $Q(t+1)$ |
| :---: | :---: | :---: |
| 0 | 0 | $Q(t)$ |
| 0 | 1 | $0$ |
| 1 | 0 | $1$ |
| 1 | 1 | $1$ |

From the table (or a 3-variable K-map):
$$Q(t+1) = S + R'Q$$
*(Unlike a regular RS flip-flop, there is no $SR = 0$ restriction.)*

**(b) Logic Diagram (Asynchronous Set-Dominate Flip-Flop):**
Block $R$ whenever $S = 1$ using $R_{int} = R \cdot S'$, then feed $S$ and $R_{int}$ into a standard NOR latch:

* **NOT gate:** input = $S$ $\rightarrow$ output is $S'$
* **AND gate:** inputs = $R, S'$ $\rightarrow$ output is $R_{int}$
* **NOR 1:** inputs = $R_{int}, Q'$ $\rightarrow$ output is **$Q$**
* **NOR 2:** inputs = $S, Q$ $\rightarrow$ output is **$Q'$**

*(Check: When $S=1$ and $R=1$, $R_{int} = 0$, so the NOR latch sees $S=1, R_{int}=0$ and sets $Q=1, Q'=0$.)*

Here are the next 5 problems (**6-6 to 6-10**) from pages 223–224, with full questions and complete, easy-to-follow answers (nothing skipped).

---

### **Problem 6-6**
**Question:**
Obtain the logic diagram of a master-slave *JK* flip-flop with AND and NOR gates. Include a provision for setting and clearing the flip-flop asynchronously (without a clock).

**Easy Answer:**
Build the master and slave as clocked *RS* flip-flops using **AND + NOR** gates (like Fig. 6-4a), add feedback from $Q$ and $Q'$, invert $CP$ for the slave, and add active-HIGH **Preset** and **Clear** inputs to both stages so they override the clock:

* **Clock Inverter (NOR 9):** inputs = $CP, CP$ $\rightarrow$ output is $CP'$
* **Preset / Clear Inverters (NOR 10 & 11):**
  * NOR 10: inputs = $\text{Preset}, \text{Preset}$ $\rightarrow$ output is $\text{Preset}'$
  * NOR 11: inputs = $\text{Clear}, \text{Clear}$ $\rightarrow$ output is $\text{Clear}'$
* **Master Stage** (enabled when $CP = 1$):
  * **AND 1** (Master Reset): inputs = $K, CP, Q, \text{Preset}'$ $\rightarrow$ goes to NOR 3
  * **AND 2** (Master Set): inputs = $J, CP, Q', \text{Clear}'$ $\rightarrow$ goes to NOR 4
  * **NOR 3** (output **$Y$**): inputs = (AND 1 output), $Y', \text{Clear}$
  * **NOR 4** (output **$Y'$**): inputs = (AND 2 output), $Y, \text{Preset}$
* **Slave Stage** (enabled when $CP = 0$, i.e. $CP' = 1$):
  * **AND 5** (Slave Set): inputs = $Y, CP'$ $\rightarrow$ goes to NOR 8
  * **AND 6** (Slave Reset): inputs = $Y', CP'$ $\rightarrow$ goes to NOR 7
  * **NOR 7** (output **$Q$**): inputs = (AND 6 output), $Q', \text{Clear}$
  * **NOR 8** (output **$Q'$**): inputs = (AND 5 output), $Q, \text{Preset}$

**How Preset & Clear work (without a clock):**
* $\text{Preset}=1, \text{Clear}=0$: forces $Y'=0, Y=1$ and $Q'=0, Q=1$ (Set).
* $\text{Clear}=1, \text{Preset}=0$: forces $Y=0, Y'=1$ and $Q=0, Q'=1$ (Clear).
* $\text{Preset}=\text{Clear}=0$: normal clocked *JK* master-slave operation.

---

### **Problem 6-7**
**Question:**
This problem investigates the operation of the master-slave *JK* flip-flop through the binary transition in the internal gates of Fig. 6-11. Evaluate the binary values (0 or 1) in the outputs of the nine gates when the inputs to the circuit go through the following sequence:
(a) $CP = 0, Y = 0, Q = 0,$ and $J = K = 1$.
(b) After $CP$ goes to 1 ($Y$ should go to 1; $Q$ remains at 0).
(c) After $CP$ goes to 0 and immediately after that $J$ goes to 0 ($Q$ should go to 1; $Y$ is unaffected).
(d) After $CP$ goes to 1 again ($Y$ should go to 0).
(e) After $CP$ goes back to 0 and immediately after that $K$ goes to 0 ($Q$ should go to 0).
(f) All succeeding pulses have no effect as long as $J$ and $K$ remain at 0.

**Easy Answer:**
In Fig. 6-11, all gates are NAND gates (gate 9 is a NOT gate):
* **Gate 1** $= \overline{J \cdot CP \cdot Q'}$, **Gate 2** $= \overline{K \cdot CP \cdot Q}$
* **Gate 3 ($Y$)** $= \overline{\text{G1} \cdot Y'}$, **Gate 4 ($Y'$)** $= \overline{\text{G2} \cdot Y}$
* **Gate 9 ($CP'$)** $= \overline{CP}$
* **Gate 5** $= \overline{Y \cdot CP'}$, **Gate 6** $= \overline{Y' \cdot CP'}$
* **Gate 7 ($Q$)** $= \overline{\text{G5} \cdot Q'}$, **Gate 8 ($Q'$)** $= \overline{\text{G6} \cdot Q}$

| Step | Conditions | G1 | G2 | G3 ($Y$) | G4 ($Y'$) | G5 | G6 | G7 ($Q$) | G8 ($Q'$) | G9 ($CP'$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **(a)** | $CP=0, Y=0, Q=0, J=K=1$ | 1 | 1 | **0** | 1 | 1 | 0 | **0** | 1 | 1 |
| **(b)** | $CP \to 1$ ($J=K=1$) | 0 | 1 | **1** | 0 | 1 | 1 | **0** | 1 | 0 |
| **(c)** | $CP \to 0$, then $J \to 0$ ($K=1$) | 1 | 1 | **1** | 0 | 0 | 1 | **1** | 0 | 1 |
| **(d)** | $CP \to 1$ ($J=0, K=1$) | 1 | 0 | **0** | 1 | 1 | 1 | **1** | 0 | 0 |
| **(e)** | $CP \to 0$, then $K \to 0$ ($J=0$) | 1 | 1 | **0** | 1 | 1 | 0 | **0** | 1 | 1 |
| **(f1)** | Next pulse: $CP=1$ ($J=K=0$) | 1 | 1 | **0** | 1 | 1 | 1 | **0** | 1 | 0 |
| **(f2)** | Pulse ends: $CP=0$ ($J=K=0$) | 1 | 1 | **0** | 1 | 1 | 0 | **0** | 1 | 1 |

**Why (f) has no effect:** With $J = K = 0$, Gates 1 and 2 stay **1** regardless of $CP$, so the master ($Y=0, Y'=1$) never changes, and the slave stays locked at $Q = 0, Q' = 1$.

---

### **Problem 6-8**
**Question:**
Connect an asynchronous clear terminal to the inputs of gates 2 and 6 of the flip-flop in Fig. 6-12.
(a) Show that when the clear input is 0, the flip-flop is cleared, and remains cleared, regardless of the values of $CP$ and $D$ inputs.
(b) Show that when the clear input is 1, it has no effect on the normal clocked operations.

**Easy Answer:**
In Fig. 6-12, all gates are NAND gates. Connecting `Clear` adds a third input to **Gate 2** (output $S$) and **Gate 6** (output $Q'$).

**(a) When `Clear = 0`:**
1. A 0 at any input of a NAND gate forces its output to 1:
   * **Gate 2** output **$S = 1$** (regardless of $CP$ and Gate 1).
   * **Gate 6** output **$Q' = 1$** (regardless of $R$ and $Q$).
2. **Gate 5** has inputs $S = 1$ and $Q' = 1$, so its output is:
   $$Q = \overline{S \cdot Q'} = \overline{1 \cdot 1} = 0$$
3. Thus $Q = 0, Q' = 1$ (cleared) and remains cleared for all $CP$ and $D$ values.

**(b) When `Clear = 1`:**
In a NAND gate, an input of `1` has no effect on the product ($X \cdot 1 = X$):
* **Gate 2** $= \overline{(\text{Gate 1}) \cdot CP \cdot 1} = \overline{(\text{Gate 1}) \cdot CP}$
* **Gate 6** $= \overline{Q \cdot R \cdot 1} = \overline{Q \cdot R}$

Both gates behave identically to Fig. 6-12, so normal clocked operation is unaffected.

---

### **Problem 6-9**
**Question:**
The full-adder of Fig. P6-10 receives two external inputs $x$ and $y$; the third input $z$ comes from the output of a *D* flip-flop. The carry output is transferred to the flip-flop every clock pulse. The external $S$ output gives the sum of $x, y,$ and $z$. Obtain the state table and state diagram of the sequential circuit.

**Easy Answer:**
Here $z = Q$ (present state), $D = C$, so:
* **Output (Sum):** $S = x \oplus y \oplus Q$
* **Next State (Carry):** $Q(t+1) = C = xy + xQ + yQ$

**State Table:**

| Present State $Q(t)$ | Inputs $xy$ | Next State $Q(t+1)$ | Output $S$ |
| :---: | :---: | :---: | :---: |
| 0 | 00 | 0 | 0 |
| 0 | 01 | 0 | 1 |
| 0 | 10 | 0 | 1 |
| 0 | 11 | 1 | 0 |
| 1 | 00 | 0 | 1 |
| 1 | 01 | 1 | 0 |
| 1 | 10 | 1 | 0 |
| 1 | 11 | 1 | 1 |

**State Diagram** *(labels are `xy/S`)*:
* Two state circles: **`0`** and **`1`**.
* **`0` $\rightarrow$ `0`** (self-loop): `00/0`, `01/1`, `10/1`
* **`0` $\rightarrow$ `1`**: `11/0`
* **`1` $\rightarrow$ `0`**: `00/1`
* **`1` $\rightarrow$ `1`** (self-loop): `01/0`, `10/0`, `11/1`

*(Note: This circuit works as a **serial binary adder**.)*

---

### **Problem 6-10**
**Question:**
Derive the state table and state diagram of the sequential circuit of Fig. P6-11. What is the function of the circuit?

**Easy Answer:**
Tracing the two OR gates driving the two $T$ flip-flops $A$ and $B$ *(note: in the printed diagram, $B'$ has an extra line accidentally touching $A$'s wire; the intended connection is $A$ to the right OR gate)*:
* $T_A = A' + B$
* $T_B = A + B$

Recall for a $T$ flip-flop: $Q(t+1) = Q \oplus T$ (toggles if $T=1$, no change if $T=0$).

**State Table:**

| Present State $AB$ | $T_A = A'+B$ | $T_B = A+B$ | Next State $A(t+1)B(t+1)$ |
| :---: | :---: | :---: | :---: |
| 00 | 1 | 0 | 10 |
| 01 | 1 | 1 | 10 |
| 10 | 0 | 1 | 11 |
| 11 | 1 | 1 | 00 |

**State Diagram:**
* **`00` $\rightarrow$ `10`**
* **`10` $\rightarrow$ `11`**
* **`11` $\rightarrow$ `00`**
* **`01` $\rightarrow$ `10`** *(unused state self-corrects into the main loop)*

**Function of the circuit:**
It is a **modulo-3 (divide-by-3) counter** that repeatedly cycles through the 3 states **`00` $\rightarrow$ `10` $\rightarrow$ `11` $\rightarrow$ `00`** (and automatically enters the cycle if it ever starts in `01`).

Here are the next 5 problems (**6-11 to 6-15**) from page 225, with full questions and complete, easy-to-follow answers.

---

### **Problem 6-11**
**Question:**
A sequential circuit has four flip-flops $A, B, C, D$ and an input $x$. It is described by the following state equations:
$$A(t+1) = (CD' + C'D)x + (CD + C'D')x'$$
$$B(t+1) = A$$
$$C(t+1) = B$$
$$D(t+1) = C$$
(a) Obtain the sequence of states when $x = 1$, starting from state $ABCD = 0001$.
(b) Obtain the sequence of states when $x = 0$, starting from state $ABCD = 0000$.

**Easy Answer:**
Notice that $B, C, D$ simply shift right each clock pulse ($A \to B \to C \to D$), while:
* When **$x = 1$**: $A(t+1) = CD' + C'D = C \oplus D$ (1 if $C \neq D$, 0 if $C = D$)
* When **$x = 0$**: $A(t+1) = CD + C'D' = (C \oplus D)'$ (1 if $C = D$, 0 if $C \neq D$)

**(a) Sequence when $x = 1$, starting from `0001`:**
$$0001 \to 1000 \to 0100 \to 0010 \to 1001 \to 1100 \to 0110 \to 1011 \to 0101 \to 1010 \to 1101 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \text{ (repeats)}$$

**(b) Sequence when $x = 0$, starting from `0000`:**
$$0000 \to 1000 \to 1100 \to 1110 \to 0111 \to 1011 \to 1101 \to 0110 \to 0011 \to 1001 \to 0100 \to 1010 \to 0101 \to 0010 \to 0001 \to 0000 \text{ (repeats)}$$

---

### **Problem 6-12**
**Question:**
A sequential circuit has two flip-flops ($A$ and $B$), two inputs ($x$ and $y$) and an output ($z$). The flip-flop input functions and the circuit output function are as follows:
$$JA = xB + y'B' \qquad KA = xy'B'$$
$$JB = xA' \qquad KB = xy' + A$$
$$z = xyA + x'y'B$$
Obtain the logic diagram, state table, state diagram, and state equations.

**Easy Answer:**

**1. Logic Diagram:**
Use two clocked *JK* flip-flops ($A$ and $B$, sharing clock $CP$) and inverters for $x'$ and $y'$ ($A'$ and $B'$ come from the flip-flop $Q'$ outputs):
* **$JA$:** two 2-input AND gates ($x \cdot B$ and $y' \cdot B'$) $\to$ 2-input OR gate $\to J_A$
* **$KA$:** one 3-input AND gate ($x \cdot y' \cdot B'$) $\to K_A$
* **$JB$:** one 2-input AND gate ($x \cdot A'$) $\to J_B$
* **$KB$:** one 2-input AND gate ($x \cdot y'$) $\to$ 2-input OR gate (with $A$) $\to K_B$
* **$z$:** two 3-input AND gates ($x \cdot y \cdot A$ and $x' \cdot y' \cdot B$) $\to$ 2-input OR gate $\to z$

**2. State Equations:**
Using $Q(t+1) = JQ' + K'Q$:
* **For $A$:**
  $$A(t+1) = (xB + y'B')A' + (xy'B')'A = xA'B + y'A'B' + (x' + y + B)A$$
  Since $x'A + xB$ already covers $xA'B$ and $AB$:
  $$A(t+1) = x'A + yA + xB + y'A'B'$$
* **For $B$:**
  $$B(t+1) = (xA')B' + (xy' + A)'B = xA'B' + (x' + y)A'B = xA'B' + x'A'B + yA'B$$

**3. State Table:**

| Present State $AB$ | Next State ($xy=00$) | Next State ($xy=01$) | Next State ($xy=10$) | Next State ($xy=11$) | Output $z$ ($00$) | Output $z$ ($01$) | Output $z$ ($10$) | Output $z$ ($11$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **00** | 10 | 00 | 11 | 01 | 0 | 0 | 0 | 0 |
| **01** | 01 | 01 | 10 | 11 | 1 | 0 | 0 | 0 |
| **10** | 10 | 10 | 00 | 10 | 0 | 0 | 0 | 1 |
| **11** | 10 | 10 | 10 | 10 | 1 | 0 | 0 | 1 |

**4. State Diagram** *(edges labeled `xy/z`)*:
* Four state circles: **`00`**, **`01`**, **`10`**, **`11`**.
* From **`00`**: `00/0` $\to$ `10`, `01/0` $\to$ `00` (self), `10/0` $\to$ `11`, `11/0` $\to$ `01`
* From **`01`**: `00/1, 01/0` $\to$ `01` (self), `10/0` $\to$ `10`, `11/0` $\to$ `11`
* From **`10`**: `00/0, 01/0, 11/1` $\to$ `10` (self), `10/0` $\to$ `00`
* From **`11`**: `00/1, 01/0, 10/0, 11/1` $\to$ `10`

---

### **Problem 6-13**
**Question:**
Reduce the number of states in the following state table and tabulate the reduced state table.
*(Table with states $a$ through $h$, inputs $x=0,1$, outputs $0/1$.)*

**Easy Answer:**
Find pairs of states that have the **same next states** and **same outputs** for both $x=0$ and $x=1$:

1. **$b$ and $e$** both go to $(d, c)$ with outputs $(0, 0)$ $\implies$ **$b = e$** (remove $e$, replace $e$ with $b$).
2. **$d$ and $h$** both go to $(g, a)$ with outputs $(1, 0)$ $\implies$ **$d = h$** (remove $h$, replace $h$ with $d$).
3. After replacing $e \to b$ and $h \to d$, **$a$ and $c$** both go to $(f, b)$ with outputs $(0, 0)$ $\implies$ **$a = c$** (remove $c$, replace $c$ with $a$).

No other states are equivalent (all remaining pairs differ in outputs or next-state outputs).

**Reduced State Table (5 states):**

| Present state | Next state ($x=0$) | Next state ($x=1$) | Output ($x=0$) | Output ($x=1$) |
| :---: | :---: | :---: | :---: | :---: |
| $a$ | $f$ | $b$ | 0 | 0 |
| $b$ | $d$ | $a$ | 0 | 0 |
| $d$ | $g$ | $a$ | 1 | 0 |
| $f$ | $f$ | $b$ | 1 | 1 |
| $g$ | $g$ | $d$ | 0 | 1 |

---

### **Problem 6-14**
**Question:**
Starting from state $a$ of the state table in problem 6-14 *(book typo for 6-13)*, find the output sequence generated with an input sequence `01110010011`.

**Easy Answer:**
Tracing through the **original table** of Problem 6-13:

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | Next |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State** | $a$ | $f$ | $b$ | $c$ | $e$ | $d$ | $g$ | $h$ | $g$ | $g$ | $h$ | $a$ |
| **Input ($x$)** | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | |
| **Output** | **0** | **1** | **0** | **0** | **0** | **1** | **1** | **1** | **0** | **1** | **0** | |

**Output sequence:** **`01000111010`**

---

### **Problem 6-15**
**Question:**
Repeat problem 6-15 *(book typo for 6-14)* using the reduced table of problem 6-14 *(6-13)*. Show that the same output sequence is obtained.

**Easy Answer:**
Tracing the same input sequence `01110010011` through the **reduced table** of Problem 6-13:

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | Next |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State** | $a$ | $f$ | $b$ | $a$ | $b$ | $d$ | $g$ | $d$ | $g$ | $g$ | $d$ | $a$ |
| **Input ($x$)** | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | |
| **Output** | **0** | **1** | **0** | **0** | **0** | **1** | **1** | **1** | **0** | **1** | **0** | |

**Output sequence:** **`01000111010`** — exact same output sequence as Problem 6-14!

Here are the next 5 problems (**6-16 to 6-20**) from pages 225–226, with full questions and complete, easy-to-follow answers.

---

### **Problem 6-16**
**Question:**
Substitute binary assignment 2 of Table 6-5 to the states in Table 6-4 and obtain the binary state table. Repeat with binary assignment 3.

**Easy Answer:**
From Table 6-5 (page 203):
* **Assignment 2:** $a=000,\; b=010,\; c=011,\; d=101,\; e=111$
* **Assignment 3:** $a=000,\; b=100,\; c=010,\; d=101,\; e=011$

Replacing each letter in Table 6-4 (page 201):

**Binary State Table (Assignment 2):**

| Present State | Next State ($x=0$) | Next State ($x=1$) | Output ($x=0$) | Output ($x=1$) |
| :---: | :---: | :---: | :---: | :---: |
| 000 | 000 | 010 | 0 | 0 |
| 010 | 011 | 101 | 0 | 0 |
| 011 | 000 | 101 | 0 | 0 |
| 101 | 111 | 101 | 0 | 1 |
| 111 | 000 | 101 | 0 | 1 |

**Binary State Table (Assignment 3):**

| Present State | Next State ($x=0$) | Next State ($x=1$) | Output ($x=0$) | Output ($x=1$) |
| :---: | :---: | :---: | :---: | :---: |
| 000 | 000 | 100 | 0 | 0 |
| 100 | 010 | 101 | 0 | 0 |
| 010 | 000 | 101 | 0 | 0 |
| 101 | 011 | 101 | 0 | 1 |
| 011 | 000 | 101 | 0 | 1 |

---

### **Problem 6-17**
**Question:**
Obtain the excitation table of the $JK'$ flip-flop described in problem 6-4.

**Easy Answer:**
From Problem 6-4, the characteristic equation is $Q(t+1) = JQ' + K'Q$:
* $0 \to 0$: works for $(J=0, K'=0)$ and $(J=0, K'=1)$ $\implies J=0, K'=X$
* $0 \to 1$: works for $(J=1, K'=0)$ and $(J=1, K'=1)$ $\implies J=1, K'=X$
* $1 \to 0$: works for $(J=0, K'=0)$ and $(J=1, K'=0)$ $\implies J=X, K'=0$
* $1 \to 1$: works for $(J=0, K'=1)$ and $(J=1, K'=1)$ $\implies J=X, K'=1$

**Excitation Table:**

| $Q(t)$ | $Q(t+1)$ | $J$ | $K'$ |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | $X$ |
| 0 | 1 | 1 | $X$ |
| 1 | 0 | $X$ | 0 |
| 1 | 1 | $X$ | 1 |

---

### **Problem 6-18**
**Question:**
Obtain the excitation table of the set-dominate flip-flop described in problem 6-5.

**Easy Answer:**
From Problem 6-5, $S=1, R=1$ sets $Q(t+1) = 1$:
* $0 \to 0$: works for $(0,0)$ or $(0,1)$ $\implies S=0, R=X$
* $0 \to 1$: works for $(1,0)$ or $(1,1)$ $\implies S=1, R=X$
* $1 \to 0$: only works for $(0,1)$ $\implies S=0, R=1$
* $1 \to 1$: works for $(0,0)$, $(1,0)$, or $(1,1)$ — i.e., **any input except $(0,1)$**, written as $S=X, R=0$ (or $S=1, R=X$)

**Excitation Table:**

| $Q(t)$ | $Q(t+1)$ | $S$ | $R$ |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | $X$ |
| 0 | 1 | 1 | $X$ |
| 1 | 0 | 0 | 1 |
| 1 | 1 | $X$ *(or 1)* | $0$ *(or X)* |

*(Note: For $1 \to 1$, any combination satisfying $S + R' = 1$ works.)*

---

### **Problem 6-19**
**Question:**
A sequential circuit has one input and one output. The state diagram is shown in Fig. P6-20. Design the sequential circuit with (a) *T* flip-flops, (b) *RS* flip-flops, and (c) *JK* flip-flops.

**Easy Answer:**
Let the 3 flip-flops be $A, B, C$ and the input be $x$. The unused states `101`, `110`, and `111` (minterms $10, 11, 12, 13, 14, 15$) are **don't-care ($X$)** conditions.

**State & Excitation Table (from Fig. P6-20):**

| Present $ABC$ | Input $x$ | Next $ABC$ | Output $y$ | **(a) $T_A\;T_B\;T_C$** | **(b) $S_A R_A\;\; S_B R_B\;\; S_C R_C$** | **(c) $J_A K_A\;\; J_B K_B\;\; J_C K_C$** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 000 | 0 | 000 | 0 | 0 0 0 | $0X\;\; 0X\;\; 0X$ | $0X\;\; 0X\;\; 0X$ |
| 000 | 1 | 011 | 1 | 0 1 1 | $0X\;\; 10\;\; 10$ | $0X\;\; 1X\;\; 1X$ |
| 001 | 0 | 001 | 0 | 0 0 0 | $0X\;\; 0X\;\; X0$ | $0X\;\; 0X\;\; X0$ |
| 001 | 1 | 100 | 1 | 1 0 1 | $10\;\; 0X\;\; 01$ | $1X\;\; 0X\;\; X1$ |
| 010 | 0 | 010 | 0 | 0 0 0 | $0X\;\; X0\;\; 0X$ | $0X\;\; X0\;\; 0X$ |
| 010 | 1 | 011 | 1 | 0 0 1 | $0X\;\; X0\;\; 10$ | $0X\;\; X0\;\; 1X$ |
| 011 | 0 | 001 | 0 | 0 1 0 | $0X\;\; 01\;\; X0$ | $0X\;\; X1\;\; X0$ |
| 011 | 1 | 100 | 0 | 1 1 1 | $10\;\; 01\;\; 01$ | $1X\;\; X1\;\; X1$ |
| 100 | 0 | 010 | 0 | 1 1 0 | $01\;\; 10\;\; 0X$ | $X1\;\; 1X\;\; 0X$ |
| 100 | 1 | 000 | 1 | 1 0 0 | $01\;\; 0X\;\; 0X$ | $X1\;\; 0X\;\; 0X$ |

**Output Function (same for all 3 designs):**
$$y = B'x + C'x$$

**Simplified Flip-Flop Input Functions (using K-maps with minterms $10\text{–}15 = X$):**

**(a) Using *T* flip-flops:**
* $T_A = A + Cx$
* $T_B = BC + Ax' + A'B'C'x$
* $T_C = A'x$

**(b) Using *RS* flip-flops:**
* $S_A = Cx, \qquad R_A = A$
* $S_B = A'C'x + Ax', \qquad R_B = C$
* $S_C = A'C'x, \qquad R_C = Cx$

**(c) Using *JK* flip-flops:**
* $J_A = Cx, \qquad K_A = 1$
* $J_B = A'C'x + Ax', \qquad K_B = C$
* $J_C = A'x, \qquad K_C = x$

*(The logic diagram for each case is drawn directly from its equations using 3 flip-flops $A, B, C$ sharing clock $CP$.)*

---

### **Problem 6-20**
**Question:**
Design the circuit of a 4-bit register that converts the binary number stored in the register to its 2's complement value when input $x = 1$. The flip-flops of the register are of the *RST* type. This flip-flop has three inputs: two inputs have *RS* capabilities and one has a *T* capability. The *RS* inputs are used to transfer the 4-bit number when an input $y = 1$. Use the *T* input for the conversion.

**Easy Answer:**
Let the 4 *RST* flip-flops be $A_3, A_2, A_1, A_0$ ($A_0$ = LSB, $A_3$ = MSB), with external 4-bit data inputs $I_3, I_2, I_1, I_0$ and common clock $CP$.

**1. Parallel Load ($RS$ inputs, controlled by $y$):**
When $y = 1$, $S_i = I_i$ and $R_i = I_i'$; when $y = 0$, $S_i = R_i = 0$.
For each flip-flop $i = 0, 1, 2, 3$:
$$S_i = y \cdot I_i, \qquad R_i = y \cdot I_i'$$

**2. 2's Complement Conversion ($T$ inputs, controlled by $x$):**
Rule for 2's complement: starting from the LSB, leave all trailing `0`s and the first `1` unchanged, and **complement (toggle) every bit to the left of the first `1`**.
* **$T_0 = 0$** *(LSB never changes in 2's complement)*
* **$T_1 = x \cdot A_0$** *(toggle $A_1$ if $A_0 = 1$)*
* **$T_2 = x \cdot (A_0 + A_1)$** *(toggle $A_2$ if $A_0$ or $A_1$ is $1$)*
* **$T_3 = x \cdot (A_0 + A_1 + A_2)$** *(toggle $A_3$ if $A_0, A_1,$ or $A_2$ is $1$)*

**Logic Diagram Connections:**
* **4 *RST* flip-flops** ($A_3, A_2, A_1, A_0$) all clocked by $CP$.
* **For each bit $i$:** 1 inverter ($I_i'$) and 2 AND gates for $S_i = y I_i$ and $R_i = y I_i'$.
* **For the $T$ inputs:**
  * $T_0$ connected to logic `0`.
  * $T_1 = x A_0$ (one 2-input AND gate).
  * $T_2 = x(A_0 + A_1)$ (one 2-input OR gate $\to$ one 2-input AND gate with $x$).
  * $T_3 = x(A_0 + A_1 + A_2)$ (OR $(A_0 + A_1)$ with $A_2$ $\to$ one 2-input AND gate with $x$).

Here are the next 5 problems (**6-21 to 6-25**) from pages 225–226, with full questions and complete, easy-to-follow answers.

---

### **Problem 6-21**
**Question:**
Repeat Example 6-1 with binary assignment 3 of Table 6-5. Use *JK* flip-flops.

**Easy Answer:**
From Assignment 3 (Problem 6-16): $a=000,\; b=100,\; c=010,\; d=101,\; e=011$.
The unused states are `001`, `110`, and `111`, which give 6 don't-care minterms: **2, 3, 12, 13, 14, 15**.

**Excitation Table:**

| Present $ABC$ | Input $x$ | Next $ABC$ | $J_A K_A$ | $J_B K_B$ | $J_C K_C$ | Output $y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 000 | 0 | 000 | $0X$ | $0X$ | $0X$ | 0 |
| 000 | 1 | 100 | $1X$ | $0X$ | $0X$ | 0 |
| 010 | 0 | 000 | $0X$ | $X1$ | $0X$ | 0 |
| 010 | 1 | 101 | $1X$ | $X1$ | $1X$ | 0 |
| 011 | 0 | 000 | $0X$ | $X1$ | $X1$ | 0 |
| 011 | 1 | 101 | $1X$ | $X1$ | $X0$ | 0 |
| 100 | 0 | 010 | $X1$ | $1X$ | $0X$ | 0 |
| 100 | 1 | 101 | $X0$ | $0X$ | $1X$ | 1 |
| 101 | 0 | 011 | $X1$ | $1X$ | $X0$ | 0 |
| 101 | 1 | 101 | $X0$ | $0X$ | $X0$ | 1 |

**Simplified Flip-Flop Input & Output Functions (via K-maps with minterms 2, 3, 12–15 = $X$):**
* $J_A = x, \qquad K_A = x'$
* $J_B = Ax', \qquad K_B = 1$
* $J_C = (A + B)x, \qquad K_C = A'x'$ *(or $Bx'$)*
* $y = Ax$

*(Logic diagram uses 3 *JK* flip-flops $A, B, C$ sharing $CP$, driven by the gates above.)*

---

### **Problem 6-22**
**Question:**
Design a BCD counter with *JK* flip-flops.

**Easy Answer:**
A BCD counter counts from `0000` (0) to `1001` (9) and returns to `0000`. States `1010`–`1111` (minterms **10–15**) are unused don't-care ($X$) conditions.

**Excitation Table:**

| Present $ABCD$ | Next $ABCD$ | $J_A K_A$ | $J_B K_B$ | $J_C K_C$ | $J_D K_D$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0000 | 0001 | $0X$ | $0X$ | $0X$ | $1X$ |
| 0001 | 0010 | $0X$ | $0X$ | $1X$ | $X1$ |
| 0010 | 0011 | $0X$ | $0X$ | $X0$ | $1X$ |
| 0011 | 0100 | $0X$ | $1X$ | $X1$ | $X1$ |
| 0100 | 0101 | $0X$ | $X0$ | $0X$ | $1X$ |
| 0101 | 0110 | $0X$ | $X0$ | $1X$ | $X1$ |
| 0110 | 0111 | $0X$ | $X0$ | $X0$ | $1X$ |
| 0111 | 1000 | $1X$ | $X1$ | $X1$ | $X1$ |
| 1000 | 1001 | $X0$ | $0X$ | $0X$ | $1X$ |
| 1001 | 0000 | $X1$ | $0X$ | $0X$ | $X1$ |

**Simplified Input Functions (via K-maps with minterms 10–15 = $X$):**
* $J_A = BCD, \qquad K_A = D$
* $J_B = CD, \qquad K_B = CD$
* $J_C = A'D, \qquad K_C = D$
* $J_D = 1, \qquad K_D = 1$

---

### **Problem 6-23**
**Question:**
Design a counter that counts the decimal digits according to the 2, 4, 2, 1 code (Table 1-2). Use *T* flip-flops.

**Easy Answer:**
In Table 1-2, the 2, 4, 2, 1 code for digits 0–9 is `0000, 0001, 0010, 0011, 0100, 1011, 1100, 1101, 1110, 1111`. The 6 unused states (`0101`–`1010`, minterms **5–10**) are don't-cares ($X$).

**Excitation Table:**

| Digit | Present $ABCD$ | Next $ABCD$ | $T_A$ | $T_B$ | $T_C$ | $T_D$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0000 | 0001 | 0 | 0 | 0 | 1 |
| 1 | 0001 | 0010 | 0 | 0 | 1 | 1 |
| 2 | 0010 | 0011 | 0 | 0 | 0 | 1 |
| 3 | 0011 | 0100 | 0 | 1 | 1 | 1 |
| 4 | 0100 | 1011 | 1 | 1 | 1 | 1 |
| 5 | 1011 | 1100 | 0 | 1 | 1 | 1 |
| 6 | 1100 | 1101 | 0 | 0 | 0 | 1 |
| 7 | 1101 | 1110 | 0 | 0 | 1 | 1 |
| 8 | 1110 | 1111 | 0 | 0 | 0 | 1 |
| 9 | 1111 | 0000 | 1 | 1 | 1 | 1 |

**Simplified Input Functions (via K-maps with minterms 5–10 = $X$):**
* $T_A = BCD + A'B$
* $T_B = CD + A'B$
* $T_C = D + A'B$
* $T_D = 1$

---

### **Problem 6-24**
**Question:**
Verify the circuit obtained in Example 6-5 by using the excitation table method.

**Easy Answer:**
Using the state equations of Example 6-5:
* $A(t+1) = A'B'CD + A'B'C + ACD + AC'D' = A'B'C + A(CD + C'D')$
* $B(t+1) = A'C + CD' + A'BC = A'C + CD'$
* $C(t+1) = B$
* $D(t+1) = D'$

**16-Row Excitation Table:**

| $ABCD$ | Next $ABCD$ | $J_A K_A$ | $J_B K_B$ | $J_C K_C$ | $J_D K_D$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0000 | 0001 | $0X$ | $0X$ | $0X$ | $1X$ |
| 0001 | 0000 | $0X$ | $0X$ | $0X$ | $X1$ |
| 0010 | 1101 | $1X$ | $1X$ | $X1$ | $1X$ |
| 0011 | 1100 | $1X$ | $1X$ | $X1$ | $X1$ |
| 0100 | 0011 | $0X$ | $X1$ | $1X$ | $1X$ |
| 0101 | 0010 | $0X$ | $X1$ | $1X$ | $X1$ |
| 0110 | 0111 | $0X$ | $X0$ | $X0$ | $1X$ |
| 0111 | 0110 | $0X$ | $X0$ | $X0$ | $X1$ |
| 1000 | 1001 | $X0$ | $0X$ | $0X$ | $1X$ |
| 1001 | 0000 | $X1$ | $0X$ | $0X$ | $X1$ |
| 1010 | 0101 | $X1$ | $1X$ | $X1$ | $1X$ |
| 1011 | 1000 | $X0$ | $0X$ | $X1$ | $X1$ |
| 1100 | 1011 | $X0$ | $X1$ | $1X$ | $1X$ |
| 1101 | 0010 | $X1$ | $X1$ | $1X$ | $X1$ |
| 1110 | 0111 | $X1$ | $X0$ | $X0$ | $1X$ |
| 1111 | 1010 | $X0$ | $X1$ | $X0$ | $X1$ |

**K-map Results & Verification:**
* $J_A = B'C, \quad K_A = CD' + C'D$ *(matches Example 6-5)*
* $J_B = A'C + CD'$ *(matches Example 6-5)*
* **$K_B = C' + AD$** *(Note: Example 6-5 has a typo $K_B = AC' + AD$, which fails for states `0100` and `0101` because $(A'C')B$ was written instead of $(A'C)B$ in its derivation!)*
* $J_C = B, \quad K_C = B'$ *(matches Example 6-5)*
* $J_D = 1, \quad K_D = 1$ *(matches Example 6-5)*

---

### **Problem 6-25**
**Question:**
Design the sequential circuit described by the following state equations. Use *JK* flip-flops.
$$A(t+1) = xAB + yA'C + xy$$
$$B(t+1) = xAC + y'BC'$$
$$C(t+1) = x'B + yAB'$$

**Easy Answer:**
Match each state equation to the *JK* characteristic equation $Q(t+1) = (J)Q' + (K')Q$:

**1. Flip-flop $A$:**
$$A(t+1) = xAB + yA'C + xy(A' + A) = (yC + xy)A' + (xB + xy)A$$
* **$J_A = yC + xy$**
* **$K_A = (xB + xy)' = x' + B'y'$**

**2. Flip-flop $B$:**
$$B(t+1) = xAC(B' + B) + y'BC' = (xAC)B' + (xAC + y'C')B$$
* **$J_B = xAC$**
* **$K_B = (xAC + y'C')' = yC' + x'C + A'C$**

**3. Flip-flop $C$:**
$$C(t+1) = (x'B + yAB')(C' + C) = (x'B + yAB')C' + (x'B + yAB')C$$
* **$J_C = x'B + yAB'$**
* **$K_C = (x'B + yAB')' = xB + y'B' + A'B'$**

*(The circuit is implemented with 3 *JK* flip-flops $A, B, C$ sharing $CP$, with their $J$ and $K$ inputs driven by these Boolean functions.)*


