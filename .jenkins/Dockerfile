FROM jenkins/jenkins:lts-jdk21

# Install plugins
RUN jenkins-plugin-cli --plugins \
    configuration-as-code \
    job-dsl \
    github \
    github-branch-source \
    workflow-aggregator \
    git \
    workflow-multibranch \
    pipeline-stage-view

# Skip initial setup
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV CASC_JENKINS_CONFIG="/var/jenkins_home/casc_configs/jenkins.yaml"
# Небезопасно, но для удобства демонстрации подойдет (НЕ ДЕЛАЙТЕ так в продакшене)
USER root
