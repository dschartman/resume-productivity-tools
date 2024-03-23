import subprocess
import pytest
import os


@pytest.fixture
def template_name():
    return "swe_resume_template.md.jinja"  # Ensure this template exists for the test


@pytest.fixture
def output_file_base():
    return "generated/swe_resume"


def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Command failed with error: {e}")


def test_generate_resume(template_name, output_file_base):
    # Generate the resume markdown file
    generate_command = (
        f"poetry run python generate_resume.py {template_name} {output_file_base}.md"
    )
    pandoc_command = f"pandoc {output_file_base}.md -o {output_file_base}.docx"

    # Run the generate resume command
    run_command(generate_command)

    # Convert the generated markdown to DOCX
    run_command(pandoc_command)

    # Assertions to check if files were created
    assert os.path.isfile(f"{output_file_base}.md"), "Markdown file was not created."
    assert os.path.isfile(f"{output_file_base}.docx"), "DOCX file was not created."
