"""concept map: collapse the same exam showing up as several certs/state licenses."""
import re
CONCEPTS = {
 'cpa': r'certified public|accountant', 'bar': r'bar exam|attorney|lawyer|multistate (essay|bar)',
 'pe_fe': r'professional engineer|engineer intern|fundamentals of engineering|principles and practice of engineering|^engineer\b|civil engineer|engineer, (civil|professional)',
 'np': r'nurse practitioner|advanced practice registered', 'rn': r'registered nurse|nurse, registered|for registered nurses',
 'lpn': r'practical nurse|nurse, licensed practical|for practical nurses', 'physician': r'physician|medical doctor|internal medicine|family medicine',
 'realestate_sales': r'real estate sal', 'realestate_broker': r'real estate broker', 'insurance_producer': r'insurance producer|insurance agent',
 'mlo': r'loan originator', 'series65': r'series 65|investment advis', 'series63': r'series 63|securities agent',
 'architect': r'architect registration|^architect\b', 'teacher': r'teacher', 'social_work': r'social work',
 'counselor': r'counselor', 'soa': r'society of actuaries', 'itil': r'\bitil\b', 'appraiser': r'apprais|national uniform licensing',
 'sonography': r'sonograph', 'vet_tech': r'veterinar\w* tech', 'behavior_analyst': r'behavior analyst', 'pilot': r'pilot|flight engineer|airmen certification',
 'occupational_therapy': r'occupational therap',
}
def concept(name):
    n = str(name).lower()
    return next((k for k, p in CONCEPTS.items() if re.search(p, n)), None)
