from setuptools import setup, find_packages

setup(
    version="1.0.0",
    name="auto_subtitle_faster_whisper",
    packages=find_packages(),
    py_modules=["auto_subtitle_faster_whisper"],
    author="Miguel Piedrafita",
    install_requires=[
        'faster-whisper',
    ],
    description="With faster whisper, automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['asf=auto_subtitle_faster_whisper.cli:main'],
    },
    include_package_data=True,
)