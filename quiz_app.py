import tkinter as tk
from tkinter import ttk

# Define the questions, options, and answers
questions = [
    # Multiple Choice Questions (Single Correct Answer)
    {
        'question': 'What is the primary focus of cybersecurity?',
        'options': ['Enhancing internet speed', 'Protecting computer devices over the internet from attacks', 'Improving computer graphics', 'Increasing storage capacity'],
        'answer': 'Protecting computer devices over the internet from attacks'
    },
    {
        'question': 'Which term is used to describe activities involved in protecting something against attack or danger?',
        'options': ['Cyber', 'Security', 'Network', 'Data'],
        'answer': 'Security'
    },
    {
        'question': 'What is the goal of cyberattacks?',
        'options': ['To enhance software performance', 'To analyze, modify, or destroy sensitive information', 'To improve network speed', 'To create new software applications'],
        'answer': 'To analyze, modify, or destroy sensitive information'
    },
    {
        'question': 'What does information security specifically aim to protect?',
        'options': ['Personal computer hardware', 'Information from theft and tampering', 'Network bandwidth', 'Computer programming languages'],
        'answer': 'Information from theft and tampering'
    },
    {
        'question': 'How is information different from data in the context of cybersecurity?',
        'options': ['Information is more valuable than data', 'Data is more secure than information', 'Information is less structured than data', 'Data is more valuable than information'],
        'answer': 'Information is more valuable than data'
    },
    {
        'question': 'Which triad is essential to cybersecurity goals?',
        'options': ['CIA triad', 'DNS triad', 'IT triad', 'RSA triad'],
        'answer': 'CIA triad'
    },
    {
        'question': 'The CIA triad in cybersecurity stands for which of the following?',
        'options': ['Confidentiality, Integrity, Availability', 'Communication, Integrity, Access', 'Control, Information, Authentication', 'Confidentiality, Interaction, Authorization'],
        'answer': 'Confidentiality, Integrity, Availability'
    },
    {
        'question': 'What usually drives the attackers in a cyberattack?',
        'options': ['To test new software features', 'To disrupt normal business operations', 'To increase system efficiency', 'To enhance network security'],
        'answer': 'To disrupt normal business operations'
    },
    {
        'question': 'Which of the following is NOT a method to ensure confidentiality?',
        'options': ['Encryption', 'Backups', 'Access Control', 'Physical Security'],
        'answer': 'Backups'
    },
    {
        'question': 'Which technique is used to prevent unauthorized users from accessing data?',
        'options': ['Authentication', 'Checksums', 'Firewalls', 'Version Control'],
        'answer': 'Authentication'
    },
    {
        'question': 'Which of the following is a method to ensure data integrity?',
        'options': ['Encryption', 'Access Control', 'Firewalls', 'Checksums'],
        'answer': 'Checksums'
    },
    {
        'question': 'What does version control help with in terms of data integrity?',
        'options': ['Preventing unauthorized access', 'Ensuring data is not modified or deleted', 'Maintaining and repairing hardware', 'Regularly updating software'],
        'answer': 'Ensuring data is not modified or deleted'
    },
    {
        'question': 'Which measure helps ensure the availability of data?',
        'options': ['Encryption', 'Access Control', 'Backups stored in a geographically-isolated location', 'Checksums'],
        'answer': 'Backups stored in a geographically-isolated location'
    },
    {
        'question': 'Maintaining and repairing hardware regularly is crucial for ensuring:',
        'options': ['Confidentiality', 'Integrity', 'Availability', 'Encryption'],
        'answer': 'Availability'
    },
    {
        'question': 'What is the main goal of ethical hacking?',
        'options': ['To disrupt an organization’s operations', 'To find and fix security weaknesses in computer networks', 'To steal sensitive information', 'To develop new hacking tools'],
        'answer': 'To find and fix security weaknesses in computer networks'
    },
    {
        'question': 'Which of the following best describes a cracker?',
        'options': ['A security professional who protects networks', 'A hacker who uses skills for destructive purposes', 'A tool used for network testing', 'A method for encrypting data'],
        'answer': 'A hacker who uses skills for destructive purposes'
    },
    {
        'question': 'What term describes a flaw or weakness in a computer system?',
        'options': ['Threat', 'Risk', 'Vulnerability', 'Exploit'],
        'answer': 'Vulnerability'
    },
    {
        'question': 'An exploit is best described as:',
        'options': ['A potential security breach', 'A piece of software that takes advantage of vulnerabilities', 'A tool for maintaining hardware', 'A method of data encryption'],
        'answer': 'A piece of software that takes advantage of vulnerabilities'
    },
    {
        'question': 'Which term refers to the potential cause of loss or damage to a computer system?',
        'options': ['Vulnerability', 'Threat', 'Risk', 'Exploit'],
        'answer': 'Risk'
    },
    {
        'question': 'What is a "Target of Evaluation" (TOE)?',
        'options': ['A software tool used for ethical hacking', 'A piece of data used to check for vulnerabilities', 'Evaluation criteria used for creating security targets and protection profiles', 'A type of hacker'],
        'answer': 'Evaluation criteria used for creating security targets and protection profiles'
    },
    {
        'question': 'What is the primary objective of the "Reconnaissance" phase in ethical hacking?',
        'options': ['To exploit vulnerabilities', 'To gather all possible information about the target', 'To maintain access to the target system', 'To cover tracks and avoid detection'],
        'answer': 'To gather all possible information about the target'
    },
    {
        'question': 'During which phase do ethical hackers use gathered information to examine the network?',
        'options': ['Reconnaissance', 'Scanning', 'Gaining Access', 'Covering Tracks'],
        'answer': 'Scanning'
    },
    {
        'question': 'In which phase do ethical hackers attempt to keep their access to a target system for future use?',
        'options': ['Reconnaissance', 'Gaining Access', 'Maintaining Access', 'Covering Tracks'],
        'answer': 'Maintaining Access'
    },
    {
        'question': 'What is the main goal of the "Covering Tracks" phase?',
        'options': ['To gain unauthorized access', 'To avoid leaving traces and detection', 'To gather information about the target', 'To alter data to affect integrity'],
        'answer': 'To avoid leaving traces and detection'
    },
    {
        'question': 'Which type of attack affects confidentiality by observing data without altering it?',
        'options': ['Active Attack', 'Insider Attack', 'Passive Attack', 'Outsider Attack'],
        'answer': 'Passive Attack'
    },
    {
        'question': 'Which of the following attacks affects integrity and availability?',
        'options': ['Passive Attack', 'Insider Attack', 'Active Attack', 'Cloud Computing Threats'],
        'answer': 'Active Attack'
    },
    {
        'question': 'An attack performed by an insider is known as:',
        'options': ['Insider Attack', 'Passive Attack', 'Outsider Attack', 'Active Attack'],
        'answer': 'Insider Attack'
    },
    {
        'question': 'What kind of attack involves altering data in a noticeable way?',
        'options': ['Passive Attack', 'Active Attack', 'Insider Attack', 'Outsider Attack'],
        'answer': 'Active Attack'
    },
    {
        'question': 'Which of the following is NOT considered an attack vector?',
        'options': ['Cloud Computing Threats', 'Mobile Threats', 'Physical Security', 'Phishing'],
        'answer': 'Physical Security'
    },
    {
        'question': 'Which attack vector involves deceptive emails to steal information?',
        'options': ['Botnets', 'Web Application Hacking', 'Phishing', 'Viruses and Worms'],
        'answer': 'Phishing'
    },
    {
        'question': 'Which type of testing involves evaluating security with no prior knowledge of the network infrastructure?',
        'options': ['White-box Testing', 'Black-box Testing', 'Gray-box Testing', 'Red-box Testing'],
        'answer': 'Black-box Testing'
    },
    {
        'question': 'What is the main difference between White-box and Gray-box testing?',
        'options': ['White-box testing is done with complete knowledge of the network, whereas Gray-box testing is done with some insider knowledge.', 'White-box testing is performed externally, while Gray-box testing is performed internally.', 'White-box testing involves passive attacks, whereas Gray-box testing involves active attacks.', 'White-box testing uses no tools, while Gray-box testing uses advanced tools.'],
        'answer': 'White-box testing is done with complete knowledge of the network, whereas Gray-box testing is done with some insider knowledge.'
    },

    # True/False Questions
    {
        'question': 'Information is more valuable than data.',
        'options': ['True', 'False'],
        'answer': 'True'
    },
    {
        'question': 'Ethical hackers use different tools than malicious hackers to test security vulnerabilities.',
        'options': ['True', 'False'],
        'answer': 'False'
    },
    {
        'question': 'Availability in cybersecurity means data should be available to everyone.',
        'options': ['True', 'False'],
        'answer': 'False'
    },
    {
        'question': 'Remote access means having physical access to the computer system.',
        'options': ['True', 'False'],
        'answer': 'False'
    },
    {
        'question': 'Most network security breaches originate from outside the organization.',
        'options': ['True', 'False'],
        'answer': 'False'
    },

    # Short Answer Questions
    {
        'question': 'What is the goal of cyberattacks?',
        'options': ['To analyze, modify, or destroy sensitive information, extort money, or disrupt operations', 'None of the above'],
        'answer': 'To analyze, modify, or destroy sensitive information, extort money, or disrupt operations'
    },
    {
        'question': 'What is the definition of a "vulnerability" in cybersecurity?',
        'options': ['A flaw or weakness in a computer system.', 'A method of encrypting data.', 'A security feature.', 'None of the above.'],
        'answer': 'A flaw or weakness in a computer system.'
    },
    {
        'question': 'What is the purpose of ethical hacking?',
        'options': ['To find security weaknesses in networks.', 'To disrupt operations.', 'To steal data.', 'None of the above.'],
        'answer': 'To find security weaknesses in networks.'
    },
    {
        'question': 'What is the significance of the GDPR in cybersecurity?',
        'options': ['Set regulations for data protection and privacy for individuals within the EU', 'A type of encryption protocol', 'A method of data backup', 'A security software'],
        'answer': 'Set regulations for data protection and privacy for individuals within the EU'
    },
    {
        'question': 'List two types of attacks and their impact on confidentiality, integrity, or availability.',
        'options': ['Passive Attack (affects confidentiality), Active Attack (affects integrity and availability)', 'Any two types of attack.'],
        'answer': 'Passive Attack (affects confidentiality), Active Attack (affects integrity and availability)'
    },
]

