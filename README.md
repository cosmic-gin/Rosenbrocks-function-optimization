### Optimizing the Rosenbrock Function Using Genetic Algorithm

This project implements a genetic algorithm in Python to optimize the Rosenbrock function, a classic non-convex optimization problem. The Rosenbrock function, also known as Rosenbrock's valley or Rosenbrock's banana function, presents a challenging optimization task due to its narrow, parabolic-shaped valley where the global minimum resides.

#### About the Rosenbrock Function
The Rosenbrock function is defined as follows:
\[ f(x, y) = (a - x)^2 + b \cdot (y - x^2)^2 \]

Where \( a = 1 \) and \( b = 100 \) are parameters typically set to create the narrow valley. The global minimum is located at \( (x, y) = (1, 1) \), where \( f(x, y) = 0 \).

#### Key Steps in the Genetic Algorithm:
1. **Initialization**: Generates an initial population of candidate solutions.
2. **Evaluation**: Evaluates the fitness of each candidate, where fitness is the negative of the Rosenbrock function since we are minimizing.
3. **Selection**: Selects candidates for reproduction based on their fitness using techniques like roulette wheel selection or tournament selection.
4. **Crossover**: Combines pairs of candidates (parents) to produce new candidates (children).
5. **Mutation**: Introduces random modifications to some candidates to maintain genetic diversity.
6. **Replacement**: Forms a new generation of candidates.

#### Code Structure:
- `rosenbrock`: Defines the Rosenbrock function.
- `generate_population`: Generates an initial population within specified bounds.
- `compute_fitness`: Computes the fitness of each candidate solution.
- `select_parents`: Selects parents based on fitness for reproduction.
- `crossover`: Performs crossover to produce offspring.
- `mutation`: Introduces random mutations to offspring.
- Main loop: Executes the genetic algorithm by iterating over generations.

#### Usage:
- Set bounds and population size according to the problem requirements.
- Tune parameters like the number of generations and parents for mating.
- Execute the script to find the optimal solution for the Rosenbrock function.

#### How to Use:
1. Clone the repository.
2. Install Python (if not already installed).
3. Install necessary dependencies (NumPy).
4. Run the script to optimize the Rosenbrock function using the genetic algorithm.

#### Results:
After the specified number of generations, the script outputs the best fitness and the corresponding solution found.
![image](https://github.com/cosmic-gin/Rosenbrocks-function-optimization/assets/111762696/e3119ae6-0845-456b-907e-a3a0fa1c5ae2)
