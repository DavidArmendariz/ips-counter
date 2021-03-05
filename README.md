# Web requests

## Local development

To start local development, run in the terminal:

```bash
docker-compose up -d
```

Now you are ready to go to `http://localhost:5000/` to see the app working.

If you want to stop the container, run in the terminal:

```bash
docker-compose down
```

## Endpoints

There are three endpoints:

- `/`: If you enter to this path, your IP will be stored in memory.
- `/top`: Here, you will find the top IPs by frequency.
- `/clear`: By hitting this endpoint, you will be clearing all IPs and their frequencies.

## Tests

To run the tests, run the following command in your terminal:

```bash
docker exec web-requests python -m unittest discover
```
