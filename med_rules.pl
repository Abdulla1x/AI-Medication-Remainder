% Rules for medication interaction
interacts(paracetamol, ibuprofen).
interacts(aspirin, ibuprofen).
safe(paracetamol).
safe(vitaminc).

% Checking if two medications interact
has_interaction(Med1, Med2) :- interacts(Med1, Med2).
has_interaction(Med1, Med2) :- interacts(Med2, Med1).

% Warn if medication duration is long
long_term_risk(paracetamol, Duration) :- Duration > 10.


