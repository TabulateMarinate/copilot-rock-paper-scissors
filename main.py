from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# define the choices
choices = ["rock", "paper", "scissors", "lizard", "spock"]

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice', '').lower()

    # check if user input is valid
    if user_choice not in choices:
        return jsonify({"error": "Invalid choice. Please choose rock, paper, scissors, lizard, or spock."}), 400

    # get computer choice
    computer_choice = random.choice(choices)

    # determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        result = "You win!"
    else:
        result = "You lose!"

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    }), 200

if __name__ == "__main__":
    app.run(debug=True)