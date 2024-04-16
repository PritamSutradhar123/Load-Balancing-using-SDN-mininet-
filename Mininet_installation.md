## Here's how you can install mininet inside your VirtualBox(Ubuntu)
It's recomended to use Ubuntu 18.04.6 LTS (bionic Beaver) version
  <br>
[click this link to download](https://releases.ubuntu.com/18.04.6/ubuntu-18.04.6-desktop-amd64.iso)
<br>
After installing Ubuntu in your VM, you should run the following commands in your terminal to prepare your VM for Mininet installation
1. su
2. whoami
3. apt install sudo
4. usermod -aG sudo <user_name> #This will grant sudo previlege to the user... it's important because some file will be in read mode only
5. then restart your VM to apply the changes
<h1>Now comes the Mininet installation along with pox, openflow and other relevent folders</h1>
1. sudo apt-get update
2. sudo apt-get upgrade #this might takes some time to complete
3. sudo apt-get install git
4. git clone https://github.com/mininet/mininet
5. cd mininet
6. git tag #it will display all the versions
7. cd
8. mininet/util/install.sh -a #-a means full installation
9. sudo mn
enjoy mininet
