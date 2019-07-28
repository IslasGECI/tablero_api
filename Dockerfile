FROM python:3
COPY . /workdir/
WORKDIR /workdir
RUN pip install -r requirements.txt
CMD ["python", "-m", "app"]

