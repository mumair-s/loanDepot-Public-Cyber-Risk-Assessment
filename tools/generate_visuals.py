#!/usr/bin/env python3
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
VISUALS = BASE / "visuals"

def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def build_risk_matrix():
    risks = read_csv("risk-register.csv")
    matrix = np.array([[l * i for i in range(1, 6)] for l in range(1, 6)])

    fig, ax = plt.subplots(figsize=(8, 6))
    image = ax.imshow(matrix, origin="lower", extent=[0.5, 5.5, 0.5, 5.5], aspect="auto")
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impact")
    ax.set_ylabel("Likelihood")
    ax.set_title("loanDepot Public-Source Risk Matrix")

    for likelihood in range(1, 6):
        for impact in range(1, 6):
            ax.text(impact, likelihood, str(likelihood * impact),
                    ha="center", va="center", fontsize=9)

    positions = {}
    for risk in risks:
        key = (int(risk["Impact"]), int(risk["Likelihood"]))
        positions.setdefault(key, []).append(risk["Risk ID"])

    for (impact, likelihood), ids in positions.items():
        ax.text(impact, likelihood - 0.30, ", ".join(ids),
                ha="center", va="center", fontsize=7, fontweight="bold")

    fig.colorbar(image, ax=ax, label="Risk Score")
    fig.tight_layout()
    fig.savefig(VISUALS / "risk-matrix.png", dpi=180, metadata={"Software": None})
    plt.close(fig)

def build_timeline():
    rows = read_csv("incident-timeline.csv")
    labels = [
        ("2024-01-03", "Unauthorized access\\nwindow begins"),
        ("2024-01-04", "Incident\\nidentified"),
        ("2024-01-05", "Access window\\nends"),
        ("2024-01-08", "Initial SEC disclosure:\\naccess, encryption,\\nsystem shutdowns"),
        ("2024-01-22", "Restoration update:\\norigination, servicing,\\ncustomer portals"),
        ("2024-02-23", "Consumer breach notice:\\nsensitive data categories"),
        ("2024-02-27", "Incident contained;\\n~16.9M notifications;\\nfinancial/litigation update"),
        ("2025-03-12", "2024 Form 10-K:\\n$24.6M net incident expense"),
        ("2026-03-12", "2025 Form 10-K:\\n$1.8M additional expense"),
    ]

    fig, ax = plt.subplots(figsize=(13, 6))
    xs = list(range(len(labels)))
    ax.scatter(xs, [0] * len(xs), s=55)

    for i, (date, event) in enumerate(labels):
        y = 0.72 if i % 2 == 0 else -0.72
        ax.annotate(
            f"{date}\\n{event}",
            xy=(i, 0),
            xytext=(i, y),
            ha="center",
            va="bottom" if y > 0 else "top",
            fontsize=8,
            arrowprops={"arrowstyle": "-", "lw": 0.8},
        )

    ax.set_xlim(-0.5, len(xs) - 0.5)
    ax.set_ylim(-1.55, 1.55)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.axhline(0, linewidth=1)
    ax.set_title(
        "loanDepot Cyber Incident — Publicly Reported Timeline\\n"
        "(Event spacing is chronological, not proportional to elapsed time)"
    )
    for spine in ["left", "right", "top", "bottom"]:
        ax.spines[spine].set_visible(False)

    fig.tight_layout()
    fig.savefig(VISUALS / "incident-timeline.png", dpi=180, bbox_inches="tight", metadata={"Software": None})
    plt.close(fig)

def build_expense_chart():
    years = ["2024", "2025"]
    expenses = [24.6, 1.8]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(years, expenses)
    ax.set_ylabel("USD millions")
    ax.set_title("Reported Cybersecurity-Incident Expenses")
    for bar, value in zip(bars, expenses):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
                f"${value:.1f}M", ha="center", va="bottom")
    ax.text(0.5, -0.20,
            "2024 amount was reported net of $35.0M insurance recoveries;\n"
            "2025 amount is the separately reported fiscal-2025 incident expense.",
            ha="center", va="top", transform=ax.transAxes, fontsize=8)
    fig.tight_layout()
    fig.savefig(VISUALS / "cyber-expenses.png", dpi=180, bbox_inches="tight", metadata={"Software": None})
    plt.close(fig)

if __name__ == "__main__":
    VISUALS.mkdir(exist_ok=True)
    build_risk_matrix()
    build_timeline()
    build_expense_chart()
    print("Generated risk-matrix.png, incident-timeline.png, and cyber-expenses.png")
