# ATTENDANCE TRACKER: GROSPE & PADOJINOG
from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.getLogger("matplotlib").setLevel(logging.ERROR)

week = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

days_list = []
absents_list = []

def attendance_tracker(e):
    document.getElementById("output").innerHTML = ""
    weekday = document.getElementById("weekday").value
    absence_text = document.getElementById("absence").value

    if weekday == "" or absence_text == "":
        display("Please complete all fields first.", target="output")
        return

    absence = int(absence_text)

    days_list.append(weekday)
    absents_list.append(absence)
  
    plt.figure()
    plt.plot(days_list, absents_list, marker="o")
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    display(plt, target="output")
