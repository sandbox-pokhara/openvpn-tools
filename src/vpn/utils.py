import os

OPENVPN_CONFIG_DIR = os.path.expanduser(os.path.join('~', 'OpenVPN', 'config'))


def write_vpn_auth_file(path, vpn_username, vpn_password):
    with open(path, 'w') as fp:
        fp.write(f'{vpn_username}\n{vpn_password}\n')
