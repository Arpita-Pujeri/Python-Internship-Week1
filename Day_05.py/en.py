# Task
# Create one object of InstagramAccount
# Add at least 2 private reels
# Add at least 2 archived reels
# Display private reels as follower and non-follower
# Display archived reels using correct and wrong password
# Update password using setter and check again


class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name
        self._private_reels = []
        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print(reel)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print(reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("Access Denied! Incorrect password")
            return None

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully")
        else:
            print("Incorrect old password")

account = InstagramAccount("rose_diaries", "1234")

account.add_private_reel("Vacation Reel")
account.add_private_reel("Food Reel")

account.display_private_reels(True)
account.display_private_reels(False)

account.add_archived_reel("Old Dance Reel")
account.display_archived_reels("1234")

print(account.get_archived_reels("1234"))

account.set_password("1234", "newpass")
