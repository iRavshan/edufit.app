class ArticleService:
    def __init__(self, article_repository) -> None:
        self._article_repository = article_repository
        
    def get_by_id(self, id: int):
        return self._article_repository.get_by_id(id)
    
    def get_by_slug(self, slug: str):
        return self._article_repository.get_by_slug(slug)