import os
import subprocess
from ..domain.interfaces.repository_scanner import IRepositoryScanner

class GithubRepositoryScanner(IRepositoryScanner):
    def clone_or_fetch(self, repo_url: str, dest_path: str) -> str:
        """
        Clones remote repository using shallow clones (--depth=1) or runs git pull if exists.
        """
        if not os.path.exists(dest_path):
            os.makedirs(dest_path, exist_ok=True)

        git_dir = os.path.join(dest_path, ".git")
        if os.path.exists(git_dir):
            # Pull updates
            subprocess.run(
                ["git", "pull"],
                cwd=dest_path,
                capture_output=True,
                check=True
            )
        else:
            # Clone fresh shallow repository
            subprocess.run(
                ["git", "clone", "--depth=1", repo_url, dest_path],
                capture_output=True,
                check=True
            )
        return dest_path
Class = GithubRepositoryScanner
