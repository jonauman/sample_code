#!/bin/bash
set -e

JENKINS_HOME=/data/jenkins
JENKINS_SERVER=127.0.0.1
JENKINS_PORT=8080
PLUG_IN=$1
SSHKEY=id_rsa_wickes

function install_plugin() {
  if [[ ! -f jenkins-cli.jar ]];
  then
    wget ${JENKINS_SERVER}:${JENKINS_PORT}/jnlpJars/jenkins-cli.jar
  fi
  java -jar jenkins-cli.jar -s http://${JENKINS_SERVER}:${JENKINS_PORT}/ -i $SSHKEY install-plugin --username admin $PLUG_IN
}

install_plugin
