# resume-productivity-tools

This project automates the creation of customized resumes and cover letters tailored to specific job descriptions. It leverages Jobscan for optimizing documents against job listings, ensuring higher compatibility scores. Python, Jinja2, and Pydantic are used for template rendering and data validation, making the application process more efficient and targeted.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Poetry for dependency management
- Pandoc

### Installation

1. Clone the repository:

```bash
git clone https://yourrepositorylink.com
```

2. Navigate to the project directory:

```bash
cd resume-productivity-tools
```

3. Install dependencies using Poetry:

```bash
poetry install
```

### Usage

Generate a customized resume and cover letter with the following command:

```bash
./scripts/create_resume.sh <TEMPLATE_NAME> <OUTPUT_FILE_NAME>
```

- `<TEMPLATE_NAME>`: The name of the Jinja2 template file (without the extension).
- `<OUTPUT_FILE_NAME>`: The base name for the output file (without the extension).

Example:

```bash
./scripts/create_resume.sh swe_resume_template my_resume
```

This command will generate `my_resume.md` and convert it to `my_resume.docx`.

## Project Structure

- `data/`: JSON files for resume sections (skills, jobs, projects, education).
- `models/`: Pydantic models for data validation.
- `templates/`: Jinja2 templates for resume and cover letter.
- `utils/`: Utility scripts for data handling and template rendering.
- `generate_resume.py`: Main script for generating resumes.

## Customizing Your Resume

### Adding Data

1. **Skills**: Edit `data/base_skills.json` to update your skills.
2. **Jobs**: Add or edit JSON files in `data/jobs/` for each job experience.
3. **Projects**: Add project details in `data/projects/`.
4. **Education**: Update `data/education.json` with your educational background.

### Modifying Templates

Edit the Jinja2 templates in the `templates/` directory to change the layout or content of your resume and cover letter.

## Contributing

Contributions are welcome! Please read our contributing guidelines (link to guidelines) for how to propose bug fixes, features, and improvements.

## License

Distributed under the MIT License. See `LICENSE` for more information.
