# EEE 3117 — Transmitter and Digitization (PYQ)

**Syllabus:** Elements of transmitter and their functions, Transmission technologies, Concept of wireless transmission with antennas, Transmit diversity schemes, Channel state information at the transmitter, transmission delay. Digitization: Sampling and its classification, Sampling theorem, Nyquist criterion, Aliasing effect and its elimination, Quantizing, Quantization noise, Non-uniform quantization, Signal to quantization error ratio, Encoding, Line coding formats, Sample and hold circuit, Quantizer and encoder circuits.

---

### **Transmitter Elements, Antennas, Transmit Diversity, CSI & Transmission Delay**

_No questions found for this subtopic in the provided PYQ PDF._

### **Sampling Theorem, Nyquist Criterion, Aliasing & Sample-and-Hold**

1. **(p. 5, (b) — Topic-Wise PYQ, Series 21)** Demonstrate mathematically and graphically the significance of Nyquist rate in case of pulse communication system.

2. **(p. 5, (c) [2nd] — Topic-Wise PYQ, Series 21)** Briefly explain aliasing effect in signal transmission and its elimination technique.

3. **(p. 6, (d) — Topic-Wise PYQ, Series 17)** For the signal: $m(t) = 3\cos 500\times \pi + 4\sin 1000\times \pi$. Determine sampling frequency and the Nyquist sampling rate.

4. **(p. 12, Q.1. — CT-04, 20 Series, Sec A)** Mathematically and graphically demonstrate the significance of Nyquist rate in case of pulse modulation.

5. **(p. 13, Q.2. — CT-04, 20 Series, Sec B)** **[figure Involved]** The following figure shows the spectrum of a message signal with frequency $f_{max} = 1\text{ Hz}$. The signal is sampled at the rate of $f_s = 2.5 f_{max}$ and then passed through an ideal low pass filter with $|H(f) = 1|$ for $-f_{max} < f < f_{max}$. Draw the followings
   (i) Spectrum of the sampled signal
   (ii) Response of the low pass filter
   (iii) Spectrum of the signal at the output of the filter

   ![[attachments/fig_p13_q_2.png]]

6. **(p. 15, Q.8 (b) — Odd Semester Exam 2023 (20 Series))** Demonstrate mathematically and graphically the significance of the Nyquist rate in the case of the pulse communication system.
   *(Exact duplicate also on: p. 5, (b) (Topic-Wise PYQ, Series 20))*

### **Quantization, Quantization Noise, Non-Uniform Quantization & SQNR**

7. **(p. 5, Q.7(a) — Topic-Wise PYQ, Series 21)** **[figure Involved]** Suppose you are utilizing the illustrated system of the following figure to transform an analog signal into digital one. The maximum and minimum value of the analog signal is $20$ and $0$, respectively. The sampled signal is $x(n) = \{3.7, 5.6, 8.3, 11.5, 14.2, 17.4\}$. Assume mid-rise type quantizer and draw the characteristics curve and output waveform of the quantizer for this particular operation. Also mention the quantized value, quantization error, and the output data of the encoder.

   ![[attachments/fig_p05_q_7_a.png]]

8. **(p. 5, (c) — Topic-Wise PYQ, Series 21)** Briefly explain the relation between quantization level, step size and quantization error.

9. **(p. 5, Q.4 (a) — Topic-Wise PYQ, Series 18)** Determine the signal to quantization noise ratio of PCM system.

10. **(p. 5, (b) — Topic-Wise PYQ, Series 18)** With necessary diagrams, explain a technique for achieving non-uniform quantization using a uniform quantizer.

11. **(p. 6, (b) — Topic-Wise PYQ, Series 18)** Show the DPCM system achieves higher SNR compared to PCM system.

12. **(p. 6, Q.8. (a) — Topic-Wise PYQ, Series 17)** Show that the SNR of a PCM system in $(\alpha + 6n)\text{ dB}$, where the symbols have their usual meaning.

13. **(p. 6, (c) [Q.8] — Topic-Wise PYQ, Series 17)** Show the DPCM system achieve higher SNR compare to PCM system.

