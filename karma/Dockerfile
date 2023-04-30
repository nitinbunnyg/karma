FROM python:3.8-alpine

LABEL maintainer="Evyatar Meged <evyatarmeged@gmail.com>"
LABEL dockerfile-creator="Mostafa Hussein <mostafa.hussein91@gmail.com>"

RUN addgroup -S karma && \
    adduser -S karma -G karma

RUN apk add --no-cache gcc musl-dev libxml2-dev libxslt-dev nmap nmap-scripts openssl

USER karma
WORKDIR /home/karma
RUN pip install karma-scanner

ENV PATH=/home/karma/.local/bin:${PATH}

ENTRYPOINT ["karma"]
CMD ["--help"]
