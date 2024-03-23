from utils.template_renderer import render_resume_template


def test_render_resume_template(tmpdir):
    template_content = "Hello, {{ name }}!"
    template = tmpdir.join("hello_template.jinja")
    template.write(template_content)
    output_file = tmpdir.join("output.txt")
    render_resume_template(
        template.basename, {"name": "World"}, output_file.strpath, str(tmpdir)
    )

    assert output_file.read() == "Hello, World!"
