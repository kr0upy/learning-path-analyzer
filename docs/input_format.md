# Input CSV Format for Learning Path Analyzer

The CSV file with student logs must have the following columns:

| Column Name  | Type       | Description                                         | Required |
|-------------|-----------|-----------------------------------------------------|---------|
| student_id  | integer   | Unique identifier for each student                 | Yes     |
| timestamp   | datetime  | Date and time of the event                          | Yes     |
| event_type  | string    | Type of activity (login, quiz_attempt, assignment_submission, forum_post) | Yes |
| resource    | string    | Name of the resource (quiz, homework, forum)       | Yes     |
| score       | float     | Score achieved (leave empty for events like login) | No      |

Example:

```csv
student_id,timestamp,event_type,resource,score
1,2024-03-01 09:00,login,system,
1,2024-03-02 12:00,quiz_attempt,quiz_1,78
