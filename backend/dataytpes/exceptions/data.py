class DataRetrievalException(Exception):
    def __init__(self,  message: str, error: Exception):
        super().__init__(message)
        self.raw_errors = error

    def get_raw_error(self):
        return self.raw_errors
