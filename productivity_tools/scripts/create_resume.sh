#!/bin/bash

TEMPLATE_NAME="$1"
OUTPUT_FILE="$2"

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 TEMPLATE_NAME OUTPUT_FILE"
    exit 1
fi

poetry run python generate_resume.py "${TEMPLATE_NAME}" "${OUTPUT_FILE}.md"
pandoc "${OUTPUT_FILE}.md" -o "${OUTPUT_FILE}.docx"
