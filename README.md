# ACTTherapyHelper
ACT Therapy Helper Application, for recording thoughts and detecting trends

# To Do
## Next in line
1)  Make a base template with header/footer
2)  Integrate gmail login
3)  Make two index pages, one for logged in, one for not
4)  Add/Edit Errands
5)  Figoure how to push notifications to users who accept it
6)  Integrate celery to run background tasks
7)  Tie together making an errand and then creating a background task via celery


## Views
Login page - Gmail login

Thought logger for logging problematic thoughts, and what was associated with them

Activity Creator

If problmatic - walk through page

Trends view - emotions per day/week/month

End of day review

Morning preview?

## Models
Problably want to allow user to select time of thought, but auto pick now

Daily to do list and what times - routines

One off to do list - errands/one shots

Way to select what days to repeat a routine for - many to many to weekday field

## Big picture\User Story
User wakes up, gets a notification that its time for their
morning routine.  Click notification, log thoughts, if problematic walk through, and 30 minutes  later check that
it was completed.  This will functiont he same for routine lists
or daily todos like walking/reading/gutiar etc

For one off todos - user gets alert its time for errand X at
predetermined time by user.  User fills out thought log, and then 30 minutes later gets a checkup if they completed it.

These 30 minute later check ups can be delayed, but must eventually be answered as yes i did it or no im not doing it today. - Choice to push the todo to another date.
