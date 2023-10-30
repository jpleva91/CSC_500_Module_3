def calculate_alarm_time(current_hours, current_minutes, hours_to_wait, minutes_to_wait):
    total_minutes = current_minutes + minutes_to_wait
    extra_hours, final_minutes = divmod(total_minutes, 60)

    total_hours = current_hours + hours_to_wait + extra_hours
    final_hours = total_hours % 24

    return final_hours, final_minutes


def main():
    # Prmopt the user for the current time in hours and minutes on a 24-hour clock
    current_time = input("Enter the current time in 'HH:MM' format (24-hour clock): ")
    current_hours, current_minutes = map(int, current_time.split(':'))

    # Prompt the user for the number of hours and minutes to wait for the alarm
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
    minutes_to_wait = int(input("Enter the number of minutes to wait for the alarm: "))

    # Calculate the alarm time
    alarm_hours, alarm_minutes = calculate_alarm_time(current_hours, current_minutes, hours_to_wait, minutes_to_wait)

    # Display the time when the alarm will go off
    print(f"The alarm will go off at {alarm_hours:02}:{alarm_minutes:02}.")

    # Prompt the user if they want to set another alar
    set_another_alarm = input("Do you want to set another alarm? (yes/no): ").strip().lower()
    if set_another_alarm == 'yes':
        main()


if __name__ == "__main__":
    main()
