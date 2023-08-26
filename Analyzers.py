import dask.dataframe as dd

class StatisticAnalyzer:
    def __init__(self) -> None:
        pass

    def load(self):
        # Load datasets in memory
        print("Loading datasets...")
        self.ddf = dd.read_csv("data/topic_results.csv")
        print("Datasets loaded!")