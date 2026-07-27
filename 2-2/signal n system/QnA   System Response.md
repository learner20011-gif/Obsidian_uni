Based on the provided document, here are the step-by-step solutions for the first four questions.

### 3. 1. Page 14, Q.3(b): Determine $i_o(t)$ for the following network using Fourier transform method. [Figure involved.]

**Problem Statement:**
Find the output current $i_o(t)$ using the Fourier transform method for a circuit with a voltage source $v_s(t) = 5e^{-2t}u(t)$ V, a series resistor $R = 2 \Omega$, and a parallel combination of a capacitor $C = \frac{1}{4}$ F and an inductor $L = 2$ H. *(Assumption: Based on standard circuit diagrams, $i_o(t)$ is taken as the current through the final output branch, the 2 H inductor.)*

**Solution:**
1.  **Transform to the Frequency Domain:**
    The Fourier transform of the input voltage is:
    $$V_s(\omega) = \mathcal{F}\{5e^{-2t}u(t)\} = \frac{5}{2 + j\omega}$$
    The impedances of the circuit elements are:
    $$Z_R = 2 \Omega$$
    $$Z_C = \frac{1}{j\omega C} = \frac{1}{j\omega(1/4)} = \frac{4}{j\omega} \Omega$$
    $$Z_L = j\omega L = j2\omega \Omega$$

2.  **Find the Transfer Function $H(\omega) = \frac{I_o(\omega)}{V_s(\omega)}$:**
    Let $V_x(\omega)$ be the voltage at the node above the parallel LC branches. Applying Nodal Analysis (KCL) at this node:
    $$\frac{V_x(\omega) - V_s(\omega)}{2} + \frac{V_x(\omega)}{4/j\omega} + \frac{V_x(\omega)}{j2\omega} = 0$$
    $$V_x(\omega) \left[ \frac{1}{2} + \frac{j\omega}{4} + \frac{1}{j2\omega} \right] = \frac{V_s(\omega)}{2}$$
    Multiply by 4 to simplify:
    $$V_x(\omega) \left[ 2 + j\omega + \frac{2}{j\omega} \right] = 2 V_s(\omega)$$
    $$V_x(\omega) \left[ \frac{j2\omega + (j\omega)^2 + 2}{j\omega} \right] = 2 V_s(\omega)$$
    $$V_x(\omega) = \frac{j2\omega}{(j\omega)^2 + j2\omega + 2} V_s(\omega)$$
    The current through the inductor is $I_o(\omega) = \frac{V_x(\omega)}{Z_L}$:
    $$I_o(\omega) = \frac{V_x(\omega)}{j2\omega} = \frac{1}{(j\omega)^2 + j2\omega + 2} V_s(\omega)$$

3.  **Calculate $I_o(\omega)$ and perform Inverse Fourier Transform:**
    Substitute $V_s(\omega)$ into the equation:
    $$I_o(\omega) = \frac{5}{(2 + j\omega)((j\omega)^2 + j2\omega + 2)}$$
    To find the inverse easily, we use partial fraction expansion. Let $s = j\omega$:
    $$I_o(s) = \frac{5}{(s+2)(s^2 + 2s + 2)} = \frac{A}{s+2} + \frac{Bs + C}{s^2 + 2s + 2}$$
    $$5 = A(s^2 + 2s + 2) + (Bs + C)(s + 2)$$
    Setting $s = -2$: $5 = A(4 - 4 + 2) \implies 2A = 5 \implies A = 2.5$
    Equating $s^2$ coefficients: $0 = A + B \implies B = -2.5$
    Equating constants: $5 = 2A + 2C \implies 5 = 5 + 2C \implies C = 0$
    
    Substitute $A, B,$ and $C$ back:
    $$I_o(s) = \frac{2.5}{s+2} - \frac{2.5s}{s^2 + 2s + 2}$$
    Complete the square in the denominator of the second term ($s^2+2s+2 = (s+1)^2+1$):
    $$I_o(s) = \frac{2.5}{s+2} - 2.5 \left( \frac{s+1 - 1}{(s+1)^2 + 1} \right) = \frac{2.5}{s+2} - 2.5 \frac{s+1}{(s+1)^2 + 1} + 2.5 \frac{1}{(s+1)^2 + 1}$$
    Now, converting back from $s = j\omega$ to the time domain using standard Fourier transform pairs:
    $$i_o(t) = 2.5e^{-2t}u(t) - 2.5e^{-t}\cos(t)u(t) + 2.5e^{-t}\sin(t)u(t) \text{ A}$$

*Ans related location: Sadiku Textbook, Chapter 18 (Fourier Transform), Section 18.4 (Circuit Applications), pg. 833-835.*

***

### 3. 2. Page 15, Q.5(b): The square wave in the following waveform is applied to the following network. Find the Fourier series of $v_o(t)$. [Figure involved.]

**Problem Statement:**
A square wave voltage $v_i(t)$ with an amplitude of $\pm 10$ V and a period of $T = 2$ s is applied to an inverting ideal integrator op-amp circuit with $R = 10 \text{ k}\Omega$ and $C = 40 \mu\text{F}$ (using $\mu\text{F}$ as standard for such circuits). Find the Fourier series of the output $v_o(t)$.

**Solution:**
1.  **Fourier Series of the Input Waveform $v_i(t)$:**
    The input is an alternating square wave. 
    Period $T = 2 \text{ s} \implies \text{Fundamental frequency } \omega_0 = \frac{2\pi}{T} = \pi \text{ rad/s}$.
    The waveform is odd-symmetric, so $a_0 = 0$ and $a_n = 0$. The series only contains sine terms.
    The Fourier coefficients for a standard square wave of amplitude $V_m$ are $b_n = \frac{4V_m}{n\pi}$ for odd $n$.
    $$v_i(t) = \sum_{n=1,3,5...}^{\infty} \frac{40}{n\pi} \sin(n\pi t) \text{ V}$$
    In phasor form for each harmonic $n$: $V_{in} = \frac{40}{n\pi} \angle -90^\circ$ V.

2.  **Transfer Function of the Integrator:**
    For an inverting integrator, the output relates to the input by $v_o(t) = -\frac{1}{RC} \int v_i(t) dt$.
    In the frequency domain, the transfer function is:
    $$H(\omega) = -\frac{Z_C}{Z_R} = -\frac{1/(j\omega C)}{R} = -\frac{1}{j\omega RC} = \frac{1}{\omega RC} \angle 90^\circ$$
    Let's calculate the time constant $RC$:
    $$RC = (10 \times 10^3 \text{ }\Omega) \times (40 \times 10^{-6} \text{ F}) = 0.4 \text{ s}$$

3.  **Determine Output Fourier Series:**
    The output phasor for each harmonic is $V_{on} = H(n\omega_0) V_{in}$.
    Evaluate $H(\omega)$ at the harmonic frequencies $\omega_n = n\pi$:
    $$H(n\pi) = \frac{1}{n\pi(0.4)} \angle 90^\circ = \frac{2.5}{n\pi} \angle 90^\circ$$
    Multiply by the input phasor:
    $$V_{on} = \left( \frac{2.5}{n\pi} \angle 90^\circ \right) \left( \frac{40}{n\pi} \angle -90^\circ \right) = \frac{100}{n^2\pi^2} \angle 0^\circ$$
    Converting the phasors back to the time domain yields cosine waves (since $\angle 0^\circ$ represents a pure cosine):
    $$v_o(t) = \sum_{n=1,3,5...}^{\infty} \frac{100}{n^2\pi^2} \cos(n\pi t) \text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 17 (The Fourier Series), Section 17.4 (Circuit Applications), pg. 778-781.*

***

### 3. 3. Page 16, Q(b) (Top): If the following sawtooth waveform is applied to a band-pass filter with the transfer function shown below Determine the output. [Figure involved.]

**Problem Statement:**
A sawtooth waveform $v_i(t)$ is applied to an ideal band-pass filter. Find the output $v_o(t)$.
From the figures:
*   The sawtooth wave has a period $T = 1$ s and goes from $-1$ to $1$. The equation for one period is $v_i(t) = 2t - 1$ for $0 < t < 1$.
*   The band-pass filter has a magnitude $|H(\omega)| = 1$ in the frequency range $15 < \omega < 35$ rad/s and $0$ elsewhere. (Assuming zero phase shift).

**Solution:**
1.  **Fourier Series of the Sawtooth Wave:**
    Period $T = 1 \text{ s} \implies \omega_0 = \frac{2\pi}{T} = 2\pi \text{ rad/s}$.
    The waveform has a DC value $a_0 = 0$ (area above and below axis cancels).
    Because $v_i(t) = 2t-1$ over $0 < t < 1$ acts as a shifted odd function, we calculate $b_n$:
    $$b_n = \frac{2}{T} \int_{0}^{T} v_i(t) \sin(n\omega_0 t) dt = 2 \int_{0}^{1} (2t - 1) \sin(n 2\pi t) dt = -\frac{2}{n\pi}$$
    $$v_i(t) = \sum_{n=1}^{\infty} \left(-\frac{2}{n\pi}\right) \sin(n 2\pi t)$$

2.  **Apply the Band-Pass Filter:**
    The filter only allows angular frequencies $\omega_n$ between 15 rad/s and 35 rad/s to pass unmodified. 
    Let's check the harmonic frequencies $\omega_n = n\omega_0 = n(2\pi) \approx 6.283n$ rad/s:
    *   $n=1$: $\omega_1 \approx 6.28$ rad/s (Rejected)
    *   $n=2$: $\omega_2 \approx 12.57$ rad/s (Rejected)
    *   $n=3$: $\omega_3 \approx 18.85$ rad/s **(Passed)**
    *   $n=4$: $\omega_4 \approx 25.13$ rad/s **(Passed)**
    *   $n=5$: $\omega_5 \approx 31.42$ rad/s **(Passed)**
    *   $n=6$: $\omega_6 \approx 37.70$ rad/s (Rejected)
    
3.  **Determine the Filter Output:**
    Only the 3rd, 4th, and 5th harmonics fall within the passband ($15 < \omega < 35$) and appear at the output. 
    $$v_o(t) = \sum_{n=3}^{5} -\frac{2}{n\pi} \sin(n 2\pi t)$$
    Expanded out:
    $$v_o(t) = -\frac{2}{3\pi} \sin(6\pi t) - \frac{2}{4\pi} \sin(8\pi t) - \frac{2}{5\pi} \sin(10\pi t)$$

*Ans related location: Sadiku Textbook, Chapter 17 (The Fourier Series), Section 17.8.2 (Filters), pg. 797-799.*

***

### 3. 4. Page 18, Q.4(a): If the periodic voltage as shown in the following figure is applied to the following network; Draw the frequency spectrum of $i_0(t)$. [Figure involved.]

**Problem Statement:**
A periodic rectangular pulse train $v_s(t)$ is applied to a circuit. Find the amplitude spectrum of the current $i_0(t)$.
*   $v_s(t)$ alternates between $7.5$ V and $2.5$ V with a period $T = 2$ s.
*   The network is a $20 \Omega$ resistor in series with two parallel branches: a $50 \text{ mF}$ capacitor and a series combination of a $40 \Omega$ resistor and $100 \text{ mH}$ inductor. $i_0(t)$ is the current through the inductor branch.

**Solution:**
1.  **Fourier Series of Input Voltage:**
    Period $T = 2 \text{ s} \implies \omega_0 = \frac{2\pi}{2} = \pi \text{ rad/s}$.
    The DC component $V_{s0}$ is the average value: $V_{s0} = \frac{7.5 + 2.5}{2} = 5$ V.
    The AC component is a square wave alternating between $+2.5$ V and $-2.5$ V. Its Fourier series is:
    $$v_{s,ac}(t) = \frac{4(2.5)}{\pi} \sum_{n=1,3,5...}^{\infty} \frac{1}{n} \sin(n\pi t) = \sum_{n=odd}^{\infty} \frac{10}{n\pi} \sin(n\pi t)$$
    $$v_s(t) = 5 + \sum_{n=1,3,5...}^{\infty} \frac{10}{n\pi} \sin(n\pi t) \text{ V}$$

2.  **Network Transfer Function $H(\omega) = \frac{I_0(\omega)}{V_s(\omega)}$:**
    Circuit values: $R_1 = 20 \Omega$, $C = 0.05$ F, $R_2 = 40 \Omega$, $L = 0.1$ H.
    The impedance of the parallel combination ($Z_p$) is:
    $$Z_p = \frac{Z_C Z_{RL}}{Z_C + Z_{RL}} = \frac{(1/j\omega C)(R_2 + j\omega L)}{1/j\omega C + R_2 + j\omega L} = \frac{R_2 + j\omega L}{1 + j\omega R_2 C - \omega^2 LC}$$
    By current division and Ohm's law, the current $I_0$ through the $R_2-L$ branch is:
    $$I_0(\omega) = \frac{V_s(\omega)}{R_1 + Z_p} \cdot \frac{Z_C}{Z_C + Z_{RL}} = V_s(\omega) \frac{1}{R_1 \frac{Z_C + Z_{RL}}{Z_C} + Z_{RL}} = V_s(\omega) \frac{1}{R_1(1 + j\omega R_2 C - \omega^2 LC) + R_2 + j\omega L}$$
    Substitute the numerical values:
    $$R_1 + R_2 = 20 + 40 = 60$$
    $$R_1 L C = 20 \times 0.1 \times 0.05 = 0.1$$
    $$R_1 R_2 C + L = 20 \times 40 \times 0.05 + 0.1 = 40 + 0.1 = 40.1$$
    $$H(\omega) = \frac{1}{(60 - 0.1\omega^2) + j\omega(40.1)}$$

3.  **Amplitude Spectrum Calculation:**
    The current amplitude for each harmonic $n$ is $|I_0(n\omega_0)| = |H(n\pi)| \cdot |V_{sn}|$.
    
    *   **DC Component ($n=0$, $\omega = 0$):**
        $|H(0)| = \frac{1}{60}$
        $I_{0,0} = 5 \text{ V} \times \frac{1}{60} = \frac{1}{12} \text{ A} \approx 0.0833 \text{ A}$
        
    *   **1st Harmonic ($n=1$, $\omega = \pi \approx 3.14$):**
        $|V_{s,1}| = \frac{10}{\pi} \approx 3.183$ V
        $|H(\pi)| = \frac{1}{\sqrt{(60 - 0.1\pi^2)^2 + (40.1\pi)^2}} = \frac{1}{\sqrt{59.01^2 + 125.98^2}} \approx \frac{1}{139.1} \approx 0.00719$
        $|I_{0,1}| = 3.183 \times 0.00719 \approx 0.0229 \text{ A}$

    *   **3rd Harmonic ($n=3$, $\omega = 3\pi \approx 9.42$):**
        $|V_{s,3}| = \frac{10}{3\pi} \approx 1.061$ V
        $|H(3\pi)| = \frac{1}{\sqrt{(60 - 0.1(9\pi^2))^2 + (40.1(3\pi))^2}} = \frac{1}{\sqrt{51.12^2 + 377.9^2}} \approx \frac{1}{381.4} \approx 0.00262$
        $|I_{0,3}| = 1.061 \times 0.00262 \approx 0.0028 \text{ A}$

    *   **5th Harmonic ($n=5$, $\omega = 5\pi \approx 15.71$):**
        $|V_{s,5}| = \frac{10}{5\pi} \approx 0.637$ V
        $|H(5\pi)| = \frac{1}{\sqrt{(60 - 0.1(25\pi^2))^2 + (40.1(5\pi))^2}} = \frac{1}{\sqrt{35.3^2 + 629.9^2}} \approx \frac{1}{630.9} \approx 0.00158$
        $|I_{0,5}| = 0.637 \times 0.00158 \approx 0.0010 \text{ A}$

    **Frequency Spectrum Plot:** The frequency spectrum graph will have discrete spikes located at $\omega = 0, \pi, 3\pi, 5\pi...$ rad/s. The amplitudes drop rapidly: a strong DC spike at $\approx 0.083$ A, a smaller 1st harmonic at $\approx 0.023$ A, and virtually negligible 3rd and 5th harmonics at $\approx 0.0028$ A and $0.0010$ A.

*Ans related location: Sadiku Textbook, Chapter 17 (The Fourier Series), Section 17.6 (Exponential Fourier Series/Amplitude Spectrum), pg. 786-788.*

Based on the provided document, here are the step-by-step solutions for the next four questions (Questions 5 to 8).

### 5. Page 21, Q.5(c): Find $v_0(t)$ in the circuit given in Fig. Q. 5(c) for $v_i(t) = 2e^{-3t}u(t)$ using Fourier Transform.

