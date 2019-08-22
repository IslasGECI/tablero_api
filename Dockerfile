FROM python:3
COPY . /workdir/
WORKDIR /workdir
RUN pip install --requirement requirements.txt
RUN pip install --editable .
CMD ["python", "-m", "api"]
