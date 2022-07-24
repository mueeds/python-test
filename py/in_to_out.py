import pprint

input_data = [
{        "text": "Upstream",
          "value": "needs-triage",
          "version": None },
{       "text": "Ubuntu 12.04 ESM (Precise Pangolin)",
        "value": "DNE\n(precise was needs-triage)",
        "version": "12.04" },
{       "text": "Ubuntu 16.04 LTS (Xenial Xerus)",
        "value": "DNE",
        "version": "16.04" },
{     "text": "Ubuntu 18.04 LTS (Bionic Beaver)",
        "value": "DNE",
        "version": "18.04" }
]

output_data = [
    {'Upstream': 'needs-triage'},
    {'Ubuntu 12.04 ESM (Precise Pangolin)': 'DNE\n(precise was needs-triage)'},
    {'Ubuntu 16.04 LTS (Xenial Xerus)': 'DNE'},
    {'Ubuntu 18.04 LTS (Bionic Beaver)': 'DNE'}
]

output_data.append(input_data)

pprint.pprint(output_data)


