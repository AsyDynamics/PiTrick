Configure rpi as nas
step 1 make a directory
  mkdir Music
step 2 install samba
  sudo apt update
  sudo apt upgrade
  sudo apt install samba samba-common-bin
step 3 configure samba
  sudo su
  nano /etc/samba/smb.conf
  
  // add lines below
  [Music] 
  comment = public storage 
  browseable = yes
  path = /home/pi/Music 
  create mask = 0777 
  directory mask = 0777 
  browseable = yes
  public = yes
  
step 4 set account
  sudo smbpasswd -a account_name
  // enter passwd twice
  
step 5 restart service
  sudo /etc/init.d/samba restart
  
step last map network drive on other device
  e.g. on win 10, open 'this pc' and click 'map network drive', enter \\ipaddress\Music, then account name and passwd
  
Done!
