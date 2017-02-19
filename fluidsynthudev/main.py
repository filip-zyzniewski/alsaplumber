'Provides the entry point.'

import pyalsa.alsaseq

def main():
    seq = pyalsa.alsaseq.Sequencer(
        name = 'default',
        clientname = 'fluidsynthudev',
        streams = pyalsa.alsaseq.SEQ_OPEN_DUPLEX,
        mode = pyalsa.alsaseq.SEQ_BLOCK,
    )
    for name, id, connected in seq.connection_list():
        print name, id, connected
