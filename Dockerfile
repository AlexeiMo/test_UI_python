FROM python:3.8

RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz


RUN groupadd --gid 1000 tests \
  && useradd --uid 1000 --gid tests --shell /bin/bash --create-home tests

COPY requirements.txt .

# Download and install a dependency
# Run virtualenv /env
RUN pip install virtualenv
RUN virtualenv -p python3.8 virtual
RUN /bin/bash -c "source /virtual/bin/activate"


RUN /virtual/bin/pip install -r requirements.txt
RUN pip install -r requirements.txt

# Install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable \
rsync

# Install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Install allure
RUN apt-get -y update
RUN apt-get -y install allure


# Set display port to avoid crash
ENV DISPLAY=:99

RUN mkdir tests
WORKDIR tests

COPY . tests

RUN mkdir allure-results
RUN mkdir allure-report

CMD ["pytest", "--alluredir=allure-results", "/tests/"]
#CMD ["allure", "generate", "allure-results", "--clean", "-o", "allure-report"]
USER root
