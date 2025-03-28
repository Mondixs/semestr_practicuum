# Models for Django Application

## `QuestionViewSet` Model

- **Table Name**: `questionviewset`
- **Fields**:
  - `queryset`: `Question.objects.all()`
  - `serializer_class`: `QuestionSerializer`

---

## `ChoiceViewSet` Model

- **Table Name**: `choiceviewset`
- **Fields**:
  - `queryset`: `Choice.objects.all()`
  - `serializer_class`: `ChoiceSerializer`

---

## `StudentViewSet` Model

- **Table Name**: `studentviewset`
- **Fields**:
  - `queryset`: `Student.objects.all()`
  - `serializer_class`: `StudentSerializer`