# Create the main application window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("800x600")
root.configure(bg='#f5f5f5')

# Define global variables
current_question = 0
score = 0
total_questions = len(questions)
option_vars = []

# Create custom styles
header_font = ('Helvetica', 18, 'bold')
option_font = ('Helvetica', 14)
button_font = ('Helvetica', 12, 'bold')

# Create widgets
header_frame = tk.Frame(root, bg='#f5f5f5')
header_frame.pack(pady=20)

question_label = tk.Label(header_frame, text="", wraplength=750, font=header_font, bg='#f5f5f5', fg='#333')
question_label.pack()

options_frame = tk.Frame(root, bg='#f5f5f5')

# Progress bar
progress_frame = tk.Frame(root, bg='#f5f5f5')
progress_frame.pack(pady=10)
progress_label = tk.Label(progress_frame, text="Progress:", font=button_font, bg='#f5f5f5', fg='#333')
progress_label.pack(side=tk.LEFT, padx=10)
progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=500, mode='determinate')
progress_bar.pack(side=tk.LEFT, padx=10)

feedback_label = tk.Label(root, text="", font=button_font, bg='#f5f5f5', fg='#333')
feedback_label.pack(pady=10)

button_frame = tk.Frame(root, bg='#f5f5f5')
button_frame.pack(pady=20)

