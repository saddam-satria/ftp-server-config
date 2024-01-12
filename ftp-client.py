from ftplib import FTP


try:
    ftpClient = FTP()
    ftpClient.set_pasv(False) 
    ftpClient.connect("192.168.100.101", port=21)
    ftpClient.login("client-test", "test")

    with open("test.jpg", "rb") as file:
        ftpClient.storbinary("STOR files/test.jpg", file)
    
except Exception as E:
    print(E)