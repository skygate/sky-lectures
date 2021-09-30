FROM node:16.10-alpine

WORKDIR /frontend

COPY package.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]