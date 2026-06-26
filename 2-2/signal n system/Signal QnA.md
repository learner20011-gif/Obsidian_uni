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