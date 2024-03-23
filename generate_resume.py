import argparse
from models.core_info_model import CoreInfo
from models.eductation_model import Education
from models.experience_model import Job, Project
from models.skills_model import Skills
from models.resume_info_model import ResumeInfo
from utils.data_handeling import load_model, load_models
from utils.template_renderer import render_resume_template
from utils.template_parser import parse_template_format
from utils.renderers.renderer_factory import get_renderer


def create_resume_info() -> ResumeInfo:
    core_info = load_model("data/core_info.json", CoreInfo)
    education = load_model("data/education.json", Education)
    jobs = load_models("data/jobs/", Job)
    projects = load_models("data/projects/", Project)
    skills = load_model("data/base_skills.json", Skills)

    resume_info = ResumeInfo(
        core_info=core_info,
        education=education,
        jobs=jobs,
        projects=projects,
        skills=skills,
    )
    return resume_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a resume from a template.")
    parser.add_argument("template_name", help="The name of the Jinja2 template file.")
    parser.add_argument(
        "output_file", help="The output file path for the generated resume."
    )

    args = parser.parse_args()

    resume_info = create_resume_info()
    context = {
        "core_info": resume_info.core_info.model_dump(),
        "education": resume_info.education.model_dump(),
        "jobs": [job.model_dump() for job in resume_info.jobs],
        "projects": [project.model_dump() for project in resume_info.projects],
        "categorized_skills": resume_info.skills.model_dump(),
    }

    format = parse_template_format(args.template_name)
    renderer = get_renderer(format)

    rendered_content = renderer.render(args.template_name, context)

    with open(args.output_file, "w") as file:
        file.write(rendered_content)

    print(f"Resume successfully generated: {args.output_file}")
