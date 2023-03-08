---
layout: default
title: Vocareum
nav_order: 4
has_children: true
permalink: vocareum/
# has_toc: true
---
# FAQ - Vocareum
{: .no_toc }
If your issue cannot be resolved by any of the FAQ, please email <vlisupport@suss.edu.sg> for assistance.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Browser requirements and configurations

  **Google Chrome**
  
  1. Update the web browser to the latest version. 
  2. System Requirements (Please refer [here](https://support.google.com/chrome/a/answer/7100626) for the latest information): <br>
     a. Windows <br>
        &emsp;i. Windows 7, Windows 8, Windows 8.1, Windows 10 or later <br>
        &emsp;ii. An Intel Pentium 4 processor or later that’s SSE3 capable <br>
     b. MAC OS <br>
        &emsp;i. macOS High Sierra 10.13 later <br>
     c. Linux OS <br>
        &emsp;i. 64-bit Ubuntu 18.04+, Debian 10+, openSUSE 15.2+, or Fedora Linux 32+ <br>
        &emsp;ii. An Intel Pentium 4 processor or later that's SSE3 capable <br>
  3. Configure browser to allow third-party cookies from Vocareum. The screenshots provided at the time of writing is based on version `109.0.5414.75`. <br>
      a. Open Chrome browser. <br>
      b. On the URL bar, enter  `chrome://settings/cookies`

      ![Cookies](images/settings-cookies.png)

      c. Scroll down the page until you see this section – **Sites that can always use cookies** and click on the **Add** button.

      ![Cookies](images/cookies-add.png)

      d. In the **Add a site box**, enter `[*.]labs.vocareum.com` into the Site prompt and check **Including third-party cookies on this site**.

      ![Add Vocareum labs](images/add-voc.png)

      e. Click Add button to add and the prompt box will close.

      ![Add site](images/add-site.png)

      f. You will notice that your entry is now displayed at this section.

      ![Check](images/check-site.png)
         
      g. Restart your Chrome browser and you should be able to access Vocareum Labs now.

---

## Blank screen on Safari browser while accessing Vocareum Labs

  Students who are using Safari browser on their MAC may encounter this issue where a blank screen will appear after clicking on Vocareum Labs on Canvas (see image below).

  ![Blank screen](images/blank-screen2.png)

  To solve the issue:

  1. Click on **Safari**, then select **Preferences**.
  
     ![Preferences](images/preferences.png)
     
  3. From the **Preferences** window, click on **Privacy**.
  4. Under Website tracking setting, uncheck the **Prevent cross-site tracking** option.
  
     ![Safari settings](images/safari-settings.png)
  4. Close the prompt box.
  5. Refresh the Safari browser page.

---

## Desktop Screensaver Password

  For users who come across the virtual desktop screensaver and need the password to unlock it, the password is `labsuser`.

  ![Screensaver password](images/screensaver.png)

---

## Black Box appearing on Virtual Desktop

  If you have selected **One empty panel** on the Panel Prompt as shown below, you will get a black box on the desktop.
  
  ![Black_box](images/black-box.png)
  
  To resolve this issue:
  
  1. Right-click on an empty space on the desktop and click **Open Terminal Here** from the menu.
  2. Once the terminal appears, enter the following command:
      ```
      rm -rf ~/.config/xfce4/
      ```
  3. Navigate back to **Work Workspace** and click **End Lab**
  4. Click **Start Lab** to start the lab again.
  5. Once the lab starts, remember to choose **Use default config**

---

## Virtual desktop connection lost

  Possible scenarios:
  1. Your virtual desktop connection suddenly gets lost, and you are unable to re-connect back to your virtual desktop.
     A sample of the error is shown below.
     
     ![Connection lost](images/novnc-disconnect.png)

  2. The noVNC loading is stuck at the connecting loop indefinitely.

  To resolve these issues:
  
  a. Close the noVNC browser tab.<br>
  b. Navigate back to the **Work Workspace** and end the current session by clicking **End Lab**.<br>
  c. Click on **Start Lab** to obtain a new session.<br>
  
  ![Start/End Lab](images/start-end.png)

---

## Disconnected from Vocareum Labs / Cannot access Vocareum Labs

  For Vocareum labs, there is **a time limit of 5 hours** for each session. The session will be automatically disconnected once the 5 hours is up. You can check on the time left for your session from your work space, beside the “Start Lab” button (see image below).
  
  ![Session Time](images/sessiontime.png)
  
  You can re-access your lab by closing the lab and starting a new lab session using the "End Lab" and "Start Lab" buttons.

  If the above method does not work, you can click on "Vocareum Lab" in Canvas to reload the Vocareum lab to start a new lab session.

  ![Start/End Lab](images/voc-canvas.png)

---

## Failed to launch Lab

  If one of the following error message appears after clicking **My Work**, please close the message and click **Start Lab** again. The lab session will be able to start as soon as it has completed loading.

   ![Timeout on lab](images/timeout-lab1.png)
   ![Fail to launch tab](images/timeout-lab2.png)
   ![Fail to launch tab](images/timeout-lab3.png)

---

## Unable to login to MongoDB Compass due to incorrect keyring

  To reset your password:
  1. Open a terminal in the virtual desktop.
  2. Run the command:
     ```
     rm -rfv ~/.local/share/keyrings/Default_keyring.keyring
     ```
  3. Close the MongoDB compass application.
  4. Re-launch the MongoDB compass application. Accept the default and click **Connect**
  5. The prompt to set the password for a new keyring will appear.
  
     ![mongodb-compass password prompt](images/mongodb-set-keyring.png)
  6. Enter a new password for the keyring.

---

## MongoDB is disconnected. I am facing an error trying to reconnect MongoDB.

  For a quick fix, run the following commands on your terminal.
  ```
  cd /home/labsuser/dbfiles
  rm -rfv WiredTiger.lock mongod.lock
  sudo mongod --dbpath /home/labsuser/dbfiles --repair
  ```
  Once you run the above commands, proceed to restart your lab by pressing “End Lab” on the top right corner of your workspace and press “Start Lab” to start it again.
  ![Start/End Lab](images/start-end.png)

<details>
  <summary>Click for explanation.</summary>  
  Usually when this happens, it means that the previous Mongodb run was not logged off properly and the lock file was not removed. The commands above try to remove the lock file.
</details>

---

## Copy/Paste text from Local Desktop to Virtual Desktop

  1. Use Crtl + C keyboard shortcut to copy the text from your local desktop.
  2. Navigate to your virtual desktop and click on the arrow to open the noVNC control panel.
  
     ![Open noVNC control panel](images/novnc-control.png)
  3. Click on the **Clipboard** button on the noVNC control panel to open the Clipboard.
  
     ![Open noVNC clipboard](images/novnc-clipboard.png)
  4. Use Ctrl + V keyboard shortcut to paste the text into the Clipboard.
  5. In your virtual desktop, **right-click** on your mouse and click **Paste** to paste the contents on the application.

     ![Paste contents](images/paste-virtual-desktop.png)
     ![Paste contents](images/paste-virtual-desktop2.png)
  6. Click the arrow on the noVNC control panel to hide it.
  
     ![Close panel](images/close-novnc.png)

---

## Copy/Paste text from Virtual Desktop to Local Desktop

  1. Highlight the text you want to copy to the local desktop.
  
     ![Highlight text](images/highlight-text.png)
  2. Click on the arrow on the left to open the noVNC control panel.
  3. Click on the **Clipboard** button on the noVNC control panel to display the Clipboard.
  
     ![Open noVNC clipboard](images/display-clipboard.png)
  4. Use the Ctrl + C keyboard shortcut to copy the text in the Clipboard.
  5. Use the Ctrl + V keyboard shortcut to paste the text in your local desktop.

---

## Copy/Paste text from Local Desktop to Cloud IDE/JupyerLab

  1. Use the Ctrl+C keyboard shortcut to copy the text from your Local Desktop.
  2. Use the Ctrl+V keyboard shortcut to paste the text to the Cloud IDE/JupyterLab.

---

## Copy/Paste text from Cloud IDE/JupyerLab to Local Desktop

  1. Use the Ctrl+C keyboard shortcut to copy the text from the Cloud IDE/JupyterLab.
  2. Use the Ctrl+V keyboard shortcut to paste the text to your Local Desktop.


## How do I download files from Vocareum to my Local Desktop?

### Downloading from VSCode IDE

1. Select the file(s) that you wish to download.
2. To select multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue.
  
   ![Select files](images/select-file.png)

3. Right click on the selected file(s) and click on **Download**.

   ![Download vscode](images/download-file.png)

4. If there is a prompt appearing on your screen to ask for your permission, click **Allow**.
  
    ![Allow multiple file download](images/allow-multiple.png)

5. Verify that the file(s) have been downloaded to your computer.

   ![Verify download](images/verify-download.png)


### Downloading from JupyterLab IDE

1. Select the file(s) that you wish to download.
2. To select multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue.

    ![Select files](images/select-file-jupyter.png)

3. Right click on the selected file(s) you wish to download.
4. Select "Download".

    ![Download Jupyterlab](images/download-file-jupyter.png)


### Downloading from Virtual Desktop

1.	Navigate to **Work WorkSpace** and click the **Reload** icon <u>once</u> to reload the file tree. This step will reload the contents of the work folder.

    ![Reload](images/reload-workspace.png)

2. Click on the file/folder that you wish to download.

    ![Select file on file tree](images/file-tree-select.png)

{: .important } If you have multiple files/folders to download, you must do it one by one. The recommended way would be to zip up the files/folders into 1 zip file and you download the single zip file.

3. Click on the **Download** icon button.

    ![Download icon](images/file-tree-download.png)

4. The system will automatically compress the selected file/folder into a zip file. Click **Download zipped source** to download the file.

    ![Download zip](images/download-zipped-source.png)

---

## How do I upload my project to Vocareum?

### Uploading to VSCode IDE

<u>Method 1</u>

Simply drag and drop your directory into the explorer of IDE on Vocareum. See below.

![Upload project](images/upload.gif)

<u>Method 2</u>

1. Navigate to the directory where you wish to upload your file(s).
2. **Right-click** on an empty area on the file explorer, click **Upload** and select the file(s) that you wish to upload.

   ![Upload file](images/upload-vscode.png)

3. To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

   ![Upload file](images/upload-open.png)

4. Once upload is completed, you can find the file(s) listed under the directory in your IDE.

   ![Upload complete](images/upload-complete.png)

### Uploading to JupyterLab IDE

1. Navigate into the directory you wish to upload to. 
2. Click on the **Upload** icon button and select the file to upload. 
3. To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

     ![Upload file on Jupyter](images/upload-jupyter.gif)

### Uploading to Virtual Desktop

1. Navigate to **Work Workspace** and click on **work**.

   ![Navigate workspace](images/upload-desktop.png)

2. Click on **Upload** button.

   ![Navigate workspace](images/upload-desktop2.png)

3. To upload multiple files, hold down on the `Control` button (for Windows) on the keyboard and select the files one by one. The selected files will be highlighted in blue. Click **Open** to upload.

    ![Select files](images/upload-desktop3.png)

4. System will start to process the upload and will prompt successful when completed.

    ![Uploading](images/upload-status.png)

5. Verify that your files have successfully uploaded from the file tree or in your Virtual Desktop.

    ![Verify upload](images/verify-upload.png)

---
