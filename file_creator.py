import subprocess
import re

MACE4_PATH = "/mnt/c/Users/user/Desktop/Facultate/AI/LADR-2009-11A/bin/mace4"
RULES_FILE_PATH = "./rules.txt"
SUDOKU_SIZE = 9

class FileCreator:
    def __init__(self, grid):
        self.grid = grid
        self.path = "./solve.in"
        self.output_path = "./solve.out"

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
            with open(self.output_path, "w") as output_file:
                result = subprocess.run(
                    [MACE4_PATH, '-m', '-1', '-f', 'solve.in'],
                    stdout=output_file,
                    stderr=subprocess.PIPE,  
                    check=True
                )
            print("Mace4 ran successfully. Output written to solve.out.")

        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            print(f"stderr: {e.stderr.decode()}")

        except FileNotFoundError as e:
            print(f"File not found error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    


    def parse_mace4_output(self):
        with open(self.output_path, 'r') as file:
            content = file.read()

        success_match = re.search(r"Exiting with (\d+) model", content)
        success = success_match.group(1) if success_match else "0"

        grid_match = re.search(r"function\(value\(_,_\), \[(.*?)\]\)", content, re.DOTALL)
        if grid_match:
            grid = grid_match.group(1)
            grid_values = [int(x.strip()) + 1 for x in grid.split(",")]
            sudoku_grid = [grid_values[i:i+9] for i in range(0, len(grid_values), 9)]
        else:
            sudoku_grid = None

        return {
            "success": success,
            "sudoku_grid": sudoku_grid
        }

        