import socket
import logging
from datetime import date, datetime

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)

logging.info('Server is running')

try:
    while True:
        conn, addr = sock.accept()
        logging.info('Connected: %s', addr)
        data = conn.recv(1024)
        if data == b'hi':
            logging.info('Received message: %s', data)
            conn.send(b'hello')
        elif data == b'what date is today':
            logging.info('Received message: %s', data)
            dateAsString = str(date.today())
            conn.send(dateAsString.encode())
        elif data == b'what time is now':
            logging.info('Received message: %s', data)
            timeAsString = str(datetime.now())
            conn.send(timeAsString.encode())
        else:
            logging.warning('Received unknown message: %s', data)
            conn.send(b'unknown command')
        conn.close()
except KeyboardInterrupt:
    logging.info('Server stopped')