ARG NODE_VERSION=22.14.0
FROM node:${NODE_VERSION}
ENV MESSAGE="Hello Docker!"
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN useradd -m mynode
USER mynode
HEALTHCHECK --interval=20s --timeout=5s --start-period=5s --retries=3 CMD [ "curl", "-f", "http://localhost:3000" ]
CMD ["node", "index.js"]