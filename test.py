from yahtzee_env import YahtzeeEnv

# Create the environment
env = YahtzeeEnv()

# Reset and render the environment
state = env.reset()
print("Initial State:", state)

# Test rolling dice and selecting categories
action = [1, 0, 1, 0, 1, -1]  # Keep dice 1, 3, 5; no category chosen yet
state, reward, done, info = env.step(action)
print("After First Roll:", state)

# Test category selection
action = [1, 1, 1, 1, 1, 0]  # Keep all dice; choose category 0 (e.g., "ones")
state, reward, done, info = env.step(action)
print("After Choosing Category:", state)
print("Reward:", reward)