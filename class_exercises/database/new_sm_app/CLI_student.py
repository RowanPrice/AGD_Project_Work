import pyinputplus as pyip

from controller_student import Controller
from functools import partial


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
        posts = self.controller.get_posts()
        for post in posts:
            user_name = self.controller.get_user_name(post.user_id)

            print(f"\nTitle: {post.title}")
            print(f"Description: {post.description}")
            print(f"Author: {user_name}")
            print("-" * 40)

        input("\nEnter to return")
        return self.user_home

    def create_posts(self):
        self.show_title('Create Posts')
        title = input('Enter a title: ')
        description = input('Enter a description: ')
        self.controller.add_post(title, description)
        return self.user_home

    def view_own_posts(self):
        self.show_title('View Own Posts')

        posts = self.controller.get_posts_by_user(self.controller.current_user_id)

        for post in posts:
            print(f"\nTitle: {post.title}")
            print(f"Description: {post.description}")
            print("-" * 40)

        input("\nPress Enter to return")
        return self.user_home

    def choose_user(self):
        self.show_title('Choose User To View')
        user_names = self.controller.get_user_names()
        for user in user_names:
            print(user)
        search = input()

        if search in user_names:
            return partial(self.view_user, search)
        else:
            return self.user_home

    def view_user(self, user):
        self.show_title(f'View User - {user}')

        user_details = self.controller.get_user_details(user)

        print(f'Name: {user}')
        print(f'Age: {user_details.age}')
        print(f'Gender: {user_details.gender}')
        print(f'Nationality: {user_details.nationality}')
        print("\n--- Posts ---")

        posts = self.controller.get_posts_by_user(user_details.id)

        if not posts:
            print("This user has no posts.")
            input("\nPress enter to return...")
            return self.user_home

        for post in posts:
            print(f"\nPost ID: {post.id}")
            print(f"Title: {post.title}")
            print(f"Description: {post.description}")
            print(f"Likes: {post.number_of_likes}")
            print("-" * 40)

        post_id = input("Enter Post ID to interact or press enter to return: ")

        if post_id.isdigit():
            return partial(self.interact_with_post, int(post_id))

        return self.user_home

    def interact_with_post(self, post_id):
        self.show_title(f"Post {post_id}")

        menu_items = ['Like post', 'Comment', 'View comments', 'Home']
        choice = pyip.inputMenu(menu_items, numbered=True)

        if choice.lower() == 'like post':
            self.controller.like_post(post_id)
            print("Post liked")
            input("\nPress Enter")
            return self.interact_with_post(post_id)

        elif choice.lower() == 'comment':
            text = input("Enter your comment: ")
            self.controller.add_comment(post_id, text)
            print("Comment added")
            input("\nPress Enter")
            return self.interact_with_post(post_id)

        elif choice.lower() == 'view comments':
            comments = self.controller.get_comments_for_post(post_id)

            if not comments:
                print("No comments")
            else:
                for c in comments:
                    user_name = self.controller.get_user_name(c.user_id)
                    print(f"\n{user_name}: {c.comment}")

            input("\nPress Enter")
            return partial(self.interact_with_post, post_id)

        return self.user_home

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')
        home_items = ['View posts',
                      'Create posts',
                      'Choose user to view',
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
        elif home_choice.lower() == 'choose user to view':
            next_menu = self.choose_user
        elif home_choice.lower() == 'exit':
            next_menu = self.exit_menus
        elif home_choice.lower() == 'view own posts':
            next_menu = self.view_own_posts

        return next_menu


if __name__ == '__main__':
    cli = CLI()
# controller = Controller()