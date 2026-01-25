![[Pasted image 20260125015711.png|946]]  
![[Pasted image 20260125214811.png]]

![[Pasted image 20260125185054.png]]
![[Pasted image 20260125185149.png]]
![[Pasted image 20260125185159.png]]
###  5️⃣ Positive-Edge Triggered Version


![[Pasted image 20260125020808.png]]
![https://www.allaboutcircuits.com/uploads/articles/positive-edge-triggered-d-latch-response.jpg](https://www.allaboutcircuits.com/uploads/articles/positive-edge-triggered-d-latch-response.jpg)

### How it’s modified

- Add **one extra inverter** in the clock path

### **Related Theory Page Locations**
*   **Latches (SR, D):** Pages 193–196 (Section 5.3)
*   **Flip-Flops (D, JK, T):** Pages 196–203 (Section 5.4)
*   **Characteristic Tables:** Pages 201–202 (Section 5.4)
*   **Characteristic Equations:** Page 203 (Section 5.4)
*   **Analysis of Sequential Circuits:** Pages 204–209 (Section 5.5)
*   **Excitation Tables:** Pages 240–241 (Section 5.8)

---

### **Problem 5.1**
**Problem:** The D latch of Fig. 5.6 is constructed with four NAND gates and an inverter. Consider the following three other ways for obtaining a D latch. In each case, draw the logic diagram and verify the circuit operation.
(a) Use NOR gates for the SR latch part and AND gates for the other two. An inverter may be needed.
(b) Use NOR gates for all four gates. Inverters may be needed.
(c) Use four NAND gates only (without an inverter). This can be done by connecting the output of the upper gate in Fig. 5.6 (the gate that goes to the SR latch) to the input of the lower gate (instead of the inverter output).

**Solution:**

**(a) Using NOR SR latch and AND gates**
*   **Construction:** An SR latch made with NOR gates behaves such that $S=1, R=0$ sets it ($Q=1$) and $S=0, R=1$ resets it ($Q=0$). The inputs must be active high.
*   **Logic:** We use two AND gates to steer the Enable ($En$) and Data ($D$) signals.
    *   Set input $S = En \cdot D$
    *   Reset input $R = En \cdot D'$ (requires an inverter for $D$)
*   **Operation Verification:**
    *   If $En=0$: $S=0, R=0$. The NOR latch holds its state.
    *   If $En=1, D=1$: $S=1, R=0$. The latch sets ($Q=1$).
    *   If $En=1, D=0$: $S=0, R=1$. The latch resets ($Q=0$).
*   **Diagram Description:** $D$ and $En$ enter an AND gate (output to S). $D$ is inverted and enters a second AND gate with $En$ (output to R). S and R drive a standard NOR cross-coupled latch.

**(b) Using NOR gates for all four gates**
*   **Construction:** We replace the AND gates from part (a) with NOR gates.
*   **Logic:** We need to generate the active-high S and R signals for the NOR latch using NOR gates.
    *   $S_{input} = (D' + En')'$ which is equivalent to $D \cdot En$.
    *   $R_{input} = (D + En')'$ which is equivalent to $D' \cdot En$.
*   **Diagram Description:** This requires inverters for the inputs $D$ and $En$ to work properly with the input NOR gates to produce the AND logic.
    *   Input $En$ is inverted to $En'$.
    *   Input $D$ is inverted to $D'$.
    *   Gate 1 (top): Inputs $D', En'$. Output $S = (D' + En')' = D \cdot En$.
    *   Gate 2 (bottom): Inputs $D, En'$. Output $R = (D + En')' = D' \cdot En$.
    *   Gate 3 & 4: Standard cross-coupled NOR latch driven by S and R.

**(c) Using four NAND gates only (no inverter)**
![[dlatch.gif]]
*   **Construction:** This modifies the standard NAND D-latch (Fig 5.6) to remove the inverter. In Fig 5.6, the top steering NAND gate outputs $(D \cdot En)'$. This signal is fed to the set input of the active-low SR latch. The bottom steering NAND gate usually takes $D'$ and $En$.
*   **Modification:** Connect the output of the top steering NAND gate directly to the data input of the bottom steering NAND gate.
*   **Verification:**
    *   Let Gate 1 be the top steering gate. Output $G1 = (D \cdot En)'$.
    *   Let Gate 2 be the bottom steering gate. Its inputs are now $En$ and $G1$.
    *   Output $G2 = (En \cdot G1)' = (En \cdot (D \cdot En)')' = (En \cdot (D' + En'))' = (En \cdot D')'$.
    *   The output $G2$ is exactly the same as if we had inverted D ($D'$) and NANDed it with $En$.
    *   Therefore, if $En=1, D=1 \rightarrow G1=0, G2=1$ (Set state).
    *   If $En=1, D=0 \rightarrow G1=1, G2=0$ (Reset state).
    *   If $En=0 \rightarrow G1=1, G2=1$ (Quiescent/Hold state).

---

### **Problem 5.2**
**Problem:** Construct a JK flip-flop using a D flip-flop, a two-to-one-line multiplexer, and an inverter.

**Solution:**

![[Pasted image 20260125184909.png]]  
![[Pasted image 20260125185005.png]]

To construct a JK flip-flop using a D flip-flop, we must match the next-state behavior.
*   **JK Flip-Flop Characteristic Equation:** $Q(t+1) = JQ' + K'Q$
*   **D Flip-Flop Characteristic Equation:** $Q(t+1) = D$
*   **Mapping:** By equating the two, we need to generate an input $D$ such that:
    $$D = JQ' + K'Q$$
*   **Using a 2-to-1 Multiplexer:**
    *   A MUX has output $Y$ based on Select ($S$) and inputs $I_0, I_1$: $Y = S'I_0 + SI_1$.
    *   If we connect the flip-flop output $Q$ to the Select line ($S=Q$):
        $$Y = Q'I_0 + QI_1$$
    *   Comparing this to the target equation $D = Q'J + QK'$:
        *   $I_0$ corresponds to $J$.
        *   $I_1$ corresponds to $K'$.
*   **Construction:**
    1.  Connect the **Q output** of the D flip-flop to the **Select** input of the MUX.
    2.  Connect input **J** to the **$I_0$** (0) data input of the MUX.
    3.  Connect input **K** to an **Inverter**, and connect the inverter output ($K'$) to the **$I_1$** (1) data input of the MUX.
    4.  Connect the **Output Y** of the MUX to the **D input** of the flip-flop.
    5.  Use the same clock for the flip-flop.

---

### **Problem 5.3**
**Problem:** Show that the characteristic equation for the complement output of a JK flip-flop is $Q'(t + 1) = J'Q' + KQ$.

**Solution:**
The characteristic equation for the normal output $Q$ is:
$$Q(t+1) = JQ' + K'Q$$

To find the equation for the complement output $Q'(t+1)$, we complement the entire next-state function:
$$Q'(t+1) = (JQ' + K'Q)'$$

Using DeMorgan's Law $(A+B)' = A'B'$:
$$Q'(t+1) = (JQ')' \cdot (K'Q)'$$

Using DeMorgan's Law $(AB)' = A'+B'$:
$$Q'(t+1) = (J' + Q) \cdot (K + Q')$$

Expand the terms:
$$Q'(t+1) = J'K + J'Q' + QK + QQ'$$

Since $QQ' = 0$:
$$Q'(t+1) = J'K + J'Q' + KQ$$

Using the consensus theorem or K-map simplification (where inputs are J, K, Q'):
We can show that the term $J'K$ is redundant or subsumed when grouping 1s for the complementary function.
Alternatively, looking at the logic:
*   The flip-flop output $Q'$ becomes 1 (Sets) when $K=1$ (Reset Q) or holds 1 when $J=0$.
*   Simplifying the expression derived above:
    $$Q'(t+1) = J'Q' + KQ$$
    *(Note: $J'K$ is covered because if $J=0, K=1$, then $J'Q'$ covers cases where $Q'=1$ and $KQ$ covers cases where $Q=1$ ($Q'=0$)).*

**Final Equation:** $Q'(t + 1) = J'Q' + KQ$

---

### **Problem 5.5**
**Problem:** Explain the differences among a truth table, a state table, a characteristic table, and an excitation table. Also, explain the difference among a Boolean equation, a state equation, a characteristic equation, and a flip-flop input equation.

**Solution:**

**Tables:**
1.  **Truth Table:** Used for *combinational* circuits. Lists the output values for every possible combination of input values. It does not involve time or internal state.
2.  **State Table:** Used for *sequential* circuits analysis. It lists the "Next State" and "Output" for every combination of "Present State" and "Input". It fully describes the sequential machine's behavior.
3.  **Characteristic Table:** Used to define the operation of a specific *flip-flop*. It lists the "Next State" of the flip-flop ($Q_{n+1}$) for every combination of its specific control inputs (like J, K or D) and current state ($Q_n$).
4.  **Excitation Table:** Used for the *design* of sequential circuits. It lists the required flip-flop inputs (e.g., what J and K must be) to achieve a specific change of state (e.g., $0 \rightarrow 1$ or $1 \rightarrow 1$).

**Equations:**
1.  **Boolean Equation:** Describes the logic function of a combinational circuit output in terms of its inputs. Example: $F = AB + C$.
2.  **State Equation:** An algebraic expression for a sequential circuit that specifies the Next State variables as a function of Present State variables and Inputs. Example: $A(t+1) = A(t)x + B(t)$.
3.  **Characteristic Equation:** A specific algebraic definition for a flip-flop type, derived from its characteristic table. It defines the next state of the flip-flop based on inputs. Example for D-FF: $Q(t+1) = D$.
4.  **Flip-Flop Input Equation:** Boolean equations derived during design that describe the combinational logic driving the inputs of the flip-flops (excitation inputs). Example: $J_A = xB, K_A = x$.

---

### **Problem 5.6**
**Problem:** A sequential circuit with two D flip-flops A and B, two inputs, x and y; and one output z is specified by the following next-state and output equations:
$A(t + 1) = x'y + xB$
$B(t + 1) = x'A + xB$
$z = A$
(a) Draw the logic diagram of the circuit.
(b) List the state table for the sequential circuit.
(c) Draw the corresponding state diagram.

