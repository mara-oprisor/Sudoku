import subprocess
MACE4_PATH = "/mnt/c/Users/user/Desktop/Facultate/AI/LADR-2009-11A/bin/mace4"
RULES_FILE_PATH = "./rules.txt"
SUDOKU_SIZE = 9

class FileCreator:
    def __init__(self, grid):
        self.grid = grid
        self.path = "./solve.in"

    def create_file(self):
        rules = ""

        with open(RULES_FILE_PATH, mode="r") as file:
            rules = file.read()

        with open(self.path, mode="w") as file:
            file.write(rules)

            values = self.generate_known_values()
            file.write("\n\n\n")
            file.write("formulas(known_numbers).\n\n")
            
            for value in values:
                file.write(f"{value}\n")
            
            file.write("\n\nend_of_list.")
        
    
    def generate_known_values(self):
        values = []

        for row in range(SUDOKU_SIZE):
            for col in range(SUDOKU_SIZE):
                value = self.grid[row][col]
                if value != -1:
                    values.append(f"value({row}, {col}) = {value - 1}.")

        return values
    

    def run_mace4(self):
        try:
            result = subprocess.run([MACE4_PATH, '-m', '-1', '-f', 'solve.in'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE,
                                    check=True)
            print("Mace4 ran successfully.")
            print(result.stdout.decode()) 
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            print(f"stderr: {e.stderr.decode()}")
        except FileNotFoundError as e:
            print(f"File not found error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

        