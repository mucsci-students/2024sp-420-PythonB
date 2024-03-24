class Error_Handler:
    @staticmethod
    def handle_error(func):
        def error_catcher(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError as e:
                print(str(e))
            except TypeError as t:
                #TODO: all the ugly error messages the CLI emits are from this.
                #can we make it nicer/more specific?
                print(str(t))
        return error_catcher
