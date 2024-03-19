class Error_Handler:
    @staticmethod
    def handle_error(func):
        def error_catcher(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(str(e))
        return error_catcher
