# Models

This repository contains partially curated Myokit (`.mmt`) implementations of cardiac electrophysiology models (and a few other ones).
It exists because I want to re-use mmt files in different projects.

If you want to use these models too, please:

 1. Download the files you need.
 2. Cite the publications that the models first appeared in. Do not cite this repository.
 3. If you make _any changes_ to a file, then please update (or simply remove) the `version` and `mmt_authors` fields in its model header. You can set them to anything you like, as long as it makes it clear that the file has been modified.

Or, if you are feeling fancy:

 1. Add this repository as a git submodule to your own project.
 2. Don't change the files, but make changes to the models in code, after you've loaded them with Myokit.
    (If you do think changes to a file are warranted, let me know via an issue or a PR.)

## Why model X and not model Y?

Inclusion or non-inclusion in this list is based entirely on practical reasons.
It is not intended as any kind of judgement on the models' merits or popularity.

## Re-use

Model equations were learned from papers, but where possible also from published software.

An effort has been made to credit the original model authors in each file and to provide a DOI link to an accompanying publication that model users can cite.
Citing this repository is not encouraged.

As far as I understand, in most jurisdictions software can be copyrighted but equations can not.
I also believe that most scientists want their models to be re-used, with **attribution** but little or no other restrictions.
If you are a model author and want your model(s) removed from this list, please let me know so I can do it!

## Curation

In some cases Myokit model output has been compared against the original implementation visually or even numerically.
To avoid licensing complications, such comparisons are not shared in this repository.

## Naming

For ease & convenience, (detailed cardiac electrophysiology) models in this repo are named as `surname-year`.

The used `surname` is that of whoever appeared first in the accompanying paper's author list, in lower case and without diacritics*.
If there are multiple "first authors", an effort is made to acknowledge this in the model meta data but not in the model or file name (even if the first first author didn't do the modelling, if there were only two authors, if the authors gave their model a name, etc.).
If I have got the surname wrong (e.g. wrong part of the name, missing part of name, *diacritics really need to be there) please let me know so that I can correct it.

The used `year` is that of the accompanying journal publication, as indicated by the publisher (so not necessarily corresponding to precedence).

## Versioning

Because these files are meant to be copied and re-used, fancy versioning (e.g. git) is not the full solution.
Every file contains a list of `mmt` file authors (so *not* the model authors), and some hopefully unique version number (usually a date).
If you re-use and edit a file in your project, please update these fields to make it clear that you (not I) edited it, and that it is no longer the file you downloaded originally.
Even just removing both fields is better than not editing.

## Is this the best way to share models?

No.

A future version of [PMR](https://models.physiomeproject.org) might be.

_(In short, each model should be in its own repository, along with meta data in some standard format.
Depending on the use case, people can then use either the most recent version of the model (to share updates and bugfixes) or some tagged version (for replicatability).
The central DB would simply be a list of links to those repositories, with structured search based on the meta data in the repositories, with some low-maintenance procedure for adding or removing links, and with a free-to-use read-only API that would allow people to create their own extracts, e.g. "cardiac electrophysiology models", "carefully curated electrophysiology models", or "Professor X's gallery of biased favouritism".)_

Something like this will hopefully emerge from the current PMR later in this decade, but in the meantime here is my list.
