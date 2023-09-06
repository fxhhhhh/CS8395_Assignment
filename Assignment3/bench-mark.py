import math
import openai
import os

# Initialize the OpenAI client
openai.api_key = "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"

# Directories containing problem prompts and their corresponding solutions
PROBLEM_DIR = "problem"
SOLUTION_DIR = "solution"


def get_problems_and_solutions(problem_dir: str, solution_dir: str) -> dict:
    dataset = {}

    for filename in range(1,100):
        with open(os.path.join(problem_dir, "problem_"+ str(filename))+".txt", 'r') as f_problem, open(os.path.join(solution_dir, "solution_"+ str(filename)+".txt"),
                                                                               'r') as f_solution:
            prompt = f_problem.read().strip()
            solution = f_solution.read().strip()
            dataset[prompt] = solution

    return dataset


def generative_solution(prompt: str) -> str:
    # This is a placeholder for the generative AI solution
    # In reality, you'd replace this with the GPT model's output or any other model's output
    promot_new = "Give me the solution code,  just the code, dont reply anything else, for the following question: " + prompt
    response = openai.Completion.create(engine="davinci", prompt=promot_new, max_tokens=300)

    return response

# method 1: compare the length of the code
# def evaluate_generated_solution(expected: str, generated: str) -> float:
#     length_expected = len(expected)
#     length_generated = len(generated)
#
#     # The difference in length
#     difference = abs(length_expected - length_generated)
#
#     # Convert difference to a score between 0 and 1 using a sigmoid function
#     # The constant 10 determines the "sharpness" of the sigmoid. Adjust based on your preference.
#     score = 1 / (1 + math.exp(10 * (difference/length_expected - 0.1)))
#
#     return score

# method 2: compare the similarity of the code: the number of different words
# def evaluate_generated_solution(expected: str, generated: str) -> float:
#     set_expected = set(expected)
#     set_generated = set(generated)
#
#     intersection = len(set_expected & set_generated)
#     union = len(set_expected | set_generated)
#
#     # calculate Jaccard similarity
#     score = intersection / union if union != 0 else 0.0
#
#     return score
# method 2: compare the similarity of the code: the levenshtein_distance
def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def evaluate_generated_solution(expected: str, generated: str) -> float:

    distance = levenshtein_distance(expected, generated)
    score = 1 - (distance / max(len(expected), len(generated)))
    return score


def benchmark(problem_dir: str, solution_dir: str) -> dict:
    dataset = get_problems_and_solutions(problem_dir, solution_dir)
    results = {}

    for prompt, expected_solution in dataset.items():
        generated_solution = generative_solution(prompt)
        score = evaluate_generated_solution(expected_solution, generated_solution)
        results[prompt] = {
            "Expected": expected_solution,
            "Generated": generated_solution,
            "Score": score
        }

    return results


# Run the benchmark
results = benchmark(PROBLEM_DIR, SOLUTION_DIR)

# Display and analyze results
for prompt, data in results.items():
    print(
        f"Prompt: {prompt}\nExpected: {data['Expected']}\nGenerated: {data['Generated']}\nScore: {data['Score']}\n{'-' * 50}")
