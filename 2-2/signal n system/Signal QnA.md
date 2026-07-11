# 1. System Properties
### The system relationship is given by: $$y(t) = \text{Re}\{x(t)\}$$To prove a system is linear, it must satisfy both **additivity** and **homogeneity**. Let's test each property.

#### **1. Testing the Additivity Property**

The additivity property states that if $x_1(t) \rightarrow y_1(t)$ and $x_2(t) \rightarrow y_2(t)$, then an input of $x_1(t) + x_2(t)$ must produce an output of $y_1(t) + y_2(t)$.

1. Find the individual outputs:
    
    $$y_1(t) = \text{Re}\{x_1(t)\}$$
    
    $$y_2(t) = \text{Re}\{x_2(t)\}$$
    
    Sum of individual outputs: $y_1(t) + y_2(t) = \text{Re}\{x_1(t)\} + \text{Re}\{x_2(t)\}$
    
2. Find the system's response to a combined input $x_3(t) = x_1(t) + x_2(t)$:
    
    $$y_3(t) = \text{Re}\{x_1(t) + x_2(t)\}$$
    
3. Using the mathematical identity of complex numbers where $\text{Re}\{z_1 + z_2\} = \text{Re}\{z_1\} + \text{Re}\{z_2\}$, we can expand $y_3(t)$:
    
    $$y_3(t) = \text{Re}\{x_1(t)\} + \text{Re}\{x_2(t)\}$$
    

Since $y_3(t) = y_1(t) + y_2(t)$, the system **satisfies the additivity property**.

#### **2. Testing the Homogeneity Property**

The homogeneity property states that scaling the input by an arbitrary constant $k$ must scale the output by that same constant $k$ ($k \cdot x(t) \rightarrow k \cdot y(t)$). As suggested by the hint, let's test what happens when $k$ is a complex number, such as $k = j$.

1. Scale the original output by $k = j$:
    
    $$j \cdot y(t) = j \cdot \text{Re}\{x(t)\}$$
    
2. Pass a scaled input $x_k(t) = j \cdot x(t)$ into the system to find the new output $y_k(t)$:
    
    $$y_k(t) = \text{Re}\{j \cdot x(t)\}$$
    
3. Let $x(t)$ be represented in its real and imaginary parts as $x(t) = x_r(t) + jx_i(t)$:
    
    $$y_k(t) = \text{Re}\{j \cdot (x_r(t) + jx_i(t))\}$$
    
    $$y_k(t) = \text{Re}\{jx_r(t) + j^2x_i(t)\}$$
    
    Since $j^2 = -1$:
    
    $$y_k(t) = \text{Re}\{-x_i(t) + jx_r(t)\}$$
    
    Taking the real part of this expression yields:
    
    $$y_k(t) = -x_i(t)$$
    
4. Compare the two results:
    
    - **Expected output if linear:** $j \cdot \text{Re}\{x(t)\} = j \cdot x_r(t)$
        
    - **Actual system output:** $-x_i(t)$
        

Clearly, $-x_i(t) \neq j \cdot x_r(t)$. Because the actual output does not equal the expected scaled output when $k$ is complex, the system **violates the homogeneity property**.
### Q.1 (a) A system H has its input-output pairs given. Determine whether the system could be memoryless, causal, linear, and time invariant. For all cases justify your answers. (Figure involved)
![[Pasted image 20260626191842.png]]
**Solution:**

Let's analyze the system properties based on the provided input-output pairs.

*   **Memoryless:** A system is memoryless if its output at any given time $t$ depends only on the input at that exact same time $t$.
    *   Observe the first pair: The input $x_1(t)$ is zero for $t > 1$. However, the corresponding output $y_1(t)$ is non-zero in the interval $1 < t < 2$. For example, at $t = 1.5$, the input $x_1(1.5) = 0$, but the output $y_1(1.5) = 0.5$. Because the output is non-zero when the present input is zero, the system relies on past input values.
    *   **Conclusion:** The system is **not memoryless** (it has memory).

*   **Causal:** A system is causal if the output at any time $t$ does not depend on future inputs. Graphically, this means the output cannot start before the input starts.
    *   For the first pair, $x_1(t)$ starts at $t=0$ and $y_1(t)$ starts at $t=0$.
    *   For the second pair, $x_2(t)$ starts at $t=2$ and $y_2(t)$ starts at $t=2$.
    *   For the third pair, $x_3(t)$ starts at $t=0$ and $y_3(t)$ starts at $t=0$.
    *   In all given cases, the output never precedes the input.
    *   **Conclusion:** Based on the given pairs, the system **could be causal**.

*   **Linear:** A linear system must satisfy the principle of superposition (both additivity and homogeneity). Let's test the additivity property using the given signals.
    *   Notice the relationship between the inputs: $x_3(t)$ consists of a positive pulse from $t=0$ to $1$ and another positive pulse from $t=2$ to $3$. We can express this as a linear combination of the first two inputs: $x_3(t) = x_1(t) - x_2(t)$. (Subtracting the negative pulse $x_2$ creates a positive pulse).
    *   If the system were linear, the response to $x_3(t)$ must follow the same relationship: $y_{expected}(t) = y_1(t) - y_2(t)$.
    *   Let's find $y_{expected}(t) = y_1(t) - y_2(t)$. $y_1(t)$ is a positive triangle from 0 to 2. $y_2(t)$ is a negative triangle from 2 to 4. Subtracting $y_2(t)$ is equivalent to adding a positive triangle from 2 to 4. Thus, a linear system's output would be two *positive* triangles.
    *   However, the actual given output $y_3(t)$ consists of a positive triangle from 0 to 2 and a *negative* triangle from 2 to 4. This actual output is equal to $y_1(t) + y_2(t)$.
    *   Since $y_3(t) \neq y_1(t) - y_2(t)$, the additivity property fails.
    *   **Conclusion:** The system is **not linear**.

*   **Time-Invariant:** A system is time-invariant if a time shift in the input results in an identical time shift in the output.
    *   Let's compare the first two pairs. We can observe that the input $x_2(t)$ is a shifted and inverted version of $x_1(t)$. Specifically, $x_2(t) = -x_1(t-2)$.
    *   Looking at the corresponding outputs, we see that $y_2(t)$ is exactly the shifted and inverted version of $y_1(t)$. Specifically, $y_2(t) = -y_1(t-2)$.
    *   This specific input-output relationship is perfectly consistent with a time-invariant system (it also shows homogeneity for a scaling factor of -1, despite failing general linearity). There is no evidence in the provided graphs that contradicts time-invariance.
    *   **Conclusion:** Based on the given pairs, the system **could be time invariant**.

Location pg 98 In pdf

***

### Q.1 (b) Consider the system shown in the following figure, determine is it (i) memory less (ii) Causal (iii) time-invariant ? Figure involved.
![[Pasted image 20260626191633.png]]

**Solution:**

From the given block diagram, the system's input-output relationship is described by the equation:
$$y(t) = x(t)\cos(\omega_c t)$$
Let's analyze the properties based on this mathematical model.

**(i) Memoryless:**
A system is memoryless (instantaneous) if the output $y(t)$ at any given time $t$ depends *only* on the input $x(t)$ at that exact same instant $t$, and not on past or future values.
In the equation $y(t) = x(t)\cos(\omega_c t)$, to find $y$ at a specific time (e.g., $t=5$), we only need the value of $x$ at $t=5$ (i.e., $x(5)$) multiplied by a constant coefficient for that instant ($\cos(5\omega_c)$). It does not require $x(4)$ or $x(6)$.
**Conclusion:** The system is **memoryless**.

**(ii) Causal:**
A system is causal if the output at any time $t$ depends only on present and past inputs, not on future inputs.
Since we established the system is memoryless, it depends *only* on the present input. Because it does not depend on future inputs, it strictly satisfies the definition of causality. (All memoryless systems are inherently causal).
**Conclusion:** The system is **causal**.

**(iii) Time-invariant:**
A system is time-invariant if a time shift in the input signal $x(t-T)$ results in an identical time shift in the output signal $y(t-T)$. Let's test this.
*   **Step 1: Delay the input.** Apply a delayed input $x_1(t) = x(t-T)$ to the system. The corresponding output $y_1(t)$ is:
    $$y_1(t) = x_1(t)\cos(\omega_c t) = x(t-T)\cos(\omega_c t)$$
*   **Step 2: Delay the original output.** Take the original output expression $y(t)$ and substitute $t$ with $(t-T)$:
    $$y(t-T) = x(t-T)\cos(\omega_c(t-T))$$
*   **Step 3: Compare.**
    Does $y_1(t) = y(t-T)$ for all $t$ and $T$?
    $$x(t-T)\cos(\omega_c t) \neq x(t-T)\cos(\omega_c t - \omega_c T)$$
    Because the internal oscillator $\cos(\omega_c t)$ depends explicitly on the absolute time variable $t$, delaying the input does not delay the oscillator. The outputs are not equal.
**Conclusion:** The system is **time-variant** (not time-invariant).

Location pg 104 In pdf

### Q.1 (c) Determine which of the following system is linear or non-linear? (i) $\frac{dy(t)}{dt} + t^2y(t) = (2t+3)x(t)$ (ii) $y(t)\frac{dy(t)}{dt} + 3y(t) = x(t)$

**Solution:**

A system is linear if it satisfies the principle of superposition, which consists of the additivity and homogeneity (scaling) properties. If $x_1(t) \to y_1(t)$ and $x_2(t) \to y_2(t)$, then $a x_1(t) + b x_2(t) \to a y_1(t) + b y_2(t)$.

**(i) $\frac{dy(t)}{dt} + t^2y(t) = (2t+3)x(t)$**
Let's test for linearity.
Assume input $x_1(t)$ produces output $y_1(t)$:
$$\frac{dy_1(t)}{dt} + t^2y_1(t) = (2t+3)x_1(t)$$  --- (Eq A)
Assume input $x_2(t)$ produces output $y_2(t)$:
$$\frac{dy_2(t)}{dt} + t^2y_2(t) = (2t+3)x_2(t)$$  --- (Eq B)

Multiply (Eq A) by constant $a$ and (Eq B) by constant $b$, and add them together:
$$a\frac{dy_1(t)}{dt} + at^2y_1(t) + b\frac{dy_2(t)}{dt} + bt^2y_2(t) = a(2t+3)x_1(t) + b(2t+3)x_2(t)$$
Using the linear properties of derivatives, we can group the terms:
$$\frac{d}{dt}[a y_1(t) + b y_2(t)] + t^2[a y_1(t) + b y_2(t)] = (2t+3)[a x_1(t) + b x_2(t)]$$
Let the combined input be $x_3(t) = a x_1(t) + b x_2(t)$ and the combined output be $y_3(t) = a y_1(t) + b y_2(t)$. Substituting these into the grouped equation yields:
$$\frac{dy_3(t)}{dt} + t^2y_3(t) = (2t+3)x_3(t)$$
This shows that the linear combination of inputs $x_3(t)$ produces the exact corresponding linear combination of outputs $y_3(t)$ according to the original system equation. The time-varying coefficients $t^2$ and $(2t+3)$ do not violate linearity, as they act as independent multipliers that do not depend on the amplitude of $x$ or $y$.
**Conclusion:** System (i) is **Linear**.

**(ii) $y(t)\frac{dy(t)}{dt} + 3y(t) = x(t)$**
Let's test the homogeneity (scaling) property. If the input is scaled by a factor $k$, the output should scale by the same factor $k$.
Assume input $x_1(t)$ produces $y_1(t)$:
$$y_1(t)\frac{dy_1(t)}{dt} + 3y_1(t) = x_1(t)$$
Now, apply an input scaled by $k$: let $x_2(t) = k x_1(t)$. If the system is linear, the expected output should be $y_2(t) = k y_1(t)$. Let's substitute this expected output into the left-hand side (LHS) of the system equation to see if it equals the new input $x_2(t)$:
LHS $= [k y_1(t)] \frac{d}{dt}[k y_1(t)] + 3[k y_1(t)]$
LHS $= k^2 y_1(t) \frac{dy_1(t)}{dt} + 3k y_1(t)$
Because of the multiplication of $y(t)$ with its own derivative, a $k^2$ term appears. We can factor out $k$, but not $k^2$ from the whole expression to match the right side.
LHS $= k \left[ k y_1(t) \frac{dy_1(t)}{dt} + 3 y_1(t) \right] \neq k \left[ y_1(t) \frac{dy_1(t)}{dt} + 3 y_1(t) \right] = k x_1(t) = x_2(t)$
Since the LHS does not equal the RHS for a scaled input (unless $k=1$ or $k=0$), the homogeneity property fails.
**Conclusion:** System (ii) is **Non-linear**.

Location pg 101 In pdf

### Q.1 (a) A system is specified by its input-output relationship as $y(t) = \frac{x^2(t)}{dx/dt}$. Show that the system satisfies the homogeneity property but not the additivity property.

**Detailed Answer:**

To determine if a system is linear, it must satisfy the principle of superposition, which consists of two properties: homogeneity (scaling) and additivity.

Given the system equation:
$$y(t) = \frac{x^2(t)}{\frac{dx(t)}{dt}}$$
Let's denote the derivative of $x(t)$ as $\dot{x}(t)$ for simplicity. So, $y(t) = \frac{x^2(t)}{\dot{x}(t)}$.

**1. Checking Homogeneity (Scaling Property):**
The homogeneity property states that if an input $x(t)$ produces an output $y(t)$, then a scaled input $kx(t)$ (where $k$ is a constant) should produce a scaled output $k y(t)$.
Let the new input be $x_k(t) = k x(t)$.
The corresponding output $y_k(t)$ is:
$$y_k(t) = \frac{(x_k(t))^2}{\frac{d x_k(t)}{dt}}$$
Substitute $x_k(t) = k x(t)$:
$$y_k(t) = \frac{(k x(t))^2}{\frac{d (k x(t))}{dt}}$$
$$y_k(t) = \frac{k^2 x^2(t)}{k \frac{dx(t)}{dt}}$$
$$y_k(t) = k \left( \frac{x^2(t)}{\dot{x}(t)} \right)$$
$$y_k(t) = k y(t)$$
Since the output is scaled by the same factor $k$ as the input, the system **satisfies the homogeneity property**.

**2. Checking Additivity Property:**
The additivity property states that if an input $x_1(t)$ produces $y_1(t)$ and an input $x_2(t)$ produces $y_2(t)$, then an input $x_1(t) + x_2(t)$ should produce an output $y_1(t) + y_2(t)$.

Let the respective outputs for $x_1(t)$ and $x_2(t)$ be:
$y_1(t) = \frac{x_1^2(t)}{\dot{x}_1(t)}$
$y_2(t) = \frac{x_2^2(t)}{\dot{x}_2(t)}$

The sum of the individual outputs is:
$$y_1(t) + y_2(t) = \frac{x_1^2(t)}{\dot{x}_1(t)} + \frac{x_2^2(t)}{\dot{x}_2(t)} = \frac{x_1^2(t)\dot{x}_2(t) + x_2^2(t)\dot{x}_1(t)}{\dot{x}_1(t)\dot{x}_2(t)}$$

Now, let's apply the combined input $x_{12}(t) = x_1(t) + x_2(t)$ to the system. The new output $y_{12}(t)$ is:
$$y_{12}(t) = \frac{(x_1(t) + x_2(t))^2}{\frac{d}{dt}(x_1(t) + x_2(t))}$$
$$y_{12}(t) = \frac{x_1^2(t) + 2x_1(t)x_2(t) + x_2^2(t)}{\dot{x}_1(t) + \dot{x}_2(t)}$$

Comparing the two results:
$$\frac{x_1^2(t) + 2x_1(t)x_2(t) + x_2^2(t)}{\dot{x}_1(t) + \dot{x}_2(t)} \neq \frac{x_1^2(t)\dot{x}_2(t) + x_2^2(t)\dot{x}_1(t)}{\dot{x}_1(t)\dot{x}_2(t)}$$
Since $y_{12}(t) \neq y_1(t) + y_2(t)$, the system **does not satisfy the additivity property**.

Because it fails the additivity condition, the system is non-linear.

always mention ans related location pg no. In pdf , at the end of every soln 1.7-1 Linear and Nonlinear Systems, pg. 97-98

***

### Q.1 (a) A system is specified by its input-output relationship as $y(t) = \frac{x^2(t)}{dx/dt}$. Show that the system satisfies the homogeneity property but not the additivity property.

**Detailed Answer:**

To determine if a system is linear, it must satisfy the principle of superposition, which consists of two properties: homogeneity (scaling) and additivity.

Given the system equation:
$$y(t) = \frac{x^2(t)}{\frac{dx(t)}{dt}}$$
Let's denote the derivative of $x(t)$ as $\dot{x}(t)$ for simplicity. So, $y(t) = \frac{x^2(t)}{\dot{x}(t)}$.

**1. Checking Homogeneity (Scaling Property):**
The homogeneity property states that if an input $x(t)$ produces an output $y(t)$, then a scaled input $kx(t)$ (where $k$ is a constant) should produce a scaled output $k y(t)$.
Let the new input be $x_k(t) = k x(t)$.
The corresponding 

***

### Q.2 (a) The input-output relationship of a system is shown below.
$y(t) = \begin{cases} V_{cc}, & x(t) > V_{ref} \\ -V_{cc}, & x(t) < -V_{ref} \\ 2x(t), & \text{otherwise} \end{cases}$
Justify whether the system is (i) Invertible (ii) BIBO stable

**Solution:**

**(i) Invertibility:**
A system is invertible if unique inputs always produce unique outputs. This means there is a one-to-one mapping between the input and output; observing the output allows you to perfectly reconstruct the input.
Let's analyze the given piecewise function, which represents a clipping or saturation amplifier.
Suppose $V_{ref} = 5$ V and $V_{cc} = 10$ V.
*   If we apply an input $x_1(t) = 6$ V, the condition $x(t) > V_{ref}$ is met, so the output is $y_1(t) = V_{cc} = 10$ V.
*   If we apply a different input $x_2(t) = 8$ V, the condition $x(t) > V_{ref}$ is still met, so the output is $y_2(t) = V_{cc} = 10$ V.
Because multiple different input values (any value $> V_{ref}$) map to the exact same output value ($V_{cc}$), the mapping is many-to-one. If you observe an output of $V_{cc}$, it is impossible to know what the specific original input was, only that it was greater than $V_{ref}$. The operation cannot be undone.
**Conclusion:** The system is **not invertible**.

**(ii) BIBO Stability:**
A system is Bounded-Input Bounded-Output (BIBO) stable if every bounded input results in a bounded output.
Let the input $x(t)$ be bounded such that its magnitude never exceeds a finite constant $M_x$: $|x(t)| \le M_x < \infty$ for all $t$.
We must examine the output $y(t)$ in all three defined regions:
1.  For $x(t) > V_{ref}$, $|y(t)| = |V_{cc}|$.
2.  For $x(t) < -V_{ref}$, $|y(t)| = |-V_{cc}| = |V_{cc}|$.
3.  For $-V_{ref} \le x(t) \le V_{ref}$ (the "otherwise" case), $|y(t)| = |2x(t)|$. Since $|x(t)|$ is bounded in this region by $V_{ref}$, the maximum output is $|2V_{ref}|$.

Therefore, for any valid input, the maximum possible amplitude of the output is strictly bounded by $M_y = \max(|V_{cc}|, |2V_{ref}|)$. Since $V_{cc}$ and $V_{ref}$ are hardware constants, the output amplitude can never exceed this finite boundary, regardless of how large the bounded input $M_x$ might be (in fact, even if the input were unbounded, the output of this specific system would remain bounded by $|V_{cc}|$).
Since every bounded input guarantees a bounded output, the stability criterion is met.
**Conclusion:** The system is **BIBO stable**.

Location pg 110-111 In pdf

Hi

### Q.2. (a) Briefly describe the following classifications of systems (i) a causal system, and (ii) a time invariant system.
### A system has the following input-output relation: $y(t) = x(t) - 0.5(t + 1)$
### Determine whether this system is time invariant and causal.

**Detailed Answer:**

**Brief Descriptions:**
**(i) A Causal System:** A system is defined as causal if its output at any specific time depends exclusively on the present and/or past values of the input signal. It does not depend on future values of the input. All physically realizable, real-time systems must be causal because a system cannot foresee the future.

**(ii) A Time-Invariant System:** A system is time-invariant if a time shift in the input signal results in an identical time shift in the output signal, without changing the shape or amplitude of the output. This means the system's characteristics and parameters are constant over time. If input $x(t)$ produces output $y(t)$, then input $x(t - t_0)$ must produce output $y(t - t_0)$ for any $t_0$.

**Analysis of the given system:** 
The input-output relation is $y(t) = x(t) - 0.5(t + 1)$.

**1. Is it Causal?**
Let's analyze what the output $y$ depends on at time $t$.
The term $x(t)$ means the output depends on the input at the *current* time $t$. 
The term $- 0.5(t + 1)$ is just a function of the independent time variable $t$ itself and does not involve the input signal $x$ at any time.
Because the output $y(t)$ only requires knowledge of the input at the present time $t$ (and no future times like $x(t+1)$), the system is **causal**.

**2. Is it Time-Invariant?**
We need to check if a delayed input produces a correspondingly delayed output.
Let an input $x_1(t)$ produce an output $y_1(t)$:
$y_1(t) = x_1(t) - 0.5(t + 1)$

Now, let's define a second input $x_2(t)$ which is a delayed version of $x_1(t)$ by $t_0$:
$x_2(t) = x_1(t - t_0)$
The output $y_2(t)$ due to this new input $x_2(t)$ is found by substituting $x_2(t)$ into the system equation:
$y_2(t) = x_2(t) - 0.5(t + 1)$
Substitute $x_2(t) = x_1(t - t_0)$:
$$y_2(t) = x_1(t - t_0) - 0.5(t + 1) = x_1(t - t_0) - 0.5t - 0.5$$

Next, we take the original output $y_1(t)$ and delay it by $t_0$:
$$y_1(t - t_0) = x_1(t - t_0) - 0.5((t - t_0) + 1)$$
$$y_1(t - t_0) = x_1(t - t_0) - 0.5t + 0.5t_0 - 0.5$$

Now we compare $y_2(t)$ and $y_1(t - t_0)$:
$x_1(t - t_0) - 0.5t - 0.5 \neq x_1(t - t_0) - 0.5t + 0.5t_0 - 0.5$
Since $y_2(t) \neq y_1(t - t_0)$ (the terms differ by $0.5t_0$), the system does not respond to a delayed input with an equally delayed output. Therefore, the system is **time-varying** (not time-invariant). The explicit presence of the independent variable '$t$' outside the function argument '$x()$' causes this behavior.

always mention ans related location pg no. In pdf , at the end of every soln 1.7-2 Time-Invariant and Time-Varying Systems, pg. 102 and 1.7-4 Causal and Noncausal Systems, pg. 104-105

***
### **System (b): $y(t) = \frac{d}{dt}x(t)$**

- **Intuition:** The system simply calculates the derivative (slope) of the input. If you shift the input signal in time, its slope profile remains exactly the same, it just occurs later.
    
- **Mathematical Proof:**
    
    1. **Delay the Output:** Let a standard input $x(t)$ produce the output $y(t) = \frac{d}{dt}x(t)$. Delaying this output function by an arbitrary time $T$ yields:
        
        $$y_1(t) = y(t-T) = \frac{d}{d(t-T)}x(t-T) = \frac{d}{dt}x(t-T)$$
        
    2. **Pass a Delayed Input:** Now, pass a delayed input $x_2(t) = x(t-T)$ into the system. The system differentiates whatever input it receives:
        
        $$y_2(t) = \frac{d}{dt}x_2(t) = \frac{d}{dt}x(t-T)$$
        

Comparing the two results, $y_1(t) = y_2(t)$. Because the delayed output is identical to the system's response to a delayed input, the system strictly commutes with time-shifting and is **Time-Invariant**.

### **System Equation** $$y(t) = (\sin t)x(t-2)$$

#### **Proof via Time-Shifting**

1. **Delayed Output, $y(t-T)$:**
    
    Shift the entire original equation by $T$ seconds (replace all $t$ with $t-T$):
    
    $$y_1(t) = \sin(t-T)x(t-T-2)$$
    
2. **Response to Delayed Input, $x(t-T)$:**
    
    Pass a delayed input $x_2(t) = x(t-T)$ into the system. The system shifts the input argument by $2$ and multiplies it by the current time parameter $\sin t$:
    
    $$y_2(t) = (\sin t)x_2(t-2) = (\sin t)x(t-T-2)$$
    
3. **Compare:**
    
    $$y_1(t) \neq y_2(t) \implies \sin(t-T)x(t-T-2) \neq (\sin t)x(t-T-2)$$
    

#### **Conclusion**

Because the delayed output does not equal the response to a delayed input, the system parameters depend on absolute time $t$. Therefore, it is a **time-varying-parameter system**.

### **(a) $y(t - 1) = 2x(t - 1)$**

- **Conclusion:** **Memoryless**
    
- **Reason:** The output at time $t-1$ depends strictly on the strength of the input at that identical time $t-1$. Because it does not look backward or forward to other time instances, it requires no memory.
    

### **(b) $y(t) = \frac{d}{dt}x(t)$**

- **Conclusion:** **Dynamic (With Memory)**
    
- **Reason:** Calculating a derivative or slope requires evaluating a change across multiple points over time. This is proven by the limit definition of a derivative:
    
    $$y(t) = \lim_{T \to 0} \frac{x(t) - x(t-T)}{T}$$
    
    Because the output at time $t$ relies on an infinitesimally past value $x(t-T)$, the system possesses memory.
    

### **(c) $y(t) = (t - 1)x(t)$**

- **Conclusion:** **Memoryless**
    
- **Reason:** The output at time $t$ is simply the present input $x(t)$ multiplied by a time-varying coefficient $(t-1)$. Since the output at any instant relies purely on the input value at that same exact instant, the system is memoryless.
### Analysis of $y(t) = x(-t)$ causal or non

To test for causality, we can plug in specific values for time $t$ (both positive and negative) to see what inputs the system requires.

- **For $t = -2$ (a past time):**
    
    $$y(-2) = x(-(-2)) = x(2)$$
    
    The output at time $t = -2$ requires the input at a future time $t = 2$.
    
- **For $t = 2$ (a future time):**
    
    $$y(2) = x(-2)$$
    
    The output at time $t = 2$ requires the input at a past time $t = -2$.
    

#### Conclusion

Because the output depends on future values of the input for any $t < 0$, the system is **non-causal** (specifically, it is an anti-causal system for $t < 0$).

**Answer:** **Non-causal**

### 1. Proof of Noncausality   :   A system is causal if the output $y(t)$ depends only on inputs $x(\tau)$ for $\tau \le t$. Given: $$y(t) = \int_{t-5}^{t+5} x(\tau) d\tau$$

The upper limit of integration is $\tau = t+5$. Because $t+5 > t$, the system depends on future inputs, making it **noncausal**.

#### 2. Proof of Realizability with a 5-Second Delay

Let the delayed output be $y_d(t) = y(t-5)$. Substitute $t-5$ into the system equation:

$$y_d(t) = \int_{(t-5)-5}^{(t-5)+5} x(\tau) d\tau$$

$$y_d(t) = \int_{t-10}^{t} x(\tau) d\tau$$

The upper limit of integration is now $\tau = t$. Because the system only requires past and present inputs ($\tau \le t$), it is **causal** and physically realizable.

### (a) $y(t) = x(-t)$  **Status:** **Invertible**
    
- **Proof:** Substitute $-t$ into the system equation to find the inverse operation:
    
    $$y(-t) = x(-(-t)) = x(t)$$
    
- **Conclusion:** The input can be uniquely recovered using the inverse system $x(t) = y(-t)$.
    

### (b) $y(t) = tx(t)$  **Status:** **Not Invertible**
    
- **Proof:** Attempting to isolate the input yields:
    
    $$x(t) = \frac{1}{t}y(t)$$
    
- **Conclusion:** At $t = 0$, the equation becomes $y(0) = 0 \cdot x(0) = 0$. Because division by zero is undefined, the value of $x(0)$ is permanently lost and cannot be recovered.
    

### (c) $y(t) = \frac{d}{dt}x(t)$  **Status:** **Not Invertible**
    
- **Proof:** Consider two distinct inputs that differ only by a constant (DC component):
    
    $$x_1(t) = 1 \implies y_1(t) = \frac{d}{dt}(1) = 0$$
    
    $$x_2(t) = 2 \implies y_2(t) = \frac{d}{dt}(2) = 0$$
    
- **Conclusion:** Since distinct inputs ($x_1(t) \neq x_2(t)$) map to the exact same output ($y_1(t) = y_2(t) = 0$), the unique original input cannot be recovered.

### Worked Examples BIBO 

- **Example 1:** $y(t) = t \cdot x(t)$
    
    - _Input:_ $x(t) = u(t)$ (bounded)
        
    - _Output:_ $y(t) = t \cdot u(t)$ (ramp function)
        
    - _Analysis:_ As $t \to \infty$, the output $y(t) \to \infty$.
        
    - _Result:_ ❌ **Unstable**
        
- **Example 2:** $y(t) = x(t) + 2$
    
    - _Input:_ $x(t) = 4$ (bounded)
        
    - _Output:_ $y(t) = 6$
        
    - _Analysis:_ The output remains finite for all time.
        
    - _Result:_ ✅ **Stable**
        
**Example 3:** $y(t) = \sin(t) \cdot x(t)$

- _Input:_ Let $x(t)$ be any bounded input such that $\vert{}x(t)\vert{} \le M < \infty$.
    
- _Output:_ $y(t) = \sin(t) \cdot x(t)$
    
- _Analysis:_ Take the absolute value of both sides:
    
    $$\vert{}y(t)\vert{} = \vert{}\sin(t) \cdot x(t)\vert{} = \vert{}\sin(t)\vert{} \cdot \vert{}x(t)\vert{}$$
    
    Since $\vert{}\sin(t)\vert{} \le 1$ for all time, we can write:
    
    $$\vert{}y(t)\vert{} \le 1 \cdot M \to \vert{}y(t)\vert{} \le M$$
    
    Because $M$ is finite, the output is guaranteed to remain finite.
    
- _Result:_ ✅ **Stable**

 (a) $y(t) = x^2(t)$

- **Status:** **BIBO-Stable**
    
- **Proof:** Assume a bounded input such that $\vert{}x(t)\vert{} \le M_x < \infty$ for all $t$. Taking the absolute value of the output:
    
    $$\vert{}y(t)\vert{} = \vert{}x^2(t)\vert{} = \vert{}x(t)\vert{}^2 \le M_x^2$$
    
- **Conclusion:** Since $M_x^2 < \infty$, a bounded input always guarantees a bounded output.
### (c) $y(t) = \frac{d}{dt}x(t)$ **Status:** **BIBO-Unstable**
    
- **Proof:** Test the system using the bounded input $x(t) = u(t)$ (unit step function). The derivative of a unit step function yields an impulse function:
    
    $$y(t) = \frac{d}{dt}u(t) = \delta(t)$$
    
- **Conclusion:** At $t = 0$, the amplitude of the impulse function $\delta(t)$ is infinite ($\vert{}y(0)\vert{} = \infty$), so the system is unstable.

---

### 2. Pg 22, CT-1 Q2: A time limited rectangular pulse (left) is applied to a system produces an output as shown in the following figure (right). Express y(t) in terms of x(t). Also provide a mathematical justification whether the system is (i) Linear (ii) Time invariant and (iii) Causal. ![[Pasted image 20260712005359.png]]

**Figure Description:** 
*   **Input $x(t)$:** A standard rectangular pulse of amplitude $1$ spanning from $t=0$ to $t=1$. Mathematically: $x(t) = u(t) - u(t-1)$.
*   **Output $y(t)$:** A right-angled triangular pulse that starts at $t=0$, rises linearly to an amplitude of $1$ at $t=1$, and immediately drops to $0$. Mathematically: $y(t) = t$ for $0 \le t \le 1$, and $0$ otherwise.

**Solution:**

**Expressing $y(t)$ in terms of $x(t)$:**
Notice that the output $y(t)$ is identical to the input $x(t)$ multiplied by the time variable $t$. 
*   For $0 \le t \le 1$: $x(t) = 1$, and $t \cdot x(t) = t \cdot 1 = t$, which matches $y(t)$.
*   For everywhere else: $x(t) = 0$, and $t \cdot x(t) = 0$, which matches $y(t)$.
Therefore, the system operation is described by the equation: **$y(t) = t \cdot x(t)$**

**Mathematical Justifications:**

