class HomePageParameters:
    base_url = ''
    page_url = 'https://www.saucedemo.com/'
    home_page_header = 'Swag Labs'
    username_header = 'Accepted usernames are:'
    password_header = 'Password for all users:'
    empty_error_color = 'rgb(255, 255, 255)'
    error_color = 'rgb(226, 35, 26)'
    expected_list_of_users = ['standard_user', 'locked_out_user',
                              'problem_user', 'performance_glitch_user',
                              'error_user', 'visual_user']
    expected_password = ['secret_sauce']
    empty_username_error_text = 'Epic sadface: Username is required'
    empty_password_error_text = 'Epic sadface: Password is required'
    invalid_credentials_text = 'Epic sadface: Username and password do not match any user in this service'
    new_page_url = 'https://www.saucedemo.com/inventory.html'