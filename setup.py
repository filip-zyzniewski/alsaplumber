import os
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        f.read()

name = 'alsaplumber'

setup(
    name = name,
    version = '0.0.1',
    author = 'Filip Żyźniewski',
    author_email = 'filip.zyzniewski@gmail.com',
    description = 'Connects and disconnects MIDI inputs from sequencers.',
    license = 'GPLv3',
    keywords = 'midi alsaseq udev fluidsynth timidity',
    url = 'http://packages.python.org/alsaplumber',
    packages=[name],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