**Problem Statement:**
Find the output voltage $v_0(t)$ across the capacitor in the provided RC low-pass filter circuit using the Fourier transform method. 
*From Fig. Q. 5(c), we observe a series resistor $R = 2\ \Omega$ and a shunt capacitor $C = 1\text{ F}$.*

**Solution:**
**Step 1: Find the Fourier Transform of the input.**
The input voltage in the time domain is $v_i(t) = 2e^{-3t}u(t)$. 
Using standard Fourier transform pairs, its frequency-domain representation is:
$$V_i(\omega) = \mathcal{F}\{2e^{-3t}u(t)\} = \frac{2}{3 + j\omega}$$

**Step 2: Determine the Transfer Function $H(\omega)$.**
The circuit is a voltage divider. The output voltage $V_0(\omega)$ is taken across the capacitor.
The impedance of the resistor is $Z_R = R = 2\ \Omega$.
The impedance of the capacitor is $Z_C = \frac{1}{j\omega C} = \frac{1}{j\omega (1)} = \frac{1}{j\omega}\ \Omega$.
The transfer function $H(\omega) = \frac{V_0(\omega)}{V_i(\omega)}$ is:
$$H(\omega) = \frac{Z_C}{Z_R + Z_C} = \frac{\frac{1}{j\omega}}{2 + \frac{1}{j\omega}} = \frac{1}{1 + j2\omega}$$
To make it easier to work with, divide the numerator and denominator by 2:
$$H(\omega) = \frac{0.5}{0.5 + j\omega}$$

**Step 3: Calculate the Output in the Frequency Domain.**
Multiply the transfer function by the input transform:
$$V_0(\omega) = H(\omega) \cdot V_i(\omega) = \left( \frac{0.5}{0.5 + j\omega} \right) \left( \frac{2}{3 + j\omega} \right) = \frac{1}{(0.5 + j\omega)(3 + j\omega)}$$

**Step 4: Use Partial Fraction Expansion.**
Let $s = j\omega$ to simplify the algebra:
$$V_0(s) = \frac{1}{(s + 0.5)(s + 3)} = \frac{A}{s + 0.5} + \frac{B}{s + 3}$$
Using the cover-up method (residues):
$$A = \left. \frac{1}{s + 3} \right|_{s = -0.5} = \frac{1}{2.5} = 0.4$$
$$B = \left. \frac{1}{s + 0.5} \right|_{s = -3} = \frac{1}{-2.5} = -0.4$$
Substituting back $s = j\omega$:
$$V_0(\omega) = \frac{0.4}{0.5 + j\omega} - \frac{0.4}{3 + j\omega}$$

**Step 5: Find the Inverse Fourier Transform.**
Transforming back to the time domain using the standard pair $\mathcal{F}^{-1}\left\{ \frac{1}{a + j\omega} \right\} = e^{-at}u(t)$:
$$v_0(t) = 0.4 e^{-0.5t}u(t) - 0.4 e^{-3t}u(t)\text{ V}$$
$$v_0(t) = 0.4(e^{-0.5t} - e^{-3t})u(t)\text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 18 (Fourier Transform), Section 18.4 (Circuit Applications), pg. 833-835.*

***

### 6. Page 64, Q(c): If the sawtooth waveform shown in following Fig. is applied to an filter with the given transfer function...

**(i) Find the Fourier series expansion of the sawtooth wave.**
**(ii) Determine the output of the filter.**

**Solution for (i): Fourier Series of the Sawtooth Wave**
From the graph $x(t)$, the sawtooth wave has a period of $T = 1\text{ s}$ and ranges from $-1$ to $1$. 
The fundamental frequency is $\omega_0 = \frac{2\pi}{T} = 2\pi\text{ rad/s}$.
Over one period $t \in [0, 1)$, the mathematical description of the line is:
$$x(t) = 2t - 1$$
We find the trigonometric Fourier series coefficients ($a_0, a_n, b_n$):
*   **DC Component ($a_0$):** Since the triangle is symmetrical above and below the x-axis, the average value is $0$. ($a_0 = 0$).
*   **Cosine Coefficients ($a_n$):** 
    $$a_n = \frac{2}{T}\int_{0}^{T} x(t)\cos(n\omega_0t)dt = 2\int_{0}^{1} (2t - 1)\cos(2\pi n t)dt = 0$$ (Due to shifted odd symmetry).
*   **Sine Coefficients ($b_n$):**
    $$b_n = \frac{2}{T}\int_{0}^{T} x(t)\sin(n\omega_0t)dt = 2\int_{0}^{1} (2t - 1)\sin(2\pi n t)dt$$
    Evaluating this integral using integration by parts gives $b_n = -\frac{2}{n\pi}$.
    
Therefore, the Fourier series expansion of the input is:
$$x(t) = \sum_{n=1}^{\infty} \left(-\frac{2}{n\pi}\right) \sin(2n\pi t)$$

**Solution for (ii): Determine the Output of the Filter**
The filter's magnitude response $|H(\omega)|$ is $0$ for $\omega < 10$ and $1$ for $\omega \geq 10$. This acts as an ideal high-pass filter with a cutoff frequency $\omega_c = 10\text{ rad/s}$. (Assuming zero phase shift).
We must determine which harmonics of the input signal pass through the filter. The harmonic frequencies are $\omega_n = n\omega_0 = 2\pi n \approx 6.28n\text{ rad/s}$.
*   $n=1: \omega_1 = 2\pi \approx 6.28\text{ rad/s} < 10$ **(Blocked)**
*   $n=2: \omega_2 = 4\pi \approx 12.57\text{ rad/s} > 10$ **(Passed)**
*   $n \geq 2:$ All higher harmonics are strictly greater than 10 rad/s and are **passed**.

The output $y(t)$ is simply the input Fourier series minus the blocked 1st harmonic:
$$y(t) = \sum_{n=2}^{\infty} \left(-\frac{2}{n\pi}\right) \sin(2n\pi t)$$

*Ans related location: Sadiku Textbook, Chapter 17 (The Fourier Series), Section 17.8.2 (Filters), pg. 797-799.*

***

### 7. Page 67, Q(b): Using the Fourier transform method, find the response $v_0(t)$ of the following circuit shown in Fig. 6(b), when (i) $v_{in}(t) = \delta(t)$ and (ii) $v_{in}(t) = \sin(t)$.

**Problem Statement:**
The circuit is a voltage divider with a series resistor $R = 1\ \Omega$ and a capacitor $C = 1\text{ F}$. The output $v_0(t)$ is taken across the capacitor.

**Solution:**
**Step 1: Determine the Transfer Function $H(\omega)$.**
$$H(\omega) = \frac{V_0(\omega)}{V_{in}(\omega)} = \frac{1/(j\omega C)}{R + 1/(j\omega C)} = \frac{1}{1 + j\omega RC}$$
Substituting $R = 1\ \Omega$ and $C = 1\text{ F}$:
$$H(\omega) = \frac{1}{1 + j\omega}$$

**(i) For $v_{in}(t) = \delta(t)$:**
The Fourier transform of the unit impulse function is $\mathcal{F}\{\delta(t)\} = 1$.
$$V_0(\omega) = H(\omega) \cdot V_{in}(\omega) = \frac{1}{1 + j\omega} \cdot 1 = \frac{1}{1 + j\omega}$$
Taking the inverse Fourier transform:
$$v_0(t) = e^{-t}u(t)\text{ V}$$
*(Note: This is the impulse response $h(t)$ of the circuit.)*

**(ii) For $v_{in}(t) = \sin(t)$:**
The Fourier transform of $\sin(\omega_0 t)$ (where $\omega_0 = 1$) is:
$$V_{in}(\omega) = j\pi [\delta(\omega + 1) - \delta(\omega - 1)]$$
Multiply by the transfer function:
$$V_0(\omega) = H(\omega) V_{in}(\omega) = \frac{1}{1 + j\omega} \left( j\pi [\delta(\omega + 1) - \delta(\omega - 1)] \right)$$
Apply the sifting property of the Dirac delta function ($f(\omega)\delta(\omega - \omega_0) = f(\omega_0)\delta(\omega - \omega_0)$):
$$V_0(\omega) = j\pi \left[ \frac{1}{1 + j(-1)}\delta(\omega + 1) - \frac{1}{1 + j(1)}\delta(\omega - 1) \right]$$
$$V_0(\omega) = j\pi \left[ \frac{1}{1 - j}\delta(\omega + 1) - \frac{1}{1 + j}\delta(\omega - 1) \right]$$
Rationalizing the complex fractions ($\frac{1}{1-j} = \frac{1+j}{2}$ and $\frac{1}{1+j} = \frac{1-j}{2}$):
$$V_0(\omega) = j\pi \left[ \frac{1+j}{2}\delta(\omega + 1) - \frac{1-j}{2}\delta(\omega - 1) \right]$$
$$V_0(\omega) = \frac{\pi}{2} \left[ (j-1)\delta(\omega + 1) - (j+1)\delta(\omega - 1) \right]$$
Rearranging into standard Fourier pairs for sine and cosine:
$$V_0(\omega) = -\frac{\pi}{2}[\delta(\omega - 1) + \delta(\omega + 1)] - \frac{j\pi}{2}[\delta(\omega + 1) - \delta(\omega - 1)]$$
Taking the inverse Fourier Transform yields:
$$v_0(t) = -\frac{1}{2}\cos(t) + \frac{1}{2}\sin(t)\text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 18 (Fourier Transform), Section 18.4 (Circuit Applications), pg. 833-835.*

***

### 8. Page 6, Q.3(b): Consider the following second-order circuit
**(i) Find the value of R so that critically damped response is obtained.**
**(ii) Determine the response $v_0(t)$ if $v_s(t) = 10u(t)$ and $R = 1\ \Omega$.**

**Problem Statement:**
A series RLC circuit is driven by a voltage source $v_s(t)$. Components are $R$, $L = 2\text{ H}$, and $C = 1\text{ F}$. Output $v_0(t)$ is across the capacitor.

**Solution for (i): Value of R for Critical Damping**
For a series RLC circuit, the damping factor $\alpha$ and undamped natural frequency $\omega_0$ are defined as:
$$\alpha = \frac{R}{2L}, \quad \omega_0 = \frac{1}{\sqrt{LC}}$$
A critically damped response occurs when $\alpha = \omega_0$:
$$\frac{R}{2L} = \frac{1}{\sqrt{LC}} \implies R = 2\sqrt{\frac{L}{C}}$$
Substituting $L = 2\text{ H}$ and $C = 1\text{ F}$:
$$R = 2\sqrt{\frac{2}{1}} = 2\sqrt{2} \approx 2.828\ \Omega$$

**Solution for (ii): Response $v_0(t)$ if $v_s(t) = 10u(t)$ and $R = 1\ \Omega$**
This is a step response problem. For $t > 0$, the circuit is driven by a constant $10\text{ V}$ DC source. Assuming no initial stored energy, $v_0(0) = 0$ and $i(0) = 0$.

1.  **Determine the specific damping type:**
    With $R = 1\ \Omega$, $L = 2\text{ H}$, and $C = 1\text{ F}$:
    $$\alpha = \frac{1}{2(2)} = 0.25 \text{ Np/s}$$
    $$\omega_0 = \frac{1}{\sqrt{2(1)}} = \frac{1}{\sqrt{2}} \approx 0.707 \text{ rad/s}$$
    Since $\alpha < \omega_0$, the circuit is **underdamped**.
    The damped natural frequency is $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{\frac{1}{2} - \frac{1}{16}} = \sqrt{\frac{7}{16}} = \frac{\sqrt{7}}{4} \text{ rad/s}$.

2.  **Formulate the general solution:**
    The total response is the sum of the transient and steady-state responses: $v_0(t) = v_{ss}(t) + v_t(t)$.
    *   **Steady-state ($t \to \infty$):** The capacitor acts as an open circuit to DC, so $v_{ss} = 10\text{ V}$.
    *   **Transient:** For an underdamped system, $v_t(t) = e^{-\alpha t}(A \cos\omega_dt + B \sin\omega_dt)$.
    $$v_0(t) = 10 + e^{-0.25t}\left(A \cos\left(\frac{\sqrt{7}}{4}t\right) + B \sin\left(\frac{\sqrt{7}}{4}t\right)\right)$$

3.  **Apply initial conditions to find constants A and B:**
    *   $v_0(0) = 0$:
        $$0 = 10 + e^{0}(A \cos(0) + B \sin(0)) \implies 0 = 10 + A \implies A = -10$$
    *   $i(0) = 0$: Since $i(t) = C \frac{dv_0}{dt}$ and $C=1\text{ F}$, $\frac{dv_0}{dt}(0) = 0$.
        Differentiating $v_0(t)$ and evaluating at $t=0$:
        $$\frac{dv_0}{dt} = e^{-0.25t} \left(-\frac{\sqrt{7}}{4}A \sin\left(\frac{\sqrt{7}}{4}t\right) + \frac{\sqrt{7}}{4}B \cos\left(\frac{\sqrt{7}}{4}t\right)\right) - 0.25e^{-0.25t}\left(A \cos\left(\frac{\sqrt{7}}{4}t\right) + B \sin\left(\frac{\sqrt{7}}{4}t\right)\right)$$
        $$\frac{dv_0}{dt}(0) = \frac{\sqrt{7}}{4}B - 0.25A = 0$$
        Substitute $A = -10$:
        $$\frac{\sqrt{7}}{4}B - 0.25(-10) = 0 \implies \frac{\sqrt{7}}{4}B + 2.5 = 0 \implies B = -\frac{10}{\sqrt{7}} \approx -3.78$$

4.  **Final Expression:**
    Substituting $A$ and $B$ back into the response equation:
    $$v_0(t) = \left[ 10 - e^{-0.25t} \left( 10\cos\left(\frac{\sqrt{7}}{4}t\right) + \frac{10}{\sqrt{7}}\sin\left(\frac{\sqrt{7}}{4}t\right) \right) \right] u(t)\text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.5 (Step Response of a Series RLC Circuit), pg. 331-336.*

Based on the provided document, here are the step-by-step solutions for the next four questions (Questions 9 to 12).

### 9. Page 11, Q.2(a): The responses of a series RLC circuit are $v_c(t) = 30 - 10e^{-20t} + 30e^{-10t} V$; $i_L(t) = 40e^{-20t} - 60e^{-10t} mA$; where $v_c(t)$ and $i_L(t)$ are the capacitor voltage and inductor current respectively. Determine the values of R, L, and C.

**Problem Statement:**
Find the resistance ($R$), inductance ($L$), and capacitance ($C$) of a series RLC circuit given its voltage and current responses.

**Solution:**
**Step 1: Find Capacitance ($C$)**
In a series RLC circuit, the current through the inductor is the same as the current through the capacitor. The fundamental relationship for a capacitor is:
$$i_C(t) = i_L(t) = C \frac{dv_c(t)}{dt}$$
First, find the derivative of the given capacitor voltage $v_c(t)$:
$$\frac{dv_c(t)}{dt} = \frac{d}{dt} (30 - 10e^{-20t} + 30e^{-10t})$$
$$\frac{dv_c(t)}{dt} = -10(-20)e^{-20t} + 30(-10)e^{-10t} = 200e^{-20t} - 300e^{-10t} \text{ V/s}$$
Now, equate this to the given inductor current (converted to Amperes):
$$i_L(t) = (40e^{-20t} - 60e^{-10t}) \times 10^{-3} \text{ A}$$
$$C(200e^{-20t} - 300e^{-10t}) = (40e^{-20t} - 60e^{-10t}) \times 10^{-3}$$
$$C(200e^{-20t} - 300e^{-10t}) = 10^{-3} \times 20 \times (2e^{-20t} - 3e^{-10t})$$
$$C \times 100 \times (2e^{-20t} - 3e^{-10t}) = 20 \times 10^{-3} \times (2e^{-20t} - 3e^{-10t})$$
Comparing the terms, we can solve for $C$:
$$C \times 100 = 20 \times 10^{-3} \implies C = \frac{20 \times 10^{-3}}{100} = 200 \times 10^{-6} \text{ F} = 200 \ \mu\text{F}$$

