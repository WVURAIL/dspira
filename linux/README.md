# A Very Very Basic Linux Cheat Sheet

[Click here to download a cheat sheet](https://files.fosswire.com/2007/08/fwunixref.pdf) . It makes sense to save and print this for future reference *or* check below:

The most used and bare minimum one must know to survive within the command line:

| Command 	| Description |
|-----------|-------------|
|**man [command]** |	**Display the help information for the specified command.** |
|cd /directorypath |	Change to directory.|
|cp [options] | source destination 	Copy files and directories. |
|ls [options] |	List directory contents. |
|mv [options] source destination |	Rename or move file(s) or directories. |
|mkdir [options] | directory 	Create a new directory. |
|locate filename |	Search a copy of your filesystem for the specified filename. |
|pwd |	Display the pathname for the current directory. |
|rm [options] directory |	Remove (delete) file(s) and/or directories. |
|rmdir [options] directory |	Delete empty directories. |

use the ``man`` command to know about any command in detail

Other requently used commands:

| Command 	| Description |
|-----------|-------------|
|cat [filename] |	Display file’s contents to the standard output device (usually your monitor).|
|chmod [options] |mode filename 	Change a file’s permissions.|
|chown [options] |filename 	Change who owns a file.|
|clear |	Clear a command line screen/window for a fresh start. |
|date [options] |	Display or set the system date and time. |
|df [options] |	Display used and available disk space. |
|du [options] |	Show how much space each file takes up. |
|file [options] filename |	Determine what type of data is within a file. |
|find [pathname] [expression] |	Search for files matching a provided pattern. |
|grep [options] pattern [filesname] |	Search files or output for a particular pattern. |
|kill [options] pid |	Stop a process. If the process refuses to stop, use kill -9 pid. |
|less [options] [filename] |	View the contents of a file one page at a time. |
|ln [options] source [destination] |	Create a shortcut. |
|lpr [options] |	Send a print job. |
|passwd [name [password]] |	Change the password or allow (for the system administrator) to change any password. |
|ps [options] |	Display a snapshot of the currently running processes. |
|ssh [options] user@machine |	Remotely log in to another Linux machine, over the network. Leave an ssh session by typing exit. |
|su [options] [user [arguments]] |	Switch to another user account. |
|tail [options] [filename] |	Display the last n lines of a file (the default is 10). |
|tar [options] filename |	Store and extract files from a tarfile (.tar) or tarball (.tar.gz or .tgz). |
|top |	Displays the resources being used on your system. Press q to exit. |
|touch filename |	Create an empty file with the specified name. |
|who [options] |	Display who is logged on. |


# git it, git it good

## Get a copy of the repository 

- Open Terminal.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 2.

```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

- Press Enter. Your local clone will be created.

```
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Get updated changes from git

- Open Terminal.
- Change the current working directory to the location of your directory.

```
git pull
```

## Some unspoken rules

- Any files in the repository that you change should be copied to another location *before* making any changes


- 
