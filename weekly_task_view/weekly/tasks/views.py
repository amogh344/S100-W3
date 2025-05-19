from django.shortcuts import render

TASKS = {
    "sunday": "Plan the week ahead.",
    "monday": "Prepare for meetings.",
    "tuesday": "Grocery shopping.",
    "wednesday": "Workout session.",
    "thursday": "Clean the house.",
    "friday": "Family movie night.",
    "saturday": "Gardening and relaxation.",
}

def index(request):
    days = list(TASKS.keys())
    capitalized_days = [day.capitalize() for day in days]
    return render(request, 'index.html', {'days': capitalized_days})

def task_view(request, day):
    task = TASKS.get(day.lower(), "No task found.")
    return render(request, 'day.html', {'day': day.capitalize(), 'task': task})