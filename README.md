# FilterChaos

> **FilterChaos** is a Python script that helps you filter and extract information about bug bounty programs from a Chaos data source and save the results to a CSV file. 

## Requirements

Before using the script, you need to ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python packages can be installed using `pip`:
    ```
    pip install -r requirements.txt
    ```

## Usage

The script can be used from the command line. It takes two main arguments: the name of the bug bounty program you want to filter and an optional "bounty" flag to specify whether you want to filter programs with bounties only. Here's how to run the script:

```
python FilterChaos.py <program_name> [bounty]
```

- `<program_name>`: The name of the bug bounty program you want to search for. You can use the keyword "private" to search for private programs.
- `[bounty]` (optional): If specified as "bounty," the script will filter programs with bounties only. If not specified, all programs matching the name will be included.

**Example Usages:**

- To filter and save all programs with the name "hackerone" that offer bounties:
  ```
  python FilterChaos.py hackerone bounty
  ```

- To filter and save all programs with the name "bugcrowd" (without considering bounties):
  ```bash
  python FilterChaos.py bugcrowd
  ```

- To filter and save all private programs with bounty:
  ```
  python FilterChaos.py private bounty
  ```

## Contributing

We welcome contributions from the community to enhance FilterChaos's capabilities and usability.
Raise a pull request with proper comments of what has changed, for quickly merging into the main branch.

## License
FilterChaos is distributed under the [MIT License](./LICENSE.md). Feel free to use, modify, and distribute it in accordance with the terms outlined in the license.

## Author

👤 **Jayateertha G**

* Twitter: [@jayateerthaG](https://twitter.com/jayateerthaG)
* Github: [@jayateertha043](https://github.com/jayateertha043)

## Show your support
<a href="https://www.buymeacoffee.com/en3EoKG7j" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="50px" width="150px" ></a><br />
Give a ⭐️ if this project helped you!