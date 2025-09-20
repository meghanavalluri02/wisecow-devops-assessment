# CI/CD Pipeline Test - $(date)
FROM ubuntu:22.04

# Install tools
RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd dos2unix

# Set PATH for fortune and cowsay
ENV PATH="/usr/games:${PATH}"

# Copy and fix line endings in one step
COPY wisecow.sh /app/wisecow-fixed.sh
RUN dos2unix /app/wisecow-fixed.sh && chmod +x /app/wisecow-fixed.sh

WORKDIR /app

EXPOSE 4499

CMD ["./wisecow-fixed.sh"]
