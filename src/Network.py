"""
helpful networking functions which really should be separated
"""


def recv_msg(sock):
    """
    a macro function for getting a message from the socket.
    this function will block execution until it gets data / times out.
    this function will also crash the instance if it does not get a response from the socket.

    :param sock: the socket to fetch a message from
    :return: decoded data from the socket
    """
    # get an arbitrary number of bytes
    m = sock.recv(4096)
    # let the client know we got their message
    sock.sendall(b"200 OK")
    # return the decoded data
    return m.decode("utf-8")


# a macro for sending a message to the client
def send_msg(sock, d):
    """
    a macro function for sending a message through the socket.
    this function will block execution until it gets data / times out.
    this function will also crash the instance if it does not get a response from the socket.

    :param sock: the socket to send a message to
    :param d: the data to send
    :return: decoded data from the socket
    """
    # if d is not castable to bytes, cast it to string
    if type(d) not in [bytes, str]:
        d = str(d)
    # if d is not a bytes object, we kinda need it to be
    if type(d) != bytes:
        d = bytes(d, "utf-8")

    # send the bytes object
    sock.sendall(d)

    # wait for an answer
    ans = sock.recv(4096)

    # assert that the message was acknowledged
    # you have no idea how much headache
    # this saved me during development
    assert ans == b"200 OK"
