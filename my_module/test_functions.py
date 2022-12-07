import functions as c

# defining variables I'm using throughout the test_file
chorelist = [c.Chore('Scrub sink', 15, None), c.Chore('Cook', 30, 'Tuesday'), 
             c.Chore('Wash Dishes', 25, None), c.Chore('Vacuum', 15, None), 
             c.Chore('Wash toilet', 20, None), c.Chore('Vacuum', 15, None), 
             c.Chore('Clean bathtub', 20, None), c.Chore('Laundry', 20, None), 
             c.Chore('Bleach sink', 20, None), c.Chore('Mop', 20, None), 
             c.Chore('Take out trash', 10, 'Friday'), c.Chore('Mop', 20, None)]
people = ["Aditi", "Sydney", "Becca", "Zohar"]

def test_sort_duration():
    test1 = [c.Chore('Take out trash', 10, 'Friday'), c.Chore('Wash Dishes', 25, None), 
             c.Chore('Vacuum', 15, None), c.Chore('Wash toilet', 20, None)]
    check1 = c.sort_duration(test1)
    assert check1[0] == test1[1]
    assert check1[1] == test1[3]
    assert check1[2] == test1[2]
    assert check1[3] == test1[0]

def test_assign_person():
    test2 = c.assign_chores(chorelist, people)
    check2 = sorted(test2, key = lambda chore : chore.assigned_person)
    assert check2[0].assigned_person and check2[1].assigned_person and check2[2].assigned_person == 'Aditi'
    assert check2[3].assigned_person and check2[4].assigned_person and check2[5].assigned_person == 'Becca'
    assert check2[6].assigned_person and check2[7].assigned_person and check2[8].assigned_person == 'Sydney'
    assert check2[9].assigned_person and check2[10].assigned_person and check2[11].assigned_person == 'Zohar'

def test_least_work_day():
    Monday = [c.Chore('Mop', 35, None), c.Chore('Broom', 30, 'Monday')]
    Tuesday = [c.Chore('Mop', 35, None), c.Chore('Broom', 30, 'Monday'), c.Chore('Wash Dishes', 45, 'Monday')]
    test3 = [Monday, Tuesday]
    check3 = c.least_work_day(test3)
    assert check3 == Monday

def test_divide_into_week():
    test4 = c.divide_into_week(chorelist)
    assert len(test4) == 7
    assert test4[1][0].specific_day == 'Tuesday'
    assert test4[4][0].specific_day == 'Friday'
