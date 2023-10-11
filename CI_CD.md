### What is DevOps
- software development methodology that combines software development (Dev) with IT operations (Ops)
- participating together in the entire service life-cycle, from design through the development process to production
- automate the processes between software development and IT teams
- can build, test, and release software faster.
- DevOps is a culture that bridges the gap between cross functional teams
- breaks silos
- removes toil 

### What is CI-CD 
- Continuous Integration and CD — Continuous Delivery and Deployment
- considered the backbone of DevOps practices and automation
- Continuous Integration (CI):
  - Developers merge/commit code to master branch multiple times a day
  - fully automated build and test process
  - gives feedback within few minutes
  - void the integration hell that usually happens when people wait for release day to merge their changes into the release branch
- Continuous Integration and Continuous Delivery:
  - make sure that you can release new changes to your customers quickly in a sustainable way
  - also have automated your release process as well as automated testing
  - In continuous Delivery the deployment is completed manually
- Continuous Deployment:
  - every change that passes all stages of your production pipeline is released to your customers
  - no human intervention, and only a failed test will prevent a new change to be deployed to production

### Jenkins
What is it:
- Tool for CI-CI Pipeline
- Jenkins is an open-source automation server in which the central build and CI process take place
-  a Java-based program with packages for Windows, macOS, & Linux.
Why Jenkins:
- Open source
- flexible
- active community
- lots of plugins
- Easy to use

### Stages of Jenkins
1. Build 
2. Test
3. Deploy

### Altenratives to Jenkins
- circleci
- TeamCity
- Bamboo
- GitLab
