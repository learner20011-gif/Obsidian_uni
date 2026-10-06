---
aliases:
---

---

### **Analog filter design**

### 1. Page 8, Q.8(b): Design a Butterworth low pass filter which has the following transfer characteristics.

```
       |Gn(jω)|
          ^
      1.0 |---------\
          |          \
          |           \
          |            \ -60 dB/decade
          +-------------\---------> ω
                        ωc
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-2 (*Butterworth Filters*), pp. 439–441, 458–460
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.1 (*Lowpass Filter*), Section 14.8.1 (*First-Order Lowpass Filter*), Section 14.9 (*Scaling*), pp. 638–639, 643, 648–651

---

#### **1. Determine the Filter Order ($n$)**
* For a Butterworth low-pass filter, each pole provides a high-frequency roll-off rate (slope) of $-20\text{ dB/decade}$.
* From the given frequency response characteristic, the slope in the stopband is:
  $$\text{Slope} = -60\text{ dB/decade}$$
* Therefore, the order of the filter $n$ is:
  $$n = \frac{\text{Given Slope}}{-20\text{ dB/decade/pole}} = \frac{-60}{-20} = 3$$

---

#### **2. Normalized Transfer Function ($H_n(s)$)**
For a 3rd-order normalized Butterworth low-pass filter ($\omega_c = 1\text{ rad/s}$):
* The Butterworth polynomial for $n = 3$ is:
  $$B_3(s) = (s + 1)(s^2 + s + 1) = s^3 + 2s^2 + 2s + 1$$
* The normalized transfer function with unity DC gain is:
  $$H_n(s) = \frac{1}{B_3(s)} = \frac{1}{s^3 + 2s^2 + 2s + 1}$$

---

#### **3. Circuit Realization**
A 3rd-order Butterworth low-pass filter can be realized using either a **passive LC ladder network** or an **active op-amp circuit (Sallen-Key topology)**.

##### **Method A: Passive LC Ladder Network Realization**
For a normalized 3rd-order filter terminated with a load resistor $R_L = 1\,\Omega$:
* The normalized low-pass prototype values (from standard filter tables) are:
  $$C_1 = 1.0\text{ F}, \quad L_2 = 2.0\text{ H}, \quad C_3 = 1.0\text{ F}$$
  or with series input inductor:
  $$L_1 = 1.0\text{ H}, \quad C_2 = 2.0\text{ F}, \quad L_3 = 1.0\text{ H}$$

##### **Method B: Active Filter Realization (Cascaded Stages)**
Since $n = 3$, the transfer function is factored into a first-order stage and a second-order stage:
$$H(s) = \left(\frac{1}{s + 1}\right) \left(\frac{1}{s^2 + s + 1}\right)$$
1. **Stage 1 (First-order RC low-pass filter):**
   * Transfer function: $H_1(s) = \frac{1}{1 + sR_1C_1}$
   * Choosing $R_1 = 1\,\Omega$, we get $C_1 = 1\text{ F}$.
2. **Stage 2 (Second-order Sallen-Key low-pass filter):**
   * Standard form: $H_2(s) = \frac{1}{s^2 + \frac{\omega_0}{Q}s + \omega_0^2}$
   * Comparing with $s^2 + s + 1$: $\omega_0 = 1\text{ rad/s}$, $Q = 1$.
   * A standard equal-component Sallen-Key low-pass section provides this response.

---

### 2. Page 10, Q.6(a): Show that the decibel gain curve of Butterworth filter is smaller compared to Chebyshev filter at large frequencies.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-4 (*Chebyshev Filters*), pp. 440–441, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

---

#### **1. Magnitude Response at Large Frequencies**

* **Butterworth Filter:**
  The magnitude response of an $n$-th order Butterworth filter is:
  $$|H_B(j\omega)| = \frac{1}{\sqrt{1 + \left(\frac{\omega}{\omega_0}\right)^{2n}}}$$
  For high frequencies where $\omega \gg \omega_0$:
  $$|H_B(j\omega)| \approx \frac{1}{\left(\frac{\omega}{\omega_0}\right)^n} = \left(\frac{\omega_0}{\omega}\right)^n$$
  Expressing the gain in decibels ($\text{Gain}_{\text{dB}} = 20\log_{10}|H(j\omega)|$):
  $$G_{\text{dB}, B} \approx 20\log_{10}\left[\left(\frac{\omega}{\omega_0}\right)^{-n}\right] = -20n\log_{10}\left(\frac{\omega}{\omega_0}\right)$$

* **Chebyshev Filter:**
  The magnitude response of an $n$-th order Chebyshev filter is:
  $$|H_C(j\omega)| = \frac{1}{\sqrt{1 + \epsilon^2 C_n^2\left(\frac{\omega}{\omega_0}\right)}}$$
  where $C_n(x)$ is the Chebyshev polynomial of order $n$. For $x = \frac{\omega}{\omega_0} \gg 1$:
  $$C_n(x) \approx 2^{n-1}x^n = 2^{n-1}\left(\frac{\omega}{\omega_0}\right)^n$$
  Therefore, for $\omega \gg \omega_0$:
  $$|H_C(j\omega)| \approx \frac{1}{\sqrt{\epsilon^2 \left[2^{n-1}\left(\frac{\omega}{\omega_0}\right)^n\right]^2}} = \frac{1}{\epsilon \, 2^{n-1}\left(\frac{\omega}{\omega_0}\right)^n}$$
  Expressing this gain in decibels:
  $$G_{\text{dB}, C} \approx -20\log_{10}\left[\epsilon \, 2^{n-1}\left(\frac{\omega}{\omega_0}\right)^n\right]$$
  $$G_{\text{dB}, C} \approx -20n\log_{10}\left(\frac{\omega}{\omega_0}\right) - 20\log_{10}(\epsilon) - 20(n - 1)\log_{10}(2)$$

---

#### **2. Comparison of the Gain Curves**
Subtracting the two decibel gains:
$$G_{\text{dB}, C} - G_{\text{dB}, B} = - \left[20\log_{10}(\epsilon) + 20(n - 1)\log_{10}(2)\right]$$
* Since $20\log_{10}(2) \approx 6.02\text{ dB}$, for large $n$, the term $20(n-1)\log_{10}(2) \approx 6(n-1)\text{ dB}$ is a large positive quantity.
* Consequently:
  $$G_{\text{dB}, C} < G_{\text{dB}, B}$$
* Because the gain in decibels is negative in the stopband, a smaller (more negative) algebraic gain means the **Chebyshev filter has significantly greater attenuation** (less transmission) than the Butterworth filter at large frequencies. 
* Conversely, if comparing absolute gain magnitudes:
  $$|H_C(j\omega)| \ll |H_B(j\omega)| \quad \text{for } \omega \gg \omega_0$$
Hence, the Chebyshev filter provides much sharper rolloff and smaller gain than the Butterworth filter of the same order at large frequencies.

---

### 3. Page 10, Q.6(b): Write the steps to design a Chebyshev filter.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-4 (*Chebyshev Filters*), pp. 440–441, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

To design an analog Chebyshev low-pass filter, follow this systematic procedure:

1. **Specify Filter Requirements:**
   * Maximum passband attenuation (ripple): $A_{\max}$ (in dB) or $\alpha_p$.
   * Minimum stopband attenuation: $A_{\min}$ (in dB) or $\alpha_s$.
   * Passband edge frequency: $\omega_p$ (or $f_p$).
   * Stopband edge frequency: $\omega_s$ (or $f_s$).

2. **Calculate the Ripple Factor ($\epsilon$):**
   $$\epsilon = \sqrt{10^{0.1 A_{\max}} - 1}$$

3. **Determine the Filter Order ($n$):**
   * Using the selectivity factor $k = \frac{\omega_p}{\omega_s}$ and discrimination factor:
     $$n \ge \frac{\cosh^{-1}\left(\sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}\right)}{\cosh^{-1}\left(\frac{\omega_s}{\omega_p}\right)}$$
   * Round $n$ up to the next nearest integer.

4. **Determine the Poles of the Normalized Filter:**
   * Calculate the parameter $a$:
     $$a = \frac{1}{n} \sinh^{-1}\left(\frac{1}{\epsilon}\right)$$
   * The left-half $s$-plane poles $s_k = -\sigma_k \pm j\omega_k$ for $k = 1, 2, \dots, n$ lie on an ellipse given by:
     $$\sigma_k = \sinh(a) \sin\left(\frac{2k - 1}{2n}\pi\right)$$
     $$\omega_k = \cosh(a) \cos\left(\frac{2k - 1}{2n}\pi\right)$$

5. **Formulate the Normalized Transfer Function $H_n(s)$:**
   $$H_n(s) = \frac{H_0}{\prod_{k=1}^n (s - s_k)}$$
   where $H_0$ is chosen such that:
   * For $n$ odd: $H_n(0) = 1$ ($0\text{ dB}$)
   * For $n$ even: $H_n(0) = \frac{1}{\sqrt{1 + \epsilon^2}}$ (attenuated by the ripple value at DC).

6. **Frequency and Impedance Scaling:**
   * **Frequency Scaling:** Replace $s$ with $\frac{s}{\omega_p}$ to shift the cutoff to the desired passband edge.
   * **Impedance Scaling:** Scale resistors, inductors, and capacitors by factor $k_m = \frac{R_{\text{desired}}}{R_{\text{norm}}}$.

7. **Circuit Realization:**
   * Synthesize the scaled transfer function using active topologies (e.g., cascaded Sallen-Key stages) or passive LC ladder networks.

---

### 4. Page 13, Q.8(a): Prove that $\epsilon = \sqrt{10^{0.1A_{\max}} - 1}$ and $n = \frac{\cosh^{-1}\left(\sqrt{(10^{0.1A_{\min}}-1)/\epsilon^2}\right)}{\cosh^{-1}(\omega_s/\omega_p)}$ for Chebyshev filter; where symbols have their usual meanings. (Note: Mathematical symbols transcribed as closely as possible from original image)

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-5 (*Practical Filters and Their Specifications*), Section 4.12-4 (*Chebyshev Filters*), pp. 444–445, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

---

#### **1. Derivation of the Ripple Factor $\epsilon$**
The magnitude response of a low-pass Chebyshev filter is given by:
$$|H(j\omega)|^2 = \frac{1}{1 + \epsilon^2 C_n^2\left(\frac{\omega}{\omega_p}\right)}$$
where $C_n(x)$ is the Chebyshev polynomial of order $n$.

* At the passband edge frequency $\omega = \omega_p$, we have $\frac{\omega}{\omega_p} = 1$.
* By definition of Chebyshev polynomials, $C_n(1) = 1$ for all orders $n$.
* Therefore, the magnitude at the edge of the passband is:
  $$|H(j\omega_p)|^2 = \frac{1}{1 + \epsilon^2}$$
* The maximum passband attenuation $A_{\max}$ in decibels is defined as:
  $$A_{\max} = -10 \log_{10} |H(j\omega_p)|^2 = 10 \log_{10}\left(1 + \epsilon^2\right)$$
* Dividing by 10:
  $$0.1 A_{\max} = \log_{10}\left(1 + \epsilon^2\right)$$
* Taking the antilogarithm ($10^x$):
  $$10^{0.1 A_{\max}} = 1 + \epsilon^2$$
  $$\epsilon^2 = 10^{0.1 A_{\max}} - 1$$
* Taking the square root gives:
  $$\epsilon = \sqrt{10^{0.1 A_{\max}} - 1} \quad \text{--- (Proved)}$$

---

#### **2. Derivation of the Filter Order $n$**
* At the stopband edge frequency $\omega = \omega_s$, the minimum attenuation is $A_{\min}$ (in dB):
  $$A_{\min} = -10 \log_{10} |H(j\omega_s)|^2 = 10 \log_{10}\left[1 + \epsilon^2 C_n^2\left(\frac{\omega_s}{\omega_p}\right)\right]$$
* Dividing by 10 and taking the inverse logarithm:
  $$10^{0.1 A_{\min}} = 1 + \epsilon^2 C_n^2\left(\frac{\omega_s}{\omega_p}\right)$$
* Solving for $C_n^2\left(\frac{\omega_s}{\omega_p}\right)$:
  $$\epsilon^2 C_n^2\left(\frac{\omega_s}{\omega_p}\right) = 10^{0.1 A_{\min}} - 1$$
  $$C_n\left(\frac{\omega_s}{\omega_p}\right) = \sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}$$

* Since $\omega_s > \omega_p$, the ratio $x = \frac{\omega_s}{\omega_p} > 1$.
* In the region $x > 1$, the Chebyshev polynomial is defined as:
  $$C_n(x) = \cosh\left(n \cosh^{-1}(x)\right)$$
* Setting this equal to the expression above:
  $$\cosh\left(n \cosh^{-1}\left(\frac{\omega_s}{\omega_p}\right)\right) = \sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}$$
* Taking the inverse hyperbolic cosine ($\cosh^{-1}$) on both sides:
  $$n \cosh^{-1}\left(\frac{\omega_s}{\omega_p}\right) = \cosh^{-1}\left(\sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}\right)$$
* Solving for $n$:
  $$n = \frac{\cosh^{-1}\left(\sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}\right)}{\cosh^{-1}\left(\frac{\omega_s}{\omega_p}\right)} \quad \text{--- (Proved)}$$
### 5. Page 13, Q.8(b): A low-pass filter is to be designed according to the following specifications.
**(i) $R_L = 600\text{ ohms}$, (ii) $f_c = 1400\text{ cps}$ ($\omega_c = 8800\text{ rps}$), (iii) ripple specification is that $20 \log_{10} \frac{\text{peak magnitude}}{\text{valley magnitude}} = 1\text{ dB}$, (iv) slope of the decibel gain curve is to be -40 dB/decade, (v) $|G(j0)|$ must be unity.**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.10-5 (*Specifications*), Section 4.12-4 (*Chebyshev Filters*), pp. 439–445, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.1 (*Lowpass Filter*), Section 14.8.1 (*First-Order Lowpass Filter*), pp. 638–639, 643

---

#### **1. Identify Filter Type and Order ($n$)**
* **Filter Type:** The presence of a passband ripple requirement ($1\text{ dB}$) indicates a **Chebyshev low-pass filter**.
* **Filter Order ($n$):** 
  Each pole in a low-pass filter contributes a roll-off slope of $-20\text{ dB/decade}$ in the stopband:
  $$n = \frac{\text{Specified Slope}}{-20\text{ dB/decade}} = \frac{-40\text{ dB/decade}}{-20\text{ dB/decade}} = 2$$
  Thus, the filter is a **2nd-order Chebyshev low-pass filter**.

---

#### **2. Calculate the Ripple Factor ($\epsilon$)**
The passband ripple is $A_{\max} = 1\text{ dB}$:
$$\epsilon = \sqrt{10^{0.1 A_{\max}} - 1} = \sqrt{10^{0.1(1)} - 1} = \sqrt{1.2589 - 1} = \sqrt{0.2589} \approx 0.5088$$

---

#### **3. Normalized Pole Locations**
The poles of a Chebyshev filter lie on an ellipse and are given by:
$$s_k = -\sigma_k \pm j\omega_k, \quad k = 1, 2$$
where:
$$a = \frac{1}{n}\sinh^{-1}\left(\frac{1}{\epsilon}\right) = \frac{1}{2}\sinh^{-1}\left(\frac{1}{0.5088}\right) = \frac{1}{2}\sinh^{-1}(1.9654)$$
Using $\sinh^{-1}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$:
$$a = \frac{1}{2}\ln\left(1.9654 + \sqrt{1.9654^2 + 1}\right) = \frac{1}{2}\ln(4.1706) = 0.7141$$
Now evaluate the hyperbolic functions:
$$\sinh(a) = \sinh(0.7141) = 0.7766$$
$$\cosh(a) = \cosh(0.7141) = 1.2673$$

For $n = 2$, the angles are $\phi_k = \frac{2k-1}{2n}\pi = \frac{2k-1}{4}\pi$:
* For $k = 1$: $\phi_1 = \frac{\pi}{4} = 45^\circ$
  $$\sigma_1 = \sinh(a)\sin(45^\circ) = (0.7766)(0.7071) = 0.5491$$
  $$\omega_1 = \cosh(a)\cos(45^\circ) = (1.2673)(0.7071) = 0.8961$$

The complex conjugate poles are:
$$s_{1,2} = -0.5491 \pm j0.8961$$

---

#### **4. Normalized Transfer Function ($G_n(s)$)**
The normalized denominator polynomial is:
$$D_n(s) = (s + 0.5491 - j0.8961)(s + 0.5491 + j0.8961) = (s + 0.5491)^2 + (0.8961)^2 = s^2 + 1.0982s + 1.1045$$

According to specification (v), $|G(j0)|$ must be unity ($1.0$):
$$G_n(s) = \frac{1.1045}{s^2 + 1.0982s + 1.1045}$$

---

#### **5. Frequency-Scaled Transfer Function ($G(s)$)**
Scale the normalized transfer function by the cutoff frequency $\omega_c = 8800\text{ rad/s}$ by replacing $s$ with $\frac{s}{\omega_c}$:
$$G(s) = \frac{1.1045}{\left(\frac{s}{8800}\right)^2 + 1.0982\left(\frac{s}{8800}\right) + 1.1045} = \frac{1.1045 \times (8800)^2}{s^2 + 1.0982(8800)s + 1.1045 \times (8800)^2}$$
$$G(s) = \frac{8.553 \times 10^7}{s^2 + 9664.2s + 8.553 \times 10^7}$$

---

#### **6. Circuit Realization (LC Ladder Network)**
From standard normalized Chebyshev filter tables for $n = 2$, $1\text{ dB}$ ripple, terminated in $1\,\Omega$:
$$g_1 = C_1' = 1.8219\text{ F}, \quad g_2 = L_2' = 0.6850\text{ H}$$

Applying **magnitude scaling** ($K_m = R_L = 600\,\Omega$) and **frequency scaling** ($K_f = \omega_c = 8800\text{ rad/s}$):
$$C_1 = \frac{C_1'}{K_m K_f} = \frac{1.8219}{600 \times 8800} = 0.345\text{ }\mu\text{F}$$
$$L_2 = \frac{K_m}{K_f} L_2' = \frac{600}{8800} \times 0.6850 = 46.7\text{ mH}$$

```
                 L2 = 46.7 mH
        o-------UUUUUUUU--------+-------o (+)
                                |
             +                  |
    Vi(t)   --- C1 = 0.345 µF  [ ] RL = 600 Ω   Vo(t)
            ---                [ ]
             |                  |
        o----+------------------+-------o (-)
