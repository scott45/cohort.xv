
# Split the list
# Loop through the list
# Check if item is already in dictionary and skip
# Return final dictionary


def words(word_to_count):
    string_content = word_to_count.split()

    response = {}
    for item in string_content:

        loop_counter = 0

        # check for items not already added to the final result
        if item not in response:
            # Compare list elements
            item_repeated = 0
            while loop_counter < len(string_content):

                if str(item) == str(string_content[loop_counter]):
                    item_repeated += 1

                loop_counter += 1
            if item in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                response.update({int(item): int(item_repeated)})
            else:
                response.update({item: int(item_repeated)})

    # print(response)
    return response
