import docker as docker_sdk

from app.schemas.docker import DockerContainer

class DockerService:
    def get_running_containers(self) -> list[DockerContainer]:
        client = docker_sdk.from_env()
        containers = client.containers.list()

        result = []
        for container in containers:
            image = container.image.tags[0] if container.image.tags else "unknown"

            result.append(
                DockerContainer(
                    id=container.short_id,
                    name=container.name,
                    image=image,
                    status=container.status,
                )
            )

        return result