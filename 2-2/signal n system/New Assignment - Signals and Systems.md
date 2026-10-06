
---

## Problem 1: Frequency-Division Multiplexing (FDM) System

### Problem Statement
You transmit two information-bearing message signals $m_1(t)$ and $m_2(t)$ across a shared transmission channel simultaneously without mutual spectral overlap. Figure 1 shows the baseband spectra of both signals alongside the complete transmitter architecture. Signal $m_1(t)$ occupies baseband $[-5000, 5000]\text{ rad/s}$ with a spectral null at DC ($\omega = 0$). Signal $m_2(t)$ occupies baseband $[-5000, 5000]\text{ rad/s}$ with peak spectral density at DC.

At the transmitter:
1. Message $m_2(t)$ multiplies a subcarrier $2\cos(10000t)$, generating modulated subcarrier signal $a(t)$ at Point $a$.
2. An adder combines $m_1(t)$ and $a(t)$ into a composite baseband multiplexed signal $b(t)$ at Point $b$.
3. The multiplexed signal $b(t)$ modulates a primary carrier $2\cos(20000t)$, producing transmitted signal $c(t)$ at Point $c$.

**Tasks:**
1. Determine and sketch the Fourier spectrum at Point $a$, Point $b$, and Point $c$. Label all frequency components, band edges, and nulls.
2. Design a complete receiver architecture to reconstruct message signals $m_1(t)$ and $m_2(t)$ from the received channel signal $c(t)$. Specify the filter types, cutoff frequencies, and mixer carrier frequencies.

![[attachments/fdm_transmitter_scheme.png]]
*Fig. 1. Baseband spectra of $m_1(t)$ and $m_2(t)$ alongside the FDM transmitter architecture.*

---

### Solution to Problem 1

#### (a) Spectral Derivations at Nodes $a$, $b$, and $c$
Apply the modulation property of the Fourier transform:
$$\mathcal{F}\{2x(t)\cos(\omega_0 t)\} = X(\omega - \omega_0) + X(\omega + \omega_0)$$

**Spectrum at Point $a$:**
$$a(t) = 2m_2(t)\cos(10000t)$$
$$A(\omega) = M_2(\omega - 10000) + M_2(\omega + 10000)$$
Because $M_2(\omega)$ spans $[-5000, 5000]\text{ rad/s}$ with its peak at $\omega = 0$, $A(\omega)$ consists of two sideband lobes centered at $\pm 10000\text{ rad/s}$. These sidebands fill $[-15000, -5000]\text{ rad/s}$ and $[5000, 15000]\text{ rad/s}$. The interval $[-5000, 5000]\text{ rad/s}$ remains vacant.

**Spectrum at Point $b$:**
$$b(t) = m_1(t) + a(t)$$
$$B(\omega) = M_1(\omega) + M_2(\omega - 10000) + M_2(\omega + 10000)$$
Message $M_1(\omega)$ fills baseband $[-5000, 5000]\text{ rad/s}$ with a spectral zero at $\omega = 0$. Because $M_1(\pm 5000) = M_2(\pm 5000) = 0$, the baseband spectrum of $m_1(t)$ and the subcarrier sidebands of $m_2(t)$ meet at $\pm 5000\text{ rad/s}$ without spectral overlap. The composite signal occupies $[-15000, 15000]\text{ rad/s}$.

**Spectrum at Point $c$:**
$$c(t) = 2b(t)\cos(20000t)$$
$$C(\omega) = B(\omega - 20000) + B(\omega + 20000)$$
$$C(\omega) = M_1(\omega \mp 20000) + M_2(\omega \mp 10000) + M_2(\omega \mp 30000)$$

Over positive frequencies:
- $M_2$ sideband centered at $10000\text{ rad/s}$, occupying $[5000, 15000]\text{ rad/s}$.
- $M_1$ signal centered at $20000\text{ rad/s}$, occupying $[15000, 25000]\text{ rad/s}$.
- $M_2$ sideband centered at $30000\text{ rad/s}$, occupying $[25000, 35000]\text{ rad/s}$.

Negative frequencies mirror these three components symmetrically. The required transmission bandwidth spans $[5000, 35000]\text{ rad/s}$, giving an RF bandwidth of $30000\text{ rad/s} \approx 4.77\text{ kHz}$.

![[attachments/fdm_spectra_nodes.png]]
*Fig. 2. Signal spectra at Point $a$, Point $b$, and Point $c$ in the FDM system.*

---

#### (b) Receiver Architecture and Demodulation
You recover both message signals using two synchronous detection stages.

**Stage 1: Downconversion to Composite Baseband $b(t)$**
Mix received channel signal $c(t)$ with a local oscillator synchronized to $\cos(20000t)$:
$$v_1(t) = c(t)\cos(20000t) = 2b(t)\cos^2(20000t) = b(t) + b(t)\cos(40000t)$$
The product produces composite baseband signal $b(t)$ centered at DC alongside high-frequency replicas centered at $\pm 40000\text{ rad/s}$. Because $b(t)$ has a maximum frequency of $15000\text{ rad/s}$, pass $v_1(t)$ through a low-pass filter ($\text{LPF}_1$) having cutoff frequency $\omega_{c1} = 15000\text{ rad/s}$. This filter eliminates the $40000\text{ rad/s}$ components and yields $b(t)$.

