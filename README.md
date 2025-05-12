# CS551P Flask App
An app showing different scottish locations with data gathered in years, measurements, units, and indicators. 
Can filter data according to year and area. Ability to render information via bar charts in the future but 
not JS allowed for app. 

## Features
- Displays data such as year, measurement type, units, value, and indicator explanation.
- Filterable by year and location in Scotland.
- CI/CD on Render.

## App Organisation
- parse_traffic_csv.py: Parse the csv and redners the traffic_stats db.
- models.py: Contains logic for fetching and filtering data from the db.
- traffic_stats.py: Main Flask app that routes data into the frontend.
- templates/index.html: Displays a filterable table of traffic statistics.
- test_parse_csv.py: Tests database creation and foreign key linking.

Flask structure extremely simple with csv file showing traffic stats in Scotland. Parse python file drops a 
db table from the csv to the traffic_stats db. models filters the data in the way I want it to show on
UI. The app file ("traffic_stats") renders logic to index.html. index html shows the table.

## Testing
The test file checks:
- If the database tables were created correctly.
- If data was successfully inserted.
- If foreign key relationships are valid.
- Run tests using:
    in the bash:
        python test_parse_csv.py

## Future Work
Add a bar chart using ChartJS.
Add more data to compare to the traffic such as housing markets. 

## Render
https://cs511p-flask-app.onrender.com/
username: seluvaiasariahita@gmail.com
temp-pswrd: secret1234!

## Data Source
https://statistics.gov.scot/resource?uri=http%3A%2F%2Fstatistics.gov.scot%2Fdata%2Froad-network-traffic