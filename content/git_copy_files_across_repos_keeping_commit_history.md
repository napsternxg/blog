Title: Copy Commits Across Git Repositories Keeping Commit History
Date: 2022-09-15 10:20
Category: posts
Tags: git
Slug: git-copy-files-across-repos-keeping-commit-history
Authors: Shubhanshu Mishra
Summary: Copy Commits Across Git Repositories Keeping Commit History


Sometimes we would like to move files between two git repositories, namely, `repo1` to `repo2`. Here, both the repos do not share a commit history and may have a very different directory structure.

One use case is you are developing a standalone side project in `repo1` and would like later merge into a larger project `repo2`. 

One easy way is to simply copy files from `repo1` to `repo2` and then commit them in `repo2`. However, in this approach we loose all the commit history information of the files in `repo1`.

We can use a combination of `git format-patch` and `git am --3way` commands to achieve this. 

The key idea is to first export each commit in `repo1` as a patch file. Then apply these patches to `repo2`.

## Demo


### Setup Repositories

Let us setup 2 repositories. 

```bash
~$ git config --global user.email "you@example.com"
~$ git config --global user.name "Your Name"
~$ mkdir -p repo1 repo2
```

Setup `repo1`. 

```bash
~$ cd repo1/
~/repo1$ git init
Initialized empty Git repository in /home/user/repo1/.git/
~/repo1$ touch file1 file2
~/repo1$ echo "Hello World" > file1
~/repo1$ echo "Hello World again" > file2
~/repo1$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        file1
        file2

nothing added to commit but untracked files present (use "git add" to track)
~/repo1$ git add .
~/repo1$ git commit -am "Initial commit"
[master (root-commit) 6d58af8] Initial commit
 2 files changed, 2 insertions(+)
 create mode 100644 file1
 create mode 100644 file2
~/repo1$ git log
commit 6d58af8d140c86de700dd9206cb2c7512c39a74c (HEAD -> master)
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:48:01 2022 +0000

    Initial commit
```


Add few more commits:

```bash
~/repo1$ echo "New Lines Galore" >> file1
~/repo1$ cat file1
Hello World
New lines galore
~/repo1$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   file1

no changes added to commit (use "git add" and/or "git commit -a")
~/repo1$ git commit -am "Second commit"
[master 3f3c874] Second commit
 1 file changed, 1 insertion(+)
~/repo1$ git log
commit 3f3c874e3487d999c581cf2d2b75f49de2ab5784 (HEAD -> master)
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:48:49 2022 +0000

    Second commit

commit 6d58af8d140c86de700dd9206cb2c7512c39a74c
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:48:01 2022 +0000

    Initial commit 
```

Now setup `repo2`.

```bash
~/repo1$ cd ../repo2
~/repo2$ git init
Initialized empty Git repository in /home/user/repo2/.git/
~/repo2$ echo "This is file3 in new repo" > file3
~/repo2$ git add .
~/repo2$ git commit -am "File3"
[master (root-commit) ce65e35] File3
 1 file changed, 1 insertion(+)
 create mode 100644 file3
~/repo2$ git log
commit ce65e35e465dd5052c0c5f5a84e6ff35a856488d (HEAD -> master)
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:49:54 2022 +0000

    File3
```


### Exporting commits as patches

Now lets prepare the move from `repo1` to `repo2` keeping repo1 file history. 

First we will export each commit in repo1 as a patch in a temp directory called `~/repo1_patches`

```bash
~/repo2$ cd ../repo1
~/repo1$ mkdir ../repo1_patches
~/repo1$ git format-patch -o ../repo1_patches --root ./
../repo1_patches/0001-Initial-commit.patch
../repo1_patches/0002-Second-commit.patch
```

Now we will see what `~/repo1_patches` looks like.

```bash
~/repo1$ cd ../repo1_patches
~/repo1_patches$ ls -ltrh
total 2.0K
-rw-r--r-- 1 user user 367 Sep 16 02:50 0002-Second-commit.patch
-rw-r--r-- 1 user user 563 Sep 16 02:50 0001-Initial-commit.patch
```

These are the contents of `./0001-Initial-commit.patch`

```diff
From 6d58af8d140c86de700dd9206cb2c7512c39a74c Mon Sep 17 00:00:00 2001
From: Your Name <you@example.com>
Date: Fri, 16 Sep 2022 02:48:01 +0000
Subject: [PATCH 1/2] Initial commit

---
 file1 | 1 +
 file2 | 1 +
 2 files changed, 2 insertions(+)
 create mode 100644 file1
 create mode 100644 file2

diff --git a/file1 b/file1
new file mode 100644
index 0000000..557db03
--- /dev/null
+++ b/file1
@@ -0,0 +1 @@
+Hello World
diff --git a/file2 b/file2
new file mode 100644
index 0000000..c3aaa9d
--- /dev/null
+++ b/file2
@@ -0,0 +1 @@
+Hello World again
-- 
2.25.1
```

These are the contents of `./0002-Second-commit.patch`

```diff
From 3f3c874e3487d999c581cf2d2b75f49de2ab5784 Mon Sep 17 00:00:00 2001
From: Your Name <you@example.com>
Date: Fri, 16 Sep 2022 02:48:49 +0000
Subject: [PATCH 2/2] Second commit

---
 file1 | 1 +
 1 file changed, 1 insertion(+)

diff --git a/file1 b/file1
index 557db03..acab188 100644
--- a/file1
+++ b/file1
@@ -1 +1,2 @@
 Hello World
+New lines galore
-- 
2.25.1
```


### Applying patches as commits in new repo
Now that our patches are created, let us apply them sequentially to our new repo:


```bash
~/repo1_patches$ cd ../repo2
~/repo2$ git status
On branch master
nothing to commit, working tree clean
~/repo2$ git log
commit ce65e35e465dd5052c0c5f5a84e6ff35a856488d (HEAD -> master)
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:49:54 2022 +0000

    File3
~/repo2$ git am --3way ../repo1_patches/*.patch
Applying: Initial commit
Applying: Second commit
~/repo2$ ls -ltrh
total 3.0K
-rw-r--r-- 1 user user 26 Sep 16 02:49 file3
-rw-r--r-- 1 user user 18 Sep 16 02:53 file2
-rw-r--r-- 1 user user 29 Sep 16 02:53 file1
~/repo2$ git log
commit 3de485c1e24c555d53ede02ab6d52102ec7a2093 (HEAD -> master)
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:48:49 2022 +0000

    Second commit

commit 483f95d8944ef3b79cbb536dd0b68d9459abbfca
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:48:01 2022 +0000

    Initial commit

commit ce65e35e465dd5052c0c5f5a84e6ff35a856488d
Author: Your Name <you@example.com>
Date:   Fri Sep 16 02:49:54 2022 +0000

    File3
```

As we can see the commit history from `repo1` is now copied to `repo2` along with the files. 


## Epilogue

This is an easy fix when `repo1` is small and there is less likely to be a merge conflict between `repo1` and `repo2`. 
For more complex, you can add additional commits to move the files around.

