import os
import traceback
from subprocess import PIPE
from subprocess import Popen
from subprocess import SubprocessError

from .ip import get_ip_address
from .ip import verify_ip_change
from .logger import logger
from .process import kill_process
from .utils import write_vpn_auth_file

OPENVPN_EXE_PATH = 'C:\\Program Files\\OpenVPN\\bin\\openvpn.exe'
OPENVPN_GUI_EXE_PATH = 'C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe'


def connect(vpn_filepath, vpn_username=None, vpn_password=None, verify=True, verify_timeout=30):
    logger.info(f'Connecting to vpn {vpn_filepath}...')
    command = [
        OPENVPN_EXE_PATH,
        '--config',
        os.path.realpath(vpn_filepath)
    ]
    if vpn_username is not None and vpn_password is not None:
        auth_filepath = os.path.join(os.path.dirname(vpn_filepath), 'auth.txt')
        write_vpn_auth_file(auth_filepath, vpn_username, vpn_password)
        command += [
            '--auth-user-pass',
            os.path.realpath(auth_filepath),
        ]

    if verify:
        start_ip = get_ip_address()
    logger.info(f'Executing {" ".join(command)}')
    try:
        dir_name = os.path.dirname(vpn_filepath)
        process = Popen(command, cwd=dir_name, stdout=PIPE)
        for output in iter(process.stdout.readline, ''):
            line = output.decode().strip()
            logger.debug(line)
            if 'Initialization Sequence Completed' in line:
                break
            if 'Exiting due to fatal error' in line:
                logger.error('Error connecting to vpn: Fatal error')
                process.kill()
                return False
            if 'Access is denied' in line:
                logger.error('Error connecting to vpn: Access is denied, try running as admin')
                process.kill()
                return False

    except SubprocessError:
        logger.error(f'Error connecting to vpn: {traceback.format_exc()}')
        return False

    if verify:
        return verify_ip_change(start_ip, verify_timeout)

    return True


def disconnect():
    logger.info("Disconnecting all openvpn instances...")
    kill_process('openvpn.exe')
