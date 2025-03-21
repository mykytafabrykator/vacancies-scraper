import csv
import os
import re
from pathlib import Path

import pandas as pd
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from config import (
    TECHNOLOGIES_TO_ANALYZE,
    SCRAPING_DATA_PATH,
    ANALYSIS_DATA_PATH,
    ANALYSIS_OUTPUT_FILE
)

nltk.download("stopwords")
nltk.download("punkt")

STOPWORDS = set(stopwords.words("english"))


def load_data(folder_path):
    return [
        row["description"]
        for file in Path(folder_path).glob("*.csv")
        for row in csv.DictReader(open(file, "r", encoding="utf-8"))
        if "description" in row and row["description"].strip()
    ]


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = word_tokenize(text)
    words = [word for word in words if word not in STOPWORDS]
    return words


def count_technologies(job_descriptions):
    word_counts = Counter()

    for desc in job_descriptions:
        words = set(preprocess_text(desc))
        word_counts.update(words)

    tech_frequencies = {
        tech: word_counts[tech.lower()]
        for tech in TECHNOLOGIES_TO_ANALYZE
        if tech.lower() in word_counts
    }
    return tech_frequencies


def save_results(counts, output_path):
    df = pd.DataFrame(counts.items(), columns=["Technology", "Count"])
    df.sort_values(by="Count", ascending=False, inplace=True)
    df.to_csv(output_path, index=False)

    last_few_dirs = os.path.normpath(output_path).split(os.sep)[-3:]
    last_few_dirs_str = os.sep.join(last_few_dirs)
    print(f"[INFO] Results saved to {last_few_dirs_str}")


def analyze_technologies():
    print("\n[INFO] Analysis started!\n")

    if not os.path.exists(SCRAPING_DATA_PATH):
        print(f"Checking data folder path: {SCRAPING_DATA_PATH}")
        print("[ERROR]: Data folder does not exist!")
        return
    else:
        print("[INFO] Data folder found!")

    if not os.path.exists(ANALYSIS_DATA_PATH):
        print(f"Checking output folder path: {ANALYSIS_DATA_PATH}")
        print("[ERROR]: Output folder does not exist! Creating it...")
        os.makedirs(ANALYSIS_DATA_PATH)
    else:
        print("[INFO] Output folder found!")

    descriptions = load_data(SCRAPING_DATA_PATH)

    tech_counts = count_technologies(descriptions)

    save_results(tech_counts, ANALYSIS_OUTPUT_FILE)

    print("\n[INFO] Analysing finished.\n")


if __name__ == "__main__":
    analyze_technologies()
