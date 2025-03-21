from vacancies_analysis import analysis
from vacancies_scraper import scraper


if __name__ == "__main__":
    scraper.scrape_vacancies()
    analysis.analyze_technologies()
