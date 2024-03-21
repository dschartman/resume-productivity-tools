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

## Future Features and Roadmap

This project is in its early stages and designed to streamline the job application process. As it evolves, we plan to introduce a range of features to enhance usability, flexibility, and effectiveness. Here are some of the future features and improvements we're considering:

1. **Internal Scoring Model**: Develop an in-house scoring model to analyze and optimize resumes and cover letters, aiming to replace dependencies on external services like Jobscan. This will offer more control over the optimization process and privacy of data.

2. **User-Friendly Interface**: Introduce graphical interfaces or web-based platforms to make the tool accessible to non-technical users. Simplifying interaction with the tool can help users generate personalized documents without deep technical knowledge.

3. **Template Customization and Expansion**: Improve the template system to allow for more dynamic customization and easier modifications. This will enable users to adjust the aesthetics and structure of their resumes and cover letters to better match personal preferences and job requirements.

4. **Enhanced Error Handling and User Feedback**: Implement more detailed error messages and validation feedback within the tool. Providing clear guidance for correcting data issues will improve the user experience, especially for manually edited JSON files.

5. **Comprehensive Testing Suite**: Expand the testing framework to include integration tests that cover the end-to-end document generation process. This will ensure the tool's reliability and robustness as new features are added.

6. **Documentation and Guides**: Continue to develop detailed documentation, including step-by-step guides for creating or modifying templates, understanding data models, and troubleshooting common issues.

7. **Performance Optimization**: Address scalability and performance concerns to ensure the tool can efficiently handle an increased number of templates and extensive customization options without compromising speed or reliability.

8. **Internationalization and Localization**: Incorporate support for multiple languages and adapt the tool to meet the resume standards of different countries. This will make the tool more versatile and useful for a global audience.

We are committed to enhancing this tool and welcome feedback and contributions from the community. Stay tuned for updates as we work to bring these features to life.

## License

Distributed under the MIT License. See `LICENSE` for more information.
