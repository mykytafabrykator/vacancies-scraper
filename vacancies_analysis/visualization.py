import pandas as pd
import matplotlib.pyplot as plt

from config import ANALYSIS_OUTPUT_FILE, ANALYSIS_RATING_IMAGE

def plot_top_technologies(top_n: int = 20):
    df = pd.read_csv(ANALYSIS_OUTPUT_FILE)
    top_tech = df.sort_values(by="Count", ascending=False).head(top_n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_tech["Technology"], top_tech["Count"], color="cornflowerblue")
    plt.title("Top technologies in vacancies", fontsize=14)
    plt.xlabel("Technology")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()

    plt.savefig(ANALYSIS_RATING_IMAGE)
    plt.close()

    print(f"Image saved: {ANALYSIS_RATING_IMAGE.resolve()}")

# 📌 Використання:
if __name__ == "__main__":
    plot_top_technologies()
