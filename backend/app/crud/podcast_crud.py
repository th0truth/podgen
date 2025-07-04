from sqlmodel import select

# Local Dependencies
from .base_crud import BaseCRUD
from core.models.podcast import (
    PodcastEpisodeBase,
    PodcastEpisode
)

class PodcastCRUD(BaseCRUD):
    def __init__(self, session):
        super().__init__(session)

    async def read_by_id(self, id: int) -> PodcastEpisodeBase:
       """
       Fetch the podcast using its `id`.
       """
       statement = select(PodcastEpisode).where(PodcastEpisode.id == id)
       result = await self.session.execute(statement)
       return result.scalar_one_or_none()