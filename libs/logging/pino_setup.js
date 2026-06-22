const pino = require('pino');

function configureLogger(options = {}) {
  const level = process.env.LOG_LEVEL || 'info';
  
  return pino({
    level,
    timestamp: pino.stdTimeFunctions.isoTime,
    formatters: {
      level: (label) => {
        return { level: label.toUpperCase() };
      },
    },
    ...options
  });
}

module.exports = {
  configureLogger
};
