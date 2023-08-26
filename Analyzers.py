import dask.dataframe as dd

class StatisticAnalyzer:
    def __init__(self) -> None:
        pass

    def load(self):
        # Load datasets in memory
        print("Loading datasets...")
        self.ddf = dd.read_csv("data/topic_results.csv")
        print("Datasets loaded!")

    def related_tweets(self, topic_or_sentiment: str):
        # Get related tweets
        print("Getting related tweets...")
        related_tweets = self.ddf[self.ddf[topic_or_sentiment] == tweet]
        print("Related tweets retrieved!")

        return related_tweets
