####################################################################
# Builder stage
####################################################################
FROM node:18-slim AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

####################################################################
# Production stage
####################################################################
FROM nginx:alpine AS production

# Clean default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy build files to nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port nginx runs on
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
