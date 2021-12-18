# Algorithms
Project that implements algorithms for a few problems.

# Todo
1. Knapsack problem:
   - Brute Force
   - Dynamic Algorithm
2. Travelling Salesman Problem:
   - Brute Force
   - Dynamic Algorithm
3. Miscellaneous:
   - Implement program that runs every implemented algorithm
   - Create random test data
   - Create option to read/write data to file

# Working with branches
Its safer to work on implementation in other branches than _master_.  
The procedure is to go back to your _master_ branch to be sure that you have up-to-date code.  
For example:  
You have one file named test.py in your _master_ branch.  
You want to add second file, so you create _own_ branch.  
You created second file in your _own_ branch.  
Damian wanted to add 2 files, so he created his _other_ branch.  
He added 2 files to _other_ branch and then merged changes to _master_. So now _master_ have 3 files, but you in your _own_ branch do not have file added to _master_ by Damian, so you have only 2 files, the one that was in _master_ when you created your _own_ branch, and file that you created.  
Now, if you would create new branch, without changing branch back to _master_ and pulling changes it would still do not have files created by Damian, only yours.  
To put it visually:  
This is first scenerio, you create new branch _own2_ from branch _own_ instead of _master_:
> master (1 file) -> git checkout -b own -> own (2 files) -> git checkout -b own2 -> own2 (2 files)
This is what Damian did:
> master (1 file) -> git checkout -b other -> other (3 files) -> git push/merge -> master (3 files)
This is the proper way to create your _own2_ branch. If you merged your changes from _own_ branch to _master_, then it have 4 files. If you did not, there are 3 files:
> master (1 file) -> git checout -b own -> own (2 files) -> git push/merge (optional) -> git checkout master -> master (1/2 files) -> git pull -> master (3/4 files) -> git checkout -b own 2 -> own2 (3/4 files)
## Step 1:
### Check in which branch you are.
If you are in _master_ branch, go to **Step 3**  
If you are in _other_ branch, go to **Step 2**
## Step 2:
You are in _other_ branch. You will need to switch to _master_ branch before creating new branch.
To swich branch to master, you can use:
```
git checkout master
```
Then you should _pull_ all chenges on master with:
```
git pull
```
## Step 3
Now that you are in _master_ branch, you can safely create new branch with:
```
git checkout -b <branch name>
```

# Git Cheat-Sheet
To clone repository:
```
git clone https://github.com/matthias152/algorithms.git
```

To change/create new branch:
```
git checkout -b <branch name>   # without '-b' it will change branch
```

To add new file to current commit:
```
git add <file>
```

To confirm commit:
```
git commit -m "<description>"
```

To publish changes on Github:
```
git push origin <branch>
```
