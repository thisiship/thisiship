from selenium import webdriver
import json
from datetime import datetime


class FBScraper():
    def __init__(self, event_list):
        self.baseURL = "http://facebook.com/events/"
        self.event_list = event_list
        self.scrape_datetime = datetime.now().isoformat()
        self.setUp()
        for evt in self.event_list:
            self.fetch_event_info(evt)
        self.tearDown()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def get_event_title(self):
        return self.driver.find_element_by_id("seo_h1_tag").text

    def get_event_details(self):
        return self.driver.find_element_by_css_selector("div[data-testid='event-permalink-details'] span").text

    def get_event_date(self):
        return self.driver.find_elements_by_css_selector("""
        #event_summary #event_time_info div table tr td:nth-child(2) div[content]""")[0].text

    def get_venue_info(self):
        venue_info = {}
        venue = self.driver.find_elements_by_css_selector(
            "#event_summary ul > li:nth-child(2) a[href*='facebook']")[0]
        venue_info['name'] = venue.text
        venue_info['link'] = venue.get_attribute("href")
        return venue_info

    def get_event_privacy(self):
        return self.driver.find_elements_by_css_selector(
            "span[data-testid='event_permalink_privacy']")[0].text

    def get_hosts(self):
        host_info = []
        hosts = self.driver.find_elements_by_css_selector(
            "div[data-testid='event_permalink_feature_line'] > a")
        for host in hosts:
            text = host.text
            href = host.get_attribute('href')
            host_info.append({
                "name": text,
                "link": href,
            })
        return host_info

    def fetch_event_info(self, event):
        driver = self.driver
        event_id = event["id"]
        url = f"{self.baseURL}{event_id}"
        driver.get(url)

        new_event = {}
        new_event["url"] = url
        new_event["scrape_datetime"] = self.scrape_datetime
        new_event['title'] = self.get_event_title()
        new_event['details'] = self.get_event_details()
        new_event['datetime'] = self.get_event_date()

        new_event['venue'] = self.get_venue_info()

        new_event['privacy'] = self.get_event_privacy()
        new_event['hosts'] = self.get_hosts()

        with open(f"./events/{event_id}.json", 'w') as evt_file:
            json.dump(new_event, evt_file, indent=4, sort_keys=True)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    fb_event_ids = {}
    with open('./event_list.json', 'r') as event_list:
        fb_event_ids = json.load(event_list)

    scraper = FBScraper(fb_event_ids["events"])
