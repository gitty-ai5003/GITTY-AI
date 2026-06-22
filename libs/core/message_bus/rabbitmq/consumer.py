import pika
from typing import Callable, Dict, Any
from ..interfaces.event_bus import IEventBus
from ..serializers.event_serializer import EventSerializer
from .exchange import RabbitMQExchange
from .queue import RabbitMQQueue

class RabbitMQConsumer(IEventBus):
    def __init__(self, host: str = "localhost", port: int = 5672):
        self.host = host
        self.port = port
        self._connection = None
        self._channel = None
        self._handlers: Dict[str, Callable[[Any], None]] = {}

    def _connect(self):
        if not self._connection or self._connection.is_closed:
            self._connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host, port=self.port)
            )
            self._channel = self._connection.channel()
            RabbitMQExchange.declare(self._channel)

    def publish(self, topic: str, event: Any) -> None:
        raise NotImplementedError("Use RabbitMQPublisher to publish events.")

    def subscribe(self, queue_name: str, topic: str, handler: Callable[[Any], None]) -> None:
        self._connect()
        RabbitMQQueue.declare_and_bind(
            self._channel,
            queue_name=queue_name,
            exchange_name=RabbitMQExchange.GITTY_EVENTS,
            routing_key=topic
        )
        
        def callback(ch, method, properties, body):
            try:
                event_data = EventSerializer.deserialize(body.decode())
                handler(event_data)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                # In production, route to a Dead Letter Queue (DLQ)
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        self._channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            auto_ack=False
        )

    def start_consuming(self) -> None:
        self._connect()
        self._channel.start_consuming()

    def close(self):
        if self._connection and self._connection.is_open:
            self._connection.close()
Class = RabbitMQConsumer
