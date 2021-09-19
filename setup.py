"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
import versioneer


setup(
    name='outlookdisablespamfilter',
    version=versioneer.get_version(),
    description='Disable Spam Filter on outlook.com by transfering emails from Junk mailbox to Inbox.',
    url='https://github.com/emailfilter/outlook-disable-spam-filter',
    author='Jan Janssen',
    author_email='jan.janssen@outlook.com',
    license='BSD',
    packages=find_packages(exclude=["*tests*"]),
    install_requires=[],
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
        "console_scripts": [
            'outlookdisablespamfilter=outlookdisablespamfilter.__main__:command_line_parser'
        ]
    }
)
