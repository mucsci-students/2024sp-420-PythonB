# Zhang: in your file, include:
# from Models.errorHandler import ErrorHandler
# with @ErrorHandler.handle_error sitting right on top of each method
class ErrorHandler:
    @staticmethod
    def handle_error(func):
        def error_catcher(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"Error: {e}")
        return error_catcher
