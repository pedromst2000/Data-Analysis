import os


def get_output_dir(output_folder: str = "outputs") -> str:
    """
    Get or create an output directory for saving visualizations.
    Resolves relative to the current working directory (the project root),
    so it works correctly when each project is run with: python main.py

    Args:
        output_folder (str): Name of the output folder. Default is "outputs".

    Returns:
        str: Absolute path to the output directory.

    Example:
        >>> OUTPUT_DIR = get_output_dir()
        >>> fig.savefig(os.path.join(OUTPUT_DIR, "plot.png"))
    """
    output_dir = os.path.join(os.getcwd(), output_folder)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir