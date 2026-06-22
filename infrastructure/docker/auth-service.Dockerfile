FROM node:18-alpine

WORKDIR /app

# Copy dependency definition
COPY apps/auth-service/package*.json ./apps/auth-service/
RUN cd apps/auth-service && npm install

# Copy application source
COPY apps/auth-service/ ./apps/auth-service/

WORKDIR /app/apps/auth-service

EXPOSE 3000

CMD ["npm", "run", "dev"]
