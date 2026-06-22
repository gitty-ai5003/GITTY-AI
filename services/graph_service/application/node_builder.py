import hashlib
from libs.models import RepositoryNode, DirectoryNode, FileNode, ClassNode, FunctionNode, ImportNode, CallNode

class NodeBuilder:
    @staticmethod
    def build_repository_node(repo_id: str, name: str, path: str, metadata: dict = None) -> RepositoryNode:
        return RepositoryNode(
            id=repo_id,
            name=name,
            path=path,
            metadata=metadata or {}
        )

    @staticmethod
    def build_directory_node(repo_id: str, rel_path: str) -> DirectoryNode:
        dir_id = hashlib.sha256(f"{repo_id}:{rel_path}".encode()).hexdigest()
        return DirectoryNode(
            id=dir_id,
            name=rel_path.split("/")[-1] or rel_path,
            path=rel_path,
            metadata={"repository_id": repo_id}
        )

    @staticmethod
    def build_file_node(repo_id: str, file_path: str, metadata: dict = None) -> FileNode:
        file_id = hashlib.sha256(f"{repo_id}:{file_path}".encode()).hexdigest()
        return FileNode(
            id=file_id,
            name=file_path.split("/")[-1],
            path=file_path,
            metadata={**(metadata or {}), "repository_id": repo_id}
        )

    @staticmethod
    def build_class_node(file_id: str, class_name: str, path: str, metadata: dict = None) -> ClassNode:
        class_id = hashlib.sha256(f"{file_id}:{class_name}".encode()).hexdigest()
        return ClassNode(
            id=class_id,
            name=class_name,
            path=path,
            metadata={**(metadata or {}), "file_id": file_id}
        )

    @staticmethod
    def build_function_node(parent_id: str, func_name: str, path: str, metadata: dict = None) -> FunctionNode:
        func_id = hashlib.sha256(f"{parent_id}:{func_name}".encode()).hexdigest()
        return FunctionNode(
            id=func_id,
            name=func_name,
            path=path,
            metadata={**(metadata or {}), "parent_id": parent_id}
        )

    @staticmethod
    def build_import_node(file_id: str, import_name: str, path: str, metadata: dict = None) -> ImportNode:
        import_id = hashlib.sha256(f"{file_id}:import:{import_name}".encode()).hexdigest()
        return ImportNode(
            id=import_id,
            name=import_name,
            path=path,
            metadata={**(metadata or {}), "file_id": file_id}
        )

    @staticmethod
    def build_call_node(func_id: str, call_name: str, path: str, line: int, metadata: dict = None) -> CallNode:
        call_id = hashlib.sha256(f"{func_id}:call:{call_name}:{line}".encode()).hexdigest()
        return CallNode(
            id=call_id,
            name=call_name,
            path=path,
            metadata={**(metadata or {}), "function_id": func_id, "line": line}
        )