**(i) Linear:**
A system is linear if it satisfies the superposition principle (additivity and homogeneity).
Let $x_1(t) \rightarrow y_1(t) = t \cdot x_1(t)$
Let $x_2(t) \rightarrow y_2(t) = t \cdot x_2(t)$
Apply a combined weighted input: $x_3(t) = a x_1(t) + b x_2(t)$.
The system response will be:
$y_3(t) = t \cdot x_3(t) = t \cdot [a x_1(t) + b x_2(t)]$
$y_3(t) = a [t \cdot x_1(t)] + b [t \cdot x_2(t)]$
$y_3(t) = a y_1(t) + b y_2(t)$
Since the response to a linear combination of inputs equals the linear combination of their individual responses, the system is **Linear**.

**(ii) Time-invariant:**
A system is time-invariant if a time delay in the input causes an identical time delay in the output.
1.  Find response to delayed input $x(t - t_0)$: 
    $y_{delayed\_input}(t) = \mathcal{T}\{x(t - t_0)\} = t \cdot x(t - t_0)$
2.  Delay the original output by $t_0$: 
    $y(t - t_0) = (t - t_0) \cdot x(t - t_0)$
Comparing the two results:
$t \cdot x(t - t_0) \neq (t - t_0) \cdot x(t - t_0)$
Since the outputs are not equal, the system is **Time-Variant (Not Time-Invariant)**.

**(iii) Causal:**
A system is causal if the output at any time $t$ depends only on the present and/or past values of the input, not on future values.
For the system $y(t) = t \cdot x(t)$, the output $y$ at a specific time $t$ requires only the value of the input $x$ at that exact same time $t$. It does not require $x(t+\tau)$ where $\tau > 0$.
Therefore, the system is **Causal**.

*Reference: Lathi Chapter 1 / Class Notes Pg 24-29 (Classification of Systems).*

---

### **6. Pg 28, CT-1 Q1: Consider a discrete-time system...**
**System Equation:** $y[n] = \frac{1}{3} (x[n] + x[n-1] + x[n-2])$

**Solution:**

*   **(i) Memoryless:** A system is memoryless if its output at any given time $n$ depends *only* on the input at that exact same time $n$. Here, $y[n]$ requires $x[n-1]$ and $x[n-2]$, which are past values. 
    **Conclusion: Not Memoryless (It is a dynamic system with memory).**
*   **(ii) Causal:** A system is causal if its output depends only on present and past inputs, but not on future inputs (like $x[n+1]$). The equation utilizes $x[n]$ (present), $x[n-1]$ (past), and $x[n-2]$ (past). No future values are used.
    **Conclusion: Causal.**
*   **(iii) Linear:** A system is linear if it obeys superposition.
    Let input $x_1[n]$ produce $y_1[n] = \frac{1}{3} (x_1[n] + x_1[n-1] + x_1[n-2])$
    Let input $x_2[n]$ produce $y_2[n] = \frac{1}{3} (x_2[n] + x_2[n-1] + x_2[n-2])$
    Apply a combined input $x_3[n] = a x_1[n] + b x_2[n]$:
    $y_3[n] = \frac{1}{3} (x_3[n] + x_3[n-1] + x_3[n-2])$
    $y_3[n] = \frac{1}{3} ( (a x_1[n] + b x_2[n]) + (a x_1[n-1] + b x_2[n-1]) + (a x_1[n-2] + b x_2[n-2]) )$
    $y_3[n] = a [\frac{1}{3}(x_1[n] + x_1[n-1] + x_1[n-2])] + b [\frac{1}{3}(x_2[n] + x_2[n-1] + x_2[n-2])]$
    $y_3[n] = a y_1[n] + b y_2[n]$
    **Conclusion: Linear.**
*   **(iv) Time-invariant:** A system is time-invariant if a delay in the input causes an identical delay in the output.
    Response to a delayed input $x[n-k]$ is $y_d[n] = \frac{1}{3} (x[n-k] + x[n-k-1] + x[n-k-2])$.
    Delaying the original output $y[n]$ by $k$ yields $y[n-k] = \frac{1}{3} (x[n-k] + x[n-1-k] + x[n-2-k])$.
    Since $y_d[n] = y[n-k]$, the system's behavior does not shift over time.
    **Conclusion: Time-invariant.**
*   **(v) Stable:** A system is BIBO (Bounded-Input Bounded-Output) stable if every bounded input produces a bounded output.
    Assume the input is bounded such that $|x[n]| \le M < \infty$ for all $n$.
    $|y[n]| = |\frac{1}{3} (x[n] + x[n-1] + x[n-2])| \le \frac{1}{3} (|x[n]| + |x[n-1]| + |x[n-2]|)$
    $|y[n]| \le \frac{1}{3} (M + M + M) = \frac{3M}{3} = M < \infty$.
    The output is also bounded.
    **Conclusion: Stable.**

---

### **13. Pg 33, CT-2 Q1: The input-output relationship of a system is shown in the following figure. Provide a mathematical justification whether the system is (i) Linear and (ii) Invertible. ![[Pasted image 20260712005701.png]]**

**Figure Description:** The figure displays an input-output characteristic curve for a system. The x-axis represents the input $x(t)$, and the y-axis represents the output $y(t)$.
*   For $x(t) \le 0$, the output is $y(t) = 0$.
*   For $0 < x(t) < 2$, the output rises linearly from $0$ to $2$. The slope is $\frac{2-0}{2-0} = 1$. Thus, $y(t) = x(t)$.
*   For $x(t) \ge 2$, the output is constant at $y(t) = 2$.
This describes a **saturation** or **limiter** system (specifically, a half-wave rectifier with saturation).

**Solution:**

**(i) Linearity Justification:**
A system is linear if it satisfies the principle of superposition (both additivity and homogeneity).
Let's check homogeneity (scaling): $T\{a \cdot x(t)\} = a \cdot T\{x(t)\}$ for any scalar $a$.
*   Let an input be $x_1(t) = 1$. According to the graph, the corresponding output is $y_1(t) = 1$.
*   Now, scale the input by a constant $a = 3$, so the new input is $x_2(t) = 3 \cdot x_1(t) = 3$.
*   According to the graph, if the input is $x_2(t) = 3$, the output is capped at $y_2(t) = 2$.
*   However, if the system were linear, the output should be $3 \cdot y_1(t) = 3 \cdot 1 = 3$.
Since $y_2(t) \neq 3 \cdot y_1(t)$ (i.e., $2 \neq 3$), homogeneity fails.
**Conclusion:** The system is **Non-linear**.

**(ii) Invertibility Justification:**
A system is invertible if distinct inputs lead to distinct outputs (a one-to-one mapping). If a system is invertible, observing the output uniquely determines what the input was.
*   Let's pick an output value, say $y(t) = 2$.
*   Looking at the graph, if the output is $2$, what was the input? The input could have been $x(t) = 2$, or $x(t) = 3$, or $x(t) = 100$. Any input $x(t) \ge 2$ maps to the identical output $y(t) = 2$.
*   Similarly, for an output $y(t) = 0$, the input could be any $x(t) \le 0$.
Because multiple different inputs can produce the exact same output, the mapping is many-to-one, not one-to-one. We cannot uniquely reverse the operation to find the original input from the output.
**Conclusion:** The system is **Non-invertible**.

*Reference: Lathi Chapter 1 / Class Notes Pg 29-30 (System Classification).*

---

### **14. Pg 34, CT-2 Q1: The input-output relationship of two systems are shown the following figure. Provide a mathematical justification whether the system shown in figure (i) linear, and (ii) invertible. For both systems the slope is unity. ![[Pasted image 20260712005710.png]]**

**Figure Description:** 
Two input-output characteristic graphs are shown. Both have $x(t)$ on the horizontal axis and $y(t)$ on the vertical axis.
*   **System (i):** A straight line that does not pass through the origin. It crosses the y-axis at $y=4$ and has a slope of unity ($1$).
    Equation: **$y(t) = x(t) + 4$**
*   **System (ii):** A straight line that passes exactly through the origin $(0,0)$ and has a slope of unity ($1$).
    Equation: **$y(t) = x(t)$** (This is an identity system).

**Solution for System (i): $y(t) = x(t) + 4$**

**(i) Linearity Justification:**
We test for additivity.
*   Let input $x_1(t)$ produce output $y_1(t) = x_1(t) + 4$.
*   Let input $x_2(t)$ produce output $y_2(t) = x_2(t) + 4$.
*   Now apply an input that is the sum: $x_3(t) = x_1(t) + x_2(t)$.
*   The actual system response to this combined input is:
    $y_3(t) = x_3(t) + 4 = [x_1(t) + x_2(t)] + 4$
*   However, if the system were linear, the response should be the sum of individual responses:
    $y_{linear\_sum}(t) = y_1(t) + y_2(t) = (x_1(t) + 4) + (x_2(t) + 4) = x_1(t) + x_2(t) + 8$
Comparing the two: $[x_1(t) + x_2(t)] + 4 \neq x_1(t) + x_2(t) + 8$.
Since superposition fails, the system is **Non-linear**. 
*(A key rule of thumb: An input-output plot must be a straight line passing through the origin to be linear).*

**(ii) Invertibility Justification:**
We check if there is a unique one-to-one mapping between $x(t)$ and $y(t)$.
*   The equation is $y(t) = x(t) + 4$.
*   For any given output value $y(t)$, we can uniquely determine the input by rearranging the equation: $x(t) = y(t) - 4$.
*   Because every unique input maps to a unique output, and vice-versa, the mapping is strictly one-to-one.
**Conclusion:** The system is **Invertible**.

*(Note: The prompt specifically asks about figure (i), but for completeness, System (ii) where $y(t)=x(t)$ is both linear (passes through origin) and invertible (one-to-one).*

*Reference: Lathi Chapter 1 / Class Notes Pg 29-30 (System Classification).*

---

### **17. Pg 39, CT-1 Q1: Consider a discrete-time system...**
**System Equation:** $y[n] = \frac{1}{3} (x[n+1] + x[n] + x[n-1])$
*(Note: This is a slightly different moving-average system compared to question 6, as it includes a future term $x[n+1]$.)*

**Solution:**

*   **(i) Memoryless:** A system is memoryless if the output at index $n$ depends *only* on the input at the exact same index $n$. Here, calculating $y[n]$ requires $x[n+1]$ (future) and $x[n-1]$ (past). Since it relies on values other than the present input $x[n]$, it requires memory to store or anticipate those values.
    **Conclusion: Not Memoryless (It is a dynamic system).**

*   **(ii) Causal:** A system is causal if its output at any time depends only on present and/or past inputs, never on future inputs. In this equation, to compute $y[n]$ at the current time $n$, we need the value of $x[n+1]$. For example, to find $y[0]$, we must know $x[1]$, which has not happened yet in real time. Because it relies on a future input, the system is non-causal.
    **Conclusion: Non-causal.**

*   **(iii) Linear:** A system is linear if it obeys the principle of superposition (additivity and homogeneity).
    Let input $x_1[n]$ produce $y_1[n] = \frac{1}{3} (x_1[n+1] + x_1[n] + x_1[n-1])$
    Let input $x_2[n]$ produce $y_2[n] = \frac{1}{3} (x_2[n+1] + x_2[n] + x_2[n-1])$
    Apply a combined, weighted input: $x_3[n] = a \cdot x_1[n] + b \cdot x_2[n]$.
    The system's response to this combined input is:
    $y_3[n] = \frac{1}{3} (x_3[n+1] + x_3[n] + x_3[n-1])$
    Substitute the definition of $x_3$:
    $y_3[n] = \frac{1}{3} \big( (a \cdot x_1[n+1] + b \cdot x_2[n+1]) + (a \cdot x_1[n] + b \cdot x_2[n]) + (a \cdot x_1[n-1] + b \cdot x_2[n-1]) \big)$
    Group terms associated with '$a$' and '$b$':
    $y_3[n] = a \left[ \frac{1}{3} (x_1[n+1] + x_1[n] + x_1[n-1]) \right] + b \left[ \frac{1}{3} (x_2[n+1] + x_2[n] + x_2[n-1]) \right]$
    $y_3[n] = a \cdot y_1[n] + b \cdot y_2[n]$
    Because the response to a linear combination of inputs is the linear combination of the individual responses, the system satisfies superposition.
    **Conclusion: Linear.**

*   **(iv) Time-invariant:** A system is time-invariant if a delay in the input signal causes an identical delay in the output signal, without changing the shape of the output.
    Let's apply a delayed input signal $x_d[n] = x[n-k]$. The response to this delayed input is:
    $y_d[n] = \frac{1}{3} (x_d[n+1] + x_d[n] + x_d[n-1]) = \frac{1}{3} (x[(n+1)-k] + x[n-k] + x[(n-1)-k])$
    $y_d[n] = \frac{1}{3} (x[n-k+1] + x[n-k] + x[n-k-1])$
    Now, let's delay the original output signal $y[n]$ by $k$:
    $y[n-k] = \frac{1}{3} (x[(n-k)+1] + x[n-k] + x[(n-k)-1])$
    $y[n-k] = \frac{1}{3} (x[n-k+1] + x[n-k] + x[n-k-1])$
    Comparing the two expressions, $y_d[n] = y[n-k]$. The system's behavior does not depend on the specific time it is operated.
    **Conclusion: Time-invariant.**

*   **(v) Stable:** A system is Bounded-Input Bounded-Output (BIBO) stable if every bounded input sequence produces a bounded output sequence.
    Assume the input $x[n]$ is bounded, meaning there exists a finite positive number $M_x$ such that $|x[n]| \le M_x < \infty$ for all $n$.
    We must show the output $y[n]$ is also bounded by some finite number $M_y$.
    $|y[n]| = \left| \frac{1}{3} (x[n+1] + x[n] + x[n-1]) \right|$
    Using the triangle inequality ($|A+B| \le |A| + |B|$):
    $|y[n]| \le \frac{1}{3} (|x[n+1]| + |x[n]| + |x[n-1]|)$
    Since each individual input sample is bounded by $M_x$:
    $|y[n]| \le \frac{1}{3} (M_x + M_x + M_x) = \frac{1}{3} (3M_x) = M_x$
    Therefore, $|y[n]| \le M_x < \infty$. The output is bounded.
    **Conclusion: Stable.**

*Reference: Class Notes Pg 24-31 (Classification of Systems).*

---

### **21. Pg 41, CT-01 Q2: Determine whether the following systems are (i) Time-variant and (iii) Causal.**

**Solution:**

**(a) $y_1(t) = t \cdot x(t+1)$**

*   **(i) Time-Variant/Invariant Check:**
    A system is time-invariant if a delay in the input $x(t) \to x(t-t_0)$ causes an identical shift in the output $y(t) \to y(t-t_0)$.
    1.  Find the response to a delayed input $x_d(t) = x(t-t_0)$:
        $y_{delayed\_input}(t) = t \cdot x_d(t+1) = t \cdot x((t+1) - t_0) = \mathbf{t \cdot x(t - t_0 + 1)}$
    2.  Find the delayed version of the original output:
        $y_1(t-t_0) = (t-t_0) \cdot x((t-t_0) + 1) = \mathbf{(t - t_0) \cdot x(t - t_0 + 1)}$
    Comparing the two results: $t \cdot x(t - t_0 + 1) \neq (t - t_0) \cdot x(t - t_0 + 1)$.
    **Conclusion: The system is Time-Variant.**

*   **(iii) Causal/Non-Causal Check:**
    A system is causal if the output at present time $t$ depends *only* on present and past inputs (values of $\tau \le t$).
    Let's test an arbitrary time, say $t = 1$:
    $y_1(1) = 1 \cdot x(1+1) = x(2)$
    To determine the output at $t=1$, the system requires the input value at $t=2$, which lies in the future.
    **Conclusion: The system is Non-Causal.**

**(b) $y_2(t) = x(1-t)$**

*   **(i) Time-Variant/Invariant Check:**
    1.  Find the response to a delayed input $x_d(t) = x(t-t_0)$:
        $y_{delayed\_input}(t) = x_d(1-t) = \mathbf{x((1-t) - t_0) = x(1 - t - t_0)}$
    2.  Find the delayed version of the original output:
        $y_2(t-t_0) = \mathbf{x(1 - (t-t_0)) = x(1 - t + t_0)}$
    Comparing the two results: $x(1 - t - t_0) \neq x(1 - t + t_0)$.
    **Conclusion: The system is Time-Variant.**

*   **(iii) Causal/Non-Causal Check:**
    Let's test an arbitrary negative time, say $t = -2$:
    $y_2(-2) = x(1 - (-2)) = x(3)$
    To determine the output at $t=-2$, the system requires the input value at $t=3$, which is in the future relative to $t=-2$.
    **Conclusion: The system is Non-Causal.**

---

### **24. Pg 44, CT-01 Q2: The input and output relationship of a system is shown.** ![[Pasted image 20260712010339.png]]

**Figure Analysis:**
*   **Input $x(t)$:** A standard rectangular pulse from $t=0$ to $t=1$ with amplitude $1$. Mathematically: $x(t) = 1$ for $0 \le t \le 1$.
*   **Output $y(t)$:** A line starting at $(0,1)$ and dropping linearly to $(1,0)$. The slope is $m = \frac{0-1}{1-0} = -1$. The y-intercept is $1$. Equation for this segment: $y(t) = -t + 1$.

**Expressing $y(t)$ in terms of $x(t)$:**
Observe the relationship between $x(t)$ and $y(t)$ in the active region $[0, 1]$:
$x(t) = 1$
$y(t) = -t + 1 = (1-t) \cdot 1 = (1-t) \cdot x(t)$
Outside this region, $x(t) = 0$ and $y(t) = 0$, so $(1-t) \cdot 0 = 0$, which holds true.
**Equation:** $\mathbf{y(t) = (1 - t) x(t)}$

**Mathematical Justifications:**

**(i) Linear:**
Test for the superposition principle.
Let $x_1(t) \to y_1(t) = (1-t)x_1(t)$
Let $x_2(t) \to y_2(t) = (1-t)x_2(t)$
Apply a linear combination input: $x_3(t) = ax_1(t) + bx_2(t)$.
The system output is:
$y_3(t) = (1-t)x_3(t) = (1-t)[ax_1(t) + bx_2(t)]$
$y_3(t) = a(1-t)x_1(t) + b(1-t)x_2(t)$
$y_3(t) = a y_1(t) + b y_2(t)$
Because the response to a linear combination of inputs is the exact linear combination of their individual responses, the system satisfies superposition.
**Conclusion: The system is Linear.**

**(ii) Time-Variant:**
Test if a time shift in input causes an identical shift in output.
1.  Apply a delayed input $x_d(t) = x(t-t_0)$. The response is:
    $y_{delayed\_input}(t) = (1-t)x_d(t) = \mathbf{(1-t)x(t-t_0)}$
2.  Delay the original output by $t_0$:
    $y(t-t_0) = (1-(t-t_0))x(t-t_0) = \mathbf{(1-t+t_0)x(t-t_0)}$
Comparing the two: $(1-t)x(t-t_0) \neq (1-t+t_0)x(t-t_0)$. The system scales the input by a time-dependent factor $(1-t)$, making its behavior change depending on *when* the signal arrives.
**Conclusion: The system is Time-Variant.**

**(iii) Causal:**
A system is causal if the current output $y(t)$ depends only on current or past values of $x(t)$.
Looking at the equation $y(t) = (1-t)x(t)$:
To evaluate $y$ at any specific instant $t_1$ (e.g., $t=0.5$), we compute $y(0.5) = (0.5)x(0.5)$. The output relies strictly on the input $x$ at that exact same instant $t_1$. It does not look ahead to $x(t_1 + \tau)$.
**Conclusion: The system is Causal.**

# 2. Energy and Power Signals

### Q.1 (b) Provide a mathematical justification whether the following signals are energy or power signal or neither. (i) $e^{kt} u(-t)$, $k>0$ (ii) $u(t+2) - u(t-2)$. Also compute the energy and power of them.

**Solution:**

To classify a signal, we calculate its total energy $E$ and average power $P$.
*   If $0 < E < \infty$, it is an **energy signal** (and $P = 0$).
*   If $0 < P < \infty$, it is a **power signal** (and $E = \infty$).

**(i) $x_1(t) = e^{kt} u(-t)$ for $k>0$**
The function $u(-t)$ is $1$ for $t < 0$ and $0$ for $t > 0$. Thus, the signal only exists for negative time.

*   **Energy ($E$):**
    $$E = \int_{-\infty}^{\infty} |x_1(t)|^2 dt = \int_{-\infty}^{0} (e^{kt})^2 dt = \int_{-\infty}^{0} e^{2kt} dt$$
    $$E = \left[ \frac{e^{2kt}}{2k} \right]_{-\infty}^{0} = \frac{1}{2k} (e^0 - e^{-\infty})$$
    Since $k > 0$, as $t \rightarrow -\infty$, $e^{2kt} \rightarrow 0$.
    $$E = \frac{1}{2k} (1 - 0) = \frac{1}{2k}$$
    Because $k > 0$, the energy is a finite positive value.

*   **Power ($P$):**
    For any finite energy signal, the average power over infinite time is zero.
    $$P = \lim_{T \rightarrow \infty} \frac{1}{2T} \int_{-T}^{T} |x_1(t)|^2 dt = \lim_{T \rightarrow \infty} \frac{E}{2T} = \lim_{T \rightarrow \infty} \frac{1/2k}{2T} = 0$$

*   **Conclusion:** Because the signal has finite energy ($E = \frac{1}{2k}$) and zero power, it is an **Energy Signal**.

**(ii) $x_2(t) = u(t+2) - u(t-2)$**
This signal represents a rectangular pulse with an amplitude of 1 that turns on at $t = -2$ and turns off at $t = 2$.
$x_2(t) = 1$ for $-2 < t < 2$, and $0$ elsewhere.

*   **Energy ($E$):**
    $$E = \int_{-\infty}^{\infty} |x_2(t)|^2 dt = \int_{-2}^{2} (1)^2 dt = [t]_{-2}^{2} = 2 - (-2) = 4$$
    The energy is a finite positive value.

*   **Power ($P$):**
    Similar to the previous case, since the total energy is finite, the average power evaluated over an infinite interval is zero.
    $$P = \lim_{T \rightarrow \infty} \frac{E}{2T} = \lim_{T \rightarrow \infty} \frac{4}{2T} = 0$$

*   **Conclusion:** Because the signal has finite energy ($E = 4$) and zero power, it is an **Energy Signal**.

Location pg 66 In pdf

***

### Q.1 (a) Define energy signal and power signal. Determine whether the following signals are energy signals, power signals or neither. (i) $x_1(t) = e^{-at} u(t)$ (ii) $x_2(t) = A\cos(\omega t+\theta)$ (iii) $x_3(t) = t u(t)$

**Solution:**

**Definitions:**
A signal's size can be measured by its energy or its power over time.
1.  **Energy Signal:** A signal $x(t)$ is an energy signal if its total energy $E$ is finite and non-zero ($0 < E < \infty$). The energy is defined as the area under the squared magnitude of the signal:
    $$E = \int_{-\infty}^{\infty} |x(t)|^2 dt$$
    For an energy signal, the average power over infinite time is exactly zero ($P = 0$).
2.  **Power Signal:** A signal $x(t)$ is a power signal if its average power $P$ is finite and non-zero ($0 < P < \infty$). The average power is defined as the time average of the energy over an infinite interval:
    $$P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt$$
    For a power signal, the total energy is infinite ($E = \infty$).
    A signal cannot be both an energy and a power signal. Some signals may be neither.

**Determining Signal Types:**

**(i) $x_1(t) = e^{-at} u(t)$**
Assuming $a > 0$ (a standard assumption for a decaying exponential in physical systems), let's calculate its energy:
$$E = \int_{-\infty}^{\infty} |e^{-at} u(t)|^2 dt = \int_{0}^{\infty} e^{-2at} dt = \left[ \frac{e^{-2at}}{-2a} \right]_{0}^{\infty}$$
$$E = 0 - \left( \frac{1}{-2a} \right) = \frac{1}{2a}$$
Since $a > 0$, the energy $E$ is finite. Because it has finite energy, its average power over infinite time will be $P = \lim_{T \to \infty} \frac{E}{2T} = 0$.
**Conclusion:** $x_1(t)$ is an **energy signal** (assuming $a>0$).

**(ii) $x_2(t) = A\cos(\omega t+\theta)$**
This is a periodic sinusoidal signal. Periodic signals that do not decay to zero have infinite energy, so we check for power. Since it is periodic, we can calculate power by averaging over one period $T_0 = \frac{2\pi}{\omega}$:
$$P = \frac{1}{T_0} \int_{0}^{T_0} |A\cos(\omega t+\theta)|^2 dt = \frac{A^2}{T_0} \int_{0}^{T_0} \cos^2(\omega t+\theta) dt$$
Using the identity $\cos^2(x) = \frac{1 + \cos(2x)}{2}$:
$$P = \frac{A^2}{T_0} \int_{0}^{T_0} \left[ \frac{1}{2} + \frac{1}{2}\cos(2\omega t + 2\theta) \right] dt = \frac{A^2}{T_0} \left[ \frac{t}{2} + \frac{\sin(2\omega t + 2\theta)}{4\omega} \right]_{0}^{T_0}$$
The sine term evaluates to zero over a full period.
$$P = \frac{A^2}{T_0} \left( \frac{T_0}{2} \right) = \frac{A^2}{2}$$
The average power is finite ($A^2/2$) and non-zero, while its total energy integrated over all time is infinite.
**Conclusion:** $x_2(t)$ is a **power signal**.

**(iii) $x_3(t) = t u(t)$**
This is a causal ramp signal. As $t \to \infty$, the amplitude of the signal goes to infinity.
Let's check energy:
$$E = \int_{-\infty}^{\infty} |t u(t)|^2 dt = \int_{0}^{\infty} t^2 dt = \left[ \frac{t^3}{3} \right]_{0}^{\infty} \to \infty$$
Let's check power:
$$P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |t u(t)|^2 dt = \lim_{T \to \infty} \frac{1}{2T} \int_{0}^{T} t^2 dt = \lim_{T \to \infty} \frac{1}{2T} \left[ \frac{T^3}{3} \right] = \lim_{T \to \infty} \frac{T^2}{6} \to \infty$$
Since both energy and power are infinite, it falls into neither category.
**Conclusion:** $x_3(t)$ is **neither an energy signal nor a power signal**.

Location pg 65-66 In pdf

### **Question Statement**For a complex exponential signal of the form $x(t) = D e^{j\omega_0 t}$ (where $D$ is a complex constant), compute the average power $P_x$ and find its root-mean-square (rms) value.

 **Mathematical Steps**

#### **Step 1: Set up the power equation**

The average power $P_x$ for a continuous-time signal is defined as:

$$P_x = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} \vert{}x(t)\vert{}^2 \, dt$$

Substituting the given signal $x(t) = D e^{j\omega_0 t}$ into the equation yields:

$$P_x = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} \vert{}D e^{j\omega_0 t}\vert{}^2 \, dt$$

#### **Step 2: Simplify the magnitude squared term**

Using the algebraic property that the magnitude of a product is the product of the individual magnitudes ($\vert{}ab\vert{} = \vert{}a\vert{}\vert{}b\vert{}$):

$$\vert{}D e^{j\omega_0 t}\vert{}^2 = \vert{}D\vert{}^2 \cdot \vert{}e^{j\omega_0 t}\vert{}^2$$

We know from Euler's identity ($e^{j\theta} = \cos\theta + j\sin\theta$) that the magnitude squared of any complex exponential is always $1$:

$$\vert{}e^{j\omega_0 t}\vert{}^2 = \cos^2(\omega_0 t) + \sin^2(\omega_0 t) = 1$$

Substituting this back simplifies the integrand to a constant value:

$$\vert{}D e^{j\omega_0 t}\vert{}^2 = \vert{}D\vert{}^2 \cdot 1 = \vert{}D\vert{}^2$$

#### **Step 3: Evaluate the time integral**

Substitute the simplified constant $\vert{}D\vert{}^2$ back into the limit expression:

$$P_x = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} \vert{}D\vert{}^2 \, dt$$

Because $\vert{}D\vert{}^2$ does not depend on time $t$, factor it completely outside of the integral:

$$P_x = \lim_{T \to \infty} \frac{\vert{}D\vert{}^2}{T} \int_{-T/2}^{T/2} 1 \, dt$$

Integrating $1$ over the time interval from $-\frac{T}{2}$ to $\frac{T}{2}$ yields the total duration length, $T$:

$$P_x = \lim_{T \to \infty} \frac{\vert{}D\vert{}^2}{T} \cdot \Big[ t \Big]_{-T/2}^{T/2}$$

$$P_x = \lim_{T \to \infty} \frac{\vert{}D\vert{}^2}{T} \cdot \left( \frac{T}{2} - \left(-\frac{T}{2}\right) \right)$$

$$P_x = \lim_{T \to \infty} \frac{\vert{}D\vert{}^2}{T} \cdot T$$

#### **Step 4: Evaluate the limit to find $P_x$**

Cancel the variable $T$ from both the numerator and denominator:

$$P_x = \lim_{T \to \infty} \vert{}D\vert{}^2$$

$$\mathbf{P_x = \vert{}D\vert{}^2}$$

#### **Step 5: Calculate the root-mean-square (RMS) value**

The RMS value is defined as the positive square root of the average power:

$$x_{\text{rms}} = \sqrt{P_x}$$

$$x_{\text{rms}} = \sqrt{\vert{}D\vert{}^2}$$
$$\mathbf{x_{\text{rms}} = \vert{}D\vert{}}$$
------------------------------
### 2. Constant / DC Signal (M-09 & M-01)

* Signal: $x(t) = A$
* Type: Power Signal
* Energy Calculation:
* $$E = \int_{-\infty}^{\infty} \vert{}x(t)\vert{}^2 \, dt = \int_{-\infty}^{\infty} A^2 \, dt = \infty$$ 
* Power Calculation:
* Set up the limit:
   $$P = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} A^2 \, dt$$ 
   * Evaluate the integral:
   $$P = \lim_{T \to \infty} \frac{1}{T} \left[ A^2 \cdot T \right] = A^2$$ 
   * Conclusion: Since $E = \infty$ and $P = A^2$, it is a power signal..

---

### 1. Pg 22, CT-1 Q1: For the following signal, sketch (i) y1(t)=x(t+1) and (ii) y2(t)=x(t+1)r(t−1). Justify whether y2(t) is energy signal or power signal or neither? Also computer the energy and power of y2(t). ![[Pasted image 20260712005325.png]]

**Figure Description:** The figure shows a continuous-time signal $x(t)$ plotted against $t$. The signal is $0$ for $t < 0$, increases linearly from $0$ to $1$ between $t = 0$ and $t = 1$, remains constant at $1$ between $t = 1$ and $t = 3$, and drops abruptly to $0$ at $t = 3$. 
Mathematically, $x(t)$ can be defined as:
*   $x(t) = t$ for $0 \le t < 1$
*   $x(t) = 1$ for $1 \le t \le 3$
*   $x(t) = 0$ otherwise.

**Solution:**

**(i) Sketch $y_1(t) = x(t+1)$**
The operation $t \rightarrow t+1$ represents a time-shift. Specifically, it is a time advance by 1 unit, meaning the entire signal $x(t)$ is shifted to the left by 1 unit on the time axis.
*   The original ramp from $t=0$ to $t=1$ now occurs from $t=-1$ to $t=0$.
*   The original flat top from $t=1$ to $t=3$ now occurs from $t=0$ to $t=2$.
*   The signal drops to zero at $t=2$.
*(Sketch description: A signal starting at $(-1,0)$, rising linearly to $(0,1)$, staying flat at $y=1$ until $t=2$, and dropping to $0$).*

**(ii) Sketch $y_2(t) = x(t+1)r(t-1)$**
The function $r(t-1)$ is a delayed unit ramp function. 
*   $r(t-1) = t - 1$ for $t \ge 1$
*   $r(t-1) = 0$ for $t < 1$
To sketch $y_2(t)$, we multiply the shifted signal $y_1(t) = x(t+1)$ by $r(t-1)$.
*   For $t < 1$: $r(t-1) = 0$, so $y_2(t) = y_1(t) \cdot 0 = 0$.
*   For $1 \le t \le 2$: In this region, $y_1(t) = 1$ and $r(t-1) = t-1$. Therefore, $y_2(t) = 1 \cdot (t-1) = t-1$.
*   For $t > 2$: $y_1(t) = 0$, so $y_2(t) = 0 \cdot r(t-1) = 0$.
*(Sketch description: A triangular pulse that is $0$ everywhere except between $t=1$ and $t=2$. It starts at $(1,0)$ and rises linearly with a slope of 1 to reach the coordinate $(2,1)$, then drops immediately to zero).*

