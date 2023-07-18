from setuptools import setup, find_packages
import os

DESCRIPTION = 'OpenAI Gym environment designed for training RL agents to control the flight of a two-dimensional drone.'
LONG_DESCRIPTION = ('This package contains OpenAI Gym environment designed for training RL agents to control the flight of a '
                    'two-dimensional drone. The environment is automatically registered under id: drone-2d-custom-v0, '
                    'so it can be easily used by RL agent training libraries, such as StableBaselines3.')

setup(
    name='drone_2d_custom_gym_env',
    version='1.3.2',
    author='Sinan Ibrahim',
    author_email='S.ibrahim@innopolis.university',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data = True,
    install_requires=['gym', 'pygame', 'pymunk', 'numpy', 'stable-baselines3[extra]'],
    keywords=['reinforcement learning', 'gym environment', 'StableBaselines3', 'OpenAI Gym']

)
