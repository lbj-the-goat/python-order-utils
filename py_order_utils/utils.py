import math
import web3
from string import punctuation
from random import random
from datetime import datetime, timezone

max_int = math.pow(2, 32)

def normalize(s: str)-> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered

def normalize_address(address: str) -> str:
    return web3.Web3.toChecksumAddress(address)

def generate_seed()-> int:
    """
    Pseudo random seed
    """
    now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    return round(now * random()) 