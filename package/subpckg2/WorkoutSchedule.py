#Comments and Documentation implemented with ChatGPT

from tabulate import tabulate

class WorkoutSchedule:
    """
    A class to create, display, and customize a workout schedule with user input.
    """

    def __init__(self):
        self.workout_schedule = {}

    def generate_training_split(self):
        """
        Prompt the user to generate a workout schedule.
        """
        print("Welcome to the Workout Schedule Generator!")
        
        # Prompt user for input
        time_daily = int(input("How many minutes do you want to work out daily? "))
        
        # Limit days per week to 7
        while True:
            days_per_week = int(input("How many days per week do you plan to work out? "))
            if 1 <= days_per_week <= 7:
                break
            print("Invalid input. Please enter a number between 1 and 7.")
        
        time_of_day = input("Do you prefer working out in the Morning, Afternoon, or Evening? ").capitalize()
        activity = input("What activity will you be doing? ")

        # Populate workout schedule
        for day in range(1, days_per_week + 1):
            self.workout_schedule[f"Day {day}"] = {
                "Activity": activity,
                "Time": f"{time_daily} minutes",
                "Period": time_of_day,
            }

        print("\nWorkout schedule created successfully!")

    def display_workout_schedule(self):
        """
        Display the generated workout schedule in a tabular format.
        """
        if not self.workout_schedule:
            print("No workout schedule found. Please generate one first.")
            return

        # Prepare data for tabulation
        headers = ["Day", "Activity", "Time", "Period"]
        table_data = [
            [day, details["Activity"], details["Time"], details["Period"]]
            for day, details in self.workout_schedule.items()
        ]

        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid", colalign=("center", "center", "center", "center")))

    def customize_workout_schedule(self):
        """
        Allow the user to customize their workout schedule.
        """
        if not self.workout_schedule:
            print("No workout schedule found. Please generate one first.")
            return

        print("\nCurrent Schedule:")
        self.display_workout_schedule()

        while True:
            day_to_edit = input("\nWhich day would you like to edit? (e.g., Day 1, Day 2). Enter 'End' to finish editing: ").strip()
            if day_to_edit.capitalize() == "End":
                print("Ending schedule customization.")
                break

            if day_to_edit not in self.workout_schedule:
                print("Invalid day. Please try again.")
                continue

            # Prompt user for new activity details
            new_activity = input(f"Enter the new activity for {day_to_edit}: ").strip()
            new_time = input(f"Enter the new time for {day_to_edit} (e.g., 45 minutes): ").strip()
            new_period = input(f"Enter the new time of day for {day_to_edit} (e.g., Morning, Afternoon, Evening): ").capitalize().strip()

            # Update the schedule
            self.workout_schedule[day_to_edit] = {
                "Activity": new_activity,
                "Time": new_time,
                "Period": new_period,
            }
            print(f"{day_to_edit} has been updated successfully!")