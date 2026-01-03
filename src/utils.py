import logging
import random
import numpy as np
import sys

def setup_logger(name="research"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    # torch if needed
