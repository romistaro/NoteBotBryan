import json

# Define a function to convert data to JSONL format
def convert_to_jsonl(input_data):
    messages = [
        {"role": "system", "content": "You are studentGPT. Your task is to convert new information to short notes using markdown. Only add information that isn't written down in the markdown already"},
        {"role": "user", "content": input_data[0]},
        {"role": "assistant", "content": input_data[1]}
    ]
    return {"messages": messages}

data = [
        [
"""
CURRENT MARKDOWN:
CURRENT INFORMATION:
NEW INFORMATION:
""",
"""
"""
        ],
        [
"""
CURRENT MARKDOWN:
CURRENT INFORMATION:
NEW INFORMATION: Hello everyone.
""",
"""
"""
        ],
        [
"""
CURRENT MARKDOWN:
CURRENT INFORMATION: Hello everyone.
NEW INFORMATION: Today we will be talking about cats.
""",
"""
# Cats
"""
        ],
        [
"""
CURRENT MARKDOWN:
# Cats
CURRENT INFORMATION: Hello everyone. Today we will be talking about cats.
NEW INFORMATION: Cats have seven cervical vertebrae, 13 thoracic vertebrae, seven lumbar vertebrae.
""",
"""
## Bones in Cats
- **7 cervical** vertebrae.
- **13 thoracic** vertebrae.
- **7 lumbar** vertebrae.
"""
        ],
        [
"""
CURRENT MARKDOWN:
# Cats
## Bones in Cats
- **7 cervical** vertebrae.
- **13 thoracic** vertebrae
- **lumbar** vertebrae.
CURRENT INFORMATION: Hello everyone. Today we will be talking about cats. Cats have seven cervical vertebrae, 13 thoracic vertebrae, seven lumbar vertebrae,
NEW INFORMATION: three sacral vertebrae, and a variable number of caudal vertebrae in the tail
""",
"""
- **3 sacral** vertebrae.
- a variable number of **caudal** vertebrae.
"""
        ],
        [
"""
CURRENT MARKDOWN:
CURRENT INFORMATION:
NEW INFORMATION: The pythagorean theorem is a theorem dating
""",
"""
# The Pythagorean Theorem
"""
        ],
        [
"""
CURRENT MARKDOWN:
# The Pythagorean Theorem
CURRENT INFORMATION: The pythagorean theorem is a theorem dating
NEW INFORMATION: back to the babylonian era. It is a concept which is a
""",
"""
- Dates back to the **babylonian era**.
"""
        ],
        [
"""
CURRENT MARKDOWN:
# The Pythagorean Theorem
- Dates back to the **babylonian era**.
CURRENT INFORMATION: The pythagorean theorem is a theorem dating back to the babylonian era. It is a concept which is a
NEW INFORMATION: fundamental concept in mathematics.
""",
"""
- Fundamental concept.
"""
        ],
        [
"""
CURRENT MARKDOWN:
# The Pythagorean Theorem
- Dates back to the **babylonian era**.
- Fundamental concept.
CURRENT INFORMATION: The pythagorean theorem is a theorem dating back to the babylonian era. It is a concept which is a funadmental concept in mathematics.
NEW INFORMATION: It states, a squared plus
""",
"""
"""
        ],
        [
"""
CURRENT MARKDOWN:
# The Pythagorean Theorem
- Dates back to the babylonian era.
- Fundamental concept.
CURRENT INFORMATION: The pythagorean theorem is a theorem dating back to the babylonian era. It is a concept which is a funadmental concept in mathematics. It states, a squared plus
NEW INFORMATION: b squared equals c squared.
""",
"""
## Formula
*a^2 + b^2 = c^2*
"""
        ],
        [
"""
CURRENT MARKDOWN:
# Health Benefits of Exercise
CURRENT INFORMATION: Exercise has many health benefits. It can
NEW INFORMATION: improve your mood, reduce your risk of heart disease, and
""",
"""
# Health Benefits of Exercise
- Improves your mood
- Reduces risk of **heart disease**
"""
        ],
        [
"""
CURRENT MARKDOWN:
# Common Geometry Formulas
CURRENT INFORMATION: The area of a circle is pi times the radius squared. The
NEW INFORMATION: area of a triangle is one half the base times the height.
""",
"""
# Common Geometry Formulas
- Area of a triangle is *1/2 x base x height*
"""
        ],
        [
"""
CURRENT MARKDOWN:
# WSL Use Cases
CURRENT INFORMATION: WSL (Windows Subsystem for Linux) is a tool that allows
NEW INFORMATION: you to run Linux on Windows. It is useful for developers who
""",
"""
# WSL Use Cases
- Useful for developers
"""
        ],
        [
"""
CURRENT MARKDOWN:
# Intro to Derivatives
CURRENT INFORMATION: Derivatives are a concept in calculus that
NEW INFORMATION: are used to find the slope of a function at a point.
""",
"""
# Intro to Derivatives
- Used to find the **slope** of a function at a point
"""
        ],
]

# Write data to the JSONL file
with open('output.jsonl', 'w') as jsonl_file:
    for item in data:
        jsonl_entry = json.dumps(convert_to_jsonl(item))
        jsonl_file.write(jsonl_entry + '\n')

print('Done!')
