import logging

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Logging at different levels
logging.debug('This is a DEBUG message')
logging.info('This is an INFO message')
logging.warning('This is a WARNING message')
logging.error('This is an ERROR message')
