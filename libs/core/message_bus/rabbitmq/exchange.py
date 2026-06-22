class RabbitMQExchange:
    GITTY_EVENTS = "gitty.events"
    
    @staticmethod
    def declare(channel, name: str = GITTY_EVENTS, exchange_type: str = "topic"):
        """Declares a topic exchange in RabbitMQ."""
        channel.exchange_declare(
            exchange=name,
            exchange_type=exchange_type,
            durable=True
        )
        return name