**(iii) Justification and Computation of Energy and Power of $y_2(t)$**
*   **Justification:** A signal is an energy signal if its total energy $E$ satisfies $0 < E < \infty$ and its average power $P = 0$. A signal is a power signal if its average power $P$ satisfies $0 < P < \infty$ and its total energy $E = \infty$. 
Since $y_2(t)$ is a time-limited signal (it only exists between $t=1$ and $t=2$) with a finite amplitude, its total area squared (energy) will be finite. Therefore, $y_2(t)$ is an **Energy Signal**.
*   **Computation of Energy ($E$):**
    $E = \int_{-\infty}^{\infty} |y_2(t)|^2 dt$
    $E = \int_{1}^{2} (t-1)^2 dt$
    Let $u = t-1 \implies du = dt$. When $t=1, u=0$; when $t=2, u=1$.
    $E = \int_{0}^{1} u^2 du = \left[ \frac{u^3}{3} \right]_{0}^{1} = \frac{1}{3} - 0 = \mathbf{\frac{1}{3} \text{ Joules}}$
*   **Computation of Power ($P$):**
    $P = \lim_{T \to \infty} \frac{1}{T} \int_{-T/2}^{T/2} |y_2(t)|^2 dt$
    Since the integral yields a finite value ($1/3$), dividing a finite number by infinity yields zero.
    $P = \lim_{T \to \infty} \frac{1/3}{T} = \mathbf{0 \text{ Watts}}$

*Reference: Lathi Chapter 1 / Class Notes Pg 5-6 (Energy & Power signal), Pg 12-13 (Signal Operations).*

---

### **7. Pg 28, CT-1 Q2: Draw the following signal and comment whether...**

**Solution:**

**(i) $x_1(t) = e^{-at}u(-t)$ where $a$ is real.**
*   **Sketch:** The function $u(-t)$ is a time-reversed unit step, meaning the signal exists only for $t \le 0$ (left-sided). 
    *   If $a > 0$: As $t$ approaches $-\infty$, the term $-at$ becomes positive infinity, making $e^{-at} \to \infty$. The signal starts at $1$ at $t=0$ and grows exponentially to infinity as you move left. 
    *   If $a < 0$: The signal decays to $0$ as $t \to -\infty$.
    *(Standard academic convention usually assumes $a > 0$ when testing unboundedness, but let's evaluate both for thoroughness).*
*   **Comment:**
    *   **Case $a > 0$:** The energy $E = \int_{-\infty}^{0} |e^{-at}|^2 dt = \int_{-\infty}^{0} e^{-2at} dt = \infty$. The power $P$ is also $\infty$. Therefore, it is **Neither an energy nor a power signal**.
    *   **Case $a < 0$ (let $a=-b$ where $b>0$):** $E = \int_{-\infty}^{0} e^{2bt} dt = \frac{1}{2b} [1 - 0] = \frac{1}{2b}$. Because energy is finite, it is an **Energy Signal**.

**(ii) $x_2(t) = t u(t)$.**
*   **Sketch:** This is the standard unit ramp function. The function is $0$ for $t < 0$, starts at $(0,0)$, and increases linearly with a slope of $1$ for $t \ge 0$.
*   **Comment:** Let's test for Energy ($E$) and Power ($P$):
    $E = \int_{0}^{\infty} t^2 dt = \left[ \frac{t^3}{3} \right]_0^\infty = \infty$ (Energy is infinite).
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{0}^{T} t^2 dt = \lim_{T \to \infty} \frac{1}{2T} \left[ \frac{T^3}{3} \right] = \lim_{T \to \infty} \frac{T^2}{6} = \infty$ (Power is infinite).
    Since both energy and power are infinite, it is **Neither an energy nor a power signal**.

---

### **9. Pg 31, CT-1 Q1: Determine the energy and power of the following signals:**

**General Definitions:**
*   **Energy ($E$):** $E = \int_{-\infty}^{\infty} |x(t)|^2 dt$
*   **Power ($P$):** $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt$
*   An *energy signal* has $0 < E < \infty$ and $P = 0$. A *power signal* has $0 < P < \infty$ and $E = \infty$.

**(i) $x(t) = ke^{\beta t}$, where $k>0$, $\beta<0$**
*   **Analysis:** This signal represents an exponential curve that decays as $t \to \infty$, but as $t \to -\infty$, $e^{\beta(-\infty)} = e^{\infty} \to \infty$. Since the signal grows to infinity on the left side of the time axis, its area squared (energy) will diverge to infinity.
*   **Energy:** $E = \int_{-\infty}^{\infty} (ke^{\beta t})^2 dt = k^2 \int_{-\infty}^{\infty} e^{2\beta t} dt = k^2 \left[ \frac{e^{2\beta t}}{2\beta} \right]_{-\infty}^{\infty}$.
    Because $\beta < 0$, $e^{2\beta(\infty)} = 0$, but $e^{2\beta(-\infty)} = \infty$.
    $E = k^2 (0 - \infty) = \mathbf{\infty}$.
*   **Power:** $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} k^2 e^{2\beta t} dt = \lim_{T \to \infty} \frac{k^2}{4\beta T} (e^{2\beta T} - e^{-2\beta T})$.
    As $T \to \infty$, $e^{2\beta T} \to 0$ and $e^{-2\beta T} \to \infty$. Thus, $P = \mathbf{\infty}$.
*   **Conclusion:** It is **neither** an energy nor a power signal.

**(ii) $x(t) = ke^{\beta t}$, where $k>0$, $\beta=-2j$**
*   **Analysis:** $x(t) = ke^{-j2t}$. This is a complex exponential signal. The magnitude of a complex exponential $e^{j\theta}$ is always 1. So, $|x(t)| = |k| |e^{-j2t}| = k \cdot 1 = k$. This is a signal with a constant magnitude over all time.
*   **Energy:** $E = \int_{-\infty}^{\infty} |k|^2 dt = \int_{-\infty}^{\infty} k^2 dt = \mathbf{\infty}$.
*   **Power:** $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} k^2 dt = \lim_{T \to \infty} \frac{1}{2T} [k^2 t]_{-T}^{T} = \lim_{T \to \infty} \frac{1}{2T} (k^2(2T)) = \mathbf{k^2}$.
*   **Conclusion:** It is a **power signal** with $P = k^2$ Watts.

**(iii) $x(t) = \cos(10\pi t)u(-t)$**
*   **Analysis:** This is a cosine wave that exists only for $t \le 0$ (left-sided) because of the time-reversed unit step $u(-t)$.
*   **Energy:** $E = \int_{-\infty}^{0} \cos^2(10\pi t) dt = \int_{-\infty}^{0} \frac{1 + \cos(20\pi t)}{2} dt = \infty$ (because integrating the constant $1/2$ over an infinite interval yields infinity).
*   **Power:** $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{0} \cos^2(10\pi t) dt$
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{0} \frac{1 + \cos(20\pi t)}{2} dt$
    $P = \lim_{T \to \infty} \frac{1}{4T} \left[ t + \frac{\sin(20\pi t)}{20\pi} \right]_{-T}^{0}$
    $P = \lim_{T \to \infty} \frac{1}{4T} \left[ 0 - \left(-T + \frac{\sin(-20\pi T)}{20\pi}\right) \right] = \lim_{T \to \infty} \frac{T}{4T} = \mathbf{\frac{1}{4}}$.
*   **Conclusion:** It is a **power signal** with $P = 0.25$ Watts. *(Note: A full eternal cosine has power $1/2$. Since this exists for exactly half of eternity, its power is half of that, i.e., $1/4$).*

---

### **11. Pg 32, CT-1 Q1: Determine whether the following signals are energy signal, power signal or neither.**

**(i) $x(t) = e^{\sigma t}u(-t), \sigma > 0$**
*   This signal exists only for $t \le 0$. As $t$ goes to $-\infty$, the exponent $\sigma t$ goes to $-\infty$ (since $\sigma > 0$), making the signal decay to $0$. It is a bounded, time-limited-like decaying exponential.
*   **Energy:** $E = \int_{-\infty}^{0} |e^{\sigma t}|^2 dt = \int_{-\infty}^{0} e^{2\sigma t} dt = \left[ \frac{e^{2\sigma t}}{2\sigma} \right]_{-\infty}^{0} = \frac{1}{2\sigma} - 0 = \mathbf{\frac{1}{2\sigma} \text{ Joules}}$.
*   **Power:** Since energy is finite, power is naturally $0$.
*   **Conclusion:** It is an **Energy Signal**.

**(ii) $x(t) = e^{\sigma t}u(-t), \sigma < 0$**
*   This signal also exists only for $t \le 0$. However, as $t \to -\infty$, a negative times a negative creates a positive exponent, so $e^{\sigma t} \to e^{\infty} \to \infty$.
*   **Energy:** $E = \int_{-\infty}^{0} e^{2\sigma t} dt$. Because $2\sigma$ is negative, evaluating this at the lower limit $-\infty$ yields infinity. $E = \mathbf{\infty}$.
*   **Power:** $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{0} e^{2\sigma t} dt$. The integral evaluates to infinity, and dividing by $T$ still yields infinity. $P = \mathbf{\infty}$.
*   **Conclusion:** It is **Neither an energy nor a power signal**.

**(iii) $x(t) = t[u(t+4) - u(t-4)]$**
*   This is the function $f(t) = t$ restricted to a specific window. The term $[u(t+4) - u(t-4)]$ is a rectangular gate that is $1$ between $t = -4$ and $t = 4$, and $0$ elsewhere.
*   Thus, $x(t) = t$ for $-4 \le t \le 4$, and $0$ otherwise.
*   Since it is a finite-amplitude signal existing over a strictly finite duration, it must have finite energy.
*   **Energy:** $E = \int_{-4}^{4} t^2 dt = \left[ \frac{t^3}{3} \right]_{-4}^{4} = \frac{4^3}{3} - \frac{(-4)^3}{3} = \frac{64}{3} - (-\frac{64}{3}) = \mathbf{\frac{128}{3} \text{ Joules}}$.
*   **Power:** Since energy is finite, power is naturally $P = \mathbf{0 \text{ Watts}}$.
*   **Conclusion:** It is an **Energy Signal**.

---

### **18. Pg 39, CT-1 Q2: Draw the following signal and comment whether the signal is energy, power or neither energy nor power signal. (i) $e^{-at} u(-t)$ and $a$ is real.**

**Analysis of the Signal:**
The signal is $x(t) = e^{-at} u(-t)$.
The term $u(-t)$ is a time-reversed unit step function. It acts as a "window" that is $1$ for all time $t < 0$ and $0$ for all time $t > 0$. This means our signal $x(t)$ only exists on the left side of the y-axis (negative time).
The behavior of the signal depends crucially on the sign of the real parameter $a$.

**Case 1: Assume $a > 0$ (Positive real number)**
*   **Sketch:** For $t < 0$, the exponent $-at$ becomes $(-)(\text{positive})(- \text{time}) = \text{positive}$. As $t \to -\infty$, the term $-at \to +\infty$. Therefore, the signal $e^{-at}$ grows exponentially towards infinity as you move left along the negative time axis. It reaches $1$ at $t=0$ and then drops to $0$ for $t>0$.
    *(Sketch description: An exponential curve rising rapidly from right to left in the 2nd quadrant, ending at $(0,1)$).*
*   **Energy Calculation:** $E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{0} (e^{-at})^2 dt = \int_{-\infty}^{0} e^{-2at} dt$
    $E = \left[ \frac{e^{-2at}}{-2a} \right]_{-\infty}^{0} = \frac{e^0}{-2a} - \frac{e^{-2a(-\infty)}}{-2a} = \frac{1}{-2a} - \frac{e^{\infty}}{-2a} = \frac{-1}{2a} + \infty = \mathbf{\infty}$
*   **Power Calculation:** Since energy is infinite, we check power. 
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{0} e^{-2at} dt = \lim_{T \to \infty} \frac{1}{2T} \left[ \frac{e^{-2at}}{-2a} \right]_{-T}^{0} = \lim_{T \to \infty} \frac{1}{2T} \left( \frac{1}{-2a} - \frac{e^{2aT}}{-2a} \right)$
    As $T \to \infty$, the term $e^{2aT} \to \infty$. Dividing infinity by infinity requires L'Hopital's rule, showing the exponential grows much faster than $T$. Thus, $P = \mathbf{\infty}$.
*   **Conclusion for $a > 0$:** The signal diverges. It is **Neither an energy nor a power signal**.

**Case 2: Assume $a < 0$ (Negative real number)**
Let $a = -b$, where $b > 0$. Then the signal is $x(t) = e^{bt} u(-t)$.
*   **Sketch:** For $t < 0$, the exponent $bt$ is $(+)(-) = \text{negative}$. As $t \to -\infty$, $bt \to -\infty$, so $e^{bt} \to 0$. The signal decays to $0$ as you move left. It rises to $1$ at $t=0$ and drops to $0$ for $t>0$.
    *(Sketch description: A bounded exponential curve starting near 0 on the far left, rising to $(0,1)$ in the 2nd quadrant).*
*   **Energy Calculation:** $E = \int_{-\infty}^{0} (e^{bt})^2 dt = \int_{-\infty}^{0} e^{2bt} dt = \left[ \frac{e^{2bt}}{2b} \right]_{-\infty}^{0}$
    $E = \frac{e^0}{2b} - \frac{e^{-\infty}}{2b} = \frac{1}{2b} - 0 = \mathbf{\frac{1}{2b}}$
*   Since $b$ is a finite positive number, the energy $E$ is a finite positive value.
*   **Conclusion for $a < 0$:** Because it has finite energy, it is an **Energy Signal**.

