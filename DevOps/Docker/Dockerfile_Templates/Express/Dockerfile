# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files
COPY . .

# Expose port (Assuming it runs on port 3000)
EXPOSE 3000

# Start the app
CMD ["node", "index.js"]
