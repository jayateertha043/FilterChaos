import requests
import csv
import sys


url = "https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/main/chaos-bugbounty-list.json"

exclude_keywords = ["hackerone", "bugcrowd", "yeswehack", "hackenproof", "intigriti"]

def get_bug_bounty_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve bug bounty data.")
        return None

def filter_program(program_name, bounty, data):
    matching_programs = []
    for program in data['programs']:
        program_name_lower = program['name'].lower()
        url_lower = program['url'].lower()

        is_private = all(keyword not in url_lower for keyword in exclude_keywords)
        
        if program_name.lower() in program_name_lower or program_name.lower() in url_lower:
            if not is_private:
                if bounty:
                    if program["bounty"]:
                        matching_programs.append(program)
                else:
                    matching_programs.append(program)
        if program_name=="private":
            if is_private:
                if bounty:
                    if program["bounty"]:
                        matching_programs.append(program)
                else:
                    matching_programs.append(program)
    return matching_programs

def write_to_csv(programs, output_filename):
    if not programs:
        print(f"No matching programs found for '{program_name}'")
        return

    with open(output_filename, 'w', newline='') as csv_file:
        fieldnames = ["name","url","bounty","swag","domains"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for program in programs:
            writer.writerow(program)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python FilterChaos.py program")
        sys.exit(1)
    bounty=False
    program_name = sys.argv[1]

    if len(sys.argv) > 2:
        if sys.argv[2].lower() == "bounty":
            bounty = True

    bug_bounty_data = get_bug_bounty_data()

    if bug_bounty_data:
        matching_programs = filter_program(program_name, bounty,bug_bounty_data)
        output_filename = f"{program_name}_bug_bounty_programs.csv"
        write_to_csv(matching_programs, output_filename)
        print(f"Matching programs saved to '{output_filename}'")
