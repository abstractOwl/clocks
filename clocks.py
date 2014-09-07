#!/usr/bin/env python
"""
Simulation of Lamport clocks.
"""

class Node(object):
    """ Represents a node with a Lamport clock. """

    def __init__(self, name):
        self.clock = 0
        self.name = name

    def send(self, other):
        """
        Sends a message containing this node's clock value to another node.

        @param {Node} other - The other node to send to
        """
        self.clock += 1
        print "[*] Node %s: Sending clock message (%d)" \
                % (self.name, self.clock)
        other.receive(self.clock)

    def receive(self, clock):
        """
        Receives a clock value from another node and updates the clock value of
        this node.

        @param {number} clock - The numeric clock value of the other node
        """
        tmp = self.clock
        self.clock = max(self.clock, clock) + 1
        print "[*] Node %s: Receiving clock message (%d->%d)" \
                % (self.name, tmp, self.clock)


def add(nodes, new_nodes):
    """ Adds new node(s) to the network.

    @param {dict} nodes - Network of nodes
    @param {list} new_nodes - List of new nodes to create
    """
    for node in new_nodes:
        print "[*] Added node %s" % node
        nodes[node] = Node(node)

def list_nodes(nodes):
    """ Lists nodes in the network.

    @param {dict} nodes - Network of nodes
    """
    print "[*] Listing nodes..."
    for node in nodes:
        print "[*] Node %s (clock: %d)" % (node, nodes[node].clock)

def print_help():
    """ Prints help message. """
    print "Commands: "
    print "  add [<a>...] - Adds node(s) to the network"
    print "  list         - Lists all nodes and their clock values"
    print "  send <a> <b> - Sends a message from node a to b"
    print "  quit         - Exits"
    print "  ?            - Prints this message"

def send(nodes, params):
    """ Sends a message from a node to another node.

    @param {dict} nodes - Network of nodes
    @params {list} params - List containing (sender, receiver) pair
    """

    if len(params) != 2:
        print '[!] ERROR: Expected 2 params, got %d' % len(params)
        return

    sender, receiver = params
    if not(sender in nodes and receiver in nodes):
        print '[!] ERROR: Invalid node(s) (%s, %s)' % (sender, receiver)
        return

    nodes[sender].send(nodes[receiver])

def cmds():
    """ Prints commands and returns input. """
    return raw_input('[?] Enter command (add/list/send/quit/?): ')

def main():
    """ The entrypoint function. """
    nodes = {}
    while True:
        param_list = cmds().split()

        if len(param_list) < 1:
            continue

        print

        cmd = param_list.pop(0)

        if cmd == 'add':
            add(nodes, param_list)
        elif cmd == 'list':
            list_nodes(nodes)
        elif cmd == 'send':
            send(nodes, param_list)
        elif cmd == '?':
            print_help()
        elif cmd == 'quit':
            break
        else:
            print '[!] ERROR: Unrecognized command'

        print


if __name__ == '__main__':
    main()

