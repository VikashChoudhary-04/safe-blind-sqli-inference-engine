import statistics

class BaselineEngine:
    def __init__(self, requester, logger):
        self.req = requester
        self.logger = logger

    def establish(self, samples=10):
        times = []
        lengths = []

        for _ in range(samples):
            r = self.req.send_payload(self.req.base)
            times.append(r.time)
            lengths.append(r.length)

        self.avg_time = statistics.mean(times)
        self.std_time = statistics.stdev(times)
        self.avg_length = statistics.mean(lengths)

        self.logger.log({"baseline_time": self.avg_time})
        return self.avg_time, self.std_time, self.avg_length
