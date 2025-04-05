class RepoExistsError(RuntimeError):
    """
    An error that should be raised when a repo exists but it was expected that it
    didn't.
    """

    pass
