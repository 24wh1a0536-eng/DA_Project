#pip install pandas openpyxl matplotlib
#python a.py
#python graph1.py
#python graph2.py

## Introduction

The project **“Where Does a College Student’s Money Go?”** was conducted to understand how college students receive, spend, save, and manage their money. The survey collected responses from 35 college students and focused on their monthly financial habits, major spending categories, savings, budgeting, expense tracking, and unplanned purchases.

## Objective

The main objectives of the analysis were:

* To identify the major spending categories among college students.
* To understand students’ monthly saving habits.
* To examine how students manage and track their expenses.
* To study monthly budgeting behavior.
* To identify the frequency of unplanned purchases.
* To understand which expenses students would like to reduce.
* To examine relationships between variables such as living arrangement, spending, budgeting, savings, and unplanned purchases.
* To identify patterns in the collected data and make cautious pattern-based predictions.

## Dataset

The survey contains **35 student responses** collected through an online questionnaire. The questionnaire contains 12 main questions covering students’ education level, living arrangement, source of money, monthly money, savings, spending habits, expense tracking, budgeting, unplanned purchases, and desired spending reductions.

## Methodology

The analysis was performed using **Python, Pandas, and Matplotlib**.

The following steps were used:

1. **Data collection** – Responses were collected through the survey.
2. **Data loading** – The Excel response file was imported into Python.
3. **Data inspection** – The columns, number of responses, and response categories were examined.
4. **Descriptive analysis** – Frequencies and percentages were calculated for individual questions.
5. **Data visualization** – Bar charts were created to represent the distribution of responses.
6. **Cross-analysis** – Relationships between selected variables were examined using cross-tabulation.
7. **Pattern identification** – Recurring trends in spending, saving, and financial behavior were identified.
8. **Pattern-based prediction** – Possible tendencies for similar student groups were inferred from the observed sample.
9. **Interpretation** – The findings were converted into meaningful observations and conclusions.

## Main Findings

### Student Profile

The dataset contains 35 students. The sample is strongly concentrated among third-year students, with **32 students (91.4%)** belonging to the third year.

Regarding living arrangements:

* **17 students (48.6%)** live in hostels.
* **13 students (37.1%)** live with their parents.
* **5 students (14.3%)** live in PG accommodation.

The majority of students, **32 out of 35 (91.4%)**, reported receiving money mainly from their parents or family.

### Spending Patterns

Food was the most frequently reported major spending category, selected by **21 students (60%)**. Education was reported by 10 students (28.6%), transportation by 3 students (8.6%), and entertainment by 1 student (2.9%).

This indicates that food-related expenses form a major part of the reported spending behavior in this sample.

### Savings

Savings were relatively low among the surveyed students:

* **15 students (42.9%)** reported saving nothing.
* **17 students (48.6%)** reported saving less than ₹500.
* Only **3 students (8.6%)** reported saving ₹500 or more.

Therefore, **32 out of 35 students (91.4%)** reported either no savings or savings below ₹500.

### Budgeting

Monthly budgeting was not common among the respondents:

* **21 students (60%)** said they do not usually plan a monthly budget.
* **7 students (20%)** said they do.
* **7 students (20%)** said they sometimes plan a budget.

This shows that formal monthly budgeting was not a regular practice for most students in the sample.

### Expense Tracking

Expense tracking showed mixed behavior:

* 17 students (48.6%) track expenses sometimes.
* 9 students (25.7%) track expenses rarely.
* 5 students (14.3%) track expenses regularly.
* 4 students (11.4%) never track their expenses.

The largest group therefore tracks expenses only occasionally.

### Unplanned Purchases

Unplanned purchases were also examined. The most common response was **“rarely”**, indicating that although unplanned purchases occur, they were not reported as frequent behavior by most respondents.

The cross-analysis also showed that students who do not plan a monthly budget do not necessarily make frequent unplanned purchases. Therefore, the survey does not support a simple conclusion that lack of budgeting automatically causes frequent impulse purchases.

