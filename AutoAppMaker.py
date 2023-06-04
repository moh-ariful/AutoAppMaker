import openai
import os

openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful engineer that generates Python code."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    # Change how to access message content
    raw_code = response['choices'][0]['message']['content']
    try:
        # This line removes everything before the first ``` and after the last ```,
        # and also remove the word "python" if it is right after the first ```
        code = raw_code.split("```")[1].strip()
        if code.lower().startswith("python"):
            code = code[6:].strip()
    except IndexError:
        code = ""  # If there is no ``` in the response
    return code

def write_code_to_file(filename, code):
    with open(filename, "w") as f:
        f.write(code)

def main():
    prompt = input("What kind of Python application do you want to make? ")
    code = generate_code(prompt)
    filename = f"{prompt.replace(' ', '_').lower()}.py"
    write_code_to_file(filename, code)
    print(f"Membuat aplikasi Python baru di {filename}")

if __name__ == "__main__":
    main()