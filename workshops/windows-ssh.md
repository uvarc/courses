# SSH using Windows

How to SSH into Linux from a Windows instance. To complete these steps you will need:

* A Windows desktop with the [PuTTY SSH client](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) installed.
* An SSH keypair; the private half should be local to your workstation, the public half should already be loaded into the remote Linux instance. This keypair must be Windows-compatible, or it will not work.
* You need the public IP of the remote instance you want to shell into.
* You need the user account name of the remote instance you want to shell into.


## Logging in via SSH

1. Open PuTTY.
2. On the "Session" pane, enter the IP address of your remote instance into the "Host Name (or IP address)" field.
3. Scroll down in PuTTY settings, and look for Connection -> SSH -> Auth.
4. In the field marked "Private key file for authentication" select BROWSE. Locate the private key half on your workstation.
5. Click OPEN at the bottom of the window.
6. You should be prompted for the username you want to login as. Enter the username and press return.
7. You should now be logged into a Linux shell. 
8. Once you are done, type `exit` to leave the shell and close PuTTY.


## Creating SSH Keys using PuTTYGen

For more information on how to create a Windows-compatible SSH keypair, [see this page](https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows).

