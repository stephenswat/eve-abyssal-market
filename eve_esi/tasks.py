import logging

from huey.contrib.djhuey import on_startup

from eve_esi import ESI


logger = logging.getLogger(__name__)


@on_startup()
def initialize_esi():
    logger.info("Initializing ESI application to start Huey consumer")
    ESI._initialize_app()
    logger.info("ESI application initialized for consumer!")
