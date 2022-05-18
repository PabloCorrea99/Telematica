FROM node:14.19.1-alpine as builder

WORKDIR /bookstore

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:1.12.2-alpine

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

WORKDIR /usr/share/nginx/html

RUN mkdir bookstore

WORKDIR /bookstore

COPY --from=builder /bookstore/build /usr/share/nginx/html/bookstore

EXPOSE 5000 80

ENTRYPOINT ["nginx","-g","daemon off;"]
