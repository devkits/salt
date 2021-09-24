"""
Encapsulate the different transports available to Salt.
"""


import logging
import warnings

log = logging.getLogger(__name__)

# Suppress warnings when running with a very old pyzmq. This can be removed
# after we drop support for Ubuntu 16.04 and Debian 9
warnings.filterwarnings(
    "ignore", message="IOLoop.current expected instance.*", category=RuntimeWarning
)
