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