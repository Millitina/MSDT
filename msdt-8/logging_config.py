import logging
from datetime import datetime

# Новый уровень, т.к. логи о вызовах методов операторов засоряют лог
logging.addLevelName(5, 'DEBUG_EX')
logging.basicConfig(
    filename=f'Log_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.log',
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] => %(message)s',
    encoding='utf-8',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()

logger.info(f'Выбран уровень логирования: {logging.getLevelName(logger.level)}')
