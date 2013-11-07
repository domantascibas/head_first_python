
from string import Template
"""Imports the Template module from the standard library's string module. This allows for simple
string-substitution templates."""

def start_response(resp="text/html"):
    """This function takes a single (optional) string as its argument and uses it to create a CGI
    "Content-type" line, with "text/html" as the default"""
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
    """This function takes a string as its argument, opens the header.html file, and returns a 
    header template with a custom title."""
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    """This function takes a string as its argument and creates a footer with links."""
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    """This function takes two arguments, and creates a start for an HTML form with a default POST value.
    The user can specify the URL, where to send the form's data as well as the method to use."""
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    """This function returns the HTML markup which terminates the form and allows the user to
    customize the submit button."""
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    """This function creates an HTML Radio-button with its name and value passed in as func arguments.
    Both are required."""
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def u_list(items):
    """This function creates an unnumbered HTML list from a list passed as an argument.
    It returns a string."""
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    """This function generates header tags (H1, H2, H3, etc) from the text and header level passed as arguments.
    Level 2 is the default. "header_text" argument is required."""
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    """This function wraps the string passed in with <p> tags, and generates an HTML paragraph."""
    return('<p>' + para_text + '</p>')
