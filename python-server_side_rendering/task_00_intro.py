import os


def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: Attendees should be a list of dictionaries")
        return

    # Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A"),
        )

        # Generate output file
        output_file = f"output_{i}.txt"
        with open(output_file, "w") as file:
            file.write(invitation)

        print(f"Generated {output_file}")


# Example usage:
if __name__ == "__main__":
    # Read the template from a file
    template_file_path = "template.txt"
    if os.path.exists(template_file_path):
        with open(template_file_path, "r") as file:
            template_content = file.read()

        # List of attendees
        attendees = [
            {
                "name": "Alice",
                "event_title": "Python Conference",
                "event_date": "2023-07-15",
                "event_location": "New York",
            },
            {
                "name": "Bob",
                "event_title": "Data Science Workshop",
                "event_date": "2023-08-20",
                "event_location": "San Francisco",
            },
            {
                "name": "Charlie",
                "event_title": "AI Summit",
                "event_date": None,
                "event_location": "Boston",
            },
        ]

        # Call the function with the template and attendees list
        generate_invitations(template_content, attendees)
    else:
        print(f"Template file '{template_file_path}' does not exist.")
