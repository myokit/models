#!/usr/bin/env python3
#
# Tests all models' syntax.
#
import os
import re
#import subprocess
import sys
#import warnings

import myokit

# Natural sort regex
_natural_sort_regex = re.compile(r'([0-9]+)')


def test_models():
    """ Scans for and syntax-checks models. """

    # Scan directory, running models as we find them.
    def scan(root, failed=None):
        if failed is None:
            failed = []

        for filename in sorted(os.listdir(root), key=natural_sort_key):
            path = os.path.join(root, filename)

            # Test syntax
            if os.path.splitext(filename)[1] == '.mmt':
                print(path + '.' * (max(0, 70 - len(path))), end='')
                sys.stdout.flush()

                res = test(path)
                if res is None:
                    print('ok')
                else:
                    print('FAIL')
                    failed.append((path, res))

            # Recurse into subdirectories
            elif os.path.isdir(path):
                # Ignore hidden directories
                if filename[:1] == '.':
                    continue
                scan(path, failed)

        return failed

    failed = scan('.')
    if failed:
        for path, e in failed:
            print('-' * 79)
            print('Error output for: ' + path)
            print(e)
            print()
        print('-' * 79)
        print('Test failed (' + str(len(failed)) + ') error(s).')
        return False
    print('Test passed.')
    return True


def test(path):
    """ Tests a model's syntax. """

    # Check that we can load it
    try:
        m = myokit.load_model(path)
    except myokit.ParseError as e:
        return str(e)

    # Check its meta-data
    tags = [
        'name',
        'mmt_authors',
        'version',
        'desc',
        'display_name',
    ]
    for tag in tags:
        if tag not in m.meta:
            return f'Missing meta data annotation: {tag}'

    return None


def natural_sort_key(s):
    """
    Function to use as ``key`` in a sort, to get natural sorting of strings
    (e.g. "2" before "10").

    Example::

        names.sort(key=natural_sort_key)

    """
    # Code adapted from: http://stackoverflow.com/questions/4836710/
    return [
        int(text) if text.isdigit() else text.lower()
        for text in _natural_sort_regex.split(s)]


if __name__ == '__main__':
    print('Syntax-checking all model files!')
    print('This is used for regular online testing.')
    print('If you are not interested in testing the models,')
    print()
    print('  Press Ctrl+C to abort.')
    print()
    if not test_models():
        sys.exit(1)
