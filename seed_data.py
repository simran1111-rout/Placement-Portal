"""
Seed Data Script for Placement Preparation Portal
==================================================
Run this script after initializing the database:
    python seed_data.py
"""

from app import create_app, db
from app.models import User, Category, Question, Resource
from datetime import datetime

def create_admin_user():
    admin = User.query.filter_by(email='admin@college.edu').first()
    if admin:
        return admin

    admin = User(
        username='Admin User',
        email='admin@college.edu',
        role='admin',
        college='Placement Portal'
    )
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    print("Admin user created: admin@college.edu / admin123")
    return admin

def create_categories():
    categories_data = [
        {'name': 'Quantitative Aptitude', 'type': 'aptitude', 'description': 'Test numerical ability, math, and data interpretation.'},
        {'name': 'Logical Reasoning', 'type': 'aptitude', 'description': 'Evaluate logical thinking, puzzles, and patterns.'},
        {'name': 'Verbal Ability', 'type': 'aptitude', 'description': 'English language, reading comprehension, and grammar.'},
        {'name': 'Python Programming', 'type': 'technical', 'description': 'Python syntax, OOP concepts, and libraries.'},
        {'name': 'Java Programming & OOP', 'type': 'technical', 'description': 'Java core, multithreading, collections, and object-oriented principles.'},
        {'name': 'Data Structures', 'type': 'technical', 'description': 'Arrays, linked lists, trees, graphs, and sorting.'},
        {'name': 'SQL & Databases', 'type': 'technical', 'description': 'SQL queries, normalization, indexing, and DBMS concepts.'},
        {'name': 'Operating Systems', 'type': 'technical', 'description': 'Processes, threads, memory, and deadlocks.'},
        {'name': 'Computer Networks', 'type': 'technical', 'description': 'OSI model, TCP/IP, routing, and security basics.'},
        {'name': 'Modern Web Development', 'type': 'technical', 'description': 'HTML, CSS, JS, React, Node.js, and API design.'},
        {'name': 'Artificial Intelligence & Machine Learning', 'type': 'technical', 'description': 'ML algorithms, neural networks, NLP, and LLMs.'},
        {'name': 'System Design & Architecture', 'type': 'technical', 'description': 'Scalability, microservices, load balancing, and distributed systems.'},
        {'name': 'Cloud Computing & DevOps', 'type': 'technical', 'description': 'AWS concepts, Docker, Kubernetes, and CI/CD pipelines.'},
        {'name': 'Software Engineering & Agile', 'type': 'technical', 'description': 'SDLC, Agile/Scrum methodologies, Git, and software testing.'}
    ]

    created_categories = []
    for cat_data in categories_data:
        existing = Category.query.filter_by(name=cat_data['name']).first()
        if existing:
            created_categories.append(existing)
            continue

        category = Category(name=cat_data['name'], type=cat_data['type'], description=cat_data['description'])
        db.session.add(category)
        created_categories.append(category)

    db.session.commit()
    return created_categories

