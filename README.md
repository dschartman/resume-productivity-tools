# resume-productivity-tools
Tooling to help improve the workflow of building resumes.

This guide provides instructions for adding and updating the JSON data structures used in the dynamic resume generation project. The project is structured to include information about skills, job experiences, projects, and education.

## Project Structure Overview

The project is organized into several key directories:

- `data/`: Contains JSON files for different resume sections (skills, jobs, projects, education).
- `models/`: Houses Pydantic models for validating the JSON data.
- `templates/`: Stores Jinja2 templates for rendering the resume.

## Adding and Updating Data

### Skills

Skills are categorized into Programming Languages, Frameworks and Libraries, Tools and Platforms, Cloud Platforms, AI & ML, Methodologies, and Databases.

1. **Base Skills JSON (`data/base_skills.json`)**: To add or update your base skills, edit the corresponding category array in the `base_skills.json` file. Here’s the structure:

    ```json
    {
      "Programming_Languages": ["Python", "Java"],
      "Frameworks_and_Libraries": ["Django"],
      ...
    }
    ```

2. **Project Skills**: Skills used in projects should be included in the project's JSON file under `technologies_used`, categorized accordingly.

### Jobs

Each job experience should have its own JSON file within `data/experiences/jobs/`.

1. **Creating a Job JSON File**: Name the file descriptively, e.g., `senior_dev.json`, and structure it as follows:

    ```json
    {
      "id": "job_1",
      "company": "Tech Solutions Inc.",
      "role": {
        "title": "Senior Developer",
        "responsibilities": ["Develop APIs", "Lead projects"]
      },
      ...
    }
    ```

2. **Linking Projects**: Include an array of project IDs this job is associated with.

### Projects

Projects are stored in `data/experiences/projects/`. Separate them into `personal/` or `professional/` as needed.

1. **Adding a Project**: Create a JSON file (e.g., `project_alpha.json`) with the project details:

    ```json
    {
      "id": "project_1",
      "name": "Project Alpha",
      ...
    }
    ```

### Education

Education entries are located in `data/education.json`.

1. **Updating Education**: Add or modify entries in the `education.json` file, using the following format for each entry:

    ```json
    {
      "entries": [
        {
          "degree": "B.Sc. Computer Science",
          "institution": "University X",
          ...
        }
      ]
    }
    ```

## Validating Data with Pydantic Models

Each section’s data should be validated against its corresponding Pydantic model in the `models/` directory before being used. Ensure your updates conform to the expected structure defined by these models.

## Rendering the Resume

After updating the data:

1. **Validate Data**: Use the provided Python scripts to validate your JSON files against the Pydantic models.
2. **Generate Resume**: Run the `generate_resume.py` script, specifying the template and output file.

```bash
python generate_resume.py template.jinja output.md
```

## Conclusion

This guide should help you manage the data for your dynamic resume generation project. Regularly updating and validating your information ensures that your resume remains current and accurately reflects your professional achievements.
