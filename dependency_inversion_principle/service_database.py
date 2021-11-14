from connection_interface import ConnectionInterface

class ServiceDatabase(ConnectionInterface):

    def get_data(self):
        return 'Data from Database'
    
    def set_data(self):
        return 'Data has been set'