**Step 2: Use Characteristic Equation to find $L$ and $R$**
The transient part of the response contains the terms $e^{-20t}$ and $e^{-10t}$. These exponents represent the roots of the circuit's characteristic equation:
$$s_1 = -20 \text{ Np/s}, \quad s_2 = -10 \text{ Np/s}$$
For a series RLC circuit, the characteristic equation is:
$$s^2 + \frac{R}{L}s + \frac{1}{LC} = 0$$
Using the roots, we can also construct the characteristic equation as:
$$(s - s_1)(s - s_2) = (s + 20)(s + 10) = s^2 + 30s + 200 = 0$$
By matching the coefficients of the two forms of the characteristic equation:
1.  $\frac{1}{LC} = 200$
2.  $\frac{R}{L} = 30$

**Step 3: Solve for $L$**
Using the first coefficient relation and the calculated value of $C$:
$$\frac{1}{L(200 \times 10^{-6})} = 200$$
$$L = \frac{1}{200 \times 200 \times 10^{-6}} = \frac{1}{40000 \times 10^{-6}} = \frac{1}{0.04} = 25 \text{ H}$$

**Step 4: Solve for $R$**
Using the second coefficient relation and the calculated value of $L$:
$$\frac{R}{25} = 30 \implies R = 30 \times 25 = 750 \ \Omega$$

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.3 & 8.5, pg. 319-325, 331.*

***

### 10. Page 21, Q.6(a): Define i) Critically damped ii) Under damped iii) Over damped.

**Problem Statement:**
Provide definitions for the three types of damping in a second-order circuit.

**Solution:**
In a second-order circuit (like RLC circuits), the type of natural response is determined by the roots of its characteristic equation ($s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$). The terms depend on the relationship between the neper frequency (damping factor) $\alpha$ and the undamped natural frequency $\omega_0$.

*   **i) Overdamped:** A circuit is overdamped when the damping factor is strictly greater than the resonant frequency ($\alpha > \omega_0$). The characteristic equation has two distinct real roots. The response is a sum of two decaying exponentials and sluggishly decays to its steady-state value without any oscillation.
*   **ii) Critically damped:** A circuit is critically damped when the damping factor is exactly equal to the resonant frequency ($\alpha = \omega_0$). The characteristic equation has two identical, real roots (repeated roots). This represents the boundary between oscillatory and non-oscillatory responses and it is the condition that allows the response to reach its steady-state value in the shortest possible time without overshooting.
*   **iii) Underdamped:** A circuit is underdamped when the damping factor is strictly less than the resonant frequency ($\alpha < \omega_0$). The characteristic equation has two complex conjugate roots. The response is an exponentially decaying sinusoidal oscillation (often referred to as ringing) before settling to its steady-state value.

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.3, pg. 321.*

***

### 11. Page 27, Q (Handwritten top): there is a parallel RLC circuit (without source) with $R = 1k\Omega$ & $v_c(t) = 10e^{-2000t} - 2000te^{-2000t} V$.
**(i) find the type of damping.**
**(ii) characteristic eqn.**
**(iii) find the value of C & L.**
**(iv) find the $i_R(t)$.**
**(v) capacitor voltage.**

**Solution:**
**(i) Type of damping:**
The expression for the voltage $v_c(t)$ is in the form $(A_1 + A_2t)e^{-\alpha t}$. The presence of the $t$ multiplied by the exponential indicates that the characteristic equation has repeated real roots. Therefore, the circuit is **Critically Damped**.

**(ii) Characteristic equation:**
From the exponential term $e^{-2000t}$, we can identify that the repeated root is $s_1 = s_2 = -2000$.
The characteristic equation can be constructed from its roots:
$$(s - s_1)(s - s_2) = (s + 2000)(s + 2000) = (s + 2000)^2 = 0$$
Expanding this gives the characteristic equation:
$$s^2 + 4000s + 4000000 = 0$$

**(iii) Find the value of C & L:**
For a source-free parallel RLC circuit, the standard characteristic equation is:
$$s^2 + \frac{1}{RC}s + \frac{1}{LC} = 0$$
Comparing the coefficients with our equation from part (ii):
1.  $\frac{1}{RC} = 4000$
2.  $\frac{1}{LC} = 4000000$

Given $R = 1 \text{ k}\Omega = 1000 \ \Omega$, we can find $C$:
$$\frac{1}{1000 \cdot C} = 4000 \implies C = \frac{1}{4000 \times 1000} = \frac{1}{4 \times 10^6} = 0.25 \times 10^{-6} \text{ F} = 0.25 \ \mu\text{F}$$
Now find $L$ using the second coefficient:
$$\frac{1}{L \cdot (0.25 \times 10^{-6})} = 4000000 \implies L = \frac{1}{4 \times 10^6 \times 0.25 \times 10^{-6}} = \frac{1}{1} = 1 \text{ H}$$

**(iv) Find $i_R(t)$:**
Using Ohm's law, the current through the resistor is the voltage across it divided by its resistance. In a parallel circuit, the voltage across all elements is the same, so $v_R(t) = v_c(t)$.
$$i_R(t) = \frac{v_c(t)}{R} = \frac{10e^{-2000t} - 2000te^{-2000t}}{1000}$$
$$i_R(t) = 0.01e^{-2000t} - 2te^{-2000t} \text{ A} \quad \text{or} \quad 10e^{-2000t} - 2000te^{-2000t} \text{ mA}$$

**(v) Capacitor voltage:**
This is explicitly given in the problem prompt.
$$v_c(t) = 10e^{-2000t} - 2000te^{-2000t} \text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.4 (The Source-Free Parallel RLC Circuit), pg. 326-327.*

***

### 12. Page 44, Q2: For the following circuit, Find [Figure involved]
**(i) Transfer function.**
**(ii) Impulse response.**
**(iii) Output $i_0(t)$ if $i_s(t) = e^{-2t}$.**

**Problem Statement:**
A parallel RL circuit is driven by a current source $i_s(t)$. The resistor is $R=1\ \Omega$ and the inductor is $L=1\text{ H}$. The output is the current through the inductor, $i_0(t)$.

**Solution:**
**(i) Transfer function $H(s)$:**
First, transform the circuit to the s-domain.
*   Resistance: $Z_R = R = 1\ \Omega$
*   Inductance: $Z_L = sL = s(1) = s\ \Omega$

The transfer function is defined as the ratio of the output to the input in the s-domain, assuming zero initial conditions: $H(s) = \frac{I_0(s)}{I_s(s)}$.
Applying the current division principle to the parallel branches:
$$I_0(s) = I_s(s) \frac{Z_R}{Z_R + Z_L}$$
$$I_0(s) = I_s(s) \frac{1}{1 + s}$$
Therefore, the transfer function is:
$$H(s) = \frac{1}{s + 1}$$

**(ii) Impulse response $h(t)$:**
The impulse response is the inverse Laplace transform of the transfer function:
$$h(t) = \mathcal{L}^{-1} \{H(s)\} = \mathcal{L}^{-1} \left\{ \frac{1}{s + 1} \right\}$$
Using standard Laplace transform pairs:
$$h(t) = e^{-t}u(t)$$

**(iii) Output $i_0(t)$ if $i_s(t) = e^{-2t}$:**
First, find the Laplace transform of the input current (assuming it's $e^{-2t}u(t)$ based on standard causal system problems):
$$I_s(s) = \mathcal{L} \{e^{-2t}u(t)\} = \frac{1}{s + 2}$$
The output in the s-domain is the product of the transfer function and the input:
$$I_0(s) = H(s) \cdot I_s(s) = \left( \frac{1}{s + 1} \right) \left( \frac{1}{s + 2} \right) = \frac{1}{(s + 1)(s + 2)}$$
To find the time-domain output, perform partial fraction expansion:
$$I_0(s) = \frac{A}{s + 1} + \frac{B}{s + 2}$$
Using the cover-up method (residues):
*   $A = \left. \frac{1}{s + 2} \right|_{s = -1} = \frac{1}{-1 + 2} = 1$
*   $B = \left. \frac{1}{s + 1} \right|_{s = -2} = \frac{1}{-2 + 1} = -1$

So, the partial fraction expansion is:
$$I_0(s) = \frac{1}{s + 1} - \frac{1}{s + 2}$$
Taking the inverse Laplace transform yields the output current:
$$i_0(t) = \mathcal{L}^{-1} \left\{ \frac{1}{s + 1} - \frac{1}{s + 2} \right\}$$
$$i_0(t) = (e^{-t} - e^{-2t})u(t) \text{ A}$$

*Ans related location: Sadiku Textbook, Chapter 16 (Applications of the Laplace Transform), Section 16.4 (Transfer Functions), pg. 726-728.*

Based on the provided document, here are the step-by-step solutions for the next four questions (Questions 13 to 16).

### 13. Page 48, Q.1(a) (Middle): A linear circuit is described by $4\frac{dv}{dt} + v = 10$. (i) Determine the time constant of the circuit. (ii) Determine $v(\infty)$, the final value of $v$ and (iii) If $v(0) = 2$, find $v(t)$ for $t \ge 0$.

**Problem Statement:**
Analyze the given first-order differential equation for a linear circuit to find its time constant, steady-state (final) value, and the complete time-domain response given an initial condition.

**Solution:**
**(i) Determine the time constant ($\tau$):**
The standard form of a first-order differential equation for a step response is:
$$\tau \frac{dv(t)}{dt} + v(t) = V_s$$
Comparing the given equation $4\frac{dv}{dt} + v = 10$ to the standard form, we can directly identify the time constant:
$$\tau = 4 \text{ seconds}$$

**(ii) Determine $v(\infty)$, the final value of $v$:**
At steady state (as $t \to \infty$), the voltage reaches a constant value. Therefore, the rate of change of the voltage with respect to time becomes zero ($\frac{dv}{dt} = 0$).
Substituting this into the differential equation:
$$4(0) + v(\infty) = 10$$
$$v(\infty) = 10 \text{ V}$$

**(iii) If $v(0) = 2$, find $v(t)$ for $t \ge 0$:**
The complete response of a first-order circuit is given by the formula:
$$v(t) = v(\infty) + [v(0) - v(\infty)]e^{-t/\tau}$$
Substitute the known values ($v(\infty) = 10$, $v(0) = 2$, and $\tau = 4$):
$$v(t) = 10 + [2 - 10]e^{-t/4}$$
$$v(t) = 10 - 8e^{-0.25t} \text{ V}$$

*Ans related location: Sadiku Textbook, Chapter 7 (First-Order Circuits), Section 7.5 (Step Response of an RC Circuit), pg. 273-276.*

***

### 14. Page 51, Q(b) (Middle): For a source free series RLC circuit, sketch the current $i(t)$ when (i) $R > 2\sqrt{L/C}$ (ii) $R < 2\sqrt{L/C}$ and (iii) $R = 2\sqrt{L/C}$. At what values of above R the current $i(t)$ reaches at steady state in short period of time?

**Problem Statement:**
Describe the current sketches for the three damping conditions of a source-free series RLC circuit and identify which condition reaches steady state the fastest.

**Solution:**
For a series RLC circuit, the damping factor is $\alpha = \frac{R}{2L}$ and the resonant frequency is $\omega_0 = \frac{1}{\sqrt{LC}}$. The damping conditions depend on the relationship between $\alpha$ and $\omega_0$.
*   **(i) $R > 2\sqrt{L/C}$ (Overdamped):** Here, $\alpha > \omega_0$. The roots are real and negative. The current $i(t)$ rises to a single, relatively broad peak and then decays very sluggishly to zero without crossing the time axis (no oscillation).
*   **(ii) $R < 2\sqrt{L/C}$ (Underdamped):** Here, $\alpha < \omega_0$. The roots are complex conjugates. The current $i(t)$ exhibits a damped sinusoidal oscillation (ringing). It rises, crosses the zero axis multiple times, and the amplitude of these oscillations decays exponentially to zero.
*   **(iii) $R = 2\sqrt{L/C}$ (Critically Damped):** Here, $\alpha = \omega_0$. The roots are real and repeated. The current $i(t)$ rises to a peak and then decays rapidly to zero without oscillating. 

**Sketch Descriptions:** (If drawn on a graph with $i(t)$ vs. $t$, assuming $i(0)=0$ and initial capacitor voltage kicks off the current):
*   *Overdamped curve:* A slow, wide mound that takes a long time to flatline at zero.
*   *Underdamped curve:* A wave that goes up, then dips below zero, bouncing back and forth while shrinking in height until it settles at zero.
*   *Critically damped curve:* A sharp, narrow mound that returns to the zero line faster than the overdamped case and without dipping below zero like the underdamped case.

**Shortest time to steady state:**
The current $i(t)$ reaches steady state (decays to zero) in the shortest period of time under the **critically damped** condition, which occurs when **$R = 2\sqrt{L/C}$**.

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.3 (The Source-Free Series RLC Circuit), pg. 319-324.*

***

### 15. Page 51, Q(c): For the following circuit, express the time constant, $\tau$ in terms of $\beta$. Also find the range of $\beta$ for which $\tau$ becomes negative. Sketch $v_c(t)$ if $\beta = 3$. Assume $v_c(0) = 2V$. [Figure Involved]

**Problem Statement:**
Given an RC circuit containing a dependent current source, find the time constant $\tau$, the stability condition for $\beta$, and the response $v_c(t)$.
*From the figure:* The circuit consists of a $2 \ \Omega$ resistor, a dependent current source pointing upwards with value $\beta v_a$, a $1 \ \Omega$ resistor with voltage $v_a$ marked across it ($- \text{ left}, + \text{ right}$), and a $1 \text{ F}$ capacitor with voltage $v_c$ across it.

**Solution:**
**1. Express the time constant $\tau$ in terms of $\beta$:**
Let's assign node voltages. Let the top-left node (above the $2 \ \Omega$ resistor and dependent source) be $V_1$. Let the top-right node (above the capacitor) be $V_c$. The bottom wire is the reference node (Ground, $0\text{V}$).
The $1 \ \Omega$ resistor is connected between $V_1$ and $V_c$. The voltage $v_a$ is defined as the potential difference across this resistor. The $- $ is on the $V_1$ side and the $+$ is on the $V_c$ side. Therefore:
$$v_a = V_c - V_1$$

Apply Kirchhoff's Current Law (KCL) at node $V_1$:
$$\frac{V_1}{2} - \beta v_a + \frac{V_1 - V_c}{1} = 0$$
Substitute $v_a = V_c - V_1$:
$$\frac{V_1}{2} - \beta(V_c - V_1) + V_1 - V_c = 0$$
$$0.5 V_1 - \beta V_c + \beta V_1 + V_1 - V_c = 0$$
Group the $V_1$ and $V_c$ terms:
$$V_1(1.5 + \beta) = V_c(1 + \beta) \implies V_1 = V_c \left( \frac{\beta + 1}{\beta + 1.5} \right)$$

Apply KCL at node $V_c$:
$$C\frac{dV_c}{dt} + \frac{V_c - V_1}{1} = 0$$
Given $C = 1 \text{ F}$:
$$\frac{dV_c}{dt} + V_c - V_1 = 0$$
Substitute the expression for $V_1$:
$$\frac{dV_c}{dt} + V_c - V_c \left( \frac{\beta + 1}{\beta + 1.5} \right) = 0$$
$$\frac{dV_c}{dt} + V_c \left( \frac{(\beta + 1.5) - (\beta + 1)}{\beta + 1.5} \right) = 0$$
$$\frac{dV_c}{dt} + V_c \left( \frac{0.5}{\beta + 1.5} \right) = 0$$
This is in the standard first-order form $\frac{dV_c}{dt} + \frac{1}{\tau}V_c = 0$. Therefore, the time constant is:
$$\tau = \frac{\beta + 1.5}{0.5} = 2\beta + 3 \text{ seconds}$$

**2. Find the range of $\beta$ for which $\tau$ becomes negative:**
For $\tau < 0$:
$$2\beta + 3 < 0 \implies 2\beta < -3 \implies \beta < -1.5$$

**3. Sketch $v_c(t)$ if $\beta = 3$. Assume $v_c(0) = 2V$:**
If $\beta = 3$, calculate the specific time constant:
$$\tau = 2(3) + 3 = 9 \text{ seconds}$$
The response for a source-free RC circuit is:
$$v_c(t) = v_c(0)e^{-t/\tau} = 2e^{-t/9} \text{ V for } t \ge 0$$
*Sketch description:* Plot a graph with time $t$ on the x-axis and voltage $v_c(t)$ on the y-axis. The curve starts at the y-intercept $(0, 2\text{V})$ and decays exponentially towards zero as $t \to \infty$. At $t = 9\text{s}$ (one time constant), the voltage will have dropped to approximately $36.8\%$ of its initial value, which is $2 \times 0.368 \approx 0.736\text{ V}$.

*Ans related location: Sadiku Textbook, Chapter 7 (First-Order Circuits), Section 7.2 (The Source-Free RC Circuit), pg. 254-259.*

***

### 16. Page 54, Q.2(a): Explain under-damped system with a suitable example.

**Problem Statement:**
Define what constitutes an under-damped system and provide a relevant circuit example to illustrate the concept.

**Solution:**
**Explanation of an Under-Damped System:**
An under-damped system is a second-order system in which the system's energy dissipation (damping) is low enough that the system oscillates before settling into its final steady-state value. 
Mathematically, this occurs when the damping factor ($\alpha$) is strictly less than the undamped natural frequency ($\omega_0$), i.e., $\alpha < \omega_0$. Because of this, the roots of the system's characteristic equation ($s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$) are complex conjugates. 
The physical response of an under-damped circuit to a disturbance (like a step input or initial stored energy) is an exponentially decaying sinusoidal wave. The energy bounces back and forth between the energy storage elements (inductor and capacitor) while being gradually dissipated by the resistor.

**Suitable Example:**
Consider a source-free **Series RLC Circuit** with the following component values:
*   Inductor $L = 1 \text{ H}$
*   Capacitor $C = 1 \text{ F}$
*   Resistor $R = 1 \ \Omega$

Let's calculate the system parameters:
1.  **Damping factor ($\alpha$):** For a series RLC circuit, $\alpha = \frac{R}{2L} = \frac{1}{2(1)} = 0.5 \text{ Np/s}$.
2.  **Undamped natural frequency ($\omega_0$):** $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 1}} = 1 \text{ rad/s}$.

