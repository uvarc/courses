# Introduction to Cloud - Workshop

In this lab you will learn how to create an RStudio Server instance in Amazon EC2. Follow the lab instructions below at your own pace. Please raise your hand or get the attention of an instructor if you have any questions.

* EC2 Operations
  * [Creating or setting up an SSH keypair](#set-up-ssh-keypairs).
  * [Launching an EC2 compute instance](#launch-an-ec2-instance).
  * [Bootstrapping an EC2 instance for launch](#bootstrapping-your-instance).
  * [Using a web browser to access your instance](#using-a-web-browser-to-access-your-instance).
  * [Using SSH to log into your instance](#using-ssh-to-log-into-your-instance).
* [Further Resources](#resources)

- - -

## EC2 - Elastic Compute Cloud

1. Log into the **AWS Console** using the account given to you in class.
2. From the SERVICES tab in the upper-left corner, select the **EC2** service.
3. Verify your region. EC2 instances can be placed within various regional locations around the world. For today's workshop please make sure that the OREGON region is selected for your region by checking the upper-right corner of your screen. This region is also known as US-East-2 (Ohio).

- - -

### Set up SSH Keypairs

**Mac / Linux users:**
* If this is a new AWS account, you do not yet have any SSH keys created. SSH key pairs are a secure way of signing into your EC2 instance, instead of a username and password.
* From the EC2 dashboard, select the "Key Pairs" menu item down the lefthand side of the page.
* Click on **Create Keypair**, and give it a memorable name. Then click "Create".
* The private half of the kaypair will now be immediately downloaded to your browser. Store this half in a safe location on your computer. The public half of the key pair is now in your AWS account.

**Windows users:**
* Windows users accessing Linux instances using SSH need to use PuTTy. PuTTy requires a special format of SSH key that you can create yourself. PuTTy (http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
* Follow the instructions in Step 5 (https://www.howtoforge.com/ssh_key_based_logins_putty_p2#-generate-a-privatepublic-key-pair) to create a PuTTY-compatible set of SSH keys. 
* Save the private key to your local computer.
* Copy the public key to your clipboard.
* From the EC2 dashboard, select the "Key Pairs" menu item down the lefthand side of the page.
* Select "Import Key Pair" and then paste the public half of your key into the text input. Give it a name and click IMPORT. This SSH key will be available to you in the future as you create EC2 instances.

- - -

### Launch an EC2 instance

4. From the EC2 dashboard, click **LAUNCH INSTANCE**.
5. Find the **Ubuntu Server 16.04** instance and select it using the blue button.
6. Select Instance type **t2.medium**. Take note of other instance types (sizes) available to you.
7. Click **NEXT: Configure Instance Details**.

### Bootstrapping your instance

8. Leave the settings as they are configured by default, but take time to note what they are. Scroll down the page and open the "Advanced" portion of the screen.
9. In the **User Data** field, paste the code below into the text box:

```bash
#!/bin/bash

apt-get -y update
apt-get -y upgrade

useradd -m -s /bin/bash rstudio
echo 'rstudio:rstudio'|chpasswd

apt-get -y install r-base
apt-get -y install gdebi-core
cd /tmp
wget https://download2.rstudio.org/rstudio-server-1.0.136-amd64.deb
gdebi --n rstudio-server-1.0.136-amd64.deb
```

10. Click **Next: Add Storage**. Leave these settings as they are, but note how you can expand the size of the instance hard drive, or add other drives.
11. Click **Next: Add Tags**. Create a tag for your instance (optional) and give it a simple name. Click the gray button to add a tag. They "key" should be "Name" and the "value" should be whatever you'd like to name your instance.
12. Click **Next: Security Group**. Here you will create a new security group for your instance, and grant access to users.
13. Making sure that the "Create a new security group" option is selected, click the **Add Rule** button.
14. Create a new security group rule. It should be of the "Custom TCP Rule" type, the port range should be 8787, and the source should be "Anywhere".
15. Note that security groups are an important way you control visibility and access to your instance. Some ports and services, such as web servers (port 80) are normally visible to "Anywhere", whereas administrative ports such as 22 are normally restricted to specific sources.
16. Click **Review and Launch**.
17. Review your instance settings (which you can change if necessary, taking you through the setup wizard again). Once ready, click the blue **Launch** button.
18. Finally, confirm the SSH key you will be using to access this instance. You must specify a key pair (such as the one you created in the steps above), and check the acknowledgement box before you can click **Launch Instances**.
19. Your server is now being created and configured! Take a short break (3-5 minutes) while your server is built.
20. Click on **View Instances**, or select "Instances" from the lefthand navigation.

### Using a web browser to access your instance

21. Find the instance you just created and select it using the checkbox on the left of the table.
22. Find the IPv4 Public IP of your instance. Write that down or copy it to your clipboard.
23. Using a web browser, go to your instance and specify port 8787:

```
http://<YOUR-INSTANCE-IP>:8787/
```

24. You can log into your RStudio Server using the username "rstudio" and the password "rstudio".

### Using SSH to log into your instance

25. Now let's SSH into the instance you created.

Mac / Linux users:

* Open a terminal window.
* Using the location of the private half of your SSH key and the IPv4 Public IP you copied earlier, enter this command:

```ssh -i /where/is/your/key ubuntu@YOUR-PUBLIC-IP```

* Press RETURN. Accept the key signature of your instance. You should now be logged in.

Windows users:

* Open PuTTY
* In the "Host Name" field, log in as "ubuntu" with the IPv4 Public IP of your instance in this format: 
```ubuntu@YOUR-PUBLIC-IP```
* In the "Category" list expand SSH.
* Click "Auth" (don't expand it)
* In the "Private Key for Authentication" box, browse to the PPK file you created earlier.
* Click OPEN.
* Click YES to accept your instance's key signature. You should now be logged in.

- - -

26. You are now logged into your instance as the "Ubuntu" user, a regular user. 
27. You can now `sudo su` to become root, or run `sudo` commands.
28. For example, if you were to install a web server, run this command:

```bash
sudo apt-get -y install apache2
```

29. Then, visit your new web server's home page:

```
http://YOUR-INSTANCE-IP/
```

30. You should see the Apache welcome page.

- - -

31. BONUS - Stop your instance and start it.

32. BONUS - Stop your instance and resize it to another instance type. 

- - -

### Conclusion

Congratulations! You have successfully done the following in EC2:

* Logged into the AWS Console.
* Created or imported an SSH key pair.
* Created an EC2 instance.
* Customized an EC2 security group.
* Accessed your instance through a web browser.
* Accessed your instance via SSH.


# Resources

- [AWS Services in Plain English](https://www.expeditedssl.com/aws-in-plain-english): Translates Amazon's catchy trademark names into what the service _should have_ been called. 
- http://www.ec2instances.info/: Easy EC2 Instance Comparison 
- [Open guide to AWS services](https://github.com/open-guides/og-aws#readme): very informative, well-organized, and concise guide to AWS's key services.
