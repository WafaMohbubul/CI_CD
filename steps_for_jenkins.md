## Navigating Jenkins

#### Creating new job
1. Click **New Item**
2. Enter a suitable name: `wafa-first-job`
3. Scroll down and click **OK**
4. Write a description (can be anything suitable)
5. Select **Discard old builds**
6. Scroll down to **Build** and write commands:
```commandline
whoami
uname -a
```
or
```commandline
date
```
7. click **Save**

#### Linking 2 jobs together
1. click on the job
2. On left hand navigation plane, click **Configure**
3. Scroll down to **Post-build Actions**
4. Select **Build Other Project**
4. Find the job you want to connect to 
5. Select **Trigger only if build is stable**
6. click **Save**


## Merging dev branch to main branch

#### Creating Jobs in Jenkins

1. Click Create new Job/New Item
2. label 'Wafa-CI'
3. Click 'Freestyle Project'
4. Description - suitable description
5. Tick **Discard Old Builds**
6. Max # of builds to keep = 3
7. Tick GitHub project > paste repository URL `https://github.com/WafaMohbubul/CI_CD`
7. Restrict where this project can be run = sparta-ubuntu-node 
8. Source Code Management > Git > Paste GitHub SSH link `git@github.com:WafaMohbubul/CI_CD.git`
9. Credentials > `wafa-jenkins-key6`
10. Branch specifier = `*/dev`
11. Build Triggers > Tick **GitHub hook trigger for GITcm polling**
12. Build Environment > **Provide Node & npm bin/ folder to PATH** > `Sparta-Node-JS`
13. Build:
```commandline
cd app/app
npm install
npm test
```
14. Post-build Actions > **Build other projects** > select `wafa-merge` > Trigger only if build is stable 
NOTE: A SECOND job needs to be created before connecting the 2

CI (Continuous Integration)
#### Creating a second job and Merging
1. Create second job
2. label 'Wafa-merge'
3. Click 'Freestyle Project'
4. Description - suitable description
5. Tick **Discard Old Builds**
6. Max # of builds to keep = 3
7. Tick GitHub project > paste repository URL `https://github.com/WafaMohbubul/CI_CD`
7. Restrict where this project can be run = sparta-ubuntu-node 
8. Source Code Management > Git > Paste GitHub SSH link `git@github.com:WafaMohbubul/CI_CD.git`
9. Credentials > `wafa-jenkins-key6`
10. Branch specifier = `*/dev`
11. Additional Behaviours > Merge before build > Name of repository = `origin`, branch to merge to `main`
12. Build Environment > Tick **SSH Agent** > **tech254.pem**
13. Post-build Actions > Git Publisher > Tick `Merge Results`

## PLAN for Continuous Deployment and Delivery**
Difference between deployment and delivery is that big red button in delivery to push it out. 

#### Allow Jenkins to SSH instance EC2 Instance
1. Create EC2 instance with Ubuntu 18.04 
2. Set up SSH access to your EC2 instance using `sudo apt upgrade -y`
NOTE: Ensure that Jenkins has the necessary SSH key or credentials to access the instance.
3. Install mongoDB
4. Change the BindIP to 0.0.0.0 inside file
5. Run commands:
```commandline
sudo systemctl start mongod
sudo systemctm enable mongod
```

#### Create the App virtual machine
1. Modify the SSH command to include the `-y` option to automatically confirm host authenticity without user interaction.
2. Run commands:
```commandline
sudo apt upgrade -y
```

3. Run npm install 
4. Install Node.js (or Use an AMI)
5. build step needs to be execute `npm start` within  app directory on the EC2 instance
NOTE: either install Node.js on the EC2 instance or use an Amazon Machine Image (AMI) that already has Node.js pre-installed.
7. Verify the Code via SSH: Verify that the code and dependencies are correctly set up.
11. Modify app name: add a build step to update the name of the Sparta app to `Wafa - Sparta` within the app code.


