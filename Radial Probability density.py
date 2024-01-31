#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial

# Constants
a0 = 0.529  # Bohr radius in angstroms, roughly the size of a hydrogen atom

def get_user_input():
    """
    Prompts the user for the principal and azimuthal quantum numbers, ensuring they are valid.
    """
    print("\n--- Quantum Number Input ---")
    inputs = []
    for i in range(3):
        valid_input = False
        while not valid_input:
            try:
                n = int(input(f"\nEnter the principal quantum number n (positive integer) for set {i+1}: "))
                l = int(input(f"Enter the azimuthal quantum number l (integer such that 0 <= l < n) for set {i+1}: "))
                if n > 0 and 0 <= l < n:
                    valid_input = True
                    print("\nGreat job inputting a correct value!")
                    inputs.append((n, l))
                else:
                    print("\nInvalid quantum numbers. Ensure that n is a positive integer and 0 <= l < n.")
            except ValueError:
                print("\nInvalid input. Please enter integers only.")
        if i < 2:
            more = input("\nWould you like to enter another set for comparison? (yes/no): ").lower()
            if more != 'yes':
                break
    return inputs

def radial_wavefunction(r, n, l):
    """
    Calculates the radial wavefunction R_nl(r) for given quantum numbers n and l.
    """
    normalization = np.sqrt((2/(n*a0))**3 * factorial(n-l-1) / (2*n*factorial(n+l)))
    L = genlaguerre(n-l-1, 2*l+1)
    R_nl = normalization * (2*r/n/a0)**l * np.exp(-r/n/a0) * L(2*r/n/a0)
    return R_nl

def radial_probability_density(r, n, l):
    """
    Calculates the radial probability density P(r) for given quantum numbers n and l.
    """
    R_nl_val = radial_wavefunction(r, n, l)
    P_r = r**2 * abs(R_nl_val)**2
    return P_r

def plot_radial_functions(quantum_sets):
    """
    Plots the radial wavefunction and probability density for given sets of quantum numbers.
    """
    print("\n--- Plotting Radial Functions ---")
    plt.figure(figsize=(14, 6))

    for n, l in quantum_sets:
        r_values = np.linspace(0, 50 * a0, 1000)
        R_nl_values = radial_wavefunction(r_values, n, l)
        P_r_values = radial_probability_density(r_values, n, l)

        # Plot the radial wavefunction
        plt.subplot(1, 2, 1)
        plt.plot(r_values/a0, R_nl_values, label=f'Radial Wavefunction (n={n}, l={l})')
        plt.xlabel('Radial Distance (Bohr radius)')
        plt.ylabel('Radial Wavefunction')

        # Plot the radial probability density
        plt.subplot(1, 2, 2)
        plt.plot(r_values/a0, P_r_values, label=f'Radial Probability Density (n={n}, l={l})')
        plt.xlabel('Radial Distance (Bohr radius)')
        plt.ylabel('Radial Probability Density')

    plt.subplot(1, 2, 1)
    plt.title('Comparison of Radial Wavefunctions')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title('Comparison of Radial Probability Densities')
    plt.legend()

    plt.tight_layout()
    plt.show()

def explain_concept(choice):
    """
    Provides simple explanations for different physics concepts regarding quantum mechanics with links to further resources.
    """
    explanations = {
        'A': {
            'text': "The principal quantum number (n) is like the address of an electron in an atom. It tells us which 'floor' (energy level) the electron is on. The higher the number, the further the electron is from the atom's center.",
            'video': 'https://www.youtube.com/watch?v=eRIN9CPDrpo&t=3s' 
        },
        'B': {
            'text': "The azimuthal quantum number (l) describes the shape of the electron's 'room' (orbital shape) on its 'floor'. It gives us an idea of how the electron moves around the nucleus.",
            'video': 'https://www.youtube.com/watch?v=4sLXUr2HWIs&t=12s' 
        },
        'C': {
            'text': "The radial wavefunction is a mathematical function that helps us visualize where we're likely to find an electron in an atom. It changes with distance from the atom's center, showing us how the electron's presence probability changes.",
            'video': 'https://www.youtube.com/watch?v=WUTgyBruBa8&t=40s'  
        },
        'D': {
            'text': "Think of the radial probability density as a way to measure how likely we are to find an electron at different distances from the atom's center. It's like a map showing where the electron might be.",
            'video': 'https://www.youtube.com/watch?v=JyReivWigCg&t=1s' 
        }
    }

    explanation = explanations.get(choice, {"text": "No explanation available for this choice.", "video": ""})
    print("\n" + explanation['text'])
    if explanation['video']:
        print(f"\nLearn more here: {explanation['video']}")

