# sta141c
UC Davis SQ 2024 STA141C Final Project

# Git Commands 
(All of this is done using the terminal and the GitHub interface)

## Switching between branches 
Running 'git checkout "branch_name"' allows you to switch to different branches  

## Pull Requests 
Typically, you'll want to pull when the main branch has been updated with other people's code. In this case, click the "Pull Requests" button in the ribbon at the top of the GitHub interface. Then, click the "New Pull Request button. Change the left dropdown option (the one that the arrow points to) to your branch. Change the right dropdown option (the one that the arrow extends from) to main. Then, click "Create Pull Request". If there are no conflicts, a green button will pop up that says "Merge Pull Request". Click that button and you will have the updated code saved on your machine.

Alternatively, you can do all of this in the terminal. Run "git checkout main" to switch to the main branch. Then, run "git status" to check if your branch is up to date. If it is not, run "git fetch" to fetch the new code. Then, run "git pull" to pull all the code locally. 

## Push Requests
Once you've completed a task, you'll want to push your code to your branch. To do this, make sure you are currently checked into your own branch. To do this, run 'git checkout "your_branch"' to check into your branch. Then, run 'git add "your_file_name"' to stage your changes. This doesn't push anything; think of it as prepping your file to be pushed. If you want to stage changes for all your files, you can type "git add .". The period stages changes for every file in the git folder. After that, run 'git commit -m "a message about what your new code does"'. Adding the message will help users understand what changes you've made. Once you've done that, run "git push". This will push your code to your branch. 
