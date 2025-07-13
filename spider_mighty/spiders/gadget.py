import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GadgetSpider(scrapy.Spider):
    name = "gadget"
    allowed_domains = ["mightygadget.co.uk"]
    start_urls = ["https://mightygadget.co.uk/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                wait_time=10,
                wait_until=EC.presence_of_element_located((By.TAG_NAME, "article")),
                callback=self.parse
            )

    def parse(self, response):
        articles = response.css("article")

        for article in articles:
            title = article.css("h2.entry-title a::text").get()
            url = article.css("h2.entry-title a::attr(href)").get()
            summary = article.css("div.entry-summary p::text").get()

            if url:
                yield SeleniumRequest(
                    url=url,
                    wait_time=10,
                    wait_until=EC.presence_of_element_located((By.CLASS_NAME, "entry-content")),
                    callback=self.parse_article,
                    meta={
                        "title": title,
                        "url": url,
                        "summary": summary
                    }
                )

        # Handle pagination
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield SeleniumRequest(
                url=response.urljoin(next_page),
                wait_time=10,
                wait_until=EC.presence_of_element_located((By.TAG_NAME, "article")),
                callback=self.parse
            )

    def parse_article(self, response):
        title = response.meta.get("title")
        url = response.meta.get("url")
        summary = response.meta.get("summary")

        # Extract all visible text from the article
        paragraphs = response.css("div.entry-content p::text").getall()
        content = " ".join(paragraphs).strip()

        yield {
            "title": title,
            "url": url,
            "summary": summary,
            "content": content
        }