```

---

### 6. Page 16, Q.8(b): Design a low-pass Butterworth filter having a slope of -80 dB/decade outside the pass band.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-2 (*Butterworth Filters*), pp. 439–441, 458–460
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.4 (*Bode Plots*), Section 14.8.1 (*Active Lowpass Filters*), Section 14.9 (*Scaling*), pp. 619–628, 643, 648–651

---

#### **1. Determine the Order of the Filter ($n$)**
* A Butterworth filter has an asymptotic roll-off rate of $-20n\text{ dB/decade}$ in the stopband (outside the passband).
* Given that the slope is $-80\text{ dB/decade}$:
  $$-20n = -80 \implies n = \frac{-80}{-20} = 4$$
Thus, a **4th-order** Butterworth filter is required.

---

#### **2. Normalized Transfer Function ($H_n(s)$)**
The normalized 4th-order Butterworth polynomial is given by:
$$B_4(s) = (s^2 + 0.7654s + 1)(s^2 + 1.8478s + 1)$$
The normalized transfer function with unity DC gain is:
$$H_n(s) = \frac{1}{B_4(s)} = \frac{1}{(s^2 + 0.7654s + 1)(s^2 + 1.8478s + 1)}$$

---

#### **3. Circuit Realization Using Sallen-Key Topology**
We cascade two second-order Sallen-Key low-pass filter stages:
$$H_n(s) = H_1(s) \cdot H_2(s)$$
where:
$$H_1(s) = \frac{1}{s^2 + 0.7654s + 1}, \quad H_2(s) = \frac{1}{s^2 + 1.8478s + 1}$$

```
                STAGE 1                                STAGE 2
         R1        R2                           R3        R4
   o---/\/\/--+--/\/\/--+--(+)            +---/\/\/--+--/\/\/--+--(+)
              |         |   |\            |          |         |   |\
             --- C1     |   | \           |         --- C3     |   | \
             ---       ---  |  \--+--o----+         ---       ---  |  \--+--o Vo
              |        ---  |  /  |                  |        ---  |  /  |
              |     C2  |   | /   |                  |     C4  |   | /   |
              |         +--(-)    |                  |         +--(-)    |
              |             |     |                  |             |     |
              +-------------+-----+                  +-------------+-----+
```

* **Standard Sallen-Key Low-Pass Section (Unity Gain):**
  $$H(s) = \frac{1}{s^2 C_1 C_2 R_1 R_2 + s C_2 (R_1 + R_2) + 1}$$
  Setting $R_1 = R_2 = 1\,\Omega$:
  $$H(s) = \frac{1}{s^2 C_1 C_2 + 2C_2 s + 1}$$

* **Design for Stage 1 ($s^2 + 0.7654s + 1$):**
  $$C_1 C_2 = 1 \implies C_1 = \frac{1}{C_2}$$
  $$2C_2 = 0.7654 \implies C_2 = 0.3827\text{ F}$$
  $$C_1 = \frac{1}{0.3827} = 2.613\text{ F}$$
  Choose: $R_1 = R_2 = 1\,\Omega$, $C_1 = 2.613\text{ F}$, $C_2 = 0.3827\text{ F}$.

* **Design for Stage 2 ($s^2 + 1.8478s + 1$):**
  $$C_3 C_4 = 1 \implies C_3 = \frac{1}{C_4}$$
  $$2C_4 = 1.8478 \implies C_4 = 0.9239\text{ F}$$
  $$C_3 = \frac{1}{0.9239} = 1.0824\text{ F}$$
  Choose: $R_3 = R_4 = 1\,\Omega$, $C_3 = 1.0824\text{ F}$, $C_4 = 0.9239\text{ F}$.

*(Note: For any specified cutoff frequency $\omega_c$ and practical resistor level $R_0$, frequency and impedance scaling can be applied using $R' = K_m R$ and $C' = \frac{C}{K_m K_f}$.)*

---

### 7. Page 71, Q.8(a) (Top): In context of filter performance characteristics, discuss Butterworth, Chebyshev and Elliptic filter approximations.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.10-5 (*Specifications*), Section 4.12-2 & 4.12-4 (*Butterworth & Chebyshev Filters*), pp. 439–445, 458–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

Filter approximations are mathematical functions used to approximate the ideal "brick-wall" low-pass filter response. The three most fundamental approximations are:

```
        Magnitude |H(jω)|
            1.0 |-\               --- Ideal
                |  \
  Butterworth   |   \             (Monotonic in both passband & stopband)
                |----\-\
    Chebyshev   | \/  \ \         (Equiripple in passband, monotonic in stopband)
                |------\--\-\
     Elliptic   | \/ \/ \  \ \    (Equiripple in both passband & stopband)
                +--------\--\-+---> ω
                        ωp  ωs
```

#### **1. Butterworth Filter Approximation**
* **Magnitude Response:** 
  $$|H(j\omega)| = \frac{1}{\sqrt{1 + \left(\frac{\omega}{\omega_c}\right)^{2n}}}$$
* **Passband & Stopband Behavior:** Completely **monotonic** (smooth) throughout both the passband and stopband; has no ripples.
* **Key Characteristic:** Known as **maximally flat** at $\omega = 0$ because its first $(2n - 1)$ derivatives are zero at DC.
* **Transition Band:** Widest transition band (slowest roll-off rate) among the three for a given order $n$.
* **Phase & Delay:** Best phase linearity and group delay performance among the three.

---

#### **2. Chebyshev Filter Approximation (Type I)**
* **Magnitude Response:** 
  $$|H(j\omega)| = \frac{1}{\sqrt{1 + \epsilon^2 C_n^2\left(\frac{\omega}{\omega_p}\right)}}$$
* **Passband & Stopband Behavior:** Exhibits **equiripple in the passband** and is **monotonic in the stopband**.
* **Key Characteristic:** By allowing controlled ripple in the passband, it achieves a much sharper transition (steeper roll-off) than the Butterworth filter for the same filter order.
* **Phase & Delay:** More nonlinear phase response and higher group delay variation near the cutoff frequency.

---

#### **3. Elliptic (Cauer) Filter Approximation**
* **Magnitude Response:** 
  $$|H(j\omega)| = \frac{1}{\sqrt{1 + \epsilon^2 R_n^2\left(\frac{\omega}{\omega_p}\right)}}$$
  where $R_n$ is a Jacobian elliptic rational function.
* **Passband & Stopband Behavior:** Exhibits **equiripple in both the passband and the stopband**.
* **Key Characteristic:** Provides the **sharpest transition band** (steepest roll-off) of any filter approximation for a given order $n$.
* **Poles and Zeros:** Contains both finite transmission zeros and complex conjugate poles.
* **Phase & Delay:** Possesses the poorest phase linearity and highest ringing in transient response.

---

#### **Summary Comparison Table**

| Performance Feature | Butterworth | Chebyshev (Type I) | Elliptic (Cauer) |
| :--- | :--- | :--- | :--- |
| **Passband Ripple** | None (Maximally Flat) | Equiripple | Equiripple |
| **Stopband Ripple** | None (Monotonic) | None (Monotonic) | Equiripple |
| **Transition Width** | Widest (Slowest) | Moderate | Narrowest (Sharpest) |
| **Order $n$ for Same Specs** | Highest | Moderate | Lowest |
| **Phase Linearity** | Excellent | Fair | Poor |
| **Circuit Complexity** | Simple | Moderate | Higher (requires zeros) |

---

### 8. Page 71, Q.8(a) (Middle): Show that the slope in the stop-band region for Chebyshev design is greater than Butterworth.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-4 (*Chebyshev Filters*), pp. 440–441, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

To compare the rate of attenuation (slope) in the stopband region, we examine the derivative of the attenuation/gain with respect to frequency for both filter types.

---

#### **1. Analysis at the Passband Edge ($\omega \to \omega_p = 1$)**
Let both filters be normalized such that the cutoff frequency is $\omega_p = 1$.

* **For the Butterworth Filter:**
  The squared magnitude response is:
  $$|H_B(j\omega)|^2 = \frac{1}{1 + \omega^{2n}} = \left(1 + \omega^{2n}\right)^{-1}$$
  Differentiating with respect to $\omega$:
  $$\frac{d}{d\omega} |H_B(j\omega)|^2 = -\left(1 + \omega^{2n}\right)^{-2} \cdot 2n\omega^{2n-1} = \frac{-2n\omega^{2n-1}}{\left(1 + \omega^{2n}\right)^2}$$
  At the band edge $\omega = 1$:
  $$\left.\frac{d|H_B(j\omega)|^2}{d\omega}\right|_{\omega=1} = \frac{-2n(1)}{(1 + 1)^2} = -\frac{n}{2}$$

* **For the Chebyshev Filter:**
  The squared magnitude response is:
  $$|H_C(j\omega)|^2 = \frac{1}{1 + \epsilon^2 C_n^2(\omega)} = \left[1 + \epsilon^2 C_n^2(\omega)\right]^{-1}$$
  Differentiating with respect to $\omega$:
  $$\frac{d}{d\omega} |H_C(j\omega)|^2 = -\left[1 + \epsilon^2 C_n^2(\omega)\right]^{-2} \cdot \left[2\epsilon^2 C_n(\omega) \frac{dC_n(\omega)}{d\omega}\right]$$
  At $\omega = 1$, by properties of Chebyshev polynomials:
  $$C_n(1) = 1 \quad \text{and} \quad \left.\frac{dC_n(\omega)}{d\omega}\right|_{\omega=1} = n^2$$
  Substituting these values at $\omega = 1$:
  $$\left.\frac{d|H_C(j\omega)|^2}{d\omega}\right|_{\omega=1} = -\frac{2\epsilon^2(1)(n^2)}{(1 + \epsilon^2)^2} = -\frac{2\epsilon^2}{1 + \epsilon^2} \cdot \frac{n^2}{1 + \epsilon^2}$$

* **Comparison of Slopes at the Band Edge:**
  * For Butterworth, the slope increases **linearly** with order: $\propto n$.
  * For Chebyshev, the slope increases **quadratically** with order: $\propto n^2$.
  For any order $n \ge 2$, the factor $n^2 \gg n$, which makes the negative slope of the Chebyshev filter significantly steeper at the edge of the stopband.

---

#### **2. Analysis in the Deep Stopband ($\omega \gg 1$)**
* **Butterworth Attenuation (in dB):**
  $$A_B(\omega) \approx 20 \log_{10}\left(\omega^n\right) = 20n \log_{10}(\omega)$$
* **Chebyshev Attenuation (in dB):**
  Since $C_n(\omega) \approx 2^{n-1}\omega^n$ for $\omega \gg 1$:
  $$A_C(\omega) \approx 20 \log_{10}\left(\epsilon 2^{n-1} \omega^n\right) = 20n \log_{10}(\omega) + 20(n-1)\log_{10}(2) + 20\log_{10}(\epsilon)$$

* **Rate of Change (Slope with respect to decades of frequency):**
  While both approaches asymptotically reach a slope of $20n\text{ dB/decade}$ at infinitely high frequencies, the Chebyshev filter enters the stopband with an immediate **excess attenuation** of:
  $$\Delta A = 20(n - 1)\log_{10}(2) \approx 6(n - 1)\text{ dB}$$
  Because the Chebyshev filter achieves this additional attenuation over a very narrow transition interval immediately following $\omega = 1$, its **effective slope in the transition and early stopband region is substantially higher** than that of the Butterworth filter:
  $$\left|\frac{dA_C}{d\omega}\right| > \left|\frac{dA_B}{d\omega}\right|$$

**Conclusion:** The Chebyshev filter provides a much steeper slope into the stopband than the Butterworth filter of identical order.

### 9. Page 71, Q.8(b) (Middle): For the Butterworth low pass filter, find and sketch the poles on the complex S-plane when the slope of the decibel gain curve is -80 dB/decade.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Butterworth Semicircular Pole Wall*), Section 4.12-2 (*Butterworth Filters*), pp. 439–440, 458–460
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2 (*Transfer Functions*), Section 14.9 (*Scaling & Filter Poles*), pp. 614–617, 648–651

---

#### **1. Determine the Filter Order ($n$)**
* For a Butterworth low-pass filter, each pole in the transfer function provides an asymptotic roll-off rate of $-20\text{ dB/decade}$ in the stopband.
* Given that the slope of the decibel gain curve is $-80\text{ dB/decade}$:
  $$n = \frac{-80\text{ dB/decade}}{-20\text{ dB/decade/pole}} = 4$$
Thus, the filter is a **4th-order Butterworth filter** ($n = 4$).

---

#### **2. Formula for Butterworth Poles**
The poles of a normalized Butterworth filter lie on the unit circle in the left half of the complex $s$-plane ($\text{Re}(s) < 0$). They are given by:
$$s_k = e^{j\theta_k} = \cos(\theta_k) + j\sin(\theta_k), \quad k = 1, 2, 3, 4$$
where the angles $\theta_k$ are spaced symmetrically:
$$\theta_k = \frac{2k + n - 1}{2n}\pi = \frac{2k + 3}{8}\pi = \frac{\pi}{2} + \frac{2k - 1}{8}\pi$$

Calculating the angles for $k = 1, 2, 3, 4$:
* **For $k = 1$:**
  $$\theta_1 = \frac{5\pi}{8} = 112.5^\circ$$
  $$s_1 = \cos(112.5^\circ) + j\sin(112.5^\circ) = -0.3827 + j0.9239$$

* **For $k = 2$:**
  $$\theta_2 = \frac{7\pi}{8} = 157.5^\circ$$
  $$s_2 = \cos(157.5^\circ) + j\sin(157.5^\circ) = -0.9239 + j0.3827$$

* **For $k = 3$:**
  $$\theta_3 = \frac{9\pi}{8} = 202.5^\circ = -157.5^\circ$$
  $$s_3 = \cos(202.5^\circ) + j\sin(202.5^\circ) = -0.9239 - j0.3827$$

* **For $k = 4$:**
  $$\theta_4 = \frac{11\pi}{8} = 247.5^\circ = -112.5^\circ$$
  $$s_4 = \cos(247.5^\circ) + j\sin(247.5^\circ) = -0.3827 - j0.9239$$

The two complex conjugate pairs are:
$$s_{1,4} = -0.3827 \pm j0.9239$$
$$s_{2,3} = -0.9239 \pm j0.3827$$

---

#### **3. Sketch of Poles on the Complex $s$-Plane**
All 4 poles lie on a circle of radius $\omega_0 = 1$ in the left half of the $s$-plane, with an equal angular separation of $\Delta\theta = \frac{\pi}{4} = 45^\circ$:

```
                            jω (Imaginary axis)
                                   ^
                                   |
                         s1        |
                           X       |  
                            \ 112.5°
                             \     |  
                    s2        \    |  
                      X--------\---+-----------------> σ (Real axis)
                       \ 157.5° \  | 0
                        \        \ |
                         \        \|
                          \        |
                           X       |  
                         s3 \      |  
                             \     |  
                              X    |
                            s4     |
                                   |
               (All poles lie on the unit circle, |s| = 1)
