# Readme Table of Contents (TOC) Generator
Uses the headings in a .md file to generate a table of contents. The generated TOC is hyperlinked, such that clicking on an entry in the TOC will cause the viewer to navigate to the linked heading in the document. This generator is designed to support .md files that use Github's flavor of the [CommonMark](<https://commonmark.org>) specification of Markdown. <br />
[**Jump to Demo**](<#demo>)<br />
<br />
**Last updated (this file):** 9/9/2020<br />
**Author:** John Mullan<br />

## Usage
### How to Run
```
# Clone this repository
$ git clone https://github.com/jamullan/readme-toc-generator.git

# Place your .md file into your clone of this repository

# Adjust the configuration options if desired (see below)

# Run the program and supply your .md file's name as an argument
$ python3 markdown_toc_generator <your_file.md>

# Copy the text from stdout and paste it in your .md file to serve as a hyperlinked table of contents
```
### Configuration Options
The following configuation options, shown as set to their default values below, can be adjusted inside of the `main()` function in `markdown_toc_generator.py`:<br />
```python
# the highest numbered heading to include in the TOC
DETAIL_LEVEL = 6

# the highest numbered heading to bold
EMPHASIS_LEVEL = 2

# factor by which each level will be indented by
INDENT_FACTOR = 1
```

## Demo
### TOC Generation
![Generating TOC from a .md file](demo_files/TOCGen4X.gif)
### Rendered TOC 
![Rendered TOC](demo_files/TOCRenderedV2.png)
