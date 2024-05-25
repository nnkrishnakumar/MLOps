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