```

---

### 10. Page 71, Q.8(a) (Bottom): What is modern filter? What are the differences between Butterworth and Chebyshev design?

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.10-5 (*Practical Filters*), pp. 439–445
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

---

#### **1. What is a Modern Filter?**
* **Classical Filters** (Image Parameter Method): Early filter designs used cascaded sections whose design was based on matching image impedances. They suffered from poor predictability of the overall attenuation curve and severe termination sensitivity.
* **Modern Filters** (Network Synthesis Method): A modern filter is designed using **network synthesis techniques** based on rigorous mathematical approximation theory.
  * The designer starts with explicit tolerance requirements (passband ripple, stopband attenuation, and cutoff frequencies).
  * A mathematical rational transfer function $H(s) = \frac{N(s)}{D(s)}$ is derived (e.g., Butterworth, Chebyshev, Elliptic, Bessel) that satisfies these frequency-domain criteria.
  * The resulting transfer function is then synthesized exactly into practical passive LC ladder networks or active-RC circuits (such as Sallen-Key or state-variable biquads).

---

#### **2. Differences Between Butterworth and Chebyshev Design**

| Feature | Butterworth Filter Design | Chebyshev Filter Design (Type I) |
| :--- | :--- | :--- |
| **Passband Characteristic** | **Maximally Flat**: Completely smooth and monotonic with no ripple. | **Equiripple**: Displays equal-amplitude ripples within the passband. |
| **Stopband Characteristic** | Monotonic roll-off. | Monotonic roll-off. |
| **Pole Locations** | Poles lie uniformly on a **circle** in the left half of the $s$-plane. | Poles lie on an **ellipse** in the left half of the $s$-plane. |
| **Sharpness of Roll-off** | Slower, broader transition band between passband and stopband. | Much sharper, steeper transition band for the same order $n$. |
| **Required Order ($n$)** | Requires a **higher order** $n$ to meet the same stopband attenuation specs. | Requires a **lower order** $n$ to meet the same stopband specs. |
| **Phase Response & Delay** | More linear phase response; more uniform group delay. | Highly non-linear phase response; substantial group delay distortion near cutoff. |
| **Transient Response** | Clean transient response with minimal ringing or overshoot. | Significant overshoot and ringing due to high-$Q$ poles near the cutoff edge. |
| **Design Parameters** | Specified solely by order $n$ and $-3\text{ dB}$ cutoff frequency $\omega_0$. | Requires order $n$, passband edge $\omega_p$, and ripple factor $\epsilon$ (or $A_{\max}$). |

---

### 11. Page 71, Q.8(b) (Bottom): Write down the algorithm for Butterworth filter design.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2 (*Lowpass Filters*), Section 4.12-2 (*Butterworth Filters*), pp. 439–440, 458–460
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.8 (*Active Filters*), Section 14.9 (*Scaling*), pp. 642–651

The step-by-step algorithm to design an analog low-pass Butterworth filter is as follows:

```
[ Step 1: Define Specs ] ---> [ Step 2: Calculate Order n ] ---> [ Step 3: Find Cutoff Frequency ω0 ]
                                                                                |
[ Step 6: Scaling & Circuit ] <-- [ Step 5: Transfer Function H(s) ] <-- [ Step 4: Locate LHP Poles ]
```

#### **Step 1: Define the Filter Specifications**
* Passband edge frequency: $\omega_p$ (or $f_p$).
* Maximum passband attenuation (ripple): $A_{\max}$ in dB (often $3\text{ dB}$).
* Stopband edge frequency: $\omega_s$ (or $f_s$).
* Minimum stopband attenuation: $A_{\min}$ in dB.

#### **Step 2: Calculate the Required Filter Order ($n$)**
The order $n$ is calculated using the formula:
$$n \ge \frac{\log_{10}\left(\frac{10^{0.1 A_{\min}} - 1}{10^{0.1 A_{\max}} - 1}\right)}{2\log_{10}\left(\frac{\omega_s}{\omega_p}\right)}$$
* Round $n$ up to the nearest integer.

#### **Step 3: Determine the 3-dB Cutoff Frequency ($\omega_0$ or $\omega_c$)**
Calculate $\omega_0$ to ensure the specification is met at both edges:
$$\omega_0 = \frac{\omega_p}{\left(10^{0.1 A_{\max}} - 1\right)^{\frac{1}{2n}}}$$

#### **Step 4: Find the Poles of the Normalized Filter**
Determine the $n$ poles lying on the unit circle in the left half of the $s$-plane:
$$s_k = -\sin\left(\frac{2k - 1}{2n}\pi\right) + j\cos\left(\frac{2k - 1}{2n}\pi\right), \quad k = 1, 2, \dots, n$$

#### **Step 5: Formulate the Transfer Function**
* **Normalized Transfer Function:** Combine conjugate pole pairs into second-order quadratic factors (and a first-order factor if $n$ is odd):
  $$H_n(s) = \frac{1}{B_n(s)}$$
  *(Values of $B_n(s)$ are obtained from standard Butterworth polynomial tables).*
* **Frequency Scaling:** Replace $s$ by $\frac{s}{\omega_0}$ to get the unnormalized transfer function:
  $$H(s) = H_n\left(\frac{s}{\omega_0}\right)$$

#### **Step 6: Circuit Synthesis and Scaling**
* **Active Realization:** Decompose $H(s)$ into first- and second-order sections and implement each section using **Sallen-Key** op-amp circuits.
* **Passive Realization:** Look up the normalized ladder prototype element values ($g_1, g_2, \dots, g_n$) and apply magnitude scaling ($K_m = R_L$) and frequency scaling ($K_f = \omega_0$):
  $$R' = K_m R, \quad L' = \frac{K_m}{K_f} L, \quad C' = \frac{C}{K_m K_f}$$

---

### 12. Page 72, Q.8(b): Draw the ideal and practical frequency responses of different types of filter and also distinguish between active and passive filter.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-5 (*Practical Filters*), Chapter 7, Section 7.5 (*Ideal and Practical Filters*), pp. 444–445, 730–732
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7 (*Passive Filters*), Section 14.8 (*Active Filters*), pp. 637–648

---

#### **1. Ideal and Practical Frequency Responses**

##### **(a) Lowpass Filter (LPF)**
Passes frequencies from DC up to cutoff frequency $\omega_c$, and attenuates higher frequencies.
```
         |H(jω)|
         1.0 +-------+                 --- Ideal
             |       | \
       0.707 |.......|..\              --- Practical
             |       |   \
             +-------+----+--------> ω
             0       ωc
```

##### **(b) Highpass Filter (HPF)**
Attenuates frequencies below cutoff $\omega_c$, and passes frequencies above $\omega_c$.
```
         |H(jω)|
         1.0 +           +---------+   --- Ideal
             |          /|
       0.707 |........./.|             --- Practical
             |       /   |
             +------+----+---------+-> ω
             0      ωc
```

##### **(c) Bandpass Filter (BPF)**
Passes frequencies within a band ($\omega_1$ to $\omega_2$), centered at $\omega_0$.
```
         |H(jω)|
         1.0 +       +-----+           --- Ideal
             |      /|     |\
       0.707 |...../.|.....|.\         --- Practical
             |    /  |     |  \
             +---+---+-----+---+---> ω
             0   ω1  ω0    ω2
```

##### **(d) Bandstop (Notch) Filter (BSF)**
Rejects frequencies within a specific band ($\omega_1$ to $\omega_2$), while passing all others.
```
         |H(jω)|
         1.0 +-----+       +-------+   --- Ideal
             |\    |       |    /
       0.707 |.\...|.......|.../.      --- Practical
             |  \  |       |  /
             +---+---+-----+---+---> ω
             0   ω1  ω0    ω2
```

---

#### **2. Distinguish Between Active and Passive Filters**

| Parameter / Feature | Passive Filter | Active Filter |
| :--- | :--- | :--- |
| **Components Used** | Consists only of **passive components**: Resistors ($R$), Inductors ($L$), and Capacitors ($C$). | Consists of **active devices** (Op-Amps, Transistors) along with Resistors ($R$) and Capacitors ($C$). |
| **Use of Inductors** | Requires inductors, which are heavy, bulky, and lossy at low/audio frequencies. | **Eliminates inductors** entirely, reducing size, weight, and cost. |
| **Voltage Gain** | Cannot provide power or voltage gain; maximum gain is **unity or less** ($|H| \le 1$). | Can provide **amplification** (gain $> 1$) integrated into the filter. |
| **Loading Effect** | Prone to loading; connecting a load or cascading stages changes the filter characteristics. | Op-amp buffers provide **high input impedance and low output impedance**, preventing loading when cascaded. |
| **Frequency Range** | Operates effectively from low frequencies up to **high RF, UHF, and microwave frequencies**. | Limited to lower frequencies (typically **$\le 100\text{ kHz}$ to a few MHz**) due to op-amp bandwidth limits. |
| **Power Supply** | Requires **no external DC power supply**. | Requires an **external DC power supply** to bias the active components. |
| **Tuning & Flexibility** | Difficult to tune; changing component values often requires replacing physical inductors. | Highly versatile and easy to tune using potentiometers or adjustable resistors. |

---

### **Low pass prototypes of modern filters**

### 13. Page 16, Q.8(c): Develop a normalized low-pass Chebyshev model with n=2, ϵ = 0.663, ωc = 1 rps and RL = 1Ω. The magnitude of gain must be unity at ω = 0. Sketch the approximate shape of the decibel gain curve.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-4 (*Chebyshev Filters*), pp. 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.9 (*Magnitude & Frequency Scaling*), pp. 648–651

---

#### **1. Calculate Pole Locations**
For a 2nd-order Chebyshev filter, the parameter $a$ is:
$$a = \frac{1}{n}\sinh^{-1}\left(\frac{1}{\epsilon}\right) = \frac{1}{2}\sinh^{-1}\left(\frac{1}{0.663}\right) = \frac{1}{2}\sinh^{-1}(1.5083)$$
Using $\sinh^{-1}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$:
$$a = \frac{1}{2}\ln\left(1.5083 + \sqrt{1.5083^2 + 1}\right) = \frac{1}{2}\ln(3.3175) \approx 0.5996$$
Evaluating the hyperbolic functions:
$$\sinh(a) = \sinh(0.5996) \approx 0.6362$$
$$\cosh(a) = \cosh(0.5996) \approx 1.1852$$

For $n = 2$, the angles are $\phi_k = \frac{2k-1}{4}\pi$ for $k = 1, 2$:
* $\phi_1 = \frac{\pi}{4} = 45^\circ$, $\phi_2 = \frac{3\pi}{4} = 135^\circ$
$$\sigma_1 = \sinh(a)\sin(45^\circ) = (0.6362)(0.7071) = 0.4499 \approx 0.45$$
$$\omega_1 = \cosh(a)\cos(45^\circ) = (1.1852)(0.7071) = 0.8381 \approx 0.838$$

The poles in the left-half $s$-plane are:
$$s_{1,2} = -0.45 \pm j0.838$$

---

#### **2. Normalized Transfer Function ($G(s)$)**
The denominator polynomial is:
$$D(s) = (s + 0.45)^2 + (0.838)^2 = s^2 + 0.90s + 0.9048$$
Given that $|G(j0)| = 1$ (unity DC gain):
$$G(s) = \frac{0.9048}{s^2 + 0.90s + 0.9048}$$

---

#### **3. Circuit Model Realization**
For a normalized low-pass ladder network with load $R_L = 1\,\Omega$ and $\omega_c = 1\text{ rad/s}$:
* The element values of the low-pass prototype are:
  $$C_1 = 1.438\text{ F}, \quad L_2 = 1.593\text{ H}$$

```
                L2 = 1.593 H
      o-----------UUUUUUUU----------+--------o (+)
                                    |
                 +                  |
      Vi(s)     --- C1 = 1.438 F   [ ] RL = 1 Ω   Vo(s)
                ---                [ ]
                 |                  |
      o----------+------------------+--------o (-)
