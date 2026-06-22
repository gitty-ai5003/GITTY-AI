import { Router, Request, Response, NextFunction } from 'express';
import { createClient } from 'redis';
import { config } from '../config';
import { logger } from '../config/logger';

const router = Router();

router.get('/health', async (req: Request, res: Response, next: NextFunction) => {
  let redisStatus = 'healthy';
  
  try {
    const client = createClient({
      url: `redis://${config.redis.host}:${config.redis.port}`
    });
    client.on('error', (err) => logger.error(err, 'Redis Client Error'));
    await client.connect();
    await client.ping();
    await client.disconnect();
  } catch (err: any) {
    logger.error(err, 'Redis ping failed in Auth health check');
    redisStatus = `unhealthy: ${err.message}`;
  }

  const isHealthy = !redisStatus.startsWith('unhealthy');

  res.status(isHealthy ? 200 : 500).json({
    status: isHealthy ? 'healthy' : 'unhealthy',
    timestamp: new Date().toISOString(),
    services: {
      redis: redisStatus
    }
  });
});

export default router;