def ask_for_explanation():
    """
    Asks the user if they would like an explanation of any concept.
    """
    exploring = True
    while exploring:
        print("\nWould you like to learn about any of these concepts?")
        print("A - Principal Quantum Number\nB - Azimuthal Quantum Number\nC - Radial Wavefunction\nD - Radial Probability Density")
        print("Enter A, B, C, or D to learn more, or type 'none' to continue.")
        choice = input("\nYour choice: ").upper()
        if choice in ['A', 'B', 'C', 'D']:
            explain_concept(choice)
            proceed = input("\nWould you like to explore other topics? (yes/no): ").lower()
            if proceed != 'yes':
                break
        elif choice == 'NONE':
            break
        else:
            print("\nInvalid choice. Please enter A, B, C, D, or 'none'.")

def display_additional_resources():
    """
    Displays a list of additional resources for learning more about quantum mechanics.
    """
    print("\nFurther Reading and Resources on Quantum Mechanics:")
    resources = [
        "\nIntroduction to Quantum Mechanics 3rd edition - David J. Griffiths https://www.amazon.com/Introduction-Quantum-Mechanics-David-Griffiths/dp/1107189632/ref=sr_1_1?crid=2LD3K9YDZ1JW5&keywords=griffiths+quantum+mechanics+3rd+edition&qid=1701637243&sprefix=griffiths+quantum+mechanics+%2Caps%2C142&sr=8-1&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc",
        "\nQuantum Physics for Beginners -  Carl J. Pratt https://www.amazon.com/Quantum-Physics-Beginners-Understanding-Explanation/dp/B08YQJD281/ref=sr_1_1_sspa?crid=37Y5ZEA5K4URP&keywords=quantum+mechanics&qid=1701638234&sprefix=quantum+mechanics+%2Caps%2C135&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "\nThe Little Book of String Theory -  Steven S. Gubser https://www.amazon.com/Little-String-Theory-Science-Essentials/dp/0691142890/ref=sr_1_5?crid=20QFGHAC5CNTN&keywords=string+theory&qid=1701641307&sprefix=string+theory%2Caps%2C149&sr=8-5",
        "\nReal world use of Quantum Mechanics! https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/",
        "\nHow Quantum Mechanics affect you everyday! https://www.youtube.com/watch?v=KU9Z6WivvOg",
    ]
    for resource in resources:
        print(resource)

if __name__ == "__main__":
    print("Welcome to the Quantum Radial Function Plotter. We hope you enjoy using the program! :) ")
    ask_for_explanation()  # Offer explanations at the beginning about the physics behind the program
    quantum_sets = get_user_input()
    plot_radial_functions(quantum_sets)
    display_additional_resources()
    print("\nThank you for using the Quantum Radial Function Plotter. We hope you had fun and learned something today :) ")


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial

# Constants
a0 = 0.529  # Bohr radius in angstroms, roughly the size of a hydrogen atom

def get_user_input():
    """
    Prompts the user for the principal and azimuthal quantum numbers, ensuring they are valid.
    """
    print("\n--- Quantum Number Input ---")
    inputs = []
    for i in range(3):
        valid_input = False
        while not valid_input:
            try:
                n = int(input(f"\nEnter the principal quantum number n (positive integer) for set {i+1}: "))
                l = int(input(f"Enter the azimuthal quantum number l (integer such that 0 <= l < n) for set {i+1}: "))
                if n > 0 and 0 <= l < n:
                    valid_input = True
                    print("\nGreat job inputting a correct value!")
                    inputs.append((n, l))
                else:
                    print("\nInvalid quantum numbers. Ensure that n is a positive integer and 0 <= l < n.")
            except ValueError:
                print("\nInvalid input. Please enter integers only.")
        if i < 2:
            more = input("\nWould you like to enter another set for comparison? (yes/no): ").lower()
            if more != 'yes':
                break
    return inputs

def radial_wavefunction(r, n, l):
    """
    Calculates the radial wavefunction R_nl(r) for given quantum numbers n and l.
    """
    normalization = np.sqrt((2/(n*a0))**3 * factorial(n-l-1) / (2*n*factorial(n+l)))
    L = genlaguerre(n-l-1, 2*l+1)
    R_nl = normalization * (2*r/n/a0)**l * np.exp(-r/n/a0) * L(2*r/n/a0)
    return R_nl

def radial_probability_density(r, n, l):
    """
    Calculates the radial probability density P(r) for given quantum numbers n and l.
    """
    R_nl_val = radial_wavefunction(r, n, l)
    P_r = r**2 * abs(R_nl_val)**2
    return P_r

def plot_radial_functions(quantum_sets):
    """
    Plots the radial wavefunction and probability density for given sets of quantum numbers.
    """
    print("\n--- Plotting Radial Functions ---")
    plt.figure(figsize=(14, 6))

    for n, l in quantum_sets:
        r_values = np.linspace(0, 50 * a0, 1000)
        R_nl_values = radial_wavefunction(r_values, n, l)
        P_r_values = radial_probability_density(r_values, n, l)

        # Plot the radial wavefunction
        plt.subplot(1, 2, 1)
        plt.plot(r_values/a0, R_nl_values, label=f'Radial Wavefunction (n={n}, l={l})')
        plt.xlabel('Radial Distance (Bohr radius)')
        plt.ylabel('Radial Wavefunction')

        # Plot the radial probability density
        plt.subplot(1, 2, 2)
        plt.plot(r_values/a0, P_r_values, label=f'Radial Probability Density (n={n}, l={l})')
        plt.xlabel('Radial Distance (Bohr radius)')
        plt.ylabel('Radial Probability Density')

    plt.subplot(1, 2, 1)
    plt.title('Comparison of Radial Wavefunctions')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title('Comparison of Radial Probability Densities')
    plt.legend()

    plt.tight_layout()
    plt.show()

