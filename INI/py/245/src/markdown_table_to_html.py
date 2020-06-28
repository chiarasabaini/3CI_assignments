__author__ = "Sabaini Chiara 3CI"
__version__ = "1.0 2020-04-22"

MD_DELIM = "|"

def md2html_table(md_text):
    """Returns the code for a html table from a md table
    """
    start_row = '\n\t\t\t<tr>'
    end_row = '\n\t\t\t</tr>'
    start_head_col = '\n\t\t\t\t<th>\n\t\t\t\t\t'
    end_head_col = '\n\t\t\t\t</th>'
    start_col = '\n\t\t\t\t<td>\n\t\t\t\t\t'
    end_col = '\n\t\t\t\t</td>'
    start_html = '\n\t\t<table>'
    end_html = '\n\t\t</table>'
    html = start_html
    
    with open(md_text, 'r', encoding="utf-8") as file:
        count_line = 1
        for line in file:
            line = line.split(MD_DELIM)
            col = ""
            row = ""
            for i in range(1, len(line) - 1):
                if count_line == 1:
                    tmp_col = start_head_col + line[i] + end_head_col
                    col += tmp_col
                else:
                    tmp_col = start_col + line[i] + end_col
                    col += tmp_col
            row = start_row + col + end_row
            html += row
            count_line += 1
            
        html += end_html
        
    return html

def elabora(md_text):
    html_start = '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<link rel="stylesheet" href="..\\styles\\styles.css">\n\t</head>\n\t<body>'
    html_end = '\n\t</body>\n</html>'
    md2html_table(md_text)
    html = html_start + md2html_table(md_text) + html_end
    
    with open("..\\htdocs\\country_data_reduced.html", 'w') as file:
        file.write(html)

if __name__ == "__main__":
    md_text = "..\\docs\\country_data_reduced.md"
    elabora(md_text)