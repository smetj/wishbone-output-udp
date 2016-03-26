#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tcpout.py
#
#  Copyright 2016 Jelle Smet <development@smetj.net>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from wishbone import Actor
from wishbone.event import Bulk
from gevent import socket


class UDPOut(Actor):

    '''**Submit event data to an UDP socket.**

    Writes data to an UDP socket.

    When <data> is of type list, all elements
    will be joined using <delimiter> and submitted together.

    Parameters:

        - selection(str)("@data")
           |  The part of the event to submit externally.
           |  Use an empty string to refer to the complete event.

        - host(string)("localhost")
           |  The host to submit to.

        - port(int)(19283)
           |  The port to submit to.

        - delimiter(str)("")
           |  A delimiter to add to each event.


    Queues:

        - inbox
           |  Incoming events submitted to the outside.

    '''

    def __init__(self, actor_config, host="127.0.0.1", port=19283, delimiter=""):
        Actor.__init__(self, actor_config)

        self.pool.createQueue("inbox")
        self.registerConsumer(self.consume, "inbox")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def consume(self, event):

        if isinstance(event, Bulk):
            data = Bulk.dumpFieldsAsString(self.kwargs.selection)
        else:
            data = event.get(self.kwargs.selection)

        self.socket.sendto(str(data), (self.kwargs.host, self.kwargs.port))
