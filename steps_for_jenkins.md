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

PLAN
#### Allow Jenkins to SSH instance EC2 Instance
1. Create EC2 instance 
1. Set up SSH access for Jenkins to your EC2 instance.
2. Ensure that Jenkins has the necessary SSH key or credentials to access the instance.

#### Add the -y Command for SSH Access
1. Modify the SSH command to include the `-y` option to automatically confirm host authenticity without user interaction.
2. 
```commandline
sudo apt upgrade
sudo apt upgrade -y
```
#### Copy the App Code
1. Use a build step in your "your_name-cd" job to copy the application code to the EC2 instance.

1. Change to the App Directory
2. Add a build step to navigate to the directory where the app code was copied on the EC2 instance 
3. Use the `cd` command.
Run npm install 
4. build step needs to be execute `npm install` within  app directory on the EC2 instance 
5. Install Node.js (or Use an AMI)
6. either install Node.js on the EC2 instance or use an Amazon Machine Image (AMI) that already has Node.js pre-installed.
7. Verify the Code via SSH 
8. Set up an SSH connection from Jenkins to your EC2 instance. 
9. Use an appropriate build step or script to SSH into your EC2 instance 
10. verify that the code and dependencies are correctly set up.
11. Modify app name
11. Add a build step to update the name of the Sparta app to "your_name - Sparta" within the app code.


