import os


def generate_invitations(template, attendees):
    # Vérifier les types d'entrée
    if (
        not isinstance(template, str)
        or not isinstance(attendees, list)
        or not all(isinstance(item, dict) for item in attendees)
    ):
        print("Invalid input types.")
        return

    # Gérer les entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        filled_template = template
        for key, value in attendee.items():
            placeholder = "{" + key + "}"
            filled_template = filled_template.replace(
                placeholder, value if value is not None else "N/A"
            )

        # Générer les fichiers de sortie
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as file:
            file.write(filled_template)


# Exemple d'utilisation
if __name__ == "__main__":
    template = "Hello {name},\n\nYou are invited to the {event_title} on {event_date} at {event_location}.\n\nWe look forward to your presence.\n\nBest regards,\nEvent Team"
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
    generate_invitations(template, attendees)
