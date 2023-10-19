The primary function of a foreign key in a database is to establish a link or relationship between two tables and to enforce referential integrity between them. 

Here are some refined answers to the question:

1. **Establish Relationships**: A foreign key creates a relationship between two tables by referencing a unique key, typically a primary key, in another table. This relationship allows for the structured organization of data in relational databases, enabling meaningful connections between related pieces of data.

2. **Enforce Referential Integrity**: By defining foreign key constraints, the database ensures that changes made to the referenced table (like deletions or updates) do not result in invalid data in the table containing the foreign key. For instance, if a record in the primary table is deleted, the database can be set to either prevent the deletion (if there are related records in the foreign key table) or to cascade the deletion to related records.

3. **Ensure Data Accuracy and Consistency**: Foreign keys help maintain data accuracy by ensuring that the data in the foreign key column matches values in the referenced table. This means you can't have a value in the foreign key column that doesn't exist in the corresponding primary key of the referenced table (unless it's NULL, and that's allowed by the schema).

4. **Facilitate Efficient Queries**: By establishing relationships between tables, foreign keys allow for powerful and efficient SQL queries using JOIN operations. This helps in fetching related data from different tables in a single query.

5. **Promote Database Normalization**: Foreign keys are essential components of normalized database schemas, especially in the third normal form (3NF). They help in avoiding data redundancy and ensure that data is stored logically.

Among these answers, the most encompassing one is the enforcement of referential integrity, as it captures the essence of why foreign keys are critical in relational databases. However, all these answers provide different facets of the importance and function of foreign keys.