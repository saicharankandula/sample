import logging,logging.handlers
# logger = logging.getLogger('LOGGER2')
# ch = logging.FileHandler(r"C:\Users\skandula27\Desktop\sample4.txt")
# #logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s : %(asctime)s',filename=r"C:\Users\skandula27\Desktop\sample2.txt",filemode='w')
# # create console handler and set level to debug
#
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # 'application' code
# # logger.debug('debug messatryrge')
# # logger.info('info message')
# logger.warn('warn message')
# # logger.error('error message')
# # logger.critical('critical message')

logger = logging.getLogger("mylogger")
logger.setLevel(logging.CRITICAL)

user = "dxc3students@gmail.com"
pwd = "987654321@password"
h2 = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                            fromaddr='dxc3students@gmail.com',
                            toaddrs=['saicharan.kandula18@gmail.com'],
                            subject='The log',
                            credentials=(user , pwd ),
                            secure=())
h2.setLevel(logging.CRITICAL)
#logging.handlers.SMTPHandler.emit = emit
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
h2.setFormatter(formatter)
logger.addHandler(h2)
logger.critical("critical error occured")


# create logger
logger = logging.getLogger('LOGGER1')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler(r"C:\Users\skandula27\Desktop\sample5.txt")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
logger.debug('debug message')