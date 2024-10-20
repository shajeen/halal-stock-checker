# Halal Stock Checker

This application allows users to check if a given stock is considered halal (permissible) according to Islamic principles. It uses a web scraper to fetch a list of halal stocks and provides a terminal user interface (TUI) for easy interaction.

## Features

- Web scraping of halal stocks from a reliable source
- Terminal user interface for easy stock checking
- Asynchronous stock fetching with progress bar
- Simple and intuitive user interaction

## Installation

1. Clone this repository:
```
git clone https://github.com/shajeen/halal-stock-checker.git
cd halal-stock-checker
```


2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the application using:
```
python tui_checker.py
```


Once the application starts:

1. Wait for the initial stock fetching to complete.
2. Enter a stock name in the input field.
3. Click the "Check Stock" button or press Enter.
4. The result will be displayed in the result area.

## Files

- `tui_checker.py`: Main application file containing the TUI implementation[3].
- `halal_stock.py`: Module for scraping halal stocks from the web[1].
- `requirements.txt`: List of Python dependencies[2].

## Dependencies

- requests: For making HTTP requests
- beautifulsoup4: For parsing HTML content
- textual: For creating the terminal user interface
- tqdm: For displaying progress bars

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