Since $\alpha = 0.5$ is less than $\omega_0 = 1$, the condition $\alpha < \omega_0$ is met. Therefore, this specific circuit is **under-damped**.

If there was an initial voltage on the capacitor, the resulting current $i(t)$ would oscillate back and forth (ringing) at the damped natural frequency $\omega_d = \sqrt{1^2 - 0.5^2} = 0.866 \text{ rad/s}$ while its peaks exponentially shrink according to the envelope $e^{-0.5t}$.

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.3 (The Source-Free Series RLC Circuit), pg. 321-323.*

Based on the provided document, here are the step-by-step solutions for the next four questions (Questions 17 to 20).

### 17. Page 54, Q (Middle): If $R = 50\Omega, L = 1.5H$, what value of C will make an RLC series circuit: (i) Overdamped (ii) Critically damped (iii) Underdamped?

**Problem Statement:**
Determine the required capacitance $C$ to achieve different damping conditions in a series RLC circuit given the resistance and inductance.

**Solution:**
For a series RLC circuit, the type of damping is determined by comparing the neper frequency (damping factor) $\alpha$ and the undamped natural frequency $\omega_0$.
The formulas for these parameters in a series RLC circuit are:
$$\alpha = \frac{R}{2L}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

Given values:
$R = 50\ \Omega$
$L = 1.5\text{ H}$

First, calculate the damping factor $\alpha$:
$$\alpha = \frac{50}{2(1.5)} = \frac{50}{3} \approx 16.667 \text{ Np/s}$$

**(i) Overdamped Condition:**
A circuit is overdamped when $\alpha > \omega_0$.
$$\alpha > \frac{1}{\sqrt{LC}} \implies \alpha^2 > \frac{1}{LC} \implies C > \frac{1}{L \alpha^2}$$
Substitute the known values:
$$C > \frac{1}{1.5 \times \left(\frac{50}{3}\right)^2}$$
$$C > \frac{1}{1.5 \times \frac{2500}{9}} = \frac{1}{\frac{3750}{9}} = \frac{9}{3750} \text{ F}$$
$$C > 0.0024 \text{ F} \implies C > 2.4 \text{ mF}$$

**(ii) Critically Damped Condition:**
A circuit is critically damped when $\alpha = \omega_0$.
$$C = \frac{1}{L \alpha^2}$$
Using the calculation from part (i):
$$C = 0.0024 \text{ F} = 2.4 \text{ mF}$$

**(iii) Underdamped Condition:**
A circuit is underdamped when $\alpha < \omega_0$.
$$\alpha < \frac{1}{\sqrt{LC}} \implies \alpha^2 < \frac{1}{LC} \implies C < \frac{1}{L \alpha^2}$$
Using the calculation from part (i):
$$C < 0.0024 \text{ F} \implies C < 2.4 \text{ mF}$$

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.3 (The Source-Free Series RLC Circuit), pg. 320-322.*

***

### 18. Page 55, Q.6(a): Design the capacitance, C of the second order circuit shown in Fig. 6(a) so that it will produce critically damped response. [Figure Involved]

**Problem Statement:**
Find the value of $C$ for the provided parallel RLC circuit to achieve a critically damped response.
*From Fig. 6(a):* The circuit consists of a source (labeled $V_i(t) = \delta(t)$, but drawn with a current source symbol, which is standard for parallel RLC impulsive excitation), in parallel with an inductor $L = 2\text{ H}$, a resistor $R = 0.5\ \Omega$, and a capacitor $C$.

**Solution:**
Regardless of the excitation type (source-free or driven), the damping characteristics of the circuit are determined by its natural response parameters $\alpha$ and $\omega_0$.
For a **parallel RLC circuit**, the damping factor and resonant frequency are defined as:
$$\alpha = \frac{1}{2RC}$$
$$\omega_0 = \frac{1}{\sqrt{LC}}$$

For a **critically damped** response, the damping factor must equal the undamped natural frequency:
$$\alpha = \omega_0$$
$$\frac{1}{2RC} = \frac{1}{\sqrt{LC}}$$

Square both sides to eliminate the square root:
$$\frac{1}{4R^2C^2} = \frac{1}{LC}$$

Rearrange to solve for $C$:
$$LC = 4R^2C^2$$
$$L = 4R^2C$$
$$C = \frac{L}{4R^2}$$

Substitute the given component values ($L = 2\text{ H}$, $R = 0.5\ \Omega$):
$$C = \frac{2}{4(0.5)^2} = \frac{2}{4(0.25)} = \frac{2}{1} = 2\text{ F}$$

Therefore, the capacitance must be $2\text{ F}$ to produce a critically damped response.

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.4 (The Source-Free Parallel RLC Circuit), pg. 326-327.*

***

### 19. Page 2, Q.2(c): Switch $S_1$ in the following Fig. is closed at t = 0 and $S_2$ is closed at t = 3s. Calculate $i(t)$ for all t. Also find $i(2)$ and $i(4)$. [Figure Involved]

**Problem Statement:**
Analyze a first-order RL circuit with sequential switching.
*From the figure:* A $6\text{ A}$ current source is in parallel with a $15\ \Omega$ resistor. Switch $S_1$ connects this source combination to the rest of the circuit at $t=0$. The rest of the circuit consists of a series $10\ \Omega$ resistor, followed by a $20\ \Omega$ resistor that has a switch $S_2$ in parallel with it (closing at $t=3\text{s}$), and finally a $5\text{ H}$ inductor to ground. The current $i(t)$ is through the inductor.

**Solution:**
First, let's convert the current source and its parallel $15\ \Omega$ resistor into a Thevenin equivalent to simplify the series circuit analysis:
*   $V_{th} = I_s \times R_p = 6\text{ A} \times 15\ \Omega = 90\text{ V}$
*   $R_{th} = 15\ \Omega$
The circuit is now a $90\text{ V}$ source in series with $15\ \Omega$, $S_1$, $10\ \Omega$, the ($20\ \Omega$ || $S_2$) block, and the $5\text{ H}$ inductor.

**Phase 1: $t < 0$**
Switch $S_1$ is open. No current reaches the inductor.
$$i(0^-) = 0\text{ A}$$

**Phase 2: $0 \le t < 3$ seconds**
Switch $S_1$ closes. Switch $S_2$ remains open. The total series resistance is:
$$R_{eq1} = 15\ \Omega + 10\ \Omega + 20\ \Omega = 45\ \Omega$$
The time constant for this interval is:
$$\tau_1 = \frac{L}{R_{eq1}} = \frac{5}{45} = \frac{1}{9}\text{ s}$$
The steady-state current if this phase continued indefinitely would be:
$$i_1(\infty) = \frac{V_{th}}{R_{eq1}} = \frac{90\text{ V}}{45\ \Omega} = 2\text{ A}$$
The step response formula is $i(t) = i(\infty) + [i(0) - i(\infty)]e^{-t/\tau}$:
$$i(t) = 2 + (0 - 2)e^{-9t} = 2(1 - e^{-9t})\text{ A}, \quad \text{for } 0 \le t < 3$$

**Phase 3: $t \ge 3$ seconds**
Switch $S_2$ closes, shorting out the $20\ \Omega$ resistor.
The new total series resistance is:
$$R_{eq2} = 15\ \Omega + 10\ \Omega + 0\ \Omega = 25\ \Omega$$
The new time constant is:
$$\tau_2 = \frac{L}{R_{eq2}} = \frac{5}{25} = 0.2\text{ s}$$
The new steady-state current is:
$$i_2(\infty) = \frac{V_{th}}{R_{eq2}} = \frac{90\text{ V}}{25\ \Omega} = 3.6\text{ A}$$
The initial current for this new phase is the current at $t=3$ from the previous phase:
$$i(3) = 2(1 - e^{-9(3)}) = 2(1 - e^{-27}) \approx 2\text{ A} \quad \text{(since } e^{-27} \approx 0)$$
The step response for this phase (shifted by $t=3$) is $i(t) = i_2(\infty) + [i(3) - i_2(\infty)]e^{-(t-3)/\tau_2}$:
$$i(t) = 3.6 + (2 - 3.6)e^{-5(t-3)}$$
$$i(t) = 3.6 - 1.6e^{-5(t-3)}\text{ A}, \quad \text{for } t \ge 3$$

**Summary of $i(t)$:**
$$i(t) = \begin{cases} 
0 \text{ A} & t < 0 \\
2(1 - e^{-9t}) \text{ A} & 0 \le t < 3 \\
3.6 - 1.6e^{-5(t-3)} \text{ A} & t \ge 3 
\end{cases}$$

**Calculate $i(2)$ and $i(4)$:**
*   At $t = 2$, use the equation for $0 \le t < 3$:
    $$i(2) = 2(1 - e^{-9(2)}) = 2(1 - e^{-18}) \approx 2\text{ A}$$
*   At $t = 4$, use the equation for $t \ge 3$:
    $$i(4) = 3.6 - 1.6e^{-5(4-3)} = 3.6 - 1.6e^{-5} = 3.6 - 1.6(0.006738) \approx 3.6 - 0.01078 \approx 3.589\text{ A}$$

*Ans related location: Sadiku Textbook, Chapter 7 (First-Order Circuits), Section 7.6 (Step Response of an RL Circuit), pg. 280-284.*

***

### 20. Page 2, Q.3(b): A second order circuit is shown in the following Fig. where the switch was closed for a long time and is opened at $t = 0$ s. (i) Find $v_c(0-)$ and $i_L(0-)$ (ii) Find $v_c, t > 0$. (iii) Find the nature of the response. [Figure Involved]

**Problem Statement:**
Analyze a second-order circuit with a step change to find initial conditions, the transient response equation, and the damping nature.
*From the figure:* A $6\text{V}$ DC source is in series with a $2\ \Omega$ resistor, a $1\text{H}$ inductor, and a parallel pair consisting of a $1\text{F}$ capacitor and a branch with a $1\ \Omega$ resistor and a switch. The switch is in series with the $1\ \Omega$ resistor and opens at $t=0$.

**Solution:**
**(i) Find initial conditions $v_c(0-)$ and $i_L(0-)$:**
For $t < 0$, the switch is closed for a long time. The circuit reaches DC steady state.
In DC steady state, the inductor acts as a short circuit ($0\ \Omega$) and the capacitor acts as an open circuit ($\infty\ \Omega$).
The circuit simplifies to the $6\text{V}$ source driving the $2\ \Omega$ resistor in series with the $1\ \Omega$ resistor (since the switch is closed and the capacitor is open).
The inductor current $i_L$ is the total series current:
$$i_L(0-) = \frac{V_s}{R_{total}} = \frac{6\text{ V}}{2\ \Omega + 1\ \Omega} = \frac{6}{3} = 2\text{ A}$$
The capacitor is in parallel with the $1\ \Omega$ resistor, so its voltage is the voltage across the $1\ \Omega$ resistor:
$$v_c(0-) = i_L(0-) \times 1\ \Omega = 2\text{ A} \times 1\ \Omega = 2\text{ V}$$
Because energy cannot change instantaneously:
$$i_L(0^+) = 2\text{ A}, \quad v_c(0^+) = 2\text{ V}$$

**(ii) Find $v_c(t)$ for $t > 0$:**
For $t > 0$, the switch opens, disconnecting the $1\ \Omega$ resistor.
The circuit becomes a **series RLC circuit** driven by a $6\text{V}$ source, with $R = 2\ \Omega$, $L = 1\text{ H}$, and $C = 1\text{ F}$.
Let's find the steady-state final value of the capacitor voltage ($t \to \infty$):
The capacitor acts as an open circuit to DC again, so no current flows, and there is no voltage drop across the resistor or inductor.
$$v_c(\infty) = V_s = 6\text{ V}$$
Now find the natural response parameters:
$$\alpha = \frac{R}{2L} = \frac{2}{2(1)} = 1 \text{ Np/s}$$
$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 1}} = 1 \text{ rad/s}$$
Since $\alpha = \omega_0 = 1$, the circuit is **critically damped**.
The form of the total response for a critically damped series RLC step response is:
$$v_c(t) = v_c(\infty) + (A_1 + A_2 t)e^{-\alpha t} = 6 + (A_1 + A_2 t)e^{-t}$$
Use initial conditions to find $A_1$ and $A_2$:
*   $v_c(0) = 2 \implies 6 + (A_1 + 0)e^{0} = 2 \implies A_1 = -4$
*   To use $i_L(0)$, we relate it to $v_c$: In a series RLC circuit, $i_L(t) = C\frac{dv_c}{dt}$.
    $$\frac{dv_c}{dt} = \frac{d}{dt} \left[ 6 + (-4 + A_2 t)e^{-t} \right] = A_2 e^{-t} - (-4 + A_2 t)e^{-t}$$
    At $t = 0$:
    $$\frac{dv_c(0)}{dt} = A_2 - (-4) = A_2 + 4$$
    Since $i_L(0) = 2\text{ A}$ and $C = 1\text{ F}$:
    $$C\frac{dv_c(0)}{dt} = 2 \implies 1(A_2 + 4) = 2 \implies A_2 = -2$$
Substituting $A_1$ and $A_2$ back into the response equation:
$$v_c(t) = 6 + (-4 - 2t)e^{-t}$$
$$v_c(t) = 6 - (4 + 2t)e^{-t} \text{ V}, \quad \text{for } t > 0$$

**(iii) Find the nature of the response:**
As calculated in part (ii), $\alpha = 1$ and $\omega_0 = 1$. Because $\alpha = \omega_0$, the nature of the response is **Critically damped**.

*Ans related location: Sadiku Textbook, Chapter 8 (Second-Order Circuits), Section 8.5 (Step Response of a Series RLC Circuit), pg. 331-336.*


### 21. Page 3, Q.5(a): For the following circuit (i) Draw the s-domain circuit considering $v_0(0) = 5V$. (ii) Find $v_0(t)$ (Figure Involved)

**Solution:**

**(i) S-domain Circuit Representation:**
To transform the circuit into the s-domain (Laplace domain), we replace the time-domain components with their complex frequency equivalents.
*   **Voltage Source:** The independent voltage source $v_i(t) = 10e^{-t}u(t)$ V transforms to $V_i(s) = \frac{10}{s+1}$ V.
*   **Resistors:** The two $10 \Omega$ resistors remain unchanged as $10 \Omega$.
*   **Capacitor:** The capacitor $C = 0.1$ F transforms to an impedance $Z_C(s) = \frac{1}{sC} = \frac{1}{0.1s} = \frac{10}{s} \Omega$.
*   **Initial Condition:** The initial condition of the capacitor $v_0(0) = 5$ V is modeled as a parallel independent current source. Its value is $I_0 = C v_0(0) = 0.1 \times 5 = 0.5$ A. Because the positive terminal of $v_0(t)$ is at the top, this equivalent current source points DOWNWARDS from the node.
*   **Current Source:** The independent impulse current source $2\delta(t)$ A transforms to a constant $2$ A pointing UPWARDS.

