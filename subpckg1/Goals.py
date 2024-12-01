from subpckg1.PersonalSummary import PersonalSummary
from subpckg1.EnergyRequirements import EnergyRequirements
from tabulate import tabulate

class Goals(EnergyRequirements):
    """
    Goals will calculate the client's new caloric intake based on their goals of weight loss/gain
    and the timeline of when they want to acheive them. Goals will inherit EnergyRequirements

    """

    def __init__(self):
        #initialize the inheriance
        EnergyRequirements.__init__(self)

    def goal_setting(self):
        "Will ask user if their goal is weight loss or weight gain, how much weight differential, and the timeline"

        self.goal = input("What is your main goal: weight loss or weight gain?")

        #determine weight gain or weight loss, and timeline
        if self.goal == "weight loss":
            self.weight_loss = int(input("How much weight do you want to lose? Please enter in lbs"))
            self.timeline = int(input("By when do you want to acheive this? Please answer in days"))
        else:
            self.weight_gain = int(input("How much weight do you want to gain? Please enter in lbs"))
            self.timeline = int(input("By when do you want to acheive this? Please answer in days"))


    def caloric_change(self):
        "Calculate caloric change needed for goal weight loss/gain. This is based off that 1 lb = 3500 calories"

        #caloric change = desired weight loss/gain (pounds) x 3500/ number of days
        if self.goal == "weight loss":
            #for weight loss. adding negative sign to make this variable negative for later use
            self.caloric_change = -((self.weight_loss * 3500)/self.timeline)
        else:
            #for weight gain
            self.caloric_change = (self.weight_gain * 3500)/self.timeline

        return self.caloric_change

    def caloric_intake(self):
        "Calculate client's new caloric intake based on goals and maintenance calories"

        self.caloric_change()  #calculate caloric change

        #new caloric intake = maintenance calories - caloric change. using + as weight loss will already have been made negative
        self.caloric_intake = round(self.TDEE + self.caloric_change)
        print("Your new daily caloric intake is ", round(self.caloric_intake))
