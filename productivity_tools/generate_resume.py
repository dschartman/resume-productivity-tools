import argparse
from models.core_info_model import CoreInfo
from models.eductation_model import Education
from models.experience_model import Job, Project, Summary
from models.skills_model import Skills
from models.resume_info_model import ResumeInfo
from utils.data_handeling import load_model, load_models, load_models_paths
from utils.template_renderer import render_resume_template
from utils.template_parser import parse_template_format
from utils.renderers.renderer_factory import get_renderer
from models.resume_configs import ResumeConfig


def create_resume_info(resume_config: ResumeConfig) -> ResumeInfo:
    core_info = load_model(resume_config.core_info, CoreInfo)
    education = load_model(resume_config.education, Education)
    jobs = load_models(resume_config.jobs, Job)
    projects = load_models_paths(resume_config.projects, Project)
    skills = load_model(resume_config.skills, Skills)
    summary = load_model(resume_config.summary, Summary)

    resume_info = ResumeInfo(
        core_info=core_info,
        education=education,
        jobs=jobs,
        projects=projects,
        skills=skills,
        summary=summary,
    )

    return resume_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a resume from a template.")
    parser.add_argument("config", help="Path to the resume configuration file.")
    parser.add_argument(
        "output_file", help="The output file path for the generated resume."
    )

    args = parser.parse_args()

    config = load_model(args.config, ResumeConfig)

    resume_info = create_resume_info(config)
    context = {
        "core_info": resume_info.core_info.model_dump(),
        "education": resume_info.education.model_dump(),
        "jobs": [job.model_dump() for job in resume_info.jobs],
        "projects": [project.model_dump() for project in resume_info.projects],
        "categorized_skills": resume_info.skills.model_dump(),
        "summary": resume_info.summary.content,
    }

    format = parse_template_format(config.template_name)
    renderer = get_renderer(format)

    rendered_content = renderer.render(config.template_name, context)

    with open(args.output_file, "w") as file:
        file.write(rendered_content)

    print(f"Resume successfully generated: {args.output_file}")
