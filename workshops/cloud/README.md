# Introduction to Cloud - Workshop

In this workshop you will learn the basic functionality of two of the most foundational services offered by AWS: S3 storage and EC2 compute. Follow the lab instructions below at your own pace. Please raise your hand or get the attention of an instructor if you have any questions.

* S3 Operations
  * [Working with buckets using the web UI](#create-a-bucket-in-s3).
  * [Working with buckets using the CLI](#s3-commands-in-the-aws-command-line-tools).
  * [Using an S3 bucket as a static website](#create-a-public-html-website-in-amazon-s3).
* EC2 Operations
  * [Creating or setting up an SSH keypair](#set-up-ssh-keypairs).
  * [Launching an EC2 compute instance](#launch-an-ec2-instance).
  * [Bootstrapping an EC2 instance for launch](#bootstrapping-your-instance).
  * [Using a web browser to access your instance](#using-a-web-browser-to-access-your-instance).
  * [Using SSH to log into your instance](#using-ssh-to-log-into-your-instance).

- - -

## S3 - Simple Storage Service

### Create a Bucket in S3
1. Log into the **AWS Console** using the account you set up before the workshop.
2. From the SERVICES tab in the upper-left corner, select the **S3** service.
3. Click **Create Bucket**. Note that you are not charged for creating a bucket, only for storing objects in that bucket.
4. A dialogue box will open. Enter a unique **Bucket Name** in the box.
5. Accept the default region and click **Create**.

### Adding an Object to S3
6. In the Amazon S3 console, click on the name of the bucket that you just created.
7. Click **Upload**. The Upload wizard will appear.
8. Click **Add Files**, or you can simply drag and drop files into the wizard. You may also drag entire folders if you wish. For this example, try adding an image or PDF file.
9. If you add a file that you do not want to upload, click the `X` to the right of the file name to remove it.
10. Once you have selected the appropriate files and folders to upload, click either **Upload** to complete the process, or click **Next** if you want to modify any details for your file upload(s). For this example, select **Next**.
11. If you selected **Next**, one option is to manage permissions for public users. If, for example, you wanted to make an individual file available to the public, you would open the "Manage public permissions" section and select "Read" in the "Objects" column for the "Everyone" group. Do not modify any of the object permissions settings. Then click **Next** to advance.
12. The next set of options relates to other file properties, such as storage class and encryption. Review these options and then click **Next** again.
13. Finally, review your uploads on the last pane and select **Upload** when ready. You will be able to see the progress of your upload(s).

### View Object Details in S3
14. Within the bucket that you created earlier, find a file that you uploaded in the last step.
15. Select the file by checking the box to the left. A properties pane will appear on the right of your screen.
16. Note details about your file, such as size, owner, last write date, and the link to your file. Copy the link to your object.
17. In a new browser window or tab, paste the file link and try to view it. If successful, close your tab. If not, please talk to one of the instructors.

### Delete a file in S3
18. With your file still selected in the S3 Console, select the "More" menu. Note the options available to you.
19. Select "Delete" and confirm your choice.

- - -

### S3 commands in the AWS Command-Line Tools
20. Install the AWS CLI in your terminal. Visit https://aws.amazon.com/cli/ for more instructions for your platform.
21. Setup your AWS CLI by running `aws configure` in your terminal.
22. Follow the setup instructions, and paste in your AWS Secret and AWS Secret Key.
23. To work with S3, use the `aws s3` command. For example, to get help:

```bash
aws s3 help
```

24. List your buckets

```bash
aws s3 ls
```

25. Make another bucket

```bash
aws mb s3://my-bucket
```

26. List the contents of a bucket

```bash
aws ls s3://my-bucket/                     # Displays the base contents of a bucket
aws ls s3://my-bucket/and-folder/          # Displays the contents of a subdir
aws ls s3://my-bucket/and-folder/*.png     # Displays all PNG files in the subdir
```

27. Copy an object into S3

```bash
aws s3 cp my-local-file.zip s3://my-bucket/          # Copies a file into a bucket
aws s3 cp my-local-file.zip s3://my-bucket/subdir/   # Copies a file into a subdir of a bucket
aws s3 cp s3://my-bucket/file.zip ./                 # Copies a file from a bucket
```

28. Remove a file from S3

```bash
aws s3 rm s3://my-bucket/subdir/my-file.zip   # Removes the file (called a 'key') from S3
```

29. Synchronize a local folder with S3

```bash
aws s3 sync myfolder s3://my-bucket/myfolder/   # Syncs local folder's contents up to S3
aws s3 sync s3://my-bucket/myfolder/ myfolder   # Syncs remote S3 folder down to local folder
```

- - -

BONUS - Presign a S3 URL

If you have a file that is stored privately, you can "presign" it with an expiration time to share with others.

```
aws s3 presign --expires-in 60 s3://my-bucket/file.pdf   # Presigns a URL that expires in 60 seconds
```

Try the URL in your browser immediately after creating it, then try it after it should expire.

- - -

### Create a Public HTML Website in Amazon S3
30. Open the Amazon S3 console in your browser.
31. Click on the name of a bucket you created in earlier steps. This bucket will hold your public website.
32. You should see four panel options for your bucket: **Objects**, **Properties**, **Permissions**, and **Management**.
33. Select the **Permissions** panel for your bucket.
34. You are going to set a permissions policy for your bucket. This is a set of rules that will be applied to every object you upload to your bucket.
35. Select the **Bucket Policy** button near the top.
36. In the text editor area, paste the following code. Be sure to update **YOUR-BUCKET-NAME** with the actual name of your bucket. (Also, do not update the Version date, as it applies to the policy framework and not your actual policy itself.)

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"AddPerm",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::YOUR-BUCKET-NAME/*"]
    }
  ]
}
```
Take a moment to review this JSON policy. Note that the one statement in it adds a permission, allowing any user (*) to get objects within a specific bucket, specified by a resource ARN. (ARN stands for Amazon Resource Name.)
Click **Save** to save the custom policy.

37. Next, go to the **Properties** pane for your bucket. Select the **Static website hosting** option.
38. Select the radio button indicating you want to use this bucket to host a website. Specify an index document (`index.html` is the usual index document for websites.) Then click **Save**.
39. Then select the **Objects** tab of your bucket. You will need to upload an `index.html` file now. Feel free to write one yourself if you know HTML, or [download one here](https://s3.amazonaws.com/uvasom-resources/courses/index.html) and then upload it to your bucket.
40. You have now created a bucket, dropped an `index.html` file into it, set the bucket policy to be publicly readable, and set the bucket to serve as a website. The last step is to visit your website! Return to your bucket's properties tab, and select the "Static Website Hosting" button again. At the top you will find an "Endpoint" address. This is the URL to your website. Click it.

### Conclusion

Congratulations! You have successfully done the following in S3:

* Logged into the AWS Console.
* Created a storage bucket.
* Uploaded a file to your bucket.
* Accessed details about that file.
* Adjust permissions for a file and make it publicly visible.
* Accessed the file via a web browser.
* Deleted a file from your bucket.
* Used the AWS CLI to perform some of the same functions from the command-line.
* Modified your bucket to serve as a static website.
* Set a bucket policy so that objects are visible to the public.
* Created an index.html bucket for your website.
* Visited your website and verified it works.

- - -

## EC2 - Elastic Compute Cloud

1. Log into the **AWS Console** using the account you set up before the workshop.
2. From the SERVICES tab in the upper-left corner, select the **EC2** service.
3. Verify your region. EC2 instances can be placed within various regional locations around the world. For today's workshop please make sure that the OREGON region is selected for your region by checking the upper-right corner of your screen. This region is also known as US-West-2.

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
http://YOUR-INSTANCE-IP:8787/
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
