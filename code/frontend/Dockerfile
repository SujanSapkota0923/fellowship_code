
# Stage 1 - Build Stage

FROM node:18 as BUILD
WORKDIR /app
COPY . .
RUN yarn install
RUN yarn build

# Stage 2 - Production Image

FROM nginx:alpine as PRODUCTION
COPY --from=BUILD /App/dist /var/www/html
COPY --from=BUILD /App/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

