from pages.parameters.credentials import Password
class HomePageParameters:
    base_url = ''
    username_header = 'Accepted usernames are:'
    password_header = 'Password for all users:'

    empty_error_color = 'rgb(255, 255, 255)'
    error_color = 'rgb(226, 35, 26)'

    expected_list_of_logins = ['standard_user', 'locked_out_user',
                              'problem_user', 'performance_glitch_user',
                              'error_user', 'visual_user']
    expected_passwords = [Password.password]
    empty_username_error_text = 'Epic sadface: Username is required'
    empty_password_error_text = 'Epic sadface: Password is required'
    invalid_credentials_text = 'Epic sadface: Username and password do not match any user in this service'
    locked_out_user_error_text = 'Epic sadface: Sorry, this user has been locked out.'
    inventory_page_without_login_error_text = "Epic sadface: You can only access \'/inventory.html\' when you are logged in."
    cart_page_without_login_error_text = "Epic sadface: You can only access \'/cart.html\' when you are logged in."