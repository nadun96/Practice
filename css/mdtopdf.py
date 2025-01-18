import pypandoc

# pypandoc.download_pandoc()


def md_to_pdf(input_file, output_file, pdf_engine="pdflatex"):
    try:
        # Specify the advanced PDF engine
        extra_args = ["--pdf-engine=" + pdf_engine]

        # Convert markdown to PDF using the specified engine
        pypandoc.convert_file(
            input_file, "pdf", outputfile=output_file, extra_args=extra_args
        )
        print(f"Conversion successful! PDF saved at: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_md_file = "css/css_plan.md"
output_pdf_file = "css_plan.pdf"

# Use xelatex as the PDF engine
md_to_pdf(input_md_file, output_pdf_file)
