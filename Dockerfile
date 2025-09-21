FROM ubuntu:22.04
RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd dos2unix
ENV PATH="/usr/games:${PATH}"
COPY wisecow.sh /app/wisecow-fixed.sh
RUN dos2unix /app/wisecow-fixed.sh && chmod +x /app/wisecow-fixed.sh
WORKDIR /app
EXPOSE 4499
CMD ["./wisecow-fixed.sh"]
