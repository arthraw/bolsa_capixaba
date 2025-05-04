from src.utils.variables import url
from src.ingestion.scraping import open_browser
import logging
from src.utils import log

logger = logging.getLogger(__name__)

def load_data():
    logger.info('Initializing web scraping.')
    open_browser(url)
    logger.info('Web scraping ended.')
