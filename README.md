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

