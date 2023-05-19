echo "Generating certicates..."
docker-compose -f create-certs.yml run --rm create_certs
docker-compose up -d
echo "Elasticsearch running at https://localhost:9200"
echo "Kibana running at http://localhost:5601"