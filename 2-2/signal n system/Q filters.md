Based on the provided PDF, here are the full texts of the questions related to the requested topics under **Filters**, organized accordingly. Exact word-for-word duplicates have been filtered to keep only one instance.

### **Analog filter design**

*   **Page 8, Q.8(b):** Design a Butterworth low pass filter which has the following transfer characteristics. [Figure Involved]
*   **Page 10, Q.6(a):** Show that the decibel gain curve of Butterworth filter is smaller compared to Chebyshev filter at large frequencies.
*   **Page 10, Q.6(b):** Write the steps to design a Chebyshev filter.
*   **Page 13, Q.8(a):** Prove that $\epsilon = \sqrt{10^{0.1A_{max}}-1}$ and $n = \frac{\cosh^{-1}(\sqrt{(10^{0.1A_{min}}-1)/\epsilon^2})}{\cosh^{-1}(\omega_s/\omega_p)}$ for Chebyshev filter; where symbols have their usual meanings. *(Note: Mathematical symbols transcribed as closely as possible from original image)*
*   **Page 13, Q.8(b):** A low-pass filter is to be designed according to the following specifications.
    (i) $R_L = 600$ ohms, (ii) $f_c = 1400$ cps ($\omega_c = 8800$ rps), (iii) ripple specification is that $20\log_{10} \frac{\text{peak magnitude}}{\text{valley magnitude}} = 1$ dB, (iv) slope of the decibel gain curve is to be -40 dB/decade, (v) $|G(j0)|$ must be unity.
*   **Page 16, Q.8(b):** Design a low-pass Butterworth filter having a slope of -80 dB/decade outside the pass band.
*   **Page 71, Q.8(a) (Top):** In context of filter performance characteristics, discuss Butterworth, Chebyshev and Elliptic filter approximations.
*   **Page 71, Q.8(a) (Middle):** Show that the slope in the stop-band region for Chebyshev design is greater than Butterworth.
*   **Page 71, Q.8(b) (Middle):** For the Butterworth low pass filter, find and sketch the poles on the complex S-plane when the slope of the decibel gain curve is -80 dB/decade.
*   **Page 71, Q.8(a) (Bottom):** What is modern filter? What are the differences between Butterworth and Chebyshev design?
*   **Page 71, Q.8(b) (Bottom):** Write down the algorithm for Butterworth filter design.
*   **Page 72, Q.8(b):** Draw the ideal and practical frequency responses of different types of filter and also distinguish between active and passive filter.

### **Low pass prototypes of modern filters**

*   **Page 16, Q.8(c):** Develop a normalized low-pass Chebyshev model with n=2, $\epsilon=0.663$, $\omega_c=1$ rps and $R_L=1 \Omega$. The magnitude of gain must be unity at $\omega=0$. Sketch the approximate shape of the decibel gain curve.
*   **Page 19, Q.8(b):** Design a normalized low pass Chebyshev model to meet the following specifications:
    (i) $R_L = 1k\Omega$ (ii) $\omega_c = 1$ rps (iii) The ripple specification is: $20\log_{10} \frac{\text{peak magnitude}}{\text{valley magnitude}} = 1.5$ dB (iv) Slop of the dB gain curve is to be -60 dB/decade at frequency much higher than cutoff. (v) G(j0) must be unity.
*   **Page 71, Q(c) (Top):** Find the transfer function of a Chebyshev lowpass filter to satisfy the following criteria.
    *   The ratio $r \le 2$ dB over a passband $0 < \omega \le 10$, $\omega_p = 10$ rad/s
    *   The stop band gain $G_s \le -20$dB for $\omega > 16.5$, $\omega_s = 16.5$ rad/s
*   **Page 71, Q.8(c) (Middle):** Construct the transfer function of the Chebyshev filter if $G(s)G(-s) = \frac{1}{1+0.5 C_3^2(s/j)}$.

### **Filter design and transformations**

*   **Page 10, Q.6(c):** Develop a band reject Butterworth filter with n = 2, $\omega_h = 60000$ rps, $\omega_l = 10000$ rps and $R_L = 1000\Omega$. Sketch the approximate shape of the decibel gain characteristics.
*   **Page 13, Q.6(c):** Develop a band-stop Butterworth filter with n = 2, $\omega_h = 60000$ rps, $\omega_l = 10000$ rps and $R_L = 10000\Omega$. Sketch the approximate shape of the decibel gain curve.
*   **Page 25, Q.1:** An input $x(t) = \frac{3}{2} + \frac{3}{\pi}\sum_{n=1}^{\infty}[\frac{1}{n}\sin(2\pi nt)]$ is appliled to an ideal high pass filter with unity gain, |H| = 1 and cutoff frequency, $\omega_c = 20$ rad/s.
    (a) Determine the output signal. (b) What would be range of $\omega_c$ of the filter so that first two harmonics will be blocked?
