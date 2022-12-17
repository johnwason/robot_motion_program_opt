import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='robot-motion-program-opt',
    version='0.0.1',
    description='Robot Motion Program Optimization Package',
    url='https://github.com/johnwason/robot_motion_program_opt',
    packages=setuptools.find_packages("src"),
    package_dir={"" :"src"},
    install_requires=[
        'numpy',
        'pandas',
        'general_robotics_toolbox',
        'matplotlib',
        'sklearn',
        'tesseract_robotics',
        'scipy',
        'qpsolvers[open_source_solvers]',
        'scikit-learn'
    ],
    extras_require={
        "abb": ["abb_motion_program_exec"]
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)