```

---

#### **4. Decibel Gain Curve Sketch**
* **Passband Ripple:** 
  $$A_{\max} = 10\log_{10}(1 + \epsilon^2) = 10\log_{10}(1 + 0.663^2) \approx 1.58\text{ dB}$$
* **Roll-off Slope:** $-20n = -40\text{ dB/decade}$.

```
      Gain (dB)
          0 dB +---\        /---\ 
               |    \      /     \
    -1.58 dB --+.....\..../.......\................
               |      \  /         \
               |       \/           \
               |                     \  -40 dB/decade
               +----------------------\---------> ω (log scale)
               0                     ωc = 1
```

---

### 14. Page 19, Q.8(b): Design a normalized low pass Chebyshev model to meet the following specifications:
**(i) $R_L = 1\text{k}\Omega$ (ii) $\omega_c = 1\text{ rps}$ (iii) The ripple specification is: $20 \log_{10} \frac{\text{peak magnitude}}{\text{valley magnitude}} = 1.5\text{ dB}$ (iv) Slop of the dB gain curve is to be -60 dB/decade at frequency much higher than cutoff. (v) $G(j0)$ must be unity.**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-4 (*Chebyshev Filters*), pp. 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.9 (*Magnitude & Frequency Scaling*), pp. 648–651

---

#### **1. Determine Filter Order ($n$) and Ripple Factor ($\epsilon$)**
* **Order ($n$):** 
  $$n = \frac{\text{Slope}}{-20\text{ dB/decade}} = \frac{-60\text{ dB/decade}}{-20\text{ dB/decade}} = 3$$
* **Ripple Factor ($\epsilon$):**
  $$A_{\max} = 1.5\text{ dB}$$
  $$\epsilon = \sqrt{10^{0.1(1.5)} - 1} = \sqrt{1.4125 - 1} = \sqrt{0.4125} \approx 0.6423$$

---

#### **2. Pole Locations**
$$a = \frac{1}{3}\sinh^{-1}\left(\frac{1}{0.6423}\right) = \frac{1}{3}\sinh^{-1}(1.5569) = \frac{1}{3}\ln\left(1.5569 + \sqrt{1.5569^2 + 1}\right) = \frac{1}{3}\ln(3.4074) \approx 0.4087$$
$$\sinh(a) = \sinh(0.4087) = 0.4202$$
$$\cosh(a) = \cosh(0.4087) = 1.0847$$

For $n = 3$, the angles are $\phi_k = \frac{2k-1}{6}\pi$ ($30^\circ, 90^\circ, 150^\circ$):
* **Real Pole ($k = 2$, $\phi_2 = 90^\circ$):**
  $$s_2 = -\sinh(a)\sin(90^\circ) = -0.4202$$
* **Complex Conjugate Poles ($k = 1, 3$, $\phi = 30^\circ, 150^\circ$):**
  $$\sigma = \sinh(a)\sin(30^\circ) = (0.4202)(0.5) = 0.2101$$
  $$\omega = \cosh(a)\cos(30^\circ) = (1.0847)(0.8660) = 0.9394$$
  $$s_{1,3} = -0.2101 \pm j0.9394$$

---

#### **3. Normalized Transfer Function ($G(s)$)**
$$D(s) = (s + 0.4202)\left[(s + 0.2101)^2 + (0.9394)^2\right] = (s + 0.4202)(s^2 + 0.4202s + 0.9266)$$
$$D(s) = s^3 + 0.8404s^2 + 1.1032s + 0.3894$$

Since $n = 3$ is odd, $G(0) = 1$ is satisfied by setting the numerator equal to the constant term:
$$G(s) = \frac{0.3894}{s^3 + 0.8404s^2 + 1.1032s + 0.3894}$$

---

#### **4. Circuit Model ($R_L = 1\text{ k}\Omega$, $\omega_c = 1\text{ rad/s}$)**
* Prototype element values for $1.5\text{ dB}$ ripple, $n = 3$:
  $$g_1 = 1.4029, \quad g_2 = 0.7071, \quad g_3 = 1.4029$$
* Scaling by magnitude factor $K_m = R_L = 1000$ and $K_f = \omega_c = 1$:
  $$C_1 = \frac{g_1}{K_m K_f} = \frac{1.4029}{1000 \times 1} = 1.403\text{ mF}$$
  $$L_2 = \frac{K_m}{K_f}g_2 = \frac{1000}{1}(0.7071) = 707.1\text{ H}$$
  $$C_3 = \frac{g_3}{K_m K_f} = \frac{1.4029}{1000 \times 1} = 1.403\text{ mF}$$

```
                           L2 = 707.1 H
        o-------------+------UUUUUUUU------+------------o (+)
                      |                    |
                     ---                  ---
             C1 =   ---           C3 =   ---     RL =
           1.403 mF   |         1.403 mF   |    1000 Ω
                      |                    |
        o-------------+--------------------+------------o (-)
```

---

### 15. Page 71, Q(c) (Top): Find the transfer function of a Chebyshev lowpass filter to satisfy the following criteria.
**The ratio $r \le 2\text{ dB}$ over a passband $0 < \omega \le 10$, $\omega_p = 10\text{ rad/s}$**  
**The stop band gain $G_s \le -20\text{dB}$ for $\omega > 16.5$, $\omega_s = 16.5\text{ rad/s}$**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-4 (*Chebyshev Filters*), pp. 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2 & 14.8 (*Transfer Functions & Active Filters*), pp. 614–617, 642–648

---

#### **1. Calculate Filter Order ($n$)**
* Passband ripple: $A_{\max} = 2\text{ dB}$
  $$\epsilon = \sqrt{10^{0.1(2)} - 1} = \sqrt{10^{0.2} - 1} = \sqrt{1.5849 - 1} = \sqrt{0.5849} \approx 0.7648$$
* Stopband attenuation: $A_{\min} = 20\text{ dB}$
* Ratio of frequencies:
  $$\frac{\omega_s}{\omega_p} = \frac{16.5}{10} = 1.65$$

Using the order formula:
$$n \ge \frac{\cosh^{-1}\left(\sqrt{\frac{10^{0.1 A_{\min}} - 1}{\epsilon^2}}\right)}{\cosh^{-1}\left(\frac{\omega_s}{\omega_p}\right)} = \frac{\cosh^{-1}\left(\sqrt{\frac{10^2 - 1}{0.5849}}\right)}{\cosh^{-1}(1.65)} = \frac{\cosh^{-1}\left(\sqrt{\frac{99}{0.5849}}\right)}{\cosh^{-1}(1.65)}$$
$$\sqrt{\frac{99}{0.5849}} = \sqrt{169.26} \approx 13.01$$
$$\cosh^{-1}(13.01) = \ln\left(13.01 + \sqrt{13.01^2 - 1}\right) = \ln(25.98) \approx 3.257$$
$$\cosh^{-1}(1.65) = \ln\left(1.65 + \sqrt{1.65^2 - 1}\right) = \ln(2.962) \approx 1.086$$
$$n \ge \frac{3.257}{1.086} = 2.999 \implies \mathbf{n = 3}$$

---

#### **2. Normalized Poles ($n = 3, \epsilon = 0.7648$)**
$$a = \frac{1}{3}\sinh^{-1}\left(\frac{1}{0.7648}\right) = \frac{1}{3}\sinh^{-1}(1.3075) = \frac{1}{3}\ln\left(1.3075 + \sqrt{1.3075^2 + 1}\right) = \frac{1}{3}\ln(2.9535) \approx 0.3610$$
$$\sinh(a) = \sinh(0.3610) = 0.3689$$
$$\cosh(a) = \cosh(0.3610) = 1.0662$$

Poles:
* Real pole: $s_1 = -\sinh(a) = -0.3689$
* Complex conjugate poles:
  $$\sigma = \sinh(a)\sin(30^\circ) = (0.3689)(0.5) = 0.1845$$
  $$\omega = \cosh(a)\cos(30^\circ) = (1.0662)(0.8660) = 0.9233$$
  $$s_{2,3} = -0.1845 \pm j0.9233$$

Normalized denominator:
$$D_n(s) = (s + 0.3689)\left[(s + 0.1845)^2 + (0.9233)^2\right] = (s + 0.3689)(s^2 + 0.3690s + 0.8865)$$
$$D_n(s) = s^3 + 0.7379s^2 + 1.0226s + 0.3270$$

---

#### **3. Frequency Scaling to $\omega_p = 10\text{ rad/s}$**
Substitute $s \to \frac{s}{10}$:
$$D(s) = \left(\frac{s}{10}\right)^3 + 0.7379\left(\frac{s}{10}\right)^2 + 1.0226\left(\frac{s}{10}\right) + 0.3270$$
Multiplying by $10^3 = 1000$:
$$D(s) = s^3 + 7.379s^2 + 102.26s + 327.0$$
With unity DC gain:
$$H(s) = \frac{327.0}{s^3 + 7.379s^2 + 102.26s + 327.0}$$

---

### 16. Page 71, Q.8(c) (Middle): Construct the transfer function of the Chebyshev filter if $G(s)G(-s) = \frac{1}{1+0.5C_3^2(s/j)}$.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-4 (*Chebyshev Filters*), pp. 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2 & 14.8 (*Transfer Functions*), pp. 614–617, 642–648

---

#### **1. Identify Parameters**
Comparing $G(s)G(-s) = \frac{1}{1 + \epsilon^2 C_n^2(s/j)}$:
* Order: $n = 3$
* $\epsilon^2 = 0.5 \implies \epsilon = \frac{1}{\sqrt{2}} \approx 0.7071$

---

#### **2. Pole Locations**
The poles are the roots of $1 + 0.5 C_3^2\left(\frac{s}{j}\right) = 0$:
$$a = \frac{1}{3}\sinh^{-1}\left(\frac{1}{\epsilon}\right) = \frac{1}{3}\sinh^{-1}(\sqrt{2}) = \frac{1}{3}\sinh^{-1}(1.4142)$$
Using $\sinh^{-1}(x) = \ln\left(x + \sqrt{x^2 + 1}\right)$:
$$a = \frac{1}{3}\ln\left(1.4142 + \sqrt{2 + 1}\right) = \frac{1}{3}\ln(1.4142 + 1.7321) = \frac{1}{3}\ln(3.1463) = \frac{1.1462}{3} \approx 0.3821$$

Evaluating hyperbolic functions:
$$\sinh(a) = \sinh(0.3821) \approx 0.3914$$
$$\cosh(a) = \cosh(0.3821) \approx 1.0743$$

For $n = 3$, the pole angles are $\phi_k = \frac{2k-1}{6}\pi$ ($30^\circ, 90^\circ, 150^\circ$):
* **Real Pole ($k = 2$):**
  $$s_1 = -\sinh(a)\sin(90^\circ) = -0.3914$$
* **Complex Conjugate Poles ($k = 1, 3$):**
  $$\sigma = \sinh(a)\sin(30^\circ) = (0.3914)(0.5) = 0.1957$$
  $$\omega = \cosh(a)\cos(30^\circ) = (1.0743)(0.8660) = 0.9303$$
  $$s_{2,3} = -0.1957 \pm j0.9303$$

---

#### **3. Formulate Transfer Function $G(s)$**
To ensure stability, select the poles residing strictly in the left half of the $s$-plane:
$$D(s) = (s - s_1)(s - s_2)(s - s_3) = (s + 0.3914)\left[(s + 0.1957)^2 + (0.9303)^2\right]$$
$$D(s) = (s + 0.3914)(s^2 + 0.3914s + 0.9038) = s^3 + 0.7828s^2 + 1.057s + 0.3537$$

Since $n = 3$ is odd, $|G(j0)| = 1$:
$$G(s) = \frac{0.3537}{s^3 + 0.7828s^2 + 1.057s + 0.3537}$$

---

### **Filter design and transformations**

### 17. Page 10, Q.6(c): Develop a band reject Butterworth filter with n = 2, $\omega_h$ = 60000 rps, $\omega_l$ = 10000 rps and $R_L$ = 1000Ω. Sketch the approximate shape of the decibel gain characteristics.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-4 & 4.10-5 (*Notch Filters*), pp. 441–445
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.4 & 14.8.4 (*Bandstop Filters*), pp. 640–641, 645–646

---

#### **1. Filter Specifications & Frequency Parameters**
* **Type:** Butterworth Band-Reject (Band-Stop) Filter
* **Order:** $n = 2$
* **Upper cutoff frequency:** $\omega_h = 60{,}000\text{ rad/s}$
* **Lower cutoff frequency:** $\omega_l = 10{,}000\text{ rad/s}$
* **Load resistance:** $R_L = 1000\,\Omega$

From these frequencies, we find:
* **Bandwidth ($B$):**
  $$B = \omega_h - \omega_l = 60{,}000 - 10{,}000 = 50{,}000\text{ rad/s}$$
* **Center / Resonant frequency ($\omega_0$):**
  $$\omega_0 = \sqrt{\omega_h \omega_l} = \sqrt{60{,}000 \times 10{,}000} = \sqrt{6 \times 10^8} \approx 24{,}495\text{ rad/s}$$

---

#### **2. Low-Pass to Band-Reject Transformation**
The normalized 2nd-order Butterworth low-pass prototype polynomial is:
$$B_2(S) = S^2 + \sqrt{2}S + 1$$
The normalized low-pass transfer function is:
$$H_{\text{LP}}(S) = \frac{1}{S^2 + \sqrt{2}S + 1}$$

To transform from a normalized low-pass filter to a band-reject filter, we substitute:
$$S = \frac{B s}{s^2 + \omega_0^2} = \frac{50{,}000 s}{s^2 + 6 \times 10^8}$$

Substituting into $H_{\text{LP}}(S)$:
$$H(s) = \frac{1}{\left(\frac{B s}{s^2 + \omega_0^2}\right)^2 + \sqrt{2}\left(\frac{B s}{s^2 + \omega_0^2}\right) + 1} = \frac{(s^2 + \omega_0^2)^2}{(s^2 + \omega_0^2)^2 + \sqrt{2}Bs(s^2 + \omega_0^2) + B^2 s^2}$$
$$H(s) = \frac{(s^2 + 6 \times 10^8)^2}{s^4 + 70{,}710.7 s^3 + 3.7 \times 10^9 s^2 + 4.243 \times 10^{13} s + 3.6 \times 10^{16}}$$

---

#### **3. Circuit Realization (LC Ladder Network)**
The normalized 2nd-order Butterworth low-pass prototype ($R_L = 1\,\Omega$) has:
$$C_1' = \sqrt{2}\text{ F} \approx 1.414\text{ F}, \quad L_2' = \sqrt{2}\text{ H} \approx 1.414\text{ H}$$

Under the **low-pass to band-reject transformation**:
1. **Shunt Capacitor $C_1'$** transforms into a **parallel resonant tank** in the shunt branch:
   $$C_1 = \frac{C_1'}{R_L B} = \frac{\sqrt{2}}{1000 \times 50{,}000} = 2.828 \times 10^{-8}\text{ F} = \mathbf{28.28\text{ nF}}$$
   $$L_1 = \frac{R_L B}{\omega_0^2 C_1'} = \frac{1000 \times 50{,}000}{(6 \times 10^8)\sqrt{2}} = \mathbf{58.93\text{ mH}}$$

2. **Series Inductor $L_2'$** transforms into a **series resonant branch**:
   $$L_2 = \frac{R_L L_2'}{B} = \frac{1000 \times \sqrt{2}}{50{,}000} = \mathbf{28.28\text{ mH}}$$
   $$C_2 = \frac{B}{R_L \omega_0^2 L_2'} = \frac{50{,}000}{1000 \times (6 \times 10^8)\sqrt{2}} = \mathbf{58.93\text{ nF}}$$

```
                       L2 = 28.28 mH    C2 = 58.93 nF
            o-------------UUUUUUUU----------||------------+--------o (+)
                                                          |
                                           +             [ ]
                                  C1 =   ---             [ ] RL =
                                28.28 nF ---             [ ] 1000 Ω
                                           |      L1 =    |
                                           +----UUUUUU----+
                                           |    58.93 mH  |
            o------------------------------+--------------+--------o (-)
