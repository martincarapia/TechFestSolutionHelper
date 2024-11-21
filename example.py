import SolutionTemplate

def main(problem_number: int, team_name: str, team_number: int):
    # Create a SolutionTemplate object
    solution = SolutionTemplate.Template(problem_number, team_name, team_number)
    # Read and print the content of the input file
    input = solution.read_input_file()
    print(input)
    
    # Write a message to the output file
    output = "Hello, World!"
    solution.write_to_output(output)
    
    # Close the input and output files
    solution.finished()


if __name__ == "__main__":
    main(problem_number=1, team_name="Snider", team_number=2)