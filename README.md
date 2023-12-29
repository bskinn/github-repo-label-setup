# repo-label-creator: Automatically create custom issue/PR labels in a GitHub repository

**Want a quick way to create a bunch of standard labels in a GitHub repo?**

**You want `repo-label-creator`**

Get the labels you need in a few steps:

1. Configure a GitHub personal access token with repo permissions & set it up in
   your terminal as the `GITHUB_PAT` environment variable.
2. Clone this repo.
3. Create a virtual environment (Python 3.11+), activate, and
   `pip install -r requirements.txt`.
4. Edit `labels.json` to define the labels you want to create.
5. Run `python create_labels.py <owner>/<repo`

And done!

If you want to curate your own set of preferred labels in `labels.json`, then
fork the repo first and push your changes to the labels on your fork.

For now, this code is not packaged for distribution on PyPI. If you'd like to be
able to pip install it, please say so at [#5].


## Motivation

GitHub's labeling features for issues and PRs are powerful and convenient. For
projects of substantial size, though, a structured approach to organizing and
formatting the labels is important to maximize value and usability.

While working on the [Quansight Labs website][labs site] I was exposed to
[Tania Allard]'s style of GitHub label management, and liked it a lot. (Check
out the [repo's labels][labs site labels] for an example.) I've since rolled a
similar approach out to a handful of my repos, and I've liked it enough that I
plan to keep using it.

One drawback to this approach is how many labels you need to create from the
start in order to put the framework in place. Seeing [...RESUME]


## Implementation

...RESUME


[#5]: https://github.com/bskinn/repo-label-creator/issues/5
[labs site]: https://labs.quansight.org
[labs site repo]: https://github.com/Quansight/Quansight-website
[labs site labels]: https://github.com/Quansight/Quansight-website/labels
[Tania Allard]: https://github.com/trallard