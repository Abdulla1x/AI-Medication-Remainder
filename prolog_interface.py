from pyswip import Prolog

prolog = Prolog()
prolog.consult("med_rules.pl")

def check_interaction(med1, med2):
    query = f"has_interaction({med1.lower()}, {med2.lower()})"
    return bool(list(prolog.query(query)))

def check_long_term_risk(med_name, duration_days):
    query = f"long_term_risk({med_name.lower()}, {duration_days})"
    return bool(list(prolog.query(query)))