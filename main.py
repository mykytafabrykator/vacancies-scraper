from vacancies_analysis import analysis, visualization
from vacancies_scraper import scraper


if __name__ == "__main__":
    scraper.scrape_vacancies()
    analysis.analyze_technologies()
    visualization.plot_top_technologies()
