# The Solo Online Work Playbook: No Sales, No Clients, No Interviews
**Philosophy:** Strictly task-based work. You log in, claim a task from a queue, complete it, and get paid.
**The Goal:** Use AI to maximize hourly rate (speed) or use strict human logic where AI is banned.

---

## Tier 1: EXTREME AI Boost (10x Speed)
*These tasks allow you to let AI do the "heavy lifting." Your job is simply to be the Quality Assurance (QA) manager.*

### 1. Transcription & Captioning
*   **Platforms:** Rev, TranscribeMe, GoTranscript, Scribie.
*   **The Task:** Listen to audio files (interviews, legal depositions, lectures) and type them out verbatim.
*   **Typical Pay:** \$0.30 - \$1.10 per audio minute (Rev). Beginners often earn \$2 - \$5/hr initially; skilled text-expanders/AI-users can hit \$15 - \$20/hr+.
*   **The AI Strategy:** Never type from scratch. Download the audio file and run it through **OpenAI Whisper** (free/open source) or **Otter.ai**.
*   **The Workflow:**
    1.  Download Job Audio.
    2.  Run through Whisper (Model: `large-v3`).
    3.  Paste text into the platform editor.
    4.  **Crucial Step:** Listen at 2x speed and fix the 5-10% errors (usually proper nouns or overlapping voices).
*   **Result:** A 60-minute file takes 15 minutes of work instead of 3 hours.

### 2. Translation & Post-Editing (PEMT)
*   **Platforms:** Gengo, Unbabel, Stepes, TextMaster.
*   **The Task:** Translating business documents, emails, or product descriptions from one language to another.
*   **Typical Pay:** \$0.03 - \$0.08 per word (Gengo). Hourly efficiency equivalent: \$12 - \$25/hr depending on approval speed.
*   **The AI Strategy:** Use **DeepL Pro** or **GPT-4o**.
    *   DeepL is superior for natural phrasing.
    *   GPT-4o is superior for understanding context and slang.
*   **The Workflow:** Feed the source text into the AI. Take the output and manually "humanize" it (fix grammar stiffness).
*   **⚠️ Warning:** Do not use this if you do not speak the target language. You need to be able to spot when the AI makes a critical error.

---

## Tier 2: HIGH AI Boost (Data & Parsing)
*These tasks require solving "puzzles" or extracting data. AI is better at this than humans.*

### 3. Micro-Tasks & Receipt Processing
*   **Platforms:** Amazon Mechanical Turk (MTurk), Clickworker, Microworkers.
*   **The Task:** "Extract address from this receipt," "Find the LinkedIn URL for this CEO," or "Copy text from this business card."
*   **Typical Pay:** Highly variable. \$2 - \$6/hr avg; "Super Users" with scripts can hit \$10 - \$15/hr. Pay per task is often cents (\$0.05 - \$0.50).
*   **The AI Strategy:**
    *   **Vision Tools:** Use **GPT-4o Vision** or standard OCR tools to rip text from images instantly.
    *   **Research:** Use **Perplexity.ai** to find business URLs/Emails faster than Google searching manually.
*   **Automation (Advanced):** Use **n8n** or **Python** scripts to scrape the job boards for "High Pay" tasks so you can accept them before others do.

### 4. Usability Testing (Written Portions)
*   **Platforms:** UserTesting, IntelliZoom, Userlytics.
*   **The Task:** Record your screen/voice while testing a website, then answer written survey questions at the end.
*   **Typical Pay:** \$10 per 20-min test (\$30/hr). Moderated interviews pay \$30 - \$60/hr.
*   **The AI Strategy:** You cannot fake the video part (you must speak). However, for the written summary questions ("What were 3 things you liked?"), speak your thoughts into a voice-note app, let AI summarize it, and paste the clean text into the survey box.
*   **Benefit:** Saves you from typing out long feedback forms after talking for 20 minutes.

---

## Tier 3: MODERATE AI Boost (Ideation & Structure)
*Use AI to generate ideas or vocabulary, but write the final sentences yourself to avoid "Robotic" detection.*

