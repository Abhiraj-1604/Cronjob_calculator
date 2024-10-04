from crontab import CronSlices

def interpret_cron_expression(cron_expression):
    """
    Interprets a cron expression and breaks down the schedule in human-readable terms.
    
    :param cron_expression: A string in cron format (e.g., '*/5 * * * *')
    :return: A breakdown of the schedule in readable format.
    """
    if CronSlices.is_valid(cron_expression):
        minute, hour, day_of_month, month, day_of_week = cron_expression.split()

        schedule = {
            "minute": interpret_field(minute, "minute", 0, 59),
            "hour": interpret_field(hour, "hour", 0, 23),
            "day of month": interpret_field(day_of_month, "day of the month", 1, 31),
            "month": interpret_field(month, "month", 1, 12),
            "day of week": interpret_field(day_of_week, "day of the week", 0, 7)
        }

        print("\nSchedule breakdown:")
        for field, value in schedule.items():
            print(f"{field.capitalize()}: {value}")
    else:
        print("Invalid cron expression. Please check your input.")

def interpret_field(field, name, min_value, max_value):
    """
    Interprets a single field of a cron expression.
    
    :param field: The cron field (e.g., '*/5', '*', '1-5')
    :param name: The name of the field (e.g., 'minute', 'hour')
    :param min_value: The minimum possible value for the field.
    :param max_value: The maximum possible value for the field.
    :return: A human-readable interpretation of the field.
    """
    if field == "*":
        return f"Every {name}"
    elif field.startswith("*/"):
        return f"Every {field[2:]} {name}s"
    elif "-" in field:
        start, end = field.split("-")
        return f"From {start} to {end} {name}s"
    elif "," in field:
        values = field.split(",")
        return f"On {', '.join(values)} {name}s"
    else:
        return f"At {field} {name}(s)"

# Example Usage:
cron_expression = input("Enter a cron expression (e.g., '*/5 * * * *'): ")
interpret_cron_expression(cron_expression)
