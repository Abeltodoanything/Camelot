import os
import tkinter as tk
import ttkbootstrap as ttk
from dotenv import load_dotenv 
from playwright.sync_api import sync_playwright
from openai import OpenAI


def cb_ai():
    prompt = cb_question_entry.get()

    completion = client.chat.completions.create(
        model=f"{selected_ai.get()}",
        messages=[{"role": "user", "content": prompt}]
    )

    response = completion.choices[0].message.content.strip()

    cb_output.config(state='normal')
    cb_output.delete("1.0", "end")
    cb_output.insert("end", response)
    cb_output.config(state='disabled')

def ask_ai(question, options):
    prompt = f"""
    Carefully read the following question and answer options. Provide the correct answer based on historical facts or logical reasoning.

    Question: {question}
    Options:
    """ + "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)]) + """

    Instructions:
    - Respond with the exact full text of the correct answer.
    - Do not give any numbers, letters, or extra commentary.
    - Make sure your response exactly matches one of the options above.
    """

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free", # Replace the url with the model you are using.
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()
def start_script():
    with sync_playwright() as playwright:
        run(playwright)

def run(playwright):    

    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()
    page.goto(cvs_link.get())
    
    # Login sequence
    # page.get_by_role("textbox", name="Email").fill(cvs_usr.get()) # TEST
    page.get_by_role("textbox", name="Username").fill(cvs_usr.get()) # FRESNOSTATE
    page.get_by_role("textbox", name="Password").fill(cvs_pas.get())
    # page.get_by_test_id("login-button").click() # TEST
    page.get_by_role("button", name="Login").click() # FRESNOSTATE
    page.get_by_role("button", name="Yes, this is my device").click() # FRESNOSTATE
    for i in range(int(qtn_num.get())):
        output_box._textbox.configure(state='normal')
        output_box.insert('end', f"STARTED {cvs_usr.get()}+{cvs_pas.get()}+{cvs_link.get()}+{qtn_num.get()}\n")
        output_box._textbox.configure(state='disabled')
        
        # Get question text

        # Get answer options

        # Ask AI for answer

        # Determine correct answer
    
    context.close()
    browser.close()

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"))

ai_models = ['deepseek/deepseek-chat-v3-0324:free', 'google/gemini-2.0-flash-exp:free', 'mistralai/devstral-small:free']

window = ttk.Window(themename='darkly')
window_icon = ttk.PhotoImage(file='icons/dragon.png')
window.iconphoto(True, window_icon)
window.attributes('-topmost', True)
window.title("Lounge Lizard")
window.resizable(False,False)
window.bind('<Escape>', lambda event: window.quit())

window_width = 505
window_height = 740
comp_width = window.winfo_screenwidth()
comp_height = window.winfo_screenheight()

left = int(comp_width /2 - window_width /2)
top = int(comp_height /2 - window_height /2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

bg_frame = ttk.Frame(window)
bg_frame.pack(fill="both", expand=True)


# Notebook
notebook = ttk.Notebook(bg_frame)
notebook.pack(anchor='nw', padx=2)
quizbot = ttk.Frame(notebook)
chatbot = ttk.Frame(notebook)
notebook.add(quizbot, text= 'QuizBot')
notebook.add(chatbot, text= 'Chat bot')

# Variables
cvs_usr = ttk.StringVar()
cvs_pas = ttk.StringVar()
cvs_link = ttk.StringVar()
qtn_num = ttk.IntVar(value=10)
display_output = ttk.StringVar()

# Title
title = ttk.Label(quizbot, text= 'C.Q.B.v2', font=("Helvetica", 20, 'bold' ))
title.pack(pady=10, padx=10, anchor='nw')
# Sign in Frame
sign_in = ttk.Labelframe(quizbot, borderwidth=1, relief='solid', text='Sign in')
sign_in.pack(pady=10, padx=10, anchor='nw', fill='x')

# Canvas Username
usr_title = ttk.Label(sign_in, text='Canvas Username')
usr_title.grid(column=0, row=0, pady=10, padx=10)

usr_entry = ttk.Entry(sign_in, textvariable=cvs_usr)
usr_entry.grid(column=1, row=0, pady=10, padx=10)

# Canvas Password
pas_title = ttk.Label(sign_in, text='Canvas Password')
pas_title.grid(column=0, row=2,pady=10, padx=10)

pas_entry = ttk.Entry(sign_in, show='*', textvariable=cvs_pas)
pas_entry.grid(column=1, row=2,pady=10, padx=10)

# Quiz Information Frame
quiz_info = ttk.Labelframe(quizbot, borderwidth=1, relief='solid', text= 'Quiz information')
quiz_info.pack(padx=10, anchor='nw', fill='x')
# Link & number of questions
link_title = ttk.Label(quiz_info, text='URL to Canvas Quiz')
link_title.grid(column=0,row=0,pady=10, padx=10)
link_entry = ttk.Entry(quiz_info, textvariable=cvs_link)
link_entry.grid(column=1,row=0,pady=10, padx=10)

ques_title = ttk.Label(quiz_info, text='# of questions')
ques_title.grid(column=0,row=1,pady=10, padx=10)
ques_entry = ttk.Spinbox(quiz_info, from_=0, to=50, textvariable=qtn_num)
ques_entry.grid(column=1, row=1,pady=10, padx=10)

# Start & Output
end_frame = ttk.Frame(quizbot)
end_frame.pack(pady=5, padx=10)
start_btn = ttk.Button(end_frame, text='Start', command= start_script)
start_btn.pack(pady=10)

output_box = ttk.Text(end_frame,height=450,width= 730, font=("Consolas", 12),wrap='word', state='disabled')
output_box.pack()

# Chatbot
# Variables
cb_question_entry = ttk.StringVar()
selected_ai = ttk.StringVar()

tabframe = ttk.Frame(chatbot)
tabframe.pack(expand=True, fill='both')

cb_output = ttk.Text(tabframe, font=("Helvetica", 12), wrap='word', state='disabled', foreground='white')
cb_output.pack(padx=5, pady=5)

cb_frame = ttk.Frame(tabframe)
cb_frame.pack(pady=10, padx=5)
cb_frame.columnconfigure(0, weight=1)
cb_frame.columnconfigure(1, weight=1)
cb_frame.rowconfigure(0, weight=1)
cb_frame.rowconfigure(1, weight=1)

cb_question = ttk.Entry(cb_frame, width=45, textvariable=cb_question_entry)
cb_question.grid(column=0, row=0, padx=5)

cb_submit = ttk.Button(cb_frame, text='Send', command=cb_ai)
cb_submit.grid(column=1, row=0)

ai_options = ttk.Combobox(cb_frame, textvariable=selected_ai, values=ai_models, state="readonly")
ai_options.grid(column=0, row=1, padx=5, pady=5, sticky='w')
ai_options.current(0)


window.mainloop()