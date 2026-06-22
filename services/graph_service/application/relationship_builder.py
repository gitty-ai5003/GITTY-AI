from libs.models import RelationshipModel

class RelationshipBuilder:
    @staticmethod
    def build_relationship(
        source_id: str,
        target_id: str,
        rel_type: str,
        metadata: dict = None
    ) -> RelationshipModel:
        edge_id = f"{source_id}->{rel_type}->{target_id}"
        return RelationshipModel(
            id=edge_id,
            source_node=source_id,
            target_node=target_id,
            relationship_type=rel_type,
            metadata=metadata or {}
        )
