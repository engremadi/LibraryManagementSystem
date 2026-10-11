- **Standardized REST Operations:** Full CRUD lifecycle support using standard HTTP verbs (`GET`, `POST`, `PATCH`, `DELETE`).
- **Strict Data Contracts:** Separation of schemas into `BookCreator` (ingestion), `BookUpdate` (partial modification), and `Book` (persisted entity) using Pydantic V2.
- **Explicit HTTP Semantics:** Clean status handling including `201 Created` for resource creation and `204 No Content` for idempotent deletions.
- **Partial Mutation Handling:** Robust `PATCH` semantics leveraging `model_dump(exclude_unset=True)` to guarantee atomic-like in-place updates.
- **Interactive OpenAPI Documentation:** Native Swagger UI (`/docs`) and ReDoc (`/redoc`) integrations.

---

## 📂 Project Structure
```text
.
├── main.py              # Application entry point, routing, and business logic
└── README.md            # Technical documentation