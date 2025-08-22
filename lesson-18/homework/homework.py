import pandas as pd
df = pd.read_csv('task/stackoverflow_qa.csv')
# df.head()

df['creationdate'] = pd.to_datetime(df['creationdate'])
# 1.	Find all questions that were created before 2014
before_2014 = df['creationdate'].dt.year<2014
df[before_2014]

# 2.	Find all questions with a score more than 50
score_more_50 = df['score']>50
df[score_more_50]
# 3.	Find all questions with a score between 50 and 100
score_between_50_100 = df['score'].between(50, 100)
df[score_between_50_100]
# 4.	Find all questions answered by Scott Boston

answered_questions_by = df['ans_name']=='Scott Boston'
df[answered_questions_by]
# 5.	Find all questions answered by the following 5 users
users = df['quest_name'].isin(['Jason Strimpel', 'DarkAnt', 'David Underhill', 'Hariprasad Manoharan', 'user814005'])
df[users]
# 6.	Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.


df['creationdate'] = pd.to_datetime(df['creationdate'])

start_date = pd.Timestamp('2014-03-01')
end_date = pd.Timestamp('2014-10-01')

mask_date = df['creationdate'].between(start_date, end_date)
mask_answered = df['ans_name'].str.lower() == 'unutbu'   
mask_score = df['score'] < 5

df[mask_date & mask_answered & mask_score]

# final_mask = mask_date & mask_answered & mask_score

# result = df.loc[final_mask]

# result

# 7.	Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

score_between_5_10 = df['score'].between(5, 10)
viewcount_10 = df['viewcount']>10000

df[score_between_5_10 & viewcount_10]

# # 8.	Find all questions that are not answered by Scott Boston

not_answered_name =df['ans_name'] !='Scott Boston'

df[not_answered_name]

# Homework 3:
# Titanic data set, stored as CSV. The data consists of the following data columns:
# •	PassengerId: Id of every passenger.
# •	Survived: Indication whether passenger survived. 0 for yes and 1 for no.
# •	Pclass: One out of the 3 ticket classes: Class 1, Class 2 and Class 3.
# •	Name: Name of passenger.
# •	Sex: Gender of passenger.
# •	Age: Age of passenger in years.
# •	SibSp: Number of siblings or spouses aboard.
# •	Parch: Number of parents or children aboard.
# •	Ticket: Ticket number of passenger.
# •	Fare: Indicating the fare.
# •	Cabin: Cabin number of passenger.
# •	Embarked: Port of embarkation.
import pandas as pd
titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head()
# PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked
# 1	0	3	Braund, Mr. Owen Harris	male	22.0	1	0	A/5 21171	7.2500	NaN	S
# 2	1	1	Cumings, Mrs. John Bradley (Florence Briggs Th.)	female	38.0	1	0	PC 17599	71.2833	C85	C
# 3	1	3	Heikkinen, Miss. Laina	female	26.0	0	0	STON/O2. 3101282	7.9250	NaN	S
# 4	1	1	Futrelle, Mrs. Jacques Heath (Lily May Peel)	female	35.0	1	0	113803	53.1000	C123	S
# 5	0	3	Allen, Mr. William Henry	male	35.0	0	0	373450	8.0500	NaN	S
# 1.	Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
female_passenger = titanic_df['Sex']=='female'
class_1 = titanic_df['Pclass']==1
ages = titanic_df['Age'].between(20, 30)

titanic_df[female_passenger & class_1 & ages]

# 2.	Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
fare_100=titanic_df['Fare']>100
titanic_df[fare_100]

# 3.	Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
survived_yes = titanic_df['Survived']==0
siblings = titanic_df['SibSp']==0
parents_children = titanic_df['Parch']==0
titanic_df[survived_yes & siblings & parents_children]

# 4.	Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
passenger_c = titanic_df['Embarked'].str.lower().str.startswith('c')
fare_50 = titanic_df['Fare']>50

titanic_df[passenger_c & fare_50]
# 5.	Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
siblings_abroad = titanic_df['SibSp']>0
parents_abroad = titanic_df['Parch']>0

titanic_df[siblings_abroad | parents_abroad]
# 6.	Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
age_under_15 = titanic_df['Age']<=15
survived_no = titanic_df['Survived']==1

titanic_df[age_under_15 & survived_no]
# 7.	Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
cabin_not_nan = titanic_df['Cabin'] !='NaN'
fare_greater_200 = titanic_df['Fare']>200

titanic_df[cabin_not_nan & fare_greater_200]
# 8.	Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
odd_passengerid = titanic_df['PassengerId'] % 2 !=0
titanic_df[odd_passengerid]

# 9.	Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
unique_ticket = ~titanic_df['Ticket'].str.contains('/')

titanic_df[unique_ticket]

# 10.	Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
passenger_ms = titanic_df['Name'].str.contains('Miss.')
cabin_1 = titanic_df['Pclass']==1
titanic_df[passenger_ms & cabin_1]
