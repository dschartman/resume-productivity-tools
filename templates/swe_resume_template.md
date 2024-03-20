# {{ core_info.name }}
{{ core_info.email }} | [LinkedIn]({{ core_info.linkedin }})

## Experience
{% for exp in experiences %}
### {{ exp.title }} at {{ exp.company }}
*{{ exp.duration }}*
{% for achievement in exp.achievements %}
- {{ achievement }}
{% endfor %}
{% endfor %}

## Skills
{% for category, skills in skills.items() %}
### {{ category }}
{% for skill in skills %}
- {{ skill }}
{% endfor %}
{% endfor %}

## Projects
{% for project in projects %}
### {{ project.name }} - {{ project.role }}
Technologies: {{ project.technologies | join(", ") }}
{{ project.summary }}
{% endfor %}

## Education
{% for edu in education %}
- **{{ edu.degree }}**, {{ edu.institution }} ({{ edu.year }})
{% endfor %}
