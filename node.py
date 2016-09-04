#!/usr/bin/env python
""" Contains implementations of various clock nodes. """

class Node(object):
    """ Represents a node with a clock. """

    def __init__(self, name):
        self.name = name

    def send(self, other):
        """
        Sends a message containing this node's clock value to another node.

        @param {Node} other - The other node to send to
        """
        pass

    def receive(self, other):
        """
        Receives a clock value from another node and updates the clock value of
        this node.

        @param {number} clock - The numeric clock value of the other node
        """
        pass

class LamportClockNode(Node):
    """ Represents a node with a Lamport clock. """

    def __init__(self, name):
        Node.__init__(self, name)
        self.clock = 0

    def send(self, other):
        self.clock += 1
        print "[*] Node %s: Sending clock message <%d>" \
                % (self.name, self.clock)
        other.receive(self)

    def receive(self, other):
        tmp = self.clock
        self.clock = max(self.clock, other.clock) + 1
        print "[*] Node %s: Receiving clock message <%d> -> <%d>" \
                % (self.name, tmp, self.clock)

class VectorClockNode(Node):
    """ Represents a node with a vector clock. """

    def __init__(self, name):
        Node.__init__(self, name)
        self.clock = {}
        self.clock[self.name] = 0

    def send(self, other):
        self.clock[self.name] += 1
        print "[*] Node %s: Sending clock message <%s>" \
                % (self.name, self.clock)
        other.receive(self)

    def receive(self, other):
        tmp = self.clock
        self.clock = self.merge(self.clock, other.clock)
        self.clock[self.name] = self.clock[self.name] + 1
        print "[*] Node %s: Receiving clock message <%s> -> <%s>" \
                % (self.name, tmp, self.clock)

    @staticmethod
    def merge(clock_1, clock_2):
        """ Merges two vector clocks """
        def compare(val_1, val_2):
            """ Merges two the vector clock values """
            if val_1 is None:
                return val_2
            elif val_2 is None:
                return val_1
            else:
                return max(val_1, val_2)

        keys = clock_1.keys() + clock_2.keys()
        return {k: compare(clock_1.get(k), clock_2.get(k)) for k in keys}

