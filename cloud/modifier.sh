#!/bin/bash

sudo apt-get update
sudo apt-get install python3.6

sudo wget -O /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64
sudo chmod +x /usr/local/bin/gitlab-runner
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start

sudo gitlab-runner register \
  --non-interactive \
  --url "https://gitlab.com/" \
  --registration-token "abdAps4geUGjVpPyXBMd" \
  --executor "docker" \
  --docker-image alpine:3 \
  --description "first-runner" \
  --tag-list "docker,aws, thesis-runner" \
  --run-untagged \
  --locked="false" \

echo "DONE"
