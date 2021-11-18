import sys

from . import windows
from .windows import OPENVPN_GUI_PATH

__all__ = [
    'get_connected_vpn',
    'disconnect',
    'connect',
]


def get_connected_vpn():
    if sys.platform == 'win32':
        return windows.get_connected_vpn()
    raise NotImplementedError('Platform is not implemented yet.')


def disconnect(openvpn_gui_path=OPENVPN_GUI_PATH):
    if sys.platform == 'win32':
        return windows.disconnect(openvpn_gui_path=openvpn_gui_path)
    raise NotImplementedError('Platform is not implemented yet.')


def connect(vpn_file_path, vpn_username=None, vpn_password=None, openvpn_gui_path=OPENVPN_GUI_PATH):
    if sys.platform == 'win32':
        return windows.connect(
            vpn_file_path,
            vpn_username=vpn_username,
            vpn_password=vpn_password,
            openvpn_gui_path=openvpn_gui_path,
        )
    raise NotImplementedError('Platform is not implemented yet.')
