{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1608e68e-4a4f-4330-848d-5df7c002b3d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class EnergyRequirements(PersonalSummary):\n",
    "    def __init__(self, personal_sum):\n",
    "        PersonalSummary.__init__(self)\n",
    "        self.personal_sum = personal_sum\n",
    "        \n",
    "    def calculate_RMR(self):\n",
    "        if self.personal_sum.gender == \"M\":\n",
    "            #RMR equation\n",
    "            self.RMR = (9.99*self.personal_sum.weight) + (6.25*self.personal_sum.height) - (4.92*self.personal_sum.age) + 5\n",
    "            return self.RMR\n",
    "        else:\n",
    "            #RMR equation\n",
    "            self.RMR = (9.99*self.personal_sum.weight) + (6.25*self.personal_sum.height) - (4.92*self.personal_sum.age) - 161\n",
    "            return self.RMR\n",
    "    \n",
    "    def activity_level(self):\n",
    "        columns = [\"Sedentary\", \"Lightly Active\", \"Moderately Active\", \"Very Active\", \"Extra Active\"]\n",
    "        table = [[\"little to no activity\", \n",
    "                  \"1-3 days per week of light activity\",\n",
    "                  \"moderate exercise 3-5 days per week\",\n",
    "                  \"rigorous exercise, 6-7 days per week\",\n",
    "                  \"professional athlete, labor job, 2-3 times per day\"]] \n",
    "        \n",
    "        transposed_table = list(zip(*table))\n",
    "        \n",
    "        print(\"Please pick the appropriate activity level:\")\n",
    "        print(tabulate(transposed_table, headers=[\"Activity Level\", \"Description\"], tablefmt=\"grid\", showindex=columns))\n",
    "        \n",
    "        self.activitylevel = input(\"Activity Level:\")\n",
    "       \n",
    "        \n",
    "    def calculate_TDEE(self):\n",
    "        if self.activitylevel == \"Sedentary\":\n",
    "            self.TDEE = self.RMR * 1.2\n",
    "            return self.TDEE\n",
    "        elif self.activitylevel == \"Lightly Active\":\n",
    "            self.TDEE = self.RMR * 1.375\n",
    "            return self.TDEE\n",
    "        elif self.activitylevel == \"Moderately Active\":\n",
    "            self.TDEE = self.RMR * 1.55\n",
    "            return self.TDEE\n",
    "        elif self.activitylevel == \"Very Active\":\n",
    "            self.TDEE = self.RMR * 1.725\n",
    "            return self.TDEE\n",
    "        elif self.activitylevel == \"Extra Active\":\n",
    "            self.TDEE = self.RMR * 1.9\n",
    "            return self.TDEE\n",
    "            "
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
