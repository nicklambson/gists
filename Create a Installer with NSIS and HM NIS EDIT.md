# Create a Installer with *NSIS* and *HM NIS EDIT*

------

## Introduction

**NSIS** (Nullsoft Scriptable Install System) is a professional open source system to create Windows installers. See https://nsis.sourceforge.io/Main_Page for more details.

**HM NIS EDIT** is a useful Editor for **beginners** to create installers with NSIS, allowing users to edit the generated script by the way they like. See http://hmne.sourceforge.net/ for more details.

------

## Installation

Download NSIS from [https://sourceforge.net/projects/hmne/ ](https://sourceforge.net/projects/hmne/)

Download HM NIS EDIT from [https://sourceforge.net/projects/hmne/ ](https://sourceforge.net/projects/hmne/)

**Make sure you have installed NSIS before installing the editor**

------

## Usage

Let's take the process of creating a Installer for Remove Hidden Formatting project as an example.

### Step 1:
Launch nisedit.exe, click on **File > New script from Wizard** to launch a generator. 

<img src="https://i.loli.net/2020/03/27/ZAmQdIpq27sOLvT.png" alt="1.png" style="zoom:50%;" />

<img src="https://i.loli.net/2020/03/27/wJi4qrO5elAY36j.png" alt="2.png" style="zoom:70%;" />



### Step 2: 
Delete the path if you don't have a license file.

<img src="https://i.loli.net/2020/03/27/qQmzEal69fuIBoU.png" alt="3.png" style="zoom:67%;" />



### Step 3: 
Delete the default files and add the Remove Hidden Formatting .exe file to it.

<img src="https://i.loli.net/2020/03/27/UVHus4rkJX89Boj.png" alt="4.png" style="zoom:80%;" />

<img src="https://i.loli.net/2020/03/27/adwKZn6rqcsTWXt.png" alt="5.png" style="zoom:60%;" />



### Step 4: 
Determine whether to create a shortcut based on your needs.

<img src="https://i.loli.net/2020/03/27/LAEGjpZqFY8SwzR.png" alt="6.png" style="zoom:80%;" />



### Step 5: 
Finished!

<img src="https://i.loli.net/2020/03/27/RqGbogM4nuAtWQP.png" alt="7.png" style="zoom:80%;" />

------

## FAQ

You need to modify the script for the following situations (Remember to compile the modified script):

### **Q1:** How to create an installer that does not require admin access?

**A1:** Add `RequestExecutionLevel user` to the file details:

![8.png](https://i.loli.net/2020/03/27/SnjuNKYhqXVBGbm.png)



### **Q2:** How to write a key to the registry during installation?

**A2:** Add either of the below lines of code in the `Section -Post` part of the code:  

Write it at the **User level** with :

- `WriteRegStr HKEY_CURRENT_USER "subkey" "key_name" "value"`

Write it at the **Root level** with:

- `WriteRegStr HKEY_CLASSES_ROOT "subkey" "key_name" "value"`

<img src="https://i.loli.net/2020/03/27/YuVaN35wXdUATx1.png" alt="9.png" style="zoom:150%;" />



### **Q3:** How to delete a key from the registry? (for uninstall purposes)

**A3:** Add this line in the `Uninstall` section:

- `DeleteRegKey "root_key" "subkey"`

![10.png](https://i.loli.net/2020/03/27/RgUBLATf9Yi2Dh5.png)

------