### Expenses Students Want to Reduce

Food was also the most frequently selected category that students wanted to reduce, with **14 students (40%)** selecting it.

Shopping and other expenses were each selected by 6 students (17.1%).

This is consistent with the finding that food is the largest reported major spending category.

## Cross-Analysis

Three major relationships were examined:

### Living Arrangement vs Major Spending

Food remained the leading major spending category among students living in hostels, PGs, and with parents in this sample.

### Budgeting vs Unplanned Purchases

The relationship did not show a simple direct pattern between budgeting and unplanned purchases. Students who did not budget were not necessarily frequent unplanned buyers.

### Budgeting vs Savings

The comparison between budgeting behavior and savings provides additional information about whether students who plan their finances also report different saving patterns. However, because the sample contains only 35 responses, these relationships should be interpreted as observations rather than statistically proven relationships.

## Patterns Identified

The overall analysis reveals several recurring patterns:

1. **Food is a major expense** – Food was the most commonly reported major spending category and was also the expense most frequently identified for reduction.

2. **Savings are generally low** – 91.4% of respondents reported either no savings or savings below ₹500.

3. **Budgeting is not common** – 60% of respondents reported that they do not usually plan a monthly budget.

4. **Expense tracking is mostly occasional** – The largest group of students tracks expenses only sometimes.

5. **Family support is the main source of money** – 91.4% of respondents reported parents or family as their main source of money.

6. **Living arrangement does not eliminate food expenditure** – Food was the leading spending category across the different living arrangements represented in this sample.

7. **Budgeting and unplanned purchases do not show a simple relationship** – The data does not support the assumption that students who do not budget automatically make frequent unplanned purchases.

## Pattern-Based Prediction

Based on the observed patterns, if a similar group of college students were surveyed, food is likely to remain one of the commonly reported major spending categories. Low or limited monthly savings and informal budgeting may also continue to appear among students.

However, these are **pattern-based predictions rather than machine-learning predictions**. The sample contains only 35 responses and therefore cannot reliably represent all college students.

## Limitations

The analysis has several limitations:

* The sample size is only 35 students.
* The sample is heavily concentrated among third-year students.
* Most financial questions use ranges rather than exact monetary values.
* Question 4 combines **money received/spent**, so it should not be interpreted as a precise income or expenditure measurement.
* The survey represents the behavior of the respondents and cannot automatically be generalized to all college students.
* Cross-analysis can identify patterns, but it does not by itself prove cause-and-effect relationships.

## Conclusion

The analysis of 35 college-student responses provides an overview of how students receive, spend, save, and manage their money. The results show that **food is the dominant reported spending category**, while savings are generally low. A large proportion of students reported saving nothing or less than ₹500 per month.

The analysis also shows that **monthly budgeting is not a common practice**, with most respondents saying that they do not regularly plan a monthly budget. Expense tracking is more commonly performed occasionally rather than regularly. At the same time, unplanned purchases were generally reported as occurring rarely, showing that the absence of formal budgeting does not necessarily mean frequent unplanned spending.

The cross-analysis provided additional insight into student financial behavior. Food remained an important spending category across different living arrangements, while the relationship between budgeting and unplanned purchases did not show a simple direct pattern.

Overall, the survey suggests that the students in this sample rely strongly on family support, spend a significant portion of their money on food, have relatively limited savings, and often manage their finances informally rather than through structured monthly budgeting.

The findings can help highlight areas where students may benefit from greater awareness of **budget planning, expense tracking, and saving habits**. However, because the study is based on only 35 responses and is heavily concentrated among third-year students, the results should be considered representative of this sample rather than all college students.

Thus, the project demonstrates how survey data can be transformed into meaningful information through **data cleaning, descriptive statistics, visualization, cross-analysis, pattern identification, and cautious prediction**.
