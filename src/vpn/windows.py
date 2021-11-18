
import logging
import os
from pathlib import Path
from subprocess import run

import psutil

OPENVPN_GUI_PATH = os.path.join('C:', os.sep, 'Program Files', 'OpenVPN', 'bin', 'openvpn-gui.exe')
OPENVPN_CONFIG_DIR = os.path.expanduser(os.path.join('~', 'OpenVPN', 'config'))


def write_vpn_auth_file(path, vpn_username, vpn_password):
    with open(path, 'w') as fp:
        fp.write(f'{vpn_username}\n{vpn_password}\n')


def add_credentials_to_config(vpn_file_path, auth_file_path):
    output = []
    with open(vpn_file_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if not line.startswith('auth-user-pass'):
                output.append(line)
        output.append(f'auth-user-pass {os.path.basename(auth_file_path)}\n')
    return output


def get_connected_vpn():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in ['openvpn', 'openvpn.exe']:
            try:
                cmdline = proc.cmdline()
                for key, value in zip(cmdline, cmdline[1:]):
                    if key == '--config':
                        return Path(value).stem
            except psutil.Error:
                pass
    return None


def disconnect(openvpn_gui_path=OPENVPN_GUI_PATH):
    run([openvpn_gui_path, '--command', 'disconnect_all'], timeout=30)


def connect(vpn_file_path, vpn_username=None, vpn_password=None, openvpn_gui_path=OPENVPN_GUI_PATH):
    # TODO: Verify if the vpn successfullly connected, log can be used
    connected = get_connected_vpn()
    vpn_file_stem = Path(vpn_file_path).stem
    if connected == vpn_file_stem:
        return False
    if connected is not None:
        disconnect(openvpn_gui_path=openvpn_gui_path)
    if vpn_username is not None and vpn_password is not None:
        logging.info('Creating temporary vpn auth file...')
        auth_file_path = os.path.join(OPENVPN_CONFIG_DIR, f'{vpn_file_stem}.txt')
        new_vpn_file_path = os.path.join(OPENVPN_CONFIG_DIR, f'{vpn_file_stem}.ovpn')
        write_vpn_auth_file(auth_file_path, vpn_username, vpn_password)
        new_config = add_credentials_to_config(vpn_file_path, auth_file_path)
        with open(new_vpn_file_path, 'w') as fp:
            fp.writelines(new_config)
    run([openvpn_gui_path, '--command', 'connect', vpn_file_stem], timeout=30)
    return True
