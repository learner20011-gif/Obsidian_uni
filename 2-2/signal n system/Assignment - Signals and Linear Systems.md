# Department of Electrical & Electronic Engineering
## Rajshahi University of Engineering & Technology

![[attachments/assignment_ruet_logo.png|150]]

# Assignment

**Course Code :** EEE 2201  
**Course Title :** Signals and Linear Systems  

---

| **Submitted By:** | **Submitted To:** |
| :--- | :--- |
| **Name :** Nafis Sadiq | **Dr. Md. Samiul Habib** |
| **Roll :** 2301103 | Professor |
| **Section :** B | Department of Electrical & Electronic Engineering |
| | Rajshahi University of Engineering & Technology |

**Date of Submission :** 06 October 2026

---

## 1.

A radio link sends two message signals, $m_1(t)$ and $m_2(t)$, through one channel. Each message has a bandwidth of $3000\text{ rad/s}$, and Fig. 1(a) shows the spectra. The transmitter in Fig. 1(b) moves $m_2(t)$ onto a $6000\text{ rad/s}$ subcarrier. A summer adds the shifted signal to $m_1(t)$ and produces the multiplexed signal at point $q$. A second modulator places $q(t)$ on an $18,000\text{ rad/s}$ carrier. The signal at point $r$ enters the channel. Both modulators have a gain of 2.

(a) Sketch the spectrum at points $p$, $q$, and $r$. Label every frequency component and band edge.

(b) Design a receiver. Draw the block diagram, give the type and cutoff of each filter, and show the steps you use to recover $m_1(t)$ and $m_2(t)$.

(c) State the band of frequencies the channel carries.

![[attachments/assignment_fig1_transmitter.png]]
*Fig. 1. Message spectra and transmitter for the two-signal FDM link.*

### Solution:

**(a)** Apply the modulation property $\mathcal{F}\{2x(t)\cos(\omega_0 t)\} = X(\omega - \omega_0) + X(\omega + \omega_0)$ at each modulator.

**Point $p$.** The signal is $p(t) = 2m_2(t)\cos(6000t)$, so
$$P(\omega) = M_2(\omega - 6000) + M_2(\omega + 6000)$$

$M_2(\omega)$ fills $|\omega| \le 3000\text{ rad/s}$. Therefore $P(\omega)$ has one group of lobes on $[3000, 9000]\text{ rad/s}$ and a mirror group on $[-9000, -3000]\text{ rad/s}$. The band $|\omega| < 3000\text{ rad/s}$ stays empty.

**Point $q$.** The summer gives $q(t) = m_1(t) + p(t)$, so
$$Q(\omega) = M_1(\omega) + M_2(\omega - 6000) + M_2(\omega + 6000)$$

$M_1(\omega)$ fills $|\omega| \le 3000\text{ rad/s}$. Both $M_1$ and $M_2$ fall to zero at $\omega = \pm 3000\text{ rad/s}$, so the two parts meet at those points with no overlap. The multiplexed signal extends to $9000\text{ rad/s}$.

**Point $r$.** The second modulator gives $r(t) = 2q(t)\cos(18000t)$, so
$$\begin{aligned}
R(\omega) &= Q(\omega - 18000) + Q(\omega + 18000) \\
&= M_1(\omega - 18000) + M_2(\omega - 12000) + M_2(\omega - 24000) \\
&\quad + M_1(\omega + 18000) + M_2(\omega + 12000) + M_2(\omega + 24000)
\end{aligned}$$

For $\omega > 0$, the spectrum holds an $M_2$ group centered at $12,000\text{ rad/s}$ on $[9000, 15000]\text{ rad/s}$, an $M_1$ triangle centered at $18,000\text{ rad/s}$ on $[15000, 21000]\text{ rad/s}$, and an $M_2$ group centered at $24,000\text{ rad/s}$ on $[21000, 27000]\text{ rad/s}$. The negative side mirrors these three parts. Fig. 2 shows all three spectra.

