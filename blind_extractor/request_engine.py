import requests
import time
import random
from dataclasses import dataclass


@dataclass
class ResponseData:
    time: float
    length: int
    text: str
    error: bool


class RequestEngine:
    def __init__(self, config):
        self.url = config["target"]["url"]
        self.injection_type = config["injection"]["type"]
        self.injection_name = config["injection"]["name"]
        self.base_value = config["injection"]["base_value"]

        self.timeout = config["network"]["timeout"]
        self.retries = config["network"]["retries"]

        self.jitter_min = config["traffic"]["jitter_min_ms"] / 1000
        self.jitter_max = config["traffic"]["jitter_max_ms"] / 1000

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})

        # Initial visit to gather cookies/session
        self.session.get(self.url)

    def _sleep(self):
        time.sleep(random.uniform(self.jitter_min, self.jitter_max))

    def send_payload(self, payload):
        for _ in range(self.retries):
            try:
                self._sleep()
                start = time.time()

                if self.injection_type == "cookie":
                    cookies = self.session.cookies.get_dict()
                    cookies[self.injection_name] = self.base_value + payload
                    r = self.session.get(self.url, cookies=cookies, timeout=self.timeout)

                elif self.injection_type == "param":
                    params = {self.injection_name: self.base_value + payload}
                    r = self.session.get(self.url, params=params, timeout=self.timeout)

                elif self.injection_type == "header":
                    headers = {self.injection_name: self.base_value + payload}
                    r = self.session.get(self.url, headers=headers, timeout=self.timeout)

                else:
                    raise Exception("Unknown injection type")

                return ResponseData(time.time() - start, len(r.text), r.text, False)

            except Exception:
                pass

        return ResponseData(0, 0, "", True)
