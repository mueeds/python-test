Write a simple bash script to find text files in the current directory tree and print out the first line from each file.

```Bash
for textfile in /dir; do
    head -n 1 $textfile
done
```

Write a python script to print the Fibonacci series till 100. (Fibonacci series is 1 1 2 3 5 8 …)


```Py
seq = [0,1]
result = 0


while result < 100:

    result = seq[-1] + seq[-2]
    if (result < 100):
        seq.append(result)
print(seq)
```

Write a python script that will convert the input data into the output data
```Py
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
```
```Py
# append entire list
output_data.append(input_data)

# append input into output list
for x in input_data:
    output_data.append(x)
```

Using the answer from the previous question, modify it to return only those keys that start with the word "Ubuntu"

```Py
# append input into output list
for x in input_data:
    output_data.append(x)


# iterate through list
for list in output_data:
    # interate through keys
    for k in list.keys():
        if "Ubuntu" in k:
            print(k)
```
