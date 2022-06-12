from application import app
import socket

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

if __name__ == '__main__':
    app.run(debug=True,host=ip_address)