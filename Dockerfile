FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --requirement requirements.txt
CMD ["python", "-m", "api"]
