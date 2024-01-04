import openai
from dotenv import dotenv_values


# setting and hiding the API KEY
config = dotenv_values('.env')
openai.api_key = config['OPENAI_API_KEY']

# helper function to read the response from the ChatAPI


def read_response(response: str) -> str:
    return response.choices[0].message.content


# helper functions to colorize the text in the terminal
def bold(text:str) -> str:
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end


def blue(text:str) -> str:
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end


def red(text:str) -> str:
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end


messages = []


def main():
    while True:
        try:
            user_input = input(blue('You') + ' :')
            messages.append({
                'role': 'user',
                'content': user_input
            })
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages

            )

            answer = read_response(response)

            print(bold(red('Assistant')), ' :', answer)

            messages.append({'role': 'assistant',
                            'content': answer
                             })

        except KeyboardInterrupt:
            print('exiting...')
            break


if __name__ == "__main__":
    main()
