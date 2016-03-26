              __       __    __
    .--.--.--|__.-----|  |--|  |--.-----.-----.-----.
    |  |  |  |  |__ --|     |  _  |  _  |     |  -__|
    |________|__|_____|__|__|_____|_____|__|__|_____|
                                       version 2.1.2

    Build composable event pipeline servers with minimal effort.


    ===================
    wishbone.output.udp
    ===================

    Version: 0.1.0

    A Wishbone output module to submit event data to a UDP socket.
    --------------------------------------------------------------


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


