class EsiException(Exception):
    def __init__(self, endpoint, status, args):
        message = "Endpoint '{endpoint}' returned status {status}. Parameters: {params}.".format(
            endpoint=endpoint,
            status=status,
            params=str(args)
        )

        super().__init__(message)

        self.status = status
        self.params = args
