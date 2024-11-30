FROM ubuntu:20.04

WORKDIR /home

COPY tests /home
COPY pytest.ini /home
COPY requirements.txt /home

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y default-jre wget vim jq python3-venv git

ARG ALLURE_VER=2.13.7

RUN wget https://github.com/allure-framework/allure2/releases/download/$ALLURE_VER/allure-$ALLURE_VER.tgz
RUN tar zxvf allure-$ALLURE_VER.tgz ; mv allure-$ALLURE_VER /usr/bin/allure-$ALLURE_VER
RUN ln -s /usr/bin/allure-$ALLURE_VER/bin/allure /usr/bin/allure
RUN mkdir -p /home/vagrant/jenkins/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/allure/bin/
RUN ln -s /usr/bin/allure-$ALLURE_VER/bin/allure /home/vagrant/jenkins/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/allure/bin/allure
RUN rm -rf allure-$ALLURE_VER.tgz allure-$ALLURE_VER

RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt

