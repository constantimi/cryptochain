#!/bin/bash
cd $HOME
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-get update
sudo apt-get install -y python3.6 python-pip docker-ce git kubectl

pip install pyyaml

sudo wget -O /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64
sudo chmod +x /usr/local/bin/gitlab-runner
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start

sudo gitlab-runner register \
  --non-interactive \
  --url "https://gitlab.com/" \
  --registration-token "hu9efxLH5nt2QSpLW9JH" \
  --executor "shell" \
  --description "thesis-runner" \
  --tag-list "docker,aws, thesis-runner" \
  --run-untagged \
  --locked="false" \

sudo usermod -aG docker gitlab-runner
sudo usermod -aG docker stiefff
gcloud config set project thesis-project-111
gcloud auth -q configure-docker

sudo -u gitlab-runner gcloud auth activate-service-account --key-file cloud/infrastructure/project-key.json
sudo -u gitlab-runner cat cloud/infrastructure/project-key.json | docker login -u _json_key --password-stdin https://eu.gcr.io
sudo -u gitlab-runner python cloud/kube_deployment.py

echo "DONE"
