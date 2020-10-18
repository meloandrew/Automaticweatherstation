import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
import azure.cosmos.documents as documents

from azure.cosmos import CosmosClient, PartitionKey, exceptions

class Database():
    def __init__(self):
        pass

    def insert_data(self, values: dict):
        url = "https://weatherstoragedb.documents.azure.com/"
        key = "GS1A9w4PUT11tcoCseACehKAPeD6b0ZBCfUr9lIbgPw7i8SzcdlDBVyOrMV8rO9H2mwewjfNj3R5Uyp6Gq8FbQ=="
        client = cosmos_client.CosmosClient(url, {'masterKey': key})
        database_name = 'WeatherDb'

        # Cria ou obtém o banco de dados
        try:
            database = client.create_database(database_name)
        except errors.CosmosHttpResponseError:
            database = client.get_database_client(database_name)

        # Cria ou obtém o container do docget_database_clientumento
        container_name = 'predictions'

        try:
            container = database.create_container(id=container_name, partition_key=PartitionKey(path="/prediction"))
        except exceptions.CosmosResourceExistsError:
            container = database.get_container_client(container_name)
        except exceptions.CosmosHttpResponseError:
            raise
        
        # Insere os dados
        container.upsert_item(values)
        pass
    pass