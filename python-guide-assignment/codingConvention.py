import json


class StudentRecordManager:
    """A class to manage student records."""

    def __init__(self, records_file):
        """
        Initialize the manager with the path to the records file.

        Parameters:
            records_file (str): Path to the JSON file to save records.
        """
        self.records_file = records_file
        self.records = self._load_records()

    def _load_records(self):
        """Load records from the JSON file."""
        try:
            with open(self.records_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_records(self):
        """Save records to the JSON file."""
        with open(self.records_file, "w") as file:
            json.dump(self.records, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record to the records.

        Parameters:
            student_id (int): Student's ID.
            name (str): Student's name.
            age (int): Student's age.
            grade (str): Student's grade.
        """
        new_record = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "grade": grade
        }
        self.records.append(new_record)
        self._save_records()

    def search_student(self, identifier):
        """
        Search for a student by student_id or name.

        Parameters:
            identifier (int or str): Student's ID or name.

        Returns:
            dict or None: Student's record or None if not found.
        """
        for record in self.records:
            if record["student_id"] == identifier or record["name"] == identifier:
                return {"age": record["age"], "grade": record["grade"]}
        return None

    def update_student(self, identifier, attribute, new_value):
        """
        Update a student's information by using student_id or name.

        Parameters:
            identifier (int or str): Student's ID or name.
            attribute (str): Attribute to update (age or grade).
            new_value (int or str): New value for the attribute.
        """
        for record in self.records:
            if record["student_id"] == identifier or record["name"] == identifier:
                record[attribute] = new_value
                self._save_records()
                break


if __name__ == "__main__":
    manager = StudentRecordManager("student_records.json")

    manager.add_student(1, "Alice", 20, "A")
    manager.add_student(2, "Bob", 22, "B")

    search_result = manager.search_student("Alice")
    if search_result:
        print("Student found:", search_result)
    else:
        print("Student not found.")

    manager.update_student(1, "age", 21)
    print("Updated student record:", manager.search_student(1))
 