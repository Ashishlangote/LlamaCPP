def affiliation1(affiliation: str):
    return f"""Here is the affiliation string: {affiliation}. Given an affiliation string representing author information, extract the following elements and create a JSON object with only these keys and their corresponding values found within the string. Do not add any missing or dummy data."""


def affiliation2(affiliation: str, prompt: str):
    return f"""{affiliation}\n{prompt}"""


def affiliation3(text: str):
    json_schema = '''{"authors":[{"author":"","authorPrefix":"","authorSuffix":"","authorDegrees":"","affiliation":[{"affiliationId":"","correspondingAuthor":"","department":"","organization":"","street":"","city":"","state":"","postalCode":"","country":"","email":"","phone":""},{"affiliationId":"","correspondingAuthor":"","department":"","organization":"","street":"","city":"","state":"","postalCode":"","country":"","email":"","phone":""}]}]}'''
    return f"""{text}\nGiven above content is manuscript, accurately identify and categorize information regarding authors and their affiliations. Extract details such as author names, their contributions, and affiliations, including author prefix, suffix, and degrees accompanying the author name. Affiliation details are typically located following the author's name and are indicated by footnote or endnote numbers. Specifically categorize each affiliation into Department, Organization, Street, Postal-code, City, State, and Country if present. Provide a structured output with a list of authors, and for each author, ensure that all affiliations are captured as a list, including all relevant details such as affiliation ID, corresponding author status, department, organization, street, city, state, postal code, country, email, and phone number. Use the provided template for the output JSON structure:{json_schema}"""
