# Text Sound Changer

A small, configurable tool to transform text using simple pattern rules.

This repository applies user-defined phonetic or orthographic transformation rules to text files. It's designed to be minimal and easy to extend with custom rule files.

## Features

- Apply pattern-based transforms using a rules file
- Simple file-based input/output (`input.txt` -> `output.txt`)
- Rules are editable in `rules.txt` and parsed by `rules.py`

## Repository layout

- `main.py` — program entrypoint: reads `input.txt`, applies rules, writes `output.txt`
- `rules.py` — rule parsing and applying utilities
- `rules.txt` — human-editable rules (see format below)
- `input.txt` — example input text
- `output.txt` — generated output (updated when running)

## Requirements

- Python 3.8+

No external packages are required.


## Rules format

Rules are plain text lines in `rules.txt`. Each cleaned/parsed rule expected by the program follows a simple pattern: an input pattern, an output pattern, and an environment template.

Basic ideas:

- Use `_` in the environment as the placeholder where the input pattern should appear.
- An empty input pattern can be used to match a capture group inside the environment placeholder.

Example rule lines (informal):

- `sh -> ʃ / _`  (replace `sh` with `ʃ` in the given environment)
- `_ -> a / b_c` (replace the captured token in `b_c` environment)

See `rules.py` for the exact parsing logic used by this project.

## Usage

The default behaviour reads `input.txt`, applies rules, and writes `output.txt`.

Run it with:

```bash
python main.py
```

You can edit `input.txt` and `rules.txt` and re-run to see different outputs.

## Example

1. Edit `input.txt` with some text to transform.
2. Edit `rules.txt` to include the rules you'd like to apply.
3. Run `python main.py`.
4. Inspect `output.txt` for results.

## Development notes

- The project is intentionally small — most logic lives in `rules.py` and `main.py`.
- If you modify rule parsing or the applier logic, add quick examples in `input.txt` and `rules.txt` to validate behaviour.

## License

This project is provided as-is; add a license file if you plan to publish it publicly.

Program to apply sound changes in the format x/y/_ where:
x - original sound
y - output sound
_ - environment