*(Note: Unless specified, problems often assume standard stable forms, but the full analysis covers both possibilities. If $a=0$, it's a step function which is a power signal. Given standard problem sets, demonstrating the case where it converges (is an energy signal) or diverges is expected).*

*Reference: Class Notes Pg 5-6, 9-10 (Energy & Power Signal).*

---

### **20. Pg 42, CT-01 Q1: For the following signal, $x(t)$ sketch (i) $y_1(t)=x(2t-5)$ and (ii) $y_3(t)=x(t)r(t)$. Provide a mathematical justification whether $y_2(t)$ is an energy signal or power signal or neither? Also computer the energy and power of $y_2(t)$. ![[Pasted image 20260712010221.png]]**

*(Note: There is a typo in the provided question text. It asks to sketch $y_1$ and $y_3$, but then asks to justify and compute for $y_2$. Let's assume the question intended to define $y_2(t)$ as one of the functions to be sketched, likely $y_2(t) = y_3(t) = x(t)r(t)$, which is a common pattern in these problem sets.)* Let's analyze $x(t)r(t)$.

**Base Signal $x(t)$ Analysis:**
The figure shows a triangular pulse.
*   Rises linearly from $t = -1$ to peak amplitude $1$ at $t = 0$. Equation for this segment: $x(t) = t + 1$.
*   Falls linearly from amplitude $1$ at $t = 0$ to $0$ at $t = 1$. Equation for this segment: $x(t) = -t + 1$.
*   $x(t) = 0$ for $t \le -1$ and $t \ge 1$.

**Solution:**

**(i) Sketch $y_1(t) = x(2t - 5)$**
*   **Transformations:** Rewrite as $x(2(t - 2.5))$. Time compression by a factor of 2, followed by a shift right by 2.5.
*   **Step-by-step using boundary mapping:** Map the original key points $t = \{-1, 0, 1\}$.
    *   $2t - 5 = -1 \implies 2t = 4 \implies t = 2$. (Start of signal)
    *   $2t - 5 = 0 \implies 2t = 5 \implies t = 2.5$. (Peak of signal, amplitude 1)
    *   $2t - 5 = 1 \implies 2t = 6 \implies t = 3$. (End of signal)
*   **Final Sketch:** A narrower triangular pulse shifted to the right. It starts at $t=2$, peaks at amplitude 1 at $t=2.5$, and drops to 0 at $t=3$.

**(ii) Sketch $y_2(t) = x(t)r(t)$** *(Assuming $y_2$ is $y_3$)*
*   **Analysis:** $r(t)$ is the unit ramp function, where $r(t) = t$ for $t \ge 0$, and $0$ for $t < 0$.
*   We multiply $x(t)$ pointwise by $r(t)$.
    *   For $t < 0$: $r(t) = 0$, so $y_2(t) = x(t) \cdot 0 = 0$. The left half of the triangle is eliminated.
    *   For $0 \le t \le 1$: $x(t) = -t + 1$, and $r(t) = t$. The product is $y_2(t) = t(-t + 1) = -t^2 + t$. This describes an inverted parabola. Let's find key points:
        *   At $t=0$, $y_2(0) = 0(1) = 0$.
        *   At $t=1$, $y_2(1) = 1(0) = 0$.
        *   Peak occurs at vertex. Derivative $-2t + 1 = 0 \implies t = 0.5$. Peak value $y_2(0.5) = -(0.5)^2 + 0.5 = 0.25$.
    *   For $t > 1$: $x(t) = 0$, so $y_2(t) = 0 \cdot t = 0$.
*   **Final Sketch:** The signal is $0$ everywhere except between $t=0$ and $t=1$. In that interval, draw a smooth parabolic curve starting at $(0,0)$, rising to a peak of $0.25$ at $t=0.5$, and falling back to $(1,0)$.

**(iii) Mathematical Justification & Computation of Energy and Power for $y_2(t)$**
*   **Justification:** The resulting signal $y_2(t)$ is non-zero only over a finite duration (from $t=0$ to $t=1$) and has a finite bounded amplitude (max $0.25$). Any signal that is entirely bounded within a finite time interval has a finite total area squared (energy). Therefore, it must be an **Energy Signal**.
*   **Energy Computation ($E$):**
    $E = \int_{-\infty}^{\infty} |y_2(t)|^2 dt = \int_{0}^{1} (-t^2 + t)^2 dt$
    Expand the integrand: $(-t^2 + t)^2 = t^4 - 2t^3 + t^2$
    $E = \int_{0}^{1} (t^4 - 2t^3 + t^2) dt = \left[ \frac{t^5}{5} - \frac{2t^4}{4} + \frac{t^3}{3} \right]_0^1$
    $E = \left( \frac{1}{5} - \frac{1}{2} + \frac{1}{3} \right) - 0$
    Find common denominator (30):
    $E = \frac{6}{30} - \frac{15}{30} + \frac{10}{30} = \frac{16 - 15}{30} = \mathbf{\frac{1}{30} \text{ Joules}}$.
*   **Power Computation ($P$):**
    Because it is a finite-duration energy signal, its average power computed over an infinite interval is zero.
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |y_2(t)|^2 dt = \lim_{T \to \infty} \frac{1/30}{2T} = \mathbf{0 \text{ Watts}}$.

*Reference: Class Notes Pg 5-6 (Energy & Power Signal), Pg 12-15 (Signal Operations).*

Here are the detailed solutions for questions 21 through 24 from your list.

---

### **23. Pg 44, CT-01 Q1: Sketch the signals and analytically determine if energy/power.**

**Solution:**

**(i) Sketch $u(4-t)$**
*   Rewrite as $u(-(t-4))$.
*   A standard unit step $u(t)$ turns "on" (becomes 1) for $t > 0$.
*   $u(-t)$ is time-reversed, so it is 1 for $t < 0$ and 0 for $t > 0$.
*   $u(-(t-4))$ shifts this reversed step 4 units to the right. It evaluates to 1 when $-(t-4) > 0 \implies t < 4$.
*   **Sketch:** A horizontal line at amplitude $1$ coming from $t = -\infty$, which drops abruptly to $0$ at exactly $t = 4$ and remains $0$ thereafter.

**(ii) Sketch $u(t-6) - u(t-8)$**
*   $u(t-6)$ is a unit step starting at $t=6$.
*   $u(t-8)$ is a unit step starting at $t=8$.
*   Subtracting the latter from the former turns the signal "off" at $t=8$.
*   **Sketch:** A rectangular pulse. It is $0$ everywhere except between $t = 6$ and $t = 8$, where it has an amplitude of $1$.

**(iii) Sketch $\sin(\pi t)[\delta(t+0.5) + \delta(t-0.5)]$**
*   Apply the sifting property of the Dirac delta function: $f(t)\delta(t-t_0) = f(t_0)\delta(t-t_0)$.
*   First term ($t_0 = -0.5$): $\sin(\pi(-0.5))\delta(t+0.5) = \sin(-\pi/2)\delta(t+0.5) = -1 \cdot \delta(t+0.5)$.
*   Second term ($t_0 = 0.5$): $\sin(\pi(0.5))\delta(t-0.5) = \sin(\pi/2)\delta(t-0.5) = 1 \cdot \delta(t-0.5)$.
*   The signal simplifies to: $y(t) = -\delta(t+0.5) + \delta(t-0.5)$.
*   **Sketch:** Draw two vertical arrows (impulses). One pointing downwards to $-1$ at $t = -0.5$. One pointing upwards to $1$ at $t = 0.5$. The rest of the axis is $0$.

**Analytical determination of Energy/Power for $u(t-4) - u(t-6)$:**
Let $y(t) = u(t-4) - u(t-6)$. This is a rectangular pulse of amplitude $1$ existing from $t=4$ to $t=6$.
*   **Energy ($E$):**
    $E = \int_{-\infty}^{\infty} |y(t)|^2 dt = \int_{4}^{6} (1)^2 dt = [t]_4^6 = 6 - 4 = \mathbf{2 \text{ Joules}}$
*   **Power ($P$):**
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |y(t)|^2 dt$.
    Since the integral evaluates to a finite number ($2$), as $T \to \infty$, the fraction $\frac{2}{2T}$ approaches $0$. Thus, $P = \mathbf{0 \text{ Watts}}$.
*   **Conclusion:** Because the signal has finite energy ($0 < E < \infty$) and zero average power, it is an **Energy Signal**.

# 3. Signal Fundamentals & Operations

### Q.1 (c) The output y(t) of the following figure is obtained by the transformation y(t)= x(2t-4). (i) Sketch the input, x(t). (ii) Analytically express, x(t). (Figure involved)
![[Pasted image 20260626191823.png]]
**Solution:**

We are given the relationship $y(t) = x(2t-4)$ and the graph of $y(t)$. We need to find $x(t)$.
First, let's derive the analytical expression for $y(t)$ from the provided graph. The graph shows a signal that is $0$ for $t < 1$, ramps up linearly to $1$ between $t=1$ and $t=2$, stays flat at $1$ until $t=3$, and is $0$ thereafter.
$$y(t) = \begin{cases} 
t - 1 & \text{for } 1 \le t < 2 \\
1 & \text{for } 2 \le t < 3 \\
0 & \text{otherwise} 
\end{cases}$$
Using unit step functions, this can be written as:
$$y(t) = (t-1)[u(t-1) - u(t-2)] + 1[u(t-2) - u(t-3)]$$

To find $x(t)$, we need to perform variable substitution on the given transformation. Let a dummy variable $\tau = 2t - 4$.
Solving for $t$, we get $2t = \tau + 4 \implies t = \frac{\tau}{2} + 2$.
Substitute this into the transformation equation:
$$y\left(\frac{\tau}{2} + 2\right) = x(\tau)$$
Replacing the dummy variable $\tau$ with $t$, we get the expression for $x(t)$:
$$x(t) = y\left(\frac{t}{2} + 2\right)$$
This indicates that $x(t)$ is formed by first shifting $y(t)$ to the left by 2 units (creating $y(t+2)$), and then expanding it in time by a factor of 2 (creating $y(t/2 + 2)$).

**(ii) Analytical expression for $x(t)$:**
We substitute $(t/2 + 2)$ into the piecewise definition of $y(t)$:
*   The segment $y(t) = t - 1$ for $1 \le t < 2$ becomes:
    $x(t) = (\frac{t}{2} + 2) - 1 = \frac{t}{2} + 1$
    This is valid for $1 \le (\frac{t}{2} + 2) < 2 \implies -1 \le \frac{t}{2} < 0 \implies -2 \le t < 0$.
*   The segment $y(t) = 1$ for $2 \le t < 3$ becomes:
    $x(t) = 1$
    This is valid for $2 \le (\frac{t}{2} + 2) < 3 \implies 0 \le \frac{t}{2} < 1 \implies 0 \le t < 2$.
*   Otherwise, $x(t) = 0$.

Putting it all together:
$$x(t) = \begin{cases} 
\frac{t}{2} + 1 & \text{for } -2 \le t < 0 \\
1 & \text{for } 0 \le t < 2 \\
0 & \text{otherwise} 
\end{cases}$$
Using step functions:
$$x(t) = \left(\frac{t}{2} + 1\right)[u(t+2) - u(t)] + 1[u(t) - u(t-2)]$$

**(i) Sketch the input, $x(t)$:**
Based on the analytical expression, $x(t)$ is a trapezoid. It starts at $t = -2$ with a value of $0$, ramps up linearly to a value of $1$ at $t = 0$, stays flat at $1$ until $t = 2$, and then drops to $0$ for $t > 2$.

Location pg 78 In pdf

### Q.1. (a) What is impulse function? Draw the following function $f(t) = 5\delta(t+2) + 10\delta(t) - 4\delta(t-3)$.

**Detailed Answer:**

**Definition of the Impulse Function:**
The continuous-time unit impulse function, denoted by $\delta(t)$ (also known as the Dirac delta function), is an idealized mathematical construct used to represent a signal that is infinitely narrow, infinitely tall, and has a finite area (specifically, an area of one). 

It is formally defined by two properties:
1.  **Zero everywhere except at the origin:** 
    $\delta(t) = 0$ for $t \neq 0$
2.  **Unit area:**
    $\int_{-\infty}^{\infty} \delta(t) dt = 1$

A crucial property of the impulse function is the **sampling (or sifting) property**. When a continuous function $\phi(t)$ is multiplied by an impulse located at $t = T$ and integrated over time, it extracts the value of the function at that specific instant:
$\int_{-\infty}^{\infty} \phi(t)\delta(t-T) dt = \phi(T)$

**Drawing the given function:**
The given function is $f(t) = 5\delta(t+2) + 10\delta(t) - 4\delta(t-3)$.
This function consists of three separate scaled and time-shifted impulses:

1.  **$5\delta(t+2)$:** This represents an impulse shifted to the left by 2 units (located at $t = -2$). The scalar multiplier $5$ means it has an area (or "strength") of 5. Graphically, this is drawn as a vertical arrow pointing upwards at $t = -2$ with a height or label indicating 5.
2.  **$10\delta(t)$:** This represents an impulse located at the origin ($t = 0$). The scalar multiplier $10$ means it has a strength of 10. Graphically, this is a vertical arrow pointing upwards at $t = 0$ with a label indicating 10.
3.  **$-4\delta(t-3)$:** This represents an impulse shifted to the right by 3 units (located at $t = 3$). The scalar multiplier $-4$ means it has a strength of 4, but the negative sign indicates it points downwards. Graphically, this is a vertical arrow pointing downwards at $t = 3$ with a label indicating -4.

**To sketch this:**
*   Draw a horizontal time axis ($t$).
*   At $t = -2$, draw an upward-pointing arrow and label it with strength 5.
*   At $t = 0$, draw a taller upward-pointing arrow and label it with strength 10.
*   At $t = 3$, draw a downward-pointing arrow and label it with strength -4.

always mention ans related location pg no. In pdf , at the end of every soln 1.4-2 The Unit Impulse Function $\delta(t)$, pg. 86

***

### (c) Define gate function. Express the following signal in terms of switching functions. (figure involved.)
![[Pasted image 20260628100238.png]]
**Detailed Answer:**

**Definition of Gate Function:**
A unit gate function, commonly denoted as $\text{rect}(t/\tau)$, is a rectangular pulse of unit height and width $\tau$, usually centered at the origin. It acts as a mathematical "gate," letting a signal pass through unmodified within a specific time interval and completely blocking it (multiplying by zero) outside that interval.
It is formally defined as:
$$\text{rect}\left(\frac{t}{\tau}\right) = \begin{cases} 1, & |t| < \tau/2 \\ 0, & |t| > \tau/2 \end{cases}$$
Alternatively, a gate function starting at time $t_1$ and ending at time $t_2$ can be defined using unit step functions (which the question refers to as "switching functions"):
$$\text{Gate}_{(t_1, t_2)}(t) = u(t - t_1) - u(t - t_2)$$

**Expressing the given signal:**
The provided figure shows a signal $f(t)$ that exists only in the interval from $t = 0$ to $t = T$. Outside this interval, the signal is zero. This means we will multiply some function by a gate that turns on at 0 and off at $T$, which is $[u(t) - u(t-T)]$.

Inside the interval $0 \le t \le T$, the signal is a straight line. Let's find the equation of this line $y = mt + c$.
We can identify two points on this line from the graph:
1.  At $t = 0$, the value is $E$. So, $(0, E)$. This gives us the y-intercept, $c = E$.
2.  At $t = T/2$, the value is $0$. So, $(T/2, 0)$.
3.  At $t = T$, the value is $-E$. So, $(T, -E)$.

Let's calculate the slope $m$:
$$m = \frac{\Delta y}{\Delta t} = \frac{-E - E}{T - 0} = \frac{-2E}{T}$$

So, the equation of the line that defines the signal within the active interval is:
$$y(t) = -\frac{2E}{T}t + E = E\left(1 - \frac{2t}{T}\right)$$

Now, we use the switching functions (unit step functions) to restrict this line to only exist between $t=0$ and $t=T$. We multiply the line equation by the gate function we defined earlier:
$$f(t) = E\left(1 - \frac{2t}{T}\right) [u(t) - u(t-T)]$$

Expanding this expression gives the final answer in terms of switching functions:
$$f(t) = E\left(1 - \frac{2t}{T}\right)u(t) - E\left(1 - \frac{2t}{T}\right)u(t-T)$$

always mention ans related location pg no. In pdf , at the end of every soln 1.4-1 The Unit Step Function u(t), pg. 83 and 7.2 Transforms of Some Useful Functions, pg. 689

***

### (c) Define gate function. Express the following signal in terms of switching functions. (figure involved.)
![[Pasted image 20260628171225.png]]
**Detailed Answer:**

**Definition of Gate Function:**
A unit gate function, commonly denoted as $\text{rect}(t/\tau)$, is a rectangular pulse of unit height and width $\tau$, usually centered at the origin. It acts as a mathematical "gate," letting a signal pass through unmodified within a specific time interval and completely blocking it (multiplying by zero) outside that interval.
It is formally defined as:
$$\text{rect}\left(\frac{t}{\tau}\right) = \begin{cases} 1, & |t| < \tau/2 \\ 0, & |t| > \tau/2 \end{cases}$$
Alternatively, a gate function starting at time $t_1$ and ending at time $t_2$ can be defined using unit step functions (which the question refers to as "switching functions"):
$$\text{Gate}_{(t_1, t_2)}(t) = u(t - t_1) - u(t - t_2)$$

**Expressing the given signal:**
The provided figure shows a signal $f(t)$ that exists only in the interval from $t = 0$ to $t = T$. Outside this interval, the signal is zero. This means we will multiply some function by a gate that turns on at 0 and off at $T$, which is $[u(t) - u(t-T)]$.

Inside the interval $0 \le t \le T$, the signal is a straight line. Let's find the equation of this line $y = mt + c$.
We can identify two points on this line from the graph:
1.  At $t = 0$, the value is $E$. So, $(0, E)$. This gives us the y-intercept, $c = E$.
2.  At $t = T/2$, the value is $0$. So, $(T/2, 0)$.
3.  At $t = T$, the value is $-E$. So, $(T, -E)$.

Let's calculate the slope $m$:
$$m = \frac{\Delta y}{\Delta t} = \frac{-E - E}{T - 0} = \frac{-2E}{T}$$

So, the equation of the line that defines the signal within the active interval is:
$$y(t) = -\frac{2E}{T}t + E = E\left(1 - \frac{2t}{T}\right)$$

Now, we use the switching functions (unit step functions) to restrict this line to only exist between $t=0$ and $t=T$. We multiply the line equation by the gate function we defined earlier:
$$f(t) = E\left(1 - \frac{2t}{T}\right) [u(t) - u(t-T)]$$

Expanding this expression gives the final answer in terms of switching functions:
$$f(t) = E\left(1 - \frac{2t}{T}\right)u(t) - E\left(1 - \frac{2t}{T}\right)u(t-T)$$

always mention ans related location pg no. In pdf , at the end of every soln 1.4-1 The Unit Step Function u(t), pg. 83 and 7.2 Transforms of Some Useful Functions, pg. 689

***

### (c) Find the first derivatives of the following signals and sketch the signals and their derivatives
### (i) Express the $sgn(t)$ function in terms of the step function
### Q.3. (a) Define switching functions with examples. Express the following signals interms of switching functions. (figure involved)
![[Pasted image 20260628170559.png]]
**Detailed Answer:**

**Definition of Switching Functions:**
Switching functions, often associated with the unit step function $u(t)$, are mathematical tools used to represent signals that turn "on" or "off" at specific instants in time. The basic unit step function is defined as:
$$u(t) = \begin{cases} 1, & \text{for } t > 0 \\ 0, & \text{for } t < 0 \end{cases}$$
A time-shifted unit step function $u(t - t_0)$ acts as a switch that closes (turns on to a value of 1) at time $t = t_0$. 
A "gate" function, which is "on" only between times $t_1$ and $t_2$, can be formed by subtracting two step functions: $[u(t - t_1) - u(t - t_2)]$.

**Expressing the signals:**

**(i) For signal $v_1(t)$:**
Looking at the first graph, the signal $v_1(t)$ is zero for $t < 1$. 
Between $t=1$ and $t=2$, the signal is a straight line. 
At $t=1$, the value is $-1$. 
At $t=2$, the value is $-2$.
The slope of this line is $m = \frac{-2 - (-1)}{2 - 1} = \frac{-1}{1} = -1$.
Using the point-slope form $(y - y_1 = m(t - t_1))$ with the point $(1, -1)$:
$v - (-1) = -1(t - 1) \implies v + 1 = -t + 1 \implies v = -t$
So, the equation of the line is $y(t) = -t$.
This line exists only in the interval $1 \le t \le 2$. We use a gate function to restrict it to this interval:
$$v_1(t) = -t \cdot [u(t - 1) - u(t - 2)]$$
$$v_1(t) = -t u(t - 1) + t u(t - 2)$$

**(ii) For signal $v_2(t)$:**
This signal consists of two distinct linear segments.
*   **Segment 1 ($0 \le t < 2$):** 
    The line passes through $(0, 2)$ and $(2, -2)$.
    Slope $m_1 = \frac{-2 - 2}{2 - 0} = \frac{-4}{2} = -2$.
    The y-intercept is $2$.
    The equation is $v = -2t + 2$.
    We multiply this by a gate function for the interval $[0, 2]$:
    $v_{2a}(t) = (-2t + 2) [u(t) - u(t - 2)]$

*   **Segment 2 ($2 \le t < 3$):**
    The line passes through $(2, -2)$ and $(3, 0)$.
    Slope $m_2 = \frac{0 - (-2)}{3 - 2} = \frac{2}{1} = 2$.
    Using point-slope form with $(3, 0)$: $v - 0 = 2(t - 3) \implies v = 2t - 6$.
    We multiply this by a gate function for the interval $[2, 3]$:
    $v_{2b}(t) = (2t - 6) [u(t - 2) - u(t - 3)]$

Combining both segments gives the full expression:
$$v_2(t) = (-2t + 2)[u(t) - u(t - 2)] + (2t - 6)[u(t - 2) - u(t - 3)]$$
Expanding and collecting terms with the same step functions:
$$v_2(t) = (-2t + 2)u(t) - (-2t + 2)u(t - 2) + (2t - 6)u(t - 2) - (2t - 6)u(t - 3)$$
$$v_2(t) = (-2t + 2)u(t) + [2t - 2 + 2t - 6]u(t - 2) - (2t - 6)u(t - 3)$$
**$$v_2(t) = (-2t + 2)u(t) + (4t - 8)u(t - 2) - (2t - 6)u(t - 3)$$**

always mention ans related location pg no. In pdf , at the end of every soln 1.4-1 The Unit Step Function u(t), pg. 83-85

***

### (c) Express the current pulse given in Fig. Q. 3(c) in terms of unit step and find its integral.
![[Pasted image 20260628170939.png]]
**Detailed Answer:**
**1. Expressing the current pulse $i(t)$:**
The graph in Fig. Q. 3(c) displays a piecewise constant signal.
*   From $t = 0$ to $t = 2$, the current amplitude is $+10$.
*   From $t = 2$ to $t = 4$, the current amplitude is $-10$.
*   The current is zero everywhere else.
We can express this mathematically using unit step functions $u(t)$. A rectangular pulse starting at $t=a$ and ending at $t=b$ with height $H$ is written as $H[u(t-a) - u(t-b)]$.
Applying this logic to our signal's two parts:
$$i(t) = 10[u(t) - u(t-2)] + (-10)[u(t-2) - u(t-4)]$$
$$i(t) = 10u(t) - 10u(t-2) - 10u(t-2) + 10u(t-4)$$
Combining like terms yields the final expression:
**$$i(t) = 10u(t) - 20u(t-2) + 10u(t-4)$$**

**2. Finding its integral:**
Let the integral of the current pulse be $q(t) = \int_{-\infty}^{t} i(\tau) d\tau$.
We know that the integral of a unit step function $u(t)$ is the unit ramp function, denoted as $r(t) = t \cdot u(t)$.
Integrating each term of $i(t)$ individually using the linearity property of integration:
$$q(t) = \int_{-\infty}^{t} [10u(\tau) - 20u(\tau-2) + 10u(\tau-4)] d\tau$$
**$$q(t) = 10r(t) - 20r(t-2) + 10r(t-4)$$**

To understand the shape of $q(t)$:
*   For $t \le 0$: $q(t) = 0$
*   For $0 < t \le 2$: $q(t) = 10t$ (a linear ramp rising to a peak of 20 at $t=2$)
*   For $2 < t \le 4$: $q(t) = 10t - 20(t-2) = -10t + 40$ (a linear ramp falling from 20 down to 0 at $t=4$)
*   For $t > 4$: $q(t) = 10t - 20(t-2) + 10(t-4) = 10t - 20t + 40 + 10t - 40 = 0$
The integral forms a single triangular pulse that exists between $t=0$ and $t=4$.

always mention ans related location pg no. In pdf , at the end of every soln 1.4-1 The Unit Step Function u(t), pg. 83-85

***

### **(c) Show that $\int_{-\infty}^{\infty} e^{-2(x-t)}\delta(2 - t) dt = e^{-2(x-2)}$**

First, note that the impulse function is even, meaning $\delta(2 - t) = \delta(-(t - 2)) = \delta(t - 2)$. The impulse is located at $t_0 = 2$, which lies within the integration limits $(-\infty, \infty)$.

- The integration variable is $t$ (while $x$ acts as a constant parameter).
    
- Evaluate the function $f(t) = e^{-2(x-t)}$ at $t = 2$:
    
    $$f(2) = e^{-2(x-2)}$$
    
- Therefore:
    
    $$\int_{-\infty}^{\infty} e^{-2(x-t)}\delta(2 - t) dt = \mathbf{e^{-2(x-2)}}$$

---

### **8. Pg 29, CT-1 Q3: Given the signal... Sketch the following signals derived from x(t)** ![[Pasted image 20260712005603.png]]

**Figure Analysis of Base Signal $x(t)$:**
The given signal $x(t)$ is:
*   $1$ for $0 \le t \le 1$
*   Ramps down from $1$ to $0$ linearly between $t = 1$ and $t = 2$.
*   $0$ everywhere else.

**Solution:**

**(i) Sketch $x(2t + 1)$**
*   **Transformations:** This involves a time shift (left by 1) followed by a time scaling (compression by 2).
*   **Step-by-step:**
    1.  Shift left by 1 ($x(t+1)$): The flat top moves to $[-1, 0]$ and the ramp moves to $[0, 1]$.
    2.  Compress by 2 ($x(2t+1)$): The $t$-axis values are halved. 
*   **Final Shape:** A signal that is flat at amplitude $1$ from $t = -0.5$ to $t = 0$, and ramps down to $0$ at $t = 0.5$.

**(ii) Sketch $x(t+1)u(-t)$**
*   **Transformations:** Shift left by 1, then multiply by a reversed unit step.
*   **Step-by-step:**
    1.  $x(t+1)$ shifts the entire signal left so it exists from $t=-1$ to $t=1$. The flat part is $[-1, 0]$ and the ramp is $[0, 1]$.
    2.  $u(-t)$ acts as a "window" that only lets the signal through for $t \le 0$ (it is $0$ for $t > 0$).
*   **Final Shape:** Only the flat part from the shifted signal survives. The result is a perfect rectangular pulse of amplitude $1$ from $t = -1$ to $t = 0$.

**(iii) Sketch $x(-t+1)u(t)$**
*   **Transformations:** Rewrite as $x(-(t-1))$. Time reversal, shift right by 1, then multiply by a unit step.
*   **Step-by-step:**
    1.  $x(-t)$ flips the signal across the y-axis. The flat part is now $[-1, 0]$ and the ramp (now rising) is $[-2, -1]$.
    2.  $x(-(t-1))$ shifts the flipped signal right by 1. The flat part moves to $[0, 1]$ and the rising ramp moves to $[-1, 0]$.
    3.  Multiply by $u(t)$, keeping only the $t \ge 0$ portion.
*   **Final Shape:** Only the flat part survives. The result is a perfect rectangular pulse of amplitude $1$ from $t = 0$ to $t = 1$.

**(iv) Sketch $x(t-1) + x(-t-1)$**
*   **Transformations:** This is the addition of two distinct signals.
*   **Step-by-step:**
    1.  $x(t-1)$ is shifted right by 1. It is flat from $t=1$ to $t=2$, and ramps down to $0$ at $t=3$.
    2.  $x(-t-1) = x(-(t+1))$ is reversed, then shifted left by 1. The original reversed signal $x(-t)$ lives in $[-2, 0]$. Shifting left by 1 moves it to $[-3, -1]$. It rises from $-3$ to $-2$, and is flat from $-2$ to $-1$.
*   **Final Shape:** An even, symmetric signal with two separate components. 
    *   Left side: Ramps up from $t=-3$ to $-2$, flat at amplitude $1$ from $t=-2$ to $-1$. 
    *   Gap: The signal is $0$ from $t=-1$ to $t=1$.
    *   Right side: Flat at amplitude $1$ from $t=1$ to $t=2$, ramps down to $0$ at $t=3$.

**(v) Sketch $x(t)\delta(t-1)$**
*   **Transformations:** Multiplication of a continuous signal by an impulse function.
*   **Property:** $f(t)\delta(t-t_0) = f(t_0)\delta(t-t_0)$. The impulse "samples" the value of the function at the time the impulse occurs.
*   **Step-by-step:**
    Here $t_0 = 1$. So, $x(t)\delta(t-1) = x(1)\delta(t-1)$.
    Looking at the original graph of $x(t)$, at exactly $t = 1$, the amplitude is $1$. 
    So, $x(1) = 1$.
*   **Final Shape:** The result is simply $1 \cdot \delta(t-1) = \delta(t-1)$. Sketch a single upward-pointing impulse arrow located at $t = 1$ on the axis, labeled with an area/weight of $1$.


Here are the detailed solutions for questions 9 through 12 from the provided list.

---

### **10. Pg 31, CT-1 Q2: Sketch the following signal and transformations.**

**Base Signal $x(t)$ Analysis:**
*   $x(t) = e^{2t}$ for $-4 \le t \le -2$ (A tiny exponential tail rising from left to right)
*   $x(t) = 2$ for $-2 \le t \le 2$ (A flat rectangular center)
*   $x(t) = e^{-2t}$ for $2 \le t \le 4$ (A tiny exponential tail decaying from left to right)
*   $x(t) = 0$ otherwise.
*(Note: $e^{-4}$ is approximately $0.018$, so these tails are extremely small and drop steeply to the axis. The signal is symmetric around the y-axis, meaning it is an **even function**: $x(-t) = x(t)$).*

**Transformations $y(t) = x(\alpha t + \beta)$:**
When applying transformations, we follow the order: $x(\alpha t + \beta) = x(\alpha(t + \frac{\beta}{\alpha}))$. First scale by $\alpha$, then shift by $-\frac{\beta}{\alpha}$. We map the original boundaries $[-4, -2, 2, 4]$ to new $t$ values by setting $\alpha t + \beta$ equal to the old boundaries.

**(i) $\alpha=-2, \beta=0 \implies y_1(t) = x(-2t)$**
*   Because $x(t)$ is even, $x(-2t) = x(2t)$. This is purely a time compression by a factor of 2.
*   Divide all original $t$-boundaries by 2.
*   New boundaries: $[-2, -1, 1, 2]$.
*   **Sketch Description:** The flat top is compressed to span from $t = -1$ to $t = 1$ (amplitude remains 2). The left exponential tail spans from $t = -2$ to $t = -1$. The right exponential tail spans from $t = 1$ to $t = 2$.

**(ii) $\alpha=2, \beta=-4 \implies y_2(t) = x(2t - 4)$**
*   Set $2t - 4$ equal to original boundaries:
    $2t - 4 = -4 \implies t = 0$
    $2t - 4 = -2 \implies t = 1$
    $2t - 4 = 2 \implies t = 3$
    $2t - 4 = 4 \implies t = 4$
*   **Sketch Description:** The entire signal is compressed by 2 and shifted to the right. The left tail is from $t = 0$ to $t = 1$. The flat top (amplitude 2) is from $t = 1$ to $t = 3$. The right tail is from $t = 3$ to $t = 4$.

**(iii) $\alpha=-1, \beta=4 \implies y_3(t) = x(-t + 4)$**
*   Set $-t + 4$ equal to original boundaries:
    $-t + 4 = -4 \implies t = 8$
    $-t + 4 = -2 \implies t = 6$
    $-t + 4 = 2 \implies t = 2$
    $-t + 4 = 4 \implies t = 0$
*   **Sketch Description:** The signal is time-reversed (which looks identical to the original due to symmetry) and shifted right by 4. The left tail is from $t = 0$ to $t = 2$. The flat top (amplitude 2) is from $t = 2$ to $t = 6$. The right tail is from $t = 6$ to $t = 8$.

---

### **12. Pg 32, CT-1 Q2: For the following signal $x(t)$, sketch the transformations.**

**Base Signal $x(t)$ Analysis:**
*   $x(t) = t$ for $0 \le t \le 2$ (A linear ramp starting from $(0,0)$ up to coordinate $(2,2)$).
*   $x(t) = 2$ for $2 \le t \le 4$ (A flat constant line from $t=2$ to $t=4$ at an amplitude of $2$).
*   $x(t) = 0$ otherwise. (Drops abruptly to $0$ at $t=4$).

**(i) Sketch $x(t/2)$**
*   **Transformation:** Time expansion by a factor of 2. All $t$-coordinates of key features are multiplied by 2.
*   **New Coordinates:** 
    *   Start of ramp: $(0 \times 2, 0) \to (0, 0)$
    *   End of ramp / Start of flat: $(2 \times 2, 2) \to (4, 2)$
    *   End of flat / Drop to zero: $(4 \times 2, 2) \to (8, 2)$
*   **Sketch Description:** A ramp starting at $t=0$ rising to an amplitude of $2$ at $t=4$. Then a flat constant line at amplitude $2$ extending from $t=4$ to $t=8$, dropping to zero at $t=8$.

**(ii) Sketch $x(t+4)$**
*   **Transformation:** Time advance (shift to the left) by 4 units. All $t$-coordinates subtract 4.
*   **New Coordinates:**
    *   Start of ramp: $(0 - 4, 0) \to (-4, 0)$
    *   End of ramp: $(2 - 4, 2) \to (-2, 2)$
    *   End of flat: $(4 - 4, 2) \to (0, 2)$
*   **Sketch Description:** The whole signal moves into the negative time axis. A ramp starts at $t=-4$ rising to amplitude $2$ at $t=-2$. A flat line continues from $t=-2$ to $t=0$, dropping to zero at $t=0$.

**(iii) Sketch $x(4-t)$**
*   **Transformation:** Rewrite as $x(-(t-4))$. This is a time reversal (flip across y-axis) followed by a shift to the right by 4 units.
*   *Alternatively, map boundaries:* Set $4-t$ equal to original boundaries $[0, 2, 4]$.
    $4-t = 0 \implies t=4$ (Signal ends here)
    $4-t = 2 \implies t=2$
    $4-t = 4 \implies t=0$ (Signal starts here)
*   **Sketch Description:** A flat top starts at $t=0$ and goes to $t=2$ at an amplitude of $2$. At $t=2$, it begins a linear ramp downward, hitting zero exactly at $t=4$. (It looks like a mirrored version of the original signal, stationed perfectly adjacent to the y-axis).

**(iv) Sketch $x(2t+6)$**
*   **Transformation:** Rewrite as $x(2(t+3))$. This is a time compression by a factor of 2, followed by a shift to the left by 3 units.
*   *Map boundaries:* Set $2t+6$ equal to original boundaries $[0, 2, 4]$.
    $2t+6 = 0 \implies 2t = -6 \implies t = -3$
    $2t+6 = 2 \implies 2t = -4 \implies t = -2$
    $2t+6 = 4 \implies 2t = -2 \implies t = -1$
*   **Sketch Description:** The entire signal is compressed and sits entirely on the negative axis. It starts with a ramp from $(-3, 0)$ up to $(-2, 2)$. It is followed by a flat top at amplitude $2$ from $t = -2$ to $t = -1$, dropping to zero at $t = -1$.


Here are the detailed solutions for questions 13 through 16 from the provided list.

---

### **19. Pg 39, CT-1 Q3: Given the signal $x(t)$ in the following figure. Sketch the following signals derived from $x(t)$. ![[Pasted image 20260712005941.png]]**

**Base Signal $x(t)$ Analysis:**
The image shows a pulse waveform $x(t)$:
*   $x(t) = 0$ for $t < -1$
*   $x(t) = 1$ for $-1 \le t \le 0$
*   $x(t) = 2$ for $0 < t \le 1$
*   $x(t) = 0$ for $t > 1$
It is a staircase-like pulse composed of two rectangular segments.

**Solution:**

**(i) Sketch $x(2t - 1)$**
*   **Transformations:** Rewrite as $x(2(t - 0.5))$. This involves a time compression by a factor of 2, followed by a time shift to the right by 0.5 units.
*   **Step-by-step using boundary mapping:** Set the argument $2t - 1$ equal to the key transition points of the original signal $t = \{-1, 0, 1\}$.
    *   Transition 1 (starts rising): $2t - 1 = -1 \implies 2t = 0 \implies t = 0$. (Amplitude goes from 0 to 1).
    *   Transition 2 (steps up): $2t - 1 = 0 \implies 2t = 1 \implies t = 0.5$. (Amplitude steps from 1 to 2).
    *   Transition 3 (drops to zero): $2t - 1 = 1 \implies 2t = 2 \implies t = 1$. (Amplitude drops from 2 to 0).
*   **Final Sketch:** 
    *   From $t = 0$ to $t = 0.5$, draw a horizontal line at amplitude 1.
    *   From $t = 0.5$ to $t = 1$, draw a horizontal line at amplitude 2.
    *   Signal is 0 outside this interval $[0, 1]$.

**(ii) Sketch $x(t+1)u(-t)$**
*   **Transformations:** Time shift left by 1, then multiply by a reversed unit step.
*   **Step-by-step:**
    1.  $x(t+1)$: Shift the entire original signal to the left by 1 unit.
        *   The segment $[-1, 0]$ with amplitude 1 moves to $[-2, -1]$.
        *   The segment $[0, 1]$ with amplitude 2 moves to $[-1, 0]$.
    2.  $u(-t)$: This is a window that is 1 for $t < 0$ and 0 for $t > 0$.
    3.  Multiplication: Multiply the shifted signal by this window. The entire shifted signal lies in the region $t \le 0$, so the window $u(-t)$ preserves the entire shifted signal.
*   **Final Sketch:** 
    *   From $t = -2$ to $t = -1$, amplitude is 1.
    *   From $t = -1$ to $t = 0$, amplitude is 2.
    *   Signal drops to 0 at $t = 0$ and remains 0 for $t > 0$.

**(iii) Sketch $x(-t+1)u(t)$**
*   **Transformations:** Rewrite as $x(-(t-1))$. Time reversal, shift right by 1, then multiply by a unit step.
*   **Step-by-step:**
    1.  $x(-t)$: Time-reverse (mirror) the original signal across the y-axis.
        *   The original segment $[0, 1]$ with amp 2 flips to $[-1, 0]$.
        *   The original segment $[-1, 0]$ with amp 1 flips to $[0, 1]$.
    2.  $x(-(t-1))$: Shift this mirrored signal to the right by 1 unit.
        *   The segment $[-1, 0]$ (amp 2) moves to $[0, 1]$.
        *   The segment $[0, 1]$ (amp 1) moves to $[1, 2]$.
    3.  $u(t)$: This window is 1 for $t > 0$ and 0 for $t < 0$.
    4.  Multiplication: The entire shifted-and-mirrored signal lies in $t \ge 0$, so the window $u(t)$ preserves all of it.
*   **Final Sketch:**
    *   From $t = 0$ to $t = 1$, amplitude is 2.
    *   From $t = 1$ to $t = 2$, amplitude is 1.
    *   Signal is 0 outside this interval.

**(iv) Sketch $x(t)[u(t-1) - u(t-2)]$**
*   **Transformations:** Multiply the original signal by a rectangular window.
*   **Step-by-step:**
    1.  Analyze the window: $[u(t-1) - u(t-2)]$ creates a rectangular pulse that is 1 strictly between $t = 1$ and $t = 2$, and 0 everywhere else.
    2.  Analyze the original signal $x(t)$ in that window: Look at the original graph of $x(t)$ between $t=1$ and $t=2$. The original signal $x(t)$ is exactly 0 everywhere in that region (it ends at $t=1$).
    3.  Multiplication: Multiplying $x(t)$ (which is 0 in this region) by the window (which is 1 in this region) results in 0. Multiplying everywhere else where the window is 0 also results in 0.
*   **Final Sketch:** The result is a flat line at $y = 0$ for all time $t$. The signal is completely zeroed out.

**(v) Sketch $x(t)\delta(t-2)$**
*   **Transformations:** Multiply the original continuous signal by a shifted impulse function.
*   **Property:** The sifting property states $f(t)\delta(t-t_0) = f(t_0)\delta(t-t_0)$. The result is an impulse at $t_0$ weighted by the value of the function at that specific instant.
*   **Step-by-step:**
    Here $t_0 = 2$. Therefore, $x(t)\delta(t-2) = x(2)\delta(t-2)$.
    Looking at the original graph of $x(t)$, at the exact instant $t = 2$, the value of the signal is $0$.
    So, $x(2) = 0$.
    The result is $0 \cdot \delta(t-2) = 0$.
*   **Final Sketch:** The result is a flat line at $y = 0$ for all time $t$. There is no impulse because its weight is zero.

*Reference: Class Notes Pg 12-15 (Signal Operations), Pg 22 (Singularity functions/Impulse).*

# 4. Laplace Transform

### (b) Find the Laplace transform of the following function $h(t)$. (figure involved.)
![[Pasted image 20260628100212.png]]
**Detailed Answer:**

The given figure shows a periodic signal $h(t)$. It's a triangular wave that oscillates between an amplitude of $1$ and $3$, with a period $T = 2$.
Since it is a periodic function, its Laplace transform $H(s)$ can be found using the formula for periodic signals:
$$H(s) = \frac{H_1(s)}{1 - e^{-sT}}$$
where $H_1(s)$ is the Laplace transform of the first period of the signal, and $T$ is the fundamental period. Here, $T=2$.

Let's define the function for the first period, $h_1(t)$, which exists for $0 \le t < 2$ and is zero elsewhere. 
We can view $h_1(t)$ as a DC offset of 1 added to a triangular pulse that goes from 0 to 2 and back to 0.
$h_1(t) = 1 \cdot \text{pulse}_{(0,2)} + \text{triangle}_{(0,2)}$

Let's build this systematically using ramp functions $r(t) = t u(t)$. A unit ramp has a slope of 1.
*   The signal starts at $t=0$ with a value of $1$. Because we are dealing with unilateral Laplace transforms ($t \ge 0$), this initial DC value can be represented by a unit step: $1 \cdot u(t)$.
*   From $t=0$ to $t=1$, the signal rises from 1 to 3. The slope is $\frac{3-1}{1-0} = 2$. We add a ramp of slope 2 starting at $t=0$: $+2r(t)$.
    Current function: $u(t) + 2tu(t)$
*   At $t=1$, the signal must start falling from 3 to 1. The slope of the segment from $t=1$ to $t=2$ is $\frac{1-3}{2-1} = -2$. The current slope is $+2$, so we need to add a ramp that changes the net slope to $-2$. We must add a slope of $-4$ starting at $t=1$: $-4r(t-1)$.
    Current function: $u(t) + 2tu(t) - 4(t-1)u(t-1)$
*   At $t=2$, the single-period signal $h_1(t)$ must return to zero (since it represents *only* the first period). The current slope is $-2$. To flatten it to $0$, we add a ramp of slope $+2$ at $t=2$: $+2r(t-2)$.
    Current function: $u(t) + 2tu(t) - 4(t-1)u(t-1) + 2(t-2)u(t-2)$
    Let's check the value for $t > 2$: $1 + 2t - 4(t-1) + 2(t-2) = 1 + 2t - 4t + 4 + 2t - 4 = 1$.
*   The value is stuck at 1 for $t>2$. We need it to be 0 for $t>2$ to properly define just one period. We must subtract a step function at $t=2$: $-1 \cdot u(t-2)$.
    Final expression for one period:
    $$h_1(t) = u(t) + 2r(t) - 4r(t-1) + 2r(t-2) - u(t-2)$$

Now, we take the Laplace transform of $h_1(t)$. We know that $\mathcal{L}\{u(t)\} = \frac{1}{s}$ and $\mathcal{L}\{r(t)\} = \frac{1}{s^2}$. Applying the time-shifting property:
$$H_1(s) = \frac{1}{s} + \frac{2}{s^2} - \frac{4}{s^2}e^{-s} + \frac{2}{s^2}e^{-2s} - \frac{1}{s}e^{-2s}$$

Group the $1/s$ and $1/s^2$ terms:
$$H_1(s) = \frac{1}{s}(1 - e^{-2s}) + \frac{2}{s^2}(1 - 2e^{-s} + e^{-2s})$$
Notice that $(1 - 2e^{-s} + e^{-2s})$ is a perfect square: $(1 - e^{-s})^2$.
$$H_1(s) = \frac{1 - e^{-2s}}{s} + \frac{2(1 - e^{-s})^2}{s^2}$$

Now, apply the formula for periodic signals to find the full transform $H(s)$:
$$H(s) = \frac{H_1(s)}{1 - e^{-sT}} = \frac{H_1(s)}{1 - e^{-2s}}$$
$$H(s) = \frac{\frac{1 - e^{-2s}}{s} + \frac{2(1 - e^{-s})^2}{s^2}}{1 - e^{-2s}}$$
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})^2}{s^2(1 - e^{-2s})}$$

We can simplify the denominator of the second term using the difference of squares: $(1 - e^{-2s}) = (1 - e^{-s})(1 + e^{-s})$.
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})^2}{s^2(1 - e^{-s})(1 + e^{-s})}$$
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})}{s^2(1 + e^{-s})}$$

always mention ans related location pg no. In pdf , at the end of every soln 4.2-1 Time Shifting, pg. 349-351


### (b) Find the Laplace transform of the following function $h(t)$. (figure involved.)
![[Pasted image 20260628171238.png]]
**Detailed Answer:**

The given figure shows a periodic signal $h(t)$. It's a triangular wave that oscillates between an amplitude of $1$ and $3$, with a period $T = 2$.
Since it is a periodic function, its Laplace transform $H(s)$ can be found using the formula for periodic signals:
$$H(s) = \frac{H_1(s)}{1 - e^{-sT}}$$
where $H_1(s)$ is the Laplace transform of the first period of the signal, and $T$ is the fundamental period. Here, $T=2$.

Let's define the function for the first period, $h_1(t)$, which exists for $0 \le t < 2$ and is zero elsewhere. 
We can view $h_1(t)$ as a DC offset of 1 added to a triangular pulse that goes from 0 to 2 and back to 0.
$h_1(t) = 1 \cdot \text{pulse}_{(0,2)} + \text{triangle}_{(0,2)}$

Let's build this systematically using ramp functions $r(t) = t u(t)$. A unit ramp has a slope of 1.
*   The signal starts at $t=0$ with a value of $1$. Because we are dealing with unilateral Laplace transforms ($t \ge 0$), this initial DC value can be represented by a unit step: $1 \cdot u(t)$.
*   From $t=0$ to $t=1$, the signal rises from 1 to 3. The slope is $\frac{3-1}{1-0} = 2$. We add a ramp of slope 2 starting at $t=0$: $+2r(t)$.
    Current function: $u(t) + 2tu(t)$
*   At $t=1$, the signal must start falling from 3 to 1. The slope of the segment from $t=1$ to $t=2$ is $\frac{1-3}{2-1} = -2$. The current slope is $+2$, so we need to add a ramp that changes the net slope to $-2$. We must add a slope of $-4$ starting at $t=1$: $-4r(t-1)$.
    Current function: $u(t) + 2tu(t) - 4(t-1)u(t-1)$
*   At $t=2$, the single-period signal $h_1(t)$ must return to zero (since it represents *only* the first period). The current slope is $-2$. To flatten it to $0$, we add a ramp of slope $+2$ at $t=2$: $+2r(t-2)$.
    Current function: $u(t) + 2tu(t) - 4(t-1)u(t-1) + 2(t-2)u(t-2)$
    Let's check the value for $t > 2$: $1 + 2t - 4(t-1) + 2(t-2) = 1 + 2t - 4t + 4 + 2t - 4 = 1$.
*   The value is stuck at 1 for $t>2$. We need it to be 0 for $t>2$ to properly define just one period. We must subtract a step function at $t=2$: $-1 \cdot u(t-2)$.
    Final expression for one period:
    $$h_1(t) = u(t) + 2r(t) - 4r(t-1) + 2r(t-2) - u(t-2)$$

Now, we take the Laplace transform of $h_1(t)$. We know that $\mathcal{L}\{u(t)\} = \frac{1}{s}$ and $\mathcal{L}\{r(t)\} = \frac{1}{s^2}$. Applying the time-shifting property:
$$H_1(s) = \frac{1}{s} + \frac{2}{s^2} - \frac{4}{s^2}e^{-s} + \frac{2}{s^2}e^{-2s} - \frac{1}{s}e^{-2s}$$

Group the $1/s$ and $1/s^2$ terms:
$$H_1(s) = \frac{1}{s}(1 - e^{-2s}) + \frac{2}{s^2}(1 - 2e^{-s} + e^{-2s})$$
Notice that $(1 - 2e^{-s} + e^{-2s})$ is a perfect square: $(1 - e^{-s})^2$.
$$H_1(s) = \frac{1 - e^{-2s}}{s} + \frac{2(1 - e^{-s})^2}{s^2}$$

Now, apply the formula for periodic signals to find the full transform $H(s)$:
$$H(s) = \frac{H_1(s)}{1 - e^{-sT}} = \frac{H_1(s)}{1 - e^{-2s}}$$
$$H(s) = \frac{\frac{1 - e^{-2s}}{s} + \frac{2(1 - e^{-s})^2}{s^2}}{1 - e^{-2s}}$$
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})^2}{s^2(1 - e^{-2s})}$$

We can simplify the denominator of the second term using the difference of squares: $(1 - e^{-2s}) = (1 - e^{-s})(1 + e^{-s})$.
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})^2}{s^2(1 - e^{-s})(1 + e^{-s})}$$
$$H(s) = \frac{1}{s} + \frac{2(1 - e^{-s})}{s^2(1 + e^{-s})}$$

always mention ans related location pg no. In pdf , at the end of every soln 4.2-1 Time Shifting, pg. 349-351


### (b) Find the Laplace transform of the following signal using the properties of Laplace transform. (figure involved.)
![[Pasted image 20260628100524.png]]
**Detailed Answer:**

To find the Laplace transform of the given periodic signal $f(t)$, we first determine the mathematical expression for a single period of the signal. Looking at the graph, the signal is a sawtooth wave that repeats every $T=2$ seconds. 

Let's define the first period of the signal as $f_1(t)$. From $t=0$ to $t=1$, the signal rises linearly from 0 to 5, which can be represented by the equation $5t$. From $t=1$ to $t=2$, the signal is 0. 
We can express $f_1(t)$ using the unit step function $u(t)$:
$$f_1(t) = 5t [u(t) - u(t-1)]$$
$$f_1(t) = 5t u(t) - 5t u(t-1)$$

