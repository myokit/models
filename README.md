# Models

This repository contains partially curated Myokit (`.mmt`) implementations of cardiac electrophysiology models (and a few other ones).
It exists because I want to re-use mmt files in different projects.

If you want to use these models too, please:

 1. Download the files you need.
 2. Cite the publications that the models first appeared in. Do not cite this repository.
 3. If you make _any changes_ to a file, then please update (or simply remove) the `version` and `mmt_authors` fields in its model header. You can set them to anything you like, as long as it makes it clear that the file has been modified.

Or, if you are feeling fancy:

 1. Add this repository as a git submodule to your own project.
 2. Don't change the files, but make changes to the models in code, after you've loaded them.
    (If you do think changes to a file are warranted, let me know via an issue or a PR.)

## Why model X and not model Y?

Inclusion or non-inclusion in this list is based entirely on practical reasons.
It is not intended as any kind of judgement on the models' merits or popularity.

## Re-use

Model equations were learned from papers, but where possible also from published software.

An effort has been made to credit the original model authors in each file, and to provide a DOI link to an accompanying publication which model users can cite.
Citing this repository is not encouraged.

As far as I understand, in most jurisdictions software can be copyrighted, but equations can not.
I also believe that most scientists want their models to be re-used, with **attribution** but little or no other restrictions.
However, if you are a model author and do not want your model to appear in this list, please let me know so that I can remove it!

## Curation

In some cases Myokit model output has been compared against the original implementation numerically.
To avoid licensing complications, such comparisons are not shared in this repository.

## Naming

For ease & convenience, models in this repo are named as `surname-year`.

The used `surname` is that of whoever appeared first in the accompanying paper's author list.
If there are multiple first authors, an effort is made to acknowledge this in the model meta data, but not in the name.
If I have got the surname wrong (e.g. wrong part of the name, missing part of name) please let me know so that I can correct it.
Diacritics have usually been omitted for ease of typing, but please let me know if I need to change anything.

The `year` of publication is that of the accompanying journal publication, as indicated by the publisher.

## Versioning

Because these files are meant to be copied and re-used, fancy versioning (e.g. git) is not the full solution.
Every file contains a list of `mmt` file authors (so *not* the model authors), and some hopefully unique version number (usually a date).
If you re-use and edit a file, please update these fields to make it clear that you (not I) edited it, and that it is no longer the file you downloaded originally.
Even just removing both fields is better than leaving them in unedited.

## Is this the best way to share models?

No.

A future version of [PMR](https://models.physiomeproject.org) might be.

In short, each model should be in its own repository, along with meta data in some standard format.
Depending on the use case, people can then use either the most recent version of the model (to share updates and bugfixes) or some tagged version (for replicatability).
The central DB should be a list of links to repositories, providing searchable access (based on the meta data in the repos), with some low-maintenance procedure for adding/removing links, and with a free-to-use read-only API allowing people to create their own extracts (e.g. "cardiac electrophysiology models", "carefully curated electrophysiology models", or "Professor X's biased favourites").

Something like this should hopefully emerge in the next decade, but in the meantime here's my list.

