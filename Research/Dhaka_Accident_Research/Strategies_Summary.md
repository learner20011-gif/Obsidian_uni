# Research Strategies: Dhaka Traffic Accidents (2007–2024)

## 1. Counterfactual Policy Analysis
- **Goal:** Shift from prediction to prevention.
- **Method:** Train XGBoost on fatalities; systematically flip individual features (e.g., adding dividers) to calculate **Average Treatment Effect (ATE)**.
- **Impact:** Provides quantitative policy advice (e.g., "Dividers reduce fatality by 23%").

## 2. NLP Audit: Narrative vs. Checkbox
- **Goal:** Detect data corruption/inconsistencies in police records.
- **Method:** Use **BanglaBERT** to predict accident "Cause" from the "Incident Description" (text) and flag mismatches with structured checkboxes.
- **Impact:** Automated framework for cleaning national databases.

## 3. Metro Impact Assessment (Spatio-Temporal)
- **Goal:** Measure safety impact of new infrastructure (MRT-6).
- **Method:** **Difference-in-Differences (DiD)** analysis comparing accident rate changes within 500m of Metro lines vs. control zones (e.g., Rampura) before/after 2023.
- **Impact:** Answers critical national safety questions regarding infrastructure shifts.


