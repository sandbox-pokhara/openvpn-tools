import sys

from . import windows_cui
from . import windows_gui
from .windows_gui import OPENVPN_GUI_PATH

__all__ = [
    'get_connected_vpn',
    'disconnect',
    'connect',
]


def get_connected_vpn(gui=False):
    if sys.platform == 'win32':
        if gui:
            return windows_gui.get_connected_vpn()
        else:
            raise NotImplementedError('Feature is not implemented yet.')
    raise NotImplementedError('Platform is not implemented yet.')


def disconnect(openvpn_gui_path=OPENVPN_GUI_PATH, gui=False):
    if sys.platform == 'win32':
        if gui:
            return windows_gui.disconnect(openvpn_gui_path=openvpn_gui_path)
        else:
            return windows_cui.disconnect()
    raise NotImplementedError('Platform is not implemented yet.')


def connect(vpn_file_path,
            vpn_username=None,
            vpn_password=None,
            openvpn_gui_path=OPENVPN_GUI_PATH,
            gui=False,
            verify=True,
            verify_timeout=30):
    if sys.platform == 'win32':
        if gui:
            return windows_gui.connect(
                vpn_file_path,
                vpn_username=vpn_username,
                vpn_password=vpn_password,
                openvpn_gui_path=openvpn_gui_path,
            )
        else:
            return windows_cui.connect(
                vpn_file_path,
                vpn_username=vpn_username,
                vpn_password=vpn_password,
                verify=verify,
                verify_timeout=verify_timeout,
            )
    raise NotImplementedError('Platform is not implemented yet.')
