FROM ubuntu:22.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git pandoc python3 python3-pip

COPY "entrypoint.sh" "/entrypoint.sh"
RUN chmod +x "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]