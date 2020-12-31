FROM python:3.8.2-buster as base

RUN pip install gunicorn
RUN pip install poetry

WORKDIR /DevOps-Course-Starter
COPY poetry.lock pyproject.toml /DevOps-Course-Starter/

RUN poetry config virtualenvs.create false --local && poetry install

COPY . /DevOps-Course-Starter/

#EXPOSE 5000

FROM base as production
ENV FLASK_ENV=production
RUN poetry install --no-dev
CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app

FROM base as development
RUN poetry install
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]

FROM base as test
RUN poetry install

# Install Chrome 
RUN apt-get update
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\  
    rm ./chrome.deb 

# Install Chromium WebDriver 
RUN apt-get update
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d ./
ENTRYPOINT [ "poetry", "run", "pytest" ]
