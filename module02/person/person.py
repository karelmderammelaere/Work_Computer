PERSON_REGISTRY: dict[str, "Person"] = {}
#conataints all persons attributes with key, full name in lower case

class Person:
    def __init__(self, fullname: str) -> None:
        if not isinstance(fullname, str):
            raise ValueError("fullname must be a non-empty string")

        key = fullname.lower()
        if key in PERSON_REGISTRY:
            raise ValueError(f"Person with fullname '{fullname}' already exists")

        self._fullname = fullname
        PERSON_REGISTRY[key] = self

    @property
    def fullname(self) -> str:
        return self._fullname

    def __repr__(self) -> str:
        return f"Persoon({self.fullname})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.fullname.lower() == other.fullname.lower()

def get_person(fullname: str) -> Person:
    if not isinstance(fullname, str) or not fullname.strip():
        raise ValueError("fullname must be a non-empty string")
    key = fullname.lower()
    person = PERSON_REGISTRY.get(key)
    if person:  # Als persoon al bestaat, gewoon teruggeven
        return person
    new_person = Person(fullname)  # Persoon bestaat nog niet: aanmaken en registreren
    PERSON_REGISTRY[key] = new_person
    return new_person

