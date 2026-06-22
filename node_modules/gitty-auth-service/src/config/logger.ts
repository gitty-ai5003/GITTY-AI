// Import configureLogger from shared libs/logging
const { configureLogger } = require('../../../../libs/logging/pino_setup');

export const logger = configureLogger({
  name: 'auth-service'
});
