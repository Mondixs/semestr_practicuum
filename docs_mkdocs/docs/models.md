# Models for Django Application

## `Question` Model

- **Table Name**: `question`
- **Fields**:
  - `id`: Auto-incrementing primary key (implicit in Django).
  - `question_text`: `CharField`, max length 200 characters.
  - `pub_date`: `DateTimeField`.
  
### Methods:
- `__str__()` returns the value of `question_text`.
- `was_published_recently()` checks if the question was published within the last day.

---

## `Choice` Model

- **Table Name**: `choice`
- **Fields**:
  - `id`: Auto-incrementing primary key (implicit in Django).
  - `question`: Foreign Key to `Question` model (`on_delete=models.CASCADE`).
  - `choice_text`: `CharField`, max length 200 characters.
  - `votes`: `IntegerField`, default value is 0.

### Methods:
- `__str__()` returns the value of `choice_text`.

---

## `Student` Model

- **Table Name**: `student`
- **Fields**:
  - `id`: Auto-incrementing primary key (implicit in Django).
  - `name`: `CharField`, max length 100 characters.
  - `gender`: `CharField`, max length 10 characters with choices: `['Male', 'Female']`.
  - `age`: `IntegerField`.
  - `city`: `CharField`, max length 100 characters.
  - `academic_pressure`: `FloatField`.
  - `study_satisfaction`: `FloatField`.

### Methods:
- `__str__()` returns the value of `name`.