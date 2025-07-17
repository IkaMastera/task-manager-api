# 🐧 Linux Practice Notes - Challenge

## 10 Practical Linux Tasks

### 1. Create a new user

```bash
sudo adduser devops_user

### 2.Give sudo access to a user
sudo usermod -aG sudo devops_user

### 3.List all users on the system
cut -d -f1 /etc/passwrd

### 4.Check running processes
ps aux

### 5.Kill a process
kill -9 <PID>

### 6.Check disk space usage
df -h

### 7.Check memory usage
free -h

### 8. Create and remove a dircetory
mkdir myfolder
rm -r myfolder

### 9.SSH into a remote machine
ssh username@ip_address

### 10.Copy files securely between machines
scp file.txt username@ip:/home/username/

#Core 🐧 Linux Commands Learned
ls  ### Lists files and folders in current directory
cd  ### Changes directory
chmod  ### Changes files permissions
ps  ### Shows running processes
kill ### Terminates a process
curl  ### Makes HTTP requests
scp  ### Securely copies files
ssh  ### Connects to another machine securely
grep  ### Searches for text in files
tail  ### Shows last lines of a file
head  ### Shows first lines of a file
sudo  ### Runs a command as a superuser
top  ### Live system process monitor