import sys

from vacancies_analysis import analysis, visualization
from vacancies_scraper import scraper


if __name__ == "__main__":
    if (
            3 > len(sys.argv) > 5
            and ("dou" not in sys.argv or "workua" not in sys.argv)
    ):
        print(
            "\nUsage: python main.py <platform> <vacancy input>"
            "\nPlatform choices: dou, work.ua"
            "\nCheck vacancy categories at dou "
            "before scraping (ex. values: Python, Java)"
            "\nVacancy input for work.ua must be less "
            "than 2 words (ex. values: Python Developer)"
        )
        exit(1)

    platform = sys.argv[1]
    transformed_position = ("+".join(sys.argv[2:]))

    scraper.scrape_vacancies(platform, transformed_position)
    analysis.analyze_technologies()
    visualization.plot_top_technologies()
