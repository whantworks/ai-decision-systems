def decision_pipeline(signals):
    processed = normalize(signals)
    reasoning = ai_reasoning(processed)
    decision = apply_business_rules(reasoning)
    return decision
