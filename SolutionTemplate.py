class Template:
    def __init__(self, problem_number: int, team_name: str, team_number: int) -> None:
        """
        Initialize the SolutionTemplate with problem and team numbers.
        
        :param problem_number: The number of the problem.
        :param team_name: The name of the team.
        :param team_number: The number of the team.
        """
        self.problem_number = problem_number
        self.team_name = team_name
        self.team_number = team_number
        
        # Open the input file based on the problem number
        try:
            self.infile = open(f"Input-0{self.problem_number}.txt" if self.problem_number < 10 else f"Input-{self.problem_number}.txt", "r")
        except OSError:
            print(f"Input file for problem {self.problem_number} not found.")
            self.infile = None
        
        # Open the output file based on the problem and team numbers
        try:
            self.outfile = open(f"0{self.problem_number}-{self.team_name}{self.team_number}.txt" if self.problem_number < 10 else f"{self.problem_number}-{self.team_name}{self.team_number}.txt", "w")
        except OSError:
            print(f"Unable to create output file for problem {self.problem_number}, team {self.team_name}{self.team_number}.")
            self.outfile = None

    def write_to_output(self, output: str) -> None:
        """
        Write the given output string to the output file.
        
        :param output: The string to write to the output file.
        """
        try:
            self.outfile.write(output)
        except OSError:
            print("Output file is not available.")

    def read_input_file(self) -> list:
        """
        Read and print the content of the input file.
        """
        try:
            return self.infile.read().split("\n")
        except OSError:
            print("Input file is not available.")

    def finished(self) -> None:
        """
        Close the input and output files and print a finished message.
        """
        if self.infile:
            self.infile.close()
        if self.outfile:
            self.outfile.close()
        print("Finished!")