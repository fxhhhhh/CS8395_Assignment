import math
import openai
import os

# Initialize the OpenAI client
openai.api_key = "YOUR_API_KEY"

PROBLEM_DIR = "problem"
SOLUTION_DIR = "solution"

def get_problems_and_solutions(problem_dir: str, solution_dir: str) -> dict:
    dataset = {}

    for filename in range(1,100):
        with open(os.path.join(problem_dir, f"problem_{filename}.txt"), 'r') as f_problem, \
             open(os.path.join(solution_dir, f"solution_{filename}.txt"), 'r') as f_solution:
            prompt = f_problem.read().strip()
            solution = f_solution.read().strip()
            dataset[prompt] = solution

    return dataset

def generative_solution(prompt: str) -> str:
    promot_new = "Give me the solution code, just the code, don't reply anything else, for the following question: " + prompt
    response = openai.Completion.create(engine="davinci", prompt=promot_new, max_tokens=300)
    return response.choices[0].text.strip()

def levenshtein_distance(expected: str, generated: str) -> float:
    # ... (same code as before)

def jaccard_similarity(expected: str, generated: str) -> float:
    set_expected = set(expected.split())
    set_generated = set(generated.split())

    intersection = len(set_expected & set_generated)
    union = len(set_expected | set_generated)
    return intersection / union if union != 0 else 0.0

def benchmark(problem_dir: str, solution_dir: str, evaluation_func) -> dict:
    dataset = get_problems_and_solutions(problem_dir, solution_dir)
    results = {}

    for prompt, expected_solution in dataset.items():
        generated_solution = generative_solution(prompt)
        score = evaluation_func(expected_solution, generated_solution)
        results[prompt] = {
            "Expected": expected_solution,
            "Generated": generated_solution,
            "Score": score
        }

    return results

# Using Levenshtein distance for evaluation
results_levenshtein = benchmark(PROBLEM_DIR, SOLUTION_DIR, levenshtein_distance)

# Using Jaccard similarity for evaluation
results_jaccard = benchmark(PROBLEM_DIR, SOLUTION_DIR, jaccard_similarity)

# Display and analyze results (for one of the methods as an example)
for prompt, data in results_levenshtein.items():
    print(f"Prompt: {prompt}\nExpected: {data['Expected']}\nGenerated: {data['Generated']}\nScore: {data['Score']}\n{'-' * 50}")
