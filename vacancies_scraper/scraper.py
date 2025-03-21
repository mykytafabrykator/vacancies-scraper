import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from vacancies_scraper.spiders.dou import DouSpider
from vacancies_scraper.spiders.work_ua import WorkUaSpider

from config import SCRAPING_OUTPUT_FILE


os.environ.setdefault(
    "SCRAPY_SETTINGS_MODULE", "vacancies_scraper.settings"
)


def scrape_vacancies(platform: str = "dou", position: str = "Python"):
    print("\n[INFO] Scraping started!\n")

    if os.path.exists(SCRAPING_OUTPUT_FILE):
        try:
            os.remove(SCRAPING_OUTPUT_FILE)
        except OSError as e:
            print(f"[ERROR] Deleting {SCRAPING_OUTPUT_FILE}: {e}")
            exit(1)

    process = CrawlerProcess(get_project_settings())

    try:
        if platform == "workua":
            WorkUaSpider.update_start_urls(position)
            process.crawl(WorkUaSpider)
        else:
            DouSpider.update_start_urls(position)
            process.crawl(DouSpider)
        process.start()
    except Exception as e:
        print(f"[ERROR] {e}")
        exit(1)

    print("\n[INFO] Scraping finished!\n")


if __name__ == "__main__":
    scrape_vacancies()
