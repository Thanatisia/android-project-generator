# APG - Android Project Generator implementation in Bash Shellscript

## Information
### Background
```
A simple Android project structure generator designed and aims to streamline the setting up process 
of your host system for Android application development from command line (without Android Studio).
```

### Purpose
```
The end goal is that you can also learn the specifics of how Android Studio prepares and starts up new projects.
Together with the manual compilation steps, this may potentially help you to understand the entire Mobile application development operational flow without the use of Android Studio.
```

## Setup
### Dependencies
- android-sdk
    + cmdline-tools
+ gradle

### Pre-Requisites

## Documentations
### Synopsis/Syntax
```
generate.sh {options} [actions ...]
```
### Parameters
#### Positionals
- Actions
    - `download [download-targets]` : Download the specified targets
        - Targets
            + dependencies : Download all dependencies required
    - `setup` : Prepare and setup user's shell for Android application development use
    - `template` : Generate a proper Mobile application project structure
        - Notes
            - The generated template project structure have certain sections populated by keywords that have to be edited by the user
                + This is for user design
            + Hence, before building, please look through the project structure and edit according to your needs
    - `gradle` : Setup gradle files within the generated template project structure; To be used after 'template'

### Usage
- Full setup
    - This step will
        1. Download dependencies
        2. Setup user's shell environment
        3. Generate a template android project structure
        4. Setup Gradle in the generated template android project structure
    ```
    ./generate.sh download dependencies setup template gradle
    ```

## Wiki

## Resources

## References

## Remarks

