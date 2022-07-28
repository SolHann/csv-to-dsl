import csv
import sys
# -----------------------------------------------------------
# converts a csv file into a dsl
#
# The format of the csv must be:
# Name,Description,Tag,RelationshipName,RelationShipTo,Description,RelationshipTag,
#
# Only Name and RelationshipTo are required. Any other column can be left blank.
#
# Run in command line with a csv file as the argument. Example:
# Python3 main.py example_csv
#
# -----------------------------------------------------------

# Change these constants for different default style.
SUPPLIER_FONTSIZE = "50"
RELATIONSHIP_FONTSIZE = "42"
RELATIONSHIP_COLOUR = "#707070"

file = sys.argv[1]
csv_file = open(file, newline='')
reader = csv.reader(csv_file)

prev_name = ""
name = ""

with open('dsl_code.txt', 'w') as f:
    f.write("workspace {\n"
            "   model {"
            "\n")
    reader.__next__()

    for row in reader:
        name = row[0]
        if prev_name == name:
            continue    # If there are consecutive duplicate names don't create new entities
        f.write("       " +
                row[0] + " = person \"" + row[0]
                + "\" \"" + row[1]  # description
                + "\" \"" + row[2] + "\"\n"  # tag
                )
        prev_name = row[0]

    f.write("       enterprise = enterprise \"Diagram\"{ \n "
            "           group = group \"family\"{"
            "\n")
    # This makes the reader go back to the start of the csv
    csv_file.seek(0)
    reader.__next__()

    for row in reader:
        f.write("               " +
                row[0] + " -> " + row[4]
                + " \"" + row[3] + "\" \""  # Relationship name
                + row[5] + "\" \""  # Description
                + row[6] + "\" \n")  # Tag
    f.write("           }\n      }\n   }\n"
            "   views {\n       systemLandscape "
            "{\n           include * \n       }\n"
            "       styles { \n"
            "         element Person { \n"
            "             shape person \n"
            "             metadata false \n"
            "             fontSize " + SUPPLIER_FONTSIZE + "\n"
            "       }\n"
            "          relationship Relationship { \n"
            "             fontSize " + RELATIONSHIP_FONTSIZE + "\n"
            "             colour " + RELATIONSHIP_COLOUR + "\n"                                                           
            "       }\n     }\n     theme default\n   }\n}"
            ""
            )