submit_button = tk.Button(button_frame, text="Submit", command=lambda: submit_answers(), font=button_font, bg='#4CAF50', fg='white', padx=20, pady=10, relief=tk.RAISED)
submit_button.grid(row=0, column=2, padx=10)

prev_button = tk.Button(button_frame, text="Previous", command=lambda: prev_question(), font=button_font, bg='#FF5722', fg='white', padx=20, pady=10, relief=tk.RAISED)
prev_button.grid(row=0, column=0, padx=10)

next_button = tk.Button(button_frame, text="Next", command=lambda: next_question(), font=button_font, bg='#2196F3', fg='white', padx=20, pady=10, relief=tk.RAISED)
next_button.grid(row=0, column=1, padx=10)

finish_button = tk.Button(button_frame, text="Finish Quiz", command=lambda: finish_quiz(), font=button_font, bg='#FF9800', fg='white', padx=20, pady=10, relief=tk.RAISED)
finish_button.grid(row=0, column=3, padx=10)

restart_button = tk.Button(button_frame, text="Restart Quiz", command=lambda: restart_quiz(), font=button_font, bg='#9C27B0', fg='white', padx=20, pady=10, relief=tk.RAISED)
restart_button.grid(row=0, column=4, padx=10)

# Function to update the question and options
def update_question():
    global option_vars
    question = questions[current_question]
    
    # Update the question label
    question_label.config(text=question['question'])
    
    # Clear existing options
    for widget in options_frame.winfo_children():
        widget.destroy()
    
    # Check if the question has multiple options and use the appropriate widgets
    if len(question['options']) == 1 and isinstance(question['options'][0], str):
        # Short answer question, use an Entry widget
        tk.Label(options_frame, text="Your answer:", font=option_font, bg='#f5f5f5').pack(anchor='w', padx=10, pady=5)
        answer_entry = tk.Entry(options_frame)
        answer_entry.pack(pady=5)
        option_vars = [answer_entry]
    else:
        # Use radio buttons for single-answer questions
        option_vars = [tk.StringVar(value='')]  # Use a single variable for radio buttons
        for option in question['options']:
            tk.Radiobutton(options_frame, text=option, variable=option_vars[0], value=option, font=option_font, bg='#f5f5f5').pack(anchor='w', padx=10, pady=5)
    
    # Show the options frame
    options_frame.pack(pady=10)
    
    # Update progress bar
    progress_bar['value'] = (current_question / total_questions) * 100