```

---

#### **4. Decibel Gain Characteristics Sketch**
* At $\omega = 0$ (DC) and $\omega \to \infty$: $\text{Gain} = 0\text{ dB}$.
* At $\omega_l = 10{,}000\text{ rad/s}$ and $\omega_h = 60{,}000\text{ rad/s}$: $\text{Gain} = -3\text{ dB}$.
* At $\omega_0 = 24{,}495\text{ rad/s}$: $\text{Gain} \to -\infty\text{ dB}$ (notch frequency).

```
         Gain (dB)
              0 dB +-------\                      /-------+
                   |        \                    /        |
             -3 dB +.........\................../.........+
                   |          \                /
                   |           \              /
                   |            \     /\     /
                   |             \   /  \   /
                   |              \_/    \_/
                   +---------------+------+---------------+--> ω (log scale)
                   0              ωl      ω0     ωh
                                (10k)  (24.5k)  (60k)
```

---

### 18. Page 13, Q.6(c): Develop a band-stop Butterworth filter with n = 2, $\omega_h$ = 60000 rps, $\omega_l$ = 10000 rps and $R_L$ = 10000Ω. Sketch the approximate shape of the decibel gain curve.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-4 (*Notch Filters*), pp. 441–443
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.4 & 14.8.4 (*Bandstop Filters*), pp. 640–641, 645–646

---

#### **1. Filter Parameters**
The specifications are identical to Question 17, with the only change being that the load resistance is now scaled by a factor of 10:
* $n = 2$
* $\omega_h = 60{,}000\text{ rad/s}, \quad \omega_l = 10{,}000\text{ rad/s}$
* $B = \omega_h - \omega_l = 50{,}000\text{ rad/s}$
* $\omega_0 = \sqrt{\omega_h \omega_l} = \sqrt{6 \times 10^8} \approx 24{,}495\text{ rad/s}$
* **Load resistance:** $R_L = 10{,}000\,\Omega = 10\text{ k}\Omega$

The transfer function $H(s)$ remains identical because the dimensionless gain response is invariant to magnitude scaling:
$$H(s) = \frac{(s^2 + 6 \times 10^8)^2}{s^4 + 70{,}710.7 s^3 + 3.7 \times 10^9 s^2 + 4.243 \times 10^{13} s + 3.6 \times 10^{16}}$$

---

#### **2. Component Calculation with $R_L = 10{,}000\,\Omega$**
Using magnitude scaling $K_m = 10{,}000$ and frequency scaling factor $K_f = 1$:

1. **Shunt Parallel Tank:**
   $$C_1 = \frac{C_1'}{R_L B} = \frac{\sqrt{2}}{10{,}000 \times 50{,}000} = \mathbf{2.828\text{ nF}}$$
   $$L_1 = \frac{R_L B}{\omega_0^2 C_1'} = \frac{10{,}000 \times 50{,}000}{(6 \times 10^8)\sqrt{2}} = \mathbf{589.3\text{ mH}} = 0.5893\text{ H}$$

2. **Series Resonant Branch:**
   $$L_2 = \frac{R_L L_2'}{B} = \frac{10{,}000 \times \sqrt{2}}{50{,}000} = \mathbf{282.8\text{ mH}} = 0.2828\text{ H}$$
   $$C_2 = \frac{B}{R_L \omega_0^2 L_2'} = \frac{50{,}000}{10{,}000 \times (6 \times 10^8)\sqrt{2}} = \mathbf{5.893\text{ nF}}$$

```
                       L2 = 282.8 mH    C2 = 5.893 nF
            o-------------UUUUUUUU----------||------------+--------o (+)
                                                          |
                                           +             [ ]
                                  C1 =   ---             [ ] RL =
                                2.828 nF ---             [ ] 10 kΩ
                                           |      L1 =    |
                                           +----UUUUUU----+
                                           |    589.3 mH  |
            o------------------------------+--------------+--------o (-)
```

---

#### **3. Decibel Gain Curve Sketch**
The frequency response curve is mathematically identical in shape to Question 17:
* **Passband Gain:** $0\text{ dB}$ at low frequencies ($\omega \ll \omega_l$) and high frequencies ($\omega \gg \omega_h$).
* **Half-Power Points ($-3\text{ dB}$):** Located at $\omega_l = 10{,}000\text{ rad/s}$ and $\omega_h = 60{,}000\text{ rad/s}$.
* **Notch / Rejection Peak:** Minimum transmission ($-\infty\text{ dB}$) at $\omega_0 \approx 24.5\text{ krad/s}$.

```
         Gain (dB)
              0 dB +-------\                      /-------+
                   |        \                    /        |
             -3 dB +.........\................../.........+
                   |          \                /
                   |           \              /
                   |            \     /\     /
                   |             \   /  \   /
                   |              \_/    \_/
                   +---------------+------+---------------+--> ω (log scale)
                   0              ωl      ω0     ωh
                                (10k)  (24.5k)  (60k)
```

---

### 19. Page 25, Q.1: An input $x(t) = \frac{3}{2} + \frac{3}{\pi} \sum_{n=1}^\infty \left[\frac{1}{n}\sin(2\pi nt)\right]$ is applied to an ideal high pass filter with unity gain, $|H| = 1$ and cutoff frequency, $\omega_c = 20\text{ rad/s}$.
**(a) Determine the output signal.**  
**(b) What would be range of $\omega_c$ of the filter so that first two harmonics will be blocked?**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 6, Section 6.4 & Chapter 7, Section 7.5 (*Periodic Inputs & Filtering*), pp. 637–640, 730–732
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.2 & Chapter 17, Section 17.8.2 (*Highpass Filters & Fourier Series Input*), pp. 639, 797–800

---

#### **Part (a): Determine the Output Signal**

1. **Identify the Frequencies Present in the Input:**
   * The input signal is:
     $$x(t) = \frac{3}{2} + \frac{3}{\pi}\sum_{n=1}^\infty \frac{1}{n}\sin(2\pi n t)$$
   * Fundamental frequency: $\omega_0 = 2\pi \approx 6.283\text{ rad/s}$.
   * The harmonic frequencies $\omega_n = 2\pi n$ are:
     * **DC component ($n = 0$):** $\omega = 0\text{ rad/s}$
     * **1st harmonic ($n = 1$):** $\omega_1 = 2\pi \approx 6.283\text{ rad/s}$
     * **2nd harmonic ($n = 2$):** $\omega_2 = 4\pi \approx 12.566\text{ rad/s}$
     * **3rd harmonic ($n = 3$):** $\omega_3 = 6\pi \approx 18.850\text{ rad/s}$
     * **4th harmonic ($n = 4$):** $\omega_4 = 8\pi \approx 25.133\text{ rad/s}$
     * **General $n$-th harmonic:** $\omega_n = 2\pi n\text{ rad/s}$

2. **Action of the Ideal High-Pass Filter:**
   The transfer function of the ideal high-pass filter is:
   $$|H(j\omega)| = \begin{cases} 0, & \omega < \omega_c = 20\text{ rad/s} \\ 1, & \omega > \omega_c = 20\text{ rad/s} \end{cases}$$
   * The DC component ($\omega = 0 < 20$) is **blocked**.
   * Harmonics $n = 1, 2, 3$ have frequencies $\omega_1, \omega_2, \omega_3 < 20\text{ rad/s}$, so they are **blocked**.
   * For $n \ge 4$, $\omega_n \ge 25.133\text{ rad/s} > 20\text{ rad/s}$, so they are **passed with unity gain**.

3. **Output Signal:**
   $$\mathbf{y(t) = \frac{3}{\pi} \sum_{n=4}^\infty \frac{1}{n}\sin(2\pi nt)}$$

---

#### **Part (b): Range of $\omega_c$ to Block the First Two Harmonics**
* To block the first two harmonics, their frequencies must fall strictly in the stopband:
  $$\omega_c > \omega_2 = 4\pi \approx 12.566\text{ rad/s}$$
* To pass the third and subsequent harmonics, the third harmonic frequency must lie in the passband:
  $$\omega_c \le \omega_3 = 6\pi \approx 18.850\text{ rad/s}$$
* Therefore, the required range of cutoff frequency $\omega_c$ is:
  $$\mathbf{4\pi < \omega_c \le 6\pi\text{ rad/s}} \quad \text{or} \quad \mathbf{12.566\text{ rad/s} < \omega_c \le 18.850\text{ rad/s}}$$

---

### 20. Page 37, Q.1: The following input signal is applied to an ideal band pass filer with gain, $|H| = 1$ and lower cutoff frequency, $\omega_1 = 6\text{ rad/s}$ and upper cutoff frequency, $\omega_2 = 12\text{ rad/s}$. (a) Determine the output signal. (b) What would be the range of bandwidth and the corner frequency so that the filter allows only the fundamental component.

```
                  x(t)
                   ^
                 1 |    +-------+       +-------+
                   |    |       |       |       |
      ---+---------+----+---+---+---+---+---+---+---+---> t
        -4        -2   0|   1   2   |   4   5   6
                        |           |
                    -1  +-----------+
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 6, Section 6.4 & Chapter 7, Section 7.5 (*Periodic Inputs & Filtering*), pp. 637–640, 730–732
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.3 & Chapter 17, Section 17.8.2 (*Bandpass Filters & Harmonic Response*), pp. 639–640, 797–800

---

#### **Part (a): Determine the Output Signal**

1. **Fourier Series Expansion of the Input Signal:**
   * From the figure, $x(t)$ is an **odd periodic square wave** with period $T = 4\text{ s}$ and amplitude $A = 1$:
     $$x(t) = \begin{cases} +1, & 0 < t < 2 \\ -1, & 2 < t < 4 \end{cases}$$
   * Fundamental frequency:
     $$\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{4} = \frac{\pi}{2}\text{ rad/s} \approx 1.5708\text{ rad/s}$$
   * Because of odd symmetry and half-wave symmetry:
     $$a_0 = 0, \quad a_n = 0, \quad b_n = 0 \text{ (for even } n\text{)}$$
   * For odd $n$:
     $$b_n = \frac{4}{T}\int_0^{T/2} x(t)\sin(n\omega_0 t)dt = \frac{4}{4}\int_0^2 (1)\sin\left(\frac{n\pi}{2}t\right)dt = \frac{4}{n\pi}$$
   * Thus, the Fourier series of the input is:
     $$x(t) = \sum_{n=1,3,5,\dots}^\infty \frac{4}{n\pi}\sin\left(\frac{n\pi}{2}t\right)$$

2. **Frequencies of the Harmonics:**
   * $n = 1$ (Fundamental): $\omega_1' = 1 \times \frac{\pi}{2} \approx 1.571\text{ rad/s}$
   * $n = 3$: $\omega_3' = 3 \times \frac{\pi}{2} \approx 4.712\text{ rad/s}$
   * $n = 5$: $\omega_5' = 5 \times \frac{\pi}{2} \approx 7.854\text{ rad/s}$
   * $n = 7$: $\omega_7' = 7 \times \frac{\pi}{2} \approx 10.996\text{ rad/s}$
   * $n = 9$: $\omega_9' = 9 \times \frac{\pi}{2} \approx 14.137\text{ rad/s}$

3. **Filtering by the Ideal Bandpass Filter:**
   * Passband range: $6\text{ rad/s} \le \omega \le 12\text{ rad/s}$.
   * Comparing each harmonic frequency:
     * $n = 1$ ($\omega \approx 1.571\text{ rad/s} < 6$): **Blocked**
     * $n = 3$ ($\omega \approx 4.712\text{ rad/s} < 6$): **Blocked**
     * $n = 5$ ($\omega \approx 7.854\text{ rad/s} \in [6, 12]$): **Passed**
     * $n = 7$ ($\omega \approx 10.996\text{ rad/s} \in [6, 12]$): **Passed**
     * $n = 9$ ($\omega \approx 14.137\text{ rad/s} > 12$): **Blocked**

   Therefore, only the 5th and 7th harmonics are transmitted:
   $$\mathbf{y(t) = \frac{4}{5\pi}\sin\left(\frac{5\pi}{2}t\right) + \frac{4}{7\pi}\sin\left(\frac{7\pi}{2}t\right)}$$

---

#### **Part (b): Range of Bandwidth and Corner Frequencies to Pass Only the Fundamental**
* The fundamental component is located at:
  $$\omega_0 = \frac{\pi}{2} \approx 1.571\text{ rad/s}$$
* The next nonzero harmonic is the 3rd harmonic at:
  $$\omega_3 = \frac{3\pi}{2} \approx 4.712\text{ rad/s}$$

To pass **only** the fundamental component:
1. **Lower Corner Frequency ($\omega_{c1}$):**
   Must be less than or equal to the fundamental, but above zero:
   $$0 < \omega_{c1} \le \frac{\pi}{2}\text{ rad/s} \quad (0 < \omega_{c1} \le 1.571\text{ rad/s})$$
