import pytest
import os
from SolutionTemplate import Template

@pytest.fixture
def setup_files():
    # Create a sample input file
    with open("Input-100.txt", "w") as f:
        f.write("line1\nline2\nline3")
    
    yield
    
    # Cleanup the files after tests
    os.remove("Input-100.txt")
    os.remove("100-team1.txt")

def test_read_input_file(setup_files):
    template = Template(100, "team", 1)
    lines = template.read_input_file()
    assert lines == ["line1", "line2", "line3"]

def test_write_to_output(setup_files):
    template = Template(100, "team", 1)
    template.write_to_output("output line")
    template.outfile.close()  # Ensure the file is closed after writing
    with open("100-team1.txt", "r") as f:
        content = f.read()
    assert content == "output line"