#!/usr/bin/python3
"""
Module task_00_intro
Contains generate_invitations function to handle template invitations.
"""


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.

    Args:
        template (str): The template string with placeholders.
        attendees (list): List of dictionaries containing attendee data.
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Invalid input type for template: expected str, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Invalid input type for attendees: expected list of dicts, got {type(attendees).__name__}")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    keys = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in keys:
            val = attendee.get(key)
            if val is None:
                val = "N/A"
            content = content.replace(f"{{{key}}}", str(val))

        # Write to output file
        filename = f"output_{i}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
