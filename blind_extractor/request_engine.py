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
        self.config = config

        self.base_url = config["target"]["url"]
        self.timeout = config["network"]["timeout"]
        self.retries = config["network"]["retries"]

        self.jitter_min = config["traffic"]["jitter_min_ms"] / 1000
        self.jitter_max = config["traffic"]["jitter_max_ms"] / 1000

        self.method = config["injection"]["method"]
        self.injection_type = config["injection"]["type"]
        self.injection_name = config["injection"]["name"]

        self.base_params = config.get("request", {}).get("params", {})
        self.base_headers = config.get("request", {}).get("headers", {})
        self.base_cookies = config.get("request", {}).get("cookies", {})

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})

    def _sleep(self):
        time.sleep(random.uniform(self.jitter_min, self.jitter_max))

    def send_payload(self, payload):
        for _ in range(self.retries):
            try:
                self._sleep()
                start = time.time()

                params = self.base_params.copy()
                headers = self.base_headers.copy()
                cookies = self.base_cookies.copy()
                data = {}

                # 🔥 Injection handling
                if self.injection_type == "param":
                    params[self.injection_name] = payload

                elif self.injection_type == "cookie":
                    cookies[self.injection_name] = payload

                elif self.injection_type == "header":
                    headers[self.injection_name] = payload

                else:
                    raise ValueError("Invalid injection type")

                # 🔥 Request execution
                if self.method == "GET":
                    r = self.session.get(
                        self.base_url,
                        params=params,
                        headers=headers,
                        cookies=cookies,
                        timeout=self.timeout
                    )
                else:
                    r = self.session.post(
                        self.base_url,
                        data=params,
                        headers=headers,
                        cookies=cookies,
                        timeout=self.timeout
                    )

                return ResponseData(
                    time.time() - start,
                    len(r.text),
                    r.text,
                    False
                )

            except Exception:
                pass

        return ResponseData(0, 0, "", True)
