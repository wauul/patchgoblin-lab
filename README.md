# PatchGoblin seeded lab

This is labeled demo data: a small Python weather request library with real offline tests.

`main` has no CI (builder fixture). `broken-install` has an intentional requests/urllib3 constraint conflict (repair fixture).

Run: `python -m pip install -r requirements.txt`, then `python -m pytest`.
No network request is made by the tests.
