def display_study_hours():
    # Read the inputs, calculate total and print it
    study_hours = int(input())
    study_days = int(input())
    
    total_study_hours = study_hours * study_days

    print(f"Total Study Hours: {total_study_hours}")

display_study_hours()