# Start
To start the service you need to copy the content of this repository and run `docker-compose up` inside this folder.

# Example

If you want to get the distance from city 0 to city 2 you can use the following command:
```bash
curl -i -H 'x-api-key: 123321' "http://localhost:5000/distance?city_start=0&city_finish=2"
```