2. **Upper Corner Frequency ($\omega_{c2}$):**
   Must be greater than or equal to the fundamental, but less than the 3rd harmonic:
   $$\frac{\pi}{2} \le \omega_{c2} < \frac{3\pi}{2}\text{ rad/s} \quad (1.571\text{ rad/s} \le \omega_{c2} < 4.712\text{ rad/s})$$
3. **Range of Bandwidth ($B = \omega_{c2} - \omega_{c1}$):**
   * The maximum possible bandwidth occurs when $\omega_{c1} \to 0$ and $\omega_{c2} \to \frac{3\pi}{2}$:
     $$B_{\max} < \frac{3\pi}{2} - 0 \approx \mathbf{4.712\text{ rad/s}}$$
   * Hence, the bandwidth must satisfy:
     $$\mathbf{0 < B < \frac{3\pi}{2}\text{ rad/s}} \quad (\mathbf{0 < B < 4.712\text{ rad/s}})$$
     with the passband $[\omega_{c1}, \omega_{c2}]$ containing $\omega = \frac{\pi}{2}\text{ rad/s}$.

### 21. Page 38, Q.1: The following input signal is applied to an ideal low pass filer with gain, $|H| = 1$ and cutoff frequency, $\omega_c = 12\text{ rad/s}$. (a) Determine the output signal. (b) What would be range of $\omega_c$ of the filter to pass only the DC component.

```
                  x(t)
                   ^
                 1 |    +-------+       +-------+
                   |    |       |       |       |
      ---+---------+----+---+---+---+---+---+---+---+---> t
        -4        -2   0|   1   2   |   4   5   6
                        |           |
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 6, Section 6.4 & Chapter 7, Section 7.5 (*Periodic Inputs & Filtering*), pp. 637–640, 730–732
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.1 & Chapter 17, Section 17.8.2 (*Lowpass Filters & DC Filtering*), pp. 638–639, 797–800

---

#### **Part (a): Determine the Output Signal**

1. **Fourier Series Expansion of the Input Signal:**
   * The input signal $x(t)$ is a periodic unipolar pulse train with amplitude $A = 1$ and period $T = 4\text{ s}$:
     $$x(t) = \begin{cases} 1, & 0 < t < 2 \\ 0, & 2 < t < 4 \end{cases}$$
   * Fundamental angular frequency:
     $$\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{4} = \frac{\pi}{2}\text{ rad/s} \approx 1.5708\text{ rad/s}$$
   * **DC Component ($a_0$):**
     $$a_0 = \frac{1}{T}\int_0^T x(t) dt = \frac{1}{4}\int_0^2 (1) dt = \frac{2}{4} = \frac{1}{2}$$
   * **Fourier Coefficients ($a_n, b_n$):**
     $$a_n = \frac{2}{4}\int_0^2 \cos\left(\frac{n\pi}{2}t\right) dt = \frac{1}{2}\left[\frac{2}{n\pi}\sin\left(\frac{n\pi}{2}t\right)\right]_0^2 = \frac{1}{n\pi}\sin(n\pi) = 0$$
     $$b_n = \frac{2}{4}\int_0^2 \sin\left(\frac{n\pi}{2}t\right) dt = \frac{1}{2}\left[-\frac{2}{n\pi}\cos\left(\frac{n\pi}{2}t\right)\right]_0^2 = \frac{1}{n\pi}[1 - \cos(n\pi)]$$
     $$b_n = \begin{cases} \frac{2}{n\pi}, & n \text{ is odd} \\ 0, & n \text{ is even} \end{cases}$$
   * Therefore, the input signal is represented as:
     $$x(t) = \frac{1}{2} + \sum_{n=1,3,5,\dots}^\infty \frac{2}{n\pi}\sin\left(\frac{n\pi}{2}t\right)$$

2. **Harmonic Frequencies Present in $x(t)$:**
   * DC component: $\omega = 0\text{ rad/s}$
   * $n = 1$ (Fundamental): $\omega_1 = \frac{\pi}{2} \approx 1.571\text{ rad/s}$
   * $n = 3$: $\omega_3 = \frac{3\pi}{2} \approx 4.712\text{ rad/s}$
   * $n = 5$: $\omega_5 = \frac{5\pi}{2} \approx 7.854\text{ rad/s}$
   * $n = 7$: $\omega_7 = \frac{7\pi}{2} \approx 10.996\text{ rad/s}$
   * $n = 9$: $\omega_9 = \frac{9\pi}{2} \approx 14.137\text{ rad/s}$

3. **Filtering Action ($\omega_c = 12\text{ rad/s}$):**
   * The ideal low-pass filter passes all frequencies where $\omega < \omega_c = 12\text{ rad/s}$ with unity gain ($|H| = 1$), and completely blocks all components where $\omega > 12\text{ rad/s}$.
   * Since $\omega = 0, \omega_1, \omega_3, \omega_5, \omega_7 < 12\text{ rad/s}$, the DC term and the 1st, 3rd, 5th, and 7th harmonics are passed.
   * Since $\omega_9 = 14.137\text{ rad/s} > 12\text{ rad/s}$, the 9th and all higher harmonics are blocked.

4. **Output Signal:**
   $$\mathbf{y(t) = \frac{1}{2} + \frac{2}{\pi}\sin\left(\frac{\pi}{2}t\right) + \frac{2}{3\pi}\sin\left(\frac{3\pi}{2}t\right) + \frac{2}{5\pi}\sin\left(\frac{5\pi}{2}t\right) + \frac{2}{7\pi}\sin\left(\frac{7\pi}{2}t\right)}$$

---

#### **Part (b): Range of $\omega_c$ to Pass Only the DC Component**
* To pass the DC component ($\omega = 0$), the cutoff must satisfy $\omega_c > 0$.
* To eliminate all AC harmonics, $\omega_c$ must be less than or equal to the fundamental frequency ($\omega_1 = \frac{\pi}{2}\text{ rad/s}$):
  $$\mathbf{0 < \omega_c \le \frac{\pi}{2}\text{ rad/s}} \quad \text{or} \quad \mathbf{0 < \omega_c \le 1.571\text{ rad/s}}$$

---

### 22. Page 71, Q.8(c) (Bottom): A high pass Chebyshev filter is to be designed according to the following specifications:
**(i) $R_L = 600\Omega$,**  
**(ii) (ii) $\omega_c = 8800\text{ rps}$,**  
**(iii) The ripple specification is $20 \log_{10} \frac{\text{Peak Magnitude}}{\text{Valley Magnitude}} = 1\text{dB}$**  
**(iv) Slope of the decibel gain curve is to be -60 dB/decade at frequencies much lower than cut-off.**  
**(v) $G (j0)$ must be unity.**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-2, 4.10-5 & 4.12-4 (*Chebyshev Filters*), pp. 439–445, 463–466
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.2, 14.8.2 & 14.9 (*Highpass Filters & Scaling*), pp. 639, 643, 648–651

---

#### **1. Determine Filter Order ($n$) and Ripple Factor ($\epsilon$)**
* **Filter Order ($n$):** 
  At frequencies far below the high-pass cutoff ($\omega \ll \omega_c$), each zero at the origin contributes $+20\text{ dB/decade}$ towards the passband, which corresponds to an attenuation slope of:
  $$n = \frac{60\text{ dB/decade}}{20\text{ dB/decade/pole}} = 3$$
* **Ripple Factor ($\epsilon$):**
  $$\epsilon = \sqrt{10^{0.1 A_{\max}} - 1} = \sqrt{10^{0.1(1)} - 1} = \sqrt{0.2589} \approx 0.5088$$

---

#### **2. Normalized Low-Pass Prototype Poles**
For $n = 3$ and $\epsilon = 0.5088$:
$$a = \frac{1}{3}\sinh^{-1}\left(\frac{1}{0.5088}\right) = \frac{1}{3}\sinh^{-1}(1.9654) = \frac{1}{3}(1.428) = 0.4760$$
$$\sinh(a) = \sinh(0.4760) = 0.4944, \quad \cosh(a) = \cosh(0.4760) = 1.1165$$

The normalized low-pass poles are:
* Real pole: $S_1 = -\sinh(a) = -0.4944$
* Complex pair: 
  $$\sigma = \sinh(a)\sin(30^\circ) = (0.4944)(0.5) = 0.2472$$
  $$\omega = \cosh(a)\cos(30^\circ) = (1.1165)(0.8660) = 0.9669$$
  $$S_{2,3} = -0.2472 \pm j0.9669$$

The normalized low-pass polynomial is:
$$B_3(S) = (S + 0.4944)\left[(S + 0.2472)^2 + (0.9669)^2\right] = S^3 + 0.9888S^2 + 1.2384S + 0.4913$$

---

#### **3. High-Pass Transfer Function ($G(s)$)**
Apply the low-pass to high-pass transformation $S \to \frac{\omega_c}{s}$ with $\omega_c = 8800\text{ rad/s}$:
$$G(s) = \frac{s^3}{s^3 + \left(\frac{1.2384}{0.4913}\right)\omega_c s^2 + \left(\frac{0.9888}{0.4913}\right)\omega_c^2 s + \left(\frac{1}{0.4913}\right)\omega_c^3}$$
$$G(s) = \frac{s^3}{s^3 + 2.5207\omega_c s^2 + 2.0126\omega_c^2 s + 2.0354\omega_c^3}$$
Substituting $\omega_c = 8800\text{ rad/s}$:
$$\mathbf{G(s) = \frac{s^3}{s^3 + 2.218 \times 10^4 s^2 + 1.559 \times 10^8 s + 1.387 \times 10^{12}}}$$
*(Note: At high frequencies $\omega \to \infty$, $|G(j\infty)| = 1$, which satisfies passband transmission requirements).*

---

#### **4. Circuit Component Values ($R_L = 600\,\Omega$)**
For a 3rd-order, $1\text{ dB}$ ripple Chebyshev low-pass prototype terminated in $1\,\Omega$:
$$g_1 = 2.0236\text{ F}, \quad g_2 = 0.9941\text{ H}, \quad g_3 = 2.0236\text{ F}$$

Under the **low-pass to high-pass transformation**, capacitors become inductors, and inductors become capacitors:
$$C_1 = \frac{1}{\omega_c R_L g_1} = \frac{1}{8800 \times 600 \times 2.0236} = \mathbf{0.0936\text{ }\mu\text{F}}$$
$$L_2 = \frac{R_L}{\omega_c g_2} = \frac{600}{8800 \times 0.9941} = \mathbf{68.59\text{ mH}}$$
$$C_3 = \frac{1}{\omega_c R_L g_3} = \frac{1}{8800 \times 600 \times 2.0236} = \mathbf{0.0936\text{ }\mu\text{F}}$$

```
                       C1 = 0.0936 µF   C3 = 0.0936 µF
            o----------------||---------------||------------+--------o (+)
                                                            |
                                             +             [ ]
                                    L2 =   UUUU            [ ] RL =
                                  68.59 mH UUUU            [ ] 600 Ω
                                             |              |
            o--------------------------------+--------------+--------o (-)
```

---

### 23. Page 72, Q.6(a): If the sawtooth waveform in the following figure is applied to an ideal bandpass filter with the transfer function shown in the figure, determine the output.

```
       Input x(t)                                    Filter |H(ω)|
           ^                                               ^
         1 |   /|  /|  /|                                1 |       +-------+
           |  / | / | / |                                  |       |       |
           | /  |/  |/  |                                  +-------+-------+---------> ω
      -----+----+---+---+---> t                            0      15       35
          -1    0   1   2                                            (rad/s)
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 6, Section 6.4 & Chapter 7, Section 7.5 (*Periodic Inputs & Filtering*), pp. 637–640, 730–732
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.3 & Chapter 17, Section 17.8.2 (*Bandpass Filtering of Waveforms*), pp. 639–640, 797–800

---

#### **1. Fourier Series Representation of the Sawtooth Waveform**
From the waveform figure:
* Period: $T = 1\text{ s}$
* Fundamental angular frequency:
  $$\omega_0 = \frac{2\pi}{T} = \frac{2\pi}{1} = 2\pi\text{ rad/s} \approx 6.283\text{ rad/s}$$
* Over the interval $0 < t < 1$, $x(t) = t$.
* Its Fourier series expansion is:
  $$x(t) = \frac{1}{2} - \frac{1}{\pi}\sin(\omega_0 t) - \frac{1}{2\pi}\sin(2\omega_0 t) - \frac{1}{3\pi}\sin(3\omega_0 t) - \frac{1}{4\pi}\sin(4\omega_0 t) - \frac{1}{5\pi}\sin(5\omega_0 t) - \dots$$
  $$x(t) = \frac{1}{2} - \sum_{n=1}^\infty \frac{1}{n\pi}\sin(n\omega_0 t)$$

---

#### **2. Frequencies of the Harmonics**
With $\omega_0 = 2\pi\text{ rad/s} \approx 6.283\text{ rad/s}$:
* **DC component:** $\omega = 0\text{ rad/s}$
* **$n = 1$:** $\omega_1 = 2\pi \approx 6.283\text{ rad/s}$
* **$n = 2$:** $\omega_2 = 4\pi \approx 12.566\text{ rad/s}$
* **$n = 3$:** $\omega_3 = 6\pi \approx 18.850\text{ rad/s}$
* **$n = 4$:** $\omega_4 = 8\pi \approx 25.133\text{ rad/s}$
* **$n = 5$:** $\omega_5 = 10\pi \approx 31.416\text{ rad/s}$
* **$n = 6$:** $\omega_6 = 12\pi \approx 37.699\text{ rad/s}$

---

#### **3. Ideal Bandpass Filter Transmission**
The ideal bandpass filter characteristic is defined as:
$$|H(j\omega)| = \begin{cases} 1, & 15\text{ rad/s} \le \omega \le 35\text{ rad/s} \\ 0, & \text{otherwise} \end{cases}$$

Checking which harmonic frequencies fall within the passband $[15, 35]\text{ rad/s}$:
* $\omega \le 12.566\text{ rad/s}$ ($n \le 2$): **Outside (Blocked)**
* $\omega_3 = 18.850\text{ rad/s}$ ($n = 3$): **Inside (Passed)**
* $\omega_4 = 25.133\text{ rad/s}$ ($n = 4$): **Inside (Passed)**
* $\omega_5 = 31.416\text{ rad/s}$ ($n = 5$): **Inside (Passed)**
* $\omega_6 = 37.699\text{ rad/s}$ ($n \ge 6$): **Outside (Blocked)**

---

#### **4. Output Signal ($y(t)$)**
The filter passes only the 3rd, 4th, and 5th harmonics with unity gain:
$$\mathbf{y(t) = -\frac{1}{3\pi}\sin(3\omega_0 t) - \frac{1}{4\pi}\sin(4\omega_0 t) - \frac{1}{5\pi}\sin(5\omega_0 t)}$$
$$\mathbf{y(t) = -\frac{1}{3\pi}\sin(6\pi t) - \frac{1}{4\pi}\sin(8\pi t) - \frac{1}{5\pi}\sin(10\pi t)}$$

