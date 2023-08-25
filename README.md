# Benford's Law Visualizer

This is a full stack application that allows users to upload datasets, calculate the frequency of each first digit in a column, and compare that calculation to Benford's law as a mixed line/bar graph and a pseudo-heatmap.

## Quick Start/TLDR:

1. Run docker on your local machine.
2. Run `make boot-dev` in your terminal.
3. Open http://localhost:3000 in your browser to see the web interface. The api runs on http://localhost:5001, and you can see Swagger docs at http://localhost:5001/swagger-ui.
4. If you'd prefer to see the built production version instead, you can run `make boot-local-build`
   a. frontend will be `http://localhost:3001`
   b. backend will be `http://localhost:5002`

## Frontend Information

- The frontend uses: Vue, Nuxt 3, TypeScript, Tailwind (and a few other packages)

## Backend Information

- The backend uses: Python, Flask, flask-smorest, marshmallow, sqlalchemy (and a few other packages)

## Database & Devops Information

- The database is Postgres
- Each service has Dockerfiles associated with different environments, and docker-compose pieces it all together
- The Makefile makes it even easier to run a bunch of docker-compose commands and get the enviroments spun up quickly

## Sample Data

There are a couple of files in `api/static/_sample-data` that can be used for trying out the upload UI, if you don't have your own handy.

You can also make a POST request to `/generate-csv` (probably have to increase the timeout if you're using Postman or Insomnia) or run the script in `api/generate_sample_data.py` and it will generate a 1,000,000 row csv for you. It takes about three minutes to run.
