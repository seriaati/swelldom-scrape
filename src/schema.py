from pydantic import BaseModel


class Article(BaseModel):
    title: str
    url: str

    @property
    def id(self) -> int:
        return int(self.url.split("/")[-1].split(".")[0])
