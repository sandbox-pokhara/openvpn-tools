import time

import requests

from .logger import logger

IP_ENDPOINT = 'https://api.myip.com'


def get_ip_address(endpoint=IP_ENDPOINT):
    try:
        response = requests.get(endpoint, timeout=30)
        if response.ok:
            return response.json()
        return None
    except requests.RequestException:
        return None


def verify_ip_change(original_ip, timeout=30):
    logger.info('Verifying vpn connection...')
    start = time.time()
    while True:
        if time.time() - start > timeout:
            logger.info(f'Timed out verifying vpn connection.')
            return False

        new_ip_address = get_ip_address()
        if new_ip_address is not None and original_ip != new_ip_address:
            logger.info(
                f'VPN connected successfully. Old IP: {original_ip}, New IP: {new_ip_address}')
            return True
