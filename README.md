# TreeApp
neo4j database + python rest api + react ui

STEP 1: Replace localhost from the UI/.env file with the address.

STEP 2: start the following components:

Database component (written n Python that reads data from neo4j database)
REST API component (written in Python/fastapi)
Frontend app component (written in React)
The details for running each component can be found in the run.sh scripts that are located in component subfolders.

To expose the app from AWS E2C the inbound rules shoul be configured to open ports for the React-app as well as for the fastAPI REST API Endpoint.

Assumptions: Code is as simple as possible, but there are some natural improvements that can be implemented:

Improving AWS/E2C security by adjusting Inbound configuration (current rules that use 0.0.0.0 are usually not recommended)
Using AWS load balancer to improve serving the app
Adding unit tests for a frontend code as well
Using dependency resolver for Python projects (e.g. poetry)
Encapsulating each subproject in a docker file (microservice architecture). Currently only neo4j components runs in a docker container
Improving backend application security by storing passwords in some external password storage
