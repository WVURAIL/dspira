---
layout: post
date:   2020-08-22
title: "The Command Line and Git"
summary:  The handful of Linux commands and git steps the rest of these lessons assume you already know
tags: ['School-Teachers', 'Students', 'Hobbyists' ]
categories: ['Software Setup']
order: 3
permalink: /CommandLine_and_Git/
---

Several lessons here open a terminal and start typing. If that is unfamiliar
territory, this is the short version — enough to follow the rest without being a
Linux course.

Nothing here is specific to radio astronomy. Skip it if you already live in a
terminal.

## The ones you actually need

| Command | What it does |
|---|---|
| **`man [command]`** | **Show the manual for a command. The one to remember — every command below has a manual page.** |
| `pwd` | Where am I? |
| `ls [options]` | What is in here? |
| `cd /directorypath` | Go somewhere |
| `mkdir directory` | Make a directory |
| `cp source destination` | Copy |
| `mv source destination` | Move, or rename |
| `rm [options] file` | Delete a file. There is no undo and no recycle bin. |
| `rmdir directory` | Delete an empty directory |
| `locate filename` | Find a file by name |

## The next ones you meet

| Command | What it does |
|---|---|
| `cat [filename]` | Print a file to the screen |
| `less [filename]` | Read a file one page at a time. `q` to quit. |
| `tail [filename]` | The last 10 lines — useful for logs |
| `head [filename]` | The first 10 lines |
| `grep pattern [file]` | Find lines matching a pattern |
| `find [path] [expression]` | Find files matching a pattern |
| `file filename` | What kind of file is this? |
| `chmod mode filename` | Change a file's permissions |
| `chown owner filename` | Change who owns a file |
| `df [options]` | How much disk is left |
| `du [options]` | How much space is this using |
| `free -m` | How much memory is in use |
| `top` | What is running. `q` to quit. |
| `ps [options]` | A snapshot of running processes |
| `kill pid` | Stop a process. `kill -9 pid` if it will not go. |
| `date` | The system date and time |
| `touch filename` | Create an empty file |
| `clear` | Clear the screen |
| `ssh user@machine` | Log in to another machine. `exit` to leave. |
| `tar [options] filename` | Pack and unpack `.tar`, `.tar.gz`, `.tgz` |
| `passwd` | Change a password |
| `su [user]` | Switch user |
| `who` | Who is logged in |

There are printable one-page versions of this all over the internet. Search for
"Linux command cheat sheet", print one, and put it next to the telescope.

---

## Git, enough to keep the software updated

Most of what these lessons ask of git is "get a copy" and "get the updates".

## Get a copy of a repository

Open a terminal, move to wherever you want the copy to live, and:

```bash
git clone https://github.com/WVURAIL/gr-radio_astro.git
```

That makes a directory named after the repository, containing everything.

## Get the updates

Move into that directory and:

```bash
git pull
```

### One rule worth following

**If you change a file in a cloned repository, copy your version somewhere else
before you pull.** Otherwise git has to reconcile your edits with the incoming
ones, and that is a conversation you did not want to have today.

### When `git pull` refuses

You will eventually see this:

```
Updating d0ebfc5..0b10e81
error: Your local changes to the following files would be overwritten by merge:
	examples/spectrometer_w_cal.grc
Please commit your changes or stash them before you merge.
Aborting
```

git has noticed you changed a file and will not overwrite your work without being
told to. If you want to keep your changes, copy the file elsewhere first. Then:

```bash
git stash
```

which puts your changes aside so the pull can proceed.

The first time you run that, git may stop and ask who you are:

```
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```

Do exactly that, with your own name and email, then run `git stash` and
`git pull` again.

## Updating the GNU Radio blocks

The full sequence for picking up new versions of `gr-radio_astro`:

```bash
cd gr-radio_astro
git pull
cd build
cmake ..
make
sudo make install
```

The [installation lesson]({{ site.baseurl }}/gr_radio_astro_Installation) covers
the first install, including what to do when `cmake` cannot find something.

## If you want to go further

* [Pro Git](https://git-scm.com/book/en/v2) — the standard book, free online
* [GitHub's Get Started guides](https://docs.github.com/en/get-started)
