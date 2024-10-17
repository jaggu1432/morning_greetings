from setuptools import setup, find_packages

setup(
    name='morning_greetings',  # Name of your package
    version='0.1.0',  # Version of your package
    author='Your Name',  # Your name or organization
    author_email='your.email@example.com',  # Your email address
    description='A simple contact manager that sends morning greeting messages.',  # Brief description of your package
    long_description=open('README.md').read(),  # Detailed description read from README.md
    long_description_content_type='text/markdown',  # Type of long description (Markdown in this case)
    url='https://github.com/yourusername/morning_greetings',  # URL for the package, e.g., GitHub repository
    packages=find_packages(),  # Automatically find packages in the project
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify the programming language
        'License :: OSI Approved :: MIT License',  # Specify the license
        'Operating System :: OS Independent',  # Indicate OS compatibility
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[
        # List any dependencies here, e.g., 'requests', 'numpy'
    ],
)
