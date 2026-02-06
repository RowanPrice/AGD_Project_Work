import pyinputplus as pyip

from controller_student import Controller


class CLI:
    def __init__(self):
        self.controller = Controller()
        self.current_menu = self.login
        self.running = True
        self.run_menus()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def run_menus(self):
        while self.running:
            self.current_menu = self.current_menu()

    def exit_menus(self):
        self.running = False
        print("Goodbye")

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()
        menu_items = ['Login',
                      'Create a new account',
                      'Exit',
                       ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select user or create a new account\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'create a new account':
            next_menu = self.create_account
        elif menu_choice.lower() == 'exit':
            next_menu = self.exit_menus
        else:
            user_name = input('Enter your name: ')
            if user_name in users:
                self.controller.set_current_user_from_name(user_name)
                next_menu = self.user_home
            else:
                print(f'Name: "{user_name.title()}" not recognised')
                next_menu = self.login
        return next_menu

    def create_account(self):
        self.show_title('Create Account')
        users = self.controller.get_user_names()
        user_name = input('Enter your username: ')
        if user_name in users:
            print('Username already exists')
        else:
            age = int(input('Enter your age: '))
            gender = input('Enter your gender: ')
            nationality = input('Enter your nationality: ')
            self.controller.add_user(user_name, age, gender, nationality)

        return self.login

    def view_posts(self):
        self.show_title('View Posts')
        input()
        return self.user_home

    def create_posts(self):
        self.show_title('Create Posts')
        input()
        return self.user_home

    def view_own_posts(self):
        self.show_title('View Own Posts')
        input()
        return self.user_home

    def view_users(self):
        self.show_title('View Users')
        for user in self.controller.get_user_names():
            print(user)
        input()
        return self.user_home

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')
        home_items = ['View posts',
                      'Create posts',
                      'View users',
                      'View own posts',
                      'Exit',
                      ]

        home_choice = pyip.inputMenu(home_items,
                                     numbered=True,
                                     )

        if home_choice.lower() == 'view posts':
            next_menu = self.view_posts
        elif home_choice.lower() == 'create posts':
            next_menu = self.create_posts
        elif home_choice.lower() == 'view users':
            next_menu = self.view_users
        elif home_choice.lower() == 'exit':
            next_menu = self.exit_menus
        elif home_choice.lower() == 'view own posts':
            next_menu = self.view_own_posts

        return next_menu


if __name__ == '__main__':
    cli = CLI()
# controller = Controller()