# Overview
- Purpose:  Review draft paper.
- Author: Chris Cirelli
- Date: 10-29-2023

---
### Paper
- Title: Demographics, Financials, and Fairness: How Disparities in  Predictive Models Impact Patients in Substance Use
Treatment for Length-of-Stay?
- Author: Urug,

### Questions
1. Were both HCUP and TEDS-D files provided?
2. If the data was concatenated we should probably start with the raw files pre-processing.
3. Why was the dataset limited to three states?
4. How does the python package fairlearn define unfairness and which features should be considered?
5. Does the report provide reference to any prior research for SUD patient financial condition relative to other
patient types?
6. Do we have knowledge of ML models being used in the medical field and for operational purposes?
7. Who defines what constitutes a protected variable?  Federal and state laws?
8. Is there a common / accepted definition of fairness for for ML models?

### Key Topics
1. Check LOS for outliers.  Validate dates.
2. Dataset: TEDS-D: Treatment Episode Data Set - Discharges
3. Dataset: HCUP: Healthcare Cost and Utilization Project, Filtered for SUD Discharge Data
4. Dataset-Scope: Limited to three US States: Arizona, Florida, and Maryland.
5. Study Objective: "investigate the fairness of ML models developed for  prediction of LOS in SUD treatment to identify
social groups that may be adversely impacted from the model predictions."

### References
- Substance Abuse and Mental Health Services Administration
  - url: https://www.samhsa.gov/
- TEDS-D: Treatment Episode Data Set - Discharges
  - provides discharge data from detoxification, ambulatory, and residential SUD treatment programs
  - url: https://www.samhsa.gov/data/data-we-collect/teds-treatment-episode-data-set
- Healthcare Cost Utilization Project (HCUP) State In-Patient Databases (SID)
  - url:

### Notes


**Abstract**
- ML models used to predict when to discharge patients.
- Social biases can be encoded into model(s).
- SUD: substance use disorder.
- Consequences: financial burden.
- Model Target: Length of Stay (LOS)
- Unfairness Features: race, age, region, and primary payer.

**Introduction**
- Sources of unfairness:
  - data is not fully representative of all groups (eg unbalanced)
  - model development lifecycle
  - healthcare system inherent biases.
- Critical Decision
  - how long a patient needs to stay in a facility for observation and treatment (LOS)
  - late discharge can lead to financial burden.
  - late discharge particularly import for SUD may exacerbate financial condition.
- SUD
  - "Those diagnosed with a SUD are often either treated as in-patients within hospitals, and/or in SUD treatment
programs that can range from ambulatory to intensive residential programs"
- Study Structure
  - Develop ML models to predict LOS for SUD patients.
  - Select two best performing models.
  - Assess models for fairness.
  - Assess performance of models for protected variables (race, age, and primary payer), and
  - how fair they perform for each group within a variable (i.e. equally well predictions).
  - finish with discussion of fairness/accuracy tradeoff.

**Background Literature**
- ...continue