*The s-domain circuit consists of the voltage source $V_i(s)$ in series with the first $10\Omega$ resistor, connected to the output node $V_0(s)$. At the output node, the second $10\Omega$ resistor, the capacitor impedance $10/s$, the $0.5$ A downward current source, and the $2$ A upward current source are all connected in parallel to ground.*

**(ii) Find $v_0(t)$:**
We apply Nodal Analysis at the output node $V_0(s)$. The net current entering the node from the independent sources is $2\text{ A (up)} - 0.5\text{ A (down)} = 1.5\text{ A}$.

Summing the currents leaving the node:
$$ \frac{V_0(s) - V_i(s)}{10} + \frac{V_0(s)}{10} + \frac{V_0(s)}{10/s} = 1.5 $$

Substitute $V_i(s) = \frac{10}{s+1}$ and multiply the entire equation by 10 to eliminate the denominators:
$$ \left(V_0(s) - \frac{10}{s+1}\right) + V_0(s) + s V_0(s) = 15 $$

Group the $V_0(s)$ terms together:
$$ V_0(s) (1 + 1 + s) - \frac{10}{s+1} = 15 $$
$$ V_0(s) (s + 2) = 15 + \frac{10}{s+1} $$

Find a common denominator for the right side:
$$ V_0(s) (s + 2) = \frac{15(s + 1) + 10}{s+1} = \frac{15s + 15 + 10}{s+1} = \frac{15s + 25}{s+1} $$

Solve for $V_0(s)$:
$$ V_0(s) = \frac{15s + 25}{(s+1)(s+2)} $$

Now, use partial fraction expansion to prepare for the inverse Laplace transform:
$$ V_0(s) = \frac{A}{s+1} + \frac{B}{s+2} $$
$$ A = \left. \frac{15s + 25}{s+2} \right|_{s=-1} = \frac{-15 + 25}{-1 + 2} = \frac{10}{1} = 10 $$
$$ B = \left. \frac{15s + 25}{s+1} \right|_{s=-2} = \frac{-30 + 25}{-2 + 1} = \frac{-5}{-1} = 5 $$

Substitute $A$ and $B$ back into the partial fraction expression:
$$ V_0(s) = \frac{10}{s+1} + \frac{5}{s+2} $$

Taking the inverse Laplace transform of each term yields the time-domain voltage:
$$ v_0(t) = \left( 10e^{-t} + 5e^{-2t} \right) u(t) \text{ V} $$

*Reference: Fundamentals of Electric Circuits by Sadiku, Chapter 16 (Applications of the Laplace Transform), Section 16.3, similar to Example 16.5 (Page 723).*

***

### 22. Page 5, Q.2(b): The switch of the following circuit was opened for a long period of time and is closed at t=0 s. Fill the table for the following circuit parameters. (Figure Involved)

**Solution:**
We are given $R_1=1\Omega$, $L=2\text{ H}$, $R_2=1\Omega$, and $V_s=10 u(-t)\text{ V}$. We need to evaluate the inductor current $i_L$ and voltage $v_L$ at $t=0^+$ and $t=10\text{s}$.

**1. Analysis for $t < 0$ (Steady State):**
For $t < 0$, the function $u(-t) = 1$, so the voltage source is a constant $10\text{ V}$. The switch is open, meaning the circuit consists of the $10\text{ V}$ source in series with $R_1$, $L$, and $R_2$. 
In DC steady state, the inductor acts as a short circuit ($0\Omega$).
*   The initial inductor current $i_L(0^-)$ is simply the source voltage divided by the total series resistance:
$$ i_L(0^-) = \frac{V_s}{R_1 + R_2} = \frac{10}{1 + 1} = 5 \text{ A} $$
*   Because current through an inductor cannot change instantaneously, $i_L(0^+) = i_L(0^-) = 5 \text{ A}$.

**2. Analysis for $t = 0^+$:**
At $t=0$, the switch closes, creating a short circuit from the node between $R_1$ and $L$ directly to ground. Simultaneously, for $t > 0$, $u(-t) = 0$, so the voltage source becomes $0\text{ V}$.
*   The closing of the switch isolates the right side of the circuit from the left. The inductor $L$ and resistor $R_2$ now form a closed, source-free series loop on their own.
*   By KVL around this isolated loop at $t=0^+$, $v_L(0^+) + i_L(0^+)R_2 = 0$. 
$$ v_L(0^+) = - i_L(0^+) \times R_2 = -5 \times 1 = -5 \text{ V} $$

**3. Analysis for $t > 0$:**
The right side of the circuit is a source-free RL circuit.
*   The time constant is $\tau = \frac{L}{R_2} = \frac{2\text{ H}}{1\Omega} = 2 \text{ s}$.
*   The equation for the decaying inductor current is:
$$ i_L(t) = i_L(0^+) e^{-t/\tau} = 5 e^{-0.5t} \text{ A} $$
*   The equation for the inductor voltage is:
$$ v_L(t) = L \frac{di_L}{dt} = 2 \left( 5 \times -0.5 e^{-0.5t} \right) = -5 e^{-0.5t} \text{ V} $$

**4. Evaluation at $t = 10 \text{ s}$:**
*   $i_L(10) = 5 e^{-0.5 \times 10} = 5 e^{-5} \approx 5 \times 0.006738 = 0.0337 \text{ A}$
*   $v_L(10) = -5 e^{-0.5 \times 10} = -5 e^{-5} \approx -5 \times 0.006738 = -0.0337 \text{ V}$

**Filled Table Values:**
*   (i) $i_L, t=0\text{ s}$ $\rightarrow$ **$5 \text{ A}$** (This represents $t=0^+$)
*   (ii) $v_L, t=0\text{ s}$ $\rightarrow$ **$-5 \text{ V}$** (This represents $t=0^+$)
*   (iii) $i_L, t=10\text{ s}$ $\rightarrow$ **$0.0337 \text{ A}$**
*   (iv) $v_L, t=10\text{ s}$ $\rightarrow$ **$-0.0337 \text{ V}$**

*Reference: Fundamentals of Electric Circuits by Sadiku, Chapter 7 (First-Order Circuits), Section 7.3 Source-Free RL Circuit (Page 259).*

***

### 23. Page 7, Q.5(a): In the following circuit the switch is closed for a long time before it is opened at t = 0. Find the inductor current i(t) for t>0 by transforming the circuit in s-domain. (Figure Involved)

**Solution:**

**1. Initial Conditions ($t < 0$):**
The switch is closed, establishing a DC steady state. The $0.5\text{ H}$ inductor acts as a short circuit, and the $1/20\text{ F}$ capacitor acts as an open circuit.
*   Because the inductor is a short, the node directly after it is at $10\text{ V}$. 
*   The current flows from the $10\text{ V}$ source, through the shorted inductor, and down through the $5\Omega$ resistor (since the path with the open capacitor draws no steady current).
*   The initial inductor current is:
$$ i(0^-) = \frac{10\text{ V}}{5\Omega} = 2 \text{ A} $$
*   The capacitor is connected between the $10\text{ V}$ node and the $2\Omega$ resistor (which goes to ground). Since no current flows through the $2\Omega$ resistor, there is no voltage drop across it. Thus, the initial capacitor voltage is:
$$ v_c(0^-) = 10\text{ V} $$

**2. S-Domain Transformation ($t > 0$):**
At $t=0$, the switch opens, disconnecting the $5\Omega$ resistor. The circuit becomes a series RLC circuit driven by the $10\text{ V}$ source. We transform the circuit into the Laplace domain:
*   Voltage source: $V_s(s) = \frac{10}{s}$
*   Inductor: impedance is $sL = 0.5s$. To account for the initial current, we use a series voltage source $-L i(0) = -0.5(2) = -1$ V (opposing the current flow).
*   Capacitor: impedance is $\frac{1}{sC} = \frac{1}{(1/20)s} = \frac{20}{s}$. To account for the initial voltage, we use a series voltage source $\frac{v_c(0)}{s} = \frac{10}{s}$.
*   Resistor: $2\Omega$.

**3. Circuit Analysis in the S-Domain:**
Apply Kirchhoff's Voltage Law (KVL) around the series loop:
$$ V_s(s) + L i(0) - \frac{v_c(0)}{s} = I(s) \left( sL + R + \frac{1}{sC} \right) $$
*(Note: $L i(0)$ is added because it acts as a source in the direction of current, while $v_c(0)/s$ acts against it).*
$$ \frac{10}{s} + 1 - \frac{10}{s} = I(s) \left( 0.5s + 2 + \frac{20}{s} \right) $$

Notice that the $\frac{10}{s}$ terms cancel out entirely:
$$ 1 = I(s) \left( \frac{0.5s^2 + 2s + 20}{s} \right) $$

Solve for $I(s)$:
$$ I(s) = \frac{s}{0.5s^2 + 2s + 20} $$
Multiply numerator and denominator by 2 to make the $s^2$ coefficient 1:
$$ I(s) = \frac{2s}{s^2 + 4s + 40} $$

**4. Inverse Laplace Transform:**
We complete the square for the denominator:
$$ s^2 + 4s + 40 = (s^2 + 4s + 4) + 36 = (s+2)^2 + 6^2 $$
Rewrite $I(s)$ to match standard Laplace transform pairs $\frac{s+a}{(s+a)^2 + \omega^2}$ and $\frac{\omega}{(s+a)^2 + \omega^2}$:
$$ I(s) = \frac{2(s+2-2)}{(s+2)^2 + 6^2} = 2 \left( \frac{s+2}{(s+2)^2 + 6^2} \right) - \frac{4}{(s+2)^2 + 6^2} $$
To match the sine transform form exactly, multiply and divide the second term by 6:
$$ I(s) = 2 \left( \frac{s+2}{(s+2)^2 + 6^2} \right) - \frac{4}{6} \left( \frac{6}{(s+2)^2 + 6^2} \right) $$
$$ I(s) = 2 \left( \frac{s+2}{(s+2)^2 + 6^2} \right) - \frac{2}{3} \left( \frac{6}{(s+2)^2 + 6^2} \right) $$

Taking the inverse Laplace transform gives the time-domain current:
$$ i(t) = \left( 2e^{-2t}\cos(6t) - \frac{2}{3}e^{-2t}\sin(6t) \right) u(t) \text{ A} $$

*Reference: Fundamentals of Electric Circuits by Sadiku, Chapter 16 (Applications of the Laplace Transform), Section 16.3 Circuit Analysis (Page 722).*

***

### 24. Page 9, Q.3(a): A 240W power supply circuit is shown in the following figure. This circuit employs a large inductor and capacitor. Find $i_L(t)$ for $t > 0$. Assume steady-state conditions exist at $t = 0^-$. (Figure Involved)

**Solution:**

**1. Initial Conditions ($t < 0$):**
The switch, located on the vertical branch, has an arrow indicating it **closes** at $t=0$. Therefore, for $t < 0$, the switch is OPEN. 
The $7\text{ A}$ current source supplies the circuit. In DC steady state, the $4\text{ H}$ inductor acts as a short circuit, and the $1/4\text{ F}$ capacitor acts as an open circuit.
*   Because the inductor is a short, the $8\Omega$ resistor and the $2\Omega$ resistor are effectively in parallel.
*   Equivalent resistance $R_{eq} = 8\Omega || 2\Omega = \frac{8 \times 2}{8 + 2} = 1.6 \Omega$.
*   The voltage across the parallel combination (which is also the initial capacitor voltage) is:
$$ v_c(0^-) = I \times R_{eq} = 7 \text{ A} \times 1.6 \Omega = 11.2 \text{ V} $$
*   The current flowing through the $2\Omega$ resistor branch (and thus through the shorted inductor from right to left) is:
$$ i_{2\Omega} = \frac{11.2 \text{ V}}{2 \Omega} = 5.6 \text{ A} $$
*   The reference arrow for $i_L$ points to the right. Since the actual current flows leftward from the source to the $2\Omega$ load, the initial inductor current is:
$$ i_L(0^-) = -5.6 \text{ A} $$

**2. Circuit Analysis for $t > 0$:**
At $t=0$, the switch closes, creating a short circuit directly across the $7\text{ A}$ source and the $8\Omega$ resistor, thereby completely bypassing them.
The left portion of the circuit now forms a source-free parallel RLC circuit containing the $1/4\text{ F}$ capacitor, the $2\Omega$ resistor, and the $4\text{ H}$ inductor. 
*   $R = 2\Omega$
*   $L = 4\text{ H}$
*   $C = 0.25\text{ F}$

First, we determine the damping coefficient $\alpha$ and resonant frequency $\omega_0$ for a parallel RLC circuit:
$$ \alpha = \frac{1}{2RC} = \frac{1}{2(2)(0.25)} = \frac{1}{1} = 1 \text{ Np/s} $$
$$ \omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{4(0.25)}} = \frac{1}{\sqrt{1}} = 1 \text{ rad/s} $$
Because $\alpha = \omega_0 = 1$, the circuit is **critically damped**.
The general solution for the inductor current in a critically damped circuit is:
$$ i_L(t) = (A_1 + A_2 t) e^{-\alpha t} = (A_1 + A_2 t) e^{-t} $$

**3. Solving for Constants $A_1$ and $A_2$:**
*   Using the initial current:
$$ i_L(0) = A_1 = -5.6 \text{ A} $$
*   To find $A_2$, we evaluate the derivative $\frac{di_L}{dt}$ at $t=0^+$. The voltage across the inductor in this parallel configuration is equal to the voltage across the capacitor, $v_L = v_c$.
$$ v_L(0^+) = L \frac{di_L(0^+)}{dt} = v_c(0^+) $$
$$ 4 \frac{di_L(0^+)}{dt} = 11.2 \implies \frac{di_L(0^+)}{dt} = \frac{11.2}{4} = 2.8 \text{ A/s} $$
*   Now, differentiate the general solution:
$$ \frac{di_L(t)}{dt} = A_2 e^{-t} - (A_1 + A_2 t) e^{-t} $$
Evaluate at $t=0$:
$$ \frac{di_L(0)}{dt} = A_2 - A_1 = 2.8 $$
*   Substitute $A_1 = -5.6$ into the equation:
$$ A_2 - (-5.6) = 2.8 \implies A_2 + 5.6 = 2.8 \implies A_2 = 2.8 - 5.6 = -2.8 $$

**4. Final Expression:**
Substituting $A_1$ and $A_2$ back into the generic response equation gives:
$$ i_L(t) = (-5.6 - 2.8t) e^{-t} u(t) \text{ A} $$

*Reference: Fundamentals of Electric Circuits by Sadiku, Chapter 8 (Second-Order Circuits), Section 8.4 Source-Free Parallel RLC Circuit (Page 327).*


Based on the document provided, here are the detailed step-by-step solutions for the next 4 questions (Questions 25 to 28).

### 25. Page 9, Q.3(b): Find $i(t)$ for $t > 0$ in the following circuit.
*(Image shows a 20V source, a 10 $\Omega$ resistor, a switch opening at t=0, a 40 $\Omega$ resistor, a 60 $\Omega$ resistor, a 1 mF capacitor, and a 2.5 H inductor).*

**Solution:**
From the schematic, we interpret the circuit as follows: The $20\text{V}$ source and $10\Omega$ resistor are in series, connected via a switch to a node. From this node, a $40\Omega$ resistor goes to ground, and a branch containing a $60\Omega$ resistor, a $1\text{mF}$ capacitor, and a $2.5\text{H}$ inductor in series also goes to ground.

**1. Analysis for $t < 0$ (Steady State):**
The switch is closed, so the circuit has reached DC steady state. 
*   In DC steady state, the capacitor acts as an open circuit. This means no current flows through the rightmost branch (containing the $60\Omega$ resistor, capacitor, and inductor).
*   Therefore, the initial inductor current is **$i_L(0^-) = 0 \text{ A}$**.
*   The voltage at the node above the $40\Omega$ resistor is determined by a simple voltage divider between the $10\Omega$ and $40\Omega$ resistors:
$$ V_C(0^-) = 20\text{V} \times \frac{40\Omega}{10\Omega + 40\Omega} = 20 \times \frac{40}{50} = 16\text{ V} $$
*   Because the capacitor is in parallel with the $40\Omega$ resistor (via the shorted inductor), its initial voltage is **$v_c(0^-) = 16\text{ V}$**.

**2. Analysis for $t > 0$:**
At $t = 0$, the switch opens, completely disconnecting the $20\text{V}$ source and $10\Omega$ resistor. 
The remaining circuit forms a source-free series RLC loop consisting of the $40\Omega$ resistor, the $60\Omega$ resistor, the $1\text{mF}$ capacitor, and the $2.5\text{H}$ inductor.
*   Equivalent resistance, $R = 40\Omega + 60\Omega = 100\Omega$.
*   Inductance, $L = 2.5\text{ H}$.
*   Capacitance, $C = 1\text{ mF} = 0.001\text{ F}$.