To use the time-shifting property of the Laplace transform, which states that $\mathcal{L}\{x(t-a)u(t-a)\} = e^{-as}X(s)$, we need to rewrite the second term so it is in the form of $(t-1)$:
$$f_1(t) = 5t u(t) - 5(t - 1 + 1)u(t-1)$$
$$f_1(t) = 5t u(t) - 5(t-1)u(t-1) - 5u(t-1)$$

Now, we apply the Laplace transform to $f_1(t)$ using the linearity and time-shifting properties. We know the standard transforms $\mathcal{L}\{t u(t)\} = \frac{1}{s^2}$ and $\mathcal{L}\{u(t)\} = \frac{1}{s}$:
$$F_1(s) = \mathcal{L}\{5t u(t)\} - \mathcal{L}\{5(t-1)u(t-1)\} - \mathcal{L}\{5u(t-1)\}$$
$$F_1(s) = \frac{5}{s^2} - \frac{5}{s^2}e^{-s} - \frac{5}{s}e^{-s}$$
$$F_1(s) = \frac{5 - 5e^{-s} - 5se^{-s}}{s^2}$$

For a periodic signal $f(t)$ with period $T$, the Laplace transform is given by the property:
$$F(s) = \frac{F_1(s)}{1 - e^{-sT}}$$

Substituting our $F_1(s)$ and $T=2$ into this periodic property formula gives the final Laplace transform:
$$F(s) = \frac{\frac{5 - 5e^{-s} - 5se^{-s}}{s^2}}{1 - e^{-2s}}$$
$$F(s) = \frac{5[1 - e^{-s}(1+s)]}{s^2(1 - e^{-2s})}$$

"""always mention ans related location pg no. In pdf , at the end of every soln 4.2-1 Time Shifting property, pg. 349"""

***

### Q.2. (a) Explain the following properties of the Laplace transform: (i) Scaling (ii) Time shift (iii) Frequency shift.

**Detailed Answer:**

Let $x(t)$ be a continuous-time signal and $X(s)$ be its Laplace transform, denoted as $\mathcal{L}[x(t)] = X(s)$. The specified properties describe how modifications to the signal in the time domain affect its representation in the complex frequency ($s$) domain.

**(i) Scaling Property**
The scaling property states that scaling the time variable $t$ by a real, positive constant $a$ ($a > 0$) results in an inverse scaling of the $s$-domain variable and the overall amplitude of the transform. 
Mathematically, if $x(t) \Longleftrightarrow X(s)$, then:
$$\mathcal{L}[x(at)] = \frac{1}{a} X\left(\frac{s}{a}\right)$$
*Explanation:* Time compression of a signal by a factor $a$ (where $a > 1$) causes the signal to happen faster. In the frequency domain, this results in an expansion of the Laplace transform along the $s$-scale by the same factor $a$, accompanied by an amplitude reduction by a factor of $1/a$. Conversely, time expansion ($a < 1$) results in frequency compression.

**(ii) Time Shifting Property**
The time-shifting property relates a delay in the time domain to a phase shift (multiplication by a complex exponential) in the $s$-domain.
Mathematically, if $x(t)u(t) \Longleftrightarrow X(s)$, then for a time delay $t_0 \ge 0$:
$$\mathcal{L}[x(t - t_0)u(t - t_0)] = X(s)e^{-st_0}$$
*Explanation:* Delaying a causal signal by $t_0$ seconds does not change its basic shape, but it shifts its starting point. In the Laplace domain, this time delay amounts to multiplying the original, unshifted transform $X(s)$ by the exponential factor $e^{-st_0}$.

**(iii) Frequency Shifting Property**
The frequency-shifting property is the dual of the time-shifting property. It states that multiplying a time-domain signal by an exponential function results in a shift in the complex frequency domain.
Mathematically, if $x(t) \Longleftrightarrow X(s)$, then:
$$\mathcal{L}[x(t)e^{s_0 t}] = X(s - s_0)$$
*Explanation:* If a signal is multiplied by $e^{s_0 t}$, the entire Laplace spectrum of that signal is shifted in the $s$-plane by the amount $s_0$. If $s_0$ is purely imaginary (e.g., $j\omega_0$), this represents a shift along the frequency axis, which forms the basis for modulation.

always mention ans related location pg no. In pdf , at the end of every soln 4.2 Some Properties of the Laplace Transform, pg. 349-357

***

### Q.2. (b) Find the Laplace transform of the function h(t) in the figure below. (figure involved.)
![[Pasted image 20260628100445.png]]
**Detailed Answer:**

To find the Laplace transform of the given waveform $h(t)$, we first need to express the graphical piecewise-constant function as a mathematical equation using the unit step function, $u(t)$. 

The unit step function $u(t)$ is defined as 1 for $t \ge 0$ and 0 for $t < 0$. A delayed unit step $u(t-a)$ turns "on" at $t=a$.

Looking at the graph of $h(t)$:
1.  The signal turns "on" at $t = 0$ with an amplitude of 10. This can be represented by $10u(t)$.
2.  At $t = 2$, the signal amplitude drops from 10 to 5. We can represent this drop by subtracting a step function of amplitude 5 that starts at $t=2$. This is $-5u(t-2)$.
3.  At $t = 4$, the signal amplitude drops from 5 to 0. We can represent this final drop by subtracting another step function of amplitude 5 that starts at $t=4$. This is $-5u(t-4)$.

Combining these components, the mathematical expression for the signal is:
$h(t) = 10u(t) - 5u(t-2) - 5u(t-4)$

Now, we take the unilateral Laplace transform of this equation. Because the Laplace transform is a linear operator, we can take the transform of each term individually:
$H(s) = \mathcal{L}[10u(t)] - \mathcal{L}[5u(t-2)] - \mathcal{L}[5u(t-4)]$

We use the standard Laplace transform for a unit step function:
$\mathcal{L}[u(t)] = \frac{1}{s}$

And we apply the time-shifting property $\mathcal{L}[x(t-t_0)u(t-t_0)] = X(s)e^{-st_0}$ to the delayed step functions:
$\mathcal{L}[u(t-2)] = \frac{1}{s}e^{-2s}$
$\mathcal{L}[u(t-4)] = \frac{1}{s}e^{-4s}$

Substituting these into our equation for $H(s)$ gives:
$H(s) = 10\left(\frac{1}{s}\right) - 5\left(\frac{e^{-2s}}{s}\right) - 5\left(\frac{e^{-4s}}{s}\right)$

Factoring out the common term $\frac{5}{s}$:
$H(s) = \frac{5}{s} \left( 2 - e^{-2s} - e^{-4s} \right)$

always mention ans related location pg no. In pdf , at the end of every soln 4.2-1 Time Shifting (Example 4.6), pg. 350-351

***

### Q.3. (a) Calculate the Laplace transform of the following function. (figure involved.)
![[Pasted image 20260628100339.png]]
**Detailed Answer:**

To calculate the Laplace transform of the given periodic signal $f(t)$, we first establish the mathematical expression for a single period of the waveform. Let's denote the first period of the signal as $f_1(t)$.

Looking at the provided graph:
1.  The signal is a sawtooth (or triangular) wave that starts at $t=0$ and ends one cycle at $t=2$. Therefore, the fundamental period is $T = 2$ seconds.
2.  During the first period ($0 \le t < 2$), the signal has two distinct parts:
    *   From $t=0$ to $t=1$, it rises linearly from an amplitude of 0 to 2. The equation for this line is $y = 2t$.
    *   From $t=1$ to $t=2$, the amplitude is 0.

We can express the first period $f_1(t)$ mathematically using the unit step function $u(t)$:
$$f_1(t) = 2t [u(t) - u(t-1)]$$
$$f_1(t) = 2t u(t) - 2t u(t-1)$$

To apply the Laplace transform, we need to utilize the time-shifting property, which states that $\mathcal{L}\{x(t-a)u(t-a)\} = e^{-as}X(s)$. To use this, the $t$ multiplying the delayed step function must also be delayed by the same amount. We rewrite the second term by adding and subtracting 1:
$$f_1(t) = 2t u(t) - 2(t - 1 + 1)u(t-1)$$
$$f_1(t) = 2t u(t) - 2(t-1)u(t-1) - 2u(t-1)$$

Now, we take the Laplace transform of the single period, denoted as $F_1(s)$, using the linearity property and standard transform pairs ($\mathcal{L}\{t u(t)\} = \frac{1}{s^2}$ and $\mathcal{L}\{u(t)\} = \frac{1}{s}$):
$$F_1(s) = \mathcal{L}\{2t u(t)\} - \mathcal{L}\{2(t-1)u(t-1)\} - \mathcal{L}\{2u(t-1)\}$$
$$F_1(s) = \frac{2}{s^2} - \frac{2}{s^2}e^{-s} - \frac{2}{s}e^{-s}$$
Finding a common denominator:
$$F_1(s) = \frac{2 - 2e^{-s} - 2se^{-s}}{s^2}$$

Finally, we apply the property for periodic signals. If a signal $f(t)$ is periodic with period $T$, its Laplace transform $F(s)$ is related to the transform of its first period $F_1(s)$ by the formula:
$$F(s) = \frac{F_1(s)}{1 - e^{-sT}}$$

Substituting our calculated $F_1(s)$ and the period $T = 2$:
$$F(s) = \frac{\frac{2 - 2e^{-s} - 2se^{-s}}{s^2}}{1 - e^{-2s}}$$
$$F(s) = \frac{2[1 - e^{-s} - se^{-s}]}{s^2(1 - e^{-2s})}$$

always mention ans related location pg no. In pdf , at the end of every soln 4.2-1 Time Shifting, pg. 349-351

***

### Q.4 (a) Sketch the ROC of each of the following signals and also identify whether they are Laplace transformable or not? (i) $e^{at} u(-t)$ (ii) $e^{-at} u(-t)+ e^{bt} u(t)$

**Solution:**

To determine the Region of Convergence (ROC) and whether a signal is Laplace transformable, we evaluate the bilateral Laplace transform integral: $X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt$, where $s = \sigma + j\omega$. The ROC is the range of values for $\sigma$ (the real part of $s$) for which this integral converges to a finite value.

**(i) $x_1(t) = e^{at} u(-t)$**
This is a left-sided (anticausal) signal because $u(-t)$ is 1 for $t < 0$ and 0 for $t > 0$.
The Laplace transform is:
$$X_1(s) = \int_{-\infty}^{0} e^{at} e^{-st} dt = \int_{-\infty}^{0} e^{(a-s)t} dt$$
Evaluating the integral:
$$X_1(s) = \left[ \frac{e^{(a-s)t}}{a-s} \right]_{-\infty}^0 = \frac{1}{a-s} \left( e^0 - \lim_{t \to -\infty} e^{(a-s)t} \right)$$
For the integral to converge, the limit term must go to zero. Let $s = \sigma + j\omega$. The magnitude of the limit term depends on $e^{(a-\sigma)t}$.
As $t \to -\infty$, $e^{(a-\sigma)t} \to 0$ only if the exponent multiplier $(a-\sigma)$ is positive.
Therefore, we require $a - \sigma > 0 \implies \sigma < a$.
If this condition holds, $X_1(s) = \frac{1}{a-s} (1 - 0) = \frac{-1}{s-a}$.

*   **ROC Sketch:** The ROC is the region in the s-plane to the left of the vertical line $\sigma = a$. (Imagine a Cartesian plane where the x-axis is $Re\{s\}$ and the y-axis is $Im\{s\}$. Draw a vertical dashed line at $Re\{s\} = a$. Shade everything to the left of this line).
*   **Is it Laplace Transformable?** Yes, because a valid Region of Convergence ($Re\{s\} < a$) exists.

**(ii) $x_2(t) = e^{-at} u(-t) + e^{bt} u(t)$**
This is a two-sided signal, consisting of a left-sided component and a right-sided component. By linearity, the Laplace transform $X_2(s)$ is the sum of the transforms of its components, provided their ROCs overlap. Let $x_2(t) = x_L(t) + x_R(t)$.

1.  **Left-sided component:** $x_L(t) = e^{-at} u(-t)$
    Using the result from part (i) and substituting $-a$ for $a$, the transform is $X_L(s) = \frac{-1}{s - (-a)} = \frac{-1}{s+a}$.
    The ROC for this component is $Re\{s\} < -a$.

2.  **Right-sided component:** $x_R(t) = e^{bt} u(t)$
    This is a standard causal exponential signal. Its unilateral (and bilateral) Laplace transform is:
    $$X_R(s) = \int_{0}^{\infty} e^{bt} e^{-st} dt = \int_{0}^{\infty} e^{-(s-b)t} dt = \left[ \frac{-e^{-(s-b)t}}{s-b} \right]_{0}^{\infty}$$
    For convergence at $t \to \infty$, we require $Re\{s-b\} > 0 \implies Re\{s\} > b$.
    Under this condition, $X_R(s) = 0 - (\frac{-1}{s-b}) = \frac{1}{s-b}$.
    The ROC for this component is $Re\{s\} > b$.

The overall ROC for $X_2(s)$ is the intersection of the individual ROCs:
$$\text{Overall ROC} = (Re\{s\} < -a) \cap (Re\{s\} > b)$$
This intersection represents a vertical strip in the s-plane between $\sigma = b$ and $\sigma = -a$.
*   **Condition for Existence:** This strip only exists if $b < -a$.
*   **ROC Sketch:** If $b < -a$, draw two vertical dashed lines at $\sigma = b$ and $\sigma = -a$. The ROC is the shaded region between these two lines. If $b \ge -a$, there is no overlapping region.
*   **Is it Laplace Transformable?** It depends on the constants.
    *   If **$b < -a$**, the ROC exists (a strip), and the signal **is** Laplace transformable.
    *   If **$b \ge -a$**, the ROC is empty, and the signal is **not** Laplace transformable.

Location pg 448 In pdf

***

---

### **15. Pg 35, CT-3 Q1: Find the Laplace transform of (i) $e^{3t} u(-t)$ and (ii) $e^{-3t} u(t) + e^{3t} u(-t)$. Also sketch ROC of them.**

**General Definition:** The bilateral Laplace transform is defined as $X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt$.

**Solution:**

**(i) Find Laplace transform of $x_1(t) = e^{3t} u(-t)$**
*   The term $u(-t)$ restricts the signal to negative time ($-\infty < t \le 0$). This makes it a left-sided signal.
*   Apply the definition:
    $X_1(s) = \int_{-\infty}^{\infty} e^{3t} u(-t) e^{-st} dt = \int_{-\infty}^{0} e^{3t} e^{-st} dt = \int_{-\infty}^{0} e^{(3-s)t} dt$
*   Evaluate the integral:
    $X_1(s) = \left[ \frac{e^{(3-s)t}}{3-s} \right]_{-\infty}^{0} = \frac{1}{3-s} \left[ e^0 - \lim_{t \to -\infty} e^{(3-s)t} \right]$
    $X_1(s) = \frac{1}{3-s} \left[ 1 - \lim_{t \to -\infty} e^{(3-s)t} \right]$
*   **Determine ROC (Region of Convergence):** For the integral to converge (not blow up to infinity), the term $e^{(3-s)t}$ must decay to zero as $t \to -\infty$. 
    Let $s = \sigma + j\omega$. The exponent is $(3 - (\sigma + j\omega))t = (3 - \sigma)t - j\omega t$.
    The magnitude is determined by the real part: $e^{(3-\sigma)t}$. 
    As $t \to -\infty$, for $e^{(3-\sigma)t}$ to approach $0$, the coefficient $(3-\sigma)$ must be positive.
    $3 - \sigma > 0 \implies \sigma < 3$.
    Therefore, the integral converges if $Re\{s\} < 3$.
*   Under this condition, the limit evaluates to $0$:
    $X_1(s) = \frac{1}{3-s} = \mathbf{\frac{-1}{s-3}}$, with **ROC: $Re\{s\} < 3$**.

**(ii) Find Laplace transform of $x_2(t) = e^{-3t} u(t) + e^{3t} u(-t)$**
*   This signal is the sum of a right-sided signal $x_{2R}(t) = e^{-3t} u(t)$ and the left-sided signal from part (i), $x_{2L}(t) = e^{3t} u(-t)$.
*   We can use linearity and find the transform of each part separately.
*   **Part 1 (Right-sided):**
    $\mathcal{L}\{e^{-3t} u(t)\} = \int_{0}^{\infty} e^{-3t} e^{-st} dt = \int_{0}^{\infty} e^{-(s+3)t} dt = \left[ \frac{e^{-(s+3)t}}{-(s+3)} \right]_{0}^{\infty}$
    For convergence as $t \to \infty$, the real part of $(s+3)$ must be positive: $Re\{s+3\} > 0 \implies \sigma > -3$.
    Evaluating the integral: $\frac{0 - 1}{-(s+3)} = \frac{1}{s+3}$ with ROC: $Re\{s\} > -3$.
*   **Part 2 (Left-sided):** From (i), $\mathcal{L}\{e^{3t} u(-t)\} = \frac{-1}{s-3}$ with ROC: $Re\{s\} < 3$.
*   **Combine:**
    $X_2(s) = \frac{1}{s+3} - \frac{1}{s-3} = \frac{(s-3) - (s+3)}{(s+3)(s-3)} = \mathbf{\frac{-6}{s^2 - 9}}$
*   **Determine total ROC:** The overall ROC is the intersection of the ROCs of the individual components.
    ROC $= \{Re\{s\} > -3\} \cap \{Re\{s\} < 3\} = \mathbf{-3 < Re\{s\} < 3}$. This forms a vertical strip in the s-plane.

**Sketching the ROCs:**
*   **For (i):** Draw the complex s-plane with axes $\sigma$ (real) and $j\omega$ (imaginary). Draw a dashed vertical line at $\sigma = 3$. Shade the entire region to the **left** of this line. Label the pole at $s = 3$ with an 'x'.
*   **For (ii):** Draw the s-plane. Draw dashed vertical lines at $\sigma = -3$ and $\sigma = 3$. Shade the vertical strip **between** these two lines. Label poles at $s = -3$ and $s = 3$ with 'x' marks.

*Reference: Class Notes Pg 58-61 (Laplace Transform and ROC).*

---

### **16. Pg 36, CT-3 Q1: Using the differentiation property, find the Laplace transform of the following function. ![[Pasted image 20260712005827.png]]**

**Figure Description:**
The figure shows a rectangular pulse $f(t)$ centered at the origin.
*   Amplitude is $A$.
*   It spans from $t = -T/2$ to $t = T/2$.
Mathematically, this can be written using unit step functions:
$f(t) = A [u(t + T/2) - u(t - T/2)]$

**Solution:**

