# imports

from TaxiFareModel.data import get_data, clean_data
from TaxiFareModel.utils import compute_rmse
from sklearn.model_selection import train_test_split
from TaxiFareModel.pipeline import get_pipeline


class Trainer():
    def __init__(self, X, y):
        """
            X: pandas DataFrame
            y: pandas Series
        """
        # df = get_data(nrows=nrows)
        # df = clean_data(df)
        # y = df.pop('fare_amount')
        # X = df
        # self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X, y, test_size=test_size)
        self.X = X
        self.y = y
        self.pipeline=None

    def set_pipeline(self):
        """defines the pipeline as a class attribute"""
        self.pipeline = get_pipeline()

    def run(self):
        """set and train the pipeline"""
        self.set_pipeline()
        self.pipeline.fit(self.X, self.y)

    def evaluate(self, X_test, y_test):
        """evaluates the pipeline on df_test and return the RMSE"""
        self.y_pred = self.pipeline.predict(X_test)
        return compute_rmse(self.y_pred, y_test)


if __name__ == "__main__":
    # get data
    # clean data
    # set X and y
    # hold out
    # train
    # evaluate
    print('TODO')
