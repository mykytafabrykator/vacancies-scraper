import time
import scrapy
from scrapy.http import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from config import DOU_URL


class DouSpider(scrapy.Spider):
    name = "dou"
    allowed_domains = ["dou.ua"]
    start_urls = [DOU_URL]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        chrome_options = Options()
        chrome_options.add_argument("--headless")  # приховано
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options,
        )

    def parse(self, response: Response, *args):
        self.driver.get(self.start_urls[0])

        while True:
            try:
                load_more_btn = WebDriverWait(self.driver, 3).until(
                    ec.element_to_be_clickable(
                        (By.XPATH, "//a[contains(text(),'Більше вакансій')]")
                    )
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);", load_more_btn
                )
                time.sleep(1)
                load_more_btn.click()
            except Exception as e:
                print(f"No more 'Більше вакансій' button. {e}")
                break

        jobs = self.driver.find_elements(By.CSS_SELECTOR, ".l-vacancy")

        for job in jobs:
            try:
                title = job.find_element(By.CSS_SELECTOR, "a.vt").text
                company_name = job.find_element(
                    By.CSS_SELECTOR, "a.company"
                ).text
                job_url = job.find_element(
                    By.CSS_SELECTOR, "a.vt"
                ).get_attribute("href")

                yield response.follow(
                    job_url,
                    callback=self.parse_job_details,
                    meta={"title": title, "company_name": company_name},
                )
            except Exception as e:
                print(f"[ERROR] while parsing list item: {e}")

    def parse_job_details(self, response: Response):
        title = response.meta.get("title", "No title")
        company_name = response.meta.get("company_name", "No company")

        description = response.css(
            "div.b-typo.vacancy-section p::text"
        ).getall()
        ul_items = response.css(
            "div.b-typo.vacancy-section ul li::text"
        ).getall()
        full_description = " ".join(description + ul_items).strip()

        location = response.css("span.place.bi.bi-geo-alt-fill::text").get()
        date_posted = response.css("div.date::text").get()
        if date_posted:
            date_posted = date_posted.strip()

        yield {
            "title": title,
            "company_name": company_name,
            "description": full_description,
            "location": location,
            "date_posted": date_posted,
            "url": response.url,
        }

    def closed(self, reason):
        self.driver.quit()

    @classmethod
    def update_start_urls(cls, position):
        cls.start_urls = [(cls.start_urls[0] + position)]
