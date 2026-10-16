\# Lab 5: Static Code Analysis — Issue Documentation



\*\*Program:\*\* `radio\_schedule.py`



\*\*Tools used:\*\* Pylint, Bandit, Flake8



\## Identified Issues and Fixes



| Issue | Type | Line(s) in Original Code | Description | Fix Approach |

|---|---|---|---|---|

| Hardcoded studio password | Security — Low severity | 5 | The studio password was stored directly in the source code, which could expose sensitive information. | Removed the hardcoded password from the program. |

| SQL injection risk | Security — Medium severity | 11 | SQL values were inserted into a query using string formatting, which could allow malicious input to alter the query. | Replaced string formatting with parameterized SQL queries using placeholders (`?`). |

| Unsafe `eval()` usage | Security — Medium severity | 21 | The program used `eval()` to execute a formula string, which could execute unintended code. | Removed `eval()` and replaced it with a direct check for the example formula used by the program. |

| Missing module docstring | Code quality | 1 | The module did not have a docstring describing its purpose. | Added a module-level docstring explaining the program's purpose. |

| Missing function docstrings | Code quality | Multiple | Functions did not have docstrings explaining what they do. | Added docstrings to the functions. |

| Non-standard function naming | Code quality | Multiple | Function names used camelCase rather than Python's conventional snake\_case naming style. | Renamed functions using snake\_case, such as `add\_slot`, `slot\_label`, `morning\_shows`, and `remove\_slot`. |

| Use of a global variable | Code quality | 6, 9 | The `booked\_minutes` variable was modified using a `global` statement, increasing reliance on shared state. | Removed the global variable and passed the database connection to the functions that need it. |

| Long lines | Code style — Flake8 E501 | 4, 11, 27 | Several source lines exceeded the configured maximum line length. | Split long SQL statements and other expressions across multiple lines. |

| Multiple statements on one line | Code style — Flake8 E701 | 27 | An `if` statement and its return statement appeared on the same line, reducing readability. | Expanded the conditional and return statement onto separate lines. |

| Non-f-string formatting | Code quality | 15 | The program used `.format()` for a simple string interpolation. | Replaced it with an f-string for readability. |

| Missing final newline | Code style — Pylint C0304 | End of file | The source file did not end with a newline character. | Added a newline at the end of the file. |



\## Verification Results



| Tool | Before | After |

|---|---|---|

| Pylint | 2.41/10 | 10.00/10 |

| Bandit | 3 findings: 1 Low and 2 Medium | No issues identified |

| Flake8 | 4 reported formatting violations | No errors reported |



\## Conclusion



Static code analysis helped identify security risks, code quality problems, and formatting violations in the original radio scheduling program. Parameterized SQL queries removed the identified SQL injection risk, and removing `eval()` eliminated the unsafe dynamic evaluation pattern. Improvements to naming, documentation, function structure, and formatting made the program easier to read and maintain. The final checks reported a Pylint score of 10.00/10, no Bandit issues, and no Flake8 errors.

