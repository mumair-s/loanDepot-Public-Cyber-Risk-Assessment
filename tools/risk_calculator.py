#!/usr/bin/env python3

def risk_rating(score: int) -> str:
    if not 1 <= score <= 25:
        raise ValueError("Risk score must be between 1 and 25.")
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Medium"
    if score <= 15:
        return "High"
    return "Critical"

def get_score(label: str) -> int:
    while True:
        try:
            value = int(input(f"{label} (1-5): ").strip())
            if 1 <= value <= 5:
                return value
        except ValueError:
            pass
        print("Enter a whole number from 1 to 5.")

def main():
    print("5x5 Cybersecurity Risk Calculator")
    print("-" * 33)
    likelihood = get_score("Likelihood")
    impact = get_score("Impact")
    score = likelihood * impact
    print(f"\nRisk score: {score}")
    print(f"Risk rating: {risk_rating(score)}")

if __name__ == "__main__":
    main()
