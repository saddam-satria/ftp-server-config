# FTP Server Setup

### Install

```
sudo apt install vsftpd
```

### Set Config

```
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.old
sudo nano /etc/vsftpd.conf -> Copy From file config/vsftpd.conf

```

### Create New User

```
export FTP_USER=ftp-client
sudo adduser --home /home/$FTP_USER $FTP_USER
Type Password
Enter

```

### Make FTP File

```
sudo mkdir /home/$FTP_USER/ftp
sudo chown -R $FTP_USER:$FTP_USER /home/$FTP_USER/ftp

```

### Add User To FTP User List

```
echo $FTP_USER | sudo tee -a /etc/vsftpd.userlist
```

### Try To Connect

```
ftp -d $FTP_HOST
```

### Serve As Static Content

```
sudo apt install nginx -y
sudo mkdir /var/www/contents
sudo ln -s /home/$FTP_USER/ftp /var/www/contents/$FTP_USER

for nginx configuration open config/nginx.conf


```
