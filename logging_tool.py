import logging
import os
import time
BasePase = os.path.dirname(__file__)
ford_path = os.path.join(BasePase, "log")
if not os.path.exists(ford_path):
    os.mkdir(ford_path)


class Logger:

    def __init__(self):
        self.logname = os.path.join(ford_path, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger('log')
        self.logger.setLevel(level=logging.DEBUG)
        self.formater = logging.Formatter("[%(asctime)s][%(levelname)-8s][%(filename)-6s:%(lineno)-2s]:%(message)-25s", datefmt="%Y-%m-%d %H:%M:%S")
        self.console = logging.StreamHandler()
        self.file = logging.FileHandler(filename=self.logname, mode="a", encoding="UTF-8")
        self.console.setFormatter(self.formater)
        self.file.setFormatter(self.formater)
        self.console.setLevel(logging.DEBUG)
        self.file.setLevel(logging.DEBUG)
        self.logger.addHandler(self.file)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
