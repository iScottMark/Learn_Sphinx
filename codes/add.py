class Dog:
    """
    A simple class representing a dog.

    Attributes
    ----------
    name : str
        The name of the dog.
    breed : str
        The breed of the dog.
    age : int
        The age of the dog in years.
    """

    def __init__(self, name: str, breed: str, age: int):
        """
        Initialize a Dog instance.

        Parameters
        ----------
        name : str
            The name of the dog.
        breed : str
            The breed of the dog.
        age : int
            The age of the dog in years.
        """
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self) -> str:
        """
        Simulate the dog barking.

        Returns
        -------
        str
            A string representing the dog's bark.
        """
        return f"{self.name} says: Woof!"

    def birthday(self):
        """
        Increment the dog's age by one year.
        """
        self.age += 1

    def info(self) -> str:
        """
        Return a string containing the dog's information.

        Returns
        -------
        str
            A string describing the dog.
        """
        return f"{self.name} is a {self.age}-year-old {self.breed}."
