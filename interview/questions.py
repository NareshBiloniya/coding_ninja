


SEED_QUESTIONS = [
    # ------------------ ASSOCIATE (Basic) ------------------
    {
        "id": "q1",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "Write a formula to sum the values in cells A1 through A10.",
        "expected": "=SUM(A1:A10)",
        "grading_hints": ["SUM"]
    },
    {
        "id": "q2",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "How do you calculate the average of values in B1:B20?",
        "expected": "=AVERAGE(B1:B20)",
        "grading_hints": ["AVERAGE"]
    },
    {
        "id": "q3",
        "role": "associate",
        "difficulty": "basic",
        "type": "shortcuts",
        "prompt": "What shortcut do you use to copy a cell?",
        "expected": "Ctrl+C",
        "grading_hints": ["Ctrl+C"]
    },
    {
        "id": "q4",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "Which formula will return the number of cells that contain numbers in the range C1:C10?",
        "expected": "=COUNT(C1:C10)",
        "grading_hints": ["COUNT"]
    },
    {
        "id": "q5",
        "role": "associate",
        "difficulty": "basic",
        "type": "formatting",
        "prompt": "What feature allows you to quickly apply a set of formatting to a selected range?",
        "expected": "Cell Styles or Format Painter",
        "grading_hints": ["Format Painter", "Cell Styles"]
    },
    {
        "id": "q6",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "How do you find the largest value in the range D1:D100?",
        "expected": "=MAX(D1:D100)",
        "grading_hints": ["MAX"]
    },
    {
        "id": "q7",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "Write a formula to count non-empty cells in A1:A50.",
        "expected": "=COUNTA(A1:A50)",
        "grading_hints": ["COUNTA"]
    },
    {
        "id": "q8",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "How do you join the contents of cells A1 and B1 with a space in between?",
        "expected": "=A1 & \" \" & B1",
        "grading_hints": ["&", "CONCATENATE"]
    },
    {
        "id": "q9",
        "role": "associate",
        "difficulty": "basic",
        "type": "logical",
        "prompt": "If cell A1 contains 50, write a formula that returns TRUE if it is greater than 40.",
        "expected": "=A1>40",
        "grading_hints": [">"]
    },
    {
        "id": "q10",
        "role": "associate",
        "difficulty": "basic",
        "type": "theory",
        "prompt": "Name one Excel function used for text manipulation.",
        "expected": "LEFT / RIGHT / MID / LEN / CONCATENATE",
        "grading_hints": ["LEFT", "RIGHT", "MID", "LEN", "CONCATENATE"]
    },
    {
        "id": "q11",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "Write a formula to find the smallest value in the range E1:E50.",
        "expected": "=MIN(E1:E50)",
        "grading_hints": ["MIN"]
    },
    {
        "id": "q12",
        "role": "associate",
        "difficulty": "basic",
        "type": "shortcuts",
        "prompt": "What shortcut allows you to undo your last action?",
        "expected": "Ctrl+Z",
        "grading_hints": ["Ctrl+Z"]
    },
    {
        "id": "q13",
        "role": "associate",
        "difficulty": "basic",
        "type": "thinking",
        "prompt": "If A1=10 and B1=20, write a formula to return the larger of the two values.",
        "expected": "=MAX(A1,B1)",
        "grading_hints": ["MAX"]
    },
    {
        "id": "q14",
        "role": "associate",
        "difficulty": "basic",
        "type": "learning_attitude",
        "prompt": "If you don’t know a formula, what Excel feature can help you discover it?",
        "expected": "Formula Builder / Insert Function",
        "grading_hints": ["Insert Function", "Formula Builder"]
    },
    {
        "id": "q15",
        "role": "associate",
        "difficulty": "basic",
        "type": "formula",
        "prompt": "Write a formula to round 4.567 to 2 decimal places.",
        "expected": "=ROUND(4.567,2)",
        "grading_hints": ["ROUND"]
    },

    # ------------------ ABOVE ASSOCIATE (Intermediate) ------------------
    {
        "id": "q16",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to look up the value in cell B2 within table A2:D100 and return the 4th column.",
        "expected": "=VLOOKUP(B2, A2:D100, 4, FALSE)",
        "grading_hints": ["VLOOKUP"]
    },
    {
        "id": "q17",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to extract 'Mar-2025' (MMM-YYYY) from a date in A2.",
        "expected": "=TEXT(A2, \"mmm-yyyy\")",
        "grading_hints": ["TEXT"]
    },
    {
        "id": "q18",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "How do you count only the cells greater than 100 in C1:C50?",
        "expected": "=COUNTIF(C1:C50, \">100\")",
        "grading_hints": ["COUNTIF"]
    },
    {
        "id": "q19",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Which function returns the current date and time?",
        "expected": "=NOW()",
        "grading_hints": ["NOW"]
    },
    {
        "id": "q20",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to get the last day of the month for the date in A2.",
        "expected": "=EOMONTH(A2,0)",
        "grading_hints": ["EOMONTH"]
    },
    {
        "id": "q21",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "How do you combine INDEX and MATCH to look up a value in row and column?",
        "expected": "=INDEX(B2:D100, MATCH(E1, A2:A100,0), MATCH(F1, B1:D1,0))",
        "grading_hints": ["INDEX", "MATCH"]
    },
    {
        "id": "q22",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "data_analysis",
        "prompt": "What Excel feature allows you to summarize large datasets dynamically by dragging and dropping fields?",
        "expected": "Pivot Table",
        "grading_hints": ["Pivot Table"]
    },
    {
        "id": "q23",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to round the value in A2 to the nearest integer.",
        "expected": "=ROUND(A2,0)",
        "grading_hints": ["ROUND"]
    },
    {
        "id": "q24",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to return TRUE if A1 is between 50 and 100.",
        "expected": "=AND(A1>=50, A1<=100)",
        "grading_hints": ["AND"]
    },
    {
        "id": "q25",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to replace all occurrences of 'Apple' with 'Orange' in cell A1.",
        "expected": "=SUBSTITUTE(A1,\"Apple\",\"Orange\")",
        "grading_hints": ["SUBSTITUTE"]
    },
    {
        "id": "q26",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "thinking",
        "prompt": "You have dates in column A, extract the month number for all rows.",
        "expected": "=MONTH(A1)",
        "grading_hints": ["MONTH"]
    },
    {
        "id": "q27",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Combine text in A1 and B1, but make sure all letters are uppercase.",
        "expected": "=UPPER(A1 & B1)",
        "grading_hints": ["UPPER", "&"]
    },
    {
        "id": "q28",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "How do you return the first 5 characters of cell A1?",
        "expected": "=LEFT(A1,5)",
        "grading_hints": ["LEFT"]
    },
    {
        "id": "q29",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "How do you remove extra spaces from a text in cell A1?",
        "expected": "=TRIM(A1)",
        "grading_hints": ["TRIM"]
    },
    {
        "id": "q30",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "learning_attitude",
        "prompt": "If you encounter an error like #REF!, what approach would you take to troubleshoot?",
        "expected": "Check formulas, cell references, and ranges",
        "grading_hints": ["Check formulas", "Check references"]
    },
    {
        "id": "q31",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "theory",
        "prompt": "What Excel function can be used to look up values from left to right?",
        "expected": "VLOOKUP",
        "grading_hints": ["VLOOKUP"]
    },
    {
        "id": "q32",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "data_analysis",
        "prompt": "How can you remove duplicate rows from a dataset in Excel?",
        "expected": "Remove Duplicates feature under Data tab",
        "grading_hints": ["Remove Duplicates"]
    },
    {
        "id": "q33",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to calculate the absolute value of A1.",
        "expected": "=ABS(A1)",
        "grading_hints": ["ABS"]
    },
    {
        "id": "q34",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "formula",
        "prompt": "Write a formula to count blank cells in B1:B50.",
        "expected": "=COUNTBLANK(B1:B50)",
        "grading_hints": ["COUNTBLANK"]
    },
    {
        "id": "q35",
        "role": "above_associate",
        "difficulty": "intermediate",
        "type": "thinking",
        "prompt": "You have numbers in A1:A10, write a formula to get the average of numbers greater than 50.",
        "expected": "=AVERAGEIF(A1:A10,\">50\")",
        "grading_hints": ["AVERAGEIF"]
    },

    # ------------------ SENIOR ASSOCIATE (Advanced) ------------------
    {
        "id": "q36",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "Write a formula using XLOOKUP to return the department from B2:B100 for employee in A2.",
        "expected": "=XLOOKUP(A2, A2:A100, B2:B100)",
        "grading_hints": ["XLOOKUP"]
    },
    {
        "id": "q37",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "What formula splits the text in A2 by space into multiple cells (new Excel versions)?",
        "expected": "=TEXTSPLIT(A2, \" \")",
        "grading_hints": ["TEXTSPLIT"]
    },
    {
        "id": "q38",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "data_analysis",
        "prompt": "Which Excel tool lets you connect to external data sources and clean/transform data?",
        "expected": "Power Query (Get & Transform)",
        "grading_hints": ["Power Query"]
    },
    {
        "id": "q39",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "How do you calculate running total in column B alongside daily sales in column A?",
        "expected": "=SUM($B$2:B2)",
        "grading_hints": ["SUM"]
    },
    {
        "id": "q40",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "vba",
        "prompt": "Write a one-line VBA macro to clear contents of Sheet1 cell A1.",
        "expected": "Worksheets(\"Sheet1\").Range(\"A1\").ClearContents",
        "grading_hints": ["ClearContents"]
    },
    {
        "id": "q41",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "What dynamic array formula returns unique values from A1:A100?",
        "expected": "=UNIQUE(A1:A100)",
        "grading_hints": ["UNIQUE"]
    },
    {
        "id": "q42",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "data_analysis",
        "prompt": "What Excel feature allows you to model data relationships across multiple tables?",
        "expected": "Power Pivot / Data Model",
        "grading_hints": ["Power Pivot", "Data Model"]
    },
    {
        "id": "q43",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "Write a formula to forecast the next value in a linear trend using existing data in A2:A10 and B2:B10.",
        "expected": "=FORECAST.LINEAR(next_x, B2:B10, A2:A10)",
        "grading_hints": ["FORECAST"]
    },
    {
        "id": "q44",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "logical",
        "prompt": "If A1 > 100 return 'High', else return 'Low'. Write the formula.",
        "expected": "=IF(A1>100,\"High\",\"Low\")",
        "grading_hints": ["IF"]
    },
    {
        "id": "q45",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "Write a formula to sort values in A1:A10 in ascending order (dynamic array).",
        "expected": "=SORT(A1:A10,1,TRUE)",
        "grading_hints": ["SORT"]
    },
    {
        "id": "q46",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "thinking",
        "prompt": "How would you find the top 3 sales values from column B?",
        "expected": "=LARGE(B1:B100,{1,2,3})",
        "grading_hints": ["LARGE"]
    },
    {
        "id": "q47",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "formula",
        "prompt": "Write a formula to generate a sequence of 10 numbers starting from 1.",
        "expected": "=SEQUENCE(10,1,1,1)",
        "grading_hints": ["SEQUENCE"]
    },
    {
        "id": "q48",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "theory",
        "prompt": "Name one way to create a dynamic dashboard in Excel.",
        "expected": "Pivot Chart / Slicers / Conditional Formatting / Form Controls",
        "grading_hints": ["Pivot Chart", "Slicers", "Conditional Formatting"]
    },
    {
        "id": "q49",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "learning_attitude",
        "prompt": "How do you keep updated with new Excel features?",
        "expected": "Follow Microsoft updates, blogs, Excel community, YouTube tutorials",
        "grading_hints": ["Microsoft updates", "Excel community", "tutorials"]
    },
    {
        "id": "q50",
        "role": "senior_associate",
        "difficulty": "advanced",
        "type": "thinking",
        "prompt": "You need to find trends in sales data over years. Which Excel tools would you use?",
        "expected": "Pivot Table, Charts, Trendlines, Power Pivot",
        "grading_hints": ["Pivot Table", "Charts", "Trendlines", "Power Pivot"]
    }
]


def get_questions_for_role(role: str):
    if role == "associate":
        qs = [q for q in SEED_QUESTIONS if q["role"] in ("associate", "above_associate")]
        return qs[:20]
    elif role == "above_associate":
        qs = [q for q in SEED_QUESTIONS if q["role"] in ("above_associate", "associate")]
        return qs[:35]
    else:
        return SEED_QUESTIONS[:50] if len(SEED_QUESTIONS) >= 50 else SEED_QUESTIONS