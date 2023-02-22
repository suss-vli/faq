---
layout: default
title: Vocareum
nav_order: 4
has_children: true
permalink: vocareum/
---

# FAQ - Vocareum

## 1. Browser requirements and configurations

**Google Chrome**

- Update the web browser to the latest version. 
- System Requirements (Please refer [here](https://support.google.com/chrome/a/answer/7100626) for the latest information):  
  - Windows 
    - Windows 7, Windows 8, Windows 8.1, Windows 10 or later 
    - An Intel Pentium 4 processor or later that’s SSE3 capable 
  - MAC OS 
    - macOS High Sierra 10.13 later 
  - Linux OS 
    - 64-bit Ubuntu 18.04+, Debian 10+, openSUSE 15.2+, or Fedora Linux 32+ 
    - An Intel Pentium 4 processor or later that's SSE3 capable 
- Configure browser to allow third-party cookies from Vocareum. The screenshots provided at the time of writing is based on version `109.0.5414.75`. 
  - Open Chrome browser. 
  - On the URL bar, enter  `chrome://settings/cookies` 
    ![Cookies](images/settings-cookies.png)
  - Scroll down the page until you see this section – **Sites that can always use cookies** and click on the **Add** button.
    ![Cookies](images/cookies-add.png)
  - In the **Add a site box**, enter `[*.]labs.vocareum.com` into the Site prompt and check **Including third-party cookies on this site**.
    ![Add Vocareum labs](images/add-voc.png)
  - Click Add button to add and the prompt box will close.
    ![Add site](images/add-site.png)
  - You will notice that your entry is now displayed at this section.
    ![Check](images/check-site.png)
  - Restart your Chrome browser and you should be able to access Vocareum Labs now.
    
---

## 2. Disconnected from Vocareum Labs / Cannot access Vocareum Labs

For Vocareum labs, there is **a time limit of 5 hours** for each session. The session will be automatically disconnected once the 5 hours is up. 

You can check on the time left for your session from your work space, beside the “Start Lab” button (see image below). 

![Session Time](images/voc-session-time.png)

You can re-access your lab by closing the lab and starting a new lab session using the "End Lab" and "Start Lab" buttons. 


If the above method does not work, you can click on "Vocareum Lab" in Canvas to reload the Vocareum lab to start a new lab session.

![Start/End Lab](images/voc-canvas.png)


If you have concerns about your submission, click [here](#2-submission-deadline-rules) for more info.

---

## 3. Submission deadline rules


**Before deadline**
- Students are able to submit multiple times before the assignment deadline. 

**After deadline**
- Once the deadline is over, those who have at least 1 submission before deadline cannot submit again. 
- Those who have no submission before the deadline will only have 1 chance of submitting their assignment.

---

## 4. How do I download files from Vocareum?

### Downloadinng from VSCode IDE

- Select the file(s) that you wish to download.
- To select multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue.
  
  ![Select files](images/select-file.png)

- Right click on the selected file(s) and click on **Download**.

  ![Download vscode](images/download-file.png)

- If there is a prompt appearing on your screen to ask for your permission, click **Allow**.
  
  ![Allow multiple file download](images/allow-multiple.png)

- Verify that the file(s) have been downloaded to your computer.

  ![Verify download](images/verify-download.png)


### Downloading from JupyterLab IDE

- Select the file(s) that you wish to download.
- To select multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue.

    ![Select files](images/select-file-jupyter.png)

- Right click on the selected file(s) you wish to download.
- Select "Download".

    ![Download Jupyterlab](images/download-file-jupyter.png)


### Downloading from Virtual Desktop

-	Navigate to **Work WorkSpace** and click the **Reload** icon <u>once</u> to reload the file tree. This step will reload the contents of the work folder.

    ![Reload](images/reload-workspace.png)

- Click on the file/folder that you wish to download.

    ![Select file on file tree](images/file-tree-select.png)

**NOTE**: If you have multiple files/folders to download, you must do it one by one. The recommended way would be to zip up the files/folders into 1 zip file and you download the single zip file.

- Click on the **Download** icon button.

    ![Download icon](images/file-tree-download.png)

- The system will automatically compress the selected file/folder into a zip file. Click **Download zipped source** to download the file.

    ![Download zip](images/download-zipped-source.png)


---


## 5. How do I upload my project to Vocareum?

### Uploading to VSCode IDE

<u>Method 1</u>

Simply drag and drop your directory into the explorer of IDE on Vocareum. See below.

![Upload project](images/upload.gif)

<u>Method 2</u>

- Navigate to the directory where you wish to upload your file(s).
- **Right-click** on an empty area on the file explorer, click **Upload** and select the file(s) that you wish to upload.

  ![Upload file](images/upload-vscode.png)

- To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

  ![Upload file](images/upload-open.png)

- Once upload is completed, you can find the file(s) listed under the directory in your IDE.

  ![Upload complete](images/upload-complete.png)

### Uploading to JupyterLab IDE

- Navigate into the directory you wish to upload to. 
- Click on the **Upload** icon button and select the file to upload. 
- To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

  ![Upload file on Jupyter](images/upload-jupyter.gif)

### Uploading to Virtual Desktop

- Navigate to **Work Workspace** and click on **work**.

  ![Navigate workspace](images/upload-desktop.png)

- Click on **Upload** button.

  ![Navigate workspace](images/upload-desktop2.png)

- To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

  ![Select files](images/upload-desktop3.png)

- System will start to process the upload and will prompt successful when completed.

  ![Uploading](images/upload-status.png)

- Verify that your files have successfully uploaded from the file tree or in your Virtual Desktop.

  ![Verify upload](images/verify-upload.png)

---

## 6. Mongodb is disconnected. I am facing an error trying to reconnect Mongodb.

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

## 7. I forgot my password for my mongodb-compass keyring, what can I do?

Reset your password:
1. Open a terminal in the virtual desktop. 
2. run the command: 

    `rm -rfv ~/.local/share/keyrings/Default_keyring.keyring` 

3. Close MongoDb compass application
4. Re-launch the MongoDB compass application, accept the default and click **Connect**

5.  The prompt to set the password for a new keyring will appear.

    ![mongodb-compass password prompt](images/mongodb-set-keyring.png)

6. Enter a new password for the keyring.


---