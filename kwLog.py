' kwLog module'
__author__ = 'kuang wei'

'''这个模块是我在python原有logging模块基础上简单封装的一个类，只是方便我自己使用。'''

import logging
class kwLog(object):
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    
    def __new__(cls):
        logger = logging.getLogger('kwLog')
        logger.setLevel(level = logging.INFO)
        logger.addHandler(kwLog.handler)
        logger.addHandler(kwLog.console)
        return logger        
        
def test():
    logger = kwLog()
    logger.info('hello world')
    
if __name__ == '__main__':
    test()