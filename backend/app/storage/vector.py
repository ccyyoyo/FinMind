from typing import Optional


class VectorStore:
    """Placeholder vector store client.

    Replace with Chroma, Weaviate, or Supabase Vector integration.
    """

    def __init__(self, url: Optional[str] = None) -> None:
        self.url = url or "memory://vector"

    def upsert(self, doc_id: str, content: str, metadata: dict | None = None) -> None:
        _ = (doc_id, content, metadata)
        # no-op for scaffold

    def query(self, text: str, k: int = 5) -> list[dict]:
        _ = (text, k)
        return []

