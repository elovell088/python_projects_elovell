#Chat box test - written by: Eric Lovell
#Tests MCC chat bot to ensure the correct responses based on specific input
#THIS IS FILE FOR TESTING - NOT YET FINALIZED

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

questions_to_ask = [
"How do I submit a dental claim?",
"How many cleaning does my dental insurance cover?",
"Where are the HR policies located?",
"What openings are there to advance my career",
"How long do I have to work before I can take PTO?",
"I'm new, when does my dental coverage start",
"I want to retire. What do I need to do?",
"I want my 1095",
"Where is the covid policy",
"What is the process for requesting time off?",
"How do I request more training",
"I fell at work what should I do?",
"How many days can I work remote",
"HR work from home policy",
"What is the college's policy on remote work?",
"Do I have to take a vacation day to go to my mom's funeral?",
"Do I have to use PTO for bereavement leave?",
"How can I access employee assistance programs or counseling services?",
"How can I access information about community outreach or volunteer opportunities?",
"How can I access information about employee discounts and perks?",
"How can I access information about retirement planning or financial literacy resources?",
"How can I access information about retirement plans and options?",
"How can I access information about the college's mission and values?",
"How can I access information about tuition reimbursement or educational benefits?",
"How can I access my pay stubs and tax forms?",
"How can I access professional development opportunities?",
"How can I access the employee handbook and other HR policies?",
"How can I access training and development resources?",
"How can I address a conflict with a coworker or supervisor?",
"How can I address a performance issue with a coworker or subordinate?",
"How can I view my paycheck?",
"How do I access my paystubs?",
"How do I add a dependent?",
"How do I apply for a promotion or transfer within the college?",
"How do I calculate tax withholding on my paycheck?",
"How do I change my name due to marriage?",
"How do I enroll in a benefits program and what benefits are offered?",
"How do I enroll in the college's health insurance plan?",
"How do I report a concern about the working conditions or environment?",
"How do I report a conflict of interest?",
"How do I report a HIPAA violation?",
"How do I report a problem with my paycheck or benefits?",
"How do I report a safety concern or hazard in the workplace?",
"How do I report a theft or loss of college property?",
"How do I report a violation of FERPA or other privacy laws?",
"How do I report an ethics violation or ethical concern?",
"How do I report an injury or incident that occurred on the job?",
"How do I request a leave of absence?",
"How do I request a reasonable accommodation for a disability?",
"How do I request a reasonable accommodation for a religious belief or practice?",
"How do I request a reference or verification of employment?",
"How do I request time off and what is the process?",
"How do I submit faculty availability?",
"How do I submit my 2 week notice?",
"How do I submit travel expenses?",
"How do I transfer to a different department?",
"How do I update my personal information in the HR system?",
"How long is my child covered under my insurance?",
"How much bereavement leave do we get?",
"How much can I contribute to my HSA?",
"I want proof of employment",
"I'd like to get reimbursed for the conference I went to",
"What bank does the HSA card use?",
"What benefit or 401K plans are available to Macomb employees?",
"What is balance of my FSA",
"What is my current level?",
"What is my current step?",
"What is the college's policy on workplace harassment?",
"What is the policy on attendance and punctuality?",
"What is the policy on dress code and personal appearance?",
"What is the policy on drug and alcohol use in the workplace?",
"What is the policy on employee recognition and awards?",
"What is the policy on maternity or paternity leave?",
"What is the policy on overtime and compensatory time?",
"What is the policy on political activity or advocacy in the workplace?",
"What is the policy on social media use and online behavior?",
"What is the policy on telecommuting or remote work?",
"What is the policy on using personal devices for work purposes?",
"What is the policy on vacation and sick time accrual?",
"What is the policy on workplace harassment and discrimination?",
"What is the procedure for submitting expenses/reimbursements?",
"What is the process for applying for a promotion?",
"What is the process for conducting a performance evaluation?",
"What is the process for filing a complaint or grievance?",
"What is the process for jury duty?",
"What is the process for transferring to another department?",
"What is the process to hire an intern?",
"When will I receive my HSA card?",
"Where are tax forms located?",
"Where can I change my name?",
"Where do I get proof of employment?",
"Where is my W-2?",
"Where is my W-4?",
"Where is the professional development training located?",
"How do I get a verification letter from my car insurance company?",
"How do I find my vision benefits?",
"Who is my vision insurance provider?"]

# Create a new instance of the Chrome driver
url = "https://web.powerva.microsoft.com/environments/aecc2a7d-29be-ebb9-bb56-c92141980302/bots/new_bot_25317fd1ed5e40b79765a9604d9b9176/canvas"
browser = webdriver.Chrome()
browser.get(url)

time.sleep(2)

for question in questions_to_ask:

# Find the message box by class name
    message_box = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/form/input")
    message_box.send_keys(question)

    send_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/button")
    send_button.click()

    time.sleep(.05)


"""
message_box.send_keys("How do I submit a dental claim?")
send_button.click()

time.sleep(2)

message_box.send_keys("Where are the HR policies located?")
send_button.click()

send_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/button")
send_button.click()
time.sleep(1)
get_chat_history = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[3]")
chat_history = get_chat_history.text

time.sleep(2)
print(chat_history)
print("\n\nSPLIT\n\n")
pattern = re.compile(r'^(You said: |You said:|Sent at|Bot true said:|Bot true said: )|(Just now)\s*$', re.MULTILINE)
date_and_time_regex = re.compile(r'\b[a-zA-Z]+\s+\d+\s+at\s+\d{1,2}:\d{2}\s+(?:AM|PM)\b')
# Remove matched substrings using compiled pattern with re.sub
output_string = pattern.sub('', chat_history)

# Print the output
print(output_string)
"""