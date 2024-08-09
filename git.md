# Generate a new SSH Key for github
ssh-keygen -t [key_name] -C "your_email@example.com"
ssh-keygen -t ed25519 -C "jartavia05@gmail.com"

/Users/jartavia/.ssh/public_jartavia05/base_openemr/id_ed25519


# Verify your Key's Fingerprint 
ssh-keygen -l -f ~/.ssh/[key-type]/<key file>
ssh-keygen -l -f ~/.ssh/internal/jartavia-internal-2024-06-24



# Adding a new Identity
ssh-add -D
ssh-add ~/.ssh/public_jartavia05/base_openemr/id_ed25519
ssh-add -L

# Verify your Key's Fingerprint 
## Via SSH 

### Internal Key
ssh -oHostKeyAlgorithms=+ssh-dss kvinternal@ssh-keyrotation.akamai.com

### Deployed Key
ssh -oHostKeyAlgorithms=+ssh-dss kvdeployed@ssh-keyrotation.akamai.com

ssh-keygen -l -f ~/.ssh/[key-type]/<key file>
ssh-keygen -l -f ~/.ssh/internal/jartavia-internal-2024-02-26.pub
ssh-keygen -l -f ~/.ssh/deployed/jartavia-deployed-2024-05-14.pub



# Clone a repository with a specific SSH Key
git clone ssh://git@git.source.akamai.com:7999/~jartavia/jartavia_security_details.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2022-09-02.pub"
git clone ssh://git@git.source.akamai.com:7999/~jartavia/new_set_network_list.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2022-09-02.pub"
git clone ssh://git@git.source.akamai.com:7999/cfds/custom_cat.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/cfds/custom_cat.git
ssh://git@git.source.akamai.com:7999/cfds/support_ops.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone --branch jpadden/cons_dan_analysis ssh://git@git.source.akamai.com:7999/cfds/support_ops.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/~rfilmyer/graph_multiple_timelines.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/cfds/bot_score.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/~parm/ml_challenge_for_dsops.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/~ptorbus/aws-saml-bmp-seccloud.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"

git remote add origin ssh://git@git.source.akamai.com:7999/~jartavia/custom_cat_review.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-02-26"
git remote add origin git clone ssh://git@git.source.akamai.com:7999/cfds/dash_app.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/cfds/support_ops.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"

git clone ssh://git@git.source.akamai.com:7999/cfds/custom_cat.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"

## Clone ARP Rules Repo

git clone ssh://git@git.source.akamai.com:7999/ipr/apr-detection-custom-rules.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone ssh://git@git.source.akamai.com:7999/ipr/apr-detection-files.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"

# Dash_app
git clone ssh://git@git.source.akamai.com:7999/cfds/dash_app.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"



git clone ssh://git@git.source.akamai.com:7999/~rfilmyer/athena-batch-async.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"

### Dash Activate venv
python -m venv venv-queen
source venv-queen/bin/activate


# Install athena-batch-async.git as library
pip install git+ssh://git@git.source.akamai.com:7999/~rfilmyer/athena-batch-async.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
pip install git+https://git.source.akamai.com/scm/~rfilmyer/athena-batch-async.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"


# Clone BOTFENDER
git clone ssh://git@git.source.akamai.com:7999/cf/botfender.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"


# BETTY CLONE

git clone ssh://git@git.source.akamai.com:7999/~jartavia/betty-appbattery.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
git clone --branch "feature/DSOD-66-trends-top-detections-overall-totals" ssh://git@git.source.akamai.com:7999/dsopdev/betty-appbattery.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"


# Installing athena-batch-async
git clone ssh://git@git.source.akamai.com:7999/~rfilmyer/athena-batch-async.git --config core.sshCommand="ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24"
pip3 install athena-batch-async/


# Open quen 
ssh -i <your deployed key location> <username>@prod-use1-s2et.jumpbox.global.csc.akamai.com
ssh -i ~/.ssh/deployed/jartavia-deployed-2024-05-14 jartavia@prod-use1-s2et.jumpbox.global.csc.akamai.com


ssh -A -L 8900:localhost:8901 $USER@prod-use1-s2et.jumpbox.global.csc.akamai.com -t "ssh -L 8901:localhost:8900 queen"
ssh -i ~/.ssh/deployed/jartavia-deployed-2024-05-14 -A -L 8900:localhost:8901 $USER@prod-use1-s2et.jumpbox.global.csc.akamai.com -t "ssh -L 8901:localhost:8900 queen"

## This is working:
ssh -A -o ServerAliveInterval=60  -L 8900:localhost:8900 $USER@prod-s2et-iad-1.jumpbox.global.csc.akamai.com -t ssh -L 8900:localhost:8900 $USER@prod-s2et-iad-1-s2et-1


# Copy S3 cat models
cd ~/custom_cat
aws s3 cp s3://cf-datascience-data/dash_app/cat_models/web/ . --recursive
aws s3 cp s3://cf-datascience-data/dash_app/cat_models/sdk/ . --recursive


git config --global user.email "jartavia@akamai.com"
git config --global user.name "Jose Artavia"

git config --global user.email "jartavia05@gmail.com"
git config --global user.name "Jose A. Artavia"

# Engineering VM
 ssh -i ~/.ssh/internal/jartavia-internal-2024-06-24 -A $USER@bos-lhvb5m.bos01.corp.akamai.com
 ssh -A bos-lhvgww.bos01.corp.akamai.com -L 8888:localhost:80


 # Parquet format
 brew install parquet-cli
parquet-tools cat --json [filename.parquet]


# Quick setup — if you’ve done this kind of thing before

## …or create a new repository on the command line

echo "# base_openemr" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:VentureTechnologies/base_openemr.git
git push -u origin main

## …or push an existing repository from the command line
git remote add origin git@github.com:VentureTechnologies/base_openemr.git
git branch -M main
git push -u origin main