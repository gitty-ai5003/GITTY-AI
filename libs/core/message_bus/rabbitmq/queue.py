class RabbitMQQueue:
    @staticmethod
    def declare_and_bind(channel, queue_name: str, exchange_name: str, routing_key: str):
        """Declares a queue and binds it to an exchange with a routing key."""
        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(
            queue=queue_name,
            exchange=exchange_name,
            routing_key=routing_key
        )
        return queue_name
