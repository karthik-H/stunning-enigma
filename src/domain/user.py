from typing import Any, Dict

class User:
    def __init__(self, id: int, name: str, username: str, email: str, phone: str, website: str, address: Dict[str, Any], company: Dict[str, Any]):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
        self.company = company

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'User':
        return User(
            id=data['id'],
            name=data['name'],
            username=data['username'],
            email=data['email'],
            phone=data['phone'],
            website=data['website'],
            address=data['address'],
            company=data['company']
        )