![[attachments/assignment_fig2_spectra.png]]
*Fig. 2. Spectra at points $p$, $q$, and $r$. Gold marks $m_1$ content and teal marks $m_2$ content.*

**(b)** Recover the messages in two stages. Stage one returns $r(t)$ to the multiplexed baseband signal $q(t)$. Stage two separates $m_1(t)$ from the subcarrier term $p(t)$ and demodulates $p(t)$.

**Step 1: Return to baseband.** Multiply $r(t)$ by a synchronized carrier $\cos(18000t)$:
$$v_1(t) = r(t)\cos(18000t) = 2q(t)\cos^2(18000t) = q(t) + q(t)\cos(36000t)$$

The first term is the wanted baseband signal, which extends to $9000\text{ rad/s}$. The second term occupies $[27000, 45000]\text{ rad/s}$ on the positive side. A low-pass filter, $\text{LPF}_1$, with a cutoff of $12,000\text{ rad/s}$ keeps $q(t)$ and removes the second term. Any cutoff from $9000$ to $27000\text{ rad/s}$ works.

**Step 2: Recover $m_1(t)$.** Pass $q(t)$ through $\text{LPF}_2$ with a cutoff of $3000\text{ rad/s}$. The lobes of $p(t)$ start at $3000\text{ rad/s}$, so $\text{LPF}_2$ rejects them and outputs $m_1(t)$.

**Step 3: Recover $m_2(t)$.** Pass $q(t)$ through a bandpass filter, BPF, with a passband of $3000$ to $9000\text{ rad/s}$. This filter removes $m_1(t)$ and returns $p(t)$. Multiply $p(t)$ by $\cos(6000t)$:
$$v_2(t) = p(t)\cos(6000t) = 2m_2(t)\cos^2(6000t) = m_2(t) + m_2(t)\cos(12000t)$$

The second term occupies $[9000, 15000]\text{ rad/s}$ on the positive side. $\text{LPF}_3$ with a cutoff of $3000\text{ rad/s}$ removes this term and outputs $m_2(t)$. Every filter has unity gain in its passband. Fig. 3 shows the complete receiver.

![[attachments/assignment_fig3_receiver.png]]
*Fig. 3. Receiver block diagram for recovering the two messages.*

**(c)** The positive side of $R(\omega)$ occupies $9000$ to $27000\text{ rad/s}$, which equals about $1.43\text{ kHz}$ to $4.30\text{ kHz}$. The width is $18,000\text{ rad/s}$, or about $2.86\text{ kHz}$. The channel must pass this band and its mirror image on the negative side.

---

## 2.

A continuous-time signal is given by
$$x(t) = 8\cos(16\pi t) + 6\cos(8\pi t) + 12\cos(4\pi t)$$

An ideal impulse sampler runs at $8\text{ Hz}$. Find the spectrum of the sampled signal and answer the questions below.

(a) Does low-pass filtering of the sampled signal recover $x(t)$?

(b) The sampler now runs at $24\text{ Hz}$. Do you recover $x(t)$? Explain your answer and give the filter you use.

### Solution:

**(a)** Convert each angular frequency to hertz. The three tones sit at $8\text{ Hz}$, $4\text{ Hz}$, and $2\text{ Hz}$. A cosine $A\cos(2\pi f_0 t)$ has two impulses of weight $A/2$ at $\pm f_0$, so
$$X(f) = 4[\delta(f - 8) + \delta(f + 8)] + 3[\delta(f - 4) + \delta(f + 4)] + 6[\delta(f - 2) + \delta(f + 2)]$$

Ideal impulse sampling at $f_s = 8\text{ Hz}$ scales the spectrum by $f_s$ and repeats the spectrum every $f_s$:
$$X_s(f) = f_s \sum_{k=-\infty}^\infty X(f - kf_s) = 8 \sum_{k=-\infty}^\infty X(f - 8k)$$

