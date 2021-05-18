# xdr_yara_rule_matching
This Python script must be used as part of Palo Alto Networks' Cortex XDR custom scripts. It allows you to perform a Yara-based file search on Windows machines running the Cortex XDR agent.

For performance reasons, this script embeds a compiled version of the Yara engine as it’s performing several orders of magnitude faster than the Python version of the same engine.

## Installation
The script must be uploaded directly on the Cortex XDR console in Response / Action Center / Scripts Library:
1. Click on the **New Script** button and upload the script.
2. **Script Name** could be any name or description.
3. **Supported OS** must be Windows.
4. **Timeout** could be configured to any value you want but starting with 600 seconds is good practice. Depending on your Yara search, you may need to increase this value at a later stage.
5. **Input** must be set to **Run by entry point** with **main** as an entry point. root_path and yararule are strings.
6. **Output Type** must be **Auto Detect**

And then click on **Create**

## Usage
To run your script on some of your Windows machines, right-click on your script from the **Scripts Library** menu and select **Run**. Copy/Paste your complete Yara rule in the **YARARULE** script parameter and provides the **ROOT_PATH** of your search. 

For example:

***YARARULE***
```
rule string_match
{
	strings:
		$my_text_string = "a string to search"

	condition:
		$my_text_string

}
```

***ROOT_PATH***

`C:\Users\`

## Results
When your action has been launched, you can get its results in ***Action Center / All actions***