Let's find the damping coefficient ($\alpha$) and resonant frequency ($\omega_0$):
$$ \alpha = \frac{R}{2L} = \frac{100}{2 \times 2.5} = \frac{100}{5} = 20 \text{ Np/s} $$
$$ \omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{2.5 \times 0.001}} = \frac{1}{\sqrt{0.0025}} = \frac{1}{0.05} = 20 \text{ rad/s} $$
Since $\alpha = \omega_0 = 20$, the circuit is **critically damped**.
The general equation for current in a critically damped series RLC circuit is:
$$ i(t) = (A_1 + A_2 t) e^{-\alpha t} $$

**3. Solving for Constants:**
*   At $t=0^+$, the current cannot change instantaneously, so $i(0^+) = i_L(0^-) = 0$.
$$ i(0) = A_1 = 0 $$
*   To find $A_2$, we evaluate $\frac{di(0^+)}{dt}$ using KVL around the loop at $t=0^+$. The sum of voltage drops must be zero:
$$ v_R(0^+) + v_L(0^+) + v_C(0^+) = 0 $$
$$ R i(0^+) + L \frac{di(0^+)}{dt} + v_C(0^+) = 0 $$
$$ 100(0) + 2.5 \frac{di(0^+)}{dt} + 16 = 0 \implies 2.5 \frac{di(0^+)}{dt} = -16 \implies \frac{di(0^+)}{dt} = -6.4 \text{ A/s} $$
*   Taking the derivative of our general current equation $i(t) = A_2 t e^{-20t}$:
$$ \frac{di(t)}{dt} = A_2 e^{-20t} - 20 A_2 t e^{-20t} $$
*   Evaluating at $t=0$:
$$ \frac{di(0^+)}{dt} = A_2 = -6.4 $$

**Final Equation:**
Substituting $A_1$ and $A_2$ back into the general equation gives:
$$ \mathbf{i(t) = -6.4 t e^{-20t} u(t) \text{ A}} $$

***

### 26. Page 11, Q.1(b): The switch in the following figure opens at t = 0. Determine v(t) for t > 0.
*(Image shows a 5A source, 4 $\Omega$ resistor, switch, 6 $\Omega$ resistor, 100mF capacitor, 5 $\Omega$ resistor, 20 $\Omega$ resistor, 30V source).*

**Solution:**
Based on the schematic, we interpret the topology as follows: A $5\text{A}$ current source in parallel with a $4\Omega$ resistor is connected via a switch to Node C. At Node C, a $6\Omega$ resistor and a $100\text{mF}$ capacitor connect to ground. Also from Node C, a $5\Omega$ resistor connects to Node D. At Node D, a $20\Omega$ resistor connects to ground, and a $30\text{V}$ voltage source connects to ground.

**1. Analysis for $t < 0$ (Steady State):**
The switch is closed. The capacitor is fully charged and acts as an open circuit. 
We can convert the 5A source and parallel $4\Omega$ resistor into a Thevenin equivalent: a $20\text{V}$ source in series with a $4\Omega$ resistor.
Now we apply Nodal Analysis at Node C to find the initial capacitor voltage $v(0^-)$:
$$ \frac{V_c - 20}{4} + \frac{V_c}{6} + \frac{V_c - 30}{5 + 20} = 0 $$
$$ \frac{V_c}{4} - 5 + \frac{V_c}{6} + \frac{V_c}{25} - \frac{30}{25} = 0 $$
$$ V_c \left( \frac{1}{4} + \frac{1}{6} + \frac{1}{25} \right) = 5 + 1.2 $$
To find a common denominator (300):
$$ V_c \left( \frac{75 + 50 + 12}{300} \right) = 6.2 \implies V_c \left( \frac{137}{300} \right) = 6.2 $$
$$ V_c(0^-) = \frac{6.2 \times 300}{137} = \frac{1860}{137} \approx 13.577 \text{ V} $$
Because capacitor voltage cannot change instantaneously, **$v(0^+) = 13.577 \text{ V}$**.

**2. Analysis for $t > 0$:**
The switch opens, disconnecting the left portion of the circuit. The capacitor now interacts with the rest of the circuit to its right. We find the Thevenin equivalent of the circuit connected to the capacitor.
*   **Thevenin Resistance ($R_{th}$):** Looking from the capacitor's terminals with the 30V source turned off (shorted to ground):
$$ R_{th} = 6\Omega \parallel (5\Omega + 20\Omega) = 6 \parallel 25 = \frac{6 \times 25}{6 + 25} = \frac{150}{31} \approx 4.839 \Omega $$
*   **Thevenin Voltage ($V_{th}$):** The open-circuit steady-state voltage across the capacitor branch. Using a voltage divider from the 30V source:
$$ v(\infty) = V_{th} = 30 \times \frac{6}{6 + 25} = \frac{180}{31} \approx 5.806 \text{ V} $$
*   **Time Constant ($\tau$):** 
$$ \tau = R_{th} C = \left(\frac{150}{31} \Omega \right) \times 0.1 \text{ F} = \frac{15}{31} \text{ s} \approx 0.484 \text{ s} $$

**3. Final Equation:**
Using the general step response formula for a first-order RC circuit:
$$ v(t) = v(\infty) + [v(0^+) - v(\infty)] e^{-t/\tau} $$
$$ v(t) = \frac{180}{31} + \left( \frac{1860}{137} - \frac{180}{31} \right) e^{-\frac{31}{15}t} $$
$$ \mathbf{v(t) \approx 5.806 + 7.77 e^{-2.067 t} \text{ V}} \quad \text{for } t > 0 $$

***

### 27. Page 11, Q.1(c): The switch of the circuit in the figure below is controlled electronically so that it closes when $v_c$ rises to 9V and opens when $v_c$ falls to 5V. Find and plot $v_c(t)$ for several switchings. Also find the frequency of the generating triangular waveform.

**Solution:**
From the schematic, we have a $12\text{V}$ DC source, a series resistor $R_1 = 6\text{k}\Omega$, a capacitor $C = 0.5\text{mF}$ to ground, and a branch containing a switch and $R_2 = 3\text{k}\Omega$ connected in parallel with the capacitor.

**1. Charging Phase (Switch is OPEN):**
The switch opens when the voltage falls to $5\text{V}$. During this phase, the capacitor charges from the $12\text{V}$ source through $R_1$.
*   Initial voltage: $V_{initial} = 5\text{V}$
*   Target steady-state voltage: $V_{\infty, charge} = 12\text{V}$
*   Time constant: $\tau_c = R_1 C = 6\text{k}\Omega \times 0.5\text{mF} = 3\text{ s}$
The equation for the charging voltage is:
$$ v_{c,charge}(t) = V_{\infty} + (V_{initial} - V_{\infty}) e^{-t/\tau_c} = 12 + (5 - 12) e^{-t/3} = 12 - 7e^{-t/3} \text{ V} $$
We find the time $t_c$ it takes to reach the trigger voltage of $9\text{V}$:
$$ 9 = 12 - 7e^{-t_c/3} \implies 7e^{-t_c/3} = 3 \implies e^{-t_c/3} = \frac{3}{7} $$
$$ t_c = -3 \ln(3/7) = 3 \ln(7/3) \approx \mathbf{2.542 \text{ s}} $$

**2. Discharging Phase (Switch is CLOSED):**
The switch closes when the voltage hits $9\text{V}$. Now, $R_2$ ($3\text{k}\Omega$) is placed in parallel with the capacitor, creating a voltage divider with $R_1$.
*   Initial voltage: $V_{initial} = 9\text{V}$
*   Target steady-state voltage (Thevenin equivalent): $V_{\infty, discharge} = 12 \times \frac{3\text{k}}{6\text{k} + 3\text{k}} = 12 \times \frac{3}{9} = 4\text{V}$
*   Equivalent resistance: $R_{eq} = 6\text{k} \parallel 3\text{k} = 2\text{k}\Omega$
*   Time constant: $\tau_d = R_{eq} C = 2\text{k}\Omega \times 0.5\text{mF} = 1\text{ s}$
The equation for the discharging voltage is:
$$ v_{c,discharge}(t) = V_{\infty} + (V_{initial} - V_{\infty}) e^{-t/\tau_d} = 4 + (9 - 4) e^{-t/1} = 4 + 5e^{-t} \text{ V} $$
We find the time $t_d$ it takes to fall back to the trigger voltage of $5\text{V}$:
$$ 5 = 4 + 5e^{-t_d} \implies 1 = 5e^{-t_d} \implies e^{-t_d} = 0.2 $$
$$ t_d = -\ln(0.2) = \ln(5) \approx \mathbf{1.609 \text{ s}} $$

**3. Frequency of the Waveform:**
The total period $T$ of one complete charge/discharge cycle is:
$$ T = t_c + t_d = 2.542 + 1.609 = 4.151 \text{ s} $$
The frequency $f$ is:
$$ f = \frac{1}{T} = \frac{1}{4.151} \approx \mathbf{0.241 \text{ Hz}} $$
*(The plot of $v_c(t)$ is a continuous waveform oscillating between 5V and 9V, following exponential charge and discharge curves).*

***

### 28. Page 11, Q.2(c): In the following figure, the switch S has been at position A for a long time and is moved to position B at t = 0. (i) Find $v_c(t)$ for t > 0; (ii) Find $i_L(0^+)$, $v_c(0^+)$ and $i_L(t)$ for t > 0.

**Solution:**
The circuit has a $10\text{V}$ source at Position A, ground at Position B. The main circuit consists of a switch node connected to a vertical $2.5\Omega$ resistor to ground, and a horizontal branch containing a $2.5\Omega$ resistor, a $2.5\text{H}$ inductor, and a $0.1\text{F}$ capacitor to ground.

**1. Initial Conditions ($t < 0$):**
Switch is at Position A ($10\text{V}$). DC steady state.
*   The $2.5\text{H}$ inductor acts as a short, and the $0.1\text{F}$ capacitor acts as an open circuit.
*   Because the capacitor is an open circuit, no steady-state current flows through the horizontal branch.
$$ \mathbf{i_L(0^-) = 0 \text{ A}} $$
*   The voltage at the switch node is $10\text{V}$. Since there is no voltage drop across the horizontal $2.5\Omega$ resistor and the inductor, the capacitor voltage is equal to the switch node voltage.
$$ \mathbf{v_c(0^-) = 10 \text{ V}} $$
Due to continuity, **$i_L(0^+) = 0 \text{ A}$** and **$v_c(0^+) = 10 \text{ V}$**.

**2. Circuit Analysis ($t > 0$):**
The switch moves to Position B (ground). 
*   This shorts the vertical $2.5\Omega$ resistor to ground, removing it from the dynamics.
*   We are left with a source-free series RLC circuit connected to ground.
*   $R = 2.5\Omega$, $L = 2.5\text{H}$, $C = 0.1\text{F}$.

Let's find the damping coefficient ($\alpha$) and resonant frequency ($\omega_0$):
$$ \alpha = \frac{R}{2L} = \frac{2.5}{2 \times 2.5} = 0.5 \text{ Np/s} $$
$$ \omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{2.5 \times 0.1}} = \frac{1}{\sqrt{0.25}} = \frac{1}{0.5} = 2 \text{ rad/s} $$
Since $\alpha < \omega_0$ ($0.5 < 2$), the circuit is **underdamped**.
The damped natural frequency is:
$$ \omega_d = \sqrt{\omega_0^2 - \alpha^2} = \sqrt{2^2 - 0.5^2} = \sqrt{4 - 0.25} = \sqrt{3.75} \approx 1.936 \text{ rad/s} $$

**3. Finding $v_c(t)$:**
The general solution for an underdamped series RLC circuit voltage is:
$$ v_c(t) = e^{-\alpha t} (A_1 \cos \omega_d t + A_2 \sin \omega_d t) $$
*   Using $v_c(0) = 10\text{V}$:
$$ v_c(0) = A_1 = 10 $$
*   To find $A_2$, we use the relationship $i_L(t) = C \frac{dv_c}{dt}$ (since current $i_L$ flows into the positive terminal of the capacitor):
$$ i_L(0^+) = C \left[ -\alpha A_1 + \omega_d A_2 \right] = 0 $$
$$ -0.5(10) + \sqrt{3.75} A_2 = 0 \implies \sqrt{3.75} A_2 = 5 \implies A_2 = \frac{5}{\sqrt{3.75}} \approx 2.582 $$
$$ \mathbf{v_c(t) = e^{-0.5t} \left( 10 \cos 1.936t + 2.582 \sin 1.936t \right) \text{ V}} $$

**4. Finding $i_L(t)$:**
The general solution for the inductor current is:
$$ i_L(t) = e^{-\alpha t} (B_1 \cos \omega_d t + B_2 \sin \omega_d t) $$
*   Using $i_L(0) = 0\text{A}$:
$$ i_L(0) = B_1 = 0 $$
*   To find $B_2$, we need $\frac{di_L(0^+)}{dt}$. Apply KVL around the loop at $t=0^+$:
$$ R i_L(0^+) + L \frac{di_L(0^+)}{dt} + v_c(0^+) = 0 $$
$$ 0 + 2.5 \frac{di_L(0^+)}{dt} + 10 = 0 \implies \frac{di_L(0^+)}{dt} = -4 \text{ A/s} $$
*   Take the derivative of $i_L(t)$ and evaluate at $t=0$:
$$ \frac{di_L(0)}{dt} = -\alpha B_1 + \omega_d B_2 = \sqrt{3.75} B_2 $$
$$ \sqrt{3.75} B_2 = -4 \implies B_2 = \frac{-4}{\sqrt{3.75}} \approx -2.066 $$
$$ \mathbf{i_L(t) = -2.066 e^{-0.5t} \sin(1.936t) \text{ A}} $$

Based on the provided document, here are the full texts and detailed step-by-step solutions for the next 4 questions (Questions 29 to 32).

### 29. Page 14, Q.1(c): A relay has a resistance of $200 \Omega$ and an inductance of $500\text{ mH}$. The relay contacts close when the current through the coil reaches $350\text{ mA}$. What time elapses between the application of $110\text{ V}$ to the coil and contact closure.

**Solution:**
When a DC voltage is suddenly applied to an RL circuit (like a relay coil), it acts as a step response. The circuit consists of a voltage source $V_s = 110\text{ V}$, a resistor $R = 200 \Omega$, and an inductor $L = 500\text{ mH} = 0.5\text{ H}$ in series.

The general equation for the current in a series RL circuit subjected to a DC step voltage is:
$$ i(t) = \frac{V_s}{R} \left( 1 - e^{-\frac{R}{L}t} \right) $$

**1. Identify the given parameters:**
*   $V_s = 110\text{ V}$
*   $R = 200 \Omega$
*   $L = 0.5\text{ H}$
*   Target current, $i(t_{close}) = 350\text{ mA} = 0.35\text{ A}$

**2. Calculate the steady-state current and time constant:**
*   Steady-state maximum current: $I_{max} = \frac{V_s}{R} = \frac{110}{200} = 0.55\text{ A}$
*   Time constant: $\tau = \frac{L}{R} = \frac{0.5}{200} = 0.0025\text{ s}$
*   Inverse time constant: $\frac{R}{L} = \frac{200}{0.5} = 400\text{ s}^{-1}$

**3. Set up the equation and solve for $t_{close}$:**
$$ 0.35 = 0.55 \left( 1 - e^{-400t} \right) $$
Divide both sides by $0.55$:
$$ \frac{0.35}{0.55} = 1 - e^{-400t} $$
$$ \frac{35}{55} = \frac{7}{11} = 1 - e^{-400t} $$
Rearrange to solve for the exponential term:
$$ e^{-400t} = 1 - \frac{7}{11} = \frac{4}{11} $$
Take the natural logarithm (ln) of both sides:
$$ -400t = \ln\left(\frac{4}{11}\right) $$
$$ t = \frac{-\ln(4/11)}{400} = \frac{\ln(11/4)}{400} $$
$$ t \approx \frac{1.0116}{400} \approx 0.002529 \text{ s} $$

**Answer:**
The time elapsed before contact closure is **$2.529\text{ ms}$**. 
*(Related location: Sadiku textbook, Chapter 7, Practice Problem 7.21)*

***

### 30. Page 14, Q.2(b): Obtain $i_1$ and $i_2$ for $t > 0$ for the following network. (Figure Involved)

