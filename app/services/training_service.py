from ml.train import train_models


class TrainingService:

    @staticmethod
    def train(csv_path: str):

        return train_models(csv_path)