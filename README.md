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
