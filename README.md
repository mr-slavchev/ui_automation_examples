# UI test automation examples

Test examples with Playwright Python

## Filder structure:
+ pages - contains page objects and partial page objects
+ tests - contains test examples
+ utils - all kinds of util modules
+ Dockerfile - definition for building the test container
+ requirements.txt file with all required packages

## Running tests: 
### Build the Docker image
`docker build -t my-playwright-tests .`

### Run commands with parameters: 
`docker run --rm my-playwright-tests` runs all tests in the test folder

`docker run --rm my-playwright-tests -k test_file:test_method` will run only specific test
`docker run --rm my-playwright-tests --browser firefox` will run tests with firefox browser.
Build in --browser options are: chromium, firefox and webkit.
### Run in headed mode: 
Since the container has no graphical environment, running in headed mode requires the container to connect to the host's X-server. 
#### Linux env:
Prerequisite:`x-host +` to allow connections to your x-server
`docker run --rm -e DISPLAY=$DISPLAY --ipc=host my-playwright-tests --headed`

#### Windows env:
`docker run --rm -e DISPLAY=host.docker.internal:0 --ipc=host my-playwright-tests`

