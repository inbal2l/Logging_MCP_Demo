from pathlib import Path

def _load_file(relative_path: str) -> str:
    """Load file content from the specified relative path.
    
    Args:
        relative_path: The relative path to the file from the project root
        
    Returns:
        The content of the file as a string
    """
    try:
        current_dir = Path(__file__).parent  # src/utils/
        project_root = current_dir.parent.parent  # project root
        file_path = project_root / relative_path
        
        with open(file_path, 'rb') as file:
            content = file.read().decode('utf-8', errors='ignore')
        
        print(f"File loaded: {file_path} ({len(content)} chars)")
        return content
    
    except Exception as e:
        return f"Error reading file: {str(e)}"
