# CentOS Setup Guide

Briefly describe the process you would use to set up a CentOS virtual machine and install Docker on it.

## 1. Connect to the Machine Using SSH

```bash
ssh user@hostname
```

## 2. Create a New User

```bash
sudo adduser newuser
sudo passwd newuser
```

## 3. Update Packages

```bash
sudo yum update -y
```

## 4. Generate an SSH Key

```bash
ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
```

## 5. Verify SSH Agent and Add SSH Key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

```bash
ssh-copy-id newuser@hostname
```

## 6. Install and Configure Firewall to Allow SSH

```bash
sudo yum install firewalld -y
sudo systemctl enable firewalld
sudo systemctl start firewalld
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

## 7. Install Docker

```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce docker-ce-cli containerd.io
```

## 8. Start and Enable Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

## 9. Pull a Docker Image from Docker Hub

```bash
sudo docker pull nginx
```

## 10. Run a Container from the Pulled Image

```bash
sudo docker run -d -p 8080:80 --name nginx nginx
```

Pulling the Nginx image and running a container is to verify that Docker is working correctly.

Now you can access the Nginx server at `http://hostname:8080` or `http://localhost:8080` in your web browser.
