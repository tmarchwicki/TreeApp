# TreeApp
neo4j database + python rest api + react ui

STEP 1: 
- Add env file UI/.env file with the following key: REACT_APP_API_URL.
- Add env file restapi/.env file with the following key: NEO4J_PASSWORD.
  Add env file database/.env file with the following key: NEO4J_PASSWORD.

STEP 2: start the following components:

- Database component (written n Python that reads data from neo4j database)
- REST API component (written in Python/fastapi)
- Frontend app component (written in React)
The details for running each component can be found in the run.sh scripts that are located in component subfolders.

To expose the app from AWS EC2 the inbound rules should be configured to open ports for the React-app as well as for the fastAPI REST API Endpoint.

Assumptions: Code is as simple as possible, but there are some natural improvements that can be implemented:

- Adding unit tests for the frontend code as well
- Using dependency resolver for Python projects (e.g. poetry)
- Encapsulating each subproject in a docker file. Currently only neo4j components runs in a docker container
- Improving backend application security by storing passwords in some external password storage
