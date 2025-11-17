import mammoth

# Define input and output file paths
input_docx = "projet3.docx"
output_md = "projet3.md"

with open(input_docx, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    markdown_content = result.value  # This will be HTML, further conversion to Markdown needed

# (Optional) Further conversion from HTML to Markdown using another library like `markdownify`
# from markdownify import markdownify as md
# markdown_content = md(markdown_content)

with open(output_md, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print(f"'{input_docx}' converted to '{output_md}' successfully (via HTML).")