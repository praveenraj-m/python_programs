# python_programs
<details>
<summary> 1.Basic Calculator. </summary>
Explanation:<br>
We define four functions (add, subtract, multiply, divide) that take two parameters and perform basic arithmetic operations.<br>
The input function is used to take user input for two numbers, which are then converted to floats.<br>
The program prints the results of the addition, subtraction, multiplication, and division of the two numbers.  
</details>

<details>
<summary> 2.Number Guessing Game. </summary>
Explanation:<br>
The program generates a random number between 1 and 100 using the random module.<br>
It prompts the user to guess the number and provides feedback on whether the guess is too high or too low.<br>
The game continues until the correct number is guessed.
</details>

<details>
<summary> 3. To-Do List App.</summary>
Explanation:<br>
The program provides a simple menu with options to add tasks, view tasks, or quit.<br>
Tasks are stored in a list, and the user can interactively manage the to-do list.<br>
The app continues running until the user chooses to quit.
</details>

<details>
<summary> 4. Weather App. </summary>
Explanation:<br>
The program prompts the user to enter the city name and constructs a URL to fetch weather data using the OpenWeatherMap API.<br>
It sends an HTTP request using the `requests` library and processes the JSON response.<br>
If the request is successful (status code 200), it extracts and displays the current temperature and weather description.<br>
In case of an error, it prints an error message.
</details>

<details>
<summary> 5. Hangman Game. </summary>
Explanation:<br>
The program selects a random word from a predefined list, and the player needs to guess the word by inputting letters.<br>
It displays the current state of the word with underscores for unguessed letters and updates it as the player guesses correctly.<br>
The player has a limited number of attempts (6 in this case) to guess the word.<br>
If the player guesses the word or runs out of attempts, the game ends.
</details>

<details>
<summary> 6. Basic Website Scraper. </summary>
Explanation:<br>
The Python script uses the `requests` library to fetch the HTML content of 'https://www.google.com' and `BeautifulSoup` to parse the HTML.<br>
It then extracts and prints the `href` attribute of all links (`a` tags) from the Google homepage.
</details>

<details>
<summary> 7. Basic File Handling. </summary>
Explanation:<br>
The Python program demonstrates basic file handling operations - writing content to a file and reading content from a file.<br>
It writes a sample line to a file, then reads and prints the content of the file.
</details>

<details>
<summary> 8. Program that Accepts a Sentence and Calculates the Number of Letters and Digits. </summary>
Explanation:<br>
The Python program defines a function `count_letters_digits` that takes a sentence as input and counts the number of letters and digits in it.<br>
It then takes user input, calls the function, and prints the counts of letters and digits in the entered sentence.
</details>
