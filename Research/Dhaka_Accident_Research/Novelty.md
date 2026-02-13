- “We propose an NLP-based audit of police-reported road traffic crashes in Bangladesh, comparing narrative ‘Incident Descriptions’ with checkbox ‘Cause’ fields in a 2007–2024 multi-source dataset. Unlike existing studies that use narratives to improve coding of death or injury intent in clinical or violent-death systems, our primary aim is to quantify and characterize inconsistencies between police narratives and cause checkboxes in a low- and middle-income country traffic setting. This allows us to infer systematic patterns in under-reporting, misclassification, and laziness or strategic bias in police cause coding.”

1. **Methodological twist you can add**  
    For stronger novelty, don’t just “train text classifier from narrative and compare to  Cause column”. Add at least one of:
    
    - Use **Natural Language Inference (NLI)** or contradiction detection to see if the narrative _entails_ or _contradicts_ the checkbox cause.[](https://pmc.ncbi.nlm.nih.gov/articles/PMC12582947/)​
        
    - Model **multi-source conflicts**: ARI vs BRTA vs DMP narratives/check boxes where available, as an extra layer of inconsistency.​
        
    - Analyze **temporal drift**: did inconsistency rates change after policy changes, law amendments, or big safety campaigns?
        
    - Do **bias analysis**: Are “lazy/false” checkboxes more common in certain divisions, police stations, night shifts, or when VIP vehicles are involved?
2. **Explicit “Narrative vs Checkbox” conflict as the _main problem_**
    
    - Many existing papers use narrative text to improve classification, and they observe coding errors as a side-effect.[](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413428/)
        
    - You can make the **primary research question**: “How often and in what patterns do police ‘Cause’ checkboxes disagree with narrative descriptions, and what does this imply about data quality and policy conclusions in Bangladesh road safety?”
        
    - That focus on _audit of police behaviour / reporting quality_ in traffic crashes is not obviously done yet.