FROM mongo

COPY data/mongo-data.json /init.json
CMD mongoimport --host mongo --username root --password example --authenticationDatabase admin --db example_db --collection example_collection --type json --file /init.json --jsonArray