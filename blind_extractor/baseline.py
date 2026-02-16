import statistics


class BaselineEngine:
    def __init__(self, requester, logger):
        self.req = requester
        self.logger = logger

    def establish(self):
        print("Establishing baseline...")

        times = []
        lengths = []

        for _ in range(5):
            r = self.req.send_payload("")
            times.append(r.time)
            lengths.append(r.length)

        avg_time = statistics.mean(times)
        std_dev = statistics.stdev(times) if len(times) > 1 else 0
        avg_len = statistics.mean(lengths)

        print("Baseline established")
        return avg_time, std_dev, avg_len
