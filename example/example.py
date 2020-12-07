from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


class Example:
    def __repr__(self) -> str:
        return """ 
        class to test the CRUD of the aurite DB
        no error handling for now, i wanted this to be quick  (‾◡◝)
        """

    def __init__(self, table_name) -> None:
        super().__init__()
        self.table_service = TableService(
            connection_string="AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
        )
        self.table_name = table_name

    def create_table(self):
        """Creates a table with the name given"""
        self.table_service.create_table(table_name=self.table_name)

    def insert(self, partitionKey, rowKey, value, description, *args, **kwargs):
        """
        inserts a record into the table
        required arguments:
        partitionKey,
        rowKey
        """

        task = {
            "PartitionKey": partitionKey,
            "RowKey": rowKey,
            "Value": value,
            "Description": description,
        }
        self.table_service.insert_or_merge_entity(self.table_name, task)  # * INSERT

    def update(self, partitionKey, rowKey, value, description, *args, **kwargs):
        """
        Updates a record in the table
        required arguments:
        partitionKey,
        rowKey
        """
        task = {
            "PartitionKey": partitionKey,
            "RowKey": rowKey,
            "Value": value,
            "Description": description,
        }
        self.table_service.update_entity(self.table_name, task)

    def get(self, partitionKey, rowKey, *args, **kwargs):
        """
        Gets a record into the table
        required arguments:
        partitionKey,
        rowKey
        """
        task = self.table_service.get_entity(
            self.table_name, partitionKey, rowKey
        )  # * GET
        print(task)

    def delete(self, partitionKey, rowKey, *args, **kwargs):
        """
        deletes a record from the table
        required arguments:
        partitionKey,
        rowKey
        """
        self.table_service.delete_entity(self.table_name, partitionKey, rowKey)

    def remove_table(self):
        """
        Self proclaimed destrucor,
        looks tough,
        does nothing...
        for now... ╰（‵□′）╯
        """
        self.table_service.delete_table(self.table_name)  # * DELETE FIRST
