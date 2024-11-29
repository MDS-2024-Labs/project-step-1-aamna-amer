{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1fd4fff-6ec8-40b4-83a8-6bd2711a6924",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tabulate import tabulate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3a17679-7a0e-493e-af0d-4ade502d2722",
   "metadata": {},
   "outputs": [],
   "source": [
    "class PersonalSummary:\n",
    "    def __init__(self):\n",
    "        #the init method is empty as there is nothing to initialize\n",
    "        pass\n",
    "        \n",
    "    def collect_info(self):\n",
    "        self.name = input(\"Enter your name:\")\n",
    "        self.height = float(input(\"Enter your height in cm\"))\n",
    "        self.weight = float(input(\"Enter your weight in kg\"))\n",
    "        self.age = int(input(\"Enter your age\"))\n",
    "        self.gender = input(\"Enter your gender, M or F\")\n",
    "        \n",
    "    \n",
    "    #def set_goals(self):\n",
    "    #weight loss, fat loss, muscle gain\n",
    "    #i think change to calculate_BMI and make Goals its own module\n",
    "        \n",
    "    def display_ps(self):\n",
    "        headers = [\"Name\", \"Age\", \"Height\", \"Weight\", \"Gender\"]\n",
    "        data = [[self.name, self.age, self.height, self.weight, self.gender]]\n",
    "        \n",
    "        print(tabulate(data, headers=headers, tablefmt=\"grid\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
