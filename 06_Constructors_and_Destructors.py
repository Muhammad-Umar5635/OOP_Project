class Logger:
    def __init__(self):
        print("Logger: Object has been created.")

    def __del__(self):
        print("Logger: Object is being destroyed.")
log1 = Logger()
del Logger
