"""A small contact book with normalized names."""

class ContactBook:
    def __init__(self) -> None:
        self._contacts: dict[str, str] = {}

    def add(self, name: str, phone: str) -> None:
        key = name.strip().casefold()
        if not key or not phone.strip():
            raise ValueError("name and phone are required")
        self._contacts[key] = phone.strip()

    def find(self, name: str) -> str:
        try:
            return self._contacts[name.strip().casefold()]
        except KeyError as error:
            raise ValueError("contact not found") from error

    def remove(self, name: str) -> None:
        self._contacts.pop(name.strip().casefold(), None)

if __name__ == "__main__":
    contacts = ContactBook()
    contacts.add("Asha", "555-0100")
    print(contacts.find("asha"))
