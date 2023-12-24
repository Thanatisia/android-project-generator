# CHANGELOGS

## Table of Contents
- [2023-12-24](#2023-12-24)
    + 1019H : v0.1.0

## Logs
### 2023-12-24
#### 0945H
- New
    - Created directory 'package' for holding the AndroidProjectGenerator framework/library classes, functions and attributes
        - Added source file 'apg.py' as the main library
        - Added source file 'apg_latest.py' as a latest development branch
        - Added source file 'apg_stable.py' as a stable branch
- Updates
    - Modified source file 'generator.py'
        - Migrated class AndroidProjectGenerator and related contents into source library 'package/apg.py'
        - Implemented CLI argument parsing
        - Added Platform recognition that determines if system is Windows or Linux before initializing the APG system classes based on the operating system
        - Updated documentationa and usage
- TODO
    - Clean-up and convert 'apg_latest.py' to 'apg.py'

#### 1019H
- Updates
    - Replaced 'apg_stable.py' with the latest release of 'apg.py'