The highest frequency is $8\text{ Hz}$, so the Nyquist rate is $16\text{ Hz}$. A rate of $8\text{ Hz}$ falls below this value and the replicas overlap. Inside the base interval $|f| \le 4\text{ Hz}$, the $8\text{ Hz}$ impulses of the $k = \pm 1$ replicas land on $f = 0$ and add to $8(4 + 4) = 64$. The $4\text{ Hz}$ impulses sit on the edges $f = \pm 4\text{ Hz}$. Each edge receives $8(3 + 3) = 48$, because the $k = 0$ replica and a neighboring replica both place an impulse there. The $2\text{ Hz}$ impulses stay in place with weight $8 \times 6 = 48$. Therefore
$$X_s(f) = 64\delta(f) + 48[\delta(f - 2) + \delta(f + 2)] + 48[\delta(f - 4) + \delta(f + 4)], \quad |f| \le 4\text{ Hz}$$
and the pattern repeats with a period of $8\text{ Hz}$, as Fig. 4 shows.

Check the result in the time domain. The samples are $x[n] = x(n/8) = 8 + 6(-1)^n + 12\cos(n\pi/2)$. These values are $26, 2, 2, 2$ and repeat every four samples. A low-pass filter with a cutoff of $4\text{ Hz}$, a passband gain of $1/8$, and a gain of $1/16$ at the edges returns
$$y(t) = 8 + 12\cos(4\pi t) + 6\cos(8\pi t)$$

Compare $y(t)$ with $x(t)$. The $8\text{ Hz}$ tone turns into a constant level of $8$. Both signals pass through the same samples, as the time plot in Fig. 4 shows, so no filter separates them. The answer is no. Aliasing destroys information and you cannot undo the loss.

![[attachments/assignment_fig4_sampling_8hz.png]]
*Fig. 4. Sampling $x(t)$ at $f_s = 8\text{ Hz}$. Left: $x(t)$ and the filter output $y(t)$ share every sample. Right: sampled spectrum with the base interval in pink.*

**(b)** Set $f_s = 24\text{ Hz}$. The sampled spectrum becomes
$$X_s(f) = 24 \sum_{k=-\infty}^\infty X(f - 24k)$$

The base interval now holds impulses of weight $24 \times 4 = 96$ at $\pm 8\text{ Hz}$, $24 \times 3 = 72$ at $\pm 4\text{ Hz}$, and $24 \times 6 = 144$ at $\pm 2\text{ Hz}$. The nearest replica impulse sits at $24 - 8 = 16\text{ Hz}$. This leaves a guard gap from $8\text{ Hz}$ to $16\text{ Hz}$, as Fig. 5 shows. The rate of $24\text{ Hz}$ equals $1.5$ times the Nyquist rate, so the replicas do not overlap.

Use an ideal low-pass filter with a gain of $1/24$ and a cutoff $f_c$ between $8\text{ Hz}$ and $16\text{ Hz}$, for example $12\text{ Hz}$. The filter passes the base interval and rejects every replica, so the output spectrum equals $X(f)$. The answer is yes. You recover $x(t)$ exactly. In the time domain, the same filter performs the interpolation
$$x(t) = \sum_{n=-\infty}^\infty x(n/24)\,\text{sinc}(24t - n)$$
where $\text{sinc}(u) = \sin(\pi u)/(\pi u)$.

![[attachments/assignment_fig5_sampling_24hz.png]]
*Fig. 5. Sampling $x(t)$ at $f_s = 24\text{ Hz}$. Right: the guard gap between $8\text{ Hz}$ and $16\text{ Hz}$ lets a $12\text{ Hz}$ low-pass filter isolate the base interval.*

---

### Comparison of Sampling Rates

Table 1 compares the two sampling rates.

| Sampling rate | Nyquist rate | Overlap of replicas | Guard gap | Recover $x(t)$ |
| :---: | :---: | :---: | :---: | :---: |
| 8 Hz | 16 Hz | Yes | None | No |
| 24 Hz | 16 Hz | No | 8 Hz to 16 Hz | Yes |

*Table 1. Results for the two sampling rates.*
