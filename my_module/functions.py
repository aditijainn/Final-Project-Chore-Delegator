import random

import itertools as it
import pandas as pd


class Chore():
    
    def __init__(self, name, duration, specific_day):
        
        self.name = name
        self.duration = duration
        self.specific_day = specific_day
        self.assigned_person = ''
        
        
def sort_duration(chore_list):
    """Orders chores from most to least time taken
    
    Parameters
    ----------
    chore_list : list 
        list of inputted chores by user
    
    Returns
    -------
    output : list 
        sorted list of chore objects
    """
    
    output = sorted(chore_list, key = lambda chore: 
                    chore.duration, reverse = True)
    
    return output


def assign_chores(chores, people):
    """Assigns chores to people based on duration
    
    Parameters
    ----------
    chores : list 
        list of inputted chores by user
    people : list
        list of people to share chores
    
    Returns
    -------
    all_chores : list 
        resulting list of chore objects
    """
    
    all_chores = sort_duration(chores)
    count = 0
    random.shuffle(people)
    
    for chore, person in zip(all_chores, it.cycle(people)):
        chore.assigned_person = person
        count =+ 1
        
        # shuffles the order of people every round for fairness
        if count == len(people):
            random.shuffle(people)
            count = 0   
            
    return all_chores
    
    
def least_work_day(week):
    """Finds the day with the least chore time
    
    Parameters
    ----------
    week : list 
        list of a list of chore objects, each
        element representing chores of each day
    
    Returns
    -------
    least_work_day : list 
        list of chore objects representing the
        chores for that day
    """
    
    least_work_day = week[0]
    least_time_taken = sum(chores.duration for chores in week[0])
    
    for day in week:
        total_time_taken = 0
        
        for chores in day:
            total_time_taken = total_time_taken + chores.duration
            
        if total_time_taken <= least_time_taken:
            least_time_taken = total_time_taken
            least_work_day = day
            
    return least_work_day


def divide_into_week(chores):
    """Divide chores into days based on assigned day or duration
    
    Parameters
    ----------
    chores : list 
        list of chore objects
    
    Returns
    -------
    week : list 
        list of a list of chore objects, each
        element representing chores of each day
    """
    
    distribute = []
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    
    for chore in chores:
        if chore.specific_day == None:
            distribute.append(chore)
        else:
            if chore.specific_day == 'Monday':
                monday.append(chore)
            elif chore.specific_day == 'Tuesday':
                tuesday.append(chore)
            elif chore.specific_day == 'Wednesday':
                wednesday.append(chore)
            elif chore.specific_day == 'Thursday':
                thursday.append(chore)
            elif chore.specific_day == 'Friday':
                friday.append(chore)
            elif chore.specific_day == 'Saturday':
                saturday.append(chore)
            elif chore.specific_day == 'Sunday':
                sunday.append(chore)
           
    week = [monday, tuesday, wednesday, thursday, 
            friday, saturday, sunday]
    distribute = sort_duration(distribute)
    
    for chore in distribute:
        least_work_day(week).append(chore)
        
    return week


def by_person(week, people):
    """Divide chores into a dict of each person's weekly chores
    
    Parameters
    ----------
    week : list 
        list of a list of chore objects, each
        element representing chores of each day
    people : list
        list of people to share chores
    
    Returns
    -------
    output : dictionary
        key - each person, value - array with each
        element representing chores of each day
    """
    
    sort = [[[] for b in range(len(week))] 
            for a in range(len(people))]
    i = 0
    people.sort()
    
    for day in week:
        day = sorted(day, key = lambda chore :
                     chore.assigned_person)
        j = 0
        
        for person in people:
            for chore in day:
                
                if person == chore.assigned_person: 
                    sort[j][i].append(chore.name)
                    
            j = j + 1
        i = i + 1
        
    output = dict(zip(people, sort))
    return output


def pandas_format(week, people):
    """Organises divided chores into a visual
    
    Parameters
    ----------
    week : list 
        list of a list of chore objects, each
        element representing chores of each day
    people : list
        list of people to share chores
    
    Returns
    -------
    output : pandas DataFrame
        table with chores corresponding to each
        person as columns and the days as rows   
    """
    
    output = pd.DataFrame(week, index = ['Mon', 'Tue',
             'Wed', 'Thur', 'Fri', 'Sat', 'Sun'])
    
    for person in people:
        output[person] = output[person].astype('string').apply(lambda x:
        x.replace('[','').replace(']','').replace('\'',''))
        
    return output


def chore_delegator(chore_list, people):
    """Combines functions to delegate chores
    
    Parameters
    ----------
    chore_list : list 
        list of inputted chores by user
    people : list
        list of people to share chores
    
    Returns
    -------
    output : pandas DataFrame
        table with chores corresponding to each
        person as columns and the days as rows   
    """
    
    week = divide_into_week(assign_chores(chore_list, people))
    result = by_person(week, people)
    output = pandas_format(result, people)
    
    return output
