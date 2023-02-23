---
layout: default
title: ALS
nav_order: 4
has_children: true
permalink: als/
---

# FAQ - ALS
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---
## (For ICT257 students) What to do if `rht-vmctl reset <vmname>` does not achieve its intended objective and you are still stuck with a broken `<vmname>`?

Perform the following to revert to the original checkpoint:
1. Open Hyper-V Manager
2. Click on that particular VM
3. Under the checkpoints section, click on the “RESTORE HERE!” checkpoint
4. Click on Apply button on the right
![Apply button](images/als-vm-apply.jpg)
5. In this Apply Checkpoint prompt, click on Apply button.
![confirm apply](images/als-vm-apply1.jpg)
6. It will revert back to the default state and please try to start the virtual machine again.