---

### 24. Page 72, Q.8(c): Develop a band-stop Butterworth filter for the following specifications. Filter order: n = 3, Cut-off frequencies: $\omega_h$ = 60, 000 rps, $\omega_l$ = 10, 000 rps, Load resistance: $R_L$ = 1000Ω.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-4 & 4.12 (*Notch Filters*), pp. 441–443, 458–460
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.7.4 & 14.8.4 (*Bandstop Filters*), pp. 640–641, 645–646

---

#### **1. Frequency Parameters**
* **Bandwidth ($B$):**
  $$B = \omega_h - \omega_l = 60{,}000 - 10{,}000 = 50{,}000\text{ rad/s}$$
* **Center / Notch Frequency ($\omega_0$):**
  $$\omega_0 = \sqrt{\omega_h \omega_l} = \sqrt{60{,}000 \times 10{,}000} = \sqrt{6 \times 10^8} \approx 24{,}495\text{ rad/s}$$
* **Load Resistance:** $R_L = 1000\,\Omega$

---

#### **2. Normalized Low-Pass Prototype ($n = 3$)**
For a 3rd-order normalized Butterworth low-pass filter with $R_L = 1\,\Omega$:
$$B_3(S) = (S + 1)(S^2 + S + 1) = S^3 + 2S^2 + 2S + 1$$
The prototype component values are:
$$g_1 = C_1' = 1.0\text{ F}, \quad g_2 = L_2' = 2.0\text{ H}, \quad g_3 = C_3' = 1.0\text{ F}$$

---

#### **3. Component Calculations for Band-Stop Filter**

