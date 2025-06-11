"""Configuration for annotations."""


def pytest_configure(config):
    """Register markers for autograding purposes."""
    config.addinivalue_line(
        "markers", "weight: mark test to run only on named environment"
    )


def pytest_collection_modifyitems(session, config, items):
    """Convert markers on tests into user_properties tuples."""
    for item in items:

        for marker in item.iter_markers(name="weight"):
            weight = marker.args[0]
            item.user_properties.append(("weight", weight))

        item.user_properties.append(("title", item.function.__doc__))
