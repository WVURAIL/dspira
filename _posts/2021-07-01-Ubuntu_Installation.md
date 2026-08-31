---
layout: post
date:  2023-06-27
title: Installing Ubuntu
summary:  Details for partitioning a hard drive and installing Ubuntu OS on a Windows computer
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 4
---

  *Our software works under Ubuntu versions 22.04 LTS and older.*

Installing the Ubuntu OS on a Windows computer will require you to partition the hard drive, copy Ubuntu OS onto a bootable flashdrive, and install it onto the partition, as follows:

**A. Partition a Hard Drive** - Before installing Ubuntu on the hard disk, you need to partition the hard disk in Windows.

   NOTE: A hard drive with at least 250 GB is recommended.
   
   Before proceeding, check that Device Encryption is OFF. (This is also known as Bitlocker.) For most Windows systems, this can be done as follows:
   * Boot up the computer in Windows.
   * Open the *Start* menu.
      * In the search box type "encryption".
      * In the menu that pops up, click on *Manage Bitlocker*.
      * Verify that it is off and turn off if needed.
      * If it was on and you turn it off, you will need to wait until Windows has completed un-encrypting the hard drive before you can proceed. This could take some time.

   Now you are ready to partition the hard drive.
   
   1. Open a Command Prompt window with admin rights, as follows:
         - In the search field, type `Command Prompt`, or just CMD.
         - Click on *Run as Administrator* from the selections on the right side of the window that pops up.
         - Click *Yes* on the pop-up to allow the app to make changes to your device.
         
   2. In the Command Prompt window that pops up, enter the command `diskmgmt.msc` to open the Disk Management utility.

   3. In the Disk Management window, right click on *OS (C:)* and select the *Shrink Volume* option in order to reduce the partition size.

   4. Wait for the system to query partition size data; then enter the desired amount of space you want to shrink, and hit in the *Shrink* button. The amount chosen to shrink will be the amount that will be allotted to Ubuntu. This should be an absolute minimum of 50 GB; we recommend at least 100 GB.
      
   After the shrink process completes, a new unallocated space will be present in your drive. We’ll use this free space to install Ubuntu alongside Windows, as described below. 

**B. Download Ubuntu 22.04 onto a Bootable Flashdrive**

   1. You need to [download Ubuntu Desktop 22.04 ISO](http://releases.ubuntu.com/22.04/){:target="_blank"} onto the hard drive in Windows. You want to choose the Desktop version. It will take some time to download this file.
      
   2. Download [BalenaEtcher](https://etcher.balena.io/){:target="_blank"} for Windows and install it if you don’t already have it.

   3. Install a 32 GB or larger flash drive in the usb port.
   
   4. Run *BalenaEtcher*. Choose the Ubuntu 22.04.iso file as the image and the flash drive as the target. It will take some time for this to run.
     
**C. Install Ubuntu 22.04 Alongside Windows**

   1. Turn off the computer. Place the bootable flash drive in the USB port. Turn on the computer, holding down the bootable key (F12) in order to boot from the Ubuntu USB bootable image.

   2. On the first installation screen, select *Install Ubuntu* and hit Enter to start the installation process. Complete the prompts as needed.

   3. After the installation is complete, you will restart the computer. Choose the Ubuntu option from the menu that appears.

   4.  **Check the date and time** displayed on your computer. If it is not correct, it must be corrected in order for the installation to be completed successfully. This can be changed in the *Date & Time* menu under *Settings*.

   5. Open a *Terminal* window. This can be found in the *Show Applications* waffle in the lower left corner of the screen.

      **NOTE:** Most of the commands we use are entered in a *Terminal* window. We recommend adding the *Terminal* to your Favorites to be accessed easily.
   
   6. With the time being correct, in a *Terminal* window type and enter `sudo apt update`. Then type and enter `sudo apt upgrade`. This will bring the Ubuntu installation up to date. 

 The Ubuntu OS is now ready to use.
