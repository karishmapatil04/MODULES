class ExpressionSolver:
    
    # Constructor
    def __init__(self, expression):
        self.expression = expression
    
    # Method to evaluate the expression
    def solve(self):
        try:
            result = eval(self.expression)  # evaluate expression
            return result
        except Exception as e:
            return f"Error: {e}"
    
    # Method to display result
    def display(self):
        print("Expression:", self.expression)
        print("Result:", self.solve())


# Taking input from user
exp = input("Enter a mathematical expression (e.g., 2+3*4): ")

# Create object
solver = ExpressionSolver(exp)

# Display result
solver.display()