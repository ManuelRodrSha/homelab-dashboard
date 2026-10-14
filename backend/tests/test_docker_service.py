import app.services.docker_service as docker_service_module
from app.services.docker_service import DockerService

class MockImage:
    tags = ["nginx:latest"]

class MockContainer:
    short_id= "abc123"
    name= "nginx_container"
    image = MockImage()
    status = "running"

class MockContainerManager:
    def list(self):
        return [MockContainer()]

class MockClient:
    containers = MockContainerManager()

def test_get_running_containers(monkeypatch):
    monkeypatch.setattr(docker_service_module.docker_sdk, "from_env", lambda: MockClient())

    service = DockerService()
    result = service.get_running_containers()

    assert len(result) == 1
    assert result[0].id == "abc123"
    assert result[0].name == "nginx_container"
    assert result[0].image == "nginx:latest"
    assert result[0].status == "running"