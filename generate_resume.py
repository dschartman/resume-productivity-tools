import argparse
from models.core_info_model import CoreInfo
from models.eductation_model import Education
from models.experience_model import Job, Project
from models.skills_model import Skills
from utils.data_handeling import load_model, load_models
from utils.template_renderer import render_resume_template


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a resume from a template.")
    parser.add_argument("template_name", help="The name of the Jinja2 template file.")
    parser.add_argument(
        "output_file", help="The output file path for the generated resume."
    )

    args = parser.parse_args()

    core_info = load_model("data/core_info.json", CoreInfo)
    education = load_model("data/education.json", Education)
    jobs = load_models("data/jobs/", Job)
    projects = load_models("data/projects/", Project)
    skills = load_model("data/base_skills.json", Skills)

    context = {
        "core_info": core_info.model_dump(),
        "education": education.model_dump(),
        "jobs": [job.model_dump() for job in jobs],
        "projects": [project.model_dump() for project in projects],
        "categorized_skills": skills.model_dump(),
    }

    render_resume_template(args.template_name, context, args.output_file)
