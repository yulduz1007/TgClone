import logging

error = logging.Logger('error', level=40)
info = logging.Logger('success', level=20)

error_handler = logging.FileHandler('error.log', mode='a')
critical_handler = logging.FileHandler('info.log',mode='a')

# format = logging.Formatter("%(pathname)s %(lineno)d %(levelno)s %(levelname)s %(asctime)s %(message)s")
format = logging.Formatter("%(asctime)s %(message)s")

error_handler.setFormatter(format)
error_handler.setLevel(40)
critical_handler.setFormatter(format)
critical_handler.setLevel(20)

error.addHandler(error_handler)
info.addHandler(critical_handler)