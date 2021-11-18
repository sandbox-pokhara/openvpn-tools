import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='openvpn-tools',
    version='0.0.1',
    author='Pradish Bijukchhe',
    author_email='pradishbijukchhe@gmail.com',
    description='Cross-platform openvpn tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sandbox-pokhara/openvpn-tools',
    project_urls={
        'Bug Tracker': 'https://github.com/sandbox-pokhara/openvpn-tools/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['psutil'],
)
