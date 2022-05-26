<img alt="logo" src="https://raw.githubusercontent.com/riecho14/Green-Trash/image_assets/logo.svg" width="400">

> This script doesn't encourage you to cheat. Cheating is bad. But if anybody is judging your professional skills by the graph at your GitHub profile (which caries no value) they deserve to see a rich graph.
#### Status
![WORKFLOW](https://github.com/riecho14/Green-Trash/actions/workflows/greentrash.yml/badge.svg)

## Before 😶😶😶
![BEFORE](https://github.com/riecho14/Green-Trash/blob/image_assets/before.png)

## After 💦💦💦
![AFTER](https://github.com/riecho14/Green-Trash/blob/image_assets/after.png)

## System requirements
To be able to execute the script you need to have Python and Git installed.

## How to use Green Trash with Github Actions
Create your own repo with click "Use this template" button (forked repo will not work).

Or just do in the manual way:

- Create your own repo
- Copy file `.github/workflows/greentrash.yml` and `trash_update` to your repo
- Change the `email` and `name` information on file [greentrash.yml, line 26 and 27](https://github.com/riecho14/Green-Trash/blob/main/.github/workflows/greentrash.yml#L27)
- Change the scheduling time on file [greentrash.yml, line 8](https://github.com/riecho14/Green-Trash/blob/main/.github/workflows/greentrash.yml#L8). You can use [crontab.guru](https://crontab.guru/) if you don't understand and you are not familiar with the cron schedule string `0 7,8,9,10,11 * * *`.

## How to use Green Trash with Python 
- Make sure you have Python 3 and Git installed
- Also make sure the Git you install is configured with GitHub
- Create an empty Github Repository, if you want to make it private you need to set up your account [to show private contributions](https://help.github.com/en/articles/publicizing-or-hiding-your-private-contributions-on-your-profile) and don't initialize it. This way, GitHub users will see that you contributed something, but they won't be able to see what it is.
- Download the [greentrash.py](https://github.com/riecho14/Green-Trash/archive/refs/heads/main.zip) script and open the file in your text editor.
- Delete greentrash.txt
- You can customize the script in GreenTrash.py however you want here:
```python
# Configuration
number_of_days      = 366                                           # you can change this           
number_of_commits   = 10                                            # you can change this
repositories        = "https://github.com/riecho14/Green-Trash.git" # you can change this
```
- After the script is already, you can immediately run it and crotzz 💦💦💦.

## Troubleshooting
#### No changes after running the script
Are you using a private repository? If so, enable showing private contributions
[following this guide](https://help.github.com/en/articles/publicizing-or-hiding-your-private-contributions-on-your-profile). Sometimes it can take a few minutes for GitHub to re-index your activity. Check if the repository has a new commit and wait a few minutes.

#### Still unlucky
If you're still unlucky, please create an [issue](https://github.com/riecho14/Green-Trash/issues) in this repository and I will try to answer and solve it.

## Credits
- [Github Actions](https://github.com/features/actions)
- [ad-m/github-push-action](https://github.com/ad-m/github-push-action)
- [Shpota/github-activity-generator](https://github.com/Shpota/github-activity-generator)
