import csv
# -----------------------------------------------------------
# converts a csv file into a dsl
#
# The format of the csv must be in format NAME,DESCRIPTION,RELATIONSHIP NAME, RELATIONSHIP to, DESCRIPTION, TAG(colour)
#
# email:
# github:
# -----------------------------------------------------------

# Change these constants for different default themes
SUPPLIER_FONTSIZE = "50"
RELATIONSHIP_FONTSIZE = "42"
RELATIONSHIP_COLOUR = "#707070"

file_name = input("CSV FILE NAME (include .csv): ")
csv_file = open(file_name, newline='')
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
            continue # this stops the creation of duplicate persons
        f.write("       " +
                row[0] +" = person \""+ row[0]
                + "\" \"" + row[1] + "\"\n")
        prev_name = row[0]

    f.write("       enterprise = enterprise \"Diagram\"{ \n "
            "           group = group \"family\"{"
            "\n")
    # This makes the reader go back to the start of the csv
    csv_file.seek(0)
    reader.__next__()
    for row in reader:
         f.write("               " +
                row[0] +" -> "+ row[3]
                + " \"" + row[2] + "\" \""
                + row[4] + "  "
                + row[5] + "\" \""
                + row[6] + "\" \n")
    f.write("           }\n      }\n   }\n"
            "   views {\n       systemLandscape {\n           include * \n       }\n"
            "       styles { \n"
            "         element Person { \n"
            "             shape person \n"
            "             metadata false \n"
            "             fontSize " + SUPPLIER_FONTSIZE + "\n"
            "       }\n"
            "          relationship Relationship { \n"
            "             fontSize " + RELATIONSHIP_FONTSIZE + "\n"
            "             colour " + RELATIONSHIP_COLOUR +  "\n"                                                           
            "       }\n     }\n     theme default\n   }\n}"
            ""
            )
