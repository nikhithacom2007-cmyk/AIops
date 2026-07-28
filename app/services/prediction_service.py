from ml.predict import predict


class PredictionService:

    @staticmethod
    def predict_customer(data: dict):

        return predict(data)