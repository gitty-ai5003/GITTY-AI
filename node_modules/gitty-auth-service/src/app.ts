import express from 'express';
import { config } from './config';
import { logger } from './config/logger';
import routes from './routes';
import { errorHandler } from './middleware/error';

const app = express();

app.use(express.json());

// Log incoming requests
app.use((req, res, next) => {
  logger.info({ method: req.method, url: req.url }, 'Incoming request');
  next();
});

app.use(routes);

// Global Error Handler
app.use(errorHandler);

if (process.env.NODE_ENV !== 'test') {
  app.listen(config.port, () => {
    logger.info({ port: config.port, env: config.env }, 'Auth Service started successfully');
  });
}

export default app;