def explain_concept(choice):
    """
    Provides simple explanations for different physics concepts regarding quantum mechanics with links to further resources.
    """
    explanations = {
        'A': {
            'text': "The principal quantum number (n) is like the address of an electron in an atom. It tells us which 'floor' (energy level) the electron is on. The higher the number, the further the electron is from the atom's center.",
            'video': 'https://www.youtube.com/watch?v=eRIN9CPDrpo&t=3s' 
        },
        'B': {
            'text': "The azimuthal quantum number (l) describes the shape of the electron's 'room' (orbital shape) on its 'floor'. It gives us an idea of how the electron moves around the nucleus.",
            'video': 'https://www.youtube.com/watch?v=4sLXUr2HWIs&t=12s' 
        },
        'C': {
            'text': "The radial wavefunction is a mathematical function that helps us visualize where we're likely to find an electron in an atom. It changes with distance from the atom's center, showing us how the electron's presence probability changes.",
            'video': 'https://www.youtube.com/watch?v=WUTgyBruBa8&t=40s'  
        },
        'D': {
            'text': "Think of the radial probability density as a way to measure how likely we are to find an electron at different distances from the atom's center. It's like a map showing where the electron might be.",
            'video': 'https://www.youtube.com/watch?v=JyReivWigCg&t=1s' 
        }
    }

    explanation = explanations.get(choice, {"text": "No explanation available for this choice.", "video": ""})
    print("\n" + explanation['text'])
    if explanation['video']:
        print(f"\nLearn more here: {explanation['video']}")

def ask_for_explanation():
    """
    Asks the user if they would like an explanation of any concept.
    """
    exploring = True
    while exploring:
        print("\nWould you like to learn about any of these concepts?")
        print("A - Principal Quantum Number\nB - Azimuthal Quantum Number\nC - Radial Wavefunction\nD - Radial Probability Density")
        print("Enter A, B, C, or D to learn more, or type 'none' to continue.")
        choice = input("\nYour choice: ").upper()
        if choice in ['A', 'B', 'C', 'D']:
            explain_concept(choice)
            proceed = input("\nWould you like to explore other topics? (yes/no): ").lower()
            if proceed != 'yes':
                break
        elif choice == 'NONE':
            break
        else:
            print("\nInvalid choice. Please enter A, B, C, D, or 'none'.")

def display_additional_resources():
    """
    Displays a list of additional resources for learning more about quantum mechanics.
    """
    print("\nFurther Reading and Resources on Quantum Mechanics:")
    resources = [
        "\nIntroduction to Quantum Mechanics 3rd edition - David J. Griffiths https://www.amazon.com/Introduction-Quantum-Mechanics-David-Griffiths/dp/1107189632/ref=sr_1_1?crid=2LD3K9YDZ1JW5&keywords=griffiths+quantum+mechanics+3rd+edition&qid=1701637243&sprefix=griffiths+quantum+mechanics+%2Caps%2C142&sr=8-1&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc",
        "\nQuantum Physics for Beginners -  Carl J. Pratt https://www.amazon.com/Quantum-Physics-Beginners-Understanding-Explanation/dp/B08YQJD281/ref=sr_1_1_sspa?crid=37Y5ZEA5K4URP&keywords=quantum+mechanics&qid=1701638234&sprefix=quantum+mechanics+%2Caps%2C135&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "\nThe Little Book of String Theory -  Steven S. Gubser https://www.amazon.com/Little-String-Theory-Science-Essentials/dp/0691142890/ref=sr_1_5?crid=20QFGHAC5CNTN&keywords=string+theory&qid=1701641307&sprefix=string+theory%2Caps%2C149&sr=8-5",
        "\nReal world use of Quantum Mechanics! https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/",
        "\nHow Quantum Mechanics affect you everyday! https://www.youtube.com/watch?v=KU9Z6WivvOg",
    ]
    for resource in resources:
        print(resource)

if __name__ == "__main__":
    print("Welcome to the Quantum Radial Function Plotter. We hope you enjoy using the program! :) ")
    ask_for_explanation()  # Offer explanations at the beginning about the physics behind the program
    quantum_sets = get_user_input()
    plot_radial_functions(quantum_sets)
    display_additional_resources()
    print("\nThank you for using the Quantum Radial Function Plotter. We hope you had fun and learned something today :) ")


# In[ ]:




