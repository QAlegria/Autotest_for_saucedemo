class Password:
    password = 'secret_sauce'

class StandardUser:
    standard_username = 'standard_user'
    standard_user_pass = Password.password

class LockedOutUser:
    locked_out_username = 'locked_out_user'
    locked_out_user_pass = Password.password

class ProblemUser:
    problem_username = 'problem_user'
    problem_user_pass = Password.password

class PerformanceGlitchUser:
    performance_glitch_username = 'performance_glitch_user'
    performance_glitch_user_pass = Password.password

class ErrorUser:
    error_username = 'error_user'
    error_user_pass = Password.password

class VisualUser:
    visual_username = 'visual_user'
    visual_user_pass = Password.password