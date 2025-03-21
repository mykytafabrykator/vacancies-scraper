import sys

from vacancies_analysis import analysis, visualization
from vacancies_scraper import scraper


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nUsage: python main.py <vacancy input>")
        exit(1)

    transformed_position = ("+".join(sys.argv[1:])).lower() + "/"

    scraper.scrape_vacancies(transformed_position)
    analysis.analyze_technologies()
    visualization.plot_top_technologies()
