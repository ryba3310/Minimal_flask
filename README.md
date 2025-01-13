# Minimal Flask

This project is just a mininmal flask application created for integration with AWS CI/CD pipeline.
Source code is bootstraped from Flask Pixel UI Kit.

Available through easy_envoy at site.justalab.com

In aws.yml file in github/workflows directory for github Actions there is being run a script at endpoint locally through ssh with contents:

It requires setting secret values in GitHub's repository: 
HOST - valid DNS hostname or ip address
USERNAME - SSH username
SSH_KEY - SSH private key

Additionally might be added repository access key for managment

```
#!/bin/bash
echo "Starting deployment ..."
eval $(ssh-agent)
ssh-add /path/to/key
cd /path/to/app/reposirtory
git pull
sudo docker-compose down && \
sudo docker-compose  up -d --build
echo "Deployment complete ..."
```

# TODO

- ✅ Some basic outline of purpose

- ✅ Deploy with just basic functionality for CI/CD with GitHub

- ✅ Add minimal pytest functinal tests

- ✅ Add Prometheus metrics endpoint

- ❌  Try AWS stack too, which seems more security wise(AWS CodeCommit is no longer available)
