import re
from typing import Generator

import scrapy
from scrapy.http import Response
from w3lib.html import remove_tags


class WorkUaSpider(scrapy.Spider):
    name = "work_ua"
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/jobs-python/"]

    def parse(self, response: Response, **kwargs) -> Generator:
        for vacancy in response.css("div.card.job-link"):
            link = vacancy.css("h2 a::attr(href)").get()
            if link:
                yield response.follow(
                    url=link,
                    callback=self._parse_vacancy,
                    cb_kwargs={"listing_block": vacancy}
                )

        next_page = response.css(
            "ul.pagination.hidden-xs li.add-left-default a::attr(href)"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def _parse_vacancy(
            self,
            response: Response,
            listing_block: scrapy.Selector
    ) -> Generator:
        info = listing_block.css("h2 a::attr(title)").get().split()
        title = " ".join(info[:-5]).replace(",", "")
        post_date = " ".join(info[-3:])

        company = response.css(
            'a[title^="Робота в"] span.strong-500::text'
        ).get()
        company_link = response.urljoin(
            response.css('a[title^="Робота в"]::attr(href)').get()
        )

        salary_text = response.css(
            "span.glyphicon-hryvnia-fill + span.strong-500::text"
        ).get()
        min_salary, max_salary = self._parse_salary(salary_text)

        description_html = response.css("#job-description").get()
        clean_description = self._clean_html(description_html)

        yield {
            "link": response.url,
            "title": title,
            "post_date": post_date,
            "company": company,
            "company_link": company_link,
            "min_salary": min_salary,
            "max_salary": max_salary,
            "description": clean_description,
        }

    def _parse_salary(self, salary_text: str) -> tuple:
        if not salary_text:
            return None, None

        salary_text = salary_text.replace(" ", "").replace(" ", "")

        numbers = re.findall(r"\d+", salary_text)

        if len(numbers) == 2:
            return int(numbers[0]), int(numbers[1])
        elif len(numbers) == 1:
            return int(numbers[0]), int(numbers[0])

        return None, None

    def _clean_html(self, html_text) -> None | str:
        if not html_text:
            return None
        return remove_tags(html_text).strip()
