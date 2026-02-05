from blind_extractor.config_loader import load_config
from blind_extractor.logger import EvidenceLogger
from blind_extractor.request_engine import RequestEngine
from blind_extractor.baseline import BaselineEngine
from blind_extractor.inference_engine import InferenceEngine
from blind_extractor.extractor import Extractor

def main():
    config = load_config()

    logger = EvidenceLogger(
        config["logging"]["text_log"],
        config["logging"]["json_log"]
    )

    requester = RequestEngine(config)
    baseline_engine = BaselineEngine(requester, logger)
    baseline = baseline_engine.establish()

    inference = InferenceEngine(requester, baseline, logger)
    extractor = Extractor(inference, config)

    result = extractor.extract_string()

    logger.log({"final_result": result})
    logger.save()

    print("\nExtraction complete:", result)

if __name__ == "__main__":
    main()
