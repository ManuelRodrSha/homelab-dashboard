from fastapi.testclient import TestClient 

from app.main import app
from app.models.docker import DockerContainer
import app.api.docker as docker_api

client = TestClient(app)

def test_docker_endpoint(monkeypatch):
    fake_containers = [
        DockerContainer(
            id="abc123",
            name="nginx_container",
            image="nginx:latest",
            status="running",
        )
    ]

    monkeypatch.setattr(
        docker_api.DockerService,
        "get_running_containers",
        lambda self: fake_containers,
    )

    response = client.get("/docker/containers")
    
    assert response.status_code == 200
    assert response.json() ==[
        {
            "id": "abc123",
            "name": "nginx_container",
            "image": "nginx:latest",
            "status": "running",
        }
    ]