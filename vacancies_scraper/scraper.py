import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from vacancies_scraper.spiders.work_ua import WorkUaSpider

from config import SCRAPING_OUTPUT_FILE


os.environ.setdefault(
    "SCRAPY_SETTINGS_MODULE", "vacancies_scraper.settings"
)


def scrape_vacancies():
    print("\n[INFO] Scraping started!\n")

    if os.path.exists(SCRAPING_OUTPUT_FILE):
        try:
            os.remove(SCRAPING_OUTPUT_FILE)
        except OSError as e:
            print(f"[ERROR] Deleting {SCRAPING_OUTPUT_FILE}: {e}")
            exit(1)

    process = CrawlerProcess(get_project_settings())

    try:
        process.crawl(WorkUaSpider)
        process.start()
    except Exception as e:
        print(f"[ERROR] {e}")
        exit(1)

    print("\n[INFO] Scraping finished!\n")


if __name__ == "__main__":
    scrape_vacancies()