* **Shunt Branches 1 and 3 (from $C_1' = C_3' = 1.0\text{ F}$):**
  Each transforms into a **parallel LC tank** in the shunt position:
  $$C_1 = C_3 = \frac{C_1'}{R_L B} = \frac{1.0}{1000 \times 50{,}000} = \mathbf{20\text{ nF}}$$
  $$L_1 = L_3 = \frac{R_L B}{\omega_0^2 C_1'} = \frac{1000 \times 50{,}000}{6 \times 10^8 \times 1.0} = \frac{5 \times 10^7}{6 \times 10^8} = \frac{1}{12}\text{ H} \approx \mathbf{83.33\text{ mH}}$$

* **Series Branch 2 (from $L_2' = 2.0\text{ H}$):**
  Transforms into a **series LC branch** in the series position:
  $$L_2 = \frac{R_L L_2'}{B} = \frac{1000 \times 2.0}{50{,}000} = \mathbf{40\text{ mH}}$$
  $$C_2 = \frac{B}{R_L \omega_0^2 L_2'} = \frac{50{,}000}{1000 \times (6 \times 10^8) \times 2.0} = \frac{50{,}000}{1.2 \times 10^{12}} = \mathbf{41.67\text{ nF}}$$

---

#### **4. Circuit Diagram**

```
                       L2 = 40 mH       C2 = 41.67 nF
            o-------------UUUUUUUU----------||------------+--------o (+)
                     |                                    |
                    ---                                  ---
            C1 =    ---                          C3 =    ---     RL =
           20 nF     |      L1 =                20 nF     |     1000 Ω
                     +----UUUUUU----+                     +----UUUUUU----+
                     |    83.33 mH  |                     |    83.33 mH  |
            o--------+--------------+---------------------+--------------+--------o (-)
```

---

#### **5. Band-Stop Transfer Function**
Substituting $S = \frac{B s}{s^2 + \omega_0^2}$ into $H_{\text{LP}}(S) = \frac{1}{S^3 + 2S^2 + 2S + 1}$:
$$H(s) = \frac{(s^2 + \omega_0^2)^3}{(s^2 + \omega_0^2)^3 + 2Bs(s^2 + \omega_0^2)^2 + 2B^2 s^2(s^2 + \omega_0^2) + B^3 s^3}$$
where $\omega_0^2 = 6 \times 10^8\text{ (rad/s)}^2$ and $B = 50{,}000\text{ rad/s}$.

---

### **Active filters**

### 25. Page 2, Q.3(c): A second order active filter is shown below. (i) Find the transfer function. (ii) Find the impulse response.

```
                    +--------------------+
                    |                    |
                    |                   --- 1 F
             1 Ω    |   1 Ω             ---
      vi(t) o---/\/\/--+-/\/\/---+       |
                       |         |       |
                                --- 1 F  |
                                ---      |
                                 |       |
                                ===      +--------o vo(t)
                                 |       |
                                 +----(-) \
                                           >-----+
                                 +----(+) /
```
*(Standard Sallen-Key low-pass filter with unity-gain follower: $R_1 = 1\,\Omega$, $R_2 = 1\,\Omega$, feedback capacitor $C_1 = 1\text{ F}$, and ground capacitor $C_2 = 1\text{ F}$.)*

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-3 (*Sallen-Key & Active Filter Stages*), pp. 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 8, Section 8.8 & Chapter 14, Section 14.8 (*Second-Order Op-Amp Active Filters*), pp. 344–346, 642–648

---

#### **(i) Find the Transfer Function $H(s) = \frac{V_o(s)}{V_i(s)}$**

1. **Node Analysis in the $s$-Domain:**
   * Let $v_x$ be the voltage at the node between the two $1\,\Omega$ resistors.
   * Since the op-amp is configured as an ideal voltage follower (unity gain):
     $$V_o(s) = V_+(s) = V_-(s)$$
   * At the non-inverting terminal ($V_+$), applying the voltage divider rule between $R_2$ and $C_2$:
     $$V_o(s) = \frac{\frac{1}{sC_2}}{R_2 + \frac{1}{sC_2}} V_x(s) = \frac{1}{1 + sR_2C_2} V_x(s)$$
     $$V_x(s) = (1 + sR_2C_2) V_o(s)$$

2. **KCL at Node $v_x$:**
   $$\frac{V_i - V_x}{R_1} + \frac{V_o - V_x}{\frac{1}{sC_1}} + \frac{V_o - V_x}{R_2} = 0$$
   $$\frac{V_i}{R_1} + sC_1 V_o = V_x \left[\frac{1}{R_1} + \frac{1}{R_2} + sC_1\right]$$

3. **Substitute $V_x(s)$:**
   $$\frac{V_i}{R_1} = (1 + sR_2C_2) V_o \left[\frac{1}{R_1} + \frac{1}{R_2} + sC_1\right] - sC_1 V_o$$
   Multiplying through by $R_1$:
   $$V_i(s) = V_o(s) \left[ s^2 R_1 R_2 C_1 C_2 + s C_2(R_1 + R_2) + 1 \right]$$
   
   Therefore, the general transfer function is:
   $$H(s) = \frac{V_o(s)}{V_i(s)} = \frac{1}{R_1 R_2 C_1 C_2 s^2 + (R_1 + R_2)C_2 s + 1}$$

4. **Substitute Component Values:**
   Given $R_1 = 1\,\Omega$, $R_2 = 1\,\Omega$, $C_1 = 1\text{ F}$, $C_2 = 1\text{ F}$:
   $$H(s) = \frac{1}{(1)(1)(1)(1)s^2 + (1 + 1)(1)s + 1}$$
   $$\mathbf{H(s) = \frac{1}{s^2 + 2s + 1} = \frac{1}{(s + 1)^2}}$$

---

#### **(ii) Find the Impulse Response $h(t)$**
The impulse response $h(t)$ is the inverse Laplace transform of $H(s)$:
$$h(t) = \mathcal{L}^{-1}\{H(s)\} = \mathcal{L}^{-1}\left\{\frac{1}{(s + 1)^2}\right\}$$

Using the standard transform pair $\mathcal{L}^{-1}\left\{\frac{1}{(s + a)^2}\right\} = t e^{-at} u(t)$:
$$\mathbf{h(t) = t e^{-t} u(t)}$$

---

### 26. Page 24, Q.2: A second-order active filter has the transfer function, $G(s) = \frac{1}{s^2+(\beta+4)s+4}$.
**(i) Find the response $g(t)$ if $\beta = 0$.**  
**(ii) Sketch $g(t)$ if $\beta = -4$.**  
**(iii) Plot poles and zeros in the complex S plane if $\beta = 4$.**  
**(iv) Find the range of $\beta$ for which the filter becomes stable.**

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-1 & 4.12-3 (*Active Filter Poles & Stability*), pp. 436–439, 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2, 14.8 & Chapter 16, Section 16.4–16.5 (*Transfer Functions, Active Filters & Stability*), pp. 614–617, 642–648, 737–740

---

#### **(i) Response $g(t)$ if $\beta = 0$**
For $\beta = 0$:
$$G(s) = \frac{1}{s^2 + 4s + 4} = \frac{1}{(s + 2)^2}$$
Taking the inverse Laplace transform:
$$\mathbf{g(t) = t e^{-2t} u(t)}$$

---

#### **(ii) Response and Sketch of $g(t)$ if $\beta = -4$**
For $\beta = -4$:
$$G(s) = \frac{1}{s^2 + (-4 + 4)s + 4} = \frac{1}{s^2 + 4} = \frac{1}{2} \left(\frac{2}{s^2 + 2^2}\right)$$
Taking the inverse Laplace transform:
$$g(t) = \frac{1}{2}\sin(2t) u(t) = 0.5\sin(2t) u(t)$$
* This represents a sustained, undamped sinusoidal oscillation with amplitude $0.5$ and period $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi \approx 3.14\text{ s}$.

```
             g(t)
             0.5 ^         _               _
                 |        / \             / \
                 |       /   \           /   \
               0 +------+-----\---------+-----\--------> t
                 |     0|      \       /       \
            -0.5 |      |       \_/             \_/
                 |      <--- π --->
```

---

#### **(iii) Plot Poles and Zeros in the Complex $s$-Plane if $\beta = 4$**
For $\beta = 4$:
$$G(s) = \frac{1}{s^2 + 8s + 4}$$
* **Zeros:** There are **no finite zeros** since the numerator is a constant ($1$).
* **Poles:** Roots of the characteristic equation $s^2 + 8s + 4 = 0$:
  $$s_{1,2} = \frac{-8 \pm \sqrt{8^2 - 4(1)(4)}}{2} = \frac{-8 \pm \sqrt{48}}{2} = -4 \pm 2\sqrt{3}$$
  $$p_1 = -4 + 3.464 = -0.536$$
  $$p_2 = -4 - 3.464 = -7.464$$
Both poles lie on the negative real axis:

```
                            jω
                             ^
                             |
         p2                  |         p1
    -----X-------------------+---------X-------------+-----> σ
      -7.464                 |       -0.536          0
                             |
                             |
```

---

#### **(iv) Range of $\beta$ for Stability**
A continuous-time linear system is stable if and only if all poles of its transfer function lie strictly in the open left-half of the $s$-plane ($\text{Re}(p) < 0$).
For the quadratic denominator $D(s) = s^2 + (\beta + 4)s + 4$:
* Both roots have negative real parts if and only if all coefficients are strictly positive:
  $$\beta + 4 > 0 \implies \mathbf{\beta > -4}$$
  $$4 > 0 \quad (\text{satisfied})$$

* **Summary of Stability:**
  * **Stable:** $\mathbf{\beta > -4}$ (Poles lie in LHP).
  * **Marginally Stable (Oscillatory):** $\beta = -4$ (Poles on $j\omega$ axis at $\pm j2$).
  * **Unstable:** $\beta < -4$ (Poles lie in RHP).

---

### **Realization of higher order filters**

### 27. Page 4, Q.8(c): Design a low pass Butterworth filter with Sallen-Key topology to satisfy the following specifications.
**pass band gain $G_p > -3\text{ dB}$ at $5\text{ kHz}$**  
**stop band gain $G_p < -20\text{ dB}$ at $50\text{ kHz}$**  
**The nth order (up to 4th) Butterworth polynomial is given below.**

```
Order    Butterworth polynomial
  1      s + 1
  2      s^2 + √2 s + 1
  3      (s + 1)(s^2 + s + 1)
  4      (s^2 + 0.765s + 1)(s^2 + 1.848s + 1)
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-3 (*Sallen-Key Filter Stages*), pp. 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.8.1, 14.8.3 & 14.9 (*Active Lowpass Realization*), pp. 643, 648–651

---

#### **1. Determine the Filter Order ($n$)**
* Passband cutoff frequency ($-3\text{ dB}$): $f_p = 5\text{ kHz} \implies \omega_c = 2\pi(5000) = 31{,}416\text{ rad/s}$.
* Stopband frequency: $f_s = 50\text{ kHz} \implies \omega_s = 2\pi(50000) = 314{,}159\text{ rad/s}$.
* Ratio: $\frac{\omega_s}{\omega_c} = \frac{50}{5} = 10$.
* Stopband attenuation requirement: $A_{\min} = 20\text{ dB}$.

Using the Butterworth order equation:
$$n \ge \frac{\log_{10}\left(10^{0.1 A_{\min}} - 1\right)}{2\log_{10}\left(\frac{\omega_s}{\omega_c}\right)} = \frac{\log_{10}\left(10^2 - 1\right)}{2\log_{10}(10)} = \frac{\log_{10}(99)}{2} = \frac{1.9956}{2} \approx 0.998 \implies n = 1$$

* **Selection of Topology:** While a 1st-order filter mathematically meets the minimum specification at $50\text{ kHz}$, the problem requires a **Sallen-Key topology**, which is a second-order active biquad ($n = 2$). Choosing $\mathbf{n = 2}$ fully satisfies the specification (providing $-40\text{ dB}$ attenuation at $50\text{ kHz}$, exceeding $-20\text{ dB}$) and directly realizes the Sallen-Key architecture.

---

#### **2. Normalized Transfer Function ($n = 2$)**
From the provided table, for $n = 2$:
$$H_n(s) = \frac{1}{s^2 + \sqrt{2}s + 1}$$

---

#### **3. Sallen-Key Circuit Component Calculation**
For an equal-resistance Sallen-Key low-pass filter:
$$R_1 = R_2 = R$$
Comparing the general transfer function:
$$H(s) = \frac{1}{s^2 R^2 C_1 C_2 + s(2RC_2) + 1}$$
with the scaled Butterworth denominator:
$$s^2 + \sqrt{2}\omega_c s + \omega_c^2 \implies \left(\frac{s}{\omega_c}\right)^2 + \sqrt{2}\left(\frac{s}{\omega_c}\right) + 1$$

Matching terms:
$$\omega_c^2 = \frac{1}{R^2 C_1 C_2} \implies C_1 C_2 = \frac{1}{R^2 \omega_c^2}$$
$$\frac{\sqrt{2}}{\omega_c} = 2 R C_2 \implies C_2 = \frac{\sqrt{2}}{2 R \omega_c} = \frac{1}{\sqrt{2} R \omega_c}$$
$$C_1 = \frac{2}{\sqrt{2} R \omega_c} = \frac{\sqrt{2}}{R \omega_c} = 2C_2$$

Let us choose a practical value: $\mathbf{R = 10\text{ k}\Omega}$.
With $\omega_c = 2\pi(5000) \approx 31{,}416\text{ rad/s}$:
$$C_1 = \frac{\sqrt{2}}{(10 \times 10^3)(31{,}416)} = 4.50\text{ nF}$$
$$C_2 = \frac{C_1}{2} = 2.25\text{ nF}$$

```
                           C1 = 4.5 nF
                    +----------||---------+
                    |                     |
          10 kΩ     |    10 kΩ            |
    Vi o---/\/\/----+----/\/\/----+       |
                                  |       |
                                 ---      |
                        C2 =     ---      |
                       2.25 nF    |       |
                                 ===      +--------o Vo
                                  |       |
                                  +----(-) \
                                            >-----+
                                  +----(+) /
```

---

### 28. Page 8, Q.8(c): Design a low pass Butterworth filter with Sallen-key topology to satisfy the following specifications.
**pass band gain $G_p > -3\text{ dB}$ at 5kHz**  
**stop band gain $G_p < -40\text{ dB}$ at 50 kHz**  
**The nth order (up to 5th) Butterworth polynomial is given below.**

```
Order    Butterworth polynomial
  1      s + 1
  2      s^2 + √2 s + 1
  3      (s + 1)(s^2 + s + 1)
  4      (s^2 + 0.765s + 1)(s^2 + 1.848s + 1)
  5      (s + 1)(s^2 + 0.618s + 1)(s^2 + 1.618s + 1)
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-3 (*Sallen-Key Filter Stages*), pp. 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.8.1, 14.8.3 & 14.9 (*Active Lowpass Realization*), pp. 643, 648–651

---

#### **1. Determine the Filter Order ($n$)**
* Passband cutoff frequency ($-3\text{ dB}$): $f_p = 5\text{ kHz} \implies \omega_c = 2\pi(5000) = 31{,}416\text{ rad/s}$.
* Stopband frequency: $f_s = 50\text{ kHz} \implies \omega_s = 2\pi(50000) = 314{,}159\text{ rad/s}$.
* Ratio: $\frac{\omega_s}{\omega_c} = \frac{50}{5} = 10$.
* Stopband attenuation requirement: $A_{\min} = 40\text{ dB}$.

Using the order formula for the Butterworth filter:
$$n \ge \frac{\log_{10}\left(10^{0.1 A_{\min}} - 1\right)}{2\log_{10}\left(\frac{\omega_s}{\omega_c}\right)} = \frac{\log_{10}\left(10^4 - 1\right)}{2\log_{10}(10)} = \frac{\log_{10}(9999)}{2} = \frac{3.9999}{2} \approx 2.0 \implies \mathbf{n = 2}$$
Thus, an order of **$n = 2$** exactly fulfills the design specifications.

---

#### **2. Transfer Function ($n = 2$)**
From the polynomial table, for $n = 2$:
$$B_2(s) = s^2 + \sqrt{2}s + 1$$
The frequency-scaled transfer function is:
$$H(s) = \frac{\omega_c^2}{s^2 + \sqrt{2}\omega_c s + \omega_c^2}$$
Substituting $\omega_c = 31{,}416\text{ rad/s}$:
$$H(s) = \frac{9.87 \times 10^8}{s^2 + 4.443 \times 10^4 s + 9.87 \times 10^8}$$

---

#### **3. Sallen-Key Circuit Component Calculation**
Using the standard unity-gain Sallen-Key low-pass topology:
* Select equal resistors: $\mathbf{R_1 = R_2 = R = 10\text{ k}\Omega}$.
* Capacitor relations:
  $$C_1 = \frac{\sqrt{2}}{R \omega_c} = \frac{1.4142}{(10{,}000)(31{,}416)} = \mathbf{4.50\text{ nF}}$$
  $$C_2 = \frac{1}{\sqrt{2} R \omega_c} = \frac{C_1}{2} = \mathbf{2.25\text{ nF}}$$

```
                           C1 = 4.50 nF
                    +----------||---------+
                    |                     |
          10 kΩ     |    10 kΩ            |
    Vi o---/\/\/----+----/\/\/----+       |
                                  |       |
                                 ---      |
                        C2 =     ---      |
                       2.25 nF    |       |
                                 ===      +--------o Vo
                                  |       |
                                  +----(-) \
                                            >-----+
                                  +----(+) /
```

### 29. Page 71, Q.8(b) (Top): Design a low pass Butterworth filter with Sallen-key topology to satisfy the following specifications-
**• Passband gain $G_p > -3\text{dB}$ with passband cutoff frequency $f_p = 10\text{kHz}$**  
**• Stopband gain $G_s < -40\text{dB}$ with stopband cutoff frequency $f_s = 40\text{kHz}$**  
**The nth order (up to 5th) Butterworth polynomial is given below-**

```
Order, n    Butterworth polynomial
   1        S + 1
   2        S^2 + √2 S + 1
   3        (S + 1)(S^2 + S + 1)
   4        (S^2 + 0.765S + 1)(S^2 + 1.848S + 1)
   5        (S + 1)(S^2 + 0.618S + 1)(S^2 + 1.618S + 1)
```

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.12-3 (*Sallen-Key Filter Stages*), pp. 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.8.1, 14.8.3 & 14.9 (*Active Lowpass Realization*), pp. 643, 648–651

---

#### **1. Determine the Filter Order ($n$)**
* Passband cutoff frequency ($-3\text{ dB}$): 
  $$f_p = 10\text{ kHz} \implies \omega_c = 2\pi(10{,}000) \approx 62{,}832\text{ rad/s}$$
* Stopband edge frequency: 
  $$f_s = 40\text{ kHz} \implies \omega_s = 2\pi(40{,}000) \approx 251{,}327\text{ rad/s}$$
* Frequency ratio: 
  $$\frac{\omega_s}{\omega_c} = \frac{40\text{ kHz}}{10\text{ kHz}} = 4$$
* Minimum stopband attenuation: $A_{\min} = 40\text{ dB}$

Using the Butterworth order equation:
$$n \ge \frac{\log_{10}\left(10^{0.1 A_{\min}} - 1\right)}{2\log_{10}\left(\frac{\omega_s}{\omega_c}\right)} = \frac{\log_{10}\left(10^4 - 1\right)}{2\log_{10}(4)} = \frac{\log_{10}(9999)}{2(0.60206)} = \frac{3.99996}{1.20412} \approx 3.32$$

Rounding up to the next integer yields:
$$\mathbf{n = 4}$$

---

#### **2. Filter Decomposition**
From the table, the 4th-order normalized polynomial is:
$$B_4(S) = (S^2 + 0.765S + 1)(S^2 + 1.848S + 1)$$
To implement this using Sallen-Key active filter stages, we cascade two second-order low-pass sections:
$$H_n(S) = H_1(S) \cdot H_2(S)$$
* **Stage 1:** $H_1(S) = \frac{1}{S^2 + 0.765S + 1}$
* **Stage 2:** $H_2(S) = \frac{1}{S^2 + 1.848S + 1}$

---

#### **3. Component Calculations (Equal-Resistor Sallen-Key Topology)**
For a unity-gain Sallen-Key stage with $R_1 = R_2 = R$:
$$H(s) = \frac{1}{s^2 R^2 C_A C_B + 2RC_B s + 1}$$
Comparing with $\left(\frac{s}{\omega_c}\right)^2 + c_k\left(\frac{s}{\omega_c}\right) + 1$:
$$C_B = \frac{c_k}{2 R \omega_c}, \quad C_A = \frac{2}{c_k R \omega_c} = \frac{4}{c_k^2} C_B$$

Let us select a convenient standard resistor value: $\mathbf{R = 10\text{ k}\Omega}$.  
With $\omega_c = 2\pi(10{,}000) = 62{,}832\text{ rad/s}$:
$$2R\omega_c = 2(10{,}000)(62{,}832) = 1.2566 \times 10^9$$

* **Stage 1 ($c_1 = 0.765$):**
  $$C_2 = \frac{0.765}{1.2566 \times 10^9} = \mathbf{0.609\text{ nF}} = 609\text{ pF}$$
  $$C_1 = \frac{4}{(0.765)^2} C_2 = 6.835 \times 0.609\text{ nF} = \mathbf{4.16\text{ nF}}$$

* **Stage 2 ($c_2 = 1.848$):**
  $$C_4 = \frac{1.848}{1.2566 \times 10^9} = \mathbf{1.471\text{ nF}}$$
  $$C_3 = \frac{4}{(1.848)^2} C_4 = 1.171 \times 1.471\text{ nF} = \mathbf{1.723\text{ nF}}$$

---

#### **4. Circuit Schematic**

```
                STAGE 1 (c1 = 0.765)                      STAGE 2 (c2 = 1.848)
                    C1 = 4.16 nF                              C3 = 1.72 nF
                 +-------||-------+                        +-------||-------+
                 |                |                        |                |
         10 kΩ   |  10 kΩ         |                10 kΩ   |  10 kΩ         |
   Vi o---/\/\/--+--/\/\/--+      |          +------/\/\/--+--/\/\/--+      |
                           |      |          |                       |      |
                          ---     |          |                      ---     |
                  C2 =    ---     |          |              C4 =    ---     |
                 609 pF    |      |          |            1.47 nF    |      |
                          ===     +---o------+                      ===     +---o Vo
                           |      |                                  |      |
                           +---(-)\                                  +---(-)\
                                   >----+                                    >----+
                           +---(+)/                                  +---(+)/
```

---

### **First and second order transfer functions**
*(Note: These refer specifically to extracting or analyzing mathematical properties of 1st/2nd order filters. Some crossover with Active Filters above).*

### 30. Page 44, Q.1: A second order filter circuit has the following transfer function: Find the range of k so that
**(i) The filter becomes stable.**  
**(ii) The filter provides oscillation**  
$$H(s) = \frac{10}{s^2+(k-5)s+10}$$

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-1 & 4.10-5 (*Transfer Function Stability*), pp. 436–439, 444–445
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2 & Chapter 16, Section 16.4–16.5 (*Transfer Function Analysis & Stability*), pp. 614–617, 737–740

---

#### **(i) Range of $k$ for Stability**
* **Characteristic Equation:** 
  $$D(s) = s^2 + (k - 5)s + 10 = 0$$
* A second-order continuous system $s^2 + a_1 s + a_0 = 0$ is **strictly stable** (all poles have negative real parts, i.e., lie in the open left-half of the $s$-plane) if and only if all coefficients of the characteristic polynomial are strictly positive:
  $$a_1 = k - 5 > 0 \implies \mathbf{k > 5}$$
  $$a_0 = 10 > 0 \quad (\text{satisfied})$$

* **Conclusion:** The filter is stable for **$k > 5$**.

---

#### **(ii) Value of $k$ for Oscillation**
* A linear filter produces **sustained undamped oscillations** when its poles lie directly on the imaginary axis (i.e., $\text{Re}(s) = 0$ with $\text{Im}(s) \ne 0$).
* Setting the damping term to zero:
  $$k - 5 = 0 \implies \mathbf{k = 5}$$

* **Verification:**
  For $k = 5$, the transfer function is:
  $$H(s) = \frac{10}{s^2 + 10}$$
  The poles are:
  $$s_{1,2} = \pm j\sqrt{10}$$
  The impulse response is:
  $$h(t) = \mathcal{L}^{-1}\left\{\frac{10}{s^2 + (\sqrt{10})^2}\right\} = \sqrt{10}\sin(\sqrt{10}t)u(t)$$
  which represents continuous, non-decaying sinusoidal oscillation at frequency $\omega_0 = \sqrt{10} \approx 3.162\text{ rad/s}$.

* **Conclusion:** The filter provides sustained oscillation when **$k = 5$**.

---

### 31. Page 57, Q.3(c): A second order active circuit has the following transfer function, $H(s) = \frac{1}{s^2+(\beta+4)s+4}$. Find the impulse response if (i) $\beta = 0$, (ii) $\beta = -4$ and (iii) $\beta = -8$.

> [!info] **Textbook References**
> * **BP Lathi (3rd Ed):** Chapter 4, Section 4.10-1 & 4.12-3 (*Active Circuit Analysis*), pp. 436–439, 460–463
> * **Alexander & Sadiku (5th Ed):** Chapter 14, Section 14.2 & Chapter 15, Section 15.3–15.5 (*Transfer Functions & Inverse Laplace Transforms*), pp. 614–617, 679–695

The impulse response $h(t)$ is obtained by taking the inverse Laplace transform of $H(s)$:
$$h(t) = \mathcal{L}^{-1}\{H(s)\}$$

---

#### **(i) Case $\beta = 0$**
Substitute $\beta = 0$ into $H(s)$:
$$H(s) = \frac{1}{s^2 + 4s + 4} = \frac{1}{(s + 2)^2}$$
Using the Laplace transform pair $\mathcal{L}^{-1}\left\{\frac{1}{(s + a)^2}\right\} = t e^{-at} u(t)$:
$$\mathbf{h(t) = t e^{-2t} u(t)}$$
*(This is a critically damped stable response).*

---

#### **(ii) Case $\beta = -4$**
Substitute $\beta = -4$ into $H(s)$:
$$H(s) = \frac{1}{s^2 + (-4 + 4)s + 4} = \frac{1}{s^2 + 4} = \frac{1}{2}\left(\frac{2}{s^2 + 2^2}\right)$$
Using the Laplace transform pair $\mathcal{L}^{-1}\left\{\frac{\omega}{s^2 + \omega^2}\right\} = \sin(\omega t) u(t)$:
$$\mathbf{h(t) = \frac{1}{2}\sin(2t) u(t) = 0.5\sin(2t) u(t)}$$
*(This is an undamped sinusoidal oscillation with a frequency of $2\text{ rad/s}$).*

---

#### **(iii) Case $\beta = -8$**
Substitute $\beta = -8$ into $H(s)$:
$$H(s) = \frac{1}{s^2 + (-8 + 4)s + 4} = \frac{1}{s^2 - 4s + 4} = \frac{1}{(s - 2)^2}$$
Using the Laplace transform pair $\mathcal{L}^{-1}\left\{\frac{1}{(s - a)^2}\right\} = t e^{at} u(t)$:
$$\mathbf{h(t) = t e^{2t} u(t)}$$
*(This is an unstable, exponentially growing response due to a double repeated pole in the right-half plane at $s = +2$).*

---

### **Realisation of passive filter circuits**
*(No specific questions exclusively defining or asking to realize a passive filter circuit from scratch using inductor/capacitor ladder networks were found, outside of the active Sallen-Key topologies and generic RLC analyses covered in other sections).*

---

> **Note:** With the completion of Question 31, all 31 problems contained in the uploaded exam document have now been fully solved in sequence.
> 