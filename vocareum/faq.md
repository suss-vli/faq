---
layout: default
title: 1. Vocareum
nav_order: 4
has_children: true
permalink: vocareum/
---

# FAQ - Vocareum

## 1. Disconnected from Vocareum Labs / Cannot access Vocareum Labs

For Vocareum labs, there is **a time limit of 5 hours** for each session. The session will be automatically disconnected once the 5 hours is up. 

You can check on the time left for your session from your work space, beside the “Start Lab” button (see image below). 

![Session Time](images/voc-session-time.png)

You can re-access your lab by closing the lab and starting a new lab session using the "End Lab" and "Start Lab" buttons. 


If the above method does not work, you can click on "Vocareum Lab" in Canvas to reload the Vocareum lab to start a new lab session.

![Start/End Lab](images/voc-canvas.png)


If you have concerns about your submission, click [here](#2-submission-deadline-rules) for more info.

---

## 2. Submission deadline rules


**Before deadline**
- Students are able to submit multiple times before the assignment deadline. 

**After deadline**
- Once the deadline is over, those who have at least 1 submission before deadline cannot submit again. 
- Those who have no submission before the deadline will only have 1 chance of submitting their assignment.

---

## 3. How do I upload my project to Vocareum?

**For VSCode IDE**

Simply drag and drop your directory into the explorer of IDE on Vocareum. See below.

![Upload project](images/upload.gif)

**For Jupyter Lab IDE**

To upload files to JupyterLab, click into the directory you wish to upload to. Click on the upload button and select the file to upload.

![Upload file on Jupyter](images/upload-jupyter.gif)

---

## 4. How do I download files from Vocareum?

**For VSCode IDE**

To download a single file, right click on the file and click on "Download".

![Download vscode](images/download-vscode1.png)

To download multiple files at one time, follow the steps below.

Step 1: Zip your files into an archive.

- Go into your Vocareum `desktop`.
- Put your files into a directory.
- Right click and select "Create Archive". 
- Select `zip` for the the "Archive Type" and click on "Create".

![zip](images/zip.png)

Step 2: Download via VSCode

- Go to the VSCode IDE.
- Right click on the zip file and select "Download"

![Download vscode](images/download-vscode.png)


**For JupyterLab IDE**

- Right click on the file you wish to download.
- Select "Download".

![Download Jupyterlab](images/download-juptyer.png)

---

## 5. Mongodb is disconnected. I am facing an error trying to reconnect Mongodb.

For a quick fix, run the following commands on your terminal.
```
cd /home/labsuser/dbfiles
rm -rfv WiredTiger.lock mongod.lock
sudo mongod --dbpath /home/labsuser/dbfiles --repair
```

Once you run the above commands, proceed to restart your lab by pressing “End Lab” on the top right corner of your workspace and press “Start Lab” to start it again.

![Start/End Lab](images/voc-start-end.png)


<details>
  <summary>Click for explanation.</summary>  
Usually when this happens, it means that the previous Mongodb run was not logged off properly and the lock file was not removed. The commands above try to remove hte lock file.

</details>

---

## 6. I forgot my password for my mongodb-compass keyring, what can I do?

Reset your password:
1. In Vocareum's terminal, run the command: `rm -rfv ~/.local/share/keyrings/Default_keyring.keyring` 
2. Close and re-launch mongodb-compass for the prompt to set the password for a new keyring. 
![mongodb-compass password prompt](images/mongodb-set-keyring.png)
3. Enter a new password for the keyring.

---