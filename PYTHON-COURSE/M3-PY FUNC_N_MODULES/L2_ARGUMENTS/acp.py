def shutdown(password):
    """
    Simulates a shutdown function.
    
    Parameters:
        password (str): The password required to shut down
    
    Returns:
        str: Shutdown status message
    """
    correct_password = "OpenSesame"
    
    if password == correct_password:
        return "Shutting down..."
    else:
        return "Shutdown aborted. Incorrect password."


# Example usage
user_input = input("Enter password to shut down: ")
result = shutdown(user_input)
print(result)