| Sprint | User Story                                                                 | Implementation        | Test Case                               | Git Tag |
|--------|-----------------------------------------------------------------------------|-----------------------|------------------------------------------|---------|
| 1      | As a librarian, I want to add books to the system                            | add_book()            | test_add_book_success()                  | v0.1    |
|        | As a librarian, I want to prevent duplicate book IDs                         | add_book()            | test_add_duplicate_id_raises_error()     | v0.1    |
|--------|-----------------------------------------------------------------------------|-----------------------|------------------------------------------|---------|
| 2      | As a librarian, I want to allow users to borrow books                        | borrow_book()         | test_borrow_book_success()               | v0.2    |
|        | As a librarian, I want to prevent borrowing unavailable books               | borrow_book()         | test_borrow_unavailable_book_error()     | v0.2    |
|        | As a librarian, I want to allow users to return books                        | return_book()         | test_return_book_update_status()          | v0.2    |
|--------|-----------------------------------------------------------------------------|-----------------------|------------------------------------------|---------|
| 3      | As a librarian, I want to generate library reports                           | generate_report()     | test_generate_report()                   | v0.3    |