**Solution:**
Based on the provided schematic image, the circuit consists of:
*   An independent current source $i_s(t) = 4u(t)\text{ A}$
*   A parallel resistor $R_1 = 2 \Omega$
*   A series inductor $L_1 = 1\text{ H}$
*   A parallel branch with a resistor $R_2 = 3 \Omega$ (current $i_1$ flows through it)
*   A parallel branch with an inductor $L_2 = 1\text{ H}$ (current $i_2$ flows through it)

**1. S-Domain Transformation:**
We convert the circuit elements into their Laplace (s-domain) equivalents, assuming zero initial conditions:
*   Current source: $I_s(s) = \frac{4}{s}$
*   $R_1 = 2 \Omega$
*   $L_1$ impedance: $Z_{L1} = sL_1 = s$
*   $R_2 = 3 \Omega$
*   $L_2$ impedance: $Z_{L2} = sL_2 = s$

**2. Source Transformation and Simplification:**
Convert the current source and parallel $R_1$ into a Thevenin equivalent:
*   $V_{th}(s) = I_s(s) \times R_1 = \frac{4}{s} \times 2 = \frac{8}{s} \text{ V}$
*   This voltage source is in series with $R_1 = 2 \Omega$ and $L_1 = s$.
*   Total series impedance: $Z_{series} = 2 + s$

Let $V_A(s)$ be the voltage at the node above the $3\Omega$ resistor and $1\text{H}$ inductor. The $3\Omega$ resistor and $s \Omega$ inductor are in parallel.
*   Equivalent parallel impedance: $Z_{p} = \frac{3 \cdot s}{3 + s} = \frac{3s}{s+3} \Omega$

**3. Solve for Node Voltage $V_A(s)$:**
Using voltage division:
$$ V_A(s) = V_{th}(s) \frac{Z_p}{Z_{series} + Z_p} $$
$$ V_A(s) = \left(\frac{8}{s}\right) \frac{\frac{3s}{s+3}}{(2+s) + \frac{3s}{s+3}} $$
Multiply the numerator and denominator of the main fraction by $(s+3)$:
$$ V_A(s) = \left(\frac{8}{s}\right) \frac{3s}{(2+s)(s+3) + 3s} $$
$$ V_A(s) = \frac{24}{s^2 + 5s + 6 + 3s} = \frac{24}{s^2 + 8s + 6} $$

**4. Solve for Currents $I_1(s)$ and $I_2(s)$:**
*   $I_1(s)$ is the current through the $3\Omega$ resistor:
$$ I_1(s) = \frac{V_A(s)}{3} = \frac{8}{s^2 + 8s + 6} $$
*   $I_2(s)$ is the current through the $L_2$ inductor ($Z = s$):
$$ I_2(s) = \frac{V_A(s)}{s} = \frac{24}{s(s^2 + 8s + 6)} $$

**5. Inverse Laplace Transform:**
First, find the roots of $s^2 + 8s + 6 = 0$ using the quadratic formula:
$$ s_{1,2} = \frac{-8 \pm \sqrt{64 - 24}}{2} = \frac{-8 \pm \sqrt{40}}{2} = -4 \pm \sqrt{10} $$
Let $p_1 = -4 + \sqrt{10}$ and $p_2 = -4 - \sqrt{10}$.

*For $i_1(t)$:*
$$ I_1(s) = \frac{8}{(s-p_1)(s-p_2)} = \frac{A}{s-p_1} + \frac{B}{s-p_2} $$
$$ A = \frac{8}{p_1 - p_2} = \frac{8}{2\sqrt{10}} = \frac{4}{\sqrt{10}} $$
$$ B = \frac{8}{p_2 - p_1} = -\frac{4}{\sqrt{10}} $$
$$ i_1(t) = \frac{4}{\sqrt{10}} \left( e^{(-4+\sqrt{10})t} - e^{(-4-\sqrt{10})t} \right) u(t) = \mathbf{ \frac{8}{\sqrt{10}} e^{-4t} \sinh(\sqrt{10}t) u(t) \text{ A} } $$

*For $i_2(t)$:*
$$ I_2(s) = \frac{24}{s(s-p_1)(s-p_2)} = \frac{K_0}{s} + \frac{K_1}{s-p_1} + \frac{K_2}{s-p_2} $$
$$ K_0 = \frac{24}{p_1 p_2} = \frac{24}{(-4+\sqrt{10})(-4-\sqrt{10})} = \frac{24}{16 - 10} = 4 $$
$$ K_1 = \frac{24}{p_1(p_1 - p_2)} = \frac{24}{(-4+\sqrt{10})(2\sqrt{10})} = \frac{12}{-4\sqrt{10} + 10} = -2 - 0.8\sqrt{10} $$
$$ K_2 = \frac{24}{p_2(p_2 - p_1)} = \frac{24}{(-4-\sqrt{10})(-2\sqrt{10})} = \frac{12}{4\sqrt{10} + 10} = -2 + 0.8\sqrt{10} $$
$$ \mathbf{ i_2(t) = \left[ 4 - (2 + 0.8\sqrt{10})e^{(-4+\sqrt{10})t} + (-2 + 0.8\sqrt{10})e^{(-4-\sqrt{10})t} \right] u(t) \text{ A} } $$
*(Related location: Sadiku textbook, Chapter 16, Circuit Analysis in s-domain)*

***

### 31. Page 15, Q.4(c): (ii) An 8 V battery is connected to the network via a switch. If the switch is closed at t = 0, find the current i(t) through Y(s) using the Laplace transform.

**Solution:**
*(Note: Because this is part (ii) of a question, the definition of the network $Y(s)$ is required from part (i). Based on standard textbook problems matching this exact phrasing, we assume the known problem where the input admittance $Y(s)$ has a pole at $s = -3$, a zero at $s = -1$, and $Y(\infty) = 0.25 \text{ S}$).*

**1. Determine the Admittance $Y(s)$:**
Given a zero at $s=-1$ and a pole at $s=-3$, the form of the admittance is:
$$ Y(s) = K \frac{s+1}{s+3} $$
Applying the final value $Y(\infty) = 0.25$:
$$ \lim_{s \to \infty} Y(s) = \lim_{s \to \infty} K \frac{s(1 + 1/s)}{s(1 + 3/s)} = K = 0.25 \text{ S} $$
Thus, the admittance is:
$$ Y(s) = 0.25 \frac{s+1}{s+3} $$

**2. Formulate the circuit in the s-domain:**
An $8\text{V}$ battery connected at $t=0$ acts as a step input voltage $v(t) = 8u(t)\text{ V}$. 
Transforming the voltage source to the s-domain:
$$ V(s) = \frac{8}{s} $$

**3. Calculate the Current $I(s)$:**
By Ohm's law in the s-domain, $I(s) = Y(s) V(s)$:
$$ I(s) = \left( 0.25 \frac{s+1}{s+3} \right) \left( \frac{8}{s} \right) = \frac{2(s+1)}{s(s+3)} $$

**4. Inverse Laplace Transform:**
We use partial fraction expansion to find $i(t)$:
$$ I(s) = \frac{2(s+1)}{s(s+3)} = \frac{A}{s} + \frac{B}{s+3} $$
Solve for $A$ and $B$ using the residue method:
$$ A = \left. \frac{2(s+1)}{s+3} \right|_{s=0} = \frac{2(1)}{3} = \frac{2}{3} $$
$$ B = \left. \frac{2(s+1)}{s} \right|_{s=-3} = \frac{2(-3+1)}{-3} = \frac{-4}{-3} = \frac{4}{3} $$
Substituting the coefficients back:
$$ I(s) = \frac{2/3}{s} + \frac{4/3}{s+3} $$
Taking the inverse Laplace transform of each term:
$$ \mathbf{ i(t) = \left( \frac{2}{3} + \frac{4}{3}e^{-3t} \right) u(t) \text{ A} } $$
*(Related location: Sadiku textbook, Chapter 16, Problem 16.104)*

***

### 32. Page 23, Q.1: For the following circuit shown in Fig. 1 fill the table (right). Assume that the switch of the following circuit was closed for a long time and is opened at t=0s. (Figure Involved)

**Solution:**
Based on the schematic, the circuit consists of a top common node connected to ground through four parallel branches:
1.  A $1\Omega$ resistor carrying a downward current labeled $i_x$.
2.  A dependent current source of value $9i_x$ pointing downwards.
3.  A $1\text{F}$ capacitor.
4.  A switch connected in series with a $5\text{V}$ DC source.

**1. Analysis for $t < 0$ (Initial Conditions):**
The switch is closed for a long time, establishing DC steady state. 
*   The switch directly connects the top node to the positive terminal of the $5\text{V}$ source, holding the entire top node at $5\text{V}$.
*   Therefore, the initial voltage across the capacitor is entirely dictated by this source:
$$ \mathbf{v_c(0^-) = 5 \text{ V}} $$
By continuity, $v_c(0^+) = v_c(0^-) = 5\text{ V}$.

**2. Analysis for $t > 0$ (Time Constant $\tau$):**
At $t=0$, the switch opens, disconnecting the $5\text{V}$ source. The circuit becomes a source-free parallel RC circuit with a dependent source. We need to find the equivalent resistance $R_{eq}$ seen by the capacitor to determine the time constant $\tau = R_{eq}C$.
*   Let the voltage at the top node be $v$. 
*   The current down through the $1\Omega$ resistor is $i_x = \frac{v}{1} = v$.
*   Apply Kirchhoff's Current Law (KCL) at the top node for $t > 0$:
$$ i_C + i_{R} + i_{dep} = 0 $$
$$ C \frac{dv}{dt} + i_x + 9i_x = 0 $$
Substitute $i_x = v$ and $C = 1\text{F}$:
$$ 1 \frac{dv}{dt} + v + 9v = 0 \implies \frac{dv}{dt} + 10v = 0 $$
This is a standard first-order differential equation of the form $\frac{dv}{dt} + \frac{1}{\tau}v = 0$. By matching coefficients, we see that $\frac{1}{\tau} = 10$, so the time constant is:
$$ \mathbf{\tau = 0.1 \text{ s}} $$

**3. Calculate $v_c(t = 1\text{s})$:**
The general solution for the source-free RC circuit voltage is $v_c(t) = v_c(0) e^{-t/\tau}$.
$$ v_c(t) = 5 e^{-t/0.1} = 5 e^{-10t} \text{ V} $$
Substitute $t = 1\text{ s}$ into the equation:
$$ v_c(1) = 5 e^{-10(1)} = 5 e^{-10} \text{ V} $$
$$ \mathbf{v_c(1) \approx 2.27 \times 10^{-4} \text{ V}} $$

**Filled Table Values:**
*   (i) Time constant, $\tau$ $\rightarrow$ **$0.1 \text{ s}$**
*   (ii) $V_c(0^-)$ $\rightarrow$ **$5 \text{ V}$**
*   (iii) $V_c(t=1s)$ $\rightarrow$ **$5e^{-10} \text{ V}$** (or $2.27 \times 10^{-4} \text{ V}$)

*(Related location: Sadiku textbook, Chapter 7, Section 7.2 Source-Free RC Circuit and Dependent Sources)*

Based on the document provided, here are the detailed step-by-step solutions for the next 4 questions (Questions 33 to 36).

### 33. Page 26, Q (Handwritten 1): Design a first order RC circuit which capacitor voltage is $v_c = 50 - 100e^{-2000t}$ [Hint: sketch the graph of vc vs t to understand it properly].

**Solution:**
To design a first-order RC circuit that produces this specific voltage response, we need to extract the key characteristics from the given equation: $v_c(t) = 50 - 100e^{-2000t}$ V (for $t \ge 0$).

**1. Determine the key parameters of the response:**
*   **Initial Voltage $v_c(0)$:** Substitute $t = 0$ into the equation.
    $$ v_c(0) = 50 - 100e^0 = 50 - 100 = -50 \text{ V} $$
*   **Steady-State (Final) Voltage $v_c(\infty)$:** Substitute $t \to \infty$ into the equation.
    $$ v_c(\infty) = 50 - 100(0) = 50 \text{ V} $$
*   **Time Constant ($\tau$):** The exponential term is of the form $e^{-t/\tau}$. Here, the term is $e^{-2000t}$.
    $$ \frac{1}{\tau} = 2000 \implies \tau = \frac{1}{2000} = 0.0005 \text{ s} = 0.5 \text{ ms} $$

**2. Design the Circuit:**
The standard step response of a series RC circuit connected to a DC voltage source $V_s$ is given by:
$$ v_c(t) = v_c(\infty) + [v_c(0) - v_c(\infty)] e^{-t/\tau} $$
Checking our parameters against this formula:
$$ v_c(t) = 50 + [-50 - 50] e^{-2000t} = 50 - 100e^{-2000t} $$
This matches the given equation perfectly. 

To realize this physically:
*   We need a DC voltage source $V_s$ equal to the final steady-state voltage: **$V_s = 50 \text{ V}$**.
*   We need a capacitor with an initial voltage: **$V_0 = -50 \text{ V}$** (meaning the initial polarity is opposite to the source voltage).
*   We need the product of $R$ and $C$ to equal the time constant: $RC = 0.0005 \text{ s}$. 
    Let's choose a standard, reasonable capacitor value, for example, **$C = 1 \mu\text{F} = 10^{-6} \text{ F}$**.
    Then, calculate the required resistance:
    $$ R = \frac{\tau}{C} = \frac{0.0005}{10^{-6}} = \mathbf{500 \Omega} $$

**Final Design:**
The circuit consists of a **$50 \text{ V}$ DC voltage source** connected in series with a switch (that closes at $t=0$), a **$500 \Omega$ resistor**, and a **$1 \mu\text{F}$ capacitor**. The capacitor must be pre-charged with an initial voltage of **$-50 \text{ V}$** (the positive terminal of the initial voltage opposing the positive terminal of the 50V source).

*(Related location: Sadiku textbook, Chapter 7, Section 7.5 Step Response of an RC Circuit)*

***

### 34. Page 26, Q (Handwritten 2): The switch closes at t>0. Find the inductor current when the switch is closed. [Figure Involved]

**Solution:**
Based on the handwritten circuit diagram, we have a $24\text{V}$ DC source, a switch that closes at $t=0$, a $16 \Omega$ resistor in series, and then a parallel combination of two branches: a $40 \Omega$ resistor branch and a branch with a $10 \Omega$ resistor in series with a $20 \text{ H}$ inductor. We need to find the current $i(t)$ flowing down through the inductor branch for $t > 0$.

**1. Initial Conditions ($t < 0$):**
Before the switch closes, the circuit is open, and no power is supplied to the inductor. Assuming it has been in this state for a long time, the inductor is completely unenergized.
$$ i(0^-) = 0 \text{ A} $$
Because current through an inductor cannot change instantaneously, $i(0^+) = 0 \text{ A}$.

**2. Steady-State Conditions ($t \to \infty$):**
When the switch has been closed for a long time, the circuit reaches DC steady state, and the $20 \text{ H}$ inductor acts as a short circuit ($0 \Omega$).
The circuit simplifies to a $24\text{V}$ source in series with the $16 \Omega$ resistor, which then splits into a $40 \Omega$ resistor and a $10 \Omega$ resistor in parallel.
*   Equivalent resistance of the parallel part: $R_p = 40 || 10 = \frac{40 \times 10}{40 + 10} = \frac{400}{50} = 8 \Omega$.
*   Total circuit resistance: $R_{total} = 16 \Omega + 8 \Omega = 24 \Omega$.
*   Total current from the source: $I_s = \frac{24\text{V}}{24\Omega} = 1 \text{ A}$.
*   Using current division to find the current $i(\infty)$ through the $10 \Omega$ (inductor) branch:
$$ i(\infty) = I_s \times \frac{40}{40 + 10} = 1 \times \frac{40}{50} = \mathbf{0.8 \text{ A}} $$

**3. Thevenin Resistance and Time Constant ($t > 0$):**
To find the time constant, we determine the Thevenin equivalent resistance $R_{th}$ seen by the inductor. 
We turn off the $24\text{V}$ voltage source (replace with a short circuit) and look into the terminals where the inductor is connected.
*   The $16 \Omega$ and $40 \Omega$ resistors are in parallel: $16 || 40 = \frac{16 \times 40}{16 + 40} = \frac{640}{56} = \frac{80}{7} \Omega \approx 11.43 \Omega$.
*   This combination is in series with the $10 \Omega$ resistor in the inductor's branch.
*   Total equivalent resistance seen by inductor: $R_{eq} = \frac{80}{7} + 10 = \frac{150}{7} \Omega$.
*   The time constant is:
$$ \tau = \frac{L}{R_{eq}} = \frac{20}{\frac{150}{7}} = \frac{140}{150} = \mathbf{\frac{14}{15} \text{ s}} \approx 0.933 \text{ s} $$

