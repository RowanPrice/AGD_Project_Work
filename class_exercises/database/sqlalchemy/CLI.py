from controller import Controller


class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)

        if not activities:
            print("No activities found.")
            return

        for activity in activities:
            print(activity)

    def show_all_activities(self):
        for activity in self.controller.get_all_activities():
            print(activity)

    def show_all_people(self):
        for person in self.controller.get_all_people():
            print(person)

    def show_activity_people(self):
        activity_name = input('Enter activity name: ')
        people = self.controller.get_activity_people(activity_name)

        if not people:
            print("No people found.")
            return

        for person in people:
            print(person)

    def add_person(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        self.controller.add_person(first_name, last_name)
        print("Person added.")

    def add_activity(self):
        name = input("Activity name: ")
        if self.controller.add_activity(name):
            print("Activity added.")
        else:
            print("Activity already exists.")

    def delete_person(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        if self.controller.delete_person(first_name, last_name):
            print("Person deleted.")
        else:
            print("Person not found.")

    def add_person_to_activity(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        activity = input("Activity name: ")

        if self.controller.add_person_to_activity(first_name, last_name, activity):
            print("Person added to activity.")
        else:
            print("Could not add person to activity.")


if __name__ == '__main__':
    cli = CLI()

    cli.show_all_activities()