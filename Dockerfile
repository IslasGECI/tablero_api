FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    data-science-types \
    flake8 \
    flask_testing \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov
CMD ["make", "start"]
