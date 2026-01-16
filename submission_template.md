# AI Code Review Assignment (Python)

## Candidate
- Name: Birhanu Gudisa(bir13gud17@gmail.com)
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Denominator Mismatch(Incorrect Average Calculation Error): The code divides the sum of active orders by the count of all orders (including cancelled ones). This results in an incorrect, mathematically deflated average.
- ZeroDivisionError: If the input list orders is empty, len(orders) is 0. The final line total / count will raise a ZeroDivisionError.

### Edge cases & risks
- Division by Zero: If the input list orders is empty, len(orders) is 0, causing a ZeroDivisionError
- Missing Keys: The code assumes "status" and "amount" keys exist in every dictionary; missing keys will raise a KeyError
- None Types: If order["amount"] is None, adding it to total will raise a TypeError. 

### Code quality / design issues
- Iterating logic: The separation of the count calculation (outside loop) and the sum calculation (inside loop) is the root cause of the logic error.
- Lack of Input Validation: The function does not verify if the input is actually a list or if the values are numeric.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added a guard clause for empty input lists.
- Changed logic to only increment the count for orders that are actually summed (non-cancelled).
- Added .get() usage for dictionary access to prevent KeyError.
- Aligned Counters: Updated the logic to ensure the denominator only counts the specific orders included in the total.
- Added a check to ensure valid_count > 0 before dividing.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty List: To ensure no crashes (ZeroDivisionError).
- Mixed List: A list containing accepted, cancelled, and pending orders to verify the math excludes cancelled items from both the numerator and denominator.
- Malformed Data: Dictionaries missing the "amount" key or having None as the amount.
- All Cancelled: To ensure the function handles a divisor of zero gracefully when the input list itself wasn't empty.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Inaccurate: It claims to "correctly exclude cancelled orders from the calculation," but the code only excludes them from the sum, not the count.
- Omission: It fails to mention the crash risk on empty inputs.

### Rewritten explanation
- This function calculates the average order value by filtering for non-cancelled orders. It sums the amounts of valid orders and divides that sum by the count of those specific valid orders (not the total input count), ensuring the average reflects only completed transactions. It also handles empty inputs or scenarios with zero valid orders by returning 0.0. 

## 4) Final Judgment
- Decision: Request Changes
- Justification: The logic contains a fundamental mathematical error (mismatched numerator/denominator) that produces incorrect business data. Additionally, it lacks basic safety checks for empty inputs.
- Confidence & unknowns: High confidence. Unknowns include whether 0.0 or None is the preferred return type for no valid data.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
