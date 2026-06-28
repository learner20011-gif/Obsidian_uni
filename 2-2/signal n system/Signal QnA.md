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

Hi

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