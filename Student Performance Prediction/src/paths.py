import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def project_path(*parts: str) -> str:
    return os.path.join(PROJECT_DIR, *parts)
