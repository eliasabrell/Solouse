ARG NODE_VERSION=22.14.0
FROM node:${NODE_VERSION}
#FROM node:${NODE_VERSION}-alpine
#FROM node:${NODE_VERSION}-slim

#RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

ENV PORT=3000
ENV MESSAGE="Hello Docker!"

LABEL author="Saile Abreu"
LABEL version="1.0"
LABEL description="Solouse"
LABEL env="production"

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .
RUN useradd -m mynode
USER mynode

HEALTHCHECK --interval=20s --timeout=5s --start-period=5s --retries=3 CMD [ "curl", "-f", "http://localhost:3000" ]

EXPOSE 3000

CMD ["node", "src/server.js"]