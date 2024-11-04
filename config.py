import json
import random

# Load configuration from JSON file
def load_config(file_path='config.json'):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

# Save configuration back to JSON file
def save_config(config, file_path='config.json'):
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

# Generate a preset based on config, applying selective mutation
def generate_preset(config):
    preset = {}
    for param, settings in config['parameters'].items():
        if settings['mutable']:
            # Apply mutation within a specified range
            mutation_intensity = config['mutation_settings']['mutation_intensity']
            min_val = max(settings['min'], settings['initial_value'] - mutation_intensity)
            max_val = min(settings['max'], settings['initial_value'] + mutation_intensity)
            preset[param] = random.randint(min_val, max_val)
        else:
            # Keep fixed parameters at their initial value
            preset[param] = settings['initial_value']
    return preset

# Update feedback log with feedback and modify config if necessary
def update_feedback(config, preset, liked):
    feedback_entry = {
        "preset": preset,
        "liked": liked
    }
    config['feedback_log'].append(feedback_entry)

    # Optional: Adjust mutation settings or parameter ranges based on feedback
    if liked:
        for param in preset:
            if config['parameters'][param]["mutable"]:
                # Update initial value based on feedback to "nudge" future generations
                config['parameters'][param]["initial_value"] = preset[param]
    
    # Save the updated config with feedback and new values
    save_config(config)

# Example usage
config = load_config()

# Generate a batch of presets based on current config settings
batch_size = 5
for _ in range(batch_size):
    preset = generate_preset(config)
    print("Generated Preset:", preset)

    # Example feedback (could be collected through a GUI or user input)
    liked = bool(random.getrandbits(1))  # Randomly like or dislike for this example
    print("Liked:", liked)
    
    # Update config with feedback, and optionally adjust parameters
    update_feedback(config, preset, liked)