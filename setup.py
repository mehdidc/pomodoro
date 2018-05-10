from setuptools import setup

description = "Simple command line pomodoro app with visualization of statistics"
long_description = """
Simple command line pomodoro app with visualization of statistics.

The Pomodoro technique is a time management technique for improving productivity.
Check (https://en.wikipedia.org/wiki/Pomodoro_Technique) for more details.
The code is based on : http://code.activestate.com/recipes/577358-pomodoro-timer/
"""


setup(
    name="pomodoro-cli",
    version="0.1.4",
    author="mehdi cherti",
    author_email="mehdicherti@gmail.com",
    description=description,
    long_description=long_description,
    license="MIT",
    keywords="pomodoro productivity",
    url="https://github.com/mehdidc/pomodoro",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['pomodoro', 'pomostat'],
    include_package_data=True,
    data_files=['clock.mp3'],
    install_requires=['clize', 'sigtools', 'pandas', 'matplotlib'],
)
