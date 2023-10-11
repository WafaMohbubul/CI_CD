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