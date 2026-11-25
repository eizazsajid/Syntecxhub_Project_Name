"""
Project 2: Rule-Based Expert System
Syntecxhub AI Internship - Week 1 Task

- Chhota rule engine: if-then rules + facts base
- User symptoms (facts) deta hai
- Forward chaining se conclusions infer karta hai
- Multi-step inference supported (ek rule ka conclusion,
  doosre rule ki condition ban sakta hai)
- Inference steps ka log dikhata hai taake reasoning path nazar aaye
"""

# ---------------- Rules ----------------
# Har rule: {"if": [conditions], "then": conclusion, "advice": ...}
# Conditions = symptoms ya pehle se nikle hue conclusions
RULES = [
    {
        "if": ["fever", "cough"],
        "then": "flu",
        "advice": "Flu lagta hai: aaram karo, pani zyada piyo.",
    },
    {
        "if": ["fever", "rash"],
        "then": "measles",
        "advice": "Measles ho sakta hai: foran doctor se milo.",
    },
    {
        "if": ["sore_throat", "fever"],
        "then": "throat_infection",
        "advice": "Gale ka infection lagta hai: garam pani se gargle karo.",
    },
    {
        "if": ["headache", "fever"],
        "then": "viral_fever",
        "advice": "Viral fever lagta hai: aaram karo aur bukhar check karte raho.",
    },
    {
        "if": ["cough", "breathing_difficulty"],
        "then": "asthma_risk",
        "advice": "Saans ki takleef hai: doctor se zaroor milo.",
    },
    # --- Chained rules (multi-step inference) ---
    # In rules ki condition ek conclusion hai, is liye ye
    # tabhi chalenge jab pehla rule pehle chal chuka ho.
    {
        "if": ["flu"],
        "then": "needs_rest",
        "advice": "Flu ki wajah se 2-3 din ka mukammal aaram chahiye.",
    },
    {
        "if": ["measles"],
        "then": "needs_doctor",
        "advice": "Measles serious ho sakta hai: aaj hi doctor ko dikhao.",
    },
    {
        "if": ["needs_rest", "viral_fever"],
        "then": "needs_checkup",
        "advice": "Bukhar aur thakan barqarar hai to checkup karwao.",
    },
]

# User ko dikhane ke liye symptoms ki list
SYMPTOMS = [
    "fever", "cough", "rash", "sore_throat",
    "headache", "breathing_difficulty",
]


def forward_chain(facts):
    """
    Forward chaining: facts se shuru karo, rules tab tak lagao
    jab tak koi naya conclusion na nikle.
    Returns: (all_facts, inference_log)
    """
    known = set(facts)
    log = []
    fired = set()  # kaun se rules chal chuke

    changed = True
    while changed:
        changed = False
        for i, rule in enumerate(RULES):
            if i in fired:
                continue
            # Rule tab chalta hai jab uski saari conditions known hon
            if all(cond in known for cond in rule["if"]):
                fired.add(i)
                conclusion = rule["then"]
                if conclusion not in known:
                    known.add(conclusion)
                    changed = True
                log.append(
                    f"Rule {i + 1}: IF {' + '.join(rule['if'])} "
                    f"THEN {conclusion}  ->  {rule['advice']}"
                )
    return known, log


def main():
    print("=== Rule-Based Expert System (Health Advisor) ===\n")
    print("Available symptoms:")
    print(", ".join(SYMPTOMS))
    print("\nApne symptoms comma se likho, masalan: fever, cough")
    user_input = input("Symptoms: ").strip().lower()

    facts = [s.strip().replace(" ", "_") for s in user_input.split(",") if s.strip()]
    unknown = [f for f in facts if f not in SYMPTOMS]
    facts = [f for f in facts if f in SYMPTOMS]

    if unknown:
        print(f"\nNote: ye symptoms system nahi janta (ignore kiye): {', '.join(unknown)}")
    if not facts:
        print("\nKoi valid symptom nahi diya. Dobara try karo.")
        return

    print(f"\nFacts (tumhare symptoms): {', '.join(facts)}")
    known, log = forward_chain(facts)

    print("\n--- Inference Steps (reasoning path) ---")
    if log:
        for step in log:
            print(" *", step)
    else:
        print(" Koi rule match nahi hua.")

    conclusions = [k for k in known if k not in facts]
    print("\n--- Final Conclusions ---")
    if conclusions:
        for c in conclusions:
            print(" -", c)
    else:
        print(" Koi conclusion nahi nikla. Symptoms badal kar dobara try karo.")


if __name__ == "__main__":
    main()
