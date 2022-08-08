# Sample FastAPI Project
A sample FastAPI project to built to quickly initialize the project structure.

## Features
- Package version control (virtualenv and requirements)
- Pre-commit hooks (isort, black, flake8)

## Prerequisites
* Recommended platform - Linux (Ubuntu 16.04)
* Either
   * Python 3.8 and Pip installed

## Installation and set-up
To initialize a project, clone this repository and note the filepath
Run the following command in this directory (`path/to/dir/python_project/fastapi_project`).
**Note: Ensure that the `path/to/new/project` is referencing a git-enabled directory.
```
bash setup.sh path/to/new/project
```

This sample FastAPI project structure should've been copied and initialised in `path/to/new/project`. You
can now make add the files (`git add`) and commit it to your desired repository.

## Launching the server
While in the main file path, execute the following command in the new project root directory.
```bash
bash ./run.sh
```
Alternatively, manually execute the following command, substituting `$HOST`, `$PORT` and `$APP_MODULE` as necessary.
```bash
uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
```

## Successful installation/set-up
On successful server run, navigate to `localhost:8081`.
You should be able to see `{"msg":"Hello World"}` response.

## Documentation
FastAPI comes with in-built [OpenAPI documentation](https://github.com/OAI/OpenAPI-Specification). This can be found at `localhost:8081/docs`.
You can opt for SwaggerUI (`localhost:8081/docs`) or ReDoc (`localhost:8081/redoc`).

## Deploying the service
A sample Dockerfile has been created for you. Execute the following command to build the image (with a valid $IMAGE_NAME)
```
docker build -t $IMAGE_NAME .
```
The built container can then be initialized to run the FastAPI service.
```
docker run $IMAGE_NAME
```

## Testing
FastAPI works directly with Pytest. To run unit tests, simply execute the command from the root folder.
```bash
pytest tests
```

## Contribution
Please refer to CONTRIBUTING.md for guidelines on contributing.

This repository has `pre-commit` enabled. To enable (this is pre-installed when setting up this project), run `pre-commit install --install-hooks`.
You can run pre-commit hooks manually by running `pre-commit run --all-files`. This runs the pre-commit hooks on all tracked files.



## Teardown (Removing Docker image and containers)
As the `docker build` is an image, there will likely be containers using the images as dependencies. Thus to teardown (or uninstall the tool), the associated containers must be removed before the image. Alternatively, you might consider force removing the image, although that may cause other Docker images and containers on the same machine to be affected.

Consider removing the Docker image to identify the dependent containers. For instance, running `docker image rm ticket-viewer` will return the container `9a62b15b8x1h` that is using the image.
```bash
$ docker image rm ticket-viewer
Error response from daemon: conflict: unable to remove repository reference "ticket-viewer" (must force) - container  is using its referenced image {image_id}
```
With this information, drop the container `{container_id}` and attempt to drop the image again.
```bash
$ docker rm {container_id}
{container_id}
$ docker image rm ticket-viewer
```
## Testing (For Developers)
Python Unittests are provided to ensure functionality and usability.
This can be run either in the Docker image, or from the working path of this codebase if the local machine has necessary Python packages in `requirements.txt`.

__From the Docker image__
```bash
docker run ticket-viewer sh -c "python -m unittest tests/test_viewer.py -b"
```
```bash
$ docker run ticket-viewer sh -c "python -m unittest tests/test_viewer.py -b"
....................
----------------------------------------------------------------------
Ran 20 tests in 0.051s

OK
$
```
__From working path__
```bash
python -m unittest tests/test_viewer.py -b
```
```bash
zcc-zendesk-ticket-viewer $ python -m unittest tests/test_viewer.py -b
....................
----------------------------------------------------------------------
Ran 20 tests in 0.053s

OK
zcc-zendesk-ticket-viewer $
```
