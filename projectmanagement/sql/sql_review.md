#### SQL Review

![](images/sqlReview_1.png)

---

#### Answers

1. `SELECT * FROM north_american_cities WHERE country = 'Canada';`
   ![](images/sqlReview_2.png)

2. `SELECT * FROM north_american_cities WHERE country = 'United States' ORDER BY latitude DESC;`
   ![](images/sqlReview_3.png)

3. `SELECT * FROM north_american_cities WHERE longitude < -88 ORDER BY longitude ASC;`
   ![](images/sqlReview_4.png)

4. `SELECT city FROM north_american_cities WHERE country = 'Mexico' ORDER BY population DESC LIMIT 2;`
   ![](images/sqlReview_5.png)

5. `SELECT city, population FROM north_american_cities WHERE country = 'United States' ORDER BY population DESC LIMIT 2 OFFSET 2;`
   ![](images/sqlReview_6.png)
