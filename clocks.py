#!/usr/bin/env python
""" Simulation of various clock algorithms in distributed systems. """

import sys

from node import LamportClockNode
from node import VectorClockNode

USAGE = """Commands:
  add [<a>...] - Adds node(s) to the network
  list         - Lists all nodes and their clock values
  send <a> <b> - Sends a message from node a to b
  quit         - Exits
  ?            - Prints this message"""

class Clocks(object):
    """ Runs the Clock simulation. """

    def __init__(self):
        self.nodes = {}

    def add(self, new_nodes, clock_type):
        """ Adds new node(s) to the network.

        @param {list} new_nodes - List of new nodes to create
        @param {string} clock_type - Type of node to create
        """
        for name in new_nodes:
            print "[*] Added node %s" % name
            self.nodes[name] = self.new_node(clock_type, name)

    @staticmethod
    def new_node(clock_type, name):
        """ Utility function to create a new node.

        @param {string} clock_type - Type of node to create
        @param {string} name - Name of node to create
        """
        if clock_type == 'lamport':
            return LamportClockNode(name)
        elif clock_type == 'vector':
            return VectorClockNode(name)
        else:
            raise 'Invalid node type'

    def list_nodes(self):
        """ Lists nodes in the network. """
        print "[*] Listing %d nodes..." % len(self.nodes)
        for node in self.nodes:
            print "[*] Node %s <%s>" % (node, self.nodes[node].clock)

    @staticmethod
    def print_help():
        """ Prints help message. """
        print USAGE

    def send(self, params):
        """ Sends a message from a node to another node.

        @params {list} params - List containing (sender, receiver) pair
        """
        if len(params) != 2:
            print '[!] ERROR: Expected 2 params, got %d' % len(params)
            return

        sender, receiver = params
        if not(sender in self.nodes and receiver in self.nodes):
            print '[!] ERROR: Invalid node(s) (%s, %s)' % (sender, receiver)
            return

        self.nodes[sender].send(self.nodes[receiver])

    @staticmethod
    def cmds():
        """ Prints commands and returns input. """
        return raw_input('[?] Enter command (add/list/send/quit/?): ')

    def run(self, clock_type):
        """ Runs the simulation REPL. """
        while True:
            param_list = self.cmds().split()
            if len(param_list) < 1:
                continue

            print

            cmd = param_list.pop(0)
            if cmd == 'add':
                self.add(param_list, clock_type)
            elif cmd == 'list':
                self.list_nodes()
            elif cmd == 'send':
                self.send(param_list)
            elif cmd == '?':
                self.print_help()
            elif cmd == 'quit':
                break
            else:
                print '[!] ERROR: Unrecognized command'

            print

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['lamport', 'vector']:
        CLOCK_TYPE = 'lamport'
    else:
        CLOCK_TYPE = sys.argv[1]

    Clocks().run(CLOCK_TYPE)

