# Color Picker

This script provides the following functionality:

- Press `Ctrl+C` to stop printing (ensure you are not directly focused on the script).
- Prints the position, ANSI code, hex value, and RGB value.

## Usage

1. Run the script.
2. Keep the terminal or console window in focus, but avoid directly focusing on the script.
3. The script will continuously print the position and corresponding color information.
4. Press `Ctrl+C` to stop the script from running.

## Output Format

The script will output the following information for each position:

- Position: X: {x}, Y: {y}
- ANSI Code: \033[38;5;230m
- Hex Value: {rgbToHex}
- RGB Value: {rgb}
- Color Preview

Please note that the ANSI code may not be displayed in color in all environments, but it represents the color associated with the position.

## Requirements

- Python 3.x
