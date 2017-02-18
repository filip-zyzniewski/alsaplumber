import os
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        f.read()

name = 'fluidsynthudev'

setup(
    name = name,
    version = '0.0.1',
    author = 'Filip Żyźniewski',
    author_email = 'filip.zyzniewski@gmail.com',
    description = 'Launches and kills fluidsynth on udev events',
    license = 'GPLv3',
    keywords = 'fluidsynth midi alsaseq udev',
    url = 'http://packages.python.org/fluidsynthudev',
    packages=[name],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