### 5. Reviewing & Naming Contests
*   **Platforms:** Slicethepie (Music/Fashion), Squadhelp (Naming).
*   **The Task:** Write a review for a song/commercial or suggest a name for a new brand.
*   **Typical Pay:** Slicethepie is low (\$0.03 - \$0.20 per review, ~\$2/hr). Squadhelp is contest-based (Winner takes \$100 - \$300), high risk/high reward.
*   **The AI Strategy:**
    *   *Music:* "Give me 10 adjectives to describe a moody, upbeat jazz track with trumpet solos." (Use these words to write your own review).
    *   *Naming:* "Generate 50 catchy names for a vegan soap company that uses the word 'Green'."
*   **⚠️ Risk:** These sites use "Perplexity Detection." If you copy-paste ChatGPT directly, you will be banned. Use the AI for *inspiration*, not creation.

---

## Tier 4: LOW / ZERO AI Boost (The Danger Zone)
*High-paying, stable work that strictly bans AI. These platforms pay you specifically because they need HUMAN logic.*

### 6. Search Engine Evaluation
*   **Platforms:** Appen, Telus International, WeLocalize.
*   **The Task:** Rate Google search results based on "Relevance" and "Utility" using complex, 150+ page guideline books.
*   **Typical Pay:** \$12 - \$15/hr (US). Steady part-time hours (10-20 hrs/week).
*   **Why AI Fails:** LLMs often hallucinate regarding "User Intent." (e.g., If a user types "Apple," do they mean the fruit or the iPhone? The guidelines have specific rules for this that AI often misses).
*   **The Only Boost:** Use AI to summarize the **Guidelines** (PDFs) so you can "Ctrl+F" to find rules faster during the qualification exam.

### 7. AI Training & Annotation (The "Gold Standard")
*   **Platforms:** DataAnnotation.tech, Remotasks (Outlier), RWS.
*   **The Task:** Chatting with chatbots, correcting code, writing creative stories, or fact-checking AI responses.
*   **Typical Pay:** \$20 - \$25/hr for core work. Coding/Expert domains pay \$30 - \$50+/hr.
*   **The Trap:** You are the teacher. If you use ChatGPT to do the work, you are feeding "AI data back into AI," causing **Model Collapse**.
*   **Consequence:** These platforms have the most sophisticated anti-AI detection in the world. Using AI here results in an **immediate, permanent ban**.
*   **Strategy:** This is the highest-paying tier (\$20-\$40/hr). Do the work manually. It is worth it.

---

## Expanded Technical Guide: Automation Tools

If you are technically inclined, here is how to build your "stack" for these platforms:

| Strategy | Tools Needed | Best Used For | Risk Level |
| :--- | :--- | :--- | :--- |
| **The "Whisper" Method** | OpenAI Whisper (Local install via Python) or MacWhisper | **Transcription:** Rev, TranscribeMe, GoTranscript. | 🟢 **Safe** (As long as you proofread the output). |
| **The "Vision" Solver** | GPT-4o Vision, Tesseract OCR | **Data Entry:** MTurk Receipt transcription. | 🟢 **Safe** (High accuracy, barely detectable). |
| **The "Polisher"** | DeepL, Grammarly | **Translation:** Gengo, Unbabel. | 🟢 **Safe** (Used for smoothing, not generating). |
| **The "Monitor" Bot** | Python (Selenium), n8n, RSS Feeds | **Job Sniping:** Catching tasks on Upwork/MTurk before others. | 🟡 **Gray Area** (Platforms hate bots, but you are just 'watching'). |
| **The "Clicker" Bot** | AutoHotKey, Puppeteer | **SEO Tasks:** SproutGigs, visiting sites automatically. | 🔴 **High Risk** (Likely Ban. Only for "burner" accounts). |

## Summary of Rules for Survival
1.  **Don't be greedy:** If a task takes a human 10 minutes, and you submit it in 30 seconds using AI, you will be flagged for "impossible speed." Always use a timer to simulate human work speed.
2.  **Human in the Loop:** Never fully automate. AI is 90% accurate; the missing 10% is why they are hiring humans. If you leave in AI hallucinations, you lose the account.
3.  **Read the TOS:** Know which category you are in. Using AI on **Rev** is usually fine (they just want the text). Using AI on **DataAnnotation** is fatal.
