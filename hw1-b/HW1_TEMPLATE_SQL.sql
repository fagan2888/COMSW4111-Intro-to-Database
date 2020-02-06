DROP TABLE IF EXISTS BOB;
DROP TABLE IF EXISTS AverageHeight;


/*QUESTION 0
EXAMPLE QUESTION
What is the highest salary in baseball history?
*/
Select 1
;
/*SAMPLE ANSWER*/
SELECT MAX(salary) as Max_Salary
FROM Salaries;

/*QUESTION 1
Select the first name, last name, and given name of players who are between 6 ft and 6 ft 5 inches
[hint]: Use "People"
*/
SELECT 1, 1, 1 -- replace with your code
;

/*QUESTION 2
Create a Table of all the distinct players with a first name of Bob who were born in the United States and
played at Stanford university
Include their first name, last name, playerID, and birth state
[hint] Use a Join between People and CollegePlaying
*/
CREATE Table BOB
-- replace with your code
;


/*QUESTION 3
Group together players with the same birth year, and report the year, 
 the number of players in the year, and average height for the year
 Order the resulting by year in descending order. Put this in a new table called AverageHeight
 [hint] height will be NULL for some of these years, do not consider these entries
*/
CREATE TABLE AverageHeight
  -- replace with your code
;



/*QUESTION 4
Find the players who made it into the hall of fame who played for a college located in NJ
return the player ID, first name, last name, and school ID. Order the players by School alphabetically.
*/
SELECT 1, 1, 1, 1 -- replace with your code
;

/*QUESTION 5
Find the team id, yearid and average HBP for each team using a subquery.
Limit the total number of entries returned to 100
group the entries by team and year and order by descending values
[hint] be careful to only include entries where AB is > 0
*/
SELECT 1, 1, 1 -- replace with your code
;

/*OPTIONAL UNGRADED QUESTION  
Find the top 10 most common first names in Baseball history.
Find the top 10 most common first names that made it into the hall of fame in baseball history.
What have you learned?
*/
