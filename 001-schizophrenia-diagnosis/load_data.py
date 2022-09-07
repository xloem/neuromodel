import numpy as np
import pyedflib

import os

DATAPATH = 'data'

data = {
}
for datafilename in os.listdir(DATAPATH):
    if not datafilename.endswith('.edf'):
        continue
    datafilepath = os.path.join(DATAPATH, datafilename)
    signals, signal_headers, edf_header = pyedflib.highlevel.read_edf(datafilepath, verbose=True)

    # break into 30 second chunks
    chunk_size = int(30 * signal_headers[0]['sample_rate'])
    channels, samples = signals.shape
    chunks = samples // chunk_size
    offset = (samples - chunks * chunk_size) // 2

    signals = signals[:,offset:samples-offset].reshape(channels, chunks, chunk_size)
    group = datafilename[0]
    if group not in data:
        data[group] = []
    data[group].append(signals)

for group in data.values():
    np.random.shuffle(group)

training = {
    groupname: groupdata[1:]
    for groupname, groupdata in data.items()
}
validation = {
    groupname: groupdata[:1]
    for groupname, groupdata in data.items()
}
