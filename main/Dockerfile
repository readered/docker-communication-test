FROM alpine:latest
RUN apk add --update \
  python \
  python-dev \
  py-pip \
  build-base

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "main.py"]