**4. Formulate the Final Equation:**
Using the general step response formula for a first-order RL circuit:
$$ i(t) = i(\infty) + [i(0) - i(\infty)] e^{-t/\tau} $$
$$ i(t) = 0.8 + [0 - 0.8] e^{-\frac{15}{14}t} $$
$$ \mathbf{i(t) = 0.8 \left( 1 - e^{-\frac{15}{14}t} \right) \text{ A}} \quad \text{for } t > 0 $$

*(Related location: Sadiku textbook, Chapter 7, Section 7.6 Step Response of an RL Circuit)*

***

### 35. Page 30, Q.1: The switch in the circuit closes at time t = 0. Determine the voltage v(t) after the switch closes using Laplace technique. [Figure Involved]

**Solution:**
From the schematic, the circuit consists of a $12\text{V}$ DC source. A $4\Omega$ resistor has a switch in parallel with it that closes at $t=0$. This is followed by a $2\Omega$ resistor in series. Then the circuit splits into a parallel combination of a $2\text{H}$ inductor and a $0.125\text{F}$ capacitor to ground. $v(t)$ is the voltage across the parallel LC pair.

**1. Initial Conditions ($t < 0$):**
Before the switch closes, the circuit is in DC steady state. The $12\text{V}$ source is in series with the $4\Omega$ and $2\Omega$ resistors. 
*   The capacitor acts as an open circuit.
*   The inductor acts as a short circuit to ground.
*   Therefore, the steady-state voltage across the shorted inductor (and the parallel capacitor) is zero: **$v(0^-) = 0 \text{ V}$**.
*   The initial current flowing through the inductor is:
$$ i_L(0^-) = \frac{12\text{V}}{4\Omega + 2\Omega} = \frac{12}{6} = \mathbf{2 \text{ A}} $$
Due to continuity, $v(0^+) = 0 \text{ V}$ and $i_L(0^+) = 2 \text{ A}$.

**2. S-Domain Transformation ($t > 0$):**
At $t=0$, the switch closes, completely shorting out the $4\Omega$ resistor. The circuit for $t > 0$ consists of the $12\text{V}$ source, the $2\Omega$ resistor, and the parallel LC pair.
We transform this into the Laplace domain:
*   Voltage source: $V_s(s) = \frac{12}{s}$
*   Resistor: $R = 2 \Omega$
*   Capacitor: $Z_C(s) = \frac{1}{sC} = \frac{1}{0.125s} = \frac{8}{s} \Omega$. (No initial voltage source needed as $v(0)=0$).
*   Inductor: $Z_L(s) = sL = 2s \Omega$. It has an initial current $i_L(0) = 2\text{ A}$ flowing downwards. In parallel representation, this is a current source $\frac{i_L(0)}{s} = \frac{2}{s}$ pointing downwards.

**3. Nodal Analysis in the S-Domain:**
Let $V(s)$ be the voltage at the node above the LC pair. Apply KCL at this node:
$$ \frac{V(s) - \frac{12}{s}}{2} + \frac{V(s)}{8/s} + \frac{V(s)}{2s} + \frac{2}{s} = 0 $$
$$ \frac{V(s)}{2} - \frac{6}{s} + \frac{sV(s)}{8} + \frac{V(s)}{2s} + \frac{2}{s} = 0 $$
Group the $V(s)$ terms and move the constant terms to the right:
$$ V(s) \left( \frac{1}{2} + \frac{s}{8} + \frac{1}{2s} \right) = \frac{6}{s} - \frac{2}{s} = \frac{4}{s} $$
Multiply the equation by $8s$ to clear the fractions:
$$ V(s) \left( 4s + s^2 + 4 \right) = 32 $$
$$ V(s) (s^2 + 4s + 4) = 32 $$
$$ V(s) = \frac{32}{s^2 + 4s + 4} = \frac{32}{(s+2)^2} $$

**4. Inverse Laplace Transform:**
The expression $V(s) = \frac{32}{(s+2)^2}$ matches the standard Laplace transform pair $\mathcal{L}^{-1}\left\{\frac{1}{(s+a)^2}\right\} = t e^{-at} u(t)$.
$$ \mathbf{v(t) = 32 t e^{-2t} u(t) \text{ V}} $$
*(This indicates a critically damped response, which aligns with $\alpha = \frac{1}{2RC} = \frac{1}{2(2)(0.125)} = 2$ and $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{2(0.125)}} = 2$)*.

*(Related location: Sadiku textbook, Chapter 16, Section 16.3 Circuit Analysis)*

***

### 36. Page 33, Q.2: The switch of the following circuit was opened for long period of time, and is closed at t = 0s. Fill the table for the circuit parameters: R1=2Ω, R2 = 2Ω, C = 1F. The input is Vs= 10 u(−t). [Figure Involved]

**Solution:**
Based on the schematic, we have a voltage source $V_s$ connected to $R_1$. The other side of $R_1$ is a node. From this node, a capacitor $C$ connects to ground. Also from this node, a switch connects to $R_2$, which goes to ground.
The input is given as $V_s = 10 u(-t) \text{ V}$. This means:
*   $V_s = 10 \text{ V}$ for $t < 0$
*   $V_s = 0 \text{ V}$ for $t > 0$

**1. Initial Conditions ($t < 0$):**
The problem states the switch was "opened for long period of time".
*   The circuit consists of the $10\text{V}$ source, $R_1 = 2\Omega$, and the capacitor $C = 1\text{F}$ in series. $R_2$ is disconnected.
*   In DC steady state, the capacitor acts as an open circuit, so no current flows. 
*   The capacitor fully charges to the source voltage: **$V_c(0^-) = 10 \text{ V}$**.
*   The current through the capacitor is zero: **$i_c(0^-) = 0 \text{ A}$**.

**2. Conditions Immediately After Switching ($t = 0^+$):**
At $t=0$, the switch closes, connecting $R_2$ across the capacitor. Simultaneously, the voltage source $V_s$ drops to $0\text{ V}$ (acts as a short circuit to ground).
*   Because capacitor voltage cannot change instantaneously, **$V_c(0^+) = 10 \text{ V}$**.
*   The circuit now consists of the capacitor discharging through two parallel paths to ground: $R_1$ and $R_2$.
*   To find $i_c(0^+)$, we use KCL at the top node. Assuming standard passive sign convention where $i_c$ points downwards:
$$ i_c(0^+) + i_{R1}(0^+) + i_{R2}(0^+) = 0 $$
$$ i_c(0^+) + \frac{V_c(0^+)}{R_1} + \frac{V_c(0^+)}{R_2} = 0 $$
$$ i_c(0^+) + \frac{10}{2} + \frac{10}{2} = 0 \implies i_c(0^+) + 5 + 5 = 0 \implies \mathbf{i_c(0^+) = -10 \text{ A}} $$

**3. Transient Response ($t > 0$):**
The circuit is a source-free parallel RC circuit. The capacitor discharges through the equivalent resistance $R_{eq}$ of $R_1$ and $R_2$ in parallel:
*   $R_{eq} = R_1 || R_2 = 2 || 2 = 1 \Omega$.
*   Time constant: $\tau = R_{eq} C = 1 \Omega \times 1 \text{F} = \mathbf{1 \text{ s}}$.
*   The voltage equation is:
$$ V_c(t) = V_c(0) e^{-t/\tau} = 10 e^{-t} \text{ V} $$
*   The current equation (downwards) is:
$$ i_c(t) = C \frac{dV_c}{dt} = 1 \times (-10 e^{-t}) = -10 e^{-t} \text{ A} $$

**4. Values at $t = 6\text{s}$:**
*   **$V_c(6) = 10 e^{-6} \text{ V}$** (approx. $0.0248 \text{ V}$)
*   **$i_c(6) = -10 e^{-6} \text{ A}$** (approx. $-0.0248 \text{ A}$)

**Filled Table Values:**
*   **(i) $V_c, t=0\text{s}$ :** $\mathbf{10 \text{ V}}$ (Evaluating at $t=0^+$)
*   **(ii) $i_c, t=0\text{s}$ :** $\mathbf{-10 \text{ A}}$ (Evaluating at $t=0^+$)
*   **(iii) $V_c, t=6\text{s}$ :** $\mathbf{10e^{-6} \text{ V}}$
*   **(iv) $i_c, t=6\text{s}$ :** $\mathbf{-10e^{-6} \text{ A}}$

*(Related location: Sadiku textbook, Chapter 7, Section 7.2 Source-Free RC Circuit)*



Based on the provided document, here are the full texts and detailed step-by-step solutions for the next 4 questions (Questions 37 to 40).

### 37. Page 34, Q.2: The switch of the following circuit was opened for long period of time, and is closed at t = 0s. Fill the table for the circuit parameters: R1=1$\Omega$, R2 = 1$\Omega$, C = 1F. The input is a step signal having magnitude of 10 V.
*(Image shows a voltage source $V_s$ connected to $R_1$, then a node with a capacitor $C$ to ground and a switch to $R_2$ to ground. A table is provided to fill in values for $V_c(0^-)$, $V_c$ for $t>0$, $i_c(0^-)$, $i_c$ for $t>0$, $\tau$ for $t<0$, and $\tau$ for $t>0$.)*

**Solution:**
The input is a step signal of $10\text{ V}$, which means $V_s(t) = 10u(t) \text{ V}$. This implies $V_s = 0\text{ V}$ for $t < 0$ and $V_s = 10\text{ V}$ for $t > 0$.

**1. Analysis for $t < 0$:**
*   The switch is OPEN. The voltage source is $0\text{ V}$.
*   The circuit is just a $0\text{ V}$ source in series with $R_1$ and $C$.
*   Since there is no active source, the capacitor is completely uncharged.
*   **$V_c(0^-) = 0 \text{ V}$**
*   **$i_c(0^-) = 0 \text{ A}$**
*   The time constant of the circuit in this state (if it had a source to respond to) would just involve $R_1$ and $C$.
*   **$\tau (t < 0) = R_1 \times C = 1\Omega \times 1\text{F} = 1 \text{ s}$**

**2. Analysis for $t > 0$:**
*   At $t = 0$, the switch CLOSES, and the voltage source becomes $10\text{ V}$.
*   The circuit now has the $10\text{ V}$ source and $R_1$ in series, driving the parallel combination of the capacitor $C$ and resistor $R_2$.
*   To find the response, we determine the Thevenin equivalent circuit seen by the capacitor.
    *   **Thevenin Resistance ($R_{th}$):** Turn off the source (short it to ground). Looking from the capacitor's terminals, $R_1$ and $R_2$ are in parallel.
        $$ R_{th} = R_1 || R_2 = \frac{1 \times 1}{1 + 1} = 0.5 \Omega $$
    *   **Thevenin Voltage ($V_{th}$):** The open-circuit voltage across the capacitor's terminals (with the capacitor removed). It's a simple voltage divider between $R_1$ and $R_2$:
        $$ V_{th} = V_s \times \frac{R_2}{R_1 + R_2} = 10 \times \frac{1}{1 + 1} = 5 \text{ V} $$
*   The new time constant is:
    *   **$\tau (t > 0) = R_{th} \times C = 0.5\Omega \times 1\text{F} = 0.5 \text{ s}$**
*   The capacitor voltage will exponentially approach the Thevenin voltage ($5\text{V}$) from its initial voltage ($0\text{V}$):
    *   **$V_c(t) = V_{th} + (V_c(0) - V_{th}) e^{-t/\tau} = 5 + (0 - 5) e^{-t/0.5} = \mathbf{5(1 - e^{-2t}) \text{ V}}$**
*   The capacitor current is found by taking the derivative of the voltage:
    *   **$i_c(t) = C \frac{dV_c}{dt} = 1 \times \frac{d}{dt}(5 - 5e^{-2t}) = 1 \times (-5 \times -2) e^{-2t} = \mathbf{10 e^{-2t} \text{ A}}$**

**Filled Table Values:**
*   (i) $V_c(0^-)$ $\rightarrow$ **$0 \text{ V}$**
*   (ii) $V_c, t>0$ $\rightarrow$ **$5(1 - e^{-2t}) \text{ V}$**
*   (iii) $i_c(0^-)$ $\rightarrow$ **$0 \text{ A}$**
*   (iv) $i_c, t>0$ $\rightarrow$ **$10 e^{-2t} \text{ A}$**
*   (v) $\tau, t<0$ $\rightarrow$ **$1 \text{ s}$**
*   (vi) $\tau, t>0$ $\rightarrow$ **$0.5 \text{ s}$**

***

### 38. Page 39, CT-02 Q.2: For the circuit in Fig. $v(t) = 90e^{-50t}V$ and $i(t) = 30e^{-50t}A$ at $t > 0$. (i) Find L and R. (ii) Determine the time constant. (iii) Calculate the initial energy in the inductor. (iv) What fraction of the initial energy is dissipated in 10 ms?
*(Image shows a source-free RL circuit with a resistor R and an inductor L in a single closed loop. Current $i$ flows from R to L, and voltage $v$ is across L).*

**Solution:**
The circuit is a source-free RL loop. The current $i(t)$ flows through both elements. The voltage $v(t)$ is given across the inductor.

**1. Find R and L:**
*   In a source-free RL circuit, the current decays exponentially: $i(t) = I_0 e^{-t/\tau}$. Comparing this with the given $i(t) = 30e^{-50t}\text{ A}$, we can see that the initial current is $I_0 = 30\text{ A}$ and the inverse of the time constant is $\frac{1}{\tau} = 50\text{ s}^{-1}$.
*   The voltage across an inductor is given by $v_L(t) = L \frac{di}{dt}$.
    $$ v_L(t) = L \frac{d}{dt}(30e^{-50t}) = L (30)(-50)e^{-50t} = -1500L e^{-50t} \text{ V} $$
*   The problem gives the voltage magnitude as $v(t) = 90e^{-50t}\text{ V}$. Assuming standard passive sign convention where the magnitude $|v| = |L \frac{di}{dt}|$:
    $$ |-1500L| = 90 \implies 1500L = 90 \implies L = \frac{90}{1500} = \mathbf{0.06 \text{ H}} \text{ (or } 60 \text{ mH)} $$
*   The time constant for an RL circuit is $\tau = \frac{L}{R}$. We know $\frac{1}{\tau} = \frac{R}{L} = 50$.
    $$ \frac{R}{0.06} = 50 \implies R = 50 \times 0.06 = \mathbf{3 \Omega} $$

**2. Determine the time constant:**
*   From the exponential term $e^{-50t}$, we know $\frac{1}{\tau} = 50$.
    $$ \tau = \frac{1}{50} = \mathbf{0.02 \text{ s}} \text{ (or } 20 \text{ ms)} $$

**3. Calculate the initial energy in the inductor:**
*   The initial energy $W(0)$ stored in the magnetic field of the inductor is:
    $$ W(0) = \frac{1}{2} L i(0)^2 = \frac{1}{2} (0.06\text{ H}) (30\text{ A})^2 $$
    $$ W(0) = 0.03 \times 900 = \mathbf{27 \text{ Joules}} $$

**4. Fraction of initial energy dissipated in 10 ms:**
*   The energy stored in the inductor as a function of time is $W(t) = \frac{1}{2} L i(t)^2$.
*   Since $i(t) = I_0 e^{-t/\tau}$, then $W(t) = \frac{1}{2} L (I_0 e^{-t/\tau})^2 = \left(\frac{1}{2} L I_0^2\right) e^{-2t/\tau} = W(0) e^{-2t/\tau}$.
*   At $t = 10\text{ ms} = 0.01\text{ s}$, the remaining energy is:
    $$ W(0.01) = 27 e^{-2(0.01)/0.02} = 27 e^{-2(0.5)} = 27 e^{-1} \text{ J} $$
*   The energy dissipated by the resistor is the difference between initial and remaining energy:
    $$ W_{dissip} = W(0) - W(0.01) = 27 - 27e^{-1} = 27(1 - e^{-1}) \text{ J} $$
*   The fraction of energy dissipated is:
    $$ \text{Fraction} = \frac{W_{dissip}}{W(0)} = \frac{27(1 - e^{-1})}{27} = 1 - e^{-1} $$
    $$ \text{Fraction} \approx 1 - 0.3679 = \mathbf{0.6321 \text{ or } 63.21\%} $$

***