# Function to show feedback
def show_feedback(is_correct):
    feedback_label.config(text="Correct! Good job." if is_correct else "Incorrect. Try again!", fg='green' if is_correct else 'red')

# Function to check the answers and show the score
def submit_answers():
    global current_question, score
    question = questions[current_question]
    
    # For short answer questions
    if len(question['options']) == 1 and isinstance(question['options'][0], str):
        user_answer = option_vars[0].get().strip().lower()
        if user_answer == question['answer'].strip().lower():
            score += 1
            show_feedback(True)
        else:
            show_feedback(False)
    else:  # For multiple choice questions
        selected_option = option_vars[0].get()
        if selected_option == question['answer']:
            score += 1
            show_feedback(True)
        else:
            show_feedback(False)

# Function to move to the next question or finish the quiz
def next_question():
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        update_question()
        feedback_label.config(text="")
    elif current_question == len(questions) - 1:
        show_score()

# Function to go to the previous question
def prev_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        update_question()
        feedback_label.config(text="")

# Function to finish the quiz early
def finish_quiz():
    show_score()

# Function to show the final score
def show_score():
    message = f"Your final score is {score} out of {total_questions}."
    feedback_label.config(text=message, fg='black')
    submit_button.config(state=tk.DISABLED)
    prev_button.config(state=tk.DISABLED)
    next_button.config(state=tk.DISABLED)
    finish_button.config(state=tk.DISABLED)
    restart_button.config(state=tk.NORMAL)

# Function to restart the quiz
def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0
    update_question()
    feedback_label.config(text="")
    submit_button.config(state=tk.NORMAL)
    prev_button.config(state=tk.NORMAL)
    next_button.config(state=tk.NORMAL)
    finish_button.config(state=tk.NORMAL)
    restart_button.config(state=tk.DISABLED)

# Initialize the first question
update_question()

# Run the Tkinter event loop
root.mainloop()