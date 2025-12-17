# base image

FROM node:20-alpine

#set working directory

WORKDIR /app

#copy package.json and package-lock.json
COPY package*.json ./

#install dependencies
RUN npm install

#copy all code

COPY . . 

#expose port
EXPOSE 5001

#start app 
CMD ["node", "index.js"]
