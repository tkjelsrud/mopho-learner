import random

class EvolutionaryGenerator:
    def __init__(self, config):
        self.config = config

    def mutate(self, preset):
        mutated_preset = preset.copy()
        for param, settings in self.config['parameters'].items():
            if settings['mutable']:
                # Handle categorical and continuous parameters differently
                if 'options' in settings:
                    # Categorical mutation: randomly pick a different option
                    current_value = preset[param]
                    new_value = random.choice(settings['options'])
                    # Ensure mutation picks a different option if possible
                    while new_value == current_value and len(settings['options']) > 1:
                        new_value = random.choice(settings['options'])
                    mutated_preset[param] = new_value
                else:
                    # Continuous mutation: apply mutation within a range
                    min_val = max(settings['min'], settings['initial_value'] - self.config['mutation_settings']['mutation_intensity'])
                    max_val = min(settings['max'], settings['initial_value'] + self.config['mutation_settings']['mutation_intensity'])
                    mutated_preset[param] = random.randint(min_val, max_val)
        return mutated_preset

