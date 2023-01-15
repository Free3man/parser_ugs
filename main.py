from browser import Browser
from users import Users


if __name__ == "__main__":
    # Variables
    url = "https://accounts.google.com/v3/signin/identifier?dsh=S-1610567913%3A1673709467301816&continue=https%3A%2F" \
          "%2Fadmin.google.com%2F&followup=https%3A%2F%2Fadmin.google.com%2F&osid=1&passive=1209600&flowName" \
          "=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh41gUcS57rYvVy0HxP-BXYL7PUSsABGhIs6xEU6v" \
          "-fBCcy7ljHl5XbTD_wqeK8RgW_gggXT_Q"
    email = "nbriazghin21@ugs.foundation"
    password = "Coolnikita2005"
    path_excel = r"C:\Users\Nikita Briazghin\Desktop\users.xlsx"

    # Accessing to users from Excel
    users = Users(path_excel)
    users_array = users.read_users()

    # Initialize
    browser = Browser(url, email, password, users_array)
    browser.connect_to_url()
    browser.auth()

    # Wait input
    input("Waiting for accepting the entrance from the phone. When you're ready, just press the enter!")

    # Add new users
    browser.add_users()