**Stage 2: Separation and Demodulation of $m_1(t)$ and $m_2(t)$**
- **Recovery of $m_1(t)$:** Signal $m_1(t)$ resides within $|\omega| \le 5000\text{ rad/s}$, while modulated term $a(t)$ occupies $5000 \le |\omega| \le 15000\text{ rad/s}$. Route $b(t)$ through a low-pass filter ($\text{LPF}_2$) with cutoff frequency $\omega_{c2} = 5000\text{ rad/s}$ to extract $m_1(t)$.
- **Recovery of $m_2(t)$:** Route $b(t)$ through a bandpass filter ($\text{BPF}_1$) with passband $[5000, 15000]\text{ rad/s}$ to isolate $a(t)$. Mix isolated subcarrier signal $a(t)$ with subcarrier $\cos(10000t)$:
  $$v_2(t) = a(t)\cos(10000t) = 2m_2(t)\cos^2(10000t) = m_2(t) + m_2(t)\cos(20000t)$$
  Feed $v_2(t)$ through a low-pass filter ($\text{LPF}_3$) with cutoff frequency $\omega_{c3} = 5000\text{ rad/s}$ to eliminate the $20000\text{ rad/s}$ terms and isolate $m_2(t)$.

![[attachments/fdm_receiver_architecture.png]]
*Fig. 3. Block diagram of the synchronous FDM receiver architecture.*

---

## Problem 2: Signal Sampling, Aliasing, and Reconstruction

### Problem Statement
Consider the continuous-time signal:
$$x(t) = 10\cos(20\pi t) + 5\cos(10\pi t) + 15\cos(5\pi t)$$

An ideal impulse train samples $x(t)$ at sampling frequency $f_s = 10\text{ Hz}$.
1. Derive the Fourier spectrum $X_s(f)$ of the sampled signal within the fundamental Nyquist interval.
2. Determine whether you can reconstruct original continuous signal $x(t)$ by low-pass filtering the sampled signal.
3. If you increase the sampling rate to $f_s = 20\text{ Hz}$, explain whether you can reconstruct $x(t)$ completely.

---

### Solution to Problem 2

#### (a) Spectrum at $f_s = 10\text{ Hz}$ and Reconstruction Feasibility
Calculate the cyclic frequencies in hertz:
- $20\pi\text{ rad/s} \implies f_1 = 10\text{ Hz}$
- $10\pi\text{ rad/s} \implies f_2 = 5\text{ Hz}$
- $5\pi\text{ rad/s} \implies f_3 = 2.5\text{ Hz}$

Using Euler's identity $\cos(2\pi f_0 t) \leftrightarrow \frac{1}{2}[\delta(f - f_0) + \delta(f + f_0)]$, the continuous-time Fourier transform is:
$$X(f) = 5[\delta(f - 10) + \delta(f + 10)] + 2.5[\delta(f - 5) + \delta(f + 5)] + 7.5[\delta(f - 2.5) + \delta(f + 2.5)]$$

Sampling $x(t)$ at $f_s = 10\text{ Hz}$ produces a periodic spectrum:
$$X_s(f) = 10\sum_{k=-\infty}^\infty X(f - 10k)$$

Inside the fundamental Nyquist interval $|f| \le \frac{f_s}{2} = 5\text{ Hz}$:
- The $10\text{ Hz}$ components from replicas $k = \pm 1$ alias directly to DC ($f = 0\text{ Hz}$) with weight $10(5 + 5) = 100$.
- The $5\text{ Hz}$ components fall on interval boundaries $f = \pm 5\text{ Hz}$ with weight $10(2.5 + 2.5) = 50$.
- The $2.5\text{ Hz}$ tone remains at $f = \pm 2.5\text{ Hz}$ with weight $10(7.5) = 75$.

Thus, across the fundamental Nyquist interval:
$$X_s(f) = 100\delta(f) + 75[\delta(f - 2.5) + \delta(f + 2.5)] + 50[\delta(f - 5) + \delta(f + 5)]$$

**Reconstruction Assessment:**
Maximum frequency component $f_m = 10\text{ Hz}$ requires a Nyquist rate of $f_s \ge 2f_m = 20\text{ Hz}$. Sampling at $f_s = 10\text{ Hz}$ violates this condition. The $10\text{ Hz}$ oscillation aliases entirely into a DC offset of $10$. A low-pass filter over $[-5, 5]\text{ Hz}$ outputs a constant offset rather than the original sinusoid. You cannot reconstruct $x(t)$.

![[attachments/sampling_10hz_aliasing.png]]
*Fig. 4. Severe aliasing at $f_s = 10\text{ Hz}$ in the time domain and folded spectral weights.*

---

#### (b) Signal Reconstruction at $f_s = 20\text{ Hz}$
At $f_s = 20\text{ Hz}$, the sampling rate matches the exact Nyquist rate ($2f_m = 20\text{ Hz}$).
The lower frequency tones ($2.5\text{ Hz}$ and $5\text{ Hz}$) lie strictly within the interior of the alias-free zone $(-10, 10)\text{ Hz}$.

For the boundary tone $x_1(t) = 10\cos(20\pi t)$ at $f_m = 10\text{ Hz}$:
$$x_1[n] = 10\cos\left(20\pi \frac{n}{20}\right) = 10\cos(\pi n) = 10(-1)^n$$

Because the initial phase is zero, the sample points capture the alternating positive and negative peaks ($+10, -10$) rather than zero-crossings. In the frequency domain, adjacent spectral replicas touch at $f = \pm 10\text{ Hz}$ and sum constructively to weight $20(5 + 5) = 200$. An ideal reconstruction filter with boundary gain $H(\pm 10\text{ Hz}) = \frac{1}{2f_s} = \frac{1}{40}$ recovers $X(f)$ and reconstructs $x(t)$ without information loss.

![[attachments/sampling_20hz_reconstruction.png]]
*Fig. 5. Nyquist boundary sampling at $f_s = 20\text{ Hz}$ in the time domain and alias-free spectral weights.*
