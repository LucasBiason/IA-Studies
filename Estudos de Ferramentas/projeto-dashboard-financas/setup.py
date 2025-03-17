from transaction_extractor import TransactionsExtractor
from transaction_classifier import TransactionsClassifier

if __name__ == "__main__":
    extractor = TransactionsExtractor("extratos")
    extractor.extract()
    TransactionsClassifier(extractor.df, "data/finances.csv").classify()