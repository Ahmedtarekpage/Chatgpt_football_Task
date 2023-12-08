import openai

class FootballChatBot:
    def __init__(self, api_key, team_name="Red Dragons", engine="text-davinci-003"):
        openai.api_key = api_key
        self.engine = engine
        self.team_name = team_name

    def chat_completion(self, prompt):
        try:
            response = openai.Completion.create(
                engine=self.engine,
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            print(f"Error from OpenAI API: {e}")
            return "I'm sorry, but there was an error processing your request."

class FootballChatDemo:
    def __init__(self):
        self.chatbot = FootballChatBot(api_key='your-api-key')  # Replace with your actual API key

    def run(self):
        print(f"Welcome to the {self.chatbot.team_name} Football ChatBot Demo!")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the demo. Goodbye!")
                break

            if not user_input:
                print("Please enter a valid input.")
                continue

            # Construct the conversation prompt
            conversation_history = f"You: {user_input}\nAI: "
            ai_response = self.chatbot.chat_completion(conversation_history)

            # Display AI response
            print(f"AI: {ai_response}")


if __name__ == "__main__":
    demo = FootballChatDemo()
    demo.run()
