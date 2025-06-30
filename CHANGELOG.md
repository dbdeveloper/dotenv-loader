# Changelog


## [1.0.4] – 2025-06-30

### Added
- New `dry_run` parameter in `load_env()`: allows retrieving the resolved `.env` file path without loading it. Useful for inspection or integration with external tools.

### Changed
- `DOTVERBOSE` is now a boolean-like variable and accepts the following case-insensitive truthy values: `'1'`, `'true'`, `'yes'`, `'on'`, `'ja'`.


## [1.0.3] – 2025-06-27

### Added
- Support for Python 3.13.
- Compatibility with `python-dotenv` 1.1.1.

### Changed
- Dropped support for Python 3.8.

### Fixed
- Updated documentation.


## [1.0.2] – 2025-06-26

### Fixed
- Improved error handling: if a specific `.env` file is explicitly provided via the `dotenv` parameter or the `DOTENV` environment variable, and the file does not exist, a `FileNotFoundError` is now raised.

### Changed
- Renamed the `default_env_file` parameter to `default_env_filename` for improved clarity and consistency.
- Updated CI workflow to test against multiple Python versions (3.8–3.12).

### Added
- Introduced the `DOTVERBOSE` environment variable. When defined and non-empty, it enables verbose output, displaying the path of the selected `.env` file.
- Contribution templates for pull requests and issue reports.
- GitHub Actions workflow for automated PyPI publishing.


## [1.0.1] – 2025-06-19

### Fixed
- Added compatibility with Python 3.8 and newer.


## [1.0.0] – 2025-06-18

### Added
- Initial stable release of `dotenv-loader` with full feature support.