14. **(p. 8, Q.2 — CT-02, Sec A (Selim Sir))** A signal $m(t)$ of $\text{BW} = 4\text{ kHz}$ is transmitted using binary companded PCM with $\mu = 100$. Compare the case of $L = 64$ with two case $L = 256$ from the point of view of transmission BW and output SNR.

15. **(p. 9, Question 2 — CT-02, Sec B (Selim Sir))** Show that the noise error that is SNR in digital signal $\alpha + Cn\text{ dB}$

16. **(p. 12, Q.2. — CT-04, 20 Series, Sec A)** Draw the characteristics curve of a mid-rise type uniform quantizer and briefly explain the operation of it with numerical examples.

17. **(p. 15, Q.8 (a) — Odd Semester Exam 2023 (20 Series))** In case of PCM, SNR varies from talker to talker and remains low most of the time when uniform quantization is employed. Analyze a procedure to overcome this problem associated with PCM.
   *(Exact duplicate also on: p. 5, Q.8 (a) (Topic-Wise PYQ, Series 20))*

### **Encoding, PCM & Line Coding Formats**

18. **(p. 6, (c) — Topic-Wise PYQ, Series 18)** A TV signal (video and audio) has a bandwidth of $4.5\text{ MHz}$. The signal is sampled, quantized and binary coded to obtain a PCM signal. (i) determine the sampling rate if the signal is to be sampled at a rate $20\%$ above the Nyquist rate, (ii) if the samples are quantized into $1024$ levels, determine the number of binary pulses required to encode each sample.

19. **(p. 6, Q.5 (a) — Topic-Wise PYQ, Series 18)** Discuss the operating principle of Delta modulation.

20. **(p. 6, (c) — Topic-Wise PYQ, Series 17)** Describe in detail the PCM technique with focus on its sampling rate, and signal to quantization noise ratio.

21. **(p. 6, (b) — Topic-Wise PYQ, Series 17)** A signal $m(t)$ band limited to $3\text{ kHz}$ is sampled at a rate $30\%$ higher than the Nyquist rate. The maximum acceptable error in the sample amplitude is $0.8\%$ of the peak amplitude $m_p$. The quantized samples are binary coded. Find the minimum bandwidth of a channel.

22. **(p. 6, (b) [Digital] — Topic-Wise PYQ, Series 21)** Implement the following line coding technique to convert the digital data $01100101$ into digital signal and graphically demonstrate the output signals (i) polar RZ, (ii) bipolar NRZ.

23. **(p. 7, (b) — Topic-Wise PYQ, Series 17)** Consider the following binary sequences: (i) an alternating sequence of 1's and 0's, (ii) a long sequence of 1's followed by a long sequence of 0's, (iii) a long sequence of 1's followed by single 0 and a long sequence of 1's.
   Sketch the waveform for each of these sequences using the following methods of representing symbols 1 and 0. (i) On-off signaling, (ii) Polar signaling, (iii) Return to zero signaling, and (iv) Bipolar signaling.

24. **(p. 7, (c) — Topic-Wise PYQ, Series 17)** Explain the desirable properties of a line coder.

25. **(p. 7, Q.6. (a) — Topic-Wise PYQ, Series 15)** Construct NRZ, RZ and split-phase format for the binary data '011010'.

26. **(p. 7, (c) — Topic-Wise PYQ, Series 15)** Mention the properties of a line coder.

27. **(p. 8, Q2 — CT-04, Sec A (Selim Sir))** Manchester coding

28. **(p. 10, 2. — CT-04, Sec B (Selim Sir))** Draw Manchester data from code

29. **(p. 13, Q.1. — CT-04, 20 Series, Sec B)** Draw the block diagram of a PCM system and briefly describe the transmitter portion of the mentioned system.

30. **(p. 15, Q.8 (c) — Odd Semester Exam 2023 (20 Series))** What is meant by line coding of communication systems? Draw the unipolar RZ line-coded signal of digital data $1010011$.
   *(Exact duplicate also on: p. 7, (c) (Topic-Wise PYQ, Series 20))*
