#!/usr/bin/env python3

from multiprocessing.managers import SyncManager
from multiprocessing import Manager
from queue import Queue
import copy

class NeuronManager(SyncManager):
    pass
web_neuron = Manager().dict()
alexa_neuron = Manager().dict()
NeuronManager.register('get_web_neuron', callable=lambda:web_neuron)
NeuronManager.register('get_alexa_neuron', callable=lambda:alexa_neuron)
manager = NeuronManager(address=('', 4081), authkey=b'daisy')

print("Neuron Manager Started")
server = manager.get_server()
server.serve_forever()
