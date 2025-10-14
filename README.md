

 - check versions.ps1 
    enables custom cuda folder
    will go through uv venv in a folder 
    makes  
        $ env-version-check.log
        $ env-watermark-pip.log
- env_compare
    compares the pip.log outputs from the previous step
    makes
        $ env-comparison-output.txt

- del_torch_me.py
    quick check on a single env for cuda and a few modules


