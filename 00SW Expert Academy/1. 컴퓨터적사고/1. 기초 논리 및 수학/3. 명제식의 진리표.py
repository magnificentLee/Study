# 1. p ∧ (q -> ~p)  = p and (if q then not p)
"""
p q | p ∧ (q -> ~p)
T T    (T AND F) F
T F    (T AND T) T
F T    (F AND T) F
F F    (F AND F) F
"""
# 2. (p ∧ ~q) -> r
"""
p q r| (p ∧ ~q) -> r
T T T  (T AND F):T  T  
T T F  (T AND F):F  T
T F T  (T AND T):T  T
T F F  (T AND T):F  F  
F T T  (F AND F):T  T 
F T F  (F AND F):F  T
F F T  (F AND T):T  T
F F F  (F AND T):F  T
"""
"""
∧ : AND
∨ : OR
→ : IF THEN(조건문)  : P가 참이면서 Q가 거짓인 경우만 거짓 
"""