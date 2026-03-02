# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The [New Game] button was not functioning properly, as it did not restart the game when clicked. After running out of guesses, the only way to start a new game was by reloading the page. Additionally, the hint logic was reversed. For example, when I guessed 100 and the correct number was 71, the game incorrectly displayed [Go higher] instead of [Go lower]. Similarly, when I guessed 1 and the correct number was 12, it displayed [Go lower] instead of [Go higher]. This made the gameplay confusing and prevented the user from continuing smoothly without refreshing the page. I also notice that setting to change diffulty did not actually change it and the game stay in normal diffulty. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code for this project. One example of a correct AI suggestion was identifying that the game state was not resetting when the [New Game] button was clicked. After reviewing the button’s logic more closely, I confirmed that it was not resetting the number of attempts or clearing the previous game’s status. I verified the fix by updating the reset logic and testing multiple rounds to ensure the game restarted properly each time. One example of an incomplete or misleading AI suggestion involved the hint reversal bug. The AI recognized that the [higher] and [lower] logic might be reversed, but its explanation was incomplete and did not fully resolve the issue. Through manual testing and playing the game multiple times, I was able to clearly identify the reversed condition and correct the comparison logic. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I considered the issue fully resolved after I was able to beat the game two to three times without encountering any errors. The pytest tests were generated with the help of Claude Code, and they covered key scenarios such as winning the game, handling low and high guesses correctly, and verifying that the game state resets properly when starting a new game. Claude helped me understand how the tests worked and what they were validating. After playing the game and becoming more familiar with its behavior, it became much easier for me to debug the code and confirm that everything was functioning as expected.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number keep changing because secret number was set in `st.session_state.secret` which only ran when the key was missing. This mean that when the render cycle was triggered on each interaction, the condition evaluated to true repeatedly and a new random value was picked.

Streamlit recreates the script from top to bottom every time you do something on the page (click a button, type text, etc.). That’s a rerun. To keep data between those reruns you have to store it in `st.session_state`, it behaves like a little persistent dictionary that survives the restart. Otherwise, any local variables are forgotten and you see the default values again.

I added proper initialization and reset logic. For the secret is assigned only if the key doesn’t already exist in session state, and when starting a new game I explicitly re‑set `st.session_state.secret` within the current difficulty range. That prevented random values from being regenerated on each rerun and kept the number fixed for the duration of a game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is combining manual gameplay testing with structured automated tests. Playing the game multiple times helped me understand its behavior from a user perspective, while using pytest helped verify core logic like win conditions, guess comparisons, and state resets. That combination made debugging more systematic and reliable.

Next time I work with AI on a coding task, I would be more deliberate about validating each suggestion immediately instead of assuming the logic is fully correct. I would also break problems into smaller prompts and test each change incrementally rather than applying multiple AI-generated changes at once.

This project changed the way I think about AI-generated code by showing me that AI is a powerful assistant, but not a replacement for critical thinking and testing. It can guide debugging and structure solutions, but understanding the logic and verifying behavior is still my responsibility as the developer.