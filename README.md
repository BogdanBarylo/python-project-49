### Hexlet tests and linter status:
[![Actions Status](https://github.com/BogdanBarylo/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/BogdanBarylo/python-project-49/actions)

**Welcome to the Brain Games!**

This is a small project that consists of 5 math games to test your math skills and have fun.
In each game, the condition to win is 3 correct answers in a row. If the user gives the wrong answer, the game will end. 

1.Game: "brain-even" The essence of the game is this: the user is shown a random number.
And he has to answer yes if the number is even, or no if it is odd.
[![asciicast](https://asciinema.org/a/YQ5xhbM1kW4ArgDkb5Bl0Zt9Z.svg)](https://asciinema.org/a/YQ5xhbM1kW4ArgDkb5Bl0Zt9Z)

2.Game: "brain-calc" the essence of the game: the user is shown a random mathematical expression, which must be calculated and write down the correct answer.
[![asciicast](https://asciinema.org/a/E3udXd1PvdZqCvQ68ACDfeJ7Q.svg)](https://asciinema.org/a/E3udXd1PvdZqCvQ68ACDfeJ7Q)

3.Game: "brain-gcd" the essence of the game is as follows: the user is shown two random numbers. The user must calculate and enter the greatest common divisor of these numbers.
[![asciicast](https://asciinema.org/a/VAQzgia7gZCuk9wxztw57YIbb.svg)](https://asciinema.org/a/VAQzgia7gZCuk9wxztw57YIbb)

4.Game: "brain-pogression" the essence of the game is as follows: the user is shown a random series of progression consisting of 9 numbers and one missing number. The user must enter the missing number.
[![asciicast](https://asciinema.org/a/S8KNyibH5QuTiRnBsp57Oi4Ol.svg)](https://asciinema.org/a/S8KNyibH5QuTiRnBsp57Oi4Ol)

5.Game: "brain-prime" the essence of the game is as follows: the user is shown a random number. The user has to answer yes if the number is prime, or no if it is not prime.
[![asciicast](https://asciinema.org/a/0pdE5ugqw9L7BwNlpyVGzgnr0.svg)](https://asciinema.org/a/0pdE5ugqw9L7BwNlpyVGzgnr0)


Installation requirements:

Python 3.10

Poetry 1.4.0

flake8 6.0.0


Installation instructions:

1.You need to download this repository to your computer.

2.Log in to the project root repository, enter in the terminal  ```make install```

3.The next command should be ```make package-install```

4.To enter the game you need to run the command make + game name. For example:
```
make brain-even
make brain-prime
make brain-gcd
make brain-calc
make brain-progression
```
**5.Enjoy the game :)**

