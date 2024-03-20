# {{ core_info.name }}
Address: {{ core_info.address }}
Email: [{{ core_info.email }}](mailto:{{ core_info.email }})
Phone: {{ core_info.phone }}
LinkedIn: [{{ core_info.linkedin }}]({{ core_info.linkedin }})
GitHub: [{{ core_info.github }}]({{ core_info.github }})

## Summary
Experienced Senior Software Engineer specializing in backend development and DevOps, with a focus on Python, Java, and cloud solutions. Proven leader in innovative projects, eager to apply my technical foundation and leadership skills to innovate.

## Experience
{% for job in jobs -%}
### {{ job.role.title }}, {{ job.company }} - {{ job.location }} ({{ job.start_date }} to {% if job.end_date %}{{ job.end_date }}{% else %}Present{% endif %})
#### Responsibilities
{% for responsibility in job.role.responsibilities -%}
- {{ responsibility }}
{% endfor %}
#### Key Projects
{% for project_id in job.projects -%}
{% for project in projects -%}
{% if project.id == project_id -%}
- **{{ project.name }}:** {{ project.description }}
{% endif -%}
{% endfor -%}
{% endfor -%}
{% endfor %}
## Projects
{% for project in projects -%}
### {{ project.name }}
**Description:** {{ project.description }}
{% set all_skills = [] -%}
{% for category, skills in project.technologies_used.items() -%}
    {% for skill in skills -%}
        {% set _ = all_skills.append(skill) -%}
    {% endfor -%}
{% endfor -%}
**Technologies Used:** {{ all_skills | join(', ') }}
**Achievements:**
{% for achievement in project.achievements -%}
- {{ achievement }}
{% endfor -%}
**Contributions:**
{% for contribution in project.contributions -%}
- {{ contribution }}
{% endfor %}
{% endfor -%}
## Skills
{% for category, skills in categorized_skills.items() -%}
**{{ category }}:** {{ skills | join(", ") }}
{% endfor %}
## Education
{% for entry in education.entries -%}
- **{{ entry.degree }}**, {{ entry.institution }} ({{ entry.end_year }})
{% endfor %}
