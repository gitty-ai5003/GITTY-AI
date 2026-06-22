import request from 'supertest';
import app from '../src/app';

// Mock Redis client to simulate a healthy state during tests
jest.mock('redis', () => {
  return {
    createClient: () => {
      return {
        on: () => {},
        connect: jest.fn().mockResolvedValue(true),
        ping: jest.fn().mockResolvedValue('PONG'),
        disconnect: jest.fn().mockResolvedValue(true)
      };
    }
  };
});

describe('GET /health', () => {
  it('should return a healthy response when redis is connected', async () => {
    const res = await request(app).get('/health');
    expect(res.status).toBe(200);
    expect(res.body.status).toBe('healthy');
    expect(res.body.services.redis).toBe('healthy');
  });
});
