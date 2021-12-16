FROM node:16.10-alpine

WORKDIR /frontend

COPY --chown=node:node package.json .
RUN npm install

COPY --chown=node:node . .
USER node

CMD ["npm", "start"]
