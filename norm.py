from loadconfs import initConf
from logger import initLogger
from mongodao import initMongoDAO
import os

#initialize app.conf & user.conf
try:
    config = initConf()
except Exception as error:
    template = os.path.basename(__file__)+": Unable to load configuration due to {0}. Arguments:{1!r}. Exiting.."
    message = template.format(type(error).__name__, error.args)
    print(message)
    exit()

#initialize logger
try:
    log = initLogger(config)
    log.writeInfo(os.path.basename(__file__)+": logger initialized..")
except Exception as error:
    template = os.path.basename(__file__)+": Unable to initialze logger due to {0}. Arguments:{1!r}. Exiting.."
    message = template.format(type(error).__name__, error.args)
    print(message)
    exit()

#initialise the mongo connection
try:
    mongoDAO = initMongoDAO(log, config)
except Exception as error:
    template = "Unable to connect to mongoDb due to {0}. Arguments:{1!r}. Exiting.."
    message = template.format(type(error).__name__, error.args)
    print(message)
    exit()


#test mq connection
