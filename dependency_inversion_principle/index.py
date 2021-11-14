"""
Dependency Inversion Principle
"""

from service_database import ServiceDatabase
from service_api import APIService

def main():
    # Instance of service database
    db_service = ServiceDatabase()
    print(f'Database Service: { db_service.get_data() }, { db_service.set_data() }')

    # Instance of API
    api_service = APIService()
    print(f'API Service: {api_service.get_data() }, { api_service.set_data() } ')

main()