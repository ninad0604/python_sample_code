"""
This example is to show best practices when using logging in python modules and submodules
references:
1. https://timber.io/blog/the-pythonic-guide-to-logging/#the-drawbacks
2. https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
3. https://docs.python.org/3/howto/logging.html#optimization

calling this script as:
$$ LOG_CFG=my_logging.yaml python logging_example.py

"""

import os
import logging.config
import yaml
import logging

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__ == '__main__':
    setup_logging()
