from jinja2 import Environment, FileSystemLoader


def render_resume_template(template_name, context, output_file):
    env = Environment(loader=FileSystemLoader("templates/"))
    template = env.get_template(template_name)
    rendered_resume = template.render(context)

    with open(output_file, "w") as file:
        file.write(rendered_resume)
    print(f"Resume successfully generated: {output_file}")