The differentiation property of the Laplace Transform states:
$\mathcal{L}\left\{\frac{df(t)}{dt}\right\} = s F(s) - f(0^-)$
Assuming initial conditions are zero (or dealing with a signal that is defined over all time where we use the bilateral transform and the boundary term vanishes), the property simplifies to $\mathcal{L}\{f'(t)\} = s F(s)$.
Therefore, we can find $F(s)$ by taking the derivative of $f(t)$, finding its transform, and then dividing by $s$.
$F(s) = \frac{1}{s} \mathcal{L}\{f'(t)\}$

**Step 1: Differentiate the signal $f(t)$**
The function $f(t) = A [u(t + T/2) - u(t - T/2)]$ consists of flat sections and abrupt jumps. The derivative of a constant is 0, and the derivative of a unit step jump is an impulse function $\delta(t)$ weighted by the size of the jump.
*   At $t = -T/2$, the signal jumps from $0$ to $A$. This produces a positive impulse: $A \delta(t + T/2)$.
*   At $t = T/2$, the signal jumps from $A$ down to $0$. This produces a negative impulse: $-A \delta(t - T/2)$.
So, the derivative is:
$f'(t) = A \delta(t + T/2) - A \delta(t - T/2)$

**Step 2: Find the Laplace transform of the derivative**
The Laplace transform of a shifted impulse is $\mathcal{L}\{\delta(t - t_0)\} = e^{-st_0}$.
Applying this to our derivative equation:
$\mathcal{L}\{f'(t)\} = \mathcal{L}\{A \delta(t + T/2) - A \delta(t - T/2)\}$
$\mathcal{L}\{f'(t)\} = A e^{s(T/2)} - A e^{-s(T/2)}$
$\mathcal{L}\{f'(t)\} = A \left( e^{sT/2} - e^{-sT/2} \right)$

**Step 3: Apply the differentiation property to solve for $F(s)$**
We know $s F(s) = \mathcal{L}\{f'(t)\}$.
$s F(s) = A \left( e^{sT/2} - e^{-sT/2} \right)$
$F(s) = \frac{A}{s} \left( e^{sT/2} - e^{-sT/2} \right)$

*(Optional: While this form is correct, it can be mathematically manipulated to look like a hyperbolic sine function. Recall $\sinh(x) = \frac{e^x - e^{-x}}{2}$, so $e^x - e^{-x} = 2\sinh(x)$. Let $x = sT/2$. Then $F(s) = \frac{2A}{s} \sinh(\frac{sT}{2})$.)*

The final expression is:
$\mathbf{F(s) = \frac{A}{s} \left( e^{sT/2} - e^{-sT/2} \right)}$

*Reference: Sadiku Chapter 15, Section 15.3 (Properties of the Laplace Transform) / Class Notes Pg 103, 104.*

Here are the detailed solutions for questions 17 through 20 from the provided list.

---

### **22. Pg 42, CT-3 Q2: Sketch the Region of Convergence (ROC) in the complex s-plane of the following signals.**

**Solution:**

The bilateral Laplace transform is defined as $F(s) = \int_{-\infty}^{\infty} f(t) e^{-st} dt$, where $s = \sigma + j\omega$. The ROC is the range of real values $\sigma$ for which this integral converges.

**(i) $f(t) = e^{-at}u(-t) + e^{bt}u(t)$**
We analyze the left-sided and right-sided portions separately.
*   **Right-sided portion:** $e^{bt}u(t)$. 
    $\mathcal{L}\{e^{bt}u(t)\} = \int_{0}^{\infty} e^{bt} e^{-st} dt = \int_{0}^{\infty} e^{-(s-b)t} dt = \frac{1}{s-b}$.
    For convergence at $\infty$, the real part of $(s-b)$ must be positive: $Re\{s\} > b \implies \mathbf{\sigma > b}$. (Pole at $s=b$)
*   **Left-sided portion:** $e^{-at}u(-t)$.
    $\mathcal{L}\{e^{-at}u(-t)\} = \int_{-\infty}^{0} e^{-at} e^{-st} dt = \int_{-\infty}^{0} e^{-(s+a)t} dt = \frac{-1}{s+a}$.
    For convergence at $-\infty$, the real part of $(s+a)$ must be negative: $-Re\{s+a\} > 0 \implies \mathbf{\sigma < -a}$. (Pole at $s=-a$)
*   **Total ROC:** The intersection of the two conditions: $\sigma > b$ AND $\sigma < -a$. 
    This means the ROC is the strip: $\mathbf{b < \sigma < -a}$. 
    *(Note: This transform only exists if $b < -a$. Assuming this is true for the sketch).*
*   **Sketch Description:** Draw the complex s-plane (horizontal $\sigma$-axis, vertical $j\omega$-axis). Mark a pole ($\times$) at $\sigma = b$ and a pole ($\times$) at $\sigma = -a$ (where $b$ is to the left of $-a$). Draw vertical dashed lines through both poles. **Shade the region between the two vertical lines**.

**(ii) $f(t) = e^{at}u(t) + e^{bt}u(-t)$, with $b > a$.**
*   **Right-sided portion:** $e^{at}u(t)$.
    $\mathcal{L}\{e^{at}u(t)\} = \frac{1}{s-a}$.
    Condition for convergence: $Re\{s-a\} > 0 \implies \mathbf{\sigma > a}$. (Pole at $s=a$)
*   **Left-sided portion:** $e^{bt}u(-t)$.
    $\mathcal{L}\{e^{bt}u(-t)\} = \frac{-1}{s-b}$.
    Condition for convergence: $-Re\{s-b\} > 0 \implies \mathbf{\sigma < b}$. (Pole at $s=b$)
*   **Total ROC:** The intersection of the two conditions: $\sigma > a$ AND $\sigma < b$.
    This implies $\mathbf{a < \sigma < b}$. Because the problem states $b > a$, this intersection is valid and forms a bounded vertical strip.
*   **Sketch Description:** Draw the complex s-plane. Mark a pole ($\times$) at $\sigma = a$ and a pole ($\times$) at $\sigma = b$. Draw vertical dashed lines through both poles. **Shade the rectangular strip lying strictly between the line $\sigma = a$ and the line $\sigma = b$**.

# 5. Fourier Transform

### (c) Given that the Fourier Transform of $x(t)$ is $X(\omega)$, the differentiation property of the Fourier transform states that: $\frac{dx(t)}{dt} \Leftrightarrow j\omega X(\omega)$. The signum function, $sgn(t)$ is defined as: $sgn(t) = \begin{cases} 1 & ; \quad t > 0 \\ -1 & ; \quad t < 0 \end{cases}$
### (ii) By applying the differentiation property, or otherwise, show that the Fourier transform of $sgn(t)$ is: $sgn(t) \Leftrightarrow \frac{2}{j\omega}$

**Detailed Answer:**

**(i) Expressing $sgn(t)$ in terms of the unit step function:**
The unit step function $u(t)$ is defined as:
$$u(t) = \begin{cases} 1 & \text{for } t > 0 \\ 0 & \text{for } t < 0 \end{cases}$$

We want to construct the signum function which is $1$ for $t > 0$ and $-1$ for $t < 0$.
If we multiply the unit step function by 2, we get $2u(t)$, which equals $2$ for positive time and $0$ for negative time.
To shift these values down to the desired levels of $1$ and $-1$, we simply subtract $1$ from the entire function. Let's verify:
*   For $t > 0$: $2u(t) - 1 = 2(1) - 1 = 1$
*   For $t < 0$: $2u(t) - 1 = 2(0) - 1 = -1$

This perfectly matches the definition of the signum function. Therefore:
**$$sgn(t) = 2u(t) - 1$$**

**(ii) Deriving the Fourier transform of $sgn(t)$:**
Let $x(t) = sgn(t) = 2u(t) - 1$.
First, we take the derivative of $x(t)$ with respect to time. The derivative of a constant is 0, and the derivative of the unit step function $u(t)$ is the Dirac delta function $\delta(t)$.
$$\frac{dx(t)}{dt} = \frac{d}{dt}[2u(t) - 1] = 2\frac{du(t)}{dt} - \frac{d(1)}{dt}$$
$$\frac{dx(t)}{dt} = 2\delta(t)$$

Now, we take the Fourier transform of both sides of this equation. Let $\mathcal{F}\{x(t)\} = X(\omega)$.
Applying the given differentiation property $\mathcal{F}\left\{ \frac{dx(t)}{dt} \right\} = j\omega X(\omega)$ to the left side, and the known transform pair $\mathcal{F}\{\delta(t)\} = 1$ to the right side:
$$\mathcal{F}\left\{ \frac{dx(t)}{dt} \right\} = \mathcal{F}\{2\delta(t)\}$$
$$j\omega X(\omega) = 2(1)$$
$$j\omega X(\omega) = 2$$

Finally, solving for $X(\omega)$ yields the desired Fourier transform:
**$$X(\omega) = \frac{2}{j\omega}$$**
Therefore, **$sgn(t) \Leftrightarrow \frac{2}{j\omega}$**.

always mention ans related location pg no. In pdf , at the end of every soln Example 7.10 Fourier Transform of the Sign Function, pg. 698

***

### (b) Determine the Fourier transform of $i_o(t)$ in the following network. (figure involved.)
![[Pasted image 20260628170652.png]]
**Detailed Answer:**

To find the Fourier transform of the output current $i_o(t)$, it is most efficient to analyze the circuit in the Laplace ($s$) domain to find the transfer function or the $s$-domain current $I_o(s)$, and then substitute $s = j\omega$ to get the frequency domain representation $I_o(\omega)$.

*(Note: In the provided image, the capacitor value is slightly blurry. It appears to be $\frac{1}{4}$ F. We will proceed with $C = 0.25$ F, as textbook problems rarely use milli-Farads combined with small integer ohms and Henrys, which would lead to unnecessarily messy calculations.)*

**1. Transform the circuit components to the $s$-domain:**
*   **Voltage source 1 (left):** $v_1(t) = e^{-t}u(t)$. From standard transform tables, $V_1(s) = \frac{1}{s+1}$.
*   **Resistor:** $R = 2\ \Omega \implies Z_R(s) = 2$.
*   **Capacitor:** $C = \frac{1}{4}\text{ F} \implies Z_C(s) = \frac{1}{sC} = \frac{1}{s(1/4)} = \frac{4}{s}$.
*   **Voltage source 2 (middle):** $v_2(t) = 3\delta(t)$. From standard transform tables, $V_2(s) = 3$.
*   **Inductor:** $L = 2\text{ H} \implies Z_L(s) = sL = 2s$.
*   The target variable is the current through the inductor, $I_o(s)$.

**2. Formulate the Nodal Equation:**
Let's use Nodal Analysis. Define the bottom wire as the reference node (Ground, $0\text{V}$). Let the top middle node (where the resistor, capacitor branch, and inductor meet) be $V(s)$.

The current $I_o(s)$ we want to find flows from node $V(s)$ to ground through the inductor, so:
$I_o(s) = \frac{V(s)}{Z_L(s)} = \frac{V(s)}{2s}$

Now, apply Kirchhoff's Current Law (KCL) at node $V(s)$. The sum of currents leaving the node equals zero:
$$\frac{V(s) - V_1(s)}{Z_R(s)} + \frac{V(s) - V_2(s)}{Z_C(s)} + \frac{V(s)}{Z_L(s)} = 0$$
Substitute the component values:
$$\frac{V(s) - \frac{1}{s+1}}{2} + \frac{V(s) - 3}{4/s} + \frac{V(s)}{2s} = 0$$

**3. Solve for V(s):**
Multiply the entire equation by a common denominator, such as $4s$, to clear the fractions:
$$2s\left(V(s) - \frac{1}{s+1}\right) + s \cdot s \cdot (V(s) - 3) + 2V(s) = 0$$
$$2sV(s) - \frac{2s}{s+1} + s^2V(s) - 3s^2 + 2V(s) = 0$$
Group the $V(s)$ terms together:
$$V(s)[s^2 + 2s + 2] = \frac{2s}{s+1} + 3s^2$$
Find a common denominator for the right side:
$$V(s)[s^2 + 2s + 2] = \frac{2s + 3s^2(s+1)}{s+1}$$
$$V(s)[s^2 + 2s + 2] = \frac{3s^3 + 3s^2 + 2s}{s+1}$$
Solve for $V(s)$:
$$V(s) = \frac{3s^3 + 3s^2 + 2s}{(s+1)(s^2 + 2s + 2)} = \frac{s(3s^2 + 3s + 2)}{(s+1)(s^2 + 2s + 2)}$$

**4. Determine $I_o(s)$:**
Substitute the expression for $V(s)$ back into our equation for $I_o(s)$:
$$I_o(s) = \frac{V(s)}{2s} = \frac{\frac{s(3s^2 + 3s + 2)}{(s+1)(s^2 + 2s + 2)}}{2s}$$
The '$s$' terms in the numerator and denominator cancel out cleanly:
$$I_o(s) = \frac{3s^2 + 3s + 2}{2(s+1)(s^2 + 2s + 2)}$$

**5. Convert to Fourier Transform $I_o(\omega)$:**
To obtain the Fourier transform, we substitute $s = j\omega$ into the Laplace domain expression:
$$I_o(\omega) = \left. I_o(s) \right|_{s=j\omega} = \frac{3(j\omega)^2 + 3(j\omega) + 2}{2(j\omega+1)((j\omega)^2 + 2j\omega + 2)}$$
Simplify using the fact that $j^2 = -1$:
$$I_o(\omega) = \frac{-3\omega^2 + j3\omega + 2}{2(1+j\omega)(-\omega^2 + j2\omega + 2)}$$
Rearranging the real and imaginary parts in the numerator and denominator gives the final result:
**$$I_o(\omega) = \frac{(2 - 3\omega^2) + j3\omega}{2(1 + j\omega)((2 - \omega^2) + j2\omega)}$$**

always mention ans related location pg no. In pdf , at the end of every soln 4.4 Analysis of Electrical Networks: The Transformed Network, pg. 373-375

### Q.4 (c) Using differentiation property, find the Fourier transform of the following function. Figure involved.
![[Pasted image 20260626191754.png]]
**Solution:**

Let the given function be $f(t)$. From the provided graph, $f(t)$ is a trapezoidal pulse defined as:
*   $f(t) = 0$ for $t < -2$
*   Ramps up from $0$ to $1$ between $t = -2$ and $t = -1$. The slope is $\frac{1 - 0}{-1 - (-2)} = 1$.
*   Constant at $1$ between $t = -1$ and $t = 1$.
*   Ramps down from $1$ to $0$ between $t = 1$ and $t = 2$. The slope is $\frac{0 - 1}{2 - 1} = -1$.
*   $f(t) = 0$ for $t > 2$.

The time-differentiation property of the Fourier transform states that if $x(t) \iff X(\omega)$, then:
$$\frac{d^n x(t)}{dt^n} \iff (j\omega)^n X(\omega)$$

**Step 1: Find the first derivative, $f'(t)$.**
Taking the derivative of the piecewise linear function $f(t)$ results in a sequence of rectangular pulses corresponding to the slopes:
*   Between $-2$ and $-1$, the slope is $1$. This forms a rectangular pulse of height $1$: $[u(t+2) - u(t+1)]$.
*   Between $-1$ and $1$, the slope is $0$.
*   Between $1$ and $2$, the slope is $-1$. This forms a rectangular pulse of height $-1$: $-[u(t-1) - u(t-2)]$.
So, $f'(t) = [u(t+2) - u(t+1)] - [u(t-1) - u(t-2)]$.

**Step 2: Find the second derivative, $f''(t)$.**
Taking the derivative of $f'(t)$ (which consists of step functions) yields a series of impulses at the points of discontinuity. The strength of each impulse is equal to the amount of the jump.
*   At $t=-2$, $f'(t)$ jumps from $0$ to $1$ $\rightarrow \delta(t+2)$
*   At $t=-1$, $f'(t)$ jumps from $1$ to $0$ $\rightarrow -\delta(t+1)$
*   At $t=1$, $f'(t)$ jumps from $0$ to $-1$ $\rightarrow -\delta(t-1)$
*   At $t=2$, $f'(t)$ jumps from $-1$ to $0$ $\rightarrow \delta(t-2)$
So, $f''(t) = \delta(t+2) - \delta(t+1) - \delta(t-1) + \delta(t-2)$.

**Step 3: Apply the Fourier Transform to $f''(t)$.**
Using the linearity property and the time-shifting property ($\delta(t-t_0) \iff e^{-j\omega t_0}$), we transform $f''(t)$:
$$\mathcal{F}\{f''(t)\} = e^{j2\omega} - e^{j\omega} - e^{-j\omega} + e^{-j2\omega}$$
Group the terms with matching exponents to form cosine functions, using Euler's formula $2\cos(\theta) = e^{j\theta} + e^{-j\theta}$:
$$\mathcal{F}\{f''(t)\} = (e^{j2\omega} + e^{-j2\omega}) - (e^{j\omega} + e^{-j\omega})$$
$$\mathcal{F}\{f''(t)\} = 2\cos(2\omega) - 2\cos(\omega)$$

**Step 4: Use the differentiation property to find $F(\omega)$.**
We know that $\mathcal{F}\{f''(t)\} = (j\omega)^2 F(\omega) = -\omega^2 F(\omega)$.
Equating the two expressions for the transform of the second derivative:
$$-\omega^2 F(\omega) = 2\cos(2\omega) - 2\cos(\omega)$$
Solving for $F(\omega)$:
$$F(\omega) = \frac{2\cos(\omega) - 2\cos(2\omega)}{\omega^2}$$

Location pg 718 In pdf

***

### Q.6. (b) Why a time limited signal is band unlimited in frequency domain? Explain

**Detailed Answer:**

A fundamental principle in signal processing, rooted in the properties of the Fourier Transform, dictates that a signal cannot be both strictly time-limited and strictly band-limited simultaneously. 

**Explanation:**
1.  **Time-Limited Signal:** A time-limited signal $x(t)$ is defined as having a non-zero value only within a finite time interval (e.g., $t_1 \le t \le t_2$) and being exactly zero everywhere outside this interval. Examples include a simple rectangular pulse or a short burst of sound.
2.  **Fourier Synthesis:** The Fourier Transform represents any signal as an infinite sum (integral) of everlasting complex exponentials ($e^{j\omega t}$) or sinusoids extending from $t = -\infty$ to $t = \infty$. 
3.  **The Conflict:** To synthesize a signal that is exactly zero outside a specific time window, an infinite number of these everlasting frequency components must be combined such that they perfectly destructively interfere (cancel each other out exactly to zero) everywhere outside the window, while constructively interfering to form the signal inside the window.
4.  **Band-Unlimited Consequence:** The abrupt changes required to start and stop a signal perfectly in the time domain (even if the signal looks smooth inside the window, the sudden transition to absolute zero requires infinite resolution) act like sharp edges. To represent such sharp features and exact cancellations, the Fourier transform requires frequency components that extend out to infinity. 
5.  **Mathematical Perspective (Paley-Wiener Criterion context):** If a signal were band-limited, its spectrum $X(\omega)$ would be zero outside a certain frequency range $[-B, B]$. The inverse Fourier transform of a function with finite support results in an analytic function in the time domain. An analytic function cannot be identically zero over an interval without being zero everywhere. Therefore, a strictly band-limited signal must extend infinitely in time. Conversely, if a signal is strictly time-limited, its spectrum cannot be zero over any continuous band of frequencies, meaning its spectrum must extend to infinity (band-unlimited).

In practical terms, whenever we truncate a signal in time (applying a window), we cause its frequency spectrum to spread out (spectral leakage), ensuring it contains high-frequency components that theoretically stretch to infinity.

always mention ans related location pg no. In pdf , at the end of every soln 8.2-1 Practical Difficulties in Signal Reconstruction (The Treachery of Aliasing), pg. 788-789

***

### (b) Find and draw the Fourier transform of the following sine-wave pulse. (figure involved.)
![[Pasted image 20260628100321.png]]
**Detailed Answer:**

**1. Define the Signal Mathematically:**
The figure displays a single full cycle of a sine wave.
*   It starts at $t = 0$ and ends at $t = 2$.
*   The period of this fundamental sine wave is $T = 2$.
*   The radian frequency is $\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{2} = \pi$ rad/s.
*   The amplitude is 1.

The signal can be expressed as a continuous sine wave multiplied by a rectangular gate pulse that restricts it to the interval $t=0$ to $t=2$.
$$f(t) = \sin(\pi t) [u(t) - u(t-2)]$$
Alternatively, it can be viewed as a sine wave multiplied by a rectangular pulse of width $\tau = 2$ centered at $t = 1$:
$$f(t) = \sin(\pi t) \cdot \text{rect}\left(\frac{t-1}{2}\right)$$

**2. Calculate the Fourier Transform:**
We can find the Fourier transform using the properties of the transform, specifically the modulation (frequency shifting) property and the time-shifting property.

*   **Step A: Transform of the rectangular pulse.**
    Let $g(t) = \text{rect}\left(\frac{t}{2}\right)$. This is a pulse of width $\tau=2$ centered at zero.
    Its Fourier transform is $G(\omega) = \tau \text{sinc}\left(\frac{\omega\tau}{2}\right) = 2\text{sinc}\left(\frac{2\omega}{2}\right) = 2\text{sinc}(\omega)$.
    *(Note: Using the definition $\text{sinc}(x) = \frac{\sin x}{x}$)*

*   **Step B: Apply time-shifting.**
    Our actual gating pulse is shifted to the right by 1 unit: $g(t-1) = \text{rect}\left(\frac{t-1}{2}\right)$.
    Using the time-shifting property $\mathcal{F}\{x(t-t_0)\} = X(\omega)e^{-j\omega t_0}$:
    $\mathcal{F}\left\{\text{rect}\left(\frac{t-1}{2}\right)\right\} = 2\text{sinc}(\omega)e^{-j\omega}$

*   **Step C: Apply modulation property.**
    The signal is $f(t) = \sin(\pi t) \cdot \text{rect}\left(\frac{t-1}{2}\right)$.
    The modulation property states: $\mathcal{F}\{x(t)\sin(\omega_0 t)\} = \frac{1}{2j} [X(\omega - \omega_0) - X(\omega + \omega_0)]$
    Here, $\omega_0 = \pi$ and $X(\omega)$ is the transform of our shifted rect pulse.
    $$F(\omega) = \frac{1}{2j} \left[ 2\text{sinc}(\omega - \pi)e^{-j(\omega - \pi)} - 2\text{sinc}(\omega + \pi)e^{-j(\omega + \pi)} \right]$$
    $$F(\omega) = \frac{1}{j} \left[ \text{sinc}(\omega - \pi)e^{-j\omega}e^{j\pi} - \text{sinc}(\omega + \pi)e^{-j\omega}e^{-j\pi} \right]$$
    Since $e^{j\pi} = e^{-j\pi} = -1$:
    $$F(\omega) = \frac{1}{j} \left[ -\text{sinc}(\omega - \pi)e^{-j\omega} + \text{sinc}(\omega + \pi)e^{-j\omega} \right]$$
    $$F(\omega) = j e^{-j\omega} \left[ \text{sinc}(\omega - \pi) - \text{sinc}(\omega + \pi) \right]$$

*   **Alternative Algebraic Form:**
    We can expand the sinc functions to find a single rational expression. Recall $\text{sinc}(x) = \frac{\sin x}{x}$.
    $F(\omega) = j e^{-j\omega} \left[ \frac{\sin(\omega - \pi)}{\omega - \pi} - \frac{\sin(\omega + \pi)}{\omega + \pi} \right]$
    Since $\sin(\omega - \pi) = -\sin(\omega)$ and $\sin(\omega + \pi) = -\sin(\omega)$:
    $F(\omega) = j e^{-j\omega} \left[ \frac{-\sin(\omega)}{\omega - \pi} - \frac{-\sin(\omega)}{\omega + \pi} \right] = j e^{-j\omega} \sin(\omega) \left[ \frac{-1}{\omega - \pi} + \frac{1}{\omega + \pi} \right]$
    $F(\omega) = j e^{-j\omega} \sin(\omega) \left[ \frac{-(\omega + \pi) + (\omega - \pi)}{(\omega - \pi)(\omega + \pi)} \right] = j e^{-j\omega} \sin(\omega) \left[ \frac{-2\pi}{\omega^2 - \pi^2} \right]$
    $F(\omega) = j e^{-j\omega} \left( \frac{e^{j\omega} - e^{-j\omega}}{2j} \right) \left[ \frac{2\pi}{\pi^2 - \omega^2} \right] = \frac{e^0 - e^{-j2\omega}}{2} \left[ \frac{2\pi}{\pi^2 - \omega^2} \right]$
    **$$F(\omega) = \frac{\pi(1 - e^{-j2\omega})}{\pi^2 - \omega^2}$$**

**3. Drawing the Fourier Transform:**
The most intuitive form for drawing is the superposition of sinc functions:
$|F(\omega)| = \left| \text{sinc}(\omega - \pi) - \text{sinc}(\omega + \pi) \right|$
*   The amplitude spectrum consists of the superposition of two sinc functions, one centered at $\omega = \pi$ and the other at $\omega = -\pi$.
*   Because they are subtracted, at $\omega=0$, $\text{sinc}(-\pi) - \text{sinc}(\pi) = 0 - 0 = 0$.
*   The main lobes peak near $\pm \pi$ and the side lobes decay as frequency increases.
*   The phase spectrum includes a linear phase shift component $-\omega$ due to the $e^{-j\omega}$ term, plus the phase jumps from the $j$ multiplier and the sign changes of the sinc functions.

always mention ans related location pg no. In pdf , at the end of every soln 7.2 Transforms of Some Useful Functions (Rectangular Pulse), pg. 691 and 7.3 Some Properties (Frequency Shifting), pg. 711

***

### (c) State and explain Parseval's theorem.

**Detailed Answer:**

**Statement of Parseval's Theorem:**
Parseval's theorem (specifically for the Fourier transform) establishes a fundamental relationship between the energy of a signal measured in the time domain and its energy measured in the frequency domain. 

For a continuous-time, finite-energy signal $x(t)$ with Fourier transform $X(\omega)$, Parseval's theorem states:
$$E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$
*(Note: If the frequency variable $f$ in Hertz is used instead of radian frequency $\omega$, where $\omega = 2\pi f$, the formula is $\int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df$)*

**Explanation:**
1.  **Time-Domain Energy:** The left side of the equation, $\int_{-\infty}^{\infty} |x(t)|^2 dt$, is the standard definition of the total energy $E_x$ of a signal $x(t)$. It is the area under the squared magnitude of the signal over all time.
2.  **Frequency-Domain Energy:** The right side of the equation states that you can calculate this exact same total energy by integrating the squared magnitude of the signal's Fourier transform, $|X(\omega)|^2$, over all frequencies (scaling by $\frac{1}{2\pi}$ when integrating with respect to $\omega$).
3.  **Energy Spectral Density:** This theorem implies that the quantity $|X(\omega)|^2$ represents the density of energy per unit bandwidth. Therefore, $|X(\omega)|^2$ is formally called the **energy spectral density** of the signal. It shows precisely how the signal's total energy is distributed across the frequency spectrum. 
4.  **Conservation of Energy:** Conceptually, Parseval's theorem is a statement of the conservation of energy. It mathematically guarantees that representing a signal in the frequency domain (via the Fourier transform) does not create or destroy energy; the total energy of the physical signal remains constant regardless of the domain in which it is analyzed.

always mention ans related location pg no. In pdf , at the end of every soln 7.6 Signal Energy, pg. 734

### Q.7. (a) Determine the Fourier transform of the function in the following figure. (figure involved.)
![[Pasted image 20260628100406.png]]
**Detailed Answer:**

To find the Fourier transform of the given signal $f(t)$, we can use the properties of the Fourier transform. The signal consists of two identical triangular pulses shifted in time.

**1. Define a basic pulse:**
Let's first define a basic triangular pulse $p(t)$ centered at the origin ($t=0$). 
Looking at the figure, each triangle has a base width of 2 (from -4 to -2, and from 2 to 4) and a peak amplitude of 2.
So, let $p(t)$ be a triangular pulse centered at $t=0$, with a width of 2 (from $t=-1$ to $t=1$) and a peak amplitude of 2.

We can find the Fourier transform of this basic pulse $P(\omega)$ by taking its second derivative, which results in three impulses. 
$p'(t)$ is a rectangular pulse of amplitude 2 from -1 to 0, and -2 from 0 to 1.
$p''(t) = 2\delta(t+1) - 4\delta(t) + 2\delta(t-1)$

Taking the Fourier transform of the second derivative:
$\mathcal{F}\{p''(t)\} = (j\omega)^2 P(\omega) = -\omega^2 P(\omega)$
$\mathcal{F}\{2\delta(t+1) - 4\delta(t) + 2\delta(t-1)\} = 2e^{j\omega} - 4 + 2e^{-j\omega}$
$= 2(e^{j\omega} + e^{-j\omega}) - 4 = 4\cos(\omega) - 4 = -4(1 - \cos(\omega))$
Using the half-angle identity $1 - \cos(\omega) = 2\sin^2(\omega/2)$:
$-\omega^2 P(\omega) = -8\sin^2(\omega/2)$
$P(\omega) = \frac{8\sin^2(\omega/2)}{\omega^2} = 2 \left( \frac{\sin(\omega/2)}{\omega/2} \right)^2 = 2\text{sinc}^2\left(\frac{\omega}{2}\right)$

*(Note: In the text, $\text{sinc}(x)$ is defined as $\frac{\sin x}{x}$.)*

**2. Express $f(t)$ in terms of $p(t)$:**
The given signal $f(t)$ consists of one such pulse shifted to the left by 3 units, and another shifted to the right by 3 units.
$f(t) = p(t+3) + p(t-3)$

**3. Apply the Time-Shifting Property:**
The time-shifting property states that if $x(t) \Longleftrightarrow X(\omega)$, then $x(t-t_0) \Longleftrightarrow X(\omega)e^{-j\omega t_0}$.
Applying this to our signal:
$\mathcal{F}\{f(t)\} = F(\omega) = \mathcal{F}\{p(t+3)\} + \mathcal{F}\{p(t-3)\}$
$F(\omega) = P(\omega)e^{j3\omega} + P(\omega)e^{-j3\omega}$
$F(\omega) = P(\omega) \left[ e^{j3\omega} + e^{-j3\omega} \right]$
$F(\omega) = P(\omega) [2\cos(3\omega)]$

**4. Final Expression:**
Substitute $P(\omega)$ back into the equation:
$F(\omega) = \left[ 2\text{sinc}^2\left(\frac{\omega}{2}\right) \right] [2\cos(3\omega)]$
$F(\omega) = 4\text{sinc}^2\left(\frac{\omega}{2}\right)\cos(3\omega)$

always mention ans related location pg no. In pdf , at the end of every soln 7.3 Some Properties of the Fourier Transform (Time-Shifting), pg. 707 and Example 7.17, pg. 718

***

### (c) Find the Fourier transform of the following functions: (i) $\delta(t)$, (ii) $e^{j\omega_0 t}$, (iii) $\text{sgn}(t)$

**Detailed Answer:**

**(i) Fourier Transform of $\delta(t)$:**
By definition of the Fourier transform:
$X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t} dt$
Substituting $x(t) = \delta(t)$:
$\mathcal{F}[\delta(t)] = \int_{-\infty}^{\infty} \delta(t)e^{-j\omega t} dt$
Using the sifting property of the impulse function, $\int_{-\infty}^{\infty} \phi(t)\delta(t-t_0) dt = \phi(t_0)$, we evaluate the integrand at $t=0$:
$\mathcal{F}[\delta(t)] = e^{-j\omega(0)} = e^0 = 1$
Therefore, **$\delta(t) \Longleftrightarrow 1$**.

**(ii) Fourier Transform of $e^{j\omega_0 t}$:**
This can be found easily by using the inverse Fourier transform formula and the sifting property of the delta function in the frequency domain. 
Consider a frequency domain impulse at $\omega = \omega_0$: $X(\omega) = 2\pi\delta(\omega - \omega_0)$.
Taking the inverse Fourier transform:
$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega)e^{j\omega t} d\omega$
$x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} 2\pi\delta(\omega - \omega_0)e^{j\omega t} d\omega$
$x(t) = \int_{-\infty}^{\infty} \delta(\omega - \omega_0)e^{j\omega t} d\omega$
By the sifting property, evaluate the integrand at $\omega = \omega_0$:
$x(t) = e^{j\omega_0 t}$
Therefore, by duality, **$e^{j\omega_0 t} \Longleftrightarrow 2\pi\delta(\omega - \omega_0)$**.

**(iii) Fourier Transform of $\text{sgn}(t)$:**
The signum function is defined as $\text{sgn}(t) = 1$ for $t > 0$ and $-1$ for $t < 0$.
It can be expressed using the unit step function $u(t)$:
$\text{sgn}(t) = 2u(t) - 1$
We use the known Fourier transforms of $u(t)$ and a constant $1$:
$\mathcal{F}[u(t)] = \pi\delta(\omega) + \frac{1}{j\omega}$
$\mathcal{F}[1] = 2\pi\delta(\omega)$
Using the linearity property:
$\mathcal{F}[\text{sgn}(t)] = \mathcal{F}[2u(t)] - \mathcal{F}[1]$
$\mathcal{F}[\text{sgn}(t)] = 2\left(\pi\delta(\omega) + \frac{1}{j\omega}\right) - 2\pi\delta(\omega)$
$\mathcal{F}[\text{sgn}(t)] = 2\pi\delta(\omega) + \frac{2}{j\omega} - 2\pi\delta(\omega) = \frac{2}{j\omega}$
Therefore, **$\text{sgn}(t) \Longleftrightarrow \frac{2}{j\omega}$**.

always mention ans related location pg no. In pdf , at the end of every soln Example 7.3, pg. 693; Example 7.5, pg. 694; Example 7.10, pg. 698

***

### (c) Why it is not possible to find the Fourier transform of ramp signal? State and explain Parseval's theorem.

**Detailed Answer:**

**Why the Fourier transform of a ramp signal does not exist:**
To find the Fourier transform $X(\omega)$ of a signal $x(t)$, the defining integral must converge:
$X(\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t} dt$
A sufficient condition for this integral to converge is given by the first Dirichlet condition, which states that the signal must be absolutely integrable:
$\int_{-\infty}^{\infty} |x(t)| dt < \infty$

A ramp signal is defined as $r(t) = t \cdot u(t)$. Let's check its absolute integrability:
$\int_{-\infty}^{\infty} |t \cdot u(t)| dt = \int_{0}^{\infty} t dt = \left[ \frac{t^2}{2} \right]_{0}^{\infty} = \infty$
Because the integral diverges to infinity, the ramp signal is not absolutely integrable. As $t \rightarrow \infty$, the amplitude of the ramp signal grows without bound. Consequently, the Fourier integral does not converge. Even when extending the Fourier transform to generalized functions (like we do for the unit step $u(t)$ which also technically violates strict absolute integrability), the ramp signal grows too fast (it is not a bounded signal), meaning its Fourier transform does not exist in the conventional or generalized sense.

**State and Explain Parseval's Theorem:**
*Statement:* Parseval's theorem relates the energy of a signal in the time domain to its energy in the frequency domain. For a Fourier-transformable signal $x(t)$ with Fourier transform $X(\omega)$, Parseval's theorem states:
$$E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(\omega)|^2 d\omega$$

*Explanation:* 
1.  The left side of the equation, $\int_{-\infty}^{\infty} |x(t)|^2 dt$, represents the total energy $E_x$ of the signal $x(t)$ calculated in the time domain.
2.  The right side of the equation indicates that the total energy can also be calculated in the frequency domain by integrating the squared magnitude of the Fourier transform, $|X(\omega)|^2$, over all frequencies (and scaling by $\frac{1}{2\pi}$ when using radian frequency $\omega$). 
3.  Because integrating $|X(\omega)|^2$ gives energy, the quantity $|X(\omega)|^2$ is known as the **energy spectral density** of the signal. It describes how the signal's total energy is distributed across different frequencies.
4.  Essentially, the theorem demonstrates the principle of conservation of energy: the total energy of a signal remains the same regardless of whether it is measured in the time domain or the frequency domain.

always mention ans related location pg no. In pdf , at the end of every soln 7.1 Aperiodic Signal Representation by the Fourier Integral (Existence of the Fourier Transform), pg. 685-686 and 7.6 Signal Energy, pg. 734

---

### 3. Pg 25, CT-4 Q2: Using differentiation property, find the Fourier transform of the following function. ![[Pasted image 20260712005508.png]]

**Figure Description:** The figure shows a rectangular pulse $f(t)$ centered at the origin. It has an amplitude of $A$ and spans from $t = -2$ to $t = 2$.
Mathematically, $f(t)$ can be represented using unit step functions:
$f(t) = A [u(t+2) - u(t-2)]$

**Solution:**

The time differentiation property of the Fourier Transform states that if $\mathcal{F}\{f(t)\} = F(\omega)$, then:
$\mathcal{F}\left\{\frac{df(t)}{dt}\right\} = j\omega F(\omega)$

**Step 1: Differentiate the given function $f(t)$**
Taking the derivative of the rectangular pulse $f(t) = A [u(t+2) - u(t-2)]$ yields two impulse functions (Dirac delta functions) located at the edges of the pulse.
$\frac{df(t)}{dt} = f'(t) = A \delta(t+2) - A \delta(t-2)$

**Step 2: Apply the Fourier Transform to the derivative**
We know the Fourier transform pair for a shifted impulse: $\mathcal{F}\{\delta(t - t_0)\} = e^{-j\omega t_0}$.
Applying this to our derivative:
$\mathcal{F}\{f'(t)\} = \mathcal{F}\{A \delta(t+2) - A \delta(t-2)\}$
$\mathcal{F}\{f'(t)\} = A e^{j\omega 2} - A e^{-j\omega 2}$

**Step 3: Simplify using Euler's identity**
Recall Euler's identity: $e^{j\theta} - e^{-j\theta} = 2j \sin(\theta)$.
Let $\theta = 2\omega$:
$\mathcal{F}\{f'(t)\} = A(2j \sin(2\omega)) = 2jA \sin(2\omega)$

**Step 4: Use the differentiation property to find $F(\omega)$**
Substitute the result from Step 3 into the differentiation property formula:
$j\omega F(\omega) = 2jA \sin(2\omega)$
$F(\omega) = \frac{2jA \sin(2\omega)}{j\omega}$
$\mathbf{F(\omega) = \frac{2A \sin(2\omega)}{\omega}}$

*(Optional: This can also be expressed using the sinc function where $\text{sinc}(x) = \frac{\sin(x)}{x}$. Multiply numerator and denominator by 2: $F(\omega) = 4A \frac{\sin(2\omega)}{2\omega} = 4A \text{sinc}(2\omega)$).*

*Reference: Sadiku Chapter 18, Section 18.3 (Properties of the Fourier Transform - Time Differentiation) / Class Notes Pg 103, 104.*

---

### **5. Pg 27, CT-3 Q3: Use the time-differentiation property to find the Fourier transform of the triangle pulse illustrated in Fig.** ![[Pasted image 20260712005539.png]]

**Figure Analysis:** 
The image shows a triangular pulse $x(t)$ centered at $t = 0$. It rises from $0$ at $t = -T/2$ to a peak amplitude of $1$ at $t = 0$, and then falls back to $0$ at $t = T/2$.
Let's define the mathematical equations for the slopes:
*   **Rising edge** (from $t = -T/2$ to $0$): Slope $m_1 = \frac{1 - 0}{0 - (-T/2)} = \frac{2}{T}$. 
    Equation: $x(t) = \frac{2}{T}t + 1$ 
*   **Falling edge** (from $t = 0$ to $T/2$): Slope $m_2 = \frac{0 - 1}{T/2 - 0} = -\frac{2}{T}$. 
    Equation: $x(t) = -\frac{2}{T}t + 1$

**Solution:**

**Step 1: Find the first derivative $x'(t)$**
Taking the derivative of $x(t)$ with respect to time yields the slopes of the segments.
*   For $-T/2 < t < 0$, $x'(t) = \frac{2}{T}$
*   For $0 < t < T/2$, $x'(t) = -\frac{2}{T}$
*   Everywhere else, $x'(t) = 0$
*(Sketch description of $x'(t)$: This results in two adjacent rectangular pulses. A positive rectangular pulse of amplitude $2/T$ from $t = -T/2$ to $0$, followed immediately by a negative rectangular pulse of amplitude $-2/T$ from $t = 0$ to $T/2$.)*

**Step 2: Find the second derivative $x''(t)$**
Taking the derivative of the rectangular pulses $x'(t)$ yields Dirac delta (impulse) functions at the points of discontinuity (where the signal jumps).
*   At $t = -T/2$, the signal jumps up from $0$ to $2/T$. This gives $\frac{2}{T}\delta(t + T/2)$.
*   At $t = 0$, the signal jumps down from $2/T$ to $-2/T$. The total change is $-\frac{4}{T}$. This gives $-\frac{4}{T}\delta(t)$.
*   At $t = T/2$, the signal jumps up from $-2/T$ to $0$. The total change is $+\frac{2}{T}$. This gives $\frac{2}{T}\delta(t - T/2)$.
So, the second derivative is:
$x''(t) = \frac{2}{T}\delta(t + \frac{T}{2}) - \frac{4}{T}\delta(t) + \frac{2}{T}\delta(t - \frac{T}{2})$

**Step 3: Apply the Fourier Transform to $x''(t)$**
Using the time-shifting property $\mathcal{F}\{\delta(t-t_0)\} = e^{-j\omega t_0}$:
$\mathcal{F}\{x''(t)\} = \frac{2}{T}e^{j\omega T/2} - \frac{4}{T}(1) + \frac{2}{T}e^{-j\omega T/2}$
Factor out $\frac{2}{T}$:
$\mathcal{F}\{x''(t)\} = \frac{2}{T}\left[ e^{j\omega T/2} + e^{-j\omega T/2} \right] - \frac{4}{T}$
Apply Euler's identity ($e^{j\theta} + e^{-j\theta} = 2\cos\theta$):
$\mathcal{F}\{x''(t)\} = \frac{2}{T} \left[ 2\cos\left(\frac{\omega T}{2}\right) \right] - \frac{4}{T} = \frac{4}{T}\cos\left(\frac{\omega T}{2}\right) - \frac{4}{T} = \frac{4}{T}\left[ \cos\left(\frac{\omega T}{2}\right) - 1 \right]$

**Step 4: Use the time-differentiation property to solve for $X(\omega)$**
The time differentiation property states $\mathcal{F}\{x''(t)\} = (j\omega)^2 X(\omega) = -\omega^2 X(\omega)$.
Equating the two expressions for $\mathcal{F}\{x''(t)\}$:
$-\omega^2 X(\omega) = \frac{4}{T} \left[ \cos\left(\frac{\omega T}{2}\right) - 1 \right]$
$X(\omega) = \frac{-4}{\omega^2 T} \left[ \cos\left(\frac{\omega T}{2}\right) - 1 \right] = \frac{4}{\omega^2 T} \left[ 1 - \cos\left(\frac{\omega T}{2}\right) \right]$

Using the half-angle trigonometric identity $1 - \cos(2\theta) = 2\sin^2(\theta)$:
$X(\omega) = \frac{4}{\omega^2 T} \left[ 2\sin^2\left(\frac{\omega T}{4}\right) \right]$
$\mathbf{X(\omega) = \frac{8}{\omega^2 T} \sin^2\left(\frac{\omega T}{4}\right)}$

# 6. Fourier Series & Spectrums

### (b) The square wave in the following waveform is applied to the following network. Find the Fourier series of $v_o(t)$.
![[Pasted image 20260628170311.png]]
**Detailed Answer:**

To find the Fourier series of the output voltage $v_o(t)$, we will follow a three-step process:
1.  Determine the Fourier series of the input square wave, $v_i(t)$.
2.  Determine the frequency response (transfer function) of the given op-amp circuit, $H(j\omega)$.
3.  Apply the system's frequency response to the input's Fourier series components to find the output Fourier series.

---

**Step 1: Fourier Series of the Input Signal $v_i(t)$**

From the provided graph, the input signal $v_i(t)$ is a periodic square wave with the following parameters:
*   **Amplitude:** $\pm 10\text{ V}$
*   **Fundamental Period ($T_0$):** The signal repeats every $2\text{ s}$, so $T_0 = 2\text{ s}$.
*   **Fundamental Angular Frequency ($\omega_0$):** $\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{2} = \pi \text{ rad/s}$.

Let's use the trigonometric Fourier series:
$$v_i(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$$

*   **Symmetry Analysis:**
    *   The signal has zero average value (equal area above and below the axis in one period), so the DC component **$a_0 = 0$**.
    *   The signal is an *odd function* ($v_i(-t) = -v_i(t)$). Therefore, it contains no cosine terms, meaning **$a_n = 0$** for all $n$.
    *   The signal has *half-wave symmetry* ($v_i(t - T_0/2) = -v_i(t)$). Therefore, it contains only *odd harmonics* ($n = 1, 3, 5, \dots$).

*   **Calculating $b_n$ for odd $n$:**
    $$b_n = \frac{4}{T_0} \int_{0}^{T_0/2} v_i(t) \sin(n\omega_0 t) dt$$
    For the interval $0 \le t \le 1$ ($T_0/2$), the value of $v_i(t)$ is $10$.
    $$b_n = \frac{4}{2} \int_{0}^{1} 10 \sin(n\pi t) dt = 20 \left[ \frac{-\cos(n\pi t)}{n\pi} \right]_{0}^{1}$$
    $$b_n = \frac{-20}{n\pi} [\cos(n\pi) - \cos(0)] = \frac{-20}{n\pi} [(-1)^n - 1]$$
    Since $n$ is odd, $(-1)^n = -1$:
    $$b_n = \frac{-20}{n\pi} [-1 - 1] = \frac{40}{n\pi}$$

So, the Fourier series for the input signal is:
$$v_i(t) = \sum_{n=1, 3, 5, \dots}^{\infty} \frac{40}{n\pi} \sin(n\pi t)$$

---

**Step 2: Frequency Response of the Circuit $H(j\omega)$**

The circuit shown is an ideal op-amp configured as an **inverting integrator**.
*   Input resistor $R = 10\text{ k}\Omega = 10^4\ \Omega$
*   Feedback capacitor $C = 40\text{ }\mu\text{F} = 40 \times 10^{-6}\text{ F}$

The transfer function in the $s$-domain for an inverting integrator is:
$$H(s) = \frac{V_o(s)}{V_i(s)} = -\frac{1}{sRC}$$
Calculating the time constant $RC$:
$$RC = (10^4\ \Omega) \times (40 \times 10^{-6}\text{ F}) = 400 \times 10^{-2} = 0.4\text{ s}$$
Substituting $RC$ and $s = j\omega$ to get the frequency response:
$$H(j\omega) = -\frac{1}{j\omega(0.4)} = \frac{-1}{0.4j\omega} \cdot \frac{j}{j} = \frac{-j}{-0.4\omega} = j\frac{1}{0.4\omega} = j\frac{2.5}{\omega}$$

For the $n$-th harmonic, where $\omega = n\omega_0 = n\pi$, the response is:
$$H(jn\pi) = j\frac{2.5}{n\pi}$$

---

**Step 3: Fourier Series of the Output Signal $v_o(t)$**

It is easier to apply the system response using the exponential Fourier series form.
The input trigonometric series can be converted to exponential form using $D_n = \frac{1}{2}(a_n - jb_n)$.
Since $a_n = 0$, $D_n = -j\frac{b_n}{2}$.
For the input $v_i(t)$, the exponential coefficients are:
$$D_{in, n} = -j\frac{1}{2}\left(\frac{40}{n\pi}\right) = -j\frac{20}{n\pi} \quad \text{for odd } n$$

The relationship between input and output Fourier coefficients is $D_{out, n} = D_{in, n} \cdot H(jn\omega_0)$.
Applying the transfer function to find the output coefficients:
$$D_{out, n} = \left(-j\frac{20}{n\pi}\right) \cdot H(jn\pi)$$
$$D_{out, n} = \left(-j\frac{20}{n\pi}\right) \cdot \left(j\frac{2.5}{n\pi}\right)$$
$$D_{out, n} = -j^2 \frac{20 \cdot 2.5}{(n\pi)^2}$$
Since $j^2 = -1$:
$$D_{out, n} = \frac{50}{(n\pi)^2} \quad \text{for odd } n$$

Now, we convert the output exponential coefficients back to trigonometric form:
$$a_{out, n} = 2 \cdot \text{Re}(D_{out, n}) = 2 \left( \frac{50}{(n\pi)^2} \right) = \frac{100}{n^2\pi^2}$$
$$b_{out, n} = -2 \cdot \text{Im}(D_{out, n}) = 0$$
The DC component $a_0$ is zero because the integral of a zero-mean square wave over a period is zero.

The final Fourier series for the output voltage $v_o(t)$ consists only of cosine terms (representing a triangle wave, which is expected when integrating a square wave):
**$$v_o(t) = \sum_{n=1, 3, 5, \dots}^{\infty} \frac{100}{n^2\pi^2} \cos(n\pi t)$$**

always mention ans related location pg no. In pdf , at the end of every soln 6.1 Periodic Signal Representation by Trigonometric Fourier Series, pg. 593-605 and 6.4 LTIC System Response to Periodic Inputs, pg. 637-639

Based on the images provided, here are the detailed solutions to the questions.

### (c) Find the exponential series of the following signal. Also draw the spectrum of that signal. (figure involved.)
![[Pasted image 20260628170514.png]]
**Detailed Answer:**

The figure shows a periodic signal $f(t)$ consisting of a sequence of rectangular pulses.
Let's define the parameters of the signal from the graph:
1.  **Amplitude ($A$):** The height of the pulses is $A = 10$.
2.  **Period ($T_0$):** The distance between the start of one pulse to the start of the next is from $t = -1$ to $t = 9$, or from $t = -11$ to $t = -1$. Therefore, the period is $T_0 = 10$.
3.  **Pulse Width ($\tau$):** The pulse is "on" from $t = -1$ to $t = 1$. The width is $\tau = 1 - (-1) = 2$.
4.  **Fundamental Angular Frequency ($\omega_0$):** $\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{10} = \frac{\pi}{5}$ rad/s.

The signal $f(t)$ is an even function since it is symmetric about the vertical axis ($f(t) = f(-t)$). This means its exponential Fourier series coefficients $D_n$ will be purely real.

The formula for the exponential Fourier series coefficients is:
$$D_n = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} f(t) e^{-jn\omega_0 t} dt$$

We can integrate over one full period, for example from $-5$ to $5$. Within this interval, the signal is non-zero only from $-1$ to $1$.
$$D_n = \frac{1}{10} \int_{-1}^{1} 10 \cdot e^{-jn\left(\frac{\pi}{5}\right)t} dt$$
$$D_n = \int_{-1}^{1} e^{-jn\frac{\pi}{5}t} dt$$

Let's evaluate the integral:
$$D_n = \left[ \frac{e^{-jn\frac{\pi}{5}t}}{-jn\frac{\pi}{5}} \right]_{-1}^{1}$$
$$D_n = \frac{e^{-jn\frac{\pi}{5}(1)} - e^{-jn\frac{\pi}{5}(-1)}}{-jn\frac{\pi}{5}}$$
$$D_n = \frac{e^{-jn\frac{\pi}{5}} - e^{jn\frac{\pi}{5}}}{-jn\frac{\pi}{5}}$$
Using Euler's formula, $\sin(x) = \frac{e^{jx} - e^{-jx}}{2j}$, which means $-2j \sin(x) = e^{-jx} - e^{jx}$:
$$D_n = \frac{-2j \sin\left(n\frac{\pi}{5}\right)}{-jn\frac{\pi}{5}} = \frac{2\sin\left(n\frac{\pi}{5}\right)}{n\frac{\pi}{5}}$$
To express this in a more standard form using the `sinc` function (where $\text{sinc}(x) = \frac{\sin(x)}{x}$ as defined in the textbook context):
Multiply numerator and denominator by $\frac{1}{5}$:
$$D_n = \frac{2}{5} \frac{\sin\left(n\frac{\pi}{5}\right)}{n\frac{\pi}{5}} = 0.4 \text{ sinc}\left(n\frac{\pi}{5}\right)$$

Therefore, the exponential Fourier series is:
$$f(t) = \sum_{n=-\infty}^{\infty} D_n e^{jn\omega_0 t}$$
**$$f(t) = \sum_{n=-\infty}^{\infty} \left[ 0.4 \text{ sinc}\left(n\frac{\pi}{5}\right) \right] e^{jn\frac{\pi}{5}t}$$**

**Drawing the Spectrum:**
The spectrum consists of lines at discrete frequencies $n\omega_0 = n\frac{\pi}{5}$ rad/s (or $nf_0 = \frac{n}{10}$ Hz).
The envelope of the spectrum is a scaled sinc function: $0.4 \text{ sinc}\left(\frac{\omega\tau}{2}\right) = 0.4 \text{ sinc}\left(\frac{\omega(2)}{2}\right) = 0.4 \text{ sinc}(\omega)$.
Since $D_n$ is real, we can plot it directly, noting that it can take negative values. A true amplitude spectrum $|D_n|$ would be strictly non-negative, with a corresponding phase spectrum having $\pi$ phase shifts where $D_n$ is negative.
Let's find some key values for $D_n$:
*   **DC component ($n=0$):** $D_0 = \frac{10 \times 2}{10} = 2$.
*   **Zero crossings:** The sinc envelope is zero when the argument is a multiple of $\pi$ (excluding $0$). So, $n\frac{\pi}{5} = k\pi \implies n = 5k$. The coefficients are zero for $n = \pm 5, \pm 10, \pm 15, \dots$
*   **First null bandwidth:** The first zero occurs at the 5th harmonic.

The spectrum plot is a series of discrete lines following a "sinc" shaped envelope. The central peak is at $D_0=2$. The lines are spaced apart by $\omega_0 = \pi/5$. Every 5th line is exactly zero.

always mention ans related location pg no. In pdf , at the end of every soln 6.3 Exponential Fourier Series, pg. 621-625 and Example 6.9, pg. 628-630

***

### (c) A full wave rectified signal having the following Fourier series expansion is used as the input of the circuit shown below. (figure involved.)
**$e(t) = \frac{2\times100}{\pi}(1 + \frac{2}{3}\cos 2\omega t - \frac{2}{15}\cos 4\omega t + \frac{2}{35}\cos 6\omega t \dots)$**
**where $\omega = 377$.**
**Find**
**(i) The Fourier series expression for the voltage $v_o(t)$ (first three terms only).**
**(ii) Average power delivered to the $1 \text{ k}\Omega$ resistor.**
![[Pasted image 20260628100513.png]]
**Detailed Answer:**

First, let's determine the transfer function $H(s) = \frac{V_o(s)}{E(s)}$ of the given circuit.
The circuit consists of a capacitor $C$ in series with a parallel combination of an inductor $L$ and a resistor $R$.
Given values: $C = 1 \mu\text{F} = 10^{-6}\text{ F}$, $L = 0.1\text{ H}$, $R = 1 \text{ k}\Omega = 1000\text{ }\Omega$.

The impedance of the parallel $L$ and $R$ combination ($Z_p$) is:
$$Z_p = \frac{(sL)(R)}{sL + R}$$
The total impedance of the circuit ($Z_{tot}$) is:
$$Z_{tot} = Z_C + Z_p = \frac{1}{sC} + \frac{sLR}{sL + R} = \frac{sL + R + s^2LRC}{sC(sL + R)}$$

Using the voltage divider rule, the output voltage across the resistor (and inductor) is:
$$V_o(s) = E(s) \frac{Z_p}{Z_{tot}} = E(s) \frac{\frac{sLR}{sL + R}}{\frac{s^2LRC + sL + R}{sC(sL + R)}} = E(s) \frac{s^2LRC}{s^2LRC + sL + R}$$

Divide numerator and denominator by $LRC$:
$$H(s) = \frac{V_o(s)}{E(s)} = \frac{s^2}{s^2 + \frac{1}{RC}s + \frac{1}{LC}}$$

Plugging in the component values:
$\frac{1}{RC} = \frac{1}{1000 \times 10^{-6}} = 1000$
$\frac{1}{LC} = \frac{1}{0.1 \times 10^{-6}} = 10^7$
$$H(s) = \frac{s^2}{s^2 + 1000s + 10^7}$$

To find the steady-state response for each frequency component, we evaluate $H(j\omega') = \frac{-\omega'^2}{(10^7 - \omega'^2) + j1000\omega'}$.

**Part (i): Fourier series expression for $v_o(t)$ (first three terms)**
The input signal $e(t)$ has the fundamental frequency $\omega = 377$ rad/s.
$e(t) = \frac{200}{\pi} + \frac{400}{3\pi}\cos(754 t) - \frac{400}{15\pi}\cos(1508 t) + \dots$

*   **Term 1 (DC component, $\omega' = 0$):**
    Input $E_{DC} = \frac{200}{\pi} \approx 63.66$ V.
    $H(j0) = \frac{0}{10^7} = 0$.
    Output $v_{o,dc}(t) = 0$ V.

*   **Term 2 (First AC component, $\omega' = 2\omega = 754$ rad/s):**
    Input $e_1(t) = \frac{400}{3\pi}\cos(754t) \approx 42.44 \cos(754t)$ V.
    Evaluate $H(j754)$: $\omega'^2 = 754^2 = 568516$.
    $H(j754) = \frac{-568516}{(10^7 - 568516) + j1000(754)} = \frac{-568516}{9431484 + j754000}$
    Magnitude: $|H(j754)| = \frac{568516}{\sqrt{9431484^2 + 754000^2}} \approx \frac{568516}{9461646} \approx 0.0601$
    Phase: $\angle H(j754) = 180^\circ - \arctan(\frac{754000}{9431484}) = 180^\circ - 4.57^\circ = 175.43^\circ$
    Output $v_{o1}(t) = 42.44 \times 0.0601 \cos(754t + 175.43^\circ) \approx 2.55 \cos(754t + 175.4^\circ)$ V.

*   **Term 3 (Second AC component, $\omega' = 4\omega = 1508$ rad/s):**
    Input $e_2(t) = -\frac{400}{15\pi}\cos(1508t) \approx -8.49 \cos(1508t)$ V.
    Evaluate $H(j1508)$: $\omega'^2 = 1508^2 = 2274064$.
    $H(j1508) = \frac{-2274064}{(10^7 - 2274064) + j1000(1508)} = \frac{-2274064}{7725936 + j1508000}$
    Magnitude: $|H(j1508)| = \frac{2274064}{\sqrt{7725936^2 + 1508000^2}} \approx \frac{2274064}{7871676} \approx 0.2889$
    Phase: $\angle H(j1508) = 180^\circ - \arctan(\frac{1508000}{7725936}) = 180^\circ - 11.04^\circ = 168.96^\circ$
    Output $v_{o2}(t) = -8.49 \times 0.2889 \cos(1508t + 168.96^\circ) = -2.45 \cos(1508t + 168.96^\circ)$ V.
    (Note: $-\cos(\theta + 168.96^\circ)$ is equivalent to $\cos(\theta - 11.04^\circ)$).

The Fourier series expression for $v_o(t)$ consisting of the first three terms is:
**$v_o(t) \approx 0 + 2.55 \cos(754t + 175.4^\circ) + 2.45 \cos(1508t - 11.0^\circ) \text{ V}$**

**Part (ii): Average power delivered to the $1\text{ k}\Omega$ resistor**
The average power delivered to the resistor by a sum of orthogonal sinusoidal signals is the sum of the average powers of the individual harmonics: $P_{avg} = \sum \frac{V_{peak, n}^2}{2R}$.
Using the first three terms calculated above:
$P \approx \frac{(0)^2}{2000} + \frac{(2.55)^2}{2000} + \frac{(2.45)^2}{2000}$
$P \approx 0 + 0.00325 + 0.00300 = 0.00625 \text{ W}$
**Average Power $\approx 6.25 \text{ mW}$**

"""always mention ans related location pg no. In pdf , at the end of every soln 6.4 LTIC System Response to Periodic Inputs, pg. 637"""

***

### (b) Determine the Fourier series for the half wave rectified cosine function of period 4 and amplitude 1.

**Detailed Answer:**

**1. Define the signal mathematically over one period:**
The signal $f(t)$ is a half-wave rectified cosine function.
*   **Period ($T_0$):** 4 seconds.
*   **Amplitude ($A$):** 1.
*   **Fundamental frequency ($\omega_0$):** $\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{4} = \frac{\pi}{2}$ rad/s.

The unrectified signal is $\cos(\omega_0 t) = \cos(\frac{\pi}{2}t)$. A half-wave rectifier passes the positive half-cycles and zeroes out the negative half-cycles.
The function $\cos(\frac{\pi}{2}t)$ is positive for $t \in [-1, 1]$ and negative for $t \in [1, 3]$ within one period from -1 to 3 (or -2 to 2). Let's define the function over the symmetric interval $[-\frac{T_0}{2}, \frac{T_0}{2}] = [-2, 2]$:
$$f(t) = \begin{cases} \cos\left(\frac{\pi}{2}t\right) & \text{for } -1 \le t \le 1 \\ 0 & \text{for } 1 < |t| \le 2 \end{cases}$$

**2. Analyze symmetry to simplify calculations:**
Since $\cos(x)$ is an even function, $f(t) = f(-t)$. The signal has **even symmetry**.
Therefore, all sine terms in the Fourier series will be zero:
$$b_n = 0 \quad \text{for all } n$$
The Fourier series will only contain cosine terms:
$$f(t) = a_0 + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t)$$

**3. Calculate the DC component ($a_0$):**
$$a_0 = \frac{1}{T_0} \int_{-T_0/2}^{T_0/2} f(t) dt = \frac{1}{4} \int_{-1}^{1} \cos\left(\frac{\pi}{2}t\right) dt$$
$$a_0 = \frac{1}{4} \left[ \frac{\sin(\frac{\pi}{2}t)}{\pi/2} \right]_{-1}^{1} = \frac{1}{2\pi} \left[ \sin\left(\frac{\pi}{2}\right) - \sin\left(-\frac{\pi}{2}\right) \right]$$
$$a_0 = \frac{1}{2\pi} [1 - (-1)] = \frac{2}{2\pi} = \mathbf{\frac{1}{\pi}}$$

**4. Calculate the cosine coefficients ($a_n$):**
$$a_n = \frac{2}{T_0} \int_{-T_0/2}^{T_0/2} f(t) \cos(n\omega_0 t) dt = \frac{2}{4} \int_{-1}^{1} \cos\left(\frac{\pi}{2}t\right) \cos\left(n\frac{\pi}{2}t\right) dt$$
Because the integrand is an even function, we can integrate from 0 to 1 and double the result:
$$a_n = \int_{0}^{1} \cos\left(\frac{\pi}{2}t\right) \cos\left(n\frac{\pi}{2}t\right) dt$$
Using the trigonometric identity $\cos A \cos B = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$:
$$a_n = \frac{1}{2} \int_{0}^{1} \left[ \cos\left((n+1)\frac{\pi}{2}t\right) + \cos\left((1-n)\frac{\pi}{2}t\right) \right] dt$$

We must evaluate $n=1$ separately to avoid division by zero.
*   **For $n=1$:**
    $$a_1 = \frac{1}{2} \int_{0}^{1} [\cos(\pi t) + \cos(0)] dt = \frac{1}{2} \int_{0}^{1} [\cos(\pi t) + 1] dt$$
    $$a_1 = \frac{1}{2} \left[ \frac{\sin(\pi t)}{\pi} + t \right]_{0}^{1} = \frac{1}{2} \left[ \left(\frac{\sin(\pi)}{\pi} + 1\right) - (0 + 0) \right] = \frac{1}{2}[0 + 1] = \mathbf{\frac{1}{2}}$$

*   **For $n > 1$:**
    $$a_n = \frac{1}{2} \left[ \frac{\sin((n+1)\frac{\pi}{2}t)}{(n+1)\frac{\pi}{2}} + \frac{\sin((1-n)\frac{\pi}{2}t)}{(1-n)\frac{\pi}{2}} \right]_{0}^{1}$$
    $$a_n = \frac{1}{\pi(n+1)} \sin\left((n+1)\frac{\pi}{2}\right) + \frac{1}{\pi(1-n)} \sin\left((1-n)\frac{\pi}{2}\right)$$
    Using angle addition formulas:
    $\sin((n+1)\frac{\pi}{2}) = \sin(n\frac{\pi}{2})\cos(\frac{\pi}{2}) + \cos(n\frac{\pi}{2})\sin(\frac{\pi}{2}) = \cos(n\frac{\pi}{2})$
    $\sin((1-n)\frac{\pi}{2}) = \sin(\frac{\pi}{2})\cos(n\frac{\pi}{2}) - \cos(\frac{\pi}{2})\sin(n\frac{\pi}{2}) = \cos(n\frac{\pi}{2})$
    Substitute these back into the expression for $a_n$:
    $$a_n = \frac{\cos(n\frac{\pi}{2})}{\pi(n+1)} + \frac{\cos(n\frac{\pi}{2})}{\pi(1-n)} = \frac{\cos(n\frac{\pi}{2})}{\pi} \left[ \frac{1}{1+n} + \frac{1}{1-n} \right]$$
    $$a_n = \frac{\cos(n\frac{\pi}{2})}{\pi} \left[ \frac{(1-n) + (1+n)}{(1+n)(1-n)} \right] = \mathbf{\frac{2\cos(n\frac{\pi}{2})}{\pi(1-n^2)}}$$

    Evaluate $a_n$ for even and odd $n$:
    *   If $n$ is odd ($n=3,5,7\dots$), $\cos(n\frac{\pi}{2}) = 0$, so $a_n = 0$.
    *   If $n$ is even ($n=2k$, where $k=1,2,3\dots$), $\cos(2k\frac{\pi}{2}) = \cos(k\pi) = (-1)^k$.
        $$a_{2k} = \frac{2(-1)^k}{\pi(1-(2k)^2)} = \frac{2(-1)^k}{\pi(1-4k^2)}$$

**5. Final Fourier Series Expression:**
$$f(t) = a_0 + a_1\cos(\omega_0 t) + \sum_{k=1}^{\infty} a_{2k} \cos(2k\omega_0 t)$$
**$$f(t) = \frac{1}{\pi} + \frac{1}{2}\cos\left(\frac{\pi}{2}t\right) + \sum_{k=1}^{\infty} \frac{2(-1)^k}{\pi(1-4k^2)} \cos(k\pi t)$$**

always mention ans related location pg no. In pdf , at the end of every soln 6.1 Periodic Signal Representation by Trigonometric Fourier Series, pg. 593-605

***

### (b) Find the trigonometric Fourier series for the square wave signal of Fig. Q. 4(b).
![[Pasted image 20260628170926.png]]
**Detailed Answer:**
**1. Analyze the Signal Parameters:**
From Fig. Q. 4(b), the signal $f(t)$ is a periodic square wave.
*   The signal has a peak amplitude of $A$.
*   One full period $T$ can be observed, for example, from $-T/2$ to $T/2$.
*   Within this centered period, the signal is high ($A$) from $-T/4$ to $T/4$, and low ($0$) elsewhere.
$$f(t) = \begin{cases} A, & \text{for } -T/4 \le t \le T/4 \\ 0, & \text{for } -T/2 < t < -T/4 \text{ and } T/4 < t < T/2 \end{cases}$$
*   The fundamental angular frequency is defined as $\omega_0 = \frac{2\pi}{T}$.
*   Crucially, the signal is symmetric about the vertical axis ($f(t) = f(-t)$), meaning it is an **even function**. Because of this even symmetry, its Fourier series will consist only of cosine terms, and all sine coefficients ($b_n$) will evaluate to zero.

**2. Calculate the Fourier Coefficients:**
The general form for the trigonometric Fourier series is $f(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)]$.

*   **DC Component ($a_0$):**
    $$a_0 = \frac{1}{T} \int_{-T/2}^{T/2} f(t) dt$$
    $$a_0 = \frac{1}{T} \int_{-T/4}^{T/4} A dt = \frac{A}{T} \left[t\right]_{-T/4}^{T/4} = \frac{A}{T} \left(\frac{T}{4} - \left(-\frac{T}{4}\right)\right) = \frac{A}{T} \left(\frac{T}{2}\right) = \frac{A}{2}$$

*   **Cosine Coefficients ($a_n$):**
    $$a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \cos(n\omega_0 t) dt$$
    $$a_n = \frac{2}{T} \int_{-T/4}^{T/4} A \cos(n\omega_0 t) dt = \frac{2A}{T} \left[ \frac{\sin(n\omega_0 t)}{n\omega_0} \right]_{-T/4}^{T/4}$$
    Substitute $\omega_0 = \frac{2\pi}{T}$:
    $$a_n = \frac{2A}{T \cdot n(2\pi/T)} \left[ \sin\left(n \frac{2\pi}{T} \frac{T}{4}\right) - \sin\left(n \frac{2\pi}{T} \frac{-T}{4}\right) \right]$$
    $$a_n = \frac{A}{n\pi} \left[ \sin\left(\frac{n\pi}{2}\right) - \sin\left(-\frac{n\pi}{2}\right) \right]$$
    Since sine is an odd function ($\sin(-\theta) = -\sin(\theta)$):
    $$a_n = \frac{A}{n\pi} \left[ 2\sin\left(\frac{n\pi}{2}\right) \right] = \frac{2A}{n\pi} \sin\left(\frac{n\pi}{2}\right)$$
    
    Let's evaluate $a_n$ for different integer values of $n$:
    *   If $n$ is even ($n=2, 4, 6\dots$), $\sin(n\pi/2) = 0$, so $a_{\text{even}} = 0$.
    *   If $n = 1, 5, 9\dots$, $\sin(n\pi/2) = 1$, so $a_n = \frac{2A}{n\pi}$.
    *   If $n = 3, 7, 11\dots$, $\sin(n\pi/2) = -1$, so $a_n = -\frac{2A}{n\pi}$.

*   **Sine Coefficients ($b_n$):**
    As deduced from the even symmetry, $b_n = 0$ for all $n$.

**3. Construct the Final Fourier Series:**
Substituting the calculated coefficients back into the series formula:
$$f(t) = a_0 + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t)$$
$$f(t) = \frac{A}{2} + \sum_{n=1,3,5\dots}^{\infty} \frac{2A}{n\pi} \sin\left(\frac{n\pi}{2}\right) \cos\left(\frac{2\pi n}{T} t\right)$$
Writing out the first few non-zero terms explicitly gives the final expression:
**$$f(t) = \frac{A}{2} + \frac{2A}{\pi} \left[ \cos\left(\frac{2\pi}{T} t\right) - \frac{1}{3}\cos\left(\frac{6\pi}{T} t\right) + \frac{1}{5}\cos\left(\frac{10\pi}{T} t\right) - \dots \right]$$**

always mention ans related location pg no. In pdf , at the end of every soln 6.1 Periodic Signal Representation by Trigonometric Fourier Series, pg. 593-605


### Q.5. (a) Obtain and draw the frequency spectrum of the following waveform. (figure involved.)
![[Pasted image 20260628100434.png]]
**Detailed Answer:**

The given waveform $f(t)$ is a periodic sawtooth wave. To obtain its frequency spectrum, we must compute its Exponential Fourier Series coefficients.

**1. Determine Signal Parameters:**
From the figure, the signal repeats every 1 unit of time. Therefore, the fundamental period is $T_0 = 1$.
The fundamental radian frequency is $\omega_0 = \frac{2\pi}{T_0} = \frac{2\pi}{1} = 2\pi$ rad/s.
Over one period (e.g., from $t=0$ to $t=1$), the function rises linearly from 0 to 3. The equation for a single period is:
$f(t) = 3t$ for $0 \le t < 1$

**2. Calculate the Exponential Fourier Series Coefficients ($D_n$):**
The exponential Fourier series is given by $f(t) = \sum_{n=-\infty}^{\infty} D_n e^{jn\omega_0 t}$, where the coefficients are:
$D_n = \frac{1}{T_0} \int_{0}^{T_0} f(t) e^{-jn\omega_0 t} dt$

*   **Calculate the DC component ($n=0$):**
    $D_0 = \frac{1}{T_0} \int_{0}^{T_0} f(t) dt$
    This is simply the average value (area under one period divided by the period).
    Area of the triangle $= \frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2}(1)(3) = 1.5$.
    $D_0 = \frac{1.5}{1} = 1.5$

*   **Calculate the AC components ($n \neq 0$):**
    Substitute $T_0 = 1$, $\omega_0 = 2\pi$, and $f(t) = 3t$:
    $D_n = \int_{0}^{1} 3t e^{-jn2\pi t} dt$
    
    We evaluate this integral using integration by parts: $\int u dv = uv - \int v du$
    Let $u = 3t \implies du = 3 dt$
    Let $dv = e^{-jn2\pi t} dt \implies v = \frac{e^{-jn2\pi t}}{-jn2\pi}$
    
    $D_n = \left[ 3t \frac{e^{-jn2\pi t}}{-jn2\pi} \right]_{0}^{1} - \int_{0}^{1} 3 \frac{e^{-jn2\pi t}}{-jn2\pi} dt$
    
    Evaluate the first term at limits 1 and 0:
    At $t=1$: $3(1) \frac{e^{-jn2\pi}}{-jn2\pi} = \frac{3(1)}{-jn2\pi}$ (since $e^{-jn2\pi} = \cos(2\pi n) - j\sin(2\pi n) = 1$ for integer $n$)
    At $t=0$: $3(0) \frac{e^{0}}{-jn2\pi} = 0$
    
    Evaluate the integral part:
    $\int_{0}^{1} \frac{3}{-jn2\pi} e^{-jn2\pi t} dt = \frac{3}{-jn2\pi} \left[ \frac{e^{-jn2\pi t}}{-jn2\pi} \right]_{0}^{1} = \frac{3}{(-jn2\pi)^2} (e^{-jn2\pi} - e^0) = \frac{3}{(-jn2\pi)^2} (1 - 1) = 0$
    
    Therefore, putting it all together:
    $D_n = \frac{3}{-jn2\pi} - 0 = j\frac{3}{2\pi n}$

**3. Define the Spectrum:**
The coefficients are:
$D_n = \begin{cases} 1.5 & \text{for } n = 0 \\ j\frac{3}{2\pi n} & \text{for } n \neq 0 \end{cases}$

To draw the frequency spectrum, we separate this into an amplitude spectrum $|D_n|$ and a phase spectrum $\angle D_n$.

*   **Amplitude Spectrum $|D_n|$:**
    For $n=0$: $|D_0| = 1.5$
    For $n \neq 0$: $|D_n| = \left| j\frac{3}{2\pi n} \right| = \frac{3}{2\pi |n|}$
    The amplitude spectrum consists of lines at frequencies $\omega = 2\pi n$. There is a central spike of height 1.5 at $\omega=0$. For other frequencies, the amplitude decays proportionally to $1/|n|$ symmetrically around the vertical axis.

*   **Phase Spectrum $\angle D_n$:**
    For $n=0$: The DC term is positive and real, so $\angle D_0 = 0$ rad.
    For $n > 0$ (positive frequencies): $D_n = j \times \text{(positive number)}$. A purely imaginary positive number has a phase of $\pi/2$ (or $90^\circ$). So $\angle D_n = \pi/2$.
    For $n < 0$ (negative frequencies): $D_n = j \times \text{(negative number)} = -j \times \text{(positive number)}$. A purely imaginary negative number has a phase of $-\pi/2$ (or $-90^\circ$). So $\angle D_n = -\pi/2$.
    The phase spectrum is an odd function, with lines at $-\pi/2$ for negative frequencies and lines at $\pi/2$ for positive frequencies.

always mention ans related location pg no. In pdf , at the end of every soln 6.3 Exponential Fourier Series, pg. 621-625

### Q.5 (a) A certain band-limited periodic current has only three frequencies in its Fourier series representation: dc, 50 Hz, and 100 Hz. The current may be represented as $i(t) = 4 + 6\sin(100\pi t) + 8\cos(100\pi t) - 3\sin(200\pi t) - 4\cos(200\pi t)$ A.
### (ii) If $i(t)$ flows through a 2 $\Omega$ resistor, how many watt of average power will be dissipated?

**Detailed Answer:**

**(i) Express $i(t)$ in amplitude-phase form.**

The amplitude-phase form (also called compact trigonometric form) of a Fourier series is:
$$x(t) = C_0 + \sum_{n=1}^{\infty} C_n \cos(n\omega_0 t + \theta_n)$$
Where a general harmonic term $a_n \cos(\omega t) + b_n \sin(\omega t)$ is converted using:
$C_n = \sqrt{a_n^2 + b_n^2}$
$\theta_n = \tan^{-1}\left(\frac{-b_n}{a_n}\right)$  *(Note: quadrant must be determined by the signs of $a_n$ and $-b_n$)*

The given current is:
$i(t) = 4 + \underbrace{8\cos(100\pi t) + 6\sin(100\pi t)}_{\text{First harmonic (50 Hz)}} + \underbrace{(-4)\cos(200\pi t) - 3\sin(200\pi t)}_{\text{Second harmonic (100 Hz)}}$

*   **DC Component ($C_0$):**
    $C_0 = 4$ A

*   **First Harmonic (50 Hz, $\omega_1 = 100\pi$):**
    $a_1 = 8$, $b_1 = 6$
    Amplitude $C_1 = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$ A
    Phase $\theta_1 = \tan^{-1}\left(\frac{-6}{8}\right) = \tan^{-1}(-0.75)$.
    Since $a_1$ is positive and $-b_1$ is negative, the angle is in the 4th quadrant.
    $\theta_1 \approx -36.87^\circ$ (or $-0.6435$ rad)

*   **Second Harmonic (100 Hz, $\omega_2 = 200\pi$):**
    $a_2 = -4$, $b_2 = -3$
    Amplitude $C_2 = \sqrt{(-4)^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$ A
    Phase $\theta_2 = \tan^{-1}\left(\frac{-(-3)}{-4}\right) = \tan^{-1}\left(\frac{3}{-4}\right) = \tan^{-1}(-0.75)$.
    Since $a_2$ is negative and $-b_2$ is positive, the angle is in the 2nd quadrant.
    $\theta_2 = 180^\circ - 36.87^\circ = 143.13^\circ$ (or $2.498$ rad)

Combining these components, the amplitude-phase form is:
**$$i(t) = 4 + 10\cos(100\pi t - 36.87^\circ) + 5\cos(200\pi t + 143.13^\circ) \text{ A}$$**

**(ii) Average power dissipated in a $2\ \Omega$ resistor.**

Parseval's theorem states that the total average power of a periodic signal is the sum of the average powers of its individual harmonic components.
For a current $i(t) = C_0 + \sum C_n \cos(n\omega_0 t + \theta_n)$ flowing through a resistor $R$, the average power $P_{avg}$ is:
$$P_{avg} = I_{rms}^2 R = \left( C_0^2 + \sum_{n=1}^{\infty} \frac{C_n^2}{2} \right) R$$

Using the amplitudes found in part (i):
$C_0 = 4$
$C_1 = 10$
$C_2 = 5$
$R = 2\ \Omega$

Calculate the mean square current $I_{rms}^2$:
$$I_{rms}^2 = 4^2 + \frac{10^2}{2} + \frac{5^2}{2}$$
$$I_{rms}^2 = 16 + \frac{100}{2} + \frac{25}{2}$$
$$I_{rms}^2 = 16 + 50 + 12.5 = 78.5\ \text{A}^2$$

Calculate the average power:
$$P_{avg} = 78.5 \times 2$$
**$$P_{avg} = 157\ \text{W}$$**

always mention ans related location pg no. In pdf , at the end of every soln 6.1 Periodic Signal Representation by Trigonometric Fourier Series (Compact Form), pg. 597 and 6.3-2 Parseval's Theorem, pg. 632

Based on the images provided, here are the solutions to the requested questions.

### Q.6. (a) Define the following terms: (i) Amplitude spectrum, (ii) Phase spectrum, and (iii) Ladder network.

**Detailed Answer:**

**(i) Amplitude Spectrum:**
In the context of Fourier analysis (both Fourier series and Fourier transforms), a signal is represented as a sum or integral of complex exponentials (or sinusoids) of various frequencies. The **amplitude spectrum** is a graphical plot that shows the magnitude (or absolute value) of these frequency components as a function of frequency.
*   For a periodic signal represented by an exponential Fourier series $x(t) = \sum D_n e^{jn\omega_0 t}$, the amplitude spectrum is the plot of $|D_n|$ versus the frequency variable $n\omega_0$ (or simply index $n$).
*   For an aperiodic signal represented by a Fourier transform $X(\omega)$, the amplitude spectrum is the plot of $|X(\omega)|$ versus the continuous frequency variable $\omega$. It illustrates how the signal's energy or strength is distributed across different frequencies.

**(ii) Phase Spectrum:**
Similarly, the **phase spectrum** is a graphical plot that displays the phase angle of the constituent frequency components of a signal as a function of frequency.
*   For a periodic signal, it is the plot of the angle $\angle D_n$ (or $\theta_n$ in trigonometric form) versus frequency.
*   For an aperiodic signal, it is the plot of $\angle X(\omega)$ versus $\omega$.
Together with the amplitude spectrum, the phase spectrum provides a complete frequency-domain description of the signal. The phase spectrum is crucial for understanding the relative timing and alignment of the different sinusoidal components that make up the signal.

**(iii) Ladder Network:**
A **ladder network** is a specific type of electrical circuit topology consisting of alternating series and parallel components (typically resistors, capacitors, or inductors) connected in a cascading manner. When drawn on a schematic, the repeating "L" sections make the circuit look like a ladder, where series components form the "rails" and parallel components form the "rungs." They are widely used in electrical engineering for applications such as passive filter design, attenuators, and digital-to-analog converters (like the R-2R ladder).

always mention ans related location pg no. In pdf , at the end of every soln 6.1-1 The Fourier Spectrum, pg. 598 and 4.8 Frequency Response of an LTIC System, pg. 413

***

### Q.7 (c) If the sawtooth waveform shown in following Fig. is applied to an filter with the given transfer function (i) Find the Fourier series expansion of the sawtooth wave. (ii) Determine the output of the filter. Figure involved.
![[Pasted image 20260626191714.png]]
**Solution:**

**(i) Fourier series expansion of the sawtooth wave:**

Let the sawtooth wave be $x(t)$. From the graph, we observe the following properties:
*   The signal repeats every $1$ second, so the fundamental period is $T_0 = 1$.
*   The fundamental radian frequency is $\omega_0 = \frac{2\pi}{T_0} = 2\pi$ rad/s.
*   Over one period from $t=0$ to $t=1$, the function is a straight line passing through the origin with a slope of $1$. Therefore, $x(t) = t$ for $0 \le t < 1$.

We will find the exponential Fourier series, given by $x(t) = \sum_{n=-\infty}^{\infty} D_n e^{jn\omega_0 t}$.
The coefficients $D_n$ are calculated as:
$$D_n = \frac{1}{T_0} \int_{0}^{T_0} x(t) e^{-jn\omega_0 t} dt$$
Substituting our specific signal values:
$$D_n = \int_{0}^{1} t e^{-jn2\pi t} dt$$

**For $n = 0$ (the DC component):**
$$D_0 = \int_{0}^{1} t dt = \left[ \frac{t^2}{2} \right]_0^1 = \frac{1}{2} = 0.5$$

**For $n \neq 0$:**
We use integration by parts: $\int u dv = uv - \int v du$
Let $u = t \implies du = dt$
Let $dv = e^{-jn2\pi t} dt \implies v = \frac{e^{-jn2\pi t}}{-jn2\pi}$

$$D_n = \left[ t \frac{e^{-jn2\pi t}}{-jn2\pi} \right]_0^1 - \int_{0}^{1} \frac{e^{-jn2\pi t}}{-jn2\pi} dt$$
$$D_n = \left( 1 \cdot \frac{e^{-jn2\pi}}{-jn2\pi} - 0 \right) - \left[ \frac{e^{-jn2\pi t}}{(-jn2\pi)^2} \right]_0^1$$
Since $n$ is an integer, $e^{-jn2\pi} = \cos(-2\pi n) + j\sin(-2\pi n) = 1$.
$$D_n = \frac{1}{-jn2\pi} - \frac{1}{-4\pi^2 n^2} \left( e^{-jn2\pi} - e^0 \right)$$
$$D_n = \frac{1}{-jn2\pi} - \frac{1}{-4\pi^2 n^2} (1 - 1)$$
$$D_n = \frac{1}{-jn2\pi} = \frac{j}{2\pi n}$$

The exponential Fourier series is:
$$x(t) = 0.5 + \sum_{n=-\infty, n \neq 0}^{\infty} \frac{j}{2\pi n} e^{jn2\pi t}$$

Alternatively, this can be expressed as a trigonometric Fourier series:
$$x(t) = C_0 + \sum_{n=1}^{\infty} C_n \cos(n\omega_0 t + \theta_n)$$
Where $C_0 = D_0 = 0.5$, and for $n \ge 1$: $D_n = 0 + j\frac{1}{2\pi n}$.
This implies $a_n = 2\text{Re}\{D_n\} = 0$ and $b_n = -2\text{Im}\{D_n\} = -\frac{1}{\pi n}$.
Thus, $x(t) = 0.5 - \sum_{n=1}^{\infty} \frac{1}{\pi n} \sin(2\pi n t)$.

**(ii) Determine the output of the filter:**

The given filter has a magnitude response $|H(\omega)|$ which is an ideal highpass filter.
*   $|H(\omega)| = 0$ for $|\omega| < 10$
*   $|H(\omega)| = 1$ for $|\omega| \ge 10$
(Assuming an ideal zero-phase shift for the passband, as is typical when only magnitude is given).

When a periodic signal passes through a linear time-invariant system, the output is the sum of the system's response to each individual frequency component of the input's Fourier series.
The input signal contains components at frequencies $\omega_n = n\omega_0 = 2\pi n$ rad/s.
We must check which harmonics fall into the passband ($|\omega_n| \ge 10$) and which fall into the stopband ($|\omega_n| < 10$).
*   **$n = 0$ (DC):** $\omega_0 = 0 < 10$. This component is **blocked** ($H(0) = 0$).
*   **$n = 1$ (Fundamental):** $\omega_1 = 2\pi(1) \approx 6.28 < 10$. This component is **blocked** ($H(2\pi) = 0$).
*   **$n = 2$ (2nd Harmonic):** $\omega_2 = 2\pi(2) = 4\pi \approx 12.57 \ge 10$. This component is **passed** ($H(4\pi) = 1$).
*   **$n \ge 3$:** All higher harmonics have frequencies greater than $10$ rad/s and will be **passed** unaltered.

The output $y(t)$ will be the original Fourier series minus the components that were blocked (the DC term and the first harmonic/fundamental).
Using the trigonometric form derived in part (i):
$$y(t) = - \sum_{n=2}^{\infty} \frac{1}{\pi n} \sin(2\pi n t)$$

This can also be expressed elegantly in terms of the original input signal $x(t)$ by subtracting the rejected components:
$$y(t) = x(t) - D_0 - (D_1 e^{j2\pi t} + D_{-1} e^{-j2\pi t})$$
$$y(t) = x(t) - 0.5 - \left( \frac{j}{2\pi} e^{j2\pi t} + \frac{-j}{2\pi} e^{-j2\pi t} \right)$$
$$y(t) = x(t) - 0.5 + \frac{1}{\pi}\left( \frac{e^{j2\pi t} - e^{-j2\pi t}}{2j} \right)$$
$$y(t) = x(t) - 0.5 + \frac{1}{\pi} \sin(2\pi t)$$

Location pg 638 In pdf

---

### 4. Pg 27, CT-3 Q2: Find the Fourier series of the square wave in following Fig. Plot the amplitude and phase spectra. ![[Pasted image 20260712005529.png]]

**Figure Description:** The figure shows a periodic square wave $f(t)$. The signal alternates between an amplitude of $1$ and $-1$. Analyzing the axis, one complete cycle occurs between $t = 0$ and $t = 2$.
*   $f(t) = 1$ for $0 < t < 1$
*   $f(t) = -1$ for $1 < t < 2$
*   Period $T = 2$ seconds.
*   Fundamental angular frequency $\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{2} = \pi \text{ rad/s}$.

**Solution:**

**Step 1: Check for Symmetry to simplify calculations**
*   **Odd/Even Symmetry:** $f(-t) = -f(t)$. For example, $f(0.5) = 1$ and $f(-0.5) = -1$. Because the function is odd, the DC component $a_0 = 0$ and the cosine coefficients $a_n = 0$. The Fourier series will only contain sine terms ($b_n$).
*   **Half-wave Symmetry:** $f(t \pm T/2) = -f(t)$. Here $T/2 = 1$. Shifting the wave by 1 unit inverts it. Because it possesses half-wave symmetry, the series will only contain **odd harmonics** ($n = 1, 3, 5, \dots$).

**Step 2: Calculate the Fourier coefficients ($b_n$)**
The formula for $b_n$ is:
$b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t) dt$
Since $T=2$ and $\omega_0 = \pi$:
$b_n = \frac{2}{2} \left[ \int_{0}^{1} (1) \sin(n\pi t) dt + \int_{1}^{2} (-1) \sin(n\pi t) dt \right]$
$b_n = \left[ \frac{-\cos(n\pi t)}{n\pi} \right]_{0}^{1} - \left[ \frac{-\cos(n\pi t)}{n\pi} \right]_{1}^{2}$
$b_n = \frac{1}{n\pi} \left[ (-\cos(n\pi) + \cos(0)) + (\cos(2n\pi) - \cos(n\pi)) \right]$
We know that $\cos(0) = 1$, $\cos(2n\pi) = 1$, and $\cos(n\pi) = (-1)^n$.
$b_n = \frac{1}{n\pi} \left[ -(-1)^n + 1 + 1 - (-1)^n \right]$
$b_n = \frac{1}{n\pi} \left[ 2 - 2(-1)^n \right] = \frac{2}{n\pi} \left[ 1 - (-1)^n \right]$

Evaluating for even and odd $n$:
*   If $n$ is even ($n = 2, 4, 6...$): $(-1)^n = 1 \implies b_n = \frac{2}{n\pi}[1 - 1] = 0$.
*   If $n$ is odd ($n = 1, 3, 5...$): $(-1)^n = -1 \implies b_n = \frac{2}{n\pi}[1 - (-1)] = \mathbf{\frac{4}{n\pi}}$.

**Step 3: Write the Fourier Series**
$f(t) = \sum_{n=1,3,5,\dots}^{\infty} b_n \sin(n\omega_0 t)$
$\mathbf{f(t) = \sum_{n=\text{odd}}^{\infty} \frac{4}{n\pi} \sin(n\pi t)}$

**Step 4: Plot the Amplitude and Phase Spectra**
To plot the spectra, we express the series in the amplitude-phase form: $f(t) = a_0 + \sum_{n=1}^{\infty} A_n \cos(n\omega_0 t + \phi_n)$.
We have sine terms, which can be converted to cosine terms:
$\sin(\theta) = \cos(\theta - 90^\circ)$
Therefore, the $n$-th harmonic is: $\frac{4}{n\pi} \cos(n\pi t - 90^\circ)$ (for odd $n$).

*   **Amplitude Spectrum ($A_n$):**
    $A_n = \frac{4}{n\pi}$ for $n = 1, 3, 5, \dots$
    $A_n = 0$ for $n = \text{even}$.
    *(Plot description: A discrete bar graph with vertical lines at $\omega = \pi, 3\pi, 5\pi \dots$. The heights of the bars are $4/\pi \approx 1.27$ at $\omega=\pi$, $4/3\pi \approx 0.42$ at $\omega=3\pi$, $4/5\pi \approx 0.25$ at $\omega=5\pi$, decaying as $1/n$)*.

*   **Phase Spectrum ($\phi_n$):**
    $\phi_n = -90^\circ$ for all odd $n$.
    $\phi_n = 0$ for all even $n$.
    *(Plot description: A discrete bar graph with vertical lines extending downwards to $-90^\circ$ (or $-\pi/2$ radians) strictly at frequencies $\omega = \pi, 3\pi, 5\pi \dots$)*.

*Reference: Sadiku Chapter 17, Sections 17.2 & 17.3 (Symmetry Considerations) / Class Notes Pg 89-91.*

Here are the detailed solutions for the next 4 questions (Questions 5 to 8) from your list.

# 7. Sampling and Modulation

### (b) Discuss amplitude modulation and sampling as the application scenarios of Fourier transform.

**Detailed Answer:**

The Fourier Transform is a fundamental mathematical tool that allows us to move between the time domain and the frequency domain. It reveals the frequency spectrum of a signal, making it essential for understanding and designing systems in communications and signal processing. Two primary application scenarios that rely heavily on the principles of the Fourier Transform are Amplitude Modulation (AM) and Sampling.

**1. Amplitude Modulation (AM)**
*   **Concept:** Amplitude modulation is a technique used in electronic communication to transmit baseband signals (like voice or audio, which occur at low frequencies) over long distances. This is achieved by varying the amplitude of a high-frequency carrier wave, typically a sinusoid like $\cos(\omega_c t)$, in proportion to the message signal $m(t)$. 
*   **Fourier Transform Application:** The Fourier transform explains perfectly how this process shifts signals in the frequency domain. According to the frequency-shifting property (or modulation property) of the Fourier Transform:
    If $m(t) \Leftrightarrow M(\omega)$, then multiplying the signal by a carrier yields:
    $$m(t)\cos(\omega_c t) \Leftrightarrow \frac{1}{2}[M(\omega - \omega_c) + M(\omega + \omega_c)]$$
*   **Significance:** The equation shows that in the frequency domain, the spectrum of the original low-frequency message $M(\omega)$ is shifted and centered symmetrically around the high-frequency carrier at $+\omega_c$ and $-\omega_c$. 
    *   This allows for **Frequency-Division Multiplexing (FDM)**, where multiple signals can be transmitted simultaneously over the same medium (like air or a cable) without interfering, simply by assigning each signal a different carrier frequency $\omega_c$. 
    *   It also allows for practical antenna design, as efficient electromagnetic radiation requires antenna sizes proportional to the signal's wavelength; shifting the signal to a higher frequency significantly reduces the required antenna size.

**2. Sampling**
*   **Concept:** Sampling is the process of converting a continuous-time analog signal $x(t)$ into a discrete-time signal (a sequence of numbers) by extracting its values at regular intervals $T$. This is the crucial first step in digitizing signals for processing by computers or transmitting over digital networks.
*   **Fourier Transform Application:** Mathematically, ideal sampling can be modeled as multiplying the continuous signal $x(t)$ by an impulse train $\delta_T(t) = \sum \delta(t - nT)$. The Fourier transform of the sampled signal $x_s(t)$ is derived using the frequency-convolution property:
    $$X_s(\omega) = \frac{1}{T} \sum_{k=-\infty}^{\infty} X(\omega - k\omega_s)$$
    where $\omega_s = \frac{2\pi}{T}$ is the sampling frequency.
*   **Significance:** The Fourier transform reveals that sampling a signal in the time domain creates infinite periodic replicas of the original signal's frequency spectrum, spaced exactly by the sampling frequency $\omega_s$. 
    *   This perfectly illustrates the **Nyquist-Shannon Sampling Theorem**. For the original signal to be perfectly reconstructed from its samples, these spectral replicas must not overlap. 
    *   To prevent overlap (a phenomenon known as **aliasing**, where high frequencies masquerade as low frequencies and corrupt the data), the sampling frequency $\omega_s$ must be strictly greater than twice the highest frequency component present in the original signal ($B$). Thus, the Fourier Transform provides the exact mathematical proof for the requirement $f_s > 2B$.

"""always mention ans related location pg no. In pdf , at the end of every soln 7.7 Application to Communications: Amplitude Modulation, pg. 736 and 8.1 The Sampling Theorem, pg. 776"""

### Q.7 (a) Consider a band limited signal x(t) with a Fourier transform X($\omega$) shown in the following figure. Draw the Fourier transform of the sampled signal if the sampling frequency is (i) 5 KHz (ii) 10 kHz (iii) 20 kHz. Figure involved.
![[Pasted image 20260626191739.png]]
**Solution:**

**Analysis of the Original Spectrum:**
The figure shows the Fourier transform $X(\omega)$ of a baseband signal. The spectrum is a triangle centered at $\omega = 0$ with a peak amplitude $A$.
The non-zero portion of the spectrum extends from $-2\pi\beta$ to $2\pi\beta$.
The given parameter is $\beta = 5$ kHz.
The x-axis represents radian frequency $\omega$. The maximum radian frequency present in the signal is $\omega_m = 2\pi\beta = 2\pi(5000) = 10,000\pi$ rad/s.
The maximum frequency in Hertz is $f_m = \frac{\omega_m}{2\pi} = \beta = 5$ kHz.
The bandwidth of the signal is $B = 5$ kHz.

**Sampling Theorem Principles:**
When a continuous-time signal $x(t)$ is sampled uniformly at a rate $f_s = \frac{1}{T}$ (sampling interval $T$), the spectrum of the resulting sampled signal, $X_s(\omega)$, consists of the original spectrum $X(\omega)$ repeating periodically at intervals of the sampling frequency $\omega_s = 2\pi f_s$. The amplitude of the repeating spectra is scaled by $f_s$.
Mathematically:
$$X_s(\omega) = f_s \sum_{n=-\infty}^{\infty} X(\omega - n\omega_s) = f_s \sum_{n=-\infty}^{\infty} X(\omega - n 2\pi f_s)$$
The Nyquist rate for this signal is $2f_m = 2(5 \text{ kHz}) = 10 \text{ kHz}$.

**Drawings Description for Different Sampling Frequencies:**
(Note: Since graphical output is constrained, a precise description of how to draw the plots is provided). For simplicity in describing the shapes, we will discuss the placement of the triangular spectrum "replicas" along a frequency axis $f$ (in kHz) rather than $\omega$. The base triangle exists from $-5$ kHz to $5$ kHz.

**(i) Sampling frequency $f_s = 5$ kHz:**
*   This is severe under-sampling ($f_s < 2f_m$). Aliasing will occur.
*   The replicas of the original spectrum will be shifted by multiples of $5$ kHz: $0, \pm 5 \text{ kHz}, \pm 10 \text{ kHz}, \dots$
*   The fundamental replica ($n=0$) spans from $-5$ to $5$ kHz.
*   The first positive replica ($n=1$) is centered at $5$ kHz and spans from $0$ to $10$ kHz.
*   The first negative replica ($n=-1$) is centered at $-5$ kHz and spans from $-10$ to $0$ kHz.
*   **To draw:** Observe that in the region from $0$ to $5$ kHz, the descending linear slope of the $n=0$ replica (going from amplitude $A$ down to $0$) perfectly overlaps and adds to the ascending linear slope of the $n=1$ replica (going from $0$ up to $A$). Because they are straight lines with equal and opposite slopes, their sum is a constant $A$. This happens everywhere across the frequency axis.
*   Finally, the entire spectrum must be scaled by $f_s = 5000$.
*   **Final Sketch:** Draw a continuous, flat horizontal line extending infinitely in both directions along the frequency axis. The amplitude of this constant line is $5000A$.

**(ii) Sampling frequency $f_s = 10$ kHz:**
*   This is sampling exactly at the Nyquist rate ($f_s = 2f_m$).
*   The replicas will be shifted by multiples of $10$ kHz: $0, \pm 10 \text{ kHz}, \pm 20 \text{ kHz}, \dots$
*   The fundamental replica ($n=0$) spans from $-5$ to $5$ kHz.
*   The next replica ($n=1$) is centered at $10$ kHz and spans from $5$ to $15$ kHz.
*   The adjacent replicas meet exactly at their base corners (e.g., at $\pm 5$ kHz, $\pm 15$ kHz) without overlapping.
*   **To draw:** Draw a sequence of adjacent, non-overlapping triangles resting on the x-axis. The bases of the triangles touch. The peaks are located at $0, \pm 10 \text{ kHz}, \pm 20 \text{ kHz}, \dots$
*   The peak amplitude of every triangle is scaled by $f_s = 10000$, making the peaks $10000A$.

**(iii) Sampling frequency $f_s = 20$ kHz:**
*   This is over-sampling ($f_s > 2f_m$). There will be no aliasing, and there will be gaps between the spectrum replicas.
*   The replicas will be shifted by multiples of $20$ kHz: $0, \pm 20 \text{ kHz}, \pm 40 \text{ kHz}, \dots$
*   The fundamental replica spans from $-5$ to $5$ kHz.
*   The next replica ($n=1$) is centered at $20$ kHz and spans from $15$ to $25$ kHz.
*   There is a "guard band" of zero amplitude between the replicas. The gap width is $(f_s - f_m) - f_m = 15 - 5 = 10$ kHz.
*   **To draw:** Draw a series of isolated triangles. Center them at $0, \pm 20 \text{ kHz}, \pm 40 \text{ kHz}, \dots$. Each triangle has a base width of $10$ kHz (spanning $\pm 5$ kHz from its center). The regions between the triangles are flat at zero amplitude.
*   The peak amplitude of each triangle is scaled by $f_s = 20000$, making the peaks $20000A$.

Location pg 537 In pdf

***

# 8. Z-Transform

### (b) The Z-transform of discrete time signal , x(n) must be represented by , X(Z) with its ROC - Explain.

**Detailed Answer:**

The requirement to represent a Z-transform $X(z)$ alongside its Region of Convergence (ROC) stems from two fundamental mathematical and practical reasons: convergence of the infinite series and uniqueness of the inverse transform.

**1. Convergence of the Infinite Series:**
The bilateral (two-sided) Z-transform of a discrete-time signal $x(n)$ is defined by the infinite power series:
$$X(z) = \sum_{n=-\infty}^{\infty} x(n) z^{-n}$$
Because this is an infinite sum, it does not yield a finite, well-defined value for every possible complex number $z$. The summation will only converge (evaluate to a finite number) for a specific set of values of $z$. This set of values in the complex $z$-plane where the series converges absolutely is defined as the Region of Convergence (ROC). Without the ROC, the expression $X(z)$ is mathematically incomplete because it is undefined outside that region.

**2. Uniqueness of the Inverse Z-Transform (The Primary Reason):**
More crucially, the algebraic expression for $X(z)$ alone is not sufficient to uniquely identify the original time-domain sequence $x(n)$. It is entirely possible for two completely different time-domain signals to possess the exact same algebraic formula for their Z-transforms. They are distinguished solely by their different Regions of Convergence.

To illustrate this, consider a standard example of two different signals:

*   **Signal 1: A causal (right-sided) exponential sequence**
    Let $x_1(n) = a^n u(n)$
    The Z-transform is $X_1(z) = \sum_{n=0}^{\infty} a^n z^{-n} = \sum_{n=0}^{\infty} (az^{-1})^n$. 
    This geometric series converges if $|az^{-1}| < 1 \implies |z| > |a|$.
    The closed-form expression is $X_1(z) = \frac{1}{1 - az^{-1}} = \frac{z}{z - a}$.
    So, $X_1(z) = \frac{z}{z - a}$ with **ROC: $|z| > |a|$**.

*   **Signal 2: An anti-causal (left-sided) exponential sequence**
    Let $x_2(n) = -a^n u(-n-1)$
    The Z-transform is $X_2(z) = \sum_{n=-\infty}^{-1} -a^n z^{-n}$.
    By changing variables ($m = -n$), we can show this evaluates to the exact same closed-form expression, but the convergence condition is different. It converges if $|a^{-1}z| < 1 \implies |z| < |a|$.
    The closed-form expression is $X_2(z) = \frac{z}{z - a}$.
    So, $X_2(z) = \frac{z}{z - a}$ with **ROC: $|z| < |a|$**.

**Conclusion:**
Both $x_1(n)$ and $x_2(n)$ result in the identical algebraic function $X(z) = \frac{z}{z - a}$. If you were only given the function $X(z) = \frac{z}{z - a}$ and asked to find the inverse Z-transform, the answer would be ambiguous. You wouldn't know if the original signal was $a^n u(n)$ or $-a^n u(-n-1)$. 
However, if you are given both $X(z) = \frac{z}{z - a}$ *and* the ROC $|z| > |a|$, the ambiguity is resolved, and you know the inverse is definitively the causal sequence $a^n u(n)$. Therefore, specifying the ROC is strictly required for a complete and unique Z-domain representation of a discrete-time signal.

always mention ans related location pg no. In pdf , at the end of every soln 5.8 The Bilateral z-Transform, pg. 554-555

### (c) For a discrete time signa as shown in the Fig. 8(c), show that $X(Z) = \frac{1-z^{-m}}{1-z^{-1}}$
![[Pasted image 20260628170808.png]]
**Detailed Answer:**

**1. Define the discrete-time signal $x(n)$:**
Based on the provided graph, the signal $x(n)$ consists of a sequence of unit impulses (amplitude of 1) starting at $n=0$ and ending at $n=m-1$. The signal is zero for all $n < 0$ and $n \ge m$.
Mathematically, this finite-duration sequence can be expressed as:
$$x(n) = \begin{cases} 1, & \text{for } 0 \le n \le m-1 \\ 0, & \text{otherwise} \end{cases}$$
Alternatively, using the discrete-time unit step function $u(n)$, we can express the signal as a rectangular pulse:
$$x(n) = u(n) - u(n-m)$$

**2. Approach 1: Apply the Z-transform definition directly**
The bilateral Z-transform of a discrete-time signal $x(n)$ is defined as:
$$X(z) = \sum_{n=-\infty}^{\infty} x(n) z^{-n}$$
Substituting our defined sequence $x(n)$ into the formula, the summation limits are restricted to where the signal is non-zero (from $0$ to $m-1$):
$$X(z) = \sum_{n=0}^{m-1} (1) z^{-n}$$
Expanding the summation gives:
$$X(z) = z^{-0} + z^{-1} + z^{-2} + \dots + z^{-(m-1)}$$
$$X(z) = 1 + z^{-1} + z^{-2} + \dots + z^{-(m-1)}$$
This expression is a finite geometric series. The parameters of this series are:
*   First term, $a = 1$
*   Common ratio, $r = z^{-1}$
*   Number of terms, $N = m$
The formula for the sum of a finite geometric series is $S_N = a \frac{1 - r^N}{1 - r}$ (for $r \neq 1$).
Applying this formula yields:
$$X(z) = 1 \cdot \frac{1 - (z^{-1})^m}{1 - z^{-1}}$$
**$$X(z) = \frac{1 - z^{-m}}{1 - z^{-1}}$$**
This completes the proof.

**3. Approach 2: Using Z-transform properties**
We expressed the signal earlier as $x(n) = u(n) - u(n-m)$.
We can use the linearity property and standard transform pairs:
*   Standard pair for unit step: $\mathcal{Z}\{u(n)\} = \frac{1}{1-z^{-1}}$
*   Time-shifting property: If $\mathcal{Z}\{x(n)\} = X(z)$, then $\mathcal{Z}\{x(n-k)\} = z^{-k}X(z)$
Applying these to our signal:
$$X(z) = \mathcal{Z}\{u(n)\} - \mathcal{Z}\{u(n-m)\}$$
$$X(z) = \frac{1}{1-z^{-1}} - z^{-m} \left( \frac{1}{1-z^{-1}} \right)$$
Factoring out the common term:
**$$X(z) = \frac{1 - z^{-m}}{1 - z^{-1}}$$**

**4. Determine the Region of Convergence (ROC):**
The Z-transform is given by the finite sum $X(z) = 1 + \frac{1}{z} + \frac{1}{z^2} + \dots + \frac{1}{z^{m-1}}$.
This sum evaluates to a finite number for all values of $z$ in the complex plane, except where individual terms might go to infinity. The terms containing $1/z$ will go to infinity only when $z = 0$.
Therefore, the Region of Convergence (ROC) for this finite-duration right-sided signal is the entire z-plane excluding the origin.
**ROC: $|z| > 0$**

always mention ans related location pg no. In pdf , at the end of every soln 5.1 The z-Transform, pg. 488-490 and 5.2 Some Properties of the z-Transform, pg. 501-509

Based on the provided images, here are the detailed solutions to a selection of the questions.

# 9. Miscellaneous

### (i) $x(t) = u(t) - u(t - a), \quad a > 0$
### (ii) $y(t) = t[u(t) - u(t - a)], \quad a > 0$

**Detailed Answer:**

**(i) For the signal $x(t) = u(t) - u(t - a)$**

**Derivative:**
The derivative of the unit step function $u(t)$ is the unit impulse function $\delta(t)$.
Applying the derivative operator, which is linear:
$$\frac{dx(t)}{dt} = \frac{d}{dt}[u(t)] - \frac{d}{dt}[u(t - a)]$$
**$$\frac{dx(t)}{dt} = \delta(t) - \delta(t - a)$$**

**Sketching:**
*   **$x(t)$** is a standard rectangular gate pulse. It has a value of 1 starting at $t=0$ and returns to 0 at $t=a$.
*   **$\frac{dx(t)}{dt}$** consists of two impulses that represent the points where $x(t)$ changes abruptly. There is an upward-pointing impulse at $t=0$ with a strength (area) of 1, and a downward-pointing impulse at $t=a$ with a strength of -1.

**(ii) For the signal $y(t) = t[u(t) - u(t - a)]$**

**Derivative:**
We need to use the product rule for differentiation: $\frac{d}{dt}(u \cdot v) = \frac{du}{dt}v + u\frac{dv}{dt}$.
Let $u = t$ and $v = [u(t) - u(t - a)]$.
$$\frac{dy(t)}{dt} = \frac{d(t)}{dt} \cdot [u(t) - u(t - a)] + t \cdot \frac{d}{dt}[u(t) - u(t - a)]$$
$$\frac{dy(t)}{dt} = 1 \cdot [u(t) - u(t - a)] + t \cdot [\delta(t) - \delta(t - a)]$$
Distributing the $t$:
$$\frac{dy(t)}{dt} = u(t) - u(t - a) + t\delta(t) - t\delta(t - a)$$
Now, we apply the sampling property of the impulse function: $f(t)\delta(t-t_0) = f(t_0)\delta(t-t_0)$.
*   For $t\delta(t)$, evaluate $f(t)=t$ at $t_0=0$: $0 \cdot \delta(t) = 0$.
*   For $t\delta(t-a)$, evaluate $f(t)=t$ at $t_0=a$: $a\delta(t-a)$.
Substituting these values back:
**$$\frac{dy(t)}{dt} = u(t) - u(t - a) - a\delta(t - a)$$**

**Sketching:**
*   **$y(t)$** is a ramp function that is turned on between $t=0$ and $t=a$. It starts at 0, rises with a slope of 1 to reach a value of $a$ at $t=a$, and then drops straight down to 0.
*   **$\frac{dy(t)}{dt}$** has two parts. The term $[u(t) - u(t - a)]$ is a rectangular pulse of height 1 from $t=0$ to $t=a$, representing the constant slope of the ramp. The term $-a\delta(t - a)$ is a downward-pointing impulse located at $t=a$ with a strength of $a$, representing the sudden drop in the signal's value back to zero.

always mention ans related location pg no. In pdf , at the end of every soln 1.4-2 The Unit Impulse Function $\delta(t)$ (Unit Impulse as a Generalized Function), pg. 88

Based on the provided images, here are the detailed solutions for the two questions.

### (i) Express $i(t)$ in amplitude-phase form.

