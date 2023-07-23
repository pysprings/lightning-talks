import json
import logging
import importlib.resources

import requests

from myapp.logger import init_logger


def main():
    init_logger()
    log = logging.getLogger()

    urls_text = importlib.resources.files(__package__).joinpath("urls.json").read_text()
    urls = json.loads(urls_text)

    for url in urls:
        log.info("Sending request to: %s", url)
        response = requests.get(url)
        data = response.json()
        log.info("... %s", json.dumps(data))


if __name__ == "__main__":
    main()