*   **Page 37, Q.1:** The following input signal is applied to an ideal band pass filer with gain, |H| = 1 and lower cutoff frequency, $\omega_1 = 6$ rad/s and upper cutoff frequency, $\omega_2 = 12$ rad/s. (a) Determine the output signal. (b) What would be the range of bandwidth and the corner frequency so that the filter allows only the fundamental component. [Figure Involved]
*   **Page 38, Q.1:** The following input signal is applied to an ideal low pass filer with gain, |H| = 1 and cutoff frequency, $\omega_c = 12$ rad/s. (a) Determine the output signal. (b) What would be range of $\omega_c$ of the filter to pass only the DC component. [Figure Involved]
*   **Page 71, Q.8(c) (Bottom):** A high pass Chebyshev filter is to be designed according to the following specifications:
    (i) $R_L = 600 \Omega$,
    (ii) (ii) $\omega_c = 8800$ rps,
    (iii) The ripple specification is $20\log_{10} \frac{\text{Peak Magnitude}}{\text{Valley Magnitude}} = 1$dB
    (iv) Slope of the decibel gain curve is to be -60 dB/decade at frequencies much lower than cut-off.
    (v) G (j0) must be unity.
*   **Page 72, Q.6(a):** If the sawtooth waveform in the following figure is applied to an ideal bandpass filter with the transfer function shown in the figure, determine the output. [Figure Involved]
*   **Page 72, Q.8(c):** Develop a band-stop Butterworth filter for the following specifications. Filter order: n = 3, Cut-off frequencies: $\omega_h = 60,000$ rps, $\omega_l = 10,000$ rps, Load resistance: $R_L = 1000\Omega$.

### **Active filters**

*   **Page 2, Q.3(c):** A second order active filter is shown below. (i) Find the transfer function. (ii) Find the impulse response. [Figure Involved]
*   **Page 24, Q.2:** A second-order active filter has the transfer function, $G(s) = \frac{1}{s^2 + (\beta+4)s + 4}$.
    (i) Find the response g(t) if $\beta = 0$.
    (ii) Sketch g(t) if $\beta = -4$.
    (iii) Plot poles and zeros in the complex S plane if $\beta = 4$.
    (iv) Find the range of $\beta$ for which the filter becomes stable.

### **Realization of higher order filters**

*   **Page 4, Q.8(c):** Design a low pass Butterworth filter with Sallen-Key topology to satisfy the following specifications.
    *   pass band gain $G_p > -3$ dB at 5 kHz
    *   stop band gain $G_p < -20$ dB at 50 kHz
    The nth order (up to 4th) Butterworth polynomial is given below. [Figure Involved (Table)]
*   **Page 8, Q.8(c):** Design a low pass Butterworth filter with Sallen-key topology to satisfy the following specifications.
    *   pass band gain $G_p > -3$ dB at 5kHz
    *   stop band gain $G_p < -40$ dB at 50 kHz
    The nth order (up to 5th) Butterworth polynomial is given below. [Figure Involved (Table)]
*   **Page 71, Q.8(b) (Top):** Design a low pass Butterworth filter with Sallen-key topology to satisfy the following specifications-
    *   Passband gain $G_p > -3dB$ with passband cutoff frequency $f_p = 10kHz$
    *   Stopband gain $G_s < -40dB$ with stopband cutoff frequency $f_s = 40kHz$
    The nth order (up to 5th) Butterworth polynomial is given below- [Figure Involved (Table)]

### **First and second order transfer functions**
*(Note: These refer specifically to extracting or analyzing mathematical properties of 1st/2nd order filters. Some crossover with Active Filters above).*

*   **Page 44, Q.1:** A second order filter circuit has the following transfer function: Find the range of k so that
    (i) The filter becomes stable.
    (ii) The filter provides oscillation
    $H(s) = \frac{10}{s^2 + (k-5)s + 10}$
*   **Page 57, Q.3(c):** A second order active circuit has the following transfer function, $H(s) = \frac{1}{s^2 + (\beta+4)s + 4}$. Find the impulse response if (i) $\beta = 0$, (ii) $\beta = -4$ and (iii) $\beta = -8$.

### **Realisation of passive filter circuits**
*(No specific questions exclusively defining or asking to realize a passive filter circuit from scratch using inductor/capacitor ladder networks were found, outside of the active Sallen-Key topologies and generic RLC analyses covered in other sections).*