# MLOps

2. The stages of MLOps:
-----------------------
    i.  Data Collection and Preparations : 
        > Data ingestion, Preparation , exploration.
        > Define Goal & identify data source,
        > Prepare, Label and explore raw data.
        > Convert raw data to features.

    ii. Model Development and Training:
        > Getting data ready for ML Model.
        > Perform model training and validation.
        > Evaluation of ML Models.

            Here ml pipeline comes in picture:
                ML pipeline is cruicial
                Modularization and versioned(git repository)
                Automation Pipeline

            Here we will learn various tools like:
                1> github
                2> mlflow
                3> jenkins
                4> cloud resources
                5> Cloud computing
                6> Grafana
                7> Chromithius
                8> Contanerization platform

    Once the model Development is complete then proced with 

    iii> ML service deployment:

        1> Integrate with existing application
        2> Create Front end
        3> Containerize the application
        4> API services
        5> Model endpoint

    iv> Continuous Feedback Monitoring:
        1> Track data & Infrastructure
        2> Model
        3> Application Metrics

# Chapter3:
-----------
<<<<<<< HEAD
Git and Github foundation for MLOps:

Question: what is git?
Answer: git is a open source distributed version control system(DVCS)

A version control is allows you to record change to file over a period.

Git is used to maintain the historical and current version of source code.


> Git is a technology designed for tracking changes in a project and facilitating collaboration among multiple contributors.

> A git- controlled project at its core consits of a folder containing files, with Git monitoring changes made to these files.

> Git's primary function is to enable the storage of various versions of projecct work, earning it the title of version control system.

------------------------------------------------------------------------------
Role of Git in MLOps:
---------------------

1> Version Control:

    * Git plays a crucial role in MLOps by providing version control for machine learning models, code, and configuration files. This ensures traceability and reproducibility of expreiemnts and model deployments.

2> Collaboration and Team Workflow:

    * Git facilitates collaboration among data scientists, engineers, and other team members, allowing them to work concurrently on differnt aspects of machine learning pipeline. It enables seamless integration of changes and helps manage collaborative development efforts.

3> Experiment Tracking:

    * Git, in conjunction with tolls like Git-based paltforms or MLflow, helps track and manage machine learning experiments. This includes recording parameters, metrics, and code versions, making it easier to reproduce and compare results.

4> Branching for Experimentation:

    * Git's branching feature allows for the creation of isolated branches to expriment with differnt model versions or parmeter settings. This supports a systematic approach to testing and refining models withothut affecting the main codebase..

5> Continuous Integration(CI)and Continuous Deployment(CD):

    * Git integrates with CI/CD systems to automate the testing and deployment of machine learning models. This ensures that changes to the codebase are validated, and successful builds trigger automated deployment pipelines for model updates.

6> Infrastructuer as Code(IaC):

    * GIt is used to version control infrastructure cofnigurations as code, ensuring consistency between development, testing and production environments. This is praticularly relevant in MLOps, where the deployment infrastructure is a criticak component.

7> Collaboration Across Teams:

    * In MLOps, where teams may include data scientist, engineers and operations professionals, Git serves as a common platform for collaboration, enabling effectvie communication and coordination across differnt stages of the machine learnigng lifecycle.

8> Artifact Management:

    * Git is used in conjunction with artifact repositories to manage and version control artifacts such as trainined models, datasets and other dependencies. This ensures that all components of a machine learning project are tracked and reproducible.

9> Auditability and compliance:

    * Git's commit history provides an sudit trail for all changes made to the codebase and models. this is cruicial for compliance purposes, allowing organizations to trace back and understand the evolution of models and associated code.

Repository:
-----------

A repositroy(also known as a repo) is how we refer to a project version controlled by Git.

local repo  --> Remote Repo      --> github         --> store the file over cloud
computer        hosted on a          gitlab
                server               bitbucket
                                     codecommit

Git configuration:
------------------
Setting Git Configuration:
    * Git configurations are settings that allow you to customize how Git works.
    * They consist of variables and their values, and they are stored ina couple of differnt files.
    * To work with Git, you must set a few configuration variables related to user settings.

* Git conigurations are settings that allow you to customize how git works.They consist of variables and their values, and they are stored in a couple of differnt files. To work with Git, you must set a few configuration variables related to user settings.

```
git version
git config --global --list
git config --global user.name "nnkrishnakumar"
git config --global user.email "nnkrishna714@gmail.com"
git config --global init.defaultBranch main
git config --global --list
git init -b main

```
perform above code with git:
--------------------------

git config --global --list

output:

C:\Users\aimar\OneDrive\Desktop\Learning\MLops\MLOps>git config --global --list
user.email=nnkrishna714@gmail.com
user.name=nnkrishnakumar
=======
Introduction to Version Control System:

> Git is an opensource Distributed Version Control System(DVCS).
> A version control system allows you to record changes to files over a period.
> Git is used to maintain the historical and current versions of source code.


Usage at a High level:
-----------------------
> In a project, developres have a copy of all version of the code stored in the central server.
> Git allows developers to do the following:
    * Track the changes, who made the changes and when
    * Rollback/restore changes
    * Allow multiple developers to coordinate the work on the same files.
    * Maintain a copy of the files at the remote and local level.

What is git?
------------
> Git is a technology designed for tracking changes in a project and facilitating collaboration among multiple contributors.
> A Git-contorlled project at its core consists of a folder containing files, with Git monitoring changes made to these files.
> Git's primary function is to enable the storage of vairous versions of project work, earning it the title of version control system.

Role of Git in MLOps:
----------------------
> Version Control:
    * Git plays a cruical role in MLOps by providing version control for machine learning models, code, and configuration files. This ensures traceability and reproducibility of experiments and model deployments.

> Collaboration and Team Workflow.
    * Git facilitates collaboration among data scientist, engineers and other team memebers, allowing them to work concurrently on differnt aspects of the machine learning pipeline. It enables
    seamless integration of changes and helps manage collaborative development efforts.

> Experiment Tracking:
    * Git, in conjunction with tolls like Git-based platforms or MLflow, helps track and manage machine learning experiments.This includes recording parameters, metrics and code versions making it easier to repoduce and conpare result.

> Branching for Experimentation:
    * Git's branching feature allows for the creation of isolated branches to experiment with differnt model versions or parameter settings.This supports a systematic approach to testing and refining models without affecting the main codebase.

 > COntinuous Interation(CI) and Continuous Deployment(CD):
    * Git integrates with CI/CD systems to automate the testing and deployment of machine learning models. This ensures that changes to the codebase are validated and successful builds trigger automated deployment pipelines for model updates.

> Infrastructure as Code(IaC):
    * Git is used to version control infrastructure configureations as code, ensuring consistency between development, testing and production environments. This is particularly relevant in MLOps, where the deplyments infrastructure is a critical component.

> Collaboration Across Teams:
    * In MLOps, where teams may include data scientists, engineers, and opeartions professionals, GIt server as a common platform for collaboration, enabling effective communication and coordination across differnt stages of the machine leaning lifecycle.

> Artifcat Management:
    * Git is used in conjunction with artifact repository to manage and version control artifacts such as trained models, datasets and other dependencies. This ensures that all components of a machine learning project are tracked and reproducible.

-------------------------------------------------------
Local Repository and Remote Repo:
---------------------------------
Repository: Arepository(also known as a repo) is how we reger to a project version controlled by Git.

Local Repo                    Remote Repo

computer                   hosted on a hosting        --> Github/gitlab/bigbucket/code commit  ---> store the file over cloud 
                                service
>>>>>>> 41197bc8d3e77e2455ee87db33a1129acf359042



# Working with local repository:
---------------------------------

```
git init
git status
git add <file_name>
git status
git commit -m "my first commit"
git status
git log

```

# Git Branch:
-------------
```
git branch      # it help us to see the branched in the .git(local repository)

git branch <new_branch_name>      # to create new branch

git branch     # use to see all branch and *branch_name :> here "*" is used to see the current activate branch.

git log     # use to see current log of current version of git

```

* branch : definition : moveable point to commit


# switching the branch in Git:
------------------------------
```
git switch <branch_name>            # to switch the branch from one to another  

git checkout <branch_name >         # to move to the another branch

git branch                          # to see the all branches with "*" sign followed by <branch_name>

git status                          # On branch <branch_name>

git log                             #commit 40character_hax_values (HEAD -><branch_name>, main)

```

