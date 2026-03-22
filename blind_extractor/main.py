from blind_extractor.config_loader import load_config
from blind_extractor.request_engine import RequestEngine
from blind_extractor.inference_engine import InferenceEngine
from blind_extractor.extractor import Extractor
from blind_extractor.logger import setup_logger


def main():
    config = load_config("config.yaml")

    logger = setup_logger(
        config["logging"]["text_log"],
        config["logging"]["json_log"]
    )

    requester = RequestEngine(config)
    inference = InferenceEngine(requester, config, logger)
    extractor = Extractor(inference, config, logger)

    result = extractor.extract()

    print("\nFinal Result:", result)


if __name__ == "__main__":
    main()
