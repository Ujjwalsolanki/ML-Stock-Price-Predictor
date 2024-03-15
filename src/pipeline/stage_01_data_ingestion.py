from src.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()


if __name__ == '__main__':
    try:
        obj = DataIngestion()
        obj.main()
    except Exception as e:
        raise e

