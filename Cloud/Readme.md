# Cloud Project

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSETUE46G7gv41P7dFD5i4VQ_TAgV_FIcS4Kg&usqp=CAU" width="400" height="400">


### Basic Git Workflow

Each member will work on their branch and pull request and merge to **develop** if no conflicts arise.

If conflicts arise speak to manager.

> **Warning**
> La rama **main** no se toca.


### Important git concepts

Each team member will initially clone develop branch and work on features.

The first exercise will walk you through in how to initially set up your environment.

### First Exercise:

1. Create a folder in your computer : Cloud_Project
2. Open terminal and go inside folder Cloud_Project

~~~
git clone -b develop https://github.com/IgnacioGB1990/Cloud_Members.git
~~~

3. Create your own branch and move to it:
~~~
git checkout -b "my_name"
~~~


4. Create folder with your name **inside folder members** and add readme.md with your github url (see my example)
~~~
git add .
~~~

~~~
git commit -m "my_name added github url"
~~~

~~~
git push --set-upstream origin "my_name"
~~~

### Basic git workflow

<img src="https://static.packt-cdn.com/products/9781782168454/graphics/8454OS_01_4.jpg" width="600" height="400">

### Basic Git Commands

Check status of files:
~~~
git status
~~~

Add all files to staging area prior to commit:
~~~
git add .
~~~

Add commit :
~~~
git commit -m "First Commit"
~~~

Add file to staging area and commit :
~~~
git commit -am "Two in one command"
~~~

Push changes to Github
~~~
git push
~~~

Pull any changes done remotely and update them into your local directory:

~~~
git pull
~~~

#### Branches

Creates and moves to branch:

~~~
git checkout -b "Name_of_new_branch"
~~~

Move to existing branch:

~~~
git checkout "name_of_existing_branch"
~~~

See existing branches:
~~~
git branch
~~~



## Members:

* Silvia
* Ricardo
* Alberto
* Tony
* Nacho

