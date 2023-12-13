# UI test automation examples

Test examples with Playwright Python

## Folder structure:
+ pages - contains page objects and partial page objects
+ tests - contains test examples
+ utils - all kinds of util classes
+ Dockerfile - definition for building the test container
+ requirements.txt file with all required packages

## Running tests: 
### Build the Docker image
`docker build -t my-playwright-tests .`

### Run commands with parameters: 
`docker run --rm my-playwright-tests python -m pytest` runs all tests in the test folder

`docker run --rm my-playwright-tests python -m pytest -k <test-name>` will run only specific test

`docker run --rm my-playwright-tests python -m pytest --browser firefox` will run tests with firefox browser.
Build in --browser options are: chromium, firefox and webkit.
### Run in headed mode: 
Since the container has no graphical environment, running in headed mode requires the container to connect to the host's X-server. 
#### Tested support: Linux env and Windows (using WSL):
Prerequisite:`x-host +` on the host to allow connections to your x-server
`docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --ipc=host my-playwright-tests python -m pytest --headed`

