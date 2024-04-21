# FA Simulator
This is a simple Finite Atutomata Simulator made in python using the PyGame Frame work.

A finite automaton (FA) is a simple idealized machine used to recognize patterns within input taken from some character set (or alphabet) C. The job of an FA is to accept or reject an input depending on whether the pattern defined by the FA occurs in the input.

This simulator helps to draw and test state machines (currently works on 2 inputs 'a' and 'b' only), Eliminating the need to draw on paper and manual testing.

# Get Started

1) Clone the repository or download the zip file and extract
2) Open the main.py file in your preferred IDE like pyCharm or visual studio code
3) Install pyGame into your virtual enviornment or intall if globally
4) Run the main.py file.

This is what you will see:

<img width="600" alt="SS-1" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/75e4f202-8ca2-49b6-a085-4765dd7cab76">

There are some instructions on the screen.

Now press the up arrow key to add a new state and press the down arrow key to remove the last state added.
Press left and right arrow keys to switch between selected states. 
The state selected at present is shown in top left corner.

After adding states you cand drag and drop them with holding the left mouse click.

Add some states and drag them arround.

<img width="600" alt="SS-2" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/0a218921-ff1b-4b19-99f6-fde1f9ae7d9c">

Now the important part is to set the transitions from each state to another on an input (this script currently works 2 inputs 'a' and 'b' only).

1) Select the input you want to set the transition for by pressing 'a' or 'b' on keyboard.
2) Right click on the state from which the transition is to start a black arrow with green head will appear
3) Hover the cursot over the target state and press the middle mouse button to set the transition.
4) Transition for input 'a' will be shown with red and transitions for input b will be shown with purple arrows

<img width="600" alt="SS-3" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/9bf95db7-eef9-4da5-a902-8330fa4ed8be">

Now to set end state and Dead Ends

1) Select the desired state by pressing the left and righ arrow keys (selected state is showin in top left corner)
2) To set a state to an end state press 'w' key on keyboard to to return it to a normal state press 'w' again
3) To set a state to an end state preww 'q' key on keyboard to return it to a normal state press 'q' again

<img width="600" alt="Screenshot 2024-04-21 124831" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/5cf0444b-25e0-40de-9d8f-32a3d8f1420f">

To test an input on the example of the state machine you have designed 

1) Enter the input you want to test into the black box at bottom left of the screen (it will only accept 'a' and 'b' )
2) Press the test button below the box.

<img width="749" alt="Screenshot 2024-04-21 125436" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/acf0a53a-2e22-4939-8d87-e13e89f111e0">

After pressing the test button the output will be displayed on the console of the IDE
The outputs can be 'valid string' or 'invalid string'

<img width="270" alt="Screenshot 2024-04-21 125825" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/4247602e-a381-4c25-9f51-089a29295bc4">
<img width="263" alt="Screenshot 2024-04-21 125859" src="https://github.com/kaleem-Durrani/Finite-Automata-Simulator/assets/160228066/b9090fdf-c383-408e-a29c-3820b825ea9c">

