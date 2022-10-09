import yaml


def load_yaml(param_file):
    """_summary_

    Args:
        param_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(param_file, "r") as f:
        params = yaml.safe_load(f)

    return params
