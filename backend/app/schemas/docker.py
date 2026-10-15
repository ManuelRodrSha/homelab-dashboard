from pydantic import BaseModel

class DockerContainer(BaseModel):
    id: str 
    name: str 
    image: str 
    status: str 
    