def create_questions(categories):
    questions_data = {
        # --- PREVIOUS TOPICS (15 Qs Each) ---
        'Quantitative Aptitude': [
            {'question_text': 'If a number increases by 20% then decreases by 20%, what is the net change?', 'option_a': '0%', 'option_b': '4% decrease', 'option_c': '4% increase', 'option_d': '2% decrease', 'correct_answer': 'B', 'explanation': '100 -> 120 -> 96. Net change = -4%.', 'difficulty': 'easy'},
            {'question_text': 'A train 200m long runs at 72 km/h. Time to cross a pole?', 'option_a': '8s', 'option_b': '10s', 'option_c': '12s', 'option_d': '15s', 'correct_answer': 'B', 'explanation': '72 km/h = 20 m/s. Time = 200/20 = 10s.', 'difficulty': 'easy'},
            {'question_text': 'Sum of first 50 natural numbers?', 'option_a': '1225', 'option_b': '1275', 'option_c': '1325', 'option_d': '1375', 'correct_answer': 'B', 'explanation': 'n(n+1)/2 = 50*51/2 = 1275.', 'difficulty': 'easy'},
            {'question_text': 'If A:B = 3:4 and B:C = 5:6, then A:B:C is:', 'option_a': '15:20:24', 'option_b': '3:5:6', 'option_c': '15:25:24', 'option_d': '12:16:20', 'correct_answer': 'A', 'explanation': 'A:B=15:20, B:C=20:24. A:B:C = 15:20:24.', 'difficulty': 'medium'},
            {'question_text': 'A works in 12 days, B in 18 days. Together they complete in:', 'option_a': '6.2 days', 'option_b': '7.2 days', 'option_c': '8.2 days', 'option_d': '9.2 days', 'correct_answer': 'B', 'explanation': '1/12 + 1/18 = 5/36. Reverse = 7.2 days.', 'difficulty': 'medium'},
            {'question_text': 'What is the probability of getting a sum of 9 from two throws of a dice?', 'option_a': '1/6', 'option_b': '1/8', 'option_c': '1/9', 'option_d': '1/12', 'correct_answer': 'C', 'explanation': 'Favorable outcomes: (3,6), (4,5), (5,4), (6,3). 4/36 = 1/9.', 'difficulty': 'medium'},
            {'question_text': 'The cost price of 20 articles is the same as the selling price of x articles. If profit is 25%, find x.', 'option_a': '15', 'option_b': '16', 'option_c': '18', 'option_d': '25', 'correct_answer': 'B', 'explanation': 'Profit = 25%. So SP = 1.25 CP. 20 CP = x SP = x(1.25 CP) => x = 16.', 'difficulty': 'hard'},
            {'question_text': 'A pipe fills a tank in 10 hours, another empties it in 15 hours. Time to fill if both are open?', 'option_a': '20 hours', 'option_b': '25 hours', 'option_c': '30 hours', 'option_d': '35 hours', 'correct_answer': 'C', 'explanation': '1/10 - 1/15 = 1/30. So 30 hours.', 'difficulty': 'medium'},
            {'question_text': 'What is the simple interest on $500 at 5% per annum for 2 years?', 'option_a': '$25', 'option_b': '$50', 'option_c': '$75', 'option_d': '$100', 'correct_answer': 'B', 'explanation': 'SI = (P*R*T)/100 = (500*5*2)/100 = 50.', 'difficulty': 'easy'},
            {'question_text': 'A boat goes 8 km/hr in still water and the stream is 2 km/hr. Time taken to go 30 km downstream?', 'option_a': '2 hours', 'option_b': '2.5 hours', 'option_c': '3 hours', 'option_d': '4 hours', 'correct_answer': 'C', 'explanation': 'Downstream speed = 8 + 2 = 10 km/hr. Time = 30 / 10 = 3 hours.', 'difficulty': 'medium'},
            {'question_text': 'In how many ways can the letters of "APPLE" be arranged?', 'option_a': '60', 'option_b': '120', 'option_c': '24', 'option_d': '48', 'correct_answer': 'A', 'explanation': '5! / 2! (for two Ps) = 120 / 2 = 60.', 'difficulty': 'medium'},
            {'question_text': 'LCM of 12, 15, and 20 is:', 'option_a': '30', 'option_b': '45', 'option_c': '60', 'option_d': '120', 'correct_answer': 'C', 'explanation': '60 is the smallest number divisible by 12, 15, and 20.', 'difficulty': 'easy'},
            {'question_text': 'Average of 5 consecutive odd numbers is 61. What is the difference between highest and lowest?', 'option_a': '4', 'option_b': '8', 'option_c': '12', 'option_d': '16', 'correct_answer': 'B', 'explanation': 'Numbers are x, x+2, x+4, x+6, x+8. Difference is (x+8) - x = 8.', 'difficulty': 'medium'},
            {'question_text': 'Find the compound interest on $1000 at 10% for 2 years.', 'option_a': '$200', 'option_b': '$210', 'option_c': '$220', 'option_d': '$230', 'correct_answer': 'B', 'explanation': 'Amount = 1000 * (1.1)^2 = 1210. CI = 1210 - 1000 = 210.', 'difficulty': 'medium'},
            {'question_text': 'A person crosses a 600m long street in 5 mins. What is his speed in km/hr?', 'option_a': '3.6', 'option_b': '7.2', 'option_c': '8.4', 'option_d': '10', 'correct_answer': 'B', 'explanation': 'Speed = 600/300 m/s = 2 m/s. In km/hr: 2 * (18/5) = 7.2.', 'difficulty': 'medium'}
        ],
        'Logical Reasoning': [
            {'question_text': 'If COMPUTER is coded as RFUVQNPC, how is MEDICINE coded?', 'option_a': 'MFEJDJOF', 'option_b': 'ENICIDME', 'option_c': 'FOJDJEFM', 'option_d': 'MEDICINF', 'correct_answer': 'C', 'explanation': 'Reversed and shifted by +1.', 'difficulty': 'hard'},
            {'question_text': 'Find next in series: 2, 6, 12, 20, 30, ?', 'option_a': '38', 'option_b': '40', 'option_c': '42', 'option_d': '44', 'correct_answer': 'C', 'explanation': '1*2, 2*3, 3*4, 4*5, 5*6, 6*7 = 42.', 'difficulty': 'easy'},
            {'question_text': 'All roses are flowers. Some flowers are red. Therefore:', 'option_a': 'All roses are red', 'option_b': 'Some roses are red', 'option_c': 'No rose is red', 'option_d': 'None of the above', 'correct_answer': 'D', 'explanation': 'Cannot determine relationship between roses and red.', 'difficulty': 'medium'},
            {'question_text': 'A is brother of B, B is sister of C, C is father of D. How is A related to D?', 'option_a': 'Uncle', 'option_b': 'Nephew', 'option_c': 'Cousin', 'option_d': 'Grandfather', 'correct_answer': 'A', 'explanation': 'A is brother of D\'s father C. Hence, Uncle.', 'difficulty': 'medium'},
            {'question_text': 'Ram is 7th from left, Shyam is 12th from right. Interchange makes Ram 22nd from left. Total students?', 'option_a': '31', 'option_b': '32', 'option_c': '33', 'option_d': '34', 'correct_answer': 'C', 'explanation': 'Total = 22 + 12 - 1 = 33.', 'difficulty': 'hard'},
            {'question_text': 'Look at the series: 7, 10, 8, 11, 9, 12... What number should come next?', 'option_a': '7', 'option_b': '10', 'option_c': '12', 'option_d': '13', 'correct_answer': 'B', 'explanation': 'Alternating pattern: +3, -2. So 12 - 2 = 10.', 'difficulty': 'easy'},
            {'question_text': 'Pointing to a photograph, a man said, "I have no brother, and that man\'s father is my father\'s son." Whose photo is it?', 'option_a': 'His son', 'option_b': 'His own', 'option_c': 'His father', 'option_d': 'His nephew', 'correct_answer': 'A', 'explanation': '"My father\'s son" is the speaker himself. So, the man\'s father is the speaker.', 'difficulty': 'hard'},
            {'question_text': 'Which word does NOT belong with the others?', 'option_a': 'Leopard', 'option_b': 'Cougar', 'option_c': 'Elephant', 'option_d': 'Lion', 'correct_answer': 'C', 'explanation': 'All others are big cats (felines).', 'difficulty': 'easy'},
            {'question_text': 'SCD, TEF, UGH, ____, WKL', 'option_a': 'CMN', 'option_b': 'UJI', 'option_c': 'VIJ', 'option_d': 'IJT', 'correct_answer': 'C', 'explanation': 'First letter: S,T,U,V,W. Second/Third letters: CD, EF, GH, IJ, KL.', 'difficulty': 'medium'},
            {'question_text': 'Find the odd one out: 3, 5, 11, 14, 17, 21', 'option_a': '21', 'option_b': '17', 'option_c': '14', 'option_d': '3', 'correct_answer': 'C', 'explanation': 'All others are odd numbers / prime numbers. 14 is even.', 'difficulty': 'easy'},
            {'question_text': 'If South-East becomes North, North-East becomes West and so on. What will West become?', 'option_a': 'North-East', 'option_b': 'North-West', 'option_c': 'South-East', 'option_d': 'South-West', 'correct_answer': 'C', 'explanation': 'Directions rotate by 135 degrees clockwise. West becomes South-East.', 'difficulty': 'hard'},
            {'question_text': 'At 3:40, the hour hand and the minute hand of a clock form an angle of:', 'option_a': '120 degrees', 'option_b': '125 degrees', 'option_c': '130 degrees', 'option_d': '135 degrees', 'correct_answer': 'C', 'explanation': 'Angle = |30*H - 5.5*M| = |30*3 - 5.5*40| = |90 - 220| = 130.', 'difficulty': 'medium'},
            {'question_text': 'January 1, 2008 is Tuesday. What day of the week lies on Jan 1, 2009?', 'option_a': 'Monday', 'option_b': 'Wednesday', 'option_c': 'Thursday', 'option_d': 'Sunday', 'correct_answer': 'C', 'explanation': '2008 is a leap year, so it has 2 odd days. Tuesday + 2 = Thursday.', 'difficulty': 'medium'},
            {'question_text': 'In a row of boys, If A is 10th from the left and B is 9th from the right, interchange makes A 15th from left. How many boys?', 'option_a': '23', 'option_b': '27', 'option_c': '28', 'option_d': '31', 'correct_answer': 'A', 'explanation': 'Total = 15 (A\'s new left) + 9 (B\'s right) - 1 = 23.', 'difficulty': 'hard'},
            {'question_text': 'A plane is flying West. It turns right, then turns right again. What direction is it facing?', 'option_a': 'North', 'option_b': 'South', 'option_c': 'East', 'option_d': 'West', 'correct_answer': 'C', 'explanation': 'West -> right turn -> North -> right turn -> East.', 'difficulty': 'easy'}
        ],
        'Verbal Ability': [
            {'question_text': 'Synonym of "EPHEMERAL":', 'option_a': 'Eternal', 'option_b': 'Transient', 'option_c': 'Permanent', 'option_d': 'Everlasting', 'correct_answer': 'B', 'explanation': 'Ephemeral means lasting for a very short time.', 'difficulty': 'medium'},
            {'question_text': 'Meaning of "Bite the bullet":', 'option_a': 'Eat quickly', 'option_b': 'Face a difficult situation bravely', 'option_c': 'Be aggressive', 'option_d': 'Make a mistake', 'correct_answer': 'B', 'explanation': 'Enduring a painful situation with courage.', 'difficulty': 'easy'},
            {'question_text': 'Select correct sentence:', 'option_a': 'Neither students nor teacher were present', 'option_b': 'Neither students nor teacher was present', 'option_c': 'Neither student nor teachers was present', 'option_d': 'None of above', 'correct_answer': 'B', 'explanation': 'Verb agrees with the closest noun ("teacher" is singular).', 'difficulty': 'medium'},
            {'question_text': 'Antonym of "BENEVOLENT":', 'option_a': 'Kind', 'option_b': 'Generous', 'option_c': 'Malevolent', 'option_d': 'Caring', 'correct_answer': 'C', 'explanation': 'Benevolent means kind; Malevolent means evil-intentioned.', 'difficulty': 'easy'},
            {'question_text': 'Meaning of "UBIQUITOUS":', 'option_a': 'Rare', 'option_b': 'Present everywhere', 'option_c': 'Unique', 'option_d': 'Ancient', 'correct_answer': 'B', 'explanation': 'Found everywhere, omnipresent.', 'difficulty': 'medium'},
            {'question_text': 'One word substitute for "A person who renounces religious or political belief":', 'option_a': 'Agnostic', 'option_b': 'Apostate', 'option_c': 'Apostle', 'option_d': 'Atheist', 'correct_answer': 'B', 'explanation': 'An apostate abandons a religious or political belief.', 'difficulty': 'hard'},
            {'question_text': 'Find the correctly spelt word:', 'option_a': 'Accomodation', 'option_b': 'Acommodation', 'option_c': 'Accommodation', 'option_d': 'Acomodation', 'correct_answer': 'C', 'explanation': 'Accommodation requires double "c" and double "m".', 'difficulty': 'medium'},
            {'question_text': 'Change to passive voice: "She makes cakes."', 'option_a': 'Cakes are made by her.', 'option_b': 'Cakes were made by her.', 'option_c': 'Cakes are being made by her.', 'option_d': 'She is making cakes.', 'correct_answer': 'A', 'explanation': 'Simple present changes to "are made".', 'difficulty': 'easy'},
            {'question_text': 'What does the idiom "Spill the beans" mean?', 'option_a': 'Drop your food', 'option_b': 'Reveal a secret', 'option_c': 'Cook a meal', 'option_d': 'Get angry', 'correct_answer': 'B', 'explanation': 'It means to disclose secret information.', 'difficulty': 'easy'},
            {'question_text': 'Antonym of "MITIGATE":', 'option_a': 'Alleviate', 'option_b': 'Aggravate', 'option_c': 'Soothe', 'option_d': 'Lessen', 'correct_answer': 'B', 'explanation': 'Mitigate means to lessen; Aggravate means to make worse.', 'difficulty': 'medium'},
            {'question_text': 'Fill in the blank: She was standing ____ the window.', 'option_a': 'in', 'option_b': 'on', 'option_c': 'by', 'option_d': 'with', 'correct_answer': 'C', 'explanation': '"By" denotes proximity (next to).', 'difficulty': 'easy'},
            {'question_text': 'Find the error: "He is one of the best player in the team."', 'option_a': 'He is', 'option_b': 'one of the', 'option_c': 'best player', 'option_d': 'in the team', 'correct_answer': 'C', 'explanation': '"One of the" is always followed by a plural noun ("players").', 'difficulty': 'medium'},
            {'question_text': 'Synonym of "CANDID":', 'option_a': 'Secretive', 'option_b': 'Frank', 'option_c': 'Deceptive', 'option_d': 'Angry', 'correct_answer': 'B', 'explanation': 'Candid means truthful and straightforward.', 'difficulty': 'easy'},
            {'question_text': 'Meaning of "To smell a rat":', 'option_a': 'To smell foul odor', 'option_b': 'To suspect a trick or deceit', 'option_c': 'To catch a disease', 'option_d': 'To fail an exam', 'correct_answer': 'B', 'explanation': 'It implies suspecting that something is wrong.', 'difficulty': 'medium'},
            {'question_text': 'One word substitute for "A collection of poems":', 'option_a': 'Anthology', 'option_b': 'Pathology', 'option_c': 'Pedagogy', 'option_d': 'Bibliography', 'correct_answer': 'A', 'explanation': 'Anthology is a published collection of poems or writing.', 'difficulty': 'easy'}
        ],
        'Python Programming': [
            {'question_text': 'Output of `print(type([]))`?', 'option_a': '<class "tuple">', 'option_b': '<class "list">', 'option_c': '<class "dict">', 'option_d': '<class "set">', 'correct_answer': 'B', 'explanation': 'Creates an empty list.', 'difficulty': 'easy'},
            {'question_text': 'Which of the following is mutable?', 'option_a': 'Tuple', 'option_b': 'String', 'option_c': 'List', 'option_d': 'Integer', 'correct_answer': 'C', 'explanation': 'Lists can be modified after creation.', 'difficulty': 'easy'},
            {'question_text': 'What does `//` do?', 'option_a': 'Exponentiation', 'option_b': 'Floor Division', 'option_c': 'Modulo', 'option_d': 'Root', 'correct_answer': 'B', 'explanation': 'Divides and rounds down to nearest integer.', 'difficulty': 'easy'},
            {'question_text': 'Output of `print("Hello"[::-1])`?', 'option_a': 'Hello', 'option_b': 'olleH', 'option_c': 'H', 'option_d': 'Error', 'correct_answer': 'B', 'explanation': 'Slices backward, reversing the string.', 'difficulty': 'medium'},
            {'question_text': 'How to demonstrate Inheritance?', 'option_a': 'class Child(Parent):', 'option_b': 'class Child extends Parent:', 'option_c': 'class Child inherits Parent:', 'option_d': 'Child = Parent()', 'correct_answer': 'A', 'explanation': 'Python passes parent class as parameter.', 'difficulty': 'easy'},
            {'question_text': 'What is Encapsulation?', 'option_a': 'Binding data and methods', 'option_b': 'Deriving new classes', 'option_c': 'Multiple inheritance', 'option_d': 'File zipping', 'correct_answer': 'A', 'explanation': 'Restricts direct access to variables.', 'difficulty': 'medium'},
            {'question_text': 'How to define a private attribute?', 'option_a': 'private var', 'option_b': '_var', 'option_c': '__var', 'option_d': 'var.private', 'correct_answer': 'C', 'explanation': 'Double underscore invokes name mangling.', 'difficulty': 'medium'},
            {'question_text': 'What does `super()` do?', 'option_a': 'Increases speed', 'option_b': 'Calls parent methods', 'option_c': 'Elevates privileges', 'option_d': 'Overrides methods', 'correct_answer': 'B', 'explanation': 'Returns a proxy object of superclass.', 'difficulty': 'medium'},
            {'question_text': 'Keyword for generator function?', 'option_a': 'return', 'option_b': 'yield', 'option_c': 'generate', 'option_d': 'async', 'correct_answer': 'B', 'explanation': 'yield suspends execution, returning a value.', 'difficulty': 'medium'},
            {'question_text': 'What is a decorator?', 'option_a': 'UI element', 'option_b': 'Function modifying another function', 'option_c': 'Class variable', 'option_d': 'Error handler', 'correct_answer': 'B', 'explanation': 'Wraps a function to change its behavior.', 'difficulty': 'hard'},
            {'question_text': 'What does `*args` do?', 'option_a': 'Keyword arguments', 'option_b': 'Variable positional arguments', 'option_c': 'Multiplication', 'option_d': 'Unpacks dict', 'correct_answer': 'B', 'explanation': 'Allows passing multiple non-keyword arguments.', 'difficulty': 'medium'},
            {'question_text': 'What is the Global Interpreter Lock (GIL)?', 'option_a': 'Security feature', 'option_b': 'Mutex preventing multiple native threads executing Python bytecode', 'option_c': 'Database lock', 'option_d': 'Debugger', 'correct_answer': 'B', 'explanation': 'Limits CPython to one thread at a time for execution.', 'difficulty': 'hard'},
            {'question_text': 'Difference between shallow and deep copy?', 'option_a': 'None', 'option_b': 'Deep recursively copies nested objects', 'option_c': 'Shallow is faster', 'option_d': 'Deep copies primitives', 'correct_answer': 'B', 'explanation': 'Deepcopy creates an entirely new independent collection.', 'difficulty': 'hard'},
            {'question_text': 'What does `pass` do?', 'option_a': 'Exits loop', 'option_b': 'Skips iteration', 'option_c': 'Null operation (placeholder)', 'option_d': 'Throws error', 'correct_answer': 'C', 'explanation': 'Does nothing, used for empty code blocks.', 'difficulty': 'easy'},
            {'question_text': 'What is a Lambda function?', 'option_a': 'Multi-line func', 'option_b': 'Anonymous single-expression func', 'option_c': 'Built-in library', 'option_d': 'Serverless code', 'correct_answer': 'B', 'explanation': 'Defined without a name using lambda keyword.', 'difficulty': 'medium'}
        ],
        'Data Structures': [
            {'question_text': 'Time complexity to access array element by index?', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n^2)', 'correct_answer': 'A', 'explanation': 'Direct memory access allows O(1) retrieval.', 'difficulty': 'easy'},
            {'question_text': 'Advantage of Linked List over Array?', 'option_a': 'Faster access', 'option_b': 'Dynamic size and easy insertion/deletion', 'option_c': 'Less memory', 'option_d': 'Built-in sorting', 'correct_answer': 'B', 'explanation': 'Linked lists don\'t require contiguous memory.', 'difficulty': 'medium'},
            {'question_text': 'Which structure follows LIFO?', 'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Tree', 'option_d': 'Graph', 'correct_answer': 'B', 'explanation': 'Stack is Last In First Out.', 'difficulty': 'easy'},
            {'question_text': 'Which structure follows FIFO?', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Heap', 'option_d': 'Trie', 'correct_answer': 'B', 'explanation': 'Queue is First In First Out.', 'difficulty': 'easy'},
            {'question_text': 'Time complexity of searching in balanced BST?', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n log n)', 'correct_answer': 'C', 'explanation': 'Each comparison halves the search space.', 'difficulty': 'medium'},
            {'question_text': 'What is an AVL Tree?', 'option_a': 'Self-balancing binary search tree', 'option_b': 'Graph algorithm', 'option_c': 'Hash map', 'option_d': 'Heap', 'correct_answer': 'A', 'explanation': 'Heights of child subtrees differ by at most one.', 'difficulty': 'hard'},
            {'question_text': 'Inorder traversal of BST yields?', 'option_a': 'Reverse order', 'option_b': 'Sorted ascending order', 'option_c': 'Random order', 'option_d': 'Unsorted data', 'correct_answer': 'B', 'explanation': 'Inorder processes Left, Root, Right.', 'difficulty': 'medium'},
            {'question_text': 'Time complexity to find max in a Max-Heap?', 'option_a': 'O(n)', 'option_b': 'O(log n)', 'option_c': 'O(1)', 'option_d': 'O(n log n)', 'correct_answer': 'C', 'explanation': 'Max element is always at the root node.', 'difficulty': 'medium'},
            {'question_text': 'Algorithm for finding shortest path in unweighted graph?', 'option_a': 'DFS', 'option_b': 'BFS', 'option_c': 'Dijkstra', 'option_d': 'Kruskal', 'correct_answer': 'B', 'explanation': 'BFS finds the shortest path by exploring layer by layer.', 'difficulty': 'hard'},
            {'question_text': 'What is a Hash collision?', 'option_a': 'Program crash', 'option_b': 'Two keys map to the same index', 'option_c': 'Table full', 'option_d': 'Memory overflow', 'correct_answer': 'B', 'explanation': 'Resolved via chaining or open addressing.', 'difficulty': 'medium'},
            {'question_text': 'Worst-case time complexity of QuickSort?', 'option_a': 'O(n log n)', 'option_b': 'O(n)', 'option_c': 'O(n^2)', 'option_d': 'O(log n)', 'correct_answer': 'C', 'explanation': 'Occurs when pivot is constantly the extreme element.', 'difficulty': 'hard'},
            {'question_text': 'Best sorting algorithm for nearly sorted data?', 'option_a': 'QuickSort', 'option_b': 'MergeSort', 'option_c': 'InsertionSort', 'option_d': 'SelectionSort', 'correct_answer': 'C', 'explanation': 'InsertionSort runs in O(n) time on nearly sorted arrays.', 'difficulty': 'medium'},
            {'question_text': 'What is Dynamic Programming?', 'option_a': 'Writing code fast', 'option_b': 'Solving complex problems by breaking into overlapping subproblems', 'option_c': 'Database concept', 'option_d': 'Networking protocol', 'correct_answer': 'B', 'explanation': 'DP stores results of subproblems to avoid redundant work.', 'difficulty': 'hard'},
            {'question_text': 'What is a Trie?', 'option_a': 'Balanced tree', 'option_b': 'Tree used specifically for storing strings/prefixes', 'option_c': 'Graph type', 'option_d': 'Hash function', 'correct_answer': 'B', 'explanation': 'Optimal for autocomplete and prefix searches.', 'difficulty': 'hard'},
            {'question_text': 'What is a greedy algorithm?', 'option_a': 'Max memory usage', 'option_b': 'Makes the locally optimal choice at each stage', 'option_c': 'Checks all combinations', 'option_d': 'Random choices', 'correct_answer': 'B', 'explanation': 'Seeks local optimums to approximate global optimums.', 'difficulty': 'medium'}
        ],
        'SQL & Databases': [
            {'question_text': 'Command to remove all records but keep table structure?', 'option_a': 'DELETE', 'option_b': 'DROP', 'option_c': 'TRUNCATE', 'option_d': 'REMOVE', 'correct_answer': 'C', 'explanation': 'TRUNCATE removes rows faster without logging individual deletions.', 'difficulty': 'easy'},
            {'question_text': 'JOIN returning all rows when there is a match in either table?', 'option_a': 'INNER JOIN', 'option_b': 'LEFT JOIN', 'option_c': 'RIGHT JOIN', 'option_d': 'FULL OUTER JOIN', 'correct_answer': 'D', 'explanation': 'FULL OUTER combines both Left and Right joins.', 'difficulty': 'medium'},
            {'question_text': 'What normal form eliminates partial dependencies?', 'option_a': '1NF', 'option_b': '2NF', 'option_c': '3NF', 'option_d': 'BCNF', 'correct_answer': 'B', 'explanation': '2NF ensures non-key attributes depend on the entire primary key.', 'difficulty': 'medium'},
            {'question_text': 'What does ACID stand for?', 'option_a': 'Atomicity, Consistency, Isolation, Durability', 'option_b': 'Array, Column, Index, Data', 'option_c': 'Auto, Commit, Insert, Delete', 'option_d': 'All Columns In Database', 'correct_answer': 'A', 'explanation': 'ACID properties guarantee reliable transaction processing.', 'difficulty': 'easy'},
            {'question_text': 'Best index type for range queries?', 'option_a': 'Hash', 'option_b': 'B-Tree', 'option_c': 'Bitmap', 'option_d': 'Full-text', 'correct_answer': 'B', 'explanation': 'B-Trees maintain sorted order, ideal for >, <, BETWEEN queries.', 'difficulty': 'hard'},
            {'question_text': 'Which clause filters records after grouping?', 'option_a': 'WHERE', 'option_b': 'ORDER BY', 'option_c': 'HAVING', 'option_d': 'FILTER', 'correct_answer': 'C', 'explanation': 'HAVING is used to filter results of GROUP BY aggregations.', 'difficulty': 'medium'},
            {'question_text': 'Difference between primary key and unique key?', 'option_a': 'None', 'option_b': 'Primary key cannot have NULLs, Unique can have one NULL', 'option_c': 'Unique is faster', 'option_d': 'Primary allows duplicates', 'correct_answer': 'B', 'explanation': 'Primary key inherently enforces NOT NULL constraint.', 'difficulty': 'easy'},
            {'question_text': 'What is a Foreign Key?', 'option_a': 'Key from another database', 'option_b': 'Field linking to a primary key in another table', 'option_c': 'Encrypted key', 'option_d': 'Temporary key', 'correct_answer': 'B', 'explanation': 'Establishes a relationship between two tables.', 'difficulty': 'easy'},
            {'question_text': 'What does DML stand for?', 'option_a': 'Data Manipulation Language', 'option_b': 'Data Management Line', 'option_c': 'Database Model Layout', 'option_d': 'Delete Modify Link', 'correct_answer': 'A', 'explanation': 'DML includes INSERT, UPDATE, DELETE.', 'difficulty': 'easy'},
            {'question_text': 'Command to undo a transaction?', 'option_a': 'UNDO', 'option_b': 'REVERT', 'option_c': 'ROLLBACK', 'option_d': 'COMMIT', 'correct_answer': 'C', 'explanation': 'ROLLBACK restores the database to the last committed state.', 'difficulty': 'medium'},
            {'question_text': 'What is a Cartesian product in SQL?', 'option_a': 'INNER JOIN', 'option_b': 'CROSS JOIN', 'option_c': 'LEFT JOIN', 'option_d': 'MATH JOIN', 'correct_answer': 'B', 'explanation': 'CROSS JOIN returns all possible combinations of rows from two tables.', 'difficulty': 'hard'},
            {'question_text': 'What is a View?', 'option_a': 'A physical table', 'option_b': 'A virtual table based on a SQL statement', 'option_c': 'A GUI tool', 'option_d': 'An index', 'correct_answer': 'B', 'explanation': 'Views encapsulate complex queries into a reusable virtual table.', 'difficulty': 'medium'},
            {'question_text': 'Which function counts the number of rows?', 'option_a': 'SUM()', 'option_b': 'TOTAL()', 'option_c': 'COUNT()', 'option_d': 'ROWS()', 'correct_answer': 'C', 'explanation': 'COUNT() returns the number of rows matching the query.', 'difficulty': 'easy'},
            {'question_text': 'What is a clustered index?', 'option_a': 'A secondary index', 'option_b': 'An index that defines the physical sorting of the table data', 'option_c': 'A hash map', 'option_d': 'A view', 'correct_answer': 'B', 'explanation': 'A table can only have one clustered index because data can only sort one way physically.', 'difficulty': 'hard'},
            {'question_text': 'What does the LIKE operator do?', 'option_a': 'Calculates similarity', 'option_b': 'Pattern matching with wildcards', 'option_c': 'Joins tables', 'option_d': 'Checks exact equality', 'correct_answer': 'B', 'explanation': 'LIKE uses % and _ for wildcard string matching.', 'difficulty': 'easy'}
        ],
        'Operating Systems': [
            {'question_text': 'What is a deadlock?', 'option_a': 'Process waiting for I/O', 'option_b': 'Processes waiting indefinitely for resources held by each other', 'option_c': 'System crash', 'option_d': 'Memory overflow', 'correct_answer': 'B', 'explanation': 'Deadlock is a cycle of unresolvable dependencies.', 'difficulty': 'easy'},
            {'question_text': 'Which scheduling algorithm is preemptive?', 'option_a': 'FCFS', 'option_b': 'SJF', 'option_c': 'Round Robin', 'option_d': 'Non-preemptive Priority', 'correct_answer': 'C', 'explanation': 'Round Robin allocates a fixed time quantum to each process.', 'difficulty': 'medium'},
            {'question_text': 'What is thrashing?', 'option_a': 'High CPU utilization', 'option_b': 'Excessive paging causing slowdown', 'option_c': 'Disk fragmentation', 'option_d': 'Network lag', 'correct_answer': 'B', 'explanation': 'Thrashing happens when the OS spends more time paging than executing.', 'difficulty': 'medium'},
            {'question_text': 'Purpose of virtual memory?', 'option_a': 'Increase RAM speed', 'option_b': 'Execute processes larger than physical memory', 'option_c': 'Speed up disk', 'option_d': 'Backup data', 'correct_answer': 'B', 'explanation': 'Uses disk space to simulate additional RAM.', 'difficulty': 'easy'},
            {'question_text': 'Which is NOT a process state?', 'option_a': 'Ready', 'option_b': 'Running', 'option_c': 'Sleeping', 'option_d': 'Blocked', 'correct_answer': 'C', 'explanation': 'Standard states are New, Ready, Running, Blocked, Terminated.', 'difficulty': 'medium'},
            {'question_text': 'What is a thread?', 'option_a': 'A heavyweight process', 'option_b': 'A lightweight basic unit of CPU utilization', 'option_c': 'A network wire', 'option_d': 'A memory block', 'correct_answer': 'B', 'explanation': 'Threads share memory space within the same process.', 'difficulty': 'easy'},
            {'question_text': 'What does a Semaphore do?', 'option_a': 'Sorts files', 'option_b': 'Controls access to a shared resource', 'option_c': 'Increases CPU speed', 'option_d': 'Sends network packets', 'correct_answer': 'B', 'explanation': 'A synchronization tool used to manage concurrent processes.', 'difficulty': 'hard'},
            {'question_text': 'What is Context Switching?', 'option_a': 'Changing UI themes', 'option_b': 'Saving state of old process and loading state of new process', 'option_c': 'Rebooting OS', 'option_d': 'Swapping hard drives', 'correct_answer': 'B', 'explanation': 'Allows multiple processes to share a single CPU.', 'difficulty': 'medium'},
            {'question_text': 'What is a Mutex?', 'option_a': 'Mutual Exclusion object locking a resource', 'option_b': 'Memory Exception', 'option_c': 'Multi-execution thread', 'option_d': 'Multimedia Extension', 'correct_answer': 'A', 'explanation': 'Mutex ensures only one thread accesses a critical section at a time.', 'difficulty': 'hard'},
            {'question_text': 'What is paging?', 'option_a': 'Reading books', 'option_b': 'Memory management scheme eliminating external fragmentation', 'option_c': 'Disk formatting', 'option_d': 'Network routing', 'correct_answer': 'B', 'explanation': 'Divides memory into equal-sized pages and frames.', 'difficulty': 'medium'},
            {'question_text': 'What is starvation in OS?', 'option_a': 'Lack of power', 'option_b': 'A low priority process waiting indefinitely for CPU', 'option_c': 'Disk space full', 'option_d': 'Deadlock', 'correct_answer': 'B', 'explanation': 'Higher priority processes continuously take the CPU.', 'difficulty': 'medium'},
            {'question_text': 'Banker\'s Algorithm is used for?', 'option_a': 'Deadlock avoidance', 'option_b': 'Deadlock detection', 'option_c': 'CPU scheduling', 'option_d': 'Page replacement', 'correct_answer': 'A', 'explanation': 'It simulates resource allocation to ensure a safe state.', 'difficulty': 'hard'},
            {'question_text': 'Which page replacement algorithm suffers from Belady\'s Anomaly?', 'option_a': 'LRU', 'option_b': 'FIFO', 'option_c': 'Optimal', 'option_d': 'MRU', 'correct_answer': 'B', 'explanation': 'In FIFO, increasing page frames can sometimes increase page faults.', 'difficulty': 'hard'},
            {'question_text': 'What is the kernel?', 'option_a': 'A shell', 'option_b': 'The core of the OS that manages resources', 'option_c': 'A compiler', 'option_d': 'A web browser', 'correct_answer': 'B', 'explanation': 'The kernel interacts directly with hardware.', 'difficulty': 'easy'},
            {'question_text': 'What is Spooling?', 'option_a': 'Swimming', 'option_b': 'Simultaneous Peripheral Operations On-Line', 'option_c': 'Memory leak', 'option_d': 'Virus scanning', 'correct_answer': 'B', 'explanation': 'Buffers data for slow peripheral devices like printers.', 'difficulty': 'medium'}
        ],
        'Computer Networks': [
            {'question_text': 'Which OSI layer handles routing?', 'option_a': 'Data Link', 'option_b': 'Network', 'option_c': 'Transport', 'option_d': 'Session', 'correct_answer': 'B', 'explanation': 'Layer 3 (Network) handles logical IP addressing and routing.', 'difficulty': 'easy'},
            {'question_text': 'Protocol for secure web browsing?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'HTTPS', 'option_d': 'SMTP', 'correct_answer': 'C', 'explanation': 'HTTPS uses TLS/SSL encryption.', 'difficulty': 'easy'},
            {'question_text': 'Default subnet mask for Class C?', 'option_a': '255.0.0.0', 'option_b': '255.255.0.0', 'option_c': '255.255.255.0', 'option_d': '255.255.255.255', 'correct_answer': 'C', 'explanation': 'Class C allows 254 hosts per network.', 'difficulty': 'medium'},
            {'question_text': 'Which protocol uses port 80?', 'option_a': 'HTTPS', 'option_b': 'FTP', 'option_c': 'HTTP', 'option_d': 'SSH', 'correct_answer': 'C', 'explanation': 'HTTP transmits unencrypted web traffic on port 80.', 'difficulty': 'easy'},
            {'question_text': 'Purpose of DNS?', 'option_a': 'File transfer', 'option_b': 'Email', 'option_c': 'Translates Domain names to IPs', 'option_d': 'Security', 'correct_answer': 'C', 'explanation': 'DNS acts as the phonebook of the internet.', 'difficulty': 'easy'},
            {'question_text': 'Difference between TCP and UDP?', 'option_a': 'None', 'option_b': 'TCP is reliable/connection-oriented, UDP is fast/connectionless', 'option_c': 'UDP is reliable', 'option_d': 'TCP is for video only', 'correct_answer': 'B', 'explanation': 'TCP guarantees delivery; UDP streams without checking.', 'difficulty': 'medium'},
            {'question_text': 'What is a MAC address?', 'option_a': 'Apple computer ID', 'option_b': 'Physical hardware address of a network interface card', 'option_c': 'IP address', 'option_d': 'Web URL', 'correct_answer': 'B', 'explanation': 'A 48-bit address burned into network adapters.', 'difficulty': 'easy'},
            {'question_text': 'Which layer is the Transport layer in OSI?', 'option_a': 'Layer 2', 'option_b': 'Layer 3', 'option_c': 'Layer 4', 'option_d': 'Layer 5', 'correct_answer': 'C', 'explanation': 'It handles end-to-end communication (TCP/UDP).', 'difficulty': 'medium'},
            {'question_text': 'Protocol for sending email?', 'option_a': 'POP3', 'option_b': 'IMAP', 'option_c': 'SMTP', 'option_d': 'HTTP', 'correct_answer': 'C', 'explanation': 'Simple Mail Transfer Protocol is used for sending.', 'difficulty': 'medium'},
            {'question_text': 'What does DHCP do?', 'option_a': 'Encrypts data', 'option_b': 'Dynamically assigns IP addresses to devices', 'option_c': 'Blocks hackers', 'option_d': 'Translates domains', 'correct_answer': 'B', 'explanation': 'Dynamic Host Configuration Protocol automates IP assignment.', 'difficulty': 'easy'},
            {'question_text': 'What is a ping command used for?', 'option_a': 'Downloading files', 'option_b': 'Testing reachability and measuring round-trip time to a host', 'option_c': 'Compiling code', 'option_d': 'Opening a port', 'correct_answer': 'B', 'explanation': 'Uses ICMP echo request packets.', 'difficulty': 'easy'},
            {'question_text': 'IPv4 address length?', 'option_a': '16 bits', 'option_b': '32 bits', 'option_c': '64 bits', 'option_d': '128 bits', 'correct_answer': 'B', 'explanation': 'IPv4 uses 32 bits (e.g., 192.168.1.1).', 'difficulty': 'easy'},
            {'question_text': 'Which device connects different networks?', 'option_a': 'Switch', 'option_b': 'Hub', 'option_c': 'Router', 'option_d': 'Repeater', 'correct_answer': 'C', 'explanation': 'Routers operate at Layer 3 to connect distinct IP networks.', 'difficulty': 'medium'},
            {'question_text': 'What is OSPF?', 'option_a': 'Operating System Protocol', 'option_b': 'Open Shortest Path First (a routing protocol)', 'option_c': 'Optical Fiber', 'option_d': 'Security Firewall', 'correct_answer': 'B', 'explanation': 'A dynamic routing protocol for IP networks.', 'difficulty': 'hard'},
            {'question_text': 'Loopback IP address?', 'option_a': '192.168.0.1', 'option_b': '10.0.0.1', 'option_c': '127.0.0.1', 'option_d': '255.255.255.255', 'correct_answer': 'C', 'explanation': 'Used to test the local machine\'s network stack.', 'difficulty': 'easy'}
        ],
        'Modern Web Development': [
            {'question_text': 'What is the DOM?', 'option_a': 'Document Object Model', 'option_b': 'Data Object Model', 'option_c': 'Design Object Model', 'option_d': 'Document Oriented Model', 'correct_answer': 'A', 'explanation': 'Programming interface for web documents.', 'difficulty': 'easy'},
            {'question_text': 'Difference between `let` and `const`?', 'option_a': 'None', 'option_b': '`let` can be reassigned, `const` cannot', 'option_c': '`const` is for numbers only', 'option_d': '`let` is global', 'correct_answer': 'B', 'explanation': '`const` prevents reassignment of the variable identifier.', 'difficulty': 'easy'},
            {'question_text': 'What is === in JS?', 'option_a': 'Assignment', 'option_b': 'Strict equality (checks value and type)', 'option_c': 'Loose equality', 'option_d': 'Arrow function', 'correct_answer': 'B', 'explanation': 'Avoids automatic type conversion during comparison.', 'difficulty': 'medium'},
            {'question_text': 'What is a Closure?', 'option_a': 'Ending a loop', 'option_b': 'Function retaining access to its lexical scope', 'option_c': 'Closing a div tag', 'option_d': 'A CSS property', 'correct_answer': 'B', 'explanation': 'Inner function remembers outer variables.', 'difficulty': 'hard'},
            {'question_text': 'What does array `.map()` do?', 'option_a': 'Filters items', 'option_b': 'Returns a single value', 'option_c': 'Creates a new array populated with results of a function', 'option_d': 'Finds coordinates', 'correct_answer': 'C', 'explanation': 'Transforms data in an array.', 'difficulty': 'medium'},
            {'question_text': 'What is React?', 'option_a': 'Backend framework', 'option_b': 'JS library for building UIs', 'option_c': 'Database tool', 'option_d': 'CSS compiler', 'correct_answer': 'B', 'explanation': 'Maintained by Meta for component-based UIs.', 'difficulty': 'easy'},
            {'question_text': 'What is JSX?', 'option_a': 'JavaScript XML', 'option_b': 'Java Extension', 'option_c': 'JSON format', 'option_d': 'Server script', 'correct_answer': 'A', 'explanation': 'Syntax extension allowing HTML inside JS.', 'difficulty': 'medium'},
            {'question_text': 'Hook for managing state?', 'option_a': 'useEffect', 'option_b': 'useState', 'option_c': 'useReducer', 'option_d': 'useContext', 'correct_answer': 'B', 'explanation': 'Returns state value and updater function.', 'difficulty': 'easy'},
            {'question_text': 'What is Virtual DOM?', 'option_a': 'Direct HTML copy', 'option_b': 'Lightweight in-memory representation of real DOM', 'option_c': '3D website', 'option_d': 'Chrome plugin', 'correct_answer': 'B', 'explanation': 'Optimizes React rendering performance.', 'difficulty': 'medium'},
            {'question_text': 'Purpose of `useEffect`?', 'option_a': 'Style components', 'option_b': 'Handle side effects (e.g., API calls)', 'option_c': 'Route pages', 'option_d': 'Declare variables', 'correct_answer': 'B', 'explanation': 'Runs code after render.', 'difficulty': 'medium'},
            {'question_text': 'What is Node.js?', 'option_a': 'Browser', 'option_b': 'JS runtime on V8 engine', 'option_c': 'Frontend framework', 'option_d': 'Database', 'correct_answer': 'B', 'explanation': 'Runs JS on the server.', 'difficulty': 'easy'},
            {'question_text': 'Initialize new npm project?', 'option_a': 'npm start', 'option_b': 'npm build', 'option_c': 'npm init', 'option_d': 'npm new', 'correct_answer': 'C', 'explanation': 'Creates package.json.', 'difficulty': 'easy'},
            {'question_text': 'What is Express.js?', 'option_a': 'Web framework for Node.js', 'option_b': 'Database', 'option_c': 'CSS library', 'option_d': 'Testing tool', 'correct_answer': 'A', 'explanation': 'Simplifies server routing and middleware.', 'difficulty': 'medium'},
            {'question_text': 'What is CORS?', 'option_a': 'Cross-Origin Resource Sharing', 'option_b': 'CSS Rendering Style', 'option_c': 'Central Router', 'option_d': 'Code Origin', 'correct_answer': 'A', 'explanation': 'Security policy for cross-domain requests.', 'difficulty': 'medium'},
            {'question_text': 'Advantage of SSR in Next.js?', 'option_a': 'No JS required', 'option_b': 'Better SEO and faster initial load', 'option_c': 'Uses Python', 'option_d': 'Disables CSS', 'correct_answer': 'B', 'explanation': 'Server sends fully rendered HTML.', 'difficulty': 'hard'}
        ],
        'Artificial Intelligence & Machine Learning': [
            {'question_text': 'What is Supervised Learning?', 'option_a': 'Unlabeled data training', 'option_b': 'Training with input data and correct output labels', 'option_c': 'Game playing AI', 'option_d': 'Hardcoded rules', 'correct_answer': 'B', 'explanation': 'Model learns from examples with known answers.', 'difficulty': 'easy'},
            {'question_text': 'Example of Unsupervised Learning?', 'option_a': 'Spam detection', 'option_b': 'Image classification', 'option_c': 'Customer clustering', 'option_d': 'Price prediction', 'correct_answer': 'C', 'explanation': 'Clustering finds hidden patterns in unlabeled data.', 'difficulty': 'medium'},
            {'question_text': 'What is Overfitting?', 'option_a': 'Model performs well on training data but poorly on test data', 'option_b': 'Model is too simple', 'option_c': 'Data is too large', 'option_d': 'PC overheats', 'correct_answer': 'A', 'explanation': 'Model memorizes noise instead of learning patterns.', 'difficulty': 'medium'},
            {'question_text': 'Purpose of Gradient Descent?', 'option_a': 'Increase errors', 'option_b': 'Find minimum of a function to reduce loss', 'option_c': 'Compress images', 'option_d': 'Sort data', 'correct_answer': 'B', 'explanation': 'Iteratively updates weights to minimize cost.', 'difficulty': 'hard'},
            {'question_text': 'What is an Epoch?', 'option_a': 'Single neuron layer', 'option_b': 'One full pass of training dataset through algorithm', 'option_c': 'Prediction time', 'option_d': 'Activation function', 'correct_answer': 'B', 'explanation': 'Usually takes many epochs to train a model.', 'difficulty': 'easy'},
            {'question_text': 'What does CNN stand for?', 'option_a': 'Computer Network Node', 'option_b': 'Convolutional Neural Network', 'option_c': 'Complex Neural Node', 'option_d': 'Central Network Node', 'correct_answer': 'B', 'explanation': 'Used primarily for image processing.', 'difficulty': 'easy'},
            {'question_text': 'Use case for RNN?', 'option_a': 'Static images', 'option_b': 'Sequential data (speech, time series)', 'option_c': 'Database sorting', 'option_d': 'CSS layout', 'correct_answer': 'B', 'explanation': 'Recurrent networks have memory for sequences.', 'difficulty': 'medium'},
            {'question_text': 'What does NLP mean?', 'option_a': 'Natural Language Processing', 'option_b': 'Native Logic Protocol', 'option_c': 'Neural Layer Protocol', 'option_d': 'Network Load Procedure', 'correct_answer': 'A', 'explanation': 'AI dealing with human text and speech.', 'difficulty': 'easy'},
            {'question_text': 'What is an LLM?', 'option_a': 'Language translation tool only', 'option_b': 'Large Language Model trained on vast text data', 'option_c': 'SQL database type', 'option_d': 'Edge device algorithm', 'correct_answer': 'B', 'explanation': 'Examples include GPT-4 and Gemini.', 'difficulty': 'medium'},
            {'question_text': 'What is Prompt Engineering?', 'option_a': 'Fixing servers', 'option_b': 'Designing effective inputs to guide AI outputs', 'option_c': 'Writing C++ code', 'option_d': 'Building robots', 'correct_answer': 'B', 'explanation': 'Optimizes communication with generative AI.', 'difficulty': 'easy'},
            {'question_text': 'What is an AI Hallucination?', 'option_a': 'Visual screen glitch', 'option_b': 'AI confidently generating false or nonsensical information', 'option_c': 'AI deleting code', 'option_d': 'VR feature', 'correct_answer': 'B', 'explanation': 'LLMs predict text, sometimes inventing false facts.', 'difficulty': 'medium'},
            {'question_text': 'What is a Confusion Matrix?', 'option_a': 'Math equation', 'option_b': 'Table evaluating classification performance (True/False Positives)', 'option_c': 'Code bug', 'option_d': 'Neural layer', 'correct_answer': 'B', 'explanation': 'Visualizes prediction accuracy vs actual labels.', 'difficulty': 'hard'},
            {'question_text': 'Purpose of Activation Function?', 'option_a': 'Turn on PC', 'option_b': 'Introduce non-linearity into a neuron\'s output', 'option_c': 'Download data', 'option_d': 'Stop training', 'correct_answer': 'B', 'explanation': 'Allows networks to solve complex, non-linear problems.', 'difficulty': 'hard'},
            {'question_text': 'What is Tokenization in NLP?', 'option_a': 'Encrypting passwords', 'option_b': 'Breaking text into smaller units (words/subwords)', 'option_c': 'Buying crypto', 'option_d': 'Deleting spaces', 'correct_answer': 'B', 'explanation': 'First step in processing text for AI.', 'difficulty': 'medium'},
            {'question_text': 'What is Reinforcement Learning?', 'option_a': 'Learning from Excel', 'option_b': 'Training an agent via rewards and punishments', 'option_c': 'Reading text', 'option_d': 'SQL querying', 'correct_answer': 'B', 'explanation': 'Used heavily in robotics and game AI (like chess/Go).', 'difficulty': 'medium'}
        ],

        # --- BRAND NEW CATEGORIES (15 Qs Each) ---
        'Java Programming & OOP': [
            {'question_text': 'Difference between JDK, JRE, and JVM?', 'option_a': 'They are all the same', 'option_b': 'JDK contains JRE and tools; JRE contains JVM and libraries', 'option_c': 'JVM compiles code, JDK runs it', 'option_d': 'JRE is hardware', 'correct_answer': 'B', 'explanation': 'JDK is for development, JRE is for running, JVM executes bytecode.', 'difficulty': 'medium'},
            {'question_text': 'Why is the main method in Java `static`?', 'option_a': 'To make it run faster', 'option_b': 'So JVM can invoke it without instantiating the class', 'option_c': 'To prevent inheritance', 'option_d': 'It is a security feature', 'correct_answer': 'B', 'explanation': 'Static methods belong to the class, not the object.', 'difficulty': 'medium'},
            {'question_text': 'What is Constructor Overloading?', 'option_a': 'Having multiple classes with the same name', 'option_b': 'Having multiple constructors with different parameter lists', 'option_c': 'Calling a parent constructor', 'option_d': 'A memory error', 'correct_answer': 'B', 'explanation': 'Allows creating objects with different initial data.', 'difficulty': 'easy'},
            {'question_text': 'What is a Java Interface?', 'option_a': 'A GUI window', 'option_b': 'A completely abstract class used to group related methods with empty bodies', 'option_c': 'A type of database', 'option_d': 'A network port', 'correct_answer': 'B', 'explanation': 'Interfaces define a contract that implementing classes must follow.', 'difficulty': 'easy'},
            {'question_text': 'Difference between `final`, `finally`, and `finalize`?', 'option_a': 'No difference', 'option_b': 'final is keyword, finally is block, finalize is method', 'option_c': 'All are memory management tools', 'option_d': 'All are exception handlers', 'correct_answer': 'B', 'explanation': 'final restricts modification, finally executes after try-catch, finalize is called before garbage collection.', 'difficulty': 'hard'},
            {'question_text': 'String vs StringBuilder in Java?', 'option_a': 'String is mutable, StringBuilder is immutable', 'option_b': 'String is immutable, StringBuilder is mutable', 'option_c': 'Both are mutable', 'option_d': 'Both are immutable', 'correct_answer': 'B', 'explanation': 'Modifying a String creates a new object; StringBuilder modifies the existing one.', 'difficulty': 'medium'},
            {'question_text': 'What is Garbage Collection in Java?', 'option_a': 'Deleting unused files', 'option_b': 'Automatic memory management deleting unreachable objects', 'option_c': 'Clearing browser cache', 'option_d': 'Uninstalling Java', 'correct_answer': 'B', 'explanation': 'Handled automatically by the JVM to free heap memory.', 'difficulty': 'easy'},
            {'question_text': 'Checked vs Unchecked Exceptions?', 'option_a': 'Checked are checked at compile-time, Unchecked at runtime', 'option_b': 'Unchecked are checked at compile-time', 'option_c': 'Checked cannot be caught', 'option_d': 'No difference', 'correct_answer': 'A', 'explanation': 'Checked exceptions force the programmer to handle them in code (try-catch).', 'difficulty': 'medium'},
            {'question_text': 'HashMap vs HashTable?', 'option_a': 'HashTable is synchronized (thread-safe), HashMap is not', 'option_b': 'HashMap is thread-safe', 'option_c': 'HashTable allows null keys', 'option_d': 'They are identical', 'correct_answer': 'A', 'explanation': 'HashMap is faster for single-threaded applications as it isn\'t synchronized.', 'difficulty': 'hard'},
            {'question_text': 'What is Autoboxing?', 'option_a': 'Automatic car driving', 'option_b': 'Automatic conversion the Java compiler makes between primitive types and their corresponding object wrapper classes', 'option_c': 'Creating UI boxes', 'option_d': 'Garbage collection technique', 'correct_answer': 'B', 'explanation': 'E.g., converting an int to an Integer.', 'difficulty': 'medium'},
            {'question_text': 'Does Java support multiple inheritance?', 'option_a': 'Yes, for classes', 'option_b': 'No, not at all', 'option_c': 'Yes, but only through Interfaces', 'option_d': 'Only in Java 8', 'correct_answer': 'C', 'explanation': 'To avoid the diamond problem, Java uses interfaces for multiple inheritance.', 'difficulty': 'medium'},
            {'question_text': 'What is a Singleton class?', 'option_a': 'A class with only one method', 'option_b': 'A class that can have only one object (instance) created at a time', 'option_c': 'A class with no parent', 'option_d': 'An empty class', 'correct_answer': 'B', 'explanation': 'Often used for configuration settings or database connections.', 'difficulty': 'hard'},
            {'question_text': 'Purpose of the `this` keyword?', 'option_a': 'Refers to parent class', 'option_b': 'Refers to current object instance', 'option_c': 'Exits a loop', 'option_d': 'Creates a new object', 'correct_answer': 'B', 'explanation': 'Used to resolve ambiguity between instance variables and parameters.', 'difficulty': 'easy'},
            {'question_text': 'What is Method Overriding?', 'option_a': 'Methods with same name but different parameters in same class', 'option_b': 'Subclass providing a specific implementation of a method already provided by its parent class', 'option_c': 'Deleting a method', 'option_d': 'Writing a method twice', 'correct_answer': 'B', 'explanation': 'Overriding achieves runtime polymorphism.', 'difficulty': 'easy'},
            {'question_text': 'What is the Java Stream API used for?', 'option_a': 'Streaming videos', 'option_b': 'Processing collections of objects in a functional, declarative style', 'option_c': 'Reading text files', 'option_d': 'Network sockets', 'correct_answer': 'B', 'explanation': 'Introduced in Java 8 for functional-style operations on streams of elements.', 'difficulty': 'hard'}
        ],
        'System Design & Architecture': [
            {'question_text': 'Horizontal vs Vertical Scaling?', 'option_a': 'Horizontal adds more machines, Vertical adds power (CPU/RAM) to an existing machine', 'option_b': 'Vertical adds more machines', 'option_c': 'Horizontal applies to databases only', 'option_d': 'They mean the same thing', 'correct_answer': 'A', 'explanation': 'Horizontal scaling = scale out. Vertical scaling = scale up.', 'difficulty': 'medium'},
            {'question_text': 'What is a Load Balancer?', 'option_a': 'A battery backup', 'option_b': 'A device that acts as a reverse proxy and distributes network/application traffic across multiple servers', 'option_c': 'A type of database', 'option_d': 'A CSS framework', 'correct_answer': 'B', 'explanation': 'Increases capacity and reliability of applications.', 'difficulty': 'easy'},
            {'question_text': 'What does CAP Theorem state?', 'option_a': 'Cost, Availability, Partition Tolerance', 'option_b': 'Consistency, Availability, Partition Tolerance - you can only guarantee two out of three', 'option_c': 'Code, API, Processing', 'option_d': 'Computers Are Powerful', 'correct_answer': 'B', 'explanation': 'A fundamental theorem in distributed data store design.', 'difficulty': 'hard'},
            {'question_text': 'Microservices vs Monolith?', 'option_a': 'Monoliths are better for huge teams', 'option_b': 'Microservices break an app into loosely coupled, independently deployable services', 'option_c': 'Microservices are written in one file', 'option_d': 'Monoliths use microchips', 'correct_answer': 'B', 'explanation': 'Microservices allow teams to develop, deploy, and scale services independently.', 'difficulty': 'medium'},
            {'question_text': 'Purpose of Caching (e.g., Redis)?', 'option_a': 'To slow down the system', 'option_b': 'To store frequently accessed data in memory for sub-millisecond retrieval', 'option_c': 'To permanently save user passwords', 'option_d': 'To format HTML', 'correct_answer': 'B', 'explanation': 'Reduces load on the primary database and speeds up response times.', 'difficulty': 'easy'},
            {'question_text': 'What is Database Sharding?', 'option_a': 'Deleting old records', 'option_b': 'A type of horizontal partitioning that splits a database into smaller, faster, more easily managed parts', 'option_c': 'Encrypting data', 'option_d': 'Merging tables', 'correct_answer': 'B', 'explanation': 'Each shard is held on a separate database server instance, to spread load.', 'difficulty': 'hard'},
            {'question_text': 'What is a CDN (Content Delivery Network)?', 'option_a': 'A TV broadcasting network', 'option_b': 'Geographically distributed group of servers working together to provide fast delivery of Internet content', 'option_c': 'A local area network', 'option_d': 'A secure VPN', 'correct_answer': 'B', 'explanation': 'Caches static assets (images, CSS, JS) close to the end-user.', 'difficulty': 'medium'},
            {'question_text': 'What is an API Gateway?', 'option_a': 'A payment processor', 'option_b': 'A server that acts as an API front-end, receiving API requests, enforcing throttling/security, and routing them to the back-end', 'option_c': 'A router', 'option_d': 'A web browser', 'correct_answer': 'B', 'explanation': 'Crucial in microservice architectures to manage external traffic.', 'difficulty': 'medium'},
            {'question_text': 'What is Consistent Hashing?', 'option_a': 'Using the same password everywhere', 'option_b': 'A hashing technique that minimizes reorganization of keys when nodes are added or removed', 'option_c': 'Encrypting with MD5', 'option_d': 'A sorting algorithm', 'correct_answer': 'B', 'explanation': 'Solves the problem of remapping all keys in distributed caching when a server dies.', 'difficulty': 'hard'},
            {'question_text': 'What is Event-Driven Architecture (e.g., using Kafka)?', 'option_a': 'UI based on mouse clicks', 'option_b': 'A design paradigm in which state changes (events) trigger reactions in decoupled services', 'option_c': 'A database trigger', 'option_d': 'A scheduling algorithm', 'correct_answer': 'B', 'explanation': 'Promotes highly decoupled, asynchronous systems.', 'difficulty': 'hard'},
            {'question_text': 'What is Rate Limiting?', 'option_a': 'Calculating interest', 'option_b': 'Controlling the rate of traffic sent or received by a network interface to prevent abuse/DDoS', 'option_c': 'Speeding up APIs', 'option_d': 'Compressing video', 'correct_answer': 'B', 'explanation': 'Protects backend systems from being overwhelmed.', 'difficulty': 'medium'},
            {'question_text': 'What is a SPOF?', 'option_a': 'Secure Protocol Object Format', 'option_b': 'Single Point of Failure - a part of a system that, if it fails, stops the entire system from working', 'option_c': 'Server Ping Output File', 'option_d': 'Standard Procedure', 'correct_answer': 'B', 'explanation': 'System design aims to eliminate SPOFs via redundancy.', 'difficulty': 'easy'},
            {'question_text': 'Forward vs Reverse Proxy?', 'option_a': 'Forward protects clients, Reverse protects servers', 'option_b': 'Forward protects servers, Reverse protects clients', 'option_c': 'No difference', 'option_d': 'They are database types', 'correct_answer': 'A', 'explanation': 'A reverse proxy sits in front of web servers and forwards client requests to those servers.', 'difficulty': 'hard'},
            {'question_text': 'Stateful vs Stateless systems?', 'option_a': 'Stateless remembers previous interactions, Stateful does not', 'option_b': 'Stateful saves client data on server across requests; Stateless treats each request as independent', 'option_c': 'Stateful is faster', 'option_d': 'Stateless uses more memory', 'correct_answer': 'B', 'explanation': 'Statelessness (like REST) allows easier horizontal scaling.', 'difficulty': 'medium'},
            {'question_text': 'What is a Heartbeat mechanism?', 'option_a': 'A medical app', 'option_b': 'Periodic signals sent by hardware or software to indicate normal operation', 'option_c': 'A CPU clock', 'option_d': 'An API endpoint', 'correct_answer': 'B', 'explanation': 'Used by load balancers and orchestrators to route traffic away from dead nodes.', 'difficulty': 'easy'}
        ],
        'Cloud Computing & DevOps': [
            {'question_text': 'What is IaaS?', 'option_a': 'Internet as a Service', 'option_b': 'Infrastructure as a Service (e.g., AWS EC2)', 'option_c': 'Intelligence as a Service', 'option_d': 'Identity as a Service', 'correct_answer': 'B', 'explanation': 'Provides virtualized computing resources over the internet.', 'difficulty': 'easy'},
            {'question_text': 'What is Docker?', 'option_a': 'A cloud provider', 'option_b': 'A platform to build, run, and share applications with containers', 'option_c': 'A database', 'option_d': 'A programming language', 'correct_answer': 'B', 'explanation': 'Containers package code and dependencies together so the app runs reliably anywhere.', 'difficulty': 'medium'},
            {'question_text': 'What is Kubernetes?', 'option_a': 'A Greek god', 'option_b': 'An open-source container orchestration system for automating deployment, scaling, and management', 'option_c': 'A text editor', 'option_d': 'An AWS specific service', 'correct_answer': 'B', 'explanation': 'Kubernetes manages clusters of Docker containers.', 'difficulty': 'hard'},
            {'question_text': 'What does CI/CD stand for?', 'option_a': 'Cloud Integration / Cloud Deployment', 'option_b': 'Continuous Integration / Continuous Delivery (or Deployment)', 'option_c': 'Code Insertion / Code Deletion', 'option_d': 'Central Interface / Central Database', 'correct_answer': 'B', 'explanation': 'Automates the integration of code changes and delivery to production.', 'difficulty': 'medium'},
            {'question_text': 'Difference between AWS EC2 and S3?', 'option_a': 'S3 is for compute, EC2 is for storage', 'option_b': 'EC2 provides resizable compute capacity (virtual servers); S3 provides object storage', 'option_c': 'EC2 is free', 'option_d': 'S3 is a database', 'correct_answer': 'B', 'explanation': 'EC2 = Virtual Machines. S3 = Cloud hard drive for files/objects.', 'difficulty': 'easy'},
            {'question_text': 'What is Blue/Green Deployment?', 'option_a': 'A UI coloring scheme', 'option_b': 'A release technique reducing downtime by running two identical production environments', 'option_c': 'An eco-friendly server', 'option_d': 'A Git command', 'correct_answer': 'B', 'explanation': 'Traffic is shifted from the blue (old) to green (new) environment once the green is tested.', 'difficulty': 'hard'},
            {'question_text': 'Git Rebase vs Merge?', 'option_a': 'Rebase creates a new commit, Merge rewrites history', 'option_b': 'Merge preserves branch history, Rebase rewrites history to create a linear progression', 'option_c': 'No difference', 'option_d': 'Rebase deletes files', 'correct_answer': 'B', 'explanation': 'Rebase moves the entire feature branch to begin on the tip of the master branch.', 'difficulty': 'hard'},
            {'question_text': 'What is Serverless Computing (e.g., AWS Lambda)?', 'option_a': 'Using computers without CPUs', 'option_b': 'A model where the cloud provider dynamically manages the allocation and provisioning of servers', 'option_c': 'Running code locally', 'option_d': 'A web browser feature', 'correct_answer': 'B', 'explanation': 'Developers write code, and the cloud provider handles the server infrastructure automatically.', 'difficulty': 'medium'},
            {'question_text': 'What is Infrastructure as Code (IaC)?', 'option_a': 'Writing HTML', 'option_b': 'Managing and provisioning computing infrastructure through machine-readable definition files', 'option_c': 'Building physical servers', 'option_d': 'A networking protocol', 'correct_answer': 'B', 'explanation': 'Tools like Terraform or Ansible allow you to define servers in code.', 'difficulty': 'medium'},
            {'question_text': 'What is a Hypervisor?', 'option_a': 'A fast CPU', 'option_b': 'Software that creates and runs virtual machines', 'option_c': 'A network switch', 'option_d': 'A cloud database', 'correct_answer': 'B', 'explanation': 'It separates the OS from the underlying hardware, allowing multiple OSs to share one physical host.', 'difficulty': 'hard'},
            {'question_text': 'Public vs Private Cloud?', 'option_a': 'Public is free, Private is paid', 'option_b': 'Public is shared over the internet (AWS); Private is maintained on a private network for one organization', 'option_c': 'Private is illegal', 'option_d': 'Public has no security', 'correct_answer': 'B', 'explanation': 'Private clouds offer more control but require more maintenance.', 'difficulty': 'easy'},
            {'question_text': 'What is Jenkins?', 'option_a': 'A load balancer', 'option_b': 'An open source automation server used to build CI/CD pipelines', 'option_c': 'An AWS service', 'option_d': 'A type of container', 'correct_answer': 'B', 'explanation': 'Jenkins helps automate the parts of software development related to building, testing, and deploying.', 'difficulty': 'medium'},
            {'question_text': 'What is the primary benefit of deploying microservices in containers?', 'option_a': 'It makes code run slower', 'option_b': 'Ensures environmental consistency, isolation, and fast startup times', 'option_c': 'It avoids using Linux', 'option_d': 'It replaces databases', 'correct_answer': 'B', 'explanation': 'Containers ensure the microservice runs the same way on a laptop as in production.', 'difficulty': 'medium'},
            {'question_text': 'Dockerfile vs Docker Compose?', 'option_a': 'Dockerfile builds a single image; Docker Compose manages multi-container applications', 'option_b': 'Dockerfile is for Windows, Compose is for Mac', 'option_c': 'They are exactly the same', 'option_d': 'Compose creates the Dockerfile', 'correct_answer': 'A', 'explanation': 'Compose uses a YAML file to configure application services.', 'difficulty': 'hard'},
            {'question_text': 'Difference between Git fetch and Git pull?', 'option_a': 'Fetch deletes local files', 'option_b': 'Pull downloads data; Fetch downloads and immediately merges into current branch', 'option_c': 'Fetch downloads data without merging; Pull does a fetch AND a merge', 'option_d': 'No difference', 'correct_answer': 'C', 'explanation': 'Fetch is safe, pull can cause merge conflicts immediately.', 'difficulty': 'medium'}
        ],
        'Software Engineering & Agile': [
            {'question_text': 'What are the core phases of the SDLC?', 'option_a': 'Planning, Analysis, Design, Implementation, Testing, Maintenance', 'option_b': 'Coding and Deploying', 'option_c': 'Frontend, Backend, Database', 'option_d': 'Alpha, Beta, Gamma', 'correct_answer': 'A', 'explanation': 'Software Development Life Cycle covers the entire software creation process.', 'difficulty': 'easy'},
            {'question_text': 'Waterfall vs Agile?', 'option_a': 'Waterfall is flexible, Agile is rigid', 'option_b': 'Waterfall is a linear, sequential approach; Agile is iterative and incremental', 'option_c': 'Agile is only for small apps', 'option_d': 'They are the same', 'correct_answer': 'B', 'explanation': 'Agile adapts to changing requirements, Waterfall follows a strict plan.', 'difficulty': 'medium'},
            {'question_text': 'What is a Sprint in Scrum?', 'option_a': 'Typing code quickly', 'option_b': 'A set, time-boxed period (e.g., 2 weeks) during which specific work must be completed', 'option_c': 'A type of database query', 'option_d': 'A testing phase', 'correct_answer': 'B', 'explanation': 'Sprints make projects manageable and allow for regular feedback.', 'difficulty': 'easy'},
            {'question_text': 'Unit Testing vs Integration Testing?', 'option_a': 'Unit tests individual components; Integration tests how components work together', 'option_b': 'Unit tests the UI; Integration tests the database', 'option_c': 'They are identical', 'option_d': 'Integration tests are written by clients', 'correct_answer': 'A', 'explanation': 'Unit tests are fast and isolated. Integration tests catch connection errors.', 'difficulty': 'medium'},
            {'question_text': 'Black Box vs White Box Testing?', 'option_a': 'Black box tests internal logic; White box tests functionality without knowing code', 'option_b': 'Black box tests functionality without knowing internal code; White box tests internal structures/logic', 'option_c': 'White box is only for Apple products', 'option_d': 'Black box is done in command prompt', 'correct_answer': 'B', 'explanation': 'Black box focuses on inputs and outputs. White box looks at the source code.', 'difficulty': 'medium'},
            {'question_text': 'What is Regression Testing?', 'option_a': 'Testing old hardware', 'option_b': 'Re-running functional and non-functional tests to ensure new code changes haven\'t broken existing features', 'option_c': 'Testing UI colors', 'option_d': 'Testing database speeds', 'correct_answer': 'B', 'explanation': 'Ensures that a bug fix didn\'t introduce a new bug.', 'difficulty': 'hard'},
            {'question_text': 'What is Technical Debt?', 'option_a': 'Money owed for servers', 'option_b': 'The implied cost of additional rework caused by choosing an easy (limited) solution now instead of a better approach', 'option_c': 'A loan from a bank', 'option_d': 'Buying expensive laptops', 'correct_answer': 'B', 'explanation': 'Just like financial debt, it incurs interest (makes future development harder) if not paid down.', 'difficulty': 'medium'},
            {'question_text': 'What is an MVP (Minimum Viable Product)?', 'option_a': 'Most Valuable Programmer', 'option_b': 'A product with just enough features to satisfy early customers and provide feedback for future development', 'option_c': 'A fully finished app', 'option_d': 'A prototype that doesn\'t work', 'correct_answer': 'B', 'explanation': 'Used to test a product hypothesis with minimal resources.', 'difficulty': 'easy'},
            {'question_text': 'What is the purpose of a Version Control System (VCS)?', 'option_a': 'To write code', 'option_b': 'To track and manage changes to software code over time (e.g., Git)', 'option_c': 'To compile code', 'option_d': 'To run a web server', 'correct_answer': 'B', 'explanation': 'Allows teams to collaborate, revert mistakes, and branch features.', 'difficulty': 'easy'},
            {'question_text': 'What is a Pull Request (PR)?', 'option_a': 'Downloading data from a server', 'option_b': 'A method of submitting contributions to an open development project, requesting the maintainer to merge code', 'option_c': 'An API endpoint', 'option_d': 'Deleting code', 'correct_answer': 'B', 'explanation': 'PRs are where code review happens before merging to the main branch.', 'difficulty': 'medium'},
            {'question_text': 'What is Test-Driven Development (TDD)?', 'option_a': 'Writing code first, then testing', 'option_b': 'A process relying on a very short cycle: write a failing test, write code to pass it, then refactor', 'option_c': 'Hiring testers to design the app', 'option_d': 'Testing the UI exclusively', 'correct_answer': 'B', 'explanation': 'TDD ensures high test coverage and modular code.', 'difficulty': 'hard'},
            {'question_text': 'In Jira/Agile, difference between Epic, Story, and Task?', 'option_a': 'No difference', 'option_b': 'Epic is a large body of work; Story is a feature requirement from user perspective; Task is a technical step', 'option_c': 'Epic is a bug, Story is a fix', 'option_d': 'They are coding languages', 'correct_answer': 'B', 'explanation': 'Epics break down into Stories, which break down into Sub-tasks.', 'difficulty': 'medium'},
            {'question_text': 'What is the purpose of a Daily Standup?', 'option_a': 'To write code together', 'option_b': 'A brief 15-minute daily meeting for team members to sync up on progress and blockers', 'option_c': 'To design databases', 'option_d': 'To meet with clients', 'correct_answer': 'B', 'explanation': 'Team members usually answer: What did I do yesterday? What will I do today? Any blockers?', 'difficulty': 'easy'},
            {'question_text': 'What are UML Diagrams used for?', 'option_a': 'Writing HTML', 'option_b': 'Unified Modeling Language is used to visually design and document the architecture of a software system', 'option_c': 'Database hosting', 'option_d': 'Network routing', 'correct_answer': 'B', 'explanation': 'Includes Class, Sequence, and Use Case diagrams.', 'difficulty': 'medium'},
            {'question_text': 'What is Continuous Integration (CI)?', 'option_a': 'Integrating databases together', 'option_b': 'The practice of automating the integration of code changes from multiple contributors into a single software project', 'option_c': 'Working 24/7', 'option_d': 'A frontend framework', 'correct_answer': 'B', 'explanation': 'Ensures code compiles and passes tests automatically when pushed to Git.', 'difficulty': 'hard'}
        ]
    }

    total_questions = 0
    for category in categories:
        if category.name in questions_data:
            for q_data in questions_data[category.name]:
                existing = Question.query.filter_by(
                    question_text=q_data['question_text'],
                    category_id=category.id
                ).first()
                if existing:
                    continue

                question = Question(
                    category_id=category.id,
                    question_text=q_data['question_text'],
                    option_a=q_data['option_a'],
                    option_b=q_data['option_b'],
                    option_c=q_data['option_c'],
                    option_d=q_data['option_d'],
                    correct_answer=q_data['correct_answer'],
                    explanation=q_data['explanation'],
                    difficulty=q_data['difficulty']
                )
                db.session.add(question)
                total_questions += 1

    db.session.commit()
    print(f"Created {total_questions} new questions.")
    return total_questions

def create_resources(admin_id):
    resources_data = [
        {'title': 'System Design Primer', 'description': 'Must-read for product company interviews.', 'resource_type': 'notes', 'content': 'Focus on CAP Theorem, Load Balancing, Microservices, and Database Sharding. Understand when to use NoSQL vs SQL.', 'link': None},
        {'title': 'Java OOP Concepts', 'description': 'Core Java interview guide.', 'resource_type': 'interview_tip', 'content': 'Be prepared to explain Polymorphism with real-world examples, and know the difference between Abstract Classes and Interfaces.', 'link': None},
        {'title': 'Data Structures Practice', 'description': 'DSA problems for technical interviews.', 'resource_type': 'coding_link', 'content': None, 'link': 'https://leetcode.com'},
        {'title': 'React & Frontend Mastery', 'description': 'Guide to modern frontend.', 'resource_type': 'notes', 'content': 'Understand the Virtual DOM, Context API, and how Server-Side Rendering works in Next.js.', 'link': None}
    ]

    total_resources = 0
    for res_data in resources_data:
        existing = Resource.query.filter_by(title=res_data['title']).first()
        if existing:
            continue

        resource = Resource(
            title=res_data['title'],
            description=res_data['description'],
            resource_type=res_data['resource_type'],
            content=res_data['content'],
            link=res_data['link'],
            created_by=admin_id 
        )
        db.session.add(resource)
        total_resources += 1

    db.session.commit()
    print(f"Created {total_resources} resources.")
    return total_resources

def main():
    print("=" * 50)
    print("Seeding Placement Portal Database")
    print("=" * 50)

    app = create_app()
    with app.app_context():
        db.create_all()

        print("\n1. Creating admin user...")
        admin = create_admin_user() 

        print("\n2. Creating categories...")
        categories = create_categories()

        print("\n3. Creating questions...")
        create_questions(categories)

        print("\n4. Creating resources...")
        create_resources(admin.id) 

        print("\n" + "=" * 50)
        print("Database seeding completed!")
        print("Total Questions in DB: 210")
        print("=" * 50)
        print("\nYou can now login with:")
        print("  Email: admin@college.edu")
        print("  Password: admin123")

if __name__ == '__main__':
    main()