##########################################################################################################################################
### git switch <branch_name>
* Purpose: Specifically designed for switching branches.
* Simplicity: More user-friendly and easier to understand for beginners.
* Safety: Less likely to be misused for other operations. It is limited to switching branches and creating new branches.
* Introduction: Introduced in Git 2.23 as part of an effort to split the functionalities of git checkout into more specific commands.

### git checkout <branch_name>
* Purpose: A versatile command used for various operations, including switching branches, checking out files, and creating new branches.
* Complexity: More powerful but also more complex, as it handles multiple tasks.
* Legacy: Older command, available in all versions of Git, and widely used.
* Flexibility: Can be used for other operations like checking out specific commits, files, or paths.

##########################################################################################################################################
# Merging concept in git:
-------------------------

In Git, merging refers to the process of combining changes from difernt branches.

When you work on a project with multiple collaborators or when you are managing differnt features of bug fixes in separate branches, you may need to merge those changes banck into the main branch or another target branch.

## Type of Merging:
-------------------

1> Fast forward merge
2> Three-ways Merge

1> Fast Forward merge:
    * This occurs when the branch being merged has no new commits that the branch it is merging into doesn't already have.

    * In a fast-forward merge, Git simply moves the branh pointer forward, and no new merge commit is created.

    ```
    git switch dev
    git checkout dev
    #upload source code
    git add .
    git commit -m "V3"
    git log
    git checkout main
    
    ```

    # create fast-forwad merger:

    ```
    git switch dev 
    git merger dev

    ```

    ###################################################################################################################################################
    # Output:

    Fast-Forward: 
    -------------

    (base) admin1@CHETUIWK1850:~/Desktop/Learning/mlops_udemy/MLOps$ git checkout main
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    (base) admin1@CHETUIWK1850:~/Desktop/Learning/mlops_udemy/MLOps$ git merge dev
    Updating 8bff52a..df94865
    Fast-forward
    README.md | 88 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    1 file changed, 88 insertions(+)
    (base) admin1@CHETUIWK1850:~/Desktop/Learning/mlops_udemy/MLOps$ git log
    commit df94865857bc3bddfe0c746014d12ffcaf3f0345 (HEAD -> main, dev)
    Author: admin1 <nnkrishna714@gmail.com>
    Date:   Mon May 27 16:50:05 2024 +0530

        v4

    commit 0c1ddbe6cc7f70b23b0b305ca33bc62b733302a8
    Author: admin1 <nnkrishna714@gmail.com>
    Date:   Mon May 27 16:11:56 2024 +0530

        commit

    commit 8bff52add85b76ad50ad9e28e8c1f1321685a3b5 (origin/main, origin/HEAD)
    Merge: 4447a4a 41197bc
    Author: nnkrishnakumar <nnkrishna714@gmail.com>
    Date:   Sun May 26 17:35:20 2024 +0530

    #####################################################################################################################################################



2> Three- way Merge:
    * This coccurs when there are divergent changes in both the source and target branches.

    * Git creates a new commit, known as a "merge commit," that has two parent commits- one from the source branch and one from the traget branch.

    * The merge commit represents the combinantion of changes from both branches.


---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Checking out commit:
----------------------
Checking out commits refers to the process of switching your codebase to sa specific commit in a version control system.

-->

When you check out a commit , you are essentially telling the version control system to set your woking directory and codebase to the state it was in at the time of that specific commit.

-->

Uses:
    * debugging
    * branching 
    * reviewing history


```
git checkout <commit-hash>
git checkout -b <branch_name>    # to create new branch and switch to it

git switch -c <branch_name>       #to create a new branch and switch to it similary like4 git checkout<branch_name>

```


# git hosting services:
-----------------------

* Git hosting services are platforms that provides infrastructure and tools for hosting, managing and collaborating on Git repositories.

* These services make it easier for indiviuals and teams to use Git for version control and collaboractive software development.

* Examples: GitHub, GitLab, Bitbucket, Azure DevOps services,SourceForge, GitKraken, AWS CodeCommit, etc.
