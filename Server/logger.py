# coding:utf-8
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/12 17:07   tao.chen     1.0         No
"""

import logging.config
import settings

logging.config.dictConfig(settings.LOGGING_DIC)
logger = logging.getLogger